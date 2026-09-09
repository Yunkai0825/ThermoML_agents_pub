# Reference Stats — main-agent

**Run started:** 2026-09-05 04:53:51
**Wall time (at last flush):** 352.2 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 12 | 76,156 | 104,019 | 20,176 | 180,175 | 15,014 | 142.6 | claudeopus46 |
| **TOTAL** | **12** | **76,156** | **104,019** | **20,176** | **180,175** | **15,014** | **142.6** | |

**Estimated tokens:** ~45,043 input + ~5,044 output = ~50,087 total
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
| 1 | 2 | `run_query_agent` | context=Ethanol is C2H5OH (CAS 64-17-…, purpose=Se… | 27,932 | — | — | 212.7 |
| | | **TOTAL (1 tools)** | | **27,932** | | **0** | **212.7** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 318 | 13,916 | 1,432 | 7.9 |
| 2 | L0-main | claudeopus46 | 13,598 | 1,047 | 14,645 | 1,396 | 8.3 |
| 3 | L0-main | claudeopus46 | 13,598 | 18,603 | 32,201 | 4,198 | 30.7 |
| 4 | L0-main | claudeopus46 | 13,598 | 26,971 | 40,569 | 4,549 | 33.2 |
| 5 | L0-main | claudeopus46 | 13,598 | 35,692 | 49,290 | 4,017 | 28.8 |
| 6 | L0-main | claudeopus46 | 2,106 | 3,432 | 5,538 | 155 | 2.3 |
| 7 | L0-main | claudeopus46 | 366 | 695 | 1,061 | 138 | 2.2 |
| 8 | L0-main | claudeopus46 | 2,320 | 3,017 | 5,337 | 1,118 | 7.2 |
| 9 | L0-main | claudeopus46 | 366 | 1,593 | 1,959 | 1,069 | 4.5 |
| 10 | L0-main | claudeopus46 | 560 | 3,500 | 4,060 | 107 | 1.9 |
| 11 | L0-main | claudeopus46 | 1,156 | 4,299 | 5,455 | 431 | 3.9 |
| 12 | L0-main | claudeopus46 | 1,292 | 4,852 | 6,144 | 1,566 | 11.7 |

