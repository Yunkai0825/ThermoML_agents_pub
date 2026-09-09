"""
Tool-result compactor — analysis agent subclass.
=================================================
Inherits ``ToolResultCompactor`` and wires the analysis-agent-specific
LLM client, config, and compactor catalog built from tagged
``COMPACTOR_FUNCTIONS`` via ``CompactorCatalog.from_functions()``.
"""

from __future__ import annotations

from ...ThermoML_analysis_argo_config import AGENT_CONFIG as _cfg
from ....general_db_query_engine.general_tool_management_helpers.general_tool_results_compactor_agentic_hooks import (
    ToolResult,
    ToolResultCompactor,
)
from ....general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import (
    CompactorCatalog,
)
from ..tracking_hooks.reasoning_hooks import analysis_reasoning_tracker as _reasoning
from ._tool_compactors import COMPACTOR_FUNCTIONS
from ...analysis_agent_argo_engine.argo_client import AnalysisClient as _AnalysisClient

# ── Build the compactor catalog from tagged functions ─────────
COMPACTOR_CATALOG = CompactorCatalog.from_functions(COMPACTOR_FUNCTIONS)
COMPACTOR_REGISTRY = COMPACTOR_CATALOG.registry

__all__ = ["AnalysisToolResultCompactor", "ToolResult",
           "COMPACTOR_CATALOG", "COMPACTOR_REGISTRY"]

# Lazy client singleton
_client = None


def _analysis_client_factory():
    global _client
    if _client is None:
        _client = _AnalysisClient.for_l1_data()
    return _client


class AnalysisToolResultCompactor(ToolResultCompactor):
    """Analysis-agent tool-result compactor — hardcoded dict→markdown
    + KEEP/DISCARD via AnalysisClient.

    Uses ``COMPACTOR_CATALOG`` built from tagged ``COMPACTOR_FUNCTIONS``
    via ``CompactorCatalog.from_functions()`` so that
    ``compact_tool_result(tool_name, data)`` resolves to the correct
    per-tool formatter.
    """

    def __init__(self) -> None:
        super().__init__(
            client_factory=_analysis_client_factory,
            cfg=_cfg,
            pipeline_label="analysis",
            compactor_registry=COMPACTOR_REGISTRY,
            reasoning_hook=_reasoning.make_reasoning_hook(),
        )
