{
  "answer": "## Excess Molar Enthalpy (Hᴱ) Data for Methanol + Water at 298.15 K\n\n**One block found** in the ThermoML database containing excess molar enthalpy data for the methanol + water binary system at 298.15 K.\n\n### Source Details\n\n| Field | Value |\n|---|---|\n| **DOI** | 10.1016/j.tca.2006.02.028 |\n| **Literature ID** | GLOBlit_5688 |\n| **Block** | PROPblock_1 |\n| **Property** | Excess molar enthalpy (GLOBprop_17), kJ/mol |\n| **Method** | Titration calorimetry (GLOBmeas_25) |\n| **Temperature** | 298.15 K (constant) |\n| **Pressure** | 101.0 kPa (constant) |\n| **Total data points** | 13 |\n\n### Data Table (10 of 13 points, RDP shape-preserving subset)\n\n| x(methanol) | Hᴱ (kJ/mol) |\n|---|---|\n| 0.0 | 0.0 |\n| 0.05 | −0.326 |\n| 0.15 | −0.714 |\n| 0.2 | −0.806 |\n| 0.3 | −0.85 |\n| 0.4 | −0.841 |\n| 0.5 | −0.777 |\n| 0.7 | −0.583 |\n| 0.9 | −0.241 |\n| 1.0 | 0.0 |\n\n**Full-block statistics (all 13 points):** x(methanol) spans 0–1; Hᴱ ranges from −0.85 to 0 kJ/mol.\n\n### Chemical Insight\n\nThe excess molar enthalpy is negative across the entire composition range, indicating that mixing methanol and water at 298.15 K is an exothermic process. The minimum Hᴱ of approximately −0.85 kJ/mol occurs near x(methanol) ≈ 0.3, reflecting the strong hydrogen-bonding interactions between methanol and water molecules. The asymmetric shape of the Hᴱ curve (minimum shifted toward the methanol-lean side) is characteristic of aqueous alcohol systems, where the disruption and reformation of hydrogen-bond networks is most energetically favorable at compositions where water molecules can effectively solvate the alcohol hydroxyl groups.",
  "core_claims": [
    "One block of excess molar enthalpy (Hᴱ) data for methanol + water at 298.15 K and 101.0 kPa was found in the ThermoML database (DOI 10.1016/j.tca.2006.02.028), measured by titration calorimetry, containing 13 data points spanning x(methanol) = 0–1.",
    "Hᴱ is negative across the entire composition range, indicating that mixing methanol and water at 298.15 K is exothermic, with values ranging from −0.85 to 0 kJ/mol.",
    "The minimum Hᴱ of approximately −0.85 kJ/mol occurs near x(methanol) ≈ 0.3, and the asymmetric shape of the Hᴱ curve (minimum shifted toward the methanol-lean side) is characteristic of aqueous alcohol systems reflecting strong hydrogen-bonding interactions."
  ],
  "status": "success",
  "summary": "One ThermoML block was found for the excess molar enthalpy (Hᴱ) of methanol + water at 298.15 K and 101.0 kPa, from DOI 10.1016/j.tca.2006.02.028, measured by titration calorimetry. The block contains 13 data points spanning x(methanol) = 0–1. Hᴱ is negative across the entire composition range, with a minimum of approximately −0.85 kJ/mol near x(methanol) ≈ 0.3, indicating exothermic mixing driven by strong hydrogen-bonding interactions. A shape-preserving subset of 10 points is reported, including x(methanol) values of 0.0, 0.05, 0.15, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, and 1.0 with corresponding Hᴱ values of 0.0, −0.326, −0.714, −0.806, −0.85, −0.841, −0.777, −0.583, −0.241, and 0.0 kJ/mol. The asymmetric curve shape, with the minimum shifted toward the methanol-lean side, is characteristic of aqueous alcohol systems.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_5688",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_17"
      ],
      "description": "Excess molar enthalpy for methanol + water at 298.15 K and 101.0 kPa, 13 data points, measured by titration calorimetry.",
      "doi": "10.1016/j.tca.2006.02.028",
      "lit_id": "2006-beh-gha-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 13,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_1_1"
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
            "min": 0.0,
            "max": 1.0,
            "n_unique": 13
          },
          "range_min": 0.0,
          "range_max": 1.0
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
          "meas_num_id": "GLOBmeas_25",
          "meas_ID": "titration_calorimetry",
          "method_standard": null,
          "method_custom": "Titration calorimetry",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Excess molar enthalpy (molar enthalpy of mixing), kJ/mol",
            "min": -0.85,
            "max": 0.0,
            "mean": -0.521538,
            "std": 0.302187,
            "n": 13
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -0.85,
          "range_max": 0.0
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 13,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.tca.2006.02.028",
      "block_number": "PROPblock_1",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<methanol>",
        "temperature_k",
        "pressure_kpa",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<methanol>": "0",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "mole_fraction_<methanol>": "0.05",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.326"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mole_fraction_<methanol>": "0.15",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.714"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "mole_fraction_<methanol>": "0.2",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.806"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "mole_fraction_<methanol>": "0.3",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.85"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "mole_fraction_<methanol>": "0.4",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.841"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mole_fraction_<methanol>": "0.5",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.777"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "mole_fraction_<methanol>": "0.7",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.583"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "mole_fraction_<methanol>": "0.9",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.241"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "mole_fraction_<methanol>": "1",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "0"
        }
      ],
      "inspection_id": "INSP_6bf554d45167",
      "lit_num_id": "GLOBlit_5688"
    }
  ]
}