"""
Shared stage-compaction & context-cleanup helpers.
===================================================
Deterministic (non-LLM) compaction of parallel tool batches, tool-call
and XML shortening.

All functions are **parameterised** — they receive budget / limit values
as arguments (no hard-coded config import).  Each agent provides a thin
wrapper that injects its own ``AGENT_CONFIG`` defaults.

Public API
----------
REASONING_BLOCK_RE           — compiled regex for ``<reasoning>…</reasoning>``
SUMMARY_BLOCK_RE             — compiled regex for ``<summary>…</summary>``
extract_note                 — first-N-chars preview from a tool result
compact_short_args           — one-line pretty-print of tool arguments
compact_tool_calls_for_memory — replace verbose ``<tool_call>`` XML
stage_compact_batch          — markdown table summarising a parallel batch
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ...general_text_context_marker_catalog import MARKERS

TAG_TOOL_CALL_OPEN = MARKERS.tool_call.open
TAG_TOOL_CALL_CLOSE = MARKERS.tool_call.close
TAG_WAIT = MARKERS.wait_tag
REASONING_BLOCK_RE = MARKERS.reasoning_re
SUMMARY_BLOCK_RE = MARKERS.summary_re


# ─── Helpers ─────────────────────────────────────────────────

def extract_note(text: str, max_chars: int = 200) -> str:
    """Extract the first meaningful sentences from a tool result."""
    lines = text.strip().split("\n")
    useful: list[str] = []
    n = 0
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # Skip markdown table separators
        if stripped.startswith("|") and set(stripped.replace("|", "").strip()) <= {"-"}:
            continue
        useful.append(stripped)
        n += len(stripped)
        if n >= max_chars:
            break
    note = " ".join(useful)
    if len(note) > max_chars:
        note = note[:max_chars].rsplit(" ", 1)[0] + "…"
    return note


def compact_short_args(raw_args: dict[str, Any], max_chars: int = 60) -> str:
    """Format tool arguments into a short string for summary tables."""
    priority = [
        "compounds", "doi", "names", "compound", "property_hint",
        "block_number", "properties", "property_type",
    ]
    parts: list[str] = []
    for k in priority:
        if k in raw_args:
            v = str(raw_args[k])
            if len(v) > 30:
                v = v[:27] + "…"
            parts.append(f"{k}={v}")
    for k, v in raw_args.items():
        if k in priority or k in ("purpose", "tasks"):
            continue
        sv = str(v)
        if len(sv) > 20:
            sv = sv[:17] + "…"
        parts.append(f"{k}={sv}")
    result = ", ".join(parts)
    if len(result) > max_chars:
        result = result[: max_chars - 1] + "…"
    return result


def compact_tool_calls_for_memory(
    executed_calls: list[dict],
    deferred_count: int = 0,
) -> str:
    """Build compact text replacing raw ``<tool_call>`` XML in memory.

    After tool calls are parsed and executed, the verbose JSON in
    ``<tool_call>`` blocks is dead weight.  Replace with a brief
    ``name(key_args)`` per call.
    """
    lines: list[str] = []
    for tc in executed_calls:
        name = tc.get("name", "?")
        short_args = compact_short_args(tc.get("arguments", {}), max_chars=80)
        lines.append(f"{TAG_TOOL_CALL_OPEN}{name}({short_args}){TAG_TOOL_CALL_CLOSE}")
    if deferred_count > 0:
        lines.append(f"{TAG_WAIT} ({deferred_count} deferred)")
    return "\n".join(lines)


def stage_compact_batch(
    tool_calls: list[dict],
    tool_results: list[str],
    *,
    note_chars: int = 200,
) -> str:
    """Compact a parallel batch of tool results into a summary table.

    Parameters
    ----------
    tool_calls : list[dict]
        Each dict has ``name`` and ``arguments`` keys.
    tool_results : list[str]
        Corresponding result text for each tool call.
    note_chars : int
        Max chars for the preview note column.

    Returns
    -------
    str  — markdown table summarising the batch.
    """
    n = len(tool_calls)
    lines = [
        f"**Parallel batch: {n} tools executed**\n",
        "| # | Tool | Args | Chars | Note |",
        "|---|------|------|------:|------|",
    ]
    for i, (tc, result_text) in enumerate(zip(tool_calls, tool_results), 1):
        name = tc.get("name", "?")
        args = compact_short_args(tc.get("arguments", {}))
        chars = len(result_text)
        note = extract_note(result_text, max_chars=note_chars)
        lines.append(f"| {i} | {name} | {args} | {chars} | {note} |")
    return "\n".join(lines) + "\n"


# ═══════════════════════════════════════════════════════════════
#  Base dataclass — subclass in each agent's compactor_hooks/
# ═══════════════════════════════════════════════════════════════

@dataclass
class StageCompactor:
    """Deterministic compaction engine — one instance per agent.

    Subclass in ``<agent>_context_hooks/compactor_hooks/`` and
    override numeric fields to tune per agent.
    """

    stage_compact_budget: int = 8_000
    stage_note_chars: int = 200

    def extract_note(self, text: str, max_chars: int | None = None) -> str:
        return extract_note(text, max_chars=max_chars or self.stage_note_chars)

    def compact_short_args(self, raw_args: dict[str, Any], max_chars: int = 60) -> str:
        return compact_short_args(raw_args, max_chars=max_chars)

    def compact_tool_calls_for_memory(
        self, executed_calls: list[dict], deferred_count: int = 0,
    ) -> str:
        return compact_tool_calls_for_memory(executed_calls, deferred_count)

    def stage_compact_batch(
        self, tool_calls: list[dict], tool_results: list[str],
    ) -> str:
        return stage_compact_batch(
            tool_calls, tool_results, note_chars=self.stage_note_chars,
        )

