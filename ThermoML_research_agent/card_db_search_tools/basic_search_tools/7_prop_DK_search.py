"""
7_prop_DK_search.py  (Property DK Search)
----------------------------------------------
Search PCS_ID_DK.db for property identity and domain-knowledge cards.

This tool  searches the Property Card System (PCS_ID_DK) database.  
Given a property query (name, prop_id, group), resolve it to prop_num_id(s) 
via normalisation helpers, then retrieve the full JSON card from the PCS_ID_DK database.

Public API
----------
    search_property_dk(property, prop_group=None, limit=5)  ->  dict
"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _id_alignment_search import resolve_property_ids
from normalization_helpers.paths import card_db_path
from normalization_helpers.compact import compact_card
from normalization_helpers.db_helpers import open_db
from normalization_helpers.strict_id_inputs import refinement_errors_as_results
from ThermoML_raw_json_to_card_db_parsers.id_schema import require_global_id

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

@refinement_errors_as_results
def search_property_dk(property: str | list[str], prop_group: str | None = None,
                       limit: int = 5) -> dict:
    """Return property identity / domain-knowledge cards matching *property*.

    Parameters
    ----------
    property : str | list[str], optional
        Property name, prop_id, prop_num_id, or strict ``"GLOBprop_N"`` string.
        Semicolon-separated for multiple.
        Bare numbers and retired unscoped IDs return a refinement error.
    prop_group : str or None, optional
        If given, restrict results to this property group.
    limit : int, optional
        Maximum number of results (default 5).

    Returns
    -------
    dict
        ``query``       – the original input
        ``prop_group``  – the group filter (only present when supplied)
        ``n_results``   – number of cards returned
        ``results``     – list of dicts, each containing:
            ``prop_num_id``, ``prop_id``, ``match_score``, ``match_type``,
            and the full card data merged in.
    """
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise TypeError("limit must be a positive integer")
    # Step 1 – resolve query to candidate prop_num_ids
    candidates = resolve_property_ids(property)
    if not candidates:
        return {
            "query": property,
            "n_results": 0,
            "results": [],
            "error": f"Could not resolve property {property!r} to a global ID.",
            "error_code": "QUERY_REFINEMENT_REQUIRED",
        }

    # Step 2 – filter by prop_group if requested
    if prop_group:
        gl = prop_group.lower()
        candidates = [
            c for c in candidates
            if gl in c["prop_group"].lower()
        ]

    candidates = candidates[:limit]

    # Step 3 – fetch full JSON cards from PCS_ID_DK.db
    db_path = card_db_path("PCS_ID_DK")
    results: list[dict] = []

    con = open_db(db_path)
    try:
        cur = con.cursor()
        for cand in candidates:
            pid = cand["prop_num_id"]
            row = cur.execute(
                "SELECT json_data FROM cards WHERE prop_num_id = ?", (pid,)
            ).fetchone()
            if row is None:
                continue
            card = json.loads(row[0])
            require_global_id("prop_num_id", card["prop_num_id"])
            if card["prop_num_id"] != pid:
                raise ValueError("PCS_ID_DK row/card prop_num_id mismatch")
            results.append({
                "prop_num_id": pid,
                "prop_id": cand["prop_id"],
                "match_score": cand["score"],
                "match_type": cand["match_type"],
                "compact_md": compact_card("PCS_ID_DK", card),
                **card,
            })

    finally:
        con.close()

    out: dict = {
        "query": property,
        "n_results": len(results),
        "results": results,
    }
    if prop_group is not None:
        out["prop_group"] = prop_group
    return out


# ---------------------------------------------------------------------------
# Demo / quick smoke-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    test_cases = [
        ("density", None),
        ("viscosity", None),
        ("VolumetricProp", None),      # group-style query
    ]

    # Also demo the group filter
    test_cases.append(("density", "VolumetricProp"))

    for q, grp in test_cases:
        print(f"\n{'='*70}")
        label = f"Query: {q!r}"
        if grp:
            label += f"  prop_group={grp!r}"
        print(label)
        print("=" * 70)

        resp = search_property_dk(property=q, prop_group=grp)
        print(f"  n_results: {resp['n_results']}")
        for r in resp["results"]:
            ident = r["identity"]
            name = ident["name"]
            group = ident["property_group"]
            usage = ident["db_usage"]
            n_papers = usage["n_papers"]
            print(
                f"  prop_num_id={r['prop_num_id']:<4}  "
                f"score={r['match_score']:<3}  "
                f"type={r['match_type']:<16}  "
                f"name={name}  "
                f"group={group}  "
                f"n_papers={n_papers}"
            )
