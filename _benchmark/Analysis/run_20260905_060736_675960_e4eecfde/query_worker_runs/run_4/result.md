{
  "answer": "## Viscosity Data for Binary Water + Acetonitrile at 298.15 K\n\nA single data block was found in the ThermoML database:\n\n**Source:** DOI 10.1016/j.jct.2005.08.009 (GLOBlit_2602, PROPblock_3)  \n**Property:** Dynamic viscosity (Pa·s), liquid phase  \n**Method:** Capillary tube with U-factor (GLOBmeas_140)  \n**Constraint:** Pressure = 101.0 kPa  \n**System:** Binary — water (GLOBcomp_1) + acetonitrile (GLOBcomp_15)\n\nThe block contains 16 composition points at 298.15 K spanning the full mole fraction range of acetonitrile (0 to 1). The following shape-preserving subset was returned by inspection:\n\n| x(acetonitrile) | η (Pa·s) |\n|---|---|\n| 0 | 0.0008901 |\n| 0.051 | 0.0009849 |\n| 0.1169 | 0.0009567 |\n| 0.1971 | 0.0008743 |\n| 0.4417 | 0.0006061 |\n| 0.5204 | 0.0005387 |\n| 0.6012 | 0.0004802 |\n| 0.6671 | 0.0004415 |\n| 0.7398 | 0.0004064 |\n| 0.8253 | 0.0003722 |\n| 0.886 | 0.0003561 |\n| 0.9389 | 0.0003478 |\n| 1.0 | 0.0003417 |\n\n**Chemical insight:** The viscosity shows a notable maximum near x(acetonitrile) ≈ 0.05 (η = 0.0009849 Pa·s), which exceeds the viscosity of pure water (0.0008901 Pa·s). This is characteristic of strong water–acetonitrile intermolecular interactions (hydrogen bonding between water and the nitrile group) at low acetonitrile concentrations, which enhance the local structure and resist flow. Beyond this maximum, viscosity decreases monotonically toward pure acetonitrile (0.0003417 Pa·s), which is considerably less viscous than water. The overall viscosity range at 298.15 K spans 0.0003417–0.0009849 Pa·s across 16 data points.",
  "core_claims": [
    "A single ThermoML data block (DOI 10.1016/j.jct.2005.08.009) reports dynamic viscosity of the binary water + acetonitrile system in the liquid phase at 298.15 K and 101.0 kPa, spanning 16 composition points from x(acetonitrile) = 0 to 1.",
    "The viscosity exhibits a maximum near x(acetonitrile) ≈ 0.05 (η = 0.0009849 Pa·s), exceeding the pure-water value of 0.0008901 Pa·s, attributed to strong water–acetonitrile hydrogen-bonding interactions that enhance local structure at low acetonitrile concentrations.",
    "Beyond the maximum, viscosity decreases monotonically with increasing acetonitrile mole fraction, reaching 0.0003417 Pa·s for pure acetonitrile, giving an overall range of 0.0003417–0.0009849 Pa·s across the composition span."
  ],
  "status": "success",
  "summary": "Dynamic viscosity data for the binary system water + acetonitrile at 298.15 K and 101.0 kPa were found in a single ThermoML data block (DOI 10.1016/j.jct.2005.08.009, GLOBlit_2602, PROPblock_3), measured by capillary tube with U-factor (GLOBmeas_140). The block contains 16 composition points spanning the full mole fraction range of acetonitrile (0 to 1). Viscosity exhibits a maximum near x(acetonitrile) ≈ 0.05 (0.0009849 Pa·s), exceeding that of pure water (0.0008901 Pa·s), attributed to strong water–acetonitrile hydrogen-bonding interactions. Beyond this maximum, viscosity decreases monotonically to pure acetonitrile (0.0003417 Pa·s). The overall viscosity range is 0.0003417–0.0009849 Pa·s.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_15",
      "registry_id": "acetonitrile",
      "name": "acetonitrile"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_4",
      "registry_id": "viscosity_pa_s",
      "name": "Viscosity, Pa*s"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_2602",
      "registry_id": "2006-gra-jul-0",
      "name": "10.1016/j.jct.2005.08.009"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBmeas_140",
      "registry_id": "captub_ufactor_2",
      "name": "CAPTUB:UFactor:2"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2602",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_15",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity measurements for binary water + acetonitrile at 298.15 K across the full mole fraction range (16 composition points), measured by capillary tube method at 101.0 kPa.",
      "doi": "10.1016/j.jct.2005.08.009",
      "lit_id": "2006-gra-jul-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 80,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_15",
          "name": "acetonitrile",
          "formula": "C2H3N",
          "inchi_key": "WEVYAHXRMPXWCK-UHFFFAOYSA-N",
          "SMILES": "CC#N",
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
            "min": 298.15,
            "max": 318.15,
            "n_unique": 5
          },
          "range_min": 298.15,
          "range_max": 318.15
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
            "n_unique": 16
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
            "min": 0.00029,
            "max": 0.000985,
            "mean": 0.000506,
            "std": 0.000191,
            "n": 80
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.00029,
          "range_max": 0.000985
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
          "comp_num_id": "GLOBcomp_15",
          "name": "acetonitrile",
          "formula": "C2H3N",
          "inchi_key": "WEVYAHXRMPXWCK-UHFFFAOYSA-N",
          "SMILES": "CC#N",
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
      "parent_n_datapoints": 80,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2005.08.009",
      "block_number": "PROPblock_3",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<acetonitrile>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0008901"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.051",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0009849"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.1169",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0009567"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.1971",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0008743"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.4417",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0006061"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.5204",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0005387"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.6012",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0004802"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.6671",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0004415"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.7398",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0004064"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.8253",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0003722"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.886",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0003561"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "0.9389",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0003478"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "298.15",
          "mole_fraction_<acetonitrile>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0003417"
        }
      ],
      "inspection_id": "INSP_98abce7cba9c",
      "lit_num_id": "GLOBlit_2602"
    }
  ]
}