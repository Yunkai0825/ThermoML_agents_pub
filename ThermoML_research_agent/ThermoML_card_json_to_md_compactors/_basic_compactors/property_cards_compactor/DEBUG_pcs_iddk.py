import sys
from pathlib import Path


_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
_DIAGNOSTICS = _PROJECT_ROOT.parent / "_output" / "Query" / "Diagnostics"
"""DEBUG PCS_ID_DK compactor: 2 edge cases + 1 random from PCS_ID_DK.db."""

import json, os, random, sqlite3, sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir))
_DB = os.path.join(_ROOT, 'card_databases_storage', 'Individual_cards_dbs', 'PCS_ID_DK.db')
_OUT = os.fspath(_DIAGNOSTICS / 'card_databases' / 'PCS_ID_DK')

sys.path.insert(0, _ROOT)
from ThermoML_card_json_to_md_compactors._basic_compactors.property_cards_compactor.pcs_iddk_compactor import compact_pcs_iddk

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

    # Edge 1: largest card (most DK content)
    row = con.execute(
        "SELECT prop_id, json_data FROM cards ORDER BY length(json_data) DESC LIMIT 1"
    ).fetchone()
    card = json.loads(row['json_data'])
    md = compact_pcs_iddk(card)
    print(f"  edge_largest    {row['prop_id']:<50} size={len(row['json_data']):,}B")
    _save(f"edge_largest_{row['prop_id']}", card, md)

    # Edge 2: smallest card
    row = con.execute(
        "SELECT prop_id, json_data FROM cards ORDER BY length(json_data) ASC LIMIT 1"
    ).fetchone()
    card = json.loads(row['json_data'])
    md = compact_pcs_iddk(card)
    print(f"  edge_smallest   {row['prop_id']:<50} size={len(row['json_data']):,}B")
    _save(f"edge_smallest_{row['prop_id']}", card, md)

    # Random 1
    all_ids = [r[0] for r in con.execute("SELECT prop_id FROM cards")]
    chosen = random.choice(all_ids)
    row = con.execute("SELECT prop_id, json_data FROM cards WHERE prop_id=?", (chosen,)).fetchone()
    card = json.loads(row['json_data'])
    md = compact_pcs_iddk(card)
    print(f"  random_1        {row['prop_id']:<50} size={len(row['json_data']):,}B")
    _save(f"random_1_{row['prop_id']}", card, md)

    con.close()
    print(f"\n  Output: {_OUT}")


if __name__ == '__main__':
    main()
