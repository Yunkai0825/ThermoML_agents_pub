"""
Subagent-answer context rendering.
==================================
Renders a subagent tool's JSON envelope as organized markdown for the
PARENT agent's context window only.  Every recorded rail keeps the
validated JSON verbatim: ``tool_history[*].result_full``, the tool
anchors (``result_full=``), working-memory instrumentation, the
grounding-gate inspection harvest, and the post-run funnels all see the
same wrapped JSON string as before.  The rendered markdown exists solely
inside the ``<subagent_answer>`` marker that is injected into the parent
context (``result_parts`` / tool-result memory append).

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
  catalog-machinery sections (core_id_updates / id_catalog_snapshot /
  follow_up_suggestions)
- ``summary`` — core blocks as one compact canonical table; inspections
  and catalog machinery collapse into a ``*Not stored here: …*`` note
- ``none``    — every ledger collapses into the note

Levels are resolved per boundary from the session's engine config field
``SUBAGENT_LEDGER_LEVELS = {"context": {pair: level}, "memory": {...}}``
where pair keys are ``main/Qi``, ``main/Ai``, ``main/L1``, ``main/L2``,
``Ai/Qi``, ``Ai/L1``, ``Qi/L1``, ``L1/L2``.  The memory surface (working-
memory digests, see ``envelope_memory_digest``) defaults to ``summary``.

Rendering NEVER raises: any failure falls back to the original JSON string.
"""
from __future__ import annotations

import json
import logging
import re
from typing import Any, Callable

from ...general_text_context_marker_catalog import MARKERS

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
    return [f"- {i}" for i in items]


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
    raw_answer = payload.get("answer")
    if isinstance(raw_answer, str) and raw_answer.lstrip().startswith("{"):
        try:
            parsed = json.loads(raw_answer)
            if isinstance(parsed, dict):
                inner = parsed
        except (json.JSONDecodeError, ValueError):
            inner = {}

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
        lines += [f"**Summary:** {summary}", ""]

    answer_text = inner.get("answer") if inner else raw_answer
    if isinstance(answer_text, str) and answer_text.strip():
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
    if isinstance(follow, list) and follow and ledger_level == "full":
        lines += ["**Follow-up suggestions:**", *_bullets(follow), ""]

    entity = {k: v for k, v in payload.items()
              if k.startswith("n_") and isinstance(v, (int, float))}
    if entity:
        lines += ["**Entity summary:** "
                  + " · ".join(f"{k}={v}" for k, v in sorted(entity.items())), ""]

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
    leftovers = {k: v for k, v in payload.items() if k not in handled}
    for k, v in (inner.items() if inner else ()):  # promote unhandled inner keys
        if k not in handled and k not in leftovers:
            leftovers[k] = v
    if leftovers:
        lines += ["**Other fields:**", *[
            f"- {k}: {v if isinstance(v, (str, int, float, bool)) else json.dumps(v, ensure_ascii=False)}"
            for k, v in leftovers.items()], ""]

    return "\n".join(lines).rstrip()


# ── loop-facing entry point ────────────────────────────────────

def build_subagent_context_display(
    tool_name: str,
    fn: Callable | None,
    native_result: Any,
    one_result: str,
    tool_history: list,
) -> str:
    """Context-only markdown view of a marked subagent result.

    Returns ``one_result`` unchanged for unmarked tools, error envelopes,
    unparseable payloads, or any rendering failure — the recorded rails
    (tool_history / anchors / working memory) always keep the JSON.
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
            return one_result

        payload: Any = None
        if isinstance(native_result, dict):
            payload = native_result
        else:
            body = marker_match.group(1) if marker_match else stripped
            payload = json.loads(body)
        if not isinstance(payload, dict):
            return one_result

        parent = _parent_label()
        label = (resolve_sid_label(tool_name, payload, result_text=one_result)
                 or _child_label(tool_name, tool_history))
        level = resolve_ledger_level(transition_pair(tool_name, parent),
                                     "context")
        rendered = render_subagent_payload(
            payload, tool_name=tool_name, label=label, parent=parent,
            ledger_level=level)
        wrapped = (f"{MARKERS.subagent_answer.open}\n{rendered}\n"
                   f"{MARKERS.subagent_answer.close}")

        from .react_helpers import require_result_within_limit
        return require_result_within_limit(tool_name, wrapped)
    except Exception as exc:
        log.warning("subagent context render failed for %s (%s) — "
                    "delivering JSON unchanged", tool_name, exc)
        return one_result


__all__ = [
    "LEDGER_LEVELS",
    "active_parent_label",
    "build_subagent_context_display",
    "render_subagent_payload",
    "resolve_ledger_level",
    "resolve_sid_label",
    "transition_pair",
]
