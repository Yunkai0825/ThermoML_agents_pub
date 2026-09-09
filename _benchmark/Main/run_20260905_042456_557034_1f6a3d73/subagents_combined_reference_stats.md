# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 25 | 414,116 | 530,134 | 35,832 | 944,250 | 37,770 | 290.0 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| L1-worker | 40 | 487,925 | 165,084 | 37,731 | 653,009 | 16,325 | 292.2 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| L0-main | 24 | 391,598 | 865,193 | 40,439 | 1,256,791 | 52,366 | 313.8 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| L1-worker | 43 | 571,131 | 239,857 | 48,451 | 810,988 | 18,860 | 371.0 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| L0-main | 21 | 324,044 | 1,153,389 | 41,564 | 1,477,433 | 70,353 | 333.7 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| L1-worker | 46 | 642,554 | 338,178 | 52,351 | 980,732 | 21,320 | 378.2 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| L0-main | 19 | 279,008 | 86,455 | 28,265 | 365,463 | 19,234 | 204.3 | claudeopus46 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| L0-main | 16 | 254,774 | 61,415 | 29,448 | 316,189 | 19,761 | 211.6 | claudeopus46 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| L0-main | 18 | 256,490 | 113,427 | 39,729 | 369,917 | 20,550 | 295.3 | claudeopus46 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| **TOTAL** | **252** | **3,621,640** | **3,553,132** | **353,810** | **7,174,772** | **276,539** | **2,690.1** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `search_blocks` | 2 | 1 | 5 | 4 | 22 | 22 | 2,417 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `search_blocks` | 2 | 11 | 4 | 4 | 29 | 50 | 3,112 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `search_blocks` | 9 | 1 | 1 | 2 | 3 | 10 | 154 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `block_search_adv` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `query_thermoml_parallel` | 2 | 1 | 3 | 0 | 1 | 1 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 206 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `search_blocks` | 2 | 1 | 6 | 2 | 9 | 9 | 1,349 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `search_blocks` | 2 | 1 | 6 | 2 | 9 | 9 | 1,349 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `search_system_registry` | 2 | 1 | 6 | 1 | 8 | 8 | 1,337 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `query_thermoml_parallel` | 2 | 2 | 5 | 1 | 6 | 6 | 1,189 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `fit_block_derived` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `search_blocks` | 2 | 1 | 3 | 1 | 3 | 3 | 188 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `search_blocks` | 2 | 3 | 3 | 2 | 3 | 6 | 340 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `query_thermoml_parallel` | 2 | 3 | 3 | 2 | 3 | 6 | 86 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| **TOTAL** | **43** | **31** | **48** | **21** | **97** | **131** | **11,727** |  |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | ---: | --- |
| Unique Compounds | 11 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| Unique Properties | 12 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| Unique References | 48 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| Unique Measurements | 36 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| Unique Phases | 3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| Unique Variables | 5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| Unique Solvents | 2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| Unique Constraints | 6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| Unique Block_Types | 1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| Unique parent blocks | 76 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| Explicit block/subsystem targets | 76 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| Subsystem targets | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| Target-matched data points | 6,493 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| GLOBcomp_4 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_1 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks, search_system_registry |
| GLOBprop_28 |  | query_thermoml_parallel, resolve_property_ids, search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_2395 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2432 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_2825 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_7085 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_8254 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_8424 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_8869 |  | search_blocks, search_system_registry |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9571 |  | search_blocks, search_system_registry |
| GLOBlit_10866 |  | search_blocks, search_system_registry |
| GLOBmeas_207 | Excess molar volume, m3/mol | query_thermoml_parallel, search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_170 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_138 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_280 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_18 | Volume fraction | search_blocks, search_system_registry |
| GLOBsolvent_1 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBsolvent_3 |  | search_blocks |
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBblocktype_1 |  | query_thermoml_parallel, search_system_registry |
| Unique Compounds | 2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| Unique Properties | 2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| Unique References | 10 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| Unique Measurements | 7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| Unique Phases | 1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| Unique Variables | 6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| Unique Solvents | 2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| Unique Constraints | 2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| Unique Block_Types | 1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| Unique parent blocks | 10 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| Explicit block/subsystem targets | 10 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| Subsystem targets | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| Target-matched data points | 5,675 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| GLOBcomp_15 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_18 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBprop_28 |  | resolve_property_ids |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBprop_8 | Speed of sound, m/s | query_thermoml_parallel, search_blocks |
| GLOBlit_2659 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_4124 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_7481 |  | query_thermoml_parallel, search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBmeas_18 | Speed of sound, m/s | query_thermoml_parallel, search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks |
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks |
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBconstr_4 | Frequency, MHz | query_thermoml_parallel, search_blocks |
| GLOBblocktype_1 |  | query_thermoml_parallel |
| Unique Compounds | 2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| Unique Properties | 4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| Unique References | 3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| Unique Measurements | 5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| Unique Phases | 1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| Unique Variables | 3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| Unique Constraints | 2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| Unique Block_Types | 1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| Unique parent blocks | 6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| Explicit block/subsystem targets | 6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| Subsystem targets | 0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| Target-matched data points | 868 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| **TOTAL** | **13,398** |  |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 10.1007/s10765-010-0717-9 | PROPblock_6 | declared | 15 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1007/s10765-010-0717-9 | PROPblock_8 | declared | 17 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1007/s10765-010-0861-2 | PROPblock_11 | declared | 31 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1007/s10765-010-0861-2 | PROPblock_13 | declared | 31 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2005.06.011 | PROPblock_16 | declared | 10 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2005.06.011 | PROPblock_18 | declared | 9 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2005.06.011 | PROPblock_20 | declared | 10 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2005.06.011 | PROPblock_22 | declared | 10 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2005.06.011 | PROPblock_24 | declared | 10 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2005.06.011 | PROPblock_26 | declared | 11 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2005.08.018 | PROPblock_4 | declared | 2 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2005.08.018 | PROPblock_5 | declared | 7 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2005.08.018 | PROPblock_6 | declared | 4 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2006.04.017 | PROPblock_3 | declared | 28 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2007.06.007 | PROPblock_1 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2007.06.007 | PROPblock_2 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2009.10.002 | PROPblock_17 | declared | 5 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2009.10.002 | PROPblock_18 | declared | 5 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2009.11.014 | PROPblock_2 | declared | 18 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2009.11.014 | PROPblock_3 | declared | 18 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2011.06.009 | PROPblock_1 | declared | 45 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2011.06.009 | PROPblock_2 | declared | 45 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2012.11.026 | PROPblock_4 | declared | 24 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2012.11.026 | PROPblock_5 | declared | 24 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2012.12.014 | PROPblock_2 | declared | 76 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2012.12.014 | PROPblock_3 | declared | 76 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2013.07.001 | PROPblock_6 | declared | 42 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2014.05.031 | PROPblock_4 | declared | 56 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2014.07.022 | PROPblock_1 | declared | 7 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2014.07.022 | PROPblock_2 | declared | 7 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_3 | declared | 84 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_4 | declared | 84 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2016.08.030 | PROPblock_1 | declared | 4 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2017.03.010 | PROPblock_7 | declared | 17 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2017.03.010 | PROPblock_8 | declared | 17 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_3 | declared | 72 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_4 | declared | 72 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2018.07.014 | PROPblock_4 | declared | 17 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2019.03.019 | PROPblock_8 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.fluid.2019.03.019 | PROPblock_9 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2005.06.018 | PROPblock_4 | declared | 27 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2006.08.002 | PROPblock_1 | declared | 25 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2006.08.002 | PROPblock_2 | declared | 19 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2006.08.002 | PROPblock_3 | declared | 4 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2006.08.002 | PROPblock_4 | declared | 278 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2012.08.009 | PROPblock_18 | declared | 14 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2013.08.020 | PROPblock_10 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2013.08.020 | PROPblock_11 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2013.08.020 | PROPblock_12 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2013.08.020 | PROPblock_9 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2014.05.020 | PROPblock_1 | declared | 30 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2015.06.024 | PROPblock_8 | declared | 40 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2017.07.021 | PROPblock_3 | declared | 24 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1021/je900064e | PROPblock_6 | declared | 10 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1021/je900743e | PROPblock_3 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10.1016/j.jct.2004.03.011 | 1 | 206 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |  |  |
| 10.1016/j.jct.2004.07.019 | 1 | 596 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |  |  |
| 10.1016/j.jct.2007.05.004 | 1 | 39 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |  |  |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |  |  |
| 10.1021/je034101z | 1 | 401 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |  |  |
| 10.1021/je049691v | 1 | 180 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |  |  |
| 10.1021/je0600810 | 1 | 9 | binary | search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |  |  |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |  |  |
| 10.1021/je2003622 | 1 | 16 | binary | search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |  |  |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |  |  |
| 10.1016/j.jct.2004.03.011 | PROPblock_1 | declared | 206 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | 2 | search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | 2 | search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | 2 | search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 10.1016/j.jct.2006.01.015 | 1 | 102 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |  |  |
| 10.1016/j.jct.2014.02.019 | 2 | 40 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |  |  |
| 10.1021/acs.jced.8b00176 | 3 | 198 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |  |  |
| 10.1016/j.jct.2006.01.015 | PROPblock_7 | declared | 102 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 10.1016/j.jct.2014.02.019 | PROPblock_5 | declared | 20 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 10.1016/j.jct.2014.02.019 | PROPblock_6 | declared | 20 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 10.1021/acs.jced.8b00176 | PROPblock_16 | declared | 66 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 10.1021/acs.jced.8b00176 | PROPblock_17 | declared | 66 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 10.1021/acs.jced.8b00176 | PROPblock_18 | declared | 66 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| **TOTAL** | **16** | **1,895** | **5,916** |  | **32** |  |  |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | --- | ---: | --- |
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume_dir… | 132 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 2 | 1 | `resolve_compound_ids` | purpose=Find compound IDs for ethanol…, queries=['… | 195 | KEEP ←in 278 | 195 | 3.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve ethanol and… | 250 | KEEP ←in 278 | 250 | 3.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 4 | 2 | `resolve_property_ids` | purpose=Find the global ID for excess…, queries=['… | 263 | KEEP ←in 227 | 263 | 4.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 5 | 3 | `resolve_property_ids` | limit=5, min_score=80, purpose=Confirm property ID… | 273 | KEEP ←in 218 | 273 | 8.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 6 | 4 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 996 | DISCARD ←in 39 | 938 | 16.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 7 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 539 | KEEP ←in 14,080 | 539 | 16.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 8 | 6 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_220, … | 359 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 9 | 5 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,155 | DISCARD ←in 39 | 1097 | 20.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10 | 7 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_220, … | 1,888 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 11 | 6 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 978 | KEEP ←in 30,867 | 814 | 20.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 12 | 7 | `search_blocks` | limit=10, property=GLOBprop_28, purpose=Check if e… | 1,244 | KEEP ←in 6,974 | 1148 | 12.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 13 | 8 | `block_search_adv` | compounds=['REQUIRE GLOBcomp_2 AS ethan…, explanat… | 898 | DISCARD ←in 800 | 837 | 16.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 14 | 2 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume_dir… | 20,635 | — | — | 172.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 15 | 5 | `inspect_block` | block_number=PROPblock_2, doi=10.1016/j.fluid.2004… | 1,374 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 16 | 9 | `fit_block_derived` | block_number=PROPblock_2, composition_hint=mole_fr… | 239 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 17 | 11 | `fit_block_derived` | block_number=PROPblock_2, composition_hint=mole_fr… | 963 | — | — | 1.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 18 | 14 | `predict_from_rk` | coeffs=[-4.98777e-06, 2.71547e-06, -…, mixing_rule… | 206 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 19 | 15 | `list_session_files` |  | 1,689 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume', '… | 132 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 2 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve methanol an… | 180 | KEEP ←in 277 | 180 | 3.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve methanol an… | 236 | KEEP ←in 277 | 236 | 4.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 4 | 3 | `resolve_property_ids` | limit=5, min_score=70, purpose=Find the global pro… | 256 | KEEP ←in 227 | 256 | 4.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 5 | 5 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=50, p… | 968 | KEEP ←in 3,972 | 953 | 20.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 6 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=50, p… | 104 | KEEP ←in 5,885 | 104 | 23.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 7 | 6 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2395,… | 375 | — | — | 0.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 8 | 7 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2395,… | 980 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 9 | 5 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=20, p… | 331 | KEEP ←in 5,885 | 331 | 17.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 10 | 6 | `search_system_registry` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=20, p… | 1,344 | KEEP ←in 6,499 | 1329 | 16.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 11 | 7 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_10, purpose=G… | 347 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 12 | 8 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_10, purpose=G… | 1,502 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 13 | 10 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_10, nearest={… | 861 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 14 | 11 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_10, purpose=F… | 965 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 15 | 2 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume', '… | 58,627 | — | — | 260.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 16 | 5 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 211 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 17 | 9 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 301 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 18 | 11 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 237 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 19 | 12 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 954 | — | — | 1.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 20 | 13 | `predict_from_rk` | coeffs=[-3.98239e-06, -1.5386e-07, 1…, n_points=10… | 207 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 21 | 14 | `list_session_files` |  | 1,681 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 132 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 2 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 213 | KEEP ←in 308 | 213 | 3.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 208 | KEEP ←in 308 | 208 | 4.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 4 | 3 | `resolve_property_ids` | limit=5, min_score=50, purpose=Find the global pro… | 237 | KEEP ←in 227 | 237 | 4.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 5 | 5 | `search_blocks` | compound=['GLOBcomp_15', 'GLOBcomp_18'], limit=50,… | 1,026 | KEEP ←in 6,590 | 1169 | 10.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 6 | 4 | `search_blocks` | compound=['GLOBcomp_15', 'GLOBcomp_18'], limit=50,… | 1,169 | DISCARD ←in 39 | 968 | 19.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 7 | 6 | `inspect_block_table` | block_number=PROPblock_7, literature=GLOBlit_2659,… | 357 | — | — | 0.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 8 | 7 | `inspect_block_table` | block_number=PROPblock_7, literature=GLOBlit_2659,… | 1,682 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 9 | 6 | `search_blocks` | compound=['GLOBcomp_15', 'GLOBcomp_18'], limit=50,… | 1,009 | DISCARD ←in 39 | 951 | 20.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 10 | 8 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_4124,… | 1,096 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 11 | 9 | `inspect_block_table` | block_number=PROPblock_16, literature=GLOBlit_7481… | 1,424 | — | — | 0.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 12 | 7 | `search_blocks` | compound=['GLOBcomp_15', 'GLOBcomp_18'], limit=20,… | 1,291 | KEEP ←in 9,352 | 1201 | 12.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 13 | 9 | `inspect_block_table` | block_number=PROPblock_7, literature=GLOBlit_2659,… | 2,181 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 14 | 10 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_4124,… | 1,306 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 15 | 11 | `inspect_block_table` | block_number=PROPblock_16, literature=GLOBlit_7481… | 2,245 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 16 | 12 | `inspect_block_table` | block_number=PROPblock_17, literature=GLOBlit_7481… | 1,806 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 17 | 2 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 112,499 | — | — | 210.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 18 | 4 | `fit_block_derived` | block_number=PROPblock_7, composition_hint=mole_fr… | 243 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 19 | 6 | `fit_block_derived` | block_number=PROPblock_7, composition_hint=mole_fr… | 1,004 | — | — | 1.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 20 | 8 | `fit_block_derived` | block_number=PROPblock_16, composition_hint=mole_f… | 946 | — | — | 1.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 21 | 10 | `predict_from_rk` | coeffs=[-1.13034e-06, -7.63893e-07, …, mixing_rule… | 221 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 22 | 11 | `list_session_files` |  | 3,133 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 1 | 4 | `predict_from_rk` | coeffs=[-3.982385645518985e-06, -1.5…, n_points=20… | 207 | — | — | 0.0 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 2 | 6 | `predict_from_rk` | coeffs=[-3.982385645518985e-06, -1.5…, mixing_rule… | 207 | — | — | 0.0 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 3 | 7 | `compute_ideal_baseline` | mixing_rule=linear, n_points=13, property_type=mol… | 139 | — | — | 0.0 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 4 | 8 | `predict_from_rk` | coeffs=[-3.982385645518985e-06, -1.5…, mixing_rule… | 206 | — | — | 0.0 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 5 | 9 | `list_session_files` |  | 211 | — | — | 0.1 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 1 | 3 | `predict_from_rk` | coeffs=[-4.987765356267973e-06, 2.71…, mixing_rule… | 206 | — | — | 0.5 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 2 | 4 | `list_session_files` |  | 212 | — | — | 0.0 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 3 | 5 | `predict_from_rk` | coeffs=[-4.987765356267973e-06, 2.71…, mixing_rule… | 205 | — | — | 0.1 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 4 | 6 | `predict_from_rk` | coeffs=[-4.987765356267973e-06, 2.71…, n_points=5,… | 204 | — | — | 0.0 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 5 | 7 | `predict_from_rk` | coeffs=[-4.987765356267973e-06, 2.71…, n_points=10… | 177 | — | — | 0.2 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 6 | 8 | `predict_from_rk` | coeffs=[4.987765356267973e-06, -2.71…, n_points=10… | 188 | — | — | 0.2 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 1 | 4 | `predict_from_rk` | coeffs=[-1.1303359340037732e-06, -7.…, mixing_rule… | 207 | — | — | 0.0 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 2 | 5 | `list_session_files` |  | 212 | — | — | 0.0 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 3 | 6 | `predict_from_rk` | coeffs=[-1.1303359340037732e-06, -7.…, mixing_rule… | 206 | — | — | 0.0 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 4 | 7 | `predict_from_rk` | coeffs=[-1.1303359340037732e-06, -7.…, mixing_rule… | 207 | — | — | 0.0 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| **TOTAL** | **488** |  |  | **243,497** |  | **14,690** | **942.4** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 22,518 | 750 | 23,268 | 1,557 | 10.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 2 | L0-main | claudeopus46 | 22,518 | 1,208 | 23,726 | 1,376 | 8.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 3 | L1-worker | claudeopus46 | 24,095 | 962 | 25,057 | 691 | 5.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 4 | L1-worker | claudeopus46 | 24,095 | 852 | 24,947 | 596 | 6.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 5 | L1-worker | claudeopus46 | 3,767 | 430 | 4,197 | 324 | 3.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,007 | 26,102 | 576 | 4.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 7 | L1-worker | claudeopus46 | 3,767 | 467 | 4,234 | 406 | 3.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 8 | L1-worker | claudeopus46 | 24,095 | 1,326 | 25,421 | 713 | 5.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 9 | L1-worker | claudeopus46 | 3,767 | 396 | 4,163 | 395 | 4.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,658 | 25,753 | 1,011 | 7.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 11 | L1-worker | claudeopus46 | 3,767 | 368 | 4,135 | 297 | 3.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 12 | L1-worker | claudeopus46 | 24,095 | 1,886 | 25,981 | 818 | 5.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 13 | L1-worker | claudeopus46 | 3,767 | 670 | 4,437 | 487 | 4.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,615 | 26,710 | 664 | 7.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 15 | L1-worker | claudeopus46 | 24,095 | 2,240 | 26,335 | 750 | 5.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 16 | L1-worker | claudeopus46 | 24,095 | 2,968 | 27,063 | 700 | 5.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 17 | L1-worker | claudeopus46 | 3,767 | 556 | 4,323 | 1,216 | 9.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 18 | L1-worker | claudeopus46 | 24,095 | 3,599 | 27,694 | 861 | 6.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 19 | L1-worker | claudeopus46 | 3,767 | 14,545 | 18,312 | 1,830 | 15.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 20 | L1-worker | claudeopus46 | 24,095 | 3,482 | 27,577 | 2,217 | 16.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 21 | L1-worker | claudeopus46 | 3,767 | 471 | 4,238 | 1,477 | 9.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 22 | L1-worker | claudeopus46 | 24,095 | 4,229 | 28,324 | 794 | 6.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 23 | L1-worker | claudeopus46 | 24,095 | 5,114 | 29,209 | 843 | 6.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 24 | L1-worker | claudeopus46 | 24,095 | 6,507 | 30,602 | 2,086 | 16.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 25 | L1-worker | claudeopus46 | 3,767 | 31,304 | 35,071 | 1,806 | 13.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 26 | L1-worker | claudeopus46 | 24,095 | 6,454 | 30,549 | 1,008 | 6.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 27 | L1-worker | claudeopus46 | 24,095 | 11,756 | 35,851 | 3,155 | 21.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 28 | L1-worker | claudeopus46 | 3,767 | 7,311 | 11,078 | 1,399 | 11.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 29 | L1-worker | claudeopus46 | 2,320 | 2,194 | 4,514 | 741 | 4.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 30 | L1-worker | claudeopus46 | 627 | 2,074 | 2,701 | 807 | 5.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 31 | L1-worker | claudeopus46 | 2,106 | 3,277 | 5,383 | 986 | 5.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 32 | L1-worker | claudeopus46 | 366 | 1,178 | 1,544 | 701 | 3.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 33 | L1-worker | claudeopus46 | 366 | 1,763 | 2,129 | 612 | 3.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 34 | L1-worker | claudeopus46 | 24,095 | 8,018 | 32,113 | 1,389 | 9.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 35 | L1-worker | claudeopus46 | 787 | 12,376 | 13,163 | 597 | 7.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 36 | L1-worker | claudeopus46 | 3,767 | 1,018 | 4,785 | 1,118 | 8.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 37 | L1-worker | claudeopus46 | 24,095 | 9,393 | 33,488 | 1,844 | 14.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 38 | L1-worker | claudeopus46 | 2,106 | 2,354 | 4,460 | 92 | 1.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 39 | L1-worker | claudeopus46 | 2,320 | 1,381 | 3,701 | 574 | 3.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 40 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 1.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 41 | L1-worker | claudeopus46 | 627 | 1,261 | 1,888 | 547 | 4.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 42 | L1-worker | claudeopus46 | 787 | 3,755 | 4,542 | 536 | 5.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 43 | L0-main | claudeopus46 | 22,518 | 23,630 | 46,148 | 1,108 | 11.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 44 | L0-main | claudeopus46 | 22,518 | 24,336 | 46,854 | 583 | 4.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 45 | L0-main | claudeopus46 | 22,518 | 25,016 | 47,534 | 465 | 4.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 46 | L0-main | claudeopus46 | 22,518 | 26,549 | 49,067 | 1,156 | 8.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 47 | L0-main | claudeopus46 | 22,518 | 27,264 | 49,782 | 888 | 6.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 48 | L0-main | claudeopus46 | 22,518 | 27,948 | 50,466 | 1,011 | 7.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 49 | L0-main | claudeopus46 | 22,518 | 28,756 | 51,274 | 927 | 6.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 50 | L0-main | claudeopus46 | 22,518 | 28,384 | 50,902 | 1,053 | 7.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 51 | L0-main | claudeopus46 | 22,518 | 29,068 | 51,586 | 949 | 6.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 52 | L0-main | claudeopus46 | 22,518 | 31,536 | 54,054 | 961 | 8.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 53 | L0-main | claudeopus46 | 22,518 | 32,220 | 54,738 | 776 | 5.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 54 | L0-main | claudeopus46 | 22,518 | 32,879 | 55,397 | 859 | 5.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 55 | L0-main | claudeopus46 | 22,518 | 32,842 | 55,360 | 3,168 | 36.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 56 | L0-main | claudeopus46 | 22,518 | 34,872 | 57,390 | 6,745 | 48.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 57 | L0-main | claudeopus46 | 22,518 | 44,908 | 67,426 | 4,567 | 35.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 58 | L0-main | claudeopus46 | 22,518 | 53,245 | 75,763 | 3,252 | 28.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 59 | L0-main | claudeopus46 | 2,106 | 4,230 | 6,336 | 154 | 2.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 60 | L0-main | claudeopus46 | 366 | 677 | 1,043 | 195 | 2.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 61 | L0-main | claudeopus46 | 2,320 | 3,381 | 5,701 | 1,170 | 10.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 62 | L0-main | claudeopus46 | 366 | 1,607 | 1,973 | 1,125 | 5.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 63 | L0-main | claudeopus46 | 560 | 3,902 | 4,462 | 106 | 2.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 64 | L0-main | claudeopus46 | 1,156 | 4,700 | 5,856 | 561 | 6.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 65 | L0-main | claudeopus46 | 1,918 | 6,226 | 8,144 | 1,120 | 10.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_6) |
| 1 | L0-main | claudeopus46 | 22,518 | 752 | 23,270 | 1,481 | 10.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 2 | L0-main | claudeopus46 | 22,518 | 1,165 | 23,683 | 1,271 | 8.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 3 | L1-worker | claudeopus46 | 24,095 | 871 | 24,966 | 755 | 5.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 4 | L1-worker | claudeopus46 | 24,095 | 968 | 25,063 | 737 | 5.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,889 | 25,984 | 518 | 4.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 6 | L1-worker | claudeopus46 | 3,767 | 438 | 4,205 | 317 | 3.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,028 | 26,123 | 596 | 10.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 8 | L1-worker | claudeopus46 | 24,095 | 1,464 | 25,559 | 578 | 4.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 9 | L1-worker | claudeopus46 | 3,767 | 480 | 4,247 | 408 | 4.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 10 | L1-worker | claudeopus46 | 3,767 | 396 | 4,163 | 362 | 4.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 11 | L1-worker | claudeopus46 | 24,095 | 1,653 | 25,748 | 862 | 8.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 12 | L1-worker | claudeopus46 | 24,095 | 1,977 | 26,072 | 850 | 6.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 13 | L1-worker | claudeopus46 | 24,095 | 2,380 | 26,475 | 637 | 4.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,709 | 26,804 | 662 | 5.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 15 | L1-worker | claudeopus46 | 3,767 | 4,455 | 8,222 | 1,474 | 14.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 16 | L1-worker | claudeopus46 | 3,767 | 6,341 | 10,108 | 1,666 | 15.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 17 | L1-worker | claudeopus46 | 24,095 | 3,667 | 27,762 | 730 | 6.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 18 | L1-worker | claudeopus46 | 24,095 | 2,465 | 26,560 | 1,175 | 7.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 19 | L1-worker | claudeopus46 | 24,095 | 4,424 | 28,519 | 819 | 5.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 20 | L1-worker | claudeopus46 | 24,095 | 5,740 | 29,835 | 1,327 | 10.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 21 | L1-worker | claudeopus46 | 3,767 | 6,365 | 10,132 | 1,797 | 16.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 22 | L1-worker | claudeopus46 | 2,106 | 2,450 | 4,556 | 378 | 3.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 23 | L1-worker | claudeopus46 | 627 | 1,338 | 1,965 | 768 | 5.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 24 | L1-worker | claudeopus46 | 2,320 | 1,458 | 3,778 | 836 | 5.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 25 | L1-worker | claudeopus46 | 366 | 1,155 | 1,521 | 366 | 3.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 26 | L1-worker | claudeopus46 | 366 | 1,179 | 1,545 | 756 | 4.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 27 | L1-worker | claudeopus46 | 366 | 1,273 | 1,639 | 801 | 4.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 28 | L1-worker | claudeopus46 | 1,228 | 3,127 | 4,355 | 301 | 2.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 29 | L1-worker | claudeopus46 | 24,095 | 3,161 | 27,256 | 1,991 | 13.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 30 | L1-worker | claudeopus46 | 787 | 10,234 | 11,021 | 495 | 5.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 31 | L1-worker | claudeopus46 | 3,767 | 7,014 | 10,781 | 1,629 | 15.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 32 | L1-worker | claudeopus46 | 24,095 | 4,975 | 29,070 | 1,408 | 11.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 33 | L1-worker | claudeopus46 | 24,095 | 5,714 | 29,809 | 658 | 5.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 34 | L1-worker | claudeopus46 | 24,095 | 7,570 | 31,665 | 2,521 | 20.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 35 | L1-worker | claudeopus46 | 24,095 | 13,362 | 37,457 | 3,075 | 20.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 36 | L1-worker | claudeopus46 | 24,095 | 14,618 | 38,713 | 993 | 9.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 37 | L1-worker | claudeopus46 | 24,095 | 15,945 | 40,040 | 2,470 | 20.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 38 | L1-worker | claudeopus46 | 24,062 | 20,379 | 44,441 | 2,341 | 13.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 39 | L1-worker | claudeopus46 | 24,062 | 21,941 | 46,003 | 2,242 | 18.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 40 | L1-worker | claudeopus46 | 2,320 | 2,961 | 5,281 | 808 | 5.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 41 | L1-worker | claudeopus46 | 627 | 2,841 | 3,468 | 1,095 | 6.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 42 | L1-worker | claudeopus46 | 366 | 1,245 | 1,611 | 773 | 3.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 43 | L1-worker | claudeopus46 | 2,106 | 4,050 | 6,156 | 3,024 | 12.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 44 | L1-worker | claudeopus46 | 366 | 3,801 | 4,167 | 1,687 | 6.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 45 | L1-worker | claudeopus46 | 787 | 37,356 | 38,143 | 765 | 8.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 46 | L0-main | claudeopus46 | 22,518 | 48,245 | 70,763 | 2,829 | 24.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 47 | L0-main | claudeopus46 | 22,518 | 49,479 | 71,997 | 1,661 | 11.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 48 | L0-main | claudeopus46 | 22,518 | 50,389 | 72,907 | 834 | 5.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 49 | L0-main | claudeopus46 | 22,518 | 49,704 | 72,222 | 1,544 | 12.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 50 | L0-main | claudeopus46 | 22,518 | 50,496 | 73,014 | 1,050 | 8.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 51 | L0-main | claudeopus46 | 22,518 | 51,249 | 73,767 | 813 | 6.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 52 | L0-main | claudeopus46 | 22,518 | 52,026 | 74,544 | 859 | 6.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 53 | L0-main | claudeopus46 | 22,518 | 51,785 | 74,303 | 815 | 7.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 54 | L0-main | claudeopus46 | 22,518 | 52,538 | 75,056 | 846 | 5.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 55 | L0-main | claudeopus46 | 22,518 | 52,871 | 75,389 | 932 | 6.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 56 | L0-main | claudeopus46 | 22,518 | 55,709 | 78,227 | 1,661 | 14.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 57 | L0-main | claudeopus46 | 22,518 | 56,368 | 78,886 | 2,331 | 17.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 58 | L0-main | claudeopus46 | 22,518 | 58,490 | 81,008 | 6,755 | 50.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 59 | L0-main | claudeopus46 | 22,518 | 70,759 | 93,277 | 4,676 | 37.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 60 | L0-main | claudeopus46 | 22,518 | 78,721 | 101,239 | 4,622 | 39.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 61 | L0-main | claudeopus46 | 2,106 | 6,302 | 8,408 | 274 | 3.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 62 | L0-main | claudeopus46 | 366 | 797 | 1,163 | 260 | 2.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 63 | L0-main | claudeopus46 | 2,320 | 5,451 | 7,771 | 1,267 | 9.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 64 | L0-main | claudeopus46 | 366 | 1,704 | 2,070 | 1,217 | 5.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 65 | L0-main | claudeopus46 | 560 | 6,258 | 6,818 | 186 | 2.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 66 | L0-main | claudeopus46 | 1,156 | 7,727 | 8,883 | 1,013 | 8.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 67 | L0-main | claudeopus46 | 1,918 | 6,208 | 8,126 | 1,242 | 11.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_5) |
| 1 | L0-main | claudeopus46 | 22,518 | 808 | 23,326 | 1,554 | 10.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 2 | L0-main | claudeopus46 | 22,518 | 1,232 | 23,750 | 1,263 | 7.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 3 | L1-worker | claudeopus46 | 24,095 | 919 | 25,014 | 596 | 4.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 4 | L1-worker | claudeopus46 | 24,095 | 869 | 24,964 | 669 | 5.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,971 | 26,066 | 591 | 4.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,921 | 26,016 | 579 | 4.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 7 | L1-worker | claudeopus46 | 3,767 | 483 | 4,250 | 332 | 3.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 8 | L1-worker | claudeopus46 | 3,767 | 483 | 4,250 | 382 | 4.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 9 | L1-worker | claudeopus46 | 24,095 | 1,584 | 25,679 | 855 | 6.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,517 | 25,612 | 853 | 6.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 11 | L1-worker | claudeopus46 | 3,767 | 396 | 4,163 | 343 | 3.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 12 | L1-worker | claudeopus46 | 24,095 | 2,244 | 26,339 | 642 | 4.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 13 | L1-worker | claudeopus46 | 24,095 | 2,155 | 26,250 | 849 | 6.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,912 | 27,007 | 681 | 5.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 15 | L1-worker | claudeopus46 | 3,767 | 7,072 | 10,839 | 1,465 | 13.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 16 | L1-worker | claudeopus46 | 3,767 | 573 | 4,340 | 1,262 | 9.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 17 | L1-worker | claudeopus46 | 24,095 | 3,926 | 28,021 | 955 | 7.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 18 | L1-worker | claudeopus46 | 24,095 | 3,379 | 27,474 | 2,206 | 13.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 19 | L1-worker | claudeopus46 | 24,095 | 8,732 | 32,827 | 556 | 5.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 20 | L1-worker | claudeopus46 | 24,095 | 9,379 | 33,474 | 533 | 5.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 21 | L1-worker | claudeopus46 | 3,767 | 541 | 4,308 | 1,291 | 9.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 22 | L1-worker | claudeopus46 | 24,095 | 11,351 | 35,446 | 553 | 5.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 23 | L1-worker | claudeopus46 | 24,095 | 5,291 | 29,386 | 1,141 | 7.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 24 | L1-worker | claudeopus46 | 24,095 | 12,757 | 36,852 | 438 | 4.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 25 | L1-worker | claudeopus46 | 3,767 | 9,732 | 13,499 | 1,492 | 11.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 26 | L1-worker | claudeopus46 | 24,095 | 14,477 | 38,572 | 2,207 | 17.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 27 | L1-worker | claudeopus46 | 24,095 | 6,947 | 31,042 | 2,414 | 13.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 28 | L1-worker | claudeopus46 | 24,095 | 12,170 | 36,265 | 1,380 | 11.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 29 | L1-worker | claudeopus46 | 24,095 | 20,365 | 44,460 | 3,502 | 25.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 30 | L1-worker | claudeopus46 | 24,095 | 14,663 | 38,758 | 861 | 8.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 31 | L1-worker | claudeopus46 | 627 | 3,271 | 3,898 | 959 | 6.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 32 | L1-worker | claudeopus46 | 24,095 | 16,317 | 40,412 | 572 | 4.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 33 | L1-worker | claudeopus46 | 2,320 | 3,391 | 5,711 | 1,189 | 8.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 34 | L1-worker | claudeopus46 | 2,106 | 4,381 | 6,487 | 1,830 | 9.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 35 | L1-worker | claudeopus46 | 366 | 1,370 | 1,736 | 946 | 4.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 36 | L1-worker | claudeopus46 | 366 | 1,626 | 1,992 | 1,118 | 4.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 37 | L1-worker | claudeopus46 | 366 | 2,607 | 2,973 | 1,045 | 4.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 38 | L1-worker | claudeopus46 | 24,095 | 18,857 | 42,952 | 598 | 7.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 39 | L1-worker | claudeopus46 | 787 | 26,646 | 27,433 | 874 | 9.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 40 | L1-worker | claudeopus46 | 24,062 | 20,655 | 44,717 | 3,115 | 22.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 41 | L1-worker | claudeopus46 | 24,062 | 22,581 | 46,643 | 2,565 | 17.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 42 | L1-worker | claudeopus46 | 2,320 | 2,696 | 5,016 | 772 | 5.4 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 43 | L1-worker | claudeopus46 | 627 | 2,576 | 3,203 | 793 | 6.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 44 | L1-worker | claudeopus46 | 366 | 1,209 | 1,575 | 737 | 3.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 45 | L1-worker | claudeopus46 | 366 | 1,204 | 1,570 | 780 | 4.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 46 | L1-worker | claudeopus46 | 2,106 | 3,736 | 5,842 | 2,532 | 11.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 47 | L1-worker | claudeopus46 | 366 | 3,309 | 3,675 | 1,751 | 8.3 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 48 | L1-worker | claudeopus46 | 787 | 42,937 | 43,724 | 547 | 6.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 49 | L0-main | claudeopus46 | 22,518 | 83,464 | 105,982 | 2,068 | 17.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 50 | L0-main | claudeopus46 | 22,518 | 84,267 | 106,785 | 1,111 | 8.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 51 | L0-main | claudeopus46 | 22,518 | 84,627 | 107,145 | 1,009 | 8.0 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 52 | L0-main | claudeopus46 | 22,518 | 85,392 | 107,910 | 1,266 | 9.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 53 | L0-main | claudeopus46 | 22,518 | 87,877 | 110,395 | 1,042 | 12.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 54 | L0-main | claudeopus46 | 22,518 | 88,690 | 111,208 | 801 | 6.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 55 | L0-main | claudeopus46 | 22,518 | 91,022 | 113,540 | 1,715 | 13.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 56 | L0-main | claudeopus46 | 22,518 | 91,827 | 114,345 | 1,131 | 9.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 57 | L0-main | claudeopus46 | 22,518 | 92,059 | 114,577 | 3,008 | 27.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 58 | L0-main | claudeopus46 | 22,518 | 95,540 | 118,058 | 8,083 | 61.7 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 59 | L0-main | claudeopus46 | 22,518 | 109,532 | 132,050 | 6,233 | 49.5 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 60 | L0-main | claudeopus46 | 22,518 | 121,737 | 144,255 | 6,121 | 48.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 61 | L0-main | claudeopus46 | 2,106 | 6,615 | 8,721 | 273 | 4.2 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 62 | L0-main | claudeopus46 | 366 | 796 | 1,162 | 259 | 2.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 63 | L0-main | claudeopus46 | 2,320 | 5,708 | 8,028 | 1,268 | 9.8 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 64 | L0-main | claudeopus46 | 366 | 1,705 | 2,071 | 1,223 | 5.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 65 | L0-main | claudeopus46 | 560 | 6,514 | 7,074 | 185 | 2.6 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 66 | L0-main | claudeopus46 | 1,156 | 7,997 | 9,153 | 819 | 7.9 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 67 | L0-main | claudeopus46 | 1,918 | 5,980 | 7,898 | 1,132 | 11.1 | Find and fit excess molar volume (VE) data for the binary mi (analysis_runs/run_7) |
| 1 | L0-main | claudeopus46 | 22,518 | 975 | 23,493 | 1,174 | 7.5 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 2 | L0-main | claudeopus46 | 22,518 | 1,673 | 24,191 | 802 | 5.2 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 3 | L0-main | claudeopus46 | 22,518 | 2,338 | 24,856 | 974 | 6.1 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 4 | L0-main | claudeopus46 | 22,518 | 3,161 | 25,679 | 929 | 6.3 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 5 | L0-main | claudeopus46 | 22,518 | 2,736 | 25,254 | 2,457 | 16.6 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 6 | L0-main | claudeopus46 | 22,518 | 3,550 | 26,068 | 1,060 | 10.1 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 7 | L0-main | claudeopus46 | 22,518 | 3,735 | 26,253 | 1,975 | 15.4 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 8 | L0-main | claudeopus46 | 22,518 | 4,315 | 26,833 | 2,514 | 20.0 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 9 | L0-main | claudeopus46 | 22,518 | 4,878 | 27,396 | 994 | 7.8 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 10 | L0-main | claudeopus46 | 22,518 | 5,385 | 27,903 | 5,544 | 39.7 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 11 | L0-main | claudeopus46 | 22,518 | 13,054 | 35,572 | 3,378 | 21.5 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 12 | L0-main | claudeopus46 | 22,518 | 18,548 | 41,066 | 2,491 | 13.7 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 13 | L0-main | claudeopus46 | 2,106 | 3,910 | 6,016 | 112 | 2.8 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 14 | L0-main | claudeopus46 | 366 | 635 | 1,001 | 116 | 2.3 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 15 | L0-main | claudeopus46 | 2,320 | 2,836 | 5,156 | 1,085 | 6.4 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 16 | L0-main | claudeopus46 | 366 | 1,522 | 1,888 | 1,040 | 4.8 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 17 | L0-main | claudeopus46 | 560 | 3,336 | 3,896 | 70 | 3.1 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 18 | L0-main | claudeopus46 | 1,156 | 4,135 | 5,291 | 509 | 6.2 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 19 | L0-main | claudeopus46 | 1,918 | 5,733 | 7,651 | 1,041 | 8.8 | Using the Redlich-Kister coefficients for methanol+water V^E (analysis_runs/run_9) |
| 1 | L0-main | claudeopus46 | 22,518 | 1,004 | 23,522 | 898 | 6.6 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 2 | L0-main | claudeopus46 | 22,518 | 2,287 | 24,805 | 1,648 | 9.3 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 3 | L0-main | claudeopus46 | 22,518 | 3,039 | 25,557 | 807 | 5.4 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 4 | L0-main | claudeopus46 | 22,518 | 2,140 | 24,658 | 1,968 | 14.6 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 5 | L0-main | claudeopus46 | 22,518 | 2,677 | 25,195 | 2,206 | 14.3 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 6 | L0-main | claudeopus46 | 22,518 | 3,278 | 25,796 | 2,425 | 18.8 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 7 | L0-main | claudeopus46 | 22,518 | 3,872 | 26,390 | 3,486 | 24.6 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 8 | L0-main | claudeopus46 | 22,518 | 4,421 | 26,939 | 7,003 | 50.0 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 9 | L0-main | claudeopus46 | 22,518 | 5,053 | 27,571 | 1,585 | 15.9 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 10 | L0-main | claudeopus46 | 22,518 | 8,960 | 31,478 | 2,614 | 16.5 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 11 | L0-main | claudeopus46 | 22,518 | 13,917 | 36,435 | 2,177 | 13.4 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 12 | L0-main | claudeopus46 | 2,106 | 2,968 | 5,074 | 31 | 1.7 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 13 | L0-main | claudeopus46 | 366 | 554 | 920 | 14 | 2.4 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 14 | L0-main | claudeopus46 | 2,320 | 1,866 | 4,186 | 799 | 5.1 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 15 | L0-main | claudeopus46 | 366 | 1,236 | 1,602 | 764 | 3.5 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 16 | L0-main | claudeopus46 | 1,918 | 4,143 | 6,061 | 1,023 | 9.5 | Using the Redlich-Kister coefficients for ethanol+water V^E  (analysis_runs/run_10) |
| 1 | L0-main | claudeopus46 | 22,518 | 979 | 23,497 | 1,527 | 10.3 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 2 | L0-main | claudeopus46 | 22,518 | 2,405 | 24,923 | 692 | 4.2 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 3 | L0-main | claudeopus46 | 22,518 | 3,103 | 25,621 | 803 | 4.8 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 4 | L0-main | claudeopus46 | 22,518 | 3,808 | 26,326 | 839 | 6.5 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 5 | L0-main | claudeopus46 | 22,518 | 2,413 | 24,931 | 1,356 | 11.6 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 6 | L0-main | claudeopus46 | 22,518 | 2,958 | 25,476 | 3,650 | 24.9 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 7 | L0-main | claudeopus46 | 22,518 | 3,628 | 26,146 | 4,384 | 29.7 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 8 | L0-main | claudeopus46 | 22,518 | 4,223 | 26,741 | 10,783 | 74.2 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 9 | L0-main | claudeopus46 | 22,518 | 15,406 | 37,924 | 2,789 | 27.4 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 10 | L0-main | claudeopus46 | 22,518 | 21,157 | 43,675 | 4,455 | 34.5 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 11 | L0-main | claudeopus46 | 22,518 | 28,586 | 51,104 | 4,249 | 33.4 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 12 | L0-main | claudeopus46 | 2,106 | 4,619 | 6,725 | 111 | 2.6 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 13 | L0-main | claudeopus46 | 366 | 634 | 1,000 | 115 | 2.0 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 14 | L0-main | claudeopus46 | 2,320 | 3,542 | 5,862 | 1,186 | 7.0 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 15 | L0-main | claudeopus46 | 366 | 1,623 | 1,989 | 1,141 | 4.2 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 16 | L0-main | claudeopus46 | 560 | 4,041 | 4,601 | 65 | 2.3 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 17 | L0-main | claudeopus46 | 1,156 | 4,856 | 6,012 | 473 | 5.7 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| 18 | L0-main | claudeopus46 | 1,918 | 5,446 | 7,364 | 1,111 | 10.0 | Using the Redlich-Kister coefficients for acetonitrile+DMF V (analysis_runs/run_11) |
| **TOTAL** |  |  | **3,621,640** | **3,553,132** | **7,174,772** | **353,810** | **2,690.1** |  |
