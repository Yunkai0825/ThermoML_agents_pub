{
  "answer": "**Excess molar volume (VE) data for the binary system acetonitrile + N,N-dimethylformamide (DMF) at 298.15 K — ThermoML database search results:**\n\nNo excess molar volume (GLOBprop_28) data were found in the ThermoML database for the binary system acetonitrile (GLOBcomp_15) + N,N-dimethylformamide (GLOBcomp_18). The search was conducted with and without temperature constraints, and no blocks exist for this specific property–compound combination.\n\n**Available related data for this binary system:**\n\nThe database does contain density, viscosity, and speed of sound data for the acetonitrile + DMF binary, from which excess molar volume could in principle be derived. The relevant blocks are:\n\n| DOI | Literature ID | Block | Property | Data points | T range (K) | Composition variable | P (kPa) |\n|-----|---------------|-------|----------|-------------|-------------|----------------------|---------|\n| 10.1016/j.jct.2006.01.015 | GLOBlit_2659 | PROPblock_7 | Mass density (GLOBprop_1) | 102 | 293.15–318.15 | x(acetonitrile) 0–1 | 101.0 |\n| 10.1016/j.jct.2014.02.019 | GLOBlit_4124 | PROPblock_5 | Mass density (GLOBprop_1) | 20 | 298.15–313.15 | w(DMF) 0–1 | 101.0 |\n| 10.1021/acs.jced.8b00176 | GLOBlit_7481 | PROPblock_16 | Mass density (GLOBprop_1) | 66 | 298.15–323.15 | x(DMF) 0–1 | 100.0 |\n| 10.1021/acs.jced.8b00176 | GLOBlit_7481 | PROPblock_17 | Speed of sound (GLOBprop_8) | 66 | 298.15–323.15 | x(DMF) 0–1 | 100.0 |\n| 10.1016/j.jct.2014.02.019 | GLOBlit_4124 | PROPblock_6 | Viscosity (GLOBprop_4) | Not inspected in this run | Not inspected in this run | w(DMF) | Not inspected in this run |\n| 10.1021/acs.jced.8b00176 | GLOBlit_7481 | PROPblock_18 | Viscosity (GLOBprop_4) | Not inspected in this run | Not inspected in this run | x(DMF) | Not inspected in this run |\n\n**Chemistry note:** While excess molar volume is not directly reported in the database for this system, the three density datasets (PROPblock_7, PROPblock_5, PROPblock_16) cover 298.15 K across the full composition range and could be used to calculate VE. For example, at 298.15 K from PROPblock_7 (GLOBlit_2659), the density of pure DMF is 944.6 kg/m³ and pure acetonitrile is 776.8 kg/m³, with intermediate compositions such as x(acetonitrile) = 0.5925 giving 865.2 kg/m³. Similarly, PROPblock_16 (GLOBlit_7481) reports densities at 298.15 K ranging from 776.714 kg/m³ (pure acetonitrile) to 943.934 kg/m³ (pure DMF).\n\n**Compound IDs:** acetonitrile = GLOBcomp_15, DMF = GLOBcomp_18\n**Property ID (not found in database):** Excess molar volume = GLOBprop_28",
  "core_claims": [
    "No excess molar volume (VE) data were found in the ThermoML database for the binary system acetonitrile + N,N-dimethylformamide at 298.15 K or any other temperature.",
    "The ThermoML database does contain mass density data for the acetonitrile + DMF binary system at 298.15 K across the full composition range from three independent sources (DOIs 10.1016/j.jct.2006.01.015, 10.1016/j.jct.2014.02.019, and 10.1021/acs.jced.8b00176), from which excess molar volume could in principle be calculated.",
    "Representative pure-component densities at 298.15 K from the available data include 776.8 kg/m³ (acetonitrile) and 944.6 kg/m³ (DMF) from one source, and 776.714 kg/m³ (acetonitrile) and 943.934 kg/m³ (DMF) from another."
  ],
  "status": "no_results",
  "summary": "No excess molar volume (VE, GLOBprop_28) data were found in the ThermoML database for the binary system acetonitrile (GLOBcomp_15) + N,N-dimethylformamide (GLOBcomp_18) at 298.15 K. However, mass density (GLOBprop_1) data covering the full composition range at 298.15 K are available from three sources (DOIs 10.1016/j.jct.2006.01.015, 10.1016/j.jct.2014.02.019, 10.1021/acs.jced.8b00176), from which VE could in principle be calculated. Representative density values at 298.15 K include 776.8 kg/m³ (pure acetonitrile) and 944.6 kg/m³ (pure DMF) from GLOBlit_2659 PROPblock_7, and 776.714 kg/m³ (pure acetonitrile) to 943.934 kg/m³ (pure DMF) from GLOBlit_7481 PROPblock_16. Speed of sound and viscosity data for this binary system are also present in the database.",
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
      "core_GLOB_id": "GLOBprop_28",
      "registry_id": "excess_molar_volume_m3_mol",
      "name": "Excess molar volume, m3/mol"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_1",
      "registry_id": "mass_density_kg_m3",
      "name": "Mass density, kg/m3"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_8",
      "registry_id": "speed_of_sound_m_s",
      "name": "Speed of sound, m/s"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_4",
      "registry_id": "viscosity_pa_s",
      "name": "Viscosity, Pa*s"
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
      "description": "Mass density for binary acetonitrile + DMF, 293.15–318.15 K, 101.0 kPa.",
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
      "description": "Mass density for binary acetonitrile + DMF, 298.15–313.15 K, 101.0 kPa.",
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
      "description": "Mass density for binary acetonitrile + DMF, 298.15–323.15 K, 100.0 kPa.",
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
    },
    {
      "lit_num_id": "GLOBlit_7481",
      "block_number": "PROPblock_17",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_18",
        "GLOBcomp_15"
      ],
      "prop_num_ids": [
        "GLOBprop_8"
      ],
      "description": "Speed of sound for binary acetonitrile + DMF, 298.15–323.15 K, 100.0 kPa.",
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
        },
        {
          "BLKconstr_id": "BLKconstr_2",
          "constr_num_id": "GLOBconstr_4",
          "constr_id": "frequency_mhz",
          "name": "Frequency, MHz",
          "type": "eMiscellaneous",
          "value": 3.0,
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
          "prop_num_id": "GLOBprop_8",
          "prop_ID": "speed_of_sound_m_s",
          "name": "Speed of sound, m/s",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_18",
          "meas_ID": "single_path_length_method",
          "method_standard": "Single path-length method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Speed of sound, m/s",
            "min": 1177.76,
            "max": 1457.14,
            "mean": 1325.574091,
            "std": 66.425949,
            "n": 66
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1177.76,
          "range_max": 1457.14
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
        },
        {
          "owner_id": "BLKconstr_2",
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
    },
    {
      "lit_num_id": "GLOBlit_4124",
      "block_number": "PROPblock_6",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_18",
        "GLOBcomp_15"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity for binary acetonitrile + DMF.",
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
          "prop_num_id": "GLOBprop_4",
          "prop_ID": "viscosity_pa_s",
          "name": "Viscosity, Pa*s",
          "group": "TransportProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_4",
          "meas_ID": "capillary_tube_ostwald_ubbelohde_method",
          "method_standard": "Capillary tube (Ostwald; Ubbelohde) method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000293,
            "max": 0.000799,
            "mean": 0.000492,
            "std": 0.000163,
            "n": 20
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000293,
          "range_max": 0.000799
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
      "block_number": "PROPblock_18",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_18",
        "GLOBcomp_15"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity for binary acetonitrile + DMF.",
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
          "prop_num_id": "GLOBprop_4",
          "prop_ID": "viscosity_pa_s",
          "name": "Viscosity, Pa*s",
          "group": "TransportProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_8",
          "meas_ID": "falling_or_rolling_sphere_viscometry",
          "method_standard": "Falling or rolling sphere viscometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.00028,
            "max": 0.00081,
            "mean": 0.00052,
            "std": 0.000141,
            "n": 66
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.00028,
          "range_max": 0.00081
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
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "293.15",
          "mole_fraction_<acetonitrile>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "949.1"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "293.15",
          "mole_fraction_<acetonitrile>": "0.3204",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "910.9"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "293.15",
          "mole_fraction_<acetonitrile>": "0.5925",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "870"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "293.15",
          "mole_fraction_<acetonitrile>": "0.7736",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "836.1"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "293.15",
          "mole_fraction_<acetonitrile>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "782.1"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "944.6"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.3204",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "906.3"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.5925",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "865.2"
        },
        {
          "BLKpoint_id": "BLKpoint_31",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.7736",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "831.1"
        },
        {
          "BLKpoint_id": "BLKpoint_34",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "776.8"
        },
        {
          "BLKpoint_id": "BLKpoint_35",
          "temperature_k": "303.15",
          "mole_fraction_<acetonitrile>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "940.1"
        },
        {
          "BLKpoint_id": "BLKpoint_40",
          "temperature_k": "303.15",
          "mole_fraction_<acetonitrile>": "0.3204",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "901.7"
        },
        {
          "BLKpoint_id": "BLKpoint_44",
          "temperature_k": "303.15",
          "mole_fraction_<acetonitrile>": "0.5925",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "860.4"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "303.15",
          "mole_fraction_<acetonitrile>": "0.7736",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "826.1"
        },
        {
          "BLKpoint_id": "BLKpoint_51",
          "temperature_k": "303.15",
          "mole_fraction_<acetonitrile>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "771.5"
        },
        {
          "BLKpoint_id": "BLKpoint_52",
          "temperature_k": "308.15",
          "mole_fraction_<acetonitrile>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "935.7"
        },
        {
          "BLKpoint_id": "BLKpoint_57",
          "temperature_k": "308.15",
          "mole_fraction_<acetonitrile>": "0.3204",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "897.2"
        },
        {
          "BLKpoint_id": "BLKpoint_61",
          "temperature_k": "308.15",
          "mole_fraction_<acetonitrile>": "0.5925",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "855.7"
        },
        {
          "BLKpoint_id": "BLKpoint_65",
          "temperature_k": "308.15",
          "mole_fraction_<acetonitrile>": "0.7736",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "821.2"
        },
        {
          "BLKpoint_id": "BLKpoint_68",
          "temperature_k": "308.15",
          "mole_fraction_<acetonitrile>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "766.3"
        },
        {
          "BLKpoint_id": "BLKpoint_69",
          "temperature_k": "313.15",
          "mole_fraction_<acetonitrile>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "931.2"
        },
        {
          "BLKpoint_id": "BLKpoint_74",
          "temperature_k": "313.15",
          "mole_fraction_<acetonitrile>": "0.3204",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "892.6"
        },
        {
          "BLKpoint_id": "BLKpoint_78",
          "temperature_k": "313.15",
          "mole_fraction_<acetonitrile>": "0.5925",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "850.9"
        },
        {
          "BLKpoint_id": "BLKpoint_82",
          "temperature_k": "313.15",
          "mole_fraction_<acetonitrile>": "0.7736",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "816.3"
        },
        {
          "BLKpoint_id": "BLKpoint_85",
          "temperature_k": "313.15",
          "mole_fraction_<acetonitrile>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "761"
        },
        {
          "BLKpoint_id": "BLKpoint_86",
          "temperature_k": "318.15",
          "mole_fraction_<acetonitrile>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "926.7"
        },
        {
          "BLKpoint_id": "BLKpoint_91",
          "temperature_k": "318.15",
          "mole_fraction_<acetonitrile>": "0.3204",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "888.1"
        },
        {
          "BLKpoint_id": "BLKpoint_95",
          "temperature_k": "318.15",
          "mole_fraction_<acetonitrile>": "0.5925",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "846.1"
        },
        {
          "BLKpoint_id": "BLKpoint_99",
          "temperature_k": "318.15",
          "mole_fraction_<acetonitrile>": "0.7736",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "811.4"
        },
        {
          "BLKpoint_id": "BLKpoint_102",
          "temperature_k": "318.15",
          "mole_fraction_<acetonitrile>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "755.7"
        }
      ],
      "inspection_id": "INSP_463f022500be",
      "lit_num_id": "GLOBlit_2659"
    },
    {
      "doi": "10.1016/j.jct.2014.02.019",
      "block_number": "PROPblock_5",
      "table_mode": "rdp",
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
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "303.15",
          "mass_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "771.56"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "308.15",
          "mass_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "765.26"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "313.15",
          "mass_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "759.55"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "0.5",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "856.92"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "303.15",
          "mass_fraction_<dimethylformamide>": "0.5",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "852.67"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "308.15",
          "mass_fraction_<dimethylformamide>": "0.5",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "847.38"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "313.15",
          "mass_fraction_<dimethylformamide>": "0.5",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "842.57"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "944.65"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "303.15",
          "mass_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "940.05"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "308.15",
          "mass_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "935.71"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "temperature_k": "313.15",
          "mass_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "929.91"
        }
      ],
      "inspection_id": "INSP_326b6a5ebd99",
      "lit_num_id": "GLOBlit_4124"
    },
    {
      "doi": "10.1021/acs.jced.8b00176",
      "block_number": "PROPblock_16",
      "table_mode": "rdp",
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
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.1916",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "826.376"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.3932",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "865.725"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.7926",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "922.026"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "943.934"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "303.15",
          "mole_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "771.289"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "303.15",
          "mole_fraction_<dimethylformamide>": "0.1916",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "821.229"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "303.15",
          "mole_fraction_<dimethylformamide>": "0.3932",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "860.639"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "temperature_k": "303.15",
          "mole_fraction_<dimethylformamide>": "0.7926",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "917.22"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "303.15",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "939.162"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "308.15",
          "mole_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "765.833"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "308.15",
          "mole_fraction_<dimethylformamide>": "0.1916",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "816.008"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "temperature_k": "308.15",
          "mole_fraction_<dimethylformamide>": "0.3932",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "855.56"
        },
        {
          "BLKpoint_id": "BLKpoint_31",
          "temperature_k": "308.15",
          "mole_fraction_<dimethylformamide>": "0.7926",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "912.402"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "temperature_k": "308.15",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "934.373"
        },
        {
          "BLKpoint_id": "BLKpoint_34",
          "temperature_k": "313.15",
          "mole_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "760.339"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "temperature_k": "313.15",
          "mole_fraction_<dimethylformamide>": "0.1916",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "810.757"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "temperature_k": "313.15",
          "mole_fraction_<dimethylformamide>": "0.3932",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "850.487"
        },
        {
          "BLKpoint_id": "BLKpoint_42",
          "temperature_k": "313.15",
          "mole_fraction_<dimethylformamide>": "0.7926",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "907.663"
        },
        {
          "BLKpoint_id": "BLKpoint_44",
          "temperature_k": "313.15",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "929.577"
        },
        {
          "BLKpoint_id": "BLKpoint_45",
          "temperature_k": "318.15",
          "mole_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "754.815"
        },
        {
          "BLKpoint_id": "BLKpoint_47",
          "temperature_k": "318.15",
          "mole_fraction_<dimethylformamide>": "0.1916",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "805.527"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "temperature_k": "318.15",
          "mole_fraction_<dimethylformamide>": "0.3932",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "845.354"
        },
        {
          "BLKpoint_id": "BLKpoint_53",
          "temperature_k": "318.15",
          "mole_fraction_<dimethylformamide>": "0.7926",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "902.79"
        },
        {
          "BLKpoint_id": "BLKpoint_55",
          "temperature_k": "318.15",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "924.765"
        },
        {
          "BLKpoint_id": "BLKpoint_56",
          "temperature_k": "323.15",
          "mole_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "749.253"
        },
        {
          "BLKpoint_id": "BLKpoint_58",
          "temperature_k": "323.15",
          "mole_fraction_<dimethylformamide>": "0.1916",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "800.222"
        },
        {
          "BLKpoint_id": "BLKpoint_60",
          "temperature_k": "323.15",
          "mole_fraction_<dimethylformamide>": "0.3932",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "840.213"
        },
        {
          "BLKpoint_id": "BLKpoint_64",
          "temperature_k": "323.15",
          "mole_fraction_<dimethylformamide>": "0.7926",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "897.991"
        },
        {
          "BLKpoint_id": "BLKpoint_66",
          "temperature_k": "323.15",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "919.95"
        }
      ],
      "inspection_id": "INSP_b4e09825f8b6",
      "lit_num_id": "GLOBlit_7481"
    },
    {
      "doi": "10.1021/acs.jced.8b00176",
      "block_number": "PROPblock_17",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<dimethylformamide>",
        "pressure_kpa",
        "frequency_mhz",
        "speed_of_sound_m_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1278.53"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.3932",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1361.63"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1457.14"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "303.15",
          "mole_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1258.37"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "303.15",
          "mole_fraction_<dimethylformamide>": "0.3932",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1342.15"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "303.15",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1437.81"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "308.15",
          "mole_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1238.17"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "temperature_k": "308.15",
          "mole_fraction_<dimethylformamide>": "0.3932",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1322.61"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "temperature_k": "308.15",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1418.45"
        },
        {
          "BLKpoint_id": "BLKpoint_34",
          "temperature_k": "313.15",
          "mole_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1218.03"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "temperature_k": "313.15",
          "mole_fraction_<dimethylformamide>": "0.3932",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1303.15"
        },
        {
          "BLKpoint_id": "BLKpoint_44",
          "temperature_k": "313.15",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1399.15"
        },
        {
          "BLKpoint_id": "BLKpoint_45",
          "temperature_k": "318.15",
          "mole_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1197.87"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "temperature_k": "318.15",
          "mole_fraction_<dimethylformamide>": "0.3932",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1283.73"
        },
        {
          "BLKpoint_id": "BLKpoint_55",
          "temperature_k": "318.15",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1379.92"
        },
        {
          "BLKpoint_id": "BLKpoint_56",
          "temperature_k": "323.15",
          "mole_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1177.76"
        },
        {
          "BLKpoint_id": "BLKpoint_60",
          "temperature_k": "323.15",
          "mole_fraction_<dimethylformamide>": "0.3932",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1264.36"
        },
        {
          "BLKpoint_id": "BLKpoint_66",
          "temperature_k": "323.15",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1360.74"
        }
      ],
      "inspection_id": "INSP_7e180277aa32",
      "lit_num_id": "GLOBlit_7481"
    }
  ]
}