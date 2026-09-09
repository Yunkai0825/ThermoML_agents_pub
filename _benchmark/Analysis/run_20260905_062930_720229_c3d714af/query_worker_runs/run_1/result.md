{
  "answer": "## Viscosity Data for Ethanol + Water Binary Mixtures\n\n### Best Dataset: Full Composition Range at 298.15 K\n\n**DOI:** 10.1016/j.jct.2018.02.022 [GLOBlit_5201] — PROPblock_21  \n- **System:** binary ethanol (GLOBcomp_2) + water (GLOBcomp_1), liquid phase  \n- **Total data points:** 100  \n- **Temperature range:** 293.15–308.15 K (multiple isotherms including 298.15 K)  \n- **Composition range:** x(ethanol) = 0 to 1 (full range)  \n- **Pressure:** 92.3 kPa (fixed constraint)\n\nAt **T = 298.15 K**, 25 data points span the entire mole fraction range. Representative inspected values:\n\n| x(ethanol) | Viscosity (Pa·s) |\n|------------|-----------------|\n| 0          | 0.00089689      |\n| 0.0201     | 0.001098        |\n| 0.1004     | 0.0019469       |\n| 0.1499     | 0.0022424       |\n| 0.1984     | 0.0023706       |\n| 0.2499     | 0.0024286       |\n| 0.3499     | 0.0022633       |\n| 0.399      | 0.0021697       |\n| 0.4989     | 0.0019557       |\n| 0.5495     | 0.0018796       |\n| 0.6067     | 0.0017439       |\n| 0.6956     | 0.0015722       |\n| 0.8475     | 0.0013415       |\n| 1          | 0.0010914       |\n\n**Chemistry insight:** The data clearly show the well-known viscosity maximum in the ethanol–water system. At 298.15 K, viscosity peaks near x(ethanol) ≈ 0.25 (0.0024286 Pa·s). From the inspected values, the peak-to-pure-water ratio is 0.0024286 / 0.00089689 ≈ 2.7 (computed), and the peak-to-pure-ethanol ratio is 0.0024286 / 0.0010914 ≈ 2.2 (computed). This maximum arises from strong hydrogen-bonding interactions between ethanol and water molecules, which create more structured, less mobile molecular clusters at intermediate compositions.\n\n### Second Largest Dataset: Wide Temperature Range\n\n**DOI:** 10.1021/je800150h [GLOBlit_11136] — PROPblock_8  \n- **Total data points:** 108  \n- **Temperature range:** 268.1–323.15 K (much wider T coverage)  \n- **Composition range:** x(water) = 0.1–0.9 (note: composition variable is mole fraction of water)  \n- **Pressure:** 101.0 kPa (fixed constraint)  \n- **Viscosity range:** 0.00076–0.007549 Pa·s\n\nThis block covers multiple compositions at multiple temperatures. At 298.15 K, an inspected data point at x(water) = 0.7 gives viscosity = 0.00235 Pa·s. The highest viscosity in the block (0.007549 Pa·s) occurs at x(water) = 0.8 and T = 268.1 K, illustrating the strong temperature dependence of the viscosity maximum. This dataset is particularly valuable for studying the temperature dependence of the viscosity–composition relationship across a range of 323.15 − 268.1 = 55.05 K (computed from the inspected temperature bounds).\n\n### Summary of All Found Blocks\n\nThe initial search returned a total of 14 viscosity blocks (from the search_blocks discovery query) for the ethanol + water binary system, all in the liquid phase. The two datasets above offer the best combination of composition coverage (GLOBlit_5201, full x range at 298.15 K) and temperature coverage (GLOBlit_11136, 268.1–323.15 K across x(water) = 0.1–0.9) for studying composition-dependent dynamic viscosity at and around 298.15 K.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNINSPECTED_VALUE** PROPblock_21: 2.7 exists in PROPblock_21's database table but was never shown in an inspection of this run\n  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number=\"GLOBlit_5201::PROPblock_21\", nearest={\"column\": \"temperature_k\", \"value\": 2.7})`\n- **UNGROUNDED_LITERAL** PROPblock_8: 55.05 (near '…composition relationship across a range of 323.15 - 268.1 = …') matches no inspected row/stat, database table, or other source of PROPblock_8\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_8\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"mole_fraction_<water>\", \"value\": 55.05})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** PROPblock_8: 14 (near '…of All Found Blocks  The initial search returned a total of …') matches no inspected row/stat, database table, or other source of PROPblock_8\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_8\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"mole_fraction_<water>\", \"value\": 14.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\nInspected so far: PROPblock_21, PROPblock_8",
  "core_claims": [
    "At 298.15 K and 92.3 kPa, liquid-phase dynamic viscosity data for ethanol + water spanning x(ethanol) = 0 to 1 (25 data points, DOI 10.1016/j.jct.2018.02.022) show a well-known viscosity maximum near x(ethanol) ≈ 0.25, with a peak value of 0.0024286 Pa·s compared to 0.00089689 Pa·s for pure water and 0.0010914 Pa·s for pure ethanol.",
    "The viscosity maximum in ethanol–water mixtures is attributed to strong hydrogen-bonding interactions between ethanol and water molecules, creating more structured, less mobile molecular clusters at intermediate compositions.",
    "A second dataset (DOI 10.1021/je800150h) provides 108 data points covering a wider temperature range of 268.1–323.15 K at x(water) = 0.1–0.9 and 101.0 kPa, with viscosities spanning 0.00076–0.007549 Pa·s; the highest viscosity (0.007549 Pa·s) occurs at x(water) = 0.8 and T = 268.1 K, illustrating strong temperature dependence of the viscosity maximum."
  ],
  "status": "success",
  "summary": "Viscosity data for the ethanol + water binary liquid system were identified across multiple ThermoML datasets. The best composition-coverage dataset is from DOI 10.1016/j.jct.2018.02.022 (GLOBlit_5201, PROPblock_21), containing 100 data points at 293.15–308.15 K over the full mole fraction range x(ethanol) = 0 to 1 at 92.3 kPa. At 298.15 K, 25 data points span the entire composition range and reveal the well-known viscosity maximum near x(ethanol) ≈ 0.25, where viscosity reaches 0.0024286 Pa·s compared to 0.00089689 Pa·s for pure water and 0.0010914 Pa·s for pure ethanol. This maximum is attributed to strong hydrogen-bonding interactions creating structured molecular clusters at intermediate compositions. The best temperature-coverage dataset is from DOI 10.1021/je800150h (GLOBlit_11136, PROPblock_8), with 108 data points spanning 268.1–323.15 K at x(water) = 0.1–0.9 and 101.0 kPa, with viscosities ranging from 0.00076 to 0.007549 Pa·s. At 298.15 K and x(water) = 0.7, viscosity is 0.00235 Pa·s; the highest viscosity (0.007549 Pa·s) occurs at x(water) = 0.8 and T = 268.1 K, illustrating strong temperature dependence of the viscosity maximum.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_2",
      "registry_id": "ethanol",
      "name": "ethanol"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_4",
      "registry_id": "viscosity_pa_s",
      "name": "Viscosity, Pa*s"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_5201",
      "registry_id": "2018-hog-tor-0",
      "name": "10.1016/j.jct.2018.02.022"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_11136",
      "registry_id": "2008-reh-ans-0",
      "name": "10.1021/je800150h"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_21",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of ethanol + water binary mixture, liquid phase. 100 data points, T = 293.15–308.15 K (including 298.15 K), x(ethanol) = 0–1 (full range), P = 92.3 kPa.",
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_id": "2018-hog-tor-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 100,
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
            "n_unique": 25
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
            "max": 0.002864,
            "mean": 0.001611,
            "std": 0.000493,
            "n": 100
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000759,
          "range_max": 0.002864
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
      "parent_n_datapoints": 100,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_11136",
      "block_number": "PROPblock_8",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of ethanol + water binary mixture, liquid phase. 108 data points, T = 268.1–323.15 K, x(water) = 0.1–0.9, P = 101.0 kPa.",
      "doi": "10.1021/je800150h",
      "lit_id": "2008-reh-ans-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 108,
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
            "min": 268.1,
            "max": 323.15,
            "n_unique": 12
          },
          "range_min": 268.1,
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
          "meas_num_id": "GLOBmeas_165",
          "meas_ID": "captub_ufactor_8",
          "method_standard": null,
          "method_custom": "CAPTUB::UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.00076,
            "max": 0.007549,
            "mean": 0.002353,
            "std": 0.001472,
            "n": 108
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.00076,
          "range_max": 0.007549
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
      "parent_n_datapoints": 108,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "block_number": "PROPblock_21",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<ethanol>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.0201",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.001098"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.1004",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0019469"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.1499",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0022424"
        },
        {
          "BLKpoint_id": "BLKpoint_31",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.1984",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0023706"
        },
        {
          "BLKpoint_id": "BLKpoint_32",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.2499",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0024286"
        },
        {
          "BLKpoint_id": "BLKpoint_34",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.3499",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0022633"
        },
        {
          "BLKpoint_id": "BLKpoint_35",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.399",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0021697"
        },
        {
          "BLKpoint_id": "BLKpoint_37",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.4989",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0019557"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.5495",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0018796"
        },
        {
          "BLKpoint_id": "BLKpoint_39",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.6067",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0017439"
        },
        {
          "BLKpoint_id": "BLKpoint_41",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.6956",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0015722"
        },
        {
          "BLKpoint_id": "BLKpoint_44",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.8475",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0013415"
        },
        {
          "BLKpoint_id": "BLKpoint_94",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.00089689"
        },
        {
          "BLKpoint_id": "BLKpoint_98",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "1",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0010914"
        }
      ],
      "inspection_id": "INSP_d0495ab20e5e",
      "lit_num_id": "GLOBlit_5201"
    },
    {
      "doi": "10.1021/je800150h",
      "block_number": "PROPblock_8",
      "table_mode": "rdp",
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
          "mole_fraction_<water>": "0.1",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002307"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "mole_fraction_<water>": "0.1",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001355"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "mole_fraction_<water>": "0.1",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00076"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "mole_fraction_<water>": "0.2",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002805"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "mole_fraction_<water>": "0.2",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001515"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "mole_fraction_<water>": "0.2",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000839"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "mole_fraction_<water>": "0.3",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.003345"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "mole_fraction_<water>": "0.3",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001715"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "mole_fraction_<water>": "0.3",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000902"
        },
        {
          "BLKpoint_id": "BLKpoint_37",
          "mole_fraction_<water>": "0.4",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.003991"
        },
        {
          "BLKpoint_id": "BLKpoint_39",
          "mole_fraction_<water>": "0.4",
          "temperature_k": "278.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00298"
        },
        {
          "BLKpoint_id": "BLKpoint_42",
          "mole_fraction_<water>": "0.4",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001901"
        },
        {
          "BLKpoint_id": "BLKpoint_44",
          "mole_fraction_<water>": "0.4",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001446"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "mole_fraction_<water>": "0.4",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000932"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "mole_fraction_<water>": "0.5",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.004829"
        },
        {
          "BLKpoint_id": "BLKpoint_51",
          "mole_fraction_<water>": "0.5",
          "temperature_k": "278.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.003518"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "mole_fraction_<water>": "0.5",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002153"
        },
        {
          "BLKpoint_id": "BLKpoint_57",
          "mole_fraction_<water>": "0.5",
          "temperature_k": "308.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001407"
        },
        {
          "BLKpoint_id": "BLKpoint_60",
          "mole_fraction_<water>": "0.5",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00102"
        },
        {
          "BLKpoint_id": "BLKpoint_61",
          "mole_fraction_<water>": "0.6",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.005931"
        },
        {
          "BLKpoint_id": "BLKpoint_63",
          "mole_fraction_<water>": "0.6",
          "temperature_k": "278.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.004176"
        },
        {
          "BLKpoint_id": "BLKpoint_66",
          "mole_fraction_<water>": "0.6",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002463"
        },
        {
          "BLKpoint_id": "BLKpoint_69",
          "mole_fraction_<water>": "0.6",
          "temperature_k": "308.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001582"
        },
        {
          "BLKpoint_id": "BLKpoint_72",
          "mole_fraction_<water>": "0.6",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00114"
        },
        {
          "BLKpoint_id": "BLKpoint_73",
          "mole_fraction_<water>": "0.7",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.007172"
        },
        {
          "BLKpoint_id": "BLKpoint_75",
          "mole_fraction_<water>": "0.7",
          "temperature_k": "278.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.004933"
        },
        {
          "BLKpoint_id": "BLKpoint_77",
          "mole_fraction_<water>": "0.7",
          "temperature_k": "288.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.003372"
        },
        {
          "BLKpoint_id": "BLKpoint_79",
          "mole_fraction_<water>": "0.7",
          "temperature_k": "298.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00235"
        },
        {
          "BLKpoint_id": "BLKpoint_84",
          "mole_fraction_<water>": "0.7",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00117"
        },
        {
          "BLKpoint_id": "BLKpoint_85",
          "mole_fraction_<water>": "0.8",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.007549"
        },
        {
          "BLKpoint_id": "BLKpoint_87",
          "mole_fraction_<water>": "0.8",
          "temperature_k": "278.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.005037"
        },
        {
          "BLKpoint_id": "BLKpoint_88",
          "mole_fraction_<water>": "0.8",
          "temperature_k": "283.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.004102"
        },
        {
          "BLKpoint_id": "BLKpoint_90",
          "mole_fraction_<water>": "0.8",
          "temperature_k": "293.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002841"
        },
        {
          "BLKpoint_id": "BLKpoint_93",
          "mole_fraction_<water>": "0.8",
          "temperature_k": "308.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001772"
        },
        {
          "BLKpoint_id": "BLKpoint_96",
          "mole_fraction_<water>": "0.8",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001202"
        },
        {
          "BLKpoint_id": "BLKpoint_97",
          "mole_fraction_<water>": "0.9",
          "temperature_k": "268.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.006025"
        },
        {
          "BLKpoint_id": "BLKpoint_99",
          "mole_fraction_<water>": "0.9",
          "temperature_k": "278.1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.004089"
        },
        {
          "BLKpoint_id": "BLKpoint_101",
          "mole_fraction_<water>": "0.9",
          "temperature_k": "288.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002706"
        },
        {
          "BLKpoint_id": "BLKpoint_104",
          "mole_fraction_<water>": "0.9",
          "temperature_k": "303.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001656"
        },
        {
          "BLKpoint_id": "BLKpoint_108",
          "mole_fraction_<water>": "0.9",
          "temperature_k": "323.15",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000975"
        }
      ],
      "inspection_id": "INSP_4b352e3d2858",
      "lit_num_id": "GLOBlit_11136"
    }
  ]
}