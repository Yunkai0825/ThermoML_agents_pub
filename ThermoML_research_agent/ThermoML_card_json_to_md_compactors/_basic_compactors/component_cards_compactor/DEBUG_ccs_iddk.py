import sys
from pathlib import Path


_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
_DIAGNOSTICS = _PROJECT_ROOT.parent / "_output" / "Query" / "Diagnostics"
"""DEBUG CCS_ID_DK compactor: 2 edge cases + 1 random from CCS_ID_DK.db."""

import json, os, random, sqlite3, sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir))
_DB = os.path.join(_ROOT, 'card_databases_storage', 'Individual_cards_dbs', 'CCS_ID_DK.db')
_OUT = os.fspath(_DIAGNOSTICS / 'card_databases' / 'CCS_ID_DK')

sys.path.insert(0, _ROOT)
from ThermoML_card_json_to_md_compactors._basic_compactors.component_cards_compactor.ccs_iddk_compactor import compact_ccs_iddk

random.seed(42)


def _save(label, card, md):
    os.makedirs(_OUT, exist_ok=True)
    with open(os.path.join(_OUT, f'{label}.json'), 'w', encoding='utf-8') as f:
        json.dump(card, f, indent=2, ensure_ascii=False)
    with open(os.path.join(_OUT, f'{label}.md'), 'w', encoding='utf-8') as f:
        f.write(md)


def main():
    con = sqlite3.connect(_DB)
    con.row_factory = sqlite3.Row

    # Edge 1: compound with most names
    row = con.execute(
        "SELECT comp_num_id, json_data FROM cards ORDER BY length(json_data) DESC LIMIT 1"
    ).fetchone()
    card = json.loads(row['json_data'])
    md = compact_ccs_iddk(card)
    n_names = len(card.get('names', {}).get('all_names', []))
    print(f"  edge_most_names       comp#{row['comp_num_id']:>5}  names={n_names}")
    _save('edge_most_names', card, md)

    # Edge 2: synthetic-key compound (no standard InChIKey)
    row = con.execute(
        "SELECT comp_num_id, json_data FROM cards WHERE inchi_key LIKE 'NO_INCHIKEY%' LIMIT 1"
    ).fetchone()
    if row:
        card = json.loads(row['json_data'])
        md = compact_ccs_iddk(card)
        print(f"  edge_synthetic_key    comp#{row['comp_num_id']:>5}  ik={card['identity'].get('inchi_key','')[:30]}")
        _save('edge_synthetic_key', card, md)
    else:
        print("  edge_synthetic_key    SKIPPED (none found)")

    # Random 1
    all_ids = [r[0] for r in con.execute("SELECT comp_num_id FROM cards")]
    chosen = random.sample(all_ids, 1)[0]
    row = con.execute("SELECT comp_num_id, json_data FROM cards WHERE comp_num_id=?", (chosen,)).fetchone()
    card = json.loads(row['json_data'])
    md = compact_ccs_iddk(card)
    print(f"  random_1              comp#{row['comp_num_id']:>5}  name={card.get('names',{}).get('primary_name','')}")
    _save('random_1', card, md)

    con.close()
    print(f"\n  Output: {_OUT}")


if __name__ == '__main__':
    main()
