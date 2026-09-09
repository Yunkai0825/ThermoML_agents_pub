"""
Stats recorder — analysis agent subclass.
==========================================
Inherits the thread-local, singleton-based ``StatsRecorder`` and
provides a pre-configured module-level instance for the analysis agent.
"""

from __future__ import annotations

from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.stats_references_tracking_hooks import StatsRecorder


class AnalysisStatsRecorder(StatsRecorder):
    """Analysis-agent stats recorder.

    Currently identical to the base class.  Override or extend methods
    here to customise stats rendering for the analysis agent.
    """


#: Module-level singleton for the analysis agent.
analysis_stats_recorder = AnalysisStatsRecorder()
