"""Immutable internal data contracts.

The public tool input is intentionally flat for reliable agent use.  These
dataclasses begin only after strict parsing and ID resolution, so numerical
stages never need to interpret free text or guess chemical identities.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

import numpy as np


class BaselineKind(str, Enum):
    """Chemically distinct reference meanings.

    ``THERMODYNAMIC_IDEAL`` and ``EMPIRICAL_BOUNDARY`` must never be merged:
    the latter is a comparison reference, not an ideal-mixture law.
    """

    NOT_REQUESTED = "not_requested"
    THERMODYNAMIC_IDEAL = "thermodynamic_ideal"
    EMPIRICAL_BOUNDARY = "empirical_boundary_reference"
    REPORTED_EXCESS_ZERO = "reported_excess_zero_reference"
    UNSUPPORTED = "unsupported"


@dataclass(frozen=True)
class Diagnostic:
    code: str
    message: str
    stage: str
    severity: str = "notice"
    source_key: str | None = None
    details: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        row: dict[str, Any] = {
            "code": self.code,
            "message": self.message,
            "stage": self.stage,
            "severity": self.severity,
        }
        if self.source_key is not None:
            row["source_key"] = self.source_key
        if self.details:
            row["details"] = self.details
        return row


@dataclass(frozen=True)
class RankingTarget:
    input_value: str
    quantity_key: str
    preferred_name: str
    canonical_unit: str
    prop_num_id: str | None
    var_num_id: str | None
    constr_num_id: str | None
    source_role: str
    source_global_id: str
    basis: str
    direction: str
    ranking_composition: tuple[float, ...] | None
    aggregate: str
    component_comp_num_id: str | None = None
    phase_num_id_filter: str | None = None
    component: dict[str, str] | None = None
    phase_filter: dict[str, str] | None = None
    component_linked: bool = False

    @property
    def evidence_global_ids(self) -> tuple[str, ...]:
        """Registry IDs accepted as direct or deterministic bridge evidence."""
        from ..tool_settings import VOLUMETRIC_EVIDENCE_GLOBAL_IDS

        return VOLUMETRIC_EVIDENCE_GLOBAL_IDS.get(
            self.source_global_id, (self.source_global_id,)
        )

    @property
    def pipeline_roles(self) -> tuple[str, ...]:
        roles = ["ranking_response"]
        if len(self.evidence_global_ids) > 1:
            roles.append("composition_support_field")
        return tuple(roles)

    @property
    def available_global_ids(self) -> tuple[str, ...]:
        return tuple(
            value
            for value in (
                self.prop_num_id,
                self.var_num_id,
                self.constr_num_id,
            )
            if value is not None
        )

    def as_dict(self) -> dict[str, Any]:
        return {
            "input": self.input_value,
            "quantity_key": self.quantity_key,
            "preferred_name": self.preferred_name,
            "canonical_unit": self.canonical_unit,
            "source_role": self.source_role,
            "source_global_id": self.source_global_id,
            "available_global_ids": list(self.available_global_ids),
            "basis": self.basis,
            "direction": self.direction,
            "at_mole_fraction": (
                list(self.ranking_composition)
                if self.ranking_composition is not None
                else None
            ),
            "aggregate": self.aggregate,
            "component_comp_num_id": self.component_comp_num_id,
            "phase_num_id_filter": self.phase_num_id_filter,
            "component": self.component,
            "phase_filter": self.phase_filter,
            "component_linked": self.component_linked,
            "pipeline_roles": list(self.pipeline_roles),
            "evidence_global_ids": list(self.evidence_global_ids),
        }


@dataclass(frozen=True)
class ConstraintSpec:
    input_value: str
    quantity_key: str
    preferred_name: str
    canonical_unit: str
    available_global_ids: tuple[str, ...]
    minimum: float
    maximum: float
    effective_minimum: float
    effective_maximum: float
    tolerance_kind: str
    tolerance_value: float
    tolerance_source: str
    unit_conversion_trace: tuple[dict[str, Any], ...]
    accepted_input_units: tuple[str, ...]
    component_comp_num_id: str | None = None
    phase_num_id_filter: str | None = None
    component: dict[str, str] | None = None
    phase_filter: dict[str, str] | None = None
    component_linked: bool = False

    def accepts(self, value: float) -> bool:
        return self.effective_minimum <= value <= self.effective_maximum

    def as_dict(self) -> dict[str, Any]:
        return {
            "input": self.input_value,
            "quantity_key": self.quantity_key,
            "preferred_name": self.preferred_name,
            "canonical_unit": self.canonical_unit,
            "available_global_ids": list(self.available_global_ids),
            "minimum": self.minimum,
            "maximum": self.maximum,
            "effective_minimum": self.effective_minimum,
            "effective_maximum": self.effective_maximum,
            "tolerance": {
                "kind": self.tolerance_kind,
                "value": self.tolerance_value,
                "source": self.tolerance_source,
            },
            "unit_conversion": {
                "accepted_input_units": list(self.accepted_input_units),
                "trace": list(self.unit_conversion_trace),
            },
            "component_comp_num_id": self.component_comp_num_id,
            "phase_num_id_filter": self.phase_num_id_filter,
            "component": self.component,
            "phase_filter": self.phase_filter,
            "component_linked": self.component_linked,
        }

@dataclass(frozen=True)
class NormalizedRequest:
    targets: tuple[RankingTarget, ...]
    constraints: tuple[ConstraintSpec, ...]
    center_comp_num_ids: tuple[str, ...]
    center_compounds: tuple[dict[str, str], ...]
    purpose: str
    tasks: tuple[str, ...]
    system_type: str | None
    system_scope: str
    comparison_grid: tuple[tuple[float, ...], ...] | None
    limit: int

    def as_dict(self) -> dict[str, Any]:
        return {
            "ranking_targets": [target.as_dict() for target in self.targets],
            "target_constraints": [
                constraint.as_dict() for constraint in self.constraints
            ],
            "center_comp_num_ids": list(self.center_comp_num_ids),
            "center_compounds": list(self.center_compounds),
            "purpose": self.purpose,
            "tasks": list(self.tasks),
            "system_type": self.system_type,
            "system_scope": self.system_scope,
            "comparison_grid": (
                [list(point) for point in self.comparison_grid]
                if self.comparison_grid is not None
                else "auto"
            ),
            "limit": self.limit,
        }


@dataclass(frozen=True)
class CandidateRef:
    doi: str
    lit_num_id: str
    block_number: str
    BLKsubsys_id: str | None
    search_scope: str
    block_type: str
    declared_system_type: str
    effective_system_type: str
    comp_num_ids: tuple[str, ...]
    n_datapoints: int
    declared_quantity_ids: tuple[str, ...] = ()

    @property
    def key(self) -> str:
        parts = [self.lit_num_id, self.block_number]
        if self.BLKsubsys_id is not None:
            parts.append(self.BLKsubsys_id)
        return "::".join(parts)

    def as_dict(self) -> dict[str, Any]:
        return {
            "doi": self.doi,
            "lit_num_id": self.lit_num_id,
            "block_number": self.block_number,
            "BLKsubsys_id": self.BLKsubsys_id,
            "search_scope": self.search_scope,
            "block_type": self.block_type,
            "declared_system_type": self.declared_system_type,
            "effective_system_type": self.effective_system_type,
            "comp_num_ids": list(self.comp_num_ids),
            "n_datapoints": self.n_datapoints,
            "declared_quantity_ids": list(self.declared_quantity_ids),
        }


@dataclass(frozen=True)
class DiscoveryResult:
    candidates: tuple[CandidateRef, ...]
    pages_read: int
    registry_rows_examined: int
    declared_count: int
    subsystem_count: int


@dataclass
class SourceSeries:
    """One normalized block-local experimental property curve."""

    source_key: str
    doi: str
    lit_num_id: str
    block_number: str
    BLKsubsys_id: str | None
    search_scope: str
    system_type: str
    comp_num_ids: tuple[str, ...]
    compound_names: tuple[str, ...]
    target: RankingTarget
    target_local_id: str
    phase_num_id: str | None
    phase_id: str | None
    presentation: str | None
    presentation_kind: str
    reported_unit: str
    response_semantics: str
    reference_semantics: dict[str, Any]
    coordinates: np.ndarray
    values: np.ndarray
    point_ids: tuple[tuple[str, ...], ...]
    original_coordinate_basis: tuple[str, ...]
    coordinate_comp_num_ids: tuple[str, ...]
    constraint_signature: tuple[tuple[Any, ...], ...]
    quality_score: float
    derivation: dict[str, Any]
    coordinate_constraint_proximity: np.ndarray
    coordinate_composition_reliability: np.ndarray
    observed_global_id: str | None = None
    observed_quantity_key: str | None = None
    observed_canonical_unit: str | None = None
    evidence_relation: str = "reported_direct"

    @property
    def effective_cardinality(self) -> int:
        return len(self.comp_num_ids)

    @property
    def group_key(self) -> tuple[Any, ...]:
        return (
            tuple(sorted(self.comp_num_ids)),
            self.effective_cardinality,
            self.target.quantity_key,
            self.phase_num_id,
            self.constraint_signature,
            self.response_semantics,
        )

    def evidence_identity(self) -> dict[str, Any]:
        return {
            "doi": self.doi,
            "lit_num_id": self.lit_num_id,
            "block_number": self.block_number,
            "BLKsubsys_id": self.BLKsubsys_id,
            "search_scope": self.search_scope,
            "target_local_id": self.target_local_id,
            "source_key": self.source_key,
            "observed_global_id": (
                self.observed_global_id or self.target.source_global_id
            ),
            "observed_quantity_key": (
                self.observed_quantity_key or self.target.quantity_key
            ),
            "evidence_relation": self.evidence_relation,
            "presentation": self.presentation,
            "presentation_kind": self.presentation_kind,
            "reported_unit": self.reported_unit,
            "response_semantics": self.response_semantics,
        }

    def source_identity(self) -> dict[str, Any]:
        identity = {
            "doi": self.doi,
            "lit_num_id": self.lit_num_id,
            "block_number": self.block_number,
            "BLKsubsys_id": self.BLKsubsys_id,
            "search_scope": self.search_scope,
            "target_local_id": self.target_local_id,
            "source_key": self.source_key,
        }
        selection = self.derivation.get("property_curve_selection")
        if isinstance(selection, dict):
            identity.update(
                {
                    "selection_group_id": selection.get(
                        "selection_group_id"
                    ),
                    "selected_curve_id": selection.get(
                        "selected_curve_id"
                    ),
                    "selection_score": selection.get(
                        "selection_score"
                    ),
                }
            )
        return identity


@dataclass(frozen=True)
class GridPoint:
    coordinates: tuple[float, ...]
    real_value: float
    source_point_ids: tuple[str, ...]
    interpolation_kind: str
    constraint_proximity_score: float = 1.0
    composition_reliability_score: float = 1.0
    ideal_value: float | None = None
    deviation: float | None = None
    baseline_kind: BaselineKind = BaselineKind.NOT_REQUESTED
    baseline_sources: tuple[dict[str, Any], ...] = ()

    def as_dict(self) -> dict[str, Any]:
        return {
            "composition": list(self.coordinates),
            "real_value": self.real_value,
            "ideal_value": self.ideal_value,
            "deviation": self.deviation,
            "absolute_deviation": (
                abs(self.deviation) if self.deviation is not None else None
            ),
            "source_point_ids": list(self.source_point_ids),
            "interpolation_kind": self.interpolation_kind,
            "constraint_proximity_score": (
                self.constraint_proximity_score
            ),
            "composition_reliability_score": (
                self.composition_reliability_score
            ),
            "baseline_kind": self.baseline_kind.value,
            "baseline_sources": list(self.baseline_sources),
        }


@dataclass
class InterpolatedCriterion:
    source: SourceSeries
    grid_points: list[GridPoint]
    ranking_coordinates: tuple[tuple[float, ...], ...]
    secondary_composition_coordinates: tuple[tuple[float, ...], ...]
    grid_failures: dict[tuple[float, ...], str]
    baseline_reference_ensembles: list[dict[str, Any]] = field(
        default_factory=list
    )
    baseline_message: str | None = None
    raw_ranking_value: float | None = None
    normalized_score: float | None = None
