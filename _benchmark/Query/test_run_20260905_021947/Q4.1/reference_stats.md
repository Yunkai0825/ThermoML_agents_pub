# Reference Stats — query-agent

**Run started:** 2026-09-05 05:36:05
**Wall time (at last flush):** 623.5 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 12 | 65,145 | 162,697 | 25,612 | 227,842 | 18,986 | 162.8 | claudeopus46 |
| L1-worker | 60 | 748,011 | 470,954 | 68,127 | 1,218,965 | 20,316 | 490.8 | claudeopus46 |
| **TOTAL** | **72** | **813,156** | **633,651** | **93,739** | **1,446,807** | **20,094** | **653.6** | |

**Estimated tokens:** ~361,701 input + ~23,434 output = ~385,135 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 2 | 4 | 4 | 177 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 1 | 2 | 2 | 86 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 80 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **9** | **3** | **7** | **4** | **7** | **7** | **343** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_18 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_15 |  | resolve_compound_ids, search_blocks |

#### References (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_8676 |  | search_blocks |
| GLOBlit_9900 |  | search_blocks |
| GLOBlit_11030 |  | search_blocks |
| GLOBlit_11207 |  | search_blocks |
| GLOBlit_4124 |  | search_blocks |
| GLOBlit_7481 |  | search_blocks |
| GLOBlit_2602 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |

#### Measurements (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 3 |
| Unique References | 7 |
| Unique Properties | 1 |
| Unique Measurements | 3 |
| Unique Phases | 1 |
| Unique Variables | 3 |
| Unique Constraints | 2 |
| Total DOIs | 7 |
| Unique parent blocks | 7 |
| Explicit block/subsystem targets | 7 |
| Subsystem targets | 0 |
| Target-matched data points | 343 |

---

## 3. DOI & Block References

**Unique DOIs:** 7  |  **Parent blocks:** 7  |  **Explicit targets:** 7  |  **Subsystems:** 0  |  **Target-matched datapoints:** 343

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2005.08.009 | 1 | 80 | binary | search_blocks |
| 10.1016/j.jct.2014.02.019 | 1 | 20 | binary | search_blocks |
| 10.1021/acs.jced.8b00176 | 1 | 66 | binary | search_blocks |
| 10.1021/je050209y | 1 | 11 | binary | search_blocks |
| 10.1021/je300608v | 1 | 60 | binary | search_blocks |
| 10.1021/je700671t | 1 | 98 | binary | search_blocks |
| 10.1021/je800330d | 1 | 8 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2005.08.009 | PROPblock_3 | declared | 80 | binary | — | search_blocks |
| 10.1016/j.jct.2014.02.019 | PROPblock_6 | declared | 20 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00176 | PROPblock_18 | declared | 66 | binary | — | search_blocks |
| 10.1021/je050209y | PROPblock_9 | declared | 11 | binary | — | search_blocks |
| 10.1021/je300608v | PROPblock_3 | declared | 60 | binary | — | search_blocks |
| 10.1021/je700671t | PROPblock_3 | declared | 98 | binary | — | search_blocks |
| 10.1021/je800330d | PROPblock_3 | declared | 8 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve DMF, water,… | 270 | KEEP ←in 364 | 270 | 5.3 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1',…, limit=50,… | 864 | DISCARD ←in 39 | 806 | 8.8 |
| 3 | 5 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1',…, limit=20,… | 889 | DISCARD ←in 39 | 831 | 15.9 |
| 4 | 1 | `L1_query` | instruction=Search for dynamic viscosity …, purpos… | 1,907 | — | — | 81.8 |
| 5 | 2 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1'], limit=50, … | 763 | KEEP ←in 8,201 | 763 | 21.3 |
| 6 | 3 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_8676,… | 1,354 | — | — | 0.7 |
| 7 | 4 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_9900,… | 259 | — | — | 0.0 |
| 8 | 5 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_9900,… | 260 | — | — | 0.0 |
| 9 | 6 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_9900,… | 1,498 | — | — | 0.2 |
| 10 | 2 | `L1_query` | context=Looking for binary subsystem …, id_catalog… | 22,359 | — | — | 115.9 |
| 11 | 2 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_15'], limit=50,… | 830 | KEEP ←in 4,801 | 830 | 22.3 |
| 12 | 3 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_4124,… | 362 | — | — | 0.1 |
| 13 | 4 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_4124,… | 1,094 | — | — | 0.1 |
| 14 | 5 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_7481… | 1,396 | — | — | 1.3 |
| 15 | 3 | `L1_query` | context=Building estimation for terna…, id_catalog… | 22,883 | — | — | 148.3 |
| 16 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 1,123 | KEEP ←in 2,582 | 1108 | 19.9 |
| 17 | 3 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2602,… | 357 | — | — | 0.2 |
| 18 | 4 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2602,… | 1,596 | — | — | 0.2 |
| 19 | 4 | `L1_query` | context=Building estimation for terna…, id_catalog… | 13,651 | — | — | 124.3 |
| | | **TOTAL (19 tools)** | | **73,715** | | **4,608** | **566.6** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 700 | 12,281 | 1,026 | 7.8 |
| 2 | L1-worker | claudeopus46 | 24,095 | 868 | 24,963 | 719 | 9.7 |
| 3 | L1-worker | claudeopus46 | 24,095 | 1,922 | 26,017 | 579 | 4.1 |
| 4 | L1-worker | claudeopus46 | 3,767 | 536 | 4,303 | 415 | 4.0 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,576 | 25,671 | 991 | 8.4 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,329 | 26,424 | 684 | 4.8 |
| 7 | L1-worker | claudeopus46 | 3,767 | 572 | 4,339 | 1,160 | 8.4 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,189 | 27,284 | 848 | 5.9 |
| 9 | L1-worker | claudeopus46 | 3,767 | 494 | 4,261 | 1,241 | 9.4 |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,446 | 28,541 | 1,146 | 9.1 |
| 11 | L1-worker | claudeopus46 | 2,106 | 1,910 | 4,016 | 92 | 2.0 |
| 12 | L1-worker | claudeopus46 | 627 | 801 | 1,428 | 461 | 2.9 |
| 13 | L1-worker | claudeopus46 | 2,320 | 921 | 3,241 | 488 | 3.1 |
| 14 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.0 |
| 15 | L1-worker | claudeopus46 | 787 | 2,659 | 3,446 | 373 | 3.6 |
| 16 | L0-main | claudeopus46 | 11,581 | 4,847 | 16,428 | 1,285 | 8.8 |
| 17 | L1-worker | claudeopus46 | 24,095 | 3,193 | 27,288 | 902 | 7.4 |
| 18 | L1-worker | claudeopus46 | 24,095 | 3,938 | 28,033 | 653 | 5.2 |
| 19 | L1-worker | claudeopus46 | 3,767 | 8,693 | 12,460 | 1,740 | 15.2 |
| 20 | L1-worker | claudeopus46 | 24,095 | 4,662 | 28,757 | 994 | 7.4 |
| 21 | L1-worker | claudeopus46 | 24,095 | 6,377 | 30,472 | 824 | 6.5 |
| 22 | L1-worker | claudeopus46 | 24,095 | 7,038 | 31,133 | 667 | 5.7 |
| 23 | L1-worker | claudeopus46 | 24,095 | 7,650 | 31,745 | 630 | 5.1 |
| 24 | L1-worker | claudeopus46 | 24,095 | 9,466 | 33,561 | 2,645 | 18.9 |
| 25 | L1-worker | claudeopus46 | 24,095 | 14,527 | 38,622 | 2,701 | 15.2 |
| 26 | L1-worker | claudeopus46 | 2,320 | 2,832 | 5,152 | 933 | 5.5 |
| 27 | L1-worker | claudeopus46 | 2,106 | 4,127 | 6,233 | 931 | 5.6 |
| 28 | L1-worker | claudeopus46 | 627 | 2,712 | 3,339 | 1,220 | 6.9 |
| 29 | L1-worker | claudeopus46 | 366 | 1,708 | 2,074 | 705 | 3.8 |
| 30 | L1-worker | claudeopus46 | 366 | 1,370 | 1,736 | 888 | 4.5 |
| 31 | L1-worker | claudeopus46 | 366 | 1,631 | 1,997 | 1,207 | 5.0 |
| 32 | L1-worker | claudeopus46 | 787 | 19,148 | 19,935 | 716 | 7.8 |
| 33 | L0-main | claudeopus46 | 11,581 | 22,120 | 33,701 | 1,231 | 11.4 |
| 34 | L1-worker | claudeopus46 | 24,095 | 9,736 | 33,831 | 826 | 6.2 |
| 35 | L1-worker | claudeopus46 | 24,095 | 10,459 | 34,554 | 662 | 4.8 |
| 36 | L1-worker | claudeopus46 | 3,767 | 5,288 | 9,055 | 1,637 | 15.2 |
| 37 | L1-worker | claudeopus46 | 24,095 | 11,270 | 35,365 | 1,035 | 7.8 |
| 38 | L1-worker | claudeopus46 | 24,095 | 12,043 | 36,138 | 608 | 4.9 |
| 39 | L1-worker | claudeopus46 | 24,095 | 13,447 | 37,542 | 754 | 6.4 |
| 40 | L1-worker | claudeopus46 | 24,095 | 15,191 | 39,286 | 2,376 | 17.9 |
| 41 | L1-worker | claudeopus46 | 24,095 | 21,075 | 45,170 | 2,635 | 18.8 |
| 42 | L1-worker | claudeopus46 | 24,095 | 27,321 | 51,416 | 4,849 | 32.5 |
| 43 | L1-worker | claudeopus46 | 2,106 | 5,737 | 7,843 | 1,233 | 6.1 |
| 44 | L1-worker | claudeopus46 | 627 | 4,194 | 4,821 | 1,041 | 6.8 |
| 45 | L1-worker | claudeopus46 | 2,320 | 4,314 | 6,634 | 1,286 | 8.3 |
| 46 | L1-worker | claudeopus46 | 366 | 2,010 | 2,376 | 748 | 4.1 |
| 47 | L1-worker | claudeopus46 | 366 | 1,723 | 2,089 | 1,220 | 5.5 |
| 48 | L1-worker | claudeopus46 | 787 | 22,603 | 23,390 | 725 | 8.8 |
| 49 | L0-main | claudeopus46 | 11,581 | 41,576 | 53,157 | 1,104 | 8.8 |
| 50 | L1-worker | claudeopus46 | 24,095 | 16,935 | 41,030 | 794 | 6.6 |
| 51 | L1-worker | claudeopus46 | 24,095 | 17,641 | 41,736 | 707 | 5.0 |
| 52 | L1-worker | claudeopus46 | 3,767 | 3,072 | 6,839 | 1,535 | 14.5 |
| 53 | L1-worker | claudeopus46 | 24,095 | 18,718 | 42,813 | 834 | 7.2 |
| 54 | L1-worker | claudeopus46 | 24,095 | 19,431 | 43,526 | 610 | 4.6 |
| 55 | L1-worker | claudeopus46 | 24,095 | 21,300 | 45,395 | 2,880 | 20.7 |
| 56 | L1-worker | claudeopus46 | 24,095 | 27,567 | 51,662 | 2,343 | 18.3 |
| 57 | L1-worker | claudeopus46 | 24,095 | 32,661 | 56,756 | 3,381 | 22.5 |
| 58 | L1-worker | claudeopus46 | 2,106 | 3,625 | 5,731 | 524 | 4.4 |
| 59 | L1-worker | claudeopus46 | 627 | 2,223 | 2,850 | 1,063 | 5.3 |
| 60 | L1-worker | claudeopus46 | 2,320 | 2,343 | 4,663 | 1,127 | 5.9 |
| 61 | L1-worker | claudeopus46 | 366 | 1,301 | 1,667 | 397 | 3.4 |
| 62 | L1-worker | claudeopus46 | 366 | 1,474 | 1,840 | 1,050 | 4.0 |
| 63 | L1-worker | claudeopus46 | 366 | 1,564 | 1,930 | 1,115 | 4.4 |
| 64 | L1-worker | claudeopus46 | 787 | 12,524 | 13,311 | 512 | 6.8 |
| 65 | L0-main | claudeopus46 | 11,581 | 55,212 | 66,793 | 11,801 | 80.1 |
| 66 | L0-main | claudeopus46 | 2,106 | 6,698 | 8,804 | 1,176 | 6.5 |
| 67 | L0-main | claudeopus46 | 2,320 | 6,166 | 8,486 | 1,219 | 7.5 |
| 68 | L0-main | claudeopus46 | 366 | 1,725 | 2,091 | 1,149 | 4.5 |
| 69 | L0-main | claudeopus46 | 366 | 1,694 | 2,060 | 1,170 | 4.5 |
| 70 | L0-main | claudeopus46 | 560 | 7,775 | 8,335 | 427 | 3.2 |
| 71 | L0-main | claudeopus46 | 1,156 | 11,324 | 12,480 | 2,167 | 12.9 |
| 72 | L0-main | claudeopus46 | 366 | 2,860 | 3,226 | 1,857 | 6.8 |

