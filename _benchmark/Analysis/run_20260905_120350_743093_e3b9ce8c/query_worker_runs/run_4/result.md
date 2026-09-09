{
  "answer": "## DMSO + Water Binary Mixture Data Near 25 °C\n\nThree data blocks were found in the ThermoML database for dimethyl sulfoxide (DMSO, GLOBcomp_31) + water (GLOBcomp_1) binary mixtures with refractive index, speed of sound, or surface tension measurements near 298.15 K. **No heat capacity (Cp) data** was found for this system.\n\n### Summary of Available Blocks\n\n| Block | DOI | Literature ID | Property | Total Pts | T range (K) |\n|---|---|---|---|---|---|\n| PROPblock_3 | 10.1016/j.jct.2006.01.007 | GLOBlit_2652 | Speed of sound (m/s) | 6 | 288.15–313.15 |\n| PROPblock_9 | 10.1021/je7001013 | GLOBlit_10766 | Surface tension (N/m) | 112 | 298.15–328.15 |\n| PROPblock_10 | 10.1021/je7001013 | GLOBlit_10766 | Refractive index (Na D-line) | 33 | 298.15–308.15 |\n\n### Representative Data at 298.15 K\n\n**Speed of sound** (GLOBlit_2652 :: PROPblock_3) — fixed composition x(DMSO) = 0.0385, P = 101.0 kPa:\n\n| T (K) | u (m/s) |\n|---|---|\n| 298.15 | 1568.53 |\n\nThe full block spans 288.15–313.15 K with speed of sound ranging from 1555.18 to 1579.41 m/s (6 points, monotonically increasing with temperature).\n\n**Surface tension** (GLOBlit_10766 :: PROPblock_9) at 298.15 K — 16 compositions measured, x(DMSO) = 0.0121–0.8945:\n\n| x(DMSO) | γ (N/m) |\n|---|---|\n| 0.0121 | 0.071 |\n| 0.1044 | 0.0612 |\n| 0.1979 | 0.0567 |\n| 0.2507 | 0.0554 |\n| 0.2999 | 0.0533 |\n| 0.3536 | 0.0526 |\n| 0.4523 | 0.0503 |\n| 0.501 | 0.0483 |\n| 0.59 | 0.046 |\n| 0.7027 | 0.044 |\n| 0.8088 | 0.0426 |\n| 0.8945 | 0.042 |\n\n**Refractive index** (GLOBlit_10766 :: PROPblock_10) at 298.15 K, P = 101.0 kPa — 11 compositions, x(DMSO) = 0.0121–0.7685:\n\n| x(DMSO) | n_D |\n|---|---|\n| 0.0121 | 1.34 |\n| 0.0202 | 1.344 |\n| 0.1467 | 1.396 |\n| 0.2455 | 1.4215 |\n| 0.2959 | 1.4305 |\n| 0.3213 | 1.4345 |\n| 0.3713 | 1.4415 |\n| 0.3967 | 1.4445 |\n| 0.4301 | 1.4475 |\n| 0.5964 | 1.461 |\n| 0.7685 | 1.47 |\n\n### Chemistry Insight\n\nFrom the surface tension block (GLOBlit_10766 :: PROPblock_9), the data show a steep initial drop from γ = 0.071 N/m at x(DMSO) = 0.0121 to 0.0612 N/m at x(DMSO) = 0.1044, followed by a more gradual decrease to 0.042 N/m at x(DMSO) = 0.8945. This steep initial decline reflects DMSO's preferential adsorption at the air–water interface at low concentrations. From the refractive index block (GLOBlit_10766 :: PROPblock_10), the refractive index increases monotonically from 1.34 to 1.47 across the composition range x(DMSO) = 0.0121–0.7685, consistent with the higher polarizability of DMSO compared to water.",
  "core_claims": [
    "Three ThermoML data blocks were found for the DMSO + water binary system near 298.15 K, covering speed of sound, surface tension, and refractive index; no heat capacity (Cp) data was found for this system.",
    "At 298.15 K and x(DMSO) = 0.0385, the speed of sound is 1568.53 m/s (P = 101.0 kPa), from a block spanning 288.15–313.15 K with values ranging from 1555.18 to 1579.41 m/s.",
    "At 298.15 K, surface tension decreases steeply from 0.071 N/m at x(DMSO) = 0.0121 to 0.0612 N/m at x(DMSO) = 0.1044, then more gradually to 0.042 N/m at x(DMSO) = 0.8945, reflecting DMSO's preferential adsorption at the air–water interface at low concentrations.",
    "At 298.15 K and P = 101.0 kPa, the refractive index increases monotonically from 1.34 at x(DMSO) = 0.0121 to 1.47 at x(DMSO) = 0.7685, consistent with the higher polarizability of DMSO compared to water."
  ],
  "status": "success",
  "summary": "Three ThermoML data blocks were found for the DMSO (GLOBcomp_31) + water (GLOBcomp_1) binary system near 298.15 K. No heat capacity data was found. Speed of sound data (DOI 10.1016/j.jct.2006.01.007, GLOBlit_2652, PROPblock_3) at fixed x(DMSO) = 0.0385 and 101.0 kPa gives 1568.53 m/s at 298.15 K, spanning 1555.18–1579.41 m/s over 288.15–313.15 K (6 points). Surface tension data (DOI 10.1021/je7001013, GLOBlit_10766, PROPblock_9) at 298.15 K covers 16 compositions from x(DMSO) = 0.0121 (γ = 0.071 N/m) to 0.8945 (γ = 0.042 N/m), showing a steep initial drop reflecting DMSO's preferential adsorption at the air–water interface. Refractive index data (same DOI, PROPblock_10) at 298.15 K and 101.0 kPa spans 11 compositions from x(DMSO) = 0.0121 (n_D = 1.34) to 0.7685 (n_D = 1.47), increasing monotonically consistent with DMSO's higher polarizability relative to water.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_31",
      "registry_id": "dimethyl_sulfoxide",
      "name": "dimethyl sulfoxide"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_2652",
      "registry_id": "2006-mie-kac-0",
      "name": "10.1016/j.jct.2006.01.007"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_10766",
      "registry_id": "2007-mar-ter-0",
      "name": "10.1021/je7001013"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_7",
      "registry_id": "refractive_index_na_dline",
      "name": "Refractive index (Na D-line)"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_8",
      "registry_id": "speed_of_sound_m_s",
      "name": "Speed of sound, m/s"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_13",
      "registry_id": "surface_tension_liquidgas_n_m",
      "name": "Surface tension liquid-gas, N/m"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_9",
      "registry_id": "molar_heat_capacity_at_constant_pressure_j_k_mol",
      "name": "Molar heat capacity at constant pressure, J/K/mol"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2652",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_8"
      ],
      "description": "Speed of sound measurements for DMSO + water binary mixture, 6 points, T = 288.15–313.15 K, fixed x(DMSO) = 0.0385, P = 101.0 kPa.",
      "doi": "10.1016/j.jct.2006.01.007",
      "lit_id": "2006-mie-kac-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 6,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "solvents": [],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_3",
          "constr_id": "mole_fraction_DOIcomp_3",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "value": 0.0385,
          "digits": 3,
          "component_org_num": "DOIcomp_3",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          }
        },
        {
          "BLKconstr_id": "BLKconstr_2",
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
            "min": 288.15,
            "max": 313.15,
            "n_unique": 6
          },
          "range_min": 288.15,
          "range_max": 313.15
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
            "min": 1555.18,
            "max": 1579.41,
            "mean": 1569.326667,
            "std": 9.218429,
            "n": 6
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1555.18,
          "range_max": 1579.41
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
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 6,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension measurements for DMSO + water binary mixture, 112 points, T = 298.15–328.15 K, x(DMSO) = 0.0121–0.8945.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 112,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_1_1"
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
            "max": 328.15,
            "n_unique": 7
          },
          "range_min": 298.15,
          "range_max": 328.15
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
            "min": 0.0121,
            "max": 0.8945,
            "n_unique": 19
          },
          "range_min": 0.0121,
          "range_max": 0.8945
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_13",
          "prop_ID": "surface_tension_liquidgas_n_m",
          "name": "Surface tension liquid-gas, N/m",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_36",
          "meas_ID": "maximal_bubble_pressure",
          "method_standard": "Maximal bubble pressure",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0387,
            "max": 0.071,
            "mean": 0.050623,
            "std": 0.008081,
            "n": 112
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0387,
          "range_max": 0.071
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
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 112,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_10",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index (Na D-line) measurements for DMSO + water binary mixture, 33 points, T = 298.15–308.15 K, P = 101.0 kPa, x(DMSO) = 0.0121–0.7685.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 33,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_1_1"
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
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
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
            "min": 0.0121,
            "max": 0.7685,
            "n_unique": 11
          },
          "range_min": 0.0121,
          "range_max": 0.7685
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_7",
          "prop_ID": "refractive_index_na_dline",
          "name": "Refractive index (Na D-line)",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.339,
            "max": 1.47,
            "mean": 1.420136,
            "std": 0.041686,
            "n": 33
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.339,
          "range_max": 1.47
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 33,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2006.01.007",
      "block_number": "PROPblock_3",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<dimethyl sulfoxide>",
        "pressure_kpa",
        "speed_of_sound_m_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "288.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0385",
          "pressure_kpa": "101.0",
          "speed_of_sound_m_s": "1555.18"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "293.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0385",
          "pressure_kpa": "101.0",
          "speed_of_sound_m_s": "1562.46"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0385",
          "pressure_kpa": "101.0",
          "speed_of_sound_m_s": "1568.53"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0385",
          "pressure_kpa": "101.0",
          "speed_of_sound_m_s": "1573.38"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0385",
          "pressure_kpa": "101.0",
          "speed_of_sound_m_s": "1577"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0385",
          "pressure_kpa": "101.0",
          "speed_of_sound_m_s": "1579.41"
        }
      ],
      "inspection_id": "INSP_859c666658c3",
      "lit_num_id": "GLOBlit_2652"
    },
    {
      "doi": "10.1021/je7001013",
      "block_number": "PROPblock_9",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<dimethyl sulfoxide>",
        "surface_tension_liquidgas_n_m"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.071"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.0612"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1979",
          "surface_tension_liquidgas_n_m": "0.0567"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2507",
          "surface_tension_liquidgas_n_m": "0.0554"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2999",
          "surface_tension_liquidgas_n_m": "0.0533"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3536",
          "surface_tension_liquidgas_n_m": "0.0526"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4523",
          "surface_tension_liquidgas_n_m": "0.0503"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.501",
          "surface_tension_liquidgas_n_m": "0.0483"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.046"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7027",
          "surface_tension_liquidgas_n_m": "0.044"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8088",
          "surface_tension_liquidgas_n_m": "0.0426"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.042"
        }
      ],
      "inspection_id": "INSP_4c118f2b8c2e",
      "lit_num_id": "GLOBlit_10766"
    },
    {
      "doi": "10.1021/je7001013",
      "block_number": "PROPblock_10",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<dimethyl sulfoxide>",
        "pressure_kpa",
        "refractive_index_na_dline"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.34"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0202",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.344"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1467",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.396"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2455",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4215"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2959",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4305"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3213",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4345"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3713",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4415"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3967",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4445"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4301",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4475"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.5964",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.461"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7685",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.47"
        }
      ],
      "inspection_id": "INSP_6c692cd44b0e",
      "lit_num_id": "GLOBlit_10766"
    }
  ]
}