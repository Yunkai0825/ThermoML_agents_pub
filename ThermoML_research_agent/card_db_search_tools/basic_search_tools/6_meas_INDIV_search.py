"""
6_meas_INDIV_search.py
----------------------
Search MTDKS_INDIV.db for per-paper measurement technique usage cards.

Find papers that use specific measurement methods, or find all methods used
in a specific paper.  Optionally filter to methods that measured a particular
property.

Public API
----------
    search_measurement_indiv(method=None, literature=None, property=None, limit=50)
        -> dict
"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _id_alignment_search import (
    resolve_measurement_ids,
    resolve_property_ids,
    resolve_reference_ids,
)
from normalization_helpers.paths import card_db_path
from normalization_helpers.compact import compact_card
from normalization_helpers.db_helpers import open_db
from normalization_helpers.strict_id_inputs import refinement_errors_as_results, SearchValue
from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_block_id,
    require_global_id,
)

# ═════════════════════════════════════════════════════════════════════════════
# Helpers
# ═════════════════════════════════════════════════════════════════════════════

_DB_PATH = card_db_path("MTDKS_INDIV")
_RMS_DB_PATH = card_db_path("RMS_INDIV")


def _method_matches_meas(entry: dict, meas_id_set: set[str],
                         method_names: set[str] | None = None) -> bool:
    """True only when the method occurrence references a requested global ID."""
    mid = entry["meas_num_id"]
    if mid is not None:
        require_global_id("meas_num_id", mid)
    return mid is not None and mid in meas_id_set


def _method_matches_prop(entry: dict, prop_num_id_set: set[str]) -> bool:
    """True if the method overlaps the target global property identities.

    Match on ``GLOBprop_N`` rather than occurrence-level ``prop_id``.  The
    latter can contain a DOI-local component suffix such as ``DOIcomp_2``.
    """
    props = entry["properties"]
    for p in props:
        if not isinstance(p, dict):
            raise TypeError("measurement properties entries must be objects")
        prop_num_id = require_global_id("prop_num_id", p["prop_num_id"])
        if prop_num_id in prop_num_id_set:
            return True
    return False


def _filter_methods(methods: list[dict],
                    meas_id_set: set[str] | None,
                    method_names: set[str] | None,
                    prop_num_id_set: set[str] | None) -> list[dict]:
    """Return only the method entries matching the given filters."""
    result = []
    for m in methods:
        if meas_id_set is not None and not _method_matches_meas(
            m, meas_id_set, method_names
        ):
            continue
        if prop_num_id_set is not None and not _method_matches_prop(
            m, prop_num_id_set
        ):
            continue
        result.append(m)
    return result


def _extract_result(card: dict, matching_methods: list[dict],
                    match_score: int, match_type: str) -> dict:
    """Build a single result item from the card and its matching methods."""
    key = card["key"]
    require_global_id("lit_num_id", key["lit_num_id"])
    for index, method in enumerate(matching_methods):
        if not isinstance(method, dict):
            raise TypeError(f"methods[{index}] must be an object")
        if method["meas_num_id"] is not None:
            require_global_id("meas_num_id", method["meas_num_id"])
        for block_number in method["block_numbers"]:
            require_block_id(block_number)
    return {
        "doi": key["doi"],
        "lit_num_id": key["lit_num_id"],
        "lit_id": key["lit_id"],
        "methods_summary": card["methods_summary"],
        "matching_methods": matching_methods,
        "compact_md": compact_card("MTDKS_INDIV", card),
        "match_score": match_score,
        "match_type": match_type,
    }


def _dois_for_compounds(comp_num_ids: set[str]) -> set[str]:
    """Resolve a compound filter through RMS data_inventory, never MTDKS guesses."""
    matches: set[str] = set()
    conn = open_db(_RMS_DB_PATH)
    try:
        for row in conn.execute("SELECT doi, json_data FROM cards"):
            card = json.loads(row["json_data"])
            inventory = card["data_inventory"]
            present = {
                require_global_id("comp_num_id", entry["comp_num_id"])
                for entry in inventory["compound_list"]
            }
            if comp_num_ids <= present:
                matches.add(row["doi"])
    finally:
        conn.close()
    return matches


# ═════════════════════════════════════════════════════════════════════════════
# Public API
# ═════════════════════════════════════════════════════════════════════════════

@refinement_errors_as_results
def search_measurement_indiv(
    method: SearchValue = None,
    literature: SearchValue = None,
    property: SearchValue = None,
    compound: SearchValue = None,
    limit: int = 50,
) -> dict:
    """Search MTDKS_INDIV.db for per-paper measurement technique usage cards.

    Entity parameters accept one name/canonical ``GLOB*`` ID or a native list
    of those strings. Bare numeric and retired IDs are rejected.

    Parameters
    ----------
    method : str | list, optional
        Measurement method name, meas_id, meas_num_id, or ``GLOBmeas_N``
        string.  Semicolon-separated for multiple.
    literature : str | list, optional
        DOI, lit_id, or lit_num_id.
    property : str | list, optional
        Property name, prop_id, prop_num_id, or ``GLOBprop_N``.
    compound : str | list, optional
        Compound name, formula, comp_num_id, or ``GLOBcomp_N``.
        Filters to papers that include this compound.
    limit : int
        Maximum result items returned (default 50).

    Returns
    -------
    dict
        ``query_params`` – echo of the input parameters.
        ``n_results``    – number of result items.
        ``results``      – list of per-paper result dicts.
    """
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise TypeError("limit must be a positive integer")
    query_params: dict = {}
    if method is not None:
        query_params["method"] = method
    if literature is not None:
        query_params["literature"] = literature
    if property is not None:
        query_params["property"] = property
    if compound is not None:
        query_params["compound"] = compound
    query_params["limit"] = limit

    # ── Resolve method to meas_num_ids via hub ───────────────────────────
    meas_candidates: list[dict] = []
    meas_id_set: set[str] | None = None
    meas_score_map: dict[str, tuple[int, str]] = {}

    if method is not None:
        meas_candidates = resolve_measurement_ids(method)
        if not meas_candidates:
            return {
                "query_params": query_params,
                "n_results": 0,
                "results": [],
                "note": f"Could not resolve method '{method}' to any known ID.",
            }
        meas_id_set = {c["meas_num_id"] for c in meas_candidates}
        for c in meas_candidates:
            mid = c["meas_num_id"]
            if mid not in meas_score_map or c["score"] > meas_score_map[mid][0]:
                meas_score_map[mid] = (c["score"], c["match_type"])

    method_names: set[str] | None = None

    # ── Resolve property to prop_ids via hub ─────────────────────────────
    prop_candidates: list[dict] = []
    prop_num_id_set: set[str] | None = None

    if property is not None:
        prop_candidates = resolve_property_ids(property)
        if not prop_candidates:
            return {
                "query_params": query_params,
                "n_results": 0,
                "results": [],
                "note": f"Could not resolve property '{property}' to any known ID.",
            }
        prop_num_id_set = {c["prop_num_id"] for c in prop_candidates}

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

    # ── Resolve compound to comp_num_ids via hub ───────────────────
    comp_num_ids: set[str] | None = None
    compound_dois: set[str] | None = None
    if compound is not None:
        from _id_alignment_search import resolve_compound_ids
        comp_hits = resolve_compound_ids(compound)
        if comp_hits:
            comp_num_ids = {c["comp_num_id"] for c in comp_hits}
            compound_dois = _dois_for_compounds(comp_num_ids)
        else:
            return {
                "query_params": query_params,
                "n_results": 0,
                "results": [],
                "note": f"Could not resolve compound '{compound}' to any known ID.",
            }

    # ── Query database ───────────────────────────────────────────────────
    conn = open_db(_DB_PATH)
    results: list[dict] = []

    try:
        if doi and not method and not property:
            # DOI-only: return all methods in that paper's card
            row = conn.execute(
                "SELECT json_data FROM cards WHERE doi = ?", (doi,)
            ).fetchone()
            if row and (compound_dois is None or doi in compound_dois):
                card = json.loads(row["json_data"])
                all_methods = card["methods"]
                results.append(
                    _extract_result(card, all_methods, 100, "doi_exact")
                )

        elif doi:
            # DOI + method and/or property: fetch that paper, filter methods
            row = conn.execute(
                "SELECT json_data FROM cards WHERE doi = ?", (doi,)
            ).fetchone()
            if row and (compound_dois is None or doi in compound_dois):
                card = json.loads(row["json_data"])
                matching = _filter_methods(
                    card["methods"], meas_id_set, method_names,
                    prop_num_id_set,
                )
                if matching:
                    # Determine score from best matching method
                    best_score = 100
                    best_type = "doi_exact"
                    if meas_id_set:
                        scores = [
                            meas_score_map[m["meas_num_id"]][0]
                            for m in matching
                        ]
                        best_score = max(scores) if scores else 80
                        best_type = "doi+method"
                    if prop_num_id_set:
                        best_type = best_type.replace("doi_exact", "doi") + "+property"
                    results.append(
                        _extract_result(card, matching, best_score, best_type)
                    )

        else:
            # No DOI: scan all cards row-by-row, filter by method/property
            cursor = conn.execute("SELECT json_data FROM cards")
            while True:
                row = cursor.fetchone()
                if row is None:
                    break
                card = json.loads(row["json_data"])
                if compound_dois is not None and card["key"]["doi"] not in compound_dois:
                    continue
                all_methods = card["methods"]

                matching = _filter_methods(
                    all_methods, meas_id_set, method_names, prop_num_id_set
                )
                if not matching:
                    continue

                # Compute match score
                if meas_id_set:
                    scores = [
                        meas_score_map[m["meas_num_id"]][0]
                        for m in matching
                    ]
                    best_score = max(scores) if scores else 60
                    match_type = "method"
                    if prop_num_id_set:
                        match_type = "method+property"
                elif prop_num_id_set:
                    best_score = 80
                    match_type = "property"
                else:
                    best_score = 50
                    match_type = "browse"

                results.append(
                    _extract_result(card, matching, best_score, match_type)
                )
                if len(results) >= limit:
                    break

    finally:
        conn.close()

    # Sort by descending match score, then DOI for stability
    results.sort(key=lambda r: (-r["match_score"], r["doi"]))

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

    # ── 1. Search by DOI ─────────────────────────────────────────────────
    test_doi = "10.1021/je049595u"
    print("=" * 70)
    print(f"Search: doi='{test_doi}'")
    print("=" * 70)
    resp = search_measurement_indiv(doi=test_doi)
    print(f"  n_results: {resp['n_results']}")
    for r in resp["results"][:3]:
        print(f"  doi={r['doi']}  lit_id={r.get('lit_id')}")
        print(f"    methods_summary: {r['methods_summary']}")
        for m in r["matching_methods"][:5]:
            print(
                f"    - {m.get('method_name','?')} "
                f"(meas_id={m['meas_num_id']}) "
                f"props={m.get('properties',[])} "
                f"blocks={m.get('block_numbers',[])}"
            )

    # ── 2. Search by method name ─────────────────────────────────────────
    print(f"\n{'='*70}")
    print("Search: method='DSC'")
    print("=" * 70)
    resp2 = search_measurement_indiv(method="DSC", limit=10)
    print(f"  n_results: {resp2['n_results']}")
    for r in resp2["results"][:5]:
        print(
            f"  doi={r['doi']}  score={r['match_score']}  "
            f"type={r['match_type']}  "
            f"n_matching={len(r['matching_methods'])}"
        )
        for m in r["matching_methods"][:2]:
            print(
                f"    - {m.get('method_name','?')} "
                f"(id={m['meas_num_id']}) "
                f"props={m.get('properties',[])} "
                f"instances={m.get('instance_count')}"
            )

    # ── 3. Search by property name ───────────────────────────────────────
    print(f"\n{'='*70}")
    print("Search: property='viscosity'")
    print("=" * 70)
    resp3 = search_measurement_indiv(property="viscosity", limit=10)
    print(f"  n_results: {resp3['n_results']}")
    for r in resp3["results"][:5]:
        print(
            f"  doi={r['doi']}  score={r['match_score']}  "
            f"type={r['match_type']}  "
            f"n_matching={len(r['matching_methods'])}"
        )
        for m in r["matching_methods"][:2]:
            print(
                f"    - {m.get('method_name','?')} "
                f"props={m.get('properties',[])} "
                f"instances={m.get('instance_count')}"
            )

    # ── 4. Combined: method + property ───────────────────────────────────
    print(f"\n{'='*70}")
    print("Search: method='DSC', property='viscosity'")
    print("=" * 70)
    resp4 = search_measurement_indiv(
        method="DSC", property="viscosity", limit=10
    )
    print(f"  n_results: {resp4['n_results']}")
    for r in resp4["results"][:5]:
        print(
            f"  doi={r['doi']}  score={r['match_score']}  "
            f"type={r['match_type']}  "
            f"n_matching={len(r['matching_methods'])}"
        )
