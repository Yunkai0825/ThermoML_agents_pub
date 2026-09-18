# Benchmarks and saved outputs

[Documentation home](../README.md) · [Development](DEVELOPMENT.md)

Benchmarks write under project-root `_benchmark/{Main,Query,Analysis}`.
Freeform sessions write under `_output`; the browser lists these separately.
Existing benchmark ZIPs contain migrated records, not new evaluation results.
The browser reads the archives directly without extracting files. Within each
agent directory, `test_run_ledgered_20260905.zip` stores full-framework runs and
`test_run_no_ledger_20260905.zip` stores no-ledger runs. Query's additional mode
collections retain their collection names with a `.zip` extension. Each agent
keeps its own browser tab and mode columns.

The Main and Analysis full-framework ZIPs are distributed as unchanged
[release assets](INSTALLATION.md#download-the-release-assets). Download
`Main_test_run_ledgered_20260905.zip` and `Analysis_test_run_ledgered_20260905.zip`,
then place them as `test_run_ledgered_20260905.zip` under `_benchmark/Main/` and
`_benchmark/Analysis/`, respectively. Their asset prefixes prevent filename
collisions and do not change their contents. Keep them compressed. The remaining
supplied benchmark ZIPs are stored directly in Git.

## Example folder names

Run folders sit directly at the ZIP root. Saved Main and Analysis examples use
`Q<id>_run_<YYYYMMDD_HHMMSS>`, for example `Q5.4_run_20260905_120350`. IDs follow the current prompt catalog. The short
timestamp distinguishes repeated examples, and the old random hash is omitted.
Query campaign examples use `Q<id>` or a prompt ID followed by a run timestamp.
Archived collection contents retain their saved filenames.

The folders themselves carry the current benchmark IDs, and the browser reads
those names directly. Historical prompt text and recorded IDs remain inside the
run artifacts. Two older synthetic-compound error tests use earlier prompt
wording: Main `4.1` and Analysis `6.2` originally asked about unobtainium.

## Commands

From the project root:

```shell
python ThermoML_research_agent/run_debug_benchmark.py --offline
```

This is the local import/configuration preflight and run plan. It must not be
used as evidence that provider credentials or scientific responses work.
To deliberately launch the configured live suites:

```shell
python ThermoML_research_agent/run_debug_benchmark.py --go
```

The batch launcher has a selected Main cohort and the Query/Analysis selections
declared in its source. Use its printed plan and the current prompt files when
reporting selected cases. Do not infer the cohort from an old run directory's
file count. Use `--resume TIMESTAMP` only with a matching existing campaign and
compatible prompts/settings.

For the 2026-09-18 local refresh, the preflight matches 17 Main, 28 Query, and 18
Analysis prompts. The Main selection uses current ID `4.4` for “What happens when
ethanol is mixed with water near room temperature?” An older saved campaign
labels that same prompt `3.4`; the inherited launcher still used that older ID.
The local launcher now follows the current prompt catalog and retains its four
existing exclusions. Historical campaign artifacts keep their original IDs.

The per-agent runners can also be invoked from `ThermoML_research_agent/`:

```shell
python -m NIST_ThermoML_agents._NIST_ThermoML_main_agent._DEBUG_script.run_tests
python -m NIST_ThermoML_agents.NIST_ThermoML_query_agent._DEBUG_script.run_tests
python -m NIST_ThermoML_agents.NIST_ThermoML_analysis_agent._DEBUG_script.run_tests
```

These commands call the model provider despite the `_DEBUG_script` name. They
are distinct from the mocked/deterministic tests in DEVELOPMENT.md. Consult each
runner's `--help` for prompt selection and output overrides.

For direct Anthropic benchmark requests, configure `ANTHROPIC_API_KEY` in the
launching environment and add `--anthropic` to the batch command. Without `--go`,
the launcher reports its plan. Provider/model availability is account dependent.

## Interpreting a campaign

Keep the exact prompt IDs, prompt text, code/data snapshot, model settings, and
artifacts with any reported cohort. Resume logic may skip files already written;
a partial or failed response can require inspection before retrying a campaign.
An operational success status is not a chemistry-accuracy score. Live comparison
runs are separate from the local rebuild validation.
