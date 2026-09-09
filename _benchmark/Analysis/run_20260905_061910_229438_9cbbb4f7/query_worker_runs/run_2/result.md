{
  "answer": "Inspection of PROPblock_4 from GLOBlit_11142 (DOI 10.1021/je800158z) confirms that both 303.15 K and 313.15 K are actual data points in the block.\n\n**Temperature 303.15 K** — exact match confirmed:\n\n| BLKpoint_id | mole_fraction (propan-2-ol) | temperature_k | pressure_kpa | mass_density_kg_m3 |\n|---|---|---|---|---|\n| BLKpoint_2 | 0 | 303.15 | 81.5 | 995.64 |\n\n**Temperature 313.15 K** — exact match confirmed:\n\n| BLKpoint_id | mole_fraction (propan-2-ol) | temperature_k | pressure_kpa | mass_density_kg_m3 |\n|---|---|---|---|---|\n| BLKpoint_3 | 0 | 313.15 | 81.5 | 992.21 |\n\nBoth rows shown are at mole fraction 0 (pure water end), with a fixed constraint of pressure = 81.5 kPa. The block contains 56 data points total covering the full composition range (mole fraction 0–1) and temperature range 293.15–323.15 K, with mass density spanning 758.68–998.2 kg/m³.",
  "core_claims": [
    "PROPblock_4 from GLOBlit_11142 (DOI 10.1021/je800158z) contains exact data points at both 303.15 K and 313.15 K, confirmed at mole fraction 0 (pure water) and pressure 81.5 kPa, with mass densities of 995.64 kg/m³ and 992.21 kg/m³ respectively.",
    "The block contains 56 data points total covering mole fractions 0–1 and temperatures 293.15–323.15 K, with mass density spanning 758.68–998.2 kg/m³."
  ],
  "status": "success",
  "summary": "In PROPblock_4 from GLOBlit_11142 (DOI 10.1021/je800158z), both 303.15 K and 313.15 K are confirmed as actual data points. At mole fraction 0 (pure water) and a fixed pressure constraint of 81.5 kPa, the mass density is 995.64 kg/m³ at 303.15 K and 992.21 kg/m³ at 313.15 K. The block contains 56 data points total, covering mole fractions 0–1 (propan-2-ol in water), temperatures 293.15–323.15 K, and mass densities spanning 758.68–998.2 kg/m³.",
  "core_id_updates": [],
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
      "description": "Mass density for propan-2-ol + water at 293.15–323.15 K and 81.5 kPa, covering mole fractions 0–1.",
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
      "block_number": "PROPblock_4",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<propan-2-ol>",
        "temperature_k",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_2",
          "mole_fraction_<propan-2-ol>": "0",
          "temperature_k": "303.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "995.64"
        }
      ],
      "inspection_id": "INSP_81c94e48aab9",
      "lit_num_id": "GLOBlit_11142"
    },
    {
      "doi": "10.1021/je800158z",
      "block_number": "PROPblock_4",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<propan-2-ol>",
        "temperature_k",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_3",
          "mole_fraction_<propan-2-ol>": "0",
          "temperature_k": "313.15",
          "pressure_kpa": "81.5",
          "mass_density_kg_m3": "992.21"
        }
      ],
      "inspection_id": "INSP_15f964415d37",
      "lit_num_id": "GLOBlit_11142"
    }
  ]
}