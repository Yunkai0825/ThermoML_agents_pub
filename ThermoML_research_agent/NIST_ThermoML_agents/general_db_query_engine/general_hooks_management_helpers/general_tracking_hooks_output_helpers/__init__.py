"""
Shared output-formatting helpers for test runners.
====================================================
Re-exports the public API from answer_cleaner and output_writers.

Orchestration and prompt-parsing live in
``NIST_ThermoML_agents.general_db_query_engine.general_DEBUG_test_runner_helpers``.
"""

from .answer_cleaner import clean_answer
from .output_writers import (
    answer_envelope_path,
    get_status,
    prepare_answer,
    prepare_result_answer,
    render_answer_envelope_markdown,
    structured_envelope_section_lines,
    write_result_bundle,
    write_result_md,
    write_history_md,
    write_summary_md,
    write_json_trace,
)

__all__ = [
    # answer cleaning
    "clean_answer",
    # output writers
    "answer_envelope_path",
    "get_status",
    "prepare_answer",
    "prepare_result_answer",
    "render_answer_envelope_markdown",
    "structured_envelope_section_lines",
    "write_result_bundle",
    "write_result_md",
    "write_history_md",
    "write_summary_md",
    "write_json_trace",
]
