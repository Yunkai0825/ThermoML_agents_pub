# general_text_context_marker_catalog — Centralized XML Text Markers

Defines all XML-style context markers used as structural delimiters in
the flat prompt and LLM responses throughout the agent pipeline.

---

## Purpose

Context markers are **text-level** tags (`<tool_call>`, `<reasoning>`,
`<answer>`, etc.) that mark boundaries in the data flowing through the
pipeline.  The ReAct engine and hook modules parse these markers via
compiled regexes to extract tool calls, identify reasoning blocks,
delimit answers, and manage compaction.

> **Not to be confused with anchor points** (`engine_hooks_anchors.py`), which
> are **code-level** dispatch slots in the Python control flow.
> Markers handle data format; anchors handle code behaviour.

---

## Modules

| File | Purpose |
|------|---------|
| `context_markers.py` | `TagPair` and `ContextMarkerCatalog` frozen dataclasses (15 tag families) plus the strict module-level `MARKERS` singleton |
| `__init__.py` | Re-exports all symbols from `context_markers.py` via `from .context_markers import *` |

---

## Data Structures

### `TagPair` (frozen dataclass)

```python
@dataclass(frozen=True)
class TagPair:
    open: str    # e.g. "<tool_call>"
    close: str   # e.g. "</tool_call>"
```

### `ContextMarkerCatalog` (frozen dataclass)

Groups all 15 tag families with their `TagPair` instances and compiled
regexes for extraction.

| Family | Open Tag | Purpose |
|--------|----------|---------|
| `tool_call` | `<tool_call>` | Wraps LLM tool invocations |
| `wait` | `<wait>` | Pause marker between parallel calls |
| `tool_result` | `<tool_result>` | Wraps tool execution results |
| `reasoning` | `<reasoning>` | Extended thinking / chain-of-thought |
| `summary` | `<summary>` | Compacted summaries |
| `compress` | `<compress>` | Agent-initiated compaction request |
| `compaction_guidance` | `<compaction_guidance>` | Mid-turn guidance prompt |
| `compaction_reminder` | `<compaction_reminder>` | Compaction reminder nudge |
| `compact_note` | `<compact_note>` | Compaction metadata note |
| `retry` | `<retry>` | Retry instruction |
| `system_prompt` | `<system_prompt>` | System prompt boundary |
| `answer` | `<answer>` | Final answer boundary |
| `memory` | `<memory>` | Working memory snapshot |
| `validation_guidance` | `<validation_guidance>` | Corrective guidance after a blocked tool call |
| `subagent_answer` | `<subagent_answer>` | Complete agent-generated JSON handed to a parent agent |

### Module-Level Singleton

```python
MARKERS = ContextMarkerCatalog(...)  # canonical instance
```

### Public API

Only `MARKERS`, the catalog dataclasses, `ALL_CONTEXT_MARKERS_RE`,
`strip_reasoning`, `wrap_subagent_answer`, and `mark_subagent_answer_tool` are
exported. Retired flat marker aliases are intentionally
absent; callers must use catalog paths such as `MARKERS.tool_call.open`.

---

## Consumer Pattern

```python
from NIST_ThermoML_agents.general_text_context_marker_catalog import MARKERS

# Use tag pair
prompt += MARKERS.tool_result.open + result_text + MARKERS.tool_result.close

# Use compiled regex
match = MARKERS.tool_call_re.search(response)
```

Agent-delegation tools are explicitly marked with
`@mark_subagent_answer_tool`. The shared tool catalog and both ReAct loops then
wrap the complete successful JSON result exactly once before injecting it into
the parent context. Native dictionaries remain available to tracking hooks, and
marked agent results bypass ordinary content compaction so nested identifiers
are not lost.
