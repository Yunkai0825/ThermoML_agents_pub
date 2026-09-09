"""Hardcoded data tools — deterministic block inspection.

These tools call ``extract_block_arrays()`` and ``identify_columns()``
directly and return raw dicts.  Compaction (dict→markdown) is handled
by the ``AnalysisCatalog`` wrapper layer — individual tool functions
no longer import compactors or produce ``ToolResult``.
"""

from __future__ import annotations

import numpy as np

from ...general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import (
    ToolEntry,
    uses_compactors,
)
from ..analysis_agent_context_hooks.compactor_hooks._tool_compactors import (
    compact_inspect_block,
)
from ..ThermoML_core_calc_tools.csv_io_helpers import (
    extract_block_arrays,
    identify_columns,
)
from ..ThermoML_core_calc_tools.property_response_preparation import (
    inspect_property_response_contract,
)


# ------------------------------------------------------------------
#  inspect_block  (hardcoded — no LLM subagent)
# ------------------------------------------------------------------

@uses_compactors(compact_inspect_block)
def inspect_block(
    doi: str,
    block_number: str,
    BLKsubsys_id: str | None = None,
    property_filter: str = "",
) -> dict:
    """Inspect a block's structure: column names, row count, value ranges.

    Deterministic — calls extract_block_arrays + identify_columns,
    returns compact markdown directly.

    Parameters
    ----------
    doi : str
        Paper DOI.
    block_number : str
        Strict typed block identifier (e.g. ``"PROPblock_2"`` or
        ``"RXNblock_2"``). Legacy ``block_N`` and bare numbers are rejected.
    property_filter : str
        Only include property columns matching this substring.
    """
    bd = extract_block_arrays(
        doi, block_number,
        BLKsubsys_id=BLKsubsys_id,
        property_filter=property_filter or None,
    )
    if not bd.ok:
        return {"error": bd.error, "doi": doi, "block_number": block_number, "BLKsubsys_id": BLKsubsys_id}

    match = identify_columns(bd.columns, property_filter, metadata=bd.metadata)
    property_response_contracts = [
        inspect_property_response_contract(bd.metadata, column)
        for column in match.y_columns
    ]

    raw = {
        "doi": bd.doi,
        "lit_num_id": bd.metadata["lit_num_id"],
        "block_number": bd.block_number,
        "BLKsubsys_id": bd.BLKsubsys_id,
        "block_type": bd.metadata["block_type"],
        "compounds": bd.metadata["compounds"],
        "compound_map": bd.metadata["compound_map"],
        "variables": bd.metadata["variables"],
        "properties": bd.metadata["properties"],
        "constraints": bd.metadata["constraints"],
        "solvents": bd.metadata["solvents"],
        "columns": bd.columns,
        "n_rows": bd.n_rows,
        "identified_x": match.x_columns,
        "identified_y": match.y_columns,
        "property_response_contracts": property_response_contracts,
        "column_compound_map": match.column_compound_map,
        "column_ranges": {
            col: {
                "min": round(float(np.nanmin(arr)), 6) if np.any(~np.isnan(arr)) else None,
                "max": round(float(np.nanmax(arr)), 6) if np.any(~np.isnan(arr)) else None,
                "n_valid": int(np.count_nonzero(~np.isnan(arr))),
            }
            for col, arr in bd.arrays.items()
            if col not in {"BLKpoint_id", "_source"}
        },
    }
    return raw


# ── Catalog entries ─────────────────────────────────────────────────────

TOOL_ENTRIES = [
    ToolEntry(
        "inspect_block", inspect_block,
        group="hardcoded_data",
        skip_subagent=True,
    ),
]
