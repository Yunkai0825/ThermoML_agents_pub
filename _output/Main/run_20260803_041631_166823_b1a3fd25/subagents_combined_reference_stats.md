# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 5 | 22,187 | 38,106 | 11,196 | 60,293 | 12,058 | 62.6 | claudeopus46 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| L1-worker | 13 | 76,514 | 58,343 | 16,935 | 134,857 | 10,373 | 111.0 | claudeopus46 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| L0-main | 6 | 22,485 | 325,740 | 36,287 | 348,225 | 58,037 | 173.4 | claudeopus46 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| L1-worker | 56 | 348,285 | 3,004,684 | 153,366 | 3,352,969 | 59,874 | 883.4 | claudeopus46 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| L0-main | 8 | 41,695 | 249,772 | 42,000 | 291,467 | 36,433 | 214.7 | claudeopus46 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| L1-worker | 70 | 435,869 | 1,557,124 | 118,610 | 1,992,993 | 28,471 | 739.0 | claudeopus46 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| L0-main | 8 | 50,969 | 95,687 | 39,810 | 146,656 | 18,332 | 181.5 | claudeopus46 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| L1-worker | 98 | 745,427 | 1,169,866 | 136,422 | 1,915,293 | 19,543 | 995.0 | claudeopus46 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| **TOTAL** | **264** | **1,743,431** | **6,499,322** | **554,626** | **8,242,753** | **243,121** | **3,360.6** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| `search_blocks` | 4 | 2 | 2 | 2 | 3 | 3 | 94 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| `search_system_summary` | 4 | 0 | 0 | 0 | 3 | 3 | 94 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| `search_blocks` | 2 | 1 | 6 | 3 | 14 | 14 | 534 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 6 | 5 | 27 | 29 | 2,895 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 2 | 2 | 3 | 3 | 18 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 1 | 3 | 1 | 1 | 6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 5 | 1 | 6 | 6 | 232 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 7 | 3 | 17 | 18 | 1,610 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 3 | 1 | 2 | 2 | 240 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 5 | 1 | 6 | 6 | 232 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 7 | 3 | 17 | 18 | 1,610 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 3 | 1 | 2 | 2 | 240 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 3 | 2 | 7 | 7 | 302 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 4 | 3 | 16 | 16 | 908 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 3 | 1 | 4 | 4 | 125 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 135 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_system_summary` | 2 | 0 | 0 | 0 | 16 | 29 | 1,601 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 2 | 4 | 2 | 9 | 12 | 655 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| `search_blocks` | 2 | 13 | 5 | 3 | 16 | 29 | 1,601 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 2 | 1 | 4 | 2 | 9 | 9 | 484 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 2 | 1 | 3 | 1 | 3 | 3 | 171 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 2 | 1 | 2 | 0 | 1 | 1 | 112 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 2 | 1 | 4 | 2 | 9 | 9 | 484 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 2 | 1 | 3 | 1 | 3 | 3 | 171 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 2 | 1 | 2 | 0 | 1 | 1 | 112 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 6 | 1 | 5 | 2 | 3 | 7 | 677 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| `memory_catalog_add` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `memory_catalog_add` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `memory_catalog_add` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `memory_catalog_add` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `memory_catalog_add` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 76 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 2 | 0 | 1 | 1 | 60 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_system_registry` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 76 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 2 | 0 | 1 | 1 | 60 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_system_registry` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_system_registry` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 16 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 20 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 136 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 296 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_system_registry` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_blocks` | 14 | 1 | 7 | 4 | 11 | 19 | 1,060 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| `search_system_registry` | 50 | 1 | 11 | 6 | 15 | 50 | 4,312 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| **TOTAL** | **156** | **57** | **157** | **77** | **321** | **401** | **30,103** |  |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | --- | --- |
| Unique References | 3 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| Unique Compounds | 4 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| Unique Properties | 2 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| Unique Measurements | 2 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| Unique Phases | 1 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| Unique Solvents | 1 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| Unique Variables | 2 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| Unique Constraints | 2 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| Unique parent blocks | 3 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| Explicit block/subsystem targets | 3 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| Subsystem targets | 0 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| Target-matched data points | 94 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| GLOBlit_1742 |  | search_blocks |
| GLOBlit_2092 |  | search_blocks |
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_5201 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_8949 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_10699 |  | search_blocks |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | search_blocks |
| GLOBlit_11459 |  | search_blocks |
| GLOBlit_11792 |  | search_blocks |
| GLOBlit_220 |  | search_blocks |
| GLOBlit_1483 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_2732 |  | search_blocks |
| GLOBlit_3475 |  | search_blocks |
| GLOBlit_4415 |  | search_blocks |
| GLOBlit_5473 |  | search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_7629 |  | search_blocks |
| GLOBlit_8050 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9006 |  | search_blocks |
| GLOBlit_10866 |  | search_blocks |
| GLOBlit_11504 |  | search_blocks |
| GLOBlit_6628 |  | search_blocks |
| GLOBlit_7794 |  | search_blocks |
| GLOBlit_7483 |  | search_blocks |
| GLOBlit_5533 |  | search_blocks |
| GLOBlit_8869 |  | search_blocks |
| GLOBlit_9571 |  | search_blocks |
| GLOBlit_385 |  | search_blocks |
| GLOBlit_462 |  | search_blocks |
| GLOBlit_895 |  | search_blocks |
| GLOBlit_8155 |  | search_blocks |
| GLOBlit_8254 |  | search_blocks |
| GLOBlit_8424 |  | search_blocks |
| GLOBlit_2395 |  | search_blocks |
| GLOBlit_2656 |  | search_blocks |
| GLOBlit_6951 |  | search_blocks |
| GLOBlit_8038 |  | search_blocks |
| GLOBlit_8106 |  | search_blocks |
| GLOBlit_11186 |  | search_blocks |
| GLOBlit_11506 |  | search_blocks |
| GLOBlit_1223 |  | search_blocks |
| GLOBlit_2268 |  | search_blocks |
| GLOBlit_2831 |  | search_blocks |
| GLOBlit_5254 |  | search_blocks |
| GLOBlit_5274 |  | search_blocks |
| GLOBlit_6630 |  | search_blocks |
| GLOBlit_6686 |  | search_blocks |
| GLOBlit_7228 |  | search_blocks |
| GLOBlit_7440 |  | search_blocks |
| GLOBlit_10102 |  | search_blocks |
| GLOBlit_3286 |  | search_blocks |
| GLOBlit_4021 |  | search_blocks |
| GLOBlit_8553 |  | search_blocks |
| GLOBlit_1283 |  | search_blocks |
| GLOBlit_10109 |  | search_system_summary |
| GLOBlit_2844 |  | search_blocks, search_system_summary |
| GLOBlit_2781 |  | search_blocks, search_system_summary |
| GLOBlit_10766 |  | search_system_summary |
| GLOBlit_2584 |  | search_blocks, search_system_summary |
| GLOBlit_2842 |  | search_blocks, search_system_summary |
| GLOBlit_11018 |  | search_blocks, search_system_summary |
| GLOBlit_11517 |  | search_blocks, search_system_summary |
| GLOBlit_10024 |  | search_system_summary |
| GLOBlit_5953 |  | search_blocks, search_system_summary |
| GLOBlit_10215 |  | search_system_summary |
| GLOBlit_663 |  | search_system_summary |
| GLOBlit_2652 |  | search_blocks, search_system_summary |
| GLOBlit_7713 |  | search_blocks, search_system_summary |
| GLOBlit_9547 |  | search_system_summary |
| GLOBlit_5958 |  | search_system_summary |
| GLOBcomp_2 | ethanol | search_blocks |
| GLOBcomp_1 | water | search_blocks, search_system_summary |
| GLOBcomp_4 | methanol | search_blocks |
| GLOBcomp_24 | 1,2-ethanediol | search_blocks |
| GLOBcomp_31 |  | search_blocks, search_system_summary |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBprop_18 | Electrical conductivity, S/m | search_blocks |
| GLOBprop_28 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_988 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_1497 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_236 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_203 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_212 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_36 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_19 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_14 | Electrical conductivity, S/m | search_blocks |
| GLOBmeas_2135 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_271 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_1494 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_280 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_29 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_207 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_227 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_143 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_184 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_192 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_569 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_147 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_495 | Mass density, kg/m3 | search_blocks |
| GLOBphase_1 |  | search_blocks |
| GLOBphase_3 |  | search_blocks |
| GLOBphase_10 |  | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_18 | Volume fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_15 | Mass ratio of solute to solvent | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_22 | Volume fraction | search_blocks |
| GLOBconstr_5 | Mass fraction | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_2 |  | search_blocks |
| GLOBsolvent_3 |  | search_blocks |
| GLOBsolvent_12 |  | search_blocks |
| Unique References | 77 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| Unique Compounds | 5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| Unique Properties | 5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| Unique Measurements | 36 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| Unique Phases | 3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| Unique Variables | 7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| Unique Constraints | 7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| Unique Solvents | 4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| Unique parent blocks | 113 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| Explicit block/subsystem targets | 113 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| Subsystem targets | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| Target-matched data points | 9,742 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| GLOBlit_663 |  | search_blocks |
| GLOBlit_2584 |  | search_blocks |
| GLOBlit_2652 |  | search_blocks |
| GLOBlit_2781 |  | search_blocks |
| GLOBlit_2842 |  | search_blocks |
| GLOBlit_2844 |  | search_blocks |
| GLOBlit_5953 |  | search_blocks |
| GLOBlit_5958 |  | search_blocks |
| GLOBlit_7713 |  | search_blocks |
| GLOBlit_9547 |  | search_blocks |
| GLOBlit_10024 |  | search_blocks |
| GLOBlit_10109 |  | search_blocks |
| GLOBlit_10215 |  | search_blocks |
| GLOBlit_10766 |  | search_blocks |
| GLOBlit_11018 |  | search_blocks |
| GLOBlit_11517 |  | search_blocks |
| GLOBlit_7523 |  | search_blocks |
| GLOBlit_9178 |  | search_blocks |
| GLOBlit_10194 |  | search_blocks |
| GLOBcomp_31 | dimethyl sulfoxide | search_blocks |
| GLOBcomp_1 | water | search_blocks |
| GLOBcomp_2043 | cetylpyridinium chloride | search_blocks |
| GLOBcomp_4537 | sodium ((4-aminophenyl)sulfonyl)(thiazol-2-yl)amide | search_blocks |
| GLOBcomp_377 | dodecyltrimethylammonium bromide | search_blocks |
| GLOBcomp_1776 | sodium [dodecanoyl(methyl)amino]acetate | search_blocks |
| GLOBprop_14 | Boiling temperature at pressure P, K | search_blocks |
| GLOBprop_2 | Mole fraction | search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBprop_9 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBprop_64 | Apparent molar heat capacity, J/K/mol | search_blocks |
| GLOBprop_15 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBprop_11 | Solid-liquid equilibrium temperature, K | search_blocks |
| GLOBprop_34 | Thermal conductivity, W/m/K | search_blocks |
| GLOBprop_44 | Relative permittivity at zero frequency | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks |
| GLOBprop_18 | Electrical conductivity, S/m | search_blocks |
| GLOBprop_28 |  | resolve_property_ids |
| GLOBmeas_146 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_150 | Mole fraction | search_blocks |
| GLOBmeas_147 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_31 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_811 | Speed of sound, m/s | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_57 | Apparent molar heat capacity, J/K/mol | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_15 | Speed of sound, m/s | search_blocks |
| GLOBmeas_144 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_130 | Solid-liquid equilibrium temperature, K | search_blocks |
| GLOBmeas_41 | Thermal conductivity, W/m/K | search_blocks |
| GLOBmeas_823 | Relative permittivity at zero frequency | search_blocks |
| GLOBmeas_1503 | Solid-liquid equilibrium temperature, K | search_blocks |
| GLOBmeas_359 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_145 | Mole fraction | search_blocks |
| GLOBmeas_36 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_163 | Refractive index (Na D-line) | search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_495 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_14 | Electrical conductivity, S/m | search_blocks |
| GLOBmeas_1258 | Electrical conductivity, S/m | search_blocks |
| GLOBmeas_49 | Electrical conductivity, S/m | search_blocks |
| GLOBphase_3 |  | search_blocks |
| GLOBphase_1 |  | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_7 | Solvent: Mass fraction | search_blocks |
| GLOBvar_16 | Solvent: Volume fraction | search_blocks |
| GLOBvar_9 | Amount concentration (molarity), mol/dm3 | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_8 |  | search_blocks |
| Unique References | 19 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| Unique Compounds | 6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| Unique Properties | 15 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| Unique Measurements | 28 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| Unique Phases | 2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| Unique Variables | 8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| Unique Constraints | 3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| Unique Solvents | 2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| Unique parent blocks | 33 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| Explicit block/subsystem targets | 36 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| Subsystem targets | 3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| Target-matched data points | 3,812 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| GLOBlit_2738 |  | search_blocks, search_system_registry |
| GLOBlit_2979 |  | search_blocks, search_system_registry |
| GLOBlit_4204 |  | search_blocks, search_system_registry |
| GLOBlit_4631 |  | search_blocks, search_system_registry |
| GLOBlit_4951 |  | search_blocks, search_system_registry |
| GLOBlit_5201 |  | search_blocks, search_system_registry |
| GLOBlit_5254 |  | search_blocks, search_system_registry |
| GLOBlit_5288 |  | search_blocks, search_system_registry |
| GLOBlit_6107 |  | search_blocks, search_system_registry |
| GLOBlit_6811 |  | search_blocks, search_system_registry |
| GLOBlit_9758 |  | search_blocks, search_system_registry |
| GLOBlit_1910 |  | search_blocks |
| GLOBlit_1294 |  | search_blocks |
| GLOBlit_2036 |  | search_blocks |
| GLOBlit_5300 |  | search_blocks |
| GLOBlit_5518 |  | search_blocks |
| GLOBlit_6089 |  | search_blocks |
| GLOBlit_6129 |  | search_blocks |
| GLOBlit_7495 |  | search_blocks |
| GLOBlit_7523 |  | search_blocks |
| GLOBlit_7824 |  | search_blocks |
| GLOBlit_9121 |  | search_blocks |
| GLOBlit_10425 |  | search_blocks |
| GLOBlit_178 |  | search_system_registry |
| GLOBlit_271 |  | search_system_registry |
| GLOBlit_391 |  | search_system_registry |
| GLOBlit_729 |  | search_system_registry |
| GLOBlit_844 |  | search_system_registry |
| GLOBlit_865 |  | search_system_registry |
| GLOBlit_955 |  | search_system_registry |
| GLOBlit_1310 |  | search_system_registry |
| GLOBlit_1415 |  | search_system_registry |
| GLOBlit_1426 |  | search_system_registry |
| GLOBlit_1449 |  | search_system_registry |
| GLOBlit_1468 |  | search_system_registry |
| GLOBlit_1478 |  | search_system_registry |
| GLOBlit_1490 |  | search_system_registry |
| GLOBlit_1557 |  | search_system_registry |
| GLOBcomp_58 | glycerol | search_blocks, search_system_registry |
| GLOBcomp_1 | water | search_blocks, search_system_registry |
| GLOBcomp_100 | choline chloride | search_blocks |
| GLOBcomp_855 | 2-(diethylamino)ethanol hydrochloride | search_blocks |
| GLOBcomp_605 | methyltriphenylphosphonium bromide | search_blocks |
| GLOBcomp_8274 | benzyltripropylammonium chloride | search_blocks |
| GLOBcomp_1117 | 1,8-diaza-7-bicyclo[5.4.0]undecene | search_blocks |
| GLOBcomp_3 | carbon dioxide | search_blocks |
| GLOBcomp_214 | potassium carbonate | search_blocks |
| GLOBcomp_1395 | trimethylbenzylammonium chloride | search_blocks |
| GLOBcomp_1986 | benzyltributylammonium chloride | search_blocks |
| GLOBcomp_2043 | cetylpyridinium chloride | search_blocks |
| GLOBcomp_2979 | benzyltriphenylphosphonium chloride | search_blocks |
| GLOBcomp_660 | tetrabutylammonium chloride | search_blocks |
| GLOBcomp_551 | copper sulfate | search_system_registry |
| GLOBcomp_2 | ethanol | search_system_registry |
| GLOBcomp_2007 | lithium hydroxide | search_system_registry |
| GLOBcomp_1863 | aluminum bromide | search_system_registry |
| GLOBcomp_323 | 1-ethyl-3-methylimidazolium bromide | search_system_registry |
| GLOBcomp_1563 | 1-ethylpyridinium bromide | search_system_registry |
| GLOBcomp_518 | aluminum chloride | search_system_registry |
| GLOBcomp_231 | 1-ethyl-3-methylimidazolium chloride | search_system_registry |
| GLOBcomp_84 | 1-ethyl-3-methylimidazolium tetrafluoroborate | search_system_registry |
| GLOBcomp_68 | 1-ethyl-3-methylimidazolium ethyl sulfate | search_system_registry |
| GLOBcomp_146 | 4-methyl-1,3-dioxolan-2-one | search_system_registry |
| GLOBcomp_515 | lithium fluoride | search_system_registry |
| GLOBcomp_312 | ethylene carbonate | search_system_registry |
| GLOBcomp_62 | dimethyl carbonate | search_system_registry |
| GLOBcomp_2065 | pyrrolidinium nitrate | search_system_registry |
| GLOBcomp_5889 | pyrrolidinium acetate | search_system_registry |
| GLOBcomp_3105 | pyrrolidinium formate | search_system_registry |
| GLOBcomp_2658 | ethyldiisopropylammonium formate | search_system_registry |
| GLOBcomp_3788 | 2-pentanaminium formate | search_system_registry |
| GLOBcomp_4880 | quinolinium formate | search_system_registry |
| GLOBcomp_6318 | 1,2-dimethylpyridinium formate | search_system_registry |
| GLOBcomp_6017 | 1,2,3-trimethylpyridinium formate | search_system_registry |
| GLOBcomp_6917 | pyrrolidinium hexanoate | search_system_registry |
| GLOBcomp_7415 | pyrrolidinium heptanoate | search_system_registry |
| GLOBcomp_2737 | pyrrolidinium octanoate | search_system_registry |
| GLOBcomp_4222 | pyrrolidinium nonanoate | search_system_registry |
| GLOBcomp_2395 | sodium dihydrogen citrate | search_system_registry |
| GLOBcomp_1192 | 1-heptyl-3-methylimidazolium bromide | search_system_registry |
| GLOBcomp_1296 | disodium hydrogen citrate | search_system_registry |
| GLOBcomp_270 | trisodium citrate | search_system_registry |
| GLOBcomp_202 | triethylamine | search_system_registry |
| GLOBcomp_41 | potassium chloride | search_system_registry |
| GLOBcomp_1760 | hexyltrimethylammonium bromide | search_system_registry |
| GLOBcomp_734 | 1-dodecyl-3-methylimidazolium bromide | search_system_registry |
| GLOBcomp_201 | glycylglycine | search_system_registry |
| GLOBcomp_742 | glycyl-L-valine | search_system_registry |
| GLOBcomp_495 | glycyl-L-leucine | search_system_registry |
| GLOBcomp_5033 | cetyltrimethylammonium salicylate | search_system_registry |
| GLOBcomp_232 | sodium dodecyl sulfate | search_system_registry |
| GLOBcomp_573 | 1-pentyl-3-methylimidazolium bromide | search_system_registry |
| GLOBcomp_481 | 1-butyl-2,3-dimethylimidazolium tetrafluoroborate | search_system_registry |
| GLOBcomp_374 | ribose | search_system_registry |
| GLOBcomp_90 | D-glucose | search_system_registry |
| GLOBcomp_120 | D-sucrose | search_system_registry |
| GLOBcomp_886 | D-raffinose | search_system_registry |
| GLOBcomp_5 | propan-1-ol | search_system_registry |
| GLOBcomp_3909 | sodium dodecane-1-sulfonate | search_system_registry |
| GLOBcomp_1910 | N-ethyl-N-methylpiperidinium bromide | search_system_registry |
| GLOBcomp_3836 | 1-methyl-1-propylpiperidinium bromide | search_system_registry |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBprop_18 | Electrical conductivity, S/m | search_blocks, search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_192 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_49 | Electrical conductivity, S/m | search_blocks, search_system_registry |
| GLOBmeas_14 | Electrical conductivity, S/m | search_blocks, search_system_registry |
| GLOBmeas_923 | Electrical conductivity, S/m | search_blocks |
| GLOBmeas_2068 | Electrical conductivity, S/m | search_system_registry |
| GLOBmeas_1646 | Electrical conductivity, S/m | search_system_registry |
| GLOBphase_1 |  | search_blocks, search_system_registry |
| GLOBphase_4 |  | search_system_registry |
| GLOBsolvent_1 |  | search_blocks, search_system_registry |
| GLOBsolvent_128 |  | search_blocks |
| GLOBsolvent_331 |  | search_blocks |
| GLOBsolvent_22 |  | search_blocks |
| GLOBsolvent_169 |  | search_blocks |
| GLOBsolvent_2 |  | search_system_registry |
| GLOBsolvent_375 |  | search_system_registry |
| GLOBsolvent_277 |  | search_system_registry |
| GLOBsolvent_486 |  | search_system_registry |
| GLOBsolvent_451 |  | search_system_registry |
| GLOBsolvent_163 |  | search_system_registry |
| GLOBsolvent_68 |  | search_system_registry |
| GLOBsolvent_51 |  | search_system_registry |
| GLOBsolvent_64 |  | search_system_registry |
| GLOBsolvent_425 |  | search_system_registry |
| GLOBsolvent_187 |  | search_system_registry |
| GLOBsolvent_283 |  | search_system_registry |
| GLOBsolvent_278 |  | search_system_registry |
| GLOBsolvent_194 |  | search_system_registry |
| GLOBsolvent_475 |  | search_system_registry |
| GLOBsolvent_389 |  | search_system_registry |
| GLOBsolvent_310 |  | search_system_registry |
| GLOBsolvent_34 |  | search_system_registry |
| GLOBsolvent_42 |  | search_system_registry |
| GLOBsolvent_354 |  | search_system_registry |
| GLOBsolvent_9 |  | search_system_registry |
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBvar_8 | Solvent: Mole fraction | search_blocks, search_system_registry |
| GLOBvar_15 | Mass ratio of solute to solvent | search_blocks |
| GLOBvar_19 | Amount ratio of solute to solvent | search_blocks |
| GLOBvar_7 | Solvent: Mass fraction | search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | search_system_registry |
| GLOBvar_16 | Solvent: Volume fraction | search_system_registry |
| GLOBvar_9 | Amount concentration (molarity), mol/dm3 | search_system_registry |
| GLOBvar_6 | Solvent: Molality, mol/kg | search_system_registry |
| GLOBvar_11 | Solvent: Amount concentration (molarity), mol/dm3 | search_system_registry |
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks, search_system_registry |
| GLOBconstr_13 | Amount ratio of solute to solvent | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |
| GLOBconstr_7 | Solvent: Mole fraction | search_system_registry |
| GLOBconstr_8 | Molality, mol/kg | search_system_registry |
| GLOBconstr_5 | Mass fraction | search_system_registry |
| GLOBconstr_10 | Solvent: Mass fraction | search_system_registry |
| GLOBblocktype_1 |  | search_system_registry |
| GLOBblocktype_3 |  | search_system_registry |
| GLOBblocktype_2 |  | search_system_registry |
| Unique References | 38 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| Unique Compounds | 63 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| Unique Properties | 4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| Unique Measurements | 10 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| Unique Phases | 2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| Unique Solvents | 26 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| Unique Variables | 13 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| Unique Constraints | 9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| Unique Block_Types | 3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| Unique parent blocks | 82 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| Explicit block/subsystem targets | 82 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| Subsystem targets | 0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| Target-matched data points | 14,760 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| **TOTAL** | **29,288** |  |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 10.1016/j.jct.2016.07.006 | PROPblock_1 | declared | 6 | ternary | — | search_blocks | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 10.1021/acs.jced.6b00783 | PROPblock_1 | declared | 55 | ternary | — | search_blocks | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 10.1021/je101012n | PROPblock_30 | declared | 33 | binary | — | search_blocks | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.fluid.2006.05.007 | 1 | 45 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.fluid.2006.12.005 | 2 | 10 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.fluid.2010.10.005 | 2 | 68 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.fluid.2013.01.025 | 1 | 85 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.fluid.2013.06.041 | 1 | 135 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.fluid.2015.07.012 | 4 | 332 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.fluid.2017.09.005 | 4 | 288 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.fluid.2018.11.035 | 1 | 6 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2004.03.011 | 1 | 206 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2004.07.019 | 2 | 1,161 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2005.07.012 | 1 | 96 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2006.01.007 | 1 | 6 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2006.01.011 | 2 | 20 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2006.08.002 | 3 | 301 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2006.12.012 | 2 | 240 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2007.05.004 | 4 | 152 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2007.05.010 | 1 | 10 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2007.06.007 | 1 | 40 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2007.06.010 | 1 | 92 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2010.09.003 | 1 | 54 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2013.10.010 | 1 | 4 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2015.06.024 | 1 | 40 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2018.02.022 | 4 | 652 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2018.05.016 | 1 | 12 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2018.06.021 | 1 | 15 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.jct.2019.05.013 | 2 | 24 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.tca.2011.08.013 | 2 | 32 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/acs.jced.5b00485 | 1 | 2 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/acs.jced.5b00498 | 1 | 70 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/acs.jced.5b00662 | 1 | 30 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/acs.jced.6b00526 | 2 | 166 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/acs.jced.6b01058 | 2 | 24 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/acs.jced.7b00299 | 2 | 4 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/acs.jced.7b00501 | 1 | 32 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/acs.jced.8b00058 | 1 | 20 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/acs.jced.8b00086 | 3 | 18 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/acs.jced.8b00181 | 1 | 6 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/acs.jced.8b00723 | 2 | 6 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/acs.jced.8b00939 | 2 | 18 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/acs.jced.8b01048 | 1 | 9 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/acs.jced.9b00026 | 1 | 10 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je020140j | 2 | 154 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je020173z | 1 | 24 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je025610o | 2 | 60 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je0301500 | 1 | 5 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je034101z | 1 | 401 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je049691v | 1 | 180 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je049955d | 1 | 15 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je0600810 | 2 | 18 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je0601098 | 2 | 24 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je060219e | 1 | 26 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je060335h | 1 | 164 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je2003622 | 2 | 32 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je4001203 | 1 | 138 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je4003515 | 2 | 48 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je600565m | 2 | 35 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je700300y | 2 | 168 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je700618y | 2 | 30 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je700645p | 1 | 70 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je800150h | 2 | 216 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je800271e | 2 | 104 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je800942u | 2 | 36 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je900064e | 1 | 10 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je9000697 | 2 | 32 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je9001027 | 2 | 70 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1021/je900743e | 2 | 30 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |  |  |
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2006.05.007 | PROPblock_1 | declared | 45 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2006.12.005 | PROPblock_3 | declared | 8 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2006.12.005 | PROPblock_4 | declared | 2 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2010.10.005 | PROPblock_1 | declared | 34 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2010.10.005 | PROPblock_2 | declared | 34 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2013.01.025 | PROPblock_2 | declared | 85 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2013.06.041 | PROPblock_11 | declared | 135 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_1 | declared | 80 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_2 | declared | 84 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_3 | declared | 84 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_4 | declared | 84 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_1 | declared | 72 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_2 | declared | 72 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_3 | declared | 72 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_4 | declared | 72 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2018.11.035 | PROPblock_2 | declared | 6 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2004.03.011 | PROPblock_1 | declared | 206 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2005.07.012 | PROPblock_8 | declared | 96 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2006.01.007 | PROPblock_4 | declared | 6 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2006.01.011 | PROPblock_12 | declared | 10 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2006.01.011 | PROPblock_13 | declared | 10 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2006.08.002 | PROPblock_2 | declared | 19 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2006.08.002 | PROPblock_3 | declared | 4 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2006.08.002 | PROPblock_4 | declared | 278 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2006.12.012 | PROPblock_3 | declared | 120 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2006.12.012 | PROPblock_4 | declared | 120 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2007.05.004 | PROPblock_9 | declared | 39 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2007.05.010 | PROPblock_10 | declared | 10 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2007.06.007 | PROPblock_6 | declared | 40 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2007.06.010 | PROPblock_4 | declared | 92 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2010.09.003 | PROPblock_4 | declared | 54 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2013.10.010 | PROPblock_2 | declared | 4 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2018.02.022 | PROPblock_21 | declared | 100 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2018.02.022 | PROPblock_22 | declared | 224 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2018.02.022 | PROPblock_24 | declared | 84 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2018.05.016 | PROPblock_7 | declared | 12 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2018.06.021 | PROPblock_10 | declared | 15 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2019.05.013 | PROPblock_2 | declared | 12 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.jct.2019.05.013 | PROPblock_3 | declared | 12 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.tca.2011.08.013 | PROPblock_10 | declared | 16 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.tca.2011.08.013 | PROPblock_12 | declared | 16 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.5b00485 | PROPblock_8 | declared | 2 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.5b00498 | PROPblock_1 | declared | 70 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.5b00662 | PROPblock_55 | declared | 30 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.6b00526 | PROPblock_16 | declared | 133 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.6b00526 | PROPblock_18 | declared | 33 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.7b00299 | PROPblock_11 | declared | 2 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.7b00501 | PROPblock_9 | declared | 32 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.8b00058 | PROPblock_9 | declared | 20 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | declared | 6 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.8b00086 | PROPblock_48 | declared | 6 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.8b00181 | PROPblock_11 | declared | 6 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.8b00723 | PROPblock_10 | declared | 3 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.8b00723 | PROPblock_12 | declared | 3 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.8b00939 | PROPblock_18 | declared | 9 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.8b01048 | PROPblock_10 | declared | 9 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/acs.jced.9b00026 | PROPblock_16 | declared | 10 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je020140j | PROPblock_4 | declared | 77 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je020140j | PROPblock_5 | declared | 77 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je025610o | PROPblock_5 | declared | 30 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je025610o | PROPblock_6 | declared | 30 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je0301500 | PROPblock_13 | declared | 5 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je049955d | PROPblock_16 | declared | 15 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je0600810 | PROPblock_3 | declared | 9 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je060219e | PROPblock_1 | declared | 26 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je2003622 | PROPblock_1 | declared | 16 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je4001203 | PROPblock_1 | declared | 138 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je4003515 | PROPblock_8 | declared | 25 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je600565m | PROPblock_5 | declared | 17 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je700618y | PROPblock_7 | declared | 15 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je700645p | PROPblock_6 | declared | 70 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je800150h | PROPblock_8 | declared | 108 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je800271e | PROPblock_3 | declared | 52 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je800271e | PROPblock_4 | declared | 52 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je800942u | PROPblock_5 | declared | 18 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je800942u | PROPblock_6 | declared | 18 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je900064e | PROPblock_6 | declared | 10 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je9000697 | PROPblock_1 | declared | 16 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je9000697 | PROPblock_2 | declared | 16 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je9001027 | PROPblock_3 | declared | 35 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je9001027 | PROPblock_4 | declared | 35 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je900743e | PROPblock_2 | declared | 15 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1021/je900743e | PROPblock_3 | declared | 15 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10.1016/j.fluid.2008.09.010 | 2 | 32 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1016/j.jct.2005.07.012 | 1 | 96 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1016/j.jct.2006.01.007 | 2 | 12 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1016/j.jct.2006.12.012 | 2 | 240 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1016/j.jct.2007.06.007 | 3 | 87 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1016/j.jct.2007.06.010 | 2 | 308 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1016/j.tca.2011.08.013 | 3 | 48 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1016/j.tca.2011.09.009 | 1 | 1 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1021/acs.jced.8b00326 | 2 | 192 | binary, ternary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1021/acs.jced.8b01048 | 1 | 9 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1021/je100287g | 1 | 96 | ternary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1021/je2002607 | 1 | 5 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1021/je301171y | 1 | 63 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1021/je400149j | 3 | 373 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1021/je4004788 | 4 | 389 | binary, ternary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1021/je400531a | 2 | 42 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1021/je7001013 | 2 | 145 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1021/je700645p | 1 | 70 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1021/je9001027 | 2 | 70 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |  |  |
| 10.1016/j.fluid.2008.09.010 | PROPblock_4 | declared | 16 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.fluid.2008.09.010 | PROPblock_5 | declared | 16 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.jct.2005.07.012 | PROPblock_8 | declared | 96 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.jct.2006.01.007 | PROPblock_3 | declared | 6 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.jct.2006.01.007 | PROPblock_4 | declared | 6 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.jct.2006.12.012 | PROPblock_3 | declared | 120 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.jct.2006.12.012 | PROPblock_4 | declared | 120 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.jct.2007.06.007 | PROPblock_4 | declared | 7 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.jct.2007.06.007 | PROPblock_5 | declared | 40 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.jct.2007.06.007 | PROPblock_6 | declared | 40 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.jct.2007.06.010 | PROPblock_3 | declared | 216 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.jct.2007.06.010 | PROPblock_4 | declared | 92 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.tca.2011.08.013 | PROPblock_10 | declared | 16 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.tca.2011.08.013 | PROPblock_11 | declared | 16 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.tca.2011.08.013 | PROPblock_12 | declared | 16 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1016/j.tca.2011.09.009 | PROPblock_1 | declared | 1 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/acs.jced.8b00326 | PROPblock_3 | declared | 176 | ternary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/acs.jced.8b00326 | PROPblock_3 | BLKsubsys_1 | 16 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/acs.jced.8b01048 | PROPblock_10 | declared | 9 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je100287g | PROPblock_2 | declared | 96 | ternary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je2002607 | PROPblock_1 | declared | 5 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je301171y | PROPblock_5 | declared | 63 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je400149j | PROPblock_5 | declared | 363 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je400149j | PROPblock_6 | declared | 8 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je400149j | PROPblock_7 | declared | 2 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je4004788 | PROPblock_10 | declared | 172 | ternary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je4004788 | PROPblock_10 | BLKsubsys_1 | 6 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je4004788 | PROPblock_7 | declared | 205 | ternary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je4004788 | PROPblock_7 | BLKsubsys_1 | 6 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je400531a | PROPblock_16 | declared | 21 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je400531a | PROPblock_17 | declared | 21 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je7001013 | PROPblock_10 | declared | 33 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je7001013 | PROPblock_9 | declared | 112 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je700645p | PROPblock_6 | declared | 70 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je9001027 | PROPblock_3 | declared | 35 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1021/je9001027 | PROPblock_4 | declared | 35 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10.1007/s10765-016-2089-2 | 1 | 45 | binary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2005.05.022 | 1 | 9 | ternary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2006.05.028 | 6 | 127 | binary, ternary, unary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2009.07.020 | 4 | 7 | binary, ternary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2010.05.019 | 13 | 264 | binary, unary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2010.08.004 | 3 | 354 | ternary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2011.03.031 | 2 | 119 | binary, ternary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2013.07.012 | 3 | 108 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2013.08.005 | 1 | 18 | binary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2014.01.038 | 4 | 720 | binary, ternary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2014.02.022 | 2 | 283 | binary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2014.03.024 | 4 | 64 | ternary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2014.04.027 | 2 | 522 | binary, ternary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2014.05.020 | 4 | 1,368 | ternary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2014.06.009 | 2 | 376 | ternary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2014.09.020 | 1 | 36 | ternary | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2016.04.007 | 1 | 60 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.fluid.2017.03.011 | 1 | 11 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.jct.2006.08.009 | 1 | 99 | binary | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.jct.2014.06.031 | 1 | 85 | binary | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.jct.2016.02.026 | 1 | 7 | binary | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.jct.2017.01.011 | 1 | 44 | binary | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.jct.2018.02.022 | 2 | 212 | binary | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.jct.2018.05.016 | 1 | 16 | binary | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.jct.2018.07.015 | 1 | 20 | binary | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.jct.2018.07.031 | 2 | 50 | binary, ternary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.jct.2019.04.017 | 2 | 436 | binary, ternary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.tca.2013.05.023 | 3 | 190 | binary, ternary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.tca.2013.07.012 | 1 | 296 | binary | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1016/j.tca.2013.10.028 | 1 | 21 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1021/acs.jced.5b01080 | 1 | 175 | binary | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1021/acs.jced.8b00213 | 2 | 26 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1021/acs.jced.8b00326 | 1 | 176 | ternary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1021/acs.jced.9b00134 | 1 | 6 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1021/je100104v | 2 | 15 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1021/je201184b | 1 | 107 | binary | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1021/je5002126 | 1 | 21 | binary | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |  |  |
| 10.1007/s10765-016-2089-2 | PROPblock_1 | declared | 45 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2005.05.022 | PROPblock_1 | declared | 9 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2006.05.028 | PROPblock_16 | declared | 42 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2006.05.028 | PROPblock_18 | declared | 21 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2006.05.028 | PROPblock_20 | declared | 21 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2006.05.028 | PROPblock_5 | declared | 1 | unary | 1 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2006.05.028 | PROPblock_6 | declared | 21 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2006.05.028 | PROPblock_8 | declared | 21 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2009.07.020 | PROPblock_12 | declared | 2 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2009.07.020 | PROPblock_15 | declared | 2 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2009.07.020 | PROPblock_18 | declared | 2 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2009.07.020 | PROPblock_8 | declared | 1 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.05.019 | PROPblock_33 | declared | 1 | unary | 1 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.05.019 | PROPblock_34 | declared | 21 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.05.019 | PROPblock_35 | declared | 19 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.05.019 | PROPblock_36 | declared | 22 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.05.019 | PROPblock_37 | declared | 21 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.05.019 | PROPblock_38 | declared | 23 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.05.019 | PROPblock_39 | declared | 21 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.05.019 | PROPblock_40 | declared | 21 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.05.019 | PROPblock_41 | declared | 21 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.05.019 | PROPblock_42 | declared | 25 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.05.019 | PROPblock_43 | declared | 25 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.05.019 | PROPblock_44 | declared | 21 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.05.019 | PROPblock_45 | declared | 23 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.08.004 | PROPblock_5 | declared | 194 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.08.004 | PROPblock_6 | declared | 84 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2010.08.004 | PROPblock_9 | declared | 76 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2011.03.031 | PROPblock_1 | declared | 29 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2011.03.031 | PROPblock_3 | declared | 90 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2013.07.012 | PROPblock_12 | declared | 36 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2013.07.012 | PROPblock_4 | declared | 36 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2013.07.012 | PROPblock_8 | declared | 36 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2013.08.005 | PROPblock_4 | declared | 18 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.01.038 | PROPblock_10 | declared | 72 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.01.038 | PROPblock_5 | declared | 216 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.01.038 | PROPblock_7 | declared | 216 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.01.038 | PROPblock_9 | declared | 216 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.02.022 | PROPblock_1 | declared | 213 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.02.022 | PROPblock_2 | declared | 70 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.03.024 | PROPblock_1 | declared | 7 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.03.024 | PROPblock_2 | declared | 25 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.03.024 | PROPblock_3 | declared | 12 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.03.024 | PROPblock_4 | declared | 20 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.04.027 | PROPblock_1 | declared | 456 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.04.027 | PROPblock_2 | declared | 66 | binary | 2 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.05.020 | PROPblock_1 | declared | 342 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.05.020 | PROPblock_2 | declared | 342 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.05.020 | PROPblock_3 | declared | 342 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.05.020 | PROPblock_4 | declared | 342 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.06.009 | PROPblock_1 | declared | 186 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.06.009 | PROPblock_4 | declared | 190 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2014.09.020 | PROPblock_12 | declared | 36 | ternary | 3 | search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2016.04.007 | PROPblock_1 | declared | 60 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.fluid.2017.03.011 | PROPblock_20 | declared | 11 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.jct.2006.08.009 | PROPblock_6 | declared | 99 | binary | 2 | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.jct.2008.07.005 | PROPblock_8 | declared | 96 | binary | 2 | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.jct.2014.06.031 | PROPblock_5 | declared | 85 | binary | 2 | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.jct.2016.02.026 | PROPblock_17 | declared | 7 | binary | 2 | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.jct.2017.01.011 | PROPblock_3 | declared | 44 | binary | 2 | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.jct.2018.02.022 | PROPblock_31 | declared | 136 | binary | 2 | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.jct.2018.02.022 | PROPblock_33 | declared | 76 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.jct.2018.05.016 | PROPblock_9 | declared | 16 | binary | 2 | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.jct.2018.07.015 | PROPblock_1 | declared | 20 | binary | 2 | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.jct.2018.07.031 | PROPblock_13 | declared | 25 | ternary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.jct.2018.07.031 | PROPblock_6 | declared | 25 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.jct.2019.04.017 | PROPblock_5 | declared | 186 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.jct.2019.04.017 | PROPblock_7 | declared | 250 | ternary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.tca.2013.05.023 | PROPblock_2 | declared | 10 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.tca.2013.05.023 | PROPblock_6 | declared | 90 | ternary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.tca.2013.05.023 | PROPblock_7 | declared | 90 | ternary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.tca.2013.07.012 | PROPblock_3 | declared | 296 | binary | 2 | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1016/j.tca.2013.10.028 | PROPblock_3 | declared | 21 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1021/acs.jced.5b01080 | PROPblock_15 | declared | 175 | binary | 2 | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1021/acs.jced.8b00213 | PROPblock_34 | declared | 13 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1021/acs.jced.8b00213 | PROPblock_39 | declared | 13 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1021/acs.jced.8b00326 | PROPblock_2 | declared | 176 | ternary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1021/acs.jced.9b00134 | PROPblock_13 | declared | 6 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1021/je100104v | PROPblock_1 | declared | 10 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1021/je100104v | PROPblock_13 | declared | 5 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1021/je201184b | PROPblock_6 | declared | 107 | binary | 2 | search_blocks, search_system_registry | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10.1021/je5002126 | PROPblock_3 | declared | 21 | binary | — | search_blocks | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| **TOTAL** | **231** | **16,527** | **16,621** |  | **146** |  |  |


## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | ---: | ---: | --- |
| 1 | 1 | `memory_catalog_add` | global_id=GLOBcomp_1, name=water, registry_id=wate… | 2 | — | — | 0.0 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 2 | 1 | `memory_catalog_add` | global_id=GLOBcomp_1586, name=iron(II) sulfate, re… | 2 | — | — | 0.0 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 3 | 1 | `memory_catalog_add` | global_id=GLOBprop_1, name=Mass density, registry_… | 2 | — | — | 0.0 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 4 | 1 | `memory_catalog_add` | global_id=GLOBprop_4, name=Viscosity (dynamic), re… | 2 | — | — | 0.0 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 5 | 1 | `memory_catalog_add` | global_id=GLOBprop_13, name=Surface tension (liqui… | 2 | — | — | 0.0 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 6 | 1 | `memory_catalog_add` | global_id=GLOBprop_18, name=Electrical conductivit… | 2 | — | — | 0.0 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 7 | 1 | `memory_catalog_add` | global_id=GLOBprop_37, name=Molar conductivity, re… | 2 | — | — | 0.0 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 8 | 1 | `search_blocks` | compound=['GLOBcomp_1586', 'GLOBcomp_1…, limit=50,… | 713 | DISCARD | 655 | 18.9 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 9 | 1 | `search_blocks` | compound=['GLOBcomp_1586', 'GLOBcomp_1…, limit=50,… | 806 | DISCARD | 748 | 11.9 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 10 | 1 | `search_blocks` | compound=['GLOBcomp_1586', 'GLOBcomp_1…, limit=50,… | 812 | DISCARD | 754 | 9.4 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 11 | 2 | `search_blocks` | compound=GLOBcomp_1586, limit=50, purpose=Find any… | 1,181 | KEEP | 1091 | 13.7 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 12 | 2 | `search_system_summary` | compound=GLOBcomp_1586, purpose=Check if iron(II) … | 910 | KEEP | 910 | 9.1 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 13 | 1 | `L1_query` | context=This is for finding transport…, id_catalog… | 9,990 | — | — | 114.1 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 1 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,184 | KEEP | 1079 | 14.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 2 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,208 | KEEP | 1119 | 15.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 3 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,091 | KEEP | 1046 | 14.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 4 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 857 | DISCARD | 799 | 19.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 5 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,136 | KEEP | 1106 | 10.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 6 | 1 | `L1_query` | context=Looking for electrodeposition…, id_catalog… | 271 | — | — | 155.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 7 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 1,244 | KEEP | 1154 | 21.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 8 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 1,271 | KEEP | 1170 | 21.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 9 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 748 | DISCARD | 690 | 15.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 1,014 | KEEP | 1014 | 15.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 11 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 629 | DISCARD | 571 | 15.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 12 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=10, p… | 1,335 | KEEP | 1245 | 21.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 13 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=20, p… | 1,361 | KEEP | 1245 | 15.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 14 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=10, p… | 977 | KEEP | 948 | 21.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 15 | 1 | `L1_query` | context=Looking for electrodeposition…, id_catalog… | 270 | — | — | 337.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 16 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,375 | KEEP | 1266 | 20.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 17 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,195 | KEEP | 1104 | 15.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 18 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,366 | KEEP | 1366 | 22.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 19 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,166 | KEEP | 1136 | 20.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 20 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 807 | DISCARD | 749 | 9.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 21 | 1 | `L1_query` | context=Looking for electrodeposition…, id_catalog… | 270 | — | — | 180.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 22 | 2 | `search_system_summary` | compound=['GLOBcomp_1', 'GLOBcomp_31'], purpose=Fi… | 1,333 | KEEP | 1315 | 18.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 23 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,263 | KEEP | 1169 | 22.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 24 | 1 | `L1_query` | context=Looking for electrodeposition…, id_catalog… | 419 | — | — | 262.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 1 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,359 | KEEP | 1344 | 22.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 2 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,247 | KEEP | 1142 | 23.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 3 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,349 | KEEP | 1303 | 22.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 4 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 916 | KEEP | 884 | 19.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 5 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 788 | DISCARD | 730 | 16.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 6 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 693 | DISCARD | 635 | 7.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 7 | 1 | `L1_query` | context=This is for Fe electrodeposit…, id_catalog… | 1,114 | — | — | 223.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 8 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,138 | KEEP | 1138 | 20.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 9 | 2 | `L1_query` | context=Binary system: water + DMSO. …, id_catalog… | 270 | — | — | 93.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,433 | KEEP | 1433 | 17.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 11 | 2 | `L1_query` | context=Binary system: water + DMSO. …, id_catalog… | 21,444 | — | — | 56.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 12 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 911 | KEEP | 879 | 17.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 13 | 3 | `L1_query` | context=Binary system: water + DMSO. …, id_catalog… | 8,486 | — | — | 51.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 14 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 603 | DISCARD | 545 | 13.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 15 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,221 | KEEP | 1159 | 28.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 16 | 3 | `L1_query` | context=Binary system: water + DMSO. …, id_catalog… | 270 | — | — | 97.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 17 | 2 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find the global pr… | 251 | KEEP | 251 | 5.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 18 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 892 | DISCARD | 834 | 17.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 19 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 654 | DISCARD | 596 | 15.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 20 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 781 | DISCARD | 723 | 16.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 21 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 719 | DISCARD | 661 | 18.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 22 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 825 | DISCARD | 767 | 9.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 23 | 3 | `L1_query` | context=Binary system: water + DMSO. …, id_catalog… | 1,792 | — | — | 252.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 1 | 1 | `memory_catalog_add` | global_id=GLOBcomp_1, name=water, registry_id=7732… | 2 | — | — | 0.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 2 | 1 | `memory_catalog_add` | global_id=GLOBcomp_58, name=glycerol, registry_id=… | 2 | — | — | 0.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 3 | 1 | `memory_catalog_add` | global_id=GLOBprop_1, name=Mass density, registry_… | 127 | — | — | 0.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 4 | 1 | `memory_catalog_add` | global_id=GLOBprop_4, name=Dynamic viscosity, regi… | 127 | — | — | 0.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 5 | 1 | `memory_catalog_add` | global_id=GLOBprop_13, name=Surface tension liquid… | 127 | — | — | 0.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 6 | 1 | `memory_catalog_add` | global_id=GLOBprop_28, name=Excess molar volume, r… | 127 | — | — | 0.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 7 | 1 | `memory_catalog_add` | global_id=GLOBprop_18, name=Electrical conductivit… | 127 | — | — | 0.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 8 | 2 | `memory_catalog_add` | global_id=GLOBprop_1, name=Mass density, registry_… | 2 | — | — | 0.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 9 | 2 | `memory_catalog_add` | global_id=GLOBprop_4, name=Dynamic viscosity, regi… | 2 | — | — | 0.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10 | 2 | `memory_catalog_add` | global_id=GLOBprop_13, name=Surface tension liquid… | 2 | — | — | 0.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 11 | 2 | `memory_catalog_add` | global_id=GLOBprop_18, name=Electrical conductivit… | 2 | — | — | 0.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 12 | 2 | `memory_catalog_add` | global_id=GLOBprop_28, name=Excess molar volume, r… | 2 | — | — | 0.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 13 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,072 | KEEP | 997 | 16.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 14 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,178 | KEEP | 1148 | 15.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 15 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,219 | KEEP | 1189 | 12.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 16 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 706 | DISCARD | 648 | 14.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 17 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 737 | DISCARD | 679 | 7.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 18 | 2 | `L1_query` | context=This is for Fe electrodeposit…, id_catalog… | 783 | — | — | 162.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 19 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,118 | KEEP | 1103 | 23.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 20 | 2 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,062 | KEEP | 1062 | 17.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 21 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=20, … | 1,090 | KEEP | 1090 | 21.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 22 | 3 | `L1_query` | context=Binary mixture water+glycerol…, id_catalog… | 720 | — | — | 218.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 23 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,341 | KEEP | 1311 | 19.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 24 | 3 | `L1_query` | context=Binary mixture water+glycerol…, id_catalog… | 9,461 | — | — | 59.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 25 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,190 | KEEP | 1160 | 11.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 26 | 3 | `L1_query` | context=Binary mixture water+glycerol…, id_catalog… | 8,955 | — | — | 43.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 27 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,140 | KEEP | 1125 | 23.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 28 | 2 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,145 | KEEP | 1130 | 25.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 29 | 3 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=100,… | 1,215 | KEEP | 1125 | 21.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 30 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 372 | KEEP | 372 | 20.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 31 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,122 | KEEP | 1122 | 14.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 32 | 6 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,054 | KEEP | 1039 | 14.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 33 | 7 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,118 | KEEP | 1103 | 12.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 34 | 8 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,207 | KEEP | 1192 | 12.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 35 | 4 | `L1_query` | context=Binary mixture water+glycerol…, id_catalog… | 858 | — | — | 338.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 36 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 686 | DISCARD | 628 | 14.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 37 | 2 | `search_blocks` | compound=GLOBcomp_58, limit=50, property=GLOBprop_… | 662 | DISCARD | 604 | 11.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 38 | 3 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 779 | DISCARD | 712 | 19.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 39 | 4 | `L1_query` | context=Binary mixture water+glycerol…, id_catalog… | 1,821 | — | — | 100.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 40 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 723 | DISCARD | 665 | 14.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 41 | 2 | `search_blocks` | compound=GLOBcomp_58, limit=50, property=GLOBprop_… | 1,306 | KEEP | 1201 | 20.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 42 | 2 | `search_system_registry` | compound=GLOBcomp_1, limit=50, property=GLOBprop_1… | 1,501 | KEEP | 1351 | 20.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 43 | 4 | `L1_query` | context=Binary mixture water+glycerol…, id_catalog… | 3,209 | — | — | 105.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| **TOTAL** | **206** |  |  | **138,571** |  | **64,229** | **3,966.0** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 9,605 | 1,130 | 10,735 | 3,189 | 16.5 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 2 | L1-worker | claudeopus46 | 20,643 | 2,090 | 22,733 | 2,153 | 9.7 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 3 | L1-worker | claudeopus46 | 2,065 | 443 | 2,508 | 1,590 | 9.7 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 4 | L1-worker | claudeopus46 | 2,065 | 450 | 2,515 | 1,722 | 11.1 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 5 | L1-worker | claudeopus46 | 2,065 | 455 | 2,520 | 1,292 | 8.8 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 6 | L1-worker | claudeopus46 | 20,643 | 5,261 | 25,904 | 994 | 6.9 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 7 | L1-worker | claudeopus46 | 2,065 | 7,058 | 9,123 | 1,498 | 13.0 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 8 | L1-worker | claudeopus46 | 2,065 | 1,258 | 3,323 | 1,390 | 8.4 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 9 | L1-worker | claudeopus46 | 20,643 | 8,012 | 28,655 | 2,346 | 14.3 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 10 | L1-worker | claudeopus46 | 536 | 1,819 | 2,355 | 663 | 4.9 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 11 | L1-worker | claudeopus46 | 1,356 | 1,939 | 3,295 | 894 | 5.1 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 12 | L1-worker | claudeopus46 | 1,323 | 9,885 | 11,208 | 862 | 6.6 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 13 | L1-worker | claudeopus46 | 298 | 1,584 | 1,882 | 735 | 3.8 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 14 | L1-worker | claudeopus46 | 747 | 18,089 | 18,836 | 796 | 8.7 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 15 | L0-main | claudeopus46 | 9,605 | 14,550 | 24,155 | 3,116 | 20.9 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 16 | L0-main | claudeopus46 | 1,356 | 2,319 | 3,675 | 669 | 4.7 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 17 | L0-main | claudeopus46 | 1,323 | 17,127 | 18,450 | 2,312 | 14.0 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 18 | L0-main | claudeopus46 | 298 | 2,980 | 3,278 | 1,910 | 6.5 | Find all data blocks containing iron(II) sulfate (GLOBcomp_1 (query_runs/run_1) |
| 1 | L0-main | claudeopus46 | 9,605 | 1,559 | 11,164 | 14,837 | 57.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,411 | 22,054 | 2,174 | 8.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 3 | L1-worker | claudeopus46 | 2,065 | 9,225 | 11,290 | 1,431 | 13.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 4 | L1-worker | claudeopus46 | 2,065 | 18,905 | 20,970 | 1,416 | 14.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 5 | L1-worker | claudeopus46 | 2,065 | 4,934 | 6,999 | 1,581 | 13.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 6 | L1-worker | claudeopus46 | 2,065 | 466 | 2,531 | 1,272 | 11.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 7 | L1-worker | claudeopus46 | 2,065 | 2,285 | 4,350 | 1,496 | 10.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 8 | L1-worker | claudeopus46 | 20,643 | 4,181 | 24,824 | 3,168 | 17.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 9 | L1-worker | claudeopus46 | 536 | 2,469 | 3,005 | 804 | 4.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 10 | L1-worker | claudeopus46 | 1,356 | 2,589 | 3,945 | 1,034 | 5.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 11 | L1-worker | claudeopus46 | 1,323 | 11,545 | 12,868 | 5,671 | 25.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 12 | L1-worker | claudeopus46 | 298 | 6,393 | 6,691 | 4,640 | 19.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 13 | L1-worker | claudeopus46 | 747 | 112,401 | 113,148 | 832 | 7.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 14 | L1-worker | claudeopus46 | 20,643 | 103,902 | 124,545 | 2,162 | 13.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 15 | L1-worker | claudeopus46 | 20,643 | 107,113 | 127,756 | 13,147 | 56.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 16 | L1-worker | claudeopus46 | 2,065 | 8,746 | 10,811 | 1,537 | 13.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 17 | L1-worker | claudeopus46 | 2,065 | 11,955 | 14,020 | 1,503 | 13.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 18 | L1-worker | claudeopus46 | 2,065 | 466 | 2,531 | 1,150 | 7.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 19 | L1-worker | claudeopus46 | 2,065 | 6,643 | 8,708 | 1,611 | 14.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 20 | L1-worker | claudeopus46 | 2,065 | 482 | 2,547 | 1,030 | 7.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 21 | L1-worker | claudeopus46 | 20,643 | 108,843 | 129,486 | 5,533 | 26.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 22 | L1-worker | claudeopus46 | 2,065 | 8,785 | 10,850 | 1,555 | 13.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 23 | L1-worker | claudeopus46 | 2,065 | 11,989 | 14,054 | 1,558 | 14.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 24 | L1-worker | claudeopus46 | 2,065 | 6,682 | 8,747 | 1,607 | 14.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 25 | L1-worker | claudeopus46 | 20,610 | 114,244 | 134,854 | 524 | 6.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 26 | L1-worker | claudeopus46 | 20,643 | 113,617 | 134,260 | 5,268 | 32.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 27 | L1-worker | claudeopus46 | 1,356 | 4,911 | 6,267 | 1,012 | 5.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 28 | L1-worker | claudeopus46 | 536 | 4,791 | 5,327 | 826 | 8.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 29 | L1-worker | claudeopus46 | 298 | 1,394 | 1,692 | 1,000 | 6.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 30 | L1-worker | claudeopus46 | 1,323 | 19,477 | 20,800 | 5,367 | 24.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 31 | L1-worker | claudeopus46 | 298 | 6,089 | 6,387 | 4,454 | 19.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 32 | L1-worker | claudeopus46 | 747 | 111,679 | 112,426 | 860 | 8.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 33 | L1-worker | claudeopus46 | 20,643 | 197,761 | 218,404 | 2,567 | 15.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 34 | L1-worker | claudeopus46 | 2,065 | 10,331 | 12,396 | 1,676 | 13.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 35 | L1-worker | claudeopus46 | 2,065 | 11,183 | 13,248 | 1,648 | 14.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 36 | L1-worker | claudeopus46 | 2,065 | 8,048 | 10,113 | 1,661 | 14.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 37 | L1-worker | claudeopus46 | 2,065 | 2,687 | 4,752 | 1,744 | 13.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 38 | L1-worker | claudeopus46 | 2,065 | 519 | 2,584 | 1,265 | 8.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 39 | L1-worker | claudeopus46 | 20,643 | 200,499 | 221,142 | 3,664 | 24.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 40 | L1-worker | claudeopus46 | 536 | 2,795 | 3,331 | 712 | 4.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 41 | L1-worker | claudeopus46 | 1,356 | 2,915 | 4,271 | 1,006 | 5.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 42 | L1-worker | claudeopus46 | 1,323 | 12,536 | 13,859 | 5,484 | 23.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 43 | L1-worker | claudeopus46 | 298 | 6,206 | 6,504 | 4,512 | 18.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 44 | L1-worker | claudeopus46 | 747 | 104,103 | 104,850 | 820 | 8.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 45 | L1-worker | claudeopus46 | 20,643 | 290,952 | 311,595 | 1,862 | 14.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 46 | L1-worker | claudeopus46 | 20,643 | 291,902 | 312,545 | 13,560 | 64.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 47 | L1-worker | claudeopus46 | 2,065 | 1,672 | 3,737 | 1,937 | 11.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 48 | L1-worker | claudeopus46 | 20,643 | 293,281 | 313,924 | 13,131 | 62.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 49 | L1-worker | claudeopus46 | 2,065 | 8,415 | 10,480 | 1,571 | 13.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 50 | L1-worker | claudeopus46 | 20,610 | 295,966 | 316,576 | 471 | 5.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 51 | L1-worker | claudeopus46 | 20,643 | 295,213 | 315,856 | 5,252 | 30.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 52 | L1-worker | claudeopus46 | 1,356 | 4,397 | 5,753 | 1,083 | 5.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 53 | L1-worker | claudeopus46 | 536 | 4,277 | 4,813 | 819 | 6.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 54 | L1-worker | claudeopus46 | 298 | 1,465 | 1,763 | 1,071 | 3.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 55 | L1-worker | claudeopus46 | 1,323 | 10,325 | 11,648 | 3,478 | 15.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 56 | L1-worker | claudeopus46 | 298 | 4,200 | 4,498 | 2,658 | 14.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 57 | L1-worker | claudeopus46 | 1,160 | 14,424 | 15,584 | 2,491 | 12.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 58 | L0-main | claudeopus46 | 9,605 | 293,752 | 303,357 | 7,296 | 47.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 59 | L0-main | claudeopus46 | 1,356 | 7,427 | 8,783 | 1,797 | 8.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 60 | L0-main | claudeopus46 | 298 | 2,179 | 2,477 | 1,737 | 7.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 61 | L0-main | claudeopus46 | 1,323 | 14,400 | 15,723 | 5,755 | 29.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 62 | L0-main | claudeopus46 | 298 | 6,423 | 6,721 | 4,865 | 23.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 1 | L0-main | claudeopus46 | 9,605 | 1,180 | 10,785 | 1,844 | 9.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,675 | 22,318 | 1,588 | 11.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 3 | L1-worker | claudeopus46 | 2,065 | 19,086 | 21,151 | 1,638 | 13.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 4 | L1-worker | claudeopus46 | 20,643 | 3,565 | 24,208 | 2,109 | 9.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 5 | L1-worker | claudeopus46 | 2,065 | 6,364 | 8,429 | 1,467 | 15.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 6 | L1-worker | claudeopus46 | 2,065 | 7,471 | 9,536 | 1,565 | 14.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 7 | L1-worker | claudeopus46 | 2,065 | 2,779 | 4,844 | 1,338 | 11.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 8 | L1-worker | claudeopus46 | 2,065 | 468 | 2,533 | 1,331 | 9.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 9 | L1-worker | claudeopus46 | 2,065 | 476 | 2,541 | 1,070 | 7.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 10 | L1-worker | claudeopus46 | 20,643 | 6,384 | 27,027 | 5,680 | 31.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 11 | L1-worker | claudeopus46 | 1,356 | 3,387 | 4,743 | 829 | 5.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 12 | L1-worker | claudeopus46 | 536 | 3,267 | 3,803 | 1,437 | 7.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 13 | L1-worker | claudeopus46 | 1,323 | 13,903 | 15,226 | 3,838 | 18.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 14 | L1-worker | claudeopus46 | 298 | 4,560 | 4,858 | 3,161 | 13.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 15 | L1-worker | claudeopus46 | 1,160 | 18,856 | 20,016 | 3,196 | 15.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 16 | L1-worker | claudeopus46 | 747 | 82,270 | 83,017 | 1,015 | 10.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 17 | L0-main | claudeopus46 | 9,605 | 2,836 | 12,441 | 14,559 | 64.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 18 | L1-worker | claudeopus46 | 20,643 | 1,106 | 21,749 | 890 | 6.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 19 | L1-worker | claudeopus46 | 2,065 | 6,435 | 8,500 | 1,464 | 12.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 20 | L1-worker | claudeopus46 | 20,643 | 2,778 | 23,421 | 3,298 | 17.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 21 | L1-worker | claudeopus46 | 1,356 | 2,336 | 3,692 | 754 | 4.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 22 | L1-worker | claudeopus46 | 536 | 2,216 | 2,752 | 854 | 5.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 23 | L1-worker | claudeopus46 | 298 | 1,136 | 1,434 | 742 | 3.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 24 | L1-worker | claudeopus46 | 298 | 1,210 | 1,508 | 841 | 6.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 25 | L1-worker | claudeopus46 | 1,323 | 5,028 | 6,351 | 3,010 | 12.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 26 | L1-worker | claudeopus46 | 298 | 3,732 | 4,030 | 2,289 | 10.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 27 | L1-worker | claudeopus46 | 747 | 48,310 | 49,057 | 654 | 5.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 28 | L1-worker | claudeopus46 | 1,160 | 9,008 | 10,168 | 2,354 | 11.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 29 | L1-worker | claudeopus46 | 747 | 48,375 | 49,122 | 625 | 6.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 30 | L1-worker | claudeopus46 | 20,643 | 45,744 | 66,387 | 798 | 6.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 31 | L1-worker | claudeopus46 | 2,065 | 7,547 | 9,612 | 1,671 | 16.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 32 | L1-worker | claudeopus46 | 20,643 | 47,677 | 68,320 | 1,910 | 12.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 33 | L1-worker | claudeopus46 | 1,356 | 1,841 | 3,197 | 925 | 5.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 34 | L1-worker | claudeopus46 | 536 | 1,721 | 2,257 | 823 | 5.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 35 | L1-worker | claudeopus46 | 1,323 | 4,860 | 6,183 | 1,746 | 8.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 36 | L1-worker | claudeopus46 | 298 | 2,468 | 2,766 | 1,421 | 5.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 37 | L1-worker | claudeopus46 | 747 | 25,092 | 25,839 | 526 | 6.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 38 | L0-main | claudeopus46 | 9,605 | 70,457 | 80,062 | 2,960 | 15.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 39 | L1-worker | claudeopus46 | 20,643 | 67,270 | 87,913 | 816 | 7.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 40 | L1-worker | claudeopus46 | 2,065 | 2,871 | 4,936 | 1,105 | 9.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 41 | L1-worker | claudeopus46 | 20,643 | 68,691 | 89,334 | 1,331 | 9.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 42 | L1-worker | claudeopus46 | 1,323 | 3,980 | 5,303 | 684 | 4.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 43 | L1-worker | claudeopus46 | 536 | 1,340 | 1,876 | 865 | 5.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 44 | L1-worker | claudeopus46 | 298 | 1,406 | 1,704 | 557 | 3.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 45 | L1-worker | claudeopus46 | 1,356 | 1,460 | 2,816 | 726 | 9.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 46 | L1-worker | claudeopus46 | 747 | 11,252 | 11,999 | 630 | 6.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 47 | L1-worker | claudeopus46 | 20,643 | 75,841 | 96,484 | 843 | 9.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 48 | L1-worker | claudeopus46 | 2,065 | 520 | 2,585 | 1,678 | 12.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 49 | L1-worker | claudeopus46 | 20,643 | 76,966 | 97,609 | 1,120 | 7.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 50 | L1-worker | claudeopus46 | 2,065 | 9,589 | 11,654 | 1,961 | 16.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 51 | L1-worker | claudeopus46 | 20,643 | 78,756 | 99,399 | 2,443 | 13.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 52 | L1-worker | claudeopus46 | 1,356 | 2,161 | 3,517 | 743 | 4.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 53 | L1-worker | claudeopus46 | 536 | 2,041 | 2,577 | 1,067 | 5.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 54 | L1-worker | claudeopus46 | 1,323 | 6,047 | 7,370 | 1,889 | 9.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 55 | L1-worker | claudeopus46 | 298 | 2,611 | 2,909 | 1,426 | 8.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 56 | L1-worker | claudeopus46 | 747 | 32,147 | 32,894 | 553 | 6.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 57 | L1-worker | claudeopus46 | 20,643 | 103,286 | 123,929 | 1,324 | 9.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 58 | L1-worker | claudeopus46 | 20,643 | 105,338 | 125,981 | 14,920 | 59.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 59 | L1-worker | claudeopus46 | 2,065 | 406 | 2,471 | 490 | 4.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 60 | L1-worker | claudeopus46 | 2,065 | 498 | 2,563 | 1,348 | 9.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 61 | L1-worker | claudeopus46 | 20,643 | 106,565 | 127,208 | 10,308 | 56.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 62 | L1-worker | claudeopus46 | 2,065 | 494 | 2,559 | 1,330 | 8.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 63 | L1-worker | claudeopus46 | 2,065 | 553 | 2,618 | 1,617 | 10.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 64 | L1-worker | claudeopus46 | 20,610 | 109,551 | 130,161 | 577 | 7.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 65 | L1-worker | claudeopus46 | 20,643 | 108,798 | 129,441 | 3,151 | 17.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 66 | L1-worker | claudeopus46 | 2,065 | 453 | 2,518 | 985 | 7.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 67 | L1-worker | claudeopus46 | 2,065 | 449 | 2,514 | 960 | 9.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 68 | L1-worker | claudeopus46 | 20,643 | 111,080 | 131,723 | 760 | 8.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 69 | L1-worker | claudeopus46 | 1,356 | 891 | 2,247 | 403 | 3.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 70 | L1-worker | claudeopus46 | 536 | 771 | 1,307 | 490 | 3.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 71 | L1-worker | claudeopus46 | 1,323 | 9,288 | 10,611 | 92 | 4.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 72 | L1-worker | claudeopus46 | 298 | 814 | 1,112 | 67 | 2.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 73 | L1-worker | claudeopus46 | 747 | 9,809 | 10,556 | 494 | 4.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 74 | L0-main | claudeopus46 | 9,605 | 110,457 | 120,062 | 7,012 | 46.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 75 | L0-main | claudeopus46 | 1,356 | 6,456 | 7,812 | 1,421 | 9.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 76 | L0-main | claudeopus46 | 298 | 1,803 | 2,101 | 1,409 | 8.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 77 | L0-main | claudeopus46 | 1,323 | 48,989 | 50,312 | 6,926 | 36.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 78 | L0-main | claudeopus46 | 298 | 7,594 | 7,892 | 5,869 | 25.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 1 | L0-main | claudeopus46 | 9,605 | 1,178 | 10,783 | 20,661 | 81.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 2 | L0-main | claudeopus46 | 9,605 | 3,430 | 13,035 | 2,505 | 11.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 3 | L1-worker | claudeopus46 | 20,643 | 2,042 | 22,685 | 1,557 | 8.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 4 | L1-worker | claudeopus46 | 2,065 | 7,782 | 9,847 | 1,743 | 14.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 5 | L1-worker | claudeopus46 | 2,065 | 2,742 | 4,807 | 1,628 | 11.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 6 | L1-worker | claudeopus46 | 2,065 | 2,482 | 4,547 | 1,624 | 12.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 7 | L1-worker | claudeopus46 | 20,643 | 6,354 | 26,997 | 1,294 | 8.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 8 | L1-worker | claudeopus46 | 2,065 | 472 | 2,537 | 1,122 | 7.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 9 | L1-worker | claudeopus46 | 2,065 | 480 | 2,545 | 1,052 | 7.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 10 | L1-worker | claudeopus46 | 20,643 | 8,558 | 29,201 | 4,276 | 27.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 11 | L1-worker | claudeopus46 | 1,356 | 3,279 | 4,635 | 955 | 5.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 12 | L1-worker | claudeopus46 | 536 | 3,159 | 3,695 | 967 | 6.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 13 | L1-worker | claudeopus46 | 1,323 | 11,986 | 13,309 | 2,569 | 16.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 14 | L1-worker | claudeopus46 | 298 | 3,291 | 3,589 | 2,128 | 10.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 15 | L1-worker | claudeopus46 | 747 | 55,333 | 56,080 | 521 | 5.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 16 | L1-worker | claudeopus46 | 1,160 | 15,672 | 16,832 | 2,128 | 10.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 17 | L1-worker | claudeopus46 | 747 | 55,333 | 56,080 | 679 | 7.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 18 | L0-main | claudeopus46 | 9,605 | 5,915 | 15,520 | 2,584 | 12.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 19 | L1-worker | claudeopus46 | 20,643 | 1,555 | 22,198 | 709 | 5.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 20 | L1-worker | claudeopus46 | 2,065 | 7,825 | 9,890 | 1,826 | 15.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 21 | L1-worker | claudeopus46 | 20,643 | 3,130 | 23,773 | 1,264 | 10.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 22 | L1-worker | claudeopus46 | 2,065 | 9,793 | 11,858 | 1,730 | 15.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 23 | L1-worker | claudeopus46 | 20,643 | 4,741 | 25,384 | 2,418 | 19.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 24 | L1-worker | claudeopus46 | 20,643 | 5,611 | 26,254 | 2,550 | 17.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 25 | L1-worker | claudeopus46 | 20,643 | 6,470 | 27,113 | 2,105 | 17.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 26 | L1-worker | claudeopus46 | 2,065 | 7,836 | 9,901 | 1,636 | 13.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 27 | L1-worker | claudeopus46 | 20,643 | 7,251 | 27,894 | 4,893 | 32.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 28 | L1-worker | claudeopus46 | 536 | 2,737 | 3,273 | 932 | 5.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 29 | L1-worker | claudeopus46 | 1,356 | 2,857 | 4,213 | 791 | 5.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 30 | L1-worker | claudeopus46 | 1,323 | 11,217 | 12,540 | 2,906 | 13.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 31 | L1-worker | claudeopus46 | 298 | 3,628 | 3,926 | 2,284 | 13.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 32 | L1-worker | claudeopus46 | 747 | 49,882 | 50,629 | 711 | 7.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 33 | L1-worker | claudeopus46 | 1,160 | 15,122 | 16,282 | 2,241 | 10.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 34 | L1-worker | claudeopus46 | 747 | 49,839 | 50,586 | 621 | 7.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 35 | L1-worker | claudeopus46 | 20,643 | 1,575 | 22,218 | 751 | 5.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 36 | L1-worker | claudeopus46 | 2,065 | 2,793 | 4,858 | 1,564 | 12.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 37 | L1-worker | claudeopus46 | 20,643 | 3,392 | 24,035 | 2,385 | 15.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 38 | L1-worker | claudeopus46 | 1,323 | 5,080 | 6,403 | 617 | 6.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 39 | L1-worker | claudeopus46 | 1,356 | 2,095 | 3,451 | 729 | 7.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 40 | L1-worker | claudeopus46 | 536 | 1,975 | 2,511 | 713 | 7.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 41 | L1-worker | claudeopus46 | 298 | 1,339 | 1,637 | 490 | 3.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 42 | L1-worker | claudeopus46 | 298 | 1,111 | 1,409 | 717 | 3.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 43 | L1-worker | claudeopus46 | 747 | 13,288 | 14,035 | 712 | 7.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 44 | L1-worker | claudeopus46 | 20,643 | 11,145 | 31,788 | 782 | 6.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 45 | L1-worker | claudeopus46 | 2,065 | 2,563 | 4,628 | 1,633 | 11.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 46 | L1-worker | claudeopus46 | 20,643 | 12,827 | 33,470 | 1,942 | 12.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 47 | L1-worker | claudeopus46 | 1,323 | 4,955 | 6,278 | 589 | 3.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 48 | L1-worker | claudeopus46 | 1,356 | 2,073 | 3,429 | 872 | 4.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 49 | L1-worker | claudeopus46 | 536 | 1,953 | 2,489 | 676 | 5.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 50 | L1-worker | claudeopus46 | 298 | 1,311 | 1,609 | 462 | 3.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 51 | L1-worker | claudeopus46 | 747 | 12,640 | 13,387 | 499 | 5.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 52 | L0-main | claudeopus46 | 9,605 | 26,358 | 35,963 | 3,172 | 16.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 53 | L1-worker | claudeopus46 | 20,643 | 20,387 | 41,030 | 696 | 5.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 54 | L1-worker | claudeopus46 | 2,065 | 7,834 | 9,899 | 1,689 | 14.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 55 | L1-worker | claudeopus46 | 20,643 | 21,991 | 42,634 | 936 | 7.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 56 | L1-worker | claudeopus46 | 2,065 | 9,796 | 11,861 | 1,672 | 16.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 57 | L1-worker | claudeopus46 | 20,643 | 23,718 | 44,361 | 2,746 | 17.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 58 | L1-worker | claudeopus46 | 2,065 | 9,766 | 11,831 | 1,406 | 15.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 59 | L1-worker | claudeopus46 | 20,610 | 26,341 | 46,951 | 392 | 5.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 60 | L1-worker | claudeopus46 | 20,643 | 25,588 | 46,231 | 2,742 | 21.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 61 | L1-worker | claudeopus46 | 2,065 | 7,902 | 9,967 | 1,587 | 12.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 62 | L1-worker | claudeopus46 | 20,643 | 26,536 | 47,179 | 2,361 | 15.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 63 | L1-worker | claudeopus46 | 2,065 | 2,864 | 4,929 | 1,735 | 13.8 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 64 | L1-worker | claudeopus46 | 20,643 | 28,245 | 48,888 | 1,866 | 15.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 65 | L1-worker | claudeopus46 | 2,065 | 2,703 | 4,768 | 1,895 | 14.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 66 | L1-worker | claudeopus46 | 20,610 | 30,590 | 51,200 | 343 | 5.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 67 | L1-worker | claudeopus46 | 20,643 | 29,835 | 50,478 | 878 | 6.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 68 | L1-worker | claudeopus46 | 2,065 | 2,739 | 4,804 | 1,756 | 12.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 69 | L1-worker | claudeopus46 | 20,643 | 31,479 | 52,122 | 717 | 5.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 70 | L1-worker | claudeopus46 | 2,065 | 2,669 | 4,734 | 1,779 | 12.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 71 | L1-worker | claudeopus46 | 20,643 | 33,302 | 53,945 | 4,154 | 29.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 72 | L1-worker | claudeopus46 | 1,356 | 2,699 | 4,055 | 938 | 6.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 73 | L1-worker | claudeopus46 | 536 | 2,579 | 3,115 | 1,256 | 8.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 74 | L1-worker | claudeopus46 | 298 | 1,320 | 1,618 | 926 | 3.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 75 | L1-worker | claudeopus46 | 1,323 | 16,817 | 18,140 | 4,062 | 20.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 76 | L1-worker | claudeopus46 | 298 | 4,784 | 5,082 | 3,385 | 15.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 77 | L1-worker | claudeopus46 | 1,160 | 21,824 | 22,984 | 3,054 | 14.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 78 | L1-worker | claudeopus46 | 747 | 78,638 | 79,385 | 754 | 7.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 79 | L1-worker | claudeopus46 | 20,643 | 20,129 | 40,772 | 724 | 5.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 80 | L1-worker | claudeopus46 | 2,065 | 498 | 2,563 | 905 | 7.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 81 | L1-worker | claudeopus46 | 20,643 | 21,306 | 41,949 | 769 | 6.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 82 | L1-worker | claudeopus46 | 2,065 | 409 | 2,474 | 865 | 6.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 83 | L1-worker | claudeopus46 | 20,643 | 22,506 | 43,149 | 2,205 | 15.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 84 | L1-worker | claudeopus46 | 2,065 | 493 | 2,558 | 1,209 | 10.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 85 | L1-worker | claudeopus46 | 20,610 | 24,652 | 45,262 | 604 | 6.6 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 86 | L1-worker | claudeopus46 | 20,643 | 23,899 | 44,542 | 793 | 6.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 87 | L1-worker | claudeopus46 | 1,356 | 924 | 2,280 | 355 | 3.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 88 | L1-worker | claudeopus46 | 1,323 | 5,411 | 6,734 | 92 | 3.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 89 | L1-worker | claudeopus46 | 536 | 804 | 1,340 | 534 | 4.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 90 | L1-worker | claudeopus46 | 298 | 814 | 1,112 | 67 | 3.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 91 | L1-worker | claudeopus46 | 747 | 6,023 | 6,770 | 475 | 6.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 92 | L1-worker | claudeopus46 | 20,643 | 22,038 | 42,681 | 797 | 6.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 93 | L1-worker | claudeopus46 | 2,065 | 527 | 2,592 | 954 | 6.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 94 | L1-worker | claudeopus46 | 20,643 | 23,301 | 43,944 | 1,158 | 7.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 95 | L1-worker | claudeopus46 | 2,065 | 14,148 | 16,213 | 1,562 | 13.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 96 | L1-worker | claudeopus46 | 2,065 | 9,701 | 11,766 | 1,753 | 13.5 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 97 | L1-worker | claudeopus46 | 20,643 | 26,849 | 47,492 | 2,783 | 15.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 98 | L1-worker | claudeopus46 | 536 | 1,712 | 2,248 | 740 | 7.9 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 99 | L1-worker | claudeopus46 | 1,356 | 1,832 | 3,188 | 613 | 8.1 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 100 | L1-worker | claudeopus46 | 1,323 | 7,786 | 9,109 | 92 | 10.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 101 | L1-worker | claudeopus46 | 298 | 814 | 1,112 | 67 | 6.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 102 | L1-worker | claudeopus46 | 747 | 9,770 | 10,517 | 588 | 5.2 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 103 | L0-main | claudeopus46 | 9,572 | 9,405 | 18,977 | 4,704 | 27.3 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 104 | L0-main | claudeopus46 | 1,356 | 3,856 | 5,212 | 946 | 5.4 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 105 | L0-main | claudeopus46 | 1,323 | 42,032 | 43,355 | 2,845 | 17.7 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 106 | L0-main | claudeopus46 | 298 | 3,513 | 3,811 | 2,393 | 9.0 | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| **TOTAL** |  |  | **1,743,431** | **6,499,322** | **8,242,753** | **554,626** | **3,360.6** |  |


## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| 1 | interval=3 | skipped_by_agent | 10,459 | 10,459 | 0 | 0.0% | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 2 | interval=3 | skipped_by_agent | 5,123 | 5,123 | 0 | 0.0% | Search for binary mixture data blocks containing water (GLOB (query_runs/run_2) |
| 1 | interval=3 | skipped_by_agent | 6,151 | 6,151 | 0 | 0.0% | Search for binary mixture data blocks containing water (GLOB (query_runs/run_4) |
| 1 | interval=3 | skipped_by_agent | 6,036 | 6,036 | 0 | 0.0% | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 2 | interval=3 | skipped_by_agent | 10,208 | 10,208 | 0 | 0.0% | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| 3 | interval=3 | skipped_by_agent | 4,347 | 4,347 | 0 | 0.0% | Search for binary mixture data blocks containing water (GLOB (query_runs/run_3) |
| **TOTAL** |  |  | **42,324** | **42,324** | **0** | **0** |  |
