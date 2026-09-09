"""Compact a strict MTDKS card without reconstructing identifiers."""

import json
import sys
import argparse
from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_block_id,
    require_global_id,
)
from ThermoML_card_json_to_md_compactors.strict_contracts import require_payload

def _blok(val) -> str:
    return require_block_id(val)


def compact_mtdks(card: dict) -> str:
    """Convert an MTDKS card dict to compact markdown string with registry IDs."""
    card = require_payload(
        card, {"key", "methods_summary", "methods"}, context="MTDKS_INDIV card"
    )
    key = card["key"]
    doi = key["doi"]
    lit_num_id = key["lit_num_id"]
    lit_id = key["lit_id"]
    summary = card["methods_summary"]
    n = summary["n_unique_methods"]
    n_std = summary["n_standard"]
    n_cust = summary["n_custom"]
    families = summary.get("technique_families") or []

    lines = [f"# MTDKS | {doi} | {lit_num_id}", ""]
    if lit_id:
        lines.append(f"**lit_id:** {lit_id}")
    lines.append(f"**Methods:** {n} ({n_std} standard, {n_cust} custom)")

    if families:
        lines.append(f"**Families:** {', '.join(families)}")

    lines.append("")
    lines.append("| Type | meas_num_id | meas_id | Method | Properties | Block IDs | Count |")
    lines.append("|------|-------------|---------|--------|------------|-----------|-------|")

    # Sort: standard first, then custom; alphabetical within each group
    methods = sorted(card["methods"],
                     key=lambda m: (0 if m["method_type"] == "standard" else 1,
                                    m["method_name"]))

    for m in methods:
        typ = "std" if m["method_type"] == "standard" else "cust"
        meas_num = require_global_id("meas_num_id", m["meas_num_id"])
        meas_id = m["meas_id"]
        name = m["method_name"]

        # Properties with IDs
        props = m["properties"]
        if not isinstance(props, list) or any(not isinstance(p, dict) for p in props):
            raise TypeError("MTDKS method properties must be a list of objects")
        prop_parts = []
        for p in props:
            pid = require_global_id("prop_num_id", p["prop_num_id"])
            prop_parts.append(f"{pid}:{p['prop_id']}")
        prop_str = "; ".join(prop_parts)

        blocks = ",".join(_blok(b) for b in m["block_numbers"])
        count = m["instance_count"]
        lines.append(
            f"| {typ} | {meas_num} | {meas_id} | {name} | "
            f"{prop_str} | {blocks} | {count} |"
        )

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main API — fetch from DB by ID and return markdown
# ---------------------------------------------------------------------------

def get_card_md(*, doi: str = None, lit_num_id: str = None) -> str:
    """Fetch an MTDKS_INDIV card and return compact markdown.

    Provide exactly one of *doi* or *lit_num_id*.
    """
    from ThermoML_card_json_to_md_compactors._db_access import fetch_card
    if (doi is None) == (lit_num_id is None):
        raise ValueError("Provide exactly one of doi or lit_num_id")
    if doi is not None:
        card = fetch_card("MTDKS_INDIV", "doi", doi)
    else:
        card = fetch_card("MTDKS_INDIV", "lit_num_id", lit_num_id)
    return compact_mtdks(card)


def main():
    parser = argparse.ArgumentParser(description="Compact MTDKS JSON card to markdown")
    parser.add_argument("input", nargs="?", default="-",
                        help="Path to MTDKS JSON file (default: stdin)")
    parser.add_argument("-o", "--output", default=None,
                        help="Output file path (default: stdout)")
    args = parser.parse_args()

    if args.input == "-":
        card = json.load(sys.stdin)
    else:
        with open(args.input, encoding="utf-8") as f:
            card = json.load(f)

    md = compact_mtdks(card)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(md)
    else:
        print(md)


if __name__ == "__main__":
    main()
