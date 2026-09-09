"""analysis_agent interactive hooks — LLM-driven compaction + pre-execution guidance."""

from .interactive_compactor import AnalysisInteractiveCompactor
from .fitting_variable_guidance import (
    FittingVariableGuidance,
    fitting_pre_execution_guidance,
)
from .custom_block_guidance import (
    CustomBlockFallbackGuidance,
    custom_block_pre_execution_guidance,
)

__all__ = [
    "AnalysisInteractiveCompactor",
    "FittingVariableGuidance",
    "fitting_pre_execution_guidance",
    "CustomBlockFallbackGuidance",
    "custom_block_pre_execution_guidance",
]
