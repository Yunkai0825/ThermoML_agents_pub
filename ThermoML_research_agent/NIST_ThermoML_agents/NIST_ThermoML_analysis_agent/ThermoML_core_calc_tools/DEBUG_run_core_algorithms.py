"""
DEBUG_run_core_algorithms.py
============================
Generate diagnostic CSVs from the raw ThermoML database, then run the
core algorithms (ideal_baseline, Redlich-Kister fitter) and produce
diagnostic plots under the shared _output/Analysis/CoreCalcDiagnostics folder.

Tests:
  1. Ethanol + Water  — density at 298.15 K  (single-T, linear mixing rule)
  2. Toluene + 2-Hexanol — viscosity at 298.15 & 308.15 K  (multi-T, Arrhenius rule)
  3. Ethyl methanoate + Decane — density at 291/298/308 K  (multi-T, linear rule)
  4. Toluene + 2-Hexanol — viscosity DUAL baseline (Arrhenius vs linear side-by-side)
  5. Multi-property fitting from a single block (RK on both baselines)  6. Synthetic TERNARY system — verify N-component ideal baseline
Usage:
    cd ThermoML_research_agent
    python NIST_ThermoML_agents/NIST_ThermoML_analysis_agent/ThermoML_core_calc_tools/DEBUG_run_core_algorithms.py
"""

from __future__ import annotations

import csv
import io
import os
import sys
import traceback

import numpy as np

# Fix Windows console encoding for Unicode output
if sys.stdout.encoding and sys.stdout.encoding.lower().startswith("cp"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── path setup ──────────────────────────────────────────────────
_THIS = os.path.dirname(os.path.abspath(__file__))
_WORKSPACE = os.path.abspath(os.path.join(_THIS, "..", "..", ".."))
if _WORKSPACE not in sys.path:
    sys.path.insert(0, _WORKSPACE)
_REPO_ROOT = os.path.abspath(os.path.join(_WORKSPACE, ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

# Block extractor (reads raw DB) — module name starts with digit, use spec loader
_SEARCH_TOOLS = os.path.join(_WORKSPACE, "card_db_search_tools", "basic_search_tools")
if _SEARCH_TOOLS not in sys.path:
    sys.path.insert(0, _SEARCH_TOOLS)

import importlib.util as _ilu
_spec = _ilu.spec_from_file_location(
    "block_data_extractor",
    os.path.join(_SEARCH_TOOLS, "11_block_data_extractor.py"),
)
_ext = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_ext)

# Core algorithms
from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.mixture_nonideality_calc.ideal_baseline import (
    build_ideal_baseline,
    compute_excess_property,
    default_mixing_rule,
    extract_pure_from_edges,
    pure_values_from_edges,
)
from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.Redlich_Kister_block_fitting.rk_fitter import (
    auto_fit_redlich_kister,
    eval_redlich_kister,
    fit_redlich_kister,
    fit_multi_property,
)
from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.output_helpers.csv_export import (
    save_fit_csv,
    save_excess_csv,
    save_baseline_csv,
)
from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.output_helpers.topology_repr import (
    extract_topology_points,
    topology_to_csv,
)
from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.topology_helpers.convex_hull_construction import (
    compute_convex_hull,
    select_hull_edge_points,
)

# matplotlib — use non-interactive backend
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from pathlib import Path

# ── output directories ──────────────────────────────────────────
_DIAG_ROOT = Path(_REPO_ROOT) / "_output" / "Analysis" / "CoreCalcDiagnostics"
BASELINE_DEBUG_IN  = os.fspath(_DIAG_ROOT / "baseline_input")
BASELINE_DEBUG_OUT = os.fspath(_DIAG_ROOT / "baseline_plots")
RK_DEBUG_IN        = os.fspath(_DIAG_ROOT / "rk_input")
RK_DEBUG_OUT       = os.fspath(_DIAG_ROOT / "rk_plots")
CSV_OUT            = os.fspath(_DIAG_ROOT / "csv")
TOPO_OUT           = os.fspath(_DIAG_ROOT / "topology")

for d in [BASELINE_DEBUG_IN, BASELINE_DEBUG_OUT, RK_DEBUG_IN, RK_DEBUG_OUT, CSV_OUT, TOPO_OUT]:
    os.makedirs(d, exist_ok=True)


# ═══════════════════════════════════════════════════════════════
#  Helpers
# ═══════════════════════════════════════════════════════════════

def _parse_csv(csv_text: str):
    """csv_text → (header, rows_as_dicts)"""
    reader = csv.DictReader(io.StringIO(csv_text))
    return list(reader.fieldnames or []), list(reader)


def _col_array(rows, col):
    """Extract a column as float array (NaN for blanks)."""
    vals = []
    for r in rows:
        raw = r.get(col, "")
        try:
            vals.append(float(raw))
        except (ValueError, TypeError):
            vals.append(np.nan)
    return np.array(vals)


def _save_csv(path, header, rows):
    """Write rows (list of dicts) to CSV."""
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()
        w.writerows(rows)
    print(f"  saved → {os.path.relpath(path, _WORKSPACE)}")


def _filter_T(rows, t_col, target_T, tol=0.5):
    """Filter rows to a single temperature."""
    return [r for r in rows if abs(float(r[t_col]) - target_T) < tol]


# ─── condition-variable helpers ────────────────────────────────────
#  Detect all independent condition dimensions (T, P, …) that vary
#  and group rows by their unique combinations.

_CONDITION_COLS = ["temperature_k", "pressure_kpa"]  # known condition columns


def _identify_varying_conditions(header, rows, x_col, y_col):
    """Return list of condition columns that have >1 unique value.

    Only considers columns that are NOT the composition or property column.
    """
    vary = []
    for col in _CONDITION_COLS:
        if col not in header or col == x_col or col == y_col:
            continue
        vals = {float(r[col]) for r in rows if r.get(col)}
        if len(vals) > 1:
            vary.append(col)
    return vary


def _unique_conditions(rows, cond_cols):
    """Return sorted list of unique condition tuples.

    Each tuple is (val_col0, val_col1, …) matching *cond_cols* order.
    If cond_cols is empty, returns a single (None,) tuple.
    """
    if not cond_cols:
        return [(None,)]
    combos = set()
    for r in rows:
        key = tuple(float(r[c]) for c in cond_cols)
        combos.add(key)
    return sorted(combos)


def _filter_conditions(rows, cond_cols, cond_values, tol=0.5):
    """Filter rows to match a specific condition tuple (within tolerance)."""
    if cond_values == (None,):
        return rows
    out = []
    for r in rows:
        match = True
        for col, target in zip(cond_cols, cond_values):
            if abs(float(r[col]) - target) > tol:
                match = False
                break
        if match:
            out.append(r)
    return out


def _cond_label(cond_cols, cond_values):
    """Human-readable label for a condition tuple, e.g. 'T=298.15 K, P=101.325 kPa'."""
    if cond_values == (None,):
        return ""
    parts = []
    for col, val in zip(cond_cols, cond_values):
        if "temperature" in col:
            parts.append(f"T={val} K")
        elif "pressure" in col:
            parts.append(f"P={val} kPa")
        else:
            parts.append(f"{col}={val}")
    return ", ".join(parts)


def _cond_file_tag(cond_cols, cond_values):
    """File-safe tag from condition values, e.g. '_298.15K_101.325kPa'."""
    if cond_values == (None,):
        return ""
    parts = []
    for col, val in zip(cond_cols, cond_values):
        if "temperature" in col:
            parts.append(f"{val}K")
        elif "pressure" in col:
            parts.append(f"{val}kPa")
        else:
            parts.append(f"{val}")
    return "_" + "_".join(parts)


def _save_topo_and_csv(tag, x, y_excess, y_fitted, residuals,
                       rk_coeffs, rk_order, r_squared, rmse,
                       x_label="x1", y_label="Y_excess", metadata=None):
    """Save CSV fit data + topology representation for a test."""
    # CSV: per-point data + summary
    csv_path = os.path.join(CSV_OUT, f"{tag}_fit.csv")
    save_fit_csv(csv_path, x, y_excess, y_fitted, residuals,
                 rk_coeffs, rk_order, r_squared, rmse,
                 x_label=x_label, y_label=y_label, metadata=metadata)
    print(f"  csv  → {os.path.relpath(csv_path, _WORKSPACE)}")

    # CSV: excess data
    excess_csv = os.path.join(CSV_OUT, f"{tag}_excess.csv")
    save_excess_csv(excess_csv, x, y_excess + y_fitted, np.zeros_like(y_excess) + y_fitted,
                    y_excess, x_label=x_label, y_label=y_label)
    print(f"  csv  → {os.path.relpath(excess_csv, _WORKSPACE)}")

    # Topology: compact curve from the fitted RK polynomial
    x_smooth = np.linspace(0.001, 0.999, 200)
    y_smooth = eval_redlich_kister(x_smooth, rk_coeffs)

    # Convex hull diagnostics on the smooth curve
    hull_info = compute_convex_hull(x_smooth, y_smooth)
    if "error" not in hull_info:
        print(f"  hull → {hull_info['n_hull_points']} vertices, "
              f"area={hull_info['area']:.4f}")

    topo = extract_topology_points(x_smooth, y_smooth, n=20)
    topo_path = os.path.join(TOPO_OUT, f"{tag}_topology.csv")
    topology_to_csv(topo_path, topo, x_label=x_label, y_label=y_label)
    print(f"  topo → {os.path.relpath(topo_path, _WORKSPACE)} "
          f"({topo['n_points']} pts from {topo['n_source_points']}, "
          f"hull_area={topo.get('hull_area', 0.0):.4f})")
    return topo


def _unique_T(rows, t_col):
    """Return sorted unique temperatures."""
    return sorted({float(r[t_col]) for r in rows if r.get(t_col)})


# ═══════════════════════════════════════════════════════════════
#  1. EXTRACT DEBUG INPUT CSVs FROM RAW DB
# ═══════════════════════════════════════════════════════════════

def extract_debug_inputs():
    """Pull three test datasets from PCS_INDIV.db and save as CSV."""
    print("\n" + "=" * 70)
    print("  STEP 1: Extracting debug-input CSVs from ThermoML database")
    print("=" * 70)

    datasets = {
        "ethanol_water_density": {
            "doi": "10.1016/j.fluid.2004.11.019",
            "block": "PROPblock_2",
            "description": "Ethanol + Water density at 298.15 K",
        },
        "toluene_2hexanol_viscosity": {
            "doi": "10.1016/j.fluid.2007.01.001",
            "block": "PROPblock_14",
            "description": "Toluene + 2-Hexanol viscosity at 298.15 & 308.15 K",
        },
        "ethyl_methanoate_decane_density": {
            "doi": "10.1016/j.fluid.2009.12.003",
            "block": "PROPblock_8",
            "description": "Ethyl methanoate + Decane density at 291/298/308 K",
        },
        # ── Additional binary systems (full x=0→1 coverage) ──
        "dmc_methanol_density": {
            "doi": "10.1016/j.jct.2019.02.011",
            "block": "PROPblock_5",
            "description": "Dimethyl carbonate + Methanol density (multi-T)",
        },
        "cyclohexane_hexadecane_viscosity": {
            "doi": "10.1021/je9000262",
            "block": "PROPblock_3",
            "description": "Cyclohexane + Hexadecane viscosity (multi-T, x=0→1)",
        },
        "toluene_mtbe_density": {
            "doi": "10.1007/s10765-007-0223-x",
            "block": "PROPblock_16",
            "description": "Toluene + MTBE density (multi-T, x=0→1)",
        },
        # ── New binary systems with full composition coverage ──
        "methanol_acetone_density": {
            "doi": "10.1016/j.fluid.2018.10.024",
            "block": "PROPblock_10",
            "description": "Methanol + Acetone density (x=0→1, 298-318 K)",
        },
        "acetone_chloroform_density": {
            "doi": "10.1016/j.fluid.2018.10.024",
            "block": "PROPblock_16",
            "description": "Acetone + Chloroform density (x=0→1, 298-318 K)",
        },
        "methanol_chlorobenzene_density": {
            "doi": "10.1007/s10765-008-0444-7",
            "block": "PROPblock_8",
            "description": "Methanol + Chlorobenzene density (x=0→1, 293-313 K)",
        },
        "methanol_chlorobenzene_viscosity": {
            "doi": "10.1007/s10765-008-0444-7",
            "block": "PROPblock_7",
            "description": "Methanol + Chlorobenzene viscosity (x=0→1, 293-313 K)",
        },
        "aniline_1propanol_density": {
            "doi": "10.1007/s10765-007-0204-0",
            "block": "PROPblock_6",
            "description": "Aniline + 1-Propanol density (x=0→1, 293-303 K)",
        },
    }

    extracted = {}
    for name, spec in datasets.items():
        print(f"\n  [{name}] — {spec['description']}")
        res = _ext.extract_block_csv(spec["doi"], spec["block"])
        if res.get("error"):
            print(f"    ERROR: {res['error']}")
            continue

        header, rows = _parse_csv(res["csv_text"])
        # Save to both DEBUG_input folders
        for out_dir in [BASELINE_DEBUG_IN, RK_DEBUG_IN]:
            _save_csv(os.path.join(out_dir, f"{name}.csv"), header, rows)

        extracted[name] = {
            "header": header,
            "rows": rows,
            "metadata": res.get("metadata", {}),
        }
        print(f"    columns: {header}")
        print(f"    n_rows:  {len(rows)}")
        temps = _unique_T(rows, "temperature_k") if "temperature_k" in header else []
        print(f"    T (K):   {temps}")

    return extracted


# ═══════════════════════════════════════════════════════════════
#  2. TEST IDEAL BASELINE
# ═══════════════════════════════════════════════════════════════

def _detect_comp_col(header):
    """Find the mole-fraction column and extract the component name."""
    for col in header:
        if col.startswith("mole_fraction_<") and col.endswith(">"):
            comp_name = col[len("mole_fraction_<"):-1]
            return col, comp_name
    return None, None


def _infer_other_component(comp_in_col, known_compounds):
    """Return the other component name in a binary (the one NOT in the column)."""
    others = [c for c in known_compounds if c.lower() != comp_in_col.lower()]
    return others[0] if others else f"other"


def test_ethanol_water_baseline(data):
    """Ethanol-Water density at 298.15 K — linear mixing rule.
    Uses edge extraction for pure-component values."""
    print("\n" + "=" * 70)
    print("  TEST 2a: Ideal baseline — Ethanol-Water density (linear, edge extraction)")
    print("=" * 70)

    rows = data["rows"]
    header = data["header"]
    y_col = "mass_density_kg_m3"

    # Auto-detect the composition column and component name
    x_col, comp_in_col = _detect_comp_col(header)
    assert x_col is not None, f"No mole_fraction column found in {header}"
    other_comp = _infer_other_component(comp_in_col, ["ethanol", "water"])
    print(f"  composition column: {x_col}  →  x({comp_in_col})")
    print(f"  other component:    {other_comp}")

    x = _col_array(rows, x_col)   # x of comp_in_col
    y = _col_array(rows, y_col)

    # Edge extraction: build composition dict & extract pure values
    x_dict = {comp_in_col: x, other_comp: 1.0 - x}
    edge_info = extract_pure_from_edges(x_dict, y, threshold=0.02)
    for comp, info in edge_info.items():
        print(f"  pure {comp}: {info['value']:.2f} kg/m³  "
              f"(max_x={info['max_x']:.4f}, n_near_pure={info['n_near_pure']})")
    pure_values = {comp: info["value"] for comp, info in edge_info.items()}
    assert len(pure_values) == 2, f"Expected 2 pure values, got {pure_values}"

    # Build ideal baseline — use dict x_grid (unambiguous component mapping)
    baseline = build_ideal_baseline(pure_values, {comp_in_col: x}, "density")
    assert "error" not in baseline, f"baseline error: {baseline}"
    print(f"  mixing_rule: {baseline['mixing_rule']}")
    assert baseline["mixing_rule"] == "linear"

    # Compute excess density
    excess = compute_excess_property({comp_in_col: x}, y, pure_values, "density")
    assert "error" not in excess, f"excess error: {excess}"
    print(f"  n_points:    {excess['n_points']}")
    y_exc = np.array(excess["y_excess"])
    print(f"  max |ΔρE|:   {np.max(np.abs(y_exc)):.4f} kg/m³")

    # Plot: experimental, ideal baseline, and excess
    y_ideal = np.array(baseline["y_ideal"])
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(x, y, "ko-", ms=4, label="Experimental")
    ax1.plot(x, y_ideal, "r--", lw=2, label="Ideal (linear)")
    ax1.set_xlabel(f"x({comp_in_col})")
    ax1.set_ylabel("Density (kg/m³)")
    ax1.set_title(f"{other_comp.title()} + {comp_in_col.title()} density, 298.15 K")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(x, y_exc, "bs-", ms=4)
    ax2.axhline(0, color="gray", ls="--", lw=0.8)
    ax2.set_xlabel(f"x({comp_in_col})")
    ax2.set_ylabel("Excess density (kg/m³)")
    ax2.set_title("ρᴱ = ρ_exp − ρ_ideal")
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    out = os.path.join(BASELINE_DEBUG_OUT, "ethanol_water_density_baseline.png")
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"  plot → {os.path.relpath(out, _WORKSPACE)}")

    # ── CSV: baseline data ──
    bl_csv = os.path.join(CSV_OUT, "ethanol_water_density_baseline.csv")
    save_baseline_csv(bl_csv, x, y, y_ideal,
                      x_label=f"x({comp_in_col})", y_label="density_kg_m3")
    print(f"  csv  → {os.path.relpath(bl_csv, _WORKSPACE)}")
    ex_csv = os.path.join(CSV_OUT, "ethanol_water_density_excess.csv")
    save_excess_csv(ex_csv, x, y, y_ideal, y_exc,
                    x_label=f"x({comp_in_col})", y_label="density_kg_m3")
    print(f"  csv  → {os.path.relpath(ex_csv, _WORKSPACE)}")

    return {"x": x, "y_excess": y_exc, "comp_in_col": comp_in_col,
            "other_comp": other_comp, "pure_values": pure_values}


def test_toluene_hexanol_baseline(data):
    """Toluene + 2-Hexanol viscosity — Arrhenius mixing rule (per T).
    Uses edge extraction for pure-component values."""
    print("\n" + "=" * 70)
    print("  TEST 2b: Ideal baseline — Toluene + 2-Hexanol viscosity (Arrhenius, edge extraction)")
    print("=" * 70)

    rows = data["rows"]
    header = data["header"]
    y_col = "viscosity_pa_s"
    x_col, comp_in_col = _detect_comp_col(header)
    assert x_col is not None
    other_comp = _infer_other_component(comp_in_col, ["toluene", "2-hexanol"])
    print(f"  x column: {x_col} → x({comp_in_col}), other={other_comp}")
    temps = _unique_T(rows, "temperature_k")
    print(f"  temperatures: {temps}")

    fig, axes = plt.subplots(1, len(temps), figsize=(6 * len(temps), 5))
    if len(temps) == 1:
        axes = [axes]

    all_excess = {}
    for i, T in enumerate(temps):
        sub = _filter_T(rows, "temperature_k", T)
        x = _col_array(sub, x_col)
        y = _col_array(sub, y_col)

        # Sort by x
        order = np.argsort(x)
        x, y = x[order], y[order]

        # Edge extraction
        x_dict = {comp_in_col: x, other_comp: 1.0 - x}
        pure_values = pure_values_from_edges(x_dict, y, threshold=0.02)
        print(f"  T={T} K: η({comp_in_col})={pure_values[comp_in_col]:.6f}, "
              f"η({other_comp})={pure_values[other_comp]:.6f} Pa·s")

        baseline = build_ideal_baseline(pure_values, {comp_in_col: x}, "viscosity")
        assert "error" not in baseline, f"baseline error: {baseline}"
        assert baseline["mixing_rule"] == "arrhenius"

        excess = compute_excess_property({comp_in_col: x}, y, pure_values, "viscosity")
        assert "error" not in excess
        y_exc = np.array(excess["y_excess"])
        all_excess[T] = {"x": x, "y_excess": y_exc, "pure_values": pure_values}

        # Plot
        ax = axes[i]
        ax.plot(x, y * 1000, "ko-", ms=4, label="Experimental")
        y_ideal = np.array(baseline["y_ideal"])
        ax.plot(x, y_ideal * 1000, "r--", lw=2, label="Ideal (Arrhenius)")
        ax.set_xlabel(f"x({comp_in_col})")
        ax.set_ylabel("η (mPa·s)")
        ax.set_title(f"T = {T} K")
        ax.legend()
        ax.grid(True, alpha=0.3)

    fig.suptitle("Toluene + 2-Hexanol viscosity — Arrhenius baseline", y=1.02)
    fig.tight_layout()
    out = os.path.join(BASELINE_DEBUG_OUT, "toluene_2hexanol_viscosity_baseline.png")
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot → {os.path.relpath(out, _WORKSPACE)}")

    return all_excess


def test_ethyl_methanoate_baseline(data):
    """Ethyl methanoate + Decane density — linear, 3 temperatures.
    Uses edge extraction for pure-component values."""
    print("\n" + "=" * 70)
    print("  TEST 2c: Ideal baseline — Ethyl methanoate + Decane density (multi-T, edge extraction)")
    print("=" * 70)

    rows = data["rows"]
    header = data["header"]
    y_col = "mass_density_kg_m3"
    x_col, comp_in_col = _detect_comp_col(header)
    assert x_col is not None
    other_comp = _infer_other_component(comp_in_col, ["ethyl methanoate", "decane"])
    print(f"  x column: {x_col} → x({comp_in_col}), other={other_comp}")
    temps = _unique_T(rows, "temperature_k")
    print(f"  temperatures: {temps}")

    fig, axes = plt.subplots(1, len(temps), figsize=(6 * len(temps), 5))
    if len(temps) == 1:
        axes = [axes]

    all_excess = {}
    for i, T in enumerate(temps):
        sub = _filter_T(rows, "temperature_k", T)
        x = _col_array(sub, x_col)
        y = _col_array(sub, y_col)

        order = np.argsort(x)
        x, y = x[order], y[order]

        # Edge extraction
        x_dict = {comp_in_col: x, other_comp: 1.0 - x}
        pure_values = pure_values_from_edges(x_dict, y, threshold=0.02)
        v_a = pure_values[comp_in_col]
        v_b = pure_values[other_comp]
        print(f"  T={T} K: ρ({comp_in_col})={v_a:.2f}, ρ({other_comp})={v_b:.2f} kg/m³")

        baseline = build_ideal_baseline(pure_values, {comp_in_col: x}, "density")
        assert "error" not in baseline

        excess = compute_excess_property({comp_in_col: x}, y, pure_values, "density")
        assert "error" not in excess
        y_exc = np.array(excess["y_excess"])
        all_excess[T] = {"x": x, "y_excess": y_exc, "pure_values": pure_values}

        ax = axes[i]
        ax.plot(x, y, "ko-", ms=4, label="Experimental")
        y_ideal = np.array(baseline["y_ideal"])
        ax.plot(x, y_ideal, "r--", lw=2, label="Ideal (linear)")
        ax.set_xlabel(f"x({comp_in_col})")
        ax.set_ylabel("Density (kg/m³)")
        ax.set_title(f"T = {T} K")
        ax.legend()
        ax.grid(True, alpha=0.3)

    fig.suptitle("Ethyl methanoate + Decane — density baselines", y=1.02)
    fig.tight_layout()
    out = os.path.join(BASELINE_DEBUG_OUT, "ethyl_methanoate_decane_density_baseline.png")
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot → {os.path.relpath(out, _WORKSPACE)}")

    return all_excess


# ═══════════════════════════════════════════════════════════════
#  3. TEST RK FITTER
# ═══════════════════════════════════════════════════════════════

def _filter_mixture(x, y, eps=0.02):
    """Remove pure endpoints — eps matches edge-detection threshold."""
    mask = (x > eps) & (x < 1 - eps) & ~np.isnan(x) & ~np.isnan(y)
    return x[mask], y[mask]


def test_rk_ethanol_water(excess_data):
    """RK fit for ethanol-water excess density."""
    print("\n" + "=" * 70)
    print("  TEST 3a: Redlich-Kister — Ethanol-Water excess density")
    print("=" * 70)

    x = excess_data["x"]
    y_exc = excess_data["y_excess"]
    comp_label = excess_data.get("comp_in_col", "component_1")

    x_mix, y_mix = _filter_mixture(x, y_exc)
    print(f"  mixture points (excluding endpoints): {len(x_mix)}")

    # Auto-fit with BIC selection
    result = auto_fit_redlich_kister(x_mix, y_mix, max_order=5)
    assert "error" not in result, f"RK error: {result}"

    print(f"  BIC-selected order: {result['selected_order']}")
    print(f"  coefficients: {[round(c, 4) for c in result['coeffs']]}")
    print(f"  R²:   {result['r_squared']:.6f}")
    print(f"  RMSE: {result['rmse']:.6f}")
    print(f"  BIC comparison:")
    for o in result["all_orders"]:
        marker = " <<< best" if o["order"] == result["selected_order"] else ""
        print(f"    order={o['order']}  BIC={o['bic']:8.2f}  R²={o['r_squared']:.6f}  RMSE={o['rmse']:.6f}{marker}")

    # Also do a fixed-order fit at order 3 for comparison
    fixed = fit_redlich_kister(x_mix, y_mix, max_order=3)

    # Plot: data + auto-fit + order-3 fit
    x_smooth = np.linspace(0.001, 0.999, 200)
    y_auto = eval_redlich_kister(x_smooth, result["coeffs"])
    y_fix3 = eval_redlich_kister(x_smooth, fixed["coeffs"])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    ax1.plot(x_mix, y_mix, "ko", ms=5, label="Data (ρᴱ)")
    ax1.plot(x_smooth, y_auto, "r-", lw=2,
             label=f"RK auto (n={result['selected_order']}, R²={result['r_squared']:.5f})")
    ax1.plot(x_smooth, y_fix3, "b--", lw=1.5,
             label=f"RK n=3 (R²={fixed['r_squared']:.5f})")
    ax1.axhline(0, color="gray", ls=":", lw=0.8)
    ax1.set_xlabel(f"x({comp_label})")
    ax1.set_ylabel("ρᴱ (kg/m³)")
    ax1.set_title("Ethanol + Water — RK fit of excess density")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Residual plot
    y_fitted = np.array(result["y_fitted"])
    resid = np.array(result["residuals"])
    ax2.stem(x_mix, resid, linefmt="b-", markerfmt="bo", basefmt="k-")
    ax2.axhline(0, color="gray", ls="--", lw=0.8)
    ax2.set_xlabel(f"x({comp_label})")
    ax2.set_ylabel("Residual (kg/m³)")
    ax2.set_title(f"Residuals — order {result['selected_order']}")
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    out = os.path.join(RK_DEBUG_OUT, "ethanol_water_RK_fit.png")
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"  plot → {os.path.relpath(out, _WORKSPACE)}")

    # ── CSV + topology output ──
    _save_topo_and_csv(
        "ethanol_water_density", x_mix, y_mix,
        np.array(result["y_fitted"]), np.array(result["residuals"]),
        result["coeffs"], result["selected_order"],
        result["r_squared"], result["rmse"],
        x_label=f"x({comp_label})", y_label="rho_excess_kg_m3",
        metadata={"system": "Ethanol + Water", "T_K": 298.15,
                  "property": "density", "mixing_rule": "linear"},
    )

    return result


def test_rk_toluene_hexanol(excess_by_T):
    """RK fit for toluene + 2-hexanol viscosity excess at each T."""
    print("\n" + "=" * 70)
    print("  TEST 3b: Redlich-Kister — Toluene + 2-Hexanol excess viscosity (per T)")
    print("=" * 70)

    temps = sorted(excess_by_T.keys())
    fig, axes = plt.subplots(1, len(temps), figsize=(6.5 * len(temps), 5))
    if len(temps) == 1:
        axes = [axes]

    results_by_T = {}
    for i, T in enumerate(temps):
        ed = excess_by_T[T]
        x, y_exc = _filter_mixture(ed["x"], ed["y_excess"])
        print(f"\n  T={T} K — {len(x)} mixture points")

        res = auto_fit_redlich_kister(x, y_exc, max_order=4)
        if "error" in res:
            print(f"    ERROR: {res['error']}")
            continue

        results_by_T[T] = res
        print(f"    order={res['selected_order']}  coeffs={[round(c,6) for c in res['coeffs']]}")
        print(f"    R²={res['r_squared']:.6f}  RMSE={res['rmse']:.8f}")

        x_smooth = np.linspace(0.001, 0.999, 200)
        y_smooth = eval_redlich_kister(x_smooth, res["coeffs"])

        ax = axes[i]
        ax.plot(x, y_exc, "ko", ms=5, label="Data")
        ax.plot(x_smooth, y_smooth, "r-", lw=2,
                label=f"RK n={res['selected_order']}")
        ax.axhline(0, color="gray", ls=":", lw=0.8)
        ax.set_xlabel("x(toluene)")
        ax.set_ylabel("ln(η) excess")
        ax.set_title(f"T = {T} K  (R²={res['r_squared']:.4f})")
        ax.legend()
        ax.grid(True, alpha=0.3)

    fig.suptitle("Toluene + 2-Hexanol — RK fits of excess ln(viscosity)", y=1.02)
    fig.tight_layout()
    out = os.path.join(RK_DEBUG_OUT, "toluene_2hexanol_RK_fits.png")
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot → {os.path.relpath(out, _WORKSPACE)}")

    # Coefficient-vs-T summary plot
    if len(results_by_T) > 1:
        fig2, ax = plt.subplots(figsize=(7, 5))
        max_n = max(r["selected_order"] for r in results_by_T.values())
        for k in range(max_n + 1):
            vals = []
            for T in temps:
                if T in results_by_T:
                    coeffs = results_by_T[T]["coeffs"]
                    vals.append(coeffs[k] if k < len(coeffs) else 0.0)
                else:
                    vals.append(np.nan)
            ax.plot(temps, vals, "o-", ms=6, label=f"A{k}")
        ax.set_xlabel("Temperature (K)")
        ax.set_ylabel("RK coefficient")
        ax.set_title("RK coefficients vs. Temperature")
        ax.legend()
        ax.grid(True, alpha=0.3)
        fig2.tight_layout()
        out2 = os.path.join(RK_DEBUG_OUT, "toluene_2hexanol_RK_coeffs_vs_T.png")
        fig2.savefig(out2, dpi=150)
        plt.close(fig2)
        print(f"  coeff-vs-T plot → {os.path.relpath(out2, _WORKSPACE)}")

    # ── CSV + topology per temperature ──
    for T, res in results_by_T.items():
        ed = excess_by_T[T]
        x_m, y_m = _filter_mixture(ed["x"], ed["y_excess"])
        _save_topo_and_csv(
            f"toluene_2hexanol_viscosity_{T}K", x_m, y_m,
            np.array(res["y_fitted"]), np.array(res["residuals"]),
            res["coeffs"], res["selected_order"],
            res["r_squared"], res["rmse"],
            x_label="x(toluene)", y_label="ln_eta_excess",
            metadata={"system": "Toluene + 2-Hexanol", "T_K": T,
                      "property": "viscosity", "mixing_rule": "arrhenius"},
        )

    return results_by_T


def test_rk_ethyl_methanoate(excess_by_T):
    """RK fit for ethyl methanoate + decane density at 3 temperatures."""
    print("\n" + "=" * 70)
    print("  TEST 3c: Redlich-Kister — Ethyl methanoate + Decane (multi-T density)")
    print("=" * 70)

    temps = sorted(excess_by_T.keys())
    fig, axes = plt.subplots(1, len(temps), figsize=(6 * len(temps), 5))
    if len(temps) == 1:
        axes = [axes]

    results_by_T = {}
    for i, T in enumerate(temps):
        ed = excess_by_T[T]
        x, y_exc = _filter_mixture(ed["x"], ed["y_excess"])
        print(f"\n  T={T} K — {len(x)} mixture points")

        res = auto_fit_redlich_kister(x, y_exc, max_order=4)
        if "error" in res:
            print(f"    ERROR: {res['error']}")
            continue

        results_by_T[T] = res
        print(f"    order={res['selected_order']}  coeffs={[round(c,4) for c in res['coeffs']]}")
        print(f"    R²={res['r_squared']:.6f}  RMSE={res['rmse']:.4f}")

        x_smooth = np.linspace(0.001, 0.999, 200)
        y_smooth = eval_redlich_kister(x_smooth, res["coeffs"])

        ax = axes[i]
        ax.plot(x, y_exc, "ko", ms=5, label="Data")
        ax.plot(x_smooth, y_smooth, "r-", lw=2,
                label=f"RK n={res['selected_order']}")
        ax.axhline(0, color="gray", ls=":", lw=0.8)
        ax.set_xlabel("x(ethyl methanoate)")
        ax.set_ylabel("ρᴱ (kg/m³)")
        ax.set_title(f"T = {T} K  (R²={res['r_squared']:.4f})")
        ax.legend()
        ax.grid(True, alpha=0.3)

    fig.suptitle("Ethyl methanoate + Decane — RK fits of excess density", y=1.02)
    fig.tight_layout()
    out = os.path.join(RK_DEBUG_OUT, "ethyl_methanoate_decane_RK_fits.png")
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot → {os.path.relpath(out, _WORKSPACE)}")

    # Coefficient-vs-T
    if len(results_by_T) > 1:
        fig2, ax = plt.subplots(figsize=(7, 5))
        max_n = max(r["selected_order"] for r in results_by_T.values())
        for k in range(max_n + 1):
            vals = [results_by_T[T]["coeffs"][k]
                    if T in results_by_T and k < len(results_by_T[T]["coeffs"])
                    else np.nan
                    for T in temps]
            ax.plot(temps, vals, "o-", ms=6, label=f"A{k}")
        ax.set_xlabel("Temperature (K)")
        ax.set_ylabel("RK coefficient (kg/m³)")
        ax.set_title("RK coefficients vs. Temperature — Ethyl methanoate + Decane")
        ax.legend()
        ax.grid(True, alpha=0.3)
        fig2.tight_layout()
        out2 = os.path.join(RK_DEBUG_OUT, "ethyl_methanoate_decane_RK_coeffs_vs_T.png")
        fig2.savefig(out2, dpi=150)
        plt.close(fig2)
        print(f"  coeff-vs-T plot → {os.path.relpath(out2, _WORKSPACE)}")

    # ── CSV + topology per temperature ──
    for T, res in results_by_T.items():
        ed = excess_by_T[T]
        x_m, y_m = _filter_mixture(ed["x"], ed["y_excess"])
        _save_topo_and_csv(
            f"ethyl_methanoate_decane_density_{T}K", x_m, y_m,
            np.array(res["y_fitted"]), np.array(res["residuals"]),
            res["coeffs"], res["selected_order"],
            res["r_squared"], res["rmse"],
            x_label="x(ethyl_methanoate)", y_label="rho_excess_kg_m3",
            metadata={"system": "Ethyl methanoate + Decane", "T_K": T,
                      "property": "density", "mixing_rule": "linear"},
        )

    return results_by_T


# ═══════════════════════════════════════════════════════════════
#  4. BIC ORDER-SELECTION DIAGNOSTIC
# ═══════════════════════════════════════════════════════════════

def plot_bic_diagnostic(rk_result, label, filename):
    """Plot BIC vs order for a single RK fit."""
    orders_info = rk_result.get("all_orders", [])
    if len(orders_info) < 2:
        return

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    orders = [o["order"] for o in orders_info]
    bics = [o["bic"] for o in orders_info]
    r2s = [o["r_squared"] for o in orders_info]

    best = rk_result["selected_order"]

    ax1.plot(orders, bics, "bo-", ms=8)
    ax1.plot(best, bics[best], "r*", ms=16)
    ax1.set_xlabel("RK Order")
    ax1.set_ylabel("BIC")
    ax1.set_title(f"{label} — BIC vs Order")
    ax1.grid(True, alpha=0.3)

    ax2.plot(orders, r2s, "gs-", ms=8)
    ax2.plot(best, r2s[best], "r*", ms=16)
    ax2.set_xlabel("RK Order")
    ax2.set_ylabel("R²")
    ax2.set_title(f"{label} — R² vs Order")
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    out = os.path.join(RK_DEBUG_OUT, filename)
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"  BIC diagnostic → {os.path.relpath(out, _WORKSPACE)}")


# ═══════════════════════════════════════════════════════════════
#  5. DUAL BASELINE: Arrhenius vs Linear for viscosity
# ═══════════════════════════════════════════════════════════════

def test_dual_baseline_viscosity(data):
    """Compare activation-energy (Arrhenius) vs free-energy (linear) baselines
    for viscosity: the key conceptual distinction.

    For viscosity:
      - Arrhenius ideal: ln(η_mix) = Σ x_i ln(η_i)  → excess is in ln-space
      - Linear ideal:    η_mix = Σ x_i η_i           → excess is direct difference

    Both are physically meaningful.  This test computes and plots both.
    """
    print("\n" + "=" * 70)
    print("  TEST 5: DUAL BASELINE — Arrhenius vs Linear for viscosity")
    print("=" * 70)

    rows = data["rows"]
    header = data["header"]
    y_col = "viscosity_pa_s"
    x_col, comp_in_col = _detect_comp_col(header)
    assert x_col is not None
    other_comp = _infer_other_component(comp_in_col, ["toluene", "2-hexanol"])
    temps = _unique_T(rows, "temperature_k")

    fig, axes = plt.subplots(2, len(temps), figsize=(7 * len(temps), 10))
    if len(temps) == 1:
        axes = axes.reshape(2, 1)

    dual_results = {}  # T → {"x_mix", "excess_linear", "excess_arrhenius"}
    for i, T in enumerate(temps):
        sub = _filter_T(rows, "temperature_k", T)
        x = _col_array(sub, x_col)
        y = _col_array(sub, y_col)
        order = np.argsort(x)
        x, y = x[order], y[order]

        # Edge extraction
        x_dict_T = {comp_in_col: x, other_comp: 1.0 - x}
        pure_values = pure_values_from_edges(x_dict_T, y, threshold=0.02)

        print(f"\n  T={T} K: η({comp_in_col})={pure_values[comp_in_col]:.6f}, "
              f"η({other_comp})={pure_values[other_comp]:.6f} Pa·s")

        # Compute BOTH baselines using mixing_rule="both"
        excess = compute_excess_property(
            {comp_in_col: x}, y, pure_values, "viscosity",
            mixing_rule="both",
        )
        assert "error" not in excess, f"dual excess error: {excess}"
        assert excess["mixing_rule"] == "both"

        y_ideal_lin = np.array(excess["y_ideal_linear"])
        y_ideal_arr = np.array(excess["y_ideal_arrhenius"])
        y_exc_lin = np.array(excess["y_excess_linear"])
        y_exc_arr = np.array(excess["y_excess_arrhenius"])

        print(f"    max |ηᴱ (linear)|:    {np.max(np.abs(y_exc_lin)):.6f} Pa·s")
        print(f"    max |Δln(η) (Arrh.)|: {np.max(np.abs(y_exc_arr)):.6f}")

        dual_results[T] = {
            "x": x, "y": y,
            "y_ideal_linear": y_ideal_lin,
            "y_ideal_arrhenius": y_ideal_arr,
            "y_excess_linear": y_exc_lin,
            "y_excess_arrhenius": y_exc_arr,
            "pure_values": pure_values,
        }

        # Top row: raw data + both ideal baselines
        ax_top = axes[0, i]
        ax_top.plot(x, y * 1000, "ko-", ms=4, label="Experimental")
        ax_top.plot(x, y_ideal_lin * 1000, "b--", lw=2, label="Ideal (linear/free-energy)")
        ax_top.plot(x, y_ideal_arr * 1000, "r--", lw=2, label="Ideal (Arrhenius/activ.-energy)")
        ax_top.set_xlabel(f"x({comp_in_col})")
        ax_top.set_ylabel("η (mPa·s)")
        ax_top.set_title(f"T = {T} K — Baselines")
        ax_top.legend(fontsize=8)
        ax_top.grid(True, alpha=0.3)

        # Bottom row: both excess properties
        ax_bot = axes[1, i]
        ax_bot.plot(x, y_exc_lin * 1000, "bs-", ms=4, label="ηᴱ (free-energy ideal)")
        ax_bot2 = ax_bot.twinx()
        ax_bot2.plot(x, y_exc_arr, "r^-", ms=4, label="Δln(η) (activ.-energy ideal)")
        ax_bot.set_xlabel(f"x({comp_in_col})")
        ax_bot.set_ylabel("ηᴱ (mPa·s)", color="blue")
        ax_bot2.set_ylabel("Δln(η)", color="red")
        ax_bot.set_title(f"T = {T} K — Excess properties")
        ax_bot.axhline(0, color="gray", ls=":", lw=0.8)
        # Combined legend
        lines1 = ax_bot.get_lines()
        lines2 = ax_bot2.get_lines()
        ax_bot.legend(lines1 + lines2, [l.get_label() for l in lines1 + lines2], fontsize=8)
        ax_bot.grid(True, alpha=0.3)

    fig.suptitle("Toluene + 2-Hexanol viscosity — Dual baseline comparison", y=1.02, fontsize=13)
    fig.tight_layout()
    out = os.path.join(BASELINE_DEBUG_OUT, "toluene_2hexanol_DUAL_baseline.png")
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot → {os.path.relpath(out, _WORKSPACE)}")

    return dual_results


# ═══════════════════════════════════════════════════════════════
#  6. MULTI-PROPERTY RK: fit both excess types with RK
# ═══════════════════════════════════════════════════════════════

def test_multi_property_rk(dual_results):
    """Fit RK polynomials to BOTH excess functions (linear & Arrhenius)
    for viscosity, then compare the quality and coefficients.

    This demonstrates fit_multi_property: fitting two different
    excess definitions from the same raw data simultaneously.
    """
    print("\n" + "=" * 70)
    print("  TEST 6: MULTI-PROPERTY RK — Arrhenius vs Linear excess fits")
    print("=" * 70)

    temps = sorted(dual_results.keys())
    fig, axes = plt.subplots(2, len(temps), figsize=(7 * len(temps), 10))
    if len(temps) == 1:
        axes = axes.reshape(2, 1)

    all_rk_results = {}
    for i, T in enumerate(temps):
        d = dual_results[T]
        x, y_exc_lin, y_exc_arr = d["x"], d["y_excess_linear"], d["y_excess_arrhenius"]

        x_mix, y_lin_mix = _filter_mixture(x, y_exc_lin)
        _, y_arr_mix = _filter_mixture(x, y_exc_arr)

        print(f"\n  T={T} K — {len(x_mix)} mixture points")

        # Fit both via fit_multi_property
        excess_dict = {
            "linear": y_lin_mix,
            "arrhenius": y_arr_mix,
        }
        rk_results = fit_multi_property(x_mix, excess_dict, max_order=4)
        all_rk_results[T] = rk_results

        for label, res in rk_results.items():
            if "error" in res:
                print(f"    {label}: ERROR — {res['error']}")
            else:
                print(f"    {label}: order={res['selected_order']}  "
                      f"R²={res['r_squared']:.6f}  RMSE={res['rmse']:.8f}  "
                      f"coeffs={[round(c, 6) for c in res['coeffs']]}")

        x_smooth = np.linspace(0.001, 0.999, 200)

        # Top row: LINEAR excess RK fit
        ax_lin = axes[0, i]
        res_lin = rk_results["linear"]
        if "error" not in res_lin:
            y_smooth_lin = eval_redlich_kister(x_smooth, res_lin["coeffs"])
            ax_lin.plot(x_mix, y_lin_mix * 1000, "bs", ms=5, label="Data (ηᴱ)")
            ax_lin.plot(x_smooth, y_smooth_lin * 1000, "b-", lw=2,
                        label=f"RK n={res_lin['selected_order']} (R²={res_lin['r_squared']:.4f})")
            ax_lin.axhline(0, color="gray", ls=":", lw=0.8)
            ax_lin.set_ylabel("ηᴱ (mPa·s)")
        ax_lin.set_xlabel(f"x(toluene)")
        ax_lin.set_title(f"T={T} K — Free-energy ideal excess")
        ax_lin.legend(fontsize=8)
        ax_lin.grid(True, alpha=0.3)

        # Bottom row: ARRHENIUS excess RK fit
        ax_arr = axes[1, i]
        res_arr = rk_results["arrhenius"]
        if "error" not in res_arr:
            y_smooth_arr = eval_redlich_kister(x_smooth, res_arr["coeffs"])
            ax_arr.plot(x_mix, y_arr_mix, "r^", ms=5, label="Data (Δln η)")
            ax_arr.plot(x_smooth, y_smooth_arr, "r-", lw=2,
                        label=f"RK n={res_arr['selected_order']} (R²={res_arr['r_squared']:.4f})")
            ax_arr.axhline(0, color="gray", ls=":", lw=0.8)
            ax_arr.set_ylabel("Δln(η)")
        ax_arr.set_xlabel(f"x(toluene)")
        ax_arr.set_title(f"T={T} K — Activ.-energy ideal excess")
        ax_arr.legend(fontsize=8)
        ax_arr.grid(True, alpha=0.3)

    fig.suptitle("Toluene + 2-Hexanol — RK fits: Linear vs Arrhenius excess", y=1.02, fontsize=13)
    fig.tight_layout()
    out = os.path.join(RK_DEBUG_OUT, "toluene_2hexanol_DUAL_RK_fits.png")
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot → {os.path.relpath(out, _WORKSPACE)}")

    # Coefficient comparison plot across temperatures (if multi-T)
    if len(temps) > 1:
        fig2, (ax_c1, ax_c2) = plt.subplots(1, 2, figsize=(13, 5))

        for rule, ax_c, title in [
            ("linear", ax_c1, "Free-energy ideal (ηᴱ)"),
            ("arrhenius", ax_c2, "Activ.-energy ideal (Δln η)"),
        ]:
            max_n = max(
                (rk[rule].get("selected_order", 0)
                 for rk in all_rk_results.values() if "error" not in rk[rule]),
                default=0,
            )
            for k in range(max_n + 1):
                vals = []
                for T in temps:
                    res = all_rk_results[T][rule]
                    if "error" not in res and k < len(res["coeffs"]):
                        vals.append(res["coeffs"][k])
                    else:
                        vals.append(np.nan)
                ax_c.plot(temps, vals, "o-", ms=6, label=f"A{k}")
            ax_c.set_xlabel("Temperature (K)")
            ax_c.set_ylabel("RK coefficient")
            ax_c.set_title(f"RK coeffs vs T — {title}")
            ax_c.legend()
            ax_c.grid(True, alpha=0.3)

        fig2.tight_layout()
        out2 = os.path.join(RK_DEBUG_OUT, "toluene_2hexanol_DUAL_coeffs_vs_T.png")
        fig2.savefig(out2, dpi=150)
        plt.close(fig2)
        print(f"  coeff-vs-T plot → {os.path.relpath(out2, _WORKSPACE)}")

    return all_rk_results


# ═══════════════════════════════════════════════════════════════
#  7. TERNARY SYNTHETIC TEST — N-component ideal baseline
# ═══════════════════════════════════════════════════════════════

def test_ternary_synthetic():
    """Verify N-component ideal baseline with a synthetic ternary system.

    Creates a grid of (x_A, x_B, x_C) compositions with known pure-
    component densities and verifies:
      - Linear ideal baseline: ρ_ideal = x_A·ρ_A + x_B·ρ_B + x_C·ρ_C
      - Arrhenius ideal baseline for viscosity
      - extract_pure_from_edges recovers the pure values correctly
      - Excess property for synthetic data with known nonideality
    """
    print("\n" + "=" * 70)
    print("  TEST 7: TERNARY SYNTHETIC — N-component ideal baseline")
    print("=" * 70)

    # Known pure-component densities (kg/m³) — realistic water/ethanol/methanol
    pure_rho = {"water": 997.0, "ethanol": 789.0, "methanol": 791.0}
    # Known pure-component viscosities (Pa·s)
    pure_eta = {"water": 0.891e-3, "ethanol": 1.074e-3, "methanol": 0.544e-3}

    comps = ["water", "ethanol", "methanol"]

    # Generate a regular simplex grid: x_A + x_B + x_C = 1
    n_per_edge = 15
    points = []
    for i in range(n_per_edge + 1):
        for j in range(n_per_edge + 1 - i):
            k = n_per_edge - i - j
            points.append((i / n_per_edge, j / n_per_edge, k / n_per_edge))
    points = np.array(points)
    x_A, x_B, x_C = points[:, 0], points[:, 1], points[:, 2]
    n_pts = len(x_A)
    print(f"  generated {n_pts} ternary grid points")

    # ---- Test 1: Linear baseline (density) ----
    print("\n  [7a] Linear baseline for density")
    x_dict = {"water": x_A, "ethanol": x_B, "methanol": x_C}
    baseline = build_ideal_baseline(pure_rho, x_dict, "density", component_order=comps)
    assert "error" not in baseline, f"baseline error: {baseline}"
    assert baseline["n_components"] == 3
    assert baseline["mixing_rule"] == "linear"

    y_ideal = np.array(baseline["y_ideal"])
    y_expected = x_A * 997.0 + x_B * 789.0 + x_C * 791.0
    max_diff = np.max(np.abs(y_ideal - y_expected))
    print(f"    max |y_ideal - expected| = {max_diff:.2e}  (should be ~0)")
    assert max_diff < 1e-10, f"Linear baseline mismatch: {max_diff}"
    print(f"    ρ range: {y_ideal.min():.1f} → {y_ideal.max():.1f} kg/m³")

    # ---- Test 2: Arrhenius baseline (viscosity) ----
    print("\n  [7b] Arrhenius baseline for viscosity")
    baseline_arr = build_ideal_baseline(pure_eta, x_dict, "viscosity", component_order=comps)
    assert "error" not in baseline_arr
    assert baseline_arr["mixing_rule"] == "arrhenius"
    y_ideal_arr = np.array(baseline_arr["y_ideal"])
    y_expected_arr = np.exp(
        x_A * np.log(0.891e-3) + x_B * np.log(1.074e-3) + x_C * np.log(0.544e-3)
    )
    max_diff_arr = np.max(np.abs(y_ideal_arr - y_expected_arr))
    print(f"    max |y_ideal - expected| = {max_diff_arr:.2e}  (should be ~0)")
    assert max_diff_arr < 1e-15

    # ---- Test 3: edge extraction on ternary data ----
    print("\n  [7c] Edge extraction on ternary data")
    # Synthesize property data with slight nonideality
    rng = np.random.default_rng(42)
    y_synth = y_expected + 5.0 * rng.normal(size=n_pts)  # small noise
    # Force near-pure points to exact values (simulating real endpoints)
    for idx in range(n_pts):
        if x_A[idx] > 0.98:
            y_synth[idx] = 997.0 + rng.normal() * 0.1
        elif x_B[idx] > 0.98:
            y_synth[idx] = 789.0 + rng.normal() * 0.1
        elif x_C[idx] > 0.98:
            y_synth[idx] = 791.0 + rng.normal() * 0.1

    extracted = extract_pure_from_edges(x_dict, y_synth, threshold=0.02)
    print(f"    extracted pure values: {extracted}")
    assert len(extracted) == 3, f"Expected 3 pure values, got {len(extracted)}"
    for comp, expected in pure_rho.items():
        actual = extracted[comp]["value"]
        err = abs(actual - expected)
        print(f"    {comp}: expected={expected:.1f}, got={actual:.1f}, "
              f"err={err:.1f}, max_x={extracted[comp]['max_x']:.4f}")
        assert err < 2.0, f"Edge extraction error for {comp}: {err}"

    # Flat dict for downstream calls
    pure_from_edges = {c: d["value"] for c, d in extracted.items()}

    # ---- Test 4: Ternary excess property ----
    print("\n  [7d] Ternary excess property")
    # Add a known ternary interaction: Y_excess = α·x_A·x_B·x_C
    alpha = -200.0  # ternary interaction parameter (kg/m³)
    y_with_excess = y_expected + alpha * x_A * x_B * x_C
    excess = compute_excess_property(
        x_dict, y_with_excess, pure_rho, "density",
        component_order=comps,
    )
    assert "error" not in excess, f"excess error: {excess}"
    assert excess["n_components"] == 3
    y_exc = np.array(excess["y_excess"])
    y_exc_expected = alpha * x_A * x_B * x_C
    max_exc_diff = np.max(np.abs(y_exc - y_exc_expected))
    print(f"    max |y_excess - expected| = {max_exc_diff:.2e}  (should be ~0)")
    assert max_exc_diff < 1e-10
    # Maximum excess at equimolar (1/3, 1/3, 1/3)
    equimolar_idx = np.argmin(np.abs(x_A - 1/3) + np.abs(x_B - 1/3) + np.abs(x_C - 1/3))
    print(f"    excess at equimolar: {y_exc[equimolar_idx]:.2f} kg/m³  "
          f"(expected: {alpha/27:.2f})")

    # ---- Test 5: dict input with N-1 components (inferred last) ----
    print("\n  [7e] Dict input with N-1 components (methanol inferred)")
    x_dict_partial = {"water": x_A, "ethanol": x_B}  # methanol inferred
    baseline_partial = build_ideal_baseline(
        pure_rho, x_dict_partial, "density", component_order=comps,
    )
    assert "error" not in baseline_partial
    y_partial = np.array(baseline_partial["y_ideal"])
    max_diff_partial = np.max(np.abs(y_partial - y_expected))
    print(f"    max |y_partial - y_full| = {max_diff_partial:.2e}  (should be ~0)")
    assert max_diff_partial < 1e-10

    # ---- Plot: ternary contour of ideal density + excess ----
    try:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Convert ternary to Cartesian for plotting
        # x_cart = x_B + 0.5*x_C,  y_cart = (√3/2)*x_C
        x_cart = x_B + 0.5 * x_C
        y_cart = (np.sqrt(3) / 2) * x_C

        # Triangle boundary
        tri_x = [0, 1, 0.5, 0]
        tri_y = [0, 0, np.sqrt(3)/2, 0]

        # Left: ideal density contour
        sc1 = ax1.tricontourf(x_cart, y_cart, y_ideal, levels=20, cmap="viridis")
        ax1.plot(tri_x, tri_y, "k-", lw=1.5)
        ax1.set_aspect("equal")
        fig.colorbar(sc1, ax=ax1, label="ρ_ideal (kg/m³)")
        ax1.set_title("Ideal density (linear mixing)")
        # Label vertices
        ax1.text(-0.05, -0.05, "water", ha="center", fontsize=9)
        ax1.text(1.05, -0.05, "ethanol", ha="center", fontsize=9)
        ax1.text(0.5, np.sqrt(3)/2 + 0.05, "methanol", ha="center", fontsize=9)
        ax1.set_xlim(-0.1, 1.15)
        ax1.set_ylim(-0.1, 1.0)
        ax1.axis("off")

        # Right: ternary excess
        sc2 = ax2.tricontourf(x_cart, y_cart, y_exc, levels=20, cmap="RdBu_r")
        ax2.plot(tri_x, tri_y, "k-", lw=1.5)
        ax2.set_aspect("equal")
        fig.colorbar(sc2, ax=ax2, label="ρᴱ (kg/m³)")
        ax2.set_title(f"Ternary excess (α={alpha})")
        ax2.text(-0.05, -0.05, "water", ha="center", fontsize=9)
        ax2.text(1.05, -0.05, "ethanol", ha="center", fontsize=9)
        ax2.text(0.5, np.sqrt(3)/2 + 0.05, "methanol", ha="center", fontsize=9)
        ax2.set_xlim(-0.1, 1.15)
        ax2.set_ylim(-0.1, 1.0)
        ax2.axis("off")

        fig.suptitle("Synthetic ternary: Water + Ethanol + Methanol", fontsize=13)
        fig.tight_layout()
        out = os.path.join(BASELINE_DEBUG_OUT, "ternary_synthetic.png")
        fig.savefig(out, dpi=150)
        plt.close(fig)
        print(f"\n  plot → {os.path.relpath(out, _WORKSPACE)}")
    except Exception as e:
        print(f"\n  Warning: ternary plot failed ({e}) — continuing")

    return True


# ═══════════════════════════════════════════════════════════════
#  8. GENERIC BINARY SYSTEM TEST (baseline + RK + CSV + topology)
# ═══════════════════════════════════════════════════════════════

def test_generic_binary(data, tag, property_type, known_compounds):
    """Full pipeline test for any binary system: baseline → excess → RK → CSV → topology.

    Parameters
    ----------
    data : dict   — {"header":..., "rows":..., "metadata":...}
    tag  : str    — file-name prefix (e.g. "propanol2_water_density")
    property_type : str — "density" or "viscosity"
    known_compounds : list[str] — [comp_A, comp_B]
    """
    label = tag.replace("_", " ").title()
    print(f"\n{'=' * 70}")
    print(f"  TEST 8 ({tag}): {label}")
    print(f"{'=' * 70}")

    rows  = data["rows"]
    header = data["header"]

    # Auto-detect property and composition columns
    y_col = None
    for col in header:
        if "density" in col and property_type == "density":
            y_col = col; break
        if "viscosity" in col and property_type == "viscosity":
            y_col = col; break
    if not y_col:
        print(f"  SKIP: no {property_type} column in {header}")
        return None

    x_col, comp_in_col = _detect_comp_col(header)
    if not x_col:
        print(f"  SKIP: no mole_fraction column in {header}")
        return None

    other_comp = _infer_other_component(comp_in_col, known_compounds)
    print(f"  x={x_col} → x({comp_in_col}), y={y_col}, other={other_comp}")

    temps = _unique_T(rows, "temperature_k") if "temperature_k" in header else [None]
    print(f"  temperatures: {temps}")

    # Pick at most 3 temperatures to keep output manageable
    if len(temps) > 3:
        temps = [temps[0], temps[len(temps)//2], temps[-1]]
        print(f"  → sampled to {temps}")

    results_by_T = {}
    n_cols = min(3, len(temps))
    fig, axes = plt.subplots(2, n_cols, figsize=(6 * n_cols, 9),
                             squeeze=False)

    for i, T in enumerate(temps[:n_cols]):
        sub = _filter_T(rows, "temperature_k", T) if T else rows
        x = _col_array(sub, x_col)
        y = _col_array(sub, y_col)
        order = np.argsort(x)
        x, y = x[order], y[order]

        # Edge extraction
        x_dict = {comp_in_col: x, other_comp: 1.0 - x}
        pure_vals = pure_values_from_edges(x_dict, y, threshold=0.02)
        print(f"  T={T} K: pure({comp_in_col})={pure_vals[comp_in_col]:.6g}, "
              f"pure({other_comp})={pure_vals[other_comp]:.6g}")

        rule = default_mixing_rule(property_type)
        baseline = build_ideal_baseline(pure_vals, {comp_in_col: x}, property_type)
        if "error" in baseline:
            print(f"    baseline error: {baseline['error']}")
            continue

        excess = compute_excess_property({comp_in_col: x}, y, pure_vals, property_type)
        if "error" in excess:
            print(f"    excess error: {excess['error']}")
            continue

        y_exc = np.array(excess["y_excess"])
        y_ideal = np.array(baseline["y_ideal"])
        x_mix, y_mix = _filter_mixture(x, y_exc)

        if len(x_mix) < 3:
            print(f"    only {len(x_mix)} mixture points, skipping RK")
            continue

        rk = auto_fit_redlich_kister(x_mix, y_mix, max_order=5)
        if "error" in rk:
            print(f"    RK error: {rk['error']}")
            continue

        results_by_T[T] = rk
        print(f"    RK order={rk['selected_order']} R²={rk['r_squared']:.6f} "
              f"RMSE={rk['rmse']:.6g}")

        # CSV + topology
        T_tag = f"_{T}K" if T else ""
        _save_topo_and_csv(
            f"{tag}{T_tag}", x_mix, y_mix,
            np.array(rk["y_fitted"]), np.array(rk["residuals"]),
            rk["coeffs"], rk["selected_order"],
            rk["r_squared"], rk["rmse"],
            x_label=f"x({comp_in_col})",
            y_label=f"{property_type}_excess",
            metadata={"system": label, "T_K": T,
                      "property": property_type, "mixing_rule": rule},
        )

        # Save baseline CSV
        bl_csv = os.path.join(CSV_OUT, f"{tag}{T_tag}_baseline.csv")
        save_baseline_csv(bl_csv, x, y, y_ideal,
                          x_label=f"x({comp_in_col})", y_label=property_type)
        print(f"  csv  → {os.path.relpath(bl_csv, _WORKSPACE)}")

        # Plot: top = raw + ideal, bottom = RK fit
        ax_top = axes[0, i]
        ax_top.plot(x, y, "ko-", ms=3, label="Experimental")
        ax_top.plot(x, y_ideal, "r--", lw=2, label=f"Ideal ({rule})")
        ax_top.set_xlabel(f"x({comp_in_col})")
        ax_top.set_ylabel(y_col)
        ax_top.set_title(f"T = {T} K" if T else tag)
        ax_top.legend(fontsize=8)
        ax_top.grid(True, alpha=0.3)

        ax_bot = axes[1, i]
        x_smooth = np.linspace(0.001, 0.999, 200)
        y_smooth = eval_redlich_kister(x_smooth, rk["coeffs"])
        ax_bot.plot(x_mix, y_mix, "ko", ms=4, label="Data")
        ax_bot.plot(x_smooth, y_smooth, "r-", lw=2,
                    label=f"RK n={rk['selected_order']}")
        ax_bot.axhline(0, color="gray", ls=":", lw=0.8)
        ax_bot.set_xlabel(f"x({comp_in_col})")
        ax_bot.set_ylabel("Excess")
        ax_bot.set_title(f"R²={rk['r_squared']:.5f}")
        ax_bot.legend(fontsize=8)
        ax_bot.grid(True, alpha=0.3)

    fig.suptitle(label, y=1.02, fontsize=13)
    fig.tight_layout()
    out = os.path.join(RK_DEBUG_OUT, f"{tag}_overview.png")
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot → {os.path.relpath(out, _WORKSPACE)}")

    return results_by_T


def main():
    print("=" * 70)
    print("  DEBUG: Core algorithm tests for ThermoML analysis agent")
    print("=" * 70)

    # Step 1: Extract data
    data = extract_debug_inputs()
    if not data:
        print("\nFATAL: No data extracted. Check DB paths.")
        return

    passed = 0
    failed = 0

    # Step 2: Ideal baseline tests (single-rule)
    ew_excess = th_excess = em_excess = None
    try:
        ew_excess = test_ethanol_water_baseline(data["ethanol_water_density"])
        passed += 1
    except Exception as e:
        print(f"  FAIL: ethanol-water baseline — {e}")
        failed += 1

    try:
        th_excess = test_toluene_hexanol_baseline(data["toluene_2hexanol_viscosity"])
        passed += 1
    except Exception as e:
        print(f"  FAIL: toluene-hexanol baseline — {e}")
        failed += 1

    try:
        em_excess = test_ethyl_methanoate_baseline(data["ethyl_methanoate_decane_density"])
        passed += 1
    except Exception as e:
        print(f"  FAIL: ethyl methanoate baseline — {e}")
        failed += 1

    # Step 3: RK fitting tests (single-rule)
    if ew_excess is not None:
        try:
            ew_rk = test_rk_ethanol_water(ew_excess)
            plot_bic_diagnostic(ew_rk, "Ethanol-Water ρᴱ", "ethanol_water_BIC.png")
            passed += 1
        except Exception as e:
            print(f"  FAIL: ethanol-water RK — {e}")
            failed += 1

    if th_excess is not None:
        try:
            test_rk_toluene_hexanol(th_excess)
            passed += 1
        except Exception as e:
            print(f"  FAIL: toluene-hexanol RK — {e}")
            failed += 1

    if em_excess is not None:
        try:
            test_rk_ethyl_methanoate(em_excess)
            passed += 1
        except Exception as e:
            print(f"  FAIL: ethyl methanoate RK — {e}")
            failed += 1

    # Step 4: DUAL BASELINE tests (Arrhenius vs Linear for viscosity)
    dual_results = None
    try:
        dual_results = test_dual_baseline_viscosity(data["toluene_2hexanol_viscosity"])
        passed += 1
    except Exception as e:
        print(f"  FAIL: dual baseline viscosity — {e}")
        traceback.print_exc()
        failed += 1

    # Step 5: Multi-property RK fitting (both baselines)
    if dual_results is not None:
        try:
            test_multi_property_rk(dual_results)
            passed += 1
        except Exception as e:
            print(f"  FAIL: multi-property RK — {e}")
            traceback.print_exc()
            failed += 1

    # Step 6: Ternary synthetic test (N-component generalization)
    try:
        test_ternary_synthetic()
        passed += 1
    except Exception as e:
        print(f"  FAIL: ternary synthetic — {e}")
        traceback.print_exc()
        failed += 1

    # Step 7: Additional binary systems (generic pipeline)
    additional_systems = [
        ("dmc_methanol_density", "density", ["dimethyl carbonate", "methanol"]),
        ("cyclohexane_hexadecane_viscosity", "viscosity", ["cyclohexane", "hexadecane"]),
        ("toluene_mtbe_density", "density", ["toluene", "2-methoxy-2-methylpropane"]),
        ("methanol_acetone_density", "density", ["methanol", "acetone"]),
        ("acetone_chloroform_density", "density", ["acetone", "trichloromethane"]),
        ("methanol_chlorobenzene_density", "density", ["methanol", "chlorobenzene"]),
        ("methanol_chlorobenzene_viscosity", "viscosity", ["methanol", "chlorobenzene"]),
        ("aniline_1propanol_density", "density", ["aniline", "propan-1-ol"]),
    ]
    for tag, prop_type, comp_names in additional_systems:
        if tag not in data:
            print(f"\n  SKIP: {tag} — not extracted (DOI not in DB?)")
            continue
        try:
            test_generic_binary(data[tag], tag, prop_type, comp_names)
            passed += 1
        except Exception as e:
            print(f"  FAIL: {tag} — {e}")
            traceback.print_exc()
            failed += 1

    # Summary
    print("\n" + "=" * 70)
    print(f"  SUMMARY:  {passed} passed  /  {failed} failed")
    print("=" * 70)

    print(f"\nDEBUG_input CSVs:  {BASELINE_DEBUG_IN}")
    print(f"Baseline plots:    {BASELINE_DEBUG_OUT}")
    print(f"RK plots:          {RK_DEBUG_OUT}")
    print(f"CSV output:        {CSV_OUT}")
    print(f"Topology output:   {TOPO_OUT}")


if __name__ == "__main__":
    main()
