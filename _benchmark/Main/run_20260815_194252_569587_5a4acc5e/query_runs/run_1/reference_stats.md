# Reference Stats — query-agent

**Run started:** 2026-08-15 19:43:17
**Wall time (at last flush):** 148.9 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 30,036 | 26,798 | 7,249 | 56,834 | 7,104 | 48.2 | claudeopus46 |
| L1-worker | 15 | 182,771 | 52,509 | 14,442 | 235,280 | 15,685 | 103.8 | claudeopus46 |
| verdict | 1 | 972 | 5,467 | 1,079 | 6,439 | 6,439 | 10.5 | claudeopus46 |
| **TOTAL** | **24** | **213,779** | **84,774** | **22,770** | **298,553** | **12,439** | **162.5** | |

**Estimated tokens:** ~74,638 input + ~5,692 output = ~80,330 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 1 | 1 | 1 | 1 | 7 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **4** | **1** | **1** | **1** | **1** | **1** | **7** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_4 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_15 |  | resolve_compound_ids, search_blocks |

#### References (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_8821 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |

#### Measurements (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_22 | Surface tension liquid-gas, N/m | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_2 | Mole fraction | search_blocks |

#### Constraints (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 1 |
| Unique Properties | 1 |
| Unique Measurements | 1 |
| Unique Phases | 1 |
| Unique Variables | 1 |
| Unique Constraints | 1 |
| Total DOIs | 1 |
| Unique parent blocks | 1 |
| Explicit block/subsystem targets | 1 |
| Subsystem targets | 0 |
| Target-matched data points | 7 |

---

## 3. DOI & Block References

**Unique DOIs:** 1  |  **Parent blocks:** 1  |  **Explicit targets:** 1  |  **Subsystems:** 0  |  **Target-matched datapoints:** 7

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1021/je050519g | 1 | 7 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1021/je050519g | PROPblock_13 | declared | 7 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve compound ID… | 263 | KEEP ←in 290 | 263 | 5.8 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_15'], limit=50, … | 1,269 | KEEP ←in 1,699 | 1254 | 15.0 |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_13, literature=GLOBlit_8821… | 996 | — | — | 0.1 |
| 4 | 1 | `L1_query` | context=Surface tension is GLOBprop_1…, id_catalog… | 10,732 | — | — | 97.7 |
| | | **TOTAL (4 tools)** | | **13,260** | | **1,517** | **118.6** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 1,011 | 12,592 | 1,281 | 7.5 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,158 | 25,253 | 683 | 5.0 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,219 | 26,314 | 591 | 6.1 |
| 4 | L1-worker | claudeopus46 | 3,767 | 487 | 4,254 | 411 | 5.4 |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,048 | 26,143 | 841 | 6.0 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,784 | 26,879 | 712 | 5.0 |
| 7 | L1-worker | claudeopus46 | 3,767 | 2,231 | 5,998 | 1,654 | 10.3 |
| 8 | L1-worker | claudeopus46 | 24,095 | 4,216 | 28,311 | 788 | 6.3 |
| 9 | L1-worker | claudeopus46 | 24,095 | 5,711 | 29,806 | 1,883 | 12.9 |
| 10 | L1-worker | claudeopus46 | 24,095 | 12,304 | 36,399 | 2,833 | 20.6 |
| 11 | L1-worker | claudeopus46 | 2,320 | 1,668 | 3,988 | 677 | 4.5 |
| 12 | L1-worker | claudeopus46 | 2,106 | 2,947 | 5,053 | 863 | 4.8 |
| 13 | L1-worker | claudeopus46 | 627 | 1,548 | 2,175 | 782 | 5.0 |
| 14 | L1-worker | claudeopus46 | 366 | 1,114 | 1,480 | 642 | 2.9 |
| 15 | L1-worker | claudeopus46 | 366 | 1,640 | 2,006 | 603 | 3.5 |
| 16 | L1-worker | claudeopus46 | 787 | 10,434 | 11,221 | 479 | 5.5 |
| 17 | L0-main | claudeopus46 | 11,581 | 11,717 | 23,298 | 2,442 | 15.1 |
| 18 | L0-main | claudeopus46 | 2,320 | 2,267 | 4,587 | 848 | 4.4 |
| 19 | L0-main | claudeopus46 | 2,106 | 3,110 | 5,216 | 645 | 4.8 |
| 20 | L0-main | claudeopus46 | 366 | 1,194 | 1,560 | 714 | 3.2 |
| 21 | L0-main | claudeopus46 | 366 | 1,323 | 1,689 | 809 | 7.2 |
| 22 | L0-main | claudeopus46 | 560 | 2,733 | 3,293 | 64 | 2.0 |
| 23 | L0-main | claudeopus46 | 1,156 | 3,443 | 4,599 | 446 | 4.0 |
| 24 | verdict | claudeopus46 | 972 | 5,467 | 6,439 | 1,079 | 10.5 |

