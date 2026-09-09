"""
Ramer-Douglas-Peucker (RDP) topology-based data-point compaction.

For every block the algorithm simplifies each (variables…, property) curve
by keeping only the points that define its shape — endpoints, extrema, and
significant curvature changes — discarding intermediate points that lie
close to the interpolated line.

Single-variable blocks produce a 2-D polyline (var, prop).  Multi-variable
blocks are sorted lexicographically by their variables, normalised to
[0, 1] per dimension, and simplified as an N-D polyline.

Public API
----------
compact_block_data(variables, properties, data_points, fraction=0.01)
    → dict with keys  topology, simplified_points, kept_indices
"""

import math


# ---------------------------------------------------------------------------
# RDP core
# ---------------------------------------------------------------------------

def _perp_dist(point, start, end):
    """Perpendicular distance from *point* to segment *start→end* (N-D)."""
    n = len(point)
    d = tuple(end[i] - start[i] for i in range(n))
    v = tuple(point[i] - start[i] for i in range(n))
    d2 = sum(di * di for di in d)
    if d2 == 0:
        return math.sqrt(sum(vi * vi for vi in v))
    t = max(0.0, min(1.0, sum(v[i] * d[i] for i in range(n)) / d2))
    return math.sqrt(sum((point[i] - (start[i] + t * d[i])) ** 2 for i in range(n)))


def rdp(points, epsilon):
    """Ramer-Douglas-Peucker simplification (works in any dimension).

    Parameters
    ----------
    points : list[tuple[float, ...]]
        Ordered N-D coordinate tuples.
    epsilon : float
        Maximum allowed perpendicular distance.

    Returns
    -------
    list[tuple[float, ...]]
        Simplified polyline (subset of *points* preserving order).
    """
    if len(points) <= 2:
        return list(points)

    dmax = 0.0
    idx = 0
    for i in range(1, len(points) - 1):
        d = _perp_dist(points[i], points[0], points[-1])
        if d > dmax:
            dmax = d
            idx = i

    if dmax > epsilon:
        left = rdp(points[: idx + 1], epsilon)
        right = rdp(points[idx:], epsilon)
        return left[:-1] + right
    return [points[0], points[-1]]


# ---------------------------------------------------------------------------
# Epsilon auto-tuning
# ---------------------------------------------------------------------------

def auto_epsilon(points, fraction=0.01):
    """Epsilon = *fraction* of the bounding-box diagonal of *points* (N-D)."""
    if len(points) <= 2:
        return 0.0
    ndim = len(points[0])
    return fraction * math.sqrt(sum(
        (max(p[d] for p in points) - min(p[d] for p in points)) ** 2
        for d in range(ndim)
    ))


# ---------------------------------------------------------------------------
# Dynamic minimum-kept-points (dimension-aware)
# ---------------------------------------------------------------------------

#  ndim = number of *variable* dimensions (not counting the property).
#  Same ndim ⟹ same formula — only n_original differs between blocks.
_MIN_FLOORS = {1: 8, 2: 12}          # default 15 for ndim >= 3
_MIN_FLOOR_DEFAULT = 15


def _min_kept(ndim: int, n_original: int) -> int:
    """Minimum number of points to keep after RDP, by variable-dimensionality.

    Uses ``max(floor_per_dim, ceil(sqrt(n)))`` capped at *n_original* so we
    never try to keep more points than exist.
    """
    floor = _MIN_FLOORS.get(ndim, _MIN_FLOOR_DEFAULT)
    return min(n_original, max(floor, math.ceil(math.sqrt(n_original))))


# ---------------------------------------------------------------------------
# Topology classification
# ---------------------------------------------------------------------------

def classify_curve(points):
    """Classify an ordered (x, y) curve.

    Returns a short human-readable string such as:
        ``"monotonic↑ | near-linear(R²=0.9993)"``
    """
    n = len(points)
    if n <= 1:
        return "single_point"
    if n == 2:
        return "two_points"

    ys = [p[1] for p in points]
    diffs = [ys[i + 1] - ys[i] for i in range(n - 1)]

    if all(d == 0 for d in diffs):
        return "constant"

    all_pos = all(d >= 0 for d in diffs)
    all_neg = all(d <= 0 for d in diffs)

    if all_pos:
        direction = "monotonic↑"
    elif all_neg:
        direction = "monotonic↓"
    else:
        sign_changes = sum(
            1 for i in range(len(diffs) - 1) if diffs[i] * diffs[i + 1] < 0
        )
        direction = f"non-monotonic({sign_changes} extrema)"

    # Linearity check via R²
    xs = [p[0] for p in points]
    x_mean = sum(xs) / n
    y_mean = sum(ys) / n
    ss_tot = sum((y - y_mean) ** 2 for y in ys)
    if ss_tot > 0:
        ss_xy = sum((xs[i] - x_mean) * (ys[i] - y_mean) for i in range(n))
        ss_xx = sum((x - x_mean) ** 2 for x in xs)
        if ss_xx > 0:
            slope = ss_xy / ss_xx
            intercept = y_mean - slope * x_mean
            ss_res = sum(
                (ys[i] - (slope * xs[i] + intercept)) ** 2 for i in range(n)
            )
            r_sq = 1.0 - ss_res / ss_tot
            if r_sq > 0.999:
                direction += " | linear"
            elif r_sq > 0.99:
                direction += f" | near-linear(R²={r_sq:.4f})"

    return direction


# ---------------------------------------------------------------------------
# Multi-variable helper
# ---------------------------------------------------------------------------

def _var_short_label(vname, comp_org, compounds_map):
    """Short label for a variable, resolving component if available."""
    compounds_map = compounds_map or {}
    comp_label = compounds_map.get(comp_org, "") if comp_org else ""
    nl = vname.lower()
    # Handle Solvent: prefix
    prefix = ""
    if nl.startswith("solvent:"):
        prefix = "s:"
        nl = nl[len("solvent:"):].strip()
    if "mole fraction" in nl:
        return f"{prefix}x({comp_label})" if comp_label else f"{prefix}x"
    if "mass fraction" in nl:
        return f"{prefix}w({comp_label})" if comp_label else f"{prefix}w"
    if "volume fraction" in nl:
        return f"{prefix}φ_v({comp_label})" if comp_label else f"{prefix}φ_v"
    if "molality" in nl:
        return f"{prefix}b({comp_label})" if comp_label else f"{prefix}b"
    if "amount concentration" in nl or "molarity" in nl:
        return f"{prefix}c({comp_label})" if comp_label else f"{prefix}c"
    if "temperature" in nl:
        return "T"
    if "pressure" in nl:
        return f"P({comp_label})" if comp_label else "P"
    short = vname.split(",")[0].strip().split()[0] if vname else "var"
    return f"{short}({comp_label})" if comp_label else short


def _classify_multivar(variables, data_points, compounds_map=None):
    """Produce a brief annotation for multi-variable blocks."""
    entries = []
    for v in variables:
        vnum = v["BLKvar_id"]
        vname = v.get("name", "")
        comp_org = v["component_org_num"]
        label = _var_short_label(vname, comp_org, compounds_map)
        vals = []
        for dp in data_points:
            vv = dp.get("variable_values", {}).get(vnum, {})
            val = vv.get("value")
            if val is not None and isinstance(val, (int, float)):
                vals.append(val)
        if vals:
            entries.append(f"{label}: {min(vals)}–{max(vals)}")
    return f"multi-variable({len(variables)}): " + ", ".join(entries)


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def compact_block_data(variables, properties, data_points, fraction=0.01,
                       compounds_map=None):
    """Compact a block's data points using RDP topology analysis.

    Parameters
    ----------
    variables : list[dict]
        Block variable descriptors (must have ``BLKvar_id`` key).
    properties : list[dict]
        Block property descriptors (must have ``BLKprop_id`` key).
    data_points : list[dict]
        Raw data points with ``variable_values`` and ``property_values``.
    fraction : float
        RDP epsilon as fraction of bounding-box diagonal (default 1 %).

    Returns
    -------
    dict
        - **topology** : list[dict] — per-curve classification.
        - **simplified_points** : list[dict] — compacted data points.
        - **kept_indices** : set[int] — original indices that were kept.
    """
    if not data_points or not variables or not properties:
        return {
            "topology": [],
            "simplified_points": list(data_points or []),
            "kept_indices": set(range(len(data_points or []))),
        }

    var_nums = [v["BLKvar_id"] for v in variables]
    n_vars = len(var_nums)

    kept_indices = set()
    topology_info = []

    for prop in properties:
        prop_num = prop["BLKprop_id"]

        # Build indexed (original_idx, (var1, …, varN, prop_val)) tuples
        indexed = []
        for i, dp in enumerate(data_points):
            vals = []
            ok = True
            for vn in var_nums:
                vv = dp.get("variable_values", {}).get(vn, {})
                val = vv.get("value")
                if val is None or not isinstance(val, (int, float)):
                    ok = False
                    break
                vals.append(val)
            if not ok:
                continue
            pv = dp.get("property_values", {}).get(prop_num, {})
            y = pv.get("value") if isinstance(pv, dict) else pv
            if y is None or not isinstance(y, (int, float)):
                continue
            vals.append(y)
            indexed.append((i, tuple(vals)))

        if not indexed:
            continue

        # Sort by variable dimensions, then apply RDP
        indexed.sort(key=lambda t: t[1][:n_vars])
        raw_pts = [t[1] for t in indexed]
        orig_idx = [t[0] for t in indexed]

        if n_vars > 1:
            # Normalise to [0, 1] so variables at different scales
            # contribute equally to the distance metric.
            ndim = n_vars + 1
            lo = [min(t[1][d] for t in indexed) for d in range(ndim)]
            hi = [max(t[1][d] for t in indexed) for d in range(ndim)]
            span = [hi[d] - lo[d] if hi[d] > lo[d] else 1.0
                    for d in range(ndim)]
            pts = [tuple((v[d] - lo[d]) / span[d] for d in range(ndim))
                   for v in raw_pts]
        else:
            pts = raw_pts

        eps = auto_epsilon(pts, fraction)
        min_k = _min_kept(n_vars, len(pts))
        simplified = rdp(pts, eps)

        # Adaptive: if RDP is too aggressive, halve epsilon and retry
        attempts = 0
        while len(simplified) < min_k and eps > 1e-15 and attempts < 20:
            eps *= 0.5
            simplified = rdp(pts, eps)
            attempts += 1

        kept_set = set(map(tuple, simplified))

        for j, pt in enumerate(pts):
            if tuple(pt) in kept_set:
                kept_indices.add(orig_idx[j])

        if n_vars == 1:
            shape = classify_curve(raw_pts)
        else:
            shape = _classify_multivar(variables, data_points, compounds_map)

        topology_info.append({
            "var": ",".join(var_nums) if n_vars > 1 else var_nums[0],
            "prop": prop_num,
            "shape": shape,
            "n_original": len(indexed),
            "n_kept": sum(1 for pt in pts if tuple(pt) in kept_set),
            "epsilon": round(eps, 6),
        })

    # Always keep first and last by original order
    if data_points:
        kept_indices.add(0)
        kept_indices.add(len(data_points) - 1)

    simplified_points = [data_points[i] for i in sorted(kept_indices)]

    return {
        "topology": topology_info,
        "simplified_points": simplified_points,
        "kept_indices": kept_indices,
    }
