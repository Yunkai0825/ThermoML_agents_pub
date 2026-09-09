"""Parsers for the strict, object-based block registry projections."""

import json

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_block_id,
    require_block_local_id,
    require_doi_comp_id,
    require_doi_comp_sample_id,
    require_global_id,
    require_property_assessment_id,
)


def parse_json_array_col(raw, *, field: str) -> list:
    """Parse one nullable registry JSON column as an exact array."""
    if raw is None:
        return []
    if not isinstance(raw, str) or not raw.strip():
        raise ValueError(f"registry field {field!r} must be JSON text or null")
    result = json.loads(raw)
    if not isinstance(result, list):
        raise TypeError(f"registry field {field!r} must decode to an array")
    return result


def _dict_entries(raw, *, field: str):
    result: list[dict] = []
    for index, entry in enumerate(parse_json_array_col(raw, field=field)):
        if not isinstance(entry, dict):
            raise TypeError(f"{field}[{index}] must be an object")
        result.append(dict(entry))
    return result


def parse_comp_ids_smiles(raw) -> list[dict]:
    result = _dict_entries(raw, field="comp_ids_smiles")
    required = {
        "org_num", "comp_num_id", "name", "formula", "inchi_key", "SMILES",
        "sample_num",
    }
    for index, entry in enumerate(result):
        missing = required - entry.keys()
        if missing:
            raise ValueError(f"comp_ids_smiles[{index}] is missing {sorted(missing)}")
        require_doi_comp_id(entry["org_num"])
        require_global_id("comp_num_id", entry["comp_num_id"])
        if entry["sample_num"] is not None:
            require_doi_comp_sample_id(
                entry["sample_num"], component_org_num=entry["org_num"]
            )
    return result


def parse_solvent_ids(raw) -> list[dict]:
    result = _dict_entries(raw, field="solvent_comp_ids_smiles")
    required = {"component_org_num", "comp_num_id", "solvent_num_id", "inchi_key"}
    for index, entry in enumerate(result):
        missing = required - entry.keys()
        if missing:
            raise ValueError(
                f"solvent_comp_ids_smiles[{index}] is missing {sorted(missing)}"
            )
        require_doi_comp_id(entry["component_org_num"])
        require_global_id("comp_num_id", entry["comp_num_id"])
        require_global_id("solvent_num_id", entry["solvent_num_id"])
    return result


def _validate_component_reference(entry: dict, context: str) -> None:
    if "component_org_num" not in entry:
        raise ValueError(f"{context} requires component_org_num")
    if entry["component_org_num"] is not None:
        require_doi_comp_id(entry["component_org_num"])


def _validate_phase(phase: object, context: str) -> None:
    if phase is None:
        return
    if not isinstance(phase, dict):
        raise TypeError(f"{context} must be an object or null")
    required = {"phase", "phase_num_id", "phase_id"}
    missing = required - phase.keys()
    if missing:
        raise ValueError(f"{context} is missing {sorted(missing)}")
    require_global_id("phase_num_id", phase["phase_num_id"])


def parse_var_ids_ranges(raw) -> list[dict]:
    result = _dict_entries(raw, field="var_ids_ranges")
    for index, entry in enumerate(result):
        required = {"BLKvar_id", "var_num_id", "var_id", "component_org_num", "phase"}
        missing = required - entry.keys()
        if missing:
            raise ValueError(f"var_ids_ranges[{index}] is missing {sorted(missing)}")
        require_block_local_id("var", entry["BLKvar_id"])
        require_global_id("var_num_id", entry["var_num_id"])
        _validate_component_reference(entry, f"var_ids_ranges[{index}]")
        _validate_phase(entry["phase"], f"var_ids_ranges[{index}].phase")
        if "range" not in entry or not isinstance(entry["range"], dict):
            raise ValueError("var_ids_ranges entries require a range object")
        stats = entry["range"]
        if "min" not in stats or "max" not in stats:
            raise ValueError("variable range requires min and max")
        if stats.get("BLKvar_id") != entry["BLKvar_id"]:
            raise ValueError("variable range BLKvar_id does not match its declaration")
        entry["range_min"] = stats["min"]
        entry["range_max"] = stats["max"]
    return result


def parse_prop_ids_meas_ranges(raw) -> list[dict]:
    result = _dict_entries(raw, field="prop_ids_meas_ranges")
    for index, entry in enumerate(result):
        required = {
            "BLKprop_id", "prop_num_id", "prop_ID", "component_org_num",
            "meas_num_id", "meas_ID", "uncertainty",
        }
        missing = required - entry.keys()
        if missing:
            raise ValueError(f"prop_ids_meas_ranges[{index}] is missing {sorted(missing)}")
        require_block_local_id("prop", entry["BLKprop_id"])
        require_global_id("prop_num_id", entry["prop_num_id"])
        if entry["meas_num_id"] is not None:
            require_global_id("meas_num_id", entry["meas_num_id"])
        _validate_component_reference(entry, f"prop_ids_meas_ranges[{index}]")
        uncertainty = entry["uncertainty"]
        if uncertainty is not None:
            if not isinstance(uncertainty, dict) or "assessment_num" not in uncertainty:
                raise ValueError(
                    f"prop_ids_meas_ranges[{index}].uncertainty requires assessment_num"
                )
            require_property_assessment_id(
                uncertainty["assessment_num"], BLKprop_id=entry["BLKprop_id"]
            )
        if "range" not in entry or not isinstance(entry["range"], dict):
            raise ValueError("prop_ids_meas_ranges entries require a range object")
        stats = entry["range"]
        if "min" not in stats or "max" not in stats:
            raise ValueError("property range requires min and max")
        if stats.get("BLKprop_id") != entry["BLKprop_id"]:
            raise ValueError("property range BLKprop_id does not match its declaration")
        entry["range_min"] = stats["min"]
        entry["range_max"] = stats["max"]
    return result


def parse_phase_ids(raw) -> list[dict]:
    result = _dict_entries(raw, field="prop_phase_ids")
    for index, entry in enumerate(result):
        required = {"owner_id", "role", "phase", "phase_num_id", "phase_id"}
        missing = required - entry.keys()
        if missing:
            raise ValueError(f"prop_phase_ids[{index}] is missing {sorted(missing)}")
        owner = entry["owner_id"]
        if not isinstance(owner, str) or not owner.startswith("BLK"):
            raise ValueError(f"prop_phase_ids[{index}].owner_id must be block-local")
        kind = owner[3:].split("_", 1)[0]
        require_block_local_id(kind, owner)
        require_global_id("phase_num_id", entry["phase_num_id"])
    return result


def parse_constr_ids_values(raw) -> list[dict]:
    result = _dict_entries(raw, field="constr_ids_values")
    for index, entry in enumerate(result):
        required = {
            "BLKconstr_id", "constr_num_id", "constr_id",
            "component_org_num", "phase",
        }
        missing = required - entry.keys()
        if missing:
            raise ValueError(f"constr_ids_values[{index}] is missing {sorted(missing)}")
        require_block_local_id("constr", entry["BLKconstr_id"])
        require_global_id("constr_num_id", entry["constr_num_id"])
        _validate_component_reference(entry, f"constr_ids_values[{index}]")
        _validate_phase(entry["phase"], f"constr_ids_values[{index}].phase")
    return result


def parse_participants(raw) -> list[dict]:
    result = _dict_entries(raw, field="participants")
    required = {
        "org_num", "comp_num_id", "phase_num_id", "phase_id", "sample_num",
        "stoichiometric_coef",
    }
    for index, entry in enumerate(result):
        missing = required - entry.keys()
        if missing:
            raise ValueError(f"participants[{index}] is missing {sorted(missing)}")
        require_doi_comp_id(entry["org_num"])
        require_global_id("comp_num_id", entry["comp_num_id"])
        require_global_id("phase_num_id", entry["phase_num_id"])
        if entry["sample_num"] is not None:
            require_doi_comp_sample_id(
                entry["sample_num"], component_org_num=entry["org_num"]
            )
    return result


def parse_reaction_type(name, rxn_type_num_id) -> dict:
    if not isinstance(name, str) or not name.strip():
        raise ValueError("reaction registry row requires reaction_type")
    return {
        "reaction_type": name,
        "rxn_type_num_id": require_global_id(
            "rxn_type_num_id", rxn_type_num_id
        ),
    }


def _format_common(row) -> dict:
    require_global_id("lit_num_id", row["lit_num_id"])
    require_global_id("blocktype_num_id", row["blocktype_num_id"])
    require_block_id(row["block_number"], block_type=row["block_type"])
    return {
        "doi": row["doi"],
        "block_number": row["block_number"],
        "lit_id": row["lit_id"],
        "lit_num_id": row["lit_num_id"],
        "block_type": row["block_type"],
        "blocktype_num_id": row["blocktype_num_id"],
        "BLKsubsys_id": None,
        "search_scope": "declared",
        "n_datapoints": row["n_datapoints"],
        "parent_n_datapoints": row["n_datapoints"],
        "system_type": row["system_type"],
        "declared_system_type": row["system_type"],
        "n_components": row["n_components"],
        "declared_n_components": row["n_components"],
        "compounds": parse_comp_ids_smiles(row["comp_ids_smiles"]),
        "solvents": parse_solvent_ids(row["solvent_comp_ids_smiles"]),
        "constraints": parse_constr_ids_values(row["constr_ids_values"]),
        "variables": parse_var_ids_ranges(row["var_ids_ranges"]),
        "properties": parse_prop_ids_meas_ranges(row["prop_ids_meas_ranges"]),
        "phases": parse_phase_ids(row["prop_phase_ids"]),
        "notes": row["notes"],
    }


def format_pm_row(row) -> dict:
    result = _format_common(row)
    result["declared_compounds"] = list(result["compounds"])
    return result


def _json_object(raw, *, field: str) -> dict:
    if not isinstance(raw, str) or not raw.strip():
        raise ValueError(f"registry field {field!r} must be non-empty JSON text")
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise TypeError(f"registry field {field!r} must decode to an object")
    return value


def format_pm_subsystem_row(connection, row, subsystem_row) -> dict:
    """Format one normalized, search-eligible composition subsystem target.

    The parent registry row supplies occurrence metadata.  Identity, arity,
    point membership, and supported properties come only from the normalized
    subsystem tables projected from the authoritative PCS manifest.
    """
    result = format_pm_row(row)
    subsystem_id = require_block_local_id(
        "subsys", subsystem_row["BLKsubsys_id"]
    )
    doi = row["doi"]
    block_number = row["block_number"]
    if subsystem_row["doi"] != doi or subsystem_row["block_number"] != block_number:
        raise ValueError("subsystem and parent registry identities disagree")
    if int(subsystem_row["search_eligible"]) != 1:
        raise ValueError("only search-eligible subsystem rows may be formatted")

    compound_rows = connection.execute(
        "SELECT component_role, org_num, comp_num_id, comp_name, inchi_key "
        "FROM block_subsystem_compounds WHERE doi=? AND block_number=? "
        "AND BLKsubsys_id=? ORDER BY component_role DESC, org_num",
        (doi, block_number, subsystem_id),
    ).fetchall()
    retained_rows = [entry for entry in compound_rows if entry["component_role"] == "retained"]
    if len(retained_rows) != int(subsystem_row["n_retained_components"]):
        raise ValueError("subsystem retained-component count is inconsistent")
    parent_by_org = {entry["org_num"]: entry for entry in result["compounds"]}
    retained_org_nums: set[str] = set()
    retained_compounds: list[dict] = []
    for entry in retained_rows:
        org_num = require_doi_comp_id(entry["org_num"])
        comp_num_id = require_global_id("comp_num_id", entry["comp_num_id"])
        parent = parent_by_org.get(org_num)
        if parent is None or parent["comp_num_id"] != comp_num_id:
            raise ValueError("subsystem component does not resolve to its parent block")
        retained_org_nums.add(org_num)
        retained_compounds.append(parent)

    property_rows = connection.execute(
        "SELECT BLKprop_id, prop_num_id, prop_ID, support_role, "
        "phase_compatible, component_org_num, solvent_component_org_nums_json "
        "FROM block_subsystem_properties WHERE doi=? AND block_number=? "
        "AND BLKsubsys_id=? ORDER BY BLKprop_id, support_role",
        (doi, block_number, subsystem_id),
    ).fetchall()
    supported_ids: set[str] = set()
    property_support: list[dict] = []
    for entry in property_rows:
        local_id = require_block_local_id("prop", entry["BLKprop_id"])
        require_global_id("prop_num_id", entry["prop_num_id"])
        support = {
            "BLKprop_id": local_id,
            "prop_num_id": entry["prop_num_id"],
            "prop_ID": entry["prop_ID"],
            "component_org_num": entry["component_org_num"],
            "role": entry["support_role"],
            "phase_compatible": bool(entry["phase_compatible"]),
            "solvent_component_org_nums": parse_json_array_col(
                entry["solvent_component_org_nums_json"],
                field="solvent_component_org_nums_json",
            ),
        }
        property_support.append(support)
        if support["role"] == "bulk_property" and support["phase_compatible"]:
            supported_ids.add(local_id)
    parent_properties = {entry["BLKprop_id"]: entry for entry in result["properties"]}
    missing_properties = supported_ids - parent_properties.keys()
    if missing_properties:
        raise ValueError(f"subsystem properties are absent from parent: {sorted(missing_properties)}")

    condition_ranges = parse_json_array_col(
        subsystem_row["condition_ranges_json"], field="condition_ranges_json"
    )
    condition_by_id = {}
    for entry in condition_ranges:
        if not isinstance(entry, dict):
            raise TypeError("condition_ranges_json entries must be objects")
        local_id = require_block_local_id("var", entry["BLKvar_id"])
        condition_by_id[local_id] = entry
    variables = []
    for parent_variable in result["variables"]:
        component_org_num = parent_variable.get("component_org_num")
        if component_org_num is not None and component_org_num not in retained_org_nums:
            continue
        variable = dict(parent_variable)
        condition = condition_by_id.get(variable["BLKvar_id"])
        if condition is not None:
            variable["range"] = {
                "BLKvar_id": variable["BLKvar_id"],
                "min": condition["min"],
                "max": condition["max"],
                "n": condition["n"],
            }
            variable["range_min"] = condition["min"]
            variable["range_max"] = condition["max"]
            variable["range_scope"] = "subsystem"
        else:
            variable["range_scope"] = "declared_parent"
        variables.append(variable)

    scope = _json_object(subsystem_row["scope_json"], field="scope_json")
    point_runs = parse_json_array_col(
        subsystem_row["point_runs_json"], field="point_runs_json"
    )
    point_arity_counts = _json_object(
        subsystem_row["point_arity_counts_json"], field="point_arity_counts_json"
    )
    quality_flags = parse_json_array_col(
        subsystem_row["quality_flags_json"], field="quality_flags_json"
    )
    subsystem = {
        "BLKsubsys_id": subsystem_id,
        "relationship": "composition_subset_of_declared_system",
        "effective_system_type": subsystem_row["effective_system_type"],
        "n_retained_components": int(subsystem_row["n_retained_components"]),
        "n_points": int(subsystem_row["n_points"]),
        "search_eligible": True,
        "path_class": subsystem_row["path_class"],
        "evidence_quality": subsystem_row["evidence_quality"],
        "scope": scope,
        "point_membership": {"runs": point_runs},
        "point_arity_counts": point_arity_counts,
        "retained_components": retained_compounds,
        "property_support": property_support,
        "condition_ranges": condition_ranges,
        "quality_flags": quality_flags,
    }
    properties = []
    for value in sorted(supported_ids):
        prop = dict(parent_properties[value])
        prop["range_scope"] = "declared_parent"
        properties.append(prop)
    constraints = [
        constraint for constraint in result["constraints"]
        if constraint.get("component_org_num") is None
        or constraint["component_org_num"] in retained_org_nums
    ]
    active_owner_ids = {
        *(entry["BLKprop_id"] for entry in properties),
        *(entry["BLKvar_id"] for entry in variables),
        *(entry["BLKconstr_id"] for entry in constraints),
    }
    result.update({
        "BLKsubsys_id": subsystem_id,
        "search_scope": "subsystem",
        "n_datapoints": subsystem["n_points"],
        "system_type": subsystem["effective_system_type"],
        "n_components": subsystem["n_retained_components"],
        "compounds": retained_compounds,
        "properties": properties,
        "solvents": [
            solvent for solvent in result["solvents"]
            if solvent["component_org_num"] in retained_org_nums
        ],
        "variables": variables,
        "constraints": constraints,
        "phases": [
            phase for phase in result["phases"]
            if phase["owner_id"] in active_owner_ids
        ],
        "subsystem": subsystem,
    })
    return result


def format_rxn_row(row) -> dict:
    result = _format_common(row)
    result["reaction_type"] = parse_reaction_type(
        row["reaction_type"], row["rxn_type_num_id"]
    )
    result["participants"] = parse_participants(row["participants"])
    return result


def build_prop_patterns(prop_num_id: str) -> list[str]:
    """Build an exact JSON-object LIKE pattern for a global property ID."""
    value = require_global_id("prop_num_id", prop_num_id)
    return [f'%"prop_num_id":"{value}"%']
