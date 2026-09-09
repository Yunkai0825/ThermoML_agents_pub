{
  "answer": "## Excess Molar Volume (V_E) Data for Water + Methanol Binary at 298.15 K\n\n**Source:** Safronov & Heyer (2004), DOI 10.1016/j.jct.2004.03.011 [GLOBlit_2395], Block PROPblock_1\n\n**Compounds:**\n- Water (GLOBcomp_1)\n- Methanol (GLOBcomp_4)\n\n**Property:** Excess molar volume (GLOBprop_28), liquid phase\n\nOne block was found in the ThermoML database containing excess molar volume data for the water + methanol binary system at 298.15 K. The data span pressures from 100 to 60000 kPa at three methanol mole fractions (0.25, 0.5, 0.75). All V_E values are negative, indicating volume contraction upon mixing — consistent with strong hydrogen-bonding interactions between water and methanol. The most negative V_E occurs at x(methanol) = 0.5, reflecting the composition of maximum intermolecular interaction.\n\n### Data at T = 298.15 K\n\n| Pressure (kPa) | x(methanol) | V_E (m³/mol) |\n|---|---|---|\n| 100 | 0.25 | −7.42 × 10⁻⁷ |\n| 100 | 0.50 | −1.014 × 10⁻⁶ |\n| 100 | 0.75 | −7.05 × 10⁻⁷ |\n| 5000 | 0.25 | −7.13 × 10⁻⁷ |\n| 5000 | 0.50 | −9.63 × 10⁻⁷ |\n| 5000 | 0.75 | −6.74 × 10⁻⁷ |\n| 10000 | 0.25 | −6.85 × 10⁻⁷ |\n| 10000 | 0.50 | −9.15 × 10⁻⁷ |\n| 10000 | 0.75 | −6.44 × 10⁻⁷ |\n| 20000 | 0.25 | −6.27 × 10⁻⁷ |\n| 20000 | 0.50 | −8.31 × 10⁻⁷ |\n| 20000 | 0.75 | −5.93 × 10⁻⁷ |\n| 30000 | 0.25 | −5.75 × 10⁻⁷ |\n| 30000 | 0.50 | −7.62 × 10⁻⁷ |\n| 30000 | 0.75 | −5.53 × 10⁻⁷ |\n| 40000 | 0.25 | −5.29 × 10⁻⁷ |\n| 40000 | 0.50 | −7.02 × 10⁻⁷ |\n| 40000 | 0.75 | −5.14 × 10⁻⁷ |\n| 50000 | 0.25 | −4.85 × 10⁻⁷ |\n| 50000 | 0.50 | −6.49 × 10⁻⁷ |\n| 50000 | 0.75 | −4.65 × 10⁻⁷ |\n| 60000 | 0.25 | −4.61 × 10⁻⁷ |\n| 60000 | 0.50 | −6.02 × 10⁻⁷ |\n\n**Summary statistics at 298.15 K (23 data points):** V_E ranges from −1.014 × 10⁻⁶ to −4.61 × 10⁻⁷ m³/mol. The magnitude of V_E decreases (becomes less negative) with increasing pressure, indicating that high pressure reduces the volume contraction effect. At all pressures, the equimolar composition (x = 0.5) shows the largest contraction, consistent with the symmetric nature of water–methanol hydrogen bonding.\n\nThe full block contains 206 data points spanning 298.15–523.15 K, 100–60000 kPa, and x(methanol) = 0.25–0.75, with V_E ranging from −2.545 × 10⁻⁶ to −5 × 10⁻⁹ m³/mol.",
  "core_claims": [
    "Excess molar volume data for the water + methanol binary system at 298.15 K were found in one ThermoML block (Safronov & Heyer, 2004), covering pressures from 100 to 60000 kPa at methanol mole fractions of 0.25, 0.5, and 0.75.",
    "All V_E values at 298.15 K are negative, ranging from −1.014 × 10⁻⁶ to −4.61 × 10⁻⁷ m³/mol, indicating volume contraction upon mixing consistent with strong hydrogen-bonding interactions between water and methanol.",
    "At all pressures studied, the equimolar composition (x(methanol) = 0.5) exhibits the most negative V_E, reflecting the composition of maximum intermolecular interaction.",
    "The magnitude of V_E decreases (becomes less negative) with increasing pressure at 298.15 K, indicating that high pressure reduces the volume contraction effect.",
    "The full data block contains 206 data points spanning 298.15–523.15 K, 100–60000 kPa, and x(methanol) = 0.25–0.75, with V_E ranging from −2.545 × 10⁻⁶ to −5 × 10⁻⁹ m³/mol."
  ],
  "status": "success",
  "summary": "Excess molar volume (V_E) data for the water + methanol binary system from Safronov & Heyer (2004), DOI 10.1016/j.jct.2004.03.011 (GLOBlit_2395, PROPblock_1). At 298.15 K, 23 data points cover pressures from 100 to 60000 kPa at methanol mole fractions of 0.25, 0.50, and 0.75. All V_E values are negative, ranging from −1.014 × 10⁻⁶ to −4.61 × 10⁻⁷ m³/mol, indicating volume contraction upon mixing due to strong hydrogen-bonding interactions. The most negative V_E occurs at x(methanol) = 0.5, and the magnitude of V_E decreases with increasing pressure. The full data block contains 206 points spanning 298.15–523.15 K, 100–60000 kPa, and x(methanol) = 0.25–0.75, with V_E ranging from −2.545 × 10⁻⁶ to −5 × 10⁻⁹ m³/mol.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_4",
      "registry_id": "methanol",
      "name": "methanol"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_28",
      "registry_id": "excess_molar_volume_m3_mol",
      "name": "Excess molar volume, m3/mol"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_2395",
      "registry_id": "2004-saf-hey-0",
      "name": "10.1016/j.jct.2004.03.011"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2395",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_28"
      ],
      "description": "Excess molar volume data for water + methanol binary system at 298.15 K, pressures 100–60000 kPa, methanol mole fractions 0.25, 0.5, 0.75.",
      "doi": "10.1016/j.jct.2004.03.011",
      "lit_id": "2004-saf-hey-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 206,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "constraints": [],
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
            "max": 523.15,
            "n_unique": 10
          },
          "range_min": 298.15,
          "range_max": 523.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_3",
          "var_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Pressure, kPa",
            "min": 100.0,
            "max": 60000.0,
            "n_unique": 8
          },
          "range_min": 100.0,
          "range_max": 60000.0
        },
        {
          "BLKvar_id": "BLKvar_3",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_2",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_3",
            "name": "Mole fraction",
            "min": 0.25,
            "max": 0.75,
            "n_unique": 3
          },
          "range_min": 0.25,
          "range_max": 0.75
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_28",
          "prop_ID": "excess_molar_volume_m3_mol",
          "name": "Excess molar volume, m3/mol",
          "group": "VolumetricProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_207",
          "meas_ID": "same_ufactor_2",
          "method_standard": null,
          "method_custom": "SAME:UFactor:2",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Excess molar volume, m3/mol",
            "min": -3e-06,
            "max": -0.0,
            "mean": -1e-06,
            "std": 0.0,
            "n": 206
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -3e-06,
          "range_max": -0.0
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
          "owner_id": "BLKvar_3",
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
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "parent_n_datapoints": 206,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2004.03.011",
      "block_number": "PROPblock_1",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "pressure_kpa",
        "mole_fraction_<methanol>",
        "excess_molar_volume_m3_mol"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<methanol>": "0.25",
          "excess_molar_volume_m3_mol": "-7.42e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<methanol>": "0.5",
          "excess_molar_volume_m3_mol": "-1.014e-06"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<methanol>": "0.75",
          "excess_molar_volume_m3_mol": "-7.05e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "298.15",
          "pressure_kpa": "5000",
          "mole_fraction_<methanol>": "0.25",
          "excess_molar_volume_m3_mol": "-7.13e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "pressure_kpa": "5000",
          "mole_fraction_<methanol>": "0.5",
          "excess_molar_volume_m3_mol": "-9.63e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "pressure_kpa": "5000",
          "mole_fraction_<methanol>": "0.75",
          "excess_molar_volume_m3_mol": "-6.74e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "pressure_kpa": "10000",
          "mole_fraction_<methanol>": "0.25",
          "excess_molar_volume_m3_mol": "-6.85e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "298.15",
          "pressure_kpa": "10000",
          "mole_fraction_<methanol>": "0.5",
          "excess_molar_volume_m3_mol": "-9.15e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "pressure_kpa": "10000",
          "mole_fraction_<methanol>": "0.75",
          "excess_molar_volume_m3_mol": "-6.44e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "pressure_kpa": "20000",
          "mole_fraction_<methanol>": "0.25",
          "excess_molar_volume_m3_mol": "-6.27e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "pressure_kpa": "20000",
          "mole_fraction_<methanol>": "0.5",
          "excess_molar_volume_m3_mol": "-8.31e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "pressure_kpa": "20000",
          "mole_fraction_<methanol>": "0.75",
          "excess_molar_volume_m3_mol": "-5.93e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "298.15",
          "pressure_kpa": "30000",
          "mole_fraction_<methanol>": "0.25",
          "excess_molar_volume_m3_mol": "-5.75e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "pressure_kpa": "30000",
          "mole_fraction_<methanol>": "0.5",
          "excess_molar_volume_m3_mol": "-7.62e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "298.15",
          "pressure_kpa": "30000",
          "mole_fraction_<methanol>": "0.75",
          "excess_molar_volume_m3_mol": "-5.53e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "298.15",
          "pressure_kpa": "40000",
          "mole_fraction_<methanol>": "0.25",
          "excess_molar_volume_m3_mol": "-5.29e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "298.15",
          "pressure_kpa": "40000",
          "mole_fraction_<methanol>": "0.5",
          "excess_molar_volume_m3_mol": "-7.02e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "298.15",
          "pressure_kpa": "40000",
          "mole_fraction_<methanol>": "0.75",
          "excess_molar_volume_m3_mol": "-5.14e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "298.15",
          "pressure_kpa": "50000",
          "mole_fraction_<methanol>": "0.25",
          "excess_molar_volume_m3_mol": "-4.85e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "temperature_k": "298.15",
          "pressure_kpa": "50000",
          "mole_fraction_<methanol>": "0.5",
          "excess_molar_volume_m3_mol": "-6.49e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "298.15",
          "pressure_kpa": "50000",
          "mole_fraction_<methanol>": "0.75",
          "excess_molar_volume_m3_mol": "-4.65e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "298.15",
          "pressure_kpa": "60000",
          "mole_fraction_<methanol>": "0.25",
          "excess_molar_volume_m3_mol": "-4.61e-07"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "298.15",
          "pressure_kpa": "60000",
          "mole_fraction_<methanol>": "0.5",
          "excess_molar_volume_m3_mol": "-6.02e-07"
        }
      ],
      "inspection_id": "INSP_f57121e6304e",
      "lit_num_id": "GLOBlit_2395"
    }
  ]
}