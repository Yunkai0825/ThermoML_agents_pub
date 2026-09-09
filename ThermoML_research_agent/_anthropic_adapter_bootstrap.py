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

def main() -> int | None:
    if len(sys.argv) < 2 or sys.argv[1] in {"-h", "--help"}:
        print(__doc__)
        return 0 if len(sys.argv) >= 2 else 2
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit("ANTHROPIC_API_KEY not set (bootstrap subprocess environment).")

    # ArgoClient validates this field even when the adapter supplies the HTTP
    # backend. Anthropic ignores it, so no personal Argo account is needed.
    if not os.environ.get("ARGO_API_USER", "").strip():
        os.environ["ARGO_API_USER"] = "anthropic"

    from NIST_ThermoML_agents.general_db_query_engine.general_argo_engine_helpers import (
        anthropic_argo_adapter as adapter,
    )

    original_argv = sys.argv
    module_name = original_argv[1]
    sys.argv = [module_name, *original_argv[2:]]
    adapter.install(capture_path=os.environ.get("ANTHROPIC_ADAPTER_CAPTURE"))
    try:
        mod = importlib.import_module(module_name)
        return mod.main()
    finally:
        adapter.uninstall()
        sys.argv = original_argv


if __name__ == "__main__":
    raise SystemExit(main())
