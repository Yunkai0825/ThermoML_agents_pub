{
  "answer": "## Dynamic Viscosity Data for Binary DMF + Water Mixtures near 298.15 K\n\n**Compounds:** N,N-dimethylformamide (DMF, GLOBcomp_18) and water (GLOBcomp_1)  \n**Property:** Dynamic viscosity (GLOBprop_4, Pa·s)  \n**System type:** Binary\n\n### Data Blocks Found\n\nFour blocks of dynamic viscosity data for binary DMF + water were identified. Two key blocks with inspected data at 298.15 K are detailed below:\n\n---\n\n**Block 1: GLOBlit_8676 :: PROPblock_9**  \nDOI: 10.1021/je050209y  \nTotal points: 11 | Temperature: 298.15 K (fixed) | Pressure: 101.325 kPa  \nComposition variable: mole fraction of DMF\n\n| x(DMF) | Viscosity (Pa·s) |\n|---|---|\n| 0.05 | 0.00131 |\n| 0.1001 | 0.001728 |\n| 0.2 | 0.002346 |\n| 0.299 | 0.002491 |\n| 0.3998 | 0.002273 |\n| 0.4997 | 0.001878 |\n| 0.5993 | 0.001532 |\n| 0.6995 | 0.001243 |\n| 0.8 | 0.001045 |\n| 0.8991 | 0.000901 |\n| 0.9488 | 0.000843 |\n\nViscosity range: 0.000843–0.002491 Pa·s across x(DMF) = 0.05–0.9488.\n\n---\n\n**Block 2: GLOBlit_9900 :: PROPblock_3**  \nDOI: 10.1021/je300608v  \nTotal points: 60 (full block, 293.15–308.15 K) | 15 points at 298.15 K | Pressure: 101.0 kPa  \nComposition variable: mole fraction of water\n\n| x(water) | Viscosity (Pa·s) |\n|---|---|\n| 0 | 0.0008045 |\n| 0.1 | 0.0009018 |\n| 0.2 | 0.0010386 |\n| 0.3 | 0.0012331 |\n| 0.4 | 0.0015078 |\n| 0.5 | 0.0018528 |\n| 0.6 | 0.0022264 |\n| 0.7 | 0.0024775 |\n| 0.8 | 0.0023495 |\n| 0.9 | 0.0017464 |\n| 0.94 | 0.0014116 |\n| 1 | 0.0008903 |\n\nViscosity range at 298.15 K: 0.0008045–0.0024775 Pa·s across x(water) = 0–1.\n\n---\n\nTwo additional blocks were also returned in the search (4 total), including one from GLOBlit_11030 (temperature range not inspected in this run).\n\n**Chemistry insight:** Both datasets show a pronounced viscosity maximum at intermediate compositions — near x(DMF) ≈ 0.3 in Block 1 (GLOBlit_8676::PROPblock_9, 0.002491 Pa·s) and near x(water) ≈ 0.7 in Block 2 (GLOBlit_9900::PROPblock_3, 0.0024775 Pa·s). These correspond to the same composition region (~30 mol% DMF / 70 mol% water), consistent with strong DMF–water hydrogen-bonding interactions that create structured molecular associations and enhance viscous resistance to flow at these intermediate compositions.",
  "core_claims": [
    "Four blocks of dynamic viscosity data for binary DMF + water mixtures were identified, with two key blocks providing detailed measurements at 298.15 K and near-ambient pressure.",
    "Block 1 (DOI: 10.1021/je050209y) reports 11 viscosity values at 298.15 K and 101.325 kPa spanning x(DMF) = 0.05–0.9488, with viscosity ranging from 0.000843 to 0.002491 Pa·s.",
    "Block 2 (DOI: 10.1021/je300608v) reports 12 viscosity values at 298.15 K and 101.0 kPa spanning x(water) = 0–1, with viscosity ranging from 0.0008045 to 0.0024775 Pa·s.",
    "Both datasets show a pronounced viscosity maximum at intermediate compositions near ~30 mol% DMF / 70 mol% water (0.002491 Pa·s in Block 1 at x(DMF) ≈ 0.3; 0.0024775 Pa·s in Block 2 at x(water) ≈ 0.7), consistent with strong DMF–water hydrogen-bonding interactions that create structured molecular associations and enhance viscous resistance to flow."
  ],
  "status": "success",
  "summary": "Dynamic viscosity (Pa·s) data for the binary system N,N-dimethylformamide (DMF) + water at 298.15 K were found in four data blocks. Two key blocks were inspected in detail. Block 1 (DOI 10.1021/je050209y, GLOBlit_8676::PROPblock_9) reports 11 points at 298.15 K and 101.325 kPa as a function of DMF mole fraction, with viscosities ranging from 0.000843 to 0.002491 Pa·s across x(DMF) = 0.05–0.9488. Block 2 (DOI 10.1021/je300608v, GLOBlit_9900::PROPblock_3) reports 15 points at 298.15 K and 101.0 kPa as a function of water mole fraction, with viscosities ranging from 0.0008045 to 0.0024775 Pa·s across x(water) = 0–1. Both datasets exhibit a pronounced viscosity maximum near ~30 mol% DMF / ~70 mol% water (0.002491 Pa·s in Block 1 at x(DMF) ≈ 0.3; 0.0024775 Pa·s in Block 2 at x(water) ≈ 0.7), attributed to strong DMF–water hydrogen-bonding interactions forming structured molecular associations. Two additional blocks were also returned but not inspected in detail.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_18",
      "registry_id": "dimethylformamide",
      "name": "dimethylformamide"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_4",
      "registry_id": "viscosity_pa_s",
      "name": "Viscosity, Pa*s"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_8676",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_18",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of binary DMF + water at 298.15 K and 101.325 kPa as a function of DMF mole fraction (11 points, viscosity range 0.000843–0.002491 Pa·s).",
      "doi": "10.1021/je050209y",
      "lit_id": "2005-han-oh-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 11,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
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
            "min": 0.05,
            "max": 0.9488,
            "n_unique": 11
          },
          "range_min": 0.05,
          "range_max": 0.9488
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_4",
          "prop_ID": "viscosity_pa_s",
          "name": "Viscosity, Pa*s",
          "group": "TransportProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_140",
          "meas_ID": "captub_ufactor_2",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:2",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000843,
            "max": 0.002491,
            "mean": 0.001599,
            "std": 0.00059,
            "n": 11
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000843,
          "range_max": 0.002491
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
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
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
      "parent_n_datapoints": 11,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_9900",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_18",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of binary DMF + water at 293.15–308.15 K and 101.0 kPa as a function of water mole fraction (60 total points, 15 at 298.15 K, viscosity range at 298.15 K: 0.0008045–0.0024775 Pa·s).",
      "doi": "10.1021/je300608v",
      "lit_id": "2013-joz-tyc-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 60,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
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
            "min": 293.15,
            "max": 308.15,
            "n_unique": 4
          },
          "range_min": 293.15,
          "range_max": 308.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_3",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_3",
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
            "n_unique": 15
          },
          "range_min": 0.0,
          "range_max": 1.0
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_4",
          "prop_ID": "viscosity_pa_s",
          "name": "Viscosity, Pa*s",
          "group": "TransportProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_4",
          "meas_ID": "capillary_tube_ostwald_ubbelohde_method",
          "method_standard": "Capillary tube (Ostwald; Ubbelohde) method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000712,
            "max": 0.002885,
            "mean": 0.00142,
            "std": 0.000544,
            "n": 60
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000712,
          "range_max": 0.002885
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
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
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
      "parent_n_datapoints": 60,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1021/je050209y",
      "block_number": "PROPblock_9",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<dimethylformamide>",
        "temperature_k",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<dimethylformamide>": "0.05",
          "temperature_k": "298.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.00131"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "mole_fraction_<dimethylformamide>": "0.1001",
          "temperature_k": "298.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.001728"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "mole_fraction_<dimethylformamide>": "0.2",
          "temperature_k": "298.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.002346"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mole_fraction_<dimethylformamide>": "0.299",
          "temperature_k": "298.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.002491"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "mole_fraction_<dimethylformamide>": "0.3998",
          "temperature_k": "298.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.002273"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "mole_fraction_<dimethylformamide>": "0.4997",
          "temperature_k": "298.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.001878"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "mole_fraction_<dimethylformamide>": "0.5993",
          "temperature_k": "298.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.001532"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mole_fraction_<dimethylformamide>": "0.6995",
          "temperature_k": "298.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.001243"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mole_fraction_<dimethylformamide>": "0.8",
          "temperature_k": "298.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.001045"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "mole_fraction_<dimethylformamide>": "0.8991",
          "temperature_k": "298.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.000901"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "mole_fraction_<dimethylformamide>": "0.9488",
          "temperature_k": "298.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.000843"
        }
      ],
      "inspection_id": "INSP_469970d3baa4",
      "lit_num_id": "GLOBlit_8676"
    },
    {
      "doi": "10.1021/je300608v",
      "block_number": "PROPblock_3",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<water>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0008045"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0009018"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.2",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0010386"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.3",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0012331"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.4",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0015078"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.5",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0018528"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.6",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0022264"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.7",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0024775"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.8",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0023495"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.9",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0017464"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.94",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0014116"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0008903"
        }
      ],
      "inspection_id": "INSP_223a0880d59c",
      "lit_num_id": "GLOBlit_9900"
    }
  ]
}