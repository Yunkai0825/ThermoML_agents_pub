"""agent_specific_tools — analysis-agent-only tool modules.

Currently hosts the AGENT-BUILT fallback data channel
(``register_custom_block``).  Re-exports ``TOOL_ENTRIES`` for
registration by ``AnalysisCatalog``.
"""

from .custom_block_tools import TOOL_ENTRIES, register_custom_block

__all__ = ["TOOL_ENTRIES", "register_custom_block"]
