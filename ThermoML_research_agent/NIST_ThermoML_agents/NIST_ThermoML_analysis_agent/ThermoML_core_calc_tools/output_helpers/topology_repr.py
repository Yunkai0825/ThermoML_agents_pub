"""
topology_repr — Compact topological curve representation.
==========================================================
Represents a fitted curve using a small set of *representative points*
that capture its essential shape:

  1. **Edges** — the two boundary points (x=0, x=1 or x_min, x_max).
  2. **Extrema** — local minima and maxima of the curve.
  3. **Maximum-variance points** — points where the second derivative
     (curvature) is largest, i.e. where the curve changes shape fastest.
  4. **Uniform fill** — remaining budget filled with equispaced points
     so no large gaps remain.

The result is a compact (n_points × 2) representation suitable for
database storage, quick plotting, and similarity comparison.

Public API
----------
- extract_topology_points(x, y, n=20) → dict
- topology_to_csv(path, topo_dict)     → str
"""

from __future__ import annotations

import csv
import os
from typing import Any, Dict, List, Optional

import numpy as np

# Import convex hull — try relative first, then absolute (for standalone use)
try:
    from ..topology_helpers.convex_hull_construction import (
        hull_edge_indices,
        select_hull_edge_points,
    )
except ImportError:
    from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.topology_helpers.convex_hull_construction import (
        hull_edge_indices,
        select_hull_edge_points,
    )


def extract_topology_points(
    x: np.ndarray | List[float],
    y: np.ndarray | List[float],
    n: int = 20,
    *,
    include_edges: bool = True,
    include_extrema: bool = True,
    include_max_curvature: bool = True,
    n_hull_edges: int = 6,
) -> dict:
    """Extract n representative topology points from a curve.

    The algorithm selects points in priority order:
      1. **Convex-hull edge points** — vertices of the 2-D convex hull
         of (x, y), which robustly capture the boundary of the curve
         (x-extremes, y-extremes, max-deviation from the baseline).
      2. **Extrema** — local minima and maxima of y.
      3. **Maximum-curvature points** — largest |y''|.
      4. **Uniform fill** — remaining budget with equispaced x samples,
         snapped to the nearest existing data point.

    Parameters
    ----------
    x, y : array-like
        1-D arrays defining the curve.  Need not be sorted.
    n : int
        Target number of representative points (default 20).
    include_edges : bool
        Whether to detect edge points via convex hull.
    include_extrema : bool
        Whether to include local extrema.
    include_max_curvature : bool
        Whether to include maximum-curvature points.
    n_hull_edges : int
        Number of convex-hull edge points to include (default 6).

    Returns
    -------
    dict
        {
            "x_topo": [...],          # n representative x values
            "y_topo": [...],          # corresponding y values
            "n_points": int,
            "point_labels": [...],    # "edge" / "extremum" / "curvature" / "fill"
            "n_source_points": int,   # original data length
            "hull_area": float,       # convex hull area (excess magnitude proxy)
        }
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if len(x) != len(y):
        return {"error": f"x ({len(x)}) and y ({len(y)}) length mismatch"}
    if len(x) == 0:
        return {"error": "Empty arrays"}
    if len(x) <= n:
        # Fewer points than budget — return all
        order = np.argsort(x)
        return {
            "x_topo": x[order].tolist(),
            "y_topo": y[order].tolist(),
            "n_points": len(x),
            "point_labels": ["all"] * len(x),
            "n_source_points": len(x),
            "hull_area": 0.0,
        }

    # Sort by x
    order = np.argsort(x)
    xs, ys = x[order], y[order]
    n_src = len(xs)

    selected_indices: List[int] = []   # indices into sorted arrays
    labels: List[str] = []
    used = set()
    hull_area = 0.0

    def _add(idx, label):
        if idx not in used and 0 <= idx < n_src:
            selected_indices.append(idx)
            labels.append(label)
            used.add(idx)

    # 1. Edge points via convex hull
    if include_edges:
        hull_result = select_hull_edge_points(
            xs, ys, n=min(n_hull_edges, n),
        )
        hull_area = hull_result.get("hull_area", 0.0)
        # Map hull edge indices (into xs/ys which are already sorted)
        for ei, lab in zip(hull_result["edge_indices"], hull_result["edge_labels"]):
            _add(int(ei), "edge")

    # 2. Extrema (local min/max)
    if include_extrema and n_src >= 3:
        dy = np.diff(ys)
        for i in range(len(dy) - 1):
            if len(used) >= n:
                break
            if dy[i] > 0 and dy[i + 1] < 0:       # local max
                _add(i + 1, "extremum")
            elif dy[i] < 0 and dy[i + 1] > 0:      # local min
                _add(i + 1, "extremum")

    # 3. Maximum-curvature points (largest |y''|)
    if include_max_curvature and n_src >= 3:
        dx = np.diff(xs)
        dx = np.where(dx == 0, 1e-30, dx)
        d2y = np.diff(ys, 2) / (dx[:-1] * dx[1:])
        abs_d2y = np.abs(d2y)

        n_curv = max(1, (n - len(used)) // 3)
        curv_order = np.argsort(-abs_d2y)
        for idx in curv_order[:n_curv * 3]:
            if len(used) >= n:
                break
            actual_idx = int(idx) + 1   # d2y is offset by 1
            _add(actual_idx, "curvature")
            if sum(1 for l in labels if l == "curvature") >= n_curv:
                break

    # 4. Fill remaining budget with equispaced samples
    remaining = n - len(used)
    if remaining > 0:
        fill_x = np.linspace(xs[0], xs[-1], remaining + 2)[1:-1]
        for fx in fill_x:
            if len(used) >= n:
                break
            idx = int(np.argmin(np.abs(xs - fx)))
            _add(idx, "fill")

    # If still short, add nearest-to-midpoints
    while len(used) < n and len(used) < n_src:
        for idx in range(n_src):
            if idx not in used:
                _add(idx, "fill")
                break

    # Sort selected by x
    si = np.array(selected_indices)
    sort_order = np.argsort(xs[si])
    si_sorted = si[sort_order]
    labels_sorted = [labels[sort_order[j]] for j in range(len(sort_order))]

    return {
        "x_topo": xs[si_sorted].tolist(),
        "y_topo": ys[si_sorted].tolist(),
        "n_points": len(si_sorted),
        "point_labels": labels_sorted,
        "n_source_points": n_src,
        "hull_area": hull_area,
    }


def topology_to_csv(
    path: str,
    topo: dict,
    *,
    x_label: str = "x",
    y_label: str = "y",
) -> str:
    """Write a topology representation to CSV.

    Columns: x, y, point_type
    A comment line at the top records hull_area and n_source_points.
    """
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        # Metadata comment
        hull_area = topo.get("hull_area", 0.0)
        f.write(f"# n_source_points={topo.get('n_source_points', '?')},"
                f" hull_area={hull_area:.6f}\n")
        w = csv.writer(f)
        w.writerow([x_label, y_label, "point_type"])
        for xi, yi, lab in zip(
            topo["x_topo"], topo["y_topo"], topo["point_labels"]
        ):
            w.writerow([f"{xi:.8f}", f"{yi:.8f}", lab])
    return path
