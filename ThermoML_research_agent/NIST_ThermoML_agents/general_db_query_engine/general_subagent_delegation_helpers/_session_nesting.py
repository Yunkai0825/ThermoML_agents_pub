"""
Session-nesting helper for subagent delegation.
================================================
Creates nested subdirectories inside a parent agent's active session
so that each subagent run's output (stats, history, reasoning) is
co-located with the parent's output.

The caller injects a ``get_session`` callable (from its own
hook_catalog) so this module never imports agent-specific code.
"""
from __future__ import annotations

import logging
import threading
from contextlib import contextmanager
from pathlib import Path
from typing import Callable, Dict, Iterator, Optional

from ..general_hooks_management_helpers.general_memory_management_tools_hooks_helpers import (
    session_manager_output_storage as _session_storage,
)
from ..general_hooks_management_helpers.general_memory_management_tools_hooks_helpers.session_manager_output_storage import (
    ensure_directory,
)

log = logging.getLogger(__name__)


@contextmanager
def preserve_active_session() -> Iterator[Optional[object]]:
    """Restore the caller's active session after a nested agent run.

    Nested orchestrators activate their own session in the shared execution
    context; without this guard, post-run bookkeeping (tracking merges,
    manifest writes) would resolve the CHILD session as the parent.
    """
    previous = _session_storage.get_session()
    try:
        yield previous
    finally:
        _session_storage.set_active_session(previous)


class SubagentSessionManager:
    """Thread-safe session-nesting manager.

    Parameters
    ----------
    get_session : callable
        Zero-arg callable that returns the parent agent's active
        ``SessionManager`` instance (or ``None``).  Typically
        ``hook_catalog.session_manager.get_session``.
    """

    def __init__(self, get_session: Callable[[], Optional[object]]) -> None:
        self._get_session = get_session
        self._counters: Dict[str, int] = {}
        self._lock = threading.Lock()

    def _next_run_id(self, agent_type: str) -> int:
        with self._lock:
            self._counters[agent_type] = self._counters.get(agent_type, 0) + 1
            return self._counters[agent_type]

    def get_subagent_session_dir(self, agent_type: str) -> Path:
        """Create and return a nested subfolder for *agent_type*.

        Layout::

            <parent_session_dir>/<agent_type>_runs/run_<N>/

        A delegation call without an active parent session is rejected. This
        keeps subagent artifacts and tool history durably nested rather than
        silently running an untracked subagent.
        """
        if agent_type not in {"query", "analysis"}:
            raise ValueError(f"unsupported subagent type: {agent_type!r}")
        sess = self._get_session()
        if sess is None or not hasattr(sess, "session_dir") or sess.session_dir is None:
            raise RuntimeError("subagent delegation requires an active parent session")
        run_id = self._next_run_id(agent_type)
        subdir = Path(sess.session_dir) / f"{agent_type}_runs" / f"run_{run_id}"
        ensure_directory(subdir, exist_ok=False)
        return subdir

    def get_parent_session_dir(self) -> Path:
        """Return the mandatory active parent-agent session directory."""
        sess = self._get_session()
        if sess is None or not hasattr(sess, "session_dir") or sess.session_dir is None:
            raise RuntimeError("subagent tracking merge requires an active parent session")
        return Path(sess.session_dir)
