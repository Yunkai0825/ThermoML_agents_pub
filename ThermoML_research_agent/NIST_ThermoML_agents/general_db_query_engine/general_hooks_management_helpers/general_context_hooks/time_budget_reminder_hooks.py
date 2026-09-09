"""
Time-budget reminder hook for the ReAct loop.
==============================================
Tracks elapsed wall-clock time against configurable thresholds and
injects progressive "[TIME WARNING …]" messages into the conversation
memory so the LLM learns to wrap up before the hard limit.

Usage::

    from ...general_context_hooks.time_budget_reminder_hooks import TimeBudgetTracker

    tracker = TimeBudgetTracker(timeout=1000,
                                thresholds=[0.65, 0.85, 0.95],
                                max_warnings=3)

    # Inside each iteration:
    tracker.check_and_inject_warnings(elapsed, memory)

    if tracker.is_hard_stop(elapsed):
        break

    # After tool calls:
    if tracker.all_warnings_fired:
        memory.append({"role": "user",
                       "content": tracker.make_final_warning_message()})
        # … force one last LLM call …
"""

from __future__ import annotations

import logging
from typing import List

log = logging.getLogger("time-budget")

HARD_STOP_MULTIPLIER = 1.1  # break at 110 % of budget


class TimeBudgetTracker:
    """Stateful tracker for time-budget warnings within one agent turn."""

    def __init__(
        self,
        timeout: float,
        thresholds: list[float],
        max_warnings: int,
    ) -> None:
        self._timeout = timeout
        self._thresholds = thresholds
        self._max_warnings = max_warnings
        self._warnings_fired = 0

    # ── read-only state ──────────────────────────────────────

    @property
    def warnings_fired(self) -> int:
        return self._warnings_fired

    @property
    def all_warnings_fired(self) -> bool:
        return self._warnings_fired >= self._max_warnings

    # ── core behaviour ───────────────────────────────────────

    def check_and_inject_warnings(
        self,
        elapsed: float,
        memory: List[dict],
    ) -> int:
        """Append any newly-exceeded time-warning messages to *memory*.

        Uses a while-loop so that if a single long tool call spans
        multiple thresholds (e.g. 0 %→90 %), ALL exceeded warnings
        fire in the same iteration rather than one-per-turn.

        Returns the number of new warnings injected.
        """
        count = 0
        while self._warnings_fired < self._max_warnings:
            threshold = self._thresholds[self._warnings_fired]
            if elapsed > self._timeout * threshold:
                pct = int(threshold * 100)
                warning = (
                    f"[TIME WARNING {self._warnings_fired + 1}/"
                    f"{self._max_warnings}] "
                    f"{pct}% of time budget used "
                    f"({elapsed:.0f}s / {self._timeout}s). "
                    f"Wrap up soon — provide your best answer "
                    f"with available data."
                )
                memory.append({"role": "user", "content": warning})
                self._warnings_fired += 1
                count += 1
                log.warning(warning)
            else:
                break
        return count

    def is_hard_stop(self, elapsed: float) -> bool:
        """Return *True* when the elapsed time exceeds the hard limit."""
        return elapsed > self._timeout * HARD_STOP_MULTIPLIER

    @staticmethod
    def make_final_warning_message() -> str:
        """Return the message injected when forcing a final answer."""
        return (
            "[FINAL WARNING] Time budget exhausted. "
            "You MUST provide your final answer NOW. No more tool calls."
        )
