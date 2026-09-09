"""Phase 0 — Compound & property resolution tools.

Each function returns a raw dict.  The catalog's ``wrap_tool`` handles
compaction (Layer 1) and agentic KEEP/DISCARD (Layer 2).
"""

from __future__ import annotations

from ...general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import (
    ToolEntry,
    uses_compactors,
)
from ..analysis_agent_context_hooks.compactor_hooks._tool_compactors import (
    compact_resolve_compounds,
    compact_resolve_properties,
)
import sys
from pathlib import Path

_WORKSPACE = Path(__file__).resolve().parents[3]
if str(_WORKSPACE) not in sys.path:
    sys.path.insert(0, str(_WORKSPACE))

from card_db_search_tools.basic_search_tools._id_alignment_search import (
    resolve_compound_ids,
    resolve_property_ids,
)
from card_db_search_tools.basic_search_tools.normalization_helpers.strict_id_inputs import (
    refinement_errors_as_results,
)


@uses_compactors(compact_resolve_compounds)
@refinement_errors_as_results
def resolve_compounds(compound_queries: list[str]) -> dict:
    """Resolve compound names or strict ``GLOBcomp_N`` IDs.

    Parameters
    ----------
    compound_queries : list[str]
        Compound names or strict ``GLOBcomp_N`` IDs.
    """
    if not isinstance(compound_queries, list) or not compound_queries:
        raise TypeError("compound_queries must be a non-empty array of strings")
    if any(not isinstance(name, str) or not name.strip() for name in compound_queries):
        raise TypeError("every compound_queries entry must be a non-empty string")
    results = {}
    for name in compound_queries:
        resolved = resolve_compound_ids(name)
        results[name] = resolved
    return {"resolved_compounds": results}


@uses_compactors(compact_resolve_properties)
@refinement_errors_as_results
def resolve_properties(property_queries: list[str]) -> dict:
    """Resolve property names or strict ``GLOBprop_N`` IDs.

    Parameters
    ----------
    property_queries : list[str]
        Property names or strict ``GLOBprop_N`` IDs.
    """
    if not isinstance(property_queries, list) or not property_queries:
        raise TypeError("property_queries must be a non-empty array of strings")
    if any(not isinstance(name, str) or not name.strip() for name in property_queries):
        raise TypeError("every property_queries entry must be a non-empty string")
    results = {}
    for name in property_queries:
        resolved = resolve_property_ids(name)
        results[name] = resolved
    return {"resolved_properties": results}


# ── Catalog entries ─────────────────────────────────────────────────────

TOOL_ENTRIES = [
    ToolEntry(
        "resolve_compounds", resolve_compounds,
        group="resolve",
    ),
    ToolEntry(
        "resolve_properties", resolve_properties,
        group="resolve",
    ),
]
