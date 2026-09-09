# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 8 | 30,036 | 24,191 | 6,660 | 54,227 | 6,778 | 46.0 | claudeopus46 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| L1-worker | 19 | 258,823 | 93,827 | 20,635 | 352,650 | 18,560 | 154.1 | claudeopus46 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| verdict | 1 | 972 | 4,170 | 1,027 | 5,142 | 5,142 | 10.0 | claudeopus46 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| **TOTAL** | **28** | **289,831** | **122,188** | **28,322** | **412,019** | **30,480** | **210.1** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `search_blocks` | 2 | 1 | 5 | 3 | 20 | 20 | 2,392 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| `resolve_ids` | 0 | 0 | 2 | 0 | 0 | 0 | 0 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| `search_blocks` | 2 | 1 | 5 | 3 | 10 | 10 | 1,929 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| **TOTAL** | **4** | **2** | **12** | **6** | **30** | **30** | **4,321** |  |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBlit_220 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_1483 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_2432 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_2825 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_3475 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_4415 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_5201 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_5473 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_7085 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_7178 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_7448 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_7676 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_8050 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_8888 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_9006 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_10159 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_10699 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_10866 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_11005 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBlit_11136 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBcomp_2 | ethanol | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBcomp_1 | water | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBmeas_236 | Mass density, kg/m3 | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBmeas_203 | Mass density, kg/m3 | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBmeas_212 | Mass density, kg/m3 | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBphase_1 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBvar_1 | Temperature, K | resolve_ids, search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBvar_3 | Pressure, kPa | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBvar_2 | Mole fraction | resolve_ids, search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBvar_4 | Molality, mol/kg | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBvar_5 | Mass fraction | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBsolvent_1 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBsolvent_2 |  | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBconstr_1 | Pressure, kPa | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBconstr_2 | Temperature, K | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| GLOBconstr_8 | Molality, mol/kg | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | ---: | --- |
| Unique References | 20 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| Unique Compounds | 2 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| Unique Properties | 1 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| Unique Measurements | 7 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| Unique Phases | 1 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| Unique Variables | 5 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| Unique Solvents | 2 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| Unique Constraints | 3 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| Unique parent blocks | 20 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| Explicit block/subsystem targets | 20 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| Subsystem targets | 0 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| Target-matched data points | 4,321 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| **TOTAL** | **4,402** |  |


## 3. DOI & Block References

| DOI | Blocks | Datapoints | System types | Source tools | Source |
| --- | ---: | ---: | --- | --- | --- |
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1016/j.jct.2004.07.019 | 1 | 565 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1016/j.jct.2007.05.004 | 1 | 37 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1016/j.jct.2015.06.024 | 1 | 40 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1016/j.jct.2018.02.022 | 1 | 244 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je020173z | 1 | 24 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je060335h | 1 | 164 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je4003515 | 1 | 23 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je600565m | 1 | 18 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je800150h | 1 | 108 | binary | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | — | search_blocks | Find experimental density (mass density) data for the binary (query_runs/run_1) |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | ---: | ---: | --- |
| 1 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=20, p… | 544 | KEEP ←in 12,879 | 544 | 21.6 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 2 | 3 | `resolve_ids` | entity_type=variable, limit=5, min_score=70, purpo… | 227 | KEEP ←in 320 | 227 | 5.0 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 3 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=10, p… | 1,215 | KEEP ←in 6,665 | 1215 | 19.3 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_220, … | 254 | — | — | 0.0 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_220, … | 376 | — | — | 0.2 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 6 | 8 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_220, … | 1,237 | — | — | 0.1 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 7 | 1 | `L1_query` | context=User wants experimental densi…, id_catalog… | 10,457 | — | — | 155.3 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| **TOTAL** | **32** |  |  | **14,310** |  | **1,986** | **201.5** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 11,581 | 1,101 | 12,682 | 1,330 | 8.2 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,301 | 25,396 | 1,204 | 10.3 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 3 | L1-worker | claudeopus46 | 24,095 | 1,986 | 26,081 | 653 | 5.1 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 4 | L1-worker | claudeopus46 | 3,767 | 13,361 | 17,128 | 1,800 | 16.2 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,678 | 26,773 | 1,046 | 8.1 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 6 | L1-worker | claudeopus46 | 3,767 | 514 | 4,281 | 363 | 4.9 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,437 | 27,532 | 1,497 | 11.2 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 8 | L1-worker | claudeopus46 | 24,095 | 4,376 | 28,471 | 1,989 | 13.2 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 9 | L1-worker | claudeopus46 | 3,767 | 7,100 | 10,867 | 1,507 | 14.0 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,633 | 29,728 | 1,052 | 8.6 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,405 | 30,500 | 638 | 4.9 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 12 | L1-worker | claudeopus46 | 24,095 | 7,289 | 31,384 | 837 | 7.8 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 13 | L1-worker | claudeopus46 | 24,095 | 9,054 | 33,149 | 1,321 | 8.7 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 14 | L1-worker | claudeopus46 | 24,095 | 12,400 | 36,495 | 2,949 | 14.8 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 15 | L1-worker | claudeopus46 | 2,106 | 2,848 | 4,954 | 500 | 3.6 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 16 | L1-worker | claudeopus46 | 627 | 1,306 | 1,933 | 797 | 4.5 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 17 | L1-worker | claudeopus46 | 2,320 | 1,426 | 3,746 | 778 | 4.6 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 18 | L1-worker | claudeopus46 | 366 | 1,277 | 1,643 | 488 | 3.0 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 19 | L1-worker | claudeopus46 | 366 | 1,215 | 1,581 | 738 | 3.6 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 20 | L1-worker | claudeopus46 | 787 | 10,221 | 11,008 | 478 | 7.0 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 21 | L0-main | claudeopus46 | 11,581 | 10,736 | 22,317 | 2,325 | 16.0 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 22 | L0-main | claudeopus46 | 2,320 | 1,856 | 4,176 | 653 | 4.3 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 23 | L0-main | claudeopus46 | 2,106 | 2,789 | 4,895 | 558 | 4.5 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 24 | L0-main | claudeopus46 | 366 | 1,107 | 1,473 | 519 | 2.9 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 25 | L0-main | claudeopus46 | 366 | 1,128 | 1,494 | 641 | 3.4 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 26 | L0-main | claudeopus46 | 560 | 2,338 | 2,898 | 106 | 2.0 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 27 | L0-main | claudeopus46 | 1,156 | 3,136 | 4,292 | 528 | 4.7 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
| 28 | verdict | claudeopus46 | 972 | 4,170 | 5,142 | 1,027 | 10.0 | Find experimental density (mass density) data for the binary (query_runs/run_1) |
