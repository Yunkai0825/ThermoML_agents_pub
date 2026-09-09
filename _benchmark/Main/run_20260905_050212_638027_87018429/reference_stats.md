# Reference Stats — main-agent

**Run started:** 2026-09-05 05:02:12
**Wall time (at last flush):** 1,130.9 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 26 | 243,464 | 794,296 | 61,151 | 1,037,760 | 39,913 | 411.3 | claudeopus46 |
| L1-worker | 11 | 41,437 | 11,008 | 8,553 | 52,445 | 4,767 | 73.8 | claudeopus46 |
| **TOTAL** | **37** | **284,901** | **805,304** | **69,704** | **1,090,205** | **29,465** | **485.1** | |

**Estimated tokens:** ~272,551 input + ~17,426 output = ~289,977 total
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
| 1 | 1 | `run_parallel_subagents` | tasks=[{'agent': 'query', 'label': … | 624 | KEEP ←in 36,001 | 624 | 668.4 |
| 2 | 3 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_6…, purpose=Ver… | 327 | — | — | 5.0 |
| 3 | 4 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_2…, purpose=Ver… | 451 | — | — | 6.3 |
| 4 | 5 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_8…, purpose=Ver… | 807 | — | — | 10.4 |
| 5 | 6 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_8…, purpose=Ver… | 567 | — | — | 7.7 |
| 6 | 7 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_5…, purpose=Ver… | 556 | — | — | 7.3 |
| 7 | 8 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_9…, purpose=Ver… | 655 | — | — | 6.9 |
| 8 | 10 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_6…, purpose=Ver… | 320 | — | — | 5.0 |
| 9 | 11 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_2…, purpose=Re-… | 424 | — | — | 5.5 |
| 10 | 13 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_8…, purpose=Re-… | 603 | — | — | 7.6 |
| 11 | 15 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_5…, purpose=Ver… | 630 | — | — | 6.9 |
| 12 | 16 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_9…, purpose=Re-… | 784 | — | — | 7.9 |
| | | **TOTAL (12 tools)** | | **6,748** | | **624** | **744.9** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 420 | 14,018 | 1,677 | 14.5 |
| 2 | L0-main | claudeopus46 | 3,766 | 37,090 | 40,856 | 1,417 | 12.9 |
| 3 | L0-main | claudeopus46 | 13,598 | 17,167 | 30,765 | 7,876 | 51.1 |
| 4 | L0-main | claudeopus46 | 13,598 | 30,299 | 43,897 | 1,717 | 14.3 |
| 5 | L1-worker | claudeopus46 | 3,767 | 719 | 4,486 | 512 | 4.9 |
| 6 | L0-main | claudeopus46 | 13,598 | 31,112 | 44,710 | 1,011 | 7.8 |
| 7 | L1-worker | claudeopus46 | 3,767 | 1,004 | 4,771 | 657 | 6.2 |
| 8 | L0-main | claudeopus46 | 13,598 | 31,981 | 45,579 | 1,180 | 9.7 |
| 9 | L1-worker | claudeopus46 | 3,767 | 647 | 4,414 | 1,475 | 10.2 |
| 10 | L0-main | claudeopus46 | 13,598 | 33,265 | 46,863 | 878 | 7.6 |
| 11 | L1-worker | claudeopus46 | 3,767 | 1,117 | 4,884 | 692 | 7.6 |
| 12 | L0-main | claudeopus46 | 13,598 | 34,208 | 47,806 | 651 | 6.1 |
| 13 | L1-worker | claudeopus46 | 3,767 | 1,122 | 4,889 | 692 | 7.1 |
| 14 | L0-main | claudeopus46 | 13,598 | 35,153 | 48,751 | 602 | 6.3 |
| 15 | L1-worker | claudeopus46 | 3,767 | 1,367 | 5,134 | 861 | 6.7 |
| 16 | L0-main | claudeopus46 | 13,598 | 36,138 | 49,736 | 9,384 | 57.7 |
| 17 | L0-main | claudeopus46 | 13,598 | 51,088 | 64,686 | 2,758 | 20.1 |
| 18 | L1-worker | claudeopus46 | 3,767 | 683 | 4,450 | 562 | 4.9 |
| 19 | L0-main | claudeopus46 | 13,598 | 51,814 | 65,412 | 450 | 5.3 |
| 20 | L1-worker | claudeopus46 | 3,767 | 867 | 4,634 | 566 | 5.3 |
| 21 | L0-main | claudeopus46 | 13,598 | 52,535 | 66,133 | 452 | 5.1 |
| 22 | L0-main | claudeopus46 | 13,598 | 53,600 | 67,198 | 690 | 6.0 |
| 23 | L1-worker | claudeopus46 | 3,767 | 1,056 | 4,823 | 773 | 6.4 |
| 24 | L0-main | claudeopus46 | 13,598 | 53,602 | 67,200 | 531 | 6.1 |
| 25 | L0-main | claudeopus46 | 13,598 | 54,332 | 67,930 | 496 | 4.8 |
| 26 | L1-worker | claudeopus46 | 3,767 | 1,041 | 4,808 | 787 | 6.7 |
| 27 | L0-main | claudeopus46 | 13,598 | 54,899 | 68,497 | 626 | 7.0 |
| 28 | L1-worker | claudeopus46 | 3,767 | 1,385 | 5,152 | 976 | 7.8 |
| 29 | L0-main | claudeopus46 | 13,598 | 56,019 | 69,617 | 8,840 | 56.4 |
| 30 | L0-main | claudeopus46 | 2,320 | 10,480 | 12,800 | 1,255 | 11.0 |
| 31 | L0-main | claudeopus46 | 2,106 | 10,997 | 13,103 | 1,815 | 12.2 |
| 32 | L0-main | claudeopus46 | 366 | 1,730 | 2,096 | 1,201 | 4.1 |
| 33 | L0-main | claudeopus46 | 366 | 2,355 | 2,721 | 2,230 | 8.8 |
| 34 | L0-main | claudeopus46 | 560 | 15,342 | 15,902 | 1,285 | 8.5 |
| 35 | L0-main | claudeopus46 | 1,156 | 25,009 | 26,165 | 5,729 | 32.5 |
| 36 | L0-main | claudeopus46 | 366 | 6,422 | 6,788 | 4,839 | 23.1 |
| 37 | L0-main | claudeopus46 | 1,292 | 7,239 | 8,531 | 1,561 | 12.3 |

