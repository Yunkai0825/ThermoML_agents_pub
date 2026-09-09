# Reference Stats — analysis-agent

**Run started:** 2026-09-05 04:35:15
**Wall time (at last flush):** 770.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 29 | 504,188 | 1,134,220 | 48,427 | 1,638,408 | 56,496 | 382.3 | claudeopus46 |
| L1-worker | 38 | 558,302 | 298,523 | 55,565 | 856,825 | 22,548 | 410.7 | claudeopus46 |
| **TOTAL** | **67** | **1,062,490** | **1,432,743** | **103,992** | **2,495,233** | **37,242** | **793.0** | |

**Estimated tokens:** ~623,808 input + ~25,998 output = ~649,806 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_property_ids` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 2 | 3 | 4 | 58 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 2 | 2 | 2 | 3 | 0 |
| `query_thermoml` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 2 | 3 | 4 | 58 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 3 | 2 | 3 | 4 | 0 |
| **TOTAL** | **11** | **5** | **11** | **8** | **11** | **15** | **116** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_2 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_5494 |  | resolve_compound_ids |
| GLOBcomp_1 |  | query_thermoml, resolve_compound_ids, search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_17 |  | query_thermoml, resolve_property_ids, search_blocks |

#### References (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_528 |  | query_thermoml, search_blocks |
| GLOBlit_2574 |  | query_thermoml, search_blocks |
| GLOBlit_6377 |  | query_thermoml, search_blocks |

#### Measurements (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_13 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | query_thermoml, search_blocks |
| GLOBmeas_169 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | query_thermoml, search_blocks |
| GLOBmeas_12 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | query_thermoml, search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, search_blocks |

#### Variables (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks |
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks |
| GLOBvar_3 | Pressure, kPa | query_thermoml, search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | query_thermoml, search_blocks |
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 3 |
| Unique Properties | 1 |
| Unique References | 3 |
| Unique Measurements | 3 |
| Unique Phases | 1 |
| Unique Variables | 3 |
| Unique Constraints | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 3 |
| Unique parent blocks | 4 |
| Explicit block/subsystem targets | 4 |
| Subsystem targets | 0 |
| Target-matched data points | 231 |

---

## 3. DOI & Block References

**Unique DOIs:** 3  |  **Parent blocks:** 4  |  **Explicit targets:** 4  |  **Subsystems:** 0  |  **Target-matched datapoints:** 58

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2007.06.007 | 2 | 30 | binary | query_thermoml, search_blocks |
| 10.1016/j.jct.2005.06.018 | 1 | 27 | binary | query_thermoml, search_blocks |
| 10.1016/j.tca.2017.05.023 | 1 | 1 | binary | query_thermoml, search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2007.06.007 | PROPblock_1 | declared | 15 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.fluid.2007.06.007 | PROPblock_2 | declared | 15 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.jct.2005.06.018 | PROPblock_4 | declared | 27 | binary | 2 | query_thermoml, search_blocks |
| 10.1016/j.tca.2017.05.023 | PROPblock_1 | declared | 1 | binary | 2 | query_thermoml, search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve ethanol and… | 291 | KEEP ←in 351 | 291 | 6.2 |
| 2 | 3 | `resolve_property_ids` | limit=5, min_score=70, purpose=Confirm global ID f… | 396 | KEEP ←in 269 | 396 | 6.2 |
| 3 | 5 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 744 | KEEP ←in 7,304 | 744 | 21.4 |
| 4 | 6 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_2574,… | 1,436 | — | — | 0.1 |
| 5 | 7 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_528, … | 1,588 | — | — | 0.1 |
| 6 | 8 | `inspect_block_table` | block_number=PROPblock_2, literature=GLOBlit_528, … | 1,529 | — | — | 0.1 |
| 7 | 1 | `query_thermoml` | instruction=Search for blocks containing …, purpos… | 34,443 | — | — | 206.9 |
| 8 | 2 | `query_thermoml` | id_catalog=[{'id': 'GLOBcomp_2', 'type':…, instruc… | 197 | — | — | 0.0 |
| 9 | 3 | `query_thermoml` | id_catalog=[{'global_id': 'GLOBcomp_2', …, instruc… | 233 | — | — | 0.1 |
| 10 | 2 | `search_blocks` | compound=['GLOBcomp_2', 'GLOBcomp_1'], limit=50, p… | 1,120 | KEEP ←in 7,304 | 1090 | 21.2 |
| 11 | 3 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_6377,… | 249 | — | — | 0.1 |
| 12 | 4 | `inspect_block_table` | block_number=PROPblock_1, literature=GLOBlit_6377,… | 410 | — | — | 0.1 |
| 13 | 5 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_2574,… | 1,512 | — | — | 0.3 |
| 14 | 7 | `inspect_block_table` | block_number=GLOBlit_6377::PROPblock_1, purpose=Gr… | 706 | — | — | 0.2 |
| 15 | 8 | `inspect_block_table` | block_number=GLOBlit_528::PROPblock_1, purpose=Gro… | 1,588 | — | — | 0.5 |
| 16 | 9 | `inspect_block_table` | block_number=GLOBlit_528::PROPblock_2, purpose=Ins… | 1,529 | — | — | 0.3 |
| 17 | 4 | `query_thermoml` | id_catalog=[{'global_id': 'GLOBcomp_2', …, instruc… | 40,797 | — | — | 180.2 |
| 18 | 7 | `inspect_block` | block_number=PROPblock_4, doi=10.1016/j.jct.2005.0… | 1,584 | — | — | 0.1 |
| 19 | 11 | `fit_block` | block_number=PROPblock_4, doi=10.1016/j.jct.2005.0… | 293 | — | — | 0.7 |
| 20 | 15 | `fit_block` | block_number=PROPblock_4, doi=10.1016/j.jct.2005.0… | 882 | — | — | 2.1 |
| 21 | 19 | `predict_from_rk` | coeffs=[-1.60102, 1.73493, -3.19748,…, n_points=10… | 171 | — | — | 0.1 |
| | | **TOTAL (21 tools)** | | **91,698** | | **2,521** | **447.0** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 1,008 | 23,526 | 958 | 8.0 |
| 2 | L1-worker | claudeopus46 | 24,095 | 974 | 25,069 | 753 | 5.9 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,007 | 26,102 | 619 | 5.2 |
| 4 | L1-worker | claudeopus46 | 3,767 | 510 | 4,277 | 442 | 5.5 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,700 | 25,795 | 872 | 8.0 |
| 6 | L1-worker | claudeopus46 | 3,767 | 420 | 4,187 | 697 | 6.0 |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,420 | 26,515 | 858 | 6.7 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,166 | 27,261 | 681 | 5.6 |
| 9 | L1-worker | claudeopus46 | 3,767 | 7,796 | 11,563 | 1,852 | 15.6 |
| 10 | L1-worker | claudeopus46 | 24,095 | 3,901 | 27,996 | 1,091 | 8.3 |
| 11 | L1-worker | claudeopus46 | 24,095 | 5,693 | 29,788 | 843 | 7.3 |
| 12 | L1-worker | claudeopus46 | 24,095 | 7,643 | 31,738 | 1,358 | 11.4 |
| 13 | L1-worker | claudeopus46 | 24,095 | 9,523 | 33,618 | 5,177 | 35.0 |
| 14 | L1-worker | claudeopus46 | 24,095 | 18,605 | 42,700 | 4,363 | 29.7 |
| 15 | L1-worker | claudeopus46 | 24,095 | 25,813 | 49,908 | 3,965 | 26.2 |
| 16 | L1-worker | claudeopus46 | 2,320 | 3,494 | 5,814 | 1,168 | 7.2 |
| 17 | L1-worker | claudeopus46 | 627 | 3,374 | 4,001 | 1,178 | 8.0 |
| 18 | L1-worker | claudeopus46 | 2,106 | 4,589 | 6,695 | 1,795 | 9.5 |
| 19 | L1-worker | claudeopus46 | 366 | 1,605 | 1,971 | 1,128 | 4.9 |
| 20 | L1-worker | claudeopus46 | 366 | 2,572 | 2,938 | 1,089 | 5.6 |
| 21 | L1-worker | claudeopus46 | 787 | 26,697 | 27,484 | 657 | 7.1 |
| 22 | L0-main | claudeopus46 | 22,518 | 23,034 | 45,552 | 3,441 | 26.2 |
| 23 | L0-main | claudeopus46 | 22,518 | 23,731 | 46,249 | 2,099 | 14.5 |
| 24 | L0-main | claudeopus46 | 22,518 | 24,286 | 46,804 | 1,862 | 12.6 |
| 25 | L1-worker | claudeopus46 | 24,095 | 1,595 | 25,690 | 972 | 8.3 |
| 26 | L1-worker | claudeopus46 | 24,095 | 2,332 | 26,427 | 622 | 4.8 |
| 27 | L1-worker | claudeopus46 | 3,767 | 7,767 | 11,534 | 1,769 | 15.1 |
| 28 | L1-worker | claudeopus46 | 24,095 | 3,412 | 27,507 | 803 | 7.4 |
| 29 | L1-worker | claudeopus46 | 24,095 | 4,059 | 28,154 | 591 | 4.9 |
| 30 | L1-worker | claudeopus46 | 24,095 | 4,744 | 28,839 | 2,577 | 19.6 |
| 31 | L1-worker | claudeopus46 | 24,095 | 6,683 | 30,778 | 2,516 | 20.0 |
| 32 | L1-worker | claudeopus46 | 24,095 | 13,719 | 37,814 | 588 | 6.5 |
| 33 | L1-worker | claudeopus46 | 24,095 | 14,724 | 38,819 | 605 | 7.2 |
| 34 | L1-worker | claudeopus46 | 24,095 | 16,625 | 40,720 | 414 | 4.7 |
| 35 | L1-worker | claudeopus46 | 24,095 | 18,473 | 42,568 | 2,981 | 22.1 |
| 36 | L1-worker | claudeopus46 | 24,095 | 24,309 | 48,404 | 3,012 | 22.6 |
| 37 | L1-worker | claudeopus46 | 2,106 | 4,859 | 6,965 | 1,728 | 8.4 |
| 38 | L1-worker | claudeopus46 | 627 | 3,023 | 3,650 | 1,292 | 8.4 |
| 39 | L1-worker | claudeopus46 | 2,320 | 3,143 | 5,463 | 1,322 | 13.7 |
| 40 | L1-worker | claudeopus46 | 366 | 2,505 | 2,871 | 1,275 | 5.6 |
| 41 | L1-worker | claudeopus46 | 366 | 1,759 | 2,125 | 1,277 | 5.5 |
| 42 | L1-worker | claudeopus46 | 787 | 32,290 | 33,077 | 635 | 7.2 |
| 43 | L0-main | claudeopus46 | 22,518 | 48,463 | 70,981 | 1,968 | 17.8 |
| 44 | L0-main | claudeopus46 | 22,518 | 49,273 | 71,791 | 509 | 5.4 |
| 45 | L0-main | claudeopus46 | 22,518 | 49,924 | 72,442 | 462 | 4.9 |
| 46 | L0-main | claudeopus46 | 22,518 | 51,862 | 74,380 | 1,041 | 9.6 |
| 47 | L0-main | claudeopus46 | 22,518 | 52,532 | 75,050 | 830 | 6.8 |
| 48 | L0-main | claudeopus46 | 22,518 | 53,170 | 75,688 | 906 | 6.7 |
| 49 | L0-main | claudeopus46 | 22,518 | 53,950 | 76,468 | 920 | 6.5 |
| 50 | L0-main | claudeopus46 | 22,518 | 53,663 | 76,181 | 1,043 | 8.0 |
| 51 | L0-main | claudeopus46 | 22,518 | 54,452 | 76,970 | 1,188 | 7.9 |
| 52 | L0-main | claudeopus46 | 22,518 | 55,196 | 77,714 | 996 | 7.1 |
| 53 | L0-main | claudeopus46 | 22,518 | 55,975 | 78,493 | 907 | 14.5 |
| 54 | L0-main | claudeopus46 | 22,518 | 57,484 | 80,002 | 999 | 9.2 |
| 55 | L0-main | claudeopus46 | 22,518 | 58,199 | 80,717 | 589 | 9.8 |
| 56 | L0-main | claudeopus46 | 22,518 | 58,837 | 81,355 | 669 | 4.5 |
| 57 | L0-main | claudeopus46 | 22,518 | 59,565 | 82,083 | 659 | 6.7 |
| 58 | L0-main | claudeopus46 | 22,518 | 59,176 | 81,694 | 7,676 | 52.3 |
| 59 | L0-main | claudeopus46 | 22,518 | 71,253 | 93,771 | 6,848 | 51.6 |
| 60 | L0-main | claudeopus46 | 22,518 | 82,898 | 105,416 | 6,670 | 49.4 |
| 61 | L0-main | claudeopus46 | 2,106 | 6,776 | 8,882 | 273 | 3.0 |
| 62 | L0-main | claudeopus46 | 366 | 796 | 1,162 | 259 | 2.8 |
| 63 | L0-main | claudeopus46 | 2,320 | 5,669 | 7,989 | 1,255 | 10.5 |
| 64 | L0-main | claudeopus46 | 366 | 1,692 | 2,058 | 1,210 | 5.2 |
| 65 | L0-main | claudeopus46 | 560 | 6,475 | 7,035 | 185 | 2.5 |
| 66 | L0-main | claudeopus46 | 1,156 | 8,018 | 9,174 | 826 | 7.2 |
| 67 | L0-main | claudeopus46 | 1,918 | 6,863 | 8,781 | 1,179 | 11.1 |

