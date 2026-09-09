# Reference Stats — query-agent

**Run started:** 2026-09-05 05:52:10
**Wall time (at last flush):** 379.5 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 41,617 | 79,660 | 15,349 | 121,277 | 13,475 | 99.7 | claudeopus46 |
| L1-worker | 29 | 338,046 | 218,420 | 43,910 | 556,466 | 19,188 | 312.5 | claudeopus46 |
| **TOTAL** | **38** | **379,663** | **298,080** | **59,259** | **677,743** | **17,835** | **412.2** | |

**Estimated tokens:** ~169,435 input + ~14,814 output = ~184,249 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 2 | 7 | 7 | 302 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 1 | 2 | 1 | 1 | 13 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **6** | **2** | **4** | **4** | **8** | **8** | **315** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_24 |  | resolve_compound_ids, search_blocks |

#### References (8 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2656 |  | search_blocks |
| GLOBlit_5201 |  | search_blocks |
| GLOBlit_6951 |  | search_blocks |
| GLOBlit_8038 |  | search_blocks |
| GLOBlit_8106 |  | search_blocks |
| GLOBlit_11186 |  | search_blocks |
| GLOBlit_11506 |  | search_blocks |
| GLOBlit_5843 |  | search_blocks |

#### Properties (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBprop_17 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |

#### Measurements (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_227 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_13 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 8 |
| Unique Properties | 2 |
| Unique Measurements | 7 |
| Unique Phases | 1 |
| Unique Variables | 3 |
| Unique Constraints | 2 |
| Total DOIs | 8 |
| Unique parent blocks | 8 |
| Explicit block/subsystem targets | 8 |
| Subsystem targets | 0 |
| Target-matched data points | 315 |

---

## 3. DOI & Block References

**Unique DOIs:** 8  |  **Parent blocks:** 8  |  **Explicit targets:** 8  |  **Subsystems:** 0  |  **Target-matched datapoints:** 315

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2006.01.011 | 1 | 10 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 84 | binary | search_blocks |
| 10.1016/j.tca.2009.06.004 | 1 | 13 | binary | search_blocks |
| 10.1021/acs.jced.6b00526 | 1 | 33 | binary | search_blocks |
| 10.1021/je020140j | 1 | 77 | binary | search_blocks |
| 10.1021/je025610o | 1 | 30 | binary | search_blocks |
| 10.1021/je800271e | 1 | 52 | binary | search_blocks |
| 10.1021/je9000697 | 1 | 16 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2006.01.011 | PROPblock_13 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_24 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.tca.2009.06.004 | PROPblock_1 | declared | 13 | binary | — | search_blocks |
| 10.1021/acs.jced.6b00526 | PROPblock_18 | declared | 33 | binary | — | search_blocks |
| 10.1021/je020140j | PROPblock_5 | declared | 77 | binary | — | search_blocks |
| 10.1021/je025610o | PROPblock_5 | declared | 30 | binary | — | search_blocks |
| 10.1021/je800271e | PROPblock_4 | declared | 52 | binary | — | search_blocks |
| 10.1021/je9000697 | PROPblock_1 | declared | 16 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 213 | KEEP ←in 288 | 213 | 4.7 |
| 2 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=20, … | 1,292 | KEEP ←in 9,915 | 1292 | 17.4 |
| 3 | 4 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_6951… | 1,412 | — | — | 0.1 |
| 4 | 1 | `L1_query` | context=User wants to understand how …, id_catalog… | 15,870 | — | — | 170.4 |
| 5 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,079 | KEEP ←in 1,823 | 1064 | 12.7 |
| 6 | 2 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_5843,… | 1,331 | — | — | 0.1 |
| 7 | 3 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_5843,… | 1,461 | — | — | 0.9 |
| 8 | 2 | `L1_query` | context=User is asking about non-idea…, id_catalog… | 15,803 | — | — | 117.4 |
| | | **TOTAL (8 tools)** | | **38,461** | | **2,569** | **323.7** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 598 | 12,179 | 1,614 | 9.6 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,116 | 25,211 | 833 | 8.2 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,182 | 26,277 | 601 | 4.0 |
| 4 | L1-worker | claudeopus46 | 3,767 | 472 | 4,239 | 387 | 4.6 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,777 | 25,872 | 802 | 6.4 |
| 6 | L1-worker | claudeopus46 | 3,767 | 10,356 | 14,123 | 1,682 | 15.0 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,436 | 27,531 | 1,430 | 10.5 |
| 8 | L1-worker | claudeopus46 | 24,095 | 5,220 | 29,315 | 5,108 | 38.4 |
| 9 | L1-worker | claudeopus46 | 24,095 | 16,519 | 40,614 | 4,592 | 33.8 |
| 10 | L1-worker | claudeopus46 | 24,095 | 24,161 | 48,256 | 3,798 | 26.0 |
| 11 | L1-worker | claudeopus46 | 2,106 | 5,710 | 7,816 | 701 | 5.0 |
| 12 | L1-worker | claudeopus46 | 627 | 4,353 | 4,980 | 956 | 7.0 |
| 13 | L1-worker | claudeopus46 | 2,320 | 4,473 | 6,793 | 1,111 | 7.1 |
| 14 | L1-worker | claudeopus46 | 366 | 1,478 | 1,844 | 550 | 3.3 |
| 15 | L1-worker | claudeopus46 | 366 | 1,548 | 1,914 | 1,071 | 4.1 |
| 16 | L1-worker | claudeopus46 | 787 | 16,790 | 17,577 | 655 | 7.3 |
| 17 | L0-main | claudeopus46 | 11,581 | 17,992 | 29,573 | 1,870 | 13.9 |
| 18 | L1-worker | claudeopus46 | 24,095 | 8,591 | 32,686 | 844 | 6.2 |
| 19 | L1-worker | claudeopus46 | 3,767 | 2,320 | 6,087 | 1,560 | 11.5 |
| 20 | L1-worker | claudeopus46 | 24,095 | 9,975 | 34,070 | 841 | 9.1 |
| 21 | L1-worker | claudeopus46 | 24,095 | 11,667 | 35,762 | 1,140 | 10.1 |
| 22 | L1-worker | claudeopus46 | 24,095 | 13,539 | 37,634 | 2,432 | 18.2 |
| 23 | L1-worker | claudeopus46 | 24,095 | 18,033 | 42,128 | 4,624 | 24.8 |
| 24 | L1-worker | claudeopus46 | 24,095 | 24,993 | 49,088 | 3,105 | 17.3 |
| 25 | L1-worker | claudeopus46 | 2,320 | 3,391 | 5,711 | 896 | 5.3 |
| 26 | L1-worker | claudeopus46 | 627 | 3,271 | 3,898 | 812 | 5.4 |
| 27 | L1-worker | claudeopus46 | 2,106 | 4,925 | 7,031 | 667 | 5.7 |
| 28 | L1-worker | claudeopus46 | 366 | 1,444 | 1,810 | 401 | 2.9 |
| 29 | L1-worker | claudeopus46 | 366 | 1,223 | 1,589 | 799 | 3.8 |
| 30 | L1-worker | claudeopus46 | 366 | 1,333 | 1,699 | 856 | 4.1 |
| 31 | L1-worker | claudeopus46 | 787 | 14,124 | 14,911 | 656 | 7.4 |
| 32 | L0-main | claudeopus46 | 11,581 | 33,165 | 44,746 | 6,333 | 45.0 |
| 33 | L0-main | claudeopus46 | 2,106 | 5,741 | 7,847 | 717 | 5.3 |
| 34 | L0-main | claudeopus46 | 2,320 | 5,311 | 7,631 | 1,459 | 8.6 |
| 35 | L0-main | claudeopus46 | 366 | 1,266 | 1,632 | 811 | 3.9 |
| 36 | L0-main | claudeopus46 | 366 | 1,934 | 2,300 | 1,410 | 4.7 |
| 37 | L0-main | claudeopus46 | 560 | 6,078 | 6,638 | 185 | 2.6 |
| 38 | L0-main | claudeopus46 | 1,156 | 7,575 | 8,731 | 950 | 6.1 |

