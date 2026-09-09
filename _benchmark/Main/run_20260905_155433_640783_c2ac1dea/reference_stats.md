# Reference Stats — main-agent

**Run started:** 2026-09-05 15:54:33
**Wall time (at last flush):** 1,023.9 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 17 | 97,813 | 127,268 | 27,906 | 225,081 | 13,240 | 177.0 | claudeopus46 |
| L0-menu-planner | 1 | 1,013 | 1,306 | 1,664 | 2,319 | 2,319 | 9.9 | claudesonnet46 |
| **TOTAL** | **18** | **98,826** | **128,574** | **29,570** | **227,400** | **12,633** | **186.9** | |

**Estimated tokens:** ~56,850 input + ~7,392 output = ~64,242 total
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
| 1 | 2 | `browse_subagent_tools` | purpose=Find viscosity data for ethyl…, tasks=Sear… | 1,664 | — | — | 21.6 |
| 2 | 4 | `run_query_agent` | context=The user wants to estimate vi…, purpose=Lo… | 5,611 | — | — | 250.2 |
| 3 | 5 | `run_parallel_subagents` | tasks=[{'agent': 'query', 'label': … | 1,493 | — | — | 609.1 |
| | | **TOTAL (3 tools)** | | **8,768** | | **0** | **880.9** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 262 | 13,860 | 1,794 | 12.4 |
| 2 | L0-main | claudeopus46 | 13,598 | 1,141 | 14,739 | 545 | 3.7 |
| 3 | L0-menu-planner | claudesonnet46 | 1,013 | 1,306 | 2,319 | 1,664 | 9.9 |
| 4 | L0-main | claudeopus46 | 13,598 | 2,601 | 16,199 | 2,136 | 13.7 |
| 5 | L0-main | claudeopus46 | 13,598 | 3,339 | 16,937 | 1,732 | 10.8 |
| 6 | L0-main | claudeopus46 | 13,598 | 11,729 | 25,327 | 2,372 | 15.8 |
| 7 | L0-main | claudeopus46 | 161 | 2,103 | 2,264 | 447 | 5.2 |
| 8 | L0-main | claudeopus46 | 3,766 | 32,301 | 36,067 | 1,210 | 11.5 |
| 9 | L0-main | claudeopus46 | 3,766 | 4,493 | 8,259 | 1,338 | 8.8 |
| 10 | L0-main | claudeopus46 | 13,598 | 30,981 | 44,579 | 6,051 | 38.2 |
| 11 | L0-main | claudeopus46 | 2,106 | 4,864 | 6,970 | 722 | 4.4 |
| 12 | L0-main | claudeopus46 | 2,320 | 4,505 | 6,825 | 1,133 | 8.9 |
| 13 | L0-main | claudeopus46 | 366 | 1,262 | 1,628 | 1,028 | 5.1 |
| 14 | L0-main | claudeopus46 | 366 | 1,608 | 1,974 | 1,089 | 3.9 |
| 15 | L0-main | claudeopus46 | 560 | 6,385 | 6,945 | 498 | 4.2 |
| 16 | L0-main | claudeopus46 | 1,156 | 10,345 | 11,501 | 2,179 | 12.8 |
| 17 | L0-main | claudeopus46 | 366 | 2,872 | 3,238 | 2,095 | 6.9 |
| 18 | L0-main | claudeopus46 | 1,292 | 6,477 | 7,769 | 1,537 | 10.7 |

