"""Exact algebraic transforms between measured mixture properties.
=================================================================
Rung DP2 of the measurement-priority ladder: convert *measured* mixture
data pointwise using exact physical relations, so the transformed curve
is still measurement-grade (no model content is introduced).

    DP0  direct measured excess property        (fit as-is)
    DP1  direct measured total mixture property (fit as-is)
    DP2  exact pointwise transform of measured mixture data  ← this module
    DP3  composed from pure-component values    (FALLBACK ONLY, estimate)

Every transform declares its inputs, output property, canonical units,
and the exact relation used, so tools can label provenance
("measured-derived") and the registry can be listed to the agent.

Public API
----------
- TRANSFORMS: registry dict
- density_to_molar_volume(x1, rho, M1, M2) → Vm array [m3/mol]
- molar_volume_to_density(x1, vm, M1, M2)  → rho array [kg/m3]
- kappa_s_from_rho_u(rho, u)               → κ_S array [1/Pa]
- apply_transform(name, **arrays_and_masses) → dict
"""

from __future__ import annotations

import numpy as np

__all__ = [
    "TRANSFORMS",
    "density_to_molar_volume",
    "molar_volume_to_density",
    "kappa_s_from_rho_u",
    "apply_transform",
]


def density_to_molar_volume(
    x1: np.ndarray, rho: np.ndarray, M1: float, M2: float,
) -> np.ndarray:
    """Vm = (x1·M1 + x2·M2) / ρ — exact, per measured point.

    Parameters
    ----------
    x1 : array — mole fraction of component 1
    rho : array — measured mixture mass density [kg/m3]
    M1, M2 : float — molar masses [g/mol] (converted internally)

    Returns
    -------
    array — molar volume [m3/mol]
    """
    x1 = np.asarray(x1, dtype=float)
    rho = np.asarray(rho, dtype=float)
    m_mix = (x1 * M1 + (1.0 - x1) * M2) * 1e-3   # g/mol → kg/mol
    return m_mix / rho


def molar_volume_to_density(
    x1: np.ndarray, vm: np.ndarray, M1: float, M2: float,
) -> np.ndarray:
    """ρ = (x1·M1 + x2·M2) / Vm — exact inverse of the above."""
    x1 = np.asarray(x1, dtype=float)
    vm = np.asarray(vm, dtype=float)
    m_mix = (x1 * M1 + (1.0 - x1) * M2) * 1e-3
    return m_mix / vm


def kappa_s_from_rho_u(rho: np.ndarray, u: np.ndarray) -> np.ndarray:
    """κ_S = 1 / (ρ·u²) — Laplace relation, exact from measured ρ and u.

    Both arrays must be same-state, same-composition measurements.
    Returns isentropic compressibility [1/Pa].
    """
    rho = np.asarray(rho, dtype=float)
    u = np.asarray(u, dtype=float)
    return 1.0 / (rho * u * u)


TRANSFORMS: dict[str, dict] = {
    "density_to_molar_volume": {
        "fn": density_to_molar_volume,
        "source_property": "mass_density",
        "source_units": "kg/m3",
        "target_property": "molar_volume",
        "target_units": "m3/mol",
        "target_ideal_rule": "linear",   # Vm_id = x1·V1 + x2·V2 is EXACT
        "requires": ["x1", "rho", "M1", "M2"],
        "relation": "Vm = (x1*M1 + x2*M2)/rho (exact, pointwise)",
    },
    "molar_volume_to_density": {
        "fn": molar_volume_to_density,
        "source_property": "molar_volume",
        "source_units": "m3/mol",
        "target_property": "mass_density",
        "target_units": "kg/m3",
        "target_ideal_rule": "linear",   # deviation function only (tier B)
        "requires": ["x1", "vm", "M1", "M2"],
        "relation": "rho = (x1*M1 + x2*M2)/Vm (exact, pointwise)",
    },
    "kappa_s_from_rho_u": {
        "fn": kappa_s_from_rho_u,
        "source_property": "mass_density + speed_of_sound",
        "source_units": "kg/m3, m/s",
        "target_property": "isentropic_compressibility",
        "target_units": "1/Pa",
        "target_ideal_rule": "linear",
        "requires": ["rho", "u"],
        "relation": "kappa_S = 1/(rho*u^2) (Laplace, exact, pointwise)",
        "note": "needs two y-columns from the same block/state; "
                "single-source tools cannot apply it automatically",
    },
}


def apply_transform(name: str, **kwargs) -> dict:
    """Apply a registered transform; returns {y, meta} or {error}."""
    spec = TRANSFORMS.get(name)
    if spec is None:
        return {
            "error": f"Unknown transform '{name}'. "
                     f"Available: {sorted(TRANSFORMS)}",
        }
    missing = [r for r in spec["requires"] if r not in kwargs]
    if missing:
        return {"error": f"Transform '{name}' missing inputs: {missing}"}
    try:
        y = spec["fn"](**{k: kwargs[k] for k in spec["requires"]})
    except Exception as exc:  # noqa: BLE001 — surface as tool error
        return {"error": f"Transform '{name}' failed: {exc}"}
    return {
        "y": y,
        "target_property": spec["target_property"],
        "target_units": spec["target_units"],
        "target_ideal_rule": spec["target_ideal_rule"],
        "relation": spec["relation"],
    }
