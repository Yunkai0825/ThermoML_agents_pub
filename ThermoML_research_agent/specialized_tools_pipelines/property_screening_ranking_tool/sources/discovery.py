"""Streaming candidate discovery over normalized ThermoML registries.

This stage performs coarse, role-aware pruning only.  Every candidate is
rechecked against the exact PCS declarations and authoritative raw rows by
the extraction/harmonization stages.
"""

from __future__ import annotations

import json
import sqlite3
from typing import Any, Iterator

from card_db_search_tools.basic_search_tools.advanced_block_search.catalogs import (
    PM_REGISTRY_DB,
)
from card_db_search_tools.basic_search_tools.normalization_helpers.db_helpers import (
    open_db,
)

from ..interface import (
    CandidateRef,
    ConstraintSpec,
    DiscoveryResult,
    NormalizedRequest,
)
from ..tool_settings import DISCOVERY_PAGE_SIZE




def _json_role_exists(
    column: str, json_field: str, values: tuple[str, ...]
) -> tuple[str, list[Any]]:
    placeholders = ",".join("?" for _ in values)
    return (
        "EXISTS (SELECT 1 FROM json_each(COALESCE("
        f"{column}, '[]')) j WHERE json_extract(j.value, '$.{json_field}') "
        f"IN ({placeholders}))",
        list(values),
    )


def _quantity_clause(
    *,
    prop_id: str | None,
    var_id: str | None,
    constr_id: str | None,
) -> tuple[str, list[Any]]:
    pieces: list[str] = []
    params: list[Any] = []
    if prop_id is not None:
        sql, values = _json_role_exists(
            "br.prop_ids_meas_ranges", "prop_num_id", (prop_id,)
        )
        pieces.append(sql)
        params.extend(values)
    if var_id is not None:
        sql, values = _json_role_exists(
            "br.var_ids_ranges", "var_num_id", (var_id,)
        )
        pieces.append(sql)
        params.extend(values)
    if constr_id is not None:
        sql, values = _json_role_exists(
            "br.constr_ids_values", "constr_num_id", (constr_id,)
        )
        pieces.append(sql)
        params.extend(values)
    if not pieces:
        raise ValueError("quantity has no registry role ID")
    return "(" + " OR ".join(pieces) + ")", params


def _target_quantity_clause(target) -> tuple[str, list[Any]]:
    """Accept the direct target or any registered deterministic bridge."""
    pieces: list[str] = []
    params: list[Any] = []
    property_ids = tuple(
        value
        for value in target.evidence_global_ids
        if value.startswith("GLOBprop_")
    )
    if property_ids:
        sql, values = _json_role_exists(
            "br.prop_ids_meas_ranges", "prop_num_id", property_ids
        )
        pieces.append(sql)
        params.extend(values)
    if target.var_num_id is not None:
        sql, values = _json_role_exists(
            "br.var_ids_ranges", "var_num_id", (target.var_num_id,)
        )
        pieces.append(sql)
        params.extend(values)
    if target.constr_num_id is not None:
        sql, values = _json_role_exists(
            "br.constr_ids_values", "constr_num_id", (target.constr_num_id,)
        )
        pieces.append(sql)
        params.extend(values)
    if not pieces:
        raise ValueError("ranking target has no searchable registry evidence ID")
    return "(" + " OR ".join(pieces) + ")", params


def _range_overlap_exists(
    column: str,
    id_field: str,
    values: tuple[str, ...],
    minimum: float,
    maximum: float,
    *,
    fixed_value: bool = False,
) -> tuple[str, list[Any]]:
    placeholders = ",".join("?" for _ in values)
    if fixed_value:
        numeric_path = "$.value"
        numeric_clause = (
            f"CAST(json_extract(j.value, '{numeric_path}') AS REAL) "
            "BETWEEN ? AND ?"
        )
    else:
        numeric_clause = (
            "CAST(json_extract(j.value, '$.range.min') AS REAL) <= ? "
            "AND CAST(json_extract(j.value, '$.range.max') AS REAL) >= ?"
        )
    return (
        "EXISTS (SELECT 1 FROM json_each(COALESCE("
        f"{column}, '[]')) j WHERE json_extract(j.value, '$.{id_field}') "
        f"IN ({placeholders}) AND {numeric_clause})",
        [*values, minimum, maximum] if fixed_value else [*values, maximum, minimum],
    )


def _constraint_range_clause(
    constraint: ConstraintSpec,
) -> tuple[str, list[Any]]:
    roles = (
        (
            "br.prop_ids_meas_ranges",
            "prop_num_id",
            "GLOBprop_",
            False,
        ),
        ("br.var_ids_ranges", "var_num_id", "GLOBvar_", False),
        (
            "br.constr_ids_values",
            "constr_num_id",
            "GLOBconstr_",
            True,
        ),
    )
    pieces: list[str] = []
    params: list[Any] = []
    for column, id_field, prefix, fixed_value in roles:
        global_ids = tuple(
            value
            for value in constraint.available_global_ids
            if value.startswith(prefix)
        )
        if not global_ids:
            continue
        clause, values = _range_overlap_exists(
            column,
            id_field,
            global_ids,
            constraint.effective_minimum,
            constraint.effective_maximum,
            fixed_value=fixed_value,
        )
        pieces.append(clause)
        params.extend(values)
    if not pieces:
        raise ValueError(
            f"constraint {constraint.quantity_key!r} has no registry role ID"
        )
    return "(" + " OR ".join(pieces) + ")", params

def _base_clauses(
    request: NormalizedRequest,
    *,
    subsystem: bool,
) -> tuple[list[str], list[Any]]:
    clauses: list[str] = []
    params: list[Any] = []
    for target in request.targets:
        clause, values = _target_quantity_clause(target)
        clauses.append(clause)
        params.extend(values)
    for constraint in request.constraints:
        clause, values = _constraint_range_clause(constraint)
        clauses.append(clause)
        params.extend(values)
    if subsystem:
        clauses.append("bs.search_eligible = 1")
        for comp_num_id in request.center_comp_num_ids:
            clauses.append(
                "EXISTS (SELECT 1 FROM block_subsystem_compounds bsc "
                "WHERE bsc.doi=bs.doi AND bsc.block_number=bs.block_number "
                "AND bsc.BLKsubsys_id=bs.BLKsubsys_id "
                "AND bsc.component_role='retained' AND bsc.comp_num_id=?)"
            )
            params.append(comp_num_id)
        if request.system_type is not None:
            clauses.append("bs.effective_system_type = ?")
            params.append(request.system_type)
    else:
        for comp_num_id in request.center_comp_num_ids:
            clause, values = _json_role_exists(
                "br.comp_ids_smiles", "comp_num_id", (comp_num_id,)
            )
            clauses.append(clause)
            params.extend(values)
        if request.system_type is not None:
            clauses.append("br.system_type = ?")
            params.append(request.system_type)
    return clauses, params


def _iter_registry_rows(
    connection: sqlite3.Connection,
    request: NormalizedRequest,
    *,
    subsystem: bool,
) -> Iterator[sqlite3.Row]:
    clauses, params = _base_clauses(request, subsystem=subsystem)
    cursor_doi = ""
    cursor_block = ""
    cursor_subsystem = ""
    while True:
        local_clauses = list(clauses)
        local_params = list(params)
        if subsystem:
            local_clauses.append(
                "(br.doi > ? OR (br.doi = ? AND br.block_number > ?) "
                "OR (br.doi = ? AND br.block_number = ? "
                "AND bs.BLKsubsys_id > ?))"
            )
            local_params.extend(
                [
                    cursor_doi,
                    cursor_doi,
                    cursor_block,
                    cursor_doi,
                    cursor_block,
                    cursor_subsystem,
                ]
            )
            sql = (
                "SELECT br.doi,br.lit_num_id,br.block_number,br.block_type,"
                "br.system_type AS declared_system_type,br.n_datapoints,"
                "br.var_ids_ranges,br.constr_ids_values,"
                "bs.BLKsubsys_id,bs.effective_system_type,bs.n_points,"
                "(SELECT json_group_array(comp_num_id) FROM "
                "(SELECT bsc.comp_num_id FROM block_subsystem_compounds bsc "
                "WHERE bsc.doi=bs.doi AND bsc.block_number=bs.block_number "
                "AND bsc.BLKsubsys_id=bs.BLKsubsys_id "
                "AND bsc.component_role='retained' "
                "ORDER BY bsc.comp_num_id)) AS retained_comp_ids "
                "FROM block_registry br JOIN block_subsystems bs "
                "ON bs.doi=br.doi AND bs.block_number=br.block_number "
                "WHERE "
                + " AND ".join(local_clauses)
                + " ORDER BY br.doi,br.block_number,bs.BLKsubsys_id LIMIT ?"
            )
        else:
            local_clauses.append(
                "(br.doi > ? OR (br.doi = ? AND br.block_number > ?))"
            )
            local_params.extend([cursor_doi, cursor_doi, cursor_block])
            sql = (
                "SELECT br.doi,br.lit_num_id,br.block_number,br.block_type,"
                "br.system_type AS declared_system_type,br.n_datapoints,"
                "br.var_ids_ranges,br.constr_ids_values,"
                "br.comp_ids_smiles FROM block_registry br WHERE "
                + " AND ".join(local_clauses)
                + " ORDER BY br.doi,br.block_number LIMIT ?"
            )
        local_params.append(DISCOVERY_PAGE_SIZE)
        rows = connection.execute(sql, local_params).fetchall()
        if not rows:
            return
        for row in rows:
            yield row
        last = rows[-1]
        cursor_doi = last["doi"]
        cursor_block = last["block_number"]
        cursor_subsystem = last["BLKsubsys_id"] if subsystem else ""


def _declared_quantity_ids(row: sqlite3.Row) -> tuple[str, ...]:
    values: set[str] = set()
    for column, field in (
        ("var_ids_ranges", "var_num_id"),
        ("constr_ids_values", "constr_num_id"),
    ):
        for item in json.loads(row[column] or "[]"):
            if isinstance(item, dict) and isinstance(item.get(field), str):
                values.add(item[field])
    return tuple(sorted(values))


def _declared_candidate(row: sqlite3.Row) -> CandidateRef:
    compound_rows = json.loads(row["comp_ids_smiles"])
    comp_ids = tuple(
        item["comp_num_id"]
        for item in compound_rows
        if isinstance(item, dict) and item.get("comp_num_id")
    )
    quantity_ids = _declared_quantity_ids(row)
    return CandidateRef(
        doi=row["doi"],
        lit_num_id=row["lit_num_id"],
        block_number=row["block_number"],
        BLKsubsys_id=None,
        search_scope="declared",
        block_type=row["block_type"],
        declared_system_type=row["declared_system_type"],
        effective_system_type=row["declared_system_type"],
        comp_num_ids=comp_ids,
        n_datapoints=int(row["n_datapoints"]),
        declared_quantity_ids=quantity_ids,
    )


def _subsystem_candidate(row: sqlite3.Row) -> CandidateRef:
    comp_ids = tuple(json.loads(row["retained_comp_ids"] or "[]"))
    return CandidateRef(
        doi=row["doi"],
        lit_num_id=row["lit_num_id"],
        block_number=row["block_number"],
        BLKsubsys_id=row["BLKsubsys_id"],
        search_scope="subsystem",
        block_type=row["block_type"],
        declared_system_type=row["declared_system_type"],
        effective_system_type=row["effective_system_type"],
        comp_num_ids=comp_ids,
        n_datapoints=int(row["n_points"]),
        declared_quantity_ids=_declared_quantity_ids(row),
    )


def discover_candidates(request: NormalizedRequest) -> DiscoveryResult:
    """Read every coarse match using keyset pagination.

    ``request.limit`` is deliberately ignored here.  It applies only after
    numerical comparison and ranking, so discovery never silently truncates
    the chemical search space.
    """
    if not PM_REGISTRY_DB.is_file():
        raise FileNotFoundError(PM_REGISTRY_DB)
    connection = open_db(str(PM_REGISTRY_DB))
    try:
        unique: dict[tuple[str, str, str | None], CandidateRef] = {}
        rows_examined = 0
        declared_count = 0
        subsystem_count = 0
        pages = 0
        if request.system_scope in {"declared", "either"}:
            page_rows = 0
            for row in _iter_registry_rows(connection, request, subsystem=False):
                rows_examined += 1
                page_rows += 1
                candidate = _declared_candidate(row)
                unique[
                    (candidate.doi, candidate.block_number, None)
                ] = candidate
                declared_count += 1
                if page_rows == DISCOVERY_PAGE_SIZE:
                    pages += 1
                    page_rows = 0
            if page_rows:
                pages += 1
        if request.system_scope in {"subsystem", "either"}:
            page_rows = 0
            for row in _iter_registry_rows(connection, request, subsystem=True):
                rows_examined += 1
                page_rows += 1
                candidate = _subsystem_candidate(row)
                unique[
                    (
                        candidate.doi,
                        candidate.block_number,
                        candidate.BLKsubsys_id,
                    )
                ] = candidate
                subsystem_count += 1
                if page_rows == DISCOVERY_PAGE_SIZE:
                    pages += 1
                    page_rows = 0
            if page_rows:
                pages += 1
    finally:
        connection.close()
    candidates = tuple(
        sorted(
            unique.values(),
            key=lambda item: (
                item.doi,
                item.block_number,
                item.BLKsubsys_id or "",
            ),
        )
    )
    return DiscoveryResult(
        candidates=candidates,
        pages_read=pages,
        registry_rows_examined=rows_examined,
        declared_count=declared_count,
        subsystem_count=subsystem_count,
    )
