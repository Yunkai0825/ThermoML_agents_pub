"""Location helpers for the archived ThermoML query benchmarks."""

from __future__ import annotations

from pathlib import Path


ARCHIVE_DIR_NAME = "ThermoML_20260802_batch"


def find_archive_root(source: str | Path) -> Path:
    """Return the enclosing archived batch without relying on nesting depth."""

    resolved = Path(source).resolve()
    for candidate in (resolved, *resolved.parents):
        if candidate.name == ARCHIVE_DIR_NAME:
            return candidate
    raise RuntimeError(
        f"Cannot locate enclosing {ARCHIVE_DIR_NAME!r} from {resolved}"
    )


def find_workspace_root(source: str | Path) -> Path:
    """Return the workspace containing the live ThermoML source checkout."""

    archive_root = find_archive_root(source)
    for candidate in archive_root.parents:
        if (candidate / "ThermoML_research_agent").is_dir():
            return candidate
    raise RuntimeError(
        "Cannot locate the workspace containing ThermoML_research_agent "
        f"from {archive_root}"
    )
