"""Writers for the recovered Query benchmark's seven-file artifact contract."""

from __future__ import annotations

import datetime as dt
import json
import sys
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Mapping

try:
    from .paths import find_workspace_root
except ImportError:
    from paths import find_workspace_root


PER_QUESTION_FILES = (
    "result.md",
    "tool_trace.md",
    "run_history.md",
    "working_memory.md",
    "final_full_context.md",
    "reference_stats.md",
    "reasoning_tokens_stripped.md",
)


def fenced(text: str, language: str = "") -> str:
    """Return a Markdown fence longer than any backtick run in *text*."""

    longest = 0
    current = 0
    for char in text:
        if char == chr(96):
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    marker = chr(96) * max(3, longest + 1)
    return f"{marker}{language}\n{text}\n{marker}"


def _status(result: Mapping[str, Any]) -> str:
    if result.get("error"):
        return "ERROR"
    if result.get("timed_out"):
        return "TIMEOUT"
    return "OK"


def _write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


@lru_cache(maxsize=1)
def _result_output_helpers():
    """Load the live result renderer without coupling benchmark import time.

    The recovered harness is intentionally runnable as a standalone package.
    Resolve the live ThermoML source root from this archived file's workspace
    location only when a prompt artifact is actually written.
    """

    source_root = find_workspace_root(__file__) / "ThermoML_research_agent"
    if not source_root.is_dir():
        raise RuntimeError(
            "Cannot locate live ThermoML result renderer relative to archived "
            f"benchmark: {source_root}"
        )
    source_text = str(source_root)
    if source_text not in sys.path:
        sys.path.insert(0, source_text)
    from NIST_ThermoML_agents.general_db_query_engine.general_hooks_management_helpers.general_tracking_hooks_output_helpers.output_writers import (  # noqa: E501
        prepare_result_answer,
        write_result_bundle,
    )

    return prepare_result_answer, write_result_bundle


def _tool_heading(index: int, item: Mapping[str, Any]) -> str:
    name = item.get("tool") or "unknown"
    return f"## Step {index}: {name}"


def write_prompt_artifacts(
    prompt_dir: Path,
    result: Mapping[str, Any],
    *,
    variant_label: str,
    model: str,
    compactor_model: str | None,
) -> None:
    """Write seven baseline files, plus a sidecar for structured answers."""

    prompt_dir.mkdir(parents=True, exist_ok=True)
    prompt_id = str(result["prompt_id"])
    prompt = str(result["prompt_text"])
    answer = str(result.get("answer") or "")
    history = list(result.get("tool_history") or [])

    result_path = prompt_dir / "result.md"
    prepare_result_answer, write_result_bundle = _result_output_helpers()
    answer_for_render = answer or "*No answer returned.*"
    display_answer, structured_sections = prepare_result_answer(
        result_path, answer_for_render
    )
    result_md = (
        f"# Q{prompt_id} — Result\n\n"
        f"**Prompt:** {prompt}\n\n"
        f"- **Status:** {_status(result)}\n"
        f"- **Effort:** {result.get('effort') or 'unspecified'}\n"
        f"- **Tool calls:** {len(history)}\n"
        f"- **API turns:** {result.get('iterations', 0)}\n"
        f"- **Soft-budget threshold:** turn {result.get('soft_budget_turn', 'n/a')}\n"
        f"- **Budget strikes issued:** {len(result.get('budget_events') or [])}\n"
        f"- **Forced final turn:** {bool(result.get('forced_final_turn'))}\n"
        f"- **Fresh final context:** "
        f"{int(result.get('forced_final_context_chars') or 0):,} characters\n"
        f"- **Elapsed:** {float(result.get('elapsed_s') or 0):.1f}s\n"
        f"- **Timed out:** {bool(result.get('timed_out'))}\n\n"
        "## Answer\n\n"
        f"{display_answer}"
    )
    if structured_sections:
        result_md = "\n".join([result_md, *structured_sections])
    # Match the archived _write contract for ordinary prose byte-for-byte while
    # using the production sidecar-first atomic bundle writer for envelopes.
    write_result_bundle(result_path, result_md.rstrip() + "\n", answer_for_render)

    trace_parts = [
        f"# Q{prompt_id} — Tool Trace",
        "",
        f"**Prompt:** {prompt}",
        "",
        "## Summary",
        "",
        f"- Tool calls: {len(history)}",
        f"- API turns: {result.get('iterations', 0)}",
    ]
    if not history:
        trace_parts.extend(["", "No tool calls — answered directly."])
    for index, item in enumerate(history, 1):
        args = item.get("arguments") or {}
        trace_parts.extend(
            [
                "",
                _tool_heading(index, item),
                "",
                f"- Iteration: {item.get('iteration', index)}",
                f"- Purpose: {args.get('purpose', '')}",
                f"- Tasks: {json.dumps(args.get('tasks', []), ensure_ascii=False)}",
                f"- Result characters seen by model: {item.get('result_chars', 0)}",
                f"- Raw result characters: {item.get('raw_result_chars', 0)}",
                f"- Hardcoded-compacted characters: "
                f"{item.get('hardcoded_result_chars', 0)}",
                f"- Agentic verdict: {item.get('agentic_verdict') or 'n/a'}",
                f"- Elapsed: {float(item.get('elapsed_s') or 0):.3f}s",
                f"- Compactor elapsed: {float(item.get('compactor_elapsed_s') or 0):.3f}s",
                f"- Error: {item.get('error') or 'none'}",
                "",
                "### Arguments",
                "",
                fenced(json.dumps(args, ensure_ascii=False, indent=2), "json"),
                "",
                "### Result returned to answering model",
                "",
                str(item.get("result_full") or ""),
            ]
        )
    _write(prompt_dir / "tool_trace.md", "\n".join(trace_parts))

    run_parts = [
        f"# Q{prompt_id} — Run History",
        "",
        f"**Prompt:** {prompt}",
        "",
        "This file is the audit record. For SQL calls, the fenced raw Markdown is",
        "the exact payload supplied to the task-directed agentic compactor.",
        "",
        "## Soft-budget events",
        "",
        fenced(
            json.dumps(result.get("budget_events") or [], ensure_ascii=False, indent=2),
            "json",
        ),
    ]
    for index, item in enumerate(history, 1):
        args = item.get("arguments") or {}
        raw = str(item.get("raw_result_markdown") or "")
        compacted = str(item.get("result_full") or "")
        hardcoded = str(item.get("hardcoded_result_markdown") or "")
        run_parts.extend(
            [
                "",
                _tool_heading(index, item),
                "",
                "### Call arguments",
                "",
                fenced(json.dumps(args, ensure_ascii=False, indent=2), "json"),
                "",
                "### Raw tool result Markdown (exact native serialization)",
                "",
                fenced(raw, "markdown"),
                "",
                "### Existing hardcoded compactor output (agentic input when enabled)",
                "",
                (
                    fenced(hardcoded, "markdown")
                    if hardcoded
                    else "*Not applicable (SQL raw-to-agentic or pass-through tool).*"
                ),
                "",
                "### Model-visible result",
                "",
                fenced(compacted, "markdown"),
                "",
                "### Integrity and timing",
                "",
                f"- Raw SHA-256: {item.get('raw_result_sha256') or 'n/a'}",
                f"- Raw characters: {item.get('raw_result_chars', len(raw))}",
                f"- Hardcoded-compacted characters: "
                f"{item.get('hardcoded_result_chars', len(hardcoded))}",
                f"- Model-visible characters: {item.get('result_chars', len(compacted))}",
                f"- Agentic verdict: {item.get('agentic_verdict') or 'n/a'}",
                f"- Tool elapsed: {float(item.get('tool_elapsed_s') or 0):.3f}s",
                f"- Compactor elapsed: {float(item.get('compactor_elapsed_s') or 0):.3f}s",
                f"- Total elapsed: {float(item.get('elapsed_s') or 0):.3f}s",
            ]
        )
    _write(prompt_dir / "run_history.md", "\n".join(run_parts))

    memory_parts = [
        f"# Q{prompt_id} — Working Memory",
        "",
        "Evidence returned to the answering model:",
    ]
    if not history:
        memory_parts.extend(["", "*No tool evidence.*"])
    for index, item in enumerate(history, 1):
        memory_parts.extend(
            [
                "",
                f"## {index}. {item.get('tool')}",
                "",
                str(item.get("result_full") or ""),
            ]
        )
    _write(prompt_dir / "working_memory.md", "\n".join(memory_parts))

    transcript = str(result.get("final_context") or "")
    context_md = (
        f"# Q{prompt_id} — Final Full Context\n\n"
        "## System prompt\n\n"
        f"{fenced(str(result.get('system_prompt') or ''), 'text')}\n\n"
        "## Conversation transcript\n\n"
        f"{fenced(transcript, 'json')}"
    )
    _write(prompt_dir / "final_full_context.md", context_md)

    main_usage = result.get("main_usage") or {}
    compact_usage = result.get("compactor_usage") or {}
    stats = (
        f"# Q{prompt_id} — Reference Statistics\n\n"
        f"| Variant | Model | Compactor Model | Status | API turns | Tool calls | "
        "Elapsed (s) |\n"
        "|---|---|---|---:|---:|---:|---:|\n"
        f"| {variant_label} | {model} | {compactor_model or 'none'} | "
        f"{_status(result)} | {result.get('iterations', 0)} | {len(history)} | "
        f"{float(result.get('elapsed_s') or 0):.1f} |\n\n"
        "## Token usage\n\n"
        "| Role | Calls | Input tokens | Output tokens | Cache-create | Cache-read |\n"
        "|---|---:|---:|---:|---:|---:|\n"
        f"| Answering agent | {main_usage.get('calls', 0)} | "
        f"{main_usage.get('input_tokens', 0)} | {main_usage.get('output_tokens', 0)} | "
        f"{main_usage.get('cache_creation_input_tokens', 0)} | "
        f"{main_usage.get('cache_read_input_tokens', 0)} |\n"
        f"| Result compactor(s) | {compact_usage.get('calls', 0)} | "
        f"{compact_usage.get('input_tokens', 0)} | "
        f"{compact_usage.get('output_tokens', 0)} | "
        f"{compact_usage.get('cache_creation_input_tokens', 0)} | "
        f"{compact_usage.get('cache_read_input_tokens', 0)} |\n\n"
        "## Turn budget\n\n"
        f"- API effort: {result.get('effort') or 'unspecified'}\n"
        f"- Soft escalation begins: turn {result.get('soft_budget_turn', 'n/a')}\n"
        f"- Configured strikes: {result.get('soft_budget_strikes', 'n/a')}\n"
        f"- Hard final turn: {result.get('hard_turn_limit', 'n/a')}\n"
        f"- Strikes issued: {len(result.get('budget_events') or [])}\n"
        f"- Forced final chance reached: {bool(result.get('forced_final_turn'))}\n"
        f"- Fresh final context characters: "
        f"{int(result.get('forced_final_context_chars') or 0)}\n"
        f"- Fresh final context SHA-256: "
        f"{result.get('forced_final_context_sha256') or 'n/a'}\n"
        f"- Tool request on final chance: {bool(result.get('final_tool_violation'))}"
    )
    _write(prompt_dir / "reference_stats.md", stats)

    reasoning = list(result.get("reasoning_blocks") or [])
    if reasoning:
        reasoning_body = "\n\n".join(
            f"## Block {index}\n\n{block}"
            for index, block in enumerate(reasoning, 1)
        )
    else:
        reasoning_body = (
            "No hidden reasoning was requested or exposed by the API. "
            "This artifact intentionally does not reconstruct private reasoning."
        )
    _write(
        prompt_dir / "reasoning_tokens_stripped.md",
        f"# Q{prompt_id} — Exposed Reasoning Blocks\n\n{reasoning_body}",
    )


def trace_record(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return the browser-compatible trace record without duplicated contexts."""

    record = dict(result)
    working_memory = str(record.pop("working_memory", "") or "")
    final_context = str(record.pop("final_context", "") or "")
    record.pop("system_prompt", None)
    record["working_memory_chars"] = len(working_memory)
    record["final_context_chars"] = len(final_context)
    return record


def write_run_artifacts(
    output_dir: Path,
    results: Iterable[Mapping[str, Any]],
    *,
    timestamp: str,
    variant_label: str,
    model: str,
    wall_elapsed_s: float,
    workers: int,
    prompt_source: Path,
    prompt_sha256: str,
) -> tuple[Path, Path]:
    """Write the paired run-level summary and JSON trace."""

    ordered = sorted(
        (dict(item) for item in results),
        key=lambda item: tuple(int(part) for part in str(item["prompt_id"]).split(".")),
    )
    ok = sum(_status(item) == "OK" for item in ordered)
    errors = sum(_status(item) == "ERROR" for item in ordered)
    timeouts = sum(_status(item) == "TIMEOUT" for item in ordered)
    summary_path = output_dir / f"TEST_SUMMARY_{timestamp}.md"
    trace_path = output_dir / f"TEST_TRACE_{timestamp}.json"

    lines = [
        f"# ThermoML Query Benchmark — {variant_label}",
        "",
        f"- **Timestamp:** {timestamp}",
        f"- **Model:** {model}",
        f"- **Prompts:** {len(ordered)}",
        f"- **Status:** {ok} OK, {errors} errors, {timeouts} timeouts",
        f"- **Workers:** {workers}",
        f"- **Wall time:** {wall_elapsed_s:.1f}s",
        f"- **Prompt source:** {prompt_source}",
        f"- **Prompt SHA-256:** {prompt_sha256}",
        "",
        "| Prompt | Status | Turns | Tools | Elapsed (s) | Result |",
        "|---|---|---:|---:|---:|---|",
    ]
    for item in ordered:
        pid = str(item["prompt_id"])
        lines.append(
            f"| Q{pid} | {_status(item)} | {item.get('iterations', 0)} | "
            f"{len(item.get('tool_history') or [])} | "
            f"{float(item.get('elapsed_s') or 0):.1f} | "
            f"[result](Q{pid}/result.md) |"
        )
    _write(summary_path, "\n".join(lines))
    trace_path.write_text(
        json.dumps([trace_record(item) for item in ordered], ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    return summary_path, trace_path


def append_run_log(path: Path, level: str, message: str) -> None:
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"{now} | {level:<5s} | flat-benchmark | {message}\n")
