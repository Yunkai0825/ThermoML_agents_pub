"""
Cross-registry ID alignment tool.

Central hub for **all** ID resolution and card-level compaction across
ThermoML search tools.

Handles:
  - Free-text queries (name, formula, SMILES, InChI, DOI, etc.)
  - Strict prefixed global IDs (e.g. ``GLOBcomp_3``, ``GLOBprop_1``)
  - Multi-value inputs (native string arrays)
  - All entity types: compound, property, measurement, variable,
    constraint, phase, reference, solvent, block_type, reaction_type
  - Card-level markdown rendering via compactors

Public API — ID resolution
--------------------------
search_id_alignment(entity_type, query, limit=20) -> dict
resolve_ids(entity_type, queries, min_score, limit) -> list[dict]

Convenience resolvers (for search tools):
    resolve_compound_ids, resolve_property_ids, resolve_measurement_ids,
    resolve_reference_ids, resolve_phase_ids, resolve_variable_ids,
    resolve_constraint_ids, resolve_solvent_ids

Public API — Card compaction (ID → markdown)
---------------------------------------------
resolve_card_md(card_type, doi=..., lit_num_id=..., ...) -> str
    Fetch a card from the DB by ID and return compact markdown.
"""

import csv
import logging
import sys
import os

log = logging.getLogger("id-alignment-search")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normalization_helpers import (
    resolve_compound,
    resolve_property,
    resolve_measurement,
    resolve_reference,
    resolve_variable,
    resolve_constraint,
    resolve_phase,
    resolve_solvent,
    resolve_block_type,
    resolve_reaction_type,
)
from normalization_helpers.paths import csv_path
from normalization_helpers.strict_id_inputs import (
    GLOBAL_FIELD_BY_ENTITY,
    IdentifierRefinementError,
    require_global_tool_id,
    require_typed_block_input,
    SearchValue,
    validate_search_values,
)
from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_block_local_id,
    require_global_id,
)

# ═════════════════════════════════════════════════════════════════════════════
# Resolver dispatch table
# ═════════════════════════════════════════════════════════════════════════════

_RESOLVERS = {
    "compound":      resolve_compound,
    "property":      resolve_property,
    "measurement":   resolve_measurement,
    "variable":      resolve_variable,
    "constraint":    resolve_constraint,
    "phase":         resolve_phase,
    "reference":     resolve_reference,
    "solvent":       resolve_solvent,
    "block_type":    resolve_block_type,
    "reaction_type": resolve_reaction_type,
}

VALID_ENTITY_TYPES = tuple(_RESOLVERS.keys())

# ═════════════════════════════════════════════════════════════════════════════
# CSV registry metadata per entity type
# ═════════════════════════════════════════════════════════════════════════════

# (csv_registry_name, primary_num_id_column)
_NUM_ID_COLS = {
    "compound":      ("compound_ids",      "comp_num_id"),
    "property":      ("property_ids",      "prop_num_id"),
    "measurement":   ("measurement_ids",   "meas_num_id"),
    "variable":      ("variable_ids",      "var_num_id"),
    "constraint":    ("constraint_ids",    "constr_num_id"),
    "phase":         ("phase_ids",         "phase_num_id"),
    "reference":     ("reference_ids",     "lit_num_id"),
    "solvent":       ("solvent_components", "solvent_num_id"),
    "block_type":    ("block_types",       "blocktype_num_id"),
    "reaction_type": ("reaction_type_ids", "rxn_type_num_id"),
}

# Columns to cast to int when building results from CSV rows
_INT_COLS = {
    "n_papers", "n_blocks", "n_occurrences", "n_compounds",
    "total_datapoints", "n_blocks_as_solvent",
}

# ═════════════════════════════════════════════════════════════════════════════
# CSV cache + loader
# ═════════════════════════════════════════════════════════════════════════════

_csv_cache: dict[str, list[dict[str, str]]] = {}


def _load_csv(name: str) -> list[dict[str, str]]:
    """Load a CSV registry file (cached after first read)."""
    if name not in _csv_cache:
        p = csv_path(name)
        with open(p, "r", encoding="utf-8") as fh:
            _csv_cache[name] = list(csv.DictReader(fh))
    return _csv_cache[name]


# ═════════════════════════════════════════════════════════════════════════════
# Input parsing helpers
# ═════════════════════════════════════════════════════════════════════════════

def _global_id_lookup(entity_type: str, value: str) -> dict | None:
    """Find a registry row by one strictly validated global ID."""
    spec = _NUM_ID_COLS[entity_type]
    csv_name, id_col = spec
    try:
        target = require_global_id(GLOBAL_FIELD_BY_ENTITY[entity_type], value)
    except ValueError:
        return None
    for row in _load_csv(csv_name):
        if row[id_col] == target:
            result = dict(row)
            for col in result:
                if col in _INT_COLS:
                    raw = result[col]
                    if raw == "":
                        result[col] = None
                    elif isinstance(raw, str) and raw.isdigit():
                        result[col] = int(raw)
                    else:
                        raise ValueError(
                            f"registry {entity_type}.{col} must be an integer or empty, got {raw!r}"
                        )
            result["score"] = 100
            result["match_type"] = "global_id"
            return result
    return None


# ═════════════════════════════════════════════════════════════════════════════
# Core single-query resolver (strict global-ID lookup, then text resolution)
# ═════════════════════════════════════════════════════════════════════════════

def _resolve_single(entity_type: str, query: str,
                    min_score: int = 50, limit: int = 10) -> list[dict]:
    """Resolve one query string for *entity_type*.

    A valid ``GLOB*`` identifier is matched directly. All other inputs are
    treated as names/structures/DOIs; bare numeric IDs and legacy prefixes are
    never interpreted as identifiers.
    """
    q = query.strip()
    if not q:
        return []

    hit = _global_id_lookup(entity_type, q)
    if hit and hit["score"] >= min_score:
        return [hit]

    # Text-based resolver
    resolver = _RESOLVERS[entity_type]
    hits = resolver(q, limit=limit)
    validated: list[dict] = []
    global_field = GLOBAL_FIELD_BY_ENTITY[entity_type]
    id_col = _NUM_ID_COLS[entity_type][1]
    for index, hit_row in enumerate(hits):
        if not isinstance(hit_row, dict):
            raise TypeError(f"{entity_type} resolver result[{index}] must be an object")
        for field in (id_col, "score", "match_type"):
            if field not in hit_row:
                raise ValueError(f"{entity_type} resolver result[{index}] is missing {field}")
        require_global_id(global_field, hit_row[id_col])
        score = hit_row["score"]
        if isinstance(score, bool) or not isinstance(score, int) or not 0 <= score <= 100:
            raise TypeError(f"{entity_type} resolver score must be an integer from 0 through 100")
        if not isinstance(hit_row["match_type"], str) or not hit_row["match_type"]:
            raise TypeError(f"{entity_type} resolver match_type must be a non-empty string")
        if score >= min_score:
            validated.append(hit_row)
    return validated


# ═════════════════════════════════════════════════════════════════════════════
# Multi-value resolver
# ═════════════════════════════════════════════════════════════════════════════

def resolve_ids(entity_type: str, queries: SearchValue, *,
                min_score: int = 50, limit: int = 20) -> list[dict]:
    """Resolve one or more queries for *entity_type*.

    Parameters
    ----------
    entity_type : str
        One of VALID_ENTITY_TYPES.
    queries : str | list[str] | None
        Single string, flat string list, or None.
        Bare numeric, legacy, and wrong-scope identifiers raise an explicit
        :class:`IdentifierRefinementError`.
    min_score : int
        Minimum match score to include (default 50).
    limit : int
        Maximum results returned (default 20).

    Returns
    -------
    list[dict]
        Match dicts in the same format as the underlying resolver, with
        ``score`` and ``match_type`` fields.  Deduplicated by primary
        typed global ID.
    """
    if entity_type not in _RESOLVERS:
        raise ValueError(
            f"Unknown entity_type {entity_type!r}; expected one of "
            f"{', '.join(VALID_ENTITY_TYPES)}"
        )
    if isinstance(min_score, bool) or not isinstance(min_score, int) or not 0 <= min_score <= 100:
        raise TypeError("min_score must be an integer from 0 through 100")
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise TypeError("limit must be a positive integer")
    parts = validate_search_values(entity_type, queries, field=entity_type)
    if not parts:
        return []
    id_col = _NUM_ID_COLS[entity_type][1]

    seen: set = set()
    results: list[dict] = []

    for q in parts:
        hits = _resolve_single(entity_type, q, min_score=min_score, limit=limit)
        for h in hits:
            key = h[id_col]
            if key in seen:
                continue
            seen.add(key)
            results.append(h)
            if len(results) >= limit:
                return results

    return results


# ═════════════════════════════════════════════════════════════════════════════
# Convenience resolvers (used by search tools)
# ═════════════════════════════════════════════════════════════════════════════

def resolve_compound_ids(queries: SearchValue, *, min_score: int = 50,
                         limit: int = 20) -> list[dict]:
    """Resolve compound queries (name, formula, SMILES, InChI, ID)."""
    return resolve_ids("compound", queries, min_score=min_score, limit=limit)


def resolve_property_ids(queries: SearchValue, *, min_score: int = 50,
                         limit: int = 20) -> list[dict]:
    """Resolve property queries (name, prop_id, group, ID)."""
    return resolve_ids("property", queries, min_score=min_score, limit=limit)


def resolve_measurement_ids(queries: SearchValue, *, min_score: int = 50,
                            limit: int = 20) -> list[dict]:
    """Resolve measurement queries (method name, meas_id, acronym, ID)."""
    return resolve_ids("measurement", queries, min_score=min_score, limit=limit)


def resolve_reference_ids(queries: SearchValue, *, min_score: int = 50,
                          limit: int = 20) -> list[dict]:
    """Resolve reference queries (DOI, lit_id, author, year, ID)."""
    return resolve_ids("reference", queries, min_score=min_score, limit=limit)


def resolve_phase_ids(queries: SearchValue, *, min_score: int = 50,
                      limit: int = 20) -> list[dict]:
    """Resolve phase queries (phase name, phase_id, ID)."""
    return resolve_ids("phase", queries, min_score=min_score, limit=limit)


def resolve_variable_ids(queries: SearchValue, *, min_score: int = 50,
                         limit: int = 20) -> list[dict]:
    """Resolve variable queries (name, var_id, ID)."""
    return resolve_ids("variable", queries, min_score=min_score, limit=limit)


def resolve_constraint_ids(queries: SearchValue, *, min_score: int = 50,
                           limit: int = 20) -> list[dict]:
    """Resolve constraint queries (name, constr_id, ID)."""
    return resolve_ids("constraint", queries, min_score=min_score, limit=limit)


def resolve_solvent_ids(queries: SearchValue, *, min_score: int = 50,
                        limit: int = 20) -> list[dict]:
    """Resolve solvent queries (name, formula, InChI-key, ID)."""
    return resolve_ids("solvent", queries, min_score=min_score, limit=limit)


# Agent-facing resolver adapters. Internal search code consumes row arrays;
# tool calls use an explicit object schema so result processing never has to
# infer an entity type or wrap a bare list.
def resolve_ids_tool(
    entity_type: str,
    queries: SearchValue,
    *,
    min_score: int = 50,
    limit: int = 20,
) -> dict:
    rows = resolve_ids(entity_type, queries, min_score=min_score, limit=limit)
    return {
        "entity_type": entity_type,
        "queries": queries,
        "n_results": len(rows),
        "results": rows,
    }


def resolve_compound_ids_tool(
    queries: SearchValue, *, min_score: int = 50, limit: int = 20
) -> dict:
    rows = resolve_compound_ids(queries, min_score=min_score, limit=limit)
    return {"n_results": len(rows), "results": rows}


def resolve_property_ids_tool(
    queries: SearchValue, *, min_score: int = 50, limit: int = 20
) -> dict:
    rows = resolve_property_ids(queries, min_score=min_score, limit=limit)
    return {"n_results": len(rows), "results": rows}


def resolve_measurement_ids_tool(
    queries: SearchValue, *, min_score: int = 50, limit: int = 20
) -> dict:
    rows = resolve_measurement_ids(queries, min_score=min_score, limit=limit)
    return {"n_results": len(rows), "results": rows}


def resolve_reference_ids_tool(
    queries: SearchValue, *, min_score: int = 50, limit: int = 20
) -> dict:
    rows = resolve_reference_ids(queries, min_score=min_score, limit=limit)
    return {"n_results": len(rows), "results": rows}


# ═════════════════════════════════════════════════════════════════════════════
# Public alignment API
# ═════════════════════════════════════════════════════════════════════════════

def search_id_alignment(entity_type: str, query: str, limit: int = 20) -> dict:
    """Resolve *query* against the CSV registry for *entity_type*.

    Parameters
    ----------
    entity_type : str
        One of: compound, property, measurement, variable, constraint,
        phase, reference, solvent, block_type, reaction_type.
    query : str
        Free-text search string (name, ID, formula, DOI, InChI-key, etc.).
    limit : int, optional
        Maximum number of results to return (default 20).

    Returns
    -------
    dict
        Keys: entity_type, query, n_results, results (list of match dicts).
    """
    if entity_type not in _RESOLVERS:
        raise ValueError(
            f"Unknown entity_type {entity_type!r}; expected one of "
            f"{', '.join(VALID_ENTITY_TYPES)}"
        )

    try:
        matches = resolve_ids(entity_type, query, limit=limit)
    except IdentifierRefinementError as exc:
        return {
            "entity_type": entity_type,
            "query": query,
            "n_results": 0,
            "results": [],
            **exc.as_result(),
        }

    return {
        "entity_type": entity_type,
        "query": query,
        "n_results": len(matches),
        "results": matches,
    }


# ═════════════════════════════════════════════════════════════════════════════
# Card-level compaction  (ID → compact markdown)
# ═════════════════════════════════════════════════════════════════════════════

# Lazy-imported compactor get_card_md functions.
# We defer imports to avoid heavy DB / compactor overhead unless needed.

_WORKSPACE = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir)
)
if _WORKSPACE not in sys.path:
    sys.path.insert(0, _WORKSPACE)


def _get_card_md_fn(card_type: str):
    """Return the ``get_card_md`` callable for *card_type* (lazy import)."""
    if card_type == "CCS_INDIV":
        from ThermoML_card_json_to_md_compactors._basic_compactors.component_cards_compactor.ccs_compactor import get_card_md
    elif card_type == "CCS_ID_DK":
        from ThermoML_card_json_to_md_compactors._basic_compactors.component_cards_compactor.ccs_iddk_compactor import get_card_md
    elif card_type == "MTDKS_INDIV":
        from ThermoML_card_json_to_md_compactors._basic_compactors.measurement_cards_compactor.mtdks_compactor import get_card_md
    elif card_type == "MTDKS_ID_DK":
        from ThermoML_card_json_to_md_compactors._basic_compactors.measurement_cards_compactor.mtdks_iddk_compactor import get_card_md
    elif card_type == "PCS_INDIV":
        from ThermoML_card_json_to_md_compactors._basic_compactors.property_cards_compactor.pcs_compactor import get_card_md
    elif card_type == "PCS_ID_DK":
        from ThermoML_card_json_to_md_compactors._basic_compactors.property_cards_compactor.pcs_iddk_compactor import get_card_md
    elif card_type == "RMS_INDIV":
        from ThermoML_card_json_to_md_compactors._basic_compactors.reference_cards_compactor.rms_compactor import get_card_md
    elif card_type == "PCS_BLOCK":
        from ThermoML_card_json_to_md_compactors._cross_cards_compactors.block_cards_compactor.block_compactor import get_card_md
    else:
        return None
    return get_card_md


# Valid card types for the public API
VALID_CARD_TYPES = (
    "CCS_INDIV", "CCS_ID_DK",
    "MTDKS_INDIV", "MTDKS_ID_DK",
    "PCS_INDIV", "PCS_ID_DK",
    "RMS_INDIV",
    "PCS_BLOCK",
)


def resolve_card_md(
    card_type: str,
    *,
    doi: str | None = None,
    lit_num_id: str | None = None,
    comp_num_id: str | None = None,
    meas_num_id: str | None = None,
    meas_id: str | None = None,
    prop_num_id: str | None = None,
    prop_id: str | None = None,
    block_number: str | None = None,
    BLKsubsys_id: str | None = None,
) -> str:
    """Fetch a card from the DB by resolved IDs and return compact markdown.

    Dispatches to the appropriate compactor's ``get_card_md()`` API.

    Parameters
    ----------
    card_type : str
        One of :data:`VALID_CARD_TYPES`.
    Remaining parameters
        The exact selector accepted by the requested card type:

        ============  =====================================
        Card type     Keyword args (provide one identifier)
        ============  =====================================
        CCS_INDIV     ``doi=`` or ``lit_num_id=``
        CCS_ID_DK     ``comp_num_id=``
        MTDKS_INDIV   ``doi=`` or ``lit_num_id=``
        MTDKS_ID_DK   ``meas_num_id=`` or ``meas_id=``
        PCS_INDIV     ``doi=`` or ``lit_num_id=``
        PCS_ID_DK     ``prop_num_id=`` or ``prop_id=``
        RMS_INDIV     ``doi=`` or ``lit_num_id=``
        PCS_BLOCK     ``doi=`` or ``lit_num_id=``, ``block_number=``,
                      optional ``BLKsubsys_id=``
        ============  =====================================

    Returns
    -------
    str
        Compact markdown representation. Invalid card types, strict-ID
        violations, and lookup failures raise explicit errors; they are never
        converted to an empty result.
    """
    fn = _get_card_md_fn(card_type)
    if fn is None:
        raise ValueError(
            f"Unknown card_type {card_type!r}; expected one of "
            f"{', '.join(VALID_CARD_TYPES)}"
        )
    selectors = {
        "CCS_INDIV": {"doi": doi, "lit_num_id": lit_num_id},
        "CCS_ID_DK": {"comp_num_id": comp_num_id},
        "MTDKS_INDIV": {"doi": doi, "lit_num_id": lit_num_id},
        "MTDKS_ID_DK": {"meas_num_id": meas_num_id, "meas_id": meas_id},
        "PCS_INDIV": {"doi": doi, "lit_num_id": lit_num_id},
        "PCS_ID_DK": {"prop_num_id": prop_num_id, "prop_id": prop_id},
        "RMS_INDIV": {"doi": doi, "lit_num_id": lit_num_id},
        "PCS_BLOCK": {
            "doi": doi,
            "lit_num_id": lit_num_id,
            "block_number": block_number,
            "BLKsubsys_id": BLKsubsys_id,
        },
    }
    selected = selectors[card_type]
    supplied = {
        name: value for name, value in {
            "doi": doi,
            "lit_num_id": lit_num_id,
            "comp_num_id": comp_num_id,
            "meas_num_id": meas_num_id,
            "meas_id": meas_id,
            "prop_num_id": prop_num_id,
            "prop_id": prop_id,
            "block_number": block_number,
            "BLKsubsys_id": BLKsubsys_id,
        }.items() if value is not None
    }
    irrelevant = sorted(set(supplied) - set(selected))
    if irrelevant:
        raise ValueError(
            f"{card_type} does not accept selector(s) {irrelevant}; allowed "
            f"selectors are {sorted(selected)}"
        )

    if lit_num_id is not None:
        selected["lit_num_id"] = require_global_tool_id(
            "reference", lit_num_id, field="lit_num_id"
        )
    if comp_num_id is not None:
        selected["comp_num_id"] = require_global_tool_id(
            "compound", comp_num_id, field="comp_num_id"
        )
    if meas_num_id is not None:
        selected["meas_num_id"] = require_global_tool_id(
            "measurement", meas_num_id, field="meas_num_id"
        )
    if prop_num_id is not None:
        selected["prop_num_id"] = require_global_tool_id(
            "property", prop_num_id, field="prop_num_id"
        )
    if block_number is not None:
        selected["block_number"] = require_typed_block_input(block_number)
    if BLKsubsys_id is not None:
        selected["BLKsubsys_id"] = require_block_local_id(
            "subsys", BLKsubsys_id
        )

    selected = {name: value for name, value in selected.items() if value is not None}
    identity_groups = {
        "CCS_INDIV": ("doi", "lit_num_id"),
        "CCS_ID_DK": ("comp_num_id",),
        "MTDKS_INDIV": ("doi", "lit_num_id"),
        "MTDKS_ID_DK": ("meas_num_id", "meas_id"),
        "PCS_INDIV": ("doi", "lit_num_id"),
        "PCS_ID_DK": ("prop_num_id", "prop_id"),
        "RMS_INDIV": ("doi", "lit_num_id"),
        "PCS_BLOCK": ("doi", "lit_num_id"),
    }
    identity_fields = identity_groups[card_type]
    supplied_identity = [name for name in identity_fields if name in selected]
    if len(supplied_identity) != 1:
        raise ValueError(
            f"{card_type} requires exactly one identity selector from "
            f"{list(identity_fields)}; received {supplied_identity}"
        )
    for textual in ("doi", "meas_id", "prop_id"):
        if textual in selected and (
            not isinstance(selected[textual], str) or not selected[textual]
        ):
            raise TypeError(f"{textual} must be a non-empty string")
    result = fn(**selected)
    if not isinstance(result, str) or not result:
        raise LookupError(
            f"{card_type} lookup returned no compact card for {selected}"
        )
    return result


# ── demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import json

    demos = [
        ("compound",      "water"),
        ("compound",      "ethanol"),
        ("property",      "density"),
        ("measurement",   "DSC"),
        ("reference",     "2005"),
        ("variable",      "temperature"),
        ("constraint",    "pressure"),
        ("phase",         "liquid"),
        ("solvent",       "water"),
        ("block_type",    "binary"),
        ("reaction_type", "combustion"),
    ]

    for etype, q in demos:
        result = search_id_alignment(etype, q, limit=5)
        n = result["n_results"]
        print(f"\n{'='*72}")
        print(f"  {etype:15s} | query={q!r:20s} | hits={n}")
        print(f"{'='*72}")
        for m in result["results"][:3]:
            score = m.get("score", "?")
            mtype = m.get("match_type", "?")
            # show a compact summary depending on entity type
            if etype == "compound":
                label = m.get("common_name", "")
            elif etype == "property":
                label = m.get("prop_name", "")
            elif etype == "measurement":
                label = m.get("method_name", "")
            elif etype == "reference":
                label = f'{m.get("first_author", "")} ({m.get("year", "")})'
            elif etype == "variable":
                label = m.get("var_name", "")
            elif etype == "constraint":
                label = m.get("constr_name", "")
            elif etype == "phase":
                label = m.get("phase_name", "")
            elif etype == "solvent":
                label = m.get("common_name", "")
            elif etype == "block_type":
                label = m.get("block_type", "")
            elif etype == "reaction_type":
                label = m.get("rxn_type_name", "")
            else:
                label = ""
            print(f"    score={score:3}  {mtype:16s}  {label}")

    # also show an invalid entity_type to confirm error handling
    bad = search_id_alignment("unknown_type", "test")
    print(f"\nError test: {bad}")
