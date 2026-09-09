# general_hooks_management_helpers — Shared Hook Infrastructure

Parent package for cross-agent hook modules: context hooks, memory
management, output/tracking helpers, and tool-result instrumentation.
All child packages live **under this directory** and are imported via
fully-qualified paths:

```python
from ..general_hooks_management_helpers.general_context_hooks.time_budget_reminder_hooks import ...
from ..general_hooks_management_helpers.general_memory_management_tools_hooks_helpers import ...
```

---

## Child Packages

| Package | Purpose |
|---------|---------|
| `general_context_hooks/` | Runtime hooks — time-budget, compaction, history/stats recorders (with internal error logging), reasoning capture, anchor catalog |
| `general_memory_management_tools_hooks_helpers/` | File-backed working memory (8 MCP tool wrappers), `BaseWorkingMemory`, `SessionManager`, memory anchor catalog, **`memory_tool_result_instrumentation_helper.py`** (shared tool-result wrapper) |
| `general_tracking_hooks_output_helpers/` | Output-file writers (`write_result_md`, `write_summary_md`, `write_json_trace`) and `clean_answer()` |
| `general_postans_eval_hooks/` | Shared answer-only → parallel claim and ID/metadata agents → optional hidden deterministic ID tools → downstream-JSON assembly lifecycle |

---

## Shared Tool-Result Instrumentation

`general_memory_management_tools_hooks_helpers/memory_tool_result_instrumentation_helper.py`
provides `make_instrumented_wrapper()` — a factory that wraps any tool
callable so that:

1. The result is stored in working memory via `record_tool_result()`.
2. String results are JSON-parsed when possible so that structured data
   (`core_id_updates`, `core_blocks_found`, compound details, etc.) feeds into the
   stats recorder.
3. The `AGENT_RECORD_REFERENCES` anchor is **NOT** fired here — it is
   fired exclusively from `react_loop.py` to prevent double-counting.

Used by both the **Analysis Agent** and **Main Agent** orchestrators.

---

## Anchor Point Integration

Three shared anchor-point catalogs live under this directory:

| Catalog | Location | Types |
|---------|----------|-------|
| Context anchors (31 types) | `general_context_hooks/_context_hooks_anchors_catalog.py` | PROMPT (8), ANSWER (8), TIME_BUDGET (5), COMPACTION (10) |
| Memory anchors (10 types) | `general_memory_management_tools_hooks_helpers/_memory_hooks_anchors_catalog.py` | WORKING_MEMORY (3), MEMORY_APPEND (7) |
| Post-answer anchors (15 types) | `general_postans_eval_hooks/_postans_eval_anchors_catalog.py` | answer received; shared parallel-agent dispatch/evaluation after; summary tool before/after; L2 field tool before/after/refinement; core-ID tools before/after/refinement; submission review; assembly before/after; validation failure |

The tool-anchor catalog lives in `general_tool_management_helpers/`.
