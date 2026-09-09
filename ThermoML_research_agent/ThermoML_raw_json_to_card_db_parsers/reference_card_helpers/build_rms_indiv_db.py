"""
Build SQLite database of RMS INDIV (per-DOI reference metadata) cards.

Creates card_databases_storage/RMS_INDIV.db with one row per paper,
containing the full RMS card JSON plus key indexed columns.

Usage:
    python -m ThermoML_raw_json_to_card_db_parsers.reference_card_helpers.build_rms_indiv_db
"""

import json
import os
import sqlite3
import time

from ThermoML_raw_json_to_card_db_parsers.index_lookup import ThermoMLIndex
from ThermoML_raw_json_to_card_db_parsers.reference_card_helpers.rms_builder import build_rms_card
from ThermoML_raw_json_to_card_db_parsers.shared_utils import bind_source_doi

_ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
RAW_DB = os.path.join(_ROOT, "ThermoML.v2020-09-30.db", "thermoml_raw.db")
OUT_DIR = os.path.join(_ROOT, "card_databases_storage", "Individual_cards_dbs")
OUT_DB = os.path.join(OUT_DIR, "RMS_INDIV.db")


def build_db(raw_db=RAW_DB, out_db=OUT_DB):
    """Build the RMS_INDIV card database from thermoml_raw.db."""
    os.makedirs(os.path.dirname(out_db), exist_ok=True)

    staging_db = out_db + ".building"
    for suffix in ("", "-wal", "-shm"):
        path = staging_db + suffix
        if os.path.exists(path):
            os.remove(path)

    # Open raw DB
    src = sqlite3.connect(raw_db)
    src.execute("PRAGMA journal_mode=WAL")

    # Create output DB
    dst = sqlite3.connect(staging_db)
    dst.execute("PRAGMA journal_mode=WAL")
    dst.execute("PRAGMA synchronous=NORMAL")

    dst.execute("""
        CREATE TABLE cards (
            doi          TEXT PRIMARY KEY,
            lit_num_id   TEXT NOT NULL,
            year         INTEGER,
            journal      TEXT,
            title        TEXT,
            n_compounds  INTEGER,
            n_blocks     INTEGER,
            json_data    TEXT NOT NULL
        )
    """)
    dst.execute("CREATE INDEX idx_lit_num_id ON cards(lit_num_id)")
    dst.execute("CREATE INDEX idx_year ON cards(year)")
    dst.execute("CREATE INDEX idx_journal ON cards(journal)")

    dst.execute("""
        CREATE TABLE metadata (
            key   TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    dst.commit()

    # Instantiate index once
    index = ThermoMLIndex()

    # Iterate all papers
    cursor = src.execute("SELECT doi, json_data FROM papers ORDER BY doi")
    inserted = 0
    errors = []
    t0 = time.time()

    for doi, raw_json in cursor:
        try:
            data = json.loads(raw_json)
            bind_source_doi(data, doi)
            card = build_rms_card(data, index)

            lit_num_id = card["identity"]["lit_num_id"]
            year = card["bibliographic"]["year"]
            journal = card["bibliographic"]["journal"]
            title = card["bibliographic"]["title"]
            n_compounds = card["data_inventory"]["n_compounds"]
            n_blocks = card["data_inventory"]["n_blocks"]

            dst.execute(
                "INSERT INTO cards (doi, lit_num_id, year, journal, title, n_compounds, n_blocks, json_data) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (doi, lit_num_id, year, journal, title, n_compounds, n_blocks,
                 json.dumps(card, ensure_ascii=False)),
            )
            inserted += 1

            if inserted % 2000 == 0:
                dst.commit()
                elapsed = time.time() - t0
                print(f"  {inserted:,} cards inserted  ({elapsed:.1f}s)")

        except Exception as exc:
            errors.append((doi, str(exc)))

    dst.commit()
    elapsed = time.time() - t0

    # Write metadata
    dst.execute("INSERT INTO metadata VALUES ('total_cards', ?)", (str(inserted),))
    dst.execute("INSERT INTO metadata VALUES ('id_schema', 'prefixed-v2')")
    dst.execute("INSERT INTO metadata VALUES ('error_count', ?)", (str(len(errors)),))
    dst.execute("INSERT INTO metadata VALUES ('build_time_s', ?)", (f"{elapsed:.1f}",))
    dst.commit()

    src.close()
    dst.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    dst.close()

    db_size = os.path.getsize(staging_db)
    print(f"\nDone: {inserted:,} cards in {elapsed:.1f}s")
    print(f"DB size: {db_size / 1024 / 1024:.1f} MB")
    print(f"Errors: {len(errors)}")
    if errors:
        for doi, msg in errors[:20]:
            print(f"  ERROR {doi}: {msg}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more")

    if errors:
        for suffix in ("", "-wal", "-shm"):
            path = staging_db + suffix
            if os.path.exists(path):
                os.remove(path)
        raise RuntimeError(f"RMS rebuild rejected: {len(errors)} card generation error(s)")

    os.replace(staging_db, out_db)
    print(f"Published atomically: {out_db}")

    return inserted, errors


if __name__ == "__main__":
    build_db()
