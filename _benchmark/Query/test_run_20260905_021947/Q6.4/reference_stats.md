# Reference Stats — query-agent

**Run started:** 2026-09-05 06:03:05
**Wall time (at last flush):** 194.9 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 30,402 | 38,403 | 9,711 | 68,805 | 7,645 | 59.6 | claudeopus46 |
| L1-worker | 21 | 327,308 | 135,782 | 19,927 | 463,090 | 22,051 | 149.2 | claudeopus46 |
| **TOTAL** | **30** | **357,710** | **174,185** | **29,638** | **531,895** | **17,729** | **208.8** | |

**Estimated tokens:** ~132,973 input + ~7,409 output = ~140,382 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 1 | 1 | 2 | 1 | 10 | 10 | 28 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **2** | **1** | **2** | **1** | **10** | **10** | **28** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_31 |  | resolve_compound_ids, search_blocks |

#### References (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_57 |  | search_blocks |
| GLOBlit_86 |  | search_blocks |
| GLOBlit_779 |  | search_blocks |
| GLOBlit_938 |  | search_blocks |
| GLOBlit_1246 |  | search_blocks |
| GLOBlit_1559 |  | search_blocks |
| GLOBlit_1775 |  | search_blocks |
| GLOBlit_2404 |  | search_blocks |
| GLOBlit_2435 |  | search_blocks |
| GLOBlit_2588 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |

#### Measurements (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_179 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |

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
| Unique Measurements | 5 |
| Unique Phases | 1 |
| Unique Variables | 2 |
| Unique Constraints | 1 |
| Total DOIs | 10 |
| Unique parent blocks | 10 |
| Explicit block/subsystem targets | 10 |
| Subsystem targets | 0 |
| Target-matched data points | 28 |

---

## 3. DOI & Block References

**Unique DOIs:** 10  |  **Parent blocks:** 10  |  **Explicit targets:** 10  |  **Subsystems:** 0  |  **Target-matched datapoints:** 28

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1007/s10765-008-0395-z | 1 | 1 | unary | search_blocks |
| 10.1007/s10765-009-0648-5 | 1 | 5 | unary | search_blocks |
| 10.1016/j.fluid.2010.01.002 | 1 | 4 | unary | search_blocks |
| 10.1016/j.fluid.2011.02.010 | 1 | 5 | unary | search_blocks |
| 10.1016/j.fluid.2013.05.001 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2014.09.022 | 1 | 8 | unary | search_blocks |
| 10.1016/j.fluid.2015.08.014 | 1 | 1 | unary | search_blocks |
| 10.1016/j.jct.2004.04.004 | 1 | 1 | unary | search_blocks |
| 10.1016/j.jct.2004.07.024 | 1 | 1 | unary | search_blocks |
| 10.1016/j.jct.2005.07.018 | 1 | 1 | unary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1007/s10765-008-0395-z | PROPblock_7 | declared | 1 | unary | — | search_blocks |
| 10.1007/s10765-009-0648-5 | PROPblock_4 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.fluid.2010.01.002 | PROPblock_3 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.fluid.2011.02.010 | PROPblock_3 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.fluid.2013.05.001 | PROPblock_1 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2014.09.022 | PROPblock_1 | declared | 8 | unary | — | search_blocks |
| 10.1016/j.fluid.2015.08.014 | PROPblock_6 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2004.04.004 | PROPblock_2 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2004.07.024 | PROPblock_2 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2005.07.018 | PROPblock_9 | declared | 1 | unary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve DMSO to its… | 197 | KEEP ←in 239 | 197 | 4.1 |
| 2 | 4 | `search_blocks` | compound=GLOBcomp_31, limit=10, property=GLOBprop_… | 1,087 | KEEP ←in 5,604 | 1087 | 13.0 |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_7, literature=GLOBlit_57, n… | 261 | — | — | 0.0 |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_7, literature=GLOBlit_57, n… | 335 | — | — | 0.1 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_86, n… | 843 | — | — | 0.1 |
| 6 | 9 | `inspect_block_table` | block_number=GLOBlit_57::PROPblock_7, nearest={'co… | 656 | — | — | 0.1 |
| 7 | 10 | `inspect_block_table` | block_number=GLOBlit_779::PROPblock_3, nearest={'c… | 765 | — | — | 0.6 |
| 8 | 11 | `inspect_block_table` | block_number=GLOBlit_938::PROPblock_3, nearest={'c… | 773 | — | — | 0.1 |
| 9 | 12 | `inspect_block_table` | block_number=GLOBlit_1246::PROPblock_1, nearest={'… | 648 | — | — | 0.1 |
| 10 | 1 | `L1_query` | context=User needs density of pure li…, id_catalog… | 29,280 | — | — | 141.2 |
| | | **TOTAL (10 tools)** | | **34,845** | | **1,284** | **159.4** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 605 | 12,186 | 736 | 6.2 |
| 2 | L1-worker | claudeopus46 | 24,095 | 888 | 24,983 | 587 | 5.4 |
| 3 | L1-worker | claudeopus46 | 24,095 | 1,906 | 26,001 | 520 | 4.1 |
| 4 | L1-worker | claudeopus46 | 3,767 | 401 | 4,168 | 316 | 4.0 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,500 | 25,595 | 716 | 6.7 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,175 | 26,270 | 645 | 5.3 |
| 7 | L1-worker | claudeopus46 | 3,767 | 6,027 | 9,794 | 1,398 | 11.8 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,219 | 27,314 | 812 | 6.9 |
| 9 | L1-worker | claudeopus46 | 24,095 | 3,791 | 27,886 | 539 | 4.8 |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,401 | 28,496 | 990 | 8.4 |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,614 | 29,709 | 2,198 | 14.7 |
| 12 | L1-worker | claudeopus46 | 24,095 | 11,228 | 35,323 | 730 | 7.1 |
| 13 | L1-worker | claudeopus46 | 24,095 | 12,176 | 36,271 | 708 | 6.2 |
| 14 | L1-worker | claudeopus46 | 24,095 | 13,327 | 37,422 | 586 | 4.9 |
| 15 | L1-worker | claudeopus46 | 24,095 | 14,384 | 38,479 | 620 | 4.8 |
| 16 | L1-worker | claudeopus46 | 24,062 | 15,061 | 39,123 | 2,040 | 16.2 |
| 17 | L1-worker | claudeopus46 | 2,320 | 2,171 | 4,491 | 766 | 4.4 |
| 18 | L1-worker | claudeopus46 | 627 | 2,051 | 2,678 | 760 | 6.1 |
| 19 | L1-worker | claudeopus46 | 366 | 1,203 | 1,569 | 726 | 3.4 |
| 20 | L1-worker | claudeopus46 | 2,106 | 3,180 | 5,286 | 2,292 | 10.4 |
| 21 | L1-worker | claudeopus46 | 366 | 3,069 | 3,435 | 1,326 | 6.7 |
| 22 | L1-worker | claudeopus46 | 787 | 28,010 | 28,797 | 652 | 6.9 |
| 23 | L0-main | claudeopus46 | 11,581 | 17,597 | 29,178 | 1,916 | 14.9 |
| 24 | L0-main | claudeopus46 | 2,320 | 2,084 | 4,404 | 616 | 4.1 |
| 25 | L0-main | claudeopus46 | 2,106 | 2,521 | 4,627 | 1,014 | 6.3 |
| 26 | L0-main | claudeopus46 | 366 | 1,091 | 1,457 | 577 | 2.8 |
| 27 | L0-main | claudeopus46 | 366 | 1,563 | 1,929 | 987 | 4.7 |
| 28 | L0-main | claudeopus46 | 560 | 3,709 | 4,269 | 443 | 3.4 |
| 29 | L0-main | claudeopus46 | 1,156 | 6,674 | 7,830 | 1,866 | 11.2 |
| 30 | L0-main | claudeopus46 | 366 | 2,559 | 2,925 | 1,556 | 6.0 |

