"""
Tool-result compactor — main agent subclass.
=============================================
Inherits ``ToolResultCompactor`` and wires the main-agent-specific
LLM client, config, and compactor catalog built from tagged
``COMPACTOR_FUNCTIONS`` via ``CompactorCatalog.from_functions()``.
"""
from __future__ import annotations

from ...ThermoML_main_argo_config import AGENT_CONFIG as _cfg
from ....general_db_query_engine.general_tool_management_helpers.general_tool_results_compactor_agentic_hooks import (
    ToolResult,
    ToolResultCompactor,
)
from ....general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import (
    CompactorCatalog,
)
from ._tool_compactors import COMPACTOR_FUNCTIONS
from ..tracking_hooks.reasoning_hooks import main_reasoning_tracker as _reasoning
from ...main_agent_argo_engine.argo_client import MainClient as _MainClient

# ── Build the compactor catalog from tagged functions ─────────
COMPACTOR_CATALOG = CompactorCatalog.from_functions(COMPACTOR_FUNCTIONS)
COMPACTOR_REGISTRY = COMPACTOR_CATALOG.registry

__all__ = ["MainToolResultCompactor", "ToolResult",
           "COMPACTOR_CATALOG", "COMPACTOR_REGISTRY"]

# Lazy client singleton
_client = None


def _main_client_factory():
    global _client
    if _client is None:
        _client = _MainClient.for_l0()
    return _client


class MainToolResultCompactor(ToolResultCompactor):
    """Main-agent tool-result compactor — hardcoded dict→markdown
    + KEEP/DISCARD via MainClient."""

    def __init__(self) -> None:
        super().__init__(
            client_factory=_main_client_factory,
            cfg=_cfg,
            pipeline_label="main",
            compactor_registry=COMPACTOR_REGISTRY,
            reasoning_hook=_reasoning.make_reasoning_hook(),
        )
