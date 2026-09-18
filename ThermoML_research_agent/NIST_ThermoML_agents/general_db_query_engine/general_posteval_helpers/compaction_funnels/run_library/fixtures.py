"""Regression fixture registry — the six new-format sessions.

Four Main benchmark examples from 2026-08-15, named by prompt ID and
second-resolution timestamp, plus two standalone child roots so
the query/analysis root paths stay exercised.
"""

from __future__ import annotations

from pathlib import Path

_REPO = Path(__file__).resolve().parents[6]
_BASE = _REPO / "_benchmark" / "Main"

# (label, session dir, kind)
FIXTURES: list[tuple[str, Path, str]] = [
    ("hharb_case_i",
     _BASE / "Q1.1.1_run_20260815_190212", "main"),
    ("hharb_case_iii",
     _BASE / "Q1.2.3_run_20260815_192913", "main"),
    ("hharb_case_ii",
     _BASE / "Q1.1.3_run_20260815_194252", "main"),
    ("hharb_case_iv",
     _BASE / "Q1.2.4_run_20260815_194722", "main"),
    ("hharb_case_i_qchild",
     _BASE / "Q1.1.1_run_20260815_190212" / "query_runs" / "run_1",
     "query"),
    ("hharb_case_iv_achild",
     _BASE / "Q1.2.4_run_20260815_194722" / "analysis_runs"
     / "run_1", "analysis"),
]

DEBUG_OUTPUT = Path(__file__).resolve().parents[1] / "DEBUG_output"
