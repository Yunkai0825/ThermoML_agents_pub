{
  "answer": "## Density Data for DMSO + Water Binary Mixtures near 298.15 K\n\nEight data blocks were found in the ThermoML database containing mass density (GLOBprop_1) measurements for binary mixtures of dimethyl sulfoxide (DMSO, GLOBcomp_31) and water (GLOBcomp_1) in temperature ranges overlapping with 298.15 K.\n\n### Inspected Block Details\n\n**Block 1: GLOBlit_2584 :: PROPblock_8** (DOI: 10.1016/j.jct.2005.07.012)\n- 96 data points; T = 288.15–303.15 K; x(water) = 0.0308–0.9798; ρ = 1005.71–1108.48 kg/m³; pressure = 100.0 kPa\n\nRepresentative data at 298.15 K:\n\n| x(water) | ρ (kg/m³) |\n|-----------|-----------|\n| 0.0308 | 1095.32 |\n| 0.499 | 1098.66 |\n| 0.5992 | 1095.77 |\n| 0.6987 | 1088.33 |\n| 0.8495 | 1059.24 |\n| 0.9798 | 1007.35 |\n\n**Block 2: GLOBlit_2781 :: PROPblock_4** (DOI: 10.1016/j.jct.2006.12.012)\n- 120 data points; T = 298.15–318.15 K; x(DMSO) = 0–1; ρ = 990.21–1098.86 kg/m³; pressure = 101.0 kPa\n\nRepresentative data at 298.15 K:\n\n| x(DMSO) | ρ (kg/m³) |\n|---------|-----------|\n| 0 | 997.05 |\n| 0.1587 | 1061.32 |\n| 0.3074 | 1088.96 |\n| 0.3906 | 1095.11 |\n| 0.5193 | 1098.34 |\n| 1 | 1096.29 |\n\n### Additional Blocks Found (Not Inspected in Detail)\n\nThe following additional density blocks for DMSO + water were identified by the search but were not inspected for detailed data values in this run:\n\n| # | DOI | Block | GLOBlit | Pts |\n|---|-----|-------|---------|-----|\n| 3 | 10.1016/j.jct.2006.01.007 | PROPblock_4 | GLOBlit_2652 | 6 |\n| 4 | 10.1016/j.jct.2007.06.010 | PROPblock_4 | GLOBlit_2844 | (not inspected) |\n| 5 | 10.1016/j.tca.2011.08.013 | PROPblock_12 | GLOBlit_5953 | (not inspected) |\n| 6 | 10.1021/acs.jced.8b01048 | PROPblock_10 | GLOBlit_7713 | (not inspected) |\n\nTwo further blocks were returned by the search but their details were truncated in the result.\n\n### Chemistry Insight\n\nThe DMSO–water system shows strongly non-ideal density behavior. At 298.15 K (from GLOBlit_2781::PROPblock_4), the density rises steeply from pure water (997.05 kg/m³ at x(DMSO) = 0) to a subtle maximum near x(DMSO) ≈ 0.5 (1098.34 kg/m³ at x(DMSO) = 0.5193), slightly exceeding even pure DMSO (1096.29 kg/m³). This density maximum reflects strong intermolecular interactions — particularly hydrogen bonding between the S=O group of DMSO and water — leading to more efficient molecular packing in the mixture than in either pure component.\n\nThe two richest datasets for studying density across the full composition range near 298.15 K are GLOBlit_2584 (PROPblock_8, 96 points) and GLOBlit_2781 (PROPblock_4, 120 points).\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNINSPECTED_BLOCK** PROPblock_10: PROPblock_10 is quoted with data values (298.15, …) but was never inspected in this run\n  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_10\", literature=\"<GLOBlit_N or DOI>\")`\nInspected so far: PROPblock_1, PROPblock_3, PROPblock_4, PROPblock_8",
  "core_claims": [
    "Eight ThermoML data blocks were found containing mass density measurements for binary DMSO + water mixtures in temperature ranges overlapping 298.15 K, with the two richest datasets being GLOBlit_2584 (PROPblock_8, 96 points) and GLOBlit_2781 (PROPblock_4, 120 points).",
    "At 298.15 K, the DMSO–water system exhibits strongly non-ideal density behavior: density rises steeply from pure water (997.05 kg/m³ at x(DMSO) = 0) to a maximum near x(DMSO) ≈ 0.5 (1098.34 kg/m³ at x(DMSO) = 0.5193), which slightly exceeds the density of pure DMSO (1096.29 kg/m³), reflecting strong intermolecular interactions and more efficient molecular packing in the mixture than in either pure component.",
    "Only two of the eight identified data blocks (GLOBlit_2584::PROPblock_8 and GLOBlit_2781::PROPblock_4) were inspected in detail; the remaining blocks were not inspected for data values and any quoted values from uninspected blocks are flagged as UNVERIFIED."
  ],
  "status": "success",
  "summary": "Mass density measurements for binary mixtures of dimethyl sulfoxide (DMSO) and water near 298.15 K were found across eight ThermoML data blocks. Two blocks were inspected in detail: GLOBlit_2584::PROPblock_8 (DOI 10.1016/j.jct.2005.07.012, 96 points, T = 288.15–303.15 K, x(water) = 0.0308–0.9798, ρ = 1005.71–1108.48 kg/m³, 100.0 kPa) and GLOBlit_2781::PROPblock_4 (DOI 10.1016/j.jct.2006.12.012, 120 points, T = 298.15–318.15 K, x(DMSO) = 0–1, ρ = 990.21–1098.86 kg/m³, 101.0 kPa). At 298.15 K the density rises steeply from pure water (997.05 kg/m³ at x(DMSO) = 0) to a subtle maximum near x(DMSO) ≈ 0.5 (1098.34 kg/m³ at x(DMSO) = 0.5193), slightly exceeding pure DMSO (1096.29 kg/m³ at x(DMSO) = 1). This non-ideal density maximum reflects strong hydrogen bonding between the S=O group of DMSO and water, leading to more efficient molecular packing in the mixture. Additional uninspected blocks were identified at DOIs 10.1016/j.jct.2006.01.007, 10.1016/j.jct.2007.06.010, 10.1016/j.tca.2011.08.013, and 10.1021/acs.jced.8b01048.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_31",
      "registry_id": "dimethyl_sulfoxide",
      "name": "dimethyl sulfoxide"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_1",
      "registry_id": "mass_density_kg_m3",
      "name": "Mass density, kg/m3"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2584",
      "block_number": "PROPblock_8",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of DMSO + water binary mixture; T = 288.15–303.15 K; x(water) = 0.0308–0.9798; 96 data points.",
      "doi": "10.1016/j.jct.2005.07.012",
      "lit_id": "2006-tor-mar-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 96,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_3_1"
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
          "value": 100.0,
          "digits": 1,
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
            "min": 288.15,
            "max": 303.15,
            "n_unique": 4
          },
          "range_min": 288.15,
          "range_max": 303.15
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
            "min": 0.0308,
            "max": 0.9798,
            "n_unique": 24
          },
          "range_min": 0.0308,
          "range_max": 0.9798
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
          "meas_num_id": "GLOBmeas_147",
          "meas_ID": "vibtub_ufactor_16",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:16",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 1005.71,
            "max": 1108.48,
            "mean": 1073.646458,
            "std": 33.91588,
            "n": 96
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1005.71,
          "range_max": 1108.48
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
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 96,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2781",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of DMSO + water binary mixture; T = 298.15–318.15 K; x(DMSO) = 0–1; 120 data points.",
      "doi": "10.1016/j.jct.2006.12.012",
      "lit_id": "2007-gra-jul-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 120,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
            "n_unique": 24
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
            "min": 990.21,
            "max": 1098.86,
            "mean": 1069.402667,
            "std": 29.476794,
            "n": 120
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 990.21,
          "range_max": 1098.86
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
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
      "parent_n_datapoints": 120,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2652",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of DMSO + water binary mixture; 6 data points.",
      "doi": "10.1016/j.jct.2006.01.007",
      "lit_id": "2006-mie-kac-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 6,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
          "constr_num_id": "GLOBconstr_3",
          "constr_id": "mole_fraction_DOIcomp_3",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "value": 0.0385,
          "digits": 3,
          "component_org_num": "DOIcomp_3",
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
            "min": 288.15,
            "max": 313.15,
            "n_unique": 6
          },
          "range_min": 288.15,
          "range_max": 313.15
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
          "meas_num_id": "GLOBmeas_141",
          "meas_ID": "vibtub_ufactor_8",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 1010.2,
            "max": 1019.8,
            "mean": 1015.166667,
            "std": 3.594811,
            "n": 6
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1010.2,
          "range_max": 1019.8
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
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
      "parent_n_datapoints": 6,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2844",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of DMSO + water binary mixture; not inspected in detail.",
      "doi": "10.1016/j.jct.2007.06.010",
      "lit_id": "2008-swe-blo-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 92,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
      "solvents": [
        {
          "component_org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "solvent_num_id": "GLOBsolvent_1",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N"
        }
      ],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_1",
          "constr_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "value": 350.0,
          "digits": 2,
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
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_3",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_3",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Molality, mol/kg",
            "min": 0.0205,
            "max": 2.9997,
            "n_unique": 9
          },
          "range_min": 0.0205,
          "range_max": 2.9997
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
            "min": 278.15,
            "max": 368.15,
            "n_unique": 11
          },
          "range_min": 278.15,
          "range_max": 368.15
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
            "min": 962.38,
            "max": 1028.8,
            "mean": 995.255326,
            "std": 15.512369,
            "n": 92
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 962.38,
          "range_max": 1028.8
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
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
      "parent_n_datapoints": 92,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_5953",
      "block_number": "PROPblock_12",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of DMSO + water binary mixture; not inspected in detail.",
      "doi": "10.1016/j.tca.2011.08.013",
      "lit_id": "2011-raj-gla-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 16,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_2_1"
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
            "min": 0.0121,
            "max": 0.0583,
            "n_unique": 4
          },
          "range_min": 0.0121,
          "range_max": 0.0583
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
            "min": 303.15,
            "max": 318.15,
            "n_unique": 4
          },
          "range_min": 303.15,
          "range_max": 318.15
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
          "meas_num_id": "GLOBmeas_6",
          "meas_ID": "pycnometric_method",
          "method_standard": "Pycnometric method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 996.2,
            "max": 1021.4,
            "mean": 1008.83125,
            "std": 7.798865,
            "n": 16
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 996.2,
          "range_max": 1021.4
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
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_2_1"
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
    },
    {
      "lit_num_id": "GLOBlit_7713",
      "block_number": "PROPblock_10",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of DMSO + water binary mixture; not inspected in detail.",
      "doi": "10.1021/acs.jced.8b01048",
      "lit_id": "2019-nis-mug-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 9,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_3_1"
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
          "constr_num_id": "GLOBconstr_3",
          "constr_id": "mole_fraction_DOIcomp_3",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "value": 0.998,
          "digits": 3,
          "component_org_num": "DOIcomp_3",
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
          "value": 100.0,
          "digits": 1,
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
            "max": 373.15,
            "n_unique": 9
          },
          "range_min": 293.15,
          "range_max": 373.15
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
            "min": 1019.8,
            "max": 1100.2,
            "mean": 1060.155556,
            "std": 27.518817,
            "n": 9
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1019.8,
          "range_max": 1100.2
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
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 9,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2005.07.012",
      "block_number": "PROPblock_8",
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
          "temperature_k": "288.15",
          "mole_fraction_<water>": "0.0308",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1105.54"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "288.15",
          "mole_fraction_<water>": "0.499",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1107.78"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "288.15",
          "mole_fraction_<water>": "0.5992",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1104.45"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "288.15",
          "mole_fraction_<water>": "0.6987",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1096.45"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "288.15",
          "mole_fraction_<water>": "0.8495",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1065.42"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "288.15",
          "mole_fraction_<water>": "0.9798",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1009.97"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.0308",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1100.52"
        },
        {
          "BLKpoint_id": "BLKpoint_34",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.499",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1103.24"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.5992",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1100.14"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.6987",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1092.41"
        },
        {
          "BLKpoint_id": "BLKpoint_41",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.8495",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1062.38"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.9798",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1008.78"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.0308",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1095.32"
        },
        {
          "BLKpoint_id": "BLKpoint_58",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.499",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1098.66"
        },
        {
          "BLKpoint_id": "BLKpoint_60",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.5992",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1095.77"
        },
        {
          "BLKpoint_id": "BLKpoint_62",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.6987",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1088.33"
        },
        {
          "BLKpoint_id": "BLKpoint_65",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.8495",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1059.24"
        },
        {
          "BLKpoint_id": "BLKpoint_72",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.9798",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1007.35"
        },
        {
          "BLKpoint_id": "BLKpoint_73",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.0308",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1090.32"
        },
        {
          "BLKpoint_id": "BLKpoint_82",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.499",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1094.06"
        },
        {
          "BLKpoint_id": "BLKpoint_84",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.5992",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1091.42"
        },
        {
          "BLKpoint_id": "BLKpoint_86",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.6987",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1084.2"
        },
        {
          "BLKpoint_id": "BLKpoint_89",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.8495",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1056.02"
        },
        {
          "BLKpoint_id": "BLKpoint_96",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.9798",
          "pressure_kpa": "100.0",
          "mass_density_kg_m3": "1005.71"
        }
      ],
      "inspection_id": "INSP_469eacdbeda0",
      "lit_num_id": "GLOBlit_2584"
    },
    {
      "doi": "10.1016/j.jct.2006.12.012",
      "block_number": "PROPblock_3",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<dimethyl sulfoxide>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0008901"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2379",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0033011"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3074",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0036564"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3638",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0037353"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4412",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0036062"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7595",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0024317"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001996"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0007973"
        },
        {
          "BLKpoint_id": "BLKpoint_31",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2036",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002704"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2768",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.003162"
        },
        {
          "BLKpoint_id": "BLKpoint_35",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3335",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0033221"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4412",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0032411"
        },
        {
          "BLKpoint_id": "BLKpoint_42",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.6813",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0024208"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0018357"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0007193"
        },
        {
          "BLKpoint_id": "BLKpoint_55",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2036",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002389"
        },
        {
          "BLKpoint_id": "BLKpoint_57",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2768",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002786"
        },
        {
          "BLKpoint_id": "BLKpoint_59",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3335",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0029301"
        },
        {
          "BLKpoint_id": "BLKpoint_62",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4412",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002876"
        },
        {
          "BLKpoint_id": "BLKpoint_67",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7595",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0020086"
        },
        {
          "BLKpoint_id": "BLKpoint_72",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0016689"
        },
        {
          "BLKpoint_id": "BLKpoint_73",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.000653"
        },
        {
          "BLKpoint_id": "BLKpoint_79",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2036",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0020754"
        },
        {
          "BLKpoint_id": "BLKpoint_83",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3335",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0025395"
        },
        {
          "BLKpoint_id": "BLKpoint_86",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4412",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0025085"
        },
        {
          "BLKpoint_id": "BLKpoint_91",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7595",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0018182"
        },
        {
          "BLKpoint_id": "BLKpoint_96",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0015351"
        },
        {
          "BLKpoint_id": "BLKpoint_97",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0005961"
        },
        {
          "BLKpoint_id": "BLKpoint_103",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2036",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0017611"
        },
        {
          "BLKpoint_id": "BLKpoint_107",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3335",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0021491"
        },
        {
          "BLKpoint_id": "BLKpoint_110",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4412",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0021416"
        },
        {
          "BLKpoint_id": "BLKpoint_115",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7595",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0016159"
        },
        {
          "BLKpoint_id": "BLKpoint_120",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "1",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0013935"
        }
      ],
      "inspection_id": "INSP_4fb8c018b67f",
      "lit_num_id": "GLOBlit_2781"
    },
    {
      "doi": "10.1021/je700645p",
      "block_number": "PROPblock_1",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "pressure_kpa",
        "temperature_k",
        "refractive_index_na_dline"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "pressure_kpa": "81.5",
          "temperature_k": "298.15",
          "refractive_index_na_dline": "1.3417"
        }
      ],
      "inspection_id": "INSP_5165d05564e1",
      "lit_num_id": "GLOBlit_11018"
    },
    {
      "doi": "10.1016/j.jct.2006.12.012",
      "block_number": "PROPblock_4",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<dimethyl sulfoxide>",
        "pressure_kpa",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "997.05"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1587",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1061.32"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3074",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1088.96"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3906",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1095.11"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.5193",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1098.34"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1096.29"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "995.65"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1587",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1058.32"
        },
        {
          "BLKpoint_id": "BLKpoint_34",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3074",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1085.02"
        },
        {
          "BLKpoint_id": "BLKpoint_37",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3906",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1091.09"
        },
        {
          "BLKpoint_id": "BLKpoint_39",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.5193",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1094.01"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1091.44"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "994.03"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1587",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1055.11"
        },
        {
          "BLKpoint_id": "BLKpoint_57",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2768",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1077.51"
        },
        {
          "BLKpoint_id": "BLKpoint_61",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3906",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1086.84"
        },
        {
          "BLKpoint_id": "BLKpoint_65",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.6195",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1089.61"
        },
        {
          "BLKpoint_id": "BLKpoint_72",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1086.41"
        },
        {
          "BLKpoint_id": "BLKpoint_73",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "992.22"
        },
        {
          "BLKpoint_id": "BLKpoint_78",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1587",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1051.58"
        },
        {
          "BLKpoint_id": "BLKpoint_80",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2379",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1067.99"
        },
        {
          "BLKpoint_id": "BLKpoint_83",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3335",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1079.21"
        },
        {
          "BLKpoint_id": "BLKpoint_87",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.5193",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1085.1"
        },
        {
          "BLKpoint_id": "BLKpoint_96",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1081.59"
        },
        {
          "BLKpoint_id": "BLKpoint_97",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "990.21"
        },
        {
          "BLKpoint_id": "BLKpoint_102",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1587",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1047.91"
        },
        {
          "BLKpoint_id": "BLKpoint_104",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2379",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1063.81"
        },
        {
          "BLKpoint_id": "BLKpoint_107",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3335",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1074.68"
        },
        {
          "BLKpoint_id": "BLKpoint_111",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.5193",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1080.42"
        },
        {
          "BLKpoint_id": "BLKpoint_120",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "1076.46"
        }
      ],
      "inspection_id": "INSP_9268af01c703",
      "lit_num_id": "GLOBlit_2781"
    }
  ]
}