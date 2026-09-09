"""Database connection helpers for ThermoML search tools."""

import sqlite3
from os import fspath, path as os_path
from urllib.parse import quote


def _readonly_uri(path: str) -> str:
    absolute = os_path.abspath(fspath(path)).replace("\\", "/")
    if absolute.startswith("//"):
        return f"file://{quote(absolute, safe='/:')}?mode=ro&immutable=1"
    return f"file:{quote(absolute, safe='/:')}?mode=ro&immutable=1"


def open_db(path: str) -> sqlite3.Connection:
    """Return a read-only connection with Row factory."""
    conn = sqlite3.connect(_readonly_uri(path), uri=True)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA query_only=ON")
    return conn

def resolve_pcs_block_target(
    card: dict,
    block_number: object,
    BLKsubsys_id: object = None,
) -> tuple[dict, dict | None]:
    """Resolve one declared PCS block or exact search-eligible subsystem."""
    from ThermoML_raw_json_to_card_db_parsers.id_schema import (
        require_block_id,
        require_block_local_id,
    )

    block_id = require_block_id(block_number)
    subsystem_id = (
        require_block_local_id("subsys", BLKsubsys_id)
        if BLKsubsys_id is not None else None
    )
    matches = [
        item for item in card["blocks"]
        if isinstance(item, dict) and item.get("block_number") == block_id
    ]
    if len(matches) != 1:
        raise LookupError(
            f"PCS card has {len(matches)} matches for block {block_id}"
        )
    manifests = card["blocks_summary"]["derived_indexes"][
        "composition_subsystems"
    ]
    if block_id not in manifests or not isinstance(manifests[block_id], list):
        raise ValueError(
            f"PCS card has no composition-subsystem manifest for {block_id}"
        )
    if subsystem_id is None:
        return matches[0], None
    subsystem_matches = [
        item for item in manifests[block_id]
        if isinstance(item, dict) and item.get("BLKsubsys_id") == subsystem_id
    ]
    if len(subsystem_matches) != 1:
        raise LookupError(
            f"PCS card has {len(subsystem_matches)} matches for "
            f"{block_id}/{subsystem_id}"
        )
    subsystem = subsystem_matches[0]
    if subsystem.get("search_eligible") is not True:
        raise ValueError(f"{block_id}/{subsystem_id} is not search eligible")
    return matches[0], subsystem



def project_pcs_block_target(block: dict, subsystem: dict | None) -> dict:
    """Project active PCS declarations for one declared/subsystem target."""
    required = {"compounds", "variables", "properties", "constraints", "solvents"}
    missing = required - block.keys()
    if missing:
        raise ValueError(f"PCS block is missing projection fields: {sorted(missing)}")
    if subsystem is None:
        return {field: block[field] for field in required}

    retained_orgs = {
        item["org_num"] for item in subsystem["retained_components"]
    }
    supported_properties = {
        item["BLKprop_id"]
        for item in subsystem["property_support"]
        if item["role"] == "bulk_property"
        and item["phase_compatible"] is True
    }
    return {
        "compounds": [
            item for item in block["compounds"]
            if item["org_num"] in retained_orgs
        ],
        "variables": [
            item for item in block["variables"]
            if item.get("component_org_num") is None
            or item["component_org_num"] in retained_orgs
        ],
        "properties": [
            item for item in block["properties"]
            if item["BLKprop_id"] in supported_properties
        ],
        "constraints": [
            item for item in block["constraints"]
            if item.get("component_org_num") is None
            or item["component_org_num"] in retained_orgs
        ],
        "solvents": [
            item for item in block["solvents"]
            if item["component_org_num"] in retained_orgs
        ],
    }
