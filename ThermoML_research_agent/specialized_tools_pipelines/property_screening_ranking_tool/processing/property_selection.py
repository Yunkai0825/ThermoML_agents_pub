"""Select one complete experimental property curve per comparable system."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, replace
from typing import Any

import numpy as np

from ..interface import Diagnostic, NormalizedRequest, SourceSeries
from ..tool_settings import PROPERTY_CURVE_SELECTION_SCORE_WEIGHTS
from .interpolation import (
    regulated_profile_grid,
    source_coordinate_coverage,
    source_grid_coverage,
)


@dataclass(frozen=True)
class PropertyCurveSelectionResult:
    """Selected source curves and an audit of every competing block."""

    sources: list[SourceSeries]
    report: list[dict[str, Any]]
    diagnostics: list[Diagnostic]
    n_input_sources: int
    n_candidate_curves: int
    n_selected_curves: int
    n_secondary_fallback_curves: int
    n_rejected_curves: int


def _stable_id(prefix: str, value: Any) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:20]
    return f"{prefix}_{digest}"


def _selection_group_key(source: SourceSeries) -> tuple[Any, ...]:
    """Identity that must share one selected absolute physical curve.

    Original ThermoML presentation and reference-state metadata are
    provenance, not distinct properties after successful materialization.
    """
    return (
        tuple(sorted(source.comp_num_ids)),
        source.system_type,
        source.target.source_global_id,
        source.target.component_comp_num_id,
        source.phase_num_id,
        source.constraint_signature,
        source.response_semantics,
    )


def _ranking_view_key(source: SourceSeries) -> tuple[Any, ...]:
    target = source.target
    return (
        target.basis,
        target.direction,
        target.ranking_composition,
        target.aggregate,
    )


def _candidate_key(source: SourceSeries) -> tuple[Any, ...]:
    """One reported property declaration/derived curve within one block."""
    return (
        source.source_key,
        source.doi,
        source.lit_num_id,
        source.block_number,
        source.BLKsubsys_id,
        source.search_scope,
        source.target_local_id,
        source.observed_global_id,
        source.evidence_relation,
        source.phase_num_id,
    )


def _source_components(source: SourceSeries) -> dict[str, float]:
    score = source.derivation.get("evidence_score", {})
    raw = score.get("components", {})
    missing = set(PROPERTY_CURVE_SELECTION_SCORE_WEIGHTS).difference(
        {*raw, "selection_grid_coverage"}
    )
    if missing:
        raise ValueError(
            f"{source.source_key} lacks curve-score components: "
            f"{sorted(missing)}"
        )
    return {
        name: float(np.clip(raw[name], 0.0, 1.0))
        for name in PROPERTY_CURVE_SELECTION_SCORE_WEIGHTS
        if name != "selection_grid_coverage"
    }


def _coordinate_tuple(value: list[Any]) -> tuple[float, ...]:
    return tuple(float(item) for item in value)


def _ordered_fallback_coordinates(
    primary: set[tuple[float, ...]],
    secondary: set[tuple[float, ...]],
) -> list[tuple[float, ...]]:
    def distance(coordinate: tuple[float, ...]) -> float:
        if not primary:
            return float(np.linalg.norm(np.asarray(coordinate, dtype=float)))
        return min(
            float(
                np.linalg.norm(
                    np.asarray(coordinate, dtype=float)
                    - np.asarray(reference, dtype=float)
                )
            )
            for reference in primary
        )

    return sorted(
        secondary.difference(primary),
        key=lambda coordinate: (
            round(distance(coordinate), 15),
            coordinate,
        ),
    )


def _candidate_record(
    candidate_sources: dict[tuple[Any, ...], SourceSeries],
    expected_views: tuple[tuple[Any, ...], ...],
    request: NormalizedRequest,
) -> dict[str, Any]:
    representative = next(iter(candidate_sources.values()))
    primary_coverage_by_view: list[dict[str, Any]] = []
    secondary_coverage_by_view: list[dict[str, Any]] = []
    missing_views: list[list[Any]] = []
    for view in expected_views:
        source = candidate_sources.get(view)
        if source is None:
            missing_views.append(list(view))
            continue
        primary_coverage_by_view.append(
            {
                "view": list(view),
                "target": source.target.as_dict(),
                "coverage": source_grid_coverage(source, request),
            }
        )
        secondary_coverage_by_view.append(
            {
                "view": list(view),
                "target": source.target.as_dict(),
                "coverage": source_coordinate_coverage(
                    source,
                    regulated_profile_grid(source.coordinates.shape[1]),
                ),
            }
        )
    primary_coverage = (
        min(
            float(item["coverage"]["coverage_fraction"])
            for item in primary_coverage_by_view
        )
        if primary_coverage_by_view
        else 0.0
    )
    secondary_coverage = (
        min(
            float(item["coverage"]["coverage_fraction"])
            for item in secondary_coverage_by_view
        )
        if secondary_coverage_by_view
        else 0.0
    )
    all_views_present = (
        not missing_views
        and len(primary_coverage_by_view) == len(expected_views)
    )
    primary_eligible = all_views_present and all(
        bool(item["coverage"]["eligible"])
        for item in primary_coverage_by_view
    )
    primary_coordinates = {
        _coordinate_tuple(value)
        for item in primary_coverage_by_view
        for value in item["coverage"]["requested_coordinates"]
    }
    covered_secondary_sets = [
        {
            _coordinate_tuple(value)
            for value in item["coverage"]["covered_coordinates"]
        }
        for item in secondary_coverage_by_view
    ]
    common_secondary_coordinates = (
        set.intersection(*covered_secondary_sets)
        if covered_secondary_sets
        else set()
    )
    ordered_fallback = _ordered_fallback_coordinates(
        primary_coordinates, common_secondary_coordinates
    )
    secondary_eligible = all_views_present and bool(ordered_fallback)
    secondary_fallback_coordinate = (
        ordered_fallback[0]
        if ordered_fallback and not primary_eligible
        else None
    )
    selection_grid_role = (
        "primary"
        if primary_eligible
        else "regulated_secondary"
        if secondary_eligible
        else None
    )
    selection_grid_coverage = (
        primary_coverage
        if primary_eligible
        else secondary_coverage
        if secondary_eligible
        else 0.0
    )
    components = _source_components(representative)
    components["selection_grid_coverage"] = selection_grid_coverage
    composite_score = float(
        np.clip(
            sum(
                PROPERTY_CURVE_SELECTION_SCORE_WEIGHTS[name] * value
                for name, value in components.items()
            ),
            0.0,
            1.0,
        )
    )
    candidate_identity = {
        **representative.evidence_identity(),
        "phase_num_id": representative.phase_num_id,
        "reference_semantics": representative.reference_semantics,
    }
    return {
        "candidate_id": _stable_id("property_curve_candidate", candidate_identity),
        "source": candidate_identity,
        "n_points": int(len(representative.values)),
        "score": composite_score,
        "score_components": components,
        "score_weights": dict(PROPERTY_CURVE_SELECTION_SCORE_WEIGHTS),
        "primary_grid_coverage_by_view": primary_coverage_by_view,
        "secondary_grid_coverage_by_view": secondary_coverage_by_view,
        "missing_ranking_views": missing_views,
        "primary_eligible": primary_eligible,
        "secondary_eligible": secondary_eligible,
        "selection_grid_role": selection_grid_role,
        "secondary_fallback_coordinate": (
            list(secondary_fallback_coordinate)
            if secondary_fallback_coordinate is not None
            else None
        ),
        "secondary_fallback_priority": (
            _ordered_fallback_coordinates(
                primary_coordinates,
                {
                    _coordinate_tuple(value)
                    for item in secondary_coverage_by_view
                    for value in item["coverage"]["requested_coordinates"]
                },
            ).index(secondary_fallback_coordinate)
            + 1
            if secondary_fallback_coordinate is not None
            else None
        ),
        "eligible": primary_eligible or secondary_eligible,
        "exclusion_reason": (
            None
            if primary_eligible or secondary_eligible
            else (
                "missing_ranking_view"
                if missing_views
                else "no_primary_or_regulated_secondary_grid_coverage"
            )
        ),
        "_sources": candidate_sources,
    }


def _reportable_candidate(record: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value for key, value in record.items() if key != "_sources"
    }


def select_property_curves(
    sources: list[SourceSeries],
    request: NormalizedRequest,
) -> PropertyCurveSelectionResult:
    """Choose one entire curve; never average independent blocks pointwise."""
    grouped: dict[tuple[Any, ...], list[SourceSeries]] = {}
    for source in sources:
        if source.response_semantics != "absolute_target":
            raise ValueError(
                "property selection received a non-absolute response: "
                f"{source.source_key} ({source.response_semantics})"
            )
        grouped.setdefault(_selection_group_key(source), []).append(source)

    selected_sources: list[SourceSeries] = []
    reports: list[dict[str, Any]] = []
    diagnostics: list[Diagnostic] = []
    n_candidates = 0
    n_selected = 0
    n_secondary_fallback = 0

    for group_key in sorted(grouped, key=str):
        group_sources = grouped[group_key]
        expected_views = tuple(
            sorted({_ranking_view_key(source) for source in group_sources}, key=str)
        )
        candidates: dict[
            tuple[Any, ...], dict[tuple[Any, ...], SourceSeries]
        ] = {}
        for source in group_sources:
            views = candidates.setdefault(_candidate_key(source), {})
            view = _ranking_view_key(source)
            incumbent = views.get(view)
            if incumbent is None or source.quality_score > incumbent.quality_score:
                views[view] = source

        candidate_records = [
            _candidate_record(candidate_sources, expected_views, request)
            for candidate_sources in candidates.values()
        ]
        n_candidates += len(candidate_records)
        eligible = [row for row in candidate_records if row["eligible"]]
        eligible.sort(
            key=lambda row: (
                not bool(row["primary_eligible"]),
                (
                    int(row["secondary_fallback_priority"])
                    if not row["primary_eligible"]
                    and row["secondary_fallback_priority"] is not None
                    else 0
                ),
                -float(row["score"]),
                -float(row["score_components"]["selection_grid_coverage"]),
                -float(
                    next(iter(row["_sources"].values())).quality_score
                ),
                -float(row["score_components"]["target_directness"]),
                str(row["candidate_id"]),
            )
        )
        group_id = _stable_id("property_curve_group", group_key)
        selected = eligible[0] if eligible else None
        if selected is None:
            diagnostics.append(
                Diagnostic(
                    code="NO_SELECTABLE_PROPERTY_CURVE",
                    message=(
                        "No single experimental block covers either a primary "
                        "ranking coordinate or a regulated secondary coordinate "
                        "for every requested view. Independent blocks were not "
                        "combined."
                    ),
                    stage="property_curve_selection",
                    details={
                        "selection_group_id": group_id,
                        "candidates": [
                            _reportable_candidate(row)
                            for row in candidate_records
                        ],
                    },
                )
            )
        else:
            n_selected += 1
            n_secondary_fallback += int(
                selected["selection_grid_role"] == "regulated_secondary"
            )
            selected_curve_id = _stable_id(
                "selected_property_curve",
                [group_id, selected["candidate_id"]],
            )
            for source in selected["_sources"].values():
                selection = {
                    "selection_group_id": group_id,
                    "selected_curve_id": selected_curve_id,
                    "candidate_id": selected["candidate_id"],
                    "selection_score": selected["score"],
                    "score_components": selected["score_components"],
                    "score_weights": selected["score_weights"],
                    "primary_grid_coverage_by_view": selected[
                        "primary_grid_coverage_by_view"
                    ],
                    "secondary_grid_coverage_by_view": selected[
                        "secondary_grid_coverage_by_view"
                    ],
                    "selection_grid_role": selected[
                        "selection_grid_role"
                    ],
                    "secondary_fallback_coordinate": selected[
                        "secondary_fallback_coordinate"
                    ],
                    "secondary_fallback_priority": selected[
                        "secondary_fallback_priority"
                    ],
                    "selection_rule": (
                        "primary-covering curve preferred, otherwise highest-"
                        "scoring regulated-secondary-covering curve; "
                        "no_cross_block_property_averaging"
                    ),
                }
                selected_sources.append(
                    replace(
                        source,
                        derivation={
                            **source.derivation,
                            "property_curve_selection": selection,
                        },
                    )
                )

        ordered_candidates = sorted(
            candidate_records,
            key=lambda row: (
                not bool(row["eligible"]),
                -float(row["score"]),
                str(row["candidate_id"]),
            ),
        )
        reports.append(
            {
                "selection_group_id": group_id,
                "system": {
                    "comp_num_ids": list(group_key[0]),
                    "system_type": group_key[1],
                    "target_global_id": group_key[2],
                    "target_component_comp_num_id": group_key[3],
                    "phase_num_id": group_key[4],
                    "constraint_signature": [
                        list(value) for value in group_key[5]
                    ],
                    "response_semantics": group_key[6],
                },
                "expected_ranking_views": [list(view) for view in expected_views],
                "selection_rule": (
                    "prefer_primary_then_select_one_whole_block_curve_by_"
                    "composite_score_for_regulated_secondary_context"
                ),
                "selected_grid_role": (
                    selected["selection_grid_role"] if selected else None
                ),
                "selected_candidate_id": (
                    selected["candidate_id"] if selected else None
                ),
                "selected_curve_id": (
                    _stable_id(
                        "selected_property_curve",
                        [group_id, selected["candidate_id"]],
                    )
                    if selected
                    else None
                ),
                "candidates": [
                    {
                        **_reportable_candidate(row),
                        "selected": (
                            selected is not None
                            and row["candidate_id"] == selected["candidate_id"]
                        ),
                    }
                    for row in ordered_candidates
                ],
            }
        )

    selected_sources.sort(
        key=lambda source: (
            tuple(sorted(source.comp_num_ids)),
            source.target.source_global_id,
            source.target.basis,
            source.source_key,
        )
    )
    return PropertyCurveSelectionResult(
        sources=selected_sources,
        report=reports,
        diagnostics=diagnostics,
        n_input_sources=len(sources),
        n_candidate_curves=n_candidates,
        n_selected_curves=n_selected,
        n_secondary_fallback_curves=n_secondary_fallback,
        n_rejected_curves=max(0, n_candidates - n_selected),
    )
