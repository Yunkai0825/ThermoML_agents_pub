# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:07:30
**Wall time (at last flush):** 629.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 36 | 661,814 | 1,318,020 | 52,525 | 1,979,834 | 54,995 | 430.4 | claudeopus46 |
| L1-worker | 54 | 606,842 | 194,990 | 48,592 | 801,832 | 14,848 | 368.9 | claudeopus46 |
| **TOTAL** | **90** | **1,268,656** | **1,513,010** | **101,117** | **2,781,666** | **30,907** | **799.3** | |

**Estimated tokens:** ~695,416 input + ~25,279 output = ~720,695 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 2 | 3 | 3 | 247 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 9 | 3 | 4 | 12 | 16 | 412 |
| `query_thermoml_parallel` | 2 | 1 | 2 | 2 | 3 | 3 | 225 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 2 | 1 | 2 | 1 | 2 | 2 | 0 |
| **TOTAL** | **12** | **13** | **9** | **9** | **20** | **24** | **884** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_9 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |

#### Properties (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_28 |  | resolve_property_ids |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBprop_27 | Henry's Law constant (mole fraction scale), kPa | search_blocks |
| GLOBprop_29 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks |
| GLOBprop_15 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBprop_69 | Henry's Law constant (amount concentration scale), kPa*dm3/mol | search_blocks |
| GLOBprop_3 | Activity coefficient | search_blocks |
| GLOBprop_55 | Henry's Law constant (molality scale), kPa*kg/mol | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |

#### References (12 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_5679 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8129 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_10721 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_241 |  | search_blocks |
| GLOBlit_766 |  | search_blocks |
| GLOBlit_5893 |  | search_blocks |
| GLOBlit_8267 |  | search_blocks |
| GLOBlit_8381 |  | search_blocks |
| GLOBlit_8511 |  | search_blocks |
| GLOBlit_8608 |  | search_blocks |
| GLOBlit_10006 |  | search_blocks |
| GLOBlit_11774 |  | search_blocks |

#### Measurements (13 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_258 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_203 | Mass density, kg/m3 | query_thermoml_parallel, search_blocks |
| GLOBmeas_813 | Henry's Law constant (mole fraction scale), kPa | search_blocks |
| GLOBmeas_933 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBmeas_922 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks |
| GLOBmeas_144 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_1115 | Henry's Law constant (amount concentration scale), kPa*dm3/mol | search_blocks |
| GLOBmeas_1 | Activity coefficient | search_blocks |
| GLOBmeas_38 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBmeas_22 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_294 | Henry's Law constant (mole fraction scale), kPa | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |

#### Constraints (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_12 | Amount concentration (molarity), mol/dm3 | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_7 |  | search_blocks |
| GLOBsolvent_1 |  | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml_parallel |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique Properties | 10 |
| Unique References | 12 |
| Unique Measurements | 13 |
| Unique Phases | 1 |
| Unique Variables | 3 |
| Unique Constraints | 4 |
| Unique Solvents | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 12 |
| Unique parent blocks | 16 |
| Explicit block/subsystem targets | 16 |
| Subsystem targets | 0 |
| Target-matched data points | 1,131 |

---

## 3. DOI & Block References

**Unique DOIs:** 12  |  **Parent blocks:** 16  |  **Explicit targets:** 16  |  **Subsystems:** 0  |  **Target-matched datapoints:** 412

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2005.02.006 | 1 | 4 | binary | search_blocks |
| 10.1016/j.fluid.2009.12.009 | 2 | 14 | binary | search_blocks |
| 10.1016/j.tca.2006.01.008 | 2 | 44 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.tca.2010.07.017 | 1 | 1 | binary | search_blocks |
| 10.1021/je030102f | 1 | 99 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je034137r | 1 | 5 | binary | search_blocks |
| 10.1021/je0495942 | 2 | 14 | binary | search_blocks |
| 10.1021/je049875+ | 1 | 4 | binary | search_blocks |
| 10.1021/je050082c | 1 | 18 | binary | search_blocks |
| 10.1021/je3010535 | 1 | 8 | binary | search_blocks |
| 10.1021/je7000182 | 2 | 196 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je900711h | 1 | 5 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2005.02.006 | PROPblock_1 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.fluid.2009.12.009 | PROPblock_5 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.fluid.2009.12.009 | PROPblock_6 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.tca.2006.01.008 | PROPblock_7 | declared | 22 | binary | — | search_blocks |
| 10.1016/j.tca.2006.01.008 | PROPblock_8 | declared | 22 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.tca.2010.07.017 | PROPblock_11 | declared | 1 | binary | — | search_blocks |
| 10.1021/je030102f | PROPblock_5 | declared | 99 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je034137r | PROPblock_1 | declared | 5 | binary | — | search_blocks |
| 10.1021/je0495942 | PROPblock_5 | declared | 7 | binary | — | search_blocks |
| 10.1021/je0495942 | PROPblock_6 | declared | 7 | binary | — | search_blocks |
| 10.1021/je049875+ | PROPblock_2 | declared | 4 | binary | — | search_blocks |
| 10.1021/je050082c | PROPblock_2 | declared | 18 | binary | — | search_blocks |
| 10.1021/je3010535 | PROPblock_9 | declared | 8 | binary | — | search_blocks |
| 10.1021/je7000182 | PROPblock_5 | declared | 70 | binary | — | search_blocks |
| 10.1021/je7000182 | PROPblock_6 | declared | 126 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je900711h | PROPblock_1 | declared | 5 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume', '… | 132 | — | — | 0.0 |
| 2 | 1 | `resolve_compound_ids` | purpose=Find compound IDs for acetone…, queries=['… | 199 | KEEP ←in 282 | 199 | 5.1 |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve acetone and… | 226 | KEEP ←in 282 | 226 | 4.6 |
| 4 | 2 | `resolve_property_ids` | purpose=Find property ID for excess m…, queries=['… | 255 | KEEP ←in 227 | 255 | 5.0 |
| 5 | 4 | `search_blocks` | compound=['GLOBcomp_9', 'GLOBcomp_1'], limit=50, p… | 972 | DISCARD ←in 39 | 914 | 9.5 |
| 6 | 4 | `search_blocks` | compound=['GLOBcomp_9', 'GLOBcomp_1'], limit=50, p… | 931 | KEEP ←in 5,742 | 931 | 14.5 |
| 7 | 5 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_5679,… | 1,265 | — | — | 0.2 |
| 8 | 5 | `search_blocks` | compound=['GLOBcomp_9', 'GLOBcomp_1'], limit=50, p… | 859 | DISCARD ←in 39 | 801 | 8.4 |
| 9 | 6 | `search_blocks` | compound=['GLOBcomp_9', 'GLOBcomp_1'], limit=50, p… | 1,074 | KEEP ←in 10,018 | 889 | 15.4 |
| 10 | 2 | `query_thermoml_parallel` | queries=[{'label': 'excess_volume', '… | 31,762 | — | — | 141.9 |
| 11 | 5 | `inspect_block` | block_number=PROPblock_5, doi=10.1021/je030102f, p… | 1,363 | — | — | 0.4 |
| 12 | 9 | `inspect_block` | block_number=PROPblock_6, doi=10.1021/je7000182, p… | 1,361 | — | — | 0.3 |
| 13 | 13 | `fit_block_derived` | block_number=PROPblock_5, composition_hint=mole_fr… | 208 | — | — | 0.1 |
| 14 | 15 | `fit_block_derived` | block_number=PROPblock_5, composition_hint=mole_fr… | 230 | — | — | 0.1 |
| 15 | 17 | `fit_block_derived` | block_number=PROPblock_5, composition_hint=mole_fr… | 944 | — | — | 2.8 |
| 16 | 18 | `fit_block_derived` | block_number=PROPblock_6, composition_hint=mole_fr… | 946 | — | — | 1.7 |
| 17 | 22 | `inspect_block` | block_number=PROPblock_5, doi=10.1021/je030102f, p… | 1,363 | — | — | 0.4 |
| 18 | 24 | `inspect_block` | block_number=PROPblock_6, doi=10.1021/je7000182, p… | 1,361 | — | — | 0.6 |
| 19 | 26 | `query_thermoml_parallel` | queries=[{'label': 'inspect_block5', … | 216 | — | — | 0.1 |
| 20 | 1 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_8129,… | 259 | — | — | 0.1 |
| 21 | 1 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_10721… | 259 | — | — | 0.2 |
| 22 | 2 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_8129,… | 378 | — | — | 0.7 |
| 23 | 2 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_10721… | 371 | — | — | 0.7 |
| 24 | 3 | `inspect_block_table` | block_number=PROPblock_5, literature=GLOBlit_8129,… | 1,240 | — | — | 0.7 |
| 25 | 3 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_10721… | 1,099 | — | — | 0.2 |
| 26 | 28 | `query_thermoml_parallel` | queries=[{'label': 'inspect_PROPblock… | 25,702 | — | — | 49.0 |
| | | **TOTAL (26 tools)** | | **74,975** | | **4,215** | **262.7** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 413 | 22,931 | 1,640 | 11.5 |
| 2 | L0-main | claudeopus46 | 22,518 | 798 | 23,316 | 1,070 | 6.6 |
| 3 | L1-worker | claudeopus46 | 24,095 | 815 | 24,910 | 609 | 4.7 |
| 4 | L1-worker | claudeopus46 | 24,095 | 809 | 24,904 | 557 | 4.9 |
| 5 | L1-worker | claudeopus46 | 3,767 | 434 | 4,201 | 330 | 4.7 |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,844 | 25,939 | 528 | 5.0 |
| 7 | L1-worker | claudeopus46 | 3,767 | 455 | 4,222 | 385 | 3.9 |
| 8 | L1-worker | claudeopus46 | 24,095 | 1,253 | 25,348 | 519 | 4.3 |
| 9 | L1-worker | claudeopus46 | 3,767 | 380 | 4,147 | 361 | 4.2 |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,455 | 25,550 | 834 | 6.5 |
| 11 | L1-worker | claudeopus46 | 24,095 | 1,751 | 25,846 | 854 | 5.9 |
| 12 | L1-worker | claudeopus46 | 24,095 | 2,168 | 26,263 | 643 | 5.5 |
| 13 | L1-worker | claudeopus46 | 24,095 | 2,504 | 26,599 | 695 | 4.8 |
| 14 | L1-worker | claudeopus46 | 3,767 | 573 | 4,340 | 1,385 | 9.0 |
| 15 | L1-worker | claudeopus46 | 3,767 | 6,219 | 9,986 | 1,570 | 14.0 |
| 16 | L1-worker | claudeopus46 | 24,095 | 3,478 | 27,573 | 730 | 5.7 |
| 17 | L1-worker | claudeopus46 | 24,095 | 3,076 | 27,171 | 1,050 | 8.6 |
| 18 | L1-worker | claudeopus46 | 3,767 | 467 | 4,234 | 1,140 | 8.0 |
| 19 | L1-worker | claudeopus46 | 24,095 | 4,705 | 28,800 | 841 | 5.0 |
| 20 | L1-worker | claudeopus46 | 24,095 | 4,799 | 28,894 | 2,008 | 15.1 |
| 21 | L1-worker | claudeopus46 | 3,767 | 10,386 | 14,153 | 1,631 | 13.5 |
| 22 | L1-worker | claudeopus46 | 24,095 | 6,137 | 30,232 | 1,998 | 11.8 |
| 23 | L1-worker | claudeopus46 | 2,106 | 2,609 | 4,715 | 92 | 2.1 |
| 24 | L1-worker | claudeopus46 | 2,320 | 1,679 | 3,999 | 794 | 3.7 |
| 25 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 1.8 |
| 26 | L1-worker | claudeopus46 | 627 | 1,559 | 2,186 | 896 | 4.8 |
| 27 | L1-worker | claudeopus46 | 366 | 1,231 | 1,597 | 782 | 3.2 |
| 28 | L1-worker | claudeopus46 | 787 | 4,916 | 5,703 | 531 | 5.1 |
| 29 | L1-worker | claudeopus46 | 24,095 | 13,275 | 37,370 | 4,902 | 34.8 |
| 30 | L1-worker | claudeopus46 | 24,095 | 20,654 | 44,749 | 2,641 | 20.8 |
| 31 | L1-worker | claudeopus46 | 2,320 | 2,525 | 4,845 | 678 | 4.6 |
| 32 | L1-worker | claudeopus46 | 627 | 2,405 | 3,032 | 959 | 7.6 |
| 33 | L1-worker | claudeopus46 | 2,106 | 3,461 | 5,567 | 1,662 | 8.0 |
| 34 | L1-worker | claudeopus46 | 366 | 1,115 | 1,481 | 643 | 3.7 |
| 35 | L1-worker | claudeopus46 | 366 | 2,439 | 2,805 | 973 | 4.9 |
| 36 | L1-worker | claudeopus46 | 787 | 23,675 | 24,462 | 576 | 6.8 |
| 37 | L0-main | claudeopus46 | 22,518 | 30,998 | 53,516 | 2,235 | 19.3 |
| 38 | L0-main | claudeopus46 | 22,518 | 31,784 | 54,302 | 649 | 6.2 |
| 39 | L0-main | claudeopus46 | 22,518 | 32,467 | 54,985 | 954 | 7.6 |
| 40 | L0-main | claudeopus46 | 22,518 | 34,195 | 56,713 | 1,035 | 10.5 |
| 41 | L0-main | claudeopus46 | 22,518 | 34,937 | 57,455 | 433 | 6.6 |
| 42 | L0-main | claudeopus46 | 22,518 | 35,508 | 58,026 | 625 | 5.4 |
| 43 | L0-main | claudeopus46 | 22,518 | 36,151 | 58,669 | 552 | 5.0 |
| 44 | L0-main | claudeopus46 | 22,518 | 37,259 | 59,777 | 1,501 | 27.9 |
| 45 | L0-main | claudeopus46 | 22,518 | 37,999 | 60,517 | 949 | 8.0 |
| 46 | L0-main | claudeopus46 | 22,518 | 38,724 | 61,242 | 963 | 6.7 |
| 47 | L0-main | claudeopus46 | 22,518 | 39,462 | 61,980 | 829 | 6.3 |
| 48 | L0-main | claudeopus46 | 22,518 | 39,218 | 61,736 | 2,431 | 19.5 |
| 49 | L0-main | claudeopus46 | 22,518 | 40,174 | 62,692 | 1,134 | 9.9 |
| 50 | L0-main | claudeopus46 | 22,518 | 40,441 | 62,959 | 977 | 8.1 |
| 51 | L0-main | claudeopus46 | 22,518 | 41,218 | 63,736 | 956 | 7.1 |
| 52 | L0-main | claudeopus46 | 22,518 | 43,580 | 66,098 | 1,390 | 11.5 |
| 53 | L0-main | claudeopus46 | 22,518 | 46,145 | 68,663 | 4,776 | 34.1 |
| 54 | L0-main | claudeopus46 | 22,518 | 54,323 | 76,841 | 1,107 | 9.5 |
| 55 | L0-main | claudeopus46 | 22,518 | 55,018 | 77,536 | 534 | 3.9 |
| 56 | L0-main | claudeopus46 | 22,518 | 55,633 | 78,151 | 581 | 4.6 |
| 57 | L0-main | claudeopus46 | 22,518 | 57,055 | 79,573 | 660 | 7.1 |
| 58 | L0-main | claudeopus46 | 22,518 | 57,664 | 80,182 | 464 | 3.9 |
| 59 | L0-main | claudeopus46 | 22,518 | 59,331 | 81,849 | 4,793 | 40.3 |
| 60 | L0-main | claudeopus46 | 22,518 | 67,587 | 90,105 | 2,202 | 15.0 |
| 61 | L0-main | claudeopus46 | 22,518 | 68,135 | 90,653 | 3,660 | 22.2 |
| 62 | L0-main | claudeopus46 | 22,518 | 70,083 | 92,601 | 2,753 | 11.6 |
| 63 | L1-worker | claudeopus46 | 24,095 | 1,489 | 25,584 | 768 | 5.7 |
| 64 | L1-worker | claudeopus46 | 24,095 | 1,491 | 25,586 | 690 | 6.1 |
| 65 | L1-worker | claudeopus46 | 24,095 | 2,070 | 26,165 | 610 | 4.5 |
| 66 | L1-worker | claudeopus46 | 24,095 | 2,054 | 26,149 | 605 | 5.1 |
| 67 | L1-worker | claudeopus46 | 24,095 | 2,752 | 26,847 | 846 | 6.2 |
| 68 | L1-worker | claudeopus46 | 24,095 | 2,719 | 26,814 | 891 | 7.0 |
| 69 | L1-worker | claudeopus46 | 24,095 | 4,430 | 28,525 | 1,592 | 10.9 |
| 70 | L1-worker | claudeopus46 | 24,095 | 4,211 | 28,306 | 1,440 | 10.8 |
| 71 | L1-worker | claudeopus46 | 2,106 | 3,333 | 5,439 | 487 | 4.1 |
| 72 | L1-worker | claudeopus46 | 2,320 | 1,723 | 4,043 | 644 | 4.9 |
| 73 | L1-worker | claudeopus46 | 2,106 | 3,183 | 5,289 | 482 | 3.6 |
| 74 | L1-worker | claudeopus46 | 627 | 1,603 | 2,230 | 599 | 5.3 |
| 75 | L1-worker | claudeopus46 | 2,320 | 1,571 | 3,891 | 528 | 4.9 |
| 76 | L1-worker | claudeopus46 | 627 | 1,451 | 2,078 | 638 | 5.4 |
| 77 | L1-worker | claudeopus46 | 366 | 1,264 | 1,630 | 360 | 3.2 |
| 78 | L1-worker | claudeopus46 | 366 | 1,259 | 1,625 | 355 | 3.1 |
| 79 | L1-worker | claudeopus46 | 366 | 1,081 | 1,447 | 609 | 3.7 |
| 80 | L1-worker | claudeopus46 | 366 | 965 | 1,331 | 516 | 3.4 |
| 81 | L1-worker | claudeopus46 | 787 | 10,294 | 11,081 | 494 | 6.8 |
| 82 | L1-worker | claudeopus46 | 787 | 9,927 | 10,714 | 574 | 7.2 |
| 83 | L0-main | claudeopus46 | 22,518 | 92,834 | 115,352 | 5,708 | 49.1 |
| 84 | L0-main | claudeopus46 | 2,106 | 7,087 | 9,193 | 258 | 3.0 |
| 85 | L0-main | claudeopus46 | 366 | 781 | 1,147 | 244 | 2.4 |
| 86 | L0-main | claudeopus46 | 2,320 | 6,559 | 8,879 | 1,191 | 10.8 |
| 87 | L0-main | claudeopus46 | 366 | 1,628 | 1,994 | 1,141 | 7.3 |
| 88 | L0-main | claudeopus46 | 560 | 7,350 | 7,910 | 170 | 2.3 |
| 89 | L0-main | claudeopus46 | 1,156 | 8,796 | 9,952 | 864 | 8.1 |
| 90 | L0-main | claudeopus46 | 1,918 | 6,685 | 8,603 | 1,096 | 11.5 |

