"""Convert one exact ThermoML block into source-local numerical series."""

from __future__ import annotations

import math
import re
from collections import defaultdict
from typing import Any, Callable

import numpy as np
from rdkit import Chem
from scipy.spatial import ConvexHull, QhullError

from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.mixture_nonideality_calc.composition_transforms import (
    detect_composition_basis,
)
from card_db_search_tools.basic_search_tools.advanced_block_search.catalogs import (
    load_runtime_catalogs,
)

from ..tool_settings import (
    COMPOSITION_CLOSURE_ATOL,
    COMPOSITION_SELF_CONSISTENCY_ATOL,
    CONSTRAINT_PROXIMITY_AT_SOFT_LIMIT,
    PROPERTY_SOURCE_SCORE_WEIGHTS,
    PROPERTY_SUPPORT_REFERENCE_POINTS,
    VOLUMETRIC_BRIDGE_SELF_CONSISTENCY_RTOL,
)

from ..interface import (
    ConstraintSpec,
    Diagnostic,
    NormalizedRequest,
    RankingTarget,
    SourceSeries,
)
from ..unit_conversion_lib.property_response import (
    PresentationKind,
    classify_presentation,
    presentation_requires_reference,
    reference_component_num_ids,
)
from ..sources.reader import AuthoritativeBlock
from .composition_alignment import (
    CompositionField,
    solve_composition_alignment,
)
from .relationships import (
    EVIDENCE_METADATA,
    select_unary_molar_volume_ensembles,
)


_FORMULA_TOKEN_RE = re.compile(r"([A-Z][a-z]?)(\d*)")
_COMPOSITION_TYPE = "eComponentComposition"


def _molar_mass(formula: str) -> float | None:
    """Molar mass from a simple Hill formula using RDKit's periodic table."""
    if not isinstance(formula, str) or not formula.strip():
        return None
    table = Chem.GetPeriodicTable()
    text = formula.strip()
    position = 0
    total = 0.0
    for match in _FORMULA_TOKEN_RE.finditer(text):
        if match.start() != position:
            return None
        symbol = match.group(1)
        try:
            atomic_number = table.GetAtomicNumber(symbol)
        except RuntimeError:
            return None
        if atomic_number <= 0:
            return None
        count = int(match.group(2) or "1")
        total += float(table.GetAtomicWeight(atomic_number)) * count
        position = match.end()
    if position != len(text) or total <= 0:
        return None
    return total


def _role_fields(role: str) -> tuple[str, str, str]:
    return {
        "property": ("properties", "prop_num_id", "BLKprop_id"),
        "variable": ("variables", "var_num_id", "BLKvar_id"),
        "constraint": ("constraints", "constr_num_id", "BLKconstr_id"),
    }[role]


def _phase(declaration: dict[str, Any]) -> tuple[str | None, str | None]:
    phase = (
        declaration.get("property_phase")
        or declaration.get("phase")
        or {}
    )
    if not isinstance(phase, dict):
        return None, None
    return phase.get("phase_num_id"), phase.get("phase_id")


def _reference_semantics(
    block: AuthoritativeBlock,
    declaration: dict[str, Any],
) -> dict[str, Any]:
    ref_phase = declaration.get("ref_phase")
    phase_payload = ref_phase if isinstance(ref_phase, dict) else {}
    reference_ids, resolution = reference_component_num_ids(
        block.projected, declaration
    )
    solvent_ids = tuple(
        sorted(
            {
                str(item["comp_num_id"])
                for item in block.projected.get("solvents", [])
                if isinstance(item, dict)
                and isinstance(item.get("comp_num_id"), str)
            }
        )
    )
    return {
        "ref_state_type": declaration.get("ref_state_type"),
        "ref_temperature_K": declaration.get("ref_temperature_K"),
        "ref_pressure_kPa": declaration.get("ref_pressure_kPa"),
        "property_temperature_K": declaration.get("temperature_K"),
        "property_pressure_kPa": declaration.get("pressure_kPa"),
        "ref_phase_num_id": phase_payload.get("phase_num_id"),
        "ref_phase_id": phase_payload.get("phase_id"),
        "ref_component_org_num": phase_payload.get("component_org_num"),
        "reference_comp_num_ids": reference_ids,
        "reference_component_resolution": resolution,
        "solvent_comp_num_ids": solvent_ids,
    }


def _matching_occurrences(
    block: AuthoritativeBlock,
    global_ids: tuple[str, ...],
    *,
    component_comp_num_id: str | None = None,
    phase_num_id: str | None = None,
) -> list[tuple[str, dict[str, Any]]]:
    matches: list[tuple[str, dict[str, Any]]] = []
    for role in ("variable", "constraint", "property"):
        section, global_field, local_field = _role_fields(role)
        for declaration in block.projected[section]:
            if (
                declaration.get(global_field) in global_ids
                and _declaration_matches_bindings(
                    block,
                    declaration,
                    component_comp_num_id=component_comp_num_id,
                    phase_num_id=phase_num_id,
                )
            ):
                matches.append((role, declaration))
    return matches


def _constraint_mask(
    block: AuthoritativeBlock,
    constraints: tuple[ConstraintSpec, ...],
) -> tuple[
    np.ndarray,
    list[Diagnostic],
    set[str],
    np.ndarray,
    dict[str, Any],
]:
    mask = np.ones(len(block.rows), dtype=bool)
    diagnostics: list[Diagnostic] = []
    controlled_local_ids: set[str] = set()
    constraint_scores: list[tuple[ConstraintSpec, np.ndarray]] = []
    for constraint in constraints:
        occurrences = _matching_occurrences(
            block,
            constraint.available_global_ids,
            component_comp_num_id=constraint.component_comp_num_id,
            phase_num_id=constraint.phase_num_id_filter,
        )
        if not occurrences:
            diagnostics.append(
                Diagnostic(
                    code="CONSTRAINT_OCCURRENCE_MISSING",
                    message=(
                        f"{constraint.preferred_name} is not reported as a "
                        "variable, constraint, or property in this block."
                    ),
                    stage="harmonization",
                    source_key=block.candidate.key,
                )
            )
            empty = np.zeros(len(block.rows), dtype=float)
            return (
                np.zeros(len(block.rows), dtype=bool),
                diagnostics,
                set(),
                empty,
                {"per_constraint": [], "mean_score": 0.0},
            )
        occurrence_masks: list[np.ndarray] = []
        occurrence_scores: list[np.ndarray] = []
        for role, declaration in occurrences:
            local_field = _role_fields(role)[2]
            local_id = declaration[local_field]
            controlled_local_ids.add(local_id)
            values = np.array(
                [
                    row.get(local_id)
                    if isinstance(row.get(local_id), (int, float))
                    else np.nan
                    for row in block.rows
                ],
                dtype=float,
            )
            occurrence_masks.append(
                np.isfinite(values)
                & (values >= constraint.effective_minimum)
                & (values <= constraint.effective_maximum)
            )
            occurrence_scores.append(
                _constraint_proximity_scores(values, constraint)
            )
        occurrence_mask = np.logical_or.reduce(occurrence_masks)
        best_scores = np.max(np.vstack(occurrence_scores), axis=0)
        best_scores = np.where(occurrence_mask, best_scores, 0.0)
        constraint_scores.append((constraint, best_scores))
        mask &= occurrence_mask
    if not np.any(mask):
        diagnostics.append(
            Diagnostic(
                code="NO_ROWS_AT_REQUESTED_STATE",
                message="No authoritative rows satisfy every target constraint.",
                stage="harmonization",
                source_key=block.candidate.key,
            )
        )
    if constraint_scores:
        score_matrix = np.vstack(
            [scores for _constraint, scores in constraint_scores]
        )
        proximity = np.prod(score_matrix, axis=0) ** (
            1.0 / len(constraint_scores)
        )
    else:
        proximity = np.ones(len(block.rows), dtype=float)
    proximity = np.where(mask, proximity, 0.0)
    per_constraint = []
    for constraint, scores in constraint_scores:
        accepted = scores[mask]
        per_constraint.append(
            {
                "quantity_key": constraint.quantity_key,
                "requested_range": [
                    constraint.minimum,
                    constraint.maximum,
                ],
                "effective_range": [
                    constraint.effective_minimum,
                    constraint.effective_maximum,
                ],
                "tolerance_kind": constraint.tolerance_kind,
                "mean_proximity": (
                    float(np.mean(accepted)) if len(accepted) else 0.0
                ),
                "minimum_proximity": (
                    float(np.min(accepted)) if len(accepted) else 0.0
                ),
                "exact_fraction": (
                    float(np.mean(np.isclose(accepted, 1.0)))
                    if len(accepted)
                    else 0.0
                ),
            }
        )
    return (
        mask,
        diagnostics,
        controlled_local_ids,
        proximity,
        {
            "combination": "geometric_mean_across_constraints",
            "soft_limit_score": CONSTRAINT_PROXIMITY_AT_SOFT_LIMIT,
            "mean_score": (
                float(np.mean(proximity[mask])) if np.any(mask) else 0.0
            ),
            "minimum_score": (
                float(np.min(proximity[mask])) if np.any(mask) else 0.0
            ),
            "per_constraint": per_constraint,
        },
    )


def _constraint_proximity_scores(
    values: np.ndarray,
    constraint: ConstraintSpec,
) -> np.ndarray:
    """Score exact-request rows as one and soft-window rows continuously."""
    scores = np.zeros(len(values), dtype=float)
    finite = np.isfinite(values)
    accepted = (
        finite
        & (values >= constraint.effective_minimum)
        & (values <= constraint.effective_maximum)
    )
    exact = (
        accepted
        & (values >= constraint.minimum)
        & (values <= constraint.maximum)
    )
    scores[exact] = 1.0
    for lower_side in (True, False):
        outside = accepted & (
            (values < constraint.minimum)
            if lower_side
            else (values > constraint.maximum)
        )
        if not np.any(outside):
            continue
        boundary = (
            constraint.minimum if lower_side else constraint.maximum
        )
        effective = (
            constraint.effective_minimum
            if lower_side
            else constraint.effective_maximum
        )
        if (
            constraint.tolerance_kind == "log10"
            and boundary > 0.0
            and effective > 0.0
        ):
            denominator = abs(math.log10(effective / boundary))
            distance = np.abs(np.log10(values[outside] / boundary))
        else:
            denominator = abs(effective - boundary)
            distance = np.abs(values[outside] - boundary)
        fraction = (
            np.clip(distance / denominator, 0.0, 1.0)
            if denominator > 0.0
            else np.ones(np.count_nonzero(outside), dtype=float)
        )
        scores[outside] = CONSTRAINT_PROXIMITY_AT_SOFT_LIMIT ** fraction
    return scores


def _is_composition(declaration: dict[str, Any], id_field: str) -> bool:
    if declaration.get("type") == _COMPOSITION_TYPE:
        return True
    return (
        detect_composition_basis(str(declaration.get(id_field) or ""))
        != "unknown"
    )


def _uncontrolled_state_diagnostic(
    block: AuthoritativeBlock,
    mask: np.ndarray,
    controlled_local_ids: set[str],
    target_local_ids: set[str],
) -> Diagnostic | None:
    for declaration in block.projected["variables"]:
        local_id = declaration["BLKvar_id"]
        if local_id in controlled_local_ids or local_id in target_local_ids:
            continue
        if _is_composition(declaration, "var_id"):
            continue
        values = np.array(
            [
                row.get(local_id)
                if isinstance(row.get(local_id), (int, float))
                else np.nan
                for row in block.rows
            ],
            dtype=float,
        )[mask]
        finite = values[np.isfinite(values)]
        if len(np.unique(np.round(finite, 12))) > 1:
            return Diagnostic(
                code="UNCONTROLLED_STATE_VARIABLE",
                message=(
                    f"{declaration.get('name') or declaration.get('var_id')} "
                    "varies after filtering. Add it to target_constraints so "
                    "systems are compared at a chemically equivalent state."
                ),
                stage="harmonization",
                severity="warning",
                source_key=block.candidate.key,
                details={"BLKvar_id": local_id},
            )
    return None


def _component_maps(
    block: AuthoritativeBlock,
) -> tuple[
    dict[str, dict[str, Any]],
    dict[str, str],
    dict[str, float | None],
]:
    by_org = {
        item["org_num"]: item for item in block.projected["compounds"]
    }
    org_to_global = {
        org: item["comp_num_id"] for org, item in by_org.items()
    }
    masses = {
        item["comp_num_id"]: _molar_mass(item.get("formula") or "")
        for item in by_org.values()
    }
    return by_org, org_to_global, masses


def _composition_declarations(
    block: AuthoritativeBlock,
) -> list[tuple[str, dict[str, Any]]]:
    rows: list[tuple[str, dict[str, Any]]] = []
    for role in ("variable", "constraint"):
        section, _global_field, _local_field = _role_fields(role)
        id_field = "var_id" if role == "variable" else "constr_id"
        for declaration in block.projected[section]:
            if _is_composition(declaration, id_field):
                rows.append((role, declaration))
    return rows


def _component_org_num(declaration: dict[str, Any]) -> str | None:
    value = declaration.get("component_org_num")
    if isinstance(value, str):
        return value
    identifier = str(
        declaration.get("var_id")
        or declaration.get("constr_id")
        or declaration.get("prop_ID")
        or ""
    )
    match = re.search(r"(DOIcomp_[1-9][0-9]*)", identifier)
    return match.group(1) if match else None


def _declaration_component_num_id(
    block: AuthoritativeBlock,
    declaration: dict[str, Any],
) -> str | None:
    org_num = _component_org_num(declaration)
    if org_num is None:
        return None
    for compound in block.projected["compounds"]:
        if compound.get("org_num") == org_num:
            value = compound.get("comp_num_id")
            return value if isinstance(value, str) else None
    return None


def _declaration_matches_bindings(
    block: AuthoritativeBlock,
    declaration: dict[str, Any],
    *,
    component_comp_num_id: str | None,
    phase_num_id: str | None,
) -> bool:
    if (
        component_comp_num_id is not None
        and _declaration_component_num_id(block, declaration)
        != component_comp_num_id
    ):
        return False
    if phase_num_id is not None and _phase(declaration)[0] != phase_num_id:
        return False
    return True


def _coordinate_order(
    comp_num_ids: tuple[str, ...],
    centers: tuple[str, ...],
) -> tuple[str, ...]:
    center_order = [value for value in centers if value in comp_num_ids]
    remainder = sorted(value for value in comp_num_ids if value not in center_order)
    ordered = tuple(center_order + remainder)
    if len(ordered) != len(comp_num_ids):
        raise ValueError("composition order does not cover every component")
    return ordered


def _composition_matrix(
    block: AuthoritativeBlock,
    mask: np.ndarray,
    centers: tuple[str, ...],
    unary_reference_pool: dict[str, dict[str, list[dict[str, Any]]]],
    phase_num_id: str | None,
    row_relevance_scores: np.ndarray | None = None,
) -> tuple[
    np.ndarray | None,
    tuple[str, ...],
    tuple[str, ...],
    dict[str, Any],
    Diagnostic | None,
]:
    """Resolve every usable composition definition into one canonical table."""
    comp_num_ids = tuple(
        item["comp_num_id"] for item in block.projected["compounds"]
    )
    order = _coordinate_order(comp_num_ids, centers)
    _by_org, org_to_global, masses = _component_maps(block)
    masked_rows = [
        row for row, keep in zip(block.rows, mask) if bool(keep)
    ]
    row_ids = tuple(str(row["BLKpoint_id"]) for row in masked_rows)
    solvent_ids = {
        org_to_global[item["component_org_num"]]
        for item in block.projected.get("solvents", [])
        if isinstance(item, dict)
        and item.get("component_org_num") in org_to_global
    }

    fields: list[CompositionField] = []
    for role, declaration in _composition_declarations(block):
        id_field = "var_id" if role == "variable" else "constr_id"
        identifier = str(declaration.get(id_field) or "")
        basis = detect_composition_basis(identifier)
        scope_component_num_ids: tuple[str, ...] = ()
        if basis == "solvent_scoped":
            scoped_prefixes = {
                "solvent_mole_fraction": "mole_fraction",
                "solvent_mass_fraction": "mass_fraction",
                "solvent_volume_fraction": "volume_fraction",
            }
            basis = next(
                (
                    normalized
                    for prefix, normalized in scoped_prefixes.items()
                    if identifier.lower().startswith(prefix)
                ),
                "unsupported_solvent_scoped",
            )
            scope_component_num_ids = tuple(
                component for component in order if component in solvent_ids
            )
        org_num = _component_org_num(declaration)
        if basis in {"unknown", "unsupported_solvent_scoped"} or org_num not in org_to_global:
            continue
        _section, global_field, local_field = _role_fields(role)
        local_id = declaration.get(local_field)
        global_id = declaration.get(global_field)
        if not isinstance(local_id, str) or not isinstance(global_id, str):
            continue
        values = np.asarray(
            [
                row.get(local_id)
                if isinstance(row.get(local_id), (int, float))
                else np.nan
                for row in masked_rows
            ],
            dtype=float,
        )
        fields.append(
            CompositionField(
                role=role,
                basis=basis,
                component_num_id=org_to_global[org_num],
                local_id=local_id,
                global_id=global_id,
                values=values,
                scope_component_num_ids=scope_component_num_ids,
            )
        )

    bridge_values: dict[str, np.ndarray] = {}
    bridge_source_ids: dict[str, tuple[str, ...]] = {}
    bridge_specs = {
        "GLOBprop_1": ("mass_density", "identity"),
        "GLOBprop_74": ("mass_density", "reciprocal"),
        "GLOBprop_67": ("amount_density", "identity"),
        "GLOBprop_41": ("amount_density", "reciprocal"),
    }
    for declaration in block.projected["properties"]:
        global_id = declaration.get("prop_num_id")
        local_id = declaration.get("BLKprop_id")
        if global_id not in bridge_specs or not isinstance(local_id, str):
            continue
        family, operation = bridge_specs[global_id]
        values = np.asarray(
            [
                row.get(local_id)
                if isinstance(row.get(local_id), (int, float))
                else np.nan
                for row in masked_rows
            ],
            dtype=float,
        )
        if operation == "reciprocal":
            with np.errstate(divide="ignore", invalid="ignore"):
                values = np.where(values > 0, 1.0 / values, np.nan)
        bridge_id = f"{family}::{global_id}::{local_id}"
        bridge_values[bridge_id] = values
        bridge_source_ids[bridge_id] = (local_id,)

    solvent_id = next(iter(solvent_ids)) if len(solvent_ids) == 1 else None

    pure_molar_volumes: dict[str, float] | None = None
    pure_volume_evidence: list[dict[str, Any]] = []
    if unary_reference_pool:
        selected_volumes, ensembles = select_unary_molar_volume_ensembles(
            order,
            unary_reference_pool,
            doi=block.candidate.doi,
            phase_num_id=phase_num_id,
        )
        if selected_volumes is not None:
            pure_molar_volumes = {
                component: float(selected_volumes[index])
                for index, component in enumerate(order)
            }
            pure_volume_evidence = list(ensembles)

    result = solve_composition_alignment(
        component_order=order,
        fields=fields,
        molar_masses_g_mol=masses,
        row_ids=row_ids,
        solvent_comp_num_id=solvent_id,
        bridge_values=bridge_values,
        bridge_source_ids=bridge_source_ids,
        pure_molar_volumes=pure_molar_volumes,
        pure_volume_evidence=pure_volume_evidence,
        closure_atol=COMPOSITION_CLOSURE_ATOL,
        consistency_atol=COMPOSITION_SELF_CONSISTENCY_ATOL,
        volumetric_consistency_rtol=(
            VOLUMETRIC_BRIDGE_SELF_CONSISTENCY_RTOL
        ),
        row_relevance_scores=row_relevance_scores,
    )
    source_identity = {
        "doi": block.candidate.doi,
        "lit_num_id": block.candidate.lit_num_id,
        "block_number": block.candidate.block_number,
        "BLKsubsys_id": block.candidate.BLKsubsys_id,
        "search_scope": block.candidate.search_scope,
    }
    plan = {
        **result.plan,
        "source_identity": source_identity,
        "unit_alignment": list(block.unit_alignment),
    }
    if result.error_code is not None:
        return None, (), (), plan, Diagnostic(
            code=result.error_code,
            message=result.error_message or "Composition alignment failed.",
            stage="composition_identity",
            source_key=block.candidate.key,
            details=result.error_details or {},
        )
    return (
        result.coordinates,
        result.coordinate_bases,
        result.coordinate_comp_num_ids,
        plan,
        None,
    )


def _collapse_replicates(
    coordinates: np.ndarray,
    values: np.ndarray,
    point_ids: list[str],
    constraint_proximity: np.ndarray,
    composition_reliability: np.ndarray,
) -> tuple[
    np.ndarray,
    np.ndarray,
    tuple[tuple[str, ...], ...],
    np.ndarray,
    np.ndarray,
]:
    grouped_values: dict[tuple[float, ...], list[float]] = defaultdict(list)
    grouped_ids: dict[tuple[float, ...], list[str]] = defaultdict(list)
    grouped_constraint: dict[tuple[float, ...], list[float]] = defaultdict(list)
    grouped_composition: dict[tuple[float, ...], list[float]] = defaultdict(list)
    for coordinate, value, point_id, constraint_score, composition_score in zip(
        coordinates,
        values,
        point_ids,
        constraint_proximity,
        composition_reliability,
    ):
        key = tuple(float(item) for item in np.round(coordinate, 12))
        grouped_values[key].append(float(value))
        grouped_ids[key].append(point_id)
        grouped_constraint[key].append(float(constraint_score))
        grouped_composition[key].append(float(composition_score))
    keys = sorted(grouped_values)
    collapsed_coordinates = np.array(keys, dtype=float)
    if collapsed_coordinates.ndim == 1:
        collapsed_coordinates = collapsed_coordinates.reshape(len(keys), 0)
    collapsed_values: list[float] = []
    collapsed_constraint: list[float] = []
    collapsed_composition: list[float] = []
    for key in keys:
        constraint = np.asarray(grouped_constraint[key], dtype=float)
        composition = np.asarray(grouped_composition[key], dtype=float)
        weights = np.maximum(
            constraint * composition, np.finfo(float).tiny
        )
        collapsed_values.append(
            float(np.average(grouped_values[key], weights=weights))
        )
        collapsed_constraint.append(
            float(np.average(constraint, weights=weights))
        )
        collapsed_composition.append(
            float(np.average(composition, weights=weights))
        )
    collapsed_ids = tuple(tuple(grouped_ids[key]) for key in keys)
    return (
        collapsed_coordinates,
        np.asarray(collapsed_values, dtype=float),
        collapsed_ids,
        np.asarray(collapsed_constraint, dtype=float),
        np.asarray(collapsed_composition, dtype=float),
    )


def _composition_hull_coverage(coordinates: np.ndarray) -> float:
    """Fraction of the N-component mole-fraction simplex covered by a source."""
    dimensions = coordinates.shape[1]
    if dimensions == 0:
        return 1.0
    unique = np.unique(np.round(coordinates, 12), axis=0)
    if dimensions == 1:
        return float(
            np.clip(np.ptp(unique[:, 0]) if len(unique) > 1 else 0.0, 0.0, 1.0)
        )
    if len(unique) < dimensions + 1:
        return 0.0
    if np.linalg.matrix_rank(unique[1:] - unique[0]) < dimensions:
        return 0.0
    try:
        covered_volume = float(ConvexHull(unique).volume)
    except QhullError:
        return 0.0
    full_simplex_volume = 1.0 / math.factorial(dimensions)
    return float(
        np.clip(covered_volume / full_simplex_volume, 0.0, 1.0)
    )


def _constraint_signature(
    constraints: tuple[ConstraintSpec, ...],
) -> tuple[tuple[Any, ...], ...]:
    return tuple(
        sorted(
            (
                constraint.quantity_key,
                constraint.component_comp_num_id or "",
                constraint.phase_num_id_filter or "",
                round(constraint.effective_minimum, 12),
                round(constraint.effective_maximum, 12),
            )
            for constraint in constraints
        )
    )


def _quality_score(
    n_points: int,
    coverage: float,
    target_declaration: dict[str, Any],
    *,
    constraint_proximity: float,
    composition_reliability: float,
    evidence_relation: str,
) -> tuple[float, dict[str, Any]]:
    components = {
        "support": min(
            1.0, n_points / PROPERTY_SUPPORT_REFERENCE_POINTS
        ),
        "composition_coverage": float(np.clip(coverage, 0.0, 1.0)),
        "constraint_proximity": float(
            np.clip(constraint_proximity, 0.0, 1.0)
        ),
        "composition_reliability": float(
            np.clip(composition_reliability, 0.0, 1.0)
        ),
        "uncertainty_reporting": (
            1.0 if target_declaration.get("uncertainty") else 0.5
        ),
        "target_directness": (
            1.0 if evidence_relation == "reported_direct" else 0.7
        ),
    }
    score = float(
        np.clip(
            sum(
                PROPERTY_SOURCE_SCORE_WEIGHTS[name] * value
                for name, value in components.items()
            ),
            0.0,
            1.0,
        )
    )
    return score, {
        "kind": "composite_property_source_evidence_score",
        "composite_score": score,
        "components": components,
        "weights": dict(PROPERTY_SOURCE_SCORE_WEIGHTS),
        "support_reference_points": PROPERTY_SUPPORT_REFERENCE_POINTS,
    }


def build_source_series(
    block: AuthoritativeBlock,
    request: NormalizedRequest,
    *,
    unary_reference_pool: dict[
        str, dict[str, list[dict[str, Any]]]
    ] | None = None,
    record_composition_plan: Callable[[dict[str, Any]], None] | None = None,
) -> tuple[list[SourceSeries], list[Diagnostic]]:
    """Return one atomic series for every legitimate target occurrence."""
    if not block.units_aligned:
        raise ValueError(
            f"{block.candidate.key} bypassed the unit-alignment boundary"
        )
    diagnostics: list[Diagnostic] = []
    target_occurrences: list[
        tuple[RankingTarget, dict[str, Any], str, str]
    ] = []
    for target in request.targets:
        for evidence_id in target.evidence_global_ids:
            evidence_role = (
                "property"
                if evidence_id.startswith("GLOBprop_")
                else target.source_role
            )
            section, global_field, local_field = _role_fields(evidence_role)
            for declaration in block.projected[section]:
                if (
                    declaration.get(global_field) == evidence_id
                    and _declaration_matches_bindings(
                        block,
                        declaration,
                        component_comp_num_id=(
                            target.component_comp_num_id
                            if evidence_id == target.source_global_id
                            else None
                        ),
                        phase_num_id=target.phase_num_id_filter,
                    )
                ):
                    target_occurrences.append(
                        (
                            target,
                            declaration,
                            declaration[local_field],
                            evidence_id,
                        )
                    )
    if not target_occurrences:
        diagnostics.append(
            Diagnostic(
                code="TARGET_OCCURRENCE_MISSING",
                message="Coarse registry match has no exact target occurrence.",
                stage="harmonization",
                source_key=block.candidate.key,
            )
        )
        return [], diagnostics

    (
        mask,
        constraint_diagnostics,
        controlled,
        constraint_relevance,
        constraint_match,
    ) = _constraint_mask(block, request.constraints)
    diagnostics.extend(constraint_diagnostics)
    if not np.any(mask):
        return [], diagnostics
    uncontrolled = _uncontrolled_state_diagnostic(
        block,
        mask,
        controlled,
        {
            local_id
            for _target, _decl, local_id, _evidence_id
            in target_occurrences
        },
    )
    if uncontrolled is not None:
        diagnostics.append(uncontrolled)
        return [], diagnostics

    phase_filters = {
        target.phase_num_id_filter
        for target in request.targets
        if target.phase_num_id_filter is not None
    }
    bridge_phase = next(iter(phase_filters)) if len(phase_filters) == 1 else None
    coordinates, bases, coordinate_comp_ids, plan, comp_error = _composition_matrix(
        block,
        mask,
        request.center_comp_num_ids,
        unary_reference_pool or {},
        bridge_phase,
        row_relevance_scores=constraint_relevance[mask],
    )
    if comp_error is not None or coordinates is None:
        diagnostics.append(comp_error or Diagnostic(
            code="COMPOSITION_NORMALIZATION_FAILED",
            message="Composition normalization failed without a diagnostic.",
            stage="composition_identity",
            source_key=block.candidate.key,
        ))
        return [], diagnostics
    if plan.get("conflicting_rows", 0):
        diagnostics.append(
            Diagnostic(
                code="COMPOSITION_ROWS_INCONSISTENT",
                message=(
                    "Some rows were excluded because independently sufficient "
                    "composition definitions disagreed after conversion to "
                    "mole fractions."
                ),
                stage="composition_identity",
                severity="warning",
                source_key=block.candidate.key,
                details={
                    "conflicting_rows": plan["conflicting_rows"],
                    "valid_rows": plan.get("valid_rows", 0),
                    "self_consistency_atol_mole_fraction": plan.get(
                        "self_consistency_atol_mole_fraction"
                    ),
                },
            )
        )
    volumetric_conflicts = (
        plan.get("volumetric_state_layer", {}).get("conflicting_rows", 0)
    )
    if volumetric_conflicts:
        diagnostics.append(
            Diagnostic(
                code="VOLUMETRIC_BRIDGES_INCONSISTENT",
                message=(
                    "Equivalent bulk density/volume fields disagree after "
                    "conversion to a common volumetric state."
                ),
                stage="composition_identity",
                severity="warning",
                source_key=block.candidate.key,
                details={
                    "conflicting_rows": volumetric_conflicts,
                    "relative_tolerance": plan[
                        "volumetric_state_layer"
                    ]["self_consistency_rtol"],
                },
            )
        )
    if record_composition_plan is not None:
        record_composition_plan(
            {
                "source_key": block.candidate.key,
                "doi": block.candidate.doi,
                "lit_num_id": block.candidate.lit_num_id,
                "block_number": block.candidate.block_number,
                "BLKsubsys_id": block.candidate.BLKsubsys_id,
                **plan,
            }
        )

    masked_rows = [
        row for row, keep in zip(block.rows, mask) if bool(keep)
    ]
    masked_constraint_relevance = constraint_relevance[mask]
    compounds = {
        item["comp_num_id"]: item for item in block.projected["compounds"]
    }
    ordered_comp_ids = tuple(plan.get("component_order") or block.candidate.comp_num_ids)
    compound_names = tuple(
        compounds[value]["name"] for value in ordered_comp_ids
    )
    series: list[SourceSeries] = []
    for target, declaration, local_id, evidence_id in target_occurrences:
        raw_values = np.array(
            [
                row.get(local_id)
                if isinstance(row.get(local_id), (int, float))
                else np.nan
                for row in masked_rows
            ],
            dtype=float,
        )
        finite = np.isfinite(raw_values) & np.all(
            np.isfinite(coordinates), axis=1
        )
        if not np.any(finite):
            diagnostics.append(
                Diagnostic(
                    code="NO_FINITE_TARGET_ROWS",
                    message=f"{local_id} has no finite values at the requested state.",
                    stage="harmonization",
                    source_key=block.candidate.key,
                )
            )
            continue
        row_assignment_scores = np.asarray(
            [
                (
                    assignment["selected_group_composite_score"]
                    if assignment.get("status") == "valid"
                    else np.nan
                )
                for assignment in plan["row_assignments"]
            ],
            dtype=float,
        )
        if len(row_assignment_scores) != len(finite):
            raise ValueError(
                f"{block.candidate.key} composition assignments do not "
                "match the retained composition rows"
            )
        point_ids = [
            str(row["BLKpoint_id"])
            for row, keep in zip(masked_rows, finite)
            if bool(keep)
        ]
        (
            collapsed_x,
            collapsed_y,
            collapsed_ids,
            collapsed_constraint_proximity,
            collapsed_composition_reliability,
        ) = _collapse_replicates(
            coordinates[finite],
            raw_values[finite],
            point_ids,
            masked_constraint_relevance[finite],
            row_assignment_scores[finite],
        )
        coverage = _composition_hull_coverage(collapsed_x)
        phase_num_id, phase_id = _phase(declaration)
        presentation = declaration.get("presentation")
        presentation_kind = classify_presentation(presentation)
        reference_semantics = _reference_semantics(block, declaration)
        alignment = declaration.get("unit_alignment")
        if not isinstance(alignment, dict):
            raise ValueError(
                f"{block.candidate.key}/{local_id} lacks unit alignment"
            )
        reported_unit = alignment.get("to_unit")
        if not isinstance(reported_unit, str):
            raise ValueError(
                f"{block.candidate.key}/{local_id} lacks reported unit"
            )
        source_key = (
            f"{block.candidate.key}::{local_id}::{target.quantity_key}"
            f"::{evidence_id}"
        )
        evidence_metadata = EVIDENCE_METADATA.get(
            evidence_id,
            {
                "quantity_key": target.quantity_key,
                "canonical_unit": target.canonical_unit,
            },
        )
        if presentation_kind == PresentationKind.DIRECT:
            response_semantics = "absolute_observed_quantity"
            evidence_relation = (
                "reported_direct"
                if evidence_id == target.source_global_id
                else "unmaterialized_bridge_evidence"
            )
        elif presentation_requires_reference(presentation_kind):
            response_semantics = "reference_response_unmaterialized"
            evidence_relation = (
                "reported_reference_response"
                if evidence_id == target.source_global_id
                else "unmaterialized_reference_bridge_evidence"
            )
        else:
            response_semantics = "unsupported_reported_response"
            evidence_relation = "unsupported_reported_response"
        composition_reliability = (
            float(np.mean(row_assignment_scores[finite]))
        )
        source_constraint_proximity = float(
            np.mean(masked_constraint_relevance[finite])
        )
        quality_score, evidence_score = _quality_score(
            len(collapsed_y),
            coverage,
            declaration,
            constraint_proximity=source_constraint_proximity,
            composition_reliability=composition_reliability,
            evidence_relation=evidence_relation,
        )
        series.append(
            SourceSeries(
                source_key=source_key,
                doi=block.candidate.doi,
                lit_num_id=block.candidate.lit_num_id,
                block_number=block.candidate.block_number,
                BLKsubsys_id=block.candidate.BLKsubsys_id,
                search_scope=block.candidate.search_scope,
                system_type=block.candidate.effective_system_type,
                comp_num_ids=ordered_comp_ids,
                compound_names=compound_names,
                target=target,
                target_local_id=local_id,
                phase_num_id=phase_num_id,
                phase_id=phase_id,
                presentation=presentation,
                presentation_kind=presentation_kind.value,
                reported_unit=reported_unit,
                response_semantics=response_semantics,
                reference_semantics=reference_semantics,
                coordinates=collapsed_x,
                values=collapsed_y,
                point_ids=collapsed_ids,
                original_coordinate_basis=bases,
                coordinate_comp_num_ids=coordinate_comp_ids,
                constraint_signature=_constraint_signature(request.constraints),
                quality_score=quality_score,
                derivation={
                    **plan,
                    "constraint_match": {
                        **constraint_match,
                        "target_finite_mean_score": (
                            source_constraint_proximity
                        ),
                    },
                    "evidence_score": evidence_score,
                    "replicate_aggregation": (
                        "constraint_and_composition_reliability_weighted_"
                        "mean_within_source_only"
                    ),
                    "n_authoritative_rows": len(masked_rows),
                    "n_unique_coordinates": len(collapsed_y),
                },
                observed_global_id=evidence_id,
                observed_quantity_key=evidence_metadata["quantity_key"],
                observed_canonical_unit=evidence_metadata["canonical_unit"],
                evidence_relation=evidence_relation,
                coordinate_constraint_proximity=(
                    collapsed_constraint_proximity
                ),
                coordinate_composition_reliability=(
                    collapsed_composition_reliability
                ),
            )
        )
    return series, diagnostics


def validate_harmonized_sources(
    sources: list[SourceSeries],
) -> list[SourceSeries]:
    """Validate provenance, dimensions, finite values, and compositions.

    PCS declarations already store numerical values in registry-canonical
    units, while agent-supplied state values are converted during strict
    parsing.  The post-branch barrier validates that invariant rather than
    guessing conversions.  An empty canonical-unit string is accepted because
    several valid ThermoML fractions and ratios are dimensionless.
    """
    for source in sources:
        if not source.doi or not source.lit_num_id:
            raise ValueError(
                f"{source.source_key} lacks paired DOI/lit_num_id provenance"
            )
        expected_dimensions = max(0, len(source.comp_num_ids) - 1)
        if source.coordinates.ndim != 2:
            raise ValueError(
                f"{source.source_key} coordinates are not a 2-D matrix"
            )
        if source.coordinates.shape[1] != expected_dimensions:
            raise ValueError(
                f"{source.source_key} has {source.coordinates.shape[1]} "
                f"coordinates for {len(source.comp_num_ids)} components"
            )
        if not (
            len(source.coordinates)
            == len(source.values)
            == len(source.point_ids)
        ):
            raise ValueError(
                f"{source.source_key} value/coordinate/provenance lengths differ"
            )
        for score_name, scores in (
            (
                "coordinate_constraint_proximity",
                source.coordinate_constraint_proximity,
            ),
            (
                "coordinate_composition_reliability",
                source.coordinate_composition_reliability,
            ),
        ):
            if len(scores) != len(source.values):
                raise ValueError(
                    f"{source.source_key} {score_name} length differs"
                )
            if np.any(~np.isfinite(scores)) or np.any(
                (scores < 0.0) | (scores > 1.0)
            ):
                raise ValueError(
                    f"{source.source_key} {score_name} must be finite in [0, 1]"
                )
        if not np.all(np.isfinite(source.values)):
            raise ValueError(
                f"{source.source_key} contains non-finite target values"
            )
        if not np.all(np.isfinite(source.coordinates)):
            raise ValueError(
                f"{source.source_key} contains non-finite compositions"
            )
        if source.coordinates.size:
            if np.any(source.coordinates < -1e-10):
                raise ValueError(
                    f"{source.source_key} contains a negative mole fraction"
                )
            if np.any(source.coordinates > 1.0 + 1e-10):
                raise ValueError(
                    f"{source.source_key} contains a mole fraction above one"
                )
            if np.any(source.coordinates.sum(axis=1) > 1.0 + 1e-8):
                raise ValueError(
                    f"{source.source_key} independent fractions exceed unity"
                )
        if any(not ids for ids in source.point_ids):
            raise ValueError(
                f"{source.source_key} has a value without BLKpoint evidence"
            )
        if not math.isfinite(source.quality_score):
            raise ValueError(
                f"{source.source_key} has a non-finite evidence score"
            )
    return sources
