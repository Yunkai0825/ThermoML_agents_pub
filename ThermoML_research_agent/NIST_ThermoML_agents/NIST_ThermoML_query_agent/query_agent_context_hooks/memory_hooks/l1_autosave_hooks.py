"""L1 auto-save hook — wraps ``dispatch_l1_query`` to persist results.

The L0 orchestrator's LLM agent often skips ``memory_add_result`` calls.
This wrapper ensures every L1 return is persisted in working memory
regardless of LLM compliance.

Usage::

    from ..memory_hooks.l1_autosave_hooks import L1AutoSaver

    saver = L1AutoSaver(dispatch_l1_query, mem_tools)
    tools["L1_query"] = saver
    # ... after the run ...
    print(saver.call_count)  # number of L1 calls made
"""

from __future__ import annotations

import json
import logging
from typing import Callable
from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    GLOBAL_PREFIX_BY_FIELD,
    require_global_id,
)
from ...query_agent_workflows.strict_output_contracts import validate_l1_query_output

from ....general_db_query_engine.general_argo_engine_helpers import anchor
from ....general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers import _memory_hooks_anchors_catalog as mem_anchor
from ....general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers.envelope_memory_digest import (
    digest_with_validation,
)

log = logging.getLogger("L0-Orchestrator")


# ---------------------------------------------------------------------------
# Helpers — parse L1 JSON and format as markdown for working memory
# ---------------------------------------------------------------------------

def _parse_l1_json(text: str) -> dict | None:
    """Parse the exact L1 JSON contract. Return ``None`` on invalid JSON."""
    try:
        obj = json.loads(text.strip())
        return obj if isinstance(obj, dict) else None
    except (json.JSONDecodeError, ValueError):
        return None


def _validate_l1_result(data: dict) -> None:
    """Validate the non-lossy L1 result envelope before persistence."""
    validate_l1_query_output(data)


def _apply_core_id_updates(mem_tools, core_id_updates: list[dict]) -> int:
    """Push tool-constructed core ID updates into the catalog."""
    added = 0
    global_fields = {
        "lit": "lit_num_id", "comp": "comp_num_id", "prop": "prop_num_id",
        "var": "var_num_id", "constr": "constr_num_id", "meas": "meas_num_id",
        "phase": "phase_num_id", "blocktype": "blocktype_num_id",
        "rxntype": "rxn_type_num_id", "solvent": "solvent_num_id",
    }
    for entry in core_id_updates:
        if not isinstance(entry, dict):
            raise ValueError(
                "L1_RESULT_SCHEMA_ERROR: each core_id_update must be an object"
            )
        expected = {"action", "core_GLOB_id", "registry_id", "name"}
        if set(entry) != expected:
            raise ValueError(
                "L1_RESULT_SCHEMA_ERROR: core_id_update requires exactly "
                "action, core_GLOB_id, registry_id, name"
            )
        if entry["action"] != "add":
            raise ValueError(
                "L1_RESULT_SCHEMA_ERROR: core_id_update.action must be add"
            )
        global_id = entry["core_GLOB_id"]
        matches = [
            (entity_type, field)
            for entity_type, field in global_fields.items()
            if isinstance(global_id, str)
            and global_id.startswith(GLOBAL_PREFIX_BY_FIELD[field])
        ]
        if len(matches) != 1:
            raise ValueError(
                "L1_RESULT_SCHEMA_ERROR: core_GLOB_id has no unique type"
            )
        entity_type, global_field = matches[0]
        require_global_id(global_field, global_id)
        if not isinstance(entry["registry_id"], str) or not entry["registry_id"]:
            raise ValueError(
                "L1_RESULT_SCHEMA_ERROR: registry_id must be a non-empty string"
            )
        if not isinstance(entry["name"], str) or not entry["name"]:
            raise ValueError(
                "L1_RESULT_SCHEMA_ERROR: name must be a non-empty string"
            )
        mem_tools.memory_catalog_add(
            entity_type, global_id, entry["registry_id"], entry["name"]
        )
        added += 1
    return added


class L1AutoSaver:
    """Callable wrapper that auto-persists L1 query results in working memory.

    Parameters
    ----------
    dispatch_fn : callable
        The raw L1 dispatch function
        ``(purpose, instruction, id_catalog, context) -> str``.
    mem_tools
        The ``memory_management_MCP_tools`` module (or any object
        exposing ``memory_add_result`` and ``memory_append_history``).
    """

    def __init__(self, dispatch_fn: Callable[..., str], mem_tools, hooks=None) -> None:
        self._dispatch = dispatch_fn
        self._mem = mem_tools
        self._hooks = hooks
        self.call_count: int = 0
        self._returns_subagent_answer = True

    def __call__(
        self,
        purpose: str,
        instruction: str,
        id_catalog: str = "",
        context: str = "",
    ) -> str:
        if not isinstance(purpose, str) or not purpose.strip():
            raise ValueError(
                "TOOL_ARGUMENT_REFINEMENT_REQUIRED: L1_query.purpose must be a non-empty string."
            )
        if not isinstance(instruction, str) or not instruction.strip():
            raise ValueError(
                "TOOL_ARGUMENT_REFINEMENT_REQUIRED: L1_query.instruction must be a non-empty string."
            )

        result_text = self._dispatch(
            purpose=purpose,
            instruction=instruction,
            id_catalog=id_catalog,
            context=context,
        )
        self.call_count += 1
        key = f"L1_query_{self.call_count}"

        # ── Parse and persist the compact L1 digest (full JSON stays on
        # the tool-history rail for the grounding gate / final merge) ──
        parsed = _parse_l1_json(result_text)
        if parsed is None:
            raise ValueError("L1_RESULT_SCHEMA_ERROR: L1_query must return one JSON object")
        _validate_l1_result(parsed)
        stored_result, validation_verdict = digest_with_validation(
            parsed, key=key, tool_name="L1_query", pair="Qi/L1")

        core_id_updates = parsed["core_id_updates"]
        if core_id_updates:
            n_added = _apply_core_id_updates(self._mem, core_id_updates)
            if n_added:
                log.info("ID catalog: %d entries added from %s", n_added, key)

        try:
            if self._hooks is not None:
                stored_result = anchor(
                    mem_anchor.SYNC_MEMORY_RESULT_STORE,
                    self._hooks.engine_hooks,
                    key=key,
                    content=stored_result,
                    purpose=purpose,
                    instruction=instruction,
                ) or stored_result
            self._mem.memory_add_result(key, stored_result)

            history_line = (
                f"[L1] {purpose[:120]} → stored as {key} · "
                f"validation: {validation_verdict}"
            )
            if self._hooks is not None:
                history_line = anchor(
                    mem_anchor.SYNC_MEMORY_HISTORY_APPEND,
                    self._hooks.engine_hooks,
                    content=history_line,
                    key=key,
                    purpose=purpose,
                ) or history_line
            self._mem.memory_append_history(history_line)
            log.info("Auto-saved L1 result as '%s'", key)
        except Exception:
            log.exception("Required L1 result persistence failed for %s", key)
            raise

        return result_text
