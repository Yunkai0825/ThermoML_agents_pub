"""Compact a CCS (Component Card Schema) JSON card into minimal markdown."""

import json
import sys

from ThermoML_raw_json_to_card_db_parsers.id_schema import require_global_id
from ThermoML_card_json_to_md_compactors.strict_contracts import require_payload


def _fmt_purity(value, digits, label):
    """Format a purity value with appropriate decimal places."""
    if value is None:
        return None
    if digits is not None and digits >= 1:
        # digits = significant figures in the original; render enough decimals
        fmt = f"{value:.{max(0, digits - len(str(int(value))))}f}"
    else:
        fmt = f"{value:g}"
    return f"{label}={fmt}%"


def _summarise_steps(purity_steps):
    """Collapse purity_steps into (purity_str, purification[], analysis[], impurities_str)."""
    if not purity_steps:
        return None, [], [], None

    # Collect all purification and analysis methods across steps (preserve order, dedupe)
    purification = []
    analysis = []
    seen_pur = set()
    seen_ana = set()
    for step in purity_steps:
        for m in step.get("purification_methods") or []:
            if m not in seen_pur:
                purification.append(m)
                seen_pur.add(m)
        for m in step.get("analysis_methods") or []:
            if m not in seen_ana:
                analysis.append(m)
                seen_ana.add(m)

    # Find the FINAL (highest step) purity value; prefer mol > mass > vol
    purity_str = None
    for step in reversed(purity_steps):
        p = step.get("purity") or {}
        candidate = (
            _fmt_purity(p.get("mol_fraction"), p.get("mol_fraction_digits"), "mol")
            or _fmt_purity(p.get("mass_fraction"), p.get("mass_fraction_digits"), "mass")
            or _fmt_purity(p.get("vol_fraction"), p.get("vol_fraction_digits"), "vol")
        )
        if candidate:
            purity_str = candidate
            break

    # Collect impurities from the LAST step that has any
    impurities_parts = []
    for step in reversed(purity_steps):
        imp = step.get("impurities") or {}
        w = imp.get("water_mass_pct")
        h = imp.get("halide_mass_pct")
        if w is not None:
            wd = imp.get("water_mass_pct_digits")
            fmt = f"{w:.{max(0, (wd or 1) - (len(str(int(w))) if w >= 1 else 0))}f}" if wd else f"{w:g}"
            impurities_parts.append(f"water={fmt}% (mass)")
        if h is not None:
            hd = imp.get("halide_mass_pct_digits")
            fmt = f"{h:.{max(0, (hd or 1) - (len(str(int(h))) if h >= 1 else 0))}f}" if hd else f"{h:g}"
            impurities_parts.append(f"halide={fmt}% (mass)")
        if impurities_parts:
            break

    impurities_str = "; ".join(impurities_parts) if impurities_parts else None
    return purity_str, purification, analysis, impurities_str


def compact_ccs(card: dict) -> str:
    """Convert a CCS JSON card dict into compact markdown table with canonical IDs."""
    card = require_payload(card, {"key", "compounds"}, context="CCS_INDIV card")
    key = card["key"]
    doi = key["doi"]
    lit_num_id = key["lit_num_id"]
    lit_id = key["lit_id"]
    compounds = card["compounds"]

    lines = [f"# CCS | {doi} | {lit_num_id}", ""]
    if lit_id:
        lines.append(f"**lit_id:** {lit_id}")
    lines.append(f"**Compounds:** {len(compounds)}")

    # --- collect row data for every compound × sample ---
    rows = []  # list of dicts with fixed keys
    for comp in compounds:
        comp_num_id = comp["comp_num_id"]
        inchi_key = comp.get("inchi_key", "")
        name = comp.get("name", "")
        cid = require_global_id("comp_num_id", comp_num_id)
        samples = comp.get("samples") or []

        if not samples:
            rows.append({"comp_id": cid, "Name": name, "Sample": "",
                         "InChIKey": inchi_key, "Source": "", "Status": "",
                         "Purity": "", "Purification": "", "Analysis": "",
                         "Impurities": ""})
            continue

        for sample in samples:
            sample_num = str(sample.get("sample_num", ""))
            source = sample.get("source") or ""
            status = sample.get("status") or ""
            if status == "notDescribed":
                status = ""
            purity_str, purification, analysis, impurities_str = _summarise_steps(
                sample.get("purity_steps"))
            rows.append({
                "comp_id": cid,
                "Name": name,
                "Sample": sample_num,
                "InChIKey": inchi_key,
                "Source": source,
                "Status": status,
                "Purity": purity_str or "",
                "Purification": "; ".join(purification) if purification else "",
                "Analysis": "; ".join(analysis) if analysis else "",
                "Impurities": impurities_str or "",
            })

    # --- determine which optional columns to include ---
    # Always: comp_id, Name
    always_cols = ["comp_id", "Name"]
    optional_cols = ["Sample", "InChIKey", "Source", "Status",
                     "Purity", "Purification", "Analysis", "Impurities"]
    active_optional = [c for c in optional_cols if any(r[c] for r in rows)]
    cols = always_cols + active_optional

    # --- build markdown table ---
    lines.append("")
    lines.append("| " + " | ".join(cols) + " |")
    lines.append("| " + " | ".join("---" for _ in cols) + " |")
    for r in rows:
        lines.append("| " + " | ".join(r[c] for c in cols) + " |")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main API — fetch from DB by ID and return markdown
# ---------------------------------------------------------------------------

def get_card_md(*, doi: str = None, lit_num_id: str = None) -> str:
    """Fetch a CCS_INDIV card and return compact markdown.

    Provide exactly one of *doi* or *lit_num_id*.
    """
    from ThermoML_card_json_to_md_compactors._db_access import fetch_card
    if (doi is None) == (lit_num_id is None):
        raise ValueError("Provide exactly one of doi or lit_num_id")
    if doi is not None:
        card = fetch_card("CCS_INDIV", "doi", doi)
    else:
        card = fetch_card("CCS_INDIV", "lit_num_id", lit_num_id)
    return compact_ccs(card)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Compact a CCS JSON card to markdown")
    parser.add_argument("input", nargs="?", help="Path to CCS JSON file (default: stdin)")
    parser.add_argument("-o", "--output", help="Output file path (default: stdout)")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            card = json.load(f)
    else:
        card = json.load(sys.stdin)

    md = compact_ccs(card)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(md)
    else:
        print(md)


if __name__ == "__main__":
    main()
