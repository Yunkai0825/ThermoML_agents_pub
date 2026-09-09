# Reference Stats — analysis-agent

**Run started:** 2026-09-05 04:32:51
**Wall time (at last flush):** 543.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 21 | 324,044 | 1,153,389 | 41,564 | 1,477,433 | 70,353 | 333.7 | claudeopus46 |
| L1-worker | 46 | 642,554 | 338,178 | 52,351 | 980,732 | 21,320 | 378.2 | claudeopus46 |
| **TOTAL** | **67** | **966,598** | **1,491,567** | **93,915** | **2,458,165** | **36,689** | **711.9** | |

**Estimated tokens:** ~614,541 input + ~23,478 output = ~638,019 total
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
| `search_blocks` | 2 | 1 | 3 | 1 | 3 | 3 | 188 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 3 | 3 | 2 | 3 | 6 | 340 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 2 | 3 | 3 | 2 | 3 | 6 | 86 |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **10** | **8** | **9** | **5** | **9** | **15** | **614** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_15 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_18 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |

#### Properties (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_28 |  | resolve_property_ids |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBprop_8 | Speed of sound, m/s | query_thermoml_parallel, search_blocks |

#### References (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2659 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_4124 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_7481 |  | query_thermoml_parallel, search_blocks |

#### Measurements (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_153 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBmeas_18 | Speed of sound, m/s | query_thermoml_parallel, search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBconstr_4 | Frequency, MHz | query_thermoml_parallel, search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml_parallel |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique Properties | 4 |
| Unique References | 3 |
| Unique Measurements | 5 |
| Unique Phases | 1 |
| Unique Variables | 3 |
| Unique Constraints | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 3 |
| Unique parent blocks | 6 |
| Explicit block/subsystem targets | 6 |
| Subsystem targets | 0 |
| Target-matched data points | 868 |

---

## 3. DOI & Block References

**Unique DOIs:** 3  |  **Parent blocks:** 6  |  **Explicit targets:** 6  |  **Subsystems:** 0  |  **Target-matched datapoints:** 340

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2006.01.015 | 1 | 102 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2014.02.019 | 2 | 40 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/acs.jced.8b00176 | 3 | 198 | binary | query_thermoml_parallel, search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2006.01.015 | PROPblock_7 | declared | 102 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2014.02.019 | PROPblock_5 | declared | 20 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2014.02.019 | PROPblock_6 | declared | 20 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/acs.jced.8b00176 | PROPblock_16 | declared | 66 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/acs.jced.8b00176 | PROPblock_17 | declared | 66 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/acs.jced.8b00176 | PROPblock_18 | declared | 66 | binary | 2 | query_thermoml_parallel, search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 132 | — | — | 0.0 |
| 2 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 213 | KEEP ←in 308 | 213 | 3.8 |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 208 | KEEP ←in 308 | 208 | 4.2 |
| 4 | 3 | `resolve_property_ids` | limit=5, min_score=50, purpose=Find the global pro… | 237 | KEEP ←in 227 | 237 | 4.0 |
| 5 | 5 | `search_blocks` | compound=['GLOBcomp_15', 'GLOBcomp_18'], limit=50,… | 1,026 | KEEP ←in 6,590 | 1169 | 10.1 |
| 6 | 4 | `search_blocks` | compound=['GLOBcomp_15', 'GLOBcomp_18'], limit=50,… | 1,169 | DISCARD ←in 39 | 968 | 19.6 |
| 7 | 6 | `inspect_block_table` | block_number=PROPblock_7, literature=GLOBlit_2659,… | 357 | — | — | 0.7 |
| 8 | 7 | `inspect_block_table` | block_number=PROPblock_7, literature=GLOBlit_2659,… | 1,682 | — | — | 0.1 |
| 9 | 6 | `search_blocks` | compound=['GLOBcomp_15', 'GLOBcomp_18'], limit=50,… | 1,009 | DISCARD ←in 39 | 951 | 20.9 |
| 10 | 8 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_4124,… | 1,096 | — | — | 0.1 |
| 11 | 9 | `inspect_block_table` | block_number=PROPblock_16, literature=GLOBlit_7481… | 1,424 | — | — | 0.3 |
| 12 | 7 | `search_blocks` | compound=['GLOBcomp_15', 'GLOBcomp_18'], limit=20,… | 1,291 | KEEP ←in 9,352 | 1201 | 12.5 |
| 13 | 9 | `inspect_block_table` | block_number=PROPblock_7, literature=GLOBlit_2659,… | 2,181 | — | — | 0.1 |
| 14 | 10 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_4124,… | 1,306 | — | — | 0.1 |
| 15 | 11 | `inspect_block_table` | block_number=PROPblock_16, literature=GLOBlit_7481… | 2,245 | — | — | 0.2 |
| 16 | 12 | `inspect_block_table` | block_number=PROPblock_17, literature=GLOBlit_7481… | 1,806 | — | — | 0.2 |
| 17 | 2 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 112,499 | — | — | 210.2 |
| 18 | 4 | `fit_block_derived` | block_number=PROPblock_7, composition_hint=mole_fr… | 243 | — | — | 0.1 |
| 19 | 6 | `fit_block_derived` | block_number=PROPblock_7, composition_hint=mole_fr… | 1,004 | — | — | 1.7 |
| 20 | 8 | `fit_block_derived` | block_number=PROPblock_16, composition_hint=mole_f… | 946 | — | — | 1.8 |
| 21 | 10 | `predict_from_rk` | coeffs=[-1.13034e-06, -7.63893e-07, …, mixing_rule… | 221 | — | — | 0.1 |
| 22 | 11 | `list_session_files` |  | 3,133 | — | — | 0.0 |
| | | **TOTAL (22 tools)** | | **135,428** | | **4,947** | **290.8** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 808 | 23,326 | 1,554 | 10.7 |
| 2 | L0-main | claudeopus46 | 22,518 | 1,232 | 23,750 | 1,263 | 7.5 |
| 3 | L1-worker | claudeopus46 | 24,095 | 919 | 25,014 | 596 | 4.6 |
| 4 | L1-worker | claudeopus46 | 24,095 | 869 | 24,964 | 669 | 5.5 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,971 | 26,066 | 591 | 4.5 |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,921 | 26,016 | 579 | 4.3 |
| 7 | L1-worker | claudeopus46 | 3,767 | 483 | 4,250 | 332 | 3.7 |
| 8 | L1-worker | claudeopus46 | 3,767 | 483 | 4,250 | 382 | 4.0 |
| 9 | L1-worker | claudeopus46 | 24,095 | 1,584 | 25,679 | 855 | 6.4 |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,517 | 25,612 | 853 | 6.8 |
| 11 | L1-worker | claudeopus46 | 3,767 | 396 | 4,163 | 343 | 3.9 |
| 12 | L1-worker | claudeopus46 | 24,095 | 2,244 | 26,339 | 642 | 4.8 |
| 13 | L1-worker | claudeopus46 | 24,095 | 2,155 | 26,250 | 849 | 6.4 |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,912 | 27,007 | 681 | 5.2 |
| 15 | L1-worker | claudeopus46 | 3,767 | 7,072 | 10,839 | 1,465 | 13.7 |
| 16 | L1-worker | claudeopus46 | 3,767 | 573 | 4,340 | 1,262 | 9.6 |
| 17 | L1-worker | claudeopus46 | 24,095 | 3,926 | 28,021 | 955 | 7.9 |
| 18 | L1-worker | claudeopus46 | 24,095 | 3,379 | 27,474 | 2,206 | 13.7 |
| 19 | L1-worker | claudeopus46 | 24,095 | 8,732 | 32,827 | 556 | 5.9 |
| 20 | L1-worker | claudeopus46 | 24,095 | 9,379 | 33,474 | 533 | 5.2 |
| 21 | L1-worker | claudeopus46 | 3,767 | 541 | 4,308 | 1,291 | 9.6 |
| 22 | L1-worker | claudeopus46 | 24,095 | 11,351 | 35,446 | 553 | 5.8 |
| 23 | L1-worker | claudeopus46 | 24,095 | 5,291 | 29,386 | 1,141 | 7.3 |
| 24 | L1-worker | claudeopus46 | 24,095 | 12,757 | 36,852 | 438 | 4.3 |
| 25 | L1-worker | claudeopus46 | 3,767 | 9,732 | 13,499 | 1,492 | 11.5 |
| 26 | L1-worker | claudeopus46 | 24,095 | 14,477 | 38,572 | 2,207 | 17.8 |
| 27 | L1-worker | claudeopus46 | 24,095 | 6,947 | 31,042 | 2,414 | 13.8 |
| 28 | L1-worker | claudeopus46 | 24,095 | 12,170 | 36,265 | 1,380 | 11.2 |
| 29 | L1-worker | claudeopus46 | 24,095 | 20,365 | 44,460 | 3,502 | 25.8 |
| 30 | L1-worker | claudeopus46 | 24,095 | 14,663 | 38,758 | 861 | 8.8 |
| 31 | L1-worker | claudeopus46 | 627 | 3,271 | 3,898 | 959 | 6.9 |
| 32 | L1-worker | claudeopus46 | 24,095 | 16,317 | 40,412 | 572 | 4.9 |
| 33 | L1-worker | claudeopus46 | 2,320 | 3,391 | 5,711 | 1,189 | 8.6 |
| 34 | L1-worker | claudeopus46 | 2,106 | 4,381 | 6,487 | 1,830 | 9.3 |
| 35 | L1-worker | claudeopus46 | 366 | 1,370 | 1,736 | 946 | 4.6 |
| 36 | L1-worker | claudeopus46 | 366 | 1,626 | 1,992 | 1,118 | 4.8 |
| 37 | L1-worker | claudeopus46 | 366 | 2,607 | 2,973 | 1,045 | 4.8 |
| 38 | L1-worker | claudeopus46 | 24,095 | 18,857 | 42,952 | 598 | 7.6 |
| 39 | L1-worker | claudeopus46 | 787 | 26,646 | 27,433 | 874 | 9.0 |
| 40 | L1-worker | claudeopus46 | 24,062 | 20,655 | 44,717 | 3,115 | 22.1 |
| 41 | L1-worker | claudeopus46 | 24,062 | 22,581 | 46,643 | 2,565 | 17.9 |
| 42 | L1-worker | claudeopus46 | 2,320 | 2,696 | 5,016 | 772 | 5.4 |
| 43 | L1-worker | claudeopus46 | 627 | 2,576 | 3,203 | 793 | 6.2 |
| 44 | L1-worker | claudeopus46 | 366 | 1,209 | 1,575 | 737 | 3.5 |
| 45 | L1-worker | claudeopus46 | 366 | 1,204 | 1,570 | 780 | 4.6 |
| 46 | L1-worker | claudeopus46 | 2,106 | 3,736 | 5,842 | 2,532 | 11.5 |
| 47 | L1-worker | claudeopus46 | 366 | 3,309 | 3,675 | 1,751 | 8.3 |
| 48 | L1-worker | claudeopus46 | 787 | 42,937 | 43,724 | 547 | 6.2 |
| 49 | L0-main | claudeopus46 | 22,518 | 83,464 | 105,982 | 2,068 | 17.0 |
| 50 | L0-main | claudeopus46 | 22,518 | 84,267 | 106,785 | 1,111 | 8.6 |
| 51 | L0-main | claudeopus46 | 22,518 | 84,627 | 107,145 | 1,009 | 8.0 |
| 52 | L0-main | claudeopus46 | 22,518 | 85,392 | 107,910 | 1,266 | 9.9 |
| 53 | L0-main | claudeopus46 | 22,518 | 87,877 | 110,395 | 1,042 | 12.2 |
| 54 | L0-main | claudeopus46 | 22,518 | 88,690 | 111,208 | 801 | 6.1 |
| 55 | L0-main | claudeopus46 | 22,518 | 91,022 | 113,540 | 1,715 | 13.8 |
| 56 | L0-main | claudeopus46 | 22,518 | 91,827 | 114,345 | 1,131 | 9.2 |
| 57 | L0-main | claudeopus46 | 22,518 | 92,059 | 114,577 | 3,008 | 27.1 |
| 58 | L0-main | claudeopus46 | 22,518 | 95,540 | 118,058 | 8,083 | 61.7 |
| 59 | L0-main | claudeopus46 | 22,518 | 109,532 | 132,050 | 6,233 | 49.5 |
| 60 | L0-main | claudeopus46 | 22,518 | 121,737 | 144,255 | 6,121 | 48.6 |
| 61 | L0-main | claudeopus46 | 2,106 | 6,615 | 8,721 | 273 | 4.2 |
| 62 | L0-main | claudeopus46 | 366 | 796 | 1,162 | 259 | 2.6 |
| 63 | L0-main | claudeopus46 | 2,320 | 5,708 | 8,028 | 1,268 | 9.8 |
| 64 | L0-main | claudeopus46 | 366 | 1,705 | 2,071 | 1,223 | 5.6 |
| 65 | L0-main | claudeopus46 | 560 | 6,514 | 7,074 | 185 | 2.6 |
| 66 | L0-main | claudeopus46 | 1,156 | 7,997 | 9,153 | 819 | 7.9 |
| 67 | L0-main | claudeopus46 | 1,918 | 5,980 | 7,898 | 1,132 | 11.1 |

