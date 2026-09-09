{
  "answer": "## DMSO + Water Binary Mixture Blocks\n\n### Thermal Conductivity (GLOBprop_34)\n- **Block:** PROPblock_5 in GLOBlit_10024 (DOI: 10.1021/je301171y)\n- **Points:** 63\n- **Composition range:** w(DMSO) = 0.1–0.9 (mass fraction)\n- **Temperature range:** 279.18–339.37 K\n- **Pressure:** 100.0 kPa (fixed constraint)\n- **Method:** Hot-wire method (GLOBmeas_41)\n- **Representative inspected values:** λ = 0.522 W/m/K at w=0.1, T=279.63 K; λ = 0.319 W/m/K at w=0.5013, T=279.57 K; λ = 0.196 W/m/K at w=0.9, T=338.51 K. Thermal conductivity decreases with increasing DMSO mass fraction and generally increases with temperature at each composition.\n\n### Surface Tension (GLOBprop_13)\n- **Block:** PROPblock_9 in GLOBlit_10766 (DOI: 10.1021/je7001013)\n- **Points:** 112\n- **Composition range:** x(DMSO) = 0.0121–0.8945 (mole fraction)\n- **Temperature range:** 298.15–328.15 K\n- **Method:** Maximal bubble pressure (GLOBmeas_36)\n- **Representative inspected values:** γ = 0.071 N/m at x=0.0121, T=298.15 K; γ = 0.046 N/m at x=0.59, T=298.15 K; γ = 0.042 N/m at x=0.8945, T=298.15 K; γ = 0.0387 N/m at x=0.8945, T=328.15 K. Surface tension decreases sharply with initial DMSO addition and more gradually at higher DMSO content.\n\n### Refractive Index (GLOBprop_7)\n- **Block:** PROPblock_10 in GLOBlit_10766 (DOI: 10.1021/je7001013)\n- **Points:** 33\n- **Composition range:** x(DMSO) = 0.0121–0.7685 (mole fraction)\n- **Temperature range:** 298.15–308.15 K\n- **Pressure:** 101.0 kPa (fixed constraint)\n- **Method:** Abbe refractometer (GLOBmeas_163)\n- **Representative inspected values:** n_D = 1.34 at x=0.0121, T=298.15 K; n_D = 1.4305 at x=0.2959, T=298.15 K; n_D = 1.47 at x=0.7685, T=298.15 K. Refractive index increases monotonically with DMSO mole fraction.\n\n---\n\n## All Blocks from GLOBlit_10766 (DOI: 10.1021/je7001013)\n\nThis reference contains data blocks (count derived from the search_blocks listing of that literature source) covering four sulfoxides (pure and binary with water), measuring surface tension (GLOBprop_13) and refractive index (GLOBprop_7):\n\n**Compounds studied:**\n- GLOBcomp_31 = dimethyl sulfoxide (DMSO)\n- GLOBcomp_1294 = diethyl sulfoxide\n- GLOBcomp_2145 = dipropyl sulfoxide\n- GLOBcomp_7698 = diisopropyl sulfoxide (2,2'-sulfinylbispropane)\n- GLOBcomp_1 = water\n\n| Block | System | Compound(s) | Property |\n|---|---|---|---|\n| PROPblock_1 | unary | GLOBcomp_31 (DMSO) | GLOBprop_13 (surface tension) |\n| PROPblock_2 | unary | GLOBcomp_31 (DMSO) | GLOBprop_7 (refractive index) |\n| PROPblock_3 | unary | GLOBcomp_1294 (diethyl sulfoxide) | GLOBprop_13 (surface tension) |\n| PROPblock_4 | unary | GLOBcomp_1294 (diethyl sulfoxide) | GLOBprop_7 (refractive index) |\n| PROPblock_5 | unary | GLOBcomp_2145 (dipropyl sulfoxide) | GLOBprop_13 (surface tension) |\n| PROPblock_6 | unary | GLOBcomp_2145 (dipropyl sulfoxide) | GLOBprop_7 (refractive index) |\n| PROPblock_7 | unary | GLOBcomp_7698 (diisopropyl sulfoxide) | GLOBprop_13 (surface tension) |\n| PROPblock_8 | unary | GLOBcomp_7698 (diisopropyl sulfoxide) | GLOBprop_7 (refractive index) |\n| PROPblock_9 | binary | GLOBcomp_31 + GLOBcomp_1 | GLOBprop_13 (surface tension) — 112 pts, x(DMSO) 0.0121–0.8945, T 298.15–328.15 K |\n| PROPblock_10 | binary | GLOBcomp_31 + GLOBcomp_1 | GLOBprop_7 (refractive index) — 33 pts, x(DMSO) 0.0121–0.7685, T 298.15–308.15 K |\n| PROPblock_11 | binary | GLOBcomp_1294 + GLOBcomp_1 | GLOBprop_13 (surface tension) |\n| PROPblock_12 | binary | GLOBcomp_1294 + GLOBcomp_1 | GLOBprop_7 (refractive index) |\n| PROPblock_13 | binary | GLOBcomp_2145 + GLOBcomp_1 | GLOBprop_13 (surface tension) |\n| PROPblock_14 | binary | GLOBcomp_2145 + GLOBcomp_1 | GLOBprop_7 (refractive index) |\n| PROPblock_15 | binary | GLOBcomp_7698 + GLOBcomp_1 | GLOBprop_13 (surface tension) |\n| PROPblock_16 | binary | GLOBcomp_7698 + GLOBcomp_1 | GLOBprop_7 (refractive index) |\n\nThe eight unary blocks provide pure-component baselines for each sulfoxide, while the eight binary blocks systematically cover each sulfoxide mixed with water. The DMSO+water blocks (PROPblock_9 and PROPblock_10) are the most data-rich among the binary blocks in this reference. Detailed numerical ranges for blocks not inspected in this run (PROPblock_1–8, PROPblock_11–16) are available but were not verified here.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNINSPECTED_BLOCK** PROPblock_11: PROPblock_11 is quoted with data values (16, …) but was never inspected in this run\n  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_11\", literature=\"<GLOBlit_N or DOI>\")`\nInspected so far: PROPblock_10, PROPblock_5, PROPblock_9",
  "core_claims": [
    "For the DMSO + water binary mixture at 100.0 kPa, thermal conductivity (63 points, w(DMSO) = 0.1–0.9, T = 279.18–339.37 K, hot-wire method) decreases with increasing DMSO mass fraction and generally increases with temperature at each composition, with representative values of λ = 0.522 W/m/K at w=0.1, T=279.63 K; λ = 0.319 W/m/K at w=0.5013, T=279.57 K; and λ = 0.196 W/m/K at w=0.9, T=338.51 K.",
    "For the DMSO + water binary mixture, surface tension (112 points, x(DMSO) = 0.0121–0.8945, T = 298.15–328.15 K, maximal bubble pressure method) decreases sharply with initial DMSO addition and more gradually at higher DMSO content, with representative values of γ = 0.071 N/m at x=0.0121, T=298.15 K; γ = 0.046 N/m at x=0.59, T=298.15 K; and γ = 0.042 N/m at x=0.8945, T=298.15 K.",
    "For the DMSO + water binary mixture at 101.0 kPa, refractive index (33 points, x(DMSO) = 0.0121–0.7685, T = 298.15–308.15 K, Abbe refractometer) increases monotonically with DMSO mole fraction, from n_D = 1.34 at x=0.0121 to n_D = 1.47 at x=0.7685 at 298.15 K.",
    "The reference DOI 10.1021/je7001013 contains 16 data blocks covering surface tension and refractive index for four sulfoxides (DMSO, diethyl sulfoxide, dipropyl sulfoxide, diisopropyl sulfoxide) as pure components and as binary mixtures with water; only the DMSO+water blocks (PROPblock_9 and PROPblock_10) were numerically inspected and verified.",
    "Several blocks cited in the answer (PROPblock_1–8, PROPblock_11–16) were not inspected during the analysis run and their detailed numerical ranges remain unverified."
  ],
  "status": "success",
  "summary": "Three DMSO + water binary mixture data blocks were identified and inspected. (1) Thermal conductivity (GLOBprop_34) in PROPblock_5 of GLOBlit_10024 (DOI: 10.1021/je301171y): 63 points, w(DMSO) = 0.1–0.9 mass fraction, T = 279.18–339.37 K, P = 100.0 kPa, measured by hot-wire method; representative values include λ = 0.522 W/m/K at w=0.1, T=279.63 K and λ = 0.196 W/m/K at w=0.9, T=338.51 K, with thermal conductivity decreasing with increasing DMSO content. (2) Surface tension (GLOBprop_13) in PROPblock_9 of GLOBlit_10766 (DOI: 10.1021/je7001013): 112 points, x(DMSO) = 0.0121–0.8945 mole fraction, T = 298.15–328.15 K, measured by maximal bubble pressure; representative values include γ = 0.071 N/m at x=0.0121, T=298.15 K and γ = 0.0387 N/m at x=0.8945, T=328.15 K, with surface tension decreasing sharply upon initial DMSO addition. (3) Refractive index (GLOBprop_7) in PROPblock_10 of GLOBlit_10766: 33 points, x(DMSO) = 0.0121–0.7685, T = 298.15–308.15 K, P = 101.0 kPa, measured by Abbe refractometer; n_D increases monotonically with DMSO mole fraction from 1.34 to 1.47. GLOBlit_10766 additionally contains 16 total blocks covering four sulfoxides (DMSO, diethyl sulfoxide, dipropyl sulfoxide, diisopropyl sulfoxide) as pure components and binary mixtures with water, measuring surface tension and refractive index; only the DMSO+water blocks (PROPblock_9 and PROPblock_10) were numerically inspected.",
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
      "core_GLOB_id": "GLOBcomp_1294",
      "registry_id": "diethyl_sulfoxide",
      "name": "diethyl sulfoxide"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_2145",
      "registry_id": "dipropyl_sulfoxide",
      "name": "dipropyl sulfoxide"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_7698",
      "registry_id": "2,2'-sulfinylbispropane",
      "name": "2,2'-sulfinylbispropane"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_34",
      "registry_id": "thermal_conductivity_w_m_k",
      "name": "Thermal conductivity, W/m/K"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_13",
      "registry_id": "surface_tension_liquidgas_n_m",
      "name": "Surface tension liquid-gas, N/m"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_7",
      "registry_id": "refractive_index_na_dline",
      "name": "Refractive index (Na D-line)"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_10024",
      "registry_id": "2013-zho-che-0",
      "name": "10.1021/je301171y"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_10766",
      "registry_id": "2007-mar-ter-0",
      "name": "10.1021/je7001013"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBmeas_41",
      "registry_id": "hot_wire_method",
      "name": "Hot wire method"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBmeas_36",
      "registry_id": "maximal_bubble_pressure",
      "name": "Maximal bubble pressure"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBmeas_163",
      "registry_id": "abbe_ufactor_4",
      "name": "ABBE:UFactor:4"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_10024",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_34"
      ],
      "description": "Thermal conductivity of DMSO+water binary mixture; 63 points; w(DMSO) 0.1–0.9 (mass fraction); T 279.18–339.37 K; P 100.0 kPa; hot-wire method (GLOBmeas_41).",
      "doi": "10.1021/je301171y",
      "lit_id": "2013-zho-che-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 63,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
            "BLKvar_id": "BLKvar_1",
            "name": "Mass fraction",
            "min": 0.1,
            "max": 0.9,
            "n_unique": 9
          },
          "range_min": 0.1,
          "range_max": 0.9
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
            "min": 279.18,
            "max": 339.37,
            "n_unique": 62
          },
          "range_min": 279.18,
          "range_max": 339.37
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_34",
          "prop_ID": "thermal_conductivity_w_m_k",
          "name": "Thermal conductivity, W/m/K",
          "group": "TransportProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_41",
          "meas_ID": "hot_wire_method",
          "method_standard": "Hot wire method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Thermal conductivity, W/m/K",
            "min": 0.196,
            "max": 0.594,
            "mean": 0.354825,
            "std": 0.121236,
            "n": 63
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.196,
          "range_max": 0.594
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
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
      "parent_n_datapoints": 63,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_31"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of pure DMSO.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 7,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
            "min": 298.15,
            "max": 328.15,
            "n_unique": 7
          },
          "range_min": 298.15,
          "range_max": 328.15
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_13",
          "prop_ID": "surface_tension_liquidgas_n_m",
          "name": "Surface tension liquid-gas, N/m",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_714",
          "meas_ID": "bubblep_ufactor_8",
          "method_standard": null,
          "method_custom": "BUBBLEP:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0379,
            "max": 0.0417,
            "mean": 0.039743,
            "std": 0.001359,
            "n": 7
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0379,
          "range_max": 0.0417
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
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "unary",
      "declared_n_components": 1,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "parent_n_datapoints": 7,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_31"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of pure DMSO.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 3,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
            "min": 298.15,
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 308.15
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.472,
            "max": 1.4765,
            "mean": 1.474167,
            "std": 0.002255,
            "n": 3
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.472,
          "range_max": 1.4765
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "parent_n_datapoints": 3,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_1294"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of pure diethyl sulfoxide.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 7,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
          "sample_num": "DOIcompSample_2_1"
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
            "max": 328.15,
            "n_unique": 7
          },
          "range_min": 298.15,
          "range_max": 328.15
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_13",
          "prop_ID": "surface_tension_liquidgas_n_m",
          "name": "Surface tension liquid-gas, N/m",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_714",
          "meas_ID": "bubblep_ufactor_8",
          "method_standard": null,
          "method_custom": "BUBBLEP:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.032,
            "max": 0.0346,
            "mean": 0.033243,
            "std": 0.000943,
            "n": 7
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.032,
          "range_max": 0.0346
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
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 7,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_1294"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of pure diethyl sulfoxide.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 3,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
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
            "min": 298.15,
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 308.15
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.464,
            "max": 1.468,
            "mean": 1.466,
            "std": 0.002,
            "n": 3
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.464,
          "range_max": 1.468
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
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 3,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_2145"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of pure dipropyl sulfoxide.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 7,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
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
            "max": 328.15,
            "n_unique": 7
          },
          "range_min": 298.15,
          "range_max": 328.15
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_13",
          "prop_ID": "surface_tension_liquidgas_n_m",
          "name": "Surface tension liquid-gas, N/m",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_714",
          "meas_ID": "bubblep_ufactor_8",
          "method_standard": null,
          "method_custom": "BUBBLEP:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0294,
            "max": 0.0326,
            "mean": 0.030986,
            "std": 0.001142,
            "n": 7
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0294,
          "range_max": 0.0326
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
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "parent_n_datapoints": 7,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_6",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_2145"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of pure dipropyl sulfoxide.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 3,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
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
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 308.15
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.456,
            "max": 1.4595,
            "mean": 1.457833,
            "std": 0.001756,
            "n": 3
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.456,
          "range_max": 1.4595
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
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "parent_n_datapoints": 3,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_7",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_7698"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of pure diisopropyl sulfoxide.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 7,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
          "sample_num": "DOIcompSample_4_1"
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
            "max": 328.15,
            "n_unique": 7
          },
          "range_min": 298.15,
          "range_max": 328.15
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_13",
          "prop_ID": "surface_tension_liquidgas_n_m",
          "name": "Surface tension liquid-gas, N/m",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_714",
          "meas_ID": "bubblep_ufactor_8",
          "method_standard": null,
          "method_custom": "BUBBLEP:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0291,
            "max": 0.0318,
            "mean": 0.030343,
            "std": 0.000961,
            "n": 7
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0291,
          "range_max": 0.0318
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
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "unary",
      "declared_n_components": 1,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "parent_n_datapoints": 7,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_8",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_7698"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of pure diisopropyl sulfoxide.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 3,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
          "sample_num": "DOIcompSample_4_1"
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
            "min": 298.15,
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 308.15
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.4595,
            "max": 1.4645,
            "mean": 1.462,
            "std": 0.0025,
            "n": 3
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.4595,
          "range_max": 1.4645
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "parent_n_datapoints": 3,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of DMSO+water binary mixture; 112 points; x(DMSO) 0.0121–0.8945; T 298.15–328.15 K; maximal bubble pressure method (GLOBmeas_36).",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 112,
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
            "max": 328.15,
            "n_unique": 7
          },
          "range_min": 298.15,
          "range_max": 328.15
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
            "min": 0.0121,
            "max": 0.8945,
            "n_unique": 19
          },
          "range_min": 0.0121,
          "range_max": 0.8945
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_13",
          "prop_ID": "surface_tension_liquidgas_n_m",
          "name": "Surface tension liquid-gas, N/m",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_36",
          "meas_ID": "maximal_bubble_pressure",
          "method_standard": "Maximal bubble pressure",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0387,
            "max": 0.071,
            "mean": 0.050623,
            "std": 0.008081,
            "n": 112
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0387,
          "range_max": 0.071
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 112,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_10",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of DMSO+water binary mixture; 33 points; x(DMSO) 0.0121–0.7685; T 298.15–308.15 K; P 101.0 kPa; Abbe refractometer (GLOBmeas_163).",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 33,
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
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 308.15
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
            "min": 0.0121,
            "max": 0.7685,
            "n_unique": 11
          },
          "range_min": 0.0121,
          "range_max": 0.7685
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.339,
            "max": 1.47,
            "mean": 1.420136,
            "std": 0.041686,
            "n": 33
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.339,
          "range_max": 1.47
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
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_5_1"
        }
      ],
      "parent_n_datapoints": 33,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_11",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_1294",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of diethyl sulfoxide+water binary mixture.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 56,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
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
            "max": 328.15,
            "n_unique": 7
          },
          "range_min": 298.15,
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
            "min": 0.0099,
            "max": 0.7123,
            "n_unique": 8
          },
          "range_min": 0.0099,
          "range_max": 0.7123
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_13",
          "prop_ID": "surface_tension_liquidgas_n_m",
          "name": "Surface tension liquid-gas, N/m",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_714",
          "meas_ID": "bubblep_ufactor_8",
          "method_standard": null,
          "method_custom": "BUBBLEP:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0344,
            "max": 0.0655,
            "mean": 0.048232,
            "std": 0.00916,
            "n": 56
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0344,
          "range_max": 0.0655
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
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
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
      "parent_n_datapoints": 56,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_12",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_1294",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of diethyl sulfoxide+water binary mixture.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 30,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
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
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 308.15
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
            "min": 0.0099,
            "max": 0.7741,
            "n_unique": 10
          },
          "range_min": 0.0099,
          "range_max": 0.7741
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.3315,
            "max": 1.466,
            "mean": 1.425617,
            "std": 0.04507,
            "n": 30
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.3315,
          "range_max": 1.466
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
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
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
      "parent_n_datapoints": 30,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_13",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2145",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of dipropyl sulfoxide+water binary mixture.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 63,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
          "sample_num": "DOIcompSample_3_1"
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
            "max": 328.15,
            "n_unique": 7
          },
          "range_min": 298.15,
          "range_max": 328.15
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
            "min": 0.0105,
            "max": 0.6818,
            "n_unique": 9
          },
          "range_min": 0.0105,
          "range_max": 0.6818
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_13",
          "prop_ID": "surface_tension_liquidgas_n_m",
          "name": "Surface tension liquid-gas, N/m",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_714",
          "meas_ID": "bubblep_ufactor_8",
          "method_standard": null,
          "method_custom": "BUBBLEP:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0308,
            "max": 0.0523,
            "mean": 0.038037,
            "std": 0.005438,
            "n": 63
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0308,
          "range_max": 0.0523
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
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 63,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_14",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2145",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of dipropyl sulfoxide+water binary mixture.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 30,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
          "sample_num": "DOIcompSample_3_1"
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
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
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
            "min": 0.0105,
            "max": 0.9002,
            "n_unique": 10
          },
          "range_min": 0.0105,
          "range_max": 0.9002
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.342,
            "max": 1.458,
            "mean": 1.413533,
            "std": 0.042243,
            "n": 30
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.342,
          "range_max": 1.458
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
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 30,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_15",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_7698",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of diisopropyl sulfoxide+water binary mixture.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 53,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
          "sample_num": "DOIcompSample_4_1"
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
            "max": 328.15,
            "n_unique": 7
          },
          "range_min": 298.15,
          "range_max": 328.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_4",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_4",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0087,
            "max": 0.8899,
            "n_unique": 8
          },
          "range_min": 0.0087,
          "range_max": 0.8899
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_13",
          "prop_ID": "surface_tension_liquidgas_n_m",
          "name": "Surface tension liquid-gas, N/m",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_714",
          "meas_ID": "bubblep_ufactor_8",
          "method_standard": null,
          "method_custom": "BUBBLEP:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0289,
            "max": 0.0525,
            "mean": 0.037625,
            "std": 0.007468,
            "n": 53
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0289,
          "range_max": 0.0525
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
          "sample_num": "DOIcompSample_4_1"
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
      "parent_n_datapoints": 53,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_16",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_7698",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of diisopropyl sulfoxide+water binary mixture.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 24,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
          "sample_num": "DOIcompSample_4_1"
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
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 308.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_4",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_4",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0087,
            "max": 0.8899,
            "n_unique": 8
          },
          "range_min": 0.0087,
          "range_max": 0.8899
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.342,
            "max": 1.4635,
            "mean": 1.413854,
            "std": 0.048453,
            "n": 24
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.342,
          "range_max": 1.4635
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
          "sample_num": "DOIcompSample_4_1"
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
      "parent_n_datapoints": 24,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1021/je301171y",
      "block_number": "PROPblock_5",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "mass_fraction_<dimethyl sulfoxide>",
        "temperature_k",
        "pressure_kpa",
        "thermal_conductivity_w_m_k"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mass_fraction_<dimethyl sulfoxide>": "0.1",
          "temperature_k": "279.63",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.522"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "mass_fraction_<dimethyl sulfoxide>": "0.1",
          "temperature_k": "338.6",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.594"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mass_fraction_<dimethyl sulfoxide>": "0.1995",
          "temperature_k": "279.91",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.466"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "mass_fraction_<dimethyl sulfoxide>": "0.1995",
          "temperature_k": "338.93",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.528"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "mass_fraction_<dimethyl sulfoxide>": "0.2998",
          "temperature_k": "280.21",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.414"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "mass_fraction_<dimethyl sulfoxide>": "0.2998",
          "temperature_k": "339.37",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.465"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "mass_fraction_<dimethyl sulfoxide>": "0.3967",
          "temperature_k": "279.76",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.366"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "mass_fraction_<dimethyl sulfoxide>": "0.3967",
          "temperature_k": "338.87",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.404"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "mass_fraction_<dimethyl sulfoxide>": "0.5013",
          "temperature_k": "279.57",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.319"
        },
        {
          "BLKpoint_id": "BLKpoint_35",
          "mass_fraction_<dimethyl sulfoxide>": "0.5013",
          "temperature_k": "338.61",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.347"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "mass_fraction_<dimethyl sulfoxide>": "0.599",
          "temperature_k": "280.01",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.282"
        },
        {
          "BLKpoint_id": "BLKpoint_42",
          "mass_fraction_<dimethyl sulfoxide>": "0.599",
          "temperature_k": "338.9",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.299"
        },
        {
          "BLKpoint_id": "BLKpoint_43",
          "mass_fraction_<dimethyl sulfoxide>": "0.6929",
          "temperature_k": "279.37",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.25"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "mass_fraction_<dimethyl sulfoxide>": "0.6929",
          "temperature_k": "338.59",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.261"
        },
        {
          "BLKpoint_id": "BLKpoint_50",
          "mass_fraction_<dimethyl sulfoxide>": "0.7941",
          "temperature_k": "279.69",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.222"
        },
        {
          "BLKpoint_id": "BLKpoint_56",
          "mass_fraction_<dimethyl sulfoxide>": "0.7941",
          "temperature_k": "338.86",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.224"
        },
        {
          "BLKpoint_id": "BLKpoint_57",
          "mass_fraction_<dimethyl sulfoxide>": "0.9",
          "temperature_k": "279.18",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.2"
        },
        {
          "BLKpoint_id": "BLKpoint_63",
          "mass_fraction_<dimethyl sulfoxide>": "0.9",
          "temperature_k": "338.51",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.196"
        }
      ],
      "inspection_id": "INSP_37d8a4c5a601",
      "lit_num_id": "GLOBlit_10024"
    },
    {
      "doi": "10.1021/je7001013",
      "block_number": "PROPblock_9",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<dimethyl sulfoxide>",
        "surface_tension_liquidgas_n_m"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.071"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.0612"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2999",
          "surface_tension_liquidgas_n_m": "0.0533"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4523",
          "surface_tension_liquidgas_n_m": "0.0503"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.046"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.042"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.0701"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.0606"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1979",
          "surface_tension_liquidgas_n_m": "0.0558"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2999",
          "surface_tension_liquidgas_n_m": "0.0524"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4523",
          "surface_tension_liquidgas_n_m": "0.0499"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.501",
          "surface_tension_liquidgas_n_m": "0.0474"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.0452"
        },
        {
          "BLKpoint_id": "BLKpoint_32",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.0414"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.0692"
        },
        {
          "BLKpoint_id": "BLKpoint_35",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.0598"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1979",
          "surface_tension_liquidgas_n_m": "0.0548"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2999",
          "surface_tension_liquidgas_n_m": "0.0515"
        },
        {
          "BLKpoint_id": "BLKpoint_43",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4523",
          "surface_tension_liquidgas_n_m": "0.0491"
        },
        {
          "BLKpoint_id": "BLKpoint_44",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.501",
          "surface_tension_liquidgas_n_m": "0.0467"
        },
        {
          "BLKpoint_id": "BLKpoint_45",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.0446"
        },
        {
          "BLKpoint_id": "BLKpoint_46",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7027",
          "surface_tension_liquidgas_n_m": "0.0426"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.0409"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.0676"
        },
        {
          "BLKpoint_id": "BLKpoint_51",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.0587"
        },
        {
          "BLKpoint_id": "BLKpoint_52",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1979",
          "surface_tension_liquidgas_n_m": "0.0539"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2999",
          "surface_tension_liquidgas_n_m": "0.0506"
        },
        {
          "BLKpoint_id": "BLKpoint_59",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4523",
          "surface_tension_liquidgas_n_m": "0.0482"
        },
        {
          "BLKpoint_id": "BLKpoint_61",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.0438"
        },
        {
          "BLKpoint_id": "BLKpoint_64",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.0403"
        },
        {
          "BLKpoint_id": "BLKpoint_65",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.0664"
        },
        {
          "BLKpoint_id": "BLKpoint_67",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.0579"
        },
        {
          "BLKpoint_id": "BLKpoint_69",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2507",
          "surface_tension_liquidgas_n_m": "0.0512"
        },
        {
          "BLKpoint_id": "BLKpoint_70",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3218",
          "surface_tension_liquidgas_n_m": "0.0507"
        },
        {
          "BLKpoint_id": "BLKpoint_77",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.0431"
        },
        {
          "BLKpoint_id": "BLKpoint_80",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.0398"
        },
        {
          "BLKpoint_id": "BLKpoint_81",
          "temperature_k": "323.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.0653"
        },
        {
          "BLKpoint_id": "BLKpoint_83",
          "temperature_k": "323.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.057"
        },
        {
          "BLKpoint_id": "BLKpoint_85",
          "temperature_k": "323.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2507",
          "surface_tension_liquidgas_n_m": "0.0503"
        },
        {
          "BLKpoint_id": "BLKpoint_86",
          "temperature_k": "323.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3218",
          "surface_tension_liquidgas_n_m": "0.0499"
        },
        {
          "BLKpoint_id": "BLKpoint_93",
          "temperature_k": "323.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.0423"
        },
        {
          "BLKpoint_id": "BLKpoint_96",
          "temperature_k": "323.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.0392"
        },
        {
          "BLKpoint_id": "BLKpoint_97",
          "temperature_k": "328.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.0651"
        },
        {
          "BLKpoint_id": "BLKpoint_99",
          "temperature_k": "328.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.0551"
        },
        {
          "BLKpoint_id": "BLKpoint_101",
          "temperature_k": "328.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2507",
          "surface_tension_liquidgas_n_m": "0.0494"
        },
        {
          "BLKpoint_id": "BLKpoint_102",
          "temperature_k": "328.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3218",
          "surface_tension_liquidgas_n_m": "0.049"
        },
        {
          "BLKpoint_id": "BLKpoint_104",
          "temperature_k": "328.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3549",
          "surface_tension_liquidgas_n_m": "0.0474"
        },
        {
          "BLKpoint_id": "BLKpoint_109",
          "temperature_k": "328.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.0417"
        },
        {
          "BLKpoint_id": "BLKpoint_112",
          "temperature_k": "328.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.0387"
        }
      ],
      "inspection_id": "INSP_507097ca3b25",
      "lit_num_id": "GLOBlit_10766"
    },
    {
      "doi": "10.1021/je7001013",
      "block_number": "PROPblock_10",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<dimethyl sulfoxide>",
        "pressure_kpa",
        "refractive_index_na_dline"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.34"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1467",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.396"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2959",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4305"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4301",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4475"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.5964",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.461"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7685",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.47"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.339"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1467",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4005"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2959",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4295"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3967",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.443"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.5964",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.459"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7685",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.468"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.3395"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1467",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2959",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.428"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3967",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.442"
        },
        {
          "BLKpoint_id": "BLKpoint_32",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.5964",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.458"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7685",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.466"
        }
      ],
      "inspection_id": "INSP_2257cf4faf77",
      "lit_num_id": "GLOBlit_10766"
    }
  ]
}