# Reference Stats — query-agent

**Run started:** 2026-09-05 04:43:18
**Wall time (at last flush):** 241.1 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 30,036 | 42,479 | 9,616 | 72,515 | 9,064 | 65.0 | claudeopus46 |
| L1-worker | 17 | 227,560 | 113,134 | 25,300 | 340,694 | 20,040 | 188.2 | claudeopus46 |
| verdict | 1 | 972 | 6,494 | 1,163 | 7,466 | 7,466 | 10.1 | claudeopus46 |
| **TOTAL** | **26** | **258,568** | **162,107** | **36,079** | **420,675** | **16,179** | **263.3** | |

**Estimated tokens:** ~105,168 input + ~9,019 output = ~114,187 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `search_blocks` | 2 | 1 | 3 | 1 | 2 | 2 | 155 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **2** | **1** | **3** | **1** | **2** | **2** | **155** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### References (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2781 |  | search_blocks |
| GLOBlit_11517 |  | search_blocks |

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_31 | dimethyl sulfoxide | search_blocks |
| GLOBcomp_1 | water | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |

#### Measurements (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |

#### Constraints (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique References | 2 |
| Unique Compounds | 2 |
| Unique Properties | 1 |
| Unique Measurements | 2 |
| Unique Phases | 1 |
| Unique Variables | 3 |
| Unique Constraints | 1 |
| Total DOIs | 2 |
| Unique parent blocks | 2 |
| Explicit block/subsystem targets | 2 |
| Subsystem targets | 0 |
| Target-matched data points | 155 |

---

## 3. DOI & Block References

**Unique DOIs:** 2  |  **Parent blocks:** 2  |  **Explicit targets:** 2  |  **Subsystems:** 0  |  **Target-matched datapoints:** 155

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2006.12.012 | 1 | 120 | binary | search_blocks |
| 10.1021/je9001027 | 1 | 35 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2006.12.012 | PROPblock_3 | declared | 120 | binary | — | search_blocks |
| 10.1021/je9001027 | PROPblock_3 | declared | 35 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,252 | KEEP ←in 5,142 | 1252 | 20.7 |
| 2 | 3 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2781,… | 377 | — | — | 0.1 |
| 3 | 4 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2781,… | 1,897 | — | — | 0.3 |
| 4 | 5 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11517… | 261 | — | — | 0.0 |
| 5 | 6 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11517… | 1,171 | — | — | 0.2 |
| 6 | 1 | `L1_query` | context=User wants composition depend…, id_catalog… | 23,878 | — | — | 173.4 |
| | | **TOTAL (6 tools)** | | **28,836** | | **1,252** | **194.7** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 869 | 12,450 | 1,240 | 8.3 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,244 | 25,339 | 803 | 8.3 |
| 3 | L1-worker | claudeopus46 | 24,095 | 1,974 | 26,069 | 644 | 4.4 |
| 4 | L1-worker | claudeopus46 | 3,767 | 5,623 | 9,390 | 1,552 | 15.8 |
| 5 | L1-worker | claudeopus46 | 24,095 | 3,185 | 27,280 | 786 | 7.1 |
| 6 | L1-worker | claudeopus46 | 24,095 | 4,006 | 28,101 | 671 | 5.2 |
| 7 | L1-worker | claudeopus46 | 24,095 | 6,225 | 30,320 | 1,094 | 9.3 |
| 8 | L1-worker | claudeopus46 | 24,095 | 6,926 | 31,021 | 635 | 6.0 |
| 9 | L1-worker | claudeopus46 | 24,095 | 8,414 | 32,509 | 3,294 | 24.8 |
| 10 | L1-worker | claudeopus46 | 24,095 | 15,218 | 39,313 | 4,494 | 31.9 |
| 11 | L1-worker | claudeopus46 | 24,095 | 22,734 | 46,829 | 4,606 | 33.8 |
| 12 | L1-worker | claudeopus46 | 627 | 3,422 | 4,049 | 949 | 6.7 |
| 13 | L1-worker | claudeopus46 | 2,106 | 4,907 | 7,013 | 1,235 | 7.0 |
| 14 | L1-worker | claudeopus46 | 2,320 | 3,542 | 5,862 | 1,170 | 7.5 |
| 15 | L1-worker | claudeopus46 | 366 | 2,012 | 2,378 | 757 | 4.1 |
| 16 | L1-worker | claudeopus46 | 366 | 1,360 | 1,726 | 936 | 4.5 |
| 17 | L1-worker | claudeopus46 | 366 | 1,607 | 1,973 | 1,125 | 5.2 |
| 18 | L1-worker | claudeopus46 | 787 | 20,735 | 21,522 | 549 | 6.6 |
| 19 | L0-main | claudeopus46 | 11,581 | 20,990 | 32,571 | 3,626 | 27.4 |
| 20 | L0-main | claudeopus46 | 2,106 | 4,214 | 6,320 | 721 | 5.1 |
| 21 | L0-main | claudeopus46 | 2,320 | 3,513 | 5,833 | 1,135 | 7.1 |
| 22 | L0-main | claudeopus46 | 366 | 1,270 | 1,636 | 815 | 3.8 |
| 23 | L0-main | claudeopus46 | 366 | 1,610 | 1,976 | 1,086 | 4.9 |
| 24 | L0-main | claudeopus46 | 560 | 4,273 | 4,833 | 178 | 2.9 |
| 25 | L0-main | claudeopus46 | 1,156 | 5,740 | 6,896 | 815 | 5.5 |
| 26 | verdict | claudeopus46 | 972 | 6,494 | 7,466 | 1,163 | 10.1 |

