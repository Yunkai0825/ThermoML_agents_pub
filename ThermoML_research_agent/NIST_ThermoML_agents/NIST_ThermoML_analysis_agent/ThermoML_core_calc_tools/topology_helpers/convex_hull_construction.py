"""
convex_hull_construction — Edge detection via 2-D convex hull.
================================================================
Uses ``scipy.spatial.ConvexHull`` to find the boundary (edge) points
of a 2-D point cloud (x, y).  These are the points that lie on the
convex hull of the data — the outermost "envelope" of the curve.

For thermodynamic property curves this is a robust way to locate
edge points (near x=0 and x=1), extremal-y points, and any points
that bulge beyond a simple linear interpolation.

Public API
----------
- compute_convex_hull(x, y)           → dict
- hull_edge_indices(x, y)             → list[int]
- select_hull_edge_points(x, y, n=6)  → dict
"""

from __future__ import annotations

from typing import List, Optional

import numpy as np
from scipy.spatial import ConvexHull


def compute_convex_hull(
    x: np.ndarray | List[float],
    y: np.ndarray | List[float],
) -> dict:
    """Compute the 2-D convex hull of the (x, y) point cloud.

    Parameters
    ----------
    x, y : array-like
        1-D coordinate arrays (same length).

    Returns
    -------
    dict
        {
            "hull_indices":   list[int],   # indices of hull vertices (sorted by x)
            "hull_x":         list[float], # x-values on hull
            "hull_y":         list[float], # y-values on hull
            "n_hull_points":  int,
            "n_source_points": int,
            "area":           float,       # hull area (useful for excess-property magnitude)
        }
        On error (e.g. < 3 points, collinear), returns {"error": str}.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if len(x) != len(y):
        return {"error": f"x ({len(x)}) and y ({len(y)}) length mismatch"}
    if len(x) < 3:
        return {"error": f"Need at least 3 points for a convex hull, got {len(x)}"}

    # Stack into (N, 2) for ConvexHull
    points = np.column_stack([x, y])

    try:
        hull = ConvexHull(points)
    except Exception as e:
        return {"error": f"ConvexHull failed: {e}"}

    # Hull vertices — sorted by x for reproducibility
    vi = hull.vertices
    order = np.argsort(x[vi])
    vi_sorted = vi[order]

    return {
        "hull_indices": vi_sorted.tolist(),
        "hull_x": x[vi_sorted].tolist(),
        "hull_y": y[vi_sorted].tolist(),
        "n_hull_points": len(vi_sorted),
        "n_source_points": len(x),
        "area": float(hull.volume),  # 2-D hull: volume = area
    }


def hull_edge_indices(
    x: np.ndarray | List[float],
    y: np.ndarray | List[float],
) -> List[int]:
    """Return the indices of all convex-hull vertices, sorted by x.

    Convenience wrapper for ``compute_convex_hull``.
    Returns empty list on error.
    """
    result = compute_convex_hull(x, y)
    if "error" in result:
        return []
    return result["hull_indices"]


def select_hull_edge_points(
    x: np.ndarray | List[float],
    y: np.ndarray | List[float],
    n: int = 6,
    *,
    prioritize_x_extremes: bool = True,
    prioritize_y_extremes: bool = True,
) -> dict:
    """Select up to *n* representative edge points from the convex hull.

    Selection priority:
      1. x-boundary points (min-x and max-x hull vertices)
      2. y-boundary points (min-y and max-y hull vertices)
      3. Maximum-deviation points: hull vertices farthest from
         the line connecting the two x-extreme hull points
      4. Remaining budget filled with equispaced hull vertices

    Parameters
    ----------
    x, y : array-like
        Source data.
    n : int
        Maximum number of edge points to return (default 6).
    prioritize_x_extremes : bool
        Force-include the leftmost and rightmost hull vertices.
    prioritize_y_extremes : bool
        Force-include the topmost and bottommost hull vertices.

    Returns
    -------
    dict
        {
            "edge_indices": list[int],  # indices into original arrays
            "edge_x":       list[float],
            "edge_y":       list[float],
            "edge_labels":  list[str],  # "x_min"/"x_max"/"y_min"/"y_max"/"deviation"/"fill"
            "n_edge_points": int,
            "hull_area":    float,
        }
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    hull_result = compute_convex_hull(x, y)
    if "error" in hull_result:
        # Fallback: just return first and last by x
        order = np.argsort(x)
        sel = [int(order[0]), int(order[-1])]
        return {
            "edge_indices": sel,
            "edge_x": x[sel].tolist(),
            "edge_y": y[sel].tolist(),
            "edge_labels": ["x_min", "x_max"],
            "n_edge_points": 2,
            "hull_area": 0.0,
        }

    hi = np.array(hull_result["hull_indices"])
    hx = x[hi]
    hy = y[hi]

    selected: List[int] = []  # indices into *original* arrays
    labels: List[str] = []
    used = set()

    def _add(orig_idx: int, label: str):
        if orig_idx not in used and len(selected) < n:
            selected.append(orig_idx)
            labels.append(label)
            used.add(orig_idx)

    # 1. x-extreme hull vertices
    if prioritize_x_extremes:
        _add(int(hi[np.argmin(hx)]), "x_min")
        _add(int(hi[np.argmax(hx)]), "x_max")

    # 2. y-extreme hull vertices
    if prioritize_y_extremes:
        _add(int(hi[np.argmin(hy)]), "y_min")
        _add(int(hi[np.argmax(hy)]), "y_max")

    # 3. Maximum-deviation points from the baseline (x_min→x_max line)
    if len(hi) > 2:
        # Build the line from x_min to x_max on the hull
        i_xmin = int(np.argmin(hx))
        i_xmax = int(np.argmax(hx))
        x0, y0 = hx[i_xmin], hy[i_xmin]
        x1, y1 = hx[i_xmax], hy[i_xmax]
        dx = x1 - x0
        dy = y1 - y0
        line_len = np.sqrt(dx**2 + dy**2)
        if line_len > 0:
            # Perpendicular distance of each hull vertex from the line
            dist = np.abs(dy * (hx - x0) - dx * (hy - y0)) / line_len
            # Sort hull vertices by distance, descending
            dev_order = np.argsort(-dist)
            n_dev = max(1, (n - len(used)) // 2)
            for idx in dev_order:
                if len(used) >= n:
                    break
                _add(int(hi[idx]), "deviation")
                if sum(1 for l in labels if l == "deviation") >= n_dev:
                    break

    # 4. Fill remaining budget with equispaced hull vertices
    remaining = n - len(used)
    if remaining > 0 and len(hi) > len(used):
        step = max(1, len(hi) // (remaining + 1))
        for j in range(0, len(hi), step):
            if len(used) >= n:
                break
            _add(int(hi[j]), "fill")

    # Sort selected by x
    sel_arr = np.array(selected)
    sort_order = np.argsort(x[sel_arr])
    selected = sel_arr[sort_order].tolist()
    labels = [labels[sort_order[j]] for j in range(len(sort_order))]

    return {
        "edge_indices": selected,
        "edge_x": x[np.array(selected)].tolist(),
        "edge_y": y[np.array(selected)].tolist(),
        "edge_labels": labels,
        "n_edge_points": len(selected),
        "hull_area": hull_result["area"],
    }
