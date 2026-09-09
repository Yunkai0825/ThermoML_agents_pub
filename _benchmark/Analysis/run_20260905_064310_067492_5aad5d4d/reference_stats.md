# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:43:10
**Wall time (at last flush):** 928.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 32 | 549,392 | 2,441,961 | 95,324 | 2,991,353 | 93,479 | 742.2 | claudeopus46 |
| L1-worker | 76 | 1,028,490 | 414,051 | 77,685 | 1,442,541 | 18,980 | 600.6 | claudeopus46 |
| **TOTAL** | **108** | **1,577,882** | **2,856,012** | **173,009** | **4,433,894** | **41,054** | **1342.8** | |

**Estimated tokens:** ~1,108,473 input + ~43,252 output = ~1,151,725 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 1 | 2 | 1 | 1 | 3 |
| `search_blocks` | 2 | 1 | 2 | 2 | 4 | 4 | 177 |
| `search_blocks` | 2 | 1 | 3 | 2 | 6 | 6 | 250 |
| `search_blocks` | 3 | 1 | 2 | 1 | 1 | 1 | 33 |
| `search_blocks` | 2 | 1 | 1 | 2 | 1 | 1 | 3 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml_parallel` | 3 | 1 | 3 | 3 | 8 | 9 | 0 |
| `list_session_files` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **23** | **7** | **12** | **12** | **21** | **22** | **466** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_18 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |
| GLOBcomp_24 |  | query_thermoml_parallel, resolve_compound_ids, search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 |  | query_thermoml_parallel, resolve_property_ids, search_blocks |

#### References (11 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_8892 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8676 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_9900 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_11030 |  | search_blocks |
| GLOBlit_11207 |  | search_blocks |
| GLOBlit_2656 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_5201 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_6951 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8038 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_8106 |  | query_thermoml_parallel, search_blocks |
| GLOBlit_11506 |  | search_blocks |

#### Measurements (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_4 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBmeas_140 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBmeas_8 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBmeas_227 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |
| GLOBmeas_142 | Viscosity, Pa*s | query_thermoml_parallel, search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml_parallel, search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | query_thermoml_parallel, search_blocks |
| GLOBvar_2 | Mole fraction | query_thermoml_parallel, search_blocks |
| GLOBvar_5 | Mass fraction | query_thermoml_parallel, search_blocks |

#### Constraints (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_3 | Mole fraction | query_thermoml_parallel, search_blocks |
| GLOBconstr_1 | Pressure, kPa | query_thermoml_parallel, search_blocks |
| GLOBconstr_2 | Temperature, K | query_thermoml_parallel, search_blocks |

#### Block_Types (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_3 |  | query_thermoml_parallel |
| GLOBblocktype_1 |  | query_thermoml_parallel |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 3 |
| Unique Properties | 1 |
| Unique References | 11 |
| Unique Measurements | 6 |
| Unique Phases | 1 |
| Unique Variables | 3 |
| Unique Constraints | 3 |
| Unique Block_Types | 2 |
| Total DOIs | 11 |
| Unique parent blocks | 12 |
| Explicit block/subsystem targets | 12 |
| Subsystem targets | 0 |
| Target-matched data points | 807 |

---

## 3. DOI & Block References

**Unique DOIs:** 11  |  **Parent blocks:** 12  |  **Explicit targets:** 12  |  **Subsystems:** 0  |  **Target-matched datapoints:** 463

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.jct.2006.01.011 | 1 | 10 | binary | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2018.02.022 | 1 | 84 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/acs.jced.6b00526 | 1 | 33 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je020140j | 1 | 77 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je025610o | 1 | 30 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je050209y | 1 | 11 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je060113j | 2 | 36 | binary, ternary | query_thermoml_parallel, search_blocks |
| 10.1021/je300608v | 1 | 60 | binary | query_thermoml_parallel, search_blocks |
| 10.1021/je700671t | 1 | 98 | binary | search_blocks |
| 10.1021/je800330d | 1 | 8 | binary | search_blocks |
| 10.1021/je9000697 | 1 | 16 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.jct.2006.01.011 | PROPblock_13 | declared | 10 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_24 | declared | 84 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/acs.jced.6b00526 | PROPblock_18 | declared | 33 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je020140j | PROPblock_5 | declared | 77 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je025610o | PROPblock_5 | declared | 30 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je050209y | PROPblock_9 | declared | 11 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je060113j | PROPblock_25 | declared | 3 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je060113j | PROPblock_38 | declared | 33 | ternary | 3 | query_thermoml_parallel, search_blocks |
| 10.1021/je300608v | PROPblock_3 | declared | 60 | binary | 2 | query_thermoml_parallel, search_blocks |
| 10.1021/je700671t | PROPblock_3 | declared | 98 | binary | — | search_blocks |
| 10.1021/je800330d | PROPblock_3 | declared | 8 | binary | — | search_blocks |
| 10.1021/je9000697 | PROPblock_1 | declared | 16 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `query_thermoml_parallel` | queries=[{'label': 'ternary', 'purpos… | 150 | — | — | 0.0 |
| 2 | 2 | `query_thermoml_parallel` | queries=[{'label': 'ternary_viscosity… | 132 | — | — | 0.1 |
| 3 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve DMF and wat… | 208 | KEEP ←in 295 | 208 | 4.1 |
| 4 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 290 | KEEP ←in 367 | 290 | 4.1 |
| 5 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 240 | KEEP ←in 311 | 240 | 4.2 |
| 6 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve compound ID… | 204 | KEEP ←in 288 | 204 | 4.3 |
| 7 | 3 | `resolve_property_ids` | limit=5, min_score=50, purpose=Find viscosity prop… | 238 | KEEP ←in 213 | 238 | 4.1 |
| 8 | 4 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_24'], limit=50,… | 1,244 | KEEP ←in 1,673 | 1229 | 19.9 |
| 9 | 4 | `search_blocks` | compound=['GLOBcomp_24', 'GLOBcomp_1'], limit=50, … | 1,205 | KEEP ←in 8,653 | 1205 | 19.5 |
| 10 | 4 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_1'], limit=50, … | 562 | KEEP ←in 8,201 | 562 | 24.0 |
| 11 | 5 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_24'…, limit=50,… | 1,125 | KEEP ←in 2,925 | 1110 | 13.5 |
| 12 | 6 | `inspect_block_table` | block_number=GLOBlit_8892::PROPblock_38, purpose=G… | 400 | — | — | 1.2 |
| 13 | 7 | `inspect_block_table` | block_number=GLOBlit_8892::PROPblock_38, purpose=G… | 1,616 | — | — | 0.2 |
| 14 | 5 | `search_blocks` | compound=['GLOBcomp_18', 'GLOBcomp_24'], limit=50,… | 855 | KEEP ←in 1,673 | 840 | 11.7 |
| 15 | 6 | `inspect_block_table` | block_number=PROPblock_13, literature=GLOBlit_2656… | 1,253 | — | — | 0.2 |
| 16 | 6 | `inspect_block_table` | block_number=PROPblock_9, literature=GLOBlit_8676,… | 1,354 | — | — | 0.2 |
| 17 | 7 | `inspect_block_table` | block_number=GLOBlit_5201::PROPblock_24, purpose=G… | 1,481 | — | — | 0.1 |
| 18 | 7 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_9900,… | 259 | — | — | 0.0 |
| 19 | 6 | `inspect_block_table` | block_number=PROPblock_25, literature=GLOBlit_8892… | 247 | — | — | 0.0 |
| 20 | 8 | `inspect_block_table` | block_number=GLOBlit_6951::PROPblock_18, purpose=G… | 1,412 | — | — | 0.2 |
| 21 | 7 | `inspect_block_table` | block_number=PROPblock_25, literature=GLOBlit_8892… | 382 | — | — | 0.6 |
| 22 | 9 | `inspect_block_table` | block_number=GLOBlit_8038::PROPblock_5, purpose=Gr… | 2,629 | — | — | 0.1 |
| 23 | 8 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_9900,… | 367 | — | — | 0.1 |
| 24 | 8 | `inspect_block_table` | block_number=PROPblock_25, literature=GLOBlit_8892… | 1,017 | — | — | 0.1 |
| 25 | 9 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_9900,… | 1,498 | — | — | 0.1 |
| 26 | 10 | `inspect_block_table` | block_number=GLOBlit_8106::PROPblock_5, purpose=In… | 1,513 | — | — | 0.2 |
| 27 | 3 | `query_thermoml_parallel` | queries=[{'label': 'ternary_viscosity… | 124,616 | — | — | 182.2 |
| 28 | 5 | `fit_multi_system` | purpose=Fit Arrhenius-RK viscosity mo…, systems=[{… | 464 | — | — | 0.2 |
| 29 | 8 | `inspect_block` | block_number=PROPblock_3, doi=10.1021/je300608v, p… | 1,360 | — | — | 0.1 |
| 30 | 11 | `fit_multi_system` | purpose=Fit Arrhenius-RK models for D…, systems=[{… | 1,167 | — | — | 2.7 |
| 31 | 12 | `predict_from_rk` | coeffs=[3.14029, 3.88544, 1.91579, -…, mixing_rule… | 221 | — | — | 0.1 |
| 32 | 14 | `predict_from_rk` | coeffs=[3.14029, 3.88544, 1.91579, -…, mixing_rule… | 221 | — | — | 0.1 |
| 33 | 15 | `list_session_files` |  | 2,915 | — | — | 0.5 |
| | | **TOTAL (33 tools)** | | **152,845** | | **6,126** | **298.7** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | chars=81071>80000 | skipped_by_agent | 81,071 | 81,071 | 0 | 0.0% |
| 2 | chars=83256>80000 | skipped_by_agent | 83,256 | 83,256 | 0 | 0.0% |
| 3 | chars=85310>80000 | skipped_by_agent | 85,310 | 85,310 | 0 | 0.0% |
| 4 | chars=86122>80000 | skipped_by_agent | 86,122 | 86,122 | 0 | 0.0% |
| 5 | chars=87458>80000 | skipped_by_agent | 87,458 | 87,458 | 0 | 0.0% |
| 6 | chars=90830>80000 | skipped_by_agent | 90,830 | 90,830 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 485 | 23,003 | 2,624 | 13.3 |
| 2 | L0-main | claudeopus46 | 22,518 | 913 | 23,431 | 2,109 | 10.6 |
| 3 | L0-main | claudeopus46 | 22,518 | 1,347 | 23,865 | 1,922 | 9.3 |
| 4 | L1-worker | claudeopus46 | 24,095 | 790 | 24,885 | 603 | 4.7 |
| 5 | L1-worker | claudeopus46 | 24,095 | 844 | 24,939 | 658 | 4.8 |
| 6 | L1-worker | claudeopus46 | 24,095 | 827 | 24,922 | 684 | 5.6 |
| 7 | L1-worker | claudeopus46 | 24,095 | 807 | 24,902 | 669 | 5.8 |
| 8 | L1-worker | claudeopus46 | 24,095 | 1,811 | 25,906 | 531 | 3.9 |
| 9 | L1-worker | claudeopus46 | 24,095 | 1,900 | 25,995 | 649 | 4.6 |
| 10 | L1-worker | claudeopus46 | 24,095 | 1,880 | 25,975 | 567 | 4.0 |
| 11 | L1-worker | claudeopus46 | 24,095 | 1,857 | 25,952 | 585 | 3.9 |
| 12 | L1-worker | claudeopus46 | 3,767 | 446 | 4,213 | 362 | 3.8 |
| 13 | L1-worker | claudeopus46 | 3,767 | 534 | 4,301 | 423 | 3.9 |
| 14 | L1-worker | claudeopus46 | 3,767 | 466 | 4,233 | 432 | 4.0 |
| 15 | L1-worker | claudeopus46 | 3,767 | 474 | 4,241 | 391 | 4.1 |
| 16 | L1-worker | claudeopus46 | 24,095 | 1,421 | 25,516 | 785 | 6.2 |
| 17 | L1-worker | claudeopus46 | 24,095 | 1,494 | 25,589 | 734 | 5.8 |
| 18 | L1-worker | claudeopus46 | 24,095 | 1,572 | 25,667 | 841 | 6.5 |
| 19 | L1-worker | claudeopus46 | 24,095 | 1,459 | 25,554 | 845 | 6.5 |
| 20 | L1-worker | claudeopus46 | 3,767 | 358 | 4,125 | 436 | 3.8 |
| 21 | L1-worker | claudeopus46 | 24,095 | 2,141 | 26,236 | 667 | 5.1 |
| 22 | L1-worker | claudeopus46 | 24,095 | 2,193 | 26,288 | 691 | 5.1 |
| 23 | L1-worker | claudeopus46 | 24,095 | 2,183 | 26,278 | 727 | 5.2 |
| 24 | L1-worker | claudeopus46 | 24,095 | 2,156 | 26,251 | 886 | 6.1 |
| 25 | L1-worker | claudeopus46 | 24,095 | 2,928 | 27,023 | 704 | 7.4 |
| 26 | L1-worker | claudeopus46 | 3,767 | 2,184 | 5,951 | 1,699 | 12.8 |
| 27 | L1-worker | claudeopus46 | 3,767 | 9,181 | 12,948 | 1,536 | 13.1 |
| 28 | L1-worker | claudeopus46 | 3,767 | 8,700 | 12,467 | 1,659 | 15.9 |
| 29 | L1-worker | claudeopus46 | 3,767 | 3,437 | 7,204 | 1,460 | 13.1 |
| 30 | L1-worker | claudeopus46 | 24,095 | 3,423 | 27,518 | 1,479 | 11.5 |
| 31 | L1-worker | claudeopus46 | 24,095 | 4,053 | 28,148 | 725 | 7.0 |
| 32 | L1-worker | claudeopus46 | 24,095 | 3,339 | 27,434 | 2,506 | 15.7 |
| 33 | L1-worker | claudeopus46 | 24,095 | 4,801 | 28,896 | 577 | 5.5 |
| 34 | L1-worker | claudeopus46 | 24,095 | 2,675 | 26,770 | 2,607 | 18.4 |
| 35 | L1-worker | claudeopus46 | 3,767 | 2,137 | 5,904 | 1,176 | 11.5 |
| 36 | L1-worker | claudeopus46 | 24,095 | 9,216 | 33,311 | 904 | 8.6 |
| 37 | L1-worker | claudeopus46 | 24,095 | 8,203 | 32,298 | 792 | 6.8 |
| 38 | L1-worker | claudeopus46 | 24,095 | 10,832 | 34,927 | 572 | 5.0 |
| 39 | L1-worker | claudeopus46 | 24,095 | 9,859 | 33,954 | 594 | 5.8 |
| 40 | L1-worker | claudeopus46 | 24,095 | 6,690 | 30,785 | 1,922 | 14.3 |
| 41 | L1-worker | claudeopus46 | 24,095 | 4,603 | 28,698 | 1,237 | 12.2 |
| 42 | L1-worker | claudeopus46 | 24,095 | 12,635 | 36,730 | 592 | 6.2 |
| 43 | L1-worker | claudeopus46 | 2,320 | 2,053 | 4,373 | 1,043 | 4.4 |
| 44 | L1-worker | claudeopus46 | 24,095 | 5,175 | 29,270 | 507 | 4.4 |
| 45 | L1-worker | claudeopus46 | 2,106 | 3,018 | 5,124 | 871 | 5.1 |
| 46 | L1-worker | claudeopus46 | 24,095 | 14,377 | 38,472 | 593 | 5.6 |
| 47 | L1-worker | claudeopus46 | 366 | 1,480 | 1,846 | 1,003 | 3.9 |
| 48 | L1-worker | claudeopus46 | 627 | 1,933 | 2,560 | 1,423 | 8.5 |
| 49 | L1-worker | claudeopus46 | 366 | 1,648 | 2,014 | 628 | 3.9 |
| 50 | L1-worker | claudeopus46 | 24,095 | 10,486 | 34,581 | 472 | 11.2 |
| 51 | L1-worker | claudeopus46 | 24,095 | 5,828 | 29,923 | 580 | 6.4 |
| 52 | L1-worker | claudeopus46 | 366 | 1,834 | 2,200 | 1,410 | 6.5 |
| 53 | L1-worker | claudeopus46 | 24,095 | 11,122 | 35,217 | 559 | 7.4 |
| 54 | L1-worker | claudeopus46 | 24,095 | 17,337 | 41,432 | 574 | 14.6 |
| 55 | L1-worker | claudeopus46 | 24,095 | 7,150 | 31,245 | 1,313 | 10.2 |
| 56 | L1-worker | claudeopus46 | 787 | 14,294 | 15,081 | 495 | 7.6 |
| 57 | L1-worker | claudeopus46 | 627 | 1,324 | 1,951 | 627 | 4.5 |
| 58 | L1-worker | claudeopus46 | 2,320 | 1,444 | 3,764 | 619 | 4.7 |
| 59 | L1-worker | claudeopus46 | 2,106 | 2,392 | 4,498 | 876 | 6.1 |
| 60 | L1-worker | claudeopus46 | 366 | 1,056 | 1,422 | 497 | 3.2 |
| 61 | L1-worker | claudeopus46 | 366 | 1,653 | 2,019 | 616 | 3.6 |
| 62 | L1-worker | claudeopus46 | 24,095 | 12,911 | 37,006 | 2,123 | 17.5 |
| 63 | L1-worker | claudeopus46 | 787 | 10,365 | 11,152 | 463 | 6.4 |
| 64 | L1-worker | claudeopus46 | 24,095 | 19,199 | 43,294 | 2,441 | 19.4 |
| 65 | L1-worker | claudeopus46 | 24,095 | 18,222 | 42,317 | 3,178 | 23.3 |
| 66 | L1-worker | claudeopus46 | 627 | 2,209 | 2,836 | 998 | 6.6 |
| 67 | L1-worker | claudeopus46 | 2,106 | 3,240 | 5,346 | 1,205 | 6.7 |
| 68 | L1-worker | claudeopus46 | 2,320 | 2,329 | 4,649 | 938 | 7.0 |
| 69 | L1-worker | claudeopus46 | 366 | 1,409 | 1,775 | 985 | 4.4 |
| 70 | L1-worker | claudeopus46 | 366 | 1,375 | 1,741 | 898 | 4.4 |
| 71 | L1-worker | claudeopus46 | 366 | 1,982 | 2,348 | 898 | 5.2 |
| 72 | L1-worker | claudeopus46 | 24,095 | 25,395 | 49,490 | 4,657 | 32.1 |
| 73 | L1-worker | claudeopus46 | 2,320 | 3,742 | 6,062 | 877 | 5.1 |
| 74 | L1-worker | claudeopus46 | 787 | 18,403 | 19,190 | 629 | 7.0 |
| 75 | L1-worker | claudeopus46 | 366 | 1,314 | 1,680 | 842 | 4.0 |
| 76 | L1-worker | claudeopus46 | 627 | 3,622 | 4,249 | 1,332 | 10.0 |
| 77 | L1-worker | claudeopus46 | 2,106 | 4,670 | 6,776 | 2,203 | 10.3 |
| 78 | L1-worker | claudeopus46 | 366 | 2,980 | 3,346 | 1,625 | 6.7 |
| 79 | L1-worker | claudeopus46 | 787 | 38,571 | 39,358 | 780 | 8.5 |
| 80 | L0-main | claudeopus46 | 22,518 | 102,956 | 125,474 | 3,776 | 30.6 |
| 81 | L0-main | claudeopus46 | 22,518 | 103,838 | 126,356 | 1,458 | 11.6 |
| 82 | L0-main | claudeopus46 | 22,485 | 105,031 | 127,516 | 445 | 4.7 |
| 83 | L0-main | claudeopus46 | 22,518 | 104,272 | 126,790 | 996 | 8.0 |
| 84 | L0-main | claudeopus46 | 22,518 | 104,931 | 127,449 | 505 | 4.2 |
| 85 | L0-main | claudeopus46 | 22,518 | 105,550 | 128,068 | 399 | 3.5 |
| 86 | L0-main | claudeopus46 | 22,485 | 107,781 | 130,266 | 491 | 5.7 |
| 87 | L0-main | claudeopus46 | 22,518 | 107,022 | 129,540 | 1,115 | 8.0 |
| 88 | L0-main | claudeopus46 | 22,518 | 107,684 | 130,202 | 1,678 | 10.0 |
| 89 | L0-main | claudeopus46 | 22,518 | 108,343 | 130,861 | 1,016 | 7.7 |
| 90 | L0-main | claudeopus46 | 22,485 | 112,438 | 134,923 | 396 | 5.2 |
| 91 | L0-main | claudeopus46 | 22,518 | 111,678 | 134,196 | 8,683 | 66.5 |
| 92 | L0-main | claudeopus46 | 22,485 | 113,295 | 135,780 | 479 | 12.1 |
| 93 | L0-main | claudeopus46 | 22,518 | 112,535 | 135,053 | 7,479 | 64.0 |
| 94 | L0-main | claudeopus46 | 22,518 | 113,416 | 135,934 | 10,728 | 86.5 |
| 95 | L0-main | claudeopus46 | 22,485 | 114,701 | 137,186 | 430 | 6.6 |
| 96 | L0-main | claudeopus46 | 22,518 | 113,941 | 136,459 | 10,718 | 79.8 |
| 97 | L0-main | claudeopus46 | 22,485 | 118,121 | 140,606 | 395 | 6.5 |
| 98 | L0-main | claudeopus46 | 22,518 | 117,361 | 139,879 | 12,352 | 97.4 |
| 99 | L0-main | claudeopus46 | 22,518 | 135,805 | 158,323 | 7,798 | 64.0 |
| 100 | L0-main | claudeopus46 | 22,518 | 149,990 | 172,508 | 8,242 | 64.0 |
| 101 | L0-main | claudeopus46 | 2,106 | 13,402 | 15,508 | 492 | 4.6 |
| 102 | L0-main | claudeopus46 | 366 | 1,015 | 1,381 | 484 | 5.3 |
| 103 | L0-main | claudeopus46 | 2,320 | 12,802 | 15,122 | 1,653 | 15.3 |
| 104 | L0-main | claudeopus46 | 366 | 2,090 | 2,456 | 1,598 | 5.4 |
| 105 | L0-main | claudeopus46 | 560 | 14,159 | 14,719 | 336 | 3.0 |
| 106 | L0-main | claudeopus46 | 1,156 | 17,180 | 18,336 | 1,796 | 12.1 |
| 107 | L0-main | claudeopus46 | 366 | 2,489 | 2,855 | 1,544 | 5.8 |
| 108 | L0-main | claudeopus46 | 1,918 | 5,390 | 7,308 | 1,187 | 10.9 |

