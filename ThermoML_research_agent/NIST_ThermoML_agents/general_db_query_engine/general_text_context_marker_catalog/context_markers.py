"""
Context marker definitions — single source of truth.
=====================================================
Every XML-style marker tag used in the ThermoML ReAct pipeline is
defined here as a frozen dataclass hierarchy:

- ``TagPair``  — an open/close tag pair
- ``ContextMarkerCatalog`` — groups all tag families, each with its
  tag strings and compiled regexes

The module-level singleton ``MARKERS`` holds the canonical instance.

Categories
----------
ReAct loop tags
    ``tool_call``, ``tool_result``, ``wait``
Reasoning / memory tags
    ``reasoning``, ``summary``
Compaction pipeline tags
    ``compress``, ``compaction_guidance``, ``compaction_reminder``,
    ``compact_note``
Context wrapping tags
    ``system_prompt``, ``answer``, ``memory``
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass


# ═══════════════════════════════════════════════════════════════
#  Dataclass definitions
# ═══════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class TagPair:
    """An XML open/close tag pair."""

    open: str
    close: str


@dataclass(frozen=True)
class ContextMarkerCatalog:
    """Frozen catalog of all XML context markers in the ReAct pipeline.

    Access grouped by family (``MARKERS.tool_call.open``).
    """

    # -- 1. Tool call ---------------------------------------------
    tool_call:         TagPair
    tool_call_re:      re.Pattern[str]   # JSON body
    any_tool_call_re:  re.Pattern[str]   # any body
    tool_call_name_re: re.Pattern[str]   # extract tool name

    # -- 2. Wait --------------------------------------------------
    wait_tag:          str
    wait_re:           re.Pattern[str]

    # -- 3. Tool result -------------------------------------------
    tool_result:       TagPair
    tool_result_re:    re.Pattern[str]

    # -- 4. Reasoning ---------------------------------------------
    reasoning:         TagPair
    reasoning_re:      re.Pattern[str]
    reasoning_strip_re: re.Pattern[str]  # + trailing whitespace

    # -- 5. Summary -----------------------------------------------
    summary:           TagPair
    summary_re:        re.Pattern[str]

    # -- 6. Compress ----------------------------------------------
    compress:          TagPair
    compress_re:       re.Pattern[str]

    # -- 7. Compaction guidance -----------------------------------
    compaction_guidance:    TagPair
    compaction_guidance_re: re.Pattern[str]

    # -- 8. Compaction reminder -----------------------------------
    compaction_reminder:    TagPair

    # -- 9. Compact note ------------------------------------------
    compact_note:      TagPair
    compact_note_re:   re.Pattern[str]

    # -- 10. Retry counter ----------------------------------------
    retry_re:          re.Pattern[str]

    # -- 11. System prompt ----------------------------------------
    system_prompt:     TagPair
    system_prompt_re:  re.Pattern[str]

    # -- 12. Answer -----------------------------------------------
    answer:            TagPair
    answer_re:         re.Pattern[str]

    # -- 13. Memory -----------------------------------------------
    memory:            TagPair
    memory_re:         re.Pattern[str]

    # -- 14. Validation guidance -------------------------------
    validation_guidance:    TagPair
    validation_guidance_re: re.Pattern[str]

    # -- 15. Subagent answer -----------------------------------
    subagent_answer:         TagPair
    subagent_answer_re:      re.Pattern[str]


# ═══════════════════════════════════════════════════════════════
#  Singleton instance
# ═══════════════════════════════════════════════════════════════

MARKERS = ContextMarkerCatalog(
    # 1. Tool call
    tool_call=TagPair("<tool_call>", "</tool_call>"),
    tool_call_re=re.compile(
        r"<tool_call>\s*(\{.*?\})\s*</tool_call>", re.DOTALL,
    ),
    any_tool_call_re=re.compile(
        r"<tool_call>\s*(.*?)\s*</tool_call>", re.DOTALL,
    ),
    tool_call_name_re=re.compile(
        r'<tool_call>\s*\{[^}]*"name"\s*:\s*"([^"]+)"', re.DOTALL,
    ),

    # 2. Wait
    wait_tag="<wait/>",
    wait_re=re.compile(r"<wait\s*/?>", re.IGNORECASE),

    # 3. Tool result
    tool_result=TagPair("<tool_result>", "</tool_result>"),
    tool_result_re=re.compile(
        r"<tool_result>\n(.*?)\n</tool_result>", re.DOTALL,
    ),

    # 4. Reasoning
    reasoning=TagPair("<reasoning>", "</reasoning>"),
    reasoning_re=re.compile(
        r"<reasoning>.*?</reasoning>", re.DOTALL,
    ),
    reasoning_strip_re=re.compile(
        r"<reasoning>.*?</reasoning>\s*", re.DOTALL,
    ),

    # 5. Summary
    summary=TagPair("<summary>", "</summary>"),
    summary_re=re.compile(
        r"<summary>\s*(.*?)\s*</summary>", re.DOTALL,
    ),

    # 6. Compress
    compress=TagPair("<compress>", "</compress>"),
    compress_re=re.compile(
        r"<compress>\s*(.*?)\s*</compress>", re.DOTALL,
    ),

    # 7. Compaction guidance
    compaction_guidance=TagPair("<compaction_guidance>", "</compaction_guidance>"),
    compaction_guidance_re=re.compile(
        r"<compaction_guidance>\s*(.*?)\s*</compaction_guidance>", re.DOTALL,
    ),

    # 8. Compaction reminder
    compaction_reminder=TagPair("<compaction_reminder>", "</compaction_reminder>"),

    # 9. Compact note
    compact_note=TagPair("<compact_note>", "</compact_note>"),
    compact_note_re=re.compile(
        r"<compact_note>.*?</compact_note>", re.DOTALL,
    ),

    # 10. Retry
    retry_re=re.compile(r"^\[RETRY:(\d+)\]\s*"),

    # 11. System prompt
    system_prompt=TagPair("<system_prompt>", "</system_prompt>"),
    system_prompt_re=re.compile(
        r"<system_prompt>.*?</system_prompt>", re.DOTALL,
    ),

    # 12. Answer
    answer=TagPair("<answer>", "</answer>"),
    answer_re=re.compile(
        r"<answer>.*?</answer>", re.DOTALL,
    ),

    # 13. Memory
    memory=TagPair("<memory>", "</memory>"),
    memory_re=re.compile(
        r"<memory>.*?</memory>", re.DOTALL,
    ),

    # 14. Validation guidance
    validation_guidance=TagPair("<validation_guidance>", "</validation_guidance>"),
    validation_guidance_re=re.compile(
        r"<validation_guidance>.*?</validation_guidance>", re.DOTALL,
    ),

    # 15. Subagent answer
    subagent_answer=TagPair("<subagent_answer>", "</subagent_answer>"),
    subagent_answer_re=re.compile(
        r"<subagent_answer>\s*(.*?)\s*</subagent_answer>", re.DOTALL,
    ),
)

# Master regex to strip ALL context markers from final output
ALL_CONTEXT_MARKERS_RE = re.compile(
    r"</?(?:tool_call|tool_result|wait|reasoning|summary|compress"
    r"|compaction_guidance|compaction_reminder|compact_note"
    r"|system_prompt|answer|memory|validation_guidance|subagent_answer)(?:\s*/?)>",
    re.DOTALL,
)


# ═══════════════════════════════════════════════════════════════
#  Convenience helpers
# ═══════════════════════════════════════════════════════════════

def strip_reasoning(text: str) -> str:
    """Remove ``<reasoning>…</reasoning>`` blocks (and trailing whitespace)."""
    return MARKERS.reasoning_strip_re.sub("", text).strip()


def wrap_subagent_answer(value: object) -> str:
    """Wrap one complete agent-generated JSON result exactly once."""
    if isinstance(value, str):
        text = value.strip()
        existing = MARKERS.subagent_answer_re.fullmatch(text)
        payload = existing.group(1).strip() if existing else text
        try:
            parsed = json.loads(payload)
        except json.JSONDecodeError as exc:
            raise ValueError(
                "subagent answer must be a JSON object or array"
            ) from exc
        if not isinstance(parsed, (dict, list)):
            raise TypeError("subagent answer JSON must be an object or array")
        if existing:
            return text
    elif isinstance(value, (dict, list)):
        payload = json.dumps(value, indent=2, ensure_ascii=False)
    else:
        raise TypeError("subagent answer must be JSON text, an object, or an array")
    return (
        f"{MARKERS.subagent_answer.open}\n"
        f"{payload}\n"
        f"{MARKERS.subagent_answer.close}"
    )


def mark_subagent_answer_tool(fn):
    """Mark a tool whose successful result is generated by another agent."""
    if not callable(fn):
        raise TypeError("subagent-answer tool must be callable")
    setattr(fn, "_returns_subagent_answer", True)
    return fn


# ═══════════════════════════════════════════════════════════════
#  Public API
# ═══════════════════════════════════════════════════════════════

__all__ = [
    # Dataclass types & singleton
    "TagPair", "ContextMarkerCatalog", "MARKERS",
    # Master cleanup regex
    "ALL_CONTEXT_MARKERS_RE",
    # Convenience helpers
    "strip_reasoning", "wrap_subagent_answer", "mark_subagent_answer_tool",
]
