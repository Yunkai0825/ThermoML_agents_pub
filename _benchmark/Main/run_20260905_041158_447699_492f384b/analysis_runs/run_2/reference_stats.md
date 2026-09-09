# Reference Stats — analysis-agent

**Run started:** 2026-09-05 04:12:10
**Wall time (at last flush):** 563.4 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 23 | 369,080 | 1,203,590 | 40,282 | 1,572,670 | 68,376 | 321.4 | claudeopus46 |
| L1-worker | 40 | 565,770 | 294,250 | 48,611 | 860,020 | 21,500 | 365.4 | claudeopus46 |
| **TOTAL** | **63** | **934,850** | **1,497,840** | **88,893** | **2,432,690** | **38,614** | **686.8** | |

**Estimated tokens:** ~608,172 input + ~22,223 output = ~630,395 total
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
| `search_blocks` | 2 | 1 | 6 | 2 | 9 | 9 | 1,349 |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 206 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 2 | 2 | 6 | 2 | 10 | 10 | 438 |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **10** | **5** | **15** | **4** | **20** | **20** | **1,993** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_4 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |

#### Properties (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_28 |  | query_thermoml_parallel, resolve_property_ids, search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |

#### References (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2432 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2825 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_7085 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8254 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8424 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8869 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8888 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_9571 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_10866 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2395 |  | query_thermoml_parallel, search_blocks |

#### Measurements (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_280 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_207 | Excess molar volume, m3/mol | query_thermoml_parallel, search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | query_thermoml_parallel, search_blocks |
| GLOBsolvent_3 |  | query_thermoml_parallel, search_blocks |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBvar_3 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBvar_4 | Molality, mol/kg | query_thermoml_parallel, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_18 | Volume fraction | query_thermoml_parallel, search_blocks |

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
| Unique Compounds | 2 |
| Unique Properties | 2 |
| Unique References | 10 |
| Unique Measurements | 7 |
| Unique Phases | 1 |
| Unique Solvents | 2 |
| Unique Variables | 6 |
| Unique Constraints | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 10 |
| Unique parent blocks | 10 |
| Explicit block/subsystem targets | 10 |
| Subsystem targets | 0 |
| Target-matched data points | 3,110 |

---

## 3. DOI & Block References

**Unique DOIs:** 10  |  **Parent blocks:** 10  |  **Explicit targets:** 10  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,555

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2004.03.011 | 1 | 206 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 596 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2007.05.004 | 1 | 39 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je034101z | 1 | 401 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je049691v | 1 | 180 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je0600810 | 1 | 9 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je0601098 | 1 | 12 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je2003622 | 1 | 16 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je700300y | 1 | 84 | binary | query_thermoml_parallel, search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2004.03.011 | PROPblock_1 | declared | 206 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | 2 | query_thermoml_parallel, search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume_dir… | 132 | — | — | 0.0 |
| 2 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 175 | KEEP ←in 277 | 175 | 4.1 |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve water and m… | 193 | KEEP ←in 277 | 193 | 3.8 |
| 4 | 3 | `resolve_property_ids` | limit=5, min_score=50, purpose=Find the global pro… | 200 | KEEP ←in 227 | 200 | 3.4 |
| 5 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 979 | KEEP ←in 3,972 | 964 | 15.2 |
| 6 | 6 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2395,… | 375 | — | — | 0.1 |
| 7 | 7 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2395,… | 2,077 | — | — | 0.2 |
| 8 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 1,960 | KEEP ←in 5,885 | 1960 | 41.0 |
| 9 | 6 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 247 | — | — | 0.0 |
| 10 | 7 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 364 | — | — | 0.1 |
| 11 | 8 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 958 | — | — | 0.1 |
| 12 | 9 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_8424,… | 836 | — | — | 0.5 |
| 13 | 10 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_10866… | 966 | — | — | 0.2 |
| 14 | 11 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2432,… | 878 | — | — | 0.2 |
| 15 | 12 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_7085,… | 859 | — | — | 0.1 |
| 16 | 2 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume', '… | 96,814 | — | — | 242.1 |
| 17 | 5 | `inspect_block` | block_number=PROPblock_10, doi=10.1016/j.jct.2007.… | 1,360 | — | — | 0.2 |
| 18 | 9 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 237 | — | — | 0.1 |
| 19 | 11 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 954 | — | — | 1.7 |
| 20 | 12 | `predict_from_rk` | coeffs=[-3.98239e-06, -1.5386e-07, 1…, n_points=20… | 207 | — | — | 0.1 |
| 21 | 13 | `list_session_files` |  | 1,681 | — | — | 0.0 |
| | | **TOTAL (21 tools)** | | **112,452** | | **3,492** | **313.2** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 710 | 23,228 | 1,660 | 10.4 |
| 2 | L0-main | claudeopus46 | 22,518 | 1,171 | 23,689 | 1,124 | 7.0 |
| 3 | L1-worker | claudeopus46 | 24,095 | 822 | 24,917 | 585 | 4.4 |
| 4 | L1-worker | claudeopus46 | 24,095 | 839 | 24,934 | 738 | 5.5 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,834 | 25,929 | 513 | 4.0 |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,857 | 25,952 | 518 | 3.7 |
| 7 | L1-worker | claudeopus46 | 3,767 | 432 | 4,199 | 307 | 4.0 |
| 8 | L1-worker | claudeopus46 | 3,767 | 438 | 4,205 | 330 | 3.6 |
| 9 | L1-worker | claudeopus46 | 24,095 | 1,445 | 25,540 | 623 | 5.2 |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,417 | 25,512 | 893 | 7.0 |
| 11 | L1-worker | claudeopus46 | 3,767 | 406 | 4,173 | 304 | 3.3 |
| 12 | L1-worker | claudeopus46 | 24,095 | 2,156 | 26,251 | 727 | 5.1 |
| 13 | L1-worker | claudeopus46 | 24,095 | 1,930 | 26,025 | 804 | 6.6 |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,660 | 26,755 | 667 | 5.3 |
| 15 | L1-worker | claudeopus46 | 3,767 | 6,414 | 10,181 | 1,531 | 14.7 |
| 16 | L1-worker | claudeopus46 | 3,767 | 4,456 | 8,223 | 1,408 | 14.7 |
| 17 | L1-worker | claudeopus46 | 24,095 | 3,628 | 27,723 | 697 | 6.7 |
| 18 | L1-worker | claudeopus46 | 24,095 | 4,368 | 28,463 | 673 | 5.4 |
| 19 | L1-worker | claudeopus46 | 3,767 | 6,837 | 10,604 | 2,157 | 18.4 |
| 20 | L1-worker | claudeopus46 | 24,095 | 6,740 | 30,835 | 2,222 | 18.4 |
| 21 | L1-worker | claudeopus46 | 2,106 | 3,313 | 5,419 | 790 | 4.9 |
| 22 | L1-worker | claudeopus46 | 24,095 | 4,066 | 28,161 | 2,984 | 19.5 |
| 23 | L1-worker | claudeopus46 | 2,320 | 2,353 | 4,673 | 1,018 | 6.3 |
| 24 | L1-worker | claudeopus46 | 627 | 2,233 | 2,860 | 736 | 6.7 |
| 25 | L1-worker | claudeopus46 | 366 | 1,567 | 1,933 | 556 | 3.5 |
| 26 | L1-worker | claudeopus46 | 366 | 1,455 | 1,821 | 973 | 5.3 |
| 27 | L1-worker | claudeopus46 | 24,095 | 11,143 | 35,238 | 964 | 10.4 |
| 28 | L1-worker | claudeopus46 | 787 | 12,863 | 13,650 | 511 | 6.0 |
| 29 | L1-worker | claudeopus46 | 24,095 | 11,767 | 35,862 | 635 | 5.7 |
| 30 | L1-worker | claudeopus46 | 24,095 | 12,437 | 36,532 | 639 | 5.4 |
| 31 | L1-worker | claudeopus46 | 24,095 | 13,717 | 37,812 | 1,348 | 9.8 |
| 32 | L1-worker | claudeopus46 | 24,095 | 14,932 | 39,027 | 3,371 | 22.1 |
| 33 | L1-worker | claudeopus46 | 24,095 | 16,273 | 40,368 | 1,082 | 9.1 |
| 34 | L1-worker | claudeopus46 | 24,095 | 17,536 | 41,631 | 555 | 5.2 |
| 35 | L1-worker | claudeopus46 | 24,062 | 18,534 | 42,596 | 3,638 | 28.2 |
| 36 | L1-worker | claudeopus46 | 24,062 | 22,182 | 46,244 | 3,174 | 23.1 |
| 37 | L1-worker | claudeopus46 | 2,320 | 3,816 | 6,136 | 1,088 | 8.5 |
| 38 | L1-worker | claudeopus46 | 366 | 1,525 | 1,891 | 1,043 | 4.2 |
| 39 | L1-worker | claudeopus46 | 627 | 3,696 | 4,323 | 1,670 | 13.2 |
| 40 | L1-worker | claudeopus46 | 2,106 | 4,759 | 6,865 | 2,942 | 13.6 |
| 41 | L1-worker | claudeopus46 | 366 | 3,719 | 4,085 | 2,383 | 10.3 |
| 42 | L1-worker | claudeopus46 | 787 | 61,685 | 62,472 | 814 | 8.4 |
| 43 | L0-main | claudeopus46 | 22,518 | 75,292 | 97,810 | 1,922 | 17.1 |
| 44 | L0-main | claudeopus46 | 22,518 | 76,095 | 98,613 | 808 | 7.0 |
| 45 | L0-main | claudeopus46 | 22,518 | 76,892 | 99,410 | 531 | 4.7 |
| 46 | L0-main | claudeopus46 | 22,518 | 78,384 | 100,902 | 1,560 | 12.2 |
| 47 | L0-main | claudeopus46 | 22,518 | 79,146 | 101,664 | 837 | 6.5 |
| 48 | L0-main | claudeopus46 | 22,518 | 79,828 | 102,346 | 827 | 8.2 |
| 49 | L0-main | claudeopus46 | 22,518 | 80,546 | 103,064 | 768 | 5.8 |
| 50 | L0-main | claudeopus46 | 22,518 | 80,254 | 102,772 | 1,048 | 8.5 |
| 51 | L0-main | claudeopus46 | 22,518 | 81,018 | 103,536 | 825 | 6.3 |
| 52 | L0-main | claudeopus46 | 22,518 | 83,465 | 105,983 | 1,284 | 10.7 |
| 53 | L0-main | claudeopus46 | 22,518 | 84,077 | 106,595 | 3,769 | 28.0 |
| 54 | L0-main | claudeopus46 | 22,518 | 86,081 | 108,599 | 6,725 | 54.0 |
| 55 | L0-main | claudeopus46 | 22,518 | 98,247 | 120,765 | 5,577 | 45.9 |
| 56 | L0-main | claudeopus46 | 22,518 | 108,190 | 130,708 | 5,490 | 44.7 |
| 57 | L0-main | claudeopus46 | 2,106 | 6,236 | 8,342 | 274 | 3.0 |
| 58 | L0-main | claudeopus46 | 366 | 797 | 1,163 | 260 | 2.5 |
| 59 | L0-main | claudeopus46 | 2,320 | 5,427 | 7,747 | 1,430 | 11.7 |
| 60 | L0-main | claudeopus46 | 366 | 1,867 | 2,233 | 1,375 | 5.7 |
| 61 | L0-main | claudeopus46 | 560 | 6,234 | 6,794 | 186 | 2.9 |
| 62 | L0-main | claudeopus46 | 1,156 | 7,703 | 8,859 | 973 | 8.1 |
| 63 | L0-main | claudeopus46 | 1,918 | 5,930 | 7,848 | 1,029 | 10.5 |

