# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 8 | 30,036 | 24,577 | 6,123 | 54,613 | 6,826 | 42.2 | claudeopus46 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| L1-worker | 15 | 182,771 | 48,251 | 12,923 | 231,022 | 15,401 | 94.5 | claudeopus46 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| verdict | 1 | 972 | 4,073 | 1,112 | 5,045 | 5,045 | 9.9 | claudeopus46 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| L0-main | 8 | 30,036 | 34,622 | 9,375 | 64,658 | 8,082 | 57.5 | claudeopus46 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| L1-worker | 19 | 256,284 | 101,146 | 19,704 | 357,430 | 18,812 | 151.0 | claudeopus46 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| verdict | 1 | 972 | 6,155 | 1,180 | 7,127 | 7,127 | 12.7 | claudeopus46 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| L0-main | 8 | 30,036 | 41,918 | 10,088 | 71,954 | 8,994 | 61.5 | claudeopus46 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| L1-worker | 18 | 255,056 | 113,489 | 24,315 | 368,545 | 20,474 | 185.9 | claudeopus46 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| verdict | 1 | 972 | 7,233 | 1,093 | 8,205 | 8,205 | 11.7 | claudeopus46 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| **TOTAL** | **79** | **787,135** | **381,464** | **85,913** | **1,168,599** | **98,966** | **626.9** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| **TOTAL** | **6** | **0** | **0** | **0** | **0** | **0** | **0** |  |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | ---: | --- |
| Unique Compounds | 2 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| Unique parent blocks | 0 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| Explicit block/subsystem targets | 0 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| Subsystem targets | 0 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| Target-matched data points | 0 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| GLOBcomp_15 |  | resolve_compound_ids |
| GLOBcomp_18 |  | resolve_compound_ids |
| Unique Compounds | 2 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| Unique parent blocks | 0 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| Explicit block/subsystem targets | 0 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| Subsystem targets | 0 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| Target-matched data points | 0 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| GLOBcomp_1 |  | resolve_compound_ids |
| GLOBcomp_24 |  | resolve_compound_ids |
| Unique Compounds | 2 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| Unique parent blocks | 0 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| Explicit block/subsystem targets | 0 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| Subsystem targets | 0 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| Target-matched data points | 0 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| **TOTAL** | **6** |  |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | --- | ---: | --- |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve methanol an… | 330 | KEEP ←in 283 | 330 | 4.8 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_2'], limit=20, p… | 1,290 | KEEP ←in 1,863 | 1274 | 17.1 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_16, literature=GLOBlit_1133… | 1,353 | — | — | 0.3 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 4 | 1 | `L1_query` | context=Binary system: methanol + eth…, id_catalog… | 11,432 | — | — | 91.6 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 206 | KEEP ←in 308 | 206 | 4.3 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_15', 'GLOBcomp_18'], limit=20,… | 795 | KEEP ←in 4,801 | 795 | 20.9 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_4124,… | 372 | — | — | 0.3 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_4124,… | 1,093 | — | — | 0.0 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_7481… | 1,405 | — | — | 0.1 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 6 | 1 | `L1_query` | context=Binary system: acetonitrile (…, id_catalog… | 20,246 | — | — | 144.9 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 232 | KEEP ←in 288 | 232 | 4.4 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=20, … | 949 | KEEP ←in 7,245 | 949 | 21.7 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_24, literature=GLOBlit_5201… | 371 | — | — | 0.3 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_24, literature=GLOBlit_5201… | 1,750 | — | — | 0.1 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_6951… | 1,369 | — | — | 0.1 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 6 | 1 | `L1_query` | context=Binary system: water (H2O) + …, id_catalog… | 23,962 | — | — | 179.9 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| **TOTAL** | **62** |  |  | **67,155** |  | **3,786** | **490.8** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 11,581 | 891 | 12,472 | 1,151 | 7.5 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,162 | 25,257 | 662 | 5.6 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,214 | 26,309 | 588 | 4.1 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 4 | L1-worker | claudeopus46 | 3,767 | 476 | 4,243 | 489 | 4.6 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,933 | 26,028 | 783 | 6.3 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,618 | 26,713 | 754 | 5.7 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 7 | L1-worker | claudeopus46 | 3,767 | 2,371 | 6,138 | 1,738 | 12.0 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,889 | 27,984 | 720 | 6.2 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 9 | L1-worker | claudeopus46 | 24,095 | 5,584 | 29,679 | 1,457 | 9.8 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 10 | L1-worker | claudeopus46 | 24,095 | 10,088 | 34,183 | 2,559 | 16.6 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 11 | L1-worker | claudeopus46 | 2,106 | 2,822 | 4,928 | 502 | 3.4 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 12 | L1-worker | claudeopus46 | 2,320 | 1,539 | 3,859 | 625 | 3.9 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 13 | L1-worker | claudeopus46 | 627 | 1,419 | 2,046 | 596 | 4.1 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 14 | L1-worker | claudeopus46 | 366 | 1,279 | 1,645 | 375 | 2.7 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 15 | L1-worker | claudeopus46 | 366 | 1,062 | 1,428 | 595 | 3.4 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 16 | L1-worker | claudeopus46 | 787 | 9,795 | 10,582 | 480 | 6.1 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 17 | L0-main | claudeopus46 | 11,581 | 10,810 | 22,391 | 2,110 | 13.9 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 18 | L0-main | claudeopus46 | 2,106 | 2,781 | 4,887 | 512 | 4.0 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 19 | L0-main | claudeopus46 | 2,320 | 2,058 | 4,378 | 655 | 4.5 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 20 | L0-main | claudeopus46 | 366 | 1,130 | 1,496 | 621 | 3.1 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 21 | L0-main | claudeopus46 | 366 | 1,061 | 1,427 | 581 | 3.7 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 22 | L0-main | claudeopus46 | 560 | 2,524 | 3,084 | 64 | 1.8 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 23 | L0-main | claudeopus46 | 1,156 | 3,322 | 4,478 | 429 | 3.7 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 24 | verdict | claudeopus46 | 972 | 4,073 | 5,045 | 1,112 | 9.9 | Find viscosity data for the binary mixture of methanol + eth (query_runs/run_3) |
| 1 | L0-main | claudeopus46 | 11,581 | 938 | 12,519 | 1,300 | 7.9 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,291 | 25,386 | 665 | 5.1 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,327 | 26,422 | 571 | 3.9 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 4 | L1-worker | claudeopus46 | 3,767 | 467 | 4,234 | 384 | 4.2 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,945 | 26,040 | 774 | 6.3 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,669 | 26,764 | 657 | 5.2 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 7 | L1-worker | claudeopus46 | 3,767 | 5,261 | 9,028 | 1,533 | 14.3 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,441 | 27,536 | 921 | 7.1 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,203 | 28,298 | 591 | 5.2 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,606 | 29,701 | 673 | 5.7 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 11 | L1-worker | claudeopus46 | 24,095 | 7,356 | 31,451 | 2,033 | 15.0 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 12 | L1-worker | claudeopus46 | 24,095 | 12,981 | 37,076 | 3,015 | 21.9 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 13 | L1-worker | claudeopus46 | 24,095 | 19,486 | 43,581 | 2,088 | 16.6 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 14 | L1-worker | claudeopus46 | 2,320 | 2,219 | 4,539 | 924 | 5.2 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 15 | L1-worker | claudeopus46 | 627 | 2,099 | 2,726 | 859 | 5.3 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 16 | L1-worker | claudeopus46 | 366 | 1,361 | 1,727 | 879 | 4.7 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 17 | L1-worker | claudeopus46 | 2,106 | 3,631 | 5,737 | 1,218 | 11.7 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 18 | L1-worker | claudeopus46 | 366 | 1,995 | 2,361 | 733 | 4.1 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 19 | L1-worker | claudeopus46 | 1,228 | 4,945 | 6,173 | 737 | 4.3 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 20 | L1-worker | claudeopus46 | 787 | 17,863 | 18,650 | 449 | 5.2 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 21 | L0-main | claudeopus46 | 11,581 | 15,827 | 27,408 | 2,825 | 20.2 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 22 | L0-main | claudeopus46 | 2,106 | 3,514 | 5,620 | 653 | 5.2 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 23 | L0-main | claudeopus46 | 2,320 | 2,744 | 5,064 | 1,395 | 6.1 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 24 | L0-main | claudeopus46 | 366 | 1,202 | 1,568 | 803 | 4.1 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 25 | L0-main | claudeopus46 | 366 | 1,870 | 2,236 | 1,341 | 4.6 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 26 | L0-main | claudeopus46 | 560 | 3,495 | 4,055 | 129 | 2.4 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 27 | L0-main | claudeopus46 | 1,156 | 5,032 | 6,188 | 929 | 7.0 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 28 | verdict | claudeopus46 | 972 | 6,155 | 7,127 | 1,180 | 12.7 | Find viscosity data for the binary mixture of acetonitrile + (query_runs/run_4) |
| 1 | L0-main | claudeopus46 | 11,581 | 920 | 12,501 | 1,415 | 8.0 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,242 | 25,337 | 569 | 4.8 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,275 | 26,370 | 555 | 3.6 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 4 | L1-worker | claudeopus46 | 3,767 | 457 | 4,224 | 404 | 4.3 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,909 | 26,004 | 875 | 6.7 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,639 | 26,734 | 741 | 5.1 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 7 | L1-worker | claudeopus46 | 3,767 | 7,752 | 11,519 | 1,734 | 14.6 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,587 | 27,682 | 908 | 7.2 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,346 | 28,441 | 625 | 5.4 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 10 | L1-worker | claudeopus46 | 24,095 | 6,447 | 30,542 | 821 | 7.3 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 11 | L1-worker | claudeopus46 | 24,095 | 8,187 | 32,282 | 3,057 | 22.5 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 12 | L1-worker | claudeopus46 | 24,095 | 16,172 | 40,267 | 4,178 | 36.4 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 13 | L1-worker | claudeopus46 | 24,095 | 24,478 | 48,573 | 3,889 | 30.2 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 14 | L1-worker | claudeopus46 | 2,320 | 3,019 | 5,339 | 991 | 6.1 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 15 | L1-worker | claudeopus46 | 627 | 2,899 | 3,526 | 1,043 | 7.1 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 16 | L1-worker | claudeopus46 | 2,106 | 4,382 | 6,488 | 1,445 | 7.9 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 17 | L1-worker | claudeopus46 | 366 | 1,428 | 1,794 | 946 | 3.8 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 18 | L1-worker | claudeopus46 | 366 | 2,222 | 2,588 | 878 | 4.7 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 19 | L1-worker | claudeopus46 | 787 | 20,048 | 20,835 | 656 | 8.2 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 20 | L0-main | claudeopus46 | 11,581 | 19,957 | 31,538 | 3,672 | 23.5 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 21 | L0-main | claudeopus46 | 2,106 | 4,328 | 6,434 | 793 | 6.2 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 22 | L0-main | claudeopus46 | 2,320 | 3,576 | 5,896 | 1,158 | 6.6 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 23 | L0-main | claudeopus46 | 366 | 1,342 | 1,708 | 943 | 4.0 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 24 | L0-main | claudeopus46 | 366 | 1,633 | 1,999 | 1,109 | 4.3 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 25 | L0-main | claudeopus46 | 560 | 4,328 | 4,888 | 130 | 2.3 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 26 | L0-main | claudeopus46 | 1,156 | 5,834 | 6,990 | 868 | 6.6 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| 27 | verdict | claudeopus46 | 972 | 7,233 | 8,205 | 1,093 | 11.7 | Find viscosity data for the binary mixture of water + ethyle (query_runs/run_5) |
| **TOTAL** |  |  | **787,135** | **381,464** | **1,168,599** | **85,913** | **626.9** |  |
