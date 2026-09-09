# Reference Stats — main-agent

**Run started:** 2026-09-05 04:11:34
**Wall time (at last flush):** 468.1 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 11 | 62,558 | 116,564 | 21,787 | 179,122 | 16,283 | 160.7 | claudeopus46 |
| **TOTAL** | **11** | **62,558** | **116,564** | **21,787** | **179,122** | **16,283** | **160.7** | |

**Estimated tokens:** ~44,780 input + ~5,446 output = ~50,226 total
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
| 1 | 1 | `run_analysis_agent` | context=The user wants a complete RK …, purpose=Fi… | 15,326 | — | — | 310.8 |
| | | **TOTAL (1 tools)** | | **15,326** | | **0** | **310.8** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 412 | 14,010 | 1,555 | 9.6 |
| 2 | L0-main | claudeopus46 | 13,598 | 18,905 | 32,503 | 3,636 | 28.5 |
| 3 | L0-main | claudeopus46 | 13,598 | 28,310 | 41,908 | 5,346 | 39.6 |
| 4 | L0-main | claudeopus46 | 13,598 | 39,489 | 53,087 | 6,476 | 46.5 |
| 5 | L0-main | claudeopus46 | 2,106 | 5,121 | 7,227 | 154 | 2.1 |
| 6 | L0-main | claudeopus46 | 366 | 694 | 1,060 | 137 | 2.1 |
| 7 | L0-main | claudeopus46 | 2,320 | 4,612 | 6,932 | 1,169 | 9.0 |
| 8 | L0-main | claudeopus46 | 366 | 1,644 | 2,010 | 1,125 | 4.5 |
| 9 | L0-main | claudeopus46 | 560 | 5,094 | 5,654 | 100 | 2.1 |
| 10 | L0-main | claudeopus46 | 1,156 | 5,872 | 7,028 | 505 | 4.7 |
| 11 | L0-main | claudeopus46 | 1,292 | 6,411 | 7,703 | 1,584 | 12.0 |

