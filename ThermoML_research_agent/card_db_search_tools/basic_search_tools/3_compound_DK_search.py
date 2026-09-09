"""
3_compound_DK_search.py
-----------------------
Search CCS_ID_DK.db for compound identity and domain-knowledge cards.

Given a compound query (name, formula, SMILES, InChI, InChI-key), resolve it
to comp_num_id(s) via normalisation helpers, then retrieve the full JSON card
from the CCS_ID_DK database.

Public API
----------
    search_compound_dk(compound, limit=5)  ->  dict
"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _id_alignment_search import resolve_compound_ids
from normalization_helpers.paths import card_db_path
from normalization_helpers.compact import compact_card
from normalization_helpers.db_helpers import open_db
from normalization_helpers.strict_id_inputs import refinement_errors_as_results
from ThermoML_raw_json_to_card_db_parsers.id_schema import require_global_id

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

@refinement_errors_as_results
def search_compound_dk(compound: str | list[str], limit: int = 5) -> dict:
    """Return compound identity / domain-knowledge cards matching *compound*.

    Parameters
    ----------
    compound : str | list[str], optional
        Compound name, formula, SMILES, InChI, InChI-key, comp_num_id,
        or strict ``"GLOBcomp_N"`` string. Semicolon-separated for multiple.
        Bare numbers and retired unscoped IDs return a refinement error.
    limit : int, optional
        Maximum number of results (default 5).

    Returns
    -------
    dict
        ``query``  – the original input
        ``n_results`` – number of cards returned
        ``results`` – list of dicts, each containing:
            ``comp_num_id``, ``match_score``, ``match_type``,
            and the full card data merged in.
    """
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise TypeError("limit must be a positive integer")
    candidates = resolve_compound_ids(compound)
    if not candidates:
        return {
            "query": compound,
            "n_results": 0,
            "results": [],
            "error": f"Could not resolve compound {compound!r} to a global ID.",
            "error_code": "QUERY_REFINEMENT_REQUIRED",
        }

    db_path = card_db_path("CCS_ID_DK")
    results = []

    con = open_db(db_path)
    try:
        cur = con.cursor()
        for cand in candidates:
            cid = cand["comp_num_id"]
            row = cur.execute(
                "SELECT json_data, smiles, fp_status FROM cards WHERE comp_num_id = ?", (cid,)
            ).fetchone()
            if row is None:
                continue
            card = json.loads(row[0])
            require_global_id("comp_num_id", card["comp_num_id"])
            if card["comp_num_id"] != cid:
                raise ValueError("CCS_ID_DK row/card comp_num_id mismatch")
            results.append({
                "comp_num_id": cid,
                "match_score": cand["score"],
                "match_type": cand["match_type"],
                "smiles": row[1],
                "has_fingerprint": row[2] == "ok",
                "compact_md": compact_card("CCS_ID_DK", card),
                **card,
            })
    finally:
        con.close()

    return {
        "query": compound,
        "n_results": len(results),
        "results": results,
    }


# ---------------------------------------------------------------------------
# Demo / quick smoke-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    test_queries = ["water", "CCO", "ethanol"]
    for q in test_queries:
        print(f"\n{'='*60}")
        print(f"Query: {q!r}")
        print("=" * 60)
        resp = search_compound_dk(compound=q)
        print(f"  n_results: {resp['n_results']}")
        for r in resp["results"]:
            name = r["names"]["primary_name"]
            ik = r["identity"]["inchi_key"]
            print(
                f"  comp_num_id={r['comp_num_id']}  "
                f"score={r['match_score']}  "
                f"type={r['match_type']}  "
                f"name={name}  inchi_key={ik}"
            )
