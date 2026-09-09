"""
Ideal solution baseline construction.
======================================
Given pure-component property values and a composition grid, compute
the ideal-mixture baseline using one of two mixing rules:

1. **Linear (free-energy ideal)**:  Y_mix = Σ x_i · Y_i
   Appropriate for volume-additive properties (density, molar volume,
   refractive index, heat capacity, speed of sound).

2. **Arrhenius (activation-energy ideal / Eyring)**:
   ln(Y_mix) = Σ x_i · ln(Y_i)
   Appropriate for viscosity and transport properties: the mixing is
   "ideal" in terms of the activation energy of viscous flow.

Supports **N-component** systems (binary, ternary, quaternary, ...).

For transport properties (viscosity, thermal conductivity, diffusivity)
**both** baselines are physically meaningful.  When mixing_rule="both",
both are returned so the user can compare the two excess functions:
  - excess_linear  = Y_exp − Y_ideal_linear        ("excess viscosity")
  - excess_arrhenius = ln(Y_exp) − ln(Y_ideal_arrhenius)  ("excess activation energy")

Public API
----------
- build_ideal_baseline(pure_values, x_grid, property_type, ...) → dict
- compute_excess_property(x_data, y_data, pure_values, property_type, ...) → dict
- extract_pure_from_edges(x_dict, y_data, threshold=0.02) → dict
- default_mixing_rule(property_type) → str
"""

from __future__ import annotations

import logging
import math
from typing import Dict, List, Optional, Tuple, Union

import numpy as np

log = logging.getLogger("IDEAL-BASELINE")


# ═══════════════════════════════════════════════════════════════
#  Property → mixing rule mapping
# ═══════════════════════════════════════════════════════════════

# Canonical property → default mixing rule mapping
# "arrhenius" = activation-energy ideal (Eyring); "linear" = free-energy ideal
_DEFAULT_RULE: Dict[str, str] = {
    # Transport properties → Arrhenius by default
    "viscosity":             "arrhenius",
    "thermal_conductivity":  "arrhenius",
    "diffusion_coefficient": "arrhenius",
    # Volumetric / thermodynamic → linear
    "molar_volume":          "linear",
    "density":               "linear",
    "mass_density":          "linear",
    "refractive_index":      "linear",
    "speed_of_sound":        "linear",
    "heat_capacity":         "linear",
    "surface_tension":       "linear",
}

# These properties support dual-baseline analysis (both rules valid)
_DUAL_RULE_PROPS = {"viscosity", "thermal_conductivity", "diffusion_coefficient"}


def default_mixing_rule(property_type: str) -> str:
    """Return the canonical default mixing rule for a property type.

    Returns "arrhenius" for transport properties, "linear" otherwise.
    """
    prop_key = property_type.lower().replace(" ", "_")
    return _DEFAULT_RULE.get(prop_key, "linear")


# ═══════════════════════════════════════════════════════════════
#  Composition resolution  (binary 1-D ↔ N-component dict)
# ═══════════════════════════════════════════════════════════════

# Type for x_grid: 1-D array (binary), {comp: array}, or 2-D array (n×N)
XGrid = Union[np.ndarray, List[float], Dict[str, "np.ndarray | List[float]"]]


def _resolve_compositions(
    pure_values: Dict[str, float],
    x_grid: XGrid,
    component_order: Optional[List[str]] = None,
) -> Tuple[List[str], Dict[str, np.ndarray]]:
    """Normalize any x_grid input into canonical {comp_name: array} form.

    Accepted inputs
    ---------------
    * **1-D array** (binary only): mole fractions of component_order[0];
      x_2 = 1 − x_1.
    * **dict** ``{comp_name: array}``: explicit per-component fractions.
      If N−1 components are given the last is computed as 1 − Σ.
    * **2-D array** ``(n_points × N)``: columns matched to *component_order*.
      If N−1 columns, the last component is inferred.

    Returns
    -------
    (components, x_dict)
        components : list[str]  — ordered component names
        x_dict : dict[str, ndarray] — {comp: mole_fraction_array}
    """
    comps = component_order or sorted(pure_values.keys())
    N = len(comps)

    # ---- dict input ----
    if isinstance(x_grid, dict):
        x_dict = {k: np.asarray(v, dtype=float) for k, v in x_grid.items()}
        missing = [c for c in comps if c not in x_dict]
        if len(missing) == 1:
            x_sum = sum(x_dict.values())            # element-wise
            x_dict[missing[0]] = 1.0 - x_sum
        elif len(missing) > 1:
            raise ValueError(
                f"Composition dict missing {len(missing)} components: {missing}. "
                f"At most 1 may be omitted (inferred as 1 − Σ)."
            )
        return comps, x_dict

    # ---- array input ----
    x_arr = np.asarray(x_grid, dtype=float)

    if x_arr.ndim == 1:
        if N == 2:
            return comps, {comps[0]: x_arr, comps[1]: 1.0 - x_arr}
        if N == 1:
            return comps, {comps[0]: np.ones_like(x_arr)}
        raise ValueError(
            f"1-D x_grid is only valid for unary (1) or binary (2) systems; "
            f"got {N} components. Use a dict or 2-D array."
        )

    if x_arr.ndim == 2:
        n_cols = x_arr.shape[1]
        x_dict: Dict[str, np.ndarray] = {}
        for j in range(min(n_cols, N)):
            x_dict[comps[j]] = x_arr[:, j]
        if n_cols == N - 1:
            x_dict[comps[-1]] = 1.0 - np.sum(x_arr, axis=1)
        return comps, x_dict

    raise ValueError(f"x_grid must be 1-D, 2-D array, or dict; got ndim={x_arr.ndim}")


# ═══════════════════════════════════════════════════════════════
#  N-component ideal baselines
# ═══════════════════════════════════════════════════════════════

def _build_linear_N(
    pure_values: Dict[str, float],
    x_dict: Dict[str, np.ndarray],
) -> np.ndarray:
    """Y_ideal = Σ x_i · Y_i  (N components)."""
    result = np.zeros_like(next(iter(x_dict.values())))
    for comp, x_i in x_dict.items():
        result = result + x_i * pure_values[comp]
    return result


def _build_arrhenius_N(
    pure_values: Dict[str, float],
    x_dict: Dict[str, np.ndarray],
) -> np.ndarray:
    """Y_ideal = exp(Σ x_i · ln(Y_i))  (N components)."""
    log_result = np.zeros_like(next(iter(x_dict.values())))
    for comp, x_i in x_dict.items():
        log_result = log_result + x_i * math.log(pure_values[comp])
    return np.exp(log_result)


# ═══════════════════════════════════════════════════════════════
#  Pure-value extraction from data edges
# ═══════════════════════════════════════════════════════════════

def extract_pure_from_edges(
    x_dict: Dict[str, np.ndarray],
    y_data: np.ndarray,
    threshold: float = 0.02,
    *,
    extrapolate: bool = False,
    extrapolate_min_points: int = 3,
    coverage_warn_threshold: float = 0.85,
) -> Dict[str, dict]:
    """Extract pure-component property values from data edges.

    For each component *i*, looks for data points where x_i is closest
    to 1.0 (meaning the mixture is nearly pure component *i*) and
    returns the mean measured property value at those points.

    When explicitly requested, missing endpoints can be extrapolated using
    a local linear fit. The default contract returns only directly observed
    near-pure values.

    Works for any number of components (binary, ternary, …).

    Parameters
    ----------
    x_dict : dict
        {component_name: mole_fraction_array}.  All arrays same length.
    y_data : array-like
        Measured property values (1-D, same length as the x arrays).
    threshold : float
        Points with ``x_i > 1 − threshold`` are "nearly pure".
    extrapolate : bool
        If True, when no near-pure points exist, fit a local linear
        regression on the top ``extrapolate_min_points`` highest-x
        points and extrapolate to x=1.
    extrapolate_min_points : int
        Minimum number of points needed for extrapolation (default 3).
    coverage_warn_threshold : float
        If max_x < this, the ``quality`` flag is set to ``"poor"``.

    Returns
    -------
    dict
        ``{comp: {"value", "max_x", "n_near_pure", "method", "quality"}}``.
        ``method`` is ``"direct"`` (averaged near-pure points),
        ``"extrapolated"`` (linear extrapolation to x=1), or
        ``quality`` is ``"good"``, ``"fair"``, or ``"poor"``.
    """
    y_data = np.asarray(y_data, dtype=float)
    pure_values: Dict[str, dict] = {}
    for comp, x_i in x_dict.items():
        x_i = np.asarray(x_i, dtype=float)
        valid = ~np.isnan(x_i) & ~np.isnan(y_data)
        if not np.any(valid):
            continue
        x_v = x_i[valid]
        y_v = y_data[valid]
        max_x = float(np.max(x_v))
        near_pure = x_v > (1.0 - threshold)
        n_near = int(np.sum(near_pure))

        # Quality assessment
        if max_x >= 1.0 - threshold:
            quality = "good"
        elif max_x >= coverage_warn_threshold:
            quality = "fair"
        else:
            quality = "poor"

        if n_near > 0:
            # Best case: direct averaging of near-pure points
            value = float(f"{float(np.mean(y_v[near_pure])):.8g}")
            method = "direct"
        elif extrapolate and len(x_v) >= extrapolate_min_points:
            # Extrapolate to x=1 using local linear fit on highest-x tail
            order = np.argsort(x_v)
            x_sorted = x_v[order]
            y_sorted = y_v[order]
            # Use the top 20% of points (at least extrapolate_min_points)
            n_tail = max(extrapolate_min_points, len(x_v) // 5)
            x_tail = x_sorted[-n_tail:]
            y_tail = y_sorted[-n_tail:]
            # Linear regression: y = a*x + b
            coeffs = np.polyfit(x_tail, y_tail, 1)
            value = float(f"{float(np.polyval(coeffs, 1.0)):.8g}")
            method = "extrapolated"
            log.info(
                "%s: extrapolated to x=1 from %d tail points "
                "(max_x=%.4f, slope=%.2f)",
                comp, n_tail, max_x, coeffs[0],
            )
        else:
            continue

        pure_values[comp] = {
            "value": value,
            "max_x": round(max_x, 6),
            "n_near_pure": n_near,
            "method": method,
            "quality": quality,
        }
    return pure_values


def pure_values_from_edges(
    x_dict: Dict[str, np.ndarray],
    y_data: np.ndarray,
    threshold: float = 0.02,
    *,
    extrapolate: bool = False,
) -> Dict[str, float]:
    """Convenience wrapper: same as extract_pure_from_edges but returns
    a flat ``{component: value}`` dict (no metadata), suitable for direct
    use with ``build_ideal_baseline`` / ``compute_excess_property``."""
    info = extract_pure_from_edges(x_dict, y_data, threshold, extrapolate=extrapolate)
    return {comp: d["value"] for comp, d in info.items()}


# ═══════════════════════════════════════════════════════════════
#  build_ideal_baseline  (N-component)
# ═══════════════════════════════════════════════════════════════

def build_ideal_baseline(
    pure_values: Dict[str, float],
    x_grid: XGrid,
    property_type: str,
    *,
    mixing_rule: Optional[str] = None,
    component_order: Optional[List[str]] = None,
) -> dict:
    """Compute ideal-mixture property values on a composition grid.

    Supports any number of components (binary, ternary, …).

    Parameters
    ----------
    pure_values : dict
        {component_name: pure_property_value}.  Needs one entry per
        component.
    x_grid : array-like or dict
        Composition specification:

        * **1-D array** (binary): mole fractions of the first component.
        * **dict** ``{comp_name: array}``: mole fractions per component
          (for ternary+ or explicit binary).  If N−1 entries are given
          the last is inferred as 1 − Σ.
        * **2-D array** ``(n_points × N)``: one column per component,
          matched to *component_order*.
    property_type : str
        Property identifier (e.g. "viscosity", "density").
    mixing_rule : str, optional
        "linear", "arrhenius", or "both".
        If None, uses the canonical default for *property_type*.
    component_order : list, optional
        Component names in order.  If None, sorted keys of *pure_values*.

    Returns
    -------
    dict
        Always contains: ``y_ideal`` (or ``y_ideal_linear`` /
        ``y_ideal_arrhenius`` when rule="both"), ``mixing_rule``,
        ``components``, ``pure_values``, ``n_components``, and
        ``x`` mapping each component to its composition grid.
    """
    comps, x_dict = _resolve_compositions(pure_values, x_grid, component_order)
    N = len(comps)

    # Validate: pure_values must cover every component
    missing_pv = [c for c in comps if c not in pure_values]
    if missing_pv:
        return {"error": f"Missing pure values for: {missing_pv}"}

    rule = (mixing_rule or default_mixing_rule(property_type)).lower()

    # Build the base result dict
    base: dict = {
        "components": comps,
        "pure_values": {c: pure_values[c] for c in comps},
        "n_components": N,
    }
    base["x"] = {c: x_dict[c].tolist() for c in comps}

    # Check positivity for Arrhenius
    pv_list = [pure_values[c] for c in comps]
    any_nonpos = any(v <= 0 for v in pv_list)

    if rule == "both":
        if any_nonpos:
            return {**base, "error": f"Arrhenius requires positive values, got {pv_list}"}
        base["y_ideal_linear"] = _build_linear_N(pure_values, x_dict).tolist()
        base["y_ideal_arrhenius"] = _build_arrhenius_N(pure_values, x_dict).tolist()
        base["mixing_rule"] = "both"
        return base

    if rule == "arrhenius":
        if any_nonpos:
            return {**base, "error": f"Arrhenius requires positive values, got {pv_list}"}
        base["y_ideal"] = _build_arrhenius_N(pure_values, x_dict).tolist()
        base["mixing_rule"] = "arrhenius"
        return base

    # linear (default)
    base["y_ideal"] = _build_linear_N(pure_values, x_dict).tolist()
    base["mixing_rule"] = "linear"
    return base


# ═══════════════════════════════════════════════════════════════
#  compute_excess_property  (N-component)
# ═══════════════════════════════════════════════════════════════

def compute_excess_property(
    x_data: XGrid,
    y_data: np.ndarray | List[float],
    pure_values: Dict[str, float],
    property_type: str,
    *,
    mixing_rule: Optional[str] = None,
    component_order: Optional[List[str]] = None,
) -> dict:
    """Compute excess property: Y^E = Y_exp − Y_ideal at each data point.

    Supports any number of components.

    Parameters
    ----------
    x_data : array-like or dict
        Composition data (same formats as *x_grid* in
        :func:`build_ideal_baseline`).
    y_data : array-like
        Experimental property values (1-D).
    pure_values : dict
        {component_name: pure_property_value}.
    property_type : str
        Property identifier.
    mixing_rule : str, optional
        "linear", "arrhenius", or "both". If None, uses canonical default.
    component_order : list, optional
        Component names in order.

    Returns
    -------
    dict
        Contains ``y_exp``, ``y_ideal`` (or dual variants), ``y_excess``,
        ``mixing_rule``, ``excess_label``, ``n_points``, ``n_components``,
        and ``x`` dict.
    """
    y_data = np.asarray(y_data, dtype=float)

    rule = (mixing_rule or default_mixing_rule(property_type)).lower()

    baseline = build_ideal_baseline(
        pure_values, x_data, property_type,
        mixing_rule=rule,
        component_order=component_order,
    )
    if "error" in baseline:
        return baseline

    N = baseline["n_components"]
    prop_key = property_type.lower().replace(" ", "_")

    # Composition keys to propagate
    comp_keys: dict = {"x": baseline["x"]}

    if rule == "both":
        y_ideal_lin = np.array(baseline["y_ideal_linear"])
        y_ideal_arr = np.array(baseline["y_ideal_arrhenius"])
        return {
            **comp_keys,
            "y_exp": y_data.tolist(),
            "y_ideal_linear": y_ideal_lin.tolist(),
            "y_ideal_arrhenius": y_ideal_arr.tolist(),
            "y_excess_linear": (y_data - y_ideal_lin).tolist(),
            "y_excess_arrhenius": (np.log(y_data) - np.log(y_ideal_arr)).tolist(),
            "mixing_rule": "both",
            "excess_label_linear": f"excess {prop_key} (free-energy ideal)",
            "excess_label_arrhenius": f"excess ln({prop_key}) (activation-energy ideal)",
            "n_points": len(y_data),
            "n_components": N,
        }

    y_ideal = np.array(baseline["y_ideal"])
    if rule == "arrhenius":
        y_excess = np.log(y_data) - np.log(y_ideal)
        label = f"excess ln({prop_key}) (activation-energy ideal)"
    else:
        y_excess = y_data - y_ideal
        label = f"excess {prop_key} (free-energy ideal)"

    return {
        **comp_keys,
        "y_exp": y_data.tolist(),
        "y_ideal": y_ideal.tolist(),
        "y_excess": y_excess.tolist(),
        "mixing_rule": baseline["mixing_rule"],
        "excess_label": label,
        "n_points": len(y_data),
        "n_components": N,
    }


# ═══════════════════════════════════════════════════════════════
#  Non-ideality classification
# ═══════════════════════════════════════════════════════════════

# ── Property-semantics registry ─────────────────────────────────
# Declarative, one row per property:
#   tier "A"  — excess vs the canonical ideal baseline IS a thermodynamic
#               excess function; interaction language allowed.
#               attractive_sign: sign of Y^E meaning "attractive"
#               (+1 / -1), or None when the sign has no clean
#               interaction reading (descriptive only).
#   tier "B"  — the linear-in-x baseline yields a DEVIATION function,
#               not a thermodynamic excess (the ideal reference itself
#               is curved in x).  Descriptive language only; "route"
#               names the rigorous measurement-based alternative.
#   unlisted  — tier "C": unclassified, no interaction language.
_PROPERTY_SEMANTICS: Dict[str, dict] = {
    # Tier A
    "molar_volume": {
        "tier": "A", "excess_name": "V^E", "attractive_sign": -1,
        "gloss": "V^E < 0: tighter packing / stronger unlike interactions",
    },
    "excess_molar_volume": {
        "tier": "A", "excess_name": "V^E", "attractive_sign": -1,
        "gloss": "V^E < 0: tighter packing / stronger unlike interactions",
    },
    "enthalpy": {
        "tier": "A", "excess_name": "H^E", "attractive_sign": -1,
        "gloss": "H^E < 0: exothermic mixing / attractive",
    },
    "molar_enthalpy": {
        "tier": "A", "excess_name": "H^E", "attractive_sign": -1,
        "gloss": "H^E < 0: exothermic mixing / attractive",
    },
    "excess_molar_enthalpy": {
        "tier": "A", "excess_name": "H^E", "attractive_sign": -1,
        "gloss": "H^E < 0: exothermic mixing / attractive",
    },
    "heat_capacity": {
        "tier": "A", "excess_name": "Cp^E", "attractive_sign": None,
        "gloss": "Cp^E sign reflects structural changes, not simply "
                 "attraction/repulsion",
    },
    "viscosity": {
        "tier": "A", "excess_name": "viscosity excess",
        "attractive_sign": +1,
        "gloss": "positive excess: stronger unlike interactions "
                 "(Eyring activation view)",
    },
    "thermal_conductivity": {
        "tier": "A", "excess_name": "excess", "attractive_sign": +1,
        "gloss": "positive excess: stronger unlike interactions",
    },
    "diffusion_coefficient": {
        "tier": "A", "excess_name": "excess", "attractive_sign": None,
        "gloss": "diffusivity deviations couple to viscosity and "
                 "thermodynamic factor; no single-sign reading",
    },
    # Tier B — deviation functions
    "density": {
        "tier": "B", "excess_name": "density deviation Δρ",
        "route": "convert measured ρ(x) pointwise to molar volume "
                 "(Vm = (x1·M1+x2·M2)/ρ, exact) and fit V^E "
                 "(fit_block_derived transform=density_to_molar_volume)",
    },
    "mass_density": {
        "tier": "B", "excess_name": "density deviation Δρ",
        "route": "convert measured ρ(x) pointwise to molar volume "
                 "(Vm = (x1·M1+x2·M2)/ρ, exact) and fit V^E "
                 "(fit_block_derived transform=density_to_molar_volume)",
    },
    "speed_of_sound": {
        "tier": "B", "excess_name": "sound-speed deviation Δu",
        "route": "κ_S = 1/(ρu²) (Laplace, exact from measured ρ and u), "
                 "then κ_S^E vs the volume-fraction ideal (Benson–Kiyohara)",
    },
    "refractive_index": {
        "tier": "B", "excess_name": "refractive-index deviation Δn",
        "route": "Lorentz–Lorenz / volume-fraction mixing for the ideal "
                 "reference",
    },
    "surface_tension": {
        "tier": "B", "excess_name": "surface-tension deviation Δσ",
        "route": "surface-phase adsorption models; Δσ is descriptive only",
    },
}


def property_semantics(property_type: str) -> dict:
    """Return the semantics row for a property (tier ``C`` when unknown)."""
    key = property_type.lower().replace(" ", "_")
    if key in _PROPERTY_SEMANTICS:
        return {"key": key, **_PROPERTY_SEMANTICS[key]}
    # tolerant containment match ("mass_density_kg_m3" → "mass_density")
    for k, row in _PROPERTY_SEMANTICS.items():
        if k in key:
            return {"key": k, **row}
    return {"key": key, "tier": "C"}


def classify_excess(
    y_excess: "np.ndarray | list",
    x_vals: "np.ndarray | list",
    property_type: str,
    *,
    x_interior: tuple = (0.05, 0.95),
    dominance_threshold: float = 0.8,
    rmse: Optional[float] = None,
) -> str:
    """Classify non-ideality from excess/deviation values.

    Consults the property-semantics registry:

    - **Tier A** (thermodynamic excess): returns ``attractive`` /
      ``repulsive`` / ``mixed`` with the property's sign gloss, or a
      descriptive sign statement when the property has no clean
      interaction reading.
    - **Tier B** (deviation function): returns a descriptive
      ``positive/negative deviation`` label plus the rigorous
      measurement-based route — never interaction language.
    - **Tier C** (unregistered): ``unclassified``.

    A significance gate compares max |Y^E| against ``3×rmse`` when the
    fit RMSE is supplied — scatter is never classified.
    """
    x_arr = np.asarray(x_vals, dtype=float)
    y_arr = np.asarray(y_excess, dtype=float)

    mask = (x_arr > x_interior[0]) & (x_arr < x_interior[1])
    interior = y_arr[mask]

    if len(interior) == 0:
        return "insufficient_data"

    # Check if effectively zero
    max_abs = float(np.max(np.abs(interior)))
    if max_abs < 1e-10:
        return "ideal"

    # Significance gate: never classify scatter
    if rmse is not None and rmse > 0 and max_abs < 3.0 * rmse:
        return (
            f"not significant (max |Y^E| {max_abs:.3g} < 3×RMSE "
            f"{rmse:.3g} — deviations are within fit scatter)"
        )

    pos = int(np.sum(interior > 0))
    neg = int(np.sum(interior < 0))
    total = len(interior)

    if pos / total >= dominance_threshold:
        sign = +1
    elif neg / total >= dominance_threshold:
        sign = -1
    else:
        sign = 0

    sem = property_semantics(property_type)
    tier = sem.get("tier", "C")
    sign_word = {+1: "positive", -1: "negative", 0: "mixed"}[sign]

    if tier == "A":
        if sign == 0:
            return "mixed (sign changes across composition)"
        attr = sem.get("attractive_sign")
        if attr is None:
            return (
                f"{sign_word} {sem.get('excess_name', 'excess')} "
                f"({sem.get('gloss', 'no single-sign interaction reading')})"
            )
        verdict = "attractive" if sign == attr else "repulsive"
        return f"{verdict} ({sem.get('gloss', '')})".rstrip(" ()")

    if tier == "B":
        route = sem.get("route", "")
        return (
            f"{sign_word} deviation (descriptive — the linear-x baseline "
            f"for {sem.get('key', property_type)} is not a thermodynamic "
            f"excess; rigorous route: {route})"
        )

    return (
        f"unclassified ({sign_word} deviation; no sign semantics "
        f"registered for '{property_type}')"
    )
