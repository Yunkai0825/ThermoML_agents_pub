"""
5_meas_DK_search.py
-------------------
Search MTDKS_ID_DK.db for measurement technique identity and domain-knowledge
cards.

Given a measurement method query (name, meas_id, acronym), resolve it to
meas_num_id(s) via normalisation helpers, then retrieve the full JSON card
from the MTDKS_ID_DK database. Text aliases are resolved by the canonical
measurement-alias registry before the global card lookup.

Public API
----------
    search_measurement_dk(measurement, limit=5)  ->  dict
"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _id_alignment_search import resolve_measurement_ids
from normalization_helpers.paths import card_db_path
from normalization_helpers.compact import compact_card
from normalization_helpers.db_helpers import open_db
from normalization_helpers.strict_id_inputs import refinement_errors_as_results
from ThermoML_raw_json_to_card_db_parsers.id_schema import require_global_id

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

@refinement_errors_as_results
def search_measurement_dk(measurement: str | list[str], limit: int = 5) -> dict:
    """Return measurement identity / domain-knowledge cards matching *measurement*.

    Parameters
    ----------
    measurement : str | list, optional
        Measurement method name, meas_id, canonical ``GLOBmeas_N``,
        or acronym (e.g. ``"DSC"``).  Semicolon-separated for multiple.
    limit : int, optional
        Maximum number of results (default 5).

    Returns
    -------
    dict
        ``query``      – the original input
        ``n_results``  – number of cards returned
        ``results``    – list of dicts, each containing:
            ``meas_num_id``, ``meas_id``, ``match_score``, ``match_type``,
            and the full card data merged in.
    """
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise TypeError("limit must be a positive integer")
    candidates = resolve_measurement_ids(measurement)
    if not candidates:
        return {
            "query": measurement,
            "n_results": 0,
            "results": [],
            "error": f"Could not resolve measurement {measurement!r} to a global ID.",
            "error_code": "QUERY_REFINEMENT_REQUIRED",
        }

    db_path = card_db_path("MTDKS_ID_DK")
    results = []
    seen: set = set()

    con = open_db(db_path)
    try:
        cur = con.cursor()

        # ── Primary pass: normalization-resolved candidates ───────────────
        for cand in candidates:
            mid = cand["meas_num_id"]
            if mid in seen:
                continue
            row = cur.execute(
                "SELECT meas_id, json_data FROM cards WHERE meas_num_id = ?",
                (mid,),
            ).fetchone()
            if row is None:
                continue
            seen.add(mid)
            card = json.loads(row[1])
            require_global_id("meas_num_id", card["meas_num_id"])
            if card["meas_num_id"] != mid or card["meas_ID"] != row[0]:
                raise ValueError("MTDKS_ID_DK row/card identity mismatch")
            results.append({
                "meas_num_id": mid,
                "meas_id": row[0],
                "match_score": cand["score"],
                "match_type": cand["match_type"],
                "compact_md": compact_card("MTDKS_ID_DK", card),
                **card,
            })

    finally:
        con.close()

    limited_results = results[:limit]
    return {
        "query": measurement,
        "n_results": len(limited_results),
        "n_matches": len(results),
        "results": limited_results,
    }


# ---------------------------------------------------------------------------
# Demo / quick smoke-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    test_queries = ["DSC", "viscosity", "hot wire"]
    for q in test_queries:
        print(f"\n{'='*60}")
        print(f"Query: {q!r}")
        print("=" * 60)
        resp = search_measurement_dk(measurement=q)
        print(f"  n_results: {resp['n_results']}")
        for r in resp["results"]:
            name = r["identity"]["name"]
            family = r["identity"]["measurement_family"]
            print(
                f"  meas_num_id={r['meas_num_id']}  "
                f"meas_id={r['meas_id']}  "
                f"score={r['match_score']}  "
                f"type={r['match_type']}  "
                f"name={name}  family={family}"
            )
