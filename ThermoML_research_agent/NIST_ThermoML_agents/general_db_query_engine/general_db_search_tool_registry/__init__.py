"""general_db_search_tool_registry — auto-discovered catalog of all card_db_search_tools."""

from .db_search_tool_registry import (
    SearchToolEntry,
    SEARCH_TOOL_REGISTRY,
    COMPACTOR_MODULE_MAP,
    CATEGORIES,
    list_tools_with_compactors,
    list_tools_without_compactors,
    tools_by_category,
    generate_report_md,
)

__all__ = [
    "SearchToolEntry",
    "SEARCH_TOOL_REGISTRY",
    "COMPACTOR_MODULE_MAP",
    "CATEGORIES",
    "list_tools_with_compactors",
    "list_tools_without_compactors",
    "tools_by_category",
    "generate_report_md",
]
