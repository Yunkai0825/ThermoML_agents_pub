# Reference Stats — main-agent

**Run started:** 2026-09-05 04:59:51
**Wall time (at last flush):** 1,192.4 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 13 | 76,522 | 206,468 | 40,502 | 282,990 | 21,768 | 254.3 | claudeopus46 |
| **TOTAL** | **13** | **76,522** | **206,468** | **40,502** | **282,990** | **21,768** | **254.3** | |

**Estimated tokens:** ~70,747 input + ~10,125 output = ~80,872 total
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
| 1 | 2 | `run_query_agent` | context=The user wants to understand …, purpose=Se… | 44,808 | — | — | 946.4 |
| | | **TOTAL (1 tools)** | | **44,808** | | **0** | **946.4** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 253 | 13,851 | 1,583 | 9.0 |
| 2 | L0-main | claudeopus46 | 13,598 | 912 | 14,510 | 1,322 | 7.9 |
| 3 | L0-main | claudeopus46 | 13,598 | 33,777 | 47,375 | 7,616 | 50.2 |
| 4 | L0-main | claudeopus46 | 13,598 | 45,847 | 59,445 | 10,166 | 64.2 |
| 5 | L0-main | claudeopus46 | 13,598 | 60,317 | 73,915 | 9,568 | 61.5 |
| 6 | L0-main | claudeopus46 | 2,106 | 11,802 | 13,908 | 637 | 4.9 |
| 7 | L0-main | claudeopus46 | 2,320 | 11,452 | 13,772 | 1,106 | 9.5 |
| 8 | L0-main | claudeopus46 | 366 | 1,177 | 1,543 | 1,020 | 5.0 |
| 9 | L0-main | claudeopus46 | 366 | 1,581 | 1,947 | 1,062 | 4.0 |
| 10 | L0-main | claudeopus46 | 560 | 13,211 | 13,771 | 447 | 3.6 |
| 11 | L0-main | claudeopus46 | 1,156 | 16,750 | 17,906 | 2,386 | 14.9 |
| 12 | L0-main | claudeopus46 | 366 | 3,079 | 3,445 | 2,076 | 7.5 |
| 13 | L0-main | claudeopus46 | 1,292 | 6,310 | 7,602 | 1,513 | 12.1 |

