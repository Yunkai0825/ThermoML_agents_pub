# Reference Stats — main-agent

**Run started:** 2026-09-05 05:02:49
**Wall time (at last flush):** 368.8 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 34 | 375,312 | 450,212 | 33,749 | 825,524 | 24,280 | 256.4 | claudeopus46 |
| L0-menu-planner | 2 | 2,026 | 2,703 | 2,675 | 4,729 | 2,364 | 18.1 | claudesonnet46 |
| L1-worker | 9 | 33,903 | 16,545 | 10,741 | 50,448 | 5,605 | 93.9 | claudeopus46 |
| **TOTAL** | **45** | **411,241** | **469,460** | **47,165** | **880,701** | **19,571** | **368.4** | |

**Estimated tokens:** ~220,175 input + ~11,791 output = ~231,966 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `run_subagent_tool` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
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
| 1 | 2 | `browse_subagent_tools` | purpose=Inspect block 5 of DOI 10.101…, tasks=1. R… | 1,616 | — | — | 9.7 |
| 2 | 5 | `run_subagent_tool` | kwargs={'entity_type': 'literature',…, purpose=Res… | 245 | — | — | 0.0 |
| 3 | 7 | `run_subagent_tool` | kwargs={'entity_type': 'reference', …, purpose=Res… | 343 | — | — | 4.7 |
| 4 | 9 | `browse_subagent_tools` | purpose=Inspect block 5 of GLOBlit_27…, tasks=Find… | 1,074 | — | — | 8.7 |
| 5 | 11 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2751'…, purpose=Ins… | 517 | — | — | 5.9 |
| 6 | 12 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2751'…, purpose=Ins… | 967 | — | — | 12.9 |
| 7 | 14 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2751'…, purpose=Ret… | 965 | — | — | 10.3 |
| 8 | 17 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2751'…, purpose=Ins… | 1,009 | — | — | 13.6 |
| 9 | 19 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2751'…, purpose=Get… | 1,039 | — | — | 11.4 |
| 10 | 22 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2751'…, purpose=Ins… | 1,115 | — | — | 13.2 |
| 11 | 24 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2751'…, purpose=Gro… | 984 | — | — | 12.9 |
| 12 | 26 | `run_subagent_tool` | kwargs={'literature': 'GLOBlit_2751'…, purpose=Ins… | 929 | — | — | 10.7 |
| | | **TOTAL (12 tools)** | | **10,803** | | **0** | **114.0** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 478 | 14,076 | 1,116 | 6.6 |
| 2 | L0-main | claudeopus46 | 13,598 | 1,332 | 14,930 | 636 | 4.3 |
| 3 | L0-menu-planner | claudesonnet46 | 1,013 | 1,424 | 2,437 | 1,601 | 9.6 |
| 4 | L0-main | claudeopus46 | 13,598 | 2,745 | 16,343 | 529 | 4.7 |
| 5 | L0-main | claudeopus46 | 13,598 | 3,459 | 17,057 | 502 | 4.2 |
| 6 | L0-main | claudeopus46 | 13,598 | 4,162 | 17,760 | 592 | 4.6 |
| 7 | L0-main | claudeopus46 | 13,598 | 3,855 | 17,453 | 519 | 4.6 |
| 8 | L0-main | claudeopus46 | 13,598 | 4,529 | 18,127 | 397 | 3.8 |
| 9 | L1-worker | claudeopus46 | 3,767 | 417 | 4,184 | 502 | 4.4 |
| 10 | L0-main | claudeopus46 | 13,598 | 4,753 | 18,351 | 799 | 5.9 |
| 11 | L0-main | claudeopus46 | 13,598 | 5,574 | 19,172 | 491 | 4.0 |
| 12 | L0-menu-planner | claudesonnet46 | 1,013 | 1,279 | 2,292 | 1,074 | 8.5 |
| 13 | L0-main | claudeopus46 | 13,598 | 6,447 | 20,045 | 965 | 7.6 |
| 14 | L0-main | claudeopus46 | 13,598 | 7,321 | 20,919 | 633 | 4.6 |
| 15 | L1-worker | claudeopus46 | 3,767 | 668 | 4,435 | 656 | 5.7 |
| 16 | L0-main | claudeopus46 | 13,598 | 7,725 | 21,323 | 596 | 5.1 |
| 17 | L1-worker | claudeopus46 | 3,767 | 2,698 | 6,465 | 1,347 | 12.7 |
| 18 | L0-main | claudeopus46 | 13,598 | 8,990 | 22,588 | 1,659 | 11.8 |
| 19 | L0-main | claudeopus46 | 13,598 | 10,135 | 23,733 | 762 | 5.8 |
| 20 | L1-worker | claudeopus46 | 3,767 | 717 | 4,484 | 1,317 | 10.1 |
| 21 | L0-main | claudeopus46 | 13,598 | 10,554 | 24,152 | 3,028 | 19.0 |
| 22 | L0-main | claudeopus46 | 13,598 | 17,318 | 30,916 | 855 | 7.6 |
| 23 | L0-main | claudeopus46 | 13,598 | 18,138 | 31,736 | 444 | 4.6 |
| 24 | L1-worker | claudeopus46 | 3,767 | 2,658 | 6,425 | 1,348 | 13.4 |
| 25 | L0-main | claudeopus46 | 13,598 | 19,011 | 32,609 | 900 | 8.0 |
| 26 | L0-main | claudeopus46 | 13,598 | 20,036 | 33,634 | 729 | 5.0 |
| 27 | L1-worker | claudeopus46 | 3,767 | 2,042 | 5,809 | 1,406 | 11.3 |
| 28 | L0-main | claudeopus46 | 13,598 | 20,558 | 34,156 | 5,507 | 35.6 |
| 29 | L0-main | claudeopus46 | 13,598 | 30,616 | 44,214 | 964 | 7.9 |
| 30 | L0-main | claudeopus46 | 13,598 | 31,422 | 45,020 | 541 | 5.9 |
| 31 | L1-worker | claudeopus46 | 3,767 | 2,683 | 6,450 | 1,498 | 13.1 |
| 32 | L0-main | claudeopus46 | 13,598 | 32,473 | 46,071 | 461 | 5.3 |
| 33 | L0-main | claudeopus46 | 13,598 | 33,521 | 47,119 | 807 | 6.3 |
| 34 | L1-worker | claudeopus46 | 3,767 | 2,632 | 6,399 | 1,368 | 12.7 |
| 35 | L0-main | claudeopus46 | 13,598 | 33,962 | 47,560 | 477 | 5.2 |
| 36 | L0-main | claudeopus46 | 13,598 | 35,007 | 48,605 | 573 | 4.7 |
| 37 | L1-worker | claudeopus46 | 3,767 | 2,030 | 5,797 | 1,299 | 10.5 |
| 38 | L0-main | claudeopus46 | 13,598 | 35,353 | 48,951 | 3,807 | 25.4 |
| 39 | L0-main | claudeopus46 | 2,106 | 7,644 | 9,750 | 153 | 2.5 |
| 40 | L0-main | claudeopus46 | 366 | 693 | 1,059 | 136 | 2.4 |
| 41 | L0-main | claudeopus46 | 2,320 | 7,069 | 9,389 | 1,064 | 9.5 |
| 42 | L0-main | claudeopus46 | 366 | 1,539 | 1,905 | 1,020 | 4.5 |
| 43 | L0-main | claudeopus46 | 560 | 7,550 | 8,110 | 99 | 2.9 |
| 44 | L0-main | claudeopus46 | 1,156 | 8,483 | 9,639 | 486 | 4.6 |
| 45 | L0-main | claudeopus46 | 1,292 | 7,760 | 9,052 | 1,502 | 11.9 |

