# Reference Stats — query-agent

**Run started:** 2026-09-05 16:24:07
**Wall time (at last flush):** 176.2 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 30,596 | 40,829 | 9,890 | 71,425 | 7,936 | 71.0 | claudeopus46 |
| L1-worker | 17 | 186,904 | 75,306 | 16,252 | 262,210 | 15,424 | 122.0 | claudeopus46 |
| **TOTAL** | **26** | **217,500** | **116,135** | **26,142** | **333,635** | **12,832** | **193.0** | |

**Estimated tokens:** ~83,408 input + ~6,535 output = ~89,943 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 15 | 5 | 6 | 24 | 36 | 2,749 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `resolve_reference_ids` | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| `inspect_block_table` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **4** | **15** | **5** | **6** | **26** | **36** | **2,749** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_58 |  | resolve_compound_ids, search_blocks |
| GLOBcomp_1 |  | resolve_compound_ids, search_blocks |

#### References (24 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_695 |  | search_blocks |
| GLOBlit_1910 |  | search_blocks |
| GLOBlit_2605 |  | search_blocks |
| GLOBlit_2738 |  | search_blocks |
| GLOBlit_2979 |  | search_blocks |
| GLOBlit_3181 |  | search_blocks |
| GLOBlit_3421 |  | search_blocks |
| GLOBlit_3743 |  | search_blocks |
| GLOBlit_4014 |  | search_blocks |
| GLOBlit_4204 |  | search_blocks |
| GLOBlit_4631 |  | search_blocks |
| GLOBlit_4951 |  | resolve_reference_ids, search_blocks |
| GLOBlit_5201 |  | search_blocks |
| GLOBlit_5254 |  | resolve_reference_ids, search_blocks |
| GLOBlit_5288 |  | search_blocks |
| GLOBlit_5843 |  | search_blocks |
| GLOBlit_6107 |  | search_blocks |
| GLOBlit_6532 |  | search_blocks |
| GLOBlit_6811 |  | search_blocks |
| GLOBlit_7304 |  | search_blocks |
| GLOBlit_8608 |  | search_blocks |
| GLOBlit_8736 |  | search_blocks |
| GLOBlit_9653 |  | search_blocks |
| GLOBlit_9758 |  | search_blocks |

#### Properties (15 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_14 | Boiling temperature at pressure P, K | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBprop_84 | Partial molar volume, m3/mol | search_blocks |
| GLOBprop_64 | Apparent molar heat capacity, J/K/mol | search_blocks |
| GLOBprop_1 | Mass density, kg/m3 | search_blocks |
| GLOBprop_5 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBprop_74 | Specific volume, m3/kg | search_blocks |
| GLOBprop_8 | Speed of sound, m/s | search_blocks |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBprop_17 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBprop_3 | Activity coefficient | search_blocks |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks |
| GLOBprop_39 | Refractive index (other wavelength) | search_blocks |
| GLOBprop_29 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBprop_44 | Relative permittivity at zero frequency | search_blocks |

#### Measurements (19 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_5 | Boiling temperature at pressure P, K | search_blocks |
| GLOBmeas_192 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_1187 | Partial molar volume, m3/mol | search_blocks |
| GLOBmeas_57 | Apparent molar heat capacity, J/K/mol | search_blocks |
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_133 | Vapor or sublimation pressure, kPa | search_blocks |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks |
| GLOBmeas_66 | Specific volume, m3/kg | search_blocks |
| GLOBmeas_18 | Speed of sound, m/s | search_blocks |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_13 | Excess molar enthalpy (molar enthalpy of mixing), kJ/mol | search_blocks |
| GLOBmeas_1 | Activity coefficient | search_blocks |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks |
| GLOBmeas_1790 | Refractive index (other wavelength) | search_blocks |
| GLOBmeas_1907 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBmeas_38 | Binary diffusion coefficient, m2/s | search_blocks |
| GLOBmeas_46 | Relative permittivity at zero frequency | search_blocks |
| GLOBmeas_7 | Speed of sound, m/s | search_blocks |

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks |

#### Variables (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_2 | Mole fraction | search_blocks |
| GLOBvar_1 | Temperature, K | search_blocks |
| GLOBvar_3 | Pressure, kPa | search_blocks |
| GLOBvar_4 | Molality, mol/kg | search_blocks |
| GLOBvar_5 | Mass fraction | search_blocks |

#### Constraints (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_2 | Temperature, K | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |
| GLOBconstr_5 | Mass fraction | search_blocks |
| GLOBconstr_9 | Wavelength, nm | search_blocks |

#### Solvents (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 2 |
| Unique References | 24 |
| Unique Properties | 15 |
| Unique Measurements | 19 |
| Unique Phases | 1 |
| Unique Variables | 5 |
| Unique Constraints | 6 |
| Unique Solvents | 1 |
| Total DOIs | 24 |
| Unique parent blocks | 36 |
| Explicit block/subsystem targets | 36 |
| Subsystem targets | 0 |
| Target-matched data points | 2,749 |

---

## 3. DOI & Block References

**Unique DOIs:** 24  |  **Parent blocks:** 36  |  **Explicit targets:** 36  |  **Subsystems:** 0  |  **Target-matched datapoints:** 2,749

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1016/j.fluid.2009.03.011 | 1 | 17 | binary | search_blocks |
| 10.1016/j.fluid.2016.04.007 | 1 | 60 | binary | search_blocks |
| 10.1016/j.jct.2005.08.015 | 1 | 35 | binary | search_blocks |
| 10.1016/j.jct.2006.08.009 | 2 | 261 | binary | search_blocks |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | search_blocks |
| 10.1016/j.jct.2009.11.020 | 1 | 70 | binary | search_blocks |
| 10.1016/j.jct.2011.06.016 | 1 | 73 | binary | search_blocks |
| 10.1016/j.jct.2012.09.032 | 1 | 17 | binary | search_blocks |
| 10.1016/j.jct.2013.09.046 | 1 | 94 | binary | search_blocks |
| 10.1016/j.jct.2014.06.031 | 2 | 510 | binary | search_blocks |
| 10.1016/j.jct.2016.02.026 | 1 | 7 | binary | search_blocks |
| 10.1016/j.jct.2017.01.011 | 2 | 88 | binary | search_blocks |
| 10.1016/j.jct.2018.02.022 | 3 | 348 | binary | search_blocks |
| 10.1016/j.jct.2018.05.016 | 2 | 32 | binary | search_blocks |
| 10.1016/j.jct.2018.07.015 | 2 | 40 | binary | search_blocks |
| 10.1016/j.tca.2009.06.004 | 1 | 9 | binary | search_blocks |
| 10.1016/j.tca.2013.07.012 | 1 | 296 | binary | search_blocks |
| 10.1021/acs.jced.5b00116 | 2 | 9 | binary | search_blocks |
| 10.1021/acs.jced.5b01080 | 2 | 350 | binary | search_blocks |
| 10.1021/acs.jced.7b00717 | 3 | 32 | binary | search_blocks |
| 10.1021/je050082c | 1 | 13 | binary | search_blocks |
| 10.1021/je050353j | 1 | 28 | binary | search_blocks |
| 10.1021/je200766t | 1 | 50 | binary | search_blocks |
| 10.1021/je201184b | 2 | 214 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1016/j.fluid.2009.03.011 | PROPblock_1 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.fluid.2016.04.007 | PROPblock_1 | declared | 60 | binary | — | search_blocks |
| 10.1016/j.jct.2005.08.015 | PROPblock_4 | declared | 35 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.009 | PROPblock_5 | declared | 162 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.009 | PROPblock_6 | declared | 99 | binary | — | search_blocks |
| 10.1016/j.jct.2008.07.005 | PROPblock_8 | declared | 96 | binary | — | search_blocks |
| 10.1016/j.jct.2009.11.020 | PROPblock_8 | declared | 70 | binary | — | search_blocks |
| 10.1016/j.jct.2011.06.016 | PROPblock_6 | declared | 73 | binary | — | search_blocks |
| 10.1016/j.jct.2012.09.032 | PROPblock_7 | declared | 17 | binary | — | search_blocks |
| 10.1016/j.jct.2013.09.046 | PROPblock_11 | declared | 94 | binary | — | search_blocks |
| 10.1016/j.jct.2014.06.031 | PROPblock_5 | declared | 85 | binary | — | search_blocks |
| 10.1016/j.jct.2014.06.031 | PROPblock_6 | declared | 425 | binary | — | search_blocks |
| 10.1016/j.jct.2016.02.026 | PROPblock_17 | declared | 7 | binary | — | search_blocks |
| 10.1016/j.jct.2017.01.011 | PROPblock_3 | declared | 44 | binary | — | search_blocks |
| 10.1016/j.jct.2017.01.011 | PROPblock_4 | declared | 44 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_31 | declared | 136 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_32 | declared | 136 | binary | — | search_blocks |
| 10.1016/j.jct.2018.02.022 | PROPblock_33 | declared | 76 | binary | — | search_blocks |
| 10.1016/j.jct.2018.05.016 | PROPblock_10 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2018.05.016 | PROPblock_9 | declared | 16 | binary | — | search_blocks |
| 10.1016/j.jct.2018.07.015 | PROPblock_1 | declared | 20 | binary | — | search_blocks |
| 10.1016/j.jct.2018.07.015 | PROPblock_2 | declared | 20 | binary | — | search_blocks |
| 10.1016/j.tca.2009.06.004 | PROPblock_4 | declared | 9 | binary | — | search_blocks |
| 10.1016/j.tca.2013.07.012 | PROPblock_3 | declared | 296 | binary | — | search_blocks |
| 10.1021/acs.jced.5b00116 | PROPblock_4 | declared | 4 | binary | — | search_blocks |
| 10.1021/acs.jced.5b00116 | PROPblock_5 | declared | 5 | binary | — | search_blocks |
| 10.1021/acs.jced.5b01080 | PROPblock_15 | declared | 175 | binary | — | search_blocks |
| 10.1021/acs.jced.5b01080 | PROPblock_16 | declared | 175 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00717 | PROPblock_1 | declared | 14 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00717 | PROPblock_2 | declared | 3 | binary | — | search_blocks |
| 10.1021/acs.jced.7b00717 | PROPblock_3 | declared | 15 | binary | — | search_blocks |
| 10.1021/je050082c | PROPblock_1 | declared | 13 | binary | — | search_blocks |
| 10.1021/je050353j | PROPblock_4 | declared | 28 | binary | — | search_blocks |
| 10.1021/je200766t | PROPblock_3 | declared | 50 | binary | — | search_blocks |
| 10.1021/je201184b | PROPblock_5 | declared | 107 | binary | — | search_blocks |
| 10.1021/je201184b | PROPblock_6 | declared | 107 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=50, purpose=Resolve glycerol an… | 217 | KEEP ←in 286 | 217 | 4.3 |
| 2 | 3 | `search_blocks` | compound=['GLOBcomp_58', 'GLOBcomp_1'], limit=50, … | 1,192 | KEEP ←in 23,441 | 1192 | 21.1 |
| 3 | 4 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_131, … | 153 | — | — | 0.2 |
| 4 | 5 | `resolve_reference_ids` | limit=5, min_score=50, purpose=Find GLOBlit_N for … | 276 | KEEP ←in 338 | 276 | 4.6 |
| 5 | 6 | `inspect_block_table` | block_number=PROPblock_3, literature=GLOBlit_4951,… | 1,786 | — | — | 0.1 |
| 6 | 1 | `L1_query` | instruction=Search for the binary system …, purpos… | 16,288 | — | — | 113.1 |
| | | **TOTAL (6 tools)** | | **19,912** | | **1,685** | **143.4** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 523 | 12,104 | 1,676 | 11.5 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,120 | 25,215 | 696 | 6.4 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,160 | 26,255 | 532 | 4.1 |
| 4 | L1-worker | claudeopus46 | 3,767 | 469 | 4,236 | 398 | 4.0 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,742 | 25,837 | 765 | 5.5 |
| 6 | L1-worker | claudeopus46 | 3,767 | 23,887 | 27,654 | 1,600 | 14.6 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,228 | 27,323 | 776 | 6.1 |
| 8 | L1-worker | claudeopus46 | 24,095 | 3,753 | 27,848 | 1,531 | 12.1 |
| 9 | L1-worker | claudeopus46 | 3,767 | 508 | 4,275 | 434 | 4.3 |
| 10 | L1-worker | claudeopus46 | 24,095 | 4,370 | 28,465 | 724 | 5.2 |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,501 | 30,596 | 3,137 | 23.1 |
| 12 | L1-worker | claudeopus46 | 2,106 | 4,084 | 6,190 | 623 | 3.7 |
| 13 | L1-worker | claudeopus46 | 2,320 | 2,843 | 5,163 | 892 | 6.6 |
| 14 | L1-worker | claudeopus46 | 366 | 1,400 | 1,766 | 441 | 3.3 |
| 15 | L1-worker | claudeopus46 | 627 | 2,723 | 3,350 | 1,152 | 7.9 |
| 16 | L1-worker | claudeopus46 | 366 | 1,329 | 1,695 | 852 | 4.0 |
| 17 | L1-worker | claudeopus46 | 366 | 1,563 | 1,929 | 1,139 | 4.4 |
| 18 | L1-worker | claudeopus46 | 787 | 13,626 | 14,413 | 560 | 6.7 |
| 19 | L0-main | claudeopus46 | 11,581 | 17,011 | 28,592 | 3,549 | 28.7 |
| 20 | L0-main | claudeopus46 | 2,106 | 3,819 | 5,925 | 671 | 4.7 |
| 21 | L0-main | claudeopus46 | 2,320 | 3,464 | 5,784 | 1,275 | 8.4 |
| 22 | L0-main | claudeopus46 | 366 | 1,220 | 1,586 | 786 | 3.6 |
| 23 | L0-main | claudeopus46 | 366 | 1,750 | 2,116 | 1,226 | 4.6 |
| 24 | L0-main | claudeopus46 | 560 | 4,222 | 4,782 | 163 | 2.5 |
| 25 | L0-main | claudeopus46 | 560 | 3,924 | 4,484 | 105 | 2.4 |
| 26 | L0-main | claudeopus46 | 1,156 | 4,896 | 6,052 | 439 | 4.6 |

