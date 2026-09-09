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
- [L1] Find binary mixture data blocks for water+ethanol with viscosity, density, surface tension, excess molar volume, and ele → stored as L1_query_1
- [L1] Find binary mixture data blocks for water+methanol with viscosity, density, surface tension, excess molar volume, and el → stored as L1_query_2
- [L1] Find binary mixture data blocks for water+ethylene glycol with viscosity, density, surface tension, excess molar volume, → stored as L1_query_3

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
{
  "answer": "## Water + Ethanol Binary Mixture: Property Data Availability in ThermoML\n\n### Summary of Property Coverage\n\n| Property | Global ID | Blocks Found | DOIs | Temperature Range | Notes |\n|----------|-----------|:------------:|:----:|-------------------|-------|\n| **Mass Density** | GLOBprop_1 | 29 | 22 | 268.1–618.2 K | Best coverage; pressures from atmospheric to 40 MPa |\n| **Viscosity** | GLOBprop_4 | 14 | 14 | 268.1–618.2 K | Extensive coverage, all liquid-phase |\n| **Surface Tension** | GLOBprop_13 | 3 | 3 | 293–313 K | Limited T range; ethanol mass fractions 0–0.8 |\n| **Electrical Conductivity** | GLOBprop_18 | 1 | 1 | 298.0 K | Single block: PROPblock_11, DOI 10.1021/acs.jced.8b00181 (GLOBlit_7483), 6 data points |\n| **Excess Molar Volume** | GLOBprop_28 | 0 | — | — | **No data found** in ThermoML for this binary system |\n\n### Key Findings\n\n1. **Density and viscosity** have the richest data coverage for water+ethanol, with dozens of blocks spanning a wide temperature range (268–618 K) and multiple pressure conditions. These are the most thoroughly characterized transport/volumetric properties for this system in ThermoML.\n\n2. **Surface tension** data is available but limited to near-ambient temperatures (293–313 K) across three data blocks.\n\n3. **Electrical conductivity** has minimal coverage — only one block (PROPblock_11) from GLOBlit_7483 (DOI: 10.1021/acs.jced.8b00181) with 6 data points at a single temperature of 298.0 K. This is quite sparse for electrodeposition applications.\n\n4. **Excess molar volume** (GLOBprop_28) returned zero results for the water+ethanol binary. This property may be cataloged under a different identifier, or the data may simply not be present in ThermoML for this particular system. (Note: excess molar volume data may sometimes be derivable from density data if pure-component densities are available.)\n\n### Relevance to Electrodeposition\n\nFor electrodeposition-relevant solvent characterization, the electrical conductivity data is the most directly relevant but also the scarcest (single temperature, single source). Viscosity and density are well-covered and important for mass transport modeling. Surface tension data, while limited in temperature range, is useful for wetting and meniscus behavior. The absence of excess molar volume data is a gap, though it could potentially be calculated from the extensive density datasets if pure-component reference data is available.",
  "core_claims": [
    "In ThermoML for the water+ethanol binary system, mass density (29 blocks, 22 DOIs, 268–618 K) and viscosity (14 blocks, 14 DOIs, 268–618 K) have the richest data coverage, spanning wide temperature and pressure ranges.",
    "Surface tension data for water+ethanol is available but limited to near-ambient temperatures (293–313 K) across only three data blocks.",
    "Electrical conductivity data for water+ethanol is minimal, consisting of a single block (6 data points at 298 K from one source, DOI 10.1021/acs.jced.8b00181), making it sparse for electrodeposition applications.",
    "No excess molar volume data was found in ThermoML for the water+ethanol binary system, though it may potentially be derived from the available density data if pure-component reference densities are available.",
    "For electrodeposition-relevant solvent characterization, the most directly relevant property (electrical conductivity) has the scarcest coverage, while viscosity and density—important for mass transport modeling—are well covered."
  ],
  "status": "success",
  "summary": "For the water + ethanol binary mixture in ThermoML, mass density (29 blocks, 22 DOIs, 268–618 K) and viscosity (14 blocks, 14 DOIs, 268–618 K) have the richest coverage. Surface tension appears in 3 blocks (293–313 K). Electrical conductivity is very sparse, with only one block (PROPblock_11, GLOBlit_7483, DOI 10.1021/acs.jced.8b00181) providing 6 data points at 298.0 K. Excess molar volume returned no results for this system. For electrodeposition-relevant solvent characterization, electrical conductivity is most directly relevant but scarcest; viscosity and density are well covered for mass-transport modeling; surface tension data is limited to near-ambient temperatures; and excess molar volume data is absent but could potentially be derived from the extensive density datasets.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_1742",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+ethanol binary at 350.7–373.2 K, x(ethanol) 0.1–1.0, 84 points.",
      "doi": "10.1016/j.fluid.2015.07.012",
      "lit_id": "2016-ono-ame-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 84,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
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
            "min": 350.7,
            "max": 476.2,
            "n_unique": 3
          },
          "range_min": 350.7,
          "range_max": 476.2
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
            "min": 10000.0,
            "max": 40000.0,
            "n_unique": 4
          },
          "range_min": 10000.0,
          "range_max": 40000.0
        },
        {
          "BLKvar_id": "BLKvar_3",
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
            "BLKvar_id": "BLKvar_3",
            "name": "Mole fraction",
            "min": 0.1,
            "max": 1.0,
            "n_unique": 7
          },
          "range_min": 0.1,
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
          "meas_num_id": "GLOBmeas_4",
          "meas_ID": "capillary_tube_ostwald_ubbelohde_method",
          "method_standard": "Capillary tube (Ostwald; Ubbelohde) method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000107,
            "max": 0.000737,
            "mean": 0.000403,
            "std": 0.0002,
            "n": 84
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000107,
          "range_max": 0.000737
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
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 84,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2092",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+ethanol binary at 523.2–618.2 K, x(ethanol) 0.0–1.0, 72 points.",
      "doi": "10.1016/j.fluid.2017.09.005",
      "lit_id": "2017-ono-kyo-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 72,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
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
            "min": 523.2,
            "max": 618.2,
            "n_unique": 3
          },
          "range_min": 523.2,
          "range_max": 618.2
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
            "min": 20000.0,
            "max": 40000.0,
            "n_unique": 3
          },
          "range_min": 20000.0,
          "range_max": 40000.0
        },
        {
          "BLKvar_id": "BLKvar_3",
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
            "BLKvar_id": "BLKvar_3",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 8
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
          "meas_num_id": "GLOBmeas_4",
          "meas_ID": "capillary_tube_ostwald_ubbelohde_method",
          "method_standard": "Capillary tube (Ostwald; Ubbelohde) method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 3.1e-05,
            "max": 0.000134,
            "mean": 8.4e-05,
            "std": 2.8e-05,
            "n": 72
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 3.1e-05,
          "range_max": 0.000134
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
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 72,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2825",
      "block_number": "PROPblock_11",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+ethanol binary at 293.15–303.15 K, x(water) 0.0–1.0, 37 points.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
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
            "min": 0.000797,
            "max": 0.002705,
            "mean": 0.001607,
            "std": 0.000514,
            "n": 37
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000797,
          "range_max": 0.002705
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
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 37,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
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
      "description": "Viscosity of water+ethanol binary at 293.15–303.15 K, x(ethanol) 0.0201–0.929, 100 points.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 100,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_7178",
      "block_number": "PROPblock_11",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_1",
        "GLOBcomp_2"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+ethanol binary at 298.15–303.15 K, fixed molality, 2 points.",
      "doi": "10.1021/acs.jced.7b00299",
      "lit_id": "2017-sha-asa-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 2,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
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
        },
        {
          "BLKconstr_id": "BLKconstr_2",
          "constr_num_id": "GLOBconstr_8",
          "constr_id": "molality_mol_kg_DOIcomp_2",
          "name": "Molality, mol/kg",
          "type": "eComponentComposition",
          "value": 16.0,
          "digits": 4,
          "component_org_num": "DOIcomp_2",
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
            "max": 303.15,
            "n_unique": 2
          },
          "range_min": 298.15,
          "range_max": 303.15
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
            "min": 0.001992,
            "max": 0.002367,
            "mean": 0.00218,
            "std": 0.000265,
            "n": 2
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.001992,
          "range_max": 0.002367
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 2,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_7448",
      "block_number": "PROPblock_47",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+ethanol binary at fixed T, w(water) 0.206–0.508, 6 points.",
      "doi": "10.1021/acs.jced.8b00086",
      "lit_id": "2018-gon-pal-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 6,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_6_1"
        },
        {
          "org_num": "DOIcomp_7",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_7_1"
        }
      ],
      "solvents": [],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_2",
          "constr_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "value": 298.2,
          "digits": 4,
          "component_org_num": null,
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
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_7",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_7",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Mass fraction",
            "min": 0.206,
            "max": 0.508,
            "n_unique": 6
          },
          "range_min": 0.206,
          "range_max": 0.508
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
          "meas_num_id": "GLOBmeas_8",
          "meas_ID": "falling_or_rolling_sphere_viscometry",
          "method_standard": "Falling or rolling sphere viscometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.001676,
            "max": 0.002235,
            "mean": 0.001903,
            "std": 0.000241,
            "n": 6
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.001676,
          "range_max": 0.002235
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
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_6_1"
        },
        {
          "org_num": "DOIcomp_7",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_7_1"
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
      "lit_num_id": "GLOBlit_7676",
      "block_number": "PROPblock_18",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+ethanol binary (partial result from truncated search output).",
      "doi": "10.1021/acs.jced.8b00939",
      "lit_id": "2019-kos-gon-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 9,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_7",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_7_1"
        },
        {
          "org_num": "DOIcomp_8",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_8_1"
        }
      ],
      "solvents": [],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_2",
          "constr_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "value": 298.2,
          "digits": 4,
          "component_org_num": null,
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
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_8",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_8",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Mass fraction",
            "min": 0.061,
            "max": 0.62,
            "n_unique": 9
          },
          "range_min": 0.061,
          "range_max": 0.62
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
          "meas_num_id": "GLOBmeas_8",
          "meas_ID": "falling_or_rolling_sphere_viscometry",
          "method_standard": "Falling or rolling sphere viscometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.00131,
            "max": 0.00234,
            "mean": 0.001869,
            "std": 0.000364,
            "n": 9
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.00131,
          "range_max": 0.00234
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
          "org_num": "DOIcomp_7",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_7_1"
        },
        {
          "org_num": "DOIcomp_8",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_8_1"
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
      "description": "Mass density of water+ethanol binary at 298.15 K, 100 kPa, x(ethanol) 0.003–0.80, 810 points.",
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
      "parent_n_datapoints": 810,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
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
      "description": "Mass density of water+ethanol binary at 292.95–448.15 K, 2450–39910 kPa, x(ethanol) 0.016–0.073, 140 points.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 140,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_1742",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+ethanol binary at 350.7–373.2 K, 10000–40000 kPa, x(ethanol) 0.1–1.0, 84 points.",
      "doi": "10.1016/j.fluid.2015.07.012",
      "lit_id": "2016-ono-ame-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 84,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
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
            "min": 350.7,
            "max": 476.2,
            "n_unique": 3
          },
          "range_min": 350.7,
          "range_max": 476.2
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
            "min": 10000.0,
            "max": 40000.0,
            "n_unique": 4
          },
          "range_min": 10000.0,
          "range_max": 40000.0
        },
        {
          "BLKvar_id": "BLKvar_3",
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
            "BLKvar_id": "BLKvar_3",
            "name": "Mole fraction",
            "min": 0.1,
            "max": 1.0,
            "n_unique": 7
          },
          "range_min": 0.1,
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
            "min": 582.85,
            "max": 945.15,
            "mean": 793.264881,
            "std": 87.934866,
            "n": 84
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 582.85,
          "range_max": 945.15
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
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 84,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2092",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+ethanol binary at 523.2–618.2 K, 20000–40000 kPa, x(ethanol) 0–1.0, 72 points.",
      "doi": "10.1016/j.fluid.2017.09.005",
      "lit_id": "2017-ono-kyo-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 72,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
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
            "min": 523.2,
            "max": 618.2,
            "n_unique": 3
          },
          "range_min": 523.2,
          "range_max": 618.2
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
            "min": 20000.0,
            "max": 40000.0,
            "n_unique": 3
          },
          "range_min": 20000.0,
          "range_max": 40000.0
        },
        {
          "BLKvar_id": "BLKvar_3",
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
            "BLKvar_id": "BLKvar_3",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 8
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
            "min": 250.4,
            "max": 834.3,
            "mean": 569.888889,
            "std": 137.332364,
            "n": 72
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 250.4,
          "range_max": 834.3
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
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 72,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2432",
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
      "description": "Mass density of water+ethanol binary at 298.15–298.18 K, 410–29930 kPa, b(ethanol) 0.096–0.943, 565 points.",
      "doi": "10.1016/j.jct.2004.07.019",
      "lit_id": "2004-hyn-hne-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 565,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
            "min": 298.15,
            "max": 573.15,
            "n_unique": 17
          },
          "range_min": 298.15,
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
            "max": 30300.0,
            "n_unique": 31
          },
          "range_min": 390.0,
          "range_max": 30300.0
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
            "min": 0.08808,
            "max": 1.04067,
            "n_unique": 156
          },
          "range_min": 0.08808,
          "range_max": 1.04067
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
            "min": -19.634,
            "max": -0.7809,
            "mean": -5.468488,
            "std": 3.966781,
            "n": 565
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -19.634,
          "range_max": -0.7809
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 565,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2732",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+ethanol binary at 524.15–548.15 K, 4750–27310 kPa, x(ethanol) 0.5–0.8, 278 points.",
      "doi": "10.1016/j.jct.2006.08.002",
      "lit_id": "2007-baz-abd-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 278,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
            "phase": "Fluid (supercritical or subcritical phases)",
            "phase_num_id": "GLOBphase_10",
            "phase_id": "fluid_supercritical_or_subcritical_phases"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Temperature, K",
            "min": 524.15,
            "max": 673.15,
            "n_unique": 28
          },
          "range_min": 524.15,
          "range_max": 673.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_3",
          "var_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "component_org_num": null,
          "phase": {
            "phase": "Fluid (supercritical or subcritical phases)",
            "phase_num_id": "GLOBphase_10",
            "phase_id": "fluid_supercritical_or_subcritical_phases"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Pressure, kPa",
            "min": 4750.0,
            "max": 50760.0,
            "n_unique": 251
          },
          "range_min": 4750.0,
          "range_max": 50760.0
        },
        {
          "BLKvar_id": "BLKvar_3",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_1",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_1",
          "phase": {
            "phase": "Fluid (supercritical or subcritical phases)",
            "phase_num_id": "GLOBphase_10",
            "phase_id": "fluid_supercritical_or_subcritical_phases"
          },
          "range": {
            "BLKvar_id": "BLKvar_3",
            "name": "Mole fraction",
            "min": 0.2,
            "max": 0.8,
            "n_unique": 3
          },
          "range_min": 0.2,
          "range_max": 0.8
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
            "min": 52.89,
            "max": 617.36,
            "mean": 303.042374,
            "std": 148.03136,
            "n": 278
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 52.89,
          "range_max": 617.36
        }
      ],
      "phases": [
        {
          "owner_id": "BLKprop_1",
          "role": "property_phase",
          "phase": "Fluid (supercritical or subcritical phases)",
          "phase_num_id": "GLOBphase_10",
          "phase_id": "fluid_supercritical_or_subcritical_phases"
        },
        {
          "owner_id": "BLKvar_1",
          "role": "phase",
          "phase": "Fluid (supercritical or subcritical phases)",
          "phase_num_id": "GLOBphase_10",
          "phase_id": "fluid_supercritical_or_subcritical_phases"
        },
        {
          "owner_id": "BLKvar_2",
          "role": "phase",
          "phase": "Fluid (supercritical or subcritical phases)",
          "phase_num_id": "GLOBphase_10",
          "phase_id": "fluid_supercritical_or_subcritical_phases"
        },
        {
          "owner_id": "BLKvar_3",
          "role": "phase",
          "phase": "Fluid (supercritical or subcritical phases)",
          "phase_num_id": "GLOBphase_10",
          "phase_id": "fluid_supercritical_or_subcritical_phases"
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 278,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_6628",
      "block_number": "PROPblock_8",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of water+ethanol binary at 293.15 K, w(ethanol) = 0.1 fixed, 2 points.",
      "doi": "10.1021/acs.jced.5b00485",
      "lit_id": "2016-lud-kus-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 2,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_4_1"
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
          "constr_num_id": "GLOBconstr_5",
          "constr_id": "mass_fraction_DOIcomp_4",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "value": 0.1,
          "digits": 2,
          "component_org_num": "DOIcomp_4",
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
          "value": 293.15,
          "digits": 5,
          "component_org_num": null,
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          }
        }
      ],
      "variables": [],
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
            "min": 0.0425,
            "max": 0.0443,
            "mean": 0.0434,
            "std": 0.001273,
            "n": 2
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0425,
          "range_max": 0.0443
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_4_1"
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
      "parent_n_datapoints": 2,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_7448",
      "block_number": "PROPblock_48",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of water+ethanol binary at 298.2 K, w(water) 0.206–0.508, 6 points.",
      "doi": "10.1021/acs.jced.8b00086",
      "lit_id": "2018-gon-pal-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 6,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_6_1"
        },
        {
          "org_num": "DOIcomp_7",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_7_1"
        }
      ],
      "solvents": [],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_2",
          "constr_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "value": 298.2,
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
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_7",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_7",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Mass fraction",
            "min": 0.206,
            "max": 0.508,
            "n_unique": 6
          },
          "range_min": 0.206,
          "range_max": 0.508
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
          "meas_num_id": "GLOBmeas_19",
          "meas_ID": "ring_tensiometer",
          "method_standard": "Ring tensiometer",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0248,
            "max": 0.0282,
            "mean": 0.02595,
            "std": 0.001282,
            "n": 6
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0248,
          "range_max": 0.0282
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
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "binary",
      "declared_n_components": 2,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_6",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_6_1"
        },
        {
          "org_num": "DOIcomp_7",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_7_1"
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
      "lit_num_id": "GLOBlit_7794",
      "block_number": "PROPblock_16",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of water+ethanol binary at 298.0–313.0 K, w(ethanol) 0.0–0.2, 10 points. Richest surface tension dataset.",
      "doi": "10.1021/acs.jced.9b00026",
      "lit_id": "2019-raz-hal-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 10,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_9",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_9_1"
        },
        {
          "org_num": "DOIcomp_8",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_8_1"
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
            "min": 298.0,
            "max": 313.0,
            "n_unique": 2
          },
          "range_min": 298.0,
          "range_max": 313.0
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_9",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_9",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Mass fraction",
            "min": 0.0,
            "max": 0.2,
            "n_unique": 5
          },
          "range_min": 0.0,
          "range_max": 0.2
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
          "meas_num_id": "GLOBmeas_19",
          "meas_ID": "ring_tensiometer",
          "method_standard": "Ring tensiometer",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.03671,
            "max": 0.07204,
            "mean": 0.050074,
            "std": 0.012533,
            "n": 10
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.03671,
          "range_max": 0.07204
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
          "org_num": "DOIcomp_9",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_9_1"
        },
        {
          "org_num": "DOIcomp_8",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_8_1"
        }
      ],
      "parent_n_datapoints": 10,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_7483",
      "block_number": "PROPblock_11",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_18"
      ],
      "description": "Electrical conductivity of water+ethanol binary at 298.0 K, 100.0 kPa, ethanol molality 0.9–9.51 mol/kg, 6 data points. Only conductivity block found for this system.",
      "doi": "10.1021/acs.jced.8b00181",
      "lit_id": "2018-jak-paw-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 6,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
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
          "component_org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_1",
          "solvent_num_id": "GLOBsolvent_1",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N"
        }
      ],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
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
        },
        {
          "BLKconstr_id": "BLKconstr_3",
          "constr_num_id": "GLOBconstr_4",
          "constr_id": "frequency_mhz",
          "name": "Frequency, MHz",
          "type": "eMiscellaneous",
          "value": 0.001,
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
            "BLKvar_id": "BLKvar_1",
            "name": "Molality, mol/kg",
            "min": 0.9,
            "max": 9.51,
            "n_unique": 6
          },
          "range_min": 0.9,
          "range_max": 9.51
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
            "min": 0.000248,
            "max": 0.000311,
            "mean": 0.000268,
            "std": 2.5e-05,
            "n": 6
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000248,
          "range_max": 0.000311
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
        },
        {
          "owner_id": "BLKconstr_3",
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
      "parent_n_datapoints": 6,
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
  "answer": "## Water + Methanol Binary Mixture: Property Data Availability in ThermoML\n\n### Summary of Property Coverage\n\n| Property | Global ID | Blocks Found | DOIs | Temperature Range | Notes |\n|----------|-----------|:------------:|:----:|-------------------|-------|\n| **Mass Density** | GLOBprop_1 | 18 | 14 | ~273–619 K | Best coverage; pressures from atmospheric to 60 MPa; liquid and supercritical phases |\n| **Viscosity** | GLOBprop_4 | 6 | 6 | 273.15–618.2 K | Good coverage from near-freezing to supercritical; various composition scales |\n| **Excess Molar Volume** | GLOBprop_28 | 2 | 2 | 298.15–623.15 K | Limited but present; one near-ambient block and one supercritical block |\n| **Surface Tension** | GLOBprop_13 | 0 | — | — | **No data found** in ThermoML for this binary system |\n| **Electrical Conductivity** | GLOBprop_18 | 0 | — | — | **No data found** in ThermoML for this binary system |\n\n### Detailed Block Listings\n\n#### Viscosity (GLOBprop_4) — 6 blocks, ~232 data points\n\n| # | DOI | Lit ID | Block | Points | T (K) | Composition | P (kPa) | Method |\n|---|-----|--------|-------|--------|--------|-------------|----------|--------|\n| 1 | 10.1016/j.fluid.2015.07.012 | GLOBlit_1742 | PROPblock_2 | 84 | 350.7–373.2 | x(MeOH) 0.1–1.0 | 10000–40000 | Capillary tube (Ostwald/Ubbelohde) |\n| 2 | 10.1016/j.fluid.2017.09.005 | GLOBlit_2092 | PROPblock_2 | 72 | 523.2–618.2 | x(MeOH) 0.0–1.0 | 20000–40000 | Pressure drop in straight capillary |\n| 3 | 10.1016/j.jct.2007.05.004 | GLOBlit_2825 | PROPblock_9 | 39 | 293.15–303.15 | x(water) 0.0–1.0 | 101.0 (fixed) | Capillary tube |\n| 4 | 10.1016/j.jct.2019.05.013 | GLOBlit_5533 | PROPblock_3 | 12 | 273.15–293.15 | w(MeOH) 0.0–0.4999 | 100.0 (fixed) | Falling/rolling sphere |\n| 5 | 10.1021/je0600810 | GLOBlit_8869 | PROPblock_3 | 9 | 298.15–318.15 | φ_v(MeOH) 0.01–0.3 | 101.0 (fixed) | Capillary tube |\n| 6 | 10.1021/je2003622 | GLOBlit_9571 | PROPblock_1 | 16 | 298.15–323.15 | w(MeOH) 0.0806–0.3446 | 101.0 (fixed) | Capillary tube |\n\n#### Mass Density (GLOBprop_1) — 18 blocks, 14 DOIs\n\nRepresentative blocks include:\n- GLOBlit_2432 / PROPblock_1: 596 points at ~298 K, 400–29990 kPa, b(MeOH) 0.077–0.989 (vibrating tube)\n- GLOBlit_1742 / PROPblock_1: 80 points, 350.7–373.2 K, 10000–40000 kPa, x(MeOH) 0.1–1.0 (vibrating tube)\n- GLOBlit_2092 / PROPblock_1: 72 points, 523.2–618.2 K, 20000–40000 kPa, x(MeOH) 0.0–1.0 (vibrating tube)\n- GLOBlit_385 / PROPblock_1: 45 points, 572.9–588.9 K, 10077–20019 kPa, x(MeOH) 0.007–0.880 (supercritical/subcritical fluid)\n- GLOBlit_895 / PROPblock_1: 34 points at fixed T, 20000–35000 kPa, x(MeOH) 0.04–0.95\n\n#### Excess Molar Volume (GLOBprop_28) — 2 blocks\n\n| # | DOI | Lit ID | Block | Points | T (K) | P (kPa) | x(MeOH) |\n|---|-----|--------|-------|--------|--------|----------|----------|\n| 1 | 10.1016/j.jct.2004.03.011 | GLOBlit_2395 | PROPblock_1 | 206 | 298.15–348.15 | 100–60000 | 0.25–0.75 |\n| 2 | 10.1016/j.fluid.2010.10.005 | GLOBlit_895 | PROPblock_2 | 34 | 623.15 (fixed) | 20000–35000 | 0.04–0.95 |\n\n### Key Findings\n\n1. **Mass density** has the richest coverage for water+methanol (18 blocks, 14 DOIs), spanning near-ambient to supercritical conditions with extensive pressure and composition variation. This is the most thoroughly characterized property for this system in ThermoML.\n\n2. **Viscosity** has good coverage (6 blocks, 6 DOIs) spanning 273–618 K, including both atmospheric and high-pressure measurements. The near-ambient data (GLOBlit_2825, GLOBlit_5533, GLOBlit_8869, GLOBlit_9571) covers 273–323 K at atmospheric pressure, while high-pressure/high-temperature data extends to supercritical conditions.\n\n3. **Excess molar volume** data is present but limited to 2 blocks (240 total points). The GLOBlit_2395 block provides the most useful near-ambient data (298–348 K, 100–60000 kPa), while GLOBlit_895 covers supercritical conditions at 623 K. This is notably better than the water+ethanol system, where no excess molar volume data was found.\n\n4. **Surface tension** — no data found in ThermoML for the water+methanol binary system.\n\n5. **Electrical conductivity** — no data found in ThermoML for the water+methanol binary system.\n\n### Comparison with Water+Ethanol\n\nCompared to the water+ethanol binary, the water+methanol system has fewer viscosity blocks (6 vs. 14) and fewer density blocks (18 vs. 29), but it does have excess molar volume data (2 blocks vs. 0 for ethanol). Neither system has surface tension data in abundance (ethanol has 3 blocks; methanol has 0). Electrical conductivity is absent for methanol (ethanol had 1 sparse block). For electrodeposition-relevant characterization, the water+methanol system is missing the two most directly relevant properties (surface tension and electrical conductivity).",
  "core_claims": [
    "In ThermoML, the water+methanol binary system has substantial mass density coverage (18 blocks, 14 DOIs, ~273–619 K, atmospheric to 60 MPa) and good viscosity coverage (6 blocks, 6 DOIs, 273–618 K including atmospheric and high-pressure conditions), but only limited excess molar volume data (2 blocks, 240 total points spanning 298–623 K).",
    "No surface tension or electrical conductivity data were found in ThermoML for the water+methanol binary system.",
    "Compared to the water+ethanol binary system, water+methanol has fewer viscosity blocks (6 vs. 14) and fewer density blocks (18 vs. 29), but uniquely possesses excess molar volume data (2 blocks vs. 0 for ethanol); however, it lacks surface tension data entirely (ethanol has 3 blocks) and electrical conductivity data (ethanol has 1 sparse block).",
    "For electrodeposition-relevant characterization, the water+methanol system is missing the two most directly relevant properties: surface tension and electrical conductivity."
  ],
  "status": "success",
  "summary": "For the water + methanol binary mixture in ThermoML, mass density (GLOBprop_1) has the richest coverage with 18 blocks across 14 DOIs spanning ~273–619 K and pressures from atmospheric to 60 MPa. Viscosity (GLOBprop_4) appears in 6 blocks from 6 DOIs covering 273–618 K at both atmospheric and high pressures. Excess molar volume (GLOBprop_28) is present but limited to 2 blocks (240 total points) covering 298–623 K. No data were found for surface tension (GLOBprop_13) or electrical conductivity (GLOBprop_18) for this binary system. Compared to water + ethanol, the water + methanol system has fewer viscosity and density blocks but uniquely possesses excess molar volume data; it lacks surface tension data entirely (ethanol had 3 blocks) and has no electrical conductivity data (ethanol had 1 sparse block).",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_1742",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+methanol binary, 350.7–373.2 K, 10000–40000 kPa, x(MeOH) 0.1–1.0, 84 points, capillary tube method.",
      "doi": "10.1016/j.fluid.2015.07.012",
      "lit_id": "2016-ono-ame-0",
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
            "min": 350.7,
            "max": 476.2,
            "n_unique": 3
          },
          "range_min": 350.7,
          "range_max": 476.2
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
            "min": 10000.0,
            "max": 40000.0,
            "n_unique": 4
          },
          "range_min": 10000.0,
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
            "min": 0.1,
            "max": 1.0,
            "n_unique": 7
          },
          "range_min": 0.1,
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
          "meas_num_id": "GLOBmeas_4",
          "meas_ID": "capillary_tube_ostwald_ubbelohde_method",
          "method_standard": "Capillary tube (Ostwald; Ubbelohde) method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 8.8e-05,
            "max": 0.000565,
            "mean": 0.000312,
            "std": 0.000148,
            "n": 84
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 8.8e-05,
          "range_max": 0.000565
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
      "parent_n_datapoints": 84,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2092",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+methanol binary, 523.2–618.2 K, 20000–40000 kPa, x(MeOH) 0.0–1.0, 72 points, pressure drop in straight capillary.",
      "doi": "10.1016/j.fluid.2017.09.005",
      "lit_id": "2017-ono-kyo-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 72,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
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
            "min": 523.2,
            "max": 618.2,
            "n_unique": 3
          },
          "range_min": 523.2,
          "range_max": 618.2
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
            "min": 20000.0,
            "max": 40000.0,
            "n_unique": 3
          },
          "range_min": 20000.0,
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
            "min": 0.0,
            "max": 1.0,
            "n_unique": 8
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
          "meas_num_id": "GLOBmeas_2135",
          "meas_ID": "pressure_drop_in_straight_capillary",
          "method_standard": null,
          "method_custom": "Pressure drop in straight capillary",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 2.5e-05,
            "max": 0.000121,
            "mean": 7.8e-05,
            "std": 2.6e-05,
            "n": 72
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 2.5e-05,
          "range_max": 0.000121
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
      "parent_n_datapoints": 72,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2825",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+methanol binary, 293.15–303.15 K, 101.0 kPa (constrained), x(water) 0.0–1.0, 39 points, capillary tube.",
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
            "min": 0.000508,
            "max": 0.001793,
            "mean": 0.001082,
            "std": 0.000366,
            "n": 39
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000508,
          "range_max": 0.001793
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
      "parent_n_datapoints": 39,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_5533",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+methanol binary, 273.15–293.15 K, 100.0 kPa (constrained), w(MeOH) 0.0–0.4999, 12 points, falling/rolling sphere.",
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
          "prop_num_id": "GLOBprop_4",
          "prop_ID": "viscosity_pa_s",
          "name": "Viscosity, Pa*s",
          "group": "TransportProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_8",
          "meas_ID": "falling_or_rolling_sphere_viscometry",
          "method_standard": "Falling or rolling sphere viscometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000998,
            "max": 0.003636,
            "mean": 0.002284,
            "std": 0.000953,
            "n": 12
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000998,
          "range_max": 0.003636
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
      "parent_n_datapoints": 12,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8869",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+methanol binary, 298.15–318.15 K, 101.0 kPa (constrained), φ_v(MeOH) 0.01–0.3, 9 points, capillary tube.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
            "min": 0.000702,
            "max": 0.001471,
            "mean": 0.001033,
            "std": 0.000248,
            "n": 9
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000702,
          "range_max": 0.001471
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 9,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_9571",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+methanol binary, 298.15–323.15 K, 101.0 kPa (constrained), w(MeOH) 0.0806–0.3446, 16 points, capillary tube.",
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
          "prop_num_id": "GLOBprop_4",
          "prop_ID": "viscosity_pa_s",
          "name": "Viscosity, Pa*s",
          "group": "TransportProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_271",
          "meas_ID": "captub_ufactor_6",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:6",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000638,
            "max": 0.001471,
            "mean": 0.000993,
            "std": 0.000261,
            "n": 16
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000638,
          "range_max": 0.001471
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
      "parent_n_datapoints": 16,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_385",
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
      "description": "Mass density of water+methanol binary, 572.91–588.85 K, 10077–20019 kPa, x(MeOH) 0.007–0.880, 45 points, supercritical/subcritical fluid.",
      "doi": "10.1016/j.fluid.2006.05.007",
      "lit_id": "2006-bul-tre-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 45,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
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
            "phase": "Fluid (supercritical or subcritical phases)",
            "phase_num_id": "GLOBphase_10",
            "phase_id": "fluid_supercritical_or_subcritical_phases"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Temperature, K",
            "min": 572.91,
            "max": 588.85,
            "n_unique": 38
          },
          "range_min": 572.91,
          "range_max": 588.85
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_3",
          "var_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "component_org_num": null,
          "phase": {
            "phase": "Fluid (supercritical or subcritical phases)",
            "phase_num_id": "GLOBphase_10",
            "phase_id": "fluid_supercritical_or_subcritical_phases"
          },
          "range": {
            "BLKvar_id": "BLKvar_2",
            "name": "Pressure, kPa",
            "min": 10068.0,
            "max": 20019.0,
            "n_unique": 36
          },
          "range_min": 10068.0,
          "range_max": 20019.0
        },
        {
          "BLKvar_id": "BLKvar_3",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_2",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_2",
          "phase": {
            "phase": "Fluid (supercritical or subcritical phases)",
            "phase_num_id": "GLOBphase_10",
            "phase_id": "fluid_supercritical_or_subcritical_phases"
          },
          "range": {
            "BLKvar_id": "BLKvar_3",
            "name": "Mole fraction",
            "min": 0.007,
            "max": 0.8802,
            "n_unique": 13
          },
          "range_min": 0.007,
          "range_max": 0.8802
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
            "min": 77.4,
            "max": 712.1,
            "mean": 366.728889,
            "std": 247.822048,
            "n": 45
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 77.4,
          "range_max": 712.1
        }
      ],
      "phases": [
        {
          "owner_id": "BLKprop_1",
          "role": "property_phase",
          "phase": "Fluid (supercritical or subcritical phases)",
          "phase_num_id": "GLOBphase_10",
          "phase_id": "fluid_supercritical_or_subcritical_phases"
        },
        {
          "owner_id": "BLKvar_1",
          "role": "phase",
          "phase": "Fluid (supercritical or subcritical phases)",
          "phase_num_id": "GLOBphase_10",
          "phase_id": "fluid_supercritical_or_subcritical_phases"
        },
        {
          "owner_id": "BLKvar_2",
          "role": "phase",
          "phase": "Fluid (supercritical or subcritical phases)",
          "phase_num_id": "GLOBphase_10",
          "phase_id": "fluid_supercritical_or_subcritical_phases"
        },
        {
          "owner_id": "BLKvar_3",
          "role": "phase",
          "phase": "Fluid (supercritical or subcritical phases)",
          "phase_num_id": "GLOBphase_10",
          "phase_id": "fluid_supercritical_or_subcritical_phases"
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
      "parent_n_datapoints": 45,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_462",
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
      "description": "Mass density of water+methanol binary, 556.82–561.80 K, constrained pressure, 8 points, liquid+gas phase.",
      "doi": "10.1016/j.fluid.2006.12.005",
      "lit_id": "2007-pol-abd-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 8,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
          "constr_id": "mole_fraction_DOIcomp_1",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "value": 0.5004,
          "digits": 4,
          "component_org_num": "DOIcomp_1",
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
            "min": 556.816,
            "max": 561.797,
            "n_unique": 8
          },
          "range_min": 556.816,
          "range_max": 561.797
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
          "meas_num_id": "GLOBmeas_1494",
          "meas_ID": "derived_from_heat_capacity_measurements",
          "method_standard": null,
          "method_custom": "derived from heat capacity measurements",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 214.42,
            "max": 394.8,
            "mean": 282.1925,
            "std": 59.504036,
            "n": 8
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 214.42,
          "range_max": 394.8
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 8,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_462",
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
      "description": "Mass density of water+methanol binary, 561.94–561.97 K, constrained pressure, 2 points, gas+liquid phase.",
      "doi": "10.1016/j.fluid.2006.12.005",
      "lit_id": "2007-pol-abd-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 2,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
          "constr_id": "mole_fraction_DOIcomp_1",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "value": 0.5014,
          "digits": 4,
          "component_org_num": "DOIcomp_1",
          "phase": {
            "phase": "Gas",
            "phase_num_id": "GLOBphase_3",
            "phase_id": "gas"
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
            "phase": "Gas",
            "phase_num_id": "GLOBphase_3",
            "phase_id": "gas"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Temperature, K",
            "min": 561.944,
            "max": 561.966,
            "n_unique": 2
          },
          "range_min": 561.944,
          "range_max": 561.966
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
          "meas_num_id": "GLOBmeas_1494",
          "meas_ID": "derived_from_heat_capacity_measurements",
          "method_standard": null,
          "method_custom": "derived from heat capacity measurements",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 244.77,
            "max": 252.54,
            "mean": 248.655,
            "std": 5.49422,
            "n": 2
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 244.77,
          "range_max": 252.54
        }
      ],
      "phases": [
        {
          "owner_id": "BLKprop_1",
          "role": "property_phase",
          "phase": "Gas",
          "phase_num_id": "GLOBphase_3",
          "phase_id": "gas"
        },
        {
          "owner_id": "BLKvar_1",
          "role": "phase",
          "phase": "Gas",
          "phase_num_id": "GLOBphase_3",
          "phase_id": "gas"
        },
        {
          "owner_id": "BLKconstr_1",
          "role": "phase",
          "phase": "Gas",
          "phase_num_id": "GLOBphase_3",
          "phase_id": "gas"
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 2,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_895",
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
      "description": "Mass density of water+methanol binary, constrained T, 20000–35000 kPa, x(MeOH) 0.04–0.95, 34 points.",
      "doi": "10.1016/j.fluid.2010.10.005",
      "lit_id": "2011-ono-kob-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 34,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
          "constr_num_id": "GLOBconstr_2",
          "constr_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "value": 623.15,
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
            "min": 20000.0,
            "max": 35000.0,
            "n_unique": 4
          },
          "range_min": 20000.0,
          "range_max": 35000.0
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
            "min": 0.04,
            "max": 0.95,
            "n_unique": 27
          },
          "range_min": 0.04,
          "range_max": 0.95
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
            "min": 192.93,
            "max": 603.89,
            "mean": 404.172941,
            "std": 136.880924,
            "n": 34
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 192.93,
          "range_max": 603.89
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 34,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_1742",
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
      "description": "Mass density of water+methanol binary, 350.7–373.2 K, 10000–40000 kPa, x(MeOH) 0.1–1.0, 80 points, vibrating tube.",
      "doi": "10.1016/j.fluid.2015.07.012",
      "lit_id": "2016-ono-ame-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 80,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
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
            "min": 350.7,
            "max": 476.2,
            "n_unique": 3
          },
          "range_min": 350.7,
          "range_max": 476.2
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
            "min": 10000.0,
            "max": 40000.0,
            "n_unique": 4
          },
          "range_min": 10000.0,
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
            "min": 0.1,
            "max": 1.0,
            "n_unique": 7
          },
          "range_min": 0.1,
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
            "min": 576.84,
            "max": 958.39,
            "mean": 814.059375,
            "std": 92.603502,
            "n": 80
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 576.84,
          "range_max": 958.39
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
      "parent_n_datapoints": 80,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2092",
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
      "description": "Mass density of water+methanol binary, 523.2–618.2 K, 20000–40000 kPa, x(MeOH) 0.0–1.0, 72 points, vibrating tube.",
      "doi": "10.1016/j.fluid.2017.09.005",
      "lit_id": "2017-ono-kyo-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 72,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
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
            "min": 523.2,
            "max": 618.2,
            "n_unique": 3
          },
          "range_min": 523.2,
          "range_max": 618.2
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
            "min": 20000.0,
            "max": 40000.0,
            "n_unique": 3
          },
          "range_min": 20000.0,
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
            "min": 0.0,
            "max": 1.0,
            "n_unique": 8
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
            "min": 198.2,
            "max": 834.3,
            "mean": 569.5125,
            "std": 159.701895,
            "n": 72
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 198.2,
          "range_max": 834.3
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
      "parent_n_datapoints": 72,
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
      "description": "Mass density of water+methanol binary, ~298 K, 400–29990 kPa, b(MeOH) 0.077–0.989, 596 points, vibrating tube.",
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
          "SMILES": null,
          "sample_num": "DOIcompSample_5_1"
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
          "SMILES": null,
          "sample_num": "DOIcompSample_5_1"
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
      "parent_n_datapoints": 596,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_895",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_28"
      ],
      "description": "Excess molar volume of water+methanol binary, 623.15 K (fixed), 20000–35000 kPa, x(MeOH) 0.04–0.95, 34 points, supercritical conditions.",
      "doi": "10.1016/j.fluid.2010.10.005",
      "lit_id": "2011-ono-kob-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 34,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
          "constr_num_id": "GLOBconstr_2",
          "constr_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "value": 623.15,
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
            "min": 20000.0,
            "max": 35000.0,
            "n_unique": 4
          },
          "range_min": 20000.0,
          "range_max": 35000.0
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
            "min": 0.04,
            "max": 0.95,
            "n_unique": 27
          },
          "range_min": 0.04,
          "range_max": 0.95
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_28",
          "prop_ID": "excess_molar_volume_m3_mol",
          "name": "Excess molar volume, m3/mol",
          "group": "VolumetricProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_29",
          "meas_ID": "calculated_with_densities_of_this_investigation",
          "method_standard": "Calculated with densities of this investigation",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Excess molar volume, m3/mol",
            "min": -6e-06,
            "max": 3.9e-05,
            "mean": 6e-06,
            "std": 1.1e-05,
            "n": 34
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -6e-06,
          "range_max": 3.9e-05
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
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 34,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2395",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_4",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_28"
      ],
      "description": "Excess molar volume of water+methanol binary, 298.15–348.15 K, 100–60000 kPa, x(MeOH) 0.25–0.75, 206 points, near-ambient to high pressure.",
      "doi": "10.1016/j.jct.2004.03.011",
      "lit_id": "2004-saf-hey-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 206,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_4",
          "name": "methanol",
          "formula": "CH4O",
          "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
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
            "max": 523.15,
            "n_unique": 10
          },
          "range_min": 298.15,
          "range_max": 523.15
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
            "max": 60000.0,
            "n_unique": 8
          },
          "range_min": 100.0,
          "range_max": 60000.0
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
            "min": 0.25,
            "max": 0.75,
            "n_unique": 3
          },
          "range_min": 0.25,
          "range_max": 0.75
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_28",
          "prop_ID": "excess_molar_volume_m3_mol",
          "name": "Excess molar volume, m3/mol",
          "group": "VolumetricProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_207",
          "meas_ID": "same_ufactor_2",
          "method_standard": null,
          "method_custom": "SAME:UFactor:2",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Excess molar volume, m3/mol",
            "min": -3e-06,
            "max": -0.0,
            "mean": -1e-06,
            "std": 0.0,
            "n": 206
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -3e-06,
          "range_max": -0.0
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
      "parent_n_datapoints": 206,
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
  "answer": "## Water + Ethylene Glycol Binary Mixture: Property Data Availability in ThermoML\n\n### Summary of Property Coverage\n\n| Property | Global ID | Blocks Found | Temperature Range | Notes |\n|----------|-----------|:------------:|-------------------|-------|\n| **Mass Density** | GLOBprop_1 | 16 | ~278–446 K | Best coverage; full composition range; atmospheric to high pressure |\n| **Viscosity** | GLOBprop_4 | 7 | ~273–450 K | Good coverage; full composition range |\n| **Surface Tension** | GLOBprop_13 | 4 | 283–323 K | Limited to near-ambient temperatures; 4 DOIs |\n| **Excess Molar Volume** | GLOBprop_28 | 1 | From GLOBlit_1283 (DOI: 10.1016/j.fluid.2013.06.041) | 135 data points; limited but present |\n| **Electrical Conductivity** | GLOBprop_18 | 0 | — | **No data found** in ThermoML for this binary system |\n\n### Key Findings\n\n1. **Mass density** has the richest coverage for water+ethylene glycol with 16 data blocks spanning ~278–446 K and full composition ranges. This is the most thoroughly characterized property for this system in ThermoML.\n\n2. **Viscosity** has good coverage with 7 blocks spanning ~273–450 K across the full composition range. This is important for mass transport modeling in electrodeposition applications.\n\n3. **Surface tension** data is available across 4 blocks from 4 DOIs, but limited to near-ambient temperatures (283–323 K). Ethylene glycol composition ranges vary across blocks.\n\n4. **Excess molar volume** data is present but limited to a single block from GLOBlit_1283 (DOI: 10.1016/j.fluid.2013.06.041) with 135 data points. This is better than the water+ethanol system (which had zero blocks) but less extensive than water+methanol (2 blocks, 240 points).\n\n5. **Electrical conductivity** — no data found in ThermoML for the water+ethylene glycol binary system. This is a significant gap for electrodeposition applications, where ionic conductivity is critical.\n\n### Comparison with Water+Ethanol and Water+Methanol\n\nCompared to the previously examined systems:\n- Water+ethylene glycol has more surface tension blocks (4) than water+ethanol (3) and water+methanol (0).\n- It has fewer density blocks (16) than water+ethanol (29) but comparable to water+methanol (18).\n- It has fewer viscosity blocks (7) than water+ethanol (14) but more than water+methanol (6).\n- It has 1 excess molar volume block, compared to 0 for water+ethanol and 2 for water+methanol.\n- Like water+methanol, it lacks electrical conductivity data entirely (water+ethanol had 1 sparse block).\n\nFor electrodeposition-relevant characterization, the water+ethylene glycol system has reasonable coverage of transport and volumetric properties but is missing electrical conductivity data — the property most directly relevant to electrochemical applications.",
  "core_claims": [
    "In ThermoML, the water+ethylene glycol binary system has mass density as its most extensively covered property (16 blocks, ~278–446 K, full composition range), followed by viscosity (7 blocks, ~273–450 K), surface tension (4 blocks, 283–323 K near-ambient only), and excess molar volume (1 block, 135 data points from a single DOI).",
    "No electrical conductivity data were found in ThermoML for the water+ethylene glycol binary system, representing a significant gap for electrodeposition-relevant characterization.",
    "Compared to water+ethanol and water+methanol systems, water+ethylene glycol has more surface tension blocks but fewer density and viscosity blocks; its excess molar volume coverage (1 block) falls between water+ethanol (0 blocks) and water+methanol (2 blocks).",
    "The water+ethylene glycol system has reasonable coverage of transport and volumetric properties in ThermoML but lacks the electrical conductivity data most directly relevant to electrochemical applications."
  ],
  "status": "success",
  "summary": "For the water + ethylene glycol binary mixture in ThermoML, mass density has the richest coverage (16 data blocks, ~278–446 K, full composition range), followed by viscosity (7 blocks, ~273–450 K), surface tension (4 blocks, 283–323 K, near-ambient only), and excess molar volume (1 block from DOI 10.1016/j.fluid.2013.06.041, 135 data points). No electrical conductivity data were found for this binary system, representing a significant gap for electrodeposition applications. Compared to water+ethanol and water+methanol systems, water+ethylene glycol has more surface tension blocks but fewer density and viscosity blocks, and like water+methanol it entirely lacks electrical conductivity data.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_2656",
      "block_number": "PROPblock_13",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+ethylene glycol at 293.15 K, 10 points, mass fraction composition, capillary Ostwald-Ubbelohde method.",
      "doi": "10.1016/j.jct.2006.01.011",
      "lit_id": "2006-tsi-mol-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 10,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
          "constr_num_id": "GLOBconstr_2",
          "constr_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "value": 293.15,
          "digits": 5,
          "component_org_num": null,
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
          "value": 101.325,
          "digits": 6,
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
            "min": 0.0,
            "max": 0.9,
            "n_unique": 10
          },
          "range_min": 0.0,
          "range_max": 0.9
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
            "min": 0.001008,
            "max": 0.013999,
            "mean": 0.004563,
            "std": 0.004021,
            "n": 10
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.001008,
          "range_max": 0.013999
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 10,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_24",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+ethylene glycol, 84 points, 293.15–303.15 K, x(EG) 0.0494–0.9532, concentric cylinders method.",
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_id": "2018-hog-tor-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 84,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
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
            "n_unique": 21
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
            "max": 0.020613,
            "mean": 0.007275,
            "std": 0.004937,
            "n": 84
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000759,
          "range_max": 0.020613
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
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
      "parent_n_datapoints": 84,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_6951",
      "block_number": "PROPblock_18",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+ethylene glycol, 33 points, 293.15–303.15 K, x(water) 0.0–1.0, falling/rolling sphere method.",
      "doi": "10.1021/acs.jced.6b00526",
      "lit_id": "2017-moo-ros-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 33,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
            "max": 303.15,
            "n_unique": 3
          },
          "range_min": 293.15,
          "range_max": 303.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_5",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_5",
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
          "meas_num_id": "GLOBmeas_8",
          "meas_ID": "falling_or_rolling_sphere_viscometry",
          "method_standard": "Falling or rolling sphere viscometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000755,
            "max": 0.02113,
            "mean": 0.007699,
            "std": 0.005532,
            "n": 33
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000755,
          "range_max": 0.02113
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 33,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8038",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+ethylene glycol, 77 points, 293.15–353.15 K, x(EG) 0.0–0.4036, capillary tube method.",
      "doi": "10.1021/je020140j",
      "lit_id": "2003-yan-ma-2",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 77,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
            "min": 0.0,
            "max": 1.0,
            "n_unique": 11
          },
          "range_min": 0.0,
          "range_max": 1.0
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
            "min": 293.15,
            "max": 353.15,
            "n_unique": 7
          },
          "range_min": 293.15,
          "range_max": 353.15
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
          "meas_num_id": "GLOBmeas_227",
          "meas_ID": "captub_ufactor_3",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:3",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000356,
            "max": 0.020833,
            "mean": 0.002967,
            "std": 0.003516,
            "n": 77
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000356,
          "range_max": 0.020833
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 77,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8106",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+ethylene glycol, 30 points, 296.45–449.85 K, x(EG) 0.25–0.75, capillary tube method.",
      "doi": "10.1021/je025610o",
      "lit_id": "2003-sun-tej-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 30,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
            "min": 0.25,
            "max": 0.75,
            "n_unique": 3
          },
          "range_min": 0.25,
          "range_max": 0.75
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
            "min": 296.45,
            "max": 449.85,
            "n_unique": 25
          },
          "range_min": 296.45,
          "range_max": 449.85
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
            "min": 0.000366,
            "max": 0.0123,
            "mean": 0.002177,
            "std": 0.002644,
            "n": 30
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000366,
          "range_max": 0.0123
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 30,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_11186",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Viscosity of water+ethylene glycol, 52 points, 308.15–323.15 K, x(EG) 0.0–1.0, capillary tube method.",
      "doi": "10.1021/je800271e",
      "lit_id": "2008-zha-zha-2",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 52,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
            "min": 308.15,
            "max": 323.15,
            "n_unique": 4
          },
          "range_min": 308.15,
          "range_max": 323.15
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
          "prop_num_id": "GLOBprop_4",
          "prop_ID": "viscosity_pa_s",
          "name": "Viscosity, Pa*s",
          "group": "TransportProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_165",
          "meas_ID": "captub_ufactor_8",
          "method_standard": null,
          "method_custom": "CAPTUB:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.00055,
            "max": 0.009212,
            "mean": 0.00189,
            "std": 0.00187,
            "n": 52
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.00055,
          "range_max": 0.009212
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 52,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_1223",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+ethylene glycol, 85 points, 278.15–323.15 K, x(EG) 0–0.501.",
      "doi": "10.1016/j.fluid.2013.01.025",
      "lit_id": "2013-ego-mak-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 85,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
            "min": 278.15,
            "max": 323.15,
            "n_unique": 5
          },
          "range_min": 278.15,
          "range_max": 323.15
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
            "n_unique": 17
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
            "min": 988.03,
            "max": 1123.8,
            "mean": 1068.402,
            "std": 40.438191,
            "n": 85
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 988.03,
          "range_max": 1123.8
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 85,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2268",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+ethylene glycol, 6 points, 283.15–333.15 K, constrained composition.",
      "doi": "10.1016/j.fluid.2018.11.035",
      "lit_id": "2019-jia-bi-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 6,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
        },
        {
          "BLKconstr_id": "BLKconstr_2",
          "constr_num_id": "GLOBconstr_5",
          "constr_id": "mass_fraction_DOIcomp_1",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "value": 0.365,
          "digits": 3,
          "component_org_num": "DOIcomp_1",
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
            "max": 333.15,
            "n_unique": 6
          },
          "range_min": 283.15,
          "range_max": 333.15
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
            "min": 1032.23,
            "max": 1059.35,
            "mean": 1046.515,
            "std": 10.153326,
            "n": 6
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1032.23,
          "range_max": 1059.35
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "lit_num_id": "GLOBlit_2656",
      "block_number": "PROPblock_12",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+ethylene glycol, 10 points, fixed T, w(EG) 0–0.9.",
      "doi": "10.1016/j.jct.2006.01.011",
      "lit_id": "2006-tsi-mol-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 10,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
          "constr_num_id": "GLOBconstr_2",
          "constr_id": "temperature_k",
          "name": "Temperature, K",
          "type": "eTemperature",
          "value": 293.15,
          "digits": 5,
          "component_org_num": null,
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
          "value": 101.325,
          "digits": 6,
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
            "min": 0.0,
            "max": 0.9,
            "n_unique": 10
          },
          "range_min": 0.0,
          "range_max": 0.9
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
            "min": 998.2,
            "max": 1103.7,
            "mean": 1050.429,
            "std": 37.730449,
            "n": 10
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 998.2,
          "range_max": 1103.7
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 10,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2831",
      "block_number": "PROPblock_10",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+ethylene glycol, 10 points, fixed T, molality composition variable.",
      "doi": "10.1016/j.jct.2007.05.010",
      "lit_id": "2008-kus-dag-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 10,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
          "component_org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "solvent_num_id": "GLOBsolvent_12",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N"
        }
      ],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
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
            "BLKvar_id": "BLKvar_1",
            "name": "Molality, mol/kg",
            "min": 0.0,
            "max": 1.13154,
            "n_unique": 10
          },
          "range_min": 0.0,
          "range_max": 1.13154
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
          "meas_num_id": "GLOBmeas_143",
          "meas_ID": "vibtub_ufactor_6",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:6",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 1108.1,
            "max": 1109.41,
            "mean": 1108.817,
            "std": 0.520321,
            "n": 10
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1108.1,
          "range_max": 1109.41
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 10,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_22",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of water+ethylene glycol, 224 points, 293.15–298.15 K, x(EG) 0.010–0.989.",
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_id": "2018-hog-tor-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 224,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
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
            "n_unique": 56
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
            "min": 994.252,
            "max": 1113.725,
            "mean": 1074.257442,
            "std": 36.051056,
            "n": 224
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 994.252,
          "range_max": 1113.725
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_2_1"
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
      "parent_n_datapoints": 224,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_3286",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of water+ethylene glycol, 54 points, 283.15–308.15 K, x(EG) 0.0078–0.8987, ring tensiometer.",
      "doi": "10.1016/j.jct.2010.09.003",
      "lit_id": "2011-raf-bag-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 54,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 283.15,
          "range_max": 308.15
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
            "min": 0.0078,
            "max": 0.8987,
            "n_unique": 53
          },
          "range_min": 0.0078,
          "range_max": 0.8987
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
          "meas_num_id": "GLOBmeas_19",
          "meas_ID": "ring_tensiometer",
          "method_standard": "Ring tensiometer",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.04791,
            "max": 0.0735,
            "mean": 0.060029,
            "std": 0.007421,
            "n": 54
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.04791,
          "range_max": 0.0735
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
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 54,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_4021",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of water+ethylene glycol, 4 points, 298.15 K fixed, volume fraction composition, Wilhelmy plate.",
      "doi": "10.1016/j.jct.2013.10.010",
      "lit_id": "2014-tiw-son-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 4,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
            "min": 0.0,
            "max": 0.3,
            "n_unique": 4
          },
          "range_min": 0.0,
          "range_max": 0.3
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
          "meas_num_id": "GLOBmeas_192",
          "meas_ID": "wilhelmy_plate_method",
          "method_standard": null,
          "method_custom": "Wilhelmy Plate Method",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0615,
            "max": 0.0718,
            "mean": 0.0666,
            "std": 0.004441,
            "n": 4
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0615,
          "range_max": 0.0718
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 4,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8553",
      "block_number": "PROPblock_16",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of water+ethylene glycol, 15 points, 298.15 K fixed, x(EG) 0.008–0.200, ring tensiometer.",
      "doi": "10.1021/je049955d",
      "lit_id": "2004-hab-hov-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 15,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_4_1"
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
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
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
          "var_num_id": "GLOBvar_2",
          "var_id": "mole_fraction_DOIcomp_4",
          "name": "Mole fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_4",
          "phase": {
            "phase": "Liquid",
            "phase_num_id": "GLOBphase_1",
            "phase_id": "liquid"
          },
          "range": {
            "BLKvar_id": "BLKvar_1",
            "name": "Mole fraction",
            "min": 0.008251,
            "max": 0.199955,
            "n_unique": 15
          },
          "range_min": 0.008251,
          "range_max": 0.199955
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
          "meas_num_id": "GLOBmeas_19",
          "meas_ID": "ring_tensiometer",
          "method_standard": "Ring tensiometer",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0579,
            "max": 0.0708,
            "mean": 0.067933,
            "std": 0.003485,
            "n": 15
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0579,
          "range_max": 0.0708
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
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "binary",
      "declared_n_components": 2,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_4_1"
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
      "parent_n_datapoints": 15,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_11186",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of water+ethylene glycol, 52 points, 308.15–323.15 K, x(EG) 0.0–1.0, drop volume method.",
      "doi": "10.1021/je800271e",
      "lit_id": "2008-zha-zha-2",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 52,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
            "min": 308.15,
            "max": 323.15,
            "n_unique": 4
          },
          "range_min": 308.15,
          "range_max": 323.15
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
          "prop_num_id": "GLOBprop_13",
          "prop_ID": "surface_tension_liquidgas_n_m",
          "name": "Surface tension liquid-gas, N/m",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_569",
          "meas_ID": "dropv_ufactor_4",
          "method_standard": null,
          "method_custom": "DROPV:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.046406,
            "max": 0.071023,
            "mean": 0.058347,
            "std": 0.006619,
            "n": 52
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.046406,
          "range_max": 0.071023
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 52,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_1283",
      "block_number": "PROPblock_11",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_24",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_28"
      ],
      "description": "Excess molar volume of water+ethylene glycol, 135 points, 283.15–313.15 K, x(EG) 0.00991–0.93949, 101.0 kPa, all VE values negative. DOI: 10.1016/j.fluid.2013.06.041.",
      "doi": "10.1016/j.fluid.2013.06.041",
      "lit_id": "2013-zem-tro-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 135,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
            "n_unique": 5
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
            "min": 0.00991,
            "max": 0.93949,
            "n_unique": 27
          },
          "range_min": 0.00991,
          "range_max": 0.93949
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_28",
          "prop_ID": "excess_molar_volume_m3_mol",
          "name": "Excess molar volume, m3/mol",
          "group": "VolumetricProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_29",
          "meas_ID": "calculated_with_densities_of_this_investigation",
          "method_standard": "Calculated with densities of this investigation",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Excess molar volume, m3/mol",
            "min": -0.0,
            "max": -0.0,
            "mean": -0.0,
            "std": 0.0,
            "n": 135
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -0.0,
          "range_max": -0.0
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
          "comp_num_id": "GLOBcomp_24",
          "name": "1,2-ethanediol",
          "formula": "C2H6O2",
          "inchi_key": "LYCAIKOWRPUZTN-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 135,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ]
}

