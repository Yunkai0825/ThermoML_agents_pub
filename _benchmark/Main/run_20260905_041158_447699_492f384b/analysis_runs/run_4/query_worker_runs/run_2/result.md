{
  "answer": "## Density Data for Binary Water + 1-Propanol at 298.15 K\n\nA comprehensive density dataset suitable for deriving excess molar volume (V^E) was found in the ThermoML database for the binary system **water + 1-propanol**.\n\n### Primary Dataset\n\n**Source:** DOI 10.1021/je700700f (GLOBlit_11042), Block PROPblock_14\n\n- **System:** Binary mixture of water (GLOBcomp_1) + propan-1-ol (GLOBcomp_5)\n- **Property:** Mass density (kg/m³)\n- **Temperature:** 298.15 K (isothermal)\n- **Pressure:** 101.0 kPa\n- **Total data points:** 13 across the full composition range (x₁-propanol = 0 to 1)\n- **Density range:** 799.6–997.2 kg/m³\n\nRepresentative data points (RDP subset, 8 of 13 points shown):\n\n| x(propan-1-ol) | ρ (kg/m³) |\n|---|---|\n| 0 | 997.2 |\n| 0.1986 | 914.9 |\n| 0.2979 | 887.2 |\n| 0.3949 | 866.9 |\n| 0.4955 | 850.3 |\n| 0.5953 | 836.9 |\n| 0.7969 | 816.3 |\n| 1 | 799.6 |\n\nThe density decreases monotonically with increasing propan-1-ol mole fraction, from pure water (997.2 kg/m³) to pure propan-1-ol (799.6 kg/m³). This block covers the full composition range including both pure-component endpoints, making it well-suited for calculating excess molar volumes V^E = V_mix − Σ xᵢVᵢ* at each composition, where the pure-component molar volumes Vᵢ* can be obtained directly from the endpoint densities.\n\n### Additional Sources\n\nMultiple additional mass density blocks were also found for this binary system near 298.15 K, providing opportunities for cross-validation. These additional blocks were not individually inspected in this run.",
  "core_claims": [
    "A comprehensive density dataset for the binary system water + 1-propanol at 298.15 K and 101.0 kPa was identified in ThermoML (DOI 10.1021/je700700f, Block PROPblock_14), containing 13 data points spanning the full composition range (x₁-propanol = 0 to 1) with densities ranging from 799.6–997.2 kg/m³.",
    "The density decreases monotonically with increasing propan-1-ol mole fraction, from pure water (997.2 kg/m³) to pure propan-1-ol (799.6 kg/m³).",
    "The dataset includes both pure-component endpoints, making it suitable for calculating excess molar volumes V^E at each composition."
  ],
  "status": "success",
  "summary": "Density data for the binary system water + 1-propanol at 298.15 K and 101.0 kPa were identified in the ThermoML database from DOI 10.1021/je700700f (GLOBlit_11042, Block PROPblock_14). The dataset contains 13 mass density measurements spanning the full composition range (x₁-propanol = 0 to 1), with density decreasing monotonically from 997.2 kg/m³ (pure water) to 799.6 kg/m³ (pure propan-1-ol). Representative values include 914.9 kg/m³ at x = 0.1986, 887.2 at 0.2979, 866.9 at 0.3949, 850.3 at 0.4955, 836.9 at 0.5953, and 816.3 at 0.7969. Both pure-component endpoints are included, making the block suitable for calculating excess molar volumes V^E at each composition. Additional mass density blocks for this binary system near 298.15 K exist in the database but were not individually inspected.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_5",
      "registry_id": "propan-1-ol",
      "name": "propan-1-ol"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_11042",
      "registry_id": "2008-gon-cal-0",
      "name": "10.1021/je700700f"
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
      "description": "Mass density (kg/m³) for binary water + propan-1-ol at 298.15 K, 101.0 kPa; 13 data points across full composition range (x₁-propanol = 0 to 1); density range 799.6–997.2 kg/m³.",
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
    }
  ]
}