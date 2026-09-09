# Reference Stats — query-agent

**Run started:** 2026-09-05 05:43:22
**Wall time (at last flush):** 1,093.2 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 14 | 77,286 | 233,007 | 24,596 | 310,293 | 22,163 | 160.0 | claudeopus46 |
| L1-worker | 103 | 1,423,286 | 1,092,306 | 122,233 | 2,515,592 | 24,423 | 947.9 | claudeopus46 |
| **TOTAL** | **117** | **1,500,572** | **1,325,313** | **146,829** | **2,825,885** | **24,152** | **1107.9** | |

**Estimated tokens:** ~706,471 input + ~36,707 output = ~743,178 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 3 | 1 | 1 | 3 | 1 | 1 | 13 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 1 | 1 | 2 | 1 | 10 | 10 | 21 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 1 | 1 | 2 | 1 | 10 | 10 | 73 |
| `search_blocks` | 1 | 1 | 2 | 1 | 10 | 10 | 33 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 549 |
| `resolve_ids` | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 549 |
| `search_system_registry` | 2 | 1 | 3 | 1 | 5 | 5 | 471 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 2 | 2 | 2 | 81 |
| `search_blocks` | 2 | 1 | 6 | 2 | 10 | 10 | 1,361 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **19** | **12** | **27** | **15** | **70** | **70** | **3,151** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_18 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_4 |  | resolve_compound_ids, search_blocks |

#### Properties (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_28 |  | resolve_property_ids |
| GLOBprop_41 |  | resolve_property_ids |
| GLOBprop_15 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry |

#### References (51 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_5688 |  | search_blocks |
| GLOBlit_86 |  | search_blocks |
| GLOBlit_179 |  | search_blocks |
| GLOBlit_228 |  | search_blocks |
| GLOBlit_249 |  | search_blocks |
| GLOBlit_316 |  | search_blocks |
| GLOBlit_422 |  | search_blocks |
| GLOBlit_490 |  | search_blocks |
| GLOBlit_652 |  | search_blocks |
| GLOBlit_779 |  | search_blocks |
| GLOBlit_1259 |  | search_blocks |
| GLOBlit_14 |  | search_blocks |
| GLOBlit_306 |  | search_blocks |
| GLOBlit_389 |  | search_blocks |
| GLOBlit_555 |  | search_blocks |
| GLOBlit_560 |  | search_blocks |
| GLOBlit_604 |  | search_blocks |
| GLOBlit_645 |  | search_blocks |
| GLOBlit_725 |  | search_blocks |
| GLOBlit_1136 |  | search_blocks |
| GLOBlit_57 |  | search_blocks |
| GLOBlit_60 |  | search_blocks |
| GLOBlit_119 |  | search_blocks |
| GLOBlit_134 |  | search_blocks |
| GLOBlit_259 |  | search_blocks |
| GLOBlit_267 |  | search_blocks |
| GLOBlit_323 |  | search_blocks |
| GLOBlit_349 |  | search_blocks |
| GLOBlit_376 |  | search_blocks |
| GLOBlit_1540 |  | search_blocks |
| GLOBlit_2584 |  | search_blocks, search_system_registry |
| GLOBlit_2834 |  | search_blocks |
| GLOBlit_3614 |  | search_blocks, search_system_registry |
| GLOBlit_4166 |  | search_blocks |
| GLOBlit_4174 |  | search_blocks, search_system_registry |
| GLOBlit_4340 |  | search_blocks |
| GLOBlit_8676 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9855 |  | search_blocks, search_system_registry |
| GLOBlit_11030 |  | search_blocks, search_system_registry |
| GLOBlit_4125 |  | search_blocks |
| GLOBlit_10930 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_5533 |  | search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_8254 |  | search_blocks |
| GLOBlit_8424 |  | search_blocks |
| GLOBlit_8869 |  | search_blocks |
| GLOBlit_9571 |  | search_blocks |
| GLOBlit_10866 |  | search_blocks |

#### Measurements (13 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_25 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_179 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_167 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_147 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_280 | Mass density, kg/m3 | search_blocks |

#### Phases (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks, search_system_registry |
| GLOBphase_10 |  | search_blocks |

#### Solvents (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_3 |  | search_blocks |
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_4 |  | search_blocks |

#### Variables (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_8 | Solvent: Mole fraction | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | resolve_ids, search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_18 | Volume fraction | search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_3 | Mole fraction | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | search_system_registry |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 3 |
| Unique Properties | 4 |
| Unique References | 51 |
| Unique Measurements | 13 |
| Unique Phases | 2 |
| Unique Solvents | 3 |
| Unique Variables | 7 |
| Unique Constraints | 3 |
| Unique Block_Types | 1 |
| Total DOIs | 51 |
| Unique parent blocks | 54 |
| Explicit block/subsystem targets | 54 |
| Subsystem targets | 0 |
| Target-matched data points | 3,151 |

---

## 3. DOI & Block References

**Unique DOIs:** 51  |  **Parent blocks:** 54  |  **Explicit targets:** 54  |  **Subsystems:** 0  |  **Target-matched datapoints:** 2,131

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1007/s10765-005-8590-7 | 1 | 42 | unary | search_blocks |
| 10.1007/s10765-008-0395-z | 1 | 1 | unary | search_blocks |
| 10.1007/s10765-008-0444-7 | 1 | 3 | unary | search_blocks |
| 10.1007/s10765-009-0648-5 | 1 | 5 | unary | search_blocks |
| 10.1007/s10765-011-0989-8 | 1 | 7 | unary | search_blocks |
| 10.1007/s10765-011-1149-x | 1 | 9 | unary | search_blocks |
| 10.1007/s10765-016-2096-3 | 1 | 5 | unary | search_blocks |
| 10.1016/j.fluid.2004.12.004 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2005.03.014 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2005.04.003 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2005.05.012 | 1 | 3 | unary | search_blocks |
| 10.1016/j.fluid.2005.09.009 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2005.09.025 | 2 | 2 | unary | search_blocks |
| 10.1016/j.fluid.2005.10.022 | 1 | 6 | unary | search_blocks |
| 10.1016/j.fluid.2006.01.008 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2006.03.018 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2006.05.015 | 1 | 14 | unary | search_blocks |
| 10.1016/j.fluid.2006.08.018 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2007.02.026 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2007.07.066 | 1 | 5 | unary | search_blocks |
| 10.1016/j.fluid.2007.08.008 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2008.02.008 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2008.07.001 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2008.07.018 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2009.07.010 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2010.01.002 | 2 | 8 | unary | search_blocks |
| 10.1016/j.fluid.2012.07.032 | 1 | 3 | unary | search_blocks |
| 10.1016/j.fluid.2013.05.022 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2014.08.026 | 1 | 4 | binary | search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 596 | binary | search_blocks |
| 10.1016/j.jct.2005.07.012 | 1 | 128 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2007.05.004 | 1 | 39 | binary | search_blocks |
| 10.1016/j.jct.2007.05.015 | 1 | 40 | binary | search_blocks |
| 10.1016/j.jct.2012.04.007 | 1 | 55 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2014.02.021 | 1 | 26 | binary | search_blocks |
| 10.1016/j.jct.2014.05.003 | 1 | 3 | binary | search_blocks |
| 10.1016/j.jct.2014.05.013 | 1 | 18 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2015.03.012 | 1 | 6 | binary | search_blocks |
| 10.1016/j.jct.2019.05.013 | 1 | 12 | binary | search_blocks |
| 10.1016/j.tca.2006.02.028 | 1 | 13 | ternary | search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks |
| 10.1021/je034101z | 1 | 401 | binary | search_blocks |
| 10.1021/je049691v | 1 | 180 | binary | search_blocks |
| 10.1021/je050209y | 1 | 11 | binary | search_blocks |
| 10.1021/je0600810 | 1 | 9 | binary | search_blocks |
| 10.1021/je0601098 | 2 | 26 | binary | search_blocks |
| 10.1021/je2003622 | 1 | 16 | binary | search_blocks |
| 10.1021/je300358u | 1 | 60 | binary | search_blocks, search_system_registry |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks |
| 10.1021/je700430g | 1 | 55 | binary | search_blocks |
| 10.1021/je700671t | 1 | 210 | binary | search_blocks, search_system_registry |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1007/s10765-005-8590-7 | PROPblock_1 | declared | 42 | unary | — | search_blocks |
| 10.1007/s10765-008-0395-z | PROPblock_1 | declared | 1 | unary | — | search_blocks |
| 10.1007/s10765-008-0444-7 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1007/s10765-009-0648-5 | PROPblock_6 | declared | 5 | unary | — | search_blocks |
| 10.1007/s10765-011-0989-8 | PROPblock_6 | declared | 7 | unary | — | search_blocks |
| 10.1007/s10765-011-1149-x | PROPblock_2 | declared | 9 | unary | — | search_blocks |
| 10.1007/s10765-016-2096-3 | PROPblock_7 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.fluid.2004.12.004 | PROPblock_4 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.03.014 | PROPblock_4 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.04.003 | PROPblock_6 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.05.012 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.09.009 | PROPblock_6 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.09.025 | PROPblock_1 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.09.025 | PROPblock_4 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.10.022 | PROPblock_1 | declared | 6 | unary | — | search_blocks |
| 10.1016/j.fluid.2006.01.008 | PROPblock_6 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2006.03.018 | PROPblock_8 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2006.05.015 | PROPblock_1 | declared | 14 | unary | — | search_blocks |
| 10.1016/j.fluid.2006.08.018 | PROPblock_2 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2007.02.026 | PROPblock_2 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2007.07.066 | PROPblock_2 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.fluid.2007.08.008 | PROPblock_6 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2008.02.008 | PROPblock_38 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2008.07.001 | PROPblock_8 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2008.07.018 | PROPblock_2 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2009.07.010 | PROPblock_11 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2010.01.002 | PROPblock_18 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.fluid.2010.01.002 | PROPblock_6 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.fluid.2012.07.032 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.fluid.2013.05.022 | PROPblock_1 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2014.08.026 | PROPblock_5 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | — | search_blocks |
| 10.1016/j.jct.2005.07.012 | PROPblock_9 | declared | 128 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.015 | PROPblock_18 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2012.04.007 | PROPblock_3 | declared | 55 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2014.02.021 | PROPblock_6 | declared | 26 | binary | — | search_blocks |
| 10.1016/j.jct.2014.05.003 | PROPblock_1 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.jct.2014.05.013 | PROPblock_19 | declared | 18 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2015.03.012 | PROPblock_2 | declared | 6 | binary | — | search_blocks |
| 10.1016/j.jct.2019.05.013 | PROPblock_2 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.tca.2006.02.028 | PROPblock_4 | declared | 13 | ternary | — | search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | — | search_blocks |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | — | search_blocks |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | — | search_blocks |
| 10.1021/je050209y | PROPblock_10 | declared | 11 | binary | — | search_blocks |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_30 | declared | 14 | binary | — | search_blocks |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | — | search_blocks |
| 10.1021/je300358u | PROPblock_3 | declared | 60 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | — | search_blocks |
| 10.1021/je700430g | PROPblock_8 | declared | 55 | binary | — | search_blocks |
| 10.1021/je700671t | PROPblock_4 | declared | 210 | binary | 2 | search_blocks, search_system_registry |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 251 | KEEP ←in 356 | 251 | 4.2 |
| 2 | 3 | `resolve_property_ids` | limit=5, min_score=60, purpose=Find property IDs f… | 225 | KEEP ←in 309 | 225 | 3.8 |
| 3 | 5 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1',…, limit=50,… | 1,042 | DISCARD ←in 39 | 984 | 14.6 |
| 4 | 6 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1',…, limit=50,… | 1,224 | KEEP ←in 2,201 | 1209 | 22.3 |
| 5 | 8 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_5688,… | 1,408 | — | — | 0.1 |
| 6 | 1 | `L1_query` | context=User wants molar volume of eq…, id_catalog… | 12,929 | — | — | 136.5 |
| 7 | 3 | `search_blocks` | compound=GLOBcomp_18, limit=10, property=GLOBprop_… | 1,078 | KEEP ←in 5,567 | 1078 | 17.8 |
| 8 | 4 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_228, … | 249 | — | — | 0.0 |
| 9 | 5 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_228, … | 333 | — | — | 0.1 |
| 10 | 6 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_86, n… | 837 | — | — | 0.1 |
| 11 | 8 | `inspect_block_table` | block_number=GLOBlit_228::PROPblock_4, purpose=Gro… | 565 | — | — | 0.1 |
| 12 | 2 | `L1_query` | context=User needs pure component mol…, id_catalog… | 15,380 | — | — | 123.8 |
| 13 | 3 | `search_blocks` | compound=GLOBcomp_1, limit=10, property=GLOBprop_1… | 1,282 | KEEP ←in 5,726 | 1282 | 15.7 |
| 14 | 5 | `search_blocks` | compound=GLOBcomp_4, limit=10, property=GLOBprop_1… | 1,220 | KEEP ←in 5,576 | 1206 | 16.4 |
| 15 | 6 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_306, … | 261 | — | — | 0.0 |
| 16 | 7 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_306, … | 333 | — | — | 0.1 |
| 17 | 8 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_57, n… | 675 | — | — | 0.1 |
| 18 | 10 | `inspect_block_table` | block_number=GLOBlit_306::PROPblock_6, nearest={'c… | 650 | — | — | 0.1 |
| 19 | 3 | `L1_query` | context=Building an ideal molar volum…, id_catalog… | 13,511 | — | — | 127.1 |
| 20 | 2 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find the global pr… | 262 | KEEP ←in 227 | 262 | 5.2 |
| 21 | 4 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1'], limit=20, … | 935 | DISCARD ←in 39 | 877 | 9.3 |
| 22 | 5 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1'], limit=20, … | 253 | KEEP ←in 39 | 253 | 11.3 |
| 23 | 6 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1'], limit=20, … | 216 | KEEP ←in 7,027 | 216 | 19.9 |
| 24 | 7 | `resolve_ids` | entity_type=variable, limit=10, min_score=50, purp… | 275 | KEEP ←in 241 | 275 | 4.6 |
| 25 | 8 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1'], limit=15, … | 573 | KEEP ←in 7,027 | 573 | 21.4 |
| 26 | 9 | `search_system_registry` | compound=['GLOBcomp_18', 'GLOBcomp_1'], limit=20, … | 1,331 | KEEP ←in 4,300 | 1285 | 14.5 |
| 27 | 10 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_11030… | 375 | — | — | 0.1 |
| 28 | 11 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_11030… | 1,628 | — | — | 0.1 |
| 29 | 4 | `L1_query` | context=Building estimate for ternary…, id_catalog… | 15,927 | — | — | 290.9 |
| 30 | 2 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_4'], limit=20, … | 1,053 | KEEP ←in 4,193 | 1053 | 20.7 |
| 31 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=10, p… | 1,779 | KEEP ←in 6,527 | 1779 | 40.7 |
| 32 | 4 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_4125,… | 361 | — | — | 0.1 |
| 33 | 5 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_4125,… | 1,312 | — | — | 0.1 |
| 34 | 6 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 1,487 | — | — | 0.1 |
| 35 | 8 | `inspect_block_table` | block_number=GLOBlit_4125::PROPblock_6, nearest={'… | 1,038 | — | — | 0.8 |
| 36 | 5 | `L1_query` | context=Building estimate of molar vo…, id_catalog… | 25,596 | — | — | 264.9 |
| | | **TOTAL (36 tools)** | | **107,854** | | **12,808** | **1187.6** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 698 | 12,279 | 1,407 | 10.5 |
| 2 | L1-worker | claudeopus46 | 24,095 | 967 | 25,062 | 586 | 4.9 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,012 | 26,107 | 589 | 4.7 |
| 4 | L1-worker | claudeopus46 | 3,767 | 542 | 4,309 | 398 | 4.1 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,652 | 25,747 | 869 | 6.1 |
| 6 | L1-worker | claudeopus46 | 3,767 | 475 | 4,242 | 336 | 3.6 |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,198 | 26,293 | 1,125 | 7.7 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,032 | 27,127 | 787 | 6.0 |
| 9 | L1-worker | claudeopus46 | 3,767 | 674 | 4,441 | 1,233 | 8.9 |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,029 | 28,124 | 975 | 7.0 |
| 11 | L1-worker | claudeopus46 | 3,767 | 2,653 | 6,420 | 1,746 | 13.1 |
| 12 | L1-worker | claudeopus46 | 24,095 | 5,662 | 29,757 | 2,513 | 14.8 |
| 13 | L1-worker | claudeopus46 | 24,095 | 10,130 | 34,225 | 1,183 | 8.8 |
| 14 | L1-worker | claudeopus46 | 24,095 | 11,862 | 35,957 | 1,407 | 11.9 |
| 15 | L1-worker | claudeopus46 | 2,106 | 2,626 | 4,732 | 497 | 3.6 |
| 16 | L1-worker | claudeopus46 | 2,320 | 1,538 | 3,858 | 729 | 4.2 |
| 17 | L1-worker | claudeopus46 | 627 | 1,418 | 2,045 | 897 | 4.8 |
| 18 | L1-worker | claudeopus46 | 366 | 1,274 | 1,640 | 377 | 2.5 |
| 19 | L1-worker | claudeopus46 | 366 | 1,166 | 1,532 | 332 | 3.9 |
| 20 | L1-worker | claudeopus46 | 1,228 | 3,409 | 4,637 | 390 | 3.2 |
| 21 | L1-worker | claudeopus46 | 787 | 11,507 | 12,294 | 542 | 6.9 |
| 22 | L0-main | claudeopus46 | 11,581 | 10,243 | 21,824 | 1,243 | 9.8 |
| 23 | L1-worker | claudeopus46 | 24,095 | 4,552 | 28,647 | 739 | 7.3 |
| 24 | L1-worker | claudeopus46 | 24,095 | 5,636 | 29,731 | 603 | 4.1 |
| 25 | L1-worker | claudeopus46 | 24,095 | 6,305 | 30,400 | 666 | 4.2 |
| 26 | L1-worker | claudeopus46 | 3,767 | 5,965 | 9,732 | 1,432 | 12.6 |
| 27 | L1-worker | claudeopus46 | 24,095 | 6,445 | 30,540 | 1,016 | 8.4 |
| 28 | L1-worker | claudeopus46 | 24,095 | 7,046 | 31,141 | 675 | 5.4 |
| 29 | L1-worker | claudeopus46 | 24,095 | 7,760 | 31,855 | 1,267 | 9.3 |
| 30 | L1-worker | claudeopus46 | 24,095 | 8,990 | 33,085 | 1,278 | 10.7 |
| 31 | L1-worker | claudeopus46 | 24,095 | 14,480 | 38,575 | 1,197 | 12.3 |
| 32 | L1-worker | claudeopus46 | 24,095 | 15,375 | 39,470 | 1,392 | 11.9 |
| 33 | L1-worker | claudeopus46 | 24,095 | 20,238 | 44,333 | 1,506 | 12.8 |
| 34 | L1-worker | claudeopus46 | 627 | 3,170 | 3,797 | 881 | 6.0 |
| 35 | L1-worker | claudeopus46 | 2,320 | 3,290 | 5,610 | 844 | 6.6 |
| 36 | L1-worker | claudeopus46 | 2,106 | 4,430 | 6,536 | 1,027 | 7.3 |
| 37 | L1-worker | claudeopus46 | 366 | 1,281 | 1,647 | 804 | 3.9 |
| 38 | L1-worker | claudeopus46 | 366 | 1,804 | 2,170 | 561 | 3.5 |
| 39 | L1-worker | claudeopus46 | 787 | 17,080 | 17,867 | 739 | 6.1 |
| 40 | L0-main | claudeopus46 | 11,581 | 23,399 | 34,980 | 1,398 | 10.4 |
| 41 | L1-worker | claudeopus46 | 24,095 | 9,596 | 33,691 | 740 | 6.1 |
| 42 | L1-worker | claudeopus46 | 24,095 | 10,686 | 34,781 | 671 | 4.6 |
| 43 | L1-worker | claudeopus46 | 24,095 | 11,417 | 35,512 | 635 | 3.8 |
| 44 | L1-worker | claudeopus46 | 3,767 | 6,130 | 9,897 | 1,669 | 13.3 |
| 45 | L1-worker | claudeopus46 | 24,095 | 11,749 | 35,844 | 610 | 5.0 |
| 46 | L1-worker | claudeopus46 | 24,095 | 12,449 | 36,544 | 596 | 4.9 |
| 47 | L1-worker | claudeopus46 | 3,767 | 5,984 | 9,751 | 1,605 | 12.2 |
| 48 | L1-worker | claudeopus46 | 24,095 | 13,613 | 37,708 | 844 | 7.4 |
| 49 | L1-worker | claudeopus46 | 24,095 | 14,229 | 38,324 | 565 | 5.2 |
| 50 | L1-worker | claudeopus46 | 24,095 | 14,862 | 38,957 | 766 | 6.4 |
| 51 | L1-worker | claudeopus46 | 24,095 | 15,880 | 39,975 | 1,252 | 9.6 |
| 52 | L1-worker | claudeopus46 | 24,095 | 20,179 | 44,274 | 845 | 7.4 |
| 53 | L1-worker | claudeopus46 | 24,095 | 21,182 | 45,277 | 1,090 | 9.6 |
| 54 | L1-worker | claudeopus46 | 24,095 | 24,530 | 48,625 | 1,090 | 6.0 |
| 55 | L1-worker | claudeopus46 | 2,106 | 3,059 | 5,165 | 1,004 | 5.5 |
| 56 | L1-worker | claudeopus46 | 2,320 | 1,710 | 4,030 | 915 | 5.6 |
| 57 | L1-worker | claudeopus46 | 627 | 1,590 | 2,217 | 845 | 5.9 |
| 58 | L1-worker | claudeopus46 | 366 | 1,781 | 2,147 | 538 | 3.2 |
| 59 | L1-worker | claudeopus46 | 366 | 1,352 | 1,718 | 875 | 3.9 |
| 60 | L1-worker | claudeopus46 | 787 | 13,978 | 14,765 | 634 | 6.8 |
| 61 | L0-main | claudeopus46 | 11,581 | 34,077 | 45,658 | 2,228 | 16.9 |
| 62 | L1-worker | claudeopus46 | 24,095 | 13,816 | 37,911 | 815 | 6.2 |
| 63 | L1-worker | claudeopus46 | 24,095 | 14,857 | 38,952 | 583 | 4.8 |
| 64 | L1-worker | claudeopus46 | 3,767 | 391 | 4,158 | 366 | 4.7 |
| 65 | L1-worker | claudeopus46 | 24,095 | 14,523 | 38,618 | 749 | 9.8 |
| 66 | L1-worker | claudeopus46 | 24,095 | 15,225 | 39,320 | 673 | 4.9 |
| 67 | L1-worker | claudeopus46 | 3,767 | 591 | 4,358 | 1,128 | 8.9 |
| 68 | L1-worker | claudeopus46 | 24,095 | 16,133 | 40,228 | 886 | 12.8 |
| 69 | L1-worker | claudeopus46 | 3,767 | 530 | 4,297 | 577 | 4.7 |
| 70 | L1-worker | claudeopus46 | 24,095 | 16,741 | 40,836 | 783 | 6.0 |
| 71 | L1-worker | claudeopus46 | 3,767 | 7,517 | 11,284 | 1,790 | 13.9 |
| 72 | L1-worker | claudeopus46 | 24,095 | 17,286 | 41,381 | 1,850 | 13.6 |
| 73 | L1-worker | claudeopus46 | 3,767 | 430 | 4,197 | 445 | 4.4 |
| 74 | L1-worker | claudeopus46 | 24,095 | 17,991 | 42,086 | 1,435 | 12.0 |
| 75 | L1-worker | claudeopus46 | 3,767 | 7,491 | 11,258 | 1,860 | 15.2 |
| 76 | L1-worker | claudeopus46 | 24,095 | 18,964 | 43,059 | 843 | 6.5 |
| 77 | L1-worker | claudeopus46 | 3,767 | 4,837 | 8,604 | 1,613 | 14.0 |
| 78 | L1-worker | claudeopus46 | 24,095 | 20,645 | 44,740 | 1,441 | 11.5 |
| 79 | L1-worker | claudeopus46 | 24,095 | 21,477 | 45,572 | 689 | 5.5 |
| 80 | L1-worker | claudeopus46 | 24,095 | 23,425 | 47,520 | 4,598 | 34.5 |
| 81 | L1-worker | claudeopus46 | 24,062 | 18,936 | 42,998 | 3,022 | 25.6 |
| 82 | L1-worker | claudeopus46 | 24,062 | 20,968 | 45,030 | 3,056 | 25.8 |
| 83 | L1-worker | claudeopus46 | 2,106 | 5,558 | 7,664 | 689 | 7.7 |
| 84 | L1-worker | claudeopus46 | 2,320 | 4,024 | 6,344 | 1,298 | 8.2 |
| 85 | L1-worker | claudeopus46 | 627 | 3,904 | 4,531 | 1,092 | 8.2 |
| 86 | L1-worker | claudeopus46 | 366 | 1,466 | 1,832 | 430 | 3.2 |
| 87 | L1-worker | claudeopus46 | 366 | 1,735 | 2,101 | 1,248 | 4.8 |
| 88 | L1-worker | claudeopus46 | 787 | 16,186 | 16,973 | 663 | 8.0 |
| 89 | L0-main | claudeopus46 | 11,581 | 51,183 | 62,764 | 2,777 | 22.7 |
| 90 | L1-worker | claudeopus46 | 24,095 | 20,922 | 45,017 | 820 | 8.3 |
| 91 | L1-worker | claudeopus46 | 24,095 | 21,654 | 45,749 | 644 | 5.0 |
| 92 | L1-worker | claudeopus46 | 3,767 | 4,645 | 8,412 | 1,491 | 14.5 |
| 93 | L1-worker | claudeopus46 | 24,095 | 22,664 | 46,759 | 843 | 6.6 |
| 94 | L1-worker | claudeopus46 | 3,767 | 6,983 | 10,750 | 1,480 | 14.5 |
| 95 | L1-worker | claudeopus46 | 3,767 | 7,285 | 11,052 | 2,251 | 18.8 |
| 96 | L1-worker | claudeopus46 | 24,095 | 24,821 | 48,916 | 959 | 7.5 |
| 97 | L1-worker | claudeopus46 | 24,095 | 25,571 | 49,666 | 628 | 5.7 |
| 98 | L1-worker | claudeopus46 | 24,095 | 27,179 | 51,274 | 1,127 | 9.5 |
| 99 | L1-worker | claudeopus46 | 24,095 | 29,045 | 53,140 | 5,935 | 39.8 |
| 100 | L1-worker | claudeopus46 | 24,095 | 39,641 | 63,736 | 1,993 | 16.2 |
| 101 | L1-worker | claudeopus46 | 24,095 | 41,120 | 65,215 | 4,441 | 32.2 |
| 102 | L1-worker | claudeopus46 | 24,095 | 50,257 | 74,352 | 7,072 | 48.1 |
| 103 | L1-worker | claudeopus46 | 2,106 | 7,143 | 9,249 | 1,189 | 7.2 |
| 104 | L1-worker | claudeopus46 | 2,320 | 5,530 | 7,850 | 1,159 | 7.5 |
| 105 | L1-worker | claudeopus46 | 627 | 5,410 | 6,037 | 1,031 | 8.1 |
| 106 | L1-worker | claudeopus46 | 366 | 1,966 | 2,332 | 703 | 4.0 |
| 107 | L1-worker | claudeopus46 | 366 | 1,596 | 1,962 | 1,114 | 4.8 |
| 108 | L1-worker | claudeopus46 | 787 | 24,598 | 25,385 | 804 | 8.7 |
| 109 | L0-main | claudeopus46 | 11,581 | 74,415 | 85,996 | 4,339 | 32.4 |
| 110 | L0-main | claudeopus46 | 2,320 | 4,507 | 6,827 | 1,348 | 8.0 |
| 111 | L0-main | claudeopus46 | 2,106 | 5,037 | 7,143 | 1,329 | 9.5 |
| 112 | L0-main | claudeopus46 | 366 | 1,823 | 2,189 | 1,294 | 4.6 |
| 113 | L0-main | claudeopus46 | 366 | 1,878 | 2,244 | 1,709 | 7.0 |
| 114 | L0-main | claudeopus46 | 560 | 6,689 | 7,249 | 587 | 4.1 |
| 115 | L0-main | claudeopus46 | 560 | 5,561 | 6,121 | 523 | 3.6 |
| 116 | L0-main | claudeopus46 | 1,156 | 10,413 | 11,569 | 2,391 | 13.3 |
| 117 | L0-main | claudeopus46 | 366 | 3,084 | 3,450 | 2,023 | 7.2 |

