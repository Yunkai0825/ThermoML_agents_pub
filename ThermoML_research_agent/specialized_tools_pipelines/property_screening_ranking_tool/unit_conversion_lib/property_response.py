"""Deterministic ThermoML property-response semantics.

Dimensional conversion and response-state materialization are distinct
operations, but both must agree on the unit of the number reported by a
ThermoML property declaration. This module is the stable library boundary
for the exact presentation vocabulary, reported-unit rules, deterministic
reference-component resolution, and response equations. Runtime selection
of reference data remains in ``processing.presentation_materialization``.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any


DIRECT_PRESENTATION = "Direct value, X"
DIFFERENCE_PRESENTATION = "Difference with the reference state, X-X(REF)"
RATIO_PRESENTATION = "Ratio with the reference state, X/X(REF)"
RELATIVE_DIFFERENCE_PRESENTATION = (
    "Ratio of difference with the reference state to the reference state, "
    "[X-X(REF)]/X(REF)"
)
TEMPERATURE_DIFFERENCE_PRESENTATION = (
    "Difference between upper and lower temperature, X(T2)-X(T1)"
)

PURE_SOLVENT_SAME_STATE = (
    "Pure solvent at the same temperature and pressure"
)
PURE_SOLUTE_SAME_STATE = "Pure solute at the same temperature and pressure"
PURE_COMPONENTS_SAME_PROPORTION = (
    "Pure components in the same proportion at the same temperature and "
    "pressure"
)


class PresentationKind(StrEnum):
    DIRECT = "direct"
    REFERENCE_DIFFERENCE = "reference_difference"
    REFERENCE_RATIO = "reference_ratio"
    REFERENCE_RELATIVE_DIFFERENCE = "reference_relative_difference"
    TEMPERATURE_DIFFERENCE = "temperature_difference"
    UNKNOWN = "unknown"


_KINDS = {
    DIRECT_PRESENTATION: PresentationKind.DIRECT,
    DIFFERENCE_PRESENTATION: PresentationKind.REFERENCE_DIFFERENCE,
    RATIO_PRESENTATION: PresentationKind.REFERENCE_RATIO,
    RELATIVE_DIFFERENCE_PRESENTATION: (
        PresentationKind.REFERENCE_RELATIVE_DIFFERENCE
    ),
    TEMPERATURE_DIFFERENCE_PRESENTATION: (
        PresentationKind.TEMPERATURE_DIFFERENCE
    ),
}


def classify_presentation(value: object) -> PresentationKind:
    """Return the exact normalized presentation kind, failing closed."""
    if not isinstance(value, str):
        return PresentationKind.UNKNOWN
    return _KINDS.get(value.strip(), PresentationKind.UNKNOWN)


def presentation_requires_reference(kind: PresentationKind) -> bool:
    return kind in {
        PresentationKind.REFERENCE_DIFFERENCE,
        PresentationKind.REFERENCE_RATIO,
        PresentationKind.REFERENCE_RELATIVE_DIFFERENCE,
    }


def reported_canonical_unit(
    kind: PresentationKind,
    property_canonical_unit: str,
) -> str:
    """Return the unit of the reported number before materialization."""
    if kind in {
        PresentationKind.REFERENCE_RATIO,
        PresentationKind.REFERENCE_RELATIVE_DIFFERENCE,
    }:
        return "1"
    return property_canonical_unit


def reference_component_num_ids(
    block: dict[str, Any],
    declaration: dict[str, Any],
) -> tuple[tuple[str, ...], str]:
    """Resolve component identities required by an exact reference state.

    Ambiguous multi-solvent or multi-solute references are reported instead
    of being reduced to an arbitrary component.
    """
    compounds = [
        item
        for item in block.get("compounds", [])
        if isinstance(item, dict)
        and isinstance(item.get("org_num"), str)
        and isinstance(item.get("comp_num_id"), str)
    ]
    by_org = {
        str(item["org_num"]): str(item["comp_num_id"])
        for item in compounds
    }
    solvent_ids = tuple(
        sorted(
            {
                str(item["comp_num_id"])
                for item in block.get("solvents", [])
                if isinstance(item, dict)
                and isinstance(item.get("comp_num_id"), str)
            }
        )
    )
    ref_phase = declaration.get("ref_phase")
    if isinstance(ref_phase, dict):
        org_num = ref_phase.get("component_org_num")
        if isinstance(org_num, str) and org_num in by_org:
            return (by_org[org_num],), "resolved_from_ref_phase_component"

    state = declaration.get("ref_state_type")
    if state == PURE_SOLVENT_SAME_STATE:
        if len(solvent_ids) == 1:
            return solvent_ids, "resolved_unique_solvent"
        return (), (
            "ambiguous_solvent_reference"
            if solvent_ids
            else "solvent_reference_missing"
        )
    if state == PURE_SOLUTE_SAME_STATE:
        solutes = tuple(
            sorted(set(by_org.values()).difference(solvent_ids))
        )
        if len(solutes) == 1:
            return solutes, "resolved_unique_solute"
        return (), (
            "ambiguous_solute_reference"
            if solutes
            else "solute_reference_missing"
        )
    if state == PURE_COMPONENTS_SAME_PROPORTION:
        return (
            tuple(sorted(set(by_org.values()))),
            "resolved_all_pure_components",
        )
    return (), "reference_component_not_deterministically_resolved"


def materialize_reported_response(
    kind: PresentationKind,
    reported: Any,
    reference: Any,
) -> tuple[Any, str]:
    """Apply one exact response equation to scalar or array-like values."""
    if kind == PresentationKind.REFERENCE_RATIO:
        return reported * reference, "X = (X/X_ref) * X_ref"
    if kind == PresentationKind.REFERENCE_DIFFERENCE:
        return reported + reference, "X = (X-X_ref) + X_ref"
    if kind == PresentationKind.REFERENCE_RELATIVE_DIFFERENCE:
        return (1.0 + reported) * reference, (
            "X = (1 + (X-X_ref)/X_ref) * X_ref"
        )
    raise ValueError(f"presentation {kind.value!r} is not materializable")
