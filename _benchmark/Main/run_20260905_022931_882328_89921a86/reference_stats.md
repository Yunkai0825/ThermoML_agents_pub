# Reference Stats — main-agent

**Run started:** 2026-09-05 02:29:31
**Wall time (at last flush):** 924.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 28 | 283,892 | 957,771 | 53,448 | 1,241,663 | 44,345 | 376.2 | claudeopus46 |
| L1-worker | 14 | 52,738 | 16,273 | 11,707 | 69,011 | 4,929 | 93.1 | claudeopus46 |
| **TOTAL** | **42** | **336,630** | **974,044** | **65,155** | **1,310,674** | **31,206** | **469.3** | |

**Estimated tokens:** ~327,668 input + ~16,288 output = ~343,956 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

*(no raw counter data recorded)*

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
| 1 | 1 | `run_parallel_subagents` | tasks=[{'agent': 'query', 'label': … | 697 | KEEP ←in 34,690 | 697 | 466.6 |
| 2 | 4 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_2…, purpose=Ins… | 962 | — | — | 10.7 |
| 3 | 5 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_2…, purpose=Ins… | 619 | — | — | 8.3 |
| 4 | 6 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_2…, purpose=Ins… | 1,107 | — | — | 10.3 |
| 5 | 7 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_2…, purpose=Get… | 302 | — | — | 5.3 |
| 6 | 8 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_2…, purpose=Get… | 483 | — | — | 5.4 |
| 7 | 9 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_9…, purpose=Ins… | 797 | — | — | 8.9 |
| 8 | 10 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_9…, purpose=Get… | 392 | — | — | 5.0 |
| 9 | 11 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_9…, purpose=Get… | 451 | — | — | 5.7 |
| 10 | 14 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_5201'…, purpose=Ins… | 1,126 | — | — | 9.4 |
| 11 | 15 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_5201'…, purpose=Get… | 318 | — | — | 4.4 |
| 12 | 16 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_5201'…, purpose=Ins… | 290 | — | — | 5.0 |
| 13 | 17 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2825'…, purpose=Ins… | 759 | — | — | 8.3 |
| 14 | 18 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2825'…, purpose=Ins… | 353 | — | — | 4.6 |
| 15 | 19 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2825'…, purpose=Ins… | 282 | — | — | 4.7 |
| | | **TOTAL (15 tools)** | | **8,938** | | **697** | **562.6** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 401 | 13,999 | 1,766 | 10.2 |
| 2 | L0-main | claudeopus46 | 3,766 | 35,992 | 39,758 | 1,304 | 11.4 |
| 3 | L0-main | claudeopus46 | 13,598 | 15,282 | 28,880 | 14,523 | 88.1 |
| 4 | L0-main | claudeopus46 | 13,598 | 33,768 | 47,366 | 1,121 | 9.9 |
| 5 | L0-main | claudeopus46 | 13,598 | 34,948 | 48,546 | 826 | 6.3 |
| 6 | L1-worker | claudeopus46 | 3,767 | 619 | 4,386 | 1,425 | 10.5 |
| 7 | L0-main | claudeopus46 | 13,598 | 35,366 | 48,964 | 1,215 | 8.9 |
| 8 | L1-worker | claudeopus46 | 3,767 | 554 | 4,321 | 1,072 | 8.0 |
| 9 | L0-main | claudeopus46 | 13,598 | 36,458 | 50,056 | 1,505 | 10.2 |
| 10 | L1-worker | claudeopus46 | 3,767 | 1,613 | 5,380 | 1,432 | 10.1 |
| 11 | L0-main | claudeopus46 | 13,598 | 37,997 | 51,595 | 1,079 | 9.1 |
| 12 | L1-worker | claudeopus46 | 3,767 | 1,203 | 4,970 | 513 | 5.2 |
| 13 | L0-main | claudeopus46 | 13,598 | 38,734 | 52,332 | 645 | 5.0 |
| 14 | L1-worker | claudeopus46 | 3,767 | 1,112 | 4,879 | 712 | 5.3 |
| 15 | L0-main | claudeopus46 | 13,598 | 39,656 | 53,254 | 721 | 6.7 |
| 16 | L1-worker | claudeopus46 | 3,767 | 1,444 | 5,211 | 1,104 | 8.8 |
| 17 | L0-main | claudeopus46 | 13,598 | 40,937 | 54,535 | 594 | 5.5 |
| 18 | L1-worker | claudeopus46 | 3,767 | 1,096 | 4,863 | 596 | 4.8 |
| 19 | L0-main | claudeopus46 | 13,598 | 41,719 | 55,317 | 600 | 5.7 |
| 20 | L1-worker | claudeopus46 | 3,767 | 1,145 | 4,912 | 630 | 5.4 |
| 21 | L0-main | claudeopus46 | 13,598 | 42,516 | 56,114 | 8,757 | 57.6 |
| 22 | L0-main | claudeopus46 | 13,598 | 55,879 | 69,477 | 1,245 | 10.8 |
| 23 | L0-main | claudeopus46 | 13,598 | 56,693 | 70,291 | 732 | 6.3 |
| 24 | L1-worker | claudeopus46 | 3,767 | 1,627 | 5,394 | 1,404 | 9.2 |
| 25 | L0-main | claudeopus46 | 13,598 | 57,689 | 71,287 | 610 | 6.3 |
| 26 | L1-worker | claudeopus46 | 3,767 | 1,123 | 4,890 | 452 | 4.2 |
| 27 | L0-main | claudeopus46 | 13,598 | 58,401 | 71,999 | 549 | 6.0 |
| 28 | L1-worker | claudeopus46 | 3,767 | 1,110 | 4,877 | 406 | 4.4 |
| 29 | L0-main | claudeopus46 | 13,598 | 59,036 | 72,634 | 566 | 5.6 |
| 30 | L1-worker | claudeopus46 | 3,767 | 1,427 | 5,194 | 1,024 | 8.2 |
| 31 | L0-main | claudeopus46 | 13,598 | 60,141 | 73,739 | 550 | 5.2 |
| 32 | L1-worker | claudeopus46 | 3,767 | 1,086 | 4,853 | 481 | 4.5 |
| 33 | L0-main | claudeopus46 | 13,598 | 60,850 | 74,448 | 524 | 5.4 |
| 34 | L1-worker | claudeopus46 | 3,767 | 1,114 | 4,881 | 456 | 4.5 |
| 35 | L0-main | claudeopus46 | 13,598 | 61,433 | 75,031 | 8,841 | 57.2 |
| 36 | L0-main | claudeopus46 | 2,106 | 10,649 | 12,755 | 274 | 3.2 |
| 37 | L0-main | claudeopus46 | 366 | 814 | 1,180 | 260 | 2.7 |
| 38 | L0-main | claudeopus46 | 2,320 | 10,151 | 12,471 | 1,054 | 8.2 |
| 39 | L0-main | claudeopus46 | 366 | 1,529 | 1,895 | 1,010 | 3.6 |
| 40 | L0-main | claudeopus46 | 560 | 10,919 | 11,479 | 186 | 2.3 |
| 41 | L0-main | claudeopus46 | 1,156 | 12,378 | 13,534 | 858 | 5.9 |
| 42 | L0-main | claudeopus46 | 1,292 | 7,435 | 8,727 | 1,533 | 12.9 |

