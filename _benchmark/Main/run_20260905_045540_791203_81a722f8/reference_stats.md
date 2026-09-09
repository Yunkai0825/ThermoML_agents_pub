# Reference Stats — main-agent

**Run started:** 2026-09-05 04:55:40
**Wall time (at last flush):** 383.6 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 20 | 184,940 | 310,749 | 23,273 | 495,689 | 24,784 | 177.3 | claudeopus46 |
| L1-worker | 6 | 22,602 | 5,533 | 4,548 | 28,135 | 4,689 | 39.0 | claudeopus46 |
| **TOTAL** | **26** | **207,542** | **316,282** | **27,821** | **523,824** | **20,147** | **216.3** | |

**Estimated tokens:** ~130,956 input + ~6,955 output = ~137,911 total
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
| 1 | 2 | `run_query_agent` | context=Rubbing alcohol is commonly i…, purpose=Id… | 10,183 | — | — | 169.5 |
| 2 | 6 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_5585'…, purpose=Ver… | 465 | — | — | 5.9 |
| 3 | 7 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_5585'…, purpose=Ver… | 490 | — | — | 7.0 |
| 4 | 8 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_5585'…, purpose=Ver… | 423 | — | — | 7.1 |
| 5 | 10 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_5585'…, purpose=Ver… | 536 | — | — | 6.5 |
| 6 | 11 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_5585'…, purpose=Ver… | 494 | — | — | 6.4 |
| 7 | 12 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_5585'…, purpose=Ver… | 538 | — | — | 7.5 |
| | | **TOTAL (7 tools)** | | **13,129** | | **0** | **209.9** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 276 | 13,874 | 1,216 | 7.5 |
| 2 | L0-main | claudeopus46 | 13,598 | 966 | 14,564 | 1,137 | 7.2 |
| 3 | L0-main | claudeopus46 | 13,598 | 12,221 | 25,819 | 3,464 | 23.5 |
| 4 | L0-main | claudeopus46 | 13,598 | 20,302 | 33,900 | 1,037 | 7.5 |
| 5 | L0-main | claudeopus46 | 13,598 | 21,416 | 35,014 | 746 | 5.4 |
| 6 | L0-main | claudeopus46 | 13,598 | 22,254 | 35,852 | 586 | 4.5 |
| 7 | L1-worker | claudeopus46 | 3,767 | 885 | 4,652 | 666 | 5.7 |
| 8 | L0-main | claudeopus46 | 13,598 | 21,661 | 35,259 | 748 | 6.0 |
| 9 | L1-worker | claudeopus46 | 3,767 | 911 | 4,678 | 745 | 6.7 |
| 10 | L0-main | claudeopus46 | 13,598 | 22,525 | 36,123 | 575 | 5.2 |
| 11 | L1-worker | claudeopus46 | 3,767 | 959 | 4,726 | 795 | 6.9 |
| 12 | L0-main | claudeopus46 | 13,598 | 23,326 | 36,924 | 3,602 | 25.8 |
| 13 | L0-main | claudeopus46 | 13,598 | 31,565 | 45,163 | 984 | 8.0 |
| 14 | L1-worker | claudeopus46 | 3,767 | 920 | 4,687 | 751 | 6.1 |
| 15 | L0-main | claudeopus46 | 13,598 | 32,482 | 46,080 | 468 | 4.8 |
| 16 | L1-worker | claudeopus46 | 3,767 | 907 | 4,674 | 714 | 6.3 |
| 17 | L0-main | claudeopus46 | 13,598 | 33,297 | 46,895 | 479 | 5.4 |
| 18 | L1-worker | claudeopus46 | 3,767 | 951 | 4,718 | 877 | 7.3 |
| 19 | L0-main | claudeopus46 | 13,598 | 34,125 | 47,723 | 3,637 | 26.4 |
| 20 | L0-main | claudeopus46 | 2,106 | 6,143 | 8,249 | 154 | 2.7 |
| 21 | L0-main | claudeopus46 | 366 | 694 | 1,060 | 137 | 2.6 |
| 22 | L0-main | claudeopus46 | 2,320 | 5,770 | 8,090 | 1,119 | 9.2 |
| 23 | L0-main | claudeopus46 | 366 | 1,594 | 1,960 | 1,065 | 4.5 |
| 24 | L0-main | claudeopus46 | 560 | 6,252 | 6,812 | 106 | 2.1 |
| 25 | L0-main | claudeopus46 | 1,156 | 7,054 | 8,210 | 524 | 4.8 |
| 26 | L0-main | claudeopus46 | 1,292 | 6,826 | 8,118 | 1,489 | 14.2 |

