"""Terminal UI for the ThermoML Main Agent."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from ...general_db_query_engine.general_argo_engine_helpers.argo_agent_terminal_ui import ArgoAgentTerminalUI
from ..main_agent_workflows.L0_orchestrator.orchestrator import run as _orchestrator_run


class MainAgentTerminalUI(ArgoAgentTerminalUI):
    """Interactive terminal for the ThermoML Main Agent.

    Supports multi-round continuation: after each round the conversation
    memory, working memory, and session directory are preserved so that
    follow-up questions see the full prior context.
    """

    agent_name = "ThermoML Main Agent"

    def ensure_sys_paths(self) -> None:
        workspace = Path(__file__).resolve().parents[3]
        if str(workspace) not in sys.path:
            sys.path.insert(0, str(workspace))

    def run_agent(self, question: str) -> Any:
        return _orchestrator_run(question, run_verdict=True, **self.build_run_kwargs())

    def display_result(self, result: Any) -> None:
        print("\n" + "=" * 60)
        print(f"ANSWER  (Round {result.round_number})")
        print("=" * 60)
        print(result.answer)
        if result.verdict:
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
        # Only close if the UI loop is about to exit (handled by __del__
        # or the outer loop's exit path).
        pass


def main() -> None:
    MainAgentTerminalUI().main()


if __name__ == "__main__":
    main()
