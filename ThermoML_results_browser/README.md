# ThermoML Results Browser

A local Flask application for browsing ThermoML papers and data blocks, running
Main/Query/Analysis agents, and inspecting saved answers, tool histories, plots,
and workflow figures.

## Start the browser

From the `ThermoML_research_agents_pub` directory:

```shell
python -m pip install -r requirements.txt
python launch_thermoml_browser.py
```

The launcher opens the URL it prints in your default browser. It tries port 5000
and selects another free port if that port is occupied. An explicit occupied
`--port` fails instead of opening a different application. Use `--port 0` for any
available port, `--port 5001` for a chosen port, or `--no-browser` to print the URL
without opening a tab. The server binds to `127.0.0.1`; Ctrl+C stops it.

Direct entry also works with `python -m ThermoML_results_browser.app` or
`python ThermoML_results_browser/app.py`, but those commands use fixed port 5000
and do not open a browser tab.

Keep this package beside `ThermoML_research_agent/`. The supplied index is
`ThermoML_research_agent/card_databases_storage/ThermoML_index.db`; archived
JSON/XML comes from
`ThermoML_research_agent/ThermoML.v2020-09-30.db/thermoml_raw_corpus.db`.
Startup uses those databases as read-only files and does not rebuild them.

## Local features and model access

Paper browsing, ordinary searches, saved-run inspection, and deterministic
analysis use local data. Smart search can use deterministic ID alignment;
its agentic options and new Main/Query/Analysis requests require Argo access.
Configure the launching process with `ARGO_API_USER` and, when needed,
`ARGO_API_URL`. These are provider settings, not browser accounts.
Setting `ANTHROPIC_API_KEY` does not switch this browser to Anthropic; the separate
benchmark launcher owns that optional adapter.

Every visitor can inspect raw JSON, full logs, tool histories, working memory,
reasoning, statistics, and saved workflow figures. There are no browser login or
debug-access controls. Browser JavaScript and styling use CDN resources, so local
database access does not guarantee a fully offline frontend.

## Saved output

New freeform runs persist in the shared directories below, independent of the
visitor or provider identity:

```text
_output/Main/run_.../
_output/Query/run_.../
_output/Analysis/run_.../
```

Existing Main sessions directly under `_output/run_*` remain visible. Existing
freeforms can also be stored in `_output/freeform_runs.zip` (legacy Main) or
`_output/<Agent>/freeform_runs.zip`, with run folders directly at the ZIP root.
A ZIP named after one run may instead contain that run's files at its root.
Archived sessions and new ordinary folders are listed together; an ordinary
folder takes precedence when it shares a run name with an archive. ZIP contents
are read-only, while new runs continue to write ordinary folders in `_output`.
Closing a tab does not delete output. `_benchmark/{Main,Query,Analysis}` supplies read-only
benchmark history. Collections may be directories or ZIP files; the browser reads
ZIP members directly without extracting them. Full-framework runs are stored in
`test_run_ledgered_20260905.zip`, and no-ledger runs in
`test_run_no_ledger_20260905.zip` within each agent directory. Run folders sit at
the archive root. Query's additional mode collections retain their names with a
`.zip` extension. Each agent keeps its own tab and mode columns.
Renamed examples use `Q<current prompt ID>_run_<YYYYMMDD_HHMMSS>`; a six-digit
microsecond suffix distinguishes timestamp collisions. The browser uses a valid
current ID in the folder name for grouping and retains the question text and
original prompt ID inside historical records. Legacy `run_*` examples remain
supported through question-text matching.
In route parameters, `scope=user` is the compatibility name for shared freeform
history; `scope=benchmark` selects benchmark records.

## Main routes

| Route | Purpose |
| --- | --- |
| `/` and `/papers` | Database overview and paper listing |
| `/paper/<doi>` and `/raw-json/<doi>` | Paper data and complete source JSON |
| `/compound/<inchikey>` | Compound details and related papers |
| `/search` | Structured search, similarity search, and optional alignment |
| `/agents` | Launch agents and view live output |
| `/agents/history` | Shared freeform or benchmark history |
| `/agents/launch` (POST) | Start a model request |
| `/agents/status/<run_id>` and `/agents/stream/<run_id>` | Polling and SSE output |
| `/agents/detail/<agent_type>/<dir_name>` | Saved result, history, memory, and artifacts |
| `/agents/workflow/<agent_type>/<dir_name>/<filename>` | Saved workflow figure or table |
| `/analysis` | Local analysis workbench |

See [app.py](app.py) and [agent routes](helpers/agent_routes.py) for route
contracts. Artifact routes retain containment checks for filesystem paths and ZIP
members; benchmark records cannot be deleted through the freeform endpoint.
The Specialized tools page, embedded panels, plugin adapter, and APIs are removed.

## Development checks

From the repository root, check application imports and registered routes:

```shell
python -m pip install -r requirements.txt
python -B -c "from ThermoML_results_browser.app import app; print(app.url_map)"
```

This does not launch model requests or rebuild databases. The current checkout
has no standalone browser regression suite. The [development guide](../docs/DEVELOPMENT.md)
lists the included offline checks; [publication instructions](../docs/PUBLISHING.md)
describe the no-pointer checks for local Git objects.

See [ARCHITECTURE.md](ARCHITECTURE.md) for the component boundaries.
