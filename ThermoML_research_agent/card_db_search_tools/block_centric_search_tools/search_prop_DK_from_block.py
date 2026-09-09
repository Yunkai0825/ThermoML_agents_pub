"""
Block-centric property domain-knowledge lookup — given block identifiers
(doi/lit_num_id + block_number), fetch the PCS_ID_DK (property domain
knowledge) cards for every property referenced in that block.

No PCS_INDIV is fetched because the block *is* from PCS_INDIV already.

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


# ── public API ───────────────────────────────────────────────────────────────

@refinement_errors_as_results
def search_prop_dk_from_block(
    *,
    block_number: str,
    BLKsubsys_id: str | None = None,
    doi: str | None = None,
    lit_num_id: str | None = None,
) -> dict:
    """Return PCS_ID_DK markdown for every property in a block.

    Parameters
    ----------
    doi / lit_num_id : identifies the PCS_INDIV card (provide one).
    block_number     : exact ``PROPblock_N`` or ``RXNblock_N`` identifier.

    Returns
    -------
    dict with keys:
        ``doi``, ``lit_num_id``, ``block_number``,
        ``prop_num_ids`` — list of property IDs found,
        ``pcs_dk`` — list of dicts with ``prop_num_id`` and ``md``.
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
    prop_ids = sorted({item["prop_num_id"] for item in properties})

    # PCS_ID_DK — one card per property
    pcs_dk = []
    for pid in prop_ids:
        md = resolve_card_md("PCS_ID_DK", prop_num_id=pid)
        pcs_dk.append({"prop_num_id": pid, "md": md})

    return {
        "doi": card_doi,
        "lit_num_id": card_lit,
        "block_number": block["block_number"],
        "BLKsubsys_id": BLKsubsys_id,
        "prop_num_ids": prop_ids,
        "pcs_dk": pcs_dk,
    }


# ── demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    result = search_prop_dk_from_block(doi="10.1016/j.jct.2005.03.012",
                                        block_number="PROPblock_1")
    print(f"DOI:  {result['doi']}")
    print(f"Block: {result['block_number']}")
    print(f"Properties: {result.get('prop_num_ids')}")
    for dk in result.get("pcs_dk", []):
        print(f"\n--- PCS_ID_DK prop#{dk['prop_num_id']} ({len(dk['md'])} chars) ---")
        print(dk["md"][:300])
