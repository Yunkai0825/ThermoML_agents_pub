# Reference Stats — query-agent

**Run started:** 2026-09-05 04:20:47
**Wall time (at last flush):** 207.0 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 30,036 | 34,622 | 9,375 | 64,658 | 8,082 | 57.5 | claudeopus46 |
| L1-worker | 19 | 256,284 | 101,146 | 19,704 | 357,430 | 18,812 | 151.0 | claudeopus46 |
| verdict | 1 | 972 | 6,155 | 1,180 | 7,127 | 7,127 | 12.7 | claudeopus46 |
| **TOTAL** | **28** | **287,292** | **141,923** | **30,259** | **429,215** | **15,329** | **221.2** | |

**Estimated tokens:** ~107,303 input + ~7,564 output = ~114,867 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **2** | **0** | **0** | **0** | **0** | **0** | **0** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_15 |  | resolve_compound_ids |
| GLOBcomp_18 |  | resolve_compound_ids |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
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
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 206 | KEEP ←in 308 | 206 | 4.3 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_15', 'GLOBcomp_18'], limit=20,… | 795 | KEEP ←in 4,801 | 795 | 20.9 |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_4124,… | 372 | — | — | 0.3 |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_4124,… | 1,093 | — | — | 0.0 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_7481… | 1,405 | — | — | 0.1 |
| 6 | 1 | `L1_query` | context=Binary system: acetonitrile (…, id_catalog… | 20,246 | — | — | 144.9 |
| | | **TOTAL (6 tools)** | | **24,117** | | **1,001** | **170.5** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 938 | 12,519 | 1,300 | 7.9 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,291 | 25,386 | 665 | 5.1 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,327 | 26,422 | 571 | 3.9 |
| 4 | L1-worker | claudeopus46 | 3,767 | 467 | 4,234 | 384 | 4.2 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,945 | 26,040 | 774 | 6.3 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,669 | 26,764 | 657 | 5.2 |
| 7 | L1-worker | claudeopus46 | 3,767 | 5,261 | 9,028 | 1,533 | 14.3 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,441 | 27,536 | 921 | 7.1 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,203 | 28,298 | 591 | 5.2 |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,606 | 29,701 | 673 | 5.7 |
| 11 | L1-worker | claudeopus46 | 24,095 | 7,356 | 31,451 | 2,033 | 15.0 |
| 12 | L1-worker | claudeopus46 | 24,095 | 12,981 | 37,076 | 3,015 | 21.9 |
| 13 | L1-worker | claudeopus46 | 24,095 | 19,486 | 43,581 | 2,088 | 16.6 |
| 14 | L1-worker | claudeopus46 | 2,320 | 2,219 | 4,539 | 924 | 5.2 |
| 15 | L1-worker | claudeopus46 | 627 | 2,099 | 2,726 | 859 | 5.3 |
| 16 | L1-worker | claudeopus46 | 366 | 1,361 | 1,727 | 879 | 4.7 |
| 17 | L1-worker | claudeopus46 | 2,106 | 3,631 | 5,737 | 1,218 | 11.7 |
| 18 | L1-worker | claudeopus46 | 366 | 1,995 | 2,361 | 733 | 4.1 |
| 19 | L1-worker | claudeopus46 | 1,228 | 4,945 | 6,173 | 737 | 4.3 |
| 20 | L1-worker | claudeopus46 | 787 | 17,863 | 18,650 | 449 | 5.2 |
| 21 | L0-main | claudeopus46 | 11,581 | 15,827 | 27,408 | 2,825 | 20.2 |
| 22 | L0-main | claudeopus46 | 2,106 | 3,514 | 5,620 | 653 | 5.2 |
| 23 | L0-main | claudeopus46 | 2,320 | 2,744 | 5,064 | 1,395 | 6.1 |
| 24 | L0-main | claudeopus46 | 366 | 1,202 | 1,568 | 803 | 4.1 |
| 25 | L0-main | claudeopus46 | 366 | 1,870 | 2,236 | 1,341 | 4.6 |
| 26 | L0-main | claudeopus46 | 560 | 3,495 | 4,055 | 129 | 2.4 |
| 27 | L0-main | claudeopus46 | 1,156 | 5,032 | 6,188 | 929 | 7.0 |
| 28 | verdict | claudeopus46 | 972 | 6,155 | 7,127 | 1,180 | 12.7 |

