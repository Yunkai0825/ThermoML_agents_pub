"""Working-memory digest for agent-return envelopes (memory surface).
=====================================================================

Any layer that persists a child-agent envelope (L0 storing L1 returns,
main L0 storing query/analysis child sessions) stores this compact
markdown digest instead of the raw JSON.

Rendering is SINGLE-SOURCED: the body is produced by
``engine_react_helpers.subagent_context_render.render_subagent_payload``
— the same renderer that formats subagent returns for parent contexts —
using the MEMORY-surface ledger abstraction level of the transition pair
(``resolve_ledger_level(pair, "memory")``, default ``summary``: core
blocks as one compact canonical table; verbatim ``data_inspections``,
``core_id_updates``, and ``id_catalog_snapshot`` collapse into a
``*Not stored here: …*`` note — they stay on the machine rail:
``tool_history`` → grounding gate → deterministic final-envelope merge).
Per-pair levels are exposed in each session's engine config under
``SUBAGENT_LEDGER_LEVELS["memory"]``.

This module keeps only the memory-specific envelope handling:

- table labels: the child's nested-section sid (``A#1`` / ``L1#2``,
  via ``resolve_sid_label``) so WORKING-MEMORY tables carry the same id
  as the context render of the same envelope; ids get the ``WM_``
  surface prefix (``WM_L1#2_Table#9`` ≡ context ``L1#2_Table#9``);
  fallback label when no sid resolves: ``abbreviate_key`` on the
  storage key (``L1_query_4`` → ``L1_Q4``)
- the digest header line (``**key** — status · validation badges``)
- validation-report parsing — the child's final ``[UNGROUNDED DATA
  FLAGS]`` block is split from the answer, its findings move into a
  ``**Validation:**`` section, and the verdict (``PASS`` /
  ``FLAGGED(n)``) is returned for the caller's history line.
"""

from __future__ import annotations

import json
import re

__all__ = [
    "abbreviate_key",
    "build_envelope_digest",
    "digest_with_validation",
    "split_ungrounded_flags",
    "parse_final_validation",
]

# Words abbreviated inside storage keys when forming the digest table tag.
_KEY_ABBREVIATIONS = {
    "query": "Q",
    "analysis": "A",
    "main": "M",
    "result": "R",
}


def abbreviate_key(key: str) -> str:
    """Derive the table tag from a storage key: ``L1_query_4`` → ``L1_Q4``.

    Known role words are abbreviated and glued onto a following number;
    everything else passes through unchanged.
    """
    if not isinstance(key, str) or not key.strip():
        raise ValueError("key must be a non-empty string")
    parts = key.strip().split("_")
    out: list[str] = []
    for part in parts:
        short = _KEY_ABBREVIATIONS.get(part.lower())
        if short is not None:
            out.append(short)
        elif out and out[-1] in _KEY_ABBREVIATIONS.values() and part.isdigit():
            out[-1] += part          # "Q" + "4" → "Q4"
        else:
            out.append(part)
    return "_".join(out)


def split_ungrounded_flags(answer: str) -> tuple[str, str]:
    """Split a child answer from its final ``[UNGROUNDED DATA FLAGS]`` block.

    Returns ``(clean_answer, flags_text)``; ``flags_text`` is empty when
    the child's gate left no unresolved findings.
    """
    from ...general_data_grounding_gate import FLAGS_HEADER

    index = answer.find(FLAGS_HEADER)
    if index == -1:
        return answer, ""
    head = answer[:index].rstrip()
    if head.endswith("---"):
        head = head[:-3].rstrip()
    return head, answer[index:]


_FINDING_LINE_RE = re.compile(r"^- \*\*\w+\*\* .+$", re.MULTILINE)


def parse_final_validation(answer: str) -> tuple[str, list[str], str]:
    """Extract the child's final gate state from its answer text.

    Returns ``(clean_answer, unresolved_findings, verdict)``.  The
    findings are the gate's own lines (value, anchor, context), without
    per-finding repair calls — these are UNRESOLVED after the child
    exhausted its in-session gate bounces.
    """
    clean, flags_text = split_ungrounded_flags(answer)
    if not flags_text:
        return clean, [], "PASS"
    findings = [
        line.split("\n")[0].strip()
        for line in _FINDING_LINE_RE.findall(flags_text)
    ]
    if not findings:
        return clean, [], "PASS"
    return clean, findings, f"FLAGGED({len(findings)})"


def _render_validation_section(findings: list[str], verdict: str) -> str:
    if not findings:
        return (
            "**Validation (final in-session gate):** PASS — no unresolved "
            "ungrounded values."
        )
    lines = [
        f"**Validation (final in-session gate):** {verdict} — unresolved "
        "ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if "
        "they matter):",
        "",
    ]
    lines += findings
    return "\n".join(lines)


def build_envelope_digest(envelope: dict | str, *, key: str,
                          tool_name: str = "", pair: str | None = None,
                          label: str = "") -> str:
    """Render the compact working-memory digest for one agent return."""
    return digest_with_validation(envelope, key=key, tool_name=tool_name,
                                  pair=pair, label=label)[0]


def digest_with_validation(envelope: dict | str, *, key: str,
                           tool_name: str = "",
                           pair: str | None = None,
                           label: str = "") -> tuple[str, str]:
    """Render the digest and return ``(markdown, validation_verdict)``.

    ``envelope`` may be the parsed envelope dict or its JSON text; ``pair``
    is the transition-pair settings key (e.g. ``"main/Qi"``) whose
    MEMORY-surface ledger level governs the body.  ``label`` overrides the
    table label for callers that resolve the child sid from an OUTER
    envelope (the inner answer JSON lacks ``_session_dir``); otherwise the
    sid is resolved here, falling back to ``abbreviate_key(key)``.
    Raises ``ValueError`` on payloads without the common envelope surface
    (``answer``); callers that accept free-text answers should catch it
    and store the raw text.
    """
    from ...general_argo_engine_helpers.engine_react_helpers.subagent_context_render import (
        active_parent_label,
        render_subagent_payload,
        resolve_ledger_level,
        resolve_sid_label,
    )

    if isinstance(envelope, str):
        try:
            envelope = json.loads(envelope.strip())
        except (json.JSONDecodeError, ValueError) as exc:
            raise ValueError(f"envelope for {key!r} is not JSON") from exc
    if not isinstance(envelope, dict) or "answer" not in envelope:
        raise ValueError(f"envelope for {key!r} has no answer field")

    answer_text, findings, verdict = parse_final_validation(
        str(envelope["answer"]).strip()
    )
    validation_section = _render_validation_section(findings, verdict)
    badges = [
        f"{name}: {envelope[name]}"
        for name in ("status", "confidence")
        if envelope.get(name)
    ]
    badges.append(f"validation: {verdict}")
    header = f"**{key}**" + " — " + " · ".join(badges)

    # Single-source body render: header badges replace the title/status
    # line; the cleaned answer replaces the flag-bearing one.  Table ids
    # share the context surface's sid label under the WM_ prefix.
    payload = dict(envelope)
    payload["answer"] = answer_text
    payload.pop("status", None)
    payload.pop("confidence", None)
    label = (label or resolve_sid_label(tool_name, payload)
             or abbreviate_key(key))
    body = render_subagent_payload(
        payload,
        tool_name=tool_name or key,
        label=label,
        parent=active_parent_label(),
        ledger_level=resolve_ledger_level(pair, "memory"),
        include_title=False,
        id_prefix="WM_",
    )

    parts = [header, "", body, "", validation_section, ""]
    return "\n".join(parts).rstrip() + "\n", verdict
