"""Composition-basis detection and exact interconversion.
==========================================================
Phase 1 of the composition-normalization design: a deterministic,
basis-agnostic conversion core.  Binary systems (the RK fitting domain).

Convention throughout: component 1 = the compound named in the
composition column (solute for molality/ratio bases); component 2 = the
other compound (solvent).  All conversions return the MOLE FRACTION of
component 1 — the canonical fitting basis (molar excess functions are
defined on it and the RK family is not closed under basis change).

Conversion classes:
- EXACT, molar-mass only (measurement-grade, no assumptions):
  mass fraction, molality, mass ratio, amount (mole) ratio.
- DENSITY-DEPENDENT (exact given a measured mixture density at the same
  row/state): molarity.  Volume fraction needs PURE molar volumes at T
  (bridge data) and carries a definition caveat.
- NOT CONVERTIBLE here: solvent-scoped fractions (defined within a
  solvent subsystem — overall composition is under-determined).

Molar masses come from the block's own compound formulas (see
``_formula_weight`` in fitting_tools / callers) — never from memory.
"""

from __future__ import annotations

import numpy as np

__all__ = [
    "detect_composition_basis",
    "COMPOSITION_BASES",
    "mass_to_mole",
    "mole_to_mass",
    "molality_to_mole",
    "mass_ratio_to_mole",
    "amount_ratio_to_mole",
    "molarity_to_mole",
    "volume_fraction_to_mole",
    "mole_to_volume_fraction",
    "convert_axis_to_mole_fraction",
]


# ── Basis detection (canonical var_id prefixes, var_alias.py) ───────
# Order matters: longer/scoped prefixes first so e.g. solvent_mole_fraction
# is not claimed by mole_fraction.
_BASIS_PATTERNS: list[tuple[str, str]] = [
    ("solvent_",                                   "solvent_scoped"),
    ("initial_molality",                           "solvent_scoped"),
    ("final_molality",                             "solvent_scoped"),
    ("amount_concentration_molarity_mol_dm3",      "molarity"),
    ("mass_ratio_of_solute_to_solvent",            "mass_ratio"),
    ("amount_ratio_of_solute_to_solvent",          "amount_ratio"),
    ("molality_mol_kg",                            "molality"),
    ("volume_fraction",                            "volume_fraction"),
    ("mass_fraction",                              "mass_fraction"),
    ("mole_fraction",                              "mole_fraction"),
    ("mass_concentration",                         "mass_concentration"),
]

COMPOSITION_BASES = tuple(sorted({b for _, b in _BASIS_PATTERNS}))


def detect_composition_basis(column_name: str) -> str:
    """Classify a composition column by its canonical name prefix.

    Column names are canonical var_ids with the component resolved
    (e.g. ``mass_fraction_<heptane>``), so prefix matching is exact —
    substring matching would misclassify e.g.
    ``mass_ratio_of_solute_to_solvent`` as solvent-scoped.

    Returns one of: mole_fraction, mass_fraction, volume_fraction,
    molality, molarity, mass_ratio, amount_ratio, mass_concentration,
    solvent_scoped, or "unknown".
    """
    c = (column_name or "").strip().lower()
    for prefix, basis in _BASIS_PATTERNS:
        if c.startswith(prefix):
            return basis
    return "unknown"


# ── Exact, molar-mass-only conversions ──────────────────────────────

def mass_to_mole(w1: np.ndarray, M1: float, M2: float) -> np.ndarray:
    """x1 = (w1/M1) / (w1/M1 + (1-w1)/M2) — exact."""
    w1 = np.asarray(w1, dtype=float)
    n1 = w1 / M1
    n2 = (1.0 - w1) / M2
    return n1 / (n1 + n2)


def mole_to_mass(x1: np.ndarray, M1: float, M2: float) -> np.ndarray:
    """w1 = x1·M1 / (x1·M1 + (1-x1)·M2) — exact."""
    x1 = np.asarray(x1, dtype=float)
    m1 = x1 * M1
    m2 = (1.0 - x1) * M2
    return m1 / (m1 + m2)


def molality_to_mole(b: np.ndarray, M_solvent: float) -> np.ndarray:
    """x_solute = b·M2 / (1000 + b·M2) — exact.

    b in mol/kg(solvent); M_solvent in g/mol (1 kg solvent = 1000/M2 mol).
    """
    b = np.asarray(b, dtype=float)
    return b * M_solvent / (1000.0 + b * M_solvent)


def mass_ratio_to_mole(r: np.ndarray, M1: float, M2: float) -> np.ndarray:
    """r = m_solute/m_solvent → w1 = r/(1+r) → x1 — exact."""
    r = np.asarray(r, dtype=float)
    w1 = r / (1.0 + r)
    return mass_to_mole(w1, M1, M2)


def amount_ratio_to_mole(nr: np.ndarray) -> np.ndarray:
    """nr = n_solute/n_solvent → x1 = nr/(1+nr) — exact, no constants."""
    nr = np.asarray(nr, dtype=float)
    return nr / (1.0 + nr)


# ── Density-dependent conversions (exact given measured ρ) ──────────

def molarity_to_mole(
    c: np.ndarray, rho: np.ndarray, M1: float, M2: float,
) -> np.ndarray:
    """x1 = c·M2 / (ρ − c·(M1 − M2)) — exact per row.

    c in mol/dm³ (= mol/L), ρ in kg/m³, M in g/mol.
    Derivation: c[mol/m³] = 1000·c = x1·ρ / (x1·M1' + x2·M2') with
    M' in kg/mol = M/1000, so the g/mol factors cancel to the form above
    with c·M in (mol/dm³·g/mol) = kg/m³ units.
    """
    c = np.asarray(c, dtype=float)
    rho = np.asarray(rho, dtype=float)
    return c * M2 / (rho - c * (M1 - M2))


def volume_fraction_to_mole(
    phi1: np.ndarray, V1: float, V2: float,
) -> np.ndarray:
    """x1 = (φ1/V1) / (φ1/V1 + (1−φ1)/V2) — needs PURE molar volumes at T.

    Caveat: φ is conventionally defined via pre-mixing pure volumes;
    definitions vary between papers.
    """
    phi1 = np.asarray(phi1, dtype=float)
    a = phi1 / V1
    b = (1.0 - phi1) / V2
    return a / (a + b)


def mole_to_volume_fraction(
    x1: np.ndarray, V1: float, V2: float,
) -> np.ndarray:
    """φ1 = x1·V1 / (x1·V1 + (1−x1)·V2) — inverse of the above."""
    x1 = np.asarray(x1, dtype=float)
    a = x1 * V1
    b = (1.0 - x1) * V2
    return a / (a + b)


# ── One-call façade for the fitting-tool basis gate ────────────────

def convert_axis_to_mole_fraction(
    basis: str,
    values: np.ndarray,
    *,
    M1: float | None = None,
    M2: float | None = None,
    rho: np.ndarray | None = None,
    V1: float | None = None,
    V2: float | None = None,
) -> dict:
    """Convert a composition axis to mole fraction of component 1.

    Component 1 = the compound named in the source column (solute for
    molality / ratio bases); M1/M2 in g/mol from block formulas.

    Returns ``{"x": array, "relation": str, "rung": str}`` or
    ``{"error": str}`` when the basis needs unavailable bridging data
    or is not convertible.
    """
    v = np.asarray(values, dtype=float)

    if basis == "mole_fraction":
        return {"x": v, "relation": "identity", "rung": "native"}

    if basis == "mass_fraction":
        if M1 is None or M2 is None:
            return {"error": "mass_fraction→mole needs molar masses M1, M2"}
        return {
            "x": mass_to_mole(v, M1, M2),
            "relation": f"x1=(w1/M1)/(w1/M1+w2/M2), M1={M1:g}, M2={M2:g} g/mol",
            "rung": "exact (molar masses from block formulas)",
        }

    if basis == "molality":
        if M2 is None:
            return {"error": "molality→mole needs the SOLVENT molar mass M2"}
        return {
            "x": molality_to_mole(v, M2),
            "relation": f"x1=b·M2/(1000+b·M2), M2(solvent)={M2:g} g/mol",
            "rung": "exact (molar masses from block formulas)",
        }

    if basis == "mass_ratio":
        if M1 is None or M2 is None:
            return {"error": "mass_ratio→mole needs molar masses M1, M2"}
        return {
            "x": mass_ratio_to_mole(v, M1, M2),
            "relation": f"w1=r/(1+r) then mass→mole, M1={M1:g}, M2={M2:g} g/mol",
            "rung": "exact (molar masses from block formulas)",
        }

    if basis == "amount_ratio":
        return {
            "x": amount_ratio_to_mole(v),
            "relation": "x1=nr/(1+nr)",
            "rung": "exact (no constants needed)",
        }

    if basis == "molarity":
        if rho is None:
            return {"error": (
                "molarity→mole needs the mixture density at each point. "
                "No same-block density column found; a density bridge from "
                "the composition library is required (align_compositions)."
            )}
        if M1 is None or M2 is None:
            return {"error": "molarity→mole needs molar masses M1, M2"}
        return {
            "x": molarity_to_mole(v, rho, M1, M2),
            "relation": (
                f"x1=c·M2/(ρ−c·(M1−M2)), per-row measured ρ, "
                f"M1={M1:g}, M2={M2:g} g/mol"
            ),
            "rung": "exact (measured same-block density)",
        }

    if basis == "volume_fraction":
        if V1 is None or V2 is None:
            return {"error": (
                "volume_fraction→mole needs PURE molar volumes V1, V2 at "
                "the fit temperature (composition-library bridge); note φ "
                "definitions vary between papers."
            )}
        return {
            "x": volume_fraction_to_mole(v, V1, V2),
            "relation": f"x1=(φ/V1)/(φ/V1+(1−φ)/V2), V1={V1:g}, V2={V2:g} m³/mol",
            "rung": "measured-bridge (pure molar volumes)",
        }

    if basis == "solvent_scoped":
        return {"error": (
            "solvent-scoped composition (fraction within a solvent "
            "subsystem) does not determine the overall binary composition — "
            "not convertible; choose a block with an overall composition axis."
        )}

    if basis == "mass_concentration":
        if rho is None:
            return {"error": (
                "mass_concentration→mole needs per-row mixture density "
                "(w1 = c_mass/ρ); provide a same-block density column or a "
                "composition-library bridge."
            )}
        if M1 is None or M2 is None:
            return {"error": "mass_concentration→mole needs molar masses M1, M2"}
        w1 = v / np.asarray(rho, dtype=float)
        return {
            "x": mass_to_mole(w1, M1, M2),
            "relation": (
                f"w1=c_mass/ρ (per-row measured ρ) then mass→mole, "
                f"M1={M1:g}, M2={M2:g} g/mol"
            ),
            "rung": "exact (measured same-block density)",
        }

    return {"error": f"Unrecognized composition basis '{basis}'"}


# ═══════════════════════════════════════════════════════════════════
#  Composition-library bridge support
# ═══════════════════════════════════════════════════════════════════
# The library (built by the align_compositions L1 alignment agent) is
# registered here so the fitting-tool basis gate can consume bridges
# without a toolbox→core→toolbox import cycle.
#
# Bridge schema (self-contained, name-agnostic):
#   {"property": "mass_density", "doi": ..., "block_number": ...,
#    "coeffs": [RK...], "pure_at_x0": float, "pure_at_x1": float,
#    "x_compound": str, "temperature_K": float|None, "r_squared": float,
#    "route": str}
# y(x) = x·pure_at_x1 + (1−x)·pure_at_x0 + RK(x)   (linear-rule bridge)

_ACTIVE_LIBRARY: dict | None = None


def set_active_library(library: dict | None) -> None:
    """Register the session's composition library (or clear with None)."""
    global _ACTIVE_LIBRARY
    _ACTIVE_LIBRARY = library


def get_active_library() -> dict | None:
    """Return the currently registered composition library, if any."""
    return _ACTIVE_LIBRARY


def eval_bridge_y(bridge: dict, x: np.ndarray) -> np.ndarray:
    """Evaluate a linear-rule bridge representation y(x) on mole fractions."""
    x = np.asarray(x, dtype=float)
    x2 = 1.0 - x
    y = x * float(bridge["pure_at_x1"]) + x2 * float(bridge["pure_at_x0"])
    diff = x - x2
    acc = np.zeros_like(x)
    for k, ak in enumerate(bridge.get("coeffs", [])):
        acc += float(ak) * diff**k
    return y + x * x2 * acc


def molarity_to_mole_via_bridge(
    c: np.ndarray, M1: float, M2: float, bridge: dict,
    *, max_iter: int = 30, tol: float = 1e-12,
) -> np.ndarray:
    """Solve x from molarity using a fitted ρ(x) bridge (fixed point).

    x = c·M2 / (ρ(x) − c·(M1−M2)); ρ evaluated from the bridge at each
    iterate.  Converges in a few iterations for physical inputs.
    """
    c = np.asarray(c, dtype=float)
    x = np.full_like(c, 0.5)
    for _ in range(max_iter):
        rho = eval_bridge_y(bridge, np.clip(x, 0.0, 1.0))
        x_new = c * M2 / (rho - c * (M1 - M2))
        if np.all(np.abs(x_new - x) < tol):
            x = x_new
            break
        x = x_new
    return x


def volume_fraction_to_mole_via_bridge(
    phi: np.ndarray, M1: float, M2: float, bridge: dict,
) -> np.ndarray:
    """φ→x using pure molar volumes from a ρ(x) bridge's endpoints.

    V_i = M_i[kg/mol] / ρ_pure,i with ρ from the bridge at x=1 / x=0.
    """
    rho1 = float(eval_bridge_y(bridge, np.array([1.0]))[0])
    rho0 = float(eval_bridge_y(bridge, np.array([0.0]))[0])
    V1 = (M1 * 1e-3) / rho1
    V2 = (M2 * 1e-3) / rho0
    return volume_fraction_to_mole(np.asarray(phi, dtype=float), V1, V2)
