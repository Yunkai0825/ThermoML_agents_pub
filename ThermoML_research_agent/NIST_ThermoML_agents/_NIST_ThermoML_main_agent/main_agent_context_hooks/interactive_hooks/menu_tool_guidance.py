"""
Menu tool guidance — main-agent pre-execution hook.
====================================================
Thin subclass of :class:`ToolCallGuidance` that supplies the main
agent's tool-menu registry.  All two-tier validation logic lives in
the general base class.

Bound to ``SYNC_TOOL_GUIDANCE_CHECK`` in the main agent's hook catalog.
"""

from __future__ import annotations

from ....general_db_query_engine.general_tool_management_helpers.general_tool_options_interactive_hooks import (
    ToolCallGuidance,
)


def _get_registry():
    """Lazy import to avoid circular import at module load time."""
    from ...main_agent_toobox.tool_menu._registry_builder import get_registry
    return get_registry()


class MenuToolGuidance(ToolCallGuidance):
    """Main-agent specialization — supplies the main agent's registry."""

    def __init__(self) -> None:
        super().__init__(registry_provider=_get_registry)


_menu_tool_guidance = MenuToolGuidance()

menu_tool_pre_execution_guidance = _menu_tool_guidance
"""Callable instance bound to ``SYNC_TOOL_GUIDANCE_CHECK`` anchor."""
