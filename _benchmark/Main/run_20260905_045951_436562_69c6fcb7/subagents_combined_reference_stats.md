# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 13 | 65,705 | 176,051 | 24,600 | 241,756 | 18,596 | 155.8 | claudeopus46 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| L1-worker | 79 | 1,024,134 | 745,213 | 116,158 | 1,769,347 | 22,396 | 795.3 | claudeopus46 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| verdict | 1 | 972 | 12,183 | 1,135 | 13,155 | 13,155 | 11.0 | claudeopus46 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| **TOTAL** | **93** | **1,090,811** | **933,447** | **141,893** | **2,024,258** | **54,147** | **962.1** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `search_blocks` | 2 | 1 | 3 | 2 | 3 | 4 | 58 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `search_blocks` | 2 | 1 | 3 | 2 | 3 | 4 | 58 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `search_system_summary` | 2 | 0 | 0 | 0 | 26 | 39 | 3,263 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `search_blocks` | 2 | 13 | 5 | 5 | 31 | 50 | 3,013 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `resolve_property_ids` | 0 | 5 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 1 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `search_system_summary` | 2 | 1 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `search_system_summary` | 2 | 1 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `search_system_summary` | 2 | 0 | 0 | 0 | 26 | 39 | 3,263 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `search_blocks` | 2 | 13 | 5 | 5 | 31 | 50 | 3,013 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `search_system_registry` | 2 | 10 | 5 | 5 | 26 | 39 | 3,263 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| **TOTAL** | **22** | **49** | **24** | **19** | **147** | **226** | **15,932** |  |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBlit_528 |  | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_2574 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_6377 |  | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_220 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_2432 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_5201 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_11136 |  | search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_9006 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_11574 |  | search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_1483 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_10866 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_4415 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_2825 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_3475 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_7748 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_10024 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_8050 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_10159 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_10699 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_11792 |  | search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_384 |  | search_blocks, search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_11504 |  | search_system_registry, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_3697 |  | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_5473 |  | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_6628 |  | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_7085 |  | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_7178 |  | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_7448 |  | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_7483 |  | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_7676 |  | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_7794 |  | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_8381 |  | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_8445 |  | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_8888 |  | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_11005 |  | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBlit_11774 |  | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBprop_17 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_44 | Relative permittivity at zero frequency | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_8 | Speed of sound, m/s | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_18 | Electrical conductivity, S/m | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_34 | Thermal conductivity, W/m/K | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_3 | Activity coefficient | resolve_property_ids, search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_27 | Henry's Law constant (mole fraction scale), kPa | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_29 | Binary diffusion coefficient, m2/s | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_28 |  | resolve_property_ids, search_system_summary | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_97 |  | resolve_property_ids | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_38 |  | resolve_property_ids | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_84 |  | resolve_property_ids | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_103 |  | resolve_property_ids | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBprop_41 |  | resolve_property_ids | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBmeas_13 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_169 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_12 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_133 | Vapor or sublimation pressure, kPa | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_53 | Relative permittivity at zero frequency | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_18 | Speed of sound, m/s | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_36 | Surface tension liquid-gas, N/m | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_19 | Surface tension liquid-gas, N/m | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_14 | Electrical conductivity, S/m | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_193 | Thermal conductivity, W/m/K | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_163 | Refractive index (Na D-line) | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_236 | Mass density, kg/m3 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_1 | Activity coefficient | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_38 | Binary diffusion coefficient, m2/s | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_15 | Speed of sound, m/s | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_41 | Thermal conductivity, W/m/K | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_988 | Viscosity, Pa*s | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_203 | Mass density, kg/m3 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_165 | Viscosity, Pa*s | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_212 | Mass density, kg/m3 | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_206 | Speed of sound, m/s | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_141 | Mass density, kg/m3 | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_294 | Henry's Law constant (mole fraction scale), kPa | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBmeas_6 | Mass density, kg/m3 | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBphase_1 |  | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBvar_3 | Pressure, kPa | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBvar_4 | Molality, mol/kg | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBconstr_2 | Temperature, K | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBconstr_4 | Frequency, MHz | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBconstr_5 | Mass fraction | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBconstr_8 | Molality, mol/kg | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBconstr_22 | Volume fraction | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBconstr_3 | Mole fraction | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBsolvent_1 |  | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| GLOBsolvent_2 |  | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBblocktype_1 |  | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | ---: | --- |
| Unique Compounds | 2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| Unique References | 36 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| Unique Properties | 19 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| Unique Measurements | 34 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| Unique Phases | 1 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| Unique Variables | 5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| Unique Constraints | 7 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| Unique Solvents | 2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| Unique Block_Types | 1 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| Unique parent blocks | 58 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| Explicit block/subsystem targets | 58 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| Subsystem targets | 0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| Target-matched data points | 9,406 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| **TOTAL** | **9,629** |  |


## 3. DOI & Block References

| DOI | Blocks | Datapoints | System types | Source tools | Source |
| --- | ---: | ---: | --- | --- | --- |
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.fluid.2006.04.017 | 1 | 28 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.fluid.2007.06.007 | 2 | 30 | binary | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2004.07.019 | 1 | 565 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2005.06.018 | 1 | 27 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2007.05.004 | 2 | 74 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2012.08.009 | 1 | 14 | binary | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2015.06.024 | 2 | 80 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2018.02.022 | 3 | 496 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2019.02.027 | 1 | 9 | binary | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.tca.2017.05.023 | 1 | 1 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.5b00485 | 1 | 2 | binary | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.7b00299 | 3 | 5 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.8b00086 | 3 | 18 | binary | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.8b00181 | 2 | 12 | binary | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.8b00939 | 2 | 18 | binary | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.8b01147 | 1 | 68 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.9b00026 | 1 | 10 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je020173z | 2 | 48 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je0495942 | 2 | 2 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je0497303 | 1 | 6 | binary | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je0601098 | 2 | 24 | binary | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je060335h | 1 | 164 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je301171y | 1 | 63 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je4003515 | 3 | 53 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je600565m | 2 | 35 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je700618y | 3 | 45 | binary | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je800150h | 2 | 216 | binary | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je900064e | 2 | 18 | binary | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je900266h | 1 | 164 | binary | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je900711h | 1 | 5 | binary | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je900743e | 2 | 30 | binary | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | --- | --- | ---: | --- | ---: | --- | --- |
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.fluid.2006.04.017 | PROPblock_3 | declared | 28 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.fluid.2007.06.007 | PROPblock_1 | declared | 15 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.fluid.2007.06.007 | PROPblock_2 | declared | 15 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2005.06.018 | PROPblock_4 | declared | 27 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2007.05.004 | PROPblock_11 | declared | 37 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2007.05.004 | PROPblock_12 | declared | 37 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2012.08.009 | PROPblock_18 | declared | 14 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2015.06.024 | PROPblock_8 | declared | 40 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2018.02.022 | PROPblock_20 | declared | 152 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2018.02.022 | PROPblock_21 | declared | 100 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.jct.2019.02.027 | PROPblock_21 | declared | 9 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1016/j.tca.2017.05.023 | PROPblock_1 | declared | 1 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.5b00485 | PROPblock_8 | declared | 2 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.7b00299 | PROPblock_10 | declared | 2 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.7b00299 | PROPblock_11 | declared | 2 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.7b00299 | PROPblock_12 | declared | 1 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.8b00086 | PROPblock_46 | declared | 6 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | declared | 6 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.8b00086 | PROPblock_48 | declared | 6 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.8b00181 | PROPblock_10 | declared | 6 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.8b00181 | PROPblock_11 | declared | 6 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.8b00939 | PROPblock_17 | declared | 9 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.8b00939 | PROPblock_18 | declared | 9 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.8b01147 | PROPblock_6 | declared | 68 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/acs.jced.9b00026 | PROPblock_16 | declared | 10 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je020173z | PROPblock_4 | declared | 24 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je0495942 | PROPblock_1 | declared | 1 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je0495942 | PROPblock_2 | declared | 1 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je0497303 | PROPblock_2 | declared | 6 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je0601098 | PROPblock_19 | declared | 12 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je0601098 | PROPblock_20 | declared | 12 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je060335h | PROPblock_1 | declared | 164 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je301171y | PROPblock_6 | declared | 63 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je4003515 | PROPblock_8 | declared | 25 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je4003515 | PROPblock_9 | declared | 5 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je600565m | PROPblock_5 | declared | 17 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | 2 | search_blocks, search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je700618y | PROPblock_7 | declared | 15 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je700618y | PROPblock_8 | declared | 15 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je700618y | PROPblock_9 | declared | 15 | binary | — | search_blocks | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je800150h | PROPblock_8 | declared | 108 | binary | 2 | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | 2 | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je900064e | PROPblock_5 | declared | 8 | binary | 2 | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je900064e | PROPblock_6 | declared | 10 | binary | 2 | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je900266h | PROPblock_3 | declared | 164 | binary | 2 | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je900711h | PROPblock_3 | declared | 5 | binary | 2 | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je900743e | PROPblock_2 | declared | 15 | binary | 2 | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10.1021/je900743e | PROPblock_3 | declared | 15 | binary | 2 | search_system_registry | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | ---: | ---: | --- |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve ethanol and… | 195 | KEEP ←in 278 | 195 | 4.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 718 | KEEP ←in 7,304 | 700 | 16.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 3 | 5 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=10, p… | 717 | KEEP ←in 7,304 | 717 | 21.0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 4 | 6 | `inspect_block_table` | block_number=GLOBlit_528::PROPblock_1, purpose=Get… | 403 | — | — | 0.1 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 5 | 7 | `inspect_block_table` | block_number=GLOBlit_528::PROPblock_1, purpose=Get… | 1,622 | — | — | 0.1 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 6 | 8 | `inspect_block_table` | block_number=GLOBlit_2574::PROPblock_1, nearest=te… | 259 | — | — | 0.1 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 7 | 9 | `inspect_block_table` | block_number=GLOBlit_2574::PROPblock_1, nearest={'… | 419 | — | — | 0.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 8 | 10 | `inspect_block_table` | block_number=GLOBlit_528::PROPblock_2, purpose=Ins… | 421 | — | — | 0.1 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 9 | 11 | `inspect_block_table` | block_number=GLOBlit_528::PROPblock_2, purpose=Ins… | 1,560 | — | — | 0.1 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10 | 12 | `inspect_block_table` | block_number=GLOBlit_6377::PROPblock_1, purpose=In… | 706 | — | — | 0.1 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 11 | 1 | `L1_query` | context=User wants thermodynamic mixi…, id_catalog… | 30,963 | — | — | 182.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 12 | 2 | `search_system_summary` | compound=['GLOBcomp_2', 'GLOBcomp_1'], purpose=Fin… | 1,047 | KEEP ←in 1,129 | 1047 | 14.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 13 | 3 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 950 | KEEP ←in 31,679 | 848 | 20.9 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 14 | 4 | `resolve_property_ids` | purpose=Resolve property IDs for mixi…, queries=['… | 507 | KEEP ←in 617 | 507 | 5.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 15 | 5 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,303 | KEEP ←in 1,684 | 1288 | 18.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 16 | 6 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_8381,… | 638 | — | — | 0.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 17 | 9 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_220, … | 4,222 | — | — | 0.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 18 | 2 | `L1_query` | context=Already found HE data: GLOBli…, id_catalog… | 276 | — | — | 251.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 19 | 2 | `resolve_property_ids` | limit=10, min_score=50, purpose=Resolve property I… | 244 | KEEP ←in 397 | 244 | 4.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 20 | 4 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,131 | DISCARD ←in 39 | 1073 | 10.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 21 | 5 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,093 | DISCARD ←in 39 | 1035 | 17.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 22 | 6 | `search_system_summary` | compound=['GLOBcomp_2', 'GLOBcomp_1'], property=GL… | 270 | KEEP ←in 161 | 270 | 9.9 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 23 | 7 | `search_system_summary` | compound=['GLOBcomp_2', 'GLOBcomp_1'], property=GL… | 347 | KEEP ←in 159 | 347 | 15.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 24 | 3 | `L1_query` | context=User wants excess molar volum…, id_catalog… | 2,546 | — | — | 122.4 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 25 | 2 | `search_system_summary` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=20, p… | 1,080 | KEEP ←in 1,129 | 1080 | 15.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 26 | 3 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,110 | KEEP ←in 31,679 | 1009 | 22.8 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 27 | 4 | `search_system_registry` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=100, … | 1,249 | KEEP ←in 5,620 | 1053 | 17.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 28 | 7 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_20, purpose=I… | 2,299 | — | — | 0.1 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 29 | 4 | `L1_query` | context=Already found: HE data from G…, id_catalog… | 27,417 | — | — | 234.1 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| **TOTAL** | **153** |  |  | **85,712** |  | **11,413** | **1,006.2** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 11,581 | 1,143 | 12,724 | 1,525 | 10.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,114 | 25,209 | 585 | 4.1 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,129 | 26,224 | 554 | 4.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 4 | L1-worker | claudeopus46 | 3,767 | 437 | 4,204 | 375 | 4.0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,763 | 25,858 | 893 | 7.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,486 | 26,581 | 713 | 7.3 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 7 | L1-worker | claudeopus46 | 3,767 | 7,810 | 11,577 | 1,878 | 15.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,199 | 27,294 | 1,568 | 11.7 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 9 | L1-worker | claudeopus46 | 3,767 | 7,760 | 11,527 | 1,748 | 15.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,324 | 28,419 | 1,278 | 8.8 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,105 | 29,200 | 1,496 | 11.0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 12 | L1-worker | claudeopus46 | 24,095 | 7,085 | 31,180 | 1,373 | 8.7 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 13 | L1-worker | claudeopus46 | 24,095 | 7,741 | 31,836 | 633 | 5.3 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 14 | L1-worker | claudeopus46 | 24,095 | 8,461 | 32,556 | 1,544 | 12.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 15 | L1-worker | claudeopus46 | 24,095 | 9,283 | 33,378 | 654 | 6.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 16 | L1-worker | claudeopus46 | 24,095 | 11,203 | 35,298 | 1,178 | 10.0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 17 | L1-worker | claudeopus46 | 24,062 | 11,939 | 36,001 | 2,724 | 19.7 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 18 | L1-worker | claudeopus46 | 2,320 | 2,853 | 5,173 | 1,128 | 6.8 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 19 | L1-worker | claudeopus46 | 2,106 | 4,088 | 6,194 | 1,492 | 8.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 20 | L1-worker | claudeopus46 | 366 | 1,565 | 1,931 | 1,083 | 4.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 21 | L1-worker | claudeopus46 | 366 | 2,269 | 2,635 | 1,112 | 5.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 22 | L1-worker | claudeopus46 | 627 | 2,733 | 3,360 | 1,381 | 14.4 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 23 | L1-worker | claudeopus46 | 787 | 25,923 | 26,710 | 548 | 6.3 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 24 | L0-main | claudeopus46 | 11,581 | 21,686 | 33,267 | 2,204 | 15.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 25 | L1-worker | claudeopus46 | 24,095 | 9,032 | 33,127 | 853 | 6.0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 26 | L1-worker | claudeopus46 | 24,095 | 9,800 | 33,895 | 692 | 4.3 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 27 | L1-worker | claudeopus46 | 3,767 | 1,715 | 5,482 | 1,437 | 8.7 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 28 | L1-worker | claudeopus46 | 24,095 | 10,831 | 34,926 | 1,944 | 11.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 29 | L1-worker | claudeopus46 | 3,767 | 32,144 | 35,911 | 1,636 | 16.3 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 30 | L1-worker | claudeopus46 | 24,095 | 12,319 | 36,414 | 2,601 | 15.7 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 31 | L1-worker | claudeopus46 | 3,767 | 885 | 4,652 | 646 | 5.0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 32 | L1-worker | claudeopus46 | 24,095 | 13,330 | 37,425 | 1,523 | 9.8 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 33 | L1-worker | claudeopus46 | 3,767 | 2,293 | 6,060 | 1,803 | 11.8 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 34 | L1-worker | claudeopus46 | 24,095 | 15,125 | 39,220 | 2,029 | 11.3 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 35 | L1-worker | claudeopus46 | 24,095 | 16,396 | 40,491 | 4,367 | 26.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 36 | L1-worker | claudeopus46 | 24,095 | 26,290 | 50,385 | 5,490 | 39.3 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 37 | L1-worker | claudeopus46 | 24,095 | 34,650 | 58,745 | 1,272 | 10.7 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 38 | L1-worker | claudeopus46 | 24,095 | 39,234 | 63,329 | 4,888 | 37.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 39 | L1-worker | claudeopus46 | 2,106 | 6,236 | 8,342 | 833 | 4.9 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 40 | L1-worker | claudeopus46 | 2,320 | 4,272 | 6,592 | 1,428 | 8.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 41 | L1-worker | claudeopus46 | 366 | 1,610 | 1,976 | 639 | 3.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 42 | L1-worker | claudeopus46 | 627 | 4,152 | 4,779 | 1,299 | 8.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 43 | L1-worker | claudeopus46 | 366 | 1,865 | 2,231 | 1,383 | 4.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 44 | L1-worker | claudeopus46 | 366 | 1,710 | 2,076 | 1,286 | 4.7 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 45 | L1-worker | claudeopus46 | 1,228 | 7,382 | 8,610 | 651 | 3.9 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 46 | L0-main | claudeopus46 | 11,581 | 22,333 | 33,914 | 1,225 | 8.3 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 47 | L1-worker | claudeopus46 | 24,095 | 8,409 | 32,504 | 858 | 5.7 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 48 | L1-worker | claudeopus46 | 24,095 | 9,499 | 33,594 | 612 | 4.3 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 49 | L1-worker | claudeopus46 | 3,767 | 586 | 4,353 | 400 | 4.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 50 | L1-worker | claudeopus46 | 24,095 | 9,112 | 33,207 | 803 | 6.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 51 | L1-worker | claudeopus46 | 24,095 | 9,819 | 33,914 | 717 | 5.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 52 | L1-worker | claudeopus46 | 3,767 | 613 | 4,380 | 1,381 | 9.9 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 53 | L1-worker | claudeopus46 | 24,095 | 10,936 | 35,031 | 875 | 5.9 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 54 | L1-worker | claudeopus46 | 3,767 | 509 | 4,276 | 1,711 | 11.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 55 | L1-worker | claudeopus46 | 24,095 | 12,407 | 36,502 | 866 | 6.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 56 | L1-worker | claudeopus46 | 3,767 | 639 | 4,406 | 469 | 4.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 57 | L1-worker | claudeopus46 | 24,095 | 13,055 | 37,150 | 1,496 | 9.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 58 | L1-worker | claudeopus46 | 3,767 | 665 | 4,432 | 655 | 5.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 59 | L1-worker | claudeopus46 | 24,095 | 13,821 | 37,916 | 1,584 | 11.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 60 | L1-worker | claudeopus46 | 2,106 | 2,583 | 4,689 | 92 | 2.0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 61 | L1-worker | claudeopus46 | 2,320 | 1,242 | 3,562 | 529 | 3.4 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 62 | L1-worker | claudeopus46 | 627 | 1,122 | 1,749 | 735 | 4.1 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 63 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 64 | L1-worker | claudeopus46 | 787 | 3,619 | 4,406 | 448 | 3.7 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 65 | L0-main | claudeopus46 | 11,581 | 27,805 | 39,386 | 2,047 | 12.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 66 | L1-worker | claudeopus46 | 24,095 | 11,708 | 35,803 | 1,063 | 7.0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 67 | L1-worker | claudeopus46 | 24,095 | 12,502 | 36,597 | 586 | 4.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 68 | L1-worker | claudeopus46 | 3,767 | 1,632 | 5,399 | 1,413 | 9.9 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 69 | L1-worker | claudeopus46 | 24,095 | 13,534 | 37,629 | 1,647 | 10.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 70 | L1-worker | claudeopus46 | 3,767 | 32,136 | 35,903 | 1,791 | 16.7 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 71 | L1-worker | claudeopus46 | 24,095 | 15,245 | 39,340 | 877 | 6.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 72 | L1-worker | claudeopus46 | 3,767 | 6,123 | 9,890 | 1,727 | 12.0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 73 | L1-worker | claudeopus46 | 24,095 | 16,872 | 40,967 | 4,843 | 31.0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 74 | L1-worker | claudeopus46 | 24,095 | 25,904 | 49,999 | 5,076 | 35.0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 75 | L1-worker | claudeopus46 | 24,095 | 32,774 | 56,869 | 1,704 | 11.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 76 | L1-worker | claudeopus46 | 24,095 | 35,457 | 59,552 | 4,148 | 31.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 77 | L1-worker | claudeopus46 | 2,320 | 4,841 | 7,161 | 1,359 | 8.7 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 78 | L1-worker | claudeopus46 | 627 | 4,721 | 5,348 | 1,369 | 11.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 79 | L1-worker | claudeopus46 | 366 | 1,796 | 2,162 | 1,309 | 4.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 80 | L1-worker | claudeopus46 | 2,106 | 6,829 | 8,935 | 3,955 | 14.3 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 81 | L1-worker | claudeopus46 | 366 | 4,732 | 5,098 | 3,101 | 11.9 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 82 | L1-worker | claudeopus46 | 1,228 | 11,784 | 13,012 | 573 | 5.3 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 83 | L1-worker | claudeopus46 | 787 | 24,577 | 25,364 | 681 | 6.9 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 84 | L0-main | claudeopus46 | 11,581 | 50,808 | 62,389 | 7,569 | 55.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 85 | L0-main | claudeopus46 | 2,320 | 7,120 | 9,440 | 1,222 | 7.6 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 86 | L0-main | claudeopus46 | 2,106 | 8,095 | 10,201 | 1,460 | 9.4 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 87 | L0-main | claudeopus46 | 366 | 1,697 | 2,063 | 1,173 | 4.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 88 | L0-main | claudeopus46 | 366 | 2,009 | 2,375 | 1,500 | 6.2 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 89 | L0-main | claudeopus46 | 560 | 9,565 | 10,125 | 624 | 4.3 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 90 | L0-main | claudeopus46 | 560 | 8,339 | 8,899 | 447 | 3.3 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 91 | L0-main | claudeopus46 | 1,156 | 12,922 | 14,078 | 1,836 | 11.9 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 92 | L0-main | claudeopus46 | 366 | 2,529 | 2,895 | 1,768 | 6.5 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
| 93 | verdict | claudeopus46 | 972 | 12,183 | 13,155 | 1,135 | 11.0 | Find experimental data for binary mixtures of ethanol and wa (query_runs/run_11) |
