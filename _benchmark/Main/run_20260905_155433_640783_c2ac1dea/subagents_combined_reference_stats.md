# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 7 | 39,901 | 28,333 | 8,436 | 68,234 | 9,747 | 56.2 | claudeopus46 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| L1-worker | 32 | 335,821 | 88,413 | 22,774 | 424,234 | 13,257 | 182.1 | claudeopus46 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| verdict | 1 | 972 | 4,518 | 1,023 | 5,490 | 5,490 | 8.7 | claudeopus46 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| L0-main | 7 | 39,901 | 36,382 | 7,504 | 76,283 | 10,897 | 51.6 | claudeopus46 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| L1-worker | 25 | 251,869 | 116,675 | 27,676 | 368,544 | 14,741 | 184.0 | claudeopus46 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| verdict | 1 | 972 | 4,829 | 1,106 | 5,801 | 5,801 | 9.5 | claudeopus46 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| L0-main | 17 | 123,050 | 308,381 | 23,909 | 431,431 | 25,378 | 157.3 | claudeopus46 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| L1-worker | 46 | 708,176 | 451,343 | 65,338 | 1,159,519 | 25,206 | 463.3 | claudeopus46 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| verdict | 1 | 972 | 12,452 | 1,182 | 13,424 | 13,424 | 11.3 | claudeopus46 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| **TOTAL** | **137** | **1,501,634** | **1,051,326** | **158,948** | **2,552,960** | **123,941** | **1,124.0** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `resolve_compound_ids` | 20 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| `resolve_compound_ids` | 20 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| `search_id_alignment` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| `search_id_alignment` | 20 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| `search_id_alignment` | 20 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| `search_blocks` | 5 | 6 | 5 | 2 | 6 | 9 | 332 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| `search_blocks` | 2 | 6 | 5 | 2 | 5 | 6 | 308 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| `search_blocks` | 2 | 6 | 5 | 2 | 5 | 6 | 308 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| `search_blocks` | 2 | 6 | 5 | 2 | 5 | 6 | 308 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| **TOTAL** | **95** | **24** | **20** | **8** | **21** | **27** | **1,256** |  |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | --- | --- |
| Unique Compounds | 57 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| Unique parent blocks | 0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| Explicit block/subsystem targets | 0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| Subsystem targets | 0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| Target-matched data points | 0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| GLOBlit_3147 |  | search_blocks |
| GLOBlit_3168 |  | search_blocks |
| GLOBlit_8200 |  | search_blocks |
| GLOBlit_8564 |  | search_blocks |
| GLOBlit_8573 |  | search_blocks |
| GLOBlit_10066 |  | search_blocks |
| GLOBcomp_952 | 1,3,5-trioxane | search_blocks |
| GLOBcomp_1 | water | search_blocks |
| GLOBcomp_4 | methanol | search_blocks |
| GLOBcomp_2 | ethanol | search_blocks |
| GLOBcomp_6 | propan-2-ol | search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_84 | Partial molar volume, m3/mol | search_blocks |
| GLOBprop_20 | Liquid-liquid equilibrium temperature, K | search_blocks |
| GLOBprop_2 | Mole fraction | search_blocks |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_89 | Partial molar volume, m3/mol | search_blocks |
| GLOBmeas_135 | Liquid-liquid equilibrium temperature, K | search_blocks |
| GLOBmeas_1 | Mole fraction | search_blocks |
| GLOBmeas_2218 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_20 | Speed of sound, m/s | search_blocks |
| GLOBphase_1 |  | search_blocks |
| GLOBphase_4 |  | search_blocks |
| GLOBphase_3 |  | search_blocks |
| GLOBsolvent_1 |  | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| Unique References | 6 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| Unique Compounds | 5 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| Unique Properties | 6 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| Unique Measurements | 6 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| Unique Phases | 3 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| Unique Solvents | 1 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| Unique Variables | 5 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| Unique Constraints | 2 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| Unique parent blocks | 9 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| Explicit block/subsystem targets | 9 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| Subsystem targets | 0 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| Target-matched data points | 332 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_952 | 1,3,5-trioxane | search_blocks |
| GLOBlit_3147 |  | search_blocks |
| GLOBlit_3168 |  | search_blocks |
| GLOBlit_8200 |  | search_blocks |
| GLOBlit_8573 |  | search_blocks |
| GLOBlit_10066 |  | search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_84 | Partial molar volume, m3/mol | search_blocks |
| GLOBprop_20 | Liquid-liquid equilibrium temperature, K | search_blocks |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBprop_2 | Mole fraction | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_89 | Partial molar volume, m3/mol | search_blocks |
| GLOBmeas_135 | Liquid-liquid equilibrium temperature, K | search_blocks |
| GLOBmeas_2218 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_1 | Mole fraction | search_blocks |
| GLOBmeas_20 | Speed of sound, m/s | search_blocks |
| GLOBphase_1 |  | search_blocks |
| GLOBphase_4 |  | search_blocks |
| GLOBphase_3 |  | search_blocks |
| GLOBsolvent_1 |  | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| Unique Compounds | 2 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| Unique References | 5 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| Unique Properties | 6 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| Unique Measurements | 6 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| Unique Phases | 3 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| Unique Solvents | 1 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| Unique Variables | 5 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| Unique Constraints | 2 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| Unique parent blocks | 6 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| Explicit block/subsystem targets | 6 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| Subsystem targets | 0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| Target-matched data points | 924 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| **TOTAL** | **1,407** |  |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | ---: | ---: | --- |
| 1 | 2 | `resolve_compound_ids` | limit=20, min_score=40, purpose=Find all compounds… | 790 | DISCARD ←in 1,805 | 725 | 11.1 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 2 | 3 | `resolve_compound_ids` | limit=20, min_score=40, purpose=Find ethylene oxid… | 562 | DISCARD ←in 1,772 | 497 | 8.9 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 3 | 4 | `search_id_alignment` | entity_type=compound, limit=20, purpose=Find ethyl… | 242 | KEEP ←in 283 | 242 | 4.2 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 4 | 5 | `search_id_alignment` | entity_type=compound, limit=20, purpose=Find triox… | 418 | KEEP ←in 1,997 | 418 | 7.0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 5 | 6 | `search_id_alignment` | entity_type=compound, limit=20, purpose=Find triox… | 823 | DISCARD ←in 1,892 | 759 | 11.8 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 6 | 1 | `L1_query` | context=User is trying to identify wh…, id_catalog… | 3,244 | — | — | 100.1 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 7 | 1 | `resolve_compound_ids` | purpose=Resolve water compound ID for…, queries=wa… | 156 | KEEP ←in 216 | 156 | 3.8 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 8 | 2 | `search_blocks` | compound=['GLOBcomp_952', 'GLOBcomp_1'], limit=50,… | 839 | DISCARD ←in 39 | 781 | 15.5 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 9 | 3 | `search_blocks` | compound=['GLOBcomp_2407', 'GLOBcomp_1…, limit=50,… | 741 | DISCARD ←in 39 | 683 | 14.4 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 10 | 4 | `search_blocks` | compound=['GLOBcomp_1480', 'GLOBcomp_1…, limit=50,… | 756 | DISCARD ←in 39 | 698 | 13.0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 11 | 2 | `L1_query` | context=User wants viscosity data for…, id_catalog… | 1,667 | — | — | 91.6 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 1 | 1 | `search_blocks` | compound=GLOBcomp_952, limit=50, property=GLOBprop… | 664 | DISCARD ←in 39 | 606 | 13.6 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 2 | 2 | `search_blocks` | compound=GLOBcomp_952, limit=50, property=GLOBprop… | 903 | DISCARD ←in 39 | 845 | 14.5 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 3 | 3 | `search_blocks` | compound=GLOBcomp_952, limit=50, purpose=Find all … | 667 | DISCARD ←in 39 | 609 | 8.2 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 4 | 1 | `L1_query` | context=We are searching for any visc…, id_catalog… | 1,660 | — | — | 70.4 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 5 | 1 | `search_blocks` | compound=GLOBcomp_952, limit=50, property=GLOBprop… | 746 | DISCARD ←in 39 | 688 | 13.5 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 6 | 2 | `search_blocks` | compound=GLOBcomp_952, limit=50, property=GLOBprop… | 780 | DISCARD ←in 39 | 722 | 6.6 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 7 | 3 | `search_blocks` | compound=GLOBcomp_952, limit=50, purpose=Find all … | 1,348 | KEEP ←in 5,747 | 1228 | 12.9 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 8 | 2 | `L1_query` | context=We already confirmed no pure-…, id_catalog… | 45,769 | — | — | 123.4 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 1 | 1 | `memory_catalog_add` | global_id=GLOBcomp_952, name=1,3,5-trioxane, regis… | 2 | — | — | 0.0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 2 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve water to gl… | 206 | KEEP ←in 216 | 206 | 3.5 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 3 | 3 | `search_blocks` | compound=['GLOBcomp_952', 'GLOBcomp_1'], limit=50,… | 1,293 | KEEP ←in 8,182 | 1293 | 15.8 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 4 | 5 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_3147,… | 2,230 | — | — | 0.2 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_3168,… | 1,862 | — | — | 0.1 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 6 | 9 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_8200,… | 1,197 | — | — | 0.1 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 7 | 11 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_8573,… | 1,144 | — | — | 0.4 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 8 | 2 | `L1_query` | context=We already know viscosity dat…, id_catalog… | 374 | — | — | 183.2 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 9 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve water to gl… | 181 | KEEP ←in 216 | 181 | 3.5 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 10 | 3 | `search_blocks` | compound=['GLOBcomp_952', 'GLOBcomp_1'], limit=50,… | 1,244 | KEEP ←in 8,182 | 1244 | 21.8 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 11 | 4 | `search_blocks` | compound=['GLOBcomp_952', 'GLOBcomp_1'], limit=50,… | 1,316 | KEEP ←in 8,182 | 1316 | 18.5 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 12 | 6 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_3147,… | 2,230 | — | — | 0.2 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 13 | 8 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_3168,… | 1,862 | — | — | 0.1 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 14 | 10 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_8200,… | 1,197 | — | — | 0.1 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 15 | 12 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_8573,… | 1,144 | — | — | 0.1 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 16 | 3 | `L1_query` | context=Previous query errored on cor…, id_catalog… | 61,054 | — | — | 243.4 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 17 | 4 | `memory_catalog_add` | global_id=GLOBlit_3147, name=2010-cib-ale-0 (mass … | 2 | — | — | 0.0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 18 | 5 | `memory_catalog_add` | global_id=GLOBlit_3168, name=2010-cib--0 (partial … | 2 | — | — | 0.2 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 19 | 6 | `memory_catalog_add` | global_id=GLOBlit_8200, name=2004-gru-has-0 (LLE t… | 2 | — | — | 0.0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 20 | 8 | `memory_catalog_add` | global_id=GLOBlit_8573, name=2005-alb-has-0 (VLE),… | 2 | — | — | 0.0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 21 | 9 | `memory_catalog_add` | global_id=GLOBlit_10066, name=2013-cib--0 (speed o… | 2 | — | — | 0.0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| **TOTAL** | **168** |  |  | **141,321** |  | **13,897** | **1,035.7** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 11,581 | 1,053 | 12,634 | 1,494 | 9.9 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,106 | 25,201 | 803 | 5.8 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,247 | 26,342 | 684 | 4.4 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 4 | L1-worker | claudeopus46 | 3,767 | 2,026 | 5,793 | 1,226 | 10.2 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,353 | 26,448 | 627 | 4.8 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 6 | L1-worker | claudeopus46 | 3,767 | 1,935 | 5,702 | 1,018 | 8.1 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,208 | 27,303 | 767 | 6.1 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 8 | L1-worker | claudeopus46 | 3,767 | 461 | 4,228 | 441 | 4.0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 9 | L1-worker | claudeopus46 | 24,095 | 3,809 | 27,904 | 553 | 4.5 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 10 | L1-worker | claudeopus46 | 3,767 | 2,159 | 5,926 | 679 | 6.6 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 11 | L1-worker | claudeopus46 | 24,095 | 4,507 | 28,602 | 589 | 4.7 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 12 | L1-worker | claudeopus46 | 3,767 | 2,053 | 5,820 | 1,331 | 11.2 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 13 | L1-worker | claudeopus46 | 24,095 | 5,613 | 29,708 | 1,783 | 12.4 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 14 | L1-worker | claudeopus46 | 2,106 | 2,705 | 4,811 | 312 | 3.3 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 15 | L1-worker | claudeopus46 | 2,320 | 1,478 | 3,798 | 677 | 4.9 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 16 | L1-worker | claudeopus46 | 627 | 1,358 | 1,985 | 605 | 4.9 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 17 | L1-worker | claudeopus46 | 366 | 1,089 | 1,455 | 206 | 2.3 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 18 | L1-worker | claudeopus46 | 366 | 1,114 | 1,480 | 637 | 3.4 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 19 | L1-worker | claudeopus46 | 787 | 4,553 | 5,340 | 579 | 5.0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 20 | L0-main | claudeopus46 | 11,581 | 8,013 | 19,594 | 2,153 | 14.8 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 21 | L1-worker | claudeopus46 | 24,095 | 5,206 | 29,301 | 1,023 | 7.4 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 22 | L1-worker | claudeopus46 | 3,767 | 374 | 4,141 | 269 | 3.7 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 23 | L1-worker | claudeopus46 | 24,095 | 5,659 | 29,754 | 1,086 | 7.2 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 24 | L1-worker | claudeopus46 | 3,767 | 549 | 4,316 | 1,000 | 8.4 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 25 | L1-worker | claudeopus46 | 24,095 | 6,818 | 30,913 | 868 | 6.6 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 26 | L1-worker | claudeopus46 | 3,767 | 515 | 4,282 | 895 | 7.0 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 27 | L1-worker | claudeopus46 | 24,095 | 7,918 | 32,013 | 948 | 6.9 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 28 | L1-worker | claudeopus46 | 3,767 | 499 | 4,266 | 906 | 6.8 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 29 | L1-worker | claudeopus46 | 24,095 | 9,114 | 33,209 | 832 | 6.7 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 30 | L1-worker | claudeopus46 | 2,106 | 2,851 | 4,957 | 92 | 1.9 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 31 | L1-worker | claudeopus46 | 2,320 | 963 | 3,283 | 228 | 2.5 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 32 | L1-worker | claudeopus46 | 627 | 843 | 1,470 | 445 | 3.7 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 33 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 1.9 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 34 | L1-worker | claudeopus46 | 787 | 2,461 | 3,248 | 598 | 4.8 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 35 | L0-main | claudeopus46 | 11,581 | 11,878 | 23,459 | 2,424 | 14.9 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 36 | L0-main | claudeopus46 | 2,320 | 2,128 | 4,448 | 548 | 3.6 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 37 | L0-main | claudeopus46 | 2,106 | 3,013 | 5,119 | 676 | 5.7 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 38 | L0-main | claudeopus46 | 366 | 1,023 | 1,389 | 509 | 4.1 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 39 | L0-main | claudeopus46 | 366 | 1,225 | 1,591 | 632 | 3.2 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 40 | verdict | claudeopus46 | 972 | 4,518 | 5,490 | 1,023 | 8.7 | Find viscosity data for the ethylene trioxide and water bina (query_runs/run_1) |
| 1 | L0-main | claudeopus46 | 11,581 | 962 | 12,543 | 1,200 | 7.5 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,086 | 25,181 | 739 | 5.6 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 3 | L1-worker | claudeopus46 | 3,767 | 440 | 4,207 | 804 | 7.1 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 4 | L1-worker | claudeopus46 | 24,095 | 2,059 | 26,154 | 861 | 5.8 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 5 | L1-worker | claudeopus46 | 3,767 | 434 | 4,201 | 1,046 | 7.8 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 6 | L1-worker | claudeopus46 | 24,095 | 3,365 | 27,460 | 839 | 6.0 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 7 | L1-worker | claudeopus46 | 3,767 | 386 | 4,153 | 949 | 7.8 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 8 | L1-worker | claudeopus46 | 24,095 | 4,408 | 28,503 | 1,110 | 7.2 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 9 | L1-worker | claudeopus46 | 2,106 | 2,027 | 4,133 | 92 | 2.2 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 10 | L1-worker | claudeopus46 | 2,320 | 820 | 3,140 | 398 | 3.3 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 11 | L1-worker | claudeopus46 | 627 | 700 | 1,327 | 403 | 3.2 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 12 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 1.9 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 13 | L1-worker | claudeopus46 | 787 | 2,311 | 3,098 | 495 | 4.2 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 14 | L0-main | claudeopus46 | 11,581 | 4,641 | 16,222 | 1,402 | 9.3 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 15 | L1-worker | claudeopus46 | 24,095 | 3,171 | 27,266 | 1,106 | 7.2 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 16 | L1-worker | claudeopus46 | 3,767 | 446 | 4,213 | 898 | 6.8 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 17 | L1-worker | claudeopus46 | 24,095 | 4,288 | 28,383 | 768 | 5.4 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 18 | L1-worker | claudeopus46 | 3,767 | 450 | 4,217 | 927 | 6.2 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 19 | L1-worker | claudeopus46 | 24,095 | 5,471 | 29,566 | 706 | 4.7 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 20 | L1-worker | claudeopus46 | 3,767 | 6,090 | 9,857 | 1,452 | 12.3 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 21 | L1-worker | claudeopus46 | 24,095 | 7,169 | 31,264 | 2,955 | 16.9 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 22 | L1-worker | claudeopus46 | 24,095 | 12,466 | 36,561 | 4,313 | 25.6 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 23 | L1-worker | claudeopus46 | 627 | 1,880 | 2,507 | 559 | 3.5 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 24 | L1-worker | claudeopus46 | 2,320 | 2,000 | 4,320 | 509 | 3.9 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 25 | L1-worker | claudeopus46 | 2,106 | 3,548 | 5,654 | 2,654 | 10.8 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 26 | L1-worker | claudeopus46 | 366 | 3,431 | 3,797 | 2,119 | 9.0 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 27 | L1-worker | claudeopus46 | 787 | 47,360 | 48,147 | 907 | 9.6 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 28 | L0-main | claudeopus46 | 11,581 | 22,686 | 34,267 | 2,718 | 19.9 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 29 | L0-main | claudeopus46 | 2,320 | 2,572 | 4,892 | 612 | 4.2 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 30 | L0-main | claudeopus46 | 2,106 | 3,366 | 5,472 | 519 | 4.7 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 31 | L0-main | claudeopus46 | 366 | 1,087 | 1,453 | 573 | 2.9 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 32 | L0-main | claudeopus46 | 366 | 1,068 | 1,434 | 480 | 3.1 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 33 | verdict | claudeopus46 | 972 | 4,829 | 5,801 | 1,106 | 9.5 | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 1 | L0-main | claudeopus46 | 11,581 | 937 | 12,518 | 638 | 4.9 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 2 | L0-main | claudeopus46 | 11,581 | 1,347 | 12,928 | 1,178 | 7.2 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 3 | L1-worker | claudeopus46 | 24,095 | 1,292 | 25,387 | 527 | 4.9 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 4 | L1-worker | claudeopus46 | 24,095 | 2,284 | 26,379 | 510 | 4.4 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 5 | L1-worker | claudeopus46 | 3,767 | 365 | 4,132 | 330 | 3.4 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,916 | 26,011 | 746 | 15.5 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 7 | L1-worker | claudeopus46 | 3,767 | 8,640 | 12,407 | 1,588 | 14.7 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,532 | 27,627 | 2,377 | 13.8 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 9 | L1-worker | claudeopus46 | 24,095 | 8,377 | 32,472 | 1,060 | 8.2 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 10 | L1-worker | claudeopus46 | 24,095 | 10,880 | 34,975 | 480 | 6.3 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 11 | L1-worker | claudeopus46 | 24,095 | 11,780 | 35,875 | 521 | 4.9 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 12 | L1-worker | claudeopus46 | 24,095 | 13,228 | 37,323 | 566 | 7.3 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 13 | L1-worker | claudeopus46 | 24,095 | 14,154 | 38,249 | 555 | 4.9 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 14 | L1-worker | claudeopus46 | 24,095 | 14,962 | 39,057 | 656 | 5.4 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 15 | L1-worker | claudeopus46 | 24,095 | 15,889 | 39,984 | 571 | 5.0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 16 | L1-worker | claudeopus46 | 24,095 | 16,654 | 40,749 | 437 | 3.4 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 17 | L1-worker | claudeopus46 | 24,062 | 17,105 | 41,167 | 3,852 | 24.2 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 18 | L1-worker | claudeopus46 | 24,062 | 20,423 | 44,485 | 3,190 | 21.0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 19 | L1-worker | claudeopus46 | 2,320 | 6,090 | 8,410 | 1,344 | 11.5 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 20 | L1-worker | claudeopus46 | 627 | 5,970 | 6,597 | 1,257 | 12.1 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 21 | L1-worker | claudeopus46 | 2,106 | 7,447 | 9,553 | 2,388 | 14.0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 22 | L1-worker | claudeopus46 | 366 | 1,781 | 2,147 | 1,294 | 5.0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 23 | L1-worker | claudeopus46 | 366 | 3,165 | 3,531 | 1,833 | 8.5 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 24 | L1-worker | claudeopus46 | 1,228 | 10,260 | 11,488 | 1,845 | 8.7 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 25 | L0-main | claudeopus46 | 11,581 | 2,019 | 13,600 | 1,281 | 8.2 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 26 | L1-worker | claudeopus46 | 24,095 | 1,315 | 25,410 | 622 | 5.3 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 27 | L1-worker | claudeopus46 | 24,095 | 2,291 | 26,386 | 495 | 4.0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 28 | L1-worker | claudeopus46 | 3,767 | 349 | 4,116 | 305 | 3.4 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 29 | L1-worker | claudeopus46 | 24,095 | 1,925 | 26,020 | 799 | 5.6 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 30 | L1-worker | claudeopus46 | 3,767 | 8,646 | 12,413 | 1,666 | 14.9 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 31 | L1-worker | claudeopus46 | 24,095 | 3,488 | 27,583 | 2,920 | 19.1 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 32 | L1-worker | claudeopus46 | 3,767 | 8,626 | 12,393 | 1,551 | 12.6 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 33 | L1-worker | claudeopus46 | 24,095 | 5,202 | 29,297 | 2,455 | 15.9 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 34 | L1-worker | claudeopus46 | 24,095 | 10,125 | 34,220 | 1,429 | 10.6 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 35 | L1-worker | claudeopus46 | 24,095 | 12,659 | 36,754 | 500 | 6.1 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 36 | L1-worker | claudeopus46 | 24,095 | 13,581 | 37,676 | 551 | 4.9 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 37 | L1-worker | claudeopus46 | 24,095 | 15,027 | 39,122 | 696 | 7.9 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 38 | L1-worker | claudeopus46 | 24,095 | 15,953 | 40,048 | 583 | 4.8 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 39 | L1-worker | claudeopus46 | 24,095 | 16,805 | 40,900 | 649 | 4.8 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 40 | L1-worker | claudeopus46 | 24,095 | 17,755 | 41,850 | 579 | 3.8 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 41 | L1-worker | claudeopus46 | 24,062 | 18,115 | 42,177 | 5,568 | 37.9 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 42 | L1-worker | claudeopus46 | 24,062 | 21,567 | 45,629 | 4,530 | 29.8 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 43 | L1-worker | claudeopus46 | 2,320 | 5,703 | 8,023 | 1,677 | 10.4 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 44 | L1-worker | claudeopus46 | 627 | 5,583 | 6,210 | 1,613 | 11.9 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 45 | L1-worker | claudeopus46 | 2,106 | 7,083 | 9,189 | 2,361 | 12.0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 46 | L1-worker | claudeopus46 | 366 | 2,114 | 2,480 | 1,627 | 6.3 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 47 | L1-worker | claudeopus46 | 366 | 3,138 | 3,504 | 1,764 | 8.4 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 48 | L1-worker | claudeopus46 | 1,228 | 9,899 | 11,127 | 1,842 | 8.5 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 49 | L1-worker | claudeopus46 | 787 | 48,200 | 48,987 | 629 | 7.3 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 50 | L0-main | claudeopus46 | 11,581 | 36,542 | 48,123 | 1,371 | 13.6 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 51 | L0-main | claudeopus46 | 11,581 | 37,088 | 48,669 | 521 | 5.3 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 52 | L0-main | claudeopus46 | 11,581 | 37,503 | 49,084 | 436 | 5.2 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 53 | L0-main | claudeopus46 | 11,581 | 37,887 | 49,468 | 134 | 3.3 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 54 | L0-main | claudeopus46 | 11,581 | 38,741 | 50,322 | 399 | 4.0 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 55 | L0-main | claudeopus46 | 11,581 | 38,405 | 49,986 | 408 | 4.9 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 56 | L0-main | claudeopus46 | 11,581 | 38,772 | 50,353 | 6,897 | 46.3 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 57 | L0-main | claudeopus46 | 2,106 | 6,755 | 8,861 | 1,290 | 8.9 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 58 | L0-main | claudeopus46 | 2,320 | 5,986 | 8,306 | 1,336 | 9.8 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 59 | L0-main | claudeopus46 | 366 | 1,811 | 2,177 | 1,282 | 4.4 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 60 | L0-main | claudeopus46 | 366 | 1,839 | 2,205 | 1,596 | 6.3 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 61 | L0-main | claudeopus46 | 560 | 7,866 | 8,426 | 498 | 4.1 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 62 | L0-main | claudeopus46 | 1,156 | 11,826 | 12,982 | 2,364 | 12.1 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 63 | L0-main | claudeopus46 | 366 | 3,057 | 3,423 | 2,280 | 8.8 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 64 | verdict | claudeopus46 | 972 | 12,452 | 13,424 | 1,182 | 11.3 | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| **TOTAL** |  |  | **1,501,634** | **1,051,326** | **2,552,960** | **158,948** | **1,124.0** |  |


## 3. DOI & Block References

| DOI | Blocks | Datapoints | System types | Source tools | Source |
| --- | ---: | ---: | ---: | --- | --- |
| 10.1016/j.jct.2009.08.015 | 1 | 175 | binary | search_blocks | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 10.1016/j.jct.2009.11.005 | 1 | 25 | binary | search_blocks | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 10.1021/je030243h | 1 | 19 | binary | search_blocks | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 10.1021/je049978s | 3 | 24 | binary | search_blocks | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 10.1021/je050015i | 2 | 36 | binary | search_blocks | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 10.1021/je301352v | 1 | 53 | binary | search_blocks | Search for pure-component viscosity data for 1,3,5-trioxane  (query_runs/run_3) |
| 10.1016/j.jct.2009.08.015 | PROPblock_5 | declared | 175 | binary | — |
| 10.1016/j.jct.2009.11.005 | PROPblock_5 | declared | 25 | binary | — |
| 10.1021/je030243h | PROPblock_1 | declared | 19 | binary | — |
| 10.1021/je049978s | PROPblock_1 | declared | 8 | binary | — |
| 10.1021/je049978s | PROPblock_2 | declared | 8 | binary | — |
| 10.1021/je049978s | PROPblock_3 | declared | 8 | binary | — |
| 10.1021/je050015i | PROPblock_1 | declared | 17 | binary | — |
| 10.1021/je050015i | PROPblock_2 | declared | 19 | binary | — |
| 10.1021/je301352v | PROPblock_5 | declared | 53 | binary | — |
| 10.1016/j.jct.2009.08.015 | 1 | 175 | binary | search_blocks | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 10.1016/j.jct.2009.11.005 | 1 | 25 | binary | search_blocks | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 10.1021/je030243h | 1 | 19 | binary | search_blocks | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 10.1021/je050015i | 2 | 36 | binary | search_blocks | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 10.1021/je301352v | 1 | 53 | binary | search_blocks | Search for ANY property data blocks for the binary system of (query_runs/run_2) |
| 10.1016/j.jct.2009.08.015 | PROPblock_5 | declared | 175 | binary | — |
| 10.1016/j.jct.2009.11.005 | PROPblock_5 | declared | 25 | binary | — |
| 10.1021/je030243h | PROPblock_1 | declared | 19 | binary | — |
| 10.1021/je050015i | PROPblock_1 | declared | 17 | binary | — |
| 10.1021/je050015i | PROPblock_2 | declared | 19 | binary | — |
| 10.1021/je301352v | PROPblock_5 | declared | 53 | binary | — |
| **TOTAL** | **15** | **640** | **640** |  |  |
