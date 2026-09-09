{
  "answer": "## Density Data for 1-Propanol + Water at 298.15 K (for Excess Molar Volume Derivation)\n\nThe best block found is **PROPblock_14** from **GLOBlit_11042** (DOI: 10.1021/je700700f), which contains mass density data for the binary system 1-propanol (propan-1-ol) + water at 298.15 K and 101.0 kPa, covering the full mole-fraction range from 0 to 1 with **13 data points**.\n\n### Complete Data Table\n\n| BLKpoint_id | x(1-propanol) | Pressure (kPa) | Temperature (K) | Density (kg/m³) |\n|---|---|---|---|---|\n| BLKpoint_1  | 0      | 101.0 | 298.15 | 997.2 |\n| BLKpoint_2  | 0.0504 | 101.0 | 298.15 | 975.1 |\n| BLKpoint_3  | 0.0993 | 101.0 | 298.15 | 953.3 |\n| BLKpoint_4  | 0.1986 | 101.0 | 298.15 | 914.9 |\n| BLKpoint_5  | 0.2979 | 101.0 | 298.15 | 887.2 |\n| BLKpoint_6  | 0.3949 | 101.0 | 298.15 | 866.9 |\n| BLKpoint_7  | 0.4955 | 101.0 | 298.15 | 850.3 |\n| BLKpoint_8  | 0.5953 | 101.0 | 298.15 | 836.9 |\n| BLKpoint_9  | 0.6995 | 101.0 | 298.15 | 825.6 |\n| BLKpoint_10 | 0.7969 | 101.0 | 298.15 | 816.3 |\n| BLKpoint_11 | 0.8983 | 101.0 | 298.15 | 807.7 |\n| BLKpoint_12 | 0.9518 | 101.0 | 298.15 | 803.5 |\n| BLKpoint_13 | 1      | 101.0 | 298.15 | 799.6 |\n\n### Key Details\n- **Literature:** GLOBlit_11042, DOI 10.1021/je700700f\n- **Block:** PROPblock_14 (binary: propan-1-ol + water)\n- **Data points:** 13\n- **Composition range:** x(1-propanol) = 0 to 1 (full range)\n- **Temperature:** 298.15 K (isothermal, all points)\n- **Pressure:** 101.0 kPa (all points)\n- **Density range:** 799.6 kg/m³ (pure 1-propanol) to 997.2 kg/m³ (pure water)\n\n### Chemistry Insight for Excess Molar Volume Derivation\n\nThe density decreases monotonically from pure water (997.2 kg/m³) to pure 1-propanol (799.6 kg/m³). The excess molar volume V^E can be computed at each composition from:\n\nV^E = V_mix − (x₁V₁* + x₂V₂*)\n\nwhere V_mix = (x₁M₁ + x₂M₂)/ρ_mix, using the molar masses of 1-propanol and water (these are standard IUPAC molar masses, not from this database). The pure-component molar volumes V₁* and V₂* are obtained from the endpoint densities (BLKpoint_13 and BLKpoint_1). For 1-propanol + water, V^E is expected to be negative across the composition range, reflecting volume contraction due to hydrogen-bonding interactions between the alcohol and water molecules, with a minimum typically near x ≈ 0.3–0.4. The 13-point coverage across the full composition range is well-suited for this derivation.",
  "core_claims": [
    "Mass density data for the binary system 1-propanol + water at 298.15 K and 101.0 kPa are available from PROPblock_14 of GLOBlit_11042 (DOI: 10.1021/je700700f), comprising 13 data points spanning the full mole-fraction range x(1-propanol) = 0 to 1.",
    "The density decreases monotonically from 997.2 kg/m³ for pure water to 799.6 kg/m³ for pure 1-propanol across the composition range at 298.15 K and 101.0 kPa.",
    "The 13-point full-range composition coverage is suitable for deriving excess molar volume V^E, which for 1-propanol + water is expected to be negative across the composition range due to volume contraction from hydrogen-bonding interactions, with a minimum typically near x ≈ 0.3–0.4."
  ],
  "status": "success",
  "summary": "Density data for the binary system 1-propanol + water at 298.15 K and 101.0 kPa, from PROPblock_14 of GLOBlit_11042 (DOI: 10.1021/je700700f). The dataset contains 13 data points spanning the full mole-fraction range x(1-propanol) = 0 to 1. Density decreases monotonically from 997.2 kg/m³ (pure water) to 799.6 kg/m³ (pure 1-propanol). Specific measured compositions and densities include x = 0.0504 (975.1 kg/m³), 0.0993 (953.3), 0.1986 (914.9), 0.2979 (887.2), 0.3949 (866.9), 0.4955 (850.3), 0.5953 (836.9), 0.6995 (825.6), 0.7969 (816.3), 0.8983 (807.7), and 0.9518 (803.5 kg/m³). The full-range coverage is suitable for deriving excess molar volumes V^E, which are expected to be negative across the composition range due to volume contraction from hydrogen-bonding interactions, with a minimum typically near x ≈ 0.3–0.4.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_11042",
      "block_number": "PROPblock_14",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_5",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density data for 1-propanol + water at 298.15 K and 101.0 kPa, 13 data points covering x(1-propanol) = 0 to 1, density range 799.6–997.2 kg/m³.",
      "doi": "10.1021/je700700f",
      "lit_id": "2008-gon-cal-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 13,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_1_1"
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
          "prop_num_id": "GLOBprop_1",
          "prop_ID": "mass_density_kg_m3",
          "name": "Mass density, kg/m3",
          "group": "VolumetricProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_134",
          "meas_ID": "vibtub_ufactor_4",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 799.6,
            "max": 997.2,
            "mean": 871.884615,
            "std": 68.33647,
            "n": 13
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 799.6,
          "range_max": 997.2
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
          "comp_num_id": "GLOBcomp_5",
          "name": "propan-1-ol",
          "formula": "C3H8O",
          "inchi_key": "BDERNNFJNOPAEC-UHFFFAOYSA-N",
          "SMILES": "CCCO",
          "sample_num": "DOIcompSample_1_1"
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
      "doi": "10.1021/je700700f",
      "block_number": "PROPblock_14",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<propan-1-ol>",
        "pressure_kpa",
        "temperature_k",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<propan-1-ol>": "0",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "997.2"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mole_fraction_<propan-1-ol>": "0.1986",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "914.9"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "mole_fraction_<propan-1-ol>": "0.2979",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "887.2"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "mole_fraction_<propan-1-ol>": "0.3949",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "866.9"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "mole_fraction_<propan-1-ol>": "0.4955",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "850.3"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mole_fraction_<propan-1-ol>": "0.5953",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "836.9"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "mole_fraction_<propan-1-ol>": "0.7969",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "816.3"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "mole_fraction_<propan-1-ol>": "1",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "799.6"
        }
      ],
      "inspection_id": "INSP_615d3595b96a",
      "lit_num_id": "GLOBlit_11042"
    },
    {
      "doi": "10.1021/je700700f",
      "block_number": "PROPblock_14",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<propan-1-ol>",
        "pressure_kpa",
        "temperature_k",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_2",
          "mole_fraction_<propan-1-ol>": "0.0504",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "975.1"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "mole_fraction_<propan-1-ol>": "0.0993",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "953.3"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mole_fraction_<propan-1-ol>": "0.1986",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "914.9"
        }
      ],
      "inspection_id": "INSP_3994bf71b34f",
      "lit_num_id": "GLOBlit_11042"
    },
    {
      "doi": "10.1021/je700700f",
      "block_number": "PROPblock_14",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<propan-1-ol>",
        "pressure_kpa",
        "temperature_k",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_8",
          "mole_fraction_<propan-1-ol>": "0.5953",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "836.9"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mole_fraction_<propan-1-ol>": "0.6995",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "825.6"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "mole_fraction_<propan-1-ol>": "0.7969",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "816.3"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "mole_fraction_<propan-1-ol>": "0.8983",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "807.7"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "mole_fraction_<propan-1-ol>": "0.9518",
          "pressure_kpa": "101.0",
          "temperature_k": "298.15",
          "mass_density_kg_m3": "803.5"
        }
      ],
      "inspection_id": "INSP_1e0dec3ca0e3",
      "lit_num_id": "GLOBlit_11042"
    }
  ]
}