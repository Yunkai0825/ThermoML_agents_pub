# Canonical ID alignment search agent

This package converts free-text search input into fields accepted by the
ThermoML browser. It provides a deterministic path and an Argo ReAct path. The
directory spelling `cannonical_id_alignment_search_agent` is retained in imports.

## Public API

Run Python from the repository root with the runtime dependencies and local
databases installed:

```python
from ThermoML_database_browser.cannonical_id_alignment_search_agent.alignment_agent_api import alignment_agent_run

result = alignment_agent_run(
    "ethanol + viscosity",
    settings={"use_agent": False},
)
print(result.fields)
print(result.resolution_log)
```

This explicitly selects deterministic alignment and makes no model request.
With `use_agent=True` (the API default), the function starts the Argo workflow.
The first argument is `search_text`; options belong in the `settings` dictionary.

| Setting | Meaning |
|---|---|
| `use_agent` | Boolean; select Argo (`True`, default) or deterministic (`False`) alignment |
| `entry_limit` | Positive integer guiding Argo resolution/search result limits |
| `max_wait_seconds` | Positive integer time budget for the Argo workflow |
| `allow_query_agent` | Boolean hint enabling Query-agent escalation in the Argo workflow |
| `agentic_all_fields` | Boolean hint requesting the block-filler workflow |

The deterministic API path calls `dispatch_search()` and maps the first parsed
AND-block to form fields. Agent-specific limits/escalation hints apply to the
Argo path. The lower-level validated dispatcher offers additional deterministic
validation/review options; see [helper documentation](hardcoded_search_helpers/README.md).

`AlignmentResult` includes `fields`, `answer`, `iterations`, `elapsed_seconds`,
`timed_out`, and `resolution_log`, plus `to_dict()`. It represents aligned form
fields, not the final browser paper-search result list. Resolved entities can
include canonical IDs and scores.

## Modules

| Module | Role |
|---|---|
| [alignment_agent_api.py](alignment_agent_api.py) | Public entry point and result conversion |
| [alignment_agent_argo_config.py](alignment_agent_argo_config.py) | Provider, model, and engine settings |
| [alignment_agent_argo_engine/](alignment_agent_argo_engine/README.md) | `AlignmentClient` factory |
| [alignment_agent_toolbox/](alignment_agent_toolbox/README.md) | Explicit tool catalog and context-local form state |
| [alignment_agent_workflows/](alignment_agent_workflows/README.md) | Workflow prompt loading and shared ReAct execution |
| [hardcoded_search_helpers/](hardcoded_search_helpers/README.md) | Parsing, local resolution, validation, and review |

The Argo workflow reads `ARGO_API_USER` from the server environment. Its endpoint
is currently declared directly as `API_URL` in the alignment config. The normal
browser does not automatically install the Anthropic benchmark adapter. See
[the browser guide](../README.md) for configuration and local/API boundaries.
