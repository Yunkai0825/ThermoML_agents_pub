"""Lossless block-registry projection from strict PCS cards.

The PCS card is the occurrence-preserving source for registry databases.  A
registry row stores one typed block and JSON arrays of objects; it never
reconstructs local IDs from global registry IDs.
"""

from __future__ import annotations

import json
import os
import sqlite3
import time

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_block_id,
    require_block_local_id,
    require_doi_comp_id,
    require_global_id,
)


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
PCS_DB = os.path.join(ROOT, "card_databases_storage", "Individual_cards_dbs", "PCS_INDIV.db")


CREATE_TABLE = """
PRAGMA foreign_keys=ON;

CREATE TABLE block_registry (
    doi                       TEXT NOT NULL,
    block_number              TEXT NOT NULL,
    lit_id                    TEXT,
    lit_num_id                TEXT NOT NULL,
    block_type                TEXT NOT NULL,
    blocktype_num_id          TEXT NOT NULL,
    n_datapoints              INTEGER NOT NULL,
    system_type               TEXT NOT NULL,
    n_components              INTEGER NOT NULL,
    comp_ids_smiles           TEXT NOT NULL,
    solvent_comp_ids_smiles   TEXT,
    constr_ids_values         TEXT,
    var_ids_ranges            TEXT,
    prop_ids_meas_ranges      TEXT NOT NULL,
    prop_phase_ids            TEXT,
    reaction_type             TEXT,
    rxn_type_num_id           TEXT,
    participants              TEXT,
    notes                     TEXT,
    PRIMARY KEY (doi, block_number)
);

CREATE INDEX idx_registry_lit_id ON block_registry(lit_id);
CREATE INDEX idx_registry_lit_num_id ON block_registry(lit_num_id);
CREATE INDEX idx_registry_system_type ON block_registry(system_type);
CREATE INDEX idx_registry_blocktype_num_id ON block_registry(blocktype_num_id);

CREATE TABLE block_subsystems (
    doi                       TEXT NOT NULL,
    block_number              TEXT NOT NULL,
    BLKsubsys_id              TEXT NOT NULL,
    effective_system_type     TEXT NOT NULL,
    n_retained_components     INTEGER NOT NULL,
    n_points                  INTEGER NOT NULL,
    search_eligible           INTEGER NOT NULL,
    path_class                TEXT NOT NULL,
    evidence_quality          TEXT NOT NULL,
    scope_json                TEXT NOT NULL,
    point_runs_json           TEXT NOT NULL,
    point_arity_counts_json   TEXT NOT NULL,
    condition_ranges_json     TEXT NOT NULL,
    quality_flags_json        TEXT NOT NULL,
    PRIMARY KEY (doi, block_number, BLKsubsys_id),
    FOREIGN KEY (doi, block_number)
        REFERENCES block_registry(doi, block_number)
);

CREATE TABLE block_subsystem_compounds (
    doi                       TEXT NOT NULL,
    block_number              TEXT NOT NULL,
    BLKsubsys_id              TEXT NOT NULL,
    component_role            TEXT NOT NULL,
    org_num                   TEXT NOT NULL,
    comp_num_id               TEXT NOT NULL,
    comp_name                 TEXT NOT NULL,
    inchi_key                 TEXT NOT NULL,
    PRIMARY KEY (
        doi, block_number, BLKsubsys_id, component_role, org_num
    ),
    FOREIGN KEY (doi, block_number, BLKsubsys_id)
        REFERENCES block_subsystems(doi, block_number, BLKsubsys_id)
);

CREATE TABLE block_subsystem_properties (
    doi                       TEXT NOT NULL,
    block_number              TEXT NOT NULL,
    BLKsubsys_id              TEXT NOT NULL,
    BLKprop_id                TEXT NOT NULL,
    prop_num_id               TEXT NOT NULL,
    prop_ID                   TEXT NOT NULL,
    component_org_num         TEXT,
    support_role              TEXT NOT NULL,
    phase_compatible          INTEGER NOT NULL,
    solvent_component_org_nums_json TEXT NOT NULL,
    PRIMARY KEY (
        doi, block_number, BLKsubsys_id, BLKprop_id, support_role
    ),
    FOREIGN KEY (doi, block_number, BLKsubsys_id)
        REFERENCES block_subsystems(doi, block_number, BLKsubsys_id)
);

CREATE INDEX idx_subsystem_type
    ON block_subsystems(effective_system_type, search_eligible);
CREATE INDEX idx_subsystem_points ON block_subsystems(n_points);
CREATE INDEX idx_subsystem_comp_num
    ON block_subsystem_compounds(comp_num_id, component_role);
CREATE INDEX idx_subsystem_prop_num
    ON block_subsystem_properties(prop_num_id, support_role, phase_compatible);

CREATE TABLE metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
"""


def _json(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")) if value else None


def _property_projection(block: dict) -> list[dict]:
    stats = block["data_summary"]["property_stats"]
    out = []
    for prop in block["properties"]:
        local_id = prop["BLKprop_id"]
        entry = {
            "BLKprop_id": local_id,
            "prop_num_id": prop["prop_num_id"],
            "prop_ID": prop["prop_ID"],
            "name": prop["name"],
            "group": prop["group"],
            "component_org_num": prop["component_org_num"],
            "meas_num_id": prop["meas_num_id"],
            "meas_ID": prop["meas_ID"],
            "method_standard": prop["method_standard"],
            "method_custom": prop["method_custom"],
            "range": stats[local_id],
            "uncertainty": prop["uncertainty"],
        }
        out.append(entry)
    return out


def _variable_projection(block: dict) -> list[dict]:
    ranges = block["data_summary"]["variable_ranges"]
    out = []
    for var in block["variables"]:
        local_id = var["BLKvar_id"]
        out.append({
            "BLKvar_id": local_id,
            "var_num_id": var["var_num_id"],
            "var_id": var["var_id"],
            "name": var["name"],
            "type": var["type"],
            "component_org_num": var["component_org_num"],
            "phase": var["phase"],
            "range": ranges[local_id],
        })
    return out


def _constraint_projection(block: dict) -> list[dict]:
    return [
        {
            "BLKconstr_id": item["BLKconstr_id"],
            "constr_num_id": item["constr_num_id"],
            "constr_id": item["constr_id"],
            "name": item["name"],
            "type": item["type"],
            "value": item["value"],
            "digits": item["digits"],
            "component_org_num": item["component_org_num"],
            "phase": item["phase"],
        }
        for item in block["constraints"]
    ]


def _compound_projection(block: dict) -> list[dict]:
    return [
        {
            "org_num": item["org_num"],
            "comp_num_id": item["comp_num_id"],
            "name": item["name"],
            "formula": item["formula"],
            "inchi_key": item["inchi_key"],
            "SMILES": item["SMILES"],
            "sample_num": item["sample_num"],
        }
        for item in block["compounds"]
    ]


def _phase_projection(block: dict) -> list[dict]:
    out = []
    for prop in block["properties"]:
        for field in ("property_phase", "ref_phase"):
            phase = prop[field]
            if phase:
                out.append({"owner_id": prop["BLKprop_id"], "role": field, **phase})
    for var in block["variables"]:
        if var["phase"]:
            out.append({"owner_id": var["BLKvar_id"], "role": "phase", **var["phase"]})
    for constr in block["constraints"]:
        if constr["phase"]:
            out.append({"owner_id": constr["BLKconstr_id"], "role": "phase", **constr["phase"]})
    return out


def project_block(card: dict, block: dict) -> tuple:
    require_block_id(block["block_number"], block_type=block["block_type"])
    reaction = block["reaction"]
    compounds = _compound_projection(block)
    return (
        card["key"]["doi"],
        block["block_number"],
        card["key"]["lit_id"],
        card["key"]["lit_num_id"],
        block["block_type"],
        block["blocktype_num_id"],
        int(block["data_summary"]["n_points"]),
        block["system_type"],
        len(compounds),
        _json(compounds),
        _json(block["solvents"]),
        _json(_constraint_projection(block)),
        _json(_variable_projection(block)),
        _json(_property_projection(block)),
        _json(_phase_projection(block)),
        reaction["reaction_type"] if reaction is not None else None,
        reaction["rxn_type_num_id"] if reaction is not None else None,
        _json(reaction["participants"]) if reaction is not None else None,
        None,
    )


INSERT_SQL = """
INSERT INTO block_registry (
    doi, block_number, lit_id, lit_num_id, block_type, blocktype_num_id,
    n_datapoints, system_type, n_components, comp_ids_smiles,
    solvent_comp_ids_smiles, constr_ids_values, var_ids_ranges,
    prop_ids_meas_ranges, prop_phase_ids, reaction_type, rxn_type_num_id,
    participants, notes
) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
"""


SUBSYSTEM_INSERT_SQL = """
INSERT INTO block_subsystems (
    doi, block_number, BLKsubsys_id, effective_system_type,
    n_retained_components, n_points, search_eligible, path_class,
    evidence_quality, scope_json, point_runs_json, point_arity_counts_json,
    condition_ranges_json, quality_flags_json
) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
"""

SUBSYSTEM_COMPOUND_INSERT_SQL = """
INSERT INTO block_subsystem_compounds (
    doi, block_number, BLKsubsys_id, component_role, org_num,
    comp_num_id, comp_name, inchi_key
) VALUES (?,?,?,?,?,?,?,?)
"""

SUBSYSTEM_PROPERTY_INSERT_SQL = """
INSERT INTO block_subsystem_properties (
    doi, block_number, BLKsubsys_id, BLKprop_id, prop_num_id, prop_ID,
    component_org_num, support_role, phase_compatible,
    solvent_component_org_nums_json
) VALUES (?,?,?,?,?,?,?,?,?,?)
"""


def project_subsystems(card: dict, block: dict) -> tuple[list[tuple], list[tuple], list[tuple]]:
    """Project only the authoritative PCS manifest; never reclassify here."""
    doi = card["key"]["doi"]
    block_number = require_block_id(
        block["block_number"], block_type=block["block_type"]
    )
    manifests = card["blocks_summary"]["derived_indexes"]["composition_subsystems"]
    if block_number not in manifests:
        raise ValueError(
            f"PCS composition_subsystems is missing {doi!r} {block_number!r}"
        )

    subsystem_rows = []
    compound_rows = []
    property_rows = []
    for subsystem in manifests[block_number]:
        subsystem_id = require_block_local_id("subsys", subsystem["BLKsubsys_id"])
        retained = subsystem["retained_components"]
        if len(retained) != int(subsystem["n_retained_components"]):
            raise ValueError(
                f"{doi!r} {block_number!r} {subsystem_id!r} retained count mismatch"
            )
        subsystem_rows.append((
            doi, block_number, subsystem_id, subsystem["effective_system_type"],
            int(subsystem["n_retained_components"]), int(subsystem["n_points"]),
            int(bool(subsystem["search_eligible"])), subsystem["path_class"],
            subsystem["evidence_quality"], _json(subsystem["scope"]),
            _json(subsystem["point_membership"]["runs"]),
            _json(subsystem["point_arity_counts"]),
            _json(subsystem["condition_ranges"]) or "[]",
            _json(subsystem["quality_flags"]) or "[]",
        ))
        for role, compounds in (
            ("retained", retained),
            ("excluded", subsystem["excluded_components"]),
        ):
            for compound in compounds:
                compound_rows.append((
                    doi, block_number, subsystem_id, role,
                    require_doi_comp_id(compound["org_num"]),
                    require_global_id("comp_num_id", compound["comp_num_id"]),
                    compound["name"], compound["inchi_key"],
                ))
        for prop in subsystem["property_support"]:
            property_rows.append((
                doi, block_number, subsystem_id,
                require_block_local_id("prop", prop["BLKprop_id"]),
                require_global_id("prop_num_id", prop["prop_num_id"]),
                prop["prop_ID"],
                require_doi_comp_id(prop["component_org_num"])
                if prop["component_org_num"] is not None else None,
                prop["role"], int(bool(prop["phase_compatible"])),
                _json(prop["solvent_component_org_nums"]) or "[]",
            ))
    return subsystem_rows, compound_rows, property_rows


def build_registry(*, block_type: str, output_db: str, pcs_db: str = PCS_DB) -> int:
    if not os.path.exists(pcs_db):
        raise FileNotFoundError(f"Strict PCS database not found: {pcs_db}")
    os.makedirs(os.path.dirname(output_db), exist_ok=True)
    staging = output_db + ".building"
    for suffix in ("", "-wal", "-shm"):
        path = staging + suffix
        if os.path.exists(path):
            os.remove(path)

    source = sqlite3.connect(f"file:{pcs_db}?mode=ro", uri=True)
    target = sqlite3.connect(staging)
    target.executescript(CREATE_TABLE)
    t0 = time.time()
    rows = []
    subsystem_rows = []
    subsystem_compound_rows = []
    subsystem_property_rows = []
    count = 0
    subsystem_count = 0

    def flush_rows():
        target.executemany(INSERT_SQL, rows)
        target.executemany(SUBSYSTEM_INSERT_SQL, subsystem_rows)
        target.executemany(
            SUBSYSTEM_COMPOUND_INSERT_SQL, subsystem_compound_rows
        )
        target.executemany(
            SUBSYSTEM_PROPERTY_INSERT_SQL, subsystem_property_rows
        )
        rows.clear()
        subsystem_rows.clear()
        subsystem_compound_rows.clear()
        subsystem_property_rows.clear()

    for (payload,) in source.execute("SELECT json_data FROM cards ORDER BY doi"):
        card = json.loads(payload)
        for block in card["blocks"]:
            if block["block_type"] != block_type:
                continue
            rows.append(project_block(card, block))
            projected = project_subsystems(card, block)
            subsystem_rows.extend(projected[0])
            subsystem_compound_rows.extend(projected[1])
            subsystem_property_rows.extend(projected[2])
            subsystem_count += len(projected[0])
            count += 1
            if len(rows) >= 5000:
                flush_rows()
    if rows:
        flush_rows()

    target.executemany(
        "INSERT INTO metadata(key,value) VALUES (?,?)",
        [
            ("id_schema", "prefixed-v2"),
            ("block_type", block_type),
            ("total_blocks", str(count)),
            ("total_subsystems", str(subsystem_count)),
            ("source_db", pcs_db),
            ("build_time_s", f"{time.time() - t0:.1f}"),
        ],
    )
    target.commit()
    fk_errors = target.execute("PRAGMA foreign_key_check").fetchall()
    if fk_errors:
        raise RuntimeError(f"Registry subsystem foreign-key errors: {fk_errors[:5]!r}")
    target.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    source.close()
    target.close()
    os.replace(staging, output_db)
    return count
