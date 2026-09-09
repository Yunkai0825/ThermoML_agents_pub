"""L0 sources block validator — deterministic enrichment of minimal refs.
==========================================================================

Post-answer ``id_alignment_processor`` for L0 orchestrators running the
answer-only ID branch (``include_run_record=False``): the branch reads the
plain answer and emits MINIMAL source references (``lit_num_id``/``doi`` +
``block`` [+ ``BLKsubsys_id``]).  This validator then:

1. resolves each reference against the authoritative block registries
   (existence + canonical DOI↔GLOBlit pairing) — broken references bounce
   back to a tool-free correction call (≤2 rounds) with the available
   blocks for that literature listed;
2. builds a heavily compacted card per block (ranges/counts only — never
   row data);
3. runs a bounded review pass that reads ONLY the answer + cards (+ notes
   on pruned/failed references) and per card decides: ``keep`` (write the
   final ``description``), ``discard`` (block resolved but is irrelevant —
   accidental fit), or ``refine`` (wrong pick — the reference bounces back
   through the correction loop for re-selection, bounded cycles);
4. deterministically verifies every decision matches the cards
   character-for-character; final entries are rebuilt from the cards.

The raw tool record is never rendered — the token cost of this stage is
answer + cards.
"""

from __future__ import annotations

import json
import logging
import sqlite3
from pathlib import Path
from typing import Any

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    lit_num_id_for_doi,
    require_block_id,
    require_block_local_id,
    require_global_id,
)

from ..L1_workers.core_id_management import (
    CoreIDValidationError,
    _fetch_authoritative_block,
    registry_db_path,
)
from ....general_db_query_engine.general_argo_engine_helpers.json_answer_guard import (
    guard_json_answer,
)

log = logging.getLogger("L0-sources-validator")

_ALLOWED_REF_FIELDS = {"doi", "lit_num_id", "block", "BLKsubsys_id"}
_REVIEW_FIELDS = {"doi", "lit_num_id", "block", "BLKsubsys_id", "action", "description"}
_REVIEW_ACTIONS = {"keep", "discard", "refine"}
_MAX_RESOLUTION_ROUNDS = 3      # initial + 2 corrections
_MAX_REVIEW_ROUNDS = 2          # schema/identity retries inside one review call
_MAX_REVIEW_CYCLES = 2          # describe → refine → describe passes

_CORRECTION_SYSTEM = """
You are correcting minimal ThermoML source references for a post-answer
block validator. You have no tools; use only the validation observation
and the answer text. Return exactly {"sources": [...]} where each item
carries only: `lit_num_id` (GLOBlit_N) and/or `doi`, plus `block`
(PROPblock_N / RXNblock_N), plus `BLKsubsys_id` only when the answer
explicitly cites that subsystem. Remove a reference the answer does not
support. Never invent or repair identifiers beyond what the observation
states. Output one JSON object only, without prose or code fences.
""".strip()

_DESCRIPTION_SYSTEM = """
You are the source reviewer for a ThermoML post-answer block validator.
You have no tools. You receive the completed answer, one authoritative
compact card per candidate source block (identifiers, system, ranges,
counts — no row data), and notes on references already pruned or failed.
Return exactly {"sources": [...]} with ONE item per card, fields exactly:
doi, lit_num_id, block, BLKsubsys_id, action, description. Copy doi,
lit_num_id, block, and BLKsubsys_id from the card character-for-character
(keep null when the card shows null). Set `action` per card:
- "keep" — the block genuinely backs the answer; `description` is 1–2
  sentences on what it contributes, quoting numbers only if they appear
  in the card or the answer.
- "discard" — the block resolved but does not support this answer
  (accidental fit with an irrelevant block); `description` states in one
  sentence why it is irrelevant.
- "refine" — the answer needs a block from this literature but this one
  is the wrong pick; `description` states what the correct block should
  contain so the reference can be re-selected.
Output one JSON object only, without prose or code fences.
""".strip()


def _available_blocks(lit_num_id: str) -> list[str]:
    """Block numbers registered under one literature, both registries."""
    blocks: set[str] = set()
    for registry_key in ("PM_REGISTRY", "RXN_REGISTRY"):
        path = registry_db_path(registry_key)
        if not Path(path).is_file():
            continue
        connection = sqlite3.connect(path)
        try:
            rows = connection.execute(
                "SELECT block_number FROM block_registry WHERE lit_num_id = ?",
                (lit_num_id,),
            ).fetchall()
        finally:
            connection.close()
        blocks.update(row[0] for row in rows)
    return sorted(blocks)


def _compact_card(parsed: dict, lit_num_id: str) -> dict:
    """Ranges/counts-only card from an authoritative registry block."""
    card = {
        "doi": parsed["doi"],
        "lit_num_id": lit_num_id,
        "block": parsed["block_number"],
        "BLKsubsys_id": parsed["BLKsubsys_id"],
        "block_type": parsed["block_type"],
        "system_type": parsed["system_type"],
        "n_datapoints": parsed["n_datapoints"],
        "compounds": [item["name"] for item in parsed["compounds"]],
        "properties": [
            {
                "name": item["name"],
                "min": item["range_min"],
                "max": item["range_max"],
                "method": item.get("method_standard") or item.get("method_custom"),
            }
            for item in parsed["properties"]
        ],
        "variables": [
            {"name": item["name"], "min": item["range_min"], "max": item["range_max"]}
            for item in parsed["variables"]
        ],
        "constraints": [
            {"name": item["name"], "value": item["value"]}
            for item in parsed["constraints"]
        ],
    }
    if parsed.get("reaction_type"):
        card["reaction_type"] = parsed["reaction_type"]
    return card


def _resolve_refs(sources: list) -> tuple[list[dict], list[str]]:
    """Resolve minimal refs to compact cards; collect problem strings."""
    cards: list[dict] = []
    seen: set[tuple] = set()
    problems: list[str] = []
    for index, entry in enumerate(sources):
        where = f"sources[{index}]"
        if not isinstance(entry, dict):
            problems.append(f"{where} must be an object")
            continue
        extra = set(entry) - _ALLOWED_REF_FIELDS
        if extra:
            problems.append(
                f"{where} carries non-minimal fields {sorted(extra)}; allowed: "
                f"{sorted(_ALLOWED_REF_FIELDS)}"
            )
            continue
        if "block" not in entry or (
            "lit_num_id" not in entry and "doi" not in entry
        ):
            problems.append(
                f"{where} requires block plus lit_num_id and/or doi"
            )
            continue
        try:
            if entry.get("lit_num_id") is not None:
                lit_num_id = require_global_id("lit_num_id", entry["lit_num_id"])
            else:
                lit_num_id = lit_num_id_for_doi(
                    entry["doi"], allow_unregistered=True,
                )
                if not lit_num_id:
                    problems.append(
                        f"{where}: doi {entry['doi']!r} is not in the "
                        "literature registry"
                    )
                    continue
            block_number = require_block_id(entry["block"])
            subsystem_id = (
                require_block_local_id("subsys", entry["BLKsubsys_id"])
                if entry.get("BLKsubsys_id") is not None else None
            )
        except (TypeError, ValueError) as exc:
            problems.append(f"{where}: {exc}")
            continue
        key = (lit_num_id, block_number, subsystem_id)
        if key in seen:
            continue
        try:
            parsed = _fetch_authoritative_block(
                lit_num_id, block_number, subsystem_id,
            )
        except CoreIDValidationError as exc:
            hint = ", ".join(_available_blocks(lit_num_id)[:20]) or "none"
            problems.append(
                f"{where}: {exc} — blocks registered under {lit_num_id}: {hint}"
            )
            continue
        seen.add(key)
        cards.append(_compact_card(parsed, lit_num_id))
    return cards, problems


def _minimal_refs_schema() -> dict:
    return {
        "sources": [
            {
                "lit_num_id": "GLOBlit_N and/or doi",
                "doi": "10.xxxx/... (optional when lit_num_id given)",
                "block": "PROPblock_N | RXNblock_N",
                "BLKsubsys_id": "BLKsubsys_N (only when explicitly cited)",
            }
        ]
    }


def _correct_refs(
    *,
    client: Any,
    answer: str,
    sources: list,
    problems: list[str],
    label: str,
    max_tokens: int,
) -> list:
    prompt = (
        "## Working agent answer\n"
        + answer
        + "\n\n## Current minimal source references\n"
        + json.dumps({"sources": sources}, indent=2, ensure_ascii=False)
        + "\n\n## Validation observation\n- "
        + "\n- ".join(problems)
        + "\n\n## Required JSON schema\n"
        + json.dumps(_minimal_refs_schema(), indent=2, ensure_ascii=False)
    )
    raw = client.call(prompt, _CORRECTION_SYSTEM, max_tokens=max_tokens)
    parsed, _ = guard_json_answer(
        raw,
        client=client,
        label=f"{label}-sources-correction",
        schema=_minimal_refs_schema(),
        max_retries=1,
        max_tokens=max_tokens,
    )
    if not isinstance(parsed, dict) or not isinstance(parsed.get("sources"), list):
        raise CoreIDValidationError(
            "sources correction did not return a sources array"
        )
    return parsed["sources"]


def _resolve_with_corrections(
    sources: list,
    *,
    client: Any,
    answer: str,
    label: str,
    max_tokens: int,
    pruned_notes: list[str],
    strict: bool,
) -> list[dict]:
    """Resolution loop with LLM correction rounds; failures land in notes.

    ``strict`` (initial refs) raises on exhaustion; refine cycles degrade
    to dropping the unresolved refs so kept entries survive.
    """
    cards: list[dict] = []
    problems: list[str] = []
    for round_index in range(_MAX_RESOLUTION_ROUNDS):
        cards, problems = _resolve_refs(sources)
        if not problems:
            return cards
        pruned_notes.extend(problems)
        if round_index == _MAX_RESOLUTION_ROUNDS - 1:
            break
        log.info(
            "[%s] source refs: %d problem(s), correction round %d",
            label, len(problems), round_index + 1,
        )
        sources = _correct_refs(
            client=client,
            answer=answer,
            sources=sources,
            problems=problems,
            label=label,
            max_tokens=max_tokens,
        )
    if strict:
        raise CoreIDValidationError(
            "source references failed registry validation: "
            + "; ".join(problems)
        )
    log.warning(
        "[%s] unresolved refs dropped after corrections: %s",
        label, "; ".join(problems),
    )
    return cards


def _verify_review_decisions(decisions: object, cards: list[dict]) -> list[str]:
    """Deterministic identity/shape check of review decisions vs the cards."""
    problems: list[str] = []
    if not isinstance(decisions, list):
        return ["sources must be an array"]
    expected = {
        (card["lit_num_id"], card["block"], card["BLKsubsys_id"]): card
        for card in cards
    }
    seen: set[tuple] = set()
    for index, entry in enumerate(decisions):
        where = f"sources[{index}]"
        if not isinstance(entry, dict) or set(entry) != _REVIEW_FIELDS:
            problems.append(
                f"{where} fields must be exactly {sorted(_REVIEW_FIELDS)}"
            )
            continue
        key = (entry["lit_num_id"], entry["block"], entry["BLKsubsys_id"])
        card = expected.get(key)
        if card is None:
            problems.append(f"{where} does not match any validated card: {key}")
            continue
        if key in seen:
            problems.append(f"{where} duplicates the decision for {key}")
            continue
        if entry["doi"] != card["doi"]:
            problems.append(
                f"{where}.doi must be {card['doi']!r} (from the card)"
            )
        if entry["action"] not in _REVIEW_ACTIONS:
            problems.append(
                f"{where}.action must be one of {sorted(_REVIEW_ACTIONS)}"
            )
        if not isinstance(entry["description"], str) or not entry["description"].strip():
            problems.append(f"{where}.description must be non-empty text")
        seen.add(key)
    missing = set(expected) - seen
    for key in sorted(missing, key=str):
        problems.append(f"missing decision for validated card {key}")
    return problems


def _describe_and_review(
    *,
    client: Any,
    answer: str,
    cards: list[dict],
    pruned_notes: list[str],
    label: str,
    max_tokens: int,
) -> tuple[list[dict], list[str], list[tuple[dict, str]]]:
    """Review each card against the answer: keep / discard / refine.

    Returns ``(kept_entries, discard_notes, refine_requests)``; a refine
    request pairs the rejected card with the reviewer's note.  Kept
    entries are rebuilt from the cards, so identity is guaranteed.
    """
    schema = {
        "sources": [
            {
                "doi": "copied from card",
                "lit_num_id": "copied from card",
                "block": "copied from card",
                "BLKsubsys_id": None,
                "action": "keep | discard | refine",
                "description": (
                    "keep: contribution to the answer · discard: why the "
                    "block is irrelevant · refine: what the right block "
                    "should contain"
                ),
            }
        ]
    }
    pruned_section = (
        "\n\n## Previously pruned or failed references\n- "
        + "\n- ".join(pruned_notes)
        if pruned_notes else ""
    )
    observation = ""
    decisions: object = None
    problems: list[str] = []
    for _ in range(_MAX_REVIEW_ROUNDS):
        prompt = (
            "## Working agent answer\n"
            + answer
            + "\n\n## Authoritative block cards\n"
            + json.dumps({"cards": cards}, indent=2, ensure_ascii=False)
            + pruned_section
            + observation
            + "\n\n## Required JSON schema\n"
            + json.dumps(schema, indent=2, ensure_ascii=False)
        )
        raw = client.call(prompt, _DESCRIPTION_SYSTEM, max_tokens=max_tokens)
        parsed, _ = guard_json_answer(
            raw,
            client=client,
            label=f"{label}-sources-review",
            schema=schema,
            max_retries=1,
            max_tokens=max_tokens,
        )
        decisions = parsed.get("sources") if isinstance(parsed, dict) else None
        problems = _verify_review_decisions(decisions, cards)
        if not problems:
            break
        observation = (
            "\n\n## Validation observation (fix and resubmit)\n- "
            + "\n- ".join(problems)
        )
    else:
        raise CoreIDValidationError(
            "source review failed identity verification: "
            + "; ".join(problems)
        )
    by_key = {
        (card["lit_num_id"], card["block"], card["BLKsubsys_id"]): card
        for card in cards
    }
    kept: list[dict] = []
    discard_notes: list[str] = []
    refine_requests: list[tuple[dict, str]] = []
    for entry in decisions:
        card = by_key[(entry["lit_num_id"], entry["block"], entry["BLKsubsys_id"])]
        note = entry["description"].strip()
        if entry["action"] == "keep":
            kept.append({
                "doi": card["doi"],
                "lit_num_id": card["lit_num_id"],
                "block": card["block"],
                "BLKsubsys_id": card["BLKsubsys_id"],
                "description": note,
            })
        elif entry["action"] == "discard":
            discard_notes.append(
                f"discarded {card['lit_num_id']}/{card['block']}: {note}"
            )
        else:
            refine_requests.append((card, note))
    return kept, discard_notes, refine_requests


def validate_and_enrich_l0_sources(
    *,
    id_alignment: dict[str, Any],
    client: Any,
    id_alignment_schema: dict[str, Any],
    id_alignment_prompt: str,
    answer: str,
    core_claims_evaluation: dict[str, Any],
    completed_run_record: str,
    label: str,
    max_tokens: int,
    engine_hooks: Any = None,
) -> dict[str, Any]:
    """Post-answer processor: minimal refs → validated, described sources."""
    if "sources" not in id_alignment:
        return id_alignment
    sources = id_alignment["sources"]
    if not isinstance(sources, list):
        raise TypeError("id_alignment.sources must be an array")
    if not sources:
        return {**id_alignment, "sources": []}

    pruned_notes: list[str] = []
    kept: list[dict] = []
    handled: set[tuple] = set()
    pending = sources
    for cycle in range(_MAX_REVIEW_CYCLES):
        cards = _resolve_with_corrections(
            pending,
            client=client,
            answer=answer,
            label=label,
            max_tokens=max_tokens,
            pruned_notes=pruned_notes,
            strict=(cycle == 0),
        )
        cards = [
            card for card in cards
            if (card["lit_num_id"], card["block"], card["BLKsubsys_id"])
            not in handled
        ]
        if not cards:
            break
        kept_now, discard_notes, refine_requests = _describe_and_review(
            client=client,
            answer=answer,
            cards=cards,
            pruned_notes=pruned_notes,
            label=label,
            max_tokens=max_tokens,
        )
        kept.extend(kept_now)
        pruned_notes.extend(discard_notes)
        handled.update(
            (card["lit_num_id"], card["block"], card["BLKsubsys_id"])
            for card in cards
        )
        if not refine_requests:
            break
        if cycle == _MAX_REVIEW_CYCLES - 1:
            log.warning(
                "[%s] %d refine request(s) expired at cycle limit",
                label, len(refine_requests),
            )
            break
        refine_sources: list[dict] = []
        refine_problems: list[str] = []
        for card, note in refine_requests:
            hint = ", ".join(_available_blocks(card["lit_num_id"])[:20]) or "none"
            refine_problems.append(
                f"reviewer rejected {card['lit_num_id']}/{card['block']}: "
                f"{note} — blocks registered under {card['lit_num_id']}: {hint}"
            )
            ref = {"lit_num_id": card["lit_num_id"], "block": card["block"]}
            if card["BLKsubsys_id"]:
                ref["BLKsubsys_id"] = card["BLKsubsys_id"]
            refine_sources.append(ref)
            pruned_notes.append(
                f"refined away {card['lit_num_id']}/{card['block']}: {note}"
            )
        pending = _correct_refs(
            client=client,
            answer=answer,
            sources=refine_sources,
            problems=refine_problems,
            label=label,
            max_tokens=max_tokens,
        )
    log.info(
        "[%s] sources validated: %d kept, %d pruned note(s)",
        label, len(kept), len(pruned_notes),
    )
    return {**id_alignment, "sources": kept}
