# Query Agent — Hook Customization Catalog

> Deviations from `general_hooks_management_helpers/` defaults.
> Version 6.0 — 2026-04-07

---

## 1. Anchor Wiring — `build_engine_hooks()`

The query agent's `hook_catalog.py` subclasses `AgentHookCollection` and
wires 9 anchor types from the per-domain catalogs:

| Anchor Type | Callback | Singleton |
|-------------|----------|-----------|
| `on_reasoning` | `log_reasoning_from_response` | `query_reasoning_tracker` |
| `sync_tool_result_recorded` | `log_tool_result` | `query_stats_recorder` |
| `sync_tool_call_recorded` | `log_tool_call` | `query_history_recorder` |
| `sync_tool_error_recorded` | `log_error` | `query_history_recorder` |
| `sync_tool_purpose_error_recorded` | `log_purpose_tasks_error` | `query_history_recorder` |
| `sync_stage_compaction_build` | `log_stage_compaction` | `query_history_recorder` |
| `sync_compaction_execute` | `log_compaction` | `query_history_recorder` |
| `sync_compaction_stats_recorded` | `log_compaction` | `query_stats_recorder` |
| `sync_tool_guidance_check` | `validate_block_search_adv_guidance` | advanced-search preexecution validation |

The 5 agent-level lifecycle anchors (`AGENT_START_TRACKING`, etc.) are
wired via `build_agent_lifecycle_bindings()` in `engine_hooks_anchors.py`.

---

## 2. Stage Compactor → `QueryStageCompactor`

| Parameter | General Default (`StageCompactor`) | Query Agent | Why |
|-----------|-----------------------------------|-------------|-----|
| `stage_compact_budget` | `8,000` | **`4,000`** | More aggressive stage compaction for search results |
| `stage_note_chars` | `200` | `200` | Same |
| `keep_recent` | `2` | `2` | Same |
| `preview_chars` | `800` | `800` | Same |

---

## 3. Tool Result Compactor → `QueryToolResultCompactor`

| Aspect | General Default | Query Agent |
|--------|----------------|-------------|
| `client_factory` | `None` (must be set) | `QueryClient.for_l1()` singleton |
| `cfg` | `None` (must be set) | `AGENT_CONFIG` (`QueryAgentConfig`) |
| `pipeline_label` | unset | `"query"` |
| `compactor_registry` | empty | 29 compactors from `card_db_search_tools/_tools_results_compactors/` |
| `reasoning_hook` | `None` | `query_reasoning_tracker.make_reasoning_hook()` |

### Registered Compactors (29)

**Basic search and extraction (25):** `compact_resolve_compound_ids`, `compact_resolve_property_ids`,
`compact_resolve_measurement_ids`, `compact_resolve_reference_ids`,
`compact_resolve_variable_ids`, `compact_resolve_constraint_ids`,
`compact_resolve_phase_ids`, `compact_resolve_solvent_ids`,
`compact_resolve_ids`, `compact_search_id_alignment`,
`compact_search_blocks`, `compact_search_system_registry`,
`compact_search_system_summary`, `compact_search_similar_compounds`,
`compact_search_compound_dk`, `compact_search_property_dk`,
`compact_search_measurement_dk`, `compact_search_references`,
`compact_search_compound_indiv`, `compact_search_measurement_indiv`,
`compact_extract_block_csv`, `compact_extract_multi_block_csv`,
`compact_resolve_card_md`, `compact_block_search_adv`,
`compact_inspect_block_table`

**Block-centric (4):** `compact_search_comp_from_block`,
`compact_search_meas_from_block`, `compact_search_prop_dk_from_block`,
`compact_search_reference_from_block`

---

## 4. Interactive Compactor → `QueryInteractiveCompactor`

| Aspect | General Default | Query Agent | Why |
|--------|----------------|-------------|-----|
| `protect_tools` | `set()` | `set()` (empty) | No protected tools — search results are all compressible |
| `domain_hint` | `""` | `""` (empty) | No domain hint injected |
| `reasoning_hook` | `None` | `query_reasoning_tracker.make_reasoning_hook()` | |

**Simplest possible configuration** — no customization beyond wiring config + reasoning hook.

---

## 5. Working Memory → `QueryWorkingMemory`

| Aspect | General Default (`BaseWorkingMemory`) | Query Agent | Why |
|--------|--------------------------------------|-------------|-----|
| Constructor | `__init__(self)` → `_catalog` dict | `__init__(self, mem_tools=None)` → stores `mem_tools` ref | File-backed memory via MCP tools |
| `record_tool_result()` | Not in base | **New method** — auto-extracts entities from `resolve_compound_ids`, `resolve_property_ids`, `inspect_block`, `search_blocks` | Auto-population of ID catalog |
| `_sync_catalog_to_file()` | Not in base | **New method** — pushes entries to on-disk memory via `mem_tools.memory_catalog_add()` | Persistence |
| `render()` | `render_id_catalog()` | Tries `mem_tools.memory_read()` first; falls back to `render_id_catalog()` | File-backed takes priority |
| File-backed persistence | Not in base | Via `mem_tools` MCP tools (`memory_read`, `memory_add_result`, etc.) | LLM-driven memory model |

Working-memory location is an orchestration input. Every run supplies an
explicit `memory_path`, or supplies `session_dir` from which the orchestrator
derives `session_dir/working_memory.md`. No shared source-tree default exists.

---

## 6. Query-Agent-Only Hooks (no general equivalent)

### 6a. `L1AutoSaver` — Auto-persist L1 results

| Aspect | Notes |
|--------|-------|
| Type | Callable wrapper class (not a hook subclass) |
| Wraps | `dispatch_l1_query` → auto-persists every L1 return to working memory |
| Behaviour | After each L1 call: (1) increments `call_count`, (2) `memory_add_result(key, result[:4000])`, (3) `memory_append_history(...)` |
| Failure guard | If L1 result = "Max iterations reached" and < 120 chars → appends warning telling L0 not to fabricate |
| Why | L0's LLM agent often skips `memory_add_result` calls — this ensures persistence |

### 6b. `thin_answer_guard` — Vacuous-answer detection

| Function | Purpose |
|----------|---------|
| `is_thin_answer(answer, l1_call_count)` | Returns `True` if answer looks like a chatbot stub ("stored in memory", "anything else", etc.) and ≥1 L1 query was executed |
| `force_data_presentation(result, ...)` | Re-prompts LLM with working memory Results section, asking it to include actual data/numbers |
| `THIN_MARKERS` | 12 filler phrases detected |

---

## 7. Tracking Hooks — Thin Wrappers

| Class | Base | Customization |
|-------|------|---------------|
| `QueryHistoryRecorder` | `HistoryRecorder` | None — empty subclass for future extension |
| `QueryStatsRecorder` | `StatsRecorder` | None — empty subclass |
| `QueryReasoningTracker` | `ReasoningTokenTracker` | None — `pass` body |
| `QueryTimeBudgetTracker` | `TimeBudgetTracker` | Config wiring only: `timeout=1000`, `thresholds=[0.65, 0.85, 0.95]`, `max_warnings=3` |

---

## 8. Verdict → `QueryVerdictRunner`

| Aspect | General Default (`VerdictRunner`) | Query Agent | Why |
|--------|----------------------------------|-------------|-----|
| System prompt | `""` | Full scientific-review prompt: "You are an independent scientific reviewer for thermodynamic database queries..." | Domain-specific review |
| `verdict_word_cap` | `None` | `150` | Tight word limit |
| `include_elapsed` | `True` | `True` | Same |
| `answer_char_limit` | `None` | Not set (default) | |
| Default client | Requires `client=` kwarg | Auto-creates `ArgoClient.for_verdict()` if `client=None` | Convenience |
