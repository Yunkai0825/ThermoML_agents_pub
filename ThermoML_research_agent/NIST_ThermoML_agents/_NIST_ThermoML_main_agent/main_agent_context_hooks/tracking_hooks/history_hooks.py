"""history_hooks — main agent history recorder."""
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.history_tracking_hooks import HistoryRecorder


class MainHistoryRecorder(HistoryRecorder):
    """Main agent history recorder — uses base implementation."""
    pass


main_history_recorder = MainHistoryRecorder()
