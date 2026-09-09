"""
ThermoML Analysis Agent — Interactive CLI.
==========================================
Customises ``ArgoAgentTerminalUI`` for the analysis agent.

Launch::

    python -m NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.analysis_agent_argo_engine.analysis_agent_terminal_ui
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from ...general_db_query_engine.general_argo_engine_helpers.argo_agent_terminal_ui import ArgoAgentTerminalUI
from ..analysis_agent_workflows.L0_orchestrator.orchestrator import run as _orchestrator_run


class AnalysisAgentTerminalUI(ArgoAgentTerminalUI):
    """Analysis-agent specific terminal UI.

    Supports multi-round continuation: after each round the conversation
    memory, working memory, and session directory are preserved so that
    follow-up questions see the full prior context.
    """

    agent_name = "ThermoML Analysis Agent"

    def ensure_sys_paths(self) -> None:
        _THIS_DIR = Path(__file__).absolute().parent
        _AGENT_DIR = _THIS_DIR.parent
        _AGENTS_DIR = _AGENT_DIR.parent
        _WORKSPACE = _AGENTS_DIR.parent
        for p in (_AGENT_DIR, _AGENTS_DIR, _WORKSPACE):
            if str(p) not in sys.path:
                sys.path.insert(0, str(p))

    def run_agent(self, question: str) -> Any:
        return _orchestrator_run(question, run_verdict=True, **self.build_run_kwargs())

    def display_result(self, result: Any) -> None:
        print("\n" + "=" * 60)
        print(f"ANSWER  (Round {result.round_number})")
        print("=" * 60)
        print(result.answer)
        if getattr(result, "verdict", None):
            print("\n" + "-" * 60)
            print("VERDICT")
            print("-" * 60)
            print(result.verdict)
        print(f"\n[{result.iterations} iterations, {result.elapsed_seconds:.1f}s]")
        if result.session_dir:
            print(f"Session: {result.session_dir}")
        if result.round_number > 1:
            print(f"(continuation round {result.round_number})")

    def on_after_run(self, question: str, result: Any) -> None:
        # Do NOT close session on continuation rounds — keep it alive.
        pass


def main() -> None:
    AnalysisAgentTerminalUI().main()


if __name__ == "__main__":
    main()
