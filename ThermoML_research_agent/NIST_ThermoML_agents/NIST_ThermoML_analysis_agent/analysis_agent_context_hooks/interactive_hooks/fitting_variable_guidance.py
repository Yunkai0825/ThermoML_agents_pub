"""
Fitting variable guidance — pre-execution hook for fitting tools.
=================================================================
Subclass of :class:`PreExecutionGuidance` that auto-detects
``x_vars``, ``y_props``, and ``x_vars_constrained`` for the unified
``fit_block`` tool entry.

Bound to the ``SYNC_TOOL_GUIDANCE_CHECK`` anchor via ``bind_hook``
in the analysis agent's ``hook_catalog``.

Architecture
------------
- General base: ``general_tool_options_interactive_hooks.PreExecutionGuidance``
- This subclass: overrides ``check_and_fill()`` with ThermoML-specific
  column detection and temperature constraint logic.
- Anchor dispatch: ``SYNC_TOOL_GUIDANCE_CHECK`` → ``__call__`` →
  filters by ``target_tools`` → ``check_and_fill()``
"""

from __future__ import annotations

import logging

import numpy as np
from ThermoML_raw_json_to_card_db_parsers.id_schema import require_block_id

from ....general_db_query_engine.general_tool_management_helpers.general_tool_options_interactive_hooks import (
    PreExecutionGuidance,
    block_msg,
)
from ...ThermoML_core_calc_tools.csv_io_helpers import (
    extract_block_arrays,
    identify_columns,
)

_log = logging.getLogger(__name__)

_REQUIRED = ["x_vars", "y_props", "x_vars_constrained"]
_CONTEXT  = ["doi", "block_number"]


# ------------------------------------------------------------------
#  Concrete subclass
# ------------------------------------------------------------------

class FittingVariableGuidance(PreExecutionGuidance):
    """Auto-fill fitting variable params from block data.

    When the agent omits ``x_vars``, ``y_props``, or
    ``x_vars_constrained``, fetches the block directly (no extra
    ``inspect_block`` round-trip) and resolves them.
    """

    def __init__(self) -> None:
        super().__init__(
            required_params=list(_REQUIRED),
            context_params=list(_CONTEXT),
            target_tools=("fit_block",),
        )

    # ── Core logic ───────────────────────────────────────────

    def check_and_fill(self, call_kwargs: dict) -> str | None:
        """Fetch block data, identify columns, auto-fill missing params."""
        doi = call_kwargs["doi"]
        if not isinstance(doi, str) or not doi:
            raise TypeError("fit_block doi must be a non-empty string")
        block_number = require_block_id(call_kwargs["block_number"])
        property_hint = call_kwargs.get("property_hint", "")
        composition_hint = call_kwargs.get("composition_hint", "mole_fraction")

        try:
            bd = extract_block_arrays(
                doi, block_number,
                BLKsubsys_id=call_kwargs.get("BLKsubsys_id"),
                property_filter=property_hint or None,
            )
            if not bd.ok:
                return (
                    f"**BLOCKED — cannot extract block {block_number} from {doi}: "
                    f"{bd.error}.** Specify `x_vars`, `y_props`, "
                    f"`x_vars_constrained` manually."
                )
            match = identify_columns(
                bd.columns, property_hint, composition_hint, metadata=bd.metadata,
            )
        except Exception as exc:
            _log.warning("guidance auto-detect failed: %s", exc, exc_info=True)
            return (
                f"**BLOCKED — auto-detection error: {exc}.** "
                f"Specify `x_vars`, `y_props`, `x_vars_constrained` manually."
            )

        filled: list[str] = []

        # --- Auto-fill x_vars --------------------------------------
        if not call_kwargs.get("x_vars"):
            if match.x_column:
                call_kwargs["x_vars"] = [match.x_column]
                filled.append(f"x_vars→{match.x_column}")
            elif match.x_columns:
                call_kwargs["x_vars"] = [match.x_columns[0]]
                filled.append(f"x_vars→{match.x_columns[0]}")
            else:
                return block_msg(
                    "x_vars", bd.columns,
                    identified_x=match.x_columns,
                    identified_y=match.y_columns,
                    reason="No composition column found in block.",
                    filled=filled,
                )

        # --- Auto-fill y_props -------------------------------------
        if not call_kwargs.get("y_props"):
            if match.y_column:
                call_kwargs["y_props"] = [match.y_column]
                filled.append(f"y_props→{match.y_column}")
            elif match.y_columns:
                call_kwargs["y_props"] = [match.y_columns[0]]
                filled.append(f"y_props→{match.y_columns[0]}")
            else:
                return block_msg(
                    "y_props", bd.columns,
                    identified_x=match.x_columns,
                    identified_y=match.y_columns,
                    reason="No property column found in block.",
                    filled=filled,
                )

        # --- Auto-fill x_vars_constrained --------------------------
        if call_kwargs.get("x_vars_constrained") is None:
            constraint = _auto_temperature_constraint(bd)
            if constraint is not None:
                call_kwargs["x_vars_constrained"] = constraint
                for col, spec in constraint.items():
                    filled.append(f"x_vars_constrained→{col}={spec['value']}")
            else:
                call_kwargs["x_vars_constrained"] = {}
                filled.append("x_vars_constrained→{}")

        if filled:
            _log.info("guidance hard-parse filled: %s", ", ".join(filled))

        return None   # all params present or auto-filled → proceed


# ------------------------------------------------------------------
#  Module-level hook instance
# ------------------------------------------------------------------

_fitting_guidance = FittingVariableGuidance()

fitting_pre_execution_guidance = _fitting_guidance
"""Callable instance bound to ``SYNC_TOOL_GUIDANCE_CHECK`` anchor."""


# ------------------------------------------------------------------
#  Helpers
# ------------------------------------------------------------------

def _auto_temperature_constraint(bd) -> dict | None:
    """Return a temperature constraint dict or None if no temp column."""
    temp_col = next((c for c in bd.columns if "temperature" in c.lower()), None)
    if not temp_col or temp_col not in bd.arrays:
        return None
    t_arr = bd.arrays[temp_col]
    valid_t = t_arr[~np.isnan(t_arr)]
    unique_temps = np.unique(valid_t)
    if len(unique_temps) <= 1:
        return None   # single-temperature block — no constraint needed
    target_T = float(unique_temps[len(unique_temps) // 2])
    selected_T = float(unique_temps[np.argmin(np.abs(unique_temps - target_T))])
    return {temp_col: {"value": selected_T, "tol": 0.5}}

