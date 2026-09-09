"""reasoning_hooks — main agent reasoning token tracker."""
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.reasoning_token_tracking_hooks import ReasoningTokenTracker


class MainReasoningTracker(ReasoningTokenTracker):
    """Main agent reasoning tracker — uses base implementation."""
    pass


main_reasoning_tracker = MainReasoningTracker()
