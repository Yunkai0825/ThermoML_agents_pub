"""
Hardcoded dict → markdown compactors for main agent subagent tools.
===================================================================
Each function takes a raw tool result dict and returns a compact
markdown string suitable for the tool-level subagent.

Each function is tagged with ``@compacts("tool_name")``.
"""
from __future__ import annotations

import logging

from ....general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import compacts
from ThermoML_raw_json_to_card_db_parsers.id_schema import validate_nested_identifiers

log = logging.getLogger("MAIN-compactors")


def _require_result_fields(data: dict, required: set[str], allowed: set[str], context: str) -> None:
    if not isinstance(data, dict):
        raise TypeError(f"{context} must be an object")
    missing = sorted(required - set(data))
    unknown = sorted(set(data) - allowed)
    if missing or unknown:
        raise ValueError(f"{context} has missing={missing} and unknown={unknown} fields")
    validate_nested_identifiers(data, path=context)


def _require_standard_result_types(data: dict, context: str) -> None:
    if not isinstance(data["answer"], str):
        raise TypeError(f"{context}.answer must be a string")
    for field in ("iterations", "tool_count"):
        if isinstance(data[field], bool) or not isinstance(data[field], int) or data[field] < 0:
            raise TypeError(f"{context}.{field} must be a non-negative integer")
    if (
        isinstance(data["elapsed_seconds"], bool)
        or not isinstance(data["elapsed_seconds"], (int, float))
        or data["elapsed_seconds"] < 0
    ):
        raise TypeError(f"{context}.elapsed_seconds must be a non-negative number")
    if not isinstance(data["timed_out"], bool):
        raise TypeError(f"{context}.timed_out must be boolean")
    for field in ("agent", "_question", "_session_dir"):
        if not isinstance(data[field], str) or not data[field].strip():
            raise TypeError(f"{context}.{field} must be a non-empty string")


def _require_data_inspections(data: dict, context: str) -> None:
    inspections = data["data_inspections"]
    if not isinstance(inspections, list):
        raise TypeError(f"{context}.data_inspections must be an array")
    for index, item in enumerate(inspections):
        if not isinstance(item, dict) or "inspection_id" not in item:
            raise ValueError(
                f"{context}.data_inspections[{index}] is not an inspection entry"
            )


@compacts("run_query_agent")
def compact_query_result(data: dict) -> str:
    """Compact a query agent result into key facts."""
    standard = {
        "answer", "iterations", "elapsed_seconds", "tool_count", "timed_out",
        "agent", "_question", "_session_dir", "verdict", "data_inspections",
    }
    # Exactly the keys _extract_query_entity_summary can emit.
    optional_counts = {
        "n_compounds", "n_properties", "n_dois", "n_blocks",
        "n_subsystems", "n_matching_datapoints",
    }
    _require_result_fields(data, standard, standard | optional_counts, "query agent result")
    _require_standard_result_types(data, "query agent result")
    for field in optional_counts & set(data):
        if isinstance(data[field], bool) or not isinstance(data[field], int) or data[field] < 0:
            raise TypeError(f"query agent result.{field} must be a non-negative integer")
    if data["agent"] != "query":
        raise ValueError("query agent result has the wrong agent discriminator")
    verdict = data["verdict"]
    if verdict is not None and not isinstance(verdict, str):
        raise TypeError("query agent result.verdict must be a string or null")
    _require_data_inspections(data, "query agent result")
    answer = data["answer"]
    iters = data["iterations"]
    elapsed = data["elapsed_seconds"]
    tool_count = data["tool_count"]
    timed_out = data["timed_out"]
    elapsed_str = f"{elapsed:.1f}s"

    lines = [
        f"**Query Agent** ({iters} iters, {elapsed_str}, {tool_count} tools"
        + (", TIMED OUT" if timed_out else "") + ")",
        "",
    ]

    lines.append(answer)

    if verdict:
        lines += ["", "### Verdict", verdict]

    n_insp = len(data["data_inspections"])
    lines += ["", f"**Data inspections carried:** {n_insp} verbatim table(s) "
              "(grounding evidence for quoted values)"]

    return "\n".join(lines)


@compacts("run_analysis_agent")
def compact_analysis_result(data: dict) -> str:
    """Compact an analysis agent result into key facts."""
    required = {
        "answer", "iterations", "elapsed_seconds", "tool_count", "timed_out",
        "agent", "_question", "_session_dir", "verdict", "session_dir", "output_files",
        "data_inspections",
    }
    _require_result_fields(data, required, required, "analysis agent result")
    _require_standard_result_types(data, "analysis agent result")
    if data["agent"] != "analysis":
        raise ValueError("analysis agent result has the wrong agent discriminator")
    _require_data_inspections(data, "analysis agent result")
    answer = data["answer"]
    verdict = data["verdict"]
    iters = data["iterations"]
    elapsed = data["elapsed_seconds"]
    tool_count = data["tool_count"]
    timed_out = data["timed_out"]
    session_dir = data["session_dir"]
    output_files = data["output_files"]
    if verdict is not None and not isinstance(verdict, str):
        raise TypeError("analysis agent result.verdict must be a string or null")
    if session_dir != data["_session_dir"]:
        raise ValueError("analysis agent result session_dir fields disagree")
    if not isinstance(output_files, list):
        raise TypeError("analysis agent result.output_files must be an array")
    for index, output_file in enumerate(output_files):
        if not isinstance(output_file, dict) or set(output_file) != {
            "category", "path", "description"
        }:
            raise ValueError(
                f"analysis agent result.output_files[{index}] has an invalid schema"
            )
        if any(not isinstance(output_file[field], str) for field in output_file):
            raise TypeError(
                f"analysis agent result.output_files[{index}] fields must be strings"
            )
    elapsed_str = f"{elapsed:.1f}s"

    lines = [
        f"**Analysis Agent** ({iters} iters, {elapsed_str}, {tool_count} tools"
        + (", TIMED OUT" if timed_out else "") + ")",
        "",
    ]

    lines.append(answer)

    if verdict:
        lines += ["", "### Verdict", verdict]

    n_insp = len(data["data_inspections"])
    lines += ["", f"**Data inspections carried:** {n_insp} verbatim table(s) "
              "(grounding evidence for quoted values)"]

    if output_files:
        lines += ["", f"**Output files:** {len(output_files)} files"]
        for output_file in output_files:
            desc = output_file["description"]
            lines.append(f"- `{output_file['path']}` {desc}")

    if session_dir:
        lines.append(f"\n**Session:** `{session_dir}`")

    return "\n".join(lines)


# ── All compactor functions for catalog construction ────────────
COMPACTOR_FUNCTIONS = [
    compact_query_result,
    compact_analysis_result,
]
