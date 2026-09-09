"""
Stats recorder — query agent subclass.
=======================================
Inherits the thread-local, singleton-based ``StatsRecorder`` and
provides a pre-configured module-level instance for the query agent.
"""

from __future__ import annotations

from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.stats_references_tracking_hooks import StatsRecorder


class QueryStatsRecorder(StatsRecorder):
    """Query-agent stats recorder.

    Currently identical to the base class.  Override or extend methods
    here to customise stats rendering for the query agent.
    """


#: Module-level singleton for the query agent.
query_stats_recorder = QueryStatsRecorder()
