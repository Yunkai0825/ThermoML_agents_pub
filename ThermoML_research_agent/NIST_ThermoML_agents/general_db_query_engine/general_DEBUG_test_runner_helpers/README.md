# Shared prompt benchmark helpers

This package provides parsing, scheduling and log handling for the three agents'
`_DEBUG_script/run_tests.py` benchmark entrypoints. The runners call the same
public APIs used by freeform requests. The directory name identifies the test
infrastructure; it does not enforce a user or production-access restriction.

## Exported interfaces

| Module | Exports |
|---|---|
| [DEBUG_test_prompt_parser.py](DEBUG_test_prompt_parser.py) | `parse_prompts_simple`, `parse_prompts_with_sections` |
| [DEBUG_test_orchestration.py](DEBUG_test_orchestration.py) | `RateLimiter`, `run_sequential`, `run_parallel`, `setup_run_log`, `teardown_run_log` |

`parse_prompts_simple(path)` returns `(prompt_id, prompt_text)` pairs for Main and
Analysis. `parse_prompts_with_sections(path)` returns dictionaries for Query,
including section metadata. The actual prompt files are named `test_prompts.md`.

The scheduling helpers accept a `run_fn(prompt_id, prompt_text) -> dict` callback.
`run_parallel` applies shared start-time spacing across its workers;
`run_sequential` optionally waits between completed prompts. An `after_fn` callback
can persist each result as soon as it finishes.

```python
from NIST_ThermoML_agents.general_db_query_engine.general_DEBUG_test_runner_helpers import (
    parse_prompts_simple,
    parse_prompts_with_sections,
    run_sequential,
    run_parallel,
)
```

Result Markdown, history, summaries and JSON traces are written by
[general_tracking_hooks_output_helpers](../general_hooks_management_helpers/general_tracking_hooks_output_helpers/README.md).
The concrete runners bind these writers and pass explicit per-prompt session paths.

## Run a benchmark

From `ThermoML_research_agent/`:

```powershell
# Check imports and configuration without contacting an LLM provider.
python run_debug_benchmark.py --offline

# Live Main, Query and Analysis prompt suites.
python -m NIST_ThermoML_agents._NIST_ThermoML_main_agent._DEBUG_script.run_tests --workers 1
python -m NIST_ThermoML_agents.NIST_ThermoML_query_agent._DEBUG_script.run_tests 1.1 2.1 --workers 1
python -m NIST_ThermoML_agents.NIST_ThermoML_analysis_agent._DEBUG_script.run_tests --section 2
```

Live calls require configured provider access. All three runners accept `--output`,
`--workers`, `--gap`, and `--skip-existing`; `--help` shows their defaults.
The combined `run_debug_benchmark.py --go` launcher sequences the suites and
supports `--resume <timestamp>` and `--anthropic`.

## Output layout

The default campaign path is `_benchmark/<Agent>/test_run_<timestamp>/` at the
workspace root. Full sessions are saved in `<campaign>/Q<prompt_id>/`.
A custom `--output` supplies the campaign directory, including its full sessions.

Main and Analysis also write flat `Q<id>_result.md`, `Q<id>_history.md`, and optional
`Q<id>_final_context.md` reports in the campaign directory. Query writes its result
and tool trace within each `Q<id>/` directory. Campaign-level `TEST_SUMMARY_*.md`,
`TEST_TRACE_*.json`, and the run log support review and resumption.

`--skip-existing` checks the appropriate completed-result files for each runner.
Freeform output is separate under the shared `_output/<Agent>/` directory.
See the [agent README](../../README.md) for the public API and output contract.
