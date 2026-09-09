"""
4_reference_search.py — Search RMS_INDIV.db for reference / paper cards.

Supports multi-criteria search by DOI, author, year, compound, property,
journal, and free-text title keywords.

Public API
----------
search_references(literature, author, year, compound, property,
                  journal, title_keywords, limit) -> dict
"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _id_alignment_search import (
    resolve_compound_ids,
    resolve_property_ids,
    resolve_reference_ids,
)
from normalization_helpers.paths import card_db_path
from normalization_helpers.compact import compact_card
from normalization_helpers.db_helpers import open_db
from normalization_helpers.strict_id_inputs import refinement_errors_as_results, SearchValue
from normalization_helpers.range_helpers import validate_range
from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_doi_comp_id,
    require_global_id,
)

# ═════════════════════════════════════════════════════════════════════════════
# Helpers
# ═════════════════════════════════════════════════════════════════════════════

_DB_PATH = card_db_path("RMS_INDIV")


def _card_dict(row, jdata: dict, match_score: int) -> dict:
    """Build a flat result dict from a DB row + parsed JSON."""
    required = {"bibliographic", "identity", "data_inventory"}
    missing = required - jdata.keys()
    if missing:
        raise ValueError(f"RMS card is missing fields {sorted(missing)}")
    bib = jdata["bibliographic"]
    ident = jdata["identity"]
    inv = jdata["data_inventory"]
    for field in ("authors", "volume", "pages"):
        if field not in bib:
            raise ValueError(f"RMS bibliographic object is missing {field}")
    for field in ("lit_id", "lit_num_id"):
        if field not in ident:
            raise ValueError(f"RMS identity object is missing {field}")
    for field in (
        "compound_list", "properties", "property_groups", "system_types",
        "n_datapoints",
    ):
        if field not in inv:
            raise ValueError(f"RMS data_inventory is missing {field}")
    for index, compound in enumerate(inv["compound_list"]):
        require_doi_comp_id(compound["org_num"])
        require_global_id("comp_num_id", compound["comp_num_id"])
    for index, prop in enumerate(inv["properties"]):
        require_global_id("prop_num_id", prop["prop_num_id"])
    return {
        "doi":          row["doi"],
        "lit_num_id":   require_global_id("lit_num_id", row["lit_num_id"]),
        "lit_id":       ident["lit_id"],
        "title":        row["title"],
        "authors":      bib["authors"],
        "journal":      row["journal"],
        "year":         row["year"],
        "volume":       bib["volume"],
        "pages":        bib["pages"],
        "n_compounds":  row["n_compounds"],
        "n_blocks":     row["n_blocks"],
        "compound_list": inv["compound_list"],
        "properties":   inv["properties"],
        "property_groups": inv["property_groups"],
        "system_types": inv["system_types"],
        "n_datapoints": inv["n_datapoints"],
        "compact_md":   compact_card("RMS_INDIV", jdata),
        "match_score":  match_score,
    }


# ═════════════════════════════════════════════════════════════════════════════
# Public API
# ═════════════════════════════════════════════════════════════════════════════

@refinement_errors_as_results
def search_references(
    literature: SearchValue = None,
    author: str | None = None,
    year: int | None = None,
    year_range: list[float] | None = None,
    compound: SearchValue = None,
    property: SearchValue = None,
    journal: str | None = None,
    title_keywords: str | None = None,
    limit: int = 50,
) -> dict:
    """Search RMS_INDIV.db for reference/paper cards.

    Entity parameters accept one name/canonical ``GLOB*`` ID or a native list
    of those strings. Bare numeric and retired IDs are rejected.

    Parameters
    ----------
    literature : str | list, optional
        DOI, lit_id, or lit_num_id.
    author : str, optional
        Author surname (or partial name).  Searched inside JSON authors list.
    year : int or str, optional
        Publication year (exact match on SQL column).
    year_range : tuple/list (min_year, max_year), optional
        Filter to papers published within this year range (inclusive).
        Overrides *year* if both are given.
    compound : str | list, optional
        Compound name, formula, InChI-key, SMILES, comp_num_id, or
        ``GLOBcomp_N``.  Semicolon-separated for multiple.
    property : str | list, optional
        Property name, prop_id, prop_num_id, or ``GLOBprop_N``.
    journal : str, optional
        Journal name substring (SQL LIKE).
    title_keywords : str, optional
        Space-separated keywords; all must appear in the title (SQL LIKE AND).
    limit : int
        Maximum results returned (default 50).

    Returns
    -------
    dict  with keys ``query_params``, ``n_results``, ``results``.
    """
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise TypeError("limit must be a positive integer")
    if year is not None and (isinstance(year, bool) or not isinstance(year, int)):
        raise TypeError("year must be an integer")
    if year_range is not None:
        parsed_range = validate_range(year_range, field="year_range")
        assert parsed_range is not None
        if any(not value.is_integer() for value in parsed_range):
            raise TypeError("year_range values must be integer years")
        year_range = [int(parsed_range[0]), int(parsed_range[1])]
        year = None  # year_range overrides exact year

    # ── Resolve compound / property / literature via hub ──────────────────
    comp_num_ids: set[str] = set()
    if compound is not None:
        comp_hits = resolve_compound_ids(compound)
        if not comp_hits:
            return {
                "query_params": {"compound": compound},
                "n_results": 0,
                "results": [],
                "error": f"Could not resolve compound {compound!r} to a global ID.",
                "error_code": "QUERY_REFINEMENT_REQUIRED",
            }
        comp_num_ids = {c["comp_num_id"] for c in comp_hits}

    prop_ids: set[str] = set()
    if property is not None:
        prop_hits = resolve_property_ids(property)
        if not prop_hits:
            return {
                "query_params": {"property": property},
                "n_results": 0,
                "results": [],
                "error": f"Could not resolve property {property!r} to a global ID.",
                "error_code": "QUERY_REFINEMENT_REQUIRED",
            }
        prop_ids = {p["prop_id"] for p in prop_hits}

    doi: str | None = None
    if literature is not None:
        ref_hits = resolve_reference_ids(literature)
        if not ref_hits:
            return {
                "query_params": {"literature": literature},
                "n_results": 0,
                "results": [],
                "error": f"Could not resolve literature {literature!r} to a global ID.",
                "error_code": "QUERY_REFINEMENT_REQUIRED",
            }
        doi = ref_hits[0]["doi"]

    # ── Build SQL WHERE from column-level criteria ───────────────────────
    clauses = []
    params = []

    if doi:
        clauses.append("doi = ?")
        params.append(doi)

    if year is not None:
        clauses.append("year = ?")
        params.append(year)

    if year_range is not None:
        clauses.append("year >= ? AND year <= ?")
        params.extend([year_range[0], year_range[1]])

    if journal:
        clauses.append("journal LIKE ?")
        params.append(f"%{journal}%")

    if title_keywords:
        for kw in title_keywords.strip().split():
            clauses.append("title LIKE ?")
            params.append(f"%{kw}%")

    # Decide query breadth: if we have SQL clauses, use them; otherwise use
    # a generous LIMIT so we can still filter by JSON-only criteria.
    has_sql_filter = bool(clauses)
    has_json_filter = (author is not None or comp_num_ids
                       or prop_ids)

    if has_sql_filter:
        where = " AND ".join(clauses)
        sql = f"SELECT * FROM cards WHERE {where}"
    else:
        sql = "SELECT * FROM cards"

    # When there are no SQL filters but JSON filters exist, scan all rows.
    # Otherwise respect the user limit for a raw browse.
    fetch_limit = None if has_json_filter and not has_sql_filter else limit * 5

    if fetch_limit is not None:
        sql += f" LIMIT {fetch_limit}"

    # ── Execute query and post-filter ────────────────────────────────────
    conn = open_db(_DB_PATH)
    try:
        rows = conn.execute(sql, params).fetchall()
    finally:
        conn.close()

    # Total criteria count for scoring
    total_criteria = sum(1 for v in (doi, author, year, compound,
                                      property, journal, title_keywords)
                         if v is not None)
    if total_criteria == 0:
        total_criteria = 1  # avoid division by zero on bare queries

    results = []
    author_lower = author.lower() if author else None

    for row in rows:
        jdata = json.loads(row["json_data"])
        score = 0

        # ── SQL-column matches (already guaranteed by WHERE) ─────────
        if doi and row["doi"] == doi:
            score += 1
        if year is not None and row["year"] == year:
            score += 1
        if journal and journal.lower() in row["journal"].lower():
            score += 1
        if title_keywords:
            title_lower = row["title"].lower()
            if all(kw.lower() in title_lower
                   for kw in title_keywords.strip().split()):
                score += 1

        # ── JSON-level filters ───────────────────────────────────────
        # Author
        if author_lower:
            authors = jdata["bibliographic"]["authors"]
            if any(author_lower in a.lower() for a in authors):
                score += 1
            else:
                continue  # hard filter: author must match

        # Compound
        if comp_num_ids:
            inv = jdata["data_inventory"]
            card_comp_ids = {
                require_global_id("comp_num_id", c["comp_num_id"])
                for c in inv["compound_list"]
            }
            if comp_num_ids & card_comp_ids:
                score += 1
            else:
                continue

        # Property
        if prop_ids:
            inv = jdata["data_inventory"]
            card_prop_ids = {p["prop_id"] for p in inv["properties"]}
            if prop_ids & card_prop_ids:
                score += 1
            else:
                continue

        match_score = round(score / total_criteria * 100)
        results.append(_card_dict(row, jdata, match_score))

    # ── Sort and trim ────────────────────────────────────────────────────
    results.sort(key=lambda r: (-r["match_score"], -r["n_datapoints"]))
    results = results[:limit]

    # ── Build response ───────────────────────────────────────────────────
    query_params = {
        "literature": literature,
        "doi_resolved": doi,
        "author": author,
        "year": year,
        "year_range": list(year_range) if year_range else None,
        "compound": compound,
        "compound_resolved_ids": sorted(comp_num_ids) if comp_num_ids else None,
        "property": property,
        "property_resolved_ids": sorted(prop_ids) if prop_ids else None,
        "journal": journal,
        "title_keywords": title_keywords,
        "limit": limit,
    }

    return {
        "query_params": query_params,
        "n_results": len(results),
        "results": results,
    }


# ═════════════════════════════════════════════════════════════════════════════
# CLI demo / smoke tests
# ═════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import pprint

    print("=" * 72)
    print("TEST 1 — DOI lookup")
    print("=" * 72)
    out = search_references(literature="10.1007/s10765-005-5566-6")
    print(f"  n_results: {out['n_results']}")
    if out["results"]:
        r = out["results"][0]
        print(f"  title:  {r['title'][:80]}")
        print(f"  authors: {r['authors']}")
        print(f"  year:   {r['year']}")
        print(f"  score:  {r['match_score']}")
    print()

    print("=" * 72)
    print("TEST 2 — year + compound (methane)")
    print("=" * 72)
    out = search_references(year=2005, compound="methane", limit=5)
    print(f"  compound_resolved_ids: {out['query_params']['compound_resolved_ids']}")
    print(f"  n_results: {out['n_results']}")
    for r in out["results"][:3]:
        print(f"    {r['doi']}  yr={r['year']}  score={r['match_score']}  "
              f"nc={r['n_compounds']}  '{r['title'][:50]}'")
    print()

    print("=" * 72)
    print("TEST 3 — author search")
    print("=" * 72)
    out = search_references(author="Patek", limit=5)
    print(f"  n_results: {out['n_results']}")
    for r in out["results"][:3]:
        print(f"    {r['doi']}  score={r['match_score']}  authors={r['authors']}")
    print()

    print("=" * 72)
    print("TEST 4 — journal + title keywords")
    print("=" * 72)
    out = search_references(journal="Thermophys", title_keywords="conductivity", limit=5)
    print(f"  n_results: {out['n_results']}")
    for r in out["results"][:3]:
        print(f"    {r['doi']}  '{r['title'][:60]}'  score={r['match_score']}")
    print()

    print("=" * 72)
    print("TEST 5 — property search (thermal conductivity)")
    print("=" * 72)
    out = search_references(property="thermal conductivity", limit=5)
    print(f"  property_resolved_ids: {out['query_params']['property_resolved_ids']}")
    print(f"  n_results: {out['n_results']}")
    for r in out["results"][:3]:
        props = [p["name"] for p in r["properties"]]
        print(f"    {r['doi']}  score={r['match_score']}  props={props}")
