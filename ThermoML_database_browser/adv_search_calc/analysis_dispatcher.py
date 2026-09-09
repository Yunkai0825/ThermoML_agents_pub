"""
Analysis tool dispatcher for the browser.
==========================================
Wraps the existing analysis agent's core calc modules to provide
structured JSON-ready results for the browser UI.

Tools exposed:
  1. nonideality  — Quick non-ideality analysis (uses nonideality.py)
  2. rk_fitting   — Redlich-Kister fitting via agent's numpy-based fitter
  3. inspect       — Block inspection (column ranges, structure)
  4. pure_values   — Pure-component value extraction from edges

Core modules live in:
  NIST_ThermoML_agents/NIST_ThermoML_analysis_agent/ThermoML_core_calc_tools/
"""

from __future__ import annotations

import logging
import traceback
from typing import Any, Dict, Optional

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_block_id, require_block_local_id,
)

log = logging.getLogger("ANALYSIS-DISPATCH")

# ── Lazy import helpers ───────────────────────────────────────────────────
# Agent core modules require numpy and card DB tools.
# Delay imports until first use to avoid startup failures.

_core_loaded = False
_load_error: Optional[str] = None


def _ensure_core():
    """Import heavy dependencies on first use."""
    global _core_loaded, _load_error
    global extract_block_arrays, identify_columns, filter_mixture_points
    global auto_fit_redlich_kister, eval_redlich_kister
    global build_ideal_baseline, compute_excess_property
    global extract_pure_from_edges, pure_values_from_edges, default_mixing_rule
    global classify_excess_core
    global np

    if _core_loaded:
        return
    if _load_error:
        return

    try:
        import numpy as np_ 
        np = np_

        from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.csv_io_helpers import (
            extract_block_arrays as _eba,
            identify_columns as _ic,
            filter_mixture_points as _fmp,
        )
        extract_block_arrays = _eba
        identify_columns = _ic
        filter_mixture_points = _fmp

        from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.Redlich_Kister_block_fitting.rk_fitter import (
            auto_fit_redlich_kister as _afrk,
            eval_redlich_kister as _erk,
        )
        auto_fit_redlich_kister = _afrk
        eval_redlich_kister = _erk

        from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.mixture_nonideality_calc.ideal_baseline import (
            build_ideal_baseline as _bib,
            classify_excess as _ce,
            compute_excess_property as _cep,
            extract_pure_from_edges as _epfe,
            pure_values_from_edges as _pvfe,
            default_mixing_rule as _dmr,
        )
        build_ideal_baseline = _bib
        classify_excess_core = _ce
        compute_excess_property = _cep
        extract_pure_from_edges = _epfe
        pure_values_from_edges = _pvfe
        default_mixing_rule = _dmr

        _core_loaded = True
    except Exception as exc:
        _load_error = f"Failed to load analysis core: {exc}"
        log.error(_load_error)


# ═══════════════════════════════════════════════════════════════
#  Tool metadata (exposed to browser for settings panels)
# ═══════════════════════════════════════════════════════════════

TOOL_DEFINITIONS = [
    {
        "id": "nonideality",
        "name": "Quick Non-Ideality Analysis",
        "icon": "bi-activity",
        "description": (
            "Auto-detects mole fraction and property columns, computes "
            "ideal mixing baselines (linear for volume, Arrhenius for "
            "viscosity), calculates excess properties, fits a "
            "Redlich-Kister polynomial, and classifies the system as "
            "attractive, repulsive, or mixed."
        ),
        "supports_custom": True,
        "settings": [],  # all auto-detected
    },
    {
        "id": "rk_fitting",
        "name": "Redlich-Kister Fitting",
        "icon": "bi-bezier2",
        "description": (
            "Production numpy-based RK fitting with BIC-based automatic "
            "order selection. Uses the analysis agent's full pipeline: "
            "block extraction → column matching → excess property "
            "computation → polynomial fitting."
        ),
        "supports_custom": False,
        "settings": [
            {
                "key": "property_hint",
                "label": "Property Hint",
                "type": "text",
                "placeholder": "e.g. density, viscosity, molar volume",
                "default": "",
                "help": "Substring to help identify the target property column.",
            },
            {
                "key": "composition_hint",
                "label": "Composition Type",
                "type": "select",
                "options": ["mole_fraction", "mass_fraction", "volume_fraction"],
                "default": "mole_fraction",
                "help": "Type of composition variable in the data.",
            },
            {
                "key": "max_rk_order",
                "label": "Max RK Order",
                "type": "number",
                "min": 1,
                "max": 10,
                "default": 5,
                "help": "Maximum polynomial order (BIC selects the best).",
            },
            {
                "key": "mixing_rule",
                "label": "Mixing Rule",
                "type": "select",
                "options": ["auto", "linear", "arrhenius"],
                "default": "auto",
                "help": (
                    "Ideal mixing rule for baseline. "
                    "'auto' selects based on property type."
                ),
            },
            {
                "key": "edge_threshold",
                "label": "Edge Threshold",
                "type": "number",
                "min": 0.001,
                "max": 0.1,
                "step": 0.005,
                "default": 0.02,
                "help": "Threshold for near-pure detection (x > 1-threshold).",
            },
        ],
    },
    {
        "id": "inspect",
        "name": "Block Inspector",
        "icon": "bi-search",
        "description": (
            "Examines the block structure: column names, types, ranges "
            "(min/max/n_valid), identified composition and property columns, "
            "compound mapping, and metadata."
        ),
        "supports_custom": False,
        "settings": [
            {
                "key": "property_filter",
                "label": "Property Filter",
                "type": "text",
                "placeholder": "e.g. density",
                "default": "",
                "help": "Filter columns to show only those matching this substring.",
            },
        ],
    },
    {
        "id": "pure_values",
        "name": "Pure Values Extraction",
        "icon": "bi-bullseye",
        "description": (
            "Extracts pure-component property values from composition "
            "edges using direct averaging, linear extrapolation, or "
            "fallback methods. Reports extraction quality."
        ),
        "supports_custom": False,
        "settings": [
            {
                "key": "property_hint",
                "label": "Property Hint",
                "type": "text",
                "placeholder": "e.g. density, viscosity",
                "default": "",
                "help": "Substring to help identify the target property column.",
            },
            {
                "key": "composition_hint",
                "label": "Composition Type",
                "type": "select",
                "options": ["mole_fraction", "mass_fraction", "volume_fraction"],
                "default": "mole_fraction",
                "help": "Type of composition variable in the data.",
            },
            {
                "key": "edge_threshold",
                "label": "Edge Threshold",
                "type": "number",
                "min": 0.001,
                "max": 0.1,
                "step": 0.005,
                "default": 0.02,
                "help": "Threshold for near-pure detection (x > 1-threshold).",
            },
        ],
    },
]


def get_tool_definitions() -> list[dict]:
    """Return tool definitions for the browser to render settings panels."""
    return TOOL_DEFINITIONS


# ═══════════════════════════════════════════════════════════════
#  Classification (shared with agent enrichment)
# ═══════════════════════════════════════════════════════════════

def classify_excess(y_excess: list[float], x_vals: list[float],
                    property_type: str) -> str:
    """Classify non-ideality from excess property values.

    Delegates to the canonical implementation in the agent's
    ideal_baseline module when available; falls back to a pure-Python
    version otherwise.
    """
    if _core_loaded:
        return classify_excess_core(y_excess, x_vals, property_type)

    # Fallback: pure Python (no numpy required)
    interior = [y for y, x in zip(y_excess, x_vals) if 0.05 < x < 0.95]
    if not interior:
        return "insufficient_data"

    max_abs = max(abs(d) for d in interior)
    if max_abs < 1e-10:
        return "ideal"

    pos = sum(1 for d in interior if d > 0)
    neg = sum(1 for d in interior if d < 0)
    total = len(interior)

    prop_lc = property_type.lower().replace(" ", "_")
    is_transport = prop_lc in ("viscosity", "thermal_conductivity",
                               "diffusion_coefficient")

    if is_transport:
        if pos / total >= 0.8:
            return "attractive"
        elif neg / total >= 0.8:
            return "repulsive"
    else:
        if neg / total >= 0.8:
            return "attractive"
        elif pos / total >= 0.8:
            return "repulsive"

    return "mixed"


# ═══════════════════════════════════════════════════════════════
#  Tool dispatchers
# ═══════════════════════════════════════════════════════════════

def run_nonideality(*, columns: list[dict], rows: list[list],
                    csv_text: str = "") -> dict:
    """Quick non-ideality analysis (pure Python, no numpy required)."""
    from .nonideality import (
        analyze_block, analyze_custom_csv, result_to_dict,
    )
    if csv_text:
        return result_to_dict(analyze_custom_csv(csv_text))
    return result_to_dict(analyze_block(columns, rows))


def _binary_component_names(block_data, column_match) -> list[str]:
    """Return exactly two named components or fail the fitting contract."""
    names: list[str] = []
    for compound in block_data.metadata.get("compounds", []):
        if isinstance(compound, dict) and compound.get("name"):
            name = str(compound["name"])
            if name not in names:
                names.append(name)
    for name in column_match.column_compound_map.values():
        if name and name not in names:
            names.append(name)
    if len(names) != 2:
        raise ValueError(
            "RK fitting requires exactly two named components in block metadata; "
            f"received {names!r}"
        )
    return names


def run_rk_fitting(*, doi: str, block_number: str,
                   BLKsubsys_id: str | None = None,
                   property_hint: str = "",
                   composition_hint: str = "mole_fraction",
                   max_rk_order: int = 5,
                   mixing_rule: str = "auto",
                   edge_threshold: float = 0.02) -> dict:
    """RK fitting using the analysis agent's core calc modules."""
    _ensure_core()
    if _load_error:
        return {"success": False, "error": _load_error}

    try:
        block_number = require_block_id(block_number)
        subsystem_id = (
            require_block_local_id("subsys", BLKsubsys_id)
            if BLKsubsys_id is not None else None
        )
        # 1. Extract exact parent/subsystem arrays
        bd = extract_block_arrays(
            doi, block_number, BLKsubsys_id=subsystem_id
        )
        if not bd.ok:
            return {"success": False, "error": bd.error or "Block extraction failed"}

        # 2. Identify columns
        cm = identify_columns(bd.columns, property_hint, composition_hint)
        if not cm.ok:
            return {"success": False,
                    "error": cm.error or "Column identification failed",
                    "available_columns": bd.columns}

        x_col = cm.x_column
        y_cols = cm.y_columns

        x_arr = bd.arrays.get(x_col)
        if x_arr is None:
            return {"success": False, "error": f"x column '{x_col}' not found in arrays"}

        results = []
        for y_col in y_cols:
            y_arr = bd.arrays.get(y_col)
            if y_arr is None:
                continue

            # Filter out NaN
            valid = ~np.isnan(x_arr) & ~np.isnan(y_arr)
            xv = x_arr[valid]
            yv = y_arr[valid]

            if len(xv) < 3:
                continue

            # 3. Extract pure values from edges
            # For binary: obtain both names from strict block metadata.
            comp_names = _binary_component_names(bd, cm)
            comp1, comp2 = comp_names[0], comp_names[1]
            x_dict_full = {comp1: xv, comp2: 1.0 - xv}

            pv_info = extract_pure_from_edges(x_dict_full, yv, threshold=edge_threshold)
            pv = {c: d["value"] for c, d in pv_info.items()}

            if len(pv) < 2:
                results.append({
                    "property": y_col,
                    "error": "Could not extract pure values for both components",
                    "pure_info": {c: d for c, d in pv_info.items()},
                })
                continue

            # 4. Determine property type and mixing rule
            prop_type = _guess_property_type(y_col)
            rule = mixing_rule if mixing_rule != "auto" else default_mixing_rule(prop_type)

            # 5. Compute excess property
            excess = compute_excess_property(
                xv, yv, pv, prop_type, mixing_rule=rule,
            )
            if "error" in excess:
                results.append({
                    "property": y_col,
                    "error": excess["error"],
                    "pure_values": pv,
                })
                continue

            # 6. Filter mixture points and fit RK
            y_excess_arr = np.array(excess["y_excess"])
            x_mix, y_mix = filter_mixture_points(xv, y_excess_arr, eps=0.02)

            if len(x_mix) < 3:
                results.append({
                    "property": y_col,
                    "error": f"Only {len(x_mix)} mixture points after filtering",
                    "pure_values": pv,
                })
                continue

            fit = auto_fit_redlich_kister(x_mix, y_mix, max_order=max_rk_order)
            if "error" in fit:
                results.append({
                    "property": y_col,
                    "error": fit["error"],
                    "pure_values": pv,
                })
                continue

            # 7. Generate fitted curve on fine grid
            x_grid = np.linspace(0.001, 0.999, 200)
            y_fit_grid = eval_redlich_kister(x_grid, fit["coeffs"])

            # 8. Classify
            y_ex_list = excess["y_excess"]
            x_list = xv.tolist()
            classification = classify_excess(y_ex_list, x_list, prop_type)

            results.append({
                "property": y_col,
                "composition_column": x_col,
                "components": comp_names[:2],
                "pure_values": pv,
                "pure_info": {c: d for c, d in pv_info.items()},
                "mixing_rule": excess["mixing_rule"],
                "excess_label": excess["excess_label"],
                "classification": classification,
                "n_data_points": int(len(xv)),
                "n_mixture_points": int(len(x_mix)),
                "fit": {
                    "coefficients": [round(c, 8) for c in fit["coeffs"]],
                    "order": fit["selected_order"],
                    "r_squared": round(fit.get("r_squared", 0), 6),
                    "rmse": round(fit.get("rmse", 0), 8),
                    "bic": round(fit.get("bic", 0), 3),
                    "all_orders": fit["all_orders"],
                },
                "data": {
                    "x": xv.tolist(),
                    "y_measured": yv.tolist(),
                    "y_ideal": excess["y_ideal"],
                    "y_excess": y_ex_list,
                },
                "fitted_curve": {
                    "x": x_grid.tolist(),
                    "y_excess": y_fit_grid.tolist(),
                },
            })

        if not results:
            return {"success": False,
                    "error": "No properties could be fitted",
                    "columns": bd.columns}

        # System-level classification
        classifications = [r.get("classification", "") for r in results if "error" not in r]
        system_class = _system_classification(classifications, results)

        return {
            "success": True,
            "tool": "rk_fitting",
            "doi": doi,
            "block_number": block_number,
            "BLKsubsys_id": subsystem_id,
            "n_columns": len(bd.columns),
            "n_rows": bd.n_rows,
            "metadata": {
                k: v for k, v in bd.metadata.items()
                if isinstance(v, (str, int, float, bool, list))
            },
            "system_class": system_class,
            "properties": results,
        }
    except Exception as exc:
        log.error("RK fitting failed: %s", traceback.format_exc())
        return {"success": False, "error": str(exc)}


def run_inspect(*, doi: str, block_number: str,
                BLKsubsys_id: str | None = None,
                property_filter: str = "") -> dict:
    """Block inspection using the agent's core calc modules."""
    _ensure_core()
    if _load_error:
        return {"success": False, "error": _load_error}

    try:
        block_number = require_block_id(block_number)
        subsystem_id = (
            require_block_local_id("subsys", BLKsubsys_id)
            if BLKsubsys_id is not None else None
        )
        bd = extract_block_arrays(
            doi, block_number, BLKsubsys_id=subsystem_id
        )
        if not bd.ok:
            return {"success": False, "error": bd.error or "Block extraction failed"}

        # Provenance identifiers locate rows but are not chemical variables.
        analysis_columns = [
            column for column in bd.columns
            if column not in {"BLKpoint_id", "_source"}
        ]
        col_stats = []
        for col_name in analysis_columns:
            arr = bd.arrays.get(col_name)
            if arr is None:
                continue
            valid = arr[~np.isnan(arr)]
            stat = {
                "name": col_name,
                "n_total": int(len(arr)),
                "n_valid": int(len(valid)),
                "n_missing": int(len(arr) - len(valid)),
            }
            if len(valid) > 0:
                stat["min"] = round(float(np.min(valid)), 6)
                stat["max"] = round(float(np.max(valid)), 6)
                stat["mean"] = round(float(np.mean(valid)), 6)
                if len(valid) > 1:
                    stat["std"] = round(float(np.std(valid, ddof=1)), 6)

            # Filter if requested
            if property_filter:
                if property_filter.lower() not in col_name.lower():
                    stat["filtered_out"] = True

            col_stats.append(stat)

        # Try column identification
        cm = identify_columns(
            analysis_columns, property_filter, "mole_fraction", bd.metadata
        )
        col_match = None
        if cm.ok:
            col_match = {
                "x_column": cm.x_column,
                "y_column": cm.y_column,
                "x_columns": cm.x_columns,
                "y_columns": cm.y_columns,
                "other_columns": cm.other_columns,
                "compound_map": cm.column_compound_map,
            }

        return {
            "success": True,
            "tool": "inspect",
            "doi": doi,
            "block_number": block_number,
            "BLKsubsys_id": subsystem_id,
            "n_columns": len(analysis_columns),
            "n_rows": bd.n_rows,
            "columns": col_stats,
            "column_match": col_match,
            "metadata": {
                k: v for k, v in bd.metadata.items()
                if isinstance(v, (str, int, float, bool, list))
            },
        }
    except Exception as exc:
        log.error("Inspect failed: %s", traceback.format_exc())
        return {"success": False, "error": str(exc)}


def run_pure_values(*, doi: str, block_number: str,
                    BLKsubsys_id: str | None = None,
                    property_hint: str = "",
                    composition_hint: str = "mole_fraction",
                    edge_threshold: float = 0.02) -> dict:
    """Pure-component value extraction from edges."""
    _ensure_core()
    if _load_error:
        return {"success": False, "error": _load_error}

    try:
        block_number = require_block_id(block_number)
        subsystem_id = (
            require_block_local_id("subsys", BLKsubsys_id)
            if BLKsubsys_id is not None else None
        )
        bd = extract_block_arrays(
            doi, block_number, BLKsubsys_id=subsystem_id
        )
        if not bd.ok:
            return {"success": False, "error": bd.error or "Block extraction failed"}

        cm = identify_columns(bd.columns, property_hint, composition_hint)
        if not cm.ok:
            return {"success": False,
                    "error": cm.error or "Column identification failed",
                    "available_columns": bd.columns}

        x_col = cm.x_column
        y_cols = cm.y_columns
        x_arr = bd.arrays.get(x_col)
        if x_arr is None:
            return {"success": False, "error": f"x column '{x_col}' not found"}

        comp_names = _binary_component_names(bd, cm)
        comp1, comp2 = comp_names[0], comp_names[1]

        extractions = []
        for y_col in y_cols:
            y_arr = bd.arrays.get(y_col)
            if y_arr is None:
                continue

            valid = ~np.isnan(x_arr) & ~np.isnan(y_arr)
            xv = x_arr[valid]
            yv = y_arr[valid]

            if len(xv) < 3:
                continue

            x_dict_full = {comp1: xv, comp2: 1.0 - xv}
            pv_info = extract_pure_from_edges(
                x_dict_full, yv, threshold=edge_threshold,
            )

            extractions.append({
                "property": y_col,
                "n_data_points": int(len(xv)),
                "x_range": [round(float(np.min(xv)), 4),
                            round(float(np.max(xv)), 4)],
                "pure_values": {
                    comp: {
                        "value": info["value"],
                        "max_x": info["max_x"],
                        "n_near_pure": info["n_near_pure"],
                        "method": info["method"],
                        "quality": info["quality"],
                    }
                    for comp, info in pv_info.items()
                },
            })

        if not extractions:
            return {"success": False,
                    "error": "No properties could be processed",
                    "columns": bd.columns}

        return {
            "success": True,
            "tool": "pure_values",
            "doi": doi,
            "block_number": block_number,
            "BLKsubsys_id": subsystem_id,
            "composition_column": x_col,
            "components": comp_names[:2],
            "edge_threshold": edge_threshold,
            "extractions": extractions,
        }
    except Exception as exc:
        log.error("Pure values extraction failed: %s", traceback.format_exc())
        return {"success": False, "error": str(exc)}


# ═══════════════════════════════════════════════════════════════
#  Dispatcher
# ═══════════════════════════════════════════════════════════════

_TOOL_MAP = {
    "nonideality": run_nonideality,
    "rk_fitting": run_rk_fitting,
    "inspect": run_inspect,
    "pure_values": run_pure_values,
}


def dispatch(tool: str, **kwargs) -> dict:
    """Run the requested analysis tool with the given parameters."""
    fn = _TOOL_MAP.get(tool)
    if fn is None:
        return {"success": False,
                "error": f"Unknown tool: {tool}. Available: {list(_TOOL_MAP.keys())}"}
    return fn(**kwargs)


# ═══════════════════════════════════════════════════════════════
#  Helpers
# ═══════════════════════════════════════════════════════════════

def _guess_property_type(col_name: str) -> str:
    """Guess a canonical property type from a column header."""
    cl = col_name.lower()
    if "viscos" in cl or "eta" in cl:
        return "viscosity"
    if "density" in cl or "rho" in cl:
        return "density"
    if "molar vol" in cl or "v_m" in cl:
        return "molar_volume"
    if "refract" in cl:
        return "refractive_index"
    if "speed" in cl and "sound" in cl:
        return "speed_of_sound"
    if "heat cap" in cl or "c_p" in cl:
        return "heat_capacity"
    if "surface" in cl and "tension" in cl:
        return "surface_tension"
    if "thermal cond" in cl:
        return "thermal_conductivity"
    if "diffus" in cl:
        return "diffusion_coefficient"
    return "molar_volume"  # default to linear mixing


def _system_classification(classifications: list[str],
                           results: list[dict]) -> str:
    """Build a system-level classification summary."""
    if not classifications:
        return ""
    if len(classifications) == 1:
        return classifications[0].title()
    if all(c == "attractive" for c in classifications):
        return "All properties attractive"
    if all(c == "repulsive" for c in classifications):
        return "All properties repulsive"
    # Mixed: describe per-property
    parts = []
    for r in results:
        if "error" in r and "classification" not in r:
            continue
        prop = r.get("property", "?")
        cls = r.get("classification", "?")
        parts.append(f"{prop}: {cls}")
    if parts:
        return "; ".join(parts)
    return "Mixed"
