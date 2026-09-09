# query_agent_toolbox

Tool catalog and tool implementations for the ThermoML Query Agent L0 orchestrator.

## Public API

```python
from .tool_catalog import QueryL0Catalog       # class-based catalog
from .tool_catalog import L0_CATALOG           # validated catalog instance
from .tool_catalog import ToolResult           # compacted tool result container
from .tool_catalog import COMPACTOR_CATALOG    # structured compactor catalog
from .tool_catalog import COMPACTOR_REGISTRY   # flat compactor dict
```

`QueryL0Catalog` extends `AgentToolCatalog` with memory-management
MCP tools (`save_working_memory`, `read_working_memory`, `list_memory_files`).
L1 search tools are registered explicitly by `l1_query_dispatcher.py`. The
broader `general_db_search_tool_registry` is a discovery inventory, not the
runtime source of truth for Query L1.

## Files

| File | Purpose |
|------|---------|
| `__init__.py` | Re-exports the public API from `tool_catalog` |
| `tool_catalog.py` | `QueryL0Catalog(AgentToolCatalog)` + validated catalog instance |
