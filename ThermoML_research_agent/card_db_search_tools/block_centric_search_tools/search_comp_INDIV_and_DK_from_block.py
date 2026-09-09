"""
Block-centric compound lookup — given block identifiers (doi/lit_num_id +
block_number), fetch the associated CCS_INDIV (per-DOI compound card) and
CCS_ID_DK (domain knowledge) cards for every compound in that block.

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
    """Fetch one PCS_INDIV card row."""
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


def _fetch_ccs_card(doi: str) -> dict:
    con = open_db(card_db_path("CCS_INDIV"))
    try:
        row = con.execute(
            "SELECT json_data FROM cards WHERE doi = ?", (doi,)
        ).fetchone()
    finally:
        con.close()
    if row is None:
        raise LookupError(f"CCS_INDIV card not found for DOI {doi!r}")
    return json.loads(row[0])


# ── public API ───────────────────────────────────────────────────────────────

@refinement_errors_as_results
def search_comp_from_block(
    *,
    block_number: str,
    BLKsubsys_id: str | None = None,
    doi: str | None = None,
    lit_num_id: str | None = None,
) -> dict:
    """Return CCS_INDIV + CCS_ID_DK markdown for compounds in a block.

    Parameters
    ----------
    doi / lit_num_id : identifies the PCS_INDIV card (provide one).
    block_number     : exact ``PROPblock_N`` or ``RXNblock_N`` identifier.

    Returns
    -------
    dict with keys:
        ``doi``, ``lit_num_id``, ``block_number``,
        ``comp_num_ids`` — list of compound IDs found,
        ``ccs_indiv_md`` — CCS_INDIV markdown for this DOI,
        ``ccs_dk`` — list of dicts with ``comp_num_id`` and ``md``.
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

    compounds = block["compounds"]
    if subsystem is not None:
        retained = {
            item["comp_num_id"] for item in subsystem["retained_components"]
        }
        compounds = [
            item for item in compounds if item["comp_num_id"] in retained
        ]
    comp_ids = sorted({item["comp_num_id"] for item in compounds})

    # Project the DOI compound card to this exact target. Returning the
    # complete DOI card would re-introduce compounds excluded by BLKsubsys.
    ccs_card = _fetch_ccs_card(card_doi)
    comp_id_set = set(comp_ids)
    projected_compounds = [
        item for item in ccs_card["compounds"]
        if item["comp_num_id"] in comp_id_set
    ]
    if {item["comp_num_id"] for item in projected_compounds} != comp_id_set:
        raise LookupError(
            "CCS_INDIV is missing a compound required by the PCS target"
        )
    ccs_indiv_md = compact_card(
        "CCS_INDIV",
        {"key": ccs_card["key"], "compounds": projected_compounds},
    )

    # CCS_ID_DK — one card per compound
    ccs_dk = []
    for cid in comp_ids:
        md = resolve_card_md("CCS_ID_DK", comp_num_id=cid)
        ccs_dk.append({"comp_num_id": cid, "md": md})

    return {
        "doi": card_doi,
        "lit_num_id": card_lit,
        "block_number": block["block_number"],
        "BLKsubsys_id": BLKsubsys_id,
        "comp_num_ids": comp_ids,
        "ccs_indiv_md": ccs_indiv_md,
        "ccs_dk": ccs_dk,
    }


# ── demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    result = search_comp_from_block(doi="10.1016/j.jct.2005.03.012",
                                     block_number="PROPblock_1")
    print(f"DOI:  {result['doi']}")
    print(f"Block: {result['block_number']}")
    print(f"Compounds: {result.get('comp_num_ids')}")
    print(f"\n--- CCS_INDIV ({len(result.get('ccs_indiv_md',''))} chars) ---")
    print(result.get("ccs_indiv_md", "")[:400])
    for dk in result.get("ccs_dk", []):
        print(f"\n--- CCS_ID_DK comp#{dk['comp_num_id']} ({len(dk['md'])} chars) ---")
        print(dk["md"][:300])
