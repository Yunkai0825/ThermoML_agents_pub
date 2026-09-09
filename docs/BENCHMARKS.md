# Benchmarks and recorded runs

This workspace includes live-agent benchmark runners, their prompt files, deterministic regression tests, and historical run artifacts. These serve different purposes: the live runners record agent behavior on chemistry tasks; offline tests check implementation contracts. No new live API runs or benchmark performance measurements were produced while preparing this guide.

## Prompt sets and current launcher selection

The [combined launcher](../ThermoML_research_agent/run_debug_benchmark.py) invokes the existing Main, Query, and Analysis runners in that order. One agent phase finishes before the next begins; prompts within a phase can run concurrently.

| Agent | Prompt file | Parsed cases | Combined-launcher behavior |
|---|---|---:|---|
| Main | [test_prompts.md](../ThermoML_research_agent/NIST_ThermoML_agents/_NIST_ThermoML_main_agent/_DEBUG_script/test_prompts.md) | 21 | Explicit `MAIN_IDS` filter; currently 16 matching cases, 3 workers, 12-second minimum start gap |
| Query | [test_prompts.md](../ThermoML_research_agent/NIST_ThermoML_agents/NIST_ThermoML_query_agent/_DEBUG_script/test_prompts.md) | 28 | All cases, 5 workers, 6-second minimum start gap |
| Analysis | [test_prompts.md](../ThermoML_research_agent/NIST_ThermoML_agents/NIST_ThermoML_analysis_agent/_DEBUG_script/test_prompts.md) | 18 | All cases, 5 workers, 6-second minimum start gap |

Counts were obtained from the repository's actual prompt parsers on 2026-09-09. Main covers direct retrieval/fitting, multi-step tasks, context-rich questions, and edge cases. Query covers lookups, comparisons, dependent retrieval, open goals, ambiguous questions, and out-of-scope requests. Analysis covers binary fits, ternary estimation, similarity/data gaps, property-specific tasks, open goals, and edge cases.

**Current Main selection mismatch:** `MAIN_IDS` contains 17 strings, including `3.4`, but the prompt file has no `3.4`; it contains `4.4`, which is not selected. The Main runner silently filters unknown IDs, so the effective default cohort is 16. The source list is:

```text
1.1.2 1.1.4 1.2.1 1.2.2
2.1 2.2 2.3 2.4 2.5 2.6
3.1 3.2 3.3 3.4
4.1 4.2 4.3
```

The four `1.1.1`, `1.1.3`, `1.2.3`, and `1.2.4` cases are also excluded by that explicit cohort. This documentation does not change the selection or treat the missing `3.4` as an executed experiment. Calling the Main runner without an ID filter selects all 21 current prompts, which is a different cohort.

## Inspect configuration before a run

From the repository root:

```bash
python ThermoML_research_agent/run_debug_benchmark.py --offline
```

This checks imports/configuration and prints the planned commands without credentials, network probes, or agent runs. Without `--offline`, preflight additionally checks service identity and endpoint reachability; it still does not launch the prompt batch unless `--go` is present.

After following the [installation/API setup instructions](../README.md), the live commands are:

```bash
python ThermoML_research_agent/run_debug_benchmark.py --go
python ThermoML_research_agent/run_debug_benchmark.py --go --anthropic
```

The first uses the configured Argo backend. The second uses the [Anthropic bootstrap](../ThermoML_research_agent/_anthropic_adapter_bootstrap.py) and adapter with `ANTHROPIC_API_KEY`. It retains the selected prompts and runner settings while mapping model names through the adapter. These commands perform billable/external model calls. Account identity configures the API, not a per-user output directory. There is no application user-role restriction on running the benchmark.

`--offline` cannot be combined with `--go`. The wrapper does not forward arbitrary prompt IDs, `--section`, `--workers`, `--gap`, or `--output`; use a per-agent runner when changing those settings.

## Run a smaller or custom cohort

From `ThermoML_research_agent`:

```bash
python -m NIST_ThermoML_agents.NIST_ThermoML_query_agent._DEBUG_script.run_tests 1.1 --workers 1
python -m NIST_ThermoML_agents.NIST_ThermoML_query_agent._DEBUG_script.run_tests --section 2 --workers 2 --gap 6
python -m NIST_ThermoML_agents._NIST_ThermoML_main_agent._DEBUG_script.run_tests 1.1.2 --workers 1
python -m NIST_ThermoML_agents.NIST_ThermoML_analysis_agent._DEBUG_script.run_tests 1.1 --workers 1
```

Each runner accepts positional prompt IDs and `--section`, `--workers`, `--gap`, `--output`, and `--skip-existing`. Positional IDs take precedence over a section filter. Inspect the runner's `--help` for its defaults; the Main runner defaults to one worker, unlike the combined launcher's three. `--gap` controls spacing between starts in parallel mode, not a model timeout or response deadline.

Current runner sources: [Main](../ThermoML_research_agent/NIST_ThermoML_agents/_NIST_ThermoML_main_agent/_DEBUG_script/run_tests.py), [Query](../ThermoML_research_agent/NIST_ThermoML_agents/NIST_ThermoML_query_agent/_DEBUG_script/run_tests.py), and [Analysis](../ThermoML_research_agent/NIST_ThermoML_agents/NIST_ThermoML_analysis_agent/_DEBUG_script/run_tests.py).

## Output layout

The combined launcher uses a shared timestamp and explicit paths:

```text
_benchmark/
  Main/test_run_<YYYYMMDD_HHMMSS>/
  Query/test_run_<YYYYMMDD_HHMMSS>/
  Analysis/test_run_<YYYYMMDD_HHMMSS>/
```

Standalone runners use the same per-agent benchmark roots by default. `--output` explicitly overrides the batch destination. Freeform interactive/API runs use the separate shared `_output` tree. Nested agent sessions, numerical files, and prompt traces may add further subdirectories to the selected run.

| Artifact | Main / Analysis batch | Query batch |
|---|---|---|
| Answer/result | `Q<id>_result.md` | `Q<id>/result.md` |
| Tool history | `Q<id>_history.md` | `Q<id>/tool_trace.md` |
| Context/history detail | Optional `Q<id>_final_context.md` plus session files | `Q<id>/working_memory.md`, `run_history.md`, and available session files |
| Batch summary | `TEST_SUMMARY_<timestamp>.md` | Same |
| Structured batch trace | `TEST_TRACE_<timestamp>.json` | Same |
| Log | Per-run log written by shared orchestration helpers | Same |

Results can include answer text, elapsed time, iteration counts, tool history, errors/timeouts, final context, and Main verdict information. Session artifacts can include `data/`, `plots/`, grounding evidence, workflow records, and a file catalog. Anthropic mode additionally configures raw-response capture as `anthropic_raw_capture.jsonl` at the phase destination; existing session archives may have their own captures.

## Resume and result interpretation

To resume a combined batch, reuse its timestamp, for example:

```bash
python ThermoML_research_agent/run_debug_benchmark.py --go --resume 20260909_150000
python ThermoML_research_agent/run_debug_benchmark.py --go --anthropic --resume 20260909_150000
```

Replace the example timestamp with an actual `test_run_<timestamp>` directory suffix and use the same backend/configuration. The wrapper reuses each phase directory and passes `--skip-existing`.

Resume is **file-existence based**. Main/Analysis skip a case if `Q<id>_result.md` exists; Query skips it if `Q<id>/result.md` exists. That includes recorded failures; it does not mean the case succeeded. To intentionally retry an error without altering a historical run, use the relevant runner with explicit IDs and a new output directory. Resume skips work; it does not reconstruct or re-execute a prior in-memory conversation.

Each new invocation writes summaries/traces for the cases it actually executes. A resumed directory can therefore contain multiple trace files covering different subsets. A latest trace alone is not necessarily a report for the complete cohort, and skipped results are not merged into that new trace. Compare prompt IDs across the artifacts before aggregating results.

The [status writer](../ThermoML_research_agent/NIST_ThermoML_agents/general_db_query_engine/general_hooks_management_helpers/general_tracking_hooks_output_helpers/output_writers.py) labels a result `ERROR` if its error field is populated or its answer contains uppercase `ERROR`; otherwise it uses the timeout flag and then `OK`. These are operational labels, not an independently scored chemistry accuracy metric. Reported concurrency “speedup” compares the sum of prompt durations with batch wall time; it is not a controlled comparison to a separately measured sequential run.

The combined launcher stops if a phase subprocess exits nonzero, no trace is found, every recorded result is an error/timeout, or at least 90% of five or more recorded results are errors/timeouts. This catches broad execution failures; it does not assess whether apparently successful answers are scientifically correct.

## Included historical artifacts

The inspected [_benchmark directory](../_benchmark) contains:

| Directory | Observed historical contents |
|---|---|
| [Main](../_benchmark/Main) | 24 `run_*` session folders dated 2026-08-15 through 2026-09-05; no top-level `test_run_*` batch folder |
| [Query](../_benchmark/Query) | `test_run_20260905_021947`, containing two timestamped batch traces |
| [Analysis](../_benchmark/Analysis) | 18 `run_*` session folders plus `test_run_20260905_021947`, containing three timestamped batch traces |
| [_cost_audit](../_benchmark/_cost_audit) | Cost-audit script, CSVs, figures, and Origin-related artifacts |

These are migrated records from earlier executions, not results of running today's source revision during publication preparation. Historical files can retain previous absolute paths, model names, runtime settings, and older directory conventions. A `run_*` session is not a `test_run_*` batch and cannot be passed as a batch timestamp to `--resume`.

The [cost-audit script](../_benchmark/_cost_audit/thermoml_cost_audit.py) and generated tables describe their own inputs and estimation choices. They are not current provider price quotations or fresh performance claims in this documentation.

## Reproducibility record

For a reportable run, retain the code revision, exact prompt IDs and prompt-file revision, backend/model mapping, numerical and agent configuration, database sizes/metadata or checksums, worker count and start gap, timestamped outputs, and any resume/retry history. Account credentials are not part of that record. The [data guide](DATA.md) identifies the included corpus and generated artifacts.

Deterministic tests under parser, search-tool, browser, and property-screening `tests` directories exercise code/data contracts and simulate model branches where needed. Their pass counts should be reported as software validation separately from a live-agent evaluation. Neither the existing traces nor operational `OK` labels alone establish an accuracy, quality, latency, or cost benchmark for the current code.
