"""
Post-job verdict — query agent subclass.
=========================================
Inherits ``VerdictRunner`` and sets the query-agent-specific system
prompt, word cap, and default client factory.

Public API
----------
QueryVerdictRunner  — class
"""

from __future__ import annotations

from typing import Any

from ...ThermoML_query_argo_config import AGENT_CONFIG as cfg
from ....general_db_query_engine.general_argo_engine_helpers import ArgoClient
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.postjob_verdict_hooks import (
    VerdictRunner,
    save_final_context,
)

__all__ = ["QueryVerdictRunner", "save_final_context"]

_VERDICT_SYSTEM = f"""\
You are an independent scientific reviewer for thermodynamic database queries.
You receive the user's original question, the agent's final answer, and a
summary of tool calls made during the search.

Your task:
1. **Verdict** (1-2 sentences): Are there gaps in the data or answer?
   Flag missing compounds, properties, or unexpected omissions.
2. **Explanation** (2-3 sentences): Summarise the key scientific findings
   and whether they answer the user's question.
3. **Numeric grounding**: treat specific data values in the answer that are
   not visible in the tool-call summary as UNVERIFIED and say so; flag
   suspicious patterns (smooth composition grids, "representative values",
   per-point rows where tools returned only aggregates) as likely
   fabrication.

HARD LIMIT: ≤{cfg.VERDICT_MAX_WORDS} words total.
Focus on scientific interpretation, NOT workflow critique.
Do not repeat the agent's answer — add value by pointing out what was
missed or what the data limitations are.
"""


class QueryVerdictRunner(VerdictRunner):
    """Query-agent verdict — scientific review of answer quality."""

    def __init__(self) -> None:
        super().__init__(
            system_prompt=_VERDICT_SYSTEM,
            verdict_word_cap=cfg.VERDICT_MAX_WORDS,
            include_elapsed=True,
        )

    def run_verdict(
        self,
        user_question: str,
        final_answer: str,
        tool_history: list[dict[str, Any]],
        *,
        client: ArgoClient | None = None,
    ) -> str:
        if client is None:
            client = ArgoClient.for_verdict()
        return super().run_verdict(
            user_question, final_answer, tool_history, client=client,
        )

