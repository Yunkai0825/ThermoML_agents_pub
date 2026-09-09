# Reference Stats — query-agent

**Run started:** 2026-09-05 04:11:56
**Wall time (at last flush):** 254.9 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 30,402 | 44,355 | 13,646 | 74,757 | 8,306 | 83.1 | claudeopus46 |
| L1-worker | 19 | 279,151 | 131,011 | 23,002 | 410,162 | 21,587 | 176.0 | claudeopus46 |
| verdict | 1 | 972 | 7,726 | 1,127 | 8,698 | 8,698 | 9.3 | claudeopus46 |
| **TOTAL** | **29** | **310,525** | **183,092** | **37,775** | **493,617** | **17,021** | **268.4** | |

**Estimated tokens:** ~123,404 input + ~9,443 output = ~132,847 total
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
| GLOBcomp_4 |  | resolve_compound_ids |
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
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve methanol an… | 180 | KEEP ←in 277 | 180 | 3.4 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=20, p… | 1,129 | KEEP ←in 6,223 | 1129 | 19.0 |
| 3 | 5 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_9, purpose=Ge… | 348 | — | — | 0.6 |
| 4 | 6 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_9, purpose=Ge… | 1,507 | — | — | 0.1 |
| 5 | 8 | `inspect_block_table` | block_number=GLOBlit_8869::PROPblock_3, purpose=Gr… | 955 | — | — | 0.1 |
| 6 | 9 | `inspect_block_table` | block_number=GLOBlit_9571::PROPblock_1, purpose=In… | 1,028 | — | — | 0.1 |
| 7 | 1 | `L1_query` | context=User needs mixture viscosity …, id_catalog… | 27,486 | — | — | 171.2 |
| | | **TOTAL (7 tools)** | | **32,633** | | **1,309** | **194.5** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 915 | 12,496 | 1,611 | 8.9 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,272 | 25,367 | 548 | 5.4 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,290 | 26,385 | 535 | 3.9 |
| 4 | L1-worker | claudeopus46 | 3,767 | 438 | 4,205 | 317 | 3.3 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,876 | 25,971 | 915 | 6.8 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,592 | 26,687 | 740 | 4.9 |
| 7 | L1-worker | claudeopus46 | 3,767 | 6,725 | 10,492 | 1,666 | 15.3 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,684 | 27,779 | 968 | 7.8 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,379 | 28,474 | 593 | 6.1 |
| 10 | L1-worker | claudeopus46 | 24,095 | 6,180 | 30,275 | 2,306 | 18.0 |
| 11 | L1-worker | claudeopus46 | 24,095 | 11,960 | 36,055 | 3,222 | 21.0 |
| 12 | L1-worker | claudeopus46 | 24,095 | 13,278 | 37,373 | 517 | 5.3 |
| 13 | L1-worker | claudeopus46 | 24,095 | 14,631 | 38,726 | 2,650 | 21.7 |
| 14 | L1-worker | claudeopus46 | 24,095 | 21,579 | 45,674 | 2,669 | 21.2 |
| 15 | L1-worker | claudeopus46 | 2,320 | 3,333 | 5,653 | 772 | 5.0 |
| 16 | L1-worker | claudeopus46 | 627 | 3,213 | 3,840 | 775 | 6.4 |
| 17 | L1-worker | claudeopus46 | 366 | 1,209 | 1,575 | 311 | 2.4 |
| 18 | L1-worker | claudeopus46 | 2,106 | 4,726 | 6,832 | 1,751 | 8.5 |
| 19 | L1-worker | claudeopus46 | 366 | 2,528 | 2,894 | 1,008 | 4.6 |
| 20 | L1-worker | claudeopus46 | 787 | 25,118 | 25,905 | 739 | 8.4 |
| 21 | L0-main | claudeopus46 | 11,581 | 18,819 | 30,400 | 4,706 | 34.1 |
| 22 | L0-main | claudeopus46 | 2,106 | 4,367 | 6,473 | 689 | 5.7 |
| 23 | L0-main | claudeopus46 | 2,320 | 3,620 | 5,940 | 1,223 | 7.3 |
| 24 | L0-main | claudeopus46 | 366 | 1,238 | 1,604 | 914 | 4.3 |
| 25 | L0-main | claudeopus46 | 366 | 1,698 | 2,064 | 1,174 | 4.5 |
| 26 | L0-main | claudeopus46 | 560 | 4,627 | 5,187 | 171 | 2.4 |
| 27 | L0-main | claudeopus46 | 1,156 | 6,776 | 7,932 | 1,602 | 10.4 |
| 28 | L0-main | claudeopus46 | 366 | 2,295 | 2,661 | 1,556 | 5.5 |
| 29 | verdict | claudeopus46 | 972 | 7,726 | 8,698 | 1,127 | 9.3 |

