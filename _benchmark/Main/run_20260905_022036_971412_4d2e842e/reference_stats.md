# Reference Stats — main-agent

**Run started:** 2026-09-05 02:20:36
**Wall time (at last flush):** 692.6 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 13 | 89,754 | 209,281 | 23,879 | 299,035 | 23,002 | 182.5 | claudeopus46 |
| L1-worker | 1 | 3,767 | 992 | 1,018 | 4,759 | 4,759 | 8.4 | claudeopus46 |
| **TOTAL** | **14** | **93,521** | **210,273** | **24,897** | **303,794** | **21,699** | **190.9** | |

**Estimated tokens:** ~75,948 input + ~6,224 output = ~82,172 total
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
| 1 | 1 | `run_analysis_agent` | context=The user wants density (kg/m³…, purpose=Ob… | 21,304 | — | — | 504.5 |
| 2 | 5 | `run_subagent_tool` | kwargs={'block_number': 'PROPblock_2…, purpose=Gro… | 567 | — | — | 8.6 |
| | | **TOTAL (2 tools)** | | **21,871** | | **0** | **513.1** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 13,598 | 417 | 14,015 | 1,507 | 9.5 |
| 2 | L0-main | claudeopus46 | 13,598 | 19,438 | 33,036 | 3,795 | 28.8 |
| 3 | L0-main | claudeopus46 | 13,598 | 28,985 | 42,583 | 5,751 | 41.5 |
| 4 | L0-main | claudeopus46 | 13,598 | 40,464 | 54,062 | 1,926 | 14.7 |
| 5 | L0-main | claudeopus46 | 13,598 | 41,429 | 55,027 | 780 | 6.3 |
| 6 | L1-worker | claudeopus46 | 3,767 | 992 | 4,759 | 1,018 | 8.4 |
| 7 | L0-main | claudeopus46 | 13,598 | 41,927 | 55,525 | 5,392 | 41.0 |
| 8 | L0-main | claudeopus46 | 2,106 | 6,877 | 8,983 | 154 | 2.5 |
| 9 | L0-main | claudeopus46 | 366 | 694 | 1,060 | 137 | 2.2 |
| 10 | L0-main | claudeopus46 | 2,320 | 6,363 | 8,683 | 1,168 | 9.4 |
| 11 | L0-main | claudeopus46 | 366 | 1,643 | 2,009 | 1,124 | 4.9 |
| 12 | L0-main | claudeopus46 | 560 | 6,845 | 7,405 | 100 | 2.1 |
| 13 | L0-main | claudeopus46 | 1,156 | 7,643 | 8,799 | 603 | 6.5 |
| 14 | L0-main | claudeopus46 | 1,292 | 6,556 | 7,848 | 1,442 | 13.1 |

