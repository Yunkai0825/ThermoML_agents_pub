"""
Interactive compactor — analysis agent subclass.
=================================================
Inherits the shared 3-step LLM compaction cycle and pins it to the
analysis agent's ``AGENT_CONFIG``.  Fitting-tool results are protected
from compression, and a domain hint for Redlich-Kister models is set.
"""

from __future__ import annotations

from ...ThermoML_analysis_argo_config import AGENT_CONFIG as _cfg
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.self_compactor_interactive_hooks import (
    InteractiveCompactor,
    # Re-export guidance helpers (config-free, used by react_loop)
    build_compaction_reminder,
    parse_compaction_guidance,
    TOOL_RESULT_TAG_RE,
    COMPRESS_TAG_RE,
)
from ..tracking_hooks.reasoning_hooks import analysis_reasoning_tracker as _reasoning

__all__ = [
    "AnalysisInteractiveCompactor",
    "build_compaction_reminder",
    "parse_compaction_guidance",
    "TOOL_RESULT_TAG_RE",
    "COMPRESS_TAG_RE",
]

_DOMAIN_HINT = "that fits Redlich-Kister models to binary mixture data"


class AnalysisInteractiveCompactor(InteractiveCompactor):
    """Analysis-agent LLM compactor — protects fitting tools."""

    def __init__(self) -> None:
        super().__init__(
            cfg=_cfg,
            protect_tools=_cfg.PROTECT_TOOLS,
            domain_hint=_DOMAIN_HINT,
            reasoning_hook=_reasoning.make_reasoning_hook(),
        )
