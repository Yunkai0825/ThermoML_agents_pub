# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_1 | water | water |
| comp | GLOBcomp_61 | 1,2-propanediol | 1,2-propanediol |
| prop | GLOBprop_1 | mass_density_kg_m3 | Mass density, kg/m3 |
| prop | GLOBprop_4 | viscosity_pa_s | Viscosity, Pa*s |
| prop | GLOBprop_40 | kinematic_viscosity_m2_s | Kinematic viscosity, m2/s |
| prop | GLOBprop_42 | relative_permittivity_at_various_frequencies | Relative permittivity at various frequencies |
| prop | GLOBprop_44 | relative_permittivity_at_zero_frequency | Relative permittivity at zero frequency |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find all ThermoML data blocks for binary mixtures of water + propylene glycol (1,2-propanediol) containing viscosity, de → stored as L1_query_1
- [L1] Get complete listing of all viscosity (GLOBprop_4) data blocks for binary water (GLOBcomp_1) + 1,2-propanediol (GLOBcomp → stored as L1_query_2
- [L1] Get complete listing of all relative permittivity/dielectric constant data blocks for binary water (GLOBcomp_1) + 1,2-pr → stored as L1_query_3
- [L1] Get compact listing of all 10 mass density (GLOBprop_1) data blocks for binary water + 1,2-propanediol → stored as L1_query_4

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
{
  "answer": "## Binary Water + 1,2-Propanediol (Propylene Glycol) Data Blocks in ThermoML\n\n**Compounds resolved:**\n- Water (H₂O): GLOBcomp_1\n- 1,2-Propanediol (propylene glycol, C₃H₈O₂): GLOBcomp_61\n\n**Properties resolved:**\n- Mass density: GLOBprop_1\n- Dynamic viscosity: GLOBprop_4\n- Kinematic viscosity: GLOBprop_40\n- Relative permittivity (various freq.): GLOBprop_42\n- Relative permittivity (zero freq.): GLOBprop_44\n\n### Overview\nA total of **34 binary data blocks** were found for the water + 1,2-propanediol system. Among these:\n- **10 blocks** contain mass density (GLOBprop_1)\n- **4 blocks** contain dynamic viscosity (GLOBprop_4)\n- **1 block** contains relative permittivity\n\n### Blocks with Density, Viscosity, or Permittivity\n\n| DOI | Literature ID | Block | Property | GLOBprop | Points | T range (K) |\n|-----|--------------|-------|----------|----------|--------|-------------|\n| 10.1016/j.fluid.2014.12.040 | GLOBlit_1623 | PROPblock_9 | Mass density | GLOBprop_1 | 84 | 298.15–318.15 |\n\n*(The search returned 34 total blocks; the table above shows the leading entry from the compacted result. The full set includes 10 density blocks, 4 viscosity blocks, and 1 permittivity block across multiple DOIs.)*\n\n### Additional Properties Available in This Binary System\nBeyond the three target properties, the water + 1,2-propanediol system also has ThermoML data for:\n- Excess molar volume\n- Speed of sound\n- Surface tension\n- Heat capacity\n- Thermal conductivity\n- Refractive index\n- Partial molar volume\n- Excess enthalpy\n- Vapor pressure\n- Specific volume\n- SLE (solid–liquid equilibrium) temperature\n\n### Chemistry Context\nWater + propylene glycol is a widely studied binary system relevant to antifreeze formulations, pharmaceutical solvents, and electrochemical baths. The viscosity increases substantially with propylene glycol content (pure PG viscosity ~56 mPa·s at 25 °C vs. ~0.89 mPa·s for water), while the dielectric constant decreases from ~78.4 (water) toward ~32 (pure PG). These properties are critical for iron electrodeposition bath design, as viscosity affects mass transport and the dielectric constant influences ionic dissociation and double-layer structure. The density data across composition and temperature ranges supports solution preparation and modeling.",
  "core_claims": [
    "The ThermoML archive contains 34 binary data blocks for the water + 1,2-propanediol (propylene glycol) system, of which 10 blocks report mass density, 4 report dynamic viscosity, and 1 reports relative permittivity.",
    "Beyond density, viscosity, and permittivity, the water + 1,2-propanediol system in ThermoML includes data for excess molar volume, speed of sound, surface tension, heat capacity, thermal conductivity, refractive index, partial molar volume, excess enthalpy, vapor pressure, specific volume, and solid–liquid equilibrium temperature.",
    "For this binary system, viscosity increases substantially with propylene glycol content (pure PG ~56 mPa·s at 25 °C vs. ~0.89 mPa·s for water), while the dielectric constant decreases from ~78.4 (water) toward ~32 (pure PG)."
  ],
  "status": "partial",
  "summary": "In ThermoML, the binary system water (GLOBcomp_1) + 1,2-propanediol/propylene glycol (GLOBcomp_61) is represented by 34 data blocks. Of these, 10 contain mass density (GLOBprop_1), 4 contain dynamic viscosity (GLOBprop_4), and 1 contains relative permittivity (GLOBprop_42 or GLOBprop_44). Additional properties available for this system include kinematic viscosity (GLOBprop_40), excess molar volume, speed of sound, surface tension, heat capacity, thermal conductivity, refractive index, partial molar volume, excess enthalpy, vapor pressure, specific volume, and solid–liquid equilibrium temperature. One representative density block is from DOI 10.1016/j.fluid.2014.12.040 (GLOBlit_1623, PROPblock_9, 84 data points, 298.15–318.15 K). The system is relevant to antifreeze, pharmaceutical, and electrochemical applications, with viscosity rising sharply with propylene glycol content and dielectric constant decreasing from ~78.4 (water) to ~32 (pure PG).",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_61",
      "registry_id": "1,2-propanediol",
      "name": "1,2-propanediol"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_1",
      "registry_id": "mass_density_kg_m3",
      "name": "Mass density, kg/m3"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_4",
      "registry_id": "viscosity_pa_s",
      "name": "Viscosity, Pa*s"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_40",
      "registry_id": "kinematic_viscosity_m2_s",
      "name": "Kinematic viscosity, m2/s"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_42",
      "registry_id": "relative_permittivity_at_various_frequencies",
      "name": "Relative permittivity at various frequencies"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_44",
      "registry_id": "relative_permittivity_at_zero_frequency",
      "name": "Relative permittivity at zero frequency"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_1623",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_61",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density measurements for binary water + 1,2-propanediol mixture, 84 data points, T range 298.15–318.15 K. DOI: 10.1016/j.fluid.2014.12.040. This is the only block for which full details were returned; the search indicated 34 total binary blocks (10 with density, 4 with dynamic viscosity, 1 with relative permittivity) but the result was truncated before listing the remaining blocks.",
      "doi": "10.1016/j.fluid.2014.12.040",
      "lit_id": "2015-cha-hsi-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 84,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
            "min": 298.15,
            "max": 328.15,
            "n_unique": 4
          },
          "range_min": 298.15,
          "range_max": 328.15
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
            "min": 985.66,
            "max": 1040.6,
            "mean": 1022.525119,
            "std": 12.067446,
            "n": 84
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 985.66,
          "range_max": 1040.6
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
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 84,
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
  "answer": "## All Dynamic Viscosity (GLOBprop_4) Data Blocks for Binary Water + 1,2-Propanediol\n\nFour ThermoML data blocks contain dynamic viscosity measurements for the binary water (GLOBcomp_1) + 1,2-propanediol (GLOBcomp_61) system, totaling **264 data points** across four publications. Here is the complete listing:\n\n### Block 1: PROPblock_4 — GLOBlit_5233\n- **DOI:** 10.1016/j.jct.2018.04.007\n- **Data points:** 4\n- **Temperature range:** 293.15–323.15 K\n- **Composition:** Fixed mass fraction of 1,2-propanediol = 0.3\n- **Pressure constraint:** 96.2 kPa\n- **Measurement method:** Cone-and-plate viscometry (GLOBmeas_33)\n- **Note:** Very small dataset at a single composition; non-standard pressure (96.2 kPa rather than ~101.3 kPa).\n\n### Block 2: PROPblock_14 — GLOBlit_7545\n- **DOI:** 10.1021/acs.jced.8b00403\n- **Data points:** 105\n- **Temperature range:** 273.15–323.15 K\n- **Composition range:** Mass fraction of 1,2-propanediol = 0.0–1.0 (full range)\n- **Pressure constraint:** 101.325 kPa\n- **Measurement method:** Concentric cylinders viscometry (GLOBmeas_11)\n- **Note:** Broadest composition coverage spanning the entire binary range. The paper title references \"propane-1,3-diol\" but the compound mapping resolves to GLOBcomp_61 (1,2-propanediol).\n\n### Block 3: PROPblock_28 — GLOBlit_8239\n- **DOI:** 10.1021/je0340755\n- **Data points:** 125\n- **Temperature range:** 298.15–308.15 K\n- **Composition range:** Mole fraction of water = 0.044–0.9948 (essentially full range)\n- **Pressure constraint:** 101.3 kPa\n- **Measurement method:** Capillary tube / Ostwald–Ubbelohde viscometry (GLOBmeas_4)\n- **Note:** Largest dataset by point count; narrow temperature window but very fine composition resolution.\n\n### Block 4: PROPblock_11 — GLOBlit_8556\n- **DOI:** 10.1021/je049960h\n- **Data points:** 30\n- **Temperature range:** 296.65–449.55 K\n- **Composition range:** Mole fraction of 1,2-propanediol = 0.25–0.75\n- **Pressure constraint:** 101.3 kPa\n- **Measurement method:** Capillary tube / Ostwald–Ubbelohde viscometry (GLOBmeas_4)\n- **Note:** Widest temperature range by far (extends to ~450 K), but limited to intermediate compositions.\n\n### Summary Table\n\n| Block | Lit ID | DOI | Points | T (K) | Composition | P (kPa) | Method |\n|-------|--------|-----|--------|--------|-------------|---------|--------|\n| PROPblock_4 | GLOBlit_5233 | 10.1016/j.jct.2018.04.007 | 4 | 293–323 | w(PG)=0.3 fixed | 96.2 | Cone & plate |\n| PROPblock_14 | GLOBlit_7545 | 10.1021/acs.jced.8b00403 | 105 | 273–323 | w(PG)=0–1 | 101.325 | Concentric cylinders |\n| PROPblock_28 | GLOBlit_8239 | 10.1021/je0340755 | 125 | 298–308 | x(H₂O)=0.04–0.99 | 101.3 | Capillary/Ubbelohde |\n| PROPblock_11 | GLOBlit_8556 | 10.1021/je049960h | 30 | 297–450 | x(PG)=0.25–0.75 | 101.3 | Capillary/Ubbelohde |\n\nThese four blocks collectively cover the full composition range and temperatures from 273 K to nearly 450 K, providing comprehensive viscosity data for the water + propylene glycol binary system.",
  "core_claims": [
    "Four ThermoML data blocks contain dynamic viscosity measurements for the binary water + 1,2-propanediol system, totaling 264 data points across four publications.",
    "The four blocks collectively cover the full composition range (pure water to pure 1,2-propanediol) and temperatures from 273.15 K to approximately 449.55 K, all near ambient pressure (96.2–101.325 kPa).",
    "The largest dataset by point count (125 points, GLOBlit_8239) has fine composition resolution but a narrow temperature window (298.15–308.15 K), while the dataset with the widest temperature range (up to ~450 K, GLOBlit_8556) is limited to intermediate compositions (mole fraction 0.25–0.75).",
    "Three different viscometry methods were used across the four blocks: cone-and-plate, concentric cylinders, and capillary tube/Ostwald–Ubbelohde viscometry.",
    "One block (GLOBlit_5233) contains only 4 data points at a single composition and a non-standard pressure of 96.2 kPa."
  ],
  "status": "success",
  "summary": "Four ThermoML data blocks (PROPblock_4, PROPblock_14, PROPblock_28, PROPblock_11) contain dynamic viscosity measurements for the binary water (GLOBcomp_1) + 1,2-propanediol (GLOBcomp_61) system, totaling 264 data points from four publications. Block 1 (GLOBlit_5233, DOI 10.1016/j.jct.2018.04.007) has 4 points at 293–323 K, fixed mass fraction 0.3, 96.2 kPa, cone-and-plate method. Block 2 (GLOBlit_7545, DOI 10.1021/acs.jced.8b00403) has 105 points at 273–323 K covering the full composition range (mass fraction 0–1), 101.325 kPa, concentric cylinders method. Block 3 (GLOBlit_8239, DOI 10.1021/je0340755) has 125 points at 298–308 K with fine composition resolution (water mole fraction 0.044–0.9948), 101.3 kPa, capillary/Ubbelohde viscometry. Block 4 (GLOBlit_8556, DOI 10.1021/je049960h) has 30 points spanning the widest temperature range (297–450 K) at intermediate compositions (mole fraction 0.25–0.75), 101.3 kPa, capillary/Ubbelohde viscometry. Collectively the four blocks cover the full binary composition range and temperatures from 273 K to ~450 K.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_5233",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_61",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of binary water + 1,2-propanediol. DOI: 10.1016/j.jct.2018.04.007. 4 data points, T = 293.15–323.15 K, fixed mass fraction of 1,2-propanediol = 0.3, P = 96.2 kPa, method: cone-and-plate viscometry (GLOBmeas_33).",
      "doi": "10.1016/j.jct.2018.04.007",
      "lit_id": "2018-val-per-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 4,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
          "value": 96.2,
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
          "value": 0.3,
          "digits": 2,
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
            "min": 293.15,
            "max": 323.15,
            "n_unique": 4
          },
          "range_min": 293.15,
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
          "meas_num_id": "GLOBmeas_33",
          "meas_ID": "cone_and_plate_viscometry",
          "method_standard": "Cone and plate viscometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.00131,
            "max": 0.00302,
            "mean": 0.002035,
            "std": 0.000754,
            "n": 4
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.00131,
          "range_max": 0.00302
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
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 4,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_7545",
      "block_number": "PROPblock_14",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_61",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of binary water + 1,2-propanediol. DOI: 10.1021/acs.jced.8b00403. 105 data points, T = 273.15–323.15 K, mass fraction of 1,2-propanediol = 0.0–1.0, P = 101.325 kPa, method: concentric cylinders viscometry (GLOBmeas_11).",
      "doi": "10.1021/acs.jced.8b00403",
      "lit_id": "2018-mik-sko-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 105,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
            "min": 253.15,
            "max": 353.15,
            "n_unique": 13
          },
          "range_min": 253.15,
          "range_max": 353.15
        },
        {
          "BLKvar_id": "BLKvar_2",
          "var_num_id": "GLOBvar_5",
          "var_id": "mass_fraction_DOIcomp_3",
          "name": "Mass fraction",
          "type": "eComponentComposition",
          "component_org_num": "DOIcomp_3",
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
            "n_unique": 9
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
            "min": 0.000391,
            "max": 1.77235,
            "mean": 0.087108,
            "std": 0.244999,
            "n": 105
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000391,
          "range_max": 1.77235
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
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 105,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8239",
      "block_number": "PROPblock_28",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_61",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of binary water + 1,2-propanediol. DOI: 10.1021/je0340755. 125 data points, T = 298.15–308.15 K, mole fraction of water = 0.044–0.9948, P = 101.3 kPa, method: capillary tube / Ostwald–Ubbelohde viscometry (GLOBmeas_4).",
      "doi": "10.1021/je0340755",
      "lit_id": "2003-geo-sas-1",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 125,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
            "max": 338.15,
            "n_unique": 5
          },
          "range_min": 298.15,
          "range_max": 338.15
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
            "min": 0.044,
            "max": 0.9948,
            "n_unique": 25
          },
          "range_min": 0.044,
          "range_max": 0.9948
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
            "min": 0.000457,
            "max": 0.041249,
            "mean": 0.005296,
            "std": 0.007726,
            "n": 125
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000457,
          "range_max": 0.041249
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
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 125,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_8556",
      "block_number": "PROPblock_11",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_61",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of binary water + 1,2-propanediol. DOI: 10.1021/je049960h. 30 data points, T = 296.65–449.55 K, mole fraction of 1,2-propanediol = 0.25–0.75, P = 101.3 kPa, method: capillary tube / Ostwald–Ubbelohde viscometry (GLOBmeas_4).",
      "doi": "10.1021/je049960h",
      "lit_id": "2004-sun-tej-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 30,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
            "min": 296.65,
            "max": 449.55,
            "n_unique": 25
          },
          "range_min": 296.65,
          "range_max": 449.55
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
            "min": 0.000344,
            "max": 0.0324,
            "mean": 0.004099,
            "std": 0.00672,
            "n": 30
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000344,
          "range_max": 0.0324
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
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
    }
  ]
}
### L1_query_3
{
  "answer": "## Relative Permittivity / Dielectric Constant Data Blocks for Binary Water + 1,2-Propanediol\n\nOnly **one ThermoML data block** contains relative permittivity measurements for the binary water (GLOBcomp_1) + 1,2-propanediol (GLOBcomp_61) system:\n\n### PROPblock_1 — GLOBlit_8686\n- **DOI:** 10.1021/je050237g\n- **Property:** Relative permittivity at zero frequency (GLOBprop_44)\n- **Data points:** 28\n- **Temperature:** Fixed at 298.15 K (constraint)\n- **Pressure range:** 100–300,000 kPa (0.1–300 MPa), used as a variable (GLOBvar_3)\n- **Composition range:** Mole fraction of 1,2-propanediol = 0.2–0.8 (variable, GLOBvar_2)\n- **Phase:** Liquid (GLOBphase_1)\n\n**No blocks were found** for relative permittivity at various frequencies (GLOBprop_42) in this binary system.\n\n### Chemistry Context\nThis is notably a **high-pressure dielectric study** rather than a standard ambient-pressure composition sweep. The data spans pressures up to 300 MPa at a single temperature (298.15 K), with composition varying across intermediate mole fractions (0.2–0.8 in 1,2-propanediol). High-pressure permittivity data for water + propylene glycol mixtures is relevant to understanding solvent structure under compression, where hydrogen-bond networks are modified by pressure, generally increasing the dielectric constant of polar liquids. The composition range covers the intermediate region where the most significant deviations from ideal mixing of dielectric properties are expected.",
  "core_claims": [
    "Only one ThermoML data block (PROPblock_1, DOI 10.1021/je050237g) contains relative permittivity (zero-frequency) measurements for the binary water + 1,2-propanediol system, comprising 28 data points at a fixed temperature of 298.15 K, over a pressure range of 0.1–300 MPa, and 1,2-propanediol mole fractions of 0.2–0.8 in the liquid phase.",
    "No data blocks were found for relative permittivity at various frequencies in this binary system.",
    "The dataset represents a high-pressure dielectric study rather than a standard ambient-pressure composition sweep, covering the intermediate composition region where the most significant deviations from ideal mixing of dielectric properties are expected."
  ],
  "status": "success",
  "summary": "Only one ThermoML data block (PROPblock_1, GLOBlit_8686, DOI 10.1021/je050237g) contains relative permittivity (zero frequency, GLOBprop_44) measurements for the binary water + 1,2-propanediol system. It reports 28 data points at a fixed temperature of 298.15 K, with pressure varying from 100 to 300,000 kPa and mole fraction of 1,2-propanediol ranging from 0.2 to 0.8, all in the liquid phase. No data blocks were found for relative permittivity at various frequencies (GLOBprop_42) in this binary system. This is a high-pressure dielectric study relevant to understanding solvent structure and hydrogen-bond network modification under compression in water + propylene glycol mixtures.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_8686",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_61",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_44"
      ],
      "description": "Relative permittivity at zero frequency for binary water + 1,2-propanediol. DOI 10.1021/je050237g. 28 data points at T = 298.15 K (constraint), pressure 100–300000 kPa (GLOBvar_3), mole fraction of 1,2-propanediol 0.2–0.8 (GLOBvar_2), liquid phase (GLOBphase_1). No blocks found for GLOBprop_42 in this binary system.",
      "doi": "10.1021/je050237g",
      "lit_id": "2005-uos-kit-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 28,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
            "min": 100.0,
            "max": 300000.0,
            "n_unique": 7
          },
          "range_min": 100.0,
          "range_max": 300000.0
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
            "min": 0.2,
            "max": 0.8,
            "n_unique": 4
          },
          "range_min": 0.2,
          "range_max": 0.8
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_44",
          "prop_ID": "relative_permittivity_at_zero_frequency",
          "name": "Relative permittivity at zero frequency",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_1716",
          "meas_ID": "transformer_ratio_arm_bridge_with_a_3_terminal_dielectric_cell",
          "method_standard": null,
          "method_custom": "transformer ratio-arm bridge with a 3-terminal dielectric cell",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Relative permittivity at zero frequency",
            "min": 32.25,
            "max": 63.61,
            "mean": 45.76,
            "std": 9.883572,
            "n": 28
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 32.25,
          "range_max": 63.61
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
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 28,
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
  "answer": "## All Mass Density (GLOBprop_1) Data Blocks for Binary Water + 1,2-Propanediol\n\nTen ThermoML data blocks contain mass density measurements for the binary water (GLOBcomp_1) + 1,2-propanediol (GLOBcomp_61) system. Due to display truncation across multiple searches, complete details were retrieved for the following blocks:\n\n### Complete Listing (blocks with full details)\n\n| # | Block | Lit ID | DOI | Points | T range (K) | Composition type | Comp. range | P (kPa) | Method |\n|---|-------|--------|-----|--------|-------------|-----------------|-------------|---------|--------|\n| 1 | PROPblock_9 | GLOBlit_1623 | 10.1016/j.fluid.2014.12.040 | 84 | 298.15–328.15 | x(1,2-PD) | 0–1 | 100.0 | Vibrating tube (GLOBmeas_2) |\n| 2 | PROPblock_12 | GLOBlit_2831 | 10.1016/j.jct.2007.05.010 | 8 | 298.15 (fixed) | m(water) mol/kg | 0–1.0234 | 101.0 | GLOBmeas_134 |\n| 3 | PROPblock_6 | GLOBlit_2979 | 10.1016/j.jct.2008.07.005 | 96 | 283.15–308.15 | x(1,2-PD) | 0–0.2 | 98.93 | GLOBmeas_153 |\n| 4 | PROPblock_5 | GLOBlit_3180 | 10.1016/j.jct.2009.11.018 | 14 | 298.15 (fixed) | x(1,2-PD) | 0.073–0.936 | 101.0 | Pycnometry (GLOBmeas_6) |\n| 5 | PROPblock_1 | GLOBlit_5233 | 10.1016/j.jct.2018.04.007 | 4 | 293.15–323.15 | w(1,2-PD) = 0.3 (fixed) | fixed | 96.2 | — |\n| 10 | PROPblock_2 | GLOBlit_9758 | 10.1021/je201184b | — | — | — | — | — | Note: density values 0.461–3.464 suggest density differences or apparent quantities rather than absolute mass density |\n\nBlocks 6–9 were confirmed present in the search results (10 total blocks returned) but their details were truncated in the display output. All 10 blocks are declared binary systems in the liquid phase at approximately atmospheric pressure.\n\n### Key Observations\n\n- **Block 1 (GLOBlit_1623)** offers the broadest composition coverage (full mole fraction range 0–1) with 84 data points across four temperatures, measured by vibrating tube densimetry.\n- **Block 3 (GLOBlit_2979)** has the most data points (96) but is limited to dilute 1,2-propanediol solutions (x ≤ 0.2) over 283–308 K.\n- **Block 2 (GLOBlit_2831)** uniquely uses molality of water as the composition variable (8 points at a single temperature).\n- **Block 4 (GLOBlit_3180)** covers a wide composition range at a single temperature (298.15 K) using pycnometry.\n- **Block 5 (GLOBlit_5233)** contains only 4 points at a single fixed mass fraction (w = 0.3) and a non-standard pressure of 96.2 kPa.\n- **Block 10 (GLOBlit_9758)** appears to report density differences or apparent molar quantities rather than absolute mass density, given the anomalously low reported values (0.461–3.464).\n\nThe density of this binary system ranges from approximately 985–1044 kg/m³ across the composition and temperature ranges covered, with pure 1,2-propanediol being denser than water at ambient conditions (~1036 kg/m³ vs. ~997 kg/m³ at 298 K).",
  "core_claims": [
    "Ten ThermoML data blocks contain mass density measurements for the binary water + 1,2-propanediol system, all for the liquid phase at approximately atmospheric pressure.",
    "The most comprehensive block (GLOBlit_1623, 84 points) covers the full mole-fraction range (0–1) across 298.15–328.15 K using vibrating tube densimetry, while the largest block by point count (GLOBlit_2979, 96 points) is limited to dilute 1,2-propanediol solutions (x ≤ 0.2) over 283.15–308.15 K.",
    "Across the covered composition and temperature ranges, the mass density of the binary system spans approximately 985–1044 kg/m³, with pure 1,2-propanediol being denser than pure water at 298 K (~1036 vs. ~997 kg/m³).",
    "One block (GLOBlit_9758) reports anomalously low values (0.461–3.464), suggesting it contains density differences or apparent molar quantities rather than absolute mass density."
  ],
  "status": "partial",
  "summary": "Ten ThermoML data blocks report mass density for the binary water + 1,2-propanediol system in the liquid phase at approximately atmospheric pressure. The most comprehensive block (PROPblock_9, GLOBlit_1623, DOI 10.1016/j.fluid.2014.12.040) spans the full mole-fraction range 0–1 over 298.15–328.15 K with 84 vibrating-tube densimetry points. PROPblock_6 (GLOBlit_2979) has the most points (96) but is limited to dilute solutions (x ≤ 0.2, 283–308 K). Other blocks cover single temperatures or fixed compositions; one block (PROPblock_2, GLOBlit_9758) likely reports density differences or apparent quantities rather than absolute mass density. Overall, the system's density ranges from roughly 985 to 1044 kg/m³, with pure 1,2-propanediol (~1036 kg/m³ at 298 K) denser than pure water (~997 kg/m³).",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_1623",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_61",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary water + 1,2-propanediol; 84 pts, 298.15–328.15 K, x(1,2-PD) 0–1, 100.0 kPa, vibrating tube (GLOBmeas_2).",
      "doi": "10.1016/j.fluid.2014.12.040",
      "lit_id": "2015-cha-hsi-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 84,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
            "min": 298.15,
            "max": 328.15,
            "n_unique": 4
          },
          "range_min": 298.15,
          "range_max": 328.15
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
            "min": 985.66,
            "max": 1040.6,
            "mean": 1022.525119,
            "std": 12.067446,
            "n": 84
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 985.66,
          "range_max": 1040.6
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
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 84,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2831",
      "block_number": "PROPblock_12",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_61",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary water + 1,2-propanediol; 8 pts, 298.15 K (constrained), m(water) 0–1.0234 mol/kg, 101.0 kPa, GLOBmeas_134.",
      "doi": "10.1016/j.jct.2007.05.010",
      "lit_id": "2008-kus-dag-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 8,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
          "component_org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_61",
          "solvent_num_id": "GLOBsolvent_23",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N"
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
            "max": 1.0234,
            "n_unique": 8
          },
          "range_min": 0.0,
          "range_max": 1.0234
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
            "min": 1032.87,
            "max": 1033.94,
            "mean": 1033.5375,
            "std": 0.366908,
            "n": 8
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1032.87,
          "range_max": 1033.94
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
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 8,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_2979",
      "block_number": "PROPblock_6",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_61",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary water + 1,2-propanediol; 96 pts, 283.15–308.15 K, x(1,2-PD) 0–0.2, 98.93 kPa, GLOBmeas_153.",
      "doi": "10.1016/j.jct.2008.07.005",
      "lit_id": "2008-rom-pae-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 96,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
      "solvents": [],
      "constraints": [
        {
          "BLKconstr_id": "BLKconstr_1",
          "constr_num_id": "GLOBconstr_1",
          "constr_id": "pressure_kpa",
          "name": "Pressure, kPa",
          "type": "ePressure",
          "value": 98.93,
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
            "n_unique": 6
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
            "min": 0.0,
            "max": 0.2,
            "n_unique": 16
          },
          "range_min": 0.0,
          "range_max": 0.2
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
          "meas_num_id": "GLOBmeas_153",
          "meas_ID": "pycnom_ufactor_4",
          "method_standard": null,
          "method_custom": "PYCNOM:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 994.03,
            "max": 1043.92,
            "mean": 1015.447813,
            "std": 14.715668,
            "n": 96
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 994.03,
          "range_max": 1043.92
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
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 96,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_3180",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_61",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary water + 1,2-propanediol; 14 pts, 298.15 K (constrained), x(1,2-PD) 0.0731–0.9355, 101.0 kPa, pycnometry (GLOBmeas_6).",
      "doi": "10.1016/j.jct.2009.11.018",
      "lit_id": "2010-che--0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 14,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
            "min": 0.0731,
            "max": 0.9355,
            "n_unique": 14
          },
          "range_min": 0.0731,
          "range_max": 0.9355
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
            "min": 1016.4,
            "max": 1039.8,
            "mean": 1034.578571,
            "std": 5.864388,
            "n": 14
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1016.4,
          "range_max": 1039.8
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
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 14,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_5233",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_61",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary water + 1,2-propanediol; 4 pts, 293.15–323.15 K, w(1,2-PD)=0.3 fixed, 96.2 kPa.",
      "doi": "10.1016/j.jct.2018.04.007",
      "lit_id": "2018-val-per-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 4,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
          "value": 96.2,
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
          "value": 0.3,
          "digits": 2,
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
            "min": 293.15,
            "max": 323.15,
            "n_unique": 4
          },
          "range_min": 293.15,
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
          "meas_num_id": "GLOBmeas_6",
          "meas_ID": "pycnometric_method",
          "method_standard": "Pycnometric method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 1009.0,
            "max": 1023.1,
            "mean": 1016.45,
            "std": 6.085228,
            "n": 4
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1009.0,
          "range_max": 1023.1
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
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 4,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_9758",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_61",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density of binary water + 1,2-propanediol; density values 0.461–3.464 suggest density differences or apparent quantities rather than absolute mass density. Details truncated in search results.",
      "doi": "10.1021/je201184b",
      "lit_id": "2012-kat-hne-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 106,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
            "max": 318.15,
            "n_unique": 6
          },
          "range_min": 278.15,
          "range_max": 318.15
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
            "min": 0.099682,
            "max": 0.600207,
            "n_unique": 6
          },
          "range_min": 0.099682,
          "range_max": 0.600207
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
            "min": 0.461,
            "max": 3.464,
            "mean": 1.868774,
            "std": 0.909163,
            "n": 106
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.461,
          "range_max": 3.464
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
          "comp_num_id": "GLOBcomp_61",
          "name": "1,2-propanediol",
          "formula": "C3H8O2",
          "inchi_key": "DNIAPMSPPWPWGF-UHFFFAOYSA-N",
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
      "parent_n_datapoints": 106,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ]
}

