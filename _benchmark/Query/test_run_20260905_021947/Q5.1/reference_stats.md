# Reference Stats — query-agent

**Run started:** 2026-09-05 05:53:56
**Wall time (at last flush):** 394.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 13 | 54,490 | 54,158 | 14,360 | 108,648 | 8,357 | 100.2 | claudeopus46 |
| L1-worker | 43 | 497,163 | 200,081 | 47,218 | 697,244 | 16,214 | 339.1 | claudeopus46 |
| **TOTAL** | **56** | **551,653** | **254,239** | **61,578** | **805,892** | **14,390** | **439.3** | |

**Estimated tokens:** ~201,473 input + ~15,394 output = ~216,867 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 2 | 2 | 2 | 25 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 2 | 2 | 2 | 25 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **8** | **3** | **6** | **4** | **4** | **4** | **50** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_6 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |

#### References (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_5585 |  | search_blocks |
| GLOBlit_11042 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | resolve_property_ids, search_blocks |

#### Measurements (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 2 |
| Unique Properties | 1 |
| Unique Measurements | 2 |
| Unique Phases | 1 |
| Unique Variables | 3 |
| Unique Constraints | 2 |
| Total DOIs | 2 |
| Unique parent blocks | 2 |
| Explicit block/subsystem targets | 2 |
| Subsystem targets | 0 |
| Target-matched data points | 50 |

---

## 3. DOI & Block References

**Unique DOIs:** 2  |  **Parent blocks:** 2  |  **Explicit targets:** 2  |  **Subsystems:** 0  |  **Target-matched datapoints:** 25

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2019.105880 | 1 | 12 | binary | search_blocks |
| 10.1021/je700700f | 1 | 13 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2019.105880 | PROPblock_12 | declared | 12 | binary | — | search_blocks |
| 10.1021/je700700f | PROPblock_15 | declared | 13 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 200 | KEEP ←in 285 | 200 | 4.7 |
| 2 | 3 | `search_blocks` | compound=['GLOBcomp_6', 'GLOBcomp_1'], limit=50, p… | 1,309 | KEEP ←in 3,909 | 1309 | 14.9 |
| 3 | 4 | `inspect_block_table` | block_number=PROPblock_15, literature=GLOBlit_1104… | 1,331 | — | — | 0.2 |
| 4 | 5 | `inspect_block_table` | block_number=PROPblock_12, literature=GLOBlit_5585… | 1,229 | — | — | 0.1 |
| 5 | 1 | `L1_query` | context=User wants to know if viscosi…, id_catalog… | 319 | — | — | 153.6 |
| 6 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 192 | KEEP ←in 285 | 192 | 4.3 |
| 7 | 2 | `L1_query` | context=User wants viscosity data for…, id_catalog… | 1,368 | — | — | 29.4 |
| 8 | 2 | `resolve_property_ids` | limit=5, min_score=50, purpose=Confirm GLOBprop_4 … | 255 | KEEP ←in 213 | 255 | 4.7 |
| 9 | 3 | `search_blocks` | compound=['GLOBcomp_6', 'GLOBcomp_1'], limit=50, p… | 1,437 | KEEP ←in 3,909 | 1403 | 19.4 |
| 10 | 5 | `inspect_block_table` | block_number=PROPblock_12, literature=GLOBlit_5585… | 1,229 | — | — | 0.5 |
| 11 | 7 | `inspect_block_table` | block_number=PROPblock_15, literature=GLOBlit_1104… | 1,331 | — | — | 0.1 |
| 12 | 3 | `L1_query` | context=User wants to know if viscosi…, id_catalog… | 22,504 | — | — | 118.0 |
| | | **TOTAL (12 tools)** | | **32,704** | | **3,359** | **349.9** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 506 | 12,087 | 1,121 | 7.9 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,108 | 25,203 | 574 | 4.6 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,157 | 26,252 | 566 | 4.5 |
| 4 | L1-worker | claudeopus46 | 3,767 | 475 | 4,242 | 348 | 4.1 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,738 | 25,833 | 821 | 7.0 |
| 6 | L1-worker | claudeopus46 | 3,767 | 4,365 | 8,132 | 1,592 | 14.5 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,370 | 27,465 | 1,173 | 10.0 |
| 8 | L1-worker | claudeopus46 | 24,095 | 5,133 | 29,228 | 708 | 6.2 |
| 9 | L1-worker | claudeopus46 | 24,095 | 6,737 | 30,832 | 3,016 | 20.5 |
| 10 | L1-worker | claudeopus46 | 24,095 | 14,010 | 38,105 | 4,971 | 35.2 |
| 11 | L1-worker | claudeopus46 | 24,095 | 22,664 | 46,759 | 3,774 | 27.2 |
| 12 | L1-worker | claudeopus46 | 2,106 | 4,458 | 6,564 | 1,191 | 6.6 |
| 13 | L1-worker | claudeopus46 | 627 | 3,109 | 3,736 | 967 | 6.9 |
| 14 | L1-worker | claudeopus46 | 2,320 | 3,229 | 5,549 | 1,166 | 7.3 |
| 15 | L1-worker | claudeopus46 | 366 | 1,968 | 2,334 | 711 | 3.9 |
| 16 | L1-worker | claudeopus46 | 366 | 1,378 | 1,744 | 954 | 4.5 |
| 17 | L1-worker | claudeopus46 | 366 | 1,603 | 1,969 | 1,121 | 4.7 |
| 18 | L1-worker | claudeopus46 | 1,228 | 5,751 | 6,979 | 710 | 4.2 |
| 19 | L0-main | claudeopus46 | 11,581 | 1,111 | 12,692 | 1,020 | 7.0 |
| 20 | L1-worker | claudeopus46 | 24,095 | 959 | 25,054 | 538 | 4.3 |
| 21 | L1-worker | claudeopus46 | 24,095 | 1,988 | 26,083 | 540 | 5.1 |
| 22 | L1-worker | claudeopus46 | 3,767 | 455 | 4,222 | 381 | 4.2 |
| 23 | L1-worker | claudeopus46 | 24,095 | 1,575 | 25,670 | 639 | 5.3 |
| 24 | L1-worker | claudeopus46 | 2,106 | 1,619 | 3,725 | 233 | 2.9 |
| 25 | L1-worker | claudeopus46 | 2,320 | 539 | 2,859 | 283 | 3.1 |
| 26 | L1-worker | claudeopus46 | 627 | 419 | 1,046 | 254 | 3.3 |
| 27 | L1-worker | claudeopus46 | 366 | 1,010 | 1,376 | 153 | 2.3 |
| 28 | L1-worker | claudeopus46 | 787 | 1,738 | 2,525 | 435 | 4.0 |
| 29 | L0-main | claudeopus46 | 11,581 | 4,143 | 15,724 | 1,537 | 16.0 |
| 30 | L1-worker | claudeopus46 | 24,095 | 2,992 | 27,087 | 1,026 | 7.5 |
| 31 | L1-worker | claudeopus46 | 24,095 | 4,022 | 28,117 | 594 | 4.1 |
| 32 | L1-worker | claudeopus46 | 3,767 | 388 | 4,155 | 451 | 4.5 |
| 33 | L1-worker | claudeopus46 | 24,095 | 3,723 | 27,818 | 899 | 6.2 |
| 34 | L1-worker | claudeopus46 | 3,767 | 4,362 | 8,129 | 1,617 | 13.9 |
| 35 | L1-worker | claudeopus46 | 24,095 | 5,504 | 29,599 | 2,662 | 15.4 |
| 36 | L1-worker | claudeopus46 | 24,095 | 10,713 | 34,808 | 911 | 6.9 |
| 37 | L1-worker | claudeopus46 | 24,095 | 12,252 | 36,347 | 569 | 6.0 |
| 38 | L1-worker | claudeopus46 | 24,095 | 13,279 | 37,374 | 631 | 4.3 |
| 39 | L1-worker | claudeopus46 | 24,095 | 14,053 | 38,148 | 2,830 | 20.5 |
| 40 | L1-worker | claudeopus46 | 2,106 | 4,544 | 6,650 | 1,219 | 7.3 |
| 41 | L1-worker | claudeopus46 | 2,320 | 2,961 | 5,281 | 1,229 | 8.0 |
| 42 | L1-worker | claudeopus46 | 627 | 2,841 | 3,468 | 1,151 | 8.5 |
| 43 | L1-worker | claudeopus46 | 366 | 1,996 | 2,362 | 739 | 4.1 |
| 44 | L1-worker | claudeopus46 | 366 | 1,666 | 2,032 | 1,184 | 4.5 |
| 45 | L1-worker | claudeopus46 | 366 | 1,562 | 1,928 | 1,138 | 4.6 |
| 46 | L1-worker | claudeopus46 | 787 | 19,668 | 20,455 | 549 | 6.4 |
| 47 | L0-main | claudeopus46 | 11,581 | 22,456 | 34,037 | 2,855 | 19.9 |
| 48 | L0-main | claudeopus46 | 2,106 | 3,113 | 5,219 | 655 | 5.4 |
| 49 | L0-main | claudeopus46 | 2,320 | 2,775 | 5,095 | 1,271 | 7.6 |
| 50 | L0-main | claudeopus46 | 366 | 1,204 | 1,570 | 805 | 3.7 |
| 51 | L0-main | claudeopus46 | 366 | 1,746 | 2,112 | 1,217 | 4.8 |
| 52 | L0-main | claudeopus46 | 560 | 3,518 | 4,078 | 121 | 2.7 |
| 53 | L0-main | claudeopus46 | 1,156 | 5,122 | 6,278 | 1,044 | 6.8 |
| 54 | L0-main | claudeopus46 | 366 | 1,737 | 2,103 | 908 | 4.2 |
| 55 | L0-main | claudeopus46 | 560 | 4,354 | 4,914 | 1,791 | 12.1 |
| 56 | L0-main | claudeopus46 | 366 | 2,373 | 2,739 | 15 | 2.1 |

