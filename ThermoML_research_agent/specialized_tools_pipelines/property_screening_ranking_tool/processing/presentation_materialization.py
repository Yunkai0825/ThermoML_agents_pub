"""Materialize ThermoML reference presentations into absolute quantities.

This stage is deliberately separate from unit conversion and from the
cross-property relationship graph.  It transforms the reported mathematical
response (for example ``X/X(REF)``) into the absolute observed property while
retaining the complete reference ensemble and source provenance.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Any

import numpy as np

from ..interface import Diagnostic, SourceSeries
from ..unit_conversion_lib.property_response import (
    PURE_COMPONENTS_SAME_PROPORTION,
    PURE_SOLUTE_SAME_STATE,
    PURE_SOLVENT_SAME_STATE,
    PresentationKind,
    materialize_reported_response,
)


_SUPPORTED_UNARY_REFERENCE_STATES = {
    PURE_SOLVENT_SAME_STATE,
    PURE_SOLUTE_SAME_STATE,
    PURE_COMPONENTS_SAME_PROPORTION,
}


def _compatible_reference_records(
    source: SourceSeries,
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    expected_phase = (
        source.reference_semantics.get("ref_phase_num_id")
        or source.phase_num_id
    )
    return [
        record
        for record in records
        if record.get("unit") == source.observed_canonical_unit
        and record.get("response_semantics") == "absolute_target"
        and record.get("presentation_kind") == PresentationKind.DIRECT.value
        and (
            expected_phase is None
            or record.get("phase_num_id") == expected_phase
        )
    ]


def _component_reference_ensemble(
    source: SourceSeries,
    reference_pool: dict[str, dict[str, list[dict[str, Any]]]],
    comp_num_id: str,
) -> tuple[dict[str, Any] | None, str | None]:
    quantity_key = (
        source.observed_quantity_key or source.target.quantity_key
    )
    compatible = _compatible_reference_records(
        source,
        reference_pool.get(comp_num_id, {}).get(quantity_key, []),
    )
    same_doi = [
        record
        for record in compatible
        if record.get("source", {}).get("doi") == source.doi
    ]
    selected = same_doi or compatible
    if not selected:
        return None, "absolute_unary_reference_unavailable"
    values = np.asarray(
        [record.get("value", np.nan) for record in selected],
        dtype=float,
    )
    if not np.all(np.isfinite(values)):
        return None, "nonfinite_unary_reference"
    representative = float(np.mean(values))
    return {
        "comp_num_id": comp_num_id,
        "quantity_key": quantity_key,
        "canonical_unit": source.observed_canonical_unit,
        "reference_tier": (
            "same_doi_unary_ensemble"
            if same_doi
            else "global_unary_ensemble"
        ),
        "representative_value": representative,
        "distribution": {
            "mean": representative,
            "median": float(np.median(values)),
            "standard_deviation": float(np.std(values, ddof=0)),
            "minimum": float(np.min(values)),
            "maximum": float(np.max(values)),
            "n_sources": len(selected),
            "n_observations": sum(
                int(record.get("n_observations", 0))
                for record in selected
            ),
        },
        "sources": selected,
    }, None


def _full_fraction_matrix(source: SourceSeries) -> np.ndarray:
    """Return all component mole fractions in source component order."""
    n_rows = len(source.values)
    fractions = np.zeros((n_rows, len(source.comp_num_ids)), dtype=float)
    index_by_id = {
        comp_num_id: index
        for index, comp_num_id in enumerate(source.comp_num_ids)
    }
    for axis, comp_num_id in enumerate(source.coordinate_comp_num_ids):
        if comp_num_id not in index_by_id:
            raise ValueError(
                f"composition axis {comp_num_id} is absent from source system"
            )
        fractions[:, index_by_id[comp_num_id]] = source.coordinates[:, axis]
    closure = [
        comp_num_id
        for comp_num_id in source.comp_num_ids
        if comp_num_id not in source.coordinate_comp_num_ids
    ]
    if len(closure) != 1:
        raise ValueError("reference mixture has ambiguous composition closure")
    fractions[:, index_by_id[closure[0]]] = 1.0 - np.sum(
        source.coordinates, axis=1
    )
    if np.any(fractions < -1e-10) or np.any(fractions > 1.0 + 1e-10):
        raise ValueError("reference mixture composition is outside the simplex")
    return np.clip(fractions, 0.0, 1.0)


def _reference_ensemble(
    source: SourceSeries,
    reference_pool: dict[str, dict[str, list[dict[str, Any]]]],
) -> tuple[dict[str, Any] | None, str | None]:
    state = source.reference_semantics.get("ref_state_type")
    if state not in _SUPPORTED_UNARY_REFERENCE_STATES:
        return None, f"unsupported_reference_state:{state}"
    component_ids = tuple(
        str(value)
        for value in (
            source.reference_semantics.get("reference_comp_num_ids") or ()
        )
    )
    if state in {PURE_SOLVENT_SAME_STATE, PURE_SOLUTE_SAME_STATE}:
        if len(component_ids) != 1:
            reason = source.reference_semantics.get(
                "reference_component_resolution",
                "reference_component_unresolved",
            )
            return None, str(reason)
        ensemble, failure = _component_reference_ensemble(
            source, reference_pool, component_ids[0]
        )
        if ensemble is not None:
            ensemble["reference_state_type"] = state
            ensemble["reference_equation"] = "X_ref = X_pure_component"
        return ensemble, failure

    if set(component_ids) != set(source.comp_num_ids):
        return None, "pure_component_reference_set_does_not_match_system"
    component_ensembles: list[dict[str, Any]] = []
    for comp_num_id in source.comp_num_ids:
        ensemble, failure = _component_reference_ensemble(
            source, reference_pool, comp_num_id
        )
        if ensemble is None:
            return None, f"{comp_num_id}:{failure}"
        component_ensembles.append(ensemble)
    fractions = _full_fraction_matrix(source)
    pure_values = np.asarray(
        [
            float(ensemble["representative_value"])
            for ensemble in component_ensembles
        ],
        dtype=float,
    )
    row_reference_values = fractions @ pure_values
    return {
        "comp_num_ids": list(source.comp_num_ids),
        "quantity_key": (
            source.observed_quantity_key or source.target.quantity_key
        ),
        "canonical_unit": source.observed_canonical_unit,
        "reference_state_type": state,
        "reference_equation": "X_ref(row) = sum_i x_i * X_i,pure",
        "component_ensembles": component_ensembles,
        "sources": [
            record
            for ensemble in component_ensembles
            for record in ensemble["sources"]
        ],
        "row_reference_values": row_reference_values.tolist(),
    }, None


def materialize_property_presentations(
    sources: list[SourceSeries],
    reference_pool: dict[str, dict[str, list[dict[str, Any]]]],
) -> tuple[list[SourceSeries], list[Diagnostic]]:
    """Return only absolute observed quantities, failing closed."""
    output: list[SourceSeries] = []
    diagnostics: list[Diagnostic] = []
    for source in sources:
        kind = PresentationKind(source.presentation_kind)
        if kind == PresentationKind.DIRECT:
            output.append(
                replace(
                    source,
                    response_semantics="absolute_observed_quantity",
                    derivation={
                        **source.derivation,
                        "presentation_materialization": {
                            "status": "identity",
                            "reported_presentation": source.presentation,
                            "presentation_kind": kind.value,
                            "reported_unit": source.reported_unit,
                            "absolute_observed_unit": (
                                source.observed_canonical_unit
                            ),
                            "equation": "X = reported X",
                        },
                    },
                )
            )
            continue
        if kind in {
            PresentationKind.UNKNOWN,
            PresentationKind.TEMPERATURE_DIFFERENCE,
        }:
            diagnostics.append(
                Diagnostic(
                    code="PROPERTY_PRESENTATION_UNSUPPORTED",
                    message=(
                        f"{source.presentation!r} is not an absolute "
                        "single-state response and cannot enter property "
                        "ranking."
                    ),
                    stage="presentation_materialization",
                    severity="warning",
                    source_key=source.source_key,
                    details={
                        "presentation": source.presentation,
                        "presentation_kind": kind.value,
                    },
                )
            )
            continue

        ensemble, failure = _reference_ensemble(source, reference_pool)
        if ensemble is None:
            diagnostics.append(
                Diagnostic(
                    code="REFERENCE_STATE_MATERIALIZATION_UNRESOLVED",
                    message=(
                        f"{source.presentation!r} could not be converted "
                        f"to an absolute property: {failure}."
                    ),
                    stage="presentation_materialization",
                    severity="warning",
                    source_key=source.source_key,
                    details={
                        "presentation": source.presentation,
                        "presentation_kind": kind.value,
                        "reference_semantics": (
                            source.reference_semantics
                        ),
                        "failure_reason": failure,
                    },
                )
            )
            continue
        reference_values: float | np.ndarray
        if "row_reference_values" in ensemble:
            reference_values = np.asarray(
                ensemble["row_reference_values"], dtype=float
            )
        else:
            reference_values = float(ensemble["representative_value"])
        converted, equation = materialize_reported_response(
            kind,
            np.asarray(source.values, dtype=float),
            reference_values,
        )
        if not np.all(np.isfinite(converted)):
            diagnostics.append(
                Diagnostic(
                    code="REFERENCE_STATE_MATERIALIZATION_NONFINITE",
                    message=(
                        "Reference-state materialization produced a "
                        "non-finite absolute property."
                    ),
                    stage="presentation_materialization",
                    severity="warning",
                    source_key=source.source_key,
                )
            )
            continue
        output.append(
            replace(
                source,
                values=converted,
                response_semantics="absolute_observed_quantity",
                evidence_relation=f"materialized_{kind.value}",
                derivation={
                    **source.derivation,
                    "presentation_materialization": {
                        "status": "materialized",
                        "reported_presentation": source.presentation,
                        "presentation_kind": kind.value,
                        "reported_unit": source.reported_unit,
                        "absolute_observed_unit": (
                            source.observed_canonical_unit
                        ),
                        "equation": equation,
                        "reference_ensemble": ensemble,
                    },
                },
            )
        )
    return output, diagnostics
