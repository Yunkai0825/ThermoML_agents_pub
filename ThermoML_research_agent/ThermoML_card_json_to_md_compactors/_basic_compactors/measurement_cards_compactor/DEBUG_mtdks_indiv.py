import sys
from pathlib import Path


_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
_DIAGNOSTICS = _PROJECT_ROOT.parent / "_output" / "Query" / "Diagnostics"
"""DEBUG MTDKS_INDIV compactor: 2 edge cases + 1 random from MTDKS_INDIV.db."""

import json, os, random, sqlite3, sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir))
_DB = os.path.join(_ROOT, 'card_databases_storage', 'Individual_cards_dbs', 'MTDKS_INDIV.db')
_OUT = os.fspath(_DIAGNOSTICS / 'card_databases' / 'MTDKS_INDIV')

sys.path.insert(0, _ROOT)
from ThermoML_card_json_to_md_compactors._basic_compactors.measurement_cards_compactor.mtdks_compactor import compact_mtdks

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

    # Edge 1: most methods
    row = con.execute(
        "SELECT doi, json_data FROM cards ORDER BY n_methods DESC LIMIT 1"
    ).fetchone()
    card = json.loads(row['json_data'])
    md = compact_mtdks(card)
    print(f"  edge_most_methods   {row['doi']:<45} methods={card.get('methods_summary',{}).get('n_unique_methods',0)}")
    _save(f"edge_most_methods_{row['doi'].replace('/', '_')}", card, md)

    # Edge 2: fewest methods (1)
    row = con.execute(
        "SELECT doi, json_data FROM cards ORDER BY n_methods ASC LIMIT 1"
    ).fetchone()
    card = json.loads(row['json_data'])
    md = compact_mtdks(card)
    print(f"  edge_fewest_methods {row['doi']:<45} methods={card.get('methods_summary',{}).get('n_unique_methods',0)}")
    _save(f"edge_fewest_methods_{row['doi'].replace('/', '_')}", card, md)

    # Random 1
    all_dois = [r[0] for r in con.execute("SELECT doi FROM cards")]
    chosen = random.choice(all_dois)
    row = con.execute("SELECT doi, json_data FROM cards WHERE doi=?", (chosen,)).fetchone()
    card = json.loads(row['json_data'])
    md = compact_mtdks(card)
    print(f"  random_1            {row['doi']:<45} methods={card.get('methods_summary',{}).get('n_unique_methods',0)}")
    _save(f"random_1_{row['doi'].replace('/', '_')}", card, md)

    con.close()
    print(f"\n  Output: {_OUT}")


if __name__ == '__main__':
    main()
