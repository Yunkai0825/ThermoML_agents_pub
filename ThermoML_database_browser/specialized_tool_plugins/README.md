# Specialized-tool browser plugins

This package connects persistent specialized-tool artifacts to the browser's
read-only tables, plots, diagnostics, and downloads. The page at
`/specialized-tools` displays existing output; it does not launch a pipeline.

## Current adapter and discovery

[PropertyScreeningBrowserPlugin](property_screening.py), registered as
`property-screening`, reads below the repository's `_output/Query/` directory.
It looks for:

```text
_output/Query/property_screening_runs/*/run_manifest.json
_output/Query/*/data/property_screening/*/run_manifest.json
```

A manifest supplies a valid `screen_*` run ID and declares its tables and
artifacts. The adapter validates manifests before exposing them, returns
`tabular-run-v1` detail data, and rejects paths outside the run's allowed files.
An empty browser list can mean that no matching manifests exist; it does not
trigger computation. A custom adapter instance can receive explicit `roots`.

The producing pipeline is documented in
[the property-screening project](../../ThermoML_research_agent/specialized_tools_pipelines/property_screening_ranking_tool/README.md).

## Adding an adapter

1. Subclass [SpecializedToolBrowserPlugin](base.py).
2. Supply a `PluginManifest` with a lowercase kebab-case `plugin_id`.
3. Normalize native output to `tabular-run-v1`: summaries, tables, plot rows,
   diagnostics, and an explicit artifact allowlist.
4. Register an instance in [build_default_registry()](registry.py).
5. Add temporary-directory tests covering discovery, normalization, and path rejection.

The generic [Flask routes](../helpers/specialized_tool_routes.py) serve registered
adapters without adding a pipeline-specific route. Cache directories contain
data only; the browser does not import executable code discovered in output.
