"""
ThermoML Query Agent — Public API  (ThermoML_query_api.py)
==========================================================
Single entry-point for consumers of the ThermoML query subagent.

Engine helpers in ``argo_engine_helpers/``:

  - react_helpers.py       — exact argument and result-size validation,
                              AgentTurnResult
  - react_loop.py          — agent_turn()  (sync ReAct loop)
  - react_loop_async.py    — async_agent_turn()
  - argo_client_caller.py  — ArgoClient dataclass

Top-level orchestration in ``L0_orchestrator/orchestrator.py``:

  - ThermoML_query_run()                       — sync full L0 orchestration (ReAct loop)
  - ThermoML_query_hardcoded_L0_wf_run()        — async hardcoded L0 workflow executor (no LLM decisions)
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Dict

if TYPE_CHECKING:
    from ..general_db_query_engine.general_argo_engine_helpers._argo_engine_entry_point import (
        ArgoClient,
        AgentTurnResult,
    )
    from ..general_db_query_engine.general_argo_engine_helpers.async_runner import ToolExecutor

from .query_agent_workflows.L0_orchestrator.orchestrator import (
    run as _orchestrator_run,
    hardcoded_L0_wf_run as _hardcoded_run,
)


def ThermoML_query_run(
    user_question: str,
    memory_path: str | Path | None = None,
    extra_tools: Dict[str, Callable] | None = None,
    client: ArgoClient | None = None,
    session_dir: str | Path | None = None,
    *,
    run_verdict: bool = False,
    round_number: int = 1,
    prev_context: str = "",
) -> AgentTurnResult:
    """Sync full L0 orchestration — delegates to orchestrator.run().

    Parameters
    ----------
    user_question : str
        The user's natural-language query.
    memory_path : str or Path, optional
        Explicit path to the working-memory file. Either this or
        ``session_dir`` must be supplied.
    extra_tools : dict, optional
        Additional tool callables to merge into the registry.
    client : ArgoClient, optional
        LLM caller.  Defaults to ``ArgoClient.for_l0()``.
    session_dir : str or Path, optional
        If provided, write output files (stats, history, reasoning)
        into this directory instead of deriving it from *memory_path*.
        Used when the query agent is invoked as a child of another agent
        that manages its own session.
    run_verdict : bool
        Whether to run the independent verdict agent after the loop
        (skipped on timeout). Stored on ``result.verdict``.
    round_number : int
        1-based round index inside a multi-round conversation.
    prev_context : str
        Cleaned full context from the previous round, pre-seeded into
        memory (see ``strip_context_for_continuation``).

    Returns
    -------
    AgentTurnResult
        Contains answer, verdict, iterations, elapsed time, tool history, etc.
    """
    return _orchestrator_run(
        user_question,
        memory_path=memory_path,
        extra_tools=extra_tools,
        client=client,
        session_dir=session_dir,
        run_verdict=run_verdict,
        round_number=round_number,
        prev_context=prev_context,
    )


async def ThermoML_query_hardcoded_L0_wf_run(
    user_question: str,
    tool_executor: ToolExecutor,
    memory_path: str | Path,
) -> dict[str, Any]:
    """Hardcoded L0 workflow executor (no LLM-driven decisions).

    Executes the L0 workflow phases in fixed order.  Phases that declare
    ``parallel_dispatch`` fan out via ``asyncio.gather()``.  Does NOT
    drive L1 or L2 layers — the caller must wire those into the
    *tool_executor* callback.

    Parameters
    ----------
    user_question : str
        The user's natural-language query.
    tool_executor : async callable
        ``async (tool_name, **kwargs) -> str | dict``.
    memory_path : str or Path
        Explicit path to this run's working-memory file.

    Returns
    -------
    dict with workflow, prompts, phase_results, memory_path.
    """
    return await _hardcoded_run(
        user_question,
        tool_executor=tool_executor,
        memory_path=memory_path,
    )
