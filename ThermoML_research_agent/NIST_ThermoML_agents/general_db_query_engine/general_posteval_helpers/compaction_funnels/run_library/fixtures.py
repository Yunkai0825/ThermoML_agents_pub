"""Regression fixture registry — the six new-format sessions.

Four hharb-campaign Main runs (2026-08-15, copied into the Benchmark
storage, workflow/ outputs stripped) + two standalone child roots so
the query/analysis root paths stay exercised.
"""

from __future__ import annotations

from pathlib import Path

_REPO = Path(__file__).resolve().parents[6]
_BASE = _REPO / "_benchmark" / "Main"


# (label, session dir, kind)
FIXTURES: list[tuple[str, Path, str]] = [
    ("hharb_case_i",
     _BASE / "run_20260815_190212_574300_1e8b238b", "main"),
    ("hharb_case_iii",
     _BASE / "run_20260815_192913_176284_e39010e4", "main"),
    ("hharb_case_ii",
     _BASE / "run_20260815_194252_569587_5a4acc5e", "main"),
    ("hharb_case_iv",
     _BASE / "run_20260815_194722_684644_49ae3f02", "main"),
    ("hharb_case_i_qchild",
     _BASE / "run_20260815_190212_574300_1e8b238b" / "query_runs" / "run_1",
     "query"),
    ("hharb_case_iv_achild",
     _BASE / "run_20260815_194722_684644_49ae3f02" / "analysis_runs"
     / "run_1", "analysis"),
]

DEBUG_OUTPUT = _BASE / "Diagnostics" / "compaction_funnels"
