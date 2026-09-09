# Reference Stats — query-agent

**Run started:** 2026-09-05 16:00:02
**Wall time (at last flush):** 583.1 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 17 | 123,050 | 308,381 | 23,909 | 431,431 | 25,378 | 157.3 | claudeopus46 |
| L1-worker | 46 | 708,176 | 451,343 | 65,338 | 1,159,519 | 25,206 | 463.3 | claudeopus46 |
| verdict | 1 | 972 | 12,452 | 1,182 | 13,424 | 13,424 | 11.3 | claudeopus46 |
| **TOTAL** | **64** | **832,198** | **772,176** | **90,429** | **1,604,374** | **25,068** | **631.9** | |

**Estimated tokens:** ~401,093 input + ~22,607 output = ~423,700 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 6 | 5 | 2 | 5 | 6 | 308 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 6 | 5 | 2 | 5 | 6 | 308 |
| `search_blocks` | 2 | 6 | 5 | 2 | 5 | 6 | 308 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **8** | **18** | **15** | **6** | **15** | **18** | **924** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_952 | 1,3,5-trioxane | search_blocks |

#### References (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_3147 |  | search_blocks |
| GLOBlit_3168 |  | search_blocks |
| GLOBlit_8200 |  | search_blocks |
| GLOBlit_8573 |  | search_blocks |
| GLOBlit_10066 |  | search_blocks |

#### Properties (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_84 | Partial molar volume, m3/mol | search_blocks |
| GLOBprop_20 | Liquid-liquid equilibrium temperature, K | search_blocks |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBprop_2 | Mole fraction | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |

#### Measurements (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_89 | Partial molar volume, m3/mol | search_blocks |
| GLOBmeas_135 | Liquid-liquid equilibrium temperature, K | search_blocks |
| GLOBmeas_2218 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_1 | Mole fraction | search_blocks |
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
| Unique Compounds | 2 |
| Unique References | 5 |
| Unique Properties | 6 |
| Unique Measurements | 6 |
| Unique Phases | 3 |
| Unique Solvents | 1 |
| Unique Variables | 5 |
| Unique Constraints | 2 |
| Total DOIs | 5 |
| Unique parent blocks | 6 |
| Explicit block/subsystem targets | 6 |
| Subsystem targets | 0 |
| Target-matched data points | 924 |

---

## 3. DOI & Block References

**Unique DOIs:** 5  |  **Parent blocks:** 6  |  **Explicit targets:** 6  |  **Subsystems:** 0  |  **Target-matched datapoints:** 308

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2009.08.015 | 1 | 175 | binary | search_blocks |
| 10.1016/j.jct.2009.11.005 | 1 | 25 | binary | search_blocks |
| 10.1021/je030243h | 1 | 19 | binary | search_blocks |
| 10.1021/je050015i | 2 | 36 | binary | search_blocks |
| 10.1021/je301352v | 1 | 53 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2009.08.015 | PROPblock_5 | declared | 175 | binary | — | search_blocks |
| 10.1016/j.jct.2009.11.005 | PROPblock_5 | declared | 25 | binary | — | search_blocks |
| 10.1021/je030243h | PROPblock_1 | declared | 19 | binary | — | search_blocks |
| 10.1021/je050015i | PROPblock_1 | declared | 17 | binary | — | search_blocks |
| 10.1021/je050015i | PROPblock_2 | declared | 19 | binary | — | search_blocks |
| 10.1021/je301352v | PROPblock_5 | declared | 53 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `memory_catalog_add` | global_id=GLOBcomp_952, name=1,3,5-trioxane, regis… | 2 | — | — | 0.0 |
| 2 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve water to gl… | 206 | KEEP ←in 216 | 206 | 3.5 |
| 3 | 3 | `search_blocks` | compound=['GLOBcomp_952', 'GLOBcomp_1'], limit=50,… | 1,293 | KEEP ←in 8,182 | 1293 | 15.8 |
| 4 | 5 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_3147,… | 2,230 | — | — | 0.2 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_3168,… | 1,862 | — | — | 0.1 |
| 6 | 9 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_8200,… | 1,197 | — | — | 0.1 |
| 7 | 11 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_8573,… | 1,144 | — | — | 0.4 |
| 8 | 2 | `L1_query` | context=We already know viscosity dat…, id_catalog… | 374 | — | — | 183.2 |
| 9 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve water to gl… | 181 | KEEP ←in 216 | 181 | 3.5 |
| 10 | 3 | `search_blocks` | compound=['GLOBcomp_952', 'GLOBcomp_1'], limit=50,… | 1,244 | KEEP ←in 8,182 | 1244 | 21.8 |
| 11 | 4 | `search_blocks` | compound=['GLOBcomp_952', 'GLOBcomp_1'], limit=50,… | 1,316 | KEEP ←in 8,182 | 1316 | 18.5 |
| 12 | 6 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_3147,… | 2,230 | — | — | 0.2 |
| 13 | 8 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_3168,… | 1,862 | — | — | 0.1 |
| 14 | 10 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_8200,… | 1,197 | — | — | 0.1 |
| 15 | 12 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_8573,… | 1,144 | — | — | 0.1 |
| 16 | 3 | `L1_query` | context=Previous query errored on cor…, id_catalog… | 61,054 | — | — | 243.4 |
| 17 | 4 | `memory_catalog_add` | global_id=GLOBlit_3147, name=2010-cib-ale-0 (mass … | 2 | — | — | 0.0 |
| 18 | 5 | `memory_catalog_add` | global_id=GLOBlit_3168, name=2010-cib--0 (partial … | 2 | — | — | 0.2 |
| 19 | 6 | `memory_catalog_add` | global_id=GLOBlit_8200, name=2004-gru-has-0 (LLE t… | 2 | — | — | 0.0 |
| 20 | 8 | `memory_catalog_add` | global_id=GLOBlit_8573, name=2005-alb-has-0 (VLE),… | 2 | — | — | 0.0 |
| 21 | 9 | `memory_catalog_add` | global_id=GLOBlit_10066, name=2013-cib--0 (speed o… | 2 | — | — | 0.0 |
| | | **TOTAL (21 tools)** | | **78,546** | | **4,240** | **491.2** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 937 | 12,518 | 638 | 4.9 |
| 2 | L0-main | claudeopus46 | 11,581 | 1,347 | 12,928 | 1,178 | 7.2 |
| 3 | L1-worker | claudeopus46 | 24,095 | 1,292 | 25,387 | 527 | 4.9 |
| 4 | L1-worker | claudeopus46 | 24,095 | 2,284 | 26,379 | 510 | 4.4 |
| 5 | L1-worker | claudeopus46 | 3,767 | 365 | 4,132 | 330 | 3.4 |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,916 | 26,011 | 746 | 15.5 |
| 7 | L1-worker | claudeopus46 | 3,767 | 8,640 | 12,407 | 1,588 | 14.7 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,532 | 27,627 | 2,377 | 13.8 |
| 9 | L1-worker | claudeopus46 | 24,095 | 8,377 | 32,472 | 1,060 | 8.2 |
| 10 | L1-worker | claudeopus46 | 24,095 | 10,880 | 34,975 | 480 | 6.3 |
| 11 | L1-worker | claudeopus46 | 24,095 | 11,780 | 35,875 | 521 | 4.9 |
| 12 | L1-worker | claudeopus46 | 24,095 | 13,228 | 37,323 | 566 | 7.3 |
| 13 | L1-worker | claudeopus46 | 24,095 | 14,154 | 38,249 | 555 | 4.9 |
| 14 | L1-worker | claudeopus46 | 24,095 | 14,962 | 39,057 | 656 | 5.4 |
| 15 | L1-worker | claudeopus46 | 24,095 | 15,889 | 39,984 | 571 | 5.0 |
| 16 | L1-worker | claudeopus46 | 24,095 | 16,654 | 40,749 | 437 | 3.4 |
| 17 | L1-worker | claudeopus46 | 24,062 | 17,105 | 41,167 | 3,852 | 24.2 |
| 18 | L1-worker | claudeopus46 | 24,062 | 20,423 | 44,485 | 3,190 | 21.0 |
| 19 | L1-worker | claudeopus46 | 2,320 | 6,090 | 8,410 | 1,344 | 11.5 |
| 20 | L1-worker | claudeopus46 | 627 | 5,970 | 6,597 | 1,257 | 12.1 |
| 21 | L1-worker | claudeopus46 | 2,106 | 7,447 | 9,553 | 2,388 | 14.0 |
| 22 | L1-worker | claudeopus46 | 366 | 1,781 | 2,147 | 1,294 | 5.0 |
| 23 | L1-worker | claudeopus46 | 366 | 3,165 | 3,531 | 1,833 | 8.5 |
| 24 | L1-worker | claudeopus46 | 1,228 | 10,260 | 11,488 | 1,845 | 8.7 |
| 25 | L0-main | claudeopus46 | 11,581 | 2,019 | 13,600 | 1,281 | 8.2 |
| 26 | L1-worker | claudeopus46 | 24,095 | 1,315 | 25,410 | 622 | 5.3 |
| 27 | L1-worker | claudeopus46 | 24,095 | 2,291 | 26,386 | 495 | 4.0 |
| 28 | L1-worker | claudeopus46 | 3,767 | 349 | 4,116 | 305 | 3.4 |
| 29 | L1-worker | claudeopus46 | 24,095 | 1,925 | 26,020 | 799 | 5.6 |
| 30 | L1-worker | claudeopus46 | 3,767 | 8,646 | 12,413 | 1,666 | 14.9 |
| 31 | L1-worker | claudeopus46 | 24,095 | 3,488 | 27,583 | 2,920 | 19.1 |
| 32 | L1-worker | claudeopus46 | 3,767 | 8,626 | 12,393 | 1,551 | 12.6 |
| 33 | L1-worker | claudeopus46 | 24,095 | 5,202 | 29,297 | 2,455 | 15.9 |
| 34 | L1-worker | claudeopus46 | 24,095 | 10,125 | 34,220 | 1,429 | 10.6 |
| 35 | L1-worker | claudeopus46 | 24,095 | 12,659 | 36,754 | 500 | 6.1 |
| 36 | L1-worker | claudeopus46 | 24,095 | 13,581 | 37,676 | 551 | 4.9 |
| 37 | L1-worker | claudeopus46 | 24,095 | 15,027 | 39,122 | 696 | 7.9 |
| 38 | L1-worker | claudeopus46 | 24,095 | 15,953 | 40,048 | 583 | 4.8 |
| 39 | L1-worker | claudeopus46 | 24,095 | 16,805 | 40,900 | 649 | 4.8 |
| 40 | L1-worker | claudeopus46 | 24,095 | 17,755 | 41,850 | 579 | 3.8 |
| 41 | L1-worker | claudeopus46 | 24,062 | 18,115 | 42,177 | 5,568 | 37.9 |
| 42 | L1-worker | claudeopus46 | 24,062 | 21,567 | 45,629 | 4,530 | 29.8 |
| 43 | L1-worker | claudeopus46 | 2,320 | 5,703 | 8,023 | 1,677 | 10.4 |
| 44 | L1-worker | claudeopus46 | 627 | 5,583 | 6,210 | 1,613 | 11.9 |
| 45 | L1-worker | claudeopus46 | 2,106 | 7,083 | 9,189 | 2,361 | 12.0 |
| 46 | L1-worker | claudeopus46 | 366 | 2,114 | 2,480 | 1,627 | 6.3 |
| 47 | L1-worker | claudeopus46 | 366 | 3,138 | 3,504 | 1,764 | 8.4 |
| 48 | L1-worker | claudeopus46 | 1,228 | 9,899 | 11,127 | 1,842 | 8.5 |
| 49 | L1-worker | claudeopus46 | 787 | 48,200 | 48,987 | 629 | 7.3 |
| 50 | L0-main | claudeopus46 | 11,581 | 36,542 | 48,123 | 1,371 | 13.6 |
| 51 | L0-main | claudeopus46 | 11,581 | 37,088 | 48,669 | 521 | 5.3 |
| 52 | L0-main | claudeopus46 | 11,581 | 37,503 | 49,084 | 436 | 5.2 |
| 53 | L0-main | claudeopus46 | 11,581 | 37,887 | 49,468 | 134 | 3.3 |
| 54 | L0-main | claudeopus46 | 11,581 | 38,741 | 50,322 | 399 | 4.0 |
| 55 | L0-main | claudeopus46 | 11,581 | 38,405 | 49,986 | 408 | 4.9 |
| 56 | L0-main | claudeopus46 | 11,581 | 38,772 | 50,353 | 6,897 | 46.3 |
| 57 | L0-main | claudeopus46 | 2,106 | 6,755 | 8,861 | 1,290 | 8.9 |
| 58 | L0-main | claudeopus46 | 2,320 | 5,986 | 8,306 | 1,336 | 9.8 |
| 59 | L0-main | claudeopus46 | 366 | 1,811 | 2,177 | 1,282 | 4.4 |
| 60 | L0-main | claudeopus46 | 366 | 1,839 | 2,205 | 1,596 | 6.3 |
| 61 | L0-main | claudeopus46 | 560 | 7,866 | 8,426 | 498 | 4.1 |
| 62 | L0-main | claudeopus46 | 1,156 | 11,826 | 12,982 | 2,364 | 12.1 |
| 63 | L0-main | claudeopus46 | 366 | 3,057 | 3,423 | 2,280 | 8.8 |
| 64 | verdict | claudeopus46 | 972 | 12,452 | 13,424 | 1,182 | 11.3 |

