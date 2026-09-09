"""
CCS (Component Card Schema) INDIV card builder -- per-DOI sample/purity card.

Produces one card per paper with compound sample provenance and purity information.
All compounds are indexed using canonical IDs from the CSV registry.
"""

from ThermoML_raw_json_to_card_db_parsers.shared_utils import extract_trc_ref_id, safe_float, safe_int
from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    doi_comp_id,
    doi_comp_sample_id,
)


def build_ccs_card(data, index):
    """Build Component Card Schema INDIV (sample/purity) card.

    Args:
        data: Parsed ThermoML JSON dict for one paper.
        index: ThermoMLIndex instance for canonical ID lookups.
    """
    cit = data.get("Citation", {})
    doi = cit.get("sDOI", "")
    lit_id, _ = extract_trc_ref_id(cit.get("TRCRefID"))

    ref_row = index.lookup_reference(doi)
    if ref_row is None:
        raise ValueError(f"Reference registry has no canonical ID for DOI {doi!r}")
    lit_num_id = ref_row["lit_num_id"]

    compounds_out = []
    for comp in data.get("Compound", []):
        reg = comp.get("RegNum", {})
        org_num = reg.get("nOrgNum")
        if org_num is None:
            continue

        # Canonical compound lookup
        inchi_key = comp.get("sStandardInChIKey")
        inchi = comp.get("sStandardInChI")
        names = comp.get("sCommonName", [])
        if isinstance(names, str):
            names = [names]
        formula = comp.get("sFormulaMolec", "")
        comp_row = index.lookup_compound(
            inchi_key=inchi_key, standard_inchi=inchi,
            common_name=names[0] if names else None, formula=formula)
        if comp_row is None:
            raise ValueError(
                f"Compound registry lookup failed for DOI {doi!r}, org_num={org_num!r}"
            )
        comp_num_id = comp_row["comp_num_id"]
        resolved_ik = inchi_key or comp_row["inchi_key"]

        samples_out = []
        samples = comp.get("Sample", [])
        if isinstance(samples, dict):
            samples = [samples]

        for sample in samples:
            purity_steps = []
            purities = sample.get("purity", [])
            if isinstance(purities, dict):
                purities = [purities]

            for pur in purities:
                step = {
                    "step": safe_int(pur.get("nStep")),
                    "purity": {
                        "mass_fraction": safe_float(pur.get("nPurityMass")),
                        "mass_fraction_digits": safe_int(pur.get("nPurityMassDigits")),
                        "mol_fraction": safe_float(pur.get("nPurityMol")),
                        "mol_fraction_digits": safe_int(pur.get("nPurityMolDigits")),
                        "vol_fraction": safe_float(pur.get("nPurityVol")),
                        "vol_fraction_digits": safe_int(pur.get("nPurityVolDigits")),
                    },
                    "impurities": {
                        "water_mass_pct": safe_float(pur.get("nWaterMassPerCent")),
                        "water_mass_pct_digits": safe_int(pur.get("nWaterMassPerCentDigits")),
                        "halide_mass_pct": safe_float(pur.get("nHalideMassPerCent")),
                        "halide_mass_pct_digits": safe_int(pur.get("nHalideMassPerCentDigits")),
                    },
                    "analysis_methods": _extract_methods_list(pur, "eAnalMeth", "sAnalMeth"),
                    "purification_methods": _extract_methods_list(pur, "ePurifMethod", "sPurifMethod"),
                }
                purity_steps.append(step)

            sample_num = sample.get("nSampleNm")
            if sample_num is None:
                raise ValueError(
                    f"Sample without nSampleNm in DOI {doi!r}, org_num={org_num!r}"
                )
            samples_out.append({
                "sample_num": doi_comp_sample_id(org_num, sample_num),
                "source": sample.get("eSource"),
                "status": sample.get("eStatus"),
                "purity_steps": purity_steps if purity_steps else None,
            })

        compounds_out.append({
            "org_num": doi_comp_id(org_num),
            "comp_num_id": comp_num_id,
            "inchi_key": resolved_ik,
            "name": names[0] if names else (comp_row["common_name"] if comp_row else ""),
            "formula": comp.get("sFormulaMolec", ""),
            "samples": samples_out if samples_out else None,
        })

    return {
        "key": {"doi": doi, "lit_id": lit_id, "lit_num_id": lit_num_id},
        "compounds": compounds_out,
    }


def _extract_methods_list(pur_dict, standard_key, custom_key):
    """Extract analysis/purification methods from purity step."""
    methods = []
    std = pur_dict.get(standard_key, [])
    if isinstance(std, str):
        std = [std]
    methods.extend(std)
    cust = pur_dict.get(custom_key, [])
    if isinstance(cust, str):
        cust = [cust]
    for c in cust:
        methods.append(f"[custom] {c}")
    return methods if methods else None
