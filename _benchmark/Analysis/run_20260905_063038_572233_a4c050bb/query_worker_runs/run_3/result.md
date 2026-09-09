{
  "answer": "Pure ethanol mass density near 310 K at atmospheric pressure was found in the ThermoML database in DOI 10.1016/j.fluid.2005.10.022 (GLOBlit_323, PROPblock_2).\n\nNo data point exists at exactly 310 K. The two nearest bracketing values at 101.325 kPa are:\n\n| Temperature (K) | Mass Density (kg/m³) |\n|---|---|\n| 308.15 | 776.51 |\n| 313.15 | 772.138 |\n\nThe closest single value to 310 K is **776.51 kg/m³ at 308.15 K** (101.325 kPa), which is the nearest measured point below the target. Density decreases monotonically with temperature in this range, so the density at exactly 310 K would lie between these two values (approximately 772–777 kg/m³), but no interpolated value can be stated as a measured datum.",
  "core_claims": [
    "No ThermoML data point exists at exactly 310 K for pure ethanol mass density at atmospheric pressure; the two nearest bracketing values at 101.325 kPa are 776.51 kg/m³ at 308.15 K and 772.138 kg/m³ at 313.15 K (from DOI 10.1016/j.fluid.2005.10.022), so the closest single measured value to 310 K is 776.51 kg/m³ at 308.15 K and 101.325 kPa."
  ],
  "status": "success",
  "summary": "Pure ethanol mass density near 310 K at atmospheric pressure (101.325 kPa) was found in DOI 10.1016/j.fluid.2005.10.022. No data point exists at exactly 310 K. The two nearest bracketing measured values are 776.51 kg/m³ at 308.15 K and 772.138 kg/m³ at 313.15 K. The closest single measured value to 310 K is 776.51 kg/m³ at 308.15 K. Density decreases monotonically with temperature in this range, so the density at exactly 310 K would lie between these two values (approximately 772–777 kg/m³), but no interpolated value is stated as a measured datum.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_323",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_2"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density measurements for pure ethanol near 308–313 K at 101.325 kPa.",
      "doi": "10.1016/j.fluid.2005.10.022",
      "lit_id": "2006-ser-kij-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 6,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_2_1"
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
            "max": 313.15,
            "n_unique": 6
          },
          "range_min": 288.15,
          "range_max": 313.15
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
            "min": 772.138,
            "max": 793.721,
            "mean": 782.973333,
            "std": 8.07447,
            "n": 6
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 772.138,
          "range_max": 793.721
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
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "unary",
      "declared_n_components": 1,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 6,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.fluid.2005.10.022",
      "block_number": "PROPblock_2",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "308.15",
          "pressure_kpa": "101.325",
          "mass_density_kg_m3": "776.51"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "313.15",
          "pressure_kpa": "101.325",
          "mass_density_kg_m3": "772.138"
        }
      ],
      "inspection_id": "INSP_390354a63208",
      "lit_num_id": "GLOBlit_323"
    }
  ]
}