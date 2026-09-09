# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:30:38
**Wall time (at last flush):** 1,044.6 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 38 | 706,817 | 1,680,864 | 87,827 | 2,387,681 | 62,833 | 683.2 | claudeopus46 |
| L1-worker | 57 | 719,783 | 333,899 | 58,134 | 1,053,682 | 18,485 | 465.6 | claudeopus46 |
| **TOTAL** | **95** | **1,426,600** | **2,014,763** | **145,961** | **3,441,363** | **36,224** | **1148.8** | |

**Estimated tokens:** ~860,340 input + ~36,490 output = ~896,830 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 6 | 3 | 16 | 16 | 2,184 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 3 | 1 | 5 | 5 | 0 |
| `propose_fitting_plan` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 1 | 1 | 2 | 1 | 5 | 5 | 117 |
| `search_blocks` | 1 | 1 | 2 | 1 | 5 | 5 | 66 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 2 | 1 | 1 | 1 | 2 | 2 | 0 |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 2 | 1 | 1 | 1 | 0 |
| **TOTAL** | **12** | **6** | **16** | **8** | **34** | **34** | **2,367** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | query_thermoml, query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | query_thermoml, query_thermoml_parallel, resolve_compound_ids, search_blocks |

#### References (25 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_220 |  | search_blocks |
| GLOBlit_1483 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_3475 |  | search_blocks |
| GLOBlit_4415 |  | search_blocks |
| GLOBlit_5201 |  | search_blocks |
| GLOBlit_7085 |  | query_thermoml, search_blocks |
| GLOBlit_7629 |  | search_blocks |
| GLOBlit_8050 |  | query_thermoml, search_blocks |
| GLOBlit_10159 |  | search_blocks |
| GLOBlit_10699 |  | query_thermoml, search_blocks |
| GLOBlit_10866 |  | search_blocks |
| GLOBlit_11136 |  | query_thermoml, search_blocks |
| GLOBlit_11459 |  | search_blocks |
| GLOBlit_11504 |  | search_blocks |
| GLOBlit_11792 |  | query_thermoml, search_blocks |
| GLOBlit_272 |  | search_blocks |
| GLOBlit_323 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_455 |  | search_blocks |
| GLOBlit_516 |  | search_blocks |
| GLOBlit_14 |  | search_blocks |
| GLOBlit_107 |  | search_blocks |
| GLOBlit_389 |  | search_blocks |
| GLOBlit_779 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_1136 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml, query_thermoml_parallel, search_blocks |

#### Measurements (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_138 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBmeas_236 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_203 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_212 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |

#### Phases (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBphase_10 |  | search_blocks |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml, search_blocks |
| GLOBvar_15 | Mass ratio of solute to solvent | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_2 |  | search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_22 | Volume fraction | search_blocks |

#### Block_Types (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml |
| GLOBblocktype_2 |  | query_thermoml_parallel |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 25 |
| Unique Properties | 1 |
| Unique Measurements | 10 |
| Unique Phases | 2 |
| Unique Variables | 6 |
| Unique Solvents | 2 |
| Unique Constraints | 3 |
| Unique Block_Types | 2 |
| Total DOIs | 25 |
| Unique parent blocks | 26 |
| Explicit block/subsystem targets | 26 |
| Subsystem targets | 0 |
| Target-matched data points | 2,662 |

---

## 3. DOI & Block References

**Unique DOIs:** 25  |  **Parent blocks:** 26  |  **Explicit targets:** 26  |  **Subsystems:** 0  |  **Target-matched datapoints:** 2,367

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1007/s10765-005-8590-7 | 1 | 42 | unary | search_blocks |
| 10.1007/s10765-010-0862-1 | 1 | 3 | unary | search_blocks |
| 10.1016/j.fluid.2004.11.019 | 2 | 825 | binary, unary | search_blocks |
| 10.1016/j.fluid.2005.05.023 | 1 | 79 | unary | search_blocks |
| 10.1016/j.fluid.2005.10.022 | 1 | 6 | unary | query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2006.05.015 | 1 | 14 | unary | search_blocks |
| 10.1016/j.fluid.2006.11.005 | 1 | 6 | unary | search_blocks |
| 10.1016/j.fluid.2007.04.030 | 1 | 11 | unary | search_blocks |
| 10.1016/j.fluid.2010.01.002 | 1 | 4 | unary | query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2012.07.032 | 1 | 3 | unary | search_blocks |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 565 | binary | search_blocks |
| 10.1016/j.jct.2011.10.009 | 1 | 70 | binary | search_blocks |
| 10.1016/j.jct.2015.06.024 | 1 | 40 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 244 | binary | search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | query_thermoml, search_blocks |
| 10.1021/acs.jced.8b00723 | 1 | 3 | binary | search_blocks |
| 10.1021/je020173z | 1 | 24 | binary | query_thermoml, search_blocks |
| 10.1021/je4003515 | 1 | 23 | binary | search_blocks |
| 10.1021/je600565m | 1 | 18 | binary | query_thermoml, search_blocks |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks |
| 10.1021/je800150h | 1 | 108 | binary | query_thermoml, search_blocks |
| 10.1021/je800942u | 1 | 18 | binary | search_blocks |
| 10.1021/je900064e | 1 | 10 | binary | search_blocks |
| 10.1021/je900743e | 1 | 15 | binary | query_thermoml, search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1007/s10765-005-8590-7 | PROPblock_1 | declared | 42 | unary | — | search_blocks |
| 10.1007/s10765-010-0862-1 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.fluid.2004.11.019 | PROPblock_1 | declared | 15 | unary | — | search_blocks |
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | — | search_blocks |
| 10.1016/j.fluid.2005.05.023 | PROPblock_1 | declared | 79 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.10.022 | PROPblock_2 | declared | 6 | unary | 1 | query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2006.05.015 | PROPblock_1 | declared | 14 | unary | — | search_blocks |
| 10.1016/j.fluid.2006.11.005 | PROPblock_1 | declared | 6 | unary | — | search_blocks |
| 10.1016/j.fluid.2007.04.030 | PROPblock_2 | declared | 11 | unary | — | search_blocks |
| 10.1016/j.fluid.2010.01.002 | PROPblock_18 | declared | 4 | unary | 1 | query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2012.07.032 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | — | search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_2 | declared | 565 | binary | — | search_blocks |
| 10.1016/j.jct.2011.10.009 | PROPblock_3 | declared | 70 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.024 | PROPblock_7 | declared | 40 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_19 | declared | 244 | binary | — | search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | declared | 12 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/acs.jced.8b00723 | PROPblock_12 | declared | 3 | binary | — | search_blocks |
| 10.1021/je020173z | PROPblock_5 | declared | 24 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je4003515 | PROPblock_7 | declared | 23 | binary | — | search_blocks |
| 10.1021/je600565m | PROPblock_6 | declared | 18 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je700300y | PROPblock_7 | declared | 84 | binary | — | search_blocks |
| 10.1021/je800150h | PROPblock_9 | declared | 108 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je800942u | PROPblock_6 | declared | 18 | binary | — | search_blocks |
| 10.1021/je900064e | PROPblock_6 | declared | 10 | binary | — | search_blocks |
| 10.1021/je900743e | PROPblock_3 | declared | 15 | binary | 2 | query_thermoml, search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `resolve_compound_ids` | purpose=Resolve ethanol and water to …, queries=['… | 252 | KEEP ←in 278 | 252 | 4.4 |
| 2 | 3 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,889 | KEEP ←in 10,512 | 1842 | 41.8 |
| 3 | 5 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_10699… | 1,362 | — | — | 0.1 |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_8050,… | 1,541 | — | — | 0.2 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_11136… | 1,542 | — | — | 0.6 |
| 6 | 8 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_11792… | 1,403 | — | — | 0.1 |
| 7 | 9 | `inspect_block_table` | block_number=PROPblock_7, literature=GLOBlit_7085,… | 1,191 | — | — | 0.5 |
| 8 | 1 | `query_thermoml` | instruction=Search for blocks containing …, purpos… | 55,650 | — | — | 226.8 |
| 9 | 4 | `inspect_block` | block_number=PROPblock_9, doi=10.1021/je800150h, p… | 1,359 | — | — | 0.2 |
| 10 | 7 | `propose_fitting_plan` | block_number=PROPblock_9, doi=10.1021/je800150h, p… | 134 | — | — | 0.4 |
| 11 | 11 | `fit_block` | block_number=PROPblock_9, composition_hint=mole_fr… | 247 | — | — | 0.3 |
| 12 | 13 | `fit_block` | block_number=PROPblock_9, doi=10.1021/je800150h, m… | 240 | — | — | 0.1 |
| 13 | 14 | `query_thermoml_parallel` | queries=[{'label': 'pure_water_densit… | 224 | — | — | 0.0 |
| 14 | 15 | `query_thermoml_parallel` | queries=[{'label': 'pure_water_densit… | 253 | — | — | 0.0 |
| 15 | 2 | `search_blocks` | compound=GLOBcomp_2, limit=5, property=GLOBprop_1,… | 705 | KEEP ←in 7,598 | 705 | 13.4 |
| 16 | 3 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_323, … | 258 | — | — | 0.5 |
| 17 | 2 | `search_blocks` | compound=GLOBcomp_1, limit=5, property=GLOBprop_1,… | 707 | KEEP ←in 8,379 | 707 | 20.3 |
| 18 | 4 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_323, … | 335 | — | — | 0.2 |
| 19 | 3 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_779,… | 258 | — | — | 0.0 |
| 20 | 5 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_323, … | 884 | — | — | 0.1 |
| 21 | 4 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_779,… | 333 | — | — | 0.1 |
| 22 | 5 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_779,… | 896 | — | — | 0.1 |
| 23 | 16 | `query_thermoml_parallel` | queries=[{'label': 'pure_water_densit… | 16,836 | — | — | 82.2 |
| 24 | 20 | `fit_block` | block_number=PROPblock_9, doi=10.1021/je800150h, p… | 834 | — | — | 3.3 |
| 25 | 21 | `predict_from_rk` | coeffs=[-141.929, -39.6408, 42.9829,…, mixing_rule… | 183 | — | — | 0.1 |
| 26 | 22 | `predict_from_rk` | coeffs=[-141.929, -39.6408, 42.9829,…, n_points=5,… | 181 | — | — | 0.1 |
| 27 | 23 | `list_session_files` |  | 1,519 | — | — | 0.0 |
| 28 | 24 | `predict_from_rk` | coeffs=[-141.929, -39.6408, 42.9829,…, n_points=5,… | 181 | — | — | 0.1 |
| 29 | 25 | `predict_from_rk` | coeffs=[-141.929, -39.6408, 42.9829,…, n_points=10… | 183 | — | — | 0.1 |
| 30 | 1 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_11136… | 849 | — | — | 0.3 |
| 31 | 2 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_11136… | 1,216 | — | — | 0.2 |
| 32 | 29 | `query_thermoml` | context=PROPblock_9 has 108 rows with…, id_catalog… | 11,812 | — | — | 43.7 |
| | | **TOTAL (32 tools)** | | **105,457** | | **3,506** | **440.3** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | chars=85787>80000 | skipped_by_agent | 85,787 | 85,787 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 405 | 22,923 | 1,135 | 9.6 |
| 2 | L1-worker | claudeopus46 | 24,095 | 974 | 25,069 | 635 | 5.1 |
| 3 | L1-worker | claudeopus46 | 3,767 | 467 | 4,234 | 423 | 4.3 |
| 4 | L1-worker | claudeopus46 | 24,095 | 1,505 | 25,600 | 796 | 6.5 |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,222 | 26,317 | 669 | 5.8 |
| 6 | L1-worker | claudeopus46 | 3,767 | 10,995 | 14,762 | 1,591 | 15.5 |
| 7 | L1-worker | claudeopus46 | 3,767 | 11,297 | 15,064 | 2,247 | 18.4 |
| 8 | L1-worker | claudeopus46 | 24,095 | 4,103 | 28,198 | 2,878 | 15.4 |
| 9 | L1-worker | claudeopus46 | 24,095 | 10,029 | 34,124 | 750 | 7.5 |
| 10 | L1-worker | claudeopus46 | 24,095 | 11,674 | 35,769 | 589 | 7.0 |
| 11 | L1-worker | claudeopus46 | 24,095 | 13,527 | 37,622 | 577 | 5.1 |
| 12 | L1-worker | claudeopus46 | 24,095 | 15,385 | 39,480 | 1,524 | 11.7 |
| 13 | L1-worker | claudeopus46 | 24,095 | 17,081 | 41,176 | 377 | 5.3 |
| 14 | L1-worker | claudeopus46 | 24,095 | 18,528 | 42,623 | 4,951 | 37.3 |
| 15 | L1-worker | claudeopus46 | 24,095 | 29,344 | 53,439 | 5,420 | 37.2 |
| 16 | L1-worker | claudeopus46 | 2,320 | 5,081 | 7,401 | 1,352 | 11.0 |
| 17 | L1-worker | claudeopus46 | 627 | 4,961 | 5,588 | 1,237 | 13.9 |
| 18 | L1-worker | claudeopus46 | 2,106 | 6,176 | 8,282 | 2,804 | 14.2 |
| 19 | L1-worker | claudeopus46 | 366 | 1,789 | 2,155 | 1,297 | 6.6 |
| 20 | L1-worker | claudeopus46 | 366 | 3,581 | 3,947 | 1,611 | 8.0 |
| 21 | L1-worker | claudeopus46 | 787 | 41,739 | 42,526 | 813 | 8.5 |
| 22 | L0-main | claudeopus46 | 22,518 | 31,102 | 53,620 | 1,874 | 17.1 |
| 23 | L0-main | claudeopus46 | 22,518 | 31,891 | 54,409 | 742 | 6.2 |
| 24 | L0-main | claudeopus46 | 22,518 | 32,666 | 55,184 | 554 | 4.5 |
| 25 | L0-main | claudeopus46 | 22,518 | 34,089 | 56,607 | 2,290 | 18.3 |
| 26 | L0-main | claudeopus46 | 22,518 | 34,864 | 57,382 | 1,456 | 11.1 |
| 27 | L0-main | claudeopus46 | 22,518 | 35,648 | 58,166 | 1,078 | 8.3 |
| 28 | L0-main | claudeopus46 | 22,518 | 35,438 | 57,956 | 1,802 | 13.3 |
| 29 | L0-main | claudeopus46 | 22,518 | 36,144 | 58,662 | 1,244 | 9.7 |
| 30 | L0-main | claudeopus46 | 22,518 | 36,813 | 59,331 | 1,401 | 11.8 |
| 31 | L0-main | claudeopus46 | 22,518 | 37,517 | 60,035 | 1,193 | 10.2 |
| 32 | L0-main | claudeopus46 | 22,518 | 37,264 | 59,782 | 1,664 | 13.7 |
| 33 | L0-main | claudeopus46 | 22,518 | 38,129 | 60,647 | 1,378 | 9.0 |
| 34 | L0-main | claudeopus46 | 22,518 | 38,479 | 60,997 | 2,070 | 13.2 |
| 35 | L0-main | claudeopus46 | 22,518 | 39,023 | 61,541 | 1,618 | 9.7 |
| 36 | L0-main | claudeopus46 | 22,518 | 39,541 | 62,059 | 1,776 | 9.3 |
| 37 | L1-worker | claudeopus46 | 24,095 | 1,106 | 25,201 | 671 | 5.8 |
| 38 | L1-worker | claudeopus46 | 24,095 | 1,116 | 25,211 | 674 | 5.7 |
| 39 | L1-worker | claudeopus46 | 24,095 | 1,798 | 25,893 | 565 | 4.5 |
| 40 | L1-worker | claudeopus46 | 24,095 | 1,817 | 25,912 | 597 | 8.4 |
| 41 | L1-worker | claudeopus46 | 3,767 | 7,990 | 11,757 | 1,558 | 12.7 |
| 42 | L1-worker | claudeopus46 | 24,095 | 2,464 | 26,559 | 944 | 8.1 |
| 43 | L1-worker | claudeopus46 | 3,767 | 8,777 | 12,544 | 1,604 | 19.9 |
| 44 | L1-worker | claudeopus46 | 24,095 | 3,133 | 27,228 | 521 | 4.4 |
| 45 | L1-worker | claudeopus46 | 24,095 | 2,500 | 26,595 | 821 | 7.2 |
| 46 | L1-worker | claudeopus46 | 24,095 | 3,759 | 27,854 | 593 | 4.8 |
| 47 | L1-worker | claudeopus46 | 24,095 | 3,160 | 27,255 | 570 | 4.7 |
| 48 | L1-worker | claudeopus46 | 24,095 | 4,933 | 29,028 | 710 | 8.6 |
| 49 | L1-worker | claudeopus46 | 24,095 | 3,832 | 27,927 | 626 | 5.7 |
| 50 | L1-worker | claudeopus46 | 24,095 | 7,771 | 31,866 | 725 | 4.3 |
| 51 | L1-worker | claudeopus46 | 2,106 | 2,093 | 4,199 | 411 | 3.0 |
| 52 | L1-worker | claudeopus46 | 627 | 736 | 1,363 | 567 | 3.6 |
| 53 | L1-worker | claudeopus46 | 2,320 | 856 | 3,176 | 597 | 3.8 |
| 54 | L1-worker | claudeopus46 | 24,095 | 5,081 | 29,176 | 905 | 7.6 |
| 55 | L1-worker | claudeopus46 | 366 | 1,188 | 1,554 | 293 | 2.2 |
| 56 | L1-worker | claudeopus46 | 366 | 1,034 | 1,400 | 360 | 3.0 |
| 57 | L1-worker | claudeopus46 | 24,095 | 8,114 | 32,209 | 988 | 5.2 |
| 58 | L1-worker | claudeopus46 | 787 | 6,810 | 7,597 | 492 | 6.0 |
| 59 | L1-worker | claudeopus46 | 2,106 | 2,346 | 4,452 | 444 | 3.6 |
| 60 | L1-worker | claudeopus46 | 627 | 999 | 1,626 | 615 | 4.4 |
| 61 | L1-worker | claudeopus46 | 2,320 | 1,119 | 3,439 | 649 | 4.7 |
| 62 | L1-worker | claudeopus46 | 366 | 1,221 | 1,587 | 326 | 4.6 |
| 63 | L1-worker | claudeopus46 | 366 | 1,086 | 1,452 | 614 | 3.3 |
| 64 | L1-worker | claudeopus46 | 787 | 7,674 | 8,461 | 523 | 5.9 |
| 65 | L0-main | claudeopus46 | 22,518 | 56,575 | 79,093 | 1,872 | 20.4 |
| 66 | L0-main | claudeopus46 | 22,518 | 57,295 | 79,813 | 2,305 | 17.0 |
| 67 | L0-main | claudeopus46 | 22,518 | 57,974 | 80,492 | 1,390 | 11.4 |
| 68 | L0-main | claudeopus46 | 22,518 | 58,717 | 81,235 | 1,198 | 8.2 |
| 69 | L0-main | claudeopus46 | 22,518 | 60,152 | 82,670 | 1,264 | 11.0 |
| 70 | L0-main | claudeopus46 | 22,518 | 60,821 | 83,339 | 3,678 | 26.8 |
| 71 | L0-main | claudeopus46 | 22,518 | 61,440 | 83,958 | 2,515 | 21.1 |
| 72 | L0-main | claudeopus46 | 22,518 | 63,268 | 85,786 | 4,903 | 35.9 |
| 73 | L0-main | claudeopus46 | 22,518 | 63,940 | 86,458 | 5,155 | 36.3 |
| 74 | L0-main | claudeopus46 | 22,518 | 64,535 | 87,053 | 12,388 | 89.0 |
| 75 | L0-main | claudeopus46 | 22,518 | 81,945 | 104,463 | 1,333 | 12.3 |
| 76 | L0-main | claudeopus46 | 22,518 | 82,805 | 105,323 | 8,744 | 66.8 |
| 77 | L0-main | claudeopus46 | 22,518 | 96,922 | 119,440 | 2,920 | 23.6 |
| 78 | L1-worker | claudeopus46 | 24,095 | 1,821 | 25,916 | 726 | 5.5 |
| 79 | L1-worker | claudeopus46 | 24,095 | 2,981 | 27,076 | 817 | 7.2 |
| 80 | L1-worker | claudeopus46 | 24,095 | 4,592 | 28,687 | 1,514 | 14.9 |
| 81 | L1-worker | claudeopus46 | 2,320 | 1,645 | 3,965 | 647 | 4.3 |
| 82 | L1-worker | claudeopus46 | 2,106 | 3,587 | 5,693 | 612 | 4.8 |
| 83 | L1-worker | claudeopus46 | 627 | 1,525 | 2,152 | 653 | 5.7 |
| 84 | L1-worker | claudeopus46 | 366 | 1,084 | 1,450 | 607 | 3.5 |
| 85 | L1-worker | claudeopus46 | 366 | 1,389 | 1,755 | 485 | 3.4 |
| 86 | L1-worker | claudeopus46 | 787 | 10,304 | 11,091 | 569 | 6.3 |
| 87 | L0-main | claudeopus46 | 22,485 | 107,839 | 130,324 | 462 | 12.6 |
| 88 | L0-main | claudeopus46 | 22,518 | 107,079 | 129,597 | 8,629 | 68.8 |
| 89 | L0-main | claudeopus46 | 2,106 | 12,023 | 14,129 | 389 | 4.0 |
| 90 | L0-main | claudeopus46 | 366 | 912 | 1,278 | 378 | 3.1 |
| 91 | L0-main | claudeopus46 | 2,320 | 11,503 | 13,823 | 1,305 | 12.4 |
| 92 | L0-main | claudeopus46 | 366 | 1,742 | 2,108 | 1,234 | 4.9 |
| 93 | L0-main | claudeopus46 | 560 | 12,591 | 13,151 | 267 | 2.9 |
| 94 | L0-main | claudeopus46 | 1,156 | 14,472 | 15,628 | 1,234 | 9.7 |
| 95 | L0-main | claudeopus46 | 1,918 | 7,301 | 9,219 | 989 | 10.0 |

