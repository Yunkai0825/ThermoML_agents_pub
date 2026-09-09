"""Compact an MTDKS Identity/DK card (from MTDKS_ID_DK.db) into minimal markdown."""

from ThermoML_card_json_to_md_compactors.strict_contracts import require_payload


def _fmt_modality(mod: dict) -> str:
    return ", ".join(f"{k}={v}" for k, v in mod.items() if v)


def _fmt_usage(usage: dict) -> str:
    parts = []
    n = usage.get("instance_count")
    if n is not None:
        parts.append(f"{n} instances")
    np_ = usage.get("n_papers")
    if np_ is not None:
        parts.append(f"{np_} papers")
    groups = usage.get("property_groups", [])
    if groups:
        parts.append(f"groups={','.join(groups)}")
    return " | ".join(parts) if parts else ""


def _fmt_dict_item(d: dict) -> str:
    """Format a dict (e.g. target_property, constraint, variable) as a compact line."""
    # target_properties: {name, property_group, unit, description}
    if "name" in d and "unit" in d:
        desc = d.get("description", "")
        group = d.get("property_group", "")
        role = d.get("role", "")
        parts = [d["name"]]
        if group:
            parts.append(group)
        if role:
            parts.append(role)
        parts.append(d["unit"])
        line = " | ".join(parts)
        if desc:
            line += f" — {desc}"
        return line
    # constraints/variables: {parameter/name, typical_range, ...}
    label = d.get("parameter") or d.get("name", "?")
    tr = d.get("typical_range") or d.get("typical_values", "")
    hl = d.get("hard_limits", "")
    effect = d.get("effect", "")
    notes = d.get("notes", "")
    parts = [f"**{label}**"]
    if tr:
        parts.append(f"typical: {tr}")
    if hl:
        parts.append(f"limits: {hl}")
    if effect:
        parts.append(f"effect: {effect}")
    if notes:
        parts.append(f"notes: {notes}")
    return " — ".join(parts)


def _fmt_field(lines: list, key: str, value, indent: str = ""):
    """Append formatted lines for a single field within a structured section."""
    if isinstance(value, str) and value:
        lines.append(f"{indent}**{key}:** {value}")
    elif isinstance(value, (int, float, bool)):
        lines.append(f"{indent}**{key}:** {value}")
    elif isinstance(value, list) and value:
        if isinstance(value[0], dict):
            lines.append(f"{indent}**{key}:**")
            for item in value:
                lines.append(f"{indent}- {_fmt_dict_item(item)}")
        else:
            lines.append(f"{indent}**{key}:**")
            for item in value:
                lines.append(f"{indent}- {item}")
    elif isinstance(value, dict) and value:
        lines.append(f"{indent}**{key}:**")
        for k, v in value.items():
            if isinstance(v, str):
                lines.append(f"{indent}- {k}: {v}")
            else:
                lines.append(f"{indent}- {k}: {v}")


def compact_mtdks_iddk(card: dict) -> str:
    """Convert an MTDKS identity/DK card dict to compact markdown.

    Expected: {"meas_ID": str, "identity": {...}, "domain_knowledge": {...}}
    """
    card = require_payload(
        card,
        {"card_type", "meas_ID", "meas_num_id", "identity", "domain_knowledge"},
        context="MTDKS_ID_DK card",
    )
    meas_id = card["meas_ID"]
    meas_num = card["meas_num_id"]
    ident = card["identity"]
    dk = card["domain_knowledge"]

    name = ident.get("name", meas_id)
    family = ident.get("measurement_family", "")
    acronym = ident.get("acronym", "")
    aliases = ident.get("aliases", [])
    modality = ident.get("modality", {})
    usage = ident.get("db_usage", {})

    hdr = f"# MTDKS-DK | {meas_id}"
    if meas_num is not None:
        hdr += f" | {meas_num}"
    lines = [hdr, ""]
    lines.append(f"**Name:** {name}")
    if family:
        lines.append(f"**Family:** {family}")
    if acronym:
        lines.append(f"**Acronym:** {acronym}")
    if aliases:
        lines.append(f"**Aliases:** {'; '.join(aliases)}")

    # ThermoML codes
    std_name = ident.get("thermoml_standard_name", "")
    custom_codes = ident.get("thermoml_custom_codes", [])
    if std_name:
        lines.append(f"**ThermoML std:** {std_name}")
    if custom_codes:
        lines.append(f"**Custom codes:** {', '.join(custom_codes)}")

    if modality:
        lines.append(f"**Modality:** {_fmt_modality(modality)}")

    usage_str = _fmt_usage(usage)
    if usage_str:
        lines.append(f"**Usage:** {usage_str}")

    # Per-group breakdown
    per_group = usage.get("per_group", {})
    if per_group:
        gparts = [f"{g}: {v.get('instances',0)} inst/{v.get('papers',0)} papers"
                   for g, v in per_group.items()]
        lines.append(f"**Per-group:** {'; '.join(gparts)}")

    # Domain knowledge — structured block with subsections
    dk = dk or {}
    sb = dk.get("structured_block", {})
    if sb:
        lines.append("")
        lines.append("## Structured Knowledge")
        for section, content in sb.items():
            lines.append("")
            lines.append(f"### {section}")
            if isinstance(content, dict):
                for k, v in content.items():
                    _fmt_field(lines, k, v)
            elif isinstance(content, str) and content:
                lines.append(content)

    # Domain knowledge — description block with subsections
    db_ = dk.get("description_block", {})
    if db_:
        lines.append("")
        lines.append("## Description")
        for section, text in db_.items():
            if isinstance(text, str) and text.strip():
                lines.append("")
                lines.append(f"### {section}")
                lines.append(text.strip())

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main API — fetch from DB by ID and return markdown
# ---------------------------------------------------------------------------

def get_card_md(*, meas_num_id: str = None, meas_id: str = None) -> str:
    """Fetch an MTDKS_ID_DK card and return compact markdown.

    Provide exactly one of *meas_num_id* or *meas_id*.
    """
    from ThermoML_card_json_to_md_compactors._db_access import fetch_card
    if (meas_num_id is None) == (meas_id is None):
        raise ValueError("Provide exactly one of meas_num_id or meas_id")
    if meas_num_id is not None:
        card = fetch_card("MTDKS_ID_DK", "meas_num_id", meas_num_id)
    else:
        card = fetch_card("MTDKS_ID_DK", "meas_id", meas_id)
    return compact_mtdks_iddk(card)
