"""Chemically gated baselines with explicit semantic labels."""

from __future__ import annotations

from dataclasses import replace
from typing import Any

import numpy as np

from ..tool_settings import (
    LINEAR_MOLAR_BASELINE_PREFIXES,
    NO_UNIVERSAL_IDEAL_MARKERS,
)

from ..interface import (
    BaselineKind,
    Diagnostic,
    GridPoint,
    InterpolatedCriterion,
)
from .relationships import select_unary_molar_volume_ensembles


_VOLUMETRIC_IDS = {
    "GLOBprop_1",
    "GLOBprop_28",
    "GLOBprop_41",
    "GLOBprop_67",
    "GLOBprop_74",
}




def _full_fractions(point: GridPoint) -> np.ndarray:
    independent = np.asarray(point.coordinates, dtype=float)
    return np.append(independent, 1.0 - independent.sum())


def _reported_zero_policy(quantity_key: str, presentation: str | None) -> bool:
    lowered = quantity_key.casefold()
    return (
        "excess_" in lowered
        or lowered.startswith("excess")
        or "_of_mixing" in lowered
        or (
            presentation is not None
            and "excess" in presentation.casefold()
        )
    )


def _ideal_policy(quantity_key: str) -> str | None:
    lowered = quantity_key.casefold()
    if lowered.startswith("mass_density"):
        return "density_via_ideal_molar_volume"
    if lowered.startswith(LINEAR_MOLAR_BASELINE_PREFIXES):
        return "mole_fraction_linear"
    return None


def _reference_record(
    criterion: InterpolatedCriterion,
    comp_num_id: str,
    value: float,
    point_ids: tuple[str, ...],
) -> dict[str, Any]:
    source = criterion.source
    return {
        "value": float(value),
        "unit": source.target.canonical_unit,
        "quality_score": float(source.quality_score),
        "source_key": source.source_key,
        "source": source.source_identity(),
        "BLKpoint_ids": list(point_ids),
        "n_observations": len(point_ids),
        "phase_num_id": source.phase_num_id,
        "phase_id": source.phase_id,
        "presentation": source.presentation,
        "presentation_kind": source.presentation_kind,
        "response_semantics": source.response_semantics,
        "reference_semantics": dict(source.reference_semantics),
        "constraint_signature": [
            list(value) for value in source.constraint_signature
        ],
        "state_aggregation": "reported_same_block_pure_endpoint",
        "comp_num_id": comp_num_id,
    }


def _same_block_vertex_records(
    criterion: InterpolatedCriterion,
) -> dict[str, dict[str, Any]]:
    source = criterion.source
    dimensions = source.coordinates.shape[1]
    if dimensions == 0:
        if len(source.comp_num_ids) != 1 or len(source.values) != 1:
            return {}
        comp_num_id = source.comp_num_ids[0]
        return {
            comp_num_id: _reference_record(
                criterion,
                comp_num_id,
                float(source.values[0]),
                source.point_ids[0],
            )
        }
    coordinate_ids = tuple(source.coordinate_comp_num_ids)
    closure_ids = tuple(
        comp_num_id
        for comp_num_id in source.comp_num_ids
        if comp_num_id not in coordinate_ids
    )
    if len(coordinate_ids) != dimensions or len(closure_ids) != 1:
        return {}
    vertices = {
        comp_num_id: tuple(
            1.0 if position == index else 0.0
            for position in range(dimensions)
        )
        for index, comp_num_id in enumerate(coordinate_ids)
    }
    vertices[closure_ids[0]] = tuple(0.0 for _ in range(dimensions))
    records: dict[str, dict[str, Any]] = {}
    for comp_num_id, vertex in vertices.items():
        distances = np.max(
            np.abs(source.coordinates - np.asarray(vertex)[np.newaxis, :]),
            axis=1,
        )
        matches = np.where(distances <= 1e-10)[0]
        if not len(matches):
            continue
        index = int(matches[0])
        records[comp_num_id] = _reference_record(
            criterion,
            comp_num_id,
            float(source.values[index]),
            source.point_ids[index],
        )
    return records


def _compatible_external_reference(
    criterion: InterpolatedCriterion,
    record: dict[str, Any],
) -> bool:
    source = criterion.source
    if record.get("unit") != source.target.canonical_unit:
        return False
    if (
        source.phase_num_id is not None
        and record.get("phase_num_id") != source.phase_num_id
    ):
        return False
    return record.get("response_semantics") == "absolute_target"


def _distribution(
    criterion: InterpolatedCriterion,
    comp_num_id: str,
    tier: str,
    records: list[dict[str, Any]],
) -> dict[str, Any]:
    values = np.asarray([record["value"] for record in records], dtype=float)
    if not len(values) or not np.all(np.isfinite(values)):
        raise ValueError("unary reference ensemble contains invalid values")
    median = float(np.median(values))
    ensemble_id = (
        f"{criterion.source.source_key}::{criterion.source.target.quantity_key}"
        f"::{comp_num_id}::{tier}"
    )
    return {
        "ensemble_id": ensemble_id,
        "comp_num_id": comp_num_id,
        "quantity_key": criterion.source.target.quantity_key,
        "canonical_unit": criterion.source.target.canonical_unit,
        "reference_tier": tier,
        "representative_value": float(np.mean(values)),
        "distribution": {
            "mean": float(np.mean(values)),
            "median": median,
            "standard_deviation": float(np.std(values, ddof=0)),
            "minimum": float(np.min(values)),
            "maximum": float(np.max(values)),
            "q1": float(np.quantile(values, 0.25)),
            "q3": float(np.quantile(values, 0.75)),
            "median_absolute_deviation": float(
                np.median(np.abs(values - median))
            ),
            "n_sources": len(records),
            "n_observations": sum(
                int(record.get("n_observations", 0))
                for record in records
            ),
        },
        "selection_context": {
            "consumer": criterion.source.source_identity(),
            "phase_num_id": criterion.source.phase_num_id,
            "phase_id": criterion.source.phase_id,
            "presentation": criterion.source.presentation,
            "ref_phase_num_id": criterion.source.reference_semantics.get(
                "ref_phase_num_id"
            ),
            "constraint_signature": [
                list(value)
                for value in criterion.source.constraint_signature
            ],
        },
        "sources": records,
    }


def _contextual_reference_ensembles(
    criterion: InterpolatedCriterion,
    reference_pool: dict[str, dict[str, list[dict[str, Any]]]],
) -> list[dict[str, Any]] | None:
    vertices = _same_block_vertex_records(criterion)
    ensembles: list[dict[str, Any]] = []
    quantity_key = criterion.source.target.quantity_key
    for comp_num_id in criterion.source.comp_num_ids:
        if comp_num_id in vertices:
            ensembles.append(
                _distribution(
                    criterion,
                    comp_num_id,
                    "same_block_pure_endpoint",
                    [vertices[comp_num_id]],
                )
            )
            continue
        records = reference_pool.get(comp_num_id, {}).get(quantity_key, [])
        compatible = [
            record
            for record in records
            if _compatible_external_reference(criterion, record)
        ]
        same_doi = [
            record
            for record in compatible
            if record.get("source", {}).get("doi") == criterion.source.doi
        ]
        selected = same_doi or compatible
        if not selected:
            return None
        ensembles.append(
            _distribution(
                criterion,
                comp_num_id,
                (
                    "same_doi_unary_ensemble"
                    if same_doi
                    else "global_unary_ensemble"
                ),
                selected,
            )
        )
    return ensembles


def _point_ensemble_references(
    ensembles: list[dict[str, Any]],
) -> tuple[dict[str, Any], ...]:
    return tuple(
        {
            "ensemble_id": ensemble["ensemble_id"],
            "comp_num_id": ensemble["comp_num_id"],
            "reference_tier": ensemble["reference_tier"],
            "representative_value": ensemble["representative_value"],
            **ensemble["distribution"],
        }
        for ensemble in ensembles
    )


def _baseline_value(
    criterion: InterpolatedCriterion,
    point: GridPoint,
    pure_values: list[float],
    policy: str,
) -> float | None:
    x = _full_fractions(point)
    if len(x) != len(pure_values):
        return None
    if policy == "mole_fraction_linear":
        return float(np.dot(x, np.asarray(pure_values)))
    if policy == "density_via_ideal_molar_volume":
        masses = criterion.source.derivation.get("molar_masses_g_mol", {})
        ordered_masses = np.array(
            [masses.get(comp_num_id) for comp_num_id in criterion.source.comp_num_ids],
            dtype=float,
        )
        densities = np.asarray(pure_values, dtype=float)
        if (
            not np.all(np.isfinite(ordered_masses))
            or not np.all(np.isfinite(densities))
            or np.any(densities <= 0)
        ):
            return None
        molar_volumes = ordered_masses * 1e-3 / densities
        ideal_volume = float(np.dot(x, molar_volumes))
        mixture_molar_mass = float(np.dot(x, ordered_masses * 1e-3))
        if ideal_volume <= 0:
            return None
        return mixture_molar_mass / ideal_volume
    return None


def _volumetric_reference_ensembles(
    criterion: InterpolatedCriterion,
    reference_pool: dict[str, dict[str, list[dict[str, Any]]]],
) -> tuple[np.ndarray | None, list[dict[str, Any]]]:
    source = criterion.source
    pure, ensembles = select_unary_molar_volume_ensembles(
        source.comp_num_ids,
        reference_pool,
        doi=source.doi,
        phase_num_id=source.phase_num_id,
    )
    if pure is None:
        return None, []
    normalized: list[dict[str, Any]] = []
    for ensemble in ensembles:
        comp_num_id = ensemble["comp_num_id"]
        normalized.append(
            {
                "ensemble_id": (
                    f"{source.source_key}::molar_volume_m3_mol::"
                    f"{comp_num_id}::{ensemble['reference_tier']}"
                ),
                "comp_num_id": comp_num_id,
                "quantity_key": "molar_volume_m3_mol",
                "canonical_unit": "m3/mol",
                **ensemble,
                "selection_context": {
                    "consumer": source.source_identity(),
                    "phase_num_id": source.phase_num_id,
                    "constraint_signature": [
                        list(value) for value in source.constraint_signature
                    ],
                },
            }
        )
    return pure, normalized


def _volumetric_ideal_value(
    criterion: InterpolatedCriterion,
    point: GridPoint,
    pure_molar_volumes: np.ndarray,
) -> float | None:
    source = criterion.source
    x = _full_fractions(point)
    if len(x) != len(pure_molar_volumes):
        return None
    ideal_vm = float(np.dot(x, pure_molar_volumes))
    if not np.isfinite(ideal_vm) or ideal_vm <= 0:
        return None
    target_id = source.target.source_global_id
    if target_id == "GLOBprop_41":
        return ideal_vm
    if target_id == "GLOBprop_67":
        return 1.0 / ideal_vm
    masses = source.derivation.get("molar_masses_g_mol", {})
    mass_vector = np.asarray(
        [masses.get(comp_num_id, np.nan) for comp_num_id in source.comp_num_ids],
        dtype=float,
    ) * 1e-3
    if not np.all(np.isfinite(mass_vector)):
        return None
    mixture_mass = float(np.dot(x, mass_vector))
    if target_id == "GLOBprop_1":
        return mixture_mass / ideal_vm
    if target_id == "GLOBprop_74" and mixture_mass > 0:
        return ideal_vm / mixture_mass
    return None


def apply_baselines(
    criteria: list[InterpolatedCriterion],
    unary_reference_pool: dict[
        str, dict[str, list[dict[str, Any]]]
    ],
) -> tuple[list[InterpolatedCriterion], list[Diagnostic]]:
    """Attach coherent real/ideal/deviation fields to each grid point."""
    diagnostics: list[Diagnostic] = []
    output: list[InterpolatedCriterion] = []
    for criterion in criteria:
        if criterion.source.response_semantics != "absolute_target":
            raise ValueError(
                "baseline evaluation received a non-absolute response: "
                f"{criterion.source.source_key} "
                f"({criterion.source.response_semantics})"
            )
        target = criterion.source.target
        if target.basis == "real":
            output.append(criterion)
            continue
        quantity_key = target.quantity_key
        if _reported_zero_policy(quantity_key, criterion.source.presentation):
            criterion.grid_points = [
                replace(
                    point,
                    ideal_value=0.0,
                    deviation=point.real_value,
                    baseline_kind=BaselineKind.REPORTED_EXCESS_ZERO,
                )
                for point in criterion.grid_points
            ]
            output.append(criterion)
            continue

        if target.source_global_id in _VOLUMETRIC_IDS:
            pure_vm, ensembles = _volumetric_reference_ensembles(
                criterion, unary_reference_pool
            )
            if pure_vm is None:
                message = (
                    "The requested volumetric ideal/deviation basis needs "
                    "phase-compatible pure molar-volume ensembles for every "
                    "component; the selected real experimental curve remains valid."
                )
                diagnostics.append(
                    Diagnostic(
                        code="VOLUMETRIC_BASELINE_ENDPOINTS_MISSING",
                        message=message,
                        stage="baseline",
                        source_key=criterion.source.source_key,
                    )
                )
                criterion.baseline_message = message
                output.append(criterion)
                continue
            point_references = _point_ensemble_references(ensembles)
            new_points: list[GridPoint] = []
            for point in criterion.grid_points:
                ideal = _volumetric_ideal_value(
                    criterion, point, pure_vm
                )
                if ideal is None:
                    continue
                new_points.append(
                    replace(
                        point,
                        ideal_value=ideal,
                        deviation=point.real_value - ideal,
                        baseline_kind=BaselineKind.THERMODYNAMIC_IDEAL,
                        baseline_sources=point_references,
                    )
                )
            criterion.grid_points = new_points
            criterion.baseline_reference_ensembles = ensembles
            criterion.baseline_message = (
                "Ideal volumetric response was calculated in molar-volume "
                "space from pure-component ensembles and transformed once "
                "to the requested response quantity."
            )
            output.append(criterion)
            continue

        policy = _ideal_policy(quantity_key)
        ensembles = _contextual_reference_ensembles(
            criterion, unary_reference_pool
        )
        baseline_kind = BaselineKind.THERMODYNAMIC_IDEAL
        baseline_message: str | None = None
        if ensembles is None:
            message = (
                "The requested ideal/deviation basis lacks complete pure "
                "reference ensembles with matching state, phase, "
                "presentation, and reference-state semantics. The real "
                "measured series remains valid and was not discarded "
                "globally."
            )
            diagnostics.append(
                Diagnostic(
                    code="BASELINE_ENDPOINTS_MISSING",
                    message=message,
                    stage="baseline",
                    source_key=criterion.source.source_key,
                )
            )
            criterion.baseline_message = message
            output.append(criterion)
            continue

        criterion.baseline_reference_ensembles = ensembles
        pure_values = [
            float(ensemble["representative_value"])
            for ensemble in ensembles
        ]
        point_references = _point_ensemble_references(ensembles)
        tiers = ", ".join(
            f"{ensemble['comp_num_id']}={ensemble['reference_tier']}"
            for ensemble in ensembles
        )
        if policy is None:
            lowered = quantity_key.casefold()
            if target.basis == "ideal":
                message = (
                    f"No curated thermodynamic ideal-mixture rule exists for "
                    f"{quantity_key}. Reported endpoints alone do not define "
                    "an ideal property."
                )
                diagnostics.append(
                    Diagnostic(
                        code="IDEAL_POLICY_UNSUPPORTED",
                        message=message,
                        stage="baseline",
                        source_key=criterion.source.source_key,
                        details={
                            "transport_like": any(
                                marker in lowered
                                for marker in NO_UNIVERSAL_IDEAL_MARKERS
                            )
                        },
                    )
                )
                criterion.baseline_message = message
                output.append(criterion)
                continue
            policy = "mole_fraction_linear"
            baseline_kind = BaselineKind.EMPIRICAL_BOUNDARY
            baseline_message = (
                "Deviation from a linear empirical boundary reference; not "
                f"labeled as thermodynamic ideality. Reference tiers: {tiers}."
            )
        elif baseline_message is None:
            baseline_message = (
                "Pure-component references selected per compound using "
                "same-block endpoint, same-DOI unary, then global-unary "
                f"priority. Reference tiers: {tiers}."
            )

        new_points: list[GridPoint] = []
        for point in criterion.grid_points:
            ideal = _baseline_value(
                criterion, point, pure_values, policy
            )
            if ideal is None:
                continue
            new_points.append(
                replace(
                    point,
                    ideal_value=ideal,
                    deviation=point.real_value - ideal,
                    baseline_kind=baseline_kind,
                    baseline_sources=point_references,
                )
            )
        if not new_points:
            message = (
                "The baseline rule could not be evaluated with finite, "
                "dimensionally coherent reference values."
            )
            diagnostics.append(
                Diagnostic(
                    code="BASELINE_EVALUATION_FAILED",
                    message=message,
                    stage="baseline",
                    source_key=criterion.source.source_key,
                )
            )
            criterion.baseline_message = message
        else:
            criterion.grid_points = new_points
            criterion.baseline_message = baseline_message
        output.append(criterion)
    return output, diagnostics
