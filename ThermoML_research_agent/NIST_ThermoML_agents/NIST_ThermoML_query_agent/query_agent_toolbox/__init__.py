"""
query_agent_toolbox — tool helpers for the ThermoML Query Agent.
================================================================
Single entry point: ``tool_catalog``.

Public API
----------
QueryL0Catalog
    Class-based L0 memory tool catalog.
L0_CATALOG
    Instantiated catalog for the L0 orchestrator.
ToolResult
    Result container for compacted tool outputs.
COMPACTOR_CATALOG, COMPACTOR_REGISTRY
    Structured catalog and flat dict of compactors per search tool.
"""

from .tool_catalog import (
    QueryL0Catalog,
    L0_CATALOG,
    ToolResult,
    COMPACTOR_CATALOG,
    COMPACTOR_REGISTRY,
)

__all__ = [
    "QueryL0Catalog",
    "L0_CATALOG",
    "ToolResult",
    "COMPACTOR_CATALOG", "COMPACTOR_REGISTRY",
]
