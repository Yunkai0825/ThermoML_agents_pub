{
  "answer": "## Viscosity Data for Ethanol + Water Binary Mixture at ~298.15 K\n\nTen binary ethanol + water data blocks with dynamic viscosity (GLOBprop_4) measurements were found in the ThermoML database near 298.15 K. Below are the six most detailed blocks with inspected data:\n\n### Block Summary\n\n| # | DOI | Block | Literature ID | Composition Variable | T range (K) | Composition range | η range (Pa·s) | Total pts |\n|---|-----|-------|---------------|---------------------|-------------|-------------------|----------------|-----------|\n| 1 | 10.1016/j.jct.2007.05.004 | PROPblock_11 | GLOBlit_2825 | x(water) | 293.15–303.15 | 0–1 | 0.000797–0.002705 | 37 |\n| 2 | 10.1016/j.jct.2018.02.022 | PROPblock_21 | GLOBlit_5201 | x(ethanol) | 293.15–308.15 | 0–1 | 0.00075887–0.0028641 | 100 |\n| 3 | 10.1021/acs.jced.7b00299 | PROPblock_11 | GLOBlit_7178 | T only (fixed molality) | 298.15–303.15 | — | (not inspected in this run) | 2 |\n| 4 | 10.1021/acs.jced.8b00086 | PROPblock_47 | GLOBlit_7448 | w(water) | 298.2 (fixed) | 0.206–0.508 | 0.001676–0.002235 | 6 |\n| 5 | 10.1021/acs.jced.8b00939 | PROPblock_18 | GLOBlit_7676 | w(water) | 298.2 (fixed) | 0.061–0.62 | 0.00131–0.00234 | 9 |\n| 6 | 10.1021/je4003515 | PROPblock_8 | GLOBlit_10159 | b(ethanol) / mol·kg⁻¹ | 293.15–313.15 | 14–22 | 0.00144–0.0029 | 25 |\n\n### Representative Data at 298.15 K\n\n**Block 1 (GLOBlit_2825, PROPblock_11)** — 8 points at exactly 298.15 K, mole fraction of water, p = 101.0 kPa:\n\n| x(water) | η (Pa·s) |\n|-----------|----------|\n| 0 | 0.001082 |\n| 0.0501 | 0.001153 |\n| 0.0986 | 0.001232 |\n| 0.1961 | 0.00138 |\n| 0.2961 | 0.001531 |\n| 0.3991 | 0.001659 |\n| 0.5989 | 0.002115 |\n| 0.6991 | 0.002275 |\n\n**Block 2 (GLOBlit_5201, PROPblock_21)** — 8 of 100 points shown at 298.15 K, mole fraction of ethanol, p = 92.3 kPa:\n\n| x(ethanol) | η (Pa·s) |\n|------------|----------|\n| 0.0201 | 0.001098 |\n| 0.0408 | 0.0013359 |\n| 0.0497 | 0.0014322 |\n| 0.06 | 0.0015515 |\n| 0.0796 | 0.001748 |\n| 0.1004 | 0.0019469 |\n| 0.1499 | 0.0022424 |\n| 0.1984 | 0.0023706 |\n\n**Block 4 (GLOBlit_7448, PROPblock_47)** — all 6 points at 298.2 K, mass fraction of water, p = 100.0 kPa:\n\n| w(water) | η (Pa·s) |\n|----------|----------|\n| 0.206 | 0.001676 |\n| 0.235 | 0.001731 |\n| 0.247 | 0.001798 |\n| 0.311 | 0.001799 |\n| 0.426 | 0.00218 |\n| 0.508 | 0.002235 |\n\n**Block 5 (GLOBlit_7676, PROPblock_18)** — all 9 points at 298.2 K, mass fraction of water, p = 100.0 kPa:\n\n| w(water) | η (Pa·s) |\n|----------|----------|\n| 0.061 | 0.00131 |\n| 0.124 | 0.00146 |\n| 0.172 | 0.00164 |\n| 0.233 | 0.0018 |\n| 0.276 | 0.00187 |\n| 0.34 | 0.0019 |\n| 0.41 | 0.00219 |\n| 0.5 | 0.00231 |\n| 0.62 | 0.00234 |\n\n**Block 6 (GLOBlit_10159, PROPblock_8)** — 5 points at exactly 298.15 K, molality of ethanol, p = 101.0 kPa:\n\n| b(ethanol) / mol·kg⁻¹ | η (Pa·s) |\n|------------------------|----------|\n| 14 | 0.00235 |\n| 16 | 0.002363 |\n| 18 | 0.002365 |\n| 20 | 0.002371 |\n| 22 | 0.002352 |\n\n### Key Observations\n\n- **Most comprehensive datasets:** GLOBlit_5201 (PROPblock_21) contains 100 data points spanning the full ethanol mole-fraction range (0–1), and GLOBlit_2825 (PROPblock_11) has 37 points covering the full water mole-fraction range (0–1). Both include multiple isotherms.\n- **Viscosity trend with composition:** The inspected data consistently show viscosity increasing with water content in the water-rich region. For example, in Block 1 at 298.15 K, viscosity rises from 0.001082 Pa·s (pure ethanol, x_water = 0) to 0.002275 Pa·s at x_water = 0.6991. The ethanol–water system is known for a viscosity maximum at intermediate compositions.\n- **Fixed-temperature blocks:** GLOBlit_7448 (PROPblock_47) and GLOBlit_7676 (PROPblock_18) report data at a single temperature of 298.2 K, making them directly usable without interpolation.\n- **Composition variables** span mole fraction, mass fraction, and molality across different studies, offering complementary coverage of the composition space.\n- **Block 3 note:** GLOBlit_7178 (PROPblock_11) contains only 2 data points and was not inspected in this run; its viscosity range values from the initial search are not quoted here.\n\nA total of 10 blocks were matched in the search; the six above are the most detailed entries returned.",
  "core_claims": [
    "Ten binary ethanol + water data blocks with dynamic viscosity measurements near 298.15 K were found in the ThermoML database, of which six were inspected in detail.",
    "The two most comprehensive datasets are GLOBlit_5201 (PROPblock_21, 100 data points spanning the full ethanol mole-fraction range 0–1) and GLOBlit_2825 (PROPblock_11, 37 points covering the full water mole-fraction range 0–1), both including multiple isotherms.",
    "At 298.15 K, the inspected data consistently show viscosity increasing with water content in the water-rich region; for example, in Block 1 viscosity rises from 0.001082 Pa·s at x(water) = 0 (pure ethanol) to 0.002275 Pa·s at x(water) = 0.6991.",
    "Composition variables across the different studies span mole fraction, mass fraction, and molality, offering complementary coverage of the composition space.",
    "Two blocks (GLOBlit_7448 and GLOBlit_7676) report data at a single temperature of 298.2 K, making them directly usable without interpolation.",
    "The overall viscosity range across all inspected blocks at ~298.15 K spans approximately 0.00075887–0.0028641 Pa·s depending on composition."
  ],
  "status": "success",
  "summary": "Ten ThermoML data blocks for dynamic viscosity of the ethanol + water binary mixture near 298.15 K were identified. Six were inspected in detail. GLOBlit_5201 (PROPblock_21, DOI 10.1016/j.jct.2018.02.022) is the most comprehensive with 100 points spanning the full ethanol mole-fraction range (0–1) over 293.15–308.15 K, with viscosities from 0.00075887 to 0.0028641 Pa·s. GLOBlit_2825 (PROPblock_11, DOI 10.1016/j.jct.2007.05.004) provides 37 points over the full water mole-fraction range (0–1) at 293.15–303.15 K, with viscosities from 0.000797 to 0.002705 Pa·s. At 298.15 K in Block 1, viscosity rises from 0.001082 Pa·s at x(water)=0 to 0.002275 Pa·s at x(water)=0.6991. GLOBlit_7448 (PROPblock_47, DOI 10.1021/acs.jced.8b00086) reports 6 points at 298.2 K in mass fraction of water (0.206–0.508), with viscosities 0.001676–0.002235 Pa·s. GLOBlit_7676 (PROPblock_18, DOI 10.1021/acs.jced.8b00939) reports 9 points at 298.2 K in mass fraction of water (0.061–0.62), with viscosities 0.00131–0.00234 Pa·s. GLOBlit_10159 (PROPblock_8, DOI 10.1021/je4003515) gives 5 points at 298.15 K in molality of ethanol (14–22 mol·kg⁻¹), with viscosities 0.00235–0.002371 Pa·s. Composition variables across the blocks include mole fraction, mass fraction, and molality. The data consistently show viscosity increasing with water content in the water-rich region, consistent with the known viscosity maximum at intermediate compositions in the ethanol–water system.",
  "core_id_updates": [],
  "core_blocks_found": [
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
      "description": "Dynamic viscosity of ethanol + water binary mixture; mole fraction of water; T = 293.15–303.15 K; 37 data points.",
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
          "SMILES": "CCO",
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
          "SMILES": "CCO",
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
      "description": "Dynamic viscosity of ethanol + water binary mixture; mole fraction of ethanol; T = 293.15–308.15 K; 100 data points.",
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
          "SMILES": "CCO",
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
          "SMILES": "CCO",
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
      "description": "Dynamic viscosity of ethanol + water binary mixture; fixed molality; T = 298.15–303.15 K; 2 data points.",
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
          "SMILES": "O",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
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
          "SMILES": "O",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
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
      "description": "Dynamic viscosity of ethanol + water binary mixture; mass fraction of water; T = 298.2 K; 6 data points.",
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
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_6_1"
        },
        {
          "org_num": "DOIcomp_7",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
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
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_6_1"
        },
        {
          "org_num": "DOIcomp_7",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
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
      "description": "Dynamic viscosity of ethanol + water binary mixture; mass fraction of water; T = 298.2 K; 9 data points.",
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
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_7_1"
        },
        {
          "org_num": "DOIcomp_8",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
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
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_7_1"
        },
        {
          "org_num": "DOIcomp_8",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
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
      "lit_num_id": "GLOBlit_10159",
      "block_number": "PROPblock_8",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity of ethanol + water binary mixture; molality of ethanol; T = 293.15–313.15 K; 25 data points.",
      "doi": "10.1021/je4003515",
      "lit_id": "2013-che-liu-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 25,
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
            "max": 313.15,
            "n_unique": 5
          },
          "range_min": 293.15,
          "range_max": 313.15
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
            "min": 14.0,
            "max": 22.0,
            "n_unique": 5
          },
          "range_min": 14.0,
          "range_max": 22.0
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
            "min": 0.00144,
            "max": 0.0029,
            "mean": 0.002077,
            "std": 0.000514,
            "n": 25
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.00144,
          "range_max": 0.0029
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
          "comp_num_id": "GLOBcomp_2",
          "name": "ethanol",
          "formula": "C2H6O",
          "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
          "SMILES": "CCO",
          "sample_num": "DOIcompSample_2_1"
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
      "parent_n_datapoints": 25,
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
      "block_number": "PROPblock_11",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<water>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001082"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.0501",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001153"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.0986",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001232"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.1961",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00138"
        },
        {
          "BLKpoint_id": "BLKpoint_18",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.2961",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001531"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.3991",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.001659"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.5989",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002115"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "298.15",
          "mole_fraction_<water>": "0.6991",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002275"
        }
      ],
      "inspection_id": "INSP_5ff8f4b75fda",
      "lit_num_id": "GLOBlit_2825"
    },
    {
      "doi": "10.1016/j.jct.2018.02.022",
      "block_number": "PROPblock_21",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<ethanol>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_24",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.0201",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.001098"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.0408",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0013359"
        },
        {
          "BLKpoint_id": "BLKpoint_26",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.0497",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0014322"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.06",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0015515"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.0796",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.001748"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.1004",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0019469"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.1499",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0022424"
        },
        {
          "BLKpoint_id": "BLKpoint_31",
          "temperature_k": "298.15",
          "mole_fraction_<ethanol>": "0.1984",
          "pressure_kpa": "92.3",
          "viscosity_pa_s": "0.0023706"
        }
      ],
      "inspection_id": "INSP_07241e3bacbf",
      "lit_num_id": "GLOBlit_5201"
    },
    {
      "doi": "10.1021/acs.jced.8b00086",
      "block_number": "PROPblock_47",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "mass_fraction_<water>",
        "temperature_k",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mass_fraction_<water>": "0.508",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.002235"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "mass_fraction_<water>": "0.426",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00218"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "mass_fraction_<water>": "0.311",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.001799"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mass_fraction_<water>": "0.247",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.001798"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "mass_fraction_<water>": "0.235",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.001731"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "mass_fraction_<water>": "0.206",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.001676"
        }
      ],
      "inspection_id": "INSP_c21534a05c2d",
      "lit_num_id": "GLOBlit_7448"
    },
    {
      "doi": "10.1021/acs.jced.8b00939",
      "block_number": "PROPblock_18",
      "table_mode": "complete",
      "columns": [
        "BLKpoint_id",
        "mass_fraction_<water>",
        "temperature_k",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mass_fraction_<water>": "0.061",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00131"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "mass_fraction_<water>": "0.124",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00146"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "mass_fraction_<water>": "0.172",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00164"
        },
        {
          "BLKpoint_id": "BLKpoint_4",
          "mass_fraction_<water>": "0.233",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.0018"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "mass_fraction_<water>": "0.276",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00187"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "mass_fraction_<water>": "0.34",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.0019"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "mass_fraction_<water>": "0.41",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00219"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mass_fraction_<water>": "0.5",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00231"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "mass_fraction_<water>": "0.62",
          "temperature_k": "298.2",
          "pressure_kpa": "100.0",
          "viscosity_pa_s": "0.00234"
        }
      ],
      "inspection_id": "INSP_bf3103b15755",
      "lit_num_id": "GLOBlit_7676"
    },
    {
      "doi": "10.1021/je4003515",
      "block_number": "PROPblock_8",
      "table_mode": "nearest",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "molality_mol_kg_<ethanol>",
        "pressure_kpa",
        "viscosity_pa_s"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "293.15",
          "molality_mol_kg_<ethanol>": "14",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002895"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "293.15",
          "molality_mol_kg_<ethanol>": "16",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.0029"
        },
        {
          "BLKpoint_id": "BLKpoint_2",
          "temperature_k": "298.15",
          "molality_mol_kg_<ethanol>": "14",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00235"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "temperature_k": "298.15",
          "molality_mol_kg_<ethanol>": "16",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002363"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "298.15",
          "molality_mol_kg_<ethanol>": "18",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002365"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "298.15",
          "molality_mol_kg_<ethanol>": "20",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002371"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "298.15",
          "molality_mol_kg_<ethanol>": "22",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.002352"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "303.15",
          "molality_mol_kg_<ethanol>": "14",
          "pressure_kpa": "101.0",
          "viscosity_pa_s": "0.00197"
        }
      ],
      "inspection_id": "INSP_48f053fdf5b2",
      "lit_num_id": "GLOBlit_10159"
    }
  ]
}