# Reference Stats — query-agent

**Run started:** 2026-09-05 04:55:55
**Wall time (at last flush):** 169.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 30,036 | 28,268 | 7,701 | 58,304 | 7,288 | 51.1 | claudeopus46 |
| L1-worker | 16 | 206,866 | 66,104 | 17,053 | 272,970 | 17,060 | 125.8 | claudeopus46 |
| verdict | 1 | 972 | 5,385 | 1,056 | 6,357 | 6,357 | 8.6 | claudeopus46 |
| **TOTAL** | **25** | **237,874** | **99,757** | **25,810** | **337,631** | **13,505** | **185.5** | |

**Estimated tokens:** ~84,407 input + ~6,452 output = ~90,859 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 12 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **4** | **1** | **2** | **1** | **1** | **1** | **12** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_6 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |

#### References (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_5585 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |

#### Measurements (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |

#### Constraints (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 1 |
| Unique Properties | 1 |
| Unique Measurements | 1 |
| Unique Phases | 1 |
| Unique Variables | 2 |
| Unique Constraints | 1 |
| Total DOIs | 1 |
| Unique parent blocks | 1 |
| Explicit block/subsystem targets | 1 |
| Subsystem targets | 0 |
| Target-matched data points | 12 |

---

## 3. DOI & Block References

**Unique DOIs:** 1  |  **Parent blocks:** 1  |  **Explicit targets:** 1  |  **Subsystems:** 0  |  **Target-matched datapoints:** 12

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2019.105880 | 1 | 12 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2019.105880 | PROPblock_12 | declared | 12 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 200 | KEEP ←in 285 | 200 | 4.6 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_6', 'GLOBcomp_1'], limit=50, p… | 1,163 | KEEP ←in 2,041 | 1145 | 18.5 |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_12, literature=GLOBlit_5585… | 1,127 | — | — | 0.1 |
| 4 | 1 | `L1_query` | context=User is looking for viscosity…, id_catalog… | 11,648 | — | — | 118.4 |
| | | **TOTAL (4 tools)** | | **14,138** | | **1,345** | **141.6** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 937 | 12,518 | 1,439 | 9.0 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,216 | 25,311 | 675 | 5.5 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,264 | 26,359 | 565 | 4.0 |
| 4 | L1-worker | claudeopus46 | 3,767 | 474 | 4,241 | 367 | 4.5 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,846 | 25,941 | 1,057 | 7.1 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,632 | 26,727 | 627 | 4.5 |
| 7 | L1-worker | claudeopus46 | 3,767 | 2,533 | 6,300 | 1,571 | 11.7 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,748 | 27,843 | 868 | 7.0 |
| 9 | L1-worker | claudeopus46 | 24,095 | 5,243 | 29,338 | 1,639 | 13.5 |
| 10 | L1-worker | claudeopus46 | 24,095 | 9,337 | 33,432 | 2,635 | 16.5 |
| 11 | L1-worker | claudeopus46 | 24,095 | 15,391 | 39,486 | 2,313 | 17.7 |
| 12 | L1-worker | claudeopus46 | 2,106 | 3,184 | 5,290 | 848 | 5.6 |
| 13 | L1-worker | claudeopus46 | 2,320 | 1,847 | 4,167 | 988 | 6.4 |
| 14 | L1-worker | claudeopus46 | 627 | 1,727 | 2,354 | 858 | 6.7 |
| 15 | L1-worker | claudeopus46 | 366 | 1,625 | 1,991 | 500 | 3.5 |
| 16 | L1-worker | claudeopus46 | 366 | 1,425 | 1,791 | 948 | 4.2 |
| 17 | L1-worker | claudeopus46 | 787 | 11,612 | 12,399 | 594 | 7.4 |
| 18 | L0-main | claudeopus46 | 11,581 | 12,327 | 23,908 | 2,576 | 16.0 |
| 19 | L0-main | claudeopus46 | 2,320 | 2,478 | 4,798 | 881 | 5.4 |
| 20 | L0-main | claudeopus46 | 2,106 | 3,247 | 5,353 | 660 | 5.6 |
| 21 | L0-main | claudeopus46 | 366 | 1,356 | 1,722 | 837 | 4.3 |
| 22 | L0-main | claudeopus46 | 366 | 1,209 | 1,575 | 729 | 4.7 |
| 23 | L0-main | claudeopus46 | 560 | 2,952 | 3,512 | 72 | 2.2 |
| 24 | L0-main | claudeopus46 | 1,156 | 3,762 | 4,918 | 507 | 3.9 |
| 25 | verdict | claudeopus46 | 972 | 5,385 | 6,357 | 1,056 | 8.6 |

