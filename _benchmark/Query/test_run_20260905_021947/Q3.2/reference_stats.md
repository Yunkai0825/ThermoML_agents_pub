# Reference Stats — query-agent

**Run started:** 2026-09-05 05:32:51
**Wall time (at last flush):** 620.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 10 | 41,983 | 120,360 | 18,698 | 162,343 | 16,234 | 116.3 | claudeopus46 |
| L1-worker | 44 | 618,955 | 553,692 | 70,037 | 1,172,647 | 26,651 | 523.9 | claudeopus46 |
| **TOTAL** | **54** | **660,938** | **674,052** | **88,735** | **1,334,990** | **24,722** | **640.2** | |

**Estimated tokens:** ~333,747 input + ~22,183 output = ~355,930 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_system_summary` | 2 | 0 | 0 | 0 | 73 | 126 | 5,163 |
| `search_blocks` | 2 | 1 | 1 | 1 | 1 | 1 | 2 |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 278 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 1 | 8 | 10 | 172 |
| `search_blocks` | 2 | 1 | 3 | 2 | 4 | 6 | 23 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 2 | 4 | 6 | 23 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **14** | **5** | **12** | **6** | **91** | **150** | **5,661** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks, search_system_summary |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_summary |

#### References (31 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_220 |  | search_system_summary |
| GLOBlit_2432 |  | search_system_summary |
| GLOBlit_5201 |  | search_system_summary |
| GLOBlit_2732 |  | search_blocks, search_system_summary |
| GLOBlit_11136 |  | search_system_summary |
| GLOBlit_1742 |  | search_system_summary |
| GLOBlit_9006 |  | search_system_summary |
| GLOBlit_11574 |  | search_system_summary |
| GLOBlit_1197 |  | search_system_summary |
| GLOBlit_2092 |  | search_system_summary |
| GLOBlit_1483 |  | search_system_summary |
| GLOBlit_977 |  | search_blocks, search_system_summary |
| GLOBlit_10866 |  | search_system_summary |
| GLOBlit_4415 |  | search_system_summary |
| GLOBlit_2825 |  | search_system_summary |
| GLOBlit_3475 |  | search_system_summary |
| GLOBlit_7748 |  | search_system_summary |
| GLOBlit_10024 |  | search_system_summary |
| GLOBlit_1482 |  | search_system_summary |
| GLOBlit_8830 |  | search_system_summary |
| GLOBlit_299 |  | search_blocks |
| GLOBlit_742 |  | search_blocks |
| GLOBlit_757 |  | search_blocks |
| GLOBlit_1518 |  | search_blocks |
| GLOBlit_2035 |  | search_blocks |
| GLOBlit_2220 |  | search_blocks |
| GLOBlit_3971 |  | search_blocks |
| GLOBlit_5073 |  | search_blocks |
| GLOBlit_1971 |  | search_blocks |
| GLOBlit_8381 |  | search_blocks |
| GLOBlit_8511 |  | search_blocks |

#### Properties (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_3 | Activity coefficient | search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_14 | Boiling temperature at pressure P, K | search_blocks |

#### Measurements (11 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_543 | Activity coefficient | search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_5 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_1362 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_2137 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_1355 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_133 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_1045 | Activity coefficient | search_blocks |
| GLOBmeas_1042 | Activity coefficient | search_blocks |
| GLOBmeas_1153 | Activity coefficient | search_blocks |
| GLOBmeas_1 | Activity coefficient | search_blocks |

#### Phases (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |
| GLOBphase_10 |  | search_blocks |
| GLOBphase_3 |  | search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 31 |
| Unique Properties | 3 |
| Unique Measurements | 11 |
| Unique Phases | 3 |
| Unique Variables | 3 |
| Unique Constraints | 2 |
| Total DOIs | 13 |
| Unique parent blocks | 17 |
| Explicit block/subsystem targets | 17 |
| Subsystem targets | 0 |
| Target-matched data points | 498 |

---

## 3. DOI & Block References

**Unique DOIs:** 13  |  **Parent blocks:** 17  |  **Explicit targets:** 17  |  **Subsystems:** 0  |  **Target-matched datapoints:** 473

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2005.08.018 | 3 | 13 | binary | search_blocks |
| 10.1016/j.fluid.2009.10.002 | 2 | 10 | binary | search_blocks |
| 10.1016/j.fluid.2009.11.014 | 2 | 36 | binary | search_blocks |
| 10.1016/j.fluid.2011.06.009 | 1 | 45 | binary | search_blocks |
| 10.1016/j.fluid.2014.07.022 | 1 | 7 | binary | search_blocks |
| 10.1016/j.fluid.2016.08.030 | 1 | 4 | binary | search_blocks |
| 10.1016/j.fluid.2017.03.010 | 1 | 17 | binary | search_blocks |
| 10.1016/j.fluid.2018.07.014 | 1 | 17 | binary | search_blocks |
| 10.1016/j.jct.2006.08.002 | 1 | 278 | binary | search_blocks |
| 10.1016/j.jct.2013.08.020 | 1 | 16 | binary | search_blocks |
| 10.1016/j.jct.2017.07.021 | 1 | 24 | binary | search_blocks |
| 10.1021/je0495942 | 1 | 1 | binary | search_blocks |
| 10.1021/je049875+ | 1 | 5 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2005.08.018 | PROPblock_4 | declared | 2 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.08.018 | PROPblock_5 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.08.018 | PROPblock_6 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.fluid.2009.10.002 | PROPblock_17 | declared | 5 | binary | — | search_blocks |
| 10.1016/j.fluid.2009.10.002 | PROPblock_18 | declared | 5 | binary | — | search_blocks |
| 10.1016/j.fluid.2009.11.014 | PROPblock_2 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.fluid.2009.11.014 | PROPblock_3 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.fluid.2011.06.009 | PROPblock_1 | declared | 45 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.07.022 | PROPblock_1 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.fluid.2016.08.030 | PROPblock_1 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.03.010 | PROPblock_7 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.fluid.2018.07.014 | PROPblock_4 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.002 | PROPblock_4 | declared | 278 | binary | — | search_blocks |
| 10.1016/j.jct.2013.08.020 | PROPblock_9 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2017.07.021 | PROPblock_4 | declared | 24 | binary | — | search_blocks |
| 10.1021/je0495942 | PROPblock_1 | declared | 1 | binary | — | search_blocks |
| 10.1021/je049875+ | PROPblock_1 | declared | 5 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve ethanol and… | 161 | KEEP ←in 276 | 161 | 4.2 |
| 2 | 3 | `search_system_summary` | compound=['GLOBcomp_2', 'GLOBcomp_1'], purpose=Fin… | 1,103 | KEEP ←in 1,118 | 1103 | 13.1 |
| 3 | 4 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=10, p… | 1,244 | KEEP ←in 1,656 | 1230 | 18.3 |
| 4 | 5 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=10, p… | 1,075 | KEEP ←in 3,032 | 1060 | 26.7 |
| 5 | 6 | `inspect_block_table` | block_number=GLOBlit_2732::PROPblock_4, purpose=Co… | 360 | — | — | 0.1 |
| 6 | 7 | `inspect_block_table` | block_number=GLOBlit_2732::PROPblock_4, purpose=Co… | 2,222 | — | — | 0.7 |
| 7 | 8 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=10, p… | 1,280 | KEEP ←in 6,142 | 1262 | 21.2 |
| 8 | 9 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=20, p… | 1,251 | KEEP ←in 9,635 | 1251 | 15.1 |
| 9 | 11 | `inspect_block_table` | block_number=GLOBlit_299::PROPblock_4, purpose=Gro… | 672 | — | — | 0.9 |
| 10 | 12 | `inspect_block_table` | block_number=GLOBlit_977::PROPblock_1, purpose=Gro… | 2,280 | — | — | 0.1 |
| 11 | 1 | `L1_query` | context=User is building an activity-…, id_catalog… | 41,893 | — | — | 324.3 |
| 12 | 1 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,313 | KEEP ←in 9,635 | 1299 | 20.9 |
| 13 | 2 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_299, … | 831 | — | — | 0.2 |
| 14 | 3 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_299, … | 922 | — | — | 0.1 |
| 15 | 4 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_1971,… | 945 | — | — | 0.1 |
| 16 | 5 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_8511,… | 996 | — | — | 0.2 |
| 17 | 6 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_8381,… | 638 | — | — | 0.1 |
| 18 | 8 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_299, … | 672 | — | — | 0.1 |
| 19 | 2 | `L1_query` | context=Previous query found activity…, id_catalog… | 48,607 | — | — | 191.5 |
| | | **TOTAL (19 tools)** | | **108,465** | | **7,366** | **637.9** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 692 | 12,273 | 1,997 | 11.8 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,360 | 25,455 | 522 | 4.3 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,393 | 26,488 | 550 | 3.6 |
| 4 | L1-worker | claudeopus46 | 3,767 | 435 | 4,202 | 295 | 3.4 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,951 | 26,046 | 977 | 7.0 |
| 6 | L1-worker | claudeopus46 | 3,767 | 1,579 | 5,346 | 1,457 | 8.4 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,373 | 27,468 | 915 | 6.5 |
| 8 | L1-worker | claudeopus46 | 3,767 | 2,084 | 5,851 | 1,676 | 11.5 |
| 9 | L1-worker | claudeopus46 | 24,095 | 5,029 | 29,124 | 724 | 7.0 |
| 10 | L1-worker | claudeopus46 | 3,767 | 3,464 | 7,231 | 2,149 | 21.5 |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,481 | 30,576 | 1,176 | 8.9 |
| 12 | L1-worker | claudeopus46 | 24,095 | 7,180 | 31,275 | 577 | 7.3 |
| 13 | L1-worker | claudeopus46 | 24,095 | 9,730 | 33,825 | 1,366 | 11.5 |
| 14 | L1-worker | claudeopus46 | 3,767 | 6,576 | 10,343 | 1,670 | 13.4 |
| 15 | L1-worker | claudeopus46 | 24,095 | 11,529 | 35,624 | 767 | 5.5 |
| 16 | L1-worker | claudeopus46 | 3,767 | 10,023 | 13,790 | 1,586 | 14.2 |
| 17 | L1-worker | claudeopus46 | 24,095 | 13,138 | 37,233 | 5,240 | 36.6 |
| 18 | L1-worker | claudeopus46 | 24,095 | 24,394 | 48,489 | 1,173 | 9.7 |
| 19 | L1-worker | claudeopus46 | 24,095 | 25,407 | 49,502 | 1,124 | 9.7 |
| 20 | L1-worker | claudeopus46 | 24,062 | 27,686 | 51,748 | 4,038 | 33.2 |
| 21 | L1-worker | claudeopus46 | 24,062 | 31,958 | 56,020 | 4,820 | 39.5 |
| 22 | L1-worker | claudeopus46 | 2,106 | 7,412 | 9,518 | 1,709 | 9.4 |
| 23 | L1-worker | claudeopus46 | 627 | 5,811 | 6,438 | 1,406 | 11.9 |
| 24 | L1-worker | claudeopus46 | 2,320 | 5,931 | 8,251 | 1,718 | 12.1 |
| 25 | L1-worker | claudeopus46 | 366 | 2,486 | 2,852 | 964 | 4.4 |
| 26 | L1-worker | claudeopus46 | 366 | 2,155 | 2,521 | 1,663 | 5.3 |
| 27 | L1-worker | claudeopus46 | 1,228 | 9,081 | 10,309 | 976 | 4.7 |
| 28 | L1-worker | claudeopus46 | 787 | 31,765 | 32,552 | 687 | 7.5 |
| 29 | L0-main | claudeopus46 | 11,581 | 30,252 | 41,833 | 2,439 | 18.9 |
| 30 | L1-worker | claudeopus46 | 24,095 | 11,903 | 35,998 | 862 | 5.9 |
| 31 | L1-worker | claudeopus46 | 3,767 | 10,061 | 13,828 | 1,686 | 13.2 |
| 32 | L1-worker | claudeopus46 | 24,095 | 13,553 | 37,648 | 1,123 | 10.1 |
| 33 | L1-worker | claudeopus46 | 24,095 | 14,764 | 38,859 | 827 | 7.9 |
| 34 | L1-worker | claudeopus46 | 24,095 | 16,077 | 40,172 | 858 | 7.8 |
| 35 | L1-worker | claudeopus46 | 24,095 | 17,404 | 41,499 | 765 | 6.4 |
| 36 | L1-worker | claudeopus46 | 24,095 | 18,745 | 42,840 | 710 | 6.7 |
| 37 | L1-worker | claudeopus46 | 24,095 | 19,695 | 43,790 | 3,132 | 23.1 |
| 38 | L1-worker | claudeopus46 | 24,095 | 28,525 | 52,620 | 1,673 | 13.4 |
| 39 | L1-worker | claudeopus46 | 24,095 | 29,589 | 53,684 | 3,581 | 27.1 |
| 40 | L1-worker | claudeopus46 | 24,095 | 37,603 | 61,698 | 3,514 | 27.6 |
| 41 | L1-worker | claudeopus46 | 627 | 6,590 | 7,217 | 952 | 9.3 |
| 42 | L1-worker | claudeopus46 | 2,320 | 6,710 | 9,030 | 1,461 | 11.6 |
| 43 | L1-worker | claudeopus46 | 2,106 | 8,731 | 10,837 | 2,889 | 14.2 |
| 44 | L1-worker | claudeopus46 | 366 | 1,898 | 2,264 | 1,411 | 4.7 |
| 45 | L1-worker | claudeopus46 | 366 | 3,666 | 4,032 | 1,779 | 7.7 |
| 46 | L1-worker | claudeopus46 | 787 | 47,767 | 48,554 | 889 | 9.2 |
| 47 | L0-main | claudeopus46 | 11,581 | 60,408 | 71,989 | 4,216 | 31.3 |
| 48 | L0-main | claudeopus46 | 2,106 | 4,160 | 6,266 | 1,288 | 7.5 |
| 49 | L0-main | claudeopus46 | 2,320 | 3,636 | 5,956 | 1,241 | 7.9 |
| 50 | L0-main | claudeopus46 | 366 | 1,716 | 2,082 | 1,187 | 4.6 |
| 51 | L0-main | claudeopus46 | 366 | 1,837 | 2,203 | 1,594 | 8.9 |
| 52 | L0-main | claudeopus46 | 560 | 5,536 | 6,096 | 518 | 4.3 |
| 53 | L0-main | claudeopus46 | 1,156 | 9,315 | 10,471 | 2,115 | 13.4 |
| 54 | L0-main | claudeopus46 | 366 | 2,808 | 3,174 | 2,103 | 7.7 |

