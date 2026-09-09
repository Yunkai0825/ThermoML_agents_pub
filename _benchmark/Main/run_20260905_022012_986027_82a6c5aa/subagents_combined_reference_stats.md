# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 8 | 30,036 | 29,073 | 8,048 | 59,109 | 7,388 | 55.0 | claudeopus46 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| L1-worker | 18 | 255,056 | 96,119 | 18,328 | 351,175 | 19,509 | 141.9 | claudeopus46 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| verdict | 1 | 972 | 5,589 | 1,003 | 6,561 | 6,561 | 8.9 | claudeopus46 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| **TOTAL** | **27** | **286,064** | **130,781** | **27,379** | **416,845** | **33,458** | **205.8** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| **TOTAL** | **2** | **0** | **0** | **0** | **0** | **0** | **0** |  |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBcomp_4 |  | resolve_compound_ids | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| GLOBcomp_1 |  | resolve_compound_ids | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | ---: | --- |
| Unique Compounds | 2 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| Unique parent blocks | 0 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| Explicit block/subsystem targets | 0 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| Subsystem targets | 0 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| Target-matched data points | 0 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| **TOTAL** | **2** |  |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | --- | ---: | --- |
| 1 | 1 | `resolve_compound_ids` | purpose=Find compound IDs for methano…, queries=['… | 203 | KEEP ←in 277 | 203 | 4.5 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 2 | 3 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=20, p… | 1,101 | KEEP ←in 6,223 | 1101 | 21.5 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 3 | 4 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2825,… | 267 | — | — | 0.0 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 4 | 5 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2825,… | 365 | — | — | 0.2 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 5 | 6 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2825,… | 1,216 | — | — | 0.1 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 6 | 8 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_9, nearest={'… | 1,111 | — | — | 0.1 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 7 | 1 | `L1_query` | context=Property ID for dynamic visco…, id_catalog… | 12,555 | — | — | 138.9 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| **TOTAL** | **28** |  |  | **16,818** |  | **1,304** | **165.3** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 11,581 | 1,009 | 12,590 | 1,261 | 8.1 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,131 | 25,226 | 572 | 5.1 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 3 | L1-worker | claudeopus46 | 3,767 | 431 | 4,198 | 335 | 3.8 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 4 | L1-worker | claudeopus46 | 24,095 | 1,580 | 25,675 | 1,675 | 11.3 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,302 | 26,397 | 659 | 4.8 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 6 | L1-worker | claudeopus46 | 3,767 | 6,709 | 10,476 | 1,738 | 14.7 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,382 | 27,477 | 998 | 7.7 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 8 | L1-worker | claudeopus46 | 24,095 | 4,033 | 28,128 | 609 | 6.4 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,720 | 28,815 | 1,170 | 8.5 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 10 | L1-worker | claudeopus46 | 24,095 | 6,262 | 30,357 | 1,483 | 15.3 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 11 | L1-worker | claudeopus46 | 24,095 | 11,379 | 35,474 | 1,110 | 9.5 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 12 | L1-worker | claudeopus46 | 24,095 | 12,862 | 36,957 | 1,709 | 13.6 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 13 | L1-worker | claudeopus46 | 24,095 | 16,768 | 40,863 | 1,707 | 9.5 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 14 | L1-worker | claudeopus46 | 627 | 2,396 | 3,023 | 693 | 5.3 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 15 | L1-worker | claudeopus46 | 2,106 | 3,768 | 5,874 | 856 | 5.3 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 16 | L1-worker | claudeopus46 | 2,320 | 2,516 | 4,836 | 991 | 6.5 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 17 | L1-worker | claudeopus46 | 366 | 1,633 | 1,999 | 483 | 3.1 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 18 | L1-worker | claudeopus46 | 366 | 1,428 | 1,794 | 946 | 4.4 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 19 | L1-worker | claudeopus46 | 787 | 12,819 | 13,606 | 594 | 7.1 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 20 | L0-main | claudeopus46 | 11,581 | 12,999 | 24,580 | 3,057 | 22.0 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 21 | L0-main | claudeopus46 | 2,106 | 3,310 | 5,416 | 604 | 5.1 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 22 | L0-main | claudeopus46 | 2,320 | 2,469 | 4,789 | 987 | 6.0 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 23 | L0-main | claudeopus46 | 366 | 1,153 | 1,519 | 673 | 3.4 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 24 | L0-main | claudeopus46 | 366 | 1,462 | 1,828 | 938 | 4.0 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 25 | L0-main | claudeopus46 | 560 | 2,942 | 3,502 | 71 | 2.2 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 26 | L0-main | claudeopus46 | 1,156 | 3,729 | 4,885 | 457 | 4.2 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
| 27 | verdict | claudeopus46 | 972 | 5,589 | 6,561 | 1,003 | 8.9 | Find measured viscosity data for a binary mixture of methano (query_runs/run_1) |
