"""
9_system_summary_search.py — Aggregate statistical summary of data availability
for a given compound, property, or compound+property combination across the
entire ThermoML database.

Queries PureOrMixtureData_registry.db (and optionally ReactionData_registry.db)
to answer questions like "How much data do we have for water?" or "How many
papers measured the viscosity of ethanol?"

Public API
----------
    search_system_summary(compound=None, property=None, system_type=None,
                          include_reactions=False, limit=20) -> dict
"""

import sqlite3
import re
import sys
import os
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _id_alignment_search import resolve_compound_ids, resolve_property_ids
from normalization_helpers.paths import registry_db_path
from normalization_helpers.range_helpers import validate_range
from normalization_helpers.registry_parsers import (
    build_prop_patterns,
    format_pm_row,
    format_pm_subsystem_row,
    format_rxn_row,
)
from normalization_helpers.db_helpers import open_db
from normalization_helpers.strict_id_inputs import (
    refinement_errors_as_results,
    SearchValue,
    validate_search_values,
)

# ═════════════════════════════════════════════════════════════════════════════
# Helpers  (delegated to normalization_helpers)
# ═════════════════════════════════════════════════════════════════════════════

def _open_registry(name: str):
    """Return a read-only connection to a registry database."""
    return open_db(registry_db_path(name))


_build_prop_patterns = build_prop_patterns


# ═════════════════════════════════════════════════════════════════════════════
# Core query builder
# ═════════════════════════════════════════════════════════════════════════════

def _query_registry(conn, comp_ids: list[str] | None, prop_num_id: str | None,
                    system_type: str | None) -> list[sqlite3.Row]:
    """Build and execute the filtered query, return matching rows.

    Parameters
    ----------
    comp_ids : list of str or None
        List of canonical IDs like ["GLOBcomp_12", "GLOBcomp_8070"].
        ALL must be present in the row (AND logic).
    """
    clauses = []
    params = []

    if comp_ids:
        for cid in comp_ids:
            clauses.append("comp_ids_smiles LIKE ?")
            params.append(f'%"comp_num_id":"{cid}"%')

    if prop_num_id is not None:
        patterns = _build_prop_patterns(prop_num_id)
        or_clause = " OR ".join(["prop_ids_meas_ranges LIKE ?"] * len(patterns))
        clauses.append(f"({or_clause})")
        params.extend(patterns)

    if system_type is not None:
        clauses.append("system_type = ?")
        params.append(system_type)

    sql = "SELECT * FROM block_registry"
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)

    return conn.execute(sql, params).fetchall()


def _query_subsystems(
    conn,
    comp_ids: list[str] | None,
    prop_num_id: str | None,
    system_type: str | None,
) -> list[dict]:
    clauses = ["s.search_eligible = 1"]
    params: list[object] = []
    for comp_num_id in comp_ids or []:
        clauses.append(
            "EXISTS (SELECT 1 FROM block_subsystem_compounds sc "
            "WHERE sc.doi=s.doi AND sc.block_number=s.block_number "
            "AND sc.BLKsubsys_id=s.BLKsubsys_id "
            "AND sc.component_role='retained' AND sc.comp_num_id=?)"
        )
        params.append(comp_num_id)
    if prop_num_id is not None:
        clauses.append(
            "EXISTS (SELECT 1 FROM block_subsystem_properties sp "
            "WHERE sp.doi=s.doi AND sp.block_number=s.block_number "
            "AND sp.BLKsubsys_id=s.BLKsubsys_id "
            "AND sp.support_role='bulk_property' AND sp.phase_compatible=1 "
            "AND sp.prop_num_id=?)"
        )
        params.append(prop_num_id)
    if system_type is not None:
        clauses.append("s.effective_system_type = ?")
        params.append(system_type)
    sql = (
        "SELECT b.*, s.* FROM block_subsystems s JOIN block_registry b "
        "ON b.doi=s.doi AND b.block_number=s.block_number WHERE "
        + " AND ".join(clauses)
        + " ORDER BY s.doi, s.block_number, s.BLKsubsys_id"
    )
    return [
        format_pm_subsystem_row(conn, row, row)
        for row in conn.execute(sql, params).fetchall()
    ]


# ═════════════════════════════════════════════════════════════════════════════
# Statistics aggregation (single pass over rows)
# ═════════════════════════════════════════════════════════════════════════════

def _aggregate_stats(rows: list[dict], query_comp_ids: list[str] | None,
                     limit: int) -> tuple[dict, list[dict]]:
    """Aggregate explicit declared/subsystem targets without hiding overlap."""
    target_keys = {
        (row["doi"], row["block_number"], row["BLKsubsys_id"])
        for row in rows
    }
    block_keys = {(row["doi"], row["block_number"]) for row in rows}
    doi_set = {row["doi"] for row in rows}
    total_matching_datapoints = 0
    system_type_ctr = Counter()
    property_ctr = Counter()
    method_ctr = Counter()
    phase_ctr = Counter()
    compound_cooccurrence = Counter()
    comp_name_map: dict[str, str] = {}
    paper_stats: dict[str, dict] = {}
    temp_min = temp_max = pres_min = pres_max = None

    for row in rows:
        ndp = row["n_datapoints"]
        if isinstance(ndp, bool) or not isinstance(ndp, int) or ndp < 0:
            raise TypeError("registry n_datapoints must be a non-negative integer")
        total_matching_datapoints += ndp
        system_type_ctr[row["system_type"]] += 1
        paper = paper_stats.setdefault(row["doi"], {
            "doi": row["doi"],
            "lit_id": row["lit_id"],
            "lit_num_id": row["lit_num_id"],
            "block_keys": set(),
            "n_subsystems": 0,
            "n_targets": 0,
            "total_matching_datapoints": 0,
        })
        paper["block_keys"].add(row["block_number"])
        paper["n_subsystems"] += int(row["BLKsubsys_id"] is not None)
        paper["n_targets"] += 1
        paper["total_matching_datapoints"] += ndp

        for entry in row["properties"]:
            property_ctr[entry["name"]] += 1
            if entry["meas_ID"]:
                method_ctr[entry["meas_ID"]] += 1
        for entry in row["phases"]:
            if entry["phase_id"]:
                phase_ctr[entry["phase_id"]] += 1
        for entry in row["variables"]:
            lo, hi = entry["range_min"], entry["range_max"]
            if lo is None or hi is None:
                continue
            if entry["var_id"].startswith("temperature"):
                temp_min = lo if temp_min is None else min(temp_min, lo)
                temp_max = hi if temp_max is None else max(temp_max, hi)
            elif entry["var_id"].startswith("pressure"):
                pres_min = lo if pres_min is None else min(pres_min, lo)
                pres_max = hi if pres_max is None else max(pres_max, hi)
        query_set = set(query_comp_ids or [])
        for entry in row["compounds"]:
            comp_name_map.setdefault(entry["comp_num_id"], entry["name"])
            if query_comp_ids is not None and entry["comp_num_id"] not in query_set:
                compound_cooccurrence[entry["comp_num_id"]] += 1

    top_papers = []
    for paper in paper_stats.values():
        paper = dict(paper)
        paper["n_blocks"] = len(paper.pop("block_keys"))
        top_papers.append(paper)
    top_papers.sort(
        key=lambda item: (-item["total_matching_datapoints"], item["doi"])
    )
    summary = {
        "n_targets": len(target_keys),
        "n_blocks": len(block_keys),
        "n_subsystems": sum(row["BLKsubsys_id"] is not None for row in rows),
        "n_papers": len(doi_set),
        "total_matching_datapoints": total_matching_datapoints,
        "system_type_distribution": dict(system_type_ctr.most_common()),
        "property_distribution": dict(property_ctr.most_common()),
        "method_distribution": dict(method_ctr.most_common()),
        "phase_distribution": dict(phase_ctr.most_common()),
        "temperature_range_K": [temp_min, temp_max] if temp_min is not None else None,
        "pressure_range_kPa": [pres_min, pres_max] if pres_min is not None else None,
        "compound_cooccurrence": [
            {
                "comp_num_id": comp_num_id,
                "name": comp_name_map[comp_num_id],
                "n_targets": count,
            }
            for comp_num_id, count in compound_cooccurrence.most_common(10)
        ],
    }
    return summary, top_papers[:limit]


# ═════════════════════════════════════════════════════════════════════════════
# Public API
# ═════════════════════════════════════════════════════════════════════════════

from normalization_helpers.range_helpers import ranges_overlap as _ranges_overlap


def _filter_rows_by_ranges(rows, temperature_range, pressure_range):
    """Post-filter formatted targets by effective temperature/pressure ranges."""
    filtered = []
    for row in rows:
        keep = True
        if temperature_range:
            keep = any(
                entry["var_id"].startswith("temperature")
                and entry["range_min"] is not None
                and entry["range_max"] is not None
                and _ranges_overlap(
                    [entry["range_min"], entry["range_max"]], temperature_range
                )
                for entry in row["variables"]
            )
        if keep and pressure_range:
            keep = any(
                entry["var_id"].startswith("pressure")
                and entry["range_min"] is not None
                and entry["range_max"] is not None
                and _ranges_overlap(
                    [entry["range_min"], entry["range_max"]], pressure_range
                )
                for entry in row["variables"]
            )
        if keep:
            filtered.append(row)
    return filtered


@refinement_errors_as_results
def search_system_summary(
    compound: SearchValue = None,
    property: SearchValue = None,
    system_type: str | None = None,
    system_scope: str = "declared",
    temperature_range: list[float] | None = None,
    pressure_range: list[float] | None = None,
    include_reactions: bool = False,
    limit: int = 20,
) -> dict:
    """Return aggregate statistics for a compound, property, or both.

    Entity parameters accept one name/canonical ``GLOB*`` ID or a native list
    of those strings. Bare numeric and retired IDs are rejected.

    Parameters
    ----------
    compound : str | list, optional
        Compound name, formula, SMILES, InChI, comp_num_id, or
        ``GLOBcomp_N``.  Semicolon-separated for multiple.
    property : str | list, optional
        Property name, prop_id, prop_num_id, or ``GLOBprop_N``.
    system_type : str, optional
        Exact system_type filter ("pure", "binary", etc.).
    temperature_range : tuple/list (min_K, max_K), optional
        Keep only blocks whose temperature variable overlaps this range.
    pressure_range : tuple/list (min_kPa, max_kPa), optional
        Keep only blocks whose pressure variable overlaps this range.
    include_reactions : bool
        If True, also query ReactionData_registry.db and merge results.
    limit : int
        Max number of top papers to return.

    Returns
    -------
    dict with keys: query_params, compound_resolved, property_resolved,
                    summary, top_papers
    """
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise TypeError("limit must be a positive integer")
    if system_type is not None and (
        not isinstance(system_type, str)
        or not re.fullmatch(r"(?:unary|binary|ternary|quaternary|(?:[5-9]|[1-9][0-9]+)-component)", system_type)
    ):
        raise ValueError(
            "system_type must use the canonical registry value: unary, binary, "
            "ternary, quaternary, or N-component"
        )
    if system_scope not in {"declared", "subsystem", "either"}:
        raise ValueError(
            "system_scope must be exactly 'declared', 'subsystem', or 'either'"
        )
    t_range = validate_range(temperature_range, field="temperature_range")
    p_range = validate_range(pressure_range, field="pressure_range")

    if compound is None and property is None:
        return {
            "query_params": {
                "compound": compound,
                "property": property,
                "system_type": system_type,
                "system_scope": system_scope,
                "temperature_range": list(temperature_range) if temperature_range else None,
                "pressure_range": list(pressure_range) if pressure_range else None,
                "include_reactions": include_reactions,
            },
            "error": "At least one of 'compound' or 'property' must be provided.",
        }

    # ── Resolve inputs via hub ───────────────────────────────────────────
    comp_resolved_list = []
    comp_ids = []
    if compound is not None:
        parts = validate_search_values("compound", compound, field="compound")
        for part in parts:
            hits = resolve_compound_ids(part)
            if hits:
                comp_resolved_list.append(hits[0])
                comp_ids.append(hits[0]["comp_num_id"])
            else:
                return {
                    "query_params": {"compound": compound, "property": property,
                                     "system_type": system_type,
                "system_scope": system_scope,
                                     "include_reactions": include_reactions},
                    "compound_resolved": comp_resolved_list or None,
                    "property_resolved": None,
                    "error": f"Could not resolve compound '{part}'.",
                }
    comp_resolved = comp_resolved_list if comp_resolved_list else None

    prop_resolved = None
    prop_num_id = None
    if property is not None:
        prop_hits = resolve_property_ids(property)
        if not prop_hits:
            return {
                "query_params": {"compound": compound, "property": property,
                                 "system_type": system_type, "include_reactions": include_reactions},
                "compound_resolved": comp_resolved,
                "property_resolved": None,
                "error": f"Could not resolve property '{property}'.",
            }
        prop_resolved = prop_hits[0]
        prop_num_id = prop_resolved["prop_num_id"]

    # ── Query explicit targets ───────────────────────────────────────────
    conn = _open_registry("PM_REGISTRY")
    try:
        pm_rows: list[dict] = []
        if system_scope in {"declared", "either"}:
            pm_rows.extend(
                format_pm_row(row)
                for row in _query_registry(
                    conn, comp_ids or None, prop_num_id, system_type
                )
            )
        if system_scope in {"subsystem", "either"}:
            pm_rows.extend(
                _query_subsystems(
                    conn, comp_ids or None, prop_num_id, system_type
                )
            )
    finally:
        conn.close()
    all_rows = pm_rows

    if include_reactions and system_scope in {"declared", "either"}:
        conn_rxn = _open_registry("RXN_REGISTRY")
        try:
            all_rows.extend(
                format_rxn_row(row)
                for row in _query_registry(
                    conn_rxn, comp_ids or None, prop_num_id, system_type
                )
            )
        finally:
            conn_rxn.close()
    # ── Post-filter by temperature/pressure ranges ─────────────────────
    if t_range or p_range:
        all_rows = _filter_rows_by_ranges(all_rows, t_range, p_range)
    # ── Aggregate stats ──────────────────────────────────────────────────
    summary, top_papers = _aggregate_stats(all_rows, comp_ids or None, limit)

    return {
        "query_params": {
            "compound": compound,
            "property": property,
            "system_type": system_type,
                "system_scope": system_scope,
            "temperature_range": list(temperature_range) if temperature_range else None,
            "pressure_range": list(pressure_range) if pressure_range else None,
            "include_reactions": include_reactions,
        },
        "compound_resolved": comp_resolved,
        "property_resolved": prop_resolved,
        "summary": summary,
        "top_papers": top_papers,
    }


# ═════════════════════════════════════════════════════════════════════════════
# Demo / smoke-test
# ═════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import pprint

    def _print_summary(label: str, result: dict) -> None:
        print("=" * 70)
        print(label)
        print("=" * 70)
        if "error" in result:
            print(f"  ERROR: {result['error']}")
            return
        cr = result.get("compound_resolved")
        pr = result.get("property_resolved")
        if cr:
            print(f"  Compound: {cr.get('common_name', '?')} ({cr['comp_num_id']})")
        if pr:
            print(f"  Property: {pr.get('prop_name', '?')} ({pr['prop_num_id']})")
        s = result["summary"]
        print(f"  Blocks:     {s['n_blocks']}")
        print(f"  Papers:     {s['n_papers']}")
        print(f"  Datapoints: {s['total_matching_datapoints']}")
        print(f"  Temp range: {s['temperature_range_K']}")
        print(f"  Pres range: {s['pressure_range_kPa']}")
        print(f"  System types: {s['system_type_distribution']}")
        print(f"  Top 5 properties:")
        for name, cnt in list(s["property_distribution"].items())[:5]:
            print(f"    {name}: {cnt}")
        print(f"  Top 5 methods:")
        for name, cnt in list(s["method_distribution"].items())[:5]:
            print(f"    {name}: {cnt}")
        print(f"  Phases: {s['phase_distribution']}")
        if s["compound_cooccurrence"]:
            print(f"  Top co-occurring compounds:")
            for c in s["compound_cooccurrence"][:5]:
                print(f"    {c['comp_id']} ({c['name']}): {c['n_blocks']} blocks")
        print(f"  Top 5 papers:")
        for p in result["top_papers"][:5]:
            print(f"    {p['doi']}  blocks={p['n_blocks']}  dp={p['total_matching_datapoints']}")
        print()

    # ── 1. Summary for "water" ───────────────────────────────────────────
    _print_summary(
        "Summary: compound='water'",
        search_system_summary(compound="water"),
    )

    # ── 2. Summary for "viscosity" ───────────────────────────────────────
    _print_summary(
        "Summary: property='viscosity'",
        search_system_summary(property="viscosity"),
    )

    # ── 3. Summary for "ethanol" + "density" ─────────────────────────────
    _print_summary(
        "Summary: compound='ethanol', property='density'",
        search_system_summary(compound="ethanol", property="density"),
    )
