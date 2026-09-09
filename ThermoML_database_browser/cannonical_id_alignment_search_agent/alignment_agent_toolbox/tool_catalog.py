"""
Alignment agent tool catalog.
=============================
Registers all MCP tools the alignment agent can call during its
ReAct loop.  Follows the same pattern as QueryL0Catalog.

Usage::

    from .tool_catalog import AlignmentL0Catalog, L0_CATALOG
"""

from __future__ import annotations

import sys, os

# Add workspace root so general helpers are importable
_WS_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'ThermoML_research_agent'))
if _WS_ROOT not in sys.path:
    sys.path.insert(0, _WS_ROOT)

from NIST_ThermoML_agents.general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import (
    AgentToolCatalog,
    ToolEntry,
)

from . import mcp_tools as _t


# ═══════════════════════════════════════════════════════════════
#  AlignmentL0Catalog
# ═══════════════════════════════════════════════════════════════

class AlignmentL0Catalog(AgentToolCatalog):
    """L0 tool catalog for the canonical ID alignment agent.

    All tools are skip_compactor / skip_subagent because the alignment
    agent is a lightweight agent that returns structured JSON from
    deterministic helpers.
    """

    pipeline_label = "alignment"

    def __init__(self) -> None:
        super().__init__()
        self.register_many([
            # ── Parsing ──────────────
            ToolEntry(
                "parse_smart_search", _t.parse_smart_search,
                group="parsing", skip_compactor=True, skip_subagent=True,
            ),
            # ── ID Resolution ────────
            ToolEntry(
                "resolve_entity", _t.resolve_entity,
                group="resolution", skip_compactor=True, skip_subagent=True,
            ),
            # ── Bibliography ─────────
            ToolEntry(
                "search_titles", _t.search_titles,
                group="bibliography", skip_compactor=True, skip_subagent=True,
            ),
            # ── Validation ───────────
            ToolEntry(
                "validate_field", _t.validate_field,
                group="validation", skip_compactor=True, skip_subagent=True,
            ),
            ToolEntry(
                "validate_bibliography", _t.validate_bibliography,
                group="validation", skip_compactor=True, skip_subagent=True,
            ),
            # ── Review ───────────────
            ToolEntry(
                "review_top_results", _t.review_top_results,
                group="review", skip_compactor=True, skip_subagent=True,
            ),
            # ── Field setters ────────
            ToolEntry(
                "set_field", _t.set_field,
                group="fields", skip_compactor=True, skip_subagent=True,
            ),
            ToolEntry(
                "get_current_fields", _t.get_current_fields,
                group="fields", skip_compactor=True, skip_subagent=True,
            ),
            ToolEntry(
                "finalize_fields", _t.finalize_fields,
                group="fields", skip_compactor=True, skip_subagent=True,
            ),
            # ── Block fillers (guided field-by-field) ──
            ToolEntry(
                "fill_bibliography_block", _t.fill_bibliography_block,
                group="blocks", skip_compactor=True, skip_subagent=True,
            ),
            ToolEntry(
                "fill_chemistry_block", _t.fill_chemistry_block,
                group="blocks", skip_compactor=True, skip_subagent=True,
            ),
            ToolEntry(
                "fill_properties_block", _t.fill_properties_block,
                group="blocks", skip_compactor=True, skip_subagent=True,
            ),
            ToolEntry(
                "fill_variables_block", _t.fill_variables_block,
                group="blocks", skip_compactor=True, skip_subagent=True,
            ),
            ToolEntry(
                "fill_measurements_block", _t.fill_measurements_block,
                group="blocks", skip_compactor=True, skip_subagent=True,
            ),
            ToolEntry(
                "fill_constraints_block", _t.fill_constraints_block,
                group="blocks", skip_compactor=True, skip_subagent=True,
            ),
            # ── Escalation ───────────
            ToolEntry(
                "escalate_to_query_agent", _t.escalate_to_query_agent,
                group="escalation", skip_compactor=True, skip_subagent=True,
            ),
        ])


# ═══════════════════════════════════════════════════════════════
#  Module-level convenience
# ═══════════════════════════════════════════════════════════════

_l0_catalog = AlignmentL0Catalog()

L0_CATALOG = _l0_catalog
__all__ = [
    "AlignmentL0Catalog",
    "L0_CATALOG",
]
