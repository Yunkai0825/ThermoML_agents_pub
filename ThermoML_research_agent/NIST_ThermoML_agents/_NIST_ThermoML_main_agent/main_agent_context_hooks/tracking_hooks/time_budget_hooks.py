"""time_budget_hooks — main agent time budget tracker."""
from ...ThermoML_main_argo_config import AGENT_CONFIG as _cfg
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.time_budget_reminder_hooks import TimeBudgetTracker


class MainTimeBudgetTracker(TimeBudgetTracker):
    """Time-budget tracker using main agent config thresholds."""

    def __init__(
        self,
        timeout: float | None = None,
        thresholds: list[float] | None = None,
        max_warnings: int | None = None,
    ) -> None:
        super().__init__(
            timeout=timeout or _cfg.MAX_TURN_SECONDS,
            thresholds=thresholds or _cfg.WARN_THRESHOLDS,
            max_warnings=max_warnings or _cfg.MAX_WRAP_WARNINGS,
        )
