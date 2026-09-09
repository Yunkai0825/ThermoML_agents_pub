# Reference Stats — query-agent

**Run started:** 2026-09-05 04:54:07
**Wall time (at last flush):** 212.4 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 30,036 | 39,945 | 9,771 | 69,981 | 8,747 | 66.5 | claudeopus46 |
| L1-worker | 15 | 182,771 | 93,750 | 19,754 | 276,521 | 18,434 | 142.0 | claudeopus46 |
| verdict | 1 | 972 | 7,321 | 1,099 | 8,293 | 8,293 | 11.1 | claudeopus46 |
| **TOTAL** | **24** | **213,779** | **141,016** | **30,624** | **354,795** | **14,783** | **219.6** | |

**Estimated tokens:** ~88,698 input + ~7,656 output = ~96,354 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 6 | 5 | 27 | 29 | 2,895 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **5** | **1** | **6** | **5** | **27** | **29** | **2,895** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_5494 |  | resolve_compound_ids |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |

#### References (27 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_220 |  | search_blocks |
| GLOBlit_1483 |  | search_blocks |
| GLOBlit_1742 |  | search_blocks |
| GLOBlit_2092 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_2732 |  | search_blocks |
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_3475 |  | search_blocks |
| GLOBlit_4415 |  | search_blocks |
| GLOBlit_5201 |  | search_blocks |
| GLOBlit_5473 |  | search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7629 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_8050 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9006 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_10699 |  | search_blocks |
| GLOBlit_10866 |  | search_blocks |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | search_blocks |
| GLOBlit_11459 |  | search_blocks |
| GLOBlit_11504 |  | search_blocks |
| GLOBlit_11792 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |

#### Measurements (11 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_1497 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_236 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_203 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_212 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |

#### Phases (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |
| GLOBphase_3 |  | search_blocks |
| GLOBphase_10 |  | search_blocks |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_15 | Mass ratio of solute to solvent | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_2 |  | search_blocks |

#### Constraints (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_22 | Volume fraction | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 3 |
| Unique References | 27 |
| Unique Properties | 1 |
| Unique Measurements | 11 |
| Unique Phases | 3 |
| Unique Variables | 6 |
| Unique Solvents | 2 |
| Unique Constraints | 5 |
| Total DOIs | 27 |
| Unique parent blocks | 29 |
| Explicit block/subsystem targets | 29 |
| Subsystem targets | 0 |
| Target-matched data points | 2,895 |

---

## 3. DOI & Block References

**Unique DOIs:** 27  |  **Parent blocks:** 29  |  **Explicit targets:** 29  |  **Subsystems:** 0  |  **Target-matched datapoints:** 2,895

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | search_blocks |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | search_blocks |
| 10.1016/j.fluid.2015.07.012 | 1 | 84 | binary | search_blocks |
| 10.1016/j.fluid.2017.09.005 | 1 | 72 | binary | search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 565 | binary | search_blocks |
| 10.1016/j.jct.2006.08.002 | 3 | 301 | binary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 1 | 37 | binary | search_blocks |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | search_blocks |
| 10.1016/j.jct.2015.06.024 | 1 | 40 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 244 | binary | search_blocks |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | search_blocks |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00723 | 1 | 3 | binary | search_blocks |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | search_blocks |
| 10.1021/je020173z | 1 | 24 | binary | search_blocks |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks |
| 10.1021/je060335h | 1 | 164 | binary | search_blocks |
| 10.1021/je4003515 | 1 | 23 | binary | search_blocks |
| 10.1021/je600565m | 1 | 18 | binary | search_blocks |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks |
| 10.1021/je800150h | 1 | 108 | binary | search_blocks |
| 10.1021/je800942u | 1 | 18 | binary | search_blocks |
| 10.1021/je900064e | 1 | 10 | binary | search_blocks |
| 10.1021/je900743e | 1 | 15 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_3 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_3 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_2 | declared | 19 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_3 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_4 | declared | 278 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | — | search_blocks |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | — | search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00723 | PROPblock_12 | declared | 3 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | — | search_blocks |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | — | search_blocks |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | — | search_blocks |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | — | search_blocks |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | — | search_blocks |
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
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve ethanol and… | 266 | KEEP ←in 351 | 266 | 5.5 |
| 2 | 3 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,103 | KEEP ←in 18,526 | 1088 | 28.9 |
| 3 | 4 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2092,… | 2,512 | — | — | 0.1 |
| 4 | 1 | `L1_query` | context=Ethanol is C2H5OH (CAS 64-17-…, id_catalog… | 21,161 | — | — | 144.3 |
| | | **TOTAL (4 tools)** | | **25,042** | | **1,354** | **178.8** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 1,215 | 12,796 | 1,646 | 9.8 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,371 | 25,466 | 709 | 5.7 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,404 | 26,499 | 545 | 3.9 |
| 4 | L1-worker | claudeopus46 | 3,767 | 510 | 4,277 | 545 | 4.5 |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,062 | 26,157 | 786 | 6.6 |
| 6 | L1-worker | claudeopus46 | 3,767 | 18,951 | 22,718 | 1,542 | 15.5 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,497 | 27,592 | 1,003 | 8.5 |
| 8 | L1-worker | claudeopus46 | 24,095 | 6,379 | 30,474 | 3,060 | 23.6 |
| 9 | L1-worker | claudeopus46 | 24,095 | 11,927 | 36,022 | 3,153 | 20.1 |
| 10 | L1-worker | claudeopus46 | 24,095 | 17,570 | 41,665 | 3,038 | 20.1 |
| 11 | L1-worker | claudeopus46 | 2,106 | 4,661 | 6,767 | 812 | 5.4 |
| 12 | L1-worker | claudeopus46 | 627 | 3,049 | 3,676 | 973 | 6.1 |
| 13 | L1-worker | claudeopus46 | 2,320 | 3,169 | 5,489 | 1,219 | 6.7 |
| 14 | L1-worker | claudeopus46 | 366 | 1,589 | 1,955 | 578 | 3.5 |
| 15 | L1-worker | claudeopus46 | 366 | 1,656 | 2,022 | 1,169 | 4.6 |
| 16 | L1-worker | claudeopus46 | 787 | 14,955 | 15,742 | 622 | 7.2 |
| 17 | L0-main | claudeopus46 | 11,581 | 19,009 | 30,590 | 3,453 | 25.7 |
| 18 | L0-main | claudeopus46 | 2,106 | 4,503 | 6,609 | 713 | 5.7 |
| 19 | L0-main | claudeopus46 | 2,320 | 3,456 | 5,776 | 1,348 | 8.0 |
| 20 | L0-main | claudeopus46 | 366 | 1,262 | 1,628 | 674 | 4.9 |
| 21 | L0-main | claudeopus46 | 366 | 1,823 | 2,189 | 1,299 | 5.1 |
| 22 | L0-main | claudeopus46 | 560 | 3,939 | 4,499 | 107 | 2.1 |
| 23 | L0-main | claudeopus46 | 1,156 | 4,738 | 5,894 | 531 | 5.2 |
| 24 | verdict | claudeopus46 | 972 | 7,321 | 8,293 | 1,099 | 11.1 |

