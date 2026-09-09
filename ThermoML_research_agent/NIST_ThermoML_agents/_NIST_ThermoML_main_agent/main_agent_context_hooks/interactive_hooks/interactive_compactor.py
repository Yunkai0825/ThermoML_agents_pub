"""
Interactive compactor — main agent subclass.
=============================================
Inherits the shared 3-step LLM compaction cycle and pins it to the
main agent's ``AGENT_CONFIG``.  No tools are protected from compression
since the main agent only receives subagent result summaries.
"""
from __future__ import annotations

from ...ThermoML_main_argo_config import AGENT_CONFIG as _cfg
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.self_compactor_interactive_hooks import (
    InteractiveCompactor,
    build_compaction_reminder,
    parse_compaction_guidance,
    TOOL_RESULT_TAG_RE,
    COMPRESS_TAG_RE,
)
from ..tracking_hooks.reasoning_hooks import main_reasoning_tracker as _reasoning

__all__ = [
    "MainInteractiveCompactor",
    "build_compaction_reminder",
    "parse_compaction_guidance",
    "TOOL_RESULT_TAG_RE",
    "COMPRESS_TAG_RE",
]

_DOMAIN_HINT = "that orchestrates thermodynamic data queries and Redlich-Kister fitting analyses"


class MainInteractiveCompactor(InteractiveCompactor):
    """Main-agent LLM compactor — no protected tools."""

    def __init__(self) -> None:
        super().__init__(
            cfg=_cfg,
            protect_tools=_cfg.PROTECT_TOOLS,  # empty set
            domain_hint=_DOMAIN_HINT,
            reasoning_hook=_reasoning.make_reasoning_hook(),
        )
