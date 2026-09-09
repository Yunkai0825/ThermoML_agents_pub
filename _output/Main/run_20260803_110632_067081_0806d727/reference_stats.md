# Reference Stats — main-agent

**Run started:** 2026-08-03 11:06:32
**Wall time (at last flush):** 2,758.5 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 13 | 85,878 | 270,792 | 82,959 | 356,670 | 27,436 | 406.3 | claudeopus46 |
| L0-menu-planner | 2 | 1,662 | 3,026 | 9,247 | 4,688 | 2,344 | 41.0 | claudesonnet46 |
| **TOTAL** | **15** | **87,540** | **273,818** | **92,206** | **361,358** | **24,090** | **447.3** | |

**Estimated tokens:** ~90,339 input + ~23,051 output = ~113,390 total
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

## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `browse_subagent_tools` | purpose=Find water-based binary solve…, tasks=Sear… | 4,365 | — | — | 52.3 |
| 2 | 4 | `browse_subagent_tools` | purpose=Find water + co-solvent binar…, tasks=1. R… | 4,882 | — | — | 19.2 |
| 3 | 5 | `run_parallel_subagents` | tasks=[{'agent': 'query', 'label': … | 12,555 | — | — | 2302.3 |
| | | **TOTAL (3 tools)** | | **21,802** | | **0** | **2373.8** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | interval=2 | skipped_by_agent | 5,665 | 5,665 | 0 | 0.0% |
| 2 | interval=2 | skipped_by_agent | 12,415 | 12,415 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 10,215 | 615 | 10,830 | 2,205 | 11.4 |
| 2 | L0-main | claudeopus46 | 10,215 | 1,771 | 11,986 | 16,651 | 68.4 |
| 3 | L0-menu-planner | claudesonnet46 | 831 | 1,533 | 2,364 | 4,365 | 22.2 |
| 4 | L0-main | claudeopus46 | 10,182 | 6,747 | 16,929 | 581 | 5.1 |
| 5 | L0-main | claudeopus46 | 10,215 | 5,990 | 16,205 | 14,017 | 58.4 |
| 6 | L0-main | claudeopus46 | 10,215 | 10,604 | 20,819 | 1,104 | 8.4 |
| 7 | L0-menu-planner | claudesonnet46 | 831 | 1,493 | 2,324 | 4,882 | 18.8 |
| 8 | L0-main | claudeopus46 | 10,182 | 13,626 | 23,808 | 621 | 5.6 |
| 9 | L0-main | claudeopus46 | 10,215 | 12,867 | 23,082 | 5,444 | 17.5 |
| 10 | L0-main | claudeopus46 | 10,215 | 131,683 | 141,898 | 16,449 | 101.1 |
| 11 | L0-main | claudeopus46 | 1,356 | 14,396 | 15,752 | 2,356 | 16.1 |
| 12 | L0-main | claudeopus46 | 298 | 2,738 | 3,036 | 2,296 | 7.0 |
| 13 | L0-main | claudeopus46 | 1,323 | 51,465 | 52,788 | 10,371 | 50.2 |
| 14 | L0-main | claudeopus46 | 298 | 10,894 | 11,192 | 9,269 | 44.6 |
| 15 | L0-main | claudeopus46 | 949 | 7,396 | 8,345 | 1,595 | 12.5 |

