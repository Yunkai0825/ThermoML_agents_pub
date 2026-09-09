"""
Build a SQLite database of PCS INDIV cards (per-DOI property measurement blocks).

Iterates every paper in thermoml_raw.db, calls build_pcs_card() for each,
and stores the resulting card JSON plus summary stats.

Usage (from workspace root):
    python -m ThermoML_raw_json_to_card_db_parsers.property_card_helpers.build_pcs_indiv_db
"""

import json
import hashlib
import os
import msvcrt
import shutil
import sqlite3
import tempfile
import time
import traceback
from contextlib import contextmanager

from ThermoML_raw_json_to_card_db_parsers.property_card_helpers.pcs_builder import build_pcs_card
from ThermoML_raw_json_to_card_db_parsers.identity_translation import (
    TRANSLATION_CSV,
    get_global_identity_translations,
    source_catalog_sha256s,
    translation_csv_sha256,
    write_translation_csv,
)
from ThermoML_raw_json_to_card_db_parsers.index_lookup import ThermoMLIndex
from ThermoML_raw_json_to_card_db_parsers.shared_utils import bind_source_doi
from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    validate_nested_identifiers,
)
from ThermoML_raw_json_to_card_db_parsers.property_card_helpers.pcs_identity_enrichment import (
    IDENTITY_INDEX_SCHEMA_VERSION,
    COMPOSITION_SUBSYSTEM_SCHEMA_VERSION,
    validate_card_identity_indexes,
)

WORKSPACE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RAW_DB_PATH = os.path.join(WORKSPACE_ROOT, 'ThermoML.v2020-09-30.db', 'thermoml_raw.db')
OUTPUT_DIR = os.path.join(WORKSPACE_ROOT, 'card_databases_storage', 'Individual_cards_dbs')
OUTPUT_DB = os.path.join(OUTPUT_DIR, 'PCS_INDIV.db')

SCHEMA = """
CREATE TABLE cards (
    doi             TEXT PRIMARY KEY,
    lit_num_id      TEXT NOT NULL,
    n_blocks        INTEGER,
    total_datapoints INTEGER,
    json_data       TEXT NOT NULL
);

CREATE INDEX idx_cards_lit_num_id ON cards(lit_num_id);

CREATE TABLE metadata (
    key   TEXT PRIMARY KEY,
    value TEXT
);
"""


def _embedded_identity_counts(card, *, translations, doi=None):
    """Validate card-local block indexes and return aggregate entry counts."""
    validate_nested_identifiers(card)
    return validate_card_identity_indexes(
        card,
        translations=translations,
        doi=doi,
    )


def _validate_staging_database(
    conn,
    *,
    cards_expected,
    blocks_expected,
    statistics_expected,
    permutations_expected,
    subsystems_expected,
    translations,
    translation_filename,
    translation_sha256,
):
    foreign_key_errors = conn.execute("PRAGMA foreign_key_check").fetchall()
    if foreign_key_errors:
        raise RuntimeError(
            f"PCS staging database has foreign-key errors: "
            f"{foreign_key_errors[:5]!r}"
        )
    integrity = conn.execute("PRAGMA integrity_check").fetchall()
    if integrity != [("ok",)]:
        raise RuntimeError(
            f"PCS staging database failed integrity_check: {integrity[:5]!r}"
        )
    actual_tables = {
        row[0]
        for row in conn.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type = 'table' AND name NOT LIKE 'sqlite_%'"
        )
    }
    if actual_tables != {"cards", "metadata"}:
        raise RuntimeError(
            "PCS staging database must contain only cards and metadata tables; "
            f"found {sorted(actual_tables)!r}"
        )
    metadata = dict(conn.execute("SELECT key, value FROM metadata"))
    expected_metadata = {
        "identity_index_schema": IDENTITY_INDEX_SCHEMA_VERSION,
        "identity_translation_csv": translation_filename,
        "identity_translation_sha256": translation_sha256,
        "identity_storage": (
            "cards.json_data.blocks_summary.derived_indexes."
            "block_search_adv"
        ),
        "composition_subsystem_schema": COMPOSITION_SUBSYSTEM_SCHEMA_VERSION,
        "composition_subsystem_storage": (
            "cards.json_data.blocks_summary.derived_indexes."
            "composition_subsystems"
        ),
    }
    for key, expected_value in expected_metadata.items():
        if metadata.get(key) != expected_value:
            raise RuntimeError(
                f"PCS staging metadata {key!r} is "
                f"{metadata.get(key)!r}; expected {expected_value!r}"
            )

    cards_actual = 0
    blocks_actual = 0
    statistics_actual = 0
    permutations_actual = 0
    subsystems_actual = 0
    for doi, json_data in conn.execute(
        "SELECT doi, json_data FROM cards ORDER BY doi"
    ):
        card = json.loads(json_data)
        if card["key"]["doi"] != doi:
            raise RuntimeError(
                f"PCS card primary key {doi!r} disagrees with embedded DOI "
                f"{card['key']['doi']!r}"
            )
        n_blocks, n_statistics, n_permutations, n_subsystems = _embedded_identity_counts(
            card,
            translations=translations,
            doi=doi,
        )
        cards_actual += 1
        blocks_actual += n_blocks
        statistics_actual += n_statistics
        permutations_actual += n_permutations
        subsystems_actual += n_subsystems

    actual = {
        "cards": cards_actual,
        "blocks": blocks_actual,
        "statistics": statistics_actual,
        "permutations": permutations_actual,
        "subsystems": subsystems_actual,
    }
    expected = {
        "cards": cards_expected,
        "blocks": blocks_expected,
        "statistics": statistics_expected,
        "permutations": permutations_expected,
        "subsystems": subsystems_expected,
    }
    if actual != expected:
        raise RuntimeError(
            f"PCS staging row-count mismatch: actual={actual!r}, "
            f"expected={expected!r}"
        )


def _remove_staging_database(staging_db):
    for suffix in ("", "-journal", "-wal", "-shm"):
        path = staging_db + suffix
        if os.path.exists(path):
            os.remove(path)


def _file_sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _new_publish_staging_file(directory, *, prefix):
    """Reserve a build-unique same-directory path for atomic replacement."""
    descriptor, path = tempfile.mkstemp(
        dir=directory,
        prefix=prefix,
        suffix=".building",
    )
    os.close(descriptor)
    return path


@contextmanager
def _publication_lock():
    """Serialize the short two-artifact publication section on Windows."""
    lock_path = OUTPUT_DB + ".publish.lock"
    with open(lock_path, "a+b") as handle:
        handle.seek(0, os.SEEK_END)
        if handle.tell() == 0:
            handle.write(b"\0")
            handle.flush()
        handle.seek(0)
        deadline = time.monotonic() + 60.0
        while True:
            try:
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
                break
            except OSError:
                if time.monotonic() >= deadline:
                    raise TimeoutError(
                        "Timed out waiting for the PCS publication lock"
                    )
                time.sleep(0.25)
        try:
            yield
        finally:
            handle.seek(0)
            msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)


def _active_sqlite_sidecars(database_path):
    return [
        database_path + suffix
        for suffix in ("-journal", "-wal", "-shm")
        if os.path.exists(database_path + suffix)
    ]


def _replace_sqlite_database_with_retry(
    source_path,
    destination_path,
    *,
    timeout_seconds=60.0,
):
    """Atomically replace a quiescent SQLite DB despite delayed SMB closes."""
    deadline = time.monotonic() + timeout_seconds
    while True:
        active_sidecars = _active_sqlite_sidecars(destination_path)
        if active_sidecars:
            raise RuntimeError(
                "Refusing to replace PCS_INDIV.db while SQLite sidecars "
                f"exist: {active_sidecars!r}"
            )
        try:
            os.replace(source_path, destination_path)
            return
        except PermissionError as exc:
            if (
                getattr(exc, "winerror", None) not in {32, 33}
                or time.monotonic() >= deadline
            ):
                raise
            # An explicitly closed SQLite handle on an SMB share can remain
            # visible briefly while the server tears down its lease.
            time.sleep(0.25)


def _validate_published_pair(db_path=OUTPUT_DB):
    """Fail closed if a DB's content-addressed translation is unavailable."""
    conn = sqlite3.connect(db_path)
    try:
        metadata = dict(
            conn.execute(
                "SELECT key, value FROM metadata "
                "WHERE key IN ("
                "'identity_translation_csv', "
                "'identity_translation_sha256'"
                ")"
            )
        )
        integrity = conn.execute("PRAGMA integrity_check").fetchall()
    finally:
        conn.close()
    if integrity != [("ok",)]:
        raise RuntimeError(
            f"Published PCS database failed integrity_check: {integrity[:5]!r}"
        )
    filename = metadata.get("identity_translation_csv")
    expected_hash = metadata.get("identity_translation_sha256")
    if not filename or not expected_hash:
        raise RuntimeError(
            "Published PCS database has incomplete identity translation metadata"
        )
    path = os.path.join(os.path.dirname(TRANSLATION_CSV), filename)
    csv_hash = translation_csv_sha256(path)
    if expected_hash != csv_hash:
        raise RuntimeError(
            "Published PCS database and translation CSV are incoherent: "
            f"db={expected_hash!r}, csv={csv_hash!r}"
        )


def _content_addressed_translation_path(sha256):
    stem, extension = os.path.splitext(str(TRANSLATION_CSV))
    return f"{stem}.{sha256}{extension}"


def _install_content_addressed_translation(source_path, sha256):
    """Install one immutable translation generation if it is not present."""
    destination = _content_addressed_translation_path(sha256)
    if os.path.exists(destination):
        if translation_csv_sha256(destination) != sha256:
            raise RuntimeError(
                "Existing content-addressed translation CSV has "
                "unexpected content"
            )
        return destination

    staging = _new_publish_staging_file(
        os.path.dirname(TRANSLATION_CSV),
        prefix=".prop_var_constr_translations.immutable.",
    )
    try:
        shutil.copyfile(source_path, staging)
        if translation_csv_sha256(staging) != sha256:
            raise RuntimeError(
                "Content-addressed translation staging copy failed "
                "SHA-256 verification"
            )
        os.replace(staging, destination)
    finally:
        if os.path.exists(staging):
            try:
                os.remove(staging)
            except OSError:
                pass
    return destination


def _migrate_existing_translation_reference():
    """Make the prior PCS generation independent of the fixed-name export."""
    if not os.path.exists(OUTPUT_DB):
        return
    conn = sqlite3.connect(OUTPUT_DB)
    try:
        metadata = dict(
            conn.execute(
                "SELECT key, value FROM metadata "
                "WHERE key IN ("
                "'identity_translation_csv', "
                "'identity_translation_sha256'"
                ")"
            )
        )
        filename = metadata.get("identity_translation_csv")
        sha256 = metadata.get("identity_translation_sha256")
        if not filename or not sha256:
            return
        if filename != os.path.basename(TRANSLATION_CSV):
            return
        if translation_csv_sha256(TRANSLATION_CSV) != sha256:
            raise RuntimeError(
                "Legacy PCS database translation export does not match "
                "its metadata hash"
            )
        immutable = _install_content_addressed_translation(
            TRANSLATION_CSV,
            sha256,
        )
        conn.execute(
            "UPDATE metadata SET value = ? "
            "WHERE key = 'identity_translation_csv'",
            (os.path.basename(immutable),),
        )
        conn.execute(
            "INSERT OR REPLACE INTO metadata (key, value) VALUES (?, ?)",
            (
                "identity_translation_export_csv",
                os.path.basename(TRANSLATION_CSV),
            ),
        )
        conn.commit()
    finally:
        conn.close()
    _validate_published_pair()


def build_db(max_datapoints_per_block=50):
    """Build PCS_INDIV.db from thermoml_raw.db.

    The exact property/variable/constraint cross-role catalog is rebuilt from
    the authoritative ID catalogs before cards are generated.
    """
    if (
        max_datapoints_per_block is not None
        and (
            isinstance(max_datapoints_per_block, bool)
            or not isinstance(max_datapoints_per_block, int)
            or max_datapoints_per_block <= 0
        )
    ):
        raise ValueError(
            "max_datapoints_per_block must be None or a positive integer"
    )
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(TRANSLATION_CSV), exist_ok=True)
    local_staging_context = tempfile.TemporaryDirectory(
        prefix="thermoml_pcs_indiv_"
    )
    local_staging_dir = local_staging_context.name
    staging_db = os.path.join(local_staging_dir, "PCS_INDIV.db")
    staging_translation = os.path.join(
        local_staging_dir,
        os.path.basename(TRANSLATION_CSV),
    )
    previous_translation = os.path.join(
        local_staging_dir,
        os.path.basename(TRANSLATION_CSV) + ".previous",
    )

    source_hashes_at_start = source_catalog_sha256s()
    translation_rows = write_translation_csv(staging_translation)
    print(
        f"Translation registry: {len(translation_rows)} exact quantity keys "
        f"staged at {staging_translation}"
    )
    identity_translations = get_global_identity_translations(
        staging_translation
    )
    translation_hash_at_start = translation_csv_sha256(
        staging_translation
    )
    authoritative_translation = _content_addressed_translation_path(
        translation_hash_at_start
    )

    # Connect to raw DB
    raw_conn = sqlite3.connect(RAW_DB_PATH)
    raw_conn.row_factory = sqlite3.Row
    raw_conn.execute("PRAGMA query_only = ON")

    total_papers = raw_conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0]
    print(f"Raw DB: {total_papers} papers")

    # Create output DB
    out_conn = sqlite3.connect(staging_db)
    out_conn.execute("PRAGMA foreign_keys = ON")
    out_conn.executescript(SCHEMA)

    # Instantiate index once
    print("Loading ThermoMLIndex...")
    index = ThermoMLIndex()
    print("Index loaded.")

    cursor = raw_conn.execute("SELECT doi, json_data FROM papers ORDER BY doi")

    inserted = 0
    errors = 0
    error_dois = []
    identity_statistics_entries = 0
    identity_permutation_entries = 0
    enriched_blocks = 0
    composition_subsystem_entries = 0
    t0 = time.time()

    for row in cursor:
        doi = row["doi"]
        try:
            data = json.loads(row["json_data"])
            bind_source_doi(data, doi)
            card = build_pcs_card(
                data,
                index,
                max_datapoints_per_block=max_datapoints_per_block,
                identity_translations=identity_translations,
            )

            summary = card["blocks_summary"]
            n_blocks = summary["n_blocks"]
            total_dp = summary["total_datapoints"]
            lit_num_id = card["key"]["lit_num_id"]

            n_indexes, n_stats, n_permutations, n_subsystems = _embedded_identity_counts(
                card,
                translations=identity_translations,
                doi=doi,
            )
            card_json = json.dumps(
                card,
                ensure_ascii=False,
                separators=(',', ':'),
                allow_nan=False,
            )

            out_conn.execute(
                "INSERT INTO cards "
                "(doi, lit_num_id, n_blocks, total_datapoints, json_data) "
                "VALUES (?, ?, ?, ?, ?)",
                (doi, lit_num_id, n_blocks, total_dp, card_json),
            )
            identity_statistics_entries += n_stats
            identity_permutation_entries += n_permutations
            enriched_blocks += n_indexes
            composition_subsystem_entries += n_subsystems
            inserted += 1

        except Exception:
            errors += 1
            error_dois.append(doi)
            if errors <= 10:
                print(f"  ERROR [{doi}]: {traceback.format_exc().splitlines()[-1]}")

        if (inserted + errors) % 1000 == 0:
            out_conn.commit()
            elapsed = time.time() - t0
            rate = (inserted + errors) / elapsed if elapsed > 0 else 0
            print(f"  {inserted + errors:,}/{total_papers:,}  "
                  f"({inserted:,} ok, {errors} err)  "
                  f"{elapsed:.1f}s  {rate:.0f} papers/s")

    out_conn.commit()

    # Metadata and fail-closed validation
    elapsed = time.time() - t0
    finalization_error = None
    try:
        source_hashes_at_end = source_catalog_sha256s()
        translation_hash_at_end = translation_csv_sha256(
            staging_translation
        )
        if source_hashes_at_end != source_hashes_at_start:
            raise RuntimeError(
                "Canonical identity catalogs changed during the PCS build"
            )
        if translation_hash_at_end != translation_hash_at_start:
            raise RuntimeError(
                "Identity translation CSV changed during the PCS build"
            )
        meta = {
            "source_db": RAW_DB_PATH,
            "id_schema": "prefixed-v2",
            "identity_index_schema": IDENTITY_INDEX_SCHEMA_VERSION,
            "identity_translation_csv": os.path.basename(
                authoritative_translation
            ),
            "identity_translation_export_csv": os.path.basename(
                TRANSLATION_CSV
            ),
            "identity_translation_sha256": translation_hash_at_start,
            "identity_translation_quantity_keys": str(
                len(identity_translations.records)
            ),
            "identity_translation_global_ids": str(
                identity_translations.n_global_ids
            ),
            "identity_translation_source_catalog_sha256": json.dumps(
                source_hashes_at_start,
                sort_keys=True,
                separators=(",", ":"),
            ),
            "identity_storage": (
                "cards.json_data.blocks_summary.derived_indexes."
                "block_search_adv"
            ),
            "composition_subsystem_schema": COMPOSITION_SUBSYSTEM_SCHEMA_VERSION,
            "composition_subsystem_storage": (
                "cards.json_data.blocks_summary.derived_indexes."
                "composition_subsystems"
            ),
            "composition_subsystem_entries": str(composition_subsystem_entries),
            "identity_statistics_entries": str(identity_statistics_entries),
            "identity_permutation_entries": str(identity_permutation_entries),
            "identity_enriched_blocks": str(enriched_blocks),
            "total_papers": str(total_papers),
            "cards_inserted": str(inserted),
            "errors": str(errors),
            "max_datapoints_per_block": str(max_datapoints_per_block),
            "build_time_s": f"{elapsed:.1f}",
        }
        for k, v in meta.items():
            out_conn.execute(
                "INSERT INTO metadata (key, value) VALUES (?, ?)",
                (k, v),
            )
        out_conn.commit()
        _validate_staging_database(
            out_conn,
            cards_expected=inserted,
            blocks_expected=enriched_blocks,
            statistics_expected=identity_statistics_entries,
            permutations_expected=identity_permutation_entries,
            subsystems_expected=composition_subsystem_entries,
            translations=identity_translations,
            translation_filename=os.path.basename(
                authoritative_translation
            ),
            translation_sha256=translation_hash_at_start,
        )
    except Exception as exc:
        finalization_error = exc
    finally:
        raw_conn.close()
        try:
            out_conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
        except Exception as exc:
            if finalization_error is None:
                finalization_error = exc
        finally:
            out_conn.close()

    if finalization_error is not None:
        _remove_staging_database(staging_db)
        local_staging_context.cleanup()
        raise finalization_error

    db_size_mb = os.path.getsize(staging_db) / (1024 * 1024)
    print(f"\nDone: {inserted:,} cards in {elapsed:.1f}s  "
          f"({errors} errors)  DB size: {db_size_mb:.1f} MB")

    if error_dois:
        print(f"Error DOIs (first 20): {error_dois[:20]}")
        _remove_staging_database(staging_db)
        local_staging_context.cleanup()
        raise RuntimeError(f"PCS rebuild rejected: {errors} card generation error(s)")

    publish_staging_db = None
    publish_staging_export_translation = None
    database_was_published = False
    try:
        publish_staging_db = _new_publish_staging_file(
            OUTPUT_DIR,
            prefix=".PCS_INDIV.",
        )
        publish_staging_export_translation = _new_publish_staging_file(
            os.path.dirname(TRANSLATION_CSV),
            prefix=".prop_var_constr_translations.export.",
        )
        shutil.copyfile(
            staging_translation,
            publish_staging_export_translation,
        )
        shutil.copyfile(staging_db, publish_staging_db)
        local_hash = _file_sha256(staging_db)
        published_hash = _file_sha256(publish_staging_db)
        if published_hash != local_hash:
            raise RuntimeError(
                "PCS publish staging copy failed SHA-256 verification"
            )
        if (
            translation_csv_sha256(publish_staging_export_translation)
            != translation_hash_at_start
        ):
            raise RuntimeError(
                "Translation export staging copy failed SHA-256 verification"
            )

        # The content-addressed CSV is immutable and is installed before the
        # database. Replacing OUTPUT_DB is therefore the single runtime commit:
        # its metadata points to a CSV generation that already exists. The
        # fixed-name CSV is only a human-facing export.
        with _publication_lock():
            active_sidecars = _active_sqlite_sidecars(OUTPUT_DB)
            if active_sidecars:
                raise RuntimeError(
                    "Refusing to replace PCS_INDIV.db while SQLite sidecars "
                    f"exist: {active_sidecars!r}"
                )
            _migrate_existing_translation_reference()
            installed_translation = _install_content_addressed_translation(
                staging_translation,
                translation_hash_at_start,
            )
            if installed_translation != authoritative_translation:
                raise RuntimeError(
                    "Installed translation path disagrees with build metadata"
                )
            _validate_published_pair(publish_staging_db)
            active_sidecars = _active_sqlite_sidecars(OUTPUT_DB)
            if active_sidecars:
                raise RuntimeError(
                    "Existing PCS migration left active SQLite sidecars: "
                    f"{active_sidecars!r}"
                )

            had_previous_translation = os.path.exists(TRANSLATION_CSV)
            previous_translation_hash = None
            if had_previous_translation:
                shutil.copyfile(TRANSLATION_CSV, previous_translation)
                previous_translation_hash = translation_csv_sha256(
                    previous_translation
                )
            os.replace(
                publish_staging_export_translation,
                TRANSLATION_CSV,
            )
            try:
                _replace_sqlite_database_with_retry(
                    publish_staging_db,
                    OUTPUT_DB,
                )
            except Exception:
                if had_previous_translation:
                    shutil.copyfile(
                        previous_translation,
                        publish_staging_export_translation,
                    )
                    os.replace(
                        publish_staging_export_translation,
                        TRANSLATION_CSV,
                    )
                    if (
                        translation_csv_sha256(TRANSLATION_CSV)
                        != previous_translation_hash
                    ):
                        raise RuntimeError(
                            "Failed to verify restored translation export"
                        )
                elif os.path.exists(TRANSLATION_CSV):
                    os.remove(TRANSLATION_CSV)
                raise
            database_was_published = True
    finally:
        if publish_staging_db is not None:
            try:
                _remove_staging_database(publish_staging_db)
            except OSError:
                pass
        if (
            publish_staging_export_translation is not None
            and os.path.exists(publish_staging_export_translation)
        ):
            try:
                os.remove(publish_staging_export_translation)
            except OSError:
                pass
        local_staging_context.cleanup()
    if not database_was_published:
        raise RuntimeError(
            "PCS database was not published"
        )
    print(
        f"Published PCS database: {OUTPUT_DB} (sha256={local_hash})\n"
        f"Published authoritative translation CSV: "
        f"{authoritative_translation}\n"
        f"Published translation CSV export: {TRANSLATION_CSV} "
        f"(sha256={translation_hash_at_start})"
    )

    return inserted, errors


if __name__ == "__main__":
    build_db()
