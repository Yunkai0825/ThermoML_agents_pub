# Alignment Agent Toolbox

16 MCP tools available to the Argo ReAct agent during its reasoning loop.
Each tool is a Python function returning a JSON-serialisable string.

## Tool Catalog

| # | Tool | Description |
|---|------|-------------|
| 1 | `resolve_entity` | Resolve free-text to canonical IDs (compound, property, etc.) |
| 2 | `search_titles` | Score paper titles by keyword relevance |
| 3 | `validate_field` | Check a resolved value against the index registry |
| 4 | `validate_bibliography` | Check title / author / DOI against known papers |
| 5 | `set_field` | Set a search-form field value |
| 6 | `get_current_fields` | Inspect what fields have been set so far |
| 7 | `parse_smart_search` | Run the deterministic search parser |
| 8 | `review_top_results` | Run review workers on resolved query |
| 9 | `fill_bibliography_block` | Resolve & fill bibliography fields |
| 10 | `fill_chemistry_block` | Resolve & fill chemistry fields |
| 11 | `fill_properties_block` | Resolve & fill property fields |
| 12 | `fill_variables_block` | Resolve & fill variable fields |
| 13 | `fill_measurements_block` | Resolve & fill measurement fields |
| 14 | `fill_constraints_block` | Resolve & fill constraint fields |
| 15 | `escalate_to_query_agent` | Call ThermoML query agent for complex queries |
| 16 | `finalize_fields` | Mark fields as complete, return final state |

## Files

| File | Purpose |
|------|---------|
| `mcp_tools.py` | Tool implementations + `_SearchFields` state object |
| `tool_catalog.py` | `AlignmentL0Catalog` — registers tools as `ToolEntry` objects |
| `__init__.py` | Package init |

`AlignmentL0Catalog` extends `AgentToolCatalog` from the general agent
infrastructure.  All tools are marked `skip_compactor` / `skip_subagent`
because the alignment agent runs as a lightweight single-layer agent.
