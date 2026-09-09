"""stats_hooks — main agent stats recorder."""
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.stats_references_tracking_hooks import StatsRecorder


class MainStatsRecorder(StatsRecorder):
    """Main agent stats recorder — uses base implementation."""
    pass


main_stats_recorder = MainStatsRecorder()
