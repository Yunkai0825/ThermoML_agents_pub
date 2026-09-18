# ThermoML Agents

This local workspace combines the Main, Query, and Analysis agents with the
ThermoML results browser and the supplied NIST ThermoML databases. It uses the
`v2020-09-30` archive snapshot. Source records, generated cards, and saved run
artifacts provide the context for inspecting an answer.

## Start locally

Clone or download the repository, then download the seven original files from
[the `workspace-20260918` release](https://github.com/Yunkai0825/ThermoML_research_agents_pub/releases/tag/workspace-20260918)
and place them at the exact paths in [installation](docs/INSTALLATION.md#download-the-release-assets).
A Git clone or source-code ZIP alone does not include those seven files. Keep the
benchmark archives as ZIPs; the browser reads them directly.

After placing the assets, run from this folder (`ThermoML_research_agents_pub`):

```shell
python -m pip install -r requirements.txt
python launch_thermoml_browser.py
```

Use the URL printed by the launcher. It binds to localhost, tries port 5000,
and selects a free port if that port is occupied. `--port 0` always selects a
free port; `--no-browser` suppresses opening a tab. Keep the process running
and press Ctrl+C to stop it.

Python 3.13 is the local validation environment. The existing databases are the
starting point; routine setup does not regenerate them. Browsing data and saved
results needs no model-provider credentials. Live agent requests need the
server's provider configuration described in [installation](docs/INSTALLATION.md).

## Layout

```text
ThermoML_research_agents_pub/
├── launch_thermoml_browser.py
├── ThermoML_results_browser/       # Browser application and analysis tools
├── ThermoML_research_agent/         # Agent framework, search tools and databases
├── _benchmark/                     # Main, Query and Analysis benchmark artifacts
├── _output/                        # Shared freeform sessions and diagnostics
└── docs/                           # Setup, use, data and validation
```

Freeform sessions use `_output/{Main,Query,Analysis}` for everyone. Historical
Main sessions in `_output/freeform_runs.zip` remain browsable without extraction.
Benchmark output uses `_benchmark/{Main,Query,Analysis}`. Components declare these paths relative
to their source files; there is no output-routing module. Explicit API session
paths and benchmark output arguments remain available.

The browser provides shared access to saved runs and their detailed artifacts.
It has no browser-account or debug-access gates. Read-only database access,
scientific validation, and artifact path checks remain part of the application.

## Documentation

- [Installation and provider configuration](docs/INSTALLATION.md)
- [Browser and Python API usage](docs/USAGE.md)
- [Data inventory and provenance](docs/DATA.md)
- [Release asset sizes and SHA-256 checksums](docs/RELEASE_ASSETS.json)
- [Benchmark commands and recorded outputs](docs/BENCHMARKS.md)
- [Development and local validation](docs/DEVELOPMENT.md)
- [Publication policy and no-pointer checks](docs/PUBLISHING.md)
- [Workspace architecture](MASTER_ARCHITECTURE.md)
- [Browser reference](ThermoML_results_browser/README.md)
- [Agent framework and call hierarchy](ThermoML_research_agent/README.md)

## License and citation

The software uses the [MIT license](LICENSE). Keep the [third-party data notice](NOTICE)
with the NIST-derived data. [CITATION.cff](CITATION.cff) retains the manuscript,
authors, and data citations from the published project. The `workspace-20260918` tag identifies this workspace publication; no new
paper DOI is assigned by that tag.
