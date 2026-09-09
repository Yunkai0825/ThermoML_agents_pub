# Reference Stats — analysis-agent

**Run started:** 2026-09-05 04:25:09
**Wall time (at last flush):** 574.8 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 24 | 391,598 | 865,193 | 40,439 | 1,256,791 | 52,366 | 313.8 | claudeopus46 |
| L1-worker | 43 | 571,131 | 239,857 | 48,451 | 810,988 | 18,860 | 371.0 | claudeopus46 |
| **TOTAL** | **67** | **962,729** | **1,105,050** | **88,890** | **2,067,779** | **30,862** | **684.8** | |

**Estimated tokens:** ~516,944 input + ~22,222 output = ~539,166 total
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
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 206 |
| `search_blocks` | 2 | 1 | 6 | 2 | 9 | 9 | 1,349 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 6 | 2 | 9 | 9 | 1,349 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_system_registry` | 2 | 1 | 6 | 1 | 8 | 8 | 1,337 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 2 | 2 | 5 | 1 | 6 | 6 | 1,189 |
| `fit_block_derived` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **14** | **7** | **26** | **6** | **33** | **33** | **5,430** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_4 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_1 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks, search_system_registry |

#### Properties (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_28 |  | query_thermoml_parallel, resolve_property_ids, search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |

#### References (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2395 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2432 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_2825 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_7085 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_8254 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_8424 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_8869 |  | search_blocks, search_system_registry |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9571 |  | search_blocks, search_system_registry |
| GLOBlit_10866 |  | search_blocks, search_system_registry |

#### Measurements (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_207 | Excess molar volume, m3/mol | query_thermoml_parallel, search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_170 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_138 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_280 | Mass density, kg/m3 | search_blocks, search_system_registry |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks, search_system_registry |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_18 | Volume fraction | search_blocks, search_system_registry |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBsolvent_3 |  | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml_parallel, search_system_registry |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique Properties | 2 |
| Unique References | 10 |
| Unique Measurements | 7 |
| Unique Phases | 1 |
| Unique Variables | 6 |
| Unique Solvents | 2 |
| Unique Constraints | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 10 |
| Unique parent blocks | 10 |
| Explicit block/subsystem targets | 10 |
| Subsystem targets | 0 |
| Target-matched data points | 5,675 |

---

## 3. DOI & Block References

**Unique DOIs:** 10  |  **Parent blocks:** 10  |  **Explicit targets:** 10  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,555

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2004.03.011 | 1 | 206 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 596 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.jct.2007.05.004 | 1 | 39 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je034101z | 1 | 401 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je049691v | 1 | 180 | binary | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je0600810 | 1 | 9 | binary | search_blocks, search_system_registry |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks |
| 10.1021/je2003622 | 1 | 16 | binary | search_blocks, search_system_registry |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks, search_system_registry |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2004.03.011 | PROPblock_1 | declared | 206 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | — | search_blocks |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | 2 | search_blocks, search_system_registry |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume', '… | 132 | — | — | 0.0 |
| 2 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve methanol an… | 180 | KEEP ←in 277 | 180 | 3.8 |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve methanol an… | 236 | KEEP ←in 277 | 236 | 4.3 |
| 4 | 3 | `resolve_property_ids` | limit=5, min_score=70, purpose=Find the global pro… | 256 | KEEP ←in 227 | 256 | 4.7 |
| 5 | 5 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=50, p… | 968 | KEEP ←in 3,972 | 953 | 20.8 |
| 6 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=50, p… | 104 | KEEP ←in 5,885 | 104 | 23.2 |
| 7 | 6 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2395,… | 375 | — | — | 0.3 |
| 8 | 7 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2395,… | 980 | — | — | 0.1 |
| 9 | 5 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=20, p… | 331 | KEEP ←in 5,885 | 331 | 17.1 |
| 10 | 6 | `search_system_registry` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=20, p… | 1,344 | KEEP ←in 6,499 | 1329 | 16.2 |
| 11 | 7 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_10, purpose=G… | 347 | — | — | 0.1 |
| 12 | 8 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_10, purpose=G… | 1,502 | — | — | 0.1 |
| 13 | 10 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_10, nearest={… | 861 | — | — | 0.1 |
| 14 | 11 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_10, purpose=F… | 965 | — | — | 0.1 |
| 15 | 2 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume', '… | 58,627 | — | — | 260.7 |
| 16 | 5 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 211 | — | — | 0.0 |
| 17 | 9 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 301 | — | — | 0.0 |
| 18 | 11 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 237 | — | — | 0.1 |
| 19 | 12 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 954 | — | — | 1.8 |
| 20 | 13 | `predict_from_rk` | coeffs=[-3.98239e-06, -1.5386e-07, 1…, n_points=10… | 207 | — | — | 0.1 |
| 21 | 14 | `list_session_files` |  | 1,681 | — | — | 0.0 |
| | | **TOTAL (21 tools)** | | **70,799** | | **3,389** | **353.6** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 752 | 23,270 | 1,481 | 10.0 |
| 2 | L0-main | claudeopus46 | 22,518 | 1,165 | 23,683 | 1,271 | 8.5 |
| 3 | L1-worker | claudeopus46 | 24,095 | 871 | 24,966 | 755 | 5.3 |
| 4 | L1-worker | claudeopus46 | 24,095 | 968 | 25,063 | 737 | 5.8 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,889 | 25,984 | 518 | 4.1 |
| 6 | L1-worker | claudeopus46 | 3,767 | 438 | 4,205 | 317 | 3.7 |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,028 | 26,123 | 596 | 10.2 |
| 8 | L1-worker | claudeopus46 | 24,095 | 1,464 | 25,559 | 578 | 4.7 |
| 9 | L1-worker | claudeopus46 | 3,767 | 480 | 4,247 | 408 | 4.2 |
| 10 | L1-worker | claudeopus46 | 3,767 | 396 | 4,163 | 362 | 4.6 |
| 11 | L1-worker | claudeopus46 | 24,095 | 1,653 | 25,748 | 862 | 8.2 |
| 12 | L1-worker | claudeopus46 | 24,095 | 1,977 | 26,072 | 850 | 6.6 |
| 13 | L1-worker | claudeopus46 | 24,095 | 2,380 | 26,475 | 637 | 4.9 |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,709 | 26,804 | 662 | 5.3 |
| 15 | L1-worker | claudeopus46 | 3,767 | 4,455 | 8,222 | 1,474 | 14.9 |
| 16 | L1-worker | claudeopus46 | 3,767 | 6,341 | 10,108 | 1,666 | 15.9 |
| 17 | L1-worker | claudeopus46 | 24,095 | 3,667 | 27,762 | 730 | 6.6 |
| 18 | L1-worker | claudeopus46 | 24,095 | 2,465 | 26,560 | 1,175 | 7.5 |
| 19 | L1-worker | claudeopus46 | 24,095 | 4,424 | 28,519 | 819 | 5.5 |
| 20 | L1-worker | claudeopus46 | 24,095 | 5,740 | 29,835 | 1,327 | 10.5 |
| 21 | L1-worker | claudeopus46 | 3,767 | 6,365 | 10,132 | 1,797 | 16.6 |
| 22 | L1-worker | claudeopus46 | 2,106 | 2,450 | 4,556 | 378 | 3.3 |
| 23 | L1-worker | claudeopus46 | 627 | 1,338 | 1,965 | 768 | 5.2 |
| 24 | L1-worker | claudeopus46 | 2,320 | 1,458 | 3,778 | 836 | 5.9 |
| 25 | L1-worker | claudeopus46 | 366 | 1,155 | 1,521 | 366 | 3.1 |
| 26 | L1-worker | claudeopus46 | 366 | 1,179 | 1,545 | 756 | 4.1 |
| 27 | L1-worker | claudeopus46 | 366 | 1,273 | 1,639 | 801 | 4.3 |
| 28 | L1-worker | claudeopus46 | 1,228 | 3,127 | 4,355 | 301 | 2.6 |
| 29 | L1-worker | claudeopus46 | 24,095 | 3,161 | 27,256 | 1,991 | 13.3 |
| 30 | L1-worker | claudeopus46 | 787 | 10,234 | 11,021 | 495 | 5.8 |
| 31 | L1-worker | claudeopus46 | 3,767 | 7,014 | 10,781 | 1,629 | 15.7 |
| 32 | L1-worker | claudeopus46 | 24,095 | 4,975 | 29,070 | 1,408 | 11.2 |
| 33 | L1-worker | claudeopus46 | 24,095 | 5,714 | 29,809 | 658 | 5.4 |
| 34 | L1-worker | claudeopus46 | 24,095 | 7,570 | 31,665 | 2,521 | 20.6 |
| 35 | L1-worker | claudeopus46 | 24,095 | 13,362 | 37,457 | 3,075 | 20.9 |
| 36 | L1-worker | claudeopus46 | 24,095 | 14,618 | 38,713 | 993 | 9.8 |
| 37 | L1-worker | claudeopus46 | 24,095 | 15,945 | 40,040 | 2,470 | 20.0 |
| 38 | L1-worker | claudeopus46 | 24,062 | 20,379 | 44,441 | 2,341 | 13.9 |
| 39 | L1-worker | claudeopus46 | 24,062 | 21,941 | 46,003 | 2,242 | 18.2 |
| 40 | L1-worker | claudeopus46 | 2,320 | 2,961 | 5,281 | 808 | 5.4 |
| 41 | L1-worker | claudeopus46 | 627 | 2,841 | 3,468 | 1,095 | 6.8 |
| 42 | L1-worker | claudeopus46 | 366 | 1,245 | 1,611 | 773 | 3.2 |
| 43 | L1-worker | claudeopus46 | 2,106 | 4,050 | 6,156 | 3,024 | 12.8 |
| 44 | L1-worker | claudeopus46 | 366 | 3,801 | 4,167 | 1,687 | 6.2 |
| 45 | L1-worker | claudeopus46 | 787 | 37,356 | 38,143 | 765 | 8.2 |
| 46 | L0-main | claudeopus46 | 22,518 | 48,245 | 70,763 | 2,829 | 24.6 |
| 47 | L0-main | claudeopus46 | 22,518 | 49,479 | 71,997 | 1,661 | 11.8 |
| 48 | L0-main | claudeopus46 | 22,518 | 50,389 | 72,907 | 834 | 5.1 |
| 49 | L0-main | claudeopus46 | 22,518 | 49,704 | 72,222 | 1,544 | 12.3 |
| 50 | L0-main | claudeopus46 | 22,518 | 50,496 | 73,014 | 1,050 | 8.5 |
| 51 | L0-main | claudeopus46 | 22,518 | 51,249 | 73,767 | 813 | 6.1 |
| 52 | L0-main | claudeopus46 | 22,518 | 52,026 | 74,544 | 859 | 6.6 |
| 53 | L0-main | claudeopus46 | 22,518 | 51,785 | 74,303 | 815 | 7.8 |
| 54 | L0-main | claudeopus46 | 22,518 | 52,538 | 75,056 | 846 | 5.5 |
| 55 | L0-main | claudeopus46 | 22,518 | 52,871 | 75,389 | 932 | 6.2 |
| 56 | L0-main | claudeopus46 | 22,518 | 55,709 | 78,227 | 1,661 | 14.3 |
| 57 | L0-main | claudeopus46 | 22,518 | 56,368 | 78,886 | 2,331 | 17.3 |
| 58 | L0-main | claudeopus46 | 22,518 | 58,490 | 81,008 | 6,755 | 50.5 |
| 59 | L0-main | claudeopus46 | 22,518 | 70,759 | 93,277 | 4,676 | 37.0 |
| 60 | L0-main | claudeopus46 | 22,518 | 78,721 | 101,239 | 4,622 | 39.3 |
| 61 | L0-main | claudeopus46 | 2,106 | 6,302 | 8,408 | 274 | 3.0 |
| 62 | L0-main | claudeopus46 | 366 | 797 | 1,163 | 260 | 2.6 |
| 63 | L0-main | claudeopus46 | 2,320 | 5,451 | 7,771 | 1,267 | 9.4 |
| 64 | L0-main | claudeopus46 | 366 | 1,704 | 2,070 | 1,217 | 5.4 |
| 65 | L0-main | claudeopus46 | 560 | 6,258 | 6,818 | 186 | 2.5 |
| 66 | L0-main | claudeopus46 | 1,156 | 7,727 | 8,883 | 1,013 | 8.4 |
| 67 | L0-main | claudeopus46 | 1,918 | 6,208 | 8,126 | 1,242 | 11.1 |

