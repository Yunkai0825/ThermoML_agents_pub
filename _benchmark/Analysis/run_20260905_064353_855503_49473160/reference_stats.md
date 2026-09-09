# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:43:53
**Wall time (at last flush):** 857.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 30 | 504,422 | 2,200,932 | 53,033 | 2,705,354 | 90,178 | 401.8 | claudeopus46 |
| L1-worker | 58 | 707,485 | 464,787 | 75,188 | 1,172,272 | 20,211 | 603.3 | claudeopus46 |
| **TOTAL** | **88** | **1,211,907** | **2,665,719** | **128,221** | **3,877,626** | **44,063** | **1005.1** | |

**Estimated tokens:** ~969,406 input + ~32,055 output = ~1,001,461 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 0 | 4 | 4 | 1,599 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 3 | 0 | 2 | 2 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 1 | 1 | 2 | 0 | 1 | 1 | 15 |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 596 |
| `search_blocks` | 2 | 1 | 6 | 4 | 20 | 20 | 1,681 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 5 | 2 | 7 | 7 | 1,735 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 3 | 1 | 4 | 1 | 4 | 5 | 0 |
| **TOTAL** | **16** | **7** | **27** | **7** | **39** | **40** | **5,626** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | query_thermoml, query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | query_thermoml, query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_4 | methanol | query_thermoml_parallel, search_blocks |

#### References (23 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_220 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_1483 |  | query_thermoml, search_blocks |
| GLOBlit_1742 |  | query_thermoml, search_blocks |
| GLOBlit_2432 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2825 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_3475 |  | search_blocks |
| GLOBlit_5201 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_5473 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7629 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_8050 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9006 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_10699 |  | search_blocks |
| GLOBlit_10866 |  | search_blocks |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | search_blocks |
| GLOBlit_11459 |  | search_blocks |
| GLOBlit_11504 |  | search_blocks |
| GLOBlit_11792 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml, query_thermoml_parallel, search_blocks |

#### Measurements (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_138 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_236 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_203 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_212 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, query_thermoml_parallel, search_blocks |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBvar_3 | Pressure, kPa | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBvar_4 | Molality, mol/kg | query_thermoml_parallel, search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_15 | Mass ratio of solute to solvent | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | query_thermoml_parallel, search_blocks |
| GLOBsolvent_2 |  | search_blocks |

#### Block_Types (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml, query_thermoml_parallel |
| GLOBblocktype_2 |  | query_thermoml_parallel |

#### Constraints (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_22 | Volume fraction | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 3 |
| Unique References | 23 |
| Unique Properties | 1 |
| Unique Measurements | 10 |
| Unique Phases | 1 |
| Unique Variables | 6 |
| Unique Solvents | 2 |
| Unique Block_Types | 2 |
| Unique Constraints | 4 |
| Total DOIs | 23 |
| Unique parent blocks | 26 |
| Explicit block/subsystem targets | 26 |
| Subsystem targets | 0 |
| Target-matched data points | 7,468 |

---

## 3. DOI & Block References

**Unique DOIs:** 23  |  **Parent blocks:** 26  |  **Explicit targets:** 26  |  **Subsystems:** 0  |  **Target-matched datapoints:** 3,081

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2004.11.019 | 2 | 825 | binary, unary | query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | query_thermoml, search_blocks |
| 10.1016/j.fluid.2015.07.012 | 2 | 84 | binary | query_thermoml, search_blocks |
| 10.1016/j.jct.2004.07.019 | 2 | 1,161 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2007.05.004 | 1 | 37 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 244 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | search_blocks |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | search_blocks |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00723 | 1 | 3 | binary | search_blocks |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | search_blocks |
| 10.1021/je020173z | 1 | 24 | binary | search_blocks |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks |
| 10.1021/je060335h | 1 | 164 | binary | search_blocks |
| 10.1021/je4003515 | 1 | 23 | binary | search_blocks |
| 10.1021/je600565m | 1 | 18 | binary | search_blocks |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks |
| 10.1021/je800150h | 1 | 108 | binary | search_blocks |
| 10.1021/je800942u | 1 | 18 | binary | search_blocks |
| 10.1021/je900064e | 1 | 10 | binary | search_blocks |
| 10.1021/je900743e | 1 | 15 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2004.11.019 | PROPblock_1 | declared | 15 | unary | 1 | query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_1 | declared | 0 | — | — | query_thermoml |
| 10.1016/j.fluid.2015.07.012 | PROPblock_3 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00723 | PROPblock_12 | declared | 3 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | — | search_blocks |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | — | search_blocks |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | — | search_blocks |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | — | search_blocks |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | — | search_blocks |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | — | search_blocks |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | — | search_blocks |
| 10.1021/je800942u | PROPblock_6 | declared | 18 | binary | — | search_blocks |
| 10.1021/je900064e | PROPblock_6 | declared | 10 | binary | — | search_blocks |
| 10.1021/je900743e | PROPblock_3 | declared | 15 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Find GLOBcomp IDs f… | 195 | KEEP ←in 278 | 195 | 4.1 |
| 2 | 3 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 583 | KEEP ←in 5,356 | 583 | 15.7 |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_1742,… | 2,349 | — | — | 0.1 |
| 4 | 7 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_1483,… | 7,190 | — | — | 0.2 |
| 5 | 1 | `query_thermoml` | instruction=Search for blocks containing …, purpos… | 49,549 | — | — | 153.4 |
| 6 | 3 | `query_thermoml_parallel` | queries=[{'label': 'broad_search', 'p… | 210 | — | — | 0.0 |
| 7 | 4 | `query_thermoml_parallel` | queries=[{'label': 'broad_search', 'p… | 253 | — | — | 0.0 |
| 8 | 1 | `search_blocks` | block_number=GLOBlit_220::PROPblock_1, purpose=Ins… | 853 | KEEP ←in 1,674 | 839 | 9.7 |
| 9 | 1 | `search_blocks` | block_number=GLOBlit_2432::PROPblock_1, purpose=In… | 1,291 | KEEP ←in 2,534 | 1276 | 15.8 |
| 10 | 3 | `inspect_block_table` | block_number=GLOBlit_220::PROPblock_1, purpose=Gro… | 1,078 | — | — | 0.2 |
| 11 | 3 | `inspect_block_table` | block_number=GLOBlit_2432::PROPblock_1, purpose=Gr… | 4,379 | — | — | 0.2 |
| 12 | 2 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 2,046 | KEEP ←in 12,670 | 1923 | 44.3 |
| 13 | 3 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=30, p… | 2,120 | KEEP ←in 9,438 | 2120 | 46.3 |
| 14 | 4 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_220, … | 4,222 | — | — | 0.2 |
| 15 | 5 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_220, … | 1,572 | — | — | 0.1 |
| 16 | 8 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_19, purpose=V… | 1,805 | — | — | 0.2 |
| 17 | 9 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_12, purpose=G… | 1,288 | — | — | 0.1 |
| 18 | 5 | `query_thermoml_parallel` | queries=[{'label': 'broad_search', 'p… | 104,084 | — | — | 297.4 |
| 19 | 9 | `inspect_block` | block_number=PROPblock_2, doi=10.1016/j.fluid.2004… | 1,374 | — | — | 0.9 |
| 20 | 12 | `fit_multi_system` | purpose=Fit Redlich-Kister density co…, systems=[{… | 681 | — | — | 0.5 |
| 21 | 15 | `fit_multi_system` | purpose=Fit RK density correlations f…, systems=[{… | 1,616 | — | — | 3.9 |
| | | **TOTAL (21 tools)** | | **188,738** | | **6,936** | **593.3** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | chars=89078>80000 | skipped_by_agent | 89,078 | 89,078 | 0 | 0.0% |
| 2 | chars=92013>80000 | skipped_by_agent | 92,013 | 92,013 | 0 | 0.0% |
| 3 | chars=93751>80000 | skipped_by_agent | 93,751 | 93,751 | 0 | 0.0% |
| 4 | chars=96268>80000 | skipped_by_agent | 96,268 | 96,268 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 435 | 22,953 | 1,095 | 7.2 |
| 2 | L1-worker | claudeopus46 | 24,095 | 984 | 25,079 | 631 | 5.2 |
| 3 | L1-worker | claudeopus46 | 3,767 | 440 | 4,207 | 336 | 3.7 |
| 4 | L1-worker | claudeopus46 | 24,095 | 1,447 | 25,542 | 789 | 6.1 |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,155 | 26,250 | 700 | 9.0 |
| 6 | L1-worker | claudeopus46 | 3,767 | 5,849 | 9,616 | 1,860 | 15.0 |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,707 | 26,802 | 1,787 | 11.8 |
| 8 | L1-worker | claudeopus46 | 24,095 | 6,507 | 30,602 | 849 | 8.1 |
| 9 | L1-worker | claudeopus46 | 24,095 | 9,187 | 33,282 | 756 | 7.8 |
| 10 | L1-worker | claudeopus46 | 24,095 | 10,145 | 34,240 | 630 | 4.7 |
| 11 | L1-worker | claudeopus46 | 24,095 | 16,870 | 40,965 | 4,249 | 31.6 |
| 12 | L1-worker | claudeopus46 | 24,095 | 25,775 | 49,870 | 3,890 | 27.7 |
| 13 | L1-worker | claudeopus46 | 2,106 | 4,718 | 6,824 | 526 | 4.6 |
| 14 | L1-worker | claudeopus46 | 2,320 | 3,613 | 5,933 | 1,046 | 7.4 |
| 15 | L1-worker | claudeopus46 | 366 | 1,303 | 1,669 | 399 | 3.0 |
| 16 | L1-worker | claudeopus46 | 627 | 3,493 | 4,120 | 1,015 | 8.0 |
| 17 | L1-worker | claudeopus46 | 366 | 1,483 | 1,849 | 1,006 | 4.2 |
| 18 | L1-worker | claudeopus46 | 787 | 15,187 | 15,974 | 680 | 7.6 |
| 19 | L0-main | claudeopus46 | 22,518 | 28,619 | 51,137 | 1,286 | 13.0 |
| 20 | L0-main | claudeopus46 | 22,518 | 29,387 | 51,905 | 3,327 | 20.9 |
| 21 | L0-main | claudeopus46 | 22,518 | 29,656 | 52,174 | 2,090 | 13.6 |
| 22 | L0-main | claudeopus46 | 22,518 | 30,225 | 52,743 | 2,841 | 14.7 |
| 23 | L1-worker | claudeopus46 | 24,095 | 1,038 | 25,133 | 651 | 5.4 |
| 24 | L1-worker | claudeopus46 | 24,095 | 1,041 | 25,136 | 605 | 5.8 |
| 25 | L1-worker | claudeopus46 | 24,095 | 1,742 | 25,837 | 1,037 | 7.1 |
| 26 | L1-worker | claudeopus46 | 24,095 | 2,525 | 26,620 | 684 | 7.1 |
| 27 | L1-worker | claudeopus46 | 3,767 | 2,057 | 5,824 | 1,247 | 9.3 |
| 28 | L1-worker | claudeopus46 | 3,767 | 2,885 | 6,652 | 1,815 | 15.7 |
| 29 | L1-worker | claudeopus46 | 24,095 | 2,142 | 26,237 | 1,313 | 8.1 |
| 30 | L1-worker | claudeopus46 | 24,095 | 5,263 | 29,358 | 543 | 6.0 |
| 31 | L1-worker | claudeopus46 | 24,095 | 2,569 | 26,664 | 1,329 | 8.8 |
| 32 | L1-worker | claudeopus46 | 24,095 | 5,699 | 29,794 | 603 | 5.0 |
| 33 | L1-worker | claudeopus46 | 3,767 | 13,121 | 16,888 | 1,549 | 15.3 |
| 34 | L1-worker | claudeopus46 | 24,095 | 6,611 | 30,706 | 1,677 | 11.9 |
| 35 | L1-worker | claudeopus46 | 2,106 | 2,967 | 5,073 | 475 | 3.6 |
| 36 | L1-worker | claudeopus46 | 2,320 | 1,808 | 4,128 | 540 | 4.1 |
| 37 | L1-worker | claudeopus46 | 627 | 1,688 | 2,315 | 503 | 4.4 |
| 38 | L1-worker | claudeopus46 | 24,095 | 10,334 | 34,429 | 1,273 | 11.4 |
| 39 | L1-worker | claudeopus46 | 366 | 1,252 | 1,618 | 357 | 2.8 |
| 40 | L1-worker | claudeopus46 | 2,106 | 2,566 | 4,672 | 519 | 3.7 |
| 41 | L1-worker | claudeopus46 | 2,320 | 1,404 | 3,724 | 725 | 4.7 |
| 42 | L1-worker | claudeopus46 | 627 | 1,284 | 1,911 | 913 | 5.5 |
| 43 | L1-worker | claudeopus46 | 366 | 1,296 | 1,662 | 408 | 2.9 |
| 44 | L1-worker | claudeopus46 | 787 | 9,104 | 9,891 | 542 | 6.0 |
| 45 | L1-worker | claudeopus46 | 1,228 | 3,370 | 4,598 | 535 | 3.4 |
| 46 | L1-worker | claudeopus46 | 3,767 | 13,423 | 17,190 | 2,348 | 21.7 |
| 47 | L1-worker | claudeopus46 | 787 | 10,563 | 11,350 | 646 | 7.5 |
| 48 | L1-worker | claudeopus46 | 24,095 | 4,559 | 28,654 | 1,206 | 10.0 |
| 49 | L1-worker | claudeopus46 | 3,767 | 9,932 | 13,699 | 1,725 | 16.9 |
| 50 | L1-worker | claudeopus46 | 3,767 | 10,234 | 14,001 | 2,441 | 23.0 |
| 51 | L1-worker | claudeopus46 | 24,095 | 7,155 | 31,250 | 1,071 | 9.2 |
| 52 | L1-worker | claudeopus46 | 24,095 | 11,822 | 35,917 | 1,301 | 14.0 |
| 53 | L1-worker | claudeopus46 | 24,095 | 13,859 | 37,954 | 4,328 | 33.1 |
| 54 | L1-worker | claudeopus46 | 24,095 | 24,476 | 48,571 | 5,549 | 43.1 |
| 55 | L1-worker | claudeopus46 | 24,095 | 35,241 | 59,336 | 1,544 | 11.8 |
| 56 | L1-worker | claudeopus46 | 24,095 | 37,525 | 61,620 | 647 | 7.3 |
| 57 | L1-worker | claudeopus46 | 24,095 | 39,309 | 63,404 | 4,689 | 35.0 |
| 58 | L1-worker | claudeopus46 | 627 | 4,983 | 5,610 | 900 | 9.0 |
| 59 | L1-worker | claudeopus46 | 2,320 | 5,103 | 7,423 | 1,353 | 9.3 |
| 60 | L1-worker | claudeopus46 | 2,106 | 6,966 | 9,072 | 1,638 | 9.4 |
| 61 | L1-worker | claudeopus46 | 366 | 1,790 | 2,156 | 1,308 | 4.6 |
| 62 | L1-worker | claudeopus46 | 366 | 2,415 | 2,781 | 931 | 8.1 |
| 63 | L1-worker | claudeopus46 | 787 | 29,803 | 30,590 | 571 | 6.8 |
| 64 | L0-main | claudeopus46 | 22,485 | 112,543 | 135,028 | 418 | 6.4 |
| 65 | L0-main | claudeopus46 | 22,518 | 111,784 | 134,302 | 1,976 | 18.5 |
| 66 | L0-main | claudeopus46 | 22,518 | 112,671 | 135,189 | 673 | 6.0 |
| 67 | L0-main | claudeopus46 | 22,518 | 113,329 | 135,847 | 658 | 4.2 |
| 68 | L0-main | claudeopus46 | 22,518 | 114,130 | 136,648 | 682 | 5.3 |
| 69 | L0-main | claudeopus46 | 22,485 | 116,292 | 138,777 | 421 | 5.6 |
| 70 | L0-main | claudeopus46 | 22,518 | 115,533 | 138,051 | 2,151 | 15.5 |
| 71 | L0-main | claudeopus46 | 22,518 | 116,237 | 138,755 | 1,938 | 16.0 |
| 72 | L0-main | claudeopus46 | 22,518 | 116,952 | 139,470 | 1,902 | 11.0 |
| 73 | L0-main | claudeopus46 | 22,485 | 118,127 | 140,612 | 592 | 6.6 |
| 74 | L0-main | claudeopus46 | 22,518 | 117,367 | 139,885 | 1,853 | 11.5 |
| 75 | L0-main | claudeopus46 | 22,518 | 118,026 | 140,544 | 1,683 | 21.7 |
| 76 | L0-main | claudeopus46 | 22,518 | 118,672 | 141,190 | 1,796 | 10.5 |
| 77 | L0-main | claudeopus46 | 22,485 | 124,639 | 147,124 | 498 | 8.1 |
| 78 | L0-main | claudeopus46 | 22,518 | 123,879 | 146,397 | 5,721 | 41.6 |
| 79 | L0-main | claudeopus46 | 22,518 | 134,452 | 156,970 | 6,096 | 45.4 |
| 80 | L0-main | claudeopus46 | 22,518 | 145,558 | 168,076 | 5,006 | 38.6 |
| 81 | L0-main | claudeopus46 | 2,106 | 9,523 | 11,629 | 390 | 3.9 |
| 82 | L0-main | claudeopus46 | 366 | 913 | 1,279 | 439 | 3.7 |
| 83 | L0-main | claudeopus46 | 2,320 | 8,973 | 11,293 | 1,341 | 12.3 |
| 84 | L0-main | claudeopus46 | 366 | 1,778 | 2,144 | 1,296 | 7.4 |
| 85 | L0-main | claudeopus46 | 560 | 10,285 | 10,845 | 258 | 2.6 |
| 86 | L0-main | claudeopus46 | 1,156 | 13,190 | 14,346 | 1,782 | 12.3 |
| 87 | L0-main | claudeopus46 | 366 | 2,475 | 2,841 | 1,722 | 5.9 |
| 88 | L0-main | claudeopus46 | 1,918 | 5,282 | 7,200 | 1,102 | 11.8 |

