"""
RMS (Reference Metadata Schema) card builder.

Produces one card per paper with bibliographic metadata and a data inventory.
All entities are indexed using canonical IDs from the CSV registry.
"""

from ThermoML_raw_json_to_card_db_parsers.shared_utils import (
    extract_trc_ref_id, extract_property_info, extract_var_or_constraint_type,
    resolve_compound_structure_identifiers, system_type_label,
    safe_float, safe_int,
)
from ThermoML_raw_json_to_card_db_parsers.index_lookup import ThermoMLIndex
from ThermoML_raw_json_to_card_db_parsers.id_schema import doi_comp_id


def build_rms_card(data, index):
    """Build Reference Metadata Schema card from ThermoML JSON.

    Args:
        data: Parsed ThermoML JSON dict for one paper.
        index: ThermoMLIndex instance for canonical ID lookups.
    """
    cit = data.get("Citation", {})
    doi = cit.get("sDOI", "")
    lit_id, trc_ref = extract_trc_ref_id(cit.get("TRCRefID"))

    ref_row = index.lookup_reference(doi)
    if ref_row is None:
        raise ValueError(f"Reference registry has no canonical ID for DOI {doi!r}")
    lit_num_id = ref_row["lit_num_id"]

    # Bibliographic
    authors = cit.get("sAuthor", [])
    if isinstance(authors, str):
        authors = [authors]

    # Compound list with canonical IDs
    compounds = data.get("Compound", [])
    compound_list = []
    for comp in compounds:
        reg = comp.get("RegNum", {})
        org_num = reg.get("nOrgNum")
        names = comp.get("sCommonName", [])
        if isinstance(names, str):
            names = [names]

        inchi_key = comp.get("sStandardInChIKey")
        inchi = comp.get("sStandardInChI")
        formula = comp.get("sFormulaMolec", "")
        comp_row = index.lookup_compound(
            inchi_key=inchi_key, standard_inchi=inchi,
            common_name=names[0] if names else None, formula=formula)
        if comp_row is None:
            raise ValueError(
                f"Compound registry lookup failed for DOI {doi!r}, org_num={org_num!r}"
            )

        structure = resolve_compound_structure_identifiers(comp, comp_row)

        compound_list.append({
            "org_num": doi_comp_id(org_num),
            "comp_num_id": comp_row["comp_num_id"],
            "inchi_key": structure["inchi_key"],
            "SMILES": structure["SMILES"],
            "InChI": structure["InChI"],
            "name": names[0] if names else comp.get("sFormulaMolec", ""),
            "formula": comp.get("sFormulaMolec", ""),
        })

    # Scan blocks for data inventory
    pure_blocks = data.get("PureOrMixtureData", [])
    rxn_blocks = data.get("ReactionData", [])
    all_blocks = ([(b, "PureOrMixtureData") for b in pure_blocks]
                  + [(b, "ReactionData") for b in rxn_blocks])

    prop_occurrence_types = set()
    prop_groups = set()
    sys_types = set()
    temps = []
    pressures = []
    total_pts = 0

    for blk, btype in all_blocks:
        for prop in blk.get("Property", []):
            pname, gname, _, _, comp_org_num = extract_property_info(prop)
            if pname:
                prop_occurrence_types.add((pname, comp_org_num is not None))
            if gname:
                prop_groups.add(gname)

        comp_key = "Component" if btype == "PureOrMixtureData" else "Participant"
        n_comp = len(blk.get(comp_key, []))
        sys_types.add(system_type_label(n_comp))

        total_pts += len(blk.get("NumValues", []))

        # T/P from variables
        for var in blk.get("Variable", []):
            vid = var.get("VariableID", {})
            vtype = vid.get("VariableType", {})
            vname, vcat = extract_var_or_constraint_type(vtype)
            if vcat in ("eTemperature", "ePressure"):
                for nv in blk.get("NumValues", []):
                    for vv in nv.get("VariableValue", []):
                        if vv.get("nVarNumber") == var.get("nVarNumber"):
                            v = safe_float(vv.get("nVarValue"))
                            if v is not None:
                                (temps if vcat == "eTemperature" else pressures).append(v)

        # T/P from constraints
        for constr in blk.get("Constraint", []):
            cid = constr.get("ConstraintID", {})
            ctype = cid.get("ConstraintType", {})
            _, ccat = extract_var_or_constraint_type(ctype)
            v = safe_float(constr.get("nConstraintValue"))
            if v is not None:
                if ccat == "eTemperature":
                    temps.append(v)
                elif ccat == "ePressure":
                    pressures.append(v)

        # ReactionData inline T/P
        if btype == "ReactionData":
            for prop in blk.get("Property", []):
                t = safe_float(prop.get("nTemperature-K"))
                p = safe_float(prop.get("nPressure-kPa"))
                if t is not None:
                    temps.append(t)
                if p is not None:
                    pressures.append(p)

    # Build indexed property list
    prop_list = []
    for pn, component_linked in sorted(prop_occurrence_types):
        entry = {"name": pn, "component_linked": component_linked}
        prop_row = index.lookup_property(pn, component_linked)
        if prop_row is None:
            raise ValueError(f"Property registry lookup failed for {pn!r} in DOI {doi!r}")
        entry["prop_num_id"] = prop_row["prop_num_id"]
        entry["prop_id"] = ThermoMLIndex.base_id(prop_row["prop_id"])
        prop_list.append(entry)

    return {
        "identity": {
            "doi": doi,
            "lit_id": lit_id,
            "lit_num_id": lit_num_id,
            "trc_ref_id": trc_ref if trc_ref.get("year") else None,
        },
        "bibliographic": {
            "title": cit.get("sTitle", ""),
            "authors": authors,
            "journal": cit.get("sPubName", ""),
            "year": safe_int(cit.get("yrPubYr")),
            "volume": cit.get("sVol", ""),
            "pages": cit.get("sPage", ""),
            "issue_number": cit.get("sIDNum"),
            "publication_type": cit.get("eType", "journal"),
            "source_type": cit.get("eSourceType", "Original"),
            "citation_date": cit.get("dateCit", ""),
        },
        "content": {
            "abstract": cit.get("sAbstract"),
            "keywords": (cit.get("sKeyword") if isinstance(cit.get("sKeyword"), list)
                         else ([cit["sKeyword"]] if cit.get("sKeyword") else None)),
        },
        "data_inventory": {
            "n_compounds": len(compounds),
            "compound_list": compound_list,
            "n_blocks": len(all_blocks),
            "has_pure_or_mixture_data": len(pure_blocks) > 0,
            "has_reaction_data": len(rxn_blocks) > 0,
            "properties": prop_list,
            "property_groups": sorted(prop_groups),
            "system_types": sorted(sys_types),
            "temperature_range_K": ({"min": round(min(temps), 2), "max": round(max(temps), 2)}
                                    if temps else None),
            "pressure_range_kPa": ({"min": round(min(pressures), 3), "max": round(max(pressures), 3)}
                                   if pressures else None),
            "n_datapoints": total_pts,
        },
    }
