"""
Post-job verdict — main agent subclass.
=========================================
Reviews the main agent's orchestration: whether subagents were called
appropriately, whether results were synthesized correctly, and whether
the scientific conclusions follow from the data.
"""
from __future__ import annotations

from ...ThermoML_main_argo_config import AGENT_CONFIG as cfg
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.postjob_verdict_hooks import (
    VerdictRunner,
    save_final_context,
)

__all__ = ["MainVerdictRunner", "save_final_context"]

_VERDICT_SYSTEM = (
    "You are an independent verification agent reviewing a scientific "
    "investigation conducted by a master orchestrator that coordinates "
    "a ThermoML Query Agent (database search) and a ThermoML Analysis "
    "Agent (Redlich-Kister fitting).\n\n"
    "You receive: the user question, the agent's answer, and the tool "
    "history trace.\n\n"
    "Produce exactly THREE sections:\n\n"
    "**Strategy Quality** (1-2 sentences):\n"
    "Did the agent call the right subagents in the right order? "
    "Was parallelism used when appropriate? Were unnecessary calls avoided?\n"
    "CRITICAL: If the agent claims data or fits but no run_query_agent or "
    "run_analysis_agent appears in the trace, mark as FABRICATED → FAIL.\n\n"
    "**Scientific Accuracy** (1-2 sentences):\n"
    "Do the conclusions follow from the subagent results? Were numbers "
    "cited accurately? Any hallucinated data?\n"
    "NUMERIC CROSS-CHECK: verify quoted data values against tool-result "
    "numbers in the trace — ALL rows, not just the first ones. Smooth-grid "
    "compositions (0.1, 0.2, ...), values absent from every subagent "
    "result, or tables whose own min/max/mean contradict tool-returned "
    "aggregates = FABRICATED -> FAIL, even when DOI/block citations are "
    "correct.\n\n"
    "**Overall Verdict** (2-3 sentences):\n"
    "Summary, limitations, and recommendations for follow-up.\n\n"
    f"HARD LIMIT: entire response <= {cfg.VERDICT_MAX_WORDS} words. Use markdown.\n"
)


class MainVerdictRunner(VerdictRunner):
    """Main agent verdict — strategy + scientific accuracy review."""

    def __init__(self) -> None:
        super().__init__(
            system_prompt=_VERDICT_SYSTEM,
            verdict_word_cap=cfg.VERDICT_MAX_WORDS,
            answer_char_limit=cfg.VERDICT_ANSWER_CHARS,
            include_elapsed=False,
            call_kwargs=dict(
                max_tokens=cfg.VERDICT_FORMAT_MAX_TOKENS,
                stop=[],
                model=cfg.VERDICT_MODEL,
            ),
        )

