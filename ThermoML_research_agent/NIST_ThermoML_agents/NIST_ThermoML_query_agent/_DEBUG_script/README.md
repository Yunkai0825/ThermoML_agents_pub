# Query prompt benchmark

[run_tests.py](run_tests.py) executes the prompts in [test_prompts.md](test_prompts.md)
through the Query agent's public API. These are live end-to-end benchmarks and
require configured provider access. Offline regression checks are separate.

## Running

From `ThermoML_research_agent/`:

```powershell
# All prompts, five workers with the default start spacing.
python -m NIST_ThermoML_agents.NIST_ThermoML_query_agent._DEBUG_script.run_tests

# Sequential execution of selected prompts.
python -m NIST_ThermoML_agents.NIST_ThermoML_query_agent._DEBUG_script.run_tests 1.1 2.1 --workers 1

# One section, custom pacing, and a custom campaign directory.
python -m NIST_ThermoML_agents.NIST_ThermoML_query_agent._DEBUG_script.run_tests --section 3 --workers 3 --gap 10 --output ../_benchmark/Query/custom_campaign
```

Direct execution of this directory's `run_tests.py` is also supported. `--output`
is interpreted relative to the launch directory when given a relative path.
Use `--help` for all options and `--skip-existing` to skip prompts with saved results.

## Output structure

Default output is `_benchmark/Query/test_run_<timestamp>/` at the workspace root:

```text
test_run_<timestamp>/
├── Q1.1/
│   ├── result.md
│   ├── tool_trace.md
│   ├── run_history.md
│   ├── working_memory.md
│   └── workflow/             # Root-session workflow figures and audits
├── Q2.1/
├── TEST_SUMMARY_*.md
├── TEST_TRACE_*.json
└── run_log.txt
```

Additional tracking/context files depend on the run. Results and traces are written
per prompt as execution finishes. Full sessions, memory files and reports stay
inside the selected campaign; freeform Query runs use `_output/Query/` instead.

The [shared benchmark helpers](../../general_db_query_engine/general_DEBUG_test_runner_helpers/README.md)
provide parsing, scheduling, logs and callback dispatch.
