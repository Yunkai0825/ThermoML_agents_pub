# ThermoML Database Browser

A local Flask application for searching ThermoML data, inspecting measurements,
running deterministic calculations, and using the Main, Query, and Analysis agents.
See the [repository overview](../README.md) for project setup, data availability,
and the citations NIST requests for use of ThermoML Archive data.

## Start the browser

Run these commands from the repository root after installing the required data:

```sh
python -m pip install -r ThermoML_database_browser/requirements.txt
python launch_thermoml_browser.py
```

The browser requirements file includes the sibling research project's runtime
requirements. The launcher tries port 5000 and selects an available local port
if that port is already occupied. It prints the workspace path and actual URL,
then opens that URL in your default browser. Use the printed address to reach
this workspace when another application already uses port 5000. Keep the terminal
running; press **Ctrl+C** to stop the server. Closing a tab does not stop the server or remove saved results.

```sh
python launch_thermoml_browser.py --port 5001
python launch_thermoml_browser.py --no-browser
python launch_thermoml_browser.py --help
```

`--port 0` explicitly chooses an available local port. An explicit occupied
port, such as `--port 5000`, reports an error without opening a browser; choose
another port or omit `--port` to allow automatic fallback. The launcher binds
to `127.0.0.1`. An absolute path to the launcher also works from
another working directory. Direct execution with
`python -m ThermoML_database_browser.app` starts the application without opening
a browser automatically.

## Required local data

Paths are anchored to the repository, independently of the launch directory.
The browser package and research code are siblings:

```text
ThermoML_agents_pub/
├── launch_thermoml_browser.py
├── ThermoML_database_browser/
├── ThermoML_research_agent/
│   ├── card_databases_storage/
│   │   └── ThermoML_index.db
│   └── ThermoML.v2020-09-30.db/
│       └── thermoml_raw_corpus.db
├── _output/
└── _benchmark/
```

| Data | Used for |
|---|---|
| `ThermoML_research_agent/card_databases_storage/ThermoML_index.db` | Search, paper/compound lists, identifier lookup |
| `ThermoML_research_agent/ThermoML.v2020-09-30.db/thermoml_raw_corpus.db` | Paper details, raw JSON, raw block data |
| Other prepared card databases in `card_databases_storage/` | Agent tools, card previews, and database-backed calculations |

Installing Python dependencies does not create these databases. Follow the
[research project documentation](../ThermoML_research_agent/README.md) for data
and preparation details. The browser reads the compressed raw corpus directly;
loose per-DOI JSON/XML directories do not replace `thermoml_raw_corpus.db`.

## Local features and model calls

| Feature | Model service needed? |
|---|---|
| Database search, paper/compound details, raw JSON | No |
| Smart search with agentic search disabled | No; uses deterministic ID alignment |
| The four tools on the Analysis page | No; calculations run locally |
| Viewing existing history, workflow figures, and specialized-tool results | No |
| Main, Query, or Analysis runs from the Agents page | Yes, Argo in the normal browser process |
| Agentic smart search and optional Query-agent escalation | Yes, Argo |

The frontend loads Bootstrap, charting, Markdown, and related libraries from
CDNs. Local data access does not require a model service, but complete UI
styling and interactive rendering can require an internet connection or cached
CDN assets. This checkout does not bundle a fully offline frontend.

### Argo configuration

Set `ARGO_API_USER` in the environment **before starting the server**, using the
account recognized by your Argo service. For example, in PowerShell:

```powershell
$env:ARGO_API_USER = "your-argo-account"
python launch_thermoml_browser.py
```

In a POSIX shell:

```sh
export ARGO_API_USER="your-argo-account"
python launch_thermoml_browser.py
```

Main, Query, and Analysis configs accept `ARGO_API_URL` for an Argo-compatible
chat endpoint; their default endpoint is on Argonne's internal network. The
[alignment agent config](cannonical_id_alignment_search_agent/alignment_agent_argo_config.py)
currently declares its `API_URL` directly, so changing `ARGO_API_URL` alone does
not change the endpoint used by agentic smart search. Provider connectivity and
account requirements still apply; there is no browser username/login gate.

The browser's model selector chooses a model alias for the selected agent. It
does not switch providers. The research project's Anthropic adapter is installed
by the separate benchmark launcher in `--anthropic` mode; setting
`ANTHROPIC_API_KEY` does not switch this browser to Anthropic. See
[the benchmark launcher](../ThermoML_research_agent/run_debug_benchmark.py) and
[research documentation](../ThermoML_research_agent/README.md) for that workflow.

## Using the pages

- **Advanced Search:** combine bibliography, chemistry, property, data, and
  structural filters. Smart search can fill empty form fields using deterministic
  or agentic alignment. Results and paper pages include a lazily loaded **Raw JSON** panel.
- **All Papers / paper / compound:** inspect references, compounds, typed
  measurement blocks, and data tables. Canonical identifiers link to their
  corresponding paper or compound.
- **Analysis:** select a paper and block, or paste custom CSV for Quick
  Non-Ideality Analysis. The other tools provide Redlich–Kister fitting, block
  inspection, and pure-component value extraction. See [analysis tools](adv_search_calc/README.md).
- **Agents:** select Main, Query, or Analysis, enter a question, and optionally
  adjust the model and time limits. One browser-launched agent runs at a time.
  Progress, logs, live reasoning, API statistics, and completed result panels
  are available to every visitor.
- **History:** choose shared freeform runs or benchmarks. Open a result to view
  its history, memory, statistics, data, images, and available workflow figures.
- **Specialized tools:** inspect existing property-screening result manifests,
  rankings, tables, figures, and downloads. This page reads results; it does not
  launch the screening pipeline. See [the plugin adapter](specialized_tool_plugins/README.md).

## Shared outputs and history

| Location, relative to repository root | Browser behavior |
|---|---|
| `_output/Main/`, `_output/Query/`, `_output/Analysis/` | New shared, persistent freeform runs |
| `_output/run_*` | Existing flat Main sessions remain discoverable |
| `_benchmark/Main/`, `_benchmark/Query/`, `_benchmark/Analysis/` | Read-only benchmark history |

Output directories are declared directly in the code that uses them. There is
no output-routing service or per-user output directory. All visitors see the
same freeform results, and the freeform delete action removes a shared run.
Benchmark deletion is not exposed by that action. History URLs retain
`scope=user` as the compatibility name for the **shared freeform** category;
it does not identify or filter a person.

Benchmarks are grouped using the agents' prompt files and saved trace manifests.
Both nested `test_run_*/Q*` sessions and the existing flat/sibling session layouts
are supported. Full logs, tool history, memory, statistics, raw JSON, and
available workflow files have no debug-mode access gate. Older runs can lack
files that were not generated when they were created.

## Route reference

Angle-bracket segments below are placeholders. DOI and artifact paths may
contain `/`; `block_number` is a typed ID such as `PROPblock_1`, not a bare integer.

| Route | Method / purpose |
|---|---|
| `/`, `/search`, `/papers` | GET: overview, search, and paper list |
| `/paper/<doi>`, `/raw-json/<doi>` | GET: parsed paper and complete source JSON |
| `/compound/<inchikey>`, `/lit/<lit_num_id>`, `/comp/<comp_num_id>` | GET: compound detail and canonical-ID redirects |
| `/agents`, `/agents/history` | GET: launch interface and shared history |
| `/agents/launch` | POST JSON: start a run and return `run_id` |
| `/agents/status/<run_id>`, `/agents/stream/<run_id>` | GET: polling JSON or SSE progress |
| `/agents/image/<run_id>/<filename>`, `/agents/live_csv/<run_id>/<filename>` | GET: live-run image or CSV data |
| `/agents/runs/<agent_type>`, `/agents/detail/<agent_type>/<dir_name>` | GET: saved runs and detail; accept `scope` |
| `/agents/delete/<agent_type>/<dir_name>` | POST: delete a shared freeform run |
| `/agents/csv/<agent_type>/<dir_name>/<filename>`, `/agents/img/<agent_type>/<dir_name>/<filename>` | GET: saved CSV data or image |
| `/agents/workflow/<agent_type>/<dir_name>/<filename>` | GET: saved workflow PNG, HTML, or TSV |
| `/agents/card/<entity_type>/<global_id>` | GET: canonical card preview |
| `/analysis`, `/analysis/tool_definitions`, `/analysis/search_papers` | GET: workbench, tool metadata, and matching papers |
| `/analysis/paper_blocks/<doi>`, `/analysis/block_data/<doi>/<block_number>` | GET: block targets and data |
| `/analysis/run` | POST JSON: run a deterministic calculation |
| `/specialized-tools`, `/api/specialized-tools/plugins` | GET: plugin page and registry |
| `/api/specialized-tools/<plugin_id>/runs` | GET: saved specialized-tool runs |
| `/api/specialized-tools/<plugin_id>/runs/<run_key>` | GET: normalized result detail |
| `/api/specialized-tools/<plugin_id>/runs/<run_key>/tables/<table_id>` | GET: declared table data |
| `/api/specialized-tools/<plugin_id>/runs/<run_key>/artifacts/<artifact_id>` | GET: declared artifact download |

Saved-run file routes also accept `sub_run` for a nested question/session and
`scope=user`, `benchmark`, or `all`. Database block analysis accepts an optional
`BLKsubsys_id` to select an exact subsystem. The route implementations are in
[app.py](app.py), [agent routes](helpers/agent_routes.py),
[search routes](helpers/search_routes.py), and [specialized-tool routes](helpers/specialized_tool_routes.py).

## Development and checks

[Architecture](ARCHITECTURE.md) describes module ownership and execution flow.
The browser package can be tested without making paid model calls:

```sh
python -m unittest discover -s ThermoML_database_browser/tests -t .
```

These tests cover output discovery, artifacts, shared access, and mocked agent
execution. They do not establish that your provider account or network can
complete a live model request.
