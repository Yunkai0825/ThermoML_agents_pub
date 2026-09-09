# Reference Stats — analysis-agent

**Run started:** 2026-09-05 16:14:09
**Wall time (at last flush):** 494.1 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 25 | 391,964 | 632,094 | 38,755 | 1,024,058 | 40,962 | 298.0 | claudeopus46 |
| L1-worker | 22 | 351,370 | 218,177 | 29,983 | 569,547 | 25,888 | 211.8 | claudeopus46 |
| **TOTAL** | **47** | **743,334** | **850,271** | **68,738** | **1,593,605** | **33,906** | **509.8** | |

**Estimated tokens:** ~398,401 input + ~17,184 output = ~415,585 total
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
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 3 | 2 | 5 | 5 | 0 |
| **TOTAL** | **6** | **2** | **6** | **4** | **12** | **12** | **302** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_24 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | query_thermoml, resolve_compound_ids, search_blocks |

#### References (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2656 |  | query_thermoml, search_blocks |
| GLOBlit_5201 |  | query_thermoml, search_blocks |
| GLOBlit_6951 |  | query_thermoml, search_blocks |
| GLOBlit_8038 |  | query_thermoml, search_blocks |
| GLOBlit_8106 |  | query_thermoml, search_blocks |
| GLOBlit_11186 |  | search_blocks |
| GLOBlit_11506 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | query_thermoml, search_blocks |

#### Measurements (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_4 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_227 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_5 | Mass fraction | query_thermoml, search_blocks |
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | query_thermoml, search_blocks |
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 7 |
| Unique Properties | 1 |
| Unique Measurements | 6 |
| Unique Phases | 1 |
| Unique Variables | 3 |
| Unique Constraints | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 7 |
| Unique parent blocks | 7 |
| Explicit block/subsystem targets | 7 |
| Subsystem targets | 0 |
| Target-matched data points | 536 |

---

## 3. DOI & Block References

**Unique DOIs:** 7  |  **Parent blocks:** 7  |  **Explicit targets:** 7  |  **Subsystems:** 0  |  **Target-matched datapoints:** 302

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2006.01.011 | 1 | 10 | binary | query_thermoml, search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 84 | binary | query_thermoml, search_blocks |
| 10.1021/acs.jced.6b00526 | 1 | 33 | binary | query_thermoml, search_blocks |
| 10.1021/je020140j | 1 | 77 | binary | query_thermoml, search_blocks |
| 10.1021/je025610o | 1 | 30 | binary | query_thermoml, search_blocks |
| 10.1021/je800271e | 1 | 52 | binary | search_blocks |
| 10.1021/je9000697 | 1 | 16 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2006.01.011 | PROPblock_13 | declared | 10 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_24 | declared | 84 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/acs.jced.6b00526 | PROPblock_18 | declared | 33 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je020140j | PROPblock_5 | declared | 77 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je025610o | PROPblock_5 | declared | 30 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je800271e | PROPblock_4 | declared | 52 | binary | — | search_blocks |
| 10.1021/je9000697 | PROPblock_1 | declared | 16 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 213 | KEEP ←in 288 | 213 | 4.6 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_24', 'GLOBcomp_1'], limit=50, … | 1,236 | KEEP ←in 9,915 | 1206 | 20.6 |
| 3 | 6 | `inspect_block_table` | block_number=PROPblock_24, literature=GLOBlit_5201… | 249 | — | — | 0.0 |
| 4 | 7 | `inspect_block_table` | block_number=PROPblock_24, literature=GLOBlit_5201… | 378 | — | — | 0.3 |
| 5 | 8 | `inspect_block_table` | block_number=PROPblock_24, literature=GLOBlit_5201… | 942 | — | — | 0.1 |
| 6 | 9 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_6951… | 914 | — | — | 0.1 |
| 7 | 10 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_8038,… | 1,014 | — | — | 0.1 |
| 8 | 11 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_8106,… | 1,015 | — | — | 0.1 |
| 9 | 12 | `inspect_block_table` | block_number=PROPblock_13, literature=GLOBlit_2656… | 1,056 | — | — | 0.1 |
| 10 | 1 | `query_thermoml` | instruction=Search for dynamic viscosity …, purpos… | 44,382 | — | — | 195.3 |
| 11 | 4 | `inspect_block` | block_number=PROPblock_24, doi=10.1016/j.jct.2018.… | 1,379 | — | — | 0.3 |
| 12 | 8 | `fit_multi_system` | purpose=Fit viscosity of ethylene gly…, systems=[{… | 482 | — | — | 0.2 |
| 13 | 12 | `fit_multi_system` | purpose=Fit viscosity of ethylene gly…, systems=[{… | 1,176 | — | — | 3.7 |
| 14 | 13 | `predict_from_rk` | coeffs=[2.39674, -1.04444, 0.668173,…, mixing_rule… | 215 | — | — | 0.1 |
| 15 | 14 | `predict_from_rk` | coeffs=[2.274524, 1.438464, 0.538413…, mixing_rule… | 215 | — | — | 0.0 |
| | | **TOTAL (15 tools)** | | **54,866** | | **1,419** | **225.6** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 284 | 22,802 | 1,150 | 8.7 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,026 | 25,121 | 660 | 4.8 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,077 | 26,172 | 567 | 4.0 |
| 4 | L1-worker | claudeopus46 | 3,767 | 475 | 4,242 | 402 | 4.3 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,668 | 25,763 | 879 | 6.7 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,399 | 26,494 | 731 | 5.2 |
| 7 | L1-worker | claudeopus46 | 3,767 | 10,484 | 14,251 | 1,583 | 14.7 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,612 | 27,707 | 3,188 | 18.9 |
| 9 | L1-worker | claudeopus46 | 24,095 | 10,381 | 34,476 | 1,073 | 8.9 |
| 10 | L1-worker | claudeopus46 | 24,095 | 10,950 | 35,045 | 515 | 5.1 |
| 11 | L1-worker | claudeopus46 | 24,095 | 11,604 | 35,699 | 594 | 5.1 |
| 12 | L1-worker | claudeopus46 | 24,095 | 12,855 | 36,950 | 624 | 5.9 |
| 13 | L1-worker | claudeopus46 | 24,095 | 14,175 | 38,270 | 687 | 5.5 |
| 14 | L1-worker | claudeopus46 | 24,095 | 15,559 | 39,654 | 603 | 5.4 |
| 15 | L1-worker | claudeopus46 | 24,095 | 16,890 | 40,985 | 625 | 5.7 |
| 16 | L1-worker | claudeopus46 | 24,062 | 17,967 | 42,029 | 3,768 | 27.4 |
| 17 | L1-worker | claudeopus46 | 24,062 | 21,927 | 45,989 | 4,276 | 29.9 |
| 18 | L1-worker | claudeopus46 | 2,320 | 5,233 | 7,553 | 1,360 | 10.1 |
| 19 | L1-worker | claudeopus46 | 627 | 5,113 | 5,740 | 1,310 | 10.8 |
| 20 | L1-worker | claudeopus46 | 2,106 | 6,380 | 8,486 | 2,496 | 11.8 |
| 21 | L1-worker | claudeopus46 | 366 | 1,797 | 2,163 | 1,310 | 5.3 |
| 22 | L1-worker | claudeopus46 | 366 | 3,273 | 3,639 | 1,918 | 7.9 |
| 23 | L1-worker | claudeopus46 | 787 | 42,332 | 43,119 | 814 | 8.4 |
| 24 | L0-main | claudeopus46 | 22,518 | 29,398 | 51,916 | 1,241 | 13.3 |
| 25 | L0-main | claudeopus46 | 22,518 | 30,214 | 52,732 | 617 | 5.7 |
| 26 | L0-main | claudeopus46 | 22,518 | 30,933 | 53,451 | 476 | 4.4 |
| 27 | L0-main | claudeopus46 | 22,518 | 32,530 | 55,048 | 1,582 | 10.8 |
| 28 | L0-main | claudeopus46 | 22,518 | 33,244 | 55,762 | 1,126 | 8.3 |
| 29 | L0-main | claudeopus46 | 22,518 | 33,886 | 56,404 | 1,088 | 8.1 |
| 30 | L0-main | claudeopus46 | 22,518 | 34,536 | 57,054 | 1,081 | 8.2 |
| 31 | L0-main | claudeopus46 | 22,518 | 34,394 | 56,912 | 1,038 | 7.1 |
| 32 | L0-main | claudeopus46 | 22,518 | 35,035 | 57,553 | 1,272 | 8.7 |
| 33 | L0-main | claudeopus46 | 22,518 | 35,652 | 58,170 | 1,154 | 7.5 |
| 34 | L0-main | claudeopus46 | 22,518 | 36,317 | 58,835 | 1,145 | 8.2 |
| 35 | L0-main | claudeopus46 | 22,518 | 39,481 | 61,999 | 1,176 | 9.6 |
| 36 | L0-main | claudeopus46 | 22,518 | 40,115 | 62,633 | 972 | 8.7 |
| 37 | L0-main | claudeopus46 | 22,518 | 40,740 | 63,258 | 7,871 | 58.4 |
| 38 | L0-main | claudeopus46 | 22,518 | 53,498 | 76,016 | 5,586 | 45.7 |
| 39 | L0-main | claudeopus46 | 22,518 | 62,531 | 85,049 | 3,667 | 31.8 |
| 40 | L0-main | claudeopus46 | 2,106 | 4,195 | 6,301 | 386 | 3.6 |
| 41 | L0-main | claudeopus46 | 366 | 909 | 1,275 | 375 | 3.0 |
| 42 | L0-main | claudeopus46 | 2,320 | 3,796 | 6,116 | 1,095 | 7.6 |
| 43 | L0-main | claudeopus46 | 366 | 1,532 | 1,898 | 1,055 | 4.5 |
| 44 | L0-main | claudeopus46 | 560 | 4,881 | 5,441 | 264 | 2.5 |
| 45 | L0-main | claudeopus46 | 1,156 | 7,043 | 8,199 | 1,155 | 8.3 |
| 46 | L0-main | claudeopus46 | 366 | 1,848 | 2,214 | 1,109 | 5.1 |
| 47 | L0-main | claudeopus46 | 1,918 | 5,102 | 7,020 | 1,074 | 10.2 |

