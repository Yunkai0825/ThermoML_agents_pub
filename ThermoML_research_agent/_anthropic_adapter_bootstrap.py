#!/usr/bin/env python
"""Subprocess entry point for run_debug_benchmark.py's --anthropic mode.

Installs the Anthropic backend adapter, then runs the given ``run_tests``
module's ``main()`` with the remaining CLI args forwarded UNCHANGED — so
each agent subprocess is routed through the Anthropic Messages API instead
of Argo, with zero changes to any run_tests.py / agent framework file.

    python _anthropic_adapter_bootstrap.py <run_tests_module> [run_tests args...]

Reads ANTHROPIC_API_KEY (required) and ANTHROPIC_ADAPTER_CAPTURE (optional,
a .jsonl path for the passive raw-response capture) from the environment.
"""
from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent   # ThermoML_research_agent
REPO_ROOT = WORKSPACE_ROOT.parent
for _p in (str(REPO_ROOT), str(WORKSPACE_ROOT)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

def main(argv: list[str] | None = None) -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("module", help="Per-agent benchmark run_tests module")
    parser.add_argument("runner_args", nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        parser.error("ANTHROPIC_API_KEY is required for the Anthropic benchmark backend")
    # The Argo-shaped engine requires an account label even when its HTTP calls
    # are handled by the Anthropic adapter. No personal account is assumed.
    if not os.environ.get("ARGO_API_USER", "").strip():
        os.environ["ARGO_API_USER"] = "anthropic"
    from NIST_ThermoML_agents.general_db_query_engine.general_argo_engine_helpers import (
        anthropic_argo_adapter as adapter,
    )

    original_argv = sys.argv
    adapter.install(capture_path=os.environ.get("ANTHROPIC_ADAPTER_CAPTURE"))
    try:
        sys.argv = [args.module, *args.runner_args]
        importlib.import_module(args.module).main()
    finally:
        sys.argv = original_argv
        adapter.uninstall()


if __name__ == "__main__":
    main()
