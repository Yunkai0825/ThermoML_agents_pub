# Development and validation

[Documentation home](../README.md) · [Architecture](../ThermoML_research_agent/README.md)

## Source map

| Area | Entry documentation |
| --- | --- |
| Agent orchestration and tools | [Agent framework](../ThermoML_research_agent/NIST_ThermoML_agents/README.md) |
| Shared engine | [Engine helpers](../ThermoML_research_agent/NIST_ThermoML_agents/general_db_query_engine/general_argo_engine_helpers/README.md) |
| Search and identifier normalization | [Search tools](../ThermoML_research_agent/card_db_search_tools/README.md) |
| Data parsing | [Parser architecture](../ThermoML_research_agent/ThermoML_raw_json_to_card_db_parsers/PARSER_ARCHITECTURE.md) |
| Markdown compaction | [Compactor architecture](../ThermoML_research_agent/ThermoML_card_json_to_md_compactors/ARCHITECTURE.md) |
| Property screening | [Screening pipeline](../ThermoML_research_agent/specialized_tools_pipelines/property_screening_ranking_tool/README.md) |
| Web application | [Browser reference](../ThermoML_database_browser/README.md) |

Runtime workflow Markdown files are consumed by the agents. Treat changes to
those files as changes to behavior, unlike edits to explanatory READMEs.

## Install validation dependencies

From the workspace root, install the runtime packages and pytest:

```shell
python -m pip install -r ThermoML_research_agent/requirements.txt
python -m pip install pytest
```

## Included offline checks

These commands target files included by the publication's ignore rules. They use
local data or mocks and do not launch live model calls. Pull the Git LFS database
objects before running database-dependent checks; see [INSTALLATION.md](INSTALLATION.md).

Import and benchmark-output preflight, from the repository root:

```shell
python ThermoML_research_agent/run_debug_benchmark.py --offline
```

Workflow hooks, registry database paths, and search-tool regressions, from the
agent project folder:

```shell
cd ThermoML_research_agent
python -m pytest NIST_ThermoML_agents/general_db_query_engine/general_posteval_helpers/compaction_funnels/test_workflow_generation.py NIST_ThermoML_agents/general_db_query_engine/general_ThermoML_db_csv_registry/test_registry_paths.py card_db_search_tools/DEBUG_tools_scripts -q
```

The search suite's `test_live_chemistry_tools.py` exercises local database tools;
"live" in that filename does not mean a model API call.

Real-card compactor checks, from that same directory:

```shell
python ThermoML_card_json_to_md_compactors/_entry_by_entry_validator/run_all_compactor_tests.py
```

The compactor harness replaces its own generated `compactor_test_output` folder
under `_output/Query/Diagnostics/compactor_tests/`. It does not rebuild the source
databases. Its output counts depend on the installed database contents.

## Local test folders omitted from publication

[.gitignore](../.gitignore) excludes every directory named `test` or `tests`.
Consequently the maintainer workspace's root `tests/`, browser `tests/`, parser
`tests/`, and property-screening `tests/` suites are not available in a fresh
published clone. Do not use those paths as public installation checks.
Directories named `test_block_search_adv` and `test_query_tool_matrix` are
included; they are part of the search command above.

If working from a full maintainer workspace that separately retains the omitted
suites, they provide additional launcher, browser, parser, and screening coverage.
Their local presence does not mean they are distributed in this snapshot. Scratch
archives named `__tmp__` are also excluded. Select the included checks explicitly
instead of collecting the whole workspace recursively.

## Model-driven checks

The per-agent `_DEBUG_script/run_tests.py` files are scientific prompt runners.
Despite their names, they call the configured model service. Their invocation,
selection, output structure, and resume behavior are described in
[BENCHMARKS.md](BENCHMARKS.md). An import preflight or mocked test does not replace
a live evaluation of model responses.

## Reporting changes

Describe the user-visible behavior or scientific contract being changed, identify
the relevant source files, and record the checks run. For data changes, include the
snapshot and affected database/card types. For model comparisons, retain prompts,
provider/model configuration, and the corresponding output artifacts.

Use the identifiers defined in [ID_architecture.md](../ThermoML_research_agent/card_databases_storage/ID_architecture.md)
when linking between cards, blocks, and source papers. Database read-only access,
scientific input validation, and artifact path containment are implementation
contracts, independent of the browser's shared access model.
