# Reference Stats — analysis-agent

**Run started:** 2026-09-05 04:11:54
**Wall time (at last flush):** 300.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 22 | 346,562 | 291,202 | 25,967 | 637,764 | 28,989 | 201.9 | claudeopus46 |
| L1-worker | 17 | 184,365 | 52,231 | 13,770 | 236,596 | 13,917 | 100.7 | claudeopus46 |
| **TOTAL** | **39** | **530,927** | **343,433** | **39,737** | **874,360** | **22,419** | **302.6** | |

**Estimated tokens:** ~218,590 input + ~9,934 output = ~228,524 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `search_blocks` | 2 | 1 | 6 | 2 | 9 | 9 | 1,349 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 2 | 1 | 1 | 1 | 0 |
| **TOTAL** | **4** | **2** | **8** | **3** | **10** | **10** | **1,349** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### References (9 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_2825 |  | query_thermoml, search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_8254 |  | search_blocks |
| GLOBlit_8424 |  | search_blocks |
| GLOBlit_8869 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9571 |  | search_blocks |
| GLOBlit_10866 |  | search_blocks |

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_4 | methanol | query_thermoml, search_blocks |
| GLOBcomp_1 | water | query_thermoml, search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml, search_blocks |

#### Measurements (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_280 | Mass density, kg/m3 | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_3 |  | search_blocks |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_18 | Volume fraction | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique References | 9 |
| Unique Compounds | 2 |
| Unique Properties | 1 |
| Unique Measurements | 6 |
| Unique Phases | 1 |
| Unique Solvents | 2 |
| Unique Variables | 6 |
| Unique Constraints | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 9 |
| Unique parent blocks | 9 |
| Explicit block/subsystem targets | 9 |
| Subsystem targets | 0 |
| Target-matched data points | 1,388 |

---

## 3. DOI & Block References

**Unique DOIs:** 9  |  **Parent blocks:** 9  |  **Explicit targets:** 9  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,349

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2004.07.019 | 1 | 596 | binary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 1 | 39 | binary | query_thermoml, search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks |
| 10.1021/je034101z | 1 | 401 | binary | search_blocks |
| 10.1021/je049691v | 1 | 180 | binary | search_blocks |
| 10.1021/je0600810 | 1 | 9 | binary | search_blocks |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks |
| 10.1021/je2003622 | 1 | 16 | binary | search_blocks |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | — | search_blocks |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | — | search_blocks |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | — | search_blocks |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | — | search_blocks |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | — | search_blocks |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve methanol an… | 171 | KEEP ←in 277 | 171 | 3.7 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=50, p… | 748 | KEEP ←in 5,885 | 748 | 23.3 |
| 3 | 5 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_10, purpose=G… | 347 | — | — | 0.4 |
| 4 | 6 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_10, purpose=G… | 1,487 | — | — | 0.2 |
| 5 | 1 | `query_thermoml` | instruction=Search for binary mixture dat…, purpos… | 12,643 | — | — | 97.1 |
| 6 | 4 | `inspect_block` | block_number=PROPblock_10, doi=10.1016/j.jct.2007.… | 1,360 | — | — | 0.2 |
| 7 | 8 | `fit_block` | block_number=PROPblock_10, doi=10.1016/j.jct.2007.… | 246 | — | — | 0.1 |
| 8 | 12 | `fit_block` | block_number=PROPblock_10, doi=10.1016/j.jct.2007.… | 871 | — | — | 3.1 |
| | | **TOTAL (8 tools)** | | **17,873** | | **919** | **128.1** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 840 | 23,358 | 958 | 7.3 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,078 | 25,173 | 606 | 5.9 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,096 | 26,191 | 518 | 3.9 |
| 4 | L1-worker | claudeopus46 | 3,767 | 438 | 4,205 | 308 | 3.4 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,662 | 25,757 | 803 | 6.0 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,365 | 26,460 | 649 | 4.8 |
| 7 | L1-worker | claudeopus46 | 3,767 | 6,378 | 10,145 | 1,937 | 15.3 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,084 | 27,179 | 1,046 | 8.0 |
| 9 | L1-worker | claudeopus46 | 24,095 | 3,826 | 27,921 | 698 | 5.7 |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,650 | 29,745 | 1,714 | 12.6 |
| 11 | L1-worker | claudeopus46 | 2,106 | 3,044 | 5,150 | 451 | 3.1 |
| 12 | L1-worker | claudeopus46 | 2,320 | 1,845 | 4,165 | 901 | 5.3 |
| 13 | L1-worker | claudeopus46 | 366 | 1,228 | 1,594 | 349 | 2.4 |
| 14 | L1-worker | claudeopus46 | 627 | 1,725 | 2,352 | 1,033 | 6.4 |
| 15 | L1-worker | claudeopus46 | 366 | 1,338 | 1,704 | 861 | 3.5 |
| 16 | L1-worker | claudeopus46 | 366 | 1,444 | 1,810 | 1,020 | 4.6 |
| 17 | L1-worker | claudeopus46 | 1,228 | 3,795 | 5,023 | 374 | 3.1 |
| 18 | L1-worker | claudeopus46 | 787 | 11,235 | 12,022 | 502 | 6.7 |
| 19 | L0-main | claudeopus46 | 22,518 | 12,585 | 35,103 | 1,458 | 12.8 |
| 20 | L0-main | claudeopus46 | 22,518 | 13,374 | 35,892 | 571 | 5.2 |
| 21 | L0-main | claudeopus46 | 22,518 | 14,062 | 36,580 | 542 | 4.6 |
| 22 | L0-main | claudeopus46 | 22,518 | 15,823 | 38,341 | 1,480 | 11.0 |
| 23 | L0-main | claudeopus46 | 22,518 | 16,546 | 39,064 | 891 | 6.8 |
| 24 | L0-main | claudeopus46 | 22,518 | 17,227 | 39,745 | 1,142 | 8.3 |
| 25 | L0-main | claudeopus46 | 22,518 | 18,048 | 40,566 | 861 | 5.8 |
| 26 | L0-main | claudeopus46 | 22,518 | 17,744 | 40,262 | 847 | 5.9 |
| 27 | L0-main | claudeopus46 | 22,518 | 18,417 | 40,935 | 802 | 6.0 |
| 28 | L0-main | claudeopus46 | 22,518 | 19,046 | 41,564 | 892 | 10.9 |
| 29 | L0-main | claudeopus46 | 22,518 | 19,761 | 42,279 | 839 | 6.3 |
| 30 | L0-main | claudeopus46 | 22,518 | 21,430 | 43,948 | 3,847 | 27.7 |
| 31 | L0-main | claudeopus46 | 22,518 | 28,017 | 50,535 | 3,627 | 26.7 |
| 32 | L0-main | claudeopus46 | 22,518 | 34,390 | 56,908 | 3,061 | 22.7 |
| 33 | L0-main | claudeopus46 | 2,106 | 4,129 | 6,235 | 154 | 2.6 |
| 34 | L0-main | claudeopus46 | 366 | 677 | 1,043 | 195 | 2.1 |
| 35 | L0-main | claudeopus46 | 2,320 | 3,190 | 5,510 | 1,077 | 7.2 |
| 36 | L0-main | claudeopus46 | 366 | 1,514 | 1,880 | 1,037 | 4.3 |
| 37 | L0-main | claudeopus46 | 560 | 3,711 | 4,271 | 100 | 2.2 |
| 38 | L0-main | claudeopus46 | 1,156 | 4,489 | 5,645 | 476 | 4.9 |
| 39 | L0-main | claudeopus46 | 1,918 | 6,182 | 8,100 | 1,110 | 10.6 |

