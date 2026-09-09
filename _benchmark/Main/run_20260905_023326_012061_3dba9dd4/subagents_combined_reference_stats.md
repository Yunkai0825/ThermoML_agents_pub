# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 28 | 459,518 | 1,159,744 | 42,103 | 1,619,262 | 57,830 | 327.1 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| L1-worker | 39 | 541,708 | 216,963 | 39,227 | 758,671 | 19,453 | 296.9 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| L0-main | 45 | 864,080 | 4,367,889 | 62,586 | 5,231,969 | 116,265 | 537.9 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| L1-worker | 44 | 601,166 | 415,676 | 57,545 | 1,016,842 | 23,110 | 416.9 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| L0-main | 23 | 369,080 | 857,564 | 38,279 | 1,226,644 | 53,332 | 307.3 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| L1-worker | 64 | 880,749 | 379,928 | 65,249 | 1,260,677 | 19,698 | 499.3 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| **TOTAL** | **243** | **3,716,301** | **7,397,764** | **304,989** | **11,114,065** | **289,688** | **2,385.4** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 206 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `search_blocks` | 2 | 1 | 6 | 2 | 9 | 9 | 1,349 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `search_blocks` | 2 | 1 | 6 | 2 | 9 | 9 | 1,349 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `query_thermoml_parallel` | 2 | 2 | 5 | 1 | 5 | 5 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `resolve_compound_ids` | 3 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `resolve_compound_ids` | 3 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `search_blocks` | 2 | 1 | 5 | 4 | 22 | 22 | 2,417 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `search_blocks` | 2 | 1 | 5 | 4 | 22 | 22 | 2,417 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `search_blocks` | 2 | 11 | 4 | 4 | 29 | 50 | 3,112 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `search_system_registry` | 2 | 1 | 5 | 3 | 17 | 17 | 2,366 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `query_thermoml_parallel` | 2 | 1 | 5 | 3 | 17 | 17 | 747 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `fit_block_derived` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `resolve_compound_ids` | 4 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `resolve_compound_ids` | 5 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `search_blocks` | 2 | 1 | 5 | 3 | 16 | 17 | 1,379 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `search_blocks` | 2 | 14 | 6 | 6 | 27 | 50 | 1,775 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `search_id_alignment` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `query_thermoml_parallel` | 2 | 1 | 5 | 1 | 3 | 3 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `search_blocks` | 2 | 1 | 5 | 3 | 16 | 17 | 1,379 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `query_thermoml` | 2 | 1 | 2 | 2 | 3 | 3 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| **TOTAL** | **45** | **41** | **67** | **38** | **196** | **242** | **18,496** |  |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | --- | --- |
| Unique References | 10 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Compounds | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Properties | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Measurements | 7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Phases | 1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Variables | 6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Solvents | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Constraints | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Block_Types | 1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique parent blocks | 10 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Explicit block/subsystem targets | 10 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Subsystem targets | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Target-matched data points | 4,158 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| GLOBcomp_1 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_2 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_5494 |  | resolve_compound_ids |
| GLOBprop_28 |  | resolve_property_ids |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBprop_3 | Activity coefficient | search_blocks |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBprop_17 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBprop_14 | Boiling temperature at pressure P, K | search_blocks |
| GLOBprop_2 | Mole fraction | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBprop_44 | Relative permittivity at zero frequency | search_blocks |
| GLOBprop_58 | Azeotropic temperature, K | search_blocks |
| GLOBprop_45 | Azeotropic composition: mole fraction | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBlit_220 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_1483 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_2432 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_2825 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_3475 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_4415 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_5201 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_5473 |  | search_blocks |
| GLOBlit_7085 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_7178 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_8050 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9006 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_10159 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_10699 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_10866 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_11005 |  | search_blocks |
| GLOBlit_11136 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_11504 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_11792 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBlit_299 |  | search_blocks |
| GLOBlit_384 |  | search_blocks |
| GLOBlit_528 |  | search_blocks |
| GLOBlit_742 |  | search_blocks |
| GLOBlit_757 |  | search_blocks |
| GLOBlit_977 |  | search_blocks |
| GLOBlit_1184 |  | search_blocks |
| GLOBlit_1197 |  | search_blocks |
| GLOBlit_1289 |  | search_blocks |
| GLOBlit_1482 |  | search_blocks |
| GLOBlit_1518 |  | search_blocks |
| GLOBlit_1742 |  | search_blocks |
| GLOBlit_1971 |  | search_blocks |
| GLOBlit_2035 |  | search_blocks |
| GLOBlit_2092 |  | search_blocks |
| GLOBlit_2220 |  | search_blocks |
| GLOBlit_2300 |  | search_blocks |
| GLOBlit_2574 |  | search_blocks |
| GLOBlit_2732 |  | search_blocks |
| GLOBlit_3697 |  | search_blocks |
| GLOBlit_3971 |  | search_blocks |
| GLOBlit_4181 |  | search_blocks |
| GLOBlit_5073 |  | search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_66 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_236 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_203 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_212 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_141 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_6 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBmeas_543 | Activity coefficient | search_blocks |
| GLOBmeas_1045 | Activity coefficient | search_blocks |
| GLOBmeas_1042 | Activity coefficient | search_blocks |
| GLOBmeas_133 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_13 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_5 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_1362 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_2137 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_131 | Mole fraction | search_blocks |
| GLOBmeas_1 | Mole fraction | search_blocks |
| GLOBmeas_10 | Mole fraction | search_blocks |
| GLOBmeas_664 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_12 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_1153 | Activity coefficient | search_blocks |
| GLOBmeas_1355 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_169 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_161 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_1497 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_53 | Relative permittivity at zero frequency | search_blocks |
| GLOBmeas_39 | Azeotropic temperature, K | search_blocks |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks |
| GLOBmeas_24 | Mole fraction | search_blocks |
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBphase_3 |  | search_blocks |
| GLOBphase_10 |  | search_blocks |
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBsolvent_1 |  | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBsolvent_2 |  | search_blocks |
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_8 | Molality, mol/kg | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBconstr_22 | Volume fraction | query_thermoml_parallel, search_blocks, search_system_registry |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |
| GLOBblocktype_1 |  | query_thermoml_parallel, search_system_registry |
| Unique Compounds | 3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique Properties | 12 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique References | 45 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique Measurements | 33 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique Phases | 3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique Variables | 5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique Solvents | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique Constraints | 6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique Block_Types | 1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique parent blocks | 66 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Explicit block/subsystem targets | 66 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Subsystem targets | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Target-matched data points | 12,678 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| GLOBcomp_1 |  | query_thermoml, query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_797 |  | resolve_compound_ids |
| GLOBcomp_1168 |  | resolve_compound_ids |
| GLOBcomp_6445 |  | resolve_compound_ids |
| GLOBcomp_241 |  | resolve_compound_ids |
| GLOBcomp_5 |  | query_thermoml, query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBprop_28 |  | resolve_property_ids, search_id_alignment |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBprop_3 | Activity coefficient | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBprop_29 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBprop_2 | Mole fraction | search_blocks |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBprop_14 | Boiling temperature at pressure P, K | search_blocks |
| GLOBprop_45 | Azeotropic composition: mole fraction | search_blocks |
| GLOBprop_58 | Azeotropic temperature, K | search_blocks |
| GLOBprop_46 | Molar enthalpy of dilution, kJ/mol | search_blocks |
| GLOBprop_18 | Electrical conductivity, S/m | search_blocks |
| GLOBprop_15 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks |
| GLOBlit_555 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_590 |  | search_blocks |
| GLOBlit_2432 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2979 |  | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBlit_4068 |  | search_blocks |
| GLOBlit_4415 |  | search_blocks |
| GLOBlit_5585 |  | search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_8254 |  | search_blocks |
| GLOBlit_8447 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_11042 |  | query_thermoml, search_blocks |
| GLOBlit_11142 |  | query_thermoml, search_blocks |
| GLOBlit_11872 |  | search_blocks |
| GLOBlit_299 |  | search_blocks |
| GLOBlit_766 |  | search_blocks |
| GLOBlit_970 |  | search_blocks |
| GLOBlit_996 |  | search_blocks |
| GLOBlit_1742 |  | search_blocks |
| GLOBlit_2060 |  | search_blocks |
| GLOBlit_2092 |  | search_blocks |
| GLOBlit_3518 |  | search_blocks |
| GLOBlit_3796 |  | search_blocks |
| GLOBlit_4843 |  | search_blocks |
| GLOBlit_5053 |  | search_blocks |
| GLOBlit_5059 |  | search_blocks |
| GLOBlit_5124 |  | search_blocks |
| GLOBlit_6268 |  | search_blocks |
| GLOBlit_6460 |  | search_blocks |
| GLOBlit_6553 |  | search_blocks |
| GLOBlit_7483 |  | search_blocks |
| GLOBlit_7818 |  | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_143 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_543 | Activity coefficient | search_blocks |
| GLOBmeas_1045 | Activity coefficient | search_blocks |
| GLOBmeas_1042 | Activity coefficient | search_blocks |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks |
| GLOBmeas_922 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBmeas_933 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBmeas_1 | Mole fraction | search_blocks |
| GLOBmeas_133 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_5 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_39 | Azeotropic composition: mole fraction | search_blocks |
| GLOBmeas_13 | Molar enthalpy of dilution, kJ/mol | search_blocks |
| GLOBmeas_10 | Mole fraction | search_blocks |
| GLOBmeas_14 | Electrical conductivity, S/m | search_blocks |
| GLOBmeas_137 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_18 | Speed of sound, m/s | search_blocks |
| GLOBmeas_25 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_144 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks |
| GLOBphase_1 |  | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBphase_3 |  | search_blocks |
| GLOBvar_1 | Temperature, K | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_3 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBvar_4 | Molality, mol/kg | query_thermoml_parallel, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBvar_32 | Initial mass fraction of solute | search_blocks |
| GLOBconstr_1 | Pressure, kPa | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_2 | Temperature, K | query_thermoml, search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_25 | Final mass fraction of solute | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |
| GLOBsolvent_1 |  | query_thermoml_parallel, search_blocks |
| GLOBsolvent_9 |  | search_blocks |
| GLOBblocktype_1 |  | query_thermoml, query_thermoml_parallel |
| Unique Compounds | 6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| Unique Properties | 15 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| Unique References | 34 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| Unique Measurements | 27 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| Unique Phases | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| Unique Variables | 6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| Unique Constraints | 6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| Unique Solvents | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| Unique Block_Types | 1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| Unique parent blocks | 57 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| Explicit block/subsystem targets | 57 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| Subsystem targets | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| Target-matched data points | 5,265 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| **TOTAL** | **22,609** |  |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 10.1016/j.jct.2004.03.011 | PROPblock_1 | declared | 206 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2005.08.018 | 3 | 13 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2006.04.017 | 1 | 28 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2007.06.007 | 2 | 30 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2009.10.002 | 2 | 10 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2009.11.014 | 2 | 36 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2011.06.009 | 2 | 90 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2012.11.026 | 2 | 48 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2012.12.014 | 2 | 152 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2013.07.001 | 1 | 42 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2014.05.031 | 1 | 56 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2014.07.022 | 2 | 14 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2015.07.012 | 2 | 168 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2016.08.030 | 1 | 4 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2017.03.010 | 2 | 34 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2017.09.005 | 2 | 144 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2018.07.014 | 1 | 17 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2019.03.019 | 2 | 32 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2004.07.019 | 1 | 565 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2005.06.018 | 1 | 27 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2006.08.002 | 4 | 326 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2007.05.004 | 2 | 74 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2012.08.009 | 1 | 14 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2013.08.020 | 4 | 34 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2014.05.020 | 1 | 30 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2015.06.024 | 2 | 80 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2017.07.021 | 1 | 24 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2018.02.022 | 1 | 244 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/acs.jced.8b00086 | 1 | 6 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/acs.jced.8b00939 | 1 | 9 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je020173z | 1 | 24 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je060335h | 1 | 164 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je4003515 | 1 | 23 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je600565m | 1 | 18 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je700300y | 1 | 84 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je700618y | 1 | 15 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je800150h | 1 | 108 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je900064e | 1 | 10 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je900743e | 1 | 15 | binary | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2005.08.018 | PROPblock_4 | declared | 2 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2005.08.018 | PROPblock_5 | declared | 7 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2005.08.018 | PROPblock_6 | declared | 4 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2006.04.017 | PROPblock_3 | declared | 28 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2007.06.007 | PROPblock_1 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2007.06.007 | PROPblock_2 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2009.10.002 | PROPblock_17 | declared | 5 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2009.10.002 | PROPblock_18 | declared | 5 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2009.11.014 | PROPblock_2 | declared | 18 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2009.11.014 | PROPblock_3 | declared | 18 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2011.06.009 | PROPblock_1 | declared | 45 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2011.06.009 | PROPblock_2 | declared | 45 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2012.11.026 | PROPblock_4 | declared | 24 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2012.11.026 | PROPblock_5 | declared | 24 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2012.12.014 | PROPblock_2 | declared | 76 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2012.12.014 | PROPblock_3 | declared | 76 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2013.07.001 | PROPblock_6 | declared | 42 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2014.05.031 | PROPblock_4 | declared | 56 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2014.07.022 | PROPblock_1 | declared | 7 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2014.07.022 | PROPblock_2 | declared | 7 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_3 | declared | 84 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_4 | declared | 84 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2016.08.030 | PROPblock_1 | declared | 4 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2017.03.010 | PROPblock_7 | declared | 17 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2017.03.010 | PROPblock_8 | declared | 17 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_3 | declared | 72 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_4 | declared | 72 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2018.07.014 | PROPblock_4 | declared | 17 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2019.03.019 | PROPblock_8 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2019.03.019 | PROPblock_9 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2005.06.018 | PROPblock_4 | declared | 27 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2006.08.002 | PROPblock_1 | declared | 25 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2006.08.002 | PROPblock_2 | declared | 19 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2006.08.002 | PROPblock_3 | declared | 4 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2006.08.002 | PROPblock_4 | declared | 278 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2012.08.009 | PROPblock_18 | declared | 14 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2013.08.020 | PROPblock_10 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2013.08.020 | PROPblock_11 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2013.08.020 | PROPblock_12 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2013.08.020 | PROPblock_9 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2014.05.020 | PROPblock_1 | declared | 30 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2015.06.024 | PROPblock_8 | declared | 40 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2017.07.021 | PROPblock_3 | declared | 24 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je900064e | PROPblock_6 | declared | 10 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je900743e | PROPblock_3 | declared | 15 | binary | 2 | query_thermoml_parallel, search_blocks, search_system_registry | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2005.08.018 | 3 | 14 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.fluid.2007.07.066 | 2 | 30 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.fluid.2008.01.004 | 2 | 30 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.fluid.2009.12.009 | 2 | 16 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.fluid.2011.05.016 | 1 | 12 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.fluid.2011.08.009 | 1 | 28 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.fluid.2015.07.012 | 2 | 168 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.fluid.2017.05.012 | 4 | 34 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.fluid.2017.09.005 | 2 | 144 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.jct.2004.07.019 | 1 | 456 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | query_thermoml, query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.jct.2011.12.018 | 1 | 22 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.jct.2012.12.019 | 2 | 74 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.jct.2013.11.036 | 2 | 203 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.jct.2015.06.024 | 2 | 80 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.jct.2016.10.001 | 2 | 36 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.jct.2017.06.014 | 2 | 42 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.jct.2017.07.003 | 1 | 36 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.jct.2017.10.005 | 2 | 10 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.jct.2019.105880 | 3 | 48 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.tca.2015.09.022 | 1 | 1 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.tca.2018.09.022 | 1 | 1 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1021/acs.jced.5b00200 | 1 | 1 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1021/acs.jced.7b00299 | 3 | 5 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1021/acs.jced.8b00181 | 2 | 10 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1021/acs.jced.9b00102 | 3 | 166 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1021/je034101z | 1 | 380 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1021/je049738c | 1 | 8 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1021/je4003515 | 1 | 25 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1021/je700700f | 1 | 13 | binary | query_thermoml, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1021/je800158z | 1 | 56 | binary | query_thermoml, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1021/je900966r | 1 | 30 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |  |  |
| 10.1016/j.fluid.2005.08.018 | PROPblock_7 | declared | 3 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2005.08.018 | PROPblock_8 | declared | 7 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2005.08.018 | PROPblock_9 | declared | 4 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2007.07.066 | PROPblock_7 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2007.07.066 | PROPblock_8 | declared | 15 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2008.01.004 | PROPblock_4 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2008.01.004 | PROPblock_5 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2009.12.009 | PROPblock_7 | declared | 8 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2009.12.009 | PROPblock_8 | declared | 8 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2011.05.016 | PROPblock_1 | declared | 12 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2011.08.009 | PROPblock_6 | declared | 28 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_5 | declared | 84 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_6 | declared | 84 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2017.05.012 | PROPblock_4 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2017.05.012 | PROPblock_5 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2017.05.012 | PROPblock_6 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2017.05.012 | PROPblock_7 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_5 | declared | 72 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_6 | declared | 72 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2004.07.019 | PROPblock_3 | declared | 456 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2008.07.005 | PROPblock_9 | declared | 96 | binary | 2 | query_thermoml, query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2011.12.018 | PROPblock_1 | declared | 22 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2012.12.019 | PROPblock_2 | declared | 37 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2012.12.019 | PROPblock_3 | declared | 37 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2013.11.036 | PROPblock_1 | declared | 174 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2013.11.036 | PROPblock_2 | declared | 29 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2015.06.024 | PROPblock_5 | declared | 40 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2015.06.024 | PROPblock_6 | declared | 40 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2016.10.001 | PROPblock_7 | declared | 18 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2016.10.001 | PROPblock_8 | declared | 18 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2017.06.014 | PROPblock_3 | declared | 21 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2017.06.014 | PROPblock_4 | declared | 21 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2017.07.003 | PROPblock_6 | declared | 36 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2017.10.005 | PROPblock_13 | declared | 5 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2017.10.005 | PROPblock_14 | declared | 5 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2019.105880 | PROPblock_7 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2019.105880 | PROPblock_8 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.jct.2019.105880 | PROPblock_9 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.tca.2015.09.022 | PROPblock_43 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1016/j.tca.2018.09.022 | PROPblock_5 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/acs.jced.5b00200 | PROPblock_19 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/acs.jced.6b01058 | PROPblock_8 | declared | 12 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/acs.jced.7b00299 | PROPblock_13 | declared | 2 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/acs.jced.7b00299 | PROPblock_14 | declared | 2 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/acs.jced.7b00299 | PROPblock_15 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/acs.jced.8b00181 | PROPblock_8 | declared | 5 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/acs.jced.8b00181 | PROPblock_9 | declared | 5 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/acs.jced.9b00102 | PROPblock_11 | declared | 60 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/acs.jced.9b00102 | PROPblock_12 | declared | 60 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/acs.jced.9b00102 | PROPblock_13 | declared | 46 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/je034101z | PROPblock_6 | declared | 380 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/je049738c | PROPblock_26 | declared | 8 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/je0601098 | PROPblock_22 | declared | 12 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/je4003515 | PROPblock_10 | declared | 25 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/je700700f | PROPblock_14 | declared | 13 | binary | 2 | query_thermoml, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/je800158z | PROPblock_3 | declared | 56 | binary | 2 | query_thermoml, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10.1021/je900966r | PROPblock_4 | declared | 30 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| **TOTAL** | **123** | **6,166** | **7,721** |  | **54** |  |  |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | --- | ---: | --- |
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'direct_VE', 'purp… | 132 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 2 | 1 | `resolve_compound_ids` | purpose=Resolve water and methanol to…, queries=['… | 212 | KEEP ←in 277 | 212 | 4.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve global IDs … | 213 | KEEP ←in 408 | 213 | 5.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 4 | 3 | `resolve_property_ids` | limit=10, min_score=50, purpose=Resolve excess mol… | 202 | KEEP ←in 227 | 202 | 3.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 5 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 973 | KEEP ←in 3,972 | 958 | 15.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 6 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 164 | KEEP ←in 5,885 | 164 | 23.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 7 | 6 | `inspect_block_table` | block_number=GLOBlit_2395::PROPblock_1, purpose=Gr… | 375 | — | — | 0.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 8 | 7 | `inspect_block_table` | block_number=GLOBlit_2395::PROPblock_1, purpose=Gr… | 2,077 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 9 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=20, p… | 1,176 | KEEP ←in 5,885 | 1161 | 17.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10 | 7 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2432,… | 245 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 11 | 8 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2432,… | 391 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 12 | 9 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2432,… | 982 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 13 | 10 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 958 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 14 | 11 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_7085,… | 953 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 15 | 12 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_8254,… | 921 | — | — | 0.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 16 | 2 | `query_thermoml_parallel` | queries=[{'label': 'direct_VE', 'purp… | 62,286 | — | — | 180.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 17 | 7 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 237 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 18 | 10 | `inspect_block` | block_number=PROPblock_10, doi=10.1016/j.jct.2007.… | 1,360 | — | — | 0.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 19 | 14 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 954 | — | — | 1.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 20 | 16 | `predict_from_rk` | coeffs=[-3.98239e-06, -1.5386e-07, 1…, mixing_rule… | 207 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 21 | 17 | `list_session_files` |  | 1,681 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 224 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 2 | 2 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 253 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 3 | 3 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 152 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 4 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve water and e… | 307 | KEEP ←in 351 | 307 | 6.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 5 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve water and e… | 270 | KEEP ←in 351 | 270 | 5.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 6 | 4 | `resolve_property_ids` | limit=10, min_score=60, purpose=Find excess molar … | 256 | KEEP ←in 227 | 256 | 4.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 7 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 303 | KEEP ←in 14,080 | 303 | 17.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 8 | 6 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,076 | DISCARD ←in 39 | 1018 | 10.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 9 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=30, p… | 677 | KEEP ←in 14,080 | 659 | 16.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10 | 7 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,412 | KEEP ←in 30,867 | 1250 | 15.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 11 | 6 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,355 | KEEP ←in 2,557 | 1095 | 10.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 12 | 8 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=20, p… | 725 | DISCARD ←in 39 | 667 | 16.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 13 | 8 | `inspect_block_table` | block_number=GLOBlit_220::PROPblock_2, purpose=Ins… | 369 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 14 | 9 | `inspect_block_table` | block_number=GLOBlit_220::PROPblock_2, purpose=Gro… | 2,089 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 15 | 10 | `inspect_block_table` | block_number=GLOBlit_2432::PROPblock_2, purpose=Gr… | 4,539 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 16 | 11 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_19, purpose=I… | 1,805 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 17 | 4 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 163,237 | — | — | 278.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 18 | 7 | `inspect_block` | block_number=PROPblock_1, doi=10.1021/je060335h, p… | 1,359 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 19 | 9 | `fit_block_derived` | block_number=PROPblock_1, composition_hint=mole_fr… | 208 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 20 | 13 | `fit_block_derived` | block_number=PROPblock_1, composition_hint=mole_fr… | 301 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 21 | 16 | `fit_block_derived` | block_number=PROPblock_1, composition_hint=mole_fr… | 230 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 22 | 17 | `fit_block_derived` | block_number=PROPblock_1, composition_hint=mole_fr… | 954 | — | — | 1.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 23 | 18 | `predict_from_rk` | coeffs=[-4.64231e-06, 1.53527e-06, -…, n_points=10… | 205 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 24 | 19 | `fit_block_derived` | block_number=PROPblock_19, composition_hint=mole_f… | 961 | — | — | 1.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 25 | 20 | `predict_from_rk` | coeffs=[-3.38039e-06, 2.37917e-06, -…, mixing_rule… | 206 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 26 | 21 | `list_session_files` |  | 3,077 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 27 | 23 | `inspect_block` | block_number=PROPblock_1, doi=10.1021/je060335h, p… | 1,359 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 28 | 25 | `inspect_block` | block_number=PROPblock_1, doi=10.1021/je060335h, p… | 1,359 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 218 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 2 | 2 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 253 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve water and 1… | 569 | KEEP ←in 428 | 569 | 9.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 4 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 548 | KEEP ←in 496 | 548 | 9.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 5 | 3 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Resolve 1-propanol… | 202 | KEEP ←in 227 | 202 | 3.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 6 | 3 | `resolve_compound_ids` | limit=10, min_score=50, purpose=Find GLOBcomp ID f… | 267 | KEEP ←in 227 | 267 | 5.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 7 | 4 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find GLOBprop ID f… | 200 | KEEP ←in 227 | 200 | 3.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 8 | 6 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 918 | DISCARD ←in 39 | 860 | 8.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 9 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 1,200 | KEEP ←in 11,346 | 1185 | 20.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10 | 7 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 1,044 | DISCARD ←in 39 | 986 | 18.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 11 | 7 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2979,… | 249 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 12 | 8 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2979,… | 377 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 13 | 9 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2979,… | 1,598 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 14 | 8 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 768 | KEEP ←in 31,749 | 632 | 21.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 15 | 10 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_555, … | 883 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 16 | 9 | `search_id_alignment` | entity_type=property, limit=20, purpose=Find alter… | 310 | KEEP ←in 289 | 310 | 4.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 17 | 11 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_2432,… | 957 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 18 | 3 | `query_thermoml_parallel` | queries=[{'label': 'VE_direct', 'purp… | 38,620 | — | — | 174.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 19 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 423 | KEEP ←in 11,346 | 391 | 20.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 20 | 3 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 1,195 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 21 | 4 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11142… | 259 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 22 | 5 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11142… | 372 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 23 | 6 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11142… | 373 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 24 | 7 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11142… | 944 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 25 | 8 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 962 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 26 | 9 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 1,157 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 27 | 11 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2979,… | 1,629 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 28 | 4 | `query_thermoml` | context=Previously found 17 density b…, id_catalog… | 32,146 | — | — | 157.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 29 | 7 | `inspect_block` | block_number=PROPblock_14, doi=10.1021/je700700f, … | 1,367 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 30 | 11 | `fit_block_derived` | block_number=PROPblock_14, composition_hint=mole_f… | 957 | — | — | 1.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 31 | 12 | `predict_from_rk` | coeffs=[-2.58261e-06, 6.379e-07, -7.…, n_points=10… | 210 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 32 | 13 | `list_session_files` |  | 1,561 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| **TOTAL** | **639** |  |  | **358,703** |  | **14,885** | **1,099.2** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 22,518 | 717 | 23,235 | 1,731 | 11.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 2 | L0-main | claudeopus46 | 22,518 | 1,162 | 23,680 | 1,130 | 6.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 3 | L1-worker | claudeopus46 | 24,095 | 852 | 24,947 | 614 | 4.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 4 | L1-worker | claudeopus46 | 24,095 | 851 | 24,946 | 854 | 6.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 5 | L1-worker | claudeopus46 | 3,767 | 468 | 4,235 | 382 | 4.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,909 | 26,004 | 588 | 4.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 7 | L1-worker | claudeopus46 | 24,095 | 1,308 | 25,403 | 464 | 5.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 8 | L1-worker | claudeopus46 | 3,767 | 591 | 4,358 | 463 | 4.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 9 | L1-worker | claudeopus46 | 24,095 | 2,319 | 26,414 | 534 | 3.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10 | L1-worker | claudeopus46 | 3,767 | 378 | 4,145 | 330 | 3.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 11 | L1-worker | claudeopus46 | 24,095 | 1,507 | 25,602 | 862 | 6.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 12 | L1-worker | claudeopus46 | 24,095 | 2,219 | 26,314 | 641 | 5.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 13 | L1-worker | claudeopus46 | 24,095 | 1,945 | 26,040 | 821 | 6.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,691 | 26,786 | 696 | 5.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 15 | L1-worker | claudeopus46 | 3,767 | 4,455 | 8,222 | 1,398 | 13.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 16 | L1-worker | claudeopus46 | 3,767 | 6,351 | 10,118 | 1,719 | 15.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 17 | L1-worker | claudeopus46 | 24,095 | 3,649 | 27,744 | 960 | 7.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 18 | L1-worker | claudeopus46 | 24,095 | 2,358 | 26,453 | 805 | 5.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 19 | L1-worker | claudeopus46 | 24,095 | 4,460 | 28,555 | 572 | 5.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 20 | L1-worker | claudeopus46 | 3,767 | 6,356 | 10,123 | 1,628 | 16.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 21 | L1-worker | claudeopus46 | 24,095 | 6,831 | 30,926 | 2,533 | 20.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 22 | L1-worker | claudeopus46 | 2,106 | 3,637 | 5,743 | 594 | 4.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 23 | L1-worker | claudeopus46 | 2,320 | 2,664 | 4,984 | 896 | 5.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 24 | L1-worker | claudeopus46 | 627 | 2,544 | 3,171 | 952 | 7.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 25 | L1-worker | claudeopus46 | 366 | 1,371 | 1,737 | 328 | 2.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 26 | L1-worker | claudeopus46 | 366 | 1,333 | 1,699 | 851 | 3.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 27 | L1-worker | claudeopus46 | 24,095 | 3,900 | 27,995 | 3,099 | 18.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 28 | L1-worker | claudeopus46 | 787 | 12,956 | 13,743 | 577 | 6.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 29 | L1-worker | claudeopus46 | 24,095 | 9,872 | 33,967 | 590 | 5.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 30 | L1-worker | claudeopus46 | 24,095 | 10,396 | 34,491 | 514 | 5.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 31 | L1-worker | claudeopus46 | 24,095 | 11,059 | 35,154 | 632 | 5.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 32 | L1-worker | claudeopus46 | 24,095 | 12,343 | 36,438 | 620 | 6.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 33 | L1-worker | claudeopus46 | 24,095 | 13,650 | 37,745 | 635 | 5.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 34 | L1-worker | claudeopus46 | 24,095 | 14,892 | 38,987 | 591 | 5.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 35 | L1-worker | claudeopus46 | 24,062 | 15,775 | 39,837 | 3,214 | 25.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 36 | L1-worker | claudeopus46 | 2,320 | 3,345 | 5,665 | 1,133 | 6.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 37 | L1-worker | claudeopus46 | 627 | 3,225 | 3,852 | 1,204 | 9.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 38 | L1-worker | claudeopus46 | 366 | 1,570 | 1,936 | 1,083 | 4.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 39 | L1-worker | claudeopus46 | 2,106 | 4,317 | 6,423 | 2,640 | 12.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 40 | L1-worker | claudeopus46 | 366 | 3,417 | 3,783 | 1,644 | 7.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 41 | L1-worker | claudeopus46 | 787 | 33,199 | 33,986 | 566 | 6.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 42 | L0-main | claudeopus46 | 22,518 | 54,843 | 77,361 | 2,675 | 21.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 43 | L0-main | claudeopus46 | 22,518 | 56,100 | 78,618 | 1,190 | 9.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 44 | L0-main | claudeopus46 | 22,518 | 56,891 | 79,409 | 781 | 4.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 45 | L0-main | claudeopus46 | 22,518 | 57,637 | 80,155 | 866 | 4.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 46 | L0-main | claudeopus46 | 22,518 | 58,431 | 80,949 | 769 | 5.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 47 | L0-main | claudeopus46 | 22,518 | 57,090 | 79,608 | 872 | 6.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 48 | L0-main | claudeopus46 | 22,518 | 57,898 | 80,416 | 647 | 4.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 49 | L0-main | claudeopus46 | 22,518 | 58,609 | 81,127 | 532 | 4.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 50 | L0-main | claudeopus46 | 22,518 | 60,145 | 82,663 | 1,224 | 9.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 51 | L0-main | claudeopus46 | 22,518 | 60,939 | 83,457 | 860 | 7.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 52 | L0-main | claudeopus46 | 22,518 | 61,646 | 84,164 | 876 | 5.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 53 | L0-main | claudeopus46 | 22,518 | 62,405 | 84,923 | 849 | 5.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 54 | L0-main | claudeopus46 | 22,518 | 64,243 | 86,761 | 1,791 | 15.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 55 | L0-main | claudeopus46 | 22,518 | 65,182 | 87,700 | 831 | 6.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 56 | L0-main | claudeopus46 | 22,518 | 65,342 | 87,860 | 4,834 | 35.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 57 | L0-main | claudeopus46 | 22,518 | 67,418 | 89,936 | 3,760 | 31.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 58 | L0-main | claudeopus46 | 22,518 | 75,398 | 97,916 | 4,954 | 40.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 59 | L0-main | claudeopus46 | 22,518 | 83,818 | 106,336 | 4,499 | 38.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 60 | L0-main | claudeopus46 | 2,106 | 5,643 | 7,749 | 274 | 3.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 61 | L0-main | claudeopus46 | 366 | 797 | 1,163 | 260 | 2.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 62 | L0-main | claudeopus46 | 2,320 | 4,827 | 7,147 | 1,251 | 11.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 63 | L0-main | claudeopus46 | 366 | 1,688 | 2,054 | 1,206 | 5.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 64 | L0-main | claudeopus46 | 560 | 5,634 | 6,194 | 186 | 2.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 65 | L0-main | claudeopus46 | 1,156 | 7,103 | 8,259 | 1,059 | 10.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 66 | L0-main | claudeopus46 | 366 | 1,752 | 2,118 | 1,024 | 5.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 67 | L0-main | claudeopus46 | 1,918 | 6,386 | 8,304 | 1,172 | 12.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 1 | L0-main | claudeopus46 | 22,518 | 649 | 23,167 | 2,137 | 12.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 2 | L0-main | claudeopus46 | 22,518 | 1,196 | 23,714 | 1,586 | 9.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 3 | L0-main | claudeopus46 | 22,518 | 1,728 | 24,246 | 1,859 | 9.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 4 | L0-main | claudeopus46 | 22,518 | 2,171 | 24,689 | 1,484 | 9.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 5 | L1-worker | claudeopus46 | 24,095 | 897 | 24,992 | 649 | 5.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 6 | L1-worker | claudeopus46 | 24,095 | 863 | 24,958 | 824 | 6.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 7 | L1-worker | claudeopus46 | 24,095 | 1,930 | 26,025 | 548 | 4.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 8 | L1-worker | claudeopus46 | 24,095 | 1,896 | 25,991 | 532 | 4.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 9 | L1-worker | claudeopus46 | 3,767 | 510 | 4,277 | 468 | 5.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10 | L1-worker | claudeopus46 | 3,767 | 510 | 4,277 | 431 | 4.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 11 | L1-worker | claudeopus46 | 24,095 | 1,632 | 25,727 | 821 | 6.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 12 | L1-worker | claudeopus46 | 24,095 | 1,545 | 25,640 | 808 | 6.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 13 | L1-worker | claudeopus46 | 24,095 | 2,334 | 26,429 | 684 | 4.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,286 | 26,381 | 516 | 4.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 15 | L1-worker | claudeopus46 | 3,767 | 381 | 4,148 | 388 | 4.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 16 | L1-worker | claudeopus46 | 24,095 | 2,431 | 26,526 | 808 | 6.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 17 | L1-worker | claudeopus46 | 24,095 | 3,175 | 27,270 | 656 | 5.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 18 | L1-worker | claudeopus46 | 3,767 | 14,542 | 18,309 | 1,767 | 16.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 19 | L1-worker | claudeopus46 | 3,767 | 598 | 4,365 | 1,231 | 9.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 20 | L1-worker | claudeopus46 | 24,095 | 2,607 | 26,702 | 1,323 | 9.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 21 | L1-worker | claudeopus46 | 24,095 | 4,194 | 28,289 | 842 | 6.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 22 | L1-worker | claudeopus46 | 3,767 | 14,569 | 18,336 | 1,660 | 15.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 23 | L1-worker | claudeopus46 | 3,767 | 31,260 | 35,027 | 1,981 | 13.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 24 | L1-worker | claudeopus46 | 24,095 | 3,625 | 27,720 | 1,189 | 8.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 25 | L1-worker | claudeopus46 | 24,095 | 5,957 | 30,052 | 1,656 | 11.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 26 | L1-worker | claudeopus46 | 3,767 | 3,050 | 6,817 | 1,341 | 10.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 27 | L1-worker | claudeopus46 | 3,767 | 454 | 4,221 | 945 | 7.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 28 | L1-worker | claudeopus46 | 24,095 | 5,345 | 29,440 | 3,032 | 19.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 29 | L1-worker | claudeopus46 | 24,095 | 7,081 | 31,176 | 1,742 | 11.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 30 | L1-worker | claudeopus46 | 2,106 | 2,284 | 4,390 | 92 | 2.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 31 | L1-worker | claudeopus46 | 2,320 | 1,300 | 3,620 | 488 | 3.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 32 | L1-worker | claudeopus46 | 627 | 1,180 | 1,807 | 614 | 3.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 33 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 34 | L1-worker | claudeopus46 | 24,095 | 12,461 | 36,556 | 1,572 | 11.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 35 | L1-worker | claudeopus46 | 366 | 925 | 1,291 | 458 | 2.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 36 | L1-worker | claudeopus46 | 787 | 3,547 | 4,334 | 436 | 4.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 37 | L1-worker | claudeopus46 | 24,095 | 13,164 | 37,259 | 596 | 5.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 38 | L1-worker | claudeopus46 | 24,095 | 15,552 | 39,647 | 575 | 7.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 39 | L1-worker | claudeopus46 | 24,095 | 20,397 | 44,492 | 937 | 12.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 40 | L1-worker | claudeopus46 | 24,095 | 22,597 | 46,692 | 3,105 | 25.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 41 | L1-worker | claudeopus46 | 24,062 | 32,865 | 56,927 | 3,779 | 28.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 42 | L1-worker | claudeopus46 | 24,062 | 36,677 | 60,739 | 3,657 | 26.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 43 | L1-worker | claudeopus46 | 627 | 5,569 | 6,196 | 1,136 | 9.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 44 | L1-worker | claudeopus46 | 2,320 | 5,689 | 8,009 | 1,380 | 10.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 45 | L1-worker | claudeopus46 | 366 | 1,817 | 2,183 | 1,330 | 5.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 46 | L1-worker | claudeopus46 | 2,106 | 6,707 | 8,813 | 5,408 | 21.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 47 | L1-worker | claudeopus46 | 366 | 6,185 | 6,551 | 4,296 | 17.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 48 | L1-worker | claudeopus46 | 787 | 112,219 | 113,006 | 777 | 10.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 49 | L0-main | claudeopus46 | 22,485 | 114,022 | 136,507 | 471 | 7.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 50 | L0-main | claudeopus46 | 22,518 | 113,263 | 135,781 | 1,680 | 16.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 51 | L0-main | claudeopus46 | 22,518 | 114,043 | 136,561 | 926 | 7.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 52 | L0-main | claudeopus46 | 22,518 | 114,816 | 137,334 | 1,055 | 7.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 53 | L0-main | claudeopus46 | 22,485 | 117,045 | 139,530 | 373 | 5.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 54 | L0-main | claudeopus46 | 22,518 | 116,284 | 138,802 | 1,580 | 15.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 55 | L0-main | claudeopus46 | 22,518 | 117,065 | 139,583 | 768 | 7.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 56 | L0-main | claudeopus46 | 22,485 | 118,146 | 140,631 | 473 | 5.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 57 | L0-main | claudeopus46 | 22,518 | 117,385 | 139,903 | 934 | 8.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 58 | L0-main | claudeopus46 | 22,518 | 118,113 | 140,631 | 1,013 | 8.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 59 | L0-main | claudeopus46 | 22,518 | 118,837 | 141,355 | 837 | 6.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 60 | L0-main | claudeopus46 | 22,518 | 119,612 | 142,130 | 832 | 7.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 61 | L0-main | claudeopus46 | 22,485 | 120,146 | 142,631 | 572 | 6.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 62 | L0-main | claudeopus46 | 22,518 | 119,384 | 141,902 | 716 | 7.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 63 | L0-main | claudeopus46 | 22,518 | 120,084 | 142,602 | 794 | 6.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 64 | L0-main | claudeopus46 | 22,518 | 120,836 | 143,354 | 849 | 6.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 65 | L0-main | claudeopus46 | 22,485 | 121,635 | 144,120 | 521 | 9.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 66 | L0-main | claudeopus46 | 22,518 | 120,873 | 143,391 | 930 | 17.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 67 | L0-main | claudeopus46 | 22,485 | 124,318 | 146,803 | 432 | 5.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 68 | L0-main | claudeopus46 | 22,518 | 123,556 | 146,074 | 1,532 | 12.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 69 | L0-main | claudeopus46 | 22,485 | 124,967 | 147,452 | 499 | 6.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 70 | L0-main | claudeopus46 | 22,518 | 124,205 | 146,723 | 1,644 | 12.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 71 | L0-main | claudeopus46 | 22,485 | 127,743 | 150,228 | 399 | 7.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 72 | L0-main | claudeopus46 | 22,518 | 126,981 | 149,499 | 1,724 | 13.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 73 | L0-main | claudeopus46 | 22,485 | 128,309 | 150,794 | 397 | 7.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 74 | L0-main | claudeopus46 | 22,518 | 127,547 | 150,065 | 2,705 | 21.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 75 | L0-main | claudeopus46 | 22,485 | 131,711 | 154,196 | 493 | 6.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 76 | L0-main | claudeopus46 | 22,518 | 130,949 | 153,467 | 9,034 | 65.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 77 | L0-main | claudeopus46 | 22,518 | 145,069 | 167,587 | 2,187 | 18.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 78 | L0-main | claudeopus46 | 22,485 | 147,988 | 170,473 | 493 | 7.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 79 | L0-main | claudeopus46 | 22,518 | 147,226 | 169,744 | 5,317 | 42.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 80 | L0-main | claudeopus46 | 22,518 | 157,958 | 180,476 | 2,133 | 19.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 81 | L0-main | claudeopus46 | 22,485 | 160,821 | 183,306 | 474 | 7.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 82 | L0-main | claudeopus46 | 22,518 | 160,059 | 182,577 | 5,744 | 43.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 83 | L0-main | claudeopus46 | 2,106 | 10,264 | 12,370 | 266 | 3.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 84 | L0-main | claudeopus46 | 366 | 789 | 1,155 | 252 | 2.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 85 | L0-main | claudeopus46 | 2,320 | 9,516 | 11,836 | 1,091 | 10.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 86 | L0-main | claudeopus46 | 366 | 1,528 | 1,894 | 1,023 | 4.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 87 | L0-main | claudeopus46 | 560 | 10,315 | 10,875 | 178 | 2.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 88 | L0-main | claudeopus46 | 1,156 | 11,765 | 12,921 | 1,040 | 8.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 89 | L0-main | claudeopus46 | 1,918 | 6,972 | 8,890 | 1,139 | 10.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 1 | L0-main | claudeopus46 | 22,518 | 661 | 23,179 | 2,147 | 12.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 2 | L0-main | claudeopus46 | 22,518 | 1,203 | 23,721 | 1,555 | 8.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 3 | L0-main | claudeopus46 | 22,518 | 1,726 | 24,244 | 1,402 | 9.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 4 | L1-worker | claudeopus46 | 24,095 | 948 | 25,043 | 668 | 5.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 5 | L1-worker | claudeopus46 | 24,095 | 962 | 25,057 | 777 | 5.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,990 | 26,085 | 578 | 4.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,028 | 26,123 | 583 | 4.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 8 | L1-worker | claudeopus46 | 3,767 | 593 | 4,360 | 917 | 8.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 9 | L1-worker | claudeopus46 | 3,767 | 685 | 4,452 | 964 | 8.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,966 | 26,061 | 500 | 4.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 11 | L1-worker | claudeopus46 | 24,095 | 1,940 | 26,035 | 545 | 4.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 12 | L1-worker | claudeopus46 | 3,767 | 388 | 4,155 | 319 | 3.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 13 | L1-worker | claudeopus46 | 3,767 | 371 | 4,138 | 516 | 4.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,464 | 26,559 | 632 | 4.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 15 | L1-worker | claudeopus46 | 24,095 | 2,416 | 26,511 | 861 | 7.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 16 | L1-worker | claudeopus46 | 3,767 | 403 | 4,170 | 304 | 3.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 17 | L1-worker | claudeopus46 | 24,095 | 3,147 | 27,242 | 649 | 4.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 18 | L1-worker | claudeopus46 | 24,095 | 2,926 | 27,021 | 876 | 7.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 19 | L1-worker | claudeopus46 | 24,095 | 3,682 | 27,777 | 703 | 5.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 20 | L1-worker | claudeopus46 | 3,767 | 607 | 4,374 | 1,107 | 8.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 21 | L1-worker | claudeopus46 | 3,767 | 11,833 | 15,600 | 1,557 | 15.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 22 | L1-worker | claudeopus46 | 24,095 | 4,576 | 28,671 | 884 | 6.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 23 | L1-worker | claudeopus46 | 24,095 | 4,314 | 28,409 | 3,435 | 23.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 24 | L1-worker | claudeopus46 | 3,767 | 476 | 4,243 | 1,522 | 10.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 25 | L1-worker | claudeopus46 | 24,095 | 5,992 | 30,087 | 847 | 6.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 26 | L1-worker | claudeopus46 | 24,095 | 10,837 | 34,932 | 1,184 | 10.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 27 | L1-worker | claudeopus46 | 24,095 | 11,512 | 35,607 | 588 | 5.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 28 | L1-worker | claudeopus46 | 24,095 | 12,207 | 36,302 | 612 | 6.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 29 | L1-worker | claudeopus46 | 3,767 | 32,122 | 35,889 | 1,669 | 13.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 30 | L1-worker | claudeopus46 | 24,095 | 14,125 | 38,220 | 845 | 9.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 31 | L1-worker | claudeopus46 | 24,095 | 7,127 | 31,222 | 902 | 6.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 32 | L1-worker | claudeopus46 | 3,767 | 504 | 4,271 | 495 | 4.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 33 | L1-worker | claudeopus46 | 24,095 | 15,336 | 39,431 | 1,056 | 9.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 34 | L1-worker | claudeopus46 | 24,095 | 7,831 | 31,926 | 2,538 | 15.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 35 | L1-worker | claudeopus46 | 2,106 | 2,575 | 4,681 | 308 | 2.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 36 | L1-worker | claudeopus46 | 2,320 | 1,492 | 3,812 | 546 | 3.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 37 | L1-worker | claudeopus46 | 627 | 1,372 | 1,999 | 762 | 5.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 38 | L1-worker | claudeopus46 | 366 | 1,085 | 1,451 | 202 | 2.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 39 | L1-worker | claudeopus46 | 366 | 1,173 | 1,539 | 749 | 4.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 40 | L1-worker | claudeopus46 | 366 | 983 | 1,349 | 511 | 7.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 41 | L1-worker | claudeopus46 | 24,095 | 16,641 | 40,736 | 2,854 | 24.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 42 | L1-worker | claudeopus46 | 787 | 4,548 | 5,335 | 481 | 4.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 43 | L1-worker | claudeopus46 | 2,320 | 2,985 | 5,305 | 1,073 | 7.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 44 | L1-worker | claudeopus46 | 627 | 2,865 | 3,492 | 1,059 | 7.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 45 | L1-worker | claudeopus46 | 2,106 | 4,054 | 6,160 | 1,649 | 8.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 46 | L1-worker | claudeopus46 | 366 | 1,510 | 1,876 | 1,033 | 4.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 47 | L1-worker | claudeopus46 | 366 | 2,426 | 2,792 | 1,269 | 6.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 48 | L1-worker | claudeopus46 | 787 | 26,201 | 26,988 | 703 | 8.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 49 | L0-main | claudeopus46 | 22,518 | 37,848 | 60,366 | 2,640 | 26.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 50 | L1-worker | claudeopus46 | 24,095 | 2,202 | 26,297 | 907 | 6.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 51 | L1-worker | claudeopus46 | 24,095 | 2,917 | 27,012 | 560 | 4.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 52 | L1-worker | claudeopus46 | 3,767 | 11,793 | 15,560 | 1,778 | 14.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 53 | L1-worker | claudeopus46 | 24,095 | 3,287 | 27,382 | 980 | 7.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 54 | L1-worker | claudeopus46 | 24,095 | 4,867 | 28,962 | 1,384 | 11.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 55 | L1-worker | claudeopus46 | 24,095 | 5,509 | 29,604 | 549 | 4.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 56 | L1-worker | claudeopus46 | 24,095 | 6,157 | 30,252 | 691 | 6.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 57 | L1-worker | claudeopus46 | 24,095 | 6,870 | 30,965 | 960 | 7.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 58 | L1-worker | claudeopus46 | 24,095 | 8,203 | 32,298 | 1,639 | 12.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 59 | L1-worker | claudeopus46 | 24,095 | 9,644 | 33,739 | 863 | 8.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 60 | L1-worker | claudeopus46 | 24,095 | 11,108 | 35,203 | 2,001 | 16.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 61 | L1-worker | claudeopus46 | 24,095 | 15,593 | 39,688 | 1,312 | 10.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 62 | L1-worker | claudeopus46 | 24,095 | 17,548 | 41,643 | 2,409 | 20.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 63 | L1-worker | claudeopus46 | 2,320 | 2,540 | 4,860 | 1,125 | 6.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 64 | L1-worker | claudeopus46 | 627 | 2,420 | 3,047 | 1,062 | 6.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 65 | L1-worker | claudeopus46 | 2,106 | 4,863 | 6,969 | 1,642 | 9.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 66 | L1-worker | claudeopus46 | 366 | 1,562 | 1,928 | 1,080 | 4.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 67 | L1-worker | claudeopus46 | 366 | 2,419 | 2,785 | 951 | 4.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 68 | L1-worker | claudeopus46 | 787 | 24,208 | 24,995 | 524 | 5.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 69 | L0-main | claudeopus46 | 22,518 | 57,876 | 80,394 | 908 | 10.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 70 | L0-main | claudeopus46 | 22,518 | 58,583 | 81,101 | 602 | 5.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 71 | L0-main | claudeopus46 | 22,518 | 59,293 | 81,811 | 586 | 5.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 72 | L0-main | claudeopus46 | 22,518 | 60,824 | 83,342 | 1,215 | 14.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 73 | L0-main | claudeopus46 | 22,518 | 61,583 | 84,101 | 752 | 5.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 74 | L0-main | claudeopus46 | 22,518 | 62,257 | 84,775 | 816 | 7.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 75 | L0-main | claudeopus46 | 22,518 | 63,070 | 85,588 | 711 | 5.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 76 | L0-main | claudeopus46 | 22,518 | 64,625 | 87,143 | 1,245 | 9.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 77 | L0-main | claudeopus46 | 22,518 | 65,219 | 87,737 | 2,449 | 18.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 78 | L0-main | claudeopus46 | 22,518 | 67,089 | 89,607 | 8,697 | 62.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 79 | L0-main | claudeopus46 | 22,518 | 81,192 | 103,710 | 4,484 | 40.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 80 | L0-main | claudeopus46 | 22,518 | 89,584 | 112,102 | 3,447 | 30.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 81 | L0-main | claudeopus46 | 2,106 | 4,336 | 6,442 | 147 | 2.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 82 | L0-main | claudeopus46 | 366 | 670 | 1,036 | 188 | 2.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 83 | L0-main | claudeopus46 | 2,320 | 3,576 | 5,896 | 1,360 | 9.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 84 | L0-main | claudeopus46 | 366 | 1,797 | 2,163 | 1,310 | 5.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 85 | L0-main | claudeopus46 | 560 | 4,090 | 4,650 | 93 | 2.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 86 | L0-main | claudeopus46 | 1,156 | 4,847 | 6,003 | 446 | 4.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| 87 | L0-main | claudeopus46 | 1,918 | 5,615 | 7,533 | 1,079 | 10.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_5) |
| **TOTAL** |  |  | **3,716,301** | **7,397,764** | **11,114,065** | **304,989** | **2,385.4** |  |


## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| 1 | chars=98928>80000 | skipped_by_agent | 98,928 | 98,928 | 0 | 0.0% | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 2 | chars=101375>80000 | skipped_by_agent | 101,375 | 101,375 | 0 | 0.0% | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 3 | chars=102316>80000 | skipped_by_agent | 102,316 | 102,316 | 0 | 0.0% | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 4 | chars=104215>80000 | skipped_by_agent | 104,215 | 104,215 | 0 | 0.0% | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 5 | chars=105555>80000 | skipped_by_agent | 105,555 | 105,555 | 0 | 0.0% | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 6 | chars=106856>80000 | skipped_by_agent | 106,856 | 106,856 | 0 | 0.0% | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 7 | chars=107460>80000 | skipped_by_agent | 107,460 | 107,460 | 0 | 0.0% | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 8 | chars=108829>80000 | skipped_by_agent | 108,829 | 108,829 | 0 | 0.0% | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 9 | chars=109350>80000 | skipped_by_agent | 109,350 | 109,350 | 0 | 0.0% | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10 | chars=112704>80000 | skipped_by_agent | 112,704 | 112,704 | 0 | 0.0% | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 11 | chars=128578>80000 | skipped_by_agent | 128,578 | 128,578 | 0 | 0.0% | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 12 | chars=141008>80000 | skipped_by_agent | 141,008 | 141,008 | 0 | 0.0% | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| **TOTAL** |  |  | **1,327,174** | **1,327,174** | **0** | **0** |  |
