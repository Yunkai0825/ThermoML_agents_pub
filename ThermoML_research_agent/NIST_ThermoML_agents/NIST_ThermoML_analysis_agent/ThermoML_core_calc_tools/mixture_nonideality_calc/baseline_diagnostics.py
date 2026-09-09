"""
baseline_diagnostics — Plot / CSV output helpers for ideal-baseline analysis.
=============================================================================
Moved out of DEBUG_run_core_algorithms so production code can reuse it.

Public functions
----------------
run_single_baseline   — one system, one rule (linear/arrhenius), all temperatures
run_dual_baseline     — same data, both rules side-by-side
run_ternary_synthetic — synthetic N-component verification
"""

from __future__ import annotations

import csv
import os
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

# Core baseline algorithms
from .ideal_baseline import (
    build_ideal_baseline,
    compute_excess_property,
    default_mixing_rule,
    extract_pure_from_edges,
    pure_values_from_edges,
)

# CSV export helpers
try:
    from ..output_helpers.csv_export import save_baseline_csv, save_excess_csv
except ImportError:  # running outside package context
    from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.output_helpers.csv_export import (
        save_baseline_csv, save_excess_csv,
    )

# matplotlib — non-interactive backend
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ═══════════════════════════════════════════════════════════════
#  Single-rule baseline (linear OR arrhenius)
# ═══════════════════════════════════════════════════════════════

def run_single_baseline(
    *,
    x: np.ndarray,
    y: np.ndarray,
    comp_in_col: str,
    other_comp: str,
    property_type: str,
    tag: str,
    cond_label: str = "",
    plot_dir: str = ".",
    csv_dir: str = ".",
    workspace_root: str = ".",
) -> Dict[str, Any]:
    """Compute ideal baseline + excess for a single (T,P,…) slice.

    Parameters
    ----------
    x, y        : 1-D arrays already filtered to one condition group.
    comp_in_col : component whose mole fraction is *x*.
    other_comp  : the other binary component.
    property_type : "density" / "viscosity" / …
    tag         : file-name stem  (e.g. "ethanol_water_density_298.15K")
    cond_label  : human-readable condition label (for plot title)
    plot_dir, csv_dir : output directories
    workspace_root : for relative-path printing

    Returns
    -------
    dict with keys: x, y_excess, y_ideal, pure_values, mixing_rule, error (if any)
    """
    os.makedirs(plot_dir, exist_ok=True)
    os.makedirs(csv_dir, exist_ok=True)

    order = np.argsort(x)
    x, y = x[order], y[order]

    # Edge extraction
    x_dict = {comp_in_col: x, other_comp: 1.0 - x}
    try:
        pure_values = pure_values_from_edges(x_dict, y, threshold=0.02)
    except Exception as e:
        return {"error": f"edge extraction failed: {e}"}

    # Build ideal baseline
    baseline = build_ideal_baseline(pure_values, {comp_in_col: x}, property_type)
    if "error" in baseline:
        return {"error": f"baseline: {baseline['error']}"}

    # Compute excess
    excess = compute_excess_property({comp_in_col: x}, y, pure_values, property_type)
    if "error" in excess:
        return {"error": f"excess: {excess['error']}"}

    rule = baseline["mixing_rule"]
    y_ideal = np.array(baseline["y_ideal"])
    y_exc = np.array(excess["y_excess"])

    # ── Plot ──
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(x, y, "ko-", ms=4, label="Experimental")
    ax1.plot(x, y_ideal, "r--", lw=2, label=f"Ideal ({rule})")
    ax1.set_xlabel(f"x({comp_in_col})")
    ax1.set_ylabel(property_type)
    title = f"{other_comp.title()} + {comp_in_col.title()} {property_type}"
    if cond_label:
        title += f", {cond_label}"
    ax1.set_title(title)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(x, y_exc, "bs-", ms=4)
    ax2.axhline(0, color="gray", ls="--", lw=0.8)
    ax2.set_xlabel(f"x({comp_in_col})")
    ax2.set_ylabel(f"Excess {property_type}")
    ax2.set_title(f"Y_excess = Y_exp − Y_ideal")
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    plot_path = os.path.join(plot_dir, f"{tag}_baseline.png")
    fig.savefig(plot_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

    # ── CSVs ──
    bl_csv = os.path.join(csv_dir, f"{tag}_baseline.csv")
    save_baseline_csv(bl_csv, x, y, y_ideal,
                      x_label=f"x({comp_in_col})", y_label=property_type)

    ex_csv = os.path.join(csv_dir, f"{tag}_excess.csv")
    save_excess_csv(ex_csv, x, y, y_ideal, y_exc,
                    x_label=f"x({comp_in_col})", y_label=property_type,
                    mixing_rule=rule)

    return {
        "x": x,
        "y": y,
        "y_ideal": y_ideal,
        "y_excess": y_exc,
        "pure_values": pure_values,
        "mixing_rule": rule,
        "comp_in_col": comp_in_col,
        "other_comp": other_comp,
        "plot_path": plot_path,
        "csv_paths": [bl_csv, ex_csv],
    }


def run_multi_T_baseline(
    *,
    x_by_group: Dict[Any, np.ndarray],
    y_by_group: Dict[Any, np.ndarray],
    group_labels: Dict[Any, str],
    comp_in_col: str,
    other_comp: str,
    property_type: str,
    tag: str,
    plot_dir: str = ".",
    csv_dir: str = ".",
    workspace_root: str = ".",
) -> Dict[Any, Dict[str, Any]]:
    """Run baseline for multiple condition groups and produce a combined plot.

    Parameters
    ----------
    x_by_group : dict — group_key → x array
    y_by_group : dict — group_key → y array
    group_labels : dict — group_key → display label (e.g. "T=298.15 K")
    (other params as in run_single_baseline)

    Returns
    -------
    dict — group_key → result dict (same as run_single_baseline output)
    """
    os.makedirs(plot_dir, exist_ok=True)
    os.makedirs(csv_dir, exist_ok=True)

    groups = sorted(x_by_group.keys())
    n_groups = len(groups)
    results = {}

    fig, axes = plt.subplots(1, max(n_groups, 1), figsize=(6 * max(n_groups, 1), 5))
    if n_groups == 1:
        axes = [axes]

    for i, gk in enumerate(groups):
        x = x_by_group[gk]
        y = y_by_group[gk]
        gl = group_labels.get(gk, str(gk))
        order = np.argsort(x)
        x, y = x[order], y[order]

        x_dict = {comp_in_col: x, other_comp: 1.0 - x}
        try:
            pure_vals = pure_values_from_edges(x_dict, y, threshold=0.02)
        except Exception:
            results[gk] = {"error": "edge extraction failed"}
            continue

        baseline = build_ideal_baseline(pure_vals, {comp_in_col: x}, property_type)
        if "error" in baseline:
            results[gk] = {"error": baseline["error"]}
            continue

        excess = compute_excess_property({comp_in_col: x}, y, pure_vals, property_type)
        if "error" in excess:
            results[gk] = {"error": excess["error"]}
            continue

        y_ideal = np.array(baseline["y_ideal"])
        y_exc = np.array(excess["y_excess"])
        rule = baseline["mixing_rule"]

        results[gk] = {
            "x": x, "y": y,
            "y_ideal": y_ideal, "y_excess": y_exc,
            "pure_values": pure_vals, "mixing_rule": rule,
            "comp_in_col": comp_in_col, "other_comp": other_comp,
        }

        # Scale for viscosity display
        scale = 1000.0 if "viscosity" in property_type else 1.0
        unit = " (mPa·s)" if "viscosity" in property_type else ""

        ax = axes[i] if i < len(axes) else axes[-1]
        ax.plot(x, y * scale, "ko-", ms=4, label="Experimental")
        ax.plot(x, y_ideal * scale, "r--", lw=2,
                label=f"Ideal ({rule.title()})")
        ax.set_xlabel(f"x({comp_in_col})")
        ax.set_ylabel(f"{property_type}{unit}")
        ax.set_title(gl)
        ax.legend()
        ax.grid(True, alpha=0.3)

    suptitle = f"{other_comp.title()} + {comp_in_col.title()} {property_type}"
    fig.suptitle(suptitle, y=1.02)
    fig.tight_layout()
    plot_path = os.path.join(plot_dir, f"{tag}_baseline.png")
    fig.savefig(plot_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

    # Per-group CSVs (plot CSV companion)
    plot_csv_path = os.path.join(csv_dir, f"{tag}_baseline_plotdata.csv")
    _save_multi_group_plot_csv(plot_csv_path, results, groups, group_labels,
                               comp_in_col, property_type)

    return results


def _save_multi_group_plot_csv(path, results, groups, group_labels,
                                comp_in_col, property_type):
    """Write a single CSV containing ALL groups' baseline plot data."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["condition", f"x({comp_in_col})",
                     f"{property_type}_exp", f"{property_type}_ideal",
                     f"{property_type}_excess", "mixing_rule"])
        for gk in groups:
            r = results.get(gk, {})
            if "error" in r:
                continue
            gl = group_labels.get(gk, str(gk))
            for j in range(len(r["x"])):
                w.writerow([gl, f"{r['x'][j]:.8f}", f"{r['y'][j]:.8g}",
                            f"{r['y_ideal'][j]:.8g}", f"{r['y_excess'][j]:.8g}",
                            r["mixing_rule"]])


# ═══════════════════════════════════════════════════════════════
#  Dual baseline (Arrhenius vs Linear for viscosity)
# ═══════════════════════════════════════════════════════════════

def run_dual_baseline(
    *,
    x_by_group: Dict[Any, np.ndarray],
    y_by_group: Dict[Any, np.ndarray],
    group_labels: Dict[Any, str],
    comp_in_col: str,
    other_comp: str,
    tag: str,
    plot_dir: str = ".",
    csv_dir: str = ".",
) -> Dict[Any, Dict[str, Any]]:
    """Compute both Arrhenius and Linear baselines for viscosity at each group."""
    os.makedirs(plot_dir, exist_ok=True)
    os.makedirs(csv_dir, exist_ok=True)

    groups = sorted(x_by_group.keys())
    n_groups = len(groups)
    results = {}

    fig, axes = plt.subplots(2, max(n_groups, 1),
                             figsize=(7 * max(n_groups, 1), 10),
                             squeeze=False)

    for i, gk in enumerate(groups):
        x = x_by_group[gk]
        y = y_by_group[gk]
        gl = group_labels.get(gk, str(gk))
        order = np.argsort(x)
        x, y = x[order], y[order]

        x_dict = {comp_in_col: x, other_comp: 1.0 - x}
        pure_vals = pure_values_from_edges(x_dict, y, threshold=0.02)

        excess = compute_excess_property(
            {comp_in_col: x}, y, pure_vals, "viscosity", mixing_rule="both")
        if "error" in excess:
            results[gk] = {"error": excess["error"]}
            continue

        y_ideal_lin = np.array(excess["y_ideal_linear"])
        y_ideal_arr = np.array(excess["y_ideal_arrhenius"])
        y_exc_lin = np.array(excess["y_excess_linear"])
        y_exc_arr = np.array(excess["y_excess_arrhenius"])

        results[gk] = {
            "x": x, "y": y,
            "y_ideal_linear": y_ideal_lin, "y_ideal_arrhenius": y_ideal_arr,
            "y_excess_linear": y_exc_lin, "y_excess_arrhenius": y_exc_arr,
            "pure_values": pure_vals,
        }

        # Top row: raw data + both baselines
        ax_top = axes[0, i]
        ax_top.plot(x, y * 1000, "ko-", ms=4, label="Experimental")
        ax_top.plot(x, y_ideal_lin * 1000, "b--", lw=2,
                    label="Ideal (linear/free-energy)")
        ax_top.plot(x, y_ideal_arr * 1000, "r--", lw=2,
                    label="Ideal (Arrhenius/activ.-energy)")
        ax_top.set_xlabel(f"x({comp_in_col})")
        ax_top.set_ylabel("η (mPa·s)")
        ax_top.set_title(f"{gl} — Baselines")
        ax_top.legend(fontsize=8)
        ax_top.grid(True, alpha=0.3)

        # Bottom row: excess properties (dual y-axes)
        ax_bot = axes[1, i]
        ax_bot.plot(x, y_exc_lin * 1000, "bs-", ms=4,
                    label="ηᴱ (free-energy ideal)")
        ax_bot2 = ax_bot.twinx()
        ax_bot2.plot(x, y_exc_arr, "r^-", ms=4,
                     label="Δln(η) (activ.-energy ideal)")
        ax_bot.set_xlabel(f"x({comp_in_col})")
        ax_bot.set_ylabel("ηᴱ (mPa·s)", color="blue")
        ax_bot2.set_ylabel("Δln(η)", color="red")
        ax_bot.set_title(f"{gl} — Excess properties")
        ax_bot.axhline(0, color="gray", ls=":", lw=0.8)
        lines1 = ax_bot.get_lines()
        lines2 = ax_bot2.get_lines()
        ax_bot.legend(lines1 + lines2,
                      [l.get_label() for l in lines1 + lines2], fontsize=8)
        ax_bot.grid(True, alpha=0.3)

    title = f"{other_comp.title()} + {comp_in_col.title()} viscosity — Dual baseline"
    fig.suptitle(title, y=1.02, fontsize=13)
    fig.tight_layout()
    plot_path = os.path.join(plot_dir, f"{tag}_DUAL_baseline.png")
    fig.savefig(plot_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

    # CSV companion — all groups, both baselines
    csv_path = os.path.join(csv_dir, f"{tag}_DUAL_baseline.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["condition", f"x({comp_in_col})",
                     "eta_exp_Pa_s", "eta_ideal_linear", "eta_ideal_arrhenius",
                     "eta_excess_linear", "delta_ln_eta_excess_arrhenius"])
        for gk in groups:
            r = results.get(gk, {})
            if "error" in r:
                continue
            gl = group_labels.get(gk, str(gk))
            for j in range(len(r["x"])):
                w.writerow([gl, f"{r['x'][j]:.8f}",
                            f"{r['y'][j]:.8g}", f"{r['y_ideal_linear'][j]:.8g}",
                            f"{r['y_ideal_arrhenius'][j]:.8g}",
                            f"{r['y_excess_linear'][j]:.8g}",
                            f"{r['y_excess_arrhenius'][j]:.8g}"])

    return results


# ═══════════════════════════════════════════════════════════════
#  Ternary synthetic verification
# ═══════════════════════════════════════════════════════════════

def run_ternary_synthetic(
    *,
    plot_dir: str = ".",
    csv_dir: str = ".",
) -> Dict[str, Any]:
    """Generate a synthetic ternary and verify N-component ideal baseline.

    Returns dict with verification results and paths to output files.
    """
    os.makedirs(plot_dir, exist_ok=True)
    os.makedirs(csv_dir, exist_ok=True)

    pure_rho = {"water": 997.0, "ethanol": 789.0, "methanol": 791.0}
    pure_eta = {"water": 0.891e-3, "ethanol": 1.074e-3, "methanol": 0.544e-3}
    comps = ["water", "ethanol", "methanol"]

    # Regular simplex grid
    n_per_edge = 15
    points = []
    for i in range(n_per_edge + 1):
        for j in range(n_per_edge + 1 - i):
            k = n_per_edge - i - j
            points.append((i / n_per_edge, j / n_per_edge, k / n_per_edge))
    points = np.array(points)
    x_A, x_B, x_C = points[:, 0], points[:, 1], points[:, 2]
    n_pts = len(x_A)

    results = {"n_points": n_pts, "checks": {}}

    x_dict = {"water": x_A, "ethanol": x_B, "methanol": x_C}

    # 1. Linear baseline
    baseline = build_ideal_baseline(pure_rho, x_dict, "density", component_order=comps)
    y_ideal = np.array(baseline["y_ideal"])
    y_expected = x_A * 997.0 + x_B * 789.0 + x_C * 791.0
    results["checks"]["linear_max_err"] = float(np.max(np.abs(y_ideal - y_expected)))

    # 2. Arrhenius baseline
    baseline_arr = build_ideal_baseline(pure_eta, x_dict, "viscosity", component_order=comps)
    y_ideal_arr = np.array(baseline_arr["y_ideal"])
    y_expected_arr = np.exp(
        x_A * np.log(0.891e-3) + x_B * np.log(1.074e-3) + x_C * np.log(0.544e-3))
    results["checks"]["arrhenius_max_err"] = float(
        np.max(np.abs(y_ideal_arr - y_expected_arr)))

    # 3. Edge extraction
    rng = np.random.default_rng(42)
    y_synth = y_expected + 5.0 * rng.normal(size=n_pts)
    for idx in range(n_pts):
        if x_A[idx] > 0.98:
            y_synth[idx] = 997.0 + rng.normal() * 0.1
        elif x_B[idx] > 0.98:
            y_synth[idx] = 789.0 + rng.normal() * 0.1
        elif x_C[idx] > 0.98:
            y_synth[idx] = 791.0 + rng.normal() * 0.1
    extracted = extract_pure_from_edges(x_dict, y_synth, threshold=0.02)
    results["edge_extraction"] = {c: d["value"] for c, d in extracted.items()}

    # 4. Ternary excess with known interaction
    alpha = -200.0
    y_with_excess = y_expected + alpha * x_A * x_B * x_C
    excess = compute_excess_property(x_dict, y_with_excess, pure_rho, "density",
                                     component_order=comps)
    y_exc = np.array(excess["y_excess"])
    y_exc_expected = alpha * x_A * x_B * x_C
    results["checks"]["excess_max_err"] = float(np.max(np.abs(y_exc - y_exc_expected)))

    # 5. Dict with N-1 components
    x_dict_partial = {"water": x_A, "ethanol": x_B}
    baseline_partial = build_ideal_baseline(pure_rho, x_dict_partial, "density",
                                            component_order=comps)
    y_partial = np.array(baseline_partial["y_ideal"])
    results["checks"]["partial_max_err"] = float(
        np.max(np.abs(y_partial - y_expected)))

    # ── Plot ──
    try:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        x_cart = x_B + 0.5 * x_C
        y_cart = (np.sqrt(3) / 2) * x_C
        tri_x = [0, 1, 0.5, 0]
        tri_y = [0, 0, np.sqrt(3) / 2, 0]

        sc1 = ax1.tricontourf(x_cart, y_cart, y_ideal, levels=20, cmap="viridis")
        ax1.plot(tri_x, tri_y, "k-", lw=1.5)
        ax1.set_aspect("equal")
        fig.colorbar(sc1, ax=ax1, label="ρ_ideal (kg/m³)")
        ax1.set_title("Ideal density (linear mixing)")
        ax1.text(-0.05, -0.05, "water", ha="center", fontsize=9)
        ax1.text(1.05, -0.05, "ethanol", ha="center", fontsize=9)
        ax1.text(0.5, np.sqrt(3) / 2 + 0.05, "methanol", ha="center", fontsize=9)
        ax1.set_xlim(-0.1, 1.15);  ax1.set_ylim(-0.1, 1.0);  ax1.axis("off")

        sc2 = ax2.tricontourf(x_cart, y_cart, y_exc, levels=20, cmap="RdBu_r")
        ax2.plot(tri_x, tri_y, "k-", lw=1.5)
        ax2.set_aspect("equal")
        fig.colorbar(sc2, ax=ax2, label="ρᴱ (kg/m³)")
        ax2.set_title(f"Ternary excess (α={alpha})")
        ax2.text(-0.05, -0.05, "water", ha="center", fontsize=9)
        ax2.text(1.05, -0.05, "ethanol", ha="center", fontsize=9)
        ax2.text(0.5, np.sqrt(3) / 2 + 0.05, "methanol", ha="center", fontsize=9)
        ax2.set_xlim(-0.1, 1.15);  ax2.set_ylim(-0.1, 1.0);  ax2.axis("off")

        fig.suptitle("Synthetic ternary: Water + Ethanol + Methanol", fontsize=13)
        fig.tight_layout()
        plot_path = os.path.join(plot_dir, "ternary_synthetic.png")
        fig.savefig(plot_path, dpi=150)
        plt.close(fig)
        results["plot_path"] = plot_path
    except Exception as e:
        results["plot_warning"] = str(e)

    # ── CSV companion for ternary plot ──
    csv_path = os.path.join(csv_dir, "ternary_synthetic.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["x_water", "x_ethanol", "x_methanol",
                     "rho_ideal_kg_m3", "rho_excess_kg_m3"])
        for j in range(n_pts):
            w.writerow([f"{x_A[j]:.6f}", f"{x_B[j]:.6f}", f"{x_C[j]:.6f}",
                        f"{y_ideal[j]:.4f}", f"{y_exc[j]:.6f}"])
    results["csv_path"] = csv_path

    return results
