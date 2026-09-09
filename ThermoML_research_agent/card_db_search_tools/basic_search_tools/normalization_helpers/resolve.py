"""
Resolve free-text agent inputs to canonical ThermoML IDs.

Every public ``resolve_*`` function accepts a *query* string and returns a list
of match dicts sorted by descending *score* (0-100).  Each dict always contains
at minimum ``score`` and ``match_type`` alongside the entity-specific fields.
"""

import csv
import logging
import re
from difflib import SequenceMatcher
from typing import Any, Dict, List, Optional, Tuple

from .paths import csv_path
from .comp_alias import expand_comp_alias
from .prop_alias import expand_prop_alias
from .meas_alias import expand_meas_alias
from .var_alias import expand_var_alias
from .constr_alias import expand_constr_alias
from ThermoML_raw_json_to_card_db_parsers.id_schema import require_global_id

log = logging.getLogger("normalization-resolve")

from rdkit import Chem, RDLogger

RDLogger.DisableLog("rdApp.*")

# ═══════════════════════════════════════════════════════════════════════════════
# Internal helpers
# ═══════════════════════════════════════════════════════════════════════════════

_csv_cache: Dict[str, List[Dict[str, str]]] = {}

_CSV_FIELDS = {
    "compound_ids": ("comp_num_id", "comp_id", "inchi_key", "common_name", "formula", "smiles", "standard_inchi", "n_papers"),
    "property_ids": ("prop_num_id", "prop_id", "prop_name", "prop_group", "comp_id_linked", "n_blocks"),
    "measurement_ids": ("meas_num_id", "meas_id", "method_name", "method_type", "n_blocks", "n_aliases"),
    "measurement_aliases": ("source_method_name", "source_method_type", "meas_num_id", "meas_id", "n_blocks"),
    "variable_ids": ("var_num_id", "var_id", "var_name", "var_type_key", "comp_id_linked", "n_blocks"),
    "constraint_ids": ("constr_num_id", "constr_id", "constr_name", "constr_type_key", "comp_id_linked", "n_blocks"),
    "phase_ids": ("phase_num_id", "phase_id", "phase_name", "n_occurrences"),
    "reference_ids": ("lit_num_id", "doi", "lit_id", "first_author", "year", "journal", "n_compounds", "n_blocks", "total_datapoints"),
    "solvent_components": ("solvent_num_id", "comp_num_id", "inchi_key", "common_name", "formula", "n_blocks_as_solvent"),
    "block_types": ("blocktype_num_id", "block_type", "system_type", "n_blocks"),
    "reaction_type_ids": ("rxn_type_num_id", "rxn_type_id", "rxn_type_name", "n_blocks"),
}

_NUMERIC_FIELDS = {
    "n_papers", "n_blocks", "n_aliases", "n_occurrences", "year",
    "n_compounds", "total_datapoints", "n_blocks_as_solvent", "comp_id_linked",
}

_GLOBAL_ID_FIELDS = {
    "comp_num_id", "prop_num_id", "meas_num_id", "var_num_id",
    "constr_num_id", "phase_num_id", "lit_num_id", "solvent_num_id",
    "blocktype_num_id", "rxn_type_num_id",
}


def _load_csv(name: str) -> List[Dict[str, str]]:
    """Load a CSV registry file (cached after first read)."""
    if name not in _csv_cache:
        p = csv_path(name)
        with open(p, "r", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            expected = _CSV_FIELDS[name]
            if tuple(reader.fieldnames or ()) != expected:
                raise ValueError(
                    f"registry {name!r} has fields {reader.fieldnames!r}; "
                    f"expected {list(expected)!r}"
                )
            rows = list(reader)
        for row_index, row in enumerate(rows, 2):
            for field in _GLOBAL_ID_FIELDS & row.keys():
                require_global_id(field, row[field])
            for field in _NUMERIC_FIELDS & row.keys():
                raw = row[field]
                if not isinstance(raw, str) or not raw.isdigit():
                    raise ValueError(
                        f"registry {name!r} row {row_index} field {field!r} "
                        f"must be an unsigned integer, got {raw!r}"
                    )
            for field, value in row.items():
                if field not in _NUMERIC_FIELDS and not isinstance(value, str):
                    raise TypeError(
                        f"registry {name!r} row {row_index} field {field!r} must be text"
                    )
        _csv_cache[name] = rows
    return _csv_cache[name]


def _validated_query(query: object, *, limit: object) -> str:
    if not isinstance(query, str) or not query.strip():
        raise TypeError("query must be a non-empty string")
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise TypeError("limit must be a positive integer")
    return query.strip()


def _fuzzy_score(a: str, b: str) -> int:
    return int(SequenceMatcher(None, a, b).ratio() * 100)


def _rank_matches(
    query: str,
    candidates: List[Tuple[int, str]],
    threshold: int = 55,
    limit: int = 10,
) -> List[Tuple[int, str, int]]:
    """Score *query* against (index, text) *candidates*.

    Returns [(index, text, score)] sorted descending by score.
    """
    query = _validated_query(query, limit=limit)
    if isinstance(threshold, bool) or not isinstance(threshold, int) or not 0 <= threshold <= 100:
        raise TypeError("threshold must be an integer from 0 through 100")
    q = query.lower().strip()
    scored: List[Tuple[int, str, int]] = []
    for idx, text in candidates:
        t = text.lower()
        if q == t:
            scored.append((idx, text, 100))
        elif q in t or t in q:
            scored.append((idx, text, 85))
        else:
            s = _fuzzy_score(q, t)
            if s >= threshold:
                scored.append((idx, text, s))
    scored.sort(key=lambda x: -x[2])
    return scored[:limit]


# ── RDKit helpers (lazy import) ──────────────────────────────────────────────

def _smiles_to_inchi_key(smiles: str) -> Optional[str]:
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None
        inchi = Chem.MolToInchi(mol)
        return Chem.InchiToInchiKey(inchi) if inchi else None
    except (ValueError, RuntimeError) as exc:
        log.debug("Failed to convert SMILES to InChIKey for %r: %s", smiles, exc)
        return None


def _inchi_to_inchi_key(inchi: str) -> Optional[str]:
    try:
        return Chem.InchiToInchiKey(inchi)
    except (ValueError, RuntimeError) as exc:
        log.debug("Failed to convert InChI to InChIKey for %r: %s", inchi, exc)
        return None


def _make_result(row: Dict[str, str], score: int, match_type: str) -> Dict[str, Any]:
    """Merge a CSV row while preserving every prefixed ID as text."""
    if isinstance(score, bool) or not isinstance(score, int) or not 0 <= score <= 100:
        raise TypeError("score must be an integer from 0 through 100")
    if not isinstance(match_type, str) or not match_type:
        raise TypeError("match_type must be a non-empty string")
    out: Dict[str, Any] = {}
    for k, v in row.items():
        out[k] = int(v) if k in _NUMERIC_FIELDS else v
    out["score"] = score
    out["match_type"] = match_type
    return out


# ═══════════════════════════════════════════════════════════════════════════════
# Public resolvers
# ═══════════════════════════════════════════════════════════════════════════════

def resolve_compound(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Resolve a compound query (name / formula / InChI / InChI-key / SMILES).

    Returns list of dicts with keys:
        comp_num_id, inchi_key, common_name, formula, standard_inchi,
        n_papers, score, match_type
    """
    q = expand_comp_alias(_validated_query(query, limit=limit))
    rows = _load_csv("compound_ids")
    results: List[Dict[str, Any]] = []

    # 1. Exact InChI-key
    if len(q) == 27 and q.count("-") == 2:
        for r in rows:
            if r["inchi_key"].upper() == q.upper():
                results.append(_make_result(r, 100, "inchi_key"))
        if results:
            return results[:limit]

    # 2. InChI string → key
    if q.startswith("InChI="):
        key = _inchi_to_inchi_key(q)
        if key:
            for r in rows:
                if r["inchi_key"].upper() == key.upper():
                    results.append(_make_result(r, 100, "inchi"))
            if results:
                return results[:limit]

    # 3. SMILES → InChI key (always attempt if short and not InChI)
    if not q.startswith("InChI") and len(q) < 500:
        key = _smiles_to_inchi_key(q)
        if key:
            for r in rows:
                if r["inchi_key"].upper() == key.upper():
                    results.append(_make_result(r, 100, "smiles"))
            if results:
                return results[:limit]

    # 4. Exact name (case-insensitive)
    ql = q.lower()
    for r in rows:
        if r["common_name"].lower() == ql:
            results.append(_make_result(r, 100, "name_exact"))
    if results:
        return results[:limit]

    # 5. Exact formula
    for r in rows:
        if r["formula"].lower() == ql:
            results.append(_make_result(r, 95, "formula_exact"))
    if results:
        return results[:limit]

    # 6. Fuzzy name match
    name_cands = [(i, r["common_name"]) for i, r in enumerate(rows)]
    for idx, text, score in _rank_matches(q, name_cands, threshold=50, limit=limit):
        results.append(_make_result(rows[idx], score, "name_fuzzy"))

    # 7. Supplement with fuzzy formula if weak name matches
    if not results or results[0]["score"] < 80:
        seen_ids = {r["comp_num_id"] for r in results}
        formula_cands = [(i, r["formula"]) for i, r in enumerate(rows)]
        for idx, text, score in _rank_matches(q, formula_cands, threshold=70, limit=5):
            r = rows[idx]
            if r["comp_num_id"] not in seen_ids:
                results.append(_make_result(r, score, "formula_fuzzy"))

    results.sort(key=lambda x: -x["score"])
    return results[:limit]


def resolve_property(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Resolve a property query (name / prop_id).

    Returns dicts: prop_num_id, prop_id, prop_name, prop_group, comp_id_linked,
                   n_blocks, score, match_type
    """
    q = expand_prop_alias(_validated_query(query, limit=limit))
    rows = _load_csv("property_ids")
    results: List[Dict[str, Any]] = []

    # Exact prop_id
    ql = q.lower()
    for r in rows:
        if r["prop_id"].lower() == ql:
            results.append(_make_result(r, 100, "prop_id_exact"))
    if results:
        return results[:limit]

    # Exact name
    for r in rows:
        if r["prop_name"].lower() == ql:
            results.append(_make_result(r, 100, "name_exact"))
    if results:
        return results[:limit]

    # Fuzzy name
    name_cands = [(i, r["prop_name"]) for i, r in enumerate(rows)]
    for idx, text, score in _rank_matches(q, name_cands, threshold=45, limit=limit):
        results.append(_make_result(rows[idx], score, "name_fuzzy"))

    # Also try prop_id fuzzy
    id_cands = [(i, r["prop_id"].replace("_", " ")) for i, r in enumerate(rows)]
    seen = {r["prop_num_id"] for r in results}
    for idx, text, score in _rank_matches(q, id_cands, threshold=50, limit=5):
        r = rows[idx]
        if r["prop_num_id"] not in seen:
            results.append(_make_result(r, score, "prop_id_fuzzy"))

    results.sort(key=lambda x: -x["score"])
    return results[:limit]


def resolve_measurement(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Resolve a measurement method query (name / meas_id).

    Returns dicts: meas_num_id, meas_id, method_name, method_type, n_blocks,
                   score, match_type
    """
    q = expand_meas_alias(_validated_query(query, limit=limit))
    rows = _load_csv("measurement_ids")
    alias_rows = _load_csv("measurement_aliases")
    canonical_by_id = {row["meas_id"]: row for row in rows}
    results: List[Dict[str, Any]] = []

    # Exact meas_id
    ql = q.lower()
    for r in rows:
        if r["meas_id"].lower() == ql:
            results.append(_make_result(r, 100, "meas_id_exact"))
    if results:
        return results[:limit]

    # Exact raw source alias.  This is the same explicit alias registry used
    # by card generation, so search and parsing cannot disagree.
    for alias in alias_rows:
        if alias["source_method_name"].lower() == ql:
            row = dict(canonical_by_id[alias["meas_id"]])
            row["source_method_name"] = alias["source_method_name"]
            row["source_method_type"] = alias["source_method_type"]
            results.append(_make_result(row, 100, "source_alias_exact"))
    if results:
        return results[:limit]

    # Exact method_name
    for r in rows:
        if r["method_name"].lower() == ql:
            results.append(_make_result(r, 100, "name_exact"))
    if results:
        return results[:limit]

    # Fuzzy method_name
    name_cands = [(i, r["method_name"]) for i, r in enumerate(rows)]
    for idx, text, score in _rank_matches(q, name_cands, threshold=45, limit=limit):
        results.append(_make_result(rows[idx], score, "name_fuzzy"))

    # Also meas_id fuzzy (replace underscores with spaces)
    id_cands = [(i, r["meas_id"].replace("_", " ")) for i, r in enumerate(rows)]
    seen = {r["meas_num_id"] for r in results}
    for idx, text, score in _rank_matches(q, id_cands, threshold=50, limit=5):
        r = rows[idx]
        if r["meas_num_id"] not in seen:
            results.append(_make_result(r, score, "meas_id_fuzzy"))

    # Alias fuzzy matching supplements canonical labels without producing a
    # second identity namespace.
    alias_cands = [
        (i, alias["source_method_name"]) for i, alias in enumerate(alias_rows)
    ]
    seen = {r["meas_num_id"] for r in results}
    for idx, text, score in _rank_matches(q, alias_cands, threshold=50, limit=limit):
        alias = alias_rows[idx]
        row = canonical_by_id[alias["meas_id"]]
        if row["meas_num_id"] not in seen:
            enriched = dict(row)
            enriched["source_method_name"] = alias["source_method_name"]
            enriched["source_method_type"] = alias["source_method_type"]
            results.append(_make_result(enriched, score, "source_alias_fuzzy"))
            seen.add(row["meas_num_id"])

    results.sort(key=lambda x: -x["score"])
    return results[:limit]


def resolve_reference(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Resolve a reference query (DOI / lit_id / author surname / year).

    Returns dicts: lit_num_id, doi, lit_id, first_author, year, journal,
                   n_compounds, n_blocks, total_datapoints, score, match_type
    """
    q = _validated_query(query, limit=limit)
    rows = _load_csv("reference_ids")
    results: List[Dict[str, Any]] = []

    # Exact DOI
    ql = q.lower()
    for r in rows:
        if r["doi"].lower() == ql:
            results.append(_make_result(r, 100, "doi_exact"))
    if results:
        return results[:limit]

    # Exact lit_id
    for r in rows:
        if r["lit_id"].lower() == ql:
            results.append(_make_result(r, 100, "lit_id_exact"))
    if results:
        return results[:limit]

    # Year (if query is a 4-digit number)
    if re.fullmatch(r"\d{4}", q):
        for r in rows:
            if r["year"] == q:
                results.append(_make_result(r, 80, "year"))
        results.sort(key=lambda x: -x["n_blocks"])
        return results[:limit]

    # Author fuzzy
    author_cands = [(i, r["first_author"]) for i, r in enumerate(rows)]
    for idx, text, score in _rank_matches(q, author_cands, threshold=55, limit=limit):
        results.append(_make_result(rows[idx], score, "author_fuzzy"))

    # Journal fuzzy
    if not results or results[0]["score"] < 80:
        journal_cands = [(i, r["journal"]) for i, r in enumerate(rows)]
        seen = {r["lit_num_id"] for r in results}
        for idx, text, score in _rank_matches(q, journal_cands, threshold=60, limit=5):
            r = rows[idx]
            if r["lit_num_id"] not in seen:
                results.append(_make_result(r, score, "journal_fuzzy"))

    results.sort(key=lambda x: -x["score"])
    return results[:limit]


def resolve_variable(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Resolve a variable query (name / var_id).

    Returns dicts: var_num_id, var_id, var_name, var_type_key,
                   comp_id_linked, n_blocks, score, match_type
    """
    q = expand_var_alias(_validated_query(query, limit=limit))
    rows = _load_csv("variable_ids")
    results: List[Dict[str, Any]] = []

    ql = q.lower()
    for r in rows:
        if r["var_id"].lower() == ql:
            results.append(_make_result(r, 100, "var_id_exact"))
    if results:
        return results[:limit]

    for r in rows:
        if r["var_name"].lower() == ql:
            results.append(_make_result(r, 100, "name_exact"))
    if results:
        return results[:limit]

    name_cands = [(i, r["var_name"]) for i, r in enumerate(rows)]
    for idx, text, score in _rank_matches(q, name_cands, threshold=45, limit=limit):
        results.append(_make_result(rows[idx], score, "name_fuzzy"))

    id_cands = [(i, r["var_id"].replace("_", " ")) for i, r in enumerate(rows)]
    seen = {r["var_num_id"] for r in results}
    for idx, text, score in _rank_matches(q, id_cands, threshold=50, limit=5):
        r = rows[idx]
        if r["var_num_id"] not in seen:
            results.append(_make_result(r, score, "var_id_fuzzy"))

    results.sort(key=lambda x: -x["score"])
    return results[:limit]


def resolve_constraint(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Resolve a constraint query (name / constr_id).

    Returns dicts: constr_num_id, constr_id, constr_name, constr_type_key,
                   comp_id_linked, n_blocks, score, match_type
    """
    q = expand_constr_alias(_validated_query(query, limit=limit))
    rows = _load_csv("constraint_ids")
    results: List[Dict[str, Any]] = []

    ql = q.lower()
    for r in rows:
        if r["constr_id"].lower() == ql:
            results.append(_make_result(r, 100, "constr_id_exact"))
    if results:
        return results[:limit]

    for r in rows:
        if r["constr_name"].lower() == ql:
            results.append(_make_result(r, 100, "name_exact"))
    if results:
        return results[:limit]

    name_cands = [(i, r["constr_name"]) for i, r in enumerate(rows)]
    for idx, text, score in _rank_matches(q, name_cands, threshold=45, limit=limit):
        results.append(_make_result(rows[idx], score, "name_fuzzy"))

    results.sort(key=lambda x: -x["score"])
    return results[:limit]


def resolve_phase(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Resolve a phase query (name / phase_id).

    Returns dicts: phase_num_id, phase_id, phase_name, n_occurrences,
                   score, match_type
    """
    q = _validated_query(query, limit=limit)
    rows = _load_csv("phase_ids")
    results: List[Dict[str, Any]] = []

    ql = q.lower()
    for r in rows:
        if r["phase_id"].lower() == ql:
            results.append(_make_result(r, 100, "phase_id_exact"))
    if results:
        return results[:limit]

    for r in rows:
        if r["phase_name"].lower() == ql:
            results.append(_make_result(r, 100, "name_exact"))
    if results:
        return results[:limit]

    name_cands = [(i, r["phase_name"]) for i, r in enumerate(rows)]
    for idx, text, score in _rank_matches(q, name_cands, threshold=45, limit=limit):
        results.append(_make_result(rows[idx], score, "name_fuzzy"))

    results.sort(key=lambda x: -x["score"])
    return results[:limit]


def resolve_solvent(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Resolve a solvent query (name / inchi_key / formula).

    Returns dicts: solvent_num_id, comp_num_id, inchi_key, common_name,
                   formula, n_blocks_as_solvent, score, match_type
    """
    q = _validated_query(query, limit=limit)
    rows = _load_csv("solvent_components")
    results: List[Dict[str, Any]] = []

    ql = q.lower()
    # Exact inchi_key
    if len(q) == 27 and q.count("-") == 2:
        for r in rows:
            if r["inchi_key"].upper() == q.upper():
                results.append(_make_result(r, 100, "inchi_key"))
        if results:
            return results[:limit]

    # Exact name
    for r in rows:
        if r["common_name"].lower() == ql:
            results.append(_make_result(r, 100, "name_exact"))
    if results:
        return results[:limit]

    # Exact formula
    for r in rows:
        if r["formula"].lower() == ql:
            results.append(_make_result(r, 95, "formula_exact"))
    if results:
        return results[:limit]

    # Fuzzy name
    name_cands = [(i, r["common_name"]) for i, r in enumerate(rows)]
    for idx, text, score in _rank_matches(q, name_cands, threshold=50, limit=limit):
        results.append(_make_result(rows[idx], score, "name_fuzzy"))

    results.sort(key=lambda x: -x["score"])
    return results[:limit]


def resolve_block_type(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Resolve a block type query.

    Returns dicts: blocktype_num_id, block_type, system_type, n_blocks,
                   score, match_type
    """
    q = _validated_query(query, limit=limit)
    rows = _load_csv("block_types")
    results: List[Dict[str, Any]] = []

    ql = q.lower()
    for r in rows:
        if r["block_type"].lower() == ql or r["system_type"].lower() == ql:
            results.append(_make_result(r, 100, "exact"))
    if results:
        return results[:limit]

    cands = [(i, f"{r['block_type']} {r['system_type']}") for i, r in enumerate(rows)]
    for idx, text, score in _rank_matches(q, cands, threshold=45, limit=limit):
        results.append(_make_result(rows[idx], score, "fuzzy"))

    results.sort(key=lambda x: -x["score"])
    return results[:limit]


def resolve_reaction_type(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Resolve a reaction type query.

    Returns dicts: rxn_type_num_id, rxn_type_id, rxn_type_name, n_blocks,
                   score, match_type
    """
    q = _validated_query(query, limit=limit)
    rows = _load_csv("reaction_type_ids")
    results: List[Dict[str, Any]] = []

    ql = q.lower()
    for r in rows:
        if r["rxn_type_id"].lower() == ql or r["rxn_type_name"].lower() == ql:
            results.append(_make_result(r, 100, "exact"))
    if results:
        return results[:limit]

    name_cands = [(i, r["rxn_type_name"]) for i, r in enumerate(rows)]
    for idx, text, score in _rank_matches(q, name_cands, threshold=45, limit=limit):
        results.append(_make_result(rows[idx], score, "name_fuzzy"))

    results.sort(key=lambda x: -x["score"])
    return results[:limit]
