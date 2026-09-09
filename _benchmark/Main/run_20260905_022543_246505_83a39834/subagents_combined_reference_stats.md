# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 21 | 324,044 | 430,446 | 33,044 | 754,490 | 35,928 | 267.2 | claudeopus46 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| L1-worker | 22 | 331,075 | 153,370 | 36,094 | 484,445 | 22,020 | 269.8 | claudeopus46 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| **TOTAL** | **43** | **655,119** | **583,816** | **69,138** | **1,238,935** | **57,948** | **537.0** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| `search_blocks` | 2 | 1 | 6 | 2 | 9 | 9 | 1,349 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| `search_blocks` | 2 | 1 | 6 | 2 | 9 | 9 | 1,349 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| `query_thermoml` | 2 | 1 | 2 | 1 | 2 | 2 | 0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| **TOTAL** | **8** | **3** | **14** | **5** | **20** | **20** | **2,698** |  |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBcomp_4 |  | query_thermoml, resolve_compound_ids, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBcomp_1 |  | query_thermoml, resolve_compound_ids, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBlit_2432 |  | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBlit_2825 |  | query_thermoml, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBlit_7085 |  | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBlit_8254 |  | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBlit_8424 |  | query_thermoml, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBlit_8869 |  | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBlit_8888 |  | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBlit_9571 |  | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBlit_10866 |  | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBmeas_138 | Mass density, kg/m3 | query_thermoml, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBmeas_280 | Mass density, kg/m3 | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBphase_1 |  | query_thermoml, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBsolvent_1 |  | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBsolvent_3 |  | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBvar_3 | Pressure, kPa | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBvar_4 | Molality, mol/kg | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBvar_5 | Mass fraction | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBvar_18 | Volume fraction | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| GLOBconstr_2 | Temperature, K | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBblocktype_1 |  | query_thermoml | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | ---: | --- |
| Unique Compounds | 2 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| Unique References | 9 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| Unique Properties | 1 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| Unique Measurements | 6 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| Unique Phases | 1 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| Unique Solvents | 2 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| Unique Variables | 6 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| Unique Constraints | 2 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| Unique Block_Types | 1 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| Unique parent blocks | 9 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| Explicit block/subsystem targets | 9 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| Subsystem targets | 0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| Target-matched data points | 2,917 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| **TOTAL** | **2,965** |  |


## 3. DOI & Block References

| DOI | Blocks | Datapoints | System types | Source tools | Source |
| --- | ---: | ---: | --- | --- | --- |
| 10.1016/j.jct.2004.07.019 | 1 | 596 | binary | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1016/j.jct.2007.05.004 | 1 | 39 | binary | query_thermoml, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1021/je034101z | 1 | 401 | binary | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1021/je049691v | 1 | 180 | binary | query_thermoml, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1021/je0600810 | 1 | 9 | binary | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1021/je2003622 | 1 | 16 | binary | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | — | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | 2 | query_thermoml, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | — | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | — | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | 2 | query_thermoml, search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | — | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | — | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | — | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | — | search_blocks | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | --- | ---: | --- |
| 1 | 2 | `resolve_compound_ids` | min_score=80, purpose=Resolve methanol and water t… | 180 | KEEP ←in 277 | 180 | 4.1 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=50, p… | 9 | KEEP ←in 5,885 | 9 | 22.9 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 3 | 5 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=50, p… | 1,356 | KEEP ←in 5,885 | 1295 | 23.1 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 249 | — | — | 0.0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 364 | — | — | 0.2 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 6 | 8 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 1,487 | — | — | 0.2 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 7 | 9 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_8424,… | 1,195 | — | — | 0.2 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 8 | 11 | `inspect_block_table` | block_number=GLOBlit_2825::PROPblock_10, nearest={… | 861 | — | — | 0.9 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 9 | 1 | `query_thermoml` | context=Looking for experimental dens…, instructio… | 24,649 | — | — | 270.4 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10 | 4 | `inspect_block` | block_number=PROPblock_10, doi=10.1016/j.jct.2007.… | 1,360 | — | — | 0.1 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 11 | 7 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 246 | — | — | 0.1 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 12 | 10 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 954 | — | — | 1.9 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 13 | 11 | `list_session_files` |  | 1,681 | — | — | 0.1 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| **TOTAL** | **85** |  |  | **34,591** |  | **1,484** | **324.2** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 22,518 | 1,281 | 23,799 | 1,194 | 8.1 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,134 | 25,229 | 572 | 4.6 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,154 | 26,249 | 530 | 3.8 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 4 | L1-worker | claudeopus46 | 3,767 | 438 | 4,205 | 317 | 3.8 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,728 | 25,823 | 841 | 6.5 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,421 | 26,516 | 757 | 5.1 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 7 | L1-worker | claudeopus46 | 3,767 | 6,443 | 10,210 | 1,629 | 14.8 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 8 | L1-worker | claudeopus46 | 24,095 | 2,379 | 26,474 | 842 | 7.1 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 9 | L1-worker | claudeopus46 | 3,767 | 6,393 | 10,160 | 1,651 | 15.5 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,028 | 28,123 | 2,304 | 15.9 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 11 | L1-worker | claudeopus46 | 24,095 | 4,710 | 28,805 | 655 | 8.0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 12 | L1-worker | claudeopus46 | 24,095 | 5,429 | 29,524 | 825 | 7.0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 13 | L1-worker | claudeopus46 | 24,095 | 7,254 | 31,349 | 872 | 7.2 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 14 | L1-worker | claudeopus46 | 24,095 | 8,785 | 32,880 | 4,376 | 33.4 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 15 | L1-worker | claudeopus46 | 24,095 | 16,676 | 40,771 | 4,270 | 25.7 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 16 | L1-worker | claudeopus46 | 24,095 | 17,975 | 42,070 | 5,399 | 39.1 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 17 | L1-worker | claudeopus46 | 24,062 | 25,573 | 49,635 | 4,252 | 31.3 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 18 | L1-worker | claudeopus46 | 2,106 | 5,638 | 7,744 | 872 | 6.3 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 19 | L1-worker | claudeopus46 | 2,320 | 4,383 | 6,703 | 1,343 | 8.6 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 20 | L1-worker | claudeopus46 | 627 | 4,263 | 4,890 | 1,270 | 10.0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 21 | L1-worker | claudeopus46 | 366 | 1,649 | 2,015 | 646 | 3.9 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 22 | L1-worker | claudeopus46 | 366 | 1,780 | 2,146 | 1,298 | 5.0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 23 | L1-worker | claudeopus46 | 787 | 22,137 | 22,924 | 573 | 7.2 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 24 | L0-main | claudeopus46 | 22,518 | 23,342 | 45,860 | 2,312 | 18.8 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 25 | L0-main | claudeopus46 | 22,518 | 24,141 | 46,659 | 662 | 6.1 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 26 | L0-main | claudeopus46 | 22,518 | 24,915 | 47,433 | 606 | 4.6 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 27 | L0-main | claudeopus46 | 22,518 | 26,599 | 49,117 | 2,433 | 17.0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 28 | L0-main | claudeopus46 | 22,518 | 27,392 | 49,910 | 707 | 5.8 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 29 | L0-main | claudeopus46 | 22,518 | 28,077 | 50,595 | 1,017 | 7.6 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 30 | L0-main | claudeopus46 | 22,518 | 28,136 | 50,654 | 921 | 6.7 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 31 | L0-main | claudeopus46 | 22,518 | 28,872 | 51,390 | 903 | 6.7 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 32 | L0-main | claudeopus46 | 22,518 | 29,605 | 52,123 | 888 | 6.5 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 33 | L0-main | claudeopus46 | 22,518 | 31,739 | 54,257 | 2,937 | 24.0 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 34 | L0-main | claudeopus46 | 22,518 | 33,863 | 56,381 | 4,033 | 33.9 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 35 | L0-main | claudeopus46 | 22,518 | 41,724 | 64,242 | 5,491 | 46.2 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 36 | L0-main | claudeopus46 | 22,518 | 50,094 | 72,612 | 4,559 | 36.2 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 37 | L0-main | claudeopus46 | 2,106 | 6,068 | 8,174 | 154 | 2.6 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 38 | L0-main | claudeopus46 | 366 | 677 | 1,043 | 195 | 2.6 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 39 | L0-main | claudeopus46 | 2,320 | 4,688 | 7,008 | 1,182 | 9.3 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 40 | L0-main | claudeopus46 | 366 | 1,619 | 1,985 | 1,108 | 5.5 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 41 | L0-main | claudeopus46 | 560 | 5,209 | 5,769 | 100 | 2.1 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 42 | L0-main | claudeopus46 | 1,156 | 5,987 | 7,143 | 489 | 5.2 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
| 43 | L0-main | claudeopus46 | 1,918 | 6,418 | 8,336 | 1,153 | 11.7 | At 25 °C, what Redlich-Kister correlation best represents th (analysis_runs/run_2) |
