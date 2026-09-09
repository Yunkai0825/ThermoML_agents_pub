"""
rk_diagnostics — Plot / CSV / topology output for Redlich-Kister fitting.
=========================================================================
Moved out of DEBUG_run_core_algorithms so production code can reuse it.

Public functions
----------------
run_rk_fit_single       — RK fit for one (T,P) condition slice → plot + CSV + topology
run_rk_fit_multi_group  — RK fit for multiple condition groups → combined overview plot
run_multi_property_rk   — Fit RK to both linear & Arrhenius excess from dual-baseline
plot_bic_diagnostic     — BIC vs order diagnostic plot
"""

from __future__ import annotations

import csv as _csv
import os
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

# Core RK algorithms
from .rk_fitter import (
    auto_fit_redlich_kister,
    eval_redlich_kister,
    fit_multi_property,
    fit_redlich_kister,
)

# CSV / topology helpers
try:
    from ..output_helpers.csv_export import save_baseline_csv, save_excess_csv, save_fit_csv
    from ..output_helpers.topology_repr import extract_topology_points, topology_to_csv
    from ..topology_helpers.convex_hull_construction import (
        compute_convex_hull,
        select_hull_edge_points,
    )
except ImportError:
    from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.output_helpers.csv_export import (
        save_baseline_csv, save_excess_csv, save_fit_csv,
    )
    from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.output_helpers.topology_repr import (
        extract_topology_points, topology_to_csv,
    )
    from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.topology_helpers.convex_hull_construction import (
        compute_convex_hull, select_hull_edge_points,
    )

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ═══════════════════════════════════════════════════════════════
#  Helpers
# ═══════════════════════════════════════════════════════════════

def _filter_mixture(x, y, eps=0.02):
    """Remove endpoints near x=0 or x=1."""
    mask = (x > eps) & (x < 1 - eps) & ~np.isnan(x) & ~np.isnan(y)
    return x[mask], y[mask]


def _save_topo_and_csv(
    tag: str,
    x_mix: np.ndarray,
    y_excess: np.ndarray,
    y_fitted: np.ndarray,
    residuals: np.ndarray,
    rk_coeffs: list,
    rk_order: int,
    r_squared: float,
    rmse: float,
    csv_dir: str,
    topo_dir: str,
    *,
    x_label: str = "x1",
    y_label: str = "Y_excess",
    metadata: Optional[dict] = None,
) -> Dict[str, Any]:
    """Save CSV fit + excess + topology for one condition slice.

    Returns dict with paths and hull info.
    """
    os.makedirs(csv_dir, exist_ok=True)
    os.makedirs(topo_dir, exist_ok=True)

    paths = {}

    # Fit CSV
    csv_path = os.path.join(csv_dir, f"{tag}_fit.csv")
    save_fit_csv(csv_path, x_mix, y_excess, y_fitted, residuals,
                 rk_coeffs, rk_order, r_squared, rmse,
                 x_label=x_label, y_label=y_label, metadata=metadata)
    paths["fit_csv"] = csv_path

    # Excess CSV
    excess_csv = os.path.join(csv_dir, f"{tag}_excess.csv")
    save_excess_csv(excess_csv, x_mix, y_excess + y_fitted,
                    np.zeros_like(y_excess) + y_fitted,
                    y_excess, x_label=x_label, y_label=y_label)
    paths["excess_csv"] = excess_csv

    # Topology from smooth RK curve
    x_smooth = np.linspace(0.001, 0.999, 200)
    y_smooth = eval_redlich_kister(x_smooth, rk_coeffs)

    hull_info = compute_convex_hull(x_smooth, y_smooth)
    hull_n = hull_info.get("n_hull_points", 0) if "error" not in hull_info else 0
    hull_area = hull_info.get("area", 0.0) if "error" not in hull_info else 0.0

    topo = extract_topology_points(x_smooth, y_smooth, n=20)
    topo_path = os.path.join(topo_dir, f"{tag}_topology.csv")
    topology_to_csv(topo_path, topo, x_label=x_label, y_label=y_label)
    paths["topo_csv"] = topo_path

    return {
        "paths": paths,
        "hull_vertices": hull_n,
        "hull_area": hull_area,
        "topo_n_points": topo["n_points"],
    }


# ═══════════════════════════════════════════════════════════════
#  Single-group RK fit
# ═══════════════════════════════════════════════════════════════

def run_rk_fit_single(
    *,
    x_mix: np.ndarray,
    y_excess: np.ndarray,
    tag: str,
    x_label: str = "x1",
    y_label: str = "Y_excess",
    max_order: int = 5,
    plot_dir: str = ".",
    csv_dir: str = ".",
    topo_dir: str = ".",
    metadata: Optional[dict] = None,
) -> Dict[str, Any]:
    """Fit RK to excess data for a single condition group.

    Returns dict with rk_result, paths, hull_info.
    """
    os.makedirs(plot_dir, exist_ok=True)

    rk = auto_fit_redlich_kister(x_mix, y_excess, max_order=max_order)
    if "error" in rk:
        return {"error": rk["error"]}

    # Save CSV + topology
    topo_info = _save_topo_and_csv(
        tag, x_mix, y_excess,
        np.array(rk["y_fitted"]), np.array(rk["residuals"]),
        rk["coeffs"], rk["selected_order"],
        rk["r_squared"], rk["rmse"],
        csv_dir, topo_dir,
        x_label=x_label, y_label=y_label, metadata=metadata,
    )

    return {
        "rk_result": rk,
        **topo_info,
    }


# ═══════════════════════════════════════════════════════════════
#  Multi-group RK fit (overview plot with baseline + excess)
# ═══════════════════════════════════════════════════════════════

def run_rk_fit_multi_group(
    *,
    x_by_group: Dict[Any, np.ndarray],
    y_by_group: Dict[Any, np.ndarray],
    y_excess_by_group: Dict[Any, np.ndarray],
    y_ideal_by_group: Dict[Any, np.ndarray],
    group_labels: Dict[Any, str],
    group_file_tags: Dict[Any, str],
    comp_in_col: str,
    other_comp: str,
    property_type: str,
    mixing_rule: str,
    tag: str,
    max_order: int = 5,
    plot_dir: str = ".",
    csv_dir: str = ".",
    topo_dir: str = ".",
    max_groups_plotted: int = 3,
) -> Dict[str, Any]:
    """Full pipeline: baseline + RK + CSV + topology for multiple condition groups.

    Produces:
      - Overview plot (up to max_groups_plotted columns): top=raw+ideal, bottom=RK fit
      - Per-group CSV (fit, excess, baseline, topology)
      - Coeff-vs-group plot if >1 group

    Returns dict: group_key → per-group result dict, plus "overview_plot" path.
    """
    os.makedirs(plot_dir, exist_ok=True)
    os.makedirs(csv_dir, exist_ok=True)
    os.makedirs(topo_dir, exist_ok=True)

    groups = sorted(x_by_group.keys())
    plot_groups = groups[:max_groups_plotted]
    n_cols = max(len(plot_groups), 1)

    fig, axes = plt.subplots(2, n_cols, figsize=(6 * n_cols, 9), squeeze=False)

    results_by_group = {}
    rk_results_for_coeff_plot = {}

    for i, gk in enumerate(groups):
        x = x_by_group[gk]
        y = y_by_group[gk]
        y_exc = y_excess_by_group[gk]
        y_ideal = y_ideal_by_group[gk]
        gl = group_labels.get(gk, str(gk))
        ft = group_file_tags.get(gk, "")

        x_mix, y_mix = _filter_mixture(x, y_exc)
        if len(x_mix) < 3:
            results_by_group[gk] = {"error": f"only {len(x_mix)} mixture points"}
            continue

        rk = auto_fit_redlich_kister(x_mix, y_mix, max_order=max_order)
        if "error" in rk:
            results_by_group[gk] = {"error": rk["error"]}
            continue

        rk_results_for_coeff_plot[gk] = rk

        # CSV + topology
        sub_tag = f"{tag}{ft}"
        topo_info = _save_topo_and_csv(
            sub_tag, x_mix, y_mix,
            np.array(rk["y_fitted"]), np.array(rk["residuals"]),
            rk["coeffs"], rk["selected_order"],
            rk["r_squared"], rk["rmse"],
            csv_dir, topo_dir,
            x_label=f"x({comp_in_col})",
            y_label=f"{property_type}_excess",
            metadata={"system": f"{other_comp} + {comp_in_col}",
                      "condition": gl,
                      "property": property_type,
                      "mixing_rule": mixing_rule},
        )

        # Baseline CSV
        bl_csv = os.path.join(csv_dir, f"{sub_tag}_baseline.csv")
        save_baseline_csv(bl_csv, x, y, y_ideal,
                          x_label=f"x({comp_in_col})", y_label=property_type)

        results_by_group[gk] = {
            "rk_result": rk,
            **topo_info,
            "baseline_csv": bl_csv,
        }

        # ── Plot (only first max_groups_plotted) ──
        if i < n_cols:
            # Top: raw + ideal
            ax_top = axes[0, i]
            ax_top.plot(x, y, "ko-", ms=3, label="Experimental")
            ax_top.plot(x, y_ideal, "r--", lw=2, label=f"Ideal ({mixing_rule})")
            ax_top.set_xlabel(f"x({comp_in_col})")
            ax_top.set_ylabel(property_type)
            ax_top.set_title(gl)
            ax_top.legend(fontsize=8)
            ax_top.grid(True, alpha=0.3)

            # Bottom: excess + RK
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

    label = tag.replace("_", " ").title()
    fig.suptitle(label, y=1.02, fontsize=13)
    fig.tight_layout()
    overview_path = os.path.join(plot_dir, f"{tag}_overview.png")
    fig.savefig(overview_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

    # CSV companion for overview plot
    overview_csv = os.path.join(csv_dir, f"{tag}_overview_plotdata.csv")
    with open(overview_csv, "w", newline="", encoding="utf-8") as f:
        w = _csv.writer(f)
        w.writerow(["condition", f"x({comp_in_col})", f"{property_type}_exp",
                     f"{property_type}_ideal", f"{property_type}_excess",
                     "rk_order", "r_squared"])
        for gk in groups:
            r = results_by_group.get(gk, {})
            if "error" in r:
                continue
            rk = r["rk_result"]
            gl = group_labels.get(gk, str(gk))
            x = x_by_group[gk]
            y = y_by_group[gk]
            y_ideal = y_ideal_by_group[gk]
            y_exc = y_excess_by_group[gk]
            for j in range(len(x)):
                w.writerow([gl, f"{x[j]:.8f}", f"{y[j]:.8g}",
                            f"{y_ideal[j]:.8g}", f"{y_exc[j]:.8g}",
                            rk["selected_order"], f"{rk['r_squared']:.8f}"])

    # ── Coeff-vs-group plot ──
    coeff_plot_path = None
    if len(rk_results_for_coeff_plot) > 1:
        coeff_plot_path = _plot_coeffs_vs_group(
            rk_results_for_coeff_plot, groups, group_labels,
            tag, plot_dir, csv_dir, comp_in_col, property_type,
        )

    return {
        "by_group": results_by_group,
        "overview_plot": overview_path,
        "overview_csv": overview_csv,
        "coeff_plot": coeff_plot_path,
    }


def _plot_coeffs_vs_group(rk_results, groups, group_labels,
                           tag, plot_dir, csv_dir, comp_in_col, property_type):
    """Plot RK coefficients vs condition group (typically temperature)."""
    # Try to extract numeric temperature for x-axis, otherwise use group index
    temps = []
    for gk in groups:
        if isinstance(gk, (int, float)):
            temps.append(gk)
        elif isinstance(gk, tuple) and len(gk) >= 1:
            temps.append(gk[0])
        else:
            temps.append(float(groups.index(gk)))
    x_axis = temps

    max_n = max((r["selected_order"] for r in rk_results.values()), default=0)
    fig, ax = plt.subplots(figsize=(7, 5))
    coeff_data = {}
    for k in range(max_n + 1):
        vals = []
        for gk in groups:
            r = rk_results.get(gk)
            if r and k < len(r["coeffs"]):
                vals.append(r["coeffs"][k])
            else:
                vals.append(np.nan)
        coeff_data[f"A{k}"] = vals
        ax.plot(x_axis, vals, "o-", ms=6, label=f"A{k}")

    x_label = "Temperature (K)"  # default assumption
    if any("pressure" in str(gk) for gk in group_labels.values()):
        x_label = "Condition group"
    ax.set_xlabel(x_label)
    ylabel = f"RK coefficient"
    if "density" in property_type:
        ylabel += " (kg/m³)"
    ax.set_ylabel(ylabel)
    ax.set_title(f"RK coefficients vs. {x_label.split('(')[0].strip()} — "
                 f"{tag.replace('_', ' ').title()}")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    path = os.path.join(plot_dir, f"{tag}_RK_coeffs_vs_group.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)

    # CSV companion
    csv_path = os.path.join(csv_dir, f"{tag}_RK_coeffs_vs_group.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = _csv.writer(f)
        header = ["condition", x_label] + [f"A{k}" for k in range(max_n + 1)] + ["order", "R2"]
        w.writerow(header)
        for i, gk in enumerate(groups):
            r = rk_results.get(gk)
            row = [group_labels.get(gk, str(gk)), f"{x_axis[i]:.4f}"]
            for k in range(max_n + 1):
                row.append(f"{coeff_data[f'A{k}'][i]:.10g}"
                           if not np.isnan(coeff_data[f"A{k}"][i]) else "")
            row.append(str(r["selected_order"]) if r else "")
            row.append(f"{r['r_squared']:.8f}" if r else "")
            w.writerow(row)

    return path


# ═══════════════════════════════════════════════════════════════
#  BIC order-selection diagnostic
# ═══════════════════════════════════════════════════════════════

def plot_bic_diagnostic(
    rk_result: dict,
    label: str,
    plot_path: str,
    csv_dir: str = ".",
) -> Optional[str]:
    """BIC vs order + R² vs order side-by-side plot.

    Returns plot path or None if not enough orders.
    """
    orders_info = rk_result.get("all_orders", [])
    if len(orders_info) < 2:
        return None

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    orders = [o["order"] for o in orders_info]
    bics = [o["bic"] for o in orders_info]
    r2s = [o["r_squared"] for o in orders_info]
    best = rk_result["selected_order"]

    ax1.plot(orders, bics, "bo-", ms=8)
    ax1.plot(best, bics[best], "r*", ms=16)
    ax1.set_xlabel("RK Order"); ax1.set_ylabel("BIC")
    ax1.set_title(f"{label} — BIC vs Order")
    ax1.grid(True, alpha=0.3)

    ax2.plot(orders, r2s, "gs-", ms=8)
    ax2.plot(best, r2s[best], "r*", ms=16)
    ax2.set_xlabel("RK Order"); ax2.set_ylabel("R²")
    ax2.set_title(f"{label} — R² vs Order")
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    os.makedirs(os.path.dirname(plot_path) or ".", exist_ok=True)
    fig.savefig(plot_path, dpi=150)
    plt.close(fig)

    # CSV companion
    base, ext = os.path.splitext(plot_path)
    csv_path = base + ".csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = _csv.writer(f)
        w.writerow(["order", "BIC", "R_squared", "RMSE", "is_best"])
        for o in orders_info:
            w.writerow([o["order"], f"{o['bic']:.6f}", f"{o['r_squared']:.8f}",
                        f"{o['rmse']:.8f}",
                        "yes" if o["order"] == best else ""])

    return plot_path


# ═══════════════════════════════════════════════════════════════
#  Multi-property RK (dual excess: linear + Arrhenius)
# ═══════════════════════════════════════════════════════════════

def run_multi_property_rk(
    *,
    dual_results: Dict[Any, Dict[str, Any]],
    group_labels: Dict[Any, str],
    comp_in_col: str,
    other_comp: str,
    tag: str,
    max_order: int = 4,
    plot_dir: str = ".",
    csv_dir: str = ".",
) -> Dict[str, Any]:
    """Fit RK to both linear- and Arrhenius-excess for viscosity.

    Returns dict with all_rk_results and plot paths.
    """
    os.makedirs(plot_dir, exist_ok=True)
    os.makedirs(csv_dir, exist_ok=True)

    groups = sorted(dual_results.keys())
    n_groups = max(len(groups), 1)

    fig, axes = plt.subplots(2, n_groups, figsize=(7 * n_groups, 10), squeeze=False)
    all_rk = {}

    for i, gk in enumerate(groups):
        d = dual_results[gk]
        if "error" in d:
            continue

        x = d["x"]
        y_exc_lin = d["y_excess_linear"]
        y_exc_arr = d["y_excess_arrhenius"]
        gl = group_labels.get(gk, str(gk))

        x_mix, y_lin_mix = _filter_mixture(x, y_exc_lin)
        _, y_arr_mix = _filter_mixture(x, y_exc_arr)

        rk_results = fit_multi_property(
            x_mix, {"linear": y_lin_mix, "arrhenius": y_arr_mix},
            max_order=max_order)
        all_rk[gk] = rk_results

        x_smooth = np.linspace(0.001, 0.999, 200)

        # Top: linear excess
        ax_lin = axes[0, i]
        res_lin = rk_results["linear"]
        if "error" not in res_lin:
            y_smooth_lin = eval_redlich_kister(x_smooth, res_lin["coeffs"])
            ax_lin.plot(x_mix, y_lin_mix * 1000, "bs", ms=5, label="Data (ηᴱ)")
            ax_lin.plot(x_smooth, y_smooth_lin * 1000, "b-", lw=2,
                        label=f"RK n={res_lin['selected_order']} "
                              f"(R²={res_lin['r_squared']:.4f})")
            ax_lin.axhline(0, color="gray", ls=":", lw=0.8)
            ax_lin.set_ylabel("ηᴱ (mPa·s)")
        ax_lin.set_xlabel(f"x({comp_in_col})")
        ax_lin.set_title(f"{gl} — Free-energy ideal excess")
        ax_lin.legend(fontsize=8); ax_lin.grid(True, alpha=0.3)

        # Bottom: Arrhenius excess
        ax_arr = axes[1, i]
        res_arr = rk_results["arrhenius"]
        if "error" not in res_arr:
            y_smooth_arr = eval_redlich_kister(x_smooth, res_arr["coeffs"])
            ax_arr.plot(x_mix, y_arr_mix, "r^", ms=5, label="Data (Δln η)")
            ax_arr.plot(x_smooth, y_smooth_arr, "r-", lw=2,
                        label=f"RK n={res_arr['selected_order']} "
                              f"(R²={res_arr['r_squared']:.4f})")
            ax_arr.axhline(0, color="gray", ls=":", lw=0.8)
            ax_arr.set_ylabel("Δln(η)")
        ax_arr.set_xlabel(f"x({comp_in_col})")
        ax_arr.set_title(f"{gl} — Activ.-energy ideal excess")
        ax_arr.legend(fontsize=8); ax_arr.grid(True, alpha=0.3)

    title = f"{other_comp.title()} + {comp_in_col.title()} — RK fits: Linear vs Arrhenius"
    fig.suptitle(title, y=1.02, fontsize=13)
    fig.tight_layout()
    fit_plot = os.path.join(plot_dir, f"{tag}_DUAL_RK_fits.png")
    fig.savefig(fit_plot, dpi=150, bbox_inches="tight")
    plt.close(fig)

    # CSV companion for dual RK plot
    dual_csv = os.path.join(csv_dir, f"{tag}_DUAL_RK_fits.csv")
    with open(dual_csv, "w", newline="", encoding="utf-8") as f:
        w = _csv.writer(f)
        w.writerow(["condition", "baseline_type", f"x({comp_in_col})",
                     "excess_data", "rk_order", "r_squared"])
        for gk in groups:
            gl = group_labels.get(gk, str(gk))
            rk_r = all_rk.get(gk, {})
            d = dual_results[gk]
            if "error" in d:
                continue
            x = d["x"]
            x_mix, y_lin = _filter_mixture(x, d["y_excess_linear"])
            _, y_arr = _filter_mixture(x, d["y_excess_arrhenius"])
            for label_type, ym, rk in [("linear", y_lin, rk_r.get("linear", {})),
                                        ("arrhenius", y_arr, rk_r.get("arrhenius", {}))]:
                if "error" in rk:
                    continue
                for j in range(len(x_mix)):
                    w.writerow([gl, label_type, f"{x_mix[j]:.8f}", f"{ym[j]:.8g}",
                                rk["selected_order"], f"{rk['r_squared']:.8f}"])

    # Coeff-vs-group plot (if multi-group)
    coeff_plot = None
    if len(groups) > 1:
        coeff_plot = _plot_dual_coeffs_vs_group(
            all_rk, groups, group_labels, tag, plot_dir, csv_dir)

    return {
        "all_rk": all_rk,
        "fit_plot": fit_plot,
        "dual_csv": dual_csv,
        "coeff_plot": coeff_plot,
    }


def _plot_dual_coeffs_vs_group(all_rk, groups, group_labels, tag, plot_dir, csv_dir):
    """Coefficient-vs-group for both linear and Arrhenius excess."""
    temps = []
    for gk in groups:
        if isinstance(gk, (int, float)):
            temps.append(gk)
        elif isinstance(gk, tuple):
            temps.append(gk[0])
        else:
            temps.append(float(groups.index(gk)))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    csv_rows = []

    for rule, ax, title in [
        ("linear", ax1, "Free-energy ideal (ηᴱ)"),
        ("arrhenius", ax2, "Activ.-energy ideal (Δln η)"),
    ]:
        max_n = max(
            (all_rk[gk][rule].get("selected_order", 0)
             for gk in groups if gk in all_rk and "error" not in all_rk[gk].get(rule, {})),
            default=0)
        for k in range(max_n + 1):
            vals = []
            for gk in groups:
                rk_r = all_rk.get(gk, {}).get(rule, {})
                if "error" not in rk_r and k < len(rk_r.get("coeffs", [])):
                    vals.append(rk_r["coeffs"][k])
                else:
                    vals.append(np.nan)
            ax.plot(temps, vals, "o-", ms=6, label=f"A{k}")
            for j, gk in enumerate(groups):
                csv_rows.append([group_labels.get(gk, str(gk)), rule,
                                 f"A{k}", f"{temps[j]:.4f}",
                                 f"{vals[j]:.10g}" if not np.isnan(vals[j]) else ""])
        ax.set_xlabel("Temperature (K)")
        ax.set_ylabel("RK coefficient")
        ax.set_title(f"RK coeffs vs T — {title}")
        ax.legend(); ax.grid(True, alpha=0.3)

    fig.tight_layout()
    path = os.path.join(plot_dir, f"{tag}_DUAL_coeffs_vs_T.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)

    # CSV
    csv_path = os.path.join(csv_dir, f"{tag}_DUAL_coeffs_vs_T.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = _csv.writer(f)
        w.writerow(["condition", "baseline_type", "coefficient", "temperature_K", "value"])
        w.writerows(csv_rows)

    return path
