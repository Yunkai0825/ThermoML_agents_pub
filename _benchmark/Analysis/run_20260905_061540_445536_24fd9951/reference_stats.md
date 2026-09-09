# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:15:40
**Wall time (at last flush):** 517.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 21 | 324,044 | 793,814 | 47,610 | 1,117,858 | 53,231 | 343.2 | claudeopus46 |
| L1-worker | 50 | 599,325 | 236,665 | 54,291 | 835,990 | 16,719 | 407.5 | claudeopus46 |
| **TOTAL** | **71** | **923,369** | **1,030,479** | **101,901** | **1,953,848** | **27,518** | **750.7** | |

**Estimated tokens:** ~488,462 input + ~25,475 output = ~513,937 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 1 | 4 | 4 | 76 |
| `search_blocks` | 2 | 1 | 3 | 2 | 7 | 7 | 302 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 12 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 3 | 1 | 3 | 2 | 4 | 4 | 0 |
| **TOTAL** | **15** | **4** | **12** | **6** | **16** | **16** | **390** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_4 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_24 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |

#### References (12 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2825 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_5533 |  | search_blocks |
| GLOBlit_8869 |  | search_blocks |
| GLOBlit_9571 |  | search_blocks |
| GLOBlit_2656 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_5201 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_6951 |  | search_blocks |
| GLOBlit_8038 |  | search_blocks |
| GLOBlit_8106 |  | search_blocks |
| GLOBlit_11186 |  | search_blocks |
| GLOBlit_11506 |  | search_blocks |
| GLOBlit_692 |  | query_thermoml_parallel, search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |

#### Measurements (8 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_140 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_271 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBmeas_227 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks |

#### Variables (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_18 | Volume fraction | search_blocks |

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
| Unique References | 12 |
| Unique Properties | 1 |
| Unique Measurements | 8 |
| Unique Phases | 1 |
| Unique Variables | 4 |
| Unique Constraints | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 12 |
| Unique parent blocks | 12 |
| Explicit block/subsystem targets | 12 |
| Subsystem targets | 0 |
| Target-matched data points | 535 |

---

## 3. DOI & Block References

**Unique DOIs:** 12  |  **Parent blocks:** 12  |  **Explicit targets:** 12  |  **Subsystems:** 0  |  **Target-matched datapoints:** 390

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2009.03.002 | 1 | 12 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2006.01.011 | 1 | 10 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2007.05.004 | 1 | 39 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 84 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2019.05.013 | 1 | 12 | binary | search_blocks |
| 10.1021/acs.jced.6b00526 | 1 | 33 | binary | search_blocks |
| 10.1021/je020140j | 1 | 77 | binary | search_blocks |
| 10.1021/je025610o | 1 | 30 | binary | search_blocks |
| 10.1021/je0600810 | 1 | 9 | binary | search_blocks |
| 10.1021/je2003622 | 1 | 16 | binary | search_blocks |
| 10.1021/je800271e | 1 | 52 | binary | search_blocks |
| 10.1021/je9000697 | 1 | 16 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2009.03.002 | PROPblock_1 | declared | 12 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2006.01.011 | PROPblock_13 | declared | 10 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_9 | declared | 39 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_24 | declared | 84 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2019.05.013 | PROPblock_3 | declared | 12 | binary | — | search_blocks |
| 10.1021/acs.jced.6b00526 | PROPblock_18 | declared | 33 | binary | — | search_blocks |
| 10.1021/je020140j | PROPblock_5 | declared | 77 | binary | — | search_blocks |
| 10.1021/je025610o | PROPblock_5 | declared | 30 | binary | — | search_blocks |
| 10.1021/je0600810 | PROPblock_3 | declared | 9 | binary | — | search_blocks |
| 10.1021/je2003622 | PROPblock_1 | declared | 16 | binary | — | search_blocks |
| 10.1021/je800271e | PROPblock_4 | declared | 52 | binary | — | search_blocks |
| 10.1021/je9000697 | PROPblock_1 | declared | 16 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'EG_water_visc', '… | 209 | — | — | 0.0 |
| 2 | 2 | `query_thermoml_parallel` | queries=[{'label': 'EG_water_visc', '… | 132 | — | — | 0.0 |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve water and m… | 194 | KEEP ←in 277 | 194 | 4.3 |
| 4 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 212 | KEEP ←in 288 | 212 | 5.4 |
| 5 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 218 | KEEP ←in 293 | 218 | 5.0 |
| 6 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 572 | KEEP ←in 8,146 | 572 | 15.3 |
| 7 | 4 | `search_blocks` | compound=['GLOBcomp_24', 'GLOBcomp_4'], limit=50, … | 1,207 | KEEP ←in 2,201 | 1193 | 13.5 |
| 8 | 4 | `search_blocks` | compound=['GLOBcomp_24', 'GLOBcomp_1'], limit=50, … | 715 | KEEP ←in 9,915 | 715 | 15.9 |
| 9 | 6 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_692, … | 1,254 | — | — | 0.4 |
| 10 | 6 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2825,… | 1,677 | — | — | 0.5 |
| 11 | 6 | `inspect_block_table` | block_number=PROPblock_13, literature=GLOBlit_2656… | 1,253 | — | — | 0.4 |
| 12 | 7 | `inspect_block_table` | block_number=PROPblock_24, literature=GLOBlit_5201… | 1,481 | — | — | 0.6 |
| 13 | 3 | `query_thermoml_parallel` | queries=[{'label': 'EG_water_viscosit… | 60,691 | — | — | 172.7 |
| 14 | 6 | `fit_multi_system` | purpose=Fit Redlich-Kister polynomial…, systems=[{… | 624 | — | — | 0.4 |
| 15 | 9 | `fit_multi_system` | purpose=Fit Arrhenius-RK viscosity mo…, systems=[{… | 1,415 | — | — | 2.7 |
| 16 | 10 | `fit_block` | block_number=PROPblock_1, composition_hint=mole_fr… | 251 | — | — | 0.3 |
| 17 | 11 | `fit_block` | block_number=PROPblock_1, composition_hint=mass_fr… | 650 | — | — | 1.7 |
| | | **TOTAL (17 tools)** | | **72,755** | | **3,104** | **239.1** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 362 | 22,880 | 2,288 | 12.7 |
| 2 | L0-main | claudeopus46 | 22,518 | 1,004 | 23,522 | 1,711 | 9.6 |
| 3 | L0-main | claudeopus46 | 22,518 | 1,433 | 23,951 | 1,584 | 8.7 |
| 4 | L1-worker | claudeopus46 | 24,095 | 852 | 24,947 | 669 | 4.9 |
| 5 | L1-worker | claudeopus46 | 24,095 | 846 | 24,941 | 687 | 5.5 |
| 6 | L1-worker | claudeopus46 | 24,095 | 815 | 24,910 | 672 | 6.4 |
| 7 | L1-worker | claudeopus46 | 24,095 | 1,833 | 25,928 | 543 | 3.7 |
| 8 | L1-worker | claudeopus46 | 24,095 | 1,912 | 26,007 | 588 | 4.5 |
| 9 | L1-worker | claudeopus46 | 24,095 | 1,911 | 26,006 | 585 | 6.4 |
| 10 | L1-worker | claudeopus46 | 3,767 | 438 | 4,205 | 375 | 3.6 |
| 11 | L1-worker | claudeopus46 | 3,767 | 472 | 4,239 | 371 | 4.3 |
| 12 | L1-worker | claudeopus46 | 3,767 | 485 | 4,252 | 413 | 4.3 |
| 13 | L1-worker | claudeopus46 | 24,095 | 1,447 | 25,542 | 925 | 6.7 |
| 14 | L1-worker | claudeopus46 | 24,095 | 1,493 | 25,588 | 904 | 6.4 |
| 15 | L1-worker | claudeopus46 | 24,095 | 1,509 | 25,604 | 929 | 6.7 |
| 16 | L1-worker | claudeopus46 | 24,095 | 2,193 | 26,288 | 641 | 5.2 |
| 17 | L1-worker | claudeopus46 | 24,095 | 2,228 | 26,323 | 719 | 4.7 |
| 18 | L1-worker | claudeopus46 | 24,095 | 2,223 | 26,318 | 677 | 4.9 |
| 19 | L1-worker | claudeopus46 | 3,767 | 8,619 | 12,386 | 1,656 | 14.2 |
| 20 | L1-worker | claudeopus46 | 3,767 | 2,718 | 6,485 | 1,508 | 11.7 |
| 21 | L1-worker | claudeopus46 | 3,767 | 10,434 | 14,201 | 1,661 | 14.5 |
| 22 | L1-worker | claudeopus46 | 24,095 | 3,395 | 27,490 | 1,803 | 16.1 |
| 23 | L1-worker | claudeopus46 | 24,095 | 2,738 | 26,833 | 2,795 | 17.0 |
| 24 | L1-worker | claudeopus46 | 24,095 | 2,889 | 26,984 | 3,018 | 18.9 |
| 25 | L1-worker | claudeopus46 | 24,095 | 8,037 | 32,132 | 585 | 5.6 |
| 26 | L1-worker | claudeopus46 | 24,095 | 7,783 | 31,878 | 826 | 7.4 |
| 27 | L1-worker | claudeopus46 | 24,095 | 8,847 | 32,942 | 1,518 | 10.5 |
| 28 | L1-worker | claudeopus46 | 24,095 | 10,445 | 34,540 | 637 | 5.7 |
| 29 | L1-worker | claudeopus46 | 24,095 | 9,734 | 33,829 | 1,932 | 13.5 |
| 30 | L1-worker | claudeopus46 | 24,095 | 9,572 | 33,667 | 2,317 | 17.2 |
| 31 | L1-worker | claudeopus46 | 2,320 | 2,063 | 4,383 | 731 | 4.9 |
| 32 | L1-worker | claudeopus46 | 2,106 | 2,999 | 5,105 | 499 | 4.7 |
| 33 | L1-worker | claudeopus46 | 2,106 | 3,421 | 5,527 | 482 | 4.4 |
| 34 | L1-worker | claudeopus46 | 2,320 | 2,448 | 4,768 | 819 | 5.4 |
| 35 | L1-worker | claudeopus46 | 627 | 1,943 | 2,570 | 840 | 6.4 |
| 36 | L1-worker | claudeopus46 | 627 | 2,328 | 2,955 | 829 | 6.5 |
| 37 | L1-worker | claudeopus46 | 366 | 1,276 | 1,642 | 372 | 2.8 |
| 38 | L1-worker | claudeopus46 | 366 | 1,168 | 1,534 | 719 | 3.6 |
| 39 | L1-worker | claudeopus46 | 366 | 1,259 | 1,625 | 380 | 3.2 |
| 40 | L1-worker | claudeopus46 | 366 | 1,256 | 1,622 | 784 | 3.8 |
| 41 | L1-worker | claudeopus46 | 1,228 | 4,202 | 5,430 | 406 | 2.9 |
| 42 | L1-worker | claudeopus46 | 787 | 11,321 | 12,108 | 604 | 7.5 |
| 43 | L1-worker | claudeopus46 | 24,095 | 12,262 | 36,357 | 2,428 | 18.9 |
| 44 | L1-worker | claudeopus46 | 787 | 12,282 | 13,069 | 529 | 6.4 |
| 45 | L1-worker | claudeopus46 | 24,095 | 18,334 | 42,429 | 3,916 | 29.0 |
| 46 | L1-worker | claudeopus46 | 627 | 4,426 | 5,053 | 1,057 | 9.6 |
| 47 | L1-worker | claudeopus46 | 2,320 | 4,546 | 6,866 | 1,019 | 12.4 |
| 48 | L1-worker | claudeopus46 | 366 | 1,456 | 1,822 | 974 | 4.0 |
| 49 | L1-worker | claudeopus46 | 2,106 | 5,513 | 7,619 | 2,608 | 16.8 |
| 50 | L1-worker | claudeopus46 | 366 | 3,385 | 3,751 | 1,598 | 6.7 |
| 51 | L1-worker | claudeopus46 | 1,228 | 8,054 | 9,282 | 1,127 | 5.2 |
| 52 | L1-worker | claudeopus46 | 366 | 1,904 | 2,270 | 820 | 4.0 |
| 53 | L1-worker | claudeopus46 | 787 | 22,951 | 23,738 | 796 | 7.9 |
| 54 | L0-main | claudeopus46 | 22,518 | 59,620 | 82,138 | 2,262 | 16.1 |
| 55 | L0-main | claudeopus46 | 22,518 | 60,343 | 82,861 | 1,545 | 12.2 |
| 56 | L0-main | claudeopus46 | 22,518 | 60,974 | 83,492 | 1,474 | 10.0 |
| 57 | L0-main | claudeopus46 | 22,518 | 61,276 | 83,794 | 1,616 | 11.0 |
| 58 | L0-main | claudeopus46 | 22,518 | 61,877 | 84,395 | 1,849 | 11.8 |
| 59 | L0-main | claudeopus46 | 22,518 | 62,541 | 85,059 | 1,792 | 11.8 |
| 60 | L0-main | claudeopus46 | 22,518 | 66,192 | 88,710 | 1,293 | 15.3 |
| 61 | L0-main | claudeopus46 | 22,518 | 66,952 | 89,470 | 873 | 7.1 |
| 62 | L0-main | claudeopus46 | 22,518 | 69,415 | 91,933 | 11,178 | 78.4 |
| 63 | L0-main | claudeopus46 | 22,518 | 86,584 | 109,102 | 6,212 | 48.3 |
| 64 | L0-main | claudeopus46 | 22,518 | 98,832 | 121,350 | 5,816 | 44.9 |
| 65 | L0-main | claudeopus46 | 2,106 | 6,422 | 8,528 | 395 | 4.9 |
| 66 | L0-main | claudeopus46 | 2,320 | 5,945 | 8,265 | 1,305 | 7.8 |
| 67 | L0-main | claudeopus46 | 366 | 918 | 1,284 | 384 | 3.5 |
| 68 | L0-main | claudeopus46 | 366 | 1,742 | 2,108 | 1,260 | 5.3 |
| 69 | L0-main | claudeopus46 | 560 | 7,039 | 7,599 | 273 | 2.8 |
| 70 | L0-main | claudeopus46 | 1,156 | 9,204 | 10,360 | 1,330 | 10.5 |
| 71 | L0-main | claudeopus46 | 1,918 | 5,139 | 7,057 | 1,170 | 10.5 |

