# Reference Stats — query-agent

**Run started:** 2026-09-05 05:02:27
**Wall time (at last flush):** 171.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 30,036 | 22,285 | 6,389 | 52,321 | 6,540 | 46.9 | claudeopus46 |
| L1-worker | 19 | 280,013 | 89,752 | 15,127 | 369,765 | 19,461 | 122.4 | claudeopus46 |
| verdict | 1 | 972 | 3,911 | 983 | 4,883 | 4,883 | 8.4 | claudeopus46 |
| **TOTAL** | **28** | **311,021** | **115,948** | **22,499** | **426,969** | **15,248** | **177.7** | |

**Estimated tokens:** ~106,742 input + ~5,624 output = ~112,366 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 1 | 1 | 2 | 1 | 10 | 10 | 60 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **2** | **1** | **2** | **1** | **10** | **10** | **60** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |

#### References (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_14 |  | search_blocks |
| GLOBlit_306 |  | search_blocks |
| GLOBlit_555 |  | search_blocks |
| GLOBlit_560 |  | search_blocks |
| GLOBlit_604 |  | search_blocks |
| GLOBlit_645 |  | search_blocks |
| GLOBlit_725 |  | search_blocks |
| GLOBlit_779 |  | search_blocks |
| GLOBlit_1136 |  | search_blocks |
| GLOBlit_1147 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |

#### Measurements (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |

#### Phases (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_10 |  | search_blocks |
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
| Unique Measurements | 6 |
| Unique Phases | 2 |
| Unique Variables | 2 |
| Unique Constraints | 1 |
| Total DOIs | 10 |
| Unique parent blocks | 10 |
| Explicit block/subsystem targets | 10 |
| Subsystem targets | 0 |
| Target-matched data points | 60 |

---

## 3. DOI & Block References

**Unique DOIs:** 10  |  **Parent blocks:** 10  |  **Explicit targets:** 10  |  **Subsystems:** 0  |  **Target-matched datapoints:** 60

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1007/s10765-005-8590-7 | 1 | 42 | unary | search_blocks |
| 10.1016/j.fluid.2005.09.009 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2007.07.066 | 1 | 5 | unary | search_blocks |
| 10.1016/j.fluid.2007.08.008 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2008.02.008 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2008.07.001 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2009.07.010 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2010.01.002 | 1 | 4 | unary | search_blocks |
| 10.1016/j.fluid.2012.07.032 | 1 | 3 | unary | search_blocks |
| 10.1016/j.fluid.2012.08.024 | 1 | 1 | unary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1007/s10765-005-8590-7 | PROPblock_1 | declared | 42 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.09.009 | PROPblock_6 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2007.07.066 | PROPblock_2 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.fluid.2007.08.008 | PROPblock_6 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2008.02.008 | PROPblock_38 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2008.07.001 | PROPblock_8 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2009.07.010 | PROPblock_11 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2010.01.002 | PROPblock_18 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.fluid.2012.07.032 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.fluid.2012.08.024 | PROPblock_1 | declared | 1 | unary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve water compo… | 190 | KEEP ←in 216 | 190 | 4.0 |
| 2 | 4 | `search_blocks` | compound=GLOBcomp_1, limit=10, property=GLOBprop_1… | 1,234 | KEEP ←in 5,651 | 1220 | 15.1 |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_306, … | 261 | — | — | 0.0 |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_306, … | 333 | — | — | 0.1 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_555, … | 777 | — | — | 0.1 |
| 6 | 9 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_306, … | 640 | — | — | 0.1 |
| 7 | 1 | `L1_query` | context=User needs pure water density…, id_catalog… | 12,232 | — | — | 121.4 |
| | | **TOTAL (7 tools)** | | **15,667** | | **1,410** | **140.8** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 825 | 12,406 | 972 | 7.9 |
| 2 | L1-worker | claudeopus46 | 24,095 | 995 | 25,090 | 793 | 6.7 |
| 3 | L1-worker | claudeopus46 | 24,095 | 1,987 | 26,082 | 516 | 4.0 |
| 4 | L1-worker | claudeopus46 | 3,767 | 343 | 4,110 | 314 | 3.5 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,622 | 25,717 | 692 | 6.0 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,341 | 26,436 | 661 | 4.7 |
| 7 | L1-worker | claudeopus46 | 3,767 | 6,058 | 9,825 | 1,527 | 12.0 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,560 | 27,655 | 975 | 7.9 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,209 | 28,304 | 648 | 5.4 |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,905 | 29,000 | 1,148 | 8.4 |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,063 | 30,158 | 1,203 | 8.7 |
| 12 | L1-worker | claudeopus46 | 24,095 | 9,989 | 34,084 | 870 | 12.5 |
| 13 | L1-worker | claudeopus46 | 24,095 | 10,992 | 35,087 | 1,267 | 9.7 |
| 14 | L1-worker | claudeopus46 | 24,095 | 14,722 | 38,817 | 1,131 | 7.3 |
| 15 | L1-worker | claudeopus46 | 2,320 | 1,262 | 3,582 | 284 | 3.0 |
| 16 | L1-worker | claudeopus46 | 627 | 1,142 | 1,769 | 622 | 4.2 |
| 17 | L1-worker | claudeopus46 | 2,106 | 2,378 | 4,484 | 951 | 5.7 |
| 18 | L1-worker | claudeopus46 | 366 | 1,728 | 2,094 | 514 | 3.4 |
| 19 | L1-worker | claudeopus46 | 1,228 | 3,380 | 4,608 | 538 | 3.5 |
| 20 | L1-worker | claudeopus46 | 787 | 12,076 | 12,863 | 473 | 5.8 |
| 21 | L0-main | claudeopus46 | 11,581 | 9,091 | 20,672 | 1,754 | 11.9 |
| 22 | L0-main | claudeopus46 | 2,320 | 1,643 | 3,963 | 594 | 4.1 |
| 23 | L0-main | claudeopus46 | 2,106 | 2,300 | 4,406 | 758 | 5.6 |
| 24 | L0-main | claudeopus46 | 366 | 1,069 | 1,435 | 555 | 3.1 |
| 25 | L0-main | claudeopus46 | 366 | 1,307 | 1,673 | 852 | 4.8 |
| 26 | L0-main | claudeopus46 | 560 | 2,412 | 2,972 | 187 | 4.1 |
| 27 | L0-main | claudeopus46 | 1,156 | 3,638 | 4,794 | 717 | 5.4 |
| 28 | verdict | claudeopus46 | 972 | 3,911 | 4,883 | 983 | 8.4 |

