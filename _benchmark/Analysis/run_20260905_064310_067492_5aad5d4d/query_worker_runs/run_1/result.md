{
  "answer": "Viscosity data for the ternary mixture of N,N-dimethylformamide (DMF) + ethylene glycol (1,2-ethanediol) + water at 298.15 K were found in the ThermoML database.\n\n**Source:** DOI 10.1021/je060113j (GLOBlit_8892), PROPblock_38  \n**Method:** Capillary tube (Ostwald–Ubbelohde), liquid phase  \n**Pressure:** 101.0 kPa (fixed constraint)  \n**Compounds:** DMF (GLOBcomp_18), 1,2-ethanediol (GLOBcomp_24), water (GLOBcomp_1)\n\nThere are **11 data points at 298.15 K** spanning the full water mole-fraction range from 0 to 1 (the third component, DMF, makes up the balance). The data are tabulated below:\n\n| x(water) | x(1,2-ethanediol) | Viscosity (Pa·s) |\n|---|---|---|\n| 0.0000 | 0.5408 | 0.0030647 |\n| 0.2929 | 0.3824 | 0.0035692 |\n| 0.4825 | 0.2799 | 0.0037485 |\n| 0.6152 | 0.2081 | 0.0034817 |\n| 0.7132 | 0.1551 | 0.0032008 |\n| 0.7886 | 0.1143 | 0.0028546 |\n| 0.8484 | 0.0820 | 0.0024439 |\n| 0.8969 | 0.0557 | 0.0019531 |\n| 0.9372 | 0.0339 | 0.0016778 |\n| 0.9711 | 0.0156 | 0.0013057 |\n| 1.0000 | 0.0000 | 0.0008904 |\n\n**Chemistry insight:** The viscosity exhibits a non-monotonic trend with composition. Starting from the DMF + ethylene glycol binary end (x_water = 0, η = 0.0030647 Pa·s), the viscosity increases as water is added, reaching a maximum of 0.0037485 Pa·s near x(water) ≈ 0.48. Beyond this composition, the viscosity decreases steadily as the mixture becomes more water-rich, dropping to 0.0008904 Pa·s for pure water. This maximum in viscosity at intermediate compositions is characteristic of strongly hydrogen-bonding ternary systems, where the interplay of DMF–water and ethylene glycol–water interactions enhances intermolecular association beyond what either binary pair alone would produce.\n\nThe full block contains 33 data points covering temperatures from 298.15 K to 318.15 K, with viscosity values ranging from 0.000596 to 0.0037485 Pa·s across all temperatures and compositions.",
  "core_claims": [
    "Viscosity data for the ternary mixture DMF + ethylene glycol + water at 298.15 K and 101.0 kPa were found in the ThermoML database (DOI 10.1021/je060113j), comprising 11 data points spanning the full water mole-fraction range from 0 to 1.",
    "The viscosity exhibits a non-monotonic trend with composition: starting at 0.0030647 Pa·s for the DMF + ethylene glycol binary end (x_water = 0), it increases to a maximum of 0.0037485 Pa·s near x(water) ≈ 0.48, then decreases steadily to 0.0008904 Pa·s for pure water.",
    "The viscosity maximum at intermediate compositions is attributed to strongly hydrogen-bonding interactions in the ternary system, where DMF–water and ethylene glycol–water interactions enhance intermolecular association beyond what either binary pair alone would produce.",
    "The full data block contains 33 data points covering temperatures from 298.15 K to 318.15 K, with viscosity values ranging from 0.000596 to 0.0037485 Pa·s across all temperatures and compositions."
  ],
  "status": "success",
  "summary": "Viscosity data for the ternary mixture of N,N-dimethylformamide (DMF) + ethylene glycol (1,2-ethanediol) + water at 298.15 K were found in the ThermoML database (DOI 10.1021/je060113j, GLOBlit_8892, PROPblock_38). Measured by capillary tube (Ostwald–Ubbelohde) in the liquid phase at 101.0 kPa, 11 data points at 298.15 K span the full water mole-fraction range from 0 to 1. Viscosity values are: x(water)=0.0000, x(ethanediol)=0.5408, η=0.0030647 Pa·s; x(water)=0.2929, x(ethanediol)=0.3824, η=0.0035692 Pa·s; x(water)=0.4825, x(ethanediol)=0.2799, η=0.0037485 Pa·s; x(water)=0.6152, x(ethanediol)=0.2081, η=0.0034817 Pa·s; x(water)=0.7132, x(ethanediol)=0.1551, η=0.0032008 Pa·s; x(water)=0.7886, x(ethanediol)=0.1143, η=0.0028546 Pa·s; x(water)=0.8484, x(ethanediol)=0.0820, η=0.0024439 Pa·s; x(water)=0.8969, x(ethanediol)=0.0557, η=0.0019531 Pa·s; x(water)=0.9372, x(ethanediol)=0.0339, η=0.0016778 Pa·s; x(water)=0.9711, x(ethanediol)=0.0156, η=0.0013057 Pa·s; x(water)=1.0000, x(ethanediol)=0.0000, η=0.0008904 Pa·s. The viscosity shows a non-monotonic trend, rising from 0.0030647 Pa·s at x(water)=0 to a maximum of 0.0037485 Pa·s near x(water)≈0.48, then decreasing to 0.0008904 Pa·s for pure water, characteristic of strongly hydrogen-bonding ternary systems. The full data block contains 33 points covering 298.15 K to 318.15 K with viscosities ranging from 0.000596 to 0.0037485 Pa·s.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_18",
      "registry_id": "dimethylformamide",
      "name": "dimethylformamide"
    },
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
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_8892",
      "registry_id": "2006-sin-roy-0",
      "name": "10.1021/je060113j"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_8892",
      "block_number": "PROPblock_38",
      "BLKsubsys_id": null,
      "system_type": "ternary",
      "comp_num_ids": [
        "GLOBcomp_18",
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity measurements for the ternary mixture N,N-dimethylformamide + 1,2-ethanediol + water at 298.15 K and 101.0 kPa, with 11 data points spanning the full water mole-fraction range.",
      "doi": "10.1021/je060113j",
      "lit_id": "2006-sin-roy-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_3",
      "n_datapoints": 33,
      "n_components": 3,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_4_1"
        },
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
            "max": 318.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 318.15
        },
        {
          "BLKvar_id": "BLKvar_2",
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
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 11
          },
          "range_min": 0.0,
          "range_max": 1.0
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
            "min": 0.0,
            "max": 0.5408,
            "n_unique": 11
          },
          "range_min": 0.0,
          "range_max": 0.5408
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
            "min": 0.000596,
            "max": 0.003749,
            "mean": 0.002038,
            "std": 0.000839,
            "n": 33
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000596,
          "range_max": 0.003749
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
      "declared_system_type": "ternary",
      "declared_n_components": 3,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_18",
          "name": "dimethylformamide",
          "formula": "C3H7NO",
          "inchi_key": "ZMXDDKWLCZADIW-UHFFFAOYSA-N",
          "SMILES": "CN(C)C=O",
          "sample_num": "DOIcompSample_4_1"
        },
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
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_6_1"
        }
      ],
      "parent_n_datapoints": 33,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1021/je060113j",
      "block_number": "PROPblock_38",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<water>",
        "mole_fraction_<1,2-ethanediol>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0",
          "mole_fraction_<1,2-ethanediol>": "0.5408",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0030647"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.2929",
          "mole_fraction_<1,2-ethanediol>": "0.3824",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0035692"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.4825",
          "mole_fraction_<1,2-ethanediol>": "0.2799",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0037485"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.6152",
          "mole_fraction_<1,2-ethanediol>": "0.2081",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0034817"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.7132",
          "mole_fraction_<1,2-ethanediol>": "0.1551",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0032008"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.7886",
          "mole_fraction_<1,2-ethanediol>": "0.1143",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0028546"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.8484",
          "mole_fraction_<1,2-ethanediol>": "0.082",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0024439"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.8969",
          "mole_fraction_<1,2-ethanediol>": "0.0557",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0019531"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.9372",
          "mole_fraction_<1,2-ethanediol>": "0.0339",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0016778"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.9711",
          "mole_fraction_<1,2-ethanediol>": "0.0156",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0013057"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "1",
          "mole_fraction_<1,2-ethanediol>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0008904"
        }
      ],
      "inspection_id": "INSP_ccb7677d8622",
      "lit_num_id": "GLOBlit_8892"
    }
  ]
}