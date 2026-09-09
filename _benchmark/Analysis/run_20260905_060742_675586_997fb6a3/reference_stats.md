# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:07:42
**Wall time (at last flush):** 1,085.2 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 30 | 504,554 | 987,764 | 68,652 | 1,492,318 | 49,743 | 535.8 | claudeopus46 |
| L1-worker | 62 | 755,545 | 289,087 | 71,893 | 1,044,632 | 16,848 | 551.4 | claudeopus46 |
| **TOTAL** | **92** | **1,260,099** | **1,276,851** | **140,545** | **2,536,950** | **27,575** | **1087.2** | |

**Estimated tokens:** ~634,237 input + ~35,136 output = ~669,373 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 3 | 1 | 1 | 3 | 1 | 1 | 13 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 549 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 3 | 2 | 2 | 2 | 0 |
| `search_blocks` | 2 | 1 | 2 | 2 | 2 | 2 | 81 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 1 | 2 | 1 | 1 | 0 |
| `search_blocks` | 2 | 1 | 6 | 2 | 9 | 9 | 1,349 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 2 | 1 | 1 | 1 | 0 |
| **TOTAL** | **18** | **7** | **19** | **14** | **28** | **28** | **1,992** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_18 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_4 |  | query_thermoml, resolve_compound_ids, search_blocks |

#### References (22 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_5688 |  | query_thermoml, search_blocks |
| GLOBlit_1540 |  | search_blocks |
| GLOBlit_2584 |  | search_blocks |
| GLOBlit_2834 |  | query_thermoml, search_blocks |
| GLOBlit_3614 |  | search_blocks |
| GLOBlit_4166 |  | search_blocks |
| GLOBlit_4174 |  | query_thermoml, search_blocks |
| GLOBlit_4340 |  | search_blocks |
| GLOBlit_8676 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9855 |  | search_blocks |
| GLOBlit_11030 |  | search_blocks |
| GLOBlit_4125 |  | query_thermoml, search_blocks |
| GLOBlit_10930 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_2825 |  | query_thermoml, search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_8254 |  | search_blocks |
| GLOBlit_8424 |  | search_blocks |
| GLOBlit_8869 |  | search_blocks |
| GLOBlit_9571 |  | search_blocks |
| GLOBlit_10866 |  | search_blocks |

#### Properties (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_15 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml, search_blocks |

#### Measurements (8 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_25 | Molar enthalpy of solution, kJ/mol | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_147 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_280 | Mass density, kg/m3 | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, search_blocks |

#### Solvents (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_3 |  | search_blocks |
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_4 |  | search_blocks |

#### Variables (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_8 | Solvent: Mole fraction | search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml, search_blocks |
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_18 | Volume fraction | search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | query_thermoml, search_blocks |
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 3 |
| Unique References | 22 |
| Unique Properties | 2 |
| Unique Measurements | 8 |
| Unique Phases | 1 |
| Unique Solvents | 3 |
| Unique Variables | 7 |
| Unique Constraints | 3 |
| Unique Block_Types | 1 |
| Total DOIs | 22 |
| Unique parent blocks | 23 |
| Explicit block/subsystem targets | 23 |
| Subsystem targets | 0 |
| Target-matched data points | 2,115 |

---

## 3. DOI & Block References

**Unique DOIs:** 22  |  **Parent blocks:** 23  |  **Explicit targets:** 23  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,992

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2014.08.026 | 1 | 4 | binary | search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 596 | binary | search_blocks |
| 10.1016/j.jct.2005.07.012 | 1 | 128 | binary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 1 | 39 | binary | query_thermoml, search_blocks |
| 10.1016/j.jct.2007.05.015 | 1 | 40 | binary | query_thermoml, search_blocks |
| 10.1016/j.jct.2012.04.007 | 1 | 55 | binary | search_blocks |
| 10.1016/j.jct.2014.02.021 | 1 | 26 | binary | query_thermoml, search_blocks |
| 10.1016/j.jct.2014.05.003 | 1 | 3 | binary | search_blocks |
| 10.1016/j.jct.2014.05.013 | 1 | 18 | binary | query_thermoml, search_blocks |
| 10.1016/j.jct.2015.03.012 | 1 | 6 | binary | search_blocks |
| 10.1016/j.tca.2006.02.028 | 1 | 13 | ternary | query_thermoml, search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks |
| 10.1021/je034101z | 1 | 401 | binary | search_blocks |
| 10.1021/je049691v | 1 | 180 | binary | search_blocks |
| 10.1021/je050209y | 1 | 11 | binary | search_blocks |
| 10.1021/je0600810 | 1 | 9 | binary | search_blocks |
| 10.1021/je0601098 | 2 | 26 | binary | search_blocks |
| 10.1021/je2003622 | 1 | 16 | binary | search_blocks |
| 10.1021/je300358u | 1 | 60 | binary | search_blocks |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks |
| 10.1021/je700430g | 1 | 55 | binary | search_blocks |
| 10.1021/je700671t | 1 | 210 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2014.08.026 | PROPblock_5 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | — | search_blocks |
| 10.1016/j.jct.2005.07.012 | PROPblock_9 | declared | 128 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.jct.2007.05.015 | PROPblock_18 | declared | 40 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.jct.2012.04.007 | PROPblock_3 | declared | 55 | binary | — | search_blocks |
| 10.1016/j.jct.2014.02.021 | PROPblock_6 | declared | 26 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.jct.2014.05.003 | PROPblock_1 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.jct.2014.05.013 | PROPblock_19 | declared | 18 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.jct.2015.03.012 | PROPblock_2 | declared | 6 | binary | — | search_blocks |
| 10.1016/j.tca.2006.02.028 | PROPblock_4 | declared | 13 | ternary | — | query_thermoml, search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | — | search_blocks |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | — | search_blocks |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | — | search_blocks |
| 10.1021/je050209y | PROPblock_10 | declared | 11 | binary | — | search_blocks |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_30 | declared | 14 | binary | — | search_blocks |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | — | search_blocks |
| 10.1021/je300358u | PROPblock_3 | declared | 60 | binary | — | search_blocks |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | — | search_blocks |
| 10.1021/je700430g | PROPblock_8 | declared | 55 | binary | — | search_blocks |
| 10.1021/je700671t | PROPblock_4 | declared | 210 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'ternary_density',… | 209 | — | — | 0.0 |
| 2 | 2 | `query_thermoml_parallel` | queries=[{'label': 'ternary_density',… | 132 | — | — | 0.0 |
| 3 | 3 | `query_thermoml_parallel` | queries=[{'label': 'ternary_density',… | 132 | — | — | 0.0 |
| 4 | 4 | `query_thermoml_parallel` | queries=[{'label': 'ternary_density',… | 132 | — | — | 0.0 |
| 5 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 279 | KEEP ←in 356 | 279 | 5.4 |
| 6 | 4 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1',…, limit=50,… | 847 | DISCARD ←in 39 | 789 | 15.1 |
| 7 | 5 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1',…, limit=50,… | 764 | DISCARD ←in 39 | 706 | 15.3 |
| 8 | 6 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1',…, limit=20,… | 1,258 | KEEP ←in 2,201 | 1243 | 14.4 |
| 9 | 8 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_5688,… | 1,408 | — | — | 0.1 |
| 10 | 5 | `query_thermoml` | instruction=Search for blocks containing …, purpos… | 5,859 | — | — | 130.7 |
| 11 | 2 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1'], limit=50, … | 1,238 | KEEP ←in 7,027 | 1207 | 20.8 |
| 12 | 4 | `inspect_block_table` | block_number=PROPblock_18, literature=GLOBlit_2834… | 1,567 | — | — | 0.1 |
| 13 | 5 | `inspect_block_table` | block_number=PROPblock_19, literature=GLOBlit_4174… | 1,440 | — | — | 0.1 |
| 14 | 6 | `query_thermoml` | instruction=Search for blocks containing …, purpos… | 24,299 | — | — | 154.7 |
| 15 | 2 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_4'], limit=20, … | 944 | KEEP ←in 4,193 | 944 | 17.2 |
| 16 | 3 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_4125,… | 1,312 | — | — | 0.4 |
| 17 | 7 | `query_thermoml` | instruction=Search for blocks containing …, purpos… | 11,296 | — | — | 111.2 |
| 18 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=20, p… | 1,964 | KEEP ←in 5,885 | 1964 | 49.2 |
| 19 | 3 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 347 | — | — | 0.2 |
| 20 | 4 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 1,487 | — | — | 0.4 |
| 21 | 8 | `query_thermoml` | instruction=Search for binary blocks cont…, purpos… | 12,142 | — | — | 150.2 |
| 22 | 12 | `fit_block_derived` | block_number=PROPblock_18, composition_hint=mole_f… | 991 | — | — | 1.7 |
| 23 | 14 | `fit_block_derived` | block_number=PROPblock_6, composition_hint=mole_fr… | 936 | — | — | 1.7 |
| 24 | 16 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 237 | — | — | 0.1 |
| 25 | 18 | `fit_block_derived` | block_number=PROPblock_10, composition_hint=mole_f… | 954 | — | — | 2.1 |
| | | **TOTAL (25 tools)** | | **72,174** | | **7,132** | **691.1** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 417 | 22,935 | 2,448 | 13.1 |
| 2 | L0-main | claudeopus46 | 22,518 | 921 | 23,439 | 1,741 | 9.5 |
| 3 | L0-main | claudeopus46 | 22,518 | 1,300 | 23,818 | 2,032 | 9.4 |
| 4 | L0-main | claudeopus46 | 22,518 | 1,701 | 24,219 | 1,991 | 9.6 |
| 5 | L0-main | claudeopus46 | 22,518 | 2,088 | 24,606 | 686 | 5.9 |
| 6 | L1-worker | claudeopus46 | 24,095 | 869 | 24,964 | 683 | 5.2 |
| 7 | L1-worker | claudeopus46 | 24,095 | 1,928 | 26,023 | 580 | 7.8 |
| 8 | L1-worker | claudeopus46 | 3,767 | 533 | 4,300 | 431 | 4.5 |
| 9 | L1-worker | claudeopus46 | 24,095 | 1,582 | 25,677 | 961 | 8.0 |
| 10 | L1-worker | claudeopus46 | 24,095 | 2,310 | 26,405 | 686 | 4.7 |
| 11 | L1-worker | claudeopus46 | 3,767 | 570 | 4,337 | 1,284 | 8.3 |
| 12 | L1-worker | claudeopus46 | 24,095 | 3,103 | 27,198 | 852 | 6.6 |
| 13 | L1-worker | claudeopus46 | 3,767 | 489 | 4,256 | 1,153 | 8.6 |
| 14 | L1-worker | claudeopus46 | 24,095 | 4,247 | 28,342 | 859 | 6.1 |
| 15 | L1-worker | claudeopus46 | 3,767 | 2,632 | 6,399 | 1,904 | 14.1 |
| 16 | L1-worker | claudeopus46 | 24,095 | 5,840 | 29,935 | 1,702 | 10.9 |
| 17 | L1-worker | claudeopus46 | 24,095 | 9,497 | 33,592 | 1,001 | 7.4 |
| 18 | L1-worker | claudeopus46 | 24,095 | 11,204 | 35,299 | 1,618 | 12.2 |
| 19 | L1-worker | claudeopus46 | 2,106 | 2,739 | 4,845 | 92 | 2.0 |
| 20 | L1-worker | claudeopus46 | 2,320 | 1,749 | 4,069 | 442 | 4.0 |
| 21 | L1-worker | claudeopus46 | 366 | 869 | 1,235 | 67 | 2.0 |
| 22 | L1-worker | claudeopus46 | 627 | 1,629 | 2,256 | 765 | 4.8 |
| 23 | L1-worker | claudeopus46 | 787 | 4,583 | 5,370 | 591 | 5.5 |
| 24 | L0-main | claudeopus46 | 22,518 | 9,543 | 32,061 | 914 | 20.5 |
| 25 | L1-worker | claudeopus46 | 24,095 | 856 | 24,951 | 787 | 6.6 |
| 26 | L1-worker | claudeopus46 | 24,095 | 1,572 | 25,667 | 678 | 4.9 |
| 27 | L1-worker | claudeopus46 | 3,767 | 7,472 | 11,239 | 1,540 | 14.8 |
| 28 | L1-worker | claudeopus46 | 24,095 | 2,805 | 26,900 | 3,886 | 23.5 |
| 29 | L1-worker | claudeopus46 | 24,095 | 10,152 | 34,247 | 1,262 | 10.5 |
| 30 | L1-worker | claudeopus46 | 24,095 | 12,070 | 36,165 | 551 | 6.1 |
| 31 | L1-worker | claudeopus46 | 24,095 | 13,840 | 37,935 | 4,702 | 35.3 |
| 32 | L1-worker | claudeopus46 | 24,095 | 21,982 | 46,077 | 3,514 | 28.1 |
| 33 | L1-worker | claudeopus46 | 2,106 | 3,759 | 5,865 | 955 | 5.8 |
| 34 | L1-worker | claudeopus46 | 2,320 | 2,782 | 5,102 | 944 | 6.1 |
| 35 | L1-worker | claudeopus46 | 627 | 2,662 | 3,289 | 1,198 | 7.3 |
| 36 | L1-worker | claudeopus46 | 366 | 1,732 | 2,098 | 729 | 4.0 |
| 37 | L1-worker | claudeopus46 | 366 | 1,381 | 1,747 | 899 | 4.1 |
| 38 | L1-worker | claudeopus46 | 787 | 19,061 | 19,848 | 732 | 7.4 |
| 39 | L0-main | claudeopus46 | 22,518 | 27,314 | 49,832 | 787 | 7.8 |
| 40 | L1-worker | claudeopus46 | 24,095 | 847 | 24,942 | 835 | 5.7 |
| 41 | L1-worker | claudeopus46 | 24,095 | 1,559 | 25,654 | 699 | 4.7 |
| 42 | L1-worker | claudeopus46 | 3,767 | 4,672 | 8,439 | 1,484 | 11.3 |
| 43 | L1-worker | claudeopus46 | 24,095 | 2,458 | 26,553 | 753 | 10.9 |
| 44 | L1-worker | claudeopus46 | 24,095 | 4,097 | 28,192 | 2,315 | 17.9 |
| 45 | L1-worker | claudeopus46 | 24,095 | 8,412 | 32,507 | 3,654 | 20.8 |
| 46 | L1-worker | claudeopus46 | 24,095 | 14,046 | 38,141 | 1,829 | 10.8 |
| 47 | L1-worker | claudeopus46 | 2,106 | 2,467 | 4,573 | 513 | 3.5 |
| 48 | L1-worker | claudeopus46 | 2,320 | 1,499 | 3,819 | 558 | 4.4 |
| 49 | L1-worker | claudeopus46 | 366 | 1,290 | 1,656 | 501 | 3.6 |
| 50 | L1-worker | claudeopus46 | 366 | 995 | 1,361 | 523 | 3.3 |
| 51 | L1-worker | claudeopus46 | 627 | 1,379 | 2,006 | 866 | 9.6 |
| 52 | L1-worker | claudeopus46 | 366 | 1,277 | 1,643 | 853 | 4.6 |
| 53 | L1-worker | claudeopus46 | 787 | 9,912 | 10,699 | 575 | 6.4 |
| 54 | L0-main | claudeopus46 | 22,518 | 36,911 | 59,429 | 968 | 9.1 |
| 55 | L1-worker | claudeopus46 | 24,095 | 861 | 24,956 | 735 | 13.8 |
| 56 | L1-worker | claudeopus46 | 24,095 | 1,527 | 25,622 | 669 | 6.2 |
| 57 | L1-worker | claudeopus46 | 3,767 | 6,338 | 10,105 | 1,429 | 13.7 |
| 58 | L1-worker | claudeopus46 | 3,767 | 6,640 | 10,407 | 2,437 | 21.1 |
| 59 | L1-worker | claudeopus46 | 24,095 | 3,448 | 27,543 | 961 | 8.5 |
| 60 | L1-worker | claudeopus46 | 24,095 | 4,146 | 28,241 | 616 | 5.1 |
| 61 | L1-worker | claudeopus46 | 24,095 | 5,910 | 30,005 | 1,619 | 13.7 |
| 62 | L1-worker | claudeopus46 | 24,095 | 10,364 | 34,459 | 2,945 | 21.0 |
| 63 | L1-worker | claudeopus46 | 24,095 | 15,580 | 39,675 | 1,651 | 10.8 |
| 64 | L1-worker | claudeopus46 | 2,320 | 1,782 | 4,102 | 726 | 3.8 |
| 65 | L1-worker | claudeopus46 | 2,106 | 2,764 | 4,870 | 844 | 5.1 |
| 66 | L1-worker | claudeopus46 | 627 | 1,662 | 2,289 | 795 | 6.5 |
| 67 | L1-worker | claudeopus46 | 366 | 1,163 | 1,529 | 691 | 3.2 |
| 68 | L1-worker | claudeopus46 | 366 | 1,621 | 1,987 | 352 | 2.8 |
| 69 | L1-worker | claudeopus46 | 366 | 1,206 | 1,572 | 782 | 4.3 |
| 70 | L1-worker | claudeopus46 | 787 | 10,666 | 11,453 | 635 | 7.1 |
| 71 | L0-main | claudeopus46 | 22,518 | 47,713 | 70,231 | 2,966 | 23.7 |
| 72 | L0-main | claudeopus46 | 22,518 | 48,826 | 71,344 | 742 | 7.6 |
| 73 | L0-main | claudeopus46 | 22,518 | 49,535 | 72,053 | 728 | 5.9 |
| 74 | L0-main | claudeopus46 | 22,518 | 50,242 | 72,760 | 630 | 12.7 |
| 75 | L0-main | claudeopus46 | 22,518 | 51,402 | 73,920 | 842 | 7.4 |
| 76 | L0-main | claudeopus46 | 22,518 | 52,139 | 74,657 | 699 | 5.6 |
| 77 | L0-main | claudeopus46 | 22,518 | 54,345 | 76,863 | 814 | 7.4 |
| 78 | L0-main | claudeopus46 | 22,518 | 55,066 | 77,584 | 839 | 6.2 |
| 79 | L0-main | claudeopus46 | 22,518 | 55,336 | 77,854 | 1,354 | 10.1 |
| 80 | L0-main | claudeopus46 | 22,518 | 56,097 | 78,615 | 855 | 6.0 |
| 81 | L0-main | claudeopus46 | 22,518 | 58,440 | 80,958 | 12,972 | 95.9 |
| 82 | L0-main | claudeopus46 | 22,518 | 71,941 | 94,459 | 8,677 | 69.3 |
| 83 | L0-main | claudeopus46 | 22,518 | 87,105 | 109,623 | 8,336 | 67.0 |
| 84 | L0-main | claudeopus46 | 22,518 | 102,121 | 124,639 | 7,800 | 62.3 |
| 85 | L0-main | claudeopus46 | 2,106 | 12,964 | 15,070 | 515 | 5.9 |
| 86 | L0-main | claudeopus46 | 366 | 1,038 | 1,404 | 507 | 3.5 |
| 87 | L0-main | claudeopus46 | 2,320 | 12,432 | 14,752 | 1,568 | 14.3 |
| 88 | L0-main | claudeopus46 | 366 | 2,005 | 2,371 | 1,513 | 5.4 |
| 89 | L0-main | claudeopus46 | 560 | 13,812 | 14,372 | 359 | 5.5 |
| 90 | L0-main | claudeopus46 | 1,156 | 16,681 | 17,837 | 1,640 | 11.5 |
| 91 | L0-main | claudeopus46 | 366 | 2,333 | 2,699 | 1,583 | 6.8 |
| 92 | L0-main | claudeopus46 | 1,918 | 5,996 | 7,914 | 1,146 | 10.9 |

