"""
Compactors for block-centric search tools — dict→markdown formatters.
=====================================================================
Each function takes a raw tool result dict and returns a compact
markdown string.  Tagged with ``@_compacts(...)`` for auto-wiring.
"""

from __future__ import annotations

from functools import wraps


# ── Decorator — sets fn._compacts_tools (same contract as catalog.compacts) ─
def _compacts(*tools: str):
    """Tag a compactor and preserve strict ID-refinement errors."""
    def _deco(fn):
        @wraps(fn)
        def _wrapped(data, *args, **kwargs):
            if isinstance(data, dict) and data.get("error_code") == "ID_REFINEMENT_REQUIRED":
                refinement = data.get("refinement")
                if not isinstance(refinement, dict):
                    raise ValueError("ID refinement result is missing refinement object")
                required = ("field", "received", "expected", "reason")
                missing = [field for field in required if field not in refinement]
                if missing:
                    raise ValueError(f"ID refinement result is missing fields {missing}")
                return (
                    "**ID_REFINEMENT_REQUIRED**\n\n"
                    f"- field: `{refinement['field']}`\n"
                    f"- received: `{refinement['received']}`\n"
                    f"- expected: `{refinement['expected']}`\n"
                    f"- reason: {refinement['reason']}\n"
                )
            return fn(data, *args, **kwargs)

        _wrapped._compacts_tools = tools
        return _wrapped
    return _deco


def _require_payload(data: dict, fields: tuple[str, ...], tool_name: str) -> dict:
    if not isinstance(data, dict):
        raise TypeError(f"{tool_name} result must be an object")
    required = tuple(fields) + ("BLKsubsys_id",)
    missing = [field for field in required if field not in data]
    if missing:
        raise ValueError(f"{tool_name} result is missing required fields {missing}")
    subsystem = data["BLKsubsys_id"]
    if subsystem is not None and not isinstance(subsystem, str):
        raise TypeError(f"{tool_name}.BLKsubsys_id must be text or null")
    result = dict(data)
    result["block_number"] = (
        str(result["block_number"]) + " @ " + str(subsystem or "declared")
    )
    return result


def _render_dk_rows(rows: list, id_field: str, context: str) -> str:
    if not isinstance(rows, list):
        raise TypeError(f"{context} must be an array")
    parts: list[str] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or id_field not in row or "md" not in row:
            raise ValueError(
                f"{context}[{index}] must contain {id_field!r} and 'md'"
            )
        if not isinstance(row["md"], str) or not row["md"].strip():
            raise ValueError(f"{context}[{index}].md must be non-empty")
        parts.append(f"### {row[id_field]}\n\n{row['md'].strip()}")
    return "\n\n".join(parts)


_MEASUREMENT_SECTION_WEIGHTS = {
    "measurement_scope": 0.20,
    "experimental_parameters": 0.15,
    "setup_and_requirements": 0.15,
    "performance": 0.10,
    "data_and_interpretation": 0.25,
    "uncertainty": 0.15,
}


def _bounded_measurement_section(lines: list[str], budget: int) -> str:
    """Keep labeled chemistry facts from one MTDKS section within *budget*."""
    selected: list[str] = []
    used = 0
    bullets_for_label = 0
    omitted = False
    omission = "- [additional canonical measurement details omitted]"

    for source_line in lines:
        line = source_line.strip()
        if not line:
            continue
        if line.startswith("### ") or line.startswith("**"):
            bullets_for_label = 0
            limit = 520
        elif line.startswith("- "):
            if bullets_for_label >= 2:
                omitted = True
                continue
            bullets_for_label += 1
            limit = 360
        else:
            # Narrative description cards duplicate the structured fields and
            # are intentionally excluded from this block-search projection.
            omitted = True
            continue
        clipped = line if len(line) <= limit else line[: limit - 1].rstrip() + "…"
        addition = len(clipped) + 1
        if used + addition + len(omission) + 1 > budget:
            omitted = True
            break
        selected.append(clipped)
        used += addition

    if omitted and used + len(omission) + 1 <= budget:
        selected.append(omission)
    return "\n".join(selected)


def _compact_measurement_dk_markdown(md: str, *, budget: int) -> str:
    """Project a full MTDKS-DK markdown card into bounded reasoning context.

    Every structured chemistry section receives an explicit share of the
    budget.  This prevents early apparatus prose from crowding out uncertainty
    and data-interpretation evidence, while retaining the canonical card as the
    source of truth outside the ReAct context window.
    """
    if not isinstance(md, str) or not md.strip():
        raise ValueError("measurement DK markdown must be non-empty")
    if budget < 2_500:
        raise ValueError("measurement DK projection budget must be at least 2500")

    prelude: list[str] = []
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for source_line in md.splitlines():
        line = source_line.strip()
        if line == "## Description":
            break
        if line.startswith("### "):
            current = line[4:].strip()
            sections[current] = [line]
        elif current is None:
            if line and line != "## Structured Knowledge":
                prelude.append(line)
        else:
            sections[current].append(line)

    prelude_budget = min(1_600, max(700, budget // 10))
    parts = [_bounded_measurement_section(prelude, prelude_budget)]
    remaining = budget - prelude_budget
    for name, weight in _MEASUREMENT_SECTION_WEIGHTS.items():
        lines = sections.get(name, [f"### {name}", "- [section unavailable]"])
        section_budget = max(300, int(remaining * weight))
        parts.append(_bounded_measurement_section(lines, section_budget))

    rendered = "\n\n".join(part for part in parts if part).strip()
    if len(rendered) > budget:
        raise ValueError("measurement DK projection exceeded its assigned budget")
    return rendered


def _render_measurement_dk_rows(rows: list, *, budget: int) -> str:
    if not isinstance(rows, list):
        raise TypeError("search_meas_from_block.mtdks_dk must be an array")
    if not rows:
        return "(no global measurement cards)"
    per_card = max(2_500, budget // len(rows) - 120)
    parts: list[str] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or "meas_num_id" not in row or "md" not in row:
            raise ValueError(
                f"search_meas_from_block.mtdks_dk[{index}] must contain "
                "'meas_num_id' and 'md'"
            )
        projection = _compact_measurement_dk_markdown(row["md"], budget=per_card)
        parts.append(f"### {row['meas_num_id']}\n\n{projection}")
    rendered = "\n\n".join(parts)
    if len(rendered) > budget:
        raise ValueError("measurement DK rows exceeded their combined budget")
    return rendered


@_compacts("search_comp_from_block")
def compact_search_comp_from_block(data: dict) -> str:
    payload = _require_payload(
        data,
        ("doi", "lit_num_id", "block_number", "comp_num_ids", "ccs_indiv_md", "ccs_dk"),
        "search_comp_from_block",
    )
    if not isinstance(payload["comp_num_ids"], list):
        raise TypeError("search_comp_from_block.comp_num_ids must be an array")
    if not isinstance(payload["ccs_indiv_md"], str) or not payload["ccs_indiv_md"].strip():
        raise ValueError("search_comp_from_block.ccs_indiv_md must be non-empty")
    dk = _render_dk_rows(payload["ccs_dk"], "comp_num_id", "search_comp_from_block.ccs_dk")
    return (
        f"**Compounds from {payload['doi']} / {payload['block_number']}** — "
        f"IDs: {payload['comp_num_ids']}\n\n"
        f"## DOI compound card\n\n{payload['ccs_indiv_md'].strip()}\n\n"
        f"## Global compound cards\n\n{dk}\n"
    )


@_compacts("search_meas_from_block")
def compact_search_meas_from_block(data: dict) -> str:
    payload = _require_payload(
        data,
        ("doi", "lit_num_id", "block_number", "meas_num_ids", "mtdks_indiv_md", "mtdks_dk"),
        "search_meas_from_block",
    )
    if not isinstance(payload["meas_num_ids"], list):
        raise TypeError("search_meas_from_block.meas_num_ids must be an array")
    if not isinstance(payload["mtdks_indiv_md"], str) or not payload["mtdks_indiv_md"].strip():
        raise ValueError("search_meas_from_block.mtdks_indiv_md must be non-empty")
    dk = _render_measurement_dk_rows(payload["mtdks_dk"], budget=20_000)
    rendered = (
        f"**Measurements from {payload['doi']} / {payload['block_number']}** — "
        f"lit_num_id: {payload['lit_num_id']} — IDs: {payload['meas_num_ids']}\n\n"
        f"## DOI measurement card\n\n{payload['mtdks_indiv_md'].strip()}\n\n"
        f"## Global measurement chemistry projection\n\n{dk}\n"
    )
    if len(rendered) > 22_000:
        raise ValueError(
            "search_meas_from_block deterministic projection exceeded its "
            "22,000-character invariant"
        )
    return rendered


@_compacts("search_prop_dk_from_block")
def compact_search_prop_dk_from_block(data: dict) -> str:
    payload = _require_payload(
        data,
        ("doi", "lit_num_id", "block_number", "prop_num_ids", "pcs_dk"),
        "search_prop_dk_from_block",
    )
    if not isinstance(payload["prop_num_ids"], list):
        raise TypeError("search_prop_dk_from_block.prop_num_ids must be an array")
    dk = _render_dk_rows(payload["pcs_dk"], "prop_num_id", "search_prop_dk_from_block.pcs_dk")
    return (
        f"**Properties from {payload['doi']} / {payload['block_number']}** — "
        f"IDs: {payload['prop_num_ids']}\n\n{dk}\n"
    )


@_compacts("search_reference_from_block")
def compact_search_reference_from_block(data: dict) -> str:
    payload = _require_payload(
        data,
        ("doi", "lit_num_id", "block_number", "rms_indiv_md"),
        "search_reference_from_block",
    )
    if not isinstance(payload["rms_indiv_md"], str) or not payload["rms_indiv_md"].strip():
        raise ValueError("search_reference_from_block.rms_indiv_md must be non-empty")
    return (
        f"**Reference from {payload['doi']} / {payload['block_number']}**\n\n"
        f"{payload['rms_indiv_md'].strip()}\n"
    )
