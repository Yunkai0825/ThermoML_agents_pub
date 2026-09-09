# Tool History — query-agent

**Nest:** Q
**Session:** c5ed4953
**Detailed log:** run_history_detailed.md — Argo events + verbatim agent outputs (join: session id; step tag `cN` ↔ event-row `cN`)
**Prompt:** For aqueous propan-2-ol, which study provides the most complete experimental characterization? What properties were measured, which methods were used, and what purities were reported for the compounds?
**Started:** 2026-09-05 05:35:29  |  **Elapsed:** 993.9s  |  **Tool calls:** 26  |  **Nested sections:** 3

---

### Step 1 [Q · c8]: `L1_query` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "purpose": "Find studies of aqueous propan-2-ol (isopropanol + water) binary mixtures and identify which study provides the most complete experimental characterization",
  "instruction": "Search for binary mixture systems containing propan-2-ol (isopropanol, 2-propanol, CAS 67-63-0) and water (CAS 7732-18-5). List all studies (DOIs) found, the properties measured in each, and rank by number of distinct properties measured. Return DOIs, literature IDs, property names, and property IDs for the top studies.",
  "id_catalog": "",
  "context": "User wants the most comprehensive study of aqueous isopropanol. Need to find all relevant literature and compare breadth of property coverage."
}
```
</details>

- **Result:** 415 chars  |  **Time:** 0.0s  |  **Started:** 05:40:10 (t+280.2s)
- **Error:** `{
  "error": "query-L1 core-ID refinement exhausted 2 cycles: construct_core_blocks_found: core_blocks_found[1] checksum mismatch for (GLOBlit_1423, PROPblock_2): system_type expected 'unary', received 'binary'; comp_num_ids expected ['GLOBcomp_6'], received ['GLOBcomp_6', 'GLOBcomp_1']; prop_num_ids expected ['GLOBprop_7'], received ['GLOBprop_2']",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "L1_query"
}`
- **Nested:** ↳ 7 tool calls in section 'L1_1' below

---

### Step 2 [Q · c20]: `L1_query` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "purpose": "Find the most comprehensive experimental study for the binary system water + propan-2-ol (isopropanol, 2-propanol) in ThermoML",
  "instruction": "Search for binary mixture studies containing propan-2-ol (also known as isopropanol, 2-propanol, IPA) and water. Identify which literature sources (DOIs) report the largest number of different thermodynamic/transport properties for this binary system. For each literature source found, list: (1) the properties measured, (2) the measurement methods used, (3) the purities reported for each compound, and (4) the number of data blocks. Rank by breadth of characterization (number of distinct properties). Return the top results with full details.",
  "id_catalog": "",
  "context": "User wants the most complete experimental characterization of aqueous propan-2-ol. We need to find which study covers the most properties."
}
```
</details>

- **Result:** 278 chars  |  **Time:** 0.0s  |  **Started:** 05:46:49 (t+679.1s)
- **Error:** `{
  "error": "query-L1 core-ID refinement exhausted 2 cycles: construct_core_blocks_found: core_blocks_found[9] checksum mismatch for (GLOBlit_2096, PROPblock_7): prop_num_ids expected ['GLOBprop_45'], received []",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "L1_query"
}`
- **Nested:** ↳ 11 tool calls in section 'L1_2' below

---

### Step 3 [Q · c26]: `L1_query`

<details><summary>Arguments</summary>

```json
{
  "purpose": "Find all literature entries (studies) in ThermoML that report experimental data for the binary system water + propan-2-ol (2-propanol, isopropanol, CAS 67-63-0). List each study with its DOI, literature ID, and the properties measured.",
  "instruction": "Step 1: Resolve the component IDs for water (CAS 7732-18-5) and propan-2-ol (2-propanol, CAS 67-63-0). Step 2: Search for all property data blocks that contain BOTH components as a binary system. Step 3: For each literature source found, list: the GLOBlit_N ID, DOI, number of property blocks, and which properties (with GLOBprop_N IDs) are covered. Step 4: Rank the studies by the number of distinct properties measured, descending. Return the top 5 most comprehensive studies.",
  "id_catalog": "",
  "context": "User wants the most complete experimental characterization of aqueous propan-2-ol. We need to find which study measured the most different properties for this binary system."
}
```
</details>

- **Result:** 5,904 chars  |  **Time:** 244.3s  |  **Started:** 05:46:58 (t+689.0s)
- **Nested:** ↳ 5 tool calls in section 'L1_3' below

<details><summary>Result</summary>

```
<subagent_answer>
{
  "answer": "## Binary Water + Propan-2-ol: Literature Coverage in ThermoML\n\n**System:** water (GLOBcomp_1) + propan-2-ol (GLOBcomp_6), binary\n\nThe ThermoML database contains **71 declared binary data blocks** across **38 distinct DOIs** for this system, totaling approximately **2,893 data points**. The properties covered span VLE data (boiling temperature, equilibrium mole fraction, azeotropic temperature and composition), mass density, molar heat capacity (Cp), viscosity, surface tension, speed of sound, refractive index, excess molar enthalpy, electrical conductivity, and vapor pressure.\n\n### Top 5 Most Comprehensive Studies (by number of distinct properties)\n\n| Rank | GLOBlit ID | DOI | Blocks | Distinct Properties | Properties Measured | Total Points |\n|------|-----------|-----|--------|---------------------|---------------------|-------------|\n| 1 | GLOBlit_1423 | 10.1016/j.fluid.2014.02.006 | 4 | 4 | Boiling temperature, Mole fraction, Azeotropic temperature, Azeotropic composition | 36 |\n| 2 | GLOBlit_2096 | 10.1016/j.fluid.2017.09.010 | 3 | 3 | Boiling temperature, Mole fraction, Azeotropic composition | 37 |\n| 3 | GLOBlit_1311 | 10.1016/j.fluid.2013.08.007 | 2 | 2 | Mass density, Molar Cp | 1,248 |\n| 4 | GLOBlit_1827 | 10.1016/j.fluid.2015.11.034 | 2 | 2 | Boiling temperature, Mole fraction | 28 |\n| 5 | GLOBlit_2687 | 10.1016/j.jct.2006.04.006 | 2 | 2 | Boiling temperature, Mole fraction | 34 |\n\n### Additional Notable Studies (1 property each, but large datasets or unique properties)\n\n| GLOBlit ID | DOI | Property | Points |\n|-----------|-----|----------|--------|\n| GLOBlit_2432 | 10.1016/j.jct.2004.07.019 | Mass density | 529 |\n| GLOBlit_11130 | 10.1021/je8001305 | Mass density (compressed liquid) | 209 |\n| GLOBlit_1910 | 10.1016/j.fluid.2016.04.007 | Surface tension | 60 |\n| GLOBlit_378 | 10.1016/j.fluid.2006.03.021 | Boiling temperature | 48 |\n| GLOBlit_2892 | 10.1016/j.jct.2007.12.002 | Excess molar enthalpy | 45 |\n\n### Key Observations\n\n- **GLOBlit_1423** is the most property-diverse study, reporting four distinct VLE-related properties (boiling temperature, equilibrium mole fraction, and azeotropic temperature and composition) for the water + propan-2-ol system.\n- **GLOBlit_1311** is the most data-rich study overall, with 1,248 data points covering mass density (1,110 pts) and molar heat capacity (138 pts) across multiple temperatures and compositions.\n- The database also contains blocks with viscosity, speed of sound, refractive index, electrical conductivity, and vapor pressure data from additional DOIs among the 38 total literature sources, though detailed property assignments for all 71 blocks could not be fully enumerated within the 50-block search limit.\n- VLE-related measurements (boiling temperature, equilibrium mole fraction, azeotropic data) are the most commonly reported property type for this system, appearing in at least 8 distinct studies.",
  "core_claims": [
    "The ThermoML database contains 71 declared binary data blocks across 38 distinct DOIs for the water + propan-2-ol system, totaling approximately 2,893 data points.",
    "Properties covered span VLE data (boiling temperature, equilibrium mole fraction, azeotropic temperature and composition), mass density, molar heat capacity, viscosity, surface tension, speed of sound, refractive index, excess molar enthalpy, electrical conductivity, and vapor pressure.",
    "GLOBlit_1423 (DOI 10.1016/j.fluid.2014.02.006) is the most property-diverse study, reporting four distinct VLE-related properties: boiling temperature, equilibrium mole fraction, azeotropic temperature, and azeotropic composition.",
    "GLOBlit_1311 (DOI 10.1016/j.fluid.2013.08.007) is the most data-rich study with 1,248 data points covering mass density (1,110 pts) and molar heat capacity (138 pts).",
    "VLE-related measurements are the most commonly reported property type for this system, appearing in at least 8 distinct studies.",
    "Detailed property assignments for all 71 blocks could not be fully enumerated within the 50-block search limit."
  ],
  "status": "success",
  "summary": "The ThermoML database contains 71 declared binary data blocks across 38 distinct DOIs for the water + propan-2-ol system, totaling approximately 2,893 data points. Properties covered include boiling temperature, equilibrium mole fraction, azeotropic temperature and composition, mass density, molar heat capacity (Cp), viscosity, surface tension, speed of sound, refractive index, excess molar enthalpy, electrical conductivity, and vapor pressure. The most property-diverse study is GLOBlit_1423 (DOI 10.1016/j.fluid.2014.02.006), reporting four distinct VLE-related properties (boiling temperature, mole fraction, azeotropic temperature, azeotropic composition) across 36 data points. The most data-rich study is GLOBlit_1311 (DOI 10.1016/j.fluid.2013.08.007), with 1,248 data points covering mass density (1,110 pts) and molar Cp (138 pts). Other notable studies include GLOBlit_2096 (DOI 10.1016/j.fluid.2017.09.010, 3 properties, 37 points), GLOBlit_2432 (DOI 10.1016/j.jct.2004.07.019, mass density, 529 points), GLOBlit_11130 (DOI 10.1021/je8001305, compressed liquid mass density, 209 points), GLOBlit_1910 (DOI 10.1016/j.fluid.2016.04.007, surface tension, 60 points), and GLOBlit_2892 (DOI 10.1016/j.jct.2007.12.002, excess molar enthalpy, 45 points). VLE-related measurements are the most commonly reported property type, appearing in at least 8 distinct studies.",
  "core_id_updates": [
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_1",
      "registry_id": "water",
      "name": "water"
    },
    {
      "action": "add",
      "core_GLOB_id": "GLOBcomp_6",
      "registry_id": "propan-2-ol",
      "name": "propan-2-ol"
    }
  ],
  "core_blocks_found": [],
  "data_inspections": []
}
</subagent_answer>
```
</details>

---

## Nested tool calls — L1_1 (L1-query)

**Nest:** Q - L1_1
**Parent:** `L1_query` — Step 1 [Q · c8] relays this worker's result
**Started:** 05:35:38  |  **Ended:** 05:40:09  |  **Tool calls:** 7

---

### Step 2 [Q - L1_1 · c1]: `resolve_compound_ids`

<details><summary>Arguments</summary>

```json
{
  "queries": [
    "propan-2-ol",
    "water"
  ],
  "min_score": 50,
  "limit": 5,
  "purpose": "Resolve propan-2-ol and water to canonical global compound IDs",
  "tasks": "Find GLOBcomp IDs for isopropanol and water"
}
```
</details>

- **Result:** 190 chars  |  **Time:** 5.0s  |  **Started:** 05:35:48 (t+18.5s)
- **Subagent:** KEEP in 285 → 190 chars (4.3s)
  - Both compounds resolved with exact name matches.

| Compound | Global ID | Formula | SMILES |
|---|---|---|---|
| propan-2-ol | GLOBcomp_6 | C3H8O | CC(C)O |
| water | GLOBcomp_1 | H2O | O |

<details><summary>Result</summary>

```
Both compounds resolved with exact name matches.

| Compound | Global ID | Formula | SMILES |
|---|---|---|---|
| propan-2-ol | GLOBcomp_6 | C3H8O | CC(C)O |
| water | GLOBcomp_1 | H2O | O |
```
</details>

---

### Step 3 [Q - L1_1 · c2]: `search_system_registry`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_6",
    "GLOBcomp_1"
  ],
  "system_type": "binary",
  "system_scope": "declared",
  "limit": 100,
  "purpose": "Find all binary mixture data blocks for propan-2-ol + water systems",
  "tasks": "List all literature sources, properties measured, and block counts for ranking studies by breadth of characterization"
}
```
</details>

- **Result:** 1,348 chars  |  **Time:** 15.1s  |  **Started:** 05:36:00 (t+31.0s)
- **Subagent:** KEEP in 10,570 → 1,151 chars (13.6s)
  - **Summary:** 71 binary propan-2-ol + water property blocks found across 38 distinct DOIs, totaling ~2,890 data points. Block detail sections are empty, so **property names are not available** from thi

<details><summary>Result</summary>

```
**Summary:** 71 binary propan-2-ol + water property blocks found across 38 distinct DOIs, totaling ~2,890 data points. Block detail sections are empty, so **property names are not available** from this search — a follow-up `get_block_metadata` call per DOI is needed to identify measured properties.

**DOI-level aggregation (ranked by total points):**

| DOI | Blocks | Total Pts | Block IDs |
|-----|--------|-----------|-----------|
| 10.1016/j.fluid.2013.08.007 [GLOBlit_1311] | 2 | 1248 | PROPblock_4, PROPblock_5 |
| 10.1016/j.jct.2004.07.019 [GLOBlit_2432] | 1 | 529 | PROPblock_4 |
| 10.1021/je8001305 [GLOBlit_11130] | 1 | 209 | PROPblock_1 |
| 10.1016/j.fluid.2016.04.007 [GLOBlit_1910] | 1 | 60 | PROPblock_2 |
| 10.1021/je800158z [GLOBlit_11142] | 1 | 56 | PROPblock_4 |
| 10.1016/j.fluid.2006.03.021 [GLOBlit_378] | 1 | 48 | PROPblock_1 |
| 10.1021/acs.jced.8b00895 [GLOBlit_7665] | 2 | 46 | PROPblock_1, PROPblock_2 |
| 10.1016/j.jct.2007.12.002 [GLOBlit_2892] | 1 | 45 | PROPblock_1 |
| 10.1021/acs.jced.8b00228 [GLOBlit_7500] | 2 | 40 | PROPblock_4, PROPblock_5 |
| 10.1021/je700700f [GLOBlit_11042] | 3 | 39 | PROPblock_15–17 |
| 10.1021/je201010s [GLOBlit_9722] | 2 | 38 | PROPblock_7, PROPblock_8 |
| 10.1021/acs.jced.7b00523 [GLOBlit_7238] | 2 | 36 | PROPblock_3, PROPblock_4 |
| 10.1016/j.fluid.2014.02.006 [GLOBlit_1423] | 4 |
```
</details>

---

### Step 4 [Q - L1_1 · c3]: `search_blocks` ❌ ERROR

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_6",
    "GLOBcomp_1"
  ],
  "system_type": "binary",
  "system_scope": "declared",
  "limit": 71,
  "purpose": "Find all binary propan-2-ol + water blocks with property details",
  "tasks": "Return property names and IDs for each block to rank studies by property coverage"
}
```
</details>

- **Result:** 493 chars  |  **Time:** 0.0s  |  **Started:** 05:36:37 (t+67.2s)
- **Error:** `{
  "error": "Tool `search_blocks` result is too large for its mandatory subagent (~10,708 tokens / 42,834 chars after hardcoded compaction).**\n\n### Result Stats\n- **After compaction:** 42,834 chars (~10,708 tokens)\n- **Markdown table rows:** 73\n- **Top-level keys:**\n  - `query_params`: dict(4 keys)\n  - `n_results`: int\n  - `results`: list[71]\n\nNarrow the query or add a dedicated deterministic compaction tier.",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "search_blocks"
}`
- **Subagent:** OVERSIZED in 42,834 → 399 chars (0.0s)
  - compact_md=42,834 chars > limit=40,000

---

### Step 5 [Q - L1_1 · c4]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_6",
    "GLOBcomp_1"
  ],
  "system_type": "binary",
  "system_scope": "declared",
  "limit": 20,
  "purpose": "Find binary propan-2-ol + water blocks with property details",
  "tasks": "Return block-level property names and IDs for ranking studies by breadth of characterization"
}
```
</details>

- **Result:** 953 chars  |  **Time:** 15.5s  |  **Started:** 05:36:45 (t+75.9s)
- **Subagent:** KEEP in 12,134 → 845 chars (14.8s)
  - **Summary:** 20 binary propan-2-ol + water blocks found across 9 DOIs, covering 8 distinct properties. The broadest studies are DOI `10.1016/j.fluid.2013.08.007` (density + Cp, 1248 pts) and `10.1016/

<details><summary>Result</summary>

```
**Summary:** 20 binary propan-2-ol + water blocks found across 9 DOIs, covering 8 distinct properties. The broadest studies are DOI `10.1016/j.fluid.2013.08.007 [GLOBlit_1311]` (density + Cp, 1248 pts) and `10.1016/j.fluid.2014.02.006 [GLOBlit_1423]` (VLE T, x, azeotropic T & composition, 4 blocks).

### DOI Breadth Ranking

| DOI | # Blocks | Distinct Properties (GLOBprop IDs) | Total Pts |
|-----|----------|-------------------------------------|-----------|
| 10.1016/j.fluid.2014.02.006 [GLOBlit_1423] | 4 | GLOBprop_14 (T_boil), GLOBprop_2 (x_vap), GLOBprop_58 (T_azeo), GLOBprop_45 (x_azeo) | 36 |
| 10.1016/j.fluid.2013.08.007 [GLOBlit_1311] | 2 | GLOBprop_1 (ρ), GLOBprop_9 (Cp) | 1248 |
| 10.1016/j.fluid.2017.09.010 [GLOBlit_2096] | 3 | GLOBprop_14 (T_boil), GLOBprop_2 (x_vap), GLOBprop_45 (x_azeo) | 37 |
| 10.1016/j.fluid.2015.11.034 [GLOBlit_1827] | 2 | GLOBprop_14 (T_boil), GLOBprop_2 (x_vap) | 28 |
| 10.1016/j.jct. [lit_num_id=null]
```
</details>

---

### Step 6 [Q - L1_1 · c5]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_6",
    "GLOBcomp_1"
  ],
  "system_type": "binary",
  "system_scope": "declared",
  "literature": [
    "GLOBlit_11042",
    "GLOBlit_9722",
    "GLOBlit_7238",
    "GLOBlit_7665",
    "GLOBlit_7500",
    "GLOBlit_11130",
    "GLOBlit_11142",
    "GLOBlit_2892",
    "GLOBlit_378",
    "GLOBlit_1910",
    "GLOBlit_2432"
  ],
  "limit": 50,
  "purpose": "Identify properties measured in remaining top DOIs for propan-2-ol + water binary",
  "tasks": "List properties and block details for these literature sources"
}
```
</details>

- **Result:** 1,330 chars  |  **Time:** 13.4s  |  **Started:** 05:37:20 (t+110.9s)
- **Subagent:** KEEP in 5,619 → 1,330 chars (13.2s)
  - Only 3 blocks were found, all from **GLOBlit_11042** (DOI 10.1021/je700700f). The other 10 queried literature sources returned no binary blocks for propan-2-ol + water. All data are at 298.15 K, 101.0

<details><summary>Result</summary>

```
Only 3 blocks were found, all from **GLOBlit_11042** (DOI 10.1021/je700700f). The other 10 queried literature sources returned no binary blocks for propan-2-ol + water. All data are at 298.15 K, 101.0 kPa, liquid phase, with mole fraction of propan-2-ol as the variable (13 pts each).

| Block | Property | GLOBprop | Method | x range | Key values |
|---|---|---|---|---|---|
| PROPblock_15 | Viscosity (Pa·s) | GLOBprop_4 | capillary_tube_ostwald_ubbelohde | 0.0–1.0 | max ≈ 0.003087 at x=0.2994 |
| PROPblock_16 | Refractive index (Na D-line) | GLOBprop_7 | standard_abbe_refractometry | 0.0–1.0 | 1.3325–1.3756 |
| PROPblock_17 | Mass density (kg/m³) | GLOBprop_1 | vibtub_ufactor_4 | 0.0–1.0 | 997.2→780.7 (monotonic↓) |

**Reference:** González et al. (2008) — "Density and Viscosity Experimental Data of the Ternary Mixtures 1-Propanol or 2-Propanol + Water + 1-Ethyl-3-methylimidazolium Ethylsulfate."

**Compounds:** DOIcomp_2 = GLOBcomp_6 (propan-2-ol), DOIcomp_3 = GLOBcomp_1 (water)

**Note:** The remaining 10 literature sources (GLOBlit_9722, GLOBlit_7238, GLOBlit_7665, GLOBlit_7500, GLOBlit_11130, GLOBlit_11142, GLOBlit_2892, GLOBlit_378, GLOBlit_1910, GLOBlit_2432) returned no matching binary blocks. They may contain data under different system scopes or for different subsystems within multicomponent datasets.
```
</details>

---

### Step 7 [Q - L1_1 · c6]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_6",
    "GLOBcomp_1"
  ],
  "system_type": "binary",
  "system_scope": "either",
  "literature": [
    "GLOBlit_9722",
    "GLOBlit_7238",
    "GLOBlit_7665",
    "GLOBlit_7500",
    "GLOBlit_11130",
    "GLOBlit_11142",
    "GLOBlit_2892",
    "GLOBlit_378",
    "GLOBlit_1910",
    "GLOBlit_2432"
  ],
  "limit": 30,
  "purpose": "Find property details for remaining DOIs with propan-2-ol + water data",
  "tasks": "Get property names and IDs for blocks in these literature sources"
}
```
</details>

- **Result:** 930 chars  |  **Time:** 13.3s  |  **Started:** 05:37:57 (t+147.3s)
- **Subagent:** KEEP in 3,630 → 930 chars (12.6s)
  - Only 2 blocks found, both from **GLOBlit_9722** (DOI: 10.1021/je201010s). The other 9 queried literature sources yielded no binary propan-2-ol + water blocks.

| Block | DOI | GLOBlit | Property | GLO

<details><summary>Result</summary>

```
Only 2 blocks found, both from **GLOBlit_9722** (DOI: 10.1021/je201010s). The other 9 queried literature sources yielded no binary propan-2-ol + water blocks.

| Block | DOI | GLOBlit | Property | GLOBprop | Phase | T (K) | P (kPa) | Pts | Variable |
|---|---|---|---|---|---|---|---|---|---|
| PROPblock_7 | 10.1021/je201010s | GLOBlit_9722 | refractive_index_na_dline | GLOBprop_7 | Liquid | 298.15 | 101.0 | 21 | mass_fraction (GLOBvar_5, DOIcomp_1=GLOBcomp_6 propan-2-ol) |
| PROPblock_8 | 10.1021/je201010s | GLOBlit_9722 | mass_density_kg_m3 | GLOBprop_1 | Liquid | 298.15 | 101.0 | 17 | mass_fraction (GLOBvar_5, DOIcomp_1=GLOBcomp_6 propan-2-ol) |

**Key IDs:**
- Compounds: DOIcomp_1 = GLOBcomp_6 (propan-2-ol), DOIcomp_3 = GLOBcomp_1 (water)
- Methods: GLOBmeas_3 (standard_abbe_refractometry), GLOBmeas_2 (vibrating_tube_method)
- Constraints: BLKconstr_1 = GLOBconstr_1 (pressure_kpa, 101.0), BLKconstr_2 = GLOBconstr_
```
</details>

---

### Step 8 [Q - L1_1 · c7]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "literature": [
    "GLOBlit_7665",
    "GLOBlit_7238",
    "GLOBlit_7500",
    "GLOBlit_11130",
    "GLOBlit_11142",
    "GLOBlit_2892",
    "GLOBlit_378",
    "GLOBlit_1910",
    "GLOBlit_2432"
  ],
  "compound": [
    "GLOBcomp_6",
    "GLOBcomp_1"
  ],
  "system_scope": "either",
  "limit": 30,
  "purpose": "Get property details for remaining DOIs with propan-2-ol + water data",
  "tasks": "Identify properties measured in each remaining study"
}
```
</details>

- **Result:** 1,137 chars  |  **Time:** 15.4s  |  **Started:** 05:38:28 (t+179.0s)
- **Subagent:** KEEP in 3,466 → 1,137 chars (15.3s)
  - Only **1 of 9 queried DOIs** returned blocks: **GLOBlit_7665** (10.1021/acs.jced.8b00895) has VLE data for propan-2-ol + water. The remaining 8 literature IDs (GLOBlit_7238, GLOBlit_7500, GLOBlit_1113

<details><summary>Result</summary>

```
Only **1 of 9 queried DOIs** returned blocks: **GLOBlit_7665** (10.1021/acs.jced.8b00895) has VLE data for propan-2-ol + water. The remaining 8 literature IDs (GLOBlit_7238, GLOBlit_7500, GLOBlit_11130, GLOBlit_11142, GLOBlit_2892, GLOBlit_378, GLOBlit_1910, GLOBlit_2432) produced no matching blocks — they may contain multicomponent systems (with DES/salt additives) where propan-2-ol + water appear but are not the sole binary pair.

| Block | DOI | lit_id | Property | Phase | Pts | Constraint |
|---|---|---|---|---|---|---|
| PROPblock_1 | 10.1021/acs.jced.8b00895 | GLOBlit_7665 | boiling_temperature_at_pressure_p_k (GLOBprop_14) | Liquid→Gas | 23 | P = 101.3 kPa |
| PROPblock_2 | 10.1021/acs.jced.8b00895 | GLOBlit_7665 | mole_fraction (vapor composition, GLOBprop_2) | Gas (VLE) | 23 | P = 101.3 kPa |

**GLOBlit_7665 details:**
- **PROPblock_1**: T_boil vs x(propan-2-ol, liquid) at 101.3 kPa; range x = 0.0201–0.9492, T = 353.31–367.1 K; non-monotonic (azeotrope); method: ebulliometric recirculating still.
- **PROPblock_2**: y(propan-2-ol, gas) vs x(propan-2-ol, liquid) at 101.3 kPa; x-y VLE data; method: chromatography.
```
</details>

---

## Nested tool calls — L1_2 (L1-query)

**Nest:** Q - L1_2
**Parent:** `L1_query` — Step 2 [Q · c20] relays this worker's result
**Started:** 05:40:18  |  **Ended:** 05:46:48  |  **Tool calls:** 11

---

### Step 2 [Q - L1_2 · c9]: `resolve_compound_ids`

<details><summary>Arguments</summary>

```json
{
  "queries": [
    "water",
    "propan-2-ol",
    "isopropanol",
    "2-propanol"
  ],
  "min_score": 50,
  "limit": 10,
  "purpose": "Resolve compound IDs for water and propan-2-ol/isopropanol",
  "tasks": "Find canonical global IDs for water and propan-2-ol"
}
```
</details>

- **Result:** 190 chars  |  **Time:** 4.3s  |  **Started:** 05:40:29 (t+299.4s)
- **Subagent:** KEEP in 285 → 190 chars (4.2s)
  - Both compounds resolved with exact name matches.

| Compound | Global ID | Formula | SMILES |
|---|---|---|---|
| water | GLOBcomp_1 | H2O | O |
| propan-2-ol | GLOBcomp_6 | C3H8O | CC(C)O |

<details><summary>Result</summary>

```
Both compounds resolved with exact name matches.

| Compound | Global ID | Formula | SMILES |
|---|---|---|---|
| water | GLOBcomp_1 | H2O | O |
| propan-2-ol | GLOBcomp_6 | C3H8O | CC(C)O |
```
</details>

---

### Step 3 [Q - L1_2 · c10]: `search_system_registry`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_6"
  ],
  "system_type": "binary",
  "system_scope": "declared",
  "limit": 100,
  "purpose": "Find all binary water + propan-2-ol data blocks in ThermoML",
  "tasks": "List all literature sources, properties, and block counts for the binary system water + propan-2-ol"
}
```
</details>

- **Result:** 1,289 chars  |  **Time:** 20.2s  |  **Started:** 05:40:43 (t+313.2s)
- **Subagent:** KEEP in 10,570 → 1,110 chars (14.0s)
  - **Summary:** 71 declared binary property blocks for water + propan-2-ol were found across **37 unique DOIs**, totaling ~2,895 data points. Property names are not included in the registry output; indiv

<details><summary>Result</summary>

```
**Summary:** 71 declared binary property blocks for water + propan-2-ol were found across **37 unique DOIs**, totaling ~2,895 data points. Property names are not included in the registry output; individual blocks must be queried to obtain property details.

**By DOI — block counts and total points:**

| DOI | Blocks | Total Pts | Block IDs |
|-----|--------|-----------|-----------|
| 10.1016/j.fluid.2006.03.021 [GLOBlit_378] | 1 | 48 | PROPblock_1 |
| 10.1016/j.fluid.2013.08.007 [GLOBlit_1311] | 2 | 1248 | PROPblock_4, PROPblock_5 |
| 10.1016/j.fluid.2014.02.006 [GLOBlit_1423] | 4 | 36 | PROPblock_11–14 |
| 10.1016/j.fluid.2015.09.052 [GLOBlit_1801] | 1 | 17 | PROPblock_13 |
| 10.1016/j.fluid.2015.11.034 [GLOBlit_1827] | 2 | 28 | PROPblock_1, PROPblock_2 |
| 10.1016/j.fluid.2016.04.007 [GLOBlit_1910] | 1 | 60 | PROPblock_2 |
| 10.1016/j.fluid.2017.09.010 [GLOBlit_2096] | 3 | 37 | PROPblock_5–7 |
| 10.1016/j.jct.2004.07.019 [GLOBlit_2432] | 1 | 529 | PROPblock_4 |
| 10.1016/j.jct.2006.04.006 [GLOBlit_2687] | 2 | 34 | PROPblock_3, PROPblock_4 |
| 10.1016/j.jct.2007.12.002 [GLOBlit_2892] | 1 | 45 | PROPblock_1 |
| 10.1016/j.jct.2016.10.001 [GLOBlit_4843] | 2 | 30 | PROPblock_9, PROPblock_10 |
| 10.1016/j.jct.2017.02.005 [GLOBlit_4959] | 2 | 62 | PROPblock_3, PROPblock_4 |
```
</details>

---

### Step 4 [Q - L1_2 · c11]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_6"
  ],
  "system_type": "binary",
  "system_scope": "declared",
  "limit": 50,
  "purpose": "Find properties measured in binary water + propan-2-ol blocks",
  "tasks": "List all blocks with their properties, measurement methods, and compound purities for ranking DOIs by characterization breadth"
}
```
</details>

- **Result:** 1,482 chars  |  **Time:** 21.6s  |  **Started:** 05:41:11 (t+341.9s)
- **Subagent:** KEEP in 30,354 → 1,347 chars (15.0s)
  - **Summary:** 50 binary water + propan-2-ol blocks found across 20 DOIs. The broadest characterization comes from DOIs covering multiple distinct property types. No compound purity information was retu

<details><summary>Result</summary>

```
**Summary:** 50 binary water + propan-2-ol blocks found across 20 DOIs. The broadest characterization comes from DOIs covering multiple distinct property types. No compound purity information was returned in block details — purities would require separate `get_block_details` calls.

**DOI-level property breadth (ranked by number of distinct properties):**

| DOI | Blocks | Distinct Properties | Properties Listed |
|-----|--------|---------------------|-------------------|
| 10.1016/j.fluid.2013.08.007 [GLOBlit_1311] | PROPblock_4, PROPblock_5 | 2 | Mass density (GLOBprop_1), Cp (GLOBprop_9) |
| 10.1016/j.fluid.2014.02.006 [GLOBlit_1423] | PROPblock_11–14 | 4 | T_boil (GLOBprop_14), x (GLOBprop_2), T_azeo (GLOBprop_58), x_azeo (GLOBprop_45) |
| 10.1016/j.jct.2019.105880 [GLOBlit_5585] | PROPblock_10–12 | 3 | Mass density, Speed of sound (GLOBprop_8), Viscosity (GLOBprop_4) |
| 10.1021/acs.jced.6b00019 [GLOBlit_6822] | PROPblock_13–14 | 2 | Mass density, Refractive index (GLOBprop_7) |
| 10.1021/acs.jced.8b00160 [GLOBlit_7474] | PROPblock_15–16 | 2 | Mass density, Refractive index |
| 10.1021/acs.jced.8b00181 [GLOBlit_7483] | PROPblock_6–7 | 2 | Refractive index, Elec. conductivity (GLOBprop_18) |
| 10.1021/acs.jced.8b00723 [GLOBlit_7629] | PROPblock_14–15 | 2 | Mass density, Speed of sound |
| 10.1021/je049738c [GLOBlit_8447] | PROPblock_27–28 | 2 | Cp/volume (GLOBprop_63), Mass density |
| 10.1016/j.fluid.2017.09.010 [GLOBlit_2096] | PROPblock_5–7 | 3 | T_bo
```
</details>

---

### Step 5 [Q - L1_2 · c12]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_6"
  ],
  "system_type": "binary",
  "system_scope": "declared",
  "limit": 50,
  "block_number": "GLOBlit_5585::PROPblock_10",
  "purpose": "Inspect block details for GLOBlit_5585 to get measurement methods and purities",
  "tasks": "Get full block card including measurement method, compound purities, variables, constraints"
}
```
</details>

- **Result:** 1,270 chars  |  **Time:** 12.4s  |  **Started:** 05:41:44 (t+374.6s)
- **Subagent:** KEEP in 1,993 → 1,255 chars (12.3s)
  - **Summary:** PROPblock_10 from GLOBlit_5585 measures mass density (kg/m³) of the binary water + propan-2-ol system using the **vibrating tube method** (GLOBmeas_2), at 100 kPa, over T = 288.15–303.15 

<details><summary>Result</summary>

```
**Summary:** PROPblock_10 from GLOBlit_5585 measures mass density (kg/m³) of the binary water + propan-2-ol system using the **vibrating tube method** (GLOBmeas_2), at 100 kPa, over T = 288.15–303.15 K and w(propan-2-ol) = 0.1–0.3. **No compound purity information** is present in this block card.

### Block Details

| Field | Value |
|---|---|
| **Block** | PROPblock_10 |
| **DOI** | 10.1016/j.jct.2019.105880 [GLOBlit_5585] |
| **lit_id** | GLOBlit_5585 (2019-meh-haj-0) |
| **Property** | mass_density_kg_m3 (BLKprop_1 → GLOBprop_1) |
| **Method** | vibrating_tube_method (GLOBmeas_2) |
| **Phase** | Liquid |
| **Points** | 12 |
| **Uncertainty** | k=95%, Propagation, compiler |

### Compounds

| org_num | comp_num_id | Name | Formula |
|---|---|---|---|
| DOIcomp_3 | GLOBcomp_6 | propan-2-ol | C3H8O |
| DOIcomp_4 | GLOBcomp_1 | water | H2O |

### Variables & Constraints

| ID | Type | Detail | Component |
|---|---|---|---|
| BLKvar_1 (GLOBvar_1) | temperature_k | 288.15–303.15 K | — |
| BLKvar_2 (GLOBvar_5) | mass_fraction | 0.1–0.3 | DOIcomp_3 (propan-2-ol) |
| BLKconstr_1 (GLOBconstr_1) | pressure_kpa | 100.0 | — |

### Data (all 12 pts)

| T (K) | w(propan-2-ol) | ρ (kg/m³) | ±U |
|---|---|---|---|
| 288.15 | 0.1 | 983.401 | 1.24 |
| 288.15 | 0.2 |
```
</details>

---

### Step 6 [Q - L1_2 · c13]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_6"
  ],
  "block_number": "GLOBlit_5585::PROPblock_11",
  "purpose": "Inspect block 11 from GLOBlit_5585 for property, method, purity details",
  "tasks": "Get property name, measurement method, compound purities, data range"
}
```
</details>

- **Result:** 1,041 chars  |  **Time:** 11.8s  |  **Started:** 05:42:10 (t+400.6s)
- **Subagent:** KEEP in 2,069 → 1,041 chars (11.5s)
  - **Summary:** PROPblock_11 from GLOBlit_5585 reports **speed of sound (m/s)** for the binary system propan-2-ol + water, measured via the **single path length method** at 3.0 MHz and 100.0 kPa. **No co

<details><summary>Result</summary>

```
**Summary:** PROPblock_11 from GLOBlit_5585 reports **speed of sound (m/s)** for the binary system propan-2-ol + water, measured via the **single path length method** at 3.0 MHz and 100.0 kPa. **No compound purity information** is included in this block.

### Block Details

| Field | Value |
|---|---|
| Block | PROPblock_11 |
| Literature | GLOBlit_5585 (DOI: 10.1016/j.jct.2019.105880) |
| Property | speed_of_sound_m_s (GLOBprop_8) |
| Method | single_path_length_method (GLOBmeas_18) |
| Phase | Liquid |
| Points | 12 |
| Purities | **Not reported** |

### Compounds

| comp_num_id | Name | Role |
|---|---|---|
| GLOBcomp_6 (DOIcomp_3) | propan-2-ol | variable component (mass fraction) |
| GLOBcomp_1 (DOIcomp_4) | water | solvent |

### Data Range

| Variable/Constraint | Range |
|---|---|
| Temperature (BLKvar_1) | 288.15–303.15 K |
| w(propan-2-ol) (BLKvar_2) | 0.1–0.3 |
| Pressure (BLKconstr_1) | 100.0 kPa |
| Frequency (BLKconstr_2) | 3.0 MHz |
| Speed of sound | 1549.6–1638.6 m/s |
| Uncertainty (k=95%) | ±2.03–6.79 m/s |
```
</details>

---

### Step 7 [Q - L1_2 · c14]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_6"
  ],
  "block_number": "GLOBlit_5585::PROPblock_12",
  "purpose": "Inspect viscosity block from GLOBlit_5585",
  "tasks": "Get property, method, purity details for PROPblock_12"
}
```
</details>

- **Result:** 1,258 chars  |  **Time:** 11.5s  |  **Started:** 05:42:29 (t+419.8s)
- **Subagent:** KEEP in 2,041 → 1,258 chars (11.1s)
  - **Summary:** PROPblock_12 from GLOBlit_5585 is a binary viscosity block for propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1), measured by falling/rolling sphere viscometry in the liquid phase at 100 kPa.

<details><summary>Result</summary>

```
**Summary:** PROPblock_12 from GLOBlit_5585 is a binary viscosity block for propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1), measured by falling/rolling sphere viscometry in the liquid phase at 100 kPa. It contains 12 data points spanning T = 288.15–303.15 K and mass fraction of propan-2-ol = 0.1–0.3. No purity information is reported.

### Property & Method

| Field | Value |
|---|---|
| BLKprop_id | BLKprop_1 |
| prop_num_id | GLOBprop_4 |
| Property | viscosity_pa_s |
| Method (GLOBmeas_8) | falling_or_rolling_sphere_viscometry |
| Phase | Liquid |
| Constraint | pressure_kpa = 100.0 (BLKconstr_1 / GLOBconstr_1) |
| Uncertainty | k=95%, Propagation, compiler |

### Variables

| BLKvar_id | var_num_id | Variable | Component |
|---|---|---|---|
| BLKvar_1 | GLOBvar_1 | temperature_k | — |
| BLKvar_2 | GLOBvar_5 | mass_fraction_DOIcomp_3 | DOIcomp_3 (propan-2-ol) |

### Data (12 pts)

| T (K) | w(propan-2-ol) | η (Pa·s) | ±U |
|---|---|---|---|
| 288.15 | 0.1 | 0.001936 | 0.000164 |
| 288.15 | 0.2 | 0.003087 | 0.000214 |
| 288.15 | 0.3 | 0.004014 | 0.00026 |
| 293.15 | 0.1 | 0.001633 | 0.000129 |
| 293.15 | 0.2 | 0.002485 | 0.000169 |
| 293.15 | 0.3 | 0.003172 | 0.000206 |
| 298.15 | 0.1 | 0.001395 | 0.000105 |
| 298.15 | 0.2 | 0.002045 | 0
```
</details>

---

### Step 8 [Q - L1_2 · c15]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_6"
  ],
  "block_number": "GLOBlit_1423::PROPblock_11",
  "purpose": "Inspect VLE block from GLOBlit_1423",
  "tasks": "Get property, method, purity details"
}
```
</details>

- **Result:** 1,378 chars  |  **Time:** 12.9s  |  **Started:** 05:42:56 (t+446.7s)
- **Subagent:** KEEP in 1,947 → 1,363 chars (12.7s)
  - **Summary:** PROPblock_11 from GLOBlit_1423 contains isobaric VLE (boiling temperature) data for the binary system propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1) at 101.3 kPa, measured by ebulliometric

<details><summary>Result</summary>

```
**Summary:** PROPblock_11 from GLOBlit_1423 contains isobaric VLE (boiling temperature) data for the binary system propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1) at 101.3 kPa, measured by ebulliometric (recirculating still) method. 17 data points span x(propan-2-ol) = 0–1, with T_boil ranging ~353–373 K, showing an azeotrope near x ≈ 0.69–0.74.

### Block Details

| Field | Value |
|---|---|
| **Block** | PROPblock_11 |
| **DOI** | 10.1016/j.fluid.2014.02.006 [GLOBlit_1423] |
| **lit_id** | GLOBlit_1423 (2014-lin-tu-0) |
| **Property** | boiling_temperature_at_pressure_p_k (BLKprop_1 → GLOBprop_14) |
| **Method** | ebulliometric_method_recirculating_still (GLOBmeas_5) |
| **Phase** | Liquid + Gas |
| **Variable** | mole_fraction of DOIcomp_1 (propan-2-ol) in Liquid (BLKvar_1 → GLOBvar_2) |
| **Constraint** | pressure_kpa = 101.3 (Gas phase) (BLKconstr_1 → GLOBconstr_1) |
| **Uncertainty** | k=95%, Propagation, compiler |
| **Points** | 17 (10 kept via RDP) |

### Compounds

| DOI label | Global ID | Name | Formula |
|---|---|---|---|
| DOIcomp_1 | GLOBcomp_6 | propan-2-ol | C3H8O |
| DOIcomp_2 | GLOBcomp_1 | water | H2O |

**Note:** No explicit purity information was reported in this block.

### Data (10 pts, RDP-reduced)

| x(propan-2-ol, Liquid) | T_boil (K) | ±U (K) |
|---|---|---|
| 0.0 | 373.15 | 0.13 |
| 0.05 | 359.86 | 0.2 |
| 0.113 | 356.54 | 0.14 |
```
</details>

---

### Step 9 [Q - L1_2 · c16]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_6"
  ],
  "block_number": "GLOBlit_1423::PROPblock_12",
  "purpose": "Inspect block 12 of GLOBlit_1423 for property details",
  "tasks": "Get property, method, purity info"
}
```
</details>

- **Result:** 1,316 chars  |  **Time:** 11.3s  |  **Started:** 05:43:17 (t+467.4s)
- **Subagent:** KEEP in 1,840 → 1,316 chars (10.6s)
  - **Summary:** PROPblock_12 of GLOBlit_1423 is a binary VLE block for propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1) at constant pressure 101.3 kPa. It measures gas-phase mole fraction of propan-2-ol via

<details><summary>Result</summary>

```
**Summary:** PROPblock_12 of GLOBlit_1423 is a binary VLE block for propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1) at constant pressure 101.3 kPa. It measures gas-phase mole fraction of propan-2-ol via chromatography (GLOBmeas_1), with liquid-phase mole fraction as the variable. 17 data points total. No purity information is reported in this block.

### Property Details

| Field | Value |
|---|---|
| **Block** | PROPblock_12 |
| **Literature** | GLOBlit_1423 (DOI: 10.1016/j.fluid.2014.02.006) |
| **Property** | BLKprop_1 → GLOBprop_2: mole_fraction of DOIcomp_1 (propan-2-ol) |
| **Method** | GLOBmeas_1: chromatography |
| **Group** | CompositionAtPhaseEquilibrium |
| **Phase (measured)** | Gas |
| **Variable** | BLKvar_1 → GLOBvar_2: mole_fraction of DOIcomp_1, Liquid phase |
| **Constraint** | BLKconstr_1 → GLOBconstr_1: pressure_kpa = 101.3 (Gas) |
| **Points** | 17 (9 kept after RDP) |
| **Purity info** | Not reported |
| **Uncertainty** | k=95%, Propagation, compiler |

### Compounds

| DOI ID | Global ID | Name | Formula |
|---|---|---|---|
| DOIcomp_1 | GLOBcomp_6 | propan-2-ol | C3H8O |
| DOIcomp_2 | GLOBcomp_1 | water | H2O |

### Data (9 RDP-kept points)

| x(propan-2-ol, Liquid) | x(propan-2-ol, Gas) | ±U |
|---|---|---|
| 0.0 | 0.0 | — |
| 0.017 | 0.222 | 0.019 |
| 0.05 | 0.401 | 0.007
```
</details>

---

### Step 10 [Q - L1_2 · c17]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_6"
  ],
  "block_number": "GLOBlit_1423::PROPblock_13",
  "purpose": "Inspect block 13 of GLOBlit_1423 for property details",
  "tasks": "Get property, method, purity info"
}
```
</details>

- **Result:** 736 chars  |  **Time:** 8.2s  |  **Started:** 05:43:35 (t+485.1s)
- **Subagent:** KEEP in 1,327 → 736 chars (8.1s)
  - **Summary:** PROPblock_13 of GLOBlit_1423 reports a single azeotropic temperature data point for the binary system propan-2-ol + water at 101.3 kPa. The azeotropic temperature is 353.21 K (±0.23 K, k=

<details><summary>Result</summary>

```
**Summary:** PROPblock_13 of GLOBlit_1423 reports a single azeotropic temperature data point for the binary system propan-2-ol + water at 101.3 kPa. The azeotropic temperature is 353.21 K (±0.23 K, k=95%). No purity information is provided in this block.

### Property Details

| Field | Value |
|---|---|
| **Block** | PROPblock_13 |
| **Property** | Azeotropic temperature (K) — `GLOBprop_58` |
| **Method** | by_x_y (`GLOBmeas_39`) |
| **Phase** | Liquid |
| **System** | Binary: propan-2-ol (`GLOBcomp_6`, DOIcomp_1) + water (`GLOBcomp_1`, DOIcomp_2) |
| **Uncertainty** | k=95%, Propagation, compiler |
| **Purity** | Not reported in this block |

### Data

| P (kPa) | T_azeo (K) | ±U (K) |
|---|---|---|
| 101.3 | 353.21 | 0.23 |
```
</details>

---

### Step 11 [Q - L1_2 · c18]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_6"
  ],
  "block_number": "GLOBlit_1423::PROPblock_14",
  "purpose": "Inspect block 14 of GLOBlit_1423 for azeotropic composition data",
  "tasks": "Get property, method, and purity details"
}
```
</details>

- **Result:** 967 chars  |  **Time:** 9.6s  |  **Started:** 05:43:49 (t+500.1s)
- **Subagent:** KEEP in 1,375 → 967 chars (8.8s)
  - **Summary:** PROPblock_14 of GLOBlit_1423 contains a single azeotropic composition data point for the propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1) binary system at 101.3 kPa. The azeotropic mole frac

<details><summary>Result</summary>

```
**Summary:** PROPblock_14 of GLOBlit_1423 contains a single azeotropic composition data point for the propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1) binary system at 101.3 kPa. The azeotropic mole fraction of propan-2-ol is **0.688 ± 0.004** (k=95%).

### Property Details

| Field | Value |
|---|---|
| **Block** | PROPblock_14 |
| **Property** | Azeotropic composition, mole fraction (DOIcomp_1 = propan-2-ol) |
| **BLKprop_id** | BLKprop_1 |
| **prop_num_id** | GLOBprop_45 |
| **Method** | by_x_y (GLOBmeas_39) |
| **Group** | CompositionAtPhaseEquilibrium |
| **Phase** | Liquid |
| **Variable** | pressure_kpa (BLKvar_1 / GLOBvar_3), Gas phase |
| **Uncertainty** | k=95%, Propagation, compiler |

### Data Point

| P (kPa) | x(propan-2-ol, Liquid) | ±U |
|---|---|---|
| 101.3 | 0.688 | 0.004 |

### Compounds

| org_num | comp_num_id | Name | Formula |
|---|---|---|---|
| DOIcomp_1 | GLOBcomp_6 | propan-2-ol | C3H8O |
| DOIcomp_2 | GLOBcomp_1 | water | H2O |
```
</details>

---

### Step 12 [Q - L1_2 · c19]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_6"
  ],
  "block_number": "GLOBlit_2096::PROPblock_5",
  "purpose": "Inspect GLOBlit_2096 block 5 for property details",
  "tasks": "Get property, method, purity info"
}
```
</details>

- **Result:** 1,268 chars  |  **Time:** 12.0s  |  **Started:** 05:44:09 (t+519.2s)
- **Subagent:** KEEP in 1,952 → 1,268 chars (11.8s)
  - **Summary:** PROPblock_5 in GLOBlit_2096 contains **boiling temperature at pressure P (K)** for the binary system **propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1)**, measured by **ebulliometric method 

<details><summary>Result</summary>

```
**Summary:** PROPblock_5 in GLOBlit_2096 contains **boiling temperature at pressure P (K)** for the binary system **propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1)**, measured by **ebulliometric method (recirculating still)** at a fixed pressure of **101.0 kPa**. 18 data points span the full composition range (x = 0–1), showing a non-monotonic (azeotropic) profile with a minimum near 353.1 K. No purity information is reported in this block.

### Property Details

| Field | Value |
|---|---|
| Block | PROPblock_5 |
| Property | boiling_temperature_at_pressure_p_k (BLKprop_1 → GLOBprop_14) |
| Method | ebulliometric_method_recirculating_still (GLOBmeas_5) |
| Group | VaporPBoilingTAzeotropTandP |
| Phase | Liquid |
| Constraint | pressure_kpa = 101.0 (BLKconstr_1 → GLOBconstr_1) |
| Variable | mole_fraction of propan-2-ol in Liquid (BLKvar_1 → GLOBvar_2) |
| Points | 18 (10 kept after RDP) |
| Uncertainty | k=95%, Propagation, compiler |
| Purity info | Not reported |

### Data (10 pts, RDP-compressed)

| x(propan-2-ol, Liquid) | T_boil (K) | ±U (K) |
|---|---|---|
| 0.0 | 373.0 | 1.0 |
| 0.0172 | 367.1 | 0.8 |
| 0.0695 | 359.5 | 0.5 |
| 0.1263 | 356.7 | 0.2 |
| 0.1961 | 355.6 | 0.2 |
| 0.2705 | 354.9 | 0.2 |
| 0.6217 | 353.3 | 0.2 |
| 0.6892 | 353.1 |
```
</details>

---

## Nested tool calls — L1_3 (L1-query)

**Nest:** Q - L1_3
**Parent:** `L1_query` — Step 3 [Q · c26] relays this worker's result
**Started:** 05:46:58  |  **Ended:** 05:51:03  |  **Tool calls:** 5

---

### Step 2 [Q - L1_3 · c21]: `resolve_compound_ids`

<details><summary>Arguments</summary>

```json
{
  "queries": [
    "water",
    "propan-2-ol"
  ],
  "min_score": 50,
  "limit": 5,
  "purpose": "Resolve global IDs for water and propan-2-ol",
  "tasks": "Find GLOBcomp IDs for water and 2-propanol"
}
```
</details>

- **Result:** 203 chars  |  **Time:** 4.5s  |  **Started:** 05:47:07 (t+698.0s)
- **Subagent:** KEEP in 285 → 203 chars (4.1s)
  - Both compounds resolved successfully with exact name matches.

| Compound | Global ID | Formula | SMILES |
|---|---|---|---|
| water | GLOBcomp_1 | H2O | O |
| propan-2-ol | GLOBcomp_6 | C3H8O | CC(C)

<details><summary>Result</summary>

```
Both compounds resolved successfully with exact name matches.

| Compound | Global ID | Formula | SMILES |
|---|---|---|---|
| water | GLOBcomp_1 | H2O | O |
| propan-2-ol | GLOBcomp_6 | C3H8O | CC(C)O |
```
</details>

---

### Step 3 [Q - L1_3 · c22]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_6"
  ],
  "system_type": "binary",
  "limit": 50,
  "purpose": "Find all data blocks for binary water + propan-2-ol system",
  "tasks": "List all literature sources, their DOIs, block counts, and properties measured for this binary system"
}
```
</details>

- **Result:** 1,477 chars  |  **Time:** 15.1s  |  **Started:** 05:47:18 (t+708.6s)
- **Subagent:** KEEP in 30,354 → 1,313 chars (14.1s)
  - **Summary:** 50 data blocks found across 25 unique DOIs for the binary water (GLOBcomp_1) + propan-2-ol (GLOBcomp_6) system, covering VLE (boiling T, mole fraction, azeotropic data), density, heat cap

<details><summary>Result</summary>

```
**Summary:** 50 data blocks found across 25 unique DOIs for the binary water (GLOBcomp_1) + propan-2-ol (GLOBcomp_6) system, covering VLE (boiling T, mole fraction, azeotropic data), density, heat capacity, viscosity, surface tension, speed of sound, refractive index, excess enthalpy, electrical conductivity, and vapor pressure.

| DOI | Blocks | Properties |
|-----|--------|------------|
| 10.1016/j.fluid.2006.03.021 [GLOBlit_378] | PROPblock_1 (48 pts) | Boiling temperature at pressure P |
| 10.1016/j.fluid.2013.08.007 [GLOBlit_1311] | PROPblock_4 (1110 pts), PROPblock_5 (138 pts) | Mass density; Molar Cp |
| 10.1016/j.fluid.2014.02.006 [GLOBlit_1423] | PROPblock_11–14 (17,17,1,1 pts) | Boiling T; Mole fraction; Azeotropic T; Azeotropic x |
| 10.1016/j.fluid.2015.09.052 [GLOBlit_1801] | PROPblock_13 (17 pts) | Boiling T |
| 10.1016/j.fluid.2015.11.034 [GLOBlit_1827] | PROPblock_1–2 (14,14 pts) | Boiling T; Mole fraction |
| 10.1016/j.fluid.2016.04.007 [GLOBlit_1910] | PROPblock_2 (60 pts) | Surface tension |
| 10.1016/j.fluid.2017.09.010 [GLOBlit_2096] | PROPblock_5–7 (18,18,1 pts) | Boiling T; Mole fraction; Azeotropic x |
| 10.1016/j.jct.2004.07.019 [GLOBlit_2432] | PROPblock_4 (529 pts) | Mass density |
| 10.1016/j.jct.2006.04.006 [GLOBlit_2687] | PROPblock_3–4 (17,17 pts) | Boiling T; Mole fraction |
| 10.1016/j.jct.2007.12.002 [GLOBlit_2892] | PROPblock_1 (45 pts) | Excess molar enthalpy |
| 10.1016/j.jct.2016.10.001 [GLOBlit_4843] | PROPblock_9–
```
</details>

---

### Step 4 [Q - L1_3 · c23]: `search_system_registry`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_6"
  ],
  "system_type": "binary",
  "system_scope": "declared",
  "limit": 100,
  "purpose": "Find all literature entries for binary water + propan-2-ol system",
  "tasks": "List all blocks with their literature IDs, DOIs, properties, and data point counts"
}
```
</details>

- **Result:** 1,319 chars  |  **Time:** 22.9s  |  **Started:** 05:47:40 (t+731.0s)
- **Subagent:** KEEP in 10,570 → 1,137 chars (16.3s)
  - **Summary:** 71 declared binary propan-2-ol + water property blocks found across 38 distinct DOIs, totaling ~2,893 data points. Property names and literature IDs (GLOBlit_N) are **not** included in th

<details><summary>Result</summary>

```
**Summary:** 71 declared binary propan-2-ol + water property blocks found across 38 distinct DOIs, totaling ~2,893 data points. Property names and literature IDs (GLOBlit_N) are **not** included in the registry output — block detail sections are empty. The largest datasets are from `10.1016/j.fluid.2013.08.007 [GLOBlit_1311]` (1,248 pts) and `10.1016/j.jct.2004.07.019 [GLOBlit_2432]` (529 pts).

**Triage: 71 blocks — showing top 10 by data point count.**

| # | DOI | Block | Points |
|---|-----|-------|--------|
| 1 | 10.1016/j.fluid.2013.08.007 [GLOBlit_1311] | PROPblock_4 | 1110 |
| 2 | 10.1016/j.jct.2004.07.019 [GLOBlit_2432] | PROPblock_4 | 529 |
| 3 | 10.1021/je8001305 [GLOBlit_11130] | PROPblock_1 | 209 |
| 4 | 10.1016/j.fluid.2013.08.007 [GLOBlit_1311] | PROPblock_5 | 138 |
| 5 | 10.1016/j.fluid.2016.04.007 [GLOBlit_1910] | PROPblock_2 | 60 |
| 6 | 10.1021/je800158z [GLOBlit_11142] | PROPblock_4 | 56 |
| 7 | 10.1016/j.fluid.2006.03.021 [GLOBlit_378] | PROPblock_1 | 48 |
| 8 | 10.1016/j.jct.2007.12.002 [GLOBlit_2892] | PROPblock_1 | 45 |
| 9 | 10.1016/j.jct.2017.02.005 [GLOBlit_4959] | PROPblock_3 | 31 |
| 10 | 10.1021/je900966r [GLOBlit_11872] | PROPblock_6 | 30 |

**Remaining 61 blocks** range from 1 to 24 points each, spread across 33 additional DOIs.

**Search-refinement strategy:**
1. To
```
</details>

---

### Step 5 [Q - L1_3 · c24]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_6"
  ],
  "system_type": "binary",
  "limit": 50,
  "purpose": "Get remaining binary water+propan-2-ol blocks with property details",
  "tasks": "Capture blocks not shown in previous truncated results to complete the property-per-study ranking"
}
```
</details>

- **Result:** 1,373 chars  |  **Time:** 21.3s  |  **Started:** 05:48:34 (t+784.9s)
- **Subagent:** KEEP in 30,354 → 1,164 chars (15.6s)
  - All 50 binary water (GLOBcomp_1) + propan-2-ol (GLOBcomp_6) blocks retrieved successfully across 25 DOIs.

| DOI | Block | Property | Pts |
|-----|-------|----------|-----|
| 10.1016/j.fluid.2006.03.0

<details><summary>Result</summary>

```
All 50 binary water (GLOBcomp_1) + propan-2-ol (GLOBcomp_6) blocks retrieved successfully across 25 DOIs.

| DOI | Block | Property | Pts |
|-----|-------|----------|-----|
| 10.1016/j.fluid.2006.03.021 [GLOBlit_378] | PROPblock_1 | Boiling temperature | 48 |
| 10.1016/j.fluid.2013.08.007 [GLOBlit_1311] | PROPblock_4 | Mass density | 1110 |
| 10.1016/j.fluid.2013.08.007 [GLOBlit_1311] | PROPblock_5 | Molar Cp | 138 |
| 10.1016/j.fluid.2014.02.006 [GLOBlit_1423] | PROPblock_11 | Boiling temperature | 17 |
| 10.1016/j.fluid.2014.02.006 [GLOBlit_1423] | PROPblock_12 | Mole fraction | 17 |
| 10.1016/j.fluid.2014.02.006 [GLOBlit_1423] | PROPblock_13 | Azeotropic temperature | 1 |
| 10.1016/j.fluid.2014.02.006 [GLOBlit_1423] | PROPblock_14 | Azeotropic composition | 1 |
| 10.1016/j.fluid.2015.09.052 [GLOBlit_1801] | PROPblock_13 | Boiling temperature | 17 |
| 10.1016/j.fluid.2015.11.034 [GLOBlit_1827] | PROPblock_1 | Boiling temperature | 14 |
| 10.1016/j.fluid.2015.11.034 [GLOBlit_1827] | PROPblock_2 | Mole fraction | 14 |
| 10.1016/j.fluid.2016.04.007 [GLOBlit_1910] | PROPblock_2 | Surface tension | 60 |
| 10.1016/j.fluid.2017.09.010 [GLOBlit_2096] | PROPblock_5 | Boiling temperature | 18 |
| 10.1016/j.fluid.2017.09.010 [GLOBlit_2096] | PROPblock_6 | Mole fraction | 18 |
| 10.1016/j.fluid.2017.09.010 [GLOBlit_2096] | PROPblock_7 | Azeotropic composition |
```
</details>

---

### Step 6 [Q - L1_3 · c25]: `search_blocks`

<details><summary>Arguments</summary>

```json
{
  "compound": [
    "GLOBcomp_1",
    "GLOBcomp_6"
  ],
  "system_type": "binary",
  "literature": [
    "GLOBlit_11130",
    "GLOBlit_11142",
    "GLOBlit_11872",
    "GLOBlit_4959",
    "GLOBlit_4843"
  ],
  "limit": 50,
  "purpose": "Find remaining binary water+propan-2-ol blocks from DOIs not covered in first search",
  "tasks": "Get property details for blocks in these specific literature sources"
}
```
</details>

- **Result:** 1,077 chars  |  **Time:** 13.2s  |  **Started:** 05:49:22 (t+832.7s)
- **Subagent:** KEEP in 2,385 → 1,077 chars (13.0s)
  - Only 1 block found from the 5 queried literature sources. GLOBlit_11130 contains compressed/saturated liquid density data for water + propan-2-ol at fixed composition x(propan-2-ol) = 0.2483. The othe

<details><summary>Result</summary>

```
Only 1 block found from the 5 queried literature sources. GLOBlit_11130 contains compressed/saturated liquid density data for water + propan-2-ol at fixed composition x(propan-2-ol) = 0.2483. The other four sources (GLOBlit_11142, GLOBlit_11872, GLOBlit_4959, GLOBlit_4843) returned no binary blocks for this system.

| DOI | Block | lit_id | Property | Phase | Points | Composition | T range (K) | P range (kPa) |
|---|---|---|---|---|---|---|---|---|
| 10.1021/je8001305 | PROPblock_1 | GLOBlit_11130 | Mass density (kg/m³) | Liquid | 209 (50 shown, 22 kept RDP) | x(propan-2-ol)=0.2483 | 300.08–350.18 | 7.0–9562.3 |

**Block details:**

| Field | Value |
|---|---|
| Compounds | DOIcomp_1→GLOBcomp_1 (water), DOIcomp_2→GLOBcomp_6 (propan-2-ol) |
| Property | BLKprop_1 → GLOBprop_1, mass_density_kg_m3, GLOBmeas_2 (vibrating_tube_method) |
| Variables | BLKvar_1: mole_fraction (GLOBvar_2), BLKvar_2: temperature_k (GLOBvar_1), BLKvar_3: pressure_kpa (GLOBvar_3) |
| Uncertainty | k=95%, Propagation, compiler; ±U ≈ 0.86–0.91 kg/m³ |
| Density range | 850.19–900.79 kg/m³ |
```
</details>

---

## Tool Compaction Pipeline (22 calls)

| # | Tool | Pipeline | Native | Hardcoded | Agentic | Verdict | Native→Final | Section |
|--:|------|----------|-------:|----------:|--------:|---------|-------------:|---------|
| 1 | `resolve_compound_ids` | query | 567 | 285 | 190 | KEEP | −66% | L1_1 |
| 2 | `search_system_registry` | query | 281,385 | 10,570 | 1,151 | KEEP | −100% | L1_1 |
| 3 | `search_blocks` | query | 115,407 | 12,134 | 845 | KEEP | −99% | L1_1 |
| 4 | `search_blocks` | query | 19,108 | 5,619 | 1,330 | KEEP | −93% | L1_1 |
| 5 | `search_blocks` | query | 12,509 | 3,630 | 930 | KEEP | −93% | L1_1 |
| 6 | `search_blocks` | query | 11,437 | 3,466 | 1,137 | KEEP | −90% | L1_1 |
| 7 | `resolve_compound_ids` | query | 567 | 285 | 190 | KEEP | −66% | L1_2 |
| 8 | `search_system_registry` | query | 281,385 | 10,570 | 1,110 | KEEP | −100% | L1_2 |
| 9 | `search_blocks` | query | 288,748 | 30,354 | 1,347 | KEEP | −100% | L1_2 |
| 10 | `search_blocks` | query | 6,214 | 1,993 | 1,255 | KEEP | −80% | L1_2 |
| 11 | `search_blocks` | query | 6,766 | 2,069 | 1,041 | KEEP | −85% | L1_2 |
| 12 | `search_blocks` | query | 6,252 | 2,041 | 1,258 | KEEP | −80% | L1_2 |
| 13 | `search_blocks` | query | 5,963 | 1,947 | 1,363 | KEEP | −77% | L1_2 |
| 14 | `search_blocks` | query | 5,715 | 1,840 | 1,316 | KEEP | −77% | L1_2 |
| 15 | `search_blocks` | query | 4,684 | 1,327 | 736 | KEEP | −84% | L1_2 |
| 16 | `search_blocks` | query | 4,786 | 1,375 | 967 | KEEP | −80% | L1_2 |
| 17 | `search_blocks` | query | 5,992 | 1,952 | 1,268 | KEEP | −79% | L1_2 |
| 18 | `resolve_compound_ids` | query | 567 | 285 | 203 | KEEP | −64% | L1_3 |
| 19 | `search_blocks` | query | 288,748 | 30,354 | 1,313 | KEEP | −100% | L1_3 |
| 20 | `search_system_registry` | query | 281,385 | 10,570 | 1,137 | KEEP | −100% | L1_3 |
| 21 | `search_blocks` | query | 288,748 | 30,354 | 1,164 | KEEP | −100% | L1_3 |
| 22 | `search_blocks` | query | 6,494 | 2,385 | 1,077 | KEEP | −83% | L1_3 |

## Subagent Summary (23 events)

| Tool | Verdict | Input Chars | Output Chars | Time | Section |
|------|---------|-------------|-------------|------|---------|
| resolve_compound_ids | KEEP | 285 | 190 | 4.3s | L1_1 |
| search_system_registry | KEEP | 10,570 | 1,151 | 13.6s | L1_1 |
| search_blocks | OVERSIZED | 42,834 | 399 | 0.0s | L1_1 |
| search_blocks | KEEP | 12,134 | 845 | 14.8s | L1_1 |
| search_blocks | KEEP | 5,619 | 1,330 | 13.2s | L1_1 |
| search_blocks | KEEP | 3,630 | 930 | 12.6s | L1_1 |
| search_blocks | KEEP | 3,466 | 1,137 | 15.3s | L1_1 |
| resolve_compound_ids | KEEP | 285 | 190 | 4.2s | L1_2 |
| search_system_registry | KEEP | 10,570 | 1,110 | 14.0s | L1_2 |
| search_blocks | KEEP | 30,354 | 1,347 | 15.0s | L1_2 |
| search_blocks | KEEP | 1,993 | 1,255 | 12.3s | L1_2 |
| search_blocks | KEEP | 2,069 | 1,041 | 11.5s | L1_2 |
| search_blocks | KEEP | 2,041 | 1,258 | 11.1s | L1_2 |
| search_blocks | KEEP | 1,947 | 1,363 | 12.7s | L1_2 |
| search_blocks | KEEP | 1,840 | 1,316 | 10.6s | L1_2 |
| search_blocks | KEEP | 1,327 | 736 | 8.1s | L1_2 |
| search_blocks | KEEP | 1,375 | 967 | 8.8s | L1_2 |
| search_blocks | KEEP | 1,952 | 1,268 | 11.8s | L1_2 |
| resolve_compound_ids | KEEP | 285 | 203 | 4.1s | L1_3 |
| search_blocks | KEEP | 30,354 | 1,313 | 14.1s | L1_3 |
| search_system_registry | KEEP | 10,570 | 1,137 | 16.3s | L1_3 |
| search_blocks | KEEP | 30,354 | 1,164 | 15.6s | L1_3 |
| search_blocks | KEEP | 2,385 | 1,077 | 13.0s | L1_3 |

## Errors (3)

- **Step 4 · L1_1** `search_blocks` (exception): {
  "error": "Tool `search_blocks` result is too large for its mandatory subagent (~10,708 tokens / 42,834 chars after hardcoded compaction).**\n\n### Result Stats\n- **After compaction:** 42,834 char
- **Step 1** `L1_query` (exception): {
  "error": "query-L1 core-ID refinement exhausted 2 cycles: construct_core_blocks_found: core_blocks_found[1] checksum mismatch for (GLOBlit_1423, PROPblock_2): system_type expected 'unary', receive
- **Step 2** `L1_query` (exception): {
  "error": "query-L1 core-ID refinement exhausted 2 cycles: construct_core_blocks_found: core_blocks_found[9] checksum mismatch for (GLOBlit_2096, PROPblock_7): prop_num_ids expected ['GLOBprop_45']

---

**Total:** 26 tool calls  |  Tool time: 534.8s  |  Wall: 993.9s  |  **Status:** OK
