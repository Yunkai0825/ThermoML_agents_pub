# Reference Stats — main-agent

**Run started:** 2026-09-05 05:00:55
**Wall time (at last flush):** 113.2 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 16 | 156,028 | 54,783 | 10,377 | 210,811 | 13,175 | 80.3 | claudeopus46 |
| L0-menu-planner | 1 | 1,013 | 1,353 | 1,695 | 2,366 | 2,366 | 13.5 | claudesonnet46 |
| L1-worker | 4 | 15,068 | 3,545 | 2,319 | 18,613 | 4,653 | 22.4 | claudeopus46 |
| **TOTAL** | **21** | **172,109** | **59,681** | **14,391** | **231,790** | **11,037** | **116.2** | |

**Estimated tokens:** ~57,947 input + ~3,597 output = ~61,544 total
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
| 1 | 2 | `browse_subagent_tools` | purpose=Resolve common compound names…, tasks=Reso… | 1,695 | — | — | 13.6 |
| 2 | 4 | `run_subagent_tool` | kwargs={'query': 'ethanol', 'entity_…, purpose=Res… | 229 | — | — | 3.9 |
| 3 | 6 | `run_subagent_tool` | kwargs={'entity_type': 'compound', '…, purpose=Res… | 349 | — | — | 5.2 |
| 4 | 9 | `run_subagent_tool` | kwargs={'entity_type': 'compound', '…, purpose=Res… | 214 | — | — | 4.5 |
| 5 | 10 | `run_subagent_tool` | kwargs={'entity_type': 'compound', '…, purpose=Res… | 665 | — | — | 9.4 |
| | | **TOTAL (5 tools)** | | **3,152** | | **0** | **36.6** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 397 | 13,995 | 916 | 5.6 |
| 2 | L0-main | claudeopus46 | 13,598 | 1,294 | 14,892 | 632 | 5.3 |
| 3 | L0-menu-planner | claudesonnet46 | 1,013 | 1,353 | 2,366 | 1,695 | 13.5 |
| 4 | L0-main | claudeopus46 | 13,598 | 2,805 | 16,403 | 599 | 5.1 |
| 5 | L0-main | claudeopus46 | 13,598 | 3,665 | 17,263 | 641 | 4.5 |
| 6 | L1-worker | claudeopus46 | 3,767 | 445 | 4,212 | 368 | 3.9 |
| 7 | L0-main | claudeopus46 | 13,598 | 3,765 | 17,363 | 615 | 4.7 |
| 8 | L0-main | claudeopus46 | 13,598 | 4,422 | 18,020 | 681 | 4.8 |
| 9 | L1-worker | claudeopus46 | 3,767 | 488 | 4,255 | 504 | 5.1 |
| 10 | L0-main | claudeopus46 | 13,598 | 4,798 | 18,396 | 362 | 4.0 |
| 11 | L0-main | claudeopus46 | 13,598 | 5,749 | 19,347 | 565 | 4.5 |
| 12 | L0-main | claudeopus46 | 13,598 | 6,462 | 20,060 | 527 | 4.1 |
| 13 | L1-worker | claudeopus46 | 3,767 | 417 | 4,184 | 391 | 4.3 |
| 14 | L0-main | claudeopus46 | 13,598 | 5,855 | 19,453 | 423 | 4.2 |
| 15 | L1-worker | claudeopus46 | 3,767 | 2,195 | 5,962 | 1,056 | 9.1 |
| 16 | L0-main | claudeopus46 | 13,598 | 6,805 | 20,403 | 1,470 | 10.2 |
| 17 | L0-main | claudeopus46 | 2,106 | 2,134 | 4,240 | 31 | 3.5 |
| 18 | L0-main | claudeopus46 | 2,320 | 1,640 | 3,960 | 754 | 4.2 |
| 19 | L0-main | claudeopus46 | 366 | 571 | 937 | 14 | 1.8 |
| 20 | L0-main | claudeopus46 | 366 | 1,229 | 1,595 | 710 | 3.3 |
| 21 | L0-main | claudeopus46 | 1,292 | 3,192 | 4,484 | 1,437 | 10.5 |

