"""
Compactors for basic_search_tools — dict→markdown formatters.
=============================================================
Each function takes a raw tool result dict and returns a compact
markdown string.  These are used by the search tools themselves
to deliver pre-compacted results.

Each compactor is tagged with ``@_compacts("tool_name")`` to declare
which tool it serves.  ``CompactorCatalog.from_functions()`` reads
the ``_compacts_tools`` attribute for auto-wiring.
"""

from __future__ import annotations

import logging
import json
import re
from functools import wraps
from typing import Any, Dict, List

log = logging.getLogger("search-compactors")


# ── Decorator — sets fn._compacts_tools (same contract as catalog.compacts) ─
def _compacts(*tools: str):
    """Tag a compactor and preserve strict ID-refinement errors verbatim."""
    def _deco(fn):
        @wraps(fn)
        def _wrapped(data, *args, **kwargs):
            if isinstance(data, dict) and data.get("error_code") == "ID_REFINEMENT_REQUIRED":
                refinement = data["refinement"] if "refinement" in data else None
                if not isinstance(refinement, dict):
                    raise ValueError("ID refinement result is missing refinement object")
                required = ("field", "received", "expected", "reason")
                missing = [field for field in required if field not in refinement]
                if missing:
                    raise ValueError(
                        f"ID refinement result is missing refinement fields {missing}"
                    )
                return (
                    "**ID_REFINEMENT_REQUIRED**\n\n"
                    f"- field: `{refinement['field']}`\n"
                    f"- received: `{refinement['received']}`\n"
                    f"- expected: `{refinement['expected']}`\n"
                    f"- reason: {refinement['reason']}\n"
                )
            if isinstance(data, dict) and data.get("error_code") == "QUERY_REFINEMENT_REQUIRED":
                _require_fields(
                    data,
                    ("error", "n_results", "results"),
                    "query refinement result",
                )
                if data["n_results"] != 0 or data["results"] != []:
                    raise ValueError("query refinement result must contain zero results")
                return f"**QUERY_REFINEMENT_REQUIRED**\n\n{data['error']}\n"
            return fn(data, *args, **kwargs)

        _wrapped._compacts_tools = tools
        return _wrapped
    return _deco


def _require_object(value: Any, context: str) -> dict:
    if not isinstance(value, dict):
        raise TypeError(f"{context} must be an object")
    return value


def _require_fields(row: dict, fields: tuple[str, ...], context: str) -> None:
    missing = [field for field in fields if field not in row]
    if missing:
        raise ValueError(f"{context} is missing required fields {missing}")


def _require_results(data: Any, tool_name: str) -> tuple[list[dict], int]:
    payload = _require_object(data, f"{tool_name} result")
    _require_fields(payload, ("n_results", "results"), f"{tool_name} result")
    results = payload["results"]
    if not isinstance(results, list):
        raise TypeError(f"{tool_name}.results must be an array")
    if isinstance(payload["n_results"], bool) or not isinstance(payload["n_results"], int):
        raise TypeError(f"{tool_name}.n_results must be an integer")
    if payload["n_results"] != len(results):
        raise ValueError(
            f"{tool_name}.n_results={payload['n_results']} does not match "
            f"{len(results)} result rows"
        )
    for index, row in enumerate(results):
        if not isinstance(row, dict):
            raise TypeError(f"{tool_name}.results[{index}] must be an object")
    return results, payload["n_results"]

# ── Configurable limits (sensible defaults) ─────────────────────
BLOCK_CONDENSE_LIMIT = 10_000   # char limit triggering block condensation


# ═══════════════════════════════════════════════════════════════
#  Block-level condensation helpers
# ═══════════════════════════════════════════════════════════════

_TOPOLOGY_RE     = re.compile(r'\*\*Topology:\*\*')
_DATA_HEADER_RE  = re.compile(r'^###\s+Data\s*$')
_BLOCK_HEADER_RE = re.compile(r'^##\s+')
_SECTION_HEADER_RE = re.compile(r'^###\s+(\w+)')
_TABLE_ROW_RE    = re.compile(r'^\|(.+)\|$')


def _condense_block_md(md: str) -> str:
    """L1: strip data-table rows, keep metadata + Topology."""
    lines = md.split('\n')
    kept: list[str] = []
    in_data = False
    for line in lines:
        if _DATA_HEADER_RE.match(line.strip()):
            kept.append(line)
            in_data = True
            continue
        if in_data:
            if _TOPOLOGY_RE.search(line):
                kept.append(line)
                continue
            if line.strip().startswith('|'):
                continue
            if not line.strip():
                kept.append(line)
                continue
            in_data = False
            kept.append(line)
        else:
            kept.append(line)
    return '\n'.join(kept)


def _extract_section_table(lines: list[str], section_name: str) -> list[list[str]]:
    """Extract rows from a markdown table under a ### section header."""
    in_section = False
    rows: list[list[str]] = []
    skip_count = 0
    for line in lines:
        m = _SECTION_HEADER_RE.match(line.strip())
        if m:
            if m.group(1).lower() == section_name.lower():
                in_section = True
                skip_count = 0
                continue
            elif in_section:
                break
        if not in_section:
            continue
        rm = _TABLE_ROW_RE.match(line.strip())
        if rm:
            if skip_count < 2:
                skip_count += 1
                continue
            cells = [c.strip() for c in rm.group(1).split('|')]
            rows.append(cells)
    return rows


def _extract_data_ranges(lines: list[str]) -> tuple[list[tuple[str, str, str]], int]:
    """Extract min-max ranges and row count from the ### Data table."""
    in_data = False
    headers: list[str] = []
    col_vals: list[list[float]] = []
    n_data_rows = 0
    for line in lines:
        m = _SECTION_HEADER_RE.match(line.strip())
        if m:
            if m.group(1).lower() == "data":
                in_data = True
                continue
            elif in_data:
                break
        if not in_data:
            continue
        rm = _TABLE_ROW_RE.match(line.strip())
        if rm:
            cells = [c.strip() for c in rm.group(1).split('|')]
            if not headers:
                headers = cells
                col_vals = [[] for _ in headers]
                continue
            if all(c.replace('-', '').replace(':', '') == '' for c in cells):
                continue
            n_data_rows += 1
            for i, c in enumerate(cells):
                if i < len(col_vals):
                    try:
                        col_vals[i].append(float(c))
                    except (ValueError, TypeError) as exc:
                        log.debug("Failed to parse numeric value %r under %r: %s", c, headers[i], exc)
    ranges: list[tuple[str, str, str]] = []
    for i, hdr in enumerate(headers):
        if hdr.startswith('±'):
            continue
        vals = col_vals[i] if i < len(col_vals) else []
        if vals:
            ranges.append((hdr, f"{min(vals):g}", f"{max(vals):g}"))
    return ranges, n_data_rows


def _ultra_condense_block_md(md: str, *, doi: str = "", block_number: str = "") -> str:
    """L2: reduce a block to header + one-liner summaries."""
    lines = md.split('\n')
    kept: list[str] = []

    header = None
    for line in lines:
        if _BLOCK_HEADER_RE.match(line):
            header = line
            break
    if doi or block_number:
        tag = f"**{doi} / {block_number}**"
        kept.append(f"{header}  [{tag}]" if header else f"## {tag}")
    elif header:
        kept.append(header)

    data_ranges, n_data_rows = _extract_data_ranges(lines)

    comp_rows = _extract_section_table(lines, "Compounds")
    if comp_rows:
        names = [r[1] for r in comp_rows if len(r) > 1 and r[1]]
        if names:
            kept.append(f"**Compounds:** {', '.join(names)}")

    prop_rows = _extract_section_table(lines, "Properties")
    prop_phases: list[str] = []
    if prop_rows:
        pparts = [r[1] for r in prop_rows if len(r) > 1 and r[1]]
        if pparts:
            kept.append(f"**Properties:** {', '.join(pparts)}")
        methods = sorted({r[3] for r in prop_rows if len(r) > 3 and r[3]})
        if methods:
            kept.append(f"**Methods:** {', '.join(methods)}")
        prop_phases = sorted({r[5] for r in prop_rows if len(r) > 5 and r[5]})

    var_rows = _extract_section_table(lines, "Variables")
    if var_rows:
        vparts = [r[1] for r in var_rows if len(r) > 1 and r[1]]
        if vparts:
            kept.append(f"**Variables:** {', '.join(vparts)}")

    if data_ranges:
        rparts = []
        for col, lo, hi in data_ranges:
            rparts.append(f"{col}={lo}" if lo == hi else f"{col} [{lo}..{hi}]")
        kept.append(f"**Ranges:** {', '.join(rparts)}")

    constr_rows = _extract_section_table(lines, "Constraints")
    if constr_rows:
        pairs = []
        for r in constr_rows:
            cname = r[1] if len(r) > 1 else ""
            cval = r[2] if len(r) > 2 else ""
            if cname:
                pairs.append(f"{cname}={cval}" if cval else cname)
        if pairs:
            kept.append(f"**Constraints:** {', '.join(pairs)}")

    cond_lines: list[str] = []
    in_conditions = False
    for line in lines:
        m = _SECTION_HEADER_RE.match(line.strip())
        if m:
            if m.group(1).lower() == "conditions":
                in_conditions = True
                continue
            elif in_conditions:
                break
        if in_conditions and line.strip().startswith('**'):
            cond_lines.append(line.strip())

    has_phase_in_conds = any(cl.startswith("**Phases:") for cl in cond_lines)
    if prop_phases and not has_phase_in_conds:
        kept.append(f"**Phases:** {', '.join(prop_phases)}")
    kept.extend(cond_lines)

    if n_data_rows:
        kept.append(f"**Points:** {n_data_rows}")

    for line in lines:
        if _TOPOLOGY_RE.search(line):
            kept.append(line)

    return '\n'.join(kept) if kept else lines[0] if lines else ""


def _apply_block_condensation(
    parts: list[str],
    block_entries: list[tuple[str, str, str]],
) -> str:
    """Apply 2-level condensation to assembled block markdown."""
    if not block_entries:
        return "\n".join(parts) + "\n"

    block_parts = [f"\n---\n{md}" for _, _, md in block_entries]
    full = "\n".join(parts + block_parts) + "\n"

    if len(full) <= BLOCK_CONDENSE_LIMIT:
        return full

    # L1: strip data-table rows
    condensed = [_condense_block_md(md) for _, _, md in block_entries]
    block_parts = [f"\n---\n{md}" for md in condensed]
    full = "\n".join(parts + block_parts) + "\n"
    orig_chars = sum(len(md) for _, _, md in block_entries)
    new_chars = sum(len(md) for md in condensed)
    log.info("block condensation L1: %d blocks (%d -> %d chars)",
             len(block_entries), orig_chars, new_chars)

    if len(full) <= BLOCK_CONDENSE_LIMIT:
        return full

    # L2: ultra-condense to one-liner summaries
    ultra = [
        _ultra_condense_block_md(md, doi=doi, block_number=bn)
        for (doi, bn, md) in block_entries
    ]
    block_parts = [f"\n---\n{md}" for md in ultra]
    full = "\n".join(parts + block_parts) + "\n"
    log.info("block condensation L2: %d blocks (%d -> %d chars)",
             len(block_entries), new_chars, sum(len(m) for m in ultra))

    return full


# ═══════════════════════════════════════════════════════════════
#  ID Resolution compactors
# ═══════════════════════════════════════════════════════════════

@_compacts("resolve_compound_ids")
def compact_resolve_compound_ids(data: dict) -> str:
    results, n = _require_results(data, "resolve_compound_ids")
    if n == 0:
        return "**resolve_compound_ids: 0 matches.**\n"
    lines = ["| # | comp_num_id | Name | Formula | SMILES | Score | Match |",
             "|---|-------------|------|---------|--------|-------|-------|"]
    for i, r in enumerate(results[:20], 1):
        _require_fields(
            r,
            ("comp_num_id", "common_name", "formula", "smiles", "score", "match_type"),
            f"resolve_compound_ids.results[{i - 1}]",
        )
        lines.append(
            f"| {i} | {r['comp_num_id']} | {r['common_name']} | {r['formula']} | "
            f"{r['smiles']} | {r['score']} | {r['match_type']} |"
        )
    return f"resolve_compound_ids: {n} match(es).\n\n" + "\n".join(lines) + "\n"


@_compacts("resolve_property_ids")
def compact_resolve_property_ids(data: dict) -> str:
    results, n = _require_results(data, "resolve_property_ids")
    if n == 0:
        return "**resolve_property_ids: 0 matches.**\n"
    lines = ["| # | prop_num_id | Name | Group | Score | Match |",
             "|---|-------------|------|-------|-------|-------|"]
    for i, r in enumerate(results[:20], 1):
        _require_fields(
            r,
            ("prop_num_id", "prop_name", "prop_group", "score", "match_type"),
            f"resolve_property_ids.results[{i - 1}]",
        )
        lines.append(
            f"| {i} | {r['prop_num_id']} | {r['prop_name']} | {r['prop_group']} | "
            f"{r['score']} | {r['match_type']} |"
        )
    return f"resolve_property_ids: {n} match(es).\n\n" + "\n".join(lines) + "\n"


@_compacts("resolve_measurement_ids")
def compact_resolve_measurement_ids(data: dict) -> str:
    results, n = _require_results(data, "resolve_measurement_ids")
    if n == 0:
        return "**resolve_measurement_ids: 0 matches.**\n"
    lines = ["| # | meas_num_id | Method | Type | Score | Match |",
             "|---|-------------|--------|------|-------|-------|"]
    for i, r in enumerate(results[:20], 1):
        _require_fields(
            r,
            ("meas_num_id", "method_name", "method_type", "score", "match_type"),
            f"resolve_measurement_ids.results[{i - 1}]",
        )
        lines.append(
            f"| {i} | {r['meas_num_id']} | {r['method_name']} | "
            f"{r['method_type']} | {r['score']} | {r['match_type']} |"
        )
    return f"resolve_measurement_ids: {n} match(es).\n\n" + "\n".join(lines) + "\n"


@_compacts("resolve_reference_ids")
def compact_resolve_reference_ids(data: dict) -> str:
    results, n = _require_results(data, "resolve_reference_ids")
    if n == 0:
        return "**resolve_reference_ids: 0 matches.**\n"
    lines = ["| # | lit_num_id | DOI | Author | Year | Score | Match |",
             "|---|------------|-----|--------|------|-------|-------|"]
    for i, r in enumerate(results[:20], 1):
        _require_fields(
            r,
            ("lit_num_id", "doi", "first_author", "year", "score", "match_type"),
            f"resolve_reference_ids.results[{i - 1}]",
        )
        lines.append(
            f"| {i} | {r['lit_num_id']} | {r['doi']} | {r['first_author']} | "
            f"{r['year']} | {r['score']} | {r['match_type']} |"
        )
    return f"resolve_reference_ids: {n} match(es).\n\n" + "\n".join(lines) + "\n"


@_compacts("resolve_variable_ids")
def compact_resolve_variable_ids(data: dict) -> str:
    results, n = _require_results(data, "resolve_variable_ids")
    if n == 0:
        return "**resolve_variable_ids: 0 matches.**\n"
    lines = ["| # | var_num_id | Name | Type | nBlocks | Score | Match |",
             "|---|------------|------|------|--------:|-------|-------|"]
    for i, r in enumerate(results[:20], 1):
        _require_fields(
            r,
            ("var_num_id", "var_name", "var_type_key", "n_blocks", "score", "match_type"),
            f"resolve_variable_ids.results[{i - 1}]",
        )
        lines.append(
            f"| {i} | {r['var_num_id']} | {r['var_name']} | {r['var_type_key']} | "
            f"{r['n_blocks']} | {r['score']} | {r['match_type']} |"
        )
    return f"resolve_variable_ids: {n} match(es).\n\n" + "\n".join(lines) + "\n"


@_compacts("resolve_constraint_ids")
def compact_resolve_constraint_ids(data: dict) -> str:
    results, n = _require_results(data, "resolve_constraint_ids")
    if n == 0:
        return "**resolve_constraint_ids: 0 matches.**\n"
    lines = ["| # | constr_num_id | Name | Type | nBlocks | Score | Match |",
             "|---|---------------|------|------|--------:|-------|-------|"]
    for i, r in enumerate(results[:20], 1):
        _require_fields(
            r,
            ("constr_num_id", "constr_name", "constr_type_key", "n_blocks", "score", "match_type"),
            f"resolve_constraint_ids.results[{i - 1}]",
        )
        lines.append(
            f"| {i} | {r['constr_num_id']} | {r['constr_name']} | "
            f"{r['constr_type_key']} | {r['n_blocks']} | {r['score']} | "
            f"{r['match_type']} |"
        )
    return f"resolve_constraint_ids: {n} match(es).\n\n" + "\n".join(lines) + "\n"


@_compacts("resolve_phase_ids")
def compact_resolve_phase_ids(data: dict) -> str:
    results, n = _require_results(data, "resolve_phase_ids")
    if n == 0:
        return "**resolve_phase_ids: 0 matches.**\n"
    lines = ["| # | phase_num_id | Name | nOccurrences | Score | Match |",
             "|---|--------------|------|-------------:|-------|-------|"]
    for i, r in enumerate(results[:20], 1):
        _require_fields(
            r,
            ("phase_num_id", "phase_name", "n_occurrences", "score", "match_type"),
            f"resolve_phase_ids.results[{i - 1}]",
        )
        lines.append(
            f"| {i} | {r['phase_num_id']} | {r['phase_name']} | "
            f"{r['n_occurrences']} | {r['score']} | {r['match_type']} |"
        )
    return f"resolve_phase_ids: {n} match(es).\n\n" + "\n".join(lines) + "\n"


@_compacts("resolve_solvent_ids")
def compact_resolve_solvent_ids(data: dict) -> str:
    results, n = _require_results(data, "resolve_solvent_ids")
    if n == 0:
        return "**resolve_solvent_ids: 0 matches.**\n"
    lines = [
        "| # | solvent_num_id | comp_num_id | Name | Formula | Score | Match |",
        "|---|----------------|-------------|------|---------|-------|-------|",
    ]
    for i, row in enumerate(results[:20], 1):
        _require_fields(
            row,
            ("solvent_num_id", "comp_num_id", "common_name", "formula", "score", "match_type"),
            f"resolve_solvent_ids.results[{i - 1}]",
        )
        lines.append(
            f"| {i} | {row['solvent_num_id']} | {row['comp_num_id']} | "
            f"{row['common_name']} | {row['formula']} | {row['score']} | "
            f"{row['match_type']} |"
        )
    return f"resolve_solvent_ids: {n} match(es).\n\n" + "\n".join(lines) + "\n"


def _compact_block_type_ids(data: dict) -> str:
    results, n = _require_results(data, "resolve_ids(block_type)")
    if n == 0:
        return "**resolve_ids(block_type): 0 matches.**\n"
    lines = [
        "| # | blocktype_num_id | Block type | System type | Score | Match |",
        "|---|------------------|------------|-------------|-------|-------|",
    ]
    for i, row in enumerate(results[:20], 1):
        _require_fields(
            row,
            ("blocktype_num_id", "block_type", "system_type", "score", "match_type"),
            f"resolve_ids(block_type).results[{i - 1}]",
        )
        lines.append(
            f"| {i} | {row['blocktype_num_id']} | {row['block_type']} | "
            f"{row['system_type']} | {row['score']} | {row['match_type']} |"
        )
    return f"resolve_ids(block_type): {n} match(es).\n\n" + "\n".join(lines) + "\n"


def _compact_reaction_type_ids(data: dict) -> str:
    results, n = _require_results(data, "resolve_ids(reaction_type)")
    if n == 0:
        return "**resolve_ids(reaction_type): 0 matches.**\n"
    lines = [
        "| # | rxn_type_num_id | Reaction type | Name | Score | Match |",
        "|---|-----------------|---------------|------|-------|-------|",
    ]
    for i, row in enumerate(results[:20], 1):
        _require_fields(
            row,
            ("rxn_type_num_id", "rxn_type_id", "rxn_type_name", "score", "match_type"),
            f"resolve_ids(reaction_type).results[{i - 1}]",
        )
        lines.append(
            f"| {i} | {row['rxn_type_num_id']} | {row['rxn_type_id']} | "
            f"{row['rxn_type_name']} | {row['score']} | {row['match_type']} |"
        )
    return f"resolve_ids(reaction_type): {n} match(es).\n\n" + "\n".join(lines) + "\n"


@_compacts("resolve_ids")
def compact_resolve_ids(data: dict) -> str:
    """Generic resolve_ids — delegates by inspecting result fields."""
    payload = _require_object(data, "resolve_ids result")
    _require_fields(payload, ("entity_type", "queries"), "resolve_ids result")
    results, _ = _require_results(payload, "resolve_ids")
    if not results:
        return (
            f"**resolve_ids({payload['entity_type']}, {payload['queries']}): "
            "0 matches.**\n"
        )
    sample = results[0]
    # Solvent rows intentionally carry both their solvent-registry ID and the
    # linked compound-registry ID.  Dispatch on the primary solvent namespace
    # before considering the nested compound reference.
    if "solvent_num_id" in sample:
        return compact_resolve_solvent_ids(data)
    if "comp_num_id" in sample:
        return compact_resolve_compound_ids(data)
    if "prop_num_id" in sample:
        return compact_resolve_property_ids(data)
    if "meas_num_id" in sample:
        return compact_resolve_measurement_ids(data)
    if "lit_num_id" in sample:
        return compact_resolve_reference_ids(data)
    if "var_num_id" in sample:
        return compact_resolve_variable_ids(data)
    if "constr_num_id" in sample:
        return compact_resolve_constraint_ids(data)
    if "phase_num_id" in sample:
        return compact_resolve_phase_ids(data)
    if "blocktype_num_id" in sample:
        return _compact_block_type_ids(data)
    if "rxn_type_num_id" in sample:
        return _compact_reaction_type_ids(data)
    raise ValueError(
        "resolve_ids returned a result without a recognized strict global-ID field"
    )


@_compacts("search_id_alignment")
def compact_search_id_alignment(data: dict) -> str:
    payload = _require_object(data, "search_id_alignment result")
    _require_fields(payload, ("entity_type", "query"), "search_id_alignment result")
    etype = payload["entity_type"]
    query = payload["query"]
    results, n = _require_results(payload, "search_id_alignment")
    if n == 0:
        return f"**search_id_alignment({etype}, {query}): 0 results.**\n"
    header = f"search_id_alignment: {n} {etype} matches for '{query}'.\n\n"
    wrapped = {"results": results, "n_results": n}
    if etype == "compound":
        return header + compact_resolve_compound_ids(wrapped)
    if etype == "property":
        return header + compact_resolve_property_ids(wrapped)
    if etype == "measurement":
        return header + compact_resolve_measurement_ids(wrapped)
    if etype == "reference":
        return header + compact_resolve_reference_ids(wrapped)
    if etype == "variable":
        return header + compact_resolve_variable_ids(wrapped)
    if etype == "constraint":
        return header + compact_resolve_constraint_ids(wrapped)
    if etype == "phase":
        return header + compact_resolve_phase_ids(wrapped)
    if etype == "solvent":
        return header + compact_resolve_solvent_ids(wrapped)
    if etype == "block_type":
        return header + _compact_block_type_ids(wrapped)
    if etype == "reaction_type":
        return header + _compact_reaction_type_ids(wrapped)
    raise ValueError(
        f"search_id_alignment returned unsupported entity_type {etype!r}"
    )


# ═══════════════════════════════════════════════════════════════
#  Card and extracted-data tool compactors
# ═══════════════════════════════════════════════════════════════

def _compact_embedded_cards(
    data: dict,
    *,
    tool_name: str,
    identity_fields: tuple[str, ...],
    require_match_type: bool = True,
) -> str:
    """Render the exact embedded ``compact_md`` payload for card searches."""
    if not isinstance(data, dict):
        raise TypeError(f"{tool_name} result must be an object")
    results = data.get("results")
    if not isinstance(results, list):
        raise ValueError(f"{tool_name} result is missing its results list")
    n = data.get("n_results")
    if n != len(results):
        raise ValueError(
            f"{tool_name} n_results={n!r} does not match {len(results)} result rows"
        )
    if not results:
        note = data.get("note")
        return f"**{tool_name}: 0 results.**" + (f"\n\n{note}" if note else "") + "\n"

    header = "| # | " + " | ".join(identity_fields) + " | Score | Match |"
    divider = "|---|" + "|".join("---" for _ in identity_fields) + "|---:|---|"
    table = [header, divider]
    cards: list[str] = []
    for index, row in enumerate(results, 1):
        if not isinstance(row, dict):
            raise TypeError(f"{tool_name}.results[{index - 1}] must be an object")
        required = identity_fields + ("compact_md", "match_score")
        if require_match_type:
            required += ("match_type",)
        _require_fields(row, required, f"{tool_name}.results[{index - 1}]")
        compact_md = row["compact_md"]
        if not isinstance(compact_md, str) or not compact_md.strip():
            raise ValueError(
                f"{tool_name}.results[{index - 1}] has no canonical compact_md"
            )
        identity = [str(row[field]) for field in identity_fields]
        match_type = row["match_type"] if require_match_type else ""
        table.append(
            f"| {index} | " + " | ".join(identity) +
            f" | {row['match_score']} | {match_type} |"
        )
        cards.append(f"\n---\n{compact_md.strip()}")
    return f"{tool_name}: {n} result(s).\n\n" + "\n".join(table + cards) + "\n"


def _agent_text(value: Any, *, limit: int = 180) -> str:
    """Return a single-line, word-bounded value for an agent context projection."""
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(text) <= limit:
        return text
    boundary = text.rfind(" ", 0, limit - 1)
    if boundary < max(24, limit // 2):
        boundary = limit - 1
    return text[:boundary].rstrip(" ,;:") + " …"


def _agent_list(value: Any, *, max_items: int = 2, item_limit: int = 150) -> str:
    """Render a bounded list while making omitted cardinality explicit."""
    if not isinstance(value, list):
        return _agent_text(value, limit=item_limit)
    rendered = [_agent_text(item, limit=item_limit) for item in value[:max_items]]
    if len(value) > max_items:
        rendered.append(f"(+{len(value) - max_items} more in canonical card)")
    return "; ".join(item for item in rendered if item)


def _measurement_agent_projection(row: dict, *, budget: int) -> str:
    """Project a measurement DK card into bounded, chemistry-useful context.

    Measurement domain cards are deliberately rich and can exceed the complete
    ReAct result budget individually.  The working agent needs method scope,
    applicability, performance, interpretation, and uncertainty—not a second
    copy of every apparatus and prose field.  This projection selects those
    fields deterministically and omits only at field boundaries.  The canonical
    card remains the source of record and is never modified.
    """
    identity = row.get("identity")
    knowledge = row.get("domain_knowledge")
    if not isinstance(identity, dict) or not isinstance(knowledge, dict):
        raise ValueError(
            "search_measurement_dk result is missing identity/domain_knowledge objects"
        )
    structured = knowledge.get("structured_block")
    if not isinstance(structured, dict):
        raise ValueError(
            "search_measurement_dk domain_knowledge is missing structured_block"
        )

    usage = identity.get("db_usage") if isinstance(identity.get("db_usage"), dict) else {}
    modality = identity.get("modality") if isinstance(identity.get("modality"), dict) else {}
    lines = [
        f"### {row['meas_num_id']} — {_agent_text(identity.get('name') or row['meas_id'], limit=160)}",
        f"- canonical ID: `{row['meas_id']}`; family: {_agent_text(identity.get('measurement_family'), limit=100)}",
        "- modality: " + ", ".join(f"{key}={value}" for key, value in modality.items()),
        f"- database use: {usage.get('instance_count', 0)} instances across {usage.get('n_papers', 0)} papers",
    ]

    scope = structured.get("measurement_scope")
    if isinstance(scope, dict):
        lines.append("- measurement scope:")
        for key in (
            "direct_observables", "derived_observables", "target_properties",
            "phases_measured", "supported_sample_types", "unsupported_sample_types",
        ):
            if scope.get(key):
                lines.append(f"  - {key}: {_agent_list(scope[key])}")

    experimental = structured.get("experimental_parameters")
    if isinstance(experimental, dict):
        for key in ("constraints", "variables"):
            values = experimental.get(key)
            if isinstance(values, list) and values:
                summaries = []
                for item in values[:2]:
                    if isinstance(item, dict):
                        label = item.get("parameter") or item.get("name") or key
                        detail = item.get("typical_range") or item.get("typical_values") or item.get("effect")
                        summaries.append(f"{label}: {_agent_text(detail, limit=135)}")
                if len(values) > 2:
                    summaries.append(f"(+{len(values) - 2} more in canonical card)")
                lines.append(f"- {key}: " + "; ".join(summaries))

    performance = structured.get("performance")
    if isinstance(performance, dict):
        for key in ("dynamic_range", "accuracy", "precision", "throughput"):
            if performance.get(key):
                lines.append(f"- {key}: {_agent_text(performance[key], limit=190)}")

    interpretation = structured.get("data_and_interpretation")
    if isinstance(interpretation, dict):
        if interpretation.get("raw_signal_type"):
            lines.append(f"- raw signal: {_agent_text(interpretation['raw_signal_type'], limit=220)}")
        for key in (
            "analysis_methods", "model_assumptions", "common_artifacts",
            "quality_control_checks", "failure_modes",
        ):
            if interpretation.get(key):
                lines.append(f"- {key}: {_agent_list(interpretation[key])}")

    uncertainty = structured.get("uncertainty")
    if isinstance(uncertainty, dict):
        if uncertainty.get("level"):
            lines.append(f"- uncertainty: {_agent_text(uncertainty['level'], limit=220)}")
        for key in ("dominant_error_sources", "reported_as"):
            if uncertainty.get(key):
                lines.append(f"- {key}: {_agent_list(uncertainty[key])}")

    selected: list[str] = []
    used = 0
    omission = "- [additional structured fields remain available in the canonical measurement card]"
    for line in lines:
        addition = len(line) + 1
        if used + addition + len(omission) + 1 > budget:
            selected.append(omission)
            break
        selected.append(line)
        used += addition
    return "\n".join(selected)


def _compact_measurement_dk_cards(data: dict) -> str:
    """Render measurement DK matches within the global ReAct result ceiling."""
    if not isinstance(data, dict):
        raise TypeError("search_measurement_dk result must be an object")
    results = data.get("results")
    if not isinstance(results, list):
        raise ValueError("search_measurement_dk result is missing its results list")
    n = data.get("n_results")
    if n != len(results):
        raise ValueError(
            f"search_measurement_dk n_results={n!r} does not match {len(results)} result rows"
        )
    if not results:
        note = data.get("note")
        return "**search_measurement_dk: 0 results.**" + (f"\n\n{note}" if note else "") + "\n"

    table = [
        "| # | meas_num_id | meas_id | Score | Match |",
        "|---|---|---|---:|---|",
    ]
    per_card_budget = min(12_000, max(3_500, 21_000 // len(results) - 350))
    cards: list[str] = []
    for index, row in enumerate(results, 1):
        if not isinstance(row, dict):
            raise TypeError(f"search_measurement_dk.results[{index - 1}] must be an object")
        _require_fields(
            row,
            ("meas_num_id", "meas_id", "match_score", "match_type", "identity", "domain_knowledge"),
            f"search_measurement_dk.results[{index - 1}]",
        )
        table.append(
            f"| {index} | {row['meas_num_id']} | {row['meas_id']} | "
            f"{row['match_score']} | {row['match_type']} |"
        )
        cards.append("\n---\n" + _measurement_agent_projection(row, budget=per_card_budget))
    rendered = "search_measurement_dk: " + str(n) + " result(s).\n\n" + "\n".join(table + cards) + "\n"
    if len(rendered) > 22_000:
        raise ValueError(
            "search_measurement_dk deterministic projection exceeded its 22,000-character invariant"
        )
    return rendered


@_compacts("search_compound_dk")
def compact_search_compound_dk(data: dict) -> str:
    return _compact_embedded_cards(
        data, tool_name="search_compound_dk", identity_fields=("comp_num_id",)
    )


@_compacts("search_property_dk")
def compact_search_property_dk(data: dict) -> str:
    return _compact_embedded_cards(
        data, tool_name="search_property_dk", identity_fields=("prop_num_id", "prop_id")
    )


@_compacts("search_measurement_dk")
def compact_search_measurement_dk(data: dict) -> str:
    return _compact_measurement_dk_cards(data)


@_compacts("search_references")
def compact_search_references(data: dict) -> str:
    return _compact_embedded_cards(
        data,
        tool_name="search_references",
        identity_fields=("lit_num_id", "doi"),
        require_match_type=False,
    )


@_compacts("search_compound_indiv")
def compact_search_compound_indiv(data: dict) -> str:
    payload = _require_object(data, "search_compound_indiv result")
    results, _ = _require_results(payload, "search_compound_indiv")
    flattened = dict(payload)
    flattened["results"] = []
    for index, row in enumerate(results):
        _require_fields(row, ("compound",), f"search_compound_indiv.results[{index}]")
        compound = _require_object(
            row["compound"], f"search_compound_indiv.results[{index}].compound"
        )
        _require_fields(
            compound,
            ("org_num", "comp_num_id"),
            f"search_compound_indiv.results[{index}].compound",
        )
        flattened["results"].append({
            **row,
            "org_num": compound["org_num"],
            "comp_num_id": compound["comp_num_id"],
        })
    return _compact_embedded_cards(
        flattened,
        tool_name="search_compound_indiv",
        identity_fields=("lit_num_id", "doi", "org_num", "comp_num_id"),
    )


@_compacts("search_measurement_indiv")
def compact_search_measurement_indiv(data: dict) -> str:
    return _compact_embedded_cards(
        data,
        tool_name="search_measurement_indiv",
        identity_fields=("lit_num_id", "doi"),
    )


@_compacts("extract_block_csv")
def compact_extract_block_csv(data: dict) -> str:
    if not isinstance(data, dict):
        raise TypeError("extract_block_csv result must be an object")
    if "error" in data and data["error"]:
        required_error = {"doi", "block_number", "error"}
        missing_error = required_error - data.keys()
        if missing_error:
            raise ValueError(
                f"extract_block_csv error result is missing {sorted(missing_error)}"
            )
        return (
            f"**extract_block_csv failed for {data['doi']} / "
            f"{data['block_number']}:** {data['error']}\n"
        )
    required = ("doi", "block_number", "columns", "n_rows", "metadata", "csv_text")
    missing = [field for field in required if field not in data]
    if missing:
        raise ValueError(f"extract_block_csv result is missing {missing}")
    metadata = json.dumps(data["metadata"], indent=2, ensure_ascii=False)
    return (
        f"# Extracted block: {data['doi']} / {data['block_number']}\n\n"
        f"- rows: {data['n_rows']}\n"
        f"- columns: {', '.join(data['columns'])}\n\n"
        f"## Scoped metadata\n\n```json\n{metadata}\n```\n\n"
        f"## Data\n\n```csv\n{data['csv_text'].rstrip()}\n```\n"
    )


@_compacts("extract_multi_block_csv")
def compact_extract_multi_block_csv(data: dict) -> str:
    if not isinstance(data, dict):
        raise TypeError("extract_multi_block_csv result must be an object")
    required = ("columns", "n_rows", "per_block", "errors", "csv_text")
    missing = [field for field in required if field not in data]
    if missing:
        raise ValueError(f"extract_multi_block_csv result is missing {missing}")
    per_block = json.dumps(data["per_block"], indent=2, ensure_ascii=False)
    errors = "\n".join(f"- {error}" for error in data["errors"])
    return (
        f"# Extracted multi-block table\n\n"
        f"- rows: {data['n_rows']}\n"
        f"- columns: {', '.join(data['columns'])}\n\n"
        f"## Per-block provenance\n\n```json\n{per_block}\n```\n\n"
        + (f"## Errors\n\n{errors}\n\n" if errors else "")
        + f"## Data\n\n```csv\n{data['csv_text'].rstrip()}\n```\n"
    )


@_compacts("resolve_card_md")
def compact_resolve_card_md(data: str) -> str:
    if not isinstance(data, str) or not data.strip():
        raise TypeError("resolve_card_md must return non-empty markdown")
    return data


@_compacts("inspect_block_table")
def compact_inspect_block_table(data: dict) -> str:
    """Deterministic passthrough — the truth table is never LLM-triaged."""
    if not isinstance(data, dict):
        raise TypeError("inspect_block_table result must be an object")
    markdown = data.get("markdown")
    if not isinstance(markdown, str) or not markdown.strip():
        raise ValueError("inspect_block_table result is missing rendered markdown")
    if not data.get("error"):
        required = (
            "doi", "block_number", "rows_shown", "table_mode",
            "stats", "inspection_id",
        )
        missing = [field for field in required if field not in data]
        if missing:
            raise ValueError(
                f"inspect_block_table result is missing {missing}"
            )
    return markdown


# ═══════════════════════════════════════════════════════════════
#  Block / Registry / Summary Search compactors
# ═══════════════════════════════════════════════════════════════

@_compacts("search_blocks")
def compact_search_blocks(data: dict) -> str:
    """Assemble compact_md from each result with 2-level condensation."""
    results, n = _require_results(data, "search_blocks")
    if n == 0:
        note = data.get("note")
        if isinstance(note, str) and note.strip():
            return ("**search_blocks: 0 results returned.**\n\n"
                    f"**Note:** {note.strip()}\n")
        return "**search_blocks: 0 results returned.**\n"

    parts = [f"search_blocks: {n} search targets found.\n"]

    table = ["| # | DOI | Block | Target | System | Points | Properties | Score |",
             "|---|-----|-------|--------|--------|--------|------------|-------|"]
    for i, r in enumerate(results, 1):
        _require_fields(
            r,
            (
                "doi", "block_number", "BLKsubsys_id", "search_scope",
                "system_type", "n_datapoints", "properties", "match_score",
                "compact_md",
            ),
            f"search_blocks.results[{i - 1}]",
        )
        props = r["properties"]
        if not isinstance(props, list):
            raise TypeError(f"search_blocks.results[{i - 1}].properties must be an array")
        prop_str = ", ".join(
            _require_object(p, f"search_blocks.results[{i - 1}].properties entry")["name"]
            for p in props[:3]
        )
        table.append(
            f"| {i} | {r['doi']} | {r['block_number']} | "
            f"{r['BLKsubsys_id'] or 'declared'} | {r['system_type']} | "
            f"{r['n_datapoints']} | {prop_str} | {r['match_score']} |"
        )
    parts.append("\n".join(table))

    block_entries: list[tuple[str, str, str]] = []
    for index, r in enumerate(results):
        md = r["compact_md"]
        if not isinstance(md, str) or not md.strip():
            raise ValueError(f"search_blocks.results[{index}].compact_md must be non-empty")
        target = r["block_number"]
        if r["BLKsubsys_id"] is not None:
            target += f" / {r['BLKsubsys_id']}"
        block_entries.append((r["doi"], target, md))

    return _apply_block_condensation(parts, block_entries)


@_compacts("search_system_registry")
def compact_search_system_registry(data: dict) -> str:
    results, n = _require_results(data, "search_system_registry")
    if n == 0:
        return "**search_system_registry: 0 results.**\n"

    parts = [f"search_system_registry: {n} search targets found.\n"]

    table = ["| # | DOI | Block | Target | Type | nComp | Compounds | Points |",
             "|---|-----|-------|--------|------|-------|-----------|--------|"]
    for i, r in enumerate(results, 1):
        _require_fields(
            r,
            ("doi", "block_number", "BLKsubsys_id", "system_type", "n_components", "compounds", "n_datapoints", "compact_md"),
            f"search_system_registry.results[{i - 1}]",
        )
        comps = r["compounds"]
        if not isinstance(comps, list):
            raise TypeError(
                f"search_system_registry.results[{i - 1}].compounds must be an array"
            )
        comp_str = ", ".join(
            _require_object(
                c, f"search_system_registry.results[{i - 1}].compounds entry"
            )["name"]
            for c in comps[:4]
        )
        table.append(
            f"| {i} | {r['doi']} | {r['block_number']} | "
            f"{r['BLKsubsys_id'] or 'declared'} | {r['system_type']} | "
            f"{r['n_components']} | {comp_str} | {r['n_datapoints']} |"
        )
    parts.append("\n".join(table))

    block_entries: list[tuple[str, str, str]] = []
    for index, r in enumerate(results):
        md = r["compact_md"]
        if not isinstance(md, str) or not md.strip():
            raise ValueError(
                f"search_system_registry.results[{index}].compact_md must be non-empty"
            )
        target = r["block_number"]
        if r["BLKsubsys_id"] is not None:
            target += f" / {r['BLKsubsys_id']}"
        block_entries.append((r["doi"], target, md))

    return _apply_block_condensation(parts, block_entries)


@_compacts("search_system_summary")
def compact_search_system_summary(data: dict) -> str:
    payload = _require_object(data, "search_system_summary result")
    _require_fields(payload, ("summary", "top_papers"), "search_system_summary result")
    summary = _require_object(payload["summary"], "search_system_summary.summary")
    _require_fields(
        summary,
        (
            "n_targets", "n_blocks", "n_subsystems", "n_papers",
            "total_matching_datapoints", "temperature_range_K",
            "pressure_range_kPa", "system_type_distribution", "property_distribution",
            "compound_cooccurrence",
        ),
        "search_system_summary.summary",
    )
    n_targets = summary["n_targets"]
    n_blocks = summary["n_blocks"]
    n_subsystems = summary["n_subsystems"]
    n_papers = summary["n_papers"]
    total_dp = summary["total_matching_datapoints"]
    t_range = summary["temperature_range_K"]
    p_range = summary["pressure_range_kPa"]
    sys_dist = _require_object(
        summary["system_type_distribution"],
        "search_system_summary.summary.system_type_distribution",
    )
    prop_dist = _require_object(
        summary["property_distribution"],
        "search_system_summary.summary.property_distribution",
    )
    query_params = _require_object(
        payload.get("query_params", {}),
        "search_system_summary.query_params",
    )
    system_scope = query_params.get("system_scope", "declared")

    header = (
        f"System summary ({system_scope} scope): {n_targets} search targets "
        f"across {n_blocks} parent blocks ({n_subsystems} subsystem targets), "
        f"{n_papers} papers, {total_dp} target-point observations, "
        f"T = {t_range} K, P = {p_range} kPa.\n"
    )
    if system_scope == "either" and n_subsystems:
        header += (
            "Parent and subsystem targets can overlap; the target-point total "
            "is not a deduplicated count of physical measurements.\n"
        )

    if sys_dist:
        lines = ["| System type | Count |", "|-------------|-------|"]
        for stype, count in sys_dist.items():
            lines.append(f"| {stype} | {count} |")
        header += "\n" + "\n".join(lines) + "\n"

    if prop_dist:
        lines = ["| Property | Count |", "|----------|-------|"]
        for prop, count in list(prop_dist.items())[:10]:
            lines.append(f"| {prop} | {count} |")
        header += "\n" + "\n".join(lines) + "\n"

    if not isinstance(payload["top_papers"], list):
        raise TypeError("search_system_summary.top_papers must be an array")
    top = payload["top_papers"][:5]
    if top:
        lines = ["| lit_num_id | DOI | Blocks | Subsystems | Targets | Matching points |",
                 "|------------|-----|--------|------------|---------|-----------------|"]
        for p in top:
            p = _require_object(p, "search_system_summary.top_papers entry")
            _require_fields(
                p,
                ("lit_num_id", "doi", "n_blocks", "n_subsystems", "n_targets", "total_matching_datapoints"),
                "top paper",
            )
            lines.append(
                f"| {p['lit_num_id']} | {p['doi']} | {p['n_blocks']} | "
                f"{p['n_subsystems']} | {p['n_targets']} | "
                f"{p['total_matching_datapoints']} |"
            )
        header += "\n" + "\n".join(lines) + "\n"

    if not isinstance(summary["compound_cooccurrence"], list):
        raise TypeError("search_system_summary.summary.compound_cooccurrence must be an array")
    cooc = summary["compound_cooccurrence"][:10]
    if cooc:
        lines = ["| comp_num_id | Name | n_targets |",
                 "|-------------|------|-----------|"]
        for c in cooc:
            c = _require_object(c, "compound_cooccurrence entry")
            _require_fields(c, ("comp_num_id", "name", "n_targets"), "compound_cooccurrence entry")
            lines.append(
                f"| {c['comp_num_id']} | {c['name']} | {c['n_targets']} |"
            )
        header += "\n" + "\n".join(lines) + "\n"

    return header


# ═══════════════════════════════════════════════════════════════
#  Compound Similarity
# ═══════════════════════════════════════════════════════════════

@_compacts("search_similar_compounds")
def compact_search_similar_compounds(data: dict) -> str:
    payload = _require_object(data, "search_similar_compounds result")
    _require_fields(payload, ("query", "metric"), "search_similar_compounds result")
    query = _require_object(payload["query"], "search_similar_compounds.query")
    query_schemas = (
        {"comp_num_id", "name", "smiles"},
        {"name", "smiles"},
        {"inchi", "smiles"},
        {"smiles"},
    )
    if set(query) not in query_schemas:
        raise ValueError(
            "search_similar_compounds.query must match exactly one supported "
            "query mode"
        )
    metric = payload["metric"]
    results, n = _require_results(payload, "search_similar_compounds")
    if n == 0:
        return f"**search_similar_compounds({query}): 0 results.**\n"

    lines = ["| # | comp_num_id | Name | Formula | Similarity | Papers |",
             "|---|-------------|------|---------|------------|--------|"]
    for i, r in enumerate(results[:20], 1):
        _require_fields(
            r,
            (
                "comp_num_id", "inchi_key", "common_name", "formula", "smiles",
                "similarity", "n_papers",
            ),
            f"search_similar_compounds.results[{i - 1}]",
        )
        sim = r["similarity"]
        if isinstance(sim, float):
            sim = f"{sim:.4f}"
        lines.append(
            f"| {i} | {r['comp_num_id']} | {r['common_name']} | {r['formula']} | "
            f"{sim} | {r['n_papers']} |"
        )

    if "comp_num_id" in query:
        query_label = f"{query['comp_num_id']} / {query['name']}"
    elif "name" in query:
        query_label = query["name"]
    elif "inchi" in query:
        query_label = query["inchi"]
    else:
        query_label = query["smiles"]
    header = f"Similar to {query_label} ({metric}): {n} found.\n\n"
    return header + "\n".join(lines) + "\n"
