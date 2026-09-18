# Analysis Agent — Toolbox Customization Catalog

> Deviations from `general_tool_management_helpers/` defaults.
> Version 6.0 — 2026-04-08

---

## 1. L0 Tool Catalog → `AnalysisCatalog`

| Aspect | General Default (`AgentToolCatalog`) | Analysis Agent |
|--------|-------------------------------------|----------------|
| Subclass | `AgentToolCatalog` (base) | `AnalysisCatalog(AgentToolCatalog)` |
| `pipeline_label` | `""` (unset) | `"analysis"` |
| `PROTECT_TOOLS` | N/A | 4 fitting tools (`fit_block`, `fit_multi_system`, `compute_ideal_baseline`, `predict_from_rk`) exempt from LLM compaction |

### Registered Tools (14 + 1 runtime)

| Tool | Group | Compactor | `skip_subagent` | Notes |
|------|-------|-----------|-----------------|-------|
| `query_thermoml` | `query_delegation` | — | ✓ | `skip_compactor=True` — passes through raw text |
| `query_thermoml_parallel` | `query_delegation` | — | ✓ | `skip_compactor=True` |
| `align_compositions` | `query_delegation` | `compact_align_compositions` | ✓ | Dispatches the composition-alignment L1 agent |
| `run_query_agent` | `sibling_delegation` | — | ✓ | Full sibling Query-Agent run |
| `run_query_agents_parallel` | `sibling_delegation` | — | ✓ | Parallel sibling runs |
| `inspect_block` | `hardcoded_data` | `compact_inspect_block` | ✓ | Deterministic |
| `get_pure_values` | `hardcoded_data` | `compact_get_pure_values` | ✓ | Deterministic |
| `fit_block` | `fitting` | `compact_fit_block` | ✓ | PROTECTED; handles isotherm sweeps + multi-property shapes internally |
| `fit_block_derived` | `fitting` | `compact_fit_block_derived` | ✓ | Exact pointwise transform → RK fit |
| `fit_multi_system` | `fitting` | `compact_fit_multi_system` | ✓ | PROTECTED |
| `propose_fitting_plan` | `fitting` | `compact_propose_fitting_plan` | ✓ | Validate before fitting |
| `compute_ideal_baseline` | `fitting` | `compact_compute_ideal_baseline` | ✓ | PROTECTED |
| `predict_from_rk` | `fitting` | `compact_predict_from_rk` | ✓ | PROTECTED |
| `register_custom_block` | `custom_data` | `compact_register_custom_block` | ✓ | Fallback-only agent-built blocks |

**Extra compactors (not standalone tools):** Compactors from `resolve_tools.py`
and `discovery_tools.py` are registered as "extra compactors" for sub-step
result keys only.

**`list_session_files` tool** added at runtime by orchestrator (`group="session"`,
`skip_compactor=True`).

---

## 2. Key Deviation from Query Agent Tool Model

| Aspect | Query Agent | Analysis Agent | Why |
|--------|-------------|----------------|-----|
| L0 tool surface | 8 memory tools + 1 L1 dispatch | **10+ domain tools** (delegation, inspection, fitting, session) | Analysis L0 calls tools directly |
| Tier structure | L0 → L1 → L2 (3-tier catalogs) | **L0 only** (single catalog) | No sub-dispatchers |
| PROTECT_TOOLS | None | **6 fitting tools** | Deterministic numerical output — must not be LLM-compressed |
| Dynamic tools | `L1_query` registered at runtime via `L1AutoSaver` | `list_session_files` registered at runtime | Different dynamic tool pattern |
| Compactor skipping | L0 skip all; L2 skip all | query_delegation skip all; hardcoded skip subagent only; fitting use full pipeline | Per-group skip strategy |

---

## 3. Query Delegation Tools (analysis-specific)

| Function | Parameters | What It Does |
|----------|-----------|-------------|
| `query_thermoml` | `purpose, instruction, id_catalog, context` | Calls query agent's `dispatch_l1_query` directly |
| `query_thermoml_parallel` | `queries: list[dict]` | `ThreadPoolExecutor` → parallel exact query objects |

Both import `dispatch_query` from `L1_workers.l1_query_delegation`, which
wraps the query agent's L1 workers. Analysis never searches the database
directly — all search goes through the query agent.

---

## 4. Fitting Tools (entirely analysis-specific)

| Tool | Key Parameters | Saves |
|------|---------------|-------|
| `fit_block` | doi, block_number, property_hint, max_rk_order, mixing_rule, x_vars / y_props / x_vars_constrained | CSV + PNG to session dir; one fit per isotherm when constrained, per property via y_props |
| `fit_block_derived` | doi, block_number, transform, property_hint | Exact pointwise transform (e.g. density → molar volume) then RK fit |
| `fit_multi_system` | systems: list[dict] | Per-system via `ThreadPoolExecutor` |
| `propose_fitting_plan` | doi, block_number, x_vars, y_props, x_vars_constrained | Validated plan or objections (no fit) |
| `compute_ideal_baseline` | pure_values: dict, property_type, n_points | Deterministic ideal mixing curve |
| `predict_from_rk` | coeffs: list[float], pure_values: dict, n_points | Predict from existing RK coefficients |

All-in-one `fit_block` pipeline: extract → filter → ideal baseline → excess
property → RK fit. Handles `mixing_rule="both"` for dual-baseline comparison.

---

## 5. Hardcoded Data Tools (analysis-specific)

| Tool | Purpose | Notes |
|------|---------|-------|
| `inspect_block` | Deterministic block inspection: doi, block_type, compounds, variables, properties, constraints, column ranges | No LLM subagent |
| `get_pure_values` | Edge extraction of pure-component endpoints: pure_values, edge_coverage, temperature, pressure | Deterministic |

Both marked `skip_subagent=True` — their output is deterministic dicts
that only need dict→markdown hardcoded compaction.

---

## 6. Compactors (15 analysis-specific)

**Resolve (sub-step keys):** `compact_resolve_compounds`, `compact_resolve_properties`

**Discovery (sub-step keys):** `compact_query_system_summary`, `compact_query_blocks`,
`compact_inspect_block`, `compact_find_similar_compounds`, `compact_get_pure_values`

**Fitting & alignment:** `compact_fit_block` (handles single + dual baseline,
includes BIC table, RK coefficients, R², RMSE, output paths),
`compact_fit_block_derived`, `compact_fit_multi_system`,
`compact_propose_fitting_plan`, `compact_compute_ideal_baseline`,
`compact_predict_from_rk`, `compact_align_compositions`,
`compact_register_custom_block`

**No sharing** with query agent compactors — each agent has its own
parallel set in its `compactor_hooks/` directory.
