"""Compact a CCS Identity card (from CCS_ID_DK.db) into minimal markdown."""

from ThermoML_card_json_to_md_compactors.strict_contracts import require_payload


def compact_ccs_iddk(card: dict) -> str:
    """Convert a CCS identity card dict to compact markdown.

    Expected input: {"comp_num_id": "GLOBcomp_N", "identity": {...}, "names": {...}}
    """
    card = require_payload(
        card, {"comp_num_id", "identity", "names"}, context="CCS_ID_DK card"
    )
    cid = card["comp_num_id"]
    ident = card["identity"]
    names = card["names"]

    primary = names.get("primary_name", "")
    all_names = names.get("all_names", [])
    ik = ident.get("inchi_key", "")
    formula = ident.get("formula", "")
    smiles = ident.get("SMILES")
    inchi = ident.get("InChI")

    lines = [f"# CCS-ID | {cid} | {primary}"]

    if formula:
        lines.append(f"- **Formula:** {formula}")
    if ik:
        lines.append(f"- **IK:** {ik}")
    if smiles:
        lines.append(f"- **SMILES:** {smiles}")
    if inchi:
        lines.append(f"- **InChI:** {inchi}")

    if len(all_names) > 1:
        lines.append(f"- **Names ({len(all_names)}):** {'; '.join(all_names[:10])}")
        if len(all_names) > 10:
            lines[-1] += f" ... (+{len(all_names) - 10} more)"
    elif all_names:
        lines.append(f"- **Names:** {all_names[0]}")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main API — fetch from DB by ID and return markdown
# ---------------------------------------------------------------------------

def get_card_md(*, comp_num_id: str) -> str:
    """Fetch a CCS_ID_DK card and return compact markdown."""
    from ThermoML_card_json_to_md_compactors._db_access import fetch_card
    card = fetch_card("CCS_ID_DK", "comp_num_id", comp_num_id)
    return compact_ccs_iddk(card)
