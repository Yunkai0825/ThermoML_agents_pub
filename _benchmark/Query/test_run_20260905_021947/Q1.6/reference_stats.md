# Reference Stats — query-agent

**Run started:** 2026-09-05 05:25:56
**Wall time (at last flush):** 166.0 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 30,036 | 24,775 | 7,541 | 54,811 | 6,851 | 47.1 | claudeopus46 |
| L1-worker | 19 | 279,151 | 90,432 | 17,473 | 369,583 | 19,451 | 131.6 | claudeopus46 |
| **TOTAL** | **27** | **309,187** | **115,207** | **25,014** | **424,394** | **15,718** | **178.7** | |

**Estimated tokens:** ~106,098 input + ~6,253 output = ~112,351 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 1 | 1 | 2 | 1 | 10 | 10 | 110 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **2** | **1** | **2** | **1** | **10** | **10** | **110** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |

#### References (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_1310 |  | search_blocks |
| GLOBlit_1445 |  | search_blocks |
| GLOBlit_1986 |  | search_blocks |
| GLOBlit_2622 |  | search_blocks |
| GLOBlit_3019 |  | search_blocks |
| GLOBlit_3054 |  | search_blocks |
| GLOBlit_4832 |  | search_blocks |
| GLOBlit_7221 |  | search_blocks |
| GLOBlit_7754 |  | search_blocks |
| GLOBlit_11179 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_9 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |

#### Measurements (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_31 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_12 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_132 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_9 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |

#### Constraints (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 1 |
| Unique References | 10 |
| Unique Properties | 1 |
| Unique Measurements | 4 |
| Unique Phases | 1 |
| Unique Variables | 2 |
| Unique Constraints | 1 |
| Total DOIs | 10 |
| Unique parent blocks | 10 |
| Explicit block/subsystem targets | 10 |
| Subsystem targets | 0 |
| Target-matched data points | 110 |

---

## 3. DOI & Block References

**Unique DOIs:** 10  |  **Parent blocks:** 10  |  **Explicit targets:** 10  |  **Subsystems:** 0  |  **Target-matched datapoints:** 110

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2013.08.005 | 1 | 8 | unary | search_blocks |
| 10.1016/j.fluid.2014.03.017 | 1 | 28 | unary | search_blocks |
| 10.1016/j.fluid.2016.10.005 | 1 | 9 | unary | search_blocks |
| 10.1016/j.jct.2005.10.010 | 1 | 15 | unary | search_blocks |
| 10.1016/j.jct.2008.10.002 | 1 | 6 | unary | search_blocks |
| 10.1016/j.jct.2009.01.011 | 1 | 16 | unary | search_blocks |
| 10.1016/j.jct.2016.09.031 | 1 | 1 | unary | search_blocks |
| 10.1021/acs.jced.7b00483 | 1 | 14 | unary | search_blocks |
| 10.1021/acs.jced.8b01174 | 1 | 6 | unary | search_blocks |
| 10.1021/je800248w | 1 | 7 | unary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2013.08.005 | PROPblock_1 | declared | 8 | unary | — | search_blocks |
| 10.1016/j.fluid.2014.03.017 | PROPblock_3 | declared | 28 | unary | — | search_blocks |
| 10.1016/j.fluid.2016.10.005 | PROPblock_2 | declared | 9 | unary | — | search_blocks |
| 10.1016/j.jct.2005.10.010 | PROPblock_1 | declared | 15 | unary | — | search_blocks |
| 10.1016/j.jct.2008.10.002 | PROPblock_1 | declared | 6 | unary | — | search_blocks |
| 10.1016/j.jct.2009.01.011 | PROPblock_8 | declared | 16 | unary | — | search_blocks |
| 10.1016/j.jct.2016.09.031 | PROPblock_1 | declared | 1 | unary | — | search_blocks |
| 10.1021/acs.jced.7b00483 | PROPblock_1 | declared | 14 | unary | — | search_blocks |
| 10.1021/acs.jced.8b01174 | PROPblock_5 | declared | 6 | unary | — | search_blocks |
| 10.1021/je800248w | PROPblock_1 | declared | 7 | unary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve water compo… | 181 | KEEP ←in 216 | 181 | 4.4 |
| 2 | 4 | `search_blocks` | compound=GLOBcomp_1, limit=10, property=GLOBprop_9… | 970 | KEEP ←in 5,937 | 955 | 16.1 |
| 3 | 5 | `inspect_block_table` | block_number=GLOBlit_4832::PROPblock_1, nearest=T=… | 249 | — | — | 0.0 |
| 4 | 6 | `inspect_block_table` | block_number=GLOBlit_4832::PROPblock_1, nearest={'… | 365 | — | — | 0.2 |
| 5 | 7 | `inspect_block_table` | block_number=GLOBlit_4832::PROPblock_1, nearest={'… | 714 | — | — | 0.1 |
| 6 | 8 | `inspect_block_table` | block_number=GLOBlit_1310::PROPblock_1, nearest={'… | 855 | — | — | 0.2 |
| 7 | 1 | `L1_query` | context=Property ID for molar Cp is G…, id_catalog… | 13,682 | — | — | 124.9 |
| | | **TOTAL (7 tools)** | | **17,016** | | **1,136** | **145.9** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 562 | 12,143 | 1,126 | 8.3 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,053 | 25,148 | 584 | 4.6 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,040 | 26,135 | 505 | 5.0 |
| 4 | L1-worker | claudeopus46 | 3,767 | 360 | 4,127 | 320 | 4.1 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,652 | 25,747 | 776 | 6.3 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,352 | 26,447 | 732 | 5.2 |
| 7 | L1-worker | claudeopus46 | 3,767 | 6,390 | 10,157 | 1,609 | 14.4 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,287 | 27,382 | 1,015 | 7.9 |
| 9 | L1-worker | claudeopus46 | 24,095 | 3,929 | 28,024 | 560 | 5.1 |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,610 | 28,705 | 907 | 7.8 |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,724 | 29,819 | 709 | 6.2 |
| 12 | L1-worker | claudeopus46 | 24,095 | 6,948 | 31,043 | 1,306 | 10.0 |
| 13 | L1-worker | claudeopus46 | 24,095 | 11,086 | 35,181 | 2,559 | 16.4 |
| 14 | L1-worker | claudeopus46 | 24,095 | 16,012 | 40,107 | 1,769 | 9.8 |
| 15 | L1-worker | claudeopus46 | 627 | 2,107 | 2,734 | 472 | 3.6 |
| 16 | L1-worker | claudeopus46 | 2,320 | 2,227 | 4,547 | 674 | 4.7 |
| 17 | L1-worker | claudeopus46 | 2,106 | 3,401 | 5,507 | 1,059 | 5.4 |
| 18 | L1-worker | claudeopus46 | 366 | 883 | 1,249 | 459 | 3.0 |
| 19 | L1-worker | claudeopus46 | 366 | 1,836 | 2,202 | 786 | 4.3 |
| 20 | L1-worker | claudeopus46 | 787 | 14,535 | 15,322 | 672 | 7.8 |
| 21 | L0-main | claudeopus46 | 11,581 | 11,071 | 22,652 | 1,980 | 13.2 |
| 22 | L0-main | claudeopus46 | 2,320 | 1,743 | 4,063 | 860 | 4.3 |
| 23 | L0-main | claudeopus46 | 2,106 | 2,137 | 4,243 | 812 | 5.7 |
| 24 | L0-main | claudeopus46 | 366 | 1,335 | 1,701 | 816 | 3.2 |
| 25 | L0-main | claudeopus46 | 366 | 1,361 | 1,727 | 906 | 4.0 |
| 26 | L0-main | claudeopus46 | 560 | 2,512 | 3,072 | 187 | 2.5 |
| 27 | L0-main | claudeopus46 | 1,156 | 4,054 | 5,210 | 854 | 5.9 |

