"""
Stage compaction — main agent subclass.
========================================
Inherits ``StageCompactor`` and pins numeric limits to the main
agent's ``AGENT_CONFIG``.
"""
from __future__ import annotations

from ...ThermoML_main_argo_config import AGENT_CONFIG as cfg
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.context_cleanup_compactor_hooks import (
    StageCompactor,
)

__all__ = [
    "MainStageCompactor",
]


class MainStageCompactor(StageCompactor):
    """Main-agent deterministic compactor — uses main agent config limits."""

    def __init__(self) -> None:
        super().__init__(
            stage_compact_budget=cfg.STAGE_COMPACT_BUDGET,
            stage_note_chars=cfg.STAGE_NOTE_CHARS,
        )
