"""Curated quantity, unit, and dimensional semantics for safe expressions."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable

from .errors import fail


# Base dimensions: mass, length, time, temperature, amount, electric current.
Dimension = tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction]
DIMENSIONLESS: Dimension = (Fraction(0),) * 6


def _dim(*values: int) -> Dimension:
    return tuple(Fraction(value) for value in values)  # type: ignore[return-value]


@dataclass(frozen=True)
class QuantitySemantics:
    quantity_key: str
    canonical_unit: str | None
    dimension: Dimension | None
    semantic_type: str
    is_affine: bool = False


UNIT_DIMENSIONS: dict[str, Dimension | None] = {
    "1": DIMENSIONLESS,
    "m3/mol": _dim(0, 3, 0, 0, -1, 0),
    "m6/mol2": _dim(0, 6, 0, 0, -2, 0),
    "mol/dm3": _dim(0, -3, 0, 0, 1, 0),
    "mol/m3": _dim(0, -3, 0, 0, 1, 0),
    "mol/kg": _dim(-1, 0, 0, 0, 1, 0),
    "kg/m3": _dim(1, -3, 0, 0, 0, 0),
    "m3/kg": _dim(-1, 3, 0, 0, 0, 0),
    "kJ/mol": _dim(1, 2, -2, 0, -1, 0),
    "J/(K mol)": _dim(1, 2, -2, -1, -1, 0),
    "J/(K m3)": _dim(1, -1, -2, -1, 0, 0),
    "J/(K kg)": _dim(0, 2, -2, -1, 0, 0),
    "J/g": _dim(0, 2, -2, 0, 0, 0),
    "K": _dim(0, 0, 0, 1, 0, 0),
    "kPa": _dim(1, -1, -2, 0, 0, 0),
    "kPa^n": None,
    "m2/s": _dim(0, 2, -1, 0, 0, 0),
    "S/m": _dim(-1, -3, 3, 0, 0, 2),
    "S*m2/mol": _dim(-1, 0, 3, 0, -1, 2),
    "N/m": _dim(1, 0, -2, 0, 0, 0),
    "1/K": _dim(0, 0, 0, -1, 0, 0),
    "1/kPa": _dim(-1, 1, 2, 0, 0, 0),
    "K/kPa": _dim(-1, 1, 2, 1, 0, 0),
    "MHz": _dim(0, 0, -1, 0, 0, 0),
    "Pa*s": _dim(1, -1, -1, 0, 0, 0),
    "nm": _dim(0, 1, 0, 0, 0, 0),
    "m/s": _dim(0, 1, -1, 0, 0, 0),
    "W/(m K)": _dim(1, 1, -3, -1, 0, 0),
    "kPa/K": _dim(1, -1, -2, -1, 0, 0),
    "kPa*dm3/mol": _dim(1, 2, -2, 0, -1, 0),
    "kPa*kg/mol": _dim(2, -1, -2, 0, -1, 0),
}


# Ordered longest-first. These are exact canonical quantity-key suffixes, not
# free-text name heuristics.
_UNIT_SUFFIXES: tuple[tuple[str, str], ...] = (
    ("_kpa_dm3_mol", "kPa*dm3/mol"),
    ("_kpa_kg_mol", "kPa*kg/mol"),
    ("_j_k_mol", "J/(K mol)"),
    ("_j_k_m3", "J/(K m3)"),
    ("_j_k_kg", "J/(K kg)"),
    ("_s_m2_mol", "S*m2/mol"),
    ("_m6_mol2", "m6/mol2"),
    ("_m3_mol", "m3/mol"),
    ("_mol_dm3", "mol/dm3"),
    ("_mol_m3", "mol/m3"),
    ("_mol_kg", "mol/kg"),
    ("_kg_m3", "kg/m3"),
    ("_m3_kg", "m3/kg"),
    ("_kj_mol", "kJ/mol"),
    ("_m2_s", "m2/s"),
    ("_kpa_k", "kPa/K"),
    ("_k_kpa", "K/kPa"),
    ("_1_kpa", "1/kPa"),
    ("_1_k", "1/K"),
    ("_pa_s", "Pa*s"),
    ("_w_m_k", "W/(m K)"),
    ("_n_m", "N/m"),
    ("_s_m", "S/m"),
    ("_mhz", "MHz"),
    ("_m_s", "m/s"),
    ("_j_g", "J/g"),
    ("_nm", "nm"),
    ("_kpa", "kPa"),
    ("_k", "K"),
)


_DIMENSIONLESS_MARKERS = (
    "fraction",
    "_ratio_",
    "ratio_of_",
    "activity_coefficient",
    "fugacity_coefficient",
    "compressibility_factor",
    "osmotic_coefficient",
    "ostwald_coefficient",
    "refractive_index",
    "relative_activity",
    "relative_permittivity",
    "thermodynamic_equilibrium_constant",
    "equilibrium_constant_in_terms_of_mole_fraction",
)


def _strip_component_placeholder(quantity_key: str) -> str:
    suffix = "_{DOIcomp_id}"
    return quantity_key[:-len(suffix)] if quantity_key.endswith(suffix) else quantity_key


def _canonical_unit(quantity_key: str) -> str | None:
    key = _strip_component_placeholder(quantity_key)
    if key == "equilibrium_constant_in_terms_of_partial_pressure_kpan":
        return "kPa^n"
    for suffix, unit in _UNIT_SUFFIXES:
        if key.endswith(suffix):
            return unit
    if (
        key.startswith("amount_ratio_")
        or key.startswith("mass_ratio_")
        or key.startswith("volume_ratio_")
        or any(marker in key for marker in _DIMENSIONLESS_MARKERS)
    ):
        return "1"
    return None


def _semantic_type(quantity_key: str, unit: str | None) -> str:
    key = _strip_component_placeholder(quantity_key)
    if "mole_fraction" in key:
        return "mole_fraction"
    if "mass_fraction" in key:
        return "mass_fraction"
    if "volume_fraction" in key:
        return "volume_fraction"
    if unit == "K" and "temperature" in key:
        return "thermodynamic_temperature"
    if unit == "kPa":
        if "partial_pressure" in key:
            return "partial_pressure"
        if "vapor_or_sublimation_pressure" in key:
            return "vapor_or_sublimation_pressure"
        return "pressure"
    return key


def semantics_for_quantity(quantity_key: str) -> QuantitySemantics:
    unit = _canonical_unit(quantity_key)
    dimension = UNIT_DIMENSIONS.get(unit) if unit is not None else None
    return QuantitySemantics(
        quantity_key=quantity_key,
        canonical_unit=unit,
        dimension=dimension,
        semantic_type=_semantic_type(quantity_key, unit),
        is_affine=False,
    )


def validate_semantics_coverage(quantity_keys: Iterable[str]) -> None:
    missing = sorted(
        key
        for key in quantity_keys
        if semantics_for_quantity(key).canonical_unit is None
    )
    if missing:
        fail(
            "QUANTITY_SEMANTICS_UNAVAILABLE",
            "The runtime quantity-semantics registry is incomplete.",
            "/",
            details={"quantity_keys": missing},
        )


def unit_dimension(unit: str, pointer: str) -> Dimension:
    if unit not in UNIT_DIMENSIONS:
        fail("UNIT_MISMATCH", f"Unsupported unit {unit!r}.", pointer)
    dimension = UNIT_DIMENSIONS[unit]
    if dimension is None:
        fail(
            "QUANTITY_SEMANTICS_UNAVAILABLE",
            f"Unit {unit!r} has context-dependent dimensions.",
            pointer,
        )
    return dimension


def multiply_dimensions(left: Dimension, right: Dimension) -> Dimension:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def divide_dimensions(left: Dimension, right: Dimension) -> Dimension:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def power_dimension(base: Dimension, exponent: Fraction) -> Dimension:
    return tuple(value * exponent for value in base)  # type: ignore[return-value]


def render_dimension(dimension: Dimension) -> str:
    if dimension == DIMENSIONLESS:
        return "1"
    symbols = ("kg", "m", "s", "K", "mol", "A")
    parts: list[str] = []
    for symbol, exponent in zip(symbols, dimension):
        if exponent == 0:
            continue
        parts.append(symbol if exponent == 1 else f"{symbol}^{exponent}")
    return "*".join(parts)
