{
  "answer": "## Binary Density Data: DMF + Water at 298.15 K\n\n**11 binary blocks** were found in ThermoML containing both N,N-dimethylformamide (DMF, GLOBcomp_18) and water (GLOBcomp_1) with mass density (GLOBprop_1) near 298.15 K.\n\n### Best Full-Range Dataset: GLOBlit_2834 / PROPblock_18\n\n**DOI:** 10.1016/j.jct.2007.05.015  \n**40 data points**, all at T = 298.15 K and p = 101.0 kPa, spanning x(DMF) = 0 to 1.  \n**Density range (n=40):** 943.94–997.02 kg/m³\n\nRepresentative inspected rows:\n\n| x(DMF) | ρ (kg/m³) |\n|--------|-----------|\n| 0 | 997.02 |\n| 0.01233 | 996.44 |\n| 0.0266 | 996.21 |\n| 0.04154 | 996.18 |\n| 0.11728 | 997.02 |\n| 0.14116 | 996.93 |\n| 0.23003 | 993.87 |\n| 0.28661 | 990.18 |\n| 0.31385 | 989.17 |\n| 0.37711 | 984.28 |\n| 0.92495 | 948.01 |\n| 0.96614 | 946.28 |\n| 1 | 943.94 |\n\nThe topology is **non-monotonic** (4 extrema), showing a density maximum near x(DMF) ≈ 0.12 where the mixture density equals or slightly exceeds that of pure water (~997 kg/m³), before decreasing toward pure DMF (943.94 kg/m³).\n\n### Additional Full-Range Dataset: GLOBlit_4174 / PROPblock_19\n\n**DOI:** 10.1016/j.jct.2014.05.013  \n**18 total points** across three temperatures (288.15, 298.15, 308.15 K) at p = 100.0 kPa, using mass fraction w(DMF) = 0 to 1.\n\nAt 298.15 K specifically (inspected rows):\n\n| w(DMF) | ρ (kg/m³) |\n|--------|-----------|\n| 0 | 997 |\n| 0.4 | 996.99 |\n| 0.6 | 992.97 |\n| 0.8 | 977.38 |\n| 1 | 943.89 |\n\nThis dataset has fewer composition points at 298.15 K but confirms the same trend.\n\n### Other Blocks Found (not individually inspected)\n\nThe search_blocks tool summary also returned blocks from the following sources, which may contain relevant 298.15 K data. Point counts below are per the search_blocks summary and have not been individually verified by block inspection:\n\n- **GLOBlit_11030** (10.1021/je700671t) — reported as the largest dataset (per search summary)\n- **GLOBlit_2584** (10.1016/j.jct.2005.07.012) — multi-temperature block\n- **GLOBlit_3614** (10.1016/j.jct.2012.04.007) — narrow water-dilute composition range\n- **GLOBlit_1540** (10.1016/j.fluid.2014.08.026) — partial composition range\n- **GLOBlit_4166** (10.1016/j.jct.2014.05.003) — partial composition range\n- Plus additional blocks (11 total found)\n\n### Recommendation\n\n**GLOBlit_2834 / PROPblock_18** is the best single block for full-range binary density of DMF + water at 298.15 K: 40 points spanning x(DMF) = 0–1, all at exactly 298.15 K and 101.0 kPa. The non-monotonic density behavior (density maximum near x(DMF) ≈ 0.12) reflects strong DMF–water hydrogen-bonding interactions that produce volume contraction in the water-rich region.",
  "core_claims": [
    "11 binary ThermoML blocks were found containing mass density data for DMF + water near 298.15 K.",
    "The best full-range dataset is GLOBlit_2834 / PROPblock_18 (DOI: 10.1016/j.jct.2007.05.015), comprising 40 data points at T = 298.15 K and p = 101.0 kPa, spanning x(DMF) = 0 to 1, with a density range of 943.94–997.02 kg/m³.",
    "The density–composition relationship is non-monotonic, exhibiting a density maximum near x(DMF) ≈ 0.12 where the mixture density equals or slightly exceeds that of pure water (~997 kg/m³), before decreasing toward pure DMF (943.94 kg/m³).",
    "The non-monotonic behavior is attributed to strong DMF–water hydrogen-bonding interactions producing volume contraction in the water-rich region.",
    "A second full-range dataset (GLOBlit_4174 / PROPblock_19, DOI: 10.1016/j.jct.2014.05.013) with fewer composition points at 298.15 K confirms the same overall trend."
  ],
  "status": "success",
  "summary": "Eleven ThermoML binary blocks contain mass density data for DMF (N,N-dimethylformamide) + water near 298.15 K. The recommended full-range dataset is GLOBlit_2834 / PROPblock_18 (DOI 10.1016/j.jct.2007.05.015), which provides 40 data points at T = 298.15 K and p = 101.0 kPa spanning x(DMF) = 0 to 1, with densities from 943.94 to 997.02 kg/m³. The density profile is non-monotonic with a maximum near x(DMF) ≈ 0.12 where the mixture density equals or slightly exceeds that of pure water (~997 kg/m³), before decreasing toward pure DMF (943.94 kg/m³). A second full-range dataset, GLOBlit_4174 / PROPblock_19 (DOI 10.1016/j.jct.2014.05.013), has fewer composition points at 298.15 K but confirms the same trend, with pure-DMF density of 943.89 kg/m³. Additional blocks from sources including GLOBlit_11030 (10.1021/je700671t), GLOBlit_2584 (10.1016/j.jct.2005.07.012), GLOBlit_3614 (10.1016/j.jct.2012.04.007), GLOBlit_1540 (10.1016/j.fluid.2014.08.026), and GLOBlit_4166 (10.1016/j.jct.2014.05.003) were also found but not individually inspected. The non-monotonic behavior reflects strong DMF–water hydrogen-bonding interactions producing volume contraction in the water-rich region.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2834",
      "block_number": "PROPblock_18",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_18",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of DMF + water at 298.15 K and 101.0 kPa; 40 data points spanning x(DMF) = 0–1, density range 943.94–997.02 kg/m³, non-monotonic with maximum near x(DMF) ≈ 0.12.",
      "doi": "10.1016/j.jct.2007.05.015",
      "lit_id": "2008-pap-aro-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 40,
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
          "org_num": "DOIcomp_7",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_7_1"
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
        },
        {
          "BLKconstr_id": "BLKconstr_2",
          "constr_num_id": "GLOBconstr_2",
          "constr_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "value": 298.15,
          "digits": 5,
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
            "BLKvar_id": "BLKvar_1",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 40
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
          "meas_num_id": "GLOBmeas_147",
          "meas_ID": "vibtub_ufactor_16",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:16",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 943.94,
            "max": 997.02,
            "mean": 975.8625,
            "std": 17.879394,
            "n": 40
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 943.94,
          "range_max": 997.02
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
          "org_num": "DOIcomp_7",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_7_1"
        }
      ],
      "parent_n_datapoints": 40,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_4174",
      "block_number": "PROPblock_19",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_18",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of DMF + water at multiple temperatures (288.15, 298.15, 308.15 K) and 100.0 kPa; 18 total points using mass fraction w(DMF) = 0–1.",
      "doi": "10.1016/j.jct.2014.05.013",
      "lit_id": "2014-zha-li-2",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 18,
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
            "min": 288.15,
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 288.15,
          "range_max": 308.15
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
            "n_unique": 6
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
            "min": 934.39,
            "max": 1003.56,
            "mean": 983.972222,
            "std": 20.650547,
            "n": 18
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 934.39,
          "range_max": 1003.56
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
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_5_1"
        }
      ],
      "parent_n_datapoints": 18,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2007.05.015",
      "block_number": "PROPblock_18",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<dimethylformamide>",
        "pressure_kpa",
        "temperature_k",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "997.02"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "mole_fraction_<dimethylformamide>": "0.01233",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "996.44"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "mole_fraction_<dimethylformamide>": "0.0266",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "996.21"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mole_fraction_<dimethylformamide>": "0.0276",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "996.23"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "mole_fraction_<dimethylformamide>": "0.04154",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "996.18"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mole_fraction_<dimethylformamide>": "0.11728",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "997.02"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "mole_fraction_<dimethylformamide>": "0.14116",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "996.93"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "mole_fraction_<dimethylformamide>": "0.23003",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "993.87"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "mole_fraction_<dimethylformamide>": "0.28661",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "990.18"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "mole_fraction_<dimethylformamide>": "0.31385",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "989.17"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "mole_fraction_<dimethylformamide>": "0.37711",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "984.28"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "mole_fraction_<dimethylformamide>": "0.92495",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "948.01"
        },
        {
          "BLKpoint_id": "BLKpoint_39",
          "mole_fraction_<dimethylformamide>": "0.96614",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "946.28"
        },
        {
          "BLKpoint_id": "BLKpoint_40",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "943.94"
        }
      ],
      "inspection_id": "INSP_440a0c0a80b2",
      "lit_num_id": "GLOBlit_2834"
    },
    {
      "doi": "10.1016/j.jct.2014.05.013",
      "block_number": "PROPblock_19",
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
          "temperature_k": "288.15",
          "mass_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "999"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "288.15",
          "mass_fraction_<dimethylformamide>": "0.4",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1003.56"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "288.15",
          "mass_fraction_<dimethylformamide>": "0.6",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1001.34"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "288.15",
          "mass_fraction_<dimethylformamide>": "0.8",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "986.63"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "288.15",
          "mass_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "953.53"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "997"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "0.4",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "996.99"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "0.6",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "992.97"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "0.8",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "977.38"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "943.89"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "308.15",
          "mass_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "994.03"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "308.15",
          "mass_fraction_<dimethylformamide>": "0.4",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "990"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "308.15",
          "mass_fraction_<dimethylformamide>": "0.6",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "984.33"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "308.15",
          "mass_fraction_<dimethylformamide>": "0.8",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "968.07"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "308.15",
          "mass_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "934.39"
        }
      ],
      "inspection_id": "INSP_3831ba56c42d",
      "lit_num_id": "GLOBlit_4174"
    }
  ]
}