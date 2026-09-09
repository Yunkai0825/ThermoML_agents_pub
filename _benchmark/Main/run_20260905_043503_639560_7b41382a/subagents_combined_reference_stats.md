# Combined Subagent Stats


## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| L0-main | 29 | 504,188 | 1,134,220 | 48,427 | 1,638,408 | 56,496 | 382.3 | claudeopus46 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| L1-worker | 38 | 558,302 | 298,523 | 55,565 | 856,825 | 22,548 | 410.7 | claudeopus46 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| **TOTAL** | **67** | **1,062,490** | **1,432,743** | **103,992** | **2,495,233** | **79,044** | **793.0** |  |  |


### 2a. Raw Tool-Return Counters

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints | Source |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `resolve_compound_ids` | 3 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `search_blocks` | 2 | 1 | 3 | 2 | 3 | 4 | 58 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `query_thermoml` | 2 | 1 | 2 | 2 | 2 | 3 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `query_thermoml` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `query_thermoml` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `search_blocks` | 2 | 1 | 3 | 2 | 3 | 4 | 58 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| `query_thermoml` | 2 | 1 | 3 | 2 | 3 | 4 | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| **TOTAL** | **11** | **5** | **11** | **8** | **11** | **15** | **116** |  |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBcomp_2 |  | query_thermoml, resolve_compound_ids, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| GLOBcomp_5494 |  | resolve_compound_ids | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| GLOBcomp_1 |  | query_thermoml, resolve_compound_ids, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBprop_17 |  | query_thermoml, resolve_property_ids, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBlit_528 |  | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| GLOBlit_2574 |  | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| GLOBlit_6377 |  | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBmeas_13 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| GLOBmeas_169 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| GLOBmeas_12 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBphase_1 |  | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| GLOBvar_3 | Pressure, kPa | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBconstr_2 | Temperature, K | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |


### 2b. Agent-Condensed Data Complexity

| ID | Name | Source tools | Source |
| --- | --- | --- | --- |
| GLOBblocktype_1 |  | query_thermoml | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |


### 2b. Agent-Condensed Data Complexity

| Metric | Count | Source |
| --- | ---: | --- |
| Unique Compounds | 3 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| Unique Properties | 1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| Unique References | 3 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| Unique Measurements | 3 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| Unique Phases | 1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| Unique Variables | 3 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| Unique Constraints | 2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| Unique Block_Types | 1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| Unique parent blocks | 4 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| Explicit block/subsystem targets | 4 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| Subsystem targets | 0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| Target-matched data points | 231 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| **TOTAL** | **256** |  |


## 3. DOI & Block References

| DOI | Blocks | Datapoints | System types | Source tools | Source |
| --- | ---: | ---: | --- | --- | --- |
| 10.1016/j.fluid.2007.06.007 | 2 | 30 | binary | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 10.1016/j.jct.2005.06.018 | 1 | 27 | binary | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 10.1016/j.tca.2017.05.023 | 1 | 1 | binary | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |


## 3. DOI & Block References

| DOI | Block | Target | Datapoints | System | nComp | Source tools | Source |
| --- | --- | --- | ---: | --- | ---: | --- | --- |
| 10.1016/j.fluid.2007.06.007 | PROPblock_1 | declared | 15 | binary | 2 | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 10.1016/j.fluid.2007.06.007 | PROPblock_2 | declared | 15 | binary | 2 | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 10.1016/j.jct.2005.06.018 | PROPblock_4 | declared | 27 | binary | 2 | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 10.1016/j.tca.2017.05.023 | PROPblock_1 | declared | 1 | binary | 2 | query_thermoml, search_blocks | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |


## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) | Source |
| ---: | ---: | --- | --- | ---: | --- | --- | ---: | --- |
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve ethanol and… | 291 | KEEP ←in 351 | 291 | 6.2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 2 | 3 | `resolve_property_ids` | limit=5, min_score=70, purpose=Confirm global ID f… | 396 | KEEP ←in 269 | 396 | 6.2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 3 | 5 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 744 | KEEP ←in 7,304 | 744 | 21.4 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_2574,… | 1,436 | — | — | 0.1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_528, … | 1,588 | — | — | 0.1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 6 | 8 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_528, … | 1,529 | — | — | 0.1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 7 | 1 | `query_thermoml` | instruction=Search for blocks containing …, purpos… | 34,443 | — | — | 206.9 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 8 | 2 | `query_thermoml` | id_catalog=[{'id': 'GLOBcomp_2', 'type':…, instruc… | 197 | — | — | 0.0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 9 | 3 | `query_thermoml` | id_catalog=[{'global_id': 'GLOBcomp_2', …, instruc… | 233 | — | — | 0.1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 10 | 2 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,120 | KEEP ←in 7,304 | 1090 | 21.2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 11 | 3 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_6377,… | 249 | — | — | 0.1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 12 | 4 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_6377,… | 410 | — | — | 0.1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 13 | 5 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_2574,… | 1,512 | — | — | 0.3 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 14 | 7 | `inspect_block_table` | block_number=GLOBlit_6377::PROPblock_1, purpose=Gr… | 706 | — | — | 0.2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 15 | 8 | `inspect_block_table` | block_number=GLOBlit_528::PROPblock_1, purpose=Gro… | 1,588 | — | — | 0.5 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 16 | 9 | `inspect_block_table` | block_number=GLOBlit_528::PROPblock_2, purpose=Ins… | 1,529 | — | — | 0.3 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 17 | 4 | `query_thermoml` | id_catalog=[{'global_id': 'GLOBcomp_2', …, instruc… | 40,797 | — | — | 180.2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 18 | 7 | `inspect_block` | block_number=PROPblock_4, doi=10.1016/j.jct.2005.0… | 1,584 | — | — | 0.1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 19 | 11 | `fit_block` | block_number=PROPblock_4, doi=10.1016/j.jct.2005.0… | 293 | — | — | 0.7 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 20 | 15 | `fit_block` | block_number=PROPblock_4, doi=10.1016/j.jct.2005.0… | 882 | — | — | 2.1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 21 | 19 | `predict_from_rk` | coeffs=[-1.60102, 1.73493, -3.19748,…, n_points=10… | 171 | — | — | 0.1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| **TOTAL** | **131** |  |  | **91,698** |  | **2,521** | **447.0** |  |


## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) | Source |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | L0-main | claudeopus46 | 22,518 | 1,008 | 23,526 | 958 | 8.0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 2 | L1-worker | claudeopus46 | 24,095 | 974 | 25,069 | 753 | 5.9 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,007 | 26,102 | 619 | 5.2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 4 | L1-worker | claudeopus46 | 3,767 | 510 | 4,277 | 442 | 5.5 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,700 | 25,795 | 872 | 8.0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 6 | L1-worker | claudeopus46 | 3,767 | 420 | 4,187 | 697 | 6.0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,420 | 26,515 | 858 | 6.7 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,166 | 27,261 | 681 | 5.6 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 9 | L1-worker | claudeopus46 | 3,767 | 7,796 | 11,563 | 1,852 | 15.6 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 10 | L1-worker | claudeopus46 | 24,095 | 3,901 | 27,996 | 1,091 | 8.3 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,693 | 29,788 | 843 | 7.3 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 12 | L1-worker | claudeopus46 | 24,095 | 7,643 | 31,738 | 1,358 | 11.4 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 13 | L1-worker | claudeopus46 | 24,095 | 9,523 | 33,618 | 5,177 | 35.0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 14 | L1-worker | claudeopus46 | 24,095 | 18,605 | 42,700 | 4,363 | 29.7 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 15 | L1-worker | claudeopus46 | 24,095 | 25,813 | 49,908 | 3,965 | 26.2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 16 | L1-worker | claudeopus46 | 2,320 | 3,494 | 5,814 | 1,168 | 7.2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 17 | L1-worker | claudeopus46 | 627 | 3,374 | 4,001 | 1,178 | 8.0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 18 | L1-worker | claudeopus46 | 2,106 | 4,589 | 6,695 | 1,795 | 9.5 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 19 | L1-worker | claudeopus46 | 366 | 1,605 | 1,971 | 1,128 | 4.9 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 20 | L1-worker | claudeopus46 | 366 | 2,572 | 2,938 | 1,089 | 5.6 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 21 | L1-worker | claudeopus46 | 787 | 26,697 | 27,484 | 657 | 7.1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 22 | L0-main | claudeopus46 | 22,518 | 23,034 | 45,552 | 3,441 | 26.2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 23 | L0-main | claudeopus46 | 22,518 | 23,731 | 46,249 | 2,099 | 14.5 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 24 | L0-main | claudeopus46 | 22,518 | 24,286 | 46,804 | 1,862 | 12.6 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 25 | L1-worker | claudeopus46 | 24,095 | 1,595 | 25,690 | 972 | 8.3 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 26 | L1-worker | claudeopus46 | 24,095 | 2,332 | 26,427 | 622 | 4.8 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 27 | L1-worker | claudeopus46 | 3,767 | 7,767 | 11,534 | 1,769 | 15.1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 28 | L1-worker | claudeopus46 | 24,095 | 3,412 | 27,507 | 803 | 7.4 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 29 | L1-worker | claudeopus46 | 24,095 | 4,059 | 28,154 | 591 | 4.9 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 30 | L1-worker | claudeopus46 | 24,095 | 4,744 | 28,839 | 2,577 | 19.6 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 31 | L1-worker | claudeopus46 | 24,095 | 6,683 | 30,778 | 2,516 | 20.0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 32 | L1-worker | claudeopus46 | 24,095 | 13,719 | 37,814 | 588 | 6.5 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 33 | L1-worker | claudeopus46 | 24,095 | 14,724 | 38,819 | 605 | 7.2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 34 | L1-worker | claudeopus46 | 24,095 | 16,625 | 40,720 | 414 | 4.7 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 35 | L1-worker | claudeopus46 | 24,095 | 18,473 | 42,568 | 2,981 | 22.1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 36 | L1-worker | claudeopus46 | 24,095 | 24,309 | 48,404 | 3,012 | 22.6 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 37 | L1-worker | claudeopus46 | 2,106 | 4,859 | 6,965 | 1,728 | 8.4 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 38 | L1-worker | claudeopus46 | 627 | 3,023 | 3,650 | 1,292 | 8.4 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 39 | L1-worker | claudeopus46 | 2,320 | 3,143 | 5,463 | 1,322 | 13.7 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 40 | L1-worker | claudeopus46 | 366 | 2,505 | 2,871 | 1,275 | 5.6 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 41 | L1-worker | claudeopus46 | 366 | 1,759 | 2,125 | 1,277 | 5.5 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 42 | L1-worker | claudeopus46 | 787 | 32,290 | 33,077 | 635 | 7.2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 43 | L0-main | claudeopus46 | 22,518 | 48,463 | 70,981 | 1,968 | 17.8 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 44 | L0-main | claudeopus46 | 22,518 | 49,273 | 71,791 | 509 | 5.4 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 45 | L0-main | claudeopus46 | 22,518 | 49,924 | 72,442 | 462 | 4.9 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 46 | L0-main | claudeopus46 | 22,518 | 51,862 | 74,380 | 1,041 | 9.6 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 47 | L0-main | claudeopus46 | 22,518 | 52,532 | 75,050 | 830 | 6.8 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 48 | L0-main | claudeopus46 | 22,518 | 53,170 | 75,688 | 906 | 6.7 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 49 | L0-main | claudeopus46 | 22,518 | 53,950 | 76,468 | 920 | 6.5 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 50 | L0-main | claudeopus46 | 22,518 | 53,663 | 76,181 | 1,043 | 8.0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 51 | L0-main | claudeopus46 | 22,518 | 54,452 | 76,970 | 1,188 | 7.9 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 52 | L0-main | claudeopus46 | 22,518 | 55,196 | 77,714 | 996 | 7.1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 53 | L0-main | claudeopus46 | 22,518 | 55,975 | 78,493 | 907 | 14.5 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 54 | L0-main | claudeopus46 | 22,518 | 57,484 | 80,002 | 999 | 9.2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 55 | L0-main | claudeopus46 | 22,518 | 58,199 | 80,717 | 589 | 9.8 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 56 | L0-main | claudeopus46 | 22,518 | 58,837 | 81,355 | 669 | 4.5 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 57 | L0-main | claudeopus46 | 22,518 | 59,565 | 82,083 | 659 | 6.7 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 58 | L0-main | claudeopus46 | 22,518 | 59,176 | 81,694 | 7,676 | 52.3 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 59 | L0-main | claudeopus46 | 22,518 | 71,253 | 93,771 | 6,848 | 51.6 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 60 | L0-main | claudeopus46 | 22,518 | 82,898 | 105,416 | 6,670 | 49.4 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 61 | L0-main | claudeopus46 | 2,106 | 6,776 | 8,882 | 273 | 3.0 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 62 | L0-main | claudeopus46 | 366 | 796 | 1,162 | 259 | 2.8 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 63 | L0-main | claudeopus46 | 2,320 | 5,669 | 7,989 | 1,255 | 10.5 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 64 | L0-main | claudeopus46 | 366 | 1,692 | 2,058 | 1,210 | 5.2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 65 | L0-main | claudeopus46 | 560 | 6,475 | 7,035 | 185 | 2.5 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 66 | L0-main | claudeopus46 | 1,156 | 8,018 | 9,174 | 826 | 7.2 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
| 67 | L0-main | claudeopus46 | 1,918 | 6,863 | 8,781 | 1,179 | 11.1 | Find and fit excess molar enthalpy (HE) data for the binary  (analysis_runs/run_8) |
