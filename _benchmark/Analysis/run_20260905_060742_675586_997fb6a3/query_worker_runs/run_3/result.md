{
  "answer": "## Binary Density Data: DMF + Methanol at 298.15 K\n\n**Source:** DOI 10.1016/j.jct.2014.02.021 (GLOBlit_4125), PROPblock_6  \n**System:** Binary — methanol (GLOBcomp_4) + dimethylformamide (GLOBcomp_18)  \n**Conditions:** T = 298.15 K (fixed), P = 101.0 kPa (fixed), liquid phase  \n**Total data points:** 26 across the full composition range x(DMF) = 0–1\n\n### Representative Data Points (9 of 26, shape-preserving RDP subset)\n\n| x(DMF) | ρ / kg·m⁻³ |\n|--------|------------|\n| 0      | 786.58     |\n| 0.1988 | 843.761    |\n| 0.2004 | 843.0      |\n| 0.4022 | 882.138    |\n| 0.4054 | 881.38     |\n| 0.5982 | 909.277    |\n| 0.6008 | 908.588    |\n| 0.9033 | 936.655    |\n| 1.0    | 943.974    |\n\n**Statistics (full 26-point block):**  \n- x(DMF): 0–1  \n- ρ: 786.58–943.974 kg/m³\n\n**Chemistry insight:** The density increases monotonically from pure methanol (786.58 kg/m³) to pure DMF (943.974 kg/m³) at 298.15 K. The block includes duplicate/near-duplicate compositions (e.g., x ≈ 0.20, x ≈ 0.40, x ≈ 0.60), likely from replicate measurements, showing good reproducibility (differences < 1 kg/m³). The full block contains 26 points providing dense coverage of the composition range.\n\nA second block (PROPblock_8, GLOBlit_10930) also contains DMF + methanol density data over multiple temperatures, if additional data are needed (not inspected in this run).",
  "core_claims": [
    "For the binary system dimethylformamide (DMF) + methanol at 298.15 K and 101.0 kPa (liquid phase), 26 density data points spanning the full composition range x(DMF) = 0–1 are available from DOI 10.1016/j.jct.2014.02.021.",
    "The density increases monotonically from pure methanol (786.58 kg·m⁻³) to pure DMF (943.974 kg·m⁻³) at 298.15 K.",
    "Near-duplicate compositions (e.g., x(DMF) ≈ 0.20, ≈ 0.40, ≈ 0.60) from replicate measurements show good reproducibility, with density differences less than 1 kg·m⁻³."
  ],
  "status": "success",
  "summary": "Binary liquid density data for dimethylformamide (DMF) + methanol at 298.15 K and 101.0 kPa, from DOI 10.1016/j.jct.2014.02.021. The dataset contains 26 points spanning the full composition range x(DMF) = 0–1. Density increases monotonically from 786.58 kg/m³ (pure methanol) to 943.974 kg/m³ (pure DMF). Nine representative points are given: x(DMF) = 0, ρ = 786.58; x = 0.1988, ρ = 843.761; x = 0.2004, ρ = 843.0; x = 0.4022, ρ = 882.138; x = 0.4054, ρ = 881.38; x = 0.5982, ρ = 909.277; x = 0.6008, ρ = 908.588; x = 0.9033, ρ = 936.655; x = 1.0, ρ = 943.974 (all ρ in kg·m⁻³). Near-duplicate compositions (e.g., x ≈ 0.20, 0.40, 0.60) from replicate measurements show differences < 1 kg/m³, indicating good reproducibility. A second data block from a different literature source covering multiple temperatures was noted but not inspected.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_4125",
      "block_number": "PROPblock_6",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_18"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density measurements for methanol + dimethylformamide at 298.15 K and 101.0 kPa across the full composition range (26 data points, x(DMF) = 0–1).",
      "doi": "10.1016/j.jct.2014.02.021",
      "lit_id": "2014-pie-pie-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 26,
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_4_1"
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
          "var_id": "mole_fraction_DOIcomp_4",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_4",
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
            "n_unique": 25
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
            "min": 786.58,
            "max": 943.974,
            "mean": 876.195885,
            "std": 51.164012,
            "n": 26
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 786.58,
          "range_max": 943.974
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "parent_n_datapoints": 26,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2014.02.021",
      "block_number": "PROPblock_6",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<dimethylformamide>",
        "temperature_k",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<dimethylformamide>": "0",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "786.58"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "mole_fraction_<dimethylformamide>": "0.5982",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "909.277"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "mole_fraction_<dimethylformamide>": "1",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "943.974"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "mole_fraction_<dimethylformamide>": "0.1988",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "843.761"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "mole_fraction_<dimethylformamide>": "0.4022",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "882.138"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "mole_fraction_<dimethylformamide>": "0.6008",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "908.588"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "mole_fraction_<dimethylformamide>": "0.2004",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "843"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "mole_fraction_<dimethylformamide>": "0.4054",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "881.38"
        },
        {
          "BLKpoint_id": "BLKpoint_26",
          "mole_fraction_<dimethylformamide>": "0.9033",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "936.655"
        }
      ],
      "inspection_id": "INSP_428715c8042d",
      "lit_num_id": "GLOBlit_4125"
    }
  ]
}