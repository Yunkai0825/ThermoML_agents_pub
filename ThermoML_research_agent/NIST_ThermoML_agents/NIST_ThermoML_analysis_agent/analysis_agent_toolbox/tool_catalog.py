"""
Analysis agent tool catalog — single entry point.
==================================================
Every external consumer of the analysis toolbox should import from
here.  The module exposes three concerns:

1. **Catalog class** — ``AnalysisCatalog`` (class-based, with
   per-tool compaction metadata).
2. **Catalog instance** — ``ANALYSIS_CATALOG``.
3. **Compaction** — ``COMPACTOR_CATALOG`` + ``COMPACTOR_REGISTRY``
   + ``ToolResult`` (from compactor hooks via ``hook_catalog``).

Usage::

    from .tool_catalog import AnalysisCatalog        # class-based
    from .tool_catalog import ANALYSIS_CATALOG       # catalog instance
    from .tool_catalog import COMPACTOR_CATALOG      # structured catalog
    from .tool_catalog import ToolResult
"""

from __future__ import annotations

# ── Base catalog infrastructure ─────────────────────────────
from ...general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import (
    AgentToolCatalog,
)

# ── Compaction hooks (via hook_catalog — the main entry point) ──
from ..analysis_agent_context_hooks.hook_catalog import (
    ToolResult,
    COMPACTOR_CATALOG,
    COMPACTOR_REGISTRY,
)
from ..analysis_agent_context_hooks.compactor_hooks.tool_result_compactor import (
    _analysis_client_factory,
)
from ..ThermoML_analysis_argo_config import AGENT_CONFIG as _cfg

# ── Tool entries from each tool module ──────────────────────
from .query_delegation_tools import TOOL_ENTRIES as _delegation_entries
from .hardcoded_data_tools import TOOL_ENTRIES as _hardcoded_entries
from .fitting_tools import TOOL_ENTRIES as _fitting_entries
from .resolve_tools import TOOL_ENTRIES as _resolve_entries
from .discovery_tools import TOOL_ENTRIES as _discovery_entries
from .sibling_agent_delegation_tools import TOOL_ENTRIES as _sibling_entries
from .agent_specific_tools import TOOL_ENTRIES as _custom_entries
from .composition_library_tools import TOOL_ENTRIES as _comp_lib_entries


# ═══════════════════════════════════════════════════════════════
#  AnalysisCatalog — class-based catalog
# ═══════════════════════════════════════════════════════════════

class AnalysisCatalog(AgentToolCatalog):
    """Analysis agent tool catalog — collects TOOL_ENTRIES from each
    tool module.

    Groups (defined in each module's TOOL_ENTRIES)
    -----------------------------------------------
    - **query_delegation** — delegate to the ThermoML query agent L1 workers.
    - **sibling_delegation** — full L0 query agent (own ReAct loop).
    - **hardcoded_data** — deterministic DB lookups (skip subagent).
    - **fitting** — Redlich–Kister fitting tools (skip subagent).
    - **custom_data** — agent-built fallback blocks (register_custom_block).
    - **resolve** / **discovery** — extra compactors only (sub-step keys).
    """

    pipeline_label = "analysis"

    def __init__(self) -> None:
        super().__init__(client_factory=_analysis_client_factory, cfg=_cfg)

        self.register_many(
            _delegation_entries + _hardcoded_entries + _fitting_entries
            + [entry for entry in _discovery_entries
               if entry.name == "get_pure_values"]
            + _sibling_entries + _custom_entries + _comp_lib_entries
        )

        # Extra compactors for sub-step result keys that aren't
        # standalone tools but may appear in COMPACTOR_REGISTRY.
        for entry in _resolve_entries + [
            item for item in _discovery_entries
            if item.name != "get_pure_values"
        ]:
            if entry.compactor_fn:
                self.add_extra_compactor(entry.name, entry.compactor_fn)


_analysis_catalog = AnalysisCatalog()

ANALYSIS_CATALOG = _analysis_catalog


__all__ = [
    # Catalog instances
    "AnalysisCatalog",
    "ANALYSIS_CATALOG",
    # Compaction
    "COMPACTOR_CATALOG", "COMPACTOR_REGISTRY",
    # ToolResult
    "ToolResult",
]
