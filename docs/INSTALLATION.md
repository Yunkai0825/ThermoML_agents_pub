# Local installation

[Documentation home](../README.md) · [Data](DATA.md) · [Usage](USAGE.md)

## Download the release assets

Clone or download the source repository, then open the
[`workspace-20260918` release](https://github.com/Yunkai0825/ThermoML_research_agents_pub/releases/tag/workspace-20260918)
and download the seven files listed below from **Assets**. They contain the
unchanged original database and benchmark bytes. The Git checkout and GitHub's
source-code ZIP do not contain these seven large files.

Place each downloaded file at its destination relative to the repository root
before launching the browser. Create a destination directory if it is absent.
Rename the Main and Analysis downloads to `test_run_ledgered_20260905.zip` in
their separate directories; the asset prefixes only distinguish them on GitHub.

| Release asset | Local destination |
| --- | --- |
| `thermoml_raw.db` | `ThermoML_research_agent/ThermoML.v2020-09-30.db/thermoml_raw.db` |
| `PCS_INDIV.db` | `ThermoML_research_agent/card_databases_storage/Individual_cards_dbs/PCS_INDIV.db` |
| `PureOrMixtureData_registry.db` | `ThermoML_research_agent/card_databases_storage/PureOrMixtureData_registry.db` |
| `ThermoML_index.db` | `ThermoML_research_agent/card_databases_storage/ThermoML_index.db` |
| `thermoml_raw_corpus.db` | `ThermoML_research_agent/ThermoML.v2020-09-30.db/thermoml_raw_corpus.db` |
| `Main_test_run_ledgered_20260905.zip` | `_benchmark/Main/test_run_ledgered_20260905.zip` |
| `Analysis_test_run_ledgered_20260905.zip` | `_benchmark/Analysis/test_run_ledgered_20260905.zip` |

Keep both benchmark files as ZIP archives; do not extract them. The browser reads
members directly. Compare the downloaded sizes and SHA-256 hashes with
[RELEASE_ASSETS.json](RELEASE_ASSETS.json). PowerShell's `Get-FileHash -Algorithm SHA256`
or a shell's `sha256sum` can calculate the hashes. The remaining source, smaller
databases, benchmark collections, and freeform archives are supplied in Git.

## Environment and files

Start in `ThermoML_research_agents_pub`, the folder containing both
`ThermoML_research_agent/` and `ThermoML_results_browser/`. Python 3.13 is the
local validation environment. Other Python/platform combinations are not claimed
as tested. Complete the asset placement above and preserve the database
locations listed in [DATA.md](DATA.md).

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe launch_thermoml_browser.py
```

Bash with an appropriate Python interpreter:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python launch_thermoml_browser.py
```

The remaining examples use `python` for the interpreter with these packages.
The root `requirements.txt` is the single dependency file for the browser, agents,
and supporting tools.
The requirement bounds describe supported dependencies, not an exact environment
lockfile. Existing SQLite files are used directly; installation does not invoke
parser/database builders.

## Browser

```shell
python launch_thermoml_browser.py
```

The launcher opens the actual bound URL. Default port 5000 falls back to a free
port when unavailable. Use `--port 0` to request a free port, `--port 5001` to
require a particular port, or `--no-browser` to print the URL without opening it.
An explicit occupied port fails with an explanation. Ctrl+C stops the server.

An old browser may still be running on port 5000 from another workspace. If you
see a username badge, personal-history labels, or missing shared runs, use the
URL printed by this workspace's launcher.

## Provider configuration

Live agent calls use the server process's Argo configuration. Set its identity
before launching:

```powershell
$env:ARGO_API_USER = "your-argo-username"
python launch_thermoml_browser.py
```

On Bash, use `export ARGO_API_USER="your-argo-username"`. The identity is for
provider requests; it does not select a personal output directory or browser
account. All freeform outputs are shared.

The agent configs accept `ARGO_API_URL` for an alternate compatible endpoint.
The default service is an internal Argo endpoint and requires appropriate
network access and provider authorization. Model labels in the UI do not imply
that every account can access them. Set environment variables in the launching
shell; the application does not automatically load `.env` files.

The benchmark launcher also supports direct Anthropic mode with
`ANTHROPIC_API_KEY` and `--anthropic`; see [BENCHMARKS.md](BENCHMARKS.md).
That benchmark option does not change the browser's provider automatically.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Missing Python package | Install requirements with the same interpreter used to launch. |
| Missing database or table | Download the seven release assets first and check their destinations and hashes. The property DB is `ThermoML_research_agent/card_databases_storage/Individual_cards_dbs/PCS_INDIV.db`. |
| Agent import error | Keep the sibling layout and use the root launcher or project-directory module commands. |
| Browser tab does not open | Open the printed URL manually. |
| Styling or interactive figures fail offline | The frontend uses CDN assets; local data does not make those assets available offline. |
| Provider request fails | Check server identity, endpoint, model availability, and network access. |
