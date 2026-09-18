"""
Subagent-answer context rendering.
==================================
Renders a subagent tool's JSON envelope as organized markdown for the
PARENT agent's context window only.  Every recorded rail keeps the
validated JSON verbatim: ``tool_history[*].result_full``, the tool
anchors (``result_full=``), working-memory instrumentation, the
grounding-gate inspection harvest, and the post-run funnels all see the
same wrapped JSON string as before.  The parent-visible copy keeps the
configured ``<subagent_answer>...</subagent_answer>`` context boundary, but
its body is organized Markdown rather than JSON.

Applies to every cross-layer transfer that flows through a tool marked
with ``mark_subagent_answer_tool``: main←Q/A delegation envelopes,
analysis←query_thermoml / align_compositions relays, query-L0←L1_query,
L1←L2 leaf evaluators, and menu-forwarded variants.

Rendering scheme (user-specified):
- generated return title at ``###`` (nests under the context's ``## User``)
- answer / verdict headings demoted two levels; their tables rewritten
  canonically with a bold caption ``**<label>_Table#x_(<parent>_<label>_
  Answer):**`` and a ``row_id`` column ``<label>_Table#x_Row#N``
- core_blocks_found / data_inspections in ``####`` ledger sections of
  fenced ```` ```ledger ```` blocks with bold captions
  (``..._CoreBLK`` / ``..._INSP``)
- all column names wrapped in ``*...*``; every table value wrapped in
  ``「…」`` except the leading row-id column
- one table counter per rendered result (answer → sources → fits →
  ledgers), advanced AS-IF-FULL: dropped ledger sections still consume
  their numbers, so ``Table#9`` denotes the same table at every level

Cross-surface table identity:
- the label is the child's nested-section sid in ``#`` form (``A#1``,
  ``Q#2``, ``L1#3`` — :func:`resolve_sid_label`); the CONTEXT surface and
  the MEMORY surface (working-memory digests, ``envelope_memory_digest``)
  therefore assign the SAME ``<label>_Table#x`` id to the same table
- memory-surface ids carry a ``WM_`` prefix (surface marker only:
  ``WM_A#1_Table#3`` ≡ ``A#1_Table#3``)
- already-canonical tables quoted inside an answer are CHAINED, not
  renumbered: each hop prefixes its own label (``A#1_L1#2_Table#9``,
  deeper nests accumulate ``A#1_Q#1_L1#1_L2#1_...``); a leading ``WM_``
  is stripped when chaining
- fallback labels when no recorder / unresolvable sid: the per-run tool
  ordinal (context, ``Q#2``-style) or the abbreviated storage key
  (memory, ``L1_Q1``-style)

Ledger abstraction level (per transition pair, default ``full``):
- ``full``    — verbatim ``CoreBLK`` / ``INSP`` ledger fences plus the
  catalog-machinery sections (core_id_updates / id_catalog_snapshot)
- ``summary`` — core blocks as one compact canonical table; inspections
  and catalog machinery collapse into a ``*Not stored here: …*`` note
- ``none``    — every ledger collapses into the note

Levels are resolved per boundary from the session's engine config field
``SUBAGENT_LEDGER_LEVELS = {"context": {pair: level}, "memory": {...}}``
where pair keys are ``main/Qi``, ``main/Ai``, ``main/L1``, ``main/L2``,
``Ai/Qi``, ``Ai/L1``, ``Qi/L1``, ``L1/L2``.  The memory surface (working-
memory digests, see ``envelope_memory_digest``) defaults to ``summary``.

Rendering NEVER raises into the ReAct loop.  A marked-result parse or render
failure fails closed with a short Markdown status notice; raw JSON remains on
the audit rails but is never delivered to the parent context.
"""
from __future__ import annotations

import json
import logging
import re
from typing import Any, Callable

from ...general_text_context_marker_catalog import (
    ALL_CONTEXT_MARKERS_RE,
    MARKERS,
)

log = logging.getLogger("thermoml_engine")

# Child-label shorthand per launching tool; unknown tools fall back to "T".
_SHORT_BY_TOOL = {
    "run_query_agent": "Q",
    "run_analysis_agent": "A",
    "query_thermoml": "Q",
    "query_thermoml_parallel": "QP",
    "run_query_agents_parallel": "QP",
    "run_parallel_subagents": "PAR",
    "L1_query": "L1",
    "align_compositions": "AL",
    "L2_comp_eval": "L2",
    "L2_meas_eval": "L2",
    "L2_ref_eval": "L2",
    "L2_prop_eval": "L2",
}

# Envelope keys consumed by dedicated sections (leftovers render generically).
_HANDLED_KEYS = {
    "answer", "core_claims", "confidence", "sources", "fit_results",
    "data_inspections", "id_catalog_snapshot", "follow_up_suggestions",
    "core_id_updates", "core_blocks_found", "verdict", "output_files",
    "iterations", "elapsed_seconds", "tool_count", "timed_out", "status",
    "agent", "summary", "_question", "_session_dir", "session_dir",
}

_SEP_RE = re.compile(r"\|(?:\s*:?-+:?\s*\|)+")

# ── ledger abstraction levels (per transition pair) ────────────

LEDGER_LEVELS = ("full", "summary", "none")

# Layer tokens used in transition-pair settings keys.  Display shorthand
# is NOT the layer: query_thermoml labels as "Q" but relays an L1 worker.
_CHILD_LAYER_BY_TOOL = {
    "run_query_agent": "Qi",
    "run_query_agents_parallel": "Qi",
    "run_analysis_agent": "Ai",
    "query_thermoml": "L1",
    "query_thermoml_parallel": "L1",
    "align_compositions": "L1",
    "L1_query": "L1",
}
_PARENT_LAYER = {"Main": "main", "Query": "Qi", "Analysis": "Ai"}
# Section-sid prefix per child layer token (sids count per prefix).
_SID_PREFIX_BY_LAYER = {"Qi": "Q", "Ai": "A", "L1": "L1", "L2": "L2"}


def _short_for(tool_name: str) -> str:
    if tool_name in _SHORT_BY_TOOL:
        return _SHORT_BY_TOOL[tool_name]
    if tool_name.startswith("L2_"):
        return "L2"
    if tool_name.startswith("L1_"):
        return "L1"
    return "T"


def _sid_label(sid: str) -> str:
    """Display form of a nested-section sid: ``A_1`` → ``A#1``."""
    head, _, n = sid.rpartition("_")
    return f"{head}#{n}" if head and n.isdigit() else sid


def _parent_label() -> str:
    """Receiving-agent identity for captions: active nested section sid
    (``L1_1`` → ``L1#1``) when inside one, else the recording agent's name."""
    try:
        from ...general_hooks_management_helpers.general_context_hooks.history_tracking_hooks import (
            get_active_history_recorder,
        )
        rec = get_active_history_recorder()
        agent, section = rec.context_identity()
    except Exception:
        return "Agent"
    if section:
        return _sid_label(section)
    lowered = (agent or "").lower()
    if "main" in lowered:
        return "Main"
    if lowered.startswith("query"):
        return "Query"
    if lowered.startswith("analysis"):
        return "Analysis"
    return agent or "Agent"


def active_parent_label() -> str:
    """Public alias: receiving-agent identity for table captions."""
    return _parent_label()


def resolve_sid_label(tool_name: str, payload: dict,
                      result_text: str = "") -> str:
    """Cross-surface table label from the child's nested-section sid
    (``A#1`` / ``L1#2``).  Returns "" when no recorder is active or the
    sid is unresolvable — callers fall back to their surface-local label
    so the CONTEXT and MEMORY renders of one envelope share ids whenever
    a sid exists."""
    try:
        from ...general_hooks_management_helpers.general_context_hooks.history_tracking_hooks import (
            get_active_history_recorder,
        )
        rec = get_active_history_recorder()
        layer = _CHILD_LAYER_BY_TOOL.get(tool_name, "")
        if not layer:
            if tool_name.startswith("L2_"):
                layer = "L2"
            elif tool_name.startswith("L1_"):
                layer = "L1"
        sid = rec.resolve_child_sid(
            tool_name, payload, result_text=result_text,
            layer_prefix=_SID_PREFIX_BY_LAYER.get(layer, ""))
        return _sid_label(sid) if sid else ""
    except Exception:
        return ""


def transition_pair(tool_name: str, parent: str) -> str:
    """Canonical settings key for one transfer boundary, e.g. ``Ai/L1``.

    ``parent`` is a :func:`_parent_label` value (``Main`` / ``Query`` /
    ``Analysis`` or a nested section sid such as ``L1_2``); the child
    layer comes from the launching tool.
    """
    child = _CHILD_LAYER_BY_TOOL.get(tool_name)
    if child is None:
        if tool_name.startswith("L2_"):
            child = "L2"
        elif tool_name.startswith("L1_"):
            child = "L1"
        else:
            child = _short_for(tool_name)
    if parent in _PARENT_LAYER:
        parent_layer = _PARENT_LAYER[parent]
    else:
        head = re.split(r"[#_]", parent or "", maxsplit=1)[0]   # "L1#2" → "L1"
        parent_layer = {"L1": "L1", "L2": "L2", "Q": "Qi", "A": "Ai"}.get(
            head, parent or "Agent")
    return f"{parent_layer}/{child}"


def resolve_ledger_level(pair: str | None, surface: str = "context") -> str:
    """Ledger abstraction level for one transition pair (never raises).

    ROOT PRECEDENCE: the ROOT session's ``SUBAGENT_LEDGER_LEVELS`` map
    (claimed by the outermost ``with_engine_config`` runner) governs the
    whole session tree, overriding the nested subagent configs' own maps.
    Without a root claim, the active config's map applies.  Shape:
    ``{"context": {pair: level}, "memory": {pair: level}}``; missing
    pair → the surface's ``default`` key → built-in default
    (``context``: full, ``memory``: summary).
    """
    default = "summary" if surface == "memory" else "full"
    try:
        from ..engine_config import get_config, get_root_ledger_levels
        levels = get_root_ledger_levels()
        if levels is None:
            levels = getattr(get_config(), "SUBAGENT_LEDGER_LEVELS", None) or {}
        surf = levels.get(surface) or {}
        level = surf.get(pair or "", surf.get("default", default))
        return level if level in LEDGER_LEVELS else default
    except Exception:
        return default


def _child_label(tool_name: str, tool_history: list) -> str:
    """Per-run ordinal label ("Q#2"): counts prior history entries whose
    tool maps to the same shorthand (the current call is already appended
    in the sync loop; guard the async loop's pre-append call ordering)."""
    short = _short_for(tool_name)
    seen = sum(
        1 for entry in tool_history
        if isinstance(entry, dict) and _short_for(str(entry.get("tool", ""))) == short
    )
    return f"{short}#{max(seen, 1)}"


# ── low-level markdown helpers ─────────────────────────────────

def _esc(value: object) -> str:
    text = "—" if value is None else str(value)
    return text.replace("|", "\\|").replace("\n", "; ")


def _pipe_row(cells: list) -> str:
    return "| " + " | ".join(cells) + " |"


def _pipe_table(header: list, rows: list) -> list:
    """Canonical table: italic *headers*; values 「…」-wrapped except the
    leading row-id column."""
    body = [_pipe_row([_esc(r[0]), *[f"「{_esc(c)}」" for c in r[1:]]])
            for r in rows]
    return [_pipe_row([f"*{_esc(h)}*" for h in header]),
            "|" + "|".join("---" for _ in header) + "|",
            *body]


class _TableCounter:
    """One id sequence per rendered envelope; ``prefix`` is the surface
    marker (``WM_`` on the memory surface, "" in context)."""

    def __init__(self, label: str, prefix: str = "") -> None:
        self.label = label
        self.prefix = prefix
        self.n = 0

    def next_id(self) -> str:
        self.n += 1
        return f"{self.prefix}{self.label}_Table#{self.n}"


# Already-canonical ids quoted inside an answer (``#`` form or the
# legacy ``_`` form); chained instead of renumbered.
_CANON_TID = r"(?:WM_)?[\w#]+_Table[#_]\d+"
_CANON_CAPTION_RE = re.compile(rf"\*\*({_CANON_TID})_\((.+)\):\*\*$")
_CANON_ROW_START_RE = re.compile(rf"^(\s*\|\s*)({_CANON_TID}_Row[#_]\d+)(?=\s*\|)")


def _chain_id(canon_id: str, tc: _TableCounter) -> str:
    """Prefix a quoted canonical id with this envelope's label
    (``L1#2_Table#9`` → ``A#1_L1#2_Table#9``); any embedded ``WM_``
    surface marker is stripped, the current surface's re-applied."""
    core = canon_id[3:] if canon_id.startswith("WM_") else canon_id
    return f"{tc.prefix}{tc.label}_{core}"


def _canonicalize_text(md: str, tc: _TableCounter, parent: str,
                       kind: str = "Answer") -> str:
    """Demote headings two levels; rewrite inline tables to canonical
    row/column form with a generated bold table-identifier caption.
    Quoted ALREADY-canonical tables (captions / row-id cells, fenced or
    not) are chained via :func:`_chain_id` — never renumbered, values
    left untouched."""
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    in_fence = False
    while i < len(lines):
        line = lines[i]
        cap = _CANON_CAPTION_RE.match(line.strip())
        if cap:
            out.append(f"**{_chain_id(cap.group(1), tc)}_({cap.group(2)}):**")
            i += 1
            continue
        row = _CANON_ROW_START_RE.match(line)
        if row:
            out.append(f"{row.group(1)}{_chain_id(row.group(2), tc)}"
                       f"{line[row.end(2):]}")
            i += 1
            continue
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue
        if not in_fence and line.startswith("#"):
            out.append("##" + line)
            i += 1
            continue
        if (not in_fence and line.lstrip().startswith("|")
                and i + 1 < len(lines)
                and _SEP_RE.fullmatch(lines[i + 1].strip())):
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            if any(_CANON_ROW_START_RE.match(lines[k]) for k in range(i + 2, j)):
                out.append(line)           # already-canonical table: keep
                out.append(lines[i + 1])   # header/sep, chain row ids only
                for k in range(i + 2, j):
                    m = _CANON_ROW_START_RE.match(lines[k])
                    out.append(f"{m.group(1)}{_chain_id(m.group(2), tc)}"
                               f"{lines[k][m.end(2):]}" if m else lines[k])
                i = j
                continue
            header = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            data = [[c.strip() for c in lines[k].strip().strip("|").split("|")]
                    for k in range(i + 2, j)]
            tid = tc.next_id()
            if out and out[-1].strip():
                out.append("")
            out += [f"**{tid}_({parent}_{tc.label}_{kind}):**", "",
                    *_pipe_table(["row_id", *header],
                                 [[f"{tid}_Row#{n}", *r]
                                  for n, r in enumerate(data, 1)])]
            i = j
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


# ── ledger fences ──────────────────────────────────────────────

def _insp_ledger(insp: dict, tc: _TableCounter, parent: str) -> list:
    tid = tc.next_id()
    cols = insp.get("columns", []) or []
    rows = insp.get("rows_shown", []) or []
    meta1 = (f"lit_num_id: {insp.get('lit_num_id')} | doi: {insp.get('doi')} | "
             f"block: {insp.get('block_number')}")
    if insp.get("BLKsubsys_id"):
        meta1 += f" | BLKsubsys_id: {insp['BLKsubsys_id']}"
    meta2 = (f"table_mode: {insp.get('table_mode')} | "
             f"inspection_id: {insp.get('inspection_id')} | rows_shown: {len(rows)}")
    body = _pipe_table(
        ["row_id", *cols],
        [[f"{tid}_Row#{i}", *[r.get(c, "") for c in cols]]
         for i, r in enumerate(rows, 1)],
    )
    return ["```ledger", f"**{tid}_({parent}_{tc.label}_INSP):**", meta1, meta2, "",
            *body, "```", ""]


def _blk_structural_rows(blk: dict, tid: str) -> list:
    by_org = {c.get("org_num"): c.get("name")
              for c in blk.get("compounds", []) if isinstance(c, dict)}
    owner_phase = {p.get("owner_id"): p.get("phase")
                   for p in blk.get("phases", []) if isinstance(p, dict)}
    rows: list = []

    def phase_of(item: dict, owner_key: str) -> str:
        ph = item.get("phase")
        if isinstance(ph, dict) and ph.get("phase"):
            return ph["phase"]
        return owner_phase.get(item.get(owner_key), "—") or "—"

    for c in blk.get("constraints", []) or []:
        rows.append(["constraint", f"{c.get('BLKconstr_id')}/{c.get('constr_num_id')}",
                     c.get("name"),
                     f"value={c.get('value')} · phase={phase_of(c, 'BLKconstr_id')}"])
    for v in blk.get("variables", []) or []:
        name = v.get("name", "")
        if v.get("component_org_num"):
            name += f" of {by_org.get(v['component_org_num'], v['component_org_num'])}"
        rng = v.get("range") or {}
        rows.append(["variable", f"{v.get('BLKvar_id')}/{v.get('var_num_id')}", name,
                     f"range={v.get('range_min')}–{v.get('range_max')} · "
                     f"n_unique={rng.get('n_unique', '—')} · "
                     f"phase={phase_of(v, 'BLKvar_id')}"])
    for p in blk.get("properties", []) or []:
        rng = p.get("range") or {}
        method = p.get("method_standard") or p.get("method_custom") or "—"
        rows.append(["property", f"{p.get('BLKprop_id')}/{p.get('prop_num_id')}",
                     p.get("name"),
                     f"method={method} ({p.get('meas_num_id')}) · "
                     f"range={p.get('range_min')}–{p.get('range_max')} · "
                     f"mean={rng.get('mean', '—')} · n={rng.get('n', '—')} · "
                     f"phase={phase_of(p, 'BLKprop_id')}"])
    return [[f"{tid}_Row#{i}", *r] for i, r in enumerate(rows, 1)]


def _coreblk_ledger(blk: dict, tc: _TableCounter, parent: str) -> list:
    tid = tc.next_id()
    comps = "; ".join(
        f"{c.get('name')} ({c.get('formula')}; {c.get('comp_num_id')}; "
        f"{c.get('org_num')}; InChIKey {c.get('inchi_key')})"
        for c in blk.get("compounds", []) if isinstance(c, dict)
    )
    meta = [
        f"lit_num_id: {blk.get('lit_num_id')} | lit_id: {blk.get('lit_id')} | "
        f"doi: {blk.get('doi')}",
        f"block: {blk.get('block_number')} | BLKsubsys_id: "
        f"{blk.get('BLKsubsys_id') or '—'} | type: {blk.get('block_type')} "
        f"({blk.get('blocktype_num_id')}) | system: {blk.get('system_type')} | "
        f"n_datapoints: {blk.get('n_datapoints')}",
        f"compounds: {comps}",
        f"prop_num_ids: {', '.join(blk.get('prop_num_ids', []) or [])}",
        f"description: {blk.get('description')}",
    ]
    if blk.get("solvents"):
        meta.append(f"solvents: {blk['solvents']}")
    if blk.get("notes"):
        meta.append(f"notes: {blk['notes']}")
    if blk.get("subsystem_scope"):
        meta.append(f"subsystem_scope: {blk['subsystem_scope']}")
    body = _pipe_table(["row_id", "kind", "id", "name", "detail"],
                       _blk_structural_rows(blk, tid))
    return ["```ledger", f"**{tid}_({parent}_{tc.label}_CoreBLK):**", *meta, "",
            *body, "```", ""]


def _coreblk_summary_table(blocks: list, tc: _TableCounter, parent: str) -> list:
    """One compact canonical row per core block (ledger level ``summary``).
    Each row's id is the block's AS-IF-FULL ledger table id, so summary
    rows cite the very tables the full render shows on other surfaces."""
    rows: list = []
    for blk in blocks:
        if not isinstance(blk, dict):
            continue
        tid = tc.next_id()
        block_id = str(blk.get("block_number", ""))
        if blk.get("BLKsubsys_id"):
            block_id += f" [{blk['BLKsubsys_id']}]"
        rows.append([tid, blk.get("lit_num_id"), block_id,
                     ", ".join(blk.get("comp_num_ids", []) or []),
                     ", ".join(blk.get("prop_num_ids", []) or []),
                     blk.get("description", "")])
    return ["**Core blocks found:**", "",
            f"**{tc.prefix}{tc.label}_Blocks_({parent}_{tc.label}_CoreBLK):**",
            "", *_pipe_table(["table_id", "lit_num_id", "block_number",
                              "comp_num_ids", "prop_num_ids", "description"],
                             rows), ""]


# ── envelope rendering ─────────────────────────────────────────

def _bullets(items: list) -> list:
    """Render scalar items as valid Markdown bullets, including multiline text."""
    rendered: list[str] = []
    for item in items:
        text = "—" if item is None else str(item)
        item_lines = text.splitlines() or [""]
        rendered.append(f"- {item_lines[0]}")
        rendered.extend(f"  {line}" for line in item_lines[1:])
    return rendered


def _field_title(key: object) -> str:
    """Human-readable Markdown label for a structured-result field."""
    text = str(key).replace("_", " ").strip()
    return (text[:1].upper() + text[1:]) if text else "Value"


def _heading_text(value: object) -> str:
    """Keep data out of heading syntax without JSON-escaping its prose."""
    text = str(value).replace("\r", " ").replace("\n", " ").strip()
    return text.replace("#", "\\#") or "Unnamed"


def _is_scalar(value: object) -> bool:
    return value is None or isinstance(value, (str, int, float, bool))


def _inline_markdown(value: object) -> str:
    if value is None:
        return "—"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _flat_mapping_rows(items: list) -> tuple[list[str], list[list]] | None:
    """Return stable table columns/rows for a list of scalar-only objects."""
    if not items or not all(isinstance(item, dict) for item in items):
        return None
    columns: list[str] = []
    for item in items:
        if not all(_is_scalar(value) for value in item.values()):
            return None
        for key in item:
            key_text = str(key)
            if key_text not in columns:
                columns.append(key_text)
    return columns, [[item.get(column) for column in columns] for item in items]


def _structured_markdown_body(
    value: object,
    *,
    tc: _TableCounter,
    parent: str,
    section_label: str,
    depth: int = 0,
) -> list[str]:
    """Render arbitrary JSON-compatible data without serializing JSON.

    This is the deterministic fallback for schemas that are not answer
    envelopes (notably ``align_compositions``) and for future fields. Text is
    emitted as Markdown text; scalar arrays become lists; flat object arrays
    become canonical tables; nested values become titled Markdown sections.
    """
    if depth >= 12:
        return ["*Nested data omitted from this context view; the complete "
                "structure remains on the audit rail.*"]

    if _is_scalar(value):
        text = _inline_markdown(value)
        return text.splitlines() or [""]

    if isinstance(value, list):
        if not value:
            return ["*None.*"]
        if all(_is_scalar(item) for item in value):
            return _bullets(value)
        flat = _flat_mapping_rows(value)
        if flat is not None:
            columns, rows = flat
            tid = tc.next_id()
            table_rows = [
                [f"{tid}_Row#{index}", *row]
                for index, row in enumerate(rows, 1)
            ]
            return [
                f"**{tid}_({parent}_{tc.label}_{section_label}):**",
                "",
                *_pipe_table(["row_id", *columns], table_rows),
            ]
        lines: list[str] = []
        for index, item in enumerate(value, 1):
            if lines:
                lines.append("")
            item_name = (
                item.get("label")
                if isinstance(item, dict) and isinstance(item.get("label"), str)
                else f"Item {index}"
            )
            heading = "#" * min(5 + depth, 6)
            lines += [f"{heading} {_heading_text(item_name)}", ""]
            lines += _structured_markdown_body(
                item,
                tc=tc,
                parent=parent,
                section_label=section_label,
                depth=depth + 1,
            )
        return lines

    if isinstance(value, dict):
        if not value:
            return ["*None.*"]
        lines: list[str] = []
        for key, item in value.items():
            title = _field_title(key)
            if _is_scalar(item):
                text_lines = _inline_markdown(item).splitlines() or [""]
                if len(text_lines) == 1:
                    lines.append(f"- **{title}:** {text_lines[0]}")
                else:
                    lines += [f"**{title}:**", "", *text_lines, ""]
                continue
            if lines and lines[-1] != "":
                lines.append("")
            heading = "#" * min(5 + depth, 6)
            lines += [f"{heading} {_heading_text(title)}", ""]
            lines += _structured_markdown_body(
                item,
                tc=tc,
                parent=parent,
                section_label=f"{section_label}_{key}",
                depth=depth + 1,
            )
        return lines

    # Native results are validated as JSON-compatible before this display
    # layer. Keep an opaque unexpected object out of model context rather
    # than falling back to repr(), which can expose an unbounded payload.
    return [f"*Unsupported display value ({type(value).__name__}); complete "
            "data remains on the audit rail.*"]


def _render_structured_section(
    title: str,
    value: object,
    *,
    tc: _TableCounter,
    parent: str,
    section_label: str,
) -> list[str]:
    return [
        f"#### {_heading_text(title)}",
        "",
        *_structured_markdown_body(
            value,
            tc=tc,
            parent=parent,
            section_label=section_label,
        ),
        "",
    ]


def _render_parallel_results(
    results: list,
    *,
    tool_name: str,
    label: str,
    parent: str,
    ledger_level: str,
    tc: _TableCounter,
) -> list[str]:
    """Render n_tasks/n_queries children as Markdown, never nested JSON."""
    lines: list[str] = ["#### Parallel subagent results", ""]
    for index, entry in enumerate(results, 1):
        task_label = (
            entry.get("label")
            if isinstance(entry, dict) and isinstance(entry.get("label"), str)
            else f"result-{index}"
        )
        lines += [f"##### [{_heading_text(task_label)}]", ""]
        if not isinstance(entry, dict):
            lines += _structured_markdown_body(
                entry,
                tc=tc,
                parent=parent,
                section_label=f"Parallel{index}",
            )
            lines.append("")
            continue

        if isinstance(entry.get("error"), str) and "result" not in entry:
            lines += ["**Status:** Error", "", entry["error"], ""]
            if "salvage" in entry:
                lines += _render_structured_section(
                    "Salvaged result",
                    entry["salvage"],
                    tc=tc,
                    parent=parent,
                    section_label=f"Parallel{index}Salvage",
                )
            continue

        child = entry.get("result") if "result" in entry else {
            key: value for key, value in entry.items() if key != "label"
        }
        if isinstance(child, str) and child.lstrip().startswith("{"):
            try:
                decoded = json.loads(child)
                child = decoded if isinstance(decoded, dict) else child
            except (json.JSONDecodeError, ValueError):
                pass
        # Keep the nested id inside the canonical-id grammar ([\w#]+) so a
        # later delegation hop can chain rather than duplicate/renumber it.
        child_label = f"{label}_R{index}"
        if isinstance(child, dict) and any(
            key in child for key in ("answer", "core_claims", "verdict", "sources")
        ):
            lines += [
                render_subagent_payload(
                    child,
                    tool_name=f"{tool_name}[{task_label}]",
                    label=child_label,
                    parent=parent,
                    ledger_level=ledger_level,
                    include_title=False,
                    id_prefix=tc.prefix,
                ),
                "",
            ]
        else:
            lines += _structured_markdown_body(
                child,
                tc=tc,
                parent=parent,
                section_label=f"Parallel{index}",
            )
            lines.append("")
    return lines


def _status_line(payload: dict, inner: dict) -> str:
    parts: list[str] = []
    if payload.get("status") or inner.get("status"):
        parts.append(f"status={payload.get('status') or inner.get('status')}")
    if isinstance(payload.get("iterations"), int):
        parts.append(f"{payload['iterations']} iterations")
    if isinstance(payload.get("elapsed_seconds"), (int, float)):
        parts.append(f"{payload['elapsed_seconds']:.1f}s")
    if isinstance(payload.get("tool_count"), int):
        parts.append(f"{payload['tool_count']} tool call(s)")
    if payload.get("timed_out"):
        parts.append("TIMED OUT")
    if payload.get("agent"):
        parts.append(f"agent={payload['agent']}")
    return " · ".join(parts)


def render_subagent_payload(payload: dict, *, tool_name: str,
                            label: str, parent: str,
                            ledger_level: str = "full",
                            include_title: bool = True,
                            id_prefix: str = "") -> str:
    """Organized markdown view of one subagent envelope (display only).

    ``ledger_level`` ("full" | "summary" | "none") controls the verbatim
    ledgers and catalog-machinery sections — see the module docstring.
    ``id_prefix`` marks the surface on every table id (``WM_`` for
    working-memory digests); the id sequence itself is allocated
    AS-IF-FULL so the same table keeps the same number at every level.
    """
    if ledger_level not in LEDGER_LEVELS:
        ledger_level = "full"
    inner: dict = {}
    inner_parse_failed = False
    raw_answer = payload.get("answer")
    if isinstance(raw_answer, str) and raw_answer.lstrip().startswith("{"):
        try:
            parsed = json.loads(raw_answer)
            if isinstance(parsed, dict):
                inner = parsed
            else:
                inner_parse_failed = True
        except (json.JSONDecodeError, ValueError):
            inner_parse_failed = True

    def field(key: str):
        return inner.get(key) if key in inner else payload.get(key)

    tc = _TableCounter(label, id_prefix)
    lines: list[str] = []
    if include_title:
        lines += [f"### {label} — {tool_name} return", ""]
    head: list[str] = []
    status = _status_line(payload, inner)
    if status:
        head.append(f"**Status:** {status}")
    if payload.get("_question"):
        head.append(f"**Question:** {payload['_question']}")
    session = payload.get("_session_dir") or payload.get("session_dir")
    if session:
        head.append(f"**Session:** `{session}`")
    if head:
        lines += [*head, ""]

    summary = field("summary")
    if isinstance(summary, str) and summary.strip():
        lines += ["**Summary:**", "",
                  _canonicalize_text(summary, tc, parent, kind="Summary"), ""]
    answer_text = inner.get("answer") if inner else raw_answer
    if inner_parse_failed:
        lines += [
            "**Answer:**",
            "",
            "*The delegated answer envelope could not be rendered safely. "
            "Its original structured text remains on the audit rail and was "
            "not inserted into this context.*",
            "",
        ]
    elif isinstance(answer_text, str) and answer_text.strip():
        lines += ["**Answer:**", "",
                  _canonicalize_text(answer_text, tc, parent), ""]

    claims = field("core_claims")
    if isinstance(claims, list) and claims:
        lines += ["**Core claims:**", *_bullets(claims), ""]
    confidence = field("confidence")
    if isinstance(confidence, str) and confidence:
        lines += [f"**Confidence:** {confidence}", ""]

    sources = field("sources")
    if isinstance(sources, list) and sources and all(
            isinstance(s, dict) for s in sources):
        tid = tc.next_id()
        rows = [[f"{tid}_Row#{i}", s.get("lit_num_id"), s.get("block"),
                 s.get("doi"), s.get("BLKsubsys_id"), s.get("description")]
                for i, s in enumerate(sources, 1)]
        lines += ["**Sources:**", "", f"**{tid}_({parent}_{label}_Sources):**", "",
                  *_pipe_table(["row_id", "lit_num_id", "block", "doi",
                                "BLKsubsys_id", "description"], rows), ""]

    fits = field("fit_results")
    if isinstance(fits, list) and fits and all(isinstance(f, dict) for f in fits):
        tid = tc.next_id()
        rows = [[f"{tid}_Row#{i}", f.get("lit_num_id"), f.get("block_number"),
                 f.get("property"), f.get("rk_order"),
                 ", ".join(str(c) for c in f.get("rk_coeffs", []) or []),
                 f.get("r_squared"), f.get("rmse"), f.get("n_points"),
                 f.get("temperature_K"), f.get("mixing_rule")]
                for i, f in enumerate(fits, 1)]
        lines += ["**Fit results:**", "",
                  f"**{tid}_({parent}_{label}_FitResults):**", "",
                  *_pipe_table(["row_id", "lit_num_id", "block", "property",
                                "rk_order", "rk_coeffs", "r_squared", "rmse",
                                "n_points", "T_K", "mixing_rule"], rows), ""]

    n_insp_dropped = n_upd_dropped = n_cat_dropped = n_blk_dropped = 0

    catalog = field("id_catalog_snapshot")
    if isinstance(catalog, list) and catalog:
        if ledger_level == "full":
            rows = [[e.get("type"), e.get("global_id"), e.get("registry_id"),
                     e.get("name")] for e in catalog if isinstance(e, dict)]
            lines += ["**ID catalog snapshot:**", "",
                      *_pipe_table(["type", "global_id", "registry_id", "name"],
                                   rows), ""]
        else:
            n_cat_dropped = len(catalog)

    id_updates = field("core_id_updates")
    if isinstance(id_updates, list) and id_updates:
        if ledger_level == "full":
            lines += ["**Core ID updates:**", *[
                f"- {u.get('action')} {u.get('core_GLOB_id')} — {u.get('name')} "
                f"(registry: {u.get('registry_id')})"
                for u in id_updates if isinstance(u, dict)], ""]
        else:
            n_upd_dropped = len(id_updates)

    follow = field("follow_up_suggestions")
    if isinstance(follow, list) and follow:
        lines += ["**Follow-up suggestions:**", *_bullets(follow), ""]

    entity = {k: v for k, v in payload.items()
              if k.startswith("n_") and isinstance(v, (int, float))}
    if entity:
        lines += ["**Entity summary:** "
                  + " · ".join(f"{k}={v}" for k, v in sorted(entity.items())), ""]

    parallel_results = field("results")
    if isinstance(parallel_results, list) and parallel_results:
        lines += _render_parallel_results(
            parallel_results,
            tool_name=tool_name,
            label=label,
            parent=parent,
            ledger_level=ledger_level,
            tc=tc,
        )

    blocks = field("core_blocks_found")
    if isinstance(blocks, list) and blocks:
        if ledger_level == "full":
            lines += ["#### Core blocks found — verbatim ledger", ""]
            for blk in blocks:
                if isinstance(blk, dict):
                    lines += _coreblk_ledger(blk, tc, parent)
        elif ledger_level == "summary":
            lines += _coreblk_summary_table(blocks, tc, parent)
        else:
            for blk in blocks:      # as-if-full: dropped ledgers keep ids
                if isinstance(blk, dict):
                    tc.next_id()
            n_blk_dropped = len(blocks)

    # Ledger dedupe (display only): the lifted top-level array wins; the
    # inner copy inside the answer JSON is byte-identical when both exist.
    inspections = payload.get("data_inspections")
    if not (isinstance(inspections, list) and inspections):
        inspections = inner.get("data_inspections")
    if isinstance(inspections, list) and inspections:
        if ledger_level == "full":
            lines += ["#### Data inspections — verbatim ledger", ""]
            for insp in inspections:
                if isinstance(insp, dict):
                    lines += _insp_ledger(insp, tc, parent)
        else:
            for insp in inspections:  # as-if-full: dropped ledgers keep ids
                if isinstance(insp, dict):
                    tc.next_id()
            n_insp_dropped = len(inspections)

    dropped: list[str] = []
    if n_insp_dropped:
        dropped.append(f"{n_insp_dropped} verbatim data_inspections table(s)")
    if n_upd_dropped:
        dropped.append(f"{n_upd_dropped} core_id_update(s) already applied "
                       "to the ID catalog")
    if n_cat_dropped:
        dropped.append(f"{n_cat_dropped} id_catalog_snapshot row(s) "
                       "(catalog is merged separately)")
    if n_blk_dropped:
        dropped.append(f"{n_blk_dropped} core block record(s)")
    if dropped:
        lines += ["*Not stored here: " + "; ".join(dropped)
                  + ". Verbatim evidence stays on the tool-history rail and "
                  "is re-attached to the final envelope deterministically.*",
                  ""]

    files = payload.get("output_files")
    if isinstance(files, list) and files:
        lines += ["**Output files:**", *[
            f"- [{f.get('category')}] `{f.get('path')}` — {f.get('description')}"
            for f in files if isinstance(f, dict)], ""]

    verdict = payload.get("verdict")
    if isinstance(verdict, str) and verdict.strip():
        lines += ["**Verdict:**", "",
                  _canonicalize_text(verdict, tc, parent, kind="Verdict"), ""]

    handled = _HANDLED_KEYS | set(entity)
    if isinstance(parallel_results, list):
        handled.add("results")
    leftovers = {k: v for k, v in payload.items() if k not in handled}
    for k, v in (inner.items() if inner else ()):  # promote unhandled inner keys
        if k not in handled and k not in leftovers:
            leftovers[k] = v
    if leftovers:
        lines += ["#### Additional returned fields", ""]
        for key, value in leftovers.items():
            lines += _render_structured_section(
                _field_title(key),
                value,
                tc=tc,
                parent=parent,
                section_label=f"Additional_{key}",
            )

    return "\n".join(lines).rstrip()


# ── loop-facing entry point ────────────────────────────────────

def _wrap_parent_markdown(markdown: str) -> str:
    """Wrap rendered Markdown in one unambiguous subagent context boundary."""
    # Escape every registered engine marker in agent-authored text before
    # adding the one real outer boundary. The catalog's master regex is the
    # single source of truth; unrelated HTML and ordinary Markdown survive.
    safe = ALL_CONTEXT_MARKERS_RE.sub(
        lambda match: (
            match.group(0)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        ),
        markdown.rstrip(),
    )
    return (
        f"{MARKERS.subagent_answer.open}\n"
        f"{safe}\n"
        f"{MARKERS.subagent_answer.close}"
    )


def build_subagent_context_display(
    tool_name: str,
    fn: Callable | None,
    native_result: Any,
    one_result: str,
    tool_history: list,
) -> str:
    """Context-only Markdown view of a marked subagent result.

    Unmarked tools pass through unchanged. Marked results keep one configured
    subagent context boundary whose body is Markdown after the structured
    transport has been validated and recorded. Parse/render failures fail
    closed to a wrapped Markdown status notice; the recorded rails (tool
    history, anchors, and working memory) keep the original JSON.
    """
    try:
        marked = fn is not None and getattr(fn, "_returns_subagent_answer", False)
        stripped = one_result.strip() if isinstance(one_result, str) else ""
        # search, not fullmatch: an oversized result carries the
        # TOOL_RESULT_SIZE_WARNING banner before the marker
        marker_match = MARKERS.subagent_answer_re.search(stripped)
        if not marked and marker_match is None:
            return one_result
        if isinstance(native_result, dict) and "error_code" in native_result:
            code = str(native_result.get("error_code") or "SUBAGENT_ERROR")
            return _wrap_parent_markdown(
                f"### {tool_name} delegated return unavailable\n\n"
                f"**Status:** {code}\n\n"
                "The delegated tool reported an error. Its structured details "
                "remain on the audit rail and were not inserted into this "
                "model context."
            )

        payload: Any = None
        if isinstance(native_result, dict):
            payload = native_result
        else:
            native_text = (
                native_result.strip() if isinstance(native_result, str) else ""
            )
            native_match = MARKERS.subagent_answer_re.search(native_text)
            body = (
                native_match.group(1)
                if native_match is not None
                else marker_match.group(1) if marker_match is not None
                else native_text or stripped
            )
            payload = json.loads(body)
        if not isinstance(payload, dict):
            raise TypeError("marked subagent payload must be an object")

        parent = _parent_label()
        label = (resolve_sid_label(tool_name, payload, result_text=one_result)
                 or _child_label(tool_name, tool_history))
        level = resolve_ledger_level(transition_pair(tool_name, parent),
                                     "context")
        rendered = render_subagent_payload(
            payload, tool_name=tool_name, label=label, parent=parent,
            ledger_level=level)
        if not rendered.strip():
            raise ValueError("marked subagent payload rendered to empty Markdown")

        from .react_helpers import require_result_within_limit
        return require_result_within_limit(
            tool_name,
            _wrap_parent_markdown(rendered),
        )
    except Exception as exc:
        log.warning("subagent context render failed for %s (%s) — failing "
                    "closed without exposing structured payload", tool_name, exc)
        return _wrap_parent_markdown(
            f"### {tool_name} delegated return unavailable\n\n"
            "**Status:** CONTEXT_RENDER_FAILED\n\n"
            "The delegated result could not be rendered safely. The complete "
            "structured result remains on the audit rail and was not inserted "
            "into this model context."
        )


__all__ = [
    "LEDGER_LEVELS",
    "active_parent_label",
    "build_subagent_context_display",
    "render_subagent_payload",
    "resolve_ledger_level",
    "resolve_sid_label",
    "transition_pair",
]
