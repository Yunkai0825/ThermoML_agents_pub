{
  "answer": "**Viscosity data for binary DMF + ethylene glycol mixtures near 298.15 K**\n\nOne data block was found in the ThermoML database for the dynamic viscosity of the binary system N,N-dimethylformamide (DMF) + 1,2-ethanediol (ethylene glycol):\n\n- **DOI:** 10.1021/je060113j (GLOBlit_8892)\n- **Block:** PROPblock_25\n- **Compounds:** GLOBcomp_18 (dimethylformamide), GLOBcomp_24 (1,2-ethanediol)\n- **Property:** Dynamic viscosity (GLOBprop_4), measured by capillary tube method (GLOBmeas_4), liquid phase\n- **Composition:** Fixed mole fraction of 1,2-ethanediol = 0.5408\n- **Pressure:** 101.0 kPa\n\nThe block contains 3 data points at three temperatures:\n\n| BLKpoint_id | Temperature (K) | x(1,2-ethanediol) | Pressure (kPa) | Viscosity (Pa·s) |\n|---|---|---|---|---|\n| BLKpoint_1 | 298.15 | 0.5408 | 101.0 | 0.0030647 |\n| BLKpoint_2 | 308.15 | 0.5408 | 101.0 | 0.0024529 |\n| BLKpoint_3 | 318.15 | 0.5408 | 101.0 | 0.0019599 |\n\nAt exactly 298.15 K, the viscosity is **0.0030647 Pa·s** (≈ 3.06 mPa·s).\n\n**Chemistry note:** The viscosity decreases monotonically with increasing temperature (near-linear, R² = 0.9962), as expected for liquid mixtures. This block provides data at only one composition (x_EG = 0.5408); no additional composition-sweep blocks were found for this binary system in the database.",
  "core_claims": [
    "In the ThermoML database (DOI 10.1021/je060113j), the dynamic viscosity of the binary DMF + ethylene glycol mixture at a fixed 1,2-ethanediol mole fraction of 0.5408 and 101.0 kPa is reported as 0.0030647 Pa·s at 298.15 K, 0.0024529 Pa·s at 308.15 K, and 0.0019599 Pa·s at 318.15 K, decreasing monotonically with increasing temperature consistent with expected liquid-mixture behavior, with only one composition (x_EG = 0.5408) available for this binary system in the database."
  ],
  "status": "success",
  "summary": "A single data block from DOI 10.1021/je060113j (GLOBlit_8892, PROPblock_25) reports the dynamic viscosity of the binary system N,N-dimethylformamide (DMF) + 1,2-ethanediol (ethylene glycol) at a fixed mole fraction of 1,2-ethanediol = 0.5408 and 101.0 kPa, measured by capillary tube method in the liquid phase. Three data points are provided: at 298.15 K the viscosity is 0.0030647 Pa·s, at 308.15 K it is 0.0024529 Pa·s, and at 318.15 K it is 0.0019599 Pa·s. Viscosity decreases monotonically with increasing temperature. No additional composition-sweep blocks were found for this binary system in the database.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_18",
      "registry_id": "dimethylformamide",
      "name": "dimethylformamide"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_24",
      "registry_id": "1,2-ethanediol",
      "name": "1,2-ethanediol"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_8892",
      "registry_id": "2006-sin-roy-0",
      "name": "10.1021/je060113j"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_4",
      "registry_id": "viscosity_pa_s",
      "name": "Viscosity, Pa*s"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBmeas_4",
      "registry_id": "capillary_tube_ostwald_ubbelohde_method",
      "name": "Capillary tube (Ostwald; Ubbelohde) method"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_8892",
      "block_number": "PROPblock_25",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_18",
        "GLOBcomp_24"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of binary dimethylformamide + 1,2-ethanediol at 298.15–318.15 K, fixed x(1,2-ethanediol) = 0.5408, 101.0 kPa, capillary tube method.",
      "doi": "10.1021/je060113j",
      "lit_id": "2006-sin-roy-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 3,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "solvents": [],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_3",
          "constr_id": "mole_fraction_DOIcomp_1",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "value": 0.5408,
          "digits": 4,
          "component_org_num": "DOIcomp_1",
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
            "max": 318.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 318.15
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
            "min": 0.00196,
            "max": 0.003065,
            "mean": 0.002492,
            "std": 0.000553,
            "n": 3
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.00196,
          "range_max": 0.003065
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "parent_n_datapoints": 3,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1021/je060113j",
      "block_number": "PROPblock_25",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<1,2-ethanediol>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<1,2-ethanediol>": "0.5408",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0030647"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "308.15",
          "mole_fraction_<1,2-ethanediol>": "0.5408",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0024529"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "318.15",
          "mole_fraction_<1,2-ethanediol>": "0.5408",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0019599"
        }
      ],
      "inspection_id": "INSP_d1035750f998",
      "lit_num_id": "GLOBlit_8892"
    }
  ]
}