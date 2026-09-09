{
  "answer": "## Speed of Sound Data for Binary Ethanol + Water Mixtures near 298.15 K\n\nFour data blocks were found in the ThermoML database containing speed of sound measurements for binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) mixtures at or near 298.15 K. Three were fully inspected:\n\n### 1. PROPblock_20 — GLOBlit_5201 (DOI: 10.1016/j.jct.2018.02.022)\n- **Data points:** 152\n- **Composition variable:** Mole fraction of ethanol, range 0–1 (full binary range including pure endpoints)\n- **Temperature range:** 293.15–308.15 K\n- **Pressure:** 92.3 kPa (fixed constraint)\n- **Speed of sound range:** 1109.59–1625.74 m/s\n\nThis is the most comprehensive dataset, spanning the entire composition range at four temperatures. At 298.15 K, representative inspected values include:\n- x(ethanol) = 0: 1496.99 m/s (pure water)\n- x(ethanol) = 0.0997: 1618.97 m/s\n- x(ethanol) = 0.1497: 1600.11 m/s\n- x(ethanol) = 0.3507: 1426.17 m/s\n- x(ethanol) = 0.5002: 1337.91 m/s\n- x(ethanol) = 1: 1143.50 m/s (pure ethanol)\n\nThe data show the well-known speed-of-sound maximum in the water-rich region (near x ≈ 0.1) before decreasing through the ethanol-rich side.\n\n### 2. PROPblock_8 — GLOBlit_4415 (DOI: 10.1016/j.jct.2015.06.024)\n- **Data points:** 40\n- **Composition variable:** Molality of ethanol (solvent: water), range 0.02159–0.21882 mol/kg\n- **Temperature range:** 288.15–308.15 K\n- **Pressure:** 84.5 kPa (fixed constraint)\n- **Speed of sound range:** 1467.43–1525.49 m/s\n\nThis dataset covers only the dilute ethanol regime but spans a broader temperature window. At 298.15 K, inspected values include:\n- m = 0.02159 mol/kg: 1497.50 m/s\n- m = 0.08646 mol/kg: 1499.71 m/s\n- m = 0.21882 mol/kg: 1503.85 m/s\n\n### 3. PROPblock_19 — GLOBlit_8888 (DOI: 10.1021/je0601098)\n- **Data points:** 12\n- **Composition variable:** Molality of water (in ethanol as solvent), range 0–1.01891 mol/kg\n- **Temperature:** 298.15 K (fixed constraint, exactly at target temperature)\n- **Pressure:** 101.0 kPa (fixed constraint)\n- **Speed of sound range:** 1142.1–1160.1 m/s\n\nThis dataset is isothermal at exactly 298.15 K and covers the ethanol-rich side of the binary. Speed of sound increases monotonically with water molality, from 1142.1 m/s (pure ethanol) to 1160.1 m/s at 1.01891 mol/kg water.\n\nA fourth block was also identified in the initial search but was not fully inspected.\n\n### Summary\n\nFor full-composition-range coverage at near-298.15 K, **PROPblock_20 (GLOBlit_5201)** is the most suitable dataset with 152 points spanning x(ethanol) = 0 to 1. For isothermal data at exactly 298.15 K on the ethanol-rich side, **PROPblock_19 (GLOBlit_8888)** provides 12 points. For dilute aqueous ethanol with temperature dependence, **PROPblock_8 (GLOBlit_4415)** offers 40 points across 288.15–308.15 K.",
  "core_claims": [
    "Four ThermoML data blocks were identified containing speed of sound measurements for binary ethanol + water mixtures at or near 298.15 K; three were fully inspected.",
    "PROPblock_20 (GLOBlit_5201, DOI: 10.1016/j.jct.2018.02.022) is the most comprehensive dataset, with 152 data points spanning the full ethanol mole fraction range (0–1) at 293.15–308.15 K and 92.3 kPa, with speed of sound values ranging from 1109.59 to 1625.74 m/s.",
    "At 298.15 K in PROPblock_20, the data show the well-known speed-of-sound maximum in the water-rich region (near x(ethanol) ≈ 0.1), with representative values including 1496.99 m/s at x = 0 (pure water), 1618.97 m/s at x = 0.0997, and 1143.50 m/s at x = 1 (pure ethanol).",
    "PROPblock_8 (GLOBlit_4415, DOI: 10.1016/j.jct.2015.06.024) provides 40 data points covering only the dilute ethanol regime (molality 0.02159–0.21882 mol/kg) at 288.15–308.15 K and 84.5 kPa, with speed of sound values from 1467.43 to 1525.49 m/s.",
    "PROPblock_19 (GLOBlit_8888, DOI: 10.1021/je0601098) provides 12 isothermal data points at exactly 298.15 K and 101.0 kPa on the ethanol-rich side (water molality 0–1.01891 mol/kg in ethanol as solvent), with speed of sound increasing monotonically from 1142.1 m/s (pure ethanol) to 1160.1 m/s."
  ],
  "status": "success",
  "summary": "Speed of sound data for binary ethanol + water mixtures near 298.15 K were found in three fully inspected ThermoML data blocks. PROPblock_20 (GLOBlit_5201, DOI: 10.1016/j.jct.2018.02.022) is the most comprehensive, with 152 data points spanning the full mole-fraction range (x(ethanol) = 0–1) at 293.15–308.15 K and 92.3 kPa, with speed of sound ranging from 1109.59 to 1625.74 m/s; at 298.15 K representative values include 1496.99 m/s (pure water), 1618.97 m/s (x = 0.0997), and 1143.50 m/s (pure ethanol), showing the well-known maximum near x ≈ 0.1. PROPblock_8 (GLOBlit_4415, DOI: 10.1016/j.jct.2015.06.024) provides 40 points in the dilute ethanol regime (molality 0.02159–0.21882 mol/kg) at 288.15–308.15 K and 84.5 kPa, with speed of sound 1467.43–1525.49 m/s. PROPblock_19 (GLOBlit_8888, DOI: 10.1021/je0601098) gives 12 isothermal points at exactly 298.15 K and 101.0 kPa on the ethanol-rich side (water molality 0–1.01891 mol/kg in ethanol), with speed of sound 1142.1–1160.1 m/s increasing monotonically with water content. A fourth block was identified but not fully inspected.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_20",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_8"
      ],
      "description": "Speed of sound for ethanol + water over full composition range (x=0–1) at 293.15–308.15 K, 152 data points.",
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_id": "2018-hog-tor-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 152,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_6_1"
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
          "value": 92.3,
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
            "min": 293.15,
            "max": 308.15,
            "n_unique": 4
          },
          "range_min": 293.15,
          "range_max": 308.15
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
            "n_unique": 38
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
            "min": 1109.59,
            "max": 1625.74,
            "mean": 1365.460658,
            "std": 183.096958,
            "n": 152
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1109.59,
          "range_max": 1625.74
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_6_1"
        }
      ],
      "parent_n_datapoints": 152,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_4415",
      "block_number": "PROPblock_8",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_8"
      ],
      "description": "Speed of sound for dilute ethanol in water (molality 0.02159–0.21882 mol/kg) at 288.15–308.15 K, 40 data points.",
      "doi": "10.1016/j.jct.2015.06.024",
      "lit_id": "2015-ebr-sad-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 40,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_4_1"
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
      "solvents": [
        {
          "component_org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_1",
          "solvent_num_id": "GLOBsolvent_1",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N"
        }
      ],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_1",
          "constr_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "value": 84.5,
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
            "min": 288.15,
            "max": 308.15,
            "n_unique": 5
          },
          "range_min": 288.15,
          "range_max": 308.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_4",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_4",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Molality, mol/kg",
            "min": 0.02159,
            "max": 0.21882,
            "n_unique": 8
          },
          "range_min": 0.02159,
          "range_max": 0.21882
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
          "meas_num_id": "GLOBmeas_7",
          "meas_ID": "sing_around_technique_in_a_fixed_path_interferometer",
          "method_standard": "Sing-around technique in a fixed-path interferometer",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Speed of sound, m/s",
            "min": 1467.43,
            "max": 1525.49,
            "mean": 1498.46825,
            "std": 18.743376,
            "n": 40
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1467.43,
          "range_max": 1525.49
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_4_1"
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
      "parent_n_datapoints": 40,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8888",
      "block_number": "PROPblock_19",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_8"
      ],
      "description": "Speed of sound for water in ethanol (molality 0–1.01891 mol/kg) at exactly 298.15 K, 12 data points.",
      "doi": "10.1021/je0601098",
      "lit_id": "2006-kus-kol-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 12,
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
          "org_num": "DOIcomp_9",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_9_1"
        }
      ],
      "solvents": [
        {
          "component_org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "solvent_num_id": "GLOBsolvent_2",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N"
        }
      ],
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
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_9",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_9",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Molality, mol/kg",
            "min": 0.0,
            "max": 1.01891,
            "n_unique": 12
          },
          "range_min": 0.0,
          "range_max": 1.01891
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
          "meas_num_id": "GLOBmeas_15",
          "meas_ID": "linear_variable_path_acoustic_interferometer",
          "method_standard": "Linear variable-path acoustic interferometer",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Speed of sound, m/s",
            "min": 1142.1,
            "max": 1160.1,
            "mean": 1151.725,
            "std": 6.117505,
            "n": 12
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1142.1,
          "range_max": 1160.1
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
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_9",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_9_1"
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
      "doi": "10.1016/j.jct.2015.06.024",
      "block_number": "PROPblock_8",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "molality_mol_kg_<ethanol>",
        "pressure_kpa",
        "frequency_mhz",
        "speed_of_sound_m_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "288.15",
          "molality_mol_kg_<ethanol>": "0.02159",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1467.43"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "288.15",
          "molality_mol_kg_<ethanol>": "0.1749",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1473.44"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "288.15",
          "molality_mol_kg_<ethanol>": "0.21882",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1475.05"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "293.15",
          "molality_mol_kg_<ethanol>": "0.02159",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1483.38"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "293.15",
          "molality_mol_kg_<ethanol>": "0.08646",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1485.8"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "293.15",
          "molality_mol_kg_<ethanol>": "0.21882",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1490.38"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "298.15",
          "molality_mol_kg_<ethanol>": "0.02159",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1497.5"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "temperature_k": "298.15",
          "molality_mol_kg_<ethanol>": "0.08646",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1499.71"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "298.15",
          "molality_mol_kg_<ethanol>": "0.21882",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1503.85"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "303.15",
          "molality_mol_kg_<ethanol>": "0.02159",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1509.79"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "temperature_k": "303.15",
          "molality_mol_kg_<ethanol>": "0.08646",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1511.74"
        },
        {
          "BLKpoint_id": "BLKpoint_32",
          "temperature_k": "303.15",
          "molality_mol_kg_<ethanol>": "0.21882",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1515.48"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "temperature_k": "308.15",
          "molality_mol_kg_<ethanol>": "0.02159",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1520.37"
        },
        {
          "BLKpoint_id": "BLKpoint_37",
          "temperature_k": "308.15",
          "molality_mol_kg_<ethanol>": "0.10866",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1522.75"
        },
        {
          "BLKpoint_id": "BLKpoint_40",
          "temperature_k": "308.15",
          "molality_mol_kg_<ethanol>": "0.21882",
          "pressure_kpa": "84.5",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1525.49"
        }
      ],
      "inspection_id": "INSP_5b61ccac8a5c",
      "lit_num_id": "GLOBlit_4415"
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "block_number": "PROPblock_20",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<ethanol>",
        "pressure_kpa",
        "frequency_mhz",
        "speed_of_sound_m_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "0.0024",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1487.73"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "0.0707",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1604.25"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "0.0997",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1625.74"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "0.1294",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1623.76"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "0.2998",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1478.23"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "0.4514",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1379.03"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "0.6503",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1288.48"
        },
        {
          "BLKpoint_id": "BLKpoint_46",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.0997",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1618.97"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.1497",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1600.11"
        },
        {
          "BLKpoint_id": "BLKpoint_52",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.3507",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1426.17"
        },
        {
          "BLKpoint_id": "BLKpoint_55",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.5002",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1337.91"
        },
        {
          "BLKpoint_id": "BLKpoint_81",
          "temperature_k": "303.15",
          "mole_fraction_<ethanol>": "0.0904",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1610.77"
        },
        {
          "BLKpoint_id": "BLKpoint_83",
          "temperature_k": "303.15",
          "mole_fraction_<ethanol>": "0.1294",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1602.74"
        },
        {
          "BLKpoint_id": "BLKpoint_88",
          "temperature_k": "303.15",
          "mole_fraction_<ethanol>": "0.3507",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1411.8"
        },
        {
          "BLKpoint_id": "BLKpoint_91",
          "temperature_k": "303.15",
          "mole_fraction_<ethanol>": "0.5002",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1322.3"
        },
        {
          "BLKpoint_id": "BLKpoint_116",
          "temperature_k": "308.15",
          "mole_fraction_<ethanol>": "0.0801",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1602.67"
        },
        {
          "BLKpoint_id": "BLKpoint_119",
          "temperature_k": "308.15",
          "mole_fraction_<ethanol>": "0.1294",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1592.26"
        },
        {
          "BLKpoint_id": "BLKpoint_124",
          "temperature_k": "308.15",
          "mole_fraction_<ethanol>": "0.3507",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1397.33"
        },
        {
          "BLKpoint_id": "BLKpoint_127",
          "temperature_k": "308.15",
          "mole_fraction_<ethanol>": "0.5002",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1306.71"
        },
        {
          "BLKpoint_id": "BLKpoint_145",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "0",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1482.78"
        },
        {
          "BLKpoint_id": "BLKpoint_146",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1496.99"
        },
        {
          "BLKpoint_id": "BLKpoint_147",
          "temperature_k": "303.15",
          "mole_fraction_<ethanol>": "0",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1509.32"
        },
        {
          "BLKpoint_id": "BLKpoint_148",
          "temperature_k": "308.15",
          "mole_fraction_<ethanol>": "0",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1519.89"
        },
        {
          "BLKpoint_id": "BLKpoint_149",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "1",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1160.65"
        },
        {
          "BLKpoint_id": "BLKpoint_150",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "1",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1143.5"
        },
        {
          "BLKpoint_id": "BLKpoint_151",
          "temperature_k": "303.15",
          "mole_fraction_<ethanol>": "1",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1126.44"
        },
        {
          "BLKpoint_id": "BLKpoint_152",
          "temperature_k": "308.15",
          "mole_fraction_<ethanol>": "1",
          "pressure_kpa": "92.3",
          "frequency_mhz": "3.0",
          "speed_of_sound_m_s": "1109.59"
        }
      ],
      "inspection_id": "INSP_d2c2205c2128",
      "lit_num_id": "GLOBlit_5201"
    },
    {
      "doi": "10.1021/je0601098",
      "block_number": "PROPblock_19",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "molality_mol_kg_<water>",
        "pressure_kpa",
        "temperature_k",
        "speed_of_sound_m_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "molality_mol_kg_<water>": "0",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "speed_of_sound_m_s": "1142.1"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "molality_mol_kg_<water>": "0.21398",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "speed_of_sound_m_s": "1144.6"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "molality_mol_kg_<water>": "0.2705",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "speed_of_sound_m_s": "1145.9"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "molality_mol_kg_<water>": "0.31985",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "speed_of_sound_m_s": "1146.8"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "molality_mol_kg_<water>": "0.36588",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "speed_of_sound_m_s": "1148.6"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "molality_mol_kg_<water>": "0.45432",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "speed_of_sound_m_s": "1151"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "molality_mol_kg_<water>": "0.55413",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "speed_of_sound_m_s": "1153.2"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "molality_mol_kg_<water>": "0.64373",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "speed_of_sound_m_s": "1154.8"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "molality_mol_kg_<water>": "0.743",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "speed_of_sound_m_s": "1156.4"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "molality_mol_kg_<water>": "0.83492",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "speed_of_sound_m_s": "1157.7"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "molality_mol_kg_<water>": "0.92645",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "speed_of_sound_m_s": "1159.5"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "molality_mol_kg_<water>": "1.01891",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "speed_of_sound_m_s": "1160.1"
        }
      ],
      "inspection_id": "INSP_c50181997cc0",
      "lit_num_id": "GLOBlit_8888"
    }
  ]
}