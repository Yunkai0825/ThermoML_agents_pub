# Reference Stats — query-agent

**Run started:** 2026-09-05 05:59:06
**Wall time (at last flush):** 228.8 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 30,402 | 43,618 | 11,521 | 74,020 | 8,224 | 72.9 | claudeopus46 |
| L1-worker | 16 | 183,137 | 117,058 | 26,204 | 300,195 | 18,762 | 185.4 | claudeopus46 |
| **TOTAL** | **25** | **213,539** | **160,676** | **37,725** | **374,215** | **14,968** | **258.3** | |

**Estimated tokens:** ~93,553 input + ~9,431 output = ~102,984 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 7 | 4 | 20 | 20 | 257 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **4** | **1** | **7** | **4** | **20** | **20** | **257** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_26 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |

#### References (20 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_1096 |  | search_blocks |
| GLOBlit_2114 |  | search_blocks |
| GLOBlit_2516 |  | search_blocks |
| GLOBlit_2824 |  | search_blocks |
| GLOBlit_3044 |  | search_blocks |
| GLOBlit_3653 |  | search_blocks |
| GLOBlit_3928 |  | search_blocks |
| GLOBlit_4128 |  | search_blocks |
| GLOBlit_4155 |  | search_blocks |
| GLOBlit_4172 |  | search_blocks |
| GLOBlit_4346 |  | search_blocks |
| GLOBlit_4416 |  | search_blocks |
| GLOBlit_4425 |  | search_blocks |
| GLOBlit_4564 |  | search_blocks |
| GLOBlit_4631 |  | search_blocks |
| GLOBlit_4711 |  | search_blocks |
| GLOBlit_4841 |  | search_blocks |
| GLOBlit_4915 |  | search_blocks |
| GLOBlit_5013 |  | search_blocks |
| GLOBlit_5085 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |

#### Measurements (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_6 | Mass density, kg/m3 | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_9 | Amount concentration (molarity), mol/dm3 | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_20 | Ratio of amount of solute to mass of solution, mol/kg | search_blocks |

#### Constraints (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_5 | Mass fraction | search_blocks |
| GLOBconstr_8 | Molality, mol/kg | search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 20 |
| Unique Properties | 1 |
| Unique Measurements | 3 |
| Unique Phases | 1 |
| Unique Variables | 7 |
| Unique Constraints | 4 |
| Unique Solvents | 1 |
| Total DOIs | 20 |
| Unique parent blocks | 20 |
| Explicit block/subsystem targets | 20 |
| Subsystem targets | 0 |
| Target-matched data points | 257 |

---

## 3. DOI & Block References

**Unique DOIs:** 20  |  **Parent blocks:** 20  |  **Explicit targets:** 20  |  **Subsystems:** 0  |  **Target-matched datapoints:** 257

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2012.04.003 | 1 | 6 | binary | search_blocks |
| 10.1016/j.fluid.2017.10.034 | 1 | 35 | binary | search_blocks |
| 10.1016/j.jct.2005.03.008 | 1 | 4 | binary | search_blocks |
| 10.1016/j.jct.2007.05.002 | 1 | 30 | binary | search_blocks |
| 10.1016/j.jct.2008.12.011 | 1 | 39 | binary | search_blocks |
| 10.1016/j.jct.2012.05.033 | 1 | 18 | binary | search_blocks |
| 10.1016/j.jct.2013.06.009 | 1 | 8 | binary | search_blocks |
| 10.1016/j.jct.2014.03.001 | 1 | 6 | binary | search_blocks |
| 10.1016/j.jct.2014.04.014 | 1 | 1 | binary | search_blocks |
| 10.1016/j.jct.2014.05.011 | 1 | 2 | binary | search_blocks |
| 10.1016/j.jct.2015.03.020 | 1 | 3 | binary | search_blocks |
| 10.1016/j.jct.2015.06.025 | 1 | 3 | binary | search_blocks |
| 10.1016/j.jct.2015.07.002 | 1 | 12 | binary | search_blocks |
| 10.1016/j.jct.2015.11.028 | 1 | 7 | binary | search_blocks |
| 10.1016/j.jct.2016.02.026 | 1 | 15 | binary | search_blocks |
| 10.1016/j.jct.2016.05.025 | 1 | 6 | binary | search_blocks |
| 10.1016/j.jct.2016.09.040 | 1 | 25 | binary | search_blocks |
| 10.1016/j.jct.2016.12.007 | 1 | 3 | binary | search_blocks |
| 10.1016/j.jct.2017.04.015 | 1 | 9 | binary | search_blocks |
| 10.1016/j.jct.2017.07.037 | 1 | 25 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2012.04.003 | PROPblock_1 | declared | 6 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.10.034 | PROPblock_3 | declared | 35 | binary | — | search_blocks |
| 10.1016/j.jct.2005.03.008 | PROPblock_5 | declared | 4 | binary | — | search_blocks |
| 10.1016/j.jct.2007.05.002 | PROPblock_4 | declared | 30 | binary | — | search_blocks |
| 10.1016/j.jct.2008.12.011 | PROPblock_6 | declared | 39 | binary | — | search_blocks |
| 10.1016/j.jct.2012.05.033 | PROPblock_6 | declared | 18 | binary | — | search_blocks |
| 10.1016/j.jct.2013.06.009 | PROPblock_7 | declared | 8 | binary | — | search_blocks |
| 10.1016/j.jct.2014.03.001 | PROPblock_35 | declared | 6 | binary | — | search_blocks |
| 10.1016/j.jct.2014.04.014 | PROPblock_38 | declared | 1 | binary | — | search_blocks |
| 10.1016/j.jct.2014.05.011 | PROPblock_9 | declared | 2 | binary | — | search_blocks |
| 10.1016/j.jct.2015.03.020 | PROPblock_9 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.jct.2015.06.025 | PROPblock_9 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.jct.2015.07.002 | PROPblock_14 | declared | 12 | binary | — | search_blocks |
| 10.1016/j.jct.2015.11.028 | PROPblock_2 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.jct.2016.02.026 | PROPblock_8 | declared | 15 | binary | — | search_blocks |
| 10.1016/j.jct.2016.05.025 | PROPblock_13 | declared | 6 | binary | — | search_blocks |
| 10.1016/j.jct.2016.09.040 | PROPblock_10 | declared | 25 | binary | — | search_blocks |
| 10.1016/j.jct.2016.12.007 | PROPblock_7 | declared | 3 | binary | — | search_blocks |
| 10.1016/j.jct.2017.04.015 | PROPblock_7 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.jct.2017.07.037 | PROPblock_7 | declared | 25 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve NaCl and wa… | 204 | KEEP ←in 294 | 204 | 3.7 |
| 2 | 3 | `search_blocks` | compound=['GLOBcomp_26', 'GLOBcomp_1'], limit=20, … | 1,163 | KEEP ←in 13,386 | 1145 | 16.2 |
| 3 | 4 | `inspect_block_table` | block_number=GLOBlit_2114::PROPblock_3, purpose=In… | 1,425 | — | — | 0.2 |
| 4 | 1 | `L1_query` | context=User wants density data for s…, id_catalog… | 32,509 | — | — | 165.7 |
| | | **TOTAL (4 tools)** | | **35,301** | | **1,349** | **185.8** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 496 | 12,077 | 1,178 | 7.9 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,091 | 25,186 | 746 | 6.9 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,122 | 26,217 | 554 | 4.2 |
| 4 | L1-worker | claudeopus46 | 3,767 | 461 | 4,228 | 343 | 3.6 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,730 | 25,825 | 805 | 6.7 |
| 6 | L1-worker | claudeopus46 | 3,767 | 13,832 | 17,599 | 1,525 | 14.2 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,214 | 27,309 | 937 | 7.8 |
| 8 | L1-worker | claudeopus46 | 24,095 | 4,981 | 29,076 | 3,118 | 23.2 |
| 9 | L1-worker | claudeopus46 | 24,095 | 14,385 | 38,480 | 5,607 | 36.8 |
| 10 | L1-worker | claudeopus46 | 24,095 | 26,278 | 50,373 | 4,444 | 32.2 |
| 11 | L1-worker | claudeopus46 | 627 | 3,318 | 3,945 | 923 | 7.9 |
| 12 | L1-worker | claudeopus46 | 2,320 | 3,438 | 5,758 | 1,078 | 8.0 |
| 13 | L1-worker | claudeopus46 | 2,106 | 4,650 | 6,756 | 2,259 | 11.4 |
| 14 | L1-worker | claudeopus46 | 366 | 1,334 | 1,700 | 910 | 4.5 |
| 15 | L1-worker | claudeopus46 | 366 | 1,515 | 1,881 | 1,007 | 4.5 |
| 16 | L1-worker | claudeopus46 | 366 | 3,036 | 3,402 | 1,251 | 5.7 |
| 17 | L1-worker | claudeopus46 | 787 | 31,673 | 32,460 | 697 | 7.8 |
| 18 | L0-main | claudeopus46 | 11,581 | 20,703 | 32,284 | 3,078 | 23.4 |
| 19 | L0-main | claudeopus46 | 2,106 | 3,225 | 5,331 | 831 | 6.0 |
| 20 | L0-main | claudeopus46 | 2,320 | 2,897 | 5,217 | 1,032 | 7.4 |
| 21 | L0-main | claudeopus46 | 366 | 1,380 | 1,746 | 1,135 | 5.1 |
| 22 | L0-main | claudeopus46 | 366 | 1,507 | 1,873 | 988 | 4.3 |
| 23 | L0-main | claudeopus46 | 560 | 4,200 | 4,760 | 249 | 3.0 |
| 24 | L0-main | claudeopus46 | 1,156 | 6,996 | 8,152 | 1,521 | 9.6 |
| 25 | L0-main | claudeopus46 | 366 | 2,214 | 2,580 | 1,509 | 6.2 |

