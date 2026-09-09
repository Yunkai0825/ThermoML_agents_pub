{
  "answer": "## Viscosity Data for Binary DMF + Acetonitrile at 298.15 K\n\nTwo ThermoML data blocks contain dynamic viscosity measurements for the binary system N,N-dimethylformamide (DMF, GLOBcomp_18) + acetonitrile (GLOBcomp_15) at 298.15 K.\n\n### Primary dataset — full mole fraction range\n\n**Source:** DOI 10.1021/acs.jced.8b00176 (GLOBlit_7481, PROPblock_18)\nMethod: falling/rolling sphere viscometer; pressure constraint: 100.0 kPa.\nThe block contains 66 total data points (298.15–323.15 K); 11 points at 298.15 K span the complete mole fraction range of DMF:\n\n| x(DMF) | η (Pa·s) |\n|--------|----------|\n| 0      | 0.00034  |\n| 0.0989 | 0.0004   |\n| 0.1916 | 0.00044  |\n| 0.2925 | 0.00048  |\n| 0.3932 | 0.00054  |\n| 0.5029 | 0.00061  |\n| 0.6002 | 0.00065  |\n| 0.6931 | 0.00069  |\n| 0.7926 | 0.00075  |\n| 0.8996 | 0.00079  |\n| 1      | 0.00081  |\n\nThe viscosity increases monotonically from pure acetonitrile (0.00034 Pa·s) to pure DMF (0.00081 Pa·s) — a ratio of approximately 2.4 (computed from the inspected endpoint values: 0.00081 / 0.00034 ≈ 2.38). The increase is smooth and slightly concave, consistent with the stronger intermolecular interactions (hydrogen-bond accepting and dipole–dipole) in DMF compared with acetonitrile.\n\n### Secondary dataset — mass fraction basis\n\n**Source:** DOI 10.1016/j.jct.2014.02.019 (GLOBlit_4124, PROPblock_6)\nMethod: capillary (Ostwald/Ubbelohde) viscometer; pressure: 101.0 kPa; 20 total data points (298.15–313.15 K).\nFive compositions at 298.15 K (mass fraction of DMF):\n\n| w(DMF) | η (Pa·s) |\n|--------|----------|\n| 0      | 0.000342 |\n| 0.25   | 0.0003959|\n| 0.5    | 0.0005214|\n| 0.75   | 0.0006465|\n| 1      | 0.0007986|\n\nThe two datasets are mutually consistent: pure acetonitrile ≈ 0.00034 Pa·s and pure DMF ≈ 0.0008 Pa·s in both sources.\n\nThe mole-fraction dataset (PROPblock_18) is recommended for composition-dependent modelling as it covers 11 evenly spaced compositions across the full range.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNGROUNDED_LITERAL** PROPblock_18: 2.4 (near '…Pa·s) to pure DMF (0.00081 Pa·s) — a ratio of approximately …') matches no inspected row/stat, database table, or other source of PROPblock_18\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_18\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 2.4})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** PROPblock_18: 2.38 (near '…ted from the inspected endpoint values: 0.00081 / 0.00034 ≈ …') matches no inspected row/stat, database table, or other source of PROPblock_18\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_18\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 2.38})` — if it is a value you computed or an external reference, keep it and label its provenance instead\nInspected so far: PROPblock_18, PROPblock_6",
  "core_claims": [
    "At 298.15 K and approximately 100 kPa, the dynamic viscosity of the binary DMF + acetonitrile system increases monotonically from pure acetonitrile (0.00034 Pa·s) to pure DMF (0.00081 Pa·s) across 11 mole-fraction compositions spanning the full range (DOI 10.1021/acs.jced.8b00176).",
    "A second dataset (DOI 10.1016/j.jct.2014.02.019) reports viscosity on a mass-fraction basis at 298.15 K for five compositions, with pure-component values (acetonitrile 0.000342 Pa·s, DMF 0.0007986 Pa·s) mutually consistent with the first dataset.",
    "The mole-fraction dataset (11 compositions) is recommended for composition-dependent modelling over the mass-fraction dataset (5 compositions) due to its finer and more evenly spaced coverage."
  ],
  "status": "success",
  "summary": "Dynamic viscosity data for the binary system N,N-dimethylformamide (DMF) + acetonitrile at 298.15 K are reported from two ThermoML sources. The primary dataset (DOI 10.1021/acs.jced.8b00176, PROPblock_18) provides 11 mole-fraction compositions at 298.15 K and 100.0 kPa measured by falling/rolling sphere viscometer, spanning from pure acetonitrile (η = 0.00034 Pa·s at x(DMF) = 0) to pure DMF (η = 0.00081 Pa·s at x(DMF) = 1), with a smooth, monotonic, slightly concave increase. A secondary dataset (DOI 10.1016/j.jct.2014.02.019, PROPblock_6) gives five mass-fraction compositions at 298.15 K and 101.0 kPa measured by capillary viscometer, with pure-component values of 0.000342 Pa·s (acetonitrile) and 0.0007986 Pa·s (DMF). The two sources are mutually consistent. The mole-fraction dataset with 11 compositions is recommended for composition-dependent modelling.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_18",
      "registry_id": "dimethylformamide",
      "name": "dimethylformamide"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_15",
      "registry_id": "acetonitrile",
      "name": "acetonitrile"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_4",
      "registry_id": "viscosity_pa_s",
      "name": "Viscosity, Pa*s"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_7481",
      "registry_id": "2018-fat-riy-1",
      "name": "10.1021/acs.jced.8b00176"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_4124",
      "registry_id": "2014-bra-pra-0",
      "name": "10.1016/j.jct.2014.02.019"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_7481",
      "block_number": "PROPblock_18",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_18",
        "GLOBcomp_15"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of binary N,N-dimethylformamide + acetonitrile at 298.15 K across 11 mole fractions (0–1), measured by falling/rolling sphere viscometer at 100.0 kPa.",
      "doi": "10.1021/acs.jced.8b00176",
      "lit_id": "2018-fat-riy-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 66,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_15",
          "name": "acetonitrile",
          "formula": "C2H3N",
          "inchi_key": "WEVYAHXRMPXWCK-UHFFFAOYSA-N",
          "SMILES": "CC#N",
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
          "value": 100.0,
          "digits": 1,
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
            "max": 323.15,
            "n_unique": 6
          },
          "range_min": 298.15,
          "range_max": 323.15
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
            "n_unique": 11
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
          "meas_num_id": "GLOBmeas_8",
          "meas_ID": "falling_or_rolling_sphere_viscometry",
          "method_standard": "Falling or rolling sphere viscometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.00028,
            "max": 0.00081,
            "mean": 0.00052,
            "std": 0.000141,
            "n": 66
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.00028,
          "range_max": 0.00081
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
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_15",
          "name": "acetonitrile",
          "formula": "C2H3N",
          "inchi_key": "WEVYAHXRMPXWCK-UHFFFAOYSA-N",
          "SMILES": "CC#N",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 66,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_4124",
      "block_number": "PROPblock_6",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_18",
        "GLOBcomp_15"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of binary N,N-dimethylformamide + acetonitrile at 298.15 K at 5 mass fractions, measured by capillary viscometer at 101.0 kPa.",
      "doi": "10.1016/j.jct.2014.02.019",
      "lit_id": "2014-bra-pra-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 20,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_15",
          "name": "acetonitrile",
          "formula": "C2H3N",
          "inchi_key": "WEVYAHXRMPXWCK-UHFFFAOYSA-N",
          "SMILES": "CC#N",
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
            "max": 313.15,
            "n_unique": 4
          },
          "range_min": 298.15,
          "range_max": 313.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_3",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_3",
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
            "n_unique": 5
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
            "min": 0.000293,
            "max": 0.000799,
            "mean": 0.000492,
            "std": 0.000163,
            "n": 20
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000293,
          "range_max": 0.000799
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
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_15",
          "name": "acetonitrile",
          "formula": "C2H3N",
          "inchi_key": "WEVYAHXRMPXWCK-UHFFFAOYSA-N",
          "SMILES": "CC#N",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 20,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1021/acs.jced.8b00176",
      "block_number": "PROPblock_18",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<dimethylformamide>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00034"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.0989",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.0004"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.1916",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00044"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.2925",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00048"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.3932",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00054"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.5029",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00061"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.6002",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00065"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.6931",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00069"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.7926",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00075"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "0.8996",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00079"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00081"
        }
      ],
      "inspection_id": "INSP_fbc270263cf3",
      "lit_num_id": "GLOBlit_7481"
    },
    {
      "doi": "10.1016/j.jct.2014.02.019",
      "block_number": "PROPblock_6",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mass_fraction_<dimethylformamide>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000342"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "0.25",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0003959"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "0.5",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0005214"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "0.75",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0006465"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "298.15",
          "mass_fraction_<dimethylformamide>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0007986"
        }
      ],
      "inspection_id": "INSP_5ce79feb1bd5",
      "lit_num_id": "GLOBlit_4124"
    }
  ]
}