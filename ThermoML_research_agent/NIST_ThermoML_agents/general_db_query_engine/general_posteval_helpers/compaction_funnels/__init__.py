"""Compaction funnels — post-run workflow figures, tables, and audits.

Self-rooting package: the inner packages (``framework_registry``,
``funnel_evidence``, ``funnel_assembly``, ``run_library``,
``workflow_audits``) import each other by their top-level names, so this
``__init__`` puts the package folder on ``sys.path`` first.  Every module
then has ONE identity no matter the entry point (engine import,
``DEBUG_runner.py``, or a ``DEBUG_scripts`` probe run from this folder).
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_ROOT = str(_Path(__file__).resolve().parent)
if _ROOT not in _sys.path:
    _sys.path.insert(0, _ROOT)

from .api import (  # noqa: E402  (needs the self-rooting above)
    WorkflowReport,
    generate_workflow,
    generate_workflows,
    maybe_generate_workflow,
    session_kind,
)

__all__ = [
    "WorkflowReport",
    "generate_workflow",
    "generate_workflows",
    "maybe_generate_workflow",
    "session_kind",
]
