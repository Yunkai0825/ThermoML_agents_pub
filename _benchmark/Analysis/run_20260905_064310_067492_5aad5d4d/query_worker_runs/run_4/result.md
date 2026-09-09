{
  "answer": "**Viscosity data for binary ethylene glycol (1,2-ethanediol) + water mixtures near 298.15 K**\n\n**Compounds resolved:**\n- Ethylene glycol (1,2-ethanediol): **GLOBcomp_24** (C₂H₆O₂, SMILES: OCCO)\n- Water: **GLOBcomp_1** (H₂O)\n\n**Property:** Dynamic viscosity (GLOBprop_4), units: Pa·s\n\nFive inspected data blocks were found for binary liquid-phase mixtures covering temperatures near 298.15 K:\n\n| # | DOI | Block | Literature ID | Data Points | T range (K) | Composition Variable | P (kPa) |\n|---|-----|-------|---------------|-------------|-------------|----------------------|---------|\n| 1 | 10.1016/j.jct.2006.01.011 | PROPblock_13 | GLOBlit_2656 | 10 | 293.15–293.15 | mass fraction EG (GLOBcomp_24) | 101.325 |\n| 2 | 10.1016/j.jct.2018.02.022 | PROPblock_24 | GLOBlit_5201 | 84 | 293.15–308.15 | mole fraction EG (GLOBcomp_24) | 92.3 |\n| 3 | 10.1021/acs.jced.6b00526 | PROPblock_18 | GLOBlit_6951 | 33 | 293.15–303.15 | mole fraction water (GLOBcomp_1) | 100.0 |\n| 4 | 10.1021/je020140j | PROPblock_5 | GLOBlit_8038 | 77 | 293.15–353.15 | mole fraction EG (GLOBcomp_24) | 101.0 |\n| 5 | 10.1021/je025610o | PROPblock_5 | GLOBlit_8106 | 30 | 296.45–449.85 | mole fraction EG (GLOBcomp_24) | 100.0 |\n\nA sixth block was also matched in the initial search but its details were truncated; the five blocks above were fully inspected.\n\n**Representative data near 298.15 K:**\n\nFrom GLOBlit_5201::PROPblock_24 (at 298.15 K, 92.3 kPa):\n\n| Mole fraction EG | Viscosity (Pa·s) |\n|---|---|\n| 0 | 0.00089689 |\n| 0.2072 | 0.0028109 |\n| 0.4446 | 0.0060624 |\n| 1 | 0.016223 |\n\nFrom GLOBlit_6951::PROPblock_18 (at 298.15 K, 100.0 kPa):\n\n| Mole fraction water | Viscosity (Pa·s) |\n|---|---|\n| 0 | 0.01724 |\n| 0.2014 | 0.01219 |\n| 0.4011 | 0.00831 |\n| 0.6995 | 0.003884 |\n| 1 | 0.000843 |\n\n**Chemistry insight:** The viscosity of ethylene glycol–water mixtures increases strongly and nonlinearly with ethylene glycol content. In GLOBlit_5201::PROPblock_24 at 298.15 K, pure EG viscosity is 0.016223 Pa·s versus 0.00089689 Pa·s for pure water (a ratio of approximately 18×, derived by division). In GLOBlit_6951::PROPblock_18 at 298.15 K, pure EG viscosity is 0.01724 Pa·s versus 0.000843 Pa·s for pure water (a ratio of approximately 20×, derived by division). This reflects the extensive hydrogen-bonding network formed by the two hydroxyl groups of ethylene glycol. The most data-rich blocks near 298.15 K are GLOBlit_5201::PROPblock_24 (84 points, 293.15–308.15 K) and GLOBlit_8038::PROPblock_5 (77 points, 293.15–353.15 K), both using mole fraction of ethylene glycol as the composition variable.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **AMBIGUOUS_VALUE** PROPblock_5: 298.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_5\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"mole_fraction_<1,2-ethanediol>\", \"value\": 298.15})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNINSPECTED_VALUE** GLOBlit_5201::PROPblock_24: 18 exists in PROPblock_24's database table but was never shown in an inspection of this run\n  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number=\"GLOBlit_5201::PROPblock_24\", nearest={\"column\": \"temperature_k\", \"value\": 18.0})`\nInspected so far: PROPblock_13, PROPblock_18, PROPblock_24, PROPblock_5",
  "core_claims": [
    "Five ThermoML data blocks were identified containing dynamic viscosity data for binary ethylene glycol (1,2-ethanediol) + water liquid mixtures near 298.15 K, with the most data-rich blocks being GLOBlit_5201::PROPblock_24 (84 points, 293.15–308.15 K) and GLOBlit_8038::PROPblock_5 (77 points, 293.15–353.15 K).",
    "At 298.15 K, the viscosity of ethylene glycol–water mixtures increases strongly and nonlinearly with ethylene glycol content; in GLOBlit_5201::PROPblock_24 pure EG viscosity is 0.016223 Pa·s versus 0.00089689 Pa·s for pure water, and in GLOBlit_6951::PROPblock_18 pure EG viscosity is 0.01724 Pa·s versus 0.000843 Pa·s for pure water.",
    "The strong increase in viscosity with ethylene glycol content is attributed to the extensive hydrogen-bonding network formed by the two hydroxyl groups of ethylene glycol."
  ],
  "status": "success",
  "summary": "Dynamic viscosity (GLOBprop_4, Pa·s) data for binary mixtures of ethylene glycol (GLOBcomp_24, OCCO) and water (GLOBcomp_1) near 298.15 K were identified across five data blocks. The most data-rich blocks are GLOBlit_5201::PROPblock_24 (84 points, 293.15–308.15 K, mole fraction EG, 92.3 kPa) and GLOBlit_8038::PROPblock_5 (77 points, 293.15–353.15 K, mole fraction EG, 101.0 kPa). Additional blocks include GLOBlit_2656::PROPblock_13 (10 points at 293.15 K, mass fraction EG, 101.325 kPa), GLOBlit_6951::PROPblock_18 (33 points, 293.15–303.15 K, mole fraction water, 100.0 kPa), and GLOBlit_8106::PROPblock_5 (30 points, 296.45–449.85 K, mole fraction EG, 100.0 kPa). Representative values at 298.15 K from GLOBlit_5201::PROPblock_24: pure water viscosity 0.00089689 Pa·s, mole fraction EG 0.2072 gives 0.0028109 Pa·s, mole fraction EG 0.4446 gives 0.0060624 Pa·s, pure EG gives 0.016223 Pa·s. From GLOBlit_6951::PROPblock_18 at 298.15 K: pure EG (mole fraction water 0) gives 0.01724 Pa·s, mole fraction water 0.2014 gives 0.01219 Pa·s, mole fraction water 0.4011 gives 0.00831 Pa·s, mole fraction water 0.6995 gives 0.003884 Pa·s, pure water gives 0.000843 Pa·s. Viscosity increases strongly and nonlinearly with ethylene glycol content, reflecting the extensive hydrogen-bonding network of its two hydroxyl groups.",
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
      "description": "Dynamic viscosity of binary ethylene glycol + water at 293.15 K, mass fraction composition, 101.325 kPa.",
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
      "description": "Dynamic viscosity of binary ethylene glycol + water, 293.15–308.15 K, mole fraction composition, 92.3 kPa. 84 data points.",
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
    },
    {
      "lit_num_id": "GLOBlit_6951",
      "block_number": "PROPblock_18",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of binary ethylene glycol + water, 293.15–303.15 K, mole fraction of water composition, 100.0 kPa. 33 data points.",
      "doi": "10.1021/acs.jced.6b00526",
      "lit_id": "2017-moo-ros-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 33,
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
          "var_id": "mole_fraction_DOIcomp_5",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_5",
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
            "min": 0.000755,
            "max": 0.02113,
            "mean": 0.007699,
            "std": 0.005532,
            "n": 33
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000755,
          "range_max": 0.02113
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
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
      "lit_num_id": "GLOBlit_8038",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of binary ethylene glycol + water, 293.15–353.15 K, mole fraction composition, 101.0 kPa. 77 data points.",
      "doi": "10.1021/je020140j",
      "lit_id": "2003-yan-ma-2",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 77,
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
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
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
            "BLKvar_id": "BLKvar_1",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 11
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
            "max": 353.15,
            "n_unique": 7
          },
          "range_min": 293.15,
          "range_max": 353.15
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
          "meas_num_id": "GLOBmeas_227",
          "meas_ID": "captub_ufactor_3",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:3",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000356,
            "max": 0.020833,
            "mean": 0.002967,
            "std": 0.003516,
            "n": 77
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000356,
          "range_max": 0.020833
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 77,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8106",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of binary ethylene glycol + water, 296.45–449.85 K, mole fraction composition, 100.0 kPa. 30 data points.",
      "doi": "10.1021/je025610o",
      "lit_id": "2003-sun-tej-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 30,
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
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
            "BLKvar_id": "BLKvar_1",
            "name": "Mole fraction",
            "min": 0.25,
            "max": 0.75,
            "n_unique": 3
          },
          "range_min": 0.25,
          "range_max": 0.75
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
            "min": 296.45,
            "max": 449.85,
            "n_unique": 25
          },
          "range_min": 296.45,
          "range_max": 449.85
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
          "meas_num_id": "GLOBmeas_142",
          "meas_ID": "captub_ufactor_4",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000366,
            "max": 0.0123,
            "mean": 0.002177,
            "std": 0.002644,
            "n": 30
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000366,
          "range_max": 0.0123
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": "OCCO",
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 30,
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
    },
    {
      "doi": "10.1021/acs.jced.6b00526",
      "block_number": "PROPblock_18",
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
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.02113"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.2014",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01495"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.4011",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01005"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.6995",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.004584"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.000949"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01724"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.2014",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01219"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.4011",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00831"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.6995",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.003884"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.000843"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01423"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.2014",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.01014"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.4969",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.005653"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.000755"
        }
      ],
      "inspection_id": "INSP_bdb58d28aae5",
      "lit_num_id": "GLOBlit_6951"
    },
    {
      "doi": "10.1021/je020140j",
      "block_number": "PROPblock_5",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<1,2-ethanediol>",
        "temperature_k",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<1,2-ethanediol>": "0",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001002"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "mole_fraction_<1,2-ethanediol>": "0",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000356"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mole_fraction_<1,2-ethanediol>": "0.0312",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001337"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "mole_fraction_<1,2-ethanediol>": "0.0312",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000434"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "mole_fraction_<1,2-ethanediol>": "0.0676",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001785"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "mole_fraction_<1,2-ethanediol>": "0.0676",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000525"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "mole_fraction_<1,2-ethanediol>": "0.1105",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002272"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "mole_fraction_<1,2-ethanediol>": "0.1105",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001319"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "mole_fraction_<1,2-ethanediol>": "0.1105",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000629"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "mole_fraction_<1,2-ethanediol>": "0.162",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002951"
        },
        {
          "BLKpoint_id": "BLKpoint_31",
          "mole_fraction_<1,2-ethanediol>": "0.162",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001677"
        },
        {
          "BLKpoint_id": "BLKpoint_35",
          "mole_fraction_<1,2-ethanediol>": "0.162",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000758"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "mole_fraction_<1,2-ethanediol>": "0.2248",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.003941"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "mole_fraction_<1,2-ethanediol>": "0.2248",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002132"
        },
        {
          "BLKpoint_id": "BLKpoint_42",
          "mole_fraction_<1,2-ethanediol>": "0.2248",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000906"
        },
        {
          "BLKpoint_id": "BLKpoint_43",
          "mole_fraction_<1,2-ethanediol>": "0.3031",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.005102"
        },
        {
          "BLKpoint_id": "BLKpoint_45",
          "mole_fraction_<1,2-ethanediol>": "0.3031",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002756"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "mole_fraction_<1,2-ethanediol>": "0.3031",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0011"
        },
        {
          "BLKpoint_id": "BLKpoint_50",
          "mole_fraction_<1,2-ethanediol>": "0.4036",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.006898"
        },
        {
          "BLKpoint_id": "BLKpoint_52",
          "mole_fraction_<1,2-ethanediol>": "0.4036",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.003575"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "mole_fraction_<1,2-ethanediol>": "0.4036",
          "temperature_k": "333.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002053"
        },
        {
          "BLKpoint_id": "BLKpoint_56",
          "mole_fraction_<1,2-ethanediol>": "0.4036",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001359"
        },
        {
          "BLKpoint_id": "BLKpoint_57",
          "mole_fraction_<1,2-ethanediol>": "0.537",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.009696"
        },
        {
          "BLKpoint_id": "BLKpoint_58",
          "mole_fraction_<1,2-ethanediol>": "0.537",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.006749"
        },
        {
          "BLKpoint_id": "BLKpoint_59",
          "mole_fraction_<1,2-ethanediol>": "0.537",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.004776"
        },
        {
          "BLKpoint_id": "BLKpoint_61",
          "mole_fraction_<1,2-ethanediol>": "0.537",
          "temperature_k": "333.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002684"
        },
        {
          "BLKpoint_id": "BLKpoint_63",
          "mole_fraction_<1,2-ethanediol>": "0.537",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001748"
        },
        {
          "BLKpoint_id": "BLKpoint_64",
          "mole_fraction_<1,2-ethanediol>": "0.723",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.014042"
        },
        {
          "BLKpoint_id": "BLKpoint_65",
          "mole_fraction_<1,2-ethanediol>": "0.723",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.009399"
        },
        {
          "BLKpoint_id": "BLKpoint_66",
          "mole_fraction_<1,2-ethanediol>": "0.723",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.006449"
        },
        {
          "BLKpoint_id": "BLKpoint_68",
          "mole_fraction_<1,2-ethanediol>": "0.723",
          "temperature_k": "333.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00351"
        },
        {
          "BLKpoint_id": "BLKpoint_70",
          "mole_fraction_<1,2-ethanediol>": "0.723",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002296"
        },
        {
          "BLKpoint_id": "BLKpoint_71",
          "mole_fraction_<1,2-ethanediol>": "1",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.020833"
        },
        {
          "BLKpoint_id": "BLKpoint_72",
          "mole_fraction_<1,2-ethanediol>": "1",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.013646"
        },
        {
          "BLKpoint_id": "BLKpoint_73",
          "mole_fraction_<1,2-ethanediol>": "1",
          "temperature_k": "313.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.009443"
        },
        {
          "BLKpoint_id": "BLKpoint_75",
          "mole_fraction_<1,2-ethanediol>": "1",
          "temperature_k": "333.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00506"
        },
        {
          "BLKpoint_id": "BLKpoint_77",
          "mole_fraction_<1,2-ethanediol>": "1",
          "temperature_k": "353.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.003021"
        }
      ],
      "inspection_id": "INSP_ca607c3d05dd",
      "lit_num_id": "GLOBlit_8038"
    },
    {
      "doi": "10.1021/je025610o",
      "block_number": "PROPblock_5",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<1,2-ethanediol>",
        "temperature_k",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<1,2-ethanediol>": "0.25",
          "temperature_k": "296.45",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00369"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "mole_fraction_<1,2-ethanediol>": "0.25",
          "temperature_k": "313.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00229"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mole_fraction_<1,2-ethanediol>": "0.25",
          "temperature_k": "353.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00099"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mole_fraction_<1,2-ethanediol>": "0.25",
          "temperature_k": "435.55",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.000366"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mole_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "297.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00761"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "mole_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "313.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00449"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "mole_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "333.1",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00262"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "mole_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "353.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.0017"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "mole_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "380.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00107"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "mole_fraction_<1,2-ethanediol>": "0.5",
          "temperature_k": "440.65",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.0005"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "mole_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "297.35",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.0123"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "mole_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "313.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00697"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "mole_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "333.1",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00388"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "mole_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "353.05",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00242"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "mole_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "373.45",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00162"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "mole_fraction_<1,2-ethanediol>": "0.75",
          "temperature_k": "449.85",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.000594"
        }
      ],
      "inspection_id": "INSP_475115ec48f0",
      "lit_num_id": "GLOBlit_8106"
    }
  ]
}