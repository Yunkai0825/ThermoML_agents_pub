# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 21 | 324,044 | 490,289 | 26,797 | 814,333 | 38,777 | 200.4 | claudeopus46 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| L1-worker | 19 | 258,823 | 201,057 | 49,906 | 459,880 | 24,204 | 303.1 | claudeopus46 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| **TOTAL** | **40** | **582,867** | **691,346** | **76,703** | **1,274,213** | **62,981** | **503.5** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `query_thermoml` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `query_thermoml` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `search_blocks` | 2 | 1 | 3 | 2 | 7 | 7 | 302 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| `query_thermoml` | 2 | 1 | 3 | 2 | 6 | 6 | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| **TOTAL** | **6** | **2** | **6** | **4** | **13** | **13** | **302** |  |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBcomp_1 |  | query_thermoml, resolve_compound_ids, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBcomp_24 |  | query_thermoml, resolve_compound_ids, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBlit_2656 |  | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBlit_5201 |  | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBlit_6951 |  | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBlit_8038 |  | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBlit_8106 |  | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBlit_11186 |  | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBlit_11506 |  | search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBprop_4 | Viscosity, Pa*s | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBmeas_4 | Viscosity, Pa*s | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBmeas_11 | Viscosity, Pa*s | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBmeas_8 | Viscosity, Pa*s | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBmeas_227 | Viscosity, Pa*s | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBmeas_142 | Viscosity, Pa*s | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBmeas_165 | Viscosity, Pa*s | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBphase_1 |  | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBvar_5 | Mass fraction | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBconstr_2 | Temperature, K | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBblocktype_1 |  | query_thermoml | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | ---: | --- |
| Unique Compounds | 2 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| Unique References | 7 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| Unique Properties | 1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| Unique Measurements | 6 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| Unique Phases | 1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| Unique Variables | 3 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| Unique Constraints | 2 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| Unique Block_Types | 1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| Unique parent blocks | 7 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| Explicit block/subsystem targets | 7 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| Subsystem targets | 0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| Target-matched data points | 588 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| **TOTAL** | **625** |  |


## 3. DOI & Block References

| DOI | Blocks | Datapoints | System types | Source tools | Source |
| --- | ---: | ---: | --- | --- | --- |
| 10.1016/j.jct.2006.01.011 | 1 | 10 | binary | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 10.1016/j.jct.2018.02.022 | 1 | 84 | binary | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 10.1021/acs.jced.6b00526 | 1 | 33 | binary | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 10.1021/je020140j | 1 | 77 | binary | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 10.1021/je025610o | 1 | 30 | binary | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 10.1021/je800271e | 1 | 52 | binary | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 10.1021/je9000697 | 1 | 16 | binary | search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | --- | --- | ---: | --- | ---: | --- | --- |
| 10.1016/j.jct.2006.01.011 | PROPblock_13 | declared | 10 | binary | 2 | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 10.1016/j.jct.2018.02.022 | PROPblock_24 | declared | 84 | binary | 2 | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 10.1021/acs.jced.6b00526 | PROPblock_18 | declared | 33 | binary | 2 | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 10.1021/je020140j | PROPblock_5 | declared | 77 | binary | 2 | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 10.1021/je025610o | PROPblock_5 | declared | 30 | binary | 2 | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 10.1021/je800271e | PROPblock_4 | declared | 52 | binary | 2 | query_thermoml, search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 10.1021/je9000697 | PROPblock_1 | declared | 16 | binary | — | search_blocks | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | --- | ---: | --- |
| 1 | 1 | `query_thermoml` | id_catalog=[{'id': 'GLOBprop_4', 'type':…, instruc… | 189 | — | — | 0.0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 2 | 2 | `query_thermoml` | id_catalog=[{'global_id': 'GLOBprop_4', …, instruc… | 233 | — | — | 0.0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 3 | 1 | `resolve_compound_ids` | purpose=Resolve compound IDs for wate…, queries=['… | 193 | KEEP ←in 288 | 193 | 4.1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 4 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,273 | KEEP ←in 9,915 | 1273 | 19.9 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 5 | 3 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_24'], limit=50, … | 1,162 | DISCARD ←in 39 | 1104 | 14.9 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 6 | 5 | `inspect_block_table` | block_number=PROPblock_13, literature=GLOBlit_2656… | 261 | — | — | 0.0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 7 | 5 | `inspect_block_table` | block_number=PROPblock_24, literature=GLOBlit_5201… | 261 | — | — | 0.0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 8 | 5 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_6951… | 261 | — | — | 0.0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 9 | 5 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_8038,… | 261 | — | — | 0.0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 10 | 5 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_11186… | 261 | — | — | 0.0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 11 | 6 | `inspect_block_table` | block_number=PROPblock_13, literature=GLOBlit_2656… | 384 | — | — | 0.1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 12 | 6 | `inspect_block_table` | block_number=PROPblock_24, literature=GLOBlit_5201… | 378 | — | — | 0.1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 13 | 6 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_6951… | 364 | — | — | 0.2 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 14 | 6 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_8038,… | 374 | — | — | 0.1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 15 | 6 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_11186… | 340 | — | — | 0.1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 16 | 7 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_8106,… | 1,513 | — | — | 0.1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 17 | 9 | `inspect_block_table` | block_number=GLOBlit_2656::PROPblock_13, purpose=G… | 1,253 | — | — | 0.1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 18 | 9 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_24, purpose=G… | 1,481 | — | — | 0.1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 19 | 9 | `inspect_block_table` | block_number=GLOBlit_6951::PROPblock_18, purpose=G… | 1,412 | — | — | 0.1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 20 | 9 | `inspect_block_table` | block_number=GLOBlit_8038::PROPblock_5, purpose=Gr… | 2,629 | — | — | 0.1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 21 | 9 | `inspect_block_table` | block_number=GLOBlit_11186::PROPblock_4, purpose=G… | 1,229 | — | — | 0.1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 22 | 3 | `query_thermoml` | id_catalog=[{'global_id': 'GLOBprop_4', …, instruc… | 66,728 | — | — | 300.3 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 23 | 6 | `inspect_block` | block_number=PROPblock_24, doi=10.1016/j.jct.2018.… | 1,379 | — | — | 0.4 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 24 | 10 | `fit_block` | block_number=PROPblock_24, doi=10.1016/j.jct.2018.… | 269 | — | — | 0.1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 25 | 11 | `fit_block` | block_number=PROPblock_24, doi=10.1016/j.jct.2018.… | 899 | — | — | 2.0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| **TOTAL** | **147** |  |  | **84,987** |  | **2,570** | **342.9** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 22,518 | 999 | 23,517 | 981 | 9.7 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 2 | L0-main | claudeopus46 | 22,518 | 1,642 | 24,160 | 834 | 6.0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 3 | L0-main | claudeopus46 | 22,518 | 2,346 | 24,864 | 907 | 5.7 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 4 | L1-worker | claudeopus46 | 24,095 | 1,089 | 25,184 | 671 | 5.0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 5 | L1-worker | claudeopus46 | 3,767 | 472 | 4,239 | 389 | 3.9 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,715 | 25,810 | 1,230 | 6.8 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,755 | 26,850 | 1,050 | 6.3 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 8 | L1-worker | claudeopus46 | 3,767 | 10,398 | 14,165 | 1,603 | 13.9 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 9 | L1-worker | claudeopus46 | 3,767 | 561 | 4,328 | 1,370 | 9.3 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,308 | 29,403 | 3,193 | 18.5 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 11 | L1-worker | claudeopus46 | 24,095 | 11,349 | 35,444 | 12,580 | 73.9 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 12 | L1-worker | claudeopus46 | 24,095 | 13,883 | 37,978 | 1,555 | 7.6 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 13 | L1-worker | claudeopus46 | 24,095 | 16,921 | 41,016 | 6,839 | 41.9 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 14 | L1-worker | claudeopus46 | 24,095 | 18,924 | 43,019 | 2,983 | 23.5 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 15 | L1-worker | claudeopus46 | 24,095 | 26,553 | 50,648 | 1,448 | 8.7 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 16 | L1-worker | claudeopus46 | 24,095 | 29,199 | 53,294 | 6,311 | 38.5 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 17 | L1-worker | claudeopus46 | 2,320 | 3,913 | 6,233 | 1,099 | 6.3 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 18 | L1-worker | claudeopus46 | 627 | 3,793 | 4,420 | 1,372 | 8.5 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 19 | L1-worker | claudeopus46 | 2,106 | 5,123 | 7,229 | 2,351 | 9.9 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 20 | L1-worker | claudeopus46 | 366 | 1,536 | 1,902 | 1,059 | 3.9 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 21 | L1-worker | claudeopus46 | 366 | 3,128 | 3,494 | 1,862 | 7.4 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 22 | L1-worker | claudeopus46 | 787 | 44,437 | 45,224 | 941 | 9.3 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 23 | L0-main | claudeopus46 | 22,518 | 35,862 | 58,380 | 1,372 | 11.6 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 24 | L0-main | claudeopus46 | 22,518 | 36,642 | 59,160 | 570 | 4.8 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 25 | L0-main | claudeopus46 | 22,518 | 37,293 | 59,811 | 604 | 5.1 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 26 | L0-main | claudeopus46 | 22,518 | 39,000 | 61,518 | 1,225 | 9.6 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 27 | L0-main | claudeopus46 | 22,518 | 39,686 | 62,204 | 1,724 | 12.5 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 28 | L0-main | claudeopus46 | 22,518 | 40,360 | 62,878 | 896 | 6.6 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 29 | L0-main | claudeopus46 | 22,518 | 41,080 | 63,598 | 924 | 7.0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 30 | L0-main | claudeopus46 | 22,518 | 41,027 | 63,545 | 1,091 | 7.4 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 31 | L0-main | claudeopus46 | 22,518 | 43,825 | 66,343 | 4,212 | 30.7 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 32 | L0-main | claudeopus46 | 22,518 | 50,037 | 72,555 | 3,691 | 25.5 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 33 | L0-main | claudeopus46 | 22,518 | 56,073 | 78,591 | 3,129 | 23.2 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 34 | L0-main | claudeopus46 | 2,106 | 4,356 | 6,462 | 154 | 2.4 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 35 | L0-main | claudeopus46 | 366 | 677 | 1,043 | 195 | 2.2 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 36 | L0-main | claudeopus46 | 2,320 | 3,258 | 5,578 | 1,234 | 8.0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 37 | L0-main | claudeopus46 | 366 | 1,671 | 2,037 | 1,189 | 4.5 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 38 | L0-main | claudeopus46 | 560 | 3,779 | 4,339 | 100 | 3.5 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 39 | L0-main | claudeopus46 | 1,156 | 4,578 | 5,734 | 567 | 5.0 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
| 40 | L0-main | claudeopus46 | 1,918 | 6,098 | 8,016 | 1,198 | 9.4 | Fit a Redlich-Kister polynomial to the viscosity of the bina (analysis_runs/run_1) |
