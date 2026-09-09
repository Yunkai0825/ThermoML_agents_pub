"""
10_compound_similarity_search.py — Fingerprint similarity search for ThermoML compounds.
=========================================================================================

Search for structurally similar compounds using pre-computed Morgan/MACCS
fingerprints.  Supports:
  1. Query by comp_num_id (existing DB compound)
  2. Query by SMILES/InChI (arbitrary structure — on-the-fly fingerprint)
  3. Query by chemical name (auto-resolved to SMILES via resolve_compound)

Public API
----------
search_similar_compounds(
    comp_num_id=None, smiles=None, name=None,
    top_k=10, metric="morgan",
) -> dict

Returns dict with:
    query: {comp_num_id, name, smiles}
    metric: str
    results: [{comp_num_id, common_name, formula, smiles, similarity, n_papers}]
"""

from __future__ import annotations

import logging
import sqlite3
import sys
import os
from pathlib import Path
from typing import Optional

log = logging.getLogger("SIM-SEARCH")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normalization_helpers.paths import card_db_path, csv_path
from normalization_helpers.db_helpers import open_db
from _id_alignment_search import resolve_compound_ids
from normalization_helpers.strict_id_inputs import (
    refinement_errors_as_results,
    require_global_tool_id,
    validate_search_atom,
)

_CCS_IDDK_DB = card_db_path("CCS_ID_DK")

# Lazy-loaded RDKit imports
_rdkit_loaded = False
_Chem = None
_AllChem = None
_MACCSkeys = None
_DataStructs = None


def _ensure_rdkit():
    global _rdkit_loaded, _Chem, _AllChem, _MACCSkeys, _DataStructs
    if _rdkit_loaded:
        return
    from rdkit import Chem, RDLogger
    from rdkit.Chem import AllChem, MACCSkeys
    from rdkit import DataStructs
    RDLogger.DisableLog("rdApp.*")
    _Chem = Chem
    _AllChem = AllChem
    _MACCSkeys = MACCSkeys
    _DataStructs = DataStructs
    _rdkit_loaded = True


def _get_fp_db() -> sqlite3.Connection:
    if not os.path.exists(_CCS_IDDK_DB):
        raise FileNotFoundError(f"CCS_ID_DK.db not found: {_CCS_IDDK_DB}")
    return open_db(_CCS_IDDK_DB)


def _bitstring_to_bv(bitstring: str):
    _ensure_rdkit()
    return _DataStructs.CreateFromBitString(bitstring)


def _smiles_to_mol(smiles: str):
    _ensure_rdkit()
    return _Chem.MolFromSmiles(smiles)


def _inchi_to_smiles(inchi: str) -> Optional[str]:
    _ensure_rdkit()
    mol = _Chem.MolFromInchi(inchi)
    if mol is None:
        return None
    return _Chem.MolToSmiles(mol)


def _name_to_smiles(name: str) -> Optional[str]:
    """Resolve a chemical name through the compound registry only."""
    hits = resolve_compound_ids(name, limit=1)
    if hits and hits[0]["score"] >= 70:
        smiles = hits[0]["smiles"]
        if smiles:
            return smiles
    return None


def _compute_query_fp(smiles: str, metric: str):
    """Compute a fingerprint for a query molecule from SMILES."""
    _ensure_rdkit()
    mol = _smiles_to_mol(smiles)
    if mol is None:
        raise ValueError(f"Cannot parse SMILES: {smiles!r}")
    if metric == "maccs":
        return _MACCSkeys.GenMACCSKeys(mol)
    else:  # morgan
        return _AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=2048)


@refinement_errors_as_results
def search_similar_compounds(
    comp_num_id: Optional[str] = None,
    smiles: Optional[str] = None,
    inchi: Optional[str] = None,
    name: Optional[str] = None,
    top_k: int = 10,
    min_similarity: float = 0.0,
    metric: str = "morgan",
) -> dict:
    """Find the top-K most structurally similar compounds.

    Provide ONE of: comp_num_id, smiles, inchi, or name.

    Parameters
    ----------
    comp_num_id : str, optional
        Query by an existing compound's canonical ``GLOBcomp_N`` ID.
    smiles : str, optional
        Query by a SMILES string (arbitrary structure).
    inchi : str, optional
        Query by an InChI string.
    name : str, optional
        Query by chemical name (resolved to SMILES via registry).
    top_k : int
        Number of most similar compounds to return (default 10).
    min_similarity : float
        Minimum Tanimoto similarity threshold (0.0–1.0, default 0.0).
    metric : str
        "morgan" (default) or "maccs" for the similarity metric.

    Returns
    -------
    dict with keys:
        query: {comp_num_id, name, smiles}
        metric: str
        results: list of {comp_num_id, common_name, formula, smiles,
                          similarity, n_papers}
    """
    supplied_queries = [
        value for value in (comp_num_id, smiles, inchi, name)
        if value is not None
    ]
    if len(supplied_queries) != 1:
        raise ValueError(
            "TOOL_ARGUMENT_REFINEMENT_REQUIRED: exactly one of comp_num_id, "
            "smiles, inchi, or name is required"
        )
    if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1:
        raise TypeError("TOOL_ARGUMENT_REFINEMENT_REQUIRED: top_k must be a positive integer")
    if (
        isinstance(min_similarity, bool)
        or not isinstance(min_similarity, (int, float))
        or not 0 <= min_similarity <= 1
    ):
        raise TypeError(
            "TOOL_ARGUMENT_REFINEMENT_REQUIRED: min_similarity must be numeric in [0, 1]"
        )
    if metric not in ("morgan", "maccs"):
        raise ValueError(
            "TOOL_ARGUMENT_REFINEMENT_REQUIRED: metric must be exactly 'morgan' or 'maccs'"
        )
    if name is not None:
        name = validate_search_atom("compound", name, field="name")

    _ensure_rdkit()

    fp_col = "morgan_fingerprint" if metric == "morgan" else "maccs_fingerprint"
    db = _get_fp_db()

    # ── Resolve query to a fingerprint ──
    query_info = {}
    query_fp = None

    if comp_num_id is not None:
        comp_num_id = require_global_tool_id(
            "compound", comp_num_id, field="comp_num_id"
        )
        row = db.execute(
            f"SELECT primary_name, smiles, {fp_col} FROM cards "
            f"WHERE comp_num_id = ? AND fp_status = 'ok'",
            (comp_num_id,),
        ).fetchone()
        if row is None:
            db.close()
            return {
                "error": f"comp_num_id={comp_num_id} not found or has no fingerprint",
                "error_code": "QUERY_REFINEMENT_REQUIRED",
                "n_results": 0,
                "results": [],
            }
        query_fp = _bitstring_to_bv(row[fp_col])
        query_info = {"comp_num_id": comp_num_id, "name": row["primary_name"], "smiles": row["smiles"]}

    elif smiles is not None:
        query_fp = _compute_query_fp(smiles, metric)
        query_info = {"smiles": smiles}

    elif inchi is not None:
        _smiles = _inchi_to_smiles(inchi)
        if _smiles is None:
            db.close()
            return {
                "error": f"Cannot parse InChI: {inchi!r}",
                "error_code": "QUERY_REFINEMENT_REQUIRED",
                "n_results": 0,
                "results": [],
            }
        query_fp = _compute_query_fp(_smiles, metric)
        query_info = {"inchi": inchi, "smiles": _smiles}

    elif name is not None:
        resolved_smiles = _name_to_smiles(name)
        if resolved_smiles is None:
            db.close()
            return {
                "error": f"Cannot resolve name to SMILES: {name!r}",
                "error_code": "QUERY_REFINEMENT_REQUIRED",
                "n_results": 0,
                "results": [],
            }
        query_fp = _compute_query_fp(resolved_smiles, metric)
        query_info = {"name": name, "smiles": resolved_smiles}

    # ── Compute similarities against all DB compounds ──
    rows = db.execute(
        f"SELECT comp_num_id, inchi_key, primary_name, formula, smiles, {fp_col} "
        f"FROM cards WHERE fp_status = 'ok'"
    ).fetchall()
    db.close()

    # Load n_papers from CSV for enrichment (cached)
    import csv
    csv_file = Path(csv_path("compound_ids"))
    papers_map = {}
    if not csv_file.exists():
        raise FileNotFoundError(f"Required compound registry CSV is missing: {csv_file}")
    with open(csv_file, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            require_global_tool_id("compound", r["comp_num_id"], field="comp_num_id")
            if not r["n_papers"].isdigit():
                raise ValueError(f"compound n_papers must be an integer, got {r['n_papers']!r}")
            papers_map[r["comp_num_id"]] = int(r["n_papers"])

    # Compute Tanimoto similarities
    results = []
    query_cid = query_info["comp_num_id"] if "comp_num_id" in query_info else None
    for row in rows:
        cid = row["comp_num_id"]
        if cid == query_cid:
            continue  # skip self
        target_fp = _bitstring_to_bv(row[fp_col])
        sim = _DataStructs.TanimotoSimilarity(query_fp, target_fp)
        if sim < min_similarity:
            continue
        results.append({
            "comp_num_id": cid,
            "inchi_key": row["inchi_key"],
            "common_name": row["primary_name"],
            "formula": row["formula"],
            "smiles": row["smiles"],
            "similarity": round(sim, 4),
            "n_papers": papers_map[cid],
        })

    # Sort by similarity descending, take top-K
    results.sort(key=lambda x: -x["similarity"])
    results = results[:top_k]

    return {
        "query": query_info,
        "metric": metric,
        "n_results": len(results),
        "results": results,
    }
