# Tool History — query-agent

**Nest:** Q
**Session:** 2b90712a
**Detailed log:** run_history_detailed.md — Argo events + verbatim agent outputs (join: session id; step tag `cN` ↔ event-row `cN`)
**Prompt:** I need three binary liquid systems for jointly testing density and viscosity predictions. Which systems have both properties measured for the same mixture, and which papers should I start with?
**Started:** 2026-09-05 05:28:51  |  **Elapsed:** 504.3s  |  **Tool calls:** 10  |  **Nested sections:** 1

---

### Step 1 [Q · c10]: `L1_query`

<details><summary>Arguments</summary>

```json
{
  "purpose": "Find binary liquid mixtures where both mass density and dynamic viscosity are measured in the same dataset/paper",
  "instruction": "Search for binary liquid systems that have BOTH mass density (GLOBprop_1) AND dynamic viscosity (GLOBprop_4) measured. I need systems where both properties appear for the same binary mixture. Return at least 3-5 such systems with their component names, DOIs, literature IDs, and any available data summaries (temperature ranges, composition ranges). Use the property screening/ranking tool if appropriate to find co-measured property pairs.",
  "id_catalog": "",
  "context": "User wants to identify binary liquid systems suitable for jointly testing density and viscosity predictions. Need systems with both properties co-measured."
}
```
</details>

- **Result:** 110,197 chars  |  **Time:** 381.6s  |  **Started:** 05:29:00 (t+8.8s)
- **Nested:** ↳ 9 tool calls in section 'L1_1' below

<details><summary>Result</summary>

```
[TOOL_RESULT_SIZE_WARNING: L1_query returned 109,956 characters after result processing; the target is 24,000. The full result follows — prefer narrower requests, and rely on your working memory for recall instead of re-running this call.]

<subagent_answer>
{
  "answer": "## Binary Liquid Mixtures with Co-Measured Mass Density and Dynamic Viscosity\n\nThree literature sources in the ThermoML database were confirmed to contain **both mass density (GLOBprop_1) and dynamic viscosity (GLOBprop_4)** measured for binary liquid systems. These are suitable candidates for jointly testing density and viscosity predictions.\n\n---\n\n### 1. Alkanes + Squalane — GLOBlit_25\n**DOI:** 10.1007/s10765-006-0053-2\n\nThree binary sub-systems, each with paired density and viscosity blocks at high pressure. The following block-level summaries were returned by the `search_blocks` tool but individual block data tables were not inspected in this run, so exact numerical ranges should be verified by inspecting each block before use:\n\n| System | Viscosity Block | Density Block |\n|--------|----------------|---------------|\n| Butane (GLOBcomp_102) + squalane (GLOBcomp_284) | PROPblock_9 | PROPblock_10 |\n| Hexane (GLOBcomp_12) + squalane (GLOBcomp_284) | PROPblock_11 | PROPblock_12 |\n| Octane (GLOBcomp_17) + squalane (GLOBcomp_284) | PROPblock_13 | PROPblock_14 |\n\n**Note:** The search_blocks result reported these blocks span temperature, pressure, and composition ranges, but the exact values were not verified via `inspect_block_table` in this run. Squalane is a common viscosity reference fluid, making these data useful for equation-of-state and transport-property model validation.\n\n---\n\n### 2. Diisopropyl Ether + Chlorobutane Isomers — GLOBlit_97\n**DOI:** 10.1007/s10765-010-0737-5\n\nFour binary systems with paired density and viscosity blocks. Block-level summaries were returned by `search_blocks` but individual data tables were not inspected in this run:\n\n| System | Viscosity Block | Density Block |\n|--------|----------------|---------------|\n| 1-Chlorobutane (GLOBcomp_131) + diisopropyl ether (GLOBcomp_52) | PROPblock_11 | PROPblock_12 |\n| 2-Chlorobutane (GLOBcomp_307) + diisopropyl ether (GLOBcomp_52) | PROPblock_13 | PROPblock_14 |\n| 1-Chloro-2-methylpropane (GLOBcomp_361) + diisopropyl ether (GLOBcomp_52) | PROPblock_15 | PROPblock_16 |\n| 2-Chloro-2-methylpropane (GLOBcomp_328) + diisopropyl ether (GLOBcomp_52) | PROPblock_17 | PROPblock_18 |\n\n**Chemistry note:** This set of structural isomers (1-chlorobutane, 2-chlorobutane, isobutyl chloride, tert-butyl chloride) with a common second component provides a systematic way to study the effect of branching and chlorine position on both density and viscosity of binary mixtures.\n\n---\n\n### 3. Butan-1-ol + TEGDME — GLOBlit_151\n**DOI:** 10.1007/s10765-013-1469-0\n\nOne binary system with density, viscosity, and refractive index all co-measured. Block-level summaries were returned by `search_blocks` but individual data tables were not inspected in this run:\n\n| Property | Block |\n|----------|-------|\n| Mass density (GLOBprop_1) | PROPblock_7 |\n| Dynamic viscosity (GLOBprop_4) | PROPblock_8 |\n| Refractive index (GLOBprop_7) | PROPblock_9 |\n\n**Compounds:** butan-1-ol (GLOBcomp_7), 2,5,8,11,14-pentaoxapentadecane / TEGDME (GLOBcomp_247).\n\n**Chemistry note:** The alcohol + polyether system exhibits hydrogen-bonding interactions that produce non-ideal mixing behavior in both density and viscosity, making it a stringent test for predictive models. Additionally, having three co-measured properties (density, viscosity, refractive index) in the same dataset adds further value for multi-property model validation.\n\n---\n\n### Summary\n\n| Literature | DOI | # Binary Systems | Key Chemistry |\n|------------|-----|-------------------|---------------|\n| GLOBlit_25 | 10.1007/s10765-006-0053-2 | 3 (alkane + squalane) | Non-polar hydrocarbon mixtures, high-pressure data |\n| GLOBlit_97 | 10.1007/s10765-010-0737-5 | 4 (chlorobutane isomers + diisopropyl ether) | Isomer series, atmospheric pressure |\n| GLOBlit_151 | 10.1007/s10765-013-1469-0 | 1 (butan-1-ol + TEGDME) | H-bonding system, three co-measured properties |\n\nIn total, **8 distinct binary liquid systems** across these three literature sources have both mass density and dynamic viscosity co-measured. The exact temperature, pressure, and composition ranges for each block were reported by the registry search tool but were not independently verified via block-table inspection in this run; users should inspect individual blocks (e.g., `GLOBlit_25::PROPblock_9`) to confirm precise data ranges before use.\n\n**Additional literature sources checked but found to contain only one property:**\n- GLOBlit_8 (ethanol + toluene): viscosity only\n- GLOBlit_59 (ethanol + BMIMBF₄): density only\n- GLOBlit_145 (chlorobutane isomers + ethers): viscosity only\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNINSPECTED_BLOCK** PROPblock_9: PROPblock_9 is quoted with data values (14, …) but was never inspected in this run (values 14 verified against the database — inspection is still mandatory)\n  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number=\"GLOBlit_25::PROPblock_9\")`",
  "core_claims": [
    "Three ThermoML literature sources (GLOBlit_25, GLOBlit_97, GLOBlit_151) were identified as containing both mass density and dynamic viscosity co-measured for binary liquid systems, encompassing 8 distinct binary systems in total.",
    "GLOBlit_25 (DOI 10.1007/s10765-006-0053-2) covers three alkane + squalane binary systems (butane, hexane, octane each paired with squalane) with high-pressure density and viscosity data.",
    "GLOBlit_97 (DOI 10.1007/s10765-010-0737-5) covers four chlorobutane isomer + diisopropyl ether binary systems, providing a systematic series for studying branching and chlorine-position effects on density and viscosity.",
    "GLOBlit_151 (DOI 10.1007/s10765-013-1469-0) covers one butan-1-ol + TEGDME binary system with three co-measured properties: mass density, dynamic viscosity, and refractive index.",
    "Exact temperature, pressure, and composition ranges for the identified data blocks were not independently verified via block-table inspection in this run; the answer flags this as an unresolved limitation requiring further verification before use."
  ],
  "status": "success",
  "summary": "Three ThermoML literature sources were identified as containing both mass density and dynamic viscosity co-measured for binary liquid mixtures, totaling 8 distinct binary systems. GLOBlit_25 (DOI 10.1007/s10765-006-0053-2) covers 3 alkane + squalane systems (butane, hexane, and octane each with squalane) with high-pressure data. GLOBlit_97 (DOI 10.1007/s10765-010-0737-5) covers 4 chlorobutane isomer + diisopropyl ether systems (1-chlorobutane, 2-chlorobutane, 1-chloro-2-methylpropane, and 2-chloro-2-methylpropane each with diisopropyl ether), providing a systematic isomer series. GLOBlit_151 (DOI 10.1007/s10765-013-1469-0) covers 1 system of butan-1-ol + TEGDME (2,5,8,11,14-pentaoxapentadecane) with three co-measured properties (density, viscosity, and refractive index). Exact temperature, pressure, and composition ranges for each data block were not independently verified via block-table inspection and should be confirmed before use.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_102",
      "registry_id": "butane",
      "name": "butane"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_284",
      "registry_id": "2,6,10,15,19,23-hexamethyltetracosane",
      "name": "2,6,10,15,19,23-hexamethyltetracosane"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_12",
      "registry_id": "hexane",
      "name": "hexane"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_17",
      "registry_id": "octane",
      "name": "octane"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_131",
      "registry_id": "1-chlorobutane",
      "name": "1-chlorobutane"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_52",
      "registry_id": "diisopropyl_ether",
      "name": "diisopropyl ether"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_307",
      "registry_id": "2-chlorobutane",
      "name": "2-chlorobutane"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_361",
      "registry_id": "1-chloro-2-methylpropane",
      "name": "1-chloro-2-methylpropane"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_328",
      "registry_id": "2-chloro-2-methylpropane",
      "name": "2-chloro-2-methylpropane"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_7",
      "registry_id": "butan-1-ol",
      "name": "butan-1-ol"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_247",
      "registry_id": "2,5,8,11,14-pentaoxapentadecane",
      "name": "2,5,8,11,14-pentaoxapentadecane"
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
      "core_GLOB_id": "GLOBprop_7",
      "registry_id": "refractive_index_na_dline",
      "name": "Refractive index (Na D-line)"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_25",
      "registry_id": "2006-kum-tom-0",
      "name": "10.1007/s10765-006-0053-2"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_97",
      "registry_id": "2010-mon-gue-0",
      "name": "10.1007/s10765-010-0737-5"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_151",
      "registry_id": "2013-ziv-ser-0",
      "name": "10.1007/s10765-013-1469-0"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_25",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_102",
        "GLOBcomp_284"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity for butane + squalane.",
      "doi": "10.1007/s10765-006-0053-2",
      "lit_id": "2006-kum-tom-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 80,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_102",
          "name": "butane",
          "formula": "C4H10",
          "inchi_key": "IJDNQMDRQITEOD-UHFFFAOYSA-N",
          "SMILES": "CCCC",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_284",
          "name": "2,6,10,15,19,23-hexamethyltetracosane",
          "formula": "C30H62",
          "inchi_key": "PRAKJMSDJKAYCZ-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCCC(C)CCCC(C)CCCCC(C)CCCC(C)CCCC(C)C",
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
            "min": 273.15,
            "max": 333.15,
            "n_unique": 4
          },
          "range_min": 273.15,
          "range_max": 333.15
        },
        {
          "BLKvar_id": "BLKvar_2",
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
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 0.753,
            "n_unique": 7
          },
          "range_min": 0.0,
          "range_max": 0.753
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
            "min": 100.0,
            "max": 30000.0,
            "n_unique": 8
          },
          "range_min": 100.0,
          "range_max": 30000.0
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
            "min": 0.000118,
            "max": 0.0915,
            "mean": 0.008387,
            "std": 0.015628,
            "n": 80
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000118,
          "range_max": 0.0915
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
          "comp_num_id": "GLOBcomp_102",
          "name": "butane",
          "formula": "C4H10",
          "inchi_key": "IJDNQMDRQITEOD-UHFFFAOYSA-N",
          "SMILES": "CCCC",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_284",
          "name": "2,6,10,15,19,23-hexamethyltetracosane",
          "formula": "C30H62",
          "inchi_key": "PRAKJMSDJKAYCZ-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCCC(C)CCCC(C)CCCCC(C)CCCC(C)CCCC(C)C",
          "sample_num": "DOIcompSample_4_1"
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
      "lit_num_id": "GLOBlit_25",
      "block_number": "PROPblock_10",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_102",
        "GLOBcomp_284"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density for butane + squalane.",
      "doi": "10.1007/s10765-006-0053-2",
      "lit_id": "2006-kum-tom-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 80,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_102",
          "name": "butane",
          "formula": "C4H10",
          "inchi_key": "IJDNQMDRQITEOD-UHFFFAOYSA-N",
          "SMILES": "CCCC",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_284",
          "name": "2,6,10,15,19,23-hexamethyltetracosane",
          "formula": "C30H62",
          "inchi_key": "PRAKJMSDJKAYCZ-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCCC(C)CCCC(C)CCCCC(C)CCCC(C)CCCC(C)C",
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
            "min": 273.15,
            "max": 333.15,
            "n_unique": 4
          },
          "range_min": 273.15,
          "range_max": 333.15
        },
        {
          "BLKvar_id": "BLKvar_2",
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
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 0.753,
            "n_unique": 7
          },
          "range_min": 0.0,
          "range_max": 0.753
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
            "min": 100.0,
            "max": 30000.0,
            "n_unique": 8
          },
          "range_min": 100.0,
          "range_max": 30000.0
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
            "min": 529.0,
            "max": 825.0,
            "mean": 723.9125,
            "std": 78.343158,
            "n": 80
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 529.0,
          "range_max": 825.0
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
          "comp_num_id": "GLOBcomp_102",
          "name": "butane",
          "formula": "C4H10",
          "inchi_key": "IJDNQMDRQITEOD-UHFFFAOYSA-N",
          "SMILES": "CCCC",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_284",
          "name": "2,6,10,15,19,23-hexamethyltetracosane",
          "formula": "C30H62",
          "inchi_key": "PRAKJMSDJKAYCZ-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCCC(C)CCCC(C)CCCCC(C)CCCC(C)CCCC(C)C",
          "sample_num": "DOIcompSample_4_1"
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
      "lit_num_id": "GLOBlit_25",
      "block_number": "PROPblock_11",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_12",
        "GLOBcomp_284"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity for hexane + squalane.",
      "doi": "10.1007/s10765-006-0053-2",
      "lit_id": "2006-kum-tom-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 64,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_12",
          "name": "hexane",
          "formula": "C6H14",
          "inchi_key": "VLKZOEOYAKHREP-UHFFFAOYSA-N",
          "SMILES": "CCCCCC",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_284",
          "name": "2,6,10,15,19,23-hexamethyltetracosane",
          "formula": "C30H62",
          "inchi_key": "PRAKJMSDJKAYCZ-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCCC(C)CCCC(C)CCCCC(C)CCCC(C)CCCC(C)C",
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
            "min": 273.15,
            "max": 333.15,
            "n_unique": 4
          },
          "range_min": 273.15,
          "range_max": 333.15
        },
        {
          "BLKvar_id": "BLKvar_2",
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
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 0.743,
            "n_unique": 4
          },
          "range_min": 0.0,
          "range_max": 0.743
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
            "min": 100.0,
            "max": 30000.0,
            "n_unique": 4
          },
          "range_min": 100.0,
          "range_max": 30000.0
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
            "min": 0.000218,
            "max": 0.0971,
            "mean": 0.010363,
            "std": 0.017958,
            "n": 64
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000218,
          "range_max": 0.0971
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
          "comp_num_id": "GLOBcomp_12",
          "name": "hexane",
          "formula": "C6H14",
          "inchi_key": "VLKZOEOYAKHREP-UHFFFAOYSA-N",
          "SMILES": "CCCCCC",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_284",
          "name": "2,6,10,15,19,23-hexamethyltetracosane",
          "formula": "C30H62",
          "inchi_key": "PRAKJMSDJKAYCZ-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCCC(C)CCCC(C)CCCCC(C)CCCC(C)CCCC(C)C",
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "parent_n_datapoints": 64,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_25",
      "block_number": "PROPblock_12",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_12",
        "GLOBcomp_284"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density for hexane + squalane.",
      "doi": "10.1007/s10765-006-0053-2",
      "lit_id": "2006-kum-tom-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 64,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_12",
          "name": "hexane",
          "formula": "C6H14",
          "inchi_key": "VLKZOEOYAKHREP-UHFFFAOYSA-N",
          "SMILES": "CCCCCC",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_284",
          "name": "2,6,10,15,19,23-hexamethyltetracosane",
          "formula": "C30H62",
          "inchi_key": "PRAKJMSDJKAYCZ-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCCC(C)CCCC(C)CCCCC(C)CCCC(C)CCCC(C)C",
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
            "min": 273.15,
            "max": 333.15,
            "n_unique": 4
          },
          "range_min": 273.15,
          "range_max": 333.15
        },
        {
          "BLKvar_id": "BLKvar_2",
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
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 0.743,
            "n_unique": 4
          },
          "range_min": 0.0,
          "range_max": 0.743
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
            "min": 100.0,
            "max": 30000.0,
            "n_unique": 4
          },
          "range_min": 100.0,
          "range_max": 30000.0
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
            "min": 623.0,
            "max": 824.0,
            "mean": 744.203125,
            "std": 54.586521,
            "n": 64
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 623.0,
          "range_max": 824.0
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
          "comp_num_id": "GLOBcomp_12",
          "name": "hexane",
          "formula": "C6H14",
          "inchi_key": "VLKZOEOYAKHREP-UHFFFAOYSA-N",
          "SMILES": "CCCCCC",
          "sample_num": "DOIcompSample_2_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_284",
          "name": "2,6,10,15,19,23-hexamethyltetracosane",
          "formula": "C30H62",
          "inchi_key": "PRAKJMSDJKAYCZ-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCCC(C)CCCC(C)CCCCC(C)CCCC(C)CCCC(C)C",
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "parent_n_datapoints": 64,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_25",
      "block_number": "PROPblock_13",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_284",
        "GLOBcomp_17"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity for octane + squalane.",
      "doi": "10.1007/s10765-006-0053-2",
      "lit_id": "2006-kum-tom-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 80,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_284",
          "name": "2,6,10,15,19,23-hexamethyltetracosane",
          "formula": "C30H62",
          "inchi_key": "PRAKJMSDJKAYCZ-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCCC(C)CCCC(C)CCCCC(C)CCCC(C)CCCC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_17",
          "name": "octane",
          "formula": "C8H18",
          "inchi_key": "TVMXDCGIABBOFY-UHFFFAOYSA-N",
          "SMILES": "CCCCCCCC",
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
            "min": 273.15,
            "max": 333.15,
            "n_unique": 4
          },
          "range_min": 273.15,
          "range_max": 333.15
        },
        {
          "BLKvar_id": "BLKvar_2",
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
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 6
          },
          "range_min": 0.0,
          "range_max": 1.0
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
            "min": 100.0,
            "max": 30000.0,
            "n_unique": 4
          },
          "range_min": 100.0,
          "range_max": 30000.0
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
            "min": 0.000351,
            "max": 0.2614,
            "mean": 0.021392,
            "std": 0.042825,
            "n": 80
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000351,
          "range_max": 0.2614
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_284",
          "name": "2,6,10,15,19,23-hexamethyltetracosane",
          "formula": "C30H62",
          "inchi_key": "PRAKJMSDJKAYCZ-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCCC(C)CCCC(C)CCCCC(C)CCCC(C)CCCC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_17",
          "name": "octane",
          "formula": "C8H18",
          "inchi_key": "TVMXDCGIABBOFY-UHFFFAOYSA-N",
          "SMILES": "CCCCCCCC",
          "sample_num": "DOIcompSample_3_1"
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
      "lit_num_id": "GLOBlit_25",
      "block_number": "PROPblock_14",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_284",
        "GLOBcomp_17"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density for octane + squalane.",
      "doi": "10.1007/s10765-006-0053-2",
      "lit_id": "2006-kum-tom-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 80,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_284",
          "name": "2,6,10,15,19,23-hexamethyltetracosane",
          "formula": "C30H62",
          "inchi_key": "PRAKJMSDJKAYCZ-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCCC(C)CCCC(C)CCCCC(C)CCCC(C)CCCC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_17",
          "name": "octane",
          "formula": "C8H18",
          "inchi_key": "TVMXDCGIABBOFY-UHFFFAOYSA-N",
          "SMILES": "CCCCCCCC",
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
            "min": 273.15,
            "max": 333.15,
            "n_unique": 4
          },
          "range_min": 273.15,
          "range_max": 333.15
        },
        {
          "BLKvar_id": "BLKvar_2",
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
            "BLKvar_id": "BLKvar_2",
            "name": "Mole fraction",
            "min": 0.0,
            "max": 1.0,
            "n_unique": 6
          },
          "range_min": 0.0,
          "range_max": 1.0
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
            "min": 100.0,
            "max": 30000.0,
            "n_unique": 4
          },
          "range_min": 100.0,
          "range_max": 30000.0
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
            "min": 670.0,
            "max": 835.0,
            "mean": 772.7,
            "std": 40.554823,
            "n": 80
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 670.0,
          "range_max": 835.0
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_284",
          "name": "2,6,10,15,19,23-hexamethyltetracosane",
          "formula": "C30H62",
          "inchi_key": "PRAKJMSDJKAYCZ-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCCC(C)CCCC(C)CCCCC(C)CCCC(C)CCCC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_17",
          "name": "octane",
          "formula": "C8H18",
          "inchi_key": "TVMXDCGIABBOFY-UHFFFAOYSA-N",
          "SMILES": "CCCCCCCC",
          "sample_num": "DOIcompSample_3_1"
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
      "lit_num_id": "GLOBlit_97",
      "block_number": "PROPblock_11",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_52",
        "GLOBcomp_131"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity for 1-chlorobutane + diisopropyl ether.",
      "doi": "10.1007/s10765-010-0737-5",
      "lit_id": "2010-mon-gue-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 91,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_131",
          "name": "1-chlorobutane",
          "formula": "C4H9Cl",
          "inchi_key": "VFWCMGCRMGJXDK-UHFFFAOYSA-N",
          "SMILES": "CCCCCl",
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
          "meas_num_id": "GLOBmeas_4",
          "meas_ID": "capillary_tube_ostwald_ubbelohde_method",
          "method_standard": "Capillary tube (Ostwald; Ubbelohde) method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000272,
            "max": 0.000499,
            "mean": 0.000372,
            "std": 5.3e-05,
            "n": 91
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000272,
          "range_max": 0.000499
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_131",
          "name": "1-chlorobutane",
          "formula": "C4H9Cl",
          "inchi_key": "VFWCMGCRMGJXDK-UHFFFAOYSA-N",
          "SMILES": "CCCCCl",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 91,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_97",
      "block_number": "PROPblock_12",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_52",
        "GLOBcomp_131"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density for 1-chlorobutane + diisopropyl ether.",
      "doi": "10.1007/s10765-010-0737-5",
      "lit_id": "2010-mon-gue-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 91,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_131",
          "name": "1-chlorobutane",
          "formula": "C4H9Cl",
          "inchi_key": "VFWCMGCRMGJXDK-UHFFFAOYSA-N",
          "SMILES": "CCCCCl",
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
          "meas_num_id": "GLOBmeas_143",
          "meas_ID": "vibtub_ufactor_6",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:6",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 702.378,
            "max": 897.339,
            "mean": 795.892066,
            "std": 57.042358,
            "n": 91
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 702.378,
          "range_max": 897.339
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_131",
          "name": "1-chlorobutane",
          "formula": "C4H9Cl",
          "inchi_key": "VFWCMGCRMGJXDK-UHFFFAOYSA-N",
          "SMILES": "CCCCCl",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 91,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_97",
      "block_number": "PROPblock_13",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_307",
        "GLOBcomp_52"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity for 2-chlorobutane + diisopropyl ether.",
      "doi": "10.1007/s10765-010-0737-5",
      "lit_id": "2010-mon-gue-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 91,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_307",
          "name": "2-chlorobutane",
          "formula": "C4H9Cl",
          "inchi_key": "BSPCSKHALVHRSR-UHFFFAOYSA-N",
          "SMILES": "CCC(C)Cl",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
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
          "meas_num_id": "GLOBmeas_4",
          "meas_ID": "capillary_tube_ostwald_ubbelohde_method",
          "method_standard": "Capillary tube (Ostwald; Ubbelohde) method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000272,
            "max": 0.000463,
            "mean": 0.000357,
            "std": 4.5e-05,
            "n": 91
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000272,
          "range_max": 0.000463
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
          "comp_num_id": "GLOBcomp_307",
          "name": "2-chlorobutane",
          "formula": "C4H9Cl",
          "inchi_key": "BSPCSKHALVHRSR-UHFFFAOYSA-N",
          "SMILES": "CCC(C)Cl",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "parent_n_datapoints": 91,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_97",
      "block_number": "PROPblock_14",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_307",
        "GLOBcomp_52"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density for 2-chlorobutane + diisopropyl ether.",
      "doi": "10.1007/s10765-010-0737-5",
      "lit_id": "2010-mon-gue-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 90,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_307",
          "name": "2-chlorobutane",
          "formula": "C4H9Cl",
          "inchi_key": "BSPCSKHALVHRSR-UHFFFAOYSA-N",
          "SMILES": "CCC(C)Cl",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
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
          "meas_num_id": "GLOBmeas_143",
          "meas_ID": "vibtub_ufactor_6",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:6",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 702.378,
            "max": 884.34,
            "mean": 789.576322,
            "std": 52.546939,
            "n": 90
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 702.378,
          "range_max": 884.34
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
          "comp_num_id": "GLOBcomp_307",
          "name": "2-chlorobutane",
          "formula": "C4H9Cl",
          "inchi_key": "BSPCSKHALVHRSR-UHFFFAOYSA-N",
          "SMILES": "CCC(C)Cl",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "parent_n_datapoints": 90,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_97",
      "block_number": "PROPblock_15",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_52",
        "GLOBcomp_361"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity for 1-chloro-2-methylpropane + diisopropyl ether.",
      "doi": "10.1007/s10765-010-0737-5",
      "lit_id": "2010-mon-gue-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 91,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_361",
          "name": "1-chloro-2-methylpropane",
          "formula": "C4H9Cl",
          "inchi_key": "QTBFPMKWQKYFLR-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCl",
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
          "meas_num_id": "GLOBmeas_4",
          "meas_ID": "capillary_tube_ostwald_ubbelohde_method",
          "method_standard": "Capillary tube (Ostwald; Ubbelohde) method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000272,
            "max": 0.000516,
            "mean": 0.000371,
            "std": 5.6e-05,
            "n": 91
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000272,
          "range_max": 0.000516
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_361",
          "name": "1-chloro-2-methylpropane",
          "formula": "C4H9Cl",
          "inchi_key": "QTBFPMKWQKYFLR-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCl",
          "sample_num": "DOIcompSample_5_1"
        }
      ],
      "parent_n_datapoints": 91,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_97",
      "block_number": "PROPblock_16",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_52",
        "GLOBcomp_361"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density for 1-chloro-2-methylpropane + diisopropyl ether.",
      "doi": "10.1007/s10765-010-0737-5",
      "lit_id": "2010-mon-gue-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 91,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_361",
          "name": "1-chloro-2-methylpropane",
          "formula": "C4H9Cl",
          "inchi_key": "QTBFPMKWQKYFLR-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCl",
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
          "meas_num_id": "GLOBmeas_143",
          "meas_ID": "vibtub_ufactor_6",
          "method_standard": null,
          "method_custom": "VIBTUB:UFactor:6",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Mass density, kg/m3",
            "min": 702.378,
            "max": 888.845,
            "mean": 790.074154,
            "std": 54.121303,
            "n": 91
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 702.378,
          "range_max": 888.845
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_5",
          "comp_num_id": "GLOBcomp_361",
          "name": "1-chloro-2-methylpropane",
          "formula": "C4H9Cl",
          "inchi_key": "QTBFPMKWQKYFLR-UHFFFAOYSA-N",
          "SMILES": "CC(C)CCl",
          "sample_num": "DOIcompSample_5_1"
        }
      ],
      "parent_n_datapoints": 91,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_97",
      "block_number": "PROPblock_17",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_52",
        "GLOBcomp_328"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity for 2-chloro-2-methylpropane + diisopropyl ether.",
      "doi": "10.1007/s10765-010-0737-5",
      "lit_id": "2010-mon-gue-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 91,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_328",
          "name": "2-chloro-2-methylpropane",
          "formula": "C4H9Cl",
          "inchi_key": "NBRKLOOSMBRFMH-UHFFFAOYSA-N",
          "SMILES": "CC(C)(C)Cl",
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
          "meas_num_id": "GLOBmeas_4",
          "meas_ID": "capillary_tube_ostwald_ubbelohde_method",
          "method_standard": "Capillary tube (Ostwald; Ubbelohde) method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.000272,
            "max": 0.000598,
            "mean": 0.000386,
            "std": 7.4e-05,
            "n": 91
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.000272,
          "range_max": 0.000598
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_328",
          "name": "2-chloro-2-methylpropane",
          "formula": "C4H9Cl",
          "inchi_key": "NBRKLOOSMBRFMH-UHFFFAOYSA-N",
          "SMILES": "CC(C)(C)Cl",
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "parent_n_datapoints": 91,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_97",
      "block_number": "PROPblock_18",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_52",
        "GLOBcomp_328"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density for 2-chloro-2-methylpropane + diisopropyl ether.",
      "doi": "10.1007/s10765-010-0737-5",
      "lit_id": "2010-mon-gue-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 91,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_328",
          "name": "2-chloro-2-methylpropane",
          "formula": "C4H9Cl",
          "inchi_key": "NBRKLOOSMBRFMH-UHFFFAOYSA-N",
          "SMILES": "CC(C)(C)Cl",
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
            "min": 702.378,
            "max": 855.249,
            "mean": 774.86622,
            "std": 42.423528,
            "n": 91
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 702.378,
          "range_max": 855.249
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_52",
          "name": "diisopropyl ether",
          "formula": "C6H14O",
          "inchi_key": "ZAFNJMIOTHYJRJ-UHFFFAOYSA-N",
          "SMILES": "CC(C)OC(C)C",
          "sample_num": "DOIcompSample_4_1"
        },
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_328",
          "name": "2-chloro-2-methylpropane",
          "formula": "C4H9Cl",
          "inchi_key": "NBRKLOOSMBRFMH-UHFFFAOYSA-N",
          "SMILES": "CC(C)(C)Cl",
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "parent_n_datapoints": 91,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_151",
      "block_number": "PROPblock_7",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_7",
        "GLOBcomp_247"
      ],
      "prop_num_ids": [
        "GLOBprop_1"
      ],
      "description": "Mass density for butan-1-ol + TEGDME.",
      "doi": "10.1007/s10765-013-1469-0",
      "lit_id": "2013-ziv-ser-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 110,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_7",
          "name": "butan-1-ol",
          "formula": "C4H10O",
          "inchi_key": "LRHPLDYGYMQRHN-UHFFFAOYSA-N",
          "SMILES": "CCCCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_247",
          "name": "2,5,8,11,14-pentaoxapentadecane",
          "formula": "C10H22O5",
          "inchi_key": "ZUHZGEOKBKGPSW-UHFFFAOYSA-N",
          "SMILES": "COCCOCCOCCOCCOC",
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
            "min": 288.15,
            "max": 333.15,
            "n_unique": 10
          },
          "range_min": 288.15,
          "range_max": 333.15
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
            "n_unique": 11
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
            "min": 778.056,
            "max": 1015.63,
            "mean": 920.3125,
            "std": 62.540965,
            "n": 110
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 778.056,
          "range_max": 1015.63
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
          "comp_num_id": "GLOBcomp_7",
          "name": "butan-1-ol",
          "formula": "C4H10O",
          "inchi_key": "LRHPLDYGYMQRHN-UHFFFAOYSA-N",
          "SMILES": "CCCCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_247",
          "name": "2,5,8,11,14-pentaoxapentadecane",
          "formula": "C10H22O5",
          "inchi_key": "ZUHZGEOKBKGPSW-UHFFFAOYSA-N",
          "SMILES": "COCCOCCOCCOCCOC",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 110,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_151",
      "block_number": "PROPblock_8",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_7",
        "GLOBcomp_247"
      ],
      "prop_num_ids": [
        "GLOBprop_4"
      ],
      "description": "Dynamic viscosity for butan-1-ol + TEGDME.",
      "doi": "10.1007/s10765-013-1469-0",
      "lit_id": "2013-ziv-ser-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 110,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_7",
          "name": "butan-1-ol",
          "formula": "C4H10O",
          "inchi_key": "LRHPLDYGYMQRHN-UHFFFAOYSA-N",
          "SMILES": "CCCCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_247",
          "name": "2,5,8,11,14-pentaoxapentadecane",
          "formula": "C10H22O5",
          "inchi_key": "ZUHZGEOKBKGPSW-UHFFFAOYSA-N",
          "SMILES": "COCCOCCOCCOCCOC",
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
            "min": 288.15,
            "max": 333.15,
            "n_unique": 10
          },
          "range_min": 288.15,
          "range_max": 333.15
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
          "meas_num_id": "GLOBmeas_11",
          "meas_ID": "concentric_cylinders_viscometry",
          "method_standard": "Concentric cylinders viscometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Viscosity, Pa*s",
            "min": 0.001104,
            "max": 0.004341,
            "mean": 0.002137,
            "std": 0.000723,
            "n": 110
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.001104,
          "range_max": 0.004341
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
          "comp_num_id": "GLOBcomp_7",
          "name": "butan-1-ol",
          "formula": "C4H10O",
          "inchi_key": "LRHPLDYGYMQRHN-UHFFFAOYSA-N",
          "SMILES": "CCCCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_247",
          "name": "2,5,8,11,14-pentaoxapentadecane",
          "formula": "C10H22O5",
          "inchi_key": "ZUHZGEOKBKGPSW-UHFFFAOYSA-N",
          "SMILES": "COCCOCCOCCOCCOC",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 110,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_151",
      "block_number": "PROPblock_9",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_7",
        "GLOBcomp_247"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index for butan-1-ol + TEGDME.",
      "doi": "10.1007/s10765-013-1469-0",
      "lit_id": "2013-ziv-ser-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 110,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_7",
          "name": "butan-1-ol",
          "formula": "C4H10O",
          "inchi_key": "LRHPLDYGYMQRHN-UHFFFAOYSA-N",
          "SMILES": "CCCCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_247",
          "name": "2,5,8,11,14-pentaoxapentadecane",
          "formula": "C10H22O5",
          "inchi_key": "ZUHZGEOKBKGPSW-UHFFFAOYSA-N",
          "SMILES": "COCCOCCOCCOCCOC",
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
            "min": 288.15,
            "max": 333.15,
            "n_unique": 10
          },
          "range_min": 288.15,
          "range_max": 333.15
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
            "n_unique": 11
          },
          "range_min": 0.0,
          "range_max": 1.0
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_7",
          "prop_ID": "refractive_index_na_dline",
          "name": "Refractive index (Na D-line)",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_3",
          "meas_ID": "standard_abbe_refractometry",
          "method_standard": "Standard Abbe refractometry",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.38237,
            "max": 1.4345,
            "mean": 1.412611,
            "std": 0.011827,
            "n": 110
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.38237,
          "range_max": 1.4345
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
          "comp_num_id": "GLOBcomp_7",
          "name": "butan-1-ol",
          "formula": "C4H10O",
          "inchi_key": "LRHPLDYGYMQRHN-UHFFFAOYSA-N",
          "SMILES": "CCCCO",
          "sample_num": "DOIcompSample_1_1"
        },
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_247",
          "name": "2,5,8,11,14-pentaoxapentadecane",
          "formula": "C10H22O5",
          "inchi_key": "ZUHZGEOKBKGPSW-UHFFFAOYSA-N",
          "SMILES": "COCCOCCOCCOCCOC",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 110,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": []
}
</subagent_answer>
```
</details>

---

## Nested tool calls — L1_1 (L1-query)

**Nest:** Q - L1_1
**Parent:** `L1_query` — Step 1 [Q · c10] relays this worker's result
**Started:** 05:29:00  |  **Ended:** 05:35:21  |  **Tool calls:** 9

---

### Step 1 [Q - L1_1 · c1]: `search_system_registry`

<details><summary>Arguments</summary>

```json
{
  "property": "GLOBprop_1",
  "system_type": "binary",
  "system_scope": "declared",
  "limit": 100,
  "purpose": "Find binary systems with mass density data",
  "tasks": "List binary systems with GLOBprop_1 (mass density) measurements"
}
```
</details>

- **Result:** 709 chars  |  **Time:** 19.3s  |  **Started:** 05:29:15 (t+23.4s)
- **Subagent:** KEEP in 16,871 → 683 chars (18.1s)
  - **Summary:** 100 binary systems with GLOBprop_1 (mass density) measurements were found across ~30 DOIs, covering a wide variety of compound classes (hydrocarbons, alcohols, halogenated compounds, ioni

<details><summary>Result</summary>

```
**Summary:** 100 binary systems with GLOBprop_1 (mass density) measurements were found across ~30 DOIs, covering a wide variety of compound classes (hydrocarbons, alcohols, halogenated compounds, ionic liquids, aqueous systems, refrigerants). Data point counts range from 4 to 277 per block. **Triage mode applied** — 100 entries returned; shortlisting the 10 largest datasets.

### Top 10 by data points

| # | DOI | Block | Compounds | Points |
|---|-----|-------|-----------|--------|
| 1 | 10.1007/s10765-005-8590-7 [GLOBlit_14] | PROPblock_2 | ammonia, water | 277 |
| 2 | 10.1007/s10765-008-0410-4 [GLOBlit_59] | PROPblock_2 | ethanol, 1-butyl-3-methylimidazolium tetrafluoroborate | 270 |
| 3 | 10.1007
```
</details>

---

### Step 2 [Q - L1_1 · c2]: `search_system_registry`

<details><summary>Arguments</summary>

```json
{
  "property": "GLOBprop_4",
  "system_type": "binary",
  "system_scope": "declared",
  "limit": 100,
  "purpose": "Find binary systems with dynamic viscosity measurements",
  "tasks": "Search for GLOBprop_4 in binary declared systems to cross-reference with density results"
}
```
</details>

- **Result:** 1,400 chars  |  **Time:** 20.0s  |  **Started:** 05:29:39 (t+47.7s)
- **Subagent:** KEEP in 16,634 → 1,282 chars (16.7s)
  - **Summary:** 100 binary declared systems with GLOBprop_4 (dynamic viscosity) data were found, spanning diverse organic, aqueous-electrolyte, and refrigerant mixtures. These can be cross-referenced wit

<details><summary>Result</summary>

```
**Summary:** 100 binary declared systems with GLOBprop_4 (dynamic viscosity) data were found, spanning diverse organic, aqueous-electrolyte, and refrigerant mixtures. These can be cross-referenced with density (GLOBprop_3) results to identify DOIs reporting both properties.

**Triage: 100 blocks returned — presenting key statistics and representative high-point entries for cross-referencing.**

| # | DOI | Block | Compounds | Points |
|---|-----|-------|-----------|--------|
| 7 | 10.1007/s10765-006-0051-4 [GLOBlit_23] | PROPblock_1 | propane, pentafluoroethane | 246 |
| 27 | 10.1007/s10765-009-0579-1 [GLOBlit_76] | PROPblock_1 | chlorodifluoromethane, 1-chloro-1,1-difluoroethane | 237 |
| 6 | 10.1007/s10765-005-8089-2 [GLOBlit_8] | PROPblock_3 | ethanol, toluene | 185 |
| 1 | 10.1007/s10765-005-5567-5 [GLOBlit_2] | PROPblock_4 | water, potassium sulfate | 172 |
| 91 | 10.1007/s10765-013-1469-0 [GLOBlit_151] | PROPblock_8 | butan-1-ol, 2,5,8,11,14-pentaoxapentadecane | 110 |
| 45–48 | 10.1007/s10765-010-0737-5 [GLOBlit_97] | PROPblock_11/13/15/17 | diisopropyl ether + chlorobutane isomers | 91 each |
| 85–90 | 10.1007/s10765-012-1371-1 [GLOBlit_145] | PROPblock_6–11 | chlorobutane isomers + ethers | 91 each |
| 9 | 10.1007/s10765-006-0053-2 [GLOBlit_25] | PROPblock_13 | squalane, octane | 80 |
| 100 | 10.1007/s10765-016-2089-2 [GLOBlit_178] | PROPblock_2 | copper sulfate, water
```
</details>

---

### Step 4 [Q - L1_1 · c3]: `block_search_adv`

<details><summary>Arguments</summary>

```json
{
  "targets": [
    "GLOBprop_1 AS density",
    "GLOBprop_4 AS viscosity"
  ],
  "explanation": "Find binary liquid systems where both mass density and dynamic viscosity are co-measured in the same data block",
  "system_type": "binary",
  "system_scope": "declared",
  "select": [
    "COUNT(density) AS n_density",
    "COUNT(viscosity) AS n_viscosity",
    "MIN(density) AS min_density",
    "MAX(density) AS max_density"
  ],
  "order_by": [
    "n_density DESC"
  ],
  "limit": 20,
  "purpose": "Find binary systems with co-measured density and viscosity",
  "tasks": "Identify binary liquid mixtures where both mass density and dynamic viscosity appear in the same block"
}
```
</details>

- **Result:** 929 chars  |  **Time:** 12.9s  |  **Started:** 05:30:42 (t+111.2s)
- **Subagent:** DISCARD in 844 → 929 chars (10.9s)
  - 1. **Explanation:** The search returned zero results — no blocks in the registry contain both mass density and dynamic viscosity co-measured in the same data block for a binary liquid mixture. The dia

<details><summary>Result</summary>

```
**⚠ Tool `block_search_adv` result discarded by subagent.**

1. **Explanation:** The search returned zero results — no blocks in the registry contain both mass density and dynamic viscosity co-measured in the same data block for a binary liquid mixture. The diagnostic `registry_candidates=0` confirms that the filtering failed at the very first stage, before any binding or observation checks.

2. **Refinement suggestion:** Try searching for each property separately (mass density alone, then dynamic viscosity alone) to identify DOIs or systems that report at least one of them. Then cross-reference the resulting DOIs to find overlapping systems where both properties are available (possibly in different blocks within the same DOI). Alternatively, use a DOI-level or component-level search rather than requiring both properties in a single block, as many datasets report density and viscosity in separate measurement blocks.
```
</details>

---

### Step 5 [Q - L1_1 · c4]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "literature": "GLOBlit_8",
  "system_type": "binary",
  "limit": 20,
  "purpose": "Check if GLOBlit_8 (ethanol+toluene) has both density and viscosity blocks",
  "tasks": "List all property blocks in this literature source"
}
```
</details>

- **Result:** 623 chars  |  **Time:** 9.2s  |  **Started:** 05:31:09 (t+138.1s)
- **Subagent:** KEEP in 2,388 → 611 chars (9.1s)
  - **Summary:** GLOBlit_8 contains **only viscosity** data — no density block was found. The single block (PROPblock_3) provides high-pressure viscosity measurements for ethanol + toluene.

| Block | Pro

<details><summary>Result</summary>

```
**Summary:** GLOBlit_8 contains **only viscosity** data — no density block was found. The single block (PROPblock_3) provides high-pressure viscosity measurements for ethanol + toluene.

| Block | Property | GLOBprop | Points | T range (K) | P range (kPa) | x(ethanol) range |
|---|---|---|---|---|---|---|
| PROPblock_3 | Viscosity, Pa·s | GLOBprop_4 | 185 | 293.15–353.15 | 100.0–100000.0 | 0.125–0.375 |

**Key details:**
- **DOI:** 10.1007/s10765-005-8089-2 [GLOBlit_8]
- **Compounds:** DOIcomp_1 = GLOBcomp_8 (toluene), DOIcomp_2 = GLOBcomp_2 (ethanol)
- **No density property block exists in this literature source.**
```
</details>

---

### Step 7 [Q - L1_1 · c5]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "literature": "GLOBlit_97",
  "system_type": "binary",
  "limit": 20,
  "purpose": "Check if GLOBlit_97 has both density and viscosity blocks",
  "tasks": "List all property blocks for this DOI"
}
```
</details>

- **Result:** 1,092 chars  |  **Time:** 11.5s  |  **Started:** 05:31:33 (t+161.4s)
- **Subagent:** KEEP in 5,434 → 1,092 chars (11.0s)
  - **GLOBlit_97** (DOI `10.1007/s10765-010-0737-5`) contains **both density and viscosity** across 8 property blocks — 4 viscosity (GLOBprop_4) and 4 density (GLOBprop_1) — for 4 binary systems, all in t

<details><summary>Result</summary>

```
**GLOBlit_97** (DOI `10.1007/s10765-010-0737-5`) contains **both density and viscosity** across 8 property blocks — 4 viscosity (GLOBprop_4) and 4 density (GLOBprop_1) — for 4 binary systems, all in the liquid phase at T = 283.15–298.15 K.

| Block | Property | Compounds | Pts | Range |
|---|---|---|---|---|
| PROPblock_11 | Viscosity (GLOBprop_4) | GLOBcomp_131 + GLOBcomp_52 | 12 | η: 0.0003178–0.0004993 Pa·s |
| PROPblock_12 | Density (GLOBprop_1) | GLOBcomp_131 + GLOBcomp_52 | 12 | ρ: 718.289–897.339 kg/m³ |
| PROPblock_13 | Viscosity (GLOBprop_4) | GLOBcomp_307 + GLOBcomp_52 | 12 | η: 0.0003178–0.0004631 Pa·s |
| PROPblock_14 | Density (GLOBprop_1) | GLOBcomp_307 + GLOBcomp_52 | 12 | ρ: 718.289–884.34 kg/m³ |
| PROPblock_15 | Viscosity (GLOBprop_4) | GLOBcomp_52 + GLOBcomp_361 | 13 | η: 0.0003178–0.0005155 Pa·s |
| PROPblock_16 | Density (GLOBprop_1) | GLOBcomp_52 + GLOBcomp_361 | 12 | ρ: 718.289–888.845 kg/m³ |
| PROPblock_17 | Viscosity (GLOBprop_4) | GLOBcomp_328 + GLOBcomp_52 | 19 | η: 0.0003178–0.000598 Pa·s |
| PROPblock_18 | Density (GLOBprop_1) | GLOBcomp_328 + GL
```
</details>

---

### Step 8 [Q - L1_1 · c6]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "literature": "GLOBlit_145",
  "system_type": "binary",
  "limit": 20,
  "purpose": "Check if GLOBlit_145 has both density and viscosity blocks",
  "tasks": "List all property blocks in this literature source"
}
```
</details>

- **Result:** 1,189 chars  |  **Time:** 11.7s  |  **Started:** 05:31:52 (t+180.2s)
- **Subagent:** KEEP in 8,821 → 1,189 chars (11.5s)
  - **GLOBlit_145 contains only viscosity data — no density blocks were found.** All 6 binary property blocks report `viscosity_pa_s` (GLOBprop_4) in the liquid phase. The DOI is `10.1007/s10765-012-1371-

<details><summary>Result</summary>

```
**GLOBlit_145 contains only viscosity data — no density blocks were found.** All 6 binary property blocks report `viscosity_pa_s` (GLOBprop_4) in the liquid phase. The DOI is `10.1007/s10765-012-1371-1`.

| Block | Property | System (comp1 + comp2) | T range (K) | Points |
|---|---|---|---|---|
| PROPblock_6 | viscosity_pa_s | GLOBcomp_131 (1-chlorobutane) + GLOBcomp_803 (butyl ethyl ether) | 283.15–298.15 | 91 |
| PROPblock_7 | viscosity_pa_s | GLOBcomp_307 (2-chlorobutane) + GLOBcomp_803 (butyl ethyl ether) | 283.15–298.15 | 91 |
| PROPblock_8 | viscosity_pa_s | GLOBcomp_361 (1-chloro-2-methylpropane) + GLOBcomp_803 (butyl ethyl ether) | 283.15–298.15 | 91 |
| PROPblock_9 | viscosity_pa_s | GLOBcomp_131 (1-chlorobutane) + GLOBcomp_48 (2-methoxy-2-methylpropane) | 283.15–298.15 | 91 |
| PROPblock_10 | viscosity_pa_s | GLOBcomp_307 (2-chlorobutane) + GLOBcomp_48 (2-methoxy-2-methylpropane) | 283.15–298.15 | 91 |
| PROPblock_11 | viscosity_pa_s | GLOBcomp_361 (1-chloro-2-methylpropane) + GLOBcomp_48 (2-methoxy-2-methylpropane) | 283.15–298.15 | 91 |

All blocks at P = 101.0 kPa, liquid phase. **No density property blocks exist in GLOBlit_145** for binary declared systems.
```
</details>

---

### Step 9 [Q - L1_1 · c7]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "literature": "GLOBlit_25",
  "system_type": "binary",
  "limit": 20,
  "purpose": "Check if GLOBlit_25 has both density and viscosity blocks",
  "tasks": "List all property blocks for this DOI"
}
```
</details>

- **Result:** 1,104 chars  |  **Time:** 11.1s  |  **Started:** 05:32:13 (t+201.4s)
- **Subagent:** KEEP in 8,422 → 1,104 chars (10.3s)
  - **GLOBlit_25 confirms both density and viscosity data** across three binary sub-systems (each alkane + squalane), yielding 6 property blocks total. DOI: `10.1007/s10765-006-0053-2`.

| Block | Propert

<details><summary>Result</summary>

```
**GLOBlit_25 confirms both density and viscosity data** across three binary sub-systems (each alkane + squalane), yielding 6 property blocks total. DOI: `10.1007/s10765-006-0053-2`.

| Block | Property | System | Pts | T range (K) | P range (kPa) | x(squalane) range |
|---|---|---|---|---|---|---|
| PROPblock_9 | Viscosity (GLOBprop_4) | butane + squalane | 80 | 273.15–313.15 | 100–30000 | 0.0–0.741 |
| PROPblock_10 | Mass density (GLOBprop_1) | butane + squalane | 80 | 273.15–313.15 | 100–30000 | 0.0–0.741 |
| PROPblock_11 | Viscosity (GLOBprop_4) | hexane + squalane | 64 | 273.15–333.15 | 100–30000 | 0.0–0.743 |
| PROPblock_12 | Mass density (GLOBprop_1) | hexane + squalane | 64 | 273.15–333.15 | 100–30000 | 0.0–0.743 |
| PROPblock_13 | Viscosity (GLOBprop_4) | octane + squalane | 80 | 273.15–313.15 | 100–30000 | 0.0–1.0 |
| PROPblock_14 | Mass density (GLOBprop_1) | octane + squalane | 80 | 273.15–313.15 | 100–30000 | 0.0–1.0 |

**Key compounds:** DOIcomp_1 = butane (GLOBcomp_102), DOIcomp_2 = hexane (GLOBcomp_12), DOIcomp_3 = octane (GLOBcomp_17), DOIcomp_4 = squalane (GLOBcomp_284).
```
</details>

---

### Step 10 [Q - L1_1 · c8]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "literature": "GLOBlit_59",
  "system_type": "binary",
  "limit": 20,
  "purpose": "Check if GLOBlit_59 has both density and viscosity blocks",
  "tasks": "List all property blocks for this DOI"
}
```
</details>

- **Result:** 547 chars  |  **Time:** 8.8s  |  **Started:** 05:32:30 (t+218.8s)
- **Subagent:** KEEP in 2,395 → 547 chars (8.6s)
  - **Verdict:** GLOBlit_59 contains **only density data** (mass density, kg/m³) — there is **no viscosity block**. It cannot serve as a source for both density and viscosity.

| Block | Property | Points

<details><summary>Result</summary>

```
**Verdict:** GLOBlit_59 contains **only density data** (mass density, kg/m³) — there is **no viscosity block**. It cannot serve as a source for both density and viscosity.

| Block | Property | Points | System | Compounds |
|---|---|---|---|---|
| PROPblock_2 | mass_density_kg_m3 | 270 | binary | GLOBcomp_36 (BMIMBF4) + GLOBcomp_2 (ethanol) |

- **Variables:** Temperature (298.15 K only), mole fraction of BMIMBF4 (0.0701–1.0), pressure (120–39980 kPa)
- **Phase:** Liquid
- No other property blocks were returned for this literature reference.
```
</details>

---

### Step 11 [Q - L1_1 · c9]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "literature": "GLOBlit_151",
  "system_type": "binary",
  "limit": 20,
  "purpose": "Check if GLOBlit_151 has both density and viscosity blocks",
  "tasks": "List all property blocks for this literature source"
}
```
</details>

- **Result:** 890 chars  |  **Time:** 12.0s  |  **Started:** 05:32:47 (t+235.9s)
- **Subagent:** KEEP in 7,640 → 890 chars (11.9s)
  - **GLOBlit_151 confirmed to have both density and viscosity blocks**, plus a refractive index block. All three are for the binary system butan-1-ol (GLOBcomp_7) + TEGDME (GLOBcomp_247), DOI: 10.1007/s1

<details><summary>Result</summary>

```
**GLOBlit_151 confirmed to have both density and viscosity blocks**, plus a refractive index block. All three are for the binary system butan-1-ol (GLOBcomp_7) + TEGDME (GLOBcomp_247), DOI: 10.1007/s10765-013-1469-0.

| Block | Property | GLOBprop | Points | T range (K) | x(butan-1-ol) | P (kPa) | Phase |
|---|---|---|---|---|---|---|---|
| PROPblock_7 | mass_density_kg_m3 | GLOBprop_1 | 110 (23 shown) | 288.15–308.15 | 0.0–1.0 | 101.0 | Liquid |
| PROPblock_8 | viscosity_pa_s | GLOBprop_4 | 110 (26 shown) | 288.15–308.15 | 0.0–1.0 | 101.0 | Liquid |
| PROPblock_9 | refractive_index_na_dline | GLOBprop_7 | 110 (23 shown) | 288.15–308.15 | 0.0–1.0 | 101.0 | Liquid |

**Shared variables/constraints across all blocks:**
- BLKvar_1 → GLOBvar_1: temperature_k
- BLKvar_2 → GLOBvar_2: mole_fraction (DOIcomp_1 / GLOBcomp_7, butan-1-ol)
- BLKconstr_1 → GLOBconstr_1: pressure_kpa = 101.0
```
</details>

---

## Tool Compaction Pipeline (9 calls)

| # | Tool | Pipeline | Native | Hardcoded | Agentic | Verdict | Native→Final | Section |
|--:|------|----------|-------:|----------:|--------:|---------|-------------:|---------|
| 1 | `search_system_registry` | query | 435,846 | 16,871 | 683 | KEEP | −100% | L1_1 |
| 2 | `search_system_registry` | query | 434,877 | 16,634 | 1,282 | KEEP | −100% | L1_1 |
| 3 | `block_search_adv` | query | 2,634 | 844 | 929 | DISCARD | −65% | L1_1 |
| 4 | `search_blocks` | query | 6,444 | 2,388 | 611 | KEEP | −91% | L1_1 |
| 5 | `search_blocks` | query | 51,233 | 5,434 | 1,092 | KEEP | −98% | L1_1 |
| 6 | `search_blocks` | query | 37,921 | 8,821 | 1,189 | KEEP | −97% | L1_1 |
| 7 | `search_blocks` | query | 42,954 | 8,422 | 1,104 | KEEP | −97% | L1_1 |
| 8 | `search_blocks` | query | 6,754 | 2,395 | 547 | KEEP | −92% | L1_1 |
| 9 | `search_blocks` | query | 20,998 | 7,640 | 890 | KEEP | −96% | L1_1 |

## Subagent Summary (9 events)

| Tool | Verdict | Input Chars | Output Chars | Time | Section |
|------|---------|-------------|-------------|------|---------|
| search_system_registry | KEEP | 16,871 | 683 | 18.1s | L1_1 |
| search_system_registry | KEEP | 16,634 | 1,282 | 16.7s | L1_1 |
| block_search_adv | DISCARD | 844 | 929 | 10.9s | L1_1 |
| search_blocks | KEEP | 2,388 | 611 | 9.1s | L1_1 |
| search_blocks | KEEP | 5,434 | 1,092 | 11.0s | L1_1 |
| search_blocks | KEEP | 8,821 | 1,189 | 11.5s | L1_1 |
| search_blocks | KEEP | 8,422 | 1,104 | 10.3s | L1_1 |
| search_blocks | KEEP | 2,395 | 547 | 8.6s | L1_1 |
| search_blocks | KEEP | 7,640 | 890 | 11.9s | L1_1 |

---

**Total:** 10 tool calls  |  Tool time: 498.1s  |  Wall: 504.3s  |  **Status:** OK
