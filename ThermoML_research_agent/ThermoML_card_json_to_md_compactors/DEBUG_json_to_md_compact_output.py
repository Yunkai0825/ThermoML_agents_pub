import sys
from pathlib import Path


_PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
_DIAGNOSTICS = _PROJECT_ROOT.parent / "_output" / "Query" / "Diagnostics"
"""
Generate compacted markdown cards for every JSON file in Diagnostics/.

For each JSON debug card, runs the matching compactor and writes a .md file
alongside it in the same subdirectory.

Usage (from ThermoML_research_agent):
    python ThermoML_card_json_to_md_compactors/DEBUG_json_to_md_compact_output.py
"""

import json, os, sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.insert(0, _ROOT)

_DEBUG = os.fspath(_DIAGNOSTICS / 'card_databases')

from ThermoML_card_json_to_md_compactors._basic_compactors.component_cards_compactor.ccs_compactor import compact_ccs
from ThermoML_card_json_to_md_compactors._basic_compactors.component_cards_compactor.ccs_iddk_compactor import compact_ccs_iddk
from ThermoML_card_json_to_md_compactors._basic_compactors.measurement_cards_compactor.mtdks_compactor import compact_mtdks
from ThermoML_card_json_to_md_compactors._basic_compactors.measurement_cards_compactor.mtdks_iddk_compactor import compact_mtdks_iddk
from ThermoML_card_json_to_md_compactors._basic_compactors.property_cards_compactor.pcs_compactor import compact_pcs
from ThermoML_card_json_to_md_compactors._basic_compactors.property_cards_compactor.pcs_iddk_compactor import compact_pcs_iddk
from ThermoML_card_json_to_md_compactors._basic_compactors.reference_cards_compactor.rms_compactor import compact_rms
from ThermoML_card_json_to_md_compactors._cross_cards_compactors.block_cards_compactor.block_compactor import (
    _build_compounds_map,
    compact_block,
)
from ThermoML_raw_json_to_card_db_parsers.id_schema import validate_nested_identifiers

# Map Diagnostics subdirectory name → compactor function
_COMPACTORS = {
    'CCS_INDIV':   compact_ccs,
    'CCS_ID_DK':   compact_ccs_iddk,
    'MTDKS_INDIV': compact_mtdks,
    'MTDKS_ID_DK': compact_mtdks_iddk,
    'PCS_INDIV':   compact_pcs,
    'PCS_ID_DK':   compact_pcs_iddk,
    'RMS_INDIV':   compact_rms,
}


def main():
    total = 0
    for subdir, compactor in sorted(_COMPACTORS.items()):
        d = os.path.join(_DEBUG, subdir)
        if not os.path.isdir(d):
            raise FileNotFoundError(f"Required diagnostics directory not found: {d}")
        jsons = sorted(f for f in os.listdir(d) if f.endswith('.json'))
        print(f"\n=== {subdir} ({len(jsons)} cards) ===")
        for fname in jsons:
            with open(os.path.join(d, fname), encoding='utf-8') as f:
                card = json.load(f)
            validate_nested_identifiers(card, path=f"{subdir}/{fname}")
            md = compactor(card)
            md_path = os.path.join(d, fname.replace('.json', '.md'))
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(md)
            total += 1
            print(f"  {fname:<65} -> {len(md):>5} chars")
    print(f"\nDone — {total} .md files written to Diagnostics/")

    # -----------------------------------------------------------------------
    # PCS_BLOCK: extract individual blocks from PCS_INDIV JSONs
    # -----------------------------------------------------------------------
    pcs_dir = os.path.join(_DEBUG, 'PCS_INDIV')
    blk_dir = os.path.join(_DEBUG, 'PCS_BLOCK')
    os.makedirs(blk_dir, exist_ok=True)
    blk_total = 0
    if os.path.isdir(pcs_dir):
        pcs_jsons = sorted(f for f in os.listdir(pcs_dir) if f.endswith('.json'))
        print(f"\n=== PCS_BLOCK (from {len(pcs_jsons)} PCS_INDIV cards) ===")
        for fname in pcs_jsons:
            with open(os.path.join(pcs_dir, fname), encoding='utf-8') as f:
                card = json.load(f)
            validate_nested_identifiers(card, path=f"PCS_INDIV/{fname}")
            key = card["key"]
            paper = card["paper"]
            doi = key["doi"]
            lit_num_id = key["lit_num_id"]
            lit_id = key["lit_id"]
            key_info = {"doi": doi, "lit_num_id": lit_num_id, "lit_id": lit_id,
                        "title": paper.get("title", "")}
            blocks = card["blocks"]
            if not blocks:
                raise ValueError(f"PCS card has no blocks: {fname}")
            all_compounds = []
            for b in blocks:
                all_compounds.extend(b.get("compounds", []))
            cmap = _build_compounds_map(all_compounds)
            doi_slug = fname.replace('.json', '')
            # Pick one representative block: the one with most data points
            rep = max(blocks, key=lambda b: b["data_summary"]["n_points"])
            for b in [rep]:
                bn = b["block_number"]
                # Write block JSON
                blk_json = {"key_info": key_info, "block": b}
                blk_fname = f"{doi_slug}_{bn}"
                json_path = os.path.join(blk_dir, blk_fname + '.json')
                with open(json_path, 'w', encoding='utf-8') as f:
                    json.dump(blk_json, f, ensure_ascii=False)
                # Write block MD
                md = compact_block(b, key_info=key_info, compounds_map=cmap)
                md_path = os.path.join(blk_dir, blk_fname + '.md')
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(md)
                blk_total += 1
            print(f"  {fname:<65} -> {bn} (of {len(blocks)} blocks)")
        print(f"\nDone — {blk_total} block .md + .json pairs written to PCS_BLOCK/")


if __name__ == '__main__':
    main()
