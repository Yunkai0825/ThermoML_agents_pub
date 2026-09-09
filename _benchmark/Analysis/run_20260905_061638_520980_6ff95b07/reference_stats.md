# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:16:38
**Wall time (at last flush):** 767.0 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 29 | 504,188 | 1,145,206 | 44,479 | 1,649,394 | 56,875 | 372.3 | claudeopus46 |
| L1-worker | 43 | 633,010 | 359,333 | 54,924 | 992,343 | 23,077 | 403.6 | claudeopus46 |
| **TOTAL** | **72** | **1,137,198** | **1,504,539** | **99,403** | **2,641,737** | **36,690** | **775.9** | |

**Estimated tokens:** ~660,434 input + ~24,850 output = ~685,284 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 3 | 10 | 10 | 334 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 4 | 3 | 6 | 6 | 2 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 1 | 3 | 3 | 64 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 4 | 1 | 3 | 3 | 0 |
| **TOTAL** | **12** | **4** | **16** | **8** | **22** | **22** | **400** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_4 |  | query_thermoml, resolve_compound_ids, search_blocks |

#### References (12 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2825 |  | query_thermoml, search_blocks |
| GLOBlit_5201 |  | query_thermoml, search_blocks |
| GLOBlit_7178 |  | query_thermoml, search_blocks |
| GLOBlit_7448 |  | query_thermoml, search_blocks |
| GLOBlit_7676 |  | query_thermoml, search_blocks |
| GLOBlit_10159 |  | query_thermoml, search_blocks |
| GLOBlit_10699 |  | search_blocks |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | search_blocks |
| GLOBlit_11792 |  | search_blocks |
| GLOBlit_8869 |  | query_thermoml, search_blocks |
| GLOBlit_9571 |  | query_thermoml, search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | query_thermoml, search_blocks |

#### Measurements (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_140 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_988 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_271 | Viscosity, Pa*s | query_thermoml, search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, search_blocks |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml, search_blocks |
| GLOBvar_4 | Molality, mol/kg | query_thermoml, search_blocks |
| GLOBvar_18 | Volume fraction | query_thermoml, search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks |
| GLOBconstr_8 | Molality, mol/kg | query_thermoml, search_blocks |
| GLOBconstr_2 | Temperature, K | query_thermoml, search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | query_thermoml, search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 3 |
| Unique References | 12 |
| Unique Properties | 1 |
| Unique Measurements | 7 |
| Unique Phases | 1 |
| Unique Variables | 5 |
| Unique Constraints | 3 |
| Unique Solvents | 1 |
| Unique Block_Types | 1 |
| Total DOIs | 12 |
| Unique parent blocks | 13 |
| Explicit block/subsystem targets | 13 |
| Subsystem targets | 0 |
| Target-matched data points | 641 |

---

## 3. DOI & Block References

**Unique DOIs:** 12  |  **Parent blocks:** 13  |  **Explicit targets:** 13  |  **Subsystems:** 0  |  **Target-matched datapoints:** 398

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2007.05.004 | 2 | 76 | binary | query_thermoml, search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 100 | binary | query_thermoml, search_blocks |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | query_thermoml, search_blocks |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | query_thermoml, search_blocks |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | query_thermoml, search_blocks |
| 10.1021/je0600810 | 1 | 9 | binary | query_thermoml, search_blocks |
| 10.1021/je2003622 | 1 | 16 | binary | query_thermoml, search_blocks |
| 10.1021/je4003515 | 1 | 25 | binary | query_thermoml, search_blocks |
| 10.1021/je600565m | 1 | 17 | binary | search_blocks |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks |
| 10.1021/je800150h | 1 | 108 | binary | search_blocks |
| 10.1021/je900743e | 1 | 15 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_9 | declared | 39 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_21 | declared | 100 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_11 | declared | 2 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | declared | 6 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_18 | declared | 9 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je0600810 | PROPblock_3 | declared | 9 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je2003622 | PROPblock_1 | declared | 16 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je4003515 | PROPblock_8 | declared | 25 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je600565m | PROPblock_5 | declared | 17 | binary | — | search_blocks |
| 10.1021/je700618y | PROPblock_7 | declared | 15 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_8 | declared | 108 | binary | — | search_blocks |
| 10.1021/je900743e | PROPblock_2 | declared | 15 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'ethanol_water_vis… | 224 | — | — | 0.0 |
| 2 | 2 | `query_thermoml_parallel` | queries=[{'label': 'ethanol_water_vis… | 132 | — | — | 0.0 |
| 3 | 3 | `query_thermoml_parallel` | queries=[{'label': 'ethanol_water_vis… | 153 | — | — | 0.0 |
| 4 | 1 | `resolve_compound_ids` | purpose=Find compound IDs for ethanol…, queries=['… | 195 | KEEP ←in 278 | 195 | 4.0 |
| 5 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,265 | KEEP ←in 6,284 | 1265 | 25.1 |
| 6 | 5 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2825… | 249 | — | — | 0.1 |
| 7 | 6 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2825… | 365 | — | — | 0.1 |
| 8 | 7 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2825… | 1,124 | — | — | 0.1 |
| 9 | 8 | `inspect_block_table` | block_number=PROPblock_21, literature=GLOBlit_5201… | 1,137 | — | — | 1.3 |
| 10 | 9 | `inspect_block_table` | block_number=PROPblock_47, literature=GLOBlit_7448… | 999 | — | — | 0.1 |
| 11 | 10 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_7676… | 1,131 | — | — | 0.1 |
| 12 | 11 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_10159… | 1,088 | — | — | 0.1 |
| 13 | 4 | `query_thermoml` | instruction=Search for binary mixture dat…, purpos… | 52,510 | — | — | 202.6 |
| 14 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve methanol an… | 180 | KEEP ←in 277 | 180 | 4.4 |
| 15 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=50, p… | 1,202 | KEEP ←in 6,223 | 1202 | 19.7 |
| 16 | 5 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2825,… | 261 | — | — | 0.3 |
| 17 | 6 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2825,… | 358 | — | — | 0.1 |
| 18 | 7 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2825,… | 1,522 | — | — | 0.4 |
| 19 | 8 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_8869,… | 970 | — | — | 1.1 |
| 20 | 9 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_9571,… | 1,043 | — | — | 0.1 |
| 21 | 5 | `query_thermoml` | instruction=Search for binary mixture dat…, purpos… | 29,175 | — | — | 186.0 |
| 22 | 8 | `fit_multi_system` | purpose=Fit Redlich-Kister polynomial…, systems=[{… | 544 | — | — | 0.2 |
| 23 | 10 | `inspect_block` | block_number=PROPblock_21, doi=10.1016/j.jct.2018.… | 1,363 | — | — | 0.7 |
| 24 | 14 | `inspect_block` | block_number=PROPblock_9, doi=10.1016/j.jct.2007.0… | 1,338 | — | — | 0.1 |
| 25 | 15 | `fit_multi_system` | purpose=Fit Arrhenius-RK viscosity mo…, systems=[{… | 1,181 | — | — | 3.0 |
| 26 | 17 | `predict_from_rk` | coeffs=[2.728, -2.49259, 2.55005, -2…, mixing_rule… | 214 | — | — | 0.1 |
| 27 | 19 | `predict_from_rk` | coeffs=[2.53477, 1.42214, 1.33593, 0…, mixing_rule… | 211 | — | — | 0.1 |
| | | **TOTAL (27 tools)** | | **100,134** | | **2,842** | **449.9** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 408 | 22,926 | 1,972 | 11.0 |
| 2 | L0-main | claudeopus46 | 22,518 | 931 | 23,449 | 1,190 | 7.0 |
| 3 | L0-main | claudeopus46 | 22,518 | 1,341 | 23,859 | 1,448 | 8.3 |
| 4 | L0-main | claudeopus46 | 22,518 | 1,765 | 24,283 | 707 | 5.9 |
| 5 | L1-worker | claudeopus46 | 24,095 | 865 | 24,960 | 611 | 4.2 |
| 6 | L1-worker | claudeopus46 | 3,767 | 474 | 4,241 | 359 | 3.8 |
| 7 | L1-worker | claudeopus46 | 24,095 | 1,318 | 25,413 | 801 | 5.6 |
| 8 | L1-worker | claudeopus46 | 24,095 | 2,043 | 26,138 | 659 | 4.8 |
| 9 | L1-worker | claudeopus46 | 3,767 | 6,756 | 10,523 | 1,541 | 15.4 |
| 10 | L1-worker | claudeopus46 | 24,095 | 3,301 | 27,396 | 2,681 | 16.9 |
| 11 | L1-worker | claudeopus46 | 24,095 | 9,033 | 33,128 | 1,202 | 9.7 |
| 12 | L1-worker | claudeopus46 | 24,095 | 9,708 | 33,803 | 553 | 4.5 |
| 13 | L1-worker | claudeopus46 | 24,095 | 10,352 | 34,447 | 768 | 7.8 |
| 14 | L1-worker | claudeopus46 | 24,095 | 11,793 | 35,888 | 562 | 5.0 |
| 15 | L1-worker | claudeopus46 | 24,095 | 13,223 | 37,318 | 587 | 5.5 |
| 16 | L1-worker | claudeopus46 | 24,095 | 14,547 | 38,642 | 401 | 3.8 |
| 17 | L1-worker | claudeopus46 | 24,095 | 15,979 | 40,074 | 589 | 6.0 |
| 18 | L1-worker | claudeopus46 | 24,095 | 17,371 | 41,466 | 4,036 | 29.6 |
| 19 | L1-worker | claudeopus46 | 24,062 | 25,021 | 49,083 | 4,229 | 29.6 |
| 20 | L1-worker | claudeopus46 | 2,320 | 4,360 | 6,680 | 1,192 | 6.9 |
| 21 | L1-worker | claudeopus46 | 2,106 | 5,346 | 7,452 | 2,074 | 9.0 |
| 22 | L1-worker | claudeopus46 | 627 | 4,240 | 4,867 | 1,468 | 10.0 |
| 23 | L1-worker | claudeopus46 | 366 | 1,629 | 1,995 | 1,142 | 4.4 |
| 24 | L1-worker | claudeopus46 | 366 | 2,851 | 3,217 | 1,602 | 7.0 |
| 25 | L1-worker | claudeopus46 | 1,228 | 7,860 | 9,088 | 1,752 | 10.5 |
| 26 | L1-worker | claudeopus46 | 787 | 45,732 | 46,519 | 678 | 7.8 |
| 27 | L0-main | claudeopus46 | 22,518 | 33,051 | 55,569 | 1,326 | 13.0 |
| 28 | L1-worker | claudeopus46 | 24,095 | 1,466 | 25,561 | 814 | 7.4 |
| 29 | L1-worker | claudeopus46 | 24,095 | 2,498 | 26,593 | 540 | 4.3 |
| 30 | L1-worker | claudeopus46 | 3,767 | 438 | 4,205 | 317 | 3.7 |
| 31 | L1-worker | claudeopus46 | 24,095 | 2,085 | 26,180 | 846 | 6.2 |
| 32 | L1-worker | claudeopus46 | 24,095 | 2,802 | 26,897 | 677 | 5.3 |
| 33 | L1-worker | claudeopus46 | 3,767 | 6,738 | 10,505 | 1,482 | 14.5 |
| 34 | L1-worker | claudeopus46 | 24,095 | 3,961 | 28,056 | 956 | 8.0 |
| 35 | L1-worker | claudeopus46 | 24,095 | 4,611 | 28,706 | 630 | 5.7 |
| 36 | L1-worker | claudeopus46 | 24,095 | 5,268 | 29,363 | 606 | 5.5 |
| 37 | L1-worker | claudeopus46 | 24,095 | 7,100 | 31,195 | 713 | 6.6 |
| 38 | L1-worker | claudeopus46 | 24,095 | 8,416 | 32,511 | 624 | 5.6 |
| 39 | L1-worker | claudeopus46 | 24,095 | 9,813 | 33,908 | 3,020 | 21.6 |
| 40 | L1-worker | claudeopus46 | 24,095 | 16,282 | 40,377 | 3,630 | 28.1 |
| 41 | L1-worker | claudeopus46 | 24,095 | 23,361 | 47,456 | 3,121 | 23.6 |
| 42 | L1-worker | claudeopus46 | 2,320 | 3,783 | 6,103 | 1,004 | 6.9 |
| 43 | L1-worker | claudeopus46 | 2,106 | 5,370 | 7,476 | 1,675 | 8.8 |
| 44 | L1-worker | claudeopus46 | 627 | 3,663 | 4,290 | 1,054 | 9.3 |
| 45 | L1-worker | claudeopus46 | 366 | 1,441 | 1,807 | 959 | 5.1 |
| 46 | L1-worker | claudeopus46 | 366 | 2,452 | 2,818 | 1,062 | 5.6 |
| 47 | L1-worker | claudeopus46 | 1,228 | 7,037 | 8,265 | 1,137 | 4.9 |
| 48 | L1-worker | claudeopus46 | 787 | 26,946 | 27,733 | 570 | 9.1 |
| 49 | L0-main | claudeopus46 | 22,518 | 54,142 | 76,660 | 3,102 | 22.4 |
| 50 | L0-main | claudeopus46 | 22,518 | 54,918 | 77,436 | 1,576 | 10.9 |
| 51 | L0-main | claudeopus46 | 22,518 | 55,694 | 78,212 | 1,276 | 13.1 |
| 52 | L0-main | claudeopus46 | 22,518 | 55,854 | 78,372 | 596 | 6.9 |
| 53 | L0-main | claudeopus46 | 22,518 | 56,537 | 79,055 | 544 | 7.1 |
| 54 | L0-main | claudeopus46 | 22,518 | 58,594 | 81,112 | 531 | 5.0 |
| 55 | L0-main | claudeopus46 | 22,518 | 59,270 | 81,788 | 493 | 21.2 |
| 56 | L0-main | claudeopus46 | 22,518 | 59,874 | 82,392 | 577 | 5.3 |
| 57 | L0-main | claudeopus46 | 22,518 | 60,549 | 83,067 | 422 | 3.6 |
| 58 | L0-main | claudeopus46 | 22,518 | 61,624 | 84,142 | 1,418 | 12.6 |
| 59 | L0-main | claudeopus46 | 22,518 | 65,728 | 88,246 | 2,174 | 17.6 |
| 60 | L0-main | claudeopus46 | 22,518 | 66,533 | 89,051 | 809 | 10.8 |
| 61 | L0-main | claudeopus46 | 22,518 | 66,794 | 89,312 | 721 | 7.6 |
| 62 | L0-main | claudeopus46 | 22,518 | 67,472 | 89,990 | 719 | 6.1 |
| 63 | L0-main | claudeopus46 | 22,518 | 67,720 | 90,238 | 6,879 | 47.3 |
| 64 | L0-main | claudeopus46 | 22,518 | 78,009 | 100,527 | 5,584 | 48.7 |
| 65 | L0-main | claudeopus46 | 22,518 | 86,522 | 109,040 | 4,858 | 36.1 |
| 66 | L0-main | claudeopus46 | 2,106 | 5,510 | 7,616 | 274 | 4.6 |
| 67 | L0-main | claudeopus46 | 366 | 797 | 1,163 | 260 | 2.6 |
| 68 | L0-main | claudeopus46 | 2,320 | 4,987 | 7,307 | 1,480 | 10.0 |
| 69 | L0-main | claudeopus46 | 366 | 1,917 | 2,283 | 1,435 | 5.0 |
| 70 | L0-main | claudeopus46 | 560 | 5,794 | 6,354 | 186 | 5.4 |
| 71 | L0-main | claudeopus46 | 1,156 | 7,253 | 8,409 | 818 | 5.9 |
| 72 | L0-main | claudeopus46 | 1,918 | 5,618 | 7,536 | 1,104 | 11.3 |

