"""SQLite helpers for read-only database mounts."""

from __future__ import annotations

import sqlite3
from os import PathLike, fspath, path as os_path
from urllib.parse import quote


def readonly_uri(path: str | PathLike[str]) -> str:
    """Return a SQLite URI for an immutable read-only database file."""
    absolute = os_path.abspath(fspath(path)).replace("\\", "/")
    if absolute.startswith("//"):
        return f"file://{quote(absolute, safe='/:')}?mode=ro&immutable=1"
    return f"file:{quote(absolute, safe='/:')}?mode=ro&immutable=1"


def connect_readonly(path: str | PathLike[str]) -> sqlite3.Connection:
    """Open a SQLite database without requiring write access to the mount."""
    connection = sqlite3.connect(readonly_uri(path), uri=True)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA query_only=ON")
    return connection
