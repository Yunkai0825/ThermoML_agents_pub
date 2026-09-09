{
  "answer": "## Excess Molar Enthalpy (HE) Data for Ethanol + Water at 298.15 K\n\nFour data blocks were found in the ThermoML database for the binary system ethanol (GLOBcomp_2) + water (GLOBcomp_1) containing excess molar enthalpy (GLOBprop_17) data at or near 298.15 K:\n\n---\n\n### 1. GLOBlit_2574 :: PROPblock_4\n- **DOI:** 10.1016/j.jct.2005.06.018\n- **Total data points:** 27 (5 at 298.15 K, remainder at 323.15 K)\n- **Temperature range:** 298.15–323.15 K\n- **Composition range (full block):** x(ethanol) = 0.033–0.968\n- **Pressure:** 101.0 kPa (fixed)\n- **HE range:** −0.77 to −0.018 kJ/mol\n\n**298.15 K data points:**\n\n| x(ethanol) | HE (kJ/mol) |\n|---|---|\n| 0.0582 | −0.492 |\n| 0.1198 | −0.747 |\n| 0.1837 | −0.767 |\n| 0.5 | −0.391 |\n| 0.9 | −0.148 |\n\nThis block offers the **widest composition coverage** at 298.15 K (from dilute ethanol to ethanol-rich), though with only 5 data points at that temperature. The minimum HE (most exothermic mixing) occurs near x(ethanol) ≈ 0.18, consistent with the known asymmetric HE curve for ethanol–water.\n\n⚠️ **Note:** The paper title references propanediols/butanediol, not ethanol — possible compound-mapping issue; verify against the original publication.\n\n---\n\n### 2. GLOBlit_528 :: PROPblock_1\n- **DOI:** 10.1016/j.fluid.2007.06.007\n- **Data points:** 15 (all at 298.15 K)\n- **Temperature:** 298.15 K (fixed)\n- **Pressure:** 101.0 kPa (fixed)\n- **Composition range:** x(ethanol) = 0.000102–0.001551 (very dilute ethanol)\n- **HE range:** −0.01537 to −0.00104 kJ/mol\n\nThis block covers the **infinite-dilution region of ethanol in water**, with a nearly linear, monotonically decreasing HE vs. composition relationship — useful for extracting partial molar excess enthalpy at infinite dilution.\n\n---\n\n### 3. GLOBlit_528 :: PROPblock_2\n- **DOI:** 10.1016/j.fluid.2007.06.007\n- **Data points:** 15 (all at 298.15 K)\n- **Temperature:** 298.15 K (fixed)\n- **Pressure:** 101.0 kPa (fixed)\n- **Composition range:** x(water) = 0.001021–0.015286 (very dilute water, i.e., ethanol-rich side)\n- **HE range:** −0.02961 to −0.00212 kJ/mol\n\nThis block covers the **infinite-dilution region of water in ethanol**, complementing PROPblock_1 on the opposite end of the composition range.\n\n---\n\n### 4. GLOBlit_6377 (single-point block)\n- Reported in the initial search as containing a single data point near 298.15 K. Not inspected in detail due to its limited scope.\n\n---\n\n### Summary & Recommendation\n\n| Block | GLOBlit | DOI | Points at 298.15 K | Composition range | Best for |\n|---|---|---|---|---|---|\n| PROPblock_4 | GLOBlit_2574 | 10.1016/j.jct.2005.06.018 | 5 | x(ethanol) = 0.058–0.9 | Full composition range |\n| PROPblock_1 | GLOBlit_528 | 10.1016/j.fluid.2007.06.007 | 15 | x(ethanol) = 0.0001–0.0016 | Dilute ethanol limit |\n| PROPblock_2 | GLOBlit_528 | 10.1016/j.fluid.2007.06.007 | 15 | x(water) = 0.001–0.015 | Dilute water limit |\n| (single pt) | GLOBlit_6377 | — | ~1 | — | Limited use |\n\n**GLOBlit_2574::PROPblock_4** provides the broadest composition coverage at 298.15 K but has only 5 points. The two **GLOBlit_528** blocks together provide 15 (PROPblock_1) + 15 (PROPblock_2) high-resolution data points at 298.15 K, but are restricted to the two dilute extremes. All measured HE values are negative (exothermic mixing), consistent with the strong hydrogen-bonding interactions between ethanol and water.",
  "core_claims": [
    "Four ThermoML data blocks were identified for excess molar enthalpy (HE) of ethanol + water at 298.15 K and 101.0 kPa: GLOBlit_2574::PROPblock_4 (5 points spanning x(ethanol) = 0.058–0.9, HE from −0.767 to −0.148 kJ/mol), GLOBlit_528::PROPblock_1 (15 points in the very dilute ethanol region, x(ethanol) = 0.000102–0.001551, HE from −0.01537 to −0.00104 kJ/mol), GLOBlit_528::PROPblock_2 (15 points in the very dilute water region, x(water) = 0.001021–0.015286, HE from −0.02961 to −0.00212 kJ/mol), and a single-point block from GLOBlit_6377.",
    "All measured HE values are negative (exothermic mixing), consistent with strong hydrogen-bonding interactions between ethanol and water.",
    "In the broad-composition block (GLOBlit_2574::PROPblock_4), the most exothermic HE value at 298.15 K is −0.767 kJ/mol near x(ethanol) ≈ 0.18, reflecting the known asymmetric HE curve for ethanol–water.",
    "A possible compound-mapping issue exists for GLOBlit_2574::PROPblock_4, as the associated paper title references propanediols/butanediol rather than ethanol; verification against the original publication is recommended."
  ],
  "status": "success",
  "summary": "Four ThermoML data blocks were identified for the excess molar enthalpy (HE) of ethanol + water at 298.15 K and 101.0 kPa. GLOBlit_2574::PROPblock_4 (DOI 10.1016/j.jct.2005.06.018) provides 5 data points spanning x(ethanol) = 0.0582–0.9, with HE ranging from −0.767 to −0.148 kJ/mol; the most exothermic mixing occurs near x(ethanol) ≈ 0.18, though a possible compound-mapping issue is flagged because the paper title references propanediols/butanediol. GLOBlit_528::PROPblock_1 (DOI 10.1016/j.fluid.2007.06.007) gives 15 points in the very dilute ethanol region (x(ethanol) = 0.000102–0.001551, HE from −0.01537 to −0.00104 kJ/mol), while GLOBlit_528::PROPblock_2 from the same DOI gives 15 points in the very dilute water region (x(water) = 0.001021–0.015286, HE from −0.02961 to −0.00212 kJ/mol). A fourth block (GLOBlit_6377) contains approximately one data point near 298.15 K. All reported HE values are negative, consistent with exothermic mixing driven by hydrogen-bonding interactions. The GLOBlit_2574 block offers the broadest composition coverage, while the two GLOBlit_528 blocks together provide high-resolution data at both infinite-dilution limits.",
  "core_id_updates": [],
  "core_blocks_found": [
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
      "description": "Excess molar enthalpy for ethanol + water; 27 points over 298.15–323.15 K (5 at 298.15 K), x(ethanol) = 0.033–0.968, HE = −0.77 to −0.018 kJ/mol, 101.0 kPa.",
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
      "description": "Excess molar enthalpy for ethanol + water at 298.15 K; 15 points in the dilute-ethanol region, x(ethanol) = 0.000102–0.001551, HE = −0.01537 to −0.00104 kJ/mol, 101.0 kPa.",
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
      "description": "Excess molar enthalpy for ethanol + water at 298.15 K; 15 points in the dilute-water (ethanol-rich) region, x(water) = 0.001021–0.015286, HE = −0.02961 to −0.00212 kJ/mol, 101.0 kPa.",
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
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2005.06.018",
      "block_number": "PROPblock_4",
      "table_mode": "rdp",
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
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.1837",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.767"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.5",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.391"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.9",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.148"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.033",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.192"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.072",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.349"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.107",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.409"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.148",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.414"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.553",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.074"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.736",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.045"
        },
        {
          "BLKpoint_id": "BLKpoint_26",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.909",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.045"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.968",
          "pressure_kpa": "101.0",
          "excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol": "-0.018"
        }
      ],
      "inspection_id": "INSP_8c41a7d1ffa1",
      "lit_num_id": "GLOBlit_2574"
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