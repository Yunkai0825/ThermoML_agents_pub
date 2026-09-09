"""
ID resolution workers — thin wrappers around the existing fuzzy resolvers.

Each worker resolves one entity type and returns canonical global IDs
that the index DB can filter on.  Workers only import the resolver
they need and return minimal payloads (global_id + score + match_type).

All workers share the same interface:

    resolve_XYZ(query: str, limit: int = 5) -> list[ResolvedID]
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass

# Ensure card_db_search_tools is importable
_WORKSPACE = os.path.normpath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..', 'ThermoML_research_agent')
)
if _WORKSPACE not in sys.path:
    sys.path.insert(0, _WORKSPACE)

from card_db_search_tools.basic_search_tools._id_alignment_search import (
    resolve_ids,
)
from ThermoML_raw_json_to_card_db_parsers.id_schema import require_global_id


@dataclass
class ResolvedID:
    """Minimal resolved canonical ID."""
    entity_type: str
    global_id: str
    canonical_id: str   # e.g. "mass_density_kg_m3"
    display_name: str   # e.g. "Mass density, kg/m3"
    score: int          # 0–100
    match_type: str     # "exact", "alias", "fuzzy", "global_id", ...

    def to_dict(self) -> dict:
        return {
            'entity_type': self.entity_type,
            'global_id': self.global_id,
            'canonical_id': self.canonical_id,
            'display_name': self.display_name,
            'score': self.score,
            'match_type': self.match_type,
        }


# ── Column name maps per entity type ──────────────────────────────────────

_ENTITY_COLS = {
    "compound":    ("comp_num_id",   "comp_id",    "common_name"),
    "property":    ("prop_num_id",   "prop_id",    "prop_name"),
    "measurement": ("meas_num_id",   "meas_id",    "method_name"),
    "variable":    ("var_num_id",    "var_id",     "var_name"),
    "constraint":  ("constr_num_id", "constr_id",  "constr_name"),
    "phase":       ("phase_num_id",  "phase_id",   "phase_name"),
    "reference":   ("lit_num_id",    "doi",        "doi"),
    "solvent":     ("solvent_num_id","comp_num_id", "common_name"),
}


def _resolve(entity_type: str, query: str, limit: int = 5,
             min_score: int = 40) -> list[ResolvedID]:
    """Generic resolver — delegates to the cross-registry resolver."""
    try:
        id_col, canon_col, name_col = _ENTITY_COLS[entity_type]
    except KeyError as exc:
        raise ValueError(f"Unsupported entity_type: {entity_type!r}") from exc
    if not isinstance(query, str) or not query:
        raise TypeError("query must be a non-empty string")
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise TypeError("limit must be a positive integer")
    if isinstance(min_score, bool) or not isinstance(min_score, int) or not 0 <= min_score <= 100:
        raise TypeError("min_score must be an integer from 0 through 100")
    hits = resolve_ids(entity_type, query, min_score=min_score, limit=limit)
    results = []
    for index, h in enumerate(hits):
        if not isinstance(h, dict):
            raise TypeError(f"resolver result[{index}] must be an object")
        missing = {id_col, canon_col, name_col, "score", "match_type"} - h.keys()
        if missing:
            raise ValueError(f"resolver result[{index}] is missing {sorted(missing)}")
        score = h["score"]
        if isinstance(score, bool) or not isinstance(score, int) or not 0 <= score <= 100:
            raise TypeError(f"resolver result[{index}].score must be an integer from 0 through 100")
        if not isinstance(h["match_type"], str) or not h["match_type"]:
            raise TypeError(f"resolver result[{index}].match_type must be a non-empty string")
        results.append(ResolvedID(
            entity_type=entity_type,
            global_id=require_global_id(id_col, h[id_col]),
            canonical_id=h[canon_col],
            display_name=h[name_col],
            score=score,
            match_type=h["match_type"],
        ))
    return results


# ── Public convenience functions ──────────────────────────────────────────

def resolve_compound(query: str, limit: int = 5) -> list[ResolvedID]:
    return _resolve("compound", query, limit=limit)


def resolve_property(query: str, limit: int = 5) -> list[ResolvedID]:
    return _resolve("property", query, limit=limit)


def resolve_measurement(query: str, limit: int = 5) -> list[ResolvedID]:
    return _resolve("measurement", query, limit=limit)


def resolve_variable(query: str, limit: int = 5) -> list[ResolvedID]:
    return _resolve("variable", query, limit=limit)


def resolve_constraint(query: str, limit: int = 5) -> list[ResolvedID]:
    return _resolve("constraint", query, limit=limit)


def resolve_phase(query: str, limit: int = 5) -> list[ResolvedID]:
    return _resolve("phase", query, limit=limit)


def resolve_reference(query: str, limit: int = 10) -> list[ResolvedID]:
    return _resolve("reference", query, limit=limit, min_score=30)


def resolve_solvent(query: str, limit: int = 5) -> list[ResolvedID]:
    return _resolve("solvent", query, limit=limit)
