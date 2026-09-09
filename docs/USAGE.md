# Using ThermoML Agents

[Documentation home](../README.md) · [Installation](INSTALLATION.md) · [Benchmarks](BENCHMARKS.md)

## Browser

Run `python launch_thermoml_browser.py` from the workspace root. Use **All Papers**
and **Advanced Search** to inspect the local archive. Paper details link the
structured data back to the raw source JSON. **Analysis** exposes configured
calculation tools; **Specialized tools** displays saved specialized-tool results.
Some agent-assisted search/alignment operations require the provider configuration
in [INSTALLATION.md](INSTALLATION.md).

On **Agents**, choose Main for a question that may require both retrieval and
analysis, Query for retrieval, or Analysis for calculations and fitting. Start with
a specific compound/system, property, temperature/pressure conditions, and the
output you want. For example:

> Find experimental liquid-density data for water and ethanol near 298.15 K.
> Identify the source papers and report which compositions were measured.

This is an example question, not an asserted result. Actual availability depends
on the database snapshot and the returned source records.

The live page exposes answer, tool history, reasoning, memory, statistics, generated
files, and available workflow figures. **History** separates shared freeform runs
from the recorded benchmarks. All visitors see the same freeform collection.
The browser currently starts one agent run at a time because the execution engine
uses shared session/configuration state.

See [the browser reference](../ThermoML_database_browser/README.md) for routes and
supported analysis tools.

## Output files

| Run type | Default location relative to the workspace root |
| --- | --- |
| Main freeform | `_output/Main/run_*/` |
| Query freeform | `_output/Query/run_*/` |
| Analysis freeform | `_output/Analysis/run_*/` |
| Benchmark campaign | `_benchmark/<Agent>/test_run_<timestamp>/` |
| Benchmark prompt session | `<campaign>/Q<prompt-id>/` in current runners |
| Diagnostic tools | Declared subdirectories under `_output/<Agent>/` |

Closing a tab does not delete a session. Paths are declared in the code that uses
them; they do not depend on browser accounts. Explicit `session_dir` and `--output`
arguments can override the defaults for a caller-managed run.

A session may contain `result.md`, working-memory files, `run_history.md`, reference
statistics, reasoning records, `data/`, `plots/`, and `workflow/`. Main and Analysis
can contain nested `query_runs/` or `analysis_runs/`. Available files depend on the
agent and tools actually used. The browser Query wrapper writes a `result.md`;
callers of the Query Python API should also retain the returned `answer`.

## Interactive terminal entrypoints

Run these from `ThermoML_research_agent/`, with provider configuration already set:

```shell
python -m NIST_ThermoML_agents._NIST_ThermoML_main_agent.main_agent_argo_engine.main_agent_terminal_ui
python -m NIST_ThermoML_agents.NIST_ThermoML_query_agent.query_agent_argo_engine.query_agent_terminal_ui
python -m NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.analysis_agent_argo_engine.analysis_agent_terminal_ui
```

Choose one entrypoint. These are interactive model-driven sessions, not offline
tests. Their built-in help describes the conversation commands.

## Python API

Run the following examples from `ThermoML_research_agent/`, or place that directory
on the Python import path. API calls below send requests to the configured model
service.

Main automatically creates a freeform session unless one is supplied:

```python
from NIST_ThermoML_agents._NIST_ThermoML_main_agent.ThermoML_main_api import ThermoML_main_run

result = ThermoML_main_run(
    "Find water/ethanol liquid-density data near 298.15 K and identify the source blocks."
)
print(result.answer)
print(result.session_dir)
```

Query requires an explicit `session_dir` or working-memory file:

```python
from pathlib import Path
from uuid import uuid4
from NIST_ThermoML_agents.NIST_ThermoML_query_agent.ThermoML_query_api import ThermoML_query_run

session = Path("../_output/Query") / f"run_{uuid4().hex}"
result = ThermoML_query_run(
    "Find experimental liquid-density measurements for ethanol near 298.15 K.",
    session_dir=session,
)
print(result.answer)
```

Analysis exposes the same session-directory option as Main:

```python
from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_analysis_api import ThermoML_analysis_run

result = ThermoML_analysis_run(
    "Find suitable ethanol/water density blocks near 298.15 K, inspect their composition coverage, "
    "and explain whether the available points support a fit."
)
print(result.answer)
print(result.session_dir)
```

Main and Analysis enable the independent verdict by default; Query defaults it
off. Each function accepts `run_verdict`. For continuation arguments and result
fields, consult the actual [Main](../ThermoML_research_agent/NIST_ThermoML_agents/_NIST_ThermoML_main_agent/ThermoML_main_api.py),
[Query](../ThermoML_research_agent/NIST_ThermoML_agents/NIST_ThermoML_query_agent/ThermoML_query_api.py),
and [Analysis](../ThermoML_research_agent/NIST_ThermoML_agents/NIST_ThermoML_analysis_agent/ThermoML_analysis_api.py)
API definitions.

## Interpreting scientific output

Use the reported literature IDs, DOIs, and block identifiers to inspect the
underlying measurements. Separate extracted experimental values from fitted,
derived, interpolated, or proposed values. Provider/model output can vary between
runs even when the prompt and database snapshot stay the same. Keep the session
records and configuration with any result you use in a comparison or publication.
