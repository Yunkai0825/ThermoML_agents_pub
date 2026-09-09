"""Interpolate each materialized evidence source independently."""

from __future__ import annotations

import itertools
from typing import Iterable

import numpy as np
from scipy.spatial import Delaunay, QhullError

from ..tool_settings import (
    BINARY_AUTO_RANKING_GRID_POINTS,
    COMPOSITION_COORDINATE_ATOL,
    HIGHER_AUTO_RANKING_GRID_DENOMINATOR,
    REGULATED_COMPOSITION_AXIS,
    TERNARY_AUTO_RANKING_GRID_DENOMINATOR,
)

from ..interface import (
    Diagnostic,
    GridPoint,
    InterpolatedCriterion,
    NormalizedRequest,
    SourceSeries,
)


_InterpolationOutcome = tuple[GridPoint | None, str | None]


def _simplex_grid(dimensions: int, denominator: int) -> list[tuple[float, ...]]:
    points: list[tuple[float, ...]] = []
    for counts in itertools.product(
        range(denominator + 1), repeat=dimensions
    ):
        if sum(counts) <= denominator:
            points.append(
                tuple(count / denominator for count in counts)
            )
    return sorted(points)


def ranking_grid_for_source(
    source: SourceSeries, request: NormalizedRequest
) -> list[tuple[float, ...]]:
    dimensions = source.coordinates.shape[1]
    if source.target.ranking_composition is not None:
        points = [source.target.ranking_composition]
    elif request.comparison_grid is not None:
        points = list(request.comparison_grid)
    elif dimensions == 0:
        points = [()]
    elif dimensions == 1:
        points = [
            (float(value),) for value in np.linspace(0.0, 1.0, BINARY_AUTO_RANKING_GRID_POINTS)
        ]
    elif dimensions == 2:
        points = _simplex_grid(2, TERNARY_AUTO_RANKING_GRID_DENOMINATOR)
    else:
        # Higher-dimensional simplexes grow combinatorially; a 0.25 ranking
        # grid is a deterministic compromise. The secondary chemistry profile
        # below is independent of this ranking-grid choice.
        points = _simplex_grid(dimensions, HIGHER_AUTO_RANKING_GRID_DENOMINATOR)
    if any(len(point) != dimensions for point in points):
        raise ValueError(
            f"comparison grid dimension does not match {source.system_type} "
            f"source {source.source_key}"
        )
    return points


def regulated_profile_grid(
    dimensions: int,
) -> list[tuple[float, ...]]:
    if dimensions <= 0:
        return []
    return sorted(
        tuple(float(value) for value in point)
        for point in itertools.product(
            REGULATED_COMPOSITION_AXIS, repeat=dimensions
        )
        if sum(point) <= 1.0 + COMPOSITION_COORDINATE_ATOL
    )


def _point_ids_union(
    source: SourceSeries, indexes: Iterable[int]
) -> tuple[str, ...]:
    return tuple(
        sorted(
            {
                _qualified_point_id(source, point_id)
                for index in indexes
                for point_id in source.point_ids[index]
            }
        )
    )


def _qualified_point_id(source: SourceSeries, point_id: str) -> str:
    """Return the safe literature/block-scoped identity of a BLKpoint."""
    if "::" in point_id:
        return point_id
    scope = source.BLKsubsys_id or source.search_scope
    return (
        f"{source.lit_num_id}::{source.block_number}::{scope}::{point_id}"
    )


def _point_ids_for_index(
    source: SourceSeries, index: int
) -> tuple[str, ...]:
    return tuple(
        _qualified_point_id(source, point_id)
        for point_id in source.point_ids[index]
    )


def _coordinate_score(
    source: SourceSeries,
    attribute: str,
    index: int,
) -> float:
    scores = getattr(source, attribute)
    return float(scores[index])


def _combined_coordinate_score(
    source: SourceSeries,
    attribute: str,
    indexes: tuple[int, ...],
    weights: np.ndarray,
) -> float:
    values = np.asarray(
        [_coordinate_score(source, attribute, index) for index in indexes],
        dtype=float,
    )
    return float(np.dot(weights, values))


def _interpolate_unary(
    source: SourceSeries, point: tuple[float, ...]
) -> _InterpolationOutcome:
    if point != () or len(source.values) != 1:
        return None, "unary_source_not_single_valued"
    return (
        GridPoint(
            coordinates=(),
            real_value=float(source.values[0]),
            source_point_ids=_point_ids_for_index(source, 0),
            interpolation_kind=(
                "reported_value"
                if len(source.point_ids[0]) == 1
                else "within_source_replicate_mean"
            ),
            constraint_proximity_score=_coordinate_score(
                source, "coordinate_constraint_proximity", 0
            ),
            composition_reliability_score=_coordinate_score(
                source, "coordinate_composition_reliability", 0
            ),
        ),
        None,
    )


def _interpolate_1d(
    source: SourceSeries, point: tuple[float, ...]
) -> _InterpolationOutcome:
    x = source.coordinates[:, 0]
    value = point[0]
    exact = np.where(
        np.isclose(x, value, atol=COMPOSITION_COORDINATE_ATOL, rtol=0.0)
    )[0]
    if len(exact):
        index = int(exact[0])
        return (
            GridPoint(
                coordinates=point,
                real_value=float(source.values[index]),
                source_point_ids=_point_ids_for_index(source, index),
                interpolation_kind=(
                    "reported_value"
                    if len(source.point_ids[index]) == 1
                    else "within_source_replicate_mean"
                ),
                constraint_proximity_score=_coordinate_score(
                    source, "coordinate_constraint_proximity", index
                ),
                composition_reliability_score=_coordinate_score(
                    source, "coordinate_composition_reliability", index
                ),
            ),
            None,
        )
    if len(x) < 2:
        return None, "insufficient_neighbor_points"

    order = np.argsort(x)
    sorted_x = x[order]
    if (
        value < sorted_x[0] - COMPOSITION_COORDINATE_ATOL
        or value > sorted_x[-1] + COMPOSITION_COORDINATE_ATOL
    ):
        return None, "outside_reported_composition_hull"
    upper_position = int(np.searchsorted(sorted_x, value, side="right"))
    lower_position = upper_position - 1
    if lower_position < 0 or upper_position >= len(sorted_x):
        return None, "no_adjacent_bracketing_points"
    lower = int(order[lower_position])
    upper = int(order[upper_position])
    span = x[upper] - x[lower]
    if span <= 0:
        return None, "degenerate_neighbor_interval"
    fraction = (value - x[lower]) / span
    interpolation_weights = np.asarray(
        [1.0 - fraction, fraction], dtype=float
    )
    y = (
        (1.0 - fraction) * source.values[lower]
        + fraction * source.values[upper]
    )
    return (
        GridPoint(
            coordinates=point,
            real_value=float(y),
            source_point_ids=_point_ids_union(source, (lower, upper)),
            interpolation_kind="piecewise_linear_inside_source_hull",
            constraint_proximity_score=_combined_coordinate_score(
                source,
                "coordinate_constraint_proximity",
                (lower, upper),
                interpolation_weights,
            ),
            composition_reliability_score=_combined_coordinate_score(
                source,
                "coordinate_composition_reliability",
                (lower, upper),
                interpolation_weights,
            ),
        ),
        None,
    )


def _triangulation(source: SourceSeries) -> Delaunay | None:
    dimensions = source.coordinates.shape[1]
    if len(source.coordinates) < dimensions + 1:
        return None
    try:
        return Delaunay(source.coordinates)
    except QhullError:
        return None


def _interpolate_nd(
    source: SourceSeries,
    point: tuple[float, ...],
    triangulation: Delaunay | None,
) -> _InterpolationOutcome:
    coordinate = np.asarray(point, dtype=float)
    distances = np.max(
        np.abs(source.coordinates - coordinate[np.newaxis, :]), axis=1
    )
    exact = np.where(distances <= COMPOSITION_COORDINATE_ATOL)[0]
    if len(exact):
        index = int(exact[0])
        return (
            GridPoint(
                coordinates=point,
                real_value=float(source.values[index]),
                source_point_ids=_point_ids_for_index(source, index),
                interpolation_kind=(
                    "reported_value"
                    if len(source.point_ids[index]) == 1
                    else "within_source_replicate_mean"
                ),
                constraint_proximity_score=_coordinate_score(
                    source, "coordinate_constraint_proximity", index
                ),
                composition_reliability_score=_coordinate_score(
                    source, "coordinate_composition_reliability", index
                ),
            ),
            None,
        )
    if triangulation is None:
        return None, "insufficient_or_degenerate_local_simplex"
    simplex = int(
        triangulation.find_simplex(coordinate, tol=COMPOSITION_COORDINATE_ATOL)
    )
    if simplex < 0:
        return None, "outside_reported_composition_hull"
    transform = triangulation.transform[simplex]
    barycentric = np.dot(
        transform[: source.coordinates.shape[1]],
        coordinate - transform[source.coordinates.shape[1]],
    )
    weights = np.append(barycentric, 1.0 - barycentric.sum())
    if np.any(weights < -COMPOSITION_COORDINATE_ATOL):
        return None, "invalid_local_simplex_weights"
    vertices = triangulation.simplices[simplex]
    y = float(np.dot(weights, source.values[vertices]))
    return (
        GridPoint(
            coordinates=point,
            real_value=y,
            source_point_ids=_point_ids_union(
                source, (int(index) for index in vertices)
            ),
            interpolation_kind="simplex_linear_inside_source_hull",
            constraint_proximity_score=_combined_coordinate_score(
                source,
                "coordinate_constraint_proximity",
                tuple(int(index) for index in vertices),
                weights,
            ),
            composition_reliability_score=_combined_coordinate_score(
                source,
                "coordinate_composition_reliability",
                tuple(int(index) for index in vertices),
                weights,
            ),
        ),
        None,
    )


def _interpolate_coordinate(
    source: SourceSeries,
    coordinate: tuple[float, ...],
    triangulation: Delaunay | None,
) -> _InterpolationOutcome:
    dimensions = source.coordinates.shape[1]
    if dimensions == 0:
        return _interpolate_unary(source, coordinate)
    if dimensions == 1:
        return _interpolate_1d(source, coordinate)
    return _interpolate_nd(source, coordinate, triangulation)


def source_grid_coverage(
    source: SourceSeries,
    request: NormalizedRequest,
) -> dict[str, object]:
    """Measure strict source-local coverage of the primary ranking grid.

    This is evaluated before property-curve selection. It never combines
    sources and therefore cannot create a synthetic cross-block hull.
    """
    return source_coordinate_coverage(
        source, ranking_grid_for_source(source, request)
    )


def source_coordinate_coverage(
    source: SourceSeries,
    coordinates: Iterable[tuple[float, ...]],
) -> dict[str, object]:
    """Measure strict source-local coverage of explicit coordinates."""
    ranking_grid = list(coordinates)
    dimensions = source.coordinates.shape[1]
    triangulation = _triangulation(source) if dimensions >= 2 else None
    covered: list[tuple[float, ...]] = []
    failures: list[dict[str, object]] = []
    for coordinate in ranking_grid:
        point, failure = _interpolate_coordinate(
            source, coordinate, triangulation
        )
        if point is not None:
            covered.append(coordinate)
        else:
            failures.append(
                {
                    "composition": list(coordinate),
                    "reason": failure or "not_interpolable",
                }
            )
    requested = len(ranking_grid)
    return {
        "requested_coordinates": [list(value) for value in ranking_grid],
        "covered_coordinates": [list(value) for value in covered],
        "failures": failures,
        "n_requested": requested,
        "n_covered": len(covered),
        "coverage_fraction": (
            float(len(covered) / requested) if requested else 0.0
        ),
        "eligible": bool(covered),
    }


def interpolate_sources(
    sources: list[SourceSeries],
    request: NormalizedRequest,
) -> tuple[list[InterpolatedCriterion], list[Diagnostic]]:
    criteria: list[InterpolatedCriterion] = []
    diagnostics: list[Diagnostic] = []
    for source in sources:
        dimensions = source.coordinates.shape[1]
        ranking_grid = ranking_grid_for_source(source, request)
        secondary_grid = regulated_profile_grid(dimensions)
        grid = sorted(set(ranking_grid) | set(secondary_grid))
        triangulation = (
            _triangulation(source) if dimensions >= 2 else None
        )
        points: list[GridPoint] = []
        failures: dict[tuple[float, ...], str] = {}
        for coordinate in grid:
            result, failure = _interpolate_coordinate(
                source, coordinate, triangulation
            )
            if result is not None:
                points.append(result)
            elif failure is not None:
                failures[coordinate] = failure
        available_coordinates = {
            tuple(point.coordinates) for point in points
        }
        primary_available = available_coordinates.intersection(ranking_grid)
        secondary_available = available_coordinates.intersection(
            secondary_grid
        )
        if not primary_available:
            diagnostics.append(
                Diagnostic(
                    code="NO_PRIMARY_GRID_COVERAGE",
                    message=(
                        "The source does not cover any primary ranking-grid "
                        "point. It is retained only when a regulated secondary "
                        "coordinate is available; strict first-order "
                        "interpolation remains inside the reported hull."
                    ),
                    stage="interpolation",
                    severity="warning",
                    source_key=source.source_key,
                    details={
                        "ranking_grid": [list(point) for point in ranking_grid],
                        "coverage_failures": [
                            {
                                "composition": list(point),
                                "reason": failures.get(
                                    point, "not_interpolable"
                                ),
                            }
                            for point in ranking_grid
                            if point not in available_coordinates
                        ],
                    },
                )
            )
        if not primary_available and not secondary_available:
            diagnostics.append(
                Diagnostic(
                    code="NO_GRID_COVERAGE",
                    message=(
                        "The source covers neither the primary ranking grid "
                        "nor any regulated secondary coordinate."
                    ),
                    stage="interpolation",
                    source_key=source.source_key,
                )
            )
            continue
        criteria.append(
            InterpolatedCriterion(
                source=source,
                grid_points=points,
                ranking_coordinates=tuple(ranking_grid),
                secondary_composition_coordinates=tuple(secondary_grid),
                grid_failures=failures,
            )
        )
    return criteria, diagnostics
