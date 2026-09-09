"""
Hardcoded dict → markdown compactors for each analysis tool.
=============================================================
Each function takes a raw tool result dict and returns a compact
markdown string suitable for the tool‐level subagent.

Block-level condensation helpers (``_condense_block_md``,
``_ultra_condense_block_md``, ``_apply_block_condensation``, etc.)
are imported from the shared library at
``card_db_search_tools._tools_results_compactors``.

**Phase 2 fitting tools** get new compactors here.

Each function is tagged with ``@compacts("tool_name")`` to declare which
tool it serves.  ``COMPACTOR_FUNCTIONS`` at the bottom lists all tagged
functions; ``CompactorCatalog.from_functions()`` auto-builds the registry.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path as _Path
from typing import Any, Dict

from ....general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import compacts

log = logging.getLogger("ANALYSIS-compactors")

# ── Import shared block-condensation helpers ────────────────────
# The shared library lives under card_db_search_tools/ at the project root.
_SEARCH_TOOLS_ROOT = _Path(__file__).resolve().parents[4] / "card_db_search_tools"
if str(_SEARCH_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_SEARCH_TOOLS_ROOT))

from _tools_results_compactors.basic_search_tools.compactors import (  # noqa: E402
    compact_search_blocks,
    compact_search_similar_compounds,
    compact_search_system_summary,
)


def _require_object(value: Any, context: str) -> dict:
    if not isinstance(value, dict):
        raise TypeError(f"{context} must be an object")
    return value


def _require_fields(row: dict, fields: tuple[str, ...], context: str) -> None:
    missing = [field for field in fields if field not in row]
    if missing:
        raise ValueError(f"{context} is missing required fields {missing}")


def _with_target_display(row: dict, context: str) -> dict:
    _require_fields(row, ("doi", "block_number", "BLKsubsys_id"), context)
    result = dict(row)
    subsystem = result["BLKsubsys_id"]
    if subsystem is not None and not isinstance(subsystem, str):
        raise TypeError(f"{context}.BLKsubsys_id must be text or null")
    result["block_number"] = (
        str(result["block_number"]) + " @ " + str(subsystem or "declared")
    )
    return result


def _source_display(row: dict) -> str:
    source = str(row["doi"])
    if "lit_num_id" in row:
        source = f"{row['lit_num_id']} / DOI {source}"
    return source


def _error_location(row: dict) -> str:
    """Location suffix for error payloads; never demands BLKsubsys_id."""
    if "doi" not in row and "block_number" not in row:
        return ""
    _require_fields(row, ("doi", "block_number"), "located error result")
    block = str(row["block_number"])
    if row.get("BLKsubsys_id") is not None:
        block += f" @ {row['BLKsubsys_id']}"
    return f" ({_source_display(row)} / {block})"


def _error_extras(row: dict) -> str:
    """Surface self-repair fields — compaction must never bury the fix hint."""
    extras = []
    if "hint" in row:
        extras.append(f"Hint: {row['hint']}")
    if "columns_available" in row:
        extras.append(f"Columns available: {row['columns_available']}")
    if "all_columns_unfiltered" in row:
        extras.append(f"All columns (unfiltered): {row['all_columns_unfiltered']}")
    return "".join(f"\n{item}" for item in extras)


def _compact_prepared_property_response(trace: Any, context: str) -> str:
    trace = _require_object(trace, context)
    _require_fields(
        trace,
        (
            "BLKprop_id", "prop_num_id", "status", "presentation_kind",
            "equation", "reference_sources", "reported_unit", "absolute_unit",
        ),
        context,
    )
    sources = trace["reference_sources"]
    if not isinstance(sources, list):
        raise TypeError(f"{context}.reference_sources must be an array")
    return (
        f"Property response: {trace['BLKprop_id']} / {trace['prop_num_id']}; "
        f"kind={trace['presentation_kind']}; equation={trace['equation']}; "
        f"reference_sources={len(sources)}; units="
        f"{trace['reported_unit'] or 'dimensionless'} -> "
        f"{trace['absolute_unit'] or 'dimensionless'}."
    )


def _compact_phase(phase: Any, context: str) -> str:
    if phase is None:
        return "none"
    phase = _require_object(phase, context)
    _require_fields(phase, ("phase", "phase_num_id", "phase_id"), context)
    rendered = (
        f"{phase['phase']} ({phase['phase_num_id']}; {phase['phase_id']})"
    )
    if "component_org_num" in phase and phase["component_org_num"] is not None:
        rendered += f", component={phase['component_org_num']}"
    return rendered


def _compact_property_response(prop: dict, context: str) -> list[str]:
    prop = _require_object(prop, context)
    _require_fields(
        prop,
        (
            "BLKprop_id", "prop_num_id", "prop_ID", "column_name",
            "presentation", "standard_state", "ref_state_type",
            "ref_temperature_K", "ref_pressure_kPa", "property_phase",
            "ref_phase", "component_org_num", "meas_num_id", "meas_ID",
        ),
        context,
    )
    reference_state = prop["ref_state_type"]
    if prop["standard_state"] is not None:
        reference_state = (
            f"{reference_state or 'none'}; standard={prop['standard_state']}"
        )
    reference_state = reference_state or "none"
    reference_conditions = (
        f"T={prop['ref_temperature_K'] if prop['ref_temperature_K'] is not None else 'unspecified'} K; "
        f"P={prop['ref_pressure_kPa'] if prop['ref_pressure_kPa'] is not None else 'unspecified'} kPa"
    )
    measurement = (
        f"{prop['meas_num_id'] or 'none'} / {prop['meas_ID'] or 'none'}"
    )
    return [
        (
            f"- **{prop['BLKprop_id']} / {prop['prop_num_id']}** "
            f"`{prop['column_name']}` ({prop['prop_ID']})"
        ),
        f"  - reported response: {prop['presentation']}",
        f"  - measurement: {measurement}",
        f"  - property phase: {_compact_phase(prop['property_phase'], context + '.property_phase')}",
        f"  - reference: {reference_state}; {reference_conditions}",
        f"  - reference phase: {_compact_phase(prop['ref_phase'], context + '.ref_phase')}",
        f"  - component_org_num: {prop['component_org_num'] or 'none'}",
    ]


def _compact_property_responses(properties: Any, context: str) -> str:
    if not isinstance(properties, list):
        raise TypeError(f"{context} must be an array")
    lines = [
        "**Property response semantics (reported metadata; values are not materialized here)**"
    ]
    for index, prop in enumerate(properties):
        lines.extend(_compact_property_response(prop, f"{context}[{index}]"))
    return "\n".join(lines) + "\n"


def _compact_property_response_contract(contract: Any, context: str) -> str:
    contract = _require_object(contract, context)
    _require_fields(
        contract,
        (
            "BLKprop_id", "prop_num_id", "quantity_key", "column_name",
            "reported_presentation", "presentation_kind", "reported_unit",
            "absolute_unit", "requires_reference_materialization",
            "requires_normalized_composition", "ref_state_type",
            "ref_temperature_K", "ref_pressure_kPa", "property_phase",
            "ref_phase", "component_org_num", "supported",
        ),
        context,
    )
    return "\n".join(
        [
            "**Selected property response contract (inspection only; values are not materialized here)**",
            (
                f"- **{contract['BLKprop_id']} / {contract['prop_num_id']}** "
                f"`{contract['column_name']}` ({contract['quantity_key']})"
            ),
            (
                f"  - reported response: {contract['reported_presentation']} "
                f"[{contract['presentation_kind']}]"
            ),
            (
                f"  - units: reported={contract['reported_unit'] or 'dimensionless'}; "
                f"absolute={contract['absolute_unit'] or 'dimensionless'}"
            ),
            (
                "  - preparation gate: reference_materialization="
                f"{contract['requires_reference_materialization']}; "
                "normalized_composition="
                f"{contract['requires_normalized_composition']}; "
                f"supported={contract['supported']}"
            ),
            (
                f"  - reference: {contract['ref_state_type'] or 'none'}; "
                f"T={contract['ref_temperature_K'] if contract['ref_temperature_K'] is not None else 'unspecified'} K; "
                f"P={contract['ref_pressure_kPa'] if contract['ref_pressure_kPa'] is not None else 'unspecified'} kPa"
            ),
            f"  - property phase: {_compact_phase(contract['property_phase'], context + '.property_phase')}",
            f"  - reference phase: {_compact_phase(contract['ref_phase'], context + '.ref_phase')}",
            f"  - component_org_num: {contract['component_org_num'] or 'none'}",
        ]
    )


# ═══════════════════════════════════════════════════════════════
#  Phase 0 — Resolve
# ═══════════════════════════════════════════════════════════════

@compacts("resolve_compounds")
def compact_resolve_compounds(data: dict) -> str:
    payload = _require_object(data, "resolve_compounds result")
    _require_fields(payload, ("resolved_compounds",), "resolve_compounds result")
    resolved = _require_object(payload["resolved_compounds"], "resolved_compounds")
    if not resolved:
        return "**No compounds could be resolved.**\n"
    lines = ["| Compound | global_id | Formula | Score |",
             "|----------|--------|---------|-------|"]
    for name, info in resolved.items():
        if not isinstance(info, list):
            raise TypeError(f"resolved_compounds[{name!r}] must be an array")
        for index, match in enumerate(info[:3]):
            match = _require_object(match, f"resolved_compounds[{name!r}][{index}]")
            _require_fields(
                match,
                ("comp_num_id", "formula", "score"),
                f"resolved_compounds[{name!r}][{index}]",
            )
            lines.append(
                f"| {name} | {match['comp_num_id']} | {match['formula']} | "
                f"{match['score']} |"
            )
    n = len(resolved)
    return f"Resolved {n} compound(s).\n\n" + "\n".join(lines) + "\n"


@compacts("resolve_properties")
def compact_resolve_properties(data: dict) -> str:
    payload = _require_object(data, "resolve_properties result")
    _require_fields(payload, ("resolved_properties",), "resolve_properties result")
    resolved = _require_object(payload["resolved_properties"], "resolved_properties")
    if not resolved:
        return "**No properties could be resolved.**\n"
    lines = ["| Property | global_id | Group | Score |",
             "|----------|--------|-------|-------|"]
    for name, info in resolved.items():
        if not isinstance(info, list):
            raise TypeError(f"resolved_properties[{name!r}] must be an array")
        for index, match in enumerate(info[:3]):
            match = _require_object(match, f"resolved_properties[{name!r}][{index}]")
            _require_fields(
                match,
                ("prop_num_id", "prop_group", "score"),
                f"resolved_properties[{name!r}][{index}]",
            )
            lines.append(
                f"| {name} | {match['prop_num_id']} | {match['prop_group']} | "
                f"{match['score']} |"
            )
    n = len(resolved)
    return f"Resolved {n} property/properties.\n\n" + "\n".join(lines) + "\n"


# ═══════════════════════════════════════════════════════════════
#  Phase 1 — Discovery
# ═══════════════════════════════════════════════════════════════

@compacts("query_system_summary")
def compact_query_system_summary(data: dict) -> str:
    return compact_search_system_summary(data)


@compacts("query_blocks")
def compact_query_blocks(data: dict) -> str:
    """Assemble existing compact_md from each result (produced by
    block_compactor.pcs_block_compact during search)."""
    return compact_search_blocks(data).replace("search_blocks:", "query_blocks:", 1)


@compacts("inspect_block")
def compact_inspect_block(data: dict) -> str:
    payload = _require_object(data, "inspect_block result")
    if "error" in payload:
        _require_fields(payload, ("doi", "block_number", "error"), "inspect_block error")
        return f"**Error:**{_error_location(payload)} {payload['error']}{_error_extras(payload)}\n"
    payload = _with_target_display(payload, "inspect_block result")
    _require_fields(
        payload,
        (
            "doi", "block_number", "block_type", "compounds", "n_rows",
            "identified_x", "identified_y", "column_ranges", "properties",
            "property_response_contracts",
        ),
        "inspect_block result",
    )
    comps = payload["compounds"]
    if not isinstance(comps, list):
        raise TypeError("inspect_block.compounds must be an array")
    comp_names: list[str] = []
    for index, compound in enumerate(comps[:6]):
        compound = _require_object(compound, f"inspect_block.compounds[{index}]")
        _require_fields(compound, ("name",), f"inspect_block.compounds[{index}]")
        comp_names.append(compound["name"])
    comp_str = ", ".join(comp_names)
    if not isinstance(payload["identified_x"], list) or not isinstance(payload["identified_y"], list):
        raise TypeError("inspect_block identified_x and identified_y must be arrays")

    source = payload["doi"]
    if "lit_num_id" in payload:
        source = f"{payload['lit_num_id']} / DOI {source}"
    header = (
        f"**Block {source} / {payload['block_number']}** ({payload['block_type']})\n"
        f"Compounds: {comp_str} | Rows: {payload['n_rows']}\n"
        f"x‑columns: {payload['identified_x']} | y‑columns: {payload['identified_y']}\n"
    )
    header += "\n" + _compact_property_responses(
        payload["properties"], "inspect_block.properties"
    )
    contracts = payload["property_response_contracts"]
    if not isinstance(contracts, list):
        raise TypeError("inspect_block.property_response_contracts must be an array")
    if contracts:
        header += "\n" + "\n\n".join(
            _compact_property_response_contract(
                contract,
                f"inspect_block.property_response_contracts[{index}]",
            )
            for index, contract in enumerate(contracts)
        ) + "\n"

    # Column ranges table
    col_ranges = _require_object(payload["column_ranges"], "inspect_block.column_ranges")
    if col_ranges:
        lines = ["| Column | Min | Max | Valid pts |",
                 "|--------|-----|-----|-----------|"]
        for col, rng in col_ranges.items():
            rng = _require_object(rng, f"inspect_block.column_ranges[{col!r}]")
            _require_fields(rng, ("min", "max", "n_valid"), f"column range {col!r}")
            mn = "" if rng["min"] is None else f"{rng['min']:.6g}"
            mx = "" if rng["max"] is None else f"{rng['max']:.6g}"
            lines.append(f"| {col} | {mn} | {mx} | {rng['n_valid']} |")
        header += "\n" + "\n".join(lines) + "\n"

    return header


@compacts("find_similar_compounds")
def compact_find_similar_compounds(data: dict) -> str:
    return compact_search_similar_compounds(data)


@compacts("get_pure_values")
def compact_get_pure_values(data: dict) -> str:
    payload = _require_object(data, "get_pure_values result")
    if "error" in payload:
        _require_fields(payload, ("doi", "block_number", "error"), "get_pure_values error")
        code = f" [{payload['error_code']}]" if "error_code" in payload else ""
        return (
            f"**Pure-value error{code}**{_error_location(payload)}: "
            f"{payload['error']}{_error_extras(payload)}\n"
        )
    payload = _with_target_display(payload, "get_pure_values result")
    _require_fields(
        payload,
        (
            "doi", "block_number", "pure_values", "edge_coverage", "y_column",
            "n_components", "components", "property_response",
        ),
        "get_pure_values result",
    )
    pure_values = _require_object(payload["pure_values"], "get_pure_values.pure_values")
    edge = _require_object(payload["edge_coverage"], "get_pure_values.edge_coverage")

    header = (
        f"**Pure values** from {_source_display(payload)} / {payload['block_number']} "
        f"({payload['n_components']} components)\n"
        f"Property column: {payload['y_column']}\n"
        f"{_compact_prepared_property_response(payload['property_response'], 'get_pure_values.property_response')}\n"
    )
    if "temperature_K" in payload:
        header += f"Temperature: {payload['temperature_K']} K\n"
    if "pressure_kPa" in payload:
        header += f"Pressure: {payload['pressure_kPa']} kPa\n"

    lines = ["| Component | Pure value | max x | n near-pure | method | quality |",
             "|-----------|-----------|-------|-------------|--------|---------|"]
    for comp, val in pure_values.items():
        if comp not in edge:
            raise ValueError(f"get_pure_values.edge_coverage is missing {comp!r}")
        ec = _require_object(edge[comp], f"edge_coverage[{comp!r}]")
        _require_fields(ec, ("max_x", "n_near_pure", "method", "quality"), f"edge_coverage[{comp!r}]")
        max_x = ec["max_x"]
        if isinstance(max_x, float):
            max_x = f"{max_x:.4f}"
        lines.append(
            f"| {comp} | {val} | {max_x} | {ec['n_near_pure']} | "
            f"{ec['method']} | {ec['quality']} |"
        )

    out = header + "\n" + "\n".join(lines) + "\n"
    if "fit_block_mapping" in payload:
        mapping = _require_object(payload["fit_block_mapping"], "fit_block_mapping")
        _require_fields(mapping, ("x_column", "pure_at_x0", "pure_at_x1"), "fit_block_mapping")
        out += (
            f"Axis: {mapping['x_column']} — x=0 is pure {mapping['pure_at_x0']}, "
            f"x=1 is pure {mapping['pure_at_x1']}. Pass pure_values directly "
            f"to fit_block.\n"
        )
    if "applied_constraints" in payload:
        out += f"Constraints applied: {payload['applied_constraints']}\n"
    if "temperature_note" in payload:
        out += f"⚠ {payload['temperature_note']}\n"
    return out


# ═══════════════════════════════════════════════════════════════
#  Phase 2 — Fitting
# ═══════════════════════════════════════════════════════════════


def _fmt_bic_table(bic_analysis: list) -> str:
    """Format BIC analysis into a markdown table."""
    if not bic_analysis:
        return ""
    lines = ["| Order | BIC | R² | RMSE |",
             "|-------|-----|----|------|"]
    if not isinstance(bic_analysis, list):
        raise TypeError("bic_analysis must be an array")
    for index, entry in enumerate(bic_analysis):
        entry = _require_object(entry, f"bic_analysis[{index}]")
        _require_fields(
            entry, ("order", "bic", "r_squared", "rmse"), f"bic_analysis[{index}]"
        )
        bic = f"{entry['bic']:.2f}" if isinstance(entry["bic"], float) else entry["bic"]
        r2 = (
            f"{entry['r_squared']:.6f}"
            if isinstance(entry["r_squared"], float)
            else entry["r_squared"]
        )
        rmse = f"{entry['rmse']:.6g}" if isinstance(entry["rmse"], float) else entry["rmse"]
        lines.append(f"| {entry['order']} | {bic} | {r2} | {rmse} |")
    return "\n".join(lines) + "\n"


def _fmt_single_fit(data: dict) -> str:
    """Format a single-baseline fit_block result."""
    _require_fields(
        data,
        (
            "doi", "block_number", "components", "mixing_rule",
            "n_mixture_points", "n_total_points", "rk_coeffs", "rk_order",
            "r_squared", "rmse", "bic", "pure_values", "pure_values_source",
            "bic_analysis", "property_response",
        ),
        "single fit result",
    )
    source = _source_display(data)
    bn = data["block_number"]
    comps = data["components"]
    rule = data["mixing_rule"]
    n_mix = data["n_mixture_points"]
    n_total = data["n_total_points"]
    coeffs = data["rk_coeffs"]
    order = data["rk_order"]
    r2 = data["r_squared"]
    rmse = data["rmse"]
    bic = data["bic"]
    pv = _require_object(data["pure_values"], "single fit pure_values")
    if not isinstance(comps, list) or not isinstance(coeffs, list):
        raise TypeError("single fit components and rk_coeffs must be arrays")

    if isinstance(r2, float):
        r2 = f"{r2:.6f}"
    if isinstance(rmse, float):
        rmse = f"{rmse:.6g}"
    if isinstance(bic, float):
        bic = f"{bic:.2f}"
    coeffs_str = ", ".join(f"{c:.6g}" if isinstance(c, float) else str(c)
                           for c in coeffs)

    header = (
        f"**RK Fit** — {source} / {bn}\n"
        f"Components: {', '.join(comps)} | Mixing rule: {rule}\n"
        f"Points: {n_mix} mixture / {n_total} total\n"
        f"{_compact_prepared_property_response(data['property_response'], 'single fit property_response')}\n"
    )

    # Pure values
    pv_lines = ["| Component | Pure value |", "|-----------|-----------|"]
    for comp, val in pv.items():
        pv_lines.append(f"| {comp} | {val} |")
    header += "\n" + "\n".join(pv_lines) + "\n"
    if data["pure_values_source"]:
        header += f"Pure values: {data['pure_values_source']}\n"
    if "pure_values_note" in data:
        header += f"⚠ {data['pure_values_note']}\n"

    # Fit results
    header += (
        f"\nBIC-selected order: {order} | R² = {r2} | RMSE = {rmse} | BIC = {bic}\n"
        f"Coefficients: [{coeffs_str}]\n"
    )

    # BIC analysis table
    bic_tbl = _fmt_bic_table(data["bic_analysis"])
    if bic_tbl:
        header += f"\n{bic_tbl}"

    return header


@compacts("fit_block", "fit_block_derived")
def compact_fit_block(data: dict) -> str:
    data = _require_object(data, "fit result")
    if "error" in data:
        code = f" [{data['error_code']}]" if "error_code" in data else ""
        return (
            f"**Fit error{code}**{_error_location(data)}: "
            f"{data['error']}{_error_extras(data)}\n"
        )
    data = _with_target_display(data, "fit result")

    # ── Temperature / constraint sweep mode ───────────────────
    if "per_sweep_value" in data:
        return _fmt_sweep_fit(data)

    # ── Multi-property mode ───────────────────────────────────
    if "n_properties" in data or "results" in data:
        _require_fields(data, ("n_properties", "results"), "multi-property fit result")
        return _fmt_multi_property_fit(data)

    # ── Dual-baseline path ────────────────────────────────────
    if data.get("mixing_rule") == "both":
        _require_fields(
            data,
            (
                "doi", "block_number", "components", "n_mixture_points",
                "fit_linear", "fit_arrhenius", "property_response",
            ),
            "dual-baseline fit result",
        )
        header = (
            f"**Dual-baseline RK Fit** — {_source_display(data)} / {data['block_number']}\n"
            f"Components: {', '.join(data['components'])} | "
            f"Points: {data['n_mixture_points']} mixture\n\n"
            f"{_compact_prepared_property_response(data['property_response'], 'dual fit property_response')}\n\n"
        )
        for key in ("fit_linear", "fit_arrhenius"):
            sub = _require_object(data[key], key)
            if "error" in sub:
                header += f"**{key}:** error — {sub['error']}\n\n"
                continue
            _require_fields(
                sub,
                ("mixing_rule", "rk_coeffs", "rk_order", "r_squared", "rmse", "bic_analysis"),
                key,
            )
            rule = sub["mixing_rule"]
            coeffs = sub["rk_coeffs"]
            order = sub["rk_order"]
            r2 = sub["r_squared"]
            rmse = sub["rmse"]
            if isinstance(r2, float):
                r2 = f"{r2:.6f}"
            if isinstance(rmse, float):
                rmse = f"{rmse:.6g}"
            coeffs_str = ", ".join(
                f"{c:.6g}" if isinstance(c, float) else str(c) for c in coeffs
            )
            header += (
                f"**{rule}**: order={order}, R²={r2}, RMSE={rmse}, "
                f"coeffs=[{coeffs_str}]\n"
            )
            bic_tbl = _fmt_bic_table(sub["bic_analysis"])
            if bic_tbl:
                header += f"\n{bic_tbl}\n"
        return header

    # ── Single-baseline path ──────────────────────────────────
    return _fmt_single_fit(data)


def _fmt_multi_property_fit(data: dict) -> str:
    """Format multi-property fit results."""
    _require_fields(
        data, ("doi", "block_number", "n_properties", "results"),
        "multi-property fit result",
    )
    n = data["n_properties"]
    results = _require_object(data["results"], "multi-property results")

    header = (
        f"**Multi-property RK Fit** — {_source_display(data)} / {data['block_number']} — "
        f"{n} properties\n"
    )

    lines = ["| Property | Order | R² | RMSE | n pts | Mixing rule |",
             "|----------|-------|----|------|-------|-------------|"]
    for label, fit in results.items():
        fit = _require_object(fit, f"multi-property results[{label!r}]")
        if "error" in fit:
            lines.append(f"| {label} | ERROR: {fit['error'][:40]} | | | |")
            continue
        _require_fields(
            fit,
            (
                "rk_order", "r_squared", "rmse", "n_mixture_points",
                "mixing_rule", "rk_coeffs", "property_response",
            ),
            f"multi-property results[{label!r}]",
        )
        order = fit["rk_order"]
        r2 = fit["r_squared"]
        rmse = fit["rmse"]
        npt = fit["n_mixture_points"]
        rule = fit["mixing_rule"]
        if isinstance(r2, float):
            r2 = f"{r2:.6f}"
        if isinstance(rmse, float):
            rmse = f"{rmse:.6g}"
        lines.append(f"| {label} | {order} | {r2} | {rmse} | {npt} | {rule} |")

    header += "\n" + "\n".join(lines) + "\n"

    for label, fit in results.items():
        if "error" in fit:
            continue
        coeffs = fit["rk_coeffs"]
        coeffs_str = ", ".join(
            f"{c:.6g}" if isinstance(c, float) else str(c) for c in coeffs
        )
        header += f"\n**{label}** coeffs: [{coeffs_str}]\n"
        header += (
            _compact_prepared_property_response(
                fit["property_response"], f"multi-property {label} property_response"
            )
            + "\n"
        )

    return header


def _fmt_sweep_fit(data: dict) -> str:
    """Format constraint-sweep (e.g. temperature) fit results."""
    _require_fields(
        data,
        ("doi", "block_number", "components", "sweep_column", "n_sweep_values", "mixing_rule", "per_sweep_value"),
        "sweep fit result",
    )
    source = _source_display(data)
    bn = data["block_number"]
    comps = data["components"]
    sweep_col = data["sweep_column"]
    n_vals = data["n_sweep_values"]
    rule = data["mixing_rule"]
    per_val = data["per_sweep_value"]
    if not isinstance(comps, list) or not isinstance(per_val, list):
        raise TypeError("sweep components and per_sweep_value must be arrays")

    header = (
        f"**Sweep RK Fit** — {source} / {bn}\n"
        f"Components: {', '.join(comps)} | {n_vals} values of {sweep_col} | "
        f"Mixing rule: {rule}\n"
    )

    lines = [f"| {sweep_col} | Order | R² | RMSE | n pts | Coefficients |",
             "|-------|-------|----|------|-------|--------------|"]
    for index, entry in enumerate(per_val):
        entry = _require_object(entry, f"per_sweep_value[{index}]")
        _require_fields(entry, ("sweep_value",), f"per_sweep_value[{index}]")
        V = entry["sweep_value"]
        if "error" in entry:
            lines.append(f"| {V} | ERROR: {entry['error'][:40]} | | | |")
            continue
        _require_fields(
            entry,
            (
                "rk_order", "r_squared", "rmse", "n_mixture_points",
                "rk_coeffs", "property_response",
            ),
            f"per_sweep_value[{index}]",
        )
        order = entry["rk_order"]
        r2 = entry["r_squared"]
        rmse = entry["rmse"]
        npt = entry["n_mixture_points"]
        coeffs = entry["rk_coeffs"]
        if isinstance(r2, float):
            r2 = f"{r2:.6f}"
        if isinstance(rmse, float):
            rmse = f"{rmse:.6g}"
        coeffs_str = ", ".join(
            f"{c:.6g}" if isinstance(c, float) else str(c) for c in coeffs
        )
        lines.append(f"| {V} | {order} | {r2} | {rmse} | {npt} | [{coeffs_str}] |")

    header += "\n" + "\n".join(lines) + "\n"
    response_lines = []
    for index, entry in enumerate(per_val):
        if "error" in entry:
            continue
        response_lines.append(
            f"{sweep_col}={entry['sweep_value']}: "
            + _compact_prepared_property_response(
                entry["property_response"],
                f"per_sweep_value[{index}].property_response",
            )
        )
    if response_lines:
        header += "\n" + "\n".join(response_lines[:6]) + "\n"
        if len(response_lines) > 6:
            header += f"... {len(response_lines) - 6} additional sweep response traces retained in full result.\n"
    return header


@compacts("fit_multi_system")
def compact_fit_multi_system(data: dict) -> str:
    data = _require_object(data, "fit_multi_system result")
    _require_fields(data, ("n_systems", "results", "errors"), "fit_multi_system result")
    n = data["n_systems"]
    results = data["results"]
    errors = data["errors"]
    if not isinstance(results, list) or not isinstance(errors, list):
        raise TypeError("fit_multi_system results and errors must be arrays")

    header = f"**Multi-system RK Fit** — {n} systems\n"
    if errors:
        header += f"Errors: {'; '.join(str(e) for e in errors)}\n"

    # Summary table
    lines = ["| Label | DOI | Block | Components | Order | R² | RMSE | n pts |",
             "|-------|-----|-------|------------|-------|----|------|-------|"]
    for index, row in enumerate(results):
        row = _require_object(row, f"fit_multi_system.results[{index}]")
        _require_fields(row, ("label", "fit"), f"fit_multi_system.results[{index}]")
        label = row["label"]
        fit = _require_object(row["fit"], f"fit_multi_system.results[{index}].fit")
        if "error" in fit:
            lines.append(f"| {label} | — | — | — | ERROR: {fit['error'][:40]} | | |")
            continue
        fit = _with_target_display(fit, f"fit_multi_system.results[{index}].fit")
        _require_fields(
            fit,
            (
                "doi", "block_number", "components", "rk_order", "r_squared",
                "rmse", "n_mixture_points", "rk_coeffs", "pure_values",
                "x_column", "pure_values_source", "property_response",
            ),
            f"fit_multi_system.results[{index}].fit",
        )
        source = _source_display(fit)
        bn = fit["block_number"]
        comps = ", ".join(fit["components"])
        order = fit["rk_order"]
        r2 = fit["r_squared"]
        rmse = fit["rmse"]
        npt = fit["n_mixture_points"]
        if isinstance(r2, float):
            r2 = f"{r2:.6f}"
        if isinstance(rmse, float):
            rmse = f"{rmse:.6g}"
        lines.append(f"| {label} | {source} | {bn} | {comps} | {order} | {r2} | {rmse} | {npt} |")

    header += "\n" + "\n".join(lines) + "\n"

    # Per-system coefficient detail
    for row in results:
        fit = row["fit"]
        if "error" in fit:
            continue
        label = row["label"]
        coeffs = fit["rk_coeffs"]
        coeffs_str = ", ".join(
            f"{c:.6g}" if isinstance(c, float) else str(c) for c in coeffs
        )
        header += f"\n**{label}** coeffs: [{coeffs_str}]\n"
        header += (
            _compact_prepared_property_response(
                fit["property_response"],
                f"fit_multi_system {label} property_response",
            )
            + "\n"
        )
        pv = fit["pure_values"]
        if pv:
            pv_str = ", ".join(f"{k}={v:.6g}" if isinstance(v, float) else f"{k}={v}"
                               for k, v in pv.items())
            x_col = fit["x_column"]
            header += f"  pure values (x = {x_col}): {pv_str}\n"
        if fit["pure_values_source"]:
            header += f"  source: {fit['pure_values_source']}\n"
        if "pure_values_note" in fit:
            header += f"  ⚠ {fit['pure_values_note']}\n"

    return header


@compacts("compute_ideal_baseline")
def compact_compute_ideal_baseline(data: dict) -> str:
    data = _require_object(data, "compute_ideal_baseline result")
    if "error" in data:
        return f"**Baseline error:** {data['error']}\n"
    _require_fields(
        data, ("mixing_rule", "components", "y_ideal"), "compute_ideal_baseline result"
    )
    rule = data["mixing_rule"]
    comps = data["components"]
    y_ideal = data["y_ideal"]
    if not isinstance(comps, list) or not isinstance(y_ideal, list):
        raise TypeError("baseline components and y_ideal must be arrays")
    n = len(y_ideal)

    header = (
        f"**Ideal baseline** ({rule})\n"
        f"Components: {', '.join(str(c) for c in comps)} | {n} grid points\n"
    )

    # Show endpoints + midpoint
    if n >= 3:
        header += (
            f"Y(x=0) = {y_ideal[0]:.6g}, "
            f"Y(x=0.5) ≈ {y_ideal[n//2]:.6g}, "
            f"Y(x=1) = {y_ideal[-1]:.6g}\n"
        )

    return header


@compacts("predict_from_rk")
def compact_predict_from_rk(data: dict) -> str:
    data = _require_object(data, "predict_from_rk result")
    if "error" in data:
        return f"**Prediction error:** {data['error']}\n"
    _require_fields(
        data,
        ("mixing_rule", "rk_order", "components", "y_predicted", "y_excess", "x1"),
        "predict_from_rk result",
    )
    rule = data["mixing_rule"]
    order = data["rk_order"]
    comps = data["components"]
    y_pred = data["y_predicted"]
    y_excess = data["y_excess"]
    if not all(isinstance(value, list) for value in (comps, y_pred, y_excess, data["x1"])):
        raise TypeError("prediction components and numeric series must be arrays")
    n = len(y_pred)

    header = (
        f"**RK Prediction** (order {order}, {rule})\n"
        f"Components: {', '.join(str(c) for c in comps)} | {n} grid points\n"
    )

    # Endpoints + midpoint + extrema
    if n >= 3:
        header += (
            f"Y(x=0) = {y_pred[0]:.6g}, "
            f"Y(x=0.5) ≈ {y_pred[n//2]:.6g}, "
            f"Y(x=1) = {y_pred[-1]:.6g}\n"
        )
        x_grid = data["x1"]
        if len(x_grid) == n:
            i_max = max(range(n), key=lambda i: y_pred[i])
            header += f"Y_max = {y_pred[i_max]:.6g} at x1 = {x_grid[i_max]:.3g}\n"
    if y_excess and len(y_excess) >= 3:
        max_exc = max(y_excess, key=abs)
        space = " (ln-space)" if rule == "arrhenius" else ""
        header += f"Max |excess|{space} = {max_exc:.6g}\n"

    return header


@compacts("propose_fitting_plan")
def compact_propose_fitting_plan(data: dict) -> str:
    """Compactor for propose_fitting_plan."""
    data = _require_object(data, "propose_fitting_plan result")
    if "error" in data:
        return f"**Fitting plan error:** {data['error']}\n"
    _require_fields(
        data, ("status", "warnings", "resolved"), "propose_fitting_plan result"
    )
    status = data["status"]
    lines = [f"**Fitting plan: {status}**"]
    if data["warnings"]:
        if not isinstance(data["warnings"], list):
            raise TypeError("propose_fitting_plan.warnings must be an array")
        for w in data["warnings"]:
            lines.append(f"- warning: {w}")
    if data["resolved"]:
        r = _require_object(data["resolved"], "propose_fitting_plan.resolved")
        _require_fields(
            r,
            ("x_column", "y_column", "constraints", "property_response"),
            "propose_fitting_plan.resolved",
        )
        lines.append(f"  x_col: {r['x_column']} | y_col: {r['y_column']}")
        if r["constraints"]:
            lines.append(f"  constraints: {r['constraints']}")
        lines.append(
            _compact_property_response_contract(
                r["property_response"],
                "propose_fitting_plan.resolved.property_response",
            )
        )
    return "\n".join(lines) + "\n"


@compacts("register_custom_block")
def compact_register_custom_block(data: dict) -> str:
    """Compactor for register_custom_block (agent-built fallback blocks)."""
    data = _require_object(data, "register_custom_block result")
    _require_fields(data, ("status",), "register_custom_block result")
    if "error" in data:
        md = f"**register_custom_block REJECTED:** {data['error']}\n"
        citation_errors = data["citation_errors"] if "citation_errors" in data else []
        if not isinstance(citation_errors, list):
            raise TypeError("register_custom_block.citation_errors must be an array")
        for e in citation_errors:
            md += f"- citation: {e}\n"
        return md

    if data["status"] == "refused_existing_data":
        _require_fields(
            data,
            ("reason", "existing_blocks", "compounds", "property_name"),
            "refused register_custom_block result",
        )
        lines = [
            f"**register_custom_block REFUSED — real data exists.**",
            data["reason"],
            "",
            "| DOI | Block | Points | Properties | T range (K) |",
            "|-----|-------|--------|------------|-------------|",
        ]
        if not isinstance(data["existing_blocks"], list):
            raise TypeError("existing_blocks must be an array")
        for index, b in enumerate(data["existing_blocks"][:8]):
            b = _require_object(b, f"existing_blocks[{index}]")
            _require_fields(
                b,
                ("doi", "block_number", "n_datapoints", "properties", "temperature_range"),
                f"existing_blocks[{index}]",
            )
            lines.append(
                f"| {b['doi']} | {b['block_number']} | {b['n_datapoints']} | "
                f"{b['properties']} | {b['temperature_range']} |"
            )
        lines.append("")
        lines.append("Use these blocks (inspect_block → fit_block) instead of "
                     "agent-built data.")
        return "\n".join(lines) + "\n"

    if data["status"] != "registered":
        raise ValueError(f"undeclared register_custom_block status: {data['status']!r}")
    _require_fields(
        data,
        (
            "pseudo_doi", "block_number", "n_rows", "compounds", "property_name",
            "identified_x", "identified_y", "basis", "citations", "warnings", "note",
        ),
        "registered custom block result",
    )
    lines = [
        f"**⚠ AGENT-BUILT BLOCK REGISTERED (not experimental DB data)**",
        f"pseudo-DOI: `{data['pseudo_doi']}` | "
        f"block: {data['block_number']} | rows: {data['n_rows']}",
        f"Compounds: {', '.join(data['compounds'])} | Property: {data['property_name']}",
        f"x‑columns: {data['identified_x']} | y‑columns: {data['identified_y']}",
        f"Basis: {data['basis']}",
        "Citations: " + "; ".join(
            c["doi"] + (f"#{c['block_number']}" if c["block_number"] else "")
            for c in data["citations"]
        ),
    ]
    for w in data["warnings"]:
        lines.append(f"- warning: {w}")
    if data["note"]:
        lines.append(data["note"])
    return "\n".join(lines) + "\n"


@compacts("align_compositions")
def compact_align_compositions(data: dict) -> str:
    """Compact the L1 composition-alignment result (library + data sheet)."""
    data = _require_object(data, "align_compositions result")
    if "error" in data:
        lines = [f"ERROR: {data['error']}"]
        if "note" in data:
            lines.append(data["note"])
        return "\n".join(lines) + "\n"
    _require_fields(
        data,
        (
            "system", "state", "molar_masses_g_mol", "basis_counts",
            "alignment_status", "n_blocks_surveyed", "bridge_candidates",
            "bridges", "chosen_bridge_reason", "bridge_validation",
            "cross_validation", "unsupported_conversions", "estimates",
        ),
        "align_compositions result",
    )
    sys_ = data["system"]
    state = data["state"]
    if not isinstance(sys_, list) or not isinstance(state, dict):
        raise TypeError("align_compositions system/state have invalid types")
    state_txt = ", ".join(f"{k}={v}" for k, v in state.items()) or "any state"
    mm = _require_object(data["molar_masses_g_mol"], "molar_masses_g_mol")
    mm_txt = "; ".join(f"{k}: {v:g} g/mol" for k, v in mm.items()) or "n/a"
    bases = _require_object(data["basis_counts"], "basis_counts")
    bases_txt = ", ".join(f"{k}×{v}" for k, v in
                          sorted(bases.items(), key=lambda kv: -kv[1]))
    lines = [
        f"## Composition alignment — {' + '.join(sys_)} ({state_txt}) "
        f"[status: {data['alignment_status']}]",
        f"Blocks surveyed: {data['n_blocks_surveyed']} | "
        f"bases: {bases_txt or 'none detected'}",
        f"Molar masses: {mm_txt}",
    ]

    cands = data["bridge_candidates"]
    if not isinstance(cands, list):
        raise TypeError("bridge_candidates must be an array")
    if cands:
        lines.append("")
        lines.append("Bridge candidates (agent-reviewed literature sources):")
        lines.append("| DOI | block | T(K) | R² | n | endpoints | considered |")
        lines.append("|---|---|---|---|---|---|---|")
        for index, c in enumerate(cands[:8]):
            c = _with_target_display(
                _require_object(c, f"bridge_candidates[{index}]"),
                f"bridge_candidates[{index}]",
            )
            _require_fields(
                c,
                ("doi", "block_number", "BLKsubsys_id", "temperature_K", "r_squared", "n_mixture_points", "endpoint_quality", "considered"),
                f"bridge_candidates[{index}]",
            )
            lines.append(
                f"| {_source_display(c)} | {c['block_number']} | {c['temperature_K']} | "
                f"{c['r_squared']} | {c['n_mixture_points']} | "
                f"{c['endpoint_quality']} | {c['considered']} |"
            )

    bridges = _require_object(data["bridges"], "bridges")
    br = bridges["mass_density"] if "mass_density" in bridges else None
    if br:
        br = _require_object(br, "bridges.mass_density")
        _require_fields(
            br,
            ("doi", "block_number", "BLKsubsys_id", "temperature_K", "r_squared", "n_mixture_points", "estimated"),
            "bridges.mass_density",
        )
        if br["block_number"] is not None:
            br = _with_target_display(br, "bridges.mass_density")
        est = " ⚠ ESTIMATED (artifact-backed, not measured)" \
            if br["estimated"] else ""
        bridge_source = (
            _source_display(br) if br["doi"] is not None else "estimate"
        )
        lines.append(
            f"Chosen bridge: {bridge_source} "
            f"{br['block_number'] if br['block_number'] is not None else ''} "
            f"(T={br['temperature_K']}, R²={br['r_squared']}, "
            f"n={br['n_mixture_points']}){est}"
        )
        endpoint_sources = (
            br["pure_endpoint_sources"] if "pure_endpoint_sources" in br else {}
        )
        for comp, src in endpoint_sources.items():
            src = _with_target_display(
                _require_object(src, f"pure_endpoint_sources[{comp}]"),
                f"pure_endpoint_sources[{comp}]",
            )
            if "rejected" in src:
                lines.append(
                    f"  pure ρ({comp}): source {src['doi']} "
                    f"{src['block_number']} NOT USED — {src['rejected']}"
                )
                continue
            lines.append(
                f"  pure ρ({comp}) = {src['value']} kg/m³ pinned from "
                f"{_source_display(src)} {src['block_number']} "
                f"(edge max_x={src['edge_max_x']}, "
                f"n≈pure={src['n_near_pure']})"
            )
            _require_fields(
                src,
                ("property_response",),
                f"pure_endpoint_sources[{comp}]",
            )
            lines.append(
                "    "
                + _compact_prepared_property_response(
                    src["property_response"],
                    f"pure_endpoint_sources[{comp}].property_response",
                )
            )
        val = br.get("validation") or {}
        if val:
            lines.append(
                f"  physical validation: OK — max |ρ−ρ_linear| = "
                f"{val.get('max_excess_of_mean_pct')}% of mean pure density "
                "(positive + bounded on the full grid)"
            )
        if data["chosen_bridge_reason"]:
            lines.append(f"Reason: {data['chosen_bridge_reason']}")
        if not br["estimated"]:
            lines.append(
                "NOTE: the bridge IS a fitted density representation — if "
                "the question asks for density/molar volume, use it "
                "directly (no refit needed)."
            )
    if data.get("bridge_note"):
        lines.append(f"⚠ {data['bridge_note']}")
    rejected = [
        _with_target_display(v, "bridge_validation entry")
        for v in data["bridge_validation"] if not v["ok"]
    ]
    if rejected:
        lines.append(
            "Rejected by physical validation: "
            + "; ".join(f"{_source_display(v)} {v['block_number']}"
                        for v in rejected[:4])
        )

    xv = _require_object(data["cross_validation"], "cross_validation")
    if xv.get("pure_endpoint_agreement"):
        lines.append(f"Endpoint agreement: {xv['pure_endpoint_agreement']}")
    if xv.get("bridge_agreement"):
        lines.append(f"Source agreement: {xv['bridge_agreement']}")
    for chk in (xv.get("dual_basis_checks") or [])[:3]:
        lines.append(f"Dual-basis check: {chk}")

    tt = data.get("translation_table")
    if tt:
        ncols = len(tt.get("columns", []))
        lines.append(
            f"Standard composition data sheet: {tt.get('file') or '(in-memory)'} "
            f"({ncols} basis columns on {tt.get('grid', '?')}; per-column "
            "relation + source metadata in the library JSON)"
        )
    elif data.get("translation_table_note"):
        lines.append(f"⚠ {data['translation_table_note']}")

    for uc in data["unsupported_conversions"][:5]:
        lines.append(f"UNSUPPORTED: {uc}")
    if data["estimates"]:
        lines.append(
            f"⚠ {len(data['estimates'])} artifact-backed estimate(s) "
            "registered by the agent (flagged estimated=true)."
        )
    lines.append(
        "Basis gate: exact bases auto-convert in fit_block; "
        "density-dependent bases convert via the bridge. Alignment never "
        "blocks the pipeline."
    )
    return "\n".join(lines) + "\n"


# ═══════════════════════════════════════════════════════════════
#  COMPACTOR_FUNCTIONS — all tagged compactor callables
# ═══════════════════════════════════════════════════════════════

COMPACTOR_FUNCTIONS = [
    # Phase 0
    compact_resolve_compounds,
    compact_resolve_properties,
    # Phase 1
    compact_query_system_summary,
    compact_query_blocks,
    compact_inspect_block,
    compact_find_similar_compounds,
    compact_get_pure_values,
    # Phase 2
    compact_fit_block,
    compact_fit_multi_system,
    compact_compute_ideal_baseline,
    compact_predict_from_rk,
    compact_propose_fitting_plan,
    # Composition alignment (L1 agent + deterministic assembler)
    compact_align_compositions,
    # Agent-built fallback data
    compact_register_custom_block,
]
