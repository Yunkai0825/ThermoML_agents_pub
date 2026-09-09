"""
Validation of ID coverage against raw ThermoML JSON data.

Scans all 11,923 papers' raw JSON (not relying on any pre-built DB tables)
and checks what fraction of entities in the wild are captured by the
canonical ID lists in the CSV files.

Outputs: validation_report.md under the shared _output diagnostics directory

Usage:
    python validation_raw_ThermoML.py
"""

import sqlite3
import json
import csv
import os
import sys
import time
from pathlib import Path
from collections import Counter, defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from ThermoML_raw_json_to_card_db_parsers.shared_utils import (
    slugify, meas_id_slugify, extract_var_or_constraint_type,
    extract_property_info, safe_float, canonical_compound_key,
)

HERE = os.path.dirname(os.path.abspath(__file__))
RAW_DB = os.path.join(HERE, '..', '..', '..', 'ThermoML.v2020-09-30.db', 'thermoml_raw.db')
REPORT_PATH = os.fspath(
    Path(__file__).resolve().parents[4]
    / "_output" / "Query" / "Diagnostics" / "id_coverage" / "validation_report.md"
)


# ═══════════════════════════════════════════════════════════════════════════════
#  Load CSV ID lists
# ═══════════════════════════════════════════════════════════════════════════════

def load_csv_set(filename, key_col):
    """Load a CSV and return the set of values in key_col."""
    path = os.path.join(HERE, filename)
    vals = set()
    with open(path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            vals.add(row[key_col])
    return vals


# ═══════════════════════════════════════════════════════════════════════════════
#  Scan all raw JSON
# ═══════════════════════════════════════════════════════════════════════════════

def scan_all_papers():
    """Scan every paper's raw JSON and collect all entity occurrences."""
    conn = sqlite3.connect(RAW_DB)
    papers = conn.execute("SELECT doi, json_data FROM papers").fetchall()
    conn.close()

    # Counters: how many blocks use each entity
    prop_counter    = Counter()   # prop_name -> block count
    var_counter     = Counter()   # var_name -> block count
    constr_counter  = Counter()   # constr_name -> block count
    meas_std_counter = Counter()  # method_name -> block count (standard)
    meas_cust_counter = Counter() # method_name -> block count (custom)
    compound_key_counter = Counter() # canonical compound key -> paper count
    inchi_key_counter = Counter() # real InChIKey subset -> paper count

    # Prop groups encountered
    prop_groups     = Counter()   # group_name -> block count

    # Totals
    n_papers = 0
    n_blocks = 0
    n_pm_blocks = 0
    n_rxn_blocks = 0
    n_datapoints = 0
    n_properties = 0
    n_variables = 0
    n_constraints = 0
    n_meas_std = 0
    n_meas_cust = 0
    n_meas_none = 0
    n_compounds_total = 0

    # Track papers that fail to parse
    parse_errors = []

    t0 = time.time()

    for i, (doi, json_data) in enumerate(papers):
        try:
            data = json.loads(json_data)
        except Exception as e:
            parse_errors.append((doi, f"JSON parse: {e}"))
            continue

        n_papers += 1

        # Compounds at paper level
        for comp in data.get("Compound", []):
            n_compounds_total += 1
            names = comp.get("sCommonName", [])
            if isinstance(names, str):
                names = [names]
            ik = comp.get("sStandardInChIKey")
            compound_key = canonical_compound_key(
                standard_inchi_key=ik,
                standard_inchi=comp.get("sStandardInChI"),
                common_name=names[0] if names else "",
                formula=comp.get("sFormulaMolec"),
                cas_rn=comp.get("sCASRegistryNumber"),
            )
            compound_key_counter[compound_key] += 1
            if ik:
                inchi_key_counter[ik] += 1

        # All blocks
        all_blocks = (
            [(b, "PM") for b in data.get("PureOrMixtureData", [])]
            + [(b, "Rxn") for b in data.get("ReactionData", [])]
        )

        for blk, btype in all_blocks:
            n_blocks += 1
            if btype == "PM":
                n_pm_blocks += 1
            else:
                n_rxn_blocks += 1

            n_datapoints += len(blk.get("NumValues", []))

            # Properties
            for prop in blk.get("Property", []):
                n_properties += 1
                pname, gname, method_std, method_cust = extract_property_info(prop)
                if pname:
                    prop_counter[pname] += 1
                if gname:
                    prop_groups[gname] += 1

                if method_std:
                    n_meas_std += 1
                    meas_std_counter[method_std] += 1
                elif method_cust:
                    n_meas_cust += 1
                    meas_cust_counter[method_cust] += 1
                else:
                    n_meas_none += 1

            # Variables
            for var in blk.get("Variable", []):
                n_variables += 1
                vid = var.get("VariableID", {})
                vtype_dict = vid.get("VariableType", {})
                vname, _ = extract_var_or_constraint_type(vtype_dict)
                if vname:
                    var_counter[vname] += 1

            # Constraints
            for constr in blk.get("Constraint", []):
                n_constraints += 1
                cid = constr.get("ConstraintID", {})
                ctype_dict = cid.get("ConstraintType", {})
                cname, _ = extract_var_or_constraint_type(ctype_dict)
                if cname:
                    constr_counter[cname] += 1

        if (i + 1) % 2000 == 0:
            elapsed = time.time() - t0
            print(f"  {i+1:>6d}/{len(papers)} ({(i+1)/elapsed:.0f}/s)")

    elapsed = time.time() - t0
    print(f"Scan complete: {n_papers} papers in {elapsed:.1f}s")

    return {
        "n_papers": n_papers,
        "n_blocks": n_blocks,
        "n_pm_blocks": n_pm_blocks,
        "n_rxn_blocks": n_rxn_blocks,
        "n_datapoints": n_datapoints,
        "n_properties": n_properties,
        "n_variables": n_variables,
        "n_constraints": n_constraints,
        "n_meas_std": n_meas_std,
        "n_meas_cust": n_meas_cust,
        "n_meas_none": n_meas_none,
        "n_compounds_total": n_compounds_total,
        "prop_counter": prop_counter,
        "var_counter": var_counter,
        "constr_counter": constr_counter,
        "meas_std_counter": meas_std_counter,
        "meas_cust_counter": meas_cust_counter,
        "compound_key_counter": compound_key_counter,
        "inchi_key_counter": inchi_key_counter,
        "prop_groups": prop_groups,
        "parse_errors": parse_errors,
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  Coverage check
# ═══════════════════════════════════════════════════════════════════════════════

def check_coverage(csv_set, raw_counter, id_transform=None):
    """Compare CSV ID set against raw counter.

    id_transform: function to apply to raw names to get CSV-compatible IDs.
    Returns (covered_count, total_count, covered_instances, total_instances, missing).
    """
    total_types = len(raw_counter)
    total_instances = sum(raw_counter.values())
    covered_types = 0
    covered_instances = 0
    missing = {}

    for name, count in raw_counter.items():
        lookup = id_transform(name) if id_transform else name
        if lookup in csv_set:
            covered_types += 1
            covered_instances += count
        else:
            missing[name] = count

    return covered_types, total_types, covered_instances, total_instances, missing


# ═══════════════════════════════════════════════════════════════════════════════
#  Report generator
# ═══════════════════════════════════════════════════════════════════════════════

def generate_report(scan, report_path=REPORT_PATH):
    """Generate markdown validation report."""

    # Load CSV ID sets
    prop_ids    = load_csv_set("property_ids.csv", "prop_id")
    var_ids     = load_csv_set("variable_ids.csv", "var_id")
    constr_ids  = load_csv_set("constraint_ids.csv", "constr_id")
    meas_ids    = load_csv_set("measurement_ids.csv", "meas_id")
    comp_keys   = load_csv_set("compound_ids.csv", "inchi_key")

    # Also load name-based sets for cross-ref
    prop_names  = load_csv_set("property_ids.csv", "prop_name")
    var_names   = load_csv_set("variable_ids.csv", "var_name")
    constr_names = load_csv_set("constraint_ids.csv", "constr_name")
    meas_names  = load_csv_set("measurement_ids.csv", "method_name")

    lines = []
    L = lines.append

    L("# ThermoML Index — Raw JSON Coverage Validation Report\n")
    L(f"**Source**: `thermoml_raw.db` — full scan of all raw `json_data`\n")
    L(f"**Scanned**: {scan['n_papers']:,d} papers\n")
    L("")

    # ── Global totals ──
    L("## 1. Global Totals (from raw JSON scan)\n")
    L("| Metric | Count |")
    L("|---|---:|")
    L(f"| Papers parsed | {scan['n_papers']:,d} |")
    L(f"| Total blocks | {scan['n_blocks']:,d} |")
    L(f"| — PureOrMixtureData | {scan['n_pm_blocks']:,d} |")
    L(f"| — ReactionData | {scan['n_rxn_blocks']:,d} |")
    L(f"| Total datapoints (NumValues) | {scan['n_datapoints']:,d} |")
    L(f"| Total property instances | {scan['n_properties']:,d} |")
    L(f"| Total variable instances | {scan['n_variables']:,d} |")
    L(f"| Total constraint instances | {scan['n_constraints']:,d} |")
    L(f"| Measurement — standard | {scan['n_meas_std']:,d} |")
    L(f"| Measurement — custom | {scan['n_meas_cust']:,d} |")
    L(f"| Measurement — none | {scan['n_meas_none']:,d} |")
    L(f"| Compound entries (paper-level) | {scan['n_compounds_total']:,d} |")
    L(f"| Unique canonical compound keys in raw JSON | {len(scan['compound_key_counter']):,d} |")
    L(f"| Unique property names | {len(scan['prop_counter']):,d} |")
    L(f"| Unique variable names | {len(scan['var_counter']):,d} |")
    L(f"| Unique constraint names | {len(scan['constr_counter']):,d} |")
    L(f"| Unique standard methods | {len(scan['meas_std_counter']):,d} |")
    L(f"| Unique custom methods | {len(scan['meas_cust_counter']):,d} |")
    L(f"| Unique property groups | {len(scan['prop_groups']):,d} |")
    L("")

    if scan['parse_errors']:
        L(f"\n**Parse errors**: {len(scan['parse_errors'])}")
        for doi, err in scan['parse_errors'][:5]:
            L(f"- `{doi}`: {err}")
        L("")

    # ── Per-entity coverage ──
    def coverage_section(title, num, csv_set, raw_counter, id_transform,
                         name_set, id_col_label, name_col_label):
        L(f"## {num}. {title}\n")
        ct, tt, ci, ti, missing = check_coverage(csv_set, raw_counter, id_transform)
        pct_type = (ct / tt * 100) if tt else 0
        pct_inst = (ci / ti * 100) if ti else 0

        L(f"- **CSV list**: {len(csv_set):,d} unique {id_col_label}s")
        L(f"- **Raw JSON**: {tt:,d} unique names, {ti:,d} total instances")
        L(f"- **Type coverage**: {ct:,d}/{tt:,d} ({pct_type:.1f}%)")
        L(f"- **Instance coverage**: {ci:,d}/{ti:,d} ({pct_inst:.2f}%)")
        L("")

        if missing:
            L(f"### Missing from CSV ({len(missing)}):\n")
            L(f"| {name_col_label} | Instances | {id_col_label} (would be) |")
            L("|---|---:|---|")
            for name, count in sorted(missing.items(), key=lambda x: -x[1]):
                would_be = id_transform(name) if id_transform else name
                L(f"| {name} | {count:,d} | `{would_be}` |")
            L("")

        # Full list sorted by frequency
        L(f"### Full frequency table (from raw JSON):\n")
        L(f"| Rank | {name_col_label} | Instances | In CSV? |")
        L("|---:|---|---:|:---:|")
        for rank, (name, count) in enumerate(
            sorted(raw_counter.items(), key=lambda x: -x[1]), 1
        ):
            transformed = id_transform(name) if id_transform else name
            in_csv = "✓" if transformed in csv_set else "✗"
            L(f"| {rank} | {name} | {count:,d} | {in_csv} |")
        L("")

    # 2. Properties
    coverage_section(
        "Property Coverage", "2",
        prop_ids, scan['prop_counter'], slugify,
        prop_names, "prop_id", "Property Name"
    )

    # 3. Variables
    coverage_section(
        "Variable Coverage", "3",
        var_ids, scan['var_counter'], slugify,
        var_names, "var_id", "Variable Name"
    )

    # 4. Constraints
    coverage_section(
        "Constraint Coverage", "4",
        constr_ids, scan['constr_counter'], slugify,
        constr_names, "constr_id", "Constraint Name"
    )

    # 5. Standard Measurement Methods
    coverage_section(
        "Standard Measurement Method Coverage", "5",
        meas_ids, scan['meas_std_counter'], meas_id_slugify,
        meas_names, "meas_id", "Method Name"
    )

    # 6. Compounds
    L("## 6. Compound Coverage\n")
    raw_comp_keys = scan['compound_key_counter']
    ct = len(raw_comp_keys.keys() & comp_keys)
    tt = len(raw_comp_keys)
    ci = sum(c for k, c in raw_comp_keys.items() if k in comp_keys)
    ti = sum(raw_comp_keys.values())
    pct_type = (ct / tt * 100) if tt else 0
    pct_inst = (ci / ti * 100) if ti else 0

    L(f"- **CSV list**: {len(comp_keys):,d} unique canonical compound keys")
    L(f"- **Raw JSON**: {tt:,d} unique canonical compound keys, {ti:,d} total compound entries")
    L(f"- **Type coverage**: {ct:,d}/{tt:,d} ({pct_type:.1f}%)")
    L(f"- **Instance coverage**: {ci:,d}/{ti:,d} ({pct_inst:.2f}%)")
    L("")

    missing_keys = {k: v for k, v in raw_comp_keys.items() if k not in comp_keys}
    if missing_keys:
        L(f"### Missing Compound Keys ({len(missing_keys)}):\n")
        L("| Compound Key | Paper occurrences |")
        L("|---|---:|")
        for k, v in sorted(missing_keys.items(), key=lambda x: -x[1])[:20]:
            L(f"| `{k}` | {v:,d} |")
        if len(missing_keys) > 20:
            L(f"| ... +{len(missing_keys)-20} more | |")
        L("")
    else:
        L("**All canonical compound keys from raw JSON are present in the CSV.**\n")

    # Compounds without InChIKey
    n_no_ik = scan['n_compounds_total'] - sum(scan['inchi_key_counter'].values())
    if n_no_ik > 0:
        L(f"**Note**: {n_no_ik:,d} compound entries in raw JSON have no InChIKey and are covered by fallback canonical keys.\n")
    L("")

    # 7. Property groups
    L("## 7. Property Group Distribution\n")
    L("| Rank | Group Name | Block Instances |")
    L("|---:|---|---:|")
    for rank, (gname, cnt) in enumerate(
        sorted(scan['prop_groups'].items(), key=lambda x: -x[1]), 1
    ):
        L(f"| {rank} | {gname} | {cnt:,d} |")
    L("")

    # 8. Custom methods (top 30)
    L("## 8. Custom Measurement Methods (top 30)\n")
    L("These methods have no standard `meas_id` — they are free-text author descriptions.\n")
    L("| Rank | Custom Method Name | Block Instances |")
    L("|---:|---|---:|")
    for rank, (mname, cnt) in enumerate(
        sorted(scan['meas_cust_counter'].items(), key=lambda x: -x[1])[:30], 1
    ):
        L(f"| {rank} | {mname} | {cnt:,d} |")
    total_cust = len(scan['meas_cust_counter'])
    if total_cust > 30:
        L(f"| ... | +{total_cust-30} more unique custom methods | |")
    L("")

    # 9. Summary
    L("## 9. Coverage Summary\n")
    L("| Entity | CSV Types | Raw Types | Type Coverage | Instance Coverage |")
    L("|---|---:|---:|---:|---:|")

    def summary_row(label, csv_set, raw_counter, transform=None):
        tt = len(raw_counter)
        ti = sum(raw_counter.values())
        ct = sum(1 for k in raw_counter if (transform(k) if transform else k) in csv_set)
        ci = sum(v for k, v in raw_counter.items() if (transform(k) if transform else k) in csv_set)
        return f"| {label} | {len(csv_set):,d} | {tt:,d} | {ct}/{tt} ({ct/tt*100:.1f}%) | {ci:,d}/{ti:,d} ({ci/ti*100:.2f}%) |"

    L(summary_row("Properties", prop_ids, scan['prop_counter'], slugify))
    L(summary_row("Variables", var_ids, scan['var_counter'], slugify))
    L(summary_row("Constraints", constr_ids, scan['constr_counter'], slugify))
    L(summary_row("Std Methods", meas_ids, scan['meas_std_counter'], meas_id_slugify))
    L(f"| Compounds | {len(comp_keys):,d} | {len(raw_comp_keys):,d} | {ct}/{tt} ({pct_type:.1f}%) | {ci:,d}/{ti:,d} ({pct_inst:.2f}%) |")
    L("")

    # Write report
    report_text = "\n".join(lines) + "\n"
    Path(report_path).parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_text)
    print(f"\nReport written to: {report_path}")
    print(f"Report size: {len(report_text):,d} bytes")
    return report_path


# ═══════════════════════════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print(f"Raw DB: {RAW_DB}")
    print(f"Scanning all papers...\n")
    scan = scan_all_papers()
    generate_report(scan)
