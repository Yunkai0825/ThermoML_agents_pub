"""
Main agent tool catalog — single entry point.
==============================================
Every external consumer of the main agent toolbox should import from here.

Exposes:
1. **MainCatalog** — class-based tool catalog.
2. **MAIN_CATALOG** — instantiated catalog.
3. **COMPACTOR_CATALOG / COMPACTOR_REGISTRY** — compaction mappings.
4. **ToolResult** — compacted tool result container.
"""
from __future__ import annotations

from ...general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import (
    AgentToolCatalog,
    ToolEntry,
)

# ── Compaction hooks ────────────────────────────────────────
from ..main_agent_context_hooks.hook_catalog import (
    ToolResult,
    COMPACTOR_CATALOG,
    COMPACTOR_REGISTRY,
)

# ── Subagent delegation tools ──────────────────────────────
from .subagent_delegation_tools import TOOL_ENTRIES as _DELEGATION_ENTRIES

# ── Tool menu (browse + execute subagent tools directly) ────
from .tool_menu import TOOL_ENTRIES as _MENU_ENTRIES


# ═══════════════════════════════════════════════════════════════
#  MainCatalog
# ═══════════════════════════════════════════════════════════════

class MainCatalog(AgentToolCatalog):
    """Tool catalog for the ThermoML Main Agent L0 orchestrator."""

    pipeline_label = "main"

    def __init__(self) -> None:
        super().__init__()
        self.register_many(_DELEGATION_ENTRIES + _MENU_ENTRIES)


MAIN_CATALOG = MainCatalog()

__all__ = [
    "MainCatalog",
    "MAIN_CATALOG",
    "COMPACTOR_CATALOG",
    "COMPACTOR_REGISTRY",
    "ToolResult",
]
