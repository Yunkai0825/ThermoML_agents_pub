"""
CCS Compound Identity (ID & DK) card builder.

Builds Tier 1 identity cards for compounds. Two modes:
  - Per-DOI:  build identity cards for all compounds in one paper  (used by orchestrator)
  - Bulk:     build identity cards for ALL 8502 unique compounds   (for full card generation)

Schema: CCS_compound_ID_and_DK_schema.json v1.0.0
"""

import sqlite3
import json
import os
from collections import Counter

from ThermoML_raw_json_to_card_db_parsers.shared_utils import (
    resolve_compound_structure_identifiers,
)

try:
    from rdkit import Chem
    _HAS_RDKIT = True
except ImportError:
    _HAS_RDKIT = False


def _inchi_to_smiles(inchi):
    """Convert an InChI string to canonical SMILES via RDKit. Returns None on failure."""
    if not _HAS_RDKIT or not inchi:
        return None
    mol = Chem.MolFromInchi(inchi, sanitize=True)
    if mol is None:
        return None
    return Chem.MolToSmiles(mol)


def build_ccs_identity_cards_for_doi(data, index):
    """Build CCS Tier 1 identity cards for all compounds in a single paper.

    Args:
        data: Parsed ThermoML JSON dict for one paper.
        index: ThermoMLIndex instance.

    Returns:
        List of identity card dicts, one per compound.
    """
    cards = []
    for comp in data.get("Compound", []):
        card = _build_one_identity(comp, index)
        if card:
            cards.append(card)
    return cards


def build_all_ccs_identity_cards(db_path, index):
    """Build CCS Tier 1 identity cards for ALL unique compounds in the database.

    Scans the compounds table to collect all names per unique InChIKey,
    then builds one identity card per compound.

    Args:
        db_path: Path to thermoml_raw.db.
        index: ThermoMLIndex instance.

    Returns:
        List of identity card dicts, one per unique compound.
    """
    conn = sqlite3.connect(db_path)
    rows = conn.execute(
        "SELECT standard_inchi_key, standard_inchi, common_name, formula "
        "FROM compounds WHERE standard_inchi_key IS NOT NULL"
    ).fetchall()
    conn.close()

    # Group all names by InChIKey
    name_counter = {}  # inchi_key -> Counter of names
    inchi_map = {}     # inchi_key -> standard_inchi
    formula_map = {}   # inchi_key -> formula

    for inchi_key, inchi, name, formula in rows:
        if not inchi_key:
            continue
        if inchi_key not in name_counter:
            name_counter[inchi_key] = Counter()
            inchi_map[inchi_key] = inchi
            formula_map[inchi_key] = formula
        if name:
            name_counter[inchi_key][name] += 1

    # Also collect SMILES from raw JSON data
    smiles_map = _collect_smiles(db_path)

    # RDKit fallback: convert InChI → SMILES for compounds missing SMILES
    rdkit_generated = 0
    for inchi_key in name_counter:
        if inchi_key not in smiles_map:
            smiles = _inchi_to_smiles(inchi_map.get(inchi_key))
            if smiles:
                smiles_map[inchi_key] = smiles
                rdkit_generated += 1
    if rdkit_generated:
        print(f"  RDKit generated SMILES for {rdkit_generated} compounds")

    cards = []
    for inchi_key, counter in sorted(name_counter.items()):
        comp_row = index.lookup_compound(inchi_key=inchi_key)
        if comp_row is None:
            raise ValueError(f"Compound registry lookup failed for InChIKey {inchi_key!r}")
        comp_num_id = comp_row["comp_num_id"]

        # Names sorted by frequency (most common first)
        sorted_names = [name for name, _ in counter.most_common()]
        primary_name = sorted_names[0] if sorted_names else comp_row["common_name"]

        cards.append({
            "comp_num_id": comp_num_id,
            "identity": {
                "inchi_key": inchi_key,
                "SMILES": comp_row.get("smiles") or smiles_map.get(inchi_key),
                "InChI": inchi_map.get(inchi_key) or comp_row.get("standard_inchi") or None,
                "formula": formula_map.get(inchi_key, ""),
            },
            "names": {
                "primary_name": primary_name,
                "all_names": sorted_names,
            },
        })

    return cards


def _build_one_identity(comp, index):
    """Build a single identity card from a raw Compound dict."""
    inchi_key = comp.get("sStandardInChIKey")
    inchi = comp.get("sStandardInChI")
    formula = comp.get("sFormulaMolec", "")

    names = comp.get("sCommonName", [])
    if isinstance(names, str):
        names = [names]

    comp_row = index.lookup_compound(
        inchi_key=inchi_key, standard_inchi=inchi,
        common_name=names[0] if names else None, formula=formula)
    if comp_row is None:
        raise ValueError(
            f"Compound registry lookup failed for InChIKey={inchi_key!r}, formula={formula!r}"
        )
    comp_num_id = comp_row["comp_num_id"]
    structure = resolve_compound_structure_identifiers(comp, comp_row)
    smiles = structure["SMILES"] or _inchi_to_smiles(structure["InChI"])
    primary_name = comp_row["common_name"]

    return {
        "comp_num_id": comp_num_id,
        "identity": {
            "inchi_key": structure["inchi_key"],
            "SMILES": smiles,
            "InChI": structure["InChI"],
            "formula": formula,
        },
        "names": {
            "primary_name": primary_name,
            "all_names": names if names else [primary_name] if primary_name else [],
        },
    }


def _collect_smiles(db_path):
    """Scan all papers to collect SMILES for each unique InChIKey."""
    smiles_map = {}
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT json_data FROM papers")
    for (json_str,) in cursor:
        data = json.loads(json_str)
        for comp in data.get("Compound", []):
            ik = comp.get("sStandardInChIKey")
            if not ik or ik in smiles_map:
                continue
            sm = comp.get("sSmiles", [])
            if isinstance(sm, str):
                sm = [sm]
            if sm:
                smiles_map[ik] = sm[0]
    conn.close()
    return smiles_map
