"""analysis_agent compactor hooks — stage compaction, tool-result subagent,
and hardcoded dict→markdown compactors."""

from .context_stage_compaction import AnalysisStageCompactor
from .tool_result_compactor import (
    AnalysisToolResultCompactor,
    ToolResult,
    COMPACTOR_CATALOG,
    COMPACTOR_REGISTRY,
)

__all__ = [
    "AnalysisStageCompactor",
    "AnalysisToolResultCompactor",
    "ToolResult",
    "COMPACTOR_CATALOG",
    "COMPACTOR_REGISTRY",
]
