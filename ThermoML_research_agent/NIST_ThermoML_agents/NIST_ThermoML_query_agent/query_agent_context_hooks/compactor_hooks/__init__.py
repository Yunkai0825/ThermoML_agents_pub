"""query_agent compactor hooks — stage compaction, tool-result subagent,
and hardcoded dict→markdown compactors."""

from .context_stage_compaction import QueryStageCompactor
from .tool_result_compactor import (
    QueryToolResultCompactor,
    ToolResult,
    COMPACTOR_CATALOG,
    COMPACTOR_REGISTRY,
)

__all__ = [
    "QueryStageCompactor",
    "QueryToolResultCompactor",
    "ToolResult",
    "COMPACTOR_CATALOG",
    "COMPACTOR_REGISTRY",
]
