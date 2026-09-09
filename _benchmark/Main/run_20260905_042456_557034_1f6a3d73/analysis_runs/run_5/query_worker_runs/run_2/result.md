{
  "answer": "## Density Data for Methanol + Water Binary Mixture at 298.15 K\n\n### Best Dataset: Full Composition Coverage\n\n**Source:** DOI 10.1016/j.jct.2007.05.004 (GLOBlit_2825, PROPblock_10)\n\nThis block contains 13 data points at exactly 298.15 K and 101.0 kPa, spanning the full mole fraction range of water from 0 (pure methanol) to 1 (pure water). The composition variable is mole fraction of water (BLKvar_2).\n\n| Mole fraction water | Mass density (kg/m³) |\n|---|---|\n| 0 | 787.2 |\n| 0.049 | 795.47 |\n| 0.0993 | 804.11 |\n| 0.1973 | 821.73 |\n| 0.2983 | 840.79 |\n| 0.3985 | 860.59 |\n| 0.5003 | 881.69 |\n| 0.5994 | 902.96 |\n| 0.6997 | 925.21 |\n| 0.7986 | 947.17 |\n| 0.8999 | 969.84 |\n| 0.9512 | 982.53 |\n| 1 | 997.05 |\n\n(All 13 matched rows at 298.15 K shown.)\n\n### Additional Datasets Available\n\nSeveral other blocks also contain methanol + water density data with temperature ranges that may include 298.15 K. These were identified in the registry search but their individual data rows were not inspected in this run, so no specific numerical details are quoted for them:\n\n- DOI 10.1021/je049691v (GLOBlit_8424, PROPblock_3) — multi-temperature dataset with broad composition coverage\n- DOI 10.1021/je034101z (GLOBlit_8254, PROPblock_4) — multi-temperature, variable-pressure dataset\n- DOI 10.1021/acs.jced.6b01058 (GLOBlit_7085, PROPblock_6) — narrow mass fraction range\n- DOI 10.1016/j.jct.2004.07.019 (GLOBlit_2432, PROPblock_1) — relative density, variable pressure\n\n### Compound IDs\n- **Methanol:** GLOBcomp_4 (CH₄O, CAS 67-56-1)\n- **Water:** GLOBcomp_1 (H₂O, CAS 7732-18-5)\n- **Property:** Mass density (GLOBprop_1, kg/m³)\n\n### Chemistry Note\nThe GLOBlit_2825 dataset is ideal for deriving excess molar volume (V^E) at 298.15 K because it covers the complete composition range at constant atmospheric pressure. The density increases monotonically from 787.2 kg/m³ (pure methanol) to 997.05 kg/m³ (pure water). The methanol–water system is well known for exhibiting negative excess molar volumes across the entire composition range, reflecting strong hydrogen-bonding interactions and efficient molecular packing between the two components. The non-linear density–composition relationship visible in these data (the density does not follow a simple linear mixing rule) is the signature of this non-ideal volumetric behavior.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNINSPECTED_BLOCK** PROPblock_1: PROPblock_1 is quoted with data values (67, 7732, 298.15, 787.2, …) but was never inspected in this run\n  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_1\", literature=\"<GLOBlit_N or DOI>\")`\nInspected so far: PROPblock_10",
  "core_claims": [
    "At 298.15 K and 101.0 kPa, the mass density of the methanol + water binary mixture increases monotonically from 787.2 kg/m³ (pure methanol, mole fraction water = 0) to 997.05 kg/m³ (pure water, mole fraction water = 1), based on 13 data points spanning the full composition range from DOI 10.1016/j.jct.2007.05.004.",
    "The density–composition relationship is non-linear, indicating non-ideal volumetric mixing behavior consistent with the known negative excess molar volumes of the methanol–water system attributed to strong hydrogen-bonding interactions.",
    "Several additional datasets from other sources may contain methanol + water density data at 298.15 K, but their individual data rows were not inspected and no numerical values are quoted for them."
  ],
  "status": "success",
  "summary": "Density data for the methanol (GLOBcomp_4, CAS 67-56-1) + water (GLOBcomp_1, CAS 7732-18-5) binary mixture at 298.15 K and 101.0 kPa are reported from DOI 10.1016/j.jct.2007.05.004 (GLOBlit_2825, PROPblock_10). The dataset contains 13 mass density (GLOBprop_1, kg/m³) values spanning the full mole fraction range of water: 0 (787.2), 0.049 (795.47), 0.0993 (804.11), 0.1973 (821.73), 0.2983 (840.79), 0.3985 (860.59), 0.5003 (881.69), 0.5994 (902.96), 0.6997 (925.21), 0.7986 (947.17), 0.8999 (969.84), 0.9512 (982.53), and 1 (997.05). Density increases monotonically from pure methanol to pure water. The non-linear density–composition relationship reflects the well-known negative excess molar volumes arising from strong hydrogen-bonding interactions. Additional datasets potentially containing 298.15 K data were identified but not numerically inspected: DOI 10.1021/je049691v (GLOBlit_8424, PROPblock_3), DOI 10.1021/je034101z (GLOBlit_8254, PROPblock_4), DOI 10.1021/acs.jced.6b01058 (GLOBlit_7085, PROPblock_6), and DOI 10.1016/j.jct.2004.07.019 (GLOBlit_2432, PROPblock_1).",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_4",
      "registry_id": "methanol",
      "name": "methanol"
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
      "core_GLOB_id": "GLOBlit_2825",
      "registry_id": "2007-gon-cal-1",
      "name": "10.1016/j.jct.2007.05.004"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_8424",
      "registry_id": "2005-coq-val-0",
      "name": "10.1021/je049691v"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_8254",
      "registry_id": "2003-kit-kag-0",
      "name": "10.1021/je034101z"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_7085",
      "registry_id": "2017-sha-cha-0",
      "name": "10.1021/acs.jced.6b01058"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_2432",
      "registry_id": "2004-hyn-hne-0",
      "name": "10.1016/j.jct.2004.07.019"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2825",
      "block_number": "PROPblock_10",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of methanol + water at 298.15 K and 101.0 kPa across full mole fraction range, 13 data points.",
      "doi": "10.1016/j.jct.2007.05.004",
      "lit_id": "2007-gon-cal-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 39,
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
            "max": 303.15,
            "n_unique": 3
          },
          "range_min": 293.15,
          "range_max": 303.15
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
            "min": 782.48,
            "max": 998.2,
            "mean": 885.828974,
            "std": 72.087348,
            "n": 39
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 782.48,
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
      "parent_n_datapoints": 39,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8424",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of methanol + water, multi-temperature dataset with broad composition coverage.",
      "doi": "10.1021/je049691v",
      "lit_id": "2005-coq-val-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 180,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_3_1"
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
            "min": 283.15,
            "max": 353.15,
            "n_unique": 15
          },
          "range_min": 283.15,
          "range_max": 353.15
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
            "min": 0.08,
            "max": 0.9603,
            "n_unique": 12
          },
          "range_min": 0.08,
          "range_max": 0.9603
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
          "meas_num_id": "GLOBmeas_138",
          "meas_ID": "vibtub_ufactor_2",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:2",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 747.01,
            "max": 988.05,
            "mean": 872.453667,
            "std": 63.746274,
            "n": 180
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 747.01,
          "range_max": 988.05
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
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 180,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8254",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of methanol + water, multi-temperature variable-pressure dataset.",
      "doi": "10.1021/je034101z",
      "lit_id": "2003-kit-kag-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 401,
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
            "min": 0.059,
            "max": 0.708,
            "n_unique": 4
          },
          "range_min": 0.059,
          "range_max": 0.708
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
            "min": 287.15,
            "max": 417.15,
            "n_unique": 131
          },
          "range_min": 287.15,
          "range_max": 417.15
        },
        {
          "BLKvar_id": "BLKvar_3",
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
            "BLKvar_id": "BLKvar_3",
            "name": "Pressure, kPa",
            "min": 3721.0,
            "max": 29927.0,
            "n_unique": 396
          },
          "range_min": 3721.0,
          "range_max": 29927.0
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
          "meas_num_id": "GLOBmeas_170",
          "meas_ID": "isochor",
          "method_standard": null,
          "method_custom": "ISOCHOR",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 762.2,
            "max": 966.0,
            "mean": 864.876808,
            "std": 56.871822,
            "n": 401
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 762.2,
          "range_max": 966.0
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
      "parent_n_datapoints": 401,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_7085",
      "block_number": "PROPblock_6",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of methanol + water, narrow mass fraction range.",
      "doi": "10.1021/acs.jced.6b01058",
      "lit_id": "2017-sha-cha-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 12,
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
          "value": 85.0,
          "digits": 2,
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
            "max": 313.15,
            "n_unique": 4
          },
          "range_min": 298.15,
          "range_max": 313.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_2",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mass fraction",
            "min": 0.04,
            "max": 0.16,
            "n_unique": 3
          },
          "range_min": 0.04,
          "range_max": 0.16
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
            "min": 963.68,
            "max": 989.97,
            "mean": 978.324167,
            "std": 9.346563,
            "n": 12
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 963.68,
          "range_max": 989.97
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
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_2_1"
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
      "parent_n_datapoints": 12,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2432",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Relative density of methanol + water, variable pressure.",
      "doi": "10.1016/j.jct.2004.07.019",
      "lit_id": "2004-hyn-hne-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 596,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "solvents": [
        {
          "component_org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "solvent_num_id": "GLOBsolvent_1",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N"
        }
      ],
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
            "min": 298.16,
            "max": 573.15,
            "n_unique": 16
          },
          "range_min": 298.16,
          "range_max": 573.15
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
            "min": 390.0,
            "max": 30320.0,
            "n_unique": 32
          },
          "range_min": 390.0,
          "range_max": 30320.0
        },
        {
          "BLKvar_id": "BLKvar_3",
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_5",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_5",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_3",
            "name": "Molality, mol/kg",
            "min": 0.07706,
            "max": 1.04694,
            "n_unique": 161
          },
          "range_min": 0.07706,
          "range_max": 1.04694
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
            "min": -13.3065,
            "max": -0.4632,
            "mean": -3.693235,
            "std": 2.632762,
            "n": 596
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -13.3065,
          "range_max": -0.4632
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
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "parent_n_datapoints": 596,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "block_number": "PROPblock_10",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<water>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "787.2"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.049",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "795.47"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.0993",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "804.11"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.1973",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "821.73"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.2983",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "840.79"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.3985",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "860.59"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.5003",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "881.69"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.5994",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "902.96"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.7986",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "947.17"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.8999",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "969.84"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.9512",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "982.53"
        },
        {
          "BLKpoint_id": "BLKpoint_26",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "997.05"
        }
      ],
      "inspection_id": "INSP_5d31e929df24",
      "lit_num_id": "GLOBlit_2825"
    },
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "block_number": "PROPblock_10",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<water>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.6997",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "928.45"
        }
      ],
      "inspection_id": "INSP_41f65b5c2ff4",
      "lit_num_id": "GLOBlit_2825"
    },
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "block_number": "PROPblock_10",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<water>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.6997",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "925.21"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.7986",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "947.17"
        }
      ],
      "inspection_id": "INSP_924974a9f3ca",
      "lit_num_id": "GLOBlit_2825"
    }
  ]
}