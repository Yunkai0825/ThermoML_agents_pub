# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 8 | 30,036 | 28,268 | 7,701 | 58,304 | 7,288 | 51.1 | claudeopus46 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| L1-worker | 16 | 206,866 | 66,104 | 17,053 | 272,970 | 17,060 | 125.8 | claudeopus46 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| verdict | 1 | 972 | 5,385 | 1,056 | 6,357 | 6,357 | 8.6 | claudeopus46 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| **TOTAL** | **25** | **237,874** | **99,757** | **25,810** | **337,631** | **30,705** | **185.5** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 12 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| **TOTAL** | **4** | **1** | **2** | **1** | **1** | **1** | **12** |  |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBcomp_6 |  | resolve_compound_ids, search_blocks | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBlit_5585 |  | search_blocks | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBphase_1 |  | search_blocks | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBvar_1 | Temperature, K | search_blocks | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| GLOBvar_5 | Mass fraction | search_blocks | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBconstr_1 | Pressure, kPa | search_blocks | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | ---: | --- |
| Unique Compounds | 2 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| Unique References | 1 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| Unique Properties | 1 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| Unique Measurements | 1 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| Unique Phases | 1 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| Unique Variables | 2 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| Unique Constraints | 1 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| Unique parent blocks | 1 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| Explicit block/subsystem targets | 1 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| Subsystem targets | 0 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| Target-matched data points | 12 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| **TOTAL** | **23** |  |


## 3. DOI & Block References

| DOI | Blocks | Datapoints | System types | Source tools | Source |
| --- | ---: | ---: | --- | --- | --- |
| 10.1016/j.jct.2019.105880 | 1 | 12 | binary | search_blocks | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 10.1016/j.jct.2019.105880 | PROPblock_12 | declared | 12 | binary | — | search_blocks | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | ---: | ---: | --- |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 200 | KEEP ←in 285 | 200 | 4.6 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_6', 'GLOBcomp_1'], limit=50, p… | 1,163 | KEEP ←in 2,041 | 1145 | 18.5 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_12, literature=GLOBlit_5585… | 1,127 | — | — | 0.1 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 4 | 1 | `L1_query` | context=User is looking for viscosity…, id_catalog… | 11,648 | — | — | 118.4 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| **TOTAL** | **12** |  |  | **14,138** |  | **1,345** | **141.6** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 11,581 | 937 | 12,518 | 1,439 | 9.0 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,216 | 25,311 | 675 | 5.5 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,264 | 26,359 | 565 | 4.0 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 4 | L1-worker | claudeopus46 | 3,767 | 474 | 4,241 | 367 | 4.5 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,846 | 25,941 | 1,057 | 7.1 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,632 | 26,727 | 627 | 4.5 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 7 | L1-worker | claudeopus46 | 3,767 | 2,533 | 6,300 | 1,571 | 11.7 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,748 | 27,843 | 868 | 7.0 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 9 | L1-worker | claudeopus46 | 24,095 | 5,243 | 29,338 | 1,639 | 13.5 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 10 | L1-worker | claudeopus46 | 24,095 | 9,337 | 33,432 | 2,635 | 16.5 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 11 | L1-worker | claudeopus46 | 24,095 | 15,391 | 39,486 | 2,313 | 17.7 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 12 | L1-worker | claudeopus46 | 2,106 | 3,184 | 5,290 | 848 | 5.6 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 13 | L1-worker | claudeopus46 | 2,320 | 1,847 | 4,167 | 988 | 6.4 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 14 | L1-worker | claudeopus46 | 627 | 1,727 | 2,354 | 858 | 6.7 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 15 | L1-worker | claudeopus46 | 366 | 1,625 | 1,991 | 500 | 3.5 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 16 | L1-worker | claudeopus46 | 366 | 1,425 | 1,791 | 948 | 4.2 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 17 | L1-worker | claudeopus46 | 787 | 11,612 | 12,399 | 594 | 7.4 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 18 | L0-main | claudeopus46 | 11,581 | 12,327 | 23,908 | 2,576 | 16.0 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 19 | L0-main | claudeopus46 | 2,320 | 2,478 | 4,798 | 881 | 5.4 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 20 | L0-main | claudeopus46 | 2,106 | 3,247 | 5,353 | 660 | 5.6 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 21 | L0-main | claudeopus46 | 366 | 1,356 | 1,722 | 837 | 4.3 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 22 | L0-main | claudeopus46 | 366 | 1,209 | 1,575 | 729 | 4.7 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 23 | L0-main | claudeopus46 | 560 | 2,952 | 3,512 | 72 | 2.2 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 24 | L0-main | claudeopus46 | 1,156 | 3,762 | 4,918 | 507 | 3.9 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
| 25 | verdict | claudeopus46 | 972 | 5,385 | 6,357 | 1,056 | 8.6 | Find viscosity data for isopropanol (2-propanol) mixed with  (query_runs/run_10) |
