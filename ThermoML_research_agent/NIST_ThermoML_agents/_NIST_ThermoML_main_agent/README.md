# _NIST_ThermoML_main_agent — Master Orchestrator (L0)

Coordinates the query agent (database search) and the analysis agent
(Redlich-Kister fitting) to answer high-level scientific questions.
Delegates all actual work to subagents — it never touches the database
or fitting code directly.

---

## Quick Start

```python
from NIST_ThermoML_agents._NIST_ThermoML_main_agent import ThermoML_main_run

result = ThermoML_main_run("Compare excess enthalpy of ethanol-water at 298 K and 323 K")
print(result.answer)
```

---

## Public API

| Function | Returns | Description |
|----------|---------|-------------|
| `ThermoML_main_run(question, run_verdict=True)` | `MainRunResult` | Single entry point — wraps `orchestrator.run()` |

### MainRunResult

| Field | Type |
|-------|------|
| `answer` | `str` |
| `verdict` | `str \| None` |
| `iterations` | `int` |
| `elapsed_seconds` | `float` |
| `tool_history` | `list[dict]` |
| `timed_out` | `bool` |
| `session_dir` | `Path` |
| `output_files` | `dict` |

Supports both attribute and dict-style access.

---

## Configuration

| Parameter | Value |
|-----------|-------|
| Max iterations | 40 |
| Wall-clock budget | 40 min |
| LLM | Claude Opus 4.6 |
| Tool-result gate | 30,000 chars (soft — warning banner) |
| PROTECT_TOOLS | None |
| Compaction trigger | Context size > 100,000 chars (turn-based interval disabled) |

The engine config is activated per run via `@with_engine_config(cfg)`;
engine packages only provide an import-time default through
`load_default_config()`, which never overwrites the active run's config
(lazy sibling-agent imports mid-run are safe).

---

## Subagent Delegation Tools

| Tool | Target |
|------|--------|
| `run_query_agent()` | `ThermoML_query_run` (query agent) |
| `run_analysis_agent()` | `ThermoML_analysis_run` (analysis agent) |
| `run_parallel_subagents()` | Mixed batches of the above (ThreadPool) |

Singleton delegations return the child's full JSON answer to the
orchestrator inside a `subagent_answer` marker. The parallel tool instead
returns an internal `ToolResult`: the raw `{n_tasks, results}` batch is
recorded verbatim in working memory while the orchestrator context receives
an **agentically compacted** per-task report (briefed with each task's
original purpose/question; deterministic per-task snapshot if the compaction
LLM fails). Every child run also lands in
`<session>/{query,analysis}_runs/run_N/` with merged tracking tables.

### Entity Propagation

`run_query_agent()` calls `_extract_query_entity_summary(tool_history)`
after the query agent finishes. This parses `L1_query` records for entity
counts (`n_compounds`, `n_properties`, `n_dois`, `n_blocks`,
`n_subsystems`, `n_matching_datapoints`) and appends them to the return
dict so the main agent can cite data scope. Error-shaped records are
skipped.

---

## Anchor Point Wiring

| Anchor | Callback |
|--------|----------|
| `on_reasoning` | `reasoning_capture_hook` → reasoning_tokens_stripped.md |
| `sync_llm_response_after` | `stats_recorder` → iteration counters |
| `sync_tool_call_recorded` | `history_recorder` → tool_history list |
| `sync_tool_result_recorded` | `history_recorder`, `stats_recorder` |
| `sync_compaction_execute` | `MainInteractiveCompactor.should_compact()` |
| `sync_compaction_stats_recorded` | `stats_recorder` → compaction stats |
| `sync_batch_pre_validate` | `batch_validator` → `validate_batch(hooks=engine_hooks)` → fires `SYNC_TOOL_GUIDANCE_CHECK` per tool call |

Lifecycle anchors (`AGENT_START_TRACKING`, `AGENT_RECORD_REFERENCES`, etc.)
wired via `build_agent_lifecycle_bindings()` in `engine_hooks_anchors.py`.

---

## Package Layout

```
_NIST_ThermoML_main_agent/
├── ThermoML_main_api.py              # Public entry point
├── ThermoML_main_argo_config.py      # Config dataclass
├── main_agent_workflows/
│   ├── L0_orchestrator/              # orchestrator.run() + L0_main_workflow.md
│   └── _subworkflow_md_parser/       # parse_workflow(), render_prompt()
├── main_agent_toobox/
│   ├── tool_catalog.py               # MainCatalog
│   ├── subagent_delegation_tools.py  # run_query_agent, run_analysis_agent,
│   │                                 # _extract_query_entity_summary()
│   └── tool_menu/                    # Browse & execute subagent tools
├── main_agent_argo_engine/           # LLM client + terminal UI
├── main_agent_context_hooks/
│   ├── hook_catalog.py               # build_engine_hooks() — single import point
│   ├── compactor_hooks/              # compact_query_result, compact_analysis_result
│   ├── interactive_hooks/
│   ├── memory_hooks/
│   ├── reminder_hooks/
│   ├── tracking_hooks/
│   └── verdict_hooks/
└── main_agent_heath_check_helpers/
```

---

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full wiring diagram.
