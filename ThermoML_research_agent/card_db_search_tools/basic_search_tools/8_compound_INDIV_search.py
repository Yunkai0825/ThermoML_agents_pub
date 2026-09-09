"""
8_compound_INDIV_search.py — Search CCS_INDIV.db for per-paper compound
characterization and purity cards.

Given a compound and/or DOI, find papers that characterise specific compounds,
including sample source and purity information.

Public API
----------
    search_compound_indiv(compound=None, literature=None, min_purity=None, limit=50)
        -> dict
"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _id_alignment_search import resolve_compound_ids, resolve_reference_ids
from normalization_helpers.paths import card_db_path
from normalization_helpers.compact import compact_card
from normalization_helpers.purity_helpers import best_purity
from normalization_helpers.db_helpers import open_db
from normalization_helpers.strict_id_inputs import refinement_errors_as_results, SearchValue
from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_doi_comp_id,
    require_doi_comp_sample_id,
    require_global_id,
)

# ═════════════════════════════════════════════════════════════════════════════
# Helpers
# ═════════════════════════════════════════════════════════════════════════════

_DB_PATH = card_db_path("CCS_INDIV")

_best_purity = best_purity


def _extract_result(card: dict, comp_entry: dict,
                    match_score: int, match_type: str) -> dict:
    """Build a single result item from the card and a matching compound entry."""
    key = card["key"]
    require_global_id("lit_num_id", key["lit_num_id"])
    org_num = require_doi_comp_id(comp_entry["org_num"])
    require_global_id("comp_num_id", comp_entry["comp_num_id"])
    samples = comp_entry["samples"]
    if samples is not None:
        if not isinstance(samples, list):
            raise TypeError("compound samples must be an array or null")
        for index, sample in enumerate(samples):
            if not isinstance(sample, dict):
                raise TypeError(f"compound samples[{index}] must be an object")
            require_doi_comp_sample_id(
                sample["sample_num"], component_org_num=org_num
            )
    return {
        "doi": key["doi"],
        "lit_num_id": key["lit_num_id"],
        "lit_id": key["lit_id"],
        "compound": {
            "org_num": org_num,
            "comp_num_id": comp_entry["comp_num_id"],
            "inchi_key": comp_entry["inchi_key"],
            "name": comp_entry["name"],
            "formula": comp_entry["formula"],
        },
        "samples": samples,
        "compact_md": compact_card("CCS_INDIV", card),
        "match_score": match_score,
        "match_type": match_type,
    }


# ═════════════════════════════════════════════════════════════════════════════
# Public API
# ═════════════════════════════════════════════════════════════════════════════

@refinement_errors_as_results
def search_compound_indiv(
    compound: SearchValue = None,
    literature: SearchValue = None,
    min_purity: float | None = None,
    limit: int = 50,
) -> dict:
    """Search CCS_INDIV.db for per-paper compound characterisation cards.

    Entity parameters accept one name/canonical ``GLOB*`` ID or a native list
    of those strings. Bare numeric and retired IDs are rejected.

    Parameters
    ----------
    compound : str | list, optional
        Compound name, formula, SMILES, InChI, InChI-key, comp_num_id,
        or ``GLOBcomp_N``.  Semicolon-separated for multiple.
    literature : str | list, optional
        DOI, lit_id, or lit_num_id.
    min_purity : float, optional
        Minimum sample purity (0–1).
    limit : int
        Maximum result items returned (default 50).

    Returns
    -------
    dict
        ``query_params`` – echo of the input parameters.
        ``n_results``    – number of result items.
        ``results``      – list of per-compound result dicts.
    """
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise TypeError("limit must be a positive integer")
    if min_purity is not None and (
        isinstance(min_purity, bool)
        or not isinstance(min_purity, (int, float))
        or not 0 <= min_purity <= 1
    ):
        raise TypeError("min_purity must be a number from 0 through 1")

    query_params: dict = {}
    if compound is not None:
        query_params["compound"] = compound
    if literature is not None:
        query_params["literature"] = literature
    if min_purity is not None:
        query_params["min_purity"] = min_purity
    query_params["limit"] = limit

    # ── Resolve compound via hub ─────────────────────────────────────────
    comp_candidates: list[dict] = []
    comp_id_set: set[str] = set()
    if compound is not None:
        comp_candidates = resolve_compound_ids(compound)
        comp_id_set = {c["comp_num_id"] for c in comp_candidates}
        if not comp_candidates:
            return {
                "query_params": query_params,
                "n_results": 0,
                "results": [],
                "note": f"Could not resolve compound '{compound}' to any known ID.",
            }

    # Build a quick lookup: comp_num_id -> (score, match_type)
    comp_score_map: dict[str, tuple[int, str]] = {}
    for c in comp_candidates:
        cid = c["comp_num_id"]
        if cid not in comp_score_map or c["score"] > comp_score_map[cid][0]:
            comp_score_map[cid] = (c["score"], c["match_type"])

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

    # ── Query database ───────────────────────────────────────────────────
    conn = open_db(_DB_PATH)
    results: list[dict] = []

    try:
        if doi and not compound:
            # DOI-only: return all compounds in that paper's card
            row = conn.execute(
                "SELECT json_data FROM cards WHERE doi = ?", (doi,)
            ).fetchone()
            if row:
                card = json.loads(row["json_data"])
                for comp in card["compounds"]:
                    if min_purity is not None:
                        bp = _best_purity(comp["samples"])
                        if bp is None or bp < min_purity:
                            continue
                    results.append(
                        _extract_result(card, comp, 100, "doi_exact")
                    )

        elif doi and compound:
            # Both DOI and compound: narrow to that paper, filter compounds
            row = conn.execute(
                "SELECT json_data FROM cards WHERE doi = ?", (doi,)
            ).fetchone()
            if row:
                card = json.loads(row["json_data"])
                for comp in card["compounds"]:
                    cid = require_global_id("comp_num_id", comp["comp_num_id"])
                    if cid in comp_id_set:
                        if min_purity is not None:
                            bp = _best_purity(comp["samples"])
                            if bp is None or bp < min_purity:
                                continue
                        sc, mt = comp_score_map[cid]
                        results.append(
                            _extract_result(card, comp, sc, f"doi+{mt}")
                        )

        elif compound:
            # Compound-only: scan all cards, parse JSON row by row
            cursor = conn.execute("SELECT json_data FROM cards")
            while True:
                row = cursor.fetchone()
                if row is None:
                    break
                card = json.loads(row["json_data"])
                for comp in card["compounds"]:
                    cid = require_global_id("comp_num_id", comp["comp_num_id"])
                    if cid not in comp_id_set:
                        continue
                    if min_purity is not None:
                        bp = _best_purity(comp["samples"])
                        if bp is None or bp < min_purity:
                            continue
                    sc, mt = comp_score_map[cid]
                    results.append(_extract_result(card, comp, sc, mt))
                    if len(results) >= limit:
                        break
                if len(results) >= limit:
                    break

        else:
            # No filters at all — return a sample of cards
            rows = conn.execute(
                "SELECT json_data FROM cards LIMIT ?", (limit,)
            ).fetchall()
            for row in rows:
                card = json.loads(row["json_data"])
                for comp in card["compounds"]:
                    if min_purity is not None:
                        bp = _best_purity(comp["samples"])
                        if bp is None or bp < min_purity:
                            continue
                    results.append(
                        _extract_result(card, comp, 50, "browse")
                    )
                    if len(results) >= limit:
                        break
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

    # ── 1. Search by compound name ───────────────────────────────────────
    print("=" * 70)
    print("Search: compound='water'")
    print("=" * 70)
    resp = search_compound_indiv(compound="water", limit=10)
    print(f"  n_results: {resp['n_results']}")
    for r in resp["results"][:5]:
        c = r["compound"]
        n_samples = len(r["samples"] or [])
        print(
            f"  doi={r['doi']}  comp={c['name']} "
            f"(id={c['comp_num_id']})  "
            f"samples={n_samples}  score={r['match_score']}  "
            f"type={r['match_type']}"
        )

    # ── 2. Search by DOI ─────────────────────────────────────────────────
    # Pick a DOI from the first result (if any) for a round-trip test
    if resp["results"]:
        test_doi = resp["results"][0]["doi"]
    else:
        test_doi = "10.1021/je049595u"

    print(f"\n{'='*70}")
    print(f"Search: doi='{test_doi}'")
    print("=" * 70)
    resp2 = search_compound_indiv(literature=test_doi)
    print(f"  n_results: {resp2['n_results']}")
    for r in resp2["results"]:
        c = r["compound"]
        n_samples = len(r["samples"] or [])
        print(
            f"  comp={c['name']} (id={c['comp_num_id']})  "
            f"samples={n_samples}"
        )

    # ── 3. Search with min_purity ────────────────────────────────────────
    print(f"\n{'='*70}")
    print("Search: compound='water', min_purity=0.99")
    print("=" * 70)
    resp3 = search_compound_indiv(compound="water", min_purity=0.99, limit=10)
    print(f"  n_results: {resp3['n_results']}")
    for r in resp3["results"][:5]:
        c = r["compound"]
        purity = _best_purity(r["samples"])
        print(
            f"  doi={r['doi']}  comp={c['name']}  "
            f"best_purity={purity}"
        )

    # ── 4. DOI + compound combined ───────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"Search: compound='water', doi='{test_doi}'")
    print("=" * 70)
    resp4 = search_compound_indiv(compound="water", literature=test_doi)
    print(f"  n_results: {resp4['n_results']}")
    for r in resp4["results"]:
        c = r["compound"]
        print(
            f"  comp={c['name']} (id={c['comp_num_id']})  "
            f"score={r['match_score']}  type={r['match_type']}"
        )
