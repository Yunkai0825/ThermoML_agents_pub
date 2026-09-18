"""
Shared output-file writers for test runners.
=============================================
All writers expect a **standardised result dict** with these keys:

    prompt_id    : str
    prompt_text  : str
    answer       : str
    iterations   : int
    elapsed_s    : float
    timed_out    : bool
    tool_history : list[dict]
    error        : str | None   (optional)
    verdict      : str | None   (optional)
    working_memory : str         (optional)
    final_context  : str         (optional)
"""
from __future__ import annotations

import datetime as dt
import json
import re
import uuid
from dataclasses import dataclass
from pathlib import Path
from ..general_memory_management_tools_hooks_helpers.session_manager_output_storage import (
    _filesystem_path,
    ensure_directory,
)
from typing import Any, Callable, Optional


# ═══════════════════════════════════════════════════════════════════════════
#  Helpers
# ═══════════════════════════════════════════════════════════════════════════

_JSON_FENCE = chr(96) * 3
_NOT_JSON = object()
_ENVELOPE_PREFIX_RE = re.compile(
    r"^(?:(?:final\s+)?(?:answer|response)(?:\s+json)?\s*:\s*)?"
    r"\{\s*\"(?:answer|summary|core_claims|confidence|status|sources|"
    r"fit_results|follow_up_suggestions|id_catalog_snapshot|"
    r"core_id_updates|core_blocks_found|data_inspections|verdict)\"\s*:",
    re.IGNORECASE | re.DOTALL,
)
_STRUCTURED_ENVELOPE_SECTIONS = {
    "id_catalog_snapshot": (
        "ID Catalog Snapshot (structured ledger)",
        "Workflow-assembled identifier catalog; rendered by the browser.",
    ),
    "core_id_updates": (
        "Core ID Updates (deterministic ledger)",
        "Deterministic identifier updates; rendered by the browser.",
    ),
    "core_blocks_found": (
        "Core Blocks Found (deterministic ledger)",
        "Database-hydrated core block records; rendered by the browser.",
    ),
    "data_inspections": (
        "Data Inspections (deterministic evidence ledger)",
        "Hardcoded envelope merge — not agent-authored; rendered by the browser.",
    ),
}

_STANDARD_ENVELOPE_FIELDS = {
    "answer", "summary", "core_claims", "confidence", "status",
    "sources", "fit_results", "follow_up_suggestions", "output_files",
    "files", "verdict", *_STRUCTURED_ENVELOPE_SECTIONS,
}


@dataclass(frozen=True)
class PreparedAnswer:
    """Human Markdown plus the exact parsed machine envelope, when present."""

    markdown: str
    envelope: dict[str, Any] | None
    envelope_text: str | None


def _decode_json(text: str) -> Any:
    if not isinstance(text, str):
        return _NOT_JSON
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError, ValueError):
        return _NOT_JSON


def _json_candidate(text: str) -> str:
    """Return a bare JSON candidate, unwrapping one complete JSON fence."""
    candidate = str(text).strip()
    if not candidate.startswith(_JSON_FENCE):
        return candidate
    lines = candidate.splitlines()
    if len(lines) < 3 or lines[-1].strip() != _JSON_FENCE:
        return candidate
    if lines[0].strip().casefold() not in {
        _JSON_FENCE, f"{_JSON_FENCE}json",
    }:
        return candidate
    return "\n".join(lines[1:-1]).strip()


def _md_cell(value: Any) -> str:
    """Flatten a value into a readable Markdown-table cell without raw JSON."""
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (str, int, float)):
        text = str(value)
    elif isinstance(value, list):
        text = "; ".join(_md_cell(item) for item in value)
    elif isinstance(value, dict):
        text = "; ".join(
            f"{key}={_md_cell(item)}" for key, item in value.items()
        )
    else:
        text = str(value)
    return text.replace("|", "\\|").replace("\r", " ").replace("\n", "<br>")


def _table_lines(rows: list[dict[str, Any]], columns: list[str]) -> list[str]:
    if not rows:
        return []
    visible = [column for column in columns if any(column in row for row in rows)]
    visible += sorted(
        {key for row in rows for key in row} - set(visible),
        key=str.casefold,
    )
    if not visible:
        return []
    labels = [column.replace("_", " ") for column in visible]
    lines = [
        "| " + " | ".join(labels) + " |",
        "| " + " | ".join("---" for _ in visible) + " |",
    ]
    lines.extend(
        "| " + " | ".join(_md_cell(row.get(column)) for column in visible) + " |"
        for row in rows
    )
    return lines


def _generic_markdown_lines(name: str, value: Any) -> list[str]:
    """Render non-standard envelope fields without exposing JSON syntax."""
    title = name.replace("_", " ").strip().title()
    if isinstance(value, str):
        return [f"### {title}", "", value.strip()]
    if isinstance(value, list):
        dict_rows = [item for item in value if isinstance(item, dict)]
        if dict_rows and len(dict_rows) == len(value):
            return [f"### {title}", "", *_table_lines(dict_rows, [])]
        return [f"### {title}", "",
                *[f"- {_md_cell(item)}" for item in value]]
    if isinstance(value, dict):
        return [f"### {title}", "", *[
            f"- **{key.replace('_', ' ').title()}:** {_md_cell(item)}"
            for key, item in value.items()
        ]]
    return [f"**{title}:** {_md_cell(value)}"]


def render_answer_envelope_markdown(payload: dict[str, Any]) -> str:
    """Render agent-authored and ordinary metadata fields as Markdown.

    Structured ledgers are intentionally omitted here. They stay as JSON in
    result.md and are transformed into tables at the browser boundary.
    """
    raw_answer = payload.get("answer")
    if not isinstance(raw_answer, str):
        # Degraded worker envelopes carry the best available prose here.
        raw_answer = payload.get("raw_answer")
    lines: list[str] = []
    if isinstance(raw_answer, str) and raw_answer.strip():
        lines.append(raw_answer.strip())
    else:
        lines.append("*No agent-authored answer was available.*")

    summary = payload.get("summary")
    if isinstance(summary, str) and summary.strip():
        lines += ["", "### Summary", "", summary.strip()]

    claims = payload.get("core_claims")
    if isinstance(claims, list) and claims:
        lines += ["", "### Core claims", ""]
        lines += [f"- {_md_cell(claim)}" for claim in claims]

    badges = []
    confidence = payload.get("confidence")
    if isinstance(confidence, str) and confidence.strip():
        badges.append(f"**Confidence:** {confidence.strip()}")
    status = payload.get("status")
    if isinstance(status, str) and status.strip():
        badges.append(f"**Status:** {status.strip()}")
    if badges:
        lines += ["", "  |  ".join(badges)]

    sources = payload.get("sources")
    if isinstance(sources, list) and sources:
        rows = [item for item in sources if isinstance(item, dict)]
        if rows:
            lines += ["", "### Sources", "", *_table_lines(
                rows,
                ["lit_num_id", "lit_id", "doi", "block", "block_number",
                 "BLKsubsys_id", "description"],
            )]

    fits = payload.get("fit_results")
    if isinstance(fits, list) and fits:
        rows = [item for item in fits if isinstance(item, dict)]
        if rows:
            lines += ["", "### Fit results", "", *_table_lines(
                rows,
                ["lit_num_id", "block_number", "property", "rk_order",
                 "rk_coeffs", "r_squared", "rmse", "n_points",
                 "temperature_K", "mixing_rule"],
            )]

    followups = payload.get("follow_up_suggestions")
    if isinstance(followups, list) and followups:
        lines += ["", "### Suggested follow-ups", ""]
        lines += [f"- {_md_cell(item)}" for item in followups]

    for key in ("output_files", "files"):
        files = payload.get(key)
        if not isinstance(files, list) or not files:
            continue
        rows = [item for item in files if isinstance(item, dict)]
        if rows:
            lines += ["", "### Output files", "", *_table_lines(
                rows, ["category", "path", "description"],
            )]
        else:
            lines += ["", "### Output files", ""]
            lines += [f"- {_md_cell(item)}" for item in files]

    verdict = payload.get("verdict")
    if isinstance(verdict, str) and verdict.strip():
        lines += ["", "### Verdict", "", verdict.strip()]

    ignored = _STANDARD_ENVELOPE_FIELDS | {"raw_answer"}
    extras = {key: value for key, value in payload.items()
              if key not in ignored}
    if extras:
        lines += [
            "",
            "<details><summary>Other post-answer fields</summary>",
            "",
        ]
        for key, value in extras.items():
            lines += [*_generic_markdown_lines(key, value), ""]
        lines += ["</details>"]
    return "\n".join(lines).strip()


def prepare_answer(answer: str) -> PreparedAnswer:
    """Prepare one answer for human display without mutating its envelope."""
    candidate = _json_candidate(answer)
    decoded = _decode_json(candidate)
    payload = decoded if isinstance(decoded, dict) else None
    if payload is None:
        stripped = str(answer).lstrip()
        if (decoded is not _NOT_JSON
                or _ENVELOPE_PREFIX_RE.match(stripped)
                or stripped.casefold().startswith(f"{_JSON_FENCE}json")
        ):
            return PreparedAnswer(
                markdown=(
                    "*The agent returned an invalid structured final answer. "
                    "The raw response remains available in the run trace for "
                    "diagnostics.*"
                ),
                envelope=None,
                envelope_text=None,
            )
        return PreparedAnswer(markdown=str(answer).strip(), envelope=None,
                              envelope_text=None)
    return PreparedAnswer(
        markdown=render_answer_envelope_markdown(payload),
        envelope=payload,
        # Keep the model-produced JSON byte-for-byte except for surrounding
        # whitespace. The parsed object is used only for the Markdown view.
        envelope_text=candidate,
    )


def answer_envelope_path(result_path: Path) -> Path:
    """Return the non-colliding JSON-sidecar path for a result Markdown file."""
    path = Path(result_path)
    stem = path.stem
    if stem == "result":
        name = "answer_envelope.json"
    elif stem.startswith("result_"):
        name = f"answer_envelope{stem[len('result'):]}.json"
    elif stem.endswith("_result"):
        name = f"{stem[:-len('_result')]}_answer_envelope.json"
    else:
        name = f"{stem}_answer_envelope.json"
    return path.with_name(name)


def structured_envelope_section_lines(
    envelope: dict[str, Any] | None,
) -> list[str]:
    """Persist ledgers as JSON for lossless browser-side rendering."""
    if not envelope:
        return []
    lines: list[str] = []
    for key, (heading, description) in _STRUCTURED_ENVELOPE_SECTIONS.items():
        value = envelope.get(key)
        if value in (None, [], {}):
            continue
        lines += [
            "", "---", "", f"## {heading}", "", description, "",
            f"{_JSON_FENCE}json",
            json.dumps(value, indent=2, ensure_ascii=False),
            _JSON_FENCE,
        ]
    return lines


def prepare_result_answer(path: Path, answer: str) -> tuple[str, list[str]]:
    """Prepare display Markdown and structured sections without writing."""
    prepared = prepare_answer(answer)
    return prepared.markdown, structured_envelope_section_lines(prepared.envelope)


def write_text_atomic(path: Path, text: str) -> None:
    """Atomically replace one UTF-8 text file in its destination directory."""
    path = Path(path)
    ensure_directory(path.parent)
    target = _filesystem_path(path)
    temp = target.with_name(f".{target.name}.{uuid.uuid4().hex}.tmp")
    try:
        temp.write_text(text, encoding="utf-8")
        temp.replace(target)
    finally:
        if temp.exists():
            temp.unlink()


def write_result_bundle(path: Path, result_markdown: str, answer: str) -> None:
    """Atomically write the sidecar first, then result.md, with rollback.

    File replacement is atomic per file. If the result replacement fails after
    the sidecar changes, the prior sidecar is restored (or the new one removed)
    so an old result can never be paired with a new machine envelope.
    """
    path = Path(path)
    sidecar = answer_envelope_path(path)
    sidecar_fs = _filesystem_path(sidecar)
    prepared = prepare_answer(answer)
    prior_exists = sidecar_fs.exists()
    prior_bytes = sidecar_fs.read_bytes() if prior_exists else None
    try:
        if prepared.envelope_text is not None:
            write_text_atomic(sidecar, prepared.envelope_text + "\n")
        elif sidecar_fs.exists():
            sidecar_fs.unlink()
        write_text_atomic(path, result_markdown)
    except Exception:
        try:
            if prior_exists and prior_bytes is not None:
                target = _filesystem_path(sidecar)
                temp = target.with_name(
                    f".{target.name}.{uuid.uuid4().hex}.rollback")
                temp.write_bytes(prior_bytes)
                temp.replace(target)
            elif sidecar_fs.exists():
                sidecar_fs.unlink()
        except Exception:
            pass
        raise

def get_status(result: dict) -> str:
    """Derive ``'OK'``, ``'ERROR'``, or ``'TIMEOUT'`` from a result dict."""
    answer = result.get("answer", "")
    if result.get("error") or "ERROR" in answer:
        return "ERROR"
    if result.get("timed_out"):
        return "TIMEOUT"
    return "OK"


def split_answer_ledger(answer: str) -> tuple[str, list | None]:
    """Split the deterministic evidence ledger out of an envelope answer.

    ``data_inspections`` is a hardcoded post-synthesis merge — never
    agent-authored — so answer-facing surfaces report it separately from
    the answer proper. Non-envelope (prose) answers pass through untouched.
    """
    if not isinstance(answer, str) or '"data_inspections"' not in answer:
        return answer, None
    try:
        payload = json.loads(answer)
    except json.JSONDecodeError:
        return answer, None
    if not isinstance(payload, dict) or "data_inspections" not in payload:
        return answer, None
    ledger = payload.pop("data_inspections")
    if not isinstance(ledger, list):
        return answer, None
    return json.dumps(payload, indent=2, ensure_ascii=False), ledger


def ledger_section_lines(ledger: list | None) -> list[str]:
    """Render the ``## Data Inspections`` section (empty when no ledger)."""
    if not ledger:
        return []
    lines = [
        "",
        "---",
        "",
        "## Data Inspections (deterministic evidence ledger)",
        "",
        f"Hardcoded envelope merge — not agent-authored. {len(ledger)} "
        "entr(ies); verbatim rows below.",
        "",
    ]
    for item in ledger:
        if not isinstance(item, dict):
            continue
        lit = item.get("lit_num_id") or item.get("doi", "?")
        subsys = f" [{item['BLKsubsys_id']}]" if item.get("BLKsubsys_id") else ""
        rows = item.get("rows_shown")
        n_rows = len(rows) if isinstance(rows, list) else "?"
        lines.append(
            f"- {item.get('inspection_id', '?')} — "
            f"{lit}::{item.get('block_number', '?')}{subsys} · "
            f"{item.get('table_mode', '?')} · {n_rows} rows"
        )
    lines += [
        "",
        "```json",
        json.dumps(ledger, indent=2, ensure_ascii=False),
        "```",
    ]
    return lines


# ═══════════════════════════════════════════════════════════════════════════
#  Per-prompt result file
# ═══════════════════════════════════════════════════════════════════════════

def write_result_md(
    path: Path,
    result: dict,
    *,
    clean_fn: Optional[Callable[[str], str]] = None,
    include_verdict: bool = False,
) -> None:
    """Write a single result markdown file at *path*.

    Parameters
    ----------
    clean_fn : callable, optional
        If provided, applied to the raw answer text before writing.
    include_verdict : bool
        Append a ``## Verdict`` section if ``result["verdict"]`` is truthy.
    """
    pid = result["prompt_id"]
    raw_answer = result["answer"]
    # A display cleaner must never turn a valid machine envelope back into
    # visible JSON. Valid envelopes bypass cleaning and render structurally.
    if prepare_answer(raw_answer).envelope is not None:
        answer = raw_answer
    else:
        answer = clean_fn(raw_answer) if clean_fn else raw_answer
    display_answer, structured_sections = prepare_result_answer(path, answer)
    n_tools = len(result.get("tool_history", []))

    lines = [
        f"# Q{pid} — Result",
        "",
        f"**Prompt:** {result['prompt_text']}",
        "",
        f"**Tool calls:** {n_tools}  |  **Time:** {result['elapsed_s']:.1f}s  |  "
        f"**Iterations:** {result['iterations']}  |  **Timed out:** {result.get('timed_out', False)}",
        "",
        "---",
        "",
        "## Answer",
        "",
        display_answer,
    ]
    lines += structured_sections
    if include_verdict and result.get("verdict"):
        lines += ["", "---", "", "## Verdict", "", result["verdict"]]
    lines.append("")
    write_result_bundle(path, "\n".join(lines), answer)


# ═══════════════════════════════════════════════════════════════════════════
#  Per-prompt tool history / trace file
# ═══════════════════════════════════════════════════════════════════════════

def write_history_md(
    path: Path,
    result: dict,
    *,
    rich_mode: bool = False,
    include_working_memory: bool = False,
) -> None:
    """Write a tool trace / history markdown file.

    Parameters
    ----------
    rich_mode : bool
        If *True*, render full argument JSON, full result text, and agent
        reasoning in collapsible ``<details>`` blocks.  If *False*, show a
        compact step list.
    include_working_memory : bool
        Append a final working-memory snapshot section.
    """
    pid = result["prompt_id"]
    n_tools = len(result.get("tool_history", []))

    lines = [
        f"# Q{pid} — Tool {'History' if rich_mode else 'Trace'}",
        "",
        f"**Prompt:** {result['prompt_text']}",
        "",
        f"**Summary:** {result['elapsed_s']:.1f}s  |  "
        f"{result['iterations']} iterations  |  {n_tools} tools",
        "",
        "---",
        "",
    ]

    history = result.get("tool_history", [])
    if not history:
        lines.append("*No tool calls — answered directly.*")
        lines.append("")
    elif rich_mode:
        _write_rich_history(lines, history)
    else:
        _write_compact_history(lines, history)

    # Optional working-memory snapshot
    if include_working_memory:
        wm = result.get("working_memory", "")
        if wm and wm.strip():
            lines += ["---", "", "## Working Memory (final snapshot)", "", wm.strip(), ""]

    lines += [
        "---",
        "",
        f"**Total:** {n_tools} tool calls  |  {result['elapsed_s']:.1f}s  |  "
        f"{get_status(result)}",
        "",
    ]
    ensure_directory(path.parent)
    _filesystem_path(path).write_text("\n".join(lines), encoding="utf-8")


def _write_rich_history(lines: list[str], history: list[dict]) -> None:
    """Append rich tool-history steps with collapsible sections."""
    for h in history:
        it = h.get("iteration", "?")
        tn = h.get("tool", "?")
        rc = h.get("result_chars", 0)
        et = h.get("elapsed_s", 0)
        args = h.get("arguments", {})
        full = h.get("result_full", "")
        reasoning = h.get("reasoning", "")

        lines.append(f"### Step {it}: `{tn}` — {rc:,} chars, {et:.1f}s")
        lines.append("")

        if reasoning:
            lines.append("**Agent reasoning:**")
            lines.append(f"> {reasoning[:2000]}")
            if len(reasoning) > 2000:
                lines.append(f"> ...({len(reasoning)} chars total)")
            lines.append("")

        if args:
            args_json = json.dumps(args, indent=2, default=str, ensure_ascii=False)
            lines += [
                "<details><summary>Arguments</summary>", "",
                "```json", args_json, "```",
                "</details>", "",
            ]

        if full:
            preview = full[:300].replace("\n", " ")
            lines += [
                f"<details><summary>Full result ({rc:,} chars) — {preview}...</summary>", "",
                "```", full, "```",
                "</details>", "",
            ]

        lines += ["---", ""]


def _write_compact_history(lines: list[str], history: list[dict]) -> None:
    """Append compact tool-history steps."""
    for step in history:
        args_str = json.dumps({k: "..." for k in step.get("args_keys", [])})
        lines.append(f"### Step {step.get('iteration', '?')}: `{step.get('tool', '?')}`")
        lines.append(f"- **Args:** `{args_str}`")
        lines.append(f"- **Result size:** {step.get('result_chars', 0):,} chars")
        lines.append(f"- **Elapsed:** {step.get('elapsed_s', '?')}s")
        lines.append("")


# ═══════════════════════════════════════════════════════════════════════════
#  Summary + JSON trace
# ═══════════════════════════════════════════════════════════════════════════

def write_summary_md(
    out_dir: Path,
    results: list[dict],
    wall_time: float,
    workers: int,
    *,
    agent_name: str = "Agent",
    include_file_links: bool = False,
    link_subdir: bool = False,
) -> Path:
    """Write ``TEST_SUMMARY_{ts}.md`` and return its path.

    Parameters
    ----------
    include_file_links : bool
        Add per-prompt link columns to the summary table.
    link_subdir : bool
        If *True*, link to ``Q{id}/result.md`` subdir layout;
        otherwise link to ``Q{id}_result.md`` flat layout.
    """
    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = out_dir / f"TEST_SUMMARY_{ts}.md"

    n_ok = sum(1 for r in results if get_status(r) == "OK")
    n_err = sum(1 for r in results if get_status(r) == "ERROR")
    n_timeout = sum(1 for r in results if get_status(r) == "TIMEOUT")
    total_tools = sum(len(r.get("tool_history", [])) for r in results)
    serial_time = sum(r["elapsed_s"] for r in results)

    mode = "sequential" if workers <= 1 else f"parallel ({workers} workers)"
    lines = [
        f"# {agent_name} Test Summary — {ts}",
        "",
        f"**Mode:** {mode}  |  "
        f"**Total:** {len(results)}  |  **OK:** {n_ok}  |  "
        f"**Error:** {n_err}  |  **Timeout:** {n_timeout}",
        "",
        f"**Wall time:** {wall_time:.0f}s  |  "
        f"**Sum of prompt times:** {serial_time:.0f}s  |  "
        f"**Total tools:** {total_tools}",
    ]
    if workers > 1 and wall_time > 0:
        lines.append(f"**Speedup:** {serial_time / wall_time:.1f}x")

    # ── Table ──
    if include_file_links:
        lines += [
            "",
            "| # | Prompt | Tools | Time | Iters | Status | Result | Trace |",
            "|---|--------|------:|-----:|------:|--------|--------|-------|",
        ]
        for r in results:
            qid = f"Q{r['prompt_id']}"
            prompt_short = r["prompt_text"][:55] + ("..." if len(r["prompt_text"]) > 55 else "")
            status = get_status(r)
            if link_subdir:
                res_link = f"[result]({qid}/result.md)"
                trace_link = f"[trace]({qid}/tool_trace.md)"
            else:
                res_link = f"[result]({qid}_result.md)"
                trace_link = f"[history]({qid}_history.md)"
            lines.append(
                f"| {r['prompt_id']} | {prompt_short} | {len(r.get('tool_history', []))} | "
                f"{r['elapsed_s']:.0f}s | {r['iterations']} | {status} | "
                f"{res_link} | {trace_link} |"
            )
    else:
        lines += [
            "",
            "| # | Prompt | Time | Iters | Tools | Status |",
            "|---|--------|------|-------|-------|--------|",
        ]
        for r in results:
            prompt_short = r["prompt_text"][:60] + ("..." if len(r["prompt_text"]) > 60 else "")
            status = get_status(r)
            lines.append(
                f"| {r['prompt_id']} "
                f"| {prompt_short} "
                f"| {r['elapsed_s']:.0f}s "
                f"| {r['iterations']} "
                f"| {len(r.get('tool_history', []))} "
                f"| {status} |"
            )

    lines.append("")
    lines.append(
        f"**Totals:** {len(results)} prompts  |  "
        f"{total_tools} tool calls  |  {serial_time:.0f}s"
    )
    lines.append("")

    ensure_directory(path.parent)
    _filesystem_path(path).write_text("\n".join(lines), encoding="utf-8")
    return path


def write_json_trace(
    out_dir: Path,
    results: list[dict],
    *,
    exclude_fields: tuple[str, ...] = ("working_memory", "final_context"),
) -> Path:
    """Write ``TEST_TRACE_{ts}.json`` and return its path."""
    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = out_dir / f"TEST_TRACE_{ts}.json"

    trace_data = []
    for r in results:
        jr = {k: v for k, v in r.items() if k not in exclude_fields}
        for field in exclude_fields:
            if field in r:
                val = r.get(field, "") or ""
                jr[f"{field}_chars"] = len(str(val))
        trace_data.append(jr)

    ensure_directory(path.parent)
    _filesystem_path(path).write_text(
        json.dumps(trace_data, indent=2, default=str, ensure_ascii=False),
        encoding="utf-8",
    )
    return path
