{
  "answer": "## Binary Mixture Viscosity Data: Ethylene Glycol + Water near 25 °C (298.15 K)\n\n**Compounds resolved:**\n- Ethylene glycol (1,2-ethanediol): **GLOBcomp_24** (C₂H₆O₂, SMILES: OCCO)\n- Water: **GLOBcomp_1** (H₂O)\n\n**Property:** Dynamic viscosity (**GLOBprop_4**)\n\nA search for binary ethylene glycol + water viscosity blocks in the temperature range 290–310 K returned **7 blocks**, all with a match score of 100. Five of the seven cover or bracket 298.15 K. Key candidates are summarized below:\n\n### Inspected Blocks\n\n**1. GLOBlit_2656 — PROPblock_13**\n- DOI: 10.1016/j.jct.2006.01.011\n- 10 data points at fixed T = 293.15 K, P = 101.325 kPa\n- Composition variable: mass fraction of 1,2-ethanediol (0 to 0.9)\n- Viscosity range: 0.001008–0.013999 Pa·s\n- Note: Single temperature (293.15 K), about 5 K below the search target of 298.15 K.\n\nRepresentative data at 293.15 K:\n\n| mass_fraction (EG) | viscosity (Pa·s) |\n|---|---|\n| 0 | 0.001008 |\n| 0.3 | 0.002177 |\n| 0.5 | 0.003558 |\n| 0.7 | 0.00636 |\n| 0.9 | 0.013999 |\n\n**2. GLOBlit_5201 — PROPblock_24**\n- DOI: 10.1016/j.jct.2018.02.022\n- 84 data points, T range: 293.15–308.15 K, P = 92.3 kPa (fixed)\n- Composition variable: mole fraction of 1,2-ethanediol (0 to 1)\n- Viscosity range: 0.00075887–0.020613 Pa·s\n- Note: Largest dataset; includes measurements at exactly 298.15 K.\n\nRepresentative data at 298.15 K from this block:\n\n| mole_fraction (EG) | viscosity (Pa·s) |\n|---|---|\n| 0 | 0.00089689 |\n| 0.2072 | 0.0028109 |\n| 0.4446 | 0.0060624 |\n| 1 | 0.016223 |\n\n### Additional Blocks (not inspected; data point counts below are from the search_blocks summary, not from block inspections)\n\n| GLOBlit | Data Points (from search summary) | Notes |\n|---|---|---|\n| GLOBlit_8038 | 77 (search summary) | Brackets 298.15 K |\n| GLOBlit_6951 | 33 (search summary) | Brackets 298.15 K |\n| GLOBlit_11506 | 16 | Includes T = 298.15 K exactly |\n\nTwo further blocks were also returned by the search but their detailed metadata was truncated in the tool output.\n\n**Chemistry insight:** The inspected data clearly show the strongly non-linear, monotonically increasing viscosity with ethylene glycol content. In PROPblock_13, viscosity rises roughly 14-fold from pure water (0.001008 Pa·s) to 90 wt% EG (0.013999 Pa·s) at 293.15 K. In PROPblock_24 at 298.15 K, pure EG viscosity (0.016223 Pa·s) is approximately 18 times that of pure water (0.00089689 Pa·s) (ratio computed from the two inspected values). This behavior reflects the extensive hydrogen-bonding network formed between ethylene glycol and water molecules, which reaches maximum cooperativity at intermediate compositions.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **MISATTRIBUTED_VALUE** PROPblock_13: 298.15 does not belong to PROPblock_13; it matches only GLOBlit_5201::PROPblock_24 (inspected this run)\n  fix (required — this IS a database value, under a different block): `re-anchor 298.15 to GLOBlit_5201::PROPblock_24 — no new tool call needed`\n- **UNGROUNDED_LITERAL** PROPblock_24: 77 (near '…Points (from search summary) | Notes | |---|---|---| |   | 7…') matches no inspected row/stat, database table, or other source of PROPblock_24\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_24\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 77.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** PROPblock_24: 33 (near '…|---| |   | 77 (search summary) | Brackets 298.15 K | |   | …') matches no inspected row/stat, database table, or other source of PROPblock_24\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_24\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 33.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNINSPECTED_VALUE** PROPblock_24: 18 exists in PROPblock_24's database table but was never shown in an inspection of this run\n  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number=\"GLOBlit_5201::PROPblock_24\", nearest={\"column\": \"temperature_k\", \"value\": 18.0})`\nInspected so far: PROPblock_13, PROPblock_24",
  "core_claims": [
    "Seven ThermoML blocks were found for binary ethylene glycol + water dynamic viscosity near 298.15 K, with five covering or bracketing that temperature.",
    "At 293.15 K and 101.325 kPa (GLOBlit_2656, PROPblock_13), viscosity increases monotonically from 0.001008 Pa·s at 0 mass fraction ethylene glycol to 0.013999 Pa·s at 0.9 mass fraction ethylene glycol.",
    "At 298.15 K and 92.3 kPa (GLOBlit_5201, PROPblock_24), viscosity increases from 0.00089689 Pa·s for pure water to 0.016223 Pa·s for pure ethylene glycol, with intermediate values of 0.0028109 Pa·s at mole fraction 0.2072 and 0.0060624 Pa·s at mole fraction 0.4446.",
    "The viscosity increase with ethylene glycol content is strongly non-linear and monotonic, consistent with extensive hydrogen-bonding interactions between ethylene glycol and water.",
    "Several additional blocks (GLOBlit_8038, GLOBlit_6951, GLOBlit_11506) were identified but not inspected in detail, so their data remain unverified."
  ],
  "status": "success",
  "summary": "Seven ThermoML blocks (all match score 100) were found for dynamic viscosity (GLOBprop_4) of binary ethylene glycol (GLOBcomp_24, OCCO) + water (GLOBcomp_1) in the 290–310 K range. Two blocks were inspected in detail. GLOBlit_2656 PROPblock_13 contains 10 data points at 293.15 K and 101.325 kPa, with viscosity spanning 0.001008–0.013999 Pa·s over mass fractions 0–0.9 of ethylene glycol. GLOBlit_5201 PROPblock_24 is the largest inspected dataset (84 data points, 293.15–308.15 K, 92.3 kPa) covering mole fractions 0–1 and including measurements at exactly 298.15 K; representative 298.15 K values are 0.00089689 Pa·s for pure water, 0.0028109 Pa·s at mole fraction 0.2072, 0.0060624 Pa·s at 0.4446, and 0.016223 Pa·s for pure ethylene glycol. Additional uninspected blocks from GLOBlit_8038, GLOBlit_6951, and GLOBlit_11506 also bracket or include 298.15 K. The data show a strongly non-linear, monotonic increase in viscosity with ethylene glycol content, consistent with extensive hydrogen-bonding interactions between the two components.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_24",
      "registry_id": "1,2-ethanediol",
      "name": "1,2-ethanediol"
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
      "lit_num_id": "GLOBlit_2656",
      "block_number": "PROPblock_13",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of ethylene glycol + water at 293.15 K, 10 data points, mass fraction composition variable.",
      "doi": "10.1016/j.jct.2006.01.011",
      "lit_id": "2006-tsi-mol-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 10,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
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
          "value": 293.15,
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
            "BLKvar_id": "BLKvar_1",
            "name": "Mass fraction",
            "min": 0.0,
            "max": 0.9,
            "n_unique": 10
          },
          "range_min": 0.0,
          "range_max": 0.9
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
            "min": 0.001008,
            "max": 0.013999,
            "mean": 0.004563,
            "std": 0.004021,
            "n": 10
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.001008,
          "range_max": 0.013999
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
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
      "parent_n_datapoints": 10,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_24",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of ethylene glycol + water, 84 data points, T range 293.15–308.15 K, mole fraction composition variable. Includes measurements at exactly 298.15 K.",
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_id": "2018-hog-tor-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 84,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_6_1"
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
          "value": 92.3,
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
            "n_unique": 21
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
          "meas_num_id": "GLOBmeas_11",
          "meas_ID": "concentric_cylinders_viscometry",
          "method_standard": "Concentric cylinders viscometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000759,
            "max": 0.020613,
            "mean": 0.007275,
            "std": 0.004937,
            "n": 84
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000759,
          "range_max": 0.020613
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_6_1"
        }
      ],
      "parent_n_datapoints": 84,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2006.01.011",
      "block_number": "PROPblock_13",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "mass_fraction_<1,2-ethanediol>",
        "temperature_k",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mass_fraction_<1,2-ethanediol>": "0",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.001008"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "mass_fraction_<1,2-ethanediol>": "0.1",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.001293"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "mass_fraction_<1,2-ethanediol>": "0.2",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.001671"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mass_fraction_<1,2-ethanediol>": "0.3",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.002177"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "mass_fraction_<1,2-ethanediol>": "0.4",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.002837"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "mass_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.003558"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "mass_fraction_<1,2-ethanediol>": "0.6",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.004724"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mass_fraction_<1,2-ethanediol>": "0.7",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.00636"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mass_fraction_<1,2-ethanediol>": "0.8",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.008003"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "mass_fraction_<1,2-ethanediol>": "0.9",
          "temperature_k": "293.15",
          "pressure_kpa": "101.325",
          "viscosity_pa_s": "0.013999"
        }
      ],
      "inspection_id": "INSP_eb6a6a268c1a",
      "lit_num_id": "GLOBlit_2656"
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "block_number": "PROPblock_24",
      "table_mode": "rdp",
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
          "temperature_k": "293.15",
          "mole_fraction_<1,2-ethanediol>": "0.0494",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0015411"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "293.15",
          "mole_fraction_<1,2-ethanediol>": "0.2072",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0035171"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "293.15",
          "mole_fraction_<1,2-ethanediol>": "0.4446",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0076382"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "298.15",
          "mole_fraction_<1,2-ethanediol>": "0.2072",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0028109"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "temperature_k": "298.15",
          "mole_fraction_<1,2-ethanediol>": "0.4446",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0060624"
        },
        {
          "BLKpoint_id": "BLKpoint_47",
          "temperature_k": "303.15",
          "mole_fraction_<1,2-ethanediol>": "0.4446",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0053492"
        },
        {
          "BLKpoint_id": "BLKpoint_65",
          "temperature_k": "308.15",
          "mole_fraction_<1,2-ethanediol>": "0.3921",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0040265"
        },
        {
          "BLKpoint_id": "BLKpoint_77",
          "temperature_k": "293.15",
          "mole_fraction_<1,2-ethanediol>": "0",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0010673"
        },
        {
          "BLKpoint_id": "BLKpoint_78",
          "temperature_k": "298.15",
          "mole_fraction_<1,2-ethanediol>": "0",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.00089689"
        },
        {
          "BLKpoint_id": "BLKpoint_79",
          "temperature_k": "303.15",
          "mole_fraction_<1,2-ethanediol>": "0",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0008385"
        },
        {
          "BLKpoint_id": "BLKpoint_80",
          "temperature_k": "308.15",
          "mole_fraction_<1,2-ethanediol>": "0",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.00075887"
        },
        {
          "BLKpoint_id": "BLKpoint_81",
          "temperature_k": "293.15",
          "mole_fraction_<1,2-ethanediol>": "1",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.020613"
        },
        {
          "BLKpoint_id": "BLKpoint_82",
          "temperature_k": "298.15",
          "mole_fraction_<1,2-ethanediol>": "1",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.016223"
        },
        {
          "BLKpoint_id": "BLKpoint_83",
          "temperature_k": "303.15",
          "mole_fraction_<1,2-ethanediol>": "1",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.013867"
        },
        {
          "BLKpoint_id": "BLKpoint_84",
          "temperature_k": "308.15",
          "mole_fraction_<1,2-ethanediol>": "1",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.011483"
        }
      ],
      "inspection_id": "INSP_10e84136b97d",
      "lit_num_id": "GLOBlit_5201"
    }
  ]
}