# Reference Stats — query-agent

**Run started:** 2026-09-05 04:20:47
**Wall time (at last flush):** 245.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 30,036 | 41,918 | 10,088 | 71,954 | 8,994 | 61.5 | claudeopus46 |
| L1-worker | 18 | 255,056 | 113,489 | 24,315 | 368,545 | 20,474 | 185.9 | claudeopus46 |
| verdict | 1 | 972 | 7,233 | 1,093 | 8,205 | 8,205 | 11.7 | claudeopus46 |
| **TOTAL** | **27** | **286,064** | **162,640** | **35,496** | **448,704** | **16,618** | **259.1** | |

**Estimated tokens:** ~112,176 input + ~8,874 output = ~121,050 total
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
| GLOBcomp_1 |  | resolve_compound_ids |
| GLOBcomp_24 |  | resolve_compound_ids |

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
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 232 | KEEP ←in 288 | 232 | 4.4 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=20, … | 949 | KEEP ←in 7,245 | 949 | 21.7 |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_24, literature=GLOBlit_5201… | 371 | — | — | 0.3 |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_24, literature=GLOBlit_5201… | 1,750 | — | — | 0.1 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_6951… | 1,369 | — | — | 0.1 |
| 6 | 1 | `L1_query` | context=Binary system: water (H2O) + …, id_catalog… | 23,962 | — | — | 179.9 |
| | | **TOTAL (6 tools)** | | **28,633** | | **1,181** | **206.5** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 920 | 12,501 | 1,415 | 8.0 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,242 | 25,337 | 569 | 4.8 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,275 | 26,370 | 555 | 3.6 |
| 4 | L1-worker | claudeopus46 | 3,767 | 457 | 4,224 | 404 | 4.3 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,909 | 26,004 | 875 | 6.7 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,639 | 26,734 | 741 | 5.1 |
| 7 | L1-worker | claudeopus46 | 3,767 | 7,752 | 11,519 | 1,734 | 14.6 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,587 | 27,682 | 908 | 7.2 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,346 | 28,441 | 625 | 5.4 |
| 10 | L1-worker | claudeopus46 | 24,095 | 6,447 | 30,542 | 821 | 7.3 |
| 11 | L1-worker | claudeopus46 | 24,095 | 8,187 | 32,282 | 3,057 | 22.5 |
| 12 | L1-worker | claudeopus46 | 24,095 | 16,172 | 40,267 | 4,178 | 36.4 |
| 13 | L1-worker | claudeopus46 | 24,095 | 24,478 | 48,573 | 3,889 | 30.2 |
| 14 | L1-worker | claudeopus46 | 2,320 | 3,019 | 5,339 | 991 | 6.1 |
| 15 | L1-worker | claudeopus46 | 627 | 2,899 | 3,526 | 1,043 | 7.1 |
| 16 | L1-worker | claudeopus46 | 2,106 | 4,382 | 6,488 | 1,445 | 7.9 |
| 17 | L1-worker | claudeopus46 | 366 | 1,428 | 1,794 | 946 | 3.8 |
| 18 | L1-worker | claudeopus46 | 366 | 2,222 | 2,588 | 878 | 4.7 |
| 19 | L1-worker | claudeopus46 | 787 | 20,048 | 20,835 | 656 | 8.2 |
| 20 | L0-main | claudeopus46 | 11,581 | 19,957 | 31,538 | 3,672 | 23.5 |
| 21 | L0-main | claudeopus46 | 2,106 | 4,328 | 6,434 | 793 | 6.2 |
| 22 | L0-main | claudeopus46 | 2,320 | 3,576 | 5,896 | 1,158 | 6.6 |
| 23 | L0-main | claudeopus46 | 366 | 1,342 | 1,708 | 943 | 4.0 |
| 24 | L0-main | claudeopus46 | 366 | 1,633 | 1,999 | 1,109 | 4.3 |
| 25 | L0-main | claudeopus46 | 560 | 4,328 | 4,888 | 130 | 2.3 |
| 26 | L0-main | claudeopus46 | 1,156 | 5,834 | 6,990 | 868 | 6.6 |
| 27 | verdict | claudeopus46 | 972 | 7,233 | 8,205 | 1,093 | 11.7 |

