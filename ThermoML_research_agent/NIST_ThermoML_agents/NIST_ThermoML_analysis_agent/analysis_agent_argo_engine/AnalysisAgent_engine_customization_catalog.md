# Analysis Agent — Engine Customization Catalog

> Deviations from `general_argo_engine_helpers/` defaults.
> Version 6.0 — 2026-04-08

---

## 1. ArgoClient Subclass → `AnalysisClient`

| Aspect | General Default (`ArgoClient`) | Analysis Agent Override |
|--------|-------------------------------|------------------------|
| Subclass | `ArgoClient` (dataclass) | `AnalysisClient(ArgoClient)` |
| Field defaults | No defaults on base | **Baked-in defaults** from `cfg` on class body (`model`, `temperature`, `top_p`, `max_tokens`) |
| Base factories inherited | `with_tier()`, `for_verdict()`, `for_compactor()`, `for_planner()` | All 4 inherited unchanged |

### Added Factory Methods

| Factory | Model | Tier Label | Purpose |
|---------|-------|------------|---------|
| `for_l0()` | `cfg.MODEL` | `"L0-main"` | L0 orchestrator |
| `for_l1_data()` | `cfg.L1_MODEL` | `"L1-subagent"` | L1 data retrieval (query delegation) |
| `for_l1_fit()` | `cfg.L1_MODEL` | `"L1-fit"` | L1 fitting workers |

**Key difference from query agent:** Two L1 tiers (`data` vs. `fit`) instead
of one. No L2 tier — analysis does not use leaf evaluators.

---

## 2. Import-Time `load_config()`

Identical pattern to query agent: `__init__.py` calls `load_config(AGENT_CONFIG)`
at import time, setting the global singleton to `AnalysisAgentConfig`.

---

## 3. Terminal UI → `AnalysisAgentTerminalUI`

| Aspect | Query Agent | Analysis Agent | Why |
|--------|-------------|----------------|-----|
| `agent_name` | `"ThermoML Query Agent"` | `"ThermoML Analysis Agent"` | Branding |
| `run_agent()` | No `run_verdict` param | Always passes `run_verdict=True` | Verdict is part of analysis pipeline |
| `display_result()` | No verdict, `getattr` for fields | **Displays verdict section** with separator; shows `session_dir`; uses `result.round_number` | `AnalysisRunResult` has richer structure |
| `on_after_run()` | Not overridden (base no-op) | **Explicit no-op** — keeps session alive across continuation rounds | Multi-round persistence |

---

## 4. EngineConfig → `AnalysisAgentConfig`

### 4a. Base Fields That DIFFER from Query Agent

| Field | Query Agent | **Analysis Agent** | Why |
|-------|-------------|-------------------|-----|
| `MAX_TOOL_ITERATIONS` | 25 | **30** | Fitting pipelines: inspect → get_pure → fit × N systems |
| `MAX_TURN_SECONDS` | 1000 (17 min) | **1200** (20 min) | Multi-phase: query → inspect → fit → verdict |
| `VERDICT_MAX_TOKENS` | 500 | **2000** | Verdict reviews fit quality (R², BIC, overfitting) |

All other 23 base fields are **identical** to query agent.

### 4b. Analysis-Agent-Only Extra Fields

| Field | Value | Differs from Query? | Purpose |
|-------|-------|---------------------|---------|
| `L1_MODEL` | `"claudeopus46"` | Same value | L1 model |
| `SUBAGENT_MAX_TOKENS` | **500** | Query: 700 | Tool results are more structured dicts |
| `L1_DATA_MAX_ITERATIONS` | **12** | Query: single `L1_MAX_ITERATIONS=12` | Split L1 budgets |
| `L1_DATA_MAX_SECONDS` | **360** | Query: single `L1_MAX_SECONDS=360` | |
| `L1_FIT_MAX_ITERATIONS` | **15** | Not in query | Fitting needs more iterations |
| `L1_FIT_MAX_SECONDS` | **300** (5 min) | Not in query | But less wall-clock |
| `MAX_RETRY` | **3** | Query: 5 | Fewer compaction retries — structured results |
| `COMPACTION_INTERVAL` | **9999** | Query: `L1_COMPACTION_INTERVAL=999` | Renamed; turn-based compaction disabled — size trigger governs |
| `VERDICT_SOLVER_CHARS` | **3,000** | Not in query | Solver trace in verdict |
| `VERDICT_ANSWER_CHARS` | **4,000** | Not in query | Full answer in verdict |
| `VERDICT_FORMAT_MAX_TOKENS` | **800** | Not in query | Formatting LLM call |
| `PROTECT_TOOLS` | `{fit_block, fit_multi_system, predict_from_rk, compute_ideal_baseline}` | Query: not present | **4 fitting tools exempt from LLM compaction** |
| `OUTPUT_DIR` | `_PROJECT_ROOT / "_outputs_user/<bucket>/<DB>/<Agent>/Diagnostics"` | Not in query | Session artifact storage |
| `TRANSCRIPT_DIR` | `_PROJECT_ROOT / "transcripts"` | Not in query | Full conversation transcripts |

### 4c. Fields NOT in Analysis (present in Query)

| Field | Query Value | Why absent |
|-------|-------------|-----------|
| `L2_MODEL` | `"claudeopus46"` | No L2 tier |
| `L2_MAX_TOKENS` | `2000` | No L2 tier |
| `BLOCK_CONDENSE_LIMIT` | `10,000` | Inspects blocks deterministically, no condensation |

### 4d. Module-Level Domain Constants

| Constant | Value | Purpose |
|----------|-------|---------|
| `RK_MAX_ORDER` | `5` | Max Redlich-Kister polynomial order |
| `RK_MIN_DATAPOINTS` | `5` | Minimum data points for fitting |
| `IDEAL_BASELINE_PROPS` | `["molar_volume", "density", "viscosity", "refractive_index", "speed_of_sound"]` | Properties with ideal-solution baselines |
| `ARRHENIUS_PROPS` | `["viscosity"]` | Properties fitted in log space |
