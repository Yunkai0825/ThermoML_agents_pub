# ThermoML Analysis Agent — Architecture

> **Version**: 6.2  
> **Updated**: 2026-04-09  
> **Scope**: Complete architecture for the ThermoML analysis & fitting agent  
> **Companion**: [System architecture](../ARCHITECTURE.md) and [agent usage](../README.md).

---

## 1. Overview

Separate agent for thermodynamic data analysis and fitting.  **Delegates all
database queries to the ThermoML query agent** via L1 workers.  Uses
deterministic (hardcoded) tools for block inspection and pure-value extraction,
then runs deterministic calculations (ideal baselines, excess properties,
Redlich-Kister fitting).

**Design Rules:**
- The analysis agent NEVER touches the database directly.
- All DB searching is delegated to the query agent's L1 dispatcher.
- Hardcoded tools (inspect_block, get_pure_values) extract data deterministically
  using resolved DOI + block_number — no LLM subagent involved.
- Fitting tools use compact markdown generators directly — no LLM subagent.
- The agent only provides identifiers (DOI, block_number, property name) and
  pure-component reference values.

---

## 2. Directory Structure

```
NIST_ThermoML_analysis_agent/
├── __init__.py
├── ThermoML_analysis_argo_config.py    # AnalysisAgentConfig(EngineConfig) — all analysis settings
├── ThermoML_analysis_api.py           # Public API entry point (ThermoML_analysis_run)
├── ARCHITECTURE.md                    # ← This file
│
├── analysis_agent_argo_engine/        # Agent-specific LLM client
│   ├── __init__.py
│   ├── argo_client.py                 # AnalysisClient (for_l0, for_l1_data, for_l1_fit, for_verdict)
│   └── analysis_agent_terminal_ui.py  # Interactive CLI REPL
│
├── analysis_agent_toolbox/            # Tool catalog + tool modules
│   ├── __init__.py
│   ├── tool_catalog.py                # AnalysisCatalog(AgentToolCatalog) + ANALYSIS_CATALOG instance
│   ├── AnalysisAgent_toolbox_customization_catalog.md  # Toolbox customization docs
│   ├── query_delegation_tools.py      # query_thermoml, query_thermoml_parallel (L1 direct dispatch)
│   ├── hardcoded_data_tools.py        # inspect_block, get_pure_values (deterministic)
│   ├── fitting_tools.py              # fit_block, fit_multi_system, etc.
│   ├── resolve_tools.py              # resolve_compounds, resolve_properties
│   ├── discovery_tools.py            # query_system_summary, query_blocks, etc.
│   ├── sibling_agent_delegation_tools/  # Full L0 query-agent delegation
│   │   ├── __init__.py                  #   re-exports TOOL_ENTRIES
│   │   └── query_agent_tool.py          #   run_query_agent, run_query_agents_parallel
│   ├── agent_specific_tools/          # (empty — reserved)
│   └── fitting_tools/                 # (empty — reserved)
│
├── analysis_agent_context_hooks/      # All context hooks (5 sub-categories)
│   ├── __init__.py
│   ├── hook_catalog.py                # Single entry point (re-exports all)
│   ├── compactor_hooks/               # Tool-result + stage + per-tool compactors
│   │   ├── tool_result_compactor.py   # AnalysisToolResultCompactor
│   │   ├── context_stage_compaction.py # AnalysisStageCompactor
│   │   └── _tool_compactors.py        # 13 compact_*() markdown generators
│   ├── interactive_hooks/             # LLM-driven 3-step context compaction
│   │   ├── interactive_compactor.py   # AnalysisInteractiveCompactor
│   │   └── fitting_variable_guidance.py # FittingVariableGuidance(PreExecutionGuidance)
│   │                                #   → auto-fills property_type, pure values for fit_block
│   ├── memory_hooks/                  # Agent working memory
│   │   └── working_memory_hooks.py    # AnalysisWorkingMemory
│   ├── tracking_hooks/                # Observability recorders
│   │   ├── history_hooks.py           # AnalysisHistoryRecorder
│   │   ├── stats_hooks.py            # AnalysisStatsRecorder
│   │   └── time_budget_hooks.py       # AnalysisTimeBudgetTracker
│   └── verdict_hooks/                 # Post-job quality review
│       └── postjob_verdict.py         # AnalysisVerdictRunner
│
├── analysis_agent_workflows/          # Workflow orchestration
│   ├── L0_orchestrator/               # run() + AnalysisRunResult + workflow
│   │   ├── orchestrator.py
│   │   └── L0_analysis_workflow.md
│   ├── L1_workers/                    # Query delegation + workflow
│   │   ├── l1_query_delegation.py
│   │   └── L1_query_delegation_workflow.md
│   └── _subworkflow_md_parser/        # Workflow .md parser
│       └── subworkflow_parser.py
│
├── analysis_agent_heath_check_helpers/ # (empty — reserved)
│
├── _DEBUG_script/                     # Test runner & output
│
└── ThermoML_core_calc_tools/          # Pure-math / I/O (no LLM)
    ├── __init__.py
    ├── csv_io_helpers/
    │   ├── __init__.py                # Exports: BlockData, ColumnMatch, extract_block_arrays,
    │   │                              #   identify_columns, filter_mixture_points, arrays_to_csv
    │   └── block_data_io.py           # CSV parsing, array extraction, condition grouping
    ├── mixture_nonideality_calc/
    │   ├── __init__.py
    │   ├── ideal_baseline.py          # build_ideal_baseline, compute_excess_property,
    │   │                              #   extract_pure_from_edges (N-component support)
    │   ├── baseline_diagnostics.py    # run_single_baseline, run_multi_T_baseline
    │   └── notes.md
    ├── Redlich_Kister_block_fitting/
    │   ├── __init__.py
    │   ├── rk_fitter.py               # fit_redlich_kister, auto_fit_redlich_kister (BIC),
    │   │                              #   eval_redlich_kister, fit_multi_property
    │   └── rk_diagnostics.py          # run_rk_fit_single, run_rk_fit_multi_group
    ├── output_helpers/
    │   ├── __init__.py
    │   ├── csv_export.py              # save_fit_csv, save_excess_csv, save_baseline_csv
    │   ├── plot_export.py             # save_fit_plot, save_excess_plot
    │   └── topology_repr.py           # extract_topology_points, topology_to_csv
    └── topology_helpers/
        ├── __init__.py
        ├── convex_hull_construction.py    # compute_convex_hull, hull_edge_indices,
        │                                  #   select_hull_edge_points
        └── curve_representation_algorithm.py  # build_curve_topology
```

---

## 3. Core Module Reference

### 3.1 `ThermoML_analysis_argo_config.py`

`AnalysisAgentConfig(EngineConfig)` — single dataclass holding all settings.
Step 1 fields provide defaults for the 26 shared engine fields.
Step 2 fields define analysis-agent-only parameters.
Consumers import `AGENT_CONFIG` directly:
```python
from ..ThermoML_analysis_argo_config import AGENT_CONFIG as cfg
```

| Field | Default | Section | Description |
|-------|---------|---------|-------------|
| `MODEL` | `claudeopus46` | Step 1 | L0 orchestrator model |
| `VERDICT_MODEL` | `claudeopus46` | Step 1 | Post-job quality reviewer |
| `PLANNER_MODEL` | `claudeopus46` | Step 1 | Strategy planner (react_loop guidance) |
| `TEMPERATURE` | `0.3` | Step 1 | Sampling temperature |
| `MAX_TOKENS` | `6000` | Step 1 | Max tokens per LLM response |
| `MAX_TOOL_ITERATIONS` | `30` | Step 1 | L0 tool-call cap (higher than query agent) |
| `MAX_TURN_SECONDS` | `1200` | Step 1 | L0 wall-clock budget (20 min) |
| `VERDICT_MAX_TOKENS` | `2000` | Step 1 | Generous budget for fit-quality review |
| `TOOL_RESULT_CHAR_LIMIT` | `24000` | Step 1 | Post-compaction size contract; oversize raises |
| `COMPACTION_TRIGGER_CHARS` | `80000` | Step 1 | Context size triggering compaction |
| `L1_MODEL` | `claudeopus46` | Step 2 | L1 data-retrieval + fitting workers |
| `L1_DATA_MAX_ITERATIONS` | `12` | Step 2 | Data-retrieval phase iteration cap |
| `L1_FIT_MAX_ITERATIONS` | `15` | Step 2 | Fitting phase iteration cap |
| `SUBAGENT_MAX_TOKENS` | `500` | Step 2 | Tool sub-agent response budget |
| `PROTECT_TOOLS` | 6 fitting tools | Step 2 | Tools exempt from LLM compaction |
| `OUTPUT_DIR` | `_output/` | Step 2 | Session run artifact directory |
| `TRANSCRIPT_DIR` | `transcripts/` | Step 2 | Full conversation transcripts |

Module-level fitting parameters (outside the dataclass):

| Constant | Value | Description |
|----------|-------|-------------|
| `RK_MAX_ORDER` | `5` | Maximum Redlich-Kister polynomial order |
| `RK_MIN_DATAPOINTS` | `5` | Minimum data points (excl. pure) for fitting |
| `IDEAL_BASELINE_PROPS` | 5 properties | Properties with ideal-solution baselines |
| `ARRHENIUS_PROPS` | `["viscosity"]` | Properties fitted in log space |

### 3.2 `analysis_agent_argo_engine/argo_client.py`

```python
@dataclass
class AnalysisClient(_BaseClient):
    @classmethod def for_l0(cls) -> AnalysisClient       # Orchestrator
    @classmethod def for_l1_data(cls) -> AnalysisClient  # Data retrieval
    @classmethod def for_l1_fit(cls) -> AnalysisClient   # Fitting workers
    @classmethod def for_verdict(cls) -> AnalysisClient  # Post-job review
```

The analysis agent imports its concrete client only from
`analysis_agent_argo_engine/argo_client.py`; no root-level compatibility module exists.

### 3.3 `session_manager.py`

```python
class SessionManager:
    session_dir: Path       # _output/run_{ts}_{slug}/
    data_dir: Path          # session_dir / data/
    plots_dir: Path         # session_dir / plots/
    _catalog: list[dict]    # [{category, path, description}, ...]

    def ensure_dirs(self)
    def data_path(filename: str) -> Path
    def plot_path(filename: str) -> Path
    def register_file(category, path, description="")
    def list_files() -> list[dict]
    def render_manifest(*, root_dir=None) -> str

# Module-level API
def init_session(base_dir, question) -> SessionManager
def get_session() -> Optional[SessionManager]
def close_session()
```

### 3.4 `ui.py` — Thin CLI

Thin interactive CLI that re-exports ``run``, ``AnalysisRunResult``, and
``list_session_files`` from ``L0_orchestrator.orchestrator`` for backward
compatibility.  Contains only the ``main()`` REPL loop.

### 3.5 `L0_orchestrator/orchestrator.py` — Main Orchestrator

```python
class WorkingMemory:      # → analysis_agent_context_hooks/memory_hooks/working_memory_hooks.py
    """Tracks query results, resolved IDs, inspected blocks, and fit results."""
    resolved_compounds: dict
    resolved_properties: dict
    query_results: list[dict]      # v4: tracks query agent responses
    inspected_blocks: list[dict]
    fit_results: list[dict]

    def record_tool_result(self, tool_name: str, result: dict)
    def sync_to_disk(self)
    def render(self) -> str

@dataclass
class AnalysisRunResult:
    """Structured result — supports both attribute and dict-style access."""
    answer: str
    verdict: str | None
    iterations: int
    elapsed_seconds: float
    tool_history: list[dict]
    timed_out: bool = False
    session_dir: str | None = None
    output_files: list[dict]

    def __getitem__(self, key)    # dict-style: result['iterations']
    def __setitem__(self, key, value)
    def __contains__(self, key)
    def get(self, key, default=None)

def run(question: str, *, run_verdict: bool = True) -> AnalysisRunResult
def list_session_files(purpose="", tasks="") -> dict
def _save_run_output(question, result: AnalysisRunResult) -> Optional[Path]
```

### 3.6 `main_workflow_support_helpers/postjob_verdict.py`

```python
def run_verdict(question, answer, tool_history, client) -> str
```

### 3.7 `ThermoML_analysis_api.py` — Public API

```python
def ThermoML_analysis_run(
    question: str,
    *,
    run_verdict: bool = True,
    session_dir: str | Path | None = None,
) -> AnalysisRunResult
```

Single entry-point for external consumers of the analysis agent.
`session_dir` allows a parent agent to inject a pre-existing output
directory so analysis artifacts are co-located with the caller's session.

---

## 4. Tool Registry (12 Tools, 3 Phases + Sibling Delegation)

### Phase 0 — Resolution

| Tool | Signature | Purpose |
|------|-----------|---------|
| `resolve_compounds` | `(names: str) → dict \| ToolResult` | Resolve compound names → ThermoML num_ids |
| `resolve_properties` | `(names: str) → dict \| ToolResult` | Resolve property names → ThermoML num_ids |

### Phase 1 — Discovery

| Tool | Signature | Purpose |
|------|-----------|---------|
| `query_system_summary` | `(compounds: list[str], properties: list[str] \| None=None, limit=20)` | Data availability overview |
| `query_blocks` | `(compounds: list[str], properties: list[str] \| None=None, limit=50, temperature_range=None, pressure_range=None)` | Block metadata search |
| `inspect_block` | `(doi, block_number, property_filter="")` | Block structure: columns, ranges, row count |
| `find_similar_compounds` | `(compound, top_k=10, min_similarity=0.5)` | Tanimoto fingerprint similarity search |
| `get_pure_values` | `(doi, block_number, property_hint, composition_hint="mole_fraction", edge_threshold=0.02)` | Extract pure-component endpoint values |

### Phase 2 — Fitting

| Tool | Signature | Purpose |
|------|-----------|---------|
| `fit_block` | `(doi, block_number, ..., component_names: list[str] \| None, x_vars: list[str] \| None, y_props: list[str] \| None, x_vars_constrained: dict \| None, properties: list[dict] \| None, pure_values: dict \| None)` | Unified native structured binary RK fitting pipeline: single-property, multi-property, or temperature-sweep mode |
| `fit_multi_system` | `(systems: list[dict])` | Parallel fitting across exact system specifications |
| `compute_ideal_baseline` | `(pure_values: dict, property_type, n_datapoints=101, mixing_rule="")` | Standalone ideal baseline computation |
| `predict_from_rk` | `(coeffs: list[float], pure_values: dict, property_type, n_datapoints=101, mixing_rule="")` | Predict Y(x) from fitted RK coefficients |

### Sibling Delegation (Full L0 Query Agent)

| Tool | Signature | Purpose |
|------|-----------|--------|
| `run_query_agent` | `(question, purpose, tasks, context)` | Invoke the **full L0 query agent** (own ReAct loop) for open-ended DB exploration |
| `run_query_agents_parallel` | `(queries: list[dict])` | Run multiple exact L0 query-agent tasks in parallel (up to 3 workers) |

Both tools have `skip_compactor=True` and `skip_subagent=True` — the query
agent's own output is already structured, so no tool-subagent post-processing
is needed.

---

Tool arguments are validated against their exact current Python annotations.
Arrays and objects remain native JSON values; identifiers and numbers are never
coerced from old spellings or quoted numeric strings.

---

## 5. Tool Subagent Pattern

Each tool call is followed by a lightweight LLM subagent call (500 tokens)
that examines the raw result and decides:

```
<thought>Evaluate relevance & data quality</thought>
<action>KEEP</action> or <action>DISCARD</action>
<output>Extracted key facts / refinement suggestion</output>
```

```python
@dataclass
class ToolResult:
    raw: dict         # Original result dict (for working memory)
    text: str         # Subagent output markdown (for conversation)
    discarded: bool   # True if subagent chose DISCARD
```

---

## 6. Processing Pipeline

### fit_block — Full Pipeline

```
fit_block(doi, block_number, property_hint, property_type,
          component_names, x_vars, y_props, x_vars_constrained, pure_values)
    │
    ├─ _extract_and_match(doi, block_number, property_hint, composition_hint)
    │     ├─ extract_block_arrays() → BlockData (doi, columns, arrays, metadata)
    │     ├─ identify_columns(property_hint) → ColumnMatch (x_column, y_column)
    │     └─ Retry: if property_hint fails, retry without filter + add hints to error
    │
    ├─ filter_mixture_points(x, y, eps=0.02) → remove pure endpoints
    ├─ build_ideal_baseline(pure_values, x, property_type) → y_ideal
    │     ├─ Linear: Y = x₁·Y₁* + x₂·Y₂*
    │     └─ Arrhenius: Y = exp(x₁·ln(Y₁*) + x₂·ln(Y₂*))
    ├─ compute_excess_property() → y_excess = measured - ideal
    │     └─ Arrhenius: y_excess = ln(Y_meas) - (x₁·ln(Y₁*) + x₂·ln(Y₂*))
    ├─ auto_fit_redlich_kister(x, y_excess, max_order=5) → coeffs + BIC selection
    │     └─ Y^E(x₁) = x₁·x₂·Σ Aₖ·(x₁−x₂)^k
    ├─ Arrhenius back-transform: Y_fitted = exp(ln(Y_ideal) + y_excess_fitted)
    ├─ _save_fit_outputs() → CSV + plots (registered in SessionManager)
    │     └─ Arrhenius: CSV y-column = `ln_excess_{property}` (not raw property name)
    └─ call_tool_subagent() → ToolResult with extracted summary
```

### inspect_block

```
inspect_block(doi, block_number)
    │
    ├─ extract_block_arrays() → BlockData
    ├─ identify_columns() → ColumnMatch
    └─ Returns: compounds, compound_map, variables, properties, constraints,
               columns, n_rows, identified_x/y, column_compound_map, column_ranges
```

---

## 7. Postprocessing Tools (Pure Math / I/O — No LLM)

### 7.1 csv_io_helpers

| Function | Purpose |
|----------|---------|
| `extract_block_arrays(doi, block_number)` | JSON card → `BlockData` (NumPy arrays) |
| `identify_columns(columns, property_hint, composition_hint)` | Auto-detect x/y columns → `ColumnMatch` |
| `filter_mixture_points(x, y, eps=0.02)` | Remove pure endpoints (x≈0 or x≈1) |
| `arrays_to_csv(columns, data)` | Convert arrays back to CSV string |
| `identify_varying_conditions(columns, arrays, x_col, y_col)` | Detect varying T/P conditions |
| `unique_condition_groups(arrays, cond_cols)` | Sorted unique condition tuples |
| `filter_to_condition(arrays, cond_cols, values, tol)` | Filter to one T/P slice |

**Key Dataclasses:**

```python
@dataclass BlockData:    # doi, block_number, columns, arrays, n_rows, metadata, error
@dataclass ColumnMatch:  # x_column, y_column, x_columns, y_columns, column_compound_map, error
```

### 7.2 mixture_nonideality_calc

| Function | Purpose |
|----------|---------|
| `build_ideal_baseline(pure_values, x_grid, property_type)` | Compute ideal-mixture baseline (linear or Arrhenius) |
| `compute_excess_property(x_data, y_data, pure_values, property_type)` | Y^E = measured − ideal |
| `extract_pure_from_edges(x_dict, y_data, threshold)` | Extract pure-component values from data edges |
| `pure_values_from_edges(x_dict, y_data, threshold)` | Convenience: returns flat `{comp: value}` |
| `default_mixing_rule(property_type)` | Canonical rule: `"arrhenius"` for transport, `"linear"` otherwise |

N-component support: all functions accept `Dict[str, np.ndarray]` for composition.

### 7.3 Redlich_Kister_block_fitting

| Function | Purpose |
|----------|---------|
| `fit_redlich_kister(x1, y_excess, max_order=5)` | Fixed-order RK fit via least squares |
| `auto_fit_redlich_kister(x1, y_excess, max_order=5)` | Auto order selection via BIC (tries 0..max_order) |
| `eval_redlich_kister(x1, coeffs)` | Evaluate Y^E at given compositions |
| `fit_multi_property(x1, excess_dict, max_order)` | Fit RK for multiple excess properties on same x grid |

**RK Equation:** `Y^E(x₁) = x₁ · x₂ · Σ_{k=0}^{n} Aₖ · (x₁ − x₂)^k`

### 7.4 output_helpers

| Module | Functions |
|--------|-----------|
| `csv_export.py` | `save_fit_csv`, `save_excess_csv`, `save_baseline_csv` |
| `plot_export.py` | `save_fit_plot` (2-panel: fit + residuals), `save_excess_plot` |
| `topology_repr.py` | `extract_topology_points` (convex hull + curvature), `topology_to_csv` |

### 7.5 topology_helpers

| Module | Functions |
|--------|-----------|
| `convex_hull_construction.py` | `compute_convex_hull`, `hull_edge_indices`, `select_hull_edge_points` |
| `curve_representation_algorithm.py` | `build_curve_topology` (orchestrates hull + topology) |

---

## 8. Dynamic Column Resolution

Column names from raw JSON cards contain placeholder references like
`mole_fraction_DOIcomp_19` or `pressure_kpa_{DOIcomp_id}`.  The extractor
resolves these to human-readable names:

```
mole_fraction_DOIcomp_19  →  mole_fraction_<heptane>
pressure_kpa_{DOIcomp_id} →  pressure_kpa_<pentaerythritol tetrahexanoate>
temperature_k          →  temperature_k  (no compound ref, unchanged)
```

Resolution uses:
1. `org_num` mapping (XML sequential index → compound name)
2. `comp_num_id` mapping (database ID → compound name)
3. `{DOIcomp_id}` template resolution from the explicit DOI compound map

An unresolved component reference is a refinement/error condition. Component
identity is never inferred from compound-list position.

---

## 9. Memory Compaction

`analysis_agent_context_hooks/interactive_hooks/interactive_compactor.py`
is a thin wrapper around the shared compaction engine in
`general_context_hooks/self_compactor_interactive_hooks.py`.
It injects the analysis agent's config (`argo_config`) and `PROTECT_TOOLS`
set, then delegates to the shared 3-step LLM-driven cycle:

1. **SELECT** — Ask main Argo which tool results to compress (or SKIP all)
2. **COMPRESS** — Sub-agent summarizes selected results
3. **VALIDATE** — Main Argo replies with one of three verdicts:
   - **ACCEPT** — summary is good → replace memory slot
   - **RETRY** — summary missed data → immediately re-compress
     (up to `MAX_IMMEDIATE_RETRY` times within the same cycle)
   - **SKIP** — not worth compressing → tag `[RETRY:N+1]` and move on;
     will be reconsidered next cycle (up to `MAX_RETRY` total across cycles)

Compaction is fully optional — the selection step and validation step can
both freely choose to skip.  After `MAX_RETRY` cross-cycle rejections,
the result is permanently kept uncompressed.

**Protected tools** (never compressed):
`fit_block`, `fit_multi_system`, `predict_from_rk`, `compute_ideal_baseline`.

These contain final RK coefficients & R² values the agent must cite verbatim.

---

## 9b. Working Memory Formatting Pipeline

When `query_thermoml` or `query_thermoml_parallel` returns, the raw tool
result (JSON string or markdown with embedded JSON sub-sections) must be
converted to compact markdown before storing in working memory.  This
prevents raw JSON from inflating the context window.

### Single-query path (`query_thermoml`)

The instrumented wrapper passes `{**parsed_dict, "text": original_string}`
to `record_tool_result()`.  `_format_l1_block(data)` extracts:

- `summary` text (always present)
- `core_blocks_found[]` → table with DOI, typed block ID, system type, and `n_datapoints`
- If `n_datapoints` is missing from a block, the column shows "-" (auto-resolved)

Returns compact markdown:
```
**Query:** <question>
**Summary:** 4 blocks found …

| DOI | blk | compounds | properties | T(K) | P(kPa) | pts |
|-----|-----|-----------|------------|-------|--------|-----|
| 10.1016/… | 1 | ethanol, water | viscosity | 293–343 | 101 | 37 |
```

### Parallel-query path (`query_thermoml_parallel`)

Returns markdown with embedded `{...}` JSON sub-sections — one per query.
`_parse_parallel_sections(text)` splits on `---` boundaries, JSON-parses
each sub-section, formats via `_format_l1_block()`, and collects
`core_id_updates` from each sub-section's metadata.  Non-parseable sections
are kept as-is.

### ID updates

Both paths extract `compounds_found` and `properties_found` from the raw
result and merge them into the working memory's ID Catalog.

---

## 10. Phase Pipeline

| Phase | Name | Tools Used | Purpose |
|-------|------|------------|---------|
| 0 | Planning | `resolve_compounds`, `resolve_properties` | Identify systems, map names → IDs |
| 1 | Data Retrieval | `query_system_summary`, `query_blocks`, `inspect_block`, `find_similar_compounds`, `get_pure_values` | Understand data availability & structure |
| 2 | Fitting | `fit_block`, `fit_multi_system`, `compute_ideal_baseline`, `predict_from_rk` | Compute ideal baselines, excess properties, RK fit |
| 3 | Verdict | (automatic) | Independent quality review of fit results |

### 10b. Pre-Execution Guidance (Validation Chain)

Before `fit_block` executes, the anchor chain `SYNC_BATCH_PRE_VALIDATE` →
`SYNC_TOOL_GUIDANCE_CHECK` fires `FittingVariableGuidance`, which:

1. Checks if `property_type` is present; if not, infers it from
   `property_hint` and the resolved-properties catalog in working memory.
2. Fills missing `x_vars`, `y_props`, and `x_vars_constrained` with native
   arrays/objects derived from the selected block. It never serializes these
   values into JSON strings and never invents pure-component values.
3. Returns `""` (success, auto-filled) or a block message explaining
   which parameters are still missing so the LLM can self-correct.

This guidance is purely anchor-driven — `fit_block`'s `ToolEntry` has no
`guidance_fn` field.  The wiring lives in `hook_catalog.py` via
`bind_hook(fitting_pre_execution_guidance, SYNC_TOOL_GUIDANCE_CHECK)`.

---

## 10c. Sibling Delegation Architecture

`sibling_agent_delegation_tools/query_agent_tool.py` invokes the **full L0
query agent** as a peer (sibling) — unlike the L1 direct-dispatch tools in
`query_delegation_tools.py`, which bypass L0 and call L1 workers directly.

**Shared helpers** — all delegation plumbing is imported from
`general_db_query_engine.general_subagent_delegation_helpers`:

| Helper | Module | Purpose |
|--------|--------|---------|
| `SubagentSessionManager` | `_session_nesting.py` | Create per-run subdirectories under `<session_dir>/query_runs/` |
| `build_full_question` | `_question_builder.py` | Combine question + purpose/tasks/context into a structured prompt |
| `extract_run_result` | `_result_extractor.py` | Normalize `AnalysisRunResult` / `QueryRunResult` into a flat dict |
| `dispatch_parallel` | `_parallel_dispatch.py` | Run N queries via `ThreadPoolExecutor` (replaces inline pool code) |
| `merge_subagent_tracking` | `_tracking_combiner.py` | Merge subagent tracking MDs (stats, history) back into the parent session |

**Tracking merge-back** — after every query-agent call (single or parallel),
`merge_subagent_tracking()` copies the subagent's `run_history.md` and
`reference_stats.md` entries into the analysis session.  This was previously
missing and meant sibling-delegated query stats were lost.

**Parallel dispatch** — `run_query_agents_parallel` delegates to
`dispatch_parallel()` from the shared helpers instead of using an inline
`ThreadPoolExecutor`.  The helper handles JSON parsing, worker-pool
management, error collection, and per-task tracking merge-back.

---

## 11. Agent Budget Summary

| Layer | Model | Max Iters | Time Budget | Token Limit |
|-------|-------|-----------|-------------|-------------|
| L0 Orchestrator | claudeopus46 | 30 | 1200s (20 min) | 6000/call |
| L1 Data Retrieval | claudeopus46 | 12 | 240s (4 min) | 6000/call |
| L1 Fitting | claudeopus46 | 15 | 300s (5 min) | 6000/call |
| Verdict | claudeopus46 | 1 | 60s | 500/call |
| Tool Subagent | claudeopus46 | 1 | — | 500/call |

Time warnings at 65% / 85% / 95% of each layer's budget.

---

## 12. Observability & Run Diagnostics

Every run produces diagnostic files alongside the agent output:

| File | Generator | Sections |
|------|-----------|----------|
| `run_history.md` | `HistoryRecorder` | Chronological event log + Internal Errors table (if any) |
| `reference_stats.md` | `StatsRecorder` | 1) Argo Call Summary, 2) Data Complexity Summary, 3) DOI & Block References, 4) Tool Results, 5) Compaction Events, 6) Argo Call Detail Log |
| `reasoning_tokens_stripped.md` | `ReasoningTokenTracker` | Captured `<reasoning>` tokens for cost tracking |

The **Data Complexity Summary** (Section 2 of `reference_stats.md`) shows
the raw entity breadth the agent processed:
- Per-type tables of unique compounds, properties, variables, constraints
  (with num_id, name, and source tools)
- Aggregate counts: total unique entities, DOIs, blocks, data points

**Hook wiring:** Tool results go through `make_instrumented_wrapper()`
(from `memory_tool_result_instrumentation_helper.py`) which records to
working memory and passes structured dicts to the engine.
`AGENT_RECORD_REFERENCES` fires once per tool call from `react_loop.py`
(not from the wrapper — prevents double-counting).

**Internal errors:** Non-fatal errors (JSON parse failures, anchor
callback exceptions) are collected via `log_internal_error()` and
rendered as a table at the end of `run_history.md`.

---

## 13. Dependencies

**External:** NumPy, SciPy (ConvexHull), Matplotlib (Agg backend)

**Internal (sibling packages under `NIST_ThermoML_agents/`):**
- `general_argo_engine_helpers` — `ArgoClient` base class, `EngineConfig`, `react_loop`, `ArgoAgentTerminalUI`
- `general_tool_management_helpers` — `AgentToolCatalog`, `ToolEntry`, `CompactorCatalog`, `ToolResult`, `call_tool_subagent`
- `general_context_hooks` — `StatsRecorder`, `HistoryRecorder`, `TimeBudgetTracker`, `SelfCompactorInteractive`, `PostjobVerdictRunner`, `ContextCleanupCompactor`
- `general_memory_management_tools_hooks_helpers` — `SessionManager`, `WorkingMemoryBase`, `extract_entities_from_block_metadata`
- `general_subagent_delegation_helpers` — `SubagentSessionManager`, `build_full_question`, `extract_run_result`, `dispatch_parallel`, `merge_subagent_tracking`
- `general_db_search_tool_registry` — `db_search_tool_registry` (27 search tools)

**Cross-agent:**
- `NIST_ThermoML_query_agent.query_agent_workflows.L1_workers.l1_query_dispatcher` — L1 direct-dispatch query delegation target
- `NIST_ThermoML_query_agent.ThermoML_query_api.ThermoML_query_run` — full L0 sibling delegation target
