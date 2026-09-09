# Tool History — analysis-agent

**Nest:** A
**Session:** 37fd5a9c
**Detailed log:** run_history_detailed.md — Argo events + verbatim agent outputs (join: session id; step tag `cN` ↔ event-row `cN`)
**Prompt:** I am planning measurements on liquid DMSO + water near room temperature. Which thermophysical properties and composition–temperature regions are already well characterized, and where would new measurements add the most useful chemical information?
**Started:** 2026-09-05 06:24:57  |  **Elapsed:** 1289.4s  |  **Tool calls:** 42  |  **Nested sections:** 2

---

### Step 1 [A · c1]: `<malformed_tool_call_1>` ⏸️ HELD BACK BY BATCH

- **Result:** 59 chars  |  **Time:** 0.0s  |  **Started:** 06:25:13 (t+16.0s)
- **Status:** syntax-blocked

<details><summary>Validation detail</summary>

```
block 1: unclosed or structurally invalid <tool_call> block
```
</details>

---

### Step 2 [A · c2]: `query_thermoml_parallel` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "queries": [
    {
      "label": "density",
      "purpose": "Find density (GLOBprop_1) data blocks for DMSO + water binary mixtures near 288-318 K",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with mass density measurements. Return DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
      "id_catalog": [
        {
          "id": "GLOBprop_1",
          "type": "property"
        }
      ],
      "context": ""
    },
    {
      "label": "viscosity",
      "purpose": "Find viscosity (GLOBprop_4) data blocks for DMSO + water binary mixtures near 288-318 K",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with dynamic viscosity measurements. Return DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
      "id_catalog": [
        {
          "id": "GLOBprop_4",
          "type": "property"
        }
      ],
      "context": ""
    },
    {
      "label": "excess_enthalpy",
      "purpose": "Find excess molar enthalpy (GLOBprop_17) data blocks for DMSO + water binary mixtures",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with excess molar enthalpy HE measurements. Return DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
      "id_catalog": [
        {
          "id": "GLOBprop_17",
          "type": "property"
        }
      ],
      "context": ""
    },
    {
      "label": "refractive_index",
      "purpose": "Find refractive index (GLOBprop_7) data blocks for DMSO + water binary mixtures near room temperature",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with refractive index measurements. Return DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
      "id_catalog": [
        {
          "id": "GLOBprop_7",
          "type": "property"
        }
      ],
      "context": ""
    },
    {
      "label": "speed_of_sound",
      "purpose": "Find speed of sound (GLOBprop_8) data blocks for DMSO + water binary mixtures near room temperature",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with speed of sound measurements. Return DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
      "id_catalog": [
        {
          "id": "GLOBprop_8",
          "type": "property"
        }
      ],
      "context": ""
    },
    {
      "label": "heat_capacity",
      "purpose": "Find molar heat capacity (GLOBprop_9) data blocks for DMSO + water binary mixtures",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with molar heat capacity Cp measurements. Return DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
      "id_catalog": [
        {
          "id": "GLOBprop_9",
          "type": "property"
        }
      ],
      "context": ""
    },
    {
      "label": "surface_tension",
      "purpose": "Find surface tension (GLOBprop_13) data blocks for DMSO + water binary mixtures",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with surface tension measurements. Return DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
      "id_catalog": [
        {
          "id": "GLOBprop_13",
          "type": "property"
        }
      ],
      "context": ""
    }
  ]
}
```
</details>

- **Result:** 209 chars  |  **Time:** 0.0s  |  **Started:** 06:25:25 (t+27.6s)
- **Error:** `{
  "error": "queries[0].id_catalog[0] must contain exactly ['global_id', 'name', 'registry_id', 'type']; received ['id', 'type']",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml_parallel"
}`

---

### Step 3 [A · c3]: `query_thermoml_parallel` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "queries": [
    {
      "label": "density_dmso_water",
      "purpose": "Find all data blocks with mass density (GLOBprop_1) for binary mixture of DMSO (dimethyl sulfoxide) and water near room temperature (280-330 K)",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with density measurements. Return DOIs, block numbers, temperature ranges, composition ranges, and data point counts.",
      "id_catalog": null,
      "context": ""
    },
    {
      "label": "viscosity_dmso_water",
      "purpose": "Find all data blocks with dynamic viscosity (GLOBprop_4) for binary mixture of DMSO and water near room temperature (280-330 K)",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with viscosity measurements. Return DOIs, block numbers, temperature ranges, composition ranges, and data point counts.",
      "id_catalog": null,
      "context": ""
    },
    {
      "label": "excess_enthalpy_dmso_water",
      "purpose": "Find all data blocks with excess molar enthalpy (GLOBprop_17) for binary mixture of DMSO and water",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with excess molar enthalpy (HE) measurements. Return DOIs, block numbers, temperature ranges, composition ranges, and data point counts.",
      "id_catalog": null,
      "context": ""
    },
    {
      "label": "refractive_index_dmso_water",
      "purpose": "Find all data blocks with refractive index (GLOBprop_7) for binary mixture of DMSO and water near room temperature",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with refractive index measurements. Return DOIs, block numbers, temperature ranges, composition ranges, and data point counts.",
      "id_catalog": null,
      "context": ""
    },
    {
      "label": "speed_of_sound_dmso_water",
      "purpose": "Find all data blocks with speed of sound (GLOBprop_8) for binary mixture of DMSO and water near room temperature",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with speed of sound measurements. Return DOIs, block numbers, temperature ranges, composition ranges, and data point counts.",
      "id_catalog": null,
      "context": ""
    },
    {
      "label": "heat_capacity_dmso_water",
      "purpose": "Find all data blocks with molar heat capacity Cp (GLOBprop_9) for binary mixture of DMSO and water near room temperature",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with heat capacity measurements. Return DOIs, block numbers, temperature ranges, composition ranges, and data point counts.",
      "id_catalog": null,
      "context": ""
    },
    {
      "label": "surface_tension_dmso_water",
      "purpose": "Find all data blocks with surface tension (GLOBprop_13) for binary mixture of DMSO and water near room temperature",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with surface tension measurements. Return DOIs, block numbers, temperature ranges, composition ranges, and data point counts.",
      "id_catalog": null,
      "context": ""
    }
  ]
}
```
</details>

- **Result:** 132 chars  |  **Time:** 0.0s  |  **Started:** 06:25:38 (t+40.6s)
- **Error:** `{
  "error": "queries[0].id_catalog must be an array",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml_parallel"
}`

---

### Step 4 [A · c4]: `query_thermoml_parallel` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "queries": [
    {
      "label": "density_dmso_water",
      "purpose": "Find density data blocks for binary mixture of DMSO (dimethyl sulfoxide) + water near room temperature (288-318 K)",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with mass density or molar volume measurements. Report DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
      "id_catalog": null,
      "context": ""
    },
    {
      "label": "viscosity_dmso_water",
      "purpose": "Find viscosity data blocks for binary mixture of DMSO + water near room temperature",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with dynamic viscosity or kinematic viscosity measurements. Report DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
      "id_catalog": null,
      "context": ""
    },
    {
      "label": "excess_enthalpy_dmso_water",
      "purpose": "Find excess molar enthalpy (HE) data blocks for DMSO + water binary mixture",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with excess molar enthalpy measurements. Report DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
      "id_catalog": null,
      "context": ""
    },
    {
      "label": "refractive_index_dmso_water",
      "purpose": "Find refractive index data blocks for DMSO + water binary mixture near room temperature",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with refractive index measurements. Report DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
      "id_catalog": null,
      "context": ""
    },
    {
      "label": "speed_of_sound_dmso_water",
      "purpose": "Find speed of sound data blocks for DMSO + water binary mixture",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with speed of sound measurements. Report DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
      "id_catalog": null,
      "context": ""
    },
    {
      "label": "heat_capacity_dmso_water",
      "purpose": "Find heat capacity data blocks for DMSO + water binary mixture",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with molar heat capacity (Cp) measurements. Report DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
      "id_catalog": null,
      "context": ""
    },
    {
      "label": "surface_tension_dmso_water",
      "purpose": "Find surface tension data blocks for DMSO + water binary mixture",
      "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with surface tension measurements. Report DOIs, block numbers, temperature ranges, composition ranges, and number of data points.",
      "id_catalog": null,
      "context": ""
    }
  ]
}
```
</details>

- **Result:** 132 chars  |  **Time:** 0.0s  |  **Started:** 06:25:49 (t+52.4s)
- **Error:** `{
  "error": "queries[0].id_catalog must be an array",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml_parallel"
}`

---

### Step 5 [A · c14]: `query_thermoml`

<details><summary>Arguments</summary>

```json
{
  "purpose": "Find all thermophysical property data for DMSO (dimethyl sulfoxide) + water binary mixtures near room temperature (288-313 K)",
  "instruction": "Search for binary mixture data blocks containing both dimethyl sulfoxide (DMSO, CAS 67-68-5) and water (CAS 7732-18-5). Look for properties including density, viscosity, excess enthalpy, refractive index, speed of sound, heat capacity, surface tension, and vapor pressure. Focus on temperature range 288-313 K. Return all available DOIs, block numbers, property types, temperature ranges, composition ranges, and data point counts."
}
```
</details>

- **Result:** 85,458 chars  |  **Time:** 402.3s  |  **Started:** 06:25:57 (t+59.7s)
- **Nested:** ↳ 9 tool calls in section 'L1_1' below

<details><summary>Result</summary>

```
[TOOL_RESULT_SIZE_WARNING: query_thermoml returned 85,212 characters after result processing; the target is 24,000. The full result follows — prefer narrower requests, and rely on your working memory for recall instead of re-running this call.]

<subagent_answer>
{
  "answer": "## DMSO + Water Binary Mixture Data in the ThermoML Database (288\u2013313 K)\n\n### Overview\n\nThe ThermoML database contains **19 property data blocks** for the dimethyl sulfoxide (DMSO, GLOBcomp_31) + water (GLOBcomp_1) binary system in the 288\u2013313 K temperature window, spanning **12 publications** and totaling **1,425 data points**. All data are for the liquid phase.\n\n### Property Coverage\n\n| Property | GLOBprop | Block count |\n|----------|----------|-------------|\n| Mass density (kg/m\u00b3) | GLOBprop_1 | 8 |\n| Viscosity (Pa\u00b7s) | GLOBprop_4 | 3 |\n| Speed of sound (m/s) | GLOBprop_8 | 2 |\n| Apparent molar heat capacity (J/K/mol) | GLOBprop_64 | 1 |\n| Molar enthalpy of solution (kJ/mol) | GLOBprop_15 | 1 |\n| Thermal conductivity (W/m/K) | \u2014 | 1 |\n| Relative permittivity at zero frequency | GLOBprop_44 | 1 |\n| Surface tension liquid\u2013gas (N/m) | \u2014 | 1 |\n| Refractive index (Na D-line) | \u2014 | 1 |\n\n### Block Listing by Source\n\n**1. GLOBlit_2584** \u2014 DOI: 10.1016/j.jct.2005.07.012\n\n| Block | Property | Points |\n|-------|----------|--------|\n| PROPblock_8 | Mass density (GLOBprop_1) | 96 |\n\n*(Block-level details not inspected in this run.)*\n\n**2. GLOBlit_2652** \u2014 DOI: 10.1016/j.jct.2006.01.007\n\n| Block | Property | Points |\n|-------|----------|--------|\n| PROPblock_3 | Speed of sound (GLOBprop_8) | 6 |\n| PROPblock_4 | Mass density (GLOBprop_1) | 6 |\n\n*(Block-level details not inspected in this run.)*\n\n**3. GLOBlit_2781** \u2014 DOI: 10.1016/j.jct.2006.12.012\n\n| Block | Property | Points |\n|-------|----------|--------|\n| PROPblock_3 | Viscosity (GLOBprop_4) | 120 |\n| PROPblock_4 | Mass density (GLOBprop_1) | 120 |\n\n*(Block-level details not inspected in this run.)*\n\n**4. GLOBlit_2844** \u2014 DOI: 10.1016/j.jct.2007.06.010\n\n| Block | Property | Points |\n|-------|----------|--------|\n| PROPblock_3 | Apparent molar Cp (GLOBprop_64) | 216 |\n| PROPblock_4 | Mass density (GLOBprop_1) | 92 |\n\n*(Block-level details not inspected in this run.)*\n\n**5. GLOBlit_5953** \u2014 DOI: 10.1016/j.tca.2011.08.013\n\n| Block | Property | Points |\n|-------|----------|--------|\n| PROPblock_10 | Viscosity (GLOBprop_4) | 16 |\n| PROPblock_11 | Speed of sound (GLOBprop_8) | 16 |\n| PROPblock_12 | Mass density (GLOBprop_1) | 16 |\n\n*(Block-level details not inspected in this run.)*\n\n**6. GLOBlit_5958** \u2014 DOI: 10.1016/j.tca.2011.09.009\n\n| Block | Property | Points |\n|-------|----------|--------|\n| PROPblock_1 | Molar enthalpy of solution (GLOBprop_15) | 1 |\n\n*(Block-level details not inspected in this run.)*\n\n**7. GLOBlit_7713** \u2014 DOI: 10.1021/acs.jced.8b01048\n\n| Block | Property | Points |\n|-------|----------|--------|\n| PROPblock_10 | Mass density (GLOBprop_1) | 9 |\n\n*(Block-level details not inspected in this run.)*\n\n**8. GLOBlit_10109** \u2014 DOI: 10.1021/je400149j\n\n| Block | Property | Points |\n|-------|----------|--------|\n| PROPblock_5 | Relative permittivity at zero frequency (GLOBprop_44) | 363 |\n\n*(Block-level details not inspected in this run.)*\n\n**9\u201312. Additional DOIs (from summary)**\n\nThe system summary confirms 4 additional DOIs contributing blocks, including GLOBlit_10766 (DOI: 10.1021/je7001013, 2 blocks, 145 points) and others covering the remaining properties (thermal conductivity, surface tension, refractive index, and additional density data). Detailed block-level information for these was not retrieved in this run.\n\n### Top Papers by Data Volume\n\n| GLOBlit | DOI | Blocks | Matching points |\n|---------|-----|--------|----------------|\n| GLOBlit_10109 | 10.1021/je400149j | 1 | 363 |\n| GLOBlit_2844 | 10.1016/j.jct.2007.06.010 | 2 | 308 |\n| GLOBlit_2781 | 10.1016/j.jct.2006.12.012 | 2 | 240 |\n| GLOBlit_10766 | 10.1021/je7001013 | 2 | 145 |\n| GLOBlit_2584 | 10.1016/j.jct.2005.07.012 | 1 | 96 |\n\n### Chemistry Context\n\nThe DMSO\u2013water system is well known for its strong non-ideal mixing behavior driven by DMSO\u2013water hydrogen bonding. The database coverage is richest for mass density (8 blocks from multiple research groups), providing good redundancy for cross-validation. Transport properties (viscosity, speed of sound, thermal conductivity), dielectric properties (relative permittivity), and interfacial properties (surface tension, refractive index) are also represented, along with calorimetric data (apparent molar heat capacity, enthalpy of solution). Individual data-point values were not inspected in this run; targeted block inspections would be needed to retrieve specific numerical values at particular compositions and temperatures.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNINSPECTED_BLOCK** PROPblock_8: PROPblock_8 is quoted with data values (96, \u2026) but was never inspected in this run\n  fix (required \u2014 this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_8\", literature=\"<GLOBlit_N or DOI>\")`\n- **UNINSPECTED_BLOCK** PROPblock_3 + PROPblock_4: PROPblock_3 + PROPblock_4 is quoted with data values (120, 120, \u2026) but was never inspected in this run\n  fix (required \u2014 this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_3\", literature=\"<GLOBlit_N or DOI>\"); inspect_block_table(block_number=\"PROPblock_4\", literature=\"<GLOBlit_N or DOI>\")`\n- **UNINSPECTED_BLOCK** PROPblock_3 + PROPblock_4: PROPblock_3 + PROPblock_4 is quoted with data values (216, 92, \u2026) but was never inspected in this run\n  fix (required \u2014 this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_3\", literature=\"<GLOBlit_N or DOI>\"); inspect_block_table(block_number=\"PROPblock_4\", literature=\"<GLOBlit_N or DOI>\")`\n- **UNINSPECTED_BLOCK** PROPblock_10 + PROPblock_11 + PROPblock_12: PROPblock_10 + PROPblock_11 + PROPblock_12 is quoted with data values (16, 16, 16, \u2026) but was never inspected in this run\n  fix (required \u2014 this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_10\", literature=\"<GLOBlit_N or DOI>\"); inspect_block_table(block_number=\"PROPblock_11\", literature=\"<GLOBlit_N or DOI>\"); inspect_block_table(block_number=\"PROPblock_12\", literature=\"<GLOBlit_N or DOI>\")`\n- **UNINSPECTED_BLOCK** PROPblock_5: PROPblock_5 is quoted with data values (363, \u2026) but was never inspected in this run\n  fix (required \u2014 this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_5\", literature=\"<GLOBlit_N or DOI>\")`\n- **UNINSPECTED_BLOCK** PROPblock_5: PROPblock_5 is quoted with data values (145, \u2026) but was never inspected in this run\n  fix (required \u2014 this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_5\", literature=\"<GLOBlit_N or DOI>\")`\n- **UNINSPECTED_BLOCK** PROPblock_5: PROPblock_5 is quoted with data values (363, 308, 240, 145, \u2026) but was never inspected in this run\n  fix (required \u2014 this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_5\", literature=\"<GLOBlit_N or DOI>\")`",
  "core_claims": [
    "The ThermoML database contains 19 property data blocks for the DMSO + water binary system in the 288\u2013313 K temperature window, spanning 12 publications and totaling 1,425 data points, all for the liquid phase.",
    "Mass density is the most extensively covered property with 8 blocks from multiple research groups, followed by viscosity (3 blocks), speed of sound (2 blocks), and single blocks each for apparent molar heat capacity, molar enthalpy of solution, thermal conductivity, relative permittivity at zero frequency, surface tension, and refractive index.",
    "Individual data-point values were not inspected in this run; all block-level point counts and property assignments carry UNVERIFIED flags and would require targeted block inspections to confirm."
  ],
  "status": "partial",
  "summary": "The ThermoML database contains 19 property data blocks for the DMSO (GLOBcomp_31) + water (GLOBcomp_1) binary system in the 288\u2013313 K temperature range, drawn from 12 publications and totaling 1,425 liquid-phase data points. The most extensively covered property is mass density (kg/m\u00b3, GLOBprop_1) with 8 blocks, followed by viscosity (Pa\u00b7s, GLOBprop_4, 3 blocks), speed of sound (m/s, GLOBprop_8, 2 blocks), and single blocks each for apparent molar heat capacity (J/K/mol, GLOBprop_64), molar enthalpy of solution (kJ/mol, GLOBprop_15), relative permittivity at zero frequency (GLOBprop_44), thermal conductivity, surface tension, and refractive index. The largest single contributor is GLOBlit_10109 (DOI: 10.1021/je400149j) with 363 points of relative permittivity data, followed by GLOBlit_2844 (DOI: 10.1016/j.jct.2007.06.010) with 308 points covering apparent molar heat capacity and density, and GLOBlit_2781 (DOI: 10.1016/j.jct.2006.12.012) with 240 points of viscosity and density. Other notable sources include GLOBlit_10766 (DOI: 10.1021/je7001013, 145 points), GLOBlit_2584 (DOI: 10.1016/j.jct.2005.07.012, 96 density points), GLOBlit_5953 (DOI: 10.1016/j.tca.2011.08.013, 48 points across density, viscosity, and speed of sound), and GLOBlit_5958 (DOI: 10.1016/j.tca.2011.09.009, 1 enthalpy-of-solution point). Individual data-point values at specific compositions and temperatures were not inspected; block-level point counts and property assignments are reported but flagged as unverified against direct block inspection.",
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
      "description": "Mass density for DMSO + water binary mixture.",
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
      "lit_num_id": "GLOBlit_2652",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_8"
      ],
      "description": "Speed of sound for DMSO + water binary mixture.",
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
          "prop_num_id": "GLOBprop_8",
          "prop_ID": "speed_of_sound_m_s",
          "name": "Speed of sound, m/s",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_7",
          "meas_ID": "sing_around_technique_in_a_fixed_path_interferometer",
          "method_standard": "Sing-around technique in a fixed-path interferometer",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Speed of sound, m/s",
            "min": 1555.18,
            "max": 1579.41,
            "mean": 1569.326667,
            "std": 9.218429,
            "n": 6
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1555.18,
          "range_max": 1579.41
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
      "description": "Mass density for DMSO + water binary mixture.",
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
      "description": "Viscosity for DMSO + water binary mixture.",
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
      "description": "Mass density for DMSO + water binary mixture.",
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
      "lit_num_id": "GLOBlit_2844",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_64"
      ],
      "description": "Apparent molar heat capacity for DMSO + water binary mixture.",
      "doi": "10.1016/j.jct.2007.06.010",
      "lit_id": "2008-swe-blo-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 216,
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
            "max": 393.15,
            "n_unique": 24
          },
          "range_min": 278.15,
          "range_max": 393.15
        },
        {
          "BLKvar_id": "BLKvar_2",
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
            "BLKvar_id": "BLKvar_2",
            "name": "Molality, mol/kg",
            "min": 0.0205,
            "max": 2.9997,
            "n_unique": 9
          },
          "range_min": 0.0205,
          "range_max": 2.9997
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_64",
          "prop_ID": "apparent_molar_heat_capacity_j_k_mol",
          "name": "Apparent molar heat capacity, J/K/mol",
          "group": "ExcessPartialApparentEnergyProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_57",
          "meas_ID": "extra_sensitive_dsc",
          "method_standard": "Extra sensitive DSC",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Apparent molar heat capacity, J/K/mol",
            "min": 137.8,
            "max": 271.04,
            "mean": 207.224676,
            "std": 24.807154,
            "n": 216
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 137.8,
          "range_max": 271.04
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
      "parent_n_datapoints": 216,
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
      "description": "Mass density for DMSO + water binary mixture.",
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
      "description": "Viscosity for DMSO + water binary mixture.",
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
      "lit_num_id": "GLOBlit_5953",
      "block_number": "PROPblock_11",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_8"
      ],
      "description": "Speed of sound for DMSO + water binary mixture.",
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
          "prop_num_id": "GLOBprop_8",
          "prop_ID": "speed_of_sound_m_s",
          "name": "Speed of sound, m/s",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_15",
          "meas_ID": "linear_variable_path_acoustic_interferometer",
          "method_standard": "Linear variable-path acoustic interferometer",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Speed of sound, m/s",
            "min": 1534.6,
            "max": 1604.9,
            "mean": 1573.70625,
            "std": 23.583765,
            "n": 16
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1534.6,
          "range_max": 1604.9
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
      "description": "Mass density for DMSO + water binary mixture.",
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
      "lit_num_id": "GLOBlit_5958",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_15"
      ],
      "description": "Molar enthalpy of solution for DMSO + water binary mixture.",
      "doi": "10.1016/j.tca.2011.09.009",
      "lit_id": "2011-iva-smi-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 1,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
      "solvents": [
        {
          "component_org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "solvent_num_id": "GLOBsolvent_8",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N"
        }
      ],
      "constraints": [],
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
            "min": 0.092,
            "max": 0.092,
            "n_unique": 1
          },
          "range_min": 0.092,
          "range_max": 0.092
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
            "min": 101.0,
            "max": 101.0,
            "n_unique": 1
          },
          "range_min": 101.0,
          "range_max": 101.0
        },
        {
          "BLKvar_id": "BLKvar_3",
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
            "BLKvar_id": "BLKvar_3",
            "name": "Temperature, K",
            "min": 298.15,
            "max": 298.15,
            "n_unique": 1
          },
          "range_min": 298.15,
          "range_max": 298.15
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_15",
          "prop_ID": "molar_enthalpy_of_solution_kj_mol",
          "name": "Molar enthalpy of solution, kJ/mol",
          "group": "ExcessPartialApparentEnergyProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_144",
          "meas_ID": "isoperibol",
          "method_standard": null,
          "method_custom": "ISOPERIBOL",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Molar enthalpy of solution, kJ/mol",
            "min": -5.38,
            "max": -5.38,
            "mean": -5.38,
            "std": 0,
            "n": 1
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": -5.38,
          "range_max": -5.38
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
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
      "parent_n_datapoints": 1,
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
      "description": "Mass density for DMSO + water binary mixture.",
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
    },
    {
      "lit_num_id": "GLOBlit_10109",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_44"
      ],
      "description": "Relative permittivity at zero frequency for DMSO + water binary mixture.",
      "doi": "10.1021/je400149j",
      "lit_id": "2013-plo-swi-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 363,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
            "max": 333.15,
            "n_unique": 41
          },
          "range_min": 253.15,
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
          "prop_num_id": "GLOBprop_44",
          "prop_ID": "relative_permittivity_at_zero_frequency",
          "name": "Relative permittivity at zero frequency",
          "group": "RefractionSurfaceTensionSoundSpeed",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_823",
          "meas_ID": "impedance_gain_phase_analyzer",
          "method_standard": null,
          "method_custom": "impedance/gain phase analyzer",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Relative permittivity at zero frequency",
            "min": 42.0,
            "max": 91.94,
            "mean": 63.480606,
            "std": 12.656003,
            "n": 363
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 42.0,
          "range_max": 91.94
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
          "SMILES": "CS(C)=O",
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
      "parent_n_datapoints": 363,
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

### Step 6 [A · c15]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2005.07.012",
  "block_number": "PROPblock_8",
  "purpose": "Verify density block structure: composition range, temperature range, point count for DMSO+water"
}
```
</details>

- **Result:** 295 chars  |  **Time:** 0.0s  |  **Started:** 06:32:54 (t+477.0s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to inspect_block: missing a required argument: 'tasks'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 7 [A · c16]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2005.07.012",
  "block_number": "PROPblock_8",
  "purpose": "Verify composition and temperature coverage of density data for DMSO+water",
  "tasks": [
    "inspect"
  ]
}
```
</details>

- **Result:** 333 chars  |  **Time:** 0.0s  |  **Started:** 06:33:07 (t+490.1s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block.tasks received ['inspect'] (list); expected <class 'str'>; tool arguments are never coerced

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 8 [A · c17]: `inspect_block`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2005.07.012",
  "block_number": "PROPblock_8",
  "purpose": "Verify composition and temperature coverage for DMSO+water density data",
  "tasks": "inspect"
}
```
</details>

- **Result:** 1,383 chars  |  **Time:** 0.1s  |  **Started:** 06:33:12 (t+495.2s)

<details><summary>Result</summary>

```
**Block GLOBlit_2584 / DOI 10.1016/j.jct.2005.07.012 / PROPblock_8 @ declared** (PureOrMixtureData)
Compounds: dimethyl sulfoxide, water | Rows: 96
x‑columns: ['mole_fraction_<water>'] | y‑columns: ['mass_density_kg_m3']

**Property response semantics (reported metadata; values are not materialized here)**
- **BLKprop_1 / GLOBprop_1** `mass_density_kg_m3` (mass_density_kg_m3)
  - reported response: Direct value, X
  - measurement: GLOBmeas_147 / vibtub_ufactor_16
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference: none; T=unspecified K; P=unspecified kPa
  - reference phase: none
  - component_org_num: none

**Selected property response contract (inspection only; values are not materialized here)**
- **BLKprop_1 / GLOBprop_1** `mass_density_kg_m3` (mass_density_kg_m3)
  - reported response: Direct value, X [direct]
  - units: reported=kg/m3; absolute=kg/m3
  - preparation gate: reference_materialization=False; normalized_composition=False; supported=True
  - reference: none; T=unspecified K; P=unspecified kPa
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference phase: none
  - component_org_num: none

| Column | Min | Max | Valid pts |
|--------|-----|-----|-----------|
| temperature_k | 288.15 | 303.15 | 96 |
| mole_fraction_<water> | 0.0308 | 0.9798 | 96 |
| pressure_kpa | 100 | 100 | 96 |
| mass_density_kg_m3 | 1005.71 | 1108.48 | 96 |

```
</details>

---

### Step 9 [A · c18]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2006.12.012",
  "block_number": "PROPblock_3"
}
```
</details>

- **Result:** 297 chars  |  **Time:** 0.0s  |  **Started:** 06:33:22 (t+505.4s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to inspect_block: missing a required argument: 'purpose'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 10 [A · c19]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2006.12.012",
  "block_number": "PROPblock_3",
  "purpose": "Verify viscosity block composition and temperature coverage for DMSO+water"
}
```
</details>

- **Result:** 295 chars  |  **Time:** 0.0s  |  **Started:** 06:33:28 (t+511.4s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to inspect_block: missing a required argument: 'tasks'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 11 [A · c20]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2006.12.012",
  "block_number": "PROPblock_3",
  "purpose": "Verify viscosity block structure for DMSO+water",
  "tasks": [
    "inspect"
  ]
}
```
</details>

- **Result:** 333 chars  |  **Time:** 0.0s  |  **Started:** 06:33:34 (t+517.0s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block.tasks received ['inspect'] (list); expected <class 'str'>; tool arguments are never coerced

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 12 [A · c21]: `inspect_block`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2006.12.012",
  "block_number": "PROPblock_3",
  "purpose": "Verify viscosity data coverage for DMSO+water",
  "tasks": "inspect"
}
```
</details>

- **Result:** 1,379 chars  |  **Time:** 0.1s  |  **Started:** 06:33:40 (t+523.3s)

<details><summary>Result</summary>

```
**Block GLOBlit_2781 / DOI 10.1016/j.jct.2006.12.012 / PROPblock_3 @ declared** (PureOrMixtureData)
Compounds: dimethyl sulfoxide, water | Rows: 120
x‑columns: ['mole_fraction_<dimethyl sulfoxide>'] | y‑columns: ['viscosity_pa_s']

**Property response semantics (reported metadata; values are not materialized here)**
- **BLKprop_1 / GLOBprop_4** `viscosity_pa_s` (viscosity_pa_s)
  - reported response: Direct value, X
  - measurement: GLOBmeas_140 / captub_ufactor_2
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference: none; T=unspecified K; P=unspecified kPa
  - reference phase: none
  - component_org_num: none

**Selected property response contract (inspection only; values are not materialized here)**
- **BLKprop_1 / GLOBprop_4** `viscosity_pa_s` (viscosity_pa_s)
  - reported response: Direct value, X [direct]
  - units: reported=Pa*s; absolute=Pa*s
  - preparation gate: reference_materialization=False; normalized_composition=False; supported=True
  - reference: none; T=unspecified K; P=unspecified kPa
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference phase: none
  - component_org_num: none

| Column | Min | Max | Valid pts |
|--------|-----|-----|-----------|
| temperature_k | 298.15 | 318.15 | 120 |
| mole_fraction_<dimethyl sulfoxide> | 0 | 1 | 120 |
| pressure_kpa | 101 | 101 | 120 |
| viscosity_pa_s | 0.000596 | 0.003735 | 120 |

```
</details>

---

### Step 13 [A · c22]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je400149j",
  "block_number": "PROPblock_5"
}
```
</details>

- **Result:** 297 chars  |  **Time:** 0.0s  |  **Started:** 06:33:50 (t+533.3s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to inspect_block: missing a required argument: 'purpose'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 14 [A · c23]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je400149j",
  "block_number": "PROPblock_5",
  "purpose": "Inspect permittivity block for DMSO+water to verify composition and temperature coverage"
}
```
</details>

- **Result:** 295 chars  |  **Time:** 0.0s  |  **Started:** 06:33:56 (t+539.0s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to inspect_block: missing a required argument: 'tasks'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 15 [A · c24]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je400149j",
  "block_number": "PROPblock_5",
  "purpose": "Verify composition and temperature coverage for relative permittivity data of DMSO+water",
  "tasks": [
    "inspect"
  ]
}
```
</details>

- **Result:** 333 chars  |  **Time:** 0.0s  |  **Started:** 06:34:02 (t+544.6s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block.tasks received ['inspect'] (list); expected <class 'str'>; tool arguments are never coerced

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 16 [A · c25]: `inspect_block`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je400149j",
  "block_number": "PROPblock_5",
  "purpose": "Inspect relative permittivity block for DMSO+water",
  "tasks": "inspect"
}
```
</details>

- **Result:** 1,522 chars  |  **Time:** 0.1s  |  **Started:** 06:34:07 (t+549.8s)

<details><summary>Result</summary>

```
**Block GLOBlit_10109 / DOI 10.1021/je400149j / PROPblock_5 @ declared** (PureOrMixtureData)
Compounds: dimethyl sulfoxide, water | Rows: 363
x‑columns: ['mole_fraction_<dimethyl sulfoxide>'] | y‑columns: ['relative_permittivity_at_zero_frequency']

**Property response semantics (reported metadata; values are not materialized here)**
- **BLKprop_1 / GLOBprop_44** `relative_permittivity_at_zero_frequency` (relative_permittivity_at_zero_frequency)
  - reported response: Direct value, X
  - measurement: GLOBmeas_823 / impedance_gain_phase_analyzer
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference: none; T=unspecified K; P=unspecified kPa
  - reference phase: none
  - component_org_num: none

**Selected property response contract (inspection only; values are not materialized here)**
- **BLKprop_1 / GLOBprop_44** `relative_permittivity_at_zero_frequency` (relative_permittivity_at_zero_frequency)
  - reported response: Direct value, X [direct]
  - units: reported=1; absolute=1
  - preparation gate: reference_materialization=False; normalized_composition=False; supported=True
  - reference: none; T=unspecified K; P=unspecified kPa
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference phase: none
  - component_org_num: none

| Column | Min | Max | Valid pts |
|--------|-----|-----|-----------|
| temperature_k | 253.15 | 333.15 | 363 |
| mole_fraction_<dimethyl sulfoxide> | 0 | 1 | 363 |
| pressure_kpa | 101 | 101 | 363 |
| relative_permittivity_at_zero_frequency | 42 | 91.94 | 363 |

```
</details>

---

### Step 17 [A · c26]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2007.06.010",
  "block_number": "PROPblock_3"
}
```
</details>

- **Result:** 297 chars  |  **Time:** 0.0s  |  **Started:** 06:34:16 (t+558.8s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to inspect_block: missing a required argument: 'purpose'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 18 [A · c27]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2007.06.010",
  "block_number": "PROPblock_3",
  "purpose": "Inspect apparent molar heat capacity block for DMSO+water"
}
```
</details>

- **Result:** 295 chars  |  **Time:** 0.0s  |  **Started:** 06:34:38 (t+580.9s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to inspect_block: missing a required argument: 'tasks'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 19 [A · c28]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2007.06.010",
  "block_number": "PROPblock_3",
  "purpose": "Inspect apparent molar heat capacity block for DMSO+water",
  "tasks": [
    "verify composition and temperature coverage"
  ]
}
```
</details>

- **Result:** 369 chars  |  **Time:** 0.0s  |  **Started:** 06:34:44 (t+586.7s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block.tasks received ['verify composition and temperature coverage'] (list); expected <class 'str'>; tool arguments are never coerced

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 20 [A · c29]: `inspect_block`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2007.06.010",
  "block_number": "PROPblock_3",
  "purpose": "Verify composition and temperature coverage for apparent molar heat capacity of DMSO+water",
  "tasks": "inspect block structure"
}
```
</details>

- **Result:** 1,534 chars  |  **Time:** 0.1s  |  **Started:** 06:34:49 (t+591.6s)

<details><summary>Result</summary>

```
**Block GLOBlit_2844 / DOI 10.1016/j.jct.2007.06.010 / PROPblock_3 @ declared** (PureOrMixtureData)
Compounds: dimethyl sulfoxide, water | Rows: 216
x‑columns: ['molality_mol_kg_<dimethyl sulfoxide>'] | y‑columns: ['apparent_molar_heat_capacity_j_k_mol']

**Property response semantics (reported metadata; values are not materialized here)**
- **BLKprop_1 / GLOBprop_64** `apparent_molar_heat_capacity_j_k_mol` (apparent_molar_heat_capacity_j_k_mol)
  - reported response: Direct value, X
  - measurement: GLOBmeas_57 / extra_sensitive_dsc
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference: none; T=unspecified K; P=unspecified kPa
  - reference phase: none
  - component_org_num: none

**Selected property response contract (inspection only; values are not materialized here)**
- **BLKprop_1 / GLOBprop_64** `apparent_molar_heat_capacity_j_k_mol` (apparent_molar_heat_capacity_j_k_mol)
  - reported response: Direct value, X [direct]
  - units: reported=J/(K mol); absolute=J/(K mol)
  - preparation gate: reference_materialization=False; normalized_composition=False; supported=True
  - reference: none; T=unspecified K; P=unspecified kPa
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference phase: none
  - component_org_num: none

| Column | Min | Max | Valid pts |
|--------|-----|-----|-----------|
| temperature_k | 278.15 | 393.15 | 216 |
| molality_mol_kg_<dimethyl sulfoxide> | 0.0205 | 2.9997 | 216 |
| pressure_kpa | 350 | 350 | 216 |
| apparent_molar_heat_capacity_j_k_mol | 137.8 | 271.04 | 216 |

```
</details>

---

### Step 21 [A · c30]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.tca.2011.08.013",
  "block_number": "PROPblock_11"
}
```
</details>

- **Result:** 297 chars  |  **Time:** 0.0s  |  **Started:** 06:35:02 (t+604.7s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to inspect_block: missing a required argument: 'purpose'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 22 [A · c31]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.tca.2011.08.013",
  "block_number": "PROPblock_11",
  "purpose": "Inspect speed of sound block for DMSO+water to verify composition and temperature coverage"
}
```
</details>

- **Result:** 295 chars  |  **Time:** 0.0s  |  **Started:** 06:35:07 (t+610.3s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to inspect_block: missing a required argument: 'tasks'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 23 [A · c32]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.tca.2011.08.013",
  "block_number": "PROPblock_11",
  "purpose": "Inspect speed of sound block for DMSO+water composition and temperature coverage",
  "tasks": [
    "inspect"
  ]
}
```
</details>

- **Result:** 333 chars  |  **Time:** 0.0s  |  **Started:** 06:35:13 (t+616.3s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block.tasks received ['inspect'] (list); expected <class 'str'>; tool arguments are never coerced

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 24 [A · c33]: `inspect_block`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.tca.2011.08.013",
  "block_number": "PROPblock_11",
  "purpose": "Inspect speed of sound block for DMSO+water to verify composition and temperature coverage",
  "tasks": "Verify column names, value ranges, and row count for speed of sound data"
}
```
</details>

- **Result:** 1,430 chars  |  **Time:** 0.4s  |  **Started:** 06:35:18 (t+621.3s)

<details><summary>Result</summary>

```
**Block GLOBlit_5953 / DOI 10.1016/j.tca.2011.08.013 / PROPblock_11 @ declared** (PureOrMixtureData)
Compounds: dimethyl sulfoxide, water | Rows: 16
x‑columns: ['mole_fraction_<dimethyl sulfoxide>'] | y‑columns: ['speed_of_sound_m_s']

**Property response semantics (reported metadata; values are not materialized here)**
- **BLKprop_1 / GLOBprop_8** `speed_of_sound_m_s` (speed_of_sound_m_s)
  - reported response: Direct value, X
  - measurement: GLOBmeas_15 / linear_variable_path_acoustic_interferometer
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference: none; T=unspecified K; P=unspecified kPa
  - reference phase: none
  - component_org_num: none

**Selected property response contract (inspection only; values are not materialized here)**
- **BLKprop_1 / GLOBprop_8** `speed_of_sound_m_s` (speed_of_sound_m_s)
  - reported response: Direct value, X [direct]
  - units: reported=m/s; absolute=m/s
  - preparation gate: reference_materialization=False; normalized_composition=False; supported=True
  - reference: none; T=unspecified K; P=unspecified kPa
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference phase: none
  - component_org_num: none

| Column | Min | Max | Valid pts |
|--------|-----|-----|-----------|
| mole_fraction_<dimethyl sulfoxide> | 0.0121 | 0.0583 | 16 |
| temperature_k | 303.15 | 318.15 | 16 |
| pressure_kpa | 101 | 101 | 16 |
| speed_of_sound_m_s | 1534.6 | 1604.9 | 16 |

```
</details>

---

### Step 25 [A · c42]: `query_thermoml`

<details><summary>Arguments</summary>

```json
{
  "purpose": "Find remaining DMSO+water blocks for thermal conductivity, surface tension, refractive index, and GLOBlit_10766 data",
  "instruction": "Search for binary mixture blocks containing dimethyl sulfoxide (GLOBcomp_31) and water (GLOBcomp_1) for properties: thermal conductivity, surface tension (GLOBprop_13), refractive index (GLOBprop_7). Also find all blocks from GLOBlit_10766 (DOI 10.1021/je7001013). Report block numbers, property types, composition ranges, temperature ranges, and point counts."
}
```
</details>

- **Result:** 112,628 chars  |  **Time:** 325.2s  |  **Started:** 06:35:29 (t+632.1s)
- **Nested:** ↳ 8 tool calls in section 'L1_2' below

<details><summary>Result</summary>

```
[TOOL_RESULT_SIZE_WARNING: query_thermoml returned 112,381 characters after result processing; the target is 24,000. The full result follows — prefer narrower requests, and rely on your working memory for recall instead of re-running this call.]

<subagent_answer>
{
  "answer": "## DMSO + Water Binary Mixture Blocks\n\n### Thermal Conductivity (GLOBprop_34)\n- **Block:** PROPblock_5 in GLOBlit_10024 (DOI: 10.1021/je301171y)\n- **Points:** 63\n- **Composition range:** w(DMSO) = 0.1\u20130.9 (mass fraction)\n- **Temperature range:** 279.18\u2013339.37 K\n- **Pressure:** 100.0 kPa (fixed constraint)\n- **Method:** Hot-wire method (GLOBmeas_41)\n- **Representative inspected values:** \u03bb = 0.522 W/m/K at w=0.1, T=279.63 K; \u03bb = 0.319 W/m/K at w=0.5013, T=279.57 K; \u03bb = 0.196 W/m/K at w=0.9, T=338.51 K. Thermal conductivity decreases with increasing DMSO mass fraction and generally increases with temperature at each composition.\n\n### Surface Tension (GLOBprop_13)\n- **Block:** PROPblock_9 in GLOBlit_10766 (DOI: 10.1021/je7001013)\n- **Points:** 112\n- **Composition range:** x(DMSO) = 0.0121\u20130.8945 (mole fraction)\n- **Temperature range:** 298.15\u2013328.15 K\n- **Method:** Maximal bubble pressure (GLOBmeas_36)\n- **Representative inspected values:** \u03b3 = 0.071 N/m at x=0.0121, T=298.15 K; \u03b3 = 0.046 N/m at x=0.59, T=298.15 K; \u03b3 = 0.042 N/m at x=0.8945, T=298.15 K; \u03b3 = 0.0387 N/m at x=0.8945, T=328.15 K. Surface tension decreases sharply with initial DMSO addition and more gradually at higher DMSO content.\n\n### Refractive Index (GLOBprop_7)\n- **Block:** PROPblock_10 in GLOBlit_10766 (DOI: 10.1021/je7001013)\n- **Points:** 33\n- **Composition range:** x(DMSO) = 0.0121\u20130.7685 (mole fraction)\n- **Temperature range:** 298.15\u2013308.15 K\n- **Pressure:** 101.0 kPa (fixed constraint)\n- **Method:** Abbe refractometer (GLOBmeas_163)\n- **Representative inspected values:** n_D = 1.34 at x=0.0121, T=298.15 K; n_D = 1.4305 at x=0.2959, T=298.15 K; n_D = 1.47 at x=0.7685, T=298.15 K. Refractive index increases monotonically with DMSO mole fraction.\n\n---\n\n## All Blocks from GLOBlit_10766 (DOI: 10.1021/je7001013)\n\nThis reference contains data blocks (count derived from the search_blocks listing of that literature source) covering four sulfoxides (pure and binary with water), measuring surface tension (GLOBprop_13) and refractive index (GLOBprop_7):\n\n**Compounds studied:**\n- GLOBcomp_31 = dimethyl sulfoxide (DMSO)\n- GLOBcomp_1294 = diethyl sulfoxide\n- GLOBcomp_2145 = dipropyl sulfoxide\n- GLOBcomp_7698 = diisopropyl sulfoxide (2,2'-sulfinylbispropane)\n- GLOBcomp_1 = water\n\n| Block | System | Compound(s) | Property |\n|---|---|---|---|\n| PROPblock_1 | unary | GLOBcomp_31 (DMSO) | GLOBprop_13 (surface tension) |\n| PROPblock_2 | unary | GLOBcomp_31 (DMSO) | GLOBprop_7 (refractive index) |\n| PROPblock_3 | unary | GLOBcomp_1294 (diethyl sulfoxide) | GLOBprop_13 (surface tension) |\n| PROPblock_4 | unary | GLOBcomp_1294 (diethyl sulfoxide) | GLOBprop_7 (refractive index) |\n| PROPblock_5 | unary | GLOBcomp_2145 (dipropyl sulfoxide) | GLOBprop_13 (surface tension) |\n| PROPblock_6 | unary | GLOBcomp_2145 (dipropyl sulfoxide) | GLOBprop_7 (refractive index) |\n| PROPblock_7 | unary | GLOBcomp_7698 (diisopropyl sulfoxide) | GLOBprop_13 (surface tension) |\n| PROPblock_8 | unary | GLOBcomp_7698 (diisopropyl sulfoxide) | GLOBprop_7 (refractive index) |\n| PROPblock_9 | binary | GLOBcomp_31 + GLOBcomp_1 | GLOBprop_13 (surface tension) \u2014 112 pts, x(DMSO) 0.0121\u20130.8945, T 298.15\u2013328.15 K |\n| PROPblock_10 | binary | GLOBcomp_31 + GLOBcomp_1 | GLOBprop_7 (refractive index) \u2014 33 pts, x(DMSO) 0.0121\u20130.7685, T 298.15\u2013308.15 K |\n| PROPblock_11 | binary | GLOBcomp_1294 + GLOBcomp_1 | GLOBprop_13 (surface tension) |\n| PROPblock_12 | binary | GLOBcomp_1294 + GLOBcomp_1 | GLOBprop_7 (refractive index) |\n| PROPblock_13 | binary | GLOBcomp_2145 + GLOBcomp_1 | GLOBprop_13 (surface tension) |\n| PROPblock_14 | binary | GLOBcomp_2145 + GLOBcomp_1 | GLOBprop_7 (refractive index) |\n| PROPblock_15 | binary | GLOBcomp_7698 + GLOBcomp_1 | GLOBprop_13 (surface tension) |\n| PROPblock_16 | binary | GLOBcomp_7698 + GLOBcomp_1 | GLOBprop_7 (refractive index) |\n\nThe eight unary blocks provide pure-component baselines for each sulfoxide, while the eight binary blocks systematically cover each sulfoxide mixed with water. The DMSO+water blocks (PROPblock_9 and PROPblock_10) are the most data-rich among the binary blocks in this reference. Detailed numerical ranges for blocks not inspected in this run (PROPblock_1\u20138, PROPblock_11\u201316) are available but were not verified here.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNINSPECTED_BLOCK** PROPblock_11: PROPblock_11 is quoted with data values (16, \u2026) but was never inspected in this run\n  fix (required \u2014 this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_11\", literature=\"<GLOBlit_N or DOI>\")`\nInspected so far: PROPblock_10, PROPblock_5, PROPblock_9",
  "core_claims": [
    "For the DMSO + water binary mixture at 100.0 kPa, thermal conductivity (63 points, w(DMSO) = 0.1\u20130.9, T = 279.18\u2013339.37 K, hot-wire method) decreases with increasing DMSO mass fraction and generally increases with temperature at each composition, with representative values of \u03bb = 0.522 W/m/K at w=0.1, T=279.63 K; \u03bb = 0.319 W/m/K at w=0.5013, T=279.57 K; and \u03bb = 0.196 W/m/K at w=0.9, T=338.51 K.",
    "For the DMSO + water binary mixture, surface tension (112 points, x(DMSO) = 0.0121\u20130.8945, T = 298.15\u2013328.15 K, maximal bubble pressure method) decreases sharply with initial DMSO addition and more gradually at higher DMSO content, with representative values of \u03b3 = 0.071 N/m at x=0.0121, T=298.15 K; \u03b3 = 0.046 N/m at x=0.59, T=298.15 K; and \u03b3 = 0.042 N/m at x=0.8945, T=298.15 K.",
    "For the DMSO + water binary mixture at 101.0 kPa, refractive index (33 points, x(DMSO) = 0.0121\u20130.7685, T = 298.15\u2013308.15 K, Abbe refractometer) increases monotonically with DMSO mole fraction, from n_D = 1.34 at x=0.0121 to n_D = 1.47 at x=0.7685 at 298.15 K.",
    "The reference DOI 10.1021/je7001013 contains 16 data blocks covering surface tension and refractive index for four sulfoxides (DMSO, diethyl sulfoxide, dipropyl sulfoxide, diisopropyl sulfoxide) as pure components and as binary mixtures with water; only the DMSO+water blocks (PROPblock_9 and PROPblock_10) were numerically inspected and verified.",
    "Several blocks cited in the answer (PROPblock_1\u20138, PROPblock_11\u201316) were not inspected during the analysis run and their detailed numerical ranges remain unverified."
  ],
  "status": "success",
  "summary": "Three DMSO + water binary mixture data blocks were identified and inspected. (1) Thermal conductivity (GLOBprop_34) in PROPblock_5 of GLOBlit_10024 (DOI: 10.1021/je301171y): 63 points, w(DMSO) = 0.1\u20130.9 mass fraction, T = 279.18\u2013339.37 K, P = 100.0 kPa, measured by hot-wire method; representative values include \u03bb = 0.522 W/m/K at w=0.1, T=279.63 K and \u03bb = 0.196 W/m/K at w=0.9, T=338.51 K, with thermal conductivity decreasing with increasing DMSO content. (2) Surface tension (GLOBprop_13) in PROPblock_9 of GLOBlit_10766 (DOI: 10.1021/je7001013): 112 points, x(DMSO) = 0.0121\u20130.8945 mole fraction, T = 298.15\u2013328.15 K, measured by maximal bubble pressure; representative values include \u03b3 = 0.071 N/m at x=0.0121, T=298.15 K and \u03b3 = 0.0387 N/m at x=0.8945, T=328.15 K, with surface tension decreasing sharply upon initial DMSO addition. (3) Refractive index (GLOBprop_7) in PROPblock_10 of GLOBlit_10766: 33 points, x(DMSO) = 0.0121\u20130.7685, T = 298.15\u2013308.15 K, P = 101.0 kPa, measured by Abbe refractometer; n_D increases monotonically with DMSO mole fraction from 1.34 to 1.47. GLOBlit_10766 additionally contains 16 total blocks covering four sulfoxides (DMSO, diethyl sulfoxide, dipropyl sulfoxide, diisopropyl sulfoxide) as pure components and binary mixtures with water, measuring surface tension and refractive index; only the DMSO+water blocks (PROPblock_9 and PROPblock_10) were numerically inspected.",
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
      "core_GLOB_id": "GLOBcomp_1294",
      "registry_id": "diethyl_sulfoxide",
      "name": "diethyl sulfoxide"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_2145",
      "registry_id": "dipropyl_sulfoxide",
      "name": "dipropyl sulfoxide"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_7698",
      "registry_id": "2,2'-sulfinylbispropane",
      "name": "2,2'-sulfinylbispropane"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_34",
      "registry_id": "thermal_conductivity_w_m_k",
      "name": "Thermal conductivity, W/m/K"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_13",
      "registry_id": "surface_tension_liquidgas_n_m",
      "name": "Surface tension liquid-gas, N/m"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBprop_7",
      "registry_id": "refractive_index_na_dline",
      "name": "Refractive index (Na D-line)"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_10024",
      "registry_id": "2013-zho-che-0",
      "name": "10.1021/je301171y"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBlit_10766",
      "registry_id": "2007-mar-ter-0",
      "name": "10.1021/je7001013"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBmeas_41",
      "registry_id": "hot_wire_method",
      "name": "Hot wire method"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBmeas_36",
      "registry_id": "maximal_bubble_pressure",
      "name": "Maximal bubble pressure"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBmeas_163",
      "registry_id": "abbe_ufactor_4",
      "name": "ABBE:UFactor:4"
    }
  ],
  "core_blocks_found": [
    {
      "lit_num_id": "GLOBlit_10024",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_34"
      ],
      "description": "Thermal conductivity of DMSO+water binary mixture; 63 points; w(DMSO) 0.1\u20130.9 (mass fraction); T 279.18\u2013339.37 K; P 100.0 kPa; hot-wire method (GLOBmeas_41).",
      "doi": "10.1021/je301171y",
      "lit_id": "2013-zho-che-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 63,
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
            "BLKvar_id": "BLKvar_1",
            "name": "Mass fraction",
            "min": 0.1,
            "max": 0.9,
            "n_unique": 9
          },
          "range_min": 0.1,
          "range_max": 0.9
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
            "min": 279.18,
            "max": 339.37,
            "n_unique": 62
          },
          "range_min": 279.18,
          "range_max": 339.37
        }
      ],
      "properties": [
        {
          "BLKprop_id": "BLKprop_1",
          "prop_num_id": "GLOBprop_34",
          "prop_ID": "thermal_conductivity_w_m_k",
          "name": "Thermal conductivity, W/m/K",
          "group": "TransportProp",
          "component_org_num": null,
          "meas_num_id": "GLOBmeas_41",
          "meas_ID": "hot_wire_method",
          "method_standard": "Hot wire method",
          "method_custom": null,
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Thermal conductivity, W/m/K",
            "min": 0.196,
            "max": 0.594,
            "mean": 0.354825,
            "std": 0.121236,
            "n": 63
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.196,
          "range_max": 0.594
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
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_1",
          "name": "water",
          "formula": "H2O",
          "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
          "SMILES": "O",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "parent_n_datapoints": 63,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_1",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_31"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of pure DMSO.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 7,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
            "max": 328.15,
            "n_unique": 7
          },
          "range_min": 298.15,
          "range_max": 328.15
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
          "meas_num_id": "GLOBmeas_714",
          "meas_ID": "bubblep_ufactor_8",
          "method_standard": null,
          "method_custom": "BUBBLEP:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0379,
            "max": 0.0417,
            "mean": 0.039743,
            "std": 0.001359,
            "n": 7
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0379,
          "range_max": 0.0417
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
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "unary",
      "declared_n_components": 1,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "parent_n_datapoints": 7,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_2",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_31"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of pure DMSO.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 3,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
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
            "min": 298.15,
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 308.15
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.472,
            "max": 1.4765,
            "mean": 1.474167,
            "std": 0.002255,
            "n": 3
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.472,
          "range_max": 1.4765
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
      "declared_system_type": "unary",
      "declared_n_components": 1,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_1_1"
        }
      ],
      "parent_n_datapoints": 3,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_3",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_1294"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of pure diethyl sulfoxide.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 7,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
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
          "meas_num_id": "GLOBmeas_714",
          "meas_ID": "bubblep_ufactor_8",
          "method_standard": null,
          "method_custom": "BUBBLEP:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.032,
            "max": 0.0346,
            "mean": 0.033243,
            "std": 0.000943,
            "n": 7
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.032,
          "range_max": 0.0346
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
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "unary",
      "declared_n_components": 1,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 7,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_4",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_1294"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of pure diethyl sulfoxide.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 3,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
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
            "min": 298.15,
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 308.15
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.464,
            "max": 1.468,
            "mean": 1.466,
            "std": 0.002,
            "n": 3
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.464,
          "range_max": 1.468
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
      "declared_system_type": "unary",
      "declared_n_components": 1,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
          "sample_num": "DOIcompSample_2_1"
        }
      ],
      "parent_n_datapoints": 3,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_5",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_2145"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of pure dipropyl sulfoxide.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 7,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
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
            "min": 298.15,
            "max": 328.15,
            "n_unique": 7
          },
          "range_min": 298.15,
          "range_max": 328.15
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
          "meas_num_id": "GLOBmeas_714",
          "meas_ID": "bubblep_ufactor_8",
          "method_standard": null,
          "method_custom": "BUBBLEP:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0294,
            "max": 0.0326,
            "mean": 0.030986,
            "std": 0.001142,
            "n": 7
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0294,
          "range_max": 0.0326
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
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "unary",
      "declared_n_components": 1,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "parent_n_datapoints": 7,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_6",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_2145"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of pure dipropyl sulfoxide.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 3,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
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
            "min": 298.15,
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 308.15
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.456,
            "max": 1.4595,
            "mean": 1.457833,
            "std": 0.001756,
            "n": 3
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.456,
          "range_max": 1.4595
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
      "declared_system_type": "unary",
      "declared_n_components": 1,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
          "sample_num": "DOIcompSample_3_1"
        }
      ],
      "parent_n_datapoints": 3,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_7",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_7698"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of pure diisopropyl sulfoxide.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 7,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
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
            "min": 298.15,
            "max": 328.15,
            "n_unique": 7
          },
          "range_min": 298.15,
          "range_max": 328.15
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
          "meas_num_id": "GLOBmeas_714",
          "meas_ID": "bubblep_ufactor_8",
          "method_standard": null,
          "method_custom": "BUBBLEP:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0291,
            "max": 0.0318,
            "mean": 0.030343,
            "std": 0.000961,
            "n": 7
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0291,
          "range_max": 0.0318
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
        }
      ],
      "reaction_type": null,
      "participants": [],
      "notes": null,
      "declared_system_type": "unary",
      "declared_n_components": 1,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "parent_n_datapoints": 7,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_8",
      "BLKsubsys_id": null,
      "system_type": "unary",
      "comp_num_ids": [
        "GLOBcomp_7698"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of pure diisopropyl sulfoxide.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_2",
      "n_datapoints": 3,
      "n_components": 1,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
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
            "min": 298.15,
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 308.15
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.4595,
            "max": 1.4645,
            "mean": 1.462,
            "std": 0.0025,
            "n": 3
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.4595,
          "range_max": 1.4645
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
      "declared_system_type": "unary",
      "declared_n_components": 1,
      "declared_compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
          "sample_num": "DOIcompSample_4_1"
        }
      ],
      "parent_n_datapoints": 3,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
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
      "description": "Surface tension of DMSO+water binary mixture; 112 points; x(DMSO) 0.0121\u20130.8945; T 298.15\u2013328.15 K; maximal bubble pressure method (GLOBmeas_36).",
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
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_1_1"
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
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 112,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_10",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_31",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of DMSO+water binary mixture; 33 points; x(DMSO) 0.0121\u20130.7685; T 298.15\u2013308.15 K; P 101.0 kPa; Abbe refractometer (GLOBmeas_163).",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 33,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_1",
          "comp_num_id": "GLOBcomp_31",
          "name": "dimethyl sulfoxide",
          "formula": "C2H6OS",
          "inchi_key": "IAZDPXIOMUYVGZ-UHFFFAOYSA-N",
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_1_1"
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
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
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
            "min": 0.0121,
            "max": 0.7685,
            "n_unique": 11
          },
          "range_min": 0.0121,
          "range_max": 0.7685
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.339,
            "max": 1.47,
            "mean": 1.420136,
            "std": 0.041686,
            "n": 33
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.339,
          "range_max": 1.47
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
          "SMILES": "CS(C)=O",
          "sample_num": "DOIcompSample_1_1"
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
      "parent_n_datapoints": 33,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_11",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_1294",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of diethyl sulfoxide+water binary mixture.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 56,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
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
            "min": 0.0099,
            "max": 0.7123,
            "n_unique": 8
          },
          "range_min": 0.0099,
          "range_max": 0.7123
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
          "meas_num_id": "GLOBmeas_714",
          "meas_ID": "bubblep_ufactor_8",
          "method_standard": null,
          "method_custom": "BUBBLEP:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0344,
            "max": 0.0655,
            "mean": 0.048232,
            "std": 0.00916,
            "n": 56
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0344,
          "range_max": 0.0655
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
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
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
      "parent_n_datapoints": 56,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_12",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_1294",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of diethyl sulfoxide+water binary mixture.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 30,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_2",
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
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
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
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
            "min": 0.0099,
            "max": 0.7741,
            "n_unique": 10
          },
          "range_min": 0.0099,
          "range_max": 0.7741
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.3315,
            "max": 1.466,
            "mean": 1.425617,
            "std": 0.04507,
            "n": 30
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.3315,
          "range_max": 1.466
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
          "comp_num_id": "GLOBcomp_1294",
          "name": "diethyl sulfoxide",
          "formula": "C4H10OS",
          "inchi_key": "CCAFPWNGIUBUSD-UHFFFAOYSA-N",
          "SMILES": "CCS(=O)CC",
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
      "parent_n_datapoints": 30,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_13",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2145",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of dipropyl sulfoxide+water binary mixture.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 63,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
          "sample_num": "DOIcompSample_3_1"
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
            "min": 0.0105,
            "max": 0.6818,
            "n_unique": 9
          },
          "range_min": 0.0105,
          "range_max": 0.6818
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
          "meas_num_id": "GLOBmeas_714",
          "meas_ID": "bubblep_ufactor_8",
          "method_standard": null,
          "method_custom": "BUBBLEP:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0308,
            "max": 0.0523,
            "mean": 0.038037,
            "std": 0.005438,
            "n": 63
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0308,
          "range_max": 0.0523
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
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 63,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_14",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_2145",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of dipropyl sulfoxide+water binary mixture.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 30,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_3",
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
          "sample_num": "DOIcompSample_3_1"
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
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 308.15
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
            "min": 0.0105,
            "max": 0.9002,
            "n_unique": 10
          },
          "range_min": 0.0105,
          "range_max": 0.9002
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.342,
            "max": 1.458,
            "mean": 1.413533,
            "std": 0.042243,
            "n": 30
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.342,
          "range_max": 1.458
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
          "comp_num_id": "GLOBcomp_2145",
          "name": "dipropyl sulfoxide",
          "formula": "C6H14OS",
          "inchi_key": "BQCCJWMQESHLIT-UHFFFAOYSA-N",
          "SMILES": "CCCS(=O)CCC",
          "sample_num": "DOIcompSample_3_1"
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
      "parent_n_datapoints": 30,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_15",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_7698",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_13"
      ],
      "description": "Surface tension of diisopropyl sulfoxide+water binary mixture.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 53,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
          "sample_num": "DOIcompSample_4_1"
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
            "min": 0.0087,
            "max": 0.8899,
            "n_unique": 8
          },
          "range_min": 0.0087,
          "range_max": 0.8899
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
          "meas_num_id": "GLOBmeas_714",
          "meas_ID": "bubblep_ufactor_8",
          "method_standard": null,
          "method_custom": "BUBBLEP:UFactor:8",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Surface tension liquid-gas, N/m",
            "min": 0.0289,
            "max": 0.0525,
            "mean": 0.037625,
            "std": 0.007468,
            "n": 53
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 0.0289,
          "range_max": 0.0525
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
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
          "sample_num": "DOIcompSample_4_1"
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
      "parent_n_datapoints": 53,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    },
    {
      "lit_num_id": "GLOBlit_10766",
      "block_number": "PROPblock_16",
      "BLKsubsys_id": null,
      "system_type": "binary",
      "comp_num_ids": [
        "GLOBcomp_7698",
        "GLOBcomp_1"
      ],
      "prop_num_ids": [
        "GLOBprop_7"
      ],
      "description": "Refractive index of diisopropyl sulfoxide+water binary mixture.",
      "doi": "10.1021/je7001013",
      "lit_id": "2007-mar-ter-0",
      "block_type": "PureOrMixtureData",
      "blocktype_num_id": "GLOBblocktype_1",
      "n_datapoints": 24,
      "n_components": 2,
      "compounds": [
        {
          "org_num": "DOIcomp_4",
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
          "sample_num": "DOIcompSample_4_1"
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
            "max": 308.15,
            "n_unique": 3
          },
          "range_min": 298.15,
          "range_max": 308.15
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
            "min": 0.0087,
            "max": 0.8899,
            "n_unique": 8
          },
          "range_min": 0.0087,
          "range_max": 0.8899
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
          "meas_num_id": "GLOBmeas_163",
          "meas_ID": "abbe_ufactor_4",
          "method_standard": null,
          "method_custom": "ABBE:UFactor:4",
          "range": {
            "BLKprop_id": "BLKprop_1",
            "name": "Refractive index (Na D-line)",
            "min": 1.342,
            "max": 1.4635,
            "mean": 1.413854,
            "std": 0.048453,
            "n": 24
          },
          "uncertainty": {
            "evaluation_method": "Propagation of evaluated standard uncertainties",
            "confidence_level": 95,
            "evaluator": "Data file compiler",
            "assessment_num": "BLKpropAssessment_1_1"
          },
          "range_min": 1.342,
          "range_max": 1.4635
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
          "comp_num_id": "GLOBcomp_7698",
          "name": "2,2'-sulfinylbispropane",
          "formula": "C6H14OS",
          "inchi_key": "WFJXYIUAMJAURQ-UHFFFAOYSA-N",
          "SMILES": "CC(C)S(=O)C(C)C",
          "sample_num": "DOIcompSample_4_1"
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
      "parent_n_datapoints": 24,
      "subsystem_scope": null,
      "subsystem_point_runs": [],
      "subsystem_path_class": null,
      "subsystem_evidence_quality": null,
      "subsystem_condition_ranges": []
    }
  ],
  "data_inspections": [
    {
      "doi": "10.1021/je301171y",
      "block_number": "PROPblock_5",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "mass_fraction_<dimethyl sulfoxide>",
        "temperature_k",
        "pressure_kpa",
        "thermal_conductivity_w_m_k"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "mass_fraction_<dimethyl sulfoxide>": "0.1",
          "temperature_k": "279.63",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.522"
        },
        {
          "BLKpoint_id": "BLKpoint_7",
          "mass_fraction_<dimethyl sulfoxide>": "0.1",
          "temperature_k": "338.6",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.594"
        },
        {
          "BLKpoint_id": "BLKpoint_8",
          "mass_fraction_<dimethyl sulfoxide>": "0.1995",
          "temperature_k": "279.91",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.466"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "mass_fraction_<dimethyl sulfoxide>": "0.1995",
          "temperature_k": "338.93",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.528"
        },
        {
          "BLKpoint_id": "BLKpoint_15",
          "mass_fraction_<dimethyl sulfoxide>": "0.2998",
          "temperature_k": "280.21",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.414"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "mass_fraction_<dimethyl sulfoxide>": "0.2998",
          "temperature_k": "339.37",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.465"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "mass_fraction_<dimethyl sulfoxide>": "0.3967",
          "temperature_k": "279.76",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.366"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "mass_fraction_<dimethyl sulfoxide>": "0.3967",
          "temperature_k": "338.87",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.404"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "mass_fraction_<dimethyl sulfoxide>": "0.5013",
          "temperature_k": "279.57",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.319"
        },
        {
          "BLKpoint_id": "BLKpoint_35",
          "mass_fraction_<dimethyl sulfoxide>": "0.5013",
          "temperature_k": "338.61",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.347"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "mass_fraction_<dimethyl sulfoxide>": "0.599",
          "temperature_k": "280.01",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.282"
        },
        {
          "BLKpoint_id": "BLKpoint_42",
          "mass_fraction_<dimethyl sulfoxide>": "0.599",
          "temperature_k": "338.9",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.299"
        },
        {
          "BLKpoint_id": "BLKpoint_43",
          "mass_fraction_<dimethyl sulfoxide>": "0.6929",
          "temperature_k": "279.37",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.25"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "mass_fraction_<dimethyl sulfoxide>": "0.6929",
          "temperature_k": "338.59",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.261"
        },
        {
          "BLKpoint_id": "BLKpoint_50",
          "mass_fraction_<dimethyl sulfoxide>": "0.7941",
          "temperature_k": "279.69",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.222"
        },
        {
          "BLKpoint_id": "BLKpoint_56",
          "mass_fraction_<dimethyl sulfoxide>": "0.7941",
          "temperature_k": "338.86",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.224"
        },
        {
          "BLKpoint_id": "BLKpoint_57",
          "mass_fraction_<dimethyl sulfoxide>": "0.9",
          "temperature_k": "279.18",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.2"
        },
        {
          "BLKpoint_id": "BLKpoint_63",
          "mass_fraction_<dimethyl sulfoxide>": "0.9",
          "temperature_k": "338.51",
          "pressure_kpa": "100.0",
          "thermal_conductivity_w_m_k": "0.196"
        }
      ],
      "inspection_id": "INSP_37d8a4c5a601",
      "lit_num_id": "GLOBlit_10024"
    },
    {
      "doi": "10.1021/je7001013",
      "block_number": "PROPblock_9",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<dimethyl sulfoxide>",
        "surface_tension_liquidgas_n_m"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.071"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.0612"
        },
        {
          "BLKpoint_id": "BLKpoint_6",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2999",
          "surface_tension_liquidgas_n_m": "0.0533"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4523",
          "surface_tension_liquidgas_n_m": "0.0503"
        },
        {
          "BLKpoint_id": "BLKpoint_13",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.046"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.042"
        },
        {
          "BLKpoint_id": "BLKpoint_17",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.0701"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.0606"
        },
        {
          "BLKpoint_id": "BLKpoint_20",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1979",
          "surface_tension_liquidgas_n_m": "0.0558"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2999",
          "surface_tension_liquidgas_n_m": "0.0524"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4523",
          "surface_tension_liquidgas_n_m": "0.0499"
        },
        {
          "BLKpoint_id": "BLKpoint_28",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.501",
          "surface_tension_liquidgas_n_m": "0.0474"
        },
        {
          "BLKpoint_id": "BLKpoint_29",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.0452"
        },
        {
          "BLKpoint_id": "BLKpoint_32",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.0414"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.0692"
        },
        {
          "BLKpoint_id": "BLKpoint_35",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.0598"
        },
        {
          "BLKpoint_id": "BLKpoint_36",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1979",
          "surface_tension_liquidgas_n_m": "0.0548"
        },
        {
          "BLKpoint_id": "BLKpoint_38",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2999",
          "surface_tension_liquidgas_n_m": "0.0515"
        },
        {
          "BLKpoint_id": "BLKpoint_43",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4523",
          "surface_tension_liquidgas_n_m": "0.0491"
        },
        {
          "BLKpoint_id": "BLKpoint_44",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.501",
          "surface_tension_liquidgas_n_m": "0.0467"
        },
        {
          "BLKpoint_id": "BLKpoint_45",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.0446"
        },
        {
          "BLKpoint_id": "BLKpoint_46",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7027",
          "surface_tension_liquidgas_n_m": "0.0426"
        },
        {
          "BLKpoint_id": "BLKpoint_48",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.0409"
        },
        {
          "BLKpoint_id": "BLKpoint_49",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.0676"
        },
        {
          "BLKpoint_id": "BLKpoint_51",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.0587"
        },
        {
          "BLKpoint_id": "BLKpoint_52",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1979",
          "surface_tension_liquidgas_n_m": "0.0539"
        },
        {
          "BLKpoint_id": "BLKpoint_54",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2999",
          "surface_tension_liquidgas_n_m": "0.0506"
        },
        {
          "BLKpoint_id": "BLKpoint_59",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4523",
          "surface_tension_liquidgas_n_m": "0.0482"
        },
        {
          "BLKpoint_id": "BLKpoint_61",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.0438"
        },
        {
          "BLKpoint_id": "BLKpoint_64",
          "temperature_k": "313.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.0403"
        },
        {
          "BLKpoint_id": "BLKpoint_65",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.0664"
        },
        {
          "BLKpoint_id": "BLKpoint_67",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.0579"
        },
        {
          "BLKpoint_id": "BLKpoint_69",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2507",
          "surface_tension_liquidgas_n_m": "0.0512"
        },
        {
          "BLKpoint_id": "BLKpoint_70",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3218",
          "surface_tension_liquidgas_n_m": "0.0507"
        },
        {
          "BLKpoint_id": "BLKpoint_77",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.0431"
        },
        {
          "BLKpoint_id": "BLKpoint_80",
          "temperature_k": "318.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.0398"
        },
        {
          "BLKpoint_id": "BLKpoint_81",
          "temperature_k": "323.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.0653"
        },
        {
          "BLKpoint_id": "BLKpoint_83",
          "temperature_k": "323.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.057"
        },
        {
          "BLKpoint_id": "BLKpoint_85",
          "temperature_k": "323.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2507",
          "surface_tension_liquidgas_n_m": "0.0503"
        },
        {
          "BLKpoint_id": "BLKpoint_86",
          "temperature_k": "323.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3218",
          "surface_tension_liquidgas_n_m": "0.0499"
        },
        {
          "BLKpoint_id": "BLKpoint_93",
          "temperature_k": "323.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.0423"
        },
        {
          "BLKpoint_id": "BLKpoint_96",
          "temperature_k": "323.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.0392"
        },
        {
          "BLKpoint_id": "BLKpoint_97",
          "temperature_k": "328.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "surface_tension_liquidgas_n_m": "0.0651"
        },
        {
          "BLKpoint_id": "BLKpoint_99",
          "temperature_k": "328.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1044",
          "surface_tension_liquidgas_n_m": "0.0551"
        },
        {
          "BLKpoint_id": "BLKpoint_101",
          "temperature_k": "328.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2507",
          "surface_tension_liquidgas_n_m": "0.0494"
        },
        {
          "BLKpoint_id": "BLKpoint_102",
          "temperature_k": "328.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3218",
          "surface_tension_liquidgas_n_m": "0.049"
        },
        {
          "BLKpoint_id": "BLKpoint_104",
          "temperature_k": "328.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3549",
          "surface_tension_liquidgas_n_m": "0.0474"
        },
        {
          "BLKpoint_id": "BLKpoint_109",
          "temperature_k": "328.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.59",
          "surface_tension_liquidgas_n_m": "0.0417"
        },
        {
          "BLKpoint_id": "BLKpoint_112",
          "temperature_k": "328.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.8945",
          "surface_tension_liquidgas_n_m": "0.0387"
        }
      ],
      "inspection_id": "INSP_507097ca3b25",
      "lit_num_id": "GLOBlit_10766"
    },
    {
      "doi": "10.1021/je7001013",
      "block_number": "PROPblock_10",
      "table_mode": "rdp",
      "columns": [
        "BLKpoint_id",
        "temperature_k",
        "mole_fraction_<dimethyl sulfoxide>",
        "pressure_kpa",
        "refractive_index_na_dline"
      ],
      "rows_shown": [
        {
          "BLKpoint_id": "BLKpoint_1",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.34"
        },
        {
          "BLKpoint_id": "BLKpoint_3",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1467",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.396"
        },
        {
          "BLKpoint_id": "BLKpoint_5",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2959",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4305"
        },
        {
          "BLKpoint_id": "BLKpoint_9",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.4301",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4475"
        },
        {
          "BLKpoint_id": "BLKpoint_10",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.5964",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.461"
        },
        {
          "BLKpoint_id": "BLKpoint_11",
          "temperature_k": "298.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7685",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.47"
        },
        {
          "BLKpoint_id": "BLKpoint_12",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.339"
        },
        {
          "BLKpoint_id": "BLKpoint_14",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1467",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4005"
        },
        {
          "BLKpoint_id": "BLKpoint_16",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2959",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4295"
        },
        {
          "BLKpoint_id": "BLKpoint_19",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3967",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.443"
        },
        {
          "BLKpoint_id": "BLKpoint_21",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.5964",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.459"
        },
        {
          "BLKpoint_id": "BLKpoint_22",
          "temperature_k": "303.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7685",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.468"
        },
        {
          "BLKpoint_id": "BLKpoint_23",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.0121",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.3395"
        },
        {
          "BLKpoint_id": "BLKpoint_25",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.1467",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.4"
        },
        {
          "BLKpoint_id": "BLKpoint_27",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.2959",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.428"
        },
        {
          "BLKpoint_id": "BLKpoint_30",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.3967",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.442"
        },
        {
          "BLKpoint_id": "BLKpoint_32",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.5964",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.458"
        },
        {
          "BLKpoint_id": "BLKpoint_33",
          "temperature_k": "308.15",
          "mole_fraction_<dimethyl sulfoxide>": "0.7685",
          "pressure_kpa": "101.0",
          "refractive_index_na_dline": "1.466"
        }
      ],
      "inspection_id": "INSP_2257cf4faf77",
      "lit_num_id": "GLOBlit_10766"
    }
  ]
}
</subagent_answer>
```
</details>

---

## Nested tool calls — L1_1 (L1-query)

**Nest:** A - L1_1
**Parent:** `query_thermoml` — Step 5 [A · c14] relays this worker's result
**Started:** 06:25:57  |  **Ended:** 06:32:38  |  **Tool calls:** 9

---

### Step 2 [A - L1_1 · c5]: `resolve_compound_ids`

<details><summary>Arguments</summary>

```json
{
  "queries": [
    "dimethyl sulfoxide",
    "water"
  ],
  "min_score": 70,
  "limit": 5,
  "purpose": "Resolve DMSO and water to global compound IDs",
  "tasks": "Find GLOBcomp IDs for dimethyl sulfoxide and water"
}
```
</details>

- **Result:** 200 chars  |  **Time:** 3.9s  |  **Started:** 06:26:08 (t+70.5s)
- **Subagent:** KEEP in 295 → 200 chars (3.8s)
  - Both compounds resolved with exact name matches.

| Compound | Global ID | Formula | SMILES |
|---|---|---|---|
| dimethyl sulfoxide | GLOBcomp_31 | C2H6OS | CS(C)=O |
| water | GLOBcomp_1 | H2O | O |

<details><summary>Result</summary>

```
Both compounds resolved with exact name matches.

| Compound | Global ID | Formula | SMILES |
|---|---|---|---|
| dimethyl sulfoxide | GLOBcomp_31 | C2H6OS | CS(C)=O |
| water | GLOBcomp_1 | H2O | O |
```
</details>

---

### Step 4 [A - L1_1 · c6]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_31",
    "GLOBcomp_1"
  ],
  "system_type": "binary",
  "temperature_range": [
    288,
    313
  ],
  "limit": 50,
  "purpose": "Find all thermophysical property data for DMSO+water binary mixtures near room temperature",
  "tasks": "Search for binary mixture blocks containing both DMSO and water in 288-313 K range, returning DOIs, block numbers, property types, temperature ranges, composition ranges, and data point counts"
}
```
</details>

- **Result:** 1,264 chars  |  **Time:** 16.2s  |  **Started:** 06:26:28 (t+90.7s)
- **Subagent:** KEEP in 12,628 → 1,249 chars (15.6s)
  - **Summary:** 19 property blocks found for DMSO (GLOBcomp_31) + water (GLOBcomp_1) binary mixtures in the 288–313 K range, spanning 10 distinct properties across 9 DOIs. All are liquid-phase data with 

<details><summary>Result</summary>

```
**Summary:** 19 property blocks found for DMSO (GLOBcomp_31) + water (GLOBcomp_1) binary mixtures in the 288–313 K range, spanning 10 distinct properties across 9 DOIs. All are liquid-phase data with uncertainty reported at 95% confidence.

| # | DOI | Block | Property | GLOBprop | T range (K) | Composition range | Pts (orig) | Pts (kept) | GLOBlit |
|---|-----|-------|----------|----------|-------------|-------------------|------------|------------|---------|
| 1 | 10.1016/j.jct.2005.07.012 | PROPblock_8 | Mass density, kg/m³ | GLOBprop_1 | 288.15–298.15 | x(water) 0.0308–0.9798 | 96 | 15 | GLOBlit_2584 |
| 2 | 10.1016/j.jct.2006.01.007 | PROPblock_3 | Speed of sound, m/s | GLOBprop_8 | 288.15–313.15 | fixed x (constr) | 6 | 6 | GLOBlit_2652 |
| 3 | 10.1016/j.jct.2006.01.007 | PROPblock_4 | Mass density, kg/m³ | GLOBprop_1 | 288.15–313.15 | fixed x (constr) | 6 | 5 | GLOBlit_2652 |
| 4 | 10.1016/j.jct.2006.12.012 | PROPblock_3 | Viscosity, Pa·s | GLOBprop_4 | 298.15–308.15 | x(DMSO) 0–1 | 120 | 17 | GLOBlit_2781 |
| 5 | 10.1016/j.jct.2006.12.012 | PROPblock_4 | Mass density, kg/m³ | GLOBprop_1 | 298.15–308.15 | x(DMSO) 0–1 | 120 | 14 | GLOBlit_2781 |
| 6 | 10.1016/j.jct.2007.06.010 [GLOBlit_2844] | PROPblock_3 | Apparent molar Cp, J/K/mol | GL
```
</details>

---

### Step 5 [A - L1_1 · c7]: `search_system_registry`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_31",
    "GLOBcomp_1"
  ],
  "system_type": "binary",
  "temperature_range": [
    288,
    313
  ],
  "limit": 50,
  "purpose": "Find all DMSO+water binary blocks near room temperature",
  "tasks": "List all available property blocks with DOIs, properties, temperature ranges, and data point counts"
}
```
</details>

- **Result:** 1,176 chars  |  **Time:** 16.2s  |  **Started:** 06:26:53 (t+116.3s)
- **Subagent:** KEEP in 3,070 → 996 chars (12.7s)
  - **Summary:** 19 DMSO (GLOBcomp_31) + water (GLOBcomp_1) binary property blocks were found across 10 DOIs in the 288–313 K window, totaling 1,425 data points. However, the block detail sections are emp

<details><summary>Result</summary>

```
**Summary:** 19 DMSO (GLOBcomp_31) + water (GLOBcomp_1) binary property blocks were found across 10 DOIs in the 288–313 K window, totaling 1,425 data points. However, the block detail sections are empty — property names and exact temperature ranges are not included in this result.

| # | DOI | Block | Points |
|---|-----|-------|--------|
| 1 | 10.1016/j.jct.2005.07.012 [GLOBlit_2584] | PROPblock_8 | 96 |
| 2 | 10.1016/j.jct.2006.01.007 [GLOBlit_2652] | PROPblock_3 | 6 |
| 3 | 10.1016/j.jct.2006.01.007 [GLOBlit_2652] | PROPblock_4 | 6 |
| 4 | 10.1016/j.jct.2006.12.012 [GLOBlit_2781] | PROPblock_3 | 120 |
| 5 | 10.1016/j.jct.2006.12.012 [GLOBlit_2781] | PROPblock_4 | 120 |
| 6 | 10.1016/j.jct.2007.06.010 [GLOBlit_2844] | PROPblock_3 | 216 |
| 7 | 10.1016/j.jct.2007.06.010 [GLOBlit_2844] | PROPblock_4 | 92 |
| 8 | 10.1016/j.tca.2011.08.013 [GLOBlit_5953] | PROPblock_10 | 16 |
| 9 | 10.1016/j.tca.2011.08.013 [GLOBlit_5953] | PROPblock_11 | 16 |
| 10 | 10.1016/j.tca.2011.08.013 [GLOBlit_5953] | PROPblock_12 | 16 |
| 11 | 10.1016/j.tca.2011.09.009 [GLOBlit_5958] | PROPblock_1 | 1 |
| 12 | 10.1021/acs.jced.8b01048 [GLOBlit_7713] | PROPblock_10 | 9 |
| 13 | 10.1021
```
</details>

---

### Step 6 [A - L1_1 · c8]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_31",
    "GLOBcomp_1"
  ],
  "system_type": "binary",
  "temperature_range": [
    288,
    313
  ],
  "limit": 50,
  "purpose": "Get complete listing of all DMSO+water binary blocks in 288-313 K",
  "tasks": "Return all 19 blocks with property types, temperature ranges, composition ranges, and data point counts"
}
```
</details>

- **Result:** 1,212 chars  |  **Time:** 14.1s  |  **Started:** 06:27:30 (t+153.2s)
- **Subagent:** KEEP in 12,628 → 1,197 chars (13.4s)
  - All 19 DMSO+water binary blocks in the 288–313 K window were returned. Below is the complete listing with property, temperature range, composition range, and point counts.

| # | DOI | Block | Propert

<details><summary>Result</summary>

```
All 19 DMSO+water binary blocks in the 288–313 K window were returned. Below is the complete listing with property, temperature range, composition range, and point counts.

| # | DOI | Block | Property | T (K) | Composition | Pts | GLOBlit |
|---|-----|-------|----------|-------|-------------|-----|---------|
| 1 | 10.1016/j.jct.2005.07.012 | PROPblock_8 | Mass density (GLOBprop_1) | 288.15–298.15 | x(water) 0.0308–0.9798 | 96 | GLOBlit_2584 |
| 2 | 10.1016/j.jct.2006.01.007 | PROPblock_3 | Speed of sound (GLOBprop_8) | 288.15–313.15 | fixed x(DMSO) | 6 | GLOBlit_2652 |
| 3 | 10.1016/j.jct.2006.01.007 | PROPblock_4 | Mass density (GLOBprop_1) | 288.15–313.15 | fixed x(DMSO) | 6 | GLOBlit_2652 |
| 4 | 10.1016/j.jct.2006.12.012 | PROPblock_3 | Viscosity (GLOBprop_4) | 298.15–308.15 | x(DMSO) 0–1 | 120 | GLOBlit_2781 |
| 5 | 10.1016/j.jct.2006.12.012 | PROPblock_4 | Mass density (GLOBprop_1) | 298.15–308.15 | x(DMSO) 0–1 | 120 | GLOBlit_2781 |
| 6 | 10.1016/j.jct.2007.06.010 | PROPblock_3 | Apparent molar Cp (GLOBprop_64) | 278.15–303.15 | b(DMSO) 0.0205–2.9997 | 216 | GLOBlit_2844 |
| 7 | 10.1016/j.jct.2007.06.010 [GLOBlit_2844] | PROPblock_4 | Mass density (GLOBprop_1) | 278.15–368.15 | b(DMSO)
```
</details>

---

### Step 7 [A - L1_1 · c9]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_31",
    "GLOBcomp_1"
  ],
  "system_type": "binary",
  "literature": [
    "GLOBlit_5953",
    "GLOBlit_5958",
    "GLOBlit_7713"
  ],
  "temperature_range": [
    288,
    313
  ],
  "limit": 50,
  "purpose": "Get property details for remaining DMSO+water blocks",
  "tasks": "Retrieve property types, temperature ranges, composition ranges for blocks from GLOBlit_5953, GLOBlit_5958, GLOBlit_7713"
}
```
</details>

- **Result:** 1,122 chars  |  **Time:** 15.5s  |  **Started:** 06:28:04 (t+186.8s)
- **Subagent:** KEEP in 5,878 → 1,122 chars (15.4s)
  - All 3 blocks returned are from **GLOBlit_5953** (DOI: 10.1016/j.tca.2011.08.013). No blocks matched from GLOBlit_5958 or GLOBlit_7713 within the given temperature/composition filters. The blocks cover

<details><summary>Result</summary>

```
All 3 blocks returned are from **GLOBlit_5953** (DOI: 10.1016/j.tca.2011.08.013). No blocks matched from GLOBlit_5958 or GLOBlit_7713 within the given temperature/composition filters. The blocks cover dilute DMSO in water (x = 0.0121–0.0583) at 303.15–318.15 K.

| Block | Property | prop_num_id | Method | x(DMSO) range | T (K) range | Pts | Phase |
|---|---|---|---|---|---|---|---|
| PROPblock_10 | viscosity_pa_s | GLOBprop_4 | capillary_tube_ostwald_ubbelohde | 0.0121–0.0583 | 303.15–318.15 | 16 (13 kept) | Liquid |
| PROPblock_11 | speed_of_sound_m_s | GLOBprop_8 | linear_variable_path_acoustic_interferometer | 0.0121–0.0583 | 303.15–318.15 | 16 (13 kept) | Liquid |
| PROPblock_12 | mass_density_kg_m3 | GLOBprop_1 | pycnometric_method | 0.0121–0.0583 | 303.15–318.15 | 16 (12 kept) | Liquid |

**Common metadata:**
- Constraint: BLKconstr_1 → pressure_kpa = 101.0 (GLOBconstr_1)
- Variables: BLKvar_1 = mole_fraction (GLOBvar_2), BLKvar_2 = temperature_k (GLOBvar_1)
- Compounds: DOIcomp_2 = GLOBcomp_31 (DMSO), DOIcomp_3 = GLOBcomp_1 (water)
- Uncertainty: k=95%, Propagation, compiler

**Note:** GLOBlit_5958
```
</details>

---

### Step 8 [A - L1_1 · c10]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_31",
    "GLOBcomp_1"
  ],
  "system_type": "binary",
  "literature": [
    "GLOBlit_5958",
    "GLOBlit_7713"
  ],
  "limit": 50,
  "purpose": "Find remaining DMSO+water blocks from GLOBlit_5958 and GLOBlit_7713",
  "tasks": "Get property details for blocks not yet retrieved"
}
```
</details>

- **Result:** 1,033 chars  |  **Time:** 11.7s  |  **Started:** 06:28:30 (t+212.6s)
- **Subagent:** KEEP in 1,762 → 1,033 chars (11.6s)
  - Only 1 block found from GLOBlit_5958; **no blocks from GLOBlit_7713** matched the binary DMSO+water search. The single block is a molar enthalpy of solution measurement (1 data point).

### PROPblock_

<details><summary>Result</summary>

```
Only 1 block found from GLOBlit_5958; **no blocks from GLOBlit_7713** matched the binary DMSO+water search. The single block is a molar enthalpy of solution measurement (1 data point).

### PROPblock_1 — GLOBlit_5958 (10.1016/j.tca.2011.09.009)

| Field | Value |
|---|---|
| **Property** | Molar enthalpy of solution (BLKprop_1 → GLOBprop_15) |
| **Method** | Isoperibol (GLOBmeas_144) |
| **Group** | ExcessPartialApparentEnergyProp |
| **Phase** | Liquid |
| **Ref state** | Pure solute at same T and P |
| **Solvent** | DOIcomp_1 → GLOBcomp_31 (DMSO) |
| **Solute** | DOIcomp_2 → GLOBcomp_1 (water) |
| **Points** | 1 |

| b(water, mol/kg) | P (kPa) | T (K) | ΔH_sol (kJ/mol) | ±U |
|---|---|---|---|---|
| 0.092 | 101.0 | 298.15 | -5.38 | 0.11 |

### Variables
- BLKvar_1 → GLOBvar_4: molality of water
- BLKvar_2 → GLOBvar_3: pressure (kPa)
- BLKvar_3 → GLOBvar_1: temperature (K)

**Note:** GLOBlit_7713 returned zero blocks for this binary system query. It may contain data under a different system scope or compound pairing.
```
</details>

---

### Step 9 [A - L1_1 · c11]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_31",
    "GLOBcomp_1"
  ],
  "literature": [
    "GLOBlit_7713"
  ],
  "temperature_range": [
    288,
    313
  ],
  "purpose": "Find DMSO+water blocks from GLOBlit_7713",
  "tasks": "Search without system_type filter to find any blocks"
}
```
</details>

- **Result:** 916 chars  |  **Time:** 15.7s  |  **Started:** 06:28:48 (t+231.4s)
- **Subagent:** KEEP in 7,913 → 901 chars (15.3s)
  - **Summary:** GLOBlit_7713 (DOI: 10.1021/acs.jced.8b01048) contains one true binary DMSO+water block (**PROPblock_10**) with 9 density points for x(DMSO)=0.998 from 293.15–373.15 K. Two ternary blocks 

<details><summary>Result</summary>

```
**Summary:** GLOBlit_7713 (DOI: 10.1021/acs.jced.8b01048) contains one true binary DMSO+water block (**PROPblock_10**) with 9 density points for x(DMSO)=0.998 from 293.15–373.15 K. Two ternary blocks (PROPblock_3, PROPblock_4) also contain DMSO+water but as part of ionic-liquid ternary mixtures. Within the 288–313 K window, PROPblock_10 has 3 data points.

### PROPblock_10 — Binary DMSO+water density (GLOBlit_7713)

| Field | Value |
|---|---|
| DOI | 10.1021/acs.jced.8b01048 [GLOBlit_7713] |
| Block | PROPblock_10 |
| System | binary |
| Compounds | DOIcomp_3 → GLOBcomp_31 (DMSO), DOIcomp_4 → GLOBcomp_1 (water) |
| Property | BLKprop_1 → GLOBprop_1 mass_density_kg_m3, GLOBmeas_2 vibrating_tube_method, Liquid |
| Constraint | BLKconstr_1: x(DMSO)=0.998; BLKconstr_2: P=100.0 kPa |
| Points | 9 total (3 in 288–313 K range) |

**Data (all 8 kept points):**

| T (K) | ρ (kg/m³) | ±U |
|---|---|---|
| 293.15
```
</details>

---

### Step 10 [A - L1_1 · c12]: `search_system_summary`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_31",
    "GLOBcomp_1"
  ],
  "system_type": "binary",
  "temperature_range": [
    288,
    313
  ],
  "purpose": "Count all DMSO+water binary blocks in 288-313K",
  "tasks": "Get total count and property breakdown"
}
```
</details>

- **Result:** 1,270 chars  |  **Time:** 19.5s  |  **Started:** 06:29:21 (t+263.8s)
- **Subagent:** KEEP in 1,070 → 1,270 chars (12.6s)
  - **Summary:** The DMSO (GLOBcomp_31) + water (GLOBcomp_1) binary system search in 288–313 K returned **19 target blocks** across **12 papers**, with **1425 matching data points**. Mass density dominate

<details><summary>Result</summary>

```
**Summary:** The DMSO (GLOBcomp_31) + water (GLOBcomp_1) binary system search in 288–313 K returned **19 target blocks** across **12 papers**, with **1425 matching data points**. Mass density dominates with 8 blocks; transport and other thermophysical properties make up the rest.

### Property Breakdown

| Property | Block count |
|----------|------------|
| Mass density, kg/m³ | 8 |
| Viscosity, Pa·s | 3 |
| Speed of sound, m/s | 2 |
| Apparent molar heat capacity, J/K/mol | 1 |
| Molar enthalpy of solution, kJ/mol | 1 |
| Thermal conductivity, W/m/K | 1 |
| Relative permittivity at zero frequency | 1 |
| Surface tension liquid-gas, N/m | 1 |
| Refractive index (Na D-line) | 1 |

### Top Papers by Matching Points (5 of 12 shown)

| lit_num_id | DOI | Blocks | Targets | Matching pts |
|------------|-----|--------|---------|-------------|
| GLOBlit_10109 | 10.1021/je400149j | 1 | 1 | 363 |
| GLOBlit_2844 | 10.1016/j.jct.2007.06.010 | 2 | 2 | 308 |
| GLOBlit_2781 | 10.1016/j.jct.2006.12.012 | 2 | 2 | 240 |
| GLOBlit_10766 | 10.1021/je7001013 | 2 | 2 | 145 |
| GLOBlit_2584 | 10.1016/j.jct.2005.07.012 | 1 | 1 | 96 |

**Totals:** 19 blocks, 19 targets, 1425 matching points, 12 papers. Note: the raw block-level T range spans [253.15, 393.15] K overall, but
```
</details>

---

### Step 11 [A - L1_1 · c13]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_31",
    "GLOBcomp_1"
  ],
  "system_type": "binary",
  "literature": [
    "GLOBlit_10109",
    "GLOBlit_10766"
  ],
  "temperature_range": [
    288,
    313
  ],
  "limit": 10,
  "purpose": "Get details for remaining DMSO+water binary blocks",
  "tasks": "Retrieve property, T range, composition, and point counts for blocks from GLOBlit_10109 and GLOBlit_10766"
}
```
</details>

- **Result:** 1,210 chars  |  **Time:** 17.8s  |  **Started:** 06:29:49 (t+292.3s)
- **Subagent:** KEEP in 3,380 → 1,194 chars (17.3s)
  - **Summary:** Only 1 block was returned from GLOBlit_10109 (relative permittivity of DMSO+water). No blocks from GLOBlit_10766 were found — the temperature filter (288–313 K) or other criteria may have

<details><summary>Result</summary>

```
**Summary:** Only 1 block was returned from GLOBlit_10109 (relative permittivity of DMSO+water). No blocks from GLOBlit_10766 were found — the temperature filter (288–313 K) or other criteria may have excluded it.

### Block Details

| Field | Value |
|---|---|
| **Block** | PROPblock_5 |
| **DOI** | 10.1021/je400149j [GLOBlit_10109] |
| **Literature** | GLOBlit_10109 |
| **Property** | Relative permittivity at zero frequency (BLKprop_1 → GLOBprop_44) |
| **Method** | impedance_gain_phase_analyzer (GLOBmeas_823) |
| **Phase** | Liquid |
| **Total pts** | 363 (50 kept after RDP) |
| **T range** | 253.15–301.15 K |
| **x(DMSO) values** | 0.0, 0.1536, 0.2496 |
| **Pressure** | 101.0 kPa (BLKconstr_1) |
| **Compounds** | DOIcomp_1 = GLOBcomp_31 (DMSO), DOIcomp_2 = GLOBcomp_1 (water) |

### Variables & Constraints

| ID | Type | Details |
|---|---|---|
| BLKvar_1 | temperature_k (GLOBvar_1) | Liquid phase |
| BLKvar_2 | mole_fraction_DOIcomp_1 (GLOBvar_2) | DMSO, Liquid phase |
| BLKconstr_1 | pressure_kpa (GLOBconstr_1) | 101.0 kPa |

### Note on GLOBlit_10766
No blocks returned. The applied temperature filter (288–313 K) may be too restrictive, or GLOBlit_10766 may not contain binary DMSO+water
```
</details>

---

## Nested tool calls — L1_2 (L1-query)

**Nest:** A - L1_2
**Parent:** `query_thermoml` — Step 25 [A · c42] relays this worker's result
**Started:** 06:35:29  |  **Ended:** 06:40:54  |  **Tool calls:** 8

---

### Step 2 [A - L1_2 · c34]: `resolve_property_ids`

<details><summary>Arguments</summary>

```json
{
  "queries": "thermal conductivity",
  "min_score": 50,
  "limit": 5,
  "purpose": "Resolve thermal conductivity property ID",
  "tasks": "Find GLOBprop ID for thermal conductivity"
}
```
</details>

- **Result:** 239 chars  |  **Time:** 5.1s  |  **Started:** 06:35:40 (t+643.0s)
- **Subagent:** KEEP in 226 → 239 chars (4.5s)
  - **Summary:** Thermal conductivity resolves to **GLOBprop_34** (Thermal conductivity, W/m/K) with an exact match (score 100).

| Property | ID | Unit | Group |
|---|---|---|---|
| Thermal conductivity 

<details><summary>Result</summary>

```
**Summary:** Thermal conductivity resolves to **GLOBprop_34** (Thermal conductivity, W/m/K) with an exact match (score 100).

| Property | ID | Unit | Group |
|---|---|---|---|
| Thermal conductivity | GLOBprop_34 | W/m/K | TransportProp |
```
</details>

---

### Step 3 [A - L1_2 · c35]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_31",
    "GLOBcomp_1"
  ],
  "property": "GLOBprop_34",
  "system_type": "binary",
  "limit": 50,
  "purpose": "Find DMSO+water thermal conductivity blocks",
  "tasks": "Search for binary blocks with DMSO and water measuring thermal conductivity"
}
```
</details>

- **Result:** 1,265 chars  |  **Time:** 14.1s  |  **Started:** 06:35:53 (t+656.2s)
- **Subagent:** KEEP in 2,121 → 1,249 chars (13.7s)
  - **Summary:** One binary DMSO+water thermal conductivity block found: **PROPblock_5** (DOI `10.1021/je301171y`, GLOBlit_10024), containing 63 data points (15 shown after RDP compression) of liquid-phas

<details><summary>Result</summary>

```
**Summary:** One binary DMSO+water thermal conductivity block found: **PROPblock_5** (DOI `10.1021/je301171y`, GLOBlit_10024), containing 63 data points (15 shown after RDP compression) of liquid-phase thermal conductivity measured by hot-wire method at 100 kPa, covering w(DMSO) = 0.1–0.7941 and T = 279–339 K.

### Block Details

| Field | Value |
|---|---|
| Block | PROPblock_5 |
| DOI | 10.1021/je301171y [GLOBlit_10024] |
| lit_id | GLOBlit_10024 |
| System | binary (DMSO + water) |
| Total pts | 63 |
| Property | BLKprop_1 → GLOBprop_34, thermal conductivity (W/m/K), Liquid |
| Method | GLOBmeas_41, hot_wire_method |
| Variables | BLKvar_1: mass_fraction of DOIcomp_3 (GLOBcomp_31, DMSO); BLKvar_2: temperature_k |
| Constraint | BLKconstr_1: pressure_kpa = 100.0 |
| Compounds | DOIcomp_1 → GLOBcomp_1 (water); DOIcomp_3 → GLOBcomp_31 (DMSO) |

### Sample Data (15 pts, RDP-compressed)

| w(DMSO, Liq) | T (K) | λ (W/m/K) | ±U |
|---|---|---|---|
| 0.1 | 279.63 | 0.522 | 0.011 |
| 0.1 | 338.6 | 0.594 | 0.012 |
| 0.1995 | 279.91 | 0.466 | 0.009 |
| 0.1995 | 338.93 | 0.528 | 0.011 |
| 0.2998 | 280.21 | 0.414 | 0.008 |
| 0.2998 | 339.37 | 0.465 | 0.009 |
| 0.3967 | 279.76 | 0.366 | 0.007 |
| 0.3967 | 338.87 | 0.404 | 0.008 |
| 0.5013 | 279.57 | 0.319
```
</details>

---

### Step 4 [A - L1_2 · c36]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_31",
    "GLOBcomp_1"
  ],
  "property": "GLOBprop_13",
  "system_type": "binary",
  "limit": 50,
  "purpose": "Find DMSO+water binary surface tension blocks",
  "tasks": "Search for surface tension data in DMSO+water binary mixtures"
}
```
</details>

- **Result:** 1,285 chars  |  **Time:** 18.8s  |  **Started:** 06:36:21 (t+684.2s)
- **Subagent:** KEEP in 2,393 → 1,269 chars (12.6s)
  - **Summary:** One surface tension block found for the DMSO + water binary system: **PROPblock_9** from DOI `10.1021/je7001013` (GLOBlit_10766), containing 112 total data points (25 shown after RDP comp

<details><summary>Result</summary>

```
**Summary:** One surface tension block found for the DMSO + water binary system: **PROPblock_9** from DOI `10.1021/je7001013` (GLOBlit_10766), containing 112 total data points (25 shown after RDP compression) covering T = 298.15–313.15 K and x(DMSO) = 0.0121–0.8945, measured by maximal bubble pressure.

### Block Details

| Field | Value |
|---|---|
| **Block** | PROPblock_9 |
| **DOI** | 10.1021/je7001013 [GLOBlit_10766] |
| **lit_id** | GLOBlit_10766 |
| **Total pts** | 112 |
| **Property** | BLKprop_1 → GLOBprop_13, surface_tension_liquidgas_n_m |
| **Method** | GLOBmeas_36, maximal_bubble_pressure |
| **Phase** | Liquid; Air at 1 atm |
| **Compounds** | DOIcomp_1 = GLOBcomp_31 (DMSO), DOIcomp_5 = GLOBcomp_1 (water) |
| **Variables** | BLKvar_1 = GLOBvar_1 (temperature_k), BLKvar_2 = GLOBvar_2 (mole_fraction of DOIcomp_1) |
| **T range** | 298.15–313.15 K |
| **x(DMSO) range** | 0.0121–0.8945 |
| **Uncertainty** | k=95%, Propagation, compiler; ±U = 0.0003–0.0005 N/m |

### Sample Data (25 pts, RDP-compressed)

| T (K) | x(DMSO) | γ (N/m) | ±U |
|---|---|---|---|
| 298.15 | 0.0121 | 0.071 | 0.0005 |
| 298.15 | 0.1044 | 0.0612 | 0.0004 |
| 298.15 | 0.2999 | 0.0533 | 0.0004 |
| 298.15 | 0.4523 | 0.0503 | 0.0004 |
| 298.15 | 0.59 | 0.046 | 0.0004 |
| 298.15 | 0.8945
```
</details>

---

### Step 5 [A - L1_2 · c37]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_31",
    "GLOBcomp_1"
  ],
  "property": "GLOBprop_7",
  "system_type": "binary",
  "limit": 50,
  "purpose": "Find refractive index blocks for DMSO+water binary",
  "tasks": "Search for binary blocks with DMSO and water measuring refractive index"
}
```
</details>

- **Result:** 1,131 chars  |  **Time:** 18.4s  |  **Started:** 06:36:45 (t+708.3s)
- **Subagent:** KEEP in 2,265 → 1,115 chars (12.2s)
  - **Summary:** One binary block found for refractive index (Na D-line) of DMSO + water: **PROPblock_10** from DOI `10.1021/je7001013` (GLOBlit_10766), containing 33 data points at 298.15–308.15 K and x(

<details><summary>Result</summary>

```
**Summary:** One binary block found for refractive index (Na D-line) of DMSO + water: **PROPblock_10** from DOI `10.1021/je7001013` (GLOBlit_10766), containing 33 data points at 298.15–308.15 K and x(DMSO) = 0.0121–0.7685, measured at 101.0 kPa in the liquid phase.

| Field | Value |
|---|---|
| **DOI** | 10.1021/je7001013 [GLOBlit_10766] |
| **Block** | PROPblock_10 |
| **lit_id** | GLOBlit_10766 |
| **Property** | BLKprop_1 → GLOBprop_7 (refractive_index_na_dline), Liquid |
| **Method** | GLOBmeas_163 (abbe_ufactor_4) |
| **Compounds** | DOIcomp_1 = GLOBcomp_31 (DMSO), DOIcomp_5 = GLOBcomp_1 (water) |
| **Variables** | BLKvar_1 = GLOBvar_1 (temperature_k), BLKvar_2 = GLOBvar_2 (mole_fraction of DOIcomp_1) |
| **Constraint** | BLKconstr_1 = GLOBconstr_1 (pressure_kpa = 101.0) |
| **Points** | 33 total, T: 298.15–308.15 K, x(DMSO): 0.0121–0.7685 |

**Data (18 pts after RDP):**

| T (K) | x(DMSO) | n_D | ±U |
|---|---|---|---|
| 298.15 | 0.0121 | 1.34 | 0.0015 |
| 298.15 | 0.1467 | 1.396 | 0.0025 |
| 298.15 | 0.2959 | 1.4305 | 0.0015 |
| 298.15 | 0.4301 | 1.4475 | 0.0016 |
| 298.15 | 0.5964 | 1.461 | 0.0015 |
| 298
```
</details>

---

### Step 6 [A - L1_2 · c38]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "literature": "GLOBlit_10766",
  "limit": 50,
  "purpose": "Find all data blocks in GLOBlit_10766",
  "tasks": "List all blocks from DOI 10.1021/je7001013 with their properties, compounds, and data ranges"
}
```
</details>

- **Result:** 990 chars  |  **Time:** 12.7s  |  **Started:** 06:37:11 (t+734.4s)
- **Subagent:** KEEP in 9,688 → 990 chars (12.4s)
  - **Summary:** GLOBlit_10766 (DOI 10.1021/je7001013) contains 16 data blocks: 8 unary (pure sulfoxides) and 8 binary (sulfoxide + water, GLOBcomp_1), measuring surface tension (GLOBprop_13) and refracti

<details><summary>Result</summary>

```
**Summary:** GLOBlit_10766 (DOI 10.1021/je7001013) contains 16 data blocks: 8 unary (pure sulfoxides) and 8 binary (sulfoxide + water, GLOBcomp_1), measuring surface tension (GLOBprop_13) and refractive index (GLOBprop_7) across 298.15–328.15 K.

**Compounds:** GLOBcomp_31 = dimethyl sulfoxide, GLOBcomp_1294 = diethyl sulfoxide, GLOBcomp_2145 = dipropyl sulfoxide, GLOBcomp_7698 = 2,2'-sulfinylbispropane (diisopropyl sulfoxide), GLOBcomp_1 = water.

| Block | System | Compound(s) | Property | Pts (orig) | Pts (kept) | T range (K) | Composition range | Value range |
|---|---|---|---|---|---|---|---|---|
| PROPblock_1 | unary | GLOBcomp_31 | GLOBprop_13 (γ, N/m) | 7 | 3 | 298.15–328.15 | — | 0.0379–0.0417 |
| PROPblock_2 | unary | GLOBcomp_31 | GLOBprop_7 (n_D) | 3 | 3 | 298.15–308.15 | — | 1.472–1.4765 |
| PROPblock_3 | unary | GLOBcomp_1294 | GLOBprop_13 (γ, N/m) | 7 | 6 | 298.15–328.15 | — | 0.032–0.0346 |
| PROPblock_4 | unary | GLOBcomp_1294 | GLOBprop_7 (n_D) | 3 | 2 | 298
```
</details>

---

### Step 8 [A - L1_2 · c39]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_5",
  "literature": "GLOBlit_10024",
  "purpose": "Ground thermal conductivity data for DMSO+water",
  "tasks": "Return full data table for PROPblock_5"
}
```
</details>

- **Result:** 1,636 chars  |  **Time:** 0.2s  |  **Started:** 06:38:01 (t+784.4s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1021/je301171y [GLOBlit_10024] :: PROPblock_5 (binary: dimethyl sulfoxide + water)
filter: none (whole block)
block constraints: pressure_kpa = 100.0

| BLKpoint_id | mass_fraction_<dimethyl sulfoxide> | temperature_k | pressure_kpa | thermal_conductivity_w_m_k |
|---|---|---|---|---|
| BLKpoint_1 | 0.1 | 279.63 | 100.0 | 0.522 |
| BLKpoint_7 | 0.1 | 338.6 | 100.0 | 0.594 |
| BLKpoint_8 | 0.1995 | 279.91 | 100.0 | 0.466 |
| BLKpoint_14 | 0.1995 | 338.93 | 100.0 | 0.528 |
| BLKpoint_15 | 0.2998 | 280.21 | 100.0 | 0.414 |
| BLKpoint_21 | 0.2998 | 339.37 | 100.0 | 0.465 |
| BLKpoint_22 | 0.3967 | 279.76 | 100.0 | 0.366 |
| BLKpoint_28 | 0.3967 | 338.87 | 100.0 | 0.404 |
| BLKpoint_29 | 0.5013 | 279.57 | 100.0 | 0.319 |
| BLKpoint_35 | 0.5013 | 338.61 | 100.0 | 0.347 |
| BLKpoint_36 | 0.599 | 280.01 | 100.0 | 0.282 |
| BLKpoint_42 | 0.599 | 338.9 | 100.0 | 0.299 |
| BLKpoint_43 | 0.6929 | 279.37 | 100.0 | 0.25 |
| BLKpoint_49 | 0.6929 | 338.59 | 100.0 | 0.261 |
| BLKpoint_50 | 0.7941 | 279.69 | 100.0 | 0.222 |
| BLKpoint_56 | 0.7941 | 338.86 | 100.0 | 0.224 |
| BLKpoint_57 | 0.9 | 279.18 | 100.0 | 0.2 |
| BLKpoint_63 | 0.9 | 338.51 | 100.0 | 0.196 |

mode: RDP — 18 of 63 matched rows shown (shape-preserving; block has 63). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=63): mass_fraction_dimethyl_sulfoxide 0.1–0.9 (n=63); temperature_k 279.18–339.37 (n=63); pressure_kpa 100.0–100.0 (n=63); thermal_conductivity_w_m_k 0.196–0.594 (n=63)
inspection_id: INSP_37d8a4c5a601
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

### Step 10 [A - L1_2 · c40]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_9",
  "literature": "GLOBlit_10766",
  "purpose": "Ground surface tension data values for DMSO+water",
  "tasks": "Verify point count, composition range, temperature range"
}
```
</details>

- **Result:** 2,773 chars  |  **Time:** 0.2s  |  **Started:** 06:38:12 (t+794.5s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1021/je7001013 [GLOBlit_10766] :: PROPblock_9 (binary: dimethyl sulfoxide + water)
filter: none (whole block)

| BLKpoint_id | temperature_k | mole_fraction_<dimethyl sulfoxide> | surface_tension_liquidgas_n_m |
|---|---|---|---|
| BLKpoint_1 | 298.15 | 0.0121 | 0.071 |
| BLKpoint_3 | 298.15 | 0.1044 | 0.0612 |
| BLKpoint_6 | 298.15 | 0.2999 | 0.0533 |
| BLKpoint_11 | 298.15 | 0.4523 | 0.0503 |
| BLKpoint_13 | 298.15 | 0.59 | 0.046 |
| BLKpoint_16 | 298.15 | 0.8945 | 0.042 |
| BLKpoint_17 | 303.15 | 0.0121 | 0.0701 |
| BLKpoint_19 | 303.15 | 0.1044 | 0.0606 |
| BLKpoint_20 | 303.15 | 0.1979 | 0.0558 |
| BLKpoint_22 | 303.15 | 0.2999 | 0.0524 |
| BLKpoint_27 | 303.15 | 0.4523 | 0.0499 |
| BLKpoint_28 | 303.15 | 0.501 | 0.0474 |
| BLKpoint_29 | 303.15 | 0.59 | 0.0452 |
| BLKpoint_32 | 303.15 | 0.8945 | 0.0414 |
| BLKpoint_33 | 308.15 | 0.0121 | 0.0692 |
| BLKpoint_35 | 308.15 | 0.1044 | 0.0598 |
| BLKpoint_36 | 308.15 | 0.1979 | 0.0548 |
| BLKpoint_38 | 308.15 | 0.2999 | 0.0515 |
| BLKpoint_43 | 308.15 | 0.4523 | 0.0491 |
| BLKpoint_44 | 308.15 | 0.501 | 0.0467 |
| BLKpoint_45 | 308.15 | 0.59 | 0.0446 |
| BLKpoint_46 | 308.15 | 0.7027 | 0.0426 |
| BLKpoint_48 | 308.15 | 0.8945 | 0.0409 |
| BLKpoint_49 | 313.15 | 0.0121 | 0.0676 |
| BLKpoint_51 | 313.15 | 0.1044 | 0.0587 |
| BLKpoint_52 | 313.15 | 0.1979 | 0.0539 |
| BLKpoint_54 | 313.15 | 0.2999 | 0.0506 |
| BLKpoint_59 | 313.15 | 0.4523 | 0.0482 |
| BLKpoint_61 | 313.15 | 0.59 | 0.0438 |
| BLKpoint_64 | 313.15 | 0.8945 | 0.0403 |
| BLKpoint_65 | 318.15 | 0.0121 | 0.0664 |
| BLKpoint_67 | 318.15 | 0.1044 | 0.0579 |
| BLKpoint_69 | 318.15 | 0.2507 | 0.0512 |
| BLKpoint_70 | 318.15 | 0.3218 | 0.0507 |
| BLKpoint_77 | 318.15 | 0.59 | 0.0431 |
| BLKpoint_80 | 318.15 | 0.8945 | 0.0398 |
| BLKpoint_81 | 323.15 | 0.0121 | 0.0653 |
| BLKpoint_83 | 323.15 | 0.1044 | 0.057 |
| BLKpoint_85 | 323.15 | 0.2507 | 0.0503 |
| BLKpoint_86 | 323.15 | 0.3218 | 0.0499 |
| BLKpoint_93 | 323.15 | 0.59 | 0.0423 |
| BLKpoint_96 | 323.15 | 0.8945 | 0.0392 |
| BLKpoint_97 | 328.15 | 0.0121 | 0.0651 |
| BLKpoint_99 | 328.15 | 0.1044 | 0.0551 |
| BLKpoint_101 | 328.15 | 0.2507 | 0.0494 |
| BLKpoint_102 | 328.15 | 0.3218 | 0.049 |
| BLKpoint_104 | 328.15 | 0.3549 | 0.0474 |
| BLKpoint_109 | 328.15 | 0.59 | 0.0417 |
| BLKpoint_112 | 328.15 | 0.8945 | 0.0387 |

mode: RDP — 49 of 112 matched rows shown (shape-preserving; block has 112). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=112): temperature_k 298.15–328.15 (n=112); mole_fraction_dimethyl_sulfoxide 0.0121–0.8945 (n=112); surface_tension_liquidgas_n_m 0.0387–0.071 (n=112)
inspection_id: INSP_507097ca3b25
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

### Step 11 [A - L1_2 · c41]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "PROPblock_10",
  "literature": "GLOBlit_10766",
  "purpose": "Ground refractive index data values for DMSO+water block",
  "tasks": "Inspect PROPblock_10 to get verbatim data rows for refractive index"
}
```
</details>

- **Result:** 1,659 chars  |  **Time:** 0.2s  |  **Started:** 06:38:20 (t+802.5s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1021/je7001013 [GLOBlit_10766] :: PROPblock_10 (binary: dimethyl sulfoxide + water)
filter: none (whole block)
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mole_fraction_<dimethyl sulfoxide> | pressure_kpa | refractive_index_na_dline |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 0.0121 | 101.0 | 1.34 |
| BLKpoint_3 | 298.15 | 0.1467 | 101.0 | 1.396 |
| BLKpoint_5 | 298.15 | 0.2959 | 101.0 | 1.4305 |
| BLKpoint_9 | 298.15 | 0.4301 | 101.0 | 1.4475 |
| BLKpoint_10 | 298.15 | 0.5964 | 101.0 | 1.461 |
| BLKpoint_11 | 298.15 | 0.7685 | 101.0 | 1.47 |
| BLKpoint_12 | 303.15 | 0.0121 | 101.0 | 1.339 |
| BLKpoint_14 | 303.15 | 0.1467 | 101.0 | 1.4005 |
| BLKpoint_16 | 303.15 | 0.2959 | 101.0 | 1.4295 |
| BLKpoint_19 | 303.15 | 0.3967 | 101.0 | 1.443 |
| BLKpoint_21 | 303.15 | 0.5964 | 101.0 | 1.459 |
| BLKpoint_22 | 303.15 | 0.7685 | 101.0 | 1.468 |
| BLKpoint_23 | 308.15 | 0.0121 | 101.0 | 1.3395 |
| BLKpoint_25 | 308.15 | 0.1467 | 101.0 | 1.4 |
| BLKpoint_27 | 308.15 | 0.2959 | 101.0 | 1.428 |
| BLKpoint_30 | 308.15 | 0.3967 | 101.0 | 1.442 |
| BLKpoint_32 | 308.15 | 0.5964 | 101.0 | 1.458 |
| BLKpoint_33 | 308.15 | 0.7685 | 101.0 | 1.466 |

mode: RDP — 18 of 33 matched rows shown (shape-preserving; block has 33). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=33): temperature_k 298.15–308.15 (n=33); mole_fraction_dimethyl_sulfoxide 0.0121–0.7685 (n=33); pressure_kpa 101.0–101.0 (n=33); refractive_index_na_dline 1.339–1.47 (n=33)
inspection_id: INSP_2257cf4faf77
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

## Tool Compaction Pipeline (22 calls)

| # | Tool | Pipeline | Native | Hardcoded | Agentic | Verdict | Native→Final | Section |
|--:|------|----------|-------:|----------:|--------:|---------|-------------:|---------|
| 1 | `resolve_compound_ids` | query | 580 | 295 | 200 | KEEP | −66% | L1_1 |
| 2 | `search_blocks` | query | 121,456 | 12,628 | 1,249 | KEEP | −99% | L1_1 |
| 3 | `search_system_registry` | query | 82,339 | 3,070 | 996 | KEEP | −99% | L1_1 |
| 4 | `search_blocks` | query | 121,456 | 12,628 | 1,197 | KEEP | −99% | L1_1 |
| 5 | `search_blocks` | query | 18,730 | 5,878 | 1,122 | KEEP | −94% | L1_1 |
| 6 | `search_blocks` | query | 6,199 | 1,762 | 1,033 | KEEP | −83% | L1_1 |
| 7 | `search_blocks` | query | 22,909 | 7,913 | 901 | KEEP | −96% | L1_1 |
| 8 | `search_system_summary` | query | 4,118 | 1,070 | 1,270 | KEEP | −69% | L1_1 |
| 9 | `search_blocks` | query | 7,785 | 3,380 | 1,194 | KEEP | −85% | L1_1 |
| 10 | `inspect_block` | analysis | 2,844 | 1,383 | 1,383 | SKIP | −51% | — |
| 11 | `inspect_block` | analysis | 2,903 | 1,379 | 1,379 | SKIP | −52% | — |
| 12 | `inspect_block` | analysis | 3,107 | 1,522 | 1,522 | SKIP | −51% | — |
| 13 | `inspect_block` | analysis | 3,247 | 1,534 | 1,534 | SKIP | −53% | — |
| 14 | `inspect_block` | analysis | 3,003 | 1,430 | 1,430 | SKIP | −52% | — |
| 15 | `resolve_property_ids` | query | 260 | 226 | 239 | KEEP | −8% | L1_2 |
| 16 | `search_blocks` | query | 6,323 | 2,121 | 1,249 | KEEP | −80% | L1_2 |
| 17 | `search_blocks` | query | 6,238 | 2,393 | 1,269 | KEEP | −80% | L1_2 |
| 18 | `search_blocks` | query | 6,500 | 2,265 | 1,115 | KEEP | −83% | L1_2 |
| 19 | `search_blocks` | query | 86,546 | 9,688 | 990 | KEEP | −99% | L1_2 |
| 20 | `inspect_block_table` | query | 6,261 | 1,620 | 1,620 | SKIP | −74% | L1_2 |
| 21 | `inspect_block_table` | query | 11,506 | 2,757 | 2,757 | SKIP | −76% | L1_2 |
| 22 | `inspect_block_table` | query | 6,291 | 1,643 | 1,643 | SKIP | −74% | L1_2 |

## Subagent Summary (14 events)

| Tool | Verdict | Input Chars | Output Chars | Time | Section |
|------|---------|-------------|-------------|------|---------|
| resolve_compound_ids | KEEP | 295 | 200 | 3.8s | L1_1 |
| search_blocks | KEEP | 12,628 | 1,249 | 15.6s | L1_1 |
| search_system_registry | KEEP | 3,070 | 996 | 12.7s | L1_1 |
| search_blocks | KEEP | 12,628 | 1,197 | 13.4s | L1_1 |
| search_blocks | KEEP | 5,878 | 1,122 | 15.4s | L1_1 |
| search_blocks | KEEP | 1,762 | 1,033 | 11.6s | L1_1 |
| search_blocks | KEEP | 7,913 | 901 | 15.3s | L1_1 |
| search_system_summary | KEEP | 1,070 | 1,270 | 12.6s | L1_1 |
| search_blocks | KEEP | 3,380 | 1,194 | 17.3s | L1_1 |
| resolve_property_ids | KEEP | 226 | 239 | 4.5s | L1_2 |
| search_blocks | KEEP | 2,121 | 1,249 | 13.7s | L1_2 |
| search_blocks | KEEP | 2,393 | 1,269 | 12.6s | L1_2 |
| search_blocks | KEEP | 2,265 | 1,115 | 12.2s | L1_2 |
| search_blocks | KEEP | 9,688 | 990 | 12.4s | L1_2 |

## Errors (3)

- **Step 2** `query_thermoml_parallel` (exception): {
  "error": "queries[0].id_catalog[0] must contain exactly ['global_id', 'name', 'registry_id', 'type']; received ['id', 'type']",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml_pa
- **Step 3** `query_thermoml_parallel` (exception): {
  "error": "queries[0].id_catalog must be an array",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml_parallel"
}
- **Step 4** `query_thermoml_parallel` (exception): {
  "error": "queries[0].id_catalog must be an array",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml_parallel"
}

---

**Total:** 42 tool calls  |  Tool time: 928.6s  |  Wall: 1289.4s  |  **Status:** OK
