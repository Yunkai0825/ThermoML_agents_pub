# Reference Stats — query-agent

**Run started:** 2026-09-05 05:26:29
**Wall time (at last flush):** 538.4 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 41,617 | 82,904 | 14,932 | 124,521 | 13,835 | 99.2 | claudeopus46 |
| L1-worker | 44 | 572,359 | 407,792 | 60,338 | 980,151 | 22,276 | 459.9 | claudeopus46 |
| **TOTAL** | **53** | **613,976** | **490,696** | **75,270** | **1,104,672** | **20,842** | **559.1** | |

**Estimated tokens:** ~276,168 input + ~18,817 output = ~294,985 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 6 | 5 | 27 | 29 | 2,895 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 7 | 3 | 17 | 18 | 1,610 |
| `search_blocks` | 2 | 1 | 6 | 2 | 8 | 8 | 180 |
| `search_system_registry` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_system_registry` | 2 | 1 | 7 | 3 | 17 | 18 | 1,610 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **11** | **4** | **26** | **13** | **69** | **73** | **6,295** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_4 |  | resolve_compound_ids, search_blocks, search_system_registry |

#### References (36 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_220 |  | search_blocks |
| GLOBlit_1483 |  | search_blocks |
| GLOBlit_1742 |  | search_blocks, search_system_registry |
| GLOBlit_2092 |  | search_blocks, search_system_registry |
| GLOBlit_2432 |  | search_blocks, search_system_registry |
| GLOBlit_2732 |  | search_blocks |
| GLOBlit_2825 |  | search_blocks, search_system_registry |
| GLOBlit_3475 |  | search_blocks |
| GLOBlit_4415 |  | search_blocks |
| GLOBlit_5201 |  | search_blocks |
| GLOBlit_5473 |  | search_blocks |
| GLOBlit_7085 |  | search_blocks, search_system_registry |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7629 |  | search_blocks, search_system_registry |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_8050 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks, search_system_registry |
| GLOBlit_9006 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_10699 |  | search_blocks |
| GLOBlit_10866 |  | search_blocks, search_system_registry |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | search_blocks |
| GLOBlit_11459 |  | search_blocks |
| GLOBlit_11504 |  | search_blocks |
| GLOBlit_11792 |  | search_blocks |
| GLOBlit_385 |  | search_blocks, search_system_registry |
| GLOBlit_462 |  | search_blocks, search_system_registry |
| GLOBlit_895 |  | search_blocks, search_system_registry |
| GLOBlit_5533 |  | search_blocks, search_system_registry |
| GLOBlit_8155 |  | search_blocks, search_system_registry |
| GLOBlit_8254 |  | search_blocks, search_system_registry |
| GLOBlit_8424 |  | search_blocks, search_system_registry |
| GLOBlit_8869 |  | search_blocks, search_system_registry |
| GLOBlit_9571 |  | search_blocks, search_system_registry |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry |

#### Measurements (14 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_1497 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_236 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_203 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_212 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_1494 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_280 | Mass density, kg/m3 | search_blocks, search_system_registry |

#### Phases (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks, search_system_registry |
| GLOBphase_3 |  | search_blocks, search_system_registry |
| GLOBphase_10 |  | search_blocks, search_system_registry |

#### Variables (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBvar_15 | Mass ratio of solute to solvent | search_blocks, search_system_registry |
| GLOBvar_18 | Volume fraction | search_blocks, search_system_registry |

#### Solvents (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks, search_system_registry |
| GLOBsolvent_2 |  | search_blocks |
| GLOBsolvent_3 |  | search_blocks, search_system_registry |

#### Constraints (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_3 | Mole fraction | search_blocks, search_system_registry |
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks, search_system_registry |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_22 | Volume fraction | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | search_system_registry |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 3 |
| Unique References | 36 |
| Unique Properties | 1 |
| Unique Measurements | 14 |
| Unique Phases | 3 |
| Unique Variables | 7 |
| Unique Solvents | 3 |
| Unique Constraints | 5 |
| Unique Block_Types | 1 |
| Total DOIs | 36 |
| Unique parent blocks | 47 |
| Explicit block/subsystem targets | 47 |
| Subsystem targets | 0 |
| Target-matched data points | 6,295 |

---

## 3. DOI & Block References

**Unique DOIs:** 36  |  **Parent blocks:** 47  |  **Explicit targets:** 47  |  **Subsystems:** 0  |  **Target-matched datapoints:** 4,505

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | search_blocks |
| 10.1016/j.fluid.2006.05.007 | 1 | 45 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2006.12.005 | 2 | 10 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2010.10.005 | 1 | 34 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | search_blocks |
| 10.1016/j.fluid.2015.07.012 | 2 | 164 | binary | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.09.005 | 2 | 144 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2004.07.019 | 2 | 1,161 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2006.08.002 | 3 | 301 | binary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 2 | 76 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | search_blocks |
| 10.1016/j.jct.2015.06.024 | 1 | 40 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 244 | binary | search_blocks |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | search_blocks |
| 10.1016/j.jct.2019.05.013 | 1 | 12 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.6b01058 | 2 | 24 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | search_blocks |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00723 | 2 | 6 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | search_blocks |
| 10.1021/je020173z | 1 | 24 | binary | search_blocks |
| 10.1021/je0301500 | 1 | 5 | binary | search_blocks, search_system_registry |
| 10.1021/je034101z | 1 | 401 | binary | search_blocks, search_system_registry |
| 10.1021/je049691v | 1 | 180 | binary | search_blocks, search_system_registry |
| 10.1021/je0600810 | 1 | 9 | binary | search_blocks, search_system_registry |
| 10.1021/je0601098 | 2 | 24 | binary | search_blocks, search_system_registry |
| 10.1021/je060335h | 1 | 164 | binary | search_blocks |
| 10.1021/je2003622 | 1 | 16 | binary | search_blocks, search_system_registry |
| 10.1021/je4003515 | 1 | 23 | binary | search_blocks |
| 10.1021/je600565m | 1 | 18 | binary | search_blocks |
| 10.1021/je700300y | 2 | 168 | binary | search_blocks, search_system_registry |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks |
| 10.1021/je800150h | 1 | 108 | binary | search_blocks |
| 10.1021/je800942u | 1 | 18 | binary | search_blocks |
| 10.1021/je900064e | 1 | 10 | binary | search_blocks |
| 10.1021/je900743e | 1 | 15 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | — | search_blocks |
| 10.1016/j.fluid.2006.05.007 | PROPblock_1 | declared | 45 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2006.12.005 | PROPblock_3 | declared | 8 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2006.12.005 | PROPblock_4 | declared | 2 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2010.10.005 | PROPblock_1 | declared | 34 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_1 | declared | 80 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2015.07.012 | PROPblock_3 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_1 | declared | 72 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.fluid.2017.09.005 | PROPblock_3 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_2 | declared | 19 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_3 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_4 | declared | 278 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | — | search_blocks |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.jct.2019.05.013 | PROPblock_2 | declared | 12 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00723 | PROPblock_10 | declared | 3 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00723 | PROPblock_12 | declared | 3 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | — | search_blocks |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | — | search_blocks |
| 10.1021/je0301500 | PROPblock_13 | declared | 5 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | — | search_blocks |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | — | search_blocks |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | — | search_blocks |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | — | search_blocks |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | — | search_blocks |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | — | search_blocks |
| 10.1021/je800942u | PROPblock_6 | declared | 18 | binary | — | search_blocks |
| 10.1021/je900064e | PROPblock_6 | declared | 10 | binary | — | search_blocks |
| 10.1021/je900743e | PROPblock_3 | declared | 15 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve ethanol and… | 172 | KEEP ←in 278 | 172 | 4.2 |
| 2 | 3 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,111 | KEEP ←in 18,526 | 1096 | 16.1 |
| 3 | 4 | `inspect_block_table` | block_number=GLOBlit_220::PROPblock_2, purpose=Ins… | 367 | — | — | 0.3 |
| 4 | 5 | `inspect_block_table` | block_number=GLOBlit_220::PROPblock_2, purpose=Get… | 1,917 | — | — | 0.3 |
| 5 | 1 | `L1_query` | context=User wants to compare ethanol…, id_catalog… | 15,203 | — | — | 132.2 |
| 6 | 1 | `resolve_compound_ids` | purpose=Resolve methanol to its globa…, queries=me… | 241 | KEEP ←in 221 | 241 | 6.2 |
| 7 | 2 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=50, p… | 1,007 | KEEP ←in 11,575 | 989 | 16.6 |
| 8 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=50, p… | 305 | KEEP ←in 5,187 | 305 | 26.6 |
| 9 | 5 | `search_system_registry` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=20, p… | 1,088 | DISCARD ←in 39 | 1021 | 17.1 |
| 10 | 6 | `search_system_registry` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=50, p… | 1,253 | KEEP ←in 2,749 | 1047 | 18.4 |
| 11 | 7 | `inspect_block_table` | block_number=GLOBlit_2432::PROPblock_1, nearest=Te… | 285 | — | — | 0.0 |
| 12 | 8 | `inspect_block_table` | block_number=GLOBlit_2432::PROPblock_1, nearest={'… | 391 | — | — | 0.7 |
| 13 | 9 | `inspect_block_table` | block_number=GLOBlit_8254::PROPblock_4, purpose=In… | 3,534 | — | — | 0.3 |
| 14 | 10 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_10, nearest={… | 1,111 | — | — | 0.1 |
| 15 | 11 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_10, purpose=G… | 1,487 | — | — | 0.3 |
| 16 | 2 | `L1_query` | context=User wants to compare ethanol…, id_catalog… | 39,931 | — | — | 316.8 |
| | | **TOTAL (16 tools)** | | **69,403** | | **4,871** | **556.2** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 656 | 12,237 | 1,435 | 9.1 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,251 | 25,346 | 603 | 4.9 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,265 | 26,360 | 537 | 3.9 |
| 4 | L1-worker | claudeopus46 | 3,767 | 436 | 4,203 | 354 | 4.1 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,859 | 25,954 | 1,774 | 12.4 |
| 6 | L1-worker | claudeopus46 | 3,767 | 18,948 | 22,715 | 1,535 | 15.1 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,300 | 27,395 | 946 | 7.5 |
| 8 | L1-worker | claudeopus46 | 24,095 | 4,010 | 28,105 | 790 | 6.0 |
| 9 | L1-worker | claudeopus46 | 24,095 | 6,276 | 30,371 | 2,021 | 16.0 |
| 10 | L1-worker | claudeopus46 | 24,095 | 11,369 | 35,464 | 3,080 | 21.4 |
| 11 | L1-worker | claudeopus46 | 24,095 | 17,042 | 41,137 | 2,967 | 18.3 |
| 12 | L1-worker | claudeopus46 | 2,106 | 3,663 | 5,769 | 447 | 4.0 |
| 13 | L1-worker | claudeopus46 | 627 | 2,171 | 2,798 | 967 | 5.3 |
| 14 | L1-worker | claudeopus46 | 2,320 | 2,291 | 4,611 | 1,014 | 5.5 |
| 15 | L1-worker | claudeopus46 | 366 | 1,224 | 1,590 | 435 | 2.9 |
| 16 | L1-worker | claudeopus46 | 366 | 1,378 | 1,744 | 954 | 4.0 |
| 17 | L1-worker | claudeopus46 | 366 | 1,451 | 1,817 | 969 | 4.2 |
| 18 | L1-worker | claudeopus46 | 1,228 | 4,408 | 5,636 | 370 | 3.2 |
| 19 | L1-worker | claudeopus46 | 787 | 12,367 | 13,154 | 498 | 6.1 |
| 20 | L0-main | claudeopus46 | 11,581 | 14,814 | 26,395 | 1,867 | 14.8 |
| 21 | L1-worker | claudeopus46 | 24,095 | 7,492 | 31,587 | 651 | 6.1 |
| 22 | L1-worker | claudeopus46 | 3,767 | 398 | 4,165 | 411 | 5.9 |
| 23 | L1-worker | claudeopus46 | 24,095 | 7,972 | 32,067 | 689 | 5.7 |
| 24 | L1-worker | claudeopus46 | 3,767 | 12,014 | 15,781 | 1,586 | 15.5 |
| 25 | L1-worker | claudeopus46 | 24,095 | 9,294 | 33,389 | 1,477 | 10.2 |
| 26 | L1-worker | claudeopus46 | 24,095 | 10,107 | 34,202 | 1,033 | 6.4 |
| 27 | L1-worker | claudeopus46 | 3,767 | 5,701 | 9,468 | 1,790 | 19.9 |
| 28 | L1-worker | claudeopus46 | 24,095 | 10,412 | 34,507 | 1,777 | 12.3 |
| 29 | L1-worker | claudeopus46 | 3,767 | 655 | 4,422 | 1,580 | 11.5 |
| 30 | L1-worker | claudeopus46 | 24,095 | 11,880 | 35,975 | 1,022 | 6.4 |
| 31 | L1-worker | claudeopus46 | 3,767 | 3,224 | 6,991 | 1,531 | 11.6 |
| 32 | L1-worker | claudeopus46 | 24,095 | 13,479 | 37,574 | 1,129 | 8.7 |
| 33 | L1-worker | claudeopus46 | 24,095 | 14,141 | 38,236 | 691 | 6.1 |
| 34 | L1-worker | claudeopus46 | 24,095 | 14,861 | 38,956 | 1,553 | 14.6 |
| 35 | L1-worker | claudeopus46 | 24,095 | 18,743 | 42,838 | 1,233 | 11.9 |
| 36 | L1-worker | claudeopus46 | 24,095 | 20,245 | 44,340 | 756 | 6.8 |
| 37 | L1-worker | claudeopus46 | 24,095 | 22,094 | 46,189 | 7,837 | 50.9 |
| 38 | L1-worker | claudeopus46 | 24,062 | 29,900 | 53,962 | 3,624 | 28.6 |
| 39 | L1-worker | claudeopus46 | 24,062 | 34,481 | 58,543 | 2,935 | 23.6 |
| 40 | L1-worker | claudeopus46 | 2,106 | 8,964 | 11,070 | 1,220 | 8.7 |
| 41 | L1-worker | claudeopus46 | 2,320 | 7,043 | 9,363 | 1,083 | 10.4 |
| 42 | L1-worker | claudeopus46 | 366 | 1,997 | 2,363 | 713 | 4.0 |
| 43 | L1-worker | claudeopus46 | 627 | 6,923 | 7,550 | 1,342 | 13.6 |
| 44 | L1-worker | claudeopus46 | 366 | 1,520 | 1,886 | 1,048 | 4.1 |
| 45 | L1-worker | claudeopus46 | 1,228 | 10,285 | 11,513 | 713 | 4.2 |
| 46 | L1-worker | claudeopus46 | 787 | 28,258 | 29,045 | 653 | 7.4 |
| 47 | L0-main | claudeopus46 | 11,581 | 44,038 | 55,619 | 5,521 | 40.7 |
| 48 | L0-main | claudeopus46 | 2,106 | 4,601 | 6,707 | 812 | 7.5 |
| 49 | L0-main | claudeopus46 | 2,320 | 4,113 | 6,433 | 1,619 | 8.7 |
| 50 | L0-main | claudeopus46 | 366 | 1,361 | 1,727 | 906 | 4.0 |
| 51 | L0-main | claudeopus46 | 366 | 2,094 | 2,460 | 1,560 | 5.1 |
| 52 | L0-main | claudeopus46 | 560 | 4,882 | 5,442 | 187 | 2.4 |
| 53 | L0-main | claudeopus46 | 1,156 | 6,345 | 7,501 | 1,025 | 6.9 |

