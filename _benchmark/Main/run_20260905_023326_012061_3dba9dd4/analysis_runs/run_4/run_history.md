# Tool History — analysis-agent

**Nest:** main - A_2
**Session:** 74fbf4ae
**Detailed log:** run_history_detailed.md — Argo events + verbatim agent outputs (join: session id; step tag `cN` ↔ event-row `cN`)
**Prompt:** [Purpose: Determine the magnitude and composition of maximum volume contraction for water + ethanol at 25°C]
Find and fit excess molar volume (VE) data for the binary system water + ethanol at 25°C (298.15 K). Report the Redlich-Kister coefficients, the composition (mole fraction of ethanol) at which the minimum VE occurs, and the minimum VE value.

[Context: Looking for excess molar volume data. Ethanol CAS: 64-17-5, Water CAS: 7732-18-5.]
**Started:** 2026-09-05 02:33:37  |  **Elapsed:** 821.4s  |  **Tool calls:** 36  |  **Nested sections:** 2

---

### Step 1 [main - A_2 · c1]: `query_thermoml_parallel` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "queries": [
    {
      "label": "VE_direct",
      "purpose": "Find blocks with directly measured excess molar volume (VE) for binary water + ethanol at 298.15 K",
      "instruction": "Search for excess molar volume data (GLOBprop_17 or any excess volume property) for the binary system of water (CAS 7732-18-5) and ethanol (CAS 64-17-5) at approximately 298.15 K. Return DOIs, block numbers, and data point counts.",
      "id_catalog": [
        {
          "type": "compound",
          "id": "GLOBcomp_7",
          "name": "water",
          "cas": "7732-18-5"
        },
        {
          "type": "compound",
          "id": "GLOBcomp_3",
          "name": "ethanol",
          "cas": "64-17-5"
        }
      ],
      "context": ""
    },
    {
      "label": "density_data",
      "purpose": "Find blocks with density data for binary water + ethanol mixtures at 298.15 K for deriving excess molar volume",
      "instruction": "Search for mass density (GLOBprop_1) data for the binary mixture of water (CAS 7732-18-5) and ethanol (CAS 64-17-5) at approximately 298.15 K. I need blocks with composition-dependent density across the full mole fraction range. Return DOIs, block numbers, temperature ranges, and data point counts. Prefer blocks with many data points across the composition range.",
      "id_catalog": [
        {
          "type": "compound",
          "id": "GLOBcomp_7",
          "name": "water",
          "cas": "7732-18-5"
        },
        {
          "type": "compound",
          "id": "GLOBcomp_3",
          "name": "ethanol",
          "cas": "64-17-5"
        },
        {
          "type": "property",
          "id": "GLOBprop_1",
          "name": "Mass density"
        }
      ],
      "context": ""
    }
  ]
}
```
</details>

- **Result:** 224 chars  |  **Time:** 0.0s  |  **Started:** 02:33:50 (t+12.9s)
- **Error:** `{
  "error": "queries[0].id_catalog[0] must contain exactly ['global_id', 'name', 'registry_id', 'type']; received ['cas', 'id', 'name', 'type']",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml_parallel"
}`

---

### Step 2 [main - A_2 · c2]: `query_thermoml_parallel` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "queries": [
    {
      "label": "VE_direct",
      "purpose": "Find excess molar volume (VE) data for binary water + ethanol at 298.15 K",
      "instruction": "Search for blocks containing excess molar volume (GLOBprop_17 or any excess volume property) for the binary system water + ethanol at 298.15 K. Return DOIs, block numbers, and property details.",
      "id_catalog": [
        {
          "global_id": "GLOBprop_17",
          "name": "Excess molar enthalpy",
          "registry_id": "",
          "type": "property"
        }
      ],
      "context": "Water CAS: 7732-18-5, Ethanol CAS: 64-17-5. Looking for excess molar volume, not excess enthalpy. The property ID for excess molar volume may differ from GLOBprop_17."
    },
    {
      "label": "density_data",
      "purpose": "Find density data for binary water + ethanol mixture at 298.15 K",
      "instruction": "Search for blocks containing mass density (GLOBprop_1) for the binary system water + ethanol at 298.15 K. Return DOIs, block numbers, temperature ranges, and number of data points. Prefer blocks with many composition points covering the full range.",
      "id_catalog": [
        {
          "global_id": "GLOBprop_1",
          "name": "Mass density",
          "registry_id": "",
          "type": "property"
        }
      ],
      "context": "Water CAS: 7732-18-5, Ethanol CAS: 64-17-5. Need density vs composition data to derive excess molar volume."
    }
  ]
}
```
</details>

- **Result:** 253 chars  |  **Time:** 0.0s  |  **Started:** 02:34:00 (t+22.6s)
- **Error:** `{
  "error": "queries[0].id_catalog[0].type is invalid: 'property'; valid types: ['blocktype', 'comp', 'constr', 'lit', 'meas', 'phase', 'prop', 'rxntype', 'solvent', 'var']",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml_parallel"
}`

---

### Step 3 [main - A_2 · c3]: `query_thermoml_parallel` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "queries": [
    {
      "label": "VE_direct",
      "purpose": "Find excess molar volume (VE) data for water + ethanol binary mixture at 298.15 K",
      "instruction": "Search for blocks containing excess molar volume (GLOBprop_17 or any excess volume property) for the binary system water (CAS 7732-18-5) + ethanol (CAS 64-17-5) at approximately 298.15 K. Return DOIs, block numbers, and data point counts.",
      "id_catalog": [
        {
          "global_id": "GLOBprop_17",
          "name": "Excess molar enthalpy",
          "registry_id": "",
          "type": "prop"
        },
        {
          "global_id": "",
          "name": "water",
          "registry_id": "7732-18-5",
          "type": "comp"
        },
        {
          "global_id": "",
          "name": "ethanol",
          "registry_id": "64-17-5",
          "type": "comp"
        }
      ],
      "context": ""
    },
    {
      "label": "density_data",
      "purpose": "Find density data for water + ethanol binary mixture at 298.15 K for deriving excess molar volume",
      "instruction": "Search for blocks containing mass density (GLOBprop_1) for the binary system water (CAS 7732-18-5) + ethanol (CAS 64-17-5) at approximately 298.15 K. Return DOIs, block numbers, temperature ranges, and data point counts. Prefer blocks with many composition points across the full mole fraction range.",
      "id_catalog": [
        {
          "global_id": "GLOBprop_1",
          "name": "Mass density",
          "registry_id": "",
          "type": "prop"
        },
        {
          "global_id": "",
          "name": "water",
          "registry_id": "7732-18-5",
          "type": "comp"
        },
        {
          "global_id": "",
          "name": "ethanol",
          "registry_id": "64-17-5",
          "type": "comp"
        }
      ],
      "context": ""
    }
  ]
}
```
</details>

- **Result:** 152 chars  |  **Time:** 0.0s  |  **Started:** 02:34:10 (t+32.7s)
- **Error:** `{
  "error": "comp_num_id must match GLOBcomp_<positive integer>, got ''",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml_parallel"
}`

---

### Step 4 [main - A_2 · c17]: `query_thermoml_parallel`

<details><summary>Arguments</summary>

```json
{
  "queries": [
    {
      "label": "VE_direct",
      "purpose": "Find excess molar volume (VE) data for binary mixture of water and ethanol at 298.15 K",
      "instruction": "Search for blocks containing excess molar volume (GLOBprop_17 or any excess volume property) for the binary system water (CAS 7732-18-5) + ethanol (CAS 64-17-5) at approximately 298.15 K. Return DOIs, block numbers, and compound/property IDs.",
      "id_catalog": [],
      "context": ""
    },
    {
      "label": "density_data",
      "purpose": "Find density data for binary mixture of water and ethanol at 298.15 K",
      "instruction": "Search for blocks containing mass density (GLOBprop_1) for the binary system water (CAS 7732-18-5) + ethanol (CAS 64-17-5) at approximately 298.15 K. Return DOIs, block numbers, compound IDs, and number of data points. Prefer blocks with many composition points covering full range x=0 to x=1.",
      "id_catalog": [],
      "context": ""
    }
  ]
}
```
</details>

- **Result:** 163,237 chars  |  **Time:** 278.3s  |  **Started:** 02:34:20 (t+42.6s)
- **Nested:** ↳ 5 tool calls in section 'L1_1' below
- **Nested:** ↳ 8 tool calls in section 'L1_2' below

<details><summary>Result</summary>

```
[TOOL_RESULT_SIZE_WARNING: query_thermoml_parallel returned 162,981 characters after result processing; the target is 24,000. The full result follows — prefer narrower requests, and rely on your working memory for recall instead of re-running this call.]

<subagent_answer>
{
  "n_queries": 2,
  "results": [
    {
      "label": "VE_direct",
      "result": {
        "answer": "**Excess molar volume (V^E) data for water + ethanol at 298.15 K: Not found in the ThermoML database.**\n\nA comprehensive search was conducted for the binary system water (GLOBcomp_1, CAS 7732-18-5) + ethanol (GLOBcomp_2, CAS 64-17-5) with the property excess molar volume (GLOBprop_28). No data blocks were found \u2014 neither as declared binary systems nor as subsystems of higher-order mixtures.\n\nThe ThermoML database does contain data for the water + ethanol binary system, but for other properties. Among the 50 blocks found for this pair, the available properties include:\n\n- **Mass density** (kg/m\u00b3) \u2014 12 blocks (e.g., DOI 10.1016/j.fluid.2004.11.019 [GLOBlit_220]/PROPblock_2)\n- **Excess molar enthalpy** (kJ/mol) \u2014 5 blocks (e.g., DOI 10.1016/j.fluid.2007.06.007 [GLOBlit_528]/PROPblock_1)\n- **Boiling temperature** (K) \u2014 9 blocks\n- **Vapor/sublimation pressure** (kPa) \u2014 5 blocks\n- **Mole fraction** (VLE) \u2014 8 blocks\n- **Activity coefficient** \u2014 4 blocks\n- **Viscosity** (Pa\u00b7s) \u2014 4 blocks\n- **Speed of sound** (m/s) \u2014 1 block\n- **Relative permittivity** \u2014 1 block\n\nNo excess molar volume (V^E) data is available for this system in the database.",
        "core_claims": [
          "No excess molar volume (V^E) data for the water + ethanol binary system at 298.15 K were found in the ThermoML database.",
          "The ThermoML database does contain data for the water + ethanol binary system for other properties, including mass density, excess molar enthalpy, boiling temperature, vapor/sublimation pressure, mole fraction (VLE), activity coefficient, viscosity, speed of sound, and relative permittivity, across 50 data blocks."
        ],
        "status": "no_results",
        "summary": "A comprehensive search of the ThermoML database for excess molar volume (V^E) data for the binary system water (CAS 7732-18-5) + ethanol (CAS 64-17-5) at 298.15 K found no results. The database contains 50 data blocks for this binary pair, but none report excess molar volume. Available properties for this system include mass density (12 blocks), excess molar enthalpy (5 blocks), boiling temperature (9 blocks), vapor/sublimation pressure (5 blocks), mole fraction VLE (8 blocks), activity coefficient (4 blocks), viscosity (4 blocks), speed of sound (1 block), and relative permittivity (1 block).",
        "core_id_updates": [],
        "core_blocks_found": [],
        "data_inspections": []
      }
    },
    {
      "label": "density_data",
      "result": {
        "answer": "## Binary Water + Ethanol Mass Density Data near 298.15 K\n\n**Compounds:** Water (GLOBcomp_1, CAS 7732-18-5) + Ethanol (GLOBcomp_2, CAS 64-17-5)  \n**Property:** Mass density (GLOBprop_1, kg/m\u00b3)  \n**System type:** Binary, liquid phase\n\n### Available Blocks (T \u2248 295\u2013301 K)\n\n17 data blocks were found in the ThermoML database. The three largest blocks were individually inspected; the remaining 14 blocks were identified via the registry search but not individually inspected in this run. Data point counts for the uninspected blocks are from the registry search results.\n\n#### Inspected Blocks\n\n| # | DOI | GLOBlit | Block | Data Points |\n|---|-----|---------|-------|-------------|\n| 1 | 10.1016/j.fluid.2004.11.019 | GLOBlit_220 | PROPblock_2 | 810 |\n| 2 | 10.1016/j.jct.2004.07.019 | GLOBlit_2432 | PROPblock_2 | 565 |\n| 3 | 10.1016/j.jct.2018.02.022 | GLOBlit_5201 | PROPblock_19 | 244 |\n\n#### Additional Blocks (not individually inspected in this run)\n\n| # | DOI | GLOBlit | Block | Data Points (from registry) |\n|---|-----|---------|-------|-----------------------------|\n| 4 | 10.1021/je060335h | GLOBlit_9006 | PROPblock_1 | (not individually inspected) |\n| 5 | 10.1016/j.fluid.2014.05.032 | GLOBlit_1483 | PROPblock_1 | (not individually inspected) |\n| 6 | 10.1021/je800150h | GLOBlit_11136 | PROPblock_9 | (not individually inspected) |\n| 7 | 10.1021/je700300y | GLOBlit_10866 | PROPblock_7 | (not individually inspected) |\n| 8 | 10.1016/j.jct.2011.10.009 | GLOBlit_3475 | PROPblock_3 | 70 |\n| 9 | 10.1016/j.jct.2015.06.024 | GLOBlit_4415 | PROPblock_7 | 40 |\n| 10 | 10.1016/j.jct.2007.05.004 | GLOBlit_2825 | PROPblock_12 | (not individually inspected) |\n| 11 | 10.1021/je020173z | GLOBlit_8050 | PROPblock_5 | (not individually inspected) |\n| 12 | 10.1021/je4003515 | GLOBlit_10159 | PROPblock_7 | 23 |\n| 13 | 10.1021/je600565m | GLOBlit_10699 | PROPblock_6 | 18 |\n| 14 | 10.1021/je900743e | GLOBlit_11792 | PROPblock_3 | 15 |\n| 15 | 10.1021/acs.jced.6b01058 | GLOBlit_7085 | PROPblock_7 | (not individually inspected) |\n| 16 | 10.1021/je900064e | GLOBlit_11504 | PROPblock_6 | (not individually inspected) |\n| 17 | 10.1021/acs.jced.7b00299 | GLOBlit_7178 | PROPblock_10 | (not individually inspected) |\n\n### Best Candidates for Full Composition Coverage\n\n**GLOBlit_220::PROPblock_2** (810 total points) is the richest dataset. At exactly 298.15 K, there are 270 data points spanning x(ethanol) = 0.003\u20131 and pressures from 100 to 40000 kPa, with mass density ranging from 785.7 to 1012.7 kg/m\u00b3. At atmospheric pressure (100 kPa) and 298.15 K, representative values include:\n\n| x(ethanol) | \u03c1 (kg/m\u00b3) |\n|------------|-----------|\n| 0.003 | 995.3 |\n| 0.2502 | 918.5 |\n| 0.4501 | 868.8 |\n| 0.6967 | 825.2 |\n| 1 | 785.7 |\n\n**GLOBlit_5201::PROPblock_19** (244 points) provides data at 92.3 kPa across four temperatures (293.15\u2013308.15 K) with x(ethanol) = 0\u20131. At 298.15 K, representative values include:\n\n| x(ethanol) | \u03c1 (kg/m\u00b3) |\n|------------|-----------|\n| 0 | 997.267 |\n| 0.1984 | 931.84 |\n| 0.4495 | 869.34 |\n| 0.7006 | 825.07 |\n| 1 | 785.26 |\n\n**Note on GLOBlit_2432::PROPblock_2** (565 points): This block uses molality (mol/kg) as the composition variable and reports negative density values (range: \u221219.634 to \u22120.7809 kg/m\u00b3, likely relative or excess density differences), so it is less suitable for obtaining absolute density as a function of mole fraction.\n\n**Chemistry note:** Both inspected absolute-density datasets show a monotonic decrease in density from pure water (995.3\u2013997.267 kg/m\u00b3) toward pure ethanol (785.26\u2013785.7 kg/m\u00b3) at 298.15 K, consistent with the well-known non-ideal mixing behavior of this system.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNINSPECTED_BLOCK** PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10: PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10 is quoted with data values (70, 40, 23, 13, \u2026) but was never inspected in this run\n  fix (required \u2014 this region quotes data from cited database blocks): `inspect_block_table(block_number=\"PROPblock_1\", literature=\"<GLOBlit_N or DOI>\"); inspect_block_table(block_number=\"PROPblock_9\", literature=\"<GLOBlit_N or DOI>\"); inspect_block_table(block_number=\"PROPblock_7\", literature=\"<GLOBlit_N or DOI>\"); inspect_block_table(block_number=\"PROPblock_3\", literature=\"<GLOBlit_N or DOI>\"); inspect_block_table(block_number=\"PROPblock_12\", literature=\"<GLOBlit_N or DOI>\"); inspect_block_table(block_number=\"PROPblock_5\", literature=\"<GLOBlit_N or DOI>\"); inspect_block_table(block_number=\"PROPblock_6\", literature=\"<GLOBlit_N or DOI>\"); inspect_block_table(block_number=\"PROPblock_10\", literature=\"<GLOBlit_N or DOI>\")`\n- **MISATTRIBUTED_VALUE** GLOBlit_2432::PROPblock_2: 997.267 does not belong to GLOBlit_2432::PROPblock_2; it matches only GLOBlit_5201::PROPblock_19 (inspected this run)\n  fix (required \u2014 this IS a database value, under a different block): `re-anchor 997.267 to GLOBlit_5201::PROPblock_19 \u2014 no new tool call needed`\n- **MISATTRIBUTED_VALUE** GLOBlit_2432::PROPblock_2: 785.26 does not belong to GLOBlit_2432::PROPblock_2; it matches only GLOBlit_5201::PROPblock_19 (inspected this run)\n  fix (required \u2014 this IS a database value, under a different block): `re-anchor 785.26 to GLOBlit_5201::PROPblock_19 \u2014 no new tool call needed`\nInspected so far: PROPblock_19, PROPblock_2",
        "core_claims": [
          "17 ThermoML data blocks were identified for binary water + ethanol mass density near 298.15 K, but only three were individually inspected in this run; 14 blocks remain uninspected.",
          "GLOBlit_220::PROPblock_2 is the richest inspected dataset (810 total points), with 270 points at exactly 298.15 K spanning x(ethanol) = 0.003\u20131 and pressures from 100 to 40000 kPa, yielding mass densities from 785.7 to 1012.7 kg/m\u00b3.",
          "GLOBlit_5201::PROPblock_19 (244 points) provides absolute density data at 92.3 kPa and 298.15 K across x(ethanol) = 0\u20131, with density ranging from 997.267 kg/m\u00b3 (pure water) to 785.26 kg/m\u00b3 (pure ethanol).",
          "GLOBlit_2432::PROPblock_2 (565 points) reports negative density values (range: \u221219.634 to \u22120.7809 kg/m\u00b3), likely relative or excess density differences, making it less suitable for obtaining absolute density as a function of mole fraction.",
          "Both inspected absolute-density datasets show a monotonic decrease in density from pure water toward pure ethanol at 298.15 K, consistent with the well-known non-ideal mixing behavior of this system.",
          "Multiple data values and block-level details for the 14 uninspected blocks remain unverified, and some values were flagged as misattributed between blocks, limiting confidence in the completeness and attribution accuracy of the full survey."
        ],
        "status": "success",
        "summary": "Seventeen ThermoML data blocks report mass density (kg/m\u00b3) for the binary water (CAS 7732-18-5) + ethanol (CAS 64-17-5) system near 298.15 K. Three blocks were individually inspected. The richest is GLOBlit_220::PROPblock_2 (810 points), which at 298.15 K and 100 kPa spans x(ethanol) = 0.003\u20131 with density from 995.3 to 785.7 kg/m\u00b3; at 298.15 K it covers pressures from 100 to 40000 kPa across 270 points. GLOBlit_5201::PROPblock_19 (244 points) provides data at 92.3 kPa across four temperatures (293.15\u2013308.15 K) with x(ethanol) = 0\u20131; at 298.15 K representative values range from 997.267 kg/m\u00b3 (pure water) to 785.26 kg/m\u00b3 (pure ethanol). GLOBlit_2432::PROPblock_2 (565 points) uses molality as the composition variable and reports negative density values (range \u221219.634 to \u22120.7809 kg/m\u00b3), likely excess or relative density differences, making it less suitable for absolute density. Both absolute-density datasets show monotonic decrease from pure water toward pure ethanol at 298.15 K. Fourteen additional blocks were identified but not individually inspected; their data point counts and contents remain unverified.",
        "core_id_updates": [
          {
            "action": "add",
            "core_GLOB_id": "GLOBcomp_1",
            "registry_id": "water",
            "name": "water"
          },
          {
            "action": "add",
            "core_GLOB_id": "GLOBcomp_2",
            "registry_id": "ethanol",
            "name": "ethanol"
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
            "description": "Mass density for water + ethanol at 298.15 K; 810 data points spanning x(ethanol) = 0.003\u20131 and pressures 100\u201340000 kPa.",
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
                "SMILES": "CCO",
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
                "SMILES": "CCO",
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
            "parent_n_datapoints": 810,
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
            "description": "Mass density (relative/excess) for water + ethanol; 565 data points using molality composition variable with negative density values.",
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
                "SMILES": "CCO",
                "sample_num": "DOIcompSample_1_1"
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
                "SMILES": "CCO",
                "sample_num": "DOIcompSample_1_1"
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
            "parent_n_datapoints": 565,
            "subsystem_scope": null,
            "subsystem_point_runs": [],
            "subsystem_path_class": null,
            "subsystem_evidence_quality": null,
            "subsystem_condition_ranges": []
          },
          {
            "lit_num_id": "GLOBlit_5201",
            "block_number": "PROPblock_19",
            "BLKsubsys_id": null,
            "system_type": "binary",
            "comp_num_ids": [
              "GLOBcomp_2",
              "GLOBcomp_1"
            ],
            "prop_num_ids": [
              "GLOBprop_1"
            ],
            "description": "Mass density for water + ethanol at 92.3 kPa across 293.15\u2013308.15 K; 244 data points spanning x(ethanol) = 0\u20131.",
            "doi": "10.1016/j.jct.2018.02.022",
            "lit_id": "2018-hog-tor-0",
            "block_type": "PureOrMixtureData",
            "blocktype_num_id": "GLOBblocktype_1",
            "n_datapoints": 244,
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
                  "n_unique": 59
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
                  "min": 776.592,
                  "max": 998.429,
                  "mean": 881.16518,
                  "std": 74.568443,
                  "n": 244
                },
                "uncertainty": {
                  "evaluation_method": "Propagation of evaluated standard uncertainties",
                  "confidence_level": 95,
                  "evaluator": "Data file compiler",
                  "assessment_num": "BLKpropAssessment_1_1"
                },
                "range_min": 776.592,
                "range_max": 998.429
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
            "parent_n_datapoints": 244,
            "subsystem_scope": null,
            "subsystem_point_runs": [],
            "subsystem_path_class": null,
            "subsystem_evidence_quality": null,
            "subsystem_condition_ranges": []
          },
          {
            "lit_num_id": "GLOBlit_9006",
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
            "description": "Mass density for water + ethanol (not individually inspected).",
            "doi": "10.1021/je060335h",
            "lit_id": "2007-her-san-0",
            "block_type": "PureOrMixtureData",
            "blocktype_num_id": "GLOBblocktype_1",
            "n_datapoints": 164,
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
                  "max": 298.15,
                  "n_unique": 4
                },
                "range_min": 283.15,
                "range_max": 298.15
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
                  "n_unique": 41
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
                  "min": 785.22,
                  "max": 999.7,
                  "mean": 908.57689,
                  "std": 61.524659,
                  "n": 164
                },
                "uncertainty": {
                  "evaluation_method": "Propagation of evaluated standard uncertainties",
                  "confidence_level": 95,
                  "evaluator": "Data file compiler",
                  "assessment_num": "BLKpropAssessment_1_1"
                },
                "range_min": 785.22,
                "range_max": 999.7
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
                "org_num": "DOIcomp_3",
                "comp_num_id": "GLOBcomp_1",
                "name": "water",
                "formula": "H2O",
                "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
                "SMILES": "O",
                "sample_num": "DOIcompSample_3_1"
              }
            ],
            "parent_n_datapoints": 164,
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
            "description": "Mass density for water + ethanol (not individually inspected).",
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
                "SMILES": "CCO",
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
                "SMILES": "CCO",
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
            "parent_n_datapoints": 140,
            "subsystem_scope": null,
            "subsystem_point_runs": [],
            "subsystem_path_class": null,
            "subsystem_evidence_quality": null,
            "subsystem_condition_ranges": []
          },
          {
            "lit_num_id": "GLOBlit_11136",
            "block_number": "PROPblock_9",
            "BLKsubsys_id": null,
            "system_type": "binary",
            "comp_num_ids": [
              "GLOBcomp_2",
              "GLOBcomp_1"
            ],
            "prop_num_ids": [
              "GLOBprop_1"
            ],
            "description": "Mass density for water + ethanol (not individually inspected).",
            "doi": "10.1021/je800150h",
            "lit_id": "2008-reh-ans-0",
            "block_type": "PureOrMixtureData",
            "blocktype_num_id": "GLOBblocktype_1",
            "n_datapoints": 108,
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
                  "min": 268.1,
                  "max": 323.15,
                  "n_unique": 12
                },
                "range_min": 268.1,
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
                "meas_num_id": "GLOBmeas_212",
                "meas_ID": "pycnom_ufactor_16",
                "method_standard": null,
                "method_custom": "PYCNOM::UFactor:16",
                "range": {
                  "BLKprop_id": "BLKprop_1",
                  "name": "Mass density, kg/m3",
                  "min": 774.3,
                  "max": 977.3,
                  "mean": 869.766667,
                  "std": 54.624437,
                  "n": 108
                },
                "uncertainty": {
                  "evaluation_method": "Propagation of evaluated standard uncertainties",
                  "confidence_level": 95,
                  "evaluator": "Data file compiler",
                  "assessment_num": "BLKpropAssessment_1_1"
                },
                "range_min": 774.3,
                "range_max": 977.3
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
                "org_num": "DOIcomp_1",
                "comp_num_id": "GLOBcomp_1",
                "name": "water",
                "formula": "H2O",
                "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
                "SMILES": "O",
                "sample_num": "DOIcompSample_1_1"
              }
            ],
            "parent_n_datapoints": 108,
            "subsystem_scope": null,
            "subsystem_point_runs": [],
            "subsystem_path_class": null,
            "subsystem_evidence_quality": null,
            "subsystem_condition_ranges": []
          },
          {
            "lit_num_id": "GLOBlit_10866",
            "block_number": "PROPblock_7",
            "BLKsubsys_id": null,
            "system_type": "binary",
            "comp_num_ids": [
              "GLOBcomp_2",
              "GLOBcomp_1"
            ],
            "prop_num_ids": [
              "GLOBprop_1"
            ],
            "description": "Mass density for water + ethanol (not individually inspected).",
            "doi": "10.1021/je700300y",
            "lit_id": "2007-zar-jal-1",
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
                  "min": 0.0805,
                  "max": 0.9605,
                  "n_unique": 12
                },
                "range_min": 0.0805,
                "range_max": 0.9605
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
                  "min": 782.01,
                  "max": 984.04,
                  "mean": 874.349524,
                  "std": 59.376354,
                  "n": 84
                },
                "uncertainty": {
                  "evaluation_method": "Propagation of evaluated standard uncertainties",
                  "confidence_level": 95,
                  "evaluator": "Data file compiler",
                  "assessment_num": "BLKpropAssessment_1_1"
                },
                "range_min": 782.01,
                "range_max": 984.04
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
            "parent_n_datapoints": 84,
            "subsystem_scope": null,
            "subsystem_point_runs": [],
            "subsystem_path_class": null,
            "subsystem_evidence_quality": null,
            "subsystem_condition_ranges": []
          },
          {
            "lit_num_id": "GLOBlit_3475",
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
            "description": "Mass density for water + ethanol; 70 data points.",
            "doi": "10.1016/j.jct.2011.10.009",
            "lit_id": "2012-iva--3",
            "block_type": "PureOrMixtureData",
            "blocktype_num_id": "GLOBblocktype_1",
            "n_datapoints": 70,
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
                  "min": 278.15,
                  "max": 318.15,
                  "n_unique": 5
                },
                "range_min": 278.15,
                "range_max": 318.15
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
                  "min": 0.000996,
                  "max": 0.036609,
                  "n_unique": 14
                },
                "range_min": 0.000996,
                "range_max": 0.036609
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
                  "min": 767.66,
                  "max": 806.61,
                  "mean": 787.052857,
                  "std": 12.401719,
                  "n": 70
                },
                "uncertainty": {
                  "evaluation_method": "Propagation of evaluated standard uncertainties",
                  "confidence_level": 95,
                  "evaluator": "Data file compiler",
                  "assessment_num": "BLKpropAssessment_1_1"
                },
                "range_min": 767.66,
                "range_max": 806.61
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
                "org_num": "DOIcomp_1",
                "comp_num_id": "GLOBcomp_1",
                "name": "water",
                "formula": "H2O",
                "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
                "SMILES": "O",
                "sample_num": "DOIcompSample_1_1"
              }
            ],
            "parent_n_datapoints": 70,
            "subsystem_scope": null,
            "subsystem_point_runs": [],
            "subsystem_path_class": null,
            "subsystem_evidence_quality": null,
            "subsystem_condition_ranges": []
          },
          {
            "lit_num_id": "GLOBlit_4415",
            "block_number": "PROPblock_7",
            "BLKsubsys_id": null,
            "system_type": "binary",
            "comp_num_ids": [
              "GLOBcomp_2",
              "GLOBcomp_1"
            ],
            "prop_num_ids": [
              "GLOBprop_1"
            ],
            "description": "Mass density for water + ethanol; 40 data points.",
            "doi": "10.1016/j.jct.2015.06.024",
            "lit_id": "2015-ebr-sad-0",
            "block_type": "PureOrMixtureData",
            "blocktype_num_id": "GLOBblocktype_1",
            "n_datapoints": 40,
            "n_components": 2,
            "compounds": [
              {
                "org_num": "DOIcomp_4",
                "comp_num_id": "GLOBcomp_2",
                "name": "ethanol",
                "formula": "C2H6O",
                "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
                "SMILES": "CCO",
                "sample_num": "DOIcompSample_4_1"
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
            "solvents": [
              {
                "component_org_num": "DOIcomp_1",
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
                "value": 84.5,
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
                  "max": 308.15,
                  "n_unique": 5
                },
                "range_min": 288.15,
                "range_max": 308.15
              },
              {
                "BLKvar_id": "BLKvar_2",
                "var_num_id": "GLOBvar_4",
                "var_id": "molality_mol_kg_DOIcomp_4",
                "name": "Molality, mol/kg",
                "type": "eComponentComposition",
                "component_org_num": "DOIcomp_4",
                "phase": {
                  "phase": "Liquid",
                  "phase_num_id": "GLOBphase_1",
                  "phase_id": "liquid"
                },
                "range": {
                  "BLKvar_id": "BLKvar_2",
                  "name": "Molality, mol/kg",
                  "min": 0.02159,
                  "max": 0.21882,
                  "n_unique": 8
                },
                "range_min": 0.02159,
                "range_max": 0.21882
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
                  "min": 992.123,
                  "max": 998.9,
                  "mean": 995.86695,
                  "std": 1.910255,
                  "n": 40
                },
                "uncertainty": {
                  "evaluation_method": "Propagation of evaluated standard uncertainties",
                  "confidence_level": 95,
                  "evaluator": "Data file compiler",
                  "assessment_num": "BLKpropAssessment_1_1"
                },
                "range_min": 992.123,
                "range_max": 998.9
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
                "comp_num_id": "GLOBcomp_2",
                "name": "ethanol",
                "formula": "C2H6O",
                "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
                "SMILES": "CCO",
                "sample_num": "DOIcompSample_4_1"
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
            "parent_n_datapoints": 40,
            "subsystem_scope": null,
            "subsystem_point_runs": [],
            "subsystem_path_class": null,
            "subsystem_evidence_quality": null,
            "subsystem_condition_ranges": []
          },
          {
            "lit_num_id": "GLOBlit_2825",
            "block_number": "PROPblock_12",
            "BLKsubsys_id": null,
            "system_type": "binary",
            "comp_num_ids": [
              "GLOBcomp_2",
              "GLOBcomp_1"
            ],
            "prop_num_ids": [
              "GLOBprop_1"
            ],
            "description": "Mass density for water + ethanol (not individually inspected).",
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
                  "min": 781.15,
                  "max": 998.2,
                  "mean": 875.231351,
                  "std": 74.42608,
                  "n": 37
                },
                "uncertainty": {
                  "evaluation_method": "Propagation of evaluated standard uncertainties",
                  "confidence_level": 95,
                  "evaluator": "Data file compiler",
                  "assessment_num": "BLKpropAssessment_1_1"
                },
                "range_min": 781.15,
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
            "lit_num_id": "GLOBlit_8050",
            "block_number": "PROPblock_5",
            "BLKsubsys_id": null,
            "system_type": "binary",
            "comp_num_ids": [
              "GLOBcomp_2",
              "GLOBcomp_1"
            ],
            "prop_num_ids": [
              "GLOBprop_1"
            ],
            "description": "Mass density for water + ethanol (not individually inspected).",
            "doi": "10.1021/je020173z",
            "lit_id": "2003-gal-tab-0",
            "block_type": "PureOrMixtureData",
            "blocktype_num_id": "GLOBblocktype_1",
            "n_datapoints": 24,
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
                  "max": 313.15,
                  "n_unique": 2
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
                  "min": 0.10835,
                  "max": 0.71144,
                  "n_unique": 24
                },
                "range_min": 0.10835,
                "range_max": 0.71144
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
                "meas_num_id": "GLOBmeas_236",
                "meas_ID": "vibtub_ufactor_64",
                "method_standard": null,
                "method_custom": "VIBTUB:UFactor:64",
                "range": {
                  "BLKprop_id": "BLKprop_1",
                  "name": "Mass density, kg/m3",
                  "min": 848.29,
                  "max": 979.29,
                  "mean": 919.849583,
                  "std": 34.408583,
                  "n": 24
                },
                "uncertainty": {
                  "evaluation_method": "Propagation of evaluated standard uncertainties",
                  "confidence_level": 95,
                  "evaluator": "Data file compiler",
                  "assessment_num": "BLKpropAssessment_1_1"
                },
                "range_min": 848.29,
                "range_max": 979.29
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
                "org_num": "DOIcomp_3",
                "comp_num_id": "GLOBcomp_1",
                "name": "water",
                "formula": "H2O",
                "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
                "SMILES": "O",
                "sample_num": "DOIcompSample_3_1"
              }
            ],
            "parent_n_datapoints": 24,
            "subsystem_scope": null,
            "subsystem_point_runs": [],
            "subsystem_path_class": null,
            "subsystem_evidence_quality": null,
            "subsystem_condition_ranges": []
          },
          {
            "lit_num_id": "GLOBlit_10159",
            "block_number": "PROPblock_7",
            "BLKsubsys_id": null,
            "system_type": "binary",
            "comp_num_ids": [
              "GLOBcomp_2",
              "GLOBcomp_1"
            ],
            "prop_num_ids": [
              "GLOBprop_1"
            ],
            "description": "Mass density for water + ethanol; 23 data points.",
            "doi": "10.1021/je4003515",
            "lit_id": "2013-che-liu-0",
            "block_type": "PureOrMixtureData",
            "blocktype_num_id": "GLOBblocktype_1",
            "n_datapoints": 23,
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
                  "min": 901.281,
                  "max": 936.706,
                  "mean": 918.374304,
                  "std": 9.366017,
                  "n": 23
                },
                "uncertainty": {
                  "evaluation_method": "Propagation of evaluated standard uncertainties",
                  "confidence_level": 95,
                  "evaluator": "Data file compiler",
                  "assessment_num": "BLKpropAssessment_1_1"
                },
                "range_min": 901.281,
                "range_max": 936.706
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
            "parent_n_datapoints": 23,
            "subsystem_scope": null,
            "subsystem_point_runs": [],
            "subsystem_path_class": null,
            "subsystem_evidence_quality": null,
            "subsystem_condition_ranges": []
          },
          {
            "lit_num_id": "GLOBlit_10699",
            "block_number": "PROPblock_6",
            "BLKsubsys_id": null,
            "system_type": "binary",
            "comp_num_ids": [
              "GLOBcomp_2",
              "GLOBcomp_1"
            ],
            "prop_num_ids": [
              "GLOBprop_1"
            ],
            "description": "Mass density for water + ethanol; 18 data points.",
            "doi": "10.1021/je600565m",
            "lit_id": "2007-pir-cos-0",
            "block_type": "PureOrMixtureData",
            "blocktype_num_id": "GLOBblocktype_1",
            "n_datapoints": 18,
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
                  "min": 298.15,
                  "max": 318.15,
                  "n_unique": 2
                },
                "range_min": 298.15,
                "range_max": 318.15
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
                  "min": 0.0998,
                  "max": 0.9051,
                  "n_unique": 18
                },
                "range_min": 0.0998,
                "range_max": 0.9051
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
                "meas_num_id": "GLOBmeas_203",
                "meas_ID": "vibtub_ufactor_3",
                "method_standard": null,
                "method_custom": "VIBTUB:UFactor:3",
                "range": {
                  "BLKprop_id": "BLKprop_1",
                  "name": "Mass density, kg/m3",
                  "min": 780.53,
                  "max": 965.51,
                  "mean": 860.892778,
                  "std": 56.848168,
                  "n": 18
                },
                "uncertainty": {
                  "evaluation_method": "Propagation of evaluated standard uncertainties",
                  "confidence_level": 95,
                  "evaluator": "Data file compiler",
                  "assessment_num": "BLKpropAssessment_1_1"
                },
                "range_min": 780.53,
                "range_max": 965.51
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
            "parent_n_datapoints": 18,
            "subsystem_scope": null,
            "subsystem_point_runs": [],
            "subsystem_path_class": null,
            "subsystem_evidence_quality": null,
            "subsystem_condition_ranges": []
          },
          {
            "lit_num_id": "GLOBlit_11792",
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
            "description": "Mass density for water + ethanol; 15 data points.",
            "doi": "10.1021/je900743e",
            "lit_id": "2010-yan-wan-1",
            "block_type": "PureOrMixtureData",
            "blocktype_num_id": "GLOBblocktype_1",
            "n_datapoints": 15,
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
                  "n_unique": 3
                },
                "range_min": 293.15,
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
                  "min": 0.1,
                  "max": 0.5,
                  "n_unique": 5
                },
                "range_min": 0.1,
                "range_max": 0.5
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
                  "min": 897.6,
                  "max": 981.8,
                  "mean": 944.486667,
                  "std": 27.23372,
                  "n": 15
                },
                "uncertainty": {
                  "evaluation_method": "Propagation of evaluated standard uncertainties",
                  "confidence_level": 95,
                  "evaluator": "Data file compiler",
                  "assessment_num": "BLKpropAssessment_1_1"
                },
                "range_min": 897.6,
                "range_max": 981.8
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
                "org_num": "DOIcomp_3",
                "comp_num_id": "GLOBcomp_1",
                "name": "water",
                "formula": "H2O",
                "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N",
                "SMILES": "O",
                "sample_num": "DOIcompSample_3_1"
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
            "lit_num_id": "GLOBlit_7085",
            "block_number": "PROPblock_7",
            "BLKsubsys_id": null,
            "system_type": "binary",
            "comp_num_ids": [
              "GLOBcomp_2",
              "GLOBcomp_1"
            ],
            "prop_num_ids": [
              "GLOBprop_1"
            ],
            "description": "Mass density for water + ethanol (not individually inspected).",
            "doi": "10.1021/acs.jced.6b01058",
            "lit_id": "2017-sha-cha-0",
            "block_type": "PureOrMixtureData",
            "blocktype_num_id": "GLOBblocktype_1",
            "n_datapoints": 12,
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
                  "min": 966.4,
                  "max": 990.13,
                  "mean": 979.649167,
                  "std": 8.202158,
                  "n": 12
                },
                "uncertainty": {
                  "evaluation_method": "Propagation of evaluated standard uncertainties",
                  "confidence_level": 95,
                  "evaluator": "Data file compiler",
                  "assessment_num": "BLKpropAssessment_1_1"
                },
                "range_min": 966.4,
                "range_max": 990.13
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
            "lit_num_id": "GLOBlit_11504",
            "block_number": "PROPblock_6",
            "BLKsubsys_id": null,
            "system_type": "binary",
            "comp_num_ids": [
              "GLOBcomp_2",
              "GLOBcomp_1"
            ],
            "prop_num_ids": [
              "GLOBprop_1"
            ],
            "description": "Mass density for water + ethanol (not individually inspected).",
            "doi": "10.1021/je900064e",
            "lit_id": "2009-gar-gom-0",
            "block_type": "PureOrMixtureData",
            "blocktype_num_id": "GLOBblocktype_1",
            "n_datapoints": 10,
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
                "constr_num_id": "GLOBconstr_22",
                "constr_id": "volume_fraction_DOIcomp_3",
                "name": "Volume fraction",
                "type": "eComponentComposition",
                "value": 0.5,
                "digits": 1,
                "component_org_num": "DOIcomp_3",
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
                  "max": 323.15,
                  "n_unique": 8
                },
                "range_min": 288.15,
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
                "meas_num_id": "GLOBmeas_141",
                "meas_ID": "vibtub_ufactor_8",
                "method_standard": null,
                "method_custom": "VIBTUB:UFactor:8",
                "range": {
                  "BLKprop_id": "BLKprop_1",
                  "name": "Mass density, kg/m3",
                  "min": 903.71,
                  "max": 930.86,
                  "mean": 915.042,
                  "std": 9.70112,
                  "n": 10
                },
                "uncertainty": {
                  "evaluation_method": "Propagation of evaluated standard uncertainties",
                  "confidence_level": 95,
                  "evaluator": "Data file compiler",
                  "assessment_num": "BLKpropAssessment_1_1"
                },
                "range_min": 903.71,
                "range_max": 930.86
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
                "comp_num_id": "GLOBcomp_2",
                "name": "ethanol",
                "formula": "C2H6O",
                "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
                "SMILES": "CCO",
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
            "parent_n_datapoints": 10,
            "subsystem_scope": null,
            "subsystem_point_runs": [],
            "subsystem_path_class": null,
            "subsystem_evidence_quality": null,
            "subsystem_condition_ranges": []
          },
          {
            "lit_num_id": "GLOBlit_7178",
            "block_number": "PROPblock_10",
            "BLKsubsys_id": null,
            "system_type": "binary",
            "comp_num_ids": [
              "GLOBcomp_1",
              "GLOBcomp_2"
            ],
            "prop_num_ids": [
              "GLOBprop_1"
            ],
            "description": "Mass density for water + ethanol (not individually inspected).",
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
                  "min": 923.139,
                  "max": 925.8,
                  "mean": 924.4695,
                  "std": 1.881611,
                  "n": 2
                },
                "uncertainty": {
                  "evaluation_method": "Propagation of evaluated standard uncertainties",
                  "confidence_level": 95,
                  "evaluator": "Data file compiler",
                  "assessment_num": "BLKpropAssessment_1_1"
                },
                "range_min": 923.139,
                "range_max": 925.8
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
          }
        ],
        "data_inspections": [
          {
            "doi": "10.1016/j.fluid.2004.11.019",
            "block_number": "PROPblock_2",
            "table_mode": "rdp",
            "columns": [
              "BLKpoint_id",
              "temperature_k",
              "pressure_kpa",
              "mole_fraction_<ethanol>",
              "mass_density_kg_m3"
            ],
            "rows_shown": [
              {
                "BLKpoint_id": "BLKpoint_1",
                "temperature_k": "298.15",
                "pressure_kpa": "100",
                "mole_fraction_<ethanol>": "0.003",
                "mass_density_kg_m3": "995.3"
              },
              {
                "BLKpoint_id": "BLKpoint_38",
                "temperature_k": "298.15",
                "pressure_kpa": "100",
                "mole_fraction_<ethanol>": "0.2502",
                "mass_density_kg_m3": "918.5"
              },
              {
                "BLKpoint_id": "BLKpoint_43",
                "temperature_k": "298.15",
                "pressure_kpa": "100",
                "mole_fraction_<ethanol>": "0.4501",
                "mass_density_kg_m3": "868.8"
              },
              {
                "BLKpoint_id": "BLKpoint_48",
                "temperature_k": "298.15",
                "pressure_kpa": "100",
                "mole_fraction_<ethanol>": "0.6967",
                "mass_density_kg_m3": "825.2"
              },
              {
                "BLKpoint_id": "BLKpoint_54",
                "temperature_k": "298.15",
                "pressure_kpa": "100",
                "mole_fraction_<ethanol>": "1",
                "mass_density_kg_m3": "785.7"
              },
              {
                "BLKpoint_id": "BLKpoint_55",
                "temperature_k": "298.15",
                "pressure_kpa": "10000",
                "mole_fraction_<ethanol>": "0.003",
                "mass_density_kg_m3": "999.8"
              },
              {
                "BLKpoint_id": "BLKpoint_92",
                "temperature_k": "298.15",
                "pressure_kpa": "10000",
                "mole_fraction_<ethanol>": "0.2502",
                "mass_density_kg_m3": "923.3"
              },
              {
                "BLKpoint_id": "BLKpoint_97",
                "temperature_k": "298.15",
                "pressure_kpa": "10000",
                "mole_fraction_<ethanol>": "0.4501",
                "mass_density_kg_m3": "874.7"
              },
              {
                "BLKpoint_id": "BLKpoint_102",
                "temperature_k": "298.15",
                "pressure_kpa": "10000",
                "mole_fraction_<ethanol>": "0.6967",
                "mass_density_kg_m3": "832.3"
              },
              {
                "BLKpoint_id": "BLKpoint_108",
                "temperature_k": "298.15",
                "pressure_kpa": "10000",
                "mole_fraction_<ethanol>": "1",
                "mass_density_kg_m3": "794"
              },
              {
                "BLKpoint_id": "BLKpoint_109",
                "temperature_k": "298.15",
                "pressure_kpa": "20000",
                "mole_fraction_<ethanol>": "0.003",
                "mass_density_kg_m3": "1004.2"
              },
              {
                "BLKpoint_id": "BLKpoint_146",
                "temperature_k": "298.15",
                "pressure_kpa": "20000",
                "mole_fraction_<ethanol>": "0.2502",
                "mass_density_kg_m3": "928"
              },
              {
                "BLKpoint_id": "BLKpoint_151",
                "temperature_k": "298.15",
                "pressure_kpa": "20000",
                "mole_fraction_<ethanol>": "0.4501",
                "mass_density_kg_m3": "880.4"
              },
              {
                "BLKpoint_id": "BLKpoint_156",
                "temperature_k": "298.15",
                "pressure_kpa": "20000",
                "mole_fraction_<ethanol>": "0.6967",
                "mass_density_kg_m3": "839"
              },
              {
                "BLKpoint_id": "BLKpoint_162",
                "temperature_k": "298.15",
                "pressure_kpa": "20000",
                "mole_fraction_<ethanol>": "1",
                "mass_density_kg_m3": "801.9"
              },
              {
                "BLKpoint_id": "BLKpoint_163",
                "temperature_k": "298.15",
                "pressure_kpa": "30000",
                "mole_fraction_<ethanol>": "0.003",
                "mass_density_kg_m3": "1008.5"
              },
              {
                "BLKpoint_id": "BLKpoint_199",
                "temperature_k": "298.15",
                "pressure_kpa": "30000",
                "mole_fraction_<ethanol>": "0.2269",
                "mass_density_kg_m3": "938.7"
              },
              {
                "BLKpoint_id": "BLKpoint_205",
                "temperature_k": "298.15",
                "pressure_kpa": "30000",
                "mole_fraction_<ethanol>": "0.4501",
                "mass_density_kg_m3": "885.7"
              },
              {
                "BLKpoint_id": "BLKpoint_210",
                "temperature_k": "298.15",
                "pressure_kpa": "30000",
                "mole_fraction_<ethanol>": "0.6967",
                "mass_density_kg_m3": "845.1"
              },
              {
                "BLKpoint_id": "BLKpoint_216",
                "temperature_k": "298.15",
                "pressure_kpa": "30000",
                "mole_fraction_<ethanol>": "1",
                "mass_density_kg_m3": "808.9"
              },
              {
                "BLKpoint_id": "BLKpoint_217",
                "temperature_k": "298.15",
                "pressure_kpa": "40000",
                "mole_fraction_<ethanol>": "0.003",
                "mass_density_kg_m3": "1012.7"
              },
              {
                "BLKpoint_id": "BLKpoint_253",
                "temperature_k": "298.15",
                "pressure_kpa": "40000",
                "mole_fraction_<ethanol>": "0.2269",
                "mass_density_kg_m3": "942.9"
              },
              {
                "BLKpoint_id": "BLKpoint_259",
                "temperature_k": "298.15",
                "pressure_kpa": "40000",
                "mole_fraction_<ethanol>": "0.4501",
                "mass_density_kg_m3": "890.8"
              },
              {
                "BLKpoint_id": "BLKpoint_264",
                "temperature_k": "298.15",
                "pressure_kpa": "40000",
                "mole_fraction_<ethanol>": "0.6967",
                "mass_density_kg_m3": "851"
              },
              {
                "BLKpoint_id": "BLKpoint_270",
                "temperature_k": "298.15",
                "pressure_kpa": "40000",
                "mole_fraction_<ethanol>": "1",
                "mass_density_kg_m3": "815.7"
              }
            ],
            "inspection_id": "INSP_689860323003",
            "lit_num_id": "GLOBlit_220"
          },
          {
            "doi": "10.1016/j.jct.2004.07.019",
            "block_number": "PROPblock_2",
            "table_mode": "rdp",
            "columns": [
              "BLKpoint_id",
              "temperature_k",
              "pressure_kpa",
              "molality_mol_kg_<ethanol>",
              "mass_density_kg_m3"
            ],
            "rows_shown": [
              {
                "BLKpoint_id": "BLKpoint_1",
                "temperature_k": "298.15",
                "pressure_kpa": "410",
                "molality_mol_kg_<ethanol>": "0.09647",
                "mass_density_kg_m3": "-0.8568"
              },
              {
                "BLKpoint_id": "BLKpoint_6",
                "temperature_k": "298.15",
                "pressure_kpa": "410",
                "molality_mol_kg_<ethanol>": "0.94275",
                "mass_density_kg_m3": "-7.4996"
              },
              {
                "BLKpoint_id": "BLKpoint_12",
                "temperature_k": "298.15",
                "pressure_kpa": "14450",
                "molality_mol_kg_<ethanol>": "0.94273",
                "mass_density_kg_m3": "-7.71"
              },
              {
                "BLKpoint_id": "BLKpoint_19",
                "temperature_k": "298.15",
                "pressure_kpa": "14450",
                "molality_mol_kg_<ethanol>": "0.09647",
                "mass_density_kg_m3": "-0.874"
              },
              {
                "BLKpoint_id": "BLKpoint_31",
                "temperature_k": "298.15",
                "pressure_kpa": "14450",
                "molality_mol_kg_<ethanol>": "0.09647",
                "mass_density_kg_m3": "-0.874"
              },
              {
                "BLKpoint_id": "BLKpoint_42",
                "temperature_k": "298.18",
                "pressure_kpa": "29930",
                "molality_mol_kg_<ethanol>": "0.94271",
                "mass_density_kg_m3": "-7.9243"
              },
              {
                "BLKpoint_id": "BLKpoint_48",
                "temperature_k": "298.18",
                "pressure_kpa": "29930",
                "molality_mol_kg_<ethanol>": "0.94271",
                "mass_density_kg_m3": "-7.9243"
              },
              {
                "BLKpoint_id": "BLKpoint_49",
                "temperature_k": "298.18",
                "pressure_kpa": "29930",
                "molality_mol_kg_<ethanol>": "0.09646",
                "mass_density_kg_m3": "-0.9011"
              },
              {
                "BLKpoint_id": "BLKpoint_58",
                "temperature_k": "318.14",
                "pressure_kpa": "390",
                "molality_mol_kg_<ethanol>": "0.55206",
                "mass_density_kg_m3": "-4.6779"
              },
              {
                "BLKpoint_id": "BLKpoint_62",
                "temperature_k": "318.14",
                "pressure_kpa": "15370",
                "molality_mol_kg_<ethanol>": "0.55207",
                "mass_density_kg_m3": "-4.7543"
              },
              {
                "BLKpoint_id": "BLKpoint_63",
                "temperature_k": "318.14",
                "pressure_kpa": "390",
                "molality_mol_kg_<ethanol>": "0.08808",
                "mass_density_kg_m3": "-0.7809"
              },
              {
                "BLKpoint_id": "BLKpoint_71",
                "temperature_k": "318.14",
                "pressure_kpa": "390",
                "molality_mol_kg_<ethanol>": "0.08808",
                "mass_density_kg_m3": "-0.7809"
              },
              {
                "BLKpoint_id": "BLKpoint_74",
                "temperature_k": "318.14",
                "pressure_kpa": "15370",
                "molality_mol_kg_<ethanol>": "0.08808",
                "mass_density_kg_m3": "-0.7943"
              },
              {
                "BLKpoint_id": "BLKpoint_80",
                "temperature_k": "318.15",
                "pressure_kpa": "29980",
                "molality_mol_kg_<ethanol>": "0.55208",
                "mass_density_kg_m3": "-4.8174"
              },
              {
                "BLKpoint_id": "BLKpoint_85",
                "temperature_k": "318.15",
                "pressure_kpa": "29980",
                "molality_mol_kg_<ethanol>": "0.08809",
                "mass_density_kg_m3": "-0.8061"
              },
              {
                "BLKpoint_id": "BLKpoint_94",
                "temperature_k": "338.15",
                "pressure_kpa": "510",
                "molality_mol_kg_<ethanol>": "0.9427",
                "mass_density_kg_m3": "-8.0628"
              },
              {
                "BLKpoint_id": "BLKpoint_100",
                "temperature_k": "338.15",
                "pressure_kpa": "14860",
                "molality_mol_kg_<ethanol>": "0.94264",
                "mass_density_kg_m3": "-8.1024"
              },
              {
                "BLKpoint_id": "BLKpoint_113",
                "temperature_k": "338.15",
                "pressure_kpa": "510",
                "molality_mol_kg_<ethanol>": "0.09646",
                "mass_density_kg_m3": "-0.8794"
              },
              {
                "BLKpoint_id": "BLKpoint_119",
                "temperature_k": "338.15",
                "pressure_kpa": "14860",
                "molality_mol_kg_<ethanol>": "0.09646",
                "mass_density_kg_m3": "-0.8864"
              },
              {
                "BLKpoint_id": "BLKpoint_128",
                "temperature_k": "338.16",
                "pressure_kpa": "30230",
                "molality_mol_kg_<ethanol>": "0.55204",
                "mass_density_kg_m3": "-4.909"
              },
              {
                "BLKpoint_id": "BLKpoint_129",
                "temperature_k": "338.16",
                "pressure_kpa": "30230",
                "molality_mol_kg_<ethanol>": "0.10088",
                "mass_density_kg_m3": "-0.9335"
              },
              {
                "BLKpoint_id": "BLKpoint_138",
                "temperature_k": "373.17",
                "pressure_kpa": "2090",
                "molality_mol_kg_<ethanol>": "0.94262",
                "mass_density_kg_m3": "-8.8555"
              },
              {
                "BLKpoint_id": "BLKpoint_144",
                "temperature_k": "373.17",
                "pressure_kpa": "14860",
                "molality_mol_kg_<ethanol>": "0.94259",
                "mass_density_kg_m3": "-8.7729"
              },
              {
                "BLKpoint_id": "BLKpoint_150",
                "temperature_k": "373.17",
                "pressure_kpa": "30110",
                "molality_mol_kg_<ethanol>": "0.94256",
                "mass_density_kg_m3": "-8.7019"
              },
              {
                "BLKpoint_id": "BLKpoint_168",
                "temperature_k": "373.17",
                "pressure_kpa": "30110",
                "molality_mol_kg_<ethanol>": "0.94256",
                "mass_density_kg_m3": "-8.7019"
              },
              {
                "BLKpoint_id": "BLKpoint_169",
                "temperature_k": "373.17",
                "pressure_kpa": "2090",
                "molality_mol_kg_<ethanol>": "0.09645",
                "mass_density_kg_m3": "-0.9474"
              },
              {
                "BLKpoint_id": "BLKpoint_175",
                "temperature_k": "373.17",
                "pressure_kpa": "14860",
                "molality_mol_kg_<ethanol>": "0.09645",
                "mass_density_kg_m3": "-0.9386"
              },
              {
                "BLKpoint_id": "BLKpoint_181",
                "temperature_k": "373.17",
                "pressure_kpa": "30110",
                "molality_mol_kg_<ethanol>": "0.09645",
                "mass_density_kg_m3": "-0.9356"
              },
              {
                "BLKpoint_id": "BLKpoint_192",
                "temperature_k": "408.15",
                "pressure_kpa": "2040",
                "molality_mol_kg_<ethanol>": "0.94252",
                "mass_density_kg_m3": "-9.7809"
              },
              {
                "BLKpoint_id": "BLKpoint_198",
                "temperature_k": "408.15",
                "pressure_kpa": "14990",
                "molality_mol_kg_<ethanol>": "0.94247",
                "mass_density_kg_m3": "-9.585"
              },
              {
                "BLKpoint_id": "BLKpoint_204",
                "temperature_k": "408.15",
                "pressure_kpa": "29940",
                "molality_mol_kg_<ethanol>": "0.99979",
                "mass_density_kg_m3": "-9.9551"
              },
              {
                "BLKpoint_id": "BLKpoint_223",
                "temperature_k": "408.15",
                "pressure_kpa": "2040",
                "molality_mol_kg_<ethanol>": "0.09572",
                "mass_density_kg_m3": "-1.0313"
              },
              {
                "BLKpoint_id": "BLKpoint_229",
                "temperature_k": "408.15",
                "pressure_kpa": "14990",
                "molality_mol_kg_<ethanol>": "0.09572",
                "mass_density_kg_m3": "-1.0118"
              },
              {
                "BLKpoint_id": "BLKpoint_235",
                "temperature_k": "408.15",
                "pressure_kpa": "29940",
                "molality_mol_kg_<ethanol>": "0.09571",
                "mass_density_kg_m3": "-0.992"
              },
              {
                "BLKpoint_id": "BLKpoint_245",
                "temperature_k": "443.16",
                "pressure_kpa": "14970",
                "molality_mol_kg_<ethanol>": "0.99975",
                "mass_density_kg_m3": "-11.1138"
              },
              {
                "BLKpoint_id": "BLKpoint_251",
                "temperature_k": "443.16",
                "pressure_kpa": "30300",
                "molality_mol_kg_<ethanol>": "0.99973",
                "mass_density_kg_m3": "-10.7304"
              },
              {
                "BLKpoint_id": "BLKpoint_264",
                "temperature_k": "443.16",
                "pressure_kpa": "14970",
                "molality_mol_kg_<ethanol>": "0.0957",
                "mass_density_kg_m3": "-1.1033"
              },
              {
                "BLKpoint_id": "BLKpoint_270",
                "temperature_k": "443.16",
                "pressure_kpa": "30300",
                "molality_mol_kg_<ethanol>": "0.0957",
                "mass_density_kg_m3": "-1.0627"
              },
              {
                "BLKpoint_id": "BLKpoint_288",
                "temperature_k": "443.17",
                "pressure_kpa": "2110",
                "molality_mol_kg_<ethanol>": "0.09571",
                "mass_density_kg_m3": "-1.1352"
              },
              {
                "BLKpoint_id": "BLKpoint_292",
                "temperature_k": "443.17",
                "pressure_kpa": "2110",
                "molality_mol_kg_<ethanol>": "0.99977",
                "mass_density_kg_m3": "-11.4775"
              },
              {
                "BLKpoint_id": "BLKpoint_298",
                "temperature_k": "473.16",
                "pressure_kpa": "2780",
                "molality_mol_kg_<ethanol>": "0.9997",
                "mass_density_kg_m3": "-12.5432"
              },
              {
                "BLKpoint_id": "BLKpoint_304",
                "temperature_k": "473.16",
                "pressure_kpa": "14990",
                "molality_mol_kg_<ethanol>": "0.99967",
                "mass_density_kg_m3": "-12.0186"
              },
              {
                "BLKpoint_id": "BLKpoint_310",
                "temperature_k": "473.16",
                "pressure_kpa": "30050",
                "molality_mol_kg_<ethanol>": "0.99964",
                "mass_density_kg_m3": "-11.4895"
              },
              {
                "BLKpoint_id": "BLKpoint_311",
                "temperature_k": "473.16",
                "pressure_kpa": "2780",
                "molality_mol_kg_<ethanol>": "0.0957",
                "mass_density_kg_m3": "-1.2406"
              },
              {
                "BLKpoint_id": "BLKpoint_329",
                "temperature_k": "473.16",
                "pressure_kpa": "2780",
                "molality_mol_kg_<ethanol>": "0.0957",
                "mass_density_kg_m3": "-1.2406"
              },
              {
                "BLKpoint_id": "BLKpoint_335",
                "temperature_k": "473.16",
                "pressure_kpa": "14990",
                "molality_mol_kg_<ethanol>": "0.10419",
                "mass_density_kg_m3": "-1.2973"
              },
              {
                "BLKpoint_id": "BLKpoint_341",
                "temperature_k": "473.16",
                "pressure_kpa": "30050",
                "molality_mol_kg_<ethanol>": "0.10418",
                "mass_density_kg_m3": "-1.2416"
              },
              {
                "BLKpoint_id": "BLKpoint_352",
                "temperature_k": "498.15",
                "pressure_kpa": "3810",
                "molality_mol_kg_<ethanol>": "0.99959",
                "mass_density_kg_m3": "-13.5611"
              },
              {
                "BLKpoint_id": "BLKpoint_358",
                "temperature_k": "498.15",
                "pressure_kpa": "30190",
                "molality_mol_kg_<ethanol>": "0.99954",
                "mass_density_kg_m3": "-12.1289"
              },
              {
                "BLKpoint_id": "BLKpoint_371",
                "temperature_k": "498.15",
                "pressure_kpa": "3810",
                "molality_mol_kg_<ethanol>": "0.10418",
                "mass_density_kg_m3": "-1.4613"
              },
              {
                "BLKpoint_id": "BLKpoint_383",
                "temperature_k": "498.15",
                "pressure_kpa": "30190",
                "molality_mol_kg_<ethanol>": "0.10418",
                "mass_density_kg_m3": "-1.3031"
              },
              {
                "BLKpoint_id": "BLKpoint_394",
                "temperature_k": "498.16",
                "pressure_kpa": "15030",
                "molality_mol_kg_<ethanol>": "1.04067",
                "mass_density_kg_m3": "-13.3718"
              },
              {
                "BLKpoint_id": "BLKpoint_401",
                "temperature_k": "498.16",
                "pressure_kpa": "15030",
                "molality_mol_kg_<ethanol>": "0.10418",
                "mass_density_kg_m3": "-1.3877"
              },
              {
                "BLKpoint_id": "BLKpoint_412",
                "temperature_k": "523.14",
                "pressure_kpa": "5880",
                "molality_mol_kg_<ethanol>": "1.04065",
                "mass_density_kg_m3": "-15.3473"
              },
              {
                "BLKpoint_id": "BLKpoint_418",
                "temperature_k": "523.14",
                "pressure_kpa": "15560",
                "molality_mol_kg_<ethanol>": "1.04063",
                "mass_density_kg_m3": "-14.4002"
              },
              {
                "BLKpoint_id": "BLKpoint_424",
                "temperature_k": "523.14",
                "pressure_kpa": "30170",
                "molality_mol_kg_<ethanol>": "1.04062",
                "mass_density_kg_m3": "-13.3657"
              },
              {
                "BLKpoint_id": "BLKpoint_443",
                "temperature_k": "523.14",
                "pressure_kpa": "5880",
                "molality_mol_kg_<ethanol>": "0.10417",
                "mass_density_kg_m3": "-1.5874"
              },
              {
                "BLKpoint_id": "BLKpoint_449",
                "temperature_k": "523.14",
                "pressure_kpa": "15560",
                "molality_mol_kg_<ethanol>": "0.10417",
                "mass_density_kg_m3": "-1.4921"
              },
              {
                "BLKpoint_id": "BLKpoint_455",
                "temperature_k": "523.14",
                "pressure_kpa": "30170",
                "molality_mol_kg_<ethanol>": "0.10416",
                "mass_density_kg_m3": "-1.3907"
              },
              {
                "BLKpoint_id": "BLKpoint_466",
                "temperature_k": "548.16",
                "pressure_kpa": "8000",
                "molality_mol_kg_<ethanol>": "1.04058",
                "mass_density_kg_m3": "-17.0046"
              },
              {
                "BLKpoint_id": "BLKpoint_472",
                "temperature_k": "548.16",
                "pressure_kpa": "15960",
                "molality_mol_kg_<ethanol>": "1.04054",
                "mass_density_kg_m3": "-15.7466"
              },
              {
                "BLKpoint_id": "BLKpoint_478",
                "temperature_k": "548.16",
                "pressure_kpa": "30120",
                "molality_mol_kg_<ethanol>": "1.04051",
                "mass_density_kg_m3": "-14.2262"
              },
              {
                "BLKpoint_id": "BLKpoint_496",
                "temperature_k": "548.16",
                "pressure_kpa": "30120",
                "molality_mol_kg_<ethanol>": "1.04051",
                "mass_density_kg_m3": "-14.2262"
              },
              {
                "BLKpoint_id": "BLKpoint_497",
                "temperature_k": "548.16",
                "pressure_kpa": "8000",
                "molality_mol_kg_<ethanol>": "0.0881",
                "mass_density_kg_m3": "-1.4865"
              },
              {
                "BLKpoint_id": "BLKpoint_503",
                "temperature_k": "548.16",
                "pressure_kpa": "15960",
                "molality_mol_kg_<ethanol>": "0.0881",
                "mass_density_kg_m3": "-1.3838"
              },
              {
                "BLKpoint_id": "BLKpoint_509",
                "temperature_k": "548.16",
                "pressure_kpa": "30120",
                "molality_mol_kg_<ethanol>": "0.0881",
                "mass_density_kg_m3": "-1.2547"
              },
              {
                "BLKpoint_id": "BLKpoint_519",
                "temperature_k": "573.14",
                "pressure_kpa": "30090",
                "molality_mol_kg_<ethanol>": "1.04039",
                "mass_density_kg_m3": "-15.3285"
              },
              {
                "BLKpoint_id": "BLKpoint_525",
                "temperature_k": "573.14",
                "pressure_kpa": "30090",
                "molality_mol_kg_<ethanol>": "0.08809",
                "mass_density_kg_m3": "-1.3474"
              },
              {
                "BLKpoint_id": "BLKpoint_535",
                "temperature_k": "573.15",
                "pressure_kpa": "10150",
                "molality_mol_kg_<ethanol>": "1.04048",
                "mass_density_kg_m3": "-19.634"
              },
              {
                "BLKpoint_id": "BLKpoint_554",
                "temperature_k": "573.15",
                "pressure_kpa": "10150",
                "molality_mol_kg_<ethanol>": "0.0881",
                "mass_density_kg_m3": "-1.7035"
              },
              {
                "BLKpoint_id": "BLKpoint_560",
                "temperature_k": "573.15",
                "pressure_kpa": "18040",
                "molality_mol_kg_<ethanol>": "0.08809",
                "mass_density_kg_m3": "-1.5198"
              },
              {
                "BLKpoint_id": "BLKpoint_565",
                "temperature_k": "573.15",
                "pressure_kpa": "18040",
                "molality_mol_kg_<ethanol>": "1.04045",
                "mass_density_kg_m3": "-17.3814"
              }
            ],
            "inspection_id": "INSP_b3500349e479",
            "lit_num_id": "GLOBlit_2432"
          },
          {
            "doi": "10.1016/j.jct.2018.02.022",
            "block_number": "PROPblock_19",
            "table_mode": "rdp",
            "columns": [
              "BLKpoint_id",
              "temperature_k",
              "mole_fraction_<ethanol>",
              "pressure_kpa",
              "mass_density_kg_m3"
            ],
            "rows_shown": [
              {
                "BLKpoint_id": "BLKpoint_1",
                "temperature_k": "293.15",
                "mole_fraction_<ethanol>": "0.0024",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "997.039"
              },
              {
                "BLKpoint_id": "BLKpoint_23",
                "temperature_k": "293.15",
                "mole_fraction_<ethanol>": "0.7006",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "829.434"
              },
              {
                "BLKpoint_id": "BLKpoint_59",
                "temperature_k": "298.15",
                "mole_fraction_<ethanol>": "0.7006",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "825.07"
              },
              {
                "BLKpoint_id": "BLKpoint_95",
                "temperature_k": "303.15",
                "mole_fraction_<ethanol>": "0.7006",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "820.66"
              },
              {
                "BLKpoint_id": "BLKpoint_131",
                "temperature_k": "308.15",
                "mole_fraction_<ethanol>": "0.7006",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "816.2"
              },
              {
                "BLKpoint_id": "BLKpoint_145",
                "temperature_k": "293.15",
                "mole_fraction_<ethanol>": "0",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "998.429"
              },
              {
                "BLKpoint_id": "BLKpoint_146",
                "temperature_k": "298.15",
                "mole_fraction_<ethanol>": "0",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "997.267"
              },
              {
                "BLKpoint_id": "BLKpoint_147",
                "temperature_k": "303.15",
                "mole_fraction_<ethanol>": "0",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "995.867"
              },
              {
                "BLKpoint_id": "BLKpoint_148",
                "temperature_k": "308.15",
                "mole_fraction_<ethanol>": "0",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "994.252"
              },
              {
                "BLKpoint_id": "BLKpoint_149",
                "temperature_k": "293.15",
                "mole_fraction_<ethanol>": "1",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "789.547"
              },
              {
                "BLKpoint_id": "BLKpoint_150",
                "temperature_k": "298.15",
                "mole_fraction_<ethanol>": "1",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "785.26"
              },
              {
                "BLKpoint_id": "BLKpoint_151",
                "temperature_k": "303.15",
                "mole_fraction_<ethanol>": "1",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "780.941"
              },
              {
                "BLKpoint_id": "BLKpoint_152",
                "temperature_k": "308.15",
                "mole_fraction_<ethanol>": "1",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "776.592"
              },
              {
                "BLKpoint_id": "BLKpoint_160",
                "temperature_k": "293.15",
                "mole_fraction_<ethanol>": "0.1984",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "935.19"
              },
              {
                "BLKpoint_id": "BLKpoint_165",
                "temperature_k": "293.15",
                "mole_fraction_<ethanol>": "0.4495",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "873.57"
              },
              {
                "BLKpoint_id": "BLKpoint_183",
                "temperature_k": "298.15",
                "mole_fraction_<ethanol>": "0.1984",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "931.84"
              },
              {
                "BLKpoint_id": "BLKpoint_188",
                "temperature_k": "298.15",
                "mole_fraction_<ethanol>": "0.4495",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "869.34"
              },
              {
                "BLKpoint_id": "BLKpoint_206",
                "temperature_k": "303.15",
                "mole_fraction_<ethanol>": "0.1984",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "928.77"
              },
              {
                "BLKpoint_id": "BLKpoint_211",
                "temperature_k": "303.15",
                "mole_fraction_<ethanol>": "0.4495",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "865.03"
              },
              {
                "BLKpoint_id": "BLKpoint_229",
                "temperature_k": "308.15",
                "mole_fraction_<ethanol>": "0.1984",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "925.04"
              },
              {
                "BLKpoint_id": "BLKpoint_234",
                "temperature_k": "308.15",
                "mole_fraction_<ethanol>": "0.4495",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "860.66"
              },
              {
                "BLKpoint_id": "BLKpoint_244",
                "temperature_k": "308.15",
                "mole_fraction_<ethanol>": "0.929",
                "pressure_kpa": "92.3",
                "mass_density_kg_m3": "785.46"
              }
            ],
            "inspection_id": "INSP_b49f3d6ec58f",
            "lit_num_id": "GLOBlit_5201"
          }
        ]
      }
    }
  ]
}
</subagent_answer>
```
</details>

**📦 Context compaction** (after step 4, trigger: chars=98928>80000)
- **Outcome:** skipped_by_agent
- **Purpose:** Ready to proceed with fit_block_derived for density→VE transform; context is large but manageable for next steps
- **Tasks:** SKIP
- 98,928 → 98,928 chars (−0%)

---

### Step 5 [main - A_2 · c18]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "purpose": "Inspect GLOBlit_9006::PROPblock_1 for water+ethanol density at 298.15 K to verify composition range and data structure"
}
```
</details>

- **Result:** 295 chars  |  **Time:** 0.0s  |  **Started:** 02:39:22 (t+344.4s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to inspect_block: missing a required argument: 'tasks'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 6 [main - A_2 · c19]: `inspect_block` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "purpose": "Inspect density block for water+ethanol to verify composition coverage at 298.15 K",
  "tasks": [
    "verify columns",
    "check composition range",
    "check temperature coverage"
  ]
}
```
</details>

- **Result:** 397 chars  |  **Time:** 0.0s  |  **Started:** 02:39:29 (t+352.2s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ inspect_block** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block.tasks received ['verify columns', 'check composition range', 'check temperature coverage'] (list); expected <class 'str'>; tool arguments are never coerced

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 7 [main - A_2 · c20]: `inspect_block`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "purpose": "Verify columns and composition range for water+ethanol density at 298.15 K",
  "tasks": "verify columns, check composition range, check temperature coverage"
}
```
</details>

- **Result:** 1,359 chars  |  **Time:** 0.1s  |  **Started:** 02:39:37 (t+360.0s)

<details><summary>Result</summary>

```
**Block GLOBlit_9006 / DOI 10.1021/je060335h / PROPblock_1 @ declared** (PureOrMixtureData)
Compounds: ethanol, water | Rows: 164
x‑columns: ['mole_fraction_<ethanol>'] | y‑columns: ['mass_density_kg_m3']

**Property response semantics (reported metadata; values are not materialized here)**
- **BLKprop_1 / GLOBprop_1** `mass_density_kg_m3` (mass_density_kg_m3)
  - reported response: Direct value, X
  - measurement: GLOBmeas_134 / vibtub_ufactor_4
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
| temperature_k | 283.15 | 298.15 | 164 |
| mole_fraction_<ethanol> | 0 | 1 | 164 |
| pressure_kpa | 101 | 101 | 164 |
| mass_density_kg_m3 | 785.22 | 999.7 | 164 |

```
</details>

**📦 Context compaction** (after step 7, trigger: chars=101375>80000)
- **Outcome:** skipped_by_agent
- **Purpose:** About to run fit_block_derived on two blocks for density→V^E; context is large but manageable for next steps
- **Tasks:** SKIP
- 101,375 → 101,375 chars (−0%)

---

### Step 8 [main - A_2 · c21]: `fit_block_derived` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "transform": "density_to_molar_volume",
  "property_hint": "mass_density_kg_m3",
  "composition_hint": "mole_fraction",
  "x_vars": [
    "Mole fraction of ethanol"
  ],
  "y_props": [
    "Mass density, kg/m3"
  ],
  "x_vars_constrained": {
    "Temperature, K": {
      "value": 298.15,
      "tol": 0.5
    }
  },
  "max_rk_order": 5,
  "purpose": "Compute excess molar volume from density data for water+ethanol at 298.15 K",
  "tasks": [
    "fit"
  ]
}
```
</details>

- **Result:** 337 chars  |  **Time:** 0.0s  |  **Started:** 02:39:58 (t+380.9s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ fit_block_derived** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: fit_block_derived.tasks received ['fit'] (list); expected <class 'str'>; tool arguments are never coerced

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 9 [main - A_2 · c22]: `fit_block_derived`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "transform": "density_to_excess_molar_volume",
  "property_hint": "mass_density_kg_m3",
  "composition_hint": "mole_fraction",
  "x_vars_constrained": {
    "Temperature, K": {
      "value": 298.15,
      "tol": 0.5
    }
  },
  "max_rk_order": 5,
  "purpose": "Derive excess molar volume from density data for water+ethanol at 298.15 K",
  "tasks": "fit"
}
```
</details>

- **Result:** 208 chars  |  **Time:** 0.1s  |  **Started:** 02:40:06 (t+388.5s)

<details><summary>Result</summary>

```
**Fit error** (GLOBlit_9006 / DOI 10.1021/je060335h / PROPblock_1): Unknown transform 'density_to_excess_molar_volume'. Available: ['density_to_molar_volume', 'kappa_s_from_rho_u', 'molar_volume_to_density']

```
</details>

**📦 Context compaction** (after step 9, trigger: chars=102316>80000)
- **Outcome:** skipped_by_agent
- **Purpose:** Need to use density_to_molar_volume transform then fit excess, context is large but manageable for next steps
- **Tasks:** SKIP
- 102,316 → 102,316 chars (−0%)

---

### Step 10 [main - A_2 · c23]: `fit_block_derived` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "transform": "density_to_molar_volume",
  "property_hint": "mass_density_kg_m3",
  "composition_hint": "mole_fraction",
  "x_vars_constrained": {
    "Temperature, K": {
      "value": 298.15,
      "tol": 0.5
    }
  },
  "max_rk_order": 5
}
```
</details>

- **Result:** 305 chars  |  **Time:** 0.0s  |  **Started:** 02:40:21 (t+403.5s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ fit_block_derived** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to fit_block_derived: missing a required argument: 'purpose'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 11 [main - A_2 · c24]: `fit_block_derived` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "transform": "density_to_molar_volume",
  "property_hint": "mass_density_kg_m3",
  "composition_hint": "mole_fraction",
  "x_vars_constrained": {
    "Temperature, K": {
      "value": 298.15,
      "tol": 0.5
    }
  },
  "max_rk_order": 5,
  "purpose": "Derive excess molar volume (V^E) from measured density data for water+ethanol at 298.15 K"
}
```
</details>

- **Result:** 303 chars  |  **Time:** 0.0s  |  **Started:** 02:40:29 (t+412.1s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ fit_block_derived** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to fit_block_derived: missing a required argument: 'tasks'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 12 [main - A_2 · c25]: `fit_block_derived` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "transform": "density_to_molar_volume",
  "property_hint": "mass_density_kg_m3",
  "composition_hint": "mole_fraction",
  "x_vars_constrained": "{\"Temperature, K\": {\"value\": 298.15, \"tol\": 0.5}}",
  "max_rk_order": 5,
  "purpose": "Derive excess molar volume from density data for water+ethanol at 298.15 K",
  "tasks": [
    "fit_derived"
  ]
}
```
</details>

- **Result:** 345 chars  |  **Time:** 0.0s  |  **Started:** 02:40:36 (t+419.1s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ fit_block_derived** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: fit_block_derived.tasks received ['fit_derived'] (list); expected <class 'str'>; tool arguments are never coerced

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 13 [main - A_2 · c26]: `fit_block_derived` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "transform": "density_to_molar_volume",
  "property_hint": "mass_density_kg_m3",
  "composition_hint": "mole_fraction",
  "x_vars_constrained": "{\"Temperature, K\": {\"value\": 298.15, \"tol\": 0.5}}",
  "max_rk_order": 5,
  "purpose": "Derive excess molar volume from density data for water+ethanol at 298.15 K",
  "tasks": "fit_derived"
}
```
</details>

- **Result:** 301 chars  |  **Time:** 0.0s  |  **Started:** 02:40:44 (t+426.6s)
- **Error:** `{
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: fit_block_derived.x_vars_constrained received '{\"Temperature, K\": {\"value\": 298.15, \"tol\": 0.5}}' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINEMENT_REQUIRED",
  "tool": "fit_block_derived"
}`

**📦 Context compaction** (after step 13, trigger: chars=104215>80000)
- **Outcome:** skipped_by_agent
- **Purpose:** Need to run fit_block_derived with correct argument types; context is large but manageable for a few more turns
- **Tasks:** SKIP
- 104,215 → 104,215 chars (−0%)

---

### Step 14 [main - A_2 · c27]: `fit_block_derived` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "transform": "density_to_molar_volume",
  "property_hint": "mass_density_kg_m3",
  "composition_hint": "mole_fraction",
  "x_vars_constrained": {
    "Temperature, K": {
      "value": 298.15,
      "tol": 0.5
    }
  },
  "max_rk_order": 5,
  "purpose": "Derive excess molar volume from density data for water+ethanol at 298.15 K"
}
```
</details>

- **Result:** 303 chars  |  **Time:** 0.0s  |  **Started:** 02:40:59 (t+441.5s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ fit_block_derived** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to fit_block_derived: missing a required argument: 'tasks'

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 15 [main - A_2 · c28]: `fit_block_derived` 🔒 VALIDATION BLOCKED

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "transform": "density_to_molar_volume",
  "property_hint": "mass_density_kg_m3",
  "composition_hint": "mole_fraction",
  "x_vars_constrained": {
    "Temperature, K": {
      "value": 298.15,
      "tol": 0.5
    }
  },
  "max_rk_order": 5,
  "purpose": "Derive excess molar volume from measured density for water+ethanol at 298.15 K",
  "tasks": [
    "fit_block_derived"
  ]
}
```
</details>

- **Result:** 351 chars  |  **Time:** 0.0s  |  **Started:** 02:41:05 (t+447.8s)
- **Status:** blocked

<details><summary>Validation detail</summary>

```
**✗ fit_block_derived** — tool syntax or arguments need correction:
TOOL_ARGUMENT_REFINEMENT_REQUIRED: fit_block_derived.tasks received ['fit_block_derived'] (list); expected <class 'str'>; tool arguments are never coerced

_No tool in this batch executed. Re-emit the complete batch with only registered tool names and exact declared JSON arguments._
```
</details>

---

### Step 16 [main - A_2 · c29]: `fit_block_derived`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "transform": "density_to_molar_volume",
  "property_hint": "mass_density_kg_m3",
  "composition_hint": "mole_fraction",
  "x_vars_constrained": {
    "Temperature, K": {
      "value": 298.15,
      "tol": 0.5
    }
  },
  "max_rk_order": 5,
  "purpose": "Derive excess molar volume from density data for water+ethanol at 298.15 K",
  "tasks": "fit_block_derived"
}
```
</details>

- **Result:** 230 chars  |  **Time:** 0.1s  |  **Started:** 02:41:12 (t+454.5s)

<details><summary>Result</summary>

```
**Fit error** (GLOBlit_9006 / DOI 10.1021/je060335h / PROPblock_1): Constraint column 'Temperature, K' not found
Columns available: ['BLKpoint_id', 'temperature_k', 'mole_fraction_<ethanol>', 'pressure_kpa', 'mass_density_kg_m3']

```
</details>

**📦 Context compaction** (after step 16, trigger: chars=105555>80000)
- **Outcome:** skipped_by_agent
- **Purpose:** Need to fix constraint column name to 'temperature_k' (lowercase) and run fit_block_derived successfully
- **Tasks:** SKIP
- 105,555 → 105,555 chars (−0%)

---

### Step 17 [main - A_2 · c30]: `fit_block_derived`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "transform": "density_to_molar_volume",
  "property_hint": "mass_density_kg_m3",
  "composition_hint": "mole_fraction",
  "x_vars": [
    "mole_fraction_<ethanol>"
  ],
  "y_props": [
    "mass_density_kg_m3"
  ],
  "x_vars_constrained": {
    "temperature_k": {
      "value": 298.15,
      "tol": 0.5
    }
  },
  "max_rk_order": 5,
  "purpose": "Derive excess molar volume from density for water+ethanol at 298.15 K",
  "tasks": "fit_block_derived density_to_molar_volume"
}
```
</details>

- **Result:** 954 chars  |  **Time:** 1.8s  |  **Started:** 02:41:39 (t+481.4s)

<details><summary>Result</summary>

```
**RK Fit** — GLOBlit_9006 / DOI 10.1021/je060335h / PROPblock_1 @ declared
Components: ethanol, water | Mixing rule: linear
Points: 38 mixture / 164 total
Property response: BLKprop_1 / GLOBprop_1; kind=direct; equation=X = reported X; reference_sources=0; units=kg/m3 -> kg/m3.

| Component | Pure value |
|-----------|-----------|
| ethanol | 5.8670182e-05 |
| water | 1.8262917e-05 |
Pure values: block-edges of derived data (water: direct/good, ethanol: direct/good)

BIC-selected order: 5 | R² = 0.996842 | RMSE = 1.68833e-08 | BIC = -1338.34
Coefficients: [-4.64231e-06, 1.53527e-06, -1.75543e-06, -1.45074e-07, -8.27523e-07, 1.86938e-06]

| Order | BIC | R² | RMSE |
|-------|-----|----|------|
| 0 | -1183.19 | 0.697623 | 1.65192e-07 |
| 1 | -1236.90 | 0.933140 | 7.76784e-08 |
| 2 | -1310.57 | 0.991259 | 2.80868e-08 |
| 3 | -1334.96 | 0.995819 | 1.94252e-08 |
| 4 | -1338.07 | 0.996499 | 1.77751e-08 |
| 5 | -1338.34 | 0.996842 | 1.68833e-08 |

```
</details>

**📦 Context compaction** (after step 17, trigger: chars=106856>80000)
- **Outcome:** skipped_by_agent
- **Purpose:** I have the completed fit result and need to extract the excess molar volume minimum from the fit. Ready to assemble the final answer.
- **Tasks:** SKIP
- 106,856 → 106,856 chars (−0%)

---

### Step 18 [main - A_2 · c31]: `predict_from_rk`

<details><summary>Arguments</summary>

```json
{
  "coeffs": [
    -4.64231e-06,
    1.53527e-06,
    -1.75543e-06,
    -1.45074e-07,
    -8.27523e-07,
    1.86938e-06
  ],
  "pure_values": {
    "ethanol": 5.8670182e-05,
    "water": 1.8262917e-05
  },
  "property_type": "molar_volume",
  "n_points": 101,
  "purpose": "Predict full V^E curve for water+ethanol at 298.15 K to find minimum V^E and its composition",
  "tasks": "predict"
}
```
</details>

- **Result:** 205 chars  |  **Time:** 0.1s  |  **Started:** 02:41:59 (t+501.3s)

<details><summary>Result</summary>

```
**RK Prediction** (order 5, linear)
Components: ethanol, water | 101 grid points
Y(x=0) = 1.82629e-05, Y(x=0.5) ≈ 3.7306e-05, Y(x=1) = 5.86702e-05
Y_max = 5.86702e-05 at x1 = 1
Max |excess| = -1.20529e-06

```
</details>

**📦 Context compaction** (after step 18, trigger: chars=107460>80000)
- **Outcome:** skipped_by_agent
- **Purpose:** I have the completed fit and prediction results; ready to assemble final answer
- **Tasks:** SKIP
- 107,460 → 107,460 chars (−0%)

---

### Step 19 [main - A_2 · c32]: `fit_block_derived`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1016/j.jct.2018.02.022",
  "block_number": "PROPblock_19",
  "transform": "density_to_molar_volume",
  "property_hint": "mass_density_kg_m3",
  "composition_hint": "mole_fraction",
  "x_vars_constrained": {
    "temperature_k": {
      "value": 298.15,
      "tol": 0.5
    }
  },
  "max_rk_order": 5,
  "purpose": "Fit density_to_molar_volume for water+ethanol at 298.15 K from GLOBlit_5201",
  "tasks": "fit_block_derived"
}
```
</details>

- **Result:** 961 chars  |  **Time:** 1.9s  |  **Started:** 02:42:18 (t+521.0s)

<details><summary>Result</summary>

```
**RK Fit** — GLOBlit_5201 / DOI 10.1016/j.jct.2018.02.022 / PROPblock_19 @ declared
Components: ethanol, water | Mixing rule: linear
Points: 56 mixture / 244 total
Property response: BLKprop_1 / GLOBprop_1; kind=direct; equation=X = reported X; reference_sources=0; units=kg/m3 -> kg/m3.

| Component | Pure value |
|-----------|-----------|
| ethanol | 5.8206813e-05 |
| water | 1.8110836e-05 |
Pure values: block-edges of derived data (water: direct/good, ethanol: direct/good)

BIC-selected order: 5 | R² = 0.990020 | RMSE = 3.74581e-08 | BIC = -1891.05
Coefficients: [-3.38039e-06, 2.37917e-06, -2.95307e-06, -2.37709e-06, 7.23821e-06, 7.40816e-06]

| Order | BIC | R² | RMSE |
|-------|-----|----|------|
| 0 | -1714.52 | 0.665581 | 2.16828e-07 |
| 1 | -1797.66 | 0.929482 | 9.95678e-08 |
| 2 | -1807.80 | 0.945237 | 8.77431e-08 |
| 3 | -1835.03 | 0.968664 | 6.6373e-08 |
| 4 | -1875.33 | 0.985800 | 4.46799e-08 |
| 5 | -1891.05 | 0.990020 | 3.74581e-08 |

```
</details>

**📦 Context compaction** (after step 19, trigger: chars=108829>80000)
- **Outcome:** skipped_by_agent
- **Purpose:** I have both fits complete and prediction results; ready to assemble final answer
- **Tasks:** SKIP
- 108,829 → 108,829 chars (−0%)

---

### Step 20 [main - A_2 · c33]: `predict_from_rk`

<details><summary>Arguments</summary>

```json
{
  "property_type": "molar_volume",
  "coeffs": [
    -3.38039e-06,
    2.37917e-06,
    -2.95307e-06,
    -2.37709e-06,
    7.23821e-06,
    7.40816e-06
  ],
  "pure_values": {
    "ethanol": 5.8206813e-05,
    "water": 1.8110836e-05
  },
  "n_points": 101,
  "mixing_rule": "linear",
  "purpose": "Predict V^E curve from GLOBlit_5201 fit to find minimum excess molar volume",
  "tasks": "predict excess molar volume curve"
}
```
</details>

- **Result:** 206 chars  |  **Time:** 0.1s  |  **Started:** 02:42:41 (t+543.7s)

<details><summary>Result</summary>

```
**RK Prediction** (order 5, linear)
Components: ethanol, water | 101 grid points
Y(x=0) = 1.81108e-05, Y(x=0.5) ≈ 3.73137e-05, Y(x=1) = 5.82068e-05
Y_max = 5.82068e-05 at x1 = 1
Max |excess| = -9.68328e-07

```
</details>

**📦 Context compaction** (after step 20, trigger: chars=109350>80000)
- **Outcome:** skipped_by_agent
- **Purpose:** I have both fits complete and predictions done; ready to assemble final answer
- **Tasks:** SKIP
- 109,350 → 109,350 chars (−0%)

---

### Step 21 [main - A_2 · c34]: `list_session_files`

- **Result:** 3,077 chars  |  **Time:** 0.0s  |  **Started:** 02:43:10 (t+573.1s)

<details><summary>Result</summary>

```
{
  "session_dir": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Main\\run_20260905_023326_012061_3dba9dd4\\analysis_runs\\run_4",
  "n_files": 8,
  "files": [
    {
      "category": "data",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Main\\run_20260905_023326_012061_3dba9dd4\\analysis_runs\\run_4\\data\\10_1021_je060335h_BPROPblock_1_T298.1_fit.csv",
      "description": "RK fit data \u2014 10.1021/je060335h PROPblock_1_T298.1"
    },
    {
      "category": "data",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Main\\run_20260905_023326_012061_3dba9dd4\\analysis_runs\\run_4\\data\\10_1021_je060335h_BPROPblock_1_T298.1_excess.csv",
      "description": "Excess property \u2014 10.1021/je060335h PROPblock_1_T298.1"
    },
    {
      "category": "plot",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Main\\run_20260905_023326_012061_3dba9dd4\\analysis_runs\\run_4\\plots\\10_1021_je060335h_BPROPblock_1_T298.1_fit.png",
      "description": "RK fit plot \u2014 10.1021/je060335h PROPblock_1_T298.1"
    },
    {
      "category": "plot",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Main\\run_20260905_023326_012061_3dba9dd4\\analysis_runs\\run_4\\plots\\10_1021_je060335h_BPROPblock_1_T298.1_excess.png",
      "description": "Excess plot \u2014 10.1021/je060335h PROPblock_1_T298.1"
    },
    {
      "category": "data",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Main\\run_20260905_023326_012061_3dba9dd4\\analysis_runs\\run_4\\data\\10_1016_j_jct_2018_02_022_BPROPblock_19_T298.1_fit.csv",
      "description": "RK fit data \u2014 10.1016/j.jct.2018.02.022 PROPblock_19_T298.1"
    },
    {
      "category": "data",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Main\\run_20260905_023326_012061_3dba9dd4\\analysis_runs\\run_4\\data\\10_1016_j_jct_2018_02_022_BPROPblock_19_T298.1_excess.csv",
      "description": "Excess property \u2014 10.1016/j.jct.2018.02.022 PROPblock_19_T298.1"
    },
    {
      "category": "plot",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Main\\run_20260905_023326_012061_3dba9dd4\\analysis_runs\\run_4\\plots\\10_1016_j_jct_2018_02_022_BPROPblock_19_T298.1_fit.png",
      "description": "RK fit plot \u2014 10.1016/j.jct.2018.02.022 PROPblock_19_T298.1"
    },
    {
      "category": "plot",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Main\\run_20260905_023326_012061_3dba9dd4\\analysis_runs\\run_4\\plots\\10_1016_j_jct_2018_02_022_BPROPblock_19_T298.1_excess.png",
      "description": "Excess plot \u2014 10.1016/j.jct.2018.02.022 PROPblock_19_T298.1"
    }
  ]
}
```
</details>

**📦 Context compaction** (after step 21, trigger: chars=112704>80000)
- **Outcome:** skipped_by_agent
- **Purpose:** I have all fitting results and am ready to assemble the final answer
- **Tasks:** SKIP
- 112,704 → 112,704 chars (−0%)

---

### Step 23 [main - A_2 · c35]: `inspect_block`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "purpose": "Ground data values for GLOBlit_9006::PROPblock_1 at 298.15 K",
  "tasks": "Inspect block table to verify conditions and data ranges"
}
```
</details>

- **Result:** 1,359 chars  |  **Time:** 0.1s  |  **Started:** 02:44:41 (t+664.3s)

<details><summary>Result</summary>

```
**Block GLOBlit_9006 / DOI 10.1021/je060335h / PROPblock_1 @ declared** (PureOrMixtureData)
Compounds: ethanol, water | Rows: 164
x‑columns: ['mole_fraction_<ethanol>'] | y‑columns: ['mass_density_kg_m3']

**Property response semantics (reported metadata; values are not materialized here)**
- **BLKprop_1 / GLOBprop_1** `mass_density_kg_m3` (mass_density_kg_m3)
  - reported response: Direct value, X
  - measurement: GLOBmeas_134 / vibtub_ufactor_4
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
| temperature_k | 283.15 | 298.15 | 164 |
| mole_fraction_<ethanol> | 0 | 1 | 164 |
| pressure_kpa | 101 | 101 | 164 |
| mass_density_kg_m3 | 785.22 | 999.7 | 164 |

```
</details>

**📦 Context compaction** (after step 23, trigger: chars=128578>80000)
- **Outcome:** skipped_by_agent
- **Purpose:** Ready to assemble final answer with all fits complete; context is manageable
- **Tasks:** SKIP
- 128,578 → 128,578 chars (−0%)

---

### Step 25 [main - A_2 · c36]: `inspect_block`

<details><summary>Arguments</summary>

```json
{
  "doi": "10.1021/je060335h",
  "block_number": "PROPblock_1",
  "purpose": "Ground block metadata values for PROPblock_1",
  "tasks": "Inspect block structure to verify column ranges and row count"
}
```
</details>

- **Result:** 1,359 chars  |  **Time:** 0.1s  |  **Started:** 02:45:51 (t+734.3s)

<details><summary>Result</summary>

```
**Block GLOBlit_9006 / DOI 10.1021/je060335h / PROPblock_1 @ declared** (PureOrMixtureData)
Compounds: ethanol, water | Rows: 164
x‑columns: ['mole_fraction_<ethanol>'] | y‑columns: ['mass_density_kg_m3']

**Property response semantics (reported metadata; values are not materialized here)**
- **BLKprop_1 / GLOBprop_1** `mass_density_kg_m3` (mass_density_kg_m3)
  - reported response: Direct value, X
  - measurement: GLOBmeas_134 / vibtub_ufactor_4
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
| temperature_k | 283.15 | 298.15 | 164 |
| mole_fraction_<ethanol> | 0 | 1 | 164 |
| pressure_kpa | 101 | 101 | 164 |
| mass_density_kg_m3 | 785.22 | 999.7 | 164 |

```
</details>

**📦 Context compaction** (after step 25, trigger: chars=141008>80000)
- **Outcome:** skipped_by_agent
- **Purpose:** About to give final answer, no more tool calls needed
- **Tasks:** SKIP
- 141,008 → 141,008 chars (−0%)

---

## Nested tool calls — L1_1 (L1-query)

**Nest:** main - A_2 - L1_1
**Parent:** `query_thermoml_parallel` — Step 4 [main - A_2 · c17] relays this worker's result
**Started:** 02:34:20  |  **Ended:** 02:36:26  |  **Tool calls:** 5

---

### Step 2 [main - A_2 - L1_1 · c5]: `resolve_compound_ids`

<details><summary>Arguments</summary>

```json
{
  "queries": [
    "water 7732-18-5",
    "ethanol 64-17-5"
  ],
  "min_score": 70,
  "limit": 5,
  "purpose": "Resolve water and ethanol to global compound IDs",
  "tasks": "Find GLOBcomp IDs for water and ethanol"
}
```
</details>

- **Result:** 270 chars  |  **Time:** 5.7s  |  **Started:** 02:34:30 (t+53.2s)
- **Subagent:** KEEP in 351 → 270 chars (5.0s)
  - Both water and ethanol resolved successfully to global compound IDs.

| Name | ID | Formula | SMILES |
|---|---|---|---|
| water | GLOBcomp_1 | H2O | O |
| ethanol | GLOBcomp_2 | C2H6O | CCO |

(GLOBc

<details><summary>Result</summary>

```
Both water and ethanol resolved successfully to global compound IDs.

| Name | ID | Formula | SMILES |
|---|---|---|---|
| water | GLOBcomp_1 | H2O | O |
| ethanol | GLOBcomp_2 | C2H6O | CCO |

(GLOBcomp_5494 "ethanol-1-d" is a deuterated variant and not relevant here.)
```
</details>

---

### Step 4 [main - A_2 - L1_1 · c6]: `resolve_property_ids`

<details><summary>Arguments</summary>

```json
{
  "queries": [
    "excess molar volume"
  ],
  "min_score": 60,
  "limit": 10,
  "purpose": "Find excess molar volume property ID",
  "tasks": "Resolve excess molar volume to its GLOBprop ID"
}
```
</details>

- **Result:** 256 chars  |  **Time:** 4.5s  |  **Started:** 02:34:47 (t+70.1s)
- **Subagent:** KEEP in 227 → 256 chars (4.4s)
  - **Excess molar volume** resolves to **GLOBprop_28** ("Excess molar volume, m3/mol", group: VolumetricProp) with an exact match (score 100).

| Property | ID | Units | Group |
|---|---|---|---|
| Exces

<details><summary>Result</summary>

```
**Excess molar volume** resolves to **GLOBprop_28** ("Excess molar volume, m3/mol", group: VolumetricProp) with an exact match (score 100).

| Property | ID | Units | Group |
|---|---|---|---|
| Excess molar volume | GLOBprop_28 | m3/mol | VolumetricProp |
```
</details>

---

### Step 6 [main - A_2 - L1_1 · c8]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_2"
  ],
  "property": "GLOBprop_28",
  "system_type": "binary",
  "temperature_range": [
    295.0,
    302.0
  ],
  "limit": 50,
  "purpose": "Find excess molar volume data for water+ethanol binary at 298.15 K",
  "tasks": "Search for blocks with GLOBprop_28 (excess molar volume) for GLOBcomp_1 (water) + GLOBcomp_2 (ethanol) binary system near 298.15 K"
}
```
</details>

- **Result:** 1,076 chars  |  **Time:** 10.2s  |  **Started:** 02:35:03 (t+85.8s)
- **Subagent:** DISCARD in 39 → 1,076 chars (9.8s)
  - 1. **Explanation:** The search returned zero results for excess molar volume (GLOBprop_28) of water (GLOBcomp_1) + ethanol (GLOBcomp_2) binary system in the 295–302 K range. This could mean the proper

<details><summary>Result</summary>

```
**⚠ Tool `search_blocks` result discarded by subagent.**

1. **Explanation:** The search returned zero results for excess molar volume (GLOBprop_28) of water (GLOBcomp_1) + ethanol (GLOBcomp_2) binary system in the 295–302 K range. This could mean the property ID or compound IDs don't match any indexed blocks, or the data simply isn't present under these exact global IDs.

2. **Refinement suggestions:**
   - **Broaden the temperature range** (e.g., 290–310 K) in case data is indexed at slightly different temperatures.
   - **Drop the property filter** and search only by the two compounds + binary system type to see what properties *are* available for this pair — this will confirm whether any data exists at all for water+ethanol.
   - **Try `system_scope: "all"`** instead of `"declared"` in case the binary system is inferred rather than explicitly declared.
   - **Verify the global IDs**: confirm that `GLOBcomp_1`/`GLOBcomp_2` indeed map to water/ethanol and that `GLOBprop_28` is excess molar volume by using a lookup tool (e.g., `get_global_ids` or equivalent).
```
</details>

---

### Step 7 [main - A_2 - L1_1 · c10]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_2"
  ],
  "system_type": "binary",
  "limit": 50,
  "purpose": "Find any data blocks for water+ethanol binary system",
  "tasks": "List all available properties for water+ethanol binary to identify excess molar volume blocks"
}
```
</details>

- **Result:** 1,412 chars  |  **Time:** 15.9s  |  **Started:** 02:35:19 (t+102.2s)
- **Subagent:** KEEP in 30,867 → 1,250 chars (14.0s)
  - **No excess molar volume blocks found** among the 50 water+ethanol binary blocks returned. The available properties are mass density, activity coefficient, vapor/sublimation pressure, excess molar ent

<details><summary>Result</summary>

```
**No excess molar volume blocks found** among the 50 water+ethanol binary blocks returned. The available properties are mass density, activity coefficient, vapor/sublimation pressure, excess molar enthalpy, boiling temperature, mole fraction, viscosity, relative permittivity, speed of sound, and azeotropic properties.

### Properties available for water+ethanol binary system

| Property | # Blocks | Example DOIs / Block IDs |
|---|---|---|
| Mass density (kg/m³) | 12 | `10.1016/j.fluid.2004.11.019 [GLOBlit_220]/PROPblock_2`, `10.1016/j.jct.2004.07.019 [GLOBlit_2432]/PROPblock_2`, `10.1016/j.fluid.2014.05.032 [GLOBlit_1483]/PROPblock_1`, etc. |
| Excess molar enthalpy (kJ/mol) | 5 | `10.1016/j.fluid.2007.06.007 [GLOBlit_528]/PROPblock_1`, `/PROPblock_2`, `10.1016/j.fluid.2014.05.031 [GLOBlit_1482]/PROPblock_4`, `10.1016/j.jct.2005.06.018 [GLOBlit_2574]/PROPblock_4`, `10.1016/j.jct.2014.05.020 [GLOBlit_4181]/PROPblock_1` |
| Boiling temperature (K) | 9 | various |
| Vapor/sublimation pressure (kPa) | 5 | various |
| Mole fraction (VLE) | 8 | various |
| Activity coefficient | 4 | `10.1016/j.fluid.2005.08.018 [GLOBlit_299]/PROPblock_4,5,6`, `10.1016/j.fluid.2016.08.030 [GLOBlit_1971]/PROPblock_1` |
| Viscosity (Pa·s) | 4 | various |
| Speed of sound (m/s) | 1 | `10.1016/j.jct.2015.06.024 [GLOBlit_4415]/PROPblock_8` |
| Relative permittivity | 1 | `10.1016/j.jct.2012.08.009 [GLOBlit_3697]/PROP
```
</details>

---

### Step 8 [main - A_2 - L1_1 · c12]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_2"
  ],
  "property": "GLOBprop_28",
  "system_type": "binary",
  "system_scope": "either",
  "limit": 20,
  "purpose": "Find excess molar volume for water+ethanol including subsystem scope",
  "tasks": "Search with broader scope for VE data"
}
```
</details>

- **Result:** 725 chars  |  **Time:** 16.9s  |  **Started:** 02:35:46 (t+129.3s)
- **Subagent:** DISCARD in 39 → 725 chars (7.8s)
  - 1. **Explanation:** The search returned zero results for excess molar volume (GLOBprop_28) with water (GLOBcomp_1) + ethanol (GLOBcomp_2) even with `system_scope: "either"`, indicating no matching dat

<details><summary>Result</summary>

```
**⚠ Tool `search_blocks` result discarded by subagent.**

1. **Explanation:** The search returned zero results for excess molar volume (GLOBprop_28) with water (GLOBcomp_1) + ethanol (GLOBcomp_2) even with `system_scope: "either"`, indicating no matching data blocks exist in the database for this property–compound combination.

2. **Refinement suggestion:** Try alternative approaches: (a) search for GLOBprop_28 without specifying compounds to see if any excess molar volume data exists at all, (b) search for these two compounds without a property filter to discover what properties are actually available, or (c) verify that GLOBprop_28 is the correct global ID for excess molar volume by checking the property registry.
```
</details>

---

## Nested tool calls — L1_2 (L1-query)

**Nest:** main - A_2 - L1_2
**Parent:** `query_thermoml_parallel` — Step 4 [main - A_2 · c17] relays this worker's result
**Started:** 02:34:20  |  **Ended:** 02:38:58  |  **Tool calls:** 8

---

### Step 2 [main - A_2 - L1_2 · c4]: `resolve_compound_ids`

<details><summary>Arguments</summary>

```json
{
  "queries": [
    "water 7732-18-5",
    "ethanol 64-17-5"
  ],
  "min_score": 70,
  "limit": 5,
  "purpose": "Resolve water and ethanol to global compound IDs",
  "tasks": "Find GLOBcomp IDs for water and ethanol"
}
```
</details>

- **Result:** 307 chars  |  **Time:** 6.2s  |  **Started:** 02:34:29 (t+52.2s)
- **Subagent:** KEEP in 351 → 307 chars (5.2s)
  - Both water and ethanol were successfully resolved to global compound IDs.

| Name | ID | Formula | SMILES |
|---|---|---|---|
| water | GLOBcomp_1 | H2O | O |
| ethanol | GLOBcomp_2 | C2H6O | CCO |

(

<details><summary>Result</summary>

```
Both water and ethanol were successfully resolved to global compound IDs.

| Name | ID | Formula | SMILES |
|---|---|---|---|
| water | GLOBcomp_1 | H2O | O |
| ethanol | GLOBcomp_2 | C2H6O | CCO |

(GLOBcomp_5494 "ethanol-1-d" is a deuterated variant and can be ignored for standard water–ethanol queries.)
```
</details>

---

### Step 4 [main - A_2 - L1_2 · c7]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_2"
  ],
  "property": "GLOBprop_1",
  "system_type": "binary",
  "temperature_range": [
    295.0,
    301.0
  ],
  "limit": 50,
  "purpose": "Find density data for binary water+ethanol at 298.15 K",
  "tasks": "Search for blocks with mass density for binary water+ethanol system near 298.15 K"
}
```
</details>

- **Result:** 303 chars  |  **Time:** 17.0s  |  **Started:** 02:34:47 (t+70.0s)
- **Subagent:** KEEP in 14,080 → 303 chars (16.0s)
  - **Summary:** 22 blocks found for binary water+ethanol mass density near 298.15 K. Several provide excellent isothermal data at exactly 298.15 K with broad composition coverage; others span a narrow T 

<details><summary>Result</summary>

```
**Summary:** 22 blocks found for binary water+ethanol mass density near 298.15 K. Several provide excellent isothermal data at exactly 298.15 K with broad composition coverage; others span a narrow T range that includes 298.15 K.

**Top candidates (sorted by relevance for 298.15 K isothermal density vs
```
</details>

---

### Step 5 [main - A_2 - L1_2 · c9]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_2"
  ],
  "property": "GLOBprop_1",
  "system_type": "binary",
  "temperature_range": [
    296.0,
    300.0
  ],
  "limit": 30,
  "purpose": "Find density blocks for water+ethanol binary at 298.15 K",
  "tasks": "Return DOIs, block numbers, compound IDs, data point counts for binary water+ethanol density near 298.15 K"
}
```
</details>

- **Result:** 677 chars  |  **Time:** 16.3s  |  **Started:** 02:35:13 (t+96.3s)
- **Subagent:** KEEP in 14,080 → 659 chars (15.6s)
  - **Summary:** 22 binary water+ethanol density blocks found near 298.15 K, all scoring 100. All use GLOBcomp_1 + GLOBcomp_2 for GLOBprop_1 (Mass density, kg/m³), liquid phase.

| # | DOI | Block | Pts |

<details><summary>Result</summary>

```
**Summary:** 22 binary water+ethanol density blocks found near 298.15 K, all scoring 100. All use GLOBcomp_1 + GLOBcomp_2 for GLOBprop_1 (Mass density, kg/m³), liquid phase.

| # | DOI | Block | Pts | T(K) range | Composition variable | Comp. range | ρ(kg/m³) range | GLOBlit |
|---|-----|-------|-----|-----------|----------------------|-------------|----------------|---------|
| 1 | 10.1016/j.fluid.2004.11.019 | PROPblock_2 | 810 | 298.15 | x(ethanol) | 0.003–0.7996 | 810.9–995.3 | GLOBlit_220 |
| 2 | 10.1016/j.fluid.2014.05.032 | PROPblock_1 | 140 | 292.95–448.15 | x(ethanol) | 0.0163–0.073 | 882.3–1006.1 | GLOBlit_1483 |
| 3 | 10.1016/j.jct.2004.07. [lit_num_id=null]
```
</details>

---

### Step 6 [main - A_2 - L1_2 · c11]: `search_system_registry`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_2"
  ],
  "property": "GLOBprop_1",
  "system_type": "binary",
  "system_scope": "declared",
  "temperature_range": [
    295.0,
    301.0
  ],
  "limit": 50,
  "purpose": "List all binary water+ethanol density blocks near 298.15 K",
  "tasks": "Return DOIs, block numbers, data point counts for all matching blocks"
}
```
</details>

- **Result:** 1,355 chars  |  **Time:** 10.6s  |  **Started:** 02:35:39 (t+121.6s)
- **Subagent:** KEEP in 2,557 → 1,095 chars (10.2s)
  - **Summary:** 17 binary water+ethanol density blocks were found in the temperature window 295–301 K. Data point counts range from 2 to 810, spanning 17 distinct DOI/block combinations.

| # | DOI | Blo

<details><summary>Result</summary>

```
**Summary:** 17 binary water+ethanol density blocks were found in the temperature window 295–301 K. Data point counts range from 2 to 810, spanning 17 distinct DOI/block combinations.

| # | DOI | Block | Points |
|---|-----|-------|--------|
| 1 | 10.1016/j.fluid.2004.11.019 [GLOBlit_220] | PROPblock_2 | 810 |
| 2 | 10.1016/j.fluid.2014.05.032 [GLOBlit_1483] | PROPblock_1 | 140 |
| 3 | 10.1016/j.jct.2004.07.019 [GLOBlit_2432] | PROPblock_2 | 565 |
| 4 | 10.1016/j.jct.2007.05.004 [GLOBlit_2825] | PROPblock_12 | 37 |
| 5 | 10.1016/j.jct.2011.10.009 [GLOBlit_3475] | PROPblock_3 | 70 |
| 6 | 10.1016/j.jct.2015.06.024 [GLOBlit_4415] | PROPblock_7 | 40 |
| 7 | 10.1016/j.jct.2018.02.022 [GLOBlit_5201] | PROPblock_19 | 244 |
| 8 | 10.1021/acs.jced.6b01058 [GLOBlit_7085] | PROPblock_7 | 12 |
| 9 | 10.1021/acs.jced.7b00299 [GLOBlit_7178] | PROPblock_10 | 2 |
| 10 | 10.1021/je020173z [GLOBlit_8050] | PROPblock_5 | 24 |
| 11 | 10.1021/je060335h [GLOBlit_9006] | PROPblock_1 | 164 |
| 12 | 10.1021/je4003515 [GLOBlit_10159] | PROPblock_7 | 23 |
| 13 | 10.1021/je600565m [GLOBlit_10699] | PROPblock_6 | 18 |
| 14 | 10.1021/je700300y [GLOBlit_10866] | PROPblock_7 | 84 |
| 15 | 10.1021/je800150h [GLOBlit_11136] | PROPblock_9 | 108 |
| 16 | 10.1021/je900064e [GLOBlit_11504] | PROPblock_6 | 10 |
| 17 | 10.1021/je900743e [GLOBlit_11792] | PROPblock_3 | 15
```
</details>

---

### Step 8 [main - A_2 - L1_2 · c13]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "GLOBlit_220::PROPblock_2",
  "where": "Temperature BETWEEN 297 AND 300",
  "purpose": "Inspect top density block for water+ethanol at 298.15 K",
  "tasks": "Get composition range, density range, temperature, and point count at 298.15 K"
}
```
</details>

- **Result:** 369 chars  |  **Time:** 0.2s  |  **Started:** 02:36:20 (t+163.3s)

<details><summary>Result</summary>

```
**inspect_block_table error** — where filter error: unknown column alias 'Temperature'

| alias | n_finite | min | max |
|---|---|---|---|
| temperature_k | 810 | 298.15 | 348.15 |
| pressure_kpa | 810 | 100 | 40000 |
| mole_fraction_ethanol | 810 | 0.003 | 1 |
| mass_density_kg_m3 | 810 | 739.4 | 1012.7 |

Use these aliases in `where` / `nearest` with plain numbers.
```
</details>

---

### Step 9 [main - A_2 - L1_2 · c14]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "GLOBlit_220::PROPblock_2",
  "where": "temperature_k = 298.15",
  "purpose": "Ground density data for water+ethanol at 298.15 K",
  "tasks": "Get composition range and density range at exactly 298.15 K"
}
```
</details>

- **Result:** 2,089 chars  |  **Time:** 0.1s  |  **Started:** 02:36:26 (t+169.3s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1016/j.fluid.2004.11.019 [GLOBlit_220] :: PROPblock_2 (binary: ethanol + water)
filter: where temperature_k = 298.15

| BLKpoint_id | temperature_k | pressure_kpa | mole_fraction_<ethanol> | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 100 | 0.003 | 995.3 |
| BLKpoint_38 | 298.15 | 100 | 0.2502 | 918.5 |
| BLKpoint_43 | 298.15 | 100 | 0.4501 | 868.8 |
| BLKpoint_48 | 298.15 | 100 | 0.6967 | 825.2 |
| BLKpoint_54 | 298.15 | 100 | 1 | 785.7 |
| BLKpoint_55 | 298.15 | 10000 | 0.003 | 999.8 |
| BLKpoint_92 | 298.15 | 10000 | 0.2502 | 923.3 |
| BLKpoint_97 | 298.15 | 10000 | 0.4501 | 874.7 |
| BLKpoint_102 | 298.15 | 10000 | 0.6967 | 832.3 |
| BLKpoint_108 | 298.15 | 10000 | 1 | 794 |
| BLKpoint_109 | 298.15 | 20000 | 0.003 | 1004.2 |
| BLKpoint_146 | 298.15 | 20000 | 0.2502 | 928 |
| BLKpoint_151 | 298.15 | 20000 | 0.4501 | 880.4 |
| BLKpoint_156 | 298.15 | 20000 | 0.6967 | 839 |
| BLKpoint_162 | 298.15 | 20000 | 1 | 801.9 |
| BLKpoint_163 | 298.15 | 30000 | 0.003 | 1008.5 |
| BLKpoint_199 | 298.15 | 30000 | 0.2269 | 938.7 |
| BLKpoint_205 | 298.15 | 30000 | 0.4501 | 885.7 |
| BLKpoint_210 | 298.15 | 30000 | 0.6967 | 845.1 |
| BLKpoint_216 | 298.15 | 30000 | 1 | 808.9 |
| BLKpoint_217 | 298.15 | 40000 | 0.003 | 1012.7 |
| BLKpoint_253 | 298.15 | 40000 | 0.2269 | 942.9 |
| BLKpoint_259 | 298.15 | 40000 | 0.4501 | 890.8 |
| BLKpoint_264 | 298.15 | 40000 | 0.6967 | 851 |
| BLKpoint_270 | 298.15 | 40000 | 1 | 815.7 |

mode: RDP — 25 of 270 matched rows shown (shape-preserving; block has 810). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=270): temperature_k 298.15–298.15 (n=270); pressure_kpa 100–40000 (n=270); mole_fraction_ethanol 0.003–1 (n=270); mass_density_kg_m3 785.7–1012.7 (n=270)
stats (full block, n=810): temperature_k 298.15–348.15 (n=810); pressure_kpa 100–40000 (n=810); mole_fraction_ethanol 0.003–1 (n=810); mass_density_kg_m3 739.4–1012.7 (n=810)
inspection_id: INSP_689860323003
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

### Step 10 [main - A_2 - L1_2 · c15]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "GLOBlit_2432::PROPblock_2",
  "purpose": "Ground data values for GLOBlit_2432::PROPblock_2",
  "tasks": "Get stats and sample rows at 298.15 K"
}
```
</details>

- **Result:** 4,539 chars  |  **Time:** 0.2s  |  **Started:** 02:36:34 (t+176.6s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1016/j.jct.2004.07.019 [GLOBlit_2432] :: PROPblock_2 (binary: ethanol + water)
filter: none (whole block)

| BLKpoint_id | temperature_k | pressure_kpa | molality_mol_kg_<ethanol> | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 410 | 0.09647 | -0.8568 |
| BLKpoint_6 | 298.15 | 410 | 0.94275 | -7.4996 |
| BLKpoint_12 | 298.15 | 14450 | 0.94273 | -7.71 |
| BLKpoint_19 | 298.15 | 14450 | 0.09647 | -0.874 |
| BLKpoint_31 | 298.15 | 14450 | 0.09647 | -0.874 |
| BLKpoint_42 | 298.18 | 29930 | 0.94271 | -7.9243 |
| BLKpoint_48 | 298.18 | 29930 | 0.94271 | -7.9243 |
| BLKpoint_49 | 298.18 | 29930 | 0.09646 | -0.9011 |
| BLKpoint_58 | 318.14 | 390 | 0.55206 | -4.6779 |
| BLKpoint_62 | 318.14 | 15370 | 0.55207 | -4.7543 |
| BLKpoint_63 | 318.14 | 390 | 0.08808 | -0.7809 |
| BLKpoint_71 | 318.14 | 390 | 0.08808 | -0.7809 |
| BLKpoint_74 | 318.14 | 15370 | 0.08808 | -0.7943 |
| BLKpoint_80 | 318.15 | 29980 | 0.55208 | -4.8174 |
| BLKpoint_85 | 318.15 | 29980 | 0.08809 | -0.8061 |
| BLKpoint_94 | 338.15 | 510 | 0.9427 | -8.0628 |
| BLKpoint_100 | 338.15 | 14860 | 0.94264 | -8.1024 |
| BLKpoint_113 | 338.15 | 510 | 0.09646 | -0.8794 |
| BLKpoint_119 | 338.15 | 14860 | 0.09646 | -0.8864 |
| BLKpoint_128 | 338.16 | 30230 | 0.55204 | -4.909 |
| BLKpoint_129 | 338.16 | 30230 | 0.10088 | -0.9335 |
| BLKpoint_138 | 373.17 | 2090 | 0.94262 | -8.8555 |
| BLKpoint_144 | 373.17 | 14860 | 0.94259 | -8.7729 |
| BLKpoint_150 | 373.17 | 30110 | 0.94256 | -8.7019 |
| BLKpoint_168 | 373.17 | 30110 | 0.94256 | -8.7019 |
| BLKpoint_169 | 373.17 | 2090 | 0.09645 | -0.9474 |
| BLKpoint_175 | 373.17 | 14860 | 0.09645 | -0.9386 |
| BLKpoint_181 | 373.17 | 30110 | 0.09645 | -0.9356 |
| BLKpoint_192 | 408.15 | 2040 | 0.94252 | -9.7809 |
| BLKpoint_198 | 408.15 | 14990 | 0.94247 | -9.585 |
| BLKpoint_204 | 408.15 | 29940 | 0.99979 | -9.9551 |
| BLKpoint_223 | 408.15 | 2040 | 0.09572 | -1.0313 |
| BLKpoint_229 | 408.15 | 14990 | 0.09572 | -1.0118 |
| BLKpoint_235 | 408.15 | 29940 | 0.09571 | -0.992 |
| BLKpoint_245 | 443.16 | 14970 | 0.99975 | -11.1138 |
| BLKpoint_251 | 443.16 | 30300 | 0.99973 | -10.7304 |
| BLKpoint_264 | 443.16 | 14970 | 0.0957 | -1.1033 |
| BLKpoint_270 | 443.16 | 30300 | 0.0957 | -1.0627 |
| BLKpoint_288 | 443.17 | 2110 | 0.09571 | -1.1352 |
| BLKpoint_292 | 443.17 | 2110 | 0.99977 | -11.4775 |
| BLKpoint_298 | 473.16 | 2780 | 0.9997 | -12.5432 |
| BLKpoint_304 | 473.16 | 14990 | 0.99967 | -12.0186 |
| BLKpoint_310 | 473.16 | 30050 | 0.99964 | -11.4895 |
| BLKpoint_311 | 473.16 | 2780 | 0.0957 | -1.2406 |
| BLKpoint_329 | 473.16 | 2780 | 0.0957 | -1.2406 |
| BLKpoint_335 | 473.16 | 14990 | 0.10419 | -1.2973 |
| BLKpoint_341 | 473.16 | 30050 | 0.10418 | -1.2416 |
| BLKpoint_352 | 498.15 | 3810 | 0.99959 | -13.5611 |
| BLKpoint_358 | 498.15 | 30190 | 0.99954 | -12.1289 |
| BLKpoint_371 | 498.15 | 3810 | 0.10418 | -1.4613 |
| BLKpoint_383 | 498.15 | 30190 | 0.10418 | -1.3031 |
| BLKpoint_394 | 498.16 | 15030 | 1.04067 | -13.3718 |
| BLKpoint_401 | 498.16 | 15030 | 0.10418 | -1.3877 |
| BLKpoint_412 | 523.14 | 5880 | 1.04065 | -15.3473 |
| BLKpoint_418 | 523.14 | 15560 | 1.04063 | -14.4002 |
| BLKpoint_424 | 523.14 | 30170 | 1.04062 | -13.3657 |
| BLKpoint_443 | 523.14 | 5880 | 0.10417 | -1.5874 |
| BLKpoint_449 | 523.14 | 15560 | 0.10417 | -1.4921 |
| BLKpoint_455 | 523.14 | 30170 | 0.10416 | -1.3907 |
| BLKpoint_466 | 548.16 | 8000 | 1.04058 | -17.0046 |
| BLKpoint_472 | 548.16 | 15960 | 1.04054 | -15.7466 |
| BLKpoint_478 | 548.16 | 30120 | 1.04051 | -14.2262 |
| BLKpoint_496 | 548.16 | 30120 | 1.04051 | -14.2262 |
| BLKpoint_497 | 548.16 | 8000 | 0.0881 | -1.4865 |
| BLKpoint_503 | 548.16 | 15960 | 0.0881 | -1.3838 |
| BLKpoint_509 | 548.16 | 30120 | 0.0881 | -1.2547 |
| BLKpoint_519 | 573.14 | 30090 | 1.04039 | -15.3285 |
| BLKpoint_525 | 573.14 | 30090 | 0.08809 | -1.3474 |
| BLKpoint_535 | 573.15 | 10150 | 1.04048 | -19.634 |
| BLKpoint_554 | 573.15 | 10150 | 0.0881 | -1.7035 |
| BLKpoint_560 | 573.15 | 18040 | 0.08809 | -1.5198 |
| BLKpoint_565 | 573.15 | 18040 | 1.04045 | -17.3814 |

mode: RDP — 72 of 565 matched rows shown (shape-preserving; block has 565). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=565): temperature_k 298.15–573.15 (n=565); pressure_kpa 390–30300 (n=565); molality_mol_kg_ethanol 0.08808–1.04067 (n=565); mass_density_kg_m3 -19.634–-0.7809 (n=565)
inspection_id: INSP_b3500349e479
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

### Step 11 [main - A_2 - L1_2 · c16]: `inspect_block_table`

<details><summary>Arguments</summary>

```json
{
  "block_number": "GLOBlit_5201::PROPblock_19",
  "purpose": "Inspect block for water+ethanol density data near 298.15 K",
  "tasks": "Check composition range, temperature, and density values"
}
```
</details>

- **Result:** 1,805 chars  |  **Time:** 0.2s  |  **Started:** 02:36:46 (t+189.3s)

<details><summary>Result</summary>

```
**Data inspection** — 10.1016/j.jct.2018.02.022 [GLOBlit_5201] :: PROPblock_19 (binary: ethanol + water)
filter: none (whole block)
block constraints: pressure_kpa = 92.3

| BLKpoint_id | temperature_k | mole_fraction_<ethanol> | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 293.15 | 0.0024 | 92.3 | 997.039 |
| BLKpoint_23 | 293.15 | 0.7006 | 92.3 | 829.434 |
| BLKpoint_59 | 298.15 | 0.7006 | 92.3 | 825.07 |
| BLKpoint_95 | 303.15 | 0.7006 | 92.3 | 820.66 |
| BLKpoint_131 | 308.15 | 0.7006 | 92.3 | 816.2 |
| BLKpoint_145 | 293.15 | 0 | 92.3 | 998.429 |
| BLKpoint_146 | 298.15 | 0 | 92.3 | 997.267 |
| BLKpoint_147 | 303.15 | 0 | 92.3 | 995.867 |
| BLKpoint_148 | 308.15 | 0 | 92.3 | 994.252 |
| BLKpoint_149 | 293.15 | 1 | 92.3 | 789.547 |
| BLKpoint_150 | 298.15 | 1 | 92.3 | 785.26 |
| BLKpoint_151 | 303.15 | 1 | 92.3 | 780.941 |
| BLKpoint_152 | 308.15 | 1 | 92.3 | 776.592 |
| BLKpoint_160 | 293.15 | 0.1984 | 92.3 | 935.19 |
| BLKpoint_165 | 293.15 | 0.4495 | 92.3 | 873.57 |
| BLKpoint_183 | 298.15 | 0.1984 | 92.3 | 931.84 |
| BLKpoint_188 | 298.15 | 0.4495 | 92.3 | 869.34 |
| BLKpoint_206 | 303.15 | 0.1984 | 92.3 | 928.77 |
| BLKpoint_211 | 303.15 | 0.4495 | 92.3 | 865.03 |
| BLKpoint_229 | 308.15 | 0.1984 | 92.3 | 925.04 |
| BLKpoint_234 | 308.15 | 0.4495 | 92.3 | 860.66 |
| BLKpoint_244 | 308.15 | 0.929 | 92.3 | 785.46 |

mode: RDP — 22 of 244 matched rows shown (shape-preserving; block has 244). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=244): temperature_k 293.15–308.15 (n=244); mole_fraction_ethanol 0–1 (n=244); pressure_kpa 92.3–92.3 (n=244); mass_density_kg_m3 776.592–998.429 (n=244)
inspection_id: INSP_b49f3d6ec58f
Data points may be quoted ONLY verbatim from the table above or the stats lines.
```
</details>

---

## Compaction Summary (12 events)

| Iter | Trigger | Before | After | Reduction | Outcome |
|------|---------|--------|-------|-----------|---------|
| 4 | chars=98928>80000 | 98,928 | 98,928 | −0% | skipped_by_agent |
| 7 | chars=101375>80000 | 101,375 | 101,375 | −0% | skipped_by_agent |
| 9 | chars=102316>80000 | 102,316 | 102,316 | −0% | skipped_by_agent |
| 13 | chars=104215>80000 | 104,215 | 104,215 | −0% | skipped_by_agent |
| 16 | chars=105555>80000 | 105,555 | 105,555 | −0% | skipped_by_agent |
| 17 | chars=106856>80000 | 106,856 | 106,856 | −0% | skipped_by_agent |
| 18 | chars=107460>80000 | 107,460 | 107,460 | −0% | skipped_by_agent |
| 19 | chars=108829>80000 | 108,829 | 108,829 | −0% | skipped_by_agent |
| 20 | chars=109350>80000 | 109,350 | 109,350 | −0% | skipped_by_agent |
| 21 | chars=112704>80000 | 112,704 | 112,704 | −0% | skipped_by_agent |
| 23 | chars=128578>80000 | 128,578 | 128,578 | −0% | skipped_by_agent |
| 25 | chars=141008>80000 | 141,008 | 141,008 | −0% | skipped_by_agent |

## Tool Compaction Pipeline (22 calls)

| # | Tool | Pipeline | Native | Hardcoded | Agentic | Verdict | Native→Final | Section |
|--:|------|----------|-------:|----------:|--------:|---------|-------------:|---------|
| 1 | `resolve_compound_ids` | query | 846 | 351 | 307 | KEEP | −64% | L1_2 |
| 2 | `resolve_compound_ids` | query | 846 | 351 | 270 | KEEP | −68% | L1_1 |
| 3 | `resolve_property_ids` | query | 261 | 227 | 256 | KEEP | −2% | L1_1 |
| 4 | `search_blocks` | query | 136,442 | 14,080 | 303 | KEEP | −100% | L1_2 |
| 5 | `search_blocks` | query | 221 | 39 | 1,076 | DISCARD | −-387% | L1_1 |
| 6 | `search_blocks` | query | 136,442 | 14,080 | 659 | KEEP | −100% | L1_2 |
| 7 | `search_blocks` | query | 297,132 | 30,867 | 1,250 | KEEP | −100% | L1_1 |
| 8 | `search_system_registry` | query | 73,362 | 2,557 | 1,095 | KEEP | −99% | L1_2 |
| 9 | `search_blocks` | query | 182 | 39 | 725 | DISCARD | −-298% | L1_1 |
| 10 | `inspect_block_table` | query | 1,106 | 369 | 369 | SKIP | −67% | L1_2 |
| 11 | `inspect_block_table` | query | 7,334 | 2,075 | 2,075 | SKIP | −72% | L1_2 |
| 12 | `inspect_block_table` | query | 17,399 | 4,524 | 4,524 | SKIP | −74% | L1_2 |
| 13 | `inspect_block_table` | query | 6,622 | 1,790 | 1,790 | SKIP | −73% | L1_2 |
| 14 | `inspect_block` | analysis | 2,820 | 1,359 | 1,359 | SKIP | −52% | — |
| 15 | `fit_block_derived` | analysis | 263 | 208 | 208 | SKIP | −21% | — |
| 16 | `fit_block_derived` | analysis | 288 | 230 | 230 | SKIP | −20% | — |
| 17 | `fit_block_derived` | analysis | 3,598 | 954 | 954 | SKIP | −73% | — |
| 18 | `predict_from_rk` | analysis | 7,522 | 205 | 205 | SKIP | −97% | — |
| 19 | `fit_block_derived` | analysis | 3,648 | 961 | 961 | SKIP | −74% | — |
| 20 | `predict_from_rk` | analysis | 7,498 | 206 | 206 | SKIP | −97% | — |
| 21 | `inspect_block` | analysis | 2,820 | 1,359 | 1,359 | SKIP | −52% | — |
| 22 | `inspect_block` | analysis | 2,820 | 1,359 | 1,359 | SKIP | −52% | — |

## Subagent Summary (9 events)

| Tool | Verdict | Input Chars | Output Chars | Time | Section |
|------|---------|-------------|-------------|------|---------|
| resolve_compound_ids | KEEP | 351 | 307 | 5.2s | L1_2 |
| resolve_compound_ids | KEEP | 351 | 270 | 5.0s | L1_1 |
| resolve_property_ids | KEEP | 227 | 256 | 4.4s | L1_1 |
| search_blocks | KEEP | 14,080 | 303 | 16.0s | L1_2 |
| search_blocks | DISCARD | 39 | 1,076 | 9.8s | L1_1 |
| search_blocks | KEEP | 14,080 | 659 | 15.6s | L1_2 |
| search_blocks | KEEP | 30,867 | 1,250 | 14.0s | L1_1 |
| search_system_registry | KEEP | 2,557 | 1,095 | 10.2s | L1_2 |
| search_blocks | DISCARD | 39 | 725 | 7.8s | L1_1 |

## Errors (4)

- **Step 1** `query_thermoml_parallel` (exception): {
  "error": "queries[0].id_catalog[0] must contain exactly ['global_id', 'name', 'registry_id', 'type']; received ['cas', 'id', 'name', 'type']",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "qu
- **Step 2** `query_thermoml_parallel` (exception): {
  "error": "queries[0].id_catalog[0].type is invalid: 'property'; valid types: ['blocktype', 'comp', 'constr', 'lit', 'meas', 'phase', 'prop', 'rxntype', 'solvent', 'var']",
  "error_code": "TOOL_EX
- **Step 3** `query_thermoml_parallel` (exception): {
  "error": "comp_num_id must match GLOBcomp_<positive integer>, got ''",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml_parallel"
}
- **Step 13** `fit_block_derived` (exception): {
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: fit_block_derived.x_vars_constrained received '{\"Temperature, K\": {\"value\": 298.15, \"tol\": 0.5}}' (str); expected dict | None; tool arguments are

---

**Total:** 36 tool calls  |  Tool time: 386.7s  |  Wall: 821.4s  |  **Status:** OK
