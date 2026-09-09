# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:24:27
**Wall time (at last flush):** 1,108.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 31 | 527,072 | 1,036,377 | 74,008 | 1,563,449 | 50,433 | 525.1 | claudeopus46 |
| L1-worker | 67 | 906,438 | 378,201 | 72,090 | 1,284,639 | 19,173 | 580.6 | claudeopus46 |
| **TOTAL** | **98** | **1,433,510** | **1,414,578** | **146,098** | **2,848,088** | **29,062** | **1105.7** | |

**Estimated tokens:** ~712,022 input + ~36,524 output = ~748,546 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 1 | 3 | 3 | 204 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 2 | 1 | 3 | 3 | 0 |
| `resolve_compound_ids` | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 95 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 2 | 1 | 1 | 1 | 0 |
| `resolve_compound_ids` | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 2 | 5 | 5 | 193 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 8 | 10 | 6 | 5 | 13 | 20 | 454 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 1 | 2 | 1 | 1 | 0 |
| **TOTAL** | **39** | **16** | **18** | **13** | **27** | **34** | **946** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (22 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_47 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_268 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_3079 |  | resolve_compound_ids |
| GLOBcomp_3578 |  | resolve_compound_ids |
| GLOBcomp_671 |  | resolve_compound_ids |
| GLOBcomp_1519 |  | resolve_compound_ids |
| GLOBcomp_260 |  | resolve_compound_ids |
| GLOBcomp_1061 |  | resolve_compound_ids |
| GLOBcomp_2712 |  | resolve_compound_ids |
| GLOBcomp_8069 |  | resolve_compound_ids |
| GLOBcomp_18 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_2086 |  | resolve_compound_ids |
| GLOBcomp_342 |  | resolve_compound_ids |
| GLOBcomp_63 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_5038 |  | resolve_compound_ids |
| GLOBcomp_931 | 1-bromotricyclo[3.3.1.1(3,7)]decane | search_blocks |
| GLOBcomp_53 | 2-aminoacetic acid | search_blocks |
| GLOBcomp_74 | (S)-2-aminopropanoic acid | search_blocks |
| GLOBcomp_171 | L-serine | search_blocks |
| GLOBcomp_5517 | DL-alanyl-DL-valine | search_blocks |
| GLOBcomp_468 | L-methionine | search_blocks |

#### References (21 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_8238 |  | query_thermoml, search_blocks |
| GLOBlit_8242 |  | query_thermoml, search_blocks |
| GLOBlit_9372 |  | query_thermoml, search_blocks |
| GLOBlit_8676 |  | query_thermoml, search_blocks |
| GLOBlit_9342 |  | search_blocks |
| GLOBlit_9900 |  | search_blocks |
| GLOBlit_11030 |  | search_blocks |
| GLOBlit_11207 |  | search_blocks |
| GLOBlit_1540 |  | search_blocks |
| GLOBlit_1910 |  | search_blocks |
| GLOBlit_2584 |  | search_blocks |
| GLOBlit_2834 |  | search_blocks |
| GLOBlit_2871 |  | search_blocks |
| GLOBlit_3614 |  | search_blocks |
| GLOBlit_4166 |  | search_blocks |
| GLOBlit_5674 |  | search_blocks |
| GLOBlit_5806 |  | search_blocks |
| GLOBlit_5822 |  | search_blocks |
| GLOBlit_5958 |  | search_blocks |
| GLOBlit_6254 |  | search_blocks |
| GLOBlit_11285 |  | search_blocks |

#### Properties (11 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_42 | Relative permittivity at various frequencies | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBprop_28 | Excess molar volume, m3/mol | search_blocks |
| GLOBprop_44 | Relative permittivity at zero frequency | search_blocks |
| GLOBprop_15 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBprop_3 | Activity coefficient | search_blocks |
| GLOBprop_32 | Amount concentration (molarity), mol/dm3 | search_blocks |
| GLOBprop_27 | Henry's Law constant (mole fraction scale), kPa | search_blocks |

#### Measurements (15 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_4 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_567 | Relative permittivity at various frequencies | search_blocks |
| GLOBmeas_192 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_147 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_209 | Speed of sound, m/s | search_blocks |
| GLOBmeas_176 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_55 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_53 | Relative permittivity at zero frequency | search_blocks |
| GLOBmeas_88 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_13 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_144 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_511 | Activity coefficient | search_blocks |

#### Phases (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, search_blocks |
| GLOBphase_3 |  | search_blocks |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_6 | Solvent: Molality, mol/kg | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |

#### Constraints (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks |
| GLOBconstr_2 | Temperature, K | query_thermoml, search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_12 | Amount concentration (molarity), mol/dm3 | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_21 |  | search_blocks |
| GLOBsolvent_1 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 22 |
| Unique References | 21 |
| Unique Properties | 11 |
| Unique Measurements | 15 |
| Unique Phases | 2 |
| Unique Variables | 6 |
| Unique Constraints | 5 |
| Unique Block_Types | 1 |
| Unique Solvents | 2 |
| Total DOIs | 21 |
| Unique parent blocks | 29 |
| Explicit block/subsystem targets | 29 |
| Subsystem targets | 6 |
| Target-matched data points | 1,256 |

---

## 3. DOI & Block References

**Unique DOIs:** 21  |  **Parent blocks:** 29  |  **Explicit targets:** 29  |  **Subsystems:** 6  |  **Target-matched datapoints:** 946

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2014.08.026 | 2 | 9 | binary | search_blocks |
| 10.1016/j.fluid.2016.04.007 | 1 | 60 | binary | search_blocks |
| 10.1016/j.jct.2005.07.012 | 1 | 112 | binary | search_blocks |
| 10.1016/j.jct.2007.05.015 | 2 | 54 | binary | search_blocks |
| 10.1016/j.jct.2007.09.009 | 1 | 74 | binary | search_blocks |
| 10.1016/j.jct.2012.04.007 | 1 | 55 | binary | search_blocks |
| 10.1016/j.jct.2014.05.003 | 2 | 6 | binary | search_blocks |
| 10.1016/j.tca.2005.11.035 | 1 | 4 | binary | search_blocks |
| 10.1016/j.tca.2008.10.011 | 3 | 24 | binary | search_blocks |
| 10.1016/j.tca.2008.12.016 | 1 | 12 | binary | search_blocks |
| 10.1016/j.tca.2011.09.009 | 1 | 1 | binary | search_blocks |
| 10.1016/j.tca.2015.08.006 | 1 | 13 | binary | search_blocks |
| 10.1021/je034073k | 1 | 65 | binary | query_thermoml, search_blocks |
| 10.1021/je0340809 | 2 | 190 | binary | query_thermoml, search_blocks |
| 10.1021/je050209y | 1 | 11 | binary | query_thermoml, search_blocks |
| 10.1021/je1008813 | 1 | 16 | binary | search_blocks |
| 10.1021/je100967k | 1 | 44 | binary | query_thermoml, search_blocks |
| 10.1021/je300608v | 1 | 60 | binary | search_blocks |
| 10.1021/je700671t | 1 | 98 | binary | search_blocks |
| 10.1021/je800330d | 1 | 8 | binary | search_blocks |
| 10.1021/je800517r | 3 | 30 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2014.08.026 | PROPblock_7 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.08.026 | PROPblock_8 | declared | 5 | binary | — | search_blocks |
| 10.1016/j.fluid.2016.04.007 | PROPblock_4 | declared | 60 | binary | — | search_blocks |
| 10.1016/j.jct.2005.07.012 | PROPblock_10 | declared | 112 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.015 | PROPblock_19 | declared | 27 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.015 | PROPblock_20 | declared | 27 | binary | — | search_blocks |
| 10.1016/j.jct.2007.09.009 | PROPblock_7 | declared | 74 | binary | — | search_blocks |
| 10.1016/j.jct.2012.04.007 | PROPblock_5 | declared | 55 | binary | — | search_blocks |
| 10.1016/j.jct.2014.05.003 | PROPblock_3 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.jct.2014.05.003 | PROPblock_4 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.tca.2005.11.035 | PROPblock_2 | BLKsubsys_1 | 4 | binary | — | search_blocks |
| 10.1016/j.tca.2008.10.011 | PROPblock_4 | BLKsubsys_1 | 8 | binary | — | search_blocks |
| 10.1016/j.tca.2008.10.011 | PROPblock_5 | BLKsubsys_1 | 8 | binary | — | search_blocks |
| 10.1016/j.tca.2008.10.011 | PROPblock_6 | BLKsubsys_1 | 8 | binary | — | search_blocks |
| 10.1016/j.tca.2008.12.016 | PROPblock_5 | BLKsubsys_1 | 12 | binary | — | search_blocks |
| 10.1016/j.tca.2011.09.009 | PROPblock_3 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.tca.2015.08.006 | PROPblock_4 | BLKsubsys_1 | 13 | binary | — | search_blocks |
| 10.1021/je034073k | PROPblock_3 | declared | 65 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je0340809 | PROPblock_14 | declared | 95 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je0340809 | PROPblock_17 | declared | 95 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je050209y | PROPblock_9 | declared | 11 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je1008813 | PROPblock_3 | declared | 16 | binary | — | search_blocks |
| 10.1021/je100967k | PROPblock_17 | declared | 44 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je300608v | PROPblock_3 | declared | 60 | binary | — | search_blocks |
| 10.1021/je700671t | PROPblock_3 | declared | 98 | binary | — | search_blocks |
| 10.1021/je800330d | PROPblock_3 | declared | 8 | binary | — | search_blocks |
| 10.1021/je800517r | PROPblock_10 | declared | 10 | binary | — | search_blocks |
| 10.1021/je800517r | PROPblock_11 | declared | 10 | binary | — | search_blocks |
| 10.1021/je800517r | PROPblock_12 | declared | 10 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'NMP_water_viscosi… | 209 | — | — | 0.0 |
| 2 | 2 | `query_thermoml_parallel` | queries=[{'label': 'NMP_water_viscosi… | 132 | — | — | 0.0 |
| 3 | 3 | `query_thermoml_parallel` | queries=[{'label': 'NMP_water_viscosi… | 132 | — | — | 0.2 |
| 4 | 4 | `query_thermoml_parallel` | queries=[{'label': 'NMP_water_viscosi… | 132 | — | — | 0.0 |
| 5 | 5 | `query_thermoml_parallel` | queries=[{'label': 'NMP_water_viscosi… | 132 | — | — | 0.0 |
| 6 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve NMP and wat… | 225 | KEEP ←in 299 | 225 | 17.6 |
| 7 | 4 | `search_blocks` | compound=['GLOBcomp_47', 'GLOBcomp_1'], limit=50, … | 758 | KEEP ←in 7,956 | 758 | 27.3 |
| 8 | 6 | `inspect_block_table` | block_number=GLOBlit_8238::PROPblock_3, nearest=T=… | 249 | — | — | 0.0 |
| 9 | 7 | `inspect_block_table` | block_number=GLOBlit_8238::PROPblock_3, nearest={'… | 385 | — | — | 0.1 |
| 10 | 8 | `inspect_block_table` | block_number=GLOBlit_8238::PROPblock_3, nearest={'… | 1,156 | — | — | 0.2 |
| 11 | 9 | `inspect_block_table` | block_number=GLOBlit_8242::PROPblock_17, nearest={… | 928 | — | — | 0.1 |
| 12 | 10 | `inspect_block_table` | block_number=GLOBlit_9372::PROPblock_17, nearest={… | 1,036 | — | — | 0.1 |
| 13 | 6 | `query_thermoml` | instruction=Search for binary mixture vis…, purpos… | 29,322 | — | — | 178.5 |
| 14 | 2 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Resolve compound I… | 626 | KEEP ←in 994 | 626 | 11.4 |
| 15 | 3 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve water compo… | 167 | KEEP ←in 216 | 167 | 4.5 |
| 16 | 5 | `search_blocks` | compound=['GLOBcomp_268', 'GLOBcomp_1'], limit=20,… | 1,066 | KEEP ←in 3,243 | 1051 | 15.6 |
| 17 | 6 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_8242… | 368 | — | — | 0.8 |
| 18 | 7 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_8242… | 1,579 | — | — | 0.1 |
| 19 | 9 | `inspect_block_table` | block_number=GLOBlit_8242::PROPblock_14, nearest={… | 767 | — | — | 0.6 |
| 20 | 10 | `inspect_block_table` | block_number=GLOBlit_8242::PROPblock_14, nearest={… | 767 | — | — | 0.1 |
| 21 | 7 | `query_thermoml` | instruction=Search for binary mixture vis…, purpos… | 14,727 | — | — | 148.1 |
| 22 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 747 | KEEP ←in 591 | 747 | 12.7 |
| 23 | 3 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve water compo… | 156 | KEEP ←in 216 | 156 | 4.1 |
| 24 | 5 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1'], limit=20, … | 768 | KEEP ←in 7,112 | 753 | 24.5 |
| 25 | 6 | `search_blocks` | compound=['GLOBcomp_63', 'GLOBcomp_1'], limit=20, … | 963 | DISCARD ←in 39 | 905 | 18.7 |
| 26 | 7 | `search_blocks` | compound=['GLOBcomp_63', 'GLOBcomp_1'], limit=50, … | 1,036 | DISCARD ←in 39 | 978 | 17.8 |
| 27 | 8 | `search_blocks` | compound=['GLOBcomp_63', 'GLOBcomp_1'], limit=20, … | 1,128 | KEEP ←in 10,345 | 1038 | 24.5 |
| 28 | 9 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_8676,… | 1,354 | — | — | 0.1 |
| 29 | 8 | `query_thermoml` | instruction=Search for dynamic viscosity …, purpos… | 13,525 | — | — | 251.7 |
| 30 | 11 | `fit_multi_system` | purpose=Fit viscosity data for NMP+wa…, systems=[{… | 763 | — | — | 0.3 |
| 31 | 13 | `inspect_block` | block_number=PROPblock_3, doi=10.1021/je034073k, p… | 1,396 | — | — | 0.1 |
| 32 | 15 | `inspect_block` | block_number=PROPblock_14, doi=10.1021/je0340809, … | 1,351 | — | — | 0.1 |
| 33 | 17 | `get_pure_values` | block_number=PROPblock_3, doi=10.1021/je034073k, p… | 750 | — | — | 0.1 |
| 34 | 19 | `fit_multi_system` | purpose=Fit viscosity data for NMP+wa…, systems=[{… | 981 | — | — | 2.7 |
| 35 | 20 | `fit_multi_system` | purpose=Fit viscosity data for 2-pyrr…, systems=[{… | 1,146 | — | — | 2.8 |
| | | **TOTAL (35 tools)** | | **80,927** | | **7,404** | **765.5** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 462 | 22,980 | 3,448 | 17.6 |
| 2 | L0-main | claudeopus46 | 22,518 | 1,053 | 23,571 | 2,787 | 12.2 |
| 3 | L0-main | claudeopus46 | 22,518 | 1,494 | 24,012 | 2,442 | 11.7 |
| 4 | L0-main | claudeopus46 | 22,518 | 1,946 | 24,464 | 2,103 | 10.8 |
| 5 | L0-main | claudeopus46 | 22,518 | 2,363 | 24,881 | 1,933 | 9.5 |
| 6 | L0-main | claudeopus46 | 22,518 | 2,727 | 25,245 | 765 | 7.3 |
| 7 | L1-worker | claudeopus46 | 24,095 | 943 | 25,038 | 637 | 5.4 |
| 8 | L1-worker | claudeopus46 | 24,095 | 1,980 | 26,075 | 555 | 4.6 |
| 9 | L1-worker | claudeopus46 | 3,767 | 465 | 4,232 | 390 | 17.1 |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,604 | 25,699 | 784 | 6.3 |
| 11 | L1-worker | claudeopus46 | 24,095 | 2,317 | 26,412 | 599 | 7.5 |
| 12 | L1-worker | claudeopus46 | 3,767 | 8,408 | 12,175 | 1,633 | 20.7 |
| 13 | L1-worker | claudeopus46 | 24,095 | 3,037 | 27,132 | 2,325 | 14.4 |
| 14 | L1-worker | claudeopus46 | 24,095 | 8,221 | 32,316 | 531 | 4.8 |
| 15 | L1-worker | claudeopus46 | 24,095 | 8,740 | 32,835 | 565 | 6.0 |
| 16 | L1-worker | claudeopus46 | 24,095 | 9,394 | 33,489 | 650 | 4.9 |
| 17 | L1-worker | claudeopus46 | 24,095 | 10,868 | 34,963 | 586 | 5.4 |
| 18 | L1-worker | claudeopus46 | 24,095 | 12,104 | 36,199 | 416 | 3.2 |
| 19 | L1-worker | claudeopus46 | 24,095 | 13,421 | 37,516 | 2,231 | 16.6 |
| 20 | L1-worker | claudeopus46 | 24,095 | 18,946 | 43,041 | 2,325 | 16.6 |
| 21 | L1-worker | claudeopus46 | 2,106 | 4,999 | 7,105 | 1,206 | 6.5 |
| 22 | L1-worker | claudeopus46 | 2,320 | 3,935 | 6,255 | 1,386 | 9.2 |
| 23 | L1-worker | claudeopus46 | 627 | 3,815 | 4,442 | 1,171 | 10.1 |
| 24 | L1-worker | claudeopus46 | 366 | 1,983 | 2,349 | 956 | 5.6 |
| 25 | L1-worker | claudeopus46 | 366 | 1,823 | 2,189 | 1,336 | 5.2 |
| 26 | L1-worker | claudeopus46 | 1,228 | 6,561 | 7,789 | 1,034 | 10.8 |
| 27 | L1-worker | claudeopus46 | 787 | 27,770 | 28,557 | 774 | 8.1 |
| 28 | L0-main | claudeopus46 | 22,518 | 23,622 | 46,140 | 1,859 | 15.8 |
| 29 | L1-worker | claudeopus46 | 24,095 | 1,027 | 25,122 | 716 | 5.3 |
| 30 | L1-worker | claudeopus46 | 24,095 | 2,110 | 26,205 | 644 | 4.3 |
| 31 | L1-worker | claudeopus46 | 3,767 | 1,173 | 4,940 | 1,157 | 9.8 |
| 32 | L1-worker | claudeopus46 | 24,095 | 2,128 | 26,223 | 558 | 6.5 |
| 33 | L1-worker | claudeopus46 | 3,767 | 337 | 4,104 | 287 | 3.9 |
| 34 | L1-worker | claudeopus46 | 24,095 | 2,587 | 26,682 | 1,070 | 7.5 |
| 35 | L1-worker | claudeopus46 | 24,095 | 3,333 | 27,428 | 747 | 5.5 |
| 36 | L1-worker | claudeopus46 | 3,767 | 3,793 | 7,560 | 1,575 | 15.2 |
| 37 | L1-worker | claudeopus46 | 24,095 | 4,398 | 28,493 | 895 | 8.3 |
| 38 | L1-worker | claudeopus46 | 24,095 | 5,147 | 29,242 | 698 | 5.2 |
| 39 | L1-worker | claudeopus46 | 24,095 | 7,080 | 31,175 | 1,772 | 13.6 |
| 40 | L1-worker | claudeopus46 | 24,095 | 11,610 | 35,705 | 1,228 | 9.4 |
| 41 | L1-worker | claudeopus46 | 24,095 | 12,701 | 36,796 | 522 | 6.1 |
| 42 | L1-worker | claudeopus46 | 24,095 | 13,738 | 37,833 | 1,774 | 15.3 |
| 43 | L1-worker | claudeopus46 | 2,106 | 3,053 | 5,159 | 808 | 5.5 |
| 44 | L1-worker | claudeopus46 | 2,320 | 1,905 | 4,225 | 857 | 5.8 |
| 45 | L1-worker | claudeopus46 | 627 | 1,785 | 2,412 | 1,024 | 7.1 |
| 46 | L1-worker | claudeopus46 | 366 | 1,585 | 1,951 | 574 | 3.8 |
| 47 | L1-worker | claudeopus46 | 366 | 1,294 | 1,660 | 817 | 4.2 |
| 48 | L1-worker | claudeopus46 | 366 | 1,435 | 1,801 | 1,011 | 4.9 |
| 49 | L1-worker | claudeopus46 | 787 | 11,910 | 12,697 | 569 | 10.3 |
| 50 | L0-main | claudeopus46 | 22,518 | 37,018 | 59,536 | 1,911 | 16.0 |
| 51 | L1-worker | claudeopus46 | 24,095 | 1,120 | 25,215 | 719 | 5.9 |
| 52 | L1-worker | claudeopus46 | 24,095 | 2,171 | 26,266 | 553 | 5.6 |
| 53 | L1-worker | claudeopus46 | 3,767 | 747 | 4,514 | 1,614 | 11.3 |
| 54 | L1-worker | claudeopus46 | 24,095 | 2,282 | 26,377 | 383 | 4.6 |
| 55 | L1-worker | claudeopus46 | 3,767 | 339 | 4,106 | 275 | 3.9 |
| 56 | L1-worker | claudeopus46 | 24,095 | 2,668 | 26,763 | 940 | 7.1 |
| 57 | L1-worker | claudeopus46 | 24,095 | 3,431 | 27,526 | 659 | 5.2 |
| 58 | L1-worker | claudeopus46 | 3,767 | 7,578 | 11,345 | 1,628 | 17.7 |
| 59 | L1-worker | claudeopus46 | 24,095 | 4,168 | 28,263 | 740 | 6.0 |
| 60 | L1-worker | claudeopus46 | 3,767 | 560 | 4,327 | 1,380 | 11.0 |
| 61 | L1-worker | claudeopus46 | 24,095 | 5,449 | 29,544 | 811 | 6.3 |
| 62 | L1-worker | claudeopus46 | 3,767 | 532 | 4,299 | 1,653 | 12.3 |
| 63 | L1-worker | claudeopus46 | 24,095 | 6,837 | 30,932 | 695 | 5.9 |
| 64 | L1-worker | claudeopus46 | 3,767 | 10,702 | 14,469 | 1,644 | 14.8 |
| 65 | L1-worker | claudeopus46 | 24,095 | 8,329 | 32,424 | 946 | 9.0 |
| 66 | L1-worker | claudeopus46 | 24,095 | 10,048 | 34,143 | 3,137 | 21.2 |
| 67 | L1-worker | claudeopus46 | 24,095 | 16,592 | 40,687 | 3,941 | 28.0 |
| 68 | L1-worker | claudeopus46 | 24,095 | 23,356 | 47,451 | 3,379 | 21.1 |
| 69 | L1-worker | claudeopus46 | 2,106 | 3,781 | 5,887 | 786 | 5.1 |
| 70 | L1-worker | claudeopus46 | 2,320 | 2,540 | 4,860 | 844 | 5.3 |
| 71 | L1-worker | claudeopus46 | 627 | 2,420 | 3,047 | 971 | 6.5 |
| 72 | L1-worker | claudeopus46 | 366 | 1,563 | 1,929 | 578 | 3.2 |
| 73 | L1-worker | claudeopus46 | 366 | 1,281 | 1,647 | 809 | 3.7 |
| 74 | L1-worker | claudeopus46 | 366 | 1,382 | 1,748 | 958 | 5.2 |
| 75 | L1-worker | claudeopus46 | 787 | 12,862 | 13,649 | 654 | 8.2 |
| 76 | L0-main | claudeopus46 | 22,518 | 50,196 | 72,714 | 2,452 | 18.7 |
| 77 | L0-main | claudeopus46 | 22,518 | 51,004 | 73,522 | 1,433 | 12.6 |
| 78 | L0-main | claudeopus46 | 22,518 | 51,777 | 74,295 | 1,358 | 10.2 |
| 79 | L0-main | claudeopus46 | 22,518 | 52,118 | 74,636 | 797 | 7.1 |
| 80 | L0-main | claudeopus46 | 22,518 | 52,792 | 75,310 | 490 | 4.2 |
| 81 | L0-main | claudeopus46 | 22,518 | 54,705 | 77,223 | 721 | 6.1 |
| 82 | L0-main | claudeopus46 | 22,518 | 55,394 | 77,912 | 451 | 4.3 |
| 83 | L0-main | claudeopus46 | 22,518 | 57,042 | 79,560 | 2,253 | 16.8 |
| 84 | L0-main | claudeopus46 | 22,518 | 57,812 | 80,330 | 1,311 | 9.7 |
| 85 | L0-main | claudeopus46 | 22,518 | 58,780 | 81,298 | 2,586 | 22.3 |
| 86 | L0-main | claudeopus46 | 22,518 | 59,570 | 82,088 | 1,933 | 19.4 |
| 87 | L0-main | claudeopus46 | 22,518 | 61,841 | 84,359 | 2,730 | 20.8 |
| 88 | L0-main | claudeopus46 | 22,518 | 65,679 | 88,197 | 7,372 | 54.1 |
| 89 | L0-main | claudeopus46 | 22,518 | 79,071 | 101,589 | 10,232 | 76.0 |
| 90 | L0-main | claudeopus46 | 22,518 | 95,518 | 118,036 | 10,408 | 74.8 |
| 91 | L0-main | claudeopus46 | 2,106 | 11,411 | 13,517 | 632 | 5.2 |
| 92 | L0-main | claudeopus46 | 366 | 1,155 | 1,521 | 669 | 4.0 |
| 93 | L0-main | claudeopus46 | 2,320 | 10,834 | 13,154 | 1,659 | 16.2 |
| 94 | L0-main | claudeopus46 | 366 | 2,096 | 2,462 | 1,604 | 5.7 |
| 95 | L0-main | claudeopus46 | 560 | 12,539 | 13,099 | 406 | 3.2 |
| 96 | L0-main | claudeopus46 | 1,156 | 15,972 | 17,128 | 2,088 | 14.8 |
| 97 | L0-main | claudeopus46 | 366 | 2,781 | 3,147 | 2,076 | 7.3 |
| 98 | L0-main | claudeopus46 | 1,918 | 5,605 | 7,523 | 1,099 | 10.7 |

