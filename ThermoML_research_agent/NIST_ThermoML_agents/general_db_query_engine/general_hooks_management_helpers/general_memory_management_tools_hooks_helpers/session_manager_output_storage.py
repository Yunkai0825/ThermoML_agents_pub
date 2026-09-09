"""
Session Manager — directory structure & file catalog for analysis runs.
=======================================================================
Provides a context-local session so that fitting tools can register
output files (CSVs, plots) without passing paths through every call chain.
The context propagates through async child tasks and through worker pools when
the caller submits a copied context.

Usage from orchestrator.py:
    from ..memory_hooks import session_manager
    session_manager.init_session(cfg.OUTPUT_DIR, question)

Usage from fitting_tools.py:
    from ..memory_hooks.session_manager import get_session
    sess = get_session()
    if sess:
        csv_path = sess.data_path("fit_PROPblock_10.1234_B3.csv")
"""

from __future__ import annotations

import datetime as dt
import json
import logging
import os
import uuid
from contextvars import ContextVar
from pathlib import Path
from typing import Dict, List, Optional

log = logging.getLogger("SESSION-MGR")

_active_session: ContextVar[Optional["SessionManager"]] = ContextVar(
    "thermoml_active_output_session", default=None
)


def _filesystem_path(path: Path) -> Path:
    """Return a Win32 extended-length path when the ordinary path is long."""
    if os.name != "nt":
        return path
    text = str(path)
    if text.startswith("\\\\?\\") or len(text) < 240:
        return path
    if text.startswith("\\\\"):
        return Path("\\\\?\\UNC\\" + text[2:])
    return Path("\\\\?\\" + text)


def _logical_path(path: Path | str) -> Path:
    """Strip a Win32 extended-length prefix for identity and catalog checks."""
    text = str(path)
    if text.startswith("\\\\?\\UNC\\"):
        return Path("\\\\" + text[8:])
    if text.startswith("\\\\?\\"):
        return Path(text[4:])
    return Path(text)


def ensure_directory(
    path: Path | str,
    *,
    parents: bool = True,
    exist_ok: bool = True,
) -> Path:
    """Create *path* using Win32 extended-path syntax when required.

    The returned path remains the ordinary logical path so it is suitable for
    JSON, markdown links, browser display, and downstream APIs.  Only the
    filesystem operation receives the Win32 extended-length representation.
    """
    logical_path = Path(path)
    _filesystem_path(logical_path).mkdir(parents=parents, exist_ok=exist_ok)
    return logical_path


class SessionManager:
    """Manages a single analysis-run output directory.

    Layout::
        _output/run_{ts}_{slug}/
            data/       ← CSVs (fit data, excess, baseline)
            plots/      ← PNGs (fit curves, residual plots)
            result.md
            history.md
    """

    def __init__(self, base_dir: Path, question: str):
        ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        self.session_id = f"run_{ts}_{uuid.uuid4().hex[:8]}"
        self.question = question
        self.session_dir = Path(base_dir) / self.session_id
        self.data_dir = self.session_dir / "data"
        self.plots_dir = self.session_dir / "plots"
        self.catalog_path = self.session_dir / "_session_catalog.json"
        self._catalog: List[Dict[str, str]] = []

    def ensure_dirs(self):
        """Create session directories on disk."""
        ensure_directory(self.session_dir)
        ensure_directory(self.data_dir)
        ensure_directory(self.plots_dir)

    # ── Path helpers ─────────────────────────────────────────

    def data_path(self, filename: str) -> Path:
        """Return a path inside data/ (creates dir if needed)."""
        if Path(filename).name != filename or filename in {"", ".", ".."}:
            raise ValueError("data filename must be a non-empty leaf name")
        ensure_directory(self.data_dir)
        return _filesystem_path(self.data_dir / filename)

    def plot_path(self, filename: str) -> Path:
        """Return a path inside plots/ (creates dir if needed)."""
        if Path(filename).name != filename or filename in {"", ".", ".."}:
            raise ValueError("plot filename must be a non-empty leaf name")
        ensure_directory(self.plots_dir)
        return _filesystem_path(self.plots_dir / filename)

    # ── File catalog ─────────────────────────────────────────

    def register_file(
        self,
        category: str,
        path: Path | str,
        description: str = "",
    ):
        """Register an output file in the session catalog (deduplicates by path)."""
        candidate = _logical_path(_logical_path(path).resolve())
        root = _logical_path(_logical_path(self.session_dir).resolve())
        try:
            candidate.relative_to(root)
        except ValueError as exc:
            raise ValueError("registered files must be inside the active session") from exc
        path_str = str(candidate)
        if any(e["path"] == path_str for e in self._catalog):
            return
        self._catalog.append({
            "category": category,
            "path": path_str,
            "description": description,
        })
        _filesystem_path(self.catalog_path).write_text(
            json.dumps(self._catalog, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        log.info("Registered %s: %s", category, path)

    def list_files(self) -> List[Dict[str, str]]:
        """Return all registered files grouped by category."""
        return list(self._catalog)

    def render_manifest(self, *, root_dir: str | None = None) -> str:
        """Render the file catalog as a markdown manifest.

        Parameters
        ----------
        root_dir : str, optional
            If provided, file paths are shown relative to this root.
        """
        if not self._catalog:
            return ""
        lines = ["## Session Output Files", ""]
        by_cat: Dict[str, list] = {}
        for entry in self._catalog:
            by_cat.setdefault(entry["category"], []).append(entry)
        for cat, files in by_cat.items():
            lines.append(f"### {cat}")
            for f in files:
                fpath = f["path"]
                if root_dir and fpath.startswith(root_dir):
                    fpath = "$ROOT/" + fpath[len(root_dir):].lstrip("\\/")
                desc = f" — {f['description']}" if f["description"] else ""
                lines.append(f"- `{fpath}`{desc}")
            lines.append("")
        return "\n".join(lines)


# ── Module-level API ─────────────────────────────────────────

def init_session(base_dir: Path, question: str) -> SessionManager:
    """Create and activate a new session.  Call once per run().

    Each logical run gets a unique context-local session and directory.
    """
    mgr = SessionManager(base_dir, question)
    mgr.ensure_dirs()
    _active_session.set(mgr)
    log.info("Session initialized: %s", mgr.session_dir)
    return mgr


def get_session() -> Optional[SessionManager]:
    """Return the active session for this execution context, or None."""
    return _active_session.get()


def set_active_session(mgr: Optional[SessionManager]) -> Optional[SessionManager]:
    """Rebind the active session and return the previously active one.

    Nested agent runs activate their own session; callers use the returned
    previous session to restore their context afterwards.
    """
    previous = _active_session.get()
    _active_session.set(mgr)
    return previous


def reopen_session(session_dir: Path) -> SessionManager:
    """Reopen an existing session directory for a continuation round.

    Unlike ``init_session`` this does NOT create a new timestamped
    subdirectory — it reuses *session_dir* as-is.
    """
    session_dir = Path(session_dir)
    mgr = object.__new__(SessionManager)
    mgr.session_id = session_dir.name
    mgr.question = ""
    mgr.session_dir = session_dir
    mgr.data_dir = session_dir / "data"
    mgr.plots_dir = session_dir / "plots"
    mgr.catalog_path = session_dir / "_session_catalog.json"
    catalog_fs_path = _filesystem_path(mgr.catalog_path)
    if catalog_fs_path.exists():
        loaded = json.loads(catalog_fs_path.read_text(encoding="utf-8"))
        if not isinstance(loaded, list) or not all(isinstance(item, dict) for item in loaded):
            raise ValueError("session catalog must be a JSON array of objects")
        mgr._catalog = loaded
    else:
        mgr._catalog = []
    mgr.ensure_dirs()
    _active_session.set(mgr)
    log.info("Session reopened: %s", session_dir)
    return mgr


def close_session():
    """Clear the active session for this execution context."""
    _active_session.set(None)
