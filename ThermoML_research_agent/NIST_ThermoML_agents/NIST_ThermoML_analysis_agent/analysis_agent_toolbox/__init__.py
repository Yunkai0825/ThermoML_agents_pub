"""
analysis_agent_toolbox — Analysis agent tool implementations.
=============================================================
Single entry point: ``tool_catalog``.

Architecture:
  - Query tools delegate to the ThermoML query agent via L1 workers.
  - Hardcoded tools (inspect_block, get_pure_values) are deterministic —
    no LLM subagent, no direct DB queries.
  - Fitting tools return compact markdown directly (no LLM subagent).
"""

from .tool_catalog import (
    AnalysisCatalog,
    ANALYSIS_CATALOG,
    COMPACTOR_REGISTRY,
    ToolResult,
)

# Individual tool functions (re-exported from their own modules)
from .query_delegation_tools import query_thermoml, query_thermoml_parallel
from .hardcoded_data_tools import inspect_block
from .discovery_tools import get_pure_values
from .fitting_tools import (
    fit_block,
    fit_multi_system,
    compute_ideal_baseline,
    predict_from_rk,
)

__all__ = [
    # Catalog class
    "AnalysisCatalog",
    # Catalog instance
    "ANALYSIS_CATALOG",
    # Compaction
    "COMPACTOR_REGISTRY", "compact_tool_result",
    # ToolResult
    "ToolResult",
    # Tool functions
    "query_thermoml", "query_thermoml_parallel",
    "inspect_block", "get_pure_values",
    "fit_block", "fit_multi_system", "compute_ideal_baseline", "predict_from_rk",
]
