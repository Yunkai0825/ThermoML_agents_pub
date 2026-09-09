# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 6 | 22,485 | 94,167 | 37,086 | 116,652 | 19,442 | 190.0 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| L1-worker | 16 | 118,065 | 151,070 | 51,060 | 269,135 | 16,820 | 273.0 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| L0-main | 6 | 22,485 | 111,419 | 18,400 | 133,904 | 22,317 | 103.9 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| L1-worker | 16 | 118,065 | 173,562 | 50,405 | 291,627 | 18,226 | 269.3 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| L0-main | 9 | 51,300 | 320,420 | 39,297 | 371,720 | 41,302 | 201.4 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| L1-worker | 64 | 460,609 | 1,409,333 | 123,282 | 1,869,942 | 29,217 | 684.9 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| L0-main | 10 | 60,905 | 160,782 | 23,348 | 221,687 | 22,168 | 142.0 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| L1-worker | 65 | 542,700 | 730,215 | 174,485 | 1,272,915 | 19,583 | 876.5 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| L0-main | 6 | 22,485 | 109,743 | 17,986 | 132,228 | 22,038 | 103.8 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| L1-worker | 16 | 118,098 | 200,775 | 64,179 | 318,873 | 19,929 | 331.3 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| L0-main | 10 | 60,905 | 245,212 | 26,961 | 306,117 | 30,611 | 157.1 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| L1-worker | 75 | 472,846 | 730,255 | 118,244 | 1,203,101 | 16,041 | 670.6 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| L0-main | 9 | 51,300 | 380,176 | 32,031 | 431,476 | 47,941 | 178.8 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| L1-worker | 66 | 480,186 | 2,046,459 | 199,829 | 2,526,645 | 38,282 | 974.9 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| L0-main | 8 | 41,695 | 245,861 | 38,131 | 287,556 | 35,944 | 205.7 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| L1-worker | 61 | 462,662 | 1,031,689 | 138,915 | 1,494,351 | 24,497 | 830.5 | claudeopus46 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| **TOTAL** | **443** | **3,106,791** | **8,141,138** | **1,153,639** | **11,247,929** | **424,358** | **6,193.7** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `resolve_compound_ids` | 5 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 4 | 2 | 9 | 9 | 484 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 3 | 1 | 3 | 3 | 171 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 363 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| `search_blocks` | 2 | 1 | 4 | 2 | 13 | 13 | 574 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| `search_blocks` | 2 | 1 | 3 | 2 | 5 | 5 | 193 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| `search_blocks` | 2 | 2 | 1 | 3 | 2 | 2 | 8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| `resolve_compound_ids` | 5 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| `search_blocks` | 2 | 1 | 4 | 3 | 16 | 16 | 908 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| `search_blocks` | 2 | 1 | 3 | 2 | 7 | 7 | 302 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 35 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| `search_blocks` | 2 | 1 | 4 | 3 | 16 | 16 | 908 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| `search_system_registry` | 2 | 1 | 4 | 3 | 16 | 16 | 908 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| `search_blocks` | 2 | 2 | 4 | 2 | 11 | 12 | 1,157 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 28 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| `search_blocks` | 2 | 2 | 4 | 2 | 11 | 12 | 1,157 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 76 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| `search_blocks` | 2 | 1 | 7 | 3 | 17 | 18 | 1,610 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| `search_blocks` | 2 | 1 | 5 | 1 | 6 | 6 | 232 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| `search_blocks` | 2 | 1 | 1 | 2 | 1 | 1 | 14 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `resolve_property_ids` | 0 | 5 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `search_blocks` | 2 | 16 | 5 | 4 | 20 | 30 | 712 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `search_blocks` | 2 | 1 | 4 | 2 | 5 | 5 | 182 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 80 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `search_blocks` | 2 | 1 | 2 | 2 | 1 | 1 | 100 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `search_blocks` | 2 | 1 | 2 | 2 | 1 | 1 | 100 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| `search_blocks` | 2 | 1 | 6 | 3 | 14 | 14 | 534 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| `search_system_registry` | 2 | 1 | 6 | 3 | 14 | 14 | 534 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| `search_blocks` | 2 | 1 | 6 | 5 | 27 | 29 | 2,895 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| `search_system_registry` | 2 | 1 | 6 | 5 | 27 | 29 | 2,895 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| `resolve_compound_ids` | 10 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `resolve_property_ids` | 0 | 6 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `search_blocks` | 2 | 15 | 5 | 5 | 18 | 34 | 1,780 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `search_blocks` | 2 | 1 | 3 | 2 | 4 | 4 | 264 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `search_blocks` | 2 | 1 | 4 | 3 | 10 | 10 | 611 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `search_system_registry` | 2 | 1 | 4 | 3 | 10 | 10 | 611 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `search_blocks` | 2 | 1 | 4 | 2 | 7 | 7 | 493 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `search_blocks` | 2 | 1 | 4 | 3 | 10 | 10 | 611 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 28 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `search_blocks` | 2 | 1 | 4 | 3 | 10 | 10 | 611 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `search_system_registry` | 2 | 1 | 4 | 3 | 10 | 10 | 611 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `search_blocks` | 2 | 1 | 4 | 3 | 10 | 10 | 611 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| **TOTAL** | **112** | **118** | **140** | **92** | **348** | **381** | **24,472** |  |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | --- | --- |
| Unique Compounds | 5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| Unique Properties | 5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| Unique References | 10 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| Unique Measurements | 10 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| Unique Phases | 1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| Unique Variables | 4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| Unique Constraints | 2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| Unique Solvents | 1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| Unique parent blocks | 13 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| Explicit block/subsystem targets | 13 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| Subsystem targets | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| Target-matched data points | 1,018 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_18 |  | resolve_compound_ids, search_blocks |
| GLOBprop_42 |  | resolve_property_ids, search_blocks |
| GLOBprop_44 |  | resolve_property_ids, search_blocks |
| GLOBprop_33 |  | resolve_property_ids |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBlit_1540 |  | search_blocks |
| GLOBlit_2584 |  | search_blocks |
| GLOBlit_2736 |  | search_blocks |
| GLOBlit_2834 |  | search_blocks |
| GLOBlit_3614 |  | search_blocks |
| GLOBlit_4166 |  | search_blocks |
| GLOBlit_4174 |  | search_blocks |
| GLOBlit_4340 |  | search_blocks |
| GLOBlit_8676 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9342 |  | search_blocks |
| GLOBlit_9855 |  | search_blocks |
| GLOBlit_11030 |  | search_blocks |
| GLOBlit_9900 |  | search_blocks |
| GLOBlit_11207 |  | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_147 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_167 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_567 | Relative permittivity at various frequencies | search_blocks |
| GLOBmeas_53 | Relative permittivity at zero frequency | search_blocks |
| GLOBphase_1 |  | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |
| GLOBsolvent_4 |  | search_blocks |
| Unique Compounds | 2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| Unique Properties | 5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| Unique References | 15 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| Unique Measurements | 9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| Unique Phases | 1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| Unique Variables | 4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| Unique Constraints | 3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| Unique Solvents | 1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| Unique parent blocks | 20 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| Explicit block/subsystem targets | 20 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| Subsystem targets | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| Target-matched data points | 775 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_151 |  | resolve_compound_ids |
| GLOBcomp_234 |  | resolve_compound_ids |
| GLOBcomp_770 |  | resolve_compound_ids |
| GLOBcomp_863 |  | resolve_compound_ids |
| GLOBcomp_24 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBprop_42 |  | resolve_property_ids |
| GLOBprop_44 |  | resolve_property_ids, search_blocks |
| GLOBprop_33 |  | resolve_property_ids |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBlit_1223 |  | search_blocks, search_system_registry |
| GLOBlit_2268 |  | search_blocks, search_system_registry |
| GLOBlit_2656 |  | search_blocks, search_system_registry |
| GLOBlit_2831 |  | search_blocks, search_system_registry |
| GLOBlit_5201 |  | search_blocks, search_system_registry |
| GLOBlit_5254 |  | search_blocks, search_system_registry |
| GLOBlit_5274 |  | search_blocks, search_system_registry |
| GLOBlit_6630 |  | search_blocks, search_system_registry |
| GLOBlit_6686 |  | search_blocks, search_system_registry |
| GLOBlit_6951 |  | search_blocks, search_system_registry |
| GLOBlit_7228 |  | search_blocks, search_system_registry |
| GLOBlit_7440 |  | search_blocks, search_system_registry |
| GLOBlit_8038 |  | search_blocks, search_system_registry |
| GLOBlit_8106 |  | search_blocks, search_system_registry |
| GLOBlit_10102 |  | search_blocks, search_system_registry |
| GLOBlit_11506 |  | search_blocks, search_system_registry |
| GLOBlit_11186 |  | search_blocks |
| GLOBlit_8736 |  | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_143 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_212 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_184 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_227 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_46 | Relative permittivity at zero frequency | search_blocks |
| GLOBphase_1 |  | search_blocks, search_system_registry |
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks, search_system_registry |
| GLOBsolvent_12 |  | search_blocks, search_system_registry |
| GLOBsolvent_1 |  | search_blocks, search_system_registry |
| GLOBblocktype_1 |  | search_system_registry |
| Unique Compounds | 6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| Unique Properties | 5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| Unique References | 18 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| Unique Measurements | 11 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| Unique Phases | 1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| Unique Variables | 5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| Unique Constraints | 3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| Unique Solvents | 2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| Unique Block_Types | 1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| Unique parent blocks | 24 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| Explicit block/subsystem targets | 24 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| Subsystem targets | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| Target-matched data points | 3,061 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_58 |  | resolve_compound_ids, search_blocks |
| GLOBprop_42 |  | resolve_property_ids |
| GLOBprop_44 |  | resolve_property_ids, search_blocks |
| GLOBprop_33 |  | resolve_property_ids |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBlit_2738 |  | search_blocks |
| GLOBlit_2979 |  | search_blocks |
| GLOBlit_4204 |  | search_blocks |
| GLOBlit_4631 |  | search_blocks |
| GLOBlit_4951 |  | search_blocks |
| GLOBlit_5201 |  | search_blocks |
| GLOBlit_5254 |  | search_blocks |
| GLOBlit_5288 |  | search_blocks |
| GLOBlit_6107 |  | search_blocks |
| GLOBlit_6811 |  | search_blocks |
| GLOBlit_9758 |  | search_blocks |
| GLOBlit_8736 |  | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_46 | Relative permittivity at zero frequency | search_blocks |
| GLOBphase_1 |  | search_blocks |
| GLOBsolvent_1 |  | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| Unique Compounds | 2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| Unique Properties | 5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| Unique References | 12 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| Unique Measurements | 5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| Unique Phases | 1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| Unique Solvents | 1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| Unique Variables | 5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| Unique Constraints | 2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| Unique parent blocks | 13 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| Explicit block/subsystem targets | 13 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| Subsystem targets | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| Target-matched data points | 3,499 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_4 |  | resolve_compound_ids, search_blocks |
| GLOBprop_42 |  | resolve_property_ids |
| GLOBprop_44 |  | resolve_property_ids, search_blocks |
| GLOBprop_33 |  | resolve_property_ids |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBlit_385 |  | search_blocks |
| GLOBlit_462 |  | search_blocks |
| GLOBlit_895 |  | search_blocks |
| GLOBlit_1742 |  | search_blocks |
| GLOBlit_2092 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_5533 |  | search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_7629 |  | search_blocks |
| GLOBlit_8155 |  | search_blocks |
| GLOBlit_8254 |  | search_blocks |
| GLOBlit_8424 |  | search_blocks |
| GLOBlit_8869 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9571 |  | search_blocks |
| GLOBlit_10866 |  | search_blocks |
| GLOBlit_3697 |  | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_1494 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_280 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_2135 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_271 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_53 | Relative permittivity at zero frequency | search_blocks |
| GLOBphase_10 |  | search_blocks |
| GLOBphase_1 |  | search_blocks |
| GLOBphase_3 |  | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_15 | Mass ratio of solute to solvent | search_blocks |
| GLOBvar_18 | Volume fraction | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_3 |  | search_blocks |
| Unique Compounds | 2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| Unique Properties | 5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| Unique References | 18 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| Unique Measurements | 13 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| Unique Phases | 3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| Unique Variables | 7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| Unique Constraints | 3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| Unique Solvents | 2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| Unique parent blocks | 25 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| Explicit block/subsystem targets | 25 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| Subsystem targets | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| Target-matched data points | 1,856 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_15 |  | resolve_compound_ids, search_blocks |
| GLOBprop_42 |  | resolve_property_ids, search_blocks |
| GLOBprop_44 |  | resolve_property_ids |
| GLOBprop_33 |  | resolve_property_ids |
| GLOBprop_1 |  | resolve_property_ids, search_blocks |
| GLOBprop_4 |  | resolve_property_ids, search_blocks |
| GLOBprop_3 | Activity coefficient | search_blocks |
| GLOBprop_28 | Excess molar volume, m3/mol | search_blocks |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks |
| GLOBprop_14 | Boiling temperature at pressure P, K | search_blocks |
| GLOBprop_2 | Mole fraction | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBprop_9 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBprop_15 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBprop_55 | Henry's Law constant (molality scale), kPa*kg/mol | search_blocks |
| GLOBprop_58 | Azeotropic temperature, K | search_blocks |
| GLOBprop_45 | Azeotropic composition: mole fraction | search_blocks |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBlit_664 |  | search_blocks |
| GLOBlit_1014 |  | search_blocks |
| GLOBlit_1333 |  | search_blocks |
| GLOBlit_1501 |  | search_blocks |
| GLOBlit_2602 |  | search_blocks |
| GLOBlit_2736 |  | search_blocks |
| GLOBlit_3240 |  | search_blocks |
| GLOBlit_3286 |  | search_blocks |
| GLOBlit_5572 |  | search_blocks |
| GLOBlit_5714 |  | search_blocks |
| GLOBlit_5904 |  | search_blocks |
| GLOBlit_7312 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9129 |  | search_blocks |
| GLOBlit_10006 |  | search_blocks |
| GLOBlit_10193 |  | search_blocks |
| GLOBlit_10215 |  | search_blocks |
| GLOBlit_10747 |  | search_blocks |
| GLOBlit_11018 |  | search_blocks |
| GLOBlit_11299 |  | search_blocks |
| GLOBmeas_289 | Activity coefficient | search_blocks |
| GLOBmeas_29 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks |
| GLOBmeas_5 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_1 | Mole fraction | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_147 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_311 | Speed of sound, m/s | search_blocks |
| GLOBmeas_167 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_17 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_19 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_144 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_967 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_15 | Speed of sound, m/s | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_39 | Azeotropic temperature, K | search_blocks |
| GLOBmeas_53 | Relative permittivity at various frequencies | search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |
| GLOBphase_1 |  | search_blocks |
| GLOBphase_3 |  | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_5 |  | search_blocks |
| Unique Compounds | 2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| Unique Properties | 18 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| Unique References | 20 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| Unique Measurements | 19 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| Unique Phases | 2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| Unique Constraints | 4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| Unique Variables | 5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| Unique Solvents | 2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| Unique parent blocks | 30 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| Explicit block/subsystem targets | 30 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| Subsystem targets | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| Target-matched data points | 1,174 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBprop_4 |  | resolve_property_ids, search_blocks, search_system_registry |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBprop_42 |  | resolve_property_ids |
| GLOBprop_44 |  | resolve_property_ids |
| GLOBprop_33 |  | resolve_property_ids |
| GLOBlit_1742 |  | search_blocks, search_system_registry |
| GLOBlit_2092 |  | search_blocks, search_system_registry |
| GLOBlit_2825 |  | search_blocks, search_system_registry |
| GLOBlit_5201 |  | search_blocks, search_system_registry |
| GLOBlit_7178 |  | search_blocks, search_system_registry |
| GLOBlit_7448 |  | search_blocks, search_system_registry |
| GLOBlit_7676 |  | search_blocks, search_system_registry |
| GLOBlit_8949 |  | search_blocks, search_system_registry |
| GLOBlit_10159 |  | search_blocks, search_system_registry |
| GLOBlit_10699 |  | search_blocks, search_system_registry |
| GLOBlit_11005 |  | search_blocks, search_system_registry |
| GLOBlit_11136 |  | search_blocks, search_system_registry |
| GLOBlit_11459 |  | search_blocks, search_system_registry |
| GLOBlit_11792 |  | search_blocks, search_system_registry |
| GLOBlit_220 |  | search_blocks, search_system_registry |
| GLOBlit_1483 |  | search_blocks, search_system_registry |
| GLOBlit_2432 |  | search_blocks, search_system_registry |
| GLOBlit_2732 |  | search_blocks, search_system_registry |
| GLOBlit_3475 |  | search_blocks, search_system_registry |
| GLOBlit_4415 |  | search_blocks, search_system_registry |
| GLOBlit_5473 |  | search_blocks, search_system_registry |
| GLOBlit_7085 |  | search_blocks, search_system_registry |
| GLOBlit_7629 |  | search_blocks, search_system_registry |
| GLOBlit_8050 |  | search_blocks, search_system_registry |
| GLOBlit_8888 |  | search_blocks, search_system_registry |
| GLOBlit_9006 |  | search_blocks, search_system_registry |
| GLOBlit_10866 |  | search_blocks, search_system_registry |
| GLOBlit_11504 |  | search_blocks, search_system_registry |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_988 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_142 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_1497 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_236 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_203 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_212 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBphase_1 |  | search_blocks, search_system_registry |
| GLOBphase_3 |  | search_blocks, search_system_registry |
| GLOBphase_10 |  | search_blocks, search_system_registry |
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBvar_18 | Volume fraction | search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBvar_15 | Mass ratio of solute to solvent | search_blocks, search_system_registry |
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_8 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks, search_system_registry |
| GLOBconstr_3 | Mole fraction | search_blocks, search_system_registry |
| GLOBconstr_22 | Volume fraction | search_blocks, search_system_registry |
| GLOBsolvent_1 |  | search_blocks, search_system_registry |
| GLOBsolvent_2 |  | search_blocks, search_system_registry |
| GLOBblocktype_1 |  | search_system_registry |
| Unique Compounds | 2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| Unique Properties | 5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| Unique References | 28 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| Unique Measurements | 19 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| Unique Phases | 3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| Unique Variables | 7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| Unique Constraints | 5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| Unique Solvents | 2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| Unique Block_Types | 1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| Unique parent blocks | 43 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| Explicit block/subsystem targets | 43 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| Subsystem targets | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| Target-matched data points | 6,858 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_61 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_2199 |  | resolve_compound_ids |
| GLOBcomp_5558 |  | resolve_compound_ids |
| GLOBcomp_113 |  | resolve_compound_ids |
| GLOBcomp_111 |  | resolve_compound_ids |
| GLOBcomp_251 |  | resolve_compound_ids |
| GLOBcomp_1741 |  | resolve_compound_ids |
| GLOBcomp_5309 |  | resolve_compound_ids |
| GLOBcomp_167 |  | resolve_compound_ids |
| GLOBprop_1 |  | resolve_property_ids, search_blocks, search_system_registry |
| GLOBprop_4 |  | resolve_property_ids, search_blocks |
| GLOBprop_40 |  | resolve_property_ids |
| GLOBprop_42 |  | resolve_property_ids |
| GLOBprop_44 |  | resolve_property_ids, search_blocks |
| GLOBprop_33 |  | resolve_property_ids |
| GLOBprop_28 | Excess molar volume, m3/mol | search_blocks |
| GLOBprop_85 | Excess molar heat capacity, J/K/mol | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBprop_17 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBprop_84 | Partial molar volume, m3/mol | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBprop_9 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBprop_34 | Thermal conductivity, W/m/K | search_blocks |
| GLOBprop_11 | Solid-liquid equilibrium temperature, K | search_blocks |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBprop_74 | Specific volume, m3/kg | search_blocks |
| GLOBlit_1283 |  | search_blocks |
| GLOBlit_1623 |  | search_blocks, search_system_registry |
| GLOBlit_2574 |  | search_blocks |
| GLOBlit_2605 |  | search_blocks |
| GLOBlit_2831 |  | search_blocks, search_system_registry |
| GLOBlit_2979 |  | search_blocks, search_system_registry |
| GLOBlit_3180 |  | search_blocks, search_system_registry |
| GLOBlit_5233 |  | search_blocks, search_system_registry |
| GLOBlit_5826 |  | search_blocks |
| GLOBlit_5907 |  | search_blocks |
| GLOBlit_6775 |  | search_blocks, search_system_registry |
| GLOBlit_7545 |  | search_blocks, search_system_registry |
| GLOBlit_8239 |  | search_blocks, search_system_registry |
| GLOBlit_8556 |  | search_blocks, search_system_registry |
| GLOBlit_8686 |  | search_blocks |
| GLOBlit_9758 |  | search_blocks, search_system_registry |
| GLOBlit_10313 |  | search_blocks |
| GLOBlit_11906 |  | search_blocks |
| GLOBmeas_29 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_9 | Excess molar heat capacity, J/K/mol | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_192 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_169 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_1187 | Partial molar volume, m3/mol | search_blocks |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_132 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_193 | Thermal conductivity, W/m/K | search_blocks |
| GLOBmeas_33 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_17 | Molar heat capacity at constant pressure, J/K/mol | search_blocks |
| GLOBmeas_130 | Solid-liquid equilibrium temperature, K | search_blocks |
| GLOBmeas_20 | Speed of sound, m/s | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_194 | Speed of sound, m/s | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_41 | Thermal conductivity, W/m/K | search_blocks |
| GLOBmeas_1716 | Relative permittivity at zero frequency | search_blocks |
| GLOBmeas_171 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_65 | Specific volume, m3/kg | search_blocks |
| GLOBphase_1 |  | search_blocks, search_system_registry |
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks, search_system_registry |
| GLOBconstr_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBconstr_22 | Volume fraction | search_blocks |
| GLOBsolvent_23 |  | search_blocks, search_system_registry |
| GLOBsolvent_1 |  | search_blocks, search_system_registry |
| GLOBblocktype_1 |  | search_system_registry |
| Unique Compounds | 10 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| Unique Properties | 18 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| Unique References | 18 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| Unique Measurements | 25 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| Unique Phases | 1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| Unique Variables | 5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| Unique Constraints | 5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| Unique Solvents | 2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| Unique Block_Types | 1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| Unique parent blocks | 34 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| Explicit block/subsystem targets | 34 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| Subsystem targets | 0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| Target-matched data points | 6,231 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| **TOTAL** | **25,321** |  |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 10.1016/j.jct.2005.07.012 | PROPblock_8 | declared | 96 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 10.1016/j.jct.2006.01.007 | PROPblock_4 | declared | 6 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 10.1016/j.jct.2006.12.012 | PROPblock_3 | declared | 120 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 10.1016/j.jct.2006.12.012 | PROPblock_4 | declared | 120 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 10.1016/j.jct.2007.06.007 | PROPblock_6 | declared | 40 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 10.1016/j.jct.2007.06.010 | PROPblock_4 | declared | 92 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 10.1016/j.tca.2011.08.013 | PROPblock_10 | declared | 16 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 10.1016/j.tca.2011.08.013 | PROPblock_12 | declared | 16 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 10.1021/acs.jced.8b01048 | PROPblock_10 | declared | 9 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 10.1021/je400149j | PROPblock_5 | declared | 363 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 10.1021/je700645p | PROPblock_6 | declared | 70 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 10.1021/je9001027 | PROPblock_3 | declared | 35 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 10.1021/je9001027 | PROPblock_4 | declared | 35 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 10.1016/j.fluid.2014.08.026 | 2 | 9 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1016/j.jct.2005.07.012 | 1 | 128 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1016/j.jct.2006.08.007 | 1 | 9 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1016/j.jct.2007.05.015 | 1 | 40 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1016/j.jct.2012.04.007 | 1 | 55 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1016/j.jct.2014.05.003 | 2 | 6 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1016/j.jct.2014.05.013 | 1 | 18 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1016/j.jct.2015.03.012 | 1 | 6 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1021/je050209y | 2 | 22 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1021/je0601098 | 1 | 14 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1021/je1008813 | 2 | 32 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1021/je300358u | 1 | 60 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1021/je300608v | 1 | 60 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1021/je700671t | 2 | 308 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1021/je800330d | 1 | 8 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |  |  |
| 10.1016/j.fluid.2014.08.026 | PROPblock_5 | declared | 4 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1016/j.fluid.2014.08.026 | PROPblock_6 | declared | 5 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1016/j.jct.2005.07.012 | PROPblock_9 | declared | 128 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1016/j.jct.2006.08.007 | PROPblock_2 | declared | 9 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1016/j.jct.2007.05.015 | PROPblock_18 | declared | 40 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1016/j.jct.2012.04.007 | PROPblock_3 | declared | 55 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1016/j.jct.2014.05.003 | PROPblock_1 | declared | 3 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1016/j.jct.2014.05.003 | PROPblock_2 | declared | 3 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1016/j.jct.2014.05.013 | PROPblock_19 | declared | 18 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1016/j.jct.2015.03.012 | PROPblock_2 | declared | 6 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1021/je050209y | PROPblock_10 | declared | 11 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1021/je050209y | PROPblock_9 | declared | 11 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1021/je0601098 | PROPblock_30 | declared | 14 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1021/je1008813 | PROPblock_3 | declared | 16 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1021/je1008813 | PROPblock_4 | declared | 16 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1021/je300358u | PROPblock_3 | declared | 60 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1021/je300608v | PROPblock_3 | declared | 60 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1021/je700671t | PROPblock_3 | declared | 98 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1021/je700671t | PROPblock_4 | declared | 210 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1021/je800330d | PROPblock_3 | declared | 8 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10.1016/j.fluid.2013.01.025 | 1 | 85 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1016/j.fluid.2018.11.035 | 1 | 6 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1016/j.jct.2006.01.011 | 2 | 20 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1016/j.jct.2007.05.010 | 1 | 10 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1016/j.jct.2018.02.022 | 2 | 308 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1016/j.jct.2018.05.016 | 1 | 12 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1016/j.jct.2018.06.021 | 1 | 15 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1021/acs.jced.5b00498 | 1 | 70 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1021/acs.jced.5b00662 | 1 | 30 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1021/acs.jced.6b00526 | 2 | 166 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1021/acs.jced.7b00501 | 1 | 32 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1021/acs.jced.8b00058 | 1 | 20 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1021/je020140j | 2 | 154 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1021/je025610o | 2 | 60 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1021/je050353j | 1 | 35 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1021/je4001203 | 1 | 138 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1021/je800271e | 1 | 52 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1021/je9000697 | 2 | 32 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |  |  |
| 10.1016/j.fluid.2013.01.025 | PROPblock_2 | declared | 85 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1016/j.fluid.2018.11.035 | PROPblock_2 | declared | 6 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1016/j.jct.2006.01.011 | PROPblock_12 | declared | 10 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1016/j.jct.2006.01.011 | PROPblock_13 | declared | 10 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1016/j.jct.2007.05.010 | PROPblock_10 | declared | 10 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1016/j.jct.2018.02.022 | PROPblock_22 | declared | 224 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1016/j.jct.2018.02.022 | PROPblock_24 | declared | 84 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1016/j.jct.2018.05.016 | PROPblock_7 | declared | 12 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1016/j.jct.2018.06.021 | PROPblock_10 | declared | 15 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/acs.jced.5b00498 | PROPblock_1 | declared | 70 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/acs.jced.5b00662 | PROPblock_55 | declared | 30 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/acs.jced.6b00526 | PROPblock_16 | declared | 133 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/acs.jced.6b00526 | PROPblock_18 | declared | 33 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/acs.jced.7b00501 | PROPblock_9 | declared | 32 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/acs.jced.8b00058 | PROPblock_9 | declared | 20 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/je020140j | PROPblock_4 | declared | 77 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/je020140j | PROPblock_5 | declared | 77 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/je025610o | PROPblock_5 | declared | 30 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/je025610o | PROPblock_6 | declared | 30 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/je050353j | PROPblock_3 | declared | 35 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/je4001203 | PROPblock_1 | declared | 138 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/je800271e | PROPblock_4 | declared | 52 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/je9000697 | PROPblock_1 | declared | 16 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1021/je9000697 | PROPblock_2 | declared | 16 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10.1016/j.jct.2006.08.009 | 1 | 99 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |  |  |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |  |  |
| 10.1016/j.jct.2014.06.031 | 1 | 85 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |  |  |
| 10.1016/j.jct.2016.02.026 | 1 | 7 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |  |  |
| 10.1016/j.jct.2017.01.011 | 1 | 44 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |  |  |
| 10.1016/j.jct.2018.02.022 | 2 | 212 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |  |  |
| 10.1016/j.jct.2018.05.016 | 1 | 16 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |  |  |
| 10.1016/j.jct.2018.07.015 | 1 | 20 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |  |  |
| 10.1016/j.tca.2013.07.012 | 1 | 296 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |  |  |
| 10.1021/acs.jced.5b01080 | 1 | 175 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |  |  |
| 10.1021/je050353j | 1 | 28 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |  |  |
| 10.1021/je201184b | 1 | 107 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |  |  |
| 10.1016/j.jct.2006.08.009 | PROPblock_6 | declared | 99 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10.1016/j.jct.2008.07.005 | PROPblock_8 | declared | 96 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10.1016/j.jct.2014.06.031 | PROPblock_5 | declared | 85 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10.1016/j.jct.2016.02.026 | PROPblock_17 | declared | 7 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10.1016/j.jct.2017.01.011 | PROPblock_3 | declared | 44 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10.1016/j.jct.2018.02.022 | PROPblock_31 | declared | 136 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10.1016/j.jct.2018.02.022 | PROPblock_33 | declared | 76 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10.1016/j.jct.2018.05.016 | PROPblock_9 | declared | 16 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10.1016/j.jct.2018.07.015 | PROPblock_1 | declared | 20 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10.1016/j.tca.2013.07.012 | PROPblock_3 | declared | 296 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10.1021/acs.jced.5b01080 | PROPblock_15 | declared | 175 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10.1021/je050353j | PROPblock_4 | declared | 28 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10.1021/je201184b | PROPblock_6 | declared | 107 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10.1016/j.fluid.2006.05.007 | 1 | 45 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1016/j.fluid.2006.12.005 | 2 | 10 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1016/j.fluid.2010.10.005 | 1 | 34 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1016/j.fluid.2015.07.012 | 2 | 164 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1016/j.fluid.2017.09.005 | 2 | 144 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1016/j.jct.2004.07.019 | 1 | 596 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1016/j.jct.2007.05.004 | 2 | 78 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1016/j.jct.2012.08.009 | 1 | 14 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1016/j.jct.2019.05.013 | 2 | 24 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1021/acs.jced.8b00723 | 1 | 3 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1021/je0301500 | 1 | 5 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1021/je034101z | 1 | 401 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1021/je049691v | 1 | 180 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1021/je0600810 | 2 | 18 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1021/je2003622 | 2 | 32 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |  |  |
| 10.1016/j.fluid.2006.05.007 | PROPblock_1 | declared | 45 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1016/j.fluid.2006.12.005 | PROPblock_3 | declared | 8 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1016/j.fluid.2006.12.005 | PROPblock_4 | declared | 2 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1016/j.fluid.2010.10.005 | PROPblock_1 | declared | 34 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_1 | declared | 80 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_2 | declared | 84 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_1 | declared | 72 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_2 | declared | 72 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1016/j.jct.2007.05.004 | PROPblock_9 | declared | 39 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1016/j.jct.2012.08.009 | PROPblock_17 | declared | 14 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1016/j.jct.2019.05.013 | PROPblock_2 | declared | 12 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1016/j.jct.2019.05.013 | PROPblock_3 | declared | 12 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1021/acs.jced.8b00723 | PROPblock_10 | declared | 3 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1021/je0301500 | PROPblock_13 | declared | 5 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1021/je0600810 | PROPblock_3 | declared | 9 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1021/je2003622 | PROPblock_1 | declared | 16 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10.1016/j.fluid.2008.09.011 | 2 | 3 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1016/j.fluid.2011.09.016 | 1 | 6 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1016/j.fluid.2013.09.028 | 1 | 2 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1016/j.fluid.2014.06.025 | 2 | 18 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1016/j.jct.2005.08.009 | 2 | 155 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1016/j.jct.2006.08.007 | 2 | 20 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1016/j.jct.2010.04.019 | 1 | 116 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1016/j.jct.2010.09.003 | 1 | 57 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1016/j.jct.2019.07.006 | 2 | 28 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1016/j.tca.2006.06.021 | 1 | 1 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1016/j.tca.2010.09.013 | 1 | 1 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1021/acs.jced.7b00755 | 2 | 10 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1021/je0601098 | 2 | 26 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1021/je1001329 | 1 | 12 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1021/je3010535 | 1 | 7 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1021/je400473z | 1 | 9 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1021/je400531a | 4 | 44 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1021/je700055p | 1 | 100 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1021/je700645p | 1 | 75 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1021/je800557h | 1 | 22 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |  |  |
| 10.1016/j.fluid.2008.09.011 | PROPblock_1 | declared | 2 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.fluid.2008.09.011 | PROPblock_2 | declared | 1 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.fluid.2011.09.016 | PROPblock_1 | declared | 6 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.fluid.2013.09.028 | PROPblock_19 | declared | 2 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.fluid.2014.06.025 | PROPblock_1 | declared | 9 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.fluid.2014.06.025 | PROPblock_2 | declared | 9 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.jct.2005.08.009 | PROPblock_3 | declared | 80 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.jct.2005.08.009 | PROPblock_4 | declared | 75 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.jct.2006.08.007 | PROPblock_5 | declared | 10 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.jct.2006.08.007 | PROPblock_6 | declared | 10 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.jct.2010.04.019 | PROPblock_1 | declared | 116 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.jct.2010.09.003 | PROPblock_6 | declared | 57 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.jct.2019.07.006 | PROPblock_3 | declared | 14 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.jct.2019.07.006 | PROPblock_4 | declared | 14 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.tca.2006.06.021 | PROPblock_1 | declared | 1 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.tca.2010.09.013 | PROPblock_2 | declared | 1 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1021/acs.jced.7b00755 | PROPblock_4 | declared | 5 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1021/acs.jced.7b00755 | PROPblock_5 | declared | 5 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1021/je0601098 | PROPblock_25 | declared | 13 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1021/je0601098 | PROPblock_26 | declared | 13 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1021/je1001329 | PROPblock_4 | declared | 12 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1021/je3010535 | PROPblock_13 | declared | 7 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1021/je400473z | PROPblock_1 | declared | 9 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1021/je400531a | PROPblock_10 | declared | 21 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1021/je400531a | PROPblock_11 | declared | 21 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1021/je400531a | PROPblock_12 | declared | 1 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1021/je400531a | PROPblock_13 | declared | 1 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1021/je700055p | PROPblock_2 | declared | 100 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1021/je700645p | PROPblock_5 | declared | 75 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1021/je800557h | PROPblock_5 | declared | 22 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1016/j.fluid.2015.07.012 | 2 | 168 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1016/j.fluid.2017.09.005 | 2 | 144 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1016/j.jct.2004.07.019 | 1 | 565 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1016/j.jct.2006.08.002 | 3 | 301 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1016/j.jct.2007.05.004 | 2 | 74 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1016/j.jct.2015.06.024 | 1 | 40 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1016/j.jct.2018.02.022 | 2 | 344 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/acs.jced.7b00299 | 2 | 4 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/acs.jced.8b00086 | 2 | 12 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/acs.jced.8b00723 | 1 | 3 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/acs.jced.8b00939 | 2 | 18 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/je020173z | 1 | 24 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/je060219e | 1 | 26 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/je060335h | 1 | 164 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/je4003515 | 2 | 48 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/je600565m | 2 | 35 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/je700618y | 2 | 30 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/je800150h | 2 | 216 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/je800942u | 2 | 36 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/je900064e | 1 | 10 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1021/je900743e | 2 | 30 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |  |  |
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_3 | declared | 84 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_4 | declared | 84 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_3 | declared | 72 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_4 | declared | 72 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.jct.2006.08.002 | PROPblock_2 | declared | 19 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.jct.2006.08.002 | PROPblock_3 | declared | 4 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.jct.2006.08.002 | PROPblock_4 | declared | 278 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.jct.2018.02.022 | PROPblock_21 | declared | 100 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/acs.jced.7b00299 | PROPblock_11 | declared | 2 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | declared | 6 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/acs.jced.8b00723 | PROPblock_12 | declared | 3 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/acs.jced.8b00939 | PROPblock_18 | declared | 9 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je060219e | PROPblock_1 | declared | 26 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je4003515 | PROPblock_8 | declared | 25 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je600565m | PROPblock_5 | declared | 17 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je700618y | PROPblock_7 | declared | 15 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je800150h | PROPblock_8 | declared | 108 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je800942u | PROPblock_5 | declared | 18 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je800942u | PROPblock_6 | declared | 18 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je900064e | PROPblock_6 | declared | 10 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je900743e | PROPblock_2 | declared | 15 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1021/je900743e | PROPblock_3 | declared | 15 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10.1016/j.fluid.2013.06.041 | 2 | 185 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1016/j.fluid.2014.12.040 | 2 | 168 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1016/j.jct.2005.06.018 | 1 | 36 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1016/j.jct.2005.08.015 | 1 | 33 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1016/j.jct.2007.05.010 | 2 | 16 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1016/j.jct.2009.11.018 | 2 | 28 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1016/j.jct.2018.04.007 | 4 | 16 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1016/j.tca.2009.01.008 | 1 | 30 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1016/j.tca.2010.10.012 | 1 | 5 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1021/acs.jced.5b00964 | 2 | 39 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1021/acs.jced.8b00403 | 3 | 291 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1021/je0340755 | 3 | 375 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1021/je049960h | 3 | 84 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1021/je050237g | 1 | 28 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1021/je201184b | 2 | 212 | binary | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1021/je4009014 | 1 | 73 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1021/je9010568 | 2 | 65 | binary | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |  |  |
| 10.1016/j.fluid.2013.06.041 | PROPblock_13 | declared | 100 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.fluid.2013.06.041 | PROPblock_14 | declared | 85 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.fluid.2014.12.040 | PROPblock_10 | declared | 84 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.fluid.2014.12.040 | PROPblock_9 | declared | 84 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.jct.2005.06.018 | PROPblock_1 | declared | 36 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.jct.2005.08.015 | PROPblock_2 | declared | 33 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.jct.2007.05.010 | PROPblock_11 | declared | 8 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.jct.2007.05.010 | PROPblock_12 | declared | 8 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.jct.2008.07.005 | PROPblock_6 | declared | 96 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.jct.2009.11.018 | PROPblock_5 | declared | 14 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.jct.2009.11.018 | PROPblock_6 | declared | 14 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.jct.2018.04.007 | PROPblock_1 | declared | 4 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.jct.2018.04.007 | PROPblock_2 | declared | 4 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.jct.2018.04.007 | PROPblock_3 | declared | 4 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.jct.2018.04.007 | PROPblock_4 | declared | 4 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.tca.2009.01.008 | PROPblock_9 | declared | 30 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1016/j.tca.2010.10.012 | PROPblock_2 | declared | 5 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/acs.jced.5b00964 | PROPblock_15 | declared | 36 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/acs.jced.5b00964 | PROPblock_16 | declared | 3 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/acs.jced.8b00403 | PROPblock_13 | declared | 105 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/acs.jced.8b00403 | PROPblock_14 | declared | 105 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/acs.jced.8b00403 | PROPblock_15 | declared | 81 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/je0340755 | PROPblock_28 | declared | 125 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/je0340755 | PROPblock_29 | declared | 125 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/je0340755 | PROPblock_30 | declared | 125 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/je049960h | PROPblock_10 | declared | 21 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/je049960h | PROPblock_11 | declared | 30 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/je049960h | PROPblock_12 | declared | 33 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/je050237g | PROPblock_1 | declared | 28 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/je201184b | PROPblock_1 | declared | 106 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/je201184b | PROPblock_2 | declared | 106 | binary | 2 | search_blocks, search_system_registry | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/je4009014 | PROPblock_5 | declared | 73 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/je9010568 | PROPblock_7 | declared | 44 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10.1021/je9010568 | PROPblock_8 | declared | 21 | binary | — | search_blocks | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| **TOTAL** | **189** | **10,982** | **12,000** |  | **138** |  |  |


## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | ---: | ---: | --- |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 300 | KEEP | 300 | 6.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 2 | 2 | `resolve_property_ids` | limit=5, min_score=50, purpose=Resolve property ID… | 456 | KEEP | 456 | 8.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 3 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,227 | KEEP | 1122 | 22.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 4 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,444 | KEEP | 1413 | 15.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 5 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_31'], limit=50, … | 1,240 | KEEP | 1208 | 27.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 6 | 1 | `L1_query` | context=Looking for solvent property …, id_catalog… | 270 | — | — | 279.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve global comp… | 335 | KEEP | 335 | 5.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 2 | 2 | `resolve_property_ids` | limit=5, min_score=50, purpose=Resolve property ID… | 446 | KEEP | 446 | 6.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 3 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_18'], limit=50, … | 1,287 | KEEP | 1182 | 25.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 4 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_18'], limit=50, … | 1,263 | KEEP | 1263 | 23.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 5 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_18'], limit=50, … | 1,088 | KEEP | 1028 | 20.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 6 | 1 | `L1_query` | context=User is designing Fe electrod…, id_catalog… | 270 | — | — | 278.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 488 | KEEP | 488 | 8.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 2 | 2 | `resolve_property_ids` | limit=10, min_score=50, purpose=Resolve property I… | 493 | KEEP | 493 | 6.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 3 | 1 | `L1_query` | context=Looking for viscosity, dielec…, id_catalog… | 415 | — | — | 212.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 4 | 1 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve global comp… | 254 | KEEP | 254 | 4.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 5 | 2 | `L1_query` | context=Need compound IDs before sear…, id_catalog… | 1,383 | — | — | 24.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 6 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,190 | KEEP | 1100 | 24.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 7 | 3 | `L1_query` | context=Looking for density data in w…, id_catalog… | 270 | — | — | 83.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 8 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,370 | KEEP | 1263 | 23.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 9 | 3 | `L1_query` | context=Looking for viscosity data in…, id_catalog… | 270 | — | — | 82.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10 | 2 | `resolve_property_ids` | limit=10, min_score=40, purpose=Find the global pr… | 548 | KEEP | 548 | 7.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 11 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,166 | KEEP | 1136 | 22.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 12 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 906 | DISCARD | 848 | 19.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 13 | 3 | `L1_query` | context=Looking for dielectric consta…, id_catalog… | 10,590 | — | — | 116.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 14 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,105 | KEEP | 1090 | 22.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 15 | 3 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,246 | KEEP | 1020 | 10.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 16 | 4 | `L1_query` | context=Previous search found 16 tota…, id_catalog… | 270 | — | — | 131.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve global comp… | 329 | KEEP | 329 | 6.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 2 | 2 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find property ID f… | 417 | KEEP | 417 | 6.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 3 | 1 | `L1_query` | context=Looking for solvent property …, id_catalog… | 414 | — | — | 218.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 4 | 1 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve global comp… | 320 | KEEP | 320 | 5.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 5 | 2 | `L1_query` | context=Need to identify these compou…, id_catalog… | 1,634 | — | — | 28.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 6 | 3 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find the GLOBprop … | 386 | KEEP | 386 | 6.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 7 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,197 | KEEP | 1107 | 26.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 8 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,045 | KEEP | 1015 | 12.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 9 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,231 | KEEP | 1141 | 23.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10 | 3 | `L1_query` | context=Binary mixture search for wat…, id_catalog… | 420 | — | — | 354.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 11 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,188 | KEEP | 1158 | 24.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 12 | 4 | `L1_query` | context=Looking for density data in w…, id_catalog… | 270 | — | — | 133.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 13 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,215 | KEEP | 1185 | 21.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 14 | 5 | `L1_query` | context=Binary water+glycerol mixture…, id_catalog… | 9,460 | — | — | 62.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 15 | 3 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find GLOBprop_N ID… | 451 | KEEP | 451 | 6.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 16 | 5 | `L1_query` | context=Binary water+glycerol mixture…, id_catalog… | 1,984 | — | — | 59.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve compound ID… | 226 | KEEP | 226 | 4.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 2 | 2 | `resolve_property_ids` | limit=10, min_score=50, purpose=Resolve property I… | 633 | KEEP | 633 | 8.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 3 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 1,291 | KEEP | 1190 | 26.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 4 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 1,239 | KEEP | 1149 | 24.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 5 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 1,126 | KEEP | 1096 | 19.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 6 | 1 | `L1_query` | context=Looking for solvent property …, id_catalog… | 270 | — | — | 348.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 210 | KEEP | 210 | 4.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 2 | 2 | `resolve_property_ids` | limit=5, min_score=50, purpose=Resolve property ID… | 621 | KEEP | 621 | 7.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 3 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 826 | KEEP | 765 | 21.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 4 | 1 | `L1_query` | context=This is for Fe electrodeposit…, id_catalog… | 450 | — | — | 243.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 5 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Find GLOBcomp IDs f… | 203 | KEEP | 203 | 4.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 6 | 2 | `L1_query` | context=Need these IDs to then search…, id_catalog… | 1,404 | — | — | 27.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 7 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 1,270 | KEEP | 1270 | 22.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 8 | 3 | `L1_query` | context=Looking for solvent property …, id_catalog… | 270 | — | — | 66.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 9 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 1,208 | KEEP | 1178 | 23.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10 | 3 | `L1_query` | context=Looking for solvent property …, id_catalog… | 9,039 | — | — | 66.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 11 | 1 | `resolve_property_ids` | limit=10, min_score=40, purpose=Find GLOBprop_N fo… | 547 | KEEP | 547 | 8.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 12 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 803 | DISCARD | 745 | 7.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 13 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 1,282 | KEEP | 1250 | 13.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 14 | 3 | `L1_query` | context=Looking for dielectric consta…, id_catalog… | 645 | — | — | 100.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 15 | 1 | `resolve_property_ids` | limit=10, min_score=40, purpose=Find GLOBprop_N fo… | 498 | KEEP | 498 | 7.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 16 | 4 | `L1_query` | context=Need the property ID before s…, id_catalog… | 2,373 | — | — | 31.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 17 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 756 | DISCARD | 698 | 15.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 18 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_15'], limit=50, … | 1,228 | KEEP | 1196 | 14.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 19 | 5 | `L1_query` | context=Looking for dielectric consta…, id_catalog… | 11,517 | — | — | 98.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 1 | 1 | `L1_query` | context=This is for Fe electrodeposit…, id_catalog… | 416 | — | — | 216.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 2 | 1 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 285 | KEEP | 285 | 4.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 3 | 2 | `L1_query` | context=Need to identify these compou…, id_catalog… | 1,286 | — | — | 23.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 4 | 3 | `resolve_property_ids` | limit=5, min_score=50, purpose=Confirm GLOBprop_4 … | 285 | KEEP | 285 | 4.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 5 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,314 | KEEP | 1209 | 24.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 6 | 4 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,256 | KEEP | 1040 | 23.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 7 | 3 | `L1_query` | context=Looking for viscosity data in…, id_catalog… | 270 | — | — | 288.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 8 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,145 | KEEP | 1056 | 23.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 9 | 2 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=100, … | 1,235 | KEEP | 1041 | 22.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10 | 3 | `L1_query` | context=Looking for density data in w…, id_catalog… | 270 | — | — | 170.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 11 | 2 | `resolve_property_ids` | limit=10, min_score=40, purpose=Resolve the Thermo… | 555 | KEEP | 555 | 7.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 12 | 3 | `L1_query` | context=Looking for dielectric consta…, id_catalog… | 291 | — | — | 86.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 13 | 2 | `resolve_property_ids` | limit=10, min_score=40, purpose=Find the global pr… | 442 | KEEP | 442 | 7.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 14 | 4 | `L1_query` | context=Looking for dielectric consta…, id_catalog… | 1,211 | — | — | 140.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 1 | 2 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Resolve compound I… | 242 | KEEP | 242 | 5.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 2 | 2 | `resolve_property_ids` | limit=10, min_score=50, purpose=Resolve property I… | 726 | KEEP | 726 | 6.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 3 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=50, … | 701 | KEEP | 686 | 21.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 4 | 1 | `L1_query` | context=Looking for solvent property …, id_catalog… | 11,420 | — | — | 197.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 5 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=50, … | 1,366 | KEEP | 1366 | 23.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 6 | 2 | `L1_query` | context=Previous query found 4 blocks…, id_catalog… | 270 | — | — | 72.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 7 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=50, … | 1,091 | KEEP | 1091 | 15.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 8 | 3 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=20, … | 1,140 | KEEP | 1140 | 23.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 9 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=10, … | 557 | KEEP | 542 | 22.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=10, … | 345 | KEEP | 330 | 22.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 11 | 2 | `L1_query` | context=Previous query found 10 block…, id_catalog… | 204 | — | — | 334.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 12 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=50, … | 782 | DISCARD | 724 | 15.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 13 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=50, … | 766 | KEEP | 736 | 11.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 14 | 2 | `L1_query` | context=Previous query found 1 block …, id_catalog… | 9,183 | — | — | 70.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 15 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=50, … | 1,179 | KEEP | 1104 | 22.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 16 | 2 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=20, … | 1,060 | KEEP | 970 | 24.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 17 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_61'], limit=10, … | 1,044 | KEEP | 1044 | 22.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 18 | 3 | `L1_query` | context=Previous query found 10 densi…, id_catalog… | 270 | — | — | 169.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| **TOTAL** | **237** |  |  | **136,093** |  | **54,591** | **5,857.4** |  |


## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| 1 | interval=3 | skipped_by_agent | 8,035 | 8,035 | 0 | 0.0% | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 1 | interval=3 | skipped_by_agent | 7,970 | 7,970 | 0 | 0.0% | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 1 | interval=3 | skipped_by_agent | 5,507 | 5,507 | 0 | 0.0% | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 2 | interval=3 | skipped_by_agent | 5,250 | 5,250 | 0 | 0.0% | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 1 | interval=3 | skipped_by_agent | 5,201 | 5,201 | 0 | 0.0% | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 2 | interval=3 | skipped_by_agent | 2,687 | 2,687 | 0 | 0.0% | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 1 | interval=3 | skipped_by_agent | 4,960 | 4,960 | 0 | 0.0% | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 1 | interval=3 | skipped_by_agent | 4,986 | 4,986 | 0 | 0.0% | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 1 | interval=3 | skipped_by_agent | 5,033 | 5,033 | 0 | 0.0% | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 2 | interval=3 | skipped_by_agent | 5,231 | 5,231 | 0 | 0.0% | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 3 | interval=3 | skipped_by_agent | 5,645 | 5,645 | 0 | 0.0% | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| **TOTAL** |  |  | **60,505** | **60,505** | **0** | **0** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 9,605 | 978 | 10,583 | 17,317 | 80.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,235 | 21,878 | 994 | 6.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 3 | L1-worker | claudeopus46 | 20,643 | 2,957 | 23,600 | 15,376 | 59.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 4 | L1-worker | claudeopus46 | 2,065 | 749 | 2,814 | 586 | 5.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 5 | L1-worker | claudeopus46 | 2,065 | 669 | 2,734 | 1,085 | 8.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 6 | L1-worker | claudeopus46 | 20,643 | 3,748 | 24,391 | 11,254 | 49.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 7 | L1-worker | claudeopus46 | 2,065 | 6,411 | 8,476 | 1,433 | 13.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 8 | L1-worker | claudeopus46 | 2,065 | 7,521 | 9,586 | 1,768 | 15.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 9 | L1-worker | claudeopus46 | 2,065 | 3,849 | 5,914 | 1,658 | 16.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 10 | L1-worker | claudeopus46 | 20,610 | 9,330 | 29,940 | 381 | 5.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 11 | L1-worker | claudeopus46 | 20,643 | 8,577 | 29,220 | 4,915 | 32.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 12 | L1-worker | claudeopus46 | 1,356 | 3,508 | 4,864 | 1,001 | 6.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 13 | L1-worker | claudeopus46 | 536 | 3,388 | 3,924 | 1,030 | 7.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 14 | L1-worker | claudeopus46 | 298 | 1,383 | 1,681 | 989 | 3.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 15 | L1-worker | claudeopus46 | 1,323 | 12,101 | 13,424 | 4,220 | 18.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 16 | L1-worker | claudeopus46 | 298 | 4,942 | 5,240 | 3,384 | 14.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 17 | L1-worker | claudeopus46 | 747 | 80,702 | 81,449 | 986 | 10.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 18 | L0-main | claudeopus46 | 9,605 | 72,328 | 81,933 | 9,173 | 60.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 19 | L0-main | claudeopus46 | 1,356 | 6,036 | 7,392 | 1,351 | 7.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 20 | L0-main | claudeopus46 | 298 | 1,733 | 2,031 | 1,339 | 5.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 21 | L0-main | claudeopus46 | 1,323 | 8,125 | 9,448 | 4,299 | 22.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 22 | L0-main | claudeopus46 | 298 | 4,967 | 5,265 | 3,607 | 14.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_3) |
| 1 | L0-main | claudeopus46 | 9,605 | 979 | 10,584 | 1,563 | 8.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,350 | 21,993 | 1,070 | 6.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 3 | L1-worker | claudeopus46 | 20,643 | 3,148 | 23,791 | 14,686 | 52.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 4 | L1-worker | claudeopus46 | 2,065 | 490 | 2,555 | 562 | 4.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 5 | L1-worker | claudeopus46 | 2,065 | 669 | 2,734 | 1,031 | 6.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 6 | L1-worker | claudeopus46 | 20,643 | 3,963 | 24,606 | 9,984 | 50.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 7 | L1-worker | claudeopus46 | 2,065 | 8,667 | 10,732 | 1,588 | 16.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 8 | L1-worker | claudeopus46 | 2,065 | 7,520 | 9,585 | 1,633 | 13.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 9 | L1-worker | claudeopus46 | 2,065 | 3,890 | 5,955 | 1,496 | 11.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 10 | L1-worker | claudeopus46 | 20,610 | 9,265 | 29,875 | 471 | 5.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 11 | L1-worker | claudeopus46 | 20,643 | 8,512 | 29,155 | 3,728 | 25.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 12 | L1-worker | claudeopus46 | 536 | 3,739 | 4,275 | 981 | 7.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 13 | L1-worker | claudeopus46 | 1,356 | 3,859 | 5,215 | 1,093 | 7.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 14 | L1-worker | claudeopus46 | 298 | 1,475 | 1,773 | 1,081 | 6.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 15 | L1-worker | claudeopus46 | 1,323 | 12,254 | 13,577 | 5,620 | 24.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 16 | L1-worker | claudeopus46 | 298 | 6,342 | 6,640 | 4,607 | 19.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 17 | L1-worker | claudeopus46 | 747 | 98,419 | 99,166 | 774 | 10.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 18 | L0-main | claudeopus46 | 9,605 | 89,968 | 99,573 | 6,287 | 42.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 19 | L0-main | claudeopus46 | 1,356 | 5,876 | 7,232 | 1,458 | 9.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 20 | L0-main | claudeopus46 | 298 | 1,840 | 2,138 | 1,446 | 4.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 21 | L0-main | claudeopus46 | 1,323 | 8,081 | 9,404 | 4,007 | 22.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 22 | L0-main | claudeopus46 | 298 | 4,675 | 4,973 | 3,639 | 15.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_4) |
| 1 | L0-main | claudeopus46 | 9,605 | 979 | 10,584 | 1,417 | 8.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,254 | 21,897 | 1,000 | 5.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 3 | L1-worker | claudeopus46 | 20,643 | 2,982 | 23,625 | 15,932 | 62.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 4 | L1-worker | claudeopus46 | 2,065 | 645 | 2,710 | 1,004 | 7.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 5 | L1-worker | claudeopus46 | 2,065 | 646 | 2,711 | 1,083 | 6.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 6 | L1-worker | claudeopus46 | 20,643 | 3,990 | 24,633 | 11,966 | 53.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 7 | L1-worker | claudeopus46 | 20,643 | 16,577 | 37,220 | 3,706 | 15.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 8 | L1-worker | claudeopus46 | 1,356 | 3,837 | 5,193 | 907 | 5.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 9 | L1-worker | claudeopus46 | 536 | 3,717 | 4,253 | 903 | 6.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 10 | L1-worker | claudeopus46 | 298 | 1,289 | 1,587 | 867 | 3.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 11 | L1-worker | claudeopus46 | 1,323 | 7,506 | 8,829 | 5,979 | 22.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 12 | L1-worker | claudeopus46 | 298 | 6,701 | 6,999 | 4,906 | 17.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 13 | L1-worker | claudeopus46 | 1,160 | 14,925 | 16,085 | 4,789 | 18.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 14 | L0-main | claudeopus46 | 9,605 | 1,906 | 11,511 | 881 | 6.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 15 | L1-worker | claudeopus46 | 20,643 | 840 | 21,483 | 627 | 5.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 16 | L1-worker | claudeopus46 | 2,065 | 514 | 2,579 | 464 | 4.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 17 | L1-worker | claudeopus46 | 20,643 | 1,569 | 22,212 | 420 | 4.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 18 | L1-worker | claudeopus46 | 1,323 | 2,038 | 3,361 | 234 | 2.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 19 | L1-worker | claudeopus46 | 1,356 | 551 | 1,907 | 192 | 2.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 20 | L1-worker | claudeopus46 | 536 | 431 | 967 | 372 | 3.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 21 | L1-worker | claudeopus46 | 298 | 956 | 1,254 | 154 | 2.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 22 | L1-worker | claudeopus46 | 747 | 2,491 | 3,238 | 375 | 4.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 23 | L0-main | claudeopus46 | 9,605 | 5,346 | 14,951 | 3,729 | 17.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 24 | L1-worker | claudeopus46 | 20,643 | 2,882 | 23,525 | 745 | 7.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 25 | L1-worker | claudeopus46 | 2,065 | 11,226 | 13,291 | 1,615 | 14.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 26 | L1-worker | claudeopus46 | 20,643 | 4,546 | 25,189 | 3,662 | 20.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 27 | L1-worker | claudeopus46 | 1,356 | 2,466 | 3,822 | 978 | 5.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 28 | L1-worker | claudeopus46 | 536 | 2,346 | 2,882 | 820 | 6.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 29 | L1-worker | claudeopus46 | 298 | 1,360 | 1,658 | 966 | 4.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 30 | L1-worker | claudeopus46 | 1,323 | 5,454 | 6,777 | 2,622 | 11.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 31 | L1-worker | claudeopus46 | 298 | 3,344 | 3,642 | 2,240 | 9.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 32 | L1-worker | claudeopus46 | 747 | 43,286 | 44,033 | 845 | 8.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 33 | L1-worker | claudeopus46 | 20,643 | 42,293 | 62,936 | 1,091 | 7.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 34 | L1-worker | claudeopus46 | 2,065 | 10,481 | 12,546 | 1,648 | 13.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 35 | L1-worker | claudeopus46 | 20,643 | 44,208 | 64,851 | 3,398 | 20.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 36 | L1-worker | claudeopus46 | 536 | 2,934 | 3,470 | 1,256 | 6.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 37 | L1-worker | claudeopus46 | 1,356 | 3,054 | 4,410 | 1,347 | 7.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 38 | L1-worker | claudeopus46 | 298 | 1,729 | 2,027 | 1,335 | 4.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 39 | L1-worker | claudeopus46 | 1,323 | 6,352 | 7,675 | 3,233 | 12.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 40 | L1-worker | claudeopus46 | 298 | 3,955 | 4,253 | 2,512 | 11.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 41 | L1-worker | claudeopus46 | 747 | 50,551 | 51,298 | 559 | 6.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 42 | L1-worker | claudeopus46 | 20,643 | 88,121 | 108,764 | 705 | 5.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 43 | L1-worker | claudeopus46 | 20,643 | 89,447 | 110,090 | 1,085 | 6.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 44 | L1-worker | claudeopus46 | 2,065 | 679 | 2,744 | 1,194 | 7.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 45 | L1-worker | claudeopus46 | 20,643 | 89,919 | 110,562 | 3,168 | 15.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 46 | L1-worker | claudeopus46 | 2,065 | 3,380 | 5,445 | 1,562 | 13.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 47 | L1-worker | claudeopus46 | 2,065 | 570 | 2,635 | 1,345 | 12.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 48 | L1-worker | claudeopus46 | 20,610 | 93,514 | 114,124 | 500 | 5.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 49 | L1-worker | claudeopus46 | 20,643 | 92,761 | 113,404 | 2,279 | 14.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 50 | L1-worker | claudeopus46 | 1,356 | 2,126 | 3,482 | 895 | 5.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 51 | L1-worker | claudeopus46 | 1,323 | 7,835 | 9,158 | 1,004 | 7.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 52 | L1-worker | claudeopus46 | 536 | 2,006 | 2,542 | 915 | 7.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 53 | L1-worker | claudeopus46 | 298 | 1,271 | 1,569 | 902 | 3.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 54 | L1-worker | claudeopus46 | 298 | 1,726 | 2,024 | 822 | 4.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 55 | L1-worker | claudeopus46 | 747 | 16,926 | 17,673 | 594 | 7.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 56 | L0-main | claudeopus46 | 9,605 | 103,321 | 112,926 | 3,462 | 25.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 57 | L1-worker | claudeopus46 | 20,643 | 99,136 | 119,779 | 964 | 9.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 58 | L1-worker | claudeopus46 | 2,065 | 11,219 | 13,284 | 1,521 | 13.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 59 | L1-worker | claudeopus46 | 20,643 | 100,767 | 121,410 | 861 | 9.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 60 | L1-worker | claudeopus46 | 20,643 | 102,249 | 122,892 | 678 | 4.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 61 | L1-worker | claudeopus46 | 2,065 | 3,087 | 5,152 | 1,319 | 10.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 62 | L1-worker | claudeopus46 | 20,610 | 104,201 | 124,811 | 377 | 5.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 63 | L1-worker | claudeopus46 | 20,643 | 103,448 | 124,091 | 4,763 | 32.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 64 | L1-worker | claudeopus46 | 1,356 | 2,291 | 3,647 | 983 | 7.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 65 | L1-worker | claudeopus46 | 536 | 2,171 | 2,707 | 1,274 | 8.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 66 | L1-worker | claudeopus46 | 1,323 | 7,315 | 8,638 | 3,297 | 15.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 67 | L1-worker | claudeopus46 | 298 | 4,019 | 4,317 | 2,738 | 11.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 68 | L1-worker | claudeopus46 | 747 | 63,223 | 63,970 | 785 | 7.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 69 | L0-main | claudeopus46 | 9,605 | 161,993 | 171,598 | 6,915 | 49.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 70 | L0-main | claudeopus46 | 1,356 | 6,504 | 7,860 | 1,764 | 9.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 71 | L0-main | claudeopus46 | 298 | 2,146 | 2,444 | 1,714 | 5.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 72 | L0-main | claudeopus46 | 1,323 | 27,117 | 28,440 | 10,440 | 44.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 73 | L0-main | claudeopus46 | 298 | 11,108 | 11,406 | 8,975 | 34.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_1) |
| 1 | L0-main | claudeopus46 | 9,605 | 965 | 10,570 | 1,768 | 10.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,259 | 21,902 | 1,026 | 7.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 3 | L1-worker | claudeopus46 | 20,643 | 3,013 | 23,656 | 13,821 | 54.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 4 | L1-worker | claudeopus46 | 2,065 | 476 | 2,541 | 537 | 5.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 5 | L1-worker | claudeopus46 | 2,065 | 680 | 2,745 | 1,062 | 6.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 6 | L1-worker | claudeopus46 | 20,643 | 3,754 | 24,397 | 9,705 | 45.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 7 | L1-worker | claudeopus46 | 20,643 | 14,080 | 34,723 | 3,671 | 18.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 8 | L1-worker | claudeopus46 | 1,356 | 3,486 | 4,842 | 835 | 4.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 9 | L1-worker | claudeopus46 | 536 | 3,366 | 3,902 | 796 | 5.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 10 | L1-worker | claudeopus46 | 1,323 | 6,968 | 8,291 | 8,059 | 29.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 11 | L1-worker | claudeopus46 | 298 | 8,781 | 9,079 | 6,678 | 25.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 12 | L1-worker | claudeopus46 | 1,160 | 16,917 | 18,077 | 6,638 | 24.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 13 | L0-main | claudeopus46 | 9,605 | 1,914 | 11,519 | 964 | 7.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 14 | L1-worker | claudeopus46 | 20,643 | 894 | 21,537 | 587 | 5.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 15 | L1-worker | claudeopus46 | 2,065 | 501 | 2,566 | 555 | 5.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 16 | L1-worker | claudeopus46 | 20,643 | 1,685 | 22,328 | 713 | 5.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 17 | L1-worker | claudeopus46 | 1,323 | 2,282 | 3,605 | 234 | 3.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 18 | L1-worker | claudeopus46 | 536 | 573 | 1,109 | 248 | 3.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 19 | L1-worker | claudeopus46 | 1,356 | 693 | 2,049 | 418 | 3.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 20 | L1-worker | claudeopus46 | 298 | 956 | 1,254 | 154 | 3.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 21 | L1-worker | claudeopus46 | 747 | 2,932 | 3,679 | 365 | 4.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 22 | L0-main | claudeopus46 | 9,605 | 5,863 | 15,468 | 2,013 | 16.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 23 | L1-worker | claudeopus46 | 20,643 | 3,430 | 24,073 | 1,241 | 7.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 24 | L1-worker | claudeopus46 | 20,643 | 5,399 | 26,042 | 14,392 | 57.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 25 | L1-worker | claudeopus46 | 20,643 | 6,613 | 27,256 | 13,870 | 54.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 26 | L1-worker | claudeopus46 | 2,065 | 675 | 2,740 | 966 | 6.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 27 | L1-worker | claudeopus46 | 2,065 | 8,485 | 10,550 | 1,744 | 14.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 28 | L1-worker | claudeopus46 | 20,610 | 8,267 | 28,877 | 475 | 4.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 29 | L1-worker | claudeopus46 | 20,643 | 7,514 | 28,157 | 8,016 | 39.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 30 | L1-worker | claudeopus46 | 2,065 | 3,039 | 5,104 | 1,435 | 11.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 31 | L1-worker | claudeopus46 | 2,065 | 8,488 | 10,553 | 1,672 | 14.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 32 | L1-worker | claudeopus46 | 20,643 | 10,603 | 31,246 | 7,249 | 41.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 33 | L1-worker | claudeopus46 | 20,643 | 18,601 | 39,244 | 3,875 | 17.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 34 | L1-worker | claudeopus46 | 1,356 | 4,006 | 5,362 | 1,632 | 8.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 35 | L1-worker | claudeopus46 | 536 | 3,886 | 4,422 | 1,141 | 8.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 36 | L1-worker | claudeopus46 | 298 | 2,014 | 2,312 | 1,620 | 5.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 37 | L1-worker | claudeopus46 | 1,323 | 13,784 | 15,107 | 5,015 | 21.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 38 | L1-worker | claudeopus46 | 298 | 5,737 | 6,035 | 4,165 | 19.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 39 | L1-worker | claudeopus46 | 1,160 | 20,083 | 21,243 | 4,167 | 19.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 40 | L0-main | claudeopus46 | 9,605 | 6,915 | 16,520 | 1,350 | 10.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 41 | L1-worker | claudeopus46 | 20,643 | 2,966 | 23,609 | 854 | 6.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 42 | L1-worker | claudeopus46 | 20,643 | 4,441 | 25,084 | 14,106 | 49.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 43 | L1-worker | claudeopus46 | 2,065 | 7,924 | 9,989 | 1,752 | 14.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 44 | L1-worker | claudeopus46 | 20,643 | 5,602 | 26,245 | 3,913 | 22.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 45 | L1-worker | claudeopus46 | 1,356 | 2,481 | 3,837 | 882 | 4.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 46 | L1-worker | claudeopus46 | 536 | 2,361 | 2,897 | 725 | 5.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 47 | L1-worker | claudeopus46 | 1,323 | 5,636 | 6,959 | 2,715 | 12.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 48 | L1-worker | claudeopus46 | 298 | 3,437 | 3,735 | 2,093 | 9.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 49 | L1-worker | claudeopus46 | 747 | 43,567 | 44,314 | 898 | 9.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 50 | L0-main | claudeopus46 | 9,605 | 47,141 | 56,746 | 2,057 | 12.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 51 | L1-worker | claudeopus46 | 20,643 | 42,229 | 62,872 | 1,080 | 10.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 52 | L1-worker | claudeopus46 | 2,065 | 2,919 | 4,984 | 1,695 | 12.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 53 | L1-worker | claudeopus46 | 20,643 | 43,942 | 64,585 | 2,277 | 14.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 54 | L1-worker | claudeopus46 | 1,323 | 4,842 | 6,165 | 618 | 4.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 55 | L1-worker | claudeopus46 | 1,356 | 1,849 | 3,205 | 868 | 4.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 56 | L1-worker | claudeopus46 | 536 | 1,729 | 2,265 | 797 | 5.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 57 | L1-worker | claudeopus46 | 298 | 1,340 | 1,638 | 491 | 3.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 58 | L1-worker | claudeopus46 | 747 | 13,039 | 13,786 | 819 | 8.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 59 | L1-worker | claudeopus46 | 20,643 | 51,845 | 72,488 | 665 | 6.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 60 | L1-worker | claudeopus46 | 20,643 | 53,131 | 73,774 | 1,065 | 6.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 61 | L1-worker | claudeopus46 | 20,643 | 53,826 | 74,469 | 586 | 3.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 62 | L1-worker | claudeopus46 | 2,065 | 650 | 2,715 | 1,030 | 6.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 63 | L1-worker | claudeopus46 | 20,610 | 54,569 | 75,179 | 526 | 4.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 64 | L1-worker | claudeopus46 | 20,643 | 53,816 | 74,459 | 2,097 | 14.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 65 | L1-worker | claudeopus46 | 20,643 | 56,488 | 77,131 | 1,025 | 4.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 66 | L1-worker | claudeopus46 | 1,323 | 4,235 | 5,558 | 92 | 2.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 67 | L1-worker | claudeopus46 | 1,356 | 933 | 2,289 | 474 | 4.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 68 | L1-worker | claudeopus46 | 536 | 813 | 1,349 | 570 | 4.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 69 | L1-worker | claudeopus46 | 298 | 814 | 1,112 | 67 | 2.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 70 | L1-worker | claudeopus46 | 747 | 4,871 | 5,618 | 928 | 7.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 71 | L0-main | claudeopus46 | 9,605 | 60,309 | 69,914 | 4,727 | 33.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 72 | L0-main | claudeopus46 | 1,356 | 4,858 | 6,214 | 1,219 | 7.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 73 | L0-main | claudeopus46 | 298 | 1,601 | 1,899 | 1,207 | 4.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 74 | L0-main | claudeopus46 | 1,323 | 26,194 | 27,517 | 4,354 | 25.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 75 | L0-main | claudeopus46 | 298 | 5,022 | 5,320 | 3,689 | 15.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_2) |
| 1 | L0-main | claudeopus46 | 9,605 | 965 | 10,570 | 1,874 | 9.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,348 | 21,991 | 1,014 | 6.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 3 | L1-worker | claudeopus46 | 20,643 | 3,090 | 23,733 | 14,463 | 60.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 4 | L1-worker | claudeopus46 | 2,065 | 432 | 2,497 | 420 | 3.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 5 | L1-worker | claudeopus46 | 2,065 | 669 | 2,734 | 1,300 | 8.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 6 | L1-worker | claudeopus46 | 20,643 | 3,969 | 24,612 | 12,962 | 60.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 7 | L1-worker | claudeopus46 | 20,643 | 17,766 | 38,409 | 12,184 | 58.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 8 | L1-worker | claudeopus46 | 2,065 | 11,981 | 14,046 | 1,508 | 15.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 9 | L1-worker | claudeopus46 | 2,065 | 8,813 | 10,878 | 1,588 | 15.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 10 | L1-worker | claudeopus46 | 2,065 | 2,402 | 4,467 | 1,584 | 10.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 11 | L1-worker | claudeopus46 | 20,643 | 21,648 | 42,291 | 4,205 | 27.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 12 | L1-worker | claudeopus46 | 1,356 | 4,334 | 5,690 | 862 | 5.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 13 | L1-worker | claudeopus46 | 536 | 4,214 | 4,750 | 893 | 5.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 14 | L1-worker | claudeopus46 | 298 | 1,244 | 1,542 | 850 | 3.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 15 | L1-worker | claudeopus46 | 1,323 | 13,501 | 14,824 | 5,138 | 22.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 16 | L1-worker | claudeopus46 | 298 | 5,860 | 6,158 | 4,151 | 17.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 17 | L1-worker | claudeopus46 | 747 | 99,504 | 100,251 | 1,057 | 9.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 18 | L0-main | claudeopus46 | 9,605 | 89,648 | 99,253 | 5,625 | 39.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 19 | L0-main | claudeopus46 | 1,356 | 5,230 | 6,586 | 1,077 | 8.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 20 | L0-main | claudeopus46 | 298 | 1,459 | 1,757 | 1,065 | 4.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 21 | L0-main | claudeopus46 | 1,323 | 7,419 | 8,742 | 4,354 | 24.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 22 | L0-main | claudeopus46 | 298 | 5,022 | 5,320 | 3,991 | 17.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_5) |
| 1 | L0-main | claudeopus46 | 9,605 | 973 | 10,578 | 2,022 | 11.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,490 | 22,133 | 951 | 6.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 3 | L1-worker | claudeopus46 | 20,643 | 3,169 | 23,812 | 17,783 | 54.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 4 | L1-worker | claudeopus46 | 2,065 | 447 | 2,512 | 348 | 3.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 5 | L1-worker | claudeopus46 | 2,065 | 806 | 2,871 | 1,024 | 6.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 6 | L1-worker | claudeopus46 | 20,643 | 4,063 | 24,706 | 14,328 | 54.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 7 | L1-worker | claudeopus46 | 2,065 | 18,787 | 20,852 | 1,506 | 11.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 8 | L1-worker | claudeopus46 | 20,610 | 6,255 | 26,865 | 669 | 5.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 9 | L1-worker | claudeopus46 | 20,643 | 5,502 | 26,145 | 5,997 | 29.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 10 | L1-worker | claudeopus46 | 20,643 | 12,120 | 32,763 | 3,563 | 16.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 11 | L1-worker | claudeopus46 | 536 | 3,311 | 3,847 | 1,073 | 6.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 12 | L1-worker | claudeopus46 | 1,356 | 3,431 | 4,787 | 1,021 | 6.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 13 | L1-worker | claudeopus46 | 298 | 1,403 | 1,701 | 1,009 | 4.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 14 | L1-worker | claudeopus46 | 1,323 | 8,535 | 9,858 | 4,027 | 16.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 15 | L1-worker | claudeopus46 | 298 | 4,749 | 5,047 | 3,053 | 13.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 16 | L1-worker | claudeopus46 | 1,160 | 12,997 | 14,157 | 2,723 | 14.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 17 | L0-main | claudeopus46 | 9,605 | 2,000 | 11,605 | 889 | 6.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 18 | L1-worker | claudeopus46 | 20,643 | 808 | 21,451 | 582 | 4.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 19 | L1-worker | claudeopus46 | 20,643 | 2,011 | 22,654 | 946 | 5.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 20 | L1-worker | claudeopus46 | 2,065 | 500 | 2,565 | 409 | 3.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 21 | L1-worker | claudeopus46 | 20,643 | 2,134 | 22,777 | 394 | 3.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 22 | L1-worker | claudeopus46 | 1,323 | 2,142 | 3,465 | 234 | 2.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 23 | L1-worker | claudeopus46 | 536 | 405 | 941 | 293 | 3.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 24 | L1-worker | claudeopus46 | 1,356 | 525 | 1,881 | 310 | 3.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 25 | L1-worker | claudeopus46 | 298 | 956 | 1,254 | 154 | 2.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 26 | L1-worker | claudeopus46 | 747 | 2,648 | 3,395 | 353 | 3.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 27 | L0-main | claudeopus46 | 9,605 | 5,497 | 15,102 | 3,331 | 16.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 28 | L1-worker | claudeopus46 | 20,643 | 2,817 | 23,460 | 949 | 7.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 29 | L1-worker | claudeopus46 | 2,065 | 10,060 | 12,125 | 1,636 | 15.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 30 | L1-worker | claudeopus46 | 20,643 | 4,613 | 25,256 | 2,390 | 12.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 31 | L1-worker | claudeopus46 | 1,356 | 2,339 | 3,695 | 830 | 4.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 32 | L1-worker | claudeopus46 | 536 | 2,219 | 2,755 | 1,012 | 6.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 33 | L1-worker | claudeopus46 | 1,323 | 5,400 | 6,723 | 2,287 | 9.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 34 | L1-worker | claudeopus46 | 298 | 1,368 | 1,666 | 999 | 6.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 35 | L1-worker | claudeopus46 | 298 | 3,009 | 3,307 | 1,764 | 7.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 36 | L1-worker | claudeopus46 | 747 | 37,152 | 37,899 | 498 | 5.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 37 | L1-worker | claudeopus46 | 20,643 | 35,993 | 56,636 | 886 | 8.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 38 | L1-worker | claudeopus46 | 2,065 | 3,096 | 5,161 | 1,651 | 14.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 39 | L1-worker | claudeopus46 | 20,643 | 37,723 | 58,366 | 2,148 | 13.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 40 | L1-worker | claudeopus46 | 536 | 1,421 | 1,957 | 774 | 4.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 41 | L1-worker | claudeopus46 | 1,356 | 1,541 | 2,897 | 758 | 6.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 42 | L1-worker | claudeopus46 | 1,323 | 4,527 | 5,850 | 674 | 8.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 43 | L1-worker | claudeopus46 | 298 | 1,396 | 1,694 | 547 | 4.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 44 | L1-worker | claudeopus46 | 747 | 12,232 | 12,979 | 786 | 7.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 45 | L1-worker | claudeopus46 | 20,643 | 45,126 | 65,769 | 748 | 5.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 46 | L1-worker | claudeopus46 | 2,065 | 664 | 2,729 | 1,316 | 8.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 47 | L1-worker | claudeopus46 | 20,643 | 46,133 | 66,776 | 1,470 | 11.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 48 | L1-worker | claudeopus46 | 2,065 | 579 | 2,644 | 1,073 | 6.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 49 | L1-worker | claudeopus46 | 2,065 | 3,118 | 5,183 | 1,709 | 13.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 50 | L1-worker | claudeopus46 | 20,643 | 48,966 | 69,609 | 2,616 | 16.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 51 | L1-worker | claudeopus46 | 1,356 | 1,971 | 3,327 | 797 | 4.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 52 | L1-worker | claudeopus46 | 1,323 | 7,344 | 8,667 | 753 | 5.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 53 | L1-worker | claudeopus46 | 536 | 1,851 | 2,387 | 976 | 5.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 54 | L1-worker | claudeopus46 | 298 | 1,475 | 1,773 | 626 | 3.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 55 | L1-worker | claudeopus46 | 747 | 16,555 | 17,302 | 1,906 | 13.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 56 | L1-worker | claudeopus46 | 298 | 2,265 | 2,563 | 429 | 2.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 57 | L1-worker | claudeopus46 | 1,160 | 8,674 | 9,834 | 756 | 4.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 58 | L1-worker | claudeopus46 | 747 | 16,570 | 17,317 | 526 | 5.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 59 | L0-main | claudeopus46 | 9,605 | 49,782 | 59,387 | 1,476 | 9.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 60 | L1-worker | claudeopus46 | 20,643 | 44,909 | 65,552 | 652 | 5.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 61 | L1-worker | claudeopus46 | 2,065 | 636 | 2,701 | 1,141 | 7.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 62 | L1-worker | claudeopus46 | 20,643 | 45,854 | 66,497 | 854 | 5.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 63 | L1-worker | claudeopus46 | 536 | 863 | 1,399 | 465 | 3.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 64 | L1-worker | claudeopus46 | 1,323 | 2,911 | 4,234 | 235 | 3.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 65 | L1-worker | claudeopus46 | 1,356 | 983 | 2,339 | 520 | 3.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 66 | L1-worker | claudeopus46 | 298 | 957 | 1,255 | 155 | 2.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 67 | L1-worker | claudeopus46 | 747 | 4,165 | 4,912 | 577 | 6.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 68 | L0-main | claudeopus46 | 9,605 | 55,461 | 65,066 | 1,876 | 11.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 69 | L1-worker | claudeopus46 | 20,643 | 48,079 | 68,722 | 1,343 | 8.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 70 | L1-worker | claudeopus46 | 2,065 | 531 | 2,596 | 1,228 | 7.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 71 | L1-worker | claudeopus46 | 2,065 | 3,043 | 5,108 | 1,726 | 14.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 72 | L1-worker | claudeopus46 | 20,643 | 50,756 | 71,399 | 3,175 | 18.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 73 | L1-worker | claudeopus46 | 536 | 2,650 | 3,186 | 789 | 5.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 74 | L1-worker | claudeopus46 | 1,323 | 7,213 | 8,536 | 816 | 5.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 75 | L1-worker | claudeopus46 | 1,356 | 2,770 | 4,126 | 1,050 | 6.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 76 | L1-worker | claudeopus46 | 298 | 1,538 | 1,836 | 689 | 3.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 77 | L1-worker | claudeopus46 | 747 | 17,099 | 17,846 | 1,848 | 13.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 78 | L1-worker | claudeopus46 | 298 | 2,207 | 2,505 | 388 | 2.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 79 | L1-worker | claudeopus46 | 1,160 | 8,565 | 9,725 | 725 | 7.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 80 | L1-worker | claudeopus46 | 747 | 17,135 | 17,882 | 828 | 8.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 81 | L0-main | claudeopus46 | 9,605 | 79,308 | 88,913 | 5,498 | 36.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 82 | L0-main | claudeopus46 | 1,356 | 5,182 | 6,538 | 1,499 | 8.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 83 | L0-main | claudeopus46 | 298 | 1,881 | 2,179 | 1,487 | 5.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 84 | L0-main | claudeopus46 | 1,323 | 39,686 | 41,009 | 4,774 | 32.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 85 | L0-main | claudeopus46 | 298 | 5,442 | 5,740 | 4,109 | 18.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_7) |
| 1 | L0-main | claudeopus46 | 9,605 | 963 | 10,568 | 1,879 | 10.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,394 | 22,037 | 14,740 | 66.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 3 | L1-worker | claudeopus46 | 20,643 | 16,862 | 37,505 | 5,644 | 24.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 4 | L1-worker | claudeopus46 | 1,356 | 4,931 | 6,287 | 1,056 | 6.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 5 | L1-worker | claudeopus46 | 536 | 4,811 | 5,347 | 1,024 | 7.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 6 | L1-worker | claudeopus46 | 298 | 1,438 | 1,736 | 1,044 | 3.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 7 | L1-worker | claudeopus46 | 1,323 | 6,754 | 8,077 | 14,542 | 45.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 8 | L1-worker | claudeopus46 | 298 | 15,264 | 15,562 | 12,143 | 38.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 9 | L1-worker | claudeopus46 | 1,160 | 24,329 | 25,489 | 12,098 | 39.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 10 | L0-main | claudeopus46 | 9,605 | 1,922 | 11,527 | 833 | 6.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 11 | L1-worker | claudeopus46 | 20,643 | 788 | 21,431 | 598 | 4.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 12 | L1-worker | claudeopus46 | 2,065 | 484 | 2,549 | 511 | 4.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 13 | L1-worker | claudeopus46 | 20,643 | 1,545 | 22,188 | 413 | 4.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 14 | L1-worker | claudeopus46 | 1,323 | 1,980 | 3,303 | 233 | 2.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 15 | L1-worker | claudeopus46 | 536 | 422 | 958 | 246 | 2.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 16 | L1-worker | claudeopus46 | 1,356 | 542 | 1,898 | 236 | 2.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 17 | L1-worker | claudeopus46 | 298 | 955 | 1,253 | 153 | 2.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 18 | L1-worker | claudeopus46 | 747 | 2,388 | 3,135 | 358 | 4.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 19 | L0-main | claudeopus46 | 9,605 | 5,167 | 14,772 | 3,424 | 16.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 20 | L1-worker | claudeopus46 | 20,643 | 2,593 | 23,236 | 1,467 | 9.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 21 | L1-worker | claudeopus46 | 20,643 | 4,788 | 25,431 | 14,478 | 55.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 22 | L1-worker | claudeopus46 | 20,643 | 5,975 | 26,618 | 13,589 | 49.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 23 | L1-worker | claudeopus46 | 2,065 | 375 | 2,440 | 481 | 4.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 24 | L1-worker | claudeopus46 | 2,065 | 9,281 | 11,346 | 1,515 | 14.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 25 | L1-worker | claudeopus46 | 20,610 | 7,700 | 28,310 | 493 | 6.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 26 | L1-worker | claudeopus46 | 20,643 | 6,947 | 27,590 | 7,104 | 38.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 27 | L1-worker | claudeopus46 | 2,065 | 2,594 | 4,659 | 1,705 | 15.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 28 | L1-worker | claudeopus46 | 20,643 | 8,742 | 29,385 | 4,826 | 28.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 29 | L1-worker | claudeopus46 | 1,356 | 2,931 | 4,287 | 872 | 5.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 30 | L1-worker | claudeopus46 | 536 | 2,811 | 3,347 | 1,091 | 8.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 31 | L1-worker | claudeopus46 | 298 | 1,254 | 1,552 | 860 | 5.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 32 | L1-worker | claudeopus46 | 1,323 | 10,228 | 11,551 | 5,153 | 20.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 33 | L1-worker | claudeopus46 | 298 | 5,875 | 6,173 | 4,299 | 19.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 34 | L1-worker | claudeopus46 | 747 | 94,985 | 95,732 | 528 | 6.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 35 | L1-worker | claudeopus46 | 20,643 | 88,692 | 109,335 | 936 | 7.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 36 | L1-worker | claudeopus46 | 2,065 | 19,005 | 21,070 | 1,531 | 14.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 37 | L1-worker | claudeopus46 | 20,643 | 90,325 | 110,968 | 961 | 7.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 38 | L1-worker | claudeopus46 | 2,065 | 4,780 | 6,845 | 1,708 | 12.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 39 | L1-worker | claudeopus46 | 20,643 | 92,110 | 112,753 | 7,568 | 44.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 40 | L1-worker | claudeopus46 | 1,356 | 3,567 | 4,923 | 865 | 6.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 41 | L1-worker | claudeopus46 | 536 | 3,447 | 3,983 | 1,038 | 7.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 42 | L1-worker | claudeopus46 | 298 | 1,247 | 1,545 | 853 | 4.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 43 | L1-worker | claudeopus46 | 1,323 | 8,084 | 9,407 | 4,247 | 19.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 44 | L1-worker | claudeopus46 | 298 | 4,969 | 5,267 | 3,452 | 17.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 45 | L1-worker | claudeopus46 | 1,160 | 13,412 | 14,572 | 3,094 | 17.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 46 | L1-worker | claudeopus46 | 747 | 81,518 | 82,265 | 758 | 7.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 47 | L1-worker | claudeopus46 | 20,643 | 163,571 | 184,214 | 741 | 5.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 48 | L1-worker | claudeopus46 | 20,643 | 164,933 | 185,576 | 1,162 | 7.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 49 | L1-worker | claudeopus46 | 2,065 | 718 | 2,783 | 1,245 | 7.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 50 | L1-worker | claudeopus46 | 20,643 | 165,416 | 186,059 | 5,642 | 31.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 51 | L1-worker | claudeopus46 | 20,643 | 171,679 | 192,322 | 2,845 | 11.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 52 | L1-worker | claudeopus46 | 536 | 1,948 | 2,484 | 1,006 | 6.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 53 | L1-worker | claudeopus46 | 1,356 | 2,068 | 3,424 | 1,240 | 6.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 54 | L1-worker | claudeopus46 | 298 | 1,362 | 1,660 | 993 | 4.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 55 | L1-worker | claudeopus46 | 1,323 | 4,786 | 6,109 | 1,459 | 11.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 56 | L1-worker | claudeopus46 | 298 | 2,181 | 2,479 | 1,178 | 5.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 57 | L1-worker | claudeopus46 | 1,160 | 6,572 | 7,732 | 1,177 | 5.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 58 | L0-main | claudeopus46 | 9,605 | 167,950 | 177,555 | 1,676 | 11.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 59 | L1-worker | claudeopus46 | 20,643 | 163,727 | 184,370 | 714 | 7.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 60 | L1-worker | claudeopus46 | 20,643 | 165,062 | 185,705 | 14,243 | 57.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 61 | L1-worker | claudeopus46 | 2,065 | 678 | 2,743 | 905 | 7.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 62 | L1-worker | claudeopus46 | 20,643 | 165,444 | 186,087 | 6,325 | 35.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 63 | L1-worker | claudeopus46 | 20,643 | 172,390 | 193,033 | 2,262 | 8.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 64 | L1-worker | claudeopus46 | 1,323 | 4,649 | 5,972 | 756 | 5.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 65 | L1-worker | claudeopus46 | 1,356 | 1,930 | 3,286 | 1,018 | 5.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 66 | L1-worker | claudeopus46 | 536 | 1,810 | 2,346 | 1,042 | 5.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 67 | L1-worker | claudeopus46 | 298 | 1,400 | 1,698 | 1,006 | 3.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 68 | L1-worker | claudeopus46 | 298 | 1,478 | 1,776 | 629 | 5.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 69 | L1-worker | claudeopus46 | 1,160 | 5,704 | 6,864 | 628 | 3.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 70 | L1-worker | claudeopus46 | 747 | 13,831 | 14,578 | 1,102 | 9.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 71 | L0-main | claudeopus46 | 9,605 | 169,998 | 179,603 | 6,972 | 52.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 72 | L0-main | claudeopus46 | 1,356 | 7,103 | 8,459 | 1,463 | 8.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 73 | L0-main | claudeopus46 | 298 | 1,845 | 2,143 | 1,418 | 4.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 74 | L0-main | claudeopus46 | 1,323 | 16,978 | 18,301 | 7,582 | 38.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 75 | L0-main | claudeopus46 | 298 | 8,250 | 8,548 | 6,784 | 30.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_6) |
| 1 | L0-main | claudeopus46 | 9,605 | 999 | 10,604 | 2,092 | 10.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,439 | 22,082 | 1,115 | 5.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 3 | L1-worker | claudeopus46 | 20,643 | 3,282 | 23,925 | 15,208 | 58.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 4 | L1-worker | claudeopus46 | 2,065 | 1,219 | 3,284 | 507 | 5.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 5 | L1-worker | claudeopus46 | 2,065 | 949 | 3,014 | 1,091 | 6.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 6 | L1-worker | claudeopus46 | 20,643 | 4,275 | 24,918 | 13,508 | 54.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 7 | L1-worker | claudeopus46 | 2,065 | 22,615 | 24,680 | 1,695 | 13.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 8 | L1-worker | claudeopus46 | 20,610 | 6,328 | 26,938 | 599 | 4.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 9 | L1-worker | claudeopus46 | 20,643 | 5,575 | 26,218 | 2,898 | 18.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 10 | L1-worker | claudeopus46 | 1,356 | 2,431 | 3,787 | 797 | 4.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 11 | L1-worker | claudeopus46 | 536 | 2,311 | 2,847 | 972 | 5.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 12 | L1-worker | claudeopus46 | 1,323 | 7,412 | 8,735 | 1,255 | 7.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 13 | L1-worker | claudeopus46 | 298 | 1,977 | 2,275 | 943 | 5.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 14 | L1-worker | claudeopus46 | 747 | 17,303 | 18,050 | 718 | 7.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 15 | L0-main | claudeopus46 | 9,605 | 25,134 | 34,739 | 14,539 | 67.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 16 | L1-worker | claudeopus46 | 20,643 | 13,405 | 34,048 | 773 | 6.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 17 | L1-worker | claudeopus46 | 2,065 | 8,632 | 10,697 | 1,721 | 15.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 18 | L1-worker | claudeopus46 | 20,643 | 15,265 | 35,908 | 3,655 | 17.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 19 | L1-worker | claudeopus46 | 1,356 | 3,121 | 4,477 | 960 | 6.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 20 | L1-worker | claudeopus46 | 536 | 3,001 | 3,537 | 1,079 | 7.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 21 | L1-worker | claudeopus46 | 1,323 | 6,307 | 7,630 | 2,126 | 9.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 22 | L1-worker | claudeopus46 | 298 | 2,848 | 3,146 | 1,702 | 7.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 23 | L1-worker | claudeopus46 | 747 | 33,570 | 34,317 | 583 | 6.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 24 | L1-worker | claudeopus46 | 20,643 | 42,234 | 62,877 | 798 | 6.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 25 | L1-worker | claudeopus46 | 2,065 | 7,143 | 9,208 | 1,641 | 14.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 26 | L1-worker | claudeopus46 | 20,643 | 43,801 | 64,444 | 1,127 | 8.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 27 | L1-worker | claudeopus46 | 20,643 | 45,549 | 66,192 | 12,587 | 65.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 28 | L1-worker | claudeopus46 | 2,065 | 9,005 | 11,070 | 1,589 | 15.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 29 | L1-worker | claudeopus46 | 20,610 | 47,414 | 68,024 | 618 | 9.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 30 | L1-worker | claudeopus46 | 20,643 | 46,661 | 67,304 | 13,426 | 68.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 31 | L1-worker | claudeopus46 | 2,065 | 5,197 | 7,262 | 1,878 | 14.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 32 | L1-worker | claudeopus46 | 2,065 | 7,101 | 9,166 | 1,728 | 13.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 33 | L1-worker | claudeopus46 | 20,643 | 48,410 | 69,053 | 6,814 | 42.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 34 | L1-worker | claudeopus46 | 1,356 | 3,195 | 4,551 | 975 | 6.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 35 | L1-worker | claudeopus46 | 536 | 3,075 | 3,611 | 1,282 | 8.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 36 | L1-worker | claudeopus46 | 298 | 1,357 | 1,655 | 963 | 4.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 37 | L1-worker | claudeopus46 | 1,323 | 9,925 | 11,248 | 2,957 | 16.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 38 | L1-worker | claudeopus46 | 298 | 3,679 | 3,977 | 2,516 | 11.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 39 | L1-worker | claudeopus46 | 747 | 54,672 | 55,419 | 582 | 8.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 40 | L1-worker | claudeopus46 | 1,160 | 14,060 | 15,220 | 2,751 | 13.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 41 | L1-worker | claudeopus46 | 20,643 | 42,296 | 62,939 | 1,126 | 8.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 42 | L1-worker | claudeopus46 | 2,065 | 516 | 2,581 | 1,145 | 8.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 43 | L1-worker | claudeopus46 | 2,065 | 3,074 | 5,139 | 1,014 | 10.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 44 | L1-worker | claudeopus46 | 20,643 | 44,526 | 65,169 | 2,265 | 14.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 45 | L1-worker | claudeopus46 | 536 | 1,500 | 2,036 | 701 | 4.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 46 | L1-worker | claudeopus46 | 1,356 | 1,620 | 2,976 | 717 | 4.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 47 | L1-worker | claudeopus46 | 1,323 | 5,480 | 6,803 | 681 | 9.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 48 | L1-worker | claudeopus46 | 298 | 1,403 | 1,701 | 554 | 5.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 49 | L1-worker | claudeopus46 | 747 | 13,165 | 13,912 | 554 | 6.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 50 | L0-main | claudeopus46 | 9,605 | 65,367 | 74,972 | 2,176 | 19.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 51 | L1-worker | claudeopus46 | 20,643 | 51,495 | 72,138 | 787 | 6.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 52 | L1-worker | claudeopus46 | 2,065 | 7,099 | 9,164 | 1,604 | 15.0 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 53 | L1-worker | claudeopus46 | 20,643 | 53,183 | 73,826 | 850 | 7.3 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 54 | L1-worker | claudeopus46 | 2,065 | 9,002 | 11,067 | 1,677 | 16.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 55 | L1-worker | claudeopus46 | 20,643 | 54,774 | 75,417 | 2,638 | 18.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 56 | L1-worker | claudeopus46 | 2,065 | 7,134 | 9,199 | 1,603 | 13.8 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 57 | L1-worker | claudeopus46 | 20,610 | 57,141 | 77,751 | 419 | 4.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 58 | L1-worker | claudeopus46 | 20,643 | 56,388 | 77,031 | 4,812 | 31.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 59 | L1-worker | claudeopus46 | 1,356 | 2,996 | 4,352 | 887 | 6.1 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 60 | L1-worker | claudeopus46 | 536 | 2,876 | 3,412 | 825 | 6.2 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 61 | L1-worker | claudeopus46 | 298 | 1,181 | 1,479 | 812 | 3.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 62 | L1-worker | claudeopus46 | 1,323 | 9,055 | 10,378 | 2,293 | 11.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 63 | L1-worker | claudeopus46 | 298 | 3,015 | 3,313 | 1,911 | 9.7 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 64 | L1-worker | claudeopus46 | 747 | 47,027 | 47,774 | 903 | 8.9 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 65 | L0-main | claudeopus46 | 9,605 | 105,820 | 115,425 | 5,391 | 38.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 66 | L0-main | claudeopus46 | 1,356 | 5,522 | 6,878 | 1,830 | 11.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 67 | L0-main | claudeopus46 | 298 | 2,212 | 2,510 | 1,818 | 5.6 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 68 | L0-main | claudeopus46 | 1,323 | 34,543 | 35,866 | 5,596 | 31.5 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| 69 | L0-main | claudeopus46 | 298 | 6,264 | 6,562 | 4,689 | 21.4 | Find all ThermoML data blocks for binary mixtures of water + (query_runs/run_8) |
| **TOTAL** |  |  | **3,106,791** | **8,141,138** | **11,247,929** | **1,153,639** | **6,193.7** |  |
