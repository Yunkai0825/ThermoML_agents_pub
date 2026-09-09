from pathlib import Path
"""
Master compactor test: feed deterministic examples from every current card DB
through its compactor, plus 2 edge + 1 random rows from each registry DB.

Writes JSON+MD pairs under the shared _output diagnostics directory,
in sub-directories per DB / compactor.

Usage (from ThermoML_research_agent):
    python ThermoML_card_json_to_md_compactors/_entry_by_entry_validator/run_all_compactor_tests.py
"""

import json, os, random, shutil, sqlite3, sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
sys.path.insert(0, _ROOT)

_DIAGNOSTIC_ROOT = (
    Path(__file__).resolve().parents[3]
    / "_output" / "Query" / "Diagnostics" / "compactor_tests"
)
_OUT_BASE = os.fspath(_DIAGNOSTIC_ROOT / "compactor_test_output")
_IC = os.path.join(_ROOT, 'card_databases_storage', 'Individual_cards_dbs')
_CD = os.path.join(_ROOT, 'card_databases_storage')

random.seed(42)

# ── imports ───────────────────────────────────────────────────────────────
from ThermoML_card_json_to_md_compactors._basic_compactors.component_cards_compactor.ccs_compactor import compact_ccs
from ThermoML_card_json_to_md_compactors._basic_compactors.component_cards_compactor.ccs_iddk_compactor import compact_ccs_iddk
from ThermoML_card_json_to_md_compactors._basic_compactors.measurement_cards_compactor.mtdks_compactor import compact_mtdks
from ThermoML_card_json_to_md_compactors._basic_compactors.measurement_cards_compactor.mtdks_iddk_compactor import compact_mtdks_iddk
from ThermoML_card_json_to_md_compactors._basic_compactors.property_cards_compactor.pcs_compactor import compact_pcs
from ThermoML_card_json_to_md_compactors._basic_compactors.property_cards_compactor.pcs_iddk_compactor import compact_pcs_iddk
from ThermoML_card_json_to_md_compactors._basic_compactors.reference_cards_compactor.rms_compactor import compact_rms
from ThermoML_card_json_to_md_compactors._basic_compactors.registry_cards_compactor.registry_block_compactor import compact_pm_registry, compact_rxn_registry
from ThermoML_card_json_to_md_compactors._basic_compactors.registry_cards_compactor.registry_paper_compactor import compact_pm_paper, compact_rxn_paper


# ── helpers ───────────────────────────────────────────────────────────────

def _save(out_dir, label, card_or_row, md_text):
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f'{label}.json'), 'w', encoding='utf-8') as f:
        json.dump(card_or_row, f, indent=2, ensure_ascii=False)
    with open(os.path.join(out_dir, f'{label}.md'), 'w', encoding='utf-8') as f:
        f.write(md_text)


def _load_card_db_jsons(db_name):
    """Load deterministic first/middle/last cards from a current card DB."""
    db_path = os.path.join(_IC, f"{db_name}.db")
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    try:
        total = con.execute("SELECT count(*) FROM cards").fetchone()[0]
        if total < 1:
            raise RuntimeError(f"{db_name}.db contains no cards")
        offsets = sorted({0, total // 2, total - 1})
        items = []
        for offset in offsets:
            row = con.execute(
                "SELECT rowid, json_data FROM cards ORDER BY rowid LIMIT 1 OFFSET ?",
                (offset,),
            ).fetchone()
            if row is None or not row["json_data"]:
                raise RuntimeError(f"{db_name}.db row at offset {offset} has no JSON")
            card = json.loads(row["json_data"])
            if not isinstance(card, dict):
                raise TypeError(f"{db_name}.db row {row['rowid']} JSON is not an object")
            items.append((f"row_{row['rowid']}", card))
        return items
    finally:
        con.close()


def _row_to_dict(row):
    return {k: row[k] for k in row.keys()}


def _reset_output_root():
    """Remove only this harness's generated output from preceding runs."""
    output_root = Path(_OUT_BASE).resolve()
    expected_parent = _DIAGNOSTIC_ROOT.resolve()
    if output_root.parent != expected_parent or output_root.name != "compactor_test_output":
        raise RuntimeError(f"Refusing to clear unexpected output directory: {output_root}")
    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True, exist_ok=False)


# ── 1. CCS_ID_DK ─────────────────────────────────────────────────────────

def test_ccs_iddk():
    out = os.path.join(_OUT_BASE, 'CCS_ID_DK')
    items = _load_card_db_jsons('CCS_ID_DK')
    print(f"\n=== CCS_ID_DK ({len(items)} cards) ===")
    for label, card in items:
        md = compact_ccs_iddk(card)
        _save(out, label, card, md)
        print(f"  {label:<55} {len(md):>5} chars")


# ── 2. CCS_INDIV ─────────────────────────────────────────────────────────

def test_ccs_indiv():
    out = os.path.join(_OUT_BASE, 'CCS_INDIV')
    items = _load_card_db_jsons('CCS_INDIV')
    print(f"\n=== CCS_INDIV ({len(items)} cards) ===")
    for label, card in items:
        md = compact_ccs(card)
        _save(out, label, card, md)
        print(f"  {label:<55} {len(md):>5} chars")


# ── 3. MTDKS_ID_DK (standard + registry stubs) ──────────────────────────

def test_mtdks_iddk():
    out = os.path.join(_OUT_BASE, 'MTDKS_ID_DK')
    items = _load_card_db_jsons('MTDKS_ID_DK')
    print(f"\n=== MTDKS_ID_DK — current DB cards ({len(items)}) ===")

    # Open DB once for the additional current-schema custom-stub examples.
    db_path = os.path.join(_IC, 'MTDKS_ID_DK.db')
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row

    for label, card in items:
        md = compact_mtdks_iddk(card)
        _save(out, label, card, md)
        ct = card.get('card_type', 'standard_dk')
        print(f"  {label:<55} {ct:<14} {len(md):>5} chars")

    # Extra: 2 edge + 1 random registry stubs from the current DB.
    # (reuse the same `con` opened above)

    # Edge: largest custom stub (most instances)
    row = con.execute("""
        SELECT meas_id, meas_num_id, json_data FROM cards
        WHERE card_type = 'registry_stub'
        ORDER BY json_extract(json_data, '$.identity.db_usage.instance_count') DESC
        LIMIT 1
    """).fetchone()
    if row is None:
        raise RuntimeError("MTDKS_ID_DK.db has no registry_stub cards")
    card = json.loads(row['json_data'])
    md = compact_mtdks_iddk(card)
    lbl = f"registry_edge_most_inst_{row['meas_id']}"
    _save(out, lbl, card, md)
    inst = card['identity']['db_usage']['instance_count']
    print(f"  {lbl:<55} registry_stub  {len(md):>5} chars  inst={inst}")

    # Edge: smallest custom stub (fewest instances)
    row = con.execute("""
        SELECT meas_id, meas_num_id, json_data FROM cards
        WHERE card_type = 'registry_stub'
        ORDER BY json_extract(json_data, '$.identity.db_usage.instance_count') ASC
        LIMIT 1
    """).fetchone()
    if row is None:
        raise RuntimeError("MTDKS_ID_DK.db has no registry_stub cards")
    card = json.loads(row['json_data'])
    md = compact_mtdks_iddk(card)
    lbl = f"registry_edge_least_inst_{row['meas_id']}"
    _save(out, lbl, card, md)
    inst = card['identity']['db_usage']['instance_count']
    print(f"  {lbl:<55} registry_stub  {len(md):>5} chars  inst={inst}")

    # Random registry stub
    all_stubs = [r[0] for r in con.execute(
        "SELECT meas_id FROM cards WHERE card_type='registry_stub'")]
    if not all_stubs:
        raise RuntimeError("MTDKS_ID_DK.db has no registry_stub cards")
    chosen = random.choice(all_stubs)
    row = con.execute("SELECT meas_id, meas_num_id, json_data FROM cards WHERE meas_id=?",
                      (chosen,)).fetchone()
    if row is None:
        raise RuntimeError(f"Selected MTDKS_ID_DK registry stub disappeared: {chosen}")
    card = json.loads(row['json_data'])
    md = compact_mtdks_iddk(card)
    lbl = f"registry_random_{row['meas_id']}"
    _save(out, lbl, card, md)
    print(f"  {lbl:<55} registry_stub  {len(md):>5} chars")

    con.close()


# ── 4. MTDKS_INDIV ───────────────────────────────────────────────────────

def test_mtdks_indiv():
    out = os.path.join(_OUT_BASE, 'MTDKS_INDIV')
    items = _load_card_db_jsons('MTDKS_INDIV')
    print(f"\n=== MTDKS_INDIV ({len(items)} cards) ===")
    for label, card in items:
        md = compact_mtdks(card)
        _save(out, label, card, md)
        print(f"  {label:<55} {len(md):>5} chars")


# ── 5. PCS_ID_DK ─────────────────────────────────────────────────────────

def test_pcs_iddk():
    out = os.path.join(_OUT_BASE, 'PCS_ID_DK')
    items = _load_card_db_jsons('PCS_ID_DK')
    print(f"\n=== PCS_ID_DK ({len(items)} cards) ===")
    for label, card in items:
        md = compact_pcs_iddk(card)
        _save(out, label, card, md)
        print(f"  {label:<55} {len(md):>5} chars")


# ── 6. PCS_INDIV ─────────────────────────────────────────────────────────

def test_pcs_indiv():
    out = os.path.join(_OUT_BASE, 'PCS_INDIV')
    items = _load_card_db_jsons('PCS_INDIV')
    print(f"\n=== PCS_INDIV ({len(items)} cards) ===")
    for label, card in items:
        md = compact_pcs(card)
        _save(out, label, card, md)
        print(f"  {label:<55} {len(md):>5} chars")


# ── 7. RMS_INDIV ─────────────────────────────────────────────────────────

def test_rms_indiv():
    out = os.path.join(_OUT_BASE, 'RMS_INDIV')
    items = _load_card_db_jsons('RMS_INDIV')
    print(f"\n=== RMS_INDIV ({len(items)} cards) ===")
    for label, card in items:
        md = compact_rms(card)
        _save(out, label, card, md)
        print(f"  {label:<55} {len(md):>5} chars")


# ── 8. PM_REGISTRY ───────────────────────────────────────────────────────

def test_pm_registry():
    out = os.path.join(_OUT_BASE, 'PM_REGISTRY')
    db_path = os.path.join(_CD, 'PureOrMixtureData_registry.db')
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    print(f"\n=== PM_REGISTRY ===")

    # Edge 1: most datapoints
    row = con.execute(
        "SELECT * FROM block_registry ORDER BY n_datapoints DESC LIMIT 1"
    ).fetchone()
    d = _row_to_dict(row)
    md = compact_pm_registry(d)
    lbl = f"edge_most_pts_{d['doi'].replace('/', '_')}_blk{d['block_number']}"
    _save(out, lbl, d, md)
    print(f"  {lbl:<55} pts={d['n_datapoints']:>5}  {len(md):>5} chars")

    # Edge 2: most components
    row = con.execute(
        "SELECT * FROM block_registry ORDER BY n_components DESC LIMIT 1"
    ).fetchone()
    d = _row_to_dict(row)
    md = compact_pm_registry(d)
    lbl = f"edge_most_compounds_{d['doi'].replace('/', '_')}_blk{d['block_number']}"
    _save(out, lbl, d, md)
    print(f"  {lbl:<55} comp={d['n_components']:>3}  {len(md):>5} chars")

    # Random 1
    total = con.execute("SELECT count(*) FROM block_registry").fetchone()[0]
    offset = random.randint(0, total - 1)
    row = con.execute("SELECT * FROM block_registry LIMIT 1 OFFSET ?", (offset,)).fetchone()
    d = _row_to_dict(row)
    md = compact_pm_registry(d)
    lbl = f"random_{d['doi'].replace('/', '_')}_blk{d['block_number']}"
    _save(out, lbl, d, md)
    print(f"  {lbl:<55} pts={d['n_datapoints']:>5}  {len(md):>5} chars")

    con.close()


# ── 9. RXN_REGISTRY ──────────────────────────────────────────────────────

def test_rxn_registry():
    out = os.path.join(_OUT_BASE, 'RXN_REGISTRY')
    db_path = os.path.join(_CD, 'ReactionData_registry.db')
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    print(f"\n=== RXN_REGISTRY ===")

    # Edge 1: most components
    row = con.execute(
        "SELECT * FROM block_registry ORDER BY n_components DESC LIMIT 1"
    ).fetchone()
    d = _row_to_dict(row)
    md = compact_rxn_registry(d)
    lbl = f"edge_most_compounds_{d['doi'].replace('/', '_')}_blk{d['block_number']}"
    _save(out, lbl, d, md)
    print(f"  {lbl:<55} comp={d['n_components']:>3}  {len(md):>5} chars")

    # Edge 2: most datapoints
    row = con.execute(
        "SELECT * FROM block_registry ORDER BY n_datapoints DESC LIMIT 1"
    ).fetchone()
    d = _row_to_dict(row)
    md = compact_rxn_registry(d)
    lbl = f"edge_most_pts_{d['doi'].replace('/', '_')}_blk{d['block_number']}"
    _save(out, lbl, d, md)
    print(f"  {lbl:<55} pts={d['n_datapoints']:>5}  {len(md):>5} chars")

    # Random 1
    total = con.execute("SELECT count(*) FROM block_registry").fetchone()[0]
    offset = random.randint(0, total - 1)
    row = con.execute("SELECT * FROM block_registry LIMIT 1 OFFSET ?", (offset,)).fetchone()
    d = _row_to_dict(row)
    md = compact_rxn_registry(d)
    lbl = f"random_{d['doi'].replace('/', '_')}_blk{d['block_number']}"
    _save(out, lbl, d, md)
    print(f"  {lbl:<55} pts={d['n_datapoints']:>5}  {len(md):>5} chars")

    con.close()


# ── 10. PM_REGISTRY_PAPER ────────────────────────────────────────────────

def test_pm_registry_paper():
    out = os.path.join(_OUT_BASE, 'PM_REGISTRY_PAPER')
    db_path = os.path.join(_CD, 'PureOrMixtureData_registry.db')
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    print(f"\n=== PM_REGISTRY_PAPER ===")

    # Edge 1: paper with most blocks
    top_doi = con.execute(
        "SELECT doi, count(*) as n FROM block_registry GROUP BY doi ORDER BY n DESC LIMIT 1"
    ).fetchone()
    rows = [_row_to_dict(r) for r in con.execute(
        "SELECT * FROM block_registry WHERE doi=? ORDER BY block_number", (top_doi[0],))]
    md = compact_pm_paper(rows)
    lbl = f"edge_most_blocks_{top_doi[0].replace('/', '_')}"
    _save(out, lbl, rows, md)
    print(f"  {lbl:<55} blks={len(rows):>4}  {len(md):>6} chars")

    # Edge 2: paper with most total datapoints
    top_pts_doi = con.execute(
        "SELECT doi, sum(n_datapoints) as s FROM block_registry GROUP BY doi ORDER BY s DESC LIMIT 1"
    ).fetchone()
    rows = [_row_to_dict(r) for r in con.execute(
        "SELECT * FROM block_registry WHERE doi=? ORDER BY block_number", (top_pts_doi[0],))]
    md = compact_pm_paper(rows)
    lbl = f"edge_most_pts_{top_pts_doi[0].replace('/', '_')}"
    _save(out, lbl, rows, md)
    pts = sum(r['n_datapoints'] for r in rows)
    print(f"  {lbl:<55} pts={pts:>6}  {len(md):>6} chars")

    # Random 1
    all_dois = [r[0] for r in con.execute("SELECT DISTINCT doi FROM block_registry")]
    chosen = random.choice(all_dois)
    rows = [_row_to_dict(r) for r in con.execute(
        "SELECT * FROM block_registry WHERE doi=? ORDER BY block_number", (chosen,))]
    md = compact_pm_paper(rows)
    lbl = f"random_{chosen.replace('/', '_')}"
    _save(out, lbl, rows, md)
    print(f"  {lbl:<55} blks={len(rows):>4}  {len(md):>6} chars")

    con.close()


# ── 11. RXN_REGISTRY_PAPER ───────────────────────────────────────────────

def test_rxn_registry_paper():
    out = os.path.join(_OUT_BASE, 'RXN_REGISTRY_PAPER')
    db_path = os.path.join(_CD, 'ReactionData_registry.db')
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    print(f"\n=== RXN_REGISTRY_PAPER ===")

    # Edge 1: paper with most blocks
    top_doi = con.execute(
        "SELECT doi, count(*) as n FROM block_registry GROUP BY doi ORDER BY n DESC LIMIT 1"
    ).fetchone()
    rows = [_row_to_dict(r) for r in con.execute(
        "SELECT * FROM block_registry WHERE doi=? ORDER BY block_number", (top_doi[0],))]
    md = compact_rxn_paper(rows)
    lbl = f"edge_most_blocks_{top_doi[0].replace('/', '_')}"
    _save(out, lbl, rows, md)
    print(f"  {lbl:<55} blks={len(rows):>4}  {len(md):>6} chars")

    # Edge 2: paper with most total datapoints
    top_pts_doi = con.execute(
        "SELECT doi, sum(n_datapoints) as s FROM block_registry GROUP BY doi ORDER BY s DESC LIMIT 1"
    ).fetchone()
    rows = [_row_to_dict(r) for r in con.execute(
        "SELECT * FROM block_registry WHERE doi=? ORDER BY block_number", (top_pts_doi[0],))]
    md = compact_rxn_paper(rows)
    lbl = f"edge_most_pts_{top_pts_doi[0].replace('/', '_')}"
    _save(out, lbl, rows, md)
    pts = sum(r['n_datapoints'] for r in rows)
    print(f"  {lbl:<55} pts={pts:>6}  {len(md):>6} chars")

    # Random 1
    all_dois = [r[0] for r in con.execute("SELECT DISTINCT doi FROM block_registry")]
    chosen = random.choice(all_dois)
    rows = [_row_to_dict(r) for r in con.execute(
        "SELECT * FROM block_registry WHERE doi=? ORDER BY block_number", (chosen,))]
    md = compact_rxn_paper(rows)
    lbl = f"random_{chosen.replace('/', '_')}"
    _save(out, lbl, rows, md)
    print(f"  {lbl:<55} blks={len(rows):>4}  {len(md):>6} chars")

    con.close()


# ── main ──────────────────────────────────────────────────────────────────

def main():
    _reset_output_root()
    print("=" * 70)
    print("  MASTER COMPACTOR TEST — Diagnostics cards + Registry DBs")
    print("=" * 70)

    # 7 card compactors fed from Diagnostics JSONs
    test_ccs_iddk()
    test_ccs_indiv()
    test_mtdks_iddk()
    test_mtdks_indiv()
    test_pcs_iddk()
    test_pcs_indiv()
    test_rms_indiv()

    # 2 block-level registry compactors from DBs
    test_pm_registry()
    test_rxn_registry()

    # 2 paper-level registry compactors from DBs
    test_pm_registry_paper()
    test_rxn_registry_paper()

    # tally
    total_files = 0
    for dirpath, dirnames, filenames in os.walk(_OUT_BASE):
        total_files += len(filenames)
    n_dirs = len([d for d in os.listdir(_OUT_BASE) if os.path.isdir(os.path.join(_OUT_BASE, d))])

    print("\n" + "=" * 70)
    print(f"  DONE — {n_dirs} subdirs, {total_files} files in {_OUT_BASE}")
    print("=" * 70)


if __name__ == '__main__':
    main()
