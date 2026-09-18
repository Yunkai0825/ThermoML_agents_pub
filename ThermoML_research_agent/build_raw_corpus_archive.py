#!/usr/bin/env python3
"""Build one indexed, zlib-compressed ThermoML JSON/XML container.

JSON is streamed from ``thermoml_raw.db`` and paired with each original XML
document. The atomic output is
``ThermoML.v2020-09-30.db/thermoml_raw_corpus.db``.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import os
import sqlite3
import sys
import zlib
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = ROOT / "ThermoML.v2020-09-30.db"
DEFAULT_RAW_DB = DEFAULT_SOURCE / "thermoml_raw.db"
DEFAULT_OUTPUT = DEFAULT_SOURCE / "thermoml_raw_corpus.db"


def _compress_record(record: tuple, source: Path,
                     compresslevel: int) -> tuple:
    doi, file_path, json_text = record
    member = PurePosixPath(str(file_path).replace("\\", "/"))
    xml_member = member.with_suffix(".xml")
    xml_path = source.joinpath(*xml_member.parts)
    xml_bytes = xml_path.read_bytes()
    json_bytes = json_text.encode("utf-8")
    return (
        member.as_posix(),
        doi,
        sqlite3.Binary(zlib.compress(json_bytes, compresslevel)),
        sqlite3.Binary(zlib.compress(xml_bytes, compresslevel)),
        len(json_bytes),
        len(xml_bytes),
        zlib.crc32(json_bytes),
        zlib.crc32(xml_bytes),
    )


def _verify(output: Path, expected_count: int) -> None:
    connection = sqlite3.connect(str(output))
    try:
        integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
        if integrity != "ok":
            raise RuntimeError(f"SQLite integrity check failed: {integrity}")
        count = connection.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
        if count != expected_count:
            raise RuntimeError(
                f"Container row count mismatch: expected {expected_count}, found {count}"
            )
        cursor = connection.execute(
            "SELECT path, json_zlib, xml_zlib, json_size, xml_size, "
            "json_crc32, xml_crc32 FROM documents ORDER BY path"
        )
        for index, row in enumerate(cursor, start=1):
            json_bytes = zlib.decompress(row[1])
            xml_bytes = zlib.decompress(row[2])
            if len(json_bytes) != row[3] or zlib.crc32(json_bytes) != row[5]:
                raise RuntimeError(f"JSON verification failed: {row[0]}")
            if len(xml_bytes) != row[4] or zlib.crc32(xml_bytes) != row[6]:
                raise RuntimeError(f"XML verification failed: {row[0]}")
            if index % 1000 == 0 or index == expected_count:
                print(f"Verified {index:,}/{expected_count:,}: {row[0]}", flush=True)
    finally:
        connection.close()


def build_archive(source: Path, raw_db: Path, output: Path,
                  compresslevel: int = 6, workers: int = 8) -> dict:
    source = source.resolve()
    raw_db = raw_db.resolve()
    output = output.resolve()
    if not raw_db.is_file():
        raise FileNotFoundError(f"Raw ThermoML database not found: {raw_db}")

    temp = output.with_name(output.name + ".tmp")
    if temp.exists():
        temp.unlink()
    source_connection = sqlite3.connect(str(raw_db))
    target = sqlite3.connect(str(temp))
    try:
        target.execute("PRAGMA journal_mode=OFF")
        target.execute("PRAGMA synchronous=OFF")
        target.execute("PRAGMA temp_store=MEMORY")
        target.execute("PRAGMA page_size=65536")
        target.executescript(
            "CREATE TABLE documents ("
            "path TEXT PRIMARY KEY, doi TEXT NOT NULL UNIQUE, "
            "json_zlib BLOB NOT NULL, xml_zlib BLOB NOT NULL, "
            "json_size INTEGER NOT NULL, xml_size INTEGER NOT NULL, "
            "json_crc32 INTEGER NOT NULL, xml_crc32 INTEGER NOT NULL"
            ") WITHOUT ROWID;"
            "CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL) "
            "WITHOUT ROWID;"
        )
        expected_count = source_connection.execute(
            "SELECT COUNT(*) FROM papers"
        ).fetchone()[0]
        cursor = source_connection.execute(
            "SELECT doi, file_path, json_data FROM papers ORDER BY file_path"
        )
        processed = 0
        json_bytes_total = 0
        xml_bytes_total = 0
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=max(1, workers)
        ) as executor:
            while True:
                batch = cursor.fetchmany(max(16, workers * 4))
                if not batch:
                    break
                futures = [
                    executor.submit(_compress_record, row, source, compresslevel)
                    for row in batch
                ]
                rows = [future.result() for future in futures]
                target.executemany(
                    "INSERT INTO documents VALUES (?,?,?,?,?,?,?,?)", rows
                )
                target.commit()
                processed += len(rows)
                json_bytes_total += sum(row[4] for row in rows)
                xml_bytes_total += sum(row[5] for row in rows)
                if processed % 256 == 0 or processed == expected_count:
                    print(
                        f"Compressed {processed:,}/{expected_count:,}: {rows[-1][0]}",
                        flush=True,
                    )

        if processed != expected_count:
            raise RuntimeError(
                f"Source row count changed: expected {expected_count}, processed {processed}"
            )
        metadata = {
            "format": "thermoml-zlib-sqlite-v1",
            "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "json_documents": str(processed),
            "xml_documents": str(processed),
            "json_source_bytes": str(json_bytes_total),
            "xml_source_bytes": str(xml_bytes_total),
            "compression_level": str(compresslevel),
        }
        target.executemany(
            "INSERT INTO metadata(key, value) VALUES (?, ?)", metadata.items()
        )
        target.commit()
        target.execute("VACUUM")
        target.close()
        target = None

        _verify(temp, expected_count)
        os.replace(temp, output)
    except BaseException:
        if target is not None:
            target.close()
        if temp.exists():
            temp.unlink()
        raise
    finally:
        source_connection.close()

    return {
        "output": str(output),
        "documents": expected_count,
        "archive_bytes": output.stat().st_size,
        "format": "thermoml-zlib-sqlite-v1",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--raw-db", type=Path, default=DEFAULT_RAW_DB)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--compresslevel", type=int, default=6, choices=range(1, 10))
    parser.add_argument("--workers", type=int, default=min(12, os.cpu_count() or 4))
    args = parser.parse_args()
    result = build_archive(
        args.source, args.raw_db, args.output,
        compresslevel=args.compresslevel, workers=args.workers,
    )
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
