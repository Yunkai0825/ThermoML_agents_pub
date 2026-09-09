{
  "answer": "## Density Data for Binary Acetonitrile + N,N-Dimethylformamide (DMF) at 298.15 K\n\nThree ThermoML data blocks contain mass density (GLOBprop_1, kg/m³) measurements for the binary system of acetonitrile (GLOBcomp_15) + N,N-dimethylformamide (GLOBcomp_18) at 298.15 K:\n\n### Block 1: GLOBlit_2659 / PROPblock_7\n- **DOI:** 10.1016/j.jct.2006.01.015\n- **Total data points:** 102 (full block T range: 293.15–318.15 K); 17 points at 298.15 K\n- **Composition variable:** Mole fraction of acetonitrile\n- **Pressure:** 101.0 kPa\n\nData at 298.15 K (inspection returned a shape-preserving subset of the 17 matched rows):\n\n| x(acetonitrile) | ρ (kg/m³) |\n|---|---|\n| 0 | 944.6 |\n| 0.0654 | 937.5 |\n| 0.1912 | 922.9 |\n| 0.2586 | 914.5 |\n| 0.3204 | 906.3 |\n| 0.3851 | 897.4 |\n| 0.4596 | 886.5 |\n| 0.5125 | 878.4 |\n| 0.5925 | 865.2 |\n| 0.6402 | 856.9 |\n| 0.6899 | 847.8 |\n| 0.7736 | 831.1 |\n| 0.8522 | 813.9 |\n| 0.9359 | 793.8 |\n| 1 | 776.8 |\n\n### Block 2: GLOBlit_4124 / PROPblock_5\n- **DOI:** 10.1016/j.jct.2014.02.019\n- **Total data points:** 20 (full block T range: 298.15–313.15 K); 5 points at 298.15 K\n- **Composition variable:** Mass fraction of DMF\n- **Pressure:** 101.0 kPa\n\nData at 298.15 K:\n\n| w(DMF) | ρ (kg/m³) |\n|---|---|\n| 0 | 776.47 |\n| 0.25 | 816.75 |\n| 0.5 | 856.92 |\n| 0.75 | 900.14 |\n| 1 | 944.65 |\n\n### Block 3: GLOBlit_7481 / PROPblock_16\n- **DOI:** 10.1021/acs.jced.8b00176\n- **Total data points:** 66 (full block T range: 298.15–323.15 K); 11 points at 298.15 K\n- **Composition variable:** Mole fraction of DMF\n- **Pressure:** 100.0 kPa\n\nData at 298.15 K:\n\n| x(DMF) | ρ (kg/m³) |\n|---|---|\n| 0 | 776.714 |\n| 0.0989 | 802.565 |\n| 0.1916 | 826.376 |\n| 0.2925 | 844.614 |\n| 0.3932 | 865.725 |\n| 0.5029 | 880.889 |\n| 0.6002 | 895.421 |\n| 0.6931 | 907.546 |\n| 0.7926 | 922.026 |\n| 0.8996 | 932.676 |\n| 1 | 943.934 |\n\n**Chemistry insight:** The density increases monotonically from pure acetonitrile to pure DMF at 298.15 K across all three independent studies. The pure-component endpoint values show excellent agreement: pure acetonitrile densities are 776.8 (PROPblock_7), 776.47 (PROPblock_5), and 776.714 kg/m³ (PROPblock_16), while pure DMF densities are 944.6 (PROPblock_7), 944.65 (PROPblock_5), and 943.934 kg/m³ (PROPblock_16), confirming high measurement consistency across the three sources.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **AMBIGUOUS_VALUE** PROPblock_16: 944.6 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_16\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 944.6})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **MISATTRIBUTED_VALUE** PROPblock_5: 943.934 does not belong to PROPblock_5; it matches only GLOBlit_7481::PROPblock_16 (inspected this run)\n  fix (required — this IS a database value, under a different block): `re-anchor 943.934 to GLOBlit_7481::PROPblock_16 — no new tool call needed`\nInspected so far: PROPblock_16, PROPblock_5, PROPblock_7",
  "core_claims": [
    "Three independent ThermoML data blocks report mass density for the binary system acetonitrile + N,N-dimethylformamide at 298.15 K, and all three show a monotonic increase in density from pure acetonitrile to pure DMF.",
    "Pure acetonitrile densities at 298.15 K are 776.8 kg/m³ (DOI 10.1016/j.jct.2006.01.015), 776.47 kg/m³ (DOI 10.1016/j.jct.2014.02.019), and 776.714 kg/m³ (DOI 10.1021/acs.jced.8b00176), showing close agreement across the three sources.",
    "Pure DMF densities at 298.15 K are 944.6 kg/m³ (DOI 10.1016/j.jct.2006.01.015), 944.65 kg/m³ (DOI 10.1016/j.jct.2014.02.019), and 943.934 kg/m³ (DOI 10.1021/acs.jced.8b00176), also showing close agreement.",
    "The three blocks report data at slightly different pressures (101.0 kPa for two blocks, 100.0 kPa for one) and use different composition variables (mole fraction of acetonitrile, mass fraction of DMF, or mole fraction of DMF).",
    "Some quoted pure-component values carry unresolved data-provenance flags (AMBIGUOUS_VALUE, MISATTRIBUTED_VALUE), so the cross-block attribution of specific endpoint numbers should be treated with caution."
  ],
  "status": "success",
  "summary": "Three ThermoML datasets report mass density (kg/m³) for the binary system acetonitrile + N,N-dimethylformamide (DMF) at 298.15 K. Block GLOBlit_2659/PROPblock_7 (DOI 10.1016/j.jct.2006.01.015) provides 17 points at 101.0 kPa as a function of acetonitrile mole fraction, ranging from 944.6 kg/m³ (pure DMF) to 776.8 kg/m³ (pure acetonitrile). Block GLOBlit_4124/PROPblock_5 (DOI 10.1016/j.jct.2014.02.019) provides 5 points at 101.0 kPa as a function of DMF mass fraction, from 776.47 kg/m³ (pure acetonitrile) to 944.65 kg/m³ (pure DMF). Block GLOBlit_7481/PROPblock_16 (DOI 10.1021/acs.jced.8b00176) provides 11 points at 100.0 kPa as a function of DMF mole fraction, from 776.714 kg/m³ (pure acetonitrile) to 943.934 kg/m³ (pure DMF). Density increases monotonically from pure acetonitrile to pure DMF across all three studies. Pure-component endpoint densities show excellent mutual agreement among the three independent sources.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_15",
      "registry_id": "acetonitrile",
      "name": "acetonitrile"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_18",
      "registry_id": "dimethylformamide",
      "name": "dimethylformamide"
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
      "lit_num_id": "GLOBlit_2659",
      "block_number": "PROPblock_7",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_18",
        "GLOBcomp_15"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density data for binary acetonitrile + N,N-dimethylformamide at 293.15–318.15 K; 17 points at 298.15 K.",
      "doi": "10.1016/j.jct.2006.01.015",
      "lit_id": "2006-nai--0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 102,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_15",
          "name": "acetonitrile",
          "formula": "C2H3N",
          "inchi_key": "WEVYAHXRMPXWCK-UHFFFAOYSA-N",
          "SMILES": "CC#N",
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
            "min": 293.15,
            "max": 318.15,
            "n_unique": 6
          },
          "range_min": 293.15,
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
            "min": 0.0,
            "max": 1.0,
            "n_unique": 17
          },
          "range_min": 0.0,
          "range_max": 1.0
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
          "meas_num_id": "GLOBmeas_153",
          "meas_ID": "pycnom_ufactor_4",
          "method_standard": null,
          "method_custom": "PYCNOM:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 755.7,
            "max": 949.1,
            "mean": 866.031373,
            "std": 50.670795,
            "n": 102
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 755.7,
          "range_max": 949.1
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
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_15",
          "name": "acetonitrile",
          "formula": "C2H3N",
          "inchi_key": "WEVYAHXRMPXWCK-UHFFFAOYSA-N",
          "SMILES": "CC#N",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "parent_n_datapoints": 102,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_4124",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_18",
        "GLOBcomp_15"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density data for binary acetonitrile + N,N-dimethylformamide at 298.15–313.15 K; 5 points at 298.15 K.",
      "doi": "10.1016/j.jct.2014.02.019",
      "lit_id": "2014-bra-pra-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 20,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_15",
          "name": "acetonitrile",
          "formula": "C2H3N",
          "inchi_key": "WEVYAHXRMPXWCK-UHFFFAOYSA-N",
          "SMILES": "CC#N",
          "sample_num": "DOIcompSample_2_1"
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
            "min": 0.0,
            "max": 1.0,
            "n_unique": 5
          },
          "range_min": 0.0,
          "range_max": 1.0
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
            "min": 759.55,
            "max": 944.65,
            "mean": 851.6195,
            "std": 61.609539,
            "n": 20
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 759.55,
          "range_max": 944.65
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
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_15",
          "name": "acetonitrile",
          "formula": "C2H3N",
          "inchi_key": "WEVYAHXRMPXWCK-UHFFFAOYSA-N",
          "SMILES": "CC#N",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 20,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_7481",
      "block_number": "PROPblock_16",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_18",
        "GLOBcomp_15"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density data for binary acetonitrile + N,N-dimethylformamide at 298.15–323.15 K; 11 points at 298.15 K.",
      "doi": "10.1021/acs.jced.8b00176",
      "lit_id": "2018-fat-riy-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 66,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_15",
          "name": "acetonitrile",
          "formula": "C2H3N",
          "inchi_key": "WEVYAHXRMPXWCK-UHFFFAOYSA-N",
          "SMILES": "CC#N",
          "sample_num": "DOIcompSample_2_1"
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
          "value": 100.0,
          "digits": 1,
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
            "max": 323.15,
            "n_unique": 6
          },
          "range_min": 298.15,
          "range_max": 323.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_3",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_3",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 11
          },
          "range_min": 0.0,
          "range_max": 1.0
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
            "min": 749.253,
            "max": 943.934,
            "mean": 859.997076,
            "std": 53.899195,
            "n": 66
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 749.253,
          "range_max": 943.934
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
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_15",
          "name": "acetonitrile",
          "formula": "C2H3N",
          "inchi_key": "WEVYAHXRMPXWCK-UHFFFAOYSA-N",
          "SMILES": "CC#N",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 66,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2006.01.015",
      "block_number": "PROPblock_7",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<acetonitrile>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "944.6"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.0654",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "937.5"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.1912",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "922.9"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.2586",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "914.5"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.3204",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "906.3"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.3851",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "897.4"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.4596",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "886.5"
        },
        {
          "BLKpoint_id": "BLKpoint_26",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.5125",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "878.4"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.5925",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "865.2"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.6402",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "856.9"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.6899",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "847.8"
        },
        {
          "BLKpoint_id": "BLKpoint_31",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.7736",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "831.1"
        },
        {
          "BLKpoint_id": "BLKpoint_32",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.8522",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "813.9"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.9359",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "793.8"
        },
        {
          "BLKpoint_id": "BLKpoint_34",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "776.8"
        }
      ],
      "inspection_id": "INSP_b3e3e45d8253",
      "lit_num_id": "GLOBlit_2659"
    },
    {
      "doi": "10.1016/j.jct.2014.02.019",
      "block_number": "PROPblock_5",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mass_fraction_<dimethylformamide>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "776.47"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "0.25",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "816.75"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "0.5",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "856.92"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "0.75",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "900.14"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "944.65"
        }
      ],
      "inspection_id": "INSP_ec6c2c72fb92",
      "lit_num_id": "GLOBlit_4124"
    },
    {
      "doi": "10.1021/acs.jced.8b00176",
      "block_number": "PROPblock_16",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<dimethylformamide>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "776.714"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.0989",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "802.565"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.1916",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "826.376"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.2925",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "844.614"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.3932",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "865.725"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.5029",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "880.889"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.6002",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "895.421"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.6931",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "907.546"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.7926",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "922.026"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.8996",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "932.676"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "943.934"
        }
      ],
      "inspection_id": "INSP_73f2dd990fc7",
      "lit_num_id": "GLOBlit_7481"
    }
  ]
}