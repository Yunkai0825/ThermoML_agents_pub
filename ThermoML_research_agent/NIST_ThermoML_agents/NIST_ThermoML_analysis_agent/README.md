# NIST_ThermoML_analysis_agent — Thermodynamic Fitting Agent

Multi-phase pipeline for thermodynamic postprocessing: planning →
data retrieval (via query agent delegation) → Redlich-Kister fitting →
independent verdict review.  Never touches the database directly.

---

## Quick Start

```python
from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent import ThermoML_analysis_run

result = ThermoML_analysis_run("Fit excess enthalpy of ethanol-water at 298 K")
print(result.answer)
```

---

## Public API

| Function | Returns | Description |
|----------|---------|-------------|
| `ThermoML_analysis_run(question, run_verdict=True)` | `AnalysisRunResult` | Single entry point — wraps `orchestrator.run()` |

### AnalysisRunResult

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

---

## Configuration

| Parameter | Value |
|-----------|-------|
| Max iterations | 30 |
| Wall-clock budget | 20 min |
| LLM | Claude Opus 4.6 |
| PROTECT_TOOLS | Fitting tools (exempt from LLM compaction) |
| L1_DATA cap | 12 iter / 6 min |
| L1_FIT cap | 15 iter / 5 min |
| VERDICT_MAX_TOKENS | 2000 |

---

## Pipeline Phases

| Phase | Role | Key Tools |
|-------|------|-----------|
| 0 — Planning | Understand question, identify systems | — |
| 1 — Data Retrieval | Delegate DB search to query agent | `query_thermoml()`, `query_thermoml_parallel()` |
| 2 — Fitting | RK fitting, ideal baseline, nonideality | `fit_block()`, `fit_multi_system()`, `compute_ideal_baseline()` |
| 3 — Verdict | Independent review of fit quality | verdict hooks |

### Working Memory Formatting

Query tool results are automatically formatted before storage in working
memory via `_format_l1_block()` (single queries) and
`_parse_parallel_sections()` (parallel queries).  Raw JSON is never stored.
Missing datapoint counts show as "-".  Entity IDs are extracted and merged
into the protected ID Catalog.

### Arrhenius Fitting

For transport properties (viscosity), the fitting pipeline uses Arrhenius
mixing: `Y_ideal = exp(x₁·ln(Y₁*) + x₂·ln(Y₂*))`.  The excess property
is computed in log space: `y_excess = ln(Y_meas) - ln(Y_ideal)`.
After RK fitting, the back-transform `Y_fitted = exp(ln(Y_ideal) + y_excess_fitted)`
recovers physical units.  CSV columns are labelled `ln_excess_{property}`
to reflect the fitted quantity.

---

## Tool Groups

| Group | Source | Notes |
|-------|--------|-------|
| Query delegation | `query_delegation_tools.py` | Wraps query agent L1 workers; `id_catalog` entries are typed (`comp`, `prop`, `var`, `constr`, `meas`, `phase`, `lit`, `blocktype`, `solvent`) and invalid types are rejected with the full valid list |
| Sibling delegation | `sibling_agent_delegation_tools/query_agent_tool.py` | Full query-agent runs (single + parallel) via the shared delegation helpers; children land in `<session>/query_runs/run_N/` with combined tracking merged at the parent root (`preserve_active_session` guards the session `ContextVar`) |
| Hardcoded data | `hardcoded_data_tools.py` | Deterministic lookups — skips subagent compaction |
| Fitting | `fitting_tools.py` | RK fitter, ideal baseline, prediction. Protected from compaction. Unified `fit_block` auto-detects single/multi-property/by-temperature mode |
| Resolve | `resolve_tools.py` | ID/name resolution |
| Discovery | `discovery_tools.py` | Data discovery |

### Pre-Execution Guidance

`FittingVariableGuidance` (bound to `SYNC_TOOL_GUIDANCE_CHECK` via anchor
dispatch) auto-fills native `x_vars`, `y_props`, and `x_vars_constrained`
values before `fit_block` executes. It does not infer endpoint values. If
required parameters are still missing after
auto-fill, the tool call is blocked and the LLM receives a guidance
message explaining what it needs to provide.

---

## Core Calculation Library

Shared pure-computation modules under `ThermoML_core_calc_tools/`:

| Subpackage | Purpose |
|-----------|---------|
| `Redlich_Kister_block_fitting/` | `auto_fit_redlich_kister()`, `eval_redlich_kister()` |
| `mixture_nonideality_calc/` | `build_ideal_baseline()`, `compute_excess_property()` |
| `csv_io_helpers/` | `extract_block_arrays()`, `identify_columns()` |
| `output_helpers/` | `save_fit_csv()`, `save_fit_plot()`, `save_excess_csv()` |
| `topology_helpers/` | Mixture topology utilities |

---

## Package Layout

```
NIST_ThermoML_analysis_agent/
├── ThermoML_analysis_api.py            # Public entry point
├── ThermoML_analysis_argo_config.py    # Config dataclass
├── analysis_agent_workflows/
│   ├── L0_orchestrator/                # orchestrator.run() + L0_analysis_workflow.md
│   ├── L1_workers/                     # Data retrieval + fitting sub-phases
│   └── _subworkflow_md_parser/         # parse_workflow(), render_prompt()
├── analysis_agent_toolbox/
│   ├── tool_catalog.py                 # AnalysisCatalog
│   ├── query_delegation_tools.py       # query_thermoml, query_thermoml_parallel
│   ├── fitting_tools.py               # RK fitting tools (PROTECTED)
│   ├── hardcoded_data_tools.py
│   ├── resolve_tools.py
│   ├── discovery_tools.py
│   ├── agent_specific_tools/
│   └── sibling_agent_delegation_tools/
├── analysis_agent_argo_engine/         # LLM client + terminal UI
├── analysis_agent_context_hooks/
│   ├── hook_catalog.py                 # build_engine_hooks()
│   ├── compactor_hooks/
│   ├── interactive_hooks/
│   ├── memory_hooks/
│   ├── reminder_hooks/
│   ├── tracking_hooks/
│   └── verdict_hooks/
├── analysis_agent_heath_check_helpers/
└── ThermoML_core_calc_tools/           # Pure computation library
```

---

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full wiring diagram.
