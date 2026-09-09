"""
Block-centric reference lookup — given block identifiers (doi/lit_num_id +
block_number), fetch the RMS_INDIV (reference/metadata) card for the
publication that contains that block.

Returns compact markdown via ``resolve_card_md``.
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
def search_reference_from_block(
    *,
    block_number: str,
    BLKsubsys_id: str | None = None,
    doi: str | None = None,
    lit_num_id: str | None = None,
) -> dict:
    """Return RMS_INDIV markdown for the reference that contains a block.

    Parameters
    ----------
    doi / lit_num_id : identifies the PCS_INDIV card (provide one).
    block_number     : exact ``PROPblock_N`` or ``RXNblock_N`` identifier.
                       Used only to confirm the block exists and to report
                       its block_number in the result.

    Returns
    -------
    dict with keys:
        ``doi``, ``lit_num_id``, ``block_number``,
        ``rms_indiv_md`` — RMS_INDIV markdown for this DOI.
    """
    if (doi is None) == (lit_num_id is None):
        raise ValueError("Provide exactly one of doi or lit_num_id")
    card = _fetch_pcs_card(doi=doi, lit_num_id=lit_num_id)
    if card is None:
        raise LookupError("PCS_INDIV card not found")

    key = card["key"]
    card_doi = key["doi"]
    card_lit = key["lit_num_id"]

    block, _ = resolve_pcs_block_target(card, block_number, BLKsubsys_id)

    # RMS_INDIV — one card per DOI
    rms_md = resolve_card_md("RMS_INDIV", doi=card_doi)

    return {
        "doi": card_doi,
        "lit_num_id": card_lit,
        "block_number": block["block_number"],
        "BLKsubsys_id": BLKsubsys_id,
        "rms_indiv_md": rms_md,
    }


# ── demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    result = search_reference_from_block(doi="10.1016/j.jct.2005.03.012",
                                          block_number="PROPblock_1")
    print(f"DOI:  {result['doi']}")
    print(f"Block: {result['block_number']}")
    print(f"\n--- RMS_INDIV ({len(result.get('rms_indiv_md',''))} chars) ---")
    print(result.get("rms_indiv_md", "")[:500])
