{
  "answer": "**Binary ethanol–water mass density data in the ThermoML database:**\n\nThe search for binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) mass density (GLOBprop_1) blocks found the following confirmed result:\n\n### Confirmed ethanol–water block\n\n**GLOBlit_1483 :: PROPblock_1**  \n- **DOI:** 10.1016/j.fluid.2014.05.032  \n- **System:** binary ethanol + water  \n- **Data points:** 140  \n- **Temperature range:** 292.95–448.15 K (includes isotherms at 348.15 K, near the user-requested target of ~350 K)  \n- **Pressure range:** 2450–40140 kPa (high-pressure data)  \n- **Ethanol mole fraction range:** 0.0163–0.0946 (dilute ethanol region only)  \n\nRepresentative data at 348.15 K (nearest isotherm to the requested ~350 K target):\n\n| Ethanol x | P (kPa) | ρ (kg/m³) |\n|-----------|---------|-----------|\n| 0.0163 | 39600 | 982.3 |\n| 0.0163 | 20750 | 974.7 |\n| 0.0163 | 10980 | 970.6 |\n| 0.0163 | 3220 | 967.1 |\n| 0.0343 | 39860 | 974.7 |\n| 0.0343 | 30850 | 971.3 |\n| 0.0343 | 21160 | 967.5 |\n| 0.0343 | 11590 | 963.5 |\n| 0.073 | 39600 | 958.9 |\n| 0.073 | 20870 | 950.8 |\n| 0.073 | 11060 | 946.6 |\n| 0.073 | 3330 | 943.0 |\n| 0.0946 | 37790 | 948.7 |\n| 0.0946 | 29730 | 945.4 |\n| 0.0946 | 20870 | 941.6 |\n| 0.0946 | 11390 | 937.4 |\n| 0.0946 | 2730 | 933.7 |\n\n**Note:** This dataset covers only dilute ethanol compositions (up to ~9.5 mol%) at elevated pressures (2.5–40 MPa). It does not provide atmospheric-pressure or full-composition-range density data.\n\n### Other blocks from the initial search\n\n- **GLOBlit_1742 :: PROPblock_1** — Upon inspection, this block is actually **methanol + water** (not ethanol + water) and is therefore not relevant to this query.  \n- **GLOBlit_220** and **GLOBlit_2432** were also returned by the initial search as potential ethanol–water density blocks, but these were not inspected in this run, so their exact composition/temperature coverage and data point counts cannot be confirmed here.\n\n**Chemistry note:** The inspected data show the expected trend: at 348.15 K, density decreases with increasing ethanol mole fraction (from ~982 kg/m³ at x = 0.0163 to ~949 kg/m³ at x = 0.0946 at comparable pressures), and increases with pressure at each composition, consistent with the lower density of ethanol relative to water and normal liquid compressibility behavior.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNGROUNDED_LITERAL** GLOBlit_1483::PROPblock_1: 350 (near '…s isotherms at 348.15 K, near the user-requested target of ~…') matches no inspected row/stat, database table, or other source of GLOBlit_1483::PROPblock_1\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_1483::PROPblock_1\", nearest={\"column\": \"temperature_k\", \"value\": 350.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** GLOBlit_1483::PROPblock_1: 350 (near '…tative data at 348.15 K (nearest isotherm to the requested ~…') matches no inspected row/stat, database table, or other source of GLOBlit_1483::PROPblock_1\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_1483::PROPblock_1\", nearest={\"column\": \"temperature_k\", \"value\": 350.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\nInspected so far: PROPblock_1",
  "core_claims": [
    "The ThermoML database contains a confirmed binary ethanol–water mass density block (GLOBlit_1483 :: PROPblock_1, DOI 10.1016/j.fluid.2014.05.032) with 140 data points spanning 292.95–448.15 K, 2450–40140 kPa, and ethanol mole fractions of 0.0163–0.0946 (dilute ethanol region only).",
    "At 348.15 K, the data show density decreasing with increasing ethanol mole fraction (from ~982 kg/m³ at x = 0.0163 to ~949 kg/m³ at x = 0.0946 at comparable pressures) and increasing with pressure at each composition, consistent with the lower density of ethanol relative to water and normal liquid compressibility.",
    "This dataset covers only dilute ethanol compositions (up to ~9.5 mol%) at elevated pressures (2.5–40 MPa) and does not provide atmospheric-pressure or full-composition-range density data.",
    "Two additional blocks (GLOBlit_220 and GLOBlit_2432) were returned by the initial search as potential ethanol–water density blocks but were not inspected, so their coverage cannot be confirmed."
  ],
  "status": "partial",
  "summary": "In the ThermoML database, one confirmed block of binary ethanol + water mass density data was identified: GLOBlit_1483 :: PROPblock_1 (DOI 10.1016/j.fluid.2014.05.032), containing 140 data points spanning 292.95–448.15 K, 2450–40140 kPa, and ethanol mole fractions 0.0163–0.0946 (dilute ethanol region only). Representative values at the 348.15 K isotherm show density decreasing with increasing ethanol mole fraction (e.g., ~982.3 kg/m³ at x=0.0163 and 39600 kPa down to ~933.7 kg/m³ at x=0.0946 and 2730 kPa) and increasing with pressure at each composition. This dataset covers only elevated pressures (2.5–40 MPa) and dilute ethanol compositions; it does not provide atmospheric-pressure or full-composition-range data. An initially returned block GLOBlit_1742 :: PROPblock_1 was confirmed upon inspection to be methanol + water, not ethanol + water. Two other blocks (GLOBlit_220 and GLOBlit_2432) were returned by the initial search but were not inspected, so their coverage cannot be confirmed.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_1483",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density measurements for binary ethanol + water mixtures at 292.95–448.15 K and 2450–40140 kPa, covering ethanol mole fractions 0.0163–0.0946; 140 data points.",
      "doi": "10.1016/j.fluid.2014.05.032",
      "lit_id": "2014-abd-akh-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 140,
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
      "constraints": [],
      "variables": [
        {
          "BLKvar_id": "BLKvar_1",
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
            "BLKvar_id": "BLKvar_1",
            "name": "Pressure, kPa",
            "min": 2450.0,
            "max": 40140.0,
            "n_unique": 112
          },
          "range_min": 2450.0,
          "range_max": 40140.0
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
            "min": 292.95,
            "max": 448.15,
            "n_unique": 11
          },
          "range_min": 292.95,
          "range_max": 448.15
        },
        {
          "BLKvar_id": "BLKvar_3",
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
            "BLKvar_id": "BLKvar_3",
            "name": "Mole fraction",
            "min": 0.0163,
            "max": 0.0946,
            "n_unique": 4
          },
          "range_min": 0.0163,
          "range_max": 0.0946
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
          "meas_num_id": "GLOBmeas_66",
          "meas_ID": "constant_volume_piezometry",
          "method_standard": "Constant-volume piezometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 831.7,
            "max": 1006.1,
            "mean": 934.762857,
            "std": 42.356353,
            "n": 140
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 831.7,
          "range_max": 1006.1
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
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
      "parent_n_datapoints": 140,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.fluid.2015.07.012",
      "block_number": "PROPblock_1",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "pressure_kpa",
        "mole_fraction_<methanol>",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "350.7",
          "pressure_kpa": "10000",
          "mole_fraction_<methanol>": "0.1",
          "mass_density_kg_m3": "945.55"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "350.7",
          "pressure_kpa": "10000",
          "mole_fraction_<methanol>": "0.4",
          "mass_density_kg_m3": "865.13"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "350.7",
          "pressure_kpa": "10000",
          "mole_fraction_<methanol>": "0.8",
          "mass_density_kg_m3": "780.91"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "350.7",
          "pressure_kpa": "20000",
          "mole_fraction_<methanol>": "0.1",
          "mass_density_kg_m3": "949.82"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "350.7",
          "pressure_kpa": "20000",
          "mole_fraction_<methanol>": "0.4",
          "mass_density_kg_m3": "870.55"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "350.7",
          "pressure_kpa": "20000",
          "mole_fraction_<methanol>": "0.8",
          "mass_density_kg_m3": "789.25"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "350.7",
          "pressure_kpa": "30000",
          "mole_fraction_<methanol>": "0.1",
          "mass_density_kg_m3": "954.11"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "350.7",
          "pressure_kpa": "30000",
          "mole_fraction_<methanol>": "0.4",
          "mass_density_kg_m3": "876.99"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "350.7",
          "pressure_kpa": "30000",
          "mole_fraction_<methanol>": "0.8",
          "mass_density_kg_m3": "797.6"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "350.7",
          "pressure_kpa": "40000",
          "mole_fraction_<methanol>": "0.1",
          "mass_density_kg_m3": "958.39"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "350.7",
          "pressure_kpa": "40000",
          "mole_fraction_<methanol>": "0.4",
          "mass_density_kg_m3": "882.71"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "350.7",
          "pressure_kpa": "40000",
          "mole_fraction_<methanol>": "0.8",
          "mass_density_kg_m3": "805.96"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "373.2",
          "pressure_kpa": "10000",
          "mole_fraction_<methanol>": "0.1",
          "mass_density_kg_m3": "928.71"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "temperature_k": "373.2",
          "pressure_kpa": "10000",
          "mole_fraction_<methanol>": "0.6",
          "mass_density_kg_m3": "799.33"
        },
        {
          "BLKpoint_id": "BLKpoint_31",
          "temperature_k": "373.2",
          "pressure_kpa": "10000",
          "mole_fraction_<methanol>": "1",
          "mass_density_kg_m3": "725.29"
        },
        {
          "BLKpoint_id": "BLKpoint_32",
          "temperature_k": "373.2",
          "pressure_kpa": "20000",
          "mole_fraction_<methanol>": "0.1",
          "mass_density_kg_m3": "932.78"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "temperature_k": "373.2",
          "pressure_kpa": "20000",
          "mole_fraction_<methanol>": "0.6",
          "mass_density_kg_m3": "807.98"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "temperature_k": "373.2",
          "pressure_kpa": "20000",
          "mole_fraction_<methanol>": "1",
          "mass_density_kg_m3": "737.85"
        },
        {
          "BLKpoint_id": "BLKpoint_39",
          "temperature_k": "373.2",
          "pressure_kpa": "30000",
          "mole_fraction_<methanol>": "0.1",
          "mass_density_kg_m3": "939.53"
        },
        {
          "BLKpoint_id": "BLKpoint_42",
          "temperature_k": "373.2",
          "pressure_kpa": "30000",
          "mole_fraction_<methanol>": "0.4",
          "mass_density_kg_m3": "858.91"
        },
        {
          "BLKpoint_id": "BLKpoint_45",
          "temperature_k": "373.2",
          "pressure_kpa": "30000",
          "mole_fraction_<methanol>": "1",
          "mass_density_kg_m3": "748.83"
        },
        {
          "BLKpoint_id": "BLKpoint_46",
          "temperature_k": "373.2",
          "pressure_kpa": "40000",
          "mole_fraction_<methanol>": "0.1",
          "mass_density_kg_m3": "943.52"
        },
        {
          "BLKpoint_id": "BLKpoint_50",
          "temperature_k": "373.2",
          "pressure_kpa": "40000",
          "mole_fraction_<methanol>": "0.6",
          "mass_density_kg_m3": "823.64"
        },
        {
          "BLKpoint_id": "BLKpoint_52",
          "temperature_k": "373.2",
          "pressure_kpa": "40000",
          "mole_fraction_<methanol>": "1",
          "mass_density_kg_m3": "758.66"
        },
        {
          "BLKpoint_id": "BLKpoint_53",
          "temperature_k": "476.2",
          "pressure_kpa": "10000",
          "mole_fraction_<methanol>": "0.1",
          "mass_density_kg_m3": "822.65"
        },
        {
          "BLKpoint_id": "BLKpoint_56",
          "temperature_k": "476.2",
          "pressure_kpa": "10000",
          "mole_fraction_<methanol>": "0.4",
          "mass_density_kg_m3": "714.67"
        },
        {
          "BLKpoint_id": "BLKpoint_59",
          "temperature_k": "476.2",
          "pressure_kpa": "10000",
          "mole_fraction_<methanol>": "1",
          "mass_density_kg_m3": "576.84"
        },
        {
          "BLKpoint_id": "BLKpoint_60",
          "temperature_k": "476.2",
          "pressure_kpa": "20000",
          "mole_fraction_<methanol>": "0.1",
          "mass_density_kg_m3": "831.4"
        },
        {
          "BLKpoint_id": "BLKpoint_63",
          "temperature_k": "476.2",
          "pressure_kpa": "20000",
          "mole_fraction_<methanol>": "0.4",
          "mass_density_kg_m3": "730.97"
        },
        {
          "BLKpoint_id": "BLKpoint_66",
          "temperature_k": "476.2",
          "pressure_kpa": "20000",
          "mole_fraction_<methanol>": "1",
          "mass_density_kg_m3": "612.56"
        },
        {
          "BLKpoint_id": "BLKpoint_67",
          "temperature_k": "476.2",
          "pressure_kpa": "30000",
          "mole_fraction_<methanol>": "0.1",
          "mass_density_kg_m3": "838.61"
        },
        {
          "BLKpoint_id": "BLKpoint_70",
          "temperature_k": "476.2",
          "pressure_kpa": "30000",
          "mole_fraction_<methanol>": "0.4",
          "mass_density_kg_m3": "744.11"
        },
        {
          "BLKpoint_id": "BLKpoint_73",
          "temperature_k": "476.2",
          "pressure_kpa": "30000",
          "mole_fraction_<methanol>": "1",
          "mass_density_kg_m3": "636.82"
        },
        {
          "BLKpoint_id": "BLKpoint_74",
          "temperature_k": "476.2",
          "pressure_kpa": "40000",
          "mole_fraction_<methanol>": "0.1",
          "mass_density_kg_m3": "845.82"
        },
        {
          "BLKpoint_id": "BLKpoint_77",
          "temperature_k": "476.2",
          "pressure_kpa": "40000",
          "mole_fraction_<methanol>": "0.4",
          "mass_density_kg_m3": "754.89"
        },
        {
          "BLKpoint_id": "BLKpoint_80",
          "temperature_k": "476.2",
          "pressure_kpa": "40000",
          "mole_fraction_<methanol>": "1",
          "mass_density_kg_m3": "655.67"
        }
      ],
      "inspection_id": "INSP_da246e84fdf8",
      "lit_num_id": "GLOBlit_1742"
    },
    {
      "doi": "10.1016/j.fluid.2014.05.032",
      "block_number": "PROPblock_1",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "pressure_kpa",
        "temperature_k",
        "mole_fraction_<ethanol>",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "pressure_kpa": "39170",
          "temperature_k": "297.05",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "1006.1"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "pressure_kpa": "30810",
          "temperature_k": "297.05",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "1003.2"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "pressure_kpa": "21070",
          "temperature_k": "297.05",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "997.5"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "pressure_kpa": "11280",
          "temperature_k": "297.05",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "993.5"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "pressure_kpa": "2490",
          "temperature_k": "297.05",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "990.8"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "pressure_kpa": "38480",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "995.2"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "pressure_kpa": "30890",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "992.3"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "pressure_kpa": "21080",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "988.4"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "pressure_kpa": "11390",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "984.4"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "pressure_kpa": "2570",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "980.6"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "pressure_kpa": "39910",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "982.3"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "pressure_kpa": "29500",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "978.3"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "pressure_kpa": "20750",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "974.7"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "pressure_kpa": "10980",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "970.6"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "pressure_kpa": "3220",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "967.1"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "pressure_kpa": "35700",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "964.6"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "pressure_kpa": "30600",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "962.5"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "pressure_kpa": "21160",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "958.3"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "pressure_kpa": "11320",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "953.8"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "pressure_kpa": "3370",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "950.2"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "pressure_kpa": "39890",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "948"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "pressure_kpa": "30790",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "943.7"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "pressure_kpa": "21360",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "939.3"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "pressure_kpa": "11630",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "934.4"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "pressure_kpa": "3710",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "930.3"
        },
        {
          "BLKpoint_id": "BLKpoint_26",
          "pressure_kpa": "39560",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "927.2"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "pressure_kpa": "30570",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "922.4"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "pressure_kpa": "20970",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "917"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "pressure_kpa": "10170",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "911"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "pressure_kpa": "2680",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "906.7"
        },
        {
          "BLKpoint_id": "BLKpoint_31",
          "pressure_kpa": "38340",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "903.5"
        },
        {
          "BLKpoint_id": "BLKpoint_32",
          "pressure_kpa": "31050",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "899.4"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "pressure_kpa": "21530",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "893.7"
        },
        {
          "BLKpoint_id": "BLKpoint_34",
          "pressure_kpa": "11920",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "887.5"
        },
        {
          "BLKpoint_id": "BLKpoint_35",
          "pressure_kpa": "3960",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.0163",
          "mass_density_kg_m3": "882.3"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "pressure_kpa": "39230",
          "temperature_k": "292.95",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "988"
        },
        {
          "BLKpoint_id": "BLKpoint_37",
          "pressure_kpa": "30930",
          "temperature_k": "292.95",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "985"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "pressure_kpa": "21120",
          "temperature_k": "292.95",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "981.2"
        },
        {
          "BLKpoint_id": "BLKpoint_39",
          "pressure_kpa": "11320",
          "temperature_k": "292.95",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "977.6"
        },
        {
          "BLKpoint_id": "BLKpoint_40",
          "pressure_kpa": "2450",
          "temperature_k": "292.95",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "974.2"
        },
        {
          "BLKpoint_id": "BLKpoint_41",
          "pressure_kpa": "38600",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "973.6"
        },
        {
          "BLKpoint_id": "BLKpoint_42",
          "pressure_kpa": "30360",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "970.6"
        },
        {
          "BLKpoint_id": "BLKpoint_43",
          "pressure_kpa": "20790",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "966.7"
        },
        {
          "BLKpoint_id": "BLKpoint_44",
          "pressure_kpa": "10940",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "962.8"
        },
        {
          "BLKpoint_id": "BLKpoint_45",
          "pressure_kpa": "2610",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "959.3"
        },
        {
          "BLKpoint_id": "BLKpoint_46",
          "pressure_kpa": "39600",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "958.9"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "pressure_kpa": "20870",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "950.8"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "pressure_kpa": "11060",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "946.6"
        },
        {
          "BLKpoint_id": "BLKpoint_50",
          "pressure_kpa": "3330",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "943"
        },
        {
          "BLKpoint_id": "BLKpoint_51",
          "pressure_kpa": "37230",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "939.9"
        },
        {
          "BLKpoint_id": "BLKpoint_52",
          "pressure_kpa": "30670",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "937"
        },
        {
          "BLKpoint_id": "BLKpoint_53",
          "pressure_kpa": "21080",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "932.5"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "pressure_kpa": "11320",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "927.7"
        },
        {
          "BLKpoint_id": "BLKpoint_55",
          "pressure_kpa": "3510",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "923.9"
        },
        {
          "BLKpoint_id": "BLKpoint_56",
          "pressure_kpa": "39500",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "920.7"
        },
        {
          "BLKpoint_id": "BLKpoint_57",
          "pressure_kpa": "30790",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "916.3"
        },
        {
          "BLKpoint_id": "BLKpoint_58",
          "pressure_kpa": "21160",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "911.4"
        },
        {
          "BLKpoint_id": "BLKpoint_59",
          "pressure_kpa": "11510",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "906.2"
        },
        {
          "BLKpoint_id": "BLKpoint_60",
          "pressure_kpa": "3710",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "901.9"
        },
        {
          "BLKpoint_id": "BLKpoint_61",
          "pressure_kpa": "40110",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "898.6"
        },
        {
          "BLKpoint_id": "BLKpoint_62",
          "pressure_kpa": "30490",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "893"
        },
        {
          "BLKpoint_id": "BLKpoint_63",
          "pressure_kpa": "20110",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "887.1"
        },
        {
          "BLKpoint_id": "BLKpoint_64",
          "pressure_kpa": "10710",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "881.1"
        },
        {
          "BLKpoint_id": "BLKpoint_65",
          "pressure_kpa": "2760",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "875.9"
        },
        {
          "BLKpoint_id": "BLKpoint_66",
          "pressure_kpa": "37210",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "873"
        },
        {
          "BLKpoint_id": "BLKpoint_67",
          "pressure_kpa": "31170",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "869.2"
        },
        {
          "BLKpoint_id": "BLKpoint_68",
          "pressure_kpa": "21690",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "862.7"
        },
        {
          "BLKpoint_id": "BLKpoint_69",
          "pressure_kpa": "12160",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "855.6"
        },
        {
          "BLKpoint_id": "BLKpoint_70",
          "pressure_kpa": "4000",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.073",
          "mass_density_kg_m3": "849.3"
        },
        {
          "BLKpoint_id": "BLKpoint_71",
          "pressure_kpa": "40030",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "979.8"
        },
        {
          "BLKpoint_id": "BLKpoint_72",
          "pressure_kpa": "29980",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "976.1"
        },
        {
          "BLKpoint_id": "BLKpoint_73",
          "pressure_kpa": "20060",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "972.4"
        },
        {
          "BLKpoint_id": "BLKpoint_74",
          "pressure_kpa": "10120",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "968.6"
        },
        {
          "BLKpoint_id": "BLKpoint_75",
          "pressure_kpa": "2560",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "965.8"
        },
        {
          "BLKpoint_id": "BLKpoint_76",
          "pressure_kpa": "39810",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "966.2"
        },
        {
          "BLKpoint_id": "BLKpoint_77",
          "pressure_kpa": "32400",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "963.3"
        },
        {
          "BLKpoint_id": "BLKpoint_78",
          "pressure_kpa": "20710",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "958.8"
        },
        {
          "BLKpoint_id": "BLKpoint_79",
          "pressure_kpa": "11140",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "954.9"
        },
        {
          "BLKpoint_id": "BLKpoint_80",
          "pressure_kpa": "2730",
          "temperature_k": "323.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "951.3"
        },
        {
          "BLKpoint_id": "BLKpoint_81",
          "pressure_kpa": "37790",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "948.7"
        },
        {
          "BLKpoint_id": "BLKpoint_82",
          "pressure_kpa": "29730",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "945.4"
        },
        {
          "BLKpoint_id": "BLKpoint_83",
          "pressure_kpa": "20870",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "941.6"
        },
        {
          "BLKpoint_id": "BLKpoint_84",
          "pressure_kpa": "11390",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "937.4"
        },
        {
          "BLKpoint_id": "BLKpoint_85",
          "pressure_kpa": "2730",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "933.7"
        },
        {
          "BLKpoint_id": "BLKpoint_86",
          "pressure_kpa": "39410",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "927.3"
        },
        {
          "BLKpoint_id": "BLKpoint_87",
          "pressure_kpa": "30850",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "922.3"
        },
        {
          "BLKpoint_id": "BLKpoint_88",
          "pressure_kpa": "21200",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "917.7"
        },
        {
          "BLKpoint_id": "BLKpoint_90",
          "pressure_kpa": "3330",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "908.6"
        },
        {
          "BLKpoint_id": "BLKpoint_91",
          "pressure_kpa": "39610",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "905.3"
        },
        {
          "BLKpoint_id": "BLKpoint_92",
          "pressure_kpa": "30850",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "901.1"
        },
        {
          "BLKpoint_id": "BLKpoint_93",
          "pressure_kpa": "21200",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "896"
        },
        {
          "BLKpoint_id": "BLKpoint_94",
          "pressure_kpa": "11430",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "890.4"
        },
        {
          "BLKpoint_id": "BLKpoint_95",
          "pressure_kpa": "3510",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "885.8"
        },
        {
          "BLKpoint_id": "BLKpoint_96",
          "pressure_kpa": "39860",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "882.2"
        },
        {
          "BLKpoint_id": "BLKpoint_97",
          "pressure_kpa": "30100",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "875.5"
        },
        {
          "BLKpoint_id": "BLKpoint_98",
          "pressure_kpa": "20200",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "869.5"
        },
        {
          "BLKpoint_id": "BLKpoint_99",
          "pressure_kpa": "10050",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "863.9"
        },
        {
          "BLKpoint_id": "BLKpoint_100",
          "pressure_kpa": "2750",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "860.1"
        },
        {
          "BLKpoint_id": "BLKpoint_101",
          "pressure_kpa": "40140",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "858.6"
        },
        {
          "BLKpoint_id": "BLKpoint_102",
          "pressure_kpa": "30990",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "852.6"
        },
        {
          "BLKpoint_id": "BLKpoint_103",
          "pressure_kpa": "21690",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "845.8"
        },
        {
          "BLKpoint_id": "BLKpoint_104",
          "pressure_kpa": "11550",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "837.9"
        },
        {
          "BLKpoint_id": "BLKpoint_105",
          "pressure_kpa": "3860",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.0946",
          "mass_density_kg_m3": "831.7"
        },
        {
          "BLKpoint_id": "BLKpoint_106",
          "pressure_kpa": "39150",
          "temperature_k": "298.35",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "998.6"
        },
        {
          "BLKpoint_id": "BLKpoint_107",
          "pressure_kpa": "31040",
          "temperature_k": "298.35",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "995.7"
        },
        {
          "BLKpoint_id": "BLKpoint_108",
          "pressure_kpa": "21300",
          "temperature_k": "298.35",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "991.9"
        },
        {
          "BLKpoint_id": "BLKpoint_110",
          "pressure_kpa": "2590",
          "temperature_k": "298.35",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "984.1"
        },
        {
          "BLKpoint_id": "BLKpoint_112",
          "pressure_kpa": "30930",
          "temperature_k": "323.65",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "985.2"
        },
        {
          "BLKpoint_id": "BLKpoint_113",
          "pressure_kpa": "21200",
          "temperature_k": "323.65",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "981.4"
        },
        {
          "BLKpoint_id": "BLKpoint_114",
          "pressure_kpa": "11320",
          "temperature_k": "323.65",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "977.4"
        },
        {
          "BLKpoint_id": "BLKpoint_115",
          "pressure_kpa": "2610",
          "temperature_k": "323.65",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "973.6"
        },
        {
          "BLKpoint_id": "BLKpoint_116",
          "pressure_kpa": "39860",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "974.7"
        },
        {
          "BLKpoint_id": "BLKpoint_117",
          "pressure_kpa": "30850",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "971.3"
        },
        {
          "BLKpoint_id": "BLKpoint_118",
          "pressure_kpa": "21160",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "967.5"
        },
        {
          "BLKpoint_id": "BLKpoint_119",
          "pressure_kpa": "11590",
          "temperature_k": "348.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "963.5"
        },
        {
          "BLKpoint_id": "BLKpoint_121",
          "pressure_kpa": "39000",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "957.9"
        },
        {
          "BLKpoint_id": "BLKpoint_122",
          "pressure_kpa": "30520",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "954.5"
        },
        {
          "BLKpoint_id": "BLKpoint_123",
          "pressure_kpa": "21120",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "950.3"
        },
        {
          "BLKpoint_id": "BLKpoint_124",
          "pressure_kpa": "11470",
          "temperature_k": "373.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "945.9"
        },
        {
          "BLKpoint_id": "BLKpoint_126",
          "pressure_kpa": "37300",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "938.3"
        },
        {
          "BLKpoint_id": "BLKpoint_127",
          "pressure_kpa": "30930",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "935.2"
        },
        {
          "BLKpoint_id": "BLKpoint_128",
          "pressure_kpa": "21530",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "930.7"
        },
        {
          "BLKpoint_id": "BLKpoint_129",
          "pressure_kpa": "11730",
          "temperature_k": "398.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "925.8"
        },
        {
          "BLKpoint_id": "BLKpoint_131",
          "pressure_kpa": "39680",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "918.2"
        },
        {
          "BLKpoint_id": "BLKpoint_132",
          "pressure_kpa": "30640",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "913.4"
        },
        {
          "BLKpoint_id": "BLKpoint_133",
          "pressure_kpa": "21070",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "908.1"
        },
        {
          "BLKpoint_id": "BLKpoint_135",
          "pressure_kpa": "2680",
          "temperature_k": "423.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "897.3"
        },
        {
          "BLKpoint_id": "BLKpoint_136",
          "pressure_kpa": "40060",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "894.8"
        },
        {
          "BLKpoint_id": "BLKpoint_137",
          "pressure_kpa": "31010",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "889.8"
        },
        {
          "BLKpoint_id": "BLKpoint_138",
          "pressure_kpa": "22180",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "884.2"
        },
        {
          "BLKpoint_id": "BLKpoint_140",
          "pressure_kpa": "4080",
          "temperature_k": "448.15",
          "mole_fraction_<ethanol>": "0.0343",
          "mass_density_kg_m3": "872.1"
        }
      ],
      "inspection_id": "INSP_51f9b5335a8a",
      "lit_num_id": "GLOBlit_1483"
    }
  ]
}