"""compactor_hooks — re-export compaction classes for the main agent."""
from .context_stage_compaction import MainStageCompactor
from .tool_result_compactor import (
    MainToolResultCompactor,
    ToolResult,
    COMPACTOR_CATALOG,
    COMPACTOR_REGISTRY,
)

__all__ = [
    "MainStageCompactor",
    "MainToolResultCompactor",
    "ToolResult",
    "COMPACTOR_CATALOG",
    "COMPACTOR_REGISTRY",
]
