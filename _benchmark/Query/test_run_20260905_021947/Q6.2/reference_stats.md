# Reference Stats — query-agent

**Run started:** 2026-09-05 06:02:43
**Wall time (at last flush):** 89.2 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 6 | 28,320 | 10,301 | 3,900 | 38,621 | 6,436 | 24.6 | claudeopus46 |
| L1-worker | 13 | 137,982 | 22,630 | 9,601 | 160,612 | 12,354 | 75.0 | claudeopus46 |
| **TOTAL** | **19** | **166,302** | **32,931** | **13,501** | **199,233** | **10,485** | **99.6** | |

**Estimated tokens:** ~49,808 input + ~3,375 output = ~53,183 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 15 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_id_alignment` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **26** | **0** | **0** | **0** | **0** | **0** | **0** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (26 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_838 |  | resolve_compound_ids |
| GLOBcomp_1023 |  | resolve_compound_ids |
| GLOBcomp_2943 |  | resolve_compound_ids |
| GLOBcomp_199 |  | resolve_compound_ids |
| GLOBcomp_2520 |  | resolve_compound_ids |
| GLOBcomp_1687 |  | resolve_compound_ids |
| GLOBcomp_633 |  | resolve_compound_ids |
| GLOBcomp_547 |  | resolve_compound_ids |
| GLOBcomp_358 |  | resolve_compound_ids |
| GLOBcomp_600 |  | resolve_compound_ids |
| GLOBcomp_3 |  | resolve_compound_ids |
| GLOBcomp_62 |  | resolve_compound_ids |
| GLOBcomp_103 |  | resolve_compound_ids |
| GLOBcomp_214 |  | resolve_compound_ids |
| GLOBcomp_226 |  | resolve_compound_ids |
| GLOBcomp_234 |  | resolve_compound_ids |
| GLOBcomp_312 |  | resolve_compound_ids |
| GLOBcomp_708 |  | resolve_compound_ids |
| GLOBcomp_811 |  | resolve_compound_ids |
| GLOBcomp_904 |  | resolve_compound_ids |
| GLOBcomp_927 |  | resolve_compound_ids |
| GLOBcomp_937 |  | resolve_compound_ids |
| GLOBcomp_993 |  | resolve_compound_ids |
| GLOBcomp_1016 |  | resolve_compound_ids |
| GLOBcomp_1066 |  | resolve_compound_ids |
| GLOBcomp_51 |  | search_id_alignment |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 26 |
| Total DOIs | 0 |
| Unique parent blocks | 0 |
| Explicit block/subsystem targets | 0 |
| Subsystem targets | 0 |
| Target-matched data points | 0 |

---

## 3. DOI & Block References

*(no DOI/block references recorded)*

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=10, min_score=40, purpose=Find compound ID f… | 574 | DISCARD ←in 980 | 509 | 7.5 |
| 2 | 3 | `resolve_compound_ids` | limit=15, min_score=30, purpose=Find compound ID f… | 658 | DISCARD ←in 1,475 | 593 | 10.2 |
| 3 | 4 | `search_id_alignment` | entity_type=compound, limit=20, purpose=Find eleme… | 912 | DISCARD ←in 299 | 848 | 9.3 |
| 4 | 1 | `L1_query` | instruction=Search for any thermodynamic …, purpos… | 2,281 | — | — | 69.7 |
| | | **TOTAL (4 tools)** | | **4,425** | | **1,950** | **96.7** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 528 | 12,109 | 1,227 | 8.0 |
| 2 | L1-worker | claudeopus46 | 24,095 | 836 | 24,931 | 638 | 5.2 |
| 3 | L1-worker | claudeopus46 | 24,095 | 1,875 | 25,970 | 565 | 4.1 |
| 4 | L1-worker | claudeopus46 | 3,767 | 1,148 | 4,915 | 886 | 6.9 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,850 | 25,945 | 758 | 7.5 |
| 6 | L1-worker | claudeopus46 | 3,767 | 1,650 | 5,417 | 1,179 | 9.9 |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,847 | 26,942 | 957 | 6.9 |
| 8 | L1-worker | claudeopus46 | 3,767 | 477 | 4,244 | 1,192 | 9.1 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,073 | 28,168 | 1,523 | 9.8 |
| 10 | L1-worker | claudeopus46 | 2,106 | 1,971 | 4,077 | 92 | 2.1 |
| 11 | L1-worker | claudeopus46 | 627 | 894 | 1,521 | 584 | 3.1 |
| 12 | L1-worker | claudeopus46 | 2,320 | 1,014 | 3,334 | 636 | 3.9 |
| 13 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.0 |
| 14 | L1-worker | claudeopus46 | 787 | 3,126 | 3,913 | 524 | 4.5 |
| 15 | L0-main | claudeopus46 | 11,581 | 5,311 | 16,892 | 910 | 4.1 |
| 16 | L0-main | claudeopus46 | 2,320 | 1,080 | 3,400 | 517 | 3.4 |
| 17 | L0-main | claudeopus46 | 2,106 | 1,440 | 3,546 | 401 | 3.8 |
| 18 | L0-main | claudeopus46 | 366 | 992 | 1,358 | 478 | 2.7 |
| 19 | L0-main | claudeopus46 | 366 | 950 | 1,316 | 367 | 2.6 |

