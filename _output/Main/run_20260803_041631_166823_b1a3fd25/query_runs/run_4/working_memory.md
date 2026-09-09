# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find density (GLOBprop_1) data blocks for binary water+DMSO mixtures → stored as L1_query_1
- [L1] Find viscosity (GLOBprop_4) data blocks for binary water+DMSO mixtures → stored as L1_query_2
- [L1] Find surface tension data for binary water+DMSO mixtures → stored as L1_query_3
- [L1] Find electrical conductivity data for binary water+DMSO mixtures → stored as L1_query_4
- [L1] Find excess molar volume or excess molar enthalpy data for binary water+DMSO mixtures → stored as L1_query_5

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
{
  "answer": "Nine binary water (GLOBcomp_1) + dimethyl sulfoxide (GLOBcomp_31) data blocks reporting mass density (GLOBprop_1) were found in the ThermoML database, spanning 9 distinct DOIs and totaling 484 raw data points. All blocks are liquid-phase measurements. Here are the matching blocks:\n\n1. **DOI 10.1016/j.jct.2005.07.012** — GLOBlit_2584, PROPblock_8  \n   - Temperature: 288.15–298.15 K  \n   - Composition: x(water) = 0.0308–0.9798  \n   - Raw data points: 96  \n\n2. **DOI 10.1016/j.jct.2006.01.007** — GLOBlit_2652, PROPblock_4  \n   - Temperature: 288.15–313.15 K  \n   - Composition: fixed mole fraction (set as constraint)  \n   - Raw data points: 6  \n\n3. **DOI 10.1016/j.jct.2006.12.012** — GLOBlit_2781, PROPblock_4  \n   - Temperature: 298.15–308.15 K  \n   - Composition: x(DMSO) = 0–1 (full range)  \n   - Raw data points: 120  \n\n4. **DOI 10.1016/j.jct.2007.06.007** — GLOBlit_2842, PROPblock_6  \n   - Temperature: 275.15–283.15 K  \n   - Composition: x(DMSO) = 0–0.6967  \n   - Raw data points: 40  \n\n5. **DOI 10.1016/j.jct.2007.06.010** — GLOBlit_2844, PROPblock_4  \n   - Temperature: 278.15–368.15 K  \n   - Composition: b(DMSO) = 0.0205–1.0002 (molality basis)  \n   - Raw data points: 92  \n\n6. **DOI 10.1016/j.tca.2011.08.013** — GLOBlit_5953, PROPblock_12  \n   - Temperature: 303.15–318.15 K  \n   - Composition: x(DMSO) = 0.0121–0.0583 (dilute DMSO region)  \n   - Raw data points: 16  \n\n7. **DOI 10.1021/acs.jced.8b01048** — GLOBlit_7713, PROPblock_10  \n   - Temperature: 293.15–373.15 K  \n   - (Composition and point count truncated in results)  \n\nTwo additional blocks (blocks 8 and 9) were returned but their details were truncated in the search output. The total across all 9 blocks is 484 raw data points.\n\n**Chemistry note:** The water–DMSO binary system is well studied because DMSO is fully miscible with water and the mixture exhibits notable non-ideal behavior — density passes through a maximum near x(DMSO) ≈ 0.3 at room temperature, reflecting strong hydrogen-bonding interactions between water and the S=O group of DMSO. The dataset covers temperatures from 275 K to 373 K and compositions from pure water to pure DMSO, providing broad coverage for thermodynamic modeling.",
  "core_claims": [
    "Nine binary water + dimethyl sulfoxide data blocks reporting liquid-phase mass density were identified in the ThermoML database, spanning 9 distinct DOIs and totaling 484 raw data points.",
    "The dataset covers temperatures from approximately 275 K to 373 K and compositions ranging from pure water to pure DMSO, providing broad coverage for thermodynamic modeling.",
    "The water–DMSO binary system exhibits notable non-ideal behavior, with density passing through a maximum near x(DMSO) ≈ 0.3 at room temperature, attributed to strong hydrogen-bonding interactions between water and the S=O group of DMSO.",
    "All reported blocks are liquid-phase measurements; two of the nine blocks had details truncated in the search output."
  ],
  "status": "partial",
  "summary": "Nine ThermoML data blocks (484 raw data points across 9 DOIs) report liquid-phase mass density for the binary water + dimethyl sulfoxide (DMSO) system. Coverage spans temperatures from approximately 275 K to 373 K and compositions from pure water to pure DMSO, expressed variously as mole fraction or molality. Key sources include DOI 10.1016/j.jct.2005.07.012 (96 points, 288–298 K, broad composition), DOI 10.1016/j.jct.2006.12.012 (120 points, 298–308 K, full composition range), DOI 10.1016/j.jct.2007.06.010 (92 points, 278–368 K, molality basis), and DOI 10.1016/j.jct.2007.06.007 (40 points, 275–283 K, x(DMSO) up to ~0.70), among others. The system is fully miscible and exhibits non-ideal density behavior, with a density maximum near x(DMSO) ≈ 0.3 at room temperature attributed to strong water–DMSO hydrogen bonding.",
  "core_id_updates": [],
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
      "description": "Mass density of binary water+DMSO mixture. DOI 10.1016/j.jct.2005.07.012. T: 288.15–298.15 K, x(water) 0.0308–0.9798, 96 raw data points.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
      "description": "Mass density of binary water+DMSO mixture. DOI 10.1016/j.jct.2006.01.007. T: 288.15–313.15 K, fixed mole fraction (constraint), 6 raw data points.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
      "description": "Mass density of binary water+DMSO mixture. DOI 10.1016/j.jct.2006.12.012. T: 298.15–308.15 K, x(DMSO) 0–1 (full range), 120 raw data points.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
      "lit_num_id": "GLOBlit_2842",
      "block_number": "PROPblock_6",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary water+DMSO mixture. DOI 10.1016/j.jct.2007.06.007. T: 275.15–283.15 K, x(DMSO) 0–0.6967, 40 raw data points.",
      "doi": "10.1016/j.jct.2007.06.007",
      "lit_id": "2008-dho-pan-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 40,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
            "min": 275.15,
            "max": 283.15,
            "n_unique": 5
          },
          "range_min": 275.15,
          "range_max": 283.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_3",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_3",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 0.6967,
            "n_unique": 8
          },
          "range_min": 0.0,
          "range_max": 0.6967
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
            "min": 999.7,
            "max": 1158.3,
            "mean": 1077.585,
            "std": 44.008761,
            "n": 40
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 999.7,
          "range_max": 1158.3
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
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 40,
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
      "description": "Mass density of binary water+DMSO mixture. DOI 10.1016/j.jct.2007.06.010. T: 278.15–368.15 K, b(DMSO) 0.0205–1.0002 (molality basis), 92 raw data points.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
      "description": "Mass density of binary water+DMSO mixture. DOI 10.1016/j.tca.2011.08.013. T: 303.15–318.15 K, x(DMSO) 0.0121–0.0583 (dilute DMSO region), 16 raw data points.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
      "description": "Mass density of binary water+DMSO mixture. DOI 10.1021/acs.jced.8b01048. T: 293.15–373.15 K. Details truncated in search output; 2 additional blocks also truncated. Only 7 of 9 reported blocks are fully documented.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
  ]
}
### L1_query_2
{
  "answer": "Three binary water (GLOBcomp_1) + dimethyl sulfoxide (GLOBcomp_31) data blocks reporting dynamic viscosity (GLOBprop_4, Pa·s) were found in the ThermoML database. All are liquid-phase measurements at approximately 101 kPa.\n\n1. **DOI 10.1016/j.jct.2006.12.012** — GLOBlit_2781, PROPblock_3\n   - Temperature: 298.15–308.15 K (3 temperatures)\n   - Composition: x(DMSO) = 0.0–1.0 (full mole-fraction range, 24 unique compositions)\n   - Raw data points: 120\n   - Composition variable: mole fraction of DMSO\n\n2. **DOI 10.1016/j.tca.2011.08.013** — GLOBlit_5953, PROPblock_10\n   - Temperature: 303.15–318.15 K (4 temperatures)\n   - Composition: x(DMSO) = 0.0121–0.0583 (dilute DMSO region only)\n   - Raw data points: 16\n   - Composition variable: mole fraction of DMSO\n\n3. **DOI 10.1021/je9001027** — GLOBlit_11517, PROPblock_3\n   - Temperature: 298.15–318.15 K (5 temperatures)\n   - Composition: w(DMSO) = 0.0–1.0 (full mass-fraction range)\n   - Raw data points: 35\n   - Composition variable: mass fraction of DMSO\n\n**Total:** 3 data blocks across 3 distinct DOIs, totaling 171 raw data points, covering temperatures from 298 K to 318 K.\n\n**Chemistry note:** The water–DMSO binary system exhibits strongly non-ideal viscosity behavior. The dynamic viscosity passes through a pronounced maximum near x(DMSO) ≈ 0.3 at room temperature — the same composition region where the density maximum occurs — reflecting the formation of strong hydrogen-bonded water–DMSO complexes (often described as 1:2 DMSO:water stoichiometry). This viscosity maximum can be several times larger than the viscosity of either pure component, making the system a classic example of non-ideal mixing in transport properties.",
  "core_claims": [
    "Three binary water + dimethyl sulfoxide data blocks reporting dynamic viscosity (Pa·s) were identified in the ThermoML database, spanning 3 distinct DOIs and totaling 171 raw data points, all for liquid-phase measurements at approximately 101 kPa and temperatures from 298 K to 318 K.",
    "The three data blocks differ in composition coverage: one covers the full DMSO mole-fraction range (0.0–1.0), one covers only the dilute DMSO region (x(DMSO) = 0.0121–0.0583), and one covers the full mass-fraction range (0.0–1.0).",
    "The water–DMSO binary system exhibits strongly non-ideal viscosity behavior, with dynamic viscosity passing through a pronounced maximum near x(DMSO) ≈ 0.3 at room temperature, attributed to the formation of strong hydrogen-bonded water–DMSO complexes (often described as 1:2 DMSO:water stoichiometry), resulting in viscosities several times larger than those of either pure component."
  ],
  "status": "success",
  "summary": "Three ThermoML data blocks from three distinct DOIs report dynamic viscosity (Pa·s) for the binary water + dimethyl sulfoxide system, all in the liquid phase at approximately 101 kPa. The first (DOI 10.1016/j.jct.2006.12.012) covers 298.15–308.15 K across the full DMSO mole-fraction range (120 points). The second (DOI 10.1016/j.tca.2011.08.013) covers 303.15–318.15 K in the dilute DMSO region only (16 points). The third (DOI 10.1021/je9001027) covers 298.15–318.15 K across the full DMSO mass-fraction range (35 points). In total there are 171 data points spanning 298–318 K. The system is strongly non-ideal: dynamic viscosity passes through a pronounced maximum near x(DMSO) ≈ 0.3, several times larger than either pure-component value, attributed to strong hydrogen-bonded water–DMSO complex formation.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2781",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity (Pa·s) of binary water + DMSO mixture. DOI 10.1016/j.jct.2006.12.012. Temperature range 298.15–308.15 K (3 temperatures), full mole-fraction range x(DMSO) = 0.0–1.0 (24 unique compositions), 120 raw data points. Liquid phase at 101 kPa. Composition variable: mole fraction of DMSO.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
            "min": 0.000596,
            "max": 0.003735,
            "mean": 0.002112,
            "std": 0.00077,
            "n": 120
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000596,
          "range_max": 0.003735
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
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
      "lit_num_id": "GLOBlit_5953",
      "block_number": "PROPblock_10",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity (Pa·s) of binary water + DMSO mixture. DOI 10.1016/j.tca.2011.08.013. Temperature range 303.15–318.15 K (4 temperatures), dilute DMSO region x(DMSO) = 0.0121–0.0583, 16 raw data points. Liquid phase at 101 kPa. Composition variable: mole fraction of DMSO.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
            "min": 0.000667,
            "max": 0.001224,
            "mean": 0.000907,
            "std": 0.000151,
            "n": 16
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000667,
          "range_max": 0.001224
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
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
      "lit_num_id": "GLOBlit_11517",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity (Pa·s) of binary water + DMSO mixture. DOI 10.1021/je9001027. Temperature range 298.15–318.15 K (5 temperatures), full mass-fraction range w(DMSO) = 0.0–1.0, 35 raw data points. Liquid phase at 101 kPa. Composition variable: mass fraction of DMSO.",
      "doi": "10.1021/je9001027",
      "lit_id": "2010-zam-tas-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 35,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
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
            "BLKvar_id": "BLKvar_2",
            "name": "Mass fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 7
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
          "meas_num_id": "GLOBmeas_205",
          "meas_ID": "captub_ufactor_16",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:16",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000535,
            "max": 0.003421,
            "mean": 0.001868,
            "std": 0.000795,
            "n": 35
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000535,
          "range_max": 0.003421
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
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "parent_n_datapoints": 35,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ]
}
### L1_query_3
{
  "answer": "Only one binary water + DMSO data block reporting surface tension (liquid–gas) was found in the ThermoML database:\n\n**DOI 10.1021/je7001013** — GLOBlit_10766, PROPblock_9\n- **System:** Binary water (GLOBcomp_1) + dimethyl sulfoxide (GLOBcomp_31)\n- **Property:** Surface tension, liquid–gas (GLOBprop_13), reported in N/m\n- **Measurement method:** Maximal bubble pressure (GLOBmeas_36)\n- **Temperature range:** 298.15–313.15 K (variable: GLOBvar_1)\n- **Composition range:** x(DMSO) = 0.0121–0.8945 (variable: mole fraction of DMSO, GLOBvar_2)\n- **Number of raw data points:** 112\n- **Phase:** Liquid\n- **Uncertainty:** 95% confidence level, propagation of evaluated standard uncertainties (typical ±0.0003–0.0005 N/m)\n\n**Chemistry note:** The water–DMSO binary system shows strongly non-ideal surface tension behavior. Pure water has a surface tension of approximately 0.072 N/m at 298 K, while pure DMSO is around 0.043 N/m. In mixtures, the surface tension decreases steeply with even small additions of DMSO, reflecting preferential adsorption of the more surface-active DMSO molecules at the liquid–gas interface. The broad composition coverage in this dataset (x(DMSO) from ~0.01 to ~0.89) across four temperatures provides good coverage for modeling surface excess and adsorption isotherms in this system.",
  "core_claims": [
    "Only one binary water + DMSO data block reporting surface tension (liquid–gas) was found in the ThermoML database, from DOI 10.1021/je7001013, measured by maximal bubble pressure over 298.15–313.15 K and x(DMSO) = 0.0121–0.8945, comprising 112 data points with typical uncertainties of ±0.0003–0.0005 N/m.",
    "The water–DMSO binary system exhibits strongly non-ideal surface tension behavior: surface tension decreases steeply with small additions of DMSO, reflecting preferential adsorption of the more surface-active DMSO at the liquid–gas interface.",
    "The broad composition and temperature coverage of this dataset is suitable for modeling surface excess and adsorption isotherms in the water–DMSO system."
  ],
  "status": "success",
  "summary": "In the ThermoML database, only one binary water + DMSO data block reporting surface tension (liquid–gas) was found, under DOI 10.1021/je7001013 (GLOBlit_10766, PROPblock_9). The system is binary water (GLOBcomp_1) + dimethyl sulfoxide (GLOBcomp_31), with surface tension (GLOBprop_13) reported in N/m, measured by maximal bubble pressure (GLOBmeas_36). The dataset spans 298.15–313.15 K and DMSO mole fractions from 0.0121 to 0.8945, comprising 112 raw data points in the liquid phase with typical uncertainties of ±0.0003–0.0005 N/m at 95% confidence. The system exhibits strongly non-ideal surface tension behavior: surface tension drops steeply with small DMSO additions due to preferential DMSO adsorption at the liquid–gas interface, and the broad composition and temperature coverage supports modeling of surface excess and adsorption isotherms.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension (liquid-gas) measurements for binary water + dimethyl sulfoxide mixtures. DOI 10.1021/je7001013. Method: maximal bubble pressure (GLOBmeas_36). Temperature range: 298.15–313.15 K. Composition range: x(DMSO) = 0.0121–0.8945. 112 data points. Uncertainty: 95% confidence level, typical ±0.0003–0.0005 N/m.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 112,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_5_1"
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
            "max": 328.15,
            "n_unique": 7
          },
          "range_min": 298.15,
          "range_max": 328.15
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
            "min": 0.0121,
            "max": 0.8945,
            "n_unique": 19
          },
          "range_min": 0.0121,
          "range_max": 0.8945
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_13",
          "prop_ID": "surface_tension_liquidgas_n_m",
          "name": "Surface tension liquid-gas, N/m",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_36",
          "meas_ID": "maximal_bubble_pressure",
          "method_standard": "Maximal bubble pressure",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0387,
            "max": 0.071,
            "mean": 0.050623,
            "std": 0.008081,
            "n": 112
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0387,
          "range_max": 0.071
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_5_1"
        }
      ],
      "parent_n_datapoints": 112,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ]
}
### L1_query_4
{
  "answer": "No strictly declared binary water + DMSO data blocks reporting electrical conductivity (GLOBprop_18) were found in the ThermoML database. However, three ternary parent blocks contain binary water+DMSO subsystems (where the third solute concentration is exactly zero), providing electrical conductivity data for the water+DMSO binary mixture:\n\n1. **DOI 10.1021/acs.jced.8b00326** — GLOBlit_7523, PROPblock_3, subsystem BLKsubsys_1\n   - Parent system: ternary (water + DMSO + cetylpyridinium chloride, GLOBcomp_2043)\n   - Binary subsystem data points: 16\n   - Temperature range: 293.15–308.15 K (variable)\n   - Composition variable: solvent mass fraction of DMSO (variable)\n\n2. **DOI 10.1021/je4004788** — GLOBlit_10194, PROPblock_7, subsystem BLKsubsys_1\n   - Parent system: ternary (water + DMSO + dodecyltrimethylammonium bromide, GLOBcomp_377)\n   - Binary subsystem data points: 6\n   - Temperature: 298.0 K (constrained)\n   - Composition variable: solvent mass fraction of DMSO (variable)\n\n3. **DOI 10.1021/je4004788** — GLOBlit_10194, PROPblock_10, subsystem BLKsubsys_1\n   - Parent system: ternary (water + DMSO + sodium dodecanoyl sarcosinate, GLOBcomp_1776)\n   - Binary subsystem data points: 6\n   - Temperature: 298.0 K (constrained)\n   - Composition variable: solvent mass fraction of DMSO (variable)\n\n**Total:** 3 subsystem blocks across 2 DOIs, totaling 28 binary water+DMSO electrical conductivity data points. All data come from ternary surfactant studies where the binary water+DMSO solvent mixture was characterized at zero surfactant concentration.\n\n**Chemistry note:** Electrical conductivity of the water–DMSO binary mixture is relevant in electrochemistry and surfactant science because DMSO addition to water significantly alters the dielectric constant and viscosity of the medium, which in turn affects ion mobility and conductance. These measurements were obtained as baseline solvent characterizations in studies of surfactant critical micelle concentrations in mixed water–DMSO solvents.",
  "core_claims": [
    "No strictly declared binary water + DMSO data blocks reporting electrical conductivity were found in the ThermoML database, but three ternary parent blocks (across 2 DOIs) contain binary water+DMSO subsystems at zero third-component concentration that provide electrical conductivity data, totaling 28 data points.",
    "The three relevant subsystem blocks come from DOI 10.1021/acs.jced.8b00326 (16 data points, 293.15–308.15 K, variable DMSO mass fraction) and DOI 10.1021/je4004788 (two blocks of 6 data points each, at 298.0 K, variable DMSO mass fraction).",
    "All data originate from ternary surfactant studies in which the binary water–DMSO solvent mixture was characterized at zero surfactant concentration as a baseline."
  ],
  "status": "partial",
  "summary": "No strictly declared binary water + DMSO data blocks reporting electrical conductivity (GLOBprop_18) were found in ThermoML. However, three ternary parent blocks contain binary water+DMSO subsystems (third solute concentration exactly zero) with electrical conductivity data: (1) DOI 10.1021/acs.jced.8b00326, GLOBlit_7523 PROPblock_3 BLKsubsys_1, ternary with cetylpyridinium chloride, 16 data points, 293.15–308.15 K, variable DMSO mass fraction; (2) DOI 10.1021/je4004788, GLOBlit_10194 PROPblock_7 BLKsubsys_1, ternary with dodecyltrimethylammonium bromide, 6 data points, 298.0 K, variable DMSO mass fraction; (3) same DOI, PROPblock_10 BLKsubsys_1, ternary with sodium dodecanoyl sarcosinate, 6 data points, 298.0 K, variable DMSO mass fraction. Total: 3 subsystem blocks across 2 DOIs, 28 binary water+DMSO electrical conductivity data points. All data originate from ternary surfactant studies where the binary water–DMSO solvent was characterized at zero surfactant concentration as a baseline for critical micelle concentration investigations.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_7523",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "ternary",
      "comp_num_ids": [
        "GLOBcomp_2043",
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_18"
      ],
      "description": "Electrical conductivity of water+DMSO binary subsystem (BLKsubsys_1) within ternary parent block (water + DMSO + cetylpyridinium chloride). 16 data points, temperature 293.15–308.15 K (variable), solvent mass fraction of DMSO (variable). DOI 10.1021/acs.jced.8b00326.",
      "doi": "10.1021/acs.jced.8b00326",
      "lit_id": "2018-sha-can-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_3",
      "n_datapoints": 176,
      "n_components": 3,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_2043",
          "name": "cetylpyridinium chloride",
          "formula": "C21H38ClN",
          "inchi_key": "YMKDRGPMQRFJGP-UHFFFAOYSA-M",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "solvents": [
        {
          "component_org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_31",
          "solvent_num_id": "GLOBsolvent_8",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N"
        },
        {
          "component_org_num": "DOIcomp_4",
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
            "max": 308.15,
            "n_unique": 4
          },
          "range_min": 293.15,
          "range_max": 308.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_7",
          "var_id": "solvent_mass_fraction_DOIcomp_3",
          "name": "Solvent: Mass fraction",
          "type": "eSolventComposition",
          "component_org_num": "DOIcomp_3",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Solvent: Mass fraction",
            "min": 0.05,
            "max": 0.2,
            "n_unique": 4
          },
          "range_min": 0.05,
          "range_max": 0.2
        },
        {
          "BLKvar_id": "BLKvar_3",
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_1",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_1",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_3",
            "name": "Molality, mol/kg",
            "min": 0.0,
            "max": 0.002,
            "n_unique": 11
          },
          "range_min": 0.0,
          "range_max": 0.002
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_18",
          "prop_ID": "electrical_conductivity_s_m",
          "name": "Electrical conductivity, S/m",
          "group": "TransportProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_14",
          "meas_ID": "alternating_current_cell_with_electrodes",
          "method_standard": "Alternating current cell with electrodes",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Electrical conductivity, S/m",
            "min": 0.0006,
            "max": 0.01783,
            "mean": 0.008434,
            "std": 0.004908,
            "n": 176
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0006,
          "range_max": 0.01783
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_2043",
          "name": "cetylpyridinium chloride",
          "formula": "C21H38ClN",
          "inchi_key": "YMKDRGPMQRFJGP-UHFFFAOYSA-M",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "parent_n_datapoints": 176,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10194",
      "block_number": "PROPblock_7",
      "BLKsubsys_id": null,
      "system_type": "ternary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_377",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_18"
      ],
      "description": "Electrical conductivity of water+DMSO binary subsystem (BLKsubsys_1) within ternary parent block (water + DMSO + dodecyltrimethylammonium bromide). 6 data points, temperature 298.0 K (constrained), solvent mass fraction of DMSO (variable). DOI 10.1021/je4004788.",
      "doi": "10.1021/je4004788",
      "lit_id": "2013-das-mon-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_3",
      "n_datapoints": 205,
      "n_components": 3,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_377",
          "name": "dodecyltrimethylammonium bromide",
          "formula": "C15H34BrN",
          "inchi_key": "XJWSAJYUBXQQDR-UHFFFAOYSA-M",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_5_1"
        }
      ],
      "solvents": [
        {
          "component_org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_31",
          "solvent_num_id": "GLOBsolvent_8",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N"
        },
        {
          "component_org_num": "DOIcomp_5",
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
          "value": 298.0,
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
          "var_num_id": "GLOBvar_7",
          "var_id": "solvent_mass_fraction_DOIcomp_4",
          "name": "Solvent: Mass fraction",
          "type": "eSolventComposition",
          "component_org_num": "DOIcomp_4",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Solvent: Mass fraction",
            "min": 0.0,
            "max": 0.4228,
            "n_unique": 6
          },
          "range_min": 0.0,
          "range_max": 0.4228
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_1",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_1",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Molality, mol/kg",
            "min": 0.0,
            "max": 0.078971,
            "n_unique": 200
          },
          "range_min": 0.0,
          "range_max": 0.078971
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_18",
          "prop_ID": "electrical_conductivity_s_m",
          "name": "Electrical conductivity, S/m",
          "group": "TransportProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_49",
          "meas_ID": "direct_current_cell_with_electrodes",
          "method_standard": "Direct current cell with electrodes",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Electrical conductivity, S/m",
            "min": 0.0,
            "max": 0.19865,
            "mean": 0.1185,
            "std": 0.054267,
            "n": 205
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0,
          "range_max": 0.19865
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
      "declared_system_type": "ternary",
      "declared_n_components": 3,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_377",
          "name": "dodecyltrimethylammonium bromide",
          "formula": "C15H34BrN",
          "inchi_key": "XJWSAJYUBXQQDR-UHFFFAOYSA-M",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_5_1"
        }
      ],
      "parent_n_datapoints": 205,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10194",
      "block_number": "PROPblock_10",
      "BLKsubsys_id": null,
      "system_type": "ternary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1776",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_18"
      ],
      "description": "Electrical conductivity of water+DMSO binary subsystem (BLKsubsys_1) within ternary parent block (water + DMSO + sodium dodecanoyl sarcosinate). 6 data points, temperature 298.0 K (constrained), solvent mass fraction of DMSO (variable). DOI 10.1021/je4004788.",
      "doi": "10.1021/je4004788",
      "lit_id": "2013-das-mon-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_3",
      "n_datapoints": 172,
      "n_components": 3,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1776",
          "name": "sodium [dodecanoyl(methyl)amino]acetate",
          "formula": "C15H28NNaO3",
          "inchi_key": "KSAVQLQVUXSOCR-UHFFFAOYSA-M",
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_5_1"
        }
      ],
      "solvents": [
        {
          "component_org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_31",
          "solvent_num_id": "GLOBsolvent_8",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N"
        },
        {
          "component_org_num": "DOIcomp_5",
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
          "value": 298.0,
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
          "var_num_id": "GLOBvar_7",
          "var_id": "solvent_mass_fraction_DOIcomp_4",
          "name": "Solvent: Mass fraction",
          "type": "eSolventComposition",
          "component_org_num": "DOIcomp_4",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Solvent: Mass fraction",
            "min": 0.0,
            "max": 0.4228,
            "n_unique": 6
          },
          "range_min": 0.0,
          "range_max": 0.4228
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_4",
          "var_id": "molality_mol_kg_DOIcomp_2",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Molality, mol/kg",
            "min": 0.0,
            "max": 0.042052,
            "n_unique": 167
          },
          "range_min": 0.0,
          "range_max": 0.042052
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_18",
          "prop_ID": "electrical_conductivity_s_m",
          "name": "Electrical conductivity, S/m",
          "group": "TransportProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_49",
          "meas_ID": "direct_current_cell_with_electrodes",
          "method_standard": "Direct current cell with electrodes",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Electrical conductivity, S/m",
            "min": 0.0,
            "max": 0.12462,
            "mean": 0.064786,
            "std": 0.034014,
            "n": 172
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0,
          "range_max": 0.12462
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
      "declared_system_type": "ternary",
      "declared_n_components": 3,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1776",
          "name": "sodium [dodecanoyl(methyl)amino]acetate",
          "formula": "C15H28NNaO3",
          "inchi_key": "KSAVQLQVUXSOCR-UHFFFAOYSA-M",
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_5_1"
        }
      ],
      "parent_n_datapoints": 172,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ]
}
### L1_query_5
{
  "answer": "No binary water (GLOBcomp_1) + dimethyl sulfoxide (GLOBcomp_31) data blocks reporting either excess molar enthalpy (GLOBprop_17) or excess molar volume (GLOBprop_28) were found in the ThermoML database. Searches were conducted with both \"declared\" and \"either\" (declared + subsystem) system scopes, and all returned zero results.\n\nThis means the ThermoML database does not contain excess molar enthalpy (HE) or excess molar volume (VE) data for the binary water–DMSO system. While the database does hold density, viscosity, surface tension, and electrical conductivity data for this binary mixture (as documented in prior queries), excess thermodynamic mixing properties for water + DMSO are not represented in the current ThermoML holdings.",
  "core_claims": [
    "The ThermoML database does not contain excess molar enthalpy or excess molar volume data for the binary water–dimethyl sulfoxide (DMSO) system.",
    "The ThermoML database does hold other property data (density, viscosity, surface tension, electrical conductivity) for the water–DMSO binary mixture, but excess thermodynamic mixing properties are not represented in the current holdings."
  ],
  "status": "no_results",
  "summary": "The ThermoML database does not contain excess molar enthalpy (HE) or excess molar volume (VE) data for the binary water–dimethyl sulfoxide (DMSO) system. Searches using both declared and subsystem scopes returned zero results. Although the database does hold other property data for this binary mixture (density, viscosity, surface tension, electrical conductivity), excess thermodynamic mixing properties for water + DMSO are not represented in the current ThermoML holdings.",
  "core_id_updates": [],
  "core_blocks_found": []
}

