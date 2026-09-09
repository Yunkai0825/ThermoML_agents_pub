"""Block-level compactor — renders a single PCS block as compact markdown.

Contains ``pcs_block_compact()`` which renders per-block tables (compounds,
properties, variables, constraints, data) plus ``compact_block()`` which
wraps it with RDP topology compaction.

Each block card contains:
  - Header: block_number, type, system, npts, lit#
  - Compounds table
  - Properties table (with method, phase, component)
  - Variables table
  - Constraints table
  - Phases, StdState, Ref, Uncertainty, Solvent, Provenance
  - Topology annotation (RDP curve classification + compression ratio)
  - Data-points table (RDP-simplified)

Usage:
    compact_block(block_dict, key_info=None, compounds_map=None) -> str
"""

import json
import os
import sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     os.pardir, os.pardir, os.pardir))
sys.path.insert(0, _ROOT)

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    block_local_ordinal,
    require_block_id,
    require_block_local_id,
    require_doi_comp_id,
    require_global_id,
)
from ThermoML_card_json_to_md_compactors._data_points_compaction_topology.rdp_topology import (
    compact_block_data,
)
from ThermoML_card_json_to_md_compactors.strict_contracts import require_payload

_REQUIRED_BLOCK_FIELDS = {
    "block_number", "block_type", "system_type", "blocktype_num_id",
    "compounds", "properties", "solvents", "variables", "constraints",
    "data_summary", "data_points", "reaction", "auxiliary", "equation",
    "provenance",
}


# ---------------------------------------------------------------------------
# Block-only helpers (moved from pcs_compactor)
# ---------------------------------------------------------------------------

def _build_org_map(compounds):
    return {c["org_num"]: c for c in compounds}


def _build_compounds_map(compounds):
    return {
        c["org_num"]: c.get("name") or c.get("formula") or c["org_num"]
        for c in compounds
    }


def _blok(value):
    return require_block_id(value)


def _short_type(block_type):
    return "P/M" if block_type == "PureOrMixtureData" else "Rxn"


def _format_value(val):
    if val is None:
        return ""
    if isinstance(val, float):
        return repr(val)
    return str(val)


def _resolve_comp_name(org_num, org_map):
    """Resolve an org_num to its common name (comp_id)."""
    if not org_num:
        return None
    info = org_map.get(org_num)
    if info:
        return info.get("name") or info.get("formula") or str(org_num)
    return None


def _short_col(name, var_or_prop, comp_org_num, compounds_map, phase=None):
    """Generate abbreviated column header for the data table."""
    nl = name.lower()

    comp_label = ""
    if comp_org_num and compounds_map and comp_org_num in compounds_map:
        comp_label = compounds_map[comp_org_num]

    solvent_prefix = ""
    bare_nl = nl
    if nl.startswith("solvent:"):
        solvent_prefix = "s:"
        bare_nl = nl[len("solvent:"):].strip()

    def _comp_tag():
        parts = [p for p in [comp_label, phase] if p]
        return ",".join(parts)

    if "mole fraction" in bare_nl:
        tag = _comp_tag()
        return f"{solvent_prefix}x({tag})" if tag else f"{solvent_prefix}x"

    if "mass fraction" in bare_nl:
        tag = _comp_tag()
        return f"{solvent_prefix}w({tag})" if tag else f"{solvent_prefix}w"

    if "volume fraction" in bare_nl:
        tag = _comp_tag()
        return f"{solvent_prefix}\u03c6_v({tag})" if tag else f"{solvent_prefix}\u03c6_v"

    if "molality" in bare_nl:
        tag = _comp_tag()
        return f"{solvent_prefix}b({tag})" if tag else f"{solvent_prefix}b"

    if "amount concentration" in bare_nl or "molarity" in bare_nl:
        tag = _comp_tag()
        return f"{solvent_prefix}c({tag})" if tag else f"{solvent_prefix}c"

    if "mass ratio" in bare_nl:
        return f"{solvent_prefix}w_ratio({comp_label})" if comp_label else f"{solvent_prefix}w_ratio"

    if "amount ratio" in bare_nl:
        return f"{solvent_prefix}n_ratio({comp_label})" if comp_label else f"{solvent_prefix}n_ratio"

    abbrevs = [
        ("refractive index", "n_D"),
        ("boiling temperature", "T_boil(K)"),
        ("azeotropic temperature", "T_azeo(K)"),
        ("azeotropic composition", "x_azeo"),
        ("vapor or sublimation pressure", "P_vap(kPa)"),
        ("molar enthalpy of reaction", "\u0394H_rxn(kJ/mol)"),
        ("molar internal energy of reaction", "\u0394U_rxn(kJ/mol)"),
        ("molar enthalpy of transition or fusion", "\u0394H_fus(kJ/mol)"),
        ("molar enthalpy of vaporization", "\u0394H_vap(kJ/mol)"),
        ("molar heat capacity at constant pressure", "Cp(J/K/mol)"),
        ("molar enthalpy of mixing", "H_mix(kJ/mol)"),
        ("partial molar enthalpy", "H\u0304(kJ/mol)"),
        ("partial molar volume", "V\u0304(m\u00b3/mol)"),
        ("normal melting temperature", "T_melt(K)"),
        ("triple point temperature", "T_tp(K)"),
        ("mass density", "\u03c1(kg/m\u00b3)"),
        ("density", "\u03c1(kg/m\u00b3)"),
        ("speed of sound", "u(m/s)"),
        ("viscosity", "\u03b7"),
        ("surface tension", "\u03b3(N/m)"),
        ("thermal conductivity", "\u03bb(W/m/K)"),
        ("osmotic coefficient", "\u03c6_osm"),
        ("mean ionic activity coefficient", "\u03b3\u00b1"),
        ("activity coefficient", "\u03b3_act"),
        ("(relative) activity", "a"),
        ("henry's law", "H"),
        ("fugacity coefficient", "\u03c6_fug"),
        ("partial pressure", "P_i(kPa)"),
        ("tracer diffusion coefficient", "D_tr(m\u00b2/s)"),
        ("excess molar enthalpy", "H_E(kJ/mol)"),
        ("excess molar volume", "V_E(cm\u00b3/mol)"),
        ("mass concentration", "\u03c1_c(kg/m\u00b3)"),
    ]
    for pattern, abbr in abbrevs:
        if pattern in nl:
            if comp_label:
                return f"{abbr}[{comp_label}]"
            return abbr

    if "temperature" in nl and "k" in nl.split(",")[-1].lower():
        return "T(K)"
    if "pressure" in nl and "kpa" in nl.split(",")[-1].lower():
        if comp_label:
            return f"P({comp_label},kPa)"
        return "P(kPa)"

    parts = name.split(",")
    base = parts[0].strip()
    unit = parts[1].strip() if len(parts) > 1 else ""
    words = [w for w in base.split() if w.lower() not in
             ("molar", "at", "of", "the", "a", "an", "or", "and", "in")]
    short = "_".join(words[:2]) if words else base[:12]
    if unit:
        short += f"({unit})"
    if comp_label:
        short += f"[{comp_label}]"
    return short


# ---------------------------------------------------------------------------
# Per-block compact markdown
# ---------------------------------------------------------------------------

def pcs_block_compact(
    block, key_info=None, compounds_map=None, *, target_subsystem=None
):
    """Render a single block into compact markdown with canonical IDs.

    All within-DOI org_num references are resolved to canonical compound
    names/IDs. Component-resolved occurrences retain their DOIcomp_N identity.

    Parameters
    ----------
    block : dict
        One element from card["blocks"].
    key_info : dict, optional
        {"doi": ..., "lit_num_id": ..., "lit_id": ...} for the header.
    compounds_map : dict, optional
        org_num -> short label, built from the full compound list.

    Returns compact markdown string.
    """
    block = require_payload(block, _REQUIRED_BLOCK_FIELDS, context="PCS block")
    key_info = require_payload(
        key_info,
        {"doi", "lit_num_id", "lit_id", "title"},
        context="PCS block key_info",
    )

    compounds = block["compounds"]
    org_map = _build_org_map(compounds)

    if compounds_map is None:
        compounds_map = _build_compounds_map(compounds)

    doi = key_info["doi"]
    lit_num_id = key_info["lit_num_id"]

    bt = block["block_type"]
    bn_raw = _blok(block["block_number"])
    ds = block["data_summary"]
    system_type = block["system_type"]
    n_pts = ds["n_points"]
    properties = block["properties"]
    variables = block["variables"]
    constraints = block["constraints"]
    reaction = block["reaction"]
    data_points = block["data_points"]

    lines = []

    # === Header ===
    target_label = bn_raw
    if target_subsystem is not None:
        subsystem_id = require_block_local_id(
            "subsys", target_subsystem["BLKsubsys_id"]
        )
        target_label = f"{bn_raw}/{subsystem_id}"
    hdr = f"## {target_label} | {_short_type(bt)} | {system_type} | {n_pts} pts"
    if doi:
        hdr += f" | {lit_num_id}"
    lines.append(hdr)
    if target_subsystem is not None:
        retained = ", ".join(
            item["comp_num_id"]
            for item in target_subsystem["retained_components"]
        )
        excluded = ", ".join(
            item["comp_num_id"]
            for item in target_subsystem["excluded_components"]
        )
        lines.append(
            "**Exact composition subsystem:** "
            f"path={target_subsystem['path_class']}; "
            f"evidence={target_subsystem['evidence_quality']}; "
            f"retained={retained}; excluded={excluded or 'none'}"
        )
    else:
        effective = ds["effective_system_summary"]
        if effective["n_subsystems"]:
            lines.append(
                "**Composition projections:** "
                f"{effective['n_subsystems']} subsystem(s); "
                f"types={','.join(effective['system_types'])}; "
                f"search-eligible={effective['n_search_eligible']}; "
                f"referenced points={effective['n_unique_points']}"
            )

    # --- Reference ---
    lit_id = key_info["lit_id"]
    title = key_info["title"]
    if lit_id or title:
        lines.append("")
        lines.append("### Reference")
        if lit_id:
            lines.append(f"**lit_id:** {lit_id}")
        if title:
            lines.append(f"**Title:** {title}")

    # --- Compounds ---
    if compounds:
        lines.append("")
        lines.append("### Compounds")
        lines.append("")
        lines.append("| org_num | comp_num_id | Name | Formula |")
        lines.append("|---|---|---|---|")
        for c in sorted(compounds, key=lambda x: x["org_num"]):
            require_payload(
                c,
                {
                    "org_num", "comp_num_id", "inchi_key", "name", "formula",
                    "InChI", "SMILES", "sample_num",
                },
                context=f"PCS block compound {c['org_num']!r}",
            )
            cid = require_global_id("comp_num_id", c["comp_num_id"])
            name = c.get("name", "")
            formula = c.get("formula", "")
            lines.append(f"| {c['org_num']} | {cid} | {name} | {formula} |")

    # --- Reaction ---
    if reaction:
        lines.append("")
        lines.append("### Reaction")
        rtype = reaction["reaction_type"]
        if rtype:
            lines.append(f"**Type:** {rtype}")
        participants = reaction["participants"]
        if participants:
            reactants, products = [], []
            for p in participants:
                coef = p["stoichiometric_coef"]
                org = require_doi_comp_id(p["org_num"])
                phase = p["phase"]
                cname = _resolve_comp_name(org, org_map) or org
                ps = f"({phase})" if phase else ""
                entry = f"{abs(coef):g} {cname}{ps}"
                (reactants if coef < 0 else products).append(entry)
            lines.append(f"**Rxn:** {' + '.join(reactants)} -> {' + '.join(products)}")

    # --- Properties ---
    if properties:
        lines.append("")
        lines.append("### Properties")
        lines.append("")
        lines.append("| BLKprop_id | prop_num_id | Property | meas_num_id | Method | Group | Phase |")
        lines.append("|---|---|---|---|---|---|---|")

        for prop in properties:
            pid = require_global_id("prop_num_id", prop["prop_num_id"])
            prop_ID = prop["prop_ID"]
            mid = require_global_id("meas_num_id", prop["meas_num_id"])
            meas_id_str = prop["meas_ID"]
            group = prop["group"]

            pphase = prop.get("property_phase")
            if pphase is not None:
                require_global_id("phase_num_id", pphase["phase_num_id"])
                phase_str = pphase["phase"]
            else:
                phase_str = ""

            row = [prop["BLKprop_id"], pid, prop_ID or "",
                   mid, meas_id_str or "",
                   group or "", phase_str]

            lines.append("| " + " | ".join(row) + " |")

        # Fixed T/P on properties
        fixed_parts = []
        for prop in properties:
            t = prop.get("temperature_K")
            if t is not None:
                fixed_parts.append(f"T={t}K")
            p = prop.get("pressure_kPa")
            if p is not None:
                fixed_parts.append(f"P={p}kPa")
        if fixed_parts:
            lines.append(f"**Fixed:** {' | '.join(fixed_parts)}")

        # Ref state
        for prop in properties:
            rp = []
            if prop.get("ref_state_type"):
                rp.append(f"Type:{prop['ref_state_type']}")
            if prop.get("ref_temperature_K") is not None:
                rp.append(f"T_ref={prop['ref_temperature_K']}K")
            if prop.get("ref_pressure_kPa") is not None:
                rp.append(f"P_ref={prop['ref_pressure_kPa']}kPa")
            if prop.get("ref_phase"):
                rp.append(f"Phase_ref:{prop['ref_phase']}")
            if rp:
                lines.append(f"**Ref:** {'; '.join(rp)}")

        # Standard state
        for prop in properties:
            if prop.get("standard_state"):
                lines.append(f"**StdState:** {prop['standard_state']}")

    # --- Variables ---
    if variables:
        lines.append("")
        lines.append("### Variables")
        lines.append("")
        lines.append("| BLKvar_id | var_num_id | Variable | Component | Phase |")
        lines.append("|---|---|---|---|---|")

        for v in variables:
            vid = require_global_id("var_num_id", v["var_num_id"])
            vname = v["var_id"]
            vph = v["phase"]
            if vph is not None:
                require_global_id("phase_num_id", vph["phase_num_id"])
                phase_str = vph["phase"]
            else:
                phase_str = ""

            vcomp = v["component_org_num"]
            row = [v["BLKvar_id"], vid, vname, vcomp or "", phase_str]
            lines.append("| " + " | ".join(row) + " |")

    # --- Constraints ---
    if constraints:
        lines.append("")
        lines.append("### Constraints")
        lines.append("")
        lines.append("| BLKconstr_id | constr_num_id | Constraint | Component | Value | Phase |")
        lines.append("|---|---|---|---|---|---|")

        for c in constraints:
            cid = require_global_id("constr_num_id", c["constr_num_id"])
            cname = c["constr_id"]
            cval = _format_value(c.get("value"))
            cph = c["phase"]
            if cph is not None:
                require_global_id("phase_num_id", cph["phase_num_id"])
                phase_str = cph["phase"]
            else:
                phase_str = ""

            comp_org = c["component_org_num"]
            row = [c["BLKconstr_id"], cid, cname, comp_org or "", cval, phase_str]
            lines.append("| " + " | ".join(row) + " |")

    # --- Conditions ---
    cond_parts = []

    phases = ds.get("phases", [])
    if phases and not reaction:
        cond_parts.append(f"**Phases:** {'; '.join(phases)}")

    solvents = block["solvents"]
    if solvents:
        solvent_labels = [
            f"{s['component_org_num']}→{s['comp_num_id']} ({s['solvent_num_id']})"
            for s in solvents
        ]
        cond_parts.append(f"**Solvents:** {'; '.join(solvent_labels)}")

    unc_strs = set()
    for prop in properties:
        unc = prop.get("uncertainty")
        if not unc:
            continue
        parts = []
        cl = unc.get("confidence_level")
        if cl:
            parts.append(f"k={cl}%")
        em = unc.get("evaluation_method", "")
        if "propagation" in em.lower():
            parts.append("Propagation")
        elif em:
            parts.append(em[:25])
        ev = unc.get("evaluator", "")
        if "compiler" in ev.lower():
            parts.append("compiler")
        elif ev:
            parts.append(ev[:15])
        if parts:
            unc_strs.add(", ".join(parts))
    if unc_strs:
        cond_parts.append(f"**Unc:** {'; '.join(sorted(unc_strs))}")

    prov = block["provenance"]
    if prov:
        purpose = prov.get("experimental_purpose", "")
        if purpose and purpose != "Principal objective of the work":
            cond_parts.append(f"**Purpose:** {purpose}")

    if cond_parts:
        lines.append("")
        lines.append("### Conditions")
        lines.extend(cond_parts)

    # --- Data ---
    if data_points:
        lines.append("")
        lines.append("### Data")
        lines.append("")
        cols = []

        sorted_vars = sorted(
            variables, key=lambda v: block_local_ordinal("var", v["BLKvar_id"])
        )
        for v in sorted_vars:
            vnum = v["BLKvar_id"]
            vname = v["name"]
            vph = (v.get("phase") or {}).get("phase")
            vcomp = v["component_org_num"]
            header = _short_col(vname, "var", vcomp, compounds_map, phase=vph)
            cols.append((header, "var", vnum))

        sorted_props = sorted(
            properties, key=lambda p: block_local_ordinal("prop", p["BLKprop_id"])
        )
        prop_headers = []
        for p in sorted_props:
            pnum = p["BLKprop_id"]
            pname = p["name"]
            pcomp = p["component_org_num"]
            pph = (p.get("property_phase") or {}).get("phase")
            header = _short_col(pname, "prop", pcomp, compounds_map, phase=pph)
            prop_headers.append((header, pnum))
            cols.append((header, "prop", pnum))

        has_unc = {}
        for dp in data_points:
            for pnum, pv in dp.get("property_values", {}).items():
                pu = pv.get("point_uncertainty")
                if pu and pu.get("expanded_value") is not None:
                    has_unc[pnum] = True

        for header, pnum in prop_headers:
            if pnum in has_unc:
                uc_label = f"\u00b1U[{pnum}]" if len(prop_headers) > 1 else "\u00b1U"
                cols.append((uc_label, "unc", pnum))

        header_counts = {}
        for i, (h, _, _) in enumerate(cols):
            header_counts.setdefault(h, []).append(i)
        for h, indices in header_counts.items():
            if len(indices) > 1:
                for seq, idx in enumerate(indices, 1):
                    old_h, ctype, ckey = cols[idx]
                    cols[idx] = (f"{old_h}_{seq}", ctype, ckey)

        headers = [c[0] for c in cols]
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("|" + "|".join(["---"] * len(headers)) + "|")

        for dp in data_points:
            var_vals = dp.get("variable_values", {})
            prop_vals = dp.get("property_values", {})
            row = []
            for header, ctype, ckey in cols:
                if ctype == "var":
                    vv = var_vals.get(ckey, {})
                    row.append(_format_value(vv.get("value")) if vv else "")
                elif ctype == "prop":
                    pv = prop_vals.get(ckey, {})
                    row.append(_format_value(pv.get("value")) if pv else "")
                elif ctype == "unc":
                    pv = prop_vals.get(ckey, {})
                    pu = (pv.get("point_uncertainty") or {}) if pv else {}
                    ev = pu.get("expanded_value")
                    row.append(_format_value(ev) if ev is not None else "")
            lines.append("| " + " | ".join(row) + " |")

        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Block with RDP topology
# ---------------------------------------------------------------------------


def compact_block(
    block, key_info=None, compounds_map=None, *, target_subsystem=None
):
    """Render a single block as a standalone compact markdown card.

    Applies RDP topology compaction to reduce the data-points table
    while preserving the shape of each (variable, property) curve.
    A ``**Topology:**`` annotation is appended after the metadata
    and before the (simplified) data table.

    Parameters
    ----------
    block : dict
        A single block dict (one element of card["blocks"]).
    key_info : dict, optional
        {"doi": ..., "lit_num_id": ..., "lit_id": ...}.
    compounds_map : dict, optional
        org_num -> short label for data-table column headers.
        If not provided, built from the block's own compounds.

    Returns
    -------
    str  — compact markdown.
    """
    block = require_payload(block, _REQUIRED_BLOCK_FIELDS, context="PCS block")
    key_info = require_payload(
        key_info,
        {"doi", "lit_num_id", "lit_id", "title"},
        context="PCS block key_info",
    )
    if compounds_map is None:
        compounds_map = _build_compounds_map(block["compounds"])

    variables = block["variables"]
    properties = block["properties"]
    data_points = block["data_points"]

    result = compact_block_data(variables, properties, data_points,
                                compounds_map=compounds_map)
    topology = result["topology"]
    simplified = result["simplified_points"]

    # Build a shallow copy with simplified data points
    reduced = dict(block)
    reduced["data_points"] = simplified

    md = pcs_block_compact(
        reduced, key_info=key_info, compounds_map=compounds_map,
        target_subsystem=target_subsystem,
    )

    # Inject topology annotation between metadata and data table
    topo_line = _format_topology(topology, len(data_points), len(simplified))
    if topo_line:
        md = _inject_topology(md, topo_line)

    return md


def _subsystem_block_view(block, subsystem, *, doi):
    """Return the exact raw-row projection for a PCS composition subsystem."""
    from card_db_search_tools.basic_search_tools.normalization_helpers.db_helpers import (
        project_pcs_block_target,
    )

    subsystem_id = require_block_local_id("subsys", subsystem["BLKsubsys_id"])
    projection = project_pcs_block_target(block, subsystem)
    active_var_ids = {item["BLKvar_id"] for item in projection["variables"]}
    active_prop_ids = {item["BLKprop_id"] for item in projection["properties"]}
    active_constr_ids = {
        item["BLKconstr_id"] for item in projection["constraints"]
    }

    # PCS data_points are intentionally a bounded display sample.  An exact
    # subsystem card therefore reconstructs its points from the uncapped raw
    # extractor, which applies the authoritative manifest point runs.
    import csv
    import importlib
    import io

    extractor = importlib.import_module(
        "card_db_search_tools.basic_search_tools.11_block_data_extractor"
    )
    extracted = extractor.extract_block_csv(
        doi, block["block_number"], BLKsubsys_id=subsystem_id
    )
    if extracted["error"] is not None:
        raise LookupError(extracted["error"])
    if extracted["n_rows"] != subsystem["n_points"]:
        raise ValueError(
            f"{block['block_number']}/{subsystem_id} manifest declares "
            f"{subsystem['n_points']} points but raw extraction returned "
            f"{extracted['n_rows']}"
        )
    variable_columns = {
        item["BLKvar_id"]: item["column_name"]
        for item in extracted["metadata"]["variables"]
        if item["BLKvar_id"] in active_var_ids
    }
    property_columns = {
        item["BLKprop_id"]: item["column_name"]
        for item in extracted["metadata"]["properties"]
        if item["BLKprop_id"] in active_prop_ids
    }

    def numeric(value):
        if value in (None, ""):
            return None
        return float(value)

    points = []
    for row in csv.DictReader(io.StringIO(extracted["csv_text"])):
        points.append({
            "BLKpoint_id": row["BLKpoint_id"],
            "variable_values": {
                local_id: {"value": numeric(row[column]), "digits": None}
                for local_id, column in variable_columns.items()
            },
            "property_values": {
                local_id: {
                    "value": numeric(row[column]),
                    "digits": None,
                    "point_uncertainty": None,
                }
                for local_id, column in property_columns.items()
            },
            "BLKsubsys_refs": [subsystem_id],
        })

    data_summary = dict(block["data_summary"])
    data_summary["n_points"] = subsystem["n_points"]
    data_summary["system_type"] = subsystem["effective_system_type"]
    data_summary["compound_names"] = [
        item.get("name") or item["org_num"]
        for item in projection["compounds"]
    ]
    data_summary["property_names"] = [
        item["name"] for item in projection["properties"]
    ]
    data_summary["methods"] = [
        item["method_standard"] or item["method_custom"] or item["meas_ID"]
        for item in projection["properties"]
    ]
    data_summary["constraints_summary"] = {
        key: value
        for key, value in data_summary["constraints_summary"].items()
        if key in active_constr_ids
    }
    data_summary["variable_ranges"] = {}
    for item in projection["variables"]:
        local_id = item["BLKvar_id"]
        values = [
            point["variable_values"][local_id]["value"]
            for point in points
            if point["variable_values"].get(local_id, {}).get("value") is not None
        ]
        if values:
            data_summary["variable_ranges"][local_id] = {
                "BLKvar_id": local_id,
                "name": item["name"],
                "min": min(values),
                "max": max(values),
                "n_unique": len(set(values)),
            }
    data_summary["property_stats"] = {}
    for item in projection["properties"]:
        local_id = item["BLKprop_id"]
        values = [
            point["property_values"][local_id]["value"]
            for point in points
            if point["property_values"].get(local_id, {}).get("value") is not None
        ]
        if values:
            mean = sum(values) / len(values)
            data_summary["property_stats"][local_id] = {
                "BLKprop_id": local_id,
                "name": item["name"],
                "min": min(values),
                "max": max(values),
                "mean": mean,
                "std": (
                    sum((value - mean) ** 2 for value in values) / len(values)
                ) ** 0.5,
                "n": len(values),
            }
    data_summary["effective_system_summary"] = {
        "n_subsystems": 0,
        "system_types": [],
        "n_search_eligible": 0,
        "n_unique_points": 0,
    }

    view = dict(block)
    view.update(projection)
    view["system_type"] = subsystem["effective_system_type"]
    view["data_summary"] = data_summary
    view["data_points"] = points
    return view


def _format_topology(topology, n_original, n_kept):
    """Format topology info as a single markdown line."""
    if not topology:
        return ""
    parts = []
    for t in topology:
        if "note" in t:
            parts.append(t["note"])
        elif "shape" in t:
            parts.append(t["shape"])
    shape_str = "; ".join(parts) if parts else "—"
    return f"**Topology:** {shape_str} | {n_original} pts → {n_kept} kept (RDP)"


def _inject_topology(md, topo_line):
    """Insert topology line inside ### Data section, before the data table."""
    lines = md.split("\n")
    # Find "### Data" header and insert topology right after it
    for i, line in enumerate(lines):
        if line.strip() == "### Data":
            # Insert after "### Data" and any blank line
            insert_at = i + 1
            while insert_at < len(lines) and not lines[insert_at].strip():
                insert_at += 1
            lines.insert(insert_at, topo_line)
            return "\n".join(lines)
    # Fallback: insert before the last table header
    insert_at = None
    for i in range(len(lines) - 1):
        if lines[i].startswith("|") and lines[i + 1].startswith("|---"):
            insert_at = i
    if insert_at is not None:
        lines.insert(insert_at, topo_line)
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Compact a single PCS block JSON into markdown."
    )
    parser.add_argument(
        "input", nargs="?", default="-",
        help="Path to a block JSON file (default: stdin)"
    )
    parser.add_argument(
        "-o", "--output", default=None,
        help="Output file (default: stdout)"
    )
    args = parser.parse_args()

    if args.input == "-":
        data = json.load(sys.stdin)
    else:
        with open(args.input, encoding="utf-8") as f:
            data = json.load(f)

    payload = require_payload(data, {"key_info", "block"}, context="block CLI input")
    key_info = payload["key_info"]
    block = payload["block"]

    md = compact_block(block, key_info=key_info)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(md)
    else:
        sys.stdout.write(md)


# ---------------------------------------------------------------------------
# Main API — fetch from DB by ID and return markdown
# ---------------------------------------------------------------------------

def get_card_md(*, doi: str = None, lit_num_id: str = None,
                block_number: str, BLKsubsys_id: str = None) -> str:
    """Fetch a PCS_INDIV card, pick one block, and return compact block markdown.

    Parameters
    ----------
    doi / lit_num_id : identify the PCS card (provide exactly one).
    block_number : exact typed block ID to render.
    BLKsubsys_id : optional exact composition-subsystem projection.
    """
    from ThermoML_card_json_to_md_compactors._db_access import fetch_card
    if (doi is None) == (lit_num_id is None):
        raise ValueError("Provide exactly one of doi or lit_num_id")
    if doi is not None:
        card = fetch_card("PCS_INDIV", "doi", doi)
    else:
        card = fetch_card("PCS_INDIV", "lit_num_id", lit_num_id)

    from card_db_search_tools.basic_search_tools.normalization_helpers.db_helpers import (
        resolve_pcs_block_target,
    )

    block, subsystem = resolve_pcs_block_target(
        card, block_number, BLKsubsys_id=BLKsubsys_id
    )
    if subsystem is not None:
        block = _subsystem_block_view(block, subsystem, doi=card["key"]["doi"])

    key_info = {**card["key"], "title": card["paper"]["title"]}
    compounds_map = _build_compounds_map(block["compounds"])
    return compact_block(
        block, key_info=key_info, compounds_map=compounds_map,
        target_subsystem=subsystem,
    )


if __name__ == "__main__":
    main()
