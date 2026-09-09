"""
virtual_block_registry — session-scoped store for agent-built data blocks.
===========================================================================
When the ThermoML DB has no usable data, the analysis agent may register a
self-built block under a pseudo-DOI in
the ``agentblock/<label>`` namespace.  ``extract_block_arrays()`` checks
this registry BEFORE the real DB, so every downstream deterministic tool
(inspect_block, get_pure_values, fit_block, propose_fitting_plan) works
on virtual blocks unchanged.

Design rules
------------
- **Pure storage.**  No LLM, no imports from ``block_data_io`` (import
  cycle) — entries are stored in the exact dict shape returned by
  ``extract_block_csv()``.
- **Session-isolated and thread-safe.**  Entries are partitioned by the
  active output-session ID. ``fit_multi_system`` propagates that context into
  worker threads, so parallel runs cannot read or overwrite each other.
- **Collision-proof within a session.**  Labels are auto-suffixed when taken.
  Callers MUST use the pseudo-DOI returned by ``register_virtual_block``.
- **Provenance.**  Every entry carries ``metadata["source"]="agent_built"``
  plus the agent's ``basis`` (justification) and ``citations`` (real DOIs
  the numbers are based on).  An audit copy (CSV + JSON) is written to
  the active session's ``data/`` dir when a session exists.

The fallback-only policy (refuse when real DB data exists) is enforced by
the ``register_custom_block`` tool — NOT here.  This module is plain
storage so tests and future tools can manage entries directly.
"""

from __future__ import annotations

import datetime as _dt
import json
import logging
import re
import threading
from typing import Any, Dict, List, Optional

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_block_id,
    require_global_id,
)

log = logging.getLogger("VIRTUAL-BLOCK-REGISTRY")

#: Pseudo-DOI namespace.  Deliberately contains no ``:`` or ``.`` so that
#: ``_safe_doi_slug()`` (replaces only ``/`` and ``.``) yields a valid
#: filename on Windows, and no real DOI (``10.xxxx/...``) can collide.
VIRTUAL_DOI_PREFIX = "agentblock/"

#: Virtual property blocks use the same typed block grammar as database cards.
VIRTUAL_BLOCK_NUMBER = "PROPblock_1"

_LABEL_RE = re.compile(r"[^a-z0-9_\-]+")

# ── Store ────────────────────────────────────────────────────────────
_registry: Dict[str, Dict[str, Dict[str, Any]]] = {}
# session_id → pseudo_doi → entry dict
_lock = threading.Lock()


# ---------------------------------------------------------------------
#  Helpers
# ---------------------------------------------------------------------

def is_virtual(doi: str) -> bool:
    """True if *doi* addresses the virtual-block namespace."""
    return isinstance(doi, str) and doi.startswith(VIRTUAL_DOI_PREFIX)


def sanitize_label(label: str) -> str:
    """Lower-case, replace unsafe chars with ``_``, cap at 24 chars."""
    slug = _LABEL_RE.sub("_", str(label).strip().lower()).strip("_")
    return (slug or "block")[:24]


def _require_block_number(block_number: str) -> str:
    return require_block_id(block_number)


def _require_active_session():
    from ...analysis_agent_context_hooks.memory_hooks import get_session

    session = get_session()
    if session is None:
        raise RuntimeError(
            "VIRTUAL_BLOCK_SESSION_REQUIRED: initialize an analysis output "
            "session before registering or reading agent-built blocks"
        )
    return session


def _source_identity(metadata: Dict[str, Any]) -> Dict[str, Any]:
    """Validate and normalize the literature provenance of a virtual block.

    ``agentblock/...`` is a session-scoped computational address, not a DOI and
    therefore has no canonical literature ID of its own.  The first structured
    citation is the primary source anchor used by existing single-identity tool
    contracts; all cited literature IDs remain available in
    ``source_lit_num_ids`` so multi-source blocks do not lose provenance.
    """
    citations = metadata.get("citations", [])
    if not isinstance(citations, list):
        raise ValueError("VIRTUAL_BLOCK_CITATIONS_INVALID: citations must be a list")

    normalized: list[dict[str, str]] = []
    source_lit_num_ids: list[str] = []
    for index, citation in enumerate(citations):
        if not isinstance(citation, dict):
            raise ValueError(
                "VIRTUAL_BLOCK_CITATION_INVALID: "
                f"citations[{index}] must contain doi and lit_num_id"
            )
        doi = citation.get("doi")
        if not isinstance(doi, str) or not doi.strip():
            raise ValueError(
                f"VIRTUAL_BLOCK_CITATION_INVALID: citations[{index}].doi is required"
            )
        lit_num_id = require_global_id("lit_num_id", citation.get("lit_num_id"))
        normalized.append({"doi": doi.strip(), "lit_num_id": lit_num_id})
        if lit_num_id not in source_lit_num_ids:
            source_lit_num_ids.append(lit_num_id)

    return {
        "citations": normalized,
        "lit_num_id": source_lit_num_ids[0] if source_lit_num_ids else None,
        "source_lit_num_ids": source_lit_num_ids,
        "identity_scope": "agent_built_with_literature_provenance",
    }


# ---------------------------------------------------------------------
#  Registration
# ---------------------------------------------------------------------

def register_virtual_block(
    label: str,
    csv_text: str,
    columns: List[str],
    n_rows: int,
    metadata: Dict[str, Any],
) -> str:
    """Store an agent-built block; return its unique pseudo-DOI.

    The stored entry mimics the ``extract_block_csv()`` result shape so
    ``extract_block_arrays()`` can serve it verbatim.  If *label* is
    already taken, a numeric suffix is appended (``_2``, ``_3``, …) —
    the caller must use the returned pseudo-DOI.
    """
    base = sanitize_label(label)
    now = _dt.datetime.now().isoformat(timespec="seconds")
    session = _require_active_session()
    session_id = session.session_id

    with _lock:
        session_registry = _registry.setdefault(session_id, {})
        slug, n = base, 1
        while f"{VIRTUAL_DOI_PREFIX}{slug}" in session_registry:
            n += 1
            slug = f"{base}_{n}"
        pseudo_doi = f"{VIRTUAL_DOI_PREFIX}{slug}"

        meta = dict(metadata)
        meta.update(_source_identity(meta))
        meta["doi"] = pseudo_doi
        meta["block_number"] = VIRTUAL_BLOCK_NUMBER
        meta.setdefault("source", "agent_built")
        meta.setdefault("registered_at", now)

        session_registry[pseudo_doi] = {
            "csv_text": csv_text,
            "columns": list(columns),
            "n_rows": int(n_rows),
            "metadata": meta,
            "error": None,
        }

    log.info("registered virtual block %s (%d rows)", pseudo_doi, n_rows)
    _audit_dump(pseudo_doi)
    return pseudo_doi


def remove_virtual_block(pseudo_doi: str) -> bool:
    """Delete an entry (used when post-registration validation fails)."""
    session_id = _require_active_session().session_id
    with _lock:
        return _registry.get(session_id, {}).pop(pseudo_doi, None) is not None


def clear_registry() -> None:
    """Remove all virtual blocks owned by the active session."""
    session_id = _require_active_session().session_id
    with _lock:
        _registry.pop(session_id, None)


# ---------------------------------------------------------------------
#  Lookup (called by extract_block_arrays)
# ---------------------------------------------------------------------

def lookup(doi: str, block_number: str) -> Dict[str, Any]:
    """Return the stored block in ``extract_block_csv()`` result shape.

    Unknown pseudo-DOI / block_number → error-shaped dict (never raises),
    matching the real extractor's contract.
    """
    session_id = _require_active_session().session_id
    with _lock:
        session_registry = _registry.get(session_id, {})
        entry = session_registry.get(doi)
        known_dois = sorted(session_registry)

    if entry is None:
        known = ", ".join(known_dois) or "none registered"
        return {
            "error": (
                f"Virtual block '{doi}' not found in the agent-built block "
                f"registry (known: {known}). Register it first with "
                f"register_custom_block."
            ),
            "csv_text": "", "columns": [], "n_rows": 0, "metadata": {},
        }

    bn = _require_block_number(block_number)
    if bn != VIRTUAL_BLOCK_NUMBER:
        return {
            "error": (
                f"Block '{bn}' not found in virtual DOI '{doi}'. "
                f"Agent-built blocks always use '{VIRTUAL_BLOCK_NUMBER}'."
            ),
            "csv_text": "", "columns": [], "n_rows": 0, "metadata": {},
        }

    # Shallow copy so callers cannot mutate the stored entry.
    return {
        "csv_text": entry["csv_text"],
        "columns": list(entry["columns"]),
        "n_rows": entry["n_rows"],
        "metadata": dict(entry["metadata"]),
        "error": None,
    }


def list_virtual_blocks() -> List[Dict[str, Any]]:
    """Summaries of virtual blocks owned by the active session."""
    session_id = _require_active_session().session_id
    with _lock:
        return [
            {
                "pseudo_doi": doi,
                "n_rows": e["n_rows"],
                "columns": list(e["columns"]),
                "basis": e["metadata"].get("basis", ""),
                "citations": e["metadata"].get("citations", []),
                "registered_at": e["metadata"].get("registered_at", ""),
            }
            for doi, e in _registry.get(session_id, {}).items()
        ]


# ---------------------------------------------------------------------
#  Session audit dump  (best-effort, never raises)
# ---------------------------------------------------------------------

def _audit_dump(pseudo_doi: str) -> None:
    """Write CSV + metadata JSON of a registered block to the active
    session's data/ dir so agent-built data is fully auditable."""
    try:
        # Lazy import — memory_hooks transitively belongs to the agent
        # layer; importing here (not at module load) avoids any cycle.
        from ...analysis_agent_context_hooks.memory_hooks import get_session
        sess = get_session()
        if not sess:
            return
        with _lock:
            entry = _registry.get(sess.session_id, {}).get(pseudo_doi)
        if not entry:
            return
        slug = pseudo_doi.replace("/", "_")
        csv_path = str(sess.data_path(f"{slug}_registered.csv"))
        with open(csv_path, "w", encoding="utf-8", newline="") as fh:
            fh.write(entry["csv_text"])
        sess.register_file(
            "data", csv_path,
            f"AGENT-BUILT virtual block {pseudo_doi} (raw CSV as registered)",
        )
        meta_path = str(sess.data_path(f"{slug}_metadata.json"))
        with open(meta_path, "w", encoding="utf-8") as fh:
            json.dump(entry["metadata"], fh, indent=2, default=str)
        sess.register_file(
            "data", meta_path,
            f"AGENT-BUILT virtual block {pseudo_doi} (provenance metadata)",
        )
    except Exception as exc:  # pragma: no cover — audit must never break runs
        log.warning("virtual block audit dump failed: %s", exc)
