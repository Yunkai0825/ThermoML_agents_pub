# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:07:36
**Wall time (at last flush):** 484.6 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 19 | 279,008 | 624,394 | 47,387 | 903,402 | 47,547 | 345.1 | claudeopus46 |
| L1-worker | 64 | 787,670 | 226,677 | 57,081 | 1,014,347 | 15,849 | 459.3 | claudeopus46 |
| **TOTAL** | **83** | **1,066,678** | **851,071** | **104,468** | **1,917,749** | **23,105** | **804.4** | |

**Estimated tokens:** ~479,437 input + ~26,117 output = ~505,554 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 1 | 2 | 2 | 86 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 80 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 2 | 4 | 4 | 177 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 3 | 1 | 3 | 2 | 4 | 4 | 0 |
| **TOTAL** | **18** | **4** | **10** | **6** | **11** | **11** | **343** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_15 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_18 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |

#### References (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_4124 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_7481 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2602 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8676 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_9900 |  | search_blocks |
| GLOBlit_11030 |  | search_blocks |
| GLOBlit_11207 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |

#### Measurements (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_4 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBconstr_2 | Temperature, K | query_thermoml_parallel, search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml_parallel |

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
| Unique Block_Types | 1 |
| Total DOIs | 7 |
| Unique parent blocks | 7 |
| Explicit block/subsystem targets | 7 |
| Subsystem targets | 0 |
| Target-matched data points | 520 |

---

## 3. DOI & Block References

**Unique DOIs:** 7  |  **Parent blocks:** 7  |  **Explicit targets:** 7  |  **Subsystems:** 0  |  **Target-matched datapoints:** 343

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2005.08.009 | 1 | 80 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2014.02.019 | 1 | 20 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/acs.jced.8b00176 | 1 | 66 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je050209y | 1 | 11 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je300608v | 1 | 60 | binary | search_blocks |
| 10.1021/je700671t | 1 | 98 | binary | search_blocks |
| 10.1021/je800330d | 1 | 8 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2005.08.009 | PROPblock_3 | declared | 80 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2014.02.019 | PROPblock_6 | declared | 20 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/acs.jced.8b00176 | PROPblock_18 | declared | 66 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je050209y | PROPblock_9 | declared | 11 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je300608v | PROPblock_3 | declared | 60 | binary | — | search_blocks |
| 10.1021/je700671t | PROPblock_3 | declared | 98 | binary | — | search_blocks |
| 10.1021/je800330d | PROPblock_3 | declared | 8 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'ternary_viscosity… | 209 | — | — | 0.0 |
| 2 | 1 | `resolve_compound_ids` | purpose=Find compound IDs for DMF and…, queries=['… | 221 | KEEP ←in 308 | 221 | 4.0 |
| 3 | 1 | `resolve_compound_ids` | purpose=Find compound IDs for water a…, queries=['… | 192 | KEEP ←in 285 | 192 | 4.5 |
| 4 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 262 | KEEP ←in 364 | 262 | 4.2 |
| 5 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve DMF and wat… | 208 | KEEP ←in 295 | 208 | 4.5 |
| 6 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 975 | KEEP ←in 2,582 | 960 | 12.9 |
| 7 | 3 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_15'], limit=50,… | 909 | KEEP ←in 4,801 | 909 | 14.7 |
| 8 | 4 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1',…, limit=50,… | 1,087 | DISCARD ←in 39 | 1029 | 10.7 |
| 9 | 4 | `inspect_block_table` | block_number=GLOBlit_2602::PROPblock_3, purpose=Ve… | 357 | — | — | 0.1 |
| 10 | 4 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1'], limit=50, … | 590 | KEEP ←in 8,201 | 590 | 16.8 |
| 11 | 4 | `inspect_block_table` | block_number=GLOBlit_7481::PROPblock_18, purpose=G… | 358 | — | — | 0.1 |
| 12 | 5 | `inspect_block_table` | block_number=GLOBlit_2602::PROPblock_3, purpose=Ve… | 1,596 | — | — | 0.2 |
| 13 | 5 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_8676,… | 1,354 | — | — | 0.2 |
| 14 | 5 | `inspect_block_table` | block_number=GLOBlit_7481::PROPblock_18, purpose=G… | 1,396 | — | — | 0.2 |
| 15 | 5 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1',…, limit=50,… | 925 | DISCARD ←in 39 | 867 | 9.2 |
| 16 | 6 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1',…, limit=20,… | 259 | KEEP ←in 39 | 259 | 12.0 |
| 17 | 7 | `inspect_block_table` | block_number=GLOBlit_4124::PROPblock_6, purpose=Gr… | 1,094 | — | — | 0.1 |
| 18 | 2 | `query_thermoml_parallel` | queries=[{'label': 'ternary_viscosity… | 56,581 | — | — | 132.7 |
| 19 | 5 | `fit_multi_system` | purpose=Fit Redlich-Kister polynomial…, systems=[{… | 771 | — | — | 1.0 |
| 20 | 7 | `fit_multi_system` | purpose=Fit Arrhenius-RK models for a…, systems=[{… | 1,723 | — | — | 4.4 |
| 21 | 9 | `predict_from_rk` | coeffs=[3.1881, -3.9583, 1.8651, 0.4…, mixing_rule… | 220 | — | — | 0.3 |
| 22 | 10 | `predict_from_rk` | coeffs=[0.551336, 0.125607, -0.52268…, mixing_rule… | 227 | — | — | 0.2 |
| 23 | 11 | `predict_from_rk` | coeffs=[0.0445032, -1.16762, 0.25588…, mixing_rule… | 221 | — | — | 0.1 |
| | | **TOTAL (23 tools)** | | **71,735** | | **5,497** | **233.1** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 425 | 22,943 | 2,465 | 12.4 |
| 2 | L0-main | claudeopus46 | 22,518 | 914 | 23,432 | 1,916 | 10.2 |
| 3 | L1-worker | claudeopus46 | 24,095 | 814 | 24,909 | 564 | 4.4 |
| 4 | L1-worker | claudeopus46 | 24,095 | 828 | 24,923 | 591 | 4.9 |
| 5 | L1-worker | claudeopus46 | 24,095 | 827 | 24,922 | 685 | 5.3 |
| 6 | L1-worker | claudeopus46 | 24,095 | 814 | 24,909 | 738 | 5.8 |
| 7 | L1-worker | claudeopus46 | 3,767 | 445 | 4,212 | 371 | 3.9 |
| 8 | L1-worker | claudeopus46 | 3,767 | 424 | 4,191 | 372 | 4.2 |
| 9 | L1-worker | claudeopus46 | 24,095 | 1,879 | 25,974 | 577 | 4.3 |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,835 | 25,930 | 569 | 4.1 |
| 11 | L1-worker | claudeopus46 | 3,767 | 530 | 4,297 | 390 | 4.0 |
| 12 | L1-worker | claudeopus46 | 3,767 | 446 | 4,213 | 386 | 4.4 |
| 13 | L1-worker | claudeopus46 | 24,095 | 1,308 | 25,403 | 761 | 6.1 |
| 14 | L1-worker | claudeopus46 | 24,095 | 1,257 | 25,352 | 814 | 7.4 |
| 15 | L1-worker | claudeopus46 | 24,095 | 1,527 | 25,622 | 892 | 6.4 |
| 16 | L1-worker | claudeopus46 | 24,095 | 2,029 | 26,124 | 707 | 5.0 |
| 17 | L1-worker | claudeopus46 | 24,095 | 1,483 | 25,578 | 839 | 6.7 |
| 18 | L1-worker | claudeopus46 | 24,095 | 1,980 | 26,075 | 682 | 5.1 |
| 19 | L1-worker | claudeopus46 | 24,095 | 2,280 | 26,375 | 672 | 4.9 |
| 20 | L1-worker | claudeopus46 | 24,095 | 2,199 | 26,294 | 691 | 4.7 |
| 21 | L1-worker | claudeopus46 | 3,767 | 3,078 | 6,845 | 1,341 | 12.5 |
| 22 | L1-worker | claudeopus46 | 3,767 | 5,322 | 9,089 | 1,622 | 14.2 |
| 23 | L1-worker | claudeopus46 | 3,767 | 561 | 4,328 | 1,548 | 10.3 |
| 24 | L1-worker | claudeopus46 | 24,095 | 2,947 | 27,042 | 761 | 6.5 |
| 25 | L1-worker | claudeopus46 | 24,095 | 3,317 | 27,412 | 829 | 6.5 |
| 26 | L1-worker | claudeopus46 | 3,767 | 8,690 | 12,457 | 1,628 | 16.2 |
| 27 | L1-worker | claudeopus46 | 24,095 | 2,930 | 27,025 | 1,008 | 8.5 |
| 28 | L1-worker | claudeopus46 | 24,095 | 3,640 | 27,735 | 601 | 5.0 |
| 29 | L1-worker | claudeopus46 | 24,095 | 2,782 | 26,877 | 798 | 6.7 |
| 30 | L1-worker | claudeopus46 | 24,095 | 3,683 | 27,778 | 726 | 5.9 |
| 31 | L1-worker | claudeopus46 | 3,767 | 565 | 4,332 | 1,154 | 8.5 |
| 32 | L1-worker | claudeopus46 | 24,095 | 5,520 | 29,615 | 1,568 | 12.2 |
| 33 | L1-worker | claudeopus46 | 24,095 | 4,570 | 28,665 | 1,044 | 10.1 |
| 34 | L1-worker | claudeopus46 | 24,095 | 4,472 | 28,567 | 1,785 | 13.2 |
| 35 | L1-worker | claudeopus46 | 24,095 | 5,413 | 29,508 | 1,903 | 16.3 |
| 36 | L1-worker | claudeopus46 | 24,095 | 9,416 | 33,511 | 2,030 | 12.9 |
| 37 | L1-worker | claudeopus46 | 3,767 | 495 | 4,262 | 470 | 4.2 |
| 38 | L1-worker | claudeopus46 | 24,095 | 10,463 | 34,558 | 799 | 7.5 |
| 39 | L1-worker | claudeopus46 | 627 | 1,589 | 2,216 | 714 | 4.5 |
| 40 | L1-worker | claudeopus46 | 2,320 | 1,709 | 4,029 | 790 | 5.1 |
| 41 | L1-worker | claudeopus46 | 2,106 | 2,644 | 4,750 | 908 | 5.1 |
| 42 | L1-worker | claudeopus46 | 366 | 1,227 | 1,593 | 755 | 3.5 |
| 43 | L1-worker | claudeopus46 | 366 | 1,685 | 2,051 | 648 | 4.1 |
| 44 | L1-worker | claudeopus46 | 24,095 | 8,519 | 32,614 | 3,606 | 21.1 |
| 45 | L1-worker | claudeopus46 | 787 | 11,303 | 12,090 | 607 | 6.9 |
| 46 | L1-worker | claudeopus46 | 2,320 | 1,880 | 4,200 | 684 | 4.1 |
| 47 | L1-worker | claudeopus46 | 2,106 | 2,815 | 4,921 | 735 | 4.4 |
| 48 | L1-worker | claudeopus46 | 627 | 1,760 | 2,387 | 1,020 | 6.1 |
| 49 | L1-worker | claudeopus46 | 24,095 | 11,947 | 36,042 | 1,924 | 17.5 |
| 50 | L1-worker | claudeopus46 | 366 | 1,121 | 1,487 | 649 | 3.3 |
| 51 | L1-worker | claudeopus46 | 366 | 1,512 | 1,878 | 341 | 3.1 |
| 52 | L1-worker | claudeopus46 | 24,095 | 5,142 | 29,237 | 684 | 20.1 |
| 53 | L1-worker | claudeopus46 | 1,228 | 3,558 | 4,786 | 367 | 3.2 |
| 54 | L1-worker | claudeopus46 | 2,320 | 568 | 2,888 | 301 | 2.3 |
| 55 | L1-worker | claudeopus46 | 627 | 448 | 1,075 | 275 | 2.4 |
| 56 | L1-worker | claudeopus46 | 2,106 | 1,516 | 3,622 | 92 | 3.1 |
| 57 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.0 |
| 58 | L1-worker | claudeopus46 | 787 | 1,573 | 2,360 | 433 | 3.8 |
| 59 | L1-worker | claudeopus46 | 787 | 10,927 | 11,714 | 617 | 8.6 |
| 60 | L1-worker | claudeopus46 | 24,095 | 16,826 | 40,921 | 1,960 | 15.7 |
| 61 | L1-worker | claudeopus46 | 2,320 | 3,264 | 5,584 | 781 | 6.6 |
| 62 | L1-worker | claudeopus46 | 627 | 3,144 | 3,771 | 882 | 7.4 |
| 63 | L1-worker | claudeopus46 | 2,106 | 4,213 | 6,319 | 1,572 | 9.7 |
| 64 | L1-worker | claudeopus46 | 366 | 1,218 | 1,584 | 746 | 4.0 |
| 65 | L1-worker | claudeopus46 | 366 | 2,349 | 2,715 | 1,301 | 5.6 |
| 66 | L1-worker | claudeopus46 | 787 | 20,582 | 21,369 | 706 | 7.2 |
| 67 | L0-main | claudeopus46 | 22,518 | 55,178 | 77,696 | 2,054 | 15.6 |
| 68 | L0-main | claudeopus46 | 22,518 | 55,952 | 78,470 | 1,695 | 9.8 |
| 69 | L0-main | claudeopus46 | 22,518 | 56,830 | 79,348 | 2,052 | 13.8 |
| 70 | L0-main | claudeopus46 | 22,518 | 57,181 | 79,699 | 2,156 | 17.8 |
| 71 | L0-main | claudeopus46 | 22,518 | 57,945 | 80,463 | 2,509 | 15.6 |
| 72 | L0-main | claudeopus46 | 22,518 | 63,560 | 86,078 | 6,197 | 48.0 |
| 73 | L0-main | claudeopus46 | 22,518 | 64,298 | 86,816 | 1,168 | 10.0 |
| 74 | L0-main | claudeopus46 | 22,518 | 64,616 | 87,134 | 4,337 | 34.5 |
| 75 | L0-main | claudeopus46 | 22,518 | 65,227 | 87,745 | 4,627 | 35.3 |
| 76 | L0-main | claudeopus46 | 22,518 | 65,810 | 88,328 | 12,900 | 93.7 |
| 77 | L0-main | claudeopus46 | 2,106 | 2,325 | 4,431 | 145 | 2.4 |
| 78 | L0-main | claudeopus46 | 2,320 | 1,785 | 4,105 | 733 | 4.4 |
| 79 | L0-main | claudeopus46 | 366 | 668 | 1,034 | 186 | 2.6 |
| 80 | L0-main | claudeopus46 | 366 | 1,170 | 1,536 | 693 | 3.5 |
| 81 | L0-main | claudeopus46 | 560 | 2,297 | 2,857 | 91 | 2.1 |
| 82 | L0-main | claudeopus46 | 1,156 | 3,068 | 4,224 | 413 | 4.1 |
| 83 | L0-main | claudeopus46 | 1,918 | 5,145 | 7,063 | 1,050 | 9.3 |

