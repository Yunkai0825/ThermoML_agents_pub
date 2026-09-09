"""Strict parser and confirmation review for the flat LLM-facing contract."""

from __future__ import annotations

import hashlib
import json
import math
import re
import secrets
from dataclasses import dataclass
from typing import Any

from card_db_search_tools.basic_search_tools.advanced_block_search.catalogs import (
    CompoundRecord,
    RuntimeCatalogs,
    TranslationRow,
    load_runtime_catalogs,
)
from card_db_search_tools.basic_search_tools.advanced_block_search.errors import (
    AdvancedSearchError,
)

from ..tool_settings import (
    COMPOSITION_CLOSURE_ATOL,
    DEFAULT_SOFT_TOLERANCE,
    MAX_RETURNED_SYSTEMS,
    SOFT_TOLERANCE_BY_CANONICAL_UNIT,
    SOFT_TOLERANCE_BY_QUANTITY,
)
from ..unit_conversion_lib import (
    UnitConversionError,
    accepted_units,
    conversion_trace,
)
from .models import ConstraintSpec, NormalizedRequest, RankingTarget


_CONFIRMATION_TOKEN_PREFIX = "psr_"
_GLOBAL_QUANTITY_RE = re.compile(r"^GLOB(?:prop|var|constr)_[1-9][0-9]*$")
_GLOBAL_COMPOUND_RE = re.compile(r"^GLOBcomp_[1-9][0-9]*$")
_GLOBAL_PHASE_RE = re.compile(r"^GLOBphase_[1-9][0-9]*$")
_NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
_BETWEEN_RE = re.compile(
    rf"^(?P<id>.+?)\s+BETWEEN\s+(?P<lo>{_NUMBER})\s*(?P<u1>[^\s;]+)?"
    rf"\s+AND\s+(?P<hi>{_NUMBER})\s*(?P<u2>[^\s;]+)?"
    rf"(?:\s*;\s*tol\s*=\s*(?P<tol>{_NUMBER})\s*(?P<ut>[^\s;]+)?)?$",
    re.IGNORECASE,
)
_EQUAL_RE = re.compile(
    rf"^(?P<id>.+?)\s*=\s*(?P<value>{_NUMBER})\s*(?P<unit>[^\s;±]+)?"
    rf"(?:\s*(?:±|\+/-)\s*(?P<pm>{_NUMBER})\s*(?P<upm>[^\s;]+)?)?"
    rf"(?:\s*;\s*tol\s*=\s*(?P<tol>{_NUMBER})\s*(?P<ut>[^\s;]+)?)?$",
    re.IGNORECASE,
)


class RequestValidationError(ValueError):
    """A correctable, agent-facing input error."""

    def __init__(self, code: str, message: str, *, field: str) -> None:
        super().__init__(message)
        self.code = code
        self.field = field

    def as_issue(self, *, field: str | None = None) -> dict[str, str]:
        return {
            "code": self.code,
            "field": field or self.field,
            "message": str(self),
        }


@dataclass(frozen=True)
class RequestReviewOutcome:
    """One deterministic parse/confirmation decision."""

    review: dict[str, Any]
    request: NormalizedRequest | None
    database_fingerprint: dict[str, Any] | None


def _flat_strings(value: str | list[str], field: str) -> list[str]:
    if isinstance(value, str):
        values = [value]
    elif isinstance(value, list) and all(isinstance(item, str) for item in value):
        values = value
    else:
        raise RequestValidationError(
            "INVALID_FLAT_INPUT",
            f"{field} must be one string or a flat list[str].",
            field=field,
        )
    clean = [item.strip() for item in values if item.strip()]
    if not clean:
        raise RequestValidationError(
            "MISSING_REQUIRED_INPUT",
            f"{field} requires at least one non-empty entry.",
            field=field,
        )
    return clean


def _optional_flat_strings(
    value: str | list[str] | None, field: str
) -> list[str]:
    if value is None:
        return []
    return _flat_strings(value, field)


def _resolve_quantity(
    text: str,
    catalogs: RuntimeCatalogs,
    *,
    field: str,
) -> TranslationRow:
    value = text.strip()
    if not _GLOBAL_QUANTITY_RE.fullmatch(value):
        raise RequestValidationError(
            "GLOBAL_QUANTITY_ID_REQUIRED",
            f"{field} identifier {value!r} is not a typed "
            "GLOBprop_N/GLOBvar_N/GLOBconstr_N ID. Resolve names before "
            "calling this tool; do not submit names, keys, DOI IDs, or BLK IDs.",
            field=field,
        )
    try:
        return catalogs.translation.resolve(
            {"global_id": value}, f"/{field}"
        ).row
    except AdvancedSearchError as exc:
        raise RequestValidationError(
            exc.code,
            exc.message,
            field=field,
        ) from exc


def _parse_options(text: str) -> tuple[str, dict[str, str]]:
    segments = [segment.strip() for segment in text.split(";")]
    identity = segments[0]
    options: dict[str, str] = {}
    for segment in segments[1:]:
        if not segment:
            continue
        if "=" not in segment:
            raise RequestValidationError(
                "INVALID_TARGET_OPTION",
                f"Target option {segment!r} must be key=value.",
                field="ranking_targets",
            )
        key, value = (item.strip() for item in segment.split("=", 1))
        key = key.casefold()
        if key in options:
            raise RequestValidationError(
                "DUPLICATE_TARGET_OPTION",
                f"Target option {key!r} is repeated.",
                field="ranking_targets",
            )
        options[key] = value
    return identity, options


def _require_correct_component_binding(
    row: TranslationRow,
    options: dict[str, str],
    *,
    field: str,
) -> None:
    supplied = "component" in options
    if row.component_linked and not supplied:
        raise RequestValidationError(
            "COMPONENT_BINDING_REQUIRED",
            f"{row.quantity_key!r} is a component-linked global template. "
            "Add '; component=GLOBcomp_N' so DOI-local occurrences can be "
            "resolved without guessing.",
            field=field,
        )
    if not row.component_linked and supplied:
        raise RequestValidationError(
            "COMPONENT_BINDING_NOT_ALLOWED",
            f"{row.quantity_key!r} is not component-linked; remove the "
            "component option.",
            field=field,
        )


def _composition_tuple(value: str) -> tuple[float, ...]:
    parts = [part.strip() for part in value.split(",")]
    try:
        point = tuple(float(part) for part in parts)
    except ValueError as exc:
        raise RequestValidationError(
            "INVALID_COMPOSITION",
            f"Mole-fraction target {value!r} must contain comma-separated numbers.",
            field="ranking_targets",
        ) from exc
    if not point or any(
        not math.isfinite(item) or item < 0.0 or item > 1.0 for item in point
    ):
        raise RequestValidationError(
            "INVALID_COMPOSITION",
            "Mole-fraction coordinates must be finite values in [0, 1].",
            field="ranking_targets",
        )
    if sum(point) > 1.0 + COMPOSITION_CLOSURE_ATOL:
        raise RequestValidationError(
            "INVALID_COMPOSITION",
            "Independent mole-fraction coordinates cannot sum above one.",
            field="ranking_targets",
        )
    return point


def _parse_targets(
    value: str | list[str], catalogs: RuntimeCatalogs
) -> tuple[RankingTarget, ...]:
    targets: list[RankingTarget] = []
    for raw in _flat_strings(value, "ranking_targets"):
        identity, options = _parse_options(raw)
        unknown = sorted(
            set(options)
            - {
                "basis",
                "direction",
                "at_mole_fraction",
                "aggregate",
                "component",
                "phase",
            }
        )
        if unknown:
            raise RequestValidationError(
                "UNKNOWN_TARGET_OPTION",
                f"Unknown ranking-target options: {unknown}.",
                field="ranking_targets",
            )
        row = _resolve_quantity(
            identity,
            catalogs,
            field="ranking_targets",
        )
        _require_correct_component_binding(
            row,
            options,
            field="ranking_targets.component",
        )
        source_role: str
        source_id: str
        if row.prop_num_id is not None:
            source_role, source_id = "property", row.prop_num_id
        elif row.var_num_id is not None:
            source_role, source_id = "variable", row.var_num_id
        else:
            raise RequestValidationError(
                "UNRANKABLE_QUANTITY",
                f"{identity!r} exists only as a fixed constraint and cannot be "
                "ranked as an observed series.",
                field="ranking_targets",
            )
        basis = options.get("basis", "real").casefold()
        if basis not in {"real", "ideal", "deviation", "absolute_deviation"}:
            raise RequestValidationError(
                "INVALID_RANKING_BASIS",
                "basis must be real, ideal, deviation, or absolute_deviation.",
                field="ranking_targets",
            )
        direction = options.get("direction", "maximize").casefold()
        if direction not in {"maximize", "minimize"}:
            raise RequestValidationError(
                "INVALID_RANKING_DIRECTION",
                "direction must be maximize or minimize.",
                field="ranking_targets",
            )
        aggregate = options.get("aggregate", "mean").casefold()
        if aggregate not in {"mean", "maximum", "minimum", "integral"}:
            raise RequestValidationError(
                "INVALID_RANKING_AGGREGATE",
                "aggregate must be mean, maximum, minimum, or integral.",
                field="ranking_targets",
            )
        component = (
            _resolve_compound(
                options["component"],
                catalogs,
                field="ranking_targets.component",
            )
            if "component" in options
            else None
        )
        phase = (
            catalogs.phases_by_id[
                _resolve_phase(
                    options["phase"],
                    catalogs,
                    field="ranking_targets.phase",
                )
            ]
            if "phase" in options
            else None
        )
        targets.append(
            RankingTarget(
                input_value=raw,
                quantity_key=row.quantity_key,
                preferred_name=row.preferred_name,
                canonical_unit=row.semantics.canonical_unit or "",
                prop_num_id=row.prop_num_id,
                var_num_id=row.var_num_id,
                constr_num_id=row.constr_num_id,
                source_role=source_role,
                source_global_id=source_id,
                basis=basis,
                direction=direction,
                ranking_composition=(
                    _composition_tuple(options["at_mole_fraction"])
                    if "at_mole_fraction" in options
                    else None
                ),
                aggregate=aggregate,
                component_comp_num_id=(
                    component.comp_num_id if component is not None else None
                ),
                phase_num_id_filter=(
                    phase.phase_num_id if phase is not None else None
                ),
                component=(
                    component.as_dict() if component is not None else None
                ),
                phase_filter=(
                    {
                        "phase_num_id": phase.phase_num_id,
                        "phase_id": phase.phase_id,
                        "phase_name": phase.phase_name,
                    }
                    if phase is not None
                    else None
                ),
                component_linked=row.component_linked,
            )
        )
    return tuple(targets)


def _converted(
    value: float,
    unit: str,
    canonical: str,
    *,
    role: str,
    is_delta: bool = False,
) -> tuple[float, dict[str, Any]]:
    try:
        return conversion_trace(
            value=value,
            input_unit=unit,
            canonical_unit=canonical,
            role=role,
            is_delta=is_delta,
        )
    except UnitConversionError as exc:
        raise RequestValidationError(
            "UNIT_MISMATCH", str(exc), field="target_constraints"
        ) from exc


def _soft_tolerance_rule(
    quantity_key: str, canonical_unit: str
) -> dict[str, float | str]:
    return dict(
        SOFT_TOLERANCE_BY_QUANTITY.get(quantity_key)
        or SOFT_TOLERANCE_BY_CANONICAL_UNIT.get(canonical_unit)
        or DEFAULT_SOFT_TOLERANCE
    )


def _expanded_constraint_bounds(
    *,
    quantity_key: str,
    canonical_unit: str,
    minimum: float,
    maximum: float,
    explicit_tolerance: float | None,
) -> tuple[float, float, str, float, str]:
    if explicit_tolerance is not None:
        value = abs(float(explicit_tolerance))
        return (
            minimum - value,
            maximum + value,
            "additive",
            value,
            "explicit",
        )

    rule = _soft_tolerance_rule(quantity_key, canonical_unit)
    kind = str(rule["kind"])
    value = float(rule["value"])
    if kind == "additive":
        effective_minimum = minimum - value
        effective_maximum = maximum + value
    elif kind == "log10":
        if minimum <= 0.0 or maximum <= 0.0:
            raise RequestValidationError(
                "INVALID_LOG_TOLERANCE_DOMAIN",
                f"Automatic log-scale tolerance for {quantity_key!r} "
                "requires positive bounds. Supply an explicit ±/tol value "
                "to request an additive window around zero.",
                field="target_constraints",
            )
        factor = 10.0 ** value
        effective_minimum = minimum / factor
        effective_maximum = maximum * factor
    elif kind == "relative":
        floor = float(rule.get("absolute_floor", 0.0))
        lower_margin = max(abs(minimum) * value, floor)
        upper_margin = max(abs(maximum) * value, floor)
        effective_minimum = minimum - lower_margin
        effective_maximum = maximum + upper_margin
    else:
        raise RuntimeError(f"unsupported soft tolerance kind {kind!r}")
    return effective_minimum, effective_maximum, kind, value, "automatic"


def _constraint_options(raw: str) -> tuple[str, dict[str, str]]:
    segments = [segment.strip() for segment in raw.split(";")]
    expression = segments[0]
    options: dict[str, str] = {}
    for segment in segments[1:]:
        if not segment:
            continue
        if "=" not in segment:
            raise RequestValidationError(
                "INVALID_CONSTRAINT_OPTION",
                f"Constraint option {segment!r} must be key=value.",
                field="target_constraints",
            )
        key, value = (part.strip() for part in segment.split("=", 1))
        key = key.casefold()
        if key not in {"tol", "component", "phase"}:
            raise RequestValidationError(
                "UNKNOWN_CONSTRAINT_OPTION",
                f"Unknown constraint option {key!r}.",
                field="target_constraints",
            )
        if key in options:
            raise RequestValidationError(
                "DUPLICATE_CONSTRAINT_OPTION",
                f"Constraint option {key!r} is repeated.",
                field="target_constraints",
            )
        if not value:
            raise RequestValidationError(
                "INVALID_CONSTRAINT_OPTION",
                f"Constraint option {key!r} requires a value.",
                field="target_constraints",
            )
        options[key] = value
    if "tol" in options:
        expression = f"{expression}; tol={options['tol']}"
    return expression, options


def _parse_constraints(
    value: str | list[str], catalogs: RuntimeCatalogs
) -> tuple[ConstraintSpec, ...]:
    constraints: list[ConstraintSpec] = []
    for raw in _flat_strings(value, "target_constraints"):
        expression, options = _constraint_options(raw)
        between = _BETWEEN_RE.fullmatch(expression)
        equal = _EQUAL_RE.fullmatch(expression)
        traces: list[dict[str, Any]] = []
        explicit_tolerance: float | None = None
        if between is not None:
            identity = between.group("id").strip()
            row = _resolve_quantity(
                identity,
                catalogs,
                field="target_constraints",
            )
            _require_correct_component_binding(
                row,
                options,
                field="target_constraints.component",
            )
            canonical = row.semantics.canonical_unit or ""
            u1 = between.group("u1") or canonical
            u2 = between.group("u2") or u1
            lo, trace = _converted(
                float(between.group("lo")),
                u1,
                canonical,
                role="lower_bound",
            )
            traces.append(trace)
            hi, trace = _converted(
                float(between.group("hi")),
                u2,
                canonical,
                role="upper_bound",
            )
            traces.append(trace)
            if lo > hi:
                lo, hi = hi, lo
            if between.group("tol") is not None:
                explicit_tolerance, trace = _converted(
                    float(between.group("tol")),
                    between.group("ut") or canonical,
                    canonical,
                    role="explicit_tolerance",
                    is_delta=True,
                )
                traces.append(trace)
        elif equal is not None:
            identity = equal.group("id").strip()
            row = _resolve_quantity(
                identity,
                catalogs,
                field="target_constraints",
            )
            _require_correct_component_binding(
                row,
                options,
                field="target_constraints.component",
            )
            canonical = row.semantics.canonical_unit or ""
            unit = equal.group("unit") or canonical
            center, trace = _converted(
                float(equal.group("value")),
                unit,
                canonical,
                role="center",
            )
            traces.append(trace)
            lo = hi = center
            raw_tolerance = equal.group("pm") or equal.group("tol")
            if raw_tolerance is not None:
                tolerance_unit = (
                    equal.group("upm") or equal.group("ut") or unit
                )
                explicit_tolerance, trace = _converted(
                    float(raw_tolerance),
                    tolerance_unit,
                    canonical,
                    role="explicit_tolerance",
                    is_delta=True,
                )
                traces.append(trace)
        else:
            raise RequestValidationError(
                "INVALID_CONSTRAINT",
                "Constraint must be 'QUANTITY = value unit ± tolerance unit' "
                "or 'QUANTITY BETWEEN low unit AND high unit; tol=value unit'.",
                field="target_constraints",
            )

        (
            effective_minimum,
            effective_maximum,
            tolerance_kind,
            tolerance_value,
            tolerance_source,
        ) = _expanded_constraint_bounds(
            quantity_key=row.quantity_key,
            canonical_unit=canonical,
            minimum=lo,
            maximum=hi,
            explicit_tolerance=explicit_tolerance,
        )
        component = (
            _resolve_compound(
                options["component"],
                catalogs,
                field="target_constraints.component",
            )
            if "component" in options
            else None
        )
        phase = (
            catalogs.phases_by_id[
                _resolve_phase(
                    options["phase"],
                    catalogs,
                    field="target_constraints.phase",
                )
            ]
            if "phase" in options
            else None
        )
        constraints.append(
            ConstraintSpec(
                input_value=raw,
                quantity_key=row.quantity_key,
                preferred_name=row.preferred_name,
                canonical_unit=canonical,
                available_global_ids=row.available_global_ids,
                minimum=lo,
                maximum=hi,
                effective_minimum=effective_minimum,
                effective_maximum=effective_maximum,
                tolerance_kind=tolerance_kind,
                tolerance_value=tolerance_value,
                tolerance_source=tolerance_source,
                unit_conversion_trace=tuple(traces),
                accepted_input_units=accepted_units(canonical),
                component_comp_num_id=(
                    component.comp_num_id if component is not None else None
                ),
                phase_num_id_filter=(
                    phase.phase_num_id if phase is not None else None
                ),
                component=(
                    component.as_dict() if component is not None else None
                ),
                phase_filter=(
                    {
                        "phase_num_id": phase.phase_num_id,
                        "phase_id": phase.phase_id,
                        "phase_name": phase.phase_name,
                    }
                    if phase is not None
                    else None
                ),
                component_linked=row.component_linked,
            )
        )
    return tuple(constraints)

def _resolve_compound(
    text: str,
    catalogs: RuntimeCatalogs,
    *,
    field: str = "center_comp_num_ids",
) -> CompoundRecord:
    value = text.strip()
    if not _GLOBAL_COMPOUND_RE.fullmatch(value):
        raise RequestValidationError(
            "GLOBAL_COMPOUND_ID_REQUIRED",
            f"{field} identifier {value!r} is not GLOBcomp_N. "
            "Resolve compound names/structures before calling this tool; do "
            "not submit names, InChI, SMILES, DOI IDs, or BLK IDs.",
            field=field,
        )
    try:
        return catalogs.resolve_compound(
            {"comp_num_id": value},
            f"/{field}",
        )
    except AdvancedSearchError as exc:
        raise RequestValidationError(
            exc.code,
            exc.message,
            field=field,
        ) from exc


def _resolve_phase(
    text: str,
    catalogs: RuntimeCatalogs,
    *,
    field: str = "phase",
) -> str:
    value = text.strip()
    if not _GLOBAL_PHASE_RE.fullmatch(value):
        raise RequestValidationError(
            "GLOBAL_PHASE_ID_REQUIRED",
            f"{field} identifier {value!r} is not GLOBphase_N. Resolve phase "
            "names before calling this tool.",
            field=field,
        )
    if value not in catalogs.phases_by_id:
        raise RequestValidationError(
            "UNKNOWN_PHASE",
            f"Unknown global phase ID {value!r}.",
            field=field,
        )
    return value


def _parse_grid(
    value: str | list[str],
) -> tuple[tuple[float, ...], ...] | None:
    if isinstance(value, str) and value.strip().casefold() == "auto":
        return None
    values = _flat_strings(value, "comparison_grid")
    points: list[tuple[float, ...]] = []
    for item in values:
        for segment in item.split(";"):
            segment = segment.strip()
            if segment:
                points.append(_composition_tuple(segment))
    dimensions = {len(point) for point in points}
    if len(dimensions) != 1:
        raise RequestValidationError(
            "INCONSISTENT_GRID_DIMENSION",
            "Every comparison-grid point must have the same number of coordinates.",
            field="comparison_grid",
        )
    return tuple(sorted(set(points)))


def parse_request(
    *,
    ranking_targets: str | list[str],
    target_constraints: str | list[str],
    center_comp_num_ids: str | list[str],
    purpose: str,
    tasks: str,
    system_type: str | None = None,
    system_scope: str = "declared",
    comparison_grid: str | list[str] = "auto",
    limit: int = 20,
) -> NormalizedRequest:
    """Resolve the flat public contract into immutable chemistry identities."""
    catalogs = load_runtime_catalogs()
    targets = _parse_targets(ranking_targets, catalogs)
    constraints = _parse_constraints(target_constraints, catalogs)
    compounds = tuple(
        _resolve_compound(value, catalogs)
        for value in _flat_strings(
            center_comp_num_ids,
            "center_comp_num_ids",
        )
    )
    if len({row.comp_num_id for row in compounds}) != len(compounds):
        raise RequestValidationError(
            "DUPLICATE_COMPOUND",
            "center_comp_num_ids contains duplicate global compound IDs.",
            field="center_comp_num_ids",
        )
    if not isinstance(purpose, str) or not purpose.strip():
        raise RequestValidationError(
            "MISSING_REQUIRED_INPUT",
            "purpose must be a non-empty chemistry goal.",
            field="purpose",
        )
    if not isinstance(tasks, str) or not tasks.strip():
        raise RequestValidationError(
            "MISSING_REQUIRED_INPUT",
            "tasks must be one non-empty flat instruction string.",
            field="tasks",
        )
    parsed_tasks = (tasks.strip(),)
    scope = str(system_scope).strip().casefold()
    if scope not in {"declared", "subsystem", "either"}:
        raise RequestValidationError(
            "INVALID_SYSTEM_SCOPE",
            "system_scope must be declared, subsystem, or either. "
            "BLKsubsys search is optional and off by default.",
            field="system_scope",
        )
    parsed_system_type = None
    if system_type is not None:
        parsed_system_type = str(system_type).strip().casefold()
        if not re.fullmatch(
            r"(?:unary|binary|ternary|quaternary|[5-9][0-9]*-component)",
            parsed_system_type,
        ):
            raise RequestValidationError(
                "INVALID_SYSTEM_TYPE",
                "system_type must be unary, binary, ternary, quaternary, "
                "or N-component for N>=5.",
                field="system_type",
            )
        _system_sizes = {"unary": 1, "binary": 2, "ternary": 3, "quaternary": 4}
        _size = _system_sizes.get(
            parsed_system_type,
            int(parsed_system_type.split("-")[0])
            if parsed_system_type.endswith("-component")
            else None,
        )
        if _size is not None and len(compounds) > _size:
            raise RequestValidationError(
                "IMPOSSIBLE_CENTER_SYSTEM",
                f"{len(compounds)} center compounds can never all appear in one "
                f"{parsed_system_type} system. center_comp_num_ids lists ONLY the "
                "compound(s) shared by every compared system (the fixed chemistry "
                "axis, e.g. water when ranking aqueous binaries); the ranked "
                "alternatives are the remaining components and must NOT be listed.",
                field="center_comp_num_ids",
            )
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= MAX_RETURNED_SYSTEMS:
        raise RequestValidationError(
            "INVALID_LIMIT",
            f"limit must be an integer from 1 through {MAX_RETURNED_SYSTEMS} and applies only "
            "after deterministic ranking.",
            field="limit",
        )
    return NormalizedRequest(
        targets=targets,
        constraints=constraints,
        center_comp_num_ids=tuple(row.comp_num_id for row in compounds),
        center_compounds=tuple(row.as_dict() for row in compounds),
        purpose=purpose.strip(),
        tasks=parsed_tasks,
        system_type=parsed_system_type,
        system_scope=scope,
        comparison_grid=_parse_grid(comparison_grid),
        limit=limit,
    )


def _original_tool_call(
    *,
    ranking_targets: Any,
    target_constraints: Any,
    center_comp_num_ids: Any,
    purpose: Any,
    tasks: Any,
    system_type: Any,
    system_scope: Any,
    comparison_grid: Any,
    limit: Any,
) -> dict[str, Any]:
    return {
        "ranking_targets": ranking_targets,
        "target_constraints": target_constraints,
        "center_comp_num_ids": center_comp_num_ids,
        "purpose": purpose,
        "tasks": tasks,
        "system_type": system_type,
        "system_scope": system_scope,
        "comparison_grid": comparison_grid,
        "limit": limit,
    }


def _partial_request_enrichment(
    *,
    ranking_targets: Any,
    target_constraints: Any,
    center_comp_num_ids: Any,
    purpose: Any,
    tasks: Any,
    system_type: Any,
    system_scope: Any,
    comparison_grid: Any,
    limit: Any,
) -> tuple[dict[str, Any], list[dict[str, str]]]:
    """Resolve every independent field that is still safe after one error."""
    catalogs = load_runtime_catalogs()
    enriched: dict[str, Any] = {
        "ranking_targets": [],
        "target_constraints": [],
        "center_comp_num_ids": [],
        "center_compounds": [],
        "purpose": purpose,
        "tasks": [tasks] if isinstance(tasks, str) and tasks.strip() else [],
        "system_type": system_type,
        "system_scope": system_scope,
        "comparison_grid": comparison_grid,
        "limit": limit,
    }
    issues: list[dict[str, str]] = []

    def raw_entries(value: Any, field: str) -> list[str]:
        try:
            return _flat_strings(value, field)
        except RequestValidationError as exc:
            issues.append(exc.as_issue())
            return []

    for index, raw in enumerate(raw_entries(ranking_targets, "ranking_targets")):
        try:
            enriched["ranking_targets"].append(
                _parse_targets(raw, catalogs)[0].as_dict()
            )
        except RequestValidationError as exc:
            issues.append(exc.as_issue(field=f"ranking_targets[{index}]"))

    for index, raw in enumerate(
        raw_entries(target_constraints, "target_constraints")
    ):
        try:
            enriched["target_constraints"].append(
                _parse_constraints(raw, catalogs)[0].as_dict()
            )
        except RequestValidationError as exc:
            issues.append(
                exc.as_issue(field=f"target_constraints[{index}]")
            )

    compounds: list[CompoundRecord] = []
    for index, raw in enumerate(
        raw_entries(center_comp_num_ids, "center_comp_num_ids")
    ):
        try:
            compounds.append(_resolve_compound(raw, catalogs))
        except RequestValidationError as exc:
            issues.append(
                exc.as_issue(field=f"center_comp_num_ids[{index}]")
            )
    enriched["center_comp_num_ids"] = [
        row.comp_num_id for row in compounds
    ]
    enriched["center_compounds"] = [row.as_dict() for row in compounds]

    if not isinstance(purpose, str) or not purpose.strip():
        issues.append(
            RequestValidationError(
                "MISSING_REQUIRED_INPUT",
                "purpose must be a non-empty chemistry goal.",
                field="purpose",
            ).as_issue()
        )
    if not isinstance(tasks, str) or not tasks.strip():
        issues.append(
            RequestValidationError(
                "MISSING_REQUIRED_INPUT",
                "tasks must be one non-empty flat instruction string.",
                field="tasks",
            ).as_issue()
        )

    try:
        parse_request(
            ranking_targets=ranking_targets,
            target_constraints=target_constraints,
            center_comp_num_ids=center_comp_num_ids,
            purpose=purpose,
            tasks=tasks,
            system_type=system_type,
            system_scope=system_scope,
            comparison_grid=comparison_grid,
            limit=limit,
        )
    except RequestValidationError as exc:
        issues.append(exc.as_issue())

    unique_issues: list[dict[str, str]] = []
    # Per-entry parsing runs before the complete request parser, so retain its
    # more specific indexed field and suppress the same diagnosis later when
    # the complete parser reports the enclosing field.
    seen: set[tuple[str, str]] = set()
    for issue in issues:
        key = (issue["code"], issue["message"])
        if key not in seen:
            unique_issues.append(issue)
            seen.add(key)
    return enriched, unique_issues


def _confirmation_material(
    request: NormalizedRequest,
) -> tuple[str, dict[str, Any], str]:
    # Lazy import keeps the immutable request models independent of runtime I/O.
    from ..runtime.storage import database_fingerprint

    fingerprint = database_fingerprint()
    material = {
        "database_fingerprint_sha256": fingerprint["fingerprint_sha256"],
        "enriched_tool_call": request.as_dict(),
    }
    encoded = json.dumps(
        material,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    digest = hashlib.sha256(encoded).hexdigest()
    return f"{_CONFIRMATION_TOKEN_PREFIX}{digest}", fingerprint, digest


def review_request(
    *,
    ranking_targets: str | list[str],
    target_constraints: str | list[str],
    center_comp_num_ids: str | list[str],
    purpose: str,
    tasks: str,
    system_type: str | None = None,
    system_scope: str = "declared",
    comparison_grid: str | list[str] = "auto",
    limit: int = 20,
    confirmation_token: str | None = None,
) -> RequestReviewOutcome:
    """Hard-parse a GLOB-only call and require an exact second-call review."""
    original = _original_tool_call(
        ranking_targets=ranking_targets,
        target_constraints=target_constraints,
        center_comp_num_ids=center_comp_num_ids,
        purpose=purpose,
        tasks=tasks,
        system_type=system_type,
        system_scope=system_scope,
        comparison_grid=comparison_grid,
        limit=limit,
    )
    try:
        request = parse_request(**original)
    except RequestValidationError:
        partial, issues = _partial_request_enrichment(**original)
        return RequestReviewOutcome(
            review={
                "status": "correction_required",
                "executed": False,
                "original_tool_call": original,
                "enriched_tool_call": partial,
                "issues": issues,
                "confirmation": {
                    "required": True,
                    "token": None,
                    "instruction": (
                        "Correct the listed flat inputs. Submit only typed "
                        "GLOB IDs in identifier positions; the tool will "
                        "hard-parse all names, units, values, tolerances, "
                        "operations, defaults, and structures again."
                    ),
                },
            },
            request=None,
            database_fingerprint=None,
        )

    expected_token, fingerprint, request_digest = _confirmation_material(
        request
    )
    token_matches = (
        isinstance(confirmation_token, str)
        and secrets.compare_digest(confirmation_token, expected_token)
    )
    issues: list[dict[str, str]] = []
    if confirmation_token is not None and not token_matches:
        issues.append(
            {
                "code": "STALE_OR_MISMATCHED_CONFIRMATION",
                "field": "confirmation_token",
                "message": (
                    "The confirmation token does not match this enriched "
                    "request and current registry/database/settings state."
                ),
            }
        )
    status = "confirmed" if token_matches else "confirmation_required"
    review = {
        "status": status,
        "executed": False,
        "original_tool_call": original,
        "enriched_tool_call": request.as_dict(),
        "enrichment_policy": {
            "agent_identifier_inputs": (
                "typed global IDs only: GLOBprop_N/GLOBvar_N/GLOBconstr_N "
                "plus GLOBcomp_N and GLOBphase_N bindings"
            ),
            "hard_parsed": [
                "registry names and chemistry identities",
                "canonical units and accepted input units",
                "submitted and canonical numeric values",
                "unit-conversion traces",
                "automatic or explicit tolerance windows",
                "ranking basis, direction, composition, and aggregate",
                "system scope, comparison grid, defaults, and bounds",
            ],
            "composition_coordinate_order": (
                "center compounds first in submitted order, then remaining "
                "system compounds in global-ID order; the last component is "
                "the mole-fraction closure component"
            ),
        },
        "fingerprints": {
            "request_sha256": request_digest,
            "database_sha256": fingerprint["fingerprint_sha256"],
            "translation_sha256": fingerprint["translation_sha256"],
        },
        "issues": issues,
        "confirmation": {
            "required": not token_matches,
            "token": expected_token,
            "instruction": (
                "Check that every resolved identity, chemistry name, unit "
                "conversion, canonical value, tolerance window, ranking "
                "operation, composition coordinate, and scope matches the "
                "question. If correct, repeat the same minimal GLOB-ID call "
                "with this confirmation_token. If not, correct the minimal "
                "call and omit the old token."
                if not token_matches
                else "Exact enriched request confirmed; screening may execute."
            ),
        },
    }
    return RequestReviewOutcome(
        review=review,
        request=request,
        database_fingerprint=fingerprint,
    )
