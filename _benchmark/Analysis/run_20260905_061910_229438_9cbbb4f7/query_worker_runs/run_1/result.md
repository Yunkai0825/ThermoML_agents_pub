{
  "answer": "## Density Data for Binary Propan-2-ol + Water Mixtures\n\n### Best Dataset: GLOBlit_11142 (DOI: 10.1021/je800158z)\n\n**Block: PROPblock_4** — 56 data points of mass density (kg/m³) for the binary system propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1) in the liquid phase.\n\n- **Composition range:** x(propan-2-ol) = 0 to 1 (the inspected RDP subset shows compositions at 0, 0.0399, 0.1197, 0.2017, 0.28, 0.359, 0.4384, 0.5204, 0.5995, 0.6801, 0.7552, 0.8403, 0.9225, and 1)\n- **Temperature range:** 293.15–323.15 K (isotherms at 10 K intervals)\n- **Pressure:** 81.5 kPa (fixed constraint)\n- **Variables:** mole fraction of propan-2-ol (BLKvar_1 → GLOBvar_2), temperature (BLKvar_2 → GLOBvar_1)\n- **Density range:** 758.68–998.2 kg/m³\n\nThis is the richest dataset with excellent composition coverage across the full mole fraction range and multiple isotherms. Representative data points (verbatim from inspection):\n\n| x(propan-2-ol) | T (K) | ρ (kg/m³) |\n|---|---|---|\n| 0 | 293.15 | 998.2 |\n| 0 | 323.15 | 988.03 |\n| 0.2017 | 293.15 | 916.63 |\n| 0.2017 | 323.15 | 891.98 |\n| 0.5204 | 293.15 | 839.36 |\n| 0.5204 | 323.15 | 812.2 |\n| 1 | 293.15 | 785.1 |\n| 1 | 323.15 | 758.68 |\n\nThe density decreases monotonically with increasing propan-2-ol mole fraction at each temperature, reflecting the lower density of propan-2-ol compared to water. The temperature effect is also systematic: density decreases with increasing temperature at every composition.\n\n### Other Available Blocks (not individually inspected in this run)\n\nThe search found 12 total binary density blocks for this system. Additional candidates identified in the search include:\n\n| Literature | DOI | Notes |\n|---|---|---|\n| GLOBlit_11872 | 10.1021/je900966r | Multiple temperatures and compositions; not inspected — point count not verified |\n| GLOBlit_7474 | 10.1021/acs.jced.8b00160 | Multiple temperatures and compositions; not inspected — point count not verified |\n| GLOBlit_5585 | 10.1016/j.jct.2019.105880 | Multiple temperatures and compositions; not inspected — point count not verified |\n\nThe search also identified additional large datasets that appear to be high-pressure studies at fixed composition, making them less suitable for composition-dependent analysis at ambient conditions. These were not individually inspected.\n\n**Recommendation:** GLOBlit_11142, PROPblock_4 provides the best combination of composition coverage (spanning x = 0–1 with 56 data points across multiple compositions) and temperature variation (293.15 to 323.15 K), making it ideal for studying the composition and temperature dependence of density in propan-2-ol + water binary mixtures.",
  "core_claims": [
    "The richest identified density dataset for binary propan-2-ol + water mixtures is GLOBlit_11142 (DOI: 10.1021/je800158z), PROPblock_4, containing 56 data points of liquid-phase mass density spanning x(propan-2-ol) = 0 to 1, temperatures 293.15–323.15 K, and a fixed pressure of 81.5 kPa, with densities ranging from 758.68 to 998.2 kg/m³.",
    "Within this dataset, density decreases monotonically with increasing propan-2-ol mole fraction at each temperature and decreases with increasing temperature at every composition.",
    "Twelve total binary density blocks for propan-2-ol + water were found in the search, but only PROPblock_4 of GLOBlit_11142 was fully inspected; the remaining candidates were not individually verified for point count or suitability."
  ],
  "status": "success",
  "summary": "The best density dataset for binary propan-2-ol + water mixtures is GLOBlit_11142 (DOI: 10.1021/je800158z), PROPblock_4, containing 56 data points of mass density (kg/m³) in the liquid phase. It covers the full mole fraction range x(propan-2-ol) = 0 to 1 (14 compositions including 0, 0.0399, 0.1197, 0.2017, 0.28, 0.359, 0.4384, 0.5204, 0.5995, 0.6801, 0.7552, 0.8403, 0.9225, and 1), temperatures 293.15–323.15 K at 10 K intervals, and a fixed pressure of 81.5 kPa. Density ranges from 758.68 to 998.2 kg/m³, decreasing monotonically with increasing propan-2-ol mole fraction and with increasing temperature. Components are propan-2-ol (GLOBcomp_6) and water (GLOBcomp_1). Twelve total binary density blocks were found for this system; other candidates from GLOBlit_11872 (10.1021/je900966r), GLOBlit_7474 (10.1021/acs.jced.8b00160), and GLOBlit_5585 (10.1016/j.jct.2019.105880) were not individually inspected.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_6",
      "registry_id": "propan-2-ol",
      "name": "propan-2-ol"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_1",
      "registry_id": "mass_density_kg_m3",
      "name": "Mass density, kg/m3"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBvar_1",
      "registry_id": "temperature_k",
      "name": "Temperature, K"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBvar_2",
      "registry_id": "mole_fraction_{DOIcomp_id}",
      "name": "Mole fraction"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_11142",
      "registry_id": "2008-zar-sha-0",
      "name": "10.1021/je800158z"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_11142",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_6",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density measurements for binary propan-2-ol + water mixtures; 56 data points spanning x(propan-2-ol) = 0 to 1 at temperatures 293.15–323.15 K and 81.5 kPa.",
      "doi": "10.1021/je800158z",
      "lit_id": "2008-zar-sha-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 56,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_6",
          "name": "propan-2-ol",
          "formula": "C3H8O",
          "inchi_key": "KFZMGEQAYNKOFK-UHFFFAOYSA-N",
          "SMILES": "CC(C)O",
          "sample_num": "DOIcompSample_2_1"
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
          "value": 81.5,
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
            "BLKvar_id": "BLKvar_1",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 14
          },
          "range_min": 0.0,
          "range_max": 1.0
        },
        {
          "BLKvar_id": "BLKvar_2",
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
            "BLKvar_id": "BLKvar_2",
            "name": "Temperature, K",
            "min": 293.15,
            "max": 323.15,
            "n_unique": 4
          },
          "range_min": 293.15,
          "range_max": 323.15
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
            "min": 758.68,
            "max": 998.2,
            "mean": 854.478036,
            "std": 71.696509,
            "n": 56
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 758.68,
          "range_max": 998.2
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
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_6",
          "name": "propan-2-ol",
          "formula": "C3H8O",
          "inchi_key": "KFZMGEQAYNKOFK-UHFFFAOYSA-N",
          "SMILES": "CC(C)O",
          "sample_num": "DOIcompSample_2_1"
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
      "parent_n_datapoints": 56,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1021/je800158z",
      "block_number": "PROPblock_1",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "803.59"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "303.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "795.53"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "313.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "787.38"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "778.92"
        }
      ],
      "inspection_id": "INSP_14b56cf093c6",
      "lit_num_id": "GLOBlit_11142"
    },
    {
      "doi": "10.1021/je800158z",
      "block_number": "PROPblock_4",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<propan-2-ol>",
        "temperature_k",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<propan-2-ol>": "0",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "998.2"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mole_fraction_<propan-2-ol>": "0",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "988.03"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "mole_fraction_<propan-2-ol>": "0.0399",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "979.61"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mole_fraction_<propan-2-ol>": "0.0399",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "966.2"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mole_fraction_<propan-2-ol>": "0.1197",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "948.88"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "mole_fraction_<propan-2-ol>": "0.1197",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "926.48"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "mole_fraction_<propan-2-ol>": "0.2017",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "916.63"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "mole_fraction_<propan-2-ol>": "0.2017",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "891.98"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "mole_fraction_<propan-2-ol>": "0.28",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "891.87"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "mole_fraction_<propan-2-ol>": "0.28",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "866.23"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "mole_fraction_<propan-2-ol>": "0.359",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "871.15"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "mole_fraction_<propan-2-ol>": "0.359",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "844.85"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "mole_fraction_<propan-2-ol>": "0.4384",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "854.11"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "mole_fraction_<propan-2-ol>": "0.4384",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "827.31"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "mole_fraction_<propan-2-ol>": "0.5204",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "839.36"
        },
        {
          "BLKpoint_id": "BLKpoint_32",
          "mole_fraction_<propan-2-ol>": "0.5204",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "812.2"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "mole_fraction_<propan-2-ol>": "0.5995",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "827.56"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "mole_fraction_<propan-2-ol>": "0.5995",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "800.16"
        },
        {
          "BLKpoint_id": "BLKpoint_37",
          "mole_fraction_<propan-2-ol>": "0.6801",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "817.14"
        },
        {
          "BLKpoint_id": "BLKpoint_40",
          "mole_fraction_<propan-2-ol>": "0.6801",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "789.6"
        },
        {
          "BLKpoint_id": "BLKpoint_41",
          "mole_fraction_<propan-2-ol>": "0.7552",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "808.56"
        },
        {
          "BLKpoint_id": "BLKpoint_44",
          "mole_fraction_<propan-2-ol>": "0.7552",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "780.98"
        },
        {
          "BLKpoint_id": "BLKpoint_45",
          "mole_fraction_<propan-2-ol>": "0.8403",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "799.95"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "mole_fraction_<propan-2-ol>": "0.8403",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "772.47"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "mole_fraction_<propan-2-ol>": "0.9225",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "792.03"
        },
        {
          "BLKpoint_id": "BLKpoint_52",
          "mole_fraction_<propan-2-ol>": "0.9225",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "764.97"
        },
        {
          "BLKpoint_id": "BLKpoint_53",
          "mole_fraction_<propan-2-ol>": "1",
          "temperature_k": "293.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "785.1"
        },
        {
          "BLKpoint_id": "BLKpoint_56",
          "mole_fraction_<propan-2-ol>": "1",
          "temperature_k": "323.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "758.68"
        }
      ],
      "inspection_id": "INSP_e041177281fc",
      "lit_num_id": "GLOBlit_11142"
    }
  ]
}