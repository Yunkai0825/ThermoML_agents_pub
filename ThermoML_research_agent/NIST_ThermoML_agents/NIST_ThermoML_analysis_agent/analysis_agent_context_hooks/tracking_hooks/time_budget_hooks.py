"""
Time-budget tracker — analysis agent subclass.
================================================
Inherits ``TimeBudgetTracker`` and pre-wires the analysis agent's
config thresholds.
"""

from __future__ import annotations

from ...ThermoML_analysis_argo_config import AGENT_CONFIG as _cfg
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.time_budget_reminder_hooks import TimeBudgetTracker


class AnalysisTimeBudgetTracker(TimeBudgetTracker):
    """Analysis-agent time-budget tracker — uses analysis config thresholds.

    Override thresholds or warning behaviour here to customise for
    the analysis agent.
    """

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
