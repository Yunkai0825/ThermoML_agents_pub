"""
ThermoML Query Agent — Interactive CLI.
=======================================
Customises ``ArgoAgentTerminalUI`` for the query agent.

Launch::

    python -m NIST_ThermoML_agents.NIST_ThermoML_query_agent.query_agent_argo_engine.query_agent_terminal_ui
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[4]

from ...general_db_query_engine.general_argo_engine_helpers.argo_agent_terminal_ui import ArgoAgentTerminalUI
from ...general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers.session_manager_output_storage import (
    ensure_directory,
)
from ..query_agent_workflows.L0_orchestrator.orchestrator import run as _orchestrator_run


class QueryAgentTerminalUI(ArgoAgentTerminalUI):
    """Query-agent specific terminal UI.

    Supports multi-round continuation: after each round the conversation
    context is preserved so that follow-up questions see the full prior
    conversation history.
    """

    agent_name = "ThermoML Query Agent"

    def ensure_sys_paths(self) -> None:
        _THIS_DIR = Path(__file__).absolute().parent
        _AGENT_DIR = _THIS_DIR.parent
        _AGENTS_DIR = _AGENT_DIR.parent
        _WORKSPACE = _AGENTS_DIR.parent
        for p in (_AGENT_DIR, _AGENTS_DIR, _WORKSPACE):
            if str(p) not in sys.path:
                sys.path.insert(0, str(p))

    def run_agent(self, question: str) -> Any:
        kwargs = self.build_run_kwargs()
        if self._round <= 1:
            ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            slug = re.sub(r"[^a-zA-Z0-9]+", "_", question[:40]).strip("_").lower()
            output_root = _REPO_ROOT / "_output" / "Query"
            session_dir = output_root / f"run_{ts}_{slug or 'query'}"
            ensure_directory(session_dir, exist_ok=False)
            self._session_dir = str(session_dir)
            kwargs = {"session_dir": self._session_dir, "round_number": 1}
        return _orchestrator_run(question, **kwargs)

    def display_result(self, result: Any) -> None:
        rnd = self._round
        print("\n" + "=" * 60)
        print(f"ANSWER  (Round {rnd})")
        print("=" * 60)
        print(result.answer)
        iters = getattr(result, "iterations", None)
        elapsed = getattr(result, "elapsed_seconds", None)
        if iters is not None and elapsed is not None:
            print(f"\n[{iters} iterations, {elapsed:.1f}s]")
        if rnd > 1:
            print(f"(continuation round {rnd})")


def main() -> None:
    QueryAgentTerminalUI().main()


if __name__ == "__main__":
    main()
