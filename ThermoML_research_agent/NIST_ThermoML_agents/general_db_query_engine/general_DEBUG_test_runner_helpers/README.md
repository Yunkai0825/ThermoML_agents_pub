# Shared benchmark runner helpers

These helpers support the per-agent `_DEBUG_script/run_tests.py` entrypoints.
Live prompt runs call the public agent APIs and require a configured provider.
The helpers themselves also support offline tests with mocked agent calls.

| Export | Purpose |
|---|---|
| `parse_prompts_simple` | Read prompt ID/text pairs for Main and Analysis |
| `parse_prompts_with_sections` | Read structured prompt records for Query |
| `run_sequential`, `run_parallel` | Execute supplied `(prompt_id, prompt)` callbacks and completion callbacks |
| `setup_run_log`, `teardown_run_log` | Manage a campaign's `run_log.txt` handler |

Each runner declares its default campaign directory directly under the workspace
root: `_benchmark/Main`, `_benchmark/Query`, or `_benchmark/Analysis`. The
`--output` argument selects a custom campaign directory. Main and Analysis pass
`<campaign>/Q<prompt_id>` as the explicit agent `session_dir`; Query supplies its
memory path within the same per-prompt layout. Nested subagent files remain
inside that prompt session.

The shared helpers do not decide provider credentials or freeform output paths.
Freeform sessions are owned by each agent config or terminal UI under the shared
`_output/<Agent>` directory. Use the public `ThermoML_*_api.py` functions for Python
integration and the workspace documentation for benchmark commands.
