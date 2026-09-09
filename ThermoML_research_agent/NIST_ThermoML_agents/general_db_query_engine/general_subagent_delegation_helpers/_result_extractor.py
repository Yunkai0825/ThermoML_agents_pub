"""
Result extractor for subagent delegation.
==========================================
Extracts a standardised ``dict`` from a ``RunResult``-like object
returned by any agent's public API.
"""
from __future__ import annotations

from typing import Any, Dict
from ThermoML_raw_json_to_card_db_parsers.id_schema import validate_nested_identifiers

from ..general_data_grounding_gate.inspection_harvest import (
    export_inspections,
    harvest_inspections,
)


def extract_run_result(
    result: object,
    agent_type: str,
    question: str,
    session_dir: Any,
    *,
    extra: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    """Extract a flat result dict from a RunResult-like object.

    Parameters
    ----------
    result : object
        The object returned by ``ThermoML_*_run()``.
    agent_type : str
        ``"query"`` or ``"analysis"``.
    question : str
        The original question (stored as ``_question``).
    session_dir : Path | str | None
        The subagent session directory.
    extra : dict, optional
        Additional keys to merge into the result dict (e.g. entity
        summaries, verdict).

    Returns
    -------
    dict
        Standard keys: ``answer``, ``iterations``, ``elapsed_seconds``,
        ``tool_count``, ``timed_out``, ``agent``, ``_question``,
        ``_session_dir``, ``data_inspections`` (the child run's verbatim
        inspection ledger, envelope-ready), plus any agent-specific extras.
    """
    if agent_type not in {"query", "analysis"}:
        raise ValueError(f"agent_type must be query or analysis, got {agent_type!r}")
    required_attributes = (
        "answer", "iterations", "elapsed_seconds", "tool_history", "timed_out"
    )
    missing = [name for name in required_attributes if not hasattr(result, name)]
    if missing:
        raise TypeError(f"subagent result is missing required attributes {missing}")
    tool_history = result.tool_history
    if not isinstance(tool_history, list):
        raise TypeError("subagent result.tool_history must be an array")
    if not isinstance(result.answer, str):
        raise TypeError("subagent result.answer must be a string")
    if isinstance(result.iterations, bool) or not isinstance(result.iterations, int):
        raise TypeError("subagent result.iterations must be an integer")
    if (
        isinstance(result.elapsed_seconds, bool)
        or not isinstance(result.elapsed_seconds, (int, float))
    ):
        raise TypeError("subagent result.elapsed_seconds must be numeric")
    if not isinstance(result.timed_out, bool):
        raise TypeError("subagent result.timed_out must be boolean")
    if not isinstance(question, str) or not question.strip():
        raise TypeError("delegated question must be a non-empty string")
    if session_dir is None:
        raise ValueError("subagent session_dir is required for durable delegation")
    out: Dict[str, Any] = {
        "answer": result.answer,
        "iterations": result.iterations,
        "elapsed_seconds": result.elapsed_seconds,
        "tool_count": len(tool_history),
        "timed_out": result.timed_out,
        "agent": agent_type,
        "_question": question,
        "_session_dir": str(session_dir),
        # Lift the child's verbatim inspection ledger across the delegation
        # boundary as a REAL array (strings nested in the answer JSON are
        # invisible to the parent gate's envelope walker).
        "data_inspections": export_inspections(harvest_inspections(tool_history)),
    }
    if extra is not None:
        overlap = sorted(set(extra) & set(out))
        if overlap:
            raise ValueError(f"extra result fields overlap standard fields: {overlap}")
        out.update(extra)
    validate_nested_identifiers(out, path=f"{agent_type} subagent result")
    write_subagent_result_md(session_dir, out)
    return out


def write_subagent_result_md(session_dir: Any, result: Dict[str, Any]) -> None:
    """Persist the delegated run's answer next to its tracking artifacts.

    Child stats/history/reasoning files are written by the child's own
    recorders; the final ANSWER otherwise only exists inside the parent's
    context, so per-run auditability requires this file.
    """
    from pathlib import Path

    from ..general_hooks_management_helpers.general_memory_management_tools_hooks_helpers.session_manager_output_storage import (
        _filesystem_path,
    )
    from ..general_hooks_management_helpers.general_tracking_hooks_output_helpers.output_writers import (
        ledger_section_lines,
        split_answer_ledger,
    )

    target = Path(session_dir) / "result.md"
    if _filesystem_path(target).exists():
        return  # agents that write their own result file stay authoritative
    display_answer, ledger = split_answer_ledger(str(result.get("answer", "")))
    lines = [
        f"# Delegated {result.get('agent', '?')} run — result",
        "",
        f"**Question:** {result.get('_question', '')}",
        "",
        f"**Iterations:** {result.get('iterations')}  |  "
        f"**Elapsed:** {round(float(result.get('elapsed_seconds', 0.0)), 1)}s  |  "
        f"**Tools:** {result.get('tool_count')}  |  "
        f"**Timed out:** {result.get('timed_out')}",
        "",
        "---",
        "",
        "## Answer",
        "",
        display_answer,
    ]
    lines += ledger_section_lines(ledger)
    lines.append("")
    _filesystem_path(target).write_text("\n".join(lines), encoding="utf-8")
