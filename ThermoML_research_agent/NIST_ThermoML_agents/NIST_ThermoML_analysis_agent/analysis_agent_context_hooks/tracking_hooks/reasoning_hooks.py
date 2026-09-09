"""reasoning_hooks — analysis agent reasoning token tracker."""
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.reasoning_token_tracking_hooks import ReasoningTokenTracker


class AnalysisReasoningTracker(ReasoningTokenTracker):
    """Analysis agent reasoning tracker — uses base implementation."""
    pass


analysis_reasoning_tracker = AnalysisReasoningTracker()
