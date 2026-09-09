{
  "answer": "## Density Data for Acetone + Water Binary Mixture at 298.15 K\n\nThree binary acetone–water density blocks were found in the ThermoML database via the search_blocks discovery tool.\n\n### Available Data Blocks\n\n**PROPblock_8** (GLOBlit_5679, DOI: 10.1016/j.tca.2006.01.008) — 22 data points at exactly 298.15 K, x(acetone) from 0.0502 to 0.9451, at 101.0 kPa. *(Inspected and fully grounded below.)*\n\n**PROPblock_5** (GLOBlit_8129, DOI: 10.1021/je030102f) — Additional density data covering a wider temperature range and partial composition range. *(Not inspected in this run; no numerical details quoted.)*\n\n**PROPblock_6** (GLOBlit_10721, DOI: 10.1021/je7000182) — Additional density data covering the full composition range at multiple temperatures. *(Not inspected in this run; no numerical details quoted.)*\n\n### Inspected Density Data at 298.15 K (PROPblock_8, GLOBlit_5679)\n\nThis block provides an isothermal dataset at exactly 298.15 K and 101.0 kPa, spanning nearly the full composition range (22 data points total). A shape-preserving subset:\n\n| x(acetone) | ρ (kg/m³) |\n|---|---|\n| 0.0502 | 977 |\n| 0.2496 | 911.8 |\n| 0.3507 | 884.8 |\n| 0.4509 | 862.1 |\n| 0.5489 | 843.5 |\n| 0.6506 | 827 |\n| 0.8011 | 806.2 |\n| 0.8015 | 806.3 |\n| 0.9451 | 789.9 |\n\n**Property:** Mass density (GLOBprop_1), in kg/m³.\n**Compounds:** Acetone (GLOBcomp_9) + Water (GLOBcomp_1).\n**Full stats (n = 22):** x(acetone) from 0.0502 to 0.9451; density from 789.9 to 977 kg/m³.\n\n**Chemical insight:** The density decreases with increasing acetone mole fraction at 298.15 K, from near-pure water (~977 kg/m³ at x = 0.0502) toward near-pure acetone (~789.9 kg/m³ at x = 0.9451). The inspection topology notes a non-monotonic character with 2 extrema across all 22 points, suggesting subtle density anomalies — consistent with the known strong hydrogen-bonding interactions and excess volume effects in the acetone–water system.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNINSPECTED_BLOCK** PROPblock_6: PROPblock_6 is quoted with data values (298.15, …) but was never inspected in this run\n  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_6\", literature=\"<GLOBlit_N or DOI>\")`\nInspected so far: PROPblock_8",
  "core_claims": [
    "At 298.15 K and 101.0 kPa, the density of the acetone–water binary mixture decreases with increasing acetone mole fraction, from ~977 kg/m³ at x(acetone) = 0.0502 to ~789.9 kg/m³ at x(acetone) = 0.9451, based on 22 data points from PROPblock_8 (DOI: 10.1016/j.tca.2006.01.008).",
    "The full 22-point dataset exhibits non-monotonic character with 2 extrema, consistent with known strong hydrogen-bonding interactions and excess volume effects in the acetone–water system.",
    "Two additional density data blocks (PROPblock_5 and PROPblock_6) were identified but not inspected; no numerical details from those blocks are verified."
  ],
  "status": "success",
  "summary": "Density data for the binary mixture acetone (GLOBcomp_9) + water (GLOBcomp_1) at 298.15 K were identified in three ThermoML blocks (PROPblock_8, PROPblock_5, PROPblock_6). Only PROPblock_8 (GLOBlit_5679, DOI: 10.1016/j.tca.2006.01.008) was inspected. It contains 22 mass-density (GLOBprop_1) data points at exactly 298.15 K and 101.0 kPa, with x(acetone) ranging from 0.0502 to 0.9451 and density from 789.9 to 977 kg/m³. Representative values include 977 kg/m³ at x = 0.0502, 911.8 at 0.2496, 884.8 at 0.3507, 862.1 at 0.4509, 843.5 at 0.5489, 827 at 0.6506, 806.2 at 0.8011, 806.3 at 0.8015, and 789.9 at 0.9451. Density decreases with increasing acetone mole fraction; the full 22-point dataset shows 2 extrema, consistent with known excess-volume anomalies from strong hydrogen-bonding interactions in this system. PROPblock_5 (GLOBlit_8129) and PROPblock_6 (GLOBlit_10721) were not inspected and no numerical details from them are verified.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_5679",
      "block_number": "PROPblock_8",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_9",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density data for acetone + water at 298.15 K and 101.0 kPa, 22 data points, x(acetone) from 0.0502 to 0.9451, density from 789.9 to 977 kg/m³.",
      "doi": "10.1016/j.tca.2006.01.008",
      "lit_id": "2006-aco-rod-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 22,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_9",
          "name": "acetone",
          "formula": "C3H6O",
          "inchi_key": "CSCPPACGZOOCGX-UHFFFAOYSA-N",
          "SMILES": "CC(C)=O",
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
            "min": 0.0502,
            "max": 0.9451,
            "n_unique": 22
          },
          "range_min": 0.0502,
          "range_max": 0.9451
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
            "min": 789.9,
            "max": 977.0,
            "mean": 856.272727,
            "std": 57.529944,
            "n": 22
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 789.9,
          "range_max": 977.0
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
          "comp_num_id": "GLOBcomp_9",
          "name": "acetone",
          "formula": "C3H6O",
          "inchi_key": "CSCPPACGZOOCGX-UHFFFAOYSA-N",
          "SMILES": "CC(C)=O",
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
      "parent_n_datapoints": 22,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8129",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_9",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Density data for acetone + water covering a wider temperature range and partial composition range. Not inspected in this run.",
      "doi": "10.1021/je030102f",
      "lit_id": "2003-est-del-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 99,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_9",
          "name": "acetone",
          "formula": "C3H6O",
          "inchi_key": "CSCPPACGZOOCGX-UHFFFAOYSA-N",
          "SMILES": "CC(C)=O",
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
          "value": 101.325,
          "digits": 6,
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
            "n_unique": 11
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
            "min": 283.15,
            "max": 323.148,
            "n_unique": 30
          },
          "range_min": 283.15,
          "range_max": 323.148
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
          "meas_num_id": "GLOBmeas_258",
          "meas_ID": "vibtub_mpoint",
          "method_standard": null,
          "method_custom": "VIBTUB:mpoint",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 755.314,
            "max": 999.691,
            "mean": 862.868535,
            "std": 68.379315,
            "n": 99
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 755.314,
          "range_max": 999.691
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
          "comp_num_id": "GLOBcomp_9",
          "name": "acetone",
          "formula": "C3H6O",
          "inchi_key": "CSCPPACGZOOCGX-UHFFFAOYSA-N",
          "SMILES": "CC(C)=O",
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
      "parent_n_datapoints": 99,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10721",
      "block_number": "PROPblock_6",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_9",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Density data for acetone + water covering the full composition range at multiple temperatures. Not inspected in this run.",
      "doi": "10.1021/je7000182",
      "lit_id": "2007-end-kah-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 126,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_9",
          "name": "acetone",
          "formula": "C3H6O",
          "inchi_key": "CSCPPACGZOOCGX-UHFFFAOYSA-N",
          "SMILES": "CC(C)=O",
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
            "min": 288.15,
            "max": 328.15,
            "n_unique": 9
          },
          "range_min": 288.15,
          "range_max": 328.15
        },
        {
          "BLKvar_id": "BLKvar_2",
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
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 14
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
          "meas_num_id": "GLOBmeas_203",
          "meas_ID": "vibtub_ufactor_3",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:3",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 748.98,
            "max": 999.12,
            "mean": 881.33381,
            "std": 77.272888,
            "n": 126
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 748.98,
          "range_max": 999.12
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
          "comp_num_id": "GLOBcomp_9",
          "name": "acetone",
          "formula": "C3H6O",
          "inchi_key": "CSCPPACGZOOCGX-UHFFFAOYSA-N",
          "SMILES": "CC(C)=O",
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
      "parent_n_datapoints": 126,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.tca.2006.01.008",
      "block_number": "PROPblock_8",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<acetone>",
        "temperature_k",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<acetone>": "0.0502",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "977"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "mole_fraction_<acetone>": "0.2496",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "911.8"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "mole_fraction_<acetone>": "0.3507",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "884.8"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mole_fraction_<acetone>": "0.4509",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "862.1"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "mole_fraction_<acetone>": "0.5489",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "843.5"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "mole_fraction_<acetone>": "0.6506",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "827"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "mole_fraction_<acetone>": "0.8011",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "806.2"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "mole_fraction_<acetone>": "0.8015",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "806.3"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "mole_fraction_<acetone>": "0.9451",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "789.9"
        }
      ],
      "inspection_id": "INSP_62e1df49db96",
      "lit_num_id": "GLOBlit_5679"
    }
  ]
}