# Reference Stats — analysis-agent

**Run started:** 2026-09-05 02:20:51
**Wall time (at last flush):** 499.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 21 | 324,044 | 440,079 | 21,308 | 764,123 | 36,386 | 171.4 | claudeopus46 |
| L1-worker | 29 | 377,739 | 207,809 | 40,011 | 585,548 | 20,191 | 307.7 | claudeopus46 |
| **TOTAL** | **50** | **701,783** | **647,888** | **61,319** | **1,349,671** | **26,993** | **479.1** | |

**Estimated tokens:** ~337,417 input + ~15,329 output = ~352,746 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 5 | 4 | 22 | 22 | 2,417 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 5 | 4 | 22 | 22 | 2,417 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_ids` | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| `block_search_adv` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `block_search_adv` | 2 | 0 | 0 | 0 | 6 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 3 | 2 | 6 | 6 | 573 |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **10** | **3** | **14** | **10** | **56** | **50** | **5,407** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | block_search_adv, query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | block_search_adv, query_thermoml, resolve_compound_ids, search_blocks |

#### References (24 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_220 |  | block_search_adv, query_thermoml, search_blocks |
| GLOBlit_1483 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_3475 |  | search_blocks |
| GLOBlit_4415 |  | search_blocks |
| GLOBlit_5201 |  | block_search_adv, query_thermoml, search_blocks |
| GLOBlit_5473 |  | block_search_adv, query_thermoml, search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_8050 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9006 |  | block_search_adv, query_thermoml, search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_10699 |  | search_blocks |
| GLOBlit_10866 |  | search_blocks |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | search_blocks |
| GLOBlit_11504 |  | search_blocks |
| GLOBlit_11792 |  | search_blocks |
| GLOBlit_1742 |  | block_search_adv, query_thermoml |
| GLOBlit_2092 |  | block_search_adv, query_thermoml |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml, search_blocks |

#### Measurements (9 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_138 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_236 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_203 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_212 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | block_search_adv, query_thermoml, search_blocks |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks |
| GLOBvar_3 | Pressure, kPa | query_thermoml, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml, resolve_ids, search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_2 |  | search_blocks |

#### Constraints (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks |
| GLOBconstr_2 | Temperature, K | query_thermoml, search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_22 | Volume fraction | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | block_search_adv, query_thermoml |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 24 |
| Unique Properties | 1 |
| Unique Measurements | 9 |
| Unique Phases | 1 |
| Unique Variables | 5 |
| Unique Solvents | 2 |
| Unique Constraints | 4 |
| Unique Block_Types | 1 |
| Total DOIs | 24 |
| Unique parent blocks | 24 |
| Explicit block/subsystem targets | 24 |
| Subsystem targets | 0 |
| Target-matched data points | 6,217 |

---

## 3. DOI & Block References

**Unique DOIs:** 24  |  **Parent blocks:** 24  |  **Explicit targets:** 24  |  **Subsystems:** 0  |  **Target-matched datapoints:** 2,573

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | query_thermoml, search_blocks |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | search_blocks |
| 10.1016/j.fluid.2015.07.012 | 1 | 84 | binary | query_thermoml |
| 10.1016/j.fluid.2017.09.005 | 1 | 72 | binary | query_thermoml |
| 10.1016/j.jct.2004.07.019 | 1 | 565 | binary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 1 | 37 | binary | search_blocks |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | search_blocks |
| 10.1016/j.jct.2015.06.024 | 1 | 40 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 244 | binary | query_thermoml, search_blocks |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | query_thermoml, search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | search_blocks |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | search_blocks |
| 10.1021/je020173z | 1 | 24 | binary | search_blocks |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks |
| 10.1021/je060335h | 1 | 164 | binary | query_thermoml, search_blocks |
| 10.1021/je4003515 | 1 | 23 | binary | search_blocks |
| 10.1021/je600565m | 1 | 18 | binary | search_blocks |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks |
| 10.1021/je800150h | 1 | 108 | binary | search_blocks |
| 10.1021/je900064e | 1 | 10 | binary | search_blocks |
| 10.1021/je900743e | 1 | 15 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_3 | declared | 84 | binary | 2 | query_thermoml |
| 10.1016/j.fluid.2017.09.005 | PROPblock_3 | declared | 72 | binary | 2 | query_thermoml |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | — | search_blocks |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | — | search_blocks |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | — | search_blocks |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | — | search_blocks |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | — | search_blocks |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | — | search_blocks |
| 10.1021/je900064e | PROPblock_6 | declared | 10 | binary | — | search_blocks |
| 10.1021/je900743e | PROPblock_3 | declared | 15 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve ethanol and… | 179 | KEEP ←in 278 | 179 | 7.4 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 329 | KEEP ←in 14,080 | 300 | 31.4 |
| 3 | 5 | `inspect_block_table` | block_number=GLOBlit_220::PROPblock_1, purpose=Ins… | 311 | — | — | 0.3 |
| 4 | 6 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=30, p… | 364 | KEEP ←in 14,080 | 364 | 39.1 |
| 5 | 7 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_1, nearest=te… | 259 | — | — | 0.0 |
| 6 | 8 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_1, nearest={'… | 329 | — | — | 0.2 |
| 7 | 9 | `resolve_ids` | entity_type=variable, limit=10, min_score=70, purp… | 227 | KEEP ←in 241 | 227 | 4.6 |
| 8 | 10 | `block_search_adv` | compounds=['REQUIRE GLOBcomp_2 AS ethan…, explanat… | 869 | DISCARD ←in 970 | 808 | 18.9 |
| 9 | 11 | `block_search_adv` | compound_match=all, compounds=['REQUIRE GLOBcomp_2… | 1,282 | KEEP ←in 4,949 | 1282 | 25.0 |
| 10 | 12 | `inspect_block_table` | block_number=GLOBlit_220::PROPblock_2, purpose=Che… | 2,089 | — | — | 0.6 |
| 11 | 1 | `query_thermoml` | instruction=Search for blocks containing:…, purpos… | 47,714 | — | — | 326.1 |
| 12 | 4 | `inspect_block` | block_number=PROPblock_2, doi=10.1016/j.fluid.2004… | 1,374 | — | — | 0.5 |
| 13 | 8 | `fit_block` | block_number=PROPblock_2, composition_hint=mole_fr… | 259 | — | — | 0.2 |
| 14 | 12 | `fit_block` | block_number=PROPblock_2, doi=10.1016/j.fluid.2004… | 852 | — | — | 2.9 |
| 15 | 13 | `list_session_files` |  | 1,689 | — | — | 0.0 |
| | | **TOTAL (15 tools)** | | **58,126** | | **3,160** | **457.2** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 809 | 23,327 | 981 | 7.6 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,080 | 25,175 | 618 | 5.5 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,095 | 26,190 | 515 | 3.9 |
| 4 | L1-worker | claudeopus46 | 3,767 | 437 | 4,204 | 210 | 2.8 |
| 5 | L1-worker | claudeopus46 | 3,767 | 647 | 4,414 | 377 | 3.6 |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,669 | 25,764 | 780 | 7.0 |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,357 | 26,452 | 755 | 5.2 |
| 8 | L1-worker | claudeopus46 | 3,767 | 14,641 | 18,408 | 1,651 | 14.9 |
| 9 | L1-worker | claudeopus46 | 3,767 | 14,851 | 18,618 | 1,632 | 15.0 |
| 10 | L1-worker | claudeopus46 | 24,095 | 2,637 | 26,732 | 2,282 | 18.8 |
| 11 | L1-worker | claudeopus46 | 24,095 | 3,324 | 27,419 | 1,831 | 12.6 |
| 12 | L1-worker | claudeopus46 | 3,767 | 14,578 | 18,345 | 1,645 | 14.7 |
| 13 | L1-worker | claudeopus46 | 3,767 | 14,788 | 18,555 | 1,835 | 16.0 |
| 14 | L1-worker | claudeopus46 | 24,095 | 4,172 | 28,267 | 1,314 | 8.8 |
| 15 | L1-worker | claudeopus46 | 24,095 | 4,852 | 28,947 | 608 | 7.5 |
| 16 | L1-worker | claudeopus46 | 24,095 | 5,457 | 29,552 | 1,337 | 9.5 |
| 17 | L1-worker | claudeopus46 | 3,767 | 407 | 4,174 | 386 | 4.1 |
| 18 | L1-worker | claudeopus46 | 24,095 | 6,079 | 30,174 | 1,405 | 10.4 |
| 19 | L1-worker | claudeopus46 | 3,767 | 1,228 | 4,995 | 1,279 | 9.7 |
| 20 | L1-worker | claudeopus46 | 24,095 | 7,349 | 31,444 | 1,842 | 12.3 |
| 21 | L1-worker | claudeopus46 | 3,767 | 5,147 | 8,914 | 1,553 | 13.5 |
| 22 | L1-worker | claudeopus46 | 24,095 | 9,063 | 33,158 | 1,019 | 8.4 |
| 23 | L1-worker | claudeopus46 | 24,062 | 11,291 | 35,353 | 2,896 | 25.9 |
| 24 | L1-worker | claudeopus46 | 24,062 | 16,334 | 40,396 | 3,933 | 29.1 |
| 25 | L1-worker | claudeopus46 | 627 | 3,942 | 4,569 | 1,000 | 7.4 |
| 26 | L1-worker | claudeopus46 | 2,320 | 4,062 | 6,382 | 1,034 | 8.7 |
| 27 | L1-worker | claudeopus46 | 2,106 | 5,263 | 7,369 | 2,576 | 11.0 |
| 28 | L1-worker | claudeopus46 | 366 | 1,471 | 1,837 | 994 | 4.4 |
| 29 | L1-worker | claudeopus46 | 366 | 3,353 | 3,719 | 1,873 | 7.8 |
| 30 | L1-worker | claudeopus46 | 787 | 45,235 | 46,022 | 831 | 9.2 |
| 31 | L0-main | claudeopus46 | 22,518 | 27,106 | 49,624 | 2,482 | 21.4 |
| 32 | L0-main | claudeopus46 | 22,518 | 27,982 | 50,500 | 602 | 5.0 |
| 33 | L0-main | claudeopus46 | 22,518 | 28,677 | 51,195 | 674 | 6.5 |
| 34 | L0-main | claudeopus46 | 22,518 | 30,195 | 52,713 | 1,705 | 12.1 |
| 35 | L0-main | claudeopus46 | 22,518 | 30,934 | 53,452 | 987 | 7.6 |
| 36 | L0-main | claudeopus46 | 22,518 | 31,616 | 54,134 | 978 | 8.1 |
| 37 | L0-main | claudeopus46 | 22,518 | 32,325 | 54,843 | 925 | 7.1 |
| 38 | L0-main | claudeopus46 | 22,518 | 32,119 | 54,637 | 933 | 7.2 |
| 39 | L0-main | claudeopus46 | 22,518 | 32,833 | 55,351 | 917 | 6.5 |
| 40 | L0-main | claudeopus46 | 22,518 | 33,522 | 56,040 | 924 | 6.6 |
| 41 | L0-main | claudeopus46 | 22,518 | 34,232 | 56,750 | 881 | 6.7 |
| 42 | L0-main | claudeopus46 | 22,518 | 35,859 | 58,377 | 1,219 | 11.0 |
| 43 | L0-main | claudeopus46 | 22,518 | 37,947 | 60,465 | 3,068 | 23.9 |
| 44 | L0-main | claudeopus46 | 2,106 | 4,105 | 6,211 | 154 | 2.3 |
| 45 | L0-main | claudeopus46 | 366 | 677 | 1,043 | 195 | 3.3 |
| 46 | L0-main | claudeopus46 | 2,320 | 3,197 | 5,517 | 993 | 6.5 |
| 47 | L0-main | claudeopus46 | 366 | 1,430 | 1,796 | 958 | 4.3 |
| 48 | L0-main | claudeopus46 | 560 | 3,718 | 4,278 | 100 | 2.2 |
| 49 | L0-main | claudeopus46 | 1,156 | 4,516 | 5,672 | 454 | 4.9 |
| 50 | L0-main | claudeopus46 | 1,918 | 6,280 | 8,198 | 1,178 | 10.6 |

