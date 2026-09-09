"""Random-access reader for the single compressed ThermoML JSON/XML corpus.

Each paper is one row in an indexed SQLite container. JSON and XML payloads
are independently zlib-compressed, so the browser can retrieve one source
document without unpacking the corpus or depending on extracted DOI folders.
"""

from __future__ import annotations

import json
import sqlite3
import threading
import zlib
from pathlib import Path, PurePosixPath
from typing import Any

from .sqlite_readonly import connect_readonly


DATA_ROOT = Path(__file__).absolute().parents[2] / "ThermoML_research_agent" / "ThermoML.v2020-09-30.db"
ARCHIVE_PATH = DATA_ROOT / "thermoml_raw_corpus.db"

_local = threading.local()


def _member_name(file_path: str) -> str:
    """Normalize and validate a corpus member path."""
    normalized = str(file_path).replace("\\", "/").lstrip("/")
    member = PurePosixPath(normalized)
    if not normalized or member.is_absolute() or ".." in member.parts:
        raise ValueError(f"Unsafe ThermoML corpus path: {file_path!r}")
    return member.as_posix()


def _connection() -> sqlite3.Connection:
    try:
        stat = ARCHIVE_PATH.stat()
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            f"Compressed ThermoML corpus not found: {ARCHIVE_PATH}. "
            "Run build_raw_corpus_archive.py before starting the browser."
        ) from exc
    signature = (stat.st_mtime_ns, stat.st_size)
    connection = getattr(_local, "connection", None)
    if connection is None or getattr(_local, "signature", None) != signature:
        if connection is not None:
            connection.close()
        connection = connect_readonly(ARCHIVE_PATH)
        _local.connection = connection
        _local.signature = signature
    return connection


def read_bytes(file_path: str) -> bytes:
    """Read one JSON or XML document from the indexed compressed container."""
    member = _member_name(file_path)
    suffix = PurePosixPath(member).suffix.lower()
    if suffix not in {".json", ".xml"}:
        raise ValueError(f"Unsupported ThermoML source type: {file_path!r}")
    json_path = str(PurePosixPath(member).with_suffix(".json"))
    column = "json_zlib" if suffix == ".json" else "xml_zlib"
    row = _connection().execute(
        f"SELECT {column} AS payload FROM documents WHERE path = ?",
        (json_path,),
    ).fetchone()
    if row is None:
        raise FileNotFoundError(f"ThermoML corpus member not found: {member}")
    try:
        return zlib.decompress(row["payload"])
    except zlib.error as exc:
        raise OSError(f"Corrupt compressed ThermoML member: {member}") from exc


def read_text(file_path: str) -> str:
    """Read one UTF-8 source document from the compressed container."""
    return read_bytes(file_path).decode("utf-8-sig", errors="replace")


def read_json(file_path: str) -> Any:
    """Load one parsed ThermoML JSON document from the container."""
    return json.loads(read_text(file_path))


def archive_status() -> dict:
    """Return container metadata for diagnostics and tests."""
    connection = _connection()
    metadata = {
        row["key"]: row["value"]
        for row in connection.execute("SELECT key, value FROM metadata")
    }
    return {
        "path": str(ARCHIVE_PATH),
        "size_bytes": ARCHIVE_PATH.stat().st_size,
        "json_documents": int(metadata.get("json_documents", 0)),
        "xml_documents": int(metadata.get("xml_documents", 0)),
        "format": metadata.get("format", ""),
    }
