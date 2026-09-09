"""
1_block_search.py — Search PCS_INDIV.db for detailed block-level data cards.

This is the most detailed search tool — it returns full block data including
compounds, properties, variables, constraints, and data summaries from
individual papers.  Supports multi-criteria filtering with a two-phase
approach for efficiency:

Phase 1: Query PureOrMixtureData_registry.db (indexed, 122 K rows) to narrow
          candidate DOIs and block numbers.
Phase 2: Load matching PCS_INDIV cards and extract specific blocks.

Public API
----------
    search_blocks(compound=None, property=None, measurement=None,
                  literature=None, system_type=None, phase=None,
                  temperature_range=None, pressure_range=None, limit=50,
                  block_number=None)
        -> dict
"""

import json
import logging
import re
import sqlite3
import sys
import os

log = logging.getLogger("block-search")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _id_alignment_search import (
    resolve_compound_ids,
    resolve_property_ids,
    resolve_measurement_ids,
    resolve_phase_ids,
    resolve_reference_ids,
)
from normalization_helpers.paths import card_db_path, registry_db_path
from normalization_helpers.compact import compact_block
from normalization_helpers.range_helpers import validate_range, ranges_overlap
from normalization_helpers.db_helpers import open_db, project_pcs_block_target
from normalization_helpers.strict_id_inputs import (
    IdentifierRefinementError,
    refinement_errors_as_results,
    require_typed_block_input,
    SearchValue,
)

# ═════════════════════════════════════════════════════════════════════════════
# Internal paths
# ═════════════════════════════════════════════════════════════════════════════

_PCS_DB = card_db_path("PCS_INDIV")
_PM_REGISTRY = registry_db_path("PM_REGISTRY")
_RXN_REGISTRY = registry_db_path("RXN_REGISTRY")


# ═════════════════════════════════════════════════════════════════════════════
# Helpers — range overlap  (delegated to normalization_helpers.range_helpers)
# ═════════════════════════════════════════════════════════════════════════════


_ranges_overlap = ranges_overlap


# ═════════════════════════════════════════════════════════════════════════════
# Phase 1 — Registry pre-filter
# ═════════════════════════════════════════════════════════════════════════════

def _registry_prefilter(
    comp_ids: set[str],
    prop_num_ids: set[str],
    prop_ids_str: set[str],
    meas_num_ids: set[str],
    phase_ids: set[str],
    system_type: str | None,
    doi: str | None,
    temperature_range: tuple | None,
    pressure_range: tuple | None,
    limit: int,
) -> list[tuple[str, str]]:
    """Query all available block registries for scoped block identities.

    Both canonical block registries are required. Returns scoped
    ``(doi, block_number)`` pairs or raises when either registry cannot be
    queried.
    """
    registry_paths = (_PM_REGISTRY, _RXN_REGISTRY)
    missing = [path for path in registry_paths if not os.path.exists(path)]
    if missing:
        raise FileNotFoundError(f"Required block registries are missing: {missing}")

    clauses: list[str] = []
    params: list = []

    if doi is not None:
        clauses.append("doi = ?")
        params.append(doi)

    if system_type is not None:
        clauses.append("system_type = ?")
        params.append(system_type)

    # Registry columns are JSON arrays of objects.  Match a complete JSON
    # key/value pair so GLOBcomp_2 cannot collide with GLOBcomp_20.
    # Use AND so multi-compound queries (e.g. "ethanol, water") return
    # blocks containing ALL specified compounds, not just any one.
    # Quote the JSON global-ID value so GLOBcomp_2 cannot match GLOBcomp_299.
    if comp_ids:
        for cid in comp_ids:
            clauses.append("comp_ids_smiles LIKE ?")
            params.append(f'%"comp_num_id":"{cid}"%')

    # Property and measurement IDs are canonical global IDs in object fields.
    if prop_num_ids:
        prop_likes = ["prop_ids_meas_ranges LIKE ?" for _ in prop_num_ids]
        clauses.append("(" + " OR ".join(prop_likes) + ")")
        for pid in prop_num_ids:
            params.append(f'%"prop_num_id":"{pid}"%')

    if meas_num_ids:
        meas_likes = ["prop_ids_meas_ranges LIKE ?" for _ in meas_num_ids]
        clauses.append("(" + " OR ".join(meas_likes) + ")")
        for mid in meas_num_ids:
            params.append(f'%"meas_num_id":"{mid}"%')

    # Phase: LIKE on prop_phase_ids
    if phase_ids:
        ph_likes = ["prop_phase_ids LIKE ?" for _ in phase_ids]
        clauses.append("(" + " OR ".join(ph_likes) + ")")
        for phid in phase_ids:
            params.append(f"%{phid}%")

    sql = "SELECT doi, block_number FROM block_registry"
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    # Fetch more than limit because temperature/pressure post-filtering
    # may discard some rows
    fetch_limit = limit * 10 if (temperature_range or pressure_range) else limit * 3
    sql += f" LIMIT {int(fetch_limit)}"

    found: list[tuple[str, str]] = []
    for registry_path in registry_paths:
        conn = open_db(registry_path)
        try:
            rows = conn.execute(sql, params).fetchall()
            found.extend((r["doi"], r["block_number"]) for r in rows)
        finally:
            conn.close()
    return list(dict.fromkeys(found))


def _subsystem_registry_prefilter(
    comp_ids: set[str],
    prop_num_ids: set[str],
    prop_ids_str: set[str],
    meas_num_ids: set[str],
    phase_ids: set[str],
    system_type: str | None,
    doi: str | None,
    limit: int,
) -> list[tuple[str, str, str]]:
    """Query normalized, search-eligible PCS subsystem projections."""
    if not os.path.exists(_PM_REGISTRY):
        raise FileNotFoundError(f"Required block registry is missing: {_PM_REGISTRY}")
    clauses = ["s.search_eligible = 1"]
    params: list[object] = []
    if doi is not None:
        clauses.append("s.doi = ?")
        params.append(doi)
    if system_type is not None:
        clauses.append("s.effective_system_type = ?")
        params.append(system_type)
    for comp_id in sorted(comp_ids):
        clauses.append(
            "EXISTS (SELECT 1 FROM block_subsystem_compounds sc "
            "WHERE sc.doi=s.doi AND sc.block_number=s.block_number "
            "AND sc.BLKsubsys_id=s.BLKsubsys_id "
            "AND sc.component_role='retained' AND sc.comp_num_id=?)"
        )
        params.append(comp_id)
    if prop_num_ids or prop_ids_str:
        alternatives = []
        for prop_num_id in sorted(prop_num_ids):
            alternatives.append("sp.prop_num_id = ?")
            params.append(prop_num_id)
        for prop_id in sorted(prop_ids_str):
            alternatives.append("sp.prop_ID = ?")
            params.append(prop_id)
        clauses.append(
            "EXISTS (SELECT 1 FROM block_subsystem_properties sp "
            "WHERE sp.doi=s.doi AND sp.block_number=s.block_number "
            "AND sp.BLKsubsys_id=s.BLKsubsys_id "
            "AND sp.support_role='bulk_property' AND sp.phase_compatible=1 "
            "AND (" + " OR ".join(alternatives) + "))"
        )
    for meas_num_id in sorted(meas_num_ids):
        clauses.append("b.prop_ids_meas_ranges LIKE ?")
        params.append(f'%"meas_num_id":"{meas_num_id}"%')
    for phase_id in sorted(phase_ids):
        clauses.append("s.scope_json LIKE ?")
        params.append(f'%"phase_id":"{phase_id}"%')
    sql = (
        "SELECT DISTINCT s.doi, s.block_number, s.BLKsubsys_id "
        "FROM block_subsystems s JOIN block_registry b "
        "ON b.doi=s.doi AND b.block_number=s.block_number WHERE "
        + " AND ".join(clauses)
        + " ORDER BY s.doi, s.block_number, s.BLKsubsys_id LIMIT ?"
    )
    params.append(limit * 10)
    conn = open_db(_PM_REGISTRY)
    try:
        return [tuple(row) for row in conn.execute(sql, params).fetchall()]
    finally:
        conn.close()


def _subsystems_for_block(card: dict, block: dict) -> list[dict]:
    manifests = card["blocks_summary"]["derived_indexes"]["composition_subsystems"]
    block_number = block["block_number"]
    if block_number not in manifests:
        raise ValueError(
            f"PCS composition_subsystems is missing {card['key']['doi']!r} "
            f"{block_number!r}"
        )
    return manifests[block_number]


def _search_targets(card: dict, block: dict, system_scope: str):
    if system_scope in {"declared", "either"}:
        yield None
    if system_scope in {"subsystem", "either"}:
        yield from (
            subsystem
            for subsystem in _subsystems_for_block(card, block)
            if subsystem["search_eligible"]
        )


# ═════════════════════════════════════════════════════════════════════════════
# Phase 2 — Block-level matching on PCS_INDIV JSON
# ═════════════════════════════════════════════════════════════════════════════

def _block_matches(
    block: dict,
    card: dict,
    comp_num_id_set: set[str],
    prop_num_id_set: set[str],
    prop_id_set: set[str],
    meas_num_id_set: set[str],
    phase_id_set: set[str],
    system_type: str | None,
    temperature_range: tuple | None,
    pressure_range: tuple | None,
    subsystem: dict | None = None,
) -> tuple[int, list[str]]:
    """Score a single block against all provided criteria.

    Returns (match_score 0-100, list_of_matched_criteria).
    A score of 0 means the block does NOT satisfy the mandatory filters.
    """
    criteria_total = 0
    criteria_met = 0
    matched: list[str] = []
    subsystem_property_ids = None
    if subsystem is not None:
        subsystem_property_ids = {
            support["BLKprop_id"]
            for support in subsystem["property_support"]
            if support["role"] == "bulk_property" and support["phase_compatible"]
        }

    # ── compound ─────────────────────────────────────────────────────────
    comp_overlap = 0.0          # fraction of query compounds found in block
    if comp_num_id_set:
        criteria_total += 1
        searchable_compounds = (
            subsystem["retained_components"]
            if subsystem is not None else block["compounds"]
        )
        block_comp_ids = {c["comp_num_id"] for c in searchable_compounds}
        overlap = block_comp_ids & comp_num_id_set
        if comp_num_id_set.issubset(block_comp_ids):
            criteria_met += 1
            comp_overlap = 1.0
            matched.append("compound")
        else:
            return 0, []

    # ── property ─────────────────────────────────────────────────────────
    if prop_num_id_set or prop_id_set:
        criteria_total += 1
        block_prop_num_ids = set()
        block_prop_ids = set()
        for p in block["properties"]:
            if subsystem_property_ids is not None and p["BLKprop_id"] not in subsystem_property_ids:
                continue
            block_prop_num_ids.add(p["prop_num_id"])
            block_prop_ids.add(p["prop_ID"])
        if (block_prop_num_ids & prop_num_id_set) or (block_prop_ids & prop_id_set):
            criteria_met += 1
            matched.append("property")
        else:
            return 0, []

    # ── measurement ──────────────────────────────────────────────────────
    if meas_num_id_set:
        criteria_total += 1
        block_meas_ids = set()
        for p in block["properties"]:
            if subsystem_property_ids is not None and p["BLKprop_id"] not in subsystem_property_ids:
                continue
            block_meas_ids.add(p["meas_num_id"])
        if block_meas_ids & meas_num_id_set:
            criteria_met += 1
            matched.append("measurement")
        else:
            return 0, []

    # ── system_type ──────────────────────────────────────────────────────
    if system_type is not None:
        criteria_total += 1
        target_system_type = (
            subsystem["effective_system_type"]
            if subsystem is not None else block["system_type"]
        )
        if system_type == target_system_type:
            criteria_met += 1
            matched.append("system_type")
        else:
            return 0, []

    # ── phase ────────────────────────────────────────────────────────────
    if phase_id_set:
        criteria_total += 1
        block_phase_ids = set()
        if subsystem is not None and subsystem["scope"]["phase_id"]:
            block_phase_ids.add(subsystem["scope"]["phase_id"])
        for p in block["properties"]:
            if subsystem_property_ids is not None and p["BLKprop_id"] not in subsystem_property_ids:
                continue
            pp = p["property_phase"]
            if isinstance(pp, dict) and pp["phase_id"]:
                block_phase_ids.add(pp["phase_id"])
        if block_phase_ids & phase_id_set:
            criteria_met += 1
            matched.append("phase")
        else:
            return 0, []

    # ── temperature_range ────────────────────────────────────────────────
    if temperature_range is not None:
        criteria_total += 1
        found_temp = False
        for p in block["properties"]:
            temperature = p["temperature_K"]
            if temperature is not None and _ranges_overlap(
                [temperature, temperature], temperature_range
            ):
                found_temp = True
                break
        if not found_temp:
            range_infos = (
                subsystem["condition_ranges"]
                if subsystem is not None
                else block["data_summary"]["variable_ranges"].values()
            )
            for vinfo in range_infos:
                range_name = str(vinfo["name"]).lower()
                if "temperature" in range_name or "temp" in range_name:
                    sr_min = vinfo["min"]
                    sr_max = vinfo["max"]
                    if sr_min is not None and sr_max is not None:
                        if _ranges_overlap([sr_min, sr_max], temperature_range):
                            found_temp = True
                            break
        if not found_temp:
            for constraint in block["constraints"]:
                if str(constraint["constr_id"]).startswith("temperature_k"):
                    value = constraint["value"]
                    if value is not None and _ranges_overlap([value, value], temperature_range):
                        found_temp = True
                        break
        if found_temp:
            criteria_met += 1
            matched.append("temperature")
        else:
            return 0, []

    # ── pressure_range ───────────────────────────────────────────────────
    if pressure_range is not None:
        criteria_total += 1
        found_pres = False
        for p in block["properties"]:
            pressure = p["pressure_kPa"]
            if pressure is not None and _ranges_overlap([pressure, pressure], pressure_range):
                found_pres = True
                break
        if not found_pres:
            range_infos = (
                subsystem["condition_ranges"]
                if subsystem is not None
                else block["data_summary"]["variable_ranges"].values()
            )
            for vinfo in range_infos:
                if "pressure" in str(vinfo["name"]).lower():
                    sr_min = vinfo["min"]
                    sr_max = vinfo["max"]
                    if sr_min is not None and sr_max is not None:
                        if _ranges_overlap([sr_min, sr_max], pressure_range):
                            found_pres = True
                            break
        if not found_pres:
            for constraint in block["constraints"]:
                if str(constraint["constr_id"]).startswith("pressure_kpa"):
                    value = constraint["value"]
                    if value is not None and _ranges_overlap([value, value], pressure_range):
                        found_pres = True
                        break
        if found_pres:
            criteria_met += 1
            matched.append("pressure")
        else:
            return 0, []

    # ── score ────────────────────────────────────────────────────────────
    if criteria_total == 0:
        return 50, ["browse"]
    base_score = int(100 * criteria_met / criteria_total)
    # Boost blocks that match ALL queried compounds (not just some)
    if comp_num_id_set and comp_overlap < 1.0:
        # Partial compound match: scale down by overlap fraction
        base_score = max(1, int(base_score * (0.3 + 0.7 * comp_overlap)))
        matched.append(f"compound_overlap={comp_overlap:.0%}")
    return base_score, matched


def _subsystem_data_summary(block: dict, subsystem: dict, projected: dict) -> dict:
    condition_ranges = {
        item["BLKvar_id"]: {
            "BLKvar_id": item["BLKvar_id"],
            "name": item["name"],
            "min": item["min"],
            "max": item["max"],
            "n_unique": item["n"],
        }
        for item in subsystem["condition_ranges"]
    }
    phases = sorted({
        value
        for value in (
            subsystem["scope"].get("phase_id"),
            *((item.get("property_phase") or {}).get("phase_id")
              for item in projected["properties"]),
        )
        if value
    })
    return {
        "property_names": [item["name"] for item in projected["properties"]],
        "property_group": sorted({
            item["group"] for item in projected["properties"]
        }),
        "methods": sorted({
            item["meas_ID"] for item in projected["properties"]
            if item["meas_ID"]
        }),
        "system_type": subsystem["effective_system_type"],
        "compound_names": [item["name"] for item in projected["compounds"]],
        "phases": phases,
        "constraints_summary": {
            item["BLKconstr_id"]: item for item in projected["constraints"]
        },
        "n_points": subsystem["n_points"],
        "property_stats": {},
        "variable_ranges": condition_ranges,
        "effective_system_summary": {
            "n_subsystems": 0,
            "system_types": [],
            "n_search_eligible": 0,
            "n_unique_points": 0,
        },
        "range_scope": (
            "exact subsystem condition ranges; raw extraction required for "
            "property/composition ranges"
        ),
    }


def _compact_subsystem_target(block: dict, subsystem: dict, projected: dict) -> str:
    retained = ", ".join(
        f'{item["comp_num_id"]} ({item["name"]})'
        for item in subsystem["retained_components"]
    )
    excluded = ", ".join(
        f'{item["comp_num_id"]} ({item["name"]})'
        for item in subsystem["excluded_components"]
    ) or "none"
    properties = ", ".join(
        f'{item["BLKprop_id"]}={item["prop_num_id"]}:{item["prop_ID"]}'
        for item in projected["properties"]
    ) or "none"
    variables = ", ".join(
        f'{item["BLKvar_id"]}={item["var_num_id"]}:{item["var_id"]}'
        for item in projected["variables"]
    ) or "none"
    conditions = ", ".join(
        f'{item["BLKvar_id"]} {item["min"]}..{item["max"]} ({item["n"]} points)'
        for item in subsystem["condition_ranges"]
    ) or "none"
    return "\n".join([
        f'## {block["block_number"]} / {subsystem["BLKsubsys_id"]}',
        (
            f'**Target:** {subsystem["effective_system_type"]} composition '
            f'subsystem; {subsystem["n_points"]} raw points'
        ),
        (
            f'**Declared parent:** {block["system_type"]}; '
            f'{block["data_summary"]["n_points"]} raw points'
        ),
        f"**Retained compounds:** {retained}",
        f"**Excluded by exact reported zero:** {excluded}",
        (
            f'**Evidence:** {subsystem["evidence_quality"]} via '
            f'{", ".join(subsystem["evidence_sources"])}'
        ),
        f"**Properties:** {properties}",
        f"**Active variables:** {variables}",
        f"**Condition ranges:** {conditions}",
    ]) + "\n"


def _extract_block_result(
    card: dict,
    block: dict,
    match_score: int,
    match_criteria: list[str],
    subsystem: dict | None = None,
) -> dict:
    """Build one declared-block or embedded-subsystem search result."""
    key = card["key"]
    paper = card["paper"]
    parent_summary = block["data_summary"]
    projected = project_pcs_block_target(block, subsystem)
    if subsystem is None:
        system_type = block["system_type"]
        n_datapoints = parent_summary["n_points"]
        subsystem_id = None
        search_scope = "declared"
        data_summary = parent_summary
        compact_md = compact_block(
            block, key_info={**key, "title": paper["title"]}
        )
    else:
        system_type = subsystem["effective_system_type"]
        n_datapoints = subsystem["n_points"]
        subsystem_id = subsystem["BLKsubsys_id"]
        search_scope = "subsystem"
        data_summary = _subsystem_data_summary(block, subsystem, projected)
        compact_md = _compact_subsystem_target(block, subsystem, projected)
    return {
        "doi": key["doi"],
        "lit_num_id": key["lit_num_id"],
        "paper_title": paper["title"],
        "block_number": block["block_number"],
        "BLKsubsys_id": subsystem_id,
        "search_scope": search_scope,
        "block_type": block["block_type"],
        "system_type": system_type,
        "declared_system_type": block["system_type"],
        "compounds": projected["compounds"],
        "declared_compounds": block["compounds"],
        "properties": projected["properties"],
        "solvents": projected["solvents"],
        "variables": projected["variables"],
        "constraints": projected["constraints"],
        "data_summary": data_summary,
        "n_datapoints": n_datapoints,
        "parent_n_datapoints": parent_summary["n_points"],
        "matched_subsystem": subsystem,
        "compact_md": compact_md,
        "match_score": match_score,
        "match_criteria": match_criteria,
    }


def _evaluate_card(
    card,
    *,
    allowed_targets,
    block_filter=None,
    system_scope,
    comp_num_id_set,
    prop_num_id_set,
    prop_id_set,
    meas_num_id_set,
    phase_id_set,
    system_type,
    t_range,
    p_range,
    limit,
    doi_matched=False,
):
    results = []
    has_filters = any([
        comp_num_id_set, prop_num_id_set, meas_num_id_set,
        phase_id_set, system_type, t_range, p_range,
    ])
    for block in card["blocks"]:
        block_number = block["block_number"]
        if block_filter is not None and block_number != block_filter:
            continue
        if allowed_targets is not None and block_number not in allowed_targets:
            continue
        for subsystem in _search_targets(card, block, system_scope):
            target_id = None if subsystem is None else subsystem["BLKsubsys_id"]
            if (
                allowed_targets is not None
                and target_id not in allowed_targets[block_number]
            ):
                continue
            score, matched = _block_matches(
                block, card,
                comp_num_id_set, prop_num_id_set, prop_id_set,
                meas_num_id_set, phase_id_set,
                system_type, t_range, p_range, subsystem,
            )
            if score <= 0 and has_filters:
                continue
            if score <= 0:
                score, matched = 50, ["browse"]
            if doi_matched:
                matched = ["doi"] + matched
                score = max(score, 80)
            results.append(
                _extract_block_result(card, block, score, matched, subsystem)
            )
            if len(results) >= limit:
                return results
    return results


# ═════════════════════════════════════════════════════════════════════════════
# Public API
# ═════════════════════════════════════════════════════════════════════════════

@refinement_errors_as_results
def search_blocks(
    compound: SearchValue = None,
    property: SearchValue = None,
    measurement: SearchValue = None,
    literature: SearchValue = None,
    system_type: str | None = None,
    system_scope: str = "declared",
    phase: SearchValue = None,
    temperature_range: list[float] | None = None,
    pressure_range: list[float] | None = None,
    limit: int = 50,
    block_number: str | None = None,
) -> dict:
    """Search PCS_INDIV.db for data blocks matching multi-criteria filters.

    Entity parameters accept one name/canonical ``GLOB*`` ID or a native list
    of those strings. Bare numeric and retired unscoped IDs
    are deliberately not interpreted as identifiers.

    A block-targeted call (``block_number``) is the query-side way to
    inspect one already-identified block: the matched block returns its
    full detail view including the RDP-simplified data-points table
    (complete for blocks with \u22648 points, a shape-preserving subset for
    large ones).

    Parameters
    ----------
    compound : str | list, optional
        Compound name, formula, SMILES, InChI, InChI-key, comp_num_id,
        or ``GLOBcomp_N``.  Semicolon-separated for multiple.
    property : str | list, optional
        Property name, prop_id, or ``GLOBprop_N``.
    measurement : str | list, optional
        Measurement method name, meas_id, or ``GLOBmeas_N``.
    literature : str | list, optional
        DOI, lit_id, or lit_num_id.
    block_number : str, optional
        Target ONE block for inspection. Block numbers repeat across
        papers, so the literature scope is mandatory: pass the qualified
        form ``GLOBlit_N::PROPblock_M`` (or ``::RXNblock_M``), or a bare
        ``PROPblock_M`` together with ``literature``.
    system_type : str, optional
        ``"pure"``, ``"binary"``, ``"ternary"``, etc.
    phase : str | list, optional
        Phase name, phase_id, or ``GLOBphase_N``.
    temperature_range : tuple/list (min_K, max_K), optional
        Find blocks whose temperature data overlaps this range.
    pressure_range : tuple/list (min_kPa, max_kPa), optional
        Find blocks whose pressure data overlaps this range.
    limit : int
        Maximum result blocks returned (default 50).

    Returns
    -------
    dict
        ``query_params`` – echo of input parameters.
        ``n_results``    – number of matching blocks.
        ``results``      – list of block result dicts with match_score.
    """
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise TypeError(
            "TOOL_ARGUMENT_REFINEMENT_REQUIRED: limit must be a positive integer; "
            "values are never coerced"
        )
    if system_type is not None and (
        not isinstance(system_type, str)
        or not re.fullmatch(r"(?:unary|binary|ternary|quaternary|(?:[5-9]|[1-9][0-9]+)-component)", system_type)
    ):
        raise ValueError(
            "system_type must use the exact registry value: unary, binary, "
            "ternary, quaternary, or N-component"
        )
    if system_scope not in {"declared", "subsystem", "either"}:
        raise ValueError(
            "system_scope must be exactly 'declared', 'subsystem', or 'either'"
        )

    # ── Targeted block: literature-scoped, never bare across papers ─────
    block_filter: str | None = None
    if block_number is not None:
        if not isinstance(block_number, str):
            raise IdentifierRefinementError(
                "block_number", block_number,
                "GLOBlit_<N>::PROPblock_<M> or PROPblock_<M> with literature=",
                "block targeting takes one typed string",
            )
        candidate = block_number.strip()
        if "::" in candidate:
            lit_part, _, block_part = candidate.partition("::")
            lit_part, block_part = lit_part.strip(), block_part.strip()
            if not re.fullmatch(r"GLOBlit_[1-9]\d*", lit_part):
                raise IdentifierRefinementError(
                    "block_number", block_number,
                    "GLOBlit_<N>::PROPblock_<M> (or ::RXNblock_<M>)",
                    "the scope before '::' must be one GLOBlit id",
                )
            if literature is not None:
                raise IdentifierRefinementError(
                    "block_number", block_number,
                    "either GLOBlit_<N>::block form OR literature= + bare block",
                    "the literature scope was given twice",
                )
            block_filter = require_typed_block_input(
                block_part, field="block_number")
            literature = lit_part
        else:
            if literature is None:
                raise IdentifierRefinementError(
                    "block_number", block_number,
                    "GLOBlit_<N>::PROPblock_<M>, or literature= plus this bare id",
                    "block numbers repeat across papers and need a literature scope",
                )
            block_filter = require_typed_block_input(
                candidate, field="block_number")

    # ── Echo query params ────────────────────────────────────────────────
    query_params: dict = {}
    if compound is not None:
        query_params["compound"] = compound
    if property is not None:
        query_params["property"] = property
    if measurement is not None:
        query_params["measurement"] = measurement
    if literature is not None:
        query_params["literature"] = literature
    if block_filter is not None:
        # bare form only: qualified echoes would break the result-side
        # nested-identifier contract (block_number fields must be bare)
        query_params["block_number"] = block_filter
    if system_type is not None:
        query_params["system_type"] = system_type
    query_params["system_scope"] = system_scope
    if phase is not None:
        query_params["phase"] = phase
    if temperature_range is not None:
        query_params["temperature_range"] = list(temperature_range)
    if pressure_range is not None:
        query_params["pressure_range"] = list(pressure_range)
    query_params["limit"] = limit

    # ── Resolve inputs via id_alignment ──────────────────────────────────
    comp_candidates = resolve_compound_ids(compound) if compound is not None else []
    comp_num_id_set: set[str] = {c["comp_num_id"] for c in comp_candidates}
    if compound is not None and not comp_candidates:
        return {
            "query_params": query_params, "n_results": 0, "results": [],
            "note": f"Could not resolve compound '{compound}' to any known ID.",
        }

    prop_candidates = resolve_property_ids(property) if property is not None else []
    prop_num_id_set: set[str] = {p["prop_num_id"] for p in prop_candidates}
    prop_id_set: set[str] = {p["prop_id"] for p in prop_candidates}
    if property is not None and not prop_candidates:
        return {
            "query_params": query_params, "n_results": 0, "results": [],
            "note": f"Could not resolve property '{property}' to any known ID.",
        }

    meas_candidates = resolve_measurement_ids(measurement) if measurement is not None else []
    meas_num_id_set: set[str] = {m["meas_num_id"] for m in meas_candidates}
    if measurement is not None and not meas_candidates:
        return {
            "query_params": query_params, "n_results": 0, "results": [],
            "note": f"Could not resolve measurement '{measurement}' to any known ID.",
        }

    phase_candidates = resolve_phase_ids(phase) if phase is not None else []
    phase_id_set: set[str] = {p["phase_id"] for p in phase_candidates}
    if phase is not None and not phase_candidates:
        return {
            "query_params": query_params, "n_results": 0, "results": [],
            "note": f"Could not resolve phase '{phase}' to any known ID.",
        }

    # Resolve literature → DOI(s)
    doi: str | None = None
    if literature is not None:
        ref_hits = resolve_reference_ids(literature)
        if ref_hits:
            doi = ref_hits[0]["doi"]
        else:
            return {
                "query_params": query_params, "n_results": 0, "results": [],
                "note": f"Could not resolve literature '{literature}' to any known DOI.",
            }

    t_range = validate_range(temperature_range, field="temperature_range")
    p_range = validate_range(pressure_range, field="pressure_range")

    # ── Determine whether to use registry pre-filter ─────────────────────
    # If ONLY doi is given we can go direct to PCS_INDIV (fast path).
    # Otherwise use registry to narrow candidates first.
    use_registry = (doi is None) and any([
        comp_num_id_set, prop_num_id_set, meas_num_id_set,
        phase_id_set, system_type,
    ])

    results: list[dict] = []
    conn = open_db(_PCS_DB)

    try:
        if doi is not None:
            row = conn.execute(
                "SELECT json_data FROM cards WHERE doi = ?", (doi,)
            ).fetchone()
            if row:
                card = json.loads(row["json_data"])
                results.extend(_evaluate_card(
                    card,
                    allowed_targets=None,
                    block_filter=block_filter,
                    system_scope=system_scope,
                    comp_num_id_set=comp_num_id_set,
                    prop_num_id_set=prop_num_id_set,
                    prop_id_set=prop_id_set,
                    meas_num_id_set=meas_num_id_set,
                    phase_id_set=phase_id_set,
                    system_type=system_type,
                    t_range=t_range,
                    p_range=p_range,
                    limit=limit,
                    doi_matched=True,
                ))
        elif use_registry:
            candidates: list[tuple[str, str, str | None]] = []
            if system_scope in {"declared", "either"}:
                candidates.extend(
                    (candidate_doi, block_number, None)
                    for candidate_doi, block_number in _registry_prefilter(
                        comp_num_id_set, prop_num_id_set, prop_id_set,
                        meas_num_id_set, phase_id_set,
                        system_type, None, t_range, p_range, limit,
                    )
                )
            if system_scope in {"subsystem", "either"}:
                candidates.extend(_subsystem_registry_prefilter(
                    comp_num_id_set, prop_num_id_set, prop_id_set,
                    meas_num_id_set, phase_id_set,
                    system_type, None, limit,
                ))

            allowed_by_doi: dict[str, dict[str, set[str | None]]] = {}
            for candidate_doi, block_number, subsystem_id in candidates:
                allowed_by_doi.setdefault(candidate_doi, {}).setdefault(
                    block_number, set()
                ).add(subsystem_id)
            for candidate_doi, allowed_targets in allowed_by_doi.items():
                if len(results) >= limit:
                    break
                row = conn.execute(
                    "SELECT json_data FROM cards WHERE doi = ?", (candidate_doi,)
                ).fetchone()
                if not row:
                    continue
                card = json.loads(row["json_data"])
                results.extend(_evaluate_card(
                    card,
                    allowed_targets=allowed_targets,
                    system_scope=system_scope,
                    comp_num_id_set=comp_num_id_set,
                    prop_num_id_set=prop_num_id_set,
                    prop_id_set=prop_id_set,
                    meas_num_id_set=meas_num_id_set,
                    phase_id_set=phase_id_set,
                    system_type=system_type,
                    t_range=t_range,
                    p_range=p_range,
                    limit=limit - len(results),
                ))
        else:
            results = _full_scan(
                conn, comp_num_id_set, prop_num_id_set, prop_id_set,
                meas_num_id_set, phase_id_set, system_type,
                t_range, p_range, system_scope, limit,
            )
    finally:
        conn.close()

    # Sort by descending match score, then DOI for stability
    results.sort(key=lambda r: (-r["match_score"], r["doi"]))
    results = results[:limit]

    out = {
        "query_params": query_params,
        "n_results": len(results),
        "results": results,
    }
    if block_filter is not None and not results:
        out["note"] = (
            f"No {block_filter} under the resolved literature ({doi}) "
            "matched; check the block id or relax the other filters."
        )
    return out


def _full_scan(
    conn,
    comp_num_id_set: set[str],
    prop_num_id_set: set[str],
    prop_id_set: set[str],
    meas_num_id_set: set[str],
    phase_id_set: set[str],
    system_type: str | None,
    t_range: tuple | None,
    p_range: tuple | None,
    system_scope: str,
    limit: int,
) -> list[dict]:
    """Iterate PCS cards while preserving explicit search-target scope."""
    results: list[dict] = []
    cursor = conn.execute("SELECT json_data FROM cards")
    while len(results) < limit:
        row = cursor.fetchone()
        if row is None:
            break
        card = json.loads(row["json_data"])
        results.extend(_evaluate_card(
            card,
            allowed_targets=None,
            system_scope=system_scope,
            comp_num_id_set=comp_num_id_set,
            prop_num_id_set=prop_num_id_set,
            prop_id_set=prop_id_set,
            meas_num_id_set=meas_num_id_set,
            phase_id_set=phase_id_set,
            system_type=system_type,
            t_range=t_range,
            p_range=p_range,
            limit=limit - len(results),
        ))
    return results

# ═════════════════════════════════════════════════════════════════════════════
# Demo / smoke-test
# ═════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import pprint

    # ── 1. Search by compound name ───────────────────────────────────────
    print("=" * 70)
    print("Search: compound='water'")
    print("=" * 70)
    resp = search_blocks(compound="water", limit=10)
    print(f"  n_results: {resp['n_results']}")
    for r in resp["results"][:5]:
        comp_names = [c.get("name", "?") for c in r.get("compounds", [])]
        prop_names = [p.get("name", "?") for p in r.get("properties", [])]
        print(
            f"  doi={r['doi']}  block={r['block_number']}  "
            f"compounds={comp_names}  properties={prop_names[:2]}  "
            f"pts={r['n_datapoints']}  score={r['match_score']}  "
            f"criteria={r['match_criteria']}"
        )

    # ── 2. Search by compound + property ─────────────────────────────────
    print(f"\n{'=' * 70}")
    print("Search: compound='ethanol', property_name='density'")
    print("=" * 70)
    resp2 = search_blocks(compound="ethanol", property_name="density", limit=10)
    print(f"  n_results: {resp2['n_results']}")
    for r in resp2["results"][:5]:
        comp_names = [c.get("name", "?") for c in r.get("compounds", [])]
        prop_names = [p.get("name", "?") for p in r.get("properties", [])]
        print(
            f"  doi={r['doi']}  block={r['block_number']}  "
            f"compounds={comp_names}  properties={prop_names[:2]}  "
            f"pts={r['n_datapoints']}  score={r['match_score']}  "
            f"criteria={r['match_criteria']}"
        )

    # ── 3. DOI lookup ────────────────────────────────────────────────────
    test_doi = "10.1021/je049595u"
    if resp["results"]:
        test_doi = resp["results"][0]["doi"]
    print(f"\n{'=' * 70}")
    print(f"Search: doi='{test_doi}'")
    print("=" * 70)
    resp3 = search_blocks(doi=test_doi, limit=20)
    print(f"  n_results: {resp3['n_results']}")
    for r in resp3["results"][:5]:
        comp_names = [c.get("name", "?") for c in r.get("compounds", [])]
        prop_names = [p.get("name", "?") for p in r.get("properties", [])]
        print(
            f"  block={r['block_number']}  type={r['block_type']}  "
            f"compounds={comp_names}  properties={prop_names[:2]}  "
            f"pts={r['n_datapoints']}  score={r['match_score']}"
        )

    # ── 4. Full detail of one block ──────────────────────────────────────
    if resp2["results"]:
        print(f"\n{'=' * 70}")
        print("Full detail of first ethanol+density result:")
        print("=" * 70)
        pprint.pprint(resp2["results"][0], width=100)
