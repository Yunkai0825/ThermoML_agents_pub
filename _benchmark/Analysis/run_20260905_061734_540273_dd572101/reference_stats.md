# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:17:34
**Wall time (at last flush):** 431.6 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 28 | 481,670 | 598,222 | 41,484 | 1,079,892 | 38,567 | 306.9 | claudeopus46 |
| L1-worker | 18 | 231,327 | 108,335 | 20,035 | 339,662 | 18,870 | 143.1 | claudeopus46 |
| **TOTAL** | **46** | **712,997** | **706,557** | **61,519** | **1,419,554** | **30,859** | **450.0** | |

**Estimated tokens:** ~354,888 input + ~15,379 output = ~370,267 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 4 | 4 | 4 | 212 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 3 | 3 | 3 | 3 | 0 |
| `inspect_block` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `propose_fitting_plan` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **6** | **2** | **6** | **7** | **7** | **7** | **212** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | query_thermoml, resolve_compound_ids, search_blocks |

#### References (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_4415 |  | query_thermoml, search_blocks |
| GLOBlit_5201 |  | query_thermoml, search_blocks |
| GLOBlit_8888 |  | query_thermoml, search_blocks |
| GLOBlit_11504 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_8 | Speed of sound, m/s | query_thermoml, search_blocks |

#### Measurements (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_7 | Speed of sound, m/s | query_thermoml, search_blocks |
| GLOBmeas_18 | Speed of sound, m/s | query_thermoml, search_blocks |
| GLOBmeas_15 | Speed of sound, m/s | query_thermoml, search_blocks |
| GLOBmeas_206 | Speed of sound, m/s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, search_blocks |

#### Solvents (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | query_thermoml, search_blocks |
| GLOBsolvent_2 |  | query_thermoml, search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks |
| GLOBvar_4 | Molality, mol/kg | query_thermoml, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks |

#### Constraints (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks |
| GLOBconstr_4 | Frequency, MHz | query_thermoml, search_blocks |
| GLOBconstr_2 | Temperature, K | query_thermoml, search_blocks |
| GLOBconstr_22 | Volume fraction | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 4 |
| Unique Properties | 1 |
| Unique Measurements | 4 |
| Unique Phases | 1 |
| Unique Solvents | 2 |
| Unique Variables | 3 |
| Unique Constraints | 4 |
| Unique Block_Types | 1 |
| Total DOIs | 4 |
| Unique parent blocks | 4 |
| Explicit block/subsystem targets | 4 |
| Subsystem targets | 0 |
| Target-matched data points | 416 |

---

## 3. DOI & Block References

**Unique DOIs:** 4  |  **Parent blocks:** 4  |  **Explicit targets:** 4  |  **Subsystems:** 0  |  **Target-matched datapoints:** 212

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2015.06.024 | 1 | 40 | binary | query_thermoml, search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 152 | binary | query_thermoml, search_blocks |
| 10.1021/je0601098 | 1 | 12 | binary | query_thermoml, search_blocks |
| 10.1021/je900064e | 1 | 8 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2015.06.024 | PROPblock_8 | declared | 40 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_20 | declared | 152 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je0601098 | PROPblock_19 | declared | 12 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je900064e | PROPblock_5 | declared | 8 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml` | id_catalog=[{'id': 'GLOBprop_8', 'type':…, instruc… | 198 | — | — | 0.1 |
| 2 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve ethanol and… | 161 | KEEP ←in 276 | 161 | 5.1 |
| 3 | 4 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 772 | KEEP ←in 7,680 | 757 | 16.4 |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_4415,… | 1,663 | — | — | 0.1 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_20, literature=GLOBlit_5201… | 2,299 | — | — | 0.2 |
| 6 | 8 | `inspect_block_table` | block_number=PROPblock_19, literature=GLOBlit_8888… | 1,319 | — | — | 0.1 |
| 7 | 2 | `query_thermoml` | instruction=Search for blocks containing …, purpos… | 39,298 | — | — | 123.0 |
| 8 | 4 | `fit_block` | block_number=PROPblock_20, doi=10.1016/j.jct.2018.… | 265 | — | — | 0.1 |
| 9 | 7 | `inspect_block` | block_number=PROPblock_20, doi=10.1016/j.jct.2018.… | 143 | — | — | 0.2 |
| 10 | 11 | `propose_fitting_plan` | block_number=PROPblock_20, doi=10.1016/j.jct.2018.… | 134 | — | — | 0.1 |
| 11 | 15 | `fit_block` | block_number=PROPblock_20, doi=10.1016/j.jct.2018.… | 858 | — | — | 1.6 |
| 12 | 16 | `compute_ideal_baseline` | mixing_rule=linear, n_points=101, property_type=sp… | 128 | — | — | 0.1 |
| 13 | 17 | `predict_from_rk` | coeffs=[47.7201, -241.965, 744.598, …, mixing_rule… | 186 | — | — | 0.0 |
| 14 | 18 | `list_session_files` |  | 1,591 | — | — | 0.0 |
| | | **TOTAL (14 tools)** | | **49,015** | | **918** | **147.1** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 379 | 22,897 | 1,178 | 7.7 |
| 2 | L0-main | claudeopus46 | 22,518 | 860 | 23,378 | 744 | 5.3 |
| 3 | L1-worker | claudeopus46 | 24,095 | 946 | 25,041 | 621 | 5.3 |
| 4 | L1-worker | claudeopus46 | 24,095 | 1,987 | 26,082 | 587 | 4.0 |
| 5 | L1-worker | claudeopus46 | 3,767 | 435 | 4,202 | 295 | 3.5 |
| 6 | L1-worker | claudeopus46 | 24,095 | 1,566 | 25,661 | 885 | 6.5 |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,290 | 26,385 | 713 | 5.0 |
| 8 | L1-worker | claudeopus46 | 3,767 | 8,194 | 11,961 | 1,711 | 15.7 |
| 9 | L1-worker | claudeopus46 | 24,095 | 3,013 | 27,108 | 2,614 | 15.5 |
| 10 | L1-worker | claudeopus46 | 24,095 | 8,703 | 32,798 | 890 | 7.8 |
| 11 | L1-worker | claudeopus46 | 24,095 | 10,657 | 34,752 | 570 | 6.4 |
| 12 | L1-worker | claudeopus46 | 24,095 | 13,264 | 37,359 | 567 | 7.9 |
| 13 | L1-worker | claudeopus46 | 24,095 | 14,880 | 38,975 | 2,785 | 20.0 |
| 14 | L1-worker | claudeopus46 | 627 | 2,796 | 3,423 | 1,117 | 7.4 |
| 15 | L1-worker | claudeopus46 | 2,106 | 3,983 | 6,089 | 1,598 | 8.4 |
| 16 | L1-worker | claudeopus46 | 2,320 | 2,916 | 5,236 | 1,314 | 8.9 |
| 17 | L1-worker | claudeopus46 | 366 | 1,528 | 1,894 | 1,104 | 5.2 |
| 18 | L1-worker | claudeopus46 | 366 | 2,375 | 2,741 | 900 | 4.6 |
| 19 | L1-worker | claudeopus46 | 366 | 1,751 | 2,117 | 1,269 | 5.6 |
| 20 | L1-worker | claudeopus46 | 787 | 27,051 | 27,838 | 495 | 5.4 |
| 21 | L0-main | claudeopus46 | 22,518 | 22,850 | 45,368 | 1,882 | 15.1 |
| 22 | L0-main | claudeopus46 | 22,518 | 23,685 | 46,203 | 1,268 | 10.1 |
| 23 | L0-main | claudeopus46 | 22,518 | 24,035 | 46,553 | 631 | 5.9 |
| 24 | L0-main | claudeopus46 | 22,518 | 24,720 | 47,238 | 586 | 5.9 |
| 25 | L0-main | claudeopus46 | 22,518 | 25,393 | 47,911 | 551 | 6.2 |
| 26 | L0-main | claudeopus46 | 22,518 | 25,175 | 47,693 | 1,220 | 8.5 |
| 27 | L0-main | claudeopus46 | 22,518 | 25,842 | 48,360 | 554 | 4.4 |
| 28 | L0-main | claudeopus46 | 22,518 | 26,509 | 49,027 | 676 | 6.9 |
| 29 | L0-main | claudeopus46 | 22,518 | 27,300 | 49,818 | 630 | 4.7 |
| 30 | L0-main | claudeopus46 | 22,518 | 26,771 | 49,289 | 1,543 | 10.7 |
| 31 | L0-main | claudeopus46 | 22,518 | 27,464 | 49,982 | 906 | 7.3 |
| 32 | L0-main | claudeopus46 | 22,518 | 28,103 | 50,621 | 1,107 | 8.4 |
| 33 | L0-main | claudeopus46 | 22,518 | 28,801 | 51,319 | 964 | 16.8 |
| 34 | L0-main | claudeopus46 | 22,518 | 30,381 | 52,899 | 1,562 | 13.2 |
| 35 | L0-main | claudeopus46 | 22,518 | 31,030 | 53,548 | 852 | 6.3 |
| 36 | L0-main | claudeopus46 | 22,518 | 31,587 | 54,105 | 2,591 | 22.6 |
| 37 | L0-main | claudeopus46 | 22,518 | 33,574 | 56,092 | 5,184 | 35.8 |
| 38 | L0-main | claudeopus46 | 22,518 | 44,525 | 67,043 | 6,644 | 46.4 |
| 39 | L0-main | claudeopus46 | 22,518 | 56,936 | 79,454 | 6,010 | 21.4 |
| 40 | L0-main | claudeopus46 | 2,106 | 5,870 | 7,976 | 154 | 2.5 |
| 41 | L0-main | claudeopus46 | 366 | 677 | 1,043 | 137 | 2.5 |
| 42 | L0-main | claudeopus46 | 2,320 | 5,376 | 7,696 | 1,115 | 8.0 |
| 43 | L0-main | claudeopus46 | 366 | 1,552 | 1,918 | 1,065 | 4.0 |
| 44 | L0-main | claudeopus46 | 560 | 5,897 | 6,457 | 100 | 2.7 |
| 45 | L0-main | claudeopus46 | 1,156 | 6,766 | 7,922 | 534 | 6.9 |
| 46 | L0-main | claudeopus46 | 1,918 | 6,164 | 8,082 | 1,096 | 10.7 |

