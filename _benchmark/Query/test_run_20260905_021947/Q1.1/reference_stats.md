# Reference Stats — query-agent

**Run started:** 2026-09-05 05:21:28
**Wall time (at last flush):** 285.4 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 11 | 32,118 | 43,656 | 10,747 | 75,774 | 6,888 | 71.7 | claudeopus46 |
| L1-worker | 24 | 358,904 | 138,186 | 28,565 | 497,090 | 20,712 | 217.4 | claudeopus46 |
| **TOTAL** | **35** | **391,022** | **181,842** | **39,312** | **572,864** | **16,367** | **289.1** | |

**Estimated tokens:** ~143,216 input + ~9,828 output = ~153,044 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 5 | 3 | 20 | 20 | 2,392 |
| `resolve_ids` | 0 | 0 | 2 | 0 | 0 | 0 | 0 |
| `block_search_adv` | 2 | 0 | 0 | 0 | 3 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **6** | **1** | **7** | **3** | **23** | **20** | **2,392** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | block_search_adv, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | block_search_adv, resolve_compound_ids, search_blocks |

#### References (20 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_220 |  | block_search_adv, search_blocks |
| GLOBlit_1483 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_3475 |  | search_blocks |
| GLOBlit_4415 |  | search_blocks |
| GLOBlit_5201 |  | block_search_adv, search_blocks |
| GLOBlit_5473 |  | search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_8050 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9006 |  | block_search_adv, search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_10699 |  | search_blocks |
| GLOBlit_10866 |  | search_blocks |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |

#### Measurements (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_236 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_203 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_212 | Mass density, kg/m3 | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | block_search_adv, search_blocks |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | resolve_ids, search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_2 | Mole fraction | resolve_ids, search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_2 |  | search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | block_search_adv |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 20 |
| Unique Properties | 1 |
| Unique Measurements | 7 |
| Unique Phases | 1 |
| Unique Variables | 5 |
| Unique Solvents | 2 |
| Unique Constraints | 3 |
| Unique Block_Types | 1 |
| Total DOIs | 20 |
| Unique parent blocks | 20 |
| Explicit block/subsystem targets | 20 |
| Subsystem targets | 0 |
| Target-matched data points | 2,392 |

---

## 3. DOI & Block References

**Unique DOIs:** 20  |  **Parent blocks:** 20  |  **Explicit targets:** 20  |  **Subsystems:** 0  |  **Target-matched datapoints:** 2,392

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | search_blocks |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 565 | binary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 1 | 37 | binary | search_blocks |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | search_blocks |
| 10.1016/j.jct.2015.06.024 | 1 | 40 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 244 | binary | search_blocks |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | search_blocks |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | search_blocks |
| 10.1021/je020173z | 1 | 24 | binary | search_blocks |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks |
| 10.1021/je060335h | 1 | 164 | binary | search_blocks |
| 10.1021/je4003515 | 1 | 23 | binary | search_blocks |
| 10.1021/je600565m | 1 | 18 | binary | search_blocks |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks |
| 10.1021/je800150h | 1 | 108 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | — | search_blocks |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | — | search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | — | search_blocks |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | — | search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | — | search_blocks |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | — | search_blocks |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | — | search_blocks |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | — | search_blocks |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | — | search_blocks |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | — | search_blocks |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve ethanol and… | 195 | KEEP ←in 278 | 195 | 4.9 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=20, p… | 426 | KEEP ←in 12,879 | 426 | 22.0 |
| 3 | 6 | `resolve_ids` | entity_type=variable, limit=5, min_score=80, purpo… | 225 | KEEP ←in 320 | 225 | 4.1 |
| 4 | 7 | `block_search_adv` | compound_match=all, compounds=['REQUIRE GLOBcomp_2… | 1,136 | KEEP ←in 3,362 | 1136 | 20.9 |
| 5 | 8 | `inspect_block_table` | block_number=GLOBlit_9006::PROPblock_1, nearest=GL… | 252 | — | — | 0.0 |
| 6 | 9 | `inspect_block_table` | block_number=GLOBlit_9006::PROPblock_1, nearest={'… | 370 | — | — | 0.1 |
| 7 | 10 | `inspect_block_table` | block_number=GLOBlit_9006::PROPblock_1, nearest={'… | 1,284 | — | — | 0.1 |
| 8 | 11 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_19, nearest={… | 1,279 | — | — | 0.3 |
| 9 | 1 | `L1_query` | context=User wants the density of an …, id_catalog… | 20,039 | — | — | 221.7 |
| | | **TOTAL (9 tools)** | | **25,206** | | **1,982** | **274.1** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 599 | 12,180 | 1,239 | 8.4 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,151 | 25,246 | 909 | 6.4 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,166 | 26,261 | 521 | 4.0 |
| 4 | L1-worker | claudeopus46 | 3,767 | 437 | 4,204 | 375 | 4.2 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,768 | 25,863 | 898 | 7.6 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,477 | 26,572 | 659 | 5.1 |
| 7 | L1-worker | claudeopus46 | 3,767 | 13,349 | 17,116 | 1,702 | 15.1 |
| 8 | L1-worker | claudeopus46 | 24,095 | 2,853 | 26,948 | 2,163 | 16.5 |
| 9 | L1-worker | claudeopus46 | 24,095 | 3,736 | 27,831 | 1,562 | 11.5 |
| 10 | L1-worker | claudeopus46 | 3,767 | 524 | 4,291 | 365 | 4.0 |
| 11 | L1-worker | claudeopus46 | 24,095 | 3,856 | 27,951 | 1,553 | 11.3 |
| 12 | L1-worker | claudeopus46 | 3,767 | 3,555 | 7,322 | 1,374 | 12.1 |
| 13 | L1-worker | claudeopus46 | 24,095 | 5,349 | 29,444 | 1,097 | 8.3 |
| 14 | L1-worker | claudeopus46 | 24,095 | 5,965 | 30,060 | 684 | 5.4 |
| 15 | L1-worker | claudeopus46 | 24,095 | 6,696 | 30,791 | 805 | 6.6 |
| 16 | L1-worker | claudeopus46 | 24,095 | 8,344 | 32,439 | 1,363 | 11.2 |
| 17 | L1-worker | claudeopus46 | 24,095 | 10,009 | 34,104 | 1,959 | 15.7 |
| 18 | L1-worker | claudeopus46 | 24,062 | 14,303 | 38,365 | 2,204 | 15.4 |
| 19 | L1-worker | claudeopus46 | 24,062 | 16,478 | 40,540 | 2,436 | 20.0 |
| 20 | L1-worker | claudeopus46 | 627 | 3,271 | 3,898 | 849 | 6.1 |
| 21 | L1-worker | claudeopus46 | 2,106 | 4,663 | 6,769 | 1,167 | 6.6 |
| 22 | L1-worker | claudeopus46 | 2,320 | 3,391 | 5,711 | 1,210 | 7.9 |
| 23 | L1-worker | claudeopus46 | 366 | 1,944 | 2,310 | 689 | 3.8 |
| 24 | L1-worker | claudeopus46 | 366 | 1,647 | 2,013 | 1,165 | 4.3 |
| 25 | L1-worker | claudeopus46 | 787 | 20,254 | 21,041 | 856 | 8.3 |
| 26 | L0-main | claudeopus46 | 11,581 | 16,967 | 28,548 | 2,646 | 19.6 |
| 27 | L0-main | claudeopus46 | 2,320 | 2,325 | 4,645 | 1,002 | 5.2 |
| 28 | L0-main | claudeopus46 | 2,106 | 2,756 | 4,862 | 707 | 5.5 |
| 29 | L0-main | claudeopus46 | 366 | 1,256 | 1,622 | 801 | 3.7 |
| 30 | L0-main | claudeopus46 | 366 | 1,477 | 1,843 | 953 | 5.6 |
| 31 | L0-main | claudeopus46 | 560 | 3,068 | 3,628 | 121 | 2.1 |
| 32 | L0-main | claudeopus46 | 1,156 | 4,442 | 5,598 | 879 | 6.1 |
| 33 | L0-main | claudeopus46 | 560 | 3,809 | 4,369 | 189 | 2.9 |
| 34 | L0-main | claudeopus46 | 1,156 | 5,091 | 6,247 | 1,173 | 7.7 |
| 35 | L0-main | claudeopus46 | 366 | 1,866 | 2,232 | 1,037 | 4.9 |

