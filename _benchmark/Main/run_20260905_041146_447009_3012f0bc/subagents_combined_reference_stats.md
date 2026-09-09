# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 8 | 30,036 | 43,692 | 11,029 | 73,728 | 9,216 | 75.7 | claudeopus46 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| L1-worker | 18 | 255,056 | 105,278 | 21,015 | 360,334 | 20,018 | 158.4 | claudeopus46 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| verdict | 1 | 972 | 7,868 | 1,081 | 8,840 | 8,840 | 9.7 | claudeopus46 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| L0-main | 9 | 30,402 | 44,355 | 13,646 | 74,757 | 8,306 | 83.1 | claudeopus46 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| L1-worker | 19 | 279,151 | 131,011 | 23,002 | 410,162 | 21,587 | 176.0 | claudeopus46 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| verdict | 1 | 972 | 7,726 | 1,127 | 8,698 | 8,698 | 9.3 | claudeopus46 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| **TOTAL** | **56** | **596,589** | **339,930** | **70,900** | **936,519** | **76,665** | **512.2** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| **TOTAL** | **4** | **0** | **0** | **0** | **0** | **0** | **0** |  |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | ---: | --- |
| Unique Compounds | 2 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| Unique parent blocks | 0 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| Explicit block/subsystem targets | 0 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| Subsystem targets | 0 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| Target-matched data points | 0 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| GLOBcomp_4 |  | resolve_compound_ids |
| GLOBcomp_1 |  | resolve_compound_ids |
| Unique Compounds | 2 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| Unique parent blocks | 0 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| Explicit block/subsystem targets | 0 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| Subsystem targets | 0 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| Target-matched data points | 0 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| **TOTAL** | **4** |  |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | --- | ---: | --- |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve compound ID… | 176 | KEEP ←in 278 | 176 | 4.2 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=20, p… | 1,301 | KEEP ←in 6,284 | 1301 | 18.3 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 3 | 5 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_11, purpose=G… | 348 | — | — | 0.2 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 4 | 6 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_11, purpose=G… | 1,414 | — | — | 0.1 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 5 | 7 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_21, purpose=G… | 1,628 | — | — | 0.1 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 6 | 9 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_21, nearest={… | 780 | — | — | 0.1 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 7 | 1 | `L1_query` | context=User needs mixture viscosity …, id_catalog… | 24,000 | — | — | 148.3 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve methanol an… | 180 | KEEP ←in 277 | 180 | 3.4 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=20, p… | 1,129 | KEEP ←in 6,223 | 1129 | 19.0 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 3 | 5 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_9, purpose=Ge… | 348 | — | — | 0.6 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 4 | 6 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_9, purpose=Ge… | 1,507 | — | — | 0.1 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 5 | 8 | `inspect_block_table` | block_number=GLOBlit_8869::PROPblock_3, purpose=Gr… | 955 | — | — | 0.1 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 6 | 9 | `inspect_block_table` | block_number=GLOBlit_9571::PROPblock_1, purpose=In… | 1,028 | — | — | 0.1 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 7 | 1 | `L1_query` | context=User needs mixture viscosity …, id_catalog… | 27,486 | — | — | 171.2 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| **TOTAL** | **69** |  |  | **62,280** |  | **2,786** | **365.8** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 11,581 | 913 | 12,494 | 1,622 | 9.0 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,265 | 25,360 | 617 | 4.4 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,274 | 26,369 | 523 | 4.3 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 4 | L1-worker | claudeopus46 | 3,767 | 431 | 4,198 | 351 | 4.1 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,870 | 25,965 | 927 | 7.1 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,612 | 26,707 | 732 | 5.5 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 7 | L1-worker | claudeopus46 | 3,767 | 6,797 | 10,564 | 1,625 | 15.0 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,874 | 27,969 | 1,087 | 8.8 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,610 | 28,705 | 631 | 6.2 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 10 | L1-worker | claudeopus46 | 24,095 | 6,383 | 30,478 | 1,000 | 8.2 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 11 | L1-worker | claudeopus46 | 24,095 | 8,369 | 32,464 | 3,435 | 23.5 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 12 | L1-worker | claudeopus46 | 24,095 | 16,201 | 40,296 | 1,867 | 15.6 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 13 | L1-worker | claudeopus46 | 24,095 | 17,363 | 41,458 | 2,864 | 20.9 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 14 | L1-worker | claudeopus46 | 2,106 | 4,379 | 6,485 | 1,085 | 6.1 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 15 | L1-worker | claudeopus46 | 2,320 | 2,993 | 5,313 | 898 | 6.1 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 16 | L1-worker | claudeopus46 | 627 | 2,873 | 3,500 | 1,114 | 7.6 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 17 | L1-worker | claudeopus46 | 366 | 1,862 | 2,228 | 778 | 3.8 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 18 | L1-worker | claudeopus46 | 366 | 1,335 | 1,701 | 863 | 4.2 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 19 | L1-worker | claudeopus46 | 787 | 19,787 | 20,574 | 618 | 7.0 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 20 | L0-main | claudeopus46 | 11,581 | 19,848 | 31,429 | 4,149 | 30.0 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 21 | L0-main | claudeopus46 | 2,320 | 4,039 | 6,359 | 1,251 | 6.8 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 22 | L0-main | claudeopus46 | 2,106 | 4,784 | 6,890 | 775 | 12.2 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 23 | L0-main | claudeopus46 | 366 | 1,726 | 2,092 | 1,202 | 5.4 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 24 | L0-main | claudeopus46 | 366 | 1,324 | 1,690 | 925 | 3.9 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 25 | L0-main | claudeopus46 | 560 | 4,792 | 5,352 | 131 | 2.2 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 26 | L0-main | claudeopus46 | 1,156 | 6,266 | 7,422 | 974 | 6.2 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 27 | verdict | claudeopus46 | 972 | 7,868 | 8,840 | 1,081 | 9.7 | Find viscosity data for the binary mixture of ethanol and wa (query_runs/run_1) |
| 1 | L0-main | claudeopus46 | 11,581 | 915 | 12,496 | 1,611 | 8.9 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,272 | 25,367 | 548 | 5.4 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,290 | 26,385 | 535 | 3.9 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 4 | L1-worker | claudeopus46 | 3,767 | 438 | 4,205 | 317 | 3.3 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,876 | 25,971 | 915 | 6.8 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,592 | 26,687 | 740 | 4.9 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 7 | L1-worker | claudeopus46 | 3,767 | 6,725 | 10,492 | 1,666 | 15.3 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,684 | 27,779 | 968 | 7.8 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,379 | 28,474 | 593 | 6.1 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 10 | L1-worker | claudeopus46 | 24,095 | 6,180 | 30,275 | 2,306 | 18.0 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 11 | L1-worker | claudeopus46 | 24,095 | 11,960 | 36,055 | 3,222 | 21.0 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 12 | L1-worker | claudeopus46 | 24,095 | 13,278 | 37,373 | 517 | 5.3 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 13 | L1-worker | claudeopus46 | 24,095 | 14,631 | 38,726 | 2,650 | 21.7 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 14 | L1-worker | claudeopus46 | 24,095 | 21,579 | 45,674 | 2,669 | 21.2 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 15 | L1-worker | claudeopus46 | 2,320 | 3,333 | 5,653 | 772 | 5.0 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 16 | L1-worker | claudeopus46 | 627 | 3,213 | 3,840 | 775 | 6.4 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 17 | L1-worker | claudeopus46 | 366 | 1,209 | 1,575 | 311 | 2.4 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 18 | L1-worker | claudeopus46 | 2,106 | 4,726 | 6,832 | 1,751 | 8.5 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 19 | L1-worker | claudeopus46 | 366 | 2,528 | 2,894 | 1,008 | 4.6 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 20 | L1-worker | claudeopus46 | 787 | 25,118 | 25,905 | 739 | 8.4 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 21 | L0-main | claudeopus46 | 11,581 | 18,819 | 30,400 | 4,706 | 34.1 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 22 | L0-main | claudeopus46 | 2,106 | 4,367 | 6,473 | 689 | 5.7 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 23 | L0-main | claudeopus46 | 2,320 | 3,620 | 5,940 | 1,223 | 7.3 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 24 | L0-main | claudeopus46 | 366 | 1,238 | 1,604 | 914 | 4.3 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 25 | L0-main | claudeopus46 | 366 | 1,698 | 2,064 | 1,174 | 4.5 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 26 | L0-main | claudeopus46 | 560 | 4,627 | 5,187 | 171 | 2.4 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 27 | L0-main | claudeopus46 | 1,156 | 6,776 | 7,932 | 1,602 | 10.4 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 28 | L0-main | claudeopus46 | 366 | 2,295 | 2,661 | 1,556 | 5.5 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| 29 | verdict | claudeopus46 | 972 | 7,726 | 8,698 | 1,127 | 9.3 | Find viscosity data for the binary mixture of methanol and w (query_runs/run_2) |
| **TOTAL** |  |  | **596,589** | **339,930** | **936,519** | **70,900** | **512.2** |  |
