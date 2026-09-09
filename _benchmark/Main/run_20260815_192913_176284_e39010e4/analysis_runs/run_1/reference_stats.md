# Reference Stats — analysis-agent

**Run started:** 2026-08-15 19:29:35
**Wall time (at last flush):** 581.4 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 22 | 324,410 | 410,091 | 30,127 | 734,501 | 33,386 | 215.2 | claudeopus46 |
| L1-worker | 75 | 924,366 | 377,224 | 71,886 | 1,301,590 | 17,354 | 536.5 | claudeopus46 |
| **TOTAL** | **97** | **1,248,776** | **787,315** | **102,013** | **2,036,091** | **20,990** | **751.7** | |

**Estimated tokens:** ~509,022 input + ~25,503 output = ~534,525 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 1 | 2 | 1 | 1 | 12 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 1 | 2 | 1 | 1 | 0 |
| `query_thermoml` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_reference_ids` | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `resolve_reference_ids` | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `search_blocks` | 1 | 1 | 2 | 1 | 20 | 20 | 100 |
| `search_blocks` | 1 | 1 | 2 | 1 | 19 | 20 | 128 |
| `search_blocks` | 1 | 1 | 2 | 0 | 1 | 1 | 1 |
| `search_blocks` | 1 | 1 | 2 | 0 | 1 | 1 | 1 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 1 | 1 | 2 | 0 | 2 | 2 | 0 |
| `resolve_reference_ids` | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 3 | 1 | 3 | 2 | 1 | 4 | 61 |
| `search_blocks` | 1 | 1 | 2 | 1 | 9 | 10 | 59 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 1 | 1 | 2 | 0 | 2 | 2 | 0 |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **16** | **12** | **19** | **9** | **60** | **62** | **362** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_4 |  | query_thermoml, query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_2 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_61 | 1,2-propanediol | search_blocks |

#### Properties (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 |  | query_thermoml, query_thermoml_parallel, resolve_property_ids, search_blocks |
| GLOBprop_40 |  | resolve_property_ids |

#### References (37 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_11337 |  | query_thermoml, query_thermoml_parallel, resolve_reference_ids, search_blocks |
| GLOBlit_8 |  | search_blocks |
| GLOBlit_60 |  | search_blocks |
| GLOBlit_119 |  | search_blocks |
| GLOBlit_129 |  | search_blocks |
| GLOBlit_267 |  | search_blocks |
| GLOBlit_369 |  | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBlit_779 |  | search_blocks |
| GLOBlit_2020 |  | search_blocks |
| GLOBlit_2259 |  | search_blocks |
| GLOBlit_2580 |  | search_blocks |
| GLOBlit_2674 |  | search_blocks |
| GLOBlit_2764 |  | search_blocks |
| GLOBlit_2825 |  | search_blocks |
| GLOBlit_3540 |  | search_blocks |
| GLOBlit_3748 |  | search_blocks |
| GLOBlit_3943 |  | search_blocks |
| GLOBlit_3997 |  | search_blocks |
| GLOBlit_4126 |  | search_blocks |
| GLOBlit_4298 |  | search_blocks |
| GLOBlit_4329 |  | search_blocks |
| GLOBlit_359 |  | search_blocks |
| GLOBlit_559 |  | search_blocks |
| GLOBlit_1969 |  | search_blocks |
| GLOBlit_2568 |  | search_blocks |
| GLOBlit_2632 |  | search_blocks |
| GLOBlit_2648 |  | search_blocks |
| GLOBlit_2680 |  | search_blocks |
| GLOBlit_2707 |  | search_blocks |
| GLOBlit_2934 |  | search_blocks |
| GLOBlit_2944 |  | search_blocks |
| GLOBlit_3116 |  | search_blocks |
| GLOBlit_3224 |  | search_blocks |
| GLOBlit_3711 |  | search_blocks |
| GLOBlit_288 |  | search_blocks |
| GLOBlit_349 |  | search_blocks |
| GLOBlit_499 |  | search_blocks |

#### Measurements (8 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_4 | Viscosity, Pa*s | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_165 | Viscosity, Pa*s | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_271 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_497 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_205 | Viscosity, Pa*s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, query_thermoml_parallel, search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks |
| GLOBvar_1 | Temperature, K | query_thermoml, query_thermoml_parallel, search_blocks |
| GLOBvar_3 | Pressure, kPa | query_thermoml, query_thermoml_parallel, search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | query_thermoml, search_blocks |
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks |

#### Block_Types (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml |
| GLOBblocktype_2 |  | query_thermoml, query_thermoml_parallel |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 3 |
| Unique Properties | 2 |
| Unique References | 37 |
| Unique Measurements | 8 |
| Unique Phases | 1 |
| Unique Variables | 3 |
| Unique Constraints | 2 |
| Unique Block_Types | 2 |
| Total DOIs | 37 |
| Unique parent blocks | 48 |
| Explicit block/subsystem targets | 48 |
| Subsystem targets | 0 |
| Target-matched data points | 378 |

---

## 3. DOI & Block References

**Unique DOIs:** 37  |  **Parent blocks:** 48  |  **Explicit targets:** 48  |  **Subsystems:** 0  |  **Target-matched datapoints:** 293

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1007/s10765-005-8089-2 | 2 | 46 | unary | search_blocks |
| 10.1007/s10765-008-0444-7 | 1 | 3 | unary | search_blocks |
| 10.1007/s10765-011-0989-8 | 1 | 7 | unary | search_blocks |
| 10.1007/s10765-011-1100-1 | 1 | 7 | unary | search_blocks |
| 10.1016/j.fluid.2005.05.012 | 2 | 6 | unary | search_blocks |
| 10.1016/j.fluid.2005.07.010 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2006.01.008 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2006.01.030 | 2 | 23 | unary | search_blocks |
| 10.1016/j.fluid.2006.02.023 | 2 | 2 | unary | query_thermoml, query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2007.03.021 | 1 | 1 | unary | search_blocks |
| 10.1016/j.fluid.2007.08.006 | 1 | 3 | unary | search_blocks |
| 10.1016/j.fluid.2010.01.002 | 1 | 4 | unary | search_blocks |
| 10.1016/j.fluid.2016.08.022 | 1 | 3 | unary | search_blocks |
| 10.1016/j.fluid.2017.01.019 | 1 | 6 | unary | search_blocks |
| 10.1016/j.fluid.2018.10.024 | 1 | 5 | unary | search_blocks |
| 10.1016/j.jct.2005.06.011 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2005.07.008 | 1 | 4 | unary | search_blocks |
| 10.1016/j.jct.2005.10.022 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2005.12.010 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2006.03.010 | 2 | 4 | unary | search_blocks |
| 10.1016/j.jct.2006.03.018 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2006.06.008 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2006.10.016 | 2 | 10 | unary | search_blocks |
| 10.1016/j.jct.2007.05.004 | 2 | 6 | unary | search_blocks |
| 10.1016/j.jct.2008.03.013 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2008.04.006 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2009.06.023 | 1 | 11 | unary | search_blocks |
| 10.1016/j.jct.2010.03.022 | 1 | 23 | unary | search_blocks |
| 10.1016/j.jct.2012.01.013 | 1 | 5 | unary | search_blocks |
| 10.1016/j.jct.2012.08.024 | 1 | 7 | unary | search_blocks |
| 10.1016/j.jct.2012.10.008 | 1 | 5 | unary | search_blocks |
| 10.1016/j.jct.2013.07.010 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2013.09.018 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2014.02.022 | 1 | 3 | unary | search_blocks |
| 10.1016/j.jct.2015.01.001 | 1 | 4 | unary | search_blocks |
| 10.1016/j.jct.2015.02.022 | 1 | 4 | unary | search_blocks |
| 10.1021/je800633a | 5 | 62 | binary, ternary, unary | query_thermoml, query_thermoml_parallel, search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1007/s10765-005-8089-2 | PROPblock_1 | declared | 23 | unary | — | search_blocks |
| 10.1007/s10765-005-8089-2 | PROPblock_2 | declared | 23 | unary | — | search_blocks |
| 10.1007/s10765-008-0444-7 | PROPblock_1 | declared | 3 | unary | — | search_blocks |
| 10.1007/s10765-011-0989-8 | PROPblock_5 | declared | 7 | unary | — | search_blocks |
| 10.1007/s10765-011-1100-1 | PROPblock_6 | declared | 7 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.05.012 | PROPblock_1 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.05.012 | PROPblock_3 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.fluid.2005.07.010 | PROPblock_9 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2006.01.008 | PROPblock_11 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2006.01.030 | PROPblock_1 | declared | 20 | unary | — | search_blocks |
| 10.1016/j.fluid.2006.01.030 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.fluid.2006.02.023 | PROPblock_11 | declared | 1 | unary | 1 | query_thermoml, search_blocks |
| 10.1016/j.fluid.2006.02.023 | PROPblock_8 | declared | 1 | unary | 1 | query_thermoml_parallel, search_blocks |
| 10.1016/j.fluid.2007.03.021 | PROPblock_3 | declared | 1 | unary | — | search_blocks |
| 10.1016/j.fluid.2007.08.006 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.fluid.2010.01.002 | PROPblock_10 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.fluid.2016.08.022 | PROPblock_6 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.fluid.2017.01.019 | PROPblock_8 | declared | 6 | unary | — | search_blocks |
| 10.1016/j.fluid.2018.10.024 | PROPblock_8 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.jct.2005.06.011 | PROPblock_26 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2005.07.008 | PROPblock_1 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.jct.2005.10.022 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2005.12.010 | PROPblock_1 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2006.03.010 | PROPblock_4 | declared | 2 | unary | — | search_blocks |
| 10.1016/j.jct.2006.03.010 | PROPblock_7 | declared | 2 | unary | — | search_blocks |
| 10.1016/j.jct.2006.03.018 | PROPblock_6 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2006.06.008 | PROPblock_13 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2006.10.016 | PROPblock_1 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.jct.2006.10.016 | PROPblock_3 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_1 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2007.05.004 | PROPblock_3 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2008.03.013 | PROPblock_5 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2008.04.006 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2009.06.023 | PROPblock_1 | declared | 11 | unary | — | search_blocks |
| 10.1016/j.jct.2010.03.022 | PROPblock_2 | declared | 23 | unary | — | search_blocks |
| 10.1016/j.jct.2012.01.013 | PROPblock_1 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.jct.2012.08.024 | PROPblock_4 | declared | 7 | unary | — | search_blocks |
| 10.1016/j.jct.2012.10.008 | PROPblock_3 | declared | 5 | unary | — | search_blocks |
| 10.1016/j.jct.2013.07.010 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2013.09.018 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2014.02.022 | PROPblock_2 | declared | 3 | unary | — | search_blocks |
| 10.1016/j.jct.2015.01.001 | PROPblock_3 | declared | 4 | unary | — | search_blocks |
| 10.1016/j.jct.2015.02.022 | PROPblock_5 | declared | 4 | unary | — | search_blocks |
| 10.1021/je800633a | PROPblock_13 | declared | 12 | binary | — | search_blocks |
| 10.1021/je800633a | PROPblock_16 | declared | 12 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je800633a | PROPblock_18 | declared | 36 | ternary | — | search_blocks |
| 10.1021/je800633a | PROPblock_2 | declared | 1 | unary | 1 | query_thermoml, search_blocks |
| 10.1021/je800633a | PROPblock_8 | declared | 1 | unary | 1 | query_thermoml_parallel, search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve methanol an… | 214 | KEEP ←in 283 | 214 | 3.9 |
| 2 | 2 | `resolve_property_ids` | limit=5, min_score=80, purpose=Verify property IDs… | 230 | KEEP ←in 299 | 230 | 3.9 |
| 3 | 3 | `search_blocks` | compound=['GLOBcomp_4', 'GLOBcomp_2'], limit=50, p… | 1,198 | KEEP ←in 1,863 | 1182 | 16.1 |
| 4 | 4 | `inspect_block_table` | block_number=PROPblock_16, literature=GLOBlit_1133… | 1,353 | — | — | 0.1 |
| 5 | 1 | `query_thermoml` | instruction=Search for blocks containing …, purpos… | 12,207 | — | — | 78.2 |
| 6 | 4 | `inspect_block` | block_number=PROPblock_16, doi=10.1021/je800633a, … | 1,373 | — | — | 0.3 |
| 7 | 4 | `get_pure_values` | block_number=PROPblock_16, doi=10.1021/je800633a, … | 133 | — | — | 0.1 |
| 8 | 5 | `query_thermoml` | id_catalog=[{'type': 'comp', 'global_id'…, instruc… | 204 | — | — | 0.0 |
| 9 | 3 | `resolve_reference_ids` | limit=5, min_score=50, purpose=Resolve DOI to GLOB… | 229 | KEEP ←in 245 | 229 | 4.3 |
| 10 | 3 | `resolve_reference_ids` | limit=5, min_score=50, purpose=Find literature ID … | 323 | KEEP ←in 245 | 323 | 7.7 |
| 11 | 3 | `search_blocks` | compound=GLOBcomp_2, limit=20, property=GLOBprop_4… | 1,217 | KEEP ←in 10,917 | 1202 | 15.2 |
| 12 | 3 | `search_blocks` | compound=GLOBcomp_4, limit=20, property=GLOBprop_4… | 1,110 | KEEP ←in 10,930 | 1110 | 18.5 |
| 13 | 4 | `search_blocks` | compound=GLOBcomp_4, literature=GLOBlit_11337, pro… | 681 | KEEP ←in 1,374 | 665 | 7.7 |
| 14 | 4 | `inspect_block_table` | block_number=PROPblock_8, literature=GLOBlit_369, … | 261 | — | — | 0.0 |
| 15 | 4 | `search_blocks` | compound=GLOBcomp_2, literature=GLOBlit_11337, pro… | 649 | KEEP ←in 1,374 | 633 | 6.9 |
| 16 | 4 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_369,… | 261 | — | — | 0.0 |
| 17 | 5 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_369,… | 335 | — | — | 0.1 |
| 18 | 6 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_11337… | 623 | — | — | 0.1 |
| 19 | 6 | `inspect_block_table` | block_number=GLOBlit_11337::PROPblock_8, nearest={… | 327 | — | — | 0.1 |
| 20 | 6 | `inspect_block_table` | block_number=GLOBlit_369::PROPblock_8, nearest={'T… | 335 | — | — | 0.1 |
| 21 | 8 | `inspect_block_table` | block_number=GLOBlit_369::PROPblock_11, purpose=Gr… | 557 | — | — | 0.1 |
| 22 | 8 | `inspect_block_table` | block_number=GLOBlit_11337::PROPblock_8, purpose=G… | 537 | — | — | 0.1 |
| 23 | 8 | `inspect_block_table` | block_number=GLOBlit_369::PROPblock_8, purpose=Gro… | 557 | — | — | 0.1 |
| 24 | 6 | `query_thermoml_parallel` | queries=[{'label': 'pure_methanol_vis… | 15,313 | — | — | 153.9 |
| 25 | 9 | `inspect_block` | block_number=PROPblock_11, doi=10.1021/je800633a, … | 1,414 | — | — | 0.1 |
| 26 | 2 | `resolve_reference_ids` | limit=5, min_score=50, purpose=Find GLOBlit_N for … | 243 | KEEP ←in 245 | 243 | 7.5 |
| 27 | 3 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_1133… | 261 | — | — | 0.0 |
| 28 | 4 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_1133… | 387 | — | — | 0.2 |
| 29 | 6 | `search_blocks` | compound=GLOBcomp_2, literature=GLOBlit_11337, pro… | 1,148 | KEEP ←in 7,783 | 1148 | 14.1 |
| 30 | 6 | `search_blocks` | compound=GLOBcomp_2, limit=10, property=GLOBprop_4… | 733 | KEEP ←in 5,552 | 701 | 17.7 |
| 31 | 7 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_11337… | 623 | — | — | 0.1 |
| 32 | 9 | `inspect_block_table` | block_number=PROPblock_11, literature=GLOBlit_369,… | 644 | — | — | 0.1 |
| 33 | 9 | `query_thermoml` | context=Need pure ethanol viscosity e…, instructio… | 12,504 | — | — | 137.2 |
| 34 | 11 | `fit_block` | block_number=PROPblock_16, doi=10.1021/je800633a, … | 861 | — | — | 2.2 |
| 35 | 12 | `list_session_files` |  | 1,617 | — | — | 0.0 |
| | | **TOTAL (35 tools)** | | **60,662** | | **7,880** | **496.7** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 1,206 | 23,724 | 882 | 7.0 |
| 2 | L1-worker | claudeopus46 | 24,095 | 946 | 25,041 | 1,113 | 6.5 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,357 | 26,452 | 848 | 4.7 |
| 4 | L1-worker | claudeopus46 | 3,767 | 448 | 4,215 | 397 | 3.6 |
| 5 | L1-worker | claudeopus46 | 3,767 | 466 | 4,233 | 378 | 3.8 |
| 6 | L1-worker | claudeopus46 | 24,095 | 2,200 | 26,295 | 992 | 6.7 |
| 7 | L1-worker | claudeopus46 | 3,767 | 2,389 | 6,156 | 1,533 | 11.1 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,971 | 28,066 | 883 | 8.1 |
| 9 | L1-worker | claudeopus46 | 24,095 | 5,909 | 30,004 | 1,771 | 14.0 |
| 10 | L1-worker | claudeopus46 | 2,106 | 2,969 | 5,075 | 532 | 3.6 |
| 11 | L1-worker | claudeopus46 | 627 | 1,782 | 2,409 | 655 | 4.1 |
| 12 | L1-worker | claudeopus46 | 2,320 | 1,902 | 4,222 | 811 | 4.7 |
| 13 | L1-worker | claudeopus46 | 366 | 1,309 | 1,675 | 405 | 2.6 |
| 14 | L1-worker | claudeopus46 | 366 | 1,248 | 1,614 | 771 | 3.6 |
| 15 | L1-worker | claudeopus46 | 787 | 10,798 | 11,585 | 423 | 5.2 |
| 16 | L0-main | claudeopus46 | 22,518 | 12,537 | 35,055 | 1,271 | 10.1 |
| 17 | L0-main | claudeopus46 | 22,518 | 13,536 | 36,054 | 798 | 5.4 |
| 18 | L0-main | claudeopus46 | 22,518 | 14,543 | 37,061 | 774 | 5.4 |
| 19 | L0-main | claudeopus46 | 22,518 | 16,475 | 38,993 | 1,946 | 13.7 |
| 20 | L0-main | claudeopus46 | 22,518 | 17,264 | 39,782 | 1,474 | 7.7 |
| 21 | L1-worker | claudeopus46 | 24,095 | 878 | 24,973 | 1,178 | 7.9 |
| 22 | L1-worker | claudeopus46 | 24,095 | 875 | 24,970 | 1,146 | 8.7 |
| 23 | L1-worker | claudeopus46 | 24,095 | 2,319 | 26,414 | 908 | 5.3 |
| 24 | L1-worker | claudeopus46 | 24,095 | 2,294 | 26,389 | 907 | 4.7 |
| 25 | L1-worker | claudeopus46 | 24,095 | 3,212 | 27,307 | 928 | 4.9 |
| 26 | L1-worker | claudeopus46 | 24,095 | 3,216 | 27,311 | 911 | 5.5 |
| 27 | L1-worker | claudeopus46 | 3,767 | 387 | 4,154 | 260 | 3.0 |
| 28 | L1-worker | claudeopus46 | 3,767 | 383 | 4,150 | 368 | 4.2 |
| 29 | L1-worker | claudeopus46 | 3,767 | 597 | 4,364 | 507 | 4.2 |
| 30 | L1-worker | claudeopus46 | 3,767 | 11,313 | 15,080 | 1,613 | 13.0 |
| 31 | L1-worker | claudeopus46 | 3,767 | 11,336 | 15,103 | 1,524 | 13.4 |
| 32 | L1-worker | claudeopus46 | 24,095 | 3,534 | 27,629 | 1,607 | 10.3 |
| 33 | L1-worker | claudeopus46 | 24,095 | 3,741 | 27,836 | 1,329 | 16.5 |
| 34 | L1-worker | claudeopus46 | 3,767 | 1,784 | 5,551 | 1,004 | 7.5 |
| 35 | L1-worker | claudeopus46 | 3,767 | 1,760 | 5,527 | 954 | 6.8 |
| 36 | L1-worker | claudeopus46 | 24,095 | 5,491 | 29,586 | 1,373 | 10.1 |
| 37 | L1-worker | claudeopus46 | 24,095 | 5,325 | 29,420 | 3,547 | 22.6 |
| 38 | L1-worker | claudeopus46 | 24,095 | 6,456 | 30,551 | 1,213 | 8.8 |
| 39 | L1-worker | claudeopus46 | 24,095 | 11,272 | 35,367 | 1,199 | 8.1 |
| 40 | L1-worker | claudeopus46 | 24,095 | 7,780 | 31,875 | 2,006 | 16.0 |
| 41 | L1-worker | claudeopus46 | 24,095 | 12,122 | 36,217 | 892 | 6.6 |
| 42 | L1-worker | claudeopus46 | 24,095 | 12,607 | 36,702 | 3,106 | 20.4 |
| 43 | L1-worker | claudeopus46 | 24,095 | 13,184 | 37,279 | 787 | 7.5 |
| 44 | L1-worker | claudeopus46 | 24,095 | 18,108 | 42,203 | 1,238 | 11.5 |
| 45 | L1-worker | claudeopus46 | 24,095 | 16,990 | 41,085 | 1,590 | 14.3 |
| 46 | L1-worker | claudeopus46 | 627 | 1,366 | 1,993 | 317 | 3.5 |
| 47 | L1-worker | claudeopus46 | 24,095 | 19,823 | 43,918 | 1,078 | 9.9 |
| 48 | L1-worker | claudeopus46 | 2,320 | 1,486 | 3,806 | 533 | 4.3 |
| 49 | L1-worker | claudeopus46 | 2,106 | 2,482 | 4,588 | 1,006 | 5.5 |
| 50 | L1-worker | claudeopus46 | 366 | 728 | 1,094 | 305 | 2.3 |
| 51 | L1-worker | claudeopus46 | 366 | 970 | 1,336 | 489 | 2.9 |
| 52 | L1-worker | claudeopus46 | 627 | 1,089 | 1,716 | 576 | 3.9 |
| 53 | L1-worker | claudeopus46 | 2,320 | 1,209 | 3,529 | 572 | 4.0 |
| 54 | L1-worker | claudeopus46 | 2,106 | 2,208 | 4,314 | 796 | 4.3 |
| 55 | L1-worker | claudeopus46 | 366 | 1,783 | 2,149 | 740 | 5.0 |
| 56 | L1-worker | claudeopus46 | 366 | 1,573 | 1,939 | 588 | 3.2 |
| 57 | L1-worker | claudeopus46 | 787 | 12,621 | 13,408 | 369 | 4.7 |
| 58 | L1-worker | claudeopus46 | 1,228 | 3,779 | 5,007 | 543 | 3.3 |
| 59 | L1-worker | claudeopus46 | 787 | 12,478 | 13,265 | 665 | 7.3 |
| 60 | L1-worker | claudeopus46 | 787 | 12,620 | 13,407 | 332 | 5.2 |
| 61 | L0-main | claudeopus46 | 22,518 | 31,162 | 53,680 | 1,937 | 13.4 |
| 62 | L0-main | claudeopus46 | 22,518 | 32,071 | 54,589 | 1,457 | 9.9 |
| 63 | L0-main | claudeopus46 | 22,518 | 32,924 | 55,442 | 1,139 | 7.7 |
| 64 | L1-worker | claudeopus46 | 24,095 | 1,054 | 25,149 | 797 | 6.4 |
| 65 | L1-worker | claudeopus46 | 24,095 | 2,050 | 26,145 | 540 | 3.8 |
| 66 | L1-worker | claudeopus46 | 3,767 | 386 | 4,153 | 266 | 3.1 |
| 67 | L1-worker | claudeopus46 | 3,767 | 596 | 4,363 | 427 | 4.2 |
| 68 | L1-worker | claudeopus46 | 24,095 | 1,939 | 26,034 | 685 | 5.3 |
| 69 | L1-worker | claudeopus46 | 24,095 | 2,710 | 26,805 | 578 | 4.5 |
| 70 | L1-worker | claudeopus46 | 24,095 | 3,599 | 27,694 | 1,384 | 8.9 |
| 71 | L1-worker | claudeopus46 | 24,095 | 4,526 | 28,621 | 917 | 6.0 |
| 72 | L1-worker | claudeopus46 | 3,767 | 8,155 | 11,922 | 1,481 | 13.9 |
| 73 | L1-worker | claudeopus46 | 3,767 | 5,952 | 9,719 | 1,713 | 12.9 |
| 74 | L1-worker | claudeopus46 | 24,095 | 6,646 | 30,741 | 1,382 | 10.8 |
| 75 | L1-worker | claudeopus46 | 24,095 | 7,822 | 31,917 | 1,055 | 8.6 |
| 76 | L1-worker | claudeopus46 | 24,095 | 11,533 | 35,628 | 1,979 | 13.2 |
| 77 | L1-worker | claudeopus46 | 24,095 | 12,773 | 36,868 | 1,030 | 9.0 |
| 78 | L1-worker | claudeopus46 | 24,095 | 15,818 | 39,913 | 1,042 | 4.4 |
| 79 | L1-worker | claudeopus46 | 627 | 1,053 | 1,680 | 590 | 4.1 |
| 80 | L1-worker | claudeopus46 | 2,106 | 2,348 | 4,454 | 996 | 5.2 |
| 81 | L1-worker | claudeopus46 | 2,320 | 1,173 | 3,493 | 630 | 6.0 |
| 82 | L1-worker | claudeopus46 | 366 | 1,067 | 1,433 | 595 | 3.2 |
| 83 | L1-worker | claudeopus46 | 366 | 1,773 | 2,139 | 730 | 4.1 |
| 84 | L1-worker | claudeopus46 | 787 | 12,378 | 13,165 | 553 | 5.5 |
| 85 | L0-main | claudeopus46 | 22,518 | 37,014 | 59,532 | 1,616 | 12.6 |
| 86 | L0-main | claudeopus46 | 22,518 | 37,891 | 60,409 | 1,052 | 6.9 |
| 87 | L0-main | claudeopus46 | 22,518 | 40,044 | 62,562 | 1,173 | 10.5 |
| 88 | L0-main | claudeopus46 | 22,518 | 42,188 | 64,706 | 3,558 | 26.2 |
| 89 | L0-main | claudeopus46 | 22,518 | 49,606 | 72,124 | 4,845 | 33.3 |
| 90 | L0-main | claudeopus46 | 2,106 | 5,206 | 7,312 | 373 | 3.2 |
| 91 | L0-main | claudeopus46 | 2,320 | 3,901 | 6,221 | 1,073 | 7.5 |
| 92 | L0-main | claudeopus46 | 366 | 896 | 1,262 | 362 | 5.1 |
| 93 | L0-main | claudeopus46 | 366 | 1,510 | 1,876 | 1,033 | 4.6 |
| 94 | L0-main | claudeopus46 | 560 | 4,973 | 5,533 | 251 | 3.8 |
| 95 | L0-main | claudeopus46 | 1,156 | 6,937 | 8,093 | 1,035 | 6.5 |
| 96 | L0-main | claudeopus46 | 366 | 1,728 | 2,094 | 989 | 4.2 |
| 97 | L0-main | claudeopus46 | 1,918 | 6,479 | 8,397 | 1,089 | 10.5 |

