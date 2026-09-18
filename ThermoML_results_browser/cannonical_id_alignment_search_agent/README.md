# Canonical ID Alignment Search Agent

LLM-powered sub-agent that resolves free-text search queries into
canonical ThermoML index IDs.  Used by the browser when the
`agentic_all_fields` setting is enabled, or when a user query
cannot be resolved by deterministic search alone.

## Architecture

```
alignment_agent_api.py          ← public entry point
  ├── hardcoded_search_helpers/ ← fast deterministic path
  └── alignment_agent_argo_engine/
        └── Argo ReAct client
              ├── alignment_agent_toolbox/  (16 MCP tools)
              └── alignment_agent_workflows/  (L0 orchestrator)
```

Two execution paths:
- **Hardcoded** — deterministic parse + validate + search (no LLM)
- **Argo agent** — ReAct loop with 16 tools for complex queries

## Sub-packages

| Directory | Purpose |
|-----------|---------|
| `alignment_agent_api.py` | `alignment_agent_run()` — public API, routes to hardcoded or argo |
| `alignment_agent_argo_config.py` | Model name, system prompt, temperature, max turns |
| `alignment_agent_argo_engine/` | Argo LLM ReAct client (`AlignmentClient`) |
| `alignment_agent_toolbox/` | 16 MCP tools the agent can call |
| `alignment_agent_workflows/` | L0 orchestrator workflow |
| `hardcoded_search_helpers/` | Deterministic search, validation, review |

## Public API

From the repository root, run deterministic alignment against the local index:

```python
from ThermoML_results_browser.cannonical_id_alignment_search_agent.alignment_agent_api import (
    alignment_agent_run,
)

result = alignment_agent_run(
    search_text="ethanol + viscosity",
    settings={"use_agent": False},
)
print(result.fields)
```

Set `settings={"use_agent": True}` to use the Argo agent; that path requires
provider access and is the default when settings are omitted.
`AlignmentResult` exposes the resolved `fields`, `answer`, `resolution_log`,
`iterations`, `elapsed_seconds`, and `timed_out` values.
