# ThermoML Results Browser — Architecture

## System Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                     Flask app  (app.py)                          │
│                                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────────┐   │
│  │  Search   │  │  Papers  │  │  Agents  │  │ Analysis       │   │
│  │  /search  │  │ /paper/* │  │ /agents  │  │ workbench      │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └───────┬────────┘   │
│       │              │             │                │            │
│       ▼              ▼             ▼                ▼            │
│  ┌─────────────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │   SQLite index DB   │  │ agent_runner  │  │ adv_search_  │   │
│  │ ThermoML_index.db   │  │   .py         │  │ calc/        │   │
│  └─────────────────────┘  └──────┬───────┘  └──────┬───────┘   │
│                                  │                  │            │
│                   ┌──────────────┘         ┌────────┘            │
│                   ▼                        ▼                     │
│  ┌─────────────────────────────┐  ┌──────────────────────────┐  │
│  │ cannonical_id_alignment_    │  │ ThermoML_core_calc_tools │  │
│  │ search_agent/               │  │ (imported from agent     │  │
│  │  └─ 16 MCP tools           │  │  infrastructure)         │  │
│  │  └─ Argo ReAct engine      │  └──────────────────────────┘  │
│  │  └─ Hardcoded helpers      │                                 │
│  └─────────────────────────────┘                                │
└──────────────────────────────────────────────────────────────────┘
```

## Layers

### 1. Presentation — Jinja2 Templates

Jinja templates extend `base.html`; local JavaScript and page scripts render
agent output, charts, tables, and canonical-ID links. Bootstrap, chart libraries,
Markdown rendering, and mathematics use CDN assets.

### 2. Application and package boundaries

`app.py` owns database access, paper pages, raw JSON, and analysis endpoints.
Blueprints separate agent monitoring (`helpers/agent_routes.py`) and structured
and smart search (`helpers/search_routes.py`). Parser helpers turn raw ThermoML documents
into display data. Browser-local imports use the `ThermoML_results_browser`
package; its initializer makes the sibling `ThermoML_research_agent` importable.

The root `launch_thermoml_browser.py` creates a local threaded server, prints the
workspace and actual URL, and opens that URL. It falls back from the default port
to a free port, while an explicit occupied port fails. Windows exclusive socket
binding prevents two workspaces from accidentally sharing the same port.

Paths are anchored to source files. The index is at
`ThermoML_research_agent/card_databases_storage/ThermoML_index.db`. Source documents
come from `ThermoML_research_agent/ThermoML.v2020-09-30.db/thermoml_raw_corpus.db`,
which stores independently compressed JSON/XML payloads. SQLite readers enforce
read-only access. Raw JSON panels load lazily for every visitor.

### 3. Background Execution — agent_runner.py

`AgentRun` class wraps a single agent invocation:

- Runs in a background thread (threading)
- Generates a UUID `run_id` for status polling
- Keeps a bounded, sequence-numbered terminal buffer for reconnectable SSE
- Discovers session directory for result files
- Extracts working memory, result markdown, reasoning snapshots
- **Renders the post-answer JSON envelope at the read boundary**
  (`_render_postanswer_envelope`): the answer markdown is shown verbatim,
  followed by a "Post-answer analysis" section with core-claim bullets,
  confidence/status badges, sources as `GLOBlit | DOI | block` lines, and
  remaining fields in a collapsed JSON details block; fail-open for
  legacy flat result files
- Lists generated images and CSV data files
- Configurable time overrides
- Resolves shared freeform and benchmark roots as distinct history scopes

Public API:
- `start_run(question, agent_type, ...)` → run ID string
- `get_run(run_id)` → `AgentRun | None`
- `list_runs()`, `list_past_runs()`, `list_agent_runs()`
- `is_busy()` — thread-safety check

### 3a. Benchmark ZIP readers — helpers/benchmark_zip.py

Benchmark ZIPs are read-only collections under `_benchmark/<Agent>/`. `ZipPath`
provides directory traversal and member streams over a validated ZIP central
directory. Only metadata is cached; payloads are read from the archive when
requested, without extraction or filesystem aliases. Cache keys include archive
mtime and size. Unsafe, duplicate, or symlink members are rejected.

`agent_runner.py` discovers both ordinary folders and ZIP collections, resolves
session IDs and trace files, and retains the existing Main, Analysis, and Query
mode grouping. Result, history, memory, statistics, composition data, and workflow
readers share these paths. Artifact routes stream CSV data and serve image/workflow
bytes from memory. Existing freeforms can use the same read-only ZIP reader,
including legacy Main archives directly under `_output`. New shared freeform
runs continue to use ordinary `_output/<Agent>/run_*` folders. Archived and
ordinary sessions coexist; ordinary folders take precedence for duplicate names.

The specialized-tool page, plugin package, and its former API routes are removed.

### 4. Analysis Layer — adv_search_calc/

Two modules:

**`analysis_dispatcher.py`** — wraps four agent core calc tools for
browser consumption:
- `run_nonideality` — excess property computation + RK fit
- `run_rk_fitting` — BIC-based order selection, coefficient extraction
- `run_inspect` — raw block structure dump
- `run_pure_values` — pure-component extraction
- `classify_excess` — deviation classification helper
- `dispatch(tool, **kwargs)` — unified entry point

Lazy-imports numpy and agent modules on first call via `_ensure_core()`.
Includes `TOOL_DEFINITIONS` metadata list for UI rendering.

**`nonideality.py`** — zero-dependency (no numpy) fallback calculator.
Uses Gaussian elimination for RK fitting.  Auto-detects mole fraction,
volume, and viscosity columns.  Returns `AnalysisResult` dataclass.

### 5. Alignment Agent — cannonical_id_alignment_search_agent/

Full sub-agent for resolving free-text search queries to canonical
ThermoML index IDs:

| Sub-package | Role |
|-------------|------|
| `alignment_agent_api.py` | Public entry point: `alignment_agent_run()` |
| `alignment_agent_argo_config.py` | Model / prompt configuration |
| `alignment_agent_argo_engine/` | Argo ReAct LLM client |
| `alignment_agent_toolbox/` | 16 MCP tools (resolve, validate, fill blocks, finalize) |
| `alignment_agent_workflows/` | L0 orchestrator (multi-step plan) |
| `hardcoded_search_helpers/` | Deterministic search, validation, scoring |

---

## Data Flow

### Search Flow

```
User query → /search → SQL against ThermoML_index.db
                      → (optional) alignment agent resolves free-text
                      → Results rendered in search.html
```

### Analysis Flow

```
User selects paper → /analysis/search_papers → paper list
User picks block   → /analysis/paper_blocks  → block list
                   → /analysis/block_data    → columns + rows
User runs tool     → /analysis/run (POST)    → analysis_dispatcher.dispatch()
                   → Results + chart data returned as JSON
                   → Chart.js renders interactive plot
```

### Agent Flow

```
User enters question → /agents/launch (POST) → agent_runner.start_run()
                     → optional model override patches the selected agent config
                     → Background thread runs Main/Analysis/Query agent
                     → model config is restored when the run exits
                     → /agents/stream/<id> streams terminal + status over SSE
                     → full logs, reasoning, working memory, and API statistics
                     → final Result/History/Data/Images displayed in agents.html

History navigation → /agents/history?scope=user|benchmark
                   → paginated, source-scoped run discovery
                   → shared detail/CSV/image APIs retain the selected scope
```

---

## Shared output and access

`agent_runner.py` declares `_output/{Main,Query,Analysis}` and
`_benchmark/{Main,Query,Analysis}` directly beneath this checkout. Existing flat
`_output/run_*` Main sessions are included in freeform discovery. Benchmark
examples also support `Q<id>_run_<YYYYMMDD_HHMMSS>` with an optional microsecond
suffix. Valid current prompt IDs in these names take precedence over historical
trace IDs for grouping; the stored historical record is left intact. Legacy
`run_*` examples still use question-text matching. `scope=user`
retains its API spelling but identifies shared persistent history. There is no
output router, master-browser state, visitor account, or debug-access gate.
Provider settings come from the server environment. Benchmark history and file
containment remain separate data-integrity rules.

## External Dependencies

- **ThermoML_index.db** — pre-built SQLite index in the sibling research-agent data directory
- **NIST_ThermoML_agents** — agent infrastructure and core calculation tools (sibling research project)
- **Argo API** — configured backend for agentic alignment and Main/Query/Analysis runs
