# Reference Stats — query-agent

**Run started:** 2026-09-05 02:20:40
**Wall time (at last flush):** 239.9 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 30,036 | 37,321 | 8,879 | 67,357 | 8,419 | 63.5 | claudeopus46 |
| L1-worker | 21 | 303,612 | 117,833 | 25,368 | 421,445 | 20,068 | 192.9 | claudeopus46 |
| verdict | 1 | 972 | 6,761 | 1,057 | 7,733 | 7,733 | 10.9 | claudeopus46 |
| **TOTAL** | **30** | **334,620** | **161,915** | **35,304** | **496,535** | **16,551** | **267.3** | |

**Estimated tokens:** ~124,133 input + ~8,826 output = ~132,959 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **0** | **0** | **0** | **0** | **0** | **0** | **0** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

*(no entity references recorded)*

---

## 3. DOI & Block References

*(no DOI/block references recorded)*

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve global comp… | 264 | KEEP ←in 308 | 264 | 4.8 |
| 2 | 5 | `search_blocks` | compound=['GLOBcomp_15', 'GLOBcomp_18'], limit=50,… | 965 | KEEP ←in 4,801 | 965 | 13.4 |
| 3 | 6 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_7481… | 259 | — | — | 0.0 |
| 4 | 7 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_7481… | 375 | — | — | 0.4 |
| 5 | 8 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_7481… | 1,279 | — | — | 0.1 |
| 6 | 9 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_4124,… | 1,276 | — | — | 0.3 |
| 7 | 1 | `L1_query` | context=User wants specific experimen…, id_catalog… | 19,814 | — | — | 173.6 |
| | | **TOTAL (7 tools)** | | **24,232** | | **1,229** | **192.6** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 970 | 12,551 | 1,485 | 8.4 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,372 | 25,467 | 660 | 5.5 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,461 | 26,556 | 624 | 4.2 |
| 4 | L1-worker | claudeopus46 | 3,767 | 520 | 4,287 | 438 | 4.7 |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,084 | 26,179 | 1,315 | 9.7 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,931 | 27,026 | 924 | 7.0 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,699 | 27,794 | 795 | 5.8 |
| 8 | L1-worker | claudeopus46 | 3,767 | 5,349 | 9,116 | 1,551 | 12.8 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,223 | 28,318 | 1,126 | 11.0 |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,865 | 28,960 | 629 | 6.8 |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,548 | 29,643 | 833 | 7.3 |
| 12 | L1-worker | claudeopus46 | 24,095 | 7,160 | 31,255 | 1,230 | 11.9 |
| 13 | L1-worker | claudeopus46 | 24,095 | 8,797 | 32,892 | 3,001 | 24.0 |
| 14 | L1-worker | claudeopus46 | 24,095 | 14,860 | 38,955 | 2,671 | 20.4 |
| 15 | L1-worker | claudeopus46 | 24,095 | 20,593 | 44,688 | 2,323 | 18.7 |
| 16 | L1-worker | claudeopus46 | 2,320 | 2,454 | 4,774 | 1,022 | 6.8 |
| 17 | L1-worker | claudeopus46 | 627 | 2,334 | 2,961 | 1,056 | 7.4 |
| 18 | L1-worker | claudeopus46 | 2,106 | 3,947 | 6,053 | 1,454 | 7.8 |
| 19 | L1-worker | claudeopus46 | 366 | 1,459 | 1,825 | 982 | 4.8 |
| 20 | L1-worker | claudeopus46 | 366 | 1,467 | 1,833 | 1,043 | 4.7 |
| 21 | L1-worker | claudeopus46 | 366 | 2,231 | 2,597 | 1,095 | 5.0 |
| 22 | L1-worker | claudeopus46 | 787 | 19,479 | 20,266 | 596 | 6.6 |
| 23 | L0-main | claudeopus46 | 11,581 | 16,987 | 28,568 | 3,291 | 24.1 |
| 24 | L0-main | claudeopus46 | 2,320 | 3,232 | 5,552 | 850 | 6.3 |
| 25 | L0-main | claudeopus46 | 2,106 | 4,034 | 6,140 | 705 | 6.7 |
| 26 | L0-main | claudeopus46 | 366 | 1,254 | 1,620 | 669 | 3.6 |
| 27 | L0-main | claudeopus46 | 366 | 1,325 | 1,691 | 811 | 4.1 |
| 28 | L0-main | claudeopus46 | 560 | 3,999 | 4,559 | 185 | 2.7 |
| 29 | L0-main | claudeopus46 | 1,156 | 5,520 | 6,676 | 883 | 7.6 |
| 30 | verdict | claudeopus46 | 972 | 6,761 | 7,733 | 1,057 | 10.9 |

