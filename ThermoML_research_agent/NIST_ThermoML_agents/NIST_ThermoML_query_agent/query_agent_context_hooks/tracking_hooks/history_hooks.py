"""
History recorder — query agent subclass.
=========================================
Inherits the thread-local, singleton-based ``HistoryRecorder`` and
provides a pre-configured module-level instance for the query agent.
"""

from __future__ import annotations

from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.history_tracking_hooks import HistoryRecorder


class QueryHistoryRecorder(HistoryRecorder):
    """Query-agent history recorder.

    Currently identical to the base class.  Override or extend methods
    here to customise history rendering for the query agent (e.g. add
    query-specific sections to the markdown output).
    """


#: Module-level singleton for the query agent.
query_history_recorder = QueryHistoryRecorder()
