{
  "answer": "**Dynamic Viscosity of 2-Pyrrolidinone + Water (Binary System) near 298.15 K**\n\nA single data block was found in the ThermoML database:\n\n- **DOI:** 10.1021/je0340809 (GLOBlit_8242)\n- **Block:** PROPblock_14\n- **System:** Binary — 2-pyrrolidinone (GLOBcomp_268) + water (GLOBcomp_1)\n- **Property:** Dynamic viscosity (GLOBprop_4), liquid phase, in Pa·s\n- **Composition variable:** Mole fraction of water (GLOBvar_2)\n- **Temperature variable:** Temperature in K (GLOBvar_1)\n- **Constraint:** Pressure = 101.3 kPa (atmospheric)\n- **Total data points:** 95 (across temperatures 298.15–338.15 K)\n- **Data points at 298.15 K:** 19 (13 shown via shape-preserving selection; mole fraction of water spans 0.0549–0.9906)\n\n**Viscosity data at T = 298.15 K, P = 101.3 kPa:**\n\n| x(water) | η (Pa·s) |\n|-----------|-----------|\n| 0.0549 | 0.01302 |\n| 0.1506 | 0.012295 |\n| 0.2552 | 0.011766 |\n| 0.35 | 0.011319 |\n| 0.4496 | 0.01063 |\n| 0.5 | 0.010127 |\n| 0.5566 | 0.009408 |\n| 0.6422 | 0.008014 |\n| 0.7532 | 0.005772 |\n| 0.8516 | 0.003645 |\n| 0.9 | 0.002651 |\n| 0.9526 | 0.001667 |\n| 0.9906 | 0.001036 |\n\n**Chemical insight:** 2-Pyrrolidinone (γ-butyrolactam, the unmethylated parent of NMP) is a strongly hydrogen-bonding lactam. The viscosity decreases monotonically as the water mole fraction increases from 0.0549 to 0.9906, dropping from 0.01302 Pa·s (nearly pure 2-pyrrolidinone) to 0.001036 Pa·s (dilute 2-pyrrolidinone in water). This smooth, roughly order-of-magnitude decrease reflects the progressive dilution of the viscous lactam network by the much less viscous water. The block also contains isotherms at 308.15, 318.15, and 338.15 K (full block viscosity range: 0.000473–0.01302 Pa·s), showing the expected decrease in viscosity with rising temperature.",
  "core_claims": [
    "A single ThermoML data block (DOI 10.1021/je0340809, PROPblock_14) reports dynamic viscosity for the binary system 2-pyrrolidinone + water in the liquid phase at 101.3 kPa, covering temperatures 298.15–338.15 K with 95 total data points.",
    "At 298.15 K and 101.3 kPa, 19 data points span water mole fractions from 0.0549 to 0.9906; the dynamic viscosity decreases monotonically from 0.01302 Pa·s at x(water) = 0.0549 to 0.001036 Pa·s at x(water) = 0.9906.",
    "The monotonic viscosity decrease with increasing water content reflects progressive dilution of the viscous hydrogen-bonding lactam network by the much less viscous water.",
    "The full block viscosity range across all temperatures (298.15–338.15 K) is 0.000473–0.01302 Pa·s, showing the expected decrease in viscosity with rising temperature."
  ],
  "status": "success",
  "summary": "Dynamic viscosity of the binary system 2-pyrrolidinone + water was reported from DOI 10.1021/je0340809 (ThermoML block PROPblock_14). The property is dynamic viscosity in Pa·s for the liquid phase at 101.3 kPa, with 95 total data points spanning 298.15–338.15 K. At 298.15 K, 19 data points cover water mole fractions from 0.0549 to 0.9906. Viscosity decreases monotonically with increasing water content: from 0.01302 Pa·s at x(water)=0.0549 to 0.001036 Pa·s at x(water)=0.9906. Representative values include 0.012295 Pa·s at x=0.1506, 0.011766 Pa·s at x=0.2552, 0.01063 Pa·s at x=0.4496, 0.010127 Pa·s at x=0.5, 0.008014 Pa·s at x=0.6422, 0.005772 Pa·s at x=0.7532, 0.003645 Pa·s at x=0.8516, 0.002651 Pa·s at x=0.9, and 0.001667 Pa·s at x=0.9526. Additional isotherms at 308.15, 318.15, and 338.15 K are present in the block, with the full viscosity range being 0.000473–0.01302 Pa·s. The monotonic decrease reflects progressive dilution of the viscous lactam hydrogen-bonding network by water.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_268",
      "registry_id": "2-pyrrolidinone",
      "name": "2-pyrrolidinone"
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
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_8242",
      "registry_id": "2004-geo-sas-0",
      "name": "10.1021/je0340809"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_8242",
      "block_number": "PROPblock_14",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_268",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of 2-pyrrolidinone + water binary system at 298.15–338.15 K and 101.3 kPa; 95 data points; composition given as mole fraction of water.",
      "doi": "10.1021/je0340809",
      "lit_id": "2004-geo-sas-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 95,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_268",
          "name": "2-pyrrolidinone",
          "formula": "C4H7NO",
          "inchi_key": "HNJBEVLQSNELDL-UHFFFAOYSA-N",
          "SMILES": "OC1=NCCC1",
          "sample_num": "DOIcompSample_3_1"
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
            "min": 0.0549,
            "max": 0.9906,
            "n_unique": 19
          },
          "range_min": 0.0549,
          "range_max": 0.9906
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
            "min": 0.000473,
            "max": 0.01302,
            "mean": 0.003378,
            "std": 0.003031,
            "n": 95
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000473,
          "range_max": 0.01302
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
          "comp_num_id": "GLOBcomp_268",
          "name": "2-pyrrolidinone",
          "formula": "C4H7NO",
          "inchi_key": "HNJBEVLQSNELDL-UHFFFAOYSA-N",
          "SMILES": "OC1=NCCC1",
          "sample_num": "DOIcompSample_3_1"
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
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1021/je0340809",
      "block_number": "PROPblock_14",
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
          "mole_fraction_<water>": "0.0549",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.01302"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "mole_fraction_<water>": "0.1506",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.012295"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "mole_fraction_<water>": "0.2552",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.011766"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "mole_fraction_<water>": "0.35",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.011319"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "mole_fraction_<water>": "0.4496",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.01063"
        },
        {
          "BLKpoint_id": "BLKpoint_26",
          "mole_fraction_<water>": "0.5",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.010127"
        },
        {
          "BLKpoint_id": "BLKpoint_31",
          "mole_fraction_<water>": "0.5566",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.009408"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "mole_fraction_<water>": "0.6422",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.008014"
        },
        {
          "BLKpoint_id": "BLKpoint_41",
          "mole_fraction_<water>": "0.7532",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.005772"
        },
        {
          "BLKpoint_id": "BLKpoint_46",
          "mole_fraction_<water>": "0.8516",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.003645"
        },
        {
          "BLKpoint_id": "BLKpoint_61",
          "mole_fraction_<water>": "0.9",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.002651"
        },
        {
          "BLKpoint_id": "BLKpoint_76",
          "mole_fraction_<water>": "0.9526",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.001667"
        },
        {
          "BLKpoint_id": "BLKpoint_91",
          "mole_fraction_<water>": "0.9906",
          "temperature_k": "298.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.001036"
        }
      ],
      "inspection_id": "INSP_fc05bb5e42c6",
      "lit_num_id": "GLOBlit_8242"
    },
    {
      "doi": "10.1021/je0340809",
      "block_number": "PROPblock_14",
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
          "BLKpoint_id": "BLKpoint_2",
          "mole_fraction_<water>": "0.0549",
          "temperature_k": "308.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.008624"
        }
      ],
      "inspection_id": "INSP_df7c97271afb",
      "lit_num_id": "GLOBlit_8242"
    },
    {
      "doi": "10.1021/je0340809",
      "block_number": "PROPblock_14",
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
          "BLKpoint_id": "BLKpoint_3",
          "mole_fraction_<water>": "0.0549",
          "temperature_k": "318.15",
          "pressure_kpa": "101.3",
          "viscosity_pa_s": "0.006104"
        }
      ],
      "inspection_id": "INSP_599f3024337f",
      "lit_num_id": "GLOBlit_8242"
    }
  ]
}