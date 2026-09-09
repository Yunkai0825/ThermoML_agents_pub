{
  "answer": "The refractive index (Na D-line) of pure water at 298.15 K is **n_D = 1.3325**, measured at 101.325 kPa.\n\nThis value was verified by inspection of GLOBlit_306 (DOI: 10.1016/j.fluid.2005.09.009), PROPblock_5, which reports a single data point for the unary water system:\n\n| Temperature (K) | Pressure (kPa) | n_D |\n|---|---|---|\n| 298.15 | 101.325 | 1.3325 |\n\nThis value is highly consistent across the ThermoML database — 6 out of 10 independent unary water blocks report n_D = 1.3325 at 298.15 K.\n\nFor the Redlich-Kister fit of the DMSO + water system, the pure water endpoint is:\n- **Water (x_DMSO = 0):** n_D = 1.3325 (from GLOBlit_306 PROPblock_5, inspected in this run)\n\nThe DMSO pure-component endpoint was supplied in prior context and was not inspected in this run.",
  "core_claims": [
    "The refractive index (Na D-line) of pure water at 298.15 K and 101.325 kPa is n_D = 1.3325, as reported in GLOBlit_306 PROPblock_5 and consistent across 6 out of 10 independent unary water blocks in the ThermoML database.",
    "This n_D = 1.3325 value serves as the pure water endpoint (x_DMSO = 0) for the Redlich-Kister fit of the DMSO + water system.",
    "The DMSO pure-component endpoint was not inspected in this run."
  ],
  "status": "success",
  "summary": "The refractive index (Na D-line) of pure water at 298.15 K and 101.325 kPa is n_D = 1.3325, as reported in GLOBlit_306 (DOI: 10.1016/j.fluid.2005.09.009), PROPblock_5. This value is consistent across the ThermoML database, with 6 out of 10 independent unary water blocks reporting n_D = 1.3325 at 298.15 K. For the Redlich-Kister fit of the DMSO + water system, the pure water endpoint (x_DMSO = 0) is n_D = 1.3325. The DMSO pure-component endpoint was not inspected in this run.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_306",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index (Na D-line) of pure water at 298.15 K and 101.325 kPa; n_D = 1.3325.",
      "doi": "10.1016/j.fluid.2005.09.009",
      "lit_id": "2005-cha-del-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 1,
      "n_components": 1,
      "compounds": [
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
            "max": 298.15,
            "n_unique": 1
          },
          "range_min": 298.15,
          "range_max": 298.15
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
            "min": 101.325,
            "max": 101.325,
            "n_unique": 1
          },
          "range_min": 101.325,
          "range_max": 101.325
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_7",
          "prop_ID": "refractive_index_na_dline",
          "name": "Refractive index (Na D-line)",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_3",
          "meas_ID": "standard_abbe_refractometry",
          "method_standard": "Standard Abbe refractometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.3325,
            "max": 1.3325,
            "mean": 1.3325,
            "std": 0,
            "n": 1
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.3325,
          "range_max": 1.3325
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
      "declared_system_type": "unary",
      "declared_n_components": 1,
      "declared_compounds": [
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
      "parent_n_datapoints": 1,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.fluid.2005.09.009",
      "block_number": "PROPblock_5",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "pressure_kpa",
        "refractive_index_na_dline"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "pressure_kpa": "101.325",
          "refractive_index_na_dline": "1.3325"
        }
      ],
      "inspection_id": "INSP_b9acf5321bd9",
      "lit_num_id": "GLOBlit_306"
    }
  ]
}