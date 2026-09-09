"""
plot_export — Generate RK fit plots and residual plots.
========================================================
Uses matplotlib Agg backend (no GUI required).  All functions return
the path of the saved PNG so callers can register it.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import List, Optional, Sequence

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

log = logging.getLogger("PLOT-EXPORT")


def _draw_annotation(fig, annotation: str) -> None:
    """Footnote box under the figure; bbox_inches='tight' includes it."""
    fig.text(
        0.02, -0.02, annotation,
        fontsize=6.5, family="monospace", va="top", ha="left",
        linespacing=1.4,
        bbox=dict(boxstyle="round,pad=0.45", facecolor="#f8f8f4",
                  edgecolor="#888888", linewidth=0.6),
    )


def build_rk_annotation(
    rk: dict,
    *,
    mixing_rule: str = "linear",
    components: Optional[List[str]] = None,
    block_metadata: Optional[dict] = None,
    temperature_K: Optional[float] = None,
    n_points: Optional[int] = None,
    y_column: str = "",
) -> str:
    """Multi-line legend text: fitted RK equation + raw-block metadata.

    Pure text assembly (no I/O, no mathtext) — callers render it on the
    saved plots.  Every metadata field is optional; missing pieces are
    silently skipped so a partial block card still yields a legend.
    """
    sup = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    lines: list[str] = []

    coeffs = [float(c) for c in (rk or {}).get("coeffs", [])]
    if coeffs:
        terms = []
        for k, c in enumerate(coeffs):
            power = "" if k == 0 else (
                "·d" if k == 1 else f"·d{str(k).translate(sup)}")
            terms.append(f"{c:+.5g}{power}")
        if mixing_rule == "arrhenius":
            lhs = "ln Y = x₁·ln Y₁ + x₂·ln Y₂ + x₁x₂·P(d)"
        elif mixing_rule == "linear":
            lhs = "Y = x₁·Y₁ + x₂·Y₂ + x₁x₂·P(d)"
        else:
            lhs = f"Y_excess [{mixing_rule}] = x₁x₂·P(d)"
        lines.append(f"RK fit: {lhs}")
        lines.append(f"P(d) = {' '.join(terms)}    (d = x₁ − x₂)")

    stats = []
    if (rk or {}).get("selected_order") is not None:
        stats.append(f"order {rk['selected_order']} (BIC)")
    if (rk or {}).get("r_squared") is not None:
        stats.append(f"R² = {rk['r_squared']:.6g}")
    if (rk or {}).get("rmse") is not None:
        stats.append(f"RMSE = {rk['rmse']:.4g}")
    if n_points:
        stats.append(f"n = {n_points}")
    if temperature_K is not None:
        stats.append(f"fit slice T = {temperature_K:.2f} K")
    if stats:
        lines.append(" | ".join(stats))
    if components and len(components) >= 2:
        lines.append(f"x₁ = x({components[0]}), x₂ = x({components[1]})")

    meta = block_metadata or {}
    if meta:
        comps = [c for c in (meta.get("compounds") or [])
                 if isinstance(c, dict)]
        comp_txt = " + ".join(
            f"{c.get('name', '?')} ({c['formula']})"
            if c.get("formula") else str(c.get("name", "?"))
            for c in comps
        )
        head = " ".join(
            bit for bit in (
                str(meta.get("system_type")
                    or meta.get("declared_system_type") or "").strip(),
                str(meta.get("block_type") or "").strip(),
            ) if bit
        )
        line = ""
        if head or comp_txt:
            line = f"block: {head}" if head else "block:"
            if comp_txt:
                line += f" — {comp_txt}"
            if meta.get("n_datapoints"):
                line += f", {meta['n_datapoints']} rows"
            lines.append(line)
        solvents = meta.get("solvents") or []
        if solvents:
            lines.append("solvent: " + ", ".join(
                s.get("name", str(s)) if isinstance(s, dict) else str(s)
                for s in solvents
            ))
        props = [p for p in (meta.get("properties") or [])
                 if isinstance(p, dict)]
        prop = next(
            (p for p in props if p.get("column_name") == y_column), None,
        ) or (props[0] if props else None)
        if prop:
            bits = []
            if prop.get("prop_ID"):
                bits.append(f"property: {prop['prop_ID']}")
            if prop.get("meas_ID"):
                method = str(prop["meas_ID"])
                if prop.get("meas_num_id"):
                    method += f" [{prop['meas_num_id']}]"
                bits.append(f"method: {method}")
            if bits:
                lines.append(" | ".join(bits))
        constraints = [c for c in (meta.get("constraints") or [])
                       if isinstance(c, dict)]
        if constraints:
            parts = []
            for c in constraints:
                name = c.get("constr_id") or c.get("column_name") or "?"
                value = c.get("value")
                text = (f"{name} = {value:g}"
                        if isinstance(value, (int, float)) else
                        f"{name} = {value}")
                if c.get("compound"):
                    text += f" ({c['compound']})"
                parts.append(text)
            lines.append("block constraints: " + "; ".join(parts))

    return "\n".join(line[:150] for line in lines if line.strip())


def save_fit_plot(
    path: str | Path,
    x_mix: np.ndarray | Sequence[float],
    y_exp: np.ndarray | Sequence[float],
    y_ideal: np.ndarray | Sequence[float],
    y_fitted_total: np.ndarray | Sequence[float],
    *,
    x_label: str = "x₁",
    y_label: str = "Y",
    title: str = "Redlich-Kister Fit",
    mixing_rule: str = "linear",
    rk_order: Optional[int] = None,
    r_squared: Optional[float] = None,
    components: Optional[List[str]] = None,
    fit_curve_x: Optional[np.ndarray | Sequence[float]] = None,
    fit_curve_y: Optional[np.ndarray | Sequence[float]] = None,
    ideal_curve_x: Optional[np.ndarray | Sequence[float]] = None,
    ideal_curve_y: Optional[np.ndarray | Sequence[float]] = None,
    pure_points: Optional[Sequence[tuple]] = None,
    pure_points_label: str = "",
    annotation: Optional[str] = None,
) -> str:
    """Save a 2-panel plot: (top) fit overview, (bottom) residuals.

    Parameters
    ----------
    x_mix : array
        Composition values (mole fraction).
    y_exp : array
        Experimental property values at mixture compositions.
    y_ideal : array
        Ideal-mixture baseline values at the same compositions.
    y_fitted_total : array
        RK-predicted total values = y_ideal + y_excess_fitted.
    pure_points : sequence of (x, y) tuples, optional
        Pure-component reference values anchoring the ideal baseline
        (typically at x=0 and x=1).  Drawn as open diamonds.
    pure_points_label : str, optional
        Provenance tag shown in the legend (e.g. "named",
        "unit-converted", "block edges").
    """
    x = np.asarray(x_mix, dtype=float)
    ye = np.asarray(y_exp, dtype=float)
    yi = np.asarray(y_ideal, dtype=float)
    yf = np.asarray(y_fitted_total, dtype=float)
    residuals = ye - yf

    sort_idx = np.argsort(x)
    x, ye, yi, yf, residuals = x[sort_idx], ye[sort_idx], yi[sort_idx], yf[sort_idx], residuals[sort_idx]

    def _sorted_curve(
        curve_x: Optional[np.ndarray | Sequence[float]],
        curve_y: Optional[np.ndarray | Sequence[float]],
    ) -> tuple[np.ndarray, np.ndarray] | None:
        if curve_x is None or curve_y is None:
            return None
        cx = np.asarray(curve_x, dtype=float)
        cy = np.asarray(curve_y, dtype=float)
        if cx.shape != cy.shape or cx.ndim != 1 or cx.size < 2:
            return None
        valid = np.isfinite(cx) & np.isfinite(cy)
        if np.count_nonzero(valid) < 2:
            return None
        cx, cy = cx[valid], cy[valid]
        order = np.argsort(cx)
        return cx[order], cy[order]

    ideal_curve = _sorted_curve(ideal_curve_x, ideal_curve_y)
    fit_curve = _sorted_curve(fit_curve_x, fit_curve_y)

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(7, 6), height_ratios=[3, 1],
        sharex=True,
    )
    fig.subplots_adjust(hspace=0.08)

    # ── Top panel: data + ideal + fitted ─────────────────────
    ax1.scatter(x, ye, s=30, c="steelblue", zorder=3, label="Experimental")
    if ideal_curve is not None:
        ix, iy = ideal_curve
        ax1.plot(ix, iy, "--", color="gray", linewidth=1.2, label=f"Ideal ({mixing_rule})")
    else:
        ax1.plot(x, yi, "--", color="gray", linewidth=1.2, label=f"Ideal ({mixing_rule})")
    if fit_curve is not None:
        fx, fy = fit_curve
        ax1.plot(fx, fy, "-", color="crimson", linewidth=1.8, label="RK fit")
    else:
        ax1.plot(x, yf, "-", color="crimson", linewidth=1.8, label="RK fit")
    if pure_points:
        pts = [
            (float(p[0]), float(p[1])) for p in pure_points
            if len(p) >= 2 and np.isfinite(p[0]) and np.isfinite(p[1])
        ]
        if pts:
            tag = pure_points_label or "x=0, x=1"
            ax1.scatter(
                [p[0] for p in pts], [p[1] for p in pts],
                marker="D", s=60, facecolors="white", edgecolors="black",
                linewidths=1.2, zorder=4, label=f"Pure refs ({tag})",
            )
    ax1.set_ylabel(y_label)
    ax1.legend(fontsize=8, loc="best")

    title_parts = [title]
    if rk_order is not None:
        title_parts.append(f"order {rk_order}")
    if r_squared is not None:
        title_parts.append(f"R²={r_squared:.6f}")
    ax1.set_title("  |  ".join(title_parts), fontsize=10)
    ax1.grid(True, alpha=0.3)

    # ── Bottom panel: residuals ──────────────────────────────
    ax2.stem(x, residuals, linefmt="C0-", markerfmt="C0o", basefmt="k-")
    ax2.axhline(0, color="black", linewidth=0.5)
    ax2.set_xlabel(x_label if not components else f"x({components[0]})")
    ax2.set_ylabel("Residual")
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    if annotation:
        _draw_annotation(fig, annotation)
    logical_path = Path(path)
    ensure_directory(logical_path.parent)
    fig.savefig(str(_filesystem_path(logical_path)), dpi=150, bbox_inches="tight")
    plt.close(fig)
    log.info("Saved fit plot: %s", path)
    return str(path)


def save_excess_plot(
    path: str | Path,
    x_mix: np.ndarray | Sequence[float],
    y_excess: np.ndarray | Sequence[float],
    y_excess_fitted: np.ndarray | Sequence[float],
    *,
    x_label: str = "x₁",
    y_label: str = "Y_excess",
    title: str = "Excess Property",
    rk_order: Optional[int] = None,
    r_squared: Optional[float] = None,
    components: Optional[List[str]] = None,
    fit_curve_x: Optional[np.ndarray | Sequence[float]] = None,
    fit_curve_y: Optional[np.ndarray | Sequence[float]] = None,
    annotation: Optional[str] = None,
) -> str:
    """Save a plot of excess property: experimental vs RK-fitted curve."""
    x = np.asarray(x_mix, dtype=float)
    ye = np.asarray(y_excess, dtype=float)
    yf = np.asarray(y_excess_fitted, dtype=float)

    sort_idx = np.argsort(x)
    x, ye, yf = x[sort_idx], ye[sort_idx], yf[sort_idx]

    fit_curve = None
    if fit_curve_x is not None and fit_curve_y is not None:
        cx = np.asarray(fit_curve_x, dtype=float)
        cy = np.asarray(fit_curve_y, dtype=float)
        if cx.shape == cy.shape and cx.ndim == 1 and cx.size >= 2:
            valid = np.isfinite(cx) & np.isfinite(cy)
            if np.count_nonzero(valid) >= 2:
                cx, cy = cx[valid], cy[valid]
                order = np.argsort(cx)
                fit_curve = (cx[order], cy[order])

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.scatter(x, ye, s=30, c="steelblue", zorder=3, label="Excess (data)")
    if fit_curve is not None:
        fx, fy = fit_curve
        ax.plot(fx, fy, "-", color="crimson", linewidth=1.8, label="RK fit")
    else:
        ax.plot(x, yf, "-", color="crimson", linewidth=1.8, label="RK fit")
    ax.axhline(0, color="black", linewidth=0.5, alpha=0.5)
    ax.set_xlabel(x_label if not components else f"x({components[0]})")
    ax.set_ylabel(y_label)

    title_parts = [title]
    if rk_order is not None:
        title_parts.append(f"order {rk_order}")
    if r_squared is not None:
        title_parts.append(f"R²={r_squared:.6f}")
    ax.set_title("  |  ".join(title_parts), fontsize=10)
    ax.legend(fontsize=8, loc="best")
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    if annotation:
        _draw_annotation(fig, annotation)
    logical_path = Path(path)
    ensure_directory(logical_path.parent)
    fig.savefig(str(_filesystem_path(logical_path)), dpi=150, bbox_inches="tight")
    plt.close(fig)
    log.info("Saved excess plot: %s", path)
    return str(path)
from ....general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers.session_manager_output_storage import (
    _filesystem_path,
    ensure_directory,
)
