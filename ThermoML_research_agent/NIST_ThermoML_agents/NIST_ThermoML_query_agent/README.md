# ThermoML Query Agent

**ReAct-based LLM agent that answers thermodynamic-data questions by searching card databases built from NIST ThermoML XML archives.**

---

## Quick start

Run Python from `ThermoML_research_agent/` after installing the workspace
dependencies and configuring provider access.

```python
from pathlib import Path
from NIST_ThermoML_agents.NIST_ThermoML_query_agent.ThermoML_query_api import (
    ThermoML_query_run,
)

result = ThermoML_query_run(
    "What is the density of ethanol at 298.15 K?",
    session_dir=Path("..") / "_output" / "Query" / "example_query",
)
print(result.answer)
```

The synchronous `ThermoML_query_run()` is the primary entry-point.
An async hardcoded-workflow variant is also available. In an async function or
notebook, supply the question, a configured tool executor, and a memory path:

```python
from NIST_ThermoML_agents.NIST_ThermoML_query_agent.ThermoML_query_api import (
    ThermoML_query_hardcoded_L0_wf_run,
)

result = await ThermoML_query_hardcoded_L0_wf_run(
    question, tool_executor,
    memory_path=Path("..") / "_output" / "Query" / "example_workflow" / "working_memory.md",
)
```

See [`ThermoML_query_api.py`](ThermoML_query_api.py) for full signatures and docstrings.

---

## Installation

### Python environment

Use the [workspace installation instructions](../../../README.md). From the
workspace root, install the runtime dependencies with:

```powershell
python -m pip install -r ThermoML_research_agent/requirements.txt
```

The project is imported from `ThermoML_research_agent/`; it is not distributed
as an installable Python package. No machine-specific interpreter path is required.

### Required Python packages

| Package | Purpose |
|---------|---------|
| `requests` | Argo API HTTP calls |
| `asyncio` | Parallel L2 dispatch |
| `sqlite3` | Card-database queries (stdlib) |
| `json`, `re`, `pathlib`, `threading` | Standard library utilities |

All are either stdlib or pre-installed in the Anaconda base environment.

### `sys.path` setup

Scripts that run the agent (e.g. the test runner) insert the **workspace root** into `sys.path` so that `NIST_ThermoML_agents.*` imports resolve:

```python
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))  # → ThermoML_research_agent/
```

The test runner in `_DEBUG_script/run_tests.py` already handles this.

---

## Architecture overview

The agent uses a **three-tier ReAct hierarchy** orchestrated by an LLM (Argo API, model `claudeopus46`):

```
L0  Orchestrator     — plans, dispatches L1 calls, compacts, delivers final answer
 └─ L1  Workers      — query dispatchers that fan out to L2 evaluators
     └─ L2  Evaluators — leaf-level compound/property/measurement/reference evaluators
```

### Key modules

| Path | Role |
|------|------|
| `ThermoML_query_api.py` | **Public API** — `ThermoML_query_run()` and `ThermoML_query_hardcoded_L0_wf_run()` |
| `ThermoML_query_argo_config.py` | `QueryAgentConfig(EngineConfig)` dataclass — all query-agent settings |
| `query_agent_argo_engine/` | `QueryClient` factory (`.for_l0()`, `.for_l1()`, `.for_l2()`, `.for_verdict()`), interactive CLI |
| `query_agent_toolbox/tool_catalog.py` | `QueryL0Catalog(AgentToolCatalog)` — class-based tool catalog + `L0_TOOL_CATALOG` flat dict |
| `query_agent_context_hooks/hook_catalog.py` | **Single entry point** for all hooks (compactors, interactive, memory, tracking, verdict) |
| `query_agent_workflows/L0_orchestrator/` | Top-level orchestrator + L0 workflow markdown |
| `query_agent_workflows/L1_workers/` | L1 query dispatchers + L1 workflow markdown |
| `query_agent_workflows/L2_leaf_evaluators/` | L2 compound/property/measurement/reference evaluators + workflow markdowns |
| `query_agent_workflows/_subworkflow_md_parser/` | Markdown-driven sub-workflow loader + parser |

For the full module map and data-flow diagrams, see [`../../ARCHITECTURE.md`](../ARCHITECTURE.md) (v6.0).

### Anchor-Point Wiring

All hook callbacks are wired through the **anchor-point architecture**
(`engine_hooks_anchors.py`).  Each agent's `hook_catalog.py` subclasses
`AgentHookCollection` and overrides `build_engine_hooks()` to return
`HookBinding` iterables compiled into the dispatch dict.

| Anchor | Query Agent Callback |
|--------|---------------------|
| `ON_REASONING` | `capture_reasoning_tokens()` → reasoning_tokens_stripped.md |
| `LLM_RESPONSE_AFTER` | `QueryStatsRecorder` → iteration counters |
| `ON_TOOL_CALL` | `QueryHistoryRecorder` → tool_history list |
| `ON_TOOL_RESULT` | `QueryHistoryRecorder`, `QueryStatsRecorder` |
| `COMPACTION_TRIGGER` | `QueryInteractiveCompactor.should_compact()` |
| `ON_COMPACTION_STATS` | `QueryStatsRecorder` → compaction stats |
| `WORKING_MEMORY_LOAD` | `QueryWorkingMemory.load()` |
| `WORKING_MEMORY_RENDER` | `QueryWorkingMemory.render()` |
| `SYNC_BATCH_PRE_VALIDATE` | `batch_validator` → `validate_batch(hooks=engine_hooks)` → fires `SYNC_TOOL_GUIDANCE_CHECK` per tool call |

### Context Markers

XML tags for structured LLM output are defined in
`general_text_context_marker_catalog.ContextMarkerCatalog` (13 families).
The query agent consumes `MARKERS.tool_call`, `MARKERS.tool_result`,
`MARKERS.reasoning`, `MARKERS.answer`, etc.

### ReAct loop

Each tier runs a **ReAct loop** (`argo_engine_helpers/react_loop.py`):

1. LLM receives system prompt + conversation history
2. LLM emits a tool call (or a final answer)
3. Tool is executed, result appended to history
4. Repeat until the agent produces a final answer or hits the iteration cap

Compactors kick in automatically when the conversation context grows too large, summarising tool outputs to stay within token limits.

### Answer contract

The working agent's final `<answer>` is plain prose. The shared post-answer
lifecycle (see `general_postans_eval_hooks/`) then distills `core_claims`,
aligns IDs/metadata from the recorded tool history, reconciles literature
identities (**registered `GLOBlit_N` is authoritative over DOIs**), and
assembles the JSON envelope consumed downstream. The advanced block-search
tool (`block_search_adv`) walks its three-stage pre-execution review
automatically inside the tool — agents never emit confirmation tokens.

---

## Workspace dependencies

The query agent depends on **sibling directories** within `NIST_ThermoML_agents/`:

| Directory | What it provides |
|-----------|-----------------|
| `general_argo_engine_helpers/` | Shared ReAct engine (`agent_turn`, `ArgoClient`, `EngineConfig`), **anchor-point architecture** (`AnchorPoint`, `anchor()`, `AgentHookCollection`, singleton patching) |
| `general_tool_management_helpers/` | `AgentToolCatalog`, `ToolEntry`, `CompactorCatalog`, health checks, KEEP/DISCARD subagent, tool anchor catalog |
| `general_hooks_management_helpers/general_context_hooks/` | Runtime hooks: `TimeBudgetTracker`, 3-step compaction, `HistoryRecorder` (+ `log_internal_error()`), `StatsRecorder`, reasoning capture, context anchor catalog (31 types) |
| `general_hooks_management_helpers/general_memory_management_tools_hooks_helpers/` | File-backed working memory (8 MCP tool wrappers), `BaseWorkingMemory`, `SessionManager`, `make_instrumented_wrapper()`, memory anchor catalog (10 types) |
| `general_text_context_marker_catalog/` | `ContextMarkerCatalog` — 13 XML tag families (`tool_call`, `reasoning`, `answer`, etc.) |
| `general_db_search_tool_registry/` | Auto-discovered 27 search tools across 4 categories |
| `general_subagent_skill_schema_and_parser/` | Workflow `.md` parser + tool-description generators |
| `general_ThermoML_db_csv_registry/` | Central registry of DB/CSV paths |

External workspace dependencies (outside `NIST_ThermoML_agents/`):

| Directory | What it provides |
|-----------|-----------------|
| `card_databases_storage/` | SQLite databases: `CCS_ID_DK.db`, `MTDKS_INDIV.db`, `PCS_ID_DK.db`, `PCS_INDIV.db`, etc. + `ID_architecture.md` |
| `card_db_search_tools/` | Search-tool implementations consumed by the DB search registry |
| `ThermoML_card_json_to_md_compactors/` | Card → markdown renderers used by search tools |
| `specialized_tools_pipelines/` | Deterministic screening & ranking pipeline exposed as a search tool |

---

## Test runner

The unified test runner lives in `_DEBUG_script/run_tests.py`.
It reads prompts from `_DEBUG_script/test_prompts.md` and writes campaigns to
`_benchmark/Query/test_run_<timestamp>/` at the workspace root. These are live
agent benchmarks requiring provider access; see the [benchmark guide](_DEBUG_script/README.md).

```bash
# All prompts, 5 workers (default)
python -m NIST_ThermoML_agents.NIST_ThermoML_query_agent._DEBUG_script.run_tests

# Or run directly (sys.path auto-configured)
python _DEBUG_script/run_tests.py

# Specific prompts
python _DEBUG_script/run_tests.py 1.1 2.1 3.3

# Entire section
python _DEBUG_script/run_tests.py --section 3

# Sequential (1 worker)
python _DEBUG_script/run_tests.py --workers 1

# 8 threads, 4-second gap between API calls
python _DEBUG_script/run_tests.py --workers 8 --gap 4
```

Output structure:

```text
_benchmark/Query/test_run_<timestamp>/
├── Q1.1/
│   ├── result.md
│   ├── tool_trace.md
│   ├── run_history.md
│   └── working_memory.md
├── Q2.1/
├── TEST_SUMMARY_*.md
└── TEST_TRACE_*.json
```

`--output` overrides the campaign directory. Freeform Query sessions use the
shared `_output/Query/` directory; the Python API requires an explicit session or memory path.

---

## Configuration

All settings live in [`ThermoML_query_argo_config.py`](ThermoML_query_argo_config.py) as a
single `QueryAgentConfig(EngineConfig)` dataclass.  Step 1 fields set defaults
for the 26 shared engine parameters; Step 2 fields are query-agent-only.

Consumers import the singleton `AGENT_CONFIG` instance:
```python
from ..ThermoML_query_argo_config import AGENT_CONFIG as cfg
```

| Field | Default | Section | Purpose |
|-------|---------|---------|--------|
| `API_URL` | `https://apps-dev.inside.anl.gov/argoapi/api/v1/resource/chat/` | Step 1 | Argo REST chat endpoint |
| `API_USER` | `$ARGO_API_USER`; blank otherwise | Step 1 | API authentication; no personal fallback |
| `MODEL` | `claudeopus46` | Step 1 | L0 orchestrator + L1 worker model |
| `VERDICT_MODEL` | `claudeopus46` | Step 1 | Post-job quality reviewer |
| `PLANNER_MODEL` | `claudeopus46` | Step 1 | Strategy planner |
| `MAX_TOOL_ITERATIONS` | `25` | Step 1 | L0 tool-call iteration cap |
| `MAX_TURN_SECONDS` | `1000` | Step 1 | L0 wall-clock budget (≈17 min) |
| `VERDICT_MAX_TOKENS` | `500` | Step 1 | Verdict response budget |
| `TOOL_RESULT_CHAR_LIMIT` | `24000` | Step 1 | Post-compaction size contract; oversize raises |
| `COMPACTION_TRIGGER_CHARS` | `80000` | Step 1 | Context size triggering compaction |
| `L1_MODEL` | `claudeopus46` | Step 2 | L1 query dispatcher model |
| `L2_MODEL` | `claudeopus46` | Step 2 | L2 leaf evaluator model |
| `L1_MAX_ITERATIONS` | `12` | Step 2 | L1 dispatcher iteration cap |
| `L1_MAX_SECONDS` | `360` | Step 2 | L1 wall-clock budget (6 min) |
| `SUBAGENT_MAX_TOKENS` | `700` | Step 2 | Tool sub-agent response budget |
| `KEEP_RECENT_RESULTS` | `2` | Step 2 | Recent results exempt from trimming |
| `L1_COMPACTION_INTERVAL` | `999` | Step 2 | > L1 iteration cap — turn-based compaction disabled; size trigger governs |
| `BLOCK_CONDENSE_LIMIT` | `10000` | Step 2 | Block-level condensation trigger |

---

## Directory layout

```
NIST_ThermoML_query_agent/
├── ThermoML_query_api.py             # Public API entry-point
├── ThermoML_query_argo_config.py     # LLM / API configuration
├── __init__.py
├── README.md                         # ← This file
│
├── query_agent_argo_engine/          # Agent-specific LLM client
│   ├── __init__.py
│   ├── argo_client.py                #   QueryClient (for_l0, for_l1, for_l2, for_verdict)
│   └── query_agent_terminal_ui.py    #   Interactive CLI REPL
│
├── query_agent_toolbox/              # Tool catalog
│   ├── __init__.py
│   └── tool_catalog.py              #   QueryL0Catalog + L0_TOOL_CATALOG flat dict
│
├── query_agent_context_hooks/        # All context hooks (5 sub-categories)
│   ├── hook_catalog.py              #   Single entry point (re-exports all)
│   ├── compactor_hooks/             #   Tool-result + stage compaction
│   │   ├── tool_result_compactor.py #     QueryToolResultCompactor
│   │   └── context_stage_compaction.py # QueryStageCompactor
│   ├── interactive_hooks/           #   LLM-driven 3-step context compaction
│   │   └── interactive_compactor.py #     QueryInteractiveCompactor
│   ├── memory_hooks/                #   Memory lifecycle
│   │   ├── working_memory_hooks.py  #     QueryWorkingMemory, init, loader
│   │   ├── l1_autosave_hooks.py     #     L1AutoSaver
│   │   └── thin_answer_guard.py     #     Thin-answer detection
│   ├── tracking_hooks/              #   Observability recorders
│   │   ├── history_hooks.py         #     QueryHistoryRecorder
│   │   ├── stats_hooks.py           #     QueryStatsRecorder
│   │   └── time_budget_hooks.py     #     QueryTimeBudgetTracker
│   └── verdict_hooks/               #   Post-job review
│       └── postjob_verdict.py       #     QueryVerdictRunner
│
├── query_agent_workflows/            # Workflow orchestration
│   ├── L0_orchestrator/             #   run() + L0 workflow markdown
│   │   ├── orchestrator.py
│   │   └── L0_orchestrator_workflow.md
│   ├── L1_workers/                  #   L1 query dispatcher + workflow
│   │   ├── l1_query_dispatcher.py
│   │   └── L1_query_workflow.md
│   ├── L2_leaf_evaluators/          #   4× L2 dispatchers + workflows
│   │   ├── l2_dispatchers.py
│   │   ├── L2_comp_eval_workflow.md
│   │   ├── L2_meas_eval_workflow.md
│   │   ├── L2_prop_eval_workflow.md
│   │   └── L2_ref_eval_workflow.md
│   └── _subworkflow_md_parser/      #   Workflow .md parser
│       └── subworkflow_parser.py
│
├── query_agent_heath_check_helpers/  # (empty — reserved for agent-specific checks)
│
├── _DEBUG_script/                    # Test runner + prompts
│   ├── run_tests.py
│   └── test_prompts.md
└── (benchmark output is outside this package, under workspace/_benchmark/Query/)
```
