import sys
from pathlib import Path


_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
_DIAGNOSTICS = _PROJECT_ROOT.parent / "_output" / "Query" / "Diagnostics"
"""DEBUG ReactionData registry compactor: 2 edge cases + 1 random."""

import json, os, random, sqlite3, sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir))
_DB = os.path.join(_ROOT, 'card_databases_storage', 'ReactionData_registry.db')
_OUT = os.fspath(_DIAGNOSTICS / 'card_databases' / 'RXN_REGISTRY')

sys.path.insert(0, _ROOT)
from ThermoML_card_json_to_md_compactors._basic_compactors.registry_cards_compactor.registry_block_compactor import compact_rxn_registry

random.seed(42)


def _row_to_dict(row):
    return {k: row[k] for k in row.keys()}


def _save(label, row_dict, md):
    os.makedirs(_OUT, exist_ok=True)
    with open(os.path.join(_OUT, f'{label}.json'), 'w', encoding='utf-8') as f:
        json.dump(row_dict, f, indent=2, ensure_ascii=False)
    with open(os.path.join(_OUT, f'{label}.md'), 'w', encoding='utf-8') as f:
        f.write(md)


def main():
    con = sqlite3.connect(_DB)
    con.row_factory = sqlite3.Row

    # Edge 1: most components in a reaction block
    row = con.execute(
        "SELECT * FROM block_registry ORDER BY n_components DESC LIMIT 1"
    ).fetchone()
    d = _row_to_dict(row)
    md = compact_rxn_registry(d)
    print(f"  edge_most_comp  {d['doi']:<40} blk#{d['block_number']}  comp={d['n_components']}")
    _save(f"edge_most_compounds_{d['doi'].replace('/', '_')}_blk{d['block_number']}", d, md)

    # Edge 2: most datapoints in a reaction block
    row = con.execute(
        "SELECT * FROM block_registry ORDER BY n_datapoints DESC LIMIT 1"
    ).fetchone()
    d = _row_to_dict(row)
    md = compact_rxn_registry(d)
    print(f"  edge_most_pts   {d['doi']:<40} blk#{d['block_number']}  pts={d['n_datapoints']}")
    _save(f"edge_most_pts_{d['doi'].replace('/', '_')}_blk{d['block_number']}", d, md)

    # Random 1
    total = con.execute("SELECT count(*) FROM block_registry").fetchone()[0]
    offset = random.randint(0, total - 1)
    row = con.execute("SELECT * FROM block_registry LIMIT 1 OFFSET ?", (offset,)).fetchone()
    d = _row_to_dict(row)
    md = compact_rxn_registry(d)
    print(f"  random_1        {d['doi']:<40} blk#{d['block_number']}  pts={d['n_datapoints']}")
    _save(f"random_1_{d['doi'].replace('/', '_')}_blk{d['block_number']}", d, md)

    con.close()
    print(f"\n  Output: {_OUT}")


if __name__ == '__main__':
    main()
