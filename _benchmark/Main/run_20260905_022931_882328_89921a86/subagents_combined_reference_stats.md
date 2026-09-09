# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 9 | 41,617 | 67,201 | 14,207 | 108,818 | 12,090 | 89.3 | claudeopus46 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| L1-worker | 34 | 444,995 | 196,154 | 40,470 | 641,149 | 18,857 | 277.8 | claudeopus46 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| verdict | 1 | 972 | 6,990 | 1,133 | 7,962 | 7,962 | 10.5 | claudeopus46 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| L0-main | 9 | 41,617 | 75,830 | 12,997 | 117,447 | 13,049 | 86.7 | claudeopus46 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| L1-worker | 46 | 642,587 | 368,033 | 53,286 | 1,010,620 | 21,970 | 384.5 | claudeopus46 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| verdict | 1 | 972 | 8,407 | 1,073 | 9,379 | 9,379 | 9.6 | claudeopus46 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| **TOTAL** | **100** | **1,172,760** | **722,615** | **123,166** | **1,895,375** | **83,307** | **858.4** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| `search_blocks` | 2 | 1 | 4 | 1 | 4 | 4 | 76 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| `resolve_property_ids` | 0 | 9 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| `search_id_alignment` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| `search_id_alignment` | 0 | 4 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 4 | 3 | 10 | 10 | 334 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| `resolve_property_ids` | 0 | 7 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| **TOTAL** | **8** | **23** | **8** | **4** | **14** | **14** | **410** |  |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | ---: | --- |
| Unique Compounds | 2 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| Unique References | 4 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| Unique Properties | 13 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| Unique Measurements | 3 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| Unique Phases | 1 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| Unique Variables | 4 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| Unique Constraints | 1 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| Unique parent blocks | 4 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| Explicit block/subsystem targets | 4 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| Subsystem targets | 0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| Target-matched data points | 76 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_5201 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_10699 |  | search_blocks |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | search_blocks |
| GLOBlit_11792 |  | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | resolve_property_ids, search_blocks |
| GLOBprop_40 |  | resolve_property_ids |
| GLOBprop_48 |  | resolve_property_ids |
| GLOBprop_98 |  | resolve_property_ids |
| GLOBprop_45 |  | resolve_property_ids |
| GLOBprop_107 |  | resolve_property_ids |
| GLOBprop_60 |  | resolve_property_ids |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_988 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks |
| GLOBphase_1 |  | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBsolvent_1 |  | search_blocks |
| Unique Compounds | 2 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| Unique References | 10 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| Unique Properties | 7 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| Unique Measurements | 6 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| Unique Phases | 1 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| Unique Variables | 4 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| Unique Constraints | 3 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| Unique Solvents | 1 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| Unique parent blocks | 10 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| Explicit block/subsystem targets | 10 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| Subsystem targets | 0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| Target-matched data points | 334 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| **TOTAL** | **500** |  |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | ---: | ---: | ---: | --- | --- | --- | --- |
| 10.1016/j.jct.2007.05.004 | PROPblock_9 | declared | 39 | binary | — | search_blocks | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 10.1016/j.jct.2019.05.013 | PROPblock_3 | declared | 12 | binary | — | search_blocks | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 10.1021/je0600810 | PROPblock_3 | declared | 9 | binary | — | search_blocks | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 10.1021/je2003622 | PROPblock_1 | declared | 16 | binary | — | search_blocks | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 10.1016/j.jct.2007.05.004 | 1 | 37 | binary | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |  |  |
| 10.1016/j.jct.2018.02.022 | 1 | 100 | binary | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |  |  |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |  |  |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |  |  |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |  |  |
| 10.1021/je4003515 | 1 | 25 | binary | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |  |  |
| 10.1021/je600565m | 1 | 17 | binary | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |  |  |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |  |  |
| 10.1021/je800150h | 1 | 108 | binary | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |  |  |
| 10.1021/je900743e | 1 | 15 | binary | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |  |  |
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | — | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 10.1016/j.jct.2018.02.022 | PROPblock_21 | declared | 100 | binary | — | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 10.1021/acs.jced.7b00299 | PROPblock_11 | declared | 2 | binary | — | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | declared | 6 | binary | — | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 10.1021/acs.jced.8b00939 | PROPblock_18 | declared | 9 | binary | — | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 10.1021/je4003515 | PROPblock_8 | declared | 25 | binary | — | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 10.1021/je600565m | PROPblock_5 | declared | 17 | binary | — | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 10.1021/je700618y | PROPblock_7 | declared | 15 | binary | — | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 10.1021/je800150h | PROPblock_8 | declared | 108 | binary | — | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 10.1021/je900743e | PROPblock_2 | declared | 15 | binary | — | search_blocks | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| **TOTAL** | **10** | **334** | **410** |  |  |  |  |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | ---: | ---: | --- |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 175 | KEEP ←in 277 | 175 | 4.1 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=20, p… | 1,117 | KEEP ←in 8,146 | 1102 | 22.6 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 3 | 5 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_9, nearest=x(… | 270 | — | — | 0.1 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 4 | 6 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_9, nearest={'… | 365 | — | — | 0.1 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 5 | 7 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_9, nearest={'… | 1,269 | — | — | 0.1 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 6 | 1 | `L1_query` | context=Looking for dynamic viscosity…, id_catalog… | 28,868 | — | — | 164.0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 7 | 2 | `resolve_property_ids` | limit=20, min_score=40, purpose=Find property IDs … | 943 | DISCARD ←in 982 | 878 | 10.2 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 8 | 3 | `search_id_alignment` | entity_type=property, limit=20, purpose=Find any v… | 741 | KEEP ←in 277 | 741 | 9.5 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 9 | 4 | `search_id_alignment` | entity_type=property, limit=20, purpose=Find any e… | 631 | KEEP ←in 627 | 631 | 6.0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 10 | 5 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=10, p… | 731 | DISCARD ←in 39 | 673 | 12.8 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 11 | 2 | `L1_query` | context=Already found dynamic viscosi…, id_catalog… | 3,356 | — | — | 111.9 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve ethanol and… | 213 | KEEP ←in 278 | 213 | 4.0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=20, p… | 1,258 | KEEP ←in 6,284 | 1258 | 20.0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2825… | 262 | — | — | 0.0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2825… | 365 | — | — | 0.1 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_2825… | 1,214 | — | — | 0.1 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 6 | 8 | `inspect_block_table` | block_number=PROPblock_21, literature=GLOBlit_5201… | 1,233 | — | — | 0.2 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 7 | 9 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=10, p… | 1,091 | DISCARD ←in 39 | 1033 | 18.0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 8 | 11 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_11, nearest={… | 1,004 | — | — | 0.8 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 9 | 1 | `L1_query` | context=Property IDs: GLOBprop_4 = dy…, id_catalog… | 21,495 | — | — | 234.4 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 10 | 2 | `resolve_property_ids` | limit=20, min_score=40, purpose=Find property IDs … | 874 | KEEP ←in 801 | 874 | 11.2 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 11 | 3 | `search_id_alignment` | entity_type=property, limit=20, purpose=Find any e… | 772 | DISCARD ←in 84 | 708 | 7.2 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 12 | 4 | `search_id_alignment` | entity_type=property, limit=20, purpose=Find all v… | 277 | KEEP ←in 271 | 277 | 4.4 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 13 | 5 | `search_id_alignment` | entity_type=property, limit=30, purpose=Find all e… | 838 | KEEP ←in 627 | 838 | 6.6 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 14 | 7 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_21, nearest=x… | 264 | — | — | 0.0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 15 | 8 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_21, nearest={… | 376 | — | — | 0.2 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 16 | 9 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_21, nearest={… | 1,286 | — | — | 0.1 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 17 | 11 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_11, nearest={… | 1,057 | — | — | 0.1 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 18 | 2 | `L1_query` | context=We already found dynamic visc…, id_catalog… | 6,798 | — | — | 133.8 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| **TOTAL** | **145** |  |  | **79,143** |  | **9,401** | **782.6** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 11,581 | 901 | 12,482 | 1,516 | 9.4 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,347 | 25,442 | 540 | 4.6 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,354 | 26,449 | 522 | 3.7 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 4 | L1-worker | claudeopus46 | 3,767 | 427 | 4,194 | 305 | 4.0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,950 | 26,045 | 924 | 8.4 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,679 | 26,774 | 700 | 4.7 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 7 | L1-worker | claudeopus46 | 3,767 | 8,603 | 12,370 | 1,662 | 15.3 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,760 | 27,855 | 1,072 | 8.9 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,402 | 28,497 | 697 | 6.1 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,099 | 29,194 | 836 | 7.0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,686 | 30,781 | 2,291 | 18.1 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 12 | L1-worker | claudeopus46 | 24,095 | 11,576 | 35,671 | 4,596 | 28.3 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 13 | L1-worker | claudeopus46 | 24,095 | 18,362 | 42,457 | 4,005 | 24.4 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 14 | L1-worker | claudeopus46 | 2,320 | 2,187 | 4,507 | 825 | 5.3 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 15 | L1-worker | claudeopus46 | 627 | 2,067 | 2,694 | 855 | 5.3 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 16 | L1-worker | claudeopus46 | 2,106 | 3,655 | 5,761 | 1,811 | 8.1 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 17 | L1-worker | claudeopus46 | 366 | 1,262 | 1,628 | 790 | 3.5 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 18 | L1-worker | claudeopus46 | 366 | 2,588 | 2,954 | 1,332 | 5.5 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 19 | L1-worker | claudeopus46 | 787 | 29,170 | 29,957 | 640 | 7.0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 20 | L0-main | claudeopus46 | 11,581 | 16,723 | 28,304 | 2,522 | 18.4 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 21 | L1-worker | claudeopus46 | 24,095 | 7,205 | 31,300 | 976 | 6.1 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 22 | L1-worker | claudeopus46 | 24,095 | 8,366 | 32,461 | 740 | 4.4 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 23 | L1-worker | claudeopus46 | 3,767 | 1,212 | 4,979 | 1,437 | 9.4 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 24 | L1-worker | claudeopus46 | 24,095 | 8,641 | 32,736 | 958 | 7.0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 25 | L1-worker | claudeopus46 | 3,767 | 526 | 4,293 | 1,390 | 9.1 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 26 | L1-worker | claudeopus46 | 24,095 | 9,734 | 33,829 | 849 | 11.5 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 27 | L1-worker | claudeopus46 | 3,767 | 830 | 4,597 | 1,000 | 5.8 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 28 | L1-worker | claudeopus46 | 24,095 | 10,774 | 34,869 | 1,061 | 7.0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 29 | L1-worker | claudeopus46 | 3,767 | 512 | 4,279 | 857 | 6.5 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 30 | L1-worker | claudeopus46 | 24,095 | 11,929 | 36,024 | 2,096 | 12.7 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 31 | L1-worker | claudeopus46 | 24,095 | 15,991 | 40,086 | 2,371 | 13.1 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 32 | L1-worker | claudeopus46 | 2,106 | 3,368 | 5,474 | 92 | 2.0 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 33 | L1-worker | claudeopus46 | 627 | 1,532 | 2,159 | 846 | 3.7 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 34 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.2 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 35 | L1-worker | claudeopus46 | 2,320 | 1,652 | 3,972 | 807 | 4.7 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 36 | L1-worker | claudeopus46 | 787 | 4,839 | 5,626 | 520 | 4.4 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 37 | L0-main | claudeopus46 | 11,581 | 23,918 | 35,499 | 4,399 | 27.2 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 38 | L0-main | claudeopus46 | 2,320 | 4,091 | 6,411 | 1,087 | 6.2 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 39 | L0-main | claudeopus46 | 2,106 | 4,824 | 6,930 | 997 | 6.6 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 40 | L0-main | claudeopus46 | 366 | 1,562 | 1,928 | 1,043 | 4.3 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 41 | L0-main | claudeopus46 | 366 | 1,546 | 1,912 | 967 | 4.3 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 42 | L0-main | claudeopus46 | 560 | 5,414 | 5,974 | 341 | 3.3 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 43 | L0-main | claudeopus46 | 1,156 | 8,222 | 9,378 | 1,335 | 9.6 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 44 | verdict | claudeopus46 | 972 | 6,990 | 7,962 | 1,133 | 10.5 | Find viscosity data for methanol + water binary mixture at a (query_runs/run_4) |
| 1 | L0-main | claudeopus46 | 11,581 | 992 | 12,573 | 1,527 | 9.5 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,304 | 25,399 | 535 | 4.9 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,352 | 26,447 | 563 | 4.1 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 4 | L1-worker | claudeopus46 | 3,767 | 470 | 4,237 | 375 | 3.9 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,947 | 26,042 | 996 | 7.9 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,703 | 26,798 | 738 | 6.3 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 7 | L1-worker | claudeopus46 | 3,767 | 6,734 | 10,501 | 1,562 | 14.7 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,985 | 28,080 | 1,192 | 8.7 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,682 | 28,777 | 714 | 5.2 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,397 | 29,492 | 1,213 | 9.2 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,964 | 31,059 | 988 | 7.9 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 12 | L1-worker | claudeopus46 | 24,095 | 8,637 | 32,732 | 1,198 | 9.9 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 13 | L1-worker | claudeopus46 | 3,767 | 514 | 4,281 | 1,550 | 10.2 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 14 | L1-worker | claudeopus46 | 24,095 | 10,132 | 34,227 | 3,661 | 26.1 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 15 | L1-worker | claudeopus46 | 24,095 | 18,608 | 42,703 | 3,582 | 27.6 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 16 | L1-worker | claudeopus46 | 24,095 | 20,095 | 44,190 | 3,383 | 24.4 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 17 | L1-worker | claudeopus46 | 24,062 | 26,005 | 50,067 | 3,585 | 25.2 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 18 | L1-worker | claudeopus46 | 2,320 | 3,716 | 6,036 | 905 | 5.9 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 19 | L1-worker | claudeopus46 | 2,106 | 5,141 | 7,247 | 1,469 | 8.0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 20 | L1-worker | claudeopus46 | 627 | 3,596 | 4,223 | 1,107 | 8.4 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 21 | L1-worker | claudeopus46 | 366 | 1,342 | 1,708 | 865 | 4.3 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 22 | L1-worker | claudeopus46 | 366 | 1,518 | 1,884 | 1,094 | 4.7 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 23 | L1-worker | claudeopus46 | 366 | 2,246 | 2,612 | 1,136 | 5.3 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 24 | L1-worker | claudeopus46 | 787 | 21,693 | 22,480 | 709 | 7.5 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 25 | L0-main | claudeopus46 | 11,581 | 19,821 | 31,402 | 1,714 | 13.4 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 26 | L1-worker | claudeopus46 | 24,095 | 9,169 | 33,264 | 836 | 5.9 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 27 | L1-worker | claudeopus46 | 24,095 | 10,285 | 34,380 | 682 | 4.1 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 28 | L1-worker | claudeopus46 | 3,767 | 989 | 4,756 | 1,729 | 11.0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 29 | L1-worker | claudeopus46 | 24,095 | 10,523 | 34,618 | 965 | 6.9 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 30 | L1-worker | claudeopus46 | 3,767 | 379 | 4,146 | 948 | 6.9 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 31 | L1-worker | claudeopus46 | 24,095 | 11,670 | 35,765 | 739 | 4.6 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 32 | L1-worker | claudeopus46 | 3,767 | 435 | 4,202 | 441 | 4.3 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 33 | L1-worker | claudeopus46 | 24,095 | 12,268 | 36,363 | 651 | 4.8 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 34 | L1-worker | claudeopus46 | 3,767 | 850 | 4,617 | 1,197 | 6.5 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 35 | L1-worker | claudeopus46 | 24,095 | 13,413 | 37,508 | 1,895 | 14.6 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 36 | L1-worker | claudeopus46 | 24,095 | 17,789 | 41,884 | 637 | 6.0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 37 | L1-worker | claudeopus46 | 24,095 | 18,376 | 42,471 | 568 | 6.7 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 38 | L1-worker | claudeopus46 | 24,095 | 19,037 | 43,132 | 627 | 5.8 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 39 | L1-worker | claudeopus46 | 24,095 | 20,618 | 44,713 | 485 | 4.7 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 40 | L1-worker | claudeopus46 | 24,095 | 21,668 | 45,763 | 632 | 4.9 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 41 | L1-worker | claudeopus46 | 24,095 | 22,163 | 46,258 | 2,093 | 16.6 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 42 | L1-worker | claudeopus46 | 2,106 | 3,953 | 6,059 | 353 | 3.3 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 43 | L1-worker | claudeopus46 | 2,320 | 2,224 | 4,544 | 849 | 4.5 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 44 | L1-worker | claudeopus46 | 366 | 1,130 | 1,496 | 80 | 2.1 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 45 | L1-worker | claudeopus46 | 627 | 2,104 | 2,731 | 1,185 | 6.5 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 46 | L1-worker | claudeopus46 | 366 | 1,286 | 1,652 | 814 | 3.9 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 47 | L1-worker | claudeopus46 | 366 | 1,596 | 1,962 | 1,172 | 4.8 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 48 | L1-worker | claudeopus46 | 787 | 6,327 | 7,114 | 588 | 4.8 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 49 | L0-main | claudeopus46 | 11,581 | 30,646 | 42,227 | 4,472 | 30.3 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 50 | L0-main | claudeopus46 | 2,106 | 5,167 | 7,273 | 951 | 6.2 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 51 | L0-main | claudeopus46 | 2,320 | 4,343 | 6,663 | 1,106 | 8.3 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 52 | L0-main | claudeopus46 | 366 | 1,500 | 1,866 | 1,013 | 4.6 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 53 | L0-main | claudeopus46 | 366 | 1,581 | 1,947 | 1,062 | 4.7 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 54 | L0-main | claudeopus46 | 560 | 5,210 | 5,770 | 187 | 2.7 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 55 | L0-main | claudeopus46 | 1,156 | 6,570 | 7,726 | 965 | 7.0 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| 56 | verdict | claudeopus46 | 972 | 8,407 | 9,379 | 1,073 | 9.6 | Find viscosity data for ethanol + water binary mixture at ap (query_runs/run_3) |
| **TOTAL** |  |  | **1,172,760** | **722,615** | **1,895,375** | **123,166** | **858.4** |  |
