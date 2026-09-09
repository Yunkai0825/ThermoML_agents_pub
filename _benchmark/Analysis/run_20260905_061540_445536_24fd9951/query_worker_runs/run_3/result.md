{
  "answer": "## Binary Water + Methanol Dynamic Viscosity Data Near 298.15 K\n\nA search of the ThermoML database for dynamic viscosity (GLOBprop_4) measurements in binary water (GLOBcomp_1) + methanol (GLOBcomp_4) systems in the temperature range 293–303 K returned **4 data blocks**.\n\n### Primary Dataset\n\n| DOI | Block | Literature ID | Data Points | T Range (K) | Composition Variable | Composition Range |\n|-----|-------|---------------|-------------|-------------|---------------------|-------------------|\n| 10.1016/j.jct.2007.05.004 | PROPblock_9 | GLOBlit_2825 | 39 | 293.15–303.15 | x(water) | 0–1 |\n\nThe most comprehensive dataset is **PROPblock_9** from GLOBlit_2825 (DOI: 10.1016/j.jct.2007.05.004), which contains 39 data points spanning the full composition range (mole fraction of water from 0 to 1) at three temperatures: 293.15, 298.15, and 303.15 K, all at a fixed pressure constraint of 101.0 kPa. The viscosity values range from 0.000508 to 0.001793 Pa·s across the block.\n\n#### Representative inspected data at 298.15 K\n\n| Mole fraction water | Viscosity (Pa·s) |\n|---------------------|-----------------|\n| 0                   | 0.000545        |\n| 0.5994              | 0.001463        |\n| 0.6997              | 0.001554        |\n| 0.7986              | 0.001542        |\n| 0.8999              | 0.001317        |\n| 1                   | 0.00089         |\n\nThe data clearly show the well-known viscosity maximum in water–methanol mixtures: at 298.15 K, the viscosity peaks near x(water) ≈ 0.70 (0.001554 Pa·s), substantially exceeding the viscosity of either pure methanol (0.000545 Pa·s) or pure water (0.00089 Pa·s). This non-ideal behavior reflects strong hydrogen-bonding interactions and structural reorganization in the mixture.\n\nThree additional blocks were also identified in this temperature window, providing supplementary viscosity data at 293.15 or 298.15 K with partial composition coverage.",
  "core_claims": [
    "The ThermoML database contains a comprehensive dataset (PROPblock_9, GLOBlit_2825, DOI 10.1016/j.jct.2007.05.004) of 39 dynamic viscosity data points for binary water + methanol mixtures spanning the full composition range (mole fraction of water 0–1) at 293.15, 298.15, and 303.15 K and 101.0 kPa, with viscosity values ranging from 0.000508 to 0.001793 Pa·s.",
    "At 298.15 K, the data show a viscosity maximum near x(water) ≈ 0.70 (0.001554 Pa·s), substantially exceeding the viscosities of both pure methanol (0.000545 Pa·s) and pure water (0.00089 Pa·s), consistent with well-known non-ideal behavior attributed to strong hydrogen-bonding interactions and structural reorganization in the mixture."
  ],
  "status": "success",
  "summary": "A ThermoML search for dynamic viscosity (GLOBprop_4) of binary water (GLOBcomp_1) + methanol (GLOBcomp_4) in the 293–303 K range returned 4 data blocks. The most comprehensive is PROPblock_9 from GLOBlit_2825 (DOI: 10.1016/j.jct.2007.05.004), containing 39 data points spanning the full composition range (mole fraction of water 0–1) at 293.15, 298.15, and 303.15 K, all at 101.0 kPa, with viscosity values from 0.000508 to 0.001793 Pa·s. At 298.15 K, representative values include 0.000545 Pa·s for pure methanol, 0.001554 Pa·s near x(water) ≈ 0.70 (the viscosity maximum), and 0.00089 Pa·s for pure water, illustrating the well-known non-ideal viscosity maximum attributed to hydrogen-bonding interactions. Three additional blocks provide supplementary viscosity data at 293.15 or 298.15 K with partial composition coverage.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2825",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity measurements for water + methanol binary mixture at 293.15–303.15 K, 101.0 kPa, full composition range, 39 data points.",
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
            "min": 0.000508,
            "max": 0.001793,
            "mean": 0.001082,
            "std": 0.000366,
            "n": 39
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000508,
          "range_max": 0.001793
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
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "block_number": "PROPblock_9",
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
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000585"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.1973",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0009"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.5994",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001673"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.6997",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001793"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.7986",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001789"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.8999",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001522"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001003"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000545"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.5994",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001463"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.6997",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001554"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.7986",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001542"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.8999",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001317"
        },
        {
          "BLKpoint_id": "BLKpoint_26",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00089"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000508"
        },
        {
          "BLKpoint_id": "BLKpoint_34",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.5994",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001289"
        },
        {
          "BLKpoint_id": "BLKpoint_35",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.6997",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001342"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.7986",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001342"
        },
        {
          "BLKpoint_id": "BLKpoint_37",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.8999",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001147"
        },
        {
          "BLKpoint_id": "BLKpoint_39",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000797"
        }
      ],
      "inspection_id": "INSP_0b00b8eb05a1",
      "lit_num_id": "GLOBlit_2825"
    }
  ]
}