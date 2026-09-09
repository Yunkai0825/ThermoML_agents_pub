"""
Build the MTDKS INDIV card database.

Creates card_databases_storage/MTDKS_INDIV.db with one row per DOI containing
the full measurement-method usage card as JSON.

Run from workspace root:
    python -m ThermoML_raw_json_to_card_db_parsers.measurement_card_helpers.build_mtdks_indiv_db
"""

import json
import os
import sqlite3
import time

from ThermoML_raw_json_to_card_db_parsers.measurement_card_helpers.mtdks_builder import build_mtdks_card
from ThermoML_raw_json_to_card_db_parsers.index_lookup import ThermoMLIndex
from ThermoML_raw_json_to_card_db_parsers.shared_utils import bind_source_doi

# Paths relative to workspace root
RAW_DB = os.path.join("ThermoML.v2020-09-30.db", "thermoml_raw.db")
OUT_DIR = os.path.join("card_databases_storage", "Individual_cards_dbs")
OUT_DB = os.path.join(OUT_DIR, "MTDKS_INDIV.db")
BATCH = 2000


def build_db():
    """Build the MTDKS INDIV card database from the raw ThermoML DB."""
    os.makedirs(OUT_DIR, exist_ok=True)
    staging_db = OUT_DB + ".building"
    for suffix in ("", "-wal", "-shm"):
        path = staging_db + suffix
        if os.path.exists(path):
            os.remove(path)

    # Open raw DB (read-only)
    raw = sqlite3.connect(f"file:{RAW_DB}?mode=ro", uri=True)
    raw.row_factory = sqlite3.Row

    # Open output DB
    out = sqlite3.connect(staging_db)
    out.execute("PRAGMA journal_mode=WAL")
    out.execute(
        "CREATE TABLE cards ("
        "  doi TEXT PRIMARY KEY,"
        "  lit_num_id TEXT NOT NULL,"
        "  n_methods INTEGER,"
        "  json_data TEXT NOT NULL"
        ")"
    )
    out.execute("CREATE INDEX idx_cards_lit_num_id ON cards(lit_num_id)")
    out.execute(
        "CREATE TABLE metadata ("
        "  key TEXT PRIMARY KEY,"
        "  value TEXT"
        ")"
    )

    # Load index once
    print("Loading ThermoMLIndex ...")
    index = ThermoMLIndex()
    print("Index loaded.")

    cur = raw.execute("SELECT doi, json_data FROM papers ORDER BY doi")
    inserted = 0
    errors = []
    t0 = time.time()

    for row in cur:
        doi = row["doi"]
        try:
            data = json.loads(row["json_data"])
            bind_source_doi(data, doi)
            card = build_mtdks_card(data, index)
            lit_num_id = card["key"]["lit_num_id"]
            n_methods = card["methods_summary"]["n_unique_methods"]
            out.execute(
                "INSERT INTO cards (doi, lit_num_id, n_methods, json_data) VALUES (?,?,?,?)",
                (doi, lit_num_id, n_methods, json.dumps(card, ensure_ascii=False)),
            )
            inserted += 1
        except Exception as exc:
            errors.append((doi, str(exc)))
            print(f"  ERROR [{doi}]: {exc}")

        if inserted % BATCH == 0 and inserted > 0:
            out.commit()
            elapsed = time.time() - t0
            print(f"  {inserted} cards inserted  ({elapsed:.1f}s)")

    out.commit()

    # Write metadata
    out.execute("INSERT INTO metadata VALUES (?, ?)", ("built_at", time.strftime("%Y-%m-%dT%H:%M:%S")))
    out.execute("INSERT INTO metadata VALUES (?, ?)", ("id_schema", "prefixed-v2"))
    out.execute("INSERT INTO metadata VALUES (?, ?)", ("total_cards", str(inserted)))
    out.execute("INSERT INTO metadata VALUES (?, ?)", ("total_errors", str(len(errors))))
    out.execute("INSERT INTO metadata VALUES (?, ?)", ("source_db", RAW_DB))
    if errors:
        out.execute("INSERT INTO metadata VALUES (?, ?)", ("error_dois", json.dumps([e[0] for e in errors])))
    out.commit()

    raw.close()
    out.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    out.close()

    elapsed = time.time() - t0
    db_size_mb = os.path.getsize(staging_db) / (1024 * 1024)
    print(f"\nDone in {elapsed:.1f}s")
    print(f"  Cards inserted : {inserted}")
    print(f"  Errors         : {len(errors)}")
    print(f"  DB size        : {db_size_mb:.1f} MB")
    if errors:
        print(f"  Failed DOIs    : {[e[0] for e in errors[:20]]}")
        for suffix in ("", "-wal", "-shm"):
            path = staging_db + suffix
            if os.path.exists(path):
                os.remove(path)
        raise RuntimeError(f"MTDKS rebuild rejected: {len(errors)} card generation error(s)")
    os.replace(staging_db, OUT_DB)
    print(f"Published atomically: {OUT_DB}")
    return inserted, errors


if __name__ == "__main__":
    build_db()
