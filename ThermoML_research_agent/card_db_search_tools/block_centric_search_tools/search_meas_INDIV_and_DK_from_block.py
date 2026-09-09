"""
Block-centric measurement lookup — given block identifiers (doi/lit_num_id +
block_number), fetch the associated MTDKS_INDIV (per-DOI measurement card)
and MTDKS_ID_DK (domain knowledge) cards for every measurement method
referenced by that block's properties.

Returns compact markdown for each card via ``resolve_card_md``.
"""

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BASIC = os.path.normpath(os.path.join(_HERE, os.pardir, "basic_search_tools"))
if _BASIC not in sys.path:
    sys.path.insert(0, _BASIC)

from _id_alignment_search import resolve_card_md
from normalization_helpers.compact import compact_card
from normalization_helpers.db_helpers import open_db, resolve_pcs_block_target
from normalization_helpers.paths import card_db_path
from normalization_helpers.strict_id_inputs import (
    refinement_errors_as_results,
    require_global_tool_id,
)


# ── helpers ──────────────────────────────────────────────────────────────────

def _fetch_pcs_card(doi: str | None = None, lit_num_id: str | None = None):
    db = card_db_path("PCS_INDIV")
    con = open_db(db)
    try:
        if doi is not None:
            row = con.execute(
                "SELECT json_data FROM cards WHERE doi = ?", (doi,)
            ).fetchone()
        elif lit_num_id is not None:
            lit_num_id = require_global_tool_id(
                "reference", lit_num_id, field="lit_num_id"
            )
            row = con.execute(
                "SELECT json_data FROM cards WHERE lit_num_id = ?", (lit_num_id,)
            ).fetchone()
        else:
            raise ValueError("Exactly one of doi or lit_num_id is required")
    finally:
        con.close()
    return json.loads(row[0]) if row else None


def _fetch_mtdks_card(doi: str) -> dict:
    con = open_db(card_db_path("MTDKS_INDIV"))
    try:
        row = con.execute(
            "SELECT json_data FROM cards WHERE doi = ?", (doi,)
        ).fetchone()
    finally:
        con.close()
    if row is None:
        raise LookupError(f"MTDKS_INDIV card not found for DOI {doi!r}")
    return json.loads(row[0])


def _project_mtdks_card(
    card: dict,
    *,
    block_number: str,
    meas_num_ids: set[str],
    prop_num_ids: set[str],
) -> dict:
    methods = []
    for source in card["methods"]:
        if (
            source["meas_num_id"] not in meas_num_ids
            or block_number not in source["block_numbers"]
        ):
            continue
        method = dict(source)
        method["block_numbers"] = [block_number]
        method["properties"] = [
            prop for prop in source["properties"]
            if prop["prop_num_id"] in prop_num_ids
        ]
        if not method["properties"]:
            continue
        method["instance_count"] = 1
        methods.append(method)
    if {item["meas_num_id"] for item in methods} != meas_num_ids:
        raise LookupError(
            "MTDKS_INDIV is missing a measurement method required by the PCS target"
        )
    return {
        "key": card["key"],
        "methods_summary": {
            "n_unique_methods": len(methods),
            "n_standard": sum(
                item["method_type"] == "standard" for item in methods
            ),
            "n_custom": sum(
                item["method_type"] == "custom" for item in methods
            ),
        },
        "methods": methods,
    }


# ── public API ───────────────────────────────────────────────────────────────

@refinement_errors_as_results
def search_meas_from_block(
    *,
    block_number: str,
    BLKsubsys_id: str | None = None,
    doi: str | None = None,
    lit_num_id: str | None = None,
) -> dict:
    """Return MTDKS_INDIV + MTDKS_ID_DK markdown for measurements in a block.

    Parameters
    ----------
    doi / lit_num_id : identifies the PCS_INDIV card (provide one).
    block_number     : exact ``PROPblock_N`` or ``RXNblock_N`` identifier.

    Returns
    -------
    dict with keys:
        ``doi``, ``lit_num_id``, ``block_number``,
        ``meas_num_ids`` — list of measurement IDs found,
        ``mtdks_indiv_md`` — MTDKS_INDIV markdown for this DOI,
        ``mtdks_dk`` — list of dicts with ``meas_num_id`` and ``md``.
    """
    if (doi is None) == (lit_num_id is None):
        raise ValueError("Provide exactly one of doi or lit_num_id")
    card = _fetch_pcs_card(doi=doi, lit_num_id=lit_num_id)
    if card is None:
        raise LookupError("PCS_INDIV card not found")

    key = card["key"]
    card_doi = key["doi"]
    card_lit = key["lit_num_id"]

    block, subsystem = resolve_pcs_block_target(
        card, block_number, BLKsubsys_id
    )

    properties = block["properties"]
    if subsystem is not None:
        supported = {
            item["BLKprop_id"]
            for item in subsystem["property_support"]
            if item["role"] == "bulk_property"
            and item["phase_compatible"] is True
        }
        properties = [
            item for item in properties if item["BLKprop_id"] in supported
        ]
    meas_ids = sorted({item["meas_num_id"] for item in properties})
    prop_ids = {item["prop_num_id"] for item in properties}

    # Project the DOI measurement card to this exact target. A full DOI-level
    # card can mention methods/properties from unrelated blocks.
    mtdks_card = _fetch_mtdks_card(card_doi)
    mtdks_indiv_md = compact_card(
        "MTDKS_INDIV",
        _project_mtdks_card(
            mtdks_card,
            block_number=block["block_number"],
            meas_num_ids=set(meas_ids),
            prop_num_ids=prop_ids,
        ),
    )

    # MTDKS_ID_DK — one card per measurement method
    mtdks_dk = []
    for mid in meas_ids:
        md = resolve_card_md("MTDKS_ID_DK", meas_num_id=mid)
        mtdks_dk.append({"meas_num_id": mid, "md": md})

    return {
        "doi": card_doi,
        "lit_num_id": card_lit,
        "block_number": block["block_number"],
        "BLKsubsys_id": BLKsubsys_id,
        "meas_num_ids": meas_ids,
        "mtdks_indiv_md": mtdks_indiv_md,
        "mtdks_dk": mtdks_dk,
    }


# ── demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    result = search_meas_from_block(doi="10.1016/j.jct.2005.03.012",
                                     block_number="PROPblock_1")
    print(f"DOI:  {result['doi']}")
    print(f"Block: {result['block_number']}")
    print(f"Measurements: {result.get('meas_num_ids')}")
    print(f"\n--- MTDKS_INDIV ({len(result.get('mtdks_indiv_md',''))} chars) ---")
    print(result.get("mtdks_indiv_md", "")[:400])
    for dk in result.get("mtdks_dk", []):
        print(f"\n--- MTDKS_ID_DK meas#{dk['meas_num_id']} ({len(dk['md'])} chars) ---")
        print(dk["md"][:300])
