# Reference Stats — main-agent

**Run started:** 2026-08-15 19:47:22
**Wall time (at last flush):** 663.8 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 35,362 | 55,742 | 29,170 | 91,104 | 10,122 | 162.2 | claudeopus46 |
| **TOTAL** | **9** | **35,362** | **55,742** | **29,170** | **91,104** | **10,122** | **162.2** | |

**Estimated tokens:** ~22,776 input + ~7,292 output = ~30,068 total
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
| 1 | 1 | `run_analysis_agent` | context=The user wants a complete RK …, purpose=Ob… | 63,604 | — | — | 505.3 |
| | | **TOTAL (1 tools)** | | **63,604** | | **0** | **505.3** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 518 | 14,116 | 20,777 | 101.7 |
| 2 | L0-main | claudeopus46 | 13,598 | 29,170 | 42,768 | 3,688 | 27.2 |
| 3 | L0-main | claudeopus46 | 2,106 | 4,471 | 6,577 | 154 | 2.2 |
| 4 | L0-main | claudeopus46 | 366 | 694 | 1,060 | 137 | 2.2 |
| 5 | L0-main | claudeopus46 | 2,320 | 3,856 | 6,176 | 1,116 | 6.7 |
| 6 | L0-main | claudeopus46 | 366 | 1,591 | 1,957 | 1,072 | 4.1 |
| 7 | L0-main | claudeopus46 | 560 | 4,338 | 4,898 | 106 | 2.1 |
| 8 | L0-main | claudeopus46 | 1,156 | 5,137 | 6,293 | 540 | 4.2 |
| 9 | L0-main | claudeopus46 | 1,292 | 5,967 | 7,259 | 1,580 | 11.8 |

