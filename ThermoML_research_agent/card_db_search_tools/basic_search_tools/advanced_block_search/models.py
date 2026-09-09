"""Strict private v1 request model for role-aware advanced block search."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from .catalogs import (
    CompoundRecord,
    QuantityResolution,
    RuntimeCatalogs,
)
from .errors import (
    exact_keys,
    fail,
    pointer_join,
    require_array,
    require_int,
    require_object,
    require_string,
)
from .expressions import (
    ExprType,
    boolean_type,
    expression_references,
    infer_expression,
    numeric_type,
)


SCHEMA = "block_search_adv/v1"
_ALIAS_RE = re.compile(r"^[a-z][a-z0-9_]{0,63}$")
_SYSTEM_TYPE_RE = re.compile(
    r"^(?:unary|binary|ternary|quaternary|(?:[5-9]|[1-9][0-9]+)-component)$"
)
_SYSTEM_SCOPES = {"declared", "subsystem", "either"}
_COMPOUND_SCOPES = {
    "any",
    "system",
    "solvent",
    "participant",
    "reactant",
    "product",
}
_CARDINALITIES = {"exactly_one", "all"}
_DIRECTIONS = {"asc", "desc"}
_NULL_ORDERS = {"first", "last"}
_MAX_SELECTORS_PER_ROLE = 16
_MAX_FIXED_FILTERS = 16
_MAX_COMPUTE = 32
_MAX_SELECT = 32
_MAX_ORDER = 16


@dataclass(frozen=True)
class CompoundSelector:
    alias: str
    record: CompoundRecord
    scope: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "as": self.alias,
            "identity": {"comp_num_id": self.record.comp_num_id},
            "scope": self.scope,
        }


@dataclass(frozen=True)
class CompoundQuery:
    all_of: tuple[CompoundSelector, ...]
    any_of: tuple[CompoundSelector, ...]
    none_of: tuple[CompoundSelector, ...]
    exact_system: bool
    system_size_min: int | None
    system_size_max: int | None
    system_types: tuple[str, ...]
    system_scope: str

    @property
    def selectors(self) -> tuple[CompoundSelector, ...]:
        return self.all_of + self.any_of + self.none_of

    @property
    def aliases(self) -> dict[str, CompoundSelector]:
        return {value.alias: value for value in self.selectors}

    def as_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "all_of": [value.as_dict() for value in self.all_of],
            "any_of": [value.as_dict() for value in self.any_of],
            "none_of": [value.as_dict() for value in self.none_of],
            "exact_system": self.exact_system,
            "system_scope": self.system_scope,
        }
        if self.system_size_min is not None or self.system_size_max is not None:
            payload["system_size"] = {}
            if self.system_size_min is not None:
                payload["system_size"]["min"] = self.system_size_min
            if self.system_size_max is not None:
                payload["system_size"]["max"] = self.system_size_max
        if self.system_types:
            payload["system_type"] = {"in": list(self.system_types)}
        return payload


@dataclass(frozen=True)
class OccurrenceSelector:
    alias: str
    resolution: QuantityResolution
    source_role: str
    component_ref: str | None
    phase_num_id: str | None
    phase_component_ref: str | None
    min_finite_values: int
    min_distinct_values: int
    cardinality: str
    condition: dict[str, Any] | None = None
    applies_to: str | None = None

    @property
    def expr_type(self) -> ExprType:
        semantics = self.resolution.row.semantics
        return numeric_type(
            scope="row",
            dimension=semantics.dimension,
            unit=semantics.canonical_unit,
            semantic_type=semantics.semantic_type,
        )

    def as_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "as": self.alias,
            "quantity": (
                {"global_id": self.resolution.input_value}
                if self.resolution.input_catalog_role is not None
                else {"key": self.resolution.input_value}
            ),
            "observations": {
                "min_finite_values": self.min_finite_values,
                "min_distinct_values": self.min_distinct_values,
            },
            "cardinality": self.cardinality,
        }
        if self.component_ref is not None:
            payload["component"] = {"compound_ref": self.component_ref}
        if self.phase_num_id is not None:
            payload["phase"] = {
                "phase_num_id": self.phase_num_id,
                "match": "exact",
            }
        if self.phase_component_ref is not None:
            payload["phase_component"] = {
                "compound_ref": self.phase_component_ref,
            }
        if self.condition is not None:
            payload["condition"] = self.condition
        if self.applies_to is not None:
            payload["applies_to"] = self.applies_to
        return payload


@dataclass(frozen=True)
class ComputeItem:
    alias: str
    expr: dict[str, Any]
    expr_type: ExprType


@dataclass(frozen=True)
class SelectItem:
    alias: str
    expr: dict[str, Any]
    expr_type: ExprType


@dataclass(frozen=True)
class OrderItem:
    expr: dict[str, Any]
    direction: str
    nulls: str


@dataclass(frozen=True)
class MinimumCommonPoints:
    aliases: tuple[str, ...]
    count: int


@dataclass(frozen=True)
class LiteratureQuery:
    dois: tuple[str, ...]
    lit_num_ids: tuple[str, ...]
    year_min: int | None
    year_max: int | None
    first_author: str | None
    journal: str | None

    def as_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {}
        if self.dois:
            payload["doi_in"] = list(self.dois)
        if self.lit_num_ids:
            payload["lit_num_id_in"] = list(self.lit_num_ids)
        if self.year_min is not None or self.year_max is not None:
            payload["year"] = {}
            if self.year_min is not None:
                payload["year"]["min"] = self.year_min
            if self.year_max is not None:
                payload["year"]["max"] = self.year_max
        if self.first_author is not None:
            payload["first_author"] = self.first_author
        if self.journal is not None:
            payload["journal"] = self.journal
        return payload


@dataclass(frozen=True)
class PhaseQuery:
    all_of: tuple[str, ...]
    any_of: tuple[str, ...]
    none_of: tuple[str, ...]

    def as_dict(self) -> dict[str, Any]:
        return {
            "all_of": list(self.all_of),
            "any_of": list(self.any_of),
            "none_of": list(self.none_of),
        }


@dataclass(frozen=True)
class NormalizedRequest:
    schema: str
    compounds: CompoundQuery
    parameters: tuple[OccurrenceSelector, ...]
    targets: tuple[OccurrenceSelector, ...]
    literature: LiteratureQuery
    phases: PhaseQuery
    filtering_aliases: tuple[str, ...]
    constraints: tuple[OccurrenceSelector, ...]
    inline_states: tuple[OccurrenceSelector, ...]
    where: dict[str, Any] | None
    minimum_common_points: MinimumCommonPoints | None
    compute: tuple[ComputeItem, ...]
    select: tuple[SelectItem, ...]
    having: dict[str, Any] | None
    order_by: tuple[OrderItem, ...]
    limit: int
    explanation: str
    row_types: dict[str, ExprType]
    selected_types: dict[str, ExprType]

    @property
    def row_selectors(self) -> tuple[OccurrenceSelector, ...]:
        return self.parameters + self.targets

    @property
    def fixed_selectors(self) -> tuple[OccurrenceSelector, ...]:
        return self.constraints + self.inline_states

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema": self.schema,
            "compound_list": self.compounds.as_dict(),
            "para_identity": [value.as_dict() for value in self.parameters],
            "target_identity": [value.as_dict() for value in self.targets],
            "literature": self.literature.as_dict(),
            "phase": self.phases.as_dict(),
            "filtering_identity": [
                {"ref": value} for value in self.filtering_aliases
            ],
            "constraint_filter": [
                value.as_dict() for value in self.constraints
            ],
            "inline_state_filter": [
                value.as_dict() for value in self.inline_states
            ],
            "where": self.where,
            "minimum_common_points": (
                {
                    "of": list(self.minimum_common_points.aliases),
                    "count": self.minimum_common_points.count,
                }
                if self.minimum_common_points is not None
                else None
            ),
            "compute": [
                {"as": value.alias, "expr": value.expr}
                for value in self.compute
            ],
            "select": [
                {"as": value.alias, "expr": value.expr}
                for value in self.select
            ],
            "having": self.having,
            "order_by": [
                {
                    "expr": value.expr,
                    "direction": value.direction,
                    "nulls": value.nulls,
                }
                for value in self.order_by
            ],
            "limit": self.limit,
            "explanation": self.explanation,
        }


def _alias(value: Any, pointer: str) -> str:
    alias = require_string(value, pointer)
    if not _ALIAS_RE.fullmatch(alias):
        fail(
            "INVALID_ALIAS",
            "Aliases must match [a-z][a-z0-9_]{0,63}.",
            pointer,
            details={"received": alias},
        )
    if alias == "value":
        fail("INVALID_ALIAS", "The alias 'value' is reserved.", pointer)
    return alias


def _unique_strings(
    value: Any,
    pointer: str,
    *,
    allow_empty: bool = True,
) -> tuple[str, ...]:
    values = require_array(value, pointer)
    if not allow_empty and not values:
        fail("INVALID_REQUEST", "Expected at least one item.", pointer)
    parsed = tuple(
        require_string(item, pointer_join(pointer, index))
        for index, item in enumerate(values)
    )
    if len(set(parsed)) != len(parsed):
        fail("INVALID_REQUEST", "Duplicate values are not permitted.", pointer)
    return parsed


def _normalize_compound_set(
    value: Any,
    pointer: str,
    catalogs: RuntimeCatalogs,
    aliases_seen: set[str],
) -> tuple[CompoundSelector, ...]:
    raw = require_array(value, pointer)
    selectors: list[CompoundSelector] = []
    for index, item in enumerate(raw):
        item_pointer = pointer_join(pointer, index)
        obj = require_object(item, item_pointer)
        exact_keys(
            obj,
            item_pointer,
            allowed={"as", "identity", "scope"},
            required={"as", "identity"},
        )
        alias = _alias(obj["as"], f"{item_pointer}/as")
        if alias in aliases_seen:
            fail(
                "DUPLICATE_ALIAS",
                f"Alias {alias!r} is declared more than once.",
                f"{item_pointer}/as",
            )
        aliases_seen.add(alias)
        scope = obj.get("scope", "system")
        scope = require_string(scope, f"{item_pointer}/scope")
        if scope not in _COMPOUND_SCOPES:
            fail(
                "INVALID_REQUEST",
                f"Unsupported compound scope {scope!r}.",
                f"{item_pointer}/scope",
                details={"allowed": sorted(_COMPOUND_SCOPES)},
            )
        record = catalogs.resolve_compound(
            obj["identity"],
            f"{item_pointer}/identity",
        )
        selectors.append(CompoundSelector(alias, record, scope))
    return tuple(selectors)


def _normalize_compounds(
    value: Any,
    catalogs: RuntimeCatalogs,
    aliases_seen: set[str],
) -> CompoundQuery:
    if value is None:
        value = {}
    obj = require_object(value, "/compound_list")
    exact_keys(
        obj,
        "/compound_list",
        allowed={
            "all_of",
            "any_of",
            "none_of",
            "exact_system",
            "system_size",
            "system_type",
            "system_scope",
        },
    )
    all_of = _normalize_compound_set(
        obj.get("all_of", []),
        "/compound_list/all_of",
        catalogs,
        aliases_seen,
    )
    any_of = _normalize_compound_set(
        obj.get("any_of", []),
        "/compound_list/any_of",
        catalogs,
        aliases_seen,
    )
    none_of = _normalize_compound_set(
        obj.get("none_of", []),
        "/compound_list/none_of",
        catalogs,
        aliases_seen,
    )
    exact_system = obj.get("exact_system", False)
    if not isinstance(exact_system, bool):
        fail(
            "INVALID_REQUEST",
            "exact_system must be boolean.",
            "/compound_list/exact_system",
        )
    system_size_min: int | None = None
    system_size_max: int | None = None
    if "system_size" in obj:
        size = require_object(obj["system_size"], "/compound_list/system_size")
        exact_keys(
            size,
            "/compound_list/system_size",
            allowed={"min", "max"},
        )
        if "min" in size:
            system_size_min = require_int(
                size["min"],
                "/compound_list/system_size/min",
                minimum=1,
                maximum=100,
            )
        if "max" in size:
            system_size_max = require_int(
                size["max"],
                "/compound_list/system_size/max",
                minimum=1,
                maximum=100,
            )
        if (
            system_size_min is not None
            and system_size_max is not None
            and system_size_min > system_size_max
        ):
            fail(
                "INVALID_REQUEST",
                "system_size min cannot exceed max.",
                "/compound_list/system_size",
            )
    system_types: tuple[str, ...] = ()
    if "system_type" in obj:
        system_type = require_object(
            obj["system_type"],
            "/compound_list/system_type",
        )
        exact_keys(
            system_type,
            "/compound_list/system_type",
            allowed={"in"},
            required={"in"},
        )
        system_types = _unique_strings(
            system_type["in"],
            "/compound_list/system_type/in",
        )
        invalid = sorted(
            value for value in system_types
            if _SYSTEM_TYPE_RE.fullmatch(value) is None
        )
        if invalid:
            fail(
                "INVALID_REQUEST",
                "Use canonical system types such as unary, binary, or ternary.",
                "/compound_list/system_type/in",
                details={"invalid": invalid},
            )
    system_scope = obj.get("system_scope", "declared")
    if not isinstance(system_scope, str) or system_scope not in _SYSTEM_SCOPES:
        fail(
            "INVALID_REQUEST",
            "system_scope must be declared, subsystem, or either.",
            "/compound_list/system_scope",
        )
    if system_scope != "declared" and any(
        value.scope not in {"system", "any"}
        for value in all_of + any_of + none_of
    ):
        fail(
            "INVALID_REQUEST",
            "Subsystem targets only support compound scope system or any.",
            "/compound_list",
        )
    if exact_system:
        if not all_of:
            fail(
                "INVALID_REQUEST",
                "exact_system requires at least one all_of compound.",
                "/compound_list/exact_system",
            )
        if any(value.scope not in {"system", "any"} for value in all_of):
            fail(
                "INVALID_REQUEST",
                "exact_system all_of entries must use system or any scope.",
                "/compound_list/all_of",
            )
    return CompoundQuery(
        all_of,
        any_of,
        none_of,
        exact_system,
        system_size_min,
        system_size_max,
        system_types,
        system_scope,
    )


def _normalize_observations(
    value: Any,
    pointer: str,
) -> tuple[int, int]:
    if value is None:
        return 1, 1
    obj = require_object(value, pointer)
    exact_keys(
        obj,
        pointer,
        allowed={"min_finite_values", "min_distinct_values"},
    )
    finite = require_int(
        obj.get("min_finite_values", 1),
        f"{pointer}/min_finite_values",
        minimum=0,
        maximum=10_000_000,
    )
    distinct = require_int(
        obj.get("min_distinct_values", 1),
        f"{pointer}/min_distinct_values",
        minimum=0,
        maximum=10_000_000,
    )
    return finite, distinct


def _normalize_occurrences(
    value: Any,
    pointer: str,
    *,
    catalogs: RuntimeCatalogs,
    source_role: str,
    compound_aliases: set[str],
    aliases_seen: set[str],
    require_nonempty: bool,
    fixed: bool = False,
    target_aliases: set[str] | None = None,
) -> tuple[OccurrenceSelector, ...]:
    raw = require_array(value, pointer)
    maximum = _MAX_FIXED_FILTERS if fixed else _MAX_SELECTORS_PER_ROLE
    if len(raw) > maximum:
        fail(
            "INVALID_REQUEST",
            f"At most {maximum} selectors are permitted here.",
            pointer,
        )
    if require_nonempty and not raw:
        fail("INVALID_REQUEST", "At least one target is required.", pointer)
    selectors: list[OccurrenceSelector] = []
    for index, item in enumerate(raw):
        item_pointer = pointer_join(pointer, index)
        obj = require_object(item, item_pointer)
        allowed = {
            "as",
            "quantity",
            "component",
            "phase",
            "phase_component",
            "observations",
            "cardinality",
        }
        if fixed:
            allowed |= {"condition"}
        if source_role == "inline_state":
            allowed |= {"applies_to"}
        exact_keys(
            obj,
            item_pointer,
            allowed=allowed,
            required=(
                {"as", "quantity", "condition"}
                if fixed
                else {"as", "quantity"}
            ),
        )
        alias = _alias(obj["as"], f"{item_pointer}/as")
        if alias in aliases_seen:
            fail(
                "DUPLICATE_ALIAS",
                f"Alias {alias!r} is declared more than once.",
                f"{item_pointer}/as",
            )
        aliases_seen.add(alias)
        resolution = catalogs.translation.resolve(
            obj["quantity"],
            f"{item_pointer}/quantity",
        )
        if source_role != "inline_state":
            role_id = resolution.row.global_id_for_role(source_role)
            if role_id is None:
                fail(
                    "ROLE_UNAVAILABLE",
                    (
                        f"Quantity {resolution.row.quantity_key!r} has no "
                        f"{source_role} representation in the global catalog."
                    ),
                    f"{item_pointer}/quantity",
                )
        component_ref: str | None = None
        if "component" in obj:
            component = require_object(
                obj["component"],
                f"{item_pointer}/component",
            )
            exact_keys(
                component,
                f"{item_pointer}/component",
                allowed={"compound_ref"},
                required={"compound_ref"},
            )
            component_ref = require_string(
                component["compound_ref"],
                f"{item_pointer}/component/compound_ref",
            )
            if component_ref not in compound_aliases:
                fail(
                    "UNKNOWN_COMPOUND_REFERENCE",
                    f"Unknown compound alias {component_ref!r}.",
                    f"{item_pointer}/component/compound_ref",
                )
            if not resolution.row.component_linked:
                fail(
                    "COMPONENT_QUALIFIER_NOT_ALLOWED",
                    "This quantity is not component-linked and does not "
                    "accept a COMPONENT qualifier.",
                    f"{item_pointer}/component",
                )
        phase_num_id: str | None = None
        if "phase" in obj:
            phase = require_object(obj["phase"], f"{item_pointer}/phase")
            exact_keys(
                phase,
                f"{item_pointer}/phase",
                allowed={"phase_num_id", "match"},
                required={"phase_num_id"},
            )
            match = phase.get("match", "exact")
            if match != "exact":
                fail(
                    "INVALID_REQUEST",
                    "Only exact phase matching is supported.",
                    f"{item_pointer}/phase/match",
                )
            phase_num_id = catalogs.require_phase(
                phase["phase_num_id"],
                f"{item_pointer}/phase/phase_num_id",
            ).phase_num_id
        phase_component_ref: str | None = None
        if "phase_component" in obj:
            phase_component = require_object(
                obj["phase_component"],
                f"{item_pointer}/phase_component",
            )
            exact_keys(
                phase_component,
                f"{item_pointer}/phase_component",
                allowed={"compound_ref"},
                required={"compound_ref"},
            )
            phase_component_ref = require_string(
                phase_component["compound_ref"],
                f"{item_pointer}/phase_component/compound_ref",
            )
            if phase_component_ref not in compound_aliases:
                fail(
                    "UNKNOWN_COMPOUND_REFERENCE",
                    f"Unknown compound alias {phase_component_ref!r}.",
                    f"{item_pointer}/phase_component/compound_ref",
                )
        min_finite, min_distinct = _normalize_observations(
            obj.get("observations"),
            f"{item_pointer}/observations",
        )
        cardinality = obj.get("cardinality", "exactly_one")
        cardinality = require_string(
            cardinality,
            f"{item_pointer}/cardinality",
        )
        if cardinality not in _CARDINALITIES:
            fail(
                "INVALID_REQUEST",
                f"Unsupported cardinality {cardinality!r}.",
                f"{item_pointer}/cardinality",
                details={"allowed": sorted(_CARDINALITIES)},
            )
        if (
            resolution.row.component_linked
            and component_ref is None
            and cardinality == "exactly_one"
        ):
            fail(
                "COMPONENT_QUALIFIER_REQUIRED",
                (
                    "This component-linked quantity requires component or "
                    "cardinality='all'."
                ),
                item_pointer,
            )
        condition = obj.get("condition")
        applies_to: str | None = None
        if source_role == "inline_state":
            if "applies_to" not in obj:
                fail(
                    "INLINE_TARGET_REQUIRED",
                    "Inline state requires an explicit target alias.",
                    f"{item_pointer}/applies_to",
                )
            applies_to = require_string(
                obj["applies_to"],
                f"{item_pointer}/applies_to",
            )
            if target_aliases is None or applies_to not in target_aliases:
                fail(
                    "UNKNOWN_BINDING_REFERENCE",
                    "applies_to must name a declared target alias.",
                    f"{item_pointer}/applies_to",
                )
        selector = OccurrenceSelector(
            alias,
            resolution,
            source_role,
            component_ref,
            phase_num_id,
            phase_component_ref,
            min_finite,
            min_distinct,
            cardinality,
            condition,
            applies_to,
        )
        if condition is not None:
            semantics = resolution.row.semantics
            value_type = numeric_type(
                scope="block",
                dimension=semantics.dimension,
                unit=semantics.canonical_unit,
                semantic_type=semantics.semantic_type,
            )
            inferred = infer_expression(
                condition,
                {"value": value_type},
                f"{item_pointer}/condition",
                allow_aggregates=False,
            )
            if not inferred.boolean:
                fail(
                    "SEMANTIC_TYPE_MISMATCH",
                    "Fixed filter condition must be boolean.",
                    f"{item_pointer}/condition",
                )
        selectors.append(selector)
    return tuple(selectors)


def _normalize_literature(
    value: Any,
    catalogs: RuntimeCatalogs,
) -> LiteratureQuery:
    if value is None:
        value = {}
    obj = require_object(value, "/literature")
    exact_keys(
        obj,
        "/literature",
        allowed={
            "doi",
            "doi_in",
            "lit_num_id",
            "lit_num_id_in",
            "year",
            "first_author",
            "journal",
        },
    )
    dois: list[str] = []
    if "doi" in obj:
        dois.append(require_string(obj["doi"], "/literature/doi"))
    if "doi_in" in obj:
        dois.extend(_unique_strings(obj["doi_in"], "/literature/doi_in"))
    lit_ids: list[str] = []
    if "lit_num_id" in obj:
        lit_ids.append(
            catalogs.require_literature_id(
                obj["lit_num_id"],
                "/literature/lit_num_id",
            ).lit_num_id
        )
    if "lit_num_id_in" in obj:
        for index, value_item in enumerate(
            require_array(obj["lit_num_id_in"], "/literature/lit_num_id_in")
        ):
            lit_ids.append(
                catalogs.require_literature_id(
                    value_item,
                    pointer_join("/literature/lit_num_id_in", index),
                ).lit_num_id
            )
    unknown_dois = sorted(
        set(dois) - set(catalogs.references_by_doi)
    )
    if unknown_dois:
        fail(
            "UNKNOWN_LITERATURE",
            "One or more DOI values are absent from the reference catalog.",
            "/literature",
            details={"unknown_dois": unknown_dois},
        )
    if len(set(dois)) != len(dois) or len(set(lit_ids)) != len(lit_ids):
        fail(
            "INVALID_REQUEST",
            "Duplicate literature identifiers are not permitted.",
            "/literature",
        )
    year_min: int | None = None
    year_max: int | None = None
    if "year" in obj:
        year = require_object(obj["year"], "/literature/year")
        exact_keys(year, "/literature/year", allowed={"min", "max"})
        if "min" in year:
            year_min = require_int(
                year["min"],
                "/literature/year/min",
                minimum=1800,
                maximum=3000,
            )
        if "max" in year:
            year_max = require_int(
                year["max"],
                "/literature/year/max",
                minimum=1800,
                maximum=3000,
            )
        if (
            year_min is not None
            and year_max is not None
            and year_min > year_max
        ):
            fail(
                "INVALID_REQUEST",
                "Literature year min cannot exceed max.",
                "/literature/year",
            )
    first_author = (
        require_string(obj["first_author"], "/literature/first_author")
        if "first_author" in obj
        else None
    )
    journal = (
        require_string(obj["journal"], "/literature/journal")
        if "journal" in obj
        else None
    )
    return LiteratureQuery(
        tuple(sorted(dois)),
        tuple(sorted(lit_ids)),
        year_min,
        year_max,
        first_author,
        journal,
    )


def _normalize_phases(
    value: Any,
    catalogs: RuntimeCatalogs,
) -> PhaseQuery:
    if value is None:
        value = {}
    obj = require_object(value, "/phase")
    exact_keys(
        obj,
        "/phase",
        allowed={"all_of", "any_of", "none_of"},
    )

    def parse(field: str) -> tuple[str, ...]:
        raw = require_array(obj.get(field, []), f"/phase/{field}")
        values = tuple(
            catalogs.require_phase(
                item,
                pointer_join(f"/phase/{field}", index),
            ).phase_num_id
            for index, item in enumerate(raw)
        )
        if len(set(values)) != len(values):
            fail(
                "INVALID_REQUEST",
                "Duplicate phase IDs are not permitted.",
                f"/phase/{field}",
            )
        return values

    return PhaseQuery(parse("all_of"), parse("any_of"), parse("none_of"))


def _normalize_filtering_aliases(
    value: Any,
    row_aliases: set[str],
) -> tuple[str, ...]:
    if value is None:
        return tuple(sorted(row_aliases))
    raw = require_array(value, "/filtering_identity")
    aliases: list[str] = []
    for index, item in enumerate(raw):
        pointer = pointer_join("/filtering_identity", index)
        obj = require_object(item, pointer)
        exact_keys(obj, pointer, allowed={"ref"}, required={"ref"})
        alias = require_string(obj["ref"], f"{pointer}/ref")
        if alias not in row_aliases:
            fail(
                "UNKNOWN_BINDING_REFERENCE",
                "Filtering identity must reference a declared parameter or target.",
                f"{pointer}/ref",
            )
        aliases.append(alias)
    if len(set(aliases)) != len(aliases):
        fail(
            "INVALID_REQUEST",
            "Duplicate filtering identities are not permitted.",
            "/filtering_identity",
        )
    return tuple(aliases)


def _topological_compute(
    value: Any,
    base_types: dict[str, ExprType],
    aliases_seen: set[str],
) -> tuple[tuple[ComputeItem, ...], dict[str, ExprType]]:
    raw = require_array(value, "/compute")
    if len(raw) > _MAX_COMPUTE:
        fail(
            "INVALID_REQUEST",
            f"At most {_MAX_COMPUTE} computed columns are permitted.",
            "/compute",
        )
    definitions: dict[str, tuple[dict[str, Any], str]] = {}
    for index, item in enumerate(raw):
        pointer = pointer_join("/compute", index)
        obj = require_object(item, pointer)
        exact_keys(
            obj,
            pointer,
            allowed={"as", "expr"},
            required={"as", "expr"},
        )
        alias = _alias(obj["as"], f"{pointer}/as")
        if alias in aliases_seen or alias in definitions:
            fail(
                "DUPLICATE_ALIAS",
                f"Alias {alias!r} is declared more than once.",
                f"{pointer}/as",
            )
        definitions[alias] = (require_object(obj["expr"], f"{pointer}/expr"), pointer)
    remaining = dict(definitions)
    types = dict(base_types)
    ordered: list[ComputeItem] = []
    while remaining:
        progressed = False
        for alias in list(remaining):
            expr, pointer = remaining[alias]
            refs = expression_references(expr)
            unknown = refs - set(types) - set(remaining)
            if unknown:
                fail(
                    "UNKNOWN_BINDING_REFERENCE",
                    f"Unknown computed-expression references: {sorted(unknown)}.",
                    f"{pointer}/expr",
                )
            if refs & set(remaining):
                continue
            inferred = infer_expression(
                expr,
                types,
                f"{pointer}/expr",
                allow_aggregates=False,
            )
            if inferred.scope != "row":
                fail(
                    "NONROW_COMPUTE",
                    "Computed columns must depend on row-valued bindings.",
                    f"{pointer}/expr",
                )
            types[alias] = inferred
            aliases_seen.add(alias)
            ordered.append(ComputeItem(alias, expr, inferred))
            del remaining[alias]
            progressed = True
        if not progressed:
            fail(
                "EXPRESSION_CYCLE",
                "Computed expressions contain a dependency cycle.",
                "/compute",
                details={"aliases": sorted(remaining)},
            )
    return tuple(ordered), types


def _normalize_select(
    value: Any,
    row_types: dict[str, ExprType],
    aliases_seen: set[str],
    targets: tuple[OccurrenceSelector, ...],
) -> tuple[tuple[SelectItem, ...], dict[str, ExprType]]:
    if value is None:
        value = [
            {
                "as": f"mean_{target.alias}",
                "expr": {
                    "aggregate": "mean",
                    "expr": {"ref": target.alias},
                },
            }
            for target in targets
        ]
    raw = require_array(value, "/select")
    if not raw:
        fail("INVALID_REQUEST", "At least one select item is required.", "/select")
    if len(raw) > _MAX_SELECT:
        fail(
            "INVALID_REQUEST",
            f"At most {_MAX_SELECT} select items are permitted.",
            "/select",
        )
    items: list[SelectItem] = []
    selected_types: dict[str, ExprType] = {}
    for index, item in enumerate(raw):
        pointer = pointer_join("/select", index)
        obj = require_object(item, pointer)
        exact_keys(
            obj,
            pointer,
            allowed={"as", "expr"},
            required={"as", "expr"},
        )
        alias = _alias(obj["as"], f"{pointer}/as")
        if alias in aliases_seen or alias in selected_types:
            fail(
                "DUPLICATE_ALIAS",
                f"Alias {alias!r} is declared more than once.",
                f"{pointer}/as",
            )
        expr = require_object(obj["expr"], f"{pointer}/expr")
        inferred = infer_expression(
            expr,
            row_types,
            f"{pointer}/expr",
            allow_aggregates=True,
        )
        if inferred.scope != "block":
            fail(
                "NONSCALAR_SELECT",
                "Select expressions must produce one scalar per binding match.",
                f"{pointer}/expr",
            )
        items.append(SelectItem(alias, expr, inferred))
        selected_types[alias] = inferred
    return tuple(items), selected_types


def _normalize_minimum_common(
    value: Any,
    row_types: dict[str, ExprType],
) -> MinimumCommonPoints | None:
    if value is None:
        return None
    obj = require_object(value, "/minimum_common_points")
    exact_keys(
        obj,
        "/minimum_common_points",
        allowed={"of", "count"},
        required={"of", "count"},
    )
    aliases = _unique_strings(
        obj["of"],
        "/minimum_common_points/of",
        allow_empty=False,
    )
    unknown = sorted(set(aliases) - set(row_types))
    if unknown:
        fail(
            "UNKNOWN_BINDING_REFERENCE",
            "minimum_common_points references unknown row aliases.",
            "/minimum_common_points/of",
            details={"unknown": unknown},
        )
    count = require_int(
        obj["count"],
        "/minimum_common_points/count",
        minimum=1,
        maximum=1_000_000,
    )
    return MinimumCommonPoints(aliases, count)


def _normalize_order(
    value: Any,
    selected_types: dict[str, ExprType],
) -> tuple[OrderItem, ...]:
    raw = require_array(value, "/order_by")
    if len(raw) > _MAX_ORDER:
        fail(
            "INVALID_REQUEST",
            f"At most {_MAX_ORDER} order expressions are permitted.",
            "/order_by",
        )
    items: list[OrderItem] = []
    for index, item in enumerate(raw):
        pointer = pointer_join("/order_by", index)
        obj = require_object(item, pointer)
        exact_keys(
            obj,
            pointer,
            allowed={"expr", "direction", "nulls"},
            required={"expr"},
        )
        expr = require_object(obj["expr"], f"{pointer}/expr")
        inferred = infer_expression(
            expr,
            selected_types,
            f"{pointer}/expr",
            allow_aggregates=False,
        )
        if inferred.scope != "block":
            fail(
                "INVALID_REQUEST",
                "Order expressions must reference selected scalar aliases.",
                f"{pointer}/expr",
            )
        direction = require_string(
            obj.get("direction", "asc"),
            f"{pointer}/direction",
        )
        if direction not in _DIRECTIONS:
            fail(
                "INVALID_REQUEST",
                f"Unsupported order direction {direction!r}.",
                f"{pointer}/direction",
            )
        nulls = require_string(
            obj.get("nulls", "last"),
            f"{pointer}/nulls",
        )
        if nulls not in _NULL_ORDERS:
            fail(
                "INVALID_REQUEST",
                f"Unsupported null ordering {nulls!r}.",
                f"{pointer}/nulls",
            )
        items.append(OrderItem(expr, direction, nulls))
    return tuple(items)


def normalize_request(
    *,
    catalogs: RuntimeCatalogs,
    compound_list: Any,
    para_identity: Any,
    target_identity: Any,
    literature: Any,
    phase: Any,
    filtering_identity: Any,
    constraint_filter: Any,
    inline_state_filter: Any,
    where: Any,
    minimum_common_points: Any,
    compute: Any,
    select: Any,
    having: Any,
    order_by: Any,
    limit: Any,
    explanation: Any,
    schema: Any,
) -> NormalizedRequest:
    schema_value = require_string(schema, "/schema")
    if schema_value != SCHEMA:
        fail(
            "UNSUPPORTED_SCHEMA",
            f"Expected schema {SCHEMA!r}.",
            "/schema",
            details={"received": schema_value},
        )
    explanation_value = require_string(explanation, "/explanation")
    if len(explanation_value) > 500 or "\n" in explanation_value:
        fail(
            "INVALID_REQUEST",
            "explanation must be one line of at most 500 characters.",
            "/explanation",
        )
    # The caller-facing contract asks for one sentence. Enforce the parts that
    # are unambiguous in machine validation (one non-empty line and a bounded
    # length) without misclassifying decimal points or chemical abbreviations
    # such as “298.15 K” and “e.g.” as extra sentences.
    limit_value = require_int(limit, "/limit", minimum=1, maximum=500)

    aliases_seen: set[str] = set()
    compounds = _normalize_compounds(
        compound_list,
        catalogs,
        aliases_seen,
    )
    compound_aliases = set(compounds.aliases)
    parameters = _normalize_occurrences(
        para_identity if para_identity is not None else [],
        "/para_identity",
        catalogs=catalogs,
        source_role="variable",
        compound_aliases=compound_aliases,
        aliases_seen=aliases_seen,
        require_nonempty=False,
    )
    targets = _normalize_occurrences(
        target_identity if target_identity is not None else [],
        "/target_identity",
        catalogs=catalogs,
        source_role="property",
        compound_aliases=compound_aliases,
        aliases_seen=aliases_seen,
        require_nonempty=True,
    )
    row_selectors = parameters + targets
    row_aliases = {value.alias for value in row_selectors}
    filtering_aliases = _normalize_filtering_aliases(
        filtering_identity,
        row_aliases,
    )
    constraints = _normalize_occurrences(
        constraint_filter if constraint_filter is not None else [],
        "/constraint_filter",
        catalogs=catalogs,
        source_role="constraint",
        compound_aliases=compound_aliases,
        aliases_seen=aliases_seen,
        require_nonempty=False,
        fixed=True,
    )
    inline_states = _normalize_occurrences(
        inline_state_filter if inline_state_filter is not None else [],
        "/inline_state_filter",
        catalogs=catalogs,
        source_role="inline_state",
        compound_aliases=compound_aliases,
        aliases_seen=aliases_seen,
        require_nonempty=False,
        fixed=True,
        target_aliases={value.alias for value in targets},
    )
    literature_query = _normalize_literature(literature, catalogs)
    phases = _normalize_phases(phase, catalogs)

    base_types = {value.alias: value.expr_type for value in row_selectors}
    compute_items, row_types = _topological_compute(
        compute if compute is not None else [],
        base_types,
        aliases_seen,
    )
    where_obj: dict[str, Any] | None = None
    if where is not None:
        where_obj = require_object(where, "/where")
        inferred = infer_expression(
            where_obj,
            row_types,
            "/where",
            allow_aggregates=False,
        )
        if not inferred.boolean:
            fail(
                "SEMANTIC_TYPE_MISMATCH",
                "where must be a boolean row expression.",
                "/where",
            )
        base_refs = expression_references(where_obj) & row_aliases
        compute_by_alias = {item.alias: item.expr for item in compute_items}
        pending = list(expression_references(where_obj) & set(compute_by_alias))
        while pending:
            compute_alias = pending.pop()
            refs = expression_references(compute_by_alias[compute_alias])
            base_refs |= refs & row_aliases
            pending.extend(refs & set(compute_by_alias))
        disallowed = sorted(base_refs - set(filtering_aliases))
        if disallowed:
            fail(
                "FILTER_IDENTITY_REQUIRED",
                "where uses base aliases not declared in filtering_identity.",
                "/where",
                details={"aliases": disallowed},
            )
    minimum = _normalize_minimum_common(
        minimum_common_points,
        row_types,
    )
    select_items, selected_types = _normalize_select(
        select,
        row_types,
        aliases_seen,
        targets,
    )
    having_obj: dict[str, Any] | None = None
    if having is not None:
        having_obj = require_object(having, "/having")
        inferred = infer_expression(
            having_obj,
            {**row_types, **selected_types},
            "/having",
            allow_aggregates=True,
        )
        if not inferred.boolean or inferred.scope != "block":
            fail(
                "SEMANTIC_TYPE_MISMATCH",
                "having must be a block-level boolean over aggregates or "
                "selected aliases.",
                "/having",
            )
    order_items = _normalize_order(
        order_by if order_by is not None else [],
        selected_types,
    )
    return NormalizedRequest(
        schema_value,
        compounds,
        parameters,
        targets,
        literature_query,
        phases,
        filtering_aliases,
        constraints,
        inline_states,
        where_obj,
        minimum,
        compute_items,
        select_items,
        having_obj,
        order_items,
        limit_value,
        explanation_value,
        row_types,
        selected_types,
    )
