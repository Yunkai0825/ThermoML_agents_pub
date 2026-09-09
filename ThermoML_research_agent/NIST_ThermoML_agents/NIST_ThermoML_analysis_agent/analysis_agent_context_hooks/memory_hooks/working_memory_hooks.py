"""
Working memory for the ThermoML Analysis Agent.
================================================
Inherits the shared ID Catalog from ``BaseWorkingMemory`` and adds
session-scoped persistence, auto-extraction of compound IDs from
structured tool results (inspect_block, get_pure_values, fit_block),
and query/fit tracking.

Compound names come from **canonical block metadata** (the CSVs),
not from regex-parsing of LLM-generated text.

When a session is active, state is synced to ``_working_memory.md``
inside the session directory after every state change.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from ....general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers import session_manager_output_storage
from ....general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers.general_memory_hooks import (
    BaseWorkingMemory,
    extract_entities_from_block_metadata,
    normalize_name,
)
from ....general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers.envelope_memory_digest import (
    digest_with_validation,
)
from ....NIST_ThermoML_query_agent.query_agent_workflows.strict_output_contracts import (
    validate_l1_query_output,
)
from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    GLOBAL_PREFIX_BY_FIELD,
    require_block_id,
    require_block_local_id,
    require_global_id,
    validate_nested_identifiers,
)

if TYPE_CHECKING:
    from pathlib import Path

log = logging.getLogger("ANALYSIS-WM")
_CORE_GLOBAL_FIELD_BY_TYPE = {
    "lit": "lit_num_id", "comp": "comp_num_id", "prop": "prop_num_id",
    "var": "var_num_id", "constr": "constr_num_id", "meas": "meas_num_id",
    "phase": "phase_num_id", "blocktype": "blocktype_num_id",
    "rxntype": "rxn_type_num_id", "solvent": "solvent_num_id",
}


def _require_nonempty_doi(value: object, *, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise TypeError(f"{context}.doi must be a non-empty string")
    return value


_UNSET = object()


def _property_response_snapshot(trace: object) -> dict | None:
    """Bound materialization provenance before it enters working memory."""
    if not isinstance(trace, dict):
        return None
    snapshot = {
        key: trace.get(key)
        for key in (
            "status", "BLKprop_id", "prop_num_id", "presentation_kind",
            "equation", "reported_unit", "absolute_unit", "standard_state",
        )
    }
    sources = trace.get("reference_sources")
    if isinstance(sources, list):
        snapshot["reference_source_count"] = len(sources)
        snapshot["reference_sources"] = [
            {
                key: source.get(key)
                for key in (
                    "lit_num_id", "doi", "block_number", "BLKprop_id",
                    "comp_num_id", "phase_num_id",
                )
            }
            for source in sources[:8]
            if isinstance(source, dict)
        ]
    return snapshot


def _fit_snapshot(
    fit: dict,
    *,
    doi: object | None = None,
    lit_num_id: object | None = None,
    block_number: object | None = None,
    BLKsubsys_id: object = _UNSET,
    components: object | None = None,
    label: str | None = None,
) -> dict:
    """Create one exact successful-fit memory record without default values."""
    if not isinstance(fit, dict):
        raise TypeError("successful fit result must be an object")
    required_metrics = {
        "rk_coeffs", "rk_order", "r_squared", "rmse", "n_mixture_points"
    }
    missing = required_metrics - fit.keys()
    if missing:
        raise ValueError(
            f"successful fit result missing required fields: {sorted(missing)}"
        )
    resolved_doi = _require_nonempty_doi(
        fit["doi"] if doi is None else doi,
        context="fit result",
    )
    resolved_block = require_block_id(
        fit["block_number"] if block_number is None else block_number
    )
    resolved_lit_num_id = require_global_id(
        "lit_num_id",
        fit["lit_num_id"] if lit_num_id is None else lit_num_id,
    )
    subsystem_value = (
        fit["BLKsubsys_id"] if BLKsubsys_id is _UNSET else BLKsubsys_id
    )
    resolved_subsystem = (
        require_block_local_id("subsys", subsystem_value)
        if subsystem_value is not None else None
    )
    resolved_components = fit["components"] if components is None else components
    if not isinstance(resolved_components, list) or any(
        not isinstance(item, str) or not item for item in resolved_components
    ):
        raise TypeError("fit result components must be an array of non-empty strings")
    coeffs = fit["rk_coeffs"]
    if not isinstance(coeffs, list) or any(
        isinstance(item, bool) or not isinstance(item, (int, float))
        for item in coeffs
    ):
        raise TypeError("fit result rk_coeffs must be an array of numbers")

    snapshot = {
        "doi": resolved_doi,
        "lit_num_id": resolved_lit_num_id,
        "block_number": resolved_block,
        "BLKsubsys_id": resolved_subsystem,
        "components": resolved_components,
        "rk_coeffs": coeffs,
        "rk_order": fit["rk_order"],
        "r_squared": fit["r_squared"],
        "rmse": fit["rmse"],
        "n_mixture_points": fit["n_mixture_points"],
    }
    if label is not None:
        snapshot["label"] = label
    optional_fields = (
        "mixing_rule", "sweep_value", "selected_temperature_K",
        "output_files", "pure_values", "pure_values_source",
        "pure_values_note", "route", "transform", "composition_conversion",
    )
    for field in optional_fields:
        if field in fit:
            snapshot[field] = fit[field]
    response_snapshot = _property_response_snapshot(fit.get("property_response"))
    if response_snapshot is not None:
        snapshot["property_response"] = response_snapshot
    return snapshot

# Entity extraction from block metadata is shared via
# extract_entities_from_block_metadata in general_memory_hooks.


def _format_l1_block(data: dict, key: str) -> tuple[str, str]:
    """Compact digest of a parsed L1 JSON result for working memory.

    Returns ``(digest_markdown, validation_verdict)``: single-source
    envelope render (memory-surface ledger level for the ``Ai/L1`` pair)
    with a deterministic grounding-validation section.
    """
    validate_l1_query_output(data)
    return digest_with_validation(
        data, key=key, tool_name="query_thermoml", pair="Ai/L1")


class AnalysisWorkingMemory(BaseWorkingMemory):
    """Analysis agent working memory with session persistence."""

    def __init__(self):
        super().__init__()
        self.query_results: list[dict] = []        # [{tool, summary, blocks}, ...]
        self.inspected_blocks: list[dict] = []     # [{doi, block_number, ...}, ...]
        self.property_response_declarations: list[dict] = []
        self.fit_results: list[dict] = []          # [{label, rk_coeffs, r2, ...}, ...]
        self.property_response_events: list[dict] = []
        self.composition_library: dict | None = None   # align_compositions
        self.history: list[str] = []               # append-only action log

    # ── History helpers ──────────────────────────────────────

    def append_history(self, line: str) -> None:
        """Append a one-line entry to the in-memory history log."""
        self.history.append(line)
        self.sync_to_disk()

    # ── Auto-extract from tool results ───────────────────────
    def record_tool_result(self, tool_name: str, result: dict):
        """Automatically extract and store key information from tool results.

        Compound names are taken from **structured metadata dicts**
        (canonical names from the database CSVs), never regex-parsed
        from LLM text.
        """
        if not isinstance(result, dict):
            raise TypeError(f"{tool_name} result must be an object")
        validate_nested_identifiers(result, path=f"memory_result[{tool_name}]")

        if tool_name in ("query_thermoml", "query_thermoml_parallel"):
            if tool_name == "query_thermoml":
                query_items = [{"label": "query", "result": result}]
            else:
                if set(result) != {"n_queries", "results"}:
                    raise ValueError(
                        "query_thermoml_parallel requires exactly n_queries and results"
                    )
                if not isinstance(result["results"], list):
                    raise TypeError("query_thermoml_parallel.results must be an array")
                query_items = result["results"]
            for index, item in enumerate(query_items):
                if not isinstance(item, dict):
                    raise TypeError(f"parallel result {index} must be an object")
                if "error" in item:
                    if not {"label", "error"} <= set(item) <= {"label", "error", "salvage"}:
                        raise ValueError(
                            f"parallel error result {index} has unknown fields"
                        )
                    err_entry = {
                        "tool": tool_name,
                        "label": item["label"],
                        "error": item["error"],
                    }
                    if isinstance(item.get("salvage"), dict):
                        err_entry["salvage"] = item["salvage"]
                    self.query_results.append(err_entry)
                    continue
                if set(item) != {"label", "result"}:
                    raise ValueError(
                        f"parallel result {index} requires exactly label and result"
                    )
                data = item["result"]
                if not isinstance(data, dict):
                    raise TypeError(f"parallel result {index}.result must be an object")
                text, validation_verdict = _format_l1_block(
                    data, f"L1_query_{len(self.query_results) + 1}",
                )
                blocks = [
                    {
                        "doi": block["doi"],
                        "lit_num_id": block["lit_num_id"],
                        "block_number": block["block_number"],
                        "BLKsubsys_id": block["BLKsubsys_id"],
                    }
                    for block in data["core_blocks_found"]
                ]
                self.query_results.append({
                    "tool": tool_name,
                    "label": item["label"],
                    "summary": text,
                    "blocks": blocks,
                    "validation": validation_verdict,
                })
                for upd in data["core_id_updates"]:
                    if not isinstance(upd, dict):
                        raise TypeError("core_id_updates entries must be objects")
                    expected = {"action", "core_GLOB_id", "registry_id", "name"}
                    if set(upd) != expected:
                        raise ValueError(
                            "core_id_updates entry must contain exactly "
                            f"{sorted(expected)}"
                        )
                    if upd["action"] != "add":
                        raise ValueError(
                            f"Invalid core_id_updates action: {upd['action']!r}"
                        )
                    global_id = upd["core_GLOB_id"]
                    matches = [
                        (entity_type, field)
                        for entity_type, field in _CORE_GLOBAL_FIELD_BY_TYPE.items()
                        if isinstance(global_id, str)
                        and global_id.startswith(GLOBAL_PREFIX_BY_FIELD[field])
                    ]
                    if len(matches) != 1:
                        raise ValueError(
                            f"core_GLOB_id has no unique type: {global_id!r}"
                        )
                    entity_type, global_field = matches[0]
                    require_global_id(global_field, global_id)
                    self.add_entity(
                        entity_type,
                        upd["name"],
                        global_id=global_id,
                        registry_id=upd["registry_id"],
                    )

        elif tool_name == "inspect_block" and "error" not in result:
            required = {
                "doi", "lit_num_id", "block_number", "BLKsubsys_id", "block_type",
                "compounds", "compound_map",
                "variables", "properties", "constraints", "solvents", "columns",
                "n_rows", "identified_x", "identified_y", "column_compound_map",
                "column_ranges", "property_response_contracts",
            }
            if set(result) != required:
                raise ValueError(
                    f"inspect_block schema mismatch: missing={sorted(required - set(result))}, "
                    f"unknown={sorted(set(result) - required)}"
                )
            require_global_id("lit_num_id", result["lit_num_id"])
            self.inspected_blocks.append({
                "doi": result["doi"],
                "lit_num_id": result["lit_num_id"],
                "block_number": result["block_number"],
                "BLKsubsys_id": result["BLKsubsys_id"],
                "compounds": result["compounds"],
                "n_rows": result["n_rows"],
                "identified_x": result["identified_x"],
                "identified_y": result["identified_y"],
            })
            self.property_response_declarations.append({
                "doi": result["doi"],
                "lit_num_id": result["lit_num_id"],
                "block_number": result["block_number"],
                "BLKsubsys_id": result["BLKsubsys_id"],
                "properties": [
                    {
                        key: prop.get(key)
                        for key in (
                            "BLKprop_id", "prop_num_id", "presentation",
                            "standard_state", "ref_state_type",
                            "ref_temperature_K", "ref_pressure_kPa",
                            "property_phase", "ref_phase", "meas_num_id",
                        )
                    }
                    for prop in result["properties"]
                    if isinstance(prop, dict)
                ],
                "contracts": [
                    {
                        key: contract.get(key)
                        for key in (
                            "BLKprop_id", "prop_num_id", "quantity_key",
                            "column_name", "reported_presentation",
                            "presentation_kind", "reported_unit", "absolute_unit",
                            "requires_reference_materialization",
                            "requires_normalized_composition", "ref_state_type",
                            "ref_temperature_K", "ref_pressure_kPa",
                            "property_phase", "ref_phase", "component_org_num",
                            "supported",
                        )
                    }
                    for contract in result["property_response_contracts"]
                    if isinstance(contract, dict)
                ],
            })
            # Populate ID catalog from structured block metadata
            # Registers compounds, variables, properties, constraints
            self.ingest_block_metadata(result)

        elif tool_name == "get_pure_values" and "error" not in result:
            # Pure values keyed by canonical compound name from metadata
            required = {"doi", "lit_num_id", "block_number", "BLKsubsys_id", "pure_values"}
            missing = required - result.keys()
            if missing:
                raise ValueError(
                    f"get_pure_values result missing required fields: {sorted(missing)}"
                )
            _require_nonempty_doi(result["doi"], context="get_pure_values result")
            require_global_id("lit_num_id", result["lit_num_id"])
            require_block_id(result["block_number"])
            if result["BLKsubsys_id"] is not None:
                require_block_local_id("subsys", result["BLKsubsys_id"])
            if not isinstance(result["pure_values"], dict):
                raise TypeError("get_pure_values.pure_values must be an object")
            for comp, val in result["pure_values"].items():
                if self.find_compound_by_name(comp):
                    self.merge_compound(comp, pure_values=val)
                else:
                    log.info(
                        "Pure value for unresolved compound %r was not added to the ID catalog",
                        comp,
                    )
            response_snapshot = _property_response_snapshot(
                result.get("property_response")
            )
            if response_snapshot is not None:
                self.property_response_events.append({
                    "doi": result["doi"],
                    "lit_num_id": result["lit_num_id"],
                    "block_number": result["block_number"],
                    "BLKsubsys_id": result["BLKsubsys_id"],
                    **response_snapshot,
                })

        elif tool_name == "align_compositions" and "error" not in result:
            required = {
                "system", "state", "alignment_status", "molar_masses_g_mol",
                "basis_counts", "n_blocks_surveyed", "bridges",
                "bridge_candidates", "chosen_bridge_reason",
            }
            missing = required - result.keys()
            if missing:
                raise ValueError(
                    f"align_compositions result missing required fields: {sorted(missing)}"
                )
            bridges = result["bridges"]
            if not isinstance(bridges, dict):
                raise TypeError("align_compositions.bridges must be an object")
            br = bridges["mass_density"] if "mass_density" in bridges else None
            if br is not None:
                bridge_required = {
                    "doi", "block_number", "BLKsubsys_id", "temperature_K", "r_squared", "estimated"
                }
                bridge_missing = bridge_required - br.keys()
                if bridge_missing:
                    raise ValueError(
                        "align_compositions density bridge missing fields: "
                        f"{sorted(bridge_missing)}"
                    )
                if not isinstance(br["estimated"], bool):
                    raise TypeError("density bridge estimated must be boolean")
                if not br["estimated"]:
                    _require_nonempty_doi(br["doi"], context="density bridge")
                    require_block_id(br["block_number"])
                    if br["BLKsubsys_id"] is not None:
                        require_block_local_id("subsys", br["BLKsubsys_id"])
            tt = result["translation_table"] if "translation_table" in result else None
            self.composition_library = {
                "system": result["system"],
                "state": result["state"],
                "alignment_status": result["alignment_status"],
                "molar_masses_g_mol": result["molar_masses_g_mol"],
                "basis_counts": result["basis_counts"],
                "n_blocks_surveyed": result["n_blocks_surveyed"],
                "n_bridge_candidates": len(result["bridge_candidates"]),
                "chosen_bridge_reason": result["chosen_bridge_reason"],
                "bridge": {
                    "doi": br["doi"], "block_number": br["block_number"],
                    "BLKsubsys_id": br["BLKsubsys_id"],
                    "temperature_K": br["temperature_K"],
                    "r_squared": br["r_squared"],
                    "estimated": br["estimated"],
                } if br is not None else None,
                "translation_table_file": tt["file"] if tt is not None else None,
                "library_file": result["library_file"] if "library_file" in result else None,
            }

        elif tool_name in ("fit_block", "fit_block_derived") and "error" not in result:
            # Dispatch exact successful output variants without fabricating absent fields.
            if "per_sweep_value" in result:
                for per_v in result["per_sweep_value"]:
                    if "error" not in per_v:
                        self.fit_results.append(
                            _fit_snapshot(
                                per_v,
                                doi=result["doi"],
                                lit_num_id=result["lit_num_id"],
                                block_number=result["block_number"],
                                BLKsubsys_id=result["BLKsubsys_id"],
                                components=result["components"],
                            )
                        )
            elif "n_properties" in result and "results" in result:
                if not isinstance(result["results"], dict):
                    raise TypeError("multi-property fit results must be an object")
                for label, fit in result["results"].items():
                    if not isinstance(fit, dict):
                        raise TypeError(f"multi-property fit {label!r} must be an object")
                    if "error" not in fit:
                        self.fit_results.append(_fit_snapshot(fit, label=label))
            elif "mixing_rule" in result and result["mixing_rule"] == "both":
                for field, label in (
                    ("fit_linear", "linear baseline"),
                    ("fit_arrhenius", "arrhenius baseline"),
                ):
                    fit = result[field]
                    if "error" not in fit:
                        fit_with_count = {
                            **fit,
                            "n_mixture_points": result["n_mixture_points"],
                            "property_response": result.get("property_response"),
                        }
                        self.fit_results.append(
                            _fit_snapshot(
                                fit_with_count,
                                doi=result["doi"],
                                lit_num_id=result["lit_num_id"],
                                block_number=result["block_number"],
                                BLKsubsys_id=result["BLKsubsys_id"],
                                components=result["components"],
                                label=label,
                            )
                        )
            else:
                self.fit_results.append(_fit_snapshot(result))
            # Pure anchors are references too — keep them on the compound
            # entities so later iterations can reuse them without refetching
            pv = result["pure_values"] if "pure_values" in result else {}
            for comp, val in pv.items():
                if not self.find_compound_by_name(comp):
                    log.info(
                        "Fit pure value for unresolved compound %r was not added to the ID catalog",
                        comp,
                    )
                    continue
                if isinstance(val, bool) or not isinstance(val, (int, float)):
                    raise TypeError(f"pure value for {comp!r} must be numeric")
                self.merge_compound(comp, pure_values=float(val))

        elif tool_name == "fit_multi_system" and "results" in result:
            if set(result) != {"n_systems", "results", "errors"}:
                raise ValueError(
                    "fit_multi_system result requires exactly n_systems, results, errors"
                )
            if not isinstance(result["results"], list):
                raise TypeError("fit_multi_system.results must be an array")
            for index, item in enumerate(result["results"]):
                if not isinstance(item, dict) or set(item) != {"label", "fit"}:
                    raise ValueError(
                        f"fit_multi_system.results[{index}] requires exactly label and fit"
                    )
                fit = item["fit"]
                if not isinstance(fit, dict):
                    raise TypeError(f"fit_multi_system.results[{index}].fit must be an object")
                if "error" not in fit:
                    self.fit_results.append(
                        _fit_snapshot(fit, label=item["label"])
                    )

        # ── Append a one-line history entry ──
        err = result["error"] if "error" in result else None
        tag = f" ERROR: {str(err)[:80]}" if err else ""
        self.history.append(f"[{tool_name}]{tag}")

        self.sync_to_disk()

    # ── Disk persistence ─────────────────────────────────────
    def sync_to_disk(self):
        """Persist working memory to _working_memory.md in the session dir."""
        sess = session_manager_output_storage.get_session()
        if not sess:
            return
        content = self.render()
        if not content:
            return
        wm_path = sess.session_dir / "_working_memory.md"
        session_manager_output_storage._filesystem_path(wm_path).write_text(
            f"# Working Memory\n\n{content}\n", encoding="utf-8",
        )

    # ── Render for LLM context injection ─────────────────────
    def render(self) -> str:
        """Render working memory as a text block for the LLM."""
        parts = []

        sess = session_manager_output_storage.get_session()
        root = str(sess.session_dir) if sess else None
        if root:
            parts.append(f"**ROOT:** `{root}`")

        # ── ID Catalog (from base class) ──
        catalog = self.render_id_catalog()
        if catalog:
            parts.append(catalog)

        # ── History ──
        if self.history:
            lines = "\n".join(f"- {h}" for h in self.history)
            parts.append(f"### History\n{lines}")

        # ── Query Results (full text preserved) ──
        if self.query_results:
            qr_lines = []
            for i, q in enumerate(self.query_results):
                label = q.get("label", f"Q{i+1}")
                if "error" in q:
                    block = f"#### {label} — ERROR\n{q['error']}"
                    salvage = q.get("salvage")
                    if isinstance(salvage, dict):
                        parts_s = []
                        ids = salvage.get("searched_ids") or {}
                        for etype, gids in ids.items():
                            if gids:
                                parts_s.append(f"- {etype}: {', '.join(gids)}")
                        blocks = salvage.get("doi_blocks") or []
                        if blocks:
                            refs = "; ".join(
                                f"{b['doi']} · {b['block_number']}" for b in blocks[:30]
                            )
                            parts_s.append(f"- doi/blocks: {refs}")
                        raw = (salvage.get("raw_answer") or "").strip()
                        if raw:
                            parts_s.append(f"- raw answer (unrefined):\n{raw}")
                        if parts_s:
                            block += (
                                "\n**Salvaged from completed search — usable to "
                                "refine follow-up queries (unvalidated):**\n"
                                + "\n".join(parts_s)
                            )
                    qr_lines.append(block)
                else:
                    qr_lines.append(f"#### {label}\n{q['summary']}")
            parts.append("### Query Results\n" + "\n\n".join(qr_lines))

        if self.inspected_blocks:
            lines = []
            for block in self.inspected_blocks[-20:]:
                target = (
                    f"{block['lit_num_id']} | {block['doi']} | "
                    f"{block['block_number']}"
                )
                if block["BLKsubsys_id"] is not None:
                    target += f" @ {block['BLKsubsys_id']}"
                lines.append(
                    f"- {target}: {block['n_rows']} rows; "
                    f"x={block['identified_x']}; y={block['identified_y']}"
                )
                declarations = next(
                    (
                        item["properties"]
                        for item in reversed(self.property_response_declarations)
                        if item["doi"] == block["doi"]
                        and item["block_number"] == block["block_number"]
                        and item["BLKsubsys_id"] == block["BLKsubsys_id"]
                    ),
                    [],
                )
                for prop in declarations:
                    lines.append(
                        f"    - {prop.get('BLKprop_id')} / {prop.get('prop_num_id')}: "
                        f"presentation={prop.get('presentation')}; "
                        f"reference={prop.get('ref_state_type')}; "
                        f"standard_state={prop.get('standard_state')}"
                    )
                contracts = next(
                    (
                        item["contracts"]
                        for item in reversed(self.property_response_declarations)
                        if item["doi"] == block["doi"]
                        and item["block_number"] == block["block_number"]
                        and item["BLKsubsys_id"] == block["BLKsubsys_id"]
                    ),
                    [],
                )
                for contract in contracts:
                    lines.append(
                        f"      response gate {contract.get('BLKprop_id')} / "
                        f"{contract.get('prop_num_id')}: "
                        f"kind={contract.get('presentation_kind')}; "
                        f"materialize_reference="
                        f"{contract.get('requires_reference_materialization')}; "
                        f"supported={contract.get('supported')}; "
                        f"units={contract.get('reported_unit') or 'dimensionless'}"
                        f" -> {contract.get('absolute_unit') or 'dimensionless'}"
                    )
            parts.append("### Inspected Blocks\n" + "\n".join(lines))

        if self.composition_library:
            cl = self.composition_library
            bases = ", ".join(f"{k}×{v}" for k, v in
                              (cl.get("basis_counts") or {}).items())
            cl_lines = [
                f"  system: {' + '.join(cl.get('system', []))} | "
                f"state: {cl.get('state')} | blocks: {cl.get('n_blocks_surveyed')}"
                f" | status: {cl.get('alignment_status', '?')}",
                f"  bases: {bases or 'n/a'} | M: "
                + "; ".join(f"{k}={v:g}" for k, v in
                            (cl.get("molar_masses_g_mol") or {}).items()),
            ]
            if cl.get("bridge"):
                b = cl["bridge"]
                est = " ⚠ ESTIMATED" if b.get("estimated") else ""
                subsystem = (" @ " + b["BLKsubsys_id"]
                             if b.get("BLKsubsys_id") is not None else "")
                cl_lines.append(
                    f"  density bridge: {b['doi'] if b['doi'] is not None else 'estimate'} "
                    f"{b['block_number'] if b['block_number'] is not None else ''}{subsystem} "
                    f"(T={b['temperature_K']}, R²={b['r_squared']}){est} — "
                    f"answers density/molar-volume questions directly"
                )
                if cl.get("chosen_bridge_reason"):
                    cl_lines.append(
                        f"  chosen because: {cl['chosen_bridge_reason']}"
                        + (f" (of {cl.get('n_bridge_candidates')} candidates)"
                           if cl.get("n_bridge_candidates") else "")
                    )
            if cl.get("translation_table_file"):
                fpath = cl["translation_table_file"]
                if root and str(fpath).startswith(root):
                    fpath = "$ROOT/" + str(fpath)[len(root):].lstrip("\\/")
                cl_lines.append(f"  composition data sheet: {fpath}")
            parts.append("### Composition Library\n" + "\n".join(cl_lines))

        if self.fit_results:
            lines = []
            for f in self.fit_results:
                target = f"{f['doi']}/{f['block_number']}"
                if f["BLKsubsys_id"] is not None:
                    target += f" @ {f['BLKsubsys_id']}"
                label = (
                    f"{f['label']} [{target}]"
                    if "label" in f else target
                )
                comps = f.get("components", [])
                r2 = f.get("r_squared")
                rmse = f.get("rmse")
                order = f.get("rk_order")
                coeffs = f.get("rk_coeffs", [])
                T = f.get("temperature_K")
                t_tag = f" T={T}K" if T is not None else ""
                lines.append(
                    f"  - {label} ({', '.join(comps)}){t_tag}: "
                    f"RK order={order}, R²={r2}, RMSE={rmse}, "
                    f"coeffs={[round(c, 6) for c in coeffs]}"
                )
                response = f.get("property_response")
                if response:
                    lines.append(
                        "      response: "
                        f"{response.get('presentation_kind')} via "
                        f"{response.get('equation')} | "
                        f"{response.get('reference_source_count', 0)} reference source(s) | "
                        f"{response.get('reported_unit')} -> {response.get('absolute_unit')}"
                    )
                if f.get("route") and "derived" in str(f.get("route")):
                    lines.append(f"      route: {f['route']}"
                                 + (f" via {f['transform']}" if f.get("transform") else ""))
                if f.get("composition_conversion"):
                    lines.append(f"      ⚠ {f['composition_conversion']}")
                pv = f.get("pure_values") or {}
                if pv:
                    pv_txt = ", ".join(f"{k}={v:.6g}" for k, v in pv.items())
                    src = f.get("pure_values_source", "")
                    src_tag = f" [{src}]" if src else ""
                    lines.append(f"      pure refs: {pv_txt}{src_tag}")
                    if f.get("pure_values_note"):
                        lines.append(f"      ⚠ {f['pure_values_note']}")
                ofs = f.get("output_files", {})
                for ftype, fpath in ofs.items():
                    if root and str(fpath).startswith(root):
                        fpath = "$ROOT/" + str(fpath)[len(root):].lstrip("\\/")
                    lines.append(f"      {ftype}: {fpath}")
            parts.append("### Completed Fits\n" + "\n".join(lines))

        if self.property_response_events:
            lines = []
            for event in self.property_response_events[-20:]:
                lines.append(
                    f"- {event['lit_num_id']} | {event['doi']} | "
                    f"{event['block_number']}: {event.get('presentation_kind')} via "
                    f"{event.get('equation')} ({event.get('reference_source_count', 0)} "
                    "reference source(s))"
                )
            parts.append("### Property Response Preparation\n" + "\n".join(lines))

        if sess and sess.list_files():
            parts.append(sess.render_manifest(root_dir=root))

        return "\n\n".join(parts) if parts else ""
