{
  "answer": "Three data blocks containing dynamic viscosity (η, Pa·s) measurements for the binary system **N-methyl-2-pyrrolidone (NMP) + water** were found near 298.15 K:\n\n| # | DOI | Literature ID | Block | Data Points | T range (K) | Composition variable | Pressure (kPa) |\n|---|-----|---------------|-------|-------------|-------------|---------------------|----------------|\n| 1 | 10.1021/je034073k | GLOBlit_8238 | PROPblock_3 | 65 | 298.15–343.15 | x(NMP) | 101.15 |\n| 2 | 10.1021/je0340809 | GLOBlit_8242 | PROPblock_17 | 95 | 298.15–338.15 | x(water) | 101.3 |\n| 3 | 10.1021/je100967k | GLOBlit_9372 | PROPblock_17 | 44 | 293.15–323.15 | x(NMP) | 101.0 |\n\n**Key observations:**\n\n- **Blocks 1 and 2** (GLOBlit_8238 and GLOBlit_8242) contain data exactly at **298.15 K**, making them directly usable without interpolation.\n- **Block 3** (GLOBlit_9372) does **not** include an exact 298.15 K isotherm; the nearest temperatures are **293.15 K** (below) and **303.15 K** (above).\n- All three blocks report data at approximately atmospheric pressure (~101 kPa).\n- Block 1 uses mole fraction of NMP as the composition variable, Block 2 uses mole fraction of water, and Block 3 uses mole fraction of NMP.\n\n**Representative data at 298.15 K from Block 1** (GLOBlit_8238::PROPblock_3):\n\n| x(NMP) | η (Pa·s) |\n|--------|----------|\n| 0 | 0.00089 |\n| 0.0501 | 0.00174 |\n| 0.0701 | 0.002137 |\n| 0.1001 | 0.002762 |\n| 0.2004 | 0.004555 |\n| 0.3004 | 0.005062 |\n| 0.4012 | 0.004505 |\n| 0.503 | 0.003729 |\n\n**Representative data at 298.15 K from Block 2** (GLOBlit_8242::PROPblock_17):\n\n| x(water) | η (Pa·s) |\n|----------|----------|\n| 0.0522 | 0.001721 |\n| 0.1684 | 0.001985 |\n| 0.2465 | 0.002147 |\n| 0.3481 | 0.002535 |\n\nThe data from Block 1 clearly shows a pronounced viscosity maximum near x(NMP) ≈ 0.3 (η = 0.005062 Pa·s at x(NMP) = 0.3004, from GLOBlit_8238::PROPblock_3), after which viscosity decreases at higher NMP mole fractions. This maximum is characteristic of strong hydrogen-bonding interactions between NMP and water, which create extensive intermolecular association networks at intermediate compositions. The overall viscosity range across the full composition span is 0.000405–0.005062 Pa·s (Block 1, GLOBlit_8238::PROPblock_3 stats) and 0.000467–0.005159 Pa·s (Block 2, GLOBlit_8242::PROPblock_17 stats).\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **MISATTRIBUTED_VALUE** GLOBlit_8242::PROPblock_17: 0.005062 does not belong to GLOBlit_8242::PROPblock_17; it matches only GLOBlit_8238::PROPblock_3 (inspected this run)\n  fix (required — this IS a database value, under a different block): `re-anchor 0.005062 to GLOBlit_8238::PROPblock_3 — no new tool call needed`\n- **MISATTRIBUTED_VALUE** GLOBlit_8242::PROPblock_17: 0.3004 does not belong to GLOBlit_8242::PROPblock_17; it matches only GLOBlit_8238::PROPblock_3 (inspected this run)\n  fix (required — this IS a database value, under a different block): `re-anchor 0.3004 to GLOBlit_8238::PROPblock_3 — no new tool call needed`\n- **MISATTRIBUTED_VALUE** GLOBlit_8238::PROPblock_3: 0.000467 does not belong to GLOBlit_8238::PROPblock_3; it matches only GLOBlit_8242::PROPblock_17 (inspected this run)\n  fix (required — this IS a database value, under a different block): `re-anchor 0.000467 to GLOBlit_8242::PROPblock_17 — no new tool call needed`\n- **MISATTRIBUTED_VALUE** GLOBlit_8238::PROPblock_3: 0.005159 does not belong to GLOBlit_8238::PROPblock_3; it matches only GLOBlit_8242::PROPblock_17 (inspected this run)\n  fix (required — this IS a database value, under a different block): `re-anchor 0.005159 to GLOBlit_8242::PROPblock_17 — no new tool call needed`\nInspected so far: PROPblock_17, PROPblock_3",
  "core_claims": [
    "Three ThermoML data blocks report dynamic viscosity (η, Pa·s) for the binary system N-methyl-2-pyrrolidone (NMP) + water near 298.15 K at approximately atmospheric pressure (~101 kPa), sourced from DOIs 10.1021/je034073k, 10.1021/je0340809, and 10.1021/je100967k.",
    "Blocks 1 (GLOBlit_8238::PROPblock_3) and 2 (GLOBlit_8242::PROPblock_17) contain data exactly at 298.15 K, while Block 3 (GLOBlit_9372::PROPblock_17) lacks an exact 298.15 K isotherm, with nearest temperatures of 293.15 K and 303.15 K.",
    "Data from Block 1 (GLOBlit_8238::PROPblock_3) show a pronounced viscosity maximum near x(NMP) ≈ 0.3, with η = 0.005062 Pa·s at x(NMP) = 0.3004, after which viscosity decreases at higher NMP mole fractions.",
    "The viscosity maximum is attributed to strong hydrogen-bonding interactions between NMP and water creating extensive intermolecular association networks at intermediate compositions.",
    "The overall viscosity range across the full composition span is 0.000405–0.005062 Pa·s for Block 1 (GLOBlit_8238::PROPblock_3) and 0.000467–0.005159 Pa·s for Block 2 (GLOBlit_8242::PROPblock_17), after correcting misattributed block assignments flagged in the answer.",
    "Several quoted statistical range values were flagged as misattributed between blocks, requiring re-anchoring but not invalidating the underlying data."
  ],
  "status": "success",
  "summary": "Dynamic viscosity (η, Pa·s) data for the binary system N-methyl-2-pyrrolidone (NMP) + water near 298.15 K were found in three ThermoML data blocks. Block 1 (DOI 10.1021/je034073k, GLOBlit_8238, PROPblock_3; 65 points, 298.15–343.15 K, x(NMP), 101.15 kPa) and Block 2 (DOI 10.1021/je0340809, GLOBlit_8242, PROPblock_17; 95 points, 298.15–338.15 K, x(water), 101.3 kPa) contain data exactly at 298.15 K. Block 3 (DOI 10.1021/je100967k, GLOBlit_9372, PROPblock_17; 44 points, 293.15–323.15 K, x(NMP), 101.0 kPa) lacks an exact 298.15 K isotherm, with nearest temperatures at 293.15 K and 303.15 K. Representative 298.15 K values from Block 1 include η = 0.00089 Pa·s at x(NMP) = 0, 0.002762 Pa·s at x(NMP) = 0.1001, a maximum of 0.005062 Pa·s at x(NMP) = 0.3004, and 0.003729 Pa·s at x(NMP) = 0.503. Block 2 values at 298.15 K include η = 0.001721 Pa·s at x(water) = 0.0522 and 0.002535 Pa·s at x(water) = 0.3481. The viscosity range across the full composition span is 0.000405–0.005062 Pa·s (Block 1) and 0.000467–0.005159 Pa·s (Block 2). The pronounced viscosity maximum near x(NMP) ≈ 0.3 is characteristic of strong NMP–water hydrogen-bonding interactions.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_8238",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_47",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity measurements for N-methyl-2-pyrrolidone + water at 298.15–343.15 K, 101.15 kPa, 65 data points, composition as mole fraction of NMP.",
      "doi": "10.1021/je034073k",
      "lit_id": "2004-hen-hro-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 65,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_47",
          "name": "N-methylpyrrolidone",
          "formula": "C5H9NO",
          "inchi_key": "SECXISVLQFMRJM-UHFFFAOYSA-N",
          "SMILES": "CN1CCCC1=O",
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
          "value": 101.15,
          "digits": 5,
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
            "max": 343.15,
            "n_unique": 5
          },
          "range_min": 298.15,
          "range_max": 343.15
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
          "meas_num_id": "GLOBmeas_4",
          "meas_ID": "capillary_tube_ostwald_ubbelohde_method",
          "method_standard": "Capillary tube (Ostwald; Ubbelohde) method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000405,
            "max": 0.005062,
            "mean": 0.00167,
            "std": 0.000952,
            "n": 65
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000405,
          "range_max": 0.005062
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
          "comp_num_id": "GLOBcomp_47",
          "name": "N-methylpyrrolidone",
          "formula": "C5H9NO",
          "inchi_key": "SECXISVLQFMRJM-UHFFFAOYSA-N",
          "SMILES": "CN1CCCC1=O",
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
      "parent_n_datapoints": 65,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8242",
      "block_number": "PROPblock_17",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_47",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity measurements for N-methyl-2-pyrrolidone + water at 298.15–338.15 K, 101.3 kPa, 95 data points, composition as mole fraction of water.",
      "doi": "10.1021/je0340809",
      "lit_id": "2004-geo-sas-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 95,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_47",
          "name": "N-methylpyrrolidone",
          "formula": "C5H9NO",
          "inchi_key": "SECXISVLQFMRJM-UHFFFAOYSA-N",
          "SMILES": "CN1CCCC1=O",
          "sample_num": "DOIcompSample_4_1"
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
          "value": 101.3,
          "digits": 4,
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
            "min": 0.0522,
            "max": 0.99,
            "n_unique": 19
          },
          "range_min": 0.0522,
          "range_max": 0.99
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
            "min": 298.15,
            "max": 338.15,
            "n_unique": 5
          },
          "range_min": 298.15,
          "range_max": 338.15
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
            "min": 0.000467,
            "max": 0.005159,
            "mean": 0.001769,
            "std": 0.000996,
            "n": 95
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000467,
          "range_max": 0.005159
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
          "comp_num_id": "GLOBcomp_47",
          "name": "N-methylpyrrolidone",
          "formula": "C5H9NO",
          "inchi_key": "SECXISVLQFMRJM-UHFFFAOYSA-N",
          "SMILES": "CN1CCCC1=O",
          "sample_num": "DOIcompSample_4_1"
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
      "parent_n_datapoints": 95,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_9372",
      "block_number": "PROPblock_17",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_47",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity measurements for N-methyl-2-pyrrolidone + water at 293.15–323.15 K, 101.0 kPa, 44 data points, composition as mole fraction of NMP.",
      "doi": "10.1021/je100967k",
      "lit_id": "2011-gar-gom-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 44,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_47",
          "name": "N-methylpyrrolidone",
          "formula": "C5H9NO",
          "inchi_key": "SECXISVLQFMRJM-UHFFFAOYSA-N",
          "SMILES": "CN1CCCC1=O",
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
            "max": 323.15,
            "n_unique": 4
          },
          "range_min": 293.15,
          "range_max": 323.15
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
          "meas_num_id": "GLOBmeas_140",
          "meas_ID": "captub_ufactor_2",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:2",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000547,
            "max": 0.006774,
            "mean": 0.002457,
            "std": 0.001385,
            "n": 44
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000547,
          "range_max": 0.006774
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
          "comp_num_id": "GLOBcomp_47",
          "name": "N-methylpyrrolidone",
          "formula": "C5H9NO",
          "inchi_key": "SECXISVLQFMRJM-UHFFFAOYSA-N",
          "SMILES": "CN1CCCC1=O",
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
      "parent_n_datapoints": 44,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1021/je034073k",
      "block_number": "PROPblock_3",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<N-methylpyrrolidone>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<N-methylpyrrolidone>": "0",
          "pressure_kpa": "101.15",
          "viscosity_pa_s": "0.00089"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "298.15",
          "mole_fraction_<N-methylpyrrolidone>": "0.0501",
          "pressure_kpa": "101.15",
          "viscosity_pa_s": "0.00174"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<N-methylpyrrolidone>": "0.0701",
          "pressure_kpa": "101.15",
          "viscosity_pa_s": "0.002137"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "298.15",
          "mole_fraction_<N-methylpyrrolidone>": "0.1001",
          "pressure_kpa": "101.15",
          "viscosity_pa_s": "0.002762"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mole_fraction_<N-methylpyrrolidone>": "0.2004",
          "pressure_kpa": "101.15",
          "viscosity_pa_s": "0.004555"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "mole_fraction_<N-methylpyrrolidone>": "0.3004",
          "pressure_kpa": "101.15",
          "viscosity_pa_s": "0.005062"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "mole_fraction_<N-methylpyrrolidone>": "0.4012",
          "pressure_kpa": "101.15",
          "viscosity_pa_s": "0.004505"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "298.15",
          "mole_fraction_<N-methylpyrrolidone>": "0.503",
          "pressure_kpa": "101.15",
          "viscosity_pa_s": "0.003729"
        }
      ],
      "inspection_id": "INSP_bd9d3e42bc68",
      "lit_num_id": "GLOBlit_8238"
    },
    {
      "doi": "10.1021/je0340809",
      "block_number": "PROPblock_17",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<water>",
        "temperature_k",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<water>": "0.0522",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.001721"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "mole_fraction_<water>": "0.1684",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.001985"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "mole_fraction_<water>": "0.2465",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.002147"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "mole_fraction_<water>": "0.3481",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.002535"
        }
      ],
      "inspection_id": "INSP_8d8303b6d7df",
      "lit_num_id": "GLOBlit_8242"
    },
    {
      "doi": "10.1021/je100967k",
      "block_number": "PROPblock_17",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<N-methylpyrrolidone>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "293.15",
          "mole_fraction_<N-methylpyrrolidone>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0009933"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "293.15",
          "mole_fraction_<N-methylpyrrolidone>": "0.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0033316"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "293.15",
          "mole_fraction_<N-methylpyrrolidone>": "0.2",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0059028"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "293.15",
          "mole_fraction_<N-methylpyrrolidone>": "0.3001",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0067739"
        }
      ],
      "inspection_id": "INSP_e2b42c422e04",
      "lit_num_id": "GLOBlit_9372"
    }
  ]
}