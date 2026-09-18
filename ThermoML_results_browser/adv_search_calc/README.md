# adv_search_calc — Analysis Tools & Calculators

Browser-side analysis layer.  Wraps agent core calculation modules
for interactive use from the analysis page.

## Files

| File | Purpose |
|------|---------|
| `analysis_dispatcher.py` | 4-tool dispatcher + metadata for UI settings panels |
| `nonideality.py` | Pure-Python non-ideality calculator (no numpy) |
| `__init__.py` | Package init |

## analysis_dispatcher.py

### Tool Definitions

`TOOL_DEFINITIONS` — list of dicts consumed by `analysis.html` to render
per-tool settings cards.  Each entry carries:
- `id`, `name`, `description`, `icon`
- `settings` — list of UI controls (select, number, checkbox) with
  defaults & options

### Dispatcher Functions

| Function | Description |
|----------|-------------|
| `dispatch(tool, **kwargs)` | Route to the correct `run_*` function |
| `run_nonideality(columns, rows, ...)` | Excess property deviations + RK fit |
| `run_rk_fitting(doi, block_number, ...)` | BIC order selection, coefficients |
| `run_inspect(doi, block_number, ...)` | Raw block structure dump |
| `run_pure_values(doi, block_number, ...)` | Pure-component value extraction |
| `classify_excess(y_excess, x_vals, ...)` | Deviation classification helper |
| `get_tool_definitions()` | Return `TOOL_DEFINITIONS` for the UI |

### Lazy Loading

`_ensure_core()` imports numpy and the agent core calc modules on first
call, keeping startup fast and optional when numpy is unavailable.

## nonideality.py

Zero-dependency fallback calculator (no numpy required).

- Auto-detects mole-fraction, volume, and viscosity columns
- Computes ideal baselines (linear volume, log-mixing viscosity)
- Fits Redlich-Kister polynomials via Gaussian elimination
- Classifies deviations as attractive / repulsive / mixed

Key classes: `DeviationPoint`, `FitResult`, `PropertyAnalysis`, `AnalysisResult`.
Entry point: `analyze_block(columns, rows, ...)`.
