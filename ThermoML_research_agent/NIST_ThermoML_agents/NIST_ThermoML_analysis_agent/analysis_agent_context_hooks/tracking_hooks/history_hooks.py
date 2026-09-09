"""
History recorder — analysis agent subclass.
============================================
Inherits the thread-local, singleton-based ``HistoryRecorder`` and
provides a pre-configured module-level instance for the analysis agent.
"""

from __future__ import annotations

from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.history_tracking_hooks import HistoryRecorder


class AnalysisHistoryRecorder(HistoryRecorder):
    """Analysis-agent history recorder.

    Currently identical to the base class.  Override or extend methods
    here to customise history rendering for the analysis agent (e.g.
    add fit-quality sections to the markdown output).
    """


#: Module-level singleton for the analysis agent.
analysis_history_recorder = AnalysisHistoryRecorder()
