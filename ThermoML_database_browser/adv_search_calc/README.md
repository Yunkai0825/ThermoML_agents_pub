# Browser analysis tools

The [Analysis page](../README.md) runs deterministic calculations locally. These
functions reuse modules from the research agents without invoking an LLM.

## Dispatcher

[analysis_dispatcher.py](analysis_dispatcher.py) provides
`dispatch(tool, **kwargs)` and `get_tool_definitions()`. Tool metadata defines
the settings panels and whether custom CSV input is supported.

| Tool ID | Function | Input / behavior |
|---|---|---|
| `nonideality` | `run_nonideality()` | Columns/rows or custom CSV; ideal baselines, deviations, RK fit, and classification |
| `rk_fitting` | `run_rk_fitting()` | Database block; NumPy-based RK fitting with BIC order selection |
| `inspect` | `run_inspect()` | Database block; structure, columns, ranges, and metadata |
| `pure_values` | `run_pure_values()` | Database block; pure-component estimates from composition edges |

`run_*` arguments are keyword-only. Database tools use a DOI and typed
`block_number` (`PROPblock_*` or `RXNblock_*`), with an optional `BLKsubsys_id` for
an exact subsystem. Do not substitute raw numeric ordinals for these IDs.

The `/analysis/run` route accepts `mode="block"` with those fields, or
`mode="custom"` with `csv_text` for nonideality analysis. The browser sends
per-tool controls in the `settings` object. The dispatcher returns dictionaries
suitable for JSON responses.

`_ensure_core()` lazily imports NumPy and research calculation modules. Install
the full [browser runtime requirements](../requirements.txt); a missing or broken
core dependency is reported by the affected tool.

## Local nonideality calculator

[nonideality.py](nonideality.py) implements the quick calculator without NumPy.
It detects mole-fraction, volume, and viscosity columns, builds linear volume
or logarithmic viscosity baselines, fits RK polynomials with Gaussian
elimination, and classifies the resulting deviations.

Entry points are `analyze_block(columns, rows, ...)`,
`analyze_custom_csv(csv_text)`, and `result_to_dict(result)`. Result classes are
`DeviationPoint`, `FitResult`, `PropertyAnalysis`, and `AnalysisResult`.
