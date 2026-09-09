# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:29:30
**Wall time (at last flush):** 474.4 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 27 | 459,152 | 644,080 | 36,549 | 1,103,232 | 40,860 | 286.8 | claudeopus46 |
| L1-worker | 17 | 230,961 | 120,239 | 23,375 | 351,200 | 20,658 | 183.9 | claudeopus46 |
| **TOTAL** | **44** | **690,113** | **764,319** | **59,924** | **1,454,432** | **33,055** | **470.7** | |

**Estimated tokens:** ~363,608 input + ~14,981 output = ~378,589 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 7 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 6 | 3 | 14 | 14 | 534 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 2 | 1 | 2 | 2 | 0 |
| **TOTAL** | **11** | **2** | **8** | **4** | **16** | **16** | **534** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_5494 |  | resolve_compound_ids |
| GLOBcomp_6173 |  | resolve_compound_ids |
| GLOBcomp_6171 |  | resolve_compound_ids |
| GLOBcomp_6172 |  | resolve_compound_ids |
| GLOBcomp_4 |  | resolve_compound_ids |
| GLOBcomp_1 |  | query_thermoml, resolve_compound_ids, search_blocks |

#### References (14 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_1742 |  | search_blocks |
| GLOBlit_2092 |  | search_blocks |
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_5201 |  | query_thermoml, search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_8949 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_10699 |  | search_blocks |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | query_thermoml, search_blocks |
| GLOBlit_11459 |  | search_blocks |
| GLOBlit_11792 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | query_thermoml, search_blocks |

#### Measurements (8 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_988 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | query_thermoml, search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, search_blocks |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_18 | Volume fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_2 |  | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 7 |
| Unique References | 14 |
| Unique Properties | 1 |
| Unique Measurements | 8 |
| Unique Phases | 1 |
| Unique Variables | 6 |
| Unique Constraints | 3 |
| Unique Solvents | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 14 |
| Unique parent blocks | 14 |
| Explicit block/subsystem targets | 14 |
| Subsystem targets | 0 |
| Target-matched data points | 742 |

---

## 3. DOI & Block References

**Unique DOIs:** 14  |  **Parent blocks:** 14  |  **Explicit targets:** 14  |  **Subsystems:** 0  |  **Target-matched datapoints:** 534

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2015.07.012 | 1 | 84 | binary | search_blocks |
| 10.1016/j.fluid.2017.09.005 | 1 | 72 | binary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 1 | 37 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 100 | binary | query_thermoml, search_blocks |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | search_blocks |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | search_blocks |
| 10.1021/je060219e | 1 | 26 | binary | search_blocks |
| 10.1021/je4003515 | 1 | 25 | binary | search_blocks |
| 10.1021/je600565m | 1 | 17 | binary | search_blocks |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks |
| 10.1021/je800150h | 1 | 108 | binary | query_thermoml, search_blocks |
| 10.1021/je800942u | 1 | 18 | binary | search_blocks |
| 10.1021/je900743e | 1 | 15 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2015.07.012 | PROPblock_4 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_4 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_21 | declared | 100 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_11 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_18 | declared | 9 | binary | — | search_blocks |
| 10.1021/je060219e | PROPblock_1 | declared | 26 | binary | — | search_blocks |
| 10.1021/je4003515 | PROPblock_8 | declared | 25 | binary | — | search_blocks |
| 10.1021/je600565m | PROPblock_5 | declared | 17 | binary | — | search_blocks |
| 10.1021/je700618y | PROPblock_7 | declared | 15 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_8 | declared | 108 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je800942u | PROPblock_5 | declared | 18 | binary | — | search_blocks |
| 10.1021/je900743e | PROPblock_2 | declared | 15 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `resolve_compound_ids` | purpose=Resolve ethanol and water to …, queries=['… | 282 | KEEP ←in 652 | 282 | 8.8 |
| 2 | 2 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 913 | KEEP ←in 8,844 | 867 | 23.5 |
| 3 | 3 | `inspect_block_table` | block_number=PROPblock_21, literature=GLOBlit_5201… | 251 | — | — | 0.2 |
| 4 | 4 | `inspect_block_table` | block_number=PROPblock_21, literature=GLOBlit_5201… | 376 | — | — | 0.2 |
| 5 | 5 | `inspect_block_table` | block_number=PROPblock_21, literature=GLOBlit_5201… | 1,628 | — | — | 0.1 |
| 6 | 7 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_11136… | 2,687 | — | — | 1.1 |
| 7 | 1 | `query_thermoml` | instruction=Search for blocks containing …, purpos… | 32,069 | — | — | 179.6 |
| 8 | 4 | `inspect_block` | block_number=PROPblock_21, doi=10.1016/j.jct.2018.… | 1,363 | — | — | 0.1 |
| 9 | 7 | `fit_block` | block_number=PROPblock_21, doi=10.1016/j.jct.2018.… | 889 | — | — | 1.7 |
| 10 | 11 | `fit_multi_system` | purpose=Fit viscosity of ethanol+wate…, systems=[{… | 758 | — | — | 0.2 |
| 11 | 15 | `fit_multi_system` | purpose=Fit viscosity of ethanol+wate…, systems=[{… | 2,088 | — | — | 5.7 |
| 12 | 16 | `predict_from_rk` | coeffs=[2.77791, -2.36884, 2.91661, …, mixing_rule… | 213 | — | — | 0.1 |
| 13 | 17 | `predict_from_rk` | coeffs=[2.728, -2.49259, 2.55005, -2…, mixing_rule… | 213 | — | — | 0.1 |
| 14 | 18 | `predict_from_rk` | coeffs=[2.47975, -2.12, 2.38699, -3.…, mixing_rule… | 215 | — | — | 0.3 |
| 15 | 19 | `predict_from_rk` | coeffs=[2.33015, -1.95628, 2.03149, …, n_points=20… | 214 | — | — | 0.1 |
| | | **TOTAL (15 tools)** | | **44,159** | | **1,149** | **221.8** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 339 | 22,857 | 1,332 | 8.7 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,051 | 25,146 | 758 | 5.5 |
| 3 | L1-worker | claudeopus46 | 3,767 | 811 | 4,578 | 574 | 8.0 |
| 4 | L1-worker | claudeopus46 | 24,095 | 1,606 | 25,701 | 799 | 6.3 |
| 5 | L1-worker | claudeopus46 | 3,767 | 9,307 | 13,074 | 1,732 | 15.5 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,869 | 26,964 | 1,020 | 7.5 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,570 | 27,665 | 588 | 5.1 |
| 8 | L1-worker | claudeopus46 | 24,095 | 4,294 | 28,389 | 653 | 5.3 |
| 9 | L1-worker | claudeopus46 | 24,095 | 6,273 | 30,368 | 2,830 | 19.8 |
| 10 | L1-worker | claudeopus46 | 24,095 | 11,606 | 35,701 | 1,061 | 10.4 |
| 11 | L1-worker | claudeopus46 | 24,095 | 14,654 | 38,749 | 3,029 | 23.8 |
| 12 | L1-worker | claudeopus46 | 24,095 | 21,754 | 45,849 | 4,383 | 30.2 |
| 13 | L1-worker | claudeopus46 | 2,320 | 4,715 | 7,035 | 973 | 6.7 |
| 14 | L1-worker | claudeopus46 | 627 | 4,595 | 5,222 | 1,172 | 8.2 |
| 15 | L1-worker | claudeopus46 | 366 | 1,410 | 1,776 | 938 | 4.2 |
| 16 | L1-worker | claudeopus46 | 2,106 | 5,887 | 7,993 | 1,305 | 14.7 |
| 17 | L1-worker | claudeopus46 | 366 | 2,082 | 2,448 | 946 | 5.0 |
| 18 | L1-worker | claudeopus46 | 787 | 23,755 | 24,542 | 614 | 7.7 |
| 19 | L0-main | claudeopus46 | 22,518 | 23,204 | 45,722 | 2,898 | 21.9 |
| 20 | L0-main | claudeopus46 | 22,518 | 24,092 | 46,610 | 534 | 4.8 |
| 21 | L0-main | claudeopus46 | 22,518 | 24,763 | 47,281 | 564 | 4.5 |
| 22 | L0-main | claudeopus46 | 22,518 | 26,313 | 48,831 | 2,615 | 19.1 |
| 23 | L0-main | claudeopus46 | 22,518 | 27,074 | 49,592 | 1,356 | 9.0 |
| 24 | L0-main | claudeopus46 | 22,518 | 27,802 | 50,320 | 1,463 | 11.2 |
| 25 | L0-main | claudeopus46 | 22,518 | 29,843 | 52,361 | 2,427 | 14.4 |
| 26 | L0-main | claudeopus46 | 22,518 | 30,578 | 53,096 | 1,762 | 9.5 |
| 27 | L0-main | claudeopus46 | 22,518 | 31,281 | 53,799 | 1,794 | 25.7 |
| 28 | L0-main | claudeopus46 | 22,518 | 32,017 | 54,535 | 1,666 | 9.5 |
| 29 | L0-main | claudeopus46 | 22,518 | 32,172 | 54,690 | 1,599 | 9.0 |
| 30 | L0-main | claudeopus46 | 22,518 | 32,811 | 55,329 | 1,619 | 11.0 |
| 31 | L0-main | claudeopus46 | 22,518 | 33,432 | 55,950 | 1,742 | 10.1 |
| 32 | L0-main | claudeopus46 | 22,518 | 34,112 | 56,630 | 1,591 | 8.5 |
| 33 | L0-main | claudeopus46 | 22,518 | 40,063 | 62,581 | 892 | 8.3 |
| 34 | L0-main | claudeopus46 | 22,518 | 40,674 | 63,192 | 704 | 10.4 |
| 35 | L0-main | claudeopus46 | 22,518 | 41,256 | 63,774 | 727 | 8.3 |
| 36 | L0-main | claudeopus46 | 22,518 | 41,870 | 64,388 | 611 | 9.9 |
| 37 | L0-main | claudeopus46 | 22,518 | 42,424 | 64,942 | 4,270 | 34.2 |
| 38 | L0-main | claudeopus46 | 2,106 | 4,853 | 6,959 | 154 | 2.8 |
| 39 | L0-main | claudeopus46 | 366 | 677 | 1,043 | 137 | 2.7 |
| 40 | L0-main | claudeopus46 | 2,320 | 4,399 | 6,719 | 1,172 | 8.5 |
| 41 | L0-main | claudeopus46 | 366 | 1,609 | 1,975 | 1,127 | 4.5 |
| 42 | L0-main | claudeopus46 | 560 | 4,920 | 5,480 | 106 | 2.7 |
| 43 | L0-main | claudeopus46 | 1,156 | 5,713 | 6,869 | 561 | 5.2 |
| 44 | L0-main | claudeopus46 | 1,918 | 5,789 | 7,707 | 1,126 | 12.4 |

