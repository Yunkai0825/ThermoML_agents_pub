# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 8 | 30,036 | 26,798 | 7,249 | 56,834 | 7,104 | 48.2 | claudeopus46 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| L1-worker | 15 | 182,771 | 52,509 | 14,442 | 235,280 | 15,685 | 103.8 | claudeopus46 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| verdict | 1 | 972 | 5,467 | 1,079 | 6,439 | 6,439 | 10.5 | claudeopus46 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| **TOTAL** | **24** | **213,779** | **84,774** | **22,770** | **298,553** | **29,228** | **162.5** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| `search_blocks` | 2 | 1 | 1 | 1 | 1 | 1 | 7 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| **TOTAL** | **4** | **1** | **1** | **1** | **1** | **1** | **7** |  |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBcomp_4 |  | resolve_compound_ids, search_blocks | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| GLOBcomp_15 |  | resolve_compound_ids, search_blocks | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBlit_8821 |  | search_blocks | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBmeas_22 | Surface tension liquid-gas, N/m | search_blocks | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBphase_1 |  | search_blocks | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBvar_2 | Mole fraction | search_blocks | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBconstr_2 | Temperature, K | search_blocks | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | ---: | --- |
| Unique Compounds | 2 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| Unique References | 1 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| Unique Properties | 1 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| Unique Measurements | 1 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| Unique Phases | 1 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| Unique Variables | 1 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| Unique Constraints | 1 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| Unique parent blocks | 1 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| Explicit block/subsystem targets | 1 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| Subsystem targets | 0 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| Target-matched data points | 7 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| **TOTAL** | **17** |  |


## 3. DOI & Block References

| DOI | Blocks | Datapoints | System types | Source tools | Source |
| --- | ---: | ---: | --- | --- | --- |
| 10.1021/je050519g | 1 | 7 | binary | search_blocks | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 10.1021/je050519g | PROPblock_13 | declared | 7 | binary | — | search_blocks | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | ---: | ---: | --- |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve compound ID… | 263 | KEEP ←in 290 | 263 | 5.8 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_15'], limit=50, … | 1,269 | KEEP ←in 1,699 | 1254 | 15.0 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_13, literature=GLOBlit_8821… | 996 | — | — | 0.1 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 4 | 1 | `L1_query` | context=Surface tension is GLOBprop_1…, id_catalog… | 10,732 | — | — | 97.7 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| **TOTAL** | **12** |  |  | **13,260** |  | **1,517** | **118.6** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 11,581 | 1,011 | 12,592 | 1,281 | 7.5 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,158 | 25,253 | 683 | 5.0 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,219 | 26,314 | 591 | 6.1 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 4 | L1-worker | claudeopus46 | 3,767 | 487 | 4,254 | 411 | 5.4 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,048 | 26,143 | 841 | 6.0 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,784 | 26,879 | 712 | 5.0 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 7 | L1-worker | claudeopus46 | 3,767 | 2,231 | 5,998 | 1,654 | 10.3 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 8 | L1-worker | claudeopus46 | 24,095 | 4,216 | 28,311 | 788 | 6.3 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 9 | L1-worker | claudeopus46 | 24,095 | 5,711 | 29,806 | 1,883 | 12.9 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 10 | L1-worker | claudeopus46 | 24,095 | 12,304 | 36,399 | 2,833 | 20.6 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 11 | L1-worker | claudeopus46 | 2,320 | 1,668 | 3,988 | 677 | 4.5 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 12 | L1-worker | claudeopus46 | 2,106 | 2,947 | 5,053 | 863 | 4.8 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 13 | L1-worker | claudeopus46 | 627 | 1,548 | 2,175 | 782 | 5.0 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 14 | L1-worker | claudeopus46 | 366 | 1,114 | 1,480 | 642 | 2.9 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 15 | L1-worker | claudeopus46 | 366 | 1,640 | 2,006 | 603 | 3.5 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 16 | L1-worker | claudeopus46 | 787 | 10,434 | 11,221 | 479 | 5.5 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 17 | L0-main | claudeopus46 | 11,581 | 11,717 | 23,298 | 2,442 | 15.1 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 18 | L0-main | claudeopus46 | 2,320 | 2,267 | 4,587 | 848 | 4.4 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 19 | L0-main | claudeopus46 | 2,106 | 3,110 | 5,216 | 645 | 4.8 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 20 | L0-main | claudeopus46 | 366 | 1,194 | 1,560 | 714 | 3.2 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 21 | L0-main | claudeopus46 | 366 | 1,323 | 1,689 | 809 | 7.2 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 22 | L0-main | claudeopus46 | 560 | 2,733 | 3,293 | 64 | 2.0 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 23 | L0-main | claudeopus46 | 1,156 | 3,443 | 4,599 | 446 | 4.0 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
| 24 | verdict | claudeopus46 | 972 | 5,467 | 6,439 | 1,079 | 10.5 | Find surface tension data for binary mixtures of methanol an (query_runs/run_1) |
