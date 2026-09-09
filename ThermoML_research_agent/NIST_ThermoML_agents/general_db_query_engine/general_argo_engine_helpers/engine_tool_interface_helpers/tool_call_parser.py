"""
Tool call parsing utilities  (tool_call_parser.py)
====================================================
Parses exact JSON objects inside ``<tool_call>`` blocks.  Called by
``react_loop.agent_turn()`` after each LLM response to extract tool
invocations.  Bare JSON, Python-call syntax, and repaired malformed JSON are
deliberately rejected: the tool interface has one canonical wire format.
"""

from __future__ import annotations

import json
import logging
import math
from dataclasses import dataclass, field
from typing import Optional

from ...general_text_context_marker_catalog import MARKERS

log = logging.getLogger("ThermoML-UI")

# ─── Regex patterns (imported from general_text_context_marker_catalog) ──
_ANY_TOOL_CALL_RE = MARKERS.any_tool_call_re
_WAIT_TAG_RE = MARKERS.wait_re
_TOOL_CALL_OPEN = MARKERS.tool_call.open


# ─── Parsers ─────────────────────────────────────────────────

def _unique_json_object(pairs: list[tuple[str, object]]) -> dict:
    """Build one JSON object while rejecting ambiguous duplicate keys."""
    result: dict = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate object key {key!r}")
        result[key] = value
    return result


def _reject_json_constant(token: str) -> None:
    """Reject JavaScript constants outside the JSON number grammar."""
    raise ValueError(f"non-finite numeric token {token!r}")


def _require_finite_json_numbers(value: object) -> None:
    """Reject numeric overflow such as ``1e400`` after JSON decoding."""
    pending = [value]
    while pending:
        item = pending.pop()
        if isinstance(item, float) and not math.isfinite(item):
            raise ValueError("non-finite numeric value")
        if isinstance(item, dict):
            pending.extend(item.values())
        elif isinstance(item, list):
            pending.extend(item)


def _parse_tool_block(content: str, *, block_index: int) -> tuple[Optional[dict], str]:
    """Parse one exact JSON tool-call object and return an actionable error."""
    content = content.strip()
    try:
        obj = json.loads(
            content,
            object_pairs_hook=_unique_json_object,
            parse_constant=_reject_json_constant,
        )
    except json.JSONDecodeError as exc:
        log.debug("Rejected malformed tool-call JSON %r: %s", content[:120], exc)
        return None, (
            f"block {block_index}: invalid JSON at line {exc.lineno}, "
            f"column {exc.colno}: {exc.msg}"
        )
    except ValueError as exc:
        log.debug("Rejected non-canonical tool-call JSON %r: %s", content[:120], exc)
        return None, f"block {block_index}: invalid JSON: {exc}"
    try:
        _require_finite_json_numbers(obj)
    except ValueError as exc:
        log.debug("Rejected non-finite tool-call JSON %r: %s", content[:120], exc)
        return None, f"block {block_index}: invalid JSON: {exc}"
    if not isinstance(obj, dict):
        return None, f"block {block_index}: the JSON value must be an object"
    keys = set(obj)
    required = {"name", "arguments"}
    if keys != required:
        missing = sorted(required - keys)
        extra = sorted(keys - required)
        return None, (
            f"block {block_index}: tool-call objects require exactly "
            f"['arguments', 'name']; missing={missing}, extra={extra}"
        )
    if not isinstance(obj["name"], str) or not obj["name"].strip():
        return None, f"block {block_index}: 'name' must be a non-empty string"
    if not isinstance(obj["arguments"], dict):
        return None, f"block {block_index}: 'arguments' must be a JSON object"
    return obj, ""


def _try_parse_tool_block(content: str) -> Optional[dict]:
    """Parse one exact JSON tool-call object or return ``None``."""
    parsed, _ = _parse_tool_block(content, block_index=1)
    return parsed


# ─── Data structures ─────────────────────────────────────────

@dataclass
class ToolBatchResult:
    """Result of parsing tool calls from an LLM response."""
    calls: list[dict]
    wait_detected: bool = False
    deferred_count: int = 0  # tool calls after the <wait/> tag
    syntax_errors: list[str] = field(default_factory=list)

    @property
    def syntax_valid(self) -> bool:
        """Whether every pre-wait ``<tool_call>`` block parsed canonically."""
        return not self.syntax_errors

    def correction_message(self) -> str:
        """Return exact ReAct feedback for an atomically rejected batch."""
        details = "\n".join(f"- {error}" for error in self.syntax_errors)
        return (
            "[TOOL SYNTAX CORRECTION] The entire tool batch was rejected "
            "before execution because at least one <tool_call> block was "
            "not canonical. No tool in the batch ran.\n"
            f"{details}\n\n"
            "Re-emit the complete corrected batch. Every call must use exactly:\n"
            '<tool_call>{"name":"registered_tool_name",'
            '"arguments":{"declared_parameter":"JSON value"}}</tool_call>\n'
            "Use valid JSON, exactly the keys 'name' and 'arguments', a "
            "non-empty tool name, and a JSON object for arguments."
        )


# ─── Extractors ──────────────────────────────────────────────

def extract_tool_call(text: str) -> Optional[dict]:
    """Return the first <tool_call> block as a parsed dict, or None."""
    m = _ANY_TOOL_CALL_RE.search(text)
    if m:
        result = _try_parse_tool_block(m.group(1))
        if result:
            return result
    return None


def extract_all_tool_calls(text: str) -> ToolBatchResult:
    """Return <tool_call> blocks as parsed dicts, stopping at ``<wait/>``.

    If the LLM emits a ``<wait/>`` tag between tool_call blocks, only
    the calls *before* the first ``<wait/>`` are returned.  This lets
    the LLM explicitly batch its calls — tools after ``<wait/>`` are
    discarded (the LLM will re-emit them with correct IDs on the next
    iteration after seeing results from the first batch).

    Only the canonical JSON format is accepted inside ``<tool_call>`` tags.
    Returns a ToolBatchResult with the calls, wait flag, and deferred count.
    """
    # Find the <wait/> boundary (if any)
    wait_pos = _WAIT_TAG_RE.search(text)
    search_text = text[:wait_pos.start()] if wait_pos else text

    calls = []
    syntax_errors: list[str] = []
    matches = list(_ANY_TOOL_CALL_RE.finditer(search_text))
    for block_index, m in enumerate(matches, start=1):
        parsed, error = _parse_tool_block(m.group(1), block_index=block_index)
        if parsed:
            calls.append(parsed)
        else:
            syntax_errors.append(error)
    unmatched_count = max(0, search_text.count(_TOOL_CALL_OPEN) - len(matches))
    for offset in range(unmatched_count):
        syntax_errors.append(
            f"block {len(matches) + offset + 1}: unclosed or structurally "
            "invalid <tool_call> block"
        )

    # Count deferred calls (after the <wait/> tag)
    deferred_count = 0
    if wait_pos:
        after_wait = text[wait_pos.end():]
        deferred_count = len(_ANY_TOOL_CALL_RE.findall(after_wait))

    if wait_pos and calls:
        log.info("<wait/> detected — executing %d tools before barrier, "
                 "deferring %d to next iteration", len(calls), deferred_count)
    elif wait_pos and not calls:
        log.warning("<wait/> detected but NO tool calls before it — empty wait")

    return ToolBatchResult(
        calls=calls,
        wait_detected=bool(wait_pos),
        deferred_count=deferred_count,
        syntax_errors=syntax_errors,
    )
