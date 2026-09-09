{
  "answer": "## Density Data for Ethanol + Water Binary Mixture at 298.15 K\n\nThe ThermoML database contains extensive density data for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system at 298.15 K and atmospheric pressure (~100 kPa), suitable for deriving excess molar volume.\n\n### Primary Data Source\n\n**DOI:** 10.1016/j.fluid.2004.11.019  \n**Literature ID:** GLOBlit_220  \n**Block:** PROPblock_2  \n**Property:** Mass density (GLOBprop_1), kg/m³  \n**Total data points at 298.15 K, 100 kPa:** 54 points spanning the full composition range (ethanol mole fraction 0.003 to 1.0)\n\n### Representative Data Points (298.15 K, 100 kPa)\n\n| Ethanol mole fraction | Mass density (kg/m³) |\n|----------------------|---------------------|\n| 0.003 | 995.3 |\n| 0.0184 | 988.4 |\n| 0.0279 | 984.7 |\n| 0.0483 | 977.5 |\n| 0.0801 | 968.6 |\n| 0.1296 | 954.9 |\n| 0.2502 | 918.5 |\n| 0.3009 | 904.5 |\n| 0.35 | 891.9 |\n| 0.4501 | 868.8 |\n| 0.498 | 859.3 |\n| 0.5501 | 849.5 |\n| 0.6489 | 832.7 |\n| 0.6967 | 825.2 |\n| 0.8484 | 804.4 |\n| 1.0 | 785.7 |\n\nThe density decreases monotonically from near-pure water (~995.3 kg/m³) to pure ethanol (785.7 kg/m³). The full 54-point dataset at this isotherm provides excellent composition resolution for computing excess molar volumes via V^E = V_mix − Σ x_i V_i*, where pure component molar volumes can be obtained from the endpoint densities (x_ethanol = 0 and x_ethanol = 1).\n\n### Additional Data Availability\n\nThe search returned **22 total blocks** of ethanol+water binary density data near 298.15 K across multiple literature sources, so additional datasets are available for cross-validation if needed. The block above (GLOBlit_220::PROPblock_2) contains 810 total data points spanning 298.15–348.15 K and pressures from 100 to 40,000 kPa, making it also useful for temperature- and pressure-dependent studies.\n\n### Key Identifiers\n- **Ethanol:** GLOBcomp_2 (C₂H₆O, CCO)\n- **Water:** GLOBcomp_1 (H₂O)\n- **Mass density:** GLOBprop_1 (kg/m³)\n- **Literature:** GLOBlit_220 (DOI: 10.1016/j.fluid.2004.11.019)\n- **Block:** PROPblock_2",
  "core_claims": [
    "The ThermoML database contains 54 density data points for the ethanol + water binary system at 298.15 K and ~100 kPa, spanning ethanol mole fractions from 0.003 to 1.0, sourced from DOI 10.1016/j.fluid.2004.11.019.",
    "Mass density decreases monotonically from ~995.3 kg/m³ near pure water to 785.7 kg/m³ for pure ethanol at 298.15 K and 100 kPa.",
    "The 54-point dataset provides sufficient composition resolution for computing excess molar volumes via V^E = V_mix − Σ x_i V_i*, using pure component molar volumes from the endpoint densities.",
    "22 total blocks of ethanol + water binary density data near 298.15 K are available across multiple literature sources for cross-validation."
  ],
  "status": "success",
  "summary": "Density data for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary mixture at 298.15 K and ~100 kPa are available from ThermoML, primarily from GLOBlit_220 (DOI: 10.1016/j.fluid.2004.11.019), PROPblock_2, reporting mass density (GLOBprop_1, kg/m³). This block contains 54 data points at 298.15 K spanning ethanol mole fractions from 0.003 to 1.0, with density decreasing monotonically from ~995.3 kg/m³ (near-pure water) to 785.7 kg/m³ (pure ethanol). The full 54-point dataset provides sufficient composition resolution for computing excess molar volumes. The same block contains 810 total data points covering 298.15–348.15 K and 100–40,000 kPa. Twenty-two total blocks of ethanol+water binary density data near 298.15 K were found across multiple literature sources for cross-validation.",
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
      "core_GLOB_id": "GLOBprop_1",
      "registry_id": "mass_density_kg_m3",
      "name": "Mass density, kg/m3"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_220",
      "registry_id": "2005-pec-dol-0",
      "name": "10.1016/j.fluid.2004.11.019"
    }
  ],
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
      "description": "Mass density (kg/m³) of ethanol + water binary mixture; 54 data points at 298.15 K and 100 kPa spanning ethanol mole fraction 0.003 to 1.0; 810 total points across 298.15–348.15 K and 100–40000 kPa.",
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
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0184",
          "mass_density_kg_m3": "988.4"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0219",
          "mass_density_kg_m3": "987.6"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0279",
          "mass_density_kg_m3": "984.7"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0315",
          "mass_density_kg_m3": "984"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0366",
          "mass_density_kg_m3": "981.6"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0483",
          "mass_density_kg_m3": "977.5"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0516",
          "mass_density_kg_m3": "977.1"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0801",
          "mass_density_kg_m3": "968.6"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.0926",
          "mass_density_kg_m3": "965.6"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.1296",
          "mass_density_kg_m3": "954.9"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.2502",
          "mass_density_kg_m3": "918.5"
        },
        {
          "BLKpoint_id": "BLKpoint_40",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.3009",
          "mass_density_kg_m3": "904.5"
        },
        {
          "BLKpoint_id": "BLKpoint_41",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.35",
          "mass_density_kg_m3": "891.9"
        },
        {
          "BLKpoint_id": "BLKpoint_43",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.4501",
          "mass_density_kg_m3": "868.8"
        },
        {
          "BLKpoint_id": "BLKpoint_44",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.498",
          "mass_density_kg_m3": "859.3"
        },
        {
          "BLKpoint_id": "BLKpoint_45",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.5501",
          "mass_density_kg_m3": "849.5"
        },
        {
          "BLKpoint_id": "BLKpoint_47",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.6489",
          "mass_density_kg_m3": "832.7"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.6967",
          "mass_density_kg_m3": "825.2"
        },
        {
          "BLKpoint_id": "BLKpoint_51",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "0.8484",
          "mass_density_kg_m3": "804.4"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "temperature_k": "298.15",
          "pressure_kpa": "100",
          "mole_fraction_<ethanol>": "1",
          "mass_density_kg_m3": "785.7"
        }
      ],
      "inspection_id": "INSP_1061f889512c",
      "lit_num_id": "GLOBlit_220"
    }
  ]
}