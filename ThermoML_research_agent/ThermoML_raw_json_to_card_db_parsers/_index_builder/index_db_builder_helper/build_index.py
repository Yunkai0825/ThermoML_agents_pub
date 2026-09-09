#!/usr/bin/env python3
"""Build the strict, occurrence-preserving ThermoML search index.

The index is projected directly from prefixed PCS cards and canonical CSVs.
It never reconstructs DOI-local occurrences from global registry IDs.
"""

from __future__ import annotations

import csv
import json
import os
import sqlite3
import sys
import time

_QUERY_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
if _QUERY_ROOT not in sys.path:
    sys.path.insert(0, _QUERY_ROOT)

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_block_id,
    require_block_local_id,
    require_doi_comp_id,
    require_global_id,
)
from ThermoML_raw_json_to_card_db_parsers._index_builder.registry_db_generation_helper.registry_projection import (
    SUBSYSTEM_COMPOUND_INSERT_SQL,
    SUBSYSTEM_INSERT_SQL,
    SUBSYSTEM_PROPERTY_INSERT_SQL,
    project_subsystems,
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUERY_ROOT = _QUERY_ROOT
CSV_DIR = os.path.join(
    QUERY_ROOT, "ThermoML_raw_json_to_card_db_parsers", "_index_builder", "id_name_lists"
)
CARD_DB_DIR = os.path.join(QUERY_ROOT, "card_databases_storage")
PCS_DB = os.path.join(CARD_DB_DIR, "Individual_cards_dbs", "PCS_INDIV.db")
DB_PATH = os.path.join(CARD_DB_DIR, "ThermoML_index.db")


SCHEMA = """
PRAGMA foreign_keys=ON;
PRAGMA foreign_keys=ON;

CREATE TABLE ref_index (
    doi                 TEXT PRIMARY KEY,
    lit_id              TEXT,
    lit_num_id          TEXT NOT NULL UNIQUE,
    title               TEXT,
    year                INTEGER,
    journal             TEXT,
    first_author        TEXT,
    n_compounds         INTEGER,
    n_blocks            INTEGER,
    total_datapoints    INTEGER,
    file_path           TEXT
);

CREATE TABLE block_index (
    doi                 TEXT NOT NULL,
    block_number        TEXT NOT NULL,
    block_type          TEXT NOT NULL,
    blocktype_num_id    TEXT NOT NULL,
    n_datapoints        INTEGER NOT NULL,
    system_type         TEXT NOT NULL,
    n_components        INTEGER NOT NULL,
    compound_system     TEXT,
    comp_num_ids        TEXT NOT NULL,
    prop_num_ids        TEXT NOT NULL,
    prop_ranges         TEXT,
    var_num_ids         TEXT,
    var_ranges          TEXT,
    constr_num_ids      TEXT,
    constr_values       TEXT,
    meas_num_ids        TEXT,
    solvent_comp_ids    TEXT,
    solvent_num_ids     TEXT,
    PRIMARY KEY (doi, block_number),
    FOREIGN KEY (doi) REFERENCES ref_index(doi)
);

CREATE TABLE block_compounds (
    doi                 TEXT NOT NULL,
    block_number        TEXT NOT NULL,
    block_type          TEXT NOT NULL,
    org_num             TEXT NOT NULL,
    comp_num_id         TEXT NOT NULL,
    comp_id             TEXT,
    comp_name           TEXT,
    comp_formula        TEXT,
    inchi_key           TEXT,
    sample_num          TEXT,
    PRIMARY KEY (doi, block_number, org_num),
    FOREIGN KEY (doi, block_number) REFERENCES block_index(doi, block_number)
);

CREATE TABLE block_properties (
    doi                 TEXT NOT NULL,
    block_number        TEXT NOT NULL,
    block_type          TEXT NOT NULL,
    BLKprop_id          TEXT NOT NULL,
    prop_id             TEXT NOT NULL,
    prop_name           TEXT NOT NULL,
    prop_group          TEXT NOT NULL,
    component_org_num   TEXT,
    phase_num_id        TEXT,
    phase_id            TEXT,
    min_value           REAL,
    max_value           REAL,
    mean_value          REAL,
    n_values            INTEGER,
    prop_num_id         TEXT NOT NULL,
    assessment_num      TEXT,
    PRIMARY KEY (doi, block_number, BLKprop_id),
    FOREIGN KEY (doi, block_number) REFERENCES block_index(doi, block_number)
);

CREATE TABLE block_variables (
    doi                 TEXT NOT NULL,
    block_number        TEXT NOT NULL,
    block_type          TEXT NOT NULL,
    BLKvar_id           TEXT NOT NULL,
    var_id              TEXT NOT NULL,
    var_name            TEXT NOT NULL,
    var_type_key        TEXT,
    component_org_num   TEXT,
    phase_num_id        TEXT,
    phase_id            TEXT,
    min_value           REAL,
    max_value           REAL,
    n_unique            INTEGER,
    var_num_id          TEXT NOT NULL,
    PRIMARY KEY (doi, block_number, BLKvar_id),
    FOREIGN KEY (doi, block_number) REFERENCES block_index(doi, block_number)
);

CREATE TABLE block_constraints (
    doi                 TEXT NOT NULL,
    block_number        TEXT NOT NULL,
    block_type          TEXT NOT NULL,
    BLKconstr_id        TEXT NOT NULL,
    constr_id           TEXT NOT NULL,
    constr_name         TEXT NOT NULL,
    constr_type_key     TEXT,
    component_org_num   TEXT,
    phase_num_id        TEXT,
    phase_id            TEXT,
    value               REAL,
    digits              INTEGER,
    constr_num_id       TEXT NOT NULL,
    PRIMARY KEY (doi, block_number, BLKconstr_id),
    FOREIGN KEY (doi, block_number) REFERENCES block_index(doi, block_number)
);

CREATE TABLE block_measurements (
    doi                 TEXT NOT NULL,
    block_number        TEXT NOT NULL,
    block_type          TEXT NOT NULL,
    BLKprop_id          TEXT NOT NULL,
    meas_id             TEXT,
    method_type         TEXT,
    method_name         TEXT,
    meas_num_id         TEXT,
    PRIMARY KEY (doi, block_number, BLKprop_id),
    FOREIGN KEY (doi, block_number, BLKprop_id)
        REFERENCES block_properties(doi, block_number, BLKprop_id)
);

CREATE TABLE block_reaction (
    doi                 TEXT NOT NULL,
    block_number        TEXT NOT NULL,
    block_type          TEXT NOT NULL,
    reaction_type       TEXT NOT NULL,
    rxn_type_num_id     TEXT NOT NULL,
    rxn_type_id         TEXT NOT NULL,
    participants        TEXT NOT NULL,
    PRIMARY KEY (doi, block_number),
    FOREIGN KEY (doi, block_number) REFERENCES block_index(doi, block_number)
);

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
        REFERENCES block_index(doi, block_number)
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
    PRIMARY KEY (doi, block_number, BLKsubsys_id, component_role, org_num),
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
    PRIMARY KEY (doi, block_number, BLKsubsys_id, BLKprop_id, support_role),
    FOREIGN KEY (doi, block_number, BLKsubsys_id)
        REFERENCES block_subsystems(doi, block_number, BLKsubsys_id)
);

CREATE TABLE compound_registry (
    comp_num_id     TEXT PRIMARY KEY,
    comp_id         TEXT NOT NULL,
    inchi_key       TEXT NOT NULL UNIQUE,
    common_name     TEXT,
    formula         TEXT,
    smiles          TEXT,
    standard_inchi  TEXT,
    n_papers        INTEGER
);
CREATE TABLE prop_registry (
    prop_num_id TEXT PRIMARY KEY,
    prop_id     TEXT NOT NULL UNIQUE,
    prop_name   TEXT NOT NULL,
    prop_group  TEXT NOT NULL,
    n_blocks    INTEGER
);
CREATE TABLE var_registry (
    var_num_id   TEXT PRIMARY KEY,
    var_id       TEXT NOT NULL UNIQUE,
    var_name     TEXT NOT NULL,
    var_type_key TEXT,
    n_blocks     INTEGER
);
CREATE TABLE constr_registry (
    constr_num_id   TEXT PRIMARY KEY,
    constr_id       TEXT NOT NULL UNIQUE,
    constr_name     TEXT NOT NULL,
    constr_type_key TEXT,
    n_blocks        INTEGER
);
CREATE TABLE meas_registry (
    meas_num_id TEXT PRIMARY KEY,
    meas_id     TEXT NOT NULL UNIQUE,
    method_name TEXT NOT NULL,
    method_type TEXT,
    n_blocks    INTEGER,
    n_aliases   INTEGER
);
CREATE TABLE meas_alias_registry (
    source_method_name TEXT NOT NULL,
    source_method_type TEXT NOT NULL,
    meas_num_id        TEXT NOT NULL,
    meas_id            TEXT NOT NULL,
    n_blocks           INTEGER,
    PRIMARY KEY (source_method_name, source_method_type),
    FOREIGN KEY (meas_num_id) REFERENCES meas_registry(meas_num_id)
);
CREATE TABLE phase_registry (
    phase_num_id    TEXT PRIMARY KEY,
    phase_id        TEXT NOT NULL UNIQUE,
    phase_name      TEXT NOT NULL,
    n_occurrences   INTEGER
);
CREATE TABLE blocktype_registry (
    blocktype_num_id TEXT PRIMARY KEY,
    block_type   TEXT NOT NULL,
    system_type  TEXT NOT NULL,
    n_blocks     INTEGER,
    UNIQUE(block_type, system_type)
);
CREATE TABLE rxn_type_registry (
    rxn_type_num_id TEXT PRIMARY KEY,
    rxn_type_id     TEXT NOT NULL UNIQUE,
    rxn_type_name   TEXT NOT NULL,
    n_blocks        INTEGER
);
CREATE TABLE solvent_registry (
    solvent_num_id TEXT PRIMARY KEY,
    comp_num_id  TEXT NOT NULL UNIQUE,
    inchi_key    TEXT,
    common_name  TEXT,
    formula      TEXT,
    n_blocks     INTEGER
);
CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);

CREATE INDEX idx_ref_year ON ref_index(year);
CREATE INDEX idx_ref_litid ON ref_index(lit_id);
CREATE INDEX idx_block_type ON block_index(block_type);
CREATE INDEX idx_blocktype_num ON block_index(blocktype_num_id);
CREATE INDEX idx_bi_compsys ON block_index(compound_system);
CREATE INDEX idx_bi_systype ON block_index(system_type);
CREATE INDEX idx_bp_propid ON block_properties(prop_id);
CREATE INDEX idx_bp_propgroup ON block_properties(prop_group);
CREATE INDEX idx_bp_numid ON block_properties(prop_num_id);
CREATE INDEX idx_bv_varid ON block_variables(var_id);
CREATE INDEX idx_bv_typekey ON block_variables(var_type_key);
CREATE INDEX idx_bv_numid ON block_variables(var_num_id);
CREATE INDEX idx_bc_constrid ON block_constraints(constr_id);
CREATE INDEX idx_bc_numid ON block_constraints(constr_num_id);
CREATE INDEX idx_bm_measid ON block_measurements(meas_id);
CREATE INDEX idx_bm_numid ON block_measurements(meas_num_id);
CREATE INDEX idx_comp_org ON block_compounds(org_num);
CREATE INDEX idx_bcomp_numid ON block_compounds(comp_num_id);
CREATE INDEX idx_subsystem_type ON block_subsystems(effective_system_type, search_eligible);
CREATE INDEX idx_subsystem_points ON block_subsystems(n_points);
CREATE INDEX idx_subsystem_comp_num ON block_subsystem_compounds(comp_num_id, component_role);
CREATE INDEX idx_subsystem_prop_num ON block_subsystem_properties(prop_num_id, support_role, phase_compatible);
CREATE INDEX idx_compreg_name ON compound_registry(common_name);
CREATE INDEX idx_compreg_formula ON compound_registry(formula);
"""


def _read_csv(name: str) -> list[dict]:
    with open(os.path.join(CSV_DIR, name), encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _int(value):
    return int(value) if value not in (None, "") else None


def _load_registries(cur: sqlite3.Cursor) -> dict[str, dict]:
    compounds = {}
    for row in _read_csv("compound_ids.csv"):
        gid = require_global_id("comp_num_id", row["comp_num_id"])
        cur.execute(
            "INSERT INTO compound_registry VALUES (?,?,?,?,?,?,?,?)",
            (gid, row["comp_id"], row["inchi_key"], row["common_name"], row["formula"],
             row.get("smiles", ""), row.get("standard_inchi", ""), _int(row.get("n_papers"))),
        )
        compounds[gid] = row

    specs = [
        ("property_ids.csv", "prop_num_id", "prop_registry", "prop_num_id",
         lambda r: (r["prop_id"], r["prop_name"], r["prop_group"], _int(r.get("n_blocks")))),
        ("variable_ids.csv", "var_num_id", "var_registry", "var_num_id",
         lambda r: (r["var_id"], r["var_name"], r.get("var_type_key", ""), _int(r.get("n_blocks")))),
        ("constraint_ids.csv", "constr_num_id", "constr_registry", "constr_num_id",
         lambda r: (r["constr_id"], r["constr_name"], r.get("constr_type_key", ""), _int(r.get("n_blocks")))),
        ("measurement_ids.csv", "meas_num_id", "meas_registry", "meas_num_id",
         lambda r: (r["meas_id"], r["method_name"], r.get("method_type", ""),
                    _int(r.get("n_blocks")), _int(r.get("n_aliases")))),
        ("phase_ids.csv", "phase_num_id", "phase_registry", "phase_num_id",
         lambda r: (r["phase_id"], r["phase_name"], _int(r.get("n_occurrences")))),
    ]
    for filename, field, table, kind, payload in specs:
        for row in _read_csv(filename):
            gid = require_global_id(kind, row[field])
            values = (gid, *payload(row))
            placeholders = ",".join("?" for _ in values)
            cur.execute(f"INSERT INTO {table} VALUES ({placeholders})", values)

    for row in _read_csv("measurement_aliases.csv"):
        gid = require_global_id("meas_num_id", row["meas_num_id"])
        cur.execute(
            "INSERT INTO meas_alias_registry VALUES (?,?,?,?,?)",
            (row["source_method_name"], row["source_method_type"], gid,
             row["meas_id"], _int(row.get("n_blocks"))),
        )

    for row in _read_csv("block_types.csv"):
        gid = require_global_id("blocktype_num_id", row["blocktype_num_id"])
        cur.execute(
            "INSERT INTO blocktype_registry VALUES (?,?,?,?)",
            (gid, row["block_type"], row["system_type"], _int(row.get("n_blocks"))),
        )
    for row in _read_csv("reaction_type_ids.csv"):
        gid = require_global_id("rxn_type_num_id", row["rxn_type_num_id"])
        cur.execute(
            "INSERT INTO rxn_type_registry VALUES (?,?,?,?)",
            (gid, row["rxn_type_id"], row["rxn_type_name"], _int(row.get("n_blocks"))),
        )
    for row in _read_csv("solvent_components.csv"):
        sid = require_global_id("solvent_num_id", row["solvent_num_id"])
        cid = require_global_id("comp_num_id", row["comp_num_id"])
        cur.execute(
            "INSERT INTO solvent_registry VALUES (?,?,?,?,?,?)",
            (sid, cid, row["inchi_key"], row["common_name"], row["formula"],
             _int(row["n_blocks_as_solvent"])),
        )
    return {"compounds": compounds}


def _load_references(cur: sqlite3.Cursor):
    for row in _read_csv("reference_ids.csv"):
        lit_num_id = require_global_id("lit_num_id", row["lit_num_id"])
        cur.execute(
            "INSERT INTO ref_index VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (row["doi"], row["lit_id"], lit_num_id, "", _int(row["year"]),
             row["journal"], row["first_author"],
             _int(row["n_compounds"]), _int(row["n_blocks"]),
             _int(row["total_datapoints"]), f'{row["doi"]}.json'),
        )


def _phase_fields(owner: dict, key: str = "phase") -> tuple:
    phase = owner[key]
    if phase is None:
        return None, None
    if not isinstance(phase, dict):
        raise TypeError(f"{key} must be an object or null")
    return phase["phase_num_id"], phase["phase_id"]


def _insert_card(cur: sqlite3.Cursor, card: dict, compound_registry: dict):
    doi = card["key"]["doi"]
    cur.execute(
        "UPDATE ref_index SET title=? WHERE doi=?",
        (card["paper"]["title"], doi),
    )
    for block in card["blocks"]:
        bn = require_block_id(block["block_number"], block_type=block["block_type"])
        blocktype_id = require_global_id("blocktype_num_id", block["blocktype_num_id"])
        compounds = block["compounds"]
        properties = block["properties"]
        variables = block["variables"]
        constraints = block["constraints"]
        solvents = block["solvents"]
        summary = block["data_summary"]
        pstats = summary["property_stats"]
        vranges = summary["variable_ranges"]

        comp_ids = [require_global_id("comp_num_id", c["comp_num_id"]) for c in compounds]
        prop_ids = [require_global_id("prop_num_id", p["prop_num_id"]) for p in properties]
        var_ids = [require_global_id("var_num_id", v["var_num_id"]) for v in variables]
        constr_ids = [require_global_id("constr_num_id", c["constr_num_id"]) for c in constraints]
        meas_ids = [
            require_global_id("meas_num_id", p["meas_num_id"])
            for p in properties if p["meas_num_id"] is not None
        ]
        solvent_ids = [require_global_id("solvent_num_id", s["solvent_num_id"]) for s in solvents]

        cur.execute(
            "INSERT INTO block_index VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                doi, bn, block["block_type"], blocktype_id,
                int(summary["n_points"]), block["system_type"], len(compounds),
                " + ".join(c["name"] for c in compounds),
                json.dumps(comp_ids), json.dumps(prop_ids),
                json.dumps([pstats[p["BLKprop_id"]] for p in properties]),
                json.dumps(var_ids) if var_ids else None,
                json.dumps([vranges[v["BLKvar_id"]] for v in variables]) if variables else None,
                json.dumps(constr_ids) if constr_ids else None,
                json.dumps([c["value"] for c in constraints]) if constraints else None,
                json.dumps(meas_ids) if meas_ids else None,
                json.dumps([s["component_org_num"] for s in solvents]) if solvents else None,
                json.dumps(solvent_ids) if solvent_ids else None,
            ),
        )

        subsystem_rows, subsystem_compound_rows, subsystem_property_rows = (
            project_subsystems(card, block)
        )
        cur.executemany(SUBSYSTEM_INSERT_SQL, subsystem_rows)
        cur.executemany(
            SUBSYSTEM_COMPOUND_INSERT_SQL, subsystem_compound_rows
        )
        cur.executemany(
            SUBSYSTEM_PROPERTY_INSERT_SQL, subsystem_property_rows
        )

        for comp in compounds:
            org = require_doi_comp_id(comp["org_num"])
            gid = require_global_id("comp_num_id", comp["comp_num_id"])
            canonical = compound_registry[gid]
            cur.execute(
                "INSERT INTO block_compounds VALUES (?,?,?,?,?,?,?,?,?,?)",
                (doi, bn, block["block_type"], org, gid, canonical["comp_id"],
                 comp["name"], comp["formula"], comp["inchi_key"],
                 comp["sample_num"]),
            )

        for prop in properties:
            local = require_block_local_id("prop", prop["BLKprop_id"])
            gid = require_global_id("prop_num_id", prop["prop_num_id"])
            stat = pstats[local]
            phase_num, phase_id = _phase_fields(prop, "property_phase")
            if phase_num:
                require_global_id("phase_num_id", phase_num)
            component = prop["component_org_num"]
            if component:
                require_doi_comp_id(component)
            uncertainty = prop["uncertainty"]
            if uncertainty is not None and not isinstance(uncertainty, dict):
                raise TypeError("property uncertainty must be an object or null")
            assessment = (
                uncertainty["assessment_num"] if uncertainty is not None else None
            )
            cur.execute(
                "INSERT INTO block_properties VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (doi, bn, block["block_type"], local, prop["prop_ID"], prop["name"],
                 prop["group"], component, phase_num, phase_id, stat["min"],
                 stat["max"], stat["mean"], stat["n"], gid, assessment),
            )
            meas_gid = prop["meas_num_id"]
            if meas_gid:
                require_global_id("meas_num_id", meas_gid)
            method_type = "standard" if prop["method_standard"] else (
                "custom" if prop["method_custom"] else None
            )
            cur.execute(
                "INSERT INTO block_measurements VALUES (?,?,?,?,?,?,?,?)",
                (doi, bn, block["block_type"], local, prop["meas_ID"], method_type,
                 prop["method_standard"] or prop["method_custom"], meas_gid),
            )

        for var in variables:
            local = require_block_local_id("var", var["BLKvar_id"])
            gid = require_global_id("var_num_id", var["var_num_id"])
            rng = vranges[local]
            phase_num, phase_id = _phase_fields(var)
            if phase_num:
                require_global_id("phase_num_id", phase_num)
            component = var["component_org_num"]
            if component:
                require_doi_comp_id(component)
            cur.execute(
                "INSERT INTO block_variables VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (doi, bn, block["block_type"], local, var["var_id"], var["name"],
                 var["type"], component, phase_num, phase_id, rng["min"],
                 rng["max"], rng["n_unique"], gid),
            )

        for constr in constraints:
            local = require_block_local_id("constr", constr["BLKconstr_id"])
            gid = require_global_id("constr_num_id", constr["constr_num_id"])
            phase_num, phase_id = _phase_fields(constr)
            if phase_num:
                require_global_id("phase_num_id", phase_num)
            component = constr["component_org_num"]
            if component:
                require_doi_comp_id(component)
            cur.execute(
                "INSERT INTO block_constraints VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (doi, bn, block["block_type"], local, constr["constr_id"], constr["name"],
                 constr["type"], component, phase_num, phase_id, constr["value"],
                 constr["digits"], gid),
            )

        reaction = block["reaction"]
        if reaction:
            rxn_gid = require_global_id("rxn_type_num_id", reaction["rxn_type_num_id"])
            cur.execute(
                "INSERT INTO block_reaction VALUES (?,?,?,?,?,?,?)",
                (doi, bn, block["block_type"], reaction["reaction_type"], rxn_gid,
                 reaction["rxn_type_id"], json.dumps(reaction["participants"])),
            )


def build_index(output: str = DB_PATH, pcs_db: str = PCS_DB) -> str:
    if not os.path.exists(pcs_db):
        raise FileNotFoundError(f"PCS database not found: {pcs_db}")
    os.makedirs(os.path.dirname(output), exist_ok=True)
    staging = output + ".building"
    if os.path.exists(staging):
        os.remove(staging)

    source = sqlite3.connect(f"file:{pcs_db}?mode=ro", uri=True)
    target = sqlite3.connect(staging)
    target.executescript(SCHEMA)
    cur = target.cursor()
    start = time.time()

    registry = _load_registries(cur)
    _load_references(cur)
    target.commit()

    cards = 0
    blocks = 0
    for (payload,) in source.execute("SELECT json_data FROM cards ORDER BY doi"):
        card = json.loads(payload)
        _insert_card(cur, card, registry["compounds"])
        cards += 1
        blocks += len(card["blocks"])
        if cards % 1000 == 0:
            target.commit()
            print(f"  {cards:,} cards / {blocks:,} blocks indexed")

    target.executemany(
        "INSERT INTO metadata(key,value) VALUES (?,?)",
        [
            ("id_schema", "prefixed-v2"),
            ("source_db", pcs_db),
            ("total_cards", str(cards)),
            ("total_blocks", str(blocks)),
            ("build_time_s", f"{time.time() - start:.1f}"),
        ],
    )
    target.commit()

    fk_errors = cur.execute("PRAGMA foreign_key_check").fetchall()
    db_blocks = cur.execute("SELECT COUNT(*) FROM block_index").fetchone()[0]
    if fk_errors or db_blocks != blocks:
        target.close()
        source.close()
        raise RuntimeError(
            f"Index validation failed: fk_errors={len(fk_errors)}, blocks={db_blocks}/{blocks}"
        )

    target.close()
    source.close()
    os.replace(staging, output)
    print(f"Built {output}: {cards:,} cards, {blocks:,} blocks")
    return output


def main():
    output = DB_PATH
    if "--output" in sys.argv:
        pos = sys.argv.index("--output")
        output = sys.argv[pos + 1]
    build_index(output=output)


if __name__ == "__main__":
    main()
