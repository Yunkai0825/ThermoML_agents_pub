"""PCS compactor — DOI-level property card compaction.

pcs_doi_summary(card) -> dict
    DOI-level structured summary (NOT markdown). Contains all registry IDs
    for cross-referencing with other cards and the registry.

compact_pcs(card) -> str
    Full DOI compact markdown (summary tables + block index).

Per-block rendering lives in block_compactor.py.
"""

import json
import sys
import io
from ThermoML_card_json_to_md_compactors.strict_contracts import require_payload
from ThermoML_raw_json_to_card_db_parsers.id_schema import require_global_id


_REQUIRED_BLOCK_FIELDS = {
    "block_number", "block_type", "system_type", "blocktype_num_id",
    "compounds", "properties", "solvents", "variables", "constraints",
    "data_summary", "data_points", "reaction", "auxiliary", "equation",
    "provenance",
}


def _require_block(block):
    return require_payload(block, _REQUIRED_BLOCK_FIELDS, context="PCS block")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _blok(val) -> str:
    from ThermoML_raw_json_to_card_db_parsers.id_schema import require_block_id
    return require_block_id(val)


def _short_type(bt):
    if bt == "PureOrMixtureData":
        return "P/M"
    if bt == "ReactionData":
        return "Rxn"
    return bt


# ---------------------------------------------------------------------------
# DOI-level summary (dict, NOT markdown)
# ---------------------------------------------------------------------------

def pcs_doi_summary(card):
    """Return a structured dict summarising the entire PCS card for a DOI.

    No markdown — purely machine-readable. Contains all registry IDs.
    """
    card = require_payload(
        card, {"key", "paper", "blocks_summary", "blocks"},
        context="PCS_INDIV card",
    )
    key = card["key"]
    paper = card["paper"]
    bs = card["blocks_summary"]
    blocks = card["blocks"]

    # Collect unique compounds across all blocks
    seen_comp = {}
    for raw_block in blocks:
        b = _require_block(raw_block)
        for c in b["compounds"]:
            org = c["org_num"]
            if org not in seen_comp:
                seen_comp[org] = {
                    "org_num": org,
                    "comp_num_id": require_global_id("comp_num_id", c["comp_num_id"]),
                    "inchi_key": c["inchi_key"],
                    "name": c.get("name", ""),
                    "formula": c.get("formula", ""),
                }

    # Collect unique properties across all blocks
    seen_prop = {}
    for raw_block in blocks:
        b = _require_block(raw_block)
        for p in b["properties"]:
            pname = p["name"]
            if pname not in seen_prop:
                seen_prop[pname] = {
                    "name": pname,
                    "prop_num_id": require_global_id("prop_num_id", p["prop_num_id"]),
                    "prop_ID": p["prop_ID"],
                    "group": p["group"],
                }

    # Collect unique methods
    seen_meas = {}
    for raw_block in blocks:
        b = _require_block(raw_block)
        for p in b["properties"]:
            meas_id = p["meas_ID"]
            if meas_id and meas_id not in seen_meas:
                seen_meas[meas_id] = {
                    "meas_num_id": require_global_id("meas_num_id", p["meas_num_id"]),
                    "meas_ID": meas_id,
                    "method_standard": p.get("method_standard"),
                    "method_custom": p.get("method_custom"),
                }

    # Block index with IDs
    block_index = []
    for raw_block in blocks:
        b = _require_block(raw_block)
        bn = _blok(b["block_number"])
        ds = b["data_summary"]
        props_in_block = []
        for p in b["properties"]:
            props_in_block.append({
                "name": p["name"],
                "prop_num_id": require_global_id("prop_num_id", p["prop_num_id"]),
                "prop_ID": p["prop_ID"],
                "meas_num_id": require_global_id("meas_num_id", p["meas_num_id"]),
            })
        comp_ids_in_block = [
            require_global_id("comp_num_id", c["comp_num_id"])
            for c in b["compounds"]
        ]
        block_index.append({
            "block_number": bn,
            "block_type": b["block_type"],
            "system_type": b["system_type"],
            "n_points": ds["n_points"],
            "properties": props_in_block,
            "compound_ids": comp_ids_in_block,
        })

    return {
        "doi": key["doi"],
        "lit_num_id": key["lit_num_id"],
        "lit_id": key["lit_id"],
        "title": paper.get("title", ""),
        "n_blocks": bs["n_blocks"],
        "n_pure_or_mixture": bs["n_pure_or_mixture"],
        "n_reaction": bs["n_reaction"],
        "total_datapoints": bs["total_datapoints"],
        "temperature_range_K": bs.get("temperature_range_K"),
        "pressure_range_kPa": bs.get("pressure_range_kPa"),
        "compounds": list(seen_comp.values()),
        "properties": list(seen_prop.values()),
        "methods": list(seen_meas.values()),
        "system_types": bs.get("system_types", []),
        "property_groups": bs.get("property_groups", []),
        "block_index": block_index,
    }


# ---------------------------------------------------------------------------
# Full DOI compact markdown
# ---------------------------------------------------------------------------

def compact_pcs(card):
    """Convert a PCS card to compact markdown (summary + all blocks).

    For new code, prefer pcs_doi_summary() + pcs_block_compact() separately.
    """
    card = require_payload(
        card, {"key", "paper", "blocks_summary", "blocks"},
        context="PCS_INDIV card",
    )
    key = card["key"]
    paper = card["paper"]
    doi = key["doi"]
    lit_num_id = key["lit_num_id"]
    lit_id = key["lit_id"]

    title = paper.get("title", "")

    lines = [f"# PCS | {doi} | {lit_num_id}"]
    lines.append("")
    if lit_id:
        lines.append(f"**lit_id:** {lit_id}")
    if title:
        lines.append(f"**Title:** {title}")
    if lit_id or title:
        lines.append("")

    # Inline summary
    summary = pcs_doi_summary(card)

    # ── Data Inventory table (mirrors RMS_INDIV style) ──
    n_comps = len(summary.get("compounds", []))
    has_pm = "yes" if summary["n_pure_or_mixture"] > 0 else "no"
    has_rxn = "yes" if summary["n_reaction"] > 0 else "no"

    lines.append("## Data Inventory")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Compounds | {n_comps} |")
    lines.append(f"| Blocks | {summary['n_blocks']} ({summary['n_pure_or_mixture']} P/M, {summary['n_reaction']} Rxn) |")
    lines.append(f"| Datapoints | {summary['total_datapoints']} |")
    lines.append(f"| Has P/M data | {has_pm} |")
    lines.append(f"| Has reaction | {has_rxn} |")

    t_range = summary.get("temperature_range_K")
    p_range = summary.get("pressure_range_kPa")
    if t_range:
        lines.append(f"| T range | {t_range.get('min')}-{t_range.get('max')} K |")
    if p_range:
        lines.append(f"| P range | {p_range.get('min')}-{p_range.get('max')} kPa |")

    sys_types = summary.get("system_types") or []
    if sys_types:
        lines.append(f"| System types | {', '.join(sys_types)} |")
    prop_groups = summary.get("property_groups") or []
    if prop_groups:
        lines.append(f"| Property groups | {', '.join(prop_groups)} |")
    lines.append("")

    # Compounds table (DOI-level)
    comps = summary.get("compounds", [])
    if comps:
        comps_sorted = sorted(comps, key=lambda c: c["comp_num_id"])
        lines.append("## Compounds")
        lines.append("| comp_num_id | Name | Formula |")
        lines.append("|---|---|---|")
        for c in comps_sorted:
            cid = require_global_id("comp_num_id", c["comp_num_id"])
            name = c.get("name", "")
            formula = c.get("formula", "")
            lines.append(f"| {cid} | {name} | {formula} |")
        lines.append("")

    blocks = card["blocks"]

    # Build org_num -> compound info lookup for INDIV-level component resolution
    _indiv_org_map = {}
    for raw_block in blocks:
        b = _require_block(raw_block)
        for c in b["compounds"]:
            org = c["org_num"]
            if org and org not in _indiv_org_map:
                _indiv_org_map[org] = {
                    "comp_num_id": require_global_id("comp_num_id", c["comp_num_id"]),
                    "name": c.get("name", ""),
                    "formula": c.get("formula", ""),
                }

    # Preserve distinct component-resolved occurrences of one global type.
    prop_entries = {}
    for raw_block in blocks:
        b = _require_block(raw_block)
        for p in b["properties"]:
            pid = require_global_id("prop_num_id", p["prop_num_id"])
            prop_entries[(pid, p["prop_ID"])] = p
    if prop_entries:
        lines.append("## Properties")
        lines.append("| prop_num_id | Property | Group |")
        lines.append("|---|---|---|")
        for (pid, resolved_prop_id), p in sorted(prop_entries.items()):
            prop_ID = resolved_prop_id
            group = p.get("group", "")
            lines.append(f"| {pid} | {prop_ID} | {group} |")
        lines.append("")

    # --- Measurements table (DOI-level) ---
    meas_map = {}
    for raw_block in blocks:
        b = _require_block(raw_block)
        for p in b["properties"]:
            mid = require_global_id("meas_num_id", p["meas_num_id"])
            if mid not in meas_map:
                meas_map[mid] = {
                    "meas_ID": p["meas_ID"],
                    "method_standard": p.get("method_standard", ""),
                    "method_custom": p.get("method_custom", ""),
                }
    if meas_map:
        lines.append("## Measurements")
        lines.append("| meas_num_id | meas_id | Method |")
        lines.append("|---|---|---|")
        for mid in sorted(meas_map):
            info = meas_map[mid]
            method = info["meas_ID"] or info["method_standard"] or info["method_custom"] or ""
            lines.append(f"| {mid} | {info['meas_ID']} | {method} |")
        lines.append("")

    # --- Variables table (DOI-level, merge identical var_num_id) ---
    var_entries = {}
    for raw_block in blocks:
        b = _require_block(raw_block)
        for v in b["variables"]:
            vid = require_global_id("var_num_id", v["var_num_id"])
            var_entries[(vid, v["var_id"])] = v
    if var_entries:
        lines.append("## Variables")
        lines.append("| var_num_id | Variable | Phase |")
        lines.append("|---|---|---|")
        for (vid, resolved_var_id), v in sorted(var_entries.items()):
            var_id_display = resolved_var_id
            vph = (v.get("phase") or {}).get("phase", "")
            lines.append(f"| {vid} | {var_id_display} | {vph} |")
        lines.append("")

    # --- Constraints table (DOI-level, merge identical constr_num_id) ---
    constr_entries = {}
    for raw_block in blocks:
        b = _require_block(raw_block)
        for c in b["constraints"]:
            cid = require_global_id("constr_num_id", c["constr_num_id"])
            constr_entries[(cid, c["constr_id"])] = c
    if constr_entries:
        lines.append("## Constraints")
        lines.append("| constr_num_id | Constraint | Phase |")
        lines.append("|---|---|---|")
        for (cid, resolved_constr_id), c in sorted(constr_entries.items()):
            constr_id_display = resolved_constr_id
            cph = (c.get("phase") or {}).get("phase", "")
            lines.append(f"| {cid} | {constr_id_display} | {cph} |")
        lines.append("")

    # Block summary table
    if blocks:
        lines.append("## Blocks")
        lines.append("| block | type | system | pts | compounds | props | meas | vars | constrs |")
        lines.append("|---|---|---|---:|---|---|---|---|---|")
        for raw_block in blocks:
            b = _require_block(raw_block)
            bn = _blok(b["block_number"])
            bt = _short_type(b["block_type"])
            ds = b["data_summary"]
            stype = b["system_type"]
            npts = ds["n_points"]

            comp_refs = [
                f"{c['org_num']}→{c['comp_num_id']}"
                for c in b["compounds"]
            ]
            c_str = ", ".join(comp_refs) if comp_refs else "—"

            prop_items = []
            for p in b["properties"]:
                pid = require_global_id("prop_num_id", p["prop_num_id"])
                label = f"{p['BLKprop_id']}→{pid}"
                if p["component_org_num"]:
                    label += f"@{p['component_org_num']}"
                prop_items.append(label)

            # Measurements — canonical GLOBmeas_N identifiers.
            meas_items = []
            for p in b["properties"]:
                mid = require_global_id("meas_num_id", p["meas_num_id"])
                meas_items.append(mid)

            # Variables — canonical GLOBvar_N plus optional DOIcomp_N reference.
            var_items = []
            for v in b["variables"]:
                vid = require_global_id("var_num_id", v["var_num_id"])
                label = f"{v['BLKvar_id']}→{vid}"
                if v["component_org_num"]:
                    label += f"@{v['component_org_num']}"
                var_items.append(label)

            # Constraints — canonical GLOBconstr_N plus optional DOIcomp_N reference.
            constr_items = []
            for c in b["constraints"]:
                cid = require_global_id("constr_num_id", c["constr_num_id"])
                label = f"{c['BLKconstr_id']}→{cid}"
                if c["component_org_num"]:
                    label += f"@{c['component_org_num']}"
                constr_items.append(label)

            p_str = ", ".join(sorted(set(prop_items))) if prop_items else "—"
            m_str = ", ".join(sorted(set(meas_items))) if meas_items else "—"
            v_str = ", ".join(sorted(set(var_items))) if var_items else "—"
            cs_str = ", ".join(sorted(set(constr_items))) if constr_items else "—"
            lines.append(f"| {bn} | {bt} | {stype} | {npts} | {c_str} | {p_str} | {m_str} | {v_str} | {cs_str} |")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Main API — fetch from DB by ID and return markdown
# ---------------------------------------------------------------------------

def get_card_md(*, doi: str = None, lit_num_id: str = None) -> str:
    """Fetch a PCS_INDIV card and return compact markdown.

    Provide exactly one of *doi* or *lit_num_id*.
    """
    from ThermoML_card_json_to_md_compactors._db_access import fetch_card
    if (doi is None) == (lit_num_id is None):
        raise ValueError("Provide exactly one of doi or lit_num_id")
    if doi is not None:
        card = fetch_card("PCS_INDIV", "doi", doi)
    else:
        card = fetch_card("PCS_INDIV", "lit_num_id", lit_num_id)
    return compact_pcs(card)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Compact a PCS JSON card. Use --summary for dict output."
    )
    parser.add_argument(
        "input", nargs="?", default="-",
        help="Path to PCS JSON file (default: stdin)"
    )
    parser.add_argument(
        "-o", "--output", default=None,
        help="Output file path (default: stdout)"
    )
    parser.add_argument(
        "--summary", action="store_true",
        help="Output DOI-level summary as JSON instead of markdown"
    )
    args = parser.parse_args()

    if args.input == "-":
        data = json.load(sys.stdin)
    else:
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)

    if args.summary:
        result = json.dumps(pcs_doi_summary(data), indent=2, ensure_ascii=False)
    else:
        result = compact_pcs(data)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        out = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
        out.write(result)
        out.flush()


if __name__ == "__main__":
    main()
