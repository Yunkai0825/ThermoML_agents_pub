{
  "answer": "## Binary Ethanol + Water Mass Density Blocks at Atmospheric Pressure\n\n### Best Candidate: GLOBlit_220 :: PROPblock_2\n**DOI:** 10.1016/j.fluid.2004.11.019\n\nThis block is the strongest match for wide-composition, multi-temperature density data at atmospheric pressure:\n\n- **Total points:** 810 (162 at atmospheric pressure, P = 100 kPa)\n- **Temperatures:** 298.15, 323.15, and 348.15 K (three isotherms)\n- **Composition range:** x(ethanol) = 0.003–1.0 (full range)\n- **Density range (at 100 kPa):** 739.4–995.3 kg/m³\n\nRepresentative atmospheric-pressure data (from inspection):\n\n| T (K) | x(ethanol) | ρ (kg/m³) |\n|--------|-----------|-----------|\n| 298.15 | 0.003 | 995.3 |\n| 298.15 | 0.2502 | 918.5 |\n| 298.15 | 0.4501 | 868.8 |\n| 298.15 | 0.6967 | 825.2 |\n| 298.15 | 1.0 | 785.7 |\n| 323.15 | 0.003 | 986.5 |\n| 323.15 | 0.2269 | 905.2 |\n| 323.15 | 0.4501 | 846.7 |\n| 323.15 | 0.6967 | 802.8 |\n| 323.15 | 1.0 | 763.7 |\n| 348.15 | 0.003 | 973.1 |\n| 348.15 | 0.1903 | 895.8 |\n| 348.15 | 0.4034 | 833.4 |\n| 348.15 | 0.6489 | 785.6 |\n| 348.15 | 1.0 | 739.4 |\n\nEach isotherm has approximately 54 composition points (derived by dividing 162 atmospheric points by 3 isotherms — not a database value), providing dense composition coverage ideal for Redlich-Kister fitting.\n\n### Other Inspected Candidates\n\n**GLOBlit_5201 :: PROPblock_19** (DOI: 10.1016/j.jct.2018.02.022)\n- **Points:** 244, all at P = 92.3 kPa (near-atmospheric)\n- **Temperature:** 293.15–308.15 K (4 isotherms)\n- **Composition:** x(ethanol) = 0–1 (full range)\n- **Density:** 776.592–998.429 kg/m³\n- Excellent composition coverage but temperature range is narrower and lower than GLOBlit_220.\n\n**GLOBlit_2825 :: PROPblock_12** (DOI: 10.1016/j.jct.2007.05.004)\n- **Points:** 37, all at P = 101.0 kPa\n- **Temperature:** 293.15–303.15 K (3 isotherms)\n- **Composition:** x(water) = 0–1 (full range)\n- **Density:** 781.15–998.2 kg/m³\n- Full composition range at atmospheric pressure, but fewer points and lower temperatures.\n\n### Additional Candidates (Not Inspected)\n\nThe following blocks were identified by the search discovery tool but have not been individually inspected in this run. No specific data values are quoted for them:\n\n- **GLOBlit_9006 :: PROPblock_1** (DOI: 10.1021/je060335h) — search-reported as having full composition range at lower temperatures.\n- **GLOBlit_10866 :: PROPblock_7** (DOI: 10.1021/je700300y) — search-reported as having wide composition range.\n- **GLOBlit_10699 :: PROPblock_6** (DOI: 10.1021/je600565m) — search-reported as having moderate composition range.\n- **GLOBlit_11136 :: PROPblock_9** (DOI: 10.1021/je800150h) — search-reported as having partial composition range.\n- **GLOBlit_5473 :: PROPblock_21** (DOI: 10.1016/j.jct.2019.02.027) — search-reported as having full composition range with very few points.\n\n### Regarding GLOBlit_2432\n**DOI:** 10.1016/j.jct.2004.07.019, PROPblock_2 — Per search discovery results (not individually inspected), this block operates at elevated pressures, not atmospheric. **Not suitable** for atmospheric-pressure fitting.\n\n### Key Finding\n**No block in the database was found to cover the requested upper temperature of 353 K (instruction target, not a database value) at atmospheric pressure** for this binary system. The closest inspected data is GLOBlit_220 at 348.15 K. Per search discovery results (not inspected), GLOBlit_1742 (PROPblock_3) reaches higher temperatures but only at elevated pressures.\n\n**Recommendation:** GLOBlit_220 :: PROPblock_2 is the best single source — it provides dense composition coverage at 100 kPa across 298.15, 323.15, and 348.15 K, with x(ethanol) = 0.003–1.0. GLOBlit_5201 :: PROPblock_19 (244 pts, x = 0–1, T = 293.15–308.15 K, P = 92.3 kPa) could supplement with additional near-ambient data.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNGROUNDED_LITERAL** GLOBlit_220::PROPblock_2: 54 (near '…Each isotherm has approximately 54 composition points (deriv…') matches no inspected row/stat, database table, or other source of GLOBlit_220::PROPblock_2\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_220::PROPblock_2\", nearest={\"column\": \"temperature_k\", \"value\": 54.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** PROPblock_2: 353 (near '…abase was found to cover the requested upper temperature of …') matches no inspected row/stat, database table, or other source of PROPblock_2\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_2\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 353.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\nInspected so far: PROPblock_12, PROPblock_19, PROPblock_2",
  "core_claims": [
    "GLOBlit_220 :: PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019) is identified as the best single source for binary ethanol + water mass density data at atmospheric pressure, providing 162 points at P = 100 kPa across three isotherms (298.15, 323.15, and 348.15 K) with x(ethanol) = 0.003–1.0 and densities ranging from 739.4–995.3 kg/m³.",
    "At each isotherm in GLOBlit_220 :: PROPblock_2, density decreases monotonically with increasing ethanol mole fraction at 100 kPa, and density decreases with increasing temperature at fixed composition.",
    "GLOBlit_5201 :: PROPblock_19 (DOI: 10.1016/j.jct.2018.02.022) provides a supplementary 244-point dataset at P = 92.3 kPa over T = 293.15–308.15 K with x(ethanol) = 0–1 and densities of 776.592–998.429 kg/m³, but covers a narrower and lower temperature range than GLOBlit_220.",
    "No block in the database was found to cover 353 K at atmospheric pressure for this binary system; the closest inspected atmospheric-pressure data reaches 348.15 K (GLOBlit_220). The value 353 K is identified as an instruction target, not a database value.",
    "The stated count of approximately 54 composition points per isotherm in GLOBlit_220 :: PROPblock_2 is derived by dividing 162 atmospheric points by 3 isotherms and is flagged as UNVERIFIED against the database."
  ],
  "status": "success",
  "summary": "For binary ethanol + water mass density at atmospheric pressure, the best ThermoML source identified is GLOBlit_220 :: PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019), providing 162 atmospheric-pressure points (P = 100 kPa) across three isotherms (298.15, 323.15, and 348.15 K) with x(ethanol) = 0.003–1.0 and densities from 739.4 to 995.3 kg/m³. A supplementary source is GLOBlit_5201 :: PROPblock_19 (DOI: 10.1016/j.jct.2018.02.022) with 244 points at P = 92.3 kPa, four isotherms from 293.15 to 308.15 K, x(ethanol) = 0–1, and densities 776.592–998.429 kg/m³. GLOBlit_2825 :: PROPblock_12 (DOI: 10.1016/j.jct.2007.05.004) offers 37 points at 101.0 kPa, 293.15–303.15 K, x(water) = 0–1, densities 781.15–998.2 kg/m³. No inspected block reaches the upper target temperature of 353 K at atmospheric pressure; the highest verified atmospheric-pressure isotherm is 348.15 K in GLOBlit_220.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_220",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary ethanol + water at 100 kPa across 298.15–348.15 K, x(ethanol) = 0.003–1.0, 162 atmospheric-pressure points from 810 total.",
      "doi": "10.1016/j.fluid.2004.11.019",
      "lit_id": "2005-pec-dol-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 810,
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
            "max": 348.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 348.15
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
            "max": 40000.0,
            "n_unique": 5
          },
          "range_min": 100.0,
          "range_max": 40000.0
        },
        {
          "BLKvar_id": "BLKvar_3",
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
            "BLKvar_id": "BLKvar_3",
            "name": "Mole fraction",
            "min": 0.003,
            "max": 1.0,
            "n_unique": 54
          },
          "range_min": 0.003,
          "range_max": 1.0
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
          "meas_num_id": "GLOBmeas_138",
          "meas_ID": "vibtub_ufactor_2",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:2",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 739.4,
            "max": 1012.7,
            "mean": 923.644444,
            "std": 66.683257,
            "n": 810
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 739.4,
          "range_max": 1012.7
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
      "parent_n_datapoints": 810,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_19",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary ethanol + water at 92.3 kPa across 293.15–308.15 K, x(ethanol) = 0–1, 244 points.",
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_id": "2018-hog-tor-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 244,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_1_1"
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
            "n_unique": 59
          },
          "range_min": 0.0,
          "range_max": 1.0
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
          "meas_num_id": "GLOBmeas_2",
          "meas_ID": "vibrating_tube_method",
          "method_standard": "Vibrating tube method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 776.592,
            "max": 998.429,
            "mean": 881.16518,
            "std": 74.568443,
            "n": 244
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 776.592,
          "range_max": 998.429
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
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 244,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2825",
      "block_number": "PROPblock_12",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary ethanol + water at 101.0 kPa across 293.15–303.15 K, x(water) = 0–1, 37 points.",
      "doi": "10.1016/j.jct.2007.05.004",
      "lit_id": "2007-gon-cal-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 37,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
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
            "min": 781.15,
            "max": 998.2,
            "mean": 875.231351,
            "std": 74.42608,
            "n": 37
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 781.15,
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
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
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
      "parent_n_datapoints": 37,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.fluid.2004.11.019",
      "block_number": "PROPblock_2",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "pressure_kpa",
        "mole_fraction_<ethanol>",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "995.3"
        },
        {
          "BLKpoint_id": "BLKpoint_43",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "868.8"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "825.2"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "785.7"
        },
        {
          "BLKpoint_id": "BLKpoint_55",
          "temperature_k": "298.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "999.8"
        },
        {
          "BLKpoint_id": "BLKpoint_97",
          "temperature_k": "298.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "874.7"
        },
        {
          "BLKpoint_id": "BLKpoint_102",
          "temperature_k": "298.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "832.3"
        },
        {
          "BLKpoint_id": "BLKpoint_108",
          "temperature_k": "298.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "794"
        },
        {
          "BLKpoint_id": "BLKpoint_109",
          "temperature_k": "298.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "1004.2"
        },
        {
          "BLKpoint_id": "BLKpoint_151",
          "temperature_k": "298.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "880.4"
        },
        {
          "BLKpoint_id": "BLKpoint_156",
          "temperature_k": "298.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "839"
        },
        {
          "BLKpoint_id": "BLKpoint_162",
          "temperature_k": "298.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "801.9"
        },
        {
          "BLKpoint_id": "BLKpoint_163",
          "temperature_k": "298.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "1008.5"
        },
        {
          "BLKpoint_id": "BLKpoint_199",
          "temperature_k": "298.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "938.7"
        },
        {
          "BLKpoint_id": "BLKpoint_205",
          "temperature_k": "298.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "885.7"
        },
        {
          "BLKpoint_id": "BLKpoint_210",
          "temperature_k": "298.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "845.1"
        },
        {
          "BLKpoint_id": "BLKpoint_216",
          "temperature_k": "298.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "808.9"
        },
        {
          "BLKpoint_id": "BLKpoint_217",
          "temperature_k": "298.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "1012.7"
        },
        {
          "BLKpoint_id": "BLKpoint_253",
          "temperature_k": "298.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "942.9"
        },
        {
          "BLKpoint_id": "BLKpoint_259",
          "temperature_k": "298.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "890.8"
        },
        {
          "BLKpoint_id": "BLKpoint_264",
          "temperature_k": "298.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "851"
        },
        {
          "BLKpoint_id": "BLKpoint_270",
          "temperature_k": "298.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "815.7"
        },
        {
          "BLKpoint_id": "BLKpoint_271",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "986.5"
        },
        {
          "BLKpoint_id": "BLKpoint_307",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "905.2"
        },
        {
          "BLKpoint_id": "BLKpoint_313",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "846.7"
        },
        {
          "BLKpoint_id": "BLKpoint_318",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "802.8"
        },
        {
          "BLKpoint_id": "BLKpoint_324",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "763.7"
        },
        {
          "BLKpoint_id": "BLKpoint_325",
          "temperature_k": "323.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "990.8"
        },
        {
          "BLKpoint_id": "BLKpoint_361",
          "temperature_k": "323.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "910.3"
        },
        {
          "BLKpoint_id": "BLKpoint_367",
          "temperature_k": "323.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "853.3"
        },
        {
          "BLKpoint_id": "BLKpoint_372",
          "temperature_k": "323.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "810.9"
        },
        {
          "BLKpoint_id": "BLKpoint_378",
          "temperature_k": "323.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "773.4"
        },
        {
          "BLKpoint_id": "BLKpoint_379",
          "temperature_k": "323.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "994.9"
        },
        {
          "BLKpoint_id": "BLKpoint_415",
          "temperature_k": "323.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "915.3"
        },
        {
          "BLKpoint_id": "BLKpoint_421",
          "temperature_k": "323.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "859.7"
        },
        {
          "BLKpoint_id": "BLKpoint_426",
          "temperature_k": "323.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "818.4"
        },
        {
          "BLKpoint_id": "BLKpoint_432",
          "temperature_k": "323.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "782.3"
        },
        {
          "BLKpoint_id": "BLKpoint_433",
          "temperature_k": "323.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "999"
        },
        {
          "BLKpoint_id": "BLKpoint_469",
          "temperature_k": "323.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "920.1"
        },
        {
          "BLKpoint_id": "BLKpoint_475",
          "temperature_k": "323.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "865.7"
        },
        {
          "BLKpoint_id": "BLKpoint_480",
          "temperature_k": "323.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "825.4"
        },
        {
          "BLKpoint_id": "BLKpoint_486",
          "temperature_k": "323.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "790.3"
        },
        {
          "BLKpoint_id": "BLKpoint_487",
          "temperature_k": "323.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "1003.1"
        },
        {
          "BLKpoint_id": "BLKpoint_523",
          "temperature_k": "323.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "924.7"
        },
        {
          "BLKpoint_id": "BLKpoint_529",
          "temperature_k": "323.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "871.3"
        },
        {
          "BLKpoint_id": "BLKpoint_534",
          "temperature_k": "323.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "831.9"
        },
        {
          "BLKpoint_id": "BLKpoint_540",
          "temperature_k": "323.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "797.7"
        },
        {
          "BLKpoint_id": "BLKpoint_541",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "973.1"
        },
        {
          "BLKpoint_id": "BLKpoint_575",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.1903",
          "mass_density_kg_m3": "895.8"
        },
        {
          "BLKpoint_id": "BLKpoint_582",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.4034",
          "mass_density_kg_m3": "833.4"
        },
        {
          "BLKpoint_id": "BLKpoint_587",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.6489",
          "mass_density_kg_m3": "785.6"
        },
        {
          "BLKpoint_id": "BLKpoint_594",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "739.4"
        },
        {
          "BLKpoint_id": "BLKpoint_595",
          "temperature_k": "348.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "977.5"
        },
        {
          "BLKpoint_id": "BLKpoint_630",
          "temperature_k": "348.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.1996",
          "mass_density_kg_m3": "898.1"
        },
        {
          "BLKpoint_id": "BLKpoint_636",
          "temperature_k": "348.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.4034",
          "mass_density_kg_m3": "840.7"
        },
        {
          "BLKpoint_id": "BLKpoint_641",
          "temperature_k": "348.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "0.6489",
          "mass_density_kg_m3": "794.6"
        },
        {
          "BLKpoint_id": "BLKpoint_648",
          "temperature_k": "348.15",
          "pressure_kpa": "10000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "751.2"
        },
        {
          "BLKpoint_id": "BLKpoint_649",
          "temperature_k": "348.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "981.9"
        },
        {
          "BLKpoint_id": "BLKpoint_683",
          "temperature_k": "348.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.1903",
          "mass_density_kg_m3": "906.5"
        },
        {
          "BLKpoint_id": "BLKpoint_690",
          "temperature_k": "348.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.4034",
          "mass_density_kg_m3": "847.5"
        },
        {
          "BLKpoint_id": "BLKpoint_695",
          "temperature_k": "348.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "0.6489",
          "mass_density_kg_m3": "802.9"
        },
        {
          "BLKpoint_id": "BLKpoint_702",
          "temperature_k": "348.15",
          "pressure_kpa": "20000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "761.2"
        },
        {
          "BLKpoint_id": "BLKpoint_703",
          "temperature_k": "348.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "986.1"
        },
        {
          "BLKpoint_id": "BLKpoint_738",
          "temperature_k": "348.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.1996",
          "mass_density_kg_m3": "908.5"
        },
        {
          "BLKpoint_id": "BLKpoint_744",
          "temperature_k": "348.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.4034",
          "mass_density_kg_m3": "854"
        },
        {
          "BLKpoint_id": "BLKpoint_749",
          "temperature_k": "348.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "0.6489",
          "mass_density_kg_m3": "810.6"
        },
        {
          "BLKpoint_id": "BLKpoint_756",
          "temperature_k": "348.15",
          "pressure_kpa": "30000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "770.3"
        },
        {
          "BLKpoint_id": "BLKpoint_757",
          "temperature_k": "348.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "990.1"
        },
        {
          "BLKpoint_id": "BLKpoint_791",
          "temperature_k": "348.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.1903",
          "mass_density_kg_m3": "916.4"
        },
        {
          "BLKpoint_id": "BLKpoint_798",
          "temperature_k": "348.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.4034",
          "mass_density_kg_m3": "860"
        },
        {
          "BLKpoint_id": "BLKpoint_803",
          "temperature_k": "348.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "0.6489",
          "mass_density_kg_m3": "817.8"
        },
        {
          "BLKpoint_id": "BLKpoint_810",
          "temperature_k": "348.15",
          "pressure_kpa": "40000",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "778.6"
        }
      ],
      "inspection_id": "INSP_38392edfd29c",
      "lit_num_id": "GLOBlit_220"
    },
    {
      "doi": "10.1016/j.fluid.2004.11.019",
      "block_number": "PROPblock_2",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "pressure_kpa",
        "mole_fraction_<ethanol>",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "995.3"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.2502",
          "mass_density_kg_m3": "918.5"
        },
        {
          "BLKpoint_id": "BLKpoint_43",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "868.8"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "825.2"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "785.7"
        },
        {
          "BLKpoint_id": "BLKpoint_271",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "986.5"
        },
        {
          "BLKpoint_id": "BLKpoint_307",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.2269",
          "mass_density_kg_m3": "905.2"
        },
        {
          "BLKpoint_id": "BLKpoint_313",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "846.7"
        },
        {
          "BLKpoint_id": "BLKpoint_318",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "802.8"
        },
        {
          "BLKpoint_id": "BLKpoint_324",
          "temperature_k": "323.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "763.7"
        },
        {
          "BLKpoint_id": "BLKpoint_541",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.003",
          "mass_density_kg_m3": "973.1"
        },
        {
          "BLKpoint_id": "BLKpoint_575",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.1903",
          "mass_density_kg_m3": "895.8"
        },
        {
          "BLKpoint_id": "BLKpoint_582",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.4034",
          "mass_density_kg_m3": "833.4"
        },
        {
          "BLKpoint_id": "BLKpoint_587",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.6489",
          "mass_density_kg_m3": "785.6"
        },
        {
          "BLKpoint_id": "BLKpoint_594",
          "temperature_k": "348.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "739.4"
        }
      ],
      "inspection_id": "INSP_13b9dbeeee1e",
      "lit_num_id": "GLOBlit_220"
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "block_number": "PROPblock_19",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<ethanol>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "0.0024",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "997.039"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "0.7006",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "829.434"
        },
        {
          "BLKpoint_id": "BLKpoint_59",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.7006",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "825.07"
        },
        {
          "BLKpoint_id": "BLKpoint_95",
          "temperature_k": "303.15",
          "mole_fraction_<ethanol>": "0.7006",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "820.66"
        },
        {
          "BLKpoint_id": "BLKpoint_131",
          "temperature_k": "308.15",
          "mole_fraction_<ethanol>": "0.7006",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "816.2"
        },
        {
          "BLKpoint_id": "BLKpoint_145",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "0",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "998.429"
        },
        {
          "BLKpoint_id": "BLKpoint_146",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "997.267"
        },
        {
          "BLKpoint_id": "BLKpoint_147",
          "temperature_k": "303.15",
          "mole_fraction_<ethanol>": "0",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "995.867"
        },
        {
          "BLKpoint_id": "BLKpoint_148",
          "temperature_k": "308.15",
          "mole_fraction_<ethanol>": "0",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "994.252"
        },
        {
          "BLKpoint_id": "BLKpoint_149",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "1",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "789.547"
        },
        {
          "BLKpoint_id": "BLKpoint_150",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "1",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "785.26"
        },
        {
          "BLKpoint_id": "BLKpoint_151",
          "temperature_k": "303.15",
          "mole_fraction_<ethanol>": "1",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "780.941"
        },
        {
          "BLKpoint_id": "BLKpoint_152",
          "temperature_k": "308.15",
          "mole_fraction_<ethanol>": "1",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "776.592"
        },
        {
          "BLKpoint_id": "BLKpoint_160",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "0.1984",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "935.19"
        },
        {
          "BLKpoint_id": "BLKpoint_165",
          "temperature_k": "293.15",
          "mole_fraction_<ethanol>": "0.4495",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "873.57"
        },
        {
          "BLKpoint_id": "BLKpoint_183",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.1984",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "931.84"
        },
        {
          "BLKpoint_id": "BLKpoint_188",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.4495",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "869.34"
        },
        {
          "BLKpoint_id": "BLKpoint_206",
          "temperature_k": "303.15",
          "mole_fraction_<ethanol>": "0.1984",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "928.77"
        },
        {
          "BLKpoint_id": "BLKpoint_211",
          "temperature_k": "303.15",
          "mole_fraction_<ethanol>": "0.4495",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "865.03"
        },
        {
          "BLKpoint_id": "BLKpoint_229",
          "temperature_k": "308.15",
          "mole_fraction_<ethanol>": "0.1984",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "925.04"
        },
        {
          "BLKpoint_id": "BLKpoint_234",
          "temperature_k": "308.15",
          "mole_fraction_<ethanol>": "0.4495",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "860.66"
        },
        {
          "BLKpoint_id": "BLKpoint_244",
          "temperature_k": "308.15",
          "mole_fraction_<ethanol>": "0.929",
          "pressure_kpa": "92.3",
          "mass_density_kg_m3": "785.46"
        }
      ],
      "inspection_id": "INSP_b49f3d6ec58f",
      "lit_num_id": "GLOBlit_5201"
    },
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "block_number": "PROPblock_12",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<water>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "789.75"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.4971",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "862.82"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.6991",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "908.69"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "998.2"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "785.46"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.3991",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "840.94"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.5989",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "879.89"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "997.05"
        },
        {
          "BLKpoint_id": "BLKpoint_26",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "781.15"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.2961",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "820.29"
        },
        {
          "BLKpoint_id": "BLKpoint_32",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.5989",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "875.63"
        },
        {
          "BLKpoint_id": "BLKpoint_37",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "995.65"
        }
      ],
      "inspection_id": "INSP_1d2031e2c9c2",
      "lit_num_id": "GLOBlit_2825"
    }
  ]
}