"""
ThermoML Main Agent — Public API  (ThermoML_main_api.py)
========================================================
Single entry-point for consumers of the ThermoML main orchestrator agent.

Orchestration lives in ``L0_orchestrator/orchestrator.py``:

  - run()            — sync full orchestration (ReAct loop)
  - MainRunResult    — structured result dataclass
  - list_session_files — session catalog tool
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .main_agent_workflows.L0_orchestrator.orchestrator import MainRunResult

from .main_agent_workflows.L0_orchestrator.orchestrator import run as _orchestrator_run


def ThermoML_main_run(
    question: str,
    *,
    run_verdict: bool = True,
    session_dir: str | Path | None = None,
    round_number: int = 1,
    prev_context: str = "",
) -> MainRunResult:
    """Run the main orchestrator agent on a scientific question.

    The main agent delegates work to the query agent (database search)
    and the analysis agent (Redlich-Kister fitting) as needed.

    Parameters
    ----------
    question : str
        The user's natural-language scientific question.
    run_verdict : bool
        Whether to run the independent verdict agent after the main loop.
    session_dir : str or Path, optional
        If provided, reopen (or create) this directory for session output
        instead of auto-generating one under the default OUTPUT_DIR.
        Used when the main agent is invoked from an external harness
        that manages its own session.
    round_number : int
        1-based round index inside a multi-round conversation.
    prev_context : str
        Cleaned full context from the previous round (see
        ``strip_context_for_continuation``), pre-seeded into memory.

    Returns
    -------
    MainRunResult
        Dataclass with fields: answer, verdict, iterations,
        elapsed_seconds, tool_history, timed_out, session_dir,
        output_files.  Supports both attribute and dict-style access.
    """
    return _orchestrator_run(
        question,
        run_verdict=run_verdict,
        session_dir=session_dir,
        round_number=round_number,
        prev_context=prev_context,
    )
