"""Assemble coherent criteria and rank systems within comparable classes."""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Any

import numpy as np

from ..interface import Diagnostic, InterpolatedCriterion, NormalizedRequest
from ..tool_settings import (
    RANKING_SCORE_ABSOLUTE_TOLERANCE,
    RANKING_SCORE_RELATIVE_TOLERANCE,
    RANKING_SCORE_SIGNIFICANT_DIGITS,
    SECONDARY_RANKING_LIMIT_DIVISOR,
)


@dataclass
class RankingResult:
    rankings: list[dict[str, Any]]
    secondary_grid_rankings: list[dict[str, Any]]
    diagnostics: list[Diagnostic]
    n_eligible_candidates: int
    n_incomplete_candidates: int
    n_secondary_candidate_occurrences: int
    n_secondary_returned_occurrences: int


def _criterion_key(criterion: InterpolatedCriterion) -> tuple[Any, ...]:
    target = criterion.source.target
    return (
        target.input_value,
        target.quantity_key,
        target.basis,
        target.direction,
        target.aggregate,
        target.ranking_composition,
    )


def _system_key(criterion: InterpolatedCriterion) -> tuple[Any, ...]:
    source = criterion.source
    return (
        tuple(source.comp_num_ids),
        source.system_type,
        source.phase_num_id,
        source.constraint_signature,
        source.response_semantics,
    )


def _value_for_basis(point: dict[str, Any], basis: str) -> float | None:
    value = {
        "real": point["real_value"],
        "ideal": point["ideal_value"],
        "deviation": point["deviation"],
        "absolute_deviation": point["absolute_deviation"],
    }[basis]
    return float(value) if isinstance(value, (int, float)) else None


def _aggregate(
    values: list[float],
    coordinates: list[tuple[float, ...]],
    aggregate: str,
) -> float | None:
    if not values:
        return None
    array = np.asarray(values, dtype=float)
    if aggregate == "mean":
        return float(np.mean(array))
    if aggregate == "maximum":
        return float(np.max(array))
    if aggregate == "minimum":
        return float(np.min(array))
    if aggregate == "integral":
        if not coordinates or len(coordinates[0]) != 1:
            return None
        x = np.asarray([point[0] for point in coordinates], dtype=float)
        order = np.argsort(x)
        if len(np.unique(x)) < 2:
            return None
        return float(np.trapezoid(array[order], x[order]))
    raise ValueError(f"unsupported aggregate {aggregate!r}")


def _quantized(value: float) -> float:
    """Collapse binary floating noise without erasing chemical differences."""
    return float(f"{value:.{RANKING_SCORE_SIGNIFICANT_DIGITS}g}")


def _normalize_scores(
    rows: list[dict[str, Any]],
    criterion_key: tuple[Any, ...],
    direction: str,
) -> None:
    values = np.asarray(
        [_quantized(row["criterion_values"][criterion_key]) for row in rows],
        dtype=float,
    )
    low = float(values.min())
    high = float(values.max())
    scale = max(1.0, abs(low), abs(high))
    tolerance = max(
        RANKING_SCORE_ABSOLUTE_TOLERANCE,
        RANKING_SCORE_RELATIVE_TOLERANCE * scale,
    )
    if high - low <= tolerance:
        scores = np.ones_like(values)
    elif direction == "maximize":
        scores = (values - low) / (high - low)
    else:
        scores = (high - values) / (high - low)
    for row, score in zip(rows, scores):
        row["criterion_scores"][criterion_key] = round(
            float(np.clip(score, 0.0, 1.0)), 12
        )


def _common_ranking_coordinates(
    criteria: list[InterpolatedCriterion],
) -> set[tuple[float, ...]]:
    sets: list[set[tuple[float, ...]]] = []
    for criterion in criteria:
        available = {
            tuple(point.coordinates) for point in criterion.grid_points
        }
        sets.append(available.intersection(criterion.ranking_coordinates))
    return set.intersection(*sets) if sets else set()


def _secondary_composition_grid(
    criterion: InterpolatedCriterion,
) -> dict[str, Any] | None:
    requested = criterion.secondary_composition_coordinates
    if not requested:
        return None
    source = criterion.source
    coordinate_ids = source.coordinate_comp_num_ids
    if len(coordinate_ids) != len(requested[0]):
        raise ValueError(
            f"secondary-grid dimensions do not match coordinate IDs for "
            f"{source.source_key}"
        )
    closure_ids = [
        comp_num_id
        for comp_num_id in source.comp_num_ids
        if comp_num_id not in coordinate_ids
    ]
    if len(closure_ids) != 1:
        raise ValueError(
            f"secondary-grid closure is ambiguous for {source.source_key}"
        )
    closure_id = closure_ids[0]
    names_by_id = dict(zip(source.comp_num_ids, source.compound_names))
    points_by_coordinate = {
        tuple(point.coordinates): point for point in criterion.grid_points
    }
    values: list[dict[str, Any]] = []
    failure_counts: dict[str, int] = {}
    for coordinate in requested:
        independent = dict(zip(coordinate_ids, coordinate))
        closure_fraction = round(1.0 - sum(coordinate), 12)
        if abs(closure_fraction) < 1e-12:
            closure_fraction = 0.0
        full_composition = [
            {
                "comp_num_id": comp_num_id,
                "compound_name": names_by_id[comp_num_id],
                "mole_fraction": (
                    independent[comp_num_id]
                    if comp_num_id in independent
                    else closure_fraction
                ),
            }
            for comp_num_id in source.comp_num_ids
        ]
        point = points_by_coordinate.get(coordinate)
        if point is None:
            reason = criterion.grid_failures.get(
                coordinate, "not_interpolable"
            )
            failure_counts[reason] = failure_counts.get(reason, 0) + 1
            values.append(
                {
                    "composition": list(coordinate),
                    "full_composition": full_composition,
                    "available": False,
                    "coverage_failure_reason": reason,
                    "real_value": None,
                    "ideal_value": None,
                    "deviation": None,
                    "absolute_deviation": None,
                    "source_point_ids": [],
                    "interpolation_kind": "unavailable",
                    "baseline_kind": "not_requested",
                    "baseline_sources": [],
                }
            )
            continue
        row = point.as_dict()
        row["full_composition"] = full_composition
        row["available"] = True
        row["coverage_failure_reason"] = None
        values.append(row)
    available = sum(bool(row["available"]) for row in values)
    axis = sorted(
        {coordinate for point in requested for coordinate in point}
    )
    return {
        "role": "secondary_information_not_used_for_ranking",
        "dimensions": len(coordinate_ids),
        "axis": axis,
        "coordinate_comp_num_ids": list(coordinate_ids),
        "coordinate_compound_names": [
            names_by_id[comp_num_id] for comp_num_id in coordinate_ids
        ],
        "closure_comp_num_id": closure_id,
        "closure_compound_name": names_by_id[closure_id],
        "grid": [list(coordinate) for coordinate in requested],
        "coverage": {
            "requested": len(values),
            "available": available,
            "unavailable": len(values) - available,
            "unavailable_by_reason": failure_counts,
        },
        "values": values,
    }


def _ranking_grid_coverage(
    criterion: InterpolatedCriterion,
    used_coordinates: set[tuple[float, ...]],
) -> dict[str, Any]:
    points_by_coordinate = {
        tuple(point.coordinates): point for point in criterion.grid_points
    }
    values: list[dict[str, Any]] = []
    failure_counts: dict[str, int] = {}
    n_interpolated = 0
    n_used = 0
    for coordinate in criterion.ranking_coordinates:
        point = points_by_coordinate.get(coordinate)
        if point is None:
            reason = criterion.grid_failures.get(
                coordinate, "not_interpolable"
            )
            failure_counts[reason] = failure_counts.get(reason, 0) + 1
            values.append(
                {
                    "composition": list(coordinate),
                    "available": False,
                    "used_for_ranking": False,
                    "coverage_failure_reason": reason,
                    "real_value": None,
                    "ideal_value": None,
                    "deviation": None,
                    "absolute_deviation": None,
                    "source_point_ids": [],
                    "interpolation_kind": "unavailable",
                    "baseline_kind": "not_requested",
                    "baseline_sources": [],
                }
            )
            continue
        n_interpolated += 1
        row = point.as_dict()
        row["available"] = True
        row["used_for_ranking"] = coordinate in used_coordinates
        row["coverage_failure_reason"] = None
        n_used += int(row["used_for_ranking"])
        values.append(row)
    return {
        "requested": len(criterion.ranking_coordinates),
        "interpolated": n_interpolated,
        "used_for_ranking": n_used,
        "unavailable": len(criterion.ranking_coordinates) - n_interpolated,
        "unavailable_by_reason": failure_counts,
        "values": values,
    }


def _available_coordinates(
    criterion: InterpolatedCriterion,
) -> set[tuple[float, ...]]:
    return {tuple(point.coordinates) for point in criterion.grid_points}


def _has_primary_coverage(
    system_criteria: dict[tuple[Any, ...], InterpolatedCriterion],
    requested_keys: list[tuple[Any, ...]],
) -> bool:
    return all(
        bool(
            _available_coordinates(system_criteria[target_key]).intersection(
                system_criteria[target_key].ranking_coordinates
            )
        )
        for target_key in requested_keys
    )


def _ranking_group_payload(
    system_key: tuple[Any, ...],
) -> dict[str, Any]:
    return {
        "effective_cardinality": len(system_key[0]),
        "system_type": system_key[1],
        "phase_num_id": system_key[2],
        "constraint_signature": [list(value) for value in system_key[3]],
        "response_semantics": system_key[4],
    }


def _full_composition(
    criterion: InterpolatedCriterion,
    coordinate: tuple[float, ...],
) -> tuple[list[dict[str, Any]], str, str]:
    source = criterion.source
    coordinate_ids = source.coordinate_comp_num_ids
    if len(coordinate_ids) != len(coordinate):
        raise ValueError(
            "secondary ranking coordinate dimensions do not match "
            f"{source.source_key}"
        )
    closure_ids = [
        value for value in source.comp_num_ids if value not in coordinate_ids
    ]
    if len(closure_ids) != 1:
        raise ValueError(
            f"secondary ranking closure is ambiguous for {source.source_key}"
        )
    closure_id = closure_ids[0]
    names_by_id = dict(zip(source.comp_num_ids, source.compound_names))
    independent = dict(zip(coordinate_ids, coordinate))
    closure_fraction = round(1.0 - sum(coordinate), 12)
    if abs(closure_fraction) < 1e-12:
        closure_fraction = 0.0
    full = [
        {
            "comp_num_id": comp_num_id,
            "compound_name": names_by_id[comp_num_id],
            "mole_fraction": (
                independent[comp_num_id]
                if comp_num_id in independent
                else closure_fraction
            ),
        }
        for comp_num_id in source.comp_num_ids
    ]
    return full, closure_id, names_by_id[closure_id]


def _active_composition(
    full_composition: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], tuple[tuple[str, float], ...]]:
    """Return the chemically present system at one regulated grid point."""
    active = [
        dict(component)
        for component in full_composition
        if float(component["mole_fraction"]) > 1e-12
    ]
    total = sum(float(component["mole_fraction"]) for component in active)
    if total <= 0.0:
        raise ValueError("regulated composition has no active component")
    for component in active:
        component["mole_fraction"] = round(
            float(component["mole_fraction"]) / total, 12
        )
    signature = tuple(
        (
            str(component["comp_num_id"]),
            float(component["mole_fraction"]),
        )
        for component in sorted(
            active, key=lambda value: str(value["comp_num_id"])
        )
    )
    return active, signature


def _system_type_for_cardinality(cardinality: int) -> str:
    names = {1: "unary", 2: "binary", 3: "ternary", 4: "quaternary"}
    return names.get(cardinality, f"{cardinality}_component")


def _active_row_priority(row: dict[str, Any]) -> tuple[Any, ...]:
    """Prefer direct evidence, then the strongest selected parent curve."""
    return (
        float(row["direct_evidence_fraction"]),
        float(row["pre_dedup_quality_score"]),
        -len(row["parent_comp_num_ids"]),
        str(row["parent_candidate_key"]),
    )


def _deduplicate_active_rows(
    rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Keep one traceable observation for each active chemical identity."""
    grouped: dict[tuple[Any, ...], list[dict[str, Any]]] = {}
    for row in rows:
        key = (
            tuple(row["active_composition_signature"]),
            row["phase_num_id"],
            repr(row["ranking_group"]["constraint_signature"]),
            row["ranking_group"]["response_semantics"],
        )
        grouped.setdefault(key, []).append(row)

    selected: list[dict[str, Any]] = []
    for alternatives in grouped.values():
        alternatives.sort(key=_active_row_priority, reverse=True)
        winner = alternatives[0]
        winner["active_identity_selection"] = {
            "rule": (
                "direct_absolute_evidence_then_curve_quality_then_"
                "smallest_parent_system"
            ),
            "parent_occurrences": len(alternatives),
            "selected_parent_candidate_key": winner["parent_candidate_key"],
            "rejected_parent_candidate_keys": [
                row["parent_candidate_key"] for row in alternatives[1:]
            ],
        }
        selected.append(winner)
    return selected


def _coordinate_distance(
    left: tuple[float, ...], right: tuple[float, ...]
) -> float:
    return float(np.linalg.norm(np.asarray(left) - np.asarray(right)))


def _secondary_coordinate_specs(
    complete_systems: dict[
        tuple[Any, ...],
        dict[tuple[Any, ...], InterpolatedCriterion],
    ],
    requested_keys: list[tuple[Any, ...]],
) -> list[dict[str, Any]]:
    by_dimensions: dict[int, dict[str, set[tuple[float, ...]]]] = {}
    for system_criteria in complete_systems.values():
        for target_key in requested_keys:
            criterion = system_criteria[target_key]
            dimensions = len(criterion.source.coordinate_comp_num_ids)
            if dimensions == 0:
                continue
            record = by_dimensions.setdefault(
                dimensions, {"primary": set(), "secondary": set()}
            )
            record["primary"].update(criterion.ranking_coordinates)
            record["secondary"].update(
                criterion.secondary_composition_coordinates
            )

    specs: list[dict[str, Any]] = []
    for dimensions, coordinates in by_dimensions.items():
        primary = coordinates["primary"]
        for coordinate in coordinates["secondary"].difference(primary):
            nearest = (
                min(
                    primary,
                    key=lambda value: (
                        _coordinate_distance(coordinate, value),
                        value,
                    ),
                )
                if primary
                else tuple(0.0 for _ in range(dimensions))
            )
            specs.append(
                {
                    "dimensions": dimensions,
                    "coordinate": coordinate,
                    "nearest_primary_coordinate": nearest,
                    "distance_from_primary": _coordinate_distance(
                        coordinate, nearest
                    ),
                }
            )
    specs.sort(
        key=lambda row: (
            round(float(row["distance_from_primary"]), 15),
            int(row["dimensions"]),
            tuple(row["coordinate"]),
        )
    )
    for sequence, row in enumerate(specs, start=1):
        row["sequence"] = sequence
    return specs


def _secondary_panel(
    *,
    spec: dict[str, Any],
    complete_systems: dict[
        tuple[Any, ...],
        dict[tuple[Any, ...], InterpolatedCriterion],
    ],
    requested_keys: list[tuple[Any, ...]],
    request: NormalizedRequest,
    per_coordinate_limit: int,
) -> dict[str, Any]:
    coordinate = tuple(spec["coordinate"])
    dimensions = int(spec["dimensions"])
    eligible_systems: list[
        tuple[
            tuple[Any, ...],
            dict[tuple[Any, ...], InterpolatedCriterion],
        ]
    ] = []
    for system_key, system_criteria in complete_systems.items():
        if len(system_key[0]) != dimensions + 1:
            continue
        valid = True
        for target_key in requested_keys:
            criterion = system_criteria[target_key]
            point = next(
                (
                    value
                    for value in criterion.grid_points
                    if tuple(value.coordinates) == coordinate
                ),
                None,
            )
            if point is None or _value_for_basis(
                point.as_dict(), criterion.source.target.basis
            ) is None:
                valid = False
                break
        if valid:
            eligible_systems.append((system_key, system_criteria))

    classes: dict[
        tuple[Any, ...],
        list[
            tuple[
                tuple[Any, ...],
                dict[tuple[Any, ...], InterpolatedCriterion],
            ]
        ],
    ] = {}
    for system_key, system_criteria in eligible_systems:
        representative_criterion = system_criteria[requested_keys[0]]
        full_composition, _closure_id, _closure_name = _full_composition(
            representative_criterion, coordinate
        )
        active_composition, _active_signature = _active_composition(
            full_composition
        )
        active_cardinality = len(active_composition)
        class_key = (
            active_cardinality,
            _system_type_for_cardinality(active_cardinality),
            system_key[2],
            system_key[3],
            system_key[4],
        )
        classes.setdefault(class_key, []).append(
            (system_key, system_criteria)
        )

    all_rows: list[dict[str, Any]] = []
    for class_key, systems in sorted(
        classes.items(), key=lambda item: repr(item[0])
    ):
        class_rows: list[dict[str, Any]] = []
        for system_key, system_criteria in systems:
            criterion_values: dict[tuple[Any, ...], float] = {}
            criterion_payloads: dict[tuple[Any, ...], dict[str, Any]] = {}
            active_composition: list[dict[str, Any]] | None = None
            active_signature: tuple[tuple[str, float], ...] | None = None
            for target_key in requested_keys:
                criterion = system_criteria[target_key]
                point = next(
                    value
                    for value in criterion.grid_points
                    if tuple(value.coordinates) == coordinate
                )
                point_payload = point.as_dict()
                raw = _value_for_basis(
                    point_payload, criterion.source.target.basis
                )
                if raw is None:
                    raise AssertionError(
                        "secondary eligibility accepted an unavailable basis"
                    )
                full, closure_id, closure_name = _full_composition(
                    criterion, coordinate
                )
                criterion_active, criterion_signature = _active_composition(
                    full
                )
                if active_signature is None:
                    active_composition = criterion_active
                    active_signature = criterion_signature
                elif criterion_signature != active_signature:
                    raise ValueError(
                        "ranking targets disagree on active composition for "
                        f"{criterion.source.source_key} at {coordinate}"
                    )
                criterion_values[target_key] = raw
                criterion_payloads[target_key] = {
                    "target": criterion.source.target.as_dict(),
                    "source": criterion.source.source_identity(),
                    "evidence": criterion.source.evidence_identity(),
                    "source_key": criterion.source.source_key,
                    "quality_score": criterion.source.quality_score,
                    "ranking_mode": "single_regulated_coordinate",
                    "at_mole_fraction": list(coordinate),
                    "raw_value": raw,
                    "coordinate_comp_num_ids": list(
                        criterion.source.coordinate_comp_num_ids
                    ),
                    "closure_comp_num_id": closure_id,
                    "closure_compound_name": closure_name,
                    "full_composition": full,
                    "grid_point": point_payload,
                    "derivation": criterion.source.derivation,
                }
            representative = next(iter(system_criteria.values())).source
            if active_composition is None or active_signature is None:
                raise AssertionError("eligible system lacks active composition")
            active_comp_num_ids = [
                str(component["comp_num_id"])
                for component in active_composition
            ]
            names_by_id = dict(
                zip(representative.comp_num_ids, representative.compound_names)
            )
            class_rows.append(
                {
                    "candidate_key": "::".join(active_comp_num_ids),
                    "system_signature": repr(active_signature),
                    "system_type": _system_type_for_cardinality(
                        len(active_comp_num_ids)
                    ),
                    "comp_num_ids": active_comp_num_ids,
                    "compound_names": [
                        names_by_id[comp_num_id]
                        for comp_num_id in active_comp_num_ids
                    ],
                    "active_composition": active_composition,
                    "active_composition_signature": active_signature,
                    "parent_candidate_key": "::".join(system_key[0]),
                    "parent_comp_num_ids": list(representative.comp_num_ids),
                    "pre_dedup_quality_score": float(
                        np.mean(
                            [
                                payload["quality_score"]
                                for payload in criterion_payloads.values()
                            ]
                        )
                    ),
                    "direct_evidence_fraction": float(
                        np.mean(
                            [
                                payload["evidence"]["evidence_relation"]
                                == "reported_direct"
                                for payload in criterion_payloads.values()
                            ]
                        )
                    ),
                    "phase_num_id": representative.phase_num_id,
                    "phase_id": representative.phase_id,
                    "ranking_group": {
                        "effective_cardinality": len(active_comp_num_ids),
                        "system_type": _system_type_for_cardinality(
                            len(active_comp_num_ids)
                        ),
                        "phase_num_id": system_key[2],
                        "constraint_signature": [
                            list(value) for value in system_key[3]
                        ],
                        "response_semantics": system_key[4],
                    },
                    "criterion_values": criterion_values,
                    "criterion_scores": {},
                    "criterion_payloads": criterion_payloads,
                }
            )
        class_rows = _deduplicate_active_rows(class_rows)
        for target_key in requested_keys:
            if class_rows:
                direction = class_rows[0]["criterion_payloads"][target_key][
                    "target"
                ]["direction"]
                _normalize_scores(class_rows, target_key, direction)
        for row in class_rows:
            row["overall_score"] = round(
                float(np.mean(list(row["criterion_scores"].values()))), 12
            )
            row["quality_score"] = round(
                float(
                    np.mean(
                        [
                            payload["quality_score"]
                            for payload in row["criterion_payloads"].values()
                        ]
                    )
                ),
                12,
            )
            row["criteria"] = [
                {
                    **row["criterion_payloads"][target_key],
                    "score": row["criterion_scores"][target_key],
                }
                for target_key in requested_keys
            ]
            del row["criterion_values"]
            del row["criterion_scores"]
            del row["criterion_payloads"]
            del row["pre_dedup_quality_score"]
            del row["direct_evidence_fraction"]
        class_rows.sort(
            key=lambda row: (
                -row["overall_score"],
                -row["quality_score"],
                row["system_signature"],
            )
        )
        for rank, row in enumerate(class_rows, start=1):
            row["rank_within_group"] = rank
        all_rows.extend(class_rows)

    all_rows.sort(
        key=lambda row: (
            -row["overall_score"],
            -row["quality_score"],
            repr(row["ranking_group"]),
            row["system_signature"],
        )
    )
    returned = all_rows[:per_coordinate_limit]
    for rank, row in enumerate(returned, start=1):
        row["rank"] = rank
    return {
        "sequence": spec["sequence"],
        "role": (
            "pure_component_reference"
            if returned
            and all(len(row["comp_num_ids"]) == 1 for row in returned)
            else "lower_order_subsystem_ranking"
            if returned
            and any(
                len(row["comp_num_ids"]) < dimensions + 1
                for row in returned
            )
            else "secondary_context_not_primary_substitution"
        ),
        "dimensions": dimensions,
        "coordinate": list(coordinate),
        "nearest_primary_coordinate": list(
            spec["nearest_primary_coordinate"]
        ),
        "distance_from_primary": spec["distance_from_primary"],
        "ordering_rule": (
            "ascending Euclidean distance from the nearest primary "
            "coordinate, then ascending numeric coordinate tuple; every "
            "coordinate is ranked independently"
        ),
        "axis_semantics": {
            "center_comp_num_ids": list(request.center_comp_num_ids),
            "component_order_rule": (
                "requested center components first, remaining global "
                "component IDs sorted, final component is closure"
            ),
        },
        "per_coordinate_limit": per_coordinate_limit,
        "parent_source_occurrences": len(eligible_systems),
        "eligible_systems": len(all_rows),
        "returned_systems": len(returned),
        "rankings": returned,
    }


def _secondary_grid_rankings(
    complete_systems: dict[
        tuple[Any, ...],
        dict[tuple[Any, ...], InterpolatedCriterion],
    ],
    requested_keys: list[tuple[Any, ...]],
    request: NormalizedRequest,
) -> list[dict[str, Any]]:
    per_coordinate_limit = max(
        1, math.ceil(request.limit / SECONDARY_RANKING_LIMIT_DIVISOR)
    )
    return [
        _secondary_panel(
            spec=spec,
            complete_systems=complete_systems,
            requested_keys=requested_keys,
            request=request,
            per_coordinate_limit=per_coordinate_limit,
        )
        for spec in _secondary_coordinate_specs(
            complete_systems, requested_keys
        )
    ]

def rank_criteria(
    criteria: list[InterpolatedCriterion],
    request: NormalizedRequest,
) -> RankingResult:
    diagnostics: list[Diagnostic] = []
    by_system: dict[
        tuple[Any, ...], dict[tuple[Any, ...], InterpolatedCriterion]
    ] = {}
    for criterion in criteria:
        key = _system_key(criterion)
        criterion_key = _criterion_key(criterion)
        existing = by_system.setdefault(key, {}).get(criterion_key)
        if existing is not None:
            raise ValueError(
                "whole-curve selection produced two selected blocks for one "
                "system/criterion: "
                f"{existing.source.source_key}, {criterion.source.source_key}"
            )
        by_system[key][criterion_key] = criterion

    requested_keys = [
        (
            target.input_value,
            target.quantity_key,
            target.basis,
            target.direction,
            target.aggregate,
            target.ranking_composition,
        )
        for target in request.targets
    ]
    complete_systems: dict[
        tuple[Any, ...], dict[tuple[Any, ...], InterpolatedCriterion]
    ] = {}
    incomplete = 0
    for system_key, system_criteria in by_system.items():
        if all(key in system_criteria for key in requested_keys):
            complete_systems[system_key] = system_criteria
        else:
            incomplete += 1
            diagnostics.append(
                Diagnostic(
                    code="INCOMPLETE_TARGET_SET",
                    message=(
                        "System lacks one or more requested ranking targets "
                        "after exact filtering and interpolation."
                    ),
                    stage="ranking",
                    source_key="::".join(system_key[0]),
                )
            )

    # Curves retained solely for regulated-grid context must never enter or
    # perturb the authoritative primary comparison class.
    primary_complete_systems: dict[
        tuple[Any, ...], dict[tuple[Any, ...], InterpolatedCriterion]
    ] = {}
    for system_key, system_criteria in complete_systems.items():
        if _has_primary_coverage(system_criteria, requested_keys):
            primary_complete_systems[system_key] = system_criteria
        else:
            incomplete += 1

    # Comparable classes keep different cardinalities, phases, and constraint
    # signatures out of one normalization range.
    classes: dict[
        tuple[Any, ...],
        list[
            tuple[
                tuple[Any, ...],
                dict[tuple[Any, ...], InterpolatedCriterion],
            ]
        ],
    ] = {}
    for system_key, system_criteria in primary_complete_systems.items():
        class_key = (
            len(system_key[0]),
            system_key[1],
            system_key[2],
            system_key[3],
            system_key[4],
        )
        classes.setdefault(class_key, []).append(
            (system_key, system_criteria)
        )

    all_rows: list[dict[str, Any]] = []
    for class_key, systems in sorted(
        classes.items(), key=lambda item: repr(item[0])
    ):
        common_by_target: dict[
            tuple[Any, ...], set[tuple[float, ...]]
        ] = {}
        class_usable = True
        for target_key in requested_keys:
            common = _common_ranking_coordinates(
                [system_criteria[target_key] for _key, system_criteria in systems]
            )
            if not common:
                diagnostics.append(
                    Diagnostic(
                        code="NO_COMMON_GRID",
                        message=(
                            "Comparable systems have no shared composition "
                            "grid inside every reported source hull."
                        ),
                        stage="ranking",
                        source_key=repr(class_key),
                        details={"target": target_key[0]},
                    )
                )
                class_usable = False
            common_by_target[target_key] = common
        if not class_usable:
            incomplete += len(systems)
            continue

        class_rows: list[dict[str, Any]] = []
        for system_key, system_criteria in systems:
            criterion_values: dict[tuple[Any, ...], float] = {}
            criterion_payloads: dict[tuple[Any, ...], dict[str, Any]] = {}
            primary_active_composition: list[dict[str, Any]] | None = None
            primary_active_signature: tuple[tuple[str, float], ...] | None = None
            primary_is_single_coordinate = True
            valid = True
            for target_key in requested_keys:
                criterion = system_criteria[target_key]
                basis = criterion.source.target.basis
                common = common_by_target[target_key]
                points = [
                    point.as_dict()
                    for point in criterion.grid_points
                    if tuple(point.coordinates) in common
                ]
                values: list[float] = []
                coordinates: list[tuple[float, ...]] = []
                for point in points:
                    value = _value_for_basis(point, basis)
                    if value is not None:
                        values.append(value)
                        coordinates.append(tuple(point["composition"]))
                raw = _aggregate(
                    values,
                    coordinates,
                    criterion.source.target.aggregate,
                )
                if raw is None:
                    valid = False
                    diagnostics.append(
                        Diagnostic(
                            code="RANKING_BASIS_UNAVAILABLE",
                            message=(
                                f"{basis} values are unavailable or cannot "
                                "support the requested aggregate."
                            ),
                            stage="ranking",
                            source_key=criterion.source.source_key,
                        )
                    )
                    break
                criterion_values[target_key] = raw
                if len(coordinates) == 1:
                    full_composition, _closure_id, _closure_name = (
                        _full_composition(criterion, coordinates[0])
                    )
                    criterion_active, criterion_signature = (
                        _active_composition(full_composition)
                    )
                    if primary_active_signature is None:
                        primary_active_composition = criterion_active
                        primary_active_signature = criterion_signature
                    elif criterion_signature != primary_active_signature:
                        primary_is_single_coordinate = False
                else:
                    primary_is_single_coordinate = False
                criterion_payloads[target_key] = {
                    "target": criterion.source.target.as_dict(),
                    "source": criterion.source.source_identity(),
                    "evidence": criterion.source.evidence_identity(),
                    "source_key": criterion.source.source_key,
                    "quality_score": criterion.source.quality_score,
                    "ranking_mode": criterion.source.target.aggregate,
                    "at_mole_fraction": (
                        list(criterion.source.target.ranking_composition)
                        if criterion.source.target.ranking_composition
                        is not None
                        else None
                    ),
                    "raw_value": raw,
                    "grid_values": points,
                    "ranking_grid_coverage": (
                        _ranking_grid_coverage(criterion, common)
                    ),
                    "secondary_composition_grid": (
                        _secondary_composition_grid(criterion)
                    ),
                    "baseline_reference_ensembles": (
                        criterion.baseline_reference_ensembles
                    ),
                    "baseline_message": criterion.baseline_message,
                    "derivation": criterion.source.derivation,
                }
            if not valid:
                incomplete += 1
                continue
            representative = next(iter(system_criteria.values())).source
            use_active_identity = (
                primary_is_single_coordinate
                and primary_active_composition is not None
                and primary_active_signature is not None
            )
            active_comp_num_ids = (
                [
                    str(component["comp_num_id"])
                    for component in primary_active_composition
                ]
                if use_active_identity
                else list(representative.comp_num_ids)
            )
            names_by_id = dict(
                zip(representative.comp_num_ids, representative.compound_names)
            )
            class_rows.append(
                {
                    "system_key": system_key,
                    "candidate_key": "::".join(active_comp_num_ids),
                    "system_signature": (
                        repr(primary_active_signature)
                        if use_active_identity
                        else "::".join(sorted(system_key[0]))
                    ),
                    "system_type": (
                        _system_type_for_cardinality(len(active_comp_num_ids))
                        if use_active_identity
                        else representative.system_type
                    ),
                    "comp_num_ids": active_comp_num_ids,
                    "compound_names": [
                        names_by_id[comp_num_id]
                        for comp_num_id in active_comp_num_ids
                    ],
                    "active_composition": (
                        primary_active_composition
                        if use_active_identity
                        else None
                    ),
                    "active_composition_signature": (
                        primary_active_signature
                        if use_active_identity
                        else tuple(
                            (comp_num_id, 1.0)
                            for comp_num_id in active_comp_num_ids
                        )
                    ),
                    "parent_candidate_key": "::".join(system_key[0]),
                    "parent_comp_num_ids": list(representative.comp_num_ids),
                    "pre_dedup_quality_score": float(
                        np.mean(
                            [
                                payload["quality_score"]
                                for payload in criterion_payloads.values()
                            ]
                        )
                    ),
                    "direct_evidence_fraction": float(
                        np.mean(
                            [
                                payload["evidence"]["evidence_relation"]
                                == "reported_direct"
                                for payload in criterion_payloads.values()
                            ]
                        )
                    ),
                    "phase_num_id": representative.phase_num_id,
                    "phase_id": representative.phase_id,
                    "ranking_group": {
                        **_ranking_group_payload(system_key),
                        "effective_cardinality": len(active_comp_num_ids),
                        "system_type": (
                            _system_type_for_cardinality(
                                len(active_comp_num_ids)
                            )
                            if use_active_identity
                            else representative.system_type
                        ),
                    },
                    "criterion_values": criterion_values,
                    "criterion_scores": {},
                    "criterion_payloads": criterion_payloads,
                }
            )
        if class_rows and all(
            row["active_composition"] is not None for row in class_rows
        ):
            class_rows = _deduplicate_active_rows(class_rows)
        for target_key in requested_keys:
            if class_rows:
                direction = class_rows[0]["criterion_payloads"][target_key][
                    "target"
                ]["direction"]
                _normalize_scores(class_rows, target_key, direction)
        for row in class_rows:
            row["overall_score"] = round(
                float(np.mean(list(row["criterion_scores"].values()))),
                12,
            )
            row["quality_score"] = round(
                float(
                    np.mean(
                        [
                            payload["quality_score"]
                            for payload in row["criterion_payloads"].values()
                        ]
                    )
                ),
                12,
            )
            row["criteria"] = [
                {
                    **row["criterion_payloads"][target_key],
                    "score": row["criterion_scores"][target_key],
                }
                for target_key in requested_keys
            ]
            row["n_selected_property_curves"] = len(
                {
                    payload["source"].get("selected_curve_id")
                    for payload in row["criterion_payloads"].values()
                }
            )
            del row["criterion_values"]
            del row["criterion_scores"]
            del row["criterion_payloads"]
            del row["pre_dedup_quality_score"]
            del row["direct_evidence_fraction"]
        class_rows.sort(
            key=lambda row: (
                -row["overall_score"],
                -row["quality_score"],
                row["system_signature"],
            )
        )
        for rank, row in enumerate(class_rows, start=1):
            row["rank_within_group"] = rank
        all_rows.extend(class_rows)

    all_rows.sort(
        key=lambda row: (
            -row["overall_score"],
            -row["quality_score"],
            repr(row["ranking_group"]),
            row["system_signature"],
        )
    )
    returned = all_rows[: request.limit]
    for overall_rank, row in enumerate(returned, start=1):
        row["rank"] = overall_rank
    secondary_grid_rankings = _secondary_grid_rankings(
        complete_systems, requested_keys, request
    )
    return RankingResult(
        rankings=returned,
        secondary_grid_rankings=secondary_grid_rankings,
        diagnostics=diagnostics,
        n_eligible_candidates=len(all_rows),
        n_incomplete_candidates=incomplete,
        n_secondary_candidate_occurrences=sum(
            int(panel["eligible_systems"])
            for panel in secondary_grid_rankings
        ),
        n_secondary_returned_occurrences=sum(
            int(panel["returned_systems"])
            for panel in secondary_grid_rankings
        ),
    )
