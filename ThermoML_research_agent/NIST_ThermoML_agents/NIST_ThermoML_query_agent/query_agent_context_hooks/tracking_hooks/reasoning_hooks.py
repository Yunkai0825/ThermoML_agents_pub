"""reasoning_hooks — query agent reasoning token tracker."""
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.reasoning_token_tracking_hooks import ReasoningTokenTracker


class QueryReasoningTracker(ReasoningTokenTracker):
    """Query agent reasoning tracker — uses base implementation."""
    pass


query_reasoning_tracker = QueryReasoningTracker()
