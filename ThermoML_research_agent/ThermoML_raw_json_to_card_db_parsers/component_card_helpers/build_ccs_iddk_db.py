"""
Build SQLite database of CCS compound identity (ID & DK) cards.

Creates card_databases_storage/CCS_ID_DK.db with one row per unique compound,
covering all 8526 compounds in the canonical index (including 9 with
synthetic NO_INCHIKEY keys).

Usage:
    python -m ThermoML_raw_json_to_card_db_parsers.component_card_helpers.build_ccs_iddk_db
"""

import json
import logging
import os
import sqlite3
import sys
from datetime import datetime, timezone

from ThermoML_raw_json_to_card_db_parsers.id_schema import require_global_id

try:
    from rdkit import Chem, RDLogger
    from rdkit.Chem import AllChem, MACCSkeys
    RDLogger.DisableLog("rdApp.*")
    _HAS_RDKIT = True
except ImportError:
    _HAS_RDKIT = False

log = logging.getLogger("build-ccs-iddk")

MORGAN_RADIUS = 2
MORGAN_NBITS = 2048


def _compute_fingerprints(smiles: str) -> tuple:
    """Return (maccs_bitstring, morgan_bitstring, 'ok') or (None, None, status)."""
    if not _HAS_RDKIT:
        return None, None, "no_rdkit"
    if not smiles:
        return None, None, "no_structure"
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None, None, "parse_error"
    maccs = MACCSkeys.GenMACCSKeys(mol).ToBitString()
    morgan = AllChem.GetMorganFingerprintAsBitVect(
        mol, MORGAN_RADIUS, nBits=MORGAN_NBITS
    ).ToBitString()
    return maccs, morgan, "ok"


def build_db():
    """Build (or rebuild) CCS_ID_DK.db from raw ThermoML data."""
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    raw_db_path = os.path.join(root, "ThermoML.v2020-09-30.db", "thermoml_raw.db")
    out_dir = os.path.join(root, "card_databases_storage", "Individual_cards_dbs")
    os.makedirs(out_dir, exist_ok=True)
    out_db = os.path.join(out_dir, "CCS_ID_DK.db")

    staging = out_db + ".building"
    for suffix in ("", "-wal", "-shm"):
        path = staging + suffix
        if os.path.exists(path):
            os.remove(path)

    # Load index
    from ThermoML_raw_json_to_card_db_parsers.index_lookup import ThermoMLIndex
    index = ThermoMLIndex()

    # Build identity cards from raw DB (covers compounds WITH InChIKey)
    from ThermoML_raw_json_to_card_db_parsers._ID_and_DK_card_helper.ccs_identity_builder import (
        build_all_ccs_identity_cards,
        _inchi_to_smiles,
    )
    print("Building identity cards from raw DB...")
    cards = build_all_ccs_identity_cards(raw_db_path, index)
    print(f"  Cards from raw DB: {len(cards)}")

    # Index the cards we already have by comp_num_id
    seen_ids = {c["comp_num_id"] for c in cards if c["comp_num_id"] is not None}

    # Add synthetic-key compounds not covered by the raw-DB scan
    csv_compounds = index._compound_by_inchikey  # all indexed compounds
    missing_count = 0
    for ik, row in csv_compounds.items():
        cid = row["comp_num_id"]
        if cid in seen_ids:
            continue
        # Build a minimal identity card from the index row
        inchi = row.get("standard_inchi") or None
        cards.append({
            "comp_num_id": cid,
            "identity": {
                "inchi_key": ik,
                "SMILES": row.get("smiles") or _inchi_to_smiles(inchi),
                "InChI": inchi,
                "formula": row.get("formula", ""),
            },
            "names": {
                "primary_name": row.get("common_name", ""),
                "all_names": [row["common_name"]] if row.get("common_name") else [],
            },
        })
        seen_ids.add(cid)
        missing_count += 1

    print(f"  Supplemented from index (synthetic keys): {missing_count}")
    print(f"  Total cards: {len(cards)}")

    # Create output database
    conn = sqlite3.connect(staging)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute(
        "CREATE TABLE cards ("
        "  comp_num_id TEXT PRIMARY KEY,"
        "  inchi_key TEXT,"
        "  primary_name TEXT,"
        "  formula TEXT,"
        "  smiles TEXT,"
        "  maccs_fingerprint TEXT,"
        "  morgan_fingerprint TEXT,"
        "  fp_status TEXT NOT NULL DEFAULT 'no_structure'"
        "    CHECK(fp_status IN ('ok','no_structure','parse_error','no_rdkit')),"
        "  json_data TEXT NOT NULL"
        ")"
    )
    conn.execute("CREATE INDEX idx_cards_inchi_key ON cards(inchi_key)")
    conn.execute("CREATE INDEX idx_cards_fp_status ON cards(fp_status)")
    conn.execute(
        "CREATE TABLE metadata ("
        "  key TEXT PRIMARY KEY,"
        "  value TEXT"
        ")"
    )

    # Insert cards (with fingerprints)
    inserted = 0
    fp_ok = fp_skip = fp_err = 0
    for card in cards:
        cid = require_global_id("comp_num_id", card["comp_num_id"])
        smiles = card.get("identity", {}).get("SMILES", "") or ""
        maccs, morgan, fp_status = _compute_fingerprints(smiles)
        if fp_status == "ok":
            fp_ok += 1
        elif fp_status == "no_structure":
            fp_skip += 1
        else:
            fp_err += 1
        conn.execute(
            "INSERT INTO cards "
            "(comp_num_id, inchi_key, primary_name, formula, smiles, "
            " maccs_fingerprint, morgan_fingerprint, fp_status, json_data) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                cid,
                card["identity"]["inchi_key"],
                card["names"]["primary_name"],
                card["identity"]["formula"],
                smiles,
                maccs,
                morgan,
                fp_status,
                json.dumps(card, ensure_ascii=False),
            ),
        )
        inserted += 1
    print(f"  Fingerprints: ok={fp_ok}  no_structure={fp_skip}  errors={fp_err}")

    # Metadata
    now = datetime.now(timezone.utc).isoformat()
    conn.execute("INSERT INTO metadata VALUES (?, ?)", ("build_timestamp", now))
    conn.execute("INSERT INTO metadata VALUES (?, ?)", ("id_schema", "prefixed-v2"))
    conn.execute("INSERT INTO metadata VALUES (?, ?)", ("total_cards", str(inserted)))
    expected = len(index._compound_by_inchikey)
    if inserted != expected:
        conn.close()
        for suffix in ("", "-wal", "-shm"):
            path = staging + suffix
            if os.path.exists(path):
                os.remove(path)
        raise RuntimeError(
            "CCS ID/DK rebuild rejected: "
            f"inserted={inserted}, expected={expected}"
        )

    conn.commit()
    conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    conn.close()
    file_size = os.path.getsize(staging)
    print(f"\nDone.  {inserted} cards inserted; every card has a GLOBcomp_* ID.")
    print(f"DB: {out_db}  ({file_size:,} bytes / {file_size/1024:.1f} KB)")
    os.replace(staging, out_db)
    print(f"Published atomically: {out_db}")
    return out_db


if __name__ == "__main__":
    # Ensure workspace root is on sys.path for package imports
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if root not in sys.path:
        sys.path.insert(0, root)
    build_db()
