"""
PCS (Property Card Schema) INDIV card builder -- per-DOI measurement data card.

Produces one card per paper containing all experimental blocks and their data points.
All entities are indexed using canonical IDs from the CSV registry.
"""

import math
from collections import defaultdict

from ThermoML_raw_json_to_card_db_parsers.identity_translation import (
    get_global_identity_translations,
)
from ThermoML_raw_json_to_card_db_parsers.shared_utils import (
    system_type_label,
    extract_trc_ref_id, extract_phase_info, extract_var_or_constraint_type,
    extract_property_info, resolve_compound_structure_identifiers,
    safe_float, safe_int,
)
from ThermoML_raw_json_to_card_db_parsers.index_lookup import ThermoMLIndex
from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    block_id,
    block_local_id,
    block_local_ordinal,
    doi_comp_id,
    doi_comp_sample_id,
    property_assessment_id,
)
from ThermoML_raw_json_to_card_db_parsers.property_card_helpers.pcs_identity_enrichment import (
    build_block_identity_index,
)


def build_pcs_card(
    data,
    index,
    max_datapoints_per_block=50,
    *,
    identity_translations=None,
):
    """Build Property Card Schema INDIV (per-DOI block data) card.

    Args:
        data: Parsed ThermoML JSON dict.
        index: ThermoMLIndex instance for canonical ID lookups.
        max_datapoints_per_block: Cap data_points per block (None for all).
        identity_translations: Validated exact prop/var/constr translation
            registry. Loaded from the canonical translation CSV when omitted.
            The registry is used to embed each block's exact key permutations
            and full-column statistics in the card's derived block index.
    """
    if (
        max_datapoints_per_block is not None
        and (
            isinstance(max_datapoints_per_block, bool)
            or not isinstance(max_datapoints_per_block, int)
            or max_datapoints_per_block <= 0
        )
    ):
        raise ValueError(
            "max_datapoints_per_block must be None or a positive integer"
        )
    if identity_translations is None:
        identity_translations = get_global_identity_translations()

    cit = data["Citation"]
    doi = cit["sDOI"]
    lit_id, _ = extract_trc_ref_id(cit["TRCRefID"])

    ref_row = index.lookup_reference(doi)
    if ref_row is None:
        raise ValueError(f"Reference registry has no canonical ID for DOI {doi!r}")
    lit_num_id = ref_row["lit_num_id"]

    # Build compound lookup from top-level Compound[]
    compounds = data["Compound"]
    comp_lookup = {}
    for comp in compounds:
        reg = comp["RegNum"]
        org_num = reg["nOrgNum"]
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

        comp_lookup[org_num] = {
            "name": names[0] if names else comp.get("sFormulaMolec", ""),
            "formula": comp.get("sFormulaMolec", ""),
            "InChI": structure["InChI"],
            "SMILES": structure["SMILES"],
            "inchi_key": structure["inchi_key"],
            "comp_num_id": comp_row["comp_num_id"],
        }

    pure_blocks = data.get("PureOrMixtureData", [])
    rxn_blocks = data.get("ReactionData", [])
    all_blocks_raw = ([(b, "PureOrMixtureData") for b in pure_blocks]
                      + [(b, "ReactionData") for b in rxn_blocks])

    blocks_out = []
    block_index = []
    block_search_adv_indexes = {}
    composition_subsystem_indexes = {}
    all_prop_names = set()
    all_prop_groups = set()
    all_compound_names = set()
    all_system_types = set()
    all_methods = set()
    all_temps = []
    all_pressures = []
    total_pts = 0

    for blk, btype in all_blocks_raw:
        if btype == "PureOrMixtureData":
            bnum = blk["nPureOrMixtureDataNumber"]
        else:
            bnum = blk["nReactionDataNumber"]

        block_label = block_id(btype, bnum)

        # -- Compounds / Participants --
        comp_key = "Component" if btype == "PureOrMixtureData" else "Participant"
        block_compounds = []
        for c in blk[comp_key]:
            rn = c["RegNum"]
            on = rn["nOrgNum"]
            try:
                info = comp_lookup[on]
            except KeyError as exc:
                raise ValueError(
                    f"Block {block_label} references unknown DOI compound "
                    f"ordinal {on!r}"
                ) from exc
            comp_entry = {
                "org_num": doi_comp_id(on),
                "comp_num_id": info["comp_num_id"],
                "inchi_key": info["inchi_key"],
                "name": info["name"],
                "formula": info["formula"],
                "InChI": info.get("InChI"),
                "SMILES": info.get("SMILES"),
                "sample_num": (
                    doi_comp_sample_id(on, c["nSampleNm"])
                    if c.get("nSampleNm") is not None else None
                ),
            }
            all_compound_names.add(info["name"])
            block_compounds.append(comp_entry)

        n_comp = len(block_compounds)
        sys_type = system_type_label(n_comp)
        all_system_types.add(sys_type)
        blocktype_row = index.lookup_block_type(btype, sys_type)
        if blocktype_row is None:
            raise ValueError(
                f"Block-type registry lookup failed for {(btype, sys_type)!r} in DOI {doi!r}"
            )

        # -- Properties --
        block_properties = []
        block_prop_names = []
        block_prop_group = ""
        block_method = None
        block_solvents = []
        property_solvent_scopes = {}
        seen_solvent_orgs = set()
        declared_prop_numbers = set()

        for prop in blk.get("Property", []):
            pnum = prop.get("nPropNumber")
            if pnum is None:
                raise ValueError(
                    f"Property declaration without nPropNumber in "
                    f"{doi!r} {block_label}"
                )
            if pnum in declared_prop_numbers:
                raise ValueError(
                    f"Duplicate property declaration {pnum!r} in "
                    f"{doi!r} {block_label}"
                )
            declared_prop_numbers.add(pnum)
            pname, gname, method_std, method_cust, comp_org_num = extract_property_info(prop)

            pmid = prop.get("Property-MethodID", {})
            prop_comp_ref = pmid.get("RegNum", {}).get("nOrgNum")

            # Canonical property lookup
            prop_row = index.lookup_property(pname, prop_comp_ref is not None)
            if prop_row is None:
                raise ValueError(f"Property registry lookup failed for {pname!r} in DOI {doi!r}")
            prop_id = ThermoMLIndex.resolve_id(prop_row["prop_id"], prop_comp_ref)
            prop_num_id = prop_row["prop_num_id"]

            all_prop_names.add(pname)
            all_prop_groups.add(gname)
            block_prop_names.append(pname)
            block_prop_group = gname

            # Method with canonical lookup
            method_name = method_std or method_cust
            if method_name:
                meas_row = index.lookup_measurement(method_name)
                if meas_row is None:
                    raise ValueError(
                        f"Measurement registry lookup failed for {method_name!r} in DOI {doi!r}"
                    )
                meas_id = meas_row["meas_id"]
                meas_num_id = meas_row["meas_num_id"]
                all_methods.add(method_name)
                block_method = method_name
            else:
                meas_id = None
                meas_num_id = None

            # Phase with canonical lookup
            prop_phase = _enrich_phase(extract_phase_info(prop.get("PropPhaseID")), index)

            # Presentation, ref state, standard state
            presentation = prop.get("ePresentation")
            ref_state_type = prop.get("eRefStateType")
            ref_temp = safe_float(prop.get("nRefTemp"))
            ref_temp_digits = safe_int(prop.get("nRefTempDigits"))
            ref_press = safe_float(prop.get("nRefPressure"))
            ref_press_digits = safe_int(prop.get("nRefPressureDigits"))
            ref_phase = _enrich_phase(extract_phase_info(prop.get("RefPhaseID")), index)
            standard_state = prop.get("eStandardState")
            if ref_temp is not None and not math.isfinite(ref_temp):
                raise ValueError(
                    f"Property {pnum!r} has nonfinite reference temperature "
                    f"in {doi!r} {block_label}"
                )
            if ref_press is not None and not math.isfinite(ref_press):
                raise ValueError(
                    f"Property {pnum!r} has nonfinite reference pressure "
                    f"in {doi!r} {block_label}"
                )

            # ReactionData inline T/P
            temp_k = safe_float(prop.get("nTemperature-K"))
            temp_digits = safe_int(prop.get("nTemperatureDigits"))
            press_kpa = safe_float(prop.get("nPressure-kPa"))
            press_digits = safe_int(prop.get("nPressureDigits"))

            if temp_k is not None and not math.isfinite(temp_k):
                raise ValueError(
                    f"ReactionData property {pnum!r} has nonfinite "
                    f"temperature in {doi!r} {block_label}"
                )
            if press_kpa is not None and not math.isfinite(press_kpa):
                raise ValueError(
                    f"ReactionData property {pnum!r} has nonfinite "
                    f"pressure in {doi!r} {block_label}"
                )
            if temp_k is not None and math.isfinite(temp_k):
                all_temps.append(temp_k)
            if press_kpa is not None and math.isfinite(press_kpa):
                all_pressures.append(press_kpa)

            # Uncertainty (block-level)
            uncert = None
            comb_uncert = prop.get("CombinedUncertainty")
            if isinstance(comb_uncert, dict):
                uncert = {
                    "evaluation_method": comb_uncert.get("eCombUncertEvalMethod"),
                    "confidence_level": safe_int(comb_uncert.get("nCombUncertLevOfConfid")),
                    "evaluator": comb_uncert.get("sCombUncertEvaluator"),
                    "assessment_num": (
                        property_assessment_id(pnum, comb_uncert["nCombUncertAssessNum"])
                        if "nCombUncertAssessNum" in comb_uncert else None
                    ),
                }

            # Preserve every solvent component as a distinct DOI occurrence.
            solvent_obj = prop.get("Solvent")
            current_property_solvents = []
            if solvent_obj:
                sol_rnums = solvent_obj.get("RegNum", [])
                if isinstance(sol_rnums, dict):
                    sol_rnums = [sol_rnums]
                for sol_reg in sol_rnums:
                    sol_org = sol_reg.get("nOrgNum")
                    if sol_org is None:
                        continue
                    current_property_solvents.append(doi_comp_id(sol_org))
                    if sol_org in seen_solvent_orgs:
                        continue
                    sol_comp = comp_lookup.get(sol_org)
                    if sol_comp is None:
                        raise ValueError(
                            f"Solvent org_num={sol_org!r} is absent from DOI {doi!r} compound map"
                        )
                    solvent_row = index.lookup_solvent(sol_comp["comp_num_id"])
                    if solvent_row is None:
                        raise ValueError(
                            f"Solvent registry lookup failed for {sol_comp['comp_num_id']!r}"
                        )
                    block_solvents.append({
                        "component_org_num": doi_comp_id(sol_org),
                        "comp_num_id": sol_comp["comp_num_id"],
                        "solvent_num_id": solvent_row["solvent_num_id"],
                        "inchi_key": sol_comp["inchi_key"],
                    })
                    seen_solvent_orgs.add(sol_org)
            property_solvent_scopes[block_local_id("prop", pnum)] = current_property_solvents

            block_properties.append({
                "BLKprop_id": block_local_id("prop", pnum),
                "prop_num_id": prop_num_id,
                "prop_ID": prop_id,
                "name": pname,
                "group": gname,
                "method_standard": method_std,
                "method_custom": method_cust,
                "meas_num_id": meas_num_id,
                "meas_ID": meas_id,
                "presentation": presentation,
                "standard_state": standard_state,
                "ref_state_type": ref_state_type,
                "ref_temperature_K": ref_temp,
                "ref_temperature_digits": ref_temp_digits,
                "ref_pressure_kPa": ref_press,
                "ref_pressure_digits": ref_press_digits,
                "temperature_K": temp_k,
                "temperature_digits": temp_digits,
                "pressure_kPa": press_kpa,
                "pressure_digits": press_digits,
                "property_phase": prop_phase,
                "ref_phase": ref_phase,
                "component_org_num": (
                    doi_comp_id(prop_comp_ref) if prop_comp_ref is not None else None
                ),
                "uncertainty": uncert,
            })

        # -- Variables --
        block_variables = []
        var_num_to_type = {}
        for var in blk.get("Variable", []):
            vnum = var.get("nVarNumber")
            if vnum is None:
                raise ValueError(
                    f"Variable declaration without nVarNumber in "
                    f"{doi!r} {block_label}"
                )
            if vnum in var_num_to_type:
                raise ValueError(
                    f"Duplicate variable declaration {vnum!r} in "
                    f"{doi!r} {block_label}"
                )
            vid = var.get("VariableID", {})
            vtype_dict = vid.get("VariableType", {})
            vname, vcat = extract_var_or_constraint_type(vtype_dict)

            var_phase = _enrich_phase(extract_phase_info(var.get("VarPhaseID")), index)
            var_comp_ref = vid.get("RegNum", {}).get("nOrgNum")

            # Canonical variable lookup
            var_row = index.lookup_variable(vname, var_comp_ref is not None)
            if var_row is None:
                raise ValueError(f"Variable registry lookup failed for {vname!r} in DOI {doi!r}")
            var_num_id = var_row["var_num_id"]
            var_id = ThermoMLIndex.resolve_id(var_row["var_id"], var_comp_ref)

            var_num_to_type[vnum] = (vname, vcat)

            block_variables.append({
                "BLKvar_id": block_local_id("var", vnum),
                "var_num_id": var_num_id,
                "var_id": var_id,
                "type": vcat,
                "name": vname,
                "phase": var_phase,
                "component_org_num": (
                    doi_comp_id(var_comp_ref) if var_comp_ref is not None else None
                ),
            })

        # -- Constraints --
        block_constraints = []
        declared_constraint_numbers = set()
        for constr in blk.get("Constraint", []):
            cnum = constr.get("nConstraintNumber")
            if cnum is None:
                raise ValueError(
                    f"Constraint declaration without nConstraintNumber in "
                    f"{doi!r} {block_label}"
                )
            if cnum in declared_constraint_numbers:
                raise ValueError(
                    f"Duplicate constraint declaration {cnum!r} in "
                    f"{doi!r} {block_label}"
                )
            declared_constraint_numbers.add(cnum)
            cid = constr.get("ConstraintID", {})
            ctype_dict = cid.get("ConstraintType", {})
            cname, ccat = extract_var_or_constraint_type(ctype_dict)

            constr_phase = _enrich_phase(extract_phase_info(constr.get("ConstraintPhaseID")), index)
            constr_comp_ref = cid.get("RegNum", {}).get("nOrgNum")
            cval = safe_float(constr.get("nConstraintValue"))
            cdigits = safe_int(constr.get("nConstrDigits"))
            if cval is not None and not math.isfinite(cval):
                raise ValueError(
                    f"Constraint {cnum!r} has nonfinite value in "
                    f"{doi!r} {block_label}"
                )
            # Canonical constraint lookup
            constr_row = index.lookup_constraint(cname, constr_comp_ref is not None)
            if constr_row is None:
                raise ValueError(
                    f"Constraint registry lookup failed for {cname!r} in DOI {doi!r}"
                )
            constr_num_id = constr_row["constr_num_id"]
            constr_id = ThermoMLIndex.resolve_id(constr_row["constr_id"], constr_comp_ref)
            if cval is not None and math.isfinite(cval):
                if ccat == "eTemperature":
                    all_temps.append(cval)
                elif ccat == "ePressure":
                    all_pressures.append(cval)

            block_constraints.append({
                "BLKconstr_id": block_local_id("constr", cnum),
                "constr_num_id": constr_num_id,
                "constr_id": constr_id,
                "type": ccat,
                "name": cname,
                "value": cval,
                "digits": cdigits,
                "phase": constr_phase,
                "component_org_num": (
                    doi_comp_id(constr_comp_ref) if constr_comp_ref is not None else None
                ),
            })

        # -- Data Points --
        num_values = blk.get("NumValues", [])
        n_points = len(num_values)
        total_pts += n_points

        data_points = []
        prop_values_all = {}
        var_values_all = {}
        prop_limit_counts = {}

        for nv_idx, nv in enumerate(num_values):
            store_point = (
                max_datapoints_per_block is None
                or nv_idx < max_datapoints_per_block
            )
            var_vals = {}
            seen_var_numbers = set()
            for vv in nv.get("VariableValue", []):
                vnum = vv.get("nVarNumber")
                _validate_point_occurrence_number(
                    number=vnum,
                    declared_numbers=var_num_to_type,
                    seen_numbers=seen_var_numbers,
                    source_role="variable",
                    point_ordinal=nv_idx,
                    doi=doi,
                    block_label=block_label,
                )
                vval = safe_float(vv.get("nVarValue"))
                vdigits = safe_int(vv.get("nVarDigits"))
                if store_point:
                    var_vals[block_local_id("var", vnum)] = {
                        "value": (
                            vval
                            if vval is None or math.isfinite(vval)
                            else None
                        ),
                        "digits": vdigits,
                    }

                if vval is not None:
                    var_values_all.setdefault(vnum, []).append(vval)
                    _, vcat = var_num_to_type[vnum]
                    if vcat == "eTemperature" and math.isfinite(vval):
                        all_temps.append(vval)
                    elif vcat == "ePressure" and math.isfinite(vval):
                        all_pressures.append(vval)

            prop_vals = {}
            seen_prop_numbers = set()
            for pv in nv.get("PropertyValue", []):
                pnum = pv.get("nPropNumber")
                _validate_point_occurrence_number(
                    number=pnum,
                    declared_numbers=declared_prop_numbers,
                    seen_numbers=seen_prop_numbers,
                    source_role="property",
                    point_ordinal=nv_idx,
                    doi=doi,
                    block_label=block_label,
                )
                pval, is_limit_value = _property_numeric_value(pv)
                pdigits = safe_int(pv.get("nPropDigits"))
                if (
                    is_limit_value
                    and pval is not None
                    and not math.isfinite(pval)
                ):
                    raise ValueError(
                        f"Data point {nv_idx} property {pnum!r} has a "
                        f"nonfinite limit value in {doi!r} {block_label}"
                    )

                pt_uncert = None
                pt_comb = pv.get("CombinedUncertainty") if store_point else None
                if store_point and isinstance(pt_comb, dict):
                    exp_val = safe_float(pt_comb.get("nCombExpandUncertValue"))
                    if exp_val is not None:
                        pt_uncert = {
                            "expanded_value": (
                                exp_val if math.isfinite(exp_val) else None
                            ),
                            "assessment_num": (
                                property_assessment_id(pnum, pt_comb["nCombUncertAssessNum"])
                                if "nCombUncertAssessNum" in pt_comb else None
                            ),
                        }

                property_cell = {
                    "value": None if is_limit_value else pval,
                    "digits": pdigits,
                    "point_uncertainty": pt_uncert,
                }
                if store_point:
                    if (
                        property_cell["value"] is not None
                        and not math.isfinite(property_cell["value"])
                    ):
                        property_cell["value"] = None
                    prop_vals[block_local_id("prop", pnum)] = property_cell

                if pval is not None:
                    if is_limit_value:
                        prop_limit_counts[pnum] = (
                            prop_limit_counts.get(pnum, 0) + 1
                        )
                    else:
                        prop_values_all.setdefault(pnum, []).append(pval)
            if store_point:
                data_points.append({
                    "BLKpoint_id": block_local_id("point", nv_idx + 1),
                    "variable_values": var_vals,
                    "property_values": prop_vals,
                })

        # -- Data Summary --
        data_summary = _build_data_summary(
            block_properties, block_variables, block_constraints,
            block_compounds, prop_values_all, var_values_all, n_points,
            blk.get("PhaseID", []), index,
        )
        composition_subsystems, point_subsystem_refs = _build_composition_subsystems(
            block_type=btype,
            block_compounds=block_compounds,
            block_properties=block_properties,
            block_variables=block_variables,
            block_constraints=block_constraints,
            block_solvents=block_solvents,
            property_solvent_scopes=property_solvent_scopes,
            raw_num_values=num_values,
        )
        composition_subsystem_indexes[block_label] = composition_subsystems
        for point in data_points:
            point["BLKsubsys_refs"] = point_subsystem_refs.get(
                point["BLKpoint_id"], []
            )
        effective_system_summary = _effective_system_summary(
            composition_subsystems
        )
        data_summary["effective_system_summary"] = effective_system_summary
        if block_label in block_search_adv_indexes:
            raise ValueError(f"Duplicate block identity-index key {block_label!r}")
        block_search_adv_indexes[block_label] = build_block_identity_index(
            properties=block_properties,
            variables=block_variables,
            constraints=block_constraints,
            compounds=block_compounds,
            property_values=prop_values_all,
            variable_values=var_values_all,
            n_points=n_points,
            translations=identity_translations,
            property_limit_counts=prop_limit_counts,
            block_type=btype,
        )

        # -- Reaction (ReactionData only) --
        reaction = None
        if btype == "ReactionData":
            participants = []
            for p in blk.get("Participant", []):
                rn = p.get("RegNum", {})
                on = rn.get("nOrgNum")
                if on is None:
                    raise ValueError(f"Reaction participant without org_num in DOI {doi!r}")
                phase_name = p.get("ePhase")
                phase_row = index.lookup_phase(phase_name) if phase_name else None
                if phase_name and phase_row is None:
                    raise ValueError(
                        f"Phase registry lookup failed for {phase_name!r} in DOI {doi!r}"
                    )
                participant_comp = comp_lookup.get(on)
                if participant_comp is None:
                    raise ValueError(
                        f"Reaction participant {on!r} has no DOI compound resolution "
                        f"in DOI {doi!r}"
                    )
                stoichiometric_coef = safe_float(
                    p.get("nStoichiometricCoef")
                )
                if (
                    stoichiometric_coef is not None
                    and not math.isfinite(stoichiometric_coef)
                ):
                    raise ValueError(
                        f"Reaction participant {on!r} has nonfinite "
                        f"stoichiometric coefficient in DOI {doi!r}"
                    )
                participants.append({
                    "org_num": doi_comp_id(on),
                    "comp_num_id": participant_comp["comp_num_id"],
                    "phase": phase_name,
                    "phase_num_id": phase_row["phase_num_id"] if phase_row else None,
                    "phase_id": phase_row["phase_id"] if phase_row else None,
                    "sample_num": (
                        doi_comp_sample_id(on, p["nSampleNm"])
                        if p.get("nSampleNm") is not None else None
                    ),
                    "stoichiometric_coef": stoichiometric_coef,
                })
            source_reaction_type = blk.get("eReactionType")
            reaction_type = source_reaction_type or "Unreported reaction type"
            rxn_type_row = index.lookup_reaction_type(reaction_type)
            if rxn_type_row is None:
                raise ValueError(
                    f"Reaction-type registry lookup failed for {reaction_type!r} in DOI {doi!r}"
                )
            reaction = {
                "reaction_type": reaction_type,
                "source_reaction_type": source_reaction_type,
                "rxn_type_num_id": rxn_type_row["rxn_type_num_id"],
                "rxn_type_id": rxn_type_row["rxn_type_id"],
                "participants": participants,
            }

        # -- Provenance --
        provenance = {
            "date_added": blk.get("dateDateAdded"),
            "compiler": blk.get("sCompiler"),
            "contributor": blk.get("sContributor"),
            "experimental_purpose": blk.get("eExpPurpose"),
        }

        block_out = {
            "block_number": block_label,
            "block_type": btype,
            "system_type": sys_type,
            "blocktype_num_id": blocktype_row["blocktype_num_id"],
            "compounds": block_compounds,
            "properties": block_properties,
            "solvents": block_solvents,
            "variables": block_variables,
            "constraints": block_constraints,
            "data_summary": data_summary,
            "data_points": data_points,
            "reaction": reaction,
            "auxiliary": None,
            "equation": None,
            "provenance": provenance,
        }
        blocks_out.append(block_out)

        block_index.append({
            "block_number": block_label,
            "block_type": btype,
            "property_names": block_prop_names,
            "property_group": block_prop_group,
            "system_type": sys_type,
            "blocktype_num_id": blocktype_row["blocktype_num_id"],
            "n_points": n_points,
            "method": block_method,
            "effective_system_types": effective_system_summary["system_types"],
            "n_composition_subsystems": effective_system_summary["n_subsystems"],
            "subsystem_matching_points": effective_system_summary["n_unique_points"],
        })

    # -- Blocks Summary --
    blocks_summary = {
        "n_blocks": len(blocks_out),
        "n_pure_or_mixture": sum(1 for b in blocks_out if b["block_type"] == "PureOrMixtureData"),
        "n_reaction": sum(1 for b in blocks_out if b["block_type"] == "ReactionData"),
        "property_names": sorted(all_prop_names),
        "property_groups": sorted(all_prop_groups),
        "compound_names": sorted(all_compound_names),
        "system_types": sorted(all_system_types),
        "methods": sorted(all_methods),
        "temperature_range_K": ({"min": round(min(all_temps), 2), "max": round(max(all_temps), 2)}
                                if all_temps else None),
        "pressure_range_kPa": ({"min": round(min(all_pressures), 3), "max": round(max(all_pressures), 3)}
                                if all_pressures else None),
        "total_datapoints": total_pts,
        "block_index": block_index,
        "derived_indexes": {
            "block_search_adv": block_search_adv_indexes,
            "composition_subsystems": composition_subsystem_indexes,
        },
    }

    return {
        "key": {"doi": doi, "lit_id": lit_id, "lit_num_id": lit_num_id},
        "paper": {"doi": doi, "title": cit.get("sTitle", "")},
        "blocks_summary": blocks_summary,
        "blocks": blocks_out,
    }


_COMPOSITION_TYPE_KEYS = frozenset(
    {"eComponentComposition", "eSolventComposition"}
)


def _composition_scope(declaration):
    """Return a strict semantic scope for one composition declaration."""
    domain = declaration.get("type")
    component = declaration.get("component_org_num")
    if domain not in _COMPOSITION_TYPE_KEYS or component is None:
        return None
    phase = declaration.get("phase") or {}
    return (
        domain,
        " ".join(str(declaration.get("name") or "").casefold().split()),
        phase.get("phase_num_id"),
        phase.get("phase_id"),
        phase.get("component_org_num"),
    )


def _point_runs(point_ordinals):
    """Compress sorted one-based point ordinals into inclusive runs."""
    ordered = sorted(set(point_ordinals))
    if not ordered:
        return []
    runs = []
    start = previous = ordered[0]
    for ordinal in ordered[1:]:
        if ordinal == previous + 1:
            previous = ordinal
            continue
        runs.append([start, previous])
        start = previous = ordinal
    runs.append([start, previous])
    return runs


def _component_projection(component):
    return {
        "org_num": component["org_num"],
        "comp_num_id": component["comp_num_id"],
        "name": component["name"],
        "inchi_key": component["inchi_key"],
    }


def _phase_compatible(property_declaration, scope):
    property_phase = property_declaration.get("property_phase") or {}
    scope_phase_num_id = scope[2]
    property_phase_num_id = property_phase.get("phase_num_id")
    return (
        scope_phase_num_id is None
        or property_phase_num_id is None
        or scope_phase_num_id == property_phase_num_id
    )


def _candidate_retained_sets(parent_components, exact_zero_components):
    """Return unary/binary faces supported by exact zero evidence.

    A unary endpoint is also topologically part of each binary face obtained
    by restoring one exactly-zero component. Those endpoint-only faces remain
    non-searchable until at least one genuinely binary point is observed.
    """
    parent = set(parent_components)
    zero = set(exact_zero_components)
    direct = parent - zero
    if not direct or len(direct) > 2:
        return []
    candidates = {tuple(sorted(direct))}
    if len(direct) == 1:
        for restored in zero:
            candidate = tuple(sorted(direct | {restored}))
            if len(candidate) == 2:
                candidates.add(candidate)
    return sorted(candidates, key=lambda value: (len(value), value))


def _build_composition_subsystems(
    *,
    block_type,
    block_compounds,
    block_properties,
    block_variables,
    block_constraints,
    block_solvents,
    property_solvent_scopes,
    raw_num_values,
):
    """Classify composition-defined unary/binary projections of one block.

    This is the single authoritative classification pass. It never infers
    absence from a missing cell or an arbitrary numerical tolerance: only an
    exact, finite, reported zero in a component-linked composition variable
    or constraint can exclude a component. Reaction blocks deliberately have
    no projection semantics.
    """
    if block_type != "PureOrMixtureData" or len(block_compounds) < 2:
        return [], {}

    components_by_org = {
        component["org_num"]: component for component in block_compounds
    }
    parent_orgs = tuple(sorted(components_by_org))
    variables_by_number = {
        block_local_ordinal("var", variable["BLKvar_id"]): variable
        for variable in block_variables
    }
    properties_by_number = {
        block_local_ordinal("prop", prop["BLKprop_id"]): prop
        for prop in block_properties
    }

    fixed_zero_by_scope = defaultdict(set)
    fixed_invalid_scopes = set()
    for constraint in block_constraints:
        scope = _composition_scope(constraint)
        if scope is None:
            continue
        value = constraint.get("value")
        if value is None or not math.isfinite(value) or value < 0:
            fixed_invalid_scopes.add(scope)
        elif value == 0:
            fixed_zero_by_scope[scope].add(constraint["component_org_num"])

    accumulators = {}
    for point_ordinal, raw_point in enumerate(raw_num_values, start=1):
        values_by_scope = defaultdict(dict)
        invalid_scopes = set(fixed_invalid_scopes)
        for raw_value in raw_point.get("VariableValue", []):
            declaration = variables_by_number.get(raw_value.get("nVarNumber"))
            if declaration is None:
                continue
            scope = _composition_scope(declaration)
            if scope is None:
                continue
            value = safe_float(raw_value.get("nVarValue"))
            component = declaration["component_org_num"]
            if value is None or not math.isfinite(value) or value < 0:
                invalid_scopes.add(scope)
                continue
            values_by_scope[scope][component] = {
                "value": value,
                "digits": safe_int(raw_value.get("nVarDigits")),
                "source": declaration["BLKvar_id"],
            }

        all_scopes = set(values_by_scope) | set(fixed_zero_by_scope)
        for scope in sorted(all_scopes, key=lambda value: tuple(str(v) for v in value)):
            if scope in invalid_scopes:
                continue
            exact_zero = set(fixed_zero_by_scope.get(scope, ()))
            exact_zero.update(
                component
                for component, evidence in values_by_scope.get(scope, {}).items()
                if evidence["value"] == 0
            )
            if not exact_zero or not exact_zero.issubset(components_by_org):
                continue
            direct_retained = set(parent_orgs) - exact_zero
            for retained_tuple in _candidate_retained_sets(parent_orgs, exact_zero):
                key = (scope, retained_tuple)
                accumulator = accumulators.setdefault(
                    key,
                    {
                        "points": set(),
                        "point_arities": defaultdict(int),
                        "evidence_sources": set(),
                        "condition_values": defaultdict(list),
                        "property_support": {},
                    },
                )
                accumulator["points"].add(point_ordinal)
                accumulator["point_arities"][len(direct_retained)] += 1
                accumulator["evidence_sources"].update(
                    evidence["source"]
                    for component, evidence in values_by_scope.get(scope, {}).items()
                    if component in exact_zero and evidence["value"] == 0
                )
                accumulator["evidence_sources"].update(
                    constraint["BLKconstr_id"]
                    for constraint in block_constraints
                    if _composition_scope(constraint) == scope
                    and constraint.get("value") == 0
                )

                for raw_value in raw_point.get("VariableValue", []):
                    declaration = variables_by_number.get(raw_value.get("nVarNumber"))
                    if declaration is None or _composition_scope(declaration) is not None:
                        continue
                    value = safe_float(raw_value.get("nVarValue"))
                    if value is not None and math.isfinite(value):
                        accumulator["condition_values"][declaration["BLKvar_id"]].append(value)

                excluded = set(parent_orgs) - set(retained_tuple)
                for raw_property in raw_point.get("PropertyValue", []):
                    prop = properties_by_number.get(raw_property.get("nPropNumber"))
                    if prop is None:
                        continue
                    component = prop.get("component_org_num")
                    role = "limiting_probe" if component in excluded else "bulk_property"
                    support_key = (prop["BLKprop_id"], role)
                    accumulator["property_support"][support_key] = {
                        "BLKprop_id": prop["BLKprop_id"],
                        "prop_num_id": prop["prop_num_id"],
                        "prop_ID": prop["prop_ID"],
                        "component_org_num": component,
                        "role": role,
                        "phase_compatible": _phase_compatible(prop, scope),
                        "solvent_component_org_nums": property_solvent_scopes.get(
                            prop["BLKprop_id"], []
                        ),
                    }

    ordered_keys = sorted(
        accumulators,
        key=lambda key: (
            tuple(str(value) for value in key[0]),
            len(key[1]),
            key[1],
        ),
    )
    subsystems = []
    point_refs = defaultdict(list)
    variables_by_id = {item["BLKvar_id"]: item for item in block_variables}
    solvent_orgs = sorted(
        solvent["component_org_num"] for solvent in block_solvents
    )
    for subsystem_ordinal, key in enumerate(ordered_keys, start=1):
        scope, retained_tuple = key
        accumulator = accumulators[key]
        retained = set(retained_tuple)
        excluded = set(parent_orgs) - retained
        effective_system_type = system_type_label(len(retained))
        has_full_arity_point = accumulator["point_arities"].get(len(retained), 0) > 0
        search_eligible = len(retained) == 1 or has_full_arity_point
        subsystem_id = block_local_id("subsys", subsystem_ordinal)
        condition_ranges = []
        for local_id, values in sorted(accumulator["condition_values"].items()):
            declaration = variables_by_id[local_id]
            condition_ranges.append({
                "BLKvar_id": local_id,
                "var_num_id": declaration["var_num_id"],
                "var_id": declaration["var_id"],
                "name": declaration["name"],
                "min": round(min(values), 12),
                "max": round(max(values), 12),
                "n": len(values),
            })
        subsystem = {
            "BLKsubsys_id": subsystem_id,
            "relationship": "composition_subset_of_declared_system",
            "scope": {
                "composition_domain": scope[0],
                "basis": scope[1],
                "phase_num_id": scope[2],
                "phase_id": scope[3],
                "phase_component_org_num": scope[4],
                "solvent_component_org_nums": solvent_orgs,
            },
            "effective_system_type": effective_system_type,
            "n_retained_components": len(retained),
            "retained_components": [
                _component_projection(components_by_org[org])
                for org in sorted(retained)
            ],
            "excluded_components": [
                _component_projection(components_by_org[org])
                for org in sorted(excluded)
            ],
            "point_membership": {
                "encoding": "one_based_inclusive_runs",
                "runs": _point_runs(accumulator["points"]),
            },
            "n_points": len(accumulator["points"]),
            "point_arity_counts": {
                system_type_label(arity): count
                for arity, count in sorted(accumulator["point_arities"].items())
            },
            "evidence_quality": "exact_reported_zero",
            "evidence_sources": sorted(accumulator["evidence_sources"]),
            "search_eligible": search_eligible,
            "path_class": (
                "unary_endpoint"
                if len(retained) == 1
                else "binary_face" if search_eligible else "endpoint_only_binary_face"
            ),
            "property_support": sorted(
                accumulator["property_support"].values(),
                key=lambda item: (item["BLKprop_id"], item["role"]),
            ),
            "condition_ranges": condition_ranges,
            "quality_flags": (
                [] if search_eligible else ["no_full_arity_point"]
            ),
        }
        subsystems.append(subsystem)
        for point_ordinal in accumulator["points"]:
            point_refs[block_local_id("point", point_ordinal)].append(subsystem_id)

    return subsystems, {
        point_id: sorted(refs, key=lambda value: block_local_ordinal("subsys", value))
        for point_id, refs in point_refs.items()
    }


def _effective_system_summary(subsystems):
    point_ids = set()
    for subsystem in subsystems:
        for start, end in subsystem["point_membership"]["runs"]:
            point_ids.update(range(start, end + 1))
    return {
        "n_subsystems": len(subsystems),
        "system_types": sorted(
            {subsystem["effective_system_type"] for subsystem in subsystems}
        ),
        "n_search_eligible": sum(
            1 for subsystem in subsystems if subsystem["search_eligible"]
        ),
        "n_unique_points": len(point_ids),
    }


def _enrich_phase(phase_info, index):
    """Add phase_num_id and phase_id from index to phase info dict."""
    if not phase_info:
        return None
    ph_row = index.lookup_phase(phase_info["phase"])
    if ph_row is None:
        raise ValueError(f"Phase registry lookup failed for {phase_info['phase']!r}")
    phase_info["phase_num_id"] = ph_row["phase_num_id"]
    phase_info["phase_id"] = ph_row["phase_id"]
    return phase_info


def _build_data_summary(properties, variables, constraints, compounds,
                         prop_values_all, var_values_all, n_points, phase_ids, index):
    """Build per-block data summary with indexed fields."""
    prop_stats = {}
    for prop in properties:
        pnum = block_local_ordinal("prop", prop["BLKprop_id"])
        vals = [
            value
            for value in prop_values_all.get(pnum, [])
            if math.isfinite(value)
        ]
        if vals:
            prop_stats[prop["BLKprop_id"]] = {
                "BLKprop_id": prop["BLKprop_id"],
                "name": prop["name"],
                "min": round(min(vals), 6),
                "max": round(max(vals), 6),
                "mean": round(sum(vals) / len(vals), 6),
                "std": round(_std(vals), 6) if len(vals) > 1 else 0,
                "n": len(vals),
            }

    var_ranges = {}
    for var in variables:
        vnum = block_local_ordinal("var", var["BLKvar_id"])
        vals = [
            value
            for value in var_values_all.get(vnum, [])
            if math.isfinite(value)
        ]
        if vals:
            var_ranges[var["BLKvar_id"]] = {
                "BLKvar_id": var["BLKvar_id"],
                "name": var["name"],
                "min": round(min(vals), 6),
                "max": round(max(vals), 6),
                "n_unique": len(set(vals)),
            }

    constr_summary = {}
    for constr in constraints:
        constr_summary[constr["BLKconstr_id"]] = {
            "name": constr["name"],
            "value": constr["value"],
            "digits": constr["digits"],
            "phase": constr["phase"],
            "component_org_num": constr["component_org_num"],
        }

    phases = []
    for pid in phase_ids:
        p = pid.get("ePhase")
        if p and p not in phases:
            phases.append(p)

    methods = list(set(
        p.get("method_standard") or p.get("method_custom") or ""
        for p in properties if (p.get("method_standard") or p.get("method_custom"))
    ))

    return {
        "property_names": [p["name"] for p in properties],
        "property_group": properties[0]["group"] if properties else "",
        "methods": methods,
        "system_type": system_type_label(len(compounds)),
        "compound_names": [c["name"] for c in compounds],
        "phases": phases,
        "constraints_summary": constr_summary,
        "n_points": n_points,
        "property_stats": prop_stats,
        "variable_ranges": var_ranges,
    }


def _property_numeric_value(property_value):
    """Return a numeric property value and whether it came from PropLimit."""
    reported = safe_float(property_value.get("nPropValue"))
    if reported is not None:
        return reported, False
    prop_limit = property_value.get("PropLimit")
    if isinstance(prop_limit, dict):
        limit_value = safe_float(prop_limit.get("nPropLimitValue"))
        if limit_value is not None:
            return limit_value, True
    return None, False


def _validate_point_occurrence_number(
    *,
    number,
    declared_numbers,
    seen_numbers,
    source_role,
    point_ordinal,
    doi,
    block_label,
):
    """Reject orphan or duplicate property/variable cells in one raw row."""
    if number not in declared_numbers:
        raise ValueError(
            f"Data point {point_ordinal} references undeclared {source_role} "
            f"{number!r} in {doi!r} {block_label}"
        )
    if number in seen_numbers:
        raise ValueError(
            f"Data point {point_ordinal} repeats {source_role} {number!r} in "
            f"{doi!r} {block_label}"
        )
    seen_numbers.add(number)


def _std(vals):
    """Sample standard deviation."""
    n = len(vals)
    if n < 2:
        return 0.0
    mean = sum(vals) / n
    return math.sqrt(sum((v - mean) ** 2 for v in vals) / (n - 1))
