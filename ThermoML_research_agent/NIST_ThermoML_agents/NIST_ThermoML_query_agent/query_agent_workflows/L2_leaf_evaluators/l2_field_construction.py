"""Deterministic, field-isolated constructors for Query L2 return JSON.

Each L2 ID-alignment agent emits only a literature/block anchor, a short
description, and one or two identifier checksums.  Exactly one hidden tool is
available to each L2 field processor.  The tool validates those checksums
against the central PCS block and constructs all remaining chemistry context
from the authoritative PCS/CCS/MTDKS/RMS cards.
"""

from __future__ import annotations

import csv
import json
import sqlite3
from copy import deepcopy
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_block_id,
    require_block_local_id,
    require_doi_comp_id,
    require_global_id,
)

from ....general_db_query_engine.general_argo_engine_helpers import anchor
from ....general_db_query_engine.general_argo_engine_helpers.json_answer_guard import (
    guard_json_answer,
)
from ....general_db_query_engine.general_hooks_management_helpers.general_postans_eval_hooks import (
    _postans_eval_anchors_catalog as postans_anchor,
)
from ....general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import (
    AgentToolCatalog,
    ToolEntry,
)


_REPO_ROOT = Path(__file__).resolve().parents[4]
_CARD_DB_ROOT = _REPO_ROOT / "card_databases_storage" / "Individual_cards_dbs"
_CSV_ROOT = (
    _REPO_ROOT
    / "card_databases_storage"
    / "Canonicalized_ID_name_lists_csvs"
)

_STATUSES = frozenset({"success", "partial", "no_results"})

L2_COMP_CORE_FIELDS = frozenset(
    {
        "lit_num_id", "block_number", "BLKsubsys_id", "description",
        "comp_num_id", "org_num",
    }
)
L2_MEAS_CORE_FIELDS = frozenset(
    {
        "lit_num_id",
        "block_number",
        "BLKsubsys_id",
        "description",
        "meas_num_id",
        "BLKprop_id",
    }
)
L2_PROP_CORE_FIELDS = frozenset(
    {
        "lit_num_id",
        "block_number",
        "BLKsubsys_id",
        "description",
        "BLKprop_id",
        "prop_num_id",
    }
)
L2_REF_CORE_FIELDS = frozenset(
    {"lit_num_id", "block_number", "BLKsubsys_id", "description", "lit_id"}
)

L2_COMP_ENRICHED_FIELDS = frozenset(
    set(L2_COMP_CORE_FIELDS)
    | {
        "registry_id",
        "name",
        "formula",
        "cas",
        "purity",
        "purity_method",
        "source",
        "notes",
    }
)
L2_MEAS_ENRICHED_FIELDS = frozenset(
    set(L2_MEAS_CORE_FIELDS)
    | {
        "prop_num_id",
        "registry_id",
        "technique",
        "instrument",
        "calibration",
        "uncertainty_type",
        "uncertainty_coverage",
        "notes",
    }
)
L2_PROP_ENRICHED_FIELDS = frozenset(
    set(L2_PROP_CORE_FIELDS)
    | {
        "registry_id",
        "component_org_num",
        "group",
        "phase",
        "std_state",
        "definition",
        "notes",
    }
)
L2_REF_ENRICHED_FIELDS = frozenset(
    set(L2_REF_CORE_FIELDS)
    | {
        "doi",
        "title",
        "authors",
        "journal",
        "year",
        "n_blocks",
        "compounds_measured",
        "properties_measured",
        "notes",
    }
)


class L2FieldValidationError(ValueError):
    """An L2 core search anchor conflicts with its authoritative card."""


def _exact_object(
    value: object,
    fields: frozenset[str],
    context: str,
) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise TypeError(f"{context} must be an object")
    actual = set(value)
    if actual != set(fields):
        raise L2FieldValidationError(
            f"{context} fields must be exactly {sorted(fields)}; "
            f"missing={sorted(set(fields) - actual)}, "
            f"extra={sorted(actual - set(fields))}"
        )
    return value


def _optional_core_selector(
    value: object,
    fields: frozenset[str],
    context: str,
) -> dict[str, Any]:
    """Accept an agent-owned anchor with an optional explicit subsystem ID."""
    if not isinstance(value, dict):
        raise TypeError(f"{context} must be an object")
    required = set(fields) - {"BLKsubsys_id"}
    actual = set(value)
    missing = required - actual
    extra = actual - set(fields)
    if missing or extra:
        raise L2FieldValidationError(
            f"{context} fields must contain {sorted(required)} and may "
            "additionally contain BLKsubsys_id; "
            f"missing={sorted(missing)}, extra={sorted(extra)}"
        )
    normalized = dict(value)
    normalized.setdefault("BLKsubsys_id", None)
    return normalized


def _text(value: object, context: str, *, nonempty: bool = True) -> str:
    if not isinstance(value, str) or (nonempty and not value.strip()):
        qualifier = "non-empty " if nonempty else ""
        raise TypeError(f"{context} must be {qualifier}text")
    return value.strip()


@lru_cache(maxsize=8192)
def _load_card(database: str, key_field: str, key: str) -> dict[str, Any]:
    path = _CARD_DB_ROOT / database
    if not path.is_file():
        raise FileNotFoundError(f"required card database is missing: {path}")
    connection = sqlite3.connect(str(path))
    try:
        rows = connection.execute(
            f"SELECT json_data FROM cards WHERE {key_field} = ?",
            (key,),
        ).fetchall()
    finally:
        connection.close()
    if len(rows) != 1:
        raise L2FieldValidationError(
            f"{database}.{key_field}={key!r} resolved to {len(rows)} cards"
        )
    parsed = json.loads(rows[0][0])
    if not isinstance(parsed, dict):
        raise TypeError(f"{database}.{key_field}={key!r} is not a JSON object")
    return parsed


@lru_cache(maxsize=8192)
def _csv_row(filename: str, key_field: str, key: str) -> dict[str, str]:
    path = _CSV_ROOT / filename
    if not path.is_file():
        raise FileNotFoundError(f"required canonical registry is missing: {path}")
    matches: list[dict[str, str]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get(key_field) == key:
                matches.append(dict(row))
    if len(matches) != 1:
        raise L2FieldValidationError(
            f"{filename}.{key_field}={key!r} resolved to {len(matches)} rows"
        )
    return matches[0]


def _pcs_block(
    lit_num_id: object,
    block_number: object,
    BLKsubsys_id: object,
) -> tuple[dict, dict, dict | None]:
    lit = require_global_id("lit_num_id", lit_num_id)
    block_id = require_block_id(block_number)
    subsystem_id = (
        require_block_local_id("subsys", BLKsubsys_id)
        if BLKsubsys_id is not None else None
    )
    card = _load_card("PCS_INDIV.db", "lit_num_id", lit)
    blocks = [
        item
        for item in card.get("blocks", [])
        if isinstance(item, dict) and item.get("block_number") == block_id
    ]
    if len(blocks) != 1:
        raise L2FieldValidationError(
            f"({lit}, {block_id}) resolved to {len(blocks)} PCS blocks"
        )
    manifests = card["blocks_summary"]["derived_indexes"][
        "composition_subsystems"
    ]
    if block_id not in manifests or not isinstance(manifests[block_id], list):
        raise L2FieldValidationError(
            f"({lit}, {block_id}) has no authoritative composition-subsystem manifest"
        )
    if subsystem_id is None:
        return card, blocks[0], None
    subsystem_matches = [
        item for item in manifests[block_id]
        if isinstance(item, dict) and item.get("BLKsubsys_id") == subsystem_id
    ]
    if len(subsystem_matches) != 1:
        raise L2FieldValidationError(
            f"({lit}, {block_id}, {subsystem_id}) resolved to "
            f"{len(subsystem_matches)} subsystem manifests"
        )
    subsystem = subsystem_matches[0]
    if subsystem.get("search_eligible") is not True:
        raise L2FieldValidationError(
            f"({lit}, {block_id}, {subsystem_id}) is not search eligible"
        )
    return card, blocks[0], subsystem


def _require_subsystem_compound(
    subsystem: dict | None,
    comp_num_id: str,
    org_num: str,
    context: str,
) -> None:
    if subsystem is None:
        return
    matches = [
        item for item in subsystem["retained_components"]
        if item.get("comp_num_id") == comp_num_id and item.get("org_num") == org_num
    ]
    if len(matches) != 1:
        subsystem_id = subsystem["BLKsubsys_id"]
        raise L2FieldValidationError(
            f"{context} compound is not retained by {subsystem_id}"
        )


def _require_subsystem_property(
    subsystem: dict | None,
    BLKprop_id: str,
    context: str,
) -> None:
    if subsystem is None:
        return
    matches = [
        item for item in subsystem["property_support"]
        if item.get("BLKprop_id") == BLKprop_id
        and item.get("role") == "bulk_property"
        and item.get("phase_compatible") is True
    ]
    if len(matches) != 1:
        subsystem_id = subsystem["BLKsubsys_id"]
        raise L2FieldValidationError(
            f"{context} property is not a bulk, phase-compatible property of "
            f"{subsystem_id}"
        )


def _unique_match(
    values: object,
    predicate: Callable[[dict], bool],
    context: str,
) -> dict:
    if not isinstance(values, list):
        raise TypeError(f"{context} collection must be an array")
    matches = [item for item in values if isinstance(item, dict) and predicate(item)]
    if len(matches) != 1:
        raise L2FieldValidationError(
            f"{context} checksum resolved to {len(matches)} entries"
        )
    return matches[0]


def _join_text(values: object, *, limit: int = 4) -> str:
    if not isinstance(values, list):
        return ""
    result: list[str] = []
    for value in values:
        if isinstance(value, str) and value.strip() and value.strip() not in result:
            result.append(value.strip())
    return "; ".join(result[:limit])


def _compound_purity(sample: dict) -> tuple[float | int | None, str]:
    values: list[float | int] = []
    methods: list[str] = []
    for step in sample.get("purity_steps", []) or []:
        if not isinstance(step, dict):
            continue
        purity = step.get("purity") or {}
        if isinstance(purity, dict):
            for field in ("mass_fraction", "mol_fraction", "vol_fraction"):
                value = purity.get(field)
                if isinstance(value, (int, float)) and not isinstance(value, bool):
                    values.append(value)
                    break
        for method_field in ("analysis_methods", "purification_methods"):
            method_values = step.get(method_field)
            if isinstance(method_values, list):
                methods.extend(
                    item.strip()
                    for item in method_values
                    if isinstance(item, str) and item.strip()
                )
    return (values[0] if values else None, _join_text(methods))


def construct_l2_compounds(core_compounds: object) -> dict[str, list[dict]]:
    """Construct compound details from compound + block checksum IDs."""
    if not isinstance(core_compounds, list):
        raise TypeError("compounds must be an array")
    enriched: list[dict] = []
    seen: set[tuple[str, str, str | None, str]] = set()
    for index, value in enumerate(core_compounds):
        context = f"compounds[{index}]"
        core = _optional_core_selector(value, L2_COMP_CORE_FIELDS, context)
        lit = require_global_id("lit_num_id", core["lit_num_id"])
        block_id = require_block_id(core["block_number"])
        subsystem_id = core["BLKsubsys_id"]
        comp_id = require_global_id("comp_num_id", core["comp_num_id"])
        org_num = require_doi_comp_id(core["org_num"])
        description = _text(core["description"], f"{context}.description")
        identity = (lit, block_id, subsystem_id, org_num)
        if identity in seen:
            raise L2FieldValidationError(f"duplicate compound anchor {identity!r}")
        seen.add(identity)

        _, block, subsystem = _pcs_block(lit, block_id, subsystem_id)
        _require_subsystem_compound(subsystem, comp_id, org_num, context)
        block_comp = _unique_match(
            block.get("compounds"),
            lambda row: (
                row.get("comp_num_id") == comp_id and row.get("org_num") == org_num
            ),
            f"{context} PCS compound",
        )
        ccs = _load_card("CCS_INDIV.db", "lit_num_id", lit)
        doi_comp = _unique_match(
            ccs.get("compounds"),
            lambda row: (
                row.get("comp_num_id") == comp_id and row.get("org_num") == org_num
            ),
            f"{context} CCS compound",
        )
        sample_num = block_comp.get("sample_num")
        samples = doi_comp.get("samples") or []
        sample = _unique_match(
            samples,
            lambda row: row.get("sample_num") == sample_num,
            f"{context} CCS sample",
        )
        dk = _load_card("CCS_ID_DK.db", "comp_num_id", comp_id)
        registry = _csv_row("compound_ids.csv", "comp_num_id", comp_id)
        purity, purity_method = _compound_purity(sample)
        enriched.append(
            {
                "lit_num_id": lit,
                "block_number": block_id,
                "BLKsubsys_id": subsystem_id,
                "description": description,
                "comp_num_id": comp_id,
                "org_num": org_num,
                "registry_id": registry["comp_id"],
                "name": dk.get("names", {}).get("primary_name")
                or block_comp.get("name")
                or "",
                "formula": dk.get("identity", {}).get("formula")
                or block_comp.get("formula")
                or "",
                "cas": "",
                "purity": purity,
                "purity_method": purity_method,
                "source": sample.get("source") or "",
                "notes": sample.get("status") or "",
            }
        )
    return {"compounds": enriched}


def _measurement_dk_fields(dk: dict) -> tuple[str, str]:
    structured = dk.get("domain_knowledge", {}).get("structured_block", {})
    setup = structured.get("setup_and_requirements", {})
    if not isinstance(setup, dict):
        return "", ""
    return (
        _join_text(setup.get("instrument_components")),
        _join_text(setup.get("calibration_requirements")),
    )


def construct_l2_measurements(
    core_measurements: object,
) -> dict[str, list[dict]]:
    """Construct measurement details from method + block-property checksums."""
    if not isinstance(core_measurements, list):
        raise TypeError("measurements must be an array")
    enriched: list[dict] = []
    seen: set[tuple[str, str, str | None, str]] = set()
    for index, value in enumerate(core_measurements):
        context = f"measurements[{index}]"
        core = _optional_core_selector(value, L2_MEAS_CORE_FIELDS, context)
        lit = require_global_id("lit_num_id", core["lit_num_id"])
        block_id = require_block_id(core["block_number"])
        subsystem_id = core["BLKsubsys_id"]
        meas_id = require_global_id("meas_num_id", core["meas_num_id"])
        blk_prop_id = require_block_local_id("prop", core["BLKprop_id"])
        description = _text(core["description"], f"{context}.description")
        identity = (lit, block_id, subsystem_id, blk_prop_id)
        if identity in seen:
            raise L2FieldValidationError(f"duplicate measurement anchor {identity!r}")
        seen.add(identity)

        _, block, subsystem = _pcs_block(lit, block_id, subsystem_id)
        _require_subsystem_property(subsystem, blk_prop_id, context)
        prop = _unique_match(
            block.get("properties"),
            lambda row: row.get("BLKprop_id") == blk_prop_id,
            f"{context} PCS property",
        )
        if prop.get("meas_num_id") != meas_id:
            raise L2FieldValidationError(
                f"{context}.meas_num_id expected {prop.get('meas_num_id')!r}, "
                f"received {meas_id!r}"
            )
        prop_num_id = require_global_id("prop_num_id", prop["prop_num_id"])
        mtdks = _load_card("MTDKS_INDIV.db", "lit_num_id", lit)
        method = _unique_match(
            mtdks.get("methods"),
            lambda row: (
                row.get("meas_num_id") == meas_id
                and block_id in (row.get("block_numbers") or [])
            ),
            f"{context} MTDKS method",
        )
        dk = _load_card("MTDKS_ID_DK.db", "meas_num_id", meas_id)
        instrument, calibration = _measurement_dk_fields(dk)
        uncertainty = prop.get("uncertainty") or {}
        confidence = (
            uncertainty.get("confidence_level")
            if isinstance(uncertainty, dict)
            else None
        )
        if isinstance(confidence, (int, float)) and confidence > 1:
            confidence = confidence / 100
        if isinstance(confidence, bool) or not isinstance(
            confidence, (int, float, type(None))
        ):
            confidence = None
        enriched.append(
            {
                "lit_num_id": lit,
                "block_number": block_id,
                "BLKsubsys_id": subsystem_id,
                "description": description,
                "meas_num_id": meas_id,
                "BLKprop_id": blk_prop_id,
                "prop_num_id": prop_num_id,
                "registry_id": method.get("meas_id")
                or dk.get("meas_ID")
                or prop.get("meas_ID")
                or "",
                "technique": method.get("method_name")
                or dk.get("identity", {}).get("name")
                or "",
                "instrument": instrument,
                "calibration": calibration,
                "uncertainty_type": uncertainty.get("evaluation_method", "")
                if isinstance(uncertainty, dict)
                else "",
                "uncertainty_coverage": confidence,
                "notes": (
                    f"method_type={method.get('method_type', '')}; "
                    f"property={prop.get('name', '')}"
                ).strip("; "),
            }
        )
    return {"measurements": enriched}


def _first_definition(dk: dict) -> str:
    structured = dk.get("domain_knowledge", {}).get("structured_block", {})
    definition = structured.get("definition", {})
    if isinstance(definition, dict):
        for key in (
            "physical_quantity",
            "mathematical_definition",
            "thermodynamic_definition",
        ):
            value = definition.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
    description = dk.get("domain_knowledge", {}).get("description_block", {})
    if isinstance(description, dict):
        for key in ("property_overview", "physical_meaning", "thermodynamic_context"):
            value = description.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
    identity = dk.get("identity", {})
    name = identity.get("name", "") if isinstance(identity, dict) else ""
    unit = identity.get("unit", "") if isinstance(identity, dict) else ""
    return f"{name} [{unit}]" if name and unit else str(name or "")


def _standard_state(prop: dict) -> str:
    fields = {
        key: prop.get(key)
        for key in (
            "standard_state",
            "ref_state_type",
            "ref_temperature_K",
            "ref_pressure_kPa",
            "temperature_K",
            "pressure_kPa",
            "ref_phase",
        )
        if prop.get(key) is not None
    }
    return json.dumps(fields, sort_keys=True, ensure_ascii=False) if fields else ""


def construct_l2_properties(core_properties: object) -> dict[str, list[dict]]:
    """Construct property details from block-property + global checksums."""
    if not isinstance(core_properties, list):
        raise TypeError("properties must be an array")
    enriched: list[dict] = []
    seen: set[tuple[str, str, str | None, str]] = set()
    for index, value in enumerate(core_properties):
        context = f"properties[{index}]"
        core = _optional_core_selector(value, L2_PROP_CORE_FIELDS, context)
        lit = require_global_id("lit_num_id", core["lit_num_id"])
        block_id = require_block_id(core["block_number"])
        subsystem_id = core["BLKsubsys_id"]
        blk_prop_id = require_block_local_id("prop", core["BLKprop_id"])
        prop_num_id = require_global_id("prop_num_id", core["prop_num_id"])
        description = _text(core["description"], f"{context}.description")
        identity = (lit, block_id, subsystem_id, blk_prop_id)
        if identity in seen:
            raise L2FieldValidationError(f"duplicate property anchor {identity!r}")
        seen.add(identity)

        _, block, subsystem = _pcs_block(lit, block_id, subsystem_id)
        _require_subsystem_property(subsystem, blk_prop_id, context)
        prop = _unique_match(
            block.get("properties"),
            lambda row: row.get("BLKprop_id") == blk_prop_id,
            f"{context} PCS property",
        )
        if prop.get("prop_num_id") != prop_num_id:
            raise L2FieldValidationError(
                f"{context}.prop_num_id expected {prop.get('prop_num_id')!r}, "
                f"received {prop_num_id!r}"
            )
        dk = _load_card("PCS_ID_DK.db", "prop_num_id", prop_num_id)
        phase = prop.get("property_phase") or {}
        component_org_num = prop.get("component_org_num")
        if component_org_num is not None:
            require_doi_comp_id(component_org_num)
        enriched.append(
            {
                "lit_num_id": lit,
                "block_number": block_id,
                "BLKsubsys_id": subsystem_id,
                "description": description,
                "BLKprop_id": blk_prop_id,
                "prop_num_id": prop_num_id,
                "registry_id": prop.get("prop_ID") or dk.get("prop_ID") or "",
                "component_org_num": component_org_num,
                "group": prop.get("group")
                or dk.get("identity", {}).get("property_group")
                or "",
                "phase": phase.get("phase_id") or phase.get("phase") or "",
                "std_state": _standard_state(prop),
                "definition": _first_definition(dk),
                "notes": (
                    f"presentation={prop.get('presentation') or ''}; "
                    f"measurement={prop.get('meas_ID') or ''}"
                ).strip("; "),
            }
        )
    return {"properties": enriched}


def construct_l2_reference(core_reference: object) -> dict[str, dict]:
    """Construct reference details from one literature + block checksum."""
    core = _optional_core_selector(
        core_reference, L2_REF_CORE_FIELDS, "reference"
    )
    lit = require_global_id("lit_num_id", core["lit_num_id"])
    block_id = require_block_id(core["block_number"])
    subsystem_id = core["BLKsubsys_id"]
    lit_id = _text(core["lit_id"], "reference.lit_id")
    description = _text(core["description"], "reference.description")
    _pcs_block(lit, block_id, subsystem_id)
    rms = _load_card("RMS_INDIV.db", "lit_num_id", lit)
    identity = rms.get("identity") or {}
    if identity.get("lit_id") != lit_id:
        raise L2FieldValidationError(
            f"reference.lit_id expected {identity.get('lit_id')!r}, "
            f"received {lit_id!r}"
        )
    bibliographic = rms.get("bibliographic") or {}
    inventory = rms.get("data_inventory") or {}
    compound_names = [
        item.get("name", "")
        for item in inventory.get("compound_list", [])
        if isinstance(item, dict) and item.get("name")
    ]
    property_names = [
        item.get("name", "")
        for item in inventory.get("properties", [])
        if isinstance(item, dict) and item.get("name")
    ]
    notes = "; ".join(
        f"{key}={bibliographic[key]}"
        for key in ("publication_type", "source_type")
        if bibliographic.get(key)
    )
    return {
        "reference": {
            "lit_num_id": lit,
            "block_number": block_id,
            "BLKsubsys_id": subsystem_id,
            "description": description,
            "lit_id": lit_id,
            "doi": identity.get("doi") or "",
            "title": bibliographic.get("title") or "",
            "authors": bibliographic.get("authors") or [],
            "journal": bibliographic.get("journal") or "",
            "year": bibliographic.get("year"),
            "n_blocks": inventory.get("n_blocks", 0),
            "compounds_measured": compound_names,
            "properties_measured": property_names,
            "notes": notes,
        }
    }


class L2CompoundConstructionToolCatalog(AgentToolCatalog):
    pipeline_label = "postanswer-l2-compound"

    def __init__(self) -> None:
        super().__init__(
            entries=(
                ToolEntry(
                    "construct_l2_compounds",
                    construct_l2_compounds,
                    group="l2_compound_construction",
                    skip_compactor=True,
                    skip_subagent=True,
                ),
            )
        )


class L2MeasurementConstructionToolCatalog(AgentToolCatalog):
    pipeline_label = "postanswer-l2-measurement"

    def __init__(self) -> None:
        super().__init__(
            entries=(
                ToolEntry(
                    "construct_l2_measurements",
                    construct_l2_measurements,
                    group="l2_measurement_construction",
                    skip_compactor=True,
                    skip_subagent=True,
                ),
            )
        )


class L2PropertyConstructionToolCatalog(AgentToolCatalog):
    pipeline_label = "postanswer-l2-property"

    def __init__(self) -> None:
        super().__init__(
            entries=(
                ToolEntry(
                    "construct_l2_properties",
                    construct_l2_properties,
                    group="l2_property_construction",
                    skip_compactor=True,
                    skip_subagent=True,
                ),
            )
        )


class L2ReferenceConstructionToolCatalog(AgentToolCatalog):
    pipeline_label = "postanswer-l2-reference"

    def __init__(self) -> None:
        super().__init__(
            entries=(
                ToolEntry(
                    "construct_l2_reference",
                    construct_l2_reference,
                    group="l2_reference_construction",
                    skip_compactor=True,
                    skip_subagent=True,
                ),
            )
        )


L2_COMPOUND_CONSTRUCTION_TOOLS = L2CompoundConstructionToolCatalog()
L2_MEASUREMENT_CONSTRUCTION_TOOLS = L2MeasurementConstructionToolCatalog()
L2_PROPERTY_CONSTRUCTION_TOOLS = L2PropertyConstructionToolCatalog()
L2_REFERENCE_CONSTRUCTION_TOOLS = L2ReferenceConstructionToolCatalog()

_FIELD_CONFIG = {
    "comp": (
        "compounds",
        L2_COMP_CORE_FIELDS,
        L2_COMPOUND_CONSTRUCTION_TOOLS,
        "construct_l2_compounds",
    ),
    "meas": (
        "measurements",
        L2_MEAS_CORE_FIELDS,
        L2_MEASUREMENT_CONSTRUCTION_TOOLS,
        "construct_l2_measurements",
    ),
    "prop": (
        "properties",
        L2_PROP_CORE_FIELDS,
        L2_PROPERTY_CONSTRUCTION_TOOLS,
        "construct_l2_properties",
    ),
    "ref": (
        "reference",
        L2_REF_CORE_FIELDS,
        L2_REFERENCE_CONSTRUCTION_TOOLS,
        "construct_l2_reference",
    ),
}

_CORRECTION_SYSTEM_TEMPLATE = """
You are correcting the minimal {kind} search anchors for a ThermoML L2
post-answer stage. Return exactly the requested JSON object.

The hidden {kind} constructor reported a checksum mismatch. Use the
observation and completed run record to correct only `status` and `{field}`.
Each {field} entry may contain only the declared literature/block anchor,
brief description, and validation IDs. Never emit chemistry enrichment,
registry names, DOI, bibliographic fields, purity, apparatus, calibration,
uncertainty, definition, or notes; deterministic code owns those fields.
Omit BLKsubsys_id for a declared parent-block anchor. Include it only as the
exact recorded BLKsubsys_N value when the evidence explicitly selects that
embedded subsystem. Never emit a null BLKsubsys_id in the minimal payload.
Do not emit answer, core_claims, or summary. Remove an entry if the completed
record does not support a valid correction. Never invent an ID.

Output exactly one JSON object. No prose, tags, or code fences.
""".strip()


def _validate_core_field(kind: str, value: object) -> object:
    field, fields, _, _ = _FIELD_CONFIG[kind]
    if kind == "ref":
        return _optional_core_selector(value, fields, field)
    if not isinstance(value, list):
        raise TypeError(f"{field} must be an array")
    normalized = []
    for index, item in enumerate(value):
        normalized.append(
            _optional_core_selector(item, fields, f"{field}[{index}]")
        )
    return normalized


def _validate_minimal_alignment(kind: str, payload: object) -> dict[str, Any]:
    field = _FIELD_CONFIG[kind][0]
    result = dict(_exact_object(
        payload,
        frozenset({"status", "summary", field}),
        f"L2 {kind} ID alignment",
    ))
    if result["status"] not in _STATUSES:
        raise L2FieldValidationError(
            f"status must be one of {sorted(_STATUSES)}"
        )
    _text(result["summary"], "summary", nonempty=False)
    result[field] = _validate_core_field(kind, result[field])
    return result


def _construct_l2_field(
    kind: str,
    core_value: object,
    *,
    engine_hooks: Any = None,
) -> object:
    field, _, catalog, tool_name = _FIELD_CONFIG[kind]
    if set(catalog.tools) != {tool_name}:
        raise AssertionError(
            f"L2 {kind} constructor catalog must expose only {tool_name}"
        )
    anchor(
        postans_anchor.POSTANS_L2_FIELD_TOOL_BEFORE,
        engine_hooks,
        kind=kind,
        field=field,
        tool_name=tool_name,
        core_value=core_value,
    )
    result = catalog.tools[tool_name](core_value)
    anchor(
        postans_anchor.POSTANS_L2_FIELD_TOOL_AFTER,
        engine_hooks,
        kind=kind,
        field=field,
        tool_name=tool_name,
        result=result,
    )
    if not isinstance(result, dict) or set(result) != {field}:
        raise TypeError(f"{tool_name} returned an invalid envelope")
    return result[field]


def _refine_and_enrich_l2_field(
    kind: str,
    *,
    id_alignment: dict[str, Any],
    client: Any,
    id_alignment_schema: dict[str, Any],
    id_alignment_prompt: str,
    completed_run_record: str,
    label: str,
    max_tokens: int,
    engine_hooks: Any = None,
    max_cycles: int = 2,
    **_: Any,
) -> dict[str, Any]:
    field = _FIELD_CONFIG[kind][0]
    current = _validate_minimal_alignment(kind, deepcopy(id_alignment))
    summary = current["summary"]
    correction_schema = {
        "status": id_alignment_schema["status"],
        field: id_alignment_schema[field],
    }
    last_error: Exception | None = None
    for cycle in range(1, max_cycles + 1):
        try:
            enriched = _construct_l2_field(
                kind,
                current[field],
                engine_hooks=engine_hooks,
            )
            return {
                "status": current["status"],
                field: enriched,
                "summary": summary,
            }
        except (L2FieldValidationError, TypeError, ValueError) as exc:
            last_error = exc
            if cycle == max_cycles:
                break
            anchor(
                postans_anchor.POSTANS_L2_FIELD_REFINEMENT,
                engine_hooks,
                label=label,
                kind=kind,
                cycle=cycle,
                observation=str(exc),
            )
            prompt = (
                id_alignment_prompt
                + "\n\n## Completed run record\n"
                + completed_run_record
                + "\n\n## Constructor validation observation\n"
                + str(exc)
                + "\n\n## Current minimal field selection\n"
                + json.dumps(
                    {"status": current["status"], field: current[field]},
                    indent=2,
                    ensure_ascii=False,
                )
            )
            raw = client.call(
                prompt,
                _CORRECTION_SYSTEM_TEMPLATE.format(kind=kind, field=field),
                max_tokens=max_tokens,
            )
            parsed, _ = guard_json_answer(
                raw,
                client=client,
                label=f"{label}-l2-{kind}-field-refinement-{cycle}",
                schema=correction_schema,
                max_retries=1,
                max_tokens=max_tokens,
            )
            if not isinstance(parsed, dict) or set(parsed) != set(correction_schema):
                raise L2FieldValidationError(
                    f"L2 {kind} refinement returned invalid JSON"
                )
            current = _validate_minimal_alignment(
                kind,
                {**parsed, "summary": summary},
            )
    raise L2FieldValidationError(
        f"{label} L2 {kind} field refinement exhausted {max_cycles} cycles: "
        f"{last_error}"
    )


def refine_and_enrich_l2_compounds(**kwargs: Any) -> dict[str, Any]:
    return _refine_and_enrich_l2_field("comp", **kwargs)


def refine_and_enrich_l2_measurements(**kwargs: Any) -> dict[str, Any]:
    return _refine_and_enrich_l2_field("meas", **kwargs)


def refine_and_enrich_l2_properties(**kwargs: Any) -> dict[str, Any]:
    return _refine_and_enrich_l2_field("prop", **kwargs)


def refine_and_enrich_l2_reference(**kwargs: Any) -> dict[str, Any]:
    return _refine_and_enrich_l2_field("ref", **kwargs)


L2_ID_ALIGNMENT_PROCESSORS = {
    "comp": refine_and_enrich_l2_compounds,
    "meas": refine_and_enrich_l2_measurements,
    "prop": refine_and_enrich_l2_properties,
    "ref": refine_and_enrich_l2_reference,
}


__all__ = [
    "L2_COMP_CORE_FIELDS",
    "L2_MEAS_CORE_FIELDS",
    "L2_PROP_CORE_FIELDS",
    "L2_REF_CORE_FIELDS",
    "L2_COMP_ENRICHED_FIELDS",
    "L2_MEAS_ENRICHED_FIELDS",
    "L2_PROP_ENRICHED_FIELDS",
    "L2_REF_ENRICHED_FIELDS",
    "L2FieldValidationError",
    "construct_l2_compounds",
    "construct_l2_measurements",
    "construct_l2_properties",
    "construct_l2_reference",
    "L2CompoundConstructionToolCatalog",
    "L2MeasurementConstructionToolCatalog",
    "L2PropertyConstructionToolCatalog",
    "L2ReferenceConstructionToolCatalog",
    "L2_ID_ALIGNMENT_PROCESSORS",
]
