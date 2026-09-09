"""Compact strict object-based registry block rows into markdown."""

import json

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_block_id,
    require_global_id,
    validate_nested_identifiers,
)
from ThermoML_card_json_to_md_compactors.strict_contracts import require_payload

_REQUIRED_REGISTRY_FIELDS = {
    "doi", "block_number", "lit_id", "lit_num_id", "block_type",
    "blocktype_num_id", "n_datapoints", "system_type", "n_components",
    "comp_ids_smiles", "solvent_comp_ids_smiles", "constr_ids_values",
    "var_ids_ranges", "prop_ids_meas_ranges", "prop_phase_ids",
    "reaction_type", "rxn_type_num_id", "participants", "notes",
}


def _parse_json_col(value):
    if not value:
        return []
    parsed = json.loads(value) if isinstance(value, str) else value
    if not isinstance(parsed, list) or any(not isinstance(item, dict) for item in parsed):
        raise ValueError("Strict registry JSON columns must be arrays of objects")
    validate_nested_identifiers(parsed, path="registry JSON column")
    return parsed


def _range_text(stats):
    if not isinstance(stats, dict):
        return ""
    lo, hi = stats.get("min"), stats.get("max")
    if lo is None and hi is None:
        return ""
    return f" [{lo}, {hi}]"


def _compact_common(row, label):
    block_id = require_block_id(row["block_number"])
    lines = [f"# {label} | {row['doi']} | {block_id}", ""]
    lines.append(
        f"**Literature:** {require_global_id('lit_num_id', row['lit_num_id'])} | "
        f"{row['lit_id']}"
    )
    lines.append(
        f"**Type:** {row['blocktype_num_id']} | {row['block_type']} | "
        f"{row['system_type']} | {row['n_components']} components | "
        f"{row['n_datapoints']} pts"
    )

    compounds = _parse_json_col(row["comp_ids_smiles"])
    if compounds:
        lines.append(
            "**Compounds:** " + "; ".join(
                f"{item['org_num']}→{require_global_id('comp_num_id', item['comp_num_id'])} "
                f"{item['name'] or ''}"
                for item in compounds
            )
        )
    solvents = _parse_json_col(row["solvent_comp_ids_smiles"])
    if solvents:
        lines.append(
            "**Solvents:** " + "; ".join(
                f"{item['component_org_num']}→{item['comp_num_id']} "
                f"({item['solvent_num_id']})"
                for item in solvents
            )
        )

    variables = _parse_json_col(row["var_ids_ranges"])
    if variables:
        lines.append("**Variables:** " + "; ".join(
            f"{item['BLKvar_id']}→{item['var_num_id']}:{item['var_id']}"
            f"{_range_text(item.get('range'))}" for item in variables
        ))
    constraints = _parse_json_col(row["constr_ids_values"])
    if constraints:
        lines.append("**Constraints:** " + "; ".join(
            f"{item['BLKconstr_id']}→{item['constr_num_id']}:{item['constr_id']}"
            f"={item.get('value')}" for item in constraints
        ))
    properties = _parse_json_col(row["prop_ids_meas_ranges"])
    if properties:
        lines.append("**Properties:**")
        for item in properties:
            lines.append(
                f"  - {item['BLKprop_id']}→{item['prop_num_id']}:{item['prop_ID']} | "
                f"{require_global_id('meas_num_id', item['meas_num_id'])}:"
                f"{item['meas_ID']}"
                f"{_range_text(item.get('range'))}"
            )
    phases = _parse_json_col(row["prop_phase_ids"])
    if phases:
        lines.append("**Phases:** " + "; ".join(
            f"{item['owner_id']}:{item['role']}→"
            f"{require_global_id('phase_num_id', item['phase_num_id'])}:{item['phase']}"
            for item in phases
        ))
    return lines


def compact_pm_registry(row: dict) -> str:
    row = require_payload(
        row, _REQUIRED_REGISTRY_FIELDS, context="PureOrMixtureData registry row"
    )
    lines = _compact_common(row, "REG-PM")
    if row.get("notes"):
        lines.append(f"**Notes:** {row['notes']}")
    return "\n".join(lines) + "\n"


def compact_rxn_registry(row: dict) -> str:
    row = require_payload(
        row, _REQUIRED_REGISTRY_FIELDS, context="ReactionData registry row"
    )
    lines = _compact_common(row, "REG-RXN")
    if row.get("reaction_type"):
        lines.append(
            f"**Reaction:** {require_global_id('rxn_type_num_id', row['rxn_type_num_id'])} | "
            f"{row['reaction_type']}"
        )
    participants = _parse_json_col(row["participants"])
    if participants:
        lines.append("**Participants:**")
        for item in participants:
            lines.append(
                f"  - {item['org_num']} | "
                f"{require_global_id('comp_num_id', item['comp_num_id'])} | "
                f"{require_global_id('phase_num_id', item['phase_num_id'])}:"
                f"{item['phase_id']} | stoich={item['stoichiometric_coef']}"
            )
    if row.get("notes"):
        lines.append(f"**Notes:** {row['notes']}")
    return "\n".join(lines) + "\n"
