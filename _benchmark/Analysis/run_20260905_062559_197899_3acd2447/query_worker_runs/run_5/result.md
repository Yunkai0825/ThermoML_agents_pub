{
  "answer": "## Excess Molar Enthalpy (Hᴱ) for Ethanol + Water at 298.15 K — Full Composition Range\n\nAfter searching all available binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) excess molar enthalpy (GLOBprop_17) blocks in the ThermoML database, **GLOBlit_2574 PROPblock_4** (DOI: 10.1016/j.jct.2005.06.018) is confirmed as the best available full-range source at 298.15 K.\n\n### Data Summary\n\nThe block contains **12 data points at 298.15 K** spanning x(ethanol) = 0.0582 to 0.9, at a fixed pressure of 101.0 kPa. All Hᴱ values are negative (exothermic mixing), with a minimum (most exothermic) near x ≈ 0.15.\n\n| x(ethanol) | Hᴱ (kJ/mol) |\n|---|---|\n| 0.0582 | −0.492 |\n| 0.1198 | −0.747 |\n| 0.15 | −0.770 |\n| 0.1837 | −0.767 |\n| 0.25 | −0.702 |\n| 0.2981 | −0.649 |\n| 0.4127 | −0.501 |\n| 0.5 | −0.391 |\n| 0.607 | −0.323 |\n| 0.701 | −0.271 |\n| 0.812 | −0.206 |\n| 0.9 | −0.148 |\n\nSource: GLOBlit_2574 :: PROPblock_4 (DOI: 10.1016/j.jct.2005.06.018)\n\n### Key Observations\n\n- **Composition coverage**: x(ethanol) from 0.0582 to 0.9 — good but not extending to the very dilute water-in-ethanol limit (x → 1) or the most dilute ethanol-in-water region (x < 0.058). The full block (including other temperatures) extends to x = 0.033–0.968.\n- **Hᴱ minimum**: The most exothermic mixing occurs at x(ethanol) ≈ 0.15, with Hᴱ = −0.770 kJ/mol. This asymmetric minimum (shifted toward the water-rich side) is characteristic of ethanol–water systems, reflecting the disruption of the water hydrogen-bond network by ethanol molecules.\n- **No other full-range source found**: GLOBlit_528 covers only the extremely dilute regime (x < 0.002), and GLOBlit_6377 has only a single point. No additional full-range blocks exist in the database.\n\n### Note on the Source\n\nThe publication (10.1016/j.jct.2005.06.018) title references propanediols, but the block is registered as binary ethanol + water. This compound-mapping caveat was noted in prior context. The data values themselves are consistent with well-known ethanol–water Hᴱ behavior (negative, asymmetric minimum near x ≈ 0.15–0.2, magnitude ~0.7–0.8 kJ/mol at the minimum).",
  "core_claims": [
    "The best available full-range source for excess molar enthalpy (Hᴱ) of ethanol + water at 298.15 K in the ThermoML database is GLOBlit_2574 PROPblock_4 (DOI: 10.1016/j.jct.2005.06.018), containing 12 data points at 101.0 kPa spanning x(ethanol) = 0.0582 to 0.9.",
    "All reported Hᴱ values at 298.15 K are negative (exothermic mixing), with the most exothermic value of −0.770 kJ/mol occurring at x(ethanol) ≈ 0.15, reflecting an asymmetric minimum shifted toward the water-rich side.",
    "The composition coverage does not extend to the very dilute ethanol-in-water region (x < 0.058) or the dilute water-in-ethanol limit (x → 1) at 298.15 K, and no other full-range source was found in the database.",
    "A compound-mapping caveat exists: the source publication title references propanediols, but the block is registered as binary ethanol + water; however, the data values are consistent with well-known ethanol–water Hᴱ behavior."
  ],
  "status": "success",
  "summary": "Excess molar enthalpy (Hᴱ) for ethanol + water at 298.15 K across the full composition range is reported from GLOBlit_2574 PROPblock_4 (DOI: 10.1016/j.jct.2005.06.018). The block contains 12 data points at 101.0 kPa spanning x(ethanol) = 0.0582 to 0.9. All Hᴱ values are negative (exothermic mixing), with a minimum of −0.770 kJ/mol near x(ethanol) ≈ 0.15. Representative values include −0.492 kJ/mol at x = 0.0582, −0.747 at x = 0.1198, −0.702 at x = 0.25, −0.391 at x = 0.5, −0.271 at x = 0.701, and −0.148 kJ/mol at x = 0.9. The asymmetric minimum shifted toward the water-rich side is characteristic of ethanol–water systems. No other full-range source was found in the database; GLOBlit_528 covers only the extremely dilute regime (x < 0.002) and GLOBlit_6377 has only a single point. A caveat is noted that the source publication title references propanediols, but the block is registered as binary ethanol + water, and the data values are consistent with well-known ethanol–water Hᴱ behavior.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2574",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_17"
      ],
      "description": "Excess molar enthalpy for ethanol + water at 298.15 K, 12 data points spanning x(ethanol) = 0.0582 to 0.9, all negative with minimum near x ≈ 0.15.",
      "doi": "10.1016/j.jct.2005.06.018",
      "lit_id": "2006-nag-fra-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 27,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_5_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_4_1"
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
            "max": 323.15,
            "n_unique": 2
          },
          "range_min": 298.15,
          "range_max": 323.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_5",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_5",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.033,
            "max": 0.968,
            "n_unique": 27
          },
          "range_min": 0.033,
          "range_max": 0.968
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_17",
          "prop_ID": "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol",
          "name": "Excess molar enthalpy (molar enthalpy of mixing), kJ/mol",
          "group": "ExcessPartialApparentEnergyProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_169",
          "meas_ID": "calvet_ufactor_2",
          "method_standard": null,
          "method_custom": "CALVET:UFactor:2",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Excess molar enthalpy (molar enthalpy of mixing), kJ/mol",
            "min": -0.77,
            "max": -0.018,
            "mean": -0.325074,
            "std": 0.241185,
            "n": 27
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -0.77,
          "range_max": -0.018
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
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_5_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "parent_n_datapoints": 27,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2005.06.018",
      "block_number": "PROPblock_4",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<ethanol>",
        "pressure_kpa",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.0582",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.492"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.1198",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.747"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.77"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.1837",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.767"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.25",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.702"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.2981",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.649"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.4127",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.501"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.5",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.391"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.607",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.323"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.701",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.271"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.812",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.206"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.9",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.148"
        }
      ],
      "inspection_id": "INSP_6d19d0a7d0d6",
      "lit_num_id": "GLOBlit_2574"
    }
  ]
}