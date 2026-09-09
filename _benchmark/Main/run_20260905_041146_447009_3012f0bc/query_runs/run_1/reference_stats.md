# Reference Stats — query-agent

**Run started:** 2026-09-05 04:11:56
**Wall time (at last flush):** 222.6 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 30,036 | 43,692 | 11,029 | 73,728 | 9,216 | 75.7 | claudeopus46 |
| L1-worker | 18 | 255,056 | 105,278 | 21,015 | 360,334 | 20,018 | 158.4 | claudeopus46 |
| verdict | 1 | 972 | 7,868 | 1,081 | 8,840 | 8,840 | 9.7 | claudeopus46 |
| **TOTAL** | **27** | **286,064** | **156,838** | **33,125** | **442,902** | **16,403** | **243.8** | |

**Estimated tokens:** ~110,725 input + ~8,281 output = ~119,006 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **2** | **0** | **0** | **0** | **0** | **0** | **0** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | resolve_compound_ids |
| GLOBcomp_1 |  | resolve_compound_ids |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Total DOIs | 0 |
| Unique parent blocks | 0 |
| Explicit block/subsystem targets | 0 |
| Subsystem targets | 0 |
| Target-matched data points | 0 |

---

## 3. DOI & Block References

*(no DOI/block references recorded)*

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve compound ID… | 176 | KEEP ←in 278 | 176 | 4.2 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=20, p… | 1,301 | KEEP ←in 6,284 | 1301 | 18.3 |
| 3 | 5 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_11, purpose=G… | 348 | — | — | 0.2 |
| 4 | 6 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_11, purpose=G… | 1,414 | — | — | 0.1 |
| 5 | 7 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_21, purpose=G… | 1,628 | — | — | 0.1 |
| 6 | 9 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_21, nearest={… | 780 | — | — | 0.1 |
| 7 | 1 | `L1_query` | context=User needs mixture viscosity …, id_catalog… | 24,000 | — | — | 148.3 |
| | | **TOTAL (7 tools)** | | **29,647** | | **1,477** | **171.3** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 913 | 12,494 | 1,622 | 9.0 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,265 | 25,360 | 617 | 4.4 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,274 | 26,369 | 523 | 4.3 |
| 4 | L1-worker | claudeopus46 | 3,767 | 431 | 4,198 | 351 | 4.1 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,870 | 25,965 | 927 | 7.1 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,612 | 26,707 | 732 | 5.5 |
| 7 | L1-worker | claudeopus46 | 3,767 | 6,797 | 10,564 | 1,625 | 15.0 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,874 | 27,969 | 1,087 | 8.8 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,610 | 28,705 | 631 | 6.2 |
| 10 | L1-worker | claudeopus46 | 24,095 | 6,383 | 30,478 | 1,000 | 8.2 |
| 11 | L1-worker | claudeopus46 | 24,095 | 8,369 | 32,464 | 3,435 | 23.5 |
| 12 | L1-worker | claudeopus46 | 24,095 | 16,201 | 40,296 | 1,867 | 15.6 |
| 13 | L1-worker | claudeopus46 | 24,095 | 17,363 | 41,458 | 2,864 | 20.9 |
| 14 | L1-worker | claudeopus46 | 2,106 | 4,379 | 6,485 | 1,085 | 6.1 |
| 15 | L1-worker | claudeopus46 | 2,320 | 2,993 | 5,313 | 898 | 6.1 |
| 16 | L1-worker | claudeopus46 | 627 | 2,873 | 3,500 | 1,114 | 7.6 |
| 17 | L1-worker | claudeopus46 | 366 | 1,862 | 2,228 | 778 | 3.8 |
| 18 | L1-worker | claudeopus46 | 366 | 1,335 | 1,701 | 863 | 4.2 |
| 19 | L1-worker | claudeopus46 | 787 | 19,787 | 20,574 | 618 | 7.0 |
| 20 | L0-main | claudeopus46 | 11,581 | 19,848 | 31,429 | 4,149 | 30.0 |
| 21 | L0-main | claudeopus46 | 2,320 | 4,039 | 6,359 | 1,251 | 6.8 |
| 22 | L0-main | claudeopus46 | 2,106 | 4,784 | 6,890 | 775 | 12.2 |
| 23 | L0-main | claudeopus46 | 366 | 1,726 | 2,092 | 1,202 | 5.4 |
| 24 | L0-main | claudeopus46 | 366 | 1,324 | 1,690 | 925 | 3.9 |
| 25 | L0-main | claudeopus46 | 560 | 4,792 | 5,352 | 131 | 2.2 |
| 26 | L0-main | claudeopus46 | 1,156 | 6,266 | 7,422 | 974 | 6.2 |
| 27 | verdict | claudeopus46 | 972 | 7,868 | 8,840 | 1,081 | 9.7 |

