{
  "answer": "## Density (Mass Density) Data for Methanol + Water Binary Mixtures near 298.15 K\n\nTen data blocks were found in the ThermoML database for the binary system methanol (GLOBcomp_4) + water (GLOBcomp_1) with mass density (GLOBprop_1, kg/m³) measurements that include or approach 298.15 K. The three best candidates for atmospheric-pressure density across the composition range at 298.15 K are detailed below, followed by a summary of additional blocks.\n\n---\n\n### Top 3 Candidates (Inspected)\n\n**1. GLOBlit_2825 / PROPblock_10** — DOI: 10.1016/j.jct.2007.05.004\n\n- **Points:** 39 total\n- **T range:** 293.15–303.15 K\n- **Composition range:** x(water) = 0–1 (full range, including pure endpoints)\n- **ρ range:** 782.48–998.2 kg/m³\n- **Pressure:** 101.0 kPa (constrained)\n\nRepresentative data at 298.15 K (from inspection):\n\n| x(water) | ρ (kg/m³) |\n|-----------|-----------|\n| 0         | 787.2     |\n| 0.2983    | 840.79    |\n| 0.5003    | 881.69    |\n| 0.8999    | 969.84    |\n| 1         | 997.05    |\n\nThis block offers the best composition coverage, spanning from pure methanol to pure water at three temperatures.\n\n---\n\n**2. GLOBlit_8424 / PROPblock_3** — DOI: 10.1021/je049691v\n\n- **Points:** 180 total\n- **T range:** 283.15–353.15 K\n- **Composition range:** x(water) = 0.08–0.9603\n- **ρ range:** 747.01–988.05 kg/m³\n\nRepresentative data at 298.15 K (from inspection):\n\n| x(water) | ρ (kg/m³) |\n|-----------|-----------|\n| 0.08      | 800.1     |\n| 0.4799    | 876.94    |\n| 0.9603    | 985.01    |\n\nThis block has the largest total point count (180) and spans a wide temperature range, making it excellent for temperature-dependent studies as well.\n\n---\n\n**3. GLOBlit_10866 / PROPblock_6** — DOI: 10.1021/je700300y\n\n- **Points:** 84 total\n- **T range:** 283.15–313.15 K\n- **Composition range:** x(water) = 0.0871–0.964\n- **ρ range:** 787.52–988.96 kg/m³\n- **Pressure:** 101.0 kPa (constrained)\n\nRepresentative data at 298.15 K (from inspection):\n\n| x(water) | ρ (kg/m³) |\n|-----------|-----------|\n| 0.0871    | 801.35    |\n| 0.4788    | 876.68    |\n| 0.964     | 986       |\n\n---\n\n### Additional Blocks (Not Individually Inspected)\n\nThe following blocks were returned by the search but were not inspected for individual data rows. No specific numerical values are quoted for these blocks.\n\n| DOI | Literature ID | Block | Brief Description |\n|-----|---------------|-------|-------------------|\n| 10.1021/je0601098 | GLOBlit_8888 | PROPblock_18 | Solvent=methanol, fixed T |\n| 10.1021/je0600810 | GLOBlit_8869 | PROPblock_4 | Volume fraction basis |\n| 10.1021/acs.jced.6b01058 | GLOBlit_7085 | PROPblock_6 | Narrow composition range |\n| 10.1021/je2003622 | GLOBlit_9571 | PROPblock_2 | Mass fraction basis |\n| 10.1016/j.jct.2004.07.019 | GLOBlit_2432 | PROPblock_1 | High-pressure, Δρ values |\n| 10.1016/j.jct.2019.05.013 | GLOBlit_5533 | PROPblock_2 | Below 298 K |\n| 10.1021/je034101z | GLOBlit_8254 | PROPblock_4 | High T, high P — less relevant for 298 K |\n\n---\n\n### Summary\n\nFor atmospheric-pressure density of methanol + water at 298.15 K across the full composition range, **GLOBlit_2825 / PROPblock_10** is the best single source (full x = 0–1 coverage at 101.0 kPa). **GLOBlit_8424 / PROPblock_3** provides the most data points overall (180) with broad temperature coverage. All three top blocks show the expected non-linear density–composition behavior characteristic of the methanol–water system, with density increasing monotonically from methanol-rich to water-rich compositions.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNINSPECTED_BLOCK** PROPblock_1: PROPblock_1 is quoted with data values (298.15, …) but was never inspected in this run\n  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_1\", literature=\"<GLOBlit_N or DOI>\")`\nInspected so far: PROPblock_10, PROPblock_3, PROPblock_6",
  "core_claims": [
    "Ten ThermoML data blocks were identified for mass density of the methanol + water binary system near 298.15 K, with three blocks inspected in detail.",
    "GLOBlit_2825 / PROPblock_10 (DOI 10.1016/j.jct.2007.05.004) provides the best single-source composition coverage, spanning x(water) = 0–1 at 101.0 kPa and 298.15 K, with densities ranging from 787.2 kg/m³ (pure methanol) to 997.05 kg/m³ (pure water).",
    "GLOBlit_8424 / PROPblock_3 (DOI 10.1021/je049691v) has the largest total point count (180 points) covering 283.15–353.15 K and x(water) = 0.08–0.9603.",
    "GLOBlit_10866 / PROPblock_6 (DOI 10.1021/je700300y) covers x(water) = 0.0871–0.964 at 101.0 kPa across 283.15–313.15 K with 84 points.",
    "All three inspected blocks show density increasing monotonically from methanol-rich to water-rich compositions at 298.15 K.",
    "Seven additional blocks were returned by the search but were not individually inspected, so no specific numerical values are quoted for them; one block (PROPblock_1) was flagged as UNVERIFIED because data values attributed to it were never confirmed by inspection."
  ],
  "status": "success",
  "summary": "Ten ThermoML data blocks were identified for mass density (kg/m³) of the methanol + water binary system near 298.15 K. Three blocks were inspected in detail. GLOBlit_2825 / PROPblock_10 (DOI: 10.1016/j.jct.2007.05.004) is the best single source, covering x(water) = 0–1 at 101.0 kPa with 39 points across 293.15–303.15 K; representative 298.15 K values include 787.2 kg/m³ at x(water)=0 and 997.05 kg/m³ at x(water)=1. GLOBlit_8424 / PROPblock_3 (DOI: 10.1021/je049691v) has the most points (180) spanning 283.15–353.15 K and x(water) = 0.08–0.9603. GLOBlit_10866 / PROPblock_6 (DOI: 10.1021/je700300y) provides 84 points at 283.15–313.15 K and 101.0 kPa for x(water) = 0.0871–0.964. All three blocks show the expected monotonic, non-linear increase in density from methanol-rich to water-rich compositions. Seven additional blocks were returned but not individually inspected; these cover narrower composition or temperature ranges, different concentration bases, or high-pressure conditions.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2825",
      "block_number": "PROPblock_10",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of methanol + water at 293.15–303.15 K, x(water) = 0–1, 39 points, 101.0 kPa.",
      "doi": "10.1016/j.jct.2007.05.004",
      "lit_id": "2007-gon-cal-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 39,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
            "min": 782.48,
            "max": 998.2,
            "mean": 885.828974,
            "std": 72.087348,
            "n": 39
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 782.48,
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
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "parent_n_datapoints": 39,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8424",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of methanol + water at 283.15–353.15 K, x(water) = 0.08–0.9603, 180 points.",
      "doi": "10.1021/je049691v",
      "lit_id": "2005-coq-val-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 180,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
            "min": 283.15,
            "max": 353.15,
            "n_unique": 15
          },
          "range_min": 283.15,
          "range_max": 353.15
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
            "min": 0.08,
            "max": 0.9603,
            "n_unique": 12
          },
          "range_min": 0.08,
          "range_max": 0.9603
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
            "min": 747.01,
            "max": 988.05,
            "mean": 872.453667,
            "std": 63.746274,
            "n": 180
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 747.01,
          "range_max": 988.05
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
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "parent_n_datapoints": 180,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10866",
      "block_number": "PROPblock_6",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of methanol + water at 283.15–313.15 K, x(water) = 0.0871–0.964, 84 points, 101.0 kPa.",
      "doi": "10.1021/je700300y",
      "lit_id": "2007-zar-jal-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 84,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
            "min": 283.15,
            "max": 313.15,
            "n_unique": 7
          },
          "range_min": 283.15,
          "range_max": 313.15
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
            "min": 0.0871,
            "max": 0.964,
            "n_unique": 12
          },
          "range_min": 0.0871,
          "range_max": 0.964
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
            "min": 787.52,
            "max": 988.96,
            "mean": 888.204048,
            "std": 58.800933,
            "n": 84
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 787.52,
          "range_max": 988.96
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
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "parent_n_datapoints": 84,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8888",
      "block_number": "PROPblock_18",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of methanol + water; not individually inspected.",
      "doi": "10.1021/je0601098",
      "lit_id": "2006-kus-kol-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 12,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_9",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_9_1"
        }
      ],
      "solvents": [
        {
          "component_org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_4",
          "solvent_num_id": "GLOBsolvent_3",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N"
        }
      ],
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
        },
        {
          "BLKconstr_id": "BLKconstr_2",
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
        }
      ],
      "variables": [
        {
          "BLKvar_id": "BLKvar_1",
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_9",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_9",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Molality, mol/kg",
            "min": 0.0,
            "max": 1.01803,
            "n_unique": 12
          },
          "range_min": 0.0,
          "range_max": 1.01803
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
            "min": 786.66,
            "max": 791.86,
            "mean": 789.201167,
            "std": 1.65391,
            "n": 12
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 786.66,
          "range_max": 791.86
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_9",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_9_1"
        }
      ],
      "parent_n_datapoints": 12,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8869",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of methanol + water, volume fraction basis; not individually inspected.",
      "doi": "10.1021/je0600810",
      "lit_id": "2006-cha-das-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 9,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
          "var_num_id": "GLOBvar_18",
          "var_id": "volume_fraction_DOIcomp_1",
          "name": "Volume fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_1",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Volume fraction",
            "min": 0.01,
            "max": 0.3,
            "n_unique": 3
          },
          "range_min": 0.01,
          "range_max": 0.3
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
            "max": 318.15,
            "n_unique": 3
          },
          "range_min": 298.15,
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
          "meas_num_id": "GLOBmeas_141",
          "meas_ID": "vibtub_ufactor_8",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 946.26,
            "max": 982.97,
            "mean": 965.596667,
            "std": 12.754228,
            "n": 9
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 946.26,
          "range_max": 982.97
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
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "parent_n_datapoints": 9,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_7085",
      "block_number": "PROPblock_6",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of methanol + water, narrow composition range; not individually inspected.",
      "doi": "10.1021/acs.jced.6b01058",
      "lit_id": "2017-sha-cha-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 12,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_5_1"
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
          "value": 85.0,
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
            "max": 313.15,
            "n_unique": 4
          },
          "range_min": 298.15,
          "range_max": 313.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_2",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mass fraction",
            "min": 0.04,
            "max": 0.16,
            "n_unique": 3
          },
          "range_min": 0.04,
          "range_max": 0.16
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
            "min": 963.68,
            "max": 989.97,
            "mean": 978.324167,
            "std": 9.346563,
            "n": 12
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 963.68,
          "range_max": 989.97
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
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_5_1"
        }
      ],
      "parent_n_datapoints": 12,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_9571",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of methanol + water, mass fraction basis; not individually inspected.",
      "doi": "10.1021/je2003622",
      "lit_id": "2011-bha-cha-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 16,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_1_1"
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
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_1",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_1",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Mass fraction",
            "min": 0.0806,
            "max": 0.3446,
            "n_unique": 4
          },
          "range_min": 0.0806,
          "range_max": 0.3446
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
            "max": 323.15,
            "n_unique": 4
          },
          "range_min": 298.15,
          "range_max": 323.15
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
          "meas_num_id": "GLOBmeas_280",
          "meas_ID": "pycnom_ufactor_6",
          "method_standard": null,
          "method_custom": "PYCNOM:UFactor:6",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 928.0,
            "max": 982.97,
            "mean": 956.21375,
            "std": 17.879212,
            "n": 16
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 928.0,
          "range_max": 982.97
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
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
          "sample_num": "DOIcompSample_1_1"
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
      "lit_num_id": "GLOBlit_2432",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of methanol + water, high-pressure Δρ values; not individually inspected.",
      "doi": "10.1016/j.jct.2004.07.019",
      "lit_id": "2004-hyn-hne-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 596,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "solvents": [
        {
          "component_org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "solvent_num_id": "GLOBsolvent_1",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N"
        }
      ],
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
            "min": 298.16,
            "max": 573.15,
            "n_unique": 16
          },
          "range_min": 298.16,
          "range_max": 573.15
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
            "min": 390.0,
            "max": 30320.0,
            "n_unique": 32
          },
          "range_min": 390.0,
          "range_max": 30320.0
        },
        {
          "BLKvar_id": "BLKvar_3",
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_5",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_5",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_3",
            "name": "Molality, mol/kg",
            "min": 0.07706,
            "max": 1.04694,
            "n_unique": 161
          },
          "range_min": 0.07706,
          "range_max": 1.04694
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
            "min": -13.3065,
            "max": -0.4632,
            "mean": -3.693235,
            "std": 2.632762,
            "n": 596
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -13.3065,
          "range_max": -0.4632
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
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "parent_n_datapoints": 596,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_5533",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of methanol + water, below 298 K; not individually inspected.",
      "doi": "10.1016/j.jct.2019.05.013",
      "lit_id": "2019-sem-sto-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 12,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_2",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Mass fraction",
            "min": 0.0,
            "max": 0.4999,
            "n_unique": 6
          },
          "range_min": 0.0,
          "range_max": 0.4999
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
            "min": 273.15,
            "max": 293.15,
            "n_unique": 3
          },
          "range_min": 273.15,
          "range_max": 293.15
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
            "min": 915.53,
            "max": 999.94,
            "mean": 961.621667,
            "std": 27.202688,
            "n": 12
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 915.53,
          "range_max": 999.94
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
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "parent_n_datapoints": 12,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8254",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of methanol + water, high T and high P; not individually inspected.",
      "doi": "10.1021/je034101z",
      "lit_id": "2003-kit-kag-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 401,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
            "min": 0.059,
            "max": 0.708,
            "n_unique": 4
          },
          "range_min": 0.059,
          "range_max": 0.708
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
            "min": 287.15,
            "max": 417.15,
            "n_unique": 131
          },
          "range_min": 287.15,
          "range_max": 417.15
        },
        {
          "BLKvar_id": "BLKvar_3",
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
            "BLKvar_id": "BLKvar_3",
            "name": "Pressure, kPa",
            "min": 3721.0,
            "max": 29927.0,
            "n_unique": 396
          },
          "range_min": 3721.0,
          "range_max": 29927.0
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
          "meas_num_id": "GLOBmeas_170",
          "meas_ID": "isochor",
          "method_standard": null,
          "method_custom": "ISOCHOR",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 762.2,
            "max": 966.0,
            "mean": 864.876808,
            "std": 56.871822,
            "n": 401
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 762.2,
          "range_max": 966.0
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
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": "CO",
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
      "parent_n_datapoints": 401,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1016/j.jct.2007.05.004",
      "block_number": "PROPblock_10",
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
          "mass_density_kg_m3": "791.9"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.1973",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "826.11"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.5003",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "885.57"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.8999",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "971.59"
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
          "mass_density_kg_m3": "787.2"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.2983",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "840.79"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.5003",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "881.69"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.8999",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "969.84"
        },
        {
          "BLKpoint_id": "BLKpoint_26",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "997.05"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "782.48"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.1973",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "817.31"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.5003",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "877.32"
        },
        {
          "BLKpoint_id": "BLKpoint_37",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.8999",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "967.9"
        },
        {
          "BLKpoint_id": "BLKpoint_39",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "1",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "995.65"
        }
      ],
      "inspection_id": "INSP_03fda493b40e",
      "lit_num_id": "GLOBlit_2825"
    },
    {
      "doi": "10.1021/je049691v",
      "block_number": "PROPblock_3",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<water>",
        "mass_density_kg_m3"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "283.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "813.74"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "283.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "988.05"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "288.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "809.22"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "288.15",
          "mole_fraction_<water>": "0.4799",
          "mass_density_kg_m3": "884.77"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "288.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "987.31"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "804.67"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.4799",
          "mass_density_kg_m3": "880.88"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "986.29"
        },
        {
          "BLKpoint_id": "BLKpoint_37",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "800.1"
        },
        {
          "BLKpoint_id": "BLKpoint_42",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.4799",
          "mass_density_kg_m3": "876.94"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "985.01"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "795.52"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.4799",
          "mass_density_kg_m3": "872.93"
        },
        {
          "BLKpoint_id": "BLKpoint_60",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "983.49"
        },
        {
          "BLKpoint_id": "BLKpoint_61",
          "temperature_k": "308.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "790.9"
        },
        {
          "BLKpoint_id": "BLKpoint_66",
          "temperature_k": "308.15",
          "mole_fraction_<water>": "0.4799",
          "mass_density_kg_m3": "868.86"
        },
        {
          "BLKpoint_id": "BLKpoint_72",
          "temperature_k": "308.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "981.76"
        },
        {
          "BLKpoint_id": "BLKpoint_73",
          "temperature_k": "313.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "786.24"
        },
        {
          "BLKpoint_id": "BLKpoint_78",
          "temperature_k": "313.15",
          "mole_fraction_<water>": "0.4799",
          "mass_density_kg_m3": "864.71"
        },
        {
          "BLKpoint_id": "BLKpoint_84",
          "temperature_k": "313.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "979.82"
        },
        {
          "BLKpoint_id": "BLKpoint_85",
          "temperature_k": "318.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "781.54"
        },
        {
          "BLKpoint_id": "BLKpoint_90",
          "temperature_k": "318.15",
          "mole_fraction_<water>": "0.4799",
          "mass_density_kg_m3": "860.49"
        },
        {
          "BLKpoint_id": "BLKpoint_96",
          "temperature_k": "318.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "977.69"
        },
        {
          "BLKpoint_id": "BLKpoint_97",
          "temperature_k": "323.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "776.8"
        },
        {
          "BLKpoint_id": "BLKpoint_103",
          "temperature_k": "323.15",
          "mole_fraction_<water>": "0.56",
          "mass_density_kg_m3": "874.24"
        },
        {
          "BLKpoint_id": "BLKpoint_108",
          "temperature_k": "323.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "975.39"
        },
        {
          "BLKpoint_id": "BLKpoint_109",
          "temperature_k": "328.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "772.01"
        },
        {
          "BLKpoint_id": "BLKpoint_115",
          "temperature_k": "328.15",
          "mole_fraction_<water>": "0.56",
          "mass_density_kg_m3": "870.01"
        },
        {
          "BLKpoint_id": "BLKpoint_120",
          "temperature_k": "328.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "972.92"
        },
        {
          "BLKpoint_id": "BLKpoint_121",
          "temperature_k": "333.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "767.16"
        },
        {
          "BLKpoint_id": "BLKpoint_127",
          "temperature_k": "333.15",
          "mole_fraction_<water>": "0.56",
          "mass_density_kg_m3": "865.69"
        },
        {
          "BLKpoint_id": "BLKpoint_132",
          "temperature_k": "333.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "970.28"
        },
        {
          "BLKpoint_id": "BLKpoint_133",
          "temperature_k": "338.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "762.24"
        },
        {
          "BLKpoint_id": "BLKpoint_139",
          "temperature_k": "338.15",
          "mole_fraction_<water>": "0.56",
          "mass_density_kg_m3": "861.28"
        },
        {
          "BLKpoint_id": "BLKpoint_144",
          "temperature_k": "338.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "967.5"
        },
        {
          "BLKpoint_id": "BLKpoint_145",
          "temperature_k": "343.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "757.24"
        },
        {
          "BLKpoint_id": "BLKpoint_151",
          "temperature_k": "343.15",
          "mole_fraction_<water>": "0.56",
          "mass_density_kg_m3": "856.77"
        },
        {
          "BLKpoint_id": "BLKpoint_156",
          "temperature_k": "343.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "964.57"
        },
        {
          "BLKpoint_id": "BLKpoint_157",
          "temperature_k": "348.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "752.17"
        },
        {
          "BLKpoint_id": "BLKpoint_163",
          "temperature_k": "348.15",
          "mole_fraction_<water>": "0.56",
          "mass_density_kg_m3": "852.18"
        },
        {
          "BLKpoint_id": "BLKpoint_168",
          "temperature_k": "348.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "961.5"
        },
        {
          "BLKpoint_id": "BLKpoint_169",
          "temperature_k": "353.15",
          "mole_fraction_<water>": "0.08",
          "mass_density_kg_m3": "747.01"
        },
        {
          "BLKpoint_id": "BLKpoint_175",
          "temperature_k": "353.15",
          "mole_fraction_<water>": "0.56",
          "mass_density_kg_m3": "847.48"
        },
        {
          "BLKpoint_id": "BLKpoint_180",
          "temperature_k": "353.15",
          "mole_fraction_<water>": "0.9603",
          "mass_density_kg_m3": "958.3"
        }
      ],
      "inspection_id": "INSP_43d32aeee409",
      "lit_num_id": "GLOBlit_8424"
    },
    {
      "doi": "10.1021/je700300y",
      "block_number": "PROPblock_6",
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
          "temperature_k": "283.15",
          "mole_fraction_<water>": "0.0871",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "814.96"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "283.15",
          "mole_fraction_<water>": "0.964",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "988.96"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "288.15",
          "mole_fraction_<water>": "0.0871",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "810.44"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "288.15",
          "mole_fraction_<water>": "0.4788",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "884.5"
        },
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "288.15",
          "mole_fraction_<water>": "0.964",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "988.25"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.0871",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "805.91"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.4788",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "880.62"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "temperature_k": "293.15",
          "mole_fraction_<water>": "0.964",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "987.25"
        },
        {
          "BLKpoint_id": "BLKpoint_37",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.0871",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "801.35"
        },
        {
          "BLKpoint_id": "BLKpoint_42",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.4788",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "876.68"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.964",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "986"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.0871",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "796.78"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.4788",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "872.67"
        },
        {
          "BLKpoint_id": "BLKpoint_60",
          "temperature_k": "303.15",
          "mole_fraction_<water>": "0.964",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "984.5"
        },
        {
          "BLKpoint_id": "BLKpoint_61",
          "temperature_k": "308.15",
          "mole_fraction_<water>": "0.0871",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "792.17"
        },
        {
          "BLKpoint_id": "BLKpoint_66",
          "temperature_k": "308.15",
          "mole_fraction_<water>": "0.4788",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "868.59"
        },
        {
          "BLKpoint_id": "BLKpoint_72",
          "temperature_k": "308.15",
          "mole_fraction_<water>": "0.964",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "982.79"
        },
        {
          "BLKpoint_id": "BLKpoint_73",
          "temperature_k": "313.15",
          "mole_fraction_<water>": "0.0871",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "787.52"
        },
        {
          "BLKpoint_id": "BLKpoint_79",
          "temperature_k": "313.15",
          "mole_fraction_<water>": "0.5552",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "881.28"
        },
        {
          "BLKpoint_id": "BLKpoint_84",
          "temperature_k": "313.15",
          "mole_fraction_<water>": "0.964",
          "pressure_kpa": "101.0",
          "mass_density_kg_m3": "980.87"
        }
      ],
      "inspection_id": "INSP_3d315ee91a65",
      "lit_num_id": "GLOBlit_10866"
    }
  ]
}