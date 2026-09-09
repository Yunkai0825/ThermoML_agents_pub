{
  "answer": "## Viscosity Data for DMSO + Water Binary Mixtures near 25 °C\n\nTwo binary mixture blocks containing dimethyl sulfoxide (DMSO, GLOBcomp_31) and water (GLOBcomp_1) with dynamic viscosity (GLOBprop_4) measurements near 298.15 K were found in the ThermoML database:\n\n### Block Summary\n\n| # | DOI | Block | GLOBlit | Total pts | Composition variable | T range (K) |\n|---|-----|-------|---------|-----------|---------------------|-------------|\n| 1 | 10.1016/j.jct.2006.12.012 | PROPblock_3 | GLOBlit_2781 | 120 | Mole fraction (GLOBvar_2) | 298.15–318.15 |\n| 2 | 10.1021/je9001027 | PROPblock_3 | GLOBlit_11517 | 35 | Mass fraction (GLOBvar_5) | 298.15–318.15 |\n\nBoth blocks report data at exactly 298.15 K with a pressure constraint of 101.0 kPa.\n\n### Block 1 — Data at 298.15 K (mole-fraction basis, GLOBlit_2781::PROPblock_3)\n\n24 data points at 298.15 K spanning x(DMSO) = 0–1. Representative inspected rows:\n\n| x(DMSO) | η (Pa·s) |\n|---------|----------|\n| 0 | 0.0008901 |\n| 0.0238 | 0.0010331 |\n| 0.0489 | 0.0012576 |\n| 0.1587 | 0.0025493 |\n| 0.2036 | 0.0030165 |\n| 0.2768 | 0.0035372 |\n| 0.3335 | 0.0037144 |\n| 0.3638 | 0.0037353 |\n| 0.3906 | 0.0037169 |\n| 0.4412 | 0.0036062 |\n| 0.5193 | 0.0033124 |\n| 0.6195 | 0.0028832 |\n| 0.7595 | 0.0024317 |\n| 0.8856 | 0.0021754 |\n| 1 | 0.001996 |\n\n### Block 2 — Data at 298.15 K (mass-fraction basis, GLOBlit_11517::PROPblock_3)\n\n7 data points at 298.15 K spanning w(DMSO) = 0–1:\n\n| w(DMSO) | η (Pa·s) |\n|---------|----------|\n| 0 | 0.00089 |\n| 0.2 | 0.00134 |\n| 0.4 | 0.002221 |\n| 0.5 | 0.0028073 |\n| 0.6 | 0.003421 |\n| 0.7 | 0.0023568 |\n| 1 | 0.001966 |\n\n**Chemistry insight:** Both datasets clearly show the well-known viscosity maximum in the DMSO–water system. In Block 1, the maximum viscosity of 0.0037353 Pa·s occurs at x(DMSO) = 0.3638, which is roughly 4.2× higher than pure water (0.0008901 Pa·s) and roughly 1.9× higher than pure DMSO (0.001996 Pa·s) (both ratios computed from the inspected data rows above). In Block 2, the maximum of 0.003421 Pa·s appears at w(DMSO) = 0.6. This pronounced viscosity maximum is attributed to strong hydrogen-bonding interactions between DMSO and water that form structured DMSO·2H₂O complexes, enhancing intermolecular friction in this composition range.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNGROUNDED_LITERAL** GLOBlit_11517::PROPblock_3: 4.2 (near '…0.0037353 Pa·s occurs at x(DMSO) = 0.3638, which is roughly …') matches no inspected row/stat, database table, or other source of GLOBlit_11517::PROPblock_3\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_11517::PROPblock_3\", nearest={\"column\": \"temperature_k\", \"value\": 4.2})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNINSPECTED_VALUE** GLOBlit_11517::PROPblock_3: 1.9 exists in PROPblock_3's database table but was never shown in an inspection of this run\n  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number=\"GLOBlit_2781::PROPblock_3\", nearest={\"column\": \"temperature_k\", \"value\": 1.9})`\nInspected so far: PROPblock_3",
  "core_claims": [
    "Two ThermoML blocks report dynamic viscosity data for DMSO + water binary mixtures at 298.15 K and 101.0 kPa: Block 1 (DOI 10.1016/j.jct.2006.12.012) provides 24 data points on a mole-fraction basis spanning x(DMSO) = 0–1, and Block 2 (DOI 10.1021/je9001027) provides 7 data points on a mass-fraction basis spanning w(DMSO) = 0–1.",
    "Both datasets exhibit a pronounced viscosity maximum at intermediate DMSO compositions: in Block 1 the maximum viscosity is 0.0037353 Pa·s at x(DMSO) = 0.3638; in Block 2 the maximum is 0.003421 Pa·s at w(DMSO) = 0.6.",
    "Pure-component viscosities at 298.15 K are reported as 0.0008901 Pa·s for water and 0.001996 Pa·s for DMSO in Block 1, and 0.00089 Pa·s for water and 0.001966 Pa·s for DMSO in Block 2.",
    "The viscosity maximum is attributed to strong hydrogen-bonding interactions between DMSO and water that form structured DMSO·2H₂O complexes, enhancing intermolecular friction in the intermediate composition range."
  ],
  "status": "success",
  "summary": "Two ThermoML blocks report dynamic viscosity (GLOBprop_4) for the binary mixture of DMSO (GLOBcomp_31) and water (GLOBcomp_1) at 298.15 K and 101.0 kPa. Block 1 (GLOBlit_2781::PROPblock_3, DOI 10.1016/j.jct.2006.12.012) contains 24 data points on a mole-fraction basis spanning x(DMSO) = 0–1, with viscosities ranging from 0.0008901 Pa·s (pure water) to a maximum of 0.0037353 Pa·s at x(DMSO) = 0.3638, then decreasing to 0.001996 Pa·s for pure DMSO. Block 2 (GLOBlit_11517::PROPblock_3, DOI 10.1021/je9001027) contains 7 data points on a mass-fraction basis spanning w(DMSO) = 0–1, with viscosities from 0.00089 Pa·s (pure water) to a maximum of 0.003421 Pa·s at w(DMSO) = 0.6, decreasing to 0.001966 Pa·s for pure DMSO. Both datasets exhibit the well-known viscosity maximum in the DMSO–water system, attributed to strong hydrogen-bonding interactions forming structured DMSO·2H₂O complexes that enhance intermolecular friction in that composition range.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_31",
      "registry_id": "dimethyl_sulfoxide",
      "name": "dimethyl sulfoxide"
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
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBvar_2",
      "registry_id": "mole_fraction_{DOIcomp_id}",
      "name": "Mole fraction"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBvar_5",
      "registry_id": "mass_fraction_{DOIcomp_id}",
      "name": "Mass fraction"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_2781",
      "registry_id": "2007-gra-jul-0",
      "name": "10.1016/j.jct.2006.12.012"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_11517",
      "registry_id": "2010-zam-tas-0",
      "name": "10.1021/je9001027"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2781",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity measurements for DMSO + water binary mixture at 298.15–318.15 K on mole-fraction basis; 120 total data points, 24 at 298.15 K.",
      "doi": "10.1016/j.jct.2006.12.012",
      "lit_id": "2007-gra-jul-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 120,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
            "min": 298.15,
            "max": 318.15,
            "n_unique": 5
          },
          "range_min": 298.15,
          "range_max": 318.15
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
            "n_unique": 24
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
            "min": 0.000596,
            "max": 0.003735,
            "mean": 0.002112,
            "std": 0.00077,
            "n": 120
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000596,
          "range_max": 0.003735
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
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
      "parent_n_datapoints": 120,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_11517",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity measurements for DMSO + water binary mixture at 298.15–318.15 K on mass-fraction basis; 35 total data points, 7 at 298.15 K.",
      "doi": "10.1021/je9001027",
      "lit_id": "2010-zam-tas-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 35,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
            "n_unique": 5
          },
          "range_min": 298.15,
          "range_max": 318.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_1",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_1",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mass fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 7
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
          "meas_num_id": "GLOBmeas_205",
          "meas_ID": "captub_ufactor_16",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:16",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000535,
            "max": 0.003421,
            "mean": 0.001868,
            "std": 0.000795,
            "n": 35
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000535,
          "range_max": 0.003421
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
      "parent_n_datapoints": 35,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2006.12.012",
      "block_number": "PROPblock_3",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<dimethyl sulfoxide>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0008901"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0238",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0010331"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0489",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0012576"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1587",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0025493"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2036",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0030165"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2379",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0033011"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2768",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0035372"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3074",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0036564"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3335",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0037144"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3638",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0037353"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3906",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0037169"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4412",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0036062"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.5193",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0033124"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.6195",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0028832"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.6813",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0026556"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7595",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0024317"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8856",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0021754"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001996"
        }
      ],
      "inspection_id": "INSP_b08a03233872",
      "lit_num_id": "GLOBlit_2781"
    },
    {
      "doi": "10.1021/je9001027",
      "block_number": "PROPblock_3",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mass_fraction_<dimethyl sulfoxide>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mass_fraction_<dimethyl sulfoxide>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00089"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "298.15",
          "mass_fraction_<dimethyl sulfoxide>": "0.2",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00134"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mass_fraction_<dimethyl sulfoxide>": "0.4",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002221"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "298.15",
          "mass_fraction_<dimethyl sulfoxide>": "0.5",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0028073"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mass_fraction_<dimethyl sulfoxide>": "0.6",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.003421"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "mass_fraction_<dimethyl sulfoxide>": "0.7",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0023568"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "mass_fraction_<dimethyl sulfoxide>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001966"
        }
      ],
      "inspection_id": "INSP_c018a8ec4dd8",
      "lit_num_id": "GLOBlit_11517"
    }
  ]
}