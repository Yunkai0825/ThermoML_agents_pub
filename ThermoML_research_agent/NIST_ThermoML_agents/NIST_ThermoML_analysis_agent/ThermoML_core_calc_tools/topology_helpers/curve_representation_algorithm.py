"""
curve_representation_algorithm — Compact topological curve description.
======================================================================
Orchestrates ``convex_hull_construction`` and ``topology_repr`` to
produce a minimal representation of a curve suitable for storage,
comparison, and fast re-plotting.

The resulting "topology card" contains:
  - n representative (x, y) points with labels (edge/extremum/curvature/fill)
  - Convex hull area (a scalar proxy for excess-property magnitude)
  - Source data statistics (n_source_points, x_range, y_range)

Public API
----------
- build_curve_topology(x, y, n=20) → dict
"""

from __future__ import annotations

from typing import Dict, List, Optional

import numpy as np

from .convex_hull_construction import compute_convex_hull, select_hull_edge_points

# Import sibling package — try relative, then absolute
try:
    from ..output_helpers.topology_repr import extract_topology_points
except ImportError:
    from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.output_helpers.topology_repr import (
        extract_topology_points,
    )


def build_curve_topology(
    x: np.ndarray | List[float],
    y: np.ndarray | List[float],
    n: int = 20,
    *,
    n_hull_edges: int = 6,
) -> dict:
    """Build a compact topological representation of a curve.

    Combines convex-hull edge detection with curvature and extrema
    analysis to select the most informative points.

    Parameters
    ----------
    x, y : array-like
        1-D arrays defining the curve.
    n : int
        Target number of representative points.
    n_hull_edges : int
        Number of convex-hull vertices to prioritize.

    Returns
    -------
    dict
        {
            "x_topo": list[float],
            "y_topo": list[float],
            "n_points": int,
            "point_labels": list[str],
            "n_source_points": int,
            "hull_area": float,
            "x_range": [float, float],
            "y_range": [float, float],
            "hull_vertices": int,
        }
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    # Core topology extraction (uses convex hull internally)
    topo = extract_topology_points(
        x, y, n=n,
        include_edges=True,
        include_extrema=True,
        include_max_curvature=True,
        n_hull_edges=n_hull_edges,
    )

    if "error" in topo:
        return topo

    # Add summary statistics
    hull = compute_convex_hull(x, y)
    topo["x_range"] = [float(np.nanmin(x)), float(np.nanmax(x))]
    topo["y_range"] = [float(np.nanmin(y)), float(np.nanmax(y))]
    topo["hull_vertices"] = hull.get("n_hull_points", 0) if "error" not in hull else 0

    return topo
