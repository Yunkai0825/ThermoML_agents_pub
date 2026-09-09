# Reference Stats — query-agent

**Run started:** 2026-08-03 11:24:26
**Wall time (at last flush):** 440.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 6 | 22,485 | 109,743 | 17,986 | 132,228 | 22,038 | 103.8 | claudeopus46 |
| L1-worker | 16 | 118,098 | 200,775 | 64,179 | 318,873 | 19,929 | 331.3 | claudeopus46 |
| **TOTAL** | **22** | **140,583** | **310,518** | **82,165** | **451,101** | **20,504** | **435.1** | |

**Estimated tokens:** ~112,775 input + ~20,541 output = ~133,316 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 7 | 3 | 17 | 18 | 1,610 |
| `search_blocks` | 2 | 1 | 5 | 1 | 6 | 6 | 232 |
| `search_blocks` | 2 | 1 | 1 | 2 | 1 | 1 | 14 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **8** | **6** | **13** | **6** | **24** | **25** | **1,856** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_4 |  | resolve_compound_ids, search_blocks |

#### Properties (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_42 |  | resolve_property_ids |
| GLOBprop_44 |  | resolve_property_ids, search_blocks |
| GLOBprop_33 |  | resolve_property_ids |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |

#### References (18 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_385 |  | search_blocks |
| GLOBlit_462 |  | search_blocks |
| GLOBlit_895 |  | search_blocks |
| GLOBlit_1742 |  | search_blocks |
| GLOBlit_2092 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_5533 |  | search_blocks |
| GLOBlit_7085 |  | search_blocks |
| GLOBlit_7629 |  | search_blocks |
| GLOBlit_8155 |  | search_blocks |
| GLOBlit_8254 |  | search_blocks |
| GLOBlit_8424 |  | search_blocks |
| GLOBlit_8869 |  | search_blocks |
| GLOBlit_8888 |  | search_blocks |
| GLOBlit_9571 |  | search_blocks |
| GLOBlit_10866 |  | search_blocks |
| GLOBlit_3697 |  | search_blocks |

#### Measurements (13 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_141 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_1494 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_280 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_2135 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_271 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_53 | Relative permittivity at zero frequency | search_blocks |

#### Phases (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_10 |  | search_blocks |
| GLOBphase_1 |  | search_blocks |
| GLOBphase_3 |  | search_blocks |

#### Variables (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_15 | Mass ratio of solute to solvent | search_blocks |
| GLOBvar_18 | Volume fraction | search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_1 | Pressure, kPa | search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |
| GLOBsolvent_3 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique Properties | 5 |
| Unique References | 18 |
| Unique Measurements | 13 |
| Unique Phases | 3 |
| Unique Variables | 7 |
| Unique Constraints | 3 |
| Unique Solvents | 2 |
| Total DOIs | 18 |
| Unique parent blocks | 25 |
| Explicit block/subsystem targets | 25 |
| Subsystem targets | 0 |
| Target-matched data points | 1,856 |

---

## 3. DOI & Block References

**Unique DOIs:** 18  |  **Parent blocks:** 25  |  **Explicit targets:** 25  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,856

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2006.05.007 | 1 | 45 | binary | search_blocks |
| 10.1016/j.fluid.2006.12.005 | 2 | 10 | binary | search_blocks |
| 10.1016/j.fluid.2010.10.005 | 1 | 34 | binary | search_blocks |
| 10.1016/j.fluid.2015.07.012 | 2 | 164 | binary | search_blocks |
| 10.1016/j.fluid.2017.09.005 | 2 | 144 | binary | search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 596 | binary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 2 | 78 | binary | search_blocks |
| 10.1016/j.jct.2012.08.009 | 1 | 14 | binary | search_blocks |
| 10.1016/j.jct.2019.05.013 | 2 | 24 | binary | search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | search_blocks |
| 10.1021/acs.jced.8b00723 | 1 | 3 | binary | search_blocks |
| 10.1021/je0301500 | 1 | 5 | binary | search_blocks |
| 10.1021/je034101z | 1 | 401 | binary | search_blocks |
| 10.1021/je049691v | 1 | 180 | binary | search_blocks |
| 10.1021/je0600810 | 2 | 18 | binary | search_blocks |
| 10.1021/je0601098 | 1 | 12 | binary | search_blocks |
| 10.1021/je2003622 | 2 | 32 | binary | search_blocks |
| 10.1021/je700300y | 1 | 84 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2006.05.007 | PROPblock_1 | declared | 45 | binary | — | search_blocks |
| 10.1016/j.fluid.2006.12.005 | PROPblock_3 | declared | 8 | binary | — | search_blocks |
| 10.1016/j.fluid.2006.12.005 | PROPblock_4 | declared | 2 | binary | — | search_blocks |
| 10.1016/j.fluid.2010.10.005 | PROPblock_1 | declared | 34 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_1 | declared | 80 | binary | — | search_blocks |
| 10.1016/j.fluid.2015.07.012 | PROPblock_2 | declared | 84 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_1 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.09.005 | PROPblock_2 | declared | 72 | binary | — | search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_9 | declared | 39 | binary | — | search_blocks |
| 10.1016/j.jct.2012.08.009 | PROPblock_17 | declared | 14 | binary | — | search_blocks |
| 10.1016/j.jct.2019.05.013 | PROPblock_2 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.jct.2019.05.013 | PROPblock_3 | declared | 12 | binary | — | search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00723 | PROPblock_10 | declared | 3 | binary | — | search_blocks |
| 10.1021/je0301500 | PROPblock_13 | declared | 5 | binary | — | search_blocks |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | — | search_blocks |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | — | search_blocks |
| 10.1021/je0600810 | PROPblock_3 | declared | 9 | binary | — | search_blocks |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | — | search_blocks |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | — | search_blocks |
| 10.1021/je2003622 | PROPblock_1 | declared | 16 | binary | — | search_blocks |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | — | search_blocks |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve compound ID… | 226 | KEEP | 226 | 4.0 |
| 2 | 2 | `resolve_property_ids` | limit=10, min_score=50, purpose=Resolve property I… | 633 | KEEP | 633 | 8.3 |
| 3 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 1,291 | KEEP | 1190 | 26.9 |
| 4 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 1,239 | KEEP | 1149 | 24.3 |
| 5 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_4'], limit=50, p… | 1,126 | KEEP | 1096 | 19.9 |
| 6 | 1 | `L1_query` | context=Looking for solvent property …, id_catalog… | 270 | — | — | 348.8 |
| | | **TOTAL (6 tools)** | | **4,785** | | **4,294** | **432.2** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 9,605 | 965 | 10,570 | 1,874 | 9.9 |
| 2 | L1-worker | claudeopus46 | 20,643 | 1,348 | 21,991 | 1,014 | 6.0 |
| 3 | L1-worker | claudeopus46 | 20,643 | 3,090 | 23,733 | 14,463 | 60.7 |
| 4 | L1-worker | claudeopus46 | 2,065 | 432 | 2,497 | 420 | 3.8 |
| 5 | L1-worker | claudeopus46 | 2,065 | 669 | 2,734 | 1,300 | 8.1 |
| 6 | L1-worker | claudeopus46 | 20,643 | 3,969 | 24,612 | 12,962 | 60.8 |
| 7 | L1-worker | claudeopus46 | 20,643 | 17,766 | 38,409 | 12,184 | 58.8 |
| 8 | L1-worker | claudeopus46 | 2,065 | 11,981 | 14,046 | 1,508 | 15.8 |
| 9 | L1-worker | claudeopus46 | 2,065 | 8,813 | 10,878 | 1,588 | 15.6 |
| 10 | L1-worker | claudeopus46 | 2,065 | 2,402 | 4,467 | 1,584 | 10.8 |
| 11 | L1-worker | claudeopus46 | 20,643 | 21,648 | 42,291 | 4,205 | 27.9 |
| 12 | L1-worker | claudeopus46 | 1,356 | 4,334 | 5,690 | 862 | 5.2 |
| 13 | L1-worker | claudeopus46 | 536 | 4,214 | 4,750 | 893 | 5.5 |
| 14 | L1-worker | claudeopus46 | 298 | 1,244 | 1,542 | 850 | 3.3 |
| 15 | L1-worker | claudeopus46 | 1,323 | 13,501 | 14,824 | 5,138 | 22.2 |
| 16 | L1-worker | claudeopus46 | 298 | 5,860 | 6,158 | 4,151 | 17.4 |
| 17 | L1-worker | claudeopus46 | 747 | 99,504 | 100,251 | 1,057 | 9.4 |
| 18 | L0-main | claudeopus46 | 9,605 | 89,648 | 99,253 | 5,625 | 39.4 |
| 19 | L0-main | claudeopus46 | 1,356 | 5,230 | 6,586 | 1,077 | 8.6 |
| 20 | L0-main | claudeopus46 | 298 | 1,459 | 1,757 | 1,065 | 4.2 |
| 21 | L0-main | claudeopus46 | 1,323 | 7,419 | 8,742 | 4,354 | 24.2 |
| 22 | L0-main | claudeopus46 | 298 | 5,022 | 5,320 | 3,991 | 17.5 |

