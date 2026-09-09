# NIST ThermoML agent architecture

This reference describes the current executable package. Start with the
[agent README](README.md) for API examples and launch commands, or the
[data-platform architecture](../MASTER_ARCHITECTURE.md) for card schemas and imports.

## Package boundaries

The active agent packages are `_NIST_ThermoML_main_agent/`,
`NIST_ThermoML_query_agent/`, and `NIST_ThermoML_analysis_agent/`. Their shared
runtime is under `general_db_query_engine/`. The Editing directory is a stub.

The agents consume sibling packages within `ThermoML_research_agent/`:

- `card_db_search_tools/` resolves identifiers, searches systems and publications,
  reads cards, and extracts numeric tables.
- `ThermoML_card_json_to_md_compactors/` renders structured cards as compact text.
- `specialized_tools_pipelines/` implements deterministic property screening and ranking.
- `card_databases_storage/` and `ThermoML.v2020-09-30.db/` contain the included data assets.

`ThermoML_database_browser/` is outside the research-agent directory at the
workspace root. It calls the public agent APIs and renders the saved artifacts;
it does not own the engine's configuration or session lifecycle.

## Agent hierarchy

Main is the top-level coordinator. It delegates complete requests to Query and
Analysis, supports parallel subagent work, and can use the subagent tool menu.

Query uses an L0 orchestrator, L1 query workers, and L2 evaluators for compound,
measurement, property and reference evidence. L1 workers resolve and collect
canonical identifiers and blocks. L2 evaluators inspect the relevant card families.
The working-memory layer persists structured evidence between tool calls.

Analysis combines data retrieval with composition alignment, ideal-baseline
calculation, Redlich–Kister fitting, and diagnostics. It can delegate to the full
Query agent or invoke the query-worker path through its query-delegation tools.
Its loop is driven by its workflow and catalog rather than a fixed four-phase API.

| Public boundary | Orchestration implementation |
|---|---|
| [Main API](_NIST_ThermoML_main_agent/ThermoML_main_api.py) | [Main orchestrator](_NIST_ThermoML_main_agent/main_agent_workflows/L0_orchestrator/orchestrator.py) |
| [Query API](NIST_ThermoML_query_agent/ThermoML_query_api.py) | [Query orchestrator](NIST_ThermoML_query_agent/query_agent_workflows/L0_orchestrator/orchestrator.py) |
| [Analysis API](NIST_ThermoML_analysis_agent/ThermoML_analysis_api.py) | [Analysis orchestrator](NIST_ThermoML_analysis_agent/analysis_agent_workflows/L0_orchestrator/orchestrator.py) |

## Configuration and provider calls

[`EngineConfig`](general_db_query_engine/general_argo_engine_helpers/engine_config.py)
is the shared dataclass contract. Each agent subclasses it in its
`ThermoML_*_argo_config.py`. `load_default_config` supplies the default configuration;
`with_engine_config` sets and restores the active configuration using `ContextVar`.
A nested agent therefore runs with its own settings and returns control to its
caller's configuration.

The shared [`ArgoClient`](general_db_query_engine/general_argo_engine_helpers/argo_client_caller.py)
builds provider payloads, validates request settings, performs HTTP calls, applies
retry behavior, and records usage and request history. The asynchronous interface
supports concurrent worker calls. Per-agent client subclasses supply tier-specific
settings.

`ARGO_API_USER` identifies the configured Argo provider account. It is not a browser
login. Main, Query and Analysis read `ARGO_API_URL` when configured. Browser user
state does not choose an output directory or grant access to diagnostic data.
The optional [Anthropic adapter](general_db_query_engine/general_argo_engine_helpers/anthropic_argo_adapter.py)
translates the same engine calls for the benchmark bootstrap.

Models, token limits, iteration limits, time budgets, and compaction thresholds are
configuration values. Read the three linked config files in [README.md](README.md)
for the values in this checkout; documentation does not impose a second set of limits.

## Tools, validation and compaction

The main catalog classes are `MainCatalog`, `QueryL0Catalog`, `QueryL1Catalog`, the
L2 catalogs, and `AnalysisCatalog`. They register `ToolEntry` instances through the
shared [`AgentToolCatalog`](general_db_query_engine/general_tool_management_helpers/general_agent_tool_catalog/README.md).
The registry controls the callable surface and attaches validation and compaction
metadata. Tool-menu exposure can differ from the tools available in an agent's own loop.

The shared ReAct engine parses model tool calls, dispatches validated requests,
delivers tool results, and continues until an answer or runtime stopping condition.
The [hook layer](general_db_query_engine/general_hooks_management_helpers/README.md)
connects lifecycle events to time reminders, working-memory updates, history,
reference tracking, compaction, and post-answer evaluation.

Context compaction has several distinct responsibilities:

- Card and tool renderers reduce verbose structured responses deterministically.
- Agentic compaction summarises eligible tool results while preserving evidence.
- Working-memory and context hooks manage the material retained across turns.
- Post-answer evaluation checks claims and identifier metadata and constructs the
  answer summary. See [post-answer evaluation](general_db_query_engine/general_hooks_management_helpers/general_postans_eval_hooks/README.md).

Workflow Markdown contains prompts, tool descriptions, and response contracts.
The [shared parser](general_db_query_engine/general_subagent_skill_schema_and_parser/README.md)
validates these contracts; agent workflow modules consume the parsed results.
Canonical identifier and data-grounding checks remain scientific validation,
independent of browser access or user identity.

## Sessions and durable output

[`SessionManager`](general_db_query_engine/general_hooks_management_helpers/general_memory_management_tools_hooks_helpers/session_manager_output_storage.py)
creates or reopens session directories and tracks generated files. The active
session is context-local. The [delegation helpers](general_db_query_engine/general_subagent_delegation_helpers/README.md)
preserve the parent session while nested Query or Analysis work writes beneath it.

Default directories are declared directly by the owning config, UI, or runner:

| Caller | Default location, relative to workspace root |
|---|---|
| Main freeform API | `_output/Main/run_*` |
| Analysis freeform API | `_output/Analysis/run_*` |
| Query terminal UI | `_output/Query/run_*` |
| Query Python API | Caller supplies `session_dir` or `memory_path` |
| Per-agent benchmark | `_benchmark/<Agent>/test_run_*/Q<prompt_id>/` |

Main and Analysis benchmark runners pass explicit `session_dir` values to their
APIs. Query supplies its per-prompt memory path. Thus a custom `--output` contains
the full campaign, including session artifacts. No shared output-router module,
per-user bucket, or environment-based output-mode dispatch is required.

A session may contain result Markdown, chronological run history, reasoning and
reference statistics, structured event logs, working memory, child agent sessions,
and exported CSV/plot files. Actual files depend on the agent and executed tools.
Continuation rounds reuse the selected session and retain the appropriate prior context.

## Post-run workflow artifacts

After tracking is finalised, every completed root session calls
[`maybe_generate_workflow`](general_db_query_engine/general_posteval_helpers/compaction_funnels/api.py).
This generates workflow figures, tables and audits under `<session>/workflow/`.
Child sessions are represented in the root's delegation tree, so the automatic
hook skips separate generation for saved children. Rendering failures are reported
without changing the completed agent answer into a failure.

The [compaction-funnel package](general_db_query_engine/general_posteval_helpers/compaction_funnels/README.md)
uses saved evidence and logged arguments to reconstruct the workflow. Its legacy
log checks and scientific audits describe evidence completeness; they are not
user or debug-access gates.

## Validation and extension

Offline checks cover database paths, prompt schemas, identifier reconstruction,
grounding, search behavior, numerical tools, browser artifacts and session paths.
Live prompt benchmarks exercise the public APIs and require a configured provider.
Use the [shared benchmark runner reference](general_db_query_engine/general_DEBUG_test_runner_helpers/README.md)
and the [workspace test commands](../../README.md).

When extending an agent, update its catalog, workflow Markdown, and relevant
hooks together. Preserve explicit session ownership, canonical identifier
contracts, and the public result types. Numeric budgets belong in configuration;
artifact paths belong in their owning entrypoints. Validate changes with the
smallest relevant offline regression suite before using a live benchmark.
