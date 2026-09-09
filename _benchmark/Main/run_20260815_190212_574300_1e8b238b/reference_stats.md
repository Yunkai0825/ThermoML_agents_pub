# Reference Stats — main-agent

**Run started:** 2026-08-15 19:02:12
**Wall time (at last flush):** 354.5 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 17 | 134,314 | 60,024 | 15,584 | 194,338 | 11,431 | 116.7 | claudeopus46 |
| L0-menu-planner | 1 | 1,013 | 1,330 | 1,834 | 2,343 | 2,343 | 12.4 | claudesonnet46 |
| L1-worker | 2 | 7,534 | 828 | 770 | 8,362 | 4,181 | 9.5 | claudeopus46 |
| **TOTAL** | **20** | **142,861** | **62,182** | **18,188** | **205,043** | **10,252** | **138.6** | |

**Estimated tokens:** ~51,260 input + ~4,547 output = ~55,807 total
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
| 1 | 3 | `browse_subagent_tools` | purpose=Find experimental density of …, tasks=Sear… | 1,834 | — | — | 26.7 |
| 2 | 6 | `run_subagent_tool` | kwargs={'query': 'ethanol', 'entity_…, purpose=Res… | 218 | — | — | 4.9 |
| 3 | 6 | `run_subagent_tool` | kwargs={'query': 'water', 'entity_ty…, purpose=Res… | 210 | — | — | 4.9 |
| 4 | 8 | `run_query_agent` | context=Compound IDs resolved: ethano…, purpose=Re… | 8,345 | — | — | 204.8 |
| | | **TOTAL (4 tools)** | | **10,607** | | **0** | **241.3** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 321 | 13,919 | 1,250 | 11.6 |
| 2 | L0-main | claudeopus46 | 13,598 | 945 | 14,543 | 781 | 6.3 |
| 3 | L0-main | claudeopus46 | 13,598 | 1,716 | 15,314 | 640 | 4.3 |
| 4 | L0-menu-planner | claudesonnet46 | 1,013 | 1,330 | 2,343 | 1,834 | 12.4 |
| 5 | L0-main | claudeopus46 | 13,598 | 3,349 | 16,947 | 859 | 6.8 |
| 6 | L0-main | claudeopus46 | 13,598 | 4,422 | 18,020 | 825 | 5.7 |
| 7 | L0-main | claudeopus46 | 13,598 | 5,699 | 19,297 | 891 | 6.3 |
| 8 | L1-worker | claudeopus46 | 3,767 | 420 | 4,187 | 397 | 4.7 |
| 9 | L1-worker | claudeopus46 | 3,767 | 408 | 4,175 | 373 | 4.8 |
| 10 | L0-main | claudeopus46 | 3,766 | 684 | 4,450 | 403 | 3.4 |
| 11 | L0-main | claudeopus46 | 13,598 | 5,212 | 18,810 | 1,334 | 9.8 |
| 12 | L0-main | claudeopus46 | 13,598 | 5,844 | 19,442 | 1,403 | 9.1 |
| 13 | L0-main | claudeopus46 | 13,598 | 15,110 | 28,708 | 3,327 | 21.4 |
| 14 | L0-main | claudeopus46 | 2,106 | 2,527 | 4,633 | 154 | 2.3 |
| 15 | L0-main | claudeopus46 | 2,320 | 2,109 | 4,429 | 750 | 4.4 |
| 16 | L0-main | claudeopus46 | 366 | 694 | 1,060 | 137 | 2.1 |
| 17 | L0-main | claudeopus46 | 366 | 1,225 | 1,591 | 706 | 2.9 |
| 18 | L0-main | claudeopus46 | 560 | 2,591 | 3,151 | 106 | 4.7 |
| 19 | L0-main | claudeopus46 | 1,156 | 3,389 | 4,545 | 496 | 4.3 |
| 20 | L0-main | claudeopus46 | 1,292 | 4,187 | 5,479 | 1,522 | 11.3 |

