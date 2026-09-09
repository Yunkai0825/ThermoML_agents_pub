"""
2_system_registry_search.py — Search PureOrMixtureData_registry.db and
ReactionData_registry.db block registries.

Each registry has one row per data block with rich metadata columns including
compound identifiers, variable ranges, property/measurement ranges, phase
information, and system-type classification.

Public API
----------
    search_system_registry(compound=None, property=None, system_type=None,
                           block_type=None, literature=None, n_components=None,
                           phase=None, include_reactions=False, limit=100)
        -> dict
"""

import sys
import os
import re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _id_alignment_search import (
    resolve_compound_ids,
    resolve_property_ids,
    resolve_phase_ids,
    resolve_reference_ids,
)
from normalization_helpers.paths import registry_db_path
from normalization_helpers.compact import compact_card
from normalization_helpers.range_helpers import validate_range, ranges_overlap
from normalization_helpers.registry_parsers import (
    parse_comp_ids_smiles,
    parse_var_ids_ranges,
    parse_prop_ids_meas_ranges,
    parse_phase_ids,
    parse_constr_ids_values,
    parse_participants,
    parse_reaction_type,
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

def _compact_subsystem_registry_result(result: dict) -> str:
    """Compact one normalized subsystem without reintroducing parent fields."""
    compounds = ", ".join(
        f'{item["comp_num_id"]} ({item["name"]})'
        for item in result["compounds"]
    )
    properties = ", ".join(
        f'{item["prop_num_id"]} ({item["prop_ID"]})'
        for item in result["properties"]
    ) or "none"
    variables = ", ".join(
        f'{item["var_num_id"]} ({item["var_id"]})'
        for item in result["variables"]
    ) or "none"
    return "\n".join([
        f'### {result["doi"]} · {result["block_number"]} · {result["BLKsubsys_id"]}',
        f'- Literature ID: {result["lit_num_id"]}',
        f'- Effective system: {result["system_type"]}',
        f'- Declared parent system: {result["declared_system_type"]}',
        f'- Matching raw points: {result["n_datapoints"]}',
        f'- Retained compounds: {compounds}',
        f'- Supported bulk properties: {properties}',
        f'- Active variables: {variables}',
    ]) + "\n"


# ═════════════════════════════════════════════════════════════════════════════
# Internal paths
# ═════════════════════════════════════════════════════════════════════════════

_PM_DB = registry_db_path("PM_REGISTRY")
_RXN_DB = registry_db_path("RXN_REGISTRY")


def _build_query(
    comp_groups: list[set[str]],
    prop_ids: set[str],
    phase_ids: set[str],
    system_type: str | None,
    block_type: str | None,
    doi: str | None,
    n_components: int | None,
    limit: int,
) -> tuple[str, list]:
    """Build a SQL query string and parameter list for block_registry.

    Returns (sql_string, params_list).
    """
    clauses: list[str] = []
    params: list = []

    # Exact-match columns
    if doi is not None:
        clauses.append("doi = ?")
        params.append(doi)

    if system_type is not None:
        clauses.append("system_type = ?")
        params.append(system_type)

    if n_components is not None:
        clauses.append("n_components = ?")
        params.append(n_components)

    if block_type is not None:
        clauses.append("block_type = ?")
        params.append(block_type)

    # LIKE-based filtering on JSON text columns
    # Compound: AND across query parts, OR within fuzzy matches of one part
    for group in comp_groups:
        group_likes = ["comp_ids_smiles LIKE ?" for _ in group]
        clauses.append("(" + " OR ".join(group_likes) + ")")
        for cid in group:
            params.append(f'%"comp_num_id":"{cid}"%')

    # Property: require ANY of the resolved prop_ids to be present (OR)
    if prop_ids:
        prop_likes = ["prop_ids_meas_ranges LIKE ?" for _ in prop_ids]
        clauses.append("(" + " OR ".join(prop_likes) + ")")
        for pid in prop_ids:
            params.append(f'%"prop_num_id":"{pid}"%')

    # Phase: require ANY of the resolved phase_ids to be present (OR)
    if phase_ids:
        phase_likes = ["prop_phase_ids LIKE ?" for _ in phase_ids]
        clauses.append("(" + " OR ".join(phase_likes) + ")")
        for phid in phase_ids:
            params.append(f"%{phid}%")

    sql = "SELECT * FROM block_registry"
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += f" LIMIT {limit}"

    return sql, params


def _build_subsystem_query(
    comp_groups: list[set[str]],
    prop_ids: set[str],
    phase_ids: set[str],
    system_type: str | None,
    doi: str | None,
    n_components: int | None,
    limit: int,
) -> tuple[str, list]:
    """Build a query over authoritative, search-eligible PCS projections."""
    clauses = ["s.search_eligible = 1"]
    params: list[object] = []
    if doi is not None:
        clauses.append("s.doi = ?")
        params.append(doi)
    if system_type is not None:
        clauses.append("s.effective_system_type = ?")
        params.append(system_type)
    if n_components is not None:
        clauses.append("s.n_retained_components = ?")
        params.append(n_components)
    for group in comp_groups:
        alternatives = []
        for comp_num_id in sorted(group):
            alternatives.append("sc.comp_num_id = ?")
            params.append(comp_num_id)
        clauses.append(
            "EXISTS (SELECT 1 FROM block_subsystem_compounds sc "
            "WHERE sc.doi=s.doi AND sc.block_number=s.block_number "
            "AND sc.BLKsubsys_id=s.BLKsubsys_id "
            "AND sc.component_role='retained' AND ("
            + " OR ".join(alternatives)
            + "))"
        )
    if prop_ids:
        alternatives = []
        for prop_num_id in sorted(prop_ids):
            alternatives.append("sp.prop_num_id = ?")
            params.append(prop_num_id)
        clauses.append(
            "EXISTS (SELECT 1 FROM block_subsystem_properties sp "
            "WHERE sp.doi=s.doi AND sp.block_number=s.block_number "
            "AND sp.BLKsubsys_id=s.BLKsubsys_id "
            "AND sp.support_role='bulk_property' AND sp.phase_compatible=1 "
            "AND (" + " OR ".join(alternatives) + "))"
        )
    for phase_id in sorted(phase_ids):
        clauses.append("s.scope_json LIKE ?")
        params.append(f'%"phase_id":"{phase_id}"%')
    sql = (
        "SELECT b.*, s.* FROM block_subsystems s "
        "JOIN block_registry b ON b.doi=s.doi AND b.block_number=s.block_number "
        "WHERE " + " AND ".join(clauses)
        + " ORDER BY s.doi, s.block_number, s.BLKsubsys_id LIMIT ?"
    )
    params.append(limit)
    return sql, params


# ═════════════════════════════════════════════════════════════════════════════
# Public API
# ═════════════════════════════════════════════════════════════════════════════

_ranges_overlap = ranges_overlap


def _row_passes_range_filters(row: dict, temperature_range, pressure_range,
                              n_datapoints_min: int | None) -> bool:
    """Post-filter a formatted result dict against value/range criteria."""
    if n_datapoints_min is not None:
        ndp = row["n_datapoints"]
        if ndp < n_datapoints_min:
            return False
    if temperature_range is not None:
        found = False
        for v in row["variables"]:
            if "name" not in v or not isinstance(v["name"], str):
                raise ValueError("var_ids_ranges entries require string name")
            vname = v["name"].lower()
            if "temperature" in vname:
                rng = [v["range_min"], v["range_max"]]
                if rng[0] is not None and rng[1] is not None:
                    if _ranges_overlap(rng, temperature_range):
                        found = True
                        break
        if not found:
            return False
    if pressure_range is not None:
        found = False
        for v in row["variables"]:
            if "name" not in v or not isinstance(v["name"], str):
                raise ValueError("var_ids_ranges entries require string name")
            vname = v["name"].lower()
            if "pressure" in vname:
                rng = [v["range_min"], v["range_max"]]
                if rng[0] is not None and rng[1] is not None:
                    if _ranges_overlap(rng, pressure_range):
                        found = True
                        break
        if not found:
            return False
    return True


@refinement_errors_as_results
def search_system_registry(
    compound: SearchValue = None,
    property: SearchValue = None,
    system_type: str | None = None,
    system_scope: str = "declared",
    block_type: str | None = None,
    literature: SearchValue = None,
    n_components: int | None = None,
    phase: SearchValue = None,
    temperature_range: list[float] | None = None,
    pressure_range: list[float] | None = None,
    n_datapoints_min: int | None = None,
    include_reactions: bool = False,
    limit: int = 100,
) -> dict:
    """Search the block registries for data blocks matching the given criteria.

    Entity parameters accept one name/canonical ``GLOB*`` ID or a native list
    of those strings. Bare numeric and retired IDs are rejected.

    Parameters
    ----------
    compound : str | list, optional
        Compound name, formula, SMILES, InChI, InChI-key, comp_num_id,
        or ``GLOBcomp_N``.  Semicolon-separated for multiple.
    property : str | list, optional
        Property name, prop_id, prop_num_id, or ``GLOBprop_N``.
    system_type : str, optional
        Canonical declared or effective system type.
    system_scope : str
        Exactly ``declared``, ``subsystem``, or ``either``.
    block_type : str, optional
        "PureOrMixtureData" or "ReactionData".
    literature : str | list, optional
        DOI, lit_id, or lit_num_id.
    n_components : int, optional
        Exact number of components.
    phase : str | list, optional
        Phase name or phase_id.
    temperature_range : tuple/list (min_K, max_K), optional
        Keep blocks whose temperature variable overlaps this range.
    pressure_range : tuple/list (min_kPa, max_kPa), optional
        Keep blocks whose pressure variable overlaps this range.
    n_datapoints_min : int, optional
        Minimum datapoints per block.
    include_reactions : bool
        If True, also search ReactionData_registry.db (default: PM only).
    limit : int
        Maximum number of result rows (default 100).

    Returns
    -------
    dict
        ``query_params`` – echo of the effective query inputs.
        ``n_results``    – number of block rows returned.
        ``results``      – list of structured block dicts.
    """
    # ── Echo query params ────────────────────────────────────────────────
    query_params: dict = {}
    if compound is not None:
        query_params["compound"] = compound
    if property is not None:
        query_params["property"] = property
    if system_type is not None:
        query_params["system_type"] = system_type
    query_params["system_scope"] = system_scope
    if block_type is not None:
        query_params["block_type"] = block_type
    if literature is not None:
        query_params["literature"] = literature
    if n_components is not None:
        query_params["n_components"] = n_components
    if phase is not None:
        query_params["phase"] = phase
    if temperature_range is not None:
        query_params["temperature_range"] = list(temperature_range)
    if pressure_range is not None:
        query_params["pressure_range"] = list(pressure_range)
    if n_datapoints_min is not None:
        query_params["n_datapoints_min"] = n_datapoints_min
    query_params["include_reactions"] = include_reactions
    query_params["limit"] = limit

    # ── Resolve inputs via id_alignment ──────────────────────────────────
    comp_groups: list[set[str]] = []
    if compound is not None:
        # Resolve each strictly validated atom separately so AND logic applies
        # across atoms (OR within fuzzy matches).
        parts = validate_search_values("compound", compound, field="compound")
        for part in parts:
            hits = resolve_compound_ids(part)
            group = {c["comp_num_id"] for c in hits}
            if group:
                comp_groups.append(group)

        if not comp_groups:
            return {
                "query_params": query_params,
                "n_results": 0,
                "results": [],
                "note": f"Could not resolve compound '{compound}' to any known ID.",
            }

    prop_ids: set[str] = set()
    if property is not None:
        prop_hits = resolve_property_ids(property)
        prop_ids = {p["prop_num_id"] for p in prop_hits}
        if not prop_ids:
            return {
                "query_params": query_params,
                "n_results": 0,
                "results": [],
                "note": f"Could not resolve property '{property}' to any known ID.",
            }

    phase_ids: set[str] = set()
    if phase is not None:
        phase_hits = resolve_phase_ids(phase)
        phase_ids = {p["phase_id"] for p in phase_hits}
        if not phase_ids:
            return {
                "query_params": query_params,
                "n_results": 0,
                "results": [],
                "note": f"Could not resolve phase '{phase}' to any known ID.",
            }

    # Resolve literature → DOI
    doi: str | None = None
    if literature is not None:
        ref_hits = resolve_reference_ids(literature)
        if ref_hits:
            doi = ref_hits[0]["doi"]
        else:
            return {
                "query_params": query_params,
                "n_results": 0,
                "results": [],
                "note": f"Could not resolve literature '{literature}' to any known DOI.",
            }

    # ── Decide which registries to query ─────────────────────────────────
    search_pm = True
    search_rxn = include_reactions

    # If block_type is explicitly set, narrow accordingly
    if block_type == "ReactionData":
        search_pm = False
        search_rxn = True
    elif block_type == "PureOrMixtureData":
        search_pm = True
        search_rxn = False

    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise TypeError("limit must be a positive integer")
    if system_type is not None and (
        not isinstance(system_type, str)
        or not re.fullmatch(r"(?:unary|binary|ternary|quaternary|(?:[5-9]|[1-9][0-9]+)-component)", system_type)
    ):
        raise ValueError(
            "system_type must use the exact registry value: unary, binary, "
            "ternary, quaternary, or N-component"
        )
    if n_components is not None and (
        isinstance(n_components, bool) or not isinstance(n_components, int) or n_components < 1
    ):
        raise TypeError("n_components must be a positive integer")
    if system_scope not in {"declared", "subsystem", "either"}:
        raise ValueError(
            "system_scope must be exactly 'declared', 'subsystem', or 'either'"
        )
    if block_type == "ReactionData" and system_scope == "subsystem":
        raise ValueError("ReactionData has no composition-subsystem projections")
    if n_datapoints_min is not None and (
        isinstance(n_datapoints_min, bool)
        or not isinstance(n_datapoints_min, int)
        or n_datapoints_min < 0
    ):
        raise TypeError("n_datapoints_min must be a non-negative integer")
    t_range = validate_range(temperature_range, field="temperature_range")
    p_range = validate_range(pressure_range, field="pressure_range")

    results: list[dict] = []

    if search_pm:
        if not os.path.exists(_PM_DB):
            raise FileNotFoundError(f"Required PM registry is missing: {_PM_DB}")
        conn = open_db(_PM_DB)
        try:
            if system_scope in {"declared", "either"}:
                sql, params = _build_query(
                    comp_groups, prop_ids, phase_ids,
                    system_type, block_type, doi, n_components, limit * 10,
                )
                for row in conn.execute(sql, params):
                    result = format_pm_row(row)
                    result["compact_md"] = compact_card("PM_REGISTRY", dict(row))
                    results.append(result)
            if system_scope in {"subsystem", "either"}:
                sql, params = _build_subsystem_query(
                    comp_groups, prop_ids, phase_ids,
                    system_type, doi, n_components, limit * 10,
                )
                for row in conn.execute(sql, params):
                    result = format_pm_subsystem_row(conn, row, row)
                    result["compact_md"] = _compact_subsystem_registry_result(result)
                    results.append(result)
        finally:
            conn.close()

    if search_rxn and system_scope in {"declared", "either"}:
        if not os.path.exists(_RXN_DB):
            raise FileNotFoundError(f"Required reaction registry is missing: {_RXN_DB}")
        sql, params = _build_query(
            comp_groups, prop_ids, phase_ids,
            system_type, block_type, doi, n_components, limit * 10,
        )
        conn = open_db(_RXN_DB)
        try:
            for row in conn.execute(sql, params):
                result = format_rxn_row(row)
                result["declared_compounds"] = list(result["compounds"])
                result["compact_md"] = compact_card("RXN_REGISTRY", dict(row))
                results.append(result)
        finally:
            conn.close()

    # ── Post-filter by value/range criteria ───────────────────────────
    has_range_filter = (t_range is not None or p_range is not None
                        or n_datapoints_min is not None)
    if has_range_filter:
        results = [r for r in results
                   if _row_passes_range_filters(r, t_range, p_range, n_datapoints_min)]

    results.sort(key=lambda item: (
        item["doi"], item["block_number"],
        0 if item["search_scope"] == "declared" else 1,
        item["BLKsubsys_id"] or "",
    ))
    results = results[:limit]

    return {
        "query_params": query_params,
        "n_results": len(results),
        "results": results,
    }


# ═════════════════════════════════════════════════════════════════════════════
# Demo / smoke-test
# ═════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import pprint

    # ── 1. Search by compound "water" ────────────────────────────────────
    print("=" * 70)
    print("Search: compound='water'")
    print("=" * 70)
    resp = search_system_registry(compound="water", limit=10)
    print(f"  n_results: {resp['n_results']}")
    for r in resp["results"][:5]:
        comps = ", ".join(c["name"] for c in r["compounds"])
        props = ", ".join(p["prop_name"] for p in r["properties"])
        print(f"  doi={r['doi']}  block={r['block_number']}  "
              f"type={r['system_type']}  nc={r['n_components']}  "
              f"compounds=[{comps}]  props=[{props}]")

    # ── 2. Search by property "viscosity" ────────────────────────────────
    print(f"\n{'='*70}")
    print("Search: property='viscosity'")
    print("=" * 70)
    resp = search_system_registry(property="viscosity", limit=10)
    print(f"  n_results: {resp['n_results']}")
    for r in resp["results"][:5]:
        comps = ", ".join(c["name"] for c in r["compounds"])
        props = ", ".join(p["prop_name"] for p in r["properties"])
        print(f"  doi={r['doi']}  system={r['system_type']}  "
              f"compounds=[{comps}]  props=[{props}]")

    # ── 3. Search by DOI ─────────────────────────────────────────────────
    test_doi = "10.1021/je049595u"
    print(f"\n{'='*70}")
    print(f"Search: doi='{test_doi}'")
    print("=" * 70)
    resp = search_system_registry(literature=test_doi, limit=20)
    print(f"  n_results: {resp['n_results']}")
    for r in resp["results"][:5]:
        comps = ", ".join(c["name"] for c in r["compounds"])
        props = ", ".join(p["prop_name"] for p in r["properties"])
        phases = ", ".join(ph["phase_name"] for ph in r["phases"])
        print(f"  block={r['block_number']}  type={r['system_type']}  "
              f"nc={r['n_components']}  dp={r['n_datapoints']}  "
              f"compounds=[{comps}]  props=[{props}]  phases=[{phases}]")

    # ── 4. Search by system_type="binary" + compound "water" ─────────────
    print(f"\n{'='*70}")
    print("Search: system_type='binary', compound='water'")
    print("=" * 70)
    resp = search_system_registry(
        compound="water", system_type="binary", limit=10,
    )
    print(f"  n_results: {resp['n_results']}")
    for r in resp["results"][:5]:
        comps = ", ".join(c["name"] for c in r["compounds"])
        props = ", ".join(p["prop_name"] for p in r["properties"])
        print(f"  doi={r['doi']}  block={r['block_number']}  "
              f"nc={r['n_components']}  dp={r['n_datapoints']}  "
              f"compounds=[{comps}]  props=[{props}]")

    # ── 5. Search with include_reactions=True ────────────────────────────
    print(f"\n{'='*70}")
    print("Search: compound='water', include_reactions=True")
    print("=" * 70)
    resp = search_system_registry(
        compound="water", include_reactions=True, limit=10,
    )
    print(f"  n_results: {resp['n_results']}")
    for r in resp["results"][:5]:
        comps = ", ".join(c["name"] for c in r["compounds"])
        bt = r["block_type"]
        rxn = r.get("reaction_type")
        rxn_str = f"  rxn={rxn['rxn_name']}" if rxn else ""
        print(f"  doi={r['doi']}  block_type={bt}  "
              f"compounds=[{comps}]{rxn_str}")
