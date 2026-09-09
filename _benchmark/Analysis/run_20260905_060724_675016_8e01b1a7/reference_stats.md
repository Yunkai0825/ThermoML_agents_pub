# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:07:24
**Wall time (at last flush):** 434.8 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 23 | 369,080 | 663,099 | 28,051 | 1,032,179 | 44,877 | 232.2 | claudeopus46 |
| L1-worker | 19 | 258,823 | 203,021 | 30,341 | 461,844 | 24,307 | 216.7 | claudeopus46 |
| **TOTAL** | **42** | **627,903** | **866,120** | **58,392** | **1,494,023** | **35,571** | **448.9** | |

**Estimated tokens:** ~373,505 input + ~14,598 output = ~388,103 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 6 | 2 | 10 | 10 | 1,361 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 6 | 2 | 10 | 10 | 1,058 |
| `fit_block` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **6** | **2** | **12** | **4** | **20** | **20** | **2,419** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_4 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | query_thermoml, resolve_compound_ids, search_blocks |

#### References (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2432 |  | query_thermoml, search_blocks |
| GLOBlit_2825 |  | query_thermoml, search_blocks |
| GLOBlit_5533 |  | query_thermoml, search_blocks |
| GLOBlit_7085 |  | query_thermoml, search_blocks |
| GLOBlit_8254 |  | query_thermoml, search_blocks |
| GLOBlit_8424 |  | query_thermoml, search_blocks |
| GLOBlit_8869 |  | query_thermoml, search_blocks |
| GLOBlit_8888 |  | query_thermoml, search_blocks |
| GLOBlit_9571 |  | query_thermoml, search_blocks |
| GLOBlit_10866 |  | query_thermoml, search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml, search_blocks |

#### Measurements (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_2 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_170 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_138 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_141 | Mass density, kg/m3 | query_thermoml, search_blocks |
| GLOBmeas_280 | Mass density, kg/m3 | query_thermoml, search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | query_thermoml, search_blocks |
| GLOBsolvent_3 |  | query_thermoml, search_blocks |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks |
| GLOBvar_3 | Pressure, kPa | query_thermoml, search_blocks |
| GLOBvar_4 | Molality, mol/kg | query_thermoml, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml, search_blocks |
| GLOBvar_18 | Volume fraction | query_thermoml, search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks |
| GLOBconstr_2 | Temperature, K | query_thermoml, search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 10 |
| Unique Properties | 1 |
| Unique Measurements | 6 |
| Unique Phases | 1 |
| Unique Solvents | 2 |
| Unique Variables | 6 |
| Unique Constraints | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 10 |
| Unique parent blocks | 10 |
| Explicit block/subsystem targets | 10 |
| Subsystem targets | 0 |
| Target-matched data points | 2,722 |

---

## 3. DOI & Block References

**Unique DOIs:** 10  |  **Parent blocks:** 10  |  **Explicit targets:** 10  |  **Subsystems:** 0  |  **Target-matched datapoints:** 1,361

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2004.07.019 | 1 | 596 | binary | query_thermoml, search_blocks |
| 10.1016/j.jct.2007.05.004 | 1 | 39 | binary | query_thermoml, search_blocks |
| 10.1016/j.jct.2019.05.013 | 1 | 12 | binary | query_thermoml, search_blocks |
| 10.1021/acs.jced.6b01058 | 1 | 12 | binary | query_thermoml, search_blocks |
| 10.1021/je034101z | 1 | 401 | binary | query_thermoml, search_blocks |
| 10.1021/je049691v | 1 | 180 | binary | query_thermoml, search_blocks |
| 10.1021/je0600810 | 1 | 9 | binary | query_thermoml, search_blocks |
| 10.1021/je0601098 | 1 | 12 | binary | query_thermoml, search_blocks |
| 10.1021/je2003622 | 1 | 16 | binary | query_thermoml, search_blocks |
| 10.1021/je700300y | 1 | 84 | binary | query_thermoml, search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2004.07.019 | PROPblock_1 | declared | 596 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_10 | declared | 39 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.jct.2019.05.013 | PROPblock_2 | declared | 12 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/acs.jced.6b01058 | PROPblock_6 | declared | 12 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je034101z | PROPblock_4 | declared | 401 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je049691v | PROPblock_3 | declared | 180 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je0600810 | PROPblock_4 | declared | 9 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je0601098 | PROPblock_18 | declared | 12 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je2003622 | PROPblock_2 | declared | 16 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je700300y | PROPblock_6 | declared | 84 | binary | 2 | query_thermoml, search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve methanol an… | 180 | KEEP ←in 277 | 180 | 3.6 |
| 2 | 4 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_1'], limit=50, p… | 2,297 | KEEP ←in 6,527 | 2221 | 38.6 |
| 3 | 6 | `inspect_block_table` | block_number=PROPblock_10, literature=GLOBlit_2825… | 1,439 | — | — | 0.3 |
| 4 | 7 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_8424,… | 2,486 | — | — | 0.1 |
| 5 | 8 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_10866… | 1,720 | — | — | 0.1 |
| 6 | 1 | `query_thermoml` | instruction=Search for blocks containing …, purpos… | 80,831 | — | — | 203.0 |
| 7 | 4 | `inspect_block` | block_number=PROPblock_10, doi=10.1016/j.jct.2007.… | 1,360 | — | — | 0.1 |
| 8 | 8 | `fit_block` | block_number=PROPblock_10, doi=10.1016/j.jct.2007.… | 285 | — | — | 0.0 |
| 9 | 12 | `fit_block` | block_number=PROPblock_10, doi=10.1016/j.jct.2007.… | 246 | — | — | 0.1 |
| 10 | 13 | `fit_block` | block_number=PROPblock_10, composition_hint=mole_f… | 871 | — | — | 1.6 |
| | | **TOTAL (10 tools)** | | **91,715** | | **2,401** | **247.5** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 408 | 22,926 | 1,172 | 8.6 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,081 | 25,176 | 616 | 5.6 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,099 | 26,194 | 520 | 5.7 |
| 4 | L1-worker | claudeopus46 | 3,767 | 438 | 4,205 | 317 | 3.5 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,670 | 25,765 | 829 | 7.2 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,357 | 26,452 | 659 | 4.8 |
| 7 | L1-worker | claudeopus46 | 3,767 | 7,014 | 10,781 | 1,483 | 14.1 |
| 8 | L1-worker | claudeopus46 | 3,767 | 7,316 | 11,083 | 2,537 | 20.8 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,631 | 28,726 | 3,133 | 18.1 |
| 10 | L1-worker | claudeopus46 | 24,095 | 11,867 | 35,962 | 948 | 8.0 |
| 11 | L1-worker | claudeopus46 | 24,095 | 13,667 | 37,762 | 609 | 5.7 |
| 12 | L1-worker | claudeopus46 | 24,095 | 16,463 | 40,558 | 536 | 6.6 |
| 13 | L1-worker | claudeopus46 | 24,095 | 18,494 | 42,589 | 3,695 | 30.9 |
| 14 | L1-worker | claudeopus46 | 24,095 | 28,923 | 53,018 | 4,267 | 30.6 |
| 15 | L1-worker | claudeopus46 | 627 | 4,023 | 4,650 | 1,007 | 8.4 |
| 16 | L1-worker | claudeopus46 | 2,320 | 4,143 | 6,463 | 1,181 | 8.5 |
| 17 | L1-worker | claudeopus46 | 366 | 1,618 | 1,984 | 1,105 | 4.7 |
| 18 | L1-worker | claudeopus46 | 2,106 | 5,345 | 7,451 | 3,635 | 14.0 |
| 19 | L1-worker | claudeopus46 | 366 | 4,412 | 4,778 | 2,617 | 11.7 |
| 20 | L1-worker | claudeopus46 | 787 | 67,460 | 68,247 | 647 | 7.8 |
| 21 | L0-main | claudeopus46 | 22,518 | 35,755 | 58,273 | 1,534 | 19.3 |
| 22 | L0-main | claudeopus46 | 22,518 | 36,510 | 59,028 | 588 | 5.2 |
| 23 | L0-main | claudeopus46 | 22,518 | 37,210 | 59,728 | 502 | 3.9 |
| 24 | L0-main | claudeopus46 | 22,518 | 38,906 | 61,424 | 1,147 | 10.7 |
| 25 | L0-main | claudeopus46 | 22,518 | 39,624 | 62,142 | 846 | 7.1 |
| 26 | L0-main | claudeopus46 | 22,518 | 40,258 | 62,776 | 738 | 6.3 |
| 27 | L0-main | claudeopus46 | 22,518 | 40,950 | 63,468 | 732 | 6.2 |
| 28 | L0-main | claudeopus46 | 22,518 | 40,667 | 63,185 | 591 | 4.9 |
| 29 | L0-main | claudeopus46 | 22,518 | 41,315 | 63,833 | 810 | 6.0 |
| 30 | L0-main | claudeopus46 | 22,518 | 41,984 | 64,502 | 847 | 5.9 |
| 31 | L0-main | claudeopus46 | 22,518 | 42,708 | 65,226 | 723 | 6.0 |
| 32 | L0-main | claudeopus46 | 22,518 | 42,485 | 65,003 | 838 | 6.9 |
| 33 | L0-main | claudeopus46 | 22,518 | 45,023 | 67,541 | 4,547 | 31.5 |
| 34 | L0-main | claudeopus46 | 22,518 | 52,440 | 74,958 | 4,496 | 33.8 |
| 35 | L0-main | claudeopus46 | 22,518 | 60,776 | 83,294 | 3,808 | 29.4 |
| 36 | L0-main | claudeopus46 | 2,106 | 4,460 | 6,566 | 154 | 2.5 |
| 37 | L0-main | claudeopus46 | 366 | 677 | 1,043 | 137 | 2.3 |
| 38 | L0-main | claudeopus46 | 2,320 | 3,937 | 6,257 | 943 | 6.5 |
| 39 | L0-main | claudeopus46 | 366 | 1,380 | 1,746 | 903 | 4.1 |
| 40 | L0-main | claudeopus46 | 560 | 4,458 | 5,018 | 106 | 3.7 |
| 41 | L0-main | claudeopus46 | 1,156 | 5,236 | 6,392 | 638 | 9.7 |
| 42 | L0-main | claudeopus46 | 1,918 | 5,932 | 7,850 | 1,251 | 11.7 |

