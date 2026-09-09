{
  "answer": "Here are all the excess molar enthalpy (HE) data blocks found for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system near 298.15 K in the ThermoML database:\n\n## Summary of All HE Blocks Found\n\n| DOI | GLOBlit | Block | Total pts | Pts at 298.15 K | Composition range | Notes |\n|---|---|---|---|---|---|---|\n| 10.1016/j.fluid.2007.06.007 | GLOBlit_528 | PROPblock_1 | 15 | 15 | x(ethanol) 0.000102–0.001551 | Very dilute ethanol in water only |\n| 10.1016/j.fluid.2007.06.007 | GLOBlit_528 | PROPblock_2 | 15 | 15 | x(water) 0.001021–0.015286 | Very dilute water in ethanol only |\n| 10.1016/j.jct.2005.06.018 | GLOBlit_2574 | PROPblock_4 | 27 | 12 | x(ethanol) 0.0582–0.9 | Broad composition coverage; ⚠️ paper title references propanediols/butanediol — possible compound-mapping issue |\n| 10.1016/j.tca.2017.05.023 | GLOBlit_6377 | PROPblock_1 | 1 | 1 | x(ethanol) 0.102 only | Single data point |\n\n## Detailed Findings\n\n### GLOBlit_2574::PROPblock_4 — Best Composition Coverage at 298.15 K\nThis block contains **12 data points at 298.15 K**, spanning x(ethanol) = 0.0582 to 0.9, at 101.0 kPa:\n\n| x(ethanol) | HE (kJ/mol) |\n|---|---|\n| 0.0582 | −0.492 |\n| 0.1198 | −0.747 |\n| 0.15 | −0.77 |\n| 0.1837 | −0.767 |\n| 0.25 | −0.702 |\n| 0.2981 | −0.649 |\n| 0.4127 | −0.501 |\n| 0.5 | −0.391 |\n| 0.607 | −0.323 |\n| 0.701 | −0.271 |\n| 0.812 | −0.206 |\n| 0.9 | −0.148 |\n\nThe minimum HE is −0.77 kJ/mol at x(ethanol) ≈ 0.15, consistent with the well-known asymmetric exothermic mixing curve for ethanol + water. However, note the caution flag: the paper title in the database references propanediols/butanediol rather than ethanol, so this data should be verified against the original publication.\n\n### GLOBlit_6377::PROPblock_1 — Single Point\nDOI: 10.1016/j.tca.2017.05.023. Contains only **1 data point** at 298.15 K: x(ethanol) = 0.102, HE = −0.70659 kJ/mol, at 100 kPa. This is consistent with the GLOBlit_2574::PROPblock_4 data, which gives −0.747 kJ/mol at x = 0.1198 (a nearby but not identical composition).\n\n### GLOBlit_528::PROPblock_1 — Dilute Ethanol in Water\nDOI: 10.1016/j.fluid.2007.06.007. Contains 15 points at 298.15 K covering x(ethanol) = 0.000102–0.001551 at 101.0 kPa. HE ranges from −0.00104 to −0.01537 kJ/mol. This block covers only the very dilute ethanol end, useful for deriving partial molar excess enthalpies at infinite dilution.\n\n### GLOBlit_528::PROPblock_2 — Dilute Water in Ethanol\nSame DOI. Contains 15 points at 298.15 K covering x(water) = 0.001021–0.015286 at 101.0 kPa. HE ranges from −0.00212 to −0.02961 kJ/mol. This block covers only the very dilute water-in-ethanol end.\n\n### Conclusion\nNo additional DOIs beyond GLOBlit_528, GLOBlit_2574, and GLOBlit_6377 were found in the database for HE of ethanol + water. GLOBlit_2574::PROPblock_4 provides the broadest composition coverage with 12 points at 298.15 K spanning x(ethanol) = 0.0582–0.9. The GLOBlit_528 blocks complement this with high-resolution data in the infinite-dilution regions at both ends.",
  "core_claims": [
    "Three DOIs (GLOBlit_528, GLOBlit_2574, GLOBlit_6377) were found in the ThermoML database containing excess molar enthalpy (HE) data for the ethanol + water binary system near 298.15 K.",
    "GLOBlit_2574::PROPblock_4 provides the broadest composition coverage with 12 data points at 298.15 K spanning x(ethanol) = 0.0582–0.9 at 101.0 kPa, showing all-negative HE values with a minimum of −0.77 kJ/mol at x(ethanol) ≈ 0.15, consistent with the known asymmetric exothermic mixing curve for ethanol + water.",
    "A caution flag applies to GLOBlit_2574::PROPblock_4: the paper title in the database references propanediols/butanediol rather than ethanol, so the compound mapping should be verified against the original publication (DOI 10.1016/j.jct.2005.06.018).",
    "GLOBlit_6377::PROPblock_1 provides a single data point at 298.15 K: x(ethanol) = 0.102, HE = −0.70659 kJ/mol at 100 kPa, which is consistent with the GLOBlit_2574 data (−0.747 kJ/mol at x = 0.1198).",
    "GLOBlit_528 (DOI 10.1016/j.fluid.2007.06.007) provides high-resolution HE data in the infinite-dilution regions at both ends: 15 points for dilute ethanol in water (x(ethanol) = 0.000102–0.001551) and 15 points for dilute water in ethanol (x(water) = 0.001021–0.015286), all at 298.15 K and 101.0 kPa."
  ],
  "status": "success",
  "summary": "In the ThermoML database, excess molar enthalpy (HE) data for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system near 298.15 K were found in three sources: GLOBlit_528 (DOI 10.1016/j.fluid.2007.06.007), GLOBlit_2574 (DOI 10.1016/j.jct.2005.06.018), and GLOBlit_6377 (DOI 10.1016/j.tca.2017.05.023). GLOBlit_2574::PROPblock_4 offers the broadest composition coverage with 12 points at 298.15 K and 101.0 kPa spanning x(ethanol) = 0.0582–0.9, showing all-negative HE values with a minimum of −0.77 kJ/mol at x(ethanol) ≈ 0.15, consistent with the known asymmetric exothermic mixing curve; however, the paper title references propanediols/butanediol rather than ethanol, flagging a possible compound-mapping issue. GLOBlit_6377::PROPblock_1 provides a single point at 298.15 K (x(ethanol) = 0.102, HE = −0.70659 kJ/mol, 100 kPa), consistent with the GLOBlit_2574 data. GLOBlit_528 contains two blocks of 15 points each at 298.15 K and 101.0 kPa covering the infinite-dilution regions: PROPblock_1 for very dilute ethanol in water (x(ethanol) = 0.000102–0.001551, HE from −0.00104 to −0.01537 kJ/mol) and PROPblock_2 for very dilute water in ethanol (x(water) = 0.001021–0.015286, HE from −0.00212 to −0.02961 kJ/mol). No other DOIs were found for this system and property.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_6377",
      "registry_id": "2017-mod-kow-0",
      "name": "10.1016/j.tca.2017.05.023"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_528",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_17"
      ],
      "description": "Excess molar enthalpy for dilute ethanol in water at 298.15 K; 15 points, x(ethanol) 0.000102–0.001551.",
      "doi": "10.1016/j.fluid.2007.06.007",
      "lit_id": "2007-li-yan-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 15,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_7",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_7_1"
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
          "constr_num_id": "GLOBconstr_2",
          "constr_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "value": 298.15,
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
          "var_id": "mole_fraction_DOIcomp_7",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_7",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Mole fraction",
            "min": 0.000102,
            "max": 0.001551,
            "n_unique": 15
          },
          "range_min": 0.000102,
          "range_max": 0.001551
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_17",
          "prop_ID": "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol",
          "name": "Excess molar enthalpy (molar enthalpy of mixing), kJ/mol",
          "group": "ExcessPartialApparentEnergyProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_13",
          "meas_ID": "calvet_calorimetry",
          "method_standard": "Calvet calorimetry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Excess molar enthalpy (molar enthalpy of mixing), kJ/mol",
            "min": -0.01537,
            "max": -0.00104,
            "mean": -0.008237,
            "std": 0.004575,
            "n": 15
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -0.01537,
          "range_max": -0.00104
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
          "org_num": "DOIcomp_7",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_7_1"
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
      "parent_n_datapoints": 15,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_528",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_17"
      ],
      "description": "Excess molar enthalpy for dilute water in ethanol at 298.15 K; 15 points, x(water) 0.001021–0.015286.",
      "doi": "10.1016/j.fluid.2007.06.007",
      "lit_id": "2007-li-yan-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 15,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_7",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_7_1"
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
          "constr_num_id": "GLOBconstr_2",
          "constr_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "value": 298.15,
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
          "var_id": "mole_fraction_DOIcomp_6",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_6",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Mole fraction",
            "min": 0.001021,
            "max": 0.015286,
            "n_unique": 15
          },
          "range_min": 0.001021,
          "range_max": 0.015286
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_17",
          "prop_ID": "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol",
          "name": "Excess molar enthalpy (molar enthalpy of mixing), kJ/mol",
          "group": "ExcessPartialApparentEnergyProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_13",
          "meas_ID": "calvet_calorimetry",
          "method_standard": "Calvet calorimetry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Excess molar enthalpy (molar enthalpy of mixing), kJ/mol",
            "min": -0.02961,
            "max": -0.00212,
            "mean": -0.016162,
            "std": 0.008775,
            "n": 15
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -0.02961,
          "range_max": -0.00212
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
          "org_num": "DOIcomp_7",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_7_1"
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
      "parent_n_datapoints": 15,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2574",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_17"
      ],
      "description": "Excess molar enthalpy for ethanol + water; 12 points at 298.15 K spanning x(ethanol) 0.0582–0.9 at 101.0 kPa. Broadest composition coverage found.",
      "doi": "10.1016/j.jct.2005.06.018",
      "lit_id": "2006-nag-fra-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 27,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_5_1"
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
            "min": 298.15,
            "max": 323.15,
            "n_unique": 2
          },
          "range_min": 298.15,
          "range_max": 323.15
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
            "min": 0.033,
            "max": 0.968,
            "n_unique": 27
          },
          "range_min": 0.033,
          "range_max": 0.968
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_17",
          "prop_ID": "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol",
          "name": "Excess molar enthalpy (molar enthalpy of mixing), kJ/mol",
          "group": "ExcessPartialApparentEnergyProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_169",
          "meas_ID": "calvet_ufactor_2",
          "method_standard": null,
          "method_custom": "CALVET:UFactor:2",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Excess molar enthalpy (molar enthalpy of mixing), kJ/mol",
            "min": -0.77,
            "max": -0.018,
            "mean": -0.325074,
            "std": 0.241185,
            "n": 27
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -0.77,
          "range_max": -0.018
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
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_5_1"
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
      "parent_n_datapoints": 27,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_6377",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_17"
      ],
      "description": "Excess molar enthalpy for ethanol + water; single data point at 298.15 K, x(ethanol) = 0.102, HE = −0.70659 kJ/mol at 100 kPa.",
      "doi": "10.1016/j.tca.2017.05.023",
      "lit_id": "2017-mod-kow-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 1,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
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
      "constraints": [],
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
            "min": 0.102,
            "max": 0.102,
            "n_unique": 1
          },
          "range_min": 0.102,
          "range_max": 0.102
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_3",
          "var_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Pressure, kPa",
            "min": 100.0,
            "max": 100.0,
            "n_unique": 1
          },
          "range_min": 100.0,
          "range_max": 100.0
        },
        {
          "BLKvar_id": "BLKvar_3",
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
            "BLKvar_id": "BLKvar_3",
            "name": "Temperature, K",
            "min": 298.15,
            "max": 298.15,
            "n_unique": 1
          },
          "range_min": 298.15,
          "range_max": 298.15
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_17",
          "prop_ID": "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol",
          "name": "Excess molar enthalpy (molar enthalpy of mixing), kJ/mol",
          "group": "ExcessPartialApparentEnergyProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_12",
          "meas_ID": "flow_calorimetry",
          "method_standard": "Flow calorimetry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Excess molar enthalpy (molar enthalpy of mixing), kJ/mol",
            "min": -0.70659,
            "max": -0.70659,
            "mean": -0.70659,
            "std": 0,
            "n": 1
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -0.70659,
          "range_max": -0.70659
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
          "owner_id": "BLKvar_3",
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
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
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
      "parent_n_datapoints": 1,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2005.06.018",
      "block_number": "PROPblock_4",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<ethanol>",
        "pressure_kpa",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.0582",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.492"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.1198",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.747"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.77"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.1837",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.767"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.25",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.702"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.2981",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.649"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.4127",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.501"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.5",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.391"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.607",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.323"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.701",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.271"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.812",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.206"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.9",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.148"
        }
      ],
      "inspection_id": "INSP_6d19d0a7d0d6",
      "lit_num_id": "GLOBlit_2574"
    },
    {
      "doi": "10.1016/j.tca.2017.05.023",
      "block_number": "PROPblock_1",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<ethanol>",
        "pressure_kpa",
        "temperature_k",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<ethanol>": "0.102",
          "pressure_kpa": "100",
          "temperature_k": "298.15",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.70659"
        }
      ],
      "inspection_id": "INSP_b04400bcb35b",
      "lit_num_id": "GLOBlit_6377"
    },
    {
      "doi": "10.1016/j.fluid.2007.06.007",
      "block_number": "PROPblock_1",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<ethanol>",
        "temperature_k",
        "pressure_kpa",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<ethanol>": "0.000102",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00104"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "mole_fraction_<ethanol>": "0.000206",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00208"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "mole_fraction_<ethanol>": "0.000308",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00312"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "mole_fraction_<ethanol>": "0.000516",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00518"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "mole_fraction_<ethanol>": "0.000619",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00621"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "mole_fraction_<ethanol>": "0.000723",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00722"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mole_fraction_<ethanol>": "0.000827",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00826"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mole_fraction_<ethanol>": "0.000931",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00927"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "mole_fraction_<ethanol>": "0.001034",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.0103"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "mole_fraction_<ethanol>": "0.001241",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01233"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "mole_fraction_<ethanol>": "0.001345",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01334"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "mole_fraction_<ethanol>": "0.001551",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01537"
        }
      ],
      "inspection_id": "INSP_e0e7d5bc600c",
      "lit_num_id": "GLOBlit_528"
    },
    {
      "doi": "10.1016/j.fluid.2007.06.007",
      "block_number": "PROPblock_2",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "mole_fraction_<water>",
        "temperature_k",
        "pressure_kpa",
        "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mole_fraction_<water>": "0.001021",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00212"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "mole_fraction_<water>": "0.00205",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00424"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mole_fraction_<water>": "0.004102",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.00835"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "mole_fraction_<water>": "0.006155",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01238"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "mole_fraction_<water>": "0.007179",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.01437"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "mole_fraction_<water>": "0.010239",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02023"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "mole_fraction_<water>": "0.011252",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02213"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "mole_fraction_<water>": "0.012264",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02405"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "mole_fraction_<water>": "0.013276",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.0259"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "mole_fraction_<water>": "0.014283",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02777"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "mole_fraction_<water>": "0.015286",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.02961"
        }
      ],
      "inspection_id": "INSP_b146b18bf0c3",
      "lit_num_id": "GLOBlit_528"
    }
  ]
}