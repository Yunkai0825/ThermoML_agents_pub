"""
Stage compaction — query agent subclass.
=========================================
Inherits ``StageCompactor`` and pins numeric limits to the query
agent's ``AGENT_CONFIG``.

Public API
----------
QueryStageCompactor  — class
"""

from __future__ import annotations

from ...ThermoML_query_argo_config import AGENT_CONFIG as cfg
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.context_cleanup_compactor_hooks import (
    StageCompactor,
)

__all__ = [
    "QueryStageCompactor",
]


class QueryStageCompactor(StageCompactor):
    """Query-agent deterministic compactor — uses query config limits."""

    def __init__(self) -> None:
        super().__init__(
            stage_compact_budget=cfg.STAGE_COMPACT_BUDGET,
            stage_note_chars=cfg.STAGE_NOTE_CHARS,
        )

