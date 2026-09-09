"""Working memory for the ThermoML Query Agent.
================================================
Inherits the shared ID Catalog from ``BaseWorkingMemory`` and adds
file-backed persistence via ``general_memory_management_tools_hooks_helpers``.

The query agent uses an LLM-driven memory model: the L0 orchestrator
explicitly calls MCP tools (``memory_catalog_add``, ``memory_append_history``,
etc.) to manage memory.  ``QueryWorkingMemory`` sits as a thin in-process
mirror that can also be populated by ``record_tool_result()``
(same pattern as the analysis agent) for automatic entity extraction.

Usage::

    from ..memory_hooks.working_memory_hooks import (
        QueryWorkingMemory,
        init_working_memory,
        make_wm_loader,
    )
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from ....general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers.general_memory_hooks import (
    BaseWorkingMemory,
    _global_id_field,
)

log = logging.getLogger("QUERY-WM")

class QueryWorkingMemory(BaseWorkingMemory):
    """Query agent working memory with file-backed persistence.

    The file-backed ``WorkingMemory`` (in ``memory_local_storage_io``)
    handles the actual on-disk markdown file.  This class maintains
    the in-process ID catalog and can optionally auto-extract entities
    from tool results when used with the ``_wrap_tool`` pattern.

    Parameters
    ----------
    mem_tools : module
        The ``memory_management_MCP_tools`` module (or compatible object).
        If None, the memory operates in read-only / in-process mode.
    """

    def __init__(self, mem_tools=None):
        super().__init__()
        self._mem_tools = mem_tools

    # ── Auto-extract from tool results ───────────────────────

    def record_tool_result(self, tool_name: str, result: dict) -> None:
        """Automatically extract and store entities from tool results.

        Resolver results are ingested only from their canonical global-ID
        fields. Tool arguments captured by the instrumentation layer identify
        the entity type for generic ``resolve_ids`` calls.
        """
        resolver_entities = {
            "resolve_compound_ids": "compound",
            "resolve_property_ids": "property",
            "resolve_measurement_ids": "measurement",
            "resolve_reference_ids": "reference",
        }
        entity = resolver_entities.get(tool_name)
        if tool_name == "resolve_ids":
            entity = result["entity_type"] if "error" not in result else None
        elif tool_name == "search_id_alignment":
            entity = result["entity_type"] if "error" not in result else None

        specs = {
            "compound": ("comp", "comp_num_id", "common_name", "comp_id"),
            "property": ("prop", "prop_num_id", "prop_name", "prop_id"),
            "measurement": ("meas", "meas_num_id", "method_name", "meas_id"),
            "reference": ("lit", "lit_num_id", "doi", "lit_id"),
            "variable": ("var", "var_num_id", "var_name", "var_id"),
            "constraint": ("constr", "constr_num_id", "constr_name", "constr_id"),
            "phase": ("phase", "phase_num_id", "phase_name", "phase_id"),
            "solvent": ("solvent", "solvent_num_id", "common_name", "inchi_key"),
            "block_type": ("blocktype", "blocktype_num_id", "block_type", "block_type"),
            "reaction_type": ("rxntype", "rxn_type_num_id", "rxn_type_name", "rxn_type_id"),
        }
        if entity in specs and "error" not in result:
            required = {"entity_type", "n_results", "results"}
            if tool_name == "search_id_alignment":
                required.add("query")
            else:
                required.add("queries")
            missing = sorted(required - set(result))
            unknown = sorted(set(result) - required)
            if missing or unknown:
                raise ValueError(
                    f"{tool_name} has missing={missing} and unknown={unknown} result fields"
                )
            etype, global_field, name_field, registry_field = specs[entity]
            if not isinstance(result["results"], list):
                raise TypeError(f"{tool_name}.results must be an array")
            for match in result["results"]:
                if not isinstance(match, dict):
                    raise TypeError(f"{tool_name} returned a non-object result row")
                missing = [
                    field for field in (global_field, name_field, registry_field)
                    if field not in match
                ]
                if missing:
                    raise ValueError(
                        f"{tool_name} returned an incomplete {entity} row; "
                        f"missing {missing}: {match!r}"
                    )
                self.add_entity(
                    etype,
                    match[name_field],
                    match[global_field],
                    registry_id=match[registry_field],
                )

        if tool_name in ("search_blocks", "search_system_registry") and "error" not in result:
            if "results" not in result or not isinstance(result["results"], list):
                raise ValueError(f"{tool_name} result must contain a results array")
            for block in result["results"]:
                if not isinstance(block, dict):
                    raise TypeError(f"{tool_name}.results contains a non-object block")
                self.ingest_block_metadata(block)

        # Sync to file-backed storage if available
        self._sync_catalog_to_file()

    def _sync_catalog_to_file(self) -> None:
        """Push any new catalog entries to the file-backed memory."""
        if self._mem_tools is None:
            return
        existing = self._mem_tools.memory_catalog_list()
        existing_rows = json.loads(existing) if isinstance(existing, str) else existing
        if not isinstance(existing_rows, list):
            raise TypeError("memory_catalog_list must return an array")
        existing_ids = set()
        for index, row in enumerate(existing_rows):
            if not isinstance(row, dict) or "global_id" not in row:
                raise ValueError(f"memory catalog row {index} has an invalid schema")
            existing_ids.add(row["global_id"])

        for etype, section in self._catalog.items():
            global_field = _global_id_field(etype)
            for name, info in section.items():
                if not isinstance(info, dict):
                    raise TypeError(f"in-process catalog entry {etype}/{name} must be an object")
                if global_field not in info or "registry_id" not in info:
                    raise ValueError(f"in-process catalog entry {etype}/{name} is incomplete")
                global_id = info[global_field]
                if global_id not in existing_ids:
                    self._mem_tools.memory_catalog_add(
                        etype, global_id, info["registry_id"], name
                    )

    # ── Serialisation ────────────────────────────────────────

    def render(self) -> str:
        """Render working memory.  Reads from file-backed storage if available."""
        if self._mem_tools is not None:
            return self._mem_tools.memory_read()
        return self.render_id_catalog()
