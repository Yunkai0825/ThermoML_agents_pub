# Reference Stats — query-agent

**Run started:** 2026-09-05 05:21:52
**Wall time (at last flush):** 644.5 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 10 | 41,983 | 131,753 | 28,473 | 173,736 | 17,373 | 158.4 | claudeopus46 |
| L1-worker | 51 | 725,708 | 513,126 | 73,013 | 1,238,834 | 24,290 | 508.8 | claudeopus46 |
| **TOTAL** | **61** | **767,691** | **644,879** | **101,486** | **1,412,570** | **23,156** | **667.2** | |

**Estimated tokens:** ~353,142 input + ~25,371 output = ~378,513 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 1 | 1 | 2 | 1 | 19 | 20 | 94 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_measurement_ids` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_measurement_ids` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 1 | 1 | 2 | 1 | 10 | 10 | 26 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 1 | 1 | 2 | 1 | 20 | 20 | 120 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **4** | **3** | **6** | **3** | **49** | **50** | **240** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | resolve_compound_ids, search_blocks |

#### References (41 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_8 |  | search_blocks |
| GLOBlit_267 |  | search_blocks |
| GLOBlit_288 |  | search_blocks |
| GLOBlit_349 |  | search_blocks |
| GLOBlit_359 |  | search_blocks |
| GLOBlit_499 |  | search_blocks |
| GLOBlit_1969 |  | search_blocks |
| GLOBlit_2547 |  | search_blocks |
| GLOBlit_2568 |  | search_blocks |
| GLOBlit_2580 |  | search_blocks |
| GLOBlit_2632 |  | search_blocks |
| GLOBlit_2648 |  | search_blocks |
| GLOBlit_2674 |  | search_blocks |
| GLOBlit_2680 |  | search_blocks |
| GLOBlit_2707 |  | search_blocks |
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_2934 |  | search_blocks |
| GLOBlit_2944 |  | search_blocks |
| GLOBlit_3116 |  | search_blocks |
| GLOBlit_3572 |  | search_blocks |
| GLOBlit_3711 |  | search_blocks |
| GLOBlit_3988 |  | search_blocks |
| GLOBlit_4485 |  | search_blocks |
| GLOBlit_4940 |  | search_blocks |
| GLOBlit_3748 |  | search_blocks |
| GLOBlit_4013 |  | search_blocks |
| GLOBlit_4060 |  | search_blocks |
| GLOBlit_4369 |  | search_blocks |
| GLOBlit_5074 |  | search_blocks |
| GLOBlit_5522 |  | search_blocks |
| GLOBlit_6598 |  | search_blocks |
| GLOBlit_6838 |  | search_blocks |
| GLOBlit_6957 |  | search_blocks |
| GLOBlit_7168 |  | search_blocks |
| GLOBlit_7368 |  | search_blocks |
| GLOBlit_7448 |  | search_blocks |
| GLOBlit_7676 |  | search_blocks |
| GLOBlit_7681 |  | search_blocks |
| GLOBlit_8595 |  | search_blocks |
| GLOBlit_8647 |  | search_blocks |
| GLOBlit_9642 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |

#### Measurements (29 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_4 | Viscosity, Pa*s | resolve_measurement_ids, search_blocks |
| GLOBmeas_497 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_644 |  | resolve_measurement_ids |
| GLOBmeas_645 |  | resolve_measurement_ids |
| GLOBmeas_1532 |  | resolve_measurement_ids |
| GLOBmeas_1577 |  | resolve_measurement_ids |
| GLOBmeas_1929 |  | resolve_measurement_ids |
| GLOBmeas_1930 |  | resolve_measurement_ids |
| GLOBmeas_2055 |  | resolve_measurement_ids |
| GLOBmeas_2250 |  | resolve_measurement_ids |
| GLOBmeas_1676 |  | resolve_measurement_ids |
| GLOBmeas_129 |  | resolve_measurement_ids |
| GLOBmeas_693 |  | resolve_measurement_ids |
| GLOBmeas_1673 |  | resolve_measurement_ids |
| GLOBmeas_1345 |  | resolve_measurement_ids |
| GLOBmeas_1620 |  | resolve_measurement_ids |
| GLOBmeas_75 |  | resolve_measurement_ids |
| GLOBmeas_1574 |  | resolve_measurement_ids |
| GLOBmeas_1008 |  | resolve_measurement_ids |
| GLOBmeas_499 |  | resolve_measurement_ids |
| GLOBmeas_1387 |  | resolve_measurement_ids |
| GLOBmeas_1082 |  | resolve_measurement_ids |
| GLOBmeas_51 |  | resolve_measurement_ids |
| GLOBmeas_1376 |  | resolve_measurement_ids |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |

#### Constraints (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 1 |
| Unique References | 41 |
| Unique Properties | 1 |
| Unique Measurements | 29 |
| Unique Phases | 1 |
| Unique Variables | 2 |
| Unique Constraints | 1 |
| Total DOIs | 41 |
| Unique parent blocks | 42 |
| Explicit block/subsystem targets | 42 |
| Subsystem targets | 0 |
| Target-matched data points | 240 |

---

## 3. DOI & Block References

**Unique DOIs:** 41  |  **Parent blocks:** 42  |  **Explicit targets:** 42  |  **Subsystems:** 0  |  **Target-matched datapoints:** 177

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1007/s10765-005-8089-2 | 1 | 23 | unary | search_blocks |
| 10.1016/j.fluid.2005.05.012 | 1 | 3 | unary | search_blocks |
| 10.1016/j.fluid.2005.07.010 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2006.01.008 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2006.01.030 | 2 | 23 | unary | search_blocks |
| 10.1016/j.fluid.2007.03.021 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2016.08.022 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2005.04.019 | 1 | 1 | unary | search_blocks |
| 10.1016/j.jct.2005.06.011 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2005.07.008 | 1 | 1 | unary | search_blocks |
| 10.1016/j.jct.2005.10.022 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2005.12.010 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2006.03.010 | 1 | 2 | unary | search_blocks |
| 10.1016/j.jct.2006.03.018 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2006.06.008 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2008.03.013 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2008.04.006 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2009.06.023 | 1 | 11 | unary | search_blocks |
| 10.1016/j.jct.2012.02.027 | 1 | 1 | unary | search_blocks |
| 10.1016/j.jct.2012.08.024 | 1 | 7 | unary | search_blocks |
| 10.1016/j.jct.2012.10.008 | 1 | 5 | unary | search_blocks |
| 10.1016/j.jct.2013.09.006 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2013.09.044 | 1 | 1 | unary | search_blocks |
| 10.1016/j.jct.2013.11.026 | 1 | 1 | unary | search_blocks |
| 10.1016/j.jct.2015.04.027 | 1 | 5 | unary | search_blocks |
| 10.1016/j.jct.2015.08.036 | 1 | 5 | unary | search_blocks |
| 10.1016/j.jct.2016.12.036 | 1 | 1 | unary | search_blocks |
| 10.1016/j.jct.2017.07.022 | 1 | 7 | unary | search_blocks |
| 10.1016/j.jct.2019.04.023 | 1 | 7 | unary | search_blocks |
| 10.1021/acs.jced.5b00365 | 1 | 7 | unary | search_blocks |
| 10.1021/acs.jced.6b00096 | 1 | 2 | unary | search_blocks |
| 10.1021/acs.jced.6b00563 | 1 | 3 | unary | search_blocks |
| 10.1021/acs.jced.7b00267 | 1 | 9 | unary | search_blocks |
| 10.1021/acs.jced.7b00944 | 1 | 1 | unary | search_blocks |
| 10.1021/acs.jced.8b00086 | 1 | 1 | unary | search_blocks |
| 10.1021/acs.jced.8b00939 | 1 | 1 | unary | search_blocks |
| 10.1021/acs.jced.8b00965 | 1 | 5 | unary | search_blocks |
| 10.1021/je0500633 | 1 | 3 | unary | search_blocks |
| 10.1021/je0501639 | 1 | 3 | unary | search_blocks |
| 10.1021/je200707b | 1 | 5 | unary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1007/s10765-005-8089-2 | PROPblock_1 | declared | 23 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.05.012 | PROPblock_3 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.07.010 | PROPblock_9 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2006.01.008 | PROPblock_11 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2006.01.030 | PROPblock_1 | declared | 20 | unary | — | search_blocks |
| 10.1016/j.fluid.2006.01.030 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.fluid.2007.03.021 | PROPblock_3 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2016.08.022 | PROPblock_6 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2005.04.019 | PROPblock_4 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2005.06.011 | PROPblock_26 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2005.07.008 | PROPblock_3 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2005.10.022 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2005.12.010 | PROPblock_1 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2006.03.010 | PROPblock_7 | declared | 2 | unary | — | search_blocks |
| 10.1016/j.jct.2006.03.018 | PROPblock_6 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2006.06.008 | PROPblock_13 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_3 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2008.03.013 | PROPblock_5 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2008.04.006 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2009.06.023 | PROPblock_1 | declared | 11 | unary | — | search_blocks |
| 10.1016/j.jct.2012.02.027 | PROPblock_11 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2012.08.024 | PROPblock_4 | declared | 7 | unary | — | search_blocks |
| 10.1016/j.jct.2012.10.008 | PROPblock_6 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.jct.2013.09.006 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2013.09.044 | PROPblock_6 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2013.11.026 | PROPblock_17 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2015.04.027 | PROPblock_4 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.jct.2015.08.036 | PROPblock_2 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.jct.2016.12.036 | PROPblock_7 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.jct.2017.07.022 | PROPblock_2 | declared | 7 | unary | — | search_blocks |
| 10.1016/j.jct.2019.04.023 | PROPblock_5 | declared | 7 | unary | — | search_blocks |
| 10.1021/acs.jced.5b00365 | PROPblock_4 | declared | 7 | unary | — | search_blocks |
| 10.1021/acs.jced.6b00096 | PROPblock_2 | declared | 2 | unary | — | search_blocks |
| 10.1021/acs.jced.6b00563 | PROPblock_3 | declared | 3 | unary | — | search_blocks |
| 10.1021/acs.jced.7b00267 | PROPblock_2 | declared | 9 | unary | — | search_blocks |
| 10.1021/acs.jced.7b00944 | PROPblock_6 | declared | 1 | unary | — | search_blocks |
| 10.1021/acs.jced.8b00086 | PROPblock_17 | declared | 1 | unary | — | search_blocks |
| 10.1021/acs.jced.8b00939 | PROPblock_12 | declared | 1 | unary | — | search_blocks |
| 10.1021/acs.jced.8b00965 | PROPblock_4 | declared | 5 | unary | — | search_blocks |
| 10.1021/je0500633 | PROPblock_1 | declared | 3 | unary | — | search_blocks |
| 10.1021/je0501639 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1021/je200707b | PROPblock_5 | declared | 5 | unary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `resolve_compound_ids` | purpose=Find ethanol global ID for vi…, queries=et… | 156 | KEEP ←in 222 | 156 | 4.5 |
| 2 | 3 | `search_blocks` | compound=GLOBcomp_2, limit=20, property=GLOBprop_4… | 1,069 | KEEP ←in 10,929 | 1069 | 15.7 |
| 3 | 4 | `inspect_block_table` | block_number=GLOBlit_288::PROPblock_9, nearest=Tem… | 261 | — | — | 0.0 |
| 4 | 5 | `inspect_block_table` | block_number=GLOBlit_288::PROPblock_9, nearest={'T… | 333 | — | — | 0.3 |
| 5 | 6 | `inspect_block_table` | block_number=GLOBlit_288::PROPblock_9, nearest={'c… | 640 | — | — | 0.3 |
| 6 | 7 | `inspect_block_table` | block_number=GLOBlit_349::PROPblock_11, nearest={'… | 641 | — | — | 0.1 |
| 7 | 8 | `inspect_block_table` | block_number=GLOBlit_8::PROPblock_1, nearest={'col… | 811 | — | — | 0.1 |
| 8 | 9 | `inspect_block_table` | block_number=GLOBlit_267::PROPblock_3, nearest={'c… | 833 | — | — | 0.4 |
| 9 | 10 | `resolve_measurement_ids` | purpose=Find measurement method IDs f…, queries=vi… | 980 | KEEP ←in 625 | 980 | 12.4 |
| 10 | 11 | `resolve_measurement_ids` | limit=20, min_score=50, purpose=Find viscosity mea… | 1,307 | KEEP ←in 1,619 | 1307 | 10.0 |
| 11 | 12 | `search_blocks` | compound=GLOBcomp_2, limit=10, measurement=GLOBmea… | 1,161 | KEEP ←in 5,457 | 1146 | 20.0 |
| 12 | 1 | `L1_query` | context=User wants to know how viscos…, id_catalog… | 49,549 | — | — | 243.6 |
| 13 | 2 | `search_blocks` | compound=GLOBcomp_2, limit=20, measurement=GLOBmea… | 747 | DISCARD ←in 39 | 689 | 8.3 |
| 14 | 4 | `search_blocks` | compound=GLOBcomp_2, limit=20, measurement=GLOBmea… | 896 | DISCARD ←in 39 | 838 | 9.6 |
| 15 | 5 | `search_blocks` | compound=GLOBcomp_2, limit=20, measurement=GLOBmea… | 936 | DISCARD ←in 39 | 878 | 16.8 |
| 16 | 6 | `search_blocks` | compound=GLOBcomp_2, limit=20, measurement=GLOBmea… | 1,060 | KEEP ←in 10,820 | 1045 | 21.1 |
| 17 | 7 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_3116,… | 261 | — | — | 0.0 |
| 18 | 8 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_3116,… | 338 | — | — | 0.1 |
| 19 | 9 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_3116,… | 836 | — | — | 0.1 |
| 20 | 10 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_3748,… | 850 | — | — | 0.2 |
| 21 | 11 | `inspect_block_table` | block_number=PROPblock_6, literature=GLOBlit_4013,… | 647 | — | — | 0.3 |
| 22 | 12 | `search_blocks` | compound=GLOBcomp_2, limit=10, measurement=GLOBmea… | 842 | DISCARD ←in 39 | 784 | 10.6 |
| 23 | 2 | `L1_query` | context=Previous query found 20 block…, id_catalog… | 22,800 | — | — | 254.2 |
| | | **TOTAL (23 tools)** | | **87,954** | | **8,892** | **628.7** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 589 | 12,170 | 1,283 | 8.1 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,129 | 25,224 | 436 | 4.4 |
| 3 | L1-worker | claudeopus46 | 3,767 | 366 | 4,133 | 277 | 4.1 |
| 4 | L1-worker | claudeopus46 | 24,095 | 1,501 | 25,596 | 756 | 6.6 |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,209 | 26,304 | 618 | 4.7 |
| 6 | L1-worker | claudeopus46 | 3,767 | 11,376 | 15,143 | 1,652 | 14.7 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,243 | 27,338 | 983 | 7.3 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,879 | 27,974 | 595 | 4.5 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,503 | 28,598 | 730 | 5.9 |
| 10 | L1-worker | claudeopus46 | 24,095 | 5,469 | 29,564 | 785 | 6.4 |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,453 | 30,548 | 890 | 6.7 |
| 12 | L1-worker | claudeopus46 | 24,095 | 7,602 | 31,697 | 814 | 7.7 |
| 13 | L1-worker | claudeopus46 | 24,095 | 8,818 | 32,913 | 1,099 | 7.8 |
| 14 | L1-worker | claudeopus46 | 3,767 | 812 | 4,579 | 1,693 | 10.9 |
| 15 | L1-worker | claudeopus46 | 24,095 | 10,163 | 34,258 | 1,001 | 7.2 |
| 16 | L1-worker | claudeopus46 | 3,767 | 1,794 | 5,561 | 1,666 | 9.4 |
| 17 | L1-worker | claudeopus46 | 24,095 | 11,797 | 35,892 | 823 | 7.2 |
| 18 | L1-worker | claudeopus46 | 3,767 | 5,891 | 9,658 | 1,438 | 11.8 |
| 19 | L1-worker | claudeopus46 | 24,062 | 13,010 | 37,072 | 3,894 | 27.6 |
| 20 | L1-worker | claudeopus46 | 24,062 | 16,568 | 40,630 | 4,276 | 30.6 |
| 21 | L1-worker | claudeopus46 | 627 | 6,431 | 7,058 | 1,045 | 9.5 |
| 22 | L1-worker | claudeopus46 | 2,320 | 6,551 | 8,871 | 1,396 | 10.7 |
| 23 | L1-worker | claudeopus46 | 366 | 1,833 | 2,199 | 1,320 | 4.6 |
| 24 | L1-worker | claudeopus46 | 2,106 | 7,801 | 9,907 | 4,334 | 20.0 |
| 25 | L1-worker | claudeopus46 | 366 | 5,111 | 5,477 | 2,623 | 11.3 |
| 26 | L1-worker | claudeopus46 | 787 | 52,885 | 53,672 | 668 | 8.9 |
| 27 | L0-main | claudeopus46 | 11,581 | 32,213 | 43,794 | 4,063 | 28.2 |
| 28 | L1-worker | claudeopus46 | 24,095 | 13,203 | 37,298 | 930 | 6.9 |
| 29 | L1-worker | claudeopus46 | 24,095 | 13,995 | 38,090 | 698 | 5.4 |
| 30 | L1-worker | claudeopus46 | 3,767 | 503 | 4,270 | 1,163 | 8.0 |
| 31 | L1-worker | claudeopus46 | 24,095 | 14,723 | 38,818 | 1,036 | 6.8 |
| 32 | L1-worker | claudeopus46 | 24,095 | 15,543 | 39,638 | 850 | 5.6 |
| 33 | L1-worker | claudeopus46 | 3,767 | 546 | 4,313 | 1,374 | 9.3 |
| 34 | L1-worker | claudeopus46 | 24,095 | 16,519 | 40,614 | 1,594 | 10.9 |
| 35 | L1-worker | claudeopus46 | 3,767 | 500 | 4,267 | 1,383 | 10.2 |
| 36 | L1-worker | claudeopus46 | 24,095 | 17,909 | 42,004 | 1,326 | 9.1 |
| 37 | L1-worker | claudeopus46 | 3,767 | 11,277 | 15,044 | 1,603 | 15.0 |
| 38 | L1-worker | claudeopus46 | 24,095 | 19,367 | 43,462 | 2,323 | 17.0 |
| 39 | L1-worker | claudeopus46 | 24,095 | 20,095 | 44,190 | 648 | 5.0 |
| 40 | L1-worker | claudeopus46 | 24,095 | 20,833 | 44,928 | 587 | 5.3 |
| 41 | L1-worker | claudeopus46 | 24,095 | 21,990 | 46,085 | 1,002 | 7.8 |
| 42 | L1-worker | claudeopus46 | 24,095 | 23,240 | 47,335 | 1,794 | 13.9 |
| 43 | L1-worker | claudeopus46 | 24,095 | 24,296 | 48,391 | 2,024 | 14.4 |
| 44 | L1-worker | claudeopus46 | 3,767 | 555 | 4,322 | 1,478 | 10.2 |
| 45 | L1-worker | claudeopus46 | 24,062 | 14,270 | 38,332 | 4,527 | 29.8 |
| 46 | L1-worker | claudeopus46 | 24,062 | 18,406 | 42,468 | 3,424 | 22.0 |
| 47 | L1-worker | claudeopus46 | 627 | 4,983 | 5,610 | 844 | 6.4 |
| 48 | L1-worker | claudeopus46 | 2,320 | 5,103 | 7,423 | 1,067 | 7.0 |
| 49 | L1-worker | claudeopus46 | 2,106 | 7,395 | 9,501 | 1,693 | 9.8 |
| 50 | L1-worker | claudeopus46 | 366 | 1,255 | 1,621 | 831 | 3.9 |
| 51 | L1-worker | claudeopus46 | 366 | 1,504 | 1,870 | 1,027 | 4.4 |
| 52 | L1-worker | claudeopus46 | 366 | 2,470 | 2,836 | 1,016 | 4.8 |
| 53 | L1-worker | claudeopus46 | 787 | 25,451 | 26,238 | 959 | 9.4 |
| 54 | L0-main | claudeopus46 | 11,581 | 52,902 | 64,483 | 7,683 | 49.4 |
| 55 | L0-main | claudeopus46 | 2,320 | 5,784 | 8,104 | 1,635 | 8.0 |
| 56 | L0-main | claudeopus46 | 2,106 | 6,205 | 8,311 | 1,890 | 11.0 |
| 57 | L0-main | claudeopus46 | 366 | 2,110 | 2,476 | 1,576 | 5.7 |
| 58 | L0-main | claudeopus46 | 366 | 2,439 | 2,805 | 1,881 | 7.0 |
| 59 | L0-main | claudeopus46 | 560 | 9,129 | 9,689 | 962 | 6.5 |
| 60 | L0-main | claudeopus46 | 1,156 | 15,610 | 16,766 | 4,079 | 20.6 |
| 61 | L0-main | claudeopus46 | 366 | 4,772 | 5,138 | 3,421 | 13.9 |

