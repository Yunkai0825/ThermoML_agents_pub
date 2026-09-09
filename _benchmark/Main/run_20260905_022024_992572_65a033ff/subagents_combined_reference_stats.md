# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 8 | 30,036 | 37,321 | 8,879 | 67,357 | 8,419 | 63.5 | claudeopus46 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| L1-worker | 21 | 303,612 | 117,833 | 25,368 | 421,445 | 20,068 | 192.9 | claudeopus46 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| verdict | 1 | 972 | 6,761 | 1,057 | 7,733 | 7,733 | 10.9 | claudeopus46 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| **TOTAL** | **30** | **334,620** | **161,915** | **35,304** | **496,535** | **36,220** | **267.3** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| **TOTAL** | **0** | **0** | **0** | **0** | **0** | **0** | **0** |  |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | --- | ---: | --- |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve global comp… | 264 | KEEP ←in 308 | 264 | 4.8 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 2 | 5 | `search_blocks` | compound=['GLOBcomp_15', 'GLOBcomp_18'], limit=50,… | 965 | KEEP ←in 4,801 | 965 | 13.4 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 3 | 6 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_7481… | 259 | — | — | 0.0 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 4 | 7 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_7481… | 375 | — | — | 0.4 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 5 | 8 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_7481… | 1,279 | — | — | 0.1 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 6 | 9 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_4124,… | 1,276 | — | — | 0.3 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 7 | 1 | `L1_query` | context=User wants specific experimen…, id_catalog… | 19,814 | — | — | 173.6 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| **TOTAL** | **38** |  |  | **24,232** |  | **1,229** | **192.6** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 11,581 | 970 | 12,551 | 1,485 | 8.4 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,372 | 25,467 | 660 | 5.5 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,461 | 26,556 | 624 | 4.2 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 4 | L1-worker | claudeopus46 | 3,767 | 520 | 4,287 | 438 | 4.7 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,084 | 26,179 | 1,315 | 9.7 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,931 | 27,026 | 924 | 7.0 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,699 | 27,794 | 795 | 5.8 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 8 | L1-worker | claudeopus46 | 3,767 | 5,349 | 9,116 | 1,551 | 12.8 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,223 | 28,318 | 1,126 | 11.0 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,865 | 28,960 | 629 | 6.8 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,548 | 29,643 | 833 | 7.3 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 12 | L1-worker | claudeopus46 | 24,095 | 7,160 | 31,255 | 1,230 | 11.9 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 13 | L1-worker | claudeopus46 | 24,095 | 8,797 | 32,892 | 3,001 | 24.0 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 14 | L1-worker | claudeopus46 | 24,095 | 14,860 | 38,955 | 2,671 | 20.4 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 15 | L1-worker | claudeopus46 | 24,095 | 20,593 | 44,688 | 2,323 | 18.7 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 16 | L1-worker | claudeopus46 | 2,320 | 2,454 | 4,774 | 1,022 | 6.8 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 17 | L1-worker | claudeopus46 | 627 | 2,334 | 2,961 | 1,056 | 7.4 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 18 | L1-worker | claudeopus46 | 2,106 | 3,947 | 6,053 | 1,454 | 7.8 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 19 | L1-worker | claudeopus46 | 366 | 1,459 | 1,825 | 982 | 4.8 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 20 | L1-worker | claudeopus46 | 366 | 1,467 | 1,833 | 1,043 | 4.7 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 21 | L1-worker | claudeopus46 | 366 | 2,231 | 2,597 | 1,095 | 5.0 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 22 | L1-worker | claudeopus46 | 787 | 19,479 | 20,266 | 596 | 6.6 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 23 | L0-main | claudeopus46 | 11,581 | 16,987 | 28,568 | 3,291 | 24.1 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 24 | L0-main | claudeopus46 | 2,320 | 3,232 | 5,552 | 850 | 6.3 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 25 | L0-main | claudeopus46 | 2,106 | 4,034 | 6,140 | 705 | 6.7 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 26 | L0-main | claudeopus46 | 366 | 1,254 | 1,620 | 669 | 3.6 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 27 | L0-main | claudeopus46 | 366 | 1,325 | 1,691 | 811 | 4.1 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 28 | L0-main | claudeopus46 | 560 | 3,999 | 4,559 | 185 | 2.7 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 29 | L0-main | claudeopus46 | 1,156 | 5,520 | 6,676 | 883 | 7.6 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
| 30 | verdict | claudeopus46 | 972 | 6,761 | 7,733 | 1,057 | 10.9 | Find experimental viscosity values for an equimolar (x=0.5)  (query_runs/run_2) |
