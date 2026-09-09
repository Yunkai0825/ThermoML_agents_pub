# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 19 | 279,008 | 488,284 | 35,471 | 767,292 | 40,383 | 272.0 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| L1-worker | 46 | 608,700 | 267,119 | 51,103 | 875,819 | 19,039 | 394.3 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| L0-main | 23 | 369,080 | 1,203,590 | 40,282 | 1,572,670 | 68,376 | 321.4 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| L1-worker | 40 | 565,770 | 294,250 | 48,611 | 860,020 | 21,500 | 365.4 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| L0-main | 23 | 369,080 | 440,757 | 32,349 | 809,837 | 35,210 | 254.7 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| L1-worker | 43 | 556,809 | 209,504 | 44,801 | 766,313 | 17,821 | 334.5 | claudeopus46 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| **TOTAL** | **194** | **2,748,447** | **2,903,504** | **252,617** | **5,651,951** | **202,329** | **1,942.3** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `search_blocks` | 2 | 1 | 5 | 4 | 22 | 22 | 2,417 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `search_blocks` | 2 | 6 | 3 | 3 | 12 | 20 | 1,455 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `search_blocks` | 9 | 1 | 1 | 2 | 3 | 10 | 154 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `search_blocks` | 10 | 1 | 4 | 2 | 6 | 10 | 599 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `search_blocks` | 11 | 1 | 3 | 2 | 4 | 10 | 613 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `block_search_adv` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `query_thermoml_parallel` | 2 | 1 | 3 | 0 | 2 | 2 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `search_blocks` | 2 | 1 | 6 | 2 | 9 | 9 | 1,349 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 206 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `query_thermoml_parallel` | 2 | 2 | 6 | 2 | 10 | 10 | 438 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `search_blocks` | 2 | 1 | 5 | 3 | 16 | 17 | 1,379 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `search_blocks` | 7 | 1 | 2 | 2 | 6 | 6 | 250 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `search_blocks` | 2 | 14 | 6 | 6 | 27 | 50 | 1,775 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `query_thermoml_parallel` | 2 | 1 | 1 | 2 | 1 | 1 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| **TOTAL** | **67** | **35** | **48** | **30** | **119** | **168** | **10,635** |  |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | --- | --- |
| Unique Compounds | 28 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Properties | 7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique References | 45 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Measurements | 26 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Phases | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Variables | 6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Solvents | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Constraints | 5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique Block_Types | 1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Unique parent blocks | 70 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Explicit block/subsystem targets | 70 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Subsystem targets | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| Target-matched data points | 6,048 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| GLOBcomp_1 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_4 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBprop_28 |  | query_thermoml_parallel, resolve_property_ids, search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBlit_2432 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2825 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_7085 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8254 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8424 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8869 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8888 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_9571 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_10866 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_2395 |  | query_thermoml_parallel, search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_280 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_207 | Excess molar volume, m3/mol | query_thermoml_parallel, search_blocks |
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks |
| GLOBsolvent_1 |  | query_thermoml_parallel, search_blocks |
| GLOBsolvent_3 |  | query_thermoml_parallel, search_blocks |
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBvar_3 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBvar_4 | Molality, mol/kg | query_thermoml_parallel, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_18 | Volume fraction | query_thermoml_parallel, search_blocks |
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBconstr_2 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBblocktype_1 |  | query_thermoml_parallel |
| Unique Compounds | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| Unique Properties | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| Unique References | 10 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| Unique Measurements | 7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| Unique Phases | 1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| Unique Solvents | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| Unique Variables | 6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| Unique Constraints | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| Unique Block_Types | 1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| Unique parent blocks | 10 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| Explicit block/subsystem targets | 10 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| Subsystem targets | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| Target-matched data points | 3,110 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| GLOBcomp_1 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_5 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_482 | 1-butyl-3-methylimidazolium nitrate | search_blocks |
| GLOBcomp_299 | 3-methylbutyl ethanoate | search_blocks |
| GLOBcomp_2754 | 1-methylimidazolium acetate | search_blocks |
| GLOBcomp_268 | 2-pyrrolidinone | search_blocks |
| GLOBcomp_133 | formamide | search_blocks |
| GLOBcomp_56 | 1-hexyl-3-methylimidazolium bis[(trifluoromethyl)sulfonyl]imide | search_blocks |
| GLOBprop_28 |  | resolve_property_ids, search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
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
| GLOBlit_555 |  | search_blocks |
| GLOBlit_590 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_2979 |  | search_blocks |
| GLOBlit_4068 |  | search_blocks |
| GLOBlit_4415 |  | search_blocks |
| GLOBlit_5585 |  | search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_7178 |  | search_blocks |
| GLOBlit_8254 |  | search_blocks |
| GLOBlit_8447 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_11042 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_11142 |  | search_blocks |
| GLOBlit_11872 |  | search_blocks |
| GLOBlit_3116 |  | search_blocks |
| GLOBlit_3325 |  | search_blocks |
| GLOBlit_3540 |  | search_blocks |
| GLOBlit_5836 |  | search_blocks |
| GLOBlit_6063 |  | search_blocks |
| GLOBlit_8993 |  | search_blocks |
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
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_143 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_29 | Excess molar volume, m3/mol | search_blocks |
| GLOBmeas_55 | Excess molar volume, m3/mol | search_blocks |
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
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks |
| GLOBphase_3 |  | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_32 | Initial mass fraction of solute | search_blocks |
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |
| GLOBconstr_2 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_25 | Final mass fraction of solute | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_9 |  | search_blocks |
| GLOBblocktype_1 |  | query_thermoml_parallel |
| Unique Compounds | 8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique Properties | 15 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique References | 40 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique Measurements | 29 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique Phases | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique Variables | 6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique Constraints | 6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique Solvents | 2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique Block_Types | 1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Unique parent blocks | 63 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Explicit block/subsystem targets | 63 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Subsystem targets | 0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| Target-matched data points | 3,417 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| **TOTAL** | **13,125** |  |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 10.1007/s10765-010-0717-9 | PROPblock_6 | declared | 15 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1007/s10765-010-0717-9 | PROPblock_8 | declared | 17 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1007/s10765-010-0861-2 | PROPblock_11 | declared | 31 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1007/s10765-010-0861-2 | PROPblock_13 | declared | 31 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2005.06.011 | PROPblock_16 | declared | 10 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2005.06.011 | PROPblock_18 | declared | 9 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2005.06.011 | PROPblock_20 | declared | 10 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2005.06.011 | PROPblock_22 | declared | 10 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2005.06.011 | PROPblock_24 | declared | 10 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2005.06.011 | PROPblock_26 | declared | 11 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2005.08.001 | PROPblock_12 | declared | 17 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2005.08.001 | PROPblock_16 | declared | 111 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2005.08.001 | PROPblock_6 | declared | 23 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2005.08.018 | PROPblock_4 | declared | 2 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2005.08.018 | PROPblock_5 | declared | 7 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2005.08.018 | PROPblock_6 | declared | 4 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2006.04.017 | PROPblock_3 | declared | 28 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2007.06.007 | PROPblock_1 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2007.06.007 | PROPblock_2 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2009.10.002 | PROPblock_17 | declared | 5 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2009.10.002 | PROPblock_18 | declared | 5 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2009.11.014 | PROPblock_2 | declared | 18 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2009.11.014 | PROPblock_3 | declared | 18 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2010.01.020 | PROPblock_27 | declared | 78 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2010.05.001 | PROPblock_12 | declared | 52 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2010.05.001 | PROPblock_8 | declared | 60 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2010.10.005 | PROPblock_2 | declared | 34 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2011.01.007 | PROPblock_17 | declared | 64 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2011.01.007 | PROPblock_21 | declared | 63 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2011.06.009 | PROPblock_1 | declared | 45 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2011.06.009 | PROPblock_2 | declared | 45 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2011.06.011 | PROPblock_14 | declared | 44 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2011.06.011 | PROPblock_16 | declared | 220 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2011.07.005 | PROPblock_10 | declared | 12 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2011.09.016 | PROPblock_1 | declared | 6 | binary | — | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2011.09.016 | PROPblock_10 | declared | 56 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2011.09.016 | PROPblock_2 | declared | 25 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2011.09.016 | PROPblock_4 | declared | 65 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2011.09.016 | PROPblock_6 | declared | 139 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2011.09.016 | PROPblock_8 | declared | 98 | ternary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2012.11.026 | PROPblock_4 | declared | 24 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2012.11.026 | PROPblock_5 | declared | 24 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2012.12.014 | PROPblock_2 | declared | 76 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2012.12.014 | PROPblock_3 | declared | 76 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2013.07.001 | PROPblock_6 | declared | 42 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2013.07.034 | PROPblock_5 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2014.05.031 | PROPblock_4 | declared | 56 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.jct.2007.09.009 | PROPblock_9 | declared | 30 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je900064e | PROPblock_6 | declared | 10 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1021/je900743e | PROPblock_3 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10.1016/j.jct.2004.03.011 | 1 | 206 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |  |  |
| 10.1016/j.jct.2004.07.019 | 1 | 596 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |  |  |
| 10.1016/j.jct.2007.05.004 | 1 | 39 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |  |  |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |  |  |
| 10.1021/je034101z | 1 | 401 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |  |  |
| 10.1021/je049691v | 1 | 180 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |  |  |
| 10.1021/je0600810 | 1 | 9 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |  |  |
| 10.1021/je0601098 | 1 | 12 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |  |  |
| 10.1021/je2003622 | 1 | 16 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |  |  |
| 10.1021/je700300y | 1 | 84 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |  |  |
| 10.1016/j.jct.2004.03.011 | PROPblock_1 | declared | 206 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 10.1016/j.fluid.2005.08.018 | 3 | 14 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2007.07.066 | 2 | 30 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2008.01.004 | 2 | 30 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2009.12.009 | 2 | 16 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2011.05.016 | 1 | 12 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2011.08.009 | 1 | 28 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2015.07.012 | 2 | 168 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2017.05.012 | 4 | 34 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2017.09.005 | 2 | 144 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2004.07.019 | 1 | 456 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2009.06.023 | 1 | 88 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2010.12.009 | 1 | 60 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2011.12.018 | 1 | 22 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2012.01.013 | 1 | 45 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2012.12.019 | 2 | 74 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2013.11.036 | 2 | 203 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2015.06.024 | 2 | 80 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2016.10.001 | 2 | 36 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2017.06.014 | 2 | 42 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2017.07.003 | 1 | 36 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2017.10.005 | 2 | 10 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.jct.2019.105880 | 3 | 48 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.tca.2009.03.014 | 1 | 14 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.tca.2013.02.010 | 1 | 22 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.tca.2015.09.022 | 1 | 1 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.tca.2018.09.022 | 1 | 1 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/acs.jced.5b00200 | 1 | 1 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/acs.jced.7b00299 | 3 | 5 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/acs.jced.8b00181 | 2 | 10 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/acs.jced.9b00102 | 3 | 166 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je034101z | 1 | 380 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je049738c | 1 | 8 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je060307z | 1 | 21 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je4003515 | 1 | 25 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je700700f | 1 | 13 | binary | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je800158z | 1 | 56 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1021/je900966r | 1 | 30 | binary | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |  |  |
| 10.1016/j.fluid.2005.08.018 | PROPblock_7 | declared | 3 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2005.08.018 | PROPblock_8 | declared | 7 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2005.08.018 | PROPblock_9 | declared | 4 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2007.07.066 | PROPblock_7 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2007.07.066 | PROPblock_8 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2008.01.004 | PROPblock_4 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2008.01.004 | PROPblock_5 | declared | 15 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2009.12.009 | PROPblock_7 | declared | 8 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2009.12.009 | PROPblock_8 | declared | 8 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2011.05.016 | PROPblock_1 | declared | 12 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2011.08.009 | PROPblock_6 | declared | 28 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_5 | declared | 84 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2015.07.012 | PROPblock_6 | declared | 84 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2017.05.012 | PROPblock_4 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2017.05.012 | PROPblock_5 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2017.05.012 | PROPblock_6 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2017.05.012 | PROPblock_7 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_5 | declared | 72 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.fluid.2017.09.005 | PROPblock_6 | declared | 72 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2004.07.019 | PROPblock_3 | declared | 456 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2008.07.005 | PROPblock_9 | declared | 96 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2009.06.023 | PROPblock_14 | declared | 88 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2010.12.009 | PROPblock_20 | declared | 60 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2011.12.018 | PROPblock_1 | declared | 22 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2012.01.013 | PROPblock_23 | declared | 45 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2012.12.019 | PROPblock_2 | declared | 37 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2012.12.019 | PROPblock_3 | declared | 37 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2013.11.036 | PROPblock_1 | declared | 174 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2013.11.036 | PROPblock_2 | declared | 29 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2015.06.024 | PROPblock_5 | declared | 40 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2015.06.024 | PROPblock_6 | declared | 40 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2016.10.001 | PROPblock_7 | declared | 18 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2016.10.001 | PROPblock_8 | declared | 18 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2017.06.014 | PROPblock_3 | declared | 21 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2017.06.014 | PROPblock_4 | declared | 21 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2017.07.003 | PROPblock_6 | declared | 36 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2017.10.005 | PROPblock_13 | declared | 5 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2017.10.005 | PROPblock_14 | declared | 5 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2019.105880 | PROPblock_7 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2019.105880 | PROPblock_8 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.jct.2019.105880 | PROPblock_9 | declared | 16 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.tca.2009.03.014 | PROPblock_16 | declared | 14 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.tca.2013.02.010 | PROPblock_7 | declared | 22 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.tca.2015.09.022 | PROPblock_43 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1016/j.tca.2018.09.022 | PROPblock_5 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/acs.jced.5b00200 | PROPblock_19 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/acs.jced.6b01058 | PROPblock_8 | declared | 12 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/acs.jced.7b00299 | PROPblock_13 | declared | 2 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/acs.jced.7b00299 | PROPblock_14 | declared | 2 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/acs.jced.7b00299 | PROPblock_15 | declared | 1 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/acs.jced.8b00181 | PROPblock_8 | declared | 5 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/acs.jced.8b00181 | PROPblock_9 | declared | 5 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/acs.jced.9b00102 | PROPblock_11 | declared | 60 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/acs.jced.9b00102 | PROPblock_12 | declared | 60 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/acs.jced.9b00102 | PROPblock_13 | declared | 46 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je034101z | PROPblock_6 | declared | 380 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je049738c | PROPblock_26 | declared | 8 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je0601098 | PROPblock_22 | declared | 12 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je060307z | PROPblock_7 | declared | 21 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je4003515 | PROPblock_10 | declared | 25 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je700700f | PROPblock_14 | declared | 13 | binary | 2 | query_thermoml_parallel, search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je800158z | PROPblock_3 | declared | 56 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10.1021/je900966r | PROPblock_4 | declared | 30 | binary | — | search_blocks | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| **TOTAL** | **73** | **4,104** | **8,392** |  | **24** |  |  |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | ---: | ---: | --- |
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume_dir… | 132 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 2 | 1 | `resolve_compound_ids` | purpose=Find compound IDs for water a…, queries=['… | 172 | KEEP ←in 278 | 172 | 4.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve water and e… | 192 | KEEP ←in 278 | 192 | 4.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 4 | 2 | `resolve_property_ids` | purpose=Find the global property ID f…, queries=['… | 200 | KEEP ←in 227 | 200 | 3.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 5 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,161 | DISCARD ←in 39 | 1103 | 13.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 6 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 552 | KEEP ←in 14,080 | 552 | 24.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 7 | 5 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_220, … | 4,222 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 8 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=50, p… | 1,067 | DISCARD ←in 39 | 1009 | 16.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 9 | 6 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_220, … | 1,875 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10 | 6 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_2'], limit=20, p… | 1,370 | KEEP ←in 12,401 | 1255 | 14.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 11 | 7 | `search_blocks` | limit=10, property=GLOBprop_28, purpose=Check if e… | 1,217 | KEEP ←in 6,974 | 1121 | 12.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 12 | 8 | `search_blocks` | compound=GLOBcomp_2, limit=10, property=GLOBprop_2… | 1,329 | KEEP ←in 7,022 | 1231 | 21.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 13 | 9 | `search_blocks` | compound=GLOBcomp_1, limit=10, property=GLOBprop_2… | 1,327 | KEEP ←in 7,327 | 1241 | 13.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 14 | 10 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_1014,… | 1,074 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 15 | 11 | `block_search_adv` | compounds=['REQUIRE GLOBcomp_1 AS water…, explanat… | 932 | DISCARD ←in 775 | 871 | 19.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 16 | 2 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume', '… | 43,090 | — | — | 257.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 17 | 5 | `fit_block_derived` | block_number=PROPblock_2, composition_hint=mole_fr… | 239 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 18 | 7 | `fit_block_derived` | block_number=PROPblock_2, composition_hint=mole_fr… | 963 | — | — | 2.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 19 | 8 | `predict_from_rk` | coeffs=[-4.98777e-06, 2.71547e-06, -…, mixing_rule… | 206 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 20 | 9 | `list_session_files` |  | 1,689 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume_dir… | 132 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 2 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 175 | KEEP ←in 277 | 175 | 4.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve water and m… | 193 | KEEP ←in 277 | 193 | 3.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 4 | 3 | `resolve_property_ids` | limit=5, min_score=50, purpose=Find the global pro… | 200 | KEEP ←in 227 | 200 | 3.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 5 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 979 | KEEP ←in 3,972 | 964 | 15.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 6 | 6 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2395,… | 375 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 7 | 7 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2395,… | 2,077 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 8 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 1,960 | KEEP ←in 5,885 | 1960 | 41.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 9 | 6 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 247 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 10 | 7 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 364 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 11 | 8 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 958 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 12 | 9 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_8424,… | 836 | — | — | 0.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 13 | 10 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_10866… | 966 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 14 | 11 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_2432,… | 878 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 15 | 12 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_7085,… | 859 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 16 | 2 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume', '… | 96,814 | — | — | 242.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 17 | 5 | `inspect_block` | block_number=PROPblock_10, doi=10.1016/j.jct.2007.… | 1,360 | — | — | 0.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 18 | 9 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 237 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 19 | 11 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 954 | — | — | 1.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 20 | 12 | `predict_from_rk` | coeffs=[-3.98239e-06, -1.5386e-07, 1…, n_points=20… | 207 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 21 | 13 | `list_session_files` |  | 1,681 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'direct_VE', 'purp… | 132 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 2 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 203 | KEEP ←in 283 | 203 | 4.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 210 | KEEP ←in 283 | 210 | 4.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 4 | 3 | `resolve_property_ids` | limit=10, min_score=50, purpose=Find the global pr… | 132 | KEEP ←in 227 | 132 | 7.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 5 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 976 | DISCARD ←in 39 | 918 | 11.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 6 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 616 | KEEP ←in 11,346 | 600 | 23.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 7 | 5 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 352 | — | — | 0.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 8 | 6 | `inspect_block_table` | block_number=PROPblock_14, literature=GLOBlit_1104… | 1,195 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 9 | 6 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 1,024 | DISCARD ←in 39 | 966 | 18.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10 | 7 | `search_blocks` | compound=['GLOBcomp_5'], limit=20, property=GLOBpr… | 1,294 | KEEP ←in 8,762 | 1279 | 20.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 11 | 8 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 703 | KEEP ←in 31,749 | 627 | 21.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 12 | 9 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=20, p… | 697 | DISCARD ←in 39 | 639 | 15.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 13 | 2 | `query_thermoml_parallel` | queries=[{'label': 'direct_VE', 'purp… | 17,501 | — | — | 221.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 14 | 6 | `inspect_block` | block_number=PROPblock_14, doi=10.1021/je700700f, … | 1,367 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 15 | 10 | `fit_block_derived` | block_number=PROPblock_14, composition_hint=mole_f… | 957 | — | — | 1.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 16 | 12 | `predict_from_rk` | coeffs=[-2.58261e-06, 6.379e-07, -7.…, mixing_rule… | 210 | — | — | 0.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 17 | 13 | `list_session_files` |  | 1,561 | — | — | 0.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| **TOTAL** | **358** |  |  | **204,591** |  | **18,013** | **1,070.9** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 22,518 | 707 | 23,225 | 1,678 | 10.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 2 | L0-main | claudeopus46 | 22,518 | 1,165 | 23,683 | 1,373 | 8.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 3 | L1-worker | claudeopus46 | 24,095 | 909 | 25,004 | 562 | 4.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 4 | L1-worker | claudeopus46 | 24,095 | 966 | 25,061 | 577 | 4.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,981 | 26,076 | 544 | 3.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 6 | L1-worker | claudeopus46 | 3,767 | 430 | 4,197 | 329 | 4.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 7 | L1-worker | claudeopus46 | 3,767 | 437 | 4,204 | 374 | 4.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 8 | L1-worker | claudeopus46 | 24,095 | 1,326 | 25,421 | 502 | 5.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 9 | L1-worker | claudeopus46 | 3,767 | 406 | 4,173 | 304 | 3.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,602 | 25,697 | 757 | 6.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 11 | L1-worker | claudeopus46 | 24,095 | 1,759 | 25,854 | 780 | 6.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 12 | L1-worker | claudeopus46 | 24,095 | 2,290 | 26,385 | 713 | 5.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 13 | L1-worker | claudeopus46 | 24,095 | 2,488 | 26,583 | 658 | 4.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 14 | L1-worker | claudeopus46 | 3,767 | 553 | 4,320 | 1,461 | 11.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 15 | L1-worker | claudeopus46 | 24,095 | 3,634 | 27,729 | 766 | 5.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 16 | L1-worker | claudeopus46 | 3,767 | 14,537 | 18,304 | 1,842 | 17.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 17 | L1-worker | claudeopus46 | 24,095 | 2,817 | 26,912 | 1,056 | 7.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 18 | L1-worker | claudeopus46 | 3,767 | 475 | 4,242 | 1,403 | 9.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 19 | L1-worker | claudeopus46 | 24,095 | 7,391 | 31,486 | 1,597 | 12.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 20 | L1-worker | claudeopus46 | 24,095 | 5,026 | 29,121 | 1,221 | 8.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 21 | L1-worker | claudeopus46 | 3,767 | 12,761 | 16,528 | 1,638 | 13.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 22 | L1-worker | claudeopus46 | 24,095 | 9,688 | 33,783 | 3,134 | 23.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 23 | L1-worker | claudeopus46 | 24,095 | 6,864 | 30,959 | 1,017 | 7.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 24 | L1-worker | claudeopus46 | 3,767 | 7,302 | 11,069 | 1,394 | 11.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 25 | L1-worker | claudeopus46 | 24,095 | 16,065 | 40,160 | 2,493 | 20.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 26 | L1-worker | claudeopus46 | 24,095 | 8,462 | 32,557 | 1,163 | 8.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 27 | L1-worker | claudeopus46 | 24,095 | 21,339 | 45,434 | 2,489 | 17.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 28 | L1-worker | claudeopus46 | 2,106 | 3,707 | 5,813 | 560 | 5.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 29 | L1-worker | claudeopus46 | 2,320 | 2,620 | 4,940 | 894 | 5.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 30 | L1-worker | claudeopus46 | 3,767 | 7,356 | 11,123 | 1,517 | 13.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 31 | L1-worker | claudeopus46 | 627 | 2,500 | 3,127 | 941 | 7.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 32 | L1-worker | claudeopus46 | 366 | 1,337 | 1,703 | 433 | 3.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 33 | L1-worker | claudeopus46 | 366 | 1,331 | 1,697 | 854 | 3.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 34 | L1-worker | claudeopus46 | 366 | 1,352 | 1,718 | 928 | 4.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 35 | L1-worker | claudeopus46 | 24,095 | 10,137 | 34,232 | 956 | 7.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 36 | L1-worker | claudeopus46 | 787 | 12,945 | 13,732 | 559 | 12.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 37 | L1-worker | claudeopus46 | 3,767 | 7,645 | 11,412 | 1,521 | 10.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 38 | L1-worker | claudeopus46 | 24,095 | 11,861 | 35,956 | 1,504 | 12.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 39 | L1-worker | claudeopus46 | 24,095 | 13,379 | 37,474 | 2,353 | 18.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 40 | L1-worker | claudeopus46 | 3,767 | 1,014 | 4,781 | 1,537 | 10.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 41 | L1-worker | claudeopus46 | 24,095 | 14,723 | 38,818 | 1,918 | 13.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 42 | L1-worker | claudeopus46 | 24,062 | 15,199 | 39,261 | 2,097 | 15.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 43 | L1-worker | claudeopus46 | 24,062 | 16,334 | 40,396 | 1,708 | 10.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 44 | L1-worker | claudeopus46 | 2,106 | 2,869 | 4,975 | 92 | 1.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 45 | L1-worker | claudeopus46 | 2,320 | 1,839 | 4,159 | 504 | 2.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 46 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 47 | L1-worker | claudeopus46 | 627 | 1,719 | 2,346 | 813 | 4.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 48 | L1-worker | claudeopus46 | 787 | 4,875 | 5,662 | 573 | 4.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 49 | L0-main | claudeopus46 | 22,518 | 38,630 | 61,148 | 1,598 | 15.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 50 | L0-main | claudeopus46 | 22,518 | 39,472 | 61,990 | 871 | 6.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 51 | L0-main | claudeopus46 | 22,518 | 40,237 | 62,755 | 794 | 6.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 52 | L0-main | claudeopus46 | 22,518 | 40,222 | 62,740 | 1,035 | 7.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 53 | L0-main | claudeopus46 | 22,518 | 41,029 | 63,547 | 984 | 6.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 54 | L0-main | claudeopus46 | 22,518 | 43,452 | 65,970 | 1,276 | 10.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 55 | L0-main | claudeopus46 | 22,518 | 44,036 | 66,554 | 4,427 | 28.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 56 | L0-main | claudeopus46 | 22,518 | 46,039 | 68,557 | 6,863 | 52.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 57 | L0-main | claudeopus46 | 22,518 | 57,660 | 80,178 | 5,516 | 44.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 58 | L0-main | claudeopus46 | 22,518 | 68,910 | 91,428 | 4,689 | 37.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 59 | L0-main | claudeopus46 | 2,106 | 4,856 | 6,962 | 154 | 2.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 60 | L0-main | claudeopus46 | 366 | 677 | 1,043 | 195 | 2.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 61 | L0-main | claudeopus46 | 2,320 | 4,050 | 6,370 | 1,136 | 8.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 62 | L0-main | claudeopus46 | 366 | 1,573 | 1,939 | 1,091 | 4.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 63 | L0-main | claudeopus46 | 560 | 4,571 | 5,131 | 100 | 2.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 64 | L0-main | claudeopus46 | 1,156 | 5,369 | 6,525 | 591 | 5.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 65 | L0-main | claudeopus46 | 1,918 | 5,629 | 7,547 | 1,100 | 10.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_3) |
| 1 | L0-main | claudeopus46 | 22,518 | 710 | 23,228 | 1,660 | 10.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 2 | L0-main | claudeopus46 | 22,518 | 1,171 | 23,689 | 1,124 | 7.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 3 | L1-worker | claudeopus46 | 24,095 | 822 | 24,917 | 585 | 4.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 4 | L1-worker | claudeopus46 | 24,095 | 839 | 24,934 | 738 | 5.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,834 | 25,929 | 513 | 4.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,857 | 25,952 | 518 | 3.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 7 | L1-worker | claudeopus46 | 3,767 | 432 | 4,199 | 307 | 4.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 8 | L1-worker | claudeopus46 | 3,767 | 438 | 4,205 | 330 | 3.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 9 | L1-worker | claudeopus46 | 24,095 | 1,445 | 25,540 | 623 | 5.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,417 | 25,512 | 893 | 7.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 11 | L1-worker | claudeopus46 | 3,767 | 406 | 4,173 | 304 | 3.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 12 | L1-worker | claudeopus46 | 24,095 | 2,156 | 26,251 | 727 | 5.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 13 | L1-worker | claudeopus46 | 24,095 | 1,930 | 26,025 | 804 | 6.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,660 | 26,755 | 667 | 5.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 15 | L1-worker | claudeopus46 | 3,767 | 6,414 | 10,181 | 1,531 | 14.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 16 | L1-worker | claudeopus46 | 3,767 | 4,456 | 8,223 | 1,408 | 14.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 17 | L1-worker | claudeopus46 | 24,095 | 3,628 | 27,723 | 697 | 6.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 18 | L1-worker | claudeopus46 | 24,095 | 4,368 | 28,463 | 673 | 5.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 19 | L1-worker | claudeopus46 | 3,767 | 6,837 | 10,604 | 2,157 | 18.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 20 | L1-worker | claudeopus46 | 24,095 | 6,740 | 30,835 | 2,222 | 18.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 21 | L1-worker | claudeopus46 | 2,106 | 3,313 | 5,419 | 790 | 4.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 22 | L1-worker | claudeopus46 | 24,095 | 4,066 | 28,161 | 2,984 | 19.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 23 | L1-worker | claudeopus46 | 2,320 | 2,353 | 4,673 | 1,018 | 6.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 24 | L1-worker | claudeopus46 | 627 | 2,233 | 2,860 | 736 | 6.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 25 | L1-worker | claudeopus46 | 366 | 1,567 | 1,933 | 556 | 3.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 26 | L1-worker | claudeopus46 | 366 | 1,455 | 1,821 | 973 | 5.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 27 | L1-worker | claudeopus46 | 24,095 | 11,143 | 35,238 | 964 | 10.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 28 | L1-worker | claudeopus46 | 787 | 12,863 | 13,650 | 511 | 6.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 29 | L1-worker | claudeopus46 | 24,095 | 11,767 | 35,862 | 635 | 5.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 30 | L1-worker | claudeopus46 | 24,095 | 12,437 | 36,532 | 639 | 5.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 31 | L1-worker | claudeopus46 | 24,095 | 13,717 | 37,812 | 1,348 | 9.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 32 | L1-worker | claudeopus46 | 24,095 | 14,932 | 39,027 | 3,371 | 22.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 33 | L1-worker | claudeopus46 | 24,095 | 16,273 | 40,368 | 1,082 | 9.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 34 | L1-worker | claudeopus46 | 24,095 | 17,536 | 41,631 | 555 | 5.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 35 | L1-worker | claudeopus46 | 24,062 | 18,534 | 42,596 | 3,638 | 28.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 36 | L1-worker | claudeopus46 | 24,062 | 22,182 | 46,244 | 3,174 | 23.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 37 | L1-worker | claudeopus46 | 2,320 | 3,816 | 6,136 | 1,088 | 8.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 38 | L1-worker | claudeopus46 | 366 | 1,525 | 1,891 | 1,043 | 4.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 39 | L1-worker | claudeopus46 | 627 | 3,696 | 4,323 | 1,670 | 13.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 40 | L1-worker | claudeopus46 | 2,106 | 4,759 | 6,865 | 2,942 | 13.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 41 | L1-worker | claudeopus46 | 366 | 3,719 | 4,085 | 2,383 | 10.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 42 | L1-worker | claudeopus46 | 787 | 61,685 | 62,472 | 814 | 8.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 43 | L0-main | claudeopus46 | 22,518 | 75,292 | 97,810 | 1,922 | 17.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 44 | L0-main | claudeopus46 | 22,518 | 76,095 | 98,613 | 808 | 7.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 45 | L0-main | claudeopus46 | 22,518 | 76,892 | 99,410 | 531 | 4.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 46 | L0-main | claudeopus46 | 22,518 | 78,384 | 100,902 | 1,560 | 12.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 47 | L0-main | claudeopus46 | 22,518 | 79,146 | 101,664 | 837 | 6.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 48 | L0-main | claudeopus46 | 22,518 | 79,828 | 102,346 | 827 | 8.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 49 | L0-main | claudeopus46 | 22,518 | 80,546 | 103,064 | 768 | 5.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 50 | L0-main | claudeopus46 | 22,518 | 80,254 | 102,772 | 1,048 | 8.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 51 | L0-main | claudeopus46 | 22,518 | 81,018 | 103,536 | 825 | 6.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 52 | L0-main | claudeopus46 | 22,518 | 83,465 | 105,983 | 1,284 | 10.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 53 | L0-main | claudeopus46 | 22,518 | 84,077 | 106,595 | 3,769 | 28.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 54 | L0-main | claudeopus46 | 22,518 | 86,081 | 108,599 | 6,725 | 54.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 55 | L0-main | claudeopus46 | 22,518 | 98,247 | 120,765 | 5,577 | 45.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 56 | L0-main | claudeopus46 | 22,518 | 108,190 | 130,708 | 5,490 | 44.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 57 | L0-main | claudeopus46 | 2,106 | 6,236 | 8,342 | 274 | 3.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 58 | L0-main | claudeopus46 | 366 | 797 | 1,163 | 260 | 2.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 59 | L0-main | claudeopus46 | 2,320 | 5,427 | 7,747 | 1,430 | 11.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 60 | L0-main | claudeopus46 | 366 | 1,867 | 2,233 | 1,375 | 5.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 61 | L0-main | claudeopus46 | 560 | 6,234 | 6,794 | 186 | 2.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 62 | L0-main | claudeopus46 | 1,156 | 7,703 | 8,859 | 973 | 8.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 63 | L0-main | claudeopus46 | 1,918 | 5,930 | 7,848 | 1,029 | 10.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_2) |
| 1 | L0-main | claudeopus46 | 22,518 | 733 | 23,251 | 1,570 | 10.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 2 | L0-main | claudeopus46 | 22,518 | 1,198 | 23,716 | 1,336 | 8.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 3 | L1-worker | claudeopus46 | 24,095 | 919 | 25,014 | 597 | 4.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 4 | L1-worker | claudeopus46 | 24,095 | 988 | 25,083 | 617 | 4.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,006 | 26,101 | 535 | 4.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,937 | 26,032 | 549 | 4.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 7 | L1-worker | claudeopus46 | 3,767 | 442 | 4,209 | 370 | 3.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 8 | L1-worker | claudeopus46 | 3,767 | 442 | 4,209 | 377 | 4.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 9 | L1-worker | claudeopus46 | 24,095 | 1,621 | 25,716 | 563 | 4.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,573 | 25,668 | 854 | 7.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 11 | L1-worker | claudeopus46 | 3,767 | 408 | 4,175 | 297 | 3.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 12 | L1-worker | claudeopus46 | 3,767 | 710 | 4,477 | 294 | 3.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 13 | L1-worker | claudeopus46 | 24,095 | 2,278 | 26,373 | 764 | 5.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 14 | L1-worker | claudeopus46 | 24,095 | 2,037 | 26,132 | 923 | 6.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 15 | L1-worker | claudeopus46 | 24,095 | 2,787 | 26,882 | 706 | 5.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 16 | L1-worker | claudeopus46 | 3,767 | 598 | 4,365 | 1,307 | 10.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 17 | L1-worker | claudeopus46 | 3,767 | 11,867 | 15,634 | 1,942 | 16.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 18 | L1-worker | claudeopus46 | 24,095 | 3,751 | 27,846 | 875 | 7.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 19 | L1-worker | claudeopus46 | 24,095 | 2,889 | 26,984 | 1,568 | 11.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 20 | L1-worker | claudeopus46 | 24,095 | 3,642 | 27,737 | 755 | 6.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 21 | L1-worker | claudeopus46 | 3,767 | 505 | 4,272 | 1,370 | 9.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 22 | L1-worker | claudeopus46 | 24,095 | 5,149 | 29,244 | 836 | 6.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 23 | L1-worker | claudeopus46 | 24,095 | 5,194 | 29,289 | 1,582 | 16.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 24 | L1-worker | claudeopus46 | 3,767 | 9,148 | 12,915 | 1,555 | 13.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 25 | L1-worker | claudeopus46 | 24,095 | 9,504 | 33,599 | 2,994 | 19.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 26 | L1-worker | claudeopus46 | 24,095 | 6,856 | 30,951 | 802 | 6.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 27 | L1-worker | claudeopus46 | 24,095 | 14,948 | 39,043 | 2,247 | 14.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 28 | L1-worker | claudeopus46 | 2,320 | 1,680 | 4,000 | 638 | 4.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 29 | L1-worker | claudeopus46 | 2,106 | 2,720 | 4,826 | 963 | 5.8 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 30 | L1-worker | claudeopus46 | 627 | 1,560 | 2,187 | 816 | 5.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 31 | L1-worker | claudeopus46 | 366 | 1,075 | 1,441 | 603 | 3.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 32 | L1-worker | claudeopus46 | 366 | 1,740 | 2,106 | 596 | 3.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 33 | L1-worker | claudeopus46 | 3,767 | 32,097 | 35,864 | 1,660 | 14.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 34 | L1-worker | claudeopus46 | 787 | 10,854 | 11,641 | 662 | 7.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 35 | L1-worker | claudeopus46 | 24,095 | 7,945 | 32,040 | 1,560 | 11.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 36 | L1-worker | claudeopus46 | 3,767 | 484 | 4,251 | 899 | 7.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 37 | L1-worker | claudeopus46 | 24,095 | 9,105 | 33,200 | 2,269 | 15.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 38 | L1-worker | claudeopus46 | 24,095 | 14,457 | 38,552 | 2,917 | 19.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 39 | L1-worker | claudeopus46 | 24,095 | 19,319 | 43,414 | 2,650 | 13.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 40 | L1-worker | claudeopus46 | 2,106 | 2,950 | 5,056 | 308 | 2.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 41 | L1-worker | claudeopus46 | 2,320 | 1,841 | 4,161 | 532 | 3.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 42 | L1-worker | claudeopus46 | 627 | 1,721 | 2,348 | 871 | 5.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 43 | L1-worker | claudeopus46 | 366 | 1,085 | 1,451 | 202 | 2.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 44 | L1-worker | claudeopus46 | 366 | 1,282 | 1,648 | 858 | 3.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 45 | L1-worker | claudeopus46 | 787 | 5,390 | 6,177 | 518 | 5.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 46 | L0-main | claudeopus46 | 22,518 | 22,007 | 44,525 | 924 | 12.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 47 | L0-main | claudeopus46 | 22,518 | 23,040 | 45,558 | 529 | 4.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 48 | L0-main | claudeopus46 | 22,518 | 23,682 | 46,200 | 561 | 3.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 49 | L0-main | claudeopus46 | 22,518 | 24,421 | 46,939 | 597 | 4.0 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 50 | L0-main | claudeopus46 | 22,518 | 25,081 | 47,599 | 1,009 | 10.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 51 | L0-main | claudeopus46 | 22,518 | 25,829 | 48,347 | 792 | 5.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 52 | L0-main | claudeopus46 | 22,518 | 26,547 | 49,065 | 744 | 5.2 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 53 | L0-main | claudeopus46 | 22,518 | 27,274 | 49,792 | 676 | 4.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 54 | L0-main | claudeopus46 | 22,518 | 28,924 | 51,442 | 1,335 | 10.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 55 | L0-main | claudeopus46 | 22,518 | 29,727 | 52,245 | 814 | 5.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 56 | L0-main | claudeopus46 | 22,518 | 29,914 | 52,432 | 2,483 | 18.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 57 | L0-main | claudeopus46 | 22,518 | 31,785 | 54,303 | 6,168 | 45.7 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 58 | L0-main | claudeopus46 | 22,518 | 44,142 | 66,660 | 4,414 | 34.9 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 59 | L0-main | claudeopus46 | 22,518 | 52,166 | 74,684 | 4,009 | 31.3 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 60 | L0-main | claudeopus46 | 2,106 | 4,264 | 6,370 | 147 | 2.6 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 61 | L0-main | claudeopus46 | 366 | 670 | 1,036 | 188 | 2.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 62 | L0-main | claudeopus46 | 2,320 | 3,432 | 5,752 | 1,154 | 9.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 63 | L0-main | claudeopus46 | 366 | 1,591 | 1,957 | 1,109 | 5.4 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 64 | L0-main | claudeopus46 | 560 | 3,946 | 4,506 | 99 | 2.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 65 | L0-main | claudeopus46 | 1,156 | 4,703 | 5,859 | 551 | 5.5 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| 66 | L0-main | claudeopus46 | 1,918 | 5,681 | 7,599 | 1,140 | 11.1 | Find and fit excess molar volume (VE) data for the binary sy (analysis_runs/run_4) |
| **TOTAL** |  |  | **2,748,447** | **2,903,504** | **5,651,951** | **252,617** | **1,942.3** |  |
