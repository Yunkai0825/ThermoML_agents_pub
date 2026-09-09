"""
Interactive compactor — query agent subclass.
==============================================
Inherits the shared 3-step LLM compaction cycle and pins it to the
query agent's ``AGENT_CONFIG``.  No tool-protection or domain hint
needed for the query agent.
"""

from __future__ import annotations

from ...ThermoML_query_argo_config import AGENT_CONFIG as _cfg
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.self_compactor_interactive_hooks import (
    InteractiveCompactor,
    # Re-export guidance helpers (config-free, used by react_loop)
    build_compaction_reminder,
    parse_compaction_guidance,
    TOOL_RESULT_TAG_RE,
    COMPRESS_TAG_RE,
)
from ..tracking_hooks.reasoning_hooks import query_reasoning_tracker as _reasoning

__all__ = [
    "QueryInteractiveCompactor",
    "build_compaction_reminder",
    "parse_compaction_guidance",
    "TOOL_RESULT_TAG_RE",
    "COMPRESS_TAG_RE",
]


class QueryInteractiveCompactor(InteractiveCompactor):
    """Query-agent LLM compactor — no protected tools, no domain hint."""

    def __init__(self) -> None:
        super().__init__(cfg=_cfg, reasoning_hook=_reasoning.make_reasoning_hook())
