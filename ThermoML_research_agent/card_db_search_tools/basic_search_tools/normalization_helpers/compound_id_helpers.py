"""Compound ID resolution in variable/property/constraint ID strings.

Translates ``DOIcomp_N`` references into human-readable ``<compound_name>``
placeholders for column headers and metadata display.
"""

import re

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    block_local_ordinal,
    require_doi_comp_id,
)


def resolve_comp_in_id(raw_id: str, cmap: dict) -> str:
    """Replace compound references in an ID string with <compound_name>.

    Handles two patterns:
      1. ``DOIcomp_N``       -> ``<compound_name>``
      2. ``{DOIcomp_id}``    -> rejected in an occurrence card; templates
                               belong only in the global registry

    Examples:
        "mole_fraction_DOIcomp_19"     -> "mole_fraction_<heptane>"
        "temperature_k"                -> "temperature_k" (no comp ref)
    """
    def _sub_comp_n(m):
        key = f"DOIcomp_{m.group(1)}"
        name = cmap.get(key)
        if not name:
            raise ValueError(
                f"Component occurrence {key!r} is absent from the DOI compound map"
            )
        return f"<{name}>"
    result = re.sub(r'DOIcomp_(\d+)', _sub_comp_n, raw_id)
    if '{DOIcomp_id}' in result:
        raise ValueError(f"Unresolved global component template in block occurrence: {raw_id!r}")

    return result


def build_column_map(block: dict, cmap: dict | None = None) -> dict:
    """Build strict BLK-local ID -> human-readable column name mapping.

    All ``DOIcomp_N`` references are resolved to ``<compound_name>`` using
    the provided compound map.

    Returns dict like:
        {"BLKvar_1": "temperature_k",
         "BLKvar_2": "mole_fraction_<ethanol>",
         "BLKprop_1": "mass_density_kg_m3", ...}
    """
    if cmap is None:
        cmap = {}
    col_map = {}

    for field in ("variables", "properties", "constraints"):
        if field not in block or not isinstance(block[field], list):
            raise ValueError(f"block requires array field {field!r}")

    for v in block["variables"]:
        local_id = v["BLKvar_id"]
        block_local_ordinal("var", local_id)
        col_map[local_id] = resolve_comp_in_id(v["var_id"], cmap)

    for p in block["properties"]:
        local_id = p["BLKprop_id"]
        block_local_ordinal("prop", local_id)
        col_map[local_id] = resolve_comp_in_id(p["prop_ID"], cmap)

    for c in block["constraints"]:
        local_id = c["BLKconstr_id"]
        block_local_ordinal("constr", local_id)
        col_map[local_id] = resolve_comp_in_id(c["constr_id"], cmap)

    return col_map


def build_compound_map(block: dict, card: dict = None) -> dict:
    """Build DOIcomp_N -> compound name mapping.

    Component-resolved IDs use the paper's own ``DOIcomp_N`` namespace and
    never a ``GLOBcomp_N`` value.

    Only the DOI namespace is eligible. Global IDs and positional aliases are
    intentionally not accepted as substitutes.

    Returns dict like:
        {"DOIcomp_1": "hexane", "DOIcomp_2": "ethanol", ...}
    """
    cmap = {}

    def _put(key, name):
        checked = require_doi_comp_id(key)
        if not name:
            raise ValueError(f"Compound occurrence {checked!r} has no display name")
        if checked not in cmap:
            cmap[checked] = name

    if "compounds" not in block or not isinstance(block["compounds"], list):
        raise ValueError("block requires a compounds array")
    block_comps = block["compounds"]

    # 1. Current block's org_num — the namespace var/prop refs actually use
    for c in block_comps:
        if not isinstance(c, dict) or "org_num" not in c or "name" not in c:
            raise ValueError("every block compound requires org_num and name")
        _put(c["org_num"], c["name"])

    # Card-wide DOI occurrence coverage for cross-block references.
    if card:
        if "blocks" not in card or not isinstance(card["blocks"], list):
            raise ValueError("card requires a blocks array")
        for blk in card["blocks"]:
            if "compounds" not in blk or not isinstance(blk["compounds"], list):
                raise ValueError("every card block requires a compounds array")
            for c in blk["compounds"]:
                if not isinstance(c, dict) or "org_num" not in c or "name" not in c:
                    raise ValueError("every card compound requires org_num and name")
                _put(c["org_num"], c["name"])

    return cmap


def extract_comp_ref(id_str: str, cmap: dict) -> str:
    """Extract compound name from an ID string containing ``DOIcomp_N``.

    E.g. ``mole_fraction_DOIcomp_1`` -> ``cmap['DOIcomp_1']`` -> methane
    """
    m = re.search(r'DOIcomp_(\d+)', id_str or "")
    if m:
        key = require_doi_comp_id(f"DOIcomp_{m.group(1)}")
        if key not in cmap:
            raise ValueError(
                f"Component occurrence {key!r} is absent from the DOI compound map"
            )
        return cmap[key]
    return ""
