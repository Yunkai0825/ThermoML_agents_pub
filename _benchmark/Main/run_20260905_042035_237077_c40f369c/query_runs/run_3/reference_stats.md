# Reference Stats — query-agent

**Run started:** 2026-09-05 04:20:47
**Wall time (at last flush):** 137.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 30,036 | 24,577 | 6,123 | 54,613 | 6,826 | 42.2 | claudeopus46 |
| L1-worker | 15 | 182,771 | 48,251 | 12,923 | 231,022 | 15,401 | 94.5 | claudeopus46 |
| verdict | 1 | 972 | 4,073 | 1,112 | 5,045 | 5,045 | 9.9 | claudeopus46 |
| **TOTAL** | **24** | **213,779** | **76,901** | **20,158** | **290,680** | **12,111** | **146.6** | |

**Estimated tokens:** ~72,670 input + ~5,039 output = ~77,709 total
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
| GLOBcomp_2 |  | resolve_compound_ids |

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
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve methanol an… | 330 | KEEP ←in 283 | 330 | 4.8 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_2'], limit=20, p… | 1,290 | KEEP ←in 1,863 | 1274 | 17.1 |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_16, literature=GLOBlit_1133… | 1,353 | — | — | 0.3 |
| 4 | 1 | `L1_query` | context=Binary system: methanol + eth…, id_catalog… | 11,432 | — | — | 91.6 |
| | | **TOTAL (4 tools)** | | **14,405** | | **1,604** | **113.8** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 891 | 12,472 | 1,151 | 7.5 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,162 | 25,257 | 662 | 5.6 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,214 | 26,309 | 588 | 4.1 |
| 4 | L1-worker | claudeopus46 | 3,767 | 476 | 4,243 | 489 | 4.6 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,933 | 26,028 | 783 | 6.3 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,618 | 26,713 | 754 | 5.7 |
| 7 | L1-worker | claudeopus46 | 3,767 | 2,371 | 6,138 | 1,738 | 12.0 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,889 | 27,984 | 720 | 6.2 |
| 9 | L1-worker | claudeopus46 | 24,095 | 5,584 | 29,679 | 1,457 | 9.8 |
| 10 | L1-worker | claudeopus46 | 24,095 | 10,088 | 34,183 | 2,559 | 16.6 |
| 11 | L1-worker | claudeopus46 | 2,106 | 2,822 | 4,928 | 502 | 3.4 |
| 12 | L1-worker | claudeopus46 | 2,320 | 1,539 | 3,859 | 625 | 3.9 |
| 13 | L1-worker | claudeopus46 | 627 | 1,419 | 2,046 | 596 | 4.1 |
| 14 | L1-worker | claudeopus46 | 366 | 1,279 | 1,645 | 375 | 2.7 |
| 15 | L1-worker | claudeopus46 | 366 | 1,062 | 1,428 | 595 | 3.4 |
| 16 | L1-worker | claudeopus46 | 787 | 9,795 | 10,582 | 480 | 6.1 |
| 17 | L0-main | claudeopus46 | 11,581 | 10,810 | 22,391 | 2,110 | 13.9 |
| 18 | L0-main | claudeopus46 | 2,106 | 2,781 | 4,887 | 512 | 4.0 |
| 19 | L0-main | claudeopus46 | 2,320 | 2,058 | 4,378 | 655 | 4.5 |
| 20 | L0-main | claudeopus46 | 366 | 1,130 | 1,496 | 621 | 3.1 |
| 21 | L0-main | claudeopus46 | 366 | 1,061 | 1,427 | 581 | 3.7 |
| 22 | L0-main | claudeopus46 | 560 | 2,524 | 3,084 | 64 | 1.8 |
| 23 | L0-main | claudeopus46 | 1,156 | 3,322 | 4,478 | 429 | 3.7 |
| 24 | verdict | claudeopus46 | 972 | 4,073 | 5,045 | 1,112 | 9.9 |

