"""Phase 2 — RK fitting, multi-system, per-temperature, and prediction tools.

Each function returns a raw dict.  The catalog's ``wrap_tool`` handles
compaction (Layer 1) and agentic KEEP/DISCARD (Layer 2).
"""

from __future__ import annotations

import contextlib
import logging
import os
from pathlib import Path

import numpy as np

from ThermoML_raw_json_to_card_db_parsers.id_schema import require_block_id, require_block_local_id

from ...general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import (
    ToolEntry,
    uses_compactors,
)
from ..analysis_agent_context_hooks.compactor_hooks._tool_compactors import (
    compact_fit_block,
    compact_fit_multi_system,
    compact_compute_ideal_baseline,
    compact_predict_from_rk,
    compact_propose_fitting_plan,
)
from ..analysis_agent_context_hooks.hook_catalog import get_session
from ...general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers.session_manager_output_storage import (
    _filesystem_path,
)
from ..ThermoML_core_calc_tools.output_helpers.csv_export import (
    save_fit_csv, save_excess_csv,
)
from ..ThermoML_core_calc_tools.output_helpers.plot_export import (
    save_fit_plot, save_excess_plot, build_rk_annotation,
)

from concurrent.futures import ThreadPoolExecutor, as_completed
from contextvars import copy_context
from ..ThermoML_core_calc_tools.csv_io_helpers import (
    extract_block_arrays,
    identify_columns,
    filter_mixture_points,
)
from ..ThermoML_core_calc_tools.mixture_nonideality_calc.ideal_baseline import (
    build_ideal_baseline,
    classify_excess,
    compute_excess_property,
    default_mixing_rule,
    extract_pure_from_edges,
)
from ..ThermoML_core_calc_tools.mixture_nonideality_calc.composition_transforms import (
    convert_axis_to_mole_fraction,
    detect_composition_basis,
)
from ..ThermoML_core_calc_tools.Redlich_Kister_block_fitting.rk_fitter import (
    auto_fit_redlich_kister,
    eval_redlich_kister,
    fit_multi_property,
)
from ..ThermoML_core_calc_tools.property_response_preparation import (
    PropertyResponsePreparationError,
    inspect_property_response_contract,
    prepare_property_response,
    property_response_error_result,
)

_log = logging.getLogger("FITTING-TOOLS")


# ------------------------------------------------------------------
#  Output generation helper
# ------------------------------------------------------------------

def _safe_doi_slug(doi: str) -> str:
    """Turn a DOI into a filename-safe slug."""
    return doi.replace("/", "_").replace(".", "_")[:40]


def _dense_rk_total_curve(
    x_mix: np.ndarray,
    rk: dict,
    pure_values: dict[str, float] | None,
    property_type: str,
    mixing_rule: str,
    components: list[str] | None,
    *,
    n_grid: int = 300,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray] | None:
    """Evaluate the total RK model on a dense composition grid for plotting."""
    coeffs = rk.get("coeffs")
    if coeffs is None or not pure_values or not property_type:
        return None
    coeffs = np.asarray(coeffs, dtype=float)
    if coeffs.size == 0 or not np.all(np.isfinite(coeffs)):
        return None
    rule = (mixing_rule or "linear").lower()

    x = np.asarray(x_mix, dtype=float)
    valid = np.isfinite(x)
    if np.count_nonzero(valid) < 2:
        return None

    x_min = float(np.min(x[valid]))
    x_max = float(np.max(x[valid]))
    if not np.isfinite(x_min) or not np.isfinite(x_max) or x_max <= x_min:
        return None

    # Full composition range: the ideal baseline is anchored at the pure
    # values (x=0, x=1), so draw it end-to-end.  The caller clips the RK
    # fit curve back to the data range to avoid implying extrapolation.
    x_grid = np.linspace(0.0, 1.0, n_grid)
    baseline = build_ideal_baseline(
        pure_values, x_grid, property_type,
        mixing_rule=rule, component_order=components,
    )
    if "error" in baseline or "y_ideal" not in baseline:
        return None

    y_ideal_grid = np.asarray(baseline["y_ideal"], dtype=float)
    y_excess_grid = eval_redlich_kister(x_grid, coeffs)
    if rule == "arrhenius":
        if np.any(y_ideal_grid <= 0):
            return None
        y_fit_grid = np.exp(np.log(y_ideal_grid) + y_excess_grid)
    else:
        y_fit_grid = y_ideal_grid + y_excess_grid

    return x_grid, y_ideal_grid, y_fit_grid, y_excess_grid


def _save_fit_outputs(
    doi: str,
    block_number: str,
    x_mix: np.ndarray,
    y_mix: np.ndarray,
    y_ideal: np.ndarray,
    y_excess: np.ndarray,
    rk: dict,
    *,
    BLKsubsys_id: str | None = None,
    mixing_rule: str = "linear",
    components: list[str] | None = None,
    y_label: str = "Y",
    temperature_K: float | None = None,
    pure_values: dict[str, float] | None = None,
    property_type: str = "",
    pure_values_source: str = "",
    block_metadata: dict | None = None,
) -> dict[str, str]:
    """Save CSV + plot for a single RK fit.  Returns {type: path} dict.

    No-op if no session is active.  Never raises — logs errors instead.
    """
    sess = get_session()
    if not sess:
        return {}

    slug = _safe_doi_slug(doi)
    blk = require_block_id(block_number)
    subsystem_id = (
        require_block_local_id("subsys", BLKsubsys_id)
        if BLKsubsys_id is not None else None
    )
    subsystem_tag = f"_{subsystem_id}" if subsystem_id is not None else ""
    target_label = f"{block_number}/{subsystem_id}" if subsystem_id else block_number
    temp_tag = f"_T{temperature_K:.1f}" if temperature_K is not None else ""
    base = f"{slug}_B{blk}{subsystem_tag}{temp_tag}"

    coeffs = rk.get("coeffs", [])
    y_fitted_excess = eval_redlich_kister(x_mix, coeffs)
    if mixing_rule == "arrhenius":
        y_fitted_total = np.exp(np.log(y_ideal) + y_fitted_excess)
    else:
        y_fitted_total = y_ideal + y_fitted_excess
    residuals = y_excess - y_fitted_excess
    outputs: dict[str, str] = {}

    # For Arrhenius, excess values are in ln-space → use accurate column labels
    fit_y_label = f"ln_excess_{y_label}" if mixing_rule == "arrhenius" else y_label

    try:
        csv_path = save_fit_csv(
            str(sess.data_path(f"{base}_fit.csv")),
            x_mix, y_excess, y_fitted_excess, residuals,
            coeffs, rk.get("selected_order", len(coeffs) - 1),
            rk.get("r_squared", 0.0), rk.get("rmse", 0.0),
            y_label=fit_y_label,
            metadata={
                "doi": doi,
                "block_number": block_number,
                "BLKsubsys_id": subsystem_id,
                "mixing_rule": mixing_rule,
            },
        )
        outputs["fit_csv"] = csv_path
        sess.register_file("data", csv_path,
                           f"RK fit data — {doi} {target_label}{temp_tag}")
    except Exception as exc:
        _log.warning("CSV export failed: %s", exc, exc_info=True)

    try:
        excess_csv = save_excess_csv(
            str(sess.data_path(f"{base}_excess.csv")),
            x_mix, y_mix, y_ideal, y_excess,
            y_label=y_label, mixing_rule=mixing_rule,
        )
        outputs["excess_csv"] = excess_csv
        sess.register_file("data", excess_csv,
                           f"Excess property — {doi} {target_label}{temp_tag}")
    except Exception as exc:
        _log.warning("Excess CSV export failed: %s", exc, exc_info=True)

    try:
        dense_curve = _dense_rk_total_curve(
            x_mix, rk, pure_values, property_type, mixing_rule, components,
        )
        dense_kwargs = {}
        dense_excess_kwargs = {}
        if dense_curve is not None:
            x_grid, y_ideal_grid, y_fit_grid, y_excess_grid = dense_curve
            x_finite = np.asarray(x_mix, dtype=float)
            x_finite = x_finite[np.isfinite(x_finite)]
            x_lo = float(np.min(x_finite)) if x_finite.size else 0.0
            x_hi = float(np.max(x_finite)) if x_finite.size else 1.0
            in_rng = (x_grid >= x_lo - 1e-12) & (x_grid <= x_hi + 1e-12)
            dense_kwargs = {
                "ideal_curve_x": x_grid,
                "ideal_curve_y": y_ideal_grid,
                "fit_curve_x": x_grid[in_rng],
                "fit_curve_y": y_fit_grid[in_rng],
            }
            dense_excess_kwargs = {
                "fit_curve_x": x_grid[in_rng],
                "fit_curve_y": y_excess_grid[in_rng],
            }

        # Pure-component reference anchors: components[0] is the x-column
        # compound (pure at x=1), components[1] is pure at x=0.
        pure_points: list[tuple[float, float]] | None = None
        if pure_values and components and len(components) >= 2:
            pts: list[tuple[float, float]] = []
            p_x0 = pure_values.get(components[1])
            p_x1 = pure_values.get(components[0])
            if p_x0 is not None and np.isfinite(p_x0):
                pts.append((0.0, float(p_x0)))
            if p_x1 is not None and np.isfinite(p_x1):
                pts.append((1.0, float(p_x1)))
            pure_points = pts or None

        src = (pure_values_source or "").lower()
        if src.startswith("named"):
            pp_label = "named"
        elif src.startswith("block-edges"):
            pp_label = "block edges"
        else:
            pp_label = ""

        fit_plot_args = (x_mix, y_mix, y_ideal, y_fitted_total)
        fit_plot_kwargs = dict(
            y_label=y_label, mixing_rule=mixing_rule,
            rk_order=rk.get("selected_order"),
            r_squared=rk.get("r_squared"),
            components=components,
            title=f"RK Fit — {doi} {target_label}{temp_tag}",
            pure_points=pure_points,
            pure_points_label=pp_label,
            **dense_kwargs,
        )
        plot_p = save_fit_plot(
            str(sess.plot_path(f"{base}_fit.png")),
            *fit_plot_args, **fit_plot_kwargs,
        )
        outputs["fit_plot"] = plot_p
        sess.register_file("plot", plot_p,
                           f"RK fit plot — {doi} {target_label}{temp_tag}")
    except Exception as exc:
        _log.warning("Fit plot export failed: %s", exc, exc_info=True)

    try:
        excess_plot_args = (x_mix, y_excess, y_fitted_excess)
        excess_plot_kwargs = dict(
            y_label=f"{y_label}_excess",
            rk_order=rk.get("selected_order"),
            r_squared=rk.get("r_squared"),
            components=components,
            title=f"Excess — {doi} {target_label}{temp_tag}",
            **dense_excess_kwargs,
        )
        excess_p = save_excess_plot(
            str(sess.plot_path(f"{base}_excess.png")),
            *excess_plot_args, **excess_plot_kwargs,
        )
        outputs["excess_plot"] = excess_p
        sess.register_file("plot", excess_p,
                           f"Excess plot — {doi} {target_label}{temp_tag}")
    except Exception as exc:
        _log.warning("Excess plot export failed: %s", exc, exc_info=True)

    # ── Legend enrichment: RK equation + raw-block metadata ─────────
    # The basic plots above are already on disk; the annotated version is
    # rendered to a temp file and swapped in atomically, so any failure
    # here only logs a warning and keeps the plain plots.
    if "fit_plot" in outputs or "excess_plot" in outputs:
        try:
            meta = block_metadata
            if meta is None:
                probe = extract_block_arrays(
                    doi, block_number, BLKsubsys_id=BLKsubsys_id,
                )
                meta = probe.metadata if probe.ok else None
            if meta is None:
                _log.warning(
                    "Plot legend enrichment: no block metadata for %s %s — "
                    "equation-only legend", doi, block_number,
                )
            annotation = build_rk_annotation(
                rk, mixing_rule=mixing_rule, components=components,
                block_metadata=meta, temperature_K=temperature_K,
                n_points=int(np.asarray(x_mix, dtype=float).size),
                y_column=y_label,
            )

            def _swap(save_fn, final: str, args: tuple, kwargs: dict) -> None:
                tmp = final + ".enrich.tmp.png"
                fs_tmp = _filesystem_path(Path(tmp))
                try:
                    save_fn(tmp, *args, annotation=annotation, **kwargs)
                    os.replace(fs_tmp, _filesystem_path(Path(final)))
                finally:
                    with contextlib.suppress(OSError):
                        os.remove(fs_tmp)

            if "fit_plot" in outputs:
                _swap(save_fit_plot, outputs["fit_plot"],
                      fit_plot_args, fit_plot_kwargs)
            if "excess_plot" in outputs:
                _swap(save_excess_plot, outputs["excess_plot"],
                      excess_plot_args, excess_plot_kwargs)
        except Exception as exc:
            _log.warning(
                "Plot legend enrichment failed — basic plot kept: %s",
                exc, exc_info=True,
            )

    return outputs


# ------------------------------------------------------------------
#  Helpers shared within this module
# ------------------------------------------------------------------

def _resolve_comp_names(component_names: list[str] | None, metadata: dict) -> list[str]:
    """Return exactly two component names from input or block metadata."""
    if component_names is not None:
        if not isinstance(component_names, list) or len(component_names) != 2:
            raise TypeError("component_names must be an array of exactly two strings")
        if any(not isinstance(name, str) or not name.strip() for name in component_names):
            raise TypeError("both component_names entries must be non-empty strings")
        names = component_names
    else:
        comps = metadata.get("compounds")
        if not isinstance(comps, list):
            raise TypeError("block metadata compounds must be an array")
        names = []
        for index, compound in enumerate(comps):
            if not isinstance(compound, dict) or not isinstance(compound.get("name"), str):
                raise ValueError(f"block metadata compounds[{index}] is missing name")
            names.append(compound["name"])
    if len(names) != 2:
        raise ValueError(
            "Binary fitting requires exactly two named compounds in "
            "component_names or the selected block metadata"
        )
    return names


def _normalized_binary_composition(
    metadata: dict,
    comp_names: list[str],
    x_values: np.ndarray,
) -> dict[str, np.ndarray]:
    """Map the fitted binary mole-fraction axis to strict global IDs."""
    compounds = metadata.get("compounds")
    if not isinstance(compounds, list):
        raise PropertyResponsePreparationError(
            "BLOCK_COMPONENT_METADATA_MISSING",
            "Block metadata does not contain compound declarations.",
        )
    by_name: dict[str, str] = {}
    for compound in compounds:
        if not isinstance(compound, dict):
            continue
        name = compound.get("name")
        comp_num_id = compound.get("comp_num_id")
        if isinstance(name, str) and isinstance(comp_num_id, str):
            by_name[name.strip().casefold()] = comp_num_id
    try:
        comp_x1 = by_name[comp_names[0].strip().casefold()]
        comp_x0 = by_name[comp_names[1].strip().casefold()]
    except (IndexError, KeyError) as exc:
        raise PropertyResponsePreparationError(
            "COMPOSITION_COMPONENT_ALIGNMENT_FAILED",
            "The fitted composition axis could not be aligned to global compound IDs.",
            details={"components": comp_names, "metadata_names": sorted(by_name)},
        ) from exc
    x = np.asarray(x_values, dtype=float)
    return {comp_x1: x, comp_x0: 1.0 - x}


def _canonical_state_and_tolerances(
    constraints: dict | None,
    *,
    fallback_temperature: float | None = None,
) -> tuple[dict[str, float | None], dict[str, float]]:
    """Translate block-local state-column constraints to canonical state keys."""
    state: dict[str, float | None] = {
        "temperature_k": fallback_temperature,
        "pressure_kpa": None,
    }
    tolerances = {"temperature_k": 0.5, "pressure_kpa": 1.0}
    for column, spec in (constraints or {}).items():
        key = column.casefold()
        canonical = (
            "temperature_k" if "temperature" in key
            else "pressure_kpa" if "pressure" in key
            else None
        )
        if canonical is None:
            continue
        state[canonical] = float(spec["value"])
        tolerances[canonical] = float(spec.get("tol", tolerances[canonical]))
    return state, tolerances


def _selected_unique_state_value(
    bd,
    quantity: str,
    row_mask: np.ndarray | None,
) -> tuple[float | None, list[float]]:
    """Return one selected-row state value, or all distinct values."""
    token = "temperature" if quantity == "temperature_k" else "pressure"
    values: list[np.ndarray] = []
    for column in bd.columns:
        if token not in column.casefold() or column not in bd.arrays:
            continue
        array = np.asarray(bd.arrays[column], dtype=float)
        if row_mask is not None:
            array = array[row_mask]
        finite = array[np.isfinite(array)]
        if finite.size:
            values.append(finite)
    if not values:
        return None, []
    unique = np.unique(np.round(np.concatenate(values), decimals=10))
    listed = [float(value) for value in unique]
    return (listed[0] if len(listed) == 1 else None), listed


def _order_comps_by_x_column(comp_names: list[str], match) -> list[str]:
    """Reorder comp_names so the compound of the x column comes FIRST.

    This ensures comps[0] = x-column compound throughout the pipeline
    (build_ideal_baseline assigns x_arr to comps[0] in binary systems).
    """
    x_compound = match.column_compound_map.get(match.x_column, "")
    if x_compound and x_compound in comp_names and comp_names[0] != x_compound:
        return [x_compound] + [c for c in comp_names if c != x_compound]
    return comp_names


def _named_pure_lookup(named: dict, comp: str) -> float | None:
    """Look up one exact component key in a name-keyed pure-values object."""
    if comp not in named:
        return None
    value = named[comp]
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"pure_values[{comp!r}] must be numeric")
    return float(value)


# Standard atomic weights for deterministic molar-mass computation from the
# block's own compound formulas (used as exact bridging data for dimensional
# conversions like molar volume <-> mass density, molarity -> mass density).
_ATOMIC_WEIGHTS: dict[str, float] = {
    "H": 1.008, "D": 2.014, "B": 10.81, "C": 12.011, "N": 14.007,
    "O": 15.999, "F": 18.998, "Na": 22.990, "Mg": 24.305, "Al": 26.982,
    "Si": 28.085, "P": 30.974, "S": 32.06, "Cl": 35.45, "K": 39.098,
    "Ca": 40.078, "Fe": 55.845, "Cu": 63.546, "Zn": 65.38, "Br": 79.904,
    "I": 126.904, "Li": 6.94,
}


def _formula_weight(formula: str) -> float | None:
    """Molar mass (g/mol) from a Hill formula like ``C3H6O`` or ``(CH3)2CO``.

    Returns ``None`` for unknown elements or unparseable input.
    """
    import re as _re
    if not formula or not isinstance(formula, str):
        return None

    def _parse(s: str, i: int = 0) -> tuple[float, int]:
        total = 0.0
        while i < len(s):
            ch = s[i]
            if ch == "(":
                sub, i = _parse(s, i + 1)
                m = _re.match(r"\d+", s[i:])
                mult = int(m.group()) if m else 1
                i += m.end() if m else 0
                total += sub * mult
            elif ch == ")":
                return total, i + 1
            else:
                m = _re.match(r"([A-Z][a-z]?)(\d*)", s[i:])
                if not m or not m.group(1):
                    raise ValueError(f"bad formula at {s[i:]}")
                el, cnt = m.group(1), int(m.group(2) or 1)
                if el not in _ATOMIC_WEIGHTS:
                    raise ValueError(f"unknown element {el}")
                total += _ATOMIC_WEIGHTS[el] * cnt
                i += m.end()
        return total, i

    try:
        w, _ = _parse(formula.strip())
        return round(w, 3) if w > 0 else None
    except Exception:
        return None


def _molar_masses_from_metadata(
    metadata: dict | None, comp_names: list[str],
) -> dict[str, float]:
    """Map component names to molar masses via the block's own formulas."""
    out: dict[str, float] = {}
    if not metadata:
        return out
    comps = metadata.get("compounds", []) or []
    wanted = {str(c).strip().casefold() for c in comp_names}
    for c in comps:
        if not isinstance(c, dict):
            continue
        nm = c.get("name")
        if not isinstance(nm, str) or not nm:
            continue
        if nm.casefold() in wanted:
            mw = _formula_weight(c.get("formula") or "")
            if mw:
                out[nm] = mw
    return out


def _apply_composition_basis_gate(
    bd,
    x_col: str,
    x_vals: np.ndarray,
    comp_names: list[str],
    state_mask: np.ndarray | None,
    selected_temp: float | None = None,
    sweep_mode: bool = False,
) -> dict:
    """Detect the composition basis of *x_col* and convert to mole fraction.

    Canonical fitting basis is MOLE FRACTION (molar excess functions are
    defined on it; the RK family is not closed under basis change), so
    non-mole axes are never fitted silently:

    - mole_fraction → pass through unchanged.
    - mass_fraction / molality / mass_ratio / amount_ratio → EXACT
      pointwise conversion using molar masses from the block's own
      formulas (zero-information, temperature-independent transforms).
    - molarity / mass_concentration → exact only with a per-row measured
      density: same-block density column first, then the composition
      library's ρ(x) bridge (temperature-matched within 2 K), otherwise
      a LOUD error.  Density-dependent conversions are T-dependent, so
      they are REFUSED in temperature-sweep mode (fit per temperature).
    - volume_fraction / solvent-scoped → bridge or loud error.

    Bridge anchor provenance (the bridge's own pure-value backing — the
    same edge-extraction/quality machinery as any fit) is surfaced in
    the conversion note.

    Returns ``{"x", "basis", "note"|None}`` or ``{"error", ...}``.
    """
    basis = detect_composition_basis(x_col)
    if basis in ("mole_fraction", "unknown"):
        return {"x": x_vals, "basis": basis, "note": None}

    if sweep_mode and basis in ("molarity", "volume_fraction",
                                "mass_concentration"):
        return {
            "error": (
                f"Composition axis '{x_col}' is in {basis.upper()} basis, "
                f"whose conversion to mole fraction is TEMPERATURE-DEPENDENT "
                f"(needs ρ at each state). Temperature-sweep fitting would "
                f"reuse one density across all temperatures — fit each "
                f"temperature separately with x_vars_constrained instead."
            ),
            "composition_basis": basis,
        }

    mm = _molar_masses_from_metadata(bd.metadata, comp_names)
    M1 = mm.get(comp_names[0]) if comp_names else None
    M2 = mm.get(comp_names[1]) if len(comp_names) > 1 else None

    rho = None
    if basis in ("molarity", "mass_concentration"):
        dens_col = next(
            (c for c in bd.columns
             if "mass_density" in c.lower() or c.lower().startswith("density")),
            None,
        )
        if dens_col and dens_col in bd.arrays:
            rho_full = bd.arrays[dens_col]
            rho_reported = (
                rho_full[state_mask] if state_mask is not None else rho_full
            )
            try:
                density_response = prepare_property_response(
                    metadata=bd.metadata,
                    y_column=dens_col,
                    reported_values=rho_reported,
                    # At this point the non-mole composition axis has not yet
                    # been converted. A same-proportion density reference is
                    # therefore a genuine dependency cycle and fails closed;
                    # scalar solvent/solute references remain resolvable.
                    normalized_composition=None,
                    state={
                        "temperature_k": selected_temp,
                        "pressure_kpa": None,
                    },
                )
            except PropertyResponsePreparationError as exc:
                return {
                    "error": (
                        "The density required to normalize the composition "
                        f"axis is not an absolute response: {exc.code}: {exc}"
                    ),
                    "error_code": exc.code,
                    "composition_basis": basis,
                }
            rho = density_response.values

    # ---- Composition-library bridge (density-dependent bases without a
    # same-block density column) ----
    if rho is None and basis in ("molarity", "volume_fraction",
                                 "mass_concentration") \
            and M1 is not None and M2 is not None:
        from ..ThermoML_core_calc_tools.mixture_nonideality_calc.composition_transforms import (
            get_active_library, eval_bridge_y, mass_to_mole,
            volume_fraction_to_mole,
        )
        lib = get_active_library()
        bridge = (lib or {}).get("bridges", {}).get("mass_density")
        same_system = bridge is not None and (
            {str(c).casefold() for c in (lib or {}).get("system", [])}
            == {c.casefold() for c in comp_names}
        )
        # Temperature consistency: density bridges are state-bound.
        t_ok = True
        br_T = bridge.get("temperature_K") if bridge else None
        if bridge and br_T is not None and selected_temp is not None \
                and abs(float(br_T) - float(selected_temp)) > 2.0:
            t_ok = False
            _log.info(
                "Basis gate: library bridge at T=%.2f K does not match fit "
                "T=%.2f K — bridge skipped", float(br_T), float(selected_temp),
            )
        if bridge and same_system and t_ok:
            # Orientation: the bridge curve is parameterized on its own
            # x_compound; flip when that is the block's OTHER component.
            flip = (str(bridge.get("x_compound", "")).casefold()
                    != comp_names[0].casefold())

            def _rho_of_x1(x1: np.ndarray) -> np.ndarray:
                xb = 1.0 - x1 if flip else x1
                return eval_bridge_y(bridge, np.clip(xb, 0.0, 1.0))

            try:
                v = np.asarray(x_vals, dtype=float)
                if basis == "molarity":
                    x_conv = np.full_like(v, 0.5)
                    for _ in range(30):
                        x_new = v * M2 / (_rho_of_x1(x_conv) - v * (M1 - M2))
                        if np.all(np.abs(x_new - x_conv) < 1e-12):
                            x_conv = x_new
                            break
                        x_conv = x_new
                elif basis == "volume_fraction":
                    rho1 = float(_rho_of_x1(np.array([1.0]))[0])
                    rho0 = float(_rho_of_x1(np.array([0.0]))[0])
                    x_conv = volume_fraction_to_mole(
                        v, (M1 * 1e-3) / rho1, (M2 * 1e-3) / rho0)
                else:  # mass_concentration: w1 = c_mass/rho(x), fixed point
                    x_conv = np.full_like(v, 0.5)
                    for _ in range(30):
                        x_new = mass_to_mole(v / _rho_of_x1(x_conv), M1, M2)
                        if np.all(np.abs(x_new - x_conv) < 1e-12):
                            x_conv = x_new
                            break
                        x_conv = x_new
                anchor_source = (
                    bridge["pure_values_source"]
                    if "pure_values_source" in bridge
                    else "explicit estimated pure-density anchors"
                )
                note = (
                    f"Composition axis converted to mole fraction of "
                    f"{comp_names[0]}: {basis} → mole_fraction via the "
                    f"composition-library density bridge "
                    f"({bridge['doi']} {bridge['block_number']}, "
                    f"T={bridge['temperature_K']}, "
                    f"R²={bridge['r_squared']}) "
                    f"[{bridge['route']}; bridge anchors: {anchor_source}]. "
                    f"Source column: {x_col}."
                )
                _log.info("Basis gate: %s axis '%s' converted via library "
                          "bridge %s", basis, x_col, bridge["doi"])
                return {"x": np.asarray(x_conv, dtype=float), "basis": basis,
                        "note": note}
            except Exception as exc:  # noqa: BLE001 — fall through to error
                _log.warning("Library-bridge conversion failed: %s", exc)

    conv = convert_axis_to_mole_fraction(
        basis, x_vals, M1=M1, M2=M2, rho=rho,
    )
    if "error" in conv:
        return {
            "error": (
                f"Composition axis '{x_col}' is in {basis.upper()} basis "
                f"and cannot be fitted as-is (fits are defined in mole "
                f"fraction). {conv['error']}"
            ),
            "composition_basis": basis,
        }
    note = (
        f"Composition axis converted to mole fraction of {comp_names[0]}: "
        f"{basis} → mole_fraction via {conv['relation']} [{conv['rung']}]. "
        f"Source column: {x_col}."
    )
    _log.info("Basis gate: %s axis '%s' converted to mole fraction [%s]",
              basis, x_col, conv["rung"])
    return {"x": np.asarray(conv["x"], dtype=float), "basis": basis,
            "note": note}


def _resolve_pure_values(
    *,
    comp_names: list[str],
    x_col: str,
    x_all: np.ndarray,
    y_all: np.ndarray,
    named_values: dict | None = None,
    edge_threshold: float = 0.02,
    y_col: str = "",
    state: dict | None = None,
    metadata: dict | None = None,
):
    """Resolve the pure-component anchors for a fit deterministically.

    The block parser already identifies which compound the composition
    axis refers to (``comp_names[0]`` = x-column compound, pure at x=1;
    ``comp_names[1]`` = the other compound, pure at x=0), so the mapping
    is never guessed:

    1. ``named_values`` {component_name: value} — mapped via the parsed
       axis identity.  Unresolvable names are an ERROR listing the
       block's component names.
    2. When omitted, values are extracted from the block's endpoint rows
       (``extract_pure_from_edges`` on the same filtered arrays used
       for fitting, so multi-temperature blocks resolve per state).

    Returns ``(pv_x0, pv_x1, source, note)`` or an error dict.
    """
    comp_x1, comp_x0 = comp_names[0], comp_names[1]

    # ---- Data-implied endpoints from the state-filtered arrays ----
    valid = ~np.isnan(x_all) & ~np.isnan(y_all)
    edge0 = y_all[valid & (x_all <= edge_threshold)]
    edge1 = y_all[valid & (x_all >= 1.0 - edge_threshold)]
    y_valid = y_all[valid]

    def _scale_check(pv: float, comp: str, x_end: str, edge: np.ndarray) -> str | None:
        """Reject anchors that are wildly out of scale with the block's y data.

        Catches unit slips (g/cm³ vs kg/m³, mPa·s vs Pa·s) and wrong-property
        anchors (e.g. molar volume passed for a mass-density fit).  Zero
        anchors (excess convention) and sign-mixed data are exempt.
        """
        if abs(pv) < 1e-300 or y_valid.size == 0:
            return None
        if np.any(y_valid > 0) and np.any(y_valid < 0):
            return None  # excess-like data crossing zero: no magnitude scale
        ay = np.abs(y_valid[y_valid != 0])
        if ay.size == 0:
            return None
        if len(edge) > 0:
            ref = float(np.mean(np.abs(edge)))
            if ref <= 0 or (ref / 20.0 <= abs(pv) <= ref * 20.0):
                return None
            ref_txt = f"the block's own y({x_end}) ≈ {float(np.mean(edge)):.6g}"
        else:
            lo, hi = float(np.min(ay)), float(np.max(ay))
            if lo / 50.0 <= abs(pv) <= hi * 50.0:
                return None
            ref_txt = f"the block's y-data range {lo:.6g}…{hi:.6g}"
        return (
            f"Pure value for {comp} ({pv:.6g}) is orders of magnitude away from "
            f"{ref_txt} — likely a UNITS or PROPERTY mismatch (e.g. g/cm³ vs "
            f"kg/m³, mPa·s vs Pa·s, or a molar volume passed to a mass-density "
            f"fit). Pure anchors must be in the same units as the block's y "
            f"column. Use get_pure_values on this block, or omit pure values "
            f"to use the block's own endpoints."
        )

    # ---- 1. Named values: deterministic axis mapping ----
    if named_values:
        v1 = _named_pure_lookup(named_values, comp_x1)
        v0 = _named_pure_lookup(named_values, comp_x0)
        if v0 is None or v1 is None:
            missing = [c for c, v in ((comp_x0, v0), (comp_x1, v1)) if v is None]
            return {
                "error": (
                    f"pure_values keys {list(named_values.keys())} could not be "
                    f"matched to block component(s) {missing}. Use the block's "
                    f"component names: {comp_names} (see get_pure_values output)."
                ),
            }
        v0, v1 = float(v0), float(v1)
        first_err = (
            _scale_check(v0, comp_x0, f"{x_col}=0", edge0)
            or _scale_check(v1, comp_x1, f"{x_col}=1", edge1)
        )
        if first_err:
            return {"error": first_err}
        note = None
        if abs(v0) < 1e-300 and abs(v1) < 1e-300:
            note = "Both named pure values are 0 (excess-property convention)."
        return v0, v1, "named (matched to composition axis)", note

    # ---- 2. Nothing given: extract from the block's own edges ----
    x_dict = {comp_x1: x_all, comp_x0: 1.0 - x_all}
    try:
        info = extract_pure_from_edges(x_dict, y_all, threshold=edge_threshold)
    except Exception as e:
        return {"error": f"Pure-value extraction from block edges failed: {e}"}
    if comp_x0 not in info or comp_x1 not in info:
        return {"error": (
            "No pure values given and the block's composition coverage is "
            "insufficient to extract direct endpoints. Provide pure_values "
            f"keyed by component name ({comp_names})."
        )}
    d0, d1 = info[comp_x0], info[comp_x1]
    source = (
        f"block-edges ({comp_x0}: {d0['method']}/{d0['quality']}, "
        f"{comp_x1}: {d1['method']}/{d1['quality']})"
    )
    return float(d0["value"]), float(d1["value"]), source, None


def _validate_column_list(raw: list[str] | None) -> list[str]:
    """Validate an optional array of exact column names."""
    if raw is None:
        return []
    if not isinstance(raw, list) or not all(
        isinstance(value, str) and value for value in raw
    ):
        raise TypeError("column override must be an array of non-empty strings")
    return raw


def _validate_constraints(raw: dict | None) -> dict:
    """Validate a structured constraint object.

    Returns an empty object when omitted. Each value must be an object with
    exactly ``value`` and optional ``tol``, or ``sweep`` and optional ``tol``.
    """
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise TypeError("x_vars_constrained must be an object")
    for col, spec in raw.items():
        if not isinstance(col, str) or not col:
            raise TypeError("constraint column names must be non-empty strings")
        if not isinstance(spec, dict) or ("value" not in spec and not spec.get("sweep")):
            raise ValueError(
                f"Constraint for '{col}' must be a dict with a 'value' key "
                f"(or '\"sweep\": true'), got {spec!r}"
            )
        allowed = {"value", "tol"} if "value" in spec else {"sweep", "tol"}
        unknown = sorted(set(spec) - allowed)
        if unknown:
            raise ValueError(f"Constraint for {col!r} has undeclared fields: {unknown}")
        if "sweep" in spec and spec["sweep"] is not True:
            raise ValueError(f"Constraint for {col!r}.sweep must be true")
        for numeric_field in ("value", "tol"):
            if numeric_field in spec and (
                isinstance(spec[numeric_field], bool)
                or not isinstance(spec[numeric_field], (int, float))
            ):
                raise TypeError(
                    f"Constraint for {col!r}.{numeric_field} must be a JSON number"
                )
    return raw


def _validate_named_pure_values(raw: dict, *, context: str) -> None:
    """Validate an exact two-component, name-keyed pure-value object."""
    if not isinstance(raw, dict) or len(raw) != 2:
        raise TypeError(f"{context} must be an object keyed by exactly two component names")
    reserved = {str(key).strip().casefold() for key in raw} & {"x0", "x1"}
    if reserved:
        raise ValueError(
            f"{context} accepts component-name keys only; positional keys are forbidden: "
            f"{sorted(reserved)}"
        )
    for component, value in raw.items():
        if not isinstance(component, str) or not component:
            raise TypeError(f"{context} component keys must be non-empty strings")
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{context}[{component!r}] must be a JSON number")


def _extract_and_match(
    doi, block_number, BLKsubsys_id, property_hint, composition_hint
):
    """Extract block arrays + identify columns; return (bd, match) or error dict.

    When extraction or column-matching fails, the error dict includes
    actionable hints (available blocks / columns / properties) so the
    calling LLM can self-correct.
    """
    bd = extract_block_arrays(doi, block_number, BLKsubsys_id=BLKsubsys_id, property_filter=property_hint or None)
    if not bd.ok:
        err: dict = {"error": bd.error, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id}
        # If the block itself was found but had no rows after property filtering,
        # retry without the filter so we can report what properties exist.
        if bd.n_rows == 0 and property_hint:
            bd_all = extract_block_arrays(doi, block_number, BLKsubsys_id=BLKsubsys_id)
            if bd_all.ok:
                err["hint"] = (
                    f"property_hint='{property_hint}' filtered out all property "
                    f"columns. Available columns (unfiltered): {bd_all.columns}"
                )
        _log.warning("Block extraction failed: %s %s — %s", doi, block_number, bd.error)
        return err

    match = identify_columns(bd.columns, property_hint, composition_hint, metadata=bd.metadata)
    if not match.ok:
        # Provide the full unfiltered column list if property_hint was used
        all_columns = bd.columns
        if property_hint:
            bd_all = extract_block_arrays(doi, block_number, BLKsubsys_id=BLKsubsys_id)
            if bd_all.ok:
                all_columns = bd_all.columns
        err = {
            "error": match.error,
            "columns_available": bd.columns,
            "doi": doi,
            "block_number": block_number,
            "BLKsubsys_id": BLKsubsys_id,
        }
        if property_hint and all_columns != bd.columns:
            err["all_columns_unfiltered"] = all_columns
            err["hint"] = (
                f"property_hint='{property_hint}' did not match any property "
                f"column. Try one of the actual property columns or omit the hint."
            )
        _log.warning(
            "Column matching failed: %s %s — %s (columns: %s)",
            doi, block_number, match.error, bd.columns,
        )
        return err
    return bd, match


# ------------------------------------------------------------------
#  fit_block  (unified entry point)
# ------------------------------------------------------------------

@uses_compactors(compact_fit_block)
def fit_block(
    doi: str,
    block_number: str,
    BLKsubsys_id: str | None = None,
    property_hint: str = "",
    property_type: str = "",
    component_names: list[str] | None = None,
    composition_hint: str = "mole_fraction",
    max_rk_order: int = 5,
    mixing_rule: str = "",
    x_vars: list[str] | None = None,
    y_props: list[str] | None = None,
    x_vars_constrained: dict | None = None,
    properties: list[dict] | None = None,
    pure_values: dict | None = None,
    temperature_tolerance: float = 0.5,
) -> dict:
    """Unified binary-mixture RK fitting from a ThermoML block.

    Supports three modes, auto-detected from parameters:

    **Single fit** (default)
        Fits one property at one constraint value.

    **Multi-property** (when ``properties`` is provided)
        Fits multiple properties from the same block. Each property
        spec contains ``hint``, ``type``, and
        optionally ``mixing_rule``.  Pure values come from
        ``pure_values``.

    **Temperature sweep** (when a constraint has ``"sweep": true``)
        Discovers all unique values for the sweep column and fits each
        independently. Per-temperature pure values come from
        ``pure_values`` with numeric-string keys (e.g. ``"298.15"``).

    Parameters
    ----------
    doi, block_number : str
        Block identifier.
    property_hint : str
        Substring to identify the property column.
    property_type : str
        Property category for mixing rule selection
        ("density", "viscosity", etc.).
    component_names : list[str] | None
        Exact two-component name array.
    composition_hint : str
        Substring for composition column (default "mole_fraction").
    max_rk_order : int
        Max RK polynomial order (BIC selects best).
    mixing_rule : str
        "linear", "arrhenius", or "both".
    x_vars : list[str] | None
        Composition column names.
    y_props : list[str] | None
        Property column names.
    x_vars_constrained : dict | None
        Constraint specs. A constraint with
        ``"sweep": true`` triggers temperature-sweep mode.
        Example: ``{"Temperature, K": {"sweep": true, "tol": 0.5}}``.
    properties : list[dict] | None
        Property specs for multi-property mode:
        ``[{"hint": "density", "type": "density"}, ...]``
    pure_values : dict | None
        Pure values. Format depends on mode:
        - Single fit (RECOMMENDED): ``{"water": 0.000896, "ethanol": 0.001085}``
          — keyed by component name; the tool maps names to the
          composition axis itself (this is exactly the dict returned
          by ``get_pure_values``).
        - Multi-property: ``{"water": {"density": 997}, "ethanol": {"density": 789}}``
          (component-name keyed only)
        - Temperature sweep: name-keyed dict applied to all temperatures,
          or per-temperature component-name objects such as
          ``{"298.15": {"water": 0.6, "ethanol": 0.2}}``.
    temperature_tolerance : float
        Grouping tolerance for temperature sweep (default 0.5 K).
    """
    # ── Mode detection ────────────────────────────────────────
    if properties is not None:
        return _dispatch_multi_property(
            doi=doi, block_number=block_number,
            BLKsubsys_id=BLKsubsys_id,
            properties=properties,
            pure_values=pure_values,
            component_names=component_names,
            composition_hint=composition_hint,
            max_rk_order=max_rk_order,
            x_vars=x_vars,
            x_vars_constrained=x_vars_constrained,
        )

    constraints = _validate_constraints(x_vars_constrained)

    sweep_col = None
    sweep_tol = 0.5
    non_sweep_constraints: dict = {}
    for c_col, c_spec in constraints.items():
        if isinstance(c_spec, dict) and c_spec.get("sweep"):
            sweep_col = c_col
            sweep_tol = float(c_spec.get("tol", temperature_tolerance))
        else:
            non_sweep_constraints[c_col] = c_spec

    if sweep_col is not None:
        return _dispatch_temperature_sweep(
            doi=doi, block_number=block_number,
            BLKsubsys_id=BLKsubsys_id,
            property_hint=property_hint, property_type=property_type,
            pure_values=pure_values,
            component_names=component_names,
            composition_hint=composition_hint,
            max_rk_order=max_rk_order,
            mixing_rule=mixing_rule,
            x_vars=x_vars, y_props=y_props,
            sweep_col=sweep_col, sweep_tol=sweep_tol,
            non_sweep_constraints=non_sweep_constraints,
        )

    # ── Single-fit mode ───────────────────────────────────────
    # Name-keyed pure values (the get_pure_values dict) map to the
    # composition axis inside _fit_single — never positionally.
    pure_values_named: dict | None = None
    if pure_values is not None:
        _validate_named_pure_values(pure_values, context="pure_values")
        pure_values_named = pure_values

    return _fit_single(
        doi=doi, block_number=block_number,
        BLKsubsys_id=BLKsubsys_id,
        property_hint=property_hint, property_type=property_type,
        pure_values_named=pure_values_named,
        component_names=component_names,
        composition_hint=composition_hint,
        max_rk_order=max_rk_order, mixing_rule=mixing_rule,
        x_vars=x_vars, y_props=y_props,
        constraints=constraints,
    )


# ------------------------------------------------------------------
#  _fit_single  (core single-property, single-constraint fit)
# ------------------------------------------------------------------

def _fit_single(
    *,
    doi: str,
    block_number: str,
    BLKsubsys_id: str | None,
    property_hint: str,
    property_type: str,
    pure_values_named: dict | None = None,
    component_names: list[str] | None = None,
    composition_hint: str = "mole_fraction",
    max_rk_order: int = 5,
    mixing_rule: str = "",
    x_vars: list[str] | None = None,
    y_props: list[str] | None = None,
    constraints: dict | None = None,
) -> dict:
    """Core RK fitting: one property, one set of constraints."""
    if isinstance(max_rk_order, bool) or not isinstance(max_rk_order, int) or max_rk_order < 0:
        raise ValueError("max_rk_order must be a non-negative integer")

    result = _extract_and_match(
        doi, block_number, BLKsubsys_id, property_hint, composition_hint
    )
    if isinstance(result, dict):
        _log.warning(
            "fit_block: extraction failed for %s %s — %s",
            doi, block_number, result.get("error", "?"),
        )
        return result
    bd, match = result

    # ---- Parse explicit column overrides ----
    _x_overrides = _validate_column_list(x_vars)
    _y_overrides = _validate_column_list(y_props)
    if constraints is None:
        constraints = {}

    x_col = _x_overrides[0] if _x_overrides else match.x_column
    y_col = _y_overrides[0] if _y_overrides else match.y_column

    for _col_name, _label in [(x_col, "x"), (y_col, "y")]:
        if _col_name not in bd.arrays:
            return {
                "error": f"Requested {_label} column '{_col_name}' not found in block",
                "columns_available": bd.columns, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id,
            }

    x_all = bd.arrays[x_col]
    y_all = bd.arrays[y_col]

    # ---- Constraint filtering (explicit or auto-temperature) ----
    selected_temp = None
    applied_constraints: dict = {}
    state_mask: np.ndarray | None = None
    if constraints:
        row_mask = np.ones(len(x_all), dtype=bool)
        for c_col, c_spec in constraints.items():
            if c_col not in bd.arrays:
                return {
                    "error": f"Constraint column '{c_col}' not found in block",
                    "columns_available": bd.columns, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id,
                }
            c_val = float(c_spec["value"])
            c_tol = float(c_spec.get("tol", 0.5))
            row_mask &= np.abs(bd.arrays[c_col] - c_val) <= c_tol
            applied_constraints[c_col] = {"value": c_val, "tol": c_tol}
            if "temperature" in c_col.lower():
                selected_temp = c_val
        x_all = x_all[row_mask]
        y_all = y_all[row_mask]
        state_mask = row_mask
    else:
        # A multi-state block needs an explicit constraint or sweep.
        temp_col = next((c for c in bd.columns if "temperature" in c.lower()), None)
        if temp_col and temp_col in bd.arrays:
            t_all = bd.arrays[temp_col]
            valid_t = t_all[~np.isnan(t_all)]
            unique_temps = np.unique(valid_t)
            if len(unique_temps) > 1:
                return {
                    "error": (
                        f"STATE_REFINEMENT_REQUIRED: block contains {len(unique_temps)} "
                        f"temperatures; constrain {temp_col!r} with value/tol or sweep=true"
                    ),
                    "doi": doi,
                    "block_number": block_number,
                    "BLKsubsys_id": BLKsubsys_id,
                    "temperature_values": unique_temps.tolist(),
                }
            if len(unique_temps) == 1:
                selected_temp = float(unique_temps[0])

    # ---- Composition basis gate (canonical fitting basis = mole) ----
    comp_names = _resolve_comp_names(component_names, bd.metadata)
    comp_names = _order_comps_by_x_column(comp_names, match)
    gate = _apply_composition_basis_gate(
        bd, x_col, x_all, comp_names, state_mask,
        selected_temp=selected_temp,
    )
    if "error" in gate:
        return {**gate, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id,
                "columns_available": bd.columns}
    x_all = gate["x"]
    composition_basis = gate["basis"]
    composition_note = gate["note"]

    # ---- Property-response gate ---------------------------------------
    # PCS ``presentation`` is a mathematical declaration, not display
    # metadata.  Materialize X from X-Xref, X/Xref, etc. before endpoints,
    # ideal baselines, excess values, or RK coefficients are calculated.
    response_state, response_tolerances = _canonical_state_and_tolerances(
        applied_constraints,
        fallback_temperature=selected_temp,
    )
    response_contract = inspect_property_response_contract(bd.metadata, y_col)
    if response_contract["requires_reference_materialization"]:
        for quantity, ref_field in (
            ("temperature_k", "ref_temperature_K"),
            ("pressure_kpa", "ref_pressure_kPa"),
        ):
            if response_contract.get(ref_field) is not None or response_state[quantity] is not None:
                continue
            inferred, distinct = _selected_unique_state_value(
                bd, quantity, state_mask
            )
            if len(distinct) > 1:
                return {
                    "error": (
                        "STATE_REFINEMENT_REQUIRED: reference-relative property "
                        f"has {len(distinct)} selected {quantity} values; constrain "
                        "the state before materialization"
                    ),
                    "doi": doi,
                    "lit_num_id": bd.metadata["lit_num_id"],
                    "block_number": block_number,
                    "BLKsubsys_id": BLKsubsys_id,
                    "state_quantity": quantity,
                    "state_values": distinct,
                }
            response_state[quantity] = inferred
    try:
        response = prepare_property_response(
            metadata=bd.metadata,
            y_column=y_col,
            reported_values=y_all,
            normalized_composition=_normalized_binary_composition(
                bd.metadata, comp_names, x_all
            ),
            state=response_state,
            state_tolerances=response_tolerances,
        )
    except PropertyResponsePreparationError as exc:
        return property_response_error_result(
            exc,
            doi=doi,
            lit_num_id=bd.metadata["lit_num_id"],
            block_number=block_number,
            BLKsubsys_id=BLKsubsys_id,
        )
    y_all = response.values
    property_response = response.trace

    x_mix, y_mix = filter_mixture_points(x_all, y_all, eps=0.02)

    if len(x_mix) < 3:
        return {
            "error": f"Only {len(x_mix)} mixture points (need >= 3 for RK fit)",
            "n_total_points": bd.n_rows,
            "n_mixture_points": len(x_mix),
            "columns_used": {"x": x_col, "y": y_col},
            "selected_temperature_K": selected_temp,
            "applied_constraints": applied_constraints or None,
            "property_response": property_response,
            "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id,
        }

    rule = mixing_rule.lower() if mixing_rule else default_mixing_rule(property_type)

    # A declared excess property is already the non-ideal response.  Its
    # pure-component limit is zero by definition, so subtracting another
    # ideal baseline would manufacture a second, chemically false excess.
    declared_prop_id = str(response.declaration.get("prop_ID") or "")
    declared_excess = declared_prop_id.casefold().startswith("excess_")
    if declared_excess:
        y_ideal = np.zeros_like(y_mix, dtype=float)
        y_excess = np.asarray(y_mix, dtype=float)
        rk = auto_fit_redlich_kister(
            x_mix, y_excess, max_order=max_rk_order
        )
        if "error" in rk:
            return {
                **rk,
                "doi": doi,
                "lit_num_id": bd.metadata["lit_num_id"],
                "block_number": block_number,
                "BLKsubsys_id": BLKsubsys_id,
                "property_response": property_response,
            }
        pure_values = {comp_names[0]: 0.0, comp_names[1]: 0.0}
        raw = {
            "doi": doi,
            "lit_num_id": bd.metadata["lit_num_id"],
            "block_number": block_number,
            "BLKsubsys_id": BLKsubsys_id,
            "x_column": x_col,
            "y_column": y_col,
            "rk_coeffs": rk["coeffs"],
            "rk_order": rk["selected_order"],
            "r_squared": rk["r_squared"],
            "rmse": rk["rmse"],
            "bic": rk.get("bic"),
            "n_mixture_points": len(x_mix),
            "n_total_points": bd.n_rows,
            "mixing_rule": "declared_excess_no_baseline",
            "pure_values": pure_values,
            "components": comp_names,
            "pure_values_source": "declared excess property: zero at pure limits",
            "property_response": property_response,
            "bic_analysis": rk.get("all_orders", []),
            "classification": classify_excess(
                y_excess, x_mix, property_type, rmse=rk.get("rmse")
            ),
            "route": "measured-direct-excess (no second baseline)",
        }
        if applied_constraints:
            raw["applied_constraints"] = applied_constraints
        if selected_temp is not None:
            raw["selected_temperature_K"] = selected_temp
        if composition_basis not in ("mole_fraction", "unknown"):
            raw["composition_basis"] = composition_basis
        if composition_note:
            raw["composition_conversion"] = composition_note
        output_files = _save_fit_outputs(
            doi,
            block_number,
            x_mix,
            y_mix,
            y_ideal,
            y_excess,
            rk,
            BLKsubsys_id=BLKsubsys_id,
            mixing_rule="declared_excess_no_baseline",
            components=comp_names,
            y_label=y_col,
            temperature_K=selected_temp,
            pure_values=pure_values,
            property_type=property_type,
            pure_values_source=raw["pure_values_source"],
            block_metadata=bd.metadata,
        )
        if output_files:
            raw["output_files"] = output_files
        return raw

    # ---- Resolve pure-component anchors via the parsed axis identity ----
    # x_all/y_all are already state-filtered, so extracted endpoints and
    # swap validation refer to the same temperature/pressure as the fit.
    resolved = None
    # Same-proportion materialization already resolved every pure component
    # at this state. Reuse those exact reviewed anchors; asking the agent to
    # supply them again would duplicate evidence and can introduce mismatch.
    response_ref = property_response.get("reference_state")
    response_component_values = (
        response_ref.get("component_values")
        if isinstance(response_ref, dict) else None
    )
    if pure_values_named is None and isinstance(response_component_values, dict):
        compounds_by_name = {
            str(item.get("name", "")).strip().casefold(): item.get("comp_num_id")
            for item in bd.metadata.get("compounds", [])
            if isinstance(item, dict) and isinstance(item.get("comp_num_id"), str)
        }
        comp_x1_id = compounds_by_name.get(comp_names[0].strip().casefold())
        comp_x0_id = compounds_by_name.get(comp_names[1].strip().casefold())
        if comp_x1_id in response_component_values and comp_x0_id in response_component_values:
            resolved = (
                float(response_component_values[comp_x0_id]),
                float(response_component_values[comp_x1_id]),
                "property-presentation direct unary reference ensemble",
                "Pure anchors reused from same-proportion response materialization.",
            )
    if resolved is None:
        resolved = _resolve_pure_values(
            comp_names=comp_names, x_col=x_col,
            x_all=x_all, y_all=y_all,
            named_values=pure_values_named,
            y_col=y_col,
            state=(
                {k: v["value"] for k, v in applied_constraints.items()}
                if applied_constraints
                else ({"temperature_k": selected_temp} if selected_temp is not None else None)
            ),
            metadata=bd.metadata,
        )
    if isinstance(resolved, dict):
        return {**resolved, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id,
                "components": comp_names, "x_column": x_col,
                "selected_temperature_K": selected_temp}
    pure_at_x0, pure_at_x1, pv_source, pv_note = resolved
    pure_values = {comp_names[0]: pure_at_x1, comp_names[1]: pure_at_x0}
    if pv_note:
        _log.info("fit_block %s %s: %s", doi, block_number, pv_note)

    # ---- dual-baseline path ----
    if rule == "both":
        excess = compute_excess_property(
            x_mix, y_mix, pure_values, property_type,
            mixing_rule="both", component_order=comp_names,
        )
        if "error" in excess:
            return {**excess, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id}

        excess_dict = {
            "linear":    np.array(excess["y_excess_linear"]),
            "arrhenius": np.array(excess["y_excess_arrhenius"]),
        }
        rk_both = fit_multi_property(x_mix, excess_dict, max_order=max_rk_order)

        def _sub(key, label_key):
            r = rk_both[key]
            if "error" in r:
                return {"error": r["error"]}
            return {
                "mixing_rule": key,
                "excess_label": excess[label_key],
                "rk_coeffs": r.get("coeffs"),
                "rk_order": r.get("selected_order"),
                "r_squared": r.get("r_squared"),
                "rmse": r.get("rmse"),
                "bic": r.get("bic"),
                "bic_analysis": r.get("all_orders", []),
            }

        raw = {
            "doi": doi, "lit_num_id": bd.metadata["lit_num_id"],
            "block_number": block_number, "BLKsubsys_id": BLKsubsys_id,
            "x_column": x_col, "y_column": y_col,
            "mixing_rule": "both",
            "n_mixture_points": len(x_mix), "n_total_points": bd.n_rows,
            "pure_values": pure_values, "components": comp_names,
            "pure_values_source": pv_source,
            "property_response": property_response,
            "fit_linear":    _sub("linear",    "excess_label_linear"),
            "fit_arrhenius": _sub("arrhenius", "excess_label_arrhenius"),
        }
        if pv_note:
            raw["pure_values_note"] = pv_note
        if applied_constraints:
            raw["applied_constraints"] = applied_constraints
        for _rk, _yk in [("linear", "y_excess_linear"),
                          ("arrhenius", "y_excess_arrhenius")]:
            _ye = excess.get(_yk, [])
            if _ye:
                raw[f"classification_{_rk}"] = classify_excess(
                    _ye, x_mix, property_type,
                    rmse=rk_both.get(_rk, {}).get("rmse"),
                )
        raw["route"] = "measured-direct"
        if composition_basis not in ("mole_fraction", "unknown"):
            raw["composition_basis"] = composition_basis
        if composition_note:
            raw["composition_conversion"] = composition_note
        if selected_temp is not None:
            raw["selected_temperature_K"] = selected_temp

        all_outputs: dict[str, str] = {}
        y_ideal_lin = np.array(excess.get("y_ideal_linear", []))
        y_ideal_arr = np.array(excess.get("y_ideal_arrhenius", []))
        for rule_key, y_exc, y_id in [
            ("linear", excess_dict["linear"], y_ideal_lin),
            ("arrhenius", excess_dict["arrhenius"], y_ideal_arr),
        ]:
            rk_sub = rk_both.get(rule_key, {})
            if "error" not in rk_sub and len(y_id) > 0:
                outs = _save_fit_outputs(
                    doi, block_number, x_mix, y_mix, y_id, y_exc, rk_sub,
                    BLKsubsys_id=BLKsubsys_id,
                    mixing_rule=rule_key, components=comp_names,
                    y_label=y_col, temperature_K=selected_temp,
                    pure_values=pure_values, property_type=property_type,
                    pure_values_source=pv_source,
                    block_metadata=bd.metadata,
                )
                for k, v in outs.items():
                    all_outputs[f"{rule_key}_{k}"] = v
        if all_outputs:
            raw["output_files"] = all_outputs

        return raw

    # ---- single-baseline path ----
    baseline = build_ideal_baseline(
        pure_values, x_mix, property_type,
        mixing_rule=rule, component_order=comp_names,
    )
    if "error" in baseline:
        return {**baseline, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id}

    y_ideal = np.array(baseline["y_ideal"])
    y_excess = (np.log(y_mix) - np.log(y_ideal)) if rule == "arrhenius" else (y_mix - y_ideal)

    rk = auto_fit_redlich_kister(x_mix, y_excess, max_order=max_rk_order)
    if "error" in rk:
        return {**rk, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id}

    raw = {
        "doi": doi, "lit_num_id": bd.metadata["lit_num_id"],
        "block_number": block_number, "BLKsubsys_id": BLKsubsys_id,
        "x_column": x_col, "y_column": y_col,
        "rk_coeffs": rk["coeffs"], "rk_order": rk["selected_order"],
        "r_squared": rk["r_squared"], "rmse": rk["rmse"],
        "bic": rk.get("bic"),
        "n_mixture_points": len(x_mix), "n_total_points": bd.n_rows,
        "mixing_rule": baseline["mixing_rule"],
        "pure_values": pure_values, "components": comp_names,
        "pure_values_source": pv_source,
        "property_response": property_response,
        "bic_analysis": rk.get("all_orders", []),
        "classification": classify_excess(y_excess, x_mix, property_type,
                                          rmse=rk.get("rmse")),
        "route": "measured-direct",
    }
    if rk.get("coeff_std_errors"):
        raw["rk_coeff_std_errors"] = rk["coeff_std_errors"]
        if rk.get("insignificant_coeffs"):
            raw["insignificant_coeffs"] = rk["insignificant_coeffs"]
    if rk.get("sparse_data_note"):
        raw["fit_note"] = rk["sparse_data_note"]
    if composition_basis not in ("mole_fraction", "unknown"):
        raw["composition_basis"] = composition_basis
    if composition_note:
        raw["composition_conversion"] = composition_note
    if pv_note:
        raw["pure_values_note"] = pv_note
    if selected_temp is not None:
        raw["selected_temperature_K"] = selected_temp
    if applied_constraints:
        raw["applied_constraints"] = applied_constraints

    output_files = _save_fit_outputs(
        doi, block_number, x_mix, y_mix, y_ideal, y_excess, rk,
                    BLKsubsys_id=BLKsubsys_id,
        mixing_rule=baseline["mixing_rule"], components=comp_names,
        y_label=y_col, temperature_K=selected_temp,
        pure_values=pure_values, property_type=property_type,
        pure_values_source=pv_source,
        block_metadata=bd.metadata,
    )
    if output_files:
        raw["output_files"] = output_files

    return raw


# ------------------------------------------------------------------
#  _dispatch_multi_property  (internal: loop over properties)
# ------------------------------------------------------------------

def _dispatch_multi_property(
    *,
    doi: str,
    block_number: str,
    BLKsubsys_id: str | None,
    properties: list[dict],
    pure_values: dict | None,
    component_names: list[str] | None = None,
    composition_hint: str = "mole_fraction",
    max_rk_order: int = 5,
    x_vars: list[str] | None = None,
    x_vars_constrained: dict | None = None,
) -> dict:
    """Fit RK polynomials for multiple properties from the same block."""
    if isinstance(max_rk_order, bool) or not isinstance(max_rk_order, int) or max_rk_order < 0:
        raise ValueError("max_rk_order must be a non-negative integer")

    if not isinstance(properties, list) or not properties:
        raise TypeError("properties must be a non-empty array of property specs")
    validated_properties: list[dict] = []
    labels: set[str] = set()
    for index, spec in enumerate(properties):
        if not isinstance(spec, dict):
            raise TypeError(f"properties[{index}] must be an object")
        unknown = sorted(set(spec) - {"hint", "type", "mixing_rule"})
        missing = sorted({"hint", "type"} - set(spec))
        if unknown or missing:
            raise ValueError(
                f"properties[{index}] has missing={missing} and unknown={unknown} fields"
            )
        for field in ("hint", "type"):
            if not isinstance(spec[field], str) or not spec[field]:
                raise TypeError(f"properties[{index}].{field} must be a non-empty string")
        if "mixing_rule" in spec and (
            not isinstance(spec["mixing_rule"], str) or not spec["mixing_rule"]
        ):
            raise TypeError(
                f"properties[{index}].mixing_rule must be a non-empty string when present"
            )
        if spec["hint"] in labels:
            raise ValueError(f"duplicate property hint: {spec['hint']!r}")
        labels.add(spec["hint"])
        validated_properties.append(spec)

    if pure_values is not None:
        if not isinstance(pure_values, dict) or len(pure_values) != 2:
            raise TypeError(
                "multi-property pure_values must be an object keyed by exactly two component names"
            )
        reserved = {str(key).strip().casefold() for key in pure_values} & {"x0", "x1"}
        if reserved:
            raise ValueError(
                "pure_values accepts component-name keys only; "
                f"positional keys are forbidden: {sorted(reserved)}"
            )
        for component, values in pure_values.items():
            if not isinstance(component, str) or not component:
                raise TypeError("pure_values component keys must be non-empty strings")
            if not isinstance(values, dict):
                raise TypeError(
                    f"pure_values[{component!r}] must be an object keyed by property hint"
                )
            unknown = sorted(set(values) - labels)
            missing = sorted(labels - set(values))
            if unknown or missing:
                raise ValueError(
                    f"pure_values[{component!r}] has missing={missing} and unknown={unknown} property hints"
                )
            if any(
                isinstance(value, bool) or not isinstance(value, (int, float))
                for value in values.values()
            ):
                raise TypeError(
                    f"pure_values[{component!r}] values must all be JSON numbers"
                )

    results = {}
    constraints = _validate_constraints(x_vars_constrained)
    for spec in validated_properties:
        hint = spec["hint"]
        named_vals = (
            {component: values[hint] for component, values in pure_values.items()}
            if pure_values is not None
            else None
        )
        results[hint] = _fit_single(
            doi=doi, block_number=block_number,
            BLKsubsys_id=BLKsubsys_id,
            property_hint=hint, property_type=spec["type"],
            pure_values_named=named_vals,
            component_names=component_names, composition_hint=composition_hint,
            max_rk_order=max_rk_order, mixing_rule=spec.get("mixing_rule", ""),
            x_vars=x_vars,
            constraints=constraints,
        )

    return {
        "doi": doi,
        "block_number": block_number,
        "BLKsubsys_id": BLKsubsys_id,
        "n_properties": len(validated_properties),
        "results": results,
    }


# ------------------------------------------------------------------
#  _dispatch_temperature_sweep  (internal: fit per unique temperature)
# ------------------------------------------------------------------

def _dispatch_temperature_sweep(
    *,
    doi: str,
    block_number: str,
    BLKsubsys_id: str | None,
    property_hint: str,
    property_type: str,
    pure_values: dict | None = None,
    component_names: list[str] | None = None,
    composition_hint: str = "mole_fraction",
    max_rk_order: int = 5,
    mixing_rule: str = "",
    x_vars: list[str] | None = None,
    y_props: list[str] | None = None,
    sweep_col: str = "",
    sweep_tol: float = 0.5,
    non_sweep_constraints: dict | None = None,
) -> dict:
    """Discover unique values in *sweep_col* and fit each independently."""
    if isinstance(max_rk_order, bool) or not isinstance(max_rk_order, int) or max_rk_order < 0:
        raise ValueError("max_rk_order must be a non-negative integer")

    # Pure values are either one component-name object applied at every
    # state, or an object keyed by numeric temperature strings whose values
    # are component-name objects. Positional endpoint arrays are forbidden.
    pv_by_temp: dict | None = None
    pv_named: dict | None = None
    if pure_values is not None:
        if not isinstance(pure_values, dict) or not pure_values:
            raise TypeError("sweep pure_values must be a non-empty object when supplied")
        values = list(pure_values.values())
        if all(isinstance(value, dict) for value in values):
            pv_by_temp = pure_values
            for temp_key, named in pv_by_temp.items():
                try:
                    float(temp_key)
                except (TypeError, ValueError) as exc:
                    raise ValueError(
                        f"per-temperature pure_values key {temp_key!r} is not numeric"
                    ) from exc
                _validate_named_pure_values(named, context=f"pure_values[{temp_key!r}]")
        elif all(
            isinstance(value, (int, float)) and not isinstance(value, bool)
            for value in values
        ):
            _validate_named_pure_values(pure_values, context="pure_values")
            pv_named = pure_values
        else:
            raise TypeError(
                "sweep pure_values must contain either only numeric component values "
                "or only per-temperature component-name objects"
            )

    result = _extract_and_match(
        doi, block_number, BLKsubsys_id, property_hint, composition_hint
    )
    if isinstance(result, dict):
        _log.warning(
            "fit_block (sweep): extraction failed for %s %s — %s",
            doi, block_number, result.get("error", "?"),
        )
        return result
    bd, match = result

    _x_overrides = _validate_column_list(x_vars)
    _y_overrides = _validate_column_list(y_props)
    x_col = _x_overrides[0] if _x_overrides else match.x_column
    y_col = _y_overrides[0] if _y_overrides else match.y_column
    for _col_name, _label in [(x_col, "x"), (y_col, "y")]:
        if _col_name not in bd.arrays:
            return {
                "error": f"Requested {_label} column '{_col_name}' not found in block",
                "columns_available": bd.columns, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id,
            }

    if sweep_col not in bd.arrays:
        return {
            "error": f"Sweep column '{sweep_col}' not found in block",
            "columns_available": bd.columns, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id,
        }

    x_all = bd.arrays[x_col]
    y_all = bd.arrays[y_col]
    sweep_all = bd.arrays[sweep_col]

    # Apply non-sweep constraints first
    sweep_state_mask: np.ndarray | None = None
    if non_sweep_constraints:
        pre_mask = np.ones(len(x_all), dtype=bool)
        for c_col, c_spec in non_sweep_constraints.items():
            if c_col not in bd.arrays:
                return {"error": f"Constraint column '{c_col}' not found",
                        "columns_available": bd.columns, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id}
            c_val = float(c_spec["value"])
            c_tol = float(c_spec.get("tol", 0.5))
            pre_mask &= np.abs(bd.arrays[c_col] - c_val) <= c_tol
        x_all = x_all[pre_mask]
        y_all = y_all[pre_mask]
        sweep_all = sweep_all[pre_mask]
        sweep_state_mask = pre_mask

    comp_names = _resolve_comp_names(component_names, bd.metadata)
    comp_names = _order_comps_by_x_column(comp_names, match)

    # ---- Composition basis gate (once, before per-value slicing) ----
    gate = _apply_composition_basis_gate(
        bd, x_col, x_all, comp_names, sweep_state_mask,
        sweep_mode=True,
    )
    if "error" in gate:
        return {**gate, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id,
                "columns_available": bd.columns}
    x_all = gate["x"]
    sweep_composition_basis = gate["basis"]
    sweep_composition_note = gate["note"]

    # Group by unique sweep values
    valid = ~np.isnan(sweep_all) & ~np.isnan(x_all) & ~np.isnan(y_all)
    sweep_valid = sweep_all[valid]
    unique_vals: list[float] = []
    for v in np.sort(np.unique(sweep_valid)):
        if not unique_vals or abs(v - unique_vals[-1]) > sweep_tol:
            unique_vals.append(float(v))

    rule = mixing_rule.lower() if mixing_rule else default_mixing_rule(property_type)

    per_value = []
    for V in unique_vals:
        mask = valid & (np.abs(sweep_all - V) <= sweep_tol)
        x_V, y_V = x_all[mask], y_all[mask]

        step_constraints = dict(non_sweep_constraints or {})
        step_constraints[sweep_col] = {"value": V, "tol": sweep_tol}
        response_state, response_tolerances = _canonical_state_and_tolerances(
            step_constraints
        )
        response_contract = inspect_property_response_contract(
            bd.metadata, y_col
        )
        state_refinement = None
        if response_contract["requires_reference_materialization"]:
            for quantity, token, ref_field in (
                ("temperature_k", "temperature", "ref_temperature_K"),
                ("pressure_kpa", "pressure", "ref_pressure_kPa"),
            ):
                if (
                    response_state[quantity] is not None
                    or response_contract.get(ref_field) is not None
                ):
                    continue
                selected_arrays = []
                for column in bd.columns:
                    if token not in column.casefold() or column not in bd.arrays:
                        continue
                    array = np.asarray(bd.arrays[column], dtype=float)
                    if sweep_state_mask is not None:
                        array = array[sweep_state_mask]
                    finite = array[mask]
                    finite = finite[np.isfinite(finite)]
                    if finite.size:
                        selected_arrays.append(finite)
                if selected_arrays:
                    distinct = np.unique(
                        np.round(np.concatenate(selected_arrays), decimals=10)
                    )
                    if len(distinct) > 1:
                        state_refinement = {
                            "sweep_value": V,
                            "error": (
                                "STATE_REFINEMENT_REQUIRED: sweep slice has "
                                f"{len(distinct)} {quantity} values"
                            ),
                            "state_quantity": quantity,
                            "state_values": distinct.astype(float).tolist(),
                        }
                        break
                    response_state[quantity] = float(distinct[0])
        if state_refinement is not None:
            per_value.append(state_refinement)
            continue
        try:
            response = prepare_property_response(
                metadata=bd.metadata,
                y_column=y_col,
                reported_values=y_V,
                normalized_composition=_normalized_binary_composition(
                    bd.metadata, comp_names, x_V
                ),
                state=response_state,
                state_tolerances=response_tolerances,
            )
        except PropertyResponsePreparationError as exc:
            per_value.append({
                "sweep_value": V,
                **property_response_error_result(
                    exc,
                    doi=doi,
                    lit_num_id=bd.metadata["lit_num_id"],
                    block_number=block_number,
                    BLKsubsys_id=BLKsubsys_id,
                ),
            })
            continue
        y_V = response.values

        eps = 0.02
        mix_mask = (x_V > eps) & (x_V < 1.0 - eps)
        x_mix, y_mix = x_V[mix_mask], y_V[mix_mask]

        if len(x_mix) < 3:
            per_value.append({
                "sweep_value": V,
                "error": f"Only {len(x_mix)} mixture points at {sweep_col}={V}",
                "n_total_points": int(mask.sum()),
            })
            continue

        if str(response.declaration.get("prop_ID") or "").casefold().startswith("excess_"):
            y_ideal = np.zeros_like(y_mix, dtype=float)
            y_excess = np.asarray(y_mix, dtype=float)
            rk = auto_fit_redlich_kister(
                x_mix, y_excess, max_order=max_rk_order
            )
            if "error" in rk:
                per_value.append({"sweep_value": V, **rk})
                continue
            pure_values = {comp_names[0]: 0.0, comp_names[1]: 0.0}
            pure_source = "declared excess property: zero at pure limits"
            output_files = _save_fit_outputs(
                doi, block_number, x_mix, y_mix, y_ideal, y_excess, rk,
                BLKsubsys_id=BLKsubsys_id,
                mixing_rule="declared_excess_no_baseline",
                components=comp_names,
                y_label=y_col,
                temperature_K=V,
                pure_values=pure_values,
                property_type=property_type,
                pure_values_source=pure_source,
                block_metadata=bd.metadata,
            )
            entry = {
                "sweep_value": V,
                "rk_coeffs": rk["coeffs"],
                "rk_order": rk["selected_order"],
                "r_squared": rk["r_squared"],
                "rmse": rk["rmse"],
                "n_mixture_points": len(x_mix),
                "pure_values": pure_values,
                "pure_values_source": pure_source,
                "property_response": response.trace,
                "route": "measured-direct-excess (no second baseline)",
            }
            if output_files:
                entry["output_files"] = output_files
            per_value.append(entry)
            continue

        # Pure values for this sweep value — resolved against THIS
        # temperature's own data slice (x_V/y_V), so omitted values use
        # per-temperature endpoints are validated at the right state.
        if pv_by_temp is not None:
            matching_keys = [
                key for key in pv_by_temp if abs(float(key) - V) <= sweep_tol
            ]
            if len(matching_keys) != 1:
                per_value.append({
                    "sweep_value": V,
                    "error": (
                        f"Expected exactly one pure_values state within {sweep_tol} "
                        f"of {sweep_col}={V}; matched {matching_keys}"
                    ),
                })
                continue
            step_named = pv_by_temp[matching_keys[0]]
        else:
            step_named = pv_named

        if step_named is None:
            response_ref = response.trace.get("reference_state")
            response_values = (
                response_ref.get("component_values")
                if isinstance(response_ref, dict) else None
            )
            if isinstance(response_values, dict):
                ids_by_name = {
                    str(item.get("name", "")).strip().casefold(): item.get("comp_num_id")
                    for item in bd.metadata.get("compounds", [])
                    if isinstance(item, dict)
                    and isinstance(item.get("comp_num_id"), str)
                }
                automatic = {}
                for name in comp_names:
                    comp_num_id = ids_by_name.get(name.strip().casefold())
                    if comp_num_id in response_values:
                        automatic[name] = float(response_values[comp_num_id])
                if len(automatic) == len(comp_names):
                    step_named = automatic

        resolved = _resolve_pure_values(
            comp_names=comp_names, x_col=x_col,
            x_all=x_V, y_all=y_V,
            named_values=step_named,
            y_col=y_col,
            state={sweep_col: V},
            metadata=bd.metadata,
        )
        if isinstance(resolved, dict):
            per_value.append({"sweep_value": V, **resolved})
            continue
        px0, px1, pv_source, pv_note = resolved

        pure_values = {comp_names[0]: px1, comp_names[1]: px0}

        baseline = build_ideal_baseline(
            pure_values, x_mix, property_type,
            mixing_rule=rule, component_order=comp_names,
        )
        if "error" in baseline:
            per_value.append({"sweep_value": V, **baseline})
            continue

        y_ideal = np.array(baseline["y_ideal"])
        if rule == "arrhenius":
            y_excess = np.log(y_mix) - np.log(y_ideal)
        else:
            y_excess = y_mix - y_ideal

        rk = auto_fit_redlich_kister(x_mix, y_excess, max_order=max_rk_order)
        if "error" in rk:
            per_value.append({"sweep_value": V, **rk})
            continue

        output_files = _save_fit_outputs(
            doi, block_number, x_mix, y_mix, y_ideal, y_excess, rk,
                    BLKsubsys_id=BLKsubsys_id,
            mixing_rule=rule, components=comp_names,
            y_label=y_col, temperature_K=V,
            pure_values=pure_values, property_type=property_type,
            pure_values_source=pv_source,
            block_metadata=bd.metadata,
        )

        entry: dict = {
            "sweep_value": V,
            "rk_coeffs": rk["coeffs"],
            "rk_order": rk["selected_order"],
            "r_squared": rk["r_squared"],
            "rmse": rk["rmse"],
            "n_mixture_points": len(x_mix),
            "pure_values": pure_values,
            "pure_values_source": pv_source,
            "property_response": response.trace,
        }
        if pv_note:
            entry["pure_values_note"] = pv_note
        if output_files:
            entry["output_files"] = output_files
        per_value.append(entry)

    result_sweep = {
        "doi": doi, "lit_num_id": bd.metadata["lit_num_id"],
        "block_number": block_number, "BLKsubsys_id": BLKsubsys_id,
        "components": comp_names, "sweep_column": sweep_col,
        "n_sweep_values": len(unique_vals),
        "per_sweep_value": per_value,
        "mixing_rule": rule,
    }
    if sweep_composition_basis not in ("mole_fraction", "unknown"):
        result_sweep["composition_basis"] = sweep_composition_basis
    if sweep_composition_note:
        result_sweep["composition_conversion"] = sweep_composition_note
    return result_sweep


# ------------------------------------------------------------------
#  fit_multi_system
# ------------------------------------------------------------------

@uses_compactors(compact_fit_multi_system)
def fit_multi_system(systems: list[dict]) -> dict:
    """Fit exact ``fit_block`` requests concurrently.

    Each object requires ``label``, ``doi``, and ``block_number`` and may
    contain only declared ``fit_block`` parameters. ``BLKsubsys_id`` is
    opt-in: omit it for the declared parent or supply an exact ``BLKsubsys_N``
    selector. JSON strings, positional pure endpoints, unnamed jobs, and
    undeclared fields are rejected.
    """
    if not isinstance(systems, list) or not systems:
        raise TypeError("systems must be a non-empty array of objects")
    fit_fields = {
        "doi", "block_number", "BLKsubsys_id", "property_hint", "property_type",
        "component_names", "composition_hint", "max_rk_order", "mixing_rule",
        "x_vars", "y_props", "x_vars_constrained", "properties", "pure_values",
        "temperature_tolerance",
    }
    labels: set[str] = set()
    validated: list[dict] = []
    for index, spec in enumerate(systems):
        if not isinstance(spec, dict):
            raise TypeError(f"systems[{index}] must be an object")
        missing = sorted({"label", "doi", "block_number"} - set(spec))
        unknown = sorted(set(spec) - fit_fields - {"label"})
        if missing or unknown:
            raise ValueError(
                f"systems[{index}] has missing={missing} and unknown={unknown} fields"
            )
        normalized = dict(spec)
        normalized.setdefault("BLKsubsys_id", None)
        for field in ("label", "doi", "block_number"):
            if not isinstance(normalized[field], str) or not normalized[field]:
                raise TypeError(f"systems[{index}].{field} must be a non-empty string")
        if normalized["BLKsubsys_id"] is not None:
            require_block_local_id("subsys", normalized["BLKsubsys_id"])
        if normalized["label"] in labels:
            raise ValueError(f"duplicate system label: {normalized['label']!r}")
        labels.add(normalized["label"])
        validated.append(normalized)

    def _fit_one(spec: dict) -> dict:
        request = dict(spec)
        label = request.pop("label")
        try:
            fit = dict(fit_block(**request))
            fit.setdefault("doi", request["doi"])
            fit.setdefault("block_number", request["block_number"])
            fit.setdefault("BLKsubsys_id", request["BLKsubsys_id"])
            return {"label": label, "fit": fit}
        except Exception as exc:
            return {
                "label": label,
                "fit": {
                    "error": str(exc),
                    "doi": request["doi"],
                    "block_number": request["block_number"],
                    "BLKsubsys_id": request["BLKsubsys_id"],
                },
            }

    results, errors = [], []
    with ThreadPoolExecutor(max_workers=min(len(validated), 8)) as pool:
        futures = {
            pool.submit(copy_context().run, _fit_one, spec): spec["label"]
            for spec in validated
        }
        for future in as_completed(futures):
            try:
                result = future.result()
                results.append(result)
                if "error" in result["fit"]:
                    errors.append(f"{result['label']}: {result['fit']['error']}")
            except Exception as exc:
                errors.append(f"{futures[future]}: {exc}")

    results.sort(key=lambda result: result["label"])
    return {"n_systems": len(validated), "results": results, "errors": errors}


# ------------------------------------------------------------------
#  Low-level: compute_ideal_baseline, predict_from_rk
# ------------------------------------------------------------------

@uses_compactors(compact_compute_ideal_baseline)
def compute_ideal_baseline(
    pure_values: dict,
    property_type: str,
    n_points: int = 101,
    mixing_rule: str = "",
) -> dict:
    """Compute ideal-mixture baseline from pure component values.

    Parameters
    ----------
    pure_values : dict
        Exact component-name object: {"water": 0.891, "ethanol": 1.074}.
    property_type : str
        "viscosity" (Arrhenius) or anything else (linear).
    n_points : int
        Grid points from x=0 to x=1.
    mixing_rule : str
        "linear", "arrhenius", or "both".
    """
    _validate_named_pure_values(pure_values, context="pure_values")
    if isinstance(n_points, bool) or not isinstance(n_points, int) or n_points < 2:
        raise ValueError("n_points must be an integer >= 2; values are never coerced")

    x_grid = np.linspace(0, 1, n_points)
    return build_ideal_baseline(
        pure_values, x_grid, property_type,
        mixing_rule=mixing_rule or None,
    )


@uses_compactors(compact_predict_from_rk)
def predict_from_rk(
    coeffs: list[float],
    pure_values: dict,
    property_type: str,
    n_points: int = 101,
    mixing_rule: str = "",
) -> dict:
    """Predict mixture property using fitted RK coefficients.

    Linear rule:    Y(x) = Y_ideal(x) + Y_excess_RK(x)
    Arrhenius rule: Y(x) = Y_ideal(x) * exp(Y_excess_RK(x))
    (RK coefficients from an Arrhenius-rule fit model the excess of
    ln(Y), so the back-transform recovers physical units.)

    Parameters
    ----------
    coeffs : list[float]
        Numeric RK coefficient array: [A0, A1, ...].
    pure_values : dict
        Exact component-name object of pure values.
    property_type : str
        Property name (e.g. "viscosity", "density").
    n_points : int
        Grid points.
    mixing_rule : str
        "linear" or "arrhenius". Defaults to the canonical rule for
        *property_type* (e.g. viscosity → arrhenius).
    """
    if not isinstance(coeffs, list) or not coeffs or any(
        isinstance(value, bool) or not isinstance(value, (int, float))
        for value in coeffs
    ):
        raise TypeError("coeffs must be a non-empty array of JSON numbers")
    _validate_named_pure_values(pure_values, context="pure_values")
    if isinstance(n_points, bool) or not isinstance(n_points, int) or n_points < 2:
        raise ValueError("n_points must be an integer >= 2; values are never coerced")

    # Mixing rule has one declared parameter. It is never inferred from an
    # incorrectly populated property_type field.
    rule = (mixing_rule or "").strip().lower() or None
    ptype = (property_type or "").strip()

    x1_arr = np.linspace(0, 1, n_points)
    y_excess = eval_redlich_kister(x1_arr, coeffs)

    baseline = build_ideal_baseline(pure_values, x1_arr, ptype, mixing_rule=rule)
    if "error" in baseline:
        return baseline

    y_ideal = np.array(baseline["y_ideal"])
    if baseline["mixing_rule"] == "arrhenius":
        # Arrhenius-rule fits store the RK excess in ln-space:
        # ln(Y) = ln(Y_ideal) + y_excess  =>  Y = Y_ideal * exp(y_excess)
        y_total = y_ideal * np.exp(y_excess)
    else:
        y_total = y_ideal + y_excess

    raw = {
        "x1": x1_arr.tolist(),
        "y_ideal": y_ideal.tolist(),
        "y_excess": y_excess.tolist(),
        "y_predicted": y_total.tolist(),
        "mixing_rule": baseline["mixing_rule"],
        "rk_order": len(coeffs) - 1,
        "components": baseline["components"],
    }
    return raw


# ------------------------------------------------------------------
#  propose_fitting_plan  (validation before fitting)
# ------------------------------------------------------------------

@uses_compactors(compact_propose_fitting_plan)
def propose_fitting_plan(
    doi: str,
    block_number: str,
    BLKsubsys_id: str | None = None,
    x_vars: list[str] | None = None,
    y_props: list[str] | None = None,
    x_vars_constrained: dict | None = None,
    property_hint: str = "",
    composition_hint: str = "mole_fraction",
) -> dict:
    """Validate a fitting plan against a block before calling fit_block.

    Checks that requested columns exist, constraints are parseable,
    and returns the resolved column names and constraint values.

    Parameters
    ----------
    doi, block_number : str
        Block identifier.
    x_vars : list[str] | None
        Exact x-column names.
    y_props : list[str] | None
        Exact y-column names.
    x_vars_constrained : dict | None
        Structured constraint object.
    property_hint, composition_hint : str
        Automatic column-selection hints when x_vars / y_props are omitted.
    """
    result = _extract_and_match(
        doi, block_number, BLKsubsys_id, property_hint, composition_hint
    )
    if isinstance(result, dict):
        return result
    bd, match = result

    _x_overrides = _validate_column_list(x_vars)
    _y_overrides = _validate_column_list(y_props)
    _constraints = _validate_constraints(x_vars_constrained)
    x_col = _x_overrides[0] if _x_overrides else match.x_column
    y_col = _y_overrides[0] if _y_overrides else match.y_column

    warnings = []
    if x_col not in bd.arrays:
        warnings.append(f"x column '{x_col}' not found; available: {bd.columns}")
    if y_col not in bd.arrays:
        warnings.append(f"y column '{y_col}' not found; available: {bd.columns}")

    property_response = None
    if y_col in bd.arrays:
        try:
            property_response = inspect_property_response_contract(
                bd.metadata, y_col
            )
            if not property_response["supported"]:
                warnings.append(
                    "Selected property presentation/reference-state contract "
                    "is not supported by deterministic materialization"
                )
        except PropertyResponsePreparationError as exc:
            warnings.append(f"{exc.code}: {exc}")

    resolved_constraints = {}
    for c_col, c_spec in _constraints.items():
        if c_col not in bd.arrays:
            warnings.append(f"Constraint column '{c_col}' not found; available: {bd.columns}")
        else:
            c_val = c_spec["value"]
            c_tol = c_spec.get("tol", 0.5)
            col_data = bd.arrays[c_col]
            valid = col_data[~np.isnan(col_data)]
            nearest = float(valid[np.argmin(np.abs(valid - c_val))]) if len(valid) > 0 else None
            resolved_constraints[c_col] = {
                "value": c_val, "tol": c_tol,
                "nearest_in_data": nearest,
                "n_matching": int(np.sum(np.abs(col_data - c_val) <= c_tol)),
            }

    status = "valid" if not warnings else "warnings"
    return {
        "status": status,
        "doi": doi, "lit_num_id": bd.metadata["lit_num_id"],
        "block_number": block_number, "BLKsubsys_id": BLKsubsys_id,
        "resolved": {
            "x_column": x_col,
            "y_column": y_col,
            "constraints": resolved_constraints or None,
            "property_response": property_response,
        },
        "all_columns": bd.columns,
        "identified_x": match.x_columns,
        "identified_y": match.y_columns,
        "warnings": warnings,
        "n_rows": bd.n_rows,
    }


# ── Catalog entries ─────────────────────────────────────────────────────

@uses_compactors(compact_fit_block)
def fit_block_derived(
    doi: str,
    block_number: str,
    BLKsubsys_id: str | None = None,
    transform: str = "density_to_molar_volume",
    property_hint: str = "",
    composition_hint: str = "mole_fraction",
    x_vars: list[str] | None = None,
    y_props: list[str] | None = None,
    x_vars_constrained: dict | None = None,
    max_rk_order: int = 5,
) -> dict:
    """Fit an EXACTLY-DERIVED property from a measured mixture block (DP2).

    Data-priority ladder: prefer direct measured excess data (DP0) or the
    directly measured target property (DP1) when they exist; use this
    tool when only a convertible measured property is available (e.g.
    density measured, molar volume wanted).  Each measured point is
    transformed with an exact relation — no pure-component approximation
    is introduced — then RK-fitted like any measured curve.

    Transforms (see exact_transforms registry):
    - ``density_to_molar_volume``: Vm = (x1*M1 + x2*M2)/rho, exact.
      Molar masses come from the block's own compound formulas.
      The fitted excess IS a true excess molar volume V^E, because the
      ideal molar volume x1*V1 + x2*V2 is thermodynamically exact, with
      V1/V2 taken from the SAME block's endpoint rows at the same state.

    Parameters
    ----------
    doi, block_number : str
        Source block containing the measured property.
    transform : str
        Registered exact transform name.
    property_hint, composition_hint : str
        Column-selection hints for the source property.
    x_vars, y_props : list[str] | None
        Exact source column names.
    x_vars_constrained : dict | None
        Structured state constraints (same contract as fit_block).
    max_rk_order : int
        Max RK order (dof-capped information-criterion selection).
    """
    from ..ThermoML_core_calc_tools.mixture_nonideality_calc.exact_transforms import (
        TRANSFORMS, apply_transform,
    )
    spec = TRANSFORMS.get(transform)
    if spec is None:
        return {"error": f"Unknown transform '{transform}'. "
                         f"Available: {sorted(TRANSFORMS)}",
                         "doi": doi, "block_number": block_number,
                         "BLKsubsys_id": BLKsubsys_id}
    if transform == "kappa_s_from_rho_u":
        return {"error": (
            "kappa_s_from_rho_u needs two y-columns (density AND speed of "
            "sound) from the same state; fetch both with fit_block/"
            "inspect_block and combine manually — automatic support is "
            "single-source only."
        ), "doi": doi, "block_number": block_number,
           "BLKsubsys_id": BLKsubsys_id}

    if isinstance(max_rk_order, bool) or not isinstance(max_rk_order, int) or max_rk_order < 0:
        raise ValueError("max_rk_order must be a non-negative integer")

    hint = property_hint or spec["source_property"]
    result = _extract_and_match(
        doi, block_number, BLKsubsys_id, hint, composition_hint
    )
    if isinstance(result, dict):
        return result
    bd, match = result

    _x_overrides = _validate_column_list(x_vars)
    _y_overrides = _validate_column_list(y_props)
    x_col = _x_overrides[0] if _x_overrides else match.x_column
    y_col = _y_overrides[0] if _y_overrides else match.y_column
    for _col, _lbl in [(x_col, "x"), (y_col, "y")]:
        if _col not in bd.arrays:
            return {"error": f"Requested {_lbl} column '{_col}' not found",
                    "columns_available": bd.columns,
                    "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id}

    x_all = bd.arrays[x_col]
    y_all = bd.arrays[y_col]

    # ---- State filtering (same contract as fit_block) ----
    constraints = _validate_constraints(x_vars_constrained)
    selected_temp = None
    applied_constraints: dict = {}
    derived_state_mask: np.ndarray | None = None
    if constraints:
        row_mask = np.ones(len(x_all), dtype=bool)
        for c_col, c_spec in constraints.items():
            if c_col not in bd.arrays:
                return {"error": f"Constraint column '{c_col}' not found",
                        "columns_available": bd.columns,
                        "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id}
            c_val = c_spec["value"]
            c_tol = c_spec.get("tol", 0.5)
            row_mask &= np.abs(bd.arrays[c_col] - c_val) <= c_tol
            applied_constraints[c_col] = {"value": c_val, "tol": c_tol}
            if "temperature" in c_col.lower():
                selected_temp = c_val
        x_all, y_all = x_all[row_mask], y_all[row_mask]
        derived_state_mask = row_mask

    comp_names = _resolve_comp_names(None, bd.metadata)
    comp_names = _order_comps_by_x_column(comp_names, match)

    # ---- Composition basis gate (transform inputs need mole fraction) ----
    gate = _apply_composition_basis_gate(
        bd, x_col, x_all, comp_names, derived_state_mask,
        selected_temp=selected_temp,
    )
    if "error" in gate:
        return {**gate, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id,
                "columns_available": bd.columns}
    x_all = gate["x"]
    derived_composition_basis = gate["basis"]
    derived_composition_note = gate["note"]

    # Source properties must be absolute before applying an exact transform
    # such as rho -> Vm. Transforming a ratio/difference presentation as if
    # it were rho would be dimensionally and chemically invalid.
    response_state, response_tolerances = _canonical_state_and_tolerances(
        applied_constraints,
        fallback_temperature=selected_temp,
    )
    response_contract = inspect_property_response_contract(bd.metadata, y_col)
    if response_contract["requires_reference_materialization"]:
        for quantity, ref_field in (
            ("temperature_k", "ref_temperature_K"),
            ("pressure_kpa", "ref_pressure_kPa"),
        ):
            if response_contract.get(ref_field) is not None or response_state[quantity] is not None:
                continue
            inferred, distinct = _selected_unique_state_value(
                bd, quantity, derived_state_mask
            )
            if len(distinct) > 1:
                return {
                    "error": (
                        "STATE_REFINEMENT_REQUIRED: reference-relative source "
                        f"property has {len(distinct)} selected {quantity} values"
                    ),
                    "doi": doi,
                    "lit_num_id": bd.metadata["lit_num_id"],
                    "block_number": block_number,
                    "BLKsubsys_id": BLKsubsys_id,
                    "state_quantity": quantity,
                    "state_values": distinct,
                }
            response_state[quantity] = inferred
    try:
        response = prepare_property_response(
            metadata=bd.metadata,
            y_column=y_col,
            reported_values=y_all,
            normalized_composition=_normalized_binary_composition(
                bd.metadata, comp_names, x_all
            ),
            state=response_state,
            state_tolerances=response_tolerances,
        )
    except PropertyResponsePreparationError as exc:
        return property_response_error_result(
            exc,
            doi=doi,
            lit_num_id=bd.metadata["lit_num_id"],
            block_number=block_number,
            BLKsubsys_id=BLKsubsys_id,
        )
    y_all = response.values
    property_response = response.trace

    # ---- Exact pointwise transform on the MEASURED data ----
    mm = _molar_masses_from_metadata(bd.metadata, comp_names)
    if len(mm) < 2:
        return {"error": (
            f"Transform '{transform}' needs molar masses for both "
            f"components; block formulas resolved only {sorted(mm)} "
            f"for components {comp_names}."
        ), "doi": doi, "block_number": block_number,
           "BLKsubsys_id": BLKsubsys_id}
    M1, M2 = mm[comp_names[0]], mm[comp_names[1]]
    kw = {"x1": x_all, "M1": M1, "M2": M2}
    kw["rho" if "rho" in spec["requires"] else "vm"] = y_all
    tr = apply_transform(transform, **kw)
    if "error" in tr:
        return {**tr, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id}
    y_t = np.asarray(tr["y"], dtype=float)
    target_prop = tr["target_property"]

    x_mix, y_mix = filter_mixture_points(x_all, y_t, eps=0.02)
    if len(x_mix) < 3:
        return {"error": f"Only {len(x_mix)} mixture points after transform "
                         f"(need >= 3)", "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id}

    # ---- Endpoints from the SAME transformed measured data (no external
    # pure approximations — doctrine: measurements first) ----
    x_dict = {comp_names[0]: x_all, comp_names[1]: 1.0 - x_all}
    info = extract_pure_from_edges(x_dict, y_t, threshold=0.02)
    if comp_names[0] not in info or comp_names[1] not in info:
        return {"error": (
            "Block composition coverage is insufficient to anchor the "
            "derived property at both endpoints; cannot compute a "
            "measurement-based excess."
        ), "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id}
    d1, d0 = info[comp_names[0]], info[comp_names[1]]
    pure_values = {comp_names[0]: float(d1["value"]),
                   comp_names[1]: float(d0["value"])}
    pv_source = (
        f"block-edges of derived data ({comp_names[1]}: {d0['method']}/"
        f"{d0['quality']}, {comp_names[0]}: {d1['method']}/{d1['quality']})"
    )

    baseline = build_ideal_baseline(
        pure_values, x_mix, target_prop,
        mixing_rule=tr["target_ideal_rule"], component_order=comp_names,
    )
    if "error" in baseline:
        return {**baseline, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id}
    y_ideal = np.array(baseline["y_ideal"])
    y_excess = y_mix - y_ideal

    rk = auto_fit_redlich_kister(x_mix, y_excess, max_order=max_rk_order)
    if "error" in rk:
        return {**rk, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id}

    y_lbl = f"{target_prop}_{tr['target_units'].replace('/', '_')}_derived"
    raw = {
        "doi": doi, "lit_num_id": bd.metadata["lit_num_id"],
        "block_number": block_number, "BLKsubsys_id": BLKsubsys_id,
        "x_column": x_col, "y_column": y_lbl,
        "source_column": y_col,
        "property_response": property_response,
        "transform": transform, "relation": tr["relation"],
        "molar_masses_g_mol": {comp_names[0]: M1, comp_names[1]: M2},
        "rk_coeffs": rk["coeffs"], "rk_order": rk["selected_order"],
        "r_squared": rk["r_squared"], "rmse": rk["rmse"],
        "bic": rk.get("bic"),
        "n_mixture_points": len(x_mix), "n_total_points": bd.n_rows,
        "mixing_rule": tr["target_ideal_rule"],
        "pure_values": pure_values, "components": comp_names,
        "pure_values_source": pv_source,
        "bic_analysis": rk.get("all_orders", []),
        "classification": classify_excess(y_excess, x_mix, target_prop,
                                          rmse=rk.get("rmse")),
        "route": f"measured-derived ({transform}, exact pointwise)",
    }
    if rk.get("coeff_std_errors"):
        raw["rk_coeff_std_errors"] = rk["coeff_std_errors"]
        if rk.get("insignificant_coeffs"):
            raw["insignificant_coeffs"] = rk["insignificant_coeffs"]
    if rk.get("sparse_data_note"):
        raw["fit_note"] = rk["sparse_data_note"]
    if derived_composition_basis not in ("mole_fraction", "unknown"):
        raw["composition_basis"] = derived_composition_basis
    if derived_composition_note:
        raw["composition_conversion"] = derived_composition_note
    if selected_temp is not None:
        raw["selected_temperature_K"] = selected_temp
    if applied_constraints:
        raw["applied_constraints"] = applied_constraints

    output_files = _save_fit_outputs(
        doi, block_number, x_mix, y_mix, y_ideal, y_excess, rk,
                    BLKsubsys_id=BLKsubsys_id,
        mixing_rule=tr["target_ideal_rule"], components=comp_names,
        y_label=y_lbl, temperature_K=selected_temp,
        pure_values=pure_values, property_type=target_prop,
        pure_values_source=pv_source,
        block_metadata=bd.metadata,
    )
    if output_files:
        raw["output_files"] = output_files
    return raw


TOOL_ENTRIES = [
    ToolEntry(
        "fit_block", fit_block,
        group="fitting",
        skip_subagent=True,
    ),
    ToolEntry(
        "fit_block_derived", fit_block_derived,
        group="fitting",
        skip_subagent=True,
    ),
    ToolEntry(
        "fit_multi_system", fit_multi_system,
        group="fitting",
        skip_subagent=True,
    ),
    ToolEntry(
        "compute_ideal_baseline", compute_ideal_baseline,
        group="fitting",
        skip_subagent=True,
    ),
    ToolEntry(
        "predict_from_rk", predict_from_rk,
        group="fitting",
        skip_subagent=True,
    ),
    ToolEntry(
        "propose_fitting_plan", propose_fitting_plan,
        group="fitting",
        skip_subagent=True,
    ),
]
