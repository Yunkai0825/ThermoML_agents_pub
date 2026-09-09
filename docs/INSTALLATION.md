# Installation and configuration

[Documentation home](../README.md) · [Usage](USAGE.md) · [Data files](DATA.md)

## Environment

Python 3.13 on Windows was used for the workspace checks. Dependencies are listed
in [requirements.txt](../ThermoML_research_agent/requirements.txt); these are
minimum bounds, not an exact reproduction lockfile. Other Python and operating
system combinations have not been validated in this workspace.

The normal browser and agent workflows require Python packages and the supplied
SQLite databases. Node.js is only useful for JavaScript syntax checks. OriginPro
is optional and is used only by the cost-audit script's Origin export operation.

The data files occupy several gigabytes; use the exact inventory in [DATA.md](DATA.md)
when preparing a checkout or data bundle. Generated runs and rebuilds need
additional space.

## Obtain the workspace

Install Git and [Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage)
first. Every SQLite `*.db` file is tracked with Git LFS, so the database download
is part of setup:

```shell
git lfs install
git clone https://github.com/Yunkai0825/ThermoML_agents_pub.git
cd ThermoML_agents_pub
git lfs pull
```

The nonempty databases total about **4.875 GB**. Allow additional disk space for
the local Git LFS cache, dependencies, saved outputs, and new runs. `git lfs pull`
materializes the database contents for the checked-out revision; small text
pointer files are not usable SQLite databases.

If you already cloned the repository without Git LFS, install it, enter the
repository directory, and run `git lfs install` followed by `git lfs pull`.
Retain the sibling `ThermoML_database_browser/` and `ThermoML_research_agent/`
folders and the exact data paths in [DATA.md](DATA.md). Do not replace an active
card database with a similarly named placeholder file.

## Install dependencies

A virtual environment keeps this project's packages separate from other projects.

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r ThermoML_research_agent/requirements.txt
.\.venv\Scripts\python.exe launch_thermoml_browser.py
```

Bash, where an appropriate Python interpreter is already installed:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r ThermoML_research_agent/requirements.txt
python launch_thermoml_browser.py
```

The remaining examples use `python` for the interpreter with these dependencies.
On Windows, you can substitute `.\.venv\Scripts\python.exe` without activating
the virtual environment.

## Launch and verify

```shell
python launch_thermoml_browser.py
python launch_thermoml_browser.py --port 5001
python launch_thermoml_browser.py --no-browser
```

Choose one launch command. The server binds to `127.0.0.1`; the default port is
5000, with an automatic fallback to a free port if 5000 is occupied. The printed
URL always points to this workspace. An explicit occupied `--port` fails with an
explanation. Ctrl+C stops it. The launcher's `--port 0` option selects an available port
and prints the resulting URL. `--no-browser` suppresses only opening a tab.

Check the Python entrypoints without sending API requests:

```shell
python ThermoML_research_agent/run_debug_benchmark.py --offline
```

A successful preflight checks imports, selected configuration values, and the
planned output paths. It does not prove that credentials work, that every database
query succeeds, or that a scientific answer will be correct. For actual local
database checks, run the [included offline checks](DEVELOPMENT.md).

## Argo configuration

The browser's agent requests and ordinary terminal/API entrypoints use Argo.
Configure the server process before starting it:

PowerShell:

```powershell
$env:ARGO_API_USER = "your-argo-username"
python launch_thermoml_browser.py
```

Bash:

```bash
export ARGO_API_USER="your-argo-username"
python launch_thermoml_browser.py
```

`ARGO_API_USER` is the provider identity shared by this server, not a browser login
or output-folder name. All visitors use the same persistent freeform directories.
The service must also be reachable from your network and grant access to the
configured account and models.

| Setting | Effect |
| --- | --- |
| `ARGO_API_USER` | Provider identity used by Main, Query, Analysis, and browser alignment. |
| `ARGO_API_URL` | Overrides the Main, Query, and Analysis chat endpoint. Defaults are declared in each agent config. |
| `ANTHROPIC_API_KEY` | Required by the optional direct Anthropic benchmark adapter. |
| `ANTHROPIC_ADAPTER_CAPTURE` | Optional adapter response-capture file/directory for explicit adapter use. The batch benchmark sets a campaign capture path itself. |

The browser alignment config declares its endpoint directly; `ARGO_API_URL` does
not override that particular endpoint. See the
[alignment config](../ThermoML_database_browser/cannonical_id_alignment_search_agent/alignment_agent_argo_config.py).
Model names, time limits, and loop limits are declared in the individual
[agent configs](../ThermoML_research_agent/NIST_ThermoML_agents/).
The browser exposes model and selected time-limit overrides for a run. A listed
model label does not establish its availability on your provider account.

The application does not automatically load `.env` files. Set variables in the
shell or service environment that launches Python.

## Direct Anthropic benchmark mode

From the workspace root, set `ANTHROPIC_API_KEY` in your shell and run:

```shell
python ThermoML_research_agent/run_debug_benchmark.py --anthropic
python ThermoML_research_agent/run_debug_benchmark.py --go --anthropic
```

The first command is a preflight; the second launches model calls. The adapter
maps the configured Argo model labels to direct Anthropic model IDs; consult
[the mapping](../ThermoML_research_agent/NIST_ThermoML_agents/general_db_query_engine/general_argo_engine_helpers/anthropic_argo_adapter.py)
when reproducing a run. The public benchmark launcher applies this adapter in its
worker processes. Setting `ANTHROPIC_API_KEY` alone does not switch the browser or
ordinary API entrypoints away from Argo.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| `ModuleNotFoundError` for a third-party package | Install requirements with the same Python interpreter used to launch the app. |
| Agent package cannot be imported | Run the documented module commands from `ThermoML_research_agent/`, or use the workspace-root launcher. |
| Missing database, `no such table`, or invalid SQLite file | Run `git lfs pull`, then check the paths and file sizes in [DATA.md](DATA.md). A missing payload, empty placeholder, or LFS pointer is not a usable database. |
| Browser tab does not open | Open the printed URL manually; `--no-browser` is also available. |
| Port is occupied | The default launcher selects a free port automatically. For an explicit port, choose a different one or use `--port 0`. |
| Username badge, personal history labels, or missing shared runs | Use the actual URL printed by the workspace launcher. Another ThermoML copy may still be serving port 5000. The current history page says "Shared freeform runs" and reads this workspace's `_output` folder. |
| Agent returns a provider/configuration error | Check the server's provider identity, endpoint, network access, and selected model. `--offline` does not test these. |
| Styling, Markdown, or interactive figures fail without internet | Browser assets and interactive figure libraries use CDNs. Local data access does not imply all browser assets are available offline. |
| No figures in an older recorded run | Inspect the saved artifacts. Workflow generation is attempted after new root runs; older records may not contain figures. |
