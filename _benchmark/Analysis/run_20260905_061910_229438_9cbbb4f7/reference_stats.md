# Reference Stats — analysis-agent

**Run started:** 2026-09-05 06:19:10
**Wall time (at last flush):** 678.1 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 31 | 549,224 | 807,984 | 55,545 | 1,357,208 | 43,780 | 448.7 | claudeopus46 |
| L1-worker | 27 | 314,447 | 125,882 | 29,875 | 440,329 | 16,308 | 230.0 | claudeopus46 |
| **TOTAL** | **58** | **863,671** | **933,866** | **85,420** | **1,797,537** | **30,992** | **678.7** | |

**Estimated tokens:** ~449,384 input + ~21,355 output = ~470,739 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 6 | 2 | 12 | 12 | 2,011 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 56 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 2 | 1 | 1 | 2 | 0 |
| `query_thermoml` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `query_thermoml` | 2 | 1 | 2 | 1 | 1 | 1 | 0 |
| **TOTAL** | **10** | **4** | **12** | **5** | **15** | **16** | **2,067** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_6 |  | query_thermoml, resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | query_thermoml, resolve_compound_ids, search_blocks |

#### References (12 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_1311 |  | search_blocks |
| GLOBlit_2432 |  | search_blocks |
| GLOBlit_5585 |  | search_blocks |
| GLOBlit_6822 |  | search_blocks |
| GLOBlit_7474 |  | search_blocks |
| GLOBlit_7629 |  | search_blocks |
| GLOBlit_8447 |  | search_blocks |
| GLOBlit_9722 |  | search_blocks |
| GLOBlit_11042 |  | search_blocks |
| GLOBlit_11130 |  | search_blocks |
| GLOBlit_11142 |  | query_thermoml, search_blocks |
| GLOBlit_11872 |  | search_blocks |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | query_thermoml, search_blocks |

#### Measurements (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | query_thermoml, search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | query_thermoml, search_blocks |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_2 | Mole fraction | query_thermoml, search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_1 | Temperature, K | query_thermoml, search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |
| GLOBvar_15 | Mass ratio of solute to solvent | search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |

#### Constraints (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | query_thermoml, search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | query_thermoml |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 12 |
| Unique Properties | 1 |
| Unique Measurements | 2 |
| Unique Phases | 1 |
| Unique Variables | 6 |
| Unique Solvents | 1 |
| Unique Constraints | 2 |
| Unique Block_Types | 1 |
| Total DOIs | 12 |
| Unique parent blocks | 13 |
| Explicit block/subsystem targets | 13 |
| Subsystem targets | 0 |
| Target-matched data points | 2,179 |

---

## 3. DOI & Block References

**Unique DOIs:** 12  |  **Parent blocks:** 13  |  **Explicit targets:** 13  |  **Subsystems:** 0  |  **Target-matched datapoints:** 2,011

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2013.08.007 | 1 | 1,110 | binary | search_blocks |
| 10.1016/j.jct.2004.07.019 | 1 | 529 | binary | search_blocks |
| 10.1016/j.jct.2019.105880 | 1 | 12 | binary | search_blocks |
| 10.1021/acs.jced.6b00019 | 1 | 6 | binary | search_blocks |
| 10.1021/acs.jced.8b00160 | 1 | 18 | binary | search_blocks |
| 10.1021/acs.jced.8b00723 | 1 | 3 | binary | search_blocks |
| 10.1021/je049738c | 1 | 8 | binary | search_blocks |
| 10.1021/je201010s | 1 | 17 | binary | search_blocks |
| 10.1021/je700700f | 1 | 13 | binary | search_blocks |
| 10.1021/je8001305 | 1 | 209 | binary | search_blocks |
| 10.1021/je800158z | 2 | 56 | binary | query_thermoml, search_blocks |
| 10.1021/je900966r | 1 | 30 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2013.08.007 | PROPblock_4 | declared | 1,110 | binary | — | search_blocks |
| 10.1016/j.jct.2004.07.019 | PROPblock_4 | declared | 529 | binary | — | search_blocks |
| 10.1016/j.jct.2019.105880 | PROPblock_10 | declared | 12 | binary | — | search_blocks |
| 10.1021/acs.jced.6b00019 | PROPblock_13 | declared | 6 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00160 | PROPblock_15 | declared | 18 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00723 | PROPblock_14 | declared | 3 | binary | — | search_blocks |
| 10.1021/je049738c | PROPblock_28 | declared | 8 | binary | — | search_blocks |
| 10.1021/je201010s | PROPblock_8 | declared | 17 | binary | — | search_blocks |
| 10.1021/je700700f | PROPblock_17 | declared | 13 | binary | — | search_blocks |
| 10.1021/je8001305 | PROPblock_1 | declared | 209 | binary | — | search_blocks |
| 10.1021/je800158z | PROPblock_1 | declared | 0 | — | — | query_thermoml |
| 10.1021/je800158z | PROPblock_4 | declared | 56 | binary | 2 | query_thermoml, search_blocks |
| 10.1021/je900966r | PROPblock_6 | declared | 30 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=70, purpose=Resolve compound ID… | 183 | KEEP ←in 285 | 183 | 4.3 |
| 2 | 3 | `search_blocks` | compound=['GLOBcomp_6', 'GLOBcomp_1'], limit=50, p… | 490 | KEEP ←in 7,821 | 428 | 20.3 |
| 3 | 4 | `inspect_block_table` | block_number=GLOBlit_11142::PROPblock_1, purpose=I… | 768 | — | — | 0.1 |
| 4 | 5 | `search_blocks` | compound=['GLOBcomp_6', 'GLOBcomp_1'], limit=10, l… | 836 | KEEP ←in 2,628 | 820 | 9.8 |
| 5 | 6 | `inspect_block_table` | block_number=GLOBlit_11142::PROPblock_4, purpose=I… | 2,079 | — | — | 1.0 |
| 6 | 1 | `query_thermoml` | instruction=Search for blocks containing …, purpos… | 18,965 | — | — | 180.6 |
| 7 | 6 | `fit_block_derived` | block_number=PROPblock_4, composition_hint=mole_fr… | 250 | — | — | 0.1 |
| 8 | 10 | `fit_block_derived` | block_number=PROPblock_4, composition_hint=mole_fr… | 898 | — | — | 1.6 |
| 9 | 11 | `fit_block_derived` | block_number=PROPblock_4, composition_hint=mole_fr… | 929 | — | — | 1.8 |
| 10 | 12 | `fit_block_derived` | block_number=PROPblock_4, composition_hint=mole_fr… | 931 | — | — | 1.6 |
| 11 | 13 | `fit_block_derived` | block_number=PROPblock_4, composition_hint=mole_fr… | 945 | — | — | 2.2 |
| 12 | 14 | `fit_block_derived` | block_number=PROPblock_4, composition_hint=mole_fr… | 958 | — | — | 2.4 |
| 13 | 15 | `predict_from_rk` | coeffs=[-3.81402e-06, 1.587e-06, -2.…, n_points=10… | 210 | — | — | 0.1 |
| 14 | 16 | `predict_from_rk` | coeffs=[-3.63344e-06, 1.55557e-06, -…, mixing_rule… | 210 | — | — | 0.2 |
| 15 | 17 | `predict_from_rk` | coeffs=[-3.49707e-06, 1.56252e-06, -…, mixing_rule… | 209 | — | — | 0.1 |
| 16 | 18 | `predict_from_rk` | coeffs=[-3.38265e-06, 1.70513e-06, -…, property_ty… | 210 | — | — | 0.8 |
| 17 | 20 | `inspect_block` | block_number=PROPblock_4, doi=10.1021/je800158z, p… | 1,369 | — | — | 0.7 |
| 18 | 22 | `query_thermoml` | context=Block PROPblock_4 has 56 rows…, id_catalog… | 204 | — | — | 0.0 |
| 19 | 1 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_11142… | 758 | — | — | 0.1 |
| 20 | 2 | `inspect_block_table` | block_number=PROPblock_4, literature=GLOBlit_11142… | 758 | — | — | 0.1 |
| 21 | 23 | `query_thermoml` | context=Block PROPblock_4 has 56 rows…, id_catalog… | 8,983 | — | — | 37.1 |
| | | **TOTAL (21 tools)** | | **41,143** | | **1,431** | **265.0** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 22,518 | 370 | 22,888 | 1,400 | 10.7 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,135 | 25,230 | 643 | 5.5 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,170 | 26,265 | 555 | 3.9 |
| 4 | L1-worker | claudeopus46 | 3,767 | 460 | 4,227 | 349 | 4.2 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,748 | 25,843 | 789 | 6.2 |
| 6 | L1-worker | claudeopus46 | 3,767 | 8,253 | 12,020 | 1,846 | 14.5 |
| 7 | L1-worker | claudeopus46 | 24,095 | 2,555 | 26,650 | 1,218 | 8.5 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,743 | 27,838 | 1,244 | 8.5 |
| 9 | L1-worker | claudeopus46 | 3,767 | 3,064 | 6,831 | 1,034 | 9.4 |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,988 | 29,083 | 1,056 | 8.8 |
| 11 | L1-worker | claudeopus46 | 24,095 | 7,438 | 31,533 | 3,554 | 25.5 |
| 12 | L1-worker | claudeopus46 | 24,095 | 15,978 | 40,073 | 4,640 | 33.1 |
| 13 | L1-worker | claudeopus46 | 24,095 | 23,626 | 47,721 | 3,291 | 22.5 |
| 14 | L1-worker | claudeopus46 | 2,320 | 2,786 | 5,106 | 808 | 5.4 |
| 15 | L1-worker | claudeopus46 | 2,106 | 4,042 | 6,148 | 952 | 6.1 |
| 16 | L1-worker | claudeopus46 | 627 | 2,666 | 3,293 | 927 | 6.1 |
| 17 | L1-worker | claudeopus46 | 366 | 1,245 | 1,611 | 773 | 3.6 |
| 18 | L1-worker | claudeopus46 | 366 | 1,729 | 2,095 | 666 | 3.8 |
| 19 | L1-worker | claudeopus46 | 787 | 13,817 | 14,604 | 639 | 9.9 |
| 20 | L0-main | claudeopus46 | 22,518 | 16,481 | 38,999 | 2,243 | 18.6 |
| 21 | L0-main | claudeopus46 | 22,518 | 17,757 | 40,275 | 1,558 | 11.3 |
| 22 | L0-main | claudeopus46 | 22,518 | 18,528 | 41,046 | 927 | 6.1 |
| 23 | L0-main | claudeopus46 | 22,518 | 19,230 | 41,748 | 1,024 | 6.3 |
| 24 | L0-main | claudeopus46 | 22,518 | 20,018 | 42,536 | 849 | 4.6 |
| 25 | L0-main | claudeopus46 | 22,518 | 18,732 | 41,250 | 852 | 6.4 |
| 26 | L0-main | claudeopus46 | 22,518 | 19,462 | 41,980 | 1,006 | 7.6 |
| 27 | L0-main | claudeopus46 | 22,518 | 20,137 | 42,655 | 1,007 | 7.0 |
| 28 | L0-main | claudeopus46 | 22,518 | 20,872 | 43,390 | 954 | 5.9 |
| 29 | L0-main | claudeopus46 | 22,518 | 22,437 | 44,955 | 1,217 | 9.3 |
| 30 | L0-main | claudeopus46 | 22,518 | 25,071 | 47,589 | 1,153 | 9.1 |
| 31 | L0-main | claudeopus46 | 22,518 | 27,668 | 50,186 | 869 | 11.0 |
| 32 | L0-main | claudeopus46 | 22,518 | 30,257 | 52,775 | 880 | 9.2 |
| 33 | L0-main | claudeopus46 | 22,518 | 32,822 | 55,340 | 2,150 | 17.0 |
| 34 | L0-main | claudeopus46 | 22,518 | 33,429 | 55,947 | 808 | 8.9 |
| 35 | L0-main | claudeopus46 | 22,518 | 33,998 | 56,516 | 835 | 7.4 |
| 36 | L0-main | claudeopus46 | 22,518 | 34,611 | 57,129 | 811 | 10.4 |
| 37 | L0-main | claudeopus46 | 22,518 | 35,275 | 57,793 | 7,947 | 56.2 |
| 38 | L0-main | claudeopus46 | 22,518 | 48,540 | 71,058 | 1,064 | 9.6 |
| 39 | L0-main | claudeopus46 | 22,518 | 50,750 | 73,268 | 9,427 | 71.0 |
| 40 | L0-main | claudeopus46 | 22,518 | 65,526 | 88,044 | 2,147 | 19.3 |
| 41 | L0-main | claudeopus46 | 22,518 | 66,068 | 88,586 | 1,373 | 13.9 |
| 42 | L1-worker | claudeopus46 | 24,095 | 1,300 | 25,395 | 769 | 6.2 |
| 43 | L1-worker | claudeopus46 | 24,095 | 2,380 | 26,475 | 571 | 5.2 |
| 44 | L1-worker | claudeopus46 | 24,095 | 3,441 | 27,536 | 885 | 6.7 |
| 45 | L1-worker | claudeopus46 | 2,320 | 1,016 | 3,336 | 415 | 3.6 |
| 46 | L1-worker | claudeopus46 | 2,106 | 2,437 | 4,543 | 515 | 4.8 |
| 47 | L1-worker | claudeopus46 | 627 | 896 | 1,523 | 459 | 5.0 |
| 48 | L1-worker | claudeopus46 | 366 | 1,292 | 1,658 | 371 | 2.7 |
| 49 | L1-worker | claudeopus46 | 1,228 | 3,171 | 4,399 | 334 | 3.0 |
| 50 | L1-worker | claudeopus46 | 787 | 8,506 | 9,293 | 572 | 7.3 |
| 51 | L0-main | claudeopus46 | 22,518 | 73,227 | 95,745 | 8,178 | 65.6 |
| 52 | L0-main | claudeopus46 | 2,106 | 11,775 | 13,881 | 146 | 2.9 |
| 53 | L0-main | claudeopus46 | 366 | 669 | 1,035 | 187 | 3.1 |
| 54 | L0-main | claudeopus46 | 2,320 | 11,290 | 13,610 | 1,402 | 12.9 |
| 55 | L0-main | claudeopus46 | 366 | 1,839 | 2,205 | 1,357 | 7.0 |
| 56 | L0-main | claudeopus46 | 560 | 11,803 | 12,363 | 92 | 2.6 |
| 57 | L0-main | claudeopus46 | 1,156 | 12,583 | 13,739 | 512 | 6.1 |
| 58 | L0-main | claudeopus46 | 1,918 | 6,759 | 8,677 | 1,170 | 11.7 |

