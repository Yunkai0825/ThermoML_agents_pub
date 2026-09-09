# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_1 | 7732-18-5 | water |
| comp | GLOBcomp_58 | 56-81-5 | glycerol |
| prop | GLOBprop_1 | mass-density | Mass density |
| prop | GLOBprop_4 | dynamic-viscosity | Dynamic viscosity |
| prop | GLOBprop_13 | surface-tension | Surface tension liquid-gas |
| prop | GLOBprop_18 | electrical-conductivity | Electrical conductivity |
| prop | GLOBprop_28 | excess-molar-volume | Excess molar volume |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find dynamic viscosity (GLOBprop_4) data blocks for water+glycerol binary mixture → stored as L1_query_1
- [L1] Find surface tension (GLOBprop_13) data blocks for water+glycerol binary mixture → stored as L1_query_2
- [L1] Find excess molar volume data blocks for water+glycerol binary → stored as L1_query_3
- [L1] Find electrical conductivity data blocks for water+glycerol binary → stored as L1_query_4

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
{
  "answer": "A search for dynamic viscosity (GLOBprop_4) data in binary water (GLOBcomp_1) + glycerol (GLOBcomp_58) mixtures returned **one data block**:\n\n### Block: PROPblock_33\n\n| Field | Details |\n|---|---|\n| **Literature ID** | GLOBlit_5201 |\n| **DOI** | 10.1016/j.jct.2018.02.022 |\n| **Reference key** | 2018-hog-tor-0 |\n| **Property** | Dynamic viscosity (GLOBprop_4), units: Pa·s, liquid phase |\n| **Measurement method** | Concentric cylinders viscometry (GLOBmeas_11) |\n| **Temperature range** | 293.15–303.15 K (variable BLKvar_1 → GLOBvar_1) |\n| **Composition range** | Mole fraction of glycerol: 0.0998–0.9462 (variable BLKvar_2 → GLOBvar_2, component = glycerol) |\n| **Pressure constraint** | 92.3 kPa (BLKconstr_1 → GLOBconstr_1) |\n| **Total data points** | 76 |\n| **Compounds** | DOIcomp_5 → GLOBcomp_58 (glycerol, C₃H₈O₃); DOIcomp_6 → GLOBcomp_1 (water, H₂O) |\n\n**Representative data points** (from 76 total, RDP-compressed to 16):\n\n| T (K) | x(glycerol) | η (Pa·s) | ±U (Pa·s) |\n|---|---|---|---|\n| 293.15 | 0.0998 | 0.003277 | 0.000459 |\n| 293.15 | 0.4477 | 0.063419 | 0.008887 |\n| 293.15 | 0.5471 | 0.12425 | 0.01747 |\n| 293.15 | 0.6469 | 0.23423 | 0.03317 |\n| 293.15 | 0.7942 | 0.6844 | — |\n\n**Chemistry insight:** The data clearly shows the dramatic non-linear increase in viscosity with glycerol content — viscosity rises by roughly two orders of magnitude from x(glycerol) ≈ 0.10 to x(glycerol) ≈ 0.79 at 293.15 K. This reflects the extensive hydrogen-bonding network formed by glycerol's three hydroxyl groups, which increasingly dominates the mixture's flow resistance as glycerol concentration rises. The measurements span a wide composition range (nearly 10 mol% to 95 mol% glycerol) at near-ambient temperatures, making this dataset valuable for modeling viscosity–composition relationships in this industrially important binary system.\n\nNo other data blocks for this compound pair and property were found in the ThermoML database.",
  "core_claims": [
    "The ThermoML database contains one data block (from DOI 10.1016/j.jct.2018.02.022) reporting dynamic viscosity of binary water + glycerol mixtures, measured by concentric cylinders viscometry at 92.3 kPa, spanning 293.15–303.15 K and glycerol mole fractions of 0.0998–0.9462, comprising 76 data points.",
    "The data show a dramatic, non-linear increase in viscosity with increasing glycerol mole fraction—roughly two orders of magnitude from x(glycerol) ≈ 0.10 to ≈ 0.79 at 293.15 K—attributed to the extensive hydrogen-bonding network formed by glycerol's three hydroxyl groups.",
    "No other data blocks for dynamic viscosity of the water + glycerol binary system were found in the ThermoML database."
  ],
  "status": "success",
  "summary": "One ThermoML data block (PROPblock_33, DOI 10.1016/j.jct.2018.02.022, ref 2018-hog-tor-0) reports dynamic viscosity (GLOBprop_4, Pa·s, liquid phase) for binary water (GLOBcomp_1) + glycerol (GLOBcomp_58) mixtures, measured by concentric cylinders viscometry (GLOBmeas_11). The dataset contains 76 points covering 293.15–303.15 K and glycerol mole fractions 0.0998–0.9462 at a constrained pressure of 92.3 kPa. Viscosity increases dramatically and non-linearly with glycerol content, rising roughly two orders of magnitude from x(glycerol) ≈ 0.10 to ≈ 0.79 at 293.15 K, reflecting glycerol's extensive hydrogen-bonding network. No other ThermoML blocks were found for this property and compound pair.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_5201",
      "block_number": "PROPblock_33",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_58",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity measurements for water + glycerol binary mixture from DOI 10.1016/j.jct.2018.02.022. 76 data points spanning 293.15–303.15 K, glycerol mole fraction 0.0998–0.9462, at 92.3 kPa. Measured by concentric cylinders viscometry (GLOBmeas_11).",
      "doi": "10.1016/j.jct.2018.02.022",
      "lit_id": "2018-hog-tor-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 76,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_58",
          "name": "glycerol",
          "formula": "C3H8O3",
          "inchi_key": "PEDCQBHIVMGVHV-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_5_1"
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
            "n_unique": 19
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
            "max": 1.4084,
            "mean": 0.1989,
            "std": 0.280387,
            "n": 76
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000759,
          "range_max": 1.4084
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
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_58",
          "name": "glycerol",
          "formula": "C3H8O3",
          "inchi_key": "PEDCQBHIVMGVHV-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_5_1"
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
      "parent_n_datapoints": 76,
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
  "answer": "A search for surface tension liquid-gas (GLOBprop_13) data in binary water (GLOBcomp_1) + glycerol (GLOBcomp_58) mixtures returned **one data block**:\n\n### Block: PROPblock_1\n\n| Field | Details |\n|---|---|\n| **Literature ID** | GLOBlit_1910 |\n| **DOI** | 10.1016/j.fluid.2016.04.007 |\n| **Reference key** | 2016-kho-hey-0 |\n| **Property** | Surface tension liquid-gas (GLOBprop_13), units: N/m |\n| **Measurement method** | Wilhelmy plate (GLOBmeas_192) |\n| **Temperature range** | 295.15–315.15 K (variable BLKvar_1 → GLOBvar_1) |\n| **Composition range** | Mole fraction of glycerol: 0.02–1.0 (variable BLKvar_2 → GLOBvar_2, component = glycerol) |\n| **Total data points** | 60 |\n| **Compounds** | DOIcomp_1 → GLOBcomp_58 (glycerol, C₃H₈O₃); DOIcomp_7 → GLOBcomp_1 (water, H₂O) |\n\n**Representative data points** (from 60 total, RDP-compressed to 16):\n\n| T (K) | x(glycerol) | γ (N/m) | ±U (N/m) |\n|---|---|---|---|\n| 295.15 | 1.0 | 0.0636 | 0.0003 |\n| 300.15 | 1.0 | 0.0633 | 0.0003 |\n| 305.15 | 1.0 | 0.0629 | 0.0003 |\n| 310.15 | 1.0 | 0.0626 | 0.0003 |\n\n**Chemistry insight:** The dataset covers a broad composition range from dilute glycerol (x = 0.02) to pure glycerol (x = 1.0) at near-ambient temperatures (295–315 K). Pure water has a surface tension of approximately 0.072 N/m at room temperature, while pure glycerol is around 0.063 N/m. The surface tension of the mixture decreases as glycerol content increases, reflecting the lower surface tension of glycerol compared to water. The Wilhelmy plate method is a well-established technique for accurate surface tension measurements. The data span five temperature isotherms across the full composition range, making this dataset useful for modeling surface tension–composition–temperature relationships in this industrially relevant binary system.\n\nNo other data blocks for surface tension of the water + glycerol binary system were found in the ThermoML database.",
  "core_claims": [
    "The ThermoML database contains one data block (from DOI 10.1016/j.fluid.2016.04.007) reporting surface tension (liquid-gas) measurements for the binary water + glycerol system, comprising 60 data points measured by the Wilhelmy plate method over 295.15–315.15 K and glycerol mole fractions from 0.02 to 1.0.",
    "Surface tension of the water + glycerol mixture decreases with increasing glycerol mole fraction, consistent with pure glycerol (~0.063 N/m) having a lower surface tension than pure water (~0.072 N/m) at room temperature.",
    "The dataset spans five temperature isotherms across the full composition range, making it suitable for modeling surface tension as a function of both composition and temperature in this binary system.",
    "No other data blocks for surface tension of the water + glycerol binary system were found in the ThermoML database."
  ],
  "status": "success",
  "summary": "One ThermoML data block (GLOBlit_1910, DOI 10.1016/j.fluid.2016.04.007, ref 2016-kho-hey-0) reports surface tension liquid-gas (GLOBprop_13) for binary water (GLOBcomp_1) + glycerol (GLOBcomp_58) mixtures, measured by the Wilhelmy plate method (GLOBmeas_192). The dataset contains 60 data points spanning temperatures 295.15–315.15 K and glycerol mole fractions 0.02–1.0. Surface tension values range from roughly 0.072 N/m (water-rich) down to about 0.063 N/m (pure glycerol), decreasing with increasing glycerol content. Reported uncertainties are on the order of ±0.0003 N/m. No other ThermoML data blocks were found for surface tension of this binary system.",
  "core_id_updates": [],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_1910",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_58",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension liquid-gas data for water+glycerol binary mixture from DOI 10.1016/j.fluid.2016.04.007. 60 data points spanning T = 295.15–315.15 K and x(glycerol) = 0.02–1.0, measured by Wilhelmy plate method (GLOBmeas_192).",
      "doi": "10.1016/j.fluid.2016.04.007",
      "lit_id": "2016-kho-hey-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 60,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_58",
          "name": "glycerol",
          "formula": "C3H8O3",
          "inchi_key": "PEDCQBHIVMGVHV-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
            "min": 295.15,
            "max": 315.15,
            "n_unique": 5
          },
          "range_min": 295.15,
          "range_max": 315.15
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
            "n_unique": 12
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
          "meas_num_id": "GLOBmeas_192",
          "meas_ID": "wilhelmy_plate_method",
          "method_standard": null,
          "method_custom": "Wilhelmy plate method",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0621,
            "max": 0.0724,
            "mean": 0.068934,
            "std": 0.002252,
            "n": 60
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0621,
          "range_max": 0.0724
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
          "comp_num_id": "GLOBcomp_58",
          "name": "glycerol",
          "formula": "C3H8O3",
          "inchi_key": "PEDCQBHIVMGVHV-UHFFFAOYSA-N",
          "SMILES": null,
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 60,
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
  "answer": "No excess molar volume (GLOBprop_28) data blocks were found in the ThermoML database for the binary water (GLOBcomp_1) + glycerol (GLOBcomp_58) system. Multiple searches were conducted — using search_blocks with both compounds together, with glycerol alone, and using search_system_registry with both system scopes (\"declared\" and \"either\") — all returning zero results.\n\nThe ThermoML database does not contain excess molar volume measurements for the water + glycerol binary mixture. While other properties are available for this system (e.g., dynamic viscosity from DOI 10.1016/j.jct.2018.02.022 and surface tension from DOI 10.1016/j.fluid.2016.04.007, as found in prior queries), excess molar volume data for this particular compound pair is not present in the database.",
  "core_claims": [
    "The ThermoML database does not contain excess molar volume data for the binary water + glycerol system, despite multiple search approaches being attempted.",
    "Other properties for the water + glycerol system (e.g., dynamic viscosity and surface tension) are available in the ThermoML database, but excess molar volume is not among them."
  ],
  "status": "no_results",
  "summary": "No excess molar volume (property GLOBprop_28) data were found in the ThermoML database for the binary water (GLOBcomp_1) + glycerol (GLOBcomp_58) system. Multiple search strategies were employed—combining both compounds, searching glycerol alone, and querying the system registry with both 'declared' and 'either' scopes—all returning zero results. Other properties for this system (e.g., dynamic viscosity, surface tension) do exist in the database, but excess molar volume measurements for water + glycerol are absent.",
  "core_id_updates": [],
  "core_blocks_found": []
}
### L1_query_4
{
  "answer": "No electrical conductivity (GLOBprop_18) data blocks were found in the ThermoML database for the binary water (GLOBcomp_1) + glycerol (GLOBcomp_58) system.\n\nMultiple search strategies were employed:\n\n1. **Direct binary search** — searching for both water and glycerol together with electrical conductivity and system_type=\"binary\" returned zero results.\n\n2. **Glycerol-based broadened search** — searching for all electrical conductivity blocks containing glycerol returned 19 blocks across 10 DOIs, but none are binary water+glycerol systems. The glycerol-containing electrical conductivity data involve other co-compounds such as choline chloride (GLOBcomp_100), various ionic liquids, and deep eutectic solvents. One ternary block (GLOBlit_5300, PROPblock_13, DOI 10.1016/j.jct.2018.07.031) contains glycerol + choline chloride + water, but this is a ternary system, not the requested binary.\n\n3. **Water-based registry search** — searching for all electrical conductivity blocks containing water returned 50 blocks across 16 DOIs, spanning unary, binary, and ternary systems. None of the binary systems pair water with glycerol; they involve compounds such as copper sulfate, cetyltrimethylammonium salicylate, imidazolium-based ionic liquids, and surfactants.\n\n**Conclusion:** The ThermoML database does not contain electrical conductivity measurements for the binary water + glycerol mixture. While glycerol appears in electrical conductivity studies of deep eutectic solvents and ionic liquid mixtures, and water appears in numerous conductivity datasets with salts and surfactants, no study in the database reports conductivity for the simple binary water + glycerol system.",
  "core_claims": [
    "The ThermoML database contains no electrical conductivity data for the binary water + glycerol system.",
    "Electrical conductivity data involving glycerol exist in the database but only for other systems such as deep eutectic solvents and ionic liquid mixtures, not for binary water + glycerol.",
    "Electrical conductivity data involving water exist in the database but only for systems with salts, surfactants, and ionic liquids, not for binary water + glycerol.",
    "A ternary system (glycerol + choline chloride + water) was identified but does not satisfy the binary water + glycerol requirement."
  ],
  "status": "no_results",
  "summary": "The ThermoML database contains no electrical conductivity (GLOBprop_18) data for the binary water (GLOBcomp_1) + glycerol (GLOBcomp_58) system. Multiple search strategies were used: direct binary searches, glycerol-based broadened searches (which returned 19 blocks across 10 DOIs involving other co-compounds such as choline chloride and ionic liquids), and water-based searches (which returned 50 blocks across 16 DOIs involving salts, surfactants, and ionic liquids). One ternary block (GLOBlit_5300, PROPblock_13, DOI 10.1016/j.jct.2018.07.031) contains glycerol + choline chloride + water but is ternary, not binary. No study in the database reports electrical conductivity for the simple binary water + glycerol mixture.",
  "core_id_updates": [],
  "core_blocks_found": []
}

