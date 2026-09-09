{
  "answer": "## Binary Methanol + Water Dynamic Viscosity Data Near 298.15 K\n\nThree binary methanol–water dynamic viscosity (GLOBprop_4) data blocks were found in the ThermoML database with measurements at 298.15 K. All blocks report data at a fixed pressure of 101.0 kPa.\n\n---\n\n### Block Summary\n\n| Block | Literature | DOI | Composition Variable | Composition Range | T Range (K) | Viscosity Range (Pa·s) | Total Points | Points at 298.15 K |\n|---|---|---|---|---|---|---|---|---|\n| PROPblock_9 | GLOBlit_2825 | 10.1016/j.jct.2007.05.004 | Mole fraction (water) | 0–1 | 293.15–303.15 | 0.000508–0.001793 | 39 | 13 |\n| PROPblock_3 | GLOBlit_8869 | 10.1021/je0600810 | Volume fraction (methanol) | 0.01–0.3 | 298.15–318.15 | 0.000702–0.0014712 | 9 | 3 |\n| PROPblock_1 | GLOBlit_9571 | 10.1021/je2003622 | Mass fraction (methanol) | 0.0806–0.3446 | 298.15–323.15 | 0.0006375–0.0014712 | 16 | 4 |\n\n---\n\n### Most Comprehensive Block: PROPblock_9 (GLOBlit_2825)\n\n**DOI:** 10.1016/j.jct.2007.05.004  \n**Composition variable:** Mole fraction of water, x(water) = 0 to 1  \n**Full composition coverage at 298.15 K (13 data points, 12 shown by RDP):**\n\n| x(water) | η (Pa·s) |\n|---|---|\n| 0 | 0.000545 |\n| 0.049 | 0.000607 |\n| 0.0993 | 0.000677 |\n| 0.1973 | 0.000821 |\n| 0.2983 | 0.000987 |\n| 0.3985 | 0.00115 |\n| 0.5994 | 0.001463 |\n| 0.6997 | 0.001554 |\n| 0.7986 | 0.001542 |\n| 0.8999 | 0.001317 |\n| 0.9512 | 0.001121 |\n| 1.0 | 0.00089 |\n\nThis block clearly shows the well-known viscosity maximum in the methanol–water system: viscosity rises from pure methanol (0.000545 Pa·s) to a maximum near x(water) ≈ 0.70 (0.001554 Pa·s), then decreases toward pure water (0.00089 Pa·s). The maximum viscosity is several times larger than the pure-component values (derived from the inspected rows: 0.001554 / 0.000545 ≈ 2.9× pure methanol; 0.001554 / 0.00089 ≈ 1.7× pure water), reflecting strong hydrogen-bonding interactions and structural reorganization in the mixture.\n\n---\n\n### PROPblock_3 (GLOBlit_8869) — Data at 298.15 K\n\n**DOI:** 10.1021/je0600810  \n**Composition variable:** Volume fraction of methanol (φ_v)\n\n| φ_v(methanol) | η (Pa·s) |\n|---|---|\n| 0.01 | 0.0010844 |\n| 0.2 | 0.0013106 |\n| 0.3 | 0.0014712 |\n\nCovers only the methanol-dilute region (φ_v = 0.01–0.3).\n\n---\n\n### PROPblock_1 (GLOBlit_9571) — Data at 298.15 K\n\n**DOI:** 10.1021/je2003622  \n**Composition variable:** Mass fraction of methanol (w)\n\n| w(methanol) | η (Pa·s) |\n|---|---|\n| 0.0806 | 0.0010844 |\n| 0.1647 | 0.0013106 |\n| 0.2526 | 0.0014712 |\n| 0.3446 | 0.0014475 |\n\nAlso covers a limited methanol-lean range (w = 0.08–0.34). The slight decrease from w = 0.2526 to 0.3446 is consistent with the viscosity maximum occurring in this composition region.\n\n---\n\n### Recommendation\n\n**PROPblock_9 (GLOBlit_2825, DOI: 10.1016/j.jct.2007.05.004)** is by far the most comprehensive dataset, providing full mole-fraction coverage (0–1) at 298.15 K with 13 data points and clear resolution of the viscosity maximum. The other two blocks cover only narrow methanol-lean composition windows and use volume fraction or mass fraction rather than mole fraction.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNINSPECTED_VALUE** PROPblock_9: 1.7 exists in PROPblock_9's database table but was never shown in an inspection of this run\n  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number=\"GLOBlit_2825::PROPblock_9\", nearest={\"column\": \"temperature_k\", \"value\": 1.7})`\nInspected so far: PROPblock_1, PROPblock_3, PROPblock_9",
  "core_claims": [
    "Three binary methanol–water dynamic viscosity data blocks were found in ThermoML with measurements at 298.15 K, all at a fixed pressure of 101.0 kPa.",
    "PROPblock_9 (DOI: 10.1016/j.jct.2007.05.004) is the most comprehensive dataset, providing 13 data points spanning the full mole-fraction range of water (0 to 1) at 298.15 K.",
    "PROPblock_9 shows the well-known viscosity maximum in the methanol–water system: viscosity rises from pure methanol (0.000545 Pa·s at x(water)=0) to a maximum near x(water) ≈ 0.70 (0.001554 Pa·s), then decreases toward pure water (0.00089 Pa·s at x(water)=1.0).",
    "The other two blocks (PROPblock_3 and PROPblock_1) cover only narrow methanol-lean composition windows using volume fraction (0.01–0.3) and mass fraction (0.0806–0.3446), respectively.",
    "PROPblock_1 data show a slight viscosity decrease from w(methanol)=0.2526 to 0.3446, consistent with the viscosity maximum occurring in that composition region."
  ],
  "status": "success",
  "summary": "Three ThermoML blocks report binary methanol–water dynamic viscosity at 298.15 K and 101.0 kPa. The most comprehensive is PROPblock_9 (GLOBlit_2825, DOI 10.1016/j.jct.2007.05.004), which provides 13 data points spanning the full mole-fraction range of water (0 to 1). At 298.15 K, viscosity rises from pure methanol (0.000545 Pa·s at x(water)=0) to a maximum near x(water)≈0.70 (0.001554 Pa·s), then decreases to pure water (0.00089 Pa·s), illustrating the well-known viscosity maximum due to hydrogen-bonding interactions. PROPblock_3 (GLOBlit_8869, DOI 10.1021/je0600810) reports three points at 298.15 K in volume fraction of methanol (0.01–0.3), with viscosities 0.0010844–0.0014712 Pa·s. PROPblock_1 (GLOBlit_9571, DOI 10.1021/je2003622) reports four points at 298.15 K in mass fraction of methanol (0.0806–0.3446), with viscosities 0.0010844–0.0014712 Pa·s, showing a slight decrease from w=0.2526 to 0.3446 consistent with the viscosity maximum in that region. PROPblock_9 is recommended as the most complete dataset for this system.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2825",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of methanol + water binary mixture at 293.15–303.15 K, mole fraction of water 0–1, 39 total points (13 at 298.15 K). Full composition coverage showing viscosity maximum near x(water) ≈ 0.70.",
      "doi": "10.1016/j.jct.2007.05.004",
      "lit_id": "2007-gon-cal-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 39,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
          "meas_num_id": "GLOBmeas_140",
          "meas_ID": "captub_ufactor_2",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:2",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000508,
            "max": 0.001793,
            "mean": 0.001082,
            "std": 0.000366,
            "n": 39
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000508,
          "range_max": 0.001793
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
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "parent_n_datapoints": 39,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8869",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of methanol + water binary mixture at 298.15–318.15 K, volume fraction of methanol 0.01–0.3, 9 total points (3 at 298.15 K). Limited methanol-dilute region.",
      "doi": "10.1021/je0600810",
      "lit_id": "2006-cha-das-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 9,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
          "var_num_id": "GLOBvar_18",
          "var_id": "volume_fraction_DOIcomp_1",
          "name": "Volume fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_1",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Volume fraction",
            "min": 0.01,
            "max": 0.3,
            "n_unique": 3
          },
          "range_min": 0.01,
          "range_max": 0.3
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
          "meas_num_id": "GLOBmeas_140",
          "meas_ID": "captub_ufactor_2",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:2",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000702,
            "max": 0.001471,
            "mean": 0.001033,
            "std": 0.000248,
            "n": 9
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000702,
          "range_max": 0.001471
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
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "parent_n_datapoints": 9,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_9571",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of methanol + water binary mixture at 298.15–323.15 K, mass fraction of methanol 0.0806–0.3446, 16 total points (4 at 298.15 K). Limited methanol-lean region.",
      "doi": "10.1021/je2003622",
      "lit_id": "2011-bha-cha-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 16,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
            "min": 0.0806,
            "max": 0.3446,
            "n_unique": 4
          },
          "range_min": 0.0806,
          "range_max": 0.3446
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
            "max": 323.15,
            "n_unique": 4
          },
          "range_min": 298.15,
          "range_max": 323.15
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
          "meas_num_id": "GLOBmeas_271",
          "meas_ID": "captub_ufactor_6",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:6",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000638,
            "max": 0.001471,
            "mean": 0.000993,
            "std": 0.000261,
            "n": 16
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000638,
          "range_max": 0.001471
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
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "parent_n_datapoints": 16,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "block_number": "PROPblock_9",
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
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000545"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.049",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000607"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.0993",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000677"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.1973",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000821"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.2983",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000987"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.3985",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00115"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.5994",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001463"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.6997",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001554"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.7986",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001542"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.8999",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001317"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.9512",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001121"
        },
        {
          "BLKpoint_id": "BLKpoint_26",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00089"
        }
      ],
      "inspection_id": "INSP_f99e390ea15c",
      "lit_num_id": "GLOBlit_2825"
    },
    {
      "doi": "10.1021/je0600810",
      "block_number": "PROPblock_3",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "volume_fraction_<methanol>",
        "temperature_k",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "volume_fraction_<methanol>": "0.01",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0010844"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "volume_fraction_<methanol>": "0.2",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0013106"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "volume_fraction_<methanol>": "0.3",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0014712"
        }
      ],
      "inspection_id": "INSP_51feb0d2c046",
      "lit_num_id": "GLOBlit_8869"
    },
    {
      "doi": "10.1021/je2003622",
      "block_number": "PROPblock_1",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "mass_fraction_<methanol>",
        "temperature_k",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mass_fraction_<methanol>": "0.0806",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0010844"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "mass_fraction_<methanol>": "0.1647",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0013106"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mass_fraction_<methanol>": "0.2526",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0014712"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "mass_fraction_<methanol>": "0.3446",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0014475"
        }
      ],
      "inspection_id": "INSP_9b7df612effc",
      "lit_num_id": "GLOBlit_9571"
    }
  ]
}