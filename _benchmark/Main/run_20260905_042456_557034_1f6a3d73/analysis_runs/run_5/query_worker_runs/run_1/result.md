{
  "answer": "## Excess Molar Volume (V^E) Data for Methanol + Water at 298.15 K and Atmospheric Pressure\n\nOne data block was found in the ThermoML database containing excess molar volume measurements for the binary system methanol (CH₃OH) + water (H₂O) at 298.15 K and atmospheric pressure (100 kPa):\n\n**Source:** DOI 10.1016/j.jct.2004.03.011 (GLOBlit_2395), PROPblock_1\n\n**Property:** Excess molar volume (GLOBprop_28), liquid phase\n\n**Data at T = 298.15 K, P = 100 kPa:**\n\n| Mole fraction of methanol (x) | V^E (m³/mol) |\n|---|----|\n| 0.25 | −7.42 × 10⁻⁷ |\n| 0.50 | −1.014 × 10⁻⁶ |\n| 0.75 | −7.05 × 10⁻⁷ |\n\nAll three values are negative, which is characteristic of the methanol–water system. The most negative excess molar volume occurs at x(methanol) = 0.50 (V^E = −1.014 × 10⁻⁶ m³/mol ≈ −1.014 cm³/mol), indicating maximum volume contraction near the equimolar composition. This behavior reflects strong hydrogen-bonding interactions between methanol and water molecules that lead to a more efficient molecular packing compared to the ideal mixture.\n\nThe full block contains 206 data points spanning temperatures from 298.15 K to 523.15 K, pressures from 100 kPa to 60,000 kPa, and methanol mole fractions of 0.25, 0.50, and 0.75, with V^E values ranging from −2.545 × 10⁻⁶ to −5 × 10⁻⁹ m³/mol across all conditions.",
  "core_claims": [
    "One ThermoML data block (DOI 10.1016/j.jct.2004.03.011, PROPblock_1) reports excess molar volume (V^E) for methanol + water in the liquid phase at 298.15 K and 100 kPa at three methanol mole fractions: V^E = −7.42 × 10⁻⁷ m³/mol at x = 0.25, V^E = −1.014 × 10⁻⁶ m³/mol at x = 0.50, and V^E = −7.05 × 10⁻⁷ m³/mol at x = 0.75.",
    "All three excess molar volume values are negative, with the most negative value occurring at x(methanol) = 0.50, indicating maximum volume contraction near the equimolar composition.",
    "The full data block contains 206 data points spanning temperatures from 298.15 K to 523.15 K, pressures from 100 kPa to 60,000 kPa, and methanol mole fractions of 0.25, 0.50, and 0.75, with V^E values ranging from −2.545 × 10⁻⁶ to −5 × 10⁻⁹ m³/mol across all conditions."
  ],
  "status": "success",
  "summary": "Excess molar volume (V^E) data for methanol + water at 298.15 K and 100 kPa were found in the ThermoML database from DOI 10.1016/j.jct.2004.03.011 (GLOBlit_2395, PROPblock_1, GLOBprop_28, liquid phase). At methanol mole fractions of 0.25, 0.50, and 0.75, V^E values are −7.42 × 10⁻⁷, −1.014 × 10⁻⁶, and −7.05 × 10⁻⁷ m³/mol, respectively. All values are negative, with the most negative at x = 0.50 (≈ −1.014 cm³/mol), indicating maximum volume contraction near equimolar composition due to strong hydrogen-bonding interactions. The full data block contains 206 points spanning 298.15–523.15 K, 100–60,000 kPa, and methanol mole fractions of 0.25, 0.50, and 0.75, with V^E ranging from −2.545 × 10⁻⁶ to −5 × 10⁻⁹ m³/mol across all conditions.",
  "core_id_updates": [],
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
      "description": "Excess molar volume for methanol + water at 298.15 K and 100 kPa.",
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
      "table_mode": "complete",
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
        }
      ],
      "inspection_id": "INSP_1365f8ab7be4",
      "lit_num_id": "GLOBlit_2395"
    }
  ]
}