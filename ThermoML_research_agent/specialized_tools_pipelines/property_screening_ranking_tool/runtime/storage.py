"""Centralized runtime paths and source fingerprints."""

from __future__ import annotations

import hashlib
import json
import os
import time
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator


_OUTPUT_ROOT = Path(__file__).resolve().parents[4] / "_output" / "Query"

from ..tool_settings import (
    CACHE_LOCK_TIMEOUT_SECONDS,
    runtime_settings_snapshot,
)
from ..unit_conversion_lib import unit_translation_table_sha256

from card_db_search_tools.basic_search_tools.advanced_block_search.catalogs import (  # noqa: E402
    PCS_DB,
    PM_REGISTRY_DB,
    RAW_DB,
    load_runtime_catalogs,
)


def property_screening_cache_root() -> Path:
    """Return the local cache outside the source package."""
    root = _OUTPUT_ROOT / "_cache" / "property_screening"
    root.mkdir(parents=True, exist_ok=True)
    return root


def _temporary_runs_root() -> Path:
    return _OUTPUT_ROOT / "property_screening_runs"


def _active_session() -> Any:
    try:
        from NIST_ThermoML_agents.general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers.session_manager_output_storage import (
            get_session,
        )
    except ImportError:
        return None
    return get_session()


def register_session_file(
    category: str, path: Path, description: str
) -> bool:
    """Register a completed artifact with the active agent session."""
    session = _active_session()
    if session is None:
        return False
    session.register_file(category, path, description)
    return True

def new_run_directory() -> tuple[Path, Any]:
    """Create a unique run directory in the active session or Query temp."""
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    run_id = f"screen_{stamp}_{uuid.uuid4().hex[:8]}"
    session = _active_session()
    root = (
        session.data_dir / "property_screening"
        if session is not None
        else _temporary_runs_root()
    )
    run_dir = root / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    return run_dir, session


def _file_signature(path: Path) -> dict[str, Any]:
    stat = path.stat()
    return {
        "path": str(path),
        "size": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
    }


def database_fingerprint() -> dict[str, Any]:
    """Fingerprint every database/catalog input affecting pipeline semantics."""
    catalogs = load_runtime_catalogs()
    payload = {
        "PCS_INDIV": _file_signature(PCS_DB),
        "PureOrMixtureData_registry": _file_signature(PM_REGISTRY_DB),
        "thermoml_raw": _file_signature(RAW_DB),
        "translation_filename": catalogs.translation_filename,
        "translation_sha256": catalogs.translation_sha256,
        "pcs_build_time": catalogs.pcs_build_time,
        "tool_settings": runtime_settings_snapshot(),
        "unit_translation_table_sha256": (
            unit_translation_table_sha256()
        ),
    }
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    ).encode()
    payload["fingerprint_sha256"] = hashlib.sha256(encoded).hexdigest()
    return payload


class JsonContentCache:
    """Independent cache namespace for one deterministic pipeline branch."""

    def __init__(self, namespace: str) -> None:
        if not namespace or Path(namespace).name != namespace:
            raise ValueError("cache namespace must be one safe path segment")
        self.namespace = namespace
        self.root = property_screening_cache_root() / namespace
        self.root.mkdir(parents=True, exist_ok=True)

    def key(self, payload: dict[str, Any]) -> str:
        encoded = json.dumps(
            payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
        ).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    def read(self, key: str) -> dict[str, Any] | None:
        path = self._path(key)
        if not path.is_file():
            return None
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
        if not isinstance(value, dict):
            raise TypeError(f"cache entry {path} is not a JSON object")
        return value

    def write(self, key: str, value: dict[str, Any]) -> Path:
        path = self._path(key)
        with self._lock(key):
            if path.is_file():
                return path
            temp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
            with temp.open("x", encoding="utf-8") as handle:
                json.dump(
                    value,
                    handle,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                )
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temp, path)
        return path

    def get_or_compute(
        self,
        payload: dict[str, Any],
        compute,
    ) -> tuple[dict[str, Any], bool, str]:
        key = self.key(payload)
        cached = self.read(key)
        if cached is not None:
            return cached, True, key
        value = compute()
        if not isinstance(value, dict):
            raise TypeError("cache computation must return a JSON object")
        self.write(key, value)
        return value, False, key

    def _path(self, key: str) -> Path:
        if len(key) != 64 or any(ch not in "0123456789abcdef" for ch in key):
            raise ValueError("cache key must be a lowercase SHA-256 digest")
        return self.root / f"{key}.json"

    @contextmanager
    def _lock(
        self,
        key: str,
        timeout: float = CACHE_LOCK_TIMEOUT_SECONDS,
    ) -> Iterator[None]:
        lock = self.root / f"{key}.lock"
        deadline = time.monotonic() + timeout
        descriptor: int | None = None
        while descriptor is None:
            try:
                descriptor = os.open(
                    lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY
                )
            except FileExistsError:
                if time.monotonic() >= deadline:
                    raise TimeoutError(f"timed out waiting for cache lock {lock}")
                time.sleep(0.05)
        try:
            os.write(descriptor, str(os.getpid()).encode("ascii"))
            os.close(descriptor)
            descriptor = None
            yield
        finally:
            if descriptor is not None:
                os.close(descriptor)
            lock.unlink(missing_ok=True)
