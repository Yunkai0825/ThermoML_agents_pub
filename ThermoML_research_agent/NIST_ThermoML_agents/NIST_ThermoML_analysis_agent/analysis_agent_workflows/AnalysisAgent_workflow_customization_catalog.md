# Analysis Agent — Workflow Customization Catalog

> Deviations from `general_subagent_skill_schema_and_parser/` defaults.
> Version 6.0 — 2026-04-08

---

## 1. Orchestrator → `orchestrator.run()`

| Aspect | General Default (`agent_turn`) | Analysis Agent |
|--------|-------------------------------|----------------|
| Entry point | Caller invokes `agent_turn()` | `orchestrator.run()` → prepares session → calls `agent_turn()` |
| Return type | `AgentTurnResult` | `AnalysisRunResult` (custom dataclass wrapping AgentTurnResult + session metadata) |
| Session management | None | `init_session()` / `reopen_session()` — creates session dir, auto-restores working memory |
| Tool wrapping | None | `_wrap_tool()` — every tool call → `working_memory.record_tool_result()` |

### `agent_turn()` parameter overrides

| Parameter | General Signature | Analysis Value |
|-----------|------------------|----------------|
| `max_iterations` | (caller-supplied) | **30** |
| `timeout` | (caller-supplied) | **1200 s** (20 min) |
| `required_tools` | `[]` | **2 fitting tools** (`fit_block`, `fit_multi_system`) |
| `compaction_interval` | (caller-supplied) | **9999** (turn-based compaction disabled — size trigger governs) |
| Verdict | External `VerdictRunner` | **Inline** via `AnalysisVerdictRunner` in orchestrator |

---

## 2. Tier Structure

| Tier | Query Agent | Analysis Agent | Notes |
|------|-------------|----------------|-------|
| L0 | Orchestrator → dispatches to L1 | **Orchestrator → calls tools directly** | Analysis L0 IS the worker |
| L1 | Single dispatcher (12 iter, 360 s) | **2 specialized workers** (L1_DATA: 12 iter / 360 s, L1_FIT: 15 iter / 300 s) | Split by function |
| L2 | 4 specialized searchers (6 iter, 90 s) | **None** | No L2 tier |

---

## 3. L0 Workflow → `analysis_agent_workflows/workflow.md`

### Phase Structure (4 phases — differs from query's 3)

| Phase | Name | Tools Used | Purpose |
|-------|------|-----------|---------|
| 1 | Query Database | `query_thermoml`, `query_thermoml_parallel`, `align_compositions` | Harvest data through query agent + build composition library |
| 2 | Inspect & Extract | `inspect_block`, `get_pure_values` (+ `register_custom_block` fallback) | Deterministic block inspection |
| 3 | Fit Data | `fit_block`, `fit_block_derived`, `fit_multi_system`, `propose_fitting_plan`, `compute_ideal_baseline`, `predict_from_rk` | RK fitting + ideal baseline |
| 4 | Assemble Answer | `list_session_files` (+ LLM synthesis) | Combine query results + fit quality → final verdict |

### Tool count: **11 domain tools** (vs query L0's 9 memory-only tools)

Analysis L0 is the **substantive worker** — it calls domain tools directly
rather than delegating to L1 sub-dispatchers.

---

## 4. L1 Workers (analysis-specific)

### 4a. `l1_query_delegation`

| Aspect | Detail |
|--------|--------|
| File | `L1_workers/l1_query_delegation.py` |
| Function | `dispatch_l1_query(purpose, instruction, id_catalog, context)` |
| What it wraps | Query Agent's `dispatch_l1_query()` — NOT a separate agent_turn, but a direct function call |
| Parallel variant | `dispatch_queries_parallel(queries: list[dict])` → `ThreadPoolExecutor` → parallel exact query objects |
| Client | Uses **query** agent's client, not analysis client |

### 4b. No L1_FIT dispatcher

Despite `AnalysisAgentConfig` defining L1_FIT_* fields, there is no separate
`l1_fit_dispatcher` module. The fitting budget fields exist for **future
extensibility** — current fitting runs directly in L0.

---

## 5. No L2 Workers

Analysis agent has **zero L2 workers**. All database access is delegated to
the query agent via the L1 query delegation layer. The analysis agent never
touches the ThermoML database directly.

---

## 6. Parser / Workflow Rendering

| Aspect | General Default | Analysis Agent |
|--------|----------------|----------------|
| `parse_workflow()` | From `general_subagent_skill_schema_and_parser` | **Re-exported** — no deviation |
| `render_prompt()` | From `general_subagent_skill_schema_and_parser` | **Re-exported** — no deviation |
| Workflow file format | Markdown with `[PHASE]` headers | Same |

---

## 7. Session Management (entirely analysis-specific)

| Function | What It Does |
|----------|-------------|
| `init_session(user_question, output_dir)` | Creates session dir with UUID suffix, initializes `AnalysisWorkingMemory`, writes `manifest.json` |
| `reopen_session(session_dir)` | Loads `working_memory.json` + `manifest.json` from existing session dir |
| `save_session()` | Calls `working_memory.sync_to_disk()` + updates manifest |

Session dirs live under `_output/` with pattern:
`{sanitized_question}_{datetime}_{uuid6}/`

Neither the query agent nor the main agent has this session management
pattern — it is unique to analysis.

---

## 8. `AnalysisRunResult` (custom return type)

```
@dataclass(frozen=True)
class AnalysisRunResult:
    answer: str
    verdict: str
    session_dir: Path
    elapsed_seconds: float
    tool_calls: int
    reasoning_tokens: int
    fit_results: dict        # ← analysis-specific
    query_results: dict      # ← analysis-specific
    inspected_blocks: dict   # ← analysis-specific
```

General `AgentTurnResult` only has `answer`, `tool_calls`, `elapsed_seconds`,
`reasoning_tokens`. Analysis adds 4 domain-specific fields + verdict + session_dir.
