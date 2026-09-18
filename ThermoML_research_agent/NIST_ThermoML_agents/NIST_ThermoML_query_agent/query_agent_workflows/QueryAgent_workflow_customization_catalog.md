# Query Agent — Workflow Customization Catalog

> Deviations from `general_argo_engine_helpers/` and `general_subagent_skill_schema_and_parser/` defaults.
> Version 6.0 — 2026-04-08

---

## 1. L0 Orchestrator — `orchestrator.py`

### 1a. `run()` Signature

```python
run(user_question, memory_path, extra_tools, client,
    round_number=1, session_dir, prev_context, prev_working_memory)
```

### 1b. `agent_turn()` Parameters

| Parameter | Value | vs. General Default | Why |
|-----------|-------|---------------------|-----|
| `max_iterations` | Not passed → `cfg.MAX_TOOL_ITERATIONS` = **25** | Reads from config | |
| `timeout` | Not passed → `cfg.MAX_TURN_SECONDS` = **1000** | Reads from config | |
| `client` | `QueryClient.for_l0()` | Agent-specific tier | |
| `working_memory_loader` | `make_wm_loader(mem_tools)` → file read each iteration | File-backed | |
| `hooks` | `build_engine_hooks()` → 8 anchor callbacks | Agent-specific singletons | |
| `required_tools` | Not passed (None) | Default | |
| `compactor_fn` | Not passed (None → built-in compact_memory) | Default | |
| `compaction_interval` | Not passed (None) | Default | |
| `batch_summary_hook` | Not passed (None) | Default | |

### 1c. Query-Specific Orchestrator Features

| Feature | Description | Why |
|---------|-------------|-----|
| **Tool registration** | 8 memory tools from `L0_TOOL_CATALOG` + `L1_query` wrapped by `L1AutoSaver` | Auto-save guarantee |
| **Health check** | `run_health_check(L0_CATALOG, tools, "query-L0")` | Startup validation |
| **Tool instructions** | `build_tool_instructions(tools)` injected into system prompt | Teaches LLM the tool API |
| **Continuation support** | `round_number > 1` → prepends `prev_context` as prior conversation | Multi-round sessions |
| **Thin-answer guard** | Post-loop: `is_thin_answer()` → `force_data_presentation()` | Prevents vacuous answers |
| **Hardcoded workflow** | `hardcoded_L0_wf_run()` — async entry using `run_workflow()` pipeline | Non-LLM-driven phase execution |

---

## 2. L0 Workflow — `L0_orchestrator_workflow.md`

| Aspect | Value |
|--------|-------|
| `agent_id` | `L0_orchestrator` |
| `layer` | `0` |
| `parent` | `user` |

### System Prompt Identity

"You are the ThermoML Query Orchestrator" — manages working memory,
dispatches L1 workers, anti-hallucination rules, answer formatting,
common property IDs reference table.

### Tool Groups

| Group | Count | Tools |
|-------|-------|-------|
| `memory` | 8 | `memory_read`, `memory_append_history`, `memory_add_result`, `memory_catalog_add`, `memory_catalog_remove`, `memory_catalog_list`, `memory_compact`, `memory_reset` |
| `L1_dispatch` | 1 | `L1_query` |

### Phases

| # | Name | Description |
|---|------|-------------|
| 1 | `understand_and_plan` | Parse question, identify compounds/properties |
| 2 | `dispatch_query` | Send L1 queries |
| 3 | `compact_and_answer` | Consolidate, format final answer |

### Response JSON Schema

```json
{ "answer", "confidence", "sources", "id_catalog_snapshot", "follow_up_suggestions" }
```

---

## 3. L1 Query Dispatcher — `l1_query_dispatcher.py`

### `agent_turn()` Parameters (differ from L0)

| Parameter | Value | vs. L0 | Why |
|-----------|-------|--------|-----|
| `max_iterations` | `cfg.L1_MAX_ITERATIONS` = **12** | Explicit (L0 uses config default 25) | L1 workers need fewer iterations |
| `timeout` | `cfg.L1_MAX_SECONDS` = **360** (6 min) | Explicit (L0 uses 1000) | Tighter budget per L1 dispatch |
| `compaction_interval` | `cfg.L1_COMPACTION_INTERVAL` = **999** | Explicit (L0 doesn't pass) | Turn-based compaction disabled — size trigger governs |
| `client` | `QueryClient.for_l1()` | L1 tier | Same model, different tier label |

### L1 Workflow — `L1_query_workflow.md`

| Aspect | Value |
|--------|-------|
| `agent_id` | `L1_query` |
| `layer` | `1` |
| `parent` | `L0_orchestrator` |

**System prompt identity:** "You are a ThermoML database query worker" —
ID resolution rules, strict global format (`GLOBcomp_12`, `GLOBprop_4`),
DOI/block-local namespaces (`DOIcomp_N`, `BLKprop_N`, `BLKvar_N`,
`BLKconstr_N`, `PROPblock_N`, `RXNblock_N`), efficiency
rules (max 3 tool calls, no redundant verification).

**Tool groups (5):** `id_resolution` (6), `block_search` (3),
`compound_similarity` (1), `L2_subagents` (4), `compactors` (2).

**Phases (4):** `resolve_ids` → `search_and_filter` (with compaction) →
`deep_evaluate` (parallel L2 dispatch, `max_concurrent: 8`) → `assemble_return`.

---

## 4. L2 Leaf Evaluators — `l2_dispatchers.py`

### `agent_turn()` Parameters

| Parameter | Value | vs. L1 | Why |
|-----------|-------|--------|-----|
| `max_iterations` | `cfg.L2_MAX_ITERATIONS` = **6** | Much smaller | Brief focused evaluation |
| `timeout` | `cfg.L2_MAX_SECONDS` = **90** | Much smaller | Quick leaf-level check |
| `client` | `QueryClient.for_l2()` — `max_tokens=2000` | Smaller token budget | Leaf summaries are brief |

### L2 Workflows (4 files, all follow same pattern)

| Workflow | agent_id | Tools | Phases |
|----------|----------|-------|--------|
| `L2_comp_eval_workflow.md` | `L2_comp_eval` | `search_comp_from_block`, `search_compound_dk`, `search_compound_indiv` | fetch → fill_gaps → summarise |
| `L2_meas_eval_workflow.md` | `L2_meas_eval` | `search_meas_from_block`, `search_measurement_dk`, `search_measurement_indiv` | fetch → fill_gaps → summarise |
| `L2_ref_eval_workflow.md` | `L2_ref_eval` | `search_reference_from_block`, `search_references` | fetch → fill_gaps → summarise |
| `L2_prop_eval_workflow.md` | `L2_prop_eval` | `search_prop_dk_from_block`, `search_property_dk` | fetch → fill_gaps → summarise |

All have `layer: 2`, `parent: L1_query`.

**No compaction pipeline** — L2 tools are raw callables, no `compact_tool_result`.

---

## 5. Subworkflow Parser

| Aspect | General Default | Query Agent |
|--------|----------------|-------------|
| Implementation | `general_subagent_skill_schema_and_parser.parse_workflow` | **Pure re-export** — no custom logic |

Thin redirect so import paths within the query agent resolve correctly.

---

## 6. Summary: 3-Tier Iteration/Budget Hierarchy

| Tier | Iterations | Timeout | Token Budget | Compaction |
|------|-----------|---------|-------------|------------|
| L0 | 25 | 17 min | 6000 | Built-in (on demand) |
| L1 | 12 | 6 min | 6000 | Every 3 calls |
| L2 | 6 | 90 sec | 2000 | None |
