"""Compact an RMS (Reference Metadata Schema) JSON card into minimal markdown."""

import json
import sys
import argparse
from ThermoML_card_json_to_md_compactors.strict_contracts import require_payload
from ThermoML_raw_json_to_card_db_parsers.id_schema import require_global_id


def _last_name(author: str) -> str:
    """Extract last name from 'Last, F.' or 'Last, F.[Full]' format."""
    return author.split(",")[0].strip()


def _bool_yn(val) -> str:
    if val is True:
        return "yes"
    if val is False:
        return "no"
    return ""


def _fmt_range(rng: dict | None, unit: str) -> str | None:
    if not rng:
        return None
    lo, hi = rng.get("min"), rng.get("max")
    if lo is None and hi is None:
        return None
    if lo == hi:
        return f"{lo} {unit}"
    return f"{lo}-{hi} {unit}"


def compact_rms(card: dict) -> str:
    """Convert a parsed RMS card dict into a compact markdown string with registry IDs."""
    card = require_payload(
        card,
        {"identity", "bibliographic", "content", "data_inventory"},
        context="RMS_INDIV card",
    )
    ident = card["identity"]
    bib = card["bibliographic"]
    content = card["content"]
    inv = card["data_inventory"]

    doi = ident["doi"]
    lit_num_id = ident["lit_num_id"]
    lit_id = ident["lit_id"]
    lines: list[str] = [f"# RMS | {doi} | {lit_num_id}", ""]
    if lit_id:
        lines.append(f"**lit_id:** {lit_id}")

    # --- Bibliographic header ---
    if bib.get("title"):
        lines.append(f"**Title:** {bib['title']}")
    authors = bib.get("authors") or []
    if authors:
        lines.append(f"**Authors:** {'; '.join(_last_name(a) for a in authors)}")
    journal_parts = [p for p in [
        bib.get("journal"),
        str(bib["year"]) if bib.get("year") else None,
    ] if p]
    vol_str = bib.get("volume") or ""
    if bib.get("pages"):
        vol_str += f":{bib['pages']}"
    if bib.get("issue_number"):
        vol_str += f" (#{bib['issue_number']})"
    if vol_str:
        journal_parts.append(vol_str)
    if journal_parts:
        lines.append(f"**Journal:** {' '.join(journal_parts)}")
    source_parts = [p for p in [bib.get("source_type"), None] if p]
    if bib.get("citation_date"):
        source_parts.append(f"Cited: {bib['citation_date']}")
    if source_parts:
        lines.append(f"**Source:** {' | '.join(source_parts)}")
    lines.append("")

    # --- Abstract ---
    abstract = content.get("abstract")
    if abstract:
        lines.append("## Abstract")
        lines.append(abstract)
        lines.append("")

    # --- Keywords ---
    keywords = content.get("keywords") or []
    if keywords:
        lines.append("## Keywords")
        lines.append("; ".join(keywords))
        lines.append("")

    # --- Data Inventory table ---
    lines.append("## Data Inventory")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    rows: list[tuple[str, str]] = []
    if inv.get("n_compounds") is not None:
        rows.append(("Compounds", str(inv["n_compounds"])))
    if inv.get("n_blocks") is not None:
        rows.append(("Blocks", str(inv["n_blocks"])))
    if inv.get("n_datapoints") is not None:
        rows.append(("Datapoints", str(inv["n_datapoints"])))
    pm = _bool_yn(inv.get("has_pure_or_mixture_data"))
    if pm:
        rows.append(("Has P/M data", pm))
    rx = _bool_yn(inv.get("has_reaction_data"))
    if rx:
        rows.append(("Has reaction", rx))
    t_range = _fmt_range(inv.get("temperature_range_K"), "K")
    if t_range:
        rows.append(("T range", t_range))
    p_range = _fmt_range(inv.get("pressure_range_kPa"), "kPa")
    if p_range:
        rows.append(("P range", p_range))
    for label, val in rows:
        lines.append(f"| {label} | {val} |")
    lines.append("")

    # --- Compounds table ---
    compounds = inv.get("compound_list") or []
    if compounds:
        lines.append("### Compounds")
        hdr = ["comp_id", "Name", "IK"]
        has_formula = any(c.get("formula") for c in compounds)
        if has_formula:
            hdr.append("Formula")
        lines.append("| " + " | ".join(hdr) + " |")
        lines.append("|" + "|".join("---" for _ in hdr) + "|")
        for c in compounds:
            cid = require_global_id("comp_num_id", c["comp_num_id"])
            row = [
                cid,
                c.get("name", ""),
                c.get("inchi_key", "")[:20] if c.get("inchi_key") else "",
            ]
            if has_formula:
                row.append(c.get("formula") or "")
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")

    # --- Properties ---
    props = inv.get("properties") or []
    if props:
        lines.append("### Properties")
        if props and isinstance(props[0], dict):
            for p in props:
                pn = require_global_id("prop_num_id", p["prop_num_id"])
                pid = p["prop_id"]
                pname = p["name"]
                lines.append(f"- {pn} | {pid} | {pname}")
        else:
            for p in props:
                lines.append(f"- {p}")
        lines.append("")

    # --- Property Groups ---
    groups = inv.get("property_groups") or []
    if groups:
        lines.append("### Property Groups")
        lines.append("; ".join(groups))
        lines.append("")

    # --- System Types ---
    sys_types = inv.get("system_types") or []
    if sys_types:
        lines.append("### System Types")
        lines.append("; ".join(sys_types))
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main API — fetch from DB by ID and return markdown
# ---------------------------------------------------------------------------

def get_card_md(*, doi: str = None, lit_num_id: str = None) -> str:
    """Fetch an RMS_INDIV card and return compact markdown.

    Provide exactly one of *doi* or *lit_num_id*.
    """
    from ThermoML_card_json_to_md_compactors._db_access import fetch_card
    if (doi is None) == (lit_num_id is None):
        raise ValueError("Provide exactly one of doi or lit_num_id")
    if doi is not None:
        card = fetch_card("RMS_INDIV", "doi", doi)
    else:
        card = fetch_card("RMS_INDIV", "lit_num_id", lit_num_id)
    return compact_rms(card)


def main():
    parser = argparse.ArgumentParser(description="Compact an RMS JSON card to markdown.")
    parser.add_argument("input", nargs="?", help="Path to RMS JSON file (reads stdin if omitted)")
    parser.add_argument("-o", "--output", help="Write markdown to this file instead of stdout")
    args = parser.parse_args()

    if args.input:
        with open(args.input, encoding="utf-8") as f:
            card = json.load(f)
    else:
        card = json.load(sys.stdin)

    md = compact_rms(card)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(md)
    else:
        print(md)


if __name__ == "__main__":
    main()
