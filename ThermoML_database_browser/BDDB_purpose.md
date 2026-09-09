# Browser purpose and scope

The ThermoML Database Browser provides a local interface to the prepared
ThermoML data and the research agents. It supports structured search, paper and
compound inspection, deterministic analysis, agent-assisted questions, and
viewing saved freeform and benchmark results.

It reads the databases installed with the sibling `ThermoML_research_agent`
project. It does not build card databases or download the source corpus when
started. Available papers and properties depend on the installed dataset.

Freeform runs are shared and persistent under the repository's `_output`
directory. Benchmark archives under `_benchmark` are browsable as a separate,
read-only history category. Detailed output is available without a browser
login or debug switch; live model requests still require a configured provider.

See [the browser guide](README.md) for setup and [architecture](ARCHITECTURE.md)
for module boundaries.
