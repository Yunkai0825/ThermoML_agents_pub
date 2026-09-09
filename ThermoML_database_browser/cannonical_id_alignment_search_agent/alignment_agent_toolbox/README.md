# Alignment tool catalog

[tool_catalog.py](tool_catalog.py) registers 16 callable Python tools for the
Argo alignment loop. [mcp_tools.py](mcp_tools.py) contains their implementations.
Tools return native JSON-serializable objects, not pre-encoded JSON strings;
the shared engine serializes results at the tool boundary.

| Tool | Role |
|---|---|
| `parse_smart_search` | Parse search text using deterministic helpers |
| `resolve_entity` | Resolve names to typed canonical IDs |
| `search_titles` | Score local paper titles |
| `validate_field`, `validate_bibliography` | Validate resolved IDs and bibliography |
| `review_top_results` | Review candidate search results |
| `set_field`, `get_current_fields`, `finalize_fields` | Update, inspect, and finish form state |
| `fill_bibliography_block`, `fill_chemistry_block` | Fill bibliography and chemistry fields |
| `fill_properties_block`, `fill_variables_block` | Fill property and variable fields |
| `fill_measurements_block`, `fill_constraints_block` | Fill measurement and constraint fields |
| `escalate_to_query_agent` | Explicitly invoke the live Query agent |

`AlignmentL0Catalog` extends the research project's `AgentToolCatalog`.
Entries set `skip_compactor` and `skip_subagent` so normal automatic processing
does not add a worker around these compact field-resolution results. The
explicit escalation tool can still invoke the Query agent.

Mutable `_SearchFields` state is held in a `ContextVar`. The public alignment API
enters `alignment_fields_context()` for one request and snapshots the result
before restoring the prior context. This prevents concurrent browser requests
from sharing form state.

Use [the alignment API](../README.md) rather than manually managing tool state
for ordinary integrations. The explicit catalog is authoritative when adding or
renaming a tool.
