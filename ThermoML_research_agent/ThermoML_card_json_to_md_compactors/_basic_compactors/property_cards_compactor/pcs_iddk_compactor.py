"""Compact a PCS Identity/DK card (from PCS_ID_DK.db) into minimal markdown."""

from ThermoML_card_json_to_md_compactors.strict_contracts import require_payload


def compact_pcs_iddk(card: dict) -> str:
    """Convert a PCS identity/DK card dict to compact markdown.

    Expected: {"prop_ID": str, "identity": {...}, "domain_knowledge": {...}}
    """
    card = require_payload(
        card,
        {
            "card_type", "prop_num_id", "prop_ID", "base_prop_ID",
            "component_linked", "identity", "domain_knowledge",
        },
        context="PCS_ID_DK card",
    )
    prop_id = card["prop_ID"]
    ident = card["identity"]
    dk = card["domain_knowledge"]

    name = ident.get("name", prop_id)
    group = ident.get("property_group", "")
    pclass = ident.get("property_class", "")
    unit = ident.get("unit")
    symbol = ident.get("symbol")
    dimension = ident.get("dimension")

    lines = [f"# PCS-DK | {prop_id}", ""]
    lines.append(f"**Name:** {name}")
    if group:
        lines.append(f"**Group:** {group}")
    if pclass:
        lines.append(f"**Class:** {pclass}")
    if unit:
        lines.append(f"**Unit:** {unit}")
    if symbol:
        lines.append(f"**Symbol:** {symbol}")
    if dimension:
        lines.append(f"**Dimension:** {dimension}")

    # Boolean flags
    flags = []
    for flag in ("is_intensive", "is_molar", "is_excess", "is_partial", "is_apparent"):
        if ident.get(flag):
            flags.append(flag.replace("is_", ""))
    if flags:
        lines.append(f"**Flags:** {', '.join(flags)}")

    # Typical variables
    tvars = ident.get("typical_variables", [])
    if tvars:
        parts = [f"{v['var_name']} ({v.get('usage_fraction', 0):.0%})"
                 for v in tvars[:5]]
        lines.append(f"**Typical vars:** {'; '.join(parts)}")

    # Typical constraints
    tcons = ident.get("typical_constraints", [])
    if tcons:
        parts = [f"{c.get('constr_name', c.get('var_name', '?'))} ({c.get('usage_fraction', 0):.0%})"
                 for c in tcons[:5]]
        lines.append(f"**Typical constrs:** {'; '.join(parts)}")

    # DB usage
    usage = ident.get("db_usage", {})
    if usage:
        uparts = []
        if usage.get("total_instances") is not None:
            uparts.append(f"{usage['total_instances']} instances")
        if usage.get("n_papers") is not None:
            uparts.append(f"{usage['n_papers']} papers")
        if usage.get("rank_overall") is not None:
            uparts.append(f"rank #{usage['rank_overall']}")
        if uparts:
            lines.append(f"**Usage:** {' | '.join(uparts)}")

        methods = usage.get("common_methods", [])
        if methods:
            mparts = [f"{m['method_name']} ({m.get('fraction', 0):.0%})"
                      for m in methods[:3]]
            lines.append(f"**Top methods:** {'; '.join(mparts)}")

    # Domain knowledge — structured block
    sb = dk.get("structured_block", {})
    if sb:
        lines.append("")
        lines.append("## Structured Knowledge")
        for section, content in sb.items():
            if isinstance(content, dict):
                flat = []
                for k, v in content.items():
                    if isinstance(v, (str, int, float, bool)):
                        flat.append(f"{k}={v}")
                    elif isinstance(v, list) and v:
                        flat.append(f"{k}=[{', '.join(str(x) for x in v[:5])}]")
                if flat:
                    lines.append(f"- **{section}:** {'; '.join(flat)}")
            elif isinstance(content, str) and content:
                lines.append(f"- **{section}:** {content[:120]}")

    # Domain knowledge — description block (section names + first line)
    db_ = dk.get("description_block", {})
    if db_:
        lines.append("")
        lines.append("## Description Sections")
        for section, text in db_.items():
            if isinstance(text, str) and text.strip():
                first_line = text.strip().split("\n")[0][:120]
                lines.append(f"- **{section}:** {first_line}")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main API — fetch from DB by ID and return markdown
# ---------------------------------------------------------------------------

def get_card_md(*, prop_num_id: str = None, prop_id: str = None) -> str:
    """Fetch a PCS_ID_DK card and return compact markdown.

    Provide exactly one of *prop_num_id* or *prop_id*.
    """
    from ThermoML_card_json_to_md_compactors._db_access import fetch_card
    if (prop_num_id is None) == (prop_id is None):
        raise ValueError("Provide exactly one of prop_num_id or prop_id")
    if prop_num_id is not None:
        card = fetch_card("PCS_ID_DK", "prop_num_id", prop_num_id)
    else:
        card = fetch_card("PCS_ID_DK", "prop_id", prop_id)
    return compact_pcs_iddk(card)
