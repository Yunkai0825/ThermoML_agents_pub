# Reference Stats — query-agent

**Run started:** 2026-08-03 04:41:28
**Wall time (at last flush):** 1,207.1 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 8 | 50,969 | 95,687 | 39,810 | 146,656 | 18,332 | 181.5 | claudeopus46 |
| L1-worker | 98 | 745,427 | 1,169,866 | 136,422 | 1,915,293 | 19,543 | 995.0 | claudeopus46 |
| **TOTAL** | **106** | **796,396** | **1,265,553** | **176,232** | **2,061,949** | **19,452** | **1176.5** | |

**Estimated tokens:** ~515,487 input + ~44,058 output = ~559,545 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `memory_catalog_add` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `memory_catalog_add` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `memory_catalog_add` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `memory_catalog_add` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `memory_catalog_add` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 76 |
| `search_blocks` | 2 | 1 | 2 | 0 | 1 | 1 | 60 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 |
| `search_system_registry` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 76 |
| `search_blocks` | 2 | 1 | 2 | 0 | 1 | 1 | 60 |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 |
| `search_system_registry` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 |
| `search_system_registry` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 |
| `search_blocks` | 2 | 1 | 4 | 2 | 11 | 11 | 1,081 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 16 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 20 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 136 |
| `search_blocks` | 2 | 1 | 2 | 1 | 1 | 1 | 296 |
| `L1_query` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_system_registry` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 14 | 1 | 7 | 4 | 11 | 19 | 1,060 |
| `search_system_registry` | 50 | 1 | 11 | 6 | 15 | 50 | 4,312 |
| **TOTAL** | **96** | **18** | **66** | **32** | **122** | **165** | **14,760** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### References (38 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_2738 |  | search_blocks, search_system_registry |
| GLOBlit_2979 |  | search_blocks, search_system_registry |
| GLOBlit_4204 |  | search_blocks, search_system_registry |
| GLOBlit_4631 |  | search_blocks, search_system_registry |
| GLOBlit_4951 |  | search_blocks, search_system_registry |
| GLOBlit_5201 |  | search_blocks, search_system_registry |
| GLOBlit_5254 |  | search_blocks, search_system_registry |
| GLOBlit_5288 |  | search_blocks, search_system_registry |
| GLOBlit_6107 |  | search_blocks, search_system_registry |
| GLOBlit_6811 |  | search_blocks, search_system_registry |
| GLOBlit_9758 |  | search_blocks, search_system_registry |
| GLOBlit_1910 |  | search_blocks |
| GLOBlit_1294 |  | search_blocks |
| GLOBlit_2036 |  | search_blocks |
| GLOBlit_5300 |  | search_blocks |
| GLOBlit_5518 |  | search_blocks |
| GLOBlit_6089 |  | search_blocks |
| GLOBlit_6129 |  | search_blocks |
| GLOBlit_7495 |  | search_blocks |
| GLOBlit_7523 |  | search_blocks |
| GLOBlit_7824 |  | search_blocks |
| GLOBlit_9121 |  | search_blocks |
| GLOBlit_10425 |  | search_blocks |
| GLOBlit_178 |  | search_system_registry |
| GLOBlit_271 |  | search_system_registry |
| GLOBlit_391 |  | search_system_registry |
| GLOBlit_729 |  | search_system_registry |
| GLOBlit_844 |  | search_system_registry |
| GLOBlit_865 |  | search_system_registry |
| GLOBlit_955 |  | search_system_registry |
| GLOBlit_1310 |  | search_system_registry |
| GLOBlit_1415 |  | search_system_registry |
| GLOBlit_1426 |  | search_system_registry |
| GLOBlit_1449 |  | search_system_registry |
| GLOBlit_1468 |  | search_system_registry |
| GLOBlit_1478 |  | search_system_registry |
| GLOBlit_1490 |  | search_system_registry |
| GLOBlit_1557 |  | search_system_registry |

#### Compounds (63 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_58 | glycerol | search_blocks, search_system_registry |
| GLOBcomp_1 | water | search_blocks, search_system_registry |
| GLOBcomp_100 | choline chloride | search_blocks |
| GLOBcomp_855 | 2-(diethylamino)ethanol hydrochloride | search_blocks |
| GLOBcomp_605 | methyltriphenylphosphonium bromide | search_blocks |
| GLOBcomp_8274 | benzyltripropylammonium chloride | search_blocks |
| GLOBcomp_1117 | 1,8-diaza-7-bicyclo[5.4.0]undecene | search_blocks |
| GLOBcomp_3 | carbon dioxide | search_blocks |
| GLOBcomp_214 | potassium carbonate | search_blocks |
| GLOBcomp_1395 | trimethylbenzylammonium chloride | search_blocks |
| GLOBcomp_1986 | benzyltributylammonium chloride | search_blocks |
| GLOBcomp_2043 | cetylpyridinium chloride | search_blocks |
| GLOBcomp_2979 | benzyltriphenylphosphonium chloride | search_blocks |
| GLOBcomp_660 | tetrabutylammonium chloride | search_blocks |
| GLOBcomp_551 | copper sulfate | search_system_registry |
| GLOBcomp_2 | ethanol | search_system_registry |
| GLOBcomp_2007 | lithium hydroxide | search_system_registry |
| GLOBcomp_1863 | aluminum bromide | search_system_registry |
| GLOBcomp_323 | 1-ethyl-3-methylimidazolium bromide | search_system_registry |
| GLOBcomp_1563 | 1-ethylpyridinium bromide | search_system_registry |
| GLOBcomp_518 | aluminum chloride | search_system_registry |
| GLOBcomp_231 | 1-ethyl-3-methylimidazolium chloride | search_system_registry |
| GLOBcomp_84 | 1-ethyl-3-methylimidazolium tetrafluoroborate | search_system_registry |
| GLOBcomp_68 | 1-ethyl-3-methylimidazolium ethyl sulfate | search_system_registry |
| GLOBcomp_146 | 4-methyl-1,3-dioxolan-2-one | search_system_registry |
| GLOBcomp_515 | lithium fluoride | search_system_registry |
| GLOBcomp_312 | ethylene carbonate | search_system_registry |
| GLOBcomp_62 | dimethyl carbonate | search_system_registry |
| GLOBcomp_2065 | pyrrolidinium nitrate | search_system_registry |
| GLOBcomp_5889 | pyrrolidinium acetate | search_system_registry |
| GLOBcomp_3105 | pyrrolidinium formate | search_system_registry |
| GLOBcomp_2658 | ethyldiisopropylammonium formate | search_system_registry |
| GLOBcomp_3788 | 2-pentanaminium formate | search_system_registry |
| GLOBcomp_4880 | quinolinium formate | search_system_registry |
| GLOBcomp_6318 | 1,2-dimethylpyridinium formate | search_system_registry |
| GLOBcomp_6017 | 1,2,3-trimethylpyridinium formate | search_system_registry |
| GLOBcomp_6917 | pyrrolidinium hexanoate | search_system_registry |
| GLOBcomp_7415 | pyrrolidinium heptanoate | search_system_registry |
| GLOBcomp_2737 | pyrrolidinium octanoate | search_system_registry |
| GLOBcomp_4222 | pyrrolidinium nonanoate | search_system_registry |
| GLOBcomp_2395 | sodium dihydrogen citrate | search_system_registry |
| GLOBcomp_1192 | 1-heptyl-3-methylimidazolium bromide | search_system_registry |
| GLOBcomp_1296 | disodium hydrogen citrate | search_system_registry |
| GLOBcomp_270 | trisodium citrate | search_system_registry |
| GLOBcomp_202 | triethylamine | search_system_registry |
| GLOBcomp_41 | potassium chloride | search_system_registry |
| GLOBcomp_1760 | hexyltrimethylammonium bromide | search_system_registry |
| GLOBcomp_734 | 1-dodecyl-3-methylimidazolium bromide | search_system_registry |
| GLOBcomp_201 | glycylglycine | search_system_registry |
| GLOBcomp_742 | glycyl-L-valine | search_system_registry |
| GLOBcomp_495 | glycyl-L-leucine | search_system_registry |
| GLOBcomp_5033 | cetyltrimethylammonium salicylate | search_system_registry |
| GLOBcomp_232 | sodium dodecyl sulfate | search_system_registry |
| GLOBcomp_573 | 1-pentyl-3-methylimidazolium bromide | search_system_registry |
| GLOBcomp_481 | 1-butyl-2,3-dimethylimidazolium tetrafluoroborate | search_system_registry |
| GLOBcomp_374 | ribose | search_system_registry |
| GLOBcomp_90 | D-glucose | search_system_registry |
| GLOBcomp_120 | D-sucrose | search_system_registry |
| GLOBcomp_886 | D-raffinose | search_system_registry |
| GLOBcomp_5 | propan-1-ol | search_system_registry |
| GLOBcomp_3909 | sodium dodecane-1-sulfonate | search_system_registry |
| GLOBcomp_1910 | N-ethyl-N-methylpiperidinium bromide | search_system_registry |
| GLOBcomp_3836 | 1-methyl-1-propylpiperidinium bromide | search_system_registry |

#### Properties (4 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks |
| GLOBprop_13 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBprop_18 | Electrical conductivity, S/m | search_blocks, search_system_registry |

#### Measurements (10 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_134 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_153 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks |
| GLOBmeas_192 | Surface tension liquid-gas, N/m | search_blocks |
| GLOBmeas_49 | Electrical conductivity, S/m | search_blocks, search_system_registry |
| GLOBmeas_14 | Electrical conductivity, S/m | search_blocks, search_system_registry |
| GLOBmeas_923 | Electrical conductivity, S/m | search_blocks |
| GLOBmeas_2068 | Electrical conductivity, S/m | search_system_registry |
| GLOBmeas_1646 | Electrical conductivity, S/m | search_system_registry |

#### Phases (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks, search_system_registry |
| GLOBphase_4 |  | search_system_registry |

#### Solvents (26 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_blocks, search_system_registry |
| GLOBsolvent_128 |  | search_blocks |
| GLOBsolvent_331 |  | search_blocks |
| GLOBsolvent_22 |  | search_blocks |
| GLOBsolvent_169 |  | search_blocks |
| GLOBsolvent_2 |  | search_system_registry |
| GLOBsolvent_375 |  | search_system_registry |
| GLOBsolvent_277 |  | search_system_registry |
| GLOBsolvent_486 |  | search_system_registry |
| GLOBsolvent_451 |  | search_system_registry |
| GLOBsolvent_163 |  | search_system_registry |
| GLOBsolvent_68 |  | search_system_registry |
| GLOBsolvent_51 |  | search_system_registry |
| GLOBsolvent_64 |  | search_system_registry |
| GLOBsolvent_425 |  | search_system_registry |
| GLOBsolvent_187 |  | search_system_registry |
| GLOBsolvent_283 |  | search_system_registry |
| GLOBsolvent_278 |  | search_system_registry |
| GLOBsolvent_194 |  | search_system_registry |
| GLOBsolvent_475 |  | search_system_registry |
| GLOBsolvent_389 |  | search_system_registry |
| GLOBsolvent_310 |  | search_system_registry |
| GLOBsolvent_34 |  | search_system_registry |
| GLOBsolvent_42 |  | search_system_registry |
| GLOBsolvent_354 |  | search_system_registry |
| GLOBsolvent_9 |  | search_system_registry |

#### Variables (13 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_4 | Molality, mol/kg | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | search_blocks, search_system_registry |
| GLOBvar_8 | Solvent: Mole fraction | search_blocks, search_system_registry |
| GLOBvar_15 | Mass ratio of solute to solvent | search_blocks |
| GLOBvar_19 | Amount ratio of solute to solvent | search_blocks |
| GLOBvar_7 | Solvent: Mass fraction | search_blocks, search_system_registry |
| GLOBvar_3 | Pressure, kPa | search_system_registry |
| GLOBvar_16 | Solvent: Volume fraction | search_system_registry |
| GLOBvar_9 | Amount concentration (molarity), mol/dm3 | search_system_registry |
| GLOBvar_6 | Solvent: Molality, mol/kg | search_system_registry |
| GLOBvar_11 | Solvent: Amount concentration (molarity), mol/dm3 | search_system_registry |

#### Constraints (9 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_2 | Temperature, K | search_blocks, search_system_registry |
| GLOBconstr_13 | Amount ratio of solute to solvent | search_blocks |
| GLOBconstr_3 | Mole fraction | search_blocks |
| GLOBconstr_4 | Frequency, MHz | search_blocks |
| GLOBconstr_7 | Solvent: Mole fraction | search_system_registry |
| GLOBconstr_8 | Molality, mol/kg | search_system_registry |
| GLOBconstr_5 | Mass fraction | search_system_registry |
| GLOBconstr_10 | Solvent: Mass fraction | search_system_registry |

#### Block_Types (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | search_system_registry |
| GLOBblocktype_3 |  | search_system_registry |
| GLOBblocktype_2 |  | search_system_registry |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique References | 38 |
| Unique Compounds | 63 |
| Unique Properties | 4 |
| Unique Measurements | 10 |
| Unique Phases | 2 |
| Unique Solvents | 26 |
| Unique Variables | 13 |
| Unique Constraints | 9 |
| Unique Block_Types | 3 |
| Total DOIs | 38 |
| Unique parent blocks | 82 |
| Explicit block/subsystem targets | 82 |
| Subsystem targets | 0 |
| Target-matched data points | 14,760 |

---

## 3. DOI & Block References

**Unique DOIs:** 38  |  **Parent blocks:** 82  |  **Explicit targets:** 82  |  **Subsystems:** 0  |  **Target-matched datapoints:** 6,589

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1007/s10765-016-2089-2 | 1 | 45 | binary | search_system_registry |
| 10.1016/j.fluid.2005.05.022 | 1 | 9 | ternary | search_system_registry |
| 10.1016/j.fluid.2006.05.028 | 6 | 127 | binary, ternary, unary | search_system_registry |
| 10.1016/j.fluid.2009.07.020 | 4 | 7 | binary, ternary | search_system_registry |
| 10.1016/j.fluid.2010.05.019 | 13 | 264 | binary, unary | search_system_registry |
| 10.1016/j.fluid.2010.08.004 | 3 | 354 | ternary | search_system_registry |
| 10.1016/j.fluid.2011.03.031 | 2 | 119 | binary, ternary | search_system_registry |
| 10.1016/j.fluid.2013.07.012 | 3 | 108 | binary | search_blocks |
| 10.1016/j.fluid.2013.08.005 | 1 | 18 | binary | search_system_registry |
| 10.1016/j.fluid.2014.01.038 | 4 | 720 | binary, ternary | search_system_registry |
| 10.1016/j.fluid.2014.02.022 | 2 | 283 | binary | search_system_registry |
| 10.1016/j.fluid.2014.03.024 | 4 | 64 | ternary | search_system_registry |
| 10.1016/j.fluid.2014.04.027 | 2 | 522 | binary, ternary | search_system_registry |
| 10.1016/j.fluid.2014.05.020 | 4 | 1,368 | ternary | search_system_registry |
| 10.1016/j.fluid.2014.06.009 | 2 | 376 | ternary | search_system_registry |
| 10.1016/j.fluid.2014.09.020 | 1 | 36 | ternary | search_system_registry |
| 10.1016/j.fluid.2016.04.007 | 1 | 60 | binary | search_blocks |
| 10.1016/j.fluid.2017.03.011 | 1 | 11 | binary | search_blocks |
| 10.1016/j.jct.2006.08.009 | 1 | 99 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2008.07.005 | 1 | 96 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2014.06.031 | 1 | 85 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2016.02.026 | 1 | 7 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2017.01.011 | 1 | 44 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.02.022 | 2 | 212 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.05.016 | 1 | 16 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.07.015 | 1 | 20 | binary | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.07.031 | 2 | 50 | binary, ternary | search_blocks |
| 10.1016/j.jct.2019.04.017 | 2 | 436 | binary, ternary | search_blocks |
| 10.1016/j.tca.2013.05.023 | 3 | 190 | binary, ternary | search_blocks |
| 10.1016/j.tca.2013.07.012 | 1 | 296 | binary | search_blocks, search_system_registry |
| 10.1016/j.tca.2013.10.028 | 1 | 21 | binary | search_blocks |
| 10.1021/acs.jced.5b01080 | 1 | 175 | binary | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00213 | 2 | 26 | binary | search_blocks |
| 10.1021/acs.jced.8b00326 | 1 | 176 | ternary | search_blocks |
| 10.1021/acs.jced.9b00134 | 1 | 6 | binary | search_blocks |
| 10.1021/je100104v | 2 | 15 | binary | search_blocks |
| 10.1021/je201184b | 1 | 107 | binary | search_blocks, search_system_registry |
| 10.1021/je5002126 | 1 | 21 | binary | search_blocks |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1007/s10765-016-2089-2 | PROPblock_1 | declared | 45 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2005.05.022 | PROPblock_1 | declared | 9 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2006.05.028 | PROPblock_16 | declared | 42 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2006.05.028 | PROPblock_18 | declared | 21 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2006.05.028 | PROPblock_20 | declared | 21 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2006.05.028 | PROPblock_5 | declared | 1 | unary | 1 | search_system_registry |
| 10.1016/j.fluid.2006.05.028 | PROPblock_6 | declared | 21 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2006.05.028 | PROPblock_8 | declared | 21 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2009.07.020 | PROPblock_12 | declared | 2 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2009.07.020 | PROPblock_15 | declared | 2 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2009.07.020 | PROPblock_18 | declared | 2 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2009.07.020 | PROPblock_8 | declared | 1 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.05.019 | PROPblock_33 | declared | 1 | unary | 1 | search_system_registry |
| 10.1016/j.fluid.2010.05.019 | PROPblock_34 | declared | 21 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.05.019 | PROPblock_35 | declared | 19 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.05.019 | PROPblock_36 | declared | 22 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.05.019 | PROPblock_37 | declared | 21 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.05.019 | PROPblock_38 | declared | 23 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.05.019 | PROPblock_39 | declared | 21 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.05.019 | PROPblock_40 | declared | 21 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.05.019 | PROPblock_41 | declared | 21 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.05.019 | PROPblock_42 | declared | 25 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.05.019 | PROPblock_43 | declared | 25 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.05.019 | PROPblock_44 | declared | 21 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.05.019 | PROPblock_45 | declared | 23 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.08.004 | PROPblock_5 | declared | 194 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2010.08.004 | PROPblock_6 | declared | 84 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2010.08.004 | PROPblock_9 | declared | 76 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2011.03.031 | PROPblock_1 | declared | 29 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2011.03.031 | PROPblock_3 | declared | 90 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2013.07.012 | PROPblock_12 | declared | 36 | binary | — | search_blocks |
| 10.1016/j.fluid.2013.07.012 | PROPblock_4 | declared | 36 | binary | — | search_blocks |
| 10.1016/j.fluid.2013.07.012 | PROPblock_8 | declared | 36 | binary | — | search_blocks |
| 10.1016/j.fluid.2013.08.005 | PROPblock_4 | declared | 18 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.01.038 | PROPblock_10 | declared | 72 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.01.038 | PROPblock_5 | declared | 216 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2014.01.038 | PROPblock_7 | declared | 216 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2014.01.038 | PROPblock_9 | declared | 216 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2014.02.022 | PROPblock_1 | declared | 213 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.02.022 | PROPblock_2 | declared | 70 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.03.024 | PROPblock_1 | declared | 7 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2014.03.024 | PROPblock_2 | declared | 25 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2014.03.024 | PROPblock_3 | declared | 12 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2014.03.024 | PROPblock_4 | declared | 20 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2014.04.027 | PROPblock_1 | declared | 456 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2014.04.027 | PROPblock_2 | declared | 66 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.05.020 | PROPblock_1 | declared | 342 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2014.05.020 | PROPblock_2 | declared | 342 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2014.05.020 | PROPblock_3 | declared | 342 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2014.05.020 | PROPblock_4 | declared | 342 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2014.06.009 | PROPblock_1 | declared | 186 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2014.06.009 | PROPblock_4 | declared | 190 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2014.09.020 | PROPblock_12 | declared | 36 | ternary | 3 | search_system_registry |
| 10.1016/j.fluid.2016.04.007 | PROPblock_1 | declared | 60 | binary | — | search_blocks |
| 10.1016/j.fluid.2017.03.011 | PROPblock_20 | declared | 11 | binary | — | search_blocks |
| 10.1016/j.jct.2006.08.009 | PROPblock_6 | declared | 99 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2008.07.005 | PROPblock_8 | declared | 96 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2014.06.031 | PROPblock_5 | declared | 85 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2016.02.026 | PROPblock_17 | declared | 7 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2017.01.011 | PROPblock_3 | declared | 44 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.02.022 | PROPblock_31 | declared | 136 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.02.022 | PROPblock_33 | declared | 76 | binary | — | search_blocks |
| 10.1016/j.jct.2018.05.016 | PROPblock_9 | declared | 16 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.07.015 | PROPblock_1 | declared | 20 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.jct.2018.07.031 | PROPblock_13 | declared | 25 | ternary | — | search_blocks |
| 10.1016/j.jct.2018.07.031 | PROPblock_6 | declared | 25 | binary | — | search_blocks |
| 10.1016/j.jct.2019.04.017 | PROPblock_5 | declared | 186 | binary | — | search_blocks |
| 10.1016/j.jct.2019.04.017 | PROPblock_7 | declared | 250 | ternary | — | search_blocks |
| 10.1016/j.tca.2013.05.023 | PROPblock_2 | declared | 10 | binary | — | search_blocks |
| 10.1016/j.tca.2013.05.023 | PROPblock_6 | declared | 90 | ternary | — | search_blocks |
| 10.1016/j.tca.2013.05.023 | PROPblock_7 | declared | 90 | ternary | — | search_blocks |
| 10.1016/j.tca.2013.07.012 | PROPblock_3 | declared | 296 | binary | 2 | search_blocks, search_system_registry |
| 10.1016/j.tca.2013.10.028 | PROPblock_3 | declared | 21 | binary | — | search_blocks |
| 10.1021/acs.jced.5b01080 | PROPblock_15 | declared | 175 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/acs.jced.8b00213 | PROPblock_34 | declared | 13 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00213 | PROPblock_39 | declared | 13 | binary | — | search_blocks |
| 10.1021/acs.jced.8b00326 | PROPblock_2 | declared | 176 | ternary | — | search_blocks |
| 10.1021/acs.jced.9b00134 | PROPblock_13 | declared | 6 | binary | — | search_blocks |
| 10.1021/je100104v | PROPblock_1 | declared | 10 | binary | — | search_blocks |
| 10.1021/je100104v | PROPblock_13 | declared | 5 | binary | — | search_blocks |
| 10.1021/je201184b | PROPblock_6 | declared | 107 | binary | 2 | search_blocks, search_system_registry |
| 10.1021/je5002126 | PROPblock_3 | declared | 21 | binary | — | search_blocks |

</details>

---

## 4. Tool Results (pre-compaction)

| # | Iter | Tool | Args | Raw (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `memory_catalog_add` | global_id=GLOBcomp_1, name=water, registry_id=7732… | 2 | — | — | 0.1 |
| 2 | 1 | `memory_catalog_add` | global_id=GLOBcomp_58, name=glycerol, registry_id=… | 2 | — | — | 0.1 |
| 3 | 1 | `memory_catalog_add` | global_id=GLOBprop_1, name=Mass density, registry_… | 127 | — | — | 0.2 |
| 4 | 1 | `memory_catalog_add` | global_id=GLOBprop_4, name=Dynamic viscosity, regi… | 127 | — | — | 0.1 |
| 5 | 1 | `memory_catalog_add` | global_id=GLOBprop_13, name=Surface tension liquid… | 127 | — | — | 0.1 |
| 6 | 1 | `memory_catalog_add` | global_id=GLOBprop_28, name=Excess molar volume, r… | 127 | — | — | 0.1 |
| 7 | 1 | `memory_catalog_add` | global_id=GLOBprop_18, name=Electrical conductivit… | 127 | — | — | 0.1 |
| 8 | 2 | `memory_catalog_add` | global_id=GLOBprop_1, name=Mass density, registry_… | 2 | — | — | 0.0 |
| 9 | 2 | `memory_catalog_add` | global_id=GLOBprop_4, name=Dynamic viscosity, regi… | 2 | — | — | 0.0 |
| 10 | 2 | `memory_catalog_add` | global_id=GLOBprop_13, name=Surface tension liquid… | 2 | — | — | 0.0 |
| 11 | 2 | `memory_catalog_add` | global_id=GLOBprop_18, name=Electrical conductivit… | 2 | — | — | 0.0 |
| 12 | 2 | `memory_catalog_add` | global_id=GLOBprop_28, name=Excess molar volume, r… | 2 | — | — | 0.1 |
| 13 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,072 | KEEP | 997 | 16.6 |
| 14 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,178 | KEEP | 1148 | 15.8 |
| 15 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,219 | KEEP | 1189 | 12.4 |
| 16 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 706 | DISCARD | 648 | 14.3 |
| 17 | 2 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 737 | DISCARD | 679 | 7.9 |
| 18 | 2 | `L1_query` | context=This is for Fe electrodeposit…, id_catalog… | 783 | — | — | 162.2 |
| 19 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,118 | KEEP | 1103 | 23.0 |
| 20 | 2 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,062 | KEEP | 1062 | 17.4 |
| 21 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=20, … | 1,090 | KEEP | 1090 | 21.8 |
| 22 | 3 | `L1_query` | context=Binary mixture water+glycerol…, id_catalog… | 720 | — | — | 218.0 |
| 23 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,341 | KEEP | 1311 | 19.7 |
| 24 | 3 | `L1_query` | context=Binary mixture water+glycerol…, id_catalog… | 9,461 | — | — | 59.5 |
| 25 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,190 | KEEP | 1160 | 11.9 |
| 26 | 3 | `L1_query` | context=Binary mixture water+glycerol…, id_catalog… | 8,955 | — | — | 43.5 |
| 27 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,140 | KEEP | 1125 | 23.2 |
| 28 | 2 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,145 | KEEP | 1130 | 25.0 |
| 29 | 3 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=100,… | 1,215 | KEEP | 1125 | 21.7 |
| 30 | 4 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 372 | KEEP | 372 | 20.2 |
| 31 | 5 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,122 | KEEP | 1122 | 14.0 |
| 32 | 6 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,054 | KEEP | 1039 | 14.8 |
| 33 | 7 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,118 | KEEP | 1103 | 12.4 |
| 34 | 8 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 1,207 | KEEP | 1192 | 12.8 |
| 35 | 4 | `L1_query` | context=Binary mixture water+glycerol…, id_catalog… | 858 | — | — | 338.4 |
| 36 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 686 | DISCARD | 628 | 14.7 |
| 37 | 2 | `search_blocks` | compound=GLOBcomp_58, limit=50, property=GLOBprop_… | 662 | DISCARD | 604 | 11.3 |
| 38 | 3 | `search_system_registry` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 779 | DISCARD | 712 | 19.1 |
| 39 | 4 | `L1_query` | context=Binary mixture water+glycerol…, id_catalog… | 1,821 | — | — | 100.0 |
| 40 | 1 | `search_blocks` | compound=['GLOBcomp_1', 'GLOBcomp_58'], limit=50, … | 723 | DISCARD | 665 | 14.1 |
| 41 | 2 | `search_blocks` | compound=GLOBcomp_58, limit=50, property=GLOBprop_… | 1,306 | KEEP | 1201 | 20.8 |
| 42 | 2 | `search_system_registry` | compound=GLOBcomp_1, limit=50, property=GLOBprop_1… | 1,501 | KEEP | 1351 | 20.3 |
| 43 | 4 | `L1_query` | context=Binary mixture water+glycerol…, id_catalog… | 3,209 | — | — | 105.5 |
| | | **TOTAL (43 tools)** | | **51,199** | | **23,756** | **1433.2** |

---

## 5. Compaction Events

| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |
|--:|---------|---------|---------------:|--------------:|--------------:|----------:|
| 1 | interval=3 | skipped_by_agent | 6,036 | 6,036 | 0 | 0.0% |
| 2 | interval=3 | skipped_by_agent | 10,208 | 10,208 | 0 | 0.0% |
| 3 | interval=3 | skipped_by_agent | 4,347 | 4,347 | 0 | 0.0% |

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 9,605 | 1,178 | 10,783 | 20,661 | 81.5 |
| 2 | L0-main | claudeopus46 | 9,605 | 3,430 | 13,035 | 2,505 | 11.8 |
| 3 | L1-worker | claudeopus46 | 20,643 | 2,042 | 22,685 | 1,557 | 8.0 |
| 4 | L1-worker | claudeopus46 | 2,065 | 7,782 | 9,847 | 1,743 | 14.5 |
| 5 | L1-worker | claudeopus46 | 2,065 | 2,742 | 4,807 | 1,628 | 11.5 |
| 6 | L1-worker | claudeopus46 | 2,065 | 2,482 | 4,547 | 1,624 | 12.0 |
| 7 | L1-worker | claudeopus46 | 20,643 | 6,354 | 26,997 | 1,294 | 8.4 |
| 8 | L1-worker | claudeopus46 | 2,065 | 472 | 2,537 | 1,122 | 7.1 |
| 9 | L1-worker | claudeopus46 | 2,065 | 480 | 2,545 | 1,052 | 7.4 |
| 10 | L1-worker | claudeopus46 | 20,643 | 8,558 | 29,201 | 4,276 | 27.1 |
| 11 | L1-worker | claudeopus46 | 1,356 | 3,279 | 4,635 | 955 | 5.6 |
| 12 | L1-worker | claudeopus46 | 536 | 3,159 | 3,695 | 967 | 6.2 |
| 13 | L1-worker | claudeopus46 | 1,323 | 11,986 | 13,309 | 2,569 | 16.6 |
| 14 | L1-worker | claudeopus46 | 298 | 3,291 | 3,589 | 2,128 | 10.0 |
| 15 | L1-worker | claudeopus46 | 747 | 55,333 | 56,080 | 521 | 5.9 |
| 16 | L1-worker | claudeopus46 | 1,160 | 15,672 | 16,832 | 2,128 | 10.6 |
| 17 | L1-worker | claudeopus46 | 747 | 55,333 | 56,080 | 679 | 7.4 |
| 18 | L0-main | claudeopus46 | 9,605 | 5,915 | 15,520 | 2,584 | 12.3 |
| 19 | L1-worker | claudeopus46 | 20,643 | 1,555 | 22,198 | 709 | 5.6 |
| 20 | L1-worker | claudeopus46 | 2,065 | 7,825 | 9,890 | 1,826 | 15.0 |
| 21 | L1-worker | claudeopus46 | 20,643 | 3,130 | 23,773 | 1,264 | 10.1 |
| 22 | L1-worker | claudeopus46 | 2,065 | 9,793 | 11,858 | 1,730 | 15.5 |
| 23 | L1-worker | claudeopus46 | 20,643 | 4,741 | 25,384 | 2,418 | 19.1 |
| 24 | L1-worker | claudeopus46 | 20,643 | 5,611 | 26,254 | 2,550 | 17.7 |
| 25 | L1-worker | claudeopus46 | 20,643 | 6,470 | 27,113 | 2,105 | 17.1 |
| 26 | L1-worker | claudeopus46 | 2,065 | 7,836 | 9,901 | 1,636 | 13.8 |
| 27 | L1-worker | claudeopus46 | 20,643 | 7,251 | 27,894 | 4,893 | 32.4 |
| 28 | L1-worker | claudeopus46 | 536 | 2,737 | 3,273 | 932 | 5.1 |
| 29 | L1-worker | claudeopus46 | 1,356 | 2,857 | 4,213 | 791 | 5.3 |
| 30 | L1-worker | claudeopus46 | 1,323 | 11,217 | 12,540 | 2,906 | 13.3 |
| 31 | L1-worker | claudeopus46 | 298 | 3,628 | 3,926 | 2,284 | 13.8 |
| 32 | L1-worker | claudeopus46 | 747 | 49,882 | 50,629 | 711 | 7.7 |
| 33 | L1-worker | claudeopus46 | 1,160 | 15,122 | 16,282 | 2,241 | 10.4 |
| 34 | L1-worker | claudeopus46 | 747 | 49,839 | 50,586 | 621 | 7.0 |
| 35 | L1-worker | claudeopus46 | 20,643 | 1,575 | 22,218 | 751 | 5.9 |
| 36 | L1-worker | claudeopus46 | 2,065 | 2,793 | 4,858 | 1,564 | 12.0 |
| 37 | L1-worker | claudeopus46 | 20,643 | 3,392 | 24,035 | 2,385 | 15.2 |
| 38 | L1-worker | claudeopus46 | 1,323 | 5,080 | 6,403 | 617 | 6.1 |
| 39 | L1-worker | claudeopus46 | 1,356 | 2,095 | 3,451 | 729 | 7.0 |
| 40 | L1-worker | claudeopus46 | 536 | 1,975 | 2,511 | 713 | 7.2 |
| 41 | L1-worker | claudeopus46 | 298 | 1,339 | 1,637 | 490 | 3.5 |
| 42 | L1-worker | claudeopus46 | 298 | 1,111 | 1,409 | 717 | 3.5 |
| 43 | L1-worker | claudeopus46 | 747 | 13,288 | 14,035 | 712 | 7.4 |
| 44 | L1-worker | claudeopus46 | 20,643 | 11,145 | 31,788 | 782 | 6.5 |
| 45 | L1-worker | claudeopus46 | 2,065 | 2,563 | 4,628 | 1,633 | 11.4 |
| 46 | L1-worker | claudeopus46 | 20,643 | 12,827 | 33,470 | 1,942 | 12.1 |
| 47 | L1-worker | claudeopus46 | 1,323 | 4,955 | 6,278 | 589 | 3.7 |
| 48 | L1-worker | claudeopus46 | 1,356 | 2,073 | 3,429 | 872 | 4.7 |
| 49 | L1-worker | claudeopus46 | 536 | 1,953 | 2,489 | 676 | 5.5 |
| 50 | L1-worker | claudeopus46 | 298 | 1,311 | 1,609 | 462 | 3.1 |
| 51 | L1-worker | claudeopus46 | 747 | 12,640 | 13,387 | 499 | 5.6 |
| 52 | L0-main | claudeopus46 | 9,605 | 26,358 | 35,963 | 3,172 | 16.5 |
| 53 | L1-worker | claudeopus46 | 20,643 | 20,387 | 41,030 | 696 | 5.4 |
| 54 | L1-worker | claudeopus46 | 2,065 | 7,834 | 9,899 | 1,689 | 14.8 |
| 55 | L1-worker | claudeopus46 | 20,643 | 21,991 | 42,634 | 936 | 7.2 |
| 56 | L1-worker | claudeopus46 | 2,065 | 9,796 | 11,861 | 1,672 | 16.9 |
| 57 | L1-worker | claudeopus46 | 20,643 | 23,718 | 44,361 | 2,746 | 17.8 |
| 58 | L1-worker | claudeopus46 | 2,065 | 9,766 | 11,831 | 1,406 | 15.7 |
| 59 | L1-worker | claudeopus46 | 20,610 | 26,341 | 46,951 | 392 | 5.0 |
| 60 | L1-worker | claudeopus46 | 20,643 | 25,588 | 46,231 | 2,742 | 21.3 |
| 61 | L1-worker | claudeopus46 | 2,065 | 7,902 | 9,967 | 1,587 | 12.3 |
| 62 | L1-worker | claudeopus46 | 20,643 | 26,536 | 47,179 | 2,361 | 15.5 |
| 63 | L1-worker | claudeopus46 | 2,065 | 2,864 | 4,929 | 1,735 | 13.8 |
| 64 | L1-worker | claudeopus46 | 20,643 | 28,245 | 48,888 | 1,866 | 15.0 |
| 65 | L1-worker | claudeopus46 | 2,065 | 2,703 | 4,768 | 1,895 | 14.7 |
| 66 | L1-worker | claudeopus46 | 20,610 | 30,590 | 51,200 | 343 | 5.6 |
| 67 | L1-worker | claudeopus46 | 20,643 | 29,835 | 50,478 | 878 | 6.9 |
| 68 | L1-worker | claudeopus46 | 2,065 | 2,739 | 4,804 | 1,756 | 12.2 |
| 69 | L1-worker | claudeopus46 | 20,643 | 31,479 | 52,122 | 717 | 5.4 |
| 70 | L1-worker | claudeopus46 | 2,065 | 2,669 | 4,734 | 1,779 | 12.6 |
| 71 | L1-worker | claudeopus46 | 20,643 | 33,302 | 53,945 | 4,154 | 29.1 |
| 72 | L1-worker | claudeopus46 | 1,356 | 2,699 | 4,055 | 938 | 6.3 |
| 73 | L1-worker | claudeopus46 | 536 | 2,579 | 3,115 | 1,256 | 8.6 |
| 74 | L1-worker | claudeopus46 | 298 | 1,320 | 1,618 | 926 | 3.6 |
| 75 | L1-worker | claudeopus46 | 1,323 | 16,817 | 18,140 | 4,062 | 20.0 |
| 76 | L1-worker | claudeopus46 | 298 | 4,784 | 5,082 | 3,385 | 15.9 |
| 77 | L1-worker | claudeopus46 | 1,160 | 21,824 | 22,984 | 3,054 | 14.1 |
| 78 | L1-worker | claudeopus46 | 747 | 78,638 | 79,385 | 754 | 7.6 |
| 79 | L1-worker | claudeopus46 | 20,643 | 20,129 | 40,772 | 724 | 5.9 |
| 80 | L1-worker | claudeopus46 | 2,065 | 498 | 2,563 | 905 | 7.2 |
| 81 | L1-worker | claudeopus46 | 20,643 | 21,306 | 41,949 | 769 | 6.1 |
| 82 | L1-worker | claudeopus46 | 2,065 | 409 | 2,474 | 865 | 6.0 |
| 83 | L1-worker | claudeopus46 | 20,643 | 22,506 | 43,149 | 2,205 | 15.4 |
| 84 | L1-worker | claudeopus46 | 2,065 | 493 | 2,558 | 1,209 | 10.1 |
| 85 | L1-worker | claudeopus46 | 20,610 | 24,652 | 45,262 | 604 | 6.6 |
| 86 | L1-worker | claudeopus46 | 20,643 | 23,899 | 44,542 | 793 | 6.9 |
| 87 | L1-worker | claudeopus46 | 1,356 | 924 | 2,280 | 355 | 3.5 |
| 88 | L1-worker | claudeopus46 | 1,323 | 5,411 | 6,734 | 92 | 3.7 |
| 89 | L1-worker | claudeopus46 | 536 | 804 | 1,340 | 534 | 4.0 |
| 90 | L1-worker | claudeopus46 | 298 | 814 | 1,112 | 67 | 3.1 |
| 91 | L1-worker | claudeopus46 | 747 | 6,023 | 6,770 | 475 | 6.4 |
| 92 | L1-worker | claudeopus46 | 20,643 | 22,038 | 42,681 | 797 | 6.1 |
| 93 | L1-worker | claudeopus46 | 2,065 | 527 | 2,592 | 954 | 6.7 |
| 94 | L1-worker | claudeopus46 | 20,643 | 23,301 | 43,944 | 1,158 | 7.3 |
| 95 | L1-worker | claudeopus46 | 2,065 | 14,148 | 16,213 | 1,562 | 13.0 |
| 96 | L1-worker | claudeopus46 | 2,065 | 9,701 | 11,766 | 1,753 | 13.5 |
| 97 | L1-worker | claudeopus46 | 20,643 | 26,849 | 47,492 | 2,783 | 15.2 |
| 98 | L1-worker | claudeopus46 | 536 | 1,712 | 2,248 | 740 | 7.9 |
| 99 | L1-worker | claudeopus46 | 1,356 | 1,832 | 3,188 | 613 | 8.1 |
| 100 | L1-worker | claudeopus46 | 1,323 | 7,786 | 9,109 | 92 | 10.2 |
| 101 | L1-worker | claudeopus46 | 298 | 814 | 1,112 | 67 | 6.0 |
| 102 | L1-worker | claudeopus46 | 747 | 9,770 | 10,517 | 588 | 5.2 |
| 103 | L0-main | claudeopus46 | 9,572 | 9,405 | 18,977 | 4,704 | 27.3 |
| 104 | L0-main | claudeopus46 | 1,356 | 3,856 | 5,212 | 946 | 5.4 |
| 105 | L0-main | claudeopus46 | 1,323 | 42,032 | 43,355 | 2,845 | 17.7 |
| 106 | L0-main | claudeopus46 | 298 | 3,513 | 3,811 | 2,393 | 9.0 |

