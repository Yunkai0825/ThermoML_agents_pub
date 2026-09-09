"""
Custom block guidance — pre-execution gate for register_custom_block.
=====================================================================
Cheap parameter gate that blocks malformed ``register_custom_block``
calls BEFORE execution, with an actionable message.  The deep gates
(existing-data refusal, citation verification against the DB, CSV
validation) live inside the tool itself — this hook only ensures the
call arrives complete, so the agent never wastes a turn on a call that
cannot possibly succeed.

Bound to the ``SYNC_TOOL_GUIDANCE_CHECK`` anchor via ``bind_hook`` in
the analysis agent's ``hook_catalog`` (same pattern as
``FittingVariableGuidance``).
"""

from __future__ import annotations

import logging

from ....general_db_query_engine.general_tool_management_helpers.general_tool_options_interactive_hooks import (
    PreExecutionGuidance,
)

_log = logging.getLogger(__name__)

_MIN_BASIS_CHARS = 40

_REQUIRED = ["label", "csv_text", "compounds", "property_name", "basis", "citations"]


class CustomBlockFallbackGuidance(PreExecutionGuidance):
    """Ensure agent-built block registrations arrive fully justified.

    Overrides ``__call__`` because the base class short-circuits when
    all ``required_params`` are present — here the basis-quality check
    must ALWAYS run.
    """

    def __init__(self) -> None:
        super().__init__(
            required_params=list(_REQUIRED),
            context_params=[],
            target_tools=("register_custom_block",),
        )

    def __call__(self, *, tool_name: str, call_kwargs: dict, **_kw) -> str | None:
        if tool_name not in self.target_tools:
            return None
        result = self.check_and_fill(call_kwargs)
        return result if result else ""

    def check_and_fill(self, call_kwargs: dict) -> str | None:
        missing = [p for p in _REQUIRED if not str(call_kwargs.get(p, "")).strip()]
        if missing:
            return (
                f"**BLOCKED — register_custom_block is missing "
                f"`{'`/`'.join(missing)}`.** Agent-built blocks are a "
                f"fallback channel: they require the block data (csv_text "
                f"with `mole_fraction_<compound>`-style columns), the "
                f"compounds and property they describe, a solid `basis` "
                f"justification for every estimated number, and `citations` "
                f"to real ThermoML DOIs the estimates derive from."
            )

        basis = str(call_kwargs.get("basis", "")).strip()
        if len(basis) < _MIN_BASIS_CHARS:
            return (
                f"**BLOCKED — `basis` too short ({len(basis)} chars, need >= "
                f"{_MIN_BASIS_CHARS}).** State HOW each value was estimated "
                f"and FROM WHICH data (pure-component values, RK fits of "
                f"related systems, etc.)."
            )
        return None  # proceed — deep gates run inside the tool


# ------------------------------------------------------------------
#  Module-level singleton
# ------------------------------------------------------------------

_custom_block_guidance = CustomBlockFallbackGuidance()

custom_block_pre_execution_guidance = _custom_block_guidance
"""Callable instance bound to ``SYNC_TOOL_GUIDANCE_CHECK`` anchor."""
