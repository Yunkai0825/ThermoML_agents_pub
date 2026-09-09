"""
Tool-result compactor — query agent subclass + compactor re-exports.
====================================================================
Inherits ``ToolResultCompactor`` and wires the query-agent-specific
LLM client, config, and compactor catalog built from ``COMPACTOR_FUNCTIONS``.

Also re-exports the individual compactors from
``card_db_search_tools/_tools_results_compactors`` so that all
query-agent consumers import from this single location.
"""

from __future__ import annotations

import sys
from pathlib import Path as _Path

from ...ThermoML_query_argo_config import AGENT_CONFIG as _cfg
from ....general_db_query_engine.general_tool_management_helpers.general_tool_results_compactor_agentic_hooks import (
    ToolResult,
    ToolResultCompactor,
)
from ....general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import (
    CompactorCatalog,
)
from ..tracking_hooks.reasoning_hooks import query_reasoning_tracker as _reasoning
from ...query_agent_argo_engine.argo_client import QueryClient as _QueryClient

# ── sys.path setup for card_db_search_tools ────────────────────
_SEARCH_TOOLS_ROOT = _Path(__file__).resolve().parents[4] / "card_db_search_tools"
if str(_SEARCH_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_SEARCH_TOOLS_ROOT))

# ── Structured compactor functions ─────────────────────────────
from _tools_results_compactors import COMPACTOR_FUNCTIONS             # noqa: F401

# ── Build the compactor catalog from tagged functions ─────────────
COMPACTOR_CATALOG = CompactorCatalog.from_functions(COMPACTOR_FUNCTIONS)
COMPACTOR_REGISTRY = COMPACTOR_CATALOG.registry

__all__ = ["QueryToolResultCompactor", "ToolResult",
           "COMPACTOR_CATALOG", "COMPACTOR_REGISTRY"]

# Lazy client singleton
_client = None


def _query_client_factory():
    global _client
    if _client is None:
        _client = _QueryClient.for_l1()
    return _client

# ── Basic search-tool compactors ───────────────────────────────
from _tools_results_compactors.basic_search_tools.compactors import (  # noqa: F401
    compact_resolve_compound_ids,
    compact_resolve_property_ids,
    compact_resolve_measurement_ids,
    compact_resolve_reference_ids,
    compact_resolve_variable_ids,
    compact_resolve_constraint_ids,
    compact_resolve_phase_ids,
    compact_resolve_ids,
    compact_search_id_alignment,
    compact_search_blocks,
    compact_search_system_registry,
    compact_search_system_summary,
    compact_search_similar_compounds,
)
from _tools_results_compactors.basic_search_tools.block_search_adv_compactor import (  # noqa: F401
    compact_block_search_adv,
)

# ── Block-centric search-tool compactors ───────────────────────
from _tools_results_compactors.block_centric_search_tools.compactors import (  # noqa: F401
    compact_search_comp_from_block,
    compact_search_meas_from_block,
    compact_search_prop_dk_from_block,
    compact_search_reference_from_block,
)
from specialized_tools_pipelines.property_screening_ranking_tool.interface.agent import (  # noqa: F401
    compact_screen_property_systems,
)


class QueryToolResultCompactor(ToolResultCompactor):
    """Query-agent tool-result subagent — KEEP/DISCARD via QueryClient.

    Uses ``COMPACTOR_CATALOG`` built from ``COMPACTOR_FUNCTIONS`` so that
    ``compact_tool_result(tool_name, data)`` resolves to the correct
    per-tool formatter.
    """

    def __init__(self) -> None:
        super().__init__(
            client_factory=_query_client_factory,
            cfg=_cfg,
            pipeline_label="query",
            compactor_registry=COMPACTOR_REGISTRY,
            reasoning_hook=_reasoning.make_reasoning_hook(),
        )
