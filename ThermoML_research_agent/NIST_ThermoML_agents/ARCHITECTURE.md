# NIST ThermoML Agents — System Architecture

> **Version**: 6.1  
> **Date**: 2026-04-09  
> **Scope**: Multi-agent system for querying, analysing, and editing the ThermoML card database  
> **Complements**: [Workspace architecture](../../MASTER_ARCHITECTURE.md) (data platform & card layer)

---

## 1. Overview

The NIST ThermoML agent system is a hierarchical, ReAct-loop-driven
agentic architecture that sits *on top* of the ThermoML card database
(described in the workspace architecture guide).  It enables natural-language
queries against 11,923 publications, 8,500+ compounds, and 2.7 M data
points — using a layered design that manages context windows without
hardcoded caps.

```
┌──────────────────────────────────────────────────────────────────┐
│  USER  (natural language question)                               │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌────────────────────────────────────────────────────────┐     │
│   │  L0 ORCHESTRATOR  (NIST_ThermoML_query_agent/)         │     │
│   │  • Owns Working Memory (protected ID catalog)          │     │
│   │  • Dispatches purpose+instruction to L1 workers        │     │
│   │  • auto-stores L1 results, thin-answer guard           │     │
│   │  • Makes ALL cross-reasoning decisions                 │     │
│   │  • 800s soft budget, 25 iteration cap                  │     │
│   └──────────────┬──────────────────┬───────────────────────┘     │
│                  │                  │                             │
│     ┌────────────▼──────┐  ┌───────▼────────────┐               │
│     │  L1 QUERY WORKER  │  │  L1 POSTPROCESS    │               │
│     │  12 iters, 240s   │  │  (not yet active)  │               │
│     │  11 search tools  │  │                    │               │
│     └────────┬──────────┘  └────────────────────┘               │
│              │                                                   │
│   ┌──────────▼────────────────────────────────────────────┐     │
│   │  L2 LEAF EVALUATORS  (parallel via asyncio.gather)    │     │
│   │  6 iters, 90s each                                    │     │
│   │  L2_comp · L2_meas · L2_ref · L2_prop                │     │
│   └───────────────────────────────────────────────────────┘     │
│                                                                  │
│   ┌────────────────────────────────────────────────────────┐     │
│   │  ANALYSIS AGENT  (NIST_ThermoML_analysis_agent/)       │     │
│   │  12 tools in 3 phases (resolve → discover → fit)       │     │
│   │  ReAct loop (30 iters, 1200s) + ToolResult subagents   │     │
│   │  SessionManager for output files (CSV, plots, topology) │     │
│   │  Returns AnalysisRunResult dataclass                    │     │
│   └────────────────────────────────────────────────────────┘     │
│                                                                  │
│   ┌────────────────────────────────────────────────────────┐     │
│   │  EDITING AGENT  (NIST_ThermoML_editing_agent/)         │     │
│   │  (Placeholder — future PDF/text→ThermoML ingest)       │     │
│   └────────────────────────────────────────────────────────┘     │
│                                                                  │
│   ┌────────────────────────────────────────────────────────┐     │
│   │  MAIN AGENT  (_NIST_ThermoML_main_agent/)              │     │
│   │  Master orchestrator routing to Query + Analysis        │     │
│   │  6 delegation tools + 2 tool-menu tools                 │     │
│   │  ReAct loop (40 iters, 2400s) + entity propagation      │     │
│   │  Returns MainRunResult dataclass                        │     │
│   └────────────────────────────────────────────────────────┘     │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│  SHARED INFRASTRUCTURE                                           │
│  • general_argo_engine_helpers/ — shared ReAct engine,           │
│      EngineConfig, ArgoClient, AnchorPoint (65 anchor types      │
│      + 5 agent-level), anchor() dispatch, singleton patching     │
│  • general_text_context_marker_catalog/ — ContextMarkerCatalog   │
│      (13 XML tag families), TagPair frozen dataclass             │
│  • general_hooks_management_helpers/ — parent for:               │
│    ├─ general_context_hooks/ — time budget, compaction, tracking,│
│    │    reasoning token capture, anchor catalogs, internal errors │
│    ├─ general_memory_management_tools_hooks_helpers/ —            │
│    │    WorkingMemory, SessionManager, 8 MCP tools,              │
│    │    tool-result instrumentation wrapper                       │
│    └─ general_tracking_hooks_output_helpers/ —                    │
│         output_writers, answer_cleaner                            │
│  • general_tool_management_helpers/ — AgentToolCatalog,          │
│      CompactorCatalog, ToolEntry, health checks                  │
│  • general_db_search_tool_registry/ — 27 auto-discovered tools   │
│  • general_subagent_delegation_helpers/ — SubagentSessionManager, │
│      build_full_question, extract_run_result, dispatch_parallel,  │
│      merge_subagent_tracking (shared by main + analysis agents)   │
│  • general_subagent_skill_schema_and_parser/ — workflow MD parser │
│  • general_ThermoML_db_csv_registry/ — DB path registry          │
└──────────────────────────────────────────────────────────────────┘
```

---

## 2. Core Design Patterns

### 2.1 Configuration Architecture (`EngineConfig` + Agent Subclasses)

The configuration system uses **dataclass inheritance** to share a common
shape across agents while keeping all settings in one file per agent.

```
EngineConfig (base, 26 fields, no defaults)
├── QueryAgentConfig(EngineConfig)     — ThermoML_query_argo_config.py
│     Step 1: 26 engine fields with defaults
│     Step 2: ~20 query-agent-only fields (L1/L2 budgets, compactors, verdict)
├── AnalysisAgentConfig(EngineConfig)  — ThermoML_analysis_argo_config.py
│     Step 1: 26 engine fields with defaults (higher iteration/time caps)
│     Step 2: ~25 analysis-agent-only fields (fitting, sessions, protected tools)
└── MainAgentConfig(EngineConfig)      — ThermoML_main_argo_config.py
      Step 1: 26 engine fields with defaults (highest caps: 40 iters, 2400s)
      Step 2: ~15 main-agent-only fields (subagent delegation, tool menu)
```

**Run-local config** — each agent's engine `__init__.py` calls
`load_default_config(AGENT_CONFIG)` once at import time (a no-op when a run
config is already active, so lazy sibling-agent imports mid-run never
clobber the running agent). Every runner is decorated with
`@with_engine_config(AGENT_CONFIG)`, which token-sets/resets the active
config `ContextVar`; the shared engine modules call `get_config()` to access
the active configuration without import-time circular dependencies.

**Lazy `__init__.py`** — `argo_engine_helpers/__init__.py` eagerly imports
only `EngineConfig`, `load_config`, `load_default_config`, `get_config`.
Heavyweight symbols (`ArgoClient`, `agent_turn`, etc.) are lazy-loaded via
`__getattr__` to avoid circular imports when agent config modules subclass
`EngineConfig`.

Consumer import pattern:
```python
from ..ThermoML_query_argo_config import AGENT_CONFIG as cfg
# then: cfg.MODEL, cfg.SUBAGENT_MAX_TOKENS, cfg.L1_MAX_ITERATIONS, etc.
```

### 2.2 Class-Based Tool Catalogs

Every agent layer uses a class-based **`AgentToolCatalog`** subclass
(`general_tool_management_helpers/general_agent_tool_catalog/`) to
register its tools with compaction metadata.

```
AgentToolCatalog (base)                 # agent_tool_catalog.py
├── QueryL0Catalog                     # query_agent_toolbox/tool_catalog.py
├── QueryL1Catalog                     # query_agent_workflows/L1_workers/
├── AnalysisCatalog                    # analysis_agent_toolbox/tool_catalog.py
├── MainCatalog                        # main_agent_toobox/tool_catalog.py
└── (each subclass registers its ToolEntry list)
```

Each registered `ToolEntry` carries:
- `fn` — callable
- `compactor_fn` / `condense_fn` / `ultra_condense_fn` — compaction tiers
- `skip_compactor` / `skip_subagent` — bypass flags
- `adaptive_condense` — tool handles condensation internally

**CompactorCatalog** (`agent_tool_compactor_hooks_catalog.py`) is an
auto-wiring registry for compactors, built via `@compacts` and
`@uses_compactors` decorators.

**Health checks** (`health_check_helper/`) run at agent startup to validate:
1. Every tool has a compactor (unless `skip_compactor=True`)
2. CompactorCatalog entries match ToolEntry compactors
3. Every tool in `agent_turn()` dict is registered in the catalog

### 2.3 Anchor-Point Architecture (`engine_hooks_anchors.py`)

The ReAct engine uses an **anchor-point protocol** to decouple the
pipeline control flow from hook implementations.  Every location in the
engine that edits, generates, or interacts with context is marked by an
**anchor point** — a named dispatch slot.

**Data structures** (`engine_hooks_anchors.py`):

| Type | Description |
|------|-------------|
| `AnchorPoint` | Frozen dataclass — `name` + `anchor_types: tuple[str, ...]` |
| `AnchorCollection` | Named mapping of `AnchorPoint`s declared by a catalog |
| `AgentAnchorCollection` | 5 agent-level lifecycle anchors (see below) |
| `HookBinding` | Pairs a callback with the anchor types it applies to |
| `AgentHookCollection` | Shared agent hook collection — holds `engine_hooks`, lifecycle callbacks, and `rebuild_engine_hooks()` method |

**65 anchor types in 4 domains + 5 agent-level lifecycle anchors:**

```
╔══════════════════════════╦═════╦══════════════════════════════════════════╗
║ Context (4 sets)         ║ 31  ║ PROMPT_ANCHOR_TYPES (8),                ║
║                          ║     ║ ANSWER_ANCHOR_TYPES (8),                ║
║                          ║     ║ TIME_BUDGET_ANCHOR_TYPES (5),           ║
║                          ║     ║ COMPACTION_ANCHOR_TYPES (10)            ║
╠══════════════════════════╬═════╬══════════════════════════════════════════╣
║ Memory (2 sets)          ║ 10  ║ WORKING_MEMORY_ANCHOR_TYPES (3),        ║
║                          ║     ║ MEMORY_APPEND_ANCHOR_TYPES (7)          ║
╠══════════════════════════╬═════╬══════════════════════════════════════════╣
║ Tool Operations (3 sets) ║ 19  ║ TOOL_EXEC_ANCHOR_TYPES (11),            ║
║                          ║     ║ TOOL_COMPACTION_ANCHOR_TYPES (7),        ║
║                          ║     ║ SUBAGENT_ANCHOR_TYPES (1)               ║
╠══════════════════════════╬═════╬══════════════════════════════════════════╣
║ Agent Lifecycle          ║  5  ║ AGENT_START_TRACKING,                    ║
║                          ║     ║ AGENT_FINALIZE_TRACKING,                 ║
║                          ║     ║ AGENT_RECORD_REFERENCES,                 ║
║                          ║     ║ AGENT_SAVE_FINAL_CONTEXT,                ║
║                          ║     ║ AGENT_RUN_VERDICT                        ║
╚══════════════════════════╩═════╩══════════════════════════════════════════╝
                                  Total: 70 anchor points
```

**Dispatch functions** (`engine_hooks_anchors.py`):

| Function | Signature | Behaviour |
|----------|-----------|-----------|
| `anchor()` | `(point, hooks, /, *args, **kw)` | Fire an `AnchorPoint` against compiled hooks; missing hooks silently skipped; exceptions caught, logged, and forwarded to `log_internal_error()` |
| `bind_hook()` | `(callback, *anchor_types, name=)` | Create `HookBinding` pairing callback to anchor types |
| `compile_hooks()` | `(bindings)` | Convert `HookBinding` iterable → dispatch dict used by `anchor()` |
| `build_agent_lifecycle_bindings()` | `(history=, stats=, …)` | Build the 5 lifecycle `HookBinding`s for any agent |

**Wiring:** Each agent's `hook_catalog.py` subclasses `AgentHookCollection`,
overrides `build_engine_hooks()` to return per-domain `HookBinding`s, and
calls `compile_hooks()` in `__post_init__`.  The orchestrator passes the
compiled `engine_hooks` dict to `agent_turn(hooks=…)`.

**Three catalog modules** partition the 57 per-domain types:

| Catalog | Location | Types |
|---------|----------|-------|
| Context Hooks | `general_context_hooks/_context_hooks_anchors_catalog.py` | 31 |
| Memory Hooks | `general_memory_management_tools_hooks_helpers/_memory_hooks_anchors_catalog.py` | 10 |
| Tool Hooks | `general_tool_management_helpers/_tool_hooks_anchors_catalog.py` | 19 |

The 5 agent-level lifecycle anchors live in `engine_hooks_anchors.py`
itself and are wired via `build_agent_lifecycle_bindings()`.

### 2.3a Pre-Execution Validation Chain

Tool calls pass through a **two-level anchor chain** before execution:

1. `SYNC_BATCH_PRE_VALIDATE` — fired once per tool-call batch in
   `react_loop.py`; forwards the compiled `engine_hooks` dict to
   `validate_batch(hooks=engine_hooks)`.
2. `SYNC_TOOL_GUIDANCE_CHECK` — fired once per individual tool call
   inside `validate_batch()`; dispatches to any `PreExecutionGuidance`
   hooks bound to this anchor.

`PreExecutionGuidance` (in `general_tool_options_interactive_hooks/`)
is a frozen dataclass with `target_tools`, `required_params`, and
`context_params`.  When called via anchor dispatch, it:
- Returns `None` if the tool is not in `target_tools` (skip).
- Auto-fills missing `required_params` from `context_params` context.
- Returns `""` on success (auto-filled) or a non-empty block message
  if required parameters are still missing after fill attempts.

If any guidance hook returns a non-empty string, the tool call is
blocked and the guidance message is injected into the conversation
via `SYNC_TOOL_VALIDATION_BLOCKED`.

All agents (Analysis, Query, Main) wire `batch_validator` in their
`hook_catalog.py` → `SYNC_BATCH_PRE_VALIDATE` binding.  Agent-specific
guidance hooks (e.g. `FittingVariableGuidance` in Analysis) are bound
to `SYNC_TOOL_GUIDANCE_CHECK`.

**Usage in `react_loop.py`:**
```python
from .engine_hooks_anchors import anchor as _anchor, AnchorPoint

# Fire a catalog-defined anchor
_anchor(FLAT_PROMPT_BUILD, _hooks, iteration=iter, prompt_chars=len(flat))

# Agent-level lifecycle anchor (called by orchestrator, not react_loop)
_anchor(AGENT_START_TRACKING, hooks, agent="query", prompt=question, ...)
```

### 2.3b Context Markers (`general_text_context_marker_catalog/`)

Separate from anchor points, the system uses **XML-style text markers**
embedded in the flat prompt and LLM responses.  These are structural
delimiters parsed by regex — they mark boundaries in text, not code.

| TagPair Family | Open Tag | Purpose |
|----------------|----------|---------|
| `tool_call` | `<tool_call>` | Wraps LLM tool invocations |
| `tool_result` | `<tool_result>` | Wraps tool execution results |
| `reasoning` | `<reasoning>` | Extended thinking / chain-of-thought |
| `answer` | `<answer>` | Final answer boundary |
| `compress` | `<compress>` | Agent-initiated compaction request |
| `compaction_guidance` | `<compaction_guidance>` | Mid-turn guidance prompt |
| `memory` | `<memory>` | Working memory snapshot |
| `system_prompt` | `<system_prompt>` | System prompt boundary |
| + 5 more | … | `wait`, `summary`, `compaction_reminder`, `compact_note`, `retry` |

**Data structure:** `ContextMarkerCatalog` frozen dataclass with `TagPair`
open/close strings + compiled regexes. Module-level singleton `MARKERS`.
Only the `MARKERS` catalog is public; retired flat marker aliases are absent.

**Relationship to anchors:** Context markers handle **data format** (what
the LLM sees and produces as text). Anchors handle **code behaviour**
(what Python does at each pipeline stage). They are orthogonal systems
that collaborate at each pipeline step.

### 2.3c Reasoning Token Tracking

The `reasoning_token_tracking_hooks.py` module captures extended-thinking
tokens from LLM responses via the `ON_REASONING` anchor. Reasoning tokens
(content inside `<reasoning>` markers) are stripped from agent responses
before tool parsing but logged to `reasoning_tokens_stripped.md` in the
session output directory for diagnostics and cost tracking.

### 2.12 Shared Subagent Delegation Helpers (`general_subagent_delegation_helpers/`)

Both the **main agent** and the **analysis agent** delegate work to
sibling agents (query, analysis).  To eliminate duplication, five
reusable primitives live in `general_db_query_engine/general_subagent_delegation_helpers/`:

| Export | Purpose |
|--------|---------|
| `SubagentSessionManager` | Dependency-injection wrapper that creates nested session directories (`<session>/query_runs/`, etc.) without coupling to a specific agent's session singleton |
| `build_full_question` | Assembles a structured question string from `question`, `purpose`, and `tasks` fields |
| `extract_run_result` | Normalises any agent's return value into a standardised `dict` with `answer`, `entity_summary`, `session_dir` keys |
| `dispatch_parallel` | Spawns multiple subagent calls via `ThreadPoolExecutor`, collects results, handles per-call errors |
| `merge_subagent_tracking` | Copies / appends subagent tracking MDs (`run_history.md`, `reference_stats.md`, `reasoning_tokens_stripped.md`) into the parent session directory |

**Consumers:**
- `_NIST_ThermoML_main_agent/main_agent_toobox/subagent_delegation_tools.py`
  — `run_query_agent`, `run_analysis_agent`, `run_parallel_subagents`
- `NIST_ThermoML_analysis_agent/analysis_agent_toolbox/sibling_agent_delegation_tools/query_agent_tool.py`
  — `run_query_agent_sibling`, `run_parallel_query_siblings`

All five helpers are stateless functions (or lightweight DI wrappers)
with no LLM dependency.

### 2.4 ArgoClient Dataclass

Every agent layer instantiates its own `ArgoClient` with layer-specific
parameters (model, temperature, max_tokens, timeout).  Defined in
`argo_engine_helpers/argo_client_caller.py`.

```python
@dataclass
class ArgoClient:
    model: str        # e.g. "claudeopus46"
    temperature: float
    max_tokens: int
    timeout: int
    ...
    def call(self, prompt, system_prompt, **kw) -> str: ...
    async def acall(self, prompt, system_prompt) -> str: ...
```

Convenience constructors: `ArgoClient.for_l1()`, `.for_l2()`, `.for_verdict()`.

### 2.5 ReAct Agent Loop (`agent_turn`)

All layers share the same ReAct engine in `argo_engine_helpers/react_loop.py`:

```
while iteration < max_iterations and elapsed < budget:
    response = client.call(flat_prompt, system_prompt)
    if <tool_call> in response:
        parse → execute tool → append result to memory
        if context_chars > threshold:
            compact_memory(memory, argo_fn)   # LLM-driven 3-step
    else:
        final_answer = response
        break
    inject time_warning at 65% / 85% / 95% of budget
```

Key features:
- **Tool-call format**: `<tool_call>{"name": "...", "arguments": {...}}</tool_call>`
- **Exact parameter contract**: undeclared names and wrong JSON types produce refinement errors; no aliases or coercion
- **Result contract**: registered deterministic compactors and the mandatory
  agentic compaction stage control context size; raw tool results are never
  silently head/tail-truncated
- **Soft time warnings**: 3 chances to wrap up at 65%, 85%, 95% of budget

### 2.6 LLM-Driven Context Management (No Hardcoded Caps)

Adapted from the SRD46_db_subagent and Speciation_calc_subagent:

1. **Agent-initiated** — The main agent emits `<compress>` tags when it
   judges that old results are no longer needed in full detail.
2. **3-step LLM cycle**: SELECT → COMPRESS → VALIDATE.  A sub-agent
   does the summarisation; the validator replies ACCEPT, RETRY, or SKIP.
   RETRY triggers an immediate re-compression (up to `MAX_IMMEDIATE_RETRY`
   times); SKIP defers the candidate to the next cycle.
3. **Failure contract** — If a required compaction call or validation fails,
   the error propagates; the engine does not substitute an unvalidated or
   truncated representation.
4. **Protected sections** — The ID Catalog in Working Memory is never
   compacted.

### 2.7 Workflow Skill Markdowns

Each agent layer is defined by a `.md` file with YAML frontmatter +
structured sections:

```yaml
---
agent_id: L1_query
layer: 1
model: claudeopus46
temperature: 0.3
max_tokens: 6000
---
# System Prompt
...
# Tools
## search_tools
- search_blocks(...)
...
# Prompt Template
## Purpose
{{purpose}}
...
# Response JSON Schema
```json
{...}
```
# Phases
## phase_1: resolve_ids
...
```

The `subworkflow_skill_templates/subworkflow_parser.py` reads these into
a structured dict; `render_prompt()` substitutes template variables.

### 2.8 Working Memory (File-Backed Structured Markdown)

```
# Working Memory

## ID Catalog (PROTECTED)
| type | global_id | canonical_id | name |
|------|-----------|--------------|------|
| comp | GLOBcomp_12 | hexane | hexane |

## History (append-only, compactable)
- [L1-query] searched blocks for hexane+ethanol VLE → 4 blocks found

## Results (indexed, compactable)
### result_1
...
```

8 MCP tool functions wrap the `WorkingMemory` class: `memory_read`,
`memory_append_history`, `memory_add_result`, `memory_catalog_add`,
`memory_catalog_remove`, `memory_catalog_list`, `memory_compact`, `memory_reset`.

Thread safety: `memory_management_MCP_tools.py` uses `threading.local()`
for its internal state, so each thread in a parallel test run gets its
own `WorkingMemory` instance.

### 2.9 Internal Error Logging

Non-fatal errors are collected during a run and rendered as a batch
post-mortem section in `run_history.md` rather than crashing the pipeline.

**Data structure** (`history_tracking_hooks.py`):

```python
@dataclass
class _InternalError:
    timestamp: str
    source: str       # "react_loop", "engine_hooks", "stats_hooks"
    error_type: str   # "json_fast_path", "anchor_callback", …
    tool_name: str
    message: str
    context_preview: str  # first 500 chars of raw data
```

**API:** `history_recorder.log_internal_error(source, error_type, tool_name, message, context_preview)` — appends to the `internal_errors` list.  
**Call-sites:**
1. `react_loop.py` — JSON fast-path guard (malformed tool result)
2. `engine_hooks_anchors.py` — `anchor()` exception handler
3. `stats_references_tracking_hooks.py` — polymorphic summary handling

**Rendering:** If `internal_errors` is non-empty, `run_history.md` appends
an "Internal Errors" table after the event log with timestamp, source,
tool_name, and message columns.

### 2.10 Singleton Patching Pattern

The shared history recorder is a module-level singleton
(`history_tracking_hooks.history_recorder`).  When a multi-agent session
starts, the active agent's recorder must receive `log_internal_error()`
calls from shared code (react_loop, engine_hooks) that imports the
singleton at module load time.

**Solution:** `_start_tracking()` in `engine_hooks_anchors.py` patches
`_hr_mod.history_recorder = history` where `_hr_mod` is the
`history_tracking_hooks` module imported at the top of the file.  This
redirects all shared-layer error logging to the currently-active agent's
recorder.

```
import history_tracking_hooks as _hr_mod   # module reference (not symbol)

def _start_tracking(*, history, ...):
    _hr_mod.history_recorder = history     # patch singleton
```

The same pattern is used for `StatsRecorder` and `ReasoningTokenTracker`
via their `set_active_recorder()` / `clear_active_recorder()` functions.

### 2.11 Tool-Result Instrumentation Wrapper

The analysis and main agents share a `make_instrumented_wrapper()` factory
(`memory_tool_result_instrumentation_helper.py`) that wraps each tool
function to automatically:

1. Record the tool result in working memory via `record_tool_result()`
2. Record history text via `record_tool_history()`
3. Pass the raw result dict to the engine for reference tracking

**Result shape handling:**

| Tool returns | What WM receives |
|--------------|-------------------|
| `str` (JSON-parseable) | `{**parsed_dict, "text": original_string}` |
| `str` (not JSON) | `{"text": original_string}` |
| `dict` | The dict as-is |

**No double-counting:** The wrapper does NOT fire `AGENT_RECORD_REFERENCES`.
That anchor fires once per tool call from `react_loop.py` only, using the
JSON fast-path guard to skip non-JSON results.

---

## 3. Module Map

### 3.0 Shared Engine (`general_argo_engine_helpers/`)

| Module | Purpose |
|--------|---------|
| `engine_config.py` | `EngineConfig` base dataclass (26 fields, no defaults) + `with_engine_config()` run decorator, `load_default_config()` guarded import-time default, `load_config()`/`get_config()` |
| `engine_hooks_anchors.py` | **`AnchorPoint`**, `AnchorCollection`, `AgentAnchorCollection` (5 lifecycle anchors), `AgentHookCollection`, `HookBinding`, `bind_hook()`, `compile_hooks()`, `build_agent_lifecycle_bindings()`, **`anchor()`** dispatch with `log_internal_error()`, `EMPTY_HOOKS` |
| `__init__.py` | Eager export of `EngineConfig`/`load_config`/`get_config`/`AnchorPoint`/`anchor`; lazy `__getattr__` for `ArgoClient`, `agent_turn`, etc. |
| `argo_client_caller.py` | `ArgoClient` dataclass — sync `call()` + async `acall()`; factory methods read `get_config()` |
| `react_loop.py` | `agent_turn()` — synchronous ReAct loop; fires anchor points; JSON fast-path guard for `AGENT_RECORD_REFERENCES`; module-level `import history_tracking_hooks as _hr_mod` for error routing |
| `react_loop_async.py` | `async_agent_turn()` — async variant with matching anchors |
| `_argo_engine_entry_point.py` | Re-exports for convenient imports (also used by lazy `__init__`) |

| Sub-directory | Module | Purpose |
|---------------|--------|---------|
| `engine_react_helpers/` | `react_helpers.py` | Exact argument validation and `AgentTurnResult` |
| | `tool_call_parser.py` | Exact `<tool_call>` JSON extraction; rejects bare JSON, Python-call syntax, repairs, and extra keys |
| `engine_tool_interface_helpers/` | `tool_menu_agent_interface.py` | Tool menu registration interface |
| | `argo_agent_terminal_ui.py` | Shared terminal UI base class |
| `engine_async_helpers/` | `async_runner.py` | `fan_out()` + `run_workflow()` for parallel dispatch |

### 3.0b Context Markers (`general_text_context_marker_catalog/`)

| Module | Purpose |
|--------|---------|
| `context_markers.py` | `TagPair` and `ContextMarkerCatalog` frozen dataclasses plus the strict module-level `MARKERS` singleton |
| `__init__.py` | Re-exports all symbols from `context_markers.py` |

### 3.1 Shared Tool Management (`general_tool_management_helpers/`)

| Sub-package | Module | Purpose |
|-------------|--------|---------|
| `general_agent_tool_catalog/` | `tool_entry.py` | `ToolEntry` frozen dataclass — per-tool compaction metadata |
| | `agent_tool_catalog.py` | `AgentToolCatalog` base class — tool registration, lookup, wrapped-tools dict |
| | `agent_tool_compactor_hooks_catalog.py` | `CompactorCatalog`, `CompactorEntry`, `@compacts`/`@uses_compactors` decorators |
| | `health_check_helper/` | `run_health_check()`, `CatalogHealthCheckError` — startup validation |
| `general_tool_results_compactor_agentic_hooks/` | `_search_tool_results_compact_subagent.py` | `ToolResult`, `ToolResultCompactor`, `call_tool_subagent()` — shared KEEP/DISCARD LLM subagent |
| *(root)* | `_tool_hooks_anchors_catalog.py` | Tool anchor type sets: `TOOL_EXEC_ANCHOR_TYPES` (11), `TOOL_COMPACTION_ANCHOR_TYPES` (7), `SUBAGENT_ANCHOR_TYPES` (1) — 19 types |
| `general_tool_options_interactive_hooks/` | `_pre_execution_guidance.py` | `PreExecutionGuidance` base dataclass — anchor-compatible pre-execution guidance hook. Filters by `target_tools`, auto-fills `required_params` / `context_params`, returns block messages via `block_msg()`. Bound to `SYNC_TOOL_GUIDANCE_CHECK`. |
| `general_tool_menu_tools/` | *(empty)* | Reserved for future tool-menu utilities |

### 3.2 Query Agent (`NIST_ThermoML_query_agent/`)

| Sub-directory | Module | Purpose |
|---------------|--------|---------|
| *(root)* | `ThermoML_query_api.py` | **Public API** — `ThermoML_query_run()` and `ThermoML_query_hardcoded_L0_wf_run()` |
| | `ThermoML_query_argo_config.py` | `QueryAgentConfig(EngineConfig)` — all query-agent settings |
| `query_agent_argo_engine/` | `argo_client.py` | `QueryClient` factory: `.for_l0()`, `.for_l1()`, `.for_l2()`, `.for_verdict()` |
| | `query_agent_terminal_ui.py` | Interactive CLI REPL loop |
| `query_agent_toolbox/` | `tool_catalog.py` | `QueryL0Catalog(AgentToolCatalog)` — memory tools + `L0_TOOL_CATALOG` flat dict |
| `query_agent_context_hooks/` | `hook_catalog.py` | **Single entry point** for all query hooks (re-exports 5 categories below) |
| `…/compactor_hooks/` | `tool_result_compactor.py` | `QueryToolResultCompactor` — hardcoded dict→md + KEEP/DISCARD subagent |
| | `context_stage_compaction.py` | `QueryStageCompactor` — deterministic stage-level compaction |
| `…/interactive_hooks/` | `interactive_compactor.py` | `QueryInteractiveCompactor` — LLM-driven 3-step context compaction |
| `…/memory_hooks/` | `working_memory_hooks.py` | `QueryWorkingMemory`, `init_working_memory()`, `make_wm_loader()` |
| | `l1_autosave_hooks.py` | `L1AutoSaver` — wraps L1 dispatch with auto-persist to WM |
| | `thin_answer_guard.py` | `is_thin_answer()`, `force_data_presentation()` — post-loop quality check |
| `…/tracking_hooks/` | `history_hooks.py` | `QueryHistoryRecorder` → `run_history.md` |
| | `stats_hooks.py` | `QueryStatsRecorder` → `reference_stats.md` |
| | `time_budget_hooks.py` | `QueryTimeBudgetTracker` — 65%/85%/95% time warnings |
| `…/verdict_hooks/` | `postjob_verdict.py` | `QueryVerdictRunner`, `run_verdict`, `save_final_context` |
| `query_agent_workflows/` | `L0_orchestrator/orchestrator.py` | Entry point: `run()` + `hardcoded_L0_wf_run()` |
| | `L0_orchestrator/L0_orchestrator_workflow.md` | L0 system prompt, phases, output schema |
| | `L1_workers/l1_query_dispatcher.py` | Builds L1 tool registry, launches L1 `agent_turn` |
| | `L1_workers/L1_query_workflow.md` | L1 system prompt, 4 phases, tool catalog |
| | `L2_leaf_evaluators/l2_dispatchers.py` | 4 dispatch functions for parallel L2 calls |
| | `L2_leaf_evaluators/L2_*_workflow.md` | Per-evaluator system prompts + tool groups |
| | `_subworkflow_md_parser/subworkflow_parser.py` | Parses workflow `.md` → structured dict |
| `query_agent_heath_check_helpers/` | *(empty)* | Reserved for agent-specific health checks |
| `_DEBUG_script/` | `run_tests.py` | Unified test runner (sequential + parallel with rate limiter) |

### 3.3 Analysis Agent (`NIST_ThermoML_analysis_agent/`)

| Sub-directory | Module | Purpose |
|---------------|--------|---------|
| *(root)* | `ThermoML_analysis_api.py` | **Public API** — `ThermoML_analysis_run()` |
| | `ThermoML_analysis_argo_config.py` | `AnalysisAgentConfig(EngineConfig)` — all analysis settings |
| `analysis_agent_argo_engine/` | `argo_client.py` | `AnalysisClient` factory: `.for_l0()`, `.for_l1_data()`, `.for_l1_fit()`, `.for_verdict()` |
| | `analysis_agent_terminal_ui.py` | Interactive CLI REPL loop |
| `analysis_agent_toolbox/` | `tool_catalog.py` | `AnalysisCatalog(AgentToolCatalog)` — 10 tools + `TOOL_CATALOG` flat dict |
| | `_imports.py` | Shared path setup + csv_io/fitting imports |
| | `query_delegation_tools.py` | `query_thermoml`, `query_thermoml_parallel` (direct L1 dispatch) |
| `sibling_agent_delegation_tools/` | `query_agent_tool.py` | `run_query_agent`, `run_query_agents_parallel` — full L0 query-agent delegation via shared `general_subagent_delegation_helpers` |
| | `hardcoded_data_tools.py` | `inspect_block`, `get_pure_values` (deterministic) |
| | `fitting_tools.py` | `fit_block` (unified: auto-detects single/multi-property/by-temperature modes), `fit_multi_system`, etc.; Arrhenius back-transform + `fit_y_label` for excess-property CSV columns |
| | `resolve_tools.py` | strict ID/name resolution helpers |
| | `discovery_tools.py` | `query_system_summary`, `query_blocks`, etc. |
| `analysis_agent_context_hooks/` | `hook_catalog.py` | **Single entry point** for all analysis hooks; binds `FittingVariableGuidance` to `SYNC_TOOL_GUIDANCE_CHECK` |
| `…/compactor_hooks/` | `tool_result_compactor.py` | `AnalysisToolResultCompactor` |
| | `context_stage_compaction.py` | `AnalysisStageCompactor` |
| | `_tool_compactors.py` | 13 `compact_*()` markdown generators |
| `…/interactive_hooks/` | `interactive_compactor.py` | `AnalysisInteractiveCompactor` |
| | `fitting_variable_guidance.py` | `FittingVariableGuidance(PreExecutionGuidance)` — auto-fills native `x_vars`, `y_props`, and `x_vars_constrained` for `fit_block` |
| `…/memory_hooks/` | `working_memory_hooks.py` | `AnalysisWorkingMemory` — tracks resolved IDs, blocks, fits; `_format_l1_block()` converts L1 JSON to compact markdown; `_parse_parallel_sections()` splits parallel sub-results |
| `…/tracking_hooks/` | `history_hooks.py`, `stats_hooks.py`, `time_budget_hooks.py` | Analysis-specific recorders |
| `…/verdict_hooks/` | `postjob_verdict.py` | Post-job quality review |
| `analysis_agent_workflows/` | `L0_orchestrator/orchestrator.py` | `run()` + `AnalysisRunResult` |
| | `L0_orchestrator/L0_analysis_workflow.md` | L0 system prompt + phases |
| | `L1_workers/l1_query_delegation.py` | `dispatch_query()` → query agent's L1 |
| | `_subworkflow_md_parser/subworkflow_parser.py` | Parses workflow `.md` → structured dict |
| `analysis_agent_heath_check_helpers/` | *(empty)* | Reserved for agent-specific health checks |
| `ThermoML_core_calc_tools/` | See §7 in analysis ARCHITECTURE.md | Pure-math / I/O (no LLM) |

### 3.3b Main Agent (`_NIST_ThermoML_main_agent/`)

| Sub-directory | Module | Purpose |
|---------------|--------|---------|  
| *(root)* | `ThermoML_main_api.py` | **Public API** — `ThermoML_main_run()` → `MainRunResult` |
| | `ThermoML_main_argo_config.py` | `MainAgentConfig(EngineConfig)` — 40 max iters, 2400s budget, no protected tools |
| `main_agent_argo_engine/` | `argo_client.py` | `MainClient(ArgoClient)` with `.for_l0()` factory |
| | `main_agent_terminal_ui.py` | Interactive terminal UI with multi-round continuation |
| `main_agent_toobox/` | `tool_catalog.py` | `MainCatalog(AgentToolCatalog)` — delegation + menu tools |
| | `subagent_delegation_tools.py` | `run_query_agent()`, `run_analysis_agent()`, `run_parallel_subagents()` via shared `general_subagent_delegation_helpers` (`SubagentSessionManager`, `build_full_question`, `extract_run_result`, `dispatch_parallel`, `merge_subagent_tracking`); `_extract_query_entity_summary()` for entity propagation |
| | `tool_menu/menu_tools.py` | `browse_subagent_tools()`, `run_subagent_tool()` — direct subagent tool discovery/execution |
| | `tool_menu/_registry_builder.py` | Lazy `ToolMenuRegistry` tree from query/analysis agent tools |
| `main_agent_context_hooks/` | `hook_catalog.py` | Central re-export hub + module-level singletons |
| `…/compactor_hooks/` | `tool_result_compactor.py` | Hardcoded dict→markdown + KEEP/DISCARD via MainClient LLM |
| | `_tool_compactors.py` | `@compacts()` for `run_query_agent` and `run_analysis_agent` results |
| | `_menu_batch_summary_hook.py` | Aggregates parallel `run_subagent_tool` batch results |
| `…/interactive_hooks/` | `interactive_compactor.py` | 3-step LLM compactor (no protected tools) |
| `…/memory_hooks/` | `working_memory_hooks.py` | `MainWorkingMemory` — records full query/analysis/parallel child results (`### Query/Analysis Agent Results` sections); entity counter propagation from subagent results |
| `…/tracking_hooks/` | `history_hooks.py`, `stats_hooks.py`, `reasoning_hooks.py`, `time_budget_hooks.py` | Passthrough recorders inheriting shared base |
| `…/verdict_hooks/` | `postjob_verdict.py` | Verifies subagent dispatch strategy + scientific accuracy |
| `main_agent_workflows/` | `L0_orchestrator/orchestrator.py` | Main entry point: builds tools, runs ReAct loop via `agent_turn()` |
| | `L0_orchestrator/L0_main_workflow.md` | L0 system prompt + phases |
| | `_subworkflow_md_parser/subworkflow_parser.py` | Thin wrapper re-exporting shared parser |
| `_DEBUG_script/` | `run_tests.py` | Test runner wrapping shared test helpers |

### 3.4 Shared Context Hooks (`general_hooks_management_helpers/general_context_hooks/`)

Cross-agent hooks shared by all agents.  Each hook is a passive observer
or utility — agents never see them directly.

| Module | Purpose |
|--------|---------|
| `time_budget_reminder_hooks.py` | `TimeBudgetTracker` — injects progressive `[TIME WARNING]` at 65%/85%/95% of budget |
| `self_compactor_interactive_hooks.py` | Shared 3-step LLM compaction engine (SELECT → COMPRESS → VALIDATE) |
| `context_cleanup_compactor_hooks.py` | Context cleanup and garbage collection hooks |
| `history_tracking_hooks.py` | `HistoryRecorder` singleton — chronological event log → `run_history.md`; `_InternalError` dataclass + `log_internal_error()` + internal errors rendering |
| `stats_references_tracking_hooks.py` | `StatsRecorder` singleton — quantitative stats & data complexity → `reference_stats.md`; polymorphic summary handling (`str` / `dict` results via `isinstance` guards); strictly passive — all `log_*` methods `@_passive`-wrapped, internal anomalies demoted to a non-fatal report section instead of raising into the loop |
| `reasoning_token_tracking_hooks.py` | `ReasoningTokenTracker` — captures `<reasoning>` tokens via `ON_REASONING` anchor → `reasoning_tokens_stripped.md` |
| `_context_hooks_anchors_catalog.py` | Anchor type sets: `PROMPT_` (8), `ANSWER_` (8), `TIME_BUDGET_` (5), `COMPACTION_ANCHOR_TYPES` (10) — 31 types |
| `postjob_verdict_hooks.py` | *(placeholder — reserved for verdict telemetry)* |

The shared compactor is consumed by thin agent-specific wrappers in each
agent's `interactive_hooks/interactive_compactor.py`, which inject the
agent's own `cfg` module and protected-tool sets.

### 3.5 Memory Management (`general_hooks_management_helpers/general_memory_management_tools_hooks_helpers/`)

| Module | Purpose |
|--------|---------|
| `general_memory_hooks.py` | `BaseWorkingMemory` abstract base class — common WM interface |
| `memory_local_storage_io.py` | `WorkingMemory` class — file-backed structured markdown |
| `memory_management_MCP_tools.py` | 8 MCP tool wrappers callable from agent loops |
| `memory_merger_helpers_and_agent.py` | Memory merger utilities for cross-session consolidation |
| `session_manager_output_storage.py` | `SessionManager` — output directory structure & file catalog |
| `memory_tool_result_instrumentation_helper.py` | `make_instrumented_wrapper()` — wraps tool functions for automatic WM recording + reference tracking (used by analysis + main agents; see §2.11) |
| `entity_catalog_helpers.py` | Canonical entity ID resolution utilities |
| `_memory_hooks_anchors_catalog.py` | Memory anchor type sets: `WORKING_MEMORY_ANCHOR_TYPES` (3), `MEMORY_APPEND_ANCHOR_TYPES` (7) — 10 types |

Thread safety: `memory_management_MCP_tools.py` uses `threading.local()`
for its internal state.

### 3.5b Output Writers (`general_hooks_management_helpers/general_tracking_hooks_output_helpers/`)

| Module | Purpose |
|--------|---------|
| `output_writers.py` | `write_test_summary()`, `write_json_trace()` — test-run output generators |
| `answer_cleaner.py` | `clean_answer()` — strips context markers from final answer text |

### 3.6 Search Tool Registry (`general_db_search_tool_registry/`)

| Module | Purpose |
|--------|---------|
| `db_search_tool_registry.py` | Auto-discovers 27 search tools across 4 categories (basic, block-centric, comp-centric, measurement-centric) |

### 3.7 Other Shared Packages

| Package | Purpose |
|---------|---------|
| `general_subagent_delegation_helpers/` | Shared primitives for cross-agent delegation: `SubagentSessionManager` (DI session nesting), `build_full_question` (structured questions), `extract_run_result` (standardised result dicts), `dispatch_parallel` (parallel execution via `ThreadPoolExecutor`), `merge_subagent_tracking` (tracking MD combination). Used by both main and analysis agents. |
| `general_subagent_skill_schema_and_parser/` | Workflow `.md` parser (`subworkflow_md_parser.py`), tool-description generators (`subworkflow_md_tool_descriptions.py`) |
| `general_ThermoML_db_csv_registry/` | Central registry of DB/CSV paths (`ThermoML_db_csv_registry.py`) |
| `general_text_context_marker_catalog/` | Strict centralized `ContextMarkerCatalog` (13 XML tag families) + `TagPair` frozen dataclass |
| `general_hooks_management_helpers/` | Parent directory for context hooks, memory management, and output writers (all child packages listed above) |
| `general_DEBUG_test_runner_helpers/` | Shared test-runner infrastructure (the real entry points are agent API files, not test runners) |

---

## 4. Data Flow

### 4.1 Query Agent Flow

```
User Question
    │
    ▼
L0 orchestrator.run(question)
    │
    ├─ Initialises WorkingMemory
    ├─ Builds tool registry:
    │     memory_* → MCP tools
    │     L1_query → dispatch_l1_query
    │
    ├─ agent_turn(client_L0, system_prompt_L0, tools, ...)
    │     │
    │     ├─ LLM decides: call L1_query(purpose, instruction, id_catalog)
    │     │     │
    │     │     ▼
    │     │  dispatch_l1_query(...)
    │     │     │
    │     │     ├─ resolve IDs via _id_alignment_search
    │     │     ├─ search_system_summary / search_blocks / search_references
    │     │     ├─ (optional) spawn L2 evaluators in parallel
    │     │     │     ├─ dispatch_l2_comp_eval(...)
    │     │     │     ├─ dispatch_l2_meas_eval(...)
    │     │     │     ├─ dispatch_l2_ref_eval(...)
    │     │     │     └─ dispatch_l2_prop_eval(...)
    │     │     └─ Returns structured JSON summary
    │     │
    │     ├─ L1AutoSaver stores result + history in memory
    │     │
    │     ├─ LLM reads stored results → formulates answer
    │     │
    │     └─ Thin-answer guard: if chatbot-style, forces data presentation
    │
    └─ Returns AgentTurnResult(answer, history, memory_snapshot)
```

### 4.2 Analysis Agent Flow

```
User Question (e.g. "estimate viscosity of DMF-Water-MeOH")
    │
    ▼
analysis ui.run(question) → AnalysisRunResult
    │
    ├─ init_session() → SessionManager (output dir, data/, plots/)
    │
    ├─ Phase 0: Planning
    │     ├─ resolve_compounds(names) → canonical `GLOBcomp_N` IDs
    │     └─ resolve_properties(names) → canonical `GLOBprop_N` IDs
    │
    ├─ Phase 1: Data Retrieval
    │     ├─ query_system_summary(compounds) → availability overview
    │     ├─ query_blocks(compounds, properties) → candidate blocks
    │     ├─ inspect_block(doi, block_number) → column map + ranges
    │     │     └─ extract_block_arrays() → BlockData
    │     │     └─ identify_columns() → ColumnMatch
    │     ├─ get_pure_values(doi, block_number, property) → pure endpoint values
    │     └─ find_similar_compounds(compound) → Tanimoto similarity results
    │
    ├─ Phase 2: Fitting
    │     ├─ fit_block(doi, block, property_hint, property_type, pure_x0, pure_x1)
    │     │     ├─ _extract_and_match() → BlockData + ColumnMatch
    │     │     │     └─ retry-without-filter if property_hint fails
    │     │     ├─ filter_mixture_points(x, y, eps=0.02)
    │     │     ├─ build_ideal_baseline(pure_values, x, property_type)
    │     │     │     ├─ Linear: Y = x₁·Y₁* + x₂·Y₂*
    │     │     │     └─ Arrhenius: Y = exp(x₁·ln(Y₁*) + x₂·ln(Y₂*))
    │     │     ├─ compute_excess_property() → y_excess
    │     │     ├─ auto_fit_redlich_kister(x, y_excess, max_order=5)
    │     │     │     └─ BIC order selection (tries 0..max_order)
    │     │     └─ _save_fit_outputs() → CSV + plots
    │     │
    │     ├─ fit_multi_system(systems: list[dict]) — parallel multi-block fitting
    │     ├─ compute_ideal_baseline() — standalone baseline
    │     └─ predict_from_rk(coeffs, pure_values) — predict Y(x)
    │
    └─ Phase 3: Verdict (automatic quality review)
          └─ _run_verdict() → independent LLM reviews R², residuals, physics
```

Each tool call is followed by a `call_tool_subagent()` (500 tokens) that
produces `ToolResult(raw, text, discarded)`.  The agent sees `.text` in
conversation; working memory stores `.raw` for later reference.

### 4.3 Main Agent Flow

```
User Question (e.g. "what density data exists for ethanol-water?")
    │
    ▼
main orchestrator.run(question) → MainRunResult
    │
    ├─ init_session() → SessionManager
    ├─ build tool registry:
    │     run_query_agent, run_analysis_agent, run_parallel_subagents
    │     browse_subagent_tools, run_subagent_tool, list_session_files
    │     + 8 memory MCP tools (instrumented via make_instrumented_wrapper)
    │
    ├─ agent_turn(client_L0, system_prompt_L0, tools, ...)
    │     │
    │     ├─ LLM decides: call run_query_agent(question)
    │     │     │
    │     │     ├─ Spawns query agent → ThermoML_query_run()
    │     │     │     (preserve_active_session guards the parent session)
    │     │     ├─ _extract_query_entity_summary(tool_history)
    │     │     │     → {n_compounds, n_properties, n_dois,
    │     │     │        n_blocks, n_subsystems, n_matching_datapoints}
    │     │     └─ Returns result dict with answer + entity_summary
    │     │
    │     ├─ LLM may call run_parallel_subagents(tasks)
    │     │     ├─ ThreadPool dispatch (copy_context per task)
    │     │     └─ ToolResult: raw {n_tasks, results} → working memory,
    │     │        agentically compacted per-task report → context
    │     │
    │     ├─ Instrumented wrapper records to WM:
    │     │     ├─ _record_query()/_record_analysis() keep full child answers
    │     │     └─ Entity counts propagated to WM ID catalog
    │     │
    │     ├─ LLM may call run_analysis_agent(question)
    │     │     ├─ Spawns analysis agent → ThermoML_analysis_run()
    │     │     └─ Returns AnalysisRunResult fields
    │     │
    │     ├─ LLM synthesises results → final answer
    │     │
    │     └─ AGENT_RECORD_REFERENCES fires once (JSON fast-path guard)
    │
    └─ Verdict → independent LLM reviews dispatch strategy
```

---

## 5. Agent Budget Summary

### 5.1 Query Agent Budgets

| Layer | Model | Max Iters | Time Budget | Token Limit |
|-------|-------|-----------|-------------|-------------|
| L0 Orchestrator | claudeopus46 | 25 | 800s | 6000/call |
| L1 Query Worker | claudeopus46 | 12 | 240s | 6000/call |
| L2 Leaf Evaluator | claudeopus46 | 6 | 90s | 6000/call |
| Verdict | claudeopus46 | 1 | 60s | 500/call |
| Compactor (sub-agent) | claudeopus46 | 1 | — | 6000/call |

### 5.2 Analysis Agent Budgets

| Layer | Model | Max Iters | Time Budget | Token Limit |
|-------|-------|-----------|-------------|-------------|
| L0 Orchestrator | claudeopus46 | 30 | 1200s (20 min) | 6000/call |
| L1 Data Retrieval | claudeopus46 | 12 | 240s (4 min) | 6000/call |
| L1 Fitting | claudeopus46 | 15 | 300s (5 min) | 6000/call |
| Verdict | claudeopus46 | 1 | 60s | 500/call |
| Tool Subagent | claudeopus46 | 1 | — | 500/call |

Time warnings at 65% / 85% / 95% of each layer's budget.

### 5.3 Main Agent Budgets

| Layer | Model | Max Iters | Time Budget | Token Limit |
|-------|-------|-----------|-------------|-------------|
| L0 Orchestrator | claudeopus46 | 40 | 2400s (40 min) | 6000/call |
| Verdict | claudeopus46 | 1 | 60s | 500/call |
| Compactor (sub-agent) | claudeopus46 | 1 | — | 6000/call |

Time warnings at 65% / 85% / 95% of budget.  No protected tools
(all tool results are compactable).

---

## 6. Search Tool API Summary

All search functions in `basic_search_tools/` follow the same pattern:
agent passes human-friendly input or an exact scoped global ID →
`_id_alignment_search` resolves canonical `GLOB*` IDs → one SQLite query →
returns `{query_params, n_results, results}`. Retired unscoped IDs are rejected.

| # | Function | Database | Key Parameters |
|---|----------|----------|----------------|
| 0 | `_id_alignment_search` | ID_DK CSVs | fuzzy name→typed `GLOB*` resolution |
| 1 | `search_blocks` | PCS_INDIV + PM_registry | compounds, properties, T/P range, phase, limit |
| 2 | `search_system_registry` | PM/RD_registry | T/P range, n_datapoints_min, limit |
| 3 | `search_compound_dk` | CCS_ID_DK | name/formula/SMILES, returns SMILES + fingerprint status |
| 4 | `search_references` | RMS_INDIV | DOI, authors, journal, year_range, limit |
| 5 | `search_measurement_dk` | MTDKS_ID_DK | method name/keywords |
| 6 | `search_measurement_indiv` | MTDKS_INDIV | method, DOI, compound filter, limit |
| 7 | `search_property_dk` | PCS_ID_DK | property name/keywords |
| 8 | `search_compound_indiv` | CCS_INDIV | compound, DOI, min_purity, limit |
| 9 | `search_system_summary` | PM_registry | compounds, properties, T/P range, aggregated stats |
| 10 | `search_similar_compounds` | CCS_ID_DK (fingerprints) | name/SMILES, Morgan Tanimoto, top_k, min_similarity |
| 11 | `extract_block_csv` | PCS_INDIV | doi, block_number → resolved column names + data |

---

## 7. Relationship to Sibling Agents

This architecture was adapted from two proven sibling codebases:

| Pattern | Source | Applied In |
|---------|--------|------------|
| `ArgoClient` dataclass | SRD46 + Speciation | `argo_client.py` |
| ReAct `agent_turn` loop | SRD46 `ui.py` | `ui.py` |
| 3-step LLM compaction | SRD46 `compactor.py` | `support_helpers/compactor.py` |
| Time-budget soft warnings | Speciation `agent_turn` | `ui.py` (65/85/95%) |
| Post-job verdict | Both | `support_helpers/postjob_verdict.py` |
| Phase-gated workflow | Speciation | L0/L1/L2 workflow markdowns |
| Exact parameter validation | ThermoML strict interface | ReAct engine + wrapped tool catalog |

---

## 8. File Tree

```
NIST_ThermoML_agents/
├── ARCHITECTURE.md                              ← This file
├── __init__.py
│
├── general_argo_engine_helpers/                  # Shared ReAct engine (used by all agents)
│   ├── __init__.py                              # Eager: EngineConfig/load_config/get_config/AnchorPoint/anchor; lazy: ArgoClient, agent_turn, etc.
│   ├── engine_config.py                         # EngineConfig base dataclass + singleton
│   ├── engine_hooks_anchors.py                  # AnchorPoint (62+5 types), anchor() dispatch, EngineHooks TypedDict
│   ├── argo_client_caller.py                    # ArgoClient dataclass (call/acall)
│   ├── async_runner.py                          # fan_out() + run_workflow()
│   ├── argo_agent_terminal_ui.py                # Shared terminal UI base class
│   ├── _argo_engine_entry_point.py              # Re-exports for convenient imports
│   ├── engine_react_helpers/                    # ReAct loop subsystem
│   │   ├── react_loop.py                        # agent_turn() sync ReAct loop
│   │   ├── react_loop_async.py                  # async_agent_turn()
│   │   └── react_helpers.py                     # AgentTurnResult + exact argument validation
│   └── engine_tool_interface_helpers/           # Tool interface subsystem
│       ├── tool_call_parser.py                  # exact XML-wrapped JSON tool-call extraction
│       └── tool_menu_agent_interface.py         # Tool menu registration interface
│
├── general_text_context_marker_catalog/          # Centralized XML text markers
│   ├── __init__.py                              # Re-exports all from context_markers
│   └── context_markers.py                       # TagPair, ContextMarkerCatalog (13 families), MARKERS singleton
│
├── general_tool_management_helpers/              # Shared tool & compaction infrastructure
│   ├── __init__.py
│   ├── _tool_hooks_anchors_catalog.py           # Tool anchor types (19 types): TOOL_EXEC_, TOOL_COMPACTION_, SUBAGENT_
│   ├── general_agent_tool_catalog/              # Class-based tool catalogs
│   │   ├── __init__.py                          # Exports: ToolEntry, AgentToolCatalog, CompactorCatalog, etc.
│   │   ├── tool_entry.py                        # ToolEntry frozen dataclass
│   │   ├── agent_tool_catalog.py                # AgentToolCatalog base class
│   │   ├── agent_tool_compactor_hooks_catalog.py # CompactorCatalog + @compacts/@uses_compactors
│   │   └── health_check_helper/                 # Startup validation
│   │       ├── __init__.py
│   │       └── heath_check_tools_compactors_catalogs.py  # run_health_check(), CatalogHealthCheckError
│   ├── general_tool_results_compactor_agentic_hooks/  # Shared KEEP/DISCARD LLM subagent
│   │   ├── __init__.py                          # Exports: ToolResult, ToolResultCompactor, call_tool_subagent
│   │   └── _search_tool_results_compact_subagent.py
│   └── general_tool_menu_tools/                 # ToolMenuRegistry, MenuEntry — hierarchical tool browsing
│
├── general_hooks_management_helpers/             # Parent for context hooks, memory, output writers
│   ├── __init__.py
│   ├── README.md
│   │
│   ├── general_context_hooks/                   # Shared cross-agent runtime hooks
│   │   ├── __init__.py
│   │   ├── README.md
│   │   ├── _context_hooks_anchors_catalog.py    # Context anchor types (31 types: prompt 8, answer 8, time-budget 5, compaction 10)
│   │   ├── time_budget_reminder_hooks.py        # TimeBudgetTracker
│   │   ├── self_compactor_interactive_hooks.py  # Shared 3-step compaction engine
│   │   ├── context_cleanup_compactor_hooks.py   # Context cleanup hooks
│   │   ├── history_tracking_hooks.py            # HistoryRecorder → run_history.md
│   │   ├── stats_references_tracking_hooks.py   # StatsRecorder → reference_stats.md
│   │   ├── reasoning_token_tracking_hooks.py    # ReasoningTokenTracker → reasoning_tokens_stripped.md
│   │   └── postjob_verdict_hooks.py             # (placeholder)
│   │
│   ├── general_memory_management_tools_hooks_helpers/  # Working memory + session management
│   │   ├── __init__.py
│   │   ├── README.md
│   │   ├── _memory_hooks_anchors_catalog.py     # Memory anchor types (2 types)
│   │   ├── general_memory_hooks.py              # BaseWorkingMemory ABC
│   │   ├── memory_local_storage_io.py           # WorkingMemory class
│   │   ├── memory_management_MCP_tools.py       # 8 MCP tool wrappers
│   │   ├── memory_merger_helpers_and_agent.py   # Cross-session merger
│   │   └── session_manager_output_storage.py    # SessionManager
│   │
│   └── general_tracking_hooks_output_helpers/   # Test output & answer cleanup
│       ├── __init__.py
│       ├── output_writers.py                    # write_test_summary(), write_json_trace()
│       └── answer_cleaner.py                    # clean_answer()
│
├── general_db_search_tool_registry/              # Auto-discovered search tools
│   ├── __init__.py
│   └── db_search_tool_registry.py                # 27 tools, 4 categories
│
├── general_subagent_delegation_helpers/           # Shared cross-agent delegation primitives
│   ├── __init__.py                              # Exports: SubagentSessionManager, build_full_question, extract_run_result, dispatch_parallel, merge_subagent_tracking
│   ├── _session_nesting.py                      # SubagentSessionManager — DI wrapper for nested session dirs
│   ├── _question_builder.py                     # build_full_question() — structured question assembly
│   ├── _result_extractor.py                     # extract_run_result() — normalised result dicts
│   ├── _parallel_dispatch.py                    # dispatch_parallel() — ThreadPoolExecutor fan-out
│   └── _tracking_combiner.py                    # merge_subagent_tracking() — tracking MD combination
│
├── general_subagent_skill_schema_and_parser/     # Workflow markdown parser
│   ├── __init__.py
│   ├── subworkflow_md_parser.py
│   └── subworkflow_md_tool_descriptions.py
│
├── general_ThermoML_db_csv_registry/             # DB / CSV path registry
│   ├── __init__.py
│   └── ThermoML_db_csv_registry.py
│
├── general_hooks_management_helpers/             # Organizational only (no code)
│   └── README.md
│
├── NIST_ThermoML_query_agent/
│   ├── ThermoML_query_api.py                     # Public API entry point
│   ├── ThermoML_query_argo_config.py             # QueryAgentConfig(EngineConfig)
│   ├── __init__.py
│   ├── query_agent_argo_engine/                  # Agent-specific LLM client
│   │   ├── __init__.py
│   │   ├── argo_client.py                        # QueryClient (for_l0, for_l1, for_l2, for_verdict)
│   │   └── query_agent_terminal_ui.py            # Interactive CLI
│   ├── query_agent_toolbox/                      # Tool catalog
│   │   ├── __init__.py
│   │   └── tool_catalog.py                       # QueryL0Catalog + L0_TOOL_CATALOG flat dict
│   ├── query_agent_context_hooks/                # All context hooks (5 sub-categories)
│   │   ├── hook_catalog.py                       # Single entry point (re-exports all)
│   │   ├── compactor_hooks/                      # Tool-result + stage compaction
│   │   │   ├── tool_result_compactor.py          # QueryToolResultCompactor
│   │   │   └── context_stage_compaction.py       # QueryStageCompactor
│   │   ├── interactive_hooks/                    # LLM-driven context compaction
│   │   │   └── interactive_compactor.py          # QueryInteractiveCompactor
│   │   ├── memory_hooks/                         # Memory lifecycle
│   │   │   ├── working_memory_hooks.py           # QueryWorkingMemory, init, loader
│   │   │   ├── l1_autosave_hooks.py              # L1AutoSaver
│   │   │   └── thin_answer_guard.py              # Thin-answer detection
│   │   ├── tracking_hooks/                       # Observability recorders
│   │   │   ├── history_hooks.py                  # QueryHistoryRecorder
│   │   │   ├── stats_hooks.py                    # QueryStatsRecorder
│   │   │   └── time_budget_hooks.py              # QueryTimeBudgetTracker
│   │   └── verdict_hooks/                        # Post-job review
│   │       └── postjob_verdict.py                # QueryVerdictRunner
│   ├── query_agent_workflows/                    # Workflow orchestration
│   │   ├── L0_orchestrator/                      # run() + workflow markdown
│   │   ├── L1_workers/                           # L1 query dispatcher + workflow
│   │   ├── L2_leaf_evaluators/                   # 4× L2 dispatchers + workflows
│   │   └── _subworkflow_md_parser/               # Workflow .md parser
│   ├── query_agent_heath_check_helpers/          # (empty — reserved)
│   └── _DEBUG_script/                            # Test runner + prompts
│
├── NIST_ThermoML_analysis_agent/
│   ├── ThermoML_analysis_api.py                  # Public API entry point
│   ├── ThermoML_analysis_argo_config.py          # AnalysisAgentConfig(EngineConfig)
│   ├── __init__.py
│   ├── analysis_agent_argo_engine/               # Agent-specific LLM client
│   │   ├── argo_client.py                        # AnalysisClient (for_l0, for_l1_data, for_l1_fit, for_verdict)
│   │   └── analysis_agent_terminal_ui.py         # Interactive CLI
│   ├── analysis_agent_toolbox/                   # Tool catalog + tools
│   │   ├── tool_catalog.py                       # AnalysisCatalog + TOOL_CATALOG flat dict
│   │   ├── _imports.py                           # Shared path setup + imports
│   │   ├── query_delegation_tools.py             # query_thermoml, query_thermoml_parallel (direct L1 dispatch)
│   │   ├── sibling_agent_delegation_tools/       # Full L0 query-agent delegation (via general_subagent_delegation_helpers)
│   │   │   ├── __init__.py                       # Exports TOOL_ENTRIES
│   │   │   └── query_agent_tool.py               # run_query_agent_sibling, run_parallel_query_siblings
│   │   ├── hardcoded_data_tools.py               # inspect_block, get_pure_values
│   │   ├── fitting_tools.py                      # fit_block, fit_multi_system, etc.
│   │   ├── resolve_tools.py                      # resolve_compounds, resolve_properties
│   │   └── discovery_tools.py                    # query_system_summary, query_blocks, etc.
│   ├── analysis_agent_context_hooks/             # All context hooks (5 sub-categories)
│   │   ├── hook_catalog.py                       # Single entry point
│   │   ├── compactor_hooks/                      # Tool-result + stage + per-tool compactors
│   │   ├── interactive_hooks/                    # LLM-driven context compaction
│   │   ├── memory_hooks/                         # AnalysisWorkingMemory
│   │   ├── tracking_hooks/                       # History, stats, time budget recorders
│   │   └── verdict_hooks/                        # Post-job review
│   ├── analysis_agent_workflows/                 # Workflow orchestration
│   │   ├── L0_orchestrator/                      # run() + AnalysisRunResult + workflow
│   │   ├── L1_workers/                           # Query delegation + workflow
│   │   └── _subworkflow_md_parser/               # Workflow .md parser
│   ├── analysis_agent_heath_check_helpers/       # (empty — reserved)
│   ├── ThermoML_core_calc_tools/                 # Pure-math / I/O (no LLM)
│   │   ├── csv_io_helpers/                       # BlockData, ColumnMatch
│   │   ├── Redlich_Kister_block_fitting/         # auto_fit_redlich_kister (BIC)
│   │   ├── mixture_nonideality_calc/             # Ideal baselines, excess properties
│   │   ├── output_helpers/                       # CSV, plots, topology repr
│   │   └── topology_helpers/                     # Convex hull, curve topology
│   └── _DEBUG_script/                            # Test runner + prompts
│
├── NIST_ThermoML_editing_agent(stub)/            # (Placeholder — future PDF/text ingest)
│
└── _NIST_ThermoML_main_agent/                    # Master orchestrator (dispatches to query + analysis agents)
    ├── __init__.py
    ├── ARCHITECTURE.md                          # Detailed main agent architecture
    ├── ThermoML_main_argo_config.py             # MainAgentConfig(EngineConfig)
    ├── ThermoML_main_api.py                     # ThermoML_main_run() — public entry point
    ├── main_agent_argo_engine/                  # MainClient(ArgoClient) + terminal UI
    ├── main_agent_toobox/                       # Tool catalog + subagent delegation tools
    │   ├── tool_catalog.py                      # MainCatalog + flat dict
    │   ├── subagent_delegation_tools.py         # run_query_agent, run_analysis_agent, run_parallel_subagents (via general_subagent_delegation_helpers)
    │   └── tool_menu/                           # Hierarchical subagent tool browsing
    │       ├── __init__.py
    │       ├── menu_tools.py                    # browse_subagent_tools(), run_subagent_tool()
    │       └── _registry_builder.py             # Lazy ToolMenuRegistry tree
    ├── main_agent_context_hooks/                # All hooks (compactors, memory, tracking, verdict)
    │   └── hook_catalog.py                      # build_engine_hooks() — wires AnchorType → callbacks
    ├── main_agent_workflows/                    # L0 orchestrator + workflow markdown
    └── _DEBUG_script/                           # Test runner + prompts
```
