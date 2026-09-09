"""
Query agent tool catalog — single entry point.
===============================================
Every external consumer of the query toolbox should import from here.
The module exposes three concerns:

1. **Catalog class** — ``QueryL0Catalog`` (memory tools, class-based).
2. **Catalog instance** — ``L0_CATALOG``.
3. **Compaction** — ``COMPACTOR_CATALOG`` + ``COMPACTOR_REGISTRY``
   + ``ToolResult`` (from compactor hooks).

Usage::

    from .tool_catalog import QueryL0Catalog         # class-based
    from .tool_catalog import L0_CATALOG             # catalog instance
    from .tool_catalog import COMPACTOR_CATALOG      # structured catalog
    from .tool_catalog import ToolResult
"""

from __future__ import annotations

# ── Base catalog infrastructure ─────────────────────────────
from ...general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import AgentToolCatalog, ToolEntry

# ── Compaction hooks (via hook_catalog — the main entry point) ──
from ..query_agent_context_hooks.hook_catalog import (
    ToolResult,
    COMPACTOR_CATALOG,
    COMPACTOR_REGISTRY,
)

# ── Memory MCP tools (used by L0 orchestrator) ─────────────
from ...general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers import (
    memory_management_MCP_tools as _mem_tools,
)


# ═══════════════════════════════════════════════════════════════
#  QueryL0Catalog — memory tools (no compaction)
# ═══════════════════════════════════════════════════════════════

class QueryL0Catalog(AgentToolCatalog):
    """L0 orchestrator tool catalog — memory tools only.

    Memory tools return strings / simple dicts and never need
    compaction, so both layers are skipped.
    """

    pipeline_label = "query"

    def __init__(self) -> None:
        super().__init__()
        self.register_many([
            ToolEntry("memory_read",           _mem_tools.memory_read,           group="memory", skip_compactor=True, skip_subagent=True),
            ToolEntry("memory_append_history",  _mem_tools.memory_append_history,  group="memory", skip_compactor=True, skip_subagent=True),
            ToolEntry("memory_add_result",      _mem_tools.memory_add_result,      group="memory", skip_compactor=True, skip_subagent=True),
            ToolEntry("memory_catalog_add",     _mem_tools.memory_catalog_add,     group="memory", skip_compactor=True, skip_subagent=True),
            ToolEntry("memory_catalog_remove",  _mem_tools.memory_catalog_remove,  group="memory", skip_compactor=True, skip_subagent=True),
            ToolEntry("memory_catalog_list",    _mem_tools.memory_catalog_list,    group="memory", skip_compactor=True, skip_subagent=True),
            ToolEntry("memory_compact",         _mem_tools.memory_compact,         group="memory", skip_compactor=True, skip_subagent=True),
            ToolEntry("memory_reset",           _mem_tools.memory_reset,           group="memory", skip_compactor=True, skip_subagent=True),
        ])


_l0_catalog = QueryL0Catalog()

L0_CATALOG = _l0_catalog


__all__ = [
    # Catalog instances
    "QueryL0Catalog",
    "L0_CATALOG",
    # Compaction
    "COMPACTOR_CATALOG", "COMPACTOR_REGISTRY",
    # ToolResult
    "ToolResult",
]
