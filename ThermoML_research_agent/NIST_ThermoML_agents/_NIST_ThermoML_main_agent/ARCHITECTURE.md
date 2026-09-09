# ThermoML Main Agent — Architecture  (v6.0)

> Master orchestrator that answers scientific thermodynamic questions
> by coordinating the **Query Agent** (database search) and the
> **Analysis Agent** (Redlich-Kister fitting).  
> **Companion**: [System architecture](../ARCHITECTURE.md) and [agent usage](../README.md).

---

## Package Layout

```
_NIST_ThermoML_main_agent/
│
├── __init__.py
├── ThermoML_main_argo_config.py        # MainAgentConfig(EngineConfig)
├── ThermoML_main_api.py                # ThermoML_main_run(question, *, run_verdict, session_dir)
│
├── main_agent_argo_engine/
│   ├── __init__.py                     # loads config, re-exports MainClient
│   ├── argo_client.py                  # MainClient(ArgoClient) + for_l0()
│   └── main_agent_terminal_ui.py       # MainAgentTerminalUI — interactive CLI
│
├── main_agent_toobox/
│   ├── __init__.py
│   ├── subagent_delegation_tools.py    # run_query_agent, run_analysis_agent,
│   │                                   # run_parallel_subagents
│   │                                   # uses shared SubagentSessionManager,
│   │                                   # build_full_question, extract_run_result,
│   │                                   # dispatch_parallel, merge_subagent_tracking
│   │                                   # from general_subagent_delegation_helpers
│   ├── tool_catalog.py                 # MainCatalog(AgentToolCatalog) + flat dict
│   └── tool_menu/
│       ├── __init__.py
│       ├── menu_tools.py               # browse_subagent_tools, run_subagent_tool
│       └── _registry_builder.py         # Lazy ToolMenuRegistry tree
│
├── main_agent_context_hooks/
│   ├── __init__.py
│   ├── hook_catalog.py                 # central re-export hub + singletons
│   │
│   ├── compactor_hooks/
│   │   ├── __init__.py
│   │   ├── _tool_compactors.py         # compact_query_result, compact_analysis_result
│   │   ├── tool_result_compactor.py    # MainToolResultCompactor
│   │   └── context_stage_compaction.py # MainStageCompactor
│   │
│   ├── interactive_hooks/
│   │   ├── __init__.py
│   │   └── interactive_compactor.py    # MainInteractiveCompactor
│   │
│   ├── memory_hooks/
│   │   ├── __init__.py
│   │   └── working_memory_hooks.py     # MainWorkingMemory (query/analysis/parallel results)
│   │
│   ├── tracking_hooks/
│   │   ├── __init__.py
│   │   ├── history_hooks.py            # MainHistoryRecorder
│   │   ├── stats_hooks.py              # MainStatsRecorder
│   │   └── time_budget_hooks.py        # MainTimeBudgetTracker
│   │
│   └── verdict_hooks/
│       ├── __init__.py
│       └── postjob_verdict.py          # MainVerdictRunner + run_verdict()
│
├── main_agent_workflows/
│   ├── __init__.py
│   ├── _subworkflow_md_parser/         # thin wrapper → shared parser
│   └── L0_orchestrator/
│       ├── __init__.py
│       ├── orchestrator.py             # run() — THE main entry point
│       └── L0_main_workflow.md         # system prompt (lightweight)
│
└── _DEBUG_script/
    ├── run_tests.py                    # test runner
    └── test_prompts.md                 # scientific test questions
```

---

## Data Flow

```
User question
       │
       ▼
ThermoML_main_run(question,  ← ThermoML_main_api.py
  run_verdict=True,
  session_dir=None)
       │
       ▼
orchestrator.run()           ← L0_orchestrator/orchestrator.py
       │
       ├─── init_session()   ← session_manager
       ├─── load_workflow()  ← L0_main_workflow.md
       ├─── build tools      ← tool_catalog + health_check
       ├─── wrap tools       ← auto-record to WorkingMemory
       │
       ▼
agent_turn()                 ← general_argo_engine_helpers (ReAct loop)
       │
       ├── LLM decides which subagent(s) to call
       │      │
       │      ├── run_query_agent()          → ThermoML_query_run()
       │      │     └─ _extract_query_entity_summary(tool_history)
       │      │          → {n_compounds, n_properties, n_dois,
       │      │             n_blocks, n_subsystems, n_matching_datapoints}
       │      ├── run_analysis_agent()       → ThermoML_analysis_run()
       │      └── run_parallel_subagents()   → ThreadPool × mixed dispatch
       │            └─ ToolResult: raw batch → working memory,
       │               agentically compacted per-task report → context
       │               (deterministic snapshot if the compactor LLM fails)
       │
       ├── WorkingMemory records all results
       │     ├── _record_query()/_record_analysis() keep full child answers
       │     └── Entity counts propagated via _extract_query_entity_summary()
       ├── InteractiveCompactor manages context size
       ├── HistoryRecorder writes run_history.md
       └── StatsRecorder tracks DOI/entity references + compaction outcomes
       │
       ▼
Verdict agent                ← postjob_verdict.py
       │
       ▼
MainRunResult                ← answer + verdict + metadata
       │
       ▼
_save_run_output()           ← result.md in session_dir
```

---

## Key Configuration (ThermoML_main_argo_config.py)

| Parameter               | Value  | Rationale                         |
|--------------------------|--------|-----------------------------------|
| MODEL                    | claudeopus46 | Same model across all agents |
| MAX_TOOL_ITERATIONS      | 40     | Multi-subagent workflows need many calls |
| MAX_TURN_SECONDS         | 2400   | 40 min — subagent calls are slow  |
| TOOL_RESULT_CHAR_LIMIT   | 30000  | Soft limit — oversized results carry a size-warning banner |
| COMPACTION_TRIGGER_CHARS  | 100000 | Higher threshold for verbose results |
| COMPACTION_INTERVAL       | 999    | > MAX_TOOL_ITERATIONS — turn-based compaction disabled; the size trigger governs |
| PROTECT_TOOLS             | ∅      | All tool results can be compacted |

---

## Tools Available to the Main Agent

| Tool                      | Purpose                               | Compacted? |
|---------------------------|---------------------------------------|------------|
| `run_query_agent`         | Search ThermoML databases             | Yes        |
| `run_analysis_agent`      | RK fitting + quantitative analysis    | Yes        |
| `run_parallel_subagents`  | Batch mixed query+analysis dispatch   | Yes (agentic batch; raw → working memory) |
| `browse_subagent_tools`   | Walk hierarchical subagent tool menu  | No (raw)   |
| `run_subagent_tool`       | Execute any subagent tool by name     | No (raw)   |
| `list_session_files`      | Session file manifest                 | No (raw)   |

---

## Shared Infrastructure

All agents (query, analysis, main) share:

- **`general_argo_engine_helpers`** — `EngineConfig`, `ArgoClient`, `agent_turn()`, `AgentTurnResult`, `AnchorPoint` (65 anchor types + 5 agent-level), `anchor()` dispatch, `AgentHookCollection`, singleton patching
- **`general_text_context_marker_catalog`** — `ContextMarkerCatalog` (13 XML tag families), `TagPair` frozen dataclass, `MARKERS` singleton
- **`general_tool_management_helpers`** — `AgentToolCatalog`, `ToolEntry`, `ToolResult`, `run_health_check()`, `PreExecutionGuidance`, tool anchor catalog (19 types)
- **`general_hooks_management_helpers/general_context_hooks`** — `TimeBudgetTracker`, `HistoryRecorder` (+ `log_internal_error()`), `StatsRecorder`, `ReasoningTokenTracker`, 3-step LLM compaction engine, context anchor catalog (31 types)
- **`general_hooks_management_helpers/general_memory_management_tools_hooks_helpers`** — `BaseWorkingMemory`, `SessionManager`, 8 MCP tools, `make_instrumented_wrapper()`, memory anchor catalog (10 types)
- **`general_hooks_management_helpers/general_tracking_hooks_output_helpers`** — `output_writers`, `answer_cleaner`
- **`general_subagent_delegation_helpers`** — `SubagentSessionManager`, `build_full_question`, `extract_run_result`, `dispatch_parallel`, `merge_subagent_tracking`
- **`general_subagent_skill_schema_and_parser`** — `parse_workflow()`, `build_tool_instructions()`

---

## Anchor Point Wiring

The main agent's `hook_catalog.py` subclasses `AgentHookCollection` and
overrides `build_engine_hooks()` to return `HookBinding`s that map anchor
types to concrete callbacks:

| Anchor Type | Wired To |
|-------------|----------|
| `sync_llm_response_after` | `MainHistoryRecorder.log_llm_response` |
| `sync_tool_call_recorded` | `MainHistoryRecorder.log_tool_call` |
| `sync_tool_result_recorded` | `MainStatsRecorder.log_tool_result` |
| `sync_compaction_execute` | `MainInteractiveCompactor.check_trigger` |
| `sync_compaction_stats_recorded` | `MainStatsRecorder.log_compaction` (outcome column) |
| `sync_compaction_skipped` | `MainStatsRecorder.log_compaction` (skips are logged too) |
| `on_reasoning` | `MainReasoningTracker.log_reasoning_from_response` |
| `sync_batch_pre_validate` | `batch_validator` → `validate_batch(hooks=engine_hooks)` → fires `SYNC_TOOL_GUIDANCE_CHECK` per tool call |
| … | *(additional anchors wired per agent needs)* |

The 5 agent-level lifecycle anchors (`AGENT_START_TRACKING`,
`AGENT_FINALIZE_TRACKING`, `AGENT_RECORD_REFERENCES`,
`AGENT_SAVE_FINAL_CONTEXT`, `AGENT_RUN_VERDICT`) are wired via
`build_agent_lifecycle_bindings()` in `engine_hooks_anchors.py`.

The compiled hooks dict is passed to `agent_turn(hooks=…)` and the engine
fires anchor points at 65+ pipeline locations without importing any hook
directly.

---

## Session Output Files

Each run produces these files in the session directory:

| File | Generator | Content |
|------|-----------|---------|
| `result.md` | Orchestrator | Final answer + metadata |
| `run_history.md` | `MainHistoryRecorder` | Chronological event log |
| `_working_memory.md` | `MainWorkingMemory` | Structured memory snapshot |
| `reference_stats.md` | `MainStatsRecorder` | API call stats, tool stats, compaction outcomes, wall time |
| `reasoning_tokens_stripped.md` | `ReasoningTokenTracker` | Captured `<reasoning>` tokens |
| `final_full_context.md` | `VerdictRunner` | Complete context at verdict time |
| `query_runs/run_N/`, `analysis_runs/run_N/` | Child runners | Full per-child sessions (result.md, tracking MDs, working memory) |
| `subagents_combined_*.md` | `merge_subagent_tracking` | Child histories/stats/reasoning merged at the parent root, labelled `label (query_runs/run_N)` |
