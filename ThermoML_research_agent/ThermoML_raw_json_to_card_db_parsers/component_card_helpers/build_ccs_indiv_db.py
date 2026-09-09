"""
Build SQLite database of CCS INDIV (per-DOI sample/purity) cards.

Iterates every paper in the raw ThermoML database, calls build_ccs_card()
for each, and stores the resulting JSON card in a new SQLite database.

Usage (from workspace root):
    python -m ThermoML_raw_json_to_card_db_parsers.component_card_helpers.build_ccs_indiv_db
"""

import json
import os
import sqlite3
import time

from ThermoML_raw_json_to_card_db_parsers.component_card_helpers.ccs_builder import build_ccs_card
from ThermoML_raw_json_to_card_db_parsers.index_lookup import ThermoMLIndex
from ThermoML_raw_json_to_card_db_parsers.shared_utils import bind_source_doi

_WORKSPACE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_RAW_DB = os.path.join(_WORKSPACE, "ThermoML.v2020-09-30.db", "thermoml_raw.db")
_OUT_DIR = os.path.join(_WORKSPACE, "card_databases_storage", "Individual_cards_dbs")
_OUT_DB = os.path.join(_OUT_DIR, "CCS_INDIV.db")

BATCH_SIZE = 2000


def build_db():
    """Build the CCS INDIV card database from scratch."""
    os.makedirs(_OUT_DIR, exist_ok=True)
    staging_db = _OUT_DB + ".building"
    for suffix in ("", "-wal", "-shm"):
        path = staging_db + suffix
        if os.path.exists(path):
            os.remove(path)

    # Open raw DB (read-only)
    raw_conn = sqlite3.connect(f"file:{_RAW_DB}?mode=ro", uri=True)
    raw_conn.execute("PRAGMA journal_mode=WAL")
    raw_cur = raw_conn.cursor()

    # Open output DB
    out_conn = sqlite3.connect(staging_db)
    out_conn.execute("PRAGMA journal_mode=WAL")
    out_conn.execute("PRAGMA synchronous=NORMAL")
    out_conn.execute("""
        CREATE TABLE cards (
            doi         TEXT PRIMARY KEY,
            lit_num_id  TEXT NOT NULL,
            n_compounds INTEGER,
            json_data   TEXT NOT NULL
        )
    """)
    out_conn.execute("CREATE INDEX idx_cards_lit_num_id ON cards(lit_num_id)")
    out_conn.execute("""
        CREATE TABLE metadata (
            key   TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    out_conn.commit()

    # Build index once
    print("Loading ThermoMLIndex …")
    index = ThermoMLIndex()
    print("Index loaded.")

    raw_cur.execute("SELECT doi, json_data FROM papers ORDER BY doi")

    t0 = time.time()
    inserted = 0
    errors = []
    total_compounds = 0

    while True:
        rows = raw_cur.fetchmany(BATCH_SIZE)
        if not rows:
            break

        for doi, raw_json in rows:
            try:
                data = json.loads(raw_json)
                bind_source_doi(data, doi)
                card = build_ccs_card(data, index)
                lit_num_id = card["key"]["lit_num_id"]
                n_comp = len(card["compounds"])
                total_compounds += n_comp
                out_conn.execute(
                    "INSERT INTO cards(doi, lit_num_id, n_compounds, json_data) VALUES (?,?,?,?)",
                    (doi, lit_num_id, n_comp, json.dumps(card, ensure_ascii=False)),
                )
                inserted += 1
            except Exception as exc:
                errors.append((doi, str(exc)))

        out_conn.commit()
        elapsed = time.time() - t0
        print(f"  … {inserted:>6,d} cards  |  {len(errors)} errors  |  {elapsed:,.1f}s")

    # Final commit & metadata
    out_conn.commit()
    elapsed = time.time() - t0

    out_conn.execute("INSERT INTO metadata VALUES (?,?)", ("total_cards", str(inserted)))
    out_conn.execute("INSERT INTO metadata VALUES (?,?)", ("id_schema", "prefixed-v2"))
    out_conn.execute("INSERT INTO metadata VALUES (?,?)", ("total_compounds", str(total_compounds)))
    out_conn.execute("INSERT INTO metadata VALUES (?,?)", ("error_count", str(len(errors))))
    out_conn.execute("INSERT INTO metadata VALUES (?,?)", ("build_time_sec", f"{elapsed:.1f}"))
    if errors:
        out_conn.execute(
            "INSERT INTO metadata VALUES (?,?)",
            ("error_details", json.dumps(errors[:200], ensure_ascii=False)),
        )
    out_conn.commit()
    out_conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    out_conn.close()
    raw_conn.close()

    db_size_mb = os.path.getsize(staging_db) / (1024 * 1024)
    print(f"\nDone — {inserted:,d} cards, {total_compounds:,d} compound entries, "
          f"{len(errors)} errors, DB size {db_size_mb:.1f} MB, {elapsed:.1f}s")
    if errors:
        print(f"First 10 errors:")
        for doi, msg in errors[:10]:
            print(f"  {doi}: {msg}")
        for suffix in ("", "-wal", "-shm"):
            path = staging_db + suffix
            if os.path.exists(path):
                os.remove(path)
        raise RuntimeError(f"CCS rebuild rejected: {len(errors)} card generation error(s)")

    os.replace(staging_db, _OUT_DB)
    print(f"Published atomically: {_OUT_DB}")


if __name__ == "__main__":
    build_db()
