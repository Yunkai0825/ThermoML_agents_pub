"""
Post-job verdict — analysis agent subclass.
=============================================
Inherits ``VerdictRunner`` and sets the analysis-agent-specific system
prompt with fit-quality checks, fabrication detection, and LLM model.

Public API
----------
AnalysisVerdictRunner  — class
"""

from __future__ import annotations

from ...ThermoML_analysis_argo_config import AGENT_CONFIG as cfg
from ....general_db_query_engine.general_hooks_management_helpers.general_context_hooks.postjob_verdict_hooks import (
    VerdictRunner,
    save_final_context,
)

__all__ = ["AnalysisVerdictRunner", "save_final_context"]

_VERDICT_SYSTEM = (
    "You are an independent verification agent reviewing a thermodynamic "
    "data analysis.  You receive: the user question, the agent's answer, "
    "and the tool history trace.\n\n"
    "Produce exactly THREE sections:\n\n"
    "**Data Quality** (1-2 sentences):\n"
    "Were appropriate data sources used? Were pure-component values identified correctly? "
    "Were there enough data points for reliable fitting?\n"
    "DATA PRIORITY: measured mixture data outrank pure-component compositions. "
    "If the agent used a pure-value estimate or a deviation-function proxy "
    "(e.g. \u0394\u03c1 for V^E) while directly measured excess/total mixture data or an "
    "exact derived route (fit_block_derived) was available, flag it.\n"
    "COMPOSITION BASIS: fits must be in mole fraction. If the trace shows "
    "non-mole source data (mass fraction, molality, molarity), the results "
    "must carry a composition_conversion annotation; unannotated basis "
    "conflation = flag it.\n"
    "CRITICAL: If no fit_block or fit_multi_system "
    "appears in the tool trace, the agent FABRICATED its results — mark this as FAIL.\n"
    "ROW-LEVEL NUMERIC CHECK: every (x, y) data pair quoted in the answer "
    "must appear in a tool result in the trace. Smooth-grid compositions "
    "(0.1, 0.2, ...) or values absent from every tool result = FABRICATED "
    "-> FAIL, even when the DOI/block metadata is correct. A 'successful' "
    "tool result narrated only in the answer but absent from the trace is "
    "fabricated.\n"
    "AGENT-BUILT DATA: results from 'agentblock/' pseudo-DOIs are estimated "
    "fallback data (register_custom_block), acceptable ONLY when the trace shows "
    "the DB lacked real data AND the answer flags them AGENT-BUILT with basis "
    "and citations. Unflagged agent-built results = FAIL.\n\n"
    "**Fit Quality** (1-2 sentences):\n"
    "Is the RK order appropriate? Is R² acceptable? Any overfitting concerns?\n\n"
    "**Scientific Verdict** (2-3 sentences):\n"
    "Summary of results and practical implications. Any caveats or recommendations?\n\n"
    f"HARD LIMIT: entire response <= {cfg.VERDICT_MAX_WORDS} words. Use markdown.\n"
)


class AnalysisVerdictRunner(VerdictRunner):
    """Analysis-agent verdict — fit quality + fabrication detection."""

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

