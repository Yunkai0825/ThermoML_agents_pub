# Browser architecture

The browser is a sibling package of `ThermoML_research_agent`; it imports that
project's search tools, schemas, agents, and calculation modules. It reads
prepared databases and saved results and does not build the card databases.
[Usage and setup](README.md) describe the public entry points.

## Entry point and module ownership

[The root launcher](../launch_thermoml_browser.py) imports the Flask application,
binds a threaded Werkzeug server to `127.0.0.1`, starts it, and opens a browser
window. It tries port 5000 by default and selects a free port if that listener
is unavailable. An explicitly requested occupied port fails instead. The
workspace path and actual listening URL are printed before opening the page.
`--no-browser` suppresses only the desktop-opening step.

| Module | Responsibility |
|---|---|
| [app.py](app.py) | Flask application; index, paper, compound, raw JSON, and Analysis routes |
| [helpers/search_routes.py](helpers/search_routes.py) | Search blueprint, SQL filter construction, structural similarity, smart-query alignment |
| [helpers/agent_routes.py](helpers/agent_routes.py) | Launch/status/SSE, history, artifact, workflow, deletion, and card-preview endpoints |
| [helpers/specialized_tool_routes.py](helpers/specialized_tool_routes.py) | Generic specialized-result page, tables, and artifact downloads |
| [helpers/raw_corpus.py](helpers/raw_corpus.py) | Indexed, zlib-compressed source-document reads |
| [helpers/sqlite_readonly.py](helpers/sqlite_readonly.py) | Immutable read-only SQLite connections |
| [helpers/thermoml_parsers.py](helpers/thermoml_parsers.py) | Source JSON to display blocks, column metadata, and rows |
| [agent_runner.py](agent_runner.py) | Serialized background agent execution, progress buffers, saved-run discovery, result rendering |
| [adv_search_calc/](adv_search_calc/README.md) | Deterministic calculation dispatch and custom-CSV nonideality analysis |
| [cannonical_id_alignment_search_agent/](cannonical_id_alignment_search_agent/README.md) | Deterministic and Argo-assisted search-field alignment |
| [specialized_tool_plugins/](specialized_tool_plugins/README.md) | Explicit adapters from saved result manifests to browser data |
| [templates/](templates/README.md), `static/` | Jinja views, JavaScript result panels, charts, links, and styles |

The package initializer and direct-script entry point anchor imports to the
repository and its `ThermoML_research_agent` sibling. Database and output paths
are declared in the modules that consume them; they do not depend on the shell's
working directory or a shared output-routing module.

## Data boundaries

`app.py` and the route helpers read the search index under
`ThermoML_research_agent/card_databases_storage/`. Paper details and raw JSON use
`ThermoML_research_agent/ThermoML.v2020-09-30.db/thermoml_raw_corpus.db`.
Each archived payload is compressed independently and located by its source
path; no loose DOI file needs to be extracted during a request.

The database accessor is registered in `app.extensions` for the search
blueprint. Connections are read-only and closed at request teardown. Typed
identifiers are validated at the route/tool boundary. Artifact serving retains
file-type and path-containment checks. These protect data integrity and are
independent of browser identity: the application has no login, guest role, or
debug-mode access policy.

## Agent execution

`start_run(question, ...)` returns a **run ID string** and creates an `AgentRun`.
`get_run(run_id)` returns that in-memory object. The runner allows one active
browser-launched run at a time because the imported agents share mutable engine
and session state. An additional launch receives HTTP 409 while one is active.

The worker applies model/time settings, supplies a session directory below
`_output/<Agent>/`, calls the selected Main/Query/Analysis API, and captures
progress. Model/account overrides are restored after execution. Provider account
configuration comes from the server process, not a browser visitor.

`AgentRun` provides a bounded terminal buffer with sequence IDs for SSE
reconnection and reads the evolving history, reasoning, working-memory, and
reference-statistics files. `/agents/status/<run_id>` is the polling alternative
to `/agents/stream/<run_id>`. Both expose detailed output to every visitor.
Completed runs remain on disk after server exit, even though their live in-memory
run IDs are no longer available.

Normal browser execution uses Argo. The separate benchmark launcher installs
its Anthropic adapter inside benchmark subprocesses; it does not install that
adapter into the Flask process.

## Saved-run discovery

The runner declares two maps: `AGENT_OUTPUT_DIRS` for `_output/Main|Query|Analysis`
and `BENCHMARK_OUTPUT_DIRS` for `_benchmark/Main|Query|Analysis`. It also scans
legacy flat `_output/run_*` Main sessions. All freeform output is shared.

History scopes are categories: `user` means shared freeform, `benchmark` means
read-only benchmark archives, and `all` merges the roots for relevant APIs.
Freeform deletion cannot target benchmark roots. No browser-unload callback
removes output files.

Benchmark registration joins saved `TEST_TRACE*.json` records and result files
with each agent's `_DEBUG_script/test_prompts.md` registry. It handles new nested
`test_run_*/Q*` sessions, older flat `Q*_result.md` collections, and standalone
`run_*` sessions. Existing delegated `analysis_runs/run_*` artifacts are discovered
recursively so Main results can expose their generated figures and CSVs.

The result-reading boundary renders post-answer JSON envelopes into answer
Markdown and post-answer analysis. Canonical identifier links, evidence-ledger
tables, complete benchmark tool history, and available workflow artifacts are
presented without a debug gate. Missing files in older runs remain missing;
viewing history does not rerun an agent or regenerate its output.

## Search and calculations

Ordinary search constructs SQL against the prepared index. Structural similarity
uses the research project's local chemistry tools. Smart search calls
`alignment_agent_run(search_text, settings=...)` with `use_agent=False` for the
deterministic path or `True` for the Argo path, then fills empty search fields.
The alignment API isolates mutable form state with a context variable.

The Analysis page calls `analysis_dispatcher.dispatch(tool, **kwargs)` and returns
JSON suitable for charting. All four tools are deterministic; using calculation
modules from an agent package does not invoke a model. Database targets use DOI,
typed `PROPblock_*`/`RXNblock_*` IDs, and optional `BLKsubsys_*` IDs.

Specialized-tool routes use an explicit plugin registry. Adapters validate saved
manifests, normalize tables/figures to `tabular-run-v1`, and resolve only declared
artifacts. Result folders are never imported as executable plugins.

## Frontend and validation

Jinja templates and local JavaScript provide result tabs, live output, artifact
views, and deep links. Styling, Markdown, mathematics, and plotting libraries
also come from external CDNs; see [template notes](templates/README.md).

Run the scoped test suite from the repository root:

```sh
python -m unittest discover -s ThermoML_database_browser/tests -t .
```

Tests exercise path containment, migrated history layouts, shared access, and
mocked execution. Provider/network availability needs separate live validation.
