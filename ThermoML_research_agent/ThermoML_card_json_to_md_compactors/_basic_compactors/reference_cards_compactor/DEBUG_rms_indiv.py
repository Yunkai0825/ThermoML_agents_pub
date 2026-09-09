import sys
from pathlib import Path


_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
_DIAGNOSTICS = _PROJECT_ROOT.parent / "_output" / "Query" / "Diagnostics"
"""DEBUG RMS_INDIV compactor: 2 edge cases + 1 random from RMS_INDIV.db."""

import json, os, random, sqlite3, sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir))
_DB = os.path.join(_ROOT, 'card_databases_storage', 'Individual_cards_dbs', 'RMS_INDIV.db')
_OUT = os.fspath(_DIAGNOSTICS / 'card_databases' / 'RMS_INDIV')

sys.path.insert(0, _ROOT)
from ThermoML_card_json_to_md_compactors._basic_compactors.reference_cards_compactor.rms_compactor import compact_rms

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

    # Edge 1: most compounds
    row = con.execute(
        "SELECT doi, json_data FROM cards ORDER BY n_compounds DESC LIMIT 1"
    ).fetchone()
    card = json.loads(row['json_data'])
    md = compact_rms(card)
    print(f"  edge_most_compounds {row['doi']:<45} comp={card.get('data_inventory',{}).get('n_compounds',0)}")
    _save(f"edge_most_compounds_{row['doi'].replace('/', '_')}", card, md)

    # Edge 2: most blocks
    row = con.execute(
        "SELECT doi, json_data FROM cards ORDER BY n_blocks DESC LIMIT 1"
    ).fetchone()
    card = json.loads(row['json_data'])
    md = compact_rms(card)
    print(f"  edge_most_blocks    {row['doi']:<45} blocks={card.get('data_inventory',{}).get('n_blocks',0)}")
    _save(f"edge_most_blocks_{row['doi'].replace('/', '_')}", card, md)

    # Random 1
    all_dois = [r[0] for r in con.execute("SELECT doi FROM cards")]
    chosen = random.choice(all_dois)
    row = con.execute("SELECT doi, json_data FROM cards WHERE doi=?", (chosen,)).fetchone()
    card = json.loads(row['json_data'])
    md = compact_rms(card)
    print(f"  random_1            {row['doi']:<45} comp={card.get('data_inventory',{}).get('n_compounds',0)}")
    _save(f"random_1_{row['doi'].replace('/', '_')}", card, md)

    con.close()
    print(f"\n  Output: {_OUT}")


if __name__ == '__main__':
    main()
