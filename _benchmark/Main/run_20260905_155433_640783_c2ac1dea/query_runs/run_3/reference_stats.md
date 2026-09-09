# Reference Stats — query-agent

**Run started:** 2026-09-05 16:00:02
**Wall time (at last flush):** 248.5 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 7 | 39,901 | 36,382 | 7,504 | 76,283 | 10,897 | 51.6 | claudeopus46 |
| L1-worker | 25 | 251,869 | 116,675 | 27,676 | 368,544 | 14,741 | 184.0 | claudeopus46 |
| verdict | 1 | 972 | 4,829 | 1,106 | 5,801 | 5,801 | 9.5 | claudeopus46 |
| **TOTAL** | **33** | **292,742** | **157,886** | **36,286** | **450,628** | **13,655** | **245.1** | |

**Estimated tokens:** ~112,657 input + ~9,071 output = ~121,728 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 5 | 6 | 5 | 2 | 6 | 9 | 332 |
| **TOTAL** | **5** | **6** | **5** | **2** | **6** | **9** | **332** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### References (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_3147 |  | search_blocks |
| GLOBlit_3168 |  | search_blocks |
| GLOBlit_8200 |  | search_blocks |
| GLOBlit_8564 |  | search_blocks |
| GLOBlit_8573 |  | search_blocks |
| GLOBlit_10066 |  | search_blocks |

#### Compounds (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_952 | 1,3,5-trioxane | search_blocks |
| GLOBcomp_1 | water | search_blocks |
| GLOBcomp_4 | methanol | search_blocks |
| GLOBcomp_2 | ethanol | search_blocks |
| GLOBcomp_6 | propan-2-ol | search_blocks |

#### Properties (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_84 | Partial molar volume, m3/mol | search_blocks |
| GLOBprop_20 | Liquid-liquid equilibrium temperature, K | search_blocks |
| GLOBprop_2 | Mole fraction | search_blocks |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |

#### Measurements (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_89 | Partial molar volume, m3/mol | search_blocks |
| GLOBmeas_135 | Liquid-liquid equilibrium temperature, K | search_blocks |
| GLOBmeas_1 | Mole fraction | search_blocks |
| GLOBmeas_2218 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_20 | Speed of sound, m/s | search_blocks |

#### Phases (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |
| GLOBphase_4 |  | search_blocks |
| GLOBphase_3 |  | search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique References | 6 |
| Unique Compounds | 5 |
| Unique Properties | 6 |
| Unique Measurements | 6 |
| Unique Phases | 3 |
| Unique Solvents | 1 |
| Unique Variables | 5 |
| Unique Constraints | 2 |
| Total DOIs | 6 |
| Unique parent blocks | 9 |
| Explicit block/subsystem targets | 9 |
| Subsystem targets | 0 |
| Target-matched data points | 332 |

---

## 3. DOI & Block References

**Unique DOIs:** 6  |  **Parent blocks:** 9  |  **Explicit targets:** 9  |  **Subsystems:** 0  |  **Target-matched datapoints:** 332

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2009.08.015 | 1 | 175 | binary | search_blocks |
| 10.1016/j.jct.2009.11.005 | 1 | 25 | binary | search_blocks |
| 10.1021/je030243h | 1 | 19 | binary | search_blocks |
| 10.1021/je049978s | 3 | 24 | binary | search_blocks |
| 10.1021/je050015i | 2 | 36 | binary | search_blocks |
| 10.1021/je301352v | 1 | 53 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2009.08.015 | PROPblock_5 | declared | 175 | binary | — | search_blocks |
| 10.1016/j.jct.2009.11.005 | PROPblock_5 | declared | 25 | binary | — | search_blocks |
| 10.1021/je030243h | PROPblock_1 | declared | 19 | binary | — | search_blocks |
| 10.1021/je049978s | PROPblock_1 | declared | 8 | binary | — | search_blocks |
| 10.1021/je049978s | PROPblock_2 | declared | 8 | binary | — | search_blocks |
| 10.1021/je049978s | PROPblock_3 | declared | 8 | binary | — | search_blocks |
| 10.1021/je050015i | PROPblock_1 | declared | 17 | binary | — | search_blocks |
| 10.1021/je050015i | PROPblock_2 | declared | 19 | binary | — | search_blocks |
| 10.1021/je301352v | PROPblock_5 | declared | 53 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `search_blocks` | compound=GLOBcomp_952, limit=50, property=GLOBprop… | 664 | DISCARD ←in 39 | 606 | 13.6 |
| 2 | 2 | `search_blocks` | compound=GLOBcomp_952, limit=50, property=GLOBprop… | 903 | DISCARD ←in 39 | 845 | 14.5 |
| 3 | 3 | `search_blocks` | compound=GLOBcomp_952, limit=50, purpose=Find all … | 667 | DISCARD ←in 39 | 609 | 8.2 |
| 4 | 1 | `L1_query` | context=We are searching for any visc…, id_catalog… | 1,660 | — | — | 70.4 |
| 5 | 1 | `search_blocks` | compound=GLOBcomp_952, limit=50, property=GLOBprop… | 746 | DISCARD ←in 39 | 688 | 13.5 |
| 6 | 2 | `search_blocks` | compound=GLOBcomp_952, limit=50, property=GLOBprop… | 780 | DISCARD ←in 39 | 722 | 6.6 |
| 7 | 3 | `search_blocks` | compound=GLOBcomp_952, limit=50, purpose=Find all … | 1,348 | KEEP ←in 5,747 | 1228 | 12.9 |
| 8 | 2 | `L1_query` | context=We already confirmed no pure-…, id_catalog… | 45,769 | — | — | 123.4 |
| | | **TOTAL (8 tools)** | | **52,537** | | **4,698** | **263.1** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 962 | 12,543 | 1,200 | 7.5 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,086 | 25,181 | 739 | 5.6 |
| 3 | L1-worker | claudeopus46 | 3,767 | 440 | 4,207 | 804 | 7.1 |
| 4 | L1-worker | claudeopus46 | 24,095 | 2,059 | 26,154 | 861 | 5.8 |
| 5 | L1-worker | claudeopus46 | 3,767 | 434 | 4,201 | 1,046 | 7.8 |
| 6 | L1-worker | claudeopus46 | 24,095 | 3,365 | 27,460 | 839 | 6.0 |
| 7 | L1-worker | claudeopus46 | 3,767 | 386 | 4,153 | 949 | 7.8 |
| 8 | L1-worker | claudeopus46 | 24,095 | 4,408 | 28,503 | 1,110 | 7.2 |
| 9 | L1-worker | claudeopus46 | 2,106 | 2,027 | 4,133 | 92 | 2.2 |
| 10 | L1-worker | claudeopus46 | 2,320 | 820 | 3,140 | 398 | 3.3 |
| 11 | L1-worker | claudeopus46 | 627 | 700 | 1,327 | 403 | 3.2 |
| 12 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 1.9 |
| 13 | L1-worker | claudeopus46 | 787 | 2,311 | 3,098 | 495 | 4.2 |
| 14 | L0-main | claudeopus46 | 11,581 | 4,641 | 16,222 | 1,402 | 9.3 |
| 15 | L1-worker | claudeopus46 | 24,095 | 3,171 | 27,266 | 1,106 | 7.2 |
| 16 | L1-worker | claudeopus46 | 3,767 | 446 | 4,213 | 898 | 6.8 |
| 17 | L1-worker | claudeopus46 | 24,095 | 4,288 | 28,383 | 768 | 5.4 |
| 18 | L1-worker | claudeopus46 | 3,767 | 450 | 4,217 | 927 | 6.2 |
| 19 | L1-worker | claudeopus46 | 24,095 | 5,471 | 29,566 | 706 | 4.7 |
| 20 | L1-worker | claudeopus46 | 3,767 | 6,090 | 9,857 | 1,452 | 12.3 |
| 21 | L1-worker | claudeopus46 | 24,095 | 7,169 | 31,264 | 2,955 | 16.9 |
| 22 | L1-worker | claudeopus46 | 24,095 | 12,466 | 36,561 | 4,313 | 25.6 |
| 23 | L1-worker | claudeopus46 | 627 | 1,880 | 2,507 | 559 | 3.5 |
| 24 | L1-worker | claudeopus46 | 2,320 | 2,000 | 4,320 | 509 | 3.9 |
| 25 | L1-worker | claudeopus46 | 2,106 | 3,548 | 5,654 | 2,654 | 10.8 |
| 26 | L1-worker | claudeopus46 | 366 | 3,431 | 3,797 | 2,119 | 9.0 |
| 27 | L1-worker | claudeopus46 | 787 | 47,360 | 48,147 | 907 | 9.6 |
| 28 | L0-main | claudeopus46 | 11,581 | 22,686 | 34,267 | 2,718 | 19.9 |
| 29 | L0-main | claudeopus46 | 2,320 | 2,572 | 4,892 | 612 | 4.2 |
| 30 | L0-main | claudeopus46 | 2,106 | 3,366 | 5,472 | 519 | 4.7 |
| 31 | L0-main | claudeopus46 | 366 | 1,087 | 1,453 | 573 | 2.9 |
| 32 | L0-main | claudeopus46 | 366 | 1,068 | 1,434 | 480 | 3.1 |
| 33 | verdict | claudeopus46 | 972 | 4,829 | 5,801 | 1,106 | 9.5 |

