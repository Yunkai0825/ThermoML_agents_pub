"""Role-aware candidate binding and uncapped ThermoML row execution."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import re
import sqlite3
from collections import defaultdict
from dataclasses import dataclass
from functools import cmp_to_key
from typing import Any, Iterable, Mapping

from normalization_helpers.db_helpers import open_db

from .catalogs import (
    PCS_DB,
    PM_REGISTRY_DB,
    RXN_REGISTRY_DB,
    RuntimeCatalogs,
    load_runtime_catalogs,
    open_raw_db,
)
from .errors import AdvancedSearchError, fail
from .expressions import evaluate_block, evaluate_row
from .models import (
    CompoundSelector,
    NormalizedRequest,
    OccurrenceSelector,
    OrderItem,
    normalize_request,
)


RESULT_SCHEMA = "block_search_adv/result-v1"
ERROR_SCHEMA = "block_search_adv/error-v1"
_MAX_CANDIDATE_BLOCKS = 20_000
_MAX_BINDING_COMBINATIONS = 64
_MAX_MATERIALIZED_ROWS = 2_000_000
_BLOCK_ID_RE = re.compile(r"^(PROPblock|RXNblock)_([1-9][0-9]*)$")
_LOCAL_OCCURRENCE_RE = re.compile(r"^BLK(?:prop|var|constr)_([1-9][0-9]*)$")
_RAW_EXECUTION_CAPABILITY = object()


@dataclass(frozen=True)
class Candidate:
    doi: str
    block_id: str
    block_type: str
    lit_num_id: str
    BLKsubsys_id: str | None
    registry: dict[str, Any]


@dataclass
class ExactCandidate:
    candidate: Candidate
    card: dict[str, Any]
    block: dict[str, Any]
    index: dict[str, Any]
    compound_matches: dict[str, dict[str, Any]]
    phase_ids: tuple[str, ...]
    subsystem: dict[str, Any] | None


@dataclass
class BindingCombination:
    bindings: dict[str, dict[str, Any]]
    statistics: dict[str, dict[str, Any]]
    fixed_filter_evidence: list[dict[str, Any]]

    @property
    def key(self) -> str:
        return "|".join(
            f"{alias}={self.bindings[alias]['occurrence_key']}"
            for alias in sorted(self.bindings)
        )


@dataclass
class PreparedSearch:
    """Validated search plan with exact card bindings but no raw-row reads."""

    catalogs: RuntimeCatalogs
    request: NormalizedRequest
    diagnostics: dict[str, Any]
    exact_candidates: list[ExactCandidate]
    combinations_by_target: dict[
        tuple[str, str, str | None], list[BindingCombination]
    ]

def _json_exists_clause(column: str, json_path: str) -> str:
    return (
        "EXISTS (SELECT 1 FROM json_each(COALESCE("
        f"{column}, '[]')) AS item "
        f"WHERE json_extract(item.value, '{json_path}') = ?)"
    )


def _candidate_sql(
    request: NormalizedRequest,
    *,
    registry_kind: str,
) -> tuple[str, list[Any]]:
    clauses: list[str] = []
    params: list[Any] = []
    literature = request.literature
    if literature.dois:
        placeholders = ",".join("?" for _ in literature.dois)
        clauses.append(f"doi IN ({placeholders})")
        params.extend(literature.dois)
    if literature.lit_num_ids:
        placeholders = ",".join("?" for _ in literature.lit_num_ids)
        clauses.append(f"lit_num_id IN ({placeholders})")
        params.extend(literature.lit_num_ids)
    compounds = request.compounds
    if compounds.system_size_min is not None:
        clauses.append("n_components >= ?")
        params.append(compounds.system_size_min)
    if compounds.system_size_max is not None:
        clauses.append("n_components <= ?")
        params.append(compounds.system_size_max)
    if compounds.system_types:
        placeholders = ",".join("?" for _ in compounds.system_types)
        clauses.append(f"system_type IN ({placeholders})")
        params.extend(compounds.system_types)
    if compounds.exact_system:
        unique_ids = {
            value.record.comp_num_id for value in compounds.all_of
        }
        clauses.append("n_components = ?")
        params.append(len(unique_ids))

    # Registry predicates are only a coarse role-aware prune. Exact matching
    # always re-checks the card's embedded occurrence index.
    role_columns = {
        "variable": ("var_ids_ranges", "$.var_num_id"),
        "property": ("prop_ids_meas_ranges", "$.prop_num_id"),
        "constraint": ("constr_ids_values", "$.constr_num_id"),
    }
    role_selectors = (
        request.parameters + request.targets + request.constraints
    )
    seen_role_ids: set[tuple[str, str]] = set()
    for selector in role_selectors:
        global_id = selector.resolution.row.global_id_for_role(
            selector.source_role
        )
        if global_id is None:
            continue
        pair = (selector.source_role, global_id)
        if pair in seen_role_ids:
            continue
        seen_role_ids.add(pair)
        column, path = role_columns[selector.source_role]
        clauses.append(_json_exists_clause(column, path))
        params.append(global_id)

    # Positive component filters can be pushed down without interpreting
    # phase, participant sign, or solvent semantics.
    for compound in compounds.all_of:
        if compound.scope == "solvent" and registry_kind == "property":
            clauses.append(
                _json_exists_clause(
                    "solvent_comp_ids_smiles",
                    "$.comp_num_id",
                )
            )
            params.append(compound.record.comp_num_id)
        elif compound.scope in {
            "any",
            "system",
            "participant",
            "reactant",
            "product",
        }:
            clauses.append(
                _json_exists_clause("comp_ids_smiles", "$.comp_num_id")
            )
            params.append(compound.record.comp_num_id)

    sql = "SELECT * FROM block_registry"
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " LIMIT ?"
    params.append(_MAX_CANDIDATE_BLOCKS + 1)
    return sql, params


def _subsystem_candidate_sql(
    request: NormalizedRequest,
) -> tuple[str, list[Any]]:
    """Build a normalized child-table query for exact subsystem targets."""
    clauses = ["bs.search_eligible = 1"]
    params: list[Any] = []
    literature = request.literature
    if literature.dois:
        placeholders = ",".join("?" for _ in literature.dois)
        clauses.append(f"br.doi IN ({placeholders})")
        params.extend(literature.dois)
    if literature.lit_num_ids:
        placeholders = ",".join("?" for _ in literature.lit_num_ids)
        clauses.append(f"br.lit_num_id IN ({placeholders})")
        params.extend(literature.lit_num_ids)

    compounds = request.compounds
    if compounds.system_size_min is not None:
        clauses.append("bs.n_retained_components >= ?")
        params.append(compounds.system_size_min)
    if compounds.system_size_max is not None:
        clauses.append("bs.n_retained_components <= ?")
        params.append(compounds.system_size_max)
    if compounds.system_types:
        placeholders = ",".join("?" for _ in compounds.system_types)
        clauses.append(f"bs.effective_system_type IN ({placeholders})")
        params.extend(compounds.system_types)
    if compounds.exact_system:
        clauses.append("bs.n_retained_components = ?")
        params.append(len({item.record.comp_num_id for item in compounds.all_of}))

    for compound in compounds.all_of:
        clauses.append(
            "EXISTS (SELECT 1 FROM block_subsystem_compounds bsc "
            "WHERE bsc.doi = bs.doi AND bsc.block_number = bs.block_number "
            "AND bsc.BLKsubsys_id = bs.BLKsubsys_id "
            "AND bsc.component_role = 'retained' AND bsc.comp_num_id = ?)"
        )
        params.append(compound.record.comp_num_id)

    seen_property_ids: set[str] = set()
    for selector in request.targets:
        prop_num_id = selector.resolution.row.global_id_for_role("property")
        if prop_num_id is None or prop_num_id in seen_property_ids:
            continue
        seen_property_ids.add(prop_num_id)
        clauses.append(
            "EXISTS (SELECT 1 FROM block_subsystem_properties bsp "
            "WHERE bsp.doi = bs.doi AND bsp.block_number = bs.block_number "
            "AND bsp.BLKsubsys_id = bs.BLKsubsys_id "
            "AND bsp.prop_num_id = ? AND bsp.support_role = 'bulk_property' "
            "AND bsp.phase_compatible = 1)"
        )
        params.append(prop_num_id)

    sql = (
        "SELECT br.*, bs.BLKsubsys_id, bs.effective_system_type, "
        "bs.n_retained_components, bs.n_points AS subsystem_n_points, "
        "bs.path_class, bs.evidence_quality, bs.scope_json, "
        "bs.point_runs_json, bs.point_arity_counts_json, "
        "bs.condition_ranges_json, bs.quality_flags_json "
        "FROM block_registry br JOIN block_subsystems bs "
        "ON bs.doi = br.doi AND bs.block_number = br.block_number "
        "WHERE " + " AND ".join(clauses) + " LIMIT ?"
    )
    params.append(_MAX_CANDIDATE_BLOCKS + 1)
    return sql, params


def _discover_candidates(
    request: NormalizedRequest,
    diagnostics: dict[str, Any],
) -> list[Candidate]:
    candidates: list[Candidate] = []
    scope = request.compounds.system_scope
    sources: list[tuple[Any, str, bool]] = []
    if scope in {"declared", "either"}:
        sources.extend(((PM_REGISTRY_DB, "property", False), (RXN_REGISTRY_DB, "reaction", False)))
    if scope in {"subsystem", "either"}:
        sources.append((PM_REGISTRY_DB, "property", True))

    for path, kind, subsystem_target in sources:
        if not path.is_file():
            fail(
                "DATABASE_UNAVAILABLE",
                f"Block registry is unavailable at {path}.",
                "/",
            )
        sql, params = (
            _subsystem_candidate_sql(request)
            if subsystem_target
            else _candidate_sql(request, registry_kind=kind)
        )
        connection = open_db(str(path))
        try:
            rows = connection.execute(sql, params).fetchall()
        except sqlite3.Error as exc:
            fail(
                "DATABASE_ERROR",
                "Could not query a block registry with the required subsystem schema.",
                "/",
                details={"database": path.name, "error": str(exc)},
            )
        finally:
            connection.close()
        if len(rows) > _MAX_CANDIDATE_BLOCKS:
            fail(
                "SEARCH_TOO_BROAD",
                "Coarse search exceeds the advanced-search candidate budget.",
                "/",
                details={"max_candidate_blocks": _MAX_CANDIDATE_BLOCKS},
            )
        for row in rows:
            payload = dict(row)
            candidates.append(
                Candidate(
                    doi=payload["doi"],
                    block_id=payload["block_number"],
                    block_type=payload["block_type"],
                    lit_num_id=payload["lit_num_id"],
                    BLKsubsys_id=(payload.get("BLKsubsys_id") if subsystem_target else None),
                    registry=payload,
                )
            )
        if len(candidates) > _MAX_CANDIDATE_BLOCKS:
            fail(
                "SEARCH_TOO_BROAD",
                "Combined registries exceed the advanced-search candidate budget.",
                "/",
                details={"max_candidate_blocks": _MAX_CANDIDATE_BLOCKS},
            )

    unique: dict[tuple[str, str, str | None], Candidate] = {}
    for candidate in candidates:
        key = (candidate.doi, candidate.block_id, candidate.BLKsubsys_id)
        existing = unique.get(key)
        if existing is not None and existing.block_type != candidate.block_type:
            fail(
                "SOURCE_INDEX_MISMATCH",
                "Typed target identifiers collide across registry families.",
                "/",
                details={
                    "doi": candidate.doi,
                    "block_id": candidate.block_id,
                    "BLKsubsys_id": candidate.BLKsubsys_id,
                },
            )
        unique[key] = candidate
    diagnostics["registry_candidates"] = len(unique)
    return sorted(
        unique.values(),
        key=lambda item: (
            item.doi,
            0 if item.block_id.startswith("PROPblock_") else 1,
            int(item.block_id.rsplit("_", 1)[1]),
            item.BLKsubsys_id or "",
        ),
    )


def _literature_matches(
    candidate: Candidate,
    request: NormalizedRequest,
    catalogs: RuntimeCatalogs,
) -> bool:
    query = request.literature
    reference = catalogs.references_by_doi.get(candidate.doi)
    if reference is None:
        fail(
            "SOURCE_INDEX_MISMATCH",
            "Registry DOI is missing from the global reference catalog.",
            "/",
            details={"doi": candidate.doi},
        )
    if query.dois and candidate.doi not in query.dois:
        return False
    if query.lit_num_ids and reference.lit_num_id not in query.lit_num_ids:
        return False
    if query.year_min is not None and reference.year < query.year_min:
        return False
    if query.year_max is not None and reference.year > query.year_max:
        return False
    if (
        query.first_author is not None
        and reference.first_author.casefold() != query.first_author.casefold()
    ):
        return False
    if (
        query.journal is not None
        and reference.journal.casefold() != query.journal.casefold()
    ):
        return False
    return True


def _walk_phase_ids(value: Any) -> set[str]:
    found: set[str] = set()
    stack = [value]
    while stack:
        current = stack.pop()
        if isinstance(current, dict):
            phase = current.get("phase_num_id")
            if isinstance(phase, str):
                found.add(phase)
            stack.extend(current.values())
        elif isinstance(current, list):
            stack.extend(current)
    return found


def _compound_scope_ids(
    block: Mapping[str, Any],
) -> dict[str, set[str]]:
    system = {
        item.get("comp_num_id")
        for item in block.get("compounds", [])
        if isinstance(item, dict) and isinstance(item.get("comp_num_id"), str)
    }
    solvent = {
        item.get("comp_num_id")
        for item in block.get("solvents", [])
        if isinstance(item, dict) and isinstance(item.get("comp_num_id"), str)
    }
    reaction = block.get("reaction")
    participants = (
        reaction.get("participants", [])
        if isinstance(reaction, dict)
        else []
    )
    participant = {
        item.get("comp_num_id")
        for item in participants
        if isinstance(item, dict) and isinstance(item.get("comp_num_id"), str)
    }
    reactant = {
        item.get("comp_num_id")
        for item in participants
        if isinstance(item, dict)
        and isinstance(item.get("comp_num_id"), str)
        and isinstance(item.get("stoichiometric_coef"), (int, float))
        and item["stoichiometric_coef"] < 0
    }
    product = {
        item.get("comp_num_id")
        for item in participants
        if isinstance(item, dict)
        and isinstance(item.get("comp_num_id"), str)
        and isinstance(item.get("stoichiometric_coef"), (int, float))
        and item["stoichiometric_coef"] > 0
    }
    any_scope = system | solvent | participant
    return {
        "system": system,
        "solvent": solvent,
        "participant": participant,
        "reactant": reactant,
        "product": product,
        "any": any_scope,
    }


def _compound_matches(
    selector: CompoundSelector,
    scope_ids: Mapping[str, set[str]],
) -> bool:
    return selector.record.comp_num_id in scope_ids[selector.scope]


def _block_exact_filters(
    block: dict[str, Any],
    request: NormalizedRequest,
) -> tuple[bool, dict[str, dict[str, Any]], tuple[str, ...]]:
    scopes = _compound_scope_ids(block)
    compounds = request.compounds
    if any(not _compound_matches(value, scopes) for value in compounds.all_of):
        return False, {}, ()
    if compounds.any_of and not any(
        _compound_matches(value, scopes) for value in compounds.any_of
    ):
        return False, {}, ()
    if any(_compound_matches(value, scopes) for value in compounds.none_of):
        return False, {}, ()
    if compounds.exact_system:
        expected = {value.record.comp_num_id for value in compounds.all_of}
        if scopes["system"] != expected:
            return False, {}, ()
    n_components = len(scopes["system"])
    if (
        compounds.system_size_min is not None
        and n_components < compounds.system_size_min
    ):
        return False, {}, ()
    if (
        compounds.system_size_max is not None
        and n_components > compounds.system_size_max
    ):
        return False, {}, ()
    if (
        compounds.system_types
        and block.get("system_type") not in compounds.system_types
    ):
        return False, {}, ()

    phase_ids = _walk_phase_ids(block)
    phases = request.phases
    if any(value not in phase_ids for value in phases.all_of):
        return False, {}, ()
    if phases.any_of and not any(value in phase_ids for value in phases.any_of):
        return False, {}, ()
    if any(value in phase_ids for value in phases.none_of):
        return False, {}, ()

    matches: dict[str, dict[str, Any]] = {}
    for selector in compounds.selectors:
        if _compound_matches(selector, scopes):
            matches[selector.alias] = {
                "comp_num_id": selector.record.comp_num_id,
                "name": selector.record.common_name,
                "scope": selector.scope,
            }
    return True, matches, tuple(sorted(phase_ids))


def _phase_is_compatible(
    declaration: Mapping[str, Any],
    phase_field: str,
    scope_phase_num_id: Any,
) -> bool:
    phase = declaration.get(phase_field) or {}
    phase_num_id = phase.get("phase_num_id")
    return (
        scope_phase_num_id is None
        or phase_num_id is None
        or phase_num_id == scope_phase_num_id
    )


def _resolve_subsystem(
    card: Mapping[str, Any],
    candidate: Candidate,
) -> dict[str, Any]:
    manifests = (
        card.get("blocks_summary", {})
        .get("derived_indexes", {})
        .get("composition_subsystems")
    )
    if not isinstance(manifests, dict):
        fail(
            "SOURCE_INDEX_MISMATCH",
            "PCS card lacks the authoritative composition-subsystem index.",
            "/",
            details={"doi": candidate.doi},
        )
    entries = manifests.get(candidate.block_id)
    if not isinstance(entries, list):
        fail(
            "SOURCE_INDEX_MISMATCH",
            "PCS card lacks the candidate block's subsystem manifest.",
            "/",
            details={"doi": candidate.doi, "block_id": candidate.block_id},
        )
    matches = [
        item for item in entries
        if isinstance(item, dict)
        and item.get("BLKsubsys_id") == candidate.BLKsubsys_id
    ]
    if len(matches) != 1 or matches[0].get("search_eligible") is not True:
        fail(
            "SOURCE_INDEX_MISMATCH",
            "Registry subsystem does not resolve to one search-eligible PCS manifest.",
            "/",
            details={
                "doi": candidate.doi,
                "block_id": candidate.block_id,
                "BLKsubsys_id": candidate.BLKsubsys_id,
                "matches": len(matches),
            },
        )
    return matches[0]


def _project_subsystem_block(
    block: Mapping[str, Any],
    subsystem: Mapping[str, Any],
) -> dict[str, Any]:
    retained = {
        item["org_num"]
        for item in subsystem.get("retained_components", [])
        if isinstance(item, dict) and isinstance(item.get("org_num"), str)
    }
    if len(retained) != subsystem.get("n_retained_components"):
        fail(
            "SOURCE_INDEX_MISMATCH",
            "Subsystem retained-component count is inconsistent.",
            "/",
            details={"BLKsubsys_id": subsystem.get("BLKsubsys_id")},
        )
    support = subsystem.get("property_support")
    if not isinstance(support, list):
        fail(
            "SOURCE_INDEX_MISMATCH",
            "Subsystem property support is malformed.",
            "/",
        )
    supported_properties = {
        item.get("BLKprop_id")
        for item in support
        if isinstance(item, dict)
        and item.get("role") == "bulk_property"
        and item.get("phase_compatible") is True
        and isinstance(item.get("BLKprop_id"), str)
    }
    scope = subsystem.get("scope")
    if not isinstance(scope, dict):
        fail("SOURCE_INDEX_MISMATCH", "Subsystem scope is malformed.", "/")
    scope_phase_num_id = scope.get("phase_num_id")

    def declaration_allowed(item: Mapping[str, Any], phase_field: str) -> bool:
        component = item.get("component_org_num")
        return (
            (component is None or component in retained)
            and _phase_is_compatible(item, phase_field, scope_phase_num_id)
        )

    properties = [
        item for item in block.get("properties", [])
        if isinstance(item, dict) and item.get("BLKprop_id") in supported_properties
    ]
    variables = [
        item for item in block.get("variables", [])
        if isinstance(item, dict) and declaration_allowed(item, "phase")
    ]
    constraints = [
        item for item in block.get("constraints", [])
        if isinstance(item, dict) and declaration_allowed(item, "phase")
    ]
    projected = dict(block)
    projected.update(
        {
            "system_type": subsystem.get("effective_system_type"),
            "compounds": [
                item for item in block.get("compounds", [])
                if isinstance(item, dict) and item.get("org_num") in retained
            ],
            "solvents": [
                item for item in block.get("solvents", [])
                if isinstance(item, dict)
                and item.get("component_org_num") in retained
            ],
            "properties": properties,
            "variables": variables,
            "constraints": constraints,
        }
    )
    summary = dict(block.get("data_summary", {}))
    summary["n_points"] = subsystem.get("n_points")
    projected["data_summary"] = summary
    return projected


def _project_subsystem_index(
    index: Mapping[str, Any],
    projected_block: Mapping[str, Any],
) -> dict[str, Any]:
    allowed_by_role = {
        "property": {item["BLKprop_id"] for item in projected_block["properties"]},
        "variable": {item["BLKvar_id"] for item in projected_block["variables"]},
        "constraint": {item["BLKconstr_id"] for item in projected_block["constraints"]},
    }
    statistics = index.get("statistics")
    permutations = index.get("key_permutations")
    if not isinstance(statistics, list) or not isinstance(permutations, dict):
        fail("SOURCE_INDEX_MISMATCH", "Embedded identity index is malformed.", "/")
    filtered = [
        item for item in statistics
        if isinstance(item, dict)
        and item.get("source_role") in allowed_by_role
        and item.get("source_local_key") in allowed_by_role[item["source_role"]]
    ]
    occurrence_keys = {item["occurrence_key"] for item in filtered}
    projected_permutations = {
        key: [value for value in values if value in occurrence_keys]
        for key, values in permutations.items()
        if isinstance(values, list)
    }
    projected_permutations = {
        key: values for key, values in projected_permutations.items() if values
    }
    source_role_counts = {
        role: sum(item.get("source_role") == role for item in filtered)
        for role in ("property", "variable", "constraint")
        if any(item.get("source_role") == role for item in filtered)
    }
    return {
        "schema_version": index.get("schema_version"),
        "n_occurrences": len(filtered),
        "n_key_permutations": sum(len(values) for values in projected_permutations.values()),
        "source_role_counts": source_role_counts,
        "statistics": filtered,
        "key_permutations": projected_permutations,
    }


def _load_exact_candidates(
    candidates: list[Candidate],
    request: NormalizedRequest,
    catalogs: RuntimeCatalogs,
    diagnostics: dict[str, Any],
) -> list[ExactCandidate]:
    filtered = [
        value for value in candidates
        if _literature_matches(value, request, catalogs)
    ]
    by_doi: dict[str, list[Candidate]] = defaultdict(list)
    for candidate in filtered:
        by_doi[candidate.doi].append(candidate)
    exact: list[ExactCandidate] = []
    connection = open_db(str(PCS_DB))
    try:
        dois = sorted(by_doi)
        for offset in range(0, len(dois), 400):
            batch = dois[offset : offset + 400]
            placeholders = ",".join("?" for _ in batch)
            rows = connection.execute(
                f"SELECT doi, lit_num_id, json_data FROM cards "
                f"WHERE doi IN ({placeholders})",
                batch,
            ).fetchall()
            card_by_doi = {
                row["doi"]: json.loads(row["json_data"]) for row in rows
            }
            missing_cards = sorted(set(batch) - set(card_by_doi))
            if missing_cards:
                fail(
                    "SOURCE_INDEX_MISMATCH",
                    "Registry candidates are missing PCS cards.",
                    "/",
                    details={"dois": missing_cards[:20]},
                )
            for doi in batch:
                card = card_by_doi[doi]
                derived = (
                    card.get("blocks_summary", {})
                    .get("derived_indexes", {})
                    .get("block_search_adv", {})
                )
                block_by_id = {
                    block.get("block_number"): block
                    for block in card.get("blocks", [])
                    if isinstance(block, dict)
                    and isinstance(block.get("block_number"), str)
                }
                for candidate in by_doi[doi]:
                    parent_block = block_by_id.get(candidate.block_id)
                    parent_index = derived.get(candidate.block_id)
                    if not isinstance(parent_block, dict) or not isinstance(parent_index, dict):
                        fail(
                            "SOURCE_INDEX_MISMATCH",
                            "PCS card lacks a candidate block or embedded index.",
                            "/",
                            details={"doi": doi, "block_id": candidate.block_id},
                        )
                    if parent_block.get("block_type") != candidate.block_type:
                        fail(
                            "SOURCE_INDEX_MISMATCH",
                            "Registry and PCS block types disagree.",
                            "/",
                            details={"doi": doi, "block_id": candidate.block_id},
                        )
                    if parent_index.get("schema_version") != catalogs.identity_index_schema:
                        fail(
                            "SOURCE_INDEX_MISMATCH",
                            "Embedded block index has an unsupported schema.",
                            "/",
                            details={
                                "doi": doi,
                                "block_id": candidate.block_id,
                                "schema": parent_index.get("schema_version"),
                            },
                        )
                    subsystem = None
                    block = parent_block
                    index = parent_index
                    if candidate.BLKsubsys_id is not None:
                        subsystem = _resolve_subsystem(card, candidate)
                        block = _project_subsystem_block(parent_block, subsystem)
                        index = _project_subsystem_index(parent_index, block)
                    matched, compound_matches, phase_ids = _block_exact_filters(block, request)
                    if not matched:
                        continue
                    exact.append(
                        ExactCandidate(
                            candidate,
                            card,
                            block,
                            index,
                            compound_matches,
                            phase_ids,
                            subsystem,
                        )
                    )
    finally:
        connection.close()
    diagnostics["card_exact_candidates"] = len(exact)
    return exact


def _selector_occurrence_matches(
    selector: OccurrenceSelector,
    index: Mapping[str, Any],
    compounds: Mapping[str, CompoundSelector],
) -> list[dict[str, Any]]:
    statistics = index.get("statistics")
    permutations = index.get("key_permutations")
    if not isinstance(statistics, list) or not isinstance(permutations, dict):
        fail(
            "SOURCE_INDEX_MISMATCH",
            "Embedded identity index is malformed.",
            "/",
        )
    by_key = {
        item.get("occurrence_key"): item
        for item in statistics
        if isinstance(item, dict)
        and isinstance(item.get("occurrence_key"), str)
    }
    if selector.resolution.input_catalog_role is not None:
        candidate_keys = permutations.get(
            selector.resolution.input_value,
            [],
        )
        if not isinstance(candidate_keys, list):
            fail(
                "SOURCE_INDEX_MISMATCH",
                "Embedded key permutation value is malformed.",
                "/",
            )
    else:
        candidate_keys = list(by_key)
    expected_component = (
        compounds[selector.component_ref].record.comp_num_id
        if selector.component_ref is not None
        else None
    )
    expected_phase_component = (
        compounds[selector.phase_component_ref].record.comp_num_id
        if selector.phase_component_ref is not None
        else None
    )
    matched: dict[str, dict[str, Any]] = {}
    for occurrence_key in candidate_keys:
        statistic = by_key.get(occurrence_key)
        if statistic is None:
            fail(
                "SOURCE_INDEX_MISMATCH",
                "Permutation table references an unknown occurrence.",
                "/",
                details={"occurrence_key": occurrence_key},
            )
        if statistic.get("source_role") != selector.source_role:
            continue
        if (
            statistic.get("quantity_key")
            != selector.resolution.row.quantity_key
        ):
            continue
        if (
            expected_component is not None
            and statistic.get("comp_num_id") != expected_component
        ):
            continue
        if (
            selector.phase_num_id is not None
            and statistic.get("phase_num_id") != selector.phase_num_id
        ):
            continue
        if (
            expected_phase_component is not None
            and statistic.get("phase_component_comp_num_id")
            != expected_phase_component
        ):
            continue
        if (
            int(statistic.get("n_values") or 0)
            < selector.min_finite_values
        ):
            continue
        if (
            int(statistic.get("n_unique") or 0)
            < selector.min_distinct_values
        ):
            continue
        matched[occurrence_key] = statistic
    return [matched[key] for key in sorted(matched)]


def _binding_payload(
    selector: OccurrenceSelector,
    statistic: Mapping[str, Any],
) -> dict[str, Any]:
    semantics = selector.resolution.row.semantics
    return {
        "input_identity": selector.resolution.input_value,
        "input_catalog_role": selector.resolution.input_catalog_role,
        "translated_quantity_key": selector.resolution.row.quantity_key,
        "requested_source_role": selector.source_role,
        "source_role": statistic.get("source_role"),
        "source_global_id": statistic.get("source_global_id"),
        "occurrence_key": statistic.get("occurrence_key"),
        "source_local_key": statistic.get("source_local_key"),
        "source_instance_key": statistic.get("source_instance_key"),
        "component_org_num": statistic.get("component_org_num"),
        "comp_num_id": statistic.get("comp_num_id"),
        "phase_num_id": statistic.get("phase_num_id"),
        "phase_component_comp_num_id": statistic.get(
            "phase_component_comp_num_id"
        ),
        "applies_to_occurrence_key": statistic.get(
            "applies_to_occurrence_key"
        ),
        "unit": semantics.canonical_unit,
        "semantic_type": semantics.semantic_type,
    }


def _condition_passes(
    selector: OccurrenceSelector,
    statistic: Mapping[str, Any],
    diagnostics: dict[str, Any],
) -> tuple[bool, Any]:
    if int(statistic.get("n_values") or 0) != 1:
        return False, None
    value = statistic.get("minimum")
    if not isinstance(value, (int, float)) or not math.isfinite(float(value)):
        return False, None
    if selector.condition is None:
        return True, value
    result = evaluate_block(
        selector.condition,
        [],
        {"value": value},
        diagnostics,
    )
    return result is True, value


def _binding_combinations(
    exact: ExactCandidate,
    request: NormalizedRequest,
    diagnostics: dict[str, Any],
) -> list[BindingCombination]:
    compound_aliases = request.compounds.aliases
    selectors = request.row_selectors + request.constraints
    choices: list[tuple[OccurrenceSelector, list[dict[str, Any]]]] = []
    for selector in selectors:
        matches = _selector_occurrence_matches(
            selector,
            exact.index,
            compound_aliases,
        )
        if selector.source_role == "constraint":
            passing: list[dict[str, Any]] = []
            for statistic in matches:
                passed, _ = _condition_passes(
                    selector,
                    statistic,
                    diagnostics,
                )
                if passed:
                    passing.append(statistic)
            matches = passing
        if not matches:
            diagnostics["role_or_filter_rejections"] += 1
            return []
        if selector.cardinality == "exactly_one" and len(matches) != 1:
            diagnostics["ambiguous_binding_rejections"] += 1
            return []
        choices.append((selector, matches))

    product_size = math.prod(len(values) for _, values in choices)
    if product_size > _MAX_BINDING_COMBINATIONS:
        diagnostics["binding_budget_rejections"] += 1
        return []
    combinations: list[BindingCombination] = []
    for selected_stats in itertools.product(
        *(values for _, values in choices)
    ):
        statistics = {
            selector.alias: statistic
            for (selector, _), statistic in zip(choices, selected_stats)
        }
        bindings = {
            selector.alias: _binding_payload(selector, statistic)
            for (selector, _), statistic in zip(choices, selected_stats)
        }
        fixed_evidence: list[dict[str, Any]] = []
        for selector in request.constraints:
            statistic = statistics[selector.alias]
            _, value = _condition_passes(selector, statistic, diagnostics)
            evidence = dict(bindings[selector.alias])
            evidence.update(
                {
                    "alias": selector.alias,
                    "value": value,
                    "condition": selector.condition,
                }
            )
            fixed_evidence.append(evidence)

        inline_ok = True
        for selector in request.inline_states:
            matches = _selector_occurrence_matches(
                selector,
                exact.index,
                compound_aliases,
            )
            target_stat = statistics.get(selector.applies_to or "")
            target_occurrence = (
                target_stat.get("occurrence_key")
                if isinstance(target_stat, dict)
                else None
            )
            matches = [
                item
                for item in matches
                if item.get("applies_to_occurrence_key")
                == target_occurrence
            ]
            passing: list[tuple[dict[str, Any], Any]] = []
            for statistic in matches:
                passed, value = _condition_passes(
                    selector,
                    statistic,
                    diagnostics,
                )
                if passed:
                    passing.append((statistic, value))
            if (
                not passing
                or (
                    selector.cardinality == "exactly_one"
                    and len(passing) != 1
                )
            ):
                inline_ok = False
                if len(passing) > 1:
                    diagnostics["ambiguous_binding_rejections"] += 1
                else:
                    diagnostics["role_or_filter_rejections"] += 1
                break
            if selector.cardinality == "all" and len(passing) > 1:
                # Multiple target-linked inline states for one alias would add
                # another Cartesian axis. v1 rejects rather than hiding it.
                inline_ok = False
                diagnostics["ambiguous_binding_rejections"] += 1
                break
            statistic, value = passing[0]
            statistics[selector.alias] = statistic
            bindings[selector.alias] = _binding_payload(
                selector,
                statistic,
            )
            evidence = dict(bindings[selector.alias])
            evidence.update(
                {
                    "alias": selector.alias,
                    "value": value,
                    "condition": selector.condition,
                    "applies_to_alias": selector.applies_to,
                }
            )
            fixed_evidence.append(evidence)
        if inline_ok:
            combinations.append(
                BindingCombination(bindings, statistics, fixed_evidence)
            )

    unique = {value.key: value for value in combinations}
    diagnostics["binding_combinations"] += len(unique)
    return [unique[key] for key in sorted(unique)]


def _raw_block(
    paper: Mapping[str, Any],
    candidate: Candidate,
) -> dict[str, Any]:
    match = _BLOCK_ID_RE.fullmatch(candidate.block_id)
    if match is None:
        fail(
            "SOURCE_INDEX_MISMATCH",
            "Registry contains a malformed typed block ID.",
            "/",
            details={"block_id": candidate.block_id},
        )
    prefix, ordinal_text = match.groups()
    family = "PureOrMixtureData" if prefix == "PROPblock" else "ReactionData"
    if family != candidate.block_type:
        fail(
            "SOURCE_INDEX_MISMATCH",
            "Typed block prefix and source block family disagree.",
            "/",
            details={
                "block_id": candidate.block_id,
                "block_type": candidate.block_type,
            },
        )
    number_field = (
        "nPureOrMixtureDataNumber"
        if family == "PureOrMixtureData"
        else "nReactionDataNumber"
    )
    ordinal = int(ordinal_text)
    matches = [
        block
        for block in paper.get(family, [])
        if isinstance(block, dict) and block.get(number_field) == ordinal
    ]
    if len(matches) != 1:
        fail(
            "SOURCE_INDEX_MISMATCH",
            "Could not resolve one exact typed block in raw ThermoML.",
            "/",
            details={
                "doi": candidate.doi,
                "block_id": candidate.block_id,
                "matches": len(matches),
            },
        )
    return matches[0]


def _finite_number(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float, str)):
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def _occurrence_number(
    statistic: Mapping[str, Any],
) -> int:
    local_key = statistic.get("source_local_key")
    if not isinstance(local_key, str):
        fail(
            "SOURCE_INDEX_MISMATCH",
            "Indexed row occurrence lacks a local key.",
            "/",
        )
    match = _LOCAL_OCCURRENCE_RE.fullmatch(local_key)
    if match is None:
        fail(
            "SOURCE_INDEX_MISMATCH",
            "Indexed row occurrence has a malformed local key.",
            "/",
            details={"source_local_key": local_key},
        )
    return int(match.group(1))


def _subsystem_point_indexes(
    subsystem: Mapping[str, Any] | None,
    parent_n_rows: int,
) -> list[int]:
    if subsystem is None:
        return list(range(parent_n_rows))
    membership = subsystem.get("point_membership")
    if not isinstance(membership, dict) or membership.get("encoding") != "one_based_inclusive_runs":
        fail("SOURCE_INDEX_MISMATCH", "Subsystem point membership is malformed.", "/")
    runs = membership.get("runs")
    if not isinstance(runs, list):
        fail("SOURCE_INDEX_MISMATCH", "Subsystem point runs are malformed.", "/")
    indexes: list[int] = []
    previous = 0
    for run in runs:
        if (
            not isinstance(run, list)
            or len(run) != 2
            or any(isinstance(value, bool) or not isinstance(value, int) for value in run)
        ):
            fail("SOURCE_INDEX_MISMATCH", "Subsystem point run is malformed.", "/")
        start, end = run
        if start <= previous or end < start or end > parent_n_rows:
            fail("SOURCE_INDEX_MISMATCH", "Subsystem point runs are invalid or overlapping.", "/")
        indexes.extend(range(start - 1, end))
        previous = end
    if len(indexes) != subsystem.get("n_points"):
        fail(
            "SOURCE_INDEX_MISMATCH",
            "Subsystem point count disagrees with its inclusive runs.",
            "/",
            details={"BLKsubsys_id": subsystem.get("BLKsubsys_id")},
        )
    return indexes


def _materialize_series(
    raw_block: Mapping[str, Any],
    statistic: Mapping[str, Any],
    diagnostics: dict[str, Any],
) -> list[float | None]:
    source_role = statistic.get("source_role")
    if source_role not in {"variable", "property"}:
        fail(
            "SOURCE_INDEX_MISMATCH",
            "Only variable/property occurrences can materialize as rows.",
            "/",
            details={"source_role": source_role},
        )
    occurrence_number = _occurrence_number(statistic)
    collection = "VariableValue" if source_role == "variable" else "PropertyValue"
    number_field = "nVarNumber" if source_role == "variable" else "nPropNumber"
    value_field = "nVarValue" if source_role == "variable" else "nPropValue"
    rows = raw_block.get("NumValues", [])
    if not isinstance(rows, list):
        fail(
            "SOURCE_INDEX_MISMATCH",
            "Raw block NumValues is malformed.",
            "/",
        )
    values: list[float | None] = []
    n_limits = 0
    n_nonfinite = 0
    for row_index, raw_row in enumerate(rows):
        raw_items = (
            raw_row.get(collection, [])
            if isinstance(raw_row, dict)
            else []
        )
        matches = [
            item
            for item in raw_items
            if isinstance(item, dict)
            and item.get(number_field) == occurrence_number
        ]
        if len(matches) > 1:
            fail(
                "SOURCE_INDEX_MISMATCH",
                "Raw NumValues row contains duplicate occurrence cells.",
                "/",
                details={
                    "occurrence_key": statistic.get("occurrence_key"),
                    "row_ordinal": row_index,
                },
            )
        if not matches:
            values.append(None)
            continue
        item = matches[0]
        parsed = _finite_number(item.get(value_field))
        if parsed is not None:
            values.append(parsed)
            continue
        if source_role == "property" and isinstance(
            item.get("PropLimit"),
            dict,
        ):
            limit_value = _finite_number(
                item["PropLimit"].get("nPropLimitValue")
            )
            if limit_value is not None:
                n_limits += 1
                values.append(None)
                continue
        if item.get(value_field) is not None:
            n_nonfinite += 1
        values.append(None)

    expected_rows = int(statistic.get("n_rows") or 0)
    expected_values = int(statistic.get("n_values") or 0)
    expected_limits = int(statistic.get("n_limit_values") or 0)
    expected_nonfinite = int(statistic.get("n_nonfinite") or 0)
    finite_values = sum(value is not None for value in values)
    if (
        len(values) != expected_rows
        or n_limits != expected_limits
        or n_nonfinite != expected_nonfinite
        or finite_values != expected_values
    ):
        fail(
            "SOURCE_INDEX_MISMATCH",
            "Uncapped raw occurrence statistics disagree with PCS index.",
            "/",
            details={
                "occurrence_key": statistic.get("occurrence_key"),
                "raw_rows": len(values),
                "index_rows": expected_rows,
                "raw_finite": finite_values,
                "raw_limits": n_limits,
                "index_finite_values": expected_values,
                "index_limits": expected_limits,
                "raw_nonfinite": n_nonfinite,
                "index_nonfinite": expected_nonfinite,
            },
        )
    diagnostics["limit_cells_as_null"] += n_limits
    diagnostics["nonfinite_cells_as_null"] += n_nonfinite
    return values


def _is_finite(value: Any) -> bool:
    return (
        not isinstance(value, bool)
        and isinstance(value, (int, float))
        and math.isfinite(float(value))
    )


def _selected_payload(
    request: NormalizedRequest,
    selected: Mapping[str, Any],
) -> dict[str, dict[str, Any]]:
    payload: dict[str, dict[str, Any]] = {}
    for item in request.select:
        payload[item.alias] = {
            "value": selected.get(item.alias),
            "unit": item.expr_type.unit,
            "semantic_type": item.expr_type.semantic_type,
        }
    return payload


def _evaluate_combination(
    combination: BindingCombination,
    series_by_occurrence: Mapping[str, list[float | None]],
    n_rows: int,
    request: NormalizedRequest,
    diagnostics: dict[str, Any],
) -> dict[str, Any] | None:
    for selector in request.row_selectors:
        occurrence = combination.bindings[selector.alias]["occurrence_key"]
        observed = [
            value for value in series_by_occurrence[occurrence]
            if _is_finite(value)
        ]
        if (
            len(observed) < selector.min_finite_values
            or len(set(observed)) < selector.min_distinct_values
        ):
            diagnostics["observation_rejections"] += 1
            return None

    rows: list[dict[str, Any]] = []
    for row_index in range(n_rows):
        row: dict[str, Any] = {}
        for selector in request.row_selectors:
            occurrence = combination.bindings[selector.alias]["occurrence_key"]
            row[selector.alias] = series_by_occurrence[occurrence][row_index]
        for computed in request.compute:
            row[computed.alias] = evaluate_row(
                computed.expr,
                row,
                diagnostics,
            )
        if (
            request.where is None
            or evaluate_row(request.where, row, diagnostics) is True
        ):
            rows.append(row)
    rows_after = len(rows)
    aliases_for_complete = (
        request.minimum_common_points.aliases
        if request.minimum_common_points is not None
        else tuple(value.alias for value in request.row_selectors)
    )
    complete = sum(
        all(_is_finite(row.get(alias)) for alias in aliases_for_complete)
        for row in rows
    )
    if (
        request.minimum_common_points is not None
        and complete < request.minimum_common_points.count
    ):
        diagnostics["minimum_point_rejections"] += 1
        return None

    selected: dict[str, Any] = {}
    for item in request.select:
        selected[item.alias] = evaluate_block(
            item.expr,
            rows,
            selected,
            diagnostics,
        )
    if (
        request.having is not None
        and evaluate_block(
            request.having,
            rows,
            selected,
            diagnostics,
        )
        is not True
    ):
        diagnostics["having_rejections"] += 1
        return None
    order_keys = [
        evaluate_block(item.expr, rows, selected, diagnostics)
        for item in request.order_by
    ]
    return {
        "binding_key": combination.key,
        "bindings": combination.bindings,
        "fixed_filter_evidence": combination.fixed_filter_evidence,
        "matched_complete_points": complete,
        "complete_point_aliases": list(aliases_for_complete),
        "selected": _selected_payload(request, selected),
        "order_keys": order_keys,
        "match_trace": {
            "rows_before_where": n_rows,
            "rows_after_where": rows_after,
            "row_source": "thermoml_raw.db:NumValues",
            "card_display_rows_used": False,
        },
    }


def _reference_payload(
    exact: ExactCandidate,
    catalogs: RuntimeCatalogs,
) -> dict[str, Any]:
    candidate = exact.candidate
    reference = catalogs.references_by_doi[candidate.doi]
    match = _BLOCK_ID_RE.fullmatch(candidate.block_id)
    assert match is not None
    subsystem = exact.subsystem
    parent_block = next(
        (
            block for block in exact.card.get("blocks", [])
            if isinstance(block, dict) and block.get("block_number") == candidate.block_id
        ),
        None,
    )
    if not isinstance(parent_block, dict):
        fail("SOURCE_INDEX_MISMATCH", "Resolved PCS parent block disappeared.", "/")
    return {
        "doi": candidate.doi,
        "lit_num_id": reference.lit_num_id,
        "lit_id": reference.lit_id,
        "year": reference.year,
        "first_author": reference.first_author,
        "journal": reference.journal,
        "title": exact.card.get("paper", {}).get("title"),
        "block_id": candidate.block_id,
        "BLKsubsys_id": candidate.BLKsubsys_id,
        "search_scope": "subsystem" if subsystem is not None else "declared",
        "source_block_number": int(match.group(2)),
        "block_type": candidate.block_type,
        "blocktype_num_id": parent_block.get("blocktype_num_id"),
        "system_type": exact.block.get("system_type"),
        "n_components": len(exact.block.get("compounds", [])),
        "n_matching_datapoints": (
            subsystem.get("n_points")
            if subsystem is not None
            else parent_block.get("data_summary", {}).get("n_points")
        ),
        "declared_system_type": parent_block.get("system_type"),
        "declared_n_components": len(parent_block.get("compounds", [])),
        "parent_n_datapoints": parent_block.get("data_summary", {}).get("n_points"),
    }


def _prepare_binding_combinations(
    exact_candidates: list[ExactCandidate],
    request: NormalizedRequest,
    diagnostics: dict[str, Any],
) -> dict[tuple[str, str, str | None], list[BindingCombination]]:
    combinations_by_target: dict[
        tuple[str, str, str | None], list[BindingCombination]
    ] = {}
    for exact in exact_candidates:
        combinations = _binding_combinations(exact, request, diagnostics)
        if combinations:
            candidate = exact.candidate
            combinations_by_target[
                (candidate.doi, candidate.block_id, candidate.BLKsubsys_id)
            ] = combinations
    return combinations_by_target


def _execute_exact(
    exact_candidates: list[ExactCandidate],
    combinations_by_target: Mapping[
        tuple[str, str, str | None], list[BindingCombination]
    ],
    request: NormalizedRequest,
    catalogs: RuntimeCatalogs,
    diagnostics: dict[str, Any],
) -> list[dict[str, Any]]:
    by_doi: dict[str, list[ExactCandidate]] = defaultdict(list)
    for exact in exact_candidates:
        candidate = exact.candidate
        if (candidate.doi, candidate.block_id, candidate.BLKsubsys_id) in combinations_by_target:
            by_doi[candidate.doi].append(exact)

    results: list[dict[str, Any]] = []
    raw_connection = open_raw_db()
    materialized_rows = 0
    try:
        for doi in sorted(by_doi):
            row = raw_connection.execute(
                "SELECT json_data FROM papers WHERE doi = ?",
                (doi,),
            ).fetchone()
            if row is None:
                fail(
                    "SOURCE_INDEX_MISMATCH",
                    "PCS DOI is missing from the raw ThermoML database.",
                    "/",
                    details={"doi": doi},
                )
            try:
                paper = json.loads(row["json_data"])
            except (TypeError, json.JSONDecodeError) as exc:
                fail(
                    "SOURCE_INDEX_MISMATCH",
                    "Raw ThermoML paper JSON is malformed.",
                    "/",
                    details={"doi": doi, "error": str(exc)},
                )
            for exact in by_doi[doi]:
                candidate = exact.candidate
                raw_block = _raw_block(paper, candidate)
                raw_rows = raw_block.get("NumValues", [])
                if not isinstance(raw_rows, list):
                    fail(
                        "SOURCE_INDEX_MISMATCH",
                        "Raw block NumValues is not an array.",
                        "/",
                    )
                parent_n_rows = len(raw_rows)
                point_indexes = _subsystem_point_indexes(exact.subsystem, parent_n_rows)
                n_rows = len(point_indexes)
                materialized_rows += parent_n_rows
                if materialized_rows > _MAX_MATERIALIZED_ROWS:
                    fail(
                        "SEARCH_TOO_BROAD",
                        "Exact search exceeds the raw-row budget.",
                        "/",
                        details={"max_materialized_rows": _MAX_MATERIALIZED_ROWS},
                    )
                combinations = combinations_by_target[
                    (candidate.doi, candidate.block_id, candidate.BLKsubsys_id)
                ]
                needed_stats: dict[str, dict[str, Any]] = {}
                for combination in combinations:
                    for selector in request.row_selectors:
                        statistic = combination.statistics[selector.alias]
                        needed_stats[statistic["occurrence_key"]] = statistic
                series_by_occurrence = {}
                for occurrence, statistic in sorted(needed_stats.items()):
                    parent_series = _materialize_series(raw_block, statistic, diagnostics)
                    series_by_occurrence[occurrence] = [
                        parent_series[index] for index in point_indexes
                    ]
                binding_results = [
                    evaluated
                    for combination in combinations
                    if (
                        evaluated := _evaluate_combination(
                            combination,
                            series_by_occurrence,
                            n_rows,
                            request,
                            diagnostics,
                        )
                    ) is not None
                ]
                if not binding_results:
                    continue
                for result in binding_results:
                    result["match_trace"].update(
                        {
                            "point_scope": (
                                "subsystem_inclusive_runs"
                                if exact.subsystem is not None
                                else "declared_block"
                            ),
                            "BLKsubsys_id": candidate.BLKsubsys_id,
                            "parent_rows": parent_n_rows,
                        }
                    )
                binding_results.sort(key=lambda value: value["binding_key"])
                results.append(
                    {
                        "block": _reference_payload(exact, catalogs),
                        "match_evidence": {
                            "compound_aliases": exact.compound_matches,
                            "phase_num_ids": list(exact.phase_ids),
                            "identity_index_schema": catalogs.identity_index_schema,
                            "subsystem": exact.subsystem,
                        },
                        "binding_matches": binding_results,
                    }
                )
                diagnostics["materialized_blocks"] += 1
    finally:
        raw_connection.close()
    diagnostics["materialized_rows"] = materialized_rows
    return results


def _compare_scalar(
    left: Any,
    right: Any,
    order: OrderItem,
) -> int:
    left_null = left is None
    right_null = right is None
    if left_null or right_null:
        if left_null and right_null:
            return 0
        if left_null:
            return -1 if order.nulls == "first" else 1
        return 1 if order.nulls == "first" else -1
    if left < right:
        result = -1
    elif left > right:
        result = 1
    else:
        result = 0
    return -result if order.direction == "desc" else result


def _compare_binding(
    left: Mapping[str, Any],
    right: Mapping[str, Any],
    order_by: tuple[OrderItem, ...],
) -> int:
    for index, order in enumerate(order_by):
        compared = _compare_scalar(
            left["order_keys"][index],
            right["order_keys"][index],
            order,
        )
        if compared:
            return compared
    return (
        -1
        if left["binding_key"] < right["binding_key"]
        else 1
        if left["binding_key"] > right["binding_key"]
        else 0
    )


def _stable_block_key(result: Mapping[str, Any]) -> tuple[Any, ...]:
    block = result["block"]
    return (
        block["doi"],
        0 if block["block_id"].startswith("PROPblock_") else 1,
        block["source_block_number"],
        block.get("BLKsubsys_id") or "",
    )


def _order_results(
    results: list[dict[str, Any]],
    request: NormalizedRequest,
) -> None:
    if request.order_by:
        binding_comparator = cmp_to_key(
            lambda left, right: _compare_binding(
                left,
                right,
                request.order_by,
            )
        )
        for result in results:
            result["binding_matches"].sort(key=binding_comparator)

        def compare_blocks(
            left: Mapping[str, Any],
            right: Mapping[str, Any],
        ) -> int:
            compared = _compare_binding(
                left["binding_matches"][0],
                right["binding_matches"][0],
                request.order_by,
            )
            if compared:
                return compared
            left_key = _stable_block_key(left)
            right_key = _stable_block_key(right)
            return -1 if left_key < right_key else 1 if left_key > right_key else 0

        results.sort(key=cmp_to_key(compare_blocks))
    else:
        results.sort(key=_stable_block_key)


def _alias_resolution(request: NormalizedRequest) -> list[dict[str, Any]]:
    values: list[dict[str, Any]] = []
    for selector in request.row_selectors + request.fixed_selectors:
        payload = selector.resolution.as_result()
        payload.update(
            {
                "alias": selector.alias,
                "required_source_role": selector.source_role,
                "required_role_global_id": (
                    selector.resolution.row.global_id_for_role(
                        selector.source_role
                    )
                    if selector.source_role != "inline_state"
                    else None
                ),
                "canonical_unit": (
                    selector.resolution.row.semantics.canonical_unit
                ),
                "semantic_type": (
                    selector.resolution.row.semantics.semantic_type
                ),
            }
        )
        if selector.applies_to is not None:
            payload["applies_to"] = selector.applies_to
        values.append(payload)
    return values


def _selector_match_counts(
    exact: ExactCandidate,
    selector: OccurrenceSelector,
    request: NormalizedRequest,
) -> dict[str, int]:
    statistics = [
        item for item in exact.index.get("statistics", [])
        if isinstance(item, dict)
    ]
    quantity = [
        item for item in statistics
        if item.get("quantity_key") == selector.resolution.row.quantity_key
    ]
    requested_role = [
        item for item in quantity
        if item.get("source_role") == selector.source_role
    ]
    expected_component = (
        request.compounds.aliases[selector.component_ref].record.comp_num_id
        if selector.component_ref is not None
        else None
    )
    component = [
        item for item in requested_role
        if expected_component is None
        or item.get("comp_num_id") == expected_component
    ]
    phase = [
        item for item in component
        if selector.phase_num_id is None
        or item.get("phase_num_id") == selector.phase_num_id
    ]
    expected_phase_component = (
        request.compounds.aliases[
            selector.phase_component_ref
        ].record.comp_num_id
        if selector.phase_component_ref is not None
        else None
    )
    phase_component = [
        item for item in phase
        if expected_phase_component is None
        or item.get("phase_component_comp_num_id")
        == expected_phase_component
    ]
    observations = [
        item for item in phase_component
        if int(item.get("n_values") or 0) >= selector.min_finite_values
        and int(item.get("n_unique") or 0) >= selector.min_distinct_values
    ]
    condition = observations
    if selector.source_role == "constraint":
        condition = [
            item for item in observations
            if _condition_passes(selector, item, _empty_diagnostics())[0]
        ]
    return {
        "same_quantity_any_role": len(quantity),
        "requested_role": len(requested_role),
        "after_component": len(component),
        "after_phase": len(phase),
        "after_phase_component": len(phase_component),
        "after_observation_thresholds": len(observations),
        "after_fixed_condition": len(condition),
    }


def _property_declaration_context(
    exact: ExactCandidate,
    binding: Mapping[str, Any],
) -> dict[str, Any] | None:
    """Return observand metadata omitted from the identity-index statistic."""
    if binding.get("source_role") != "property":
        return None
    local_key = binding.get("source_local_key")
    declaration = next(
        (
            item
            for item in exact.block.get("properties", [])
            if isinstance(item, dict) and item.get("BLKprop_id") == local_key
        ),
        None,
    )
    if declaration is None:
        return None
    fields = (
        "BLKprop_id", "prop_num_id", "prop_ID", "name", "group",
        "presentation", "standard_state", "ref_state_type",
        "ref_temperature_K", "ref_pressure_kPa", "temperature_K",
        "pressure_kPa", "property_phase", "ref_phase",
        "component_org_num", "meas_num_id", "meas_ID",
        "method_standard", "method_custom",
    )
    return {field: declaration.get(field) for field in fields}


def database_intent_summary(
    prepared: PreparedSearch,
) -> dict[str, Any]:
    """Summarize exact registry/PCS bindings without opening raw ThermoML."""
    request = prepared.request
    catalogs = prepared.catalogs
    selectors = request.row_selectors + request.fixed_selectors
    by_alias: dict[str, list[dict[str, Any]]] = {
        selector.alias: [] for selector in selectors
    }
    staged_counts: dict[str, dict[str, int]] = {
        selector.alias: {
            "same_quantity_any_role": 0,
            "requested_role": 0,
            "after_component": 0,
            "after_phase": 0,
            "after_phase_component": 0,
            "after_observation_thresholds": 0,
            "after_fixed_condition": 0,
        }
        for selector in selectors
    }
    block_previews: list[dict[str, Any]] = []
    state_digest = hashlib.sha256()
    bindable_blocks = 0
    total_combinations = 0

    for exact in prepared.exact_candidates:
        candidate = exact.candidate
        target_key = (
            candidate.doi,
            candidate.block_id,
            candidate.BLKsubsys_id,
        )
        for selector in selectors:
            counts = _selector_match_counts(exact, selector, request)
            for name, value in counts.items():
                staged_counts[selector.alias][name] += value

        combinations = prepared.combinations_by_target.get(target_key, [])
        if not combinations:
            continue
        bindable_blocks += 1
        total_combinations += len(combinations)
        state_digest.update(
            json.dumps(
                target_key,
                ensure_ascii=False,
                separators=(",", ":"),
            ).encode("utf-8")
        )
        binding_examples: list[dict[str, Any]] = []
        for combination in combinations:
            state_digest.update(combination.key.encode("utf-8"))
            example_bindings: dict[str, Any] = {}
            for alias, binding in sorted(combination.bindings.items()):
                statistic = combination.statistics[alias]
                evidence = {
                    "lit_num_id": candidate.lit_num_id,
                    "doi": candidate.doi,
                    "block_id": candidate.block_id,
                    "BLKsubsys_id": candidate.BLKsubsys_id,
                    **binding,
                    "n_rows": statistic.get("n_rows"),
                    "n_values": statistic.get("n_values"),
                    "n_unique": statistic.get("n_unique"),
                    "min": statistic.get("minimum"),
                    "max": statistic.get("maximum"),
                    "constant_value": (
                        statistic.get("minimum")
                        if int(statistic.get("n_unique") or 0) == 1
                        else None
                    ),
                }
                property_context = _property_declaration_context(exact, binding)
                if property_context is not None:
                    evidence["property_context"] = property_context
                by_alias[alias].append(evidence)
                if len(binding_examples) < 3:
                    example_bindings[alias] = evidence
            if example_bindings and len(binding_examples) < 3:
                binding_examples.append(
                    {
                        "binding_key": combination.key,
                        "bindings": example_bindings,
                    }
                )
        if len(block_previews) < 20:
            block_previews.append(
                {
                    "block": _reference_payload(exact, catalogs),
                    "n_binding_combinations": len(combinations),
                    "binding_examples": binding_examples,
                }
            )

    selector_reviews: list[dict[str, Any]] = []
    for selector in selectors:
        actual_rows = by_alias[selector.alias]
        unique_actual: dict[str, dict[str, Any]] = {}
        for row in actual_rows:
            key = json.dumps(
                [
                    row.get("doi"),
                    row.get("block_id"),
                    row.get("BLKsubsys_id"),
                    row.get("occurrence_key"),
                ],
                separators=(",", ":"),
            )
            unique_actual[key] = row
        component = (
            request.compounds.aliases[selector.component_ref]
            if selector.component_ref is not None
            else None
        )
        phase_component = (
            request.compounds.aliases[selector.phase_component_ref]
            if selector.phase_component_ref is not None
            else None
        )
        phase_record = (
            catalogs.phases_by_id.get(selector.phase_num_id)
            if selector.phase_num_id is not None
            else None
        )
        property_observands: list[dict[str, Any]] = []
        seen_observands: set[str] = set()
        for occurrence in unique_actual.values():
            context = occurrence.get("property_context")
            if not isinstance(context, dict):
                continue
            observand = {
                "lit_num_id": occurrence.get("lit_num_id"),
                "doi": occurrence.get("doi"),
                "block_id": occurrence.get("block_id"),
                "BLKsubsys_id": occurrence.get("BLKsubsys_id"),
                "BLKprop_id": occurrence.get("source_local_key"),
                **context,
            }
            observand_key = json.dumps(
                observand, ensure_ascii=False, sort_keys=True, separators=(",", ":")
            )
            if observand_key not in seen_observands:
                seen_observands.add(observand_key)
                property_observands.append(observand)
        selector_reviews.append(
            {
                "alias": selector.alias,
                "input_identity": selector.resolution.input_value,
                "input_catalog_role": selector.resolution.input_catalog_role,
                "quantity_key": selector.resolution.row.quantity_key,
                "preferred_name": selector.resolution.row.preferred_name,
                "requested_source_role": selector.source_role,
                "required_role_global_id": (
                    selector.resolution.row.global_id_for_role(
                        selector.source_role
                    )
                    if selector.source_role != "inline_state"
                    else None
                ),
                "canonical_unit": (
                    selector.resolution.row.semantics.canonical_unit
                ),
                "component": (
                    {
                        "alias": component.alias,
                        "comp_num_id": component.record.comp_num_id,
                        "name": component.record.common_name,
                    }
                    if component is not None
                    else None
                ),
                "phase": (
                    {
                        "phase_num_id": phase_record.phase_num_id,
                        "phase_id": phase_record.phase_id,
                        "name": phase_record.phase_name,
                    }
                    if phase_record is not None
                    else None
                ),
                "phase_component": (
                    {
                        "alias": phase_component.alias,
                        "comp_num_id": phase_component.record.comp_num_id,
                        "name": phase_component.record.common_name,
                    }
                    if phase_component is not None
                    else None
                ),
                "cardinality": selector.cardinality,
                "applies_to": selector.applies_to,
                "stage_counts": staged_counts[selector.alias],
                "n_distinct_database_occurrences": len(unique_actual),
                "effective_quantity_global_ids": list(
                    selector.resolution.row.available_global_ids
                ),
                "source_global_id_note": (
                    "Inline state is a target-linked PCS occurrence and has no independent source GLOB ID; use the submitted/effective quantity identity plus applies_to."
                    if selector.source_role == "inline_state"
                    else None
                ),
                "actual_source_global_ids": sorted(
                    {
                        row["source_global_id"]
                        for row in unique_actual.values()
                        if isinstance(row.get("source_global_id"), str)
                    }
                ),
                "actual_component_ids": sorted(
                    {
                        row["comp_num_id"]
                        for row in unique_actual.values()
                        if isinstance(row.get("comp_num_id"), str)
                    }
                ),
                "actual_phase_ids": sorted(
                    {
                        row["phase_num_id"]
                        for row in unique_actual.values()
                        if isinstance(row.get("phase_num_id"), str)
                    }
                ),
                "examples": list(unique_actual.values())[:8],
                "property_observands": property_observands[:16],
                "property_observands_truncated": len(property_observands) > 16,
                "n_non_direct_property_observands": sum(
                    item.get("presentation") not in (None, "Direct value, X")
                    for item in property_observands
                ),
                "non_direct_property_observands": [
                    item for item in property_observands
                    if item.get("presentation") not in (None, "Direct value, X")
                ][:4],
                "n_unknown_property_presentations": sum(
                    item.get("presentation") is None for item in property_observands
                ),
                "unknown_property_presentations": [
                    item for item in property_observands
                    if item.get("presentation") is None
                ][:4],
            }
        )

    warnings: list[dict[str, Any]] = []
    for selector in selector_reviews:
        if (
            selector["input_catalog_role"] is not None
            and selector["input_catalog_role"]
            != selector["requested_source_role"]
        ):
            warnings.append(
                {
                    "code": "CROSS_ROLE_TRANSLATION",
                    "alias": selector["alias"],
                    "message": (
                        f"{selector['input_identity']} is catalogued as "
                        f"{selector['input_catalog_role']} but is intentionally "
                        f"bound as {selector['requested_source_role']} through "
                        f"quantity {selector['quantity_key']}."
                    ),
                }
            )
        if selector["n_non_direct_property_observands"]:
            warnings.append(
                {
                    "code": "NON_DIRECT_PROPERTY_PRESENTATION",
                    "alias": selector["alias"],
                    "message": (
                        "At least one bound property is a reference-state or "
                        "other non-direct presentation. Confirm that the "
                        "observand, not only its GLOB property identity, is intended."
                    ),
                    "n_occurrences": selector["n_non_direct_property_observands"],
                    "examples": selector["non_direct_property_observands"],
                }
            )
        if selector["n_unknown_property_presentations"]:
            warnings.append(
                {
                    "code": "UNKNOWN_PROPERTY_PRESENTATION",
                    "alias": selector["alias"],
                    "message": (
                        "At least one bound property has no declared presentation. "
                        "Confirm that treating the reported value as the intended observand is acceptable."
                    ),
                    "n_occurrences": selector["n_unknown_property_presentations"],
                    "examples": selector["unknown_property_presentations"],
                }
            )
        if selector["n_distinct_database_occurrences"] == 0:
            own_survivors = selector["stage_counts"]["after_fixed_condition"]
            warnings.append(
                {
                    "code": (
                        "NO_DATABASE_OCCURRENCE"
                        if own_survivors == 0
                        else "NO_JOINT_DATABASE_OCCURRENCE"
                    ),
                    "alias": selector["alias"],
                    "message": (
                        "No exact database occurrence survived this selector's requested role, component, phase, cardinality, thresholds, and fixed condition."
                        if own_survivors == 0
                        else "This selector has individually valid database occurrences, but none participates in a block jointly bindable with every other selector. Inspect the progressive counts of the selectors that reached zero."
                    ),
                    "individual_survivors": own_survivors,
                }
            )

    if (
        prepared.diagnostics["registry_candidates"] > 0
        and prepared.diagnostics["card_exact_candidates"] == 0
    ):
        warnings.append(
            {
                "code": "BLOCK_LEVEL_FILTER_ELIMINATION",
                "message": (
                    "Coarse registry candidates existed, but no PCS card survived the combined block-level literature, compound, system, subsystem, and phase-presence filters. Selector progressive counts below are scoped only to surviving exact PCS candidates."
                ),
            }
        )
    if bindable_blocks == 0:
        warnings.append(
            {
                "code": "NO_BINDABLE_BLOCKS",
                "message": (
                    "The reviewed identities and annotations produce no "
                    "jointly bindable ThermoML block. Confirm this no-data "
                    "intent or revise the request."
                ),
            }
        )

    return {
        "counts": {
            "registry_candidates": prepared.diagnostics[
                "registry_candidates"
            ],
            "card_exact_candidates": prepared.diagnostics[
                "card_exact_candidates"
            ],
            "bindable_blocks": bindable_blocks,
            "binding_combinations": total_combinations,
        },
        "binding_state_sha256": state_digest.hexdigest(),
        "selector_stage_counts_scope": (
            "Occurrences within exact PCS candidates after block-level literature, compound, system, subsystem, and phase-presence filtering."
        ),
        "selectors": selector_reviews,
        "blocks_preview": block_previews,
        "blocks_preview_truncated": bindable_blocks > len(block_previews),
        "warnings": warnings,
        "diagnostics": {
            key: value
            for key, value in prepared.diagnostics.items()
            if key not in {"materialized_blocks", "materialized_rows"}
        },
        "raw_rows_read": False,
    }

def _empty_diagnostics() -> dict[str, Any]:
    return {
        "registry_candidates": 0,
        "card_exact_candidates": 0,
        "binding_combinations": 0,
        "materialized_blocks": 0,
        "materialized_rows": 0,
        "role_or_filter_rejections": 0,
        "ambiguous_binding_rejections": 0,
        "binding_budget_rejections": 0,
        "minimum_point_rejections": 0,
        "observation_rejections": 0,
        "having_rejections": 0,
        "numeric_nulls": 0,
        "limit_cells_as_null": 0,
        "nonfinite_cells_as_null": 0,
    }


def normalize_search_request(
    **engine_kwargs: Any,
) -> tuple[RuntimeCatalogs, NormalizedRequest]:
    """Resolve the canonical request without searching block registries."""
    catalogs = load_runtime_catalogs()
    request = normalize_request(catalogs=catalogs, **engine_kwargs)
    return catalogs, request


def prepare_normalized_search(
    catalogs: RuntimeCatalogs,
    request: NormalizedRequest,
) -> PreparedSearch:
    """Resolve registry candidates and exact BLK bindings without raw rows."""
    diagnostics = _empty_diagnostics()
    candidates = _discover_candidates(request, diagnostics)
    exact_candidates = _load_exact_candidates(
        candidates,
        request,
        catalogs,
        diagnostics,
    )
    combinations_by_target = _prepare_binding_combinations(
        exact_candidates,
        request,
        diagnostics,
    )
    return PreparedSearch(
        catalogs=catalogs,
        request=request,
        diagnostics=diagnostics,
        exact_candidates=exact_candidates,
        combinations_by_target=combinations_by_target,
    )


def _execute_prepared_search(
    prepared: PreparedSearch,
    *,
    capability: object,
) -> dict[str, Any]:
    """Materialize raw ThermoML rows only for a fully reviewed search plan."""
    if capability is not _RAW_EXECUTION_CAPABILITY:
        raise PermissionError("raw Tool 12 execution requires the lifecycle capability")
    request = prepared.request
    results = _execute_exact(
        prepared.exact_candidates,
        prepared.combinations_by_target,
        request,
        prepared.catalogs,
        prepared.diagnostics,
    )
    _order_results(results, request)
    total_blocks = len(results)
    total_bindings = sum(
        len(result["binding_matches"]) for result in results
    )
    truncated = total_blocks > request.limit
    returned = results[: request.limit]
    return {
        "schema": RESULT_SCHEMA,
        "normalized_query": request.as_dict(),
        "alias_resolution": _alias_resolution(request),
        "n_results": len(returned),
        "n_binding_matches": sum(
            len(result["binding_matches"]) for result in returned
        ),
        "total_matching_blocks_before_limit": total_blocks,
        "total_binding_matches_before_limit": total_bindings,
        "results": returned,
        "diagnostics": prepared.diagnostics,
        "truncated": truncated,
    }


def error_result(
    error: AdvancedSearchError,
    *,
    explanation: Any = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "schema": ERROR_SCHEMA,
        "error": error.as_dict(),
        "results": [],
        "diagnostics": {},
    }
    if isinstance(explanation, str) and explanation:
        payload["search_explanation"] = explanation
    return payload
