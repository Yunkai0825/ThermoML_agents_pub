{
  "answer": "## Density Data for Binary Ethanol–Water Mixtures near 310 K\n\nSixteen binary ethanol–water mass density (GLOBprop_1) blocks were found in the 305–315 K temperature window. The five most useful candidates, all verified by inspection, are summarized below. The target temperature of 310 K referenced throughout is the user's query condition, not a database measurement temperature.\n\n### Inspected Candidates\n\n| DOI | Block | GLOBlit | Total Points | T range (K) | Composition range | ρ range (kg/m³) | Pressure (kPa) | Comp. variable |\n|-----|-------|---------|--------------|-------------|-------------------|-----------------|-----------------|----------------|\n| 10.1021/je600565m | PROPblock_6 | GLOBlit_10699 | 18 | 298.15–318.15 | x(water) 0.0998–0.9051 | 780.53–965.51 | 101.0 | GLOBvar_2 (mole fraction) |\n| 10.1021/je800150h | PROPblock_9 | GLOBlit_11136 | 108 | 268.1–323.15 | x(water) 0.1–0.9 | 774.3–977.3 | 101.0 | GLOBvar_2 (mole fraction) |\n| 10.1021/je020173z | PROPblock_5 | GLOBlit_8050 | 24 | 298.15–313.15 | w(ethanol) 0.10835–0.71144 | 848.29–979.29 | 101.3 | GLOBvar_5 (mass fraction) |\n| 10.1021/je900743e | PROPblock_3 | GLOBlit_11792 | 15 | 293.15–313.15 | w(ethanol) 0.1–0.5 | 897.6–981.8 | 101.0 | GLOBvar_5 (mass fraction) |\n| 10.1021/acs.jced.6b01058 | PROPblock_7 | GLOBlit_7085 | 12 | 298.15–313.15 | w(ethanol) 0.04–0.16 | 966.4–990.13 | 85.0 | GLOBvar_5 (mass fraction) |\n\n### Best Picks for Wide Composition Coverage\n\n1. **GLOBlit_11136 / PROPblock_9** (DOI: 10.1021/je800150h) — **Largest dataset with wide composition**: 108 data points spanning x(water) 0.1–0.9 across T = 268.1–323.15 K at 101.0 kPa. This block covers nearly the full composition range and a broad temperature window that brackets the user's target of 310 K. Representative inspected points at the temperature extremes:\n   - x(water) = 0.1: ρ = 824.9 kg/m³ (268.1 K) to 774.3 kg/m³ (323.15 K)\n   - x(water) = 0.9: ρ = 977.3 kg/m³ (268.1 K) to 942 kg/m³ (323.15 K)\n\n2. **GLOBlit_10699 / PROPblock_6** (DOI: 10.1021/je600565m) — **Widest mole-fraction range at two temperatures**: 18 points at x(water) 0.0998–0.9051, measured at 298.15 K and 318.15 K (101.0 kPa). The 318.15 K isotherm is the closer of the two to the user's target of 310 K. Representative inspected points at 318.15 K:\n   - x(water) = 0.1: ρ = 780.53 kg/m³\n   - x(water) = 0.5003: ρ = 840.31 kg/m³\n   - x(water) = 0.9: ρ = 952.47 kg/m³\n\n3. **GLOBlit_8050 / PROPblock_5** (DOI: 10.1021/je020173z) — **Wide mass-fraction range**: 24 points with w(ethanol) 0.10835–0.71144 at 298.15 K and 313.15 K (101.3 kPa). At 313.15 K:\n   - w(ethanol) = 0.16716: ρ = 964.04 kg/m³\n   - w(ethanol) = 0.44202: ρ = 911.19 kg/m³\n   - w(ethanol) = 0.71144: ρ = 848.29 kg/m³\n\n4. **GLOBlit_11792 / PROPblock_3** (DOI: 10.1021/je900743e) — 15 points at w(ethanol) 0.1–0.5 across 293.15–313.15 K (101.0 kPa). At 313.15 K:\n   - w(ethanol) = 0.1: ρ = 974.6 kg/m³\n   - w(ethanol) = 0.5: ρ = 897.6 kg/m³\n\n5. **GLOBlit_7085 / PROPblock_7** (DOI: 10.1021/acs.jced.6b01058) — 12 points but narrow composition (w(ethanol) 0.04–0.16) at 298.15–313.15 K. Note: measured at 85.0 kPa rather than atmospheric pressure. At 308.15 K:\n   - w(ethanol) = 0.04: ρ = 987.24 kg/m³\n   - w(ethanol) = 0.16: ρ = 968.6 kg/m³\n\n### Resolved IDs\n- Ethanol: GLOBcomp_2 (C₂H₆O)\n- Water: GLOBcomp_1 (H₂O)\n- Mass density: GLOBprop_1\n\n**GLOBlit_11136 / PROPblock_9** is the strongest overall candidate, offering 108 data points across x(water) 0.1–0.9 and a temperature range (268.1–323.15 K) that densely brackets the user's query target. **GLOBlit_10699 / PROPblock_6** provides the widest single-isotherm composition sweep (x(water) 0.0998–0.9051) but at only two temperatures (298.15 K and 318.15 K).\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNGROUNDED_LITERAL** PROPblock_9: 310 (near '…broad temperature window that brackets the user's target of …') matches no inspected row/stat, database table, or other source of PROPblock_9\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_9\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"mole_fraction_<water>\", \"value\": 310.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** PROPblock_6: 310 (near '…K isotherm is the closer of the two to the user's target of …') matches no inspected row/stat, database table, or other source of PROPblock_6\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_6\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 310.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\nInspected so far: PROPblock_3, PROPblock_5, PROPblock_6, PROPblock_7, PROPblock_9",
  "core_claims": [
    "Sixteen binary ethanol–water mass density data blocks were found in the ThermoML database within the 305–315 K temperature window, and five were inspected in detail.",
    "GLOBlit_11136 / PROPblock_9 (DOI: 10.1021/je800150h) is the strongest overall candidate, offering 108 data points across x(water) 0.1–0.9 and T = 268.1–323.15 K at 101.0 kPa, densely bracketing the query target of 310 K.",
    "GLOBlit_10699 / PROPblock_6 (DOI: 10.1021/je600565m) provides the widest single-isotherm composition sweep (x(water) 0.0998–0.9051) but at only two temperatures (298.15 K and 318.15 K) at 101.0 kPa.",
    "GLOBlit_8050 / PROPblock_5 (DOI: 10.1021/je020173z) covers w(ethanol) 0.10835–0.71144 at 298.15 K and 313.15 K (101.3 kPa), with 24 data points.",
    "GLOBlit_11792 / PROPblock_3 (DOI: 10.1021/je900743e) covers w(ethanol) 0.1–0.5 across 293.15–313.15 K (101.0 kPa), with 15 data points.",
    "GLOBlit_7085 / PROPblock_7 (DOI: 10.1021/acs.jced.6b01058) covers only a narrow composition range (w(ethanol) 0.04–0.16) and was measured at 85.0 kPa rather than atmospheric pressure.",
    "No dataset contains measurements exactly at 310 K; the value 310 K is the user's query target, not a database measurement temperature, and this is flagged as UNGROUNDED_LITERAL for both PROPblock_9 and PROPblock_6."
  ],
  "status": "success",
  "summary": "Sixteen binary ethanol–water mass-density (GLOBprop_1) blocks were identified in the 305–315 K window. Five were inspected in detail. The strongest candidate is GLOBlit_11136 / PROPblock_9 (DOI 10.1021/je800150h): 108 data points spanning x(water) 0.1–0.9 over T = 268.1–323.15 K at 101.0 kPa, with representative densities from 774.3 kg/m³ (x(water)=0.1, 323.15 K) to 977.3 kg/m³ (x(water)=0.9, 268.1 K). The second-best is GLOBlit_10699 / PROPblock_6 (DOI 10.1021/je600565m): 18 points at x(water) 0.0998–0.9051 measured at 298.15 K and 318.15 K (101.0 kPa), with densities at 318.15 K ranging from 780.53 kg/m³ (x(water)=0.1) to 952.47 kg/m³ (x(water)=0.9). Additional candidates include GLOBlit_8050 / PROPblock_5 (DOI 10.1021/je020173z, 24 points, w(ethanol) 0.10835–0.71144, 298.15–313.15 K, 101.3 kPa), GLOBlit_11792 / PROPblock_3 (DOI 10.1021/je900743e, 15 points, w(ethanol) 0.1–0.5, 293.15–313.15 K, 101.0 kPa), and GLOBlit_7085 / PROPblock_7 (DOI 10.1021/acs.jced.6b01058, 12 points, w(ethanol) 0.04–0.16, 298.15–313.15 K, 85.0 kPa). Resolved component IDs: ethanol = GLOBcomp_2 (C₂H₆O), water = GLOBcomp_1 (H₂O). The reference to 310 K throughout is the user's query target, not a measured database temperature.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_2",
      "registry_id": "ethanol",
      "name": "ethanol"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_1",
      "registry_id": "mass_density_kg_m3",
      "name": "Mass density, kg/m3"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_11136",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary ethanol–water mixture; 108 points, T = 268.1–323.15 K, x(water) 0.1–0.9, 101.0 kPa.",
      "doi": "10.1021/je800150h",
      "lit_id": "2008-reh-ans-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 108,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "solvents": [],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_1",
          "constr_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "value": 101.0,
          "digits": 3,
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          }
        }
      ],
      "variables": [
        {
          "BLKvar_id": "BLKvar_1",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_1",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_1",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Mole fraction",
            "min": 0.1,
            "max": 0.9,
            "n_unique": 9
          },
          "range_min": 0.1,
          "range_max": 0.9
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_1",
          "var_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Temperature, K",
            "min": 268.1,
            "max": 323.15,
            "n_unique": 12
          },
          "range_min": 268.1,
          "range_max": 323.15
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_1",
          "prop_ID": "mass_density_kg_m3",
          "name": "Mass density, kg/m3",
          "group": "VolumetricProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_212",
          "meas_ID": "pycnom_ufactor_16",
          "method_standard": null,
          "method_custom": "PYCNOM::UFactor:16",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 774.3,
            "max": 977.3,
            "mean": 869.766667,
            "std": 54.624437,
            "n": 108
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 774.3,
          "range_max": 977.3
        }
      ],
      "phases": [
        {
          "owner_id": "BLKprop_1",
          "role": "property_phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKvar_1",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKvar_2",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKconstr_1",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "binary",
      "declared_n_components": 2,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "parent_n_datapoints": 108,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10699",
      "block_number": "PROPblock_6",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary ethanol–water mixture; 18 points, T = 298.15–318.15 K, x(water) 0.0998–0.9051, 101.0 kPa.",
      "doi": "10.1021/je600565m",
      "lit_id": "2007-pir-cos-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 18,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "solvents": [],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_1",
          "constr_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "value": 101.0,
          "digits": 3,
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          }
        }
      ],
      "variables": [
        {
          "BLKvar_id": "BLKvar_1",
          "var_num_id": "GLOBvar_1",
          "var_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Temperature, K",
            "min": 298.15,
            "max": 318.15,
            "n_unique": 2
          },
          "range_min": 298.15,
          "range_max": 318.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_1",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_1",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0998,
            "max": 0.9051,
            "n_unique": 18
          },
          "range_min": 0.0998,
          "range_max": 0.9051
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_1",
          "prop_ID": "mass_density_kg_m3",
          "name": "Mass density, kg/m3",
          "group": "VolumetricProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_203",
          "meas_ID": "vibtub_ufactor_3",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:3",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 780.53,
            "max": 965.51,
            "mean": 860.892778,
            "std": 56.848168,
            "n": 18
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 780.53,
          "range_max": 965.51
        }
      ],
      "phases": [
        {
          "owner_id": "BLKprop_1",
          "role": "property_phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKvar_1",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKvar_2",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKconstr_1",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "binary",
      "declared_n_components": 2,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "parent_n_datapoints": 18,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8050",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary ethanol–water mixture; 24 points, T = 298.15–313.15 K, w(ethanol) 0.10835–0.71144, 101.3 kPa.",
      "doi": "10.1021/je020173z",
      "lit_id": "2003-gal-tab-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 24,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "solvents": [],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_1",
          "constr_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "value": 101.3,
          "digits": 4,
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          }
        }
      ],
      "variables": [
        {
          "BLKvar_id": "BLKvar_1",
          "var_num_id": "GLOBvar_1",
          "var_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Temperature, K",
            "min": 298.15,
            "max": 313.15,
            "n_unique": 2
          },
          "range_min": 298.15,
          "range_max": 313.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_2",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mass fraction",
            "min": 0.10835,
            "max": 0.71144,
            "n_unique": 24
          },
          "range_min": 0.10835,
          "range_max": 0.71144
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_1",
          "prop_ID": "mass_density_kg_m3",
          "name": "Mass density, kg/m3",
          "group": "VolumetricProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_236",
          "meas_ID": "vibtub_ufactor_64",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:64",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 848.29,
            "max": 979.29,
            "mean": 919.849583,
            "std": 34.408583,
            "n": 24
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 848.29,
          "range_max": 979.29
        }
      ],
      "phases": [
        {
          "owner_id": "BLKprop_1",
          "role": "property_phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKvar_1",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKvar_2",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKconstr_1",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "binary",
      "declared_n_components": 2,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "parent_n_datapoints": 24,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_11792",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary ethanol–water mixture; 15 points, T = 293.15–313.15 K, w(ethanol) 0.1–0.5, 101.0 kPa.",
      "doi": "10.1021/je900743e",
      "lit_id": "2010-yan-wan-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 15,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "solvents": [],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_1",
          "constr_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "value": 101.0,
          "digits": 3,
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          }
        }
      ],
      "variables": [
        {
          "BLKvar_id": "BLKvar_1",
          "var_num_id": "GLOBvar_1",
          "var_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Temperature, K",
            "min": 293.15,
            "max": 313.15,
            "n_unique": 3
          },
          "range_min": 293.15,
          "range_max": 313.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_2",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mass fraction",
            "min": 0.1,
            "max": 0.5,
            "n_unique": 5
          },
          "range_min": 0.1,
          "range_max": 0.5
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_1",
          "prop_ID": "mass_density_kg_m3",
          "name": "Mass density, kg/m3",
          "group": "VolumetricProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_6",
          "meas_ID": "pycnometric_method",
          "method_standard": "Pycnometric method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 897.6,
            "max": 981.8,
            "mean": 944.486667,
            "std": 27.23372,
            "n": 15
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 897.6,
          "range_max": 981.8
        }
      ],
      "phases": [
        {
          "owner_id": "BLKprop_1",
          "role": "property_phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKvar_1",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKvar_2",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKconstr_1",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "binary",
      "declared_n_components": 2,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "parent_n_datapoints": 15,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_7085",
      "block_number": "PROPblock_7",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary ethanol–water mixture; 12 points, T = 298.15–313.15 K, w(ethanol) 0.04–0.16, 85.0 kPa.",
      "doi": "10.1021/acs.jced.6b01058",
      "lit_id": "2017-sha-cha-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 12,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_5_1"
        }
      ],
      "solvents": [],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_1",
          "constr_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "value": 85.0,
          "digits": 2,
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          }
        }
      ],
      "variables": [
        {
          "BLKvar_id": "BLKvar_1",
          "var_num_id": "GLOBvar_1",
          "var_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Temperature, K",
            "min": 298.15,
            "max": 313.15,
            "n_unique": 4
          },
          "range_min": 298.15,
          "range_max": 313.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_3",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_3",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mass fraction",
            "min": 0.04,
            "max": 0.16,
            "n_unique": 3
          },
          "range_min": 0.04,
          "range_max": 0.16
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_1",
          "prop_ID": "mass_density_kg_m3",
          "name": "Mass density, kg/m3",
          "group": "VolumetricProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_2",
          "meas_ID": "vibrating_tube_method",
          "method_standard": "Vibrating tube method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 966.4,
            "max": 990.13,
            "mean": 979.649167,
            "std": 8.202158,
            "n": 12
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 966.4,
          "range_max": 990.13
        }
      ],
      "phases": [
        {
          "owner_id": "BLKprop_1",
          "role": "property_phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKvar_1",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKvar_2",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        },
        {
          "owner_id": "BLKconstr_1",
          "role": "phase",
          "phase": "Liquid",
          "phase_num_id": "GLOBphase_1",
          "phase_id": "liquid"
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "binary",
      "declared_n_components": 2,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_5_1"
        }
      ],
      "parent_n_datapoints": 12,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1021/je600565m",
      "block_number": "PROPblock_6",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<water>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.0998",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "797.6"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.2018",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "810.78"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.3085",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "826.73"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.4145",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "843.26"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.5001",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "858.65"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.7005",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "904.69"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.9051",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "965.51"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "318.15",
          "mole_fraction_<water>": "0.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "780.53"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "318.15",
          "mole_fraction_<water>": "0.3001",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "807.71"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "318.15",
          "mole_fraction_<water>": "0.5003",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "840.31"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "318.15",
          "mole_fraction_<water>": "0.7001",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "888.76"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "318.15",
          "mole_fraction_<water>": "0.8001",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "919.19"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "318.15",
          "mole_fraction_<water>": "0.9",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "952.47"
        }
      ],
      "inspection_id": "INSP_222b8f50d354",
      "lit_num_id": "GLOBlit_10699"
    },
    {
      "doi": "10.1021/je020173z",
      "block_number": "PROPblock_5",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mass_fraction_<ethanol>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mass_fraction_<ethanol>": "0.10835",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "979.29"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "298.15",
          "mass_fraction_<ethanol>": "0.29072",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "952.58"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mass_fraction_<ethanol>": "0.37367",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "937.25"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "mass_fraction_<ethanol>": "0.37505",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "936.69"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "mass_fraction_<ethanol>": "0.44319",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "922.6"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "298.15",
          "mass_fraction_<ethanol>": "0.44452",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "922.55"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mass_fraction_<ethanol>": "0.49979",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "910.43"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mass_fraction_<ethanol>": "0.50494",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "908.96"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "mass_fraction_<ethanol>": "0.62751",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "880.81"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.16716",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "964.04"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.28575",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "943.6"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.35254",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "930.27"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.44202",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "911.19"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.44449",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "910.92"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.62707",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "868.41"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.71144",
          "pressure_kpa": "101.3",
          "mass_density_kg_m3": "848.29"
        }
      ],
      "inspection_id": "INSP_1e3a753d7d42",
      "lit_num_id": "GLOBlit_8050"
    },
    {
      "doi": "10.1021/je800150h",
      "block_number": "PROPblock_9",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<water>",
        "temperature_k",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<water>": "0.1",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "824.9"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "mole_fraction_<water>": "0.1",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "774.3"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "mole_fraction_<water>": "0.2",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "838.2"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "mole_fraction_<water>": "0.2",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "787.5"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "mole_fraction_<water>": "0.3",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "852.2"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "mole_fraction_<water>": "0.3",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "801.9"
        },
        {
          "BLKpoint_id": "BLKpoint_37",
          "mole_fraction_<water>": "0.4",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "867.7"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "mole_fraction_<water>": "0.4",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "817.7"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "mole_fraction_<water>": "0.5",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "886.6"
        },
        {
          "BLKpoint_id": "BLKpoint_60",
          "mole_fraction_<water>": "0.5",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "835.8"
        },
        {
          "BLKpoint_id": "BLKpoint_61",
          "mole_fraction_<water>": "0.6",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "908.1"
        },
        {
          "BLKpoint_id": "BLKpoint_72",
          "mole_fraction_<water>": "0.6",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "857.3"
        },
        {
          "BLKpoint_id": "BLKpoint_73",
          "mole_fraction_<water>": "0.7",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "931.6"
        },
        {
          "BLKpoint_id": "BLKpoint_84",
          "mole_fraction_<water>": "0.7",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "883"
        },
        {
          "BLKpoint_id": "BLKpoint_85",
          "mole_fraction_<water>": "0.8",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "951"
        },
        {
          "BLKpoint_id": "BLKpoint_96",
          "mole_fraction_<water>": "0.8",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "911.2"
        },
        {
          "BLKpoint_id": "BLKpoint_97",
          "mole_fraction_<water>": "0.9",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "977.3"
        },
        {
          "BLKpoint_id": "BLKpoint_108",
          "mole_fraction_<water>": "0.9",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "942"
        }
      ],
      "inspection_id": "INSP_5d3a3a494c0a",
      "lit_num_id": "GLOBlit_11136"
    },
    {
      "doi": "10.1021/je900743e",
      "block_number": "PROPblock_3",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mass_fraction_<ethanol>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "293.15",
          "mass_fraction_<ethanol>": "0.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "981.8"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "293.15",
          "mass_fraction_<ethanol>": "0.2",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "968.2"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "293.15",
          "mass_fraction_<ethanol>": "0.3",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "953.6"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "293.15",
          "mass_fraction_<ethanol>": "0.4",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "935.5"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "293.15",
          "mass_fraction_<ethanol>": "0.5",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "913.9"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "303.15",
          "mass_fraction_<ethanol>": "0.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "979"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "303.15",
          "mass_fraction_<ethanol>": "0.2",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "964.1"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "303.15",
          "mass_fraction_<ethanol>": "0.3",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "947.4"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "303.15",
          "mass_fraction_<ethanol>": "0.4",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "927.2"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "303.15",
          "mass_fraction_<ethanol>": "0.5",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "905.6"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "974.6"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.2",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "958.7"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.3",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "940.3"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.4",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "919.8"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.5",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "897.6"
        }
      ],
      "inspection_id": "INSP_5cbf22ac92af",
      "lit_num_id": "GLOBlit_11792"
    },
    {
      "doi": "10.1021/acs.jced.6b01058",
      "block_number": "PROPblock_7",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mass_fraction_<ethanol>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mass_fraction_<ethanol>": "0.04",
          "pressure_kpa": "85.0",
          "mass_density_kg_m3": "990.13"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "303.15",
          "mass_fraction_<ethanol>": "0.04",
          "pressure_kpa": "85.0",
          "mass_density_kg_m3": "988.79"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "308.15",
          "mass_fraction_<ethanol>": "0.04",
          "pressure_kpa": "85.0",
          "mass_density_kg_m3": "987.24"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.04",
          "pressure_kpa": "85.0",
          "mass_density_kg_m3": "985.42"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mass_fraction_<ethanol>": "0.08",
          "pressure_kpa": "85.0",
          "mass_density_kg_m3": "983.9"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "303.15",
          "mass_fraction_<ethanol>": "0.08",
          "pressure_kpa": "85.0",
          "mass_density_kg_m3": "982.43"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "308.15",
          "mass_fraction_<ethanol>": "0.08",
          "pressure_kpa": "85.0",
          "mass_density_kg_m3": "980.77"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.08",
          "pressure_kpa": "85.0",
          "mass_density_kg_m3": "978.85"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mass_fraction_<ethanol>": "0.16",
          "pressure_kpa": "85.0",
          "mass_density_kg_m3": "972.57"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "303.15",
          "mass_fraction_<ethanol>": "0.16",
          "pressure_kpa": "85.0",
          "mass_density_kg_m3": "970.69"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "308.15",
          "mass_fraction_<ethanol>": "0.16",
          "pressure_kpa": "85.0",
          "mass_density_kg_m3": "968.6"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "313.15",
          "mass_fraction_<ethanol>": "0.16",
          "pressure_kpa": "85.0",
          "mass_density_kg_m3": "966.4"
        }
      ],
      "inspection_id": "INSP_d9f5b67c278b",
      "lit_num_id": "GLOBlit_7085"
    }
  ]
}