# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 8 | 30,036 | 22,285 | 6,389 | 52,321 | 6,540 | 46.9 | claudeopus46 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| L1-worker | 19 | 280,013 | 89,752 | 15,127 | 369,765 | 19,461 | 122.4 | claudeopus46 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| verdict | 1 | 972 | 3,911 | 983 | 4,883 | 4,883 | 8.4 | claudeopus46 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| L0-main | 10 | 41,983 | 124,752 | 28,026 | 166,735 | 16,673 | 169.9 | claudeopus46 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| L1-worker | 40 | 538,706 | 430,515 | 69,451 | 969,221 | 24,230 | 499.8 | claudeopus46 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| verdict | 1 | 972 | 13,291 | 1,104 | 14,263 | 14,263 | 10.3 | claudeopus46 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| **TOTAL** | **79** | **892,682** | **684,506** | **121,080** | **1,577,188** | **86,050** | **857.7** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| `search_blocks` | 1 | 1 | 2 | 1 | 10 | 10 | 60 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| `search_blocks` | 2 | 1 | 5 | 3 | 16 | 17 | 1,379 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| `search_blocks` | 2 | 1 | 5 | 3 | 16 | 17 | 1,379 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| `search_blocks` | 2 | 1 | 5 | 3 | 16 | 17 | 1,379 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| `search_system_registry` | 2 | 1 | 5 | 2 | 13 | 14 | 1,346 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| **TOTAL** | **12** | **5** | **22** | **12** | **71** | **75** | **5,543** |  |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | --- | --- |
| Unique Compounds | 1 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| Unique References | 10 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| Unique Properties | 1 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| Unique Measurements | 6 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| Unique Phases | 2 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| Unique Variables | 2 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| Unique Constraints | 1 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| Unique parent blocks | 10 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| Explicit block/subsystem targets | 10 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| Subsystem targets | 0 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| Target-matched data points | 60 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBcomp_5 |  | resolve_compound_ids, search_blocks, search_system_registry |
| GLOBlit_555 |  | search_blocks, search_system_registry |
| GLOBlit_590 |  | search_blocks, search_system_registry |
| GLOBlit_2432 |  | search_blocks, search_system_registry |
| GLOBlit_2979 |  | search_blocks, search_system_registry |
| GLOBlit_4068 |  | search_blocks, search_system_registry |
| GLOBlit_4415 |  | search_blocks, search_system_registry |
| GLOBlit_5585 |  | search_blocks, search_system_registry |
| GLOBlit_7085 |  | search_blocks, search_system_registry |
| GLOBlit_7178 |  | search_blocks, search_system_registry |
| GLOBlit_8254 |  | search_blocks, search_system_registry |
| GLOBlit_8447 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_10159 |  | search_blocks, search_system_registry |
| GLOBlit_11042 |  | search_blocks |
| GLOBlit_11142 |  | search_blocks, search_system_registry |
| GLOBlit_11872 |  | search_blocks, search_system_registry |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_143 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBphase_1 |  | search_blocks, search_system_registry |
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_8 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBsolvent_1 |  | search_blocks, search_system_registry |
| GLOBsolvent_9 |  | search_blocks |
| GLOBblocktype_1 |  | search_system_registry |
| Unique Compounds | 2 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| Unique References | 16 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| Unique Properties | 1 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| Unique Measurements | 7 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| Unique Phases | 1 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| Unique Variables | 5 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| Unique Constraints | 3 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| Unique Solvents | 2 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| Unique Block_Types | 1 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| Unique parent blocks | 17 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| Explicit block/subsystem targets | 17 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| Subsystem targets | 0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| Target-matched data points | 5,483 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| **TOTAL** | **5,658** |  |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 10.1007/s10765-005-8590-7 | PROPblock_1 | declared | 42 | unary | — | search_blocks | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 10.1016/j.fluid.2005.09.009 | PROPblock_6 | declared | 1 | unary | — | search_blocks | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 10.1016/j.fluid.2007.07.066 | PROPblock_2 | declared | 5 | unary | — | search_blocks | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 10.1016/j.fluid.2007.08.008 | PROPblock_6 | declared | 1 | unary | — | search_blocks | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 10.1016/j.fluid.2008.02.008 | PROPblock_38 | declared | 1 | unary | — | search_blocks | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 10.1016/j.fluid.2008.07.001 | PROPblock_8 | declared | 1 | unary | — | search_blocks | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 10.1016/j.fluid.2009.07.010 | PROPblock_11 | declared | 1 | unary | — | search_blocks | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 10.1016/j.fluid.2010.01.002 | PROPblock_18 | declared | 4 | unary | — | search_blocks | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 10.1016/j.fluid.2012.07.032 | PROPblock_2 | declared | 3 | unary | — | search_blocks | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 10.1016/j.fluid.2012.08.024 | PROPblock_1 | declared | 1 | unary | — | search_blocks | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 10.1016/j.fluid.2007.07.066 | 1 | 15 | binary | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1016/j.fluid.2008.01.004 | 1 | 15 | binary | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1016/j.jct.2004.07.019 | 1 | 456 | binary | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1016/j.jct.2013.11.036 | 2 | 203 | binary | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1016/j.jct.2015.06.024 | 1 | 40 | binary | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1016/j.jct.2019.105880 | 1 | 16 | binary | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1021/acs.jced.7b00299 | 1 | 2 | binary | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1021/je034101z | 1 | 380 | binary | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1021/je049738c | 1 | 8 | binary | search_blocks | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1021/je4003515 | 1 | 25 | binary | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1021/je700700f | 1 | 13 | binary | search_blocks | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1021/je800158z | 1 | 56 | binary | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1021/je900966r | 1 | 30 | binary | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |  |  |
| 10.1016/j.fluid.2007.07.066 | PROPblock_8 | declared | 15 | binary | 2 | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1016/j.fluid.2008.01.004 | PROPblock_5 | declared | 15 | binary | 2 | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1016/j.jct.2004.07.019 | PROPblock_3 | declared | 456 | binary | 2 | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1016/j.jct.2008.07.005 | PROPblock_9 | declared | 96 | binary | 2 | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1016/j.jct.2013.11.036 | PROPblock_1 | declared | 174 | binary | 2 | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1016/j.jct.2013.11.036 | PROPblock_2 | declared | 29 | binary | 2 | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1016/j.jct.2015.06.024 | PROPblock_5 | declared | 40 | binary | 2 | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1016/j.jct.2019.105880 | PROPblock_7 | declared | 16 | binary | 2 | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1021/acs.jced.6b01058 | PROPblock_8 | declared | 12 | binary | 2 | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1021/acs.jced.7b00299 | PROPblock_13 | declared | 2 | binary | 2 | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1021/je034101z | PROPblock_6 | declared | 380 | binary | 2 | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1021/je049738c | PROPblock_26 | declared | 8 | binary | — | search_blocks | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1021/je0601098 | PROPblock_22 | declared | 12 | binary | — | search_blocks | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1021/je4003515 | PROPblock_10 | declared | 25 | binary | 2 | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1021/je700700f | PROPblock_14 | declared | 13 | binary | — | search_blocks | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1021/je800158z | PROPblock_3 | declared | 56 | binary | 2 | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10.1021/je900966r | PROPblock_4 | declared | 30 | binary | 2 | search_blocks, search_system_registry | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| **TOTAL** | **17** | **1,379** | **1,439** |  | **28** |  |  |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | --- | ---: | --- |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve water compo… | 190 | KEEP ←in 216 | 190 | 4.0 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 2 | 4 | `search_blocks` | compound=GLOBcomp_1, limit=10, property=GLOBprop_1… | 1,234 | KEEP ←in 5,651 | 1220 | 15.1 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_306, … | 261 | — | — | 0.0 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_306, … | 333 | — | — | 0.1 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_555, … | 777 | — | — | 0.1 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 6 | 9 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_306, … | 640 | — | — | 0.1 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 7 | 1 | `L1_query` | context=User needs pure water density…, id_catalog… | 12,232 | — | — | 121.4 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 198 | KEEP ←in 283 | 198 | 4.8 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 784 | KEEP ←in 11,346 | 766 | 21.7 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_555, … | 249 | — | — | 0.1 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_555, … | 379 | — | — | 0.2 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_555, … | 980 | — | — | 0.1 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 6 | 8 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 1,179 | KEEP ←in 11,346 | 1164 | 20.8 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 7 | 9 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_2979,… | 1,118 | — | — | 0.1 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 8 | 1 | `L1_query` | context=User wants to know what densi…, id_catalog… | 28,253 | — | — | 257.0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 9 | 1 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_590, … | 249 | — | — | 0.0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10 | 2 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_590, … | 379 | — | — | 0.2 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 11 | 3 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_590, … | 1,125 | — | — | 0.2 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 12 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 1,186 | KEEP ←in 11,346 | 1186 | 22.7 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 13 | 6 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_5'], limit=50, p… | 1,214 | KEEP ←in 2,231 | 1019 | 17.9 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 14 | 2 | `L1_query` | context=Previous search found 17 bloc…, id_catalog… | 82,686 | — | — | 227.7 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| **TOTAL** | **95** |  |  | **135,646** |  | **5,743** | **714.3** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 11,581 | 825 | 12,406 | 972 | 7.9 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 2 | L1-worker | claudeopus46 | 24,095 | 995 | 25,090 | 793 | 6.7 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 3 | L1-worker | claudeopus46 | 24,095 | 1,987 | 26,082 | 516 | 4.0 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 4 | L1-worker | claudeopus46 | 3,767 | 343 | 4,110 | 314 | 3.5 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,622 | 25,717 | 692 | 6.0 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,341 | 26,436 | 661 | 4.7 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 7 | L1-worker | claudeopus46 | 3,767 | 6,058 | 9,825 | 1,527 | 12.0 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,560 | 27,655 | 975 | 7.9 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,209 | 28,304 | 648 | 5.4 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,905 | 29,000 | 1,148 | 8.4 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,063 | 30,158 | 1,203 | 8.7 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 12 | L1-worker | claudeopus46 | 24,095 | 9,989 | 34,084 | 870 | 12.5 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 13 | L1-worker | claudeopus46 | 24,095 | 10,992 | 35,087 | 1,267 | 9.7 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 14 | L1-worker | claudeopus46 | 24,095 | 14,722 | 38,817 | 1,131 | 7.3 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 15 | L1-worker | claudeopus46 | 2,320 | 1,262 | 3,582 | 284 | 3.0 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 16 | L1-worker | claudeopus46 | 627 | 1,142 | 1,769 | 622 | 4.2 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 17 | L1-worker | claudeopus46 | 2,106 | 2,378 | 4,484 | 951 | 5.7 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 18 | L1-worker | claudeopus46 | 366 | 1,728 | 2,094 | 514 | 3.4 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 19 | L1-worker | claudeopus46 | 1,228 | 3,380 | 4,608 | 538 | 3.5 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 20 | L1-worker | claudeopus46 | 787 | 12,076 | 12,863 | 473 | 5.8 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 21 | L0-main | claudeopus46 | 11,581 | 9,091 | 20,672 | 1,754 | 11.9 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 22 | L0-main | claudeopus46 | 2,320 | 1,643 | 3,963 | 594 | 4.1 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 23 | L0-main | claudeopus46 | 2,106 | 2,300 | 4,406 | 758 | 5.6 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 24 | L0-main | claudeopus46 | 366 | 1,069 | 1,435 | 555 | 3.1 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 25 | L0-main | claudeopus46 | 366 | 1,307 | 1,673 | 852 | 4.8 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 26 | L0-main | claudeopus46 | 560 | 2,412 | 2,972 | 187 | 4.1 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 27 | L0-main | claudeopus46 | 1,156 | 3,638 | 4,794 | 717 | 5.4 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 28 | verdict | claudeopus46 | 972 | 3,911 | 4,883 | 983 | 8.4 | Find the experimental density of pure water at 298.15 K. I n (query_runs/run_13) |
| 1 | L0-main | claudeopus46 | 11,581 | 1,037 | 12,618 | 1,220 | 8.3 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,240 | 25,335 | 564 | 4.9 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,258 | 26,353 | 545 | 4.3 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 4 | L1-worker | claudeopus46 | 3,767 | 442 | 4,209 | 376 | 4.7 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,867 | 25,962 | 749 | 6.1 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,560 | 26,655 | 659 | 5.5 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 7 | L1-worker | claudeopus46 | 3,767 | 11,815 | 15,582 | 1,699 | 15.0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,323 | 27,418 | 2,764 | 18.7 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 9 | L1-worker | claudeopus46 | 24,095 | 3,951 | 28,046 | 707 | 6.3 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,655 | 28,750 | 1,439 | 10.3 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,982 | 30,077 | 1,333 | 11.1 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 12 | L1-worker | claudeopus46 | 3,767 | 11,800 | 15,567 | 1,495 | 15.0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 13 | L1-worker | claudeopus46 | 24,095 | 7,592 | 31,687 | 1,093 | 8.8 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 14 | L1-worker | claudeopus46 | 24,095 | 9,089 | 33,184 | 4,910 | 35.4 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 15 | L1-worker | claudeopus46 | 24,095 | 21,125 | 45,220 | 6,373 | 43.8 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 16 | L1-worker | claudeopus46 | 24,095 | 30,815 | 54,910 | 3,749 | 28.4 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 17 | L1-worker | claudeopus46 | 2,320 | 4,100 | 6,420 | 1,018 | 7.8 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 18 | L1-worker | claudeopus46 | 627 | 3,980 | 4,607 | 1,348 | 9.9 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 19 | L1-worker | claudeopus46 | 2,106 | 5,461 | 7,567 | 1,961 | 10.1 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 20 | L1-worker | claudeopus46 | 366 | 1,455 | 1,821 | 983 | 4.6 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 21 | L1-worker | claudeopus46 | 366 | 1,759 | 2,125 | 1,335 | 5.6 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 22 | L1-worker | claudeopus46 | 366 | 2,738 | 3,104 | 1,174 | 5.6 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 23 | L1-worker | claudeopus46 | 787 | 28,242 | 29,029 | 634 | 7.2 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 24 | L0-main | claudeopus46 | 11,581 | 21,959 | 33,540 | 1,923 | 15.7 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 25 | L1-worker | claudeopus46 | 24,095 | 9,603 | 33,698 | 802 | 8.0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 26 | L1-worker | claudeopus46 | 24,095 | 10,200 | 34,295 | 685 | 4.8 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 27 | L1-worker | claudeopus46 | 24,095 | 10,929 | 35,024 | 733 | 12.5 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 28 | L1-worker | claudeopus46 | 24,095 | 12,369 | 36,464 | 811 | 7.3 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 29 | L1-worker | claudeopus46 | 24,095 | 13,134 | 37,229 | 650 | 5.9 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 30 | L1-worker | claudeopus46 | 3,767 | 11,839 | 15,606 | 1,555 | 15.3 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 31 | L1-worker | claudeopus46 | 24,095 | 14,272 | 38,367 | 972 | 7.4 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 32 | L1-worker | claudeopus46 | 3,767 | 2,765 | 6,532 | 1,685 | 12.8 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 33 | L1-worker | claudeopus46 | 24,095 | 15,844 | 39,939 | 5,027 | 33.9 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 34 | L1-worker | claudeopus46 | 24,095 | 26,883 | 50,978 | 5,496 | 38.1 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 35 | L1-worker | claudeopus46 | 24,095 | 36,068 | 60,163 | 3,686 | 28.2 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 36 | L1-worker | claudeopus46 | 2,320 | 2,914 | 5,234 | 588 | 5.1 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 37 | L1-worker | claudeopus46 | 627 | 2,794 | 3,421 | 754 | 6.4 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 38 | L1-worker | claudeopus46 | 366 | 1,025 | 1,391 | 558 | 3.1 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 39 | L1-worker | claudeopus46 | 366 | 1,165 | 1,531 | 741 | 4.3 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 40 | L1-worker | claudeopus46 | 2,106 | 4,640 | 6,746 | 4,040 | 16.2 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 41 | L1-worker | claudeopus46 | 366 | 4,817 | 5,183 | 3,245 | 13.9 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 42 | L1-worker | claudeopus46 | 787 | 83,005 | 83,792 | 515 | 7.5 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 43 | L0-main | claudeopus46 | 11,581 | 52,243 | 63,824 | 8,009 | 57.3 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 44 | L0-main | claudeopus46 | 2,320 | 5,589 | 7,909 | 1,045 | 7.2 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 45 | L0-main | claudeopus46 | 366 | 1,520 | 1,886 | 1,001 | 3.7 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 46 | L0-main | claudeopus46 | 2,106 | 6,458 | 8,564 | 1,794 | 11.3 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 47 | L0-main | claudeopus46 | 366 | 2,343 | 2,709 | 2,809 | 10.4 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 48 | L0-main | claudeopus46 | 560 | 9,355 | 9,915 | 747 | 6.1 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 49 | L0-main | claudeopus46 | 1,156 | 18,429 | 19,585 | 5,126 | 28.9 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 50 | L0-main | claudeopus46 | 366 | 5,819 | 6,185 | 4,352 | 21.0 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| 51 | verdict | claudeopus46 | 972 | 13,291 | 14,263 | 1,104 | 10.3 | Find density measurements for the binary mixture of water an (query_runs/run_12) |
| **TOTAL** |  |  | **892,682** | **684,506** | **1,577,188** | **121,080** | **857.7** |  |
