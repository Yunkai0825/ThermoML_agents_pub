"""main_agent_toobox — tools for the ThermoML Main Agent."""
from .tool_catalog import (
    MainCatalog,
    MAIN_CATALOG,
    COMPACTOR_CATALOG,
    COMPACTOR_REGISTRY,
    ToolResult,
)
from .subagent_delegation_tools import (
    run_query_agent,
    run_analysis_agent,
    run_parallel_subagents,
)
from .tool_menu import (
    browse_subagent_tools,
    run_subagent_tool,
)

__all__ = [
    "MainCatalog",
    "MAIN_CATALOG",
    "COMPACTOR_CATALOG",
    "COMPACTOR_REGISTRY",
    "ToolResult",
    "run_query_agent",
    "run_analysis_agent",
    "run_parallel_subagents",
    "browse_subagent_tools",
    "run_subagent_tool",
]
