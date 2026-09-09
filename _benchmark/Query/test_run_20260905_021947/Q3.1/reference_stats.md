# Reference Stats — query-agent

**Run started:** 2026-09-05 05:28:51
**Wall time (at last flush):** 504.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 30,402 | 96,988 | 26,923 | 127,390 | 14,154 | 136.6 | claudeopus46 |
| L1-worker | 29 | 377,739 | 351,082 | 58,164 | 728,821 | 25,131 | 382.5 | claudeopus46 |
| **TOTAL** | **38** | **408,141** | **448,070** | **85,087** | **856,211** | **22,531** | **519.1** | |

**Estimated tokens:** ~214,052 input + ~21,271 output = ~235,323 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `search_system_registry` | 82 | 1 | 6 | 5 | 39 | 100 | 5,858 |
| `search_system_registry` | 89 | 1 | 6 | 4 | 35 | 100 | 4,300 |
| `block_search_adv` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 185 |
| `search_blocks` | 5 | 2 | 2 | 1 | 1 | 8 | 727 |
| `search_blocks` | 5 | 1 | 2 | 1 | 1 | 6 | 546 |
| `search_blocks` | 4 | 2 | 3 | 0 | 1 | 6 | 448 |
| `search_blocks` | 2 | 1 | 3 | 0 | 1 | 1 | 270 |
| `search_blocks` | 2 | 3 | 2 | 1 | 1 | 3 | 330 |
| **TOTAL** | **191** | **12** | **27** | **12** | **80** | **225** | **12,664** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### References (59 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_4 |  | search_system_registry |
| GLOBlit_5 |  | search_system_registry |
| GLOBlit_6 |  | search_system_registry |
| GLOBlit_11 |  | search_system_registry |
| GLOBlit_12 |  | search_system_registry |
| GLOBlit_14 |  | search_system_registry |
| GLOBlit_15 |  | search_system_registry |
| GLOBlit_16 |  | search_system_registry |
| GLOBlit_25 |  | search_blocks, search_system_registry |
| GLOBlit_26 |  | search_system_registry |
| GLOBlit_35 |  | search_system_registry |
| GLOBlit_37 |  | search_system_registry |
| GLOBlit_48 |  | search_system_registry |
| GLOBlit_49 |  | search_system_registry |
| GLOBlit_50 |  | search_system_registry |
| GLOBlit_53 |  | search_system_registry |
| GLOBlit_56 |  | search_system_registry |
| GLOBlit_57 |  | search_system_registry |
| GLOBlit_58 |  | search_system_registry |
| GLOBlit_59 |  | search_blocks, search_system_registry |
| GLOBlit_60 |  | search_system_registry |
| GLOBlit_62 |  | search_system_registry |
| GLOBlit_67 |  | search_system_registry |
| GLOBlit_68 |  | search_system_registry |
| GLOBlit_69 |  | search_system_registry |
| GLOBlit_71 |  | search_system_registry |
| GLOBlit_73 |  | search_system_registry |
| GLOBlit_76 |  | search_system_registry |
| GLOBlit_78 |  | search_system_registry |
| GLOBlit_80 |  | search_system_registry |
| GLOBlit_81 |  | search_system_registry |
| GLOBlit_84 |  | search_system_registry |
| GLOBlit_86 |  | search_system_registry |
| GLOBlit_87 |  | search_system_registry |
| GLOBlit_88 |  | search_system_registry |
| GLOBlit_89 |  | search_system_registry |
| GLOBlit_94 |  | search_system_registry |
| GLOBlit_96 |  | search_system_registry |
| GLOBlit_97 |  | search_blocks, search_system_registry |
| GLOBlit_2 |  | search_system_registry |
| GLOBlit_8 |  | search_blocks, search_system_registry |
| GLOBlit_23 |  | search_system_registry |
| GLOBlit_98 |  | search_system_registry |
| GLOBlit_99 |  | search_system_registry |
| GLOBlit_105 |  | search_system_registry |
| GLOBlit_113 |  | search_system_registry |
| GLOBlit_119 |  | search_system_registry |
| GLOBlit_120 |  | search_system_registry |
| GLOBlit_121 |  | search_system_registry |
| GLOBlit_126 |  | search_system_registry |
| GLOBlit_128 |  | search_system_registry |
| GLOBlit_129 |  | search_system_registry |
| GLOBlit_130 |  | search_system_registry |
| GLOBlit_145 |  | search_blocks, search_system_registry |
| GLOBlit_151 |  | search_blocks, search_system_registry |
| GLOBlit_155 |  | search_system_registry |
| GLOBlit_156 |  | search_system_registry |
| GLOBlit_169 |  | search_system_registry |
| GLOBlit_178 |  | search_system_registry |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | search_system_registry |

#### Compounds (120 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_595 | dibromomethane | search_system_registry |
| GLOBcomp_10 | ethyl acetate | search_system_registry |
| GLOBcomp_995 | bromochloromethane | search_system_registry |
| GLOBcomp_86 | 1,2-dichloroethane | search_system_registry |
| GLOBcomp_1355 | 1-bromo-2-chloroethane | search_system_registry |
| GLOBcomp_299 | 3-methylbutyl ethanoate | search_system_registry |
| GLOBcomp_643 | butyl 2-propenoate | search_system_registry |
| GLOBcomp_783 | ethyl propenoate | search_system_registry |
| GLOBcomp_376 | methyl methacrylate | search_system_registry |
| GLOBcomp_108 | styrene | search_system_registry |
| GLOBcomp_12 | hexane | search_blocks, search_system_registry |
| GLOBcomp_13 | cyclohexane | search_system_registry |
| GLOBcomp_21 | decane | search_system_registry |
| GLOBcomp_71 | hexadecane | search_system_registry |
| GLOBcomp_284 | 2,6,10,15,19,23-hexamethyltetracosane | search_blocks, search_system_registry |
| GLOBcomp_6 | propan-2-ol | search_system_registry |
| GLOBcomp_5 | propan-1-ol | search_system_registry |
| GLOBcomp_7 | butan-1-ol | search_blocks, search_system_registry |
| GLOBcomp_34 | octan-1-ol | search_system_registry |
| GLOBcomp_38 | hexan-1-ol | search_system_registry |
| GLOBcomp_31 | dimethyl sulfoxide | search_system_registry |
| GLOBcomp_77 | heptan-1-ol | search_system_registry |
| GLOBcomp_199 | ammonia | search_system_registry |
| GLOBcomp_1 | water | search_system_registry |
| GLOBcomp_127 | difluoromethane | search_system_registry |
| GLOBcomp_147 | pentafluoroethane | search_system_registry |
| GLOBcomp_57 | propane | search_system_registry |
| GLOBcomp_98 | 2-methylpropane | search_system_registry |
| GLOBcomp_102 | butane | search_blocks, search_system_registry |
| GLOBcomp_17 | octane | search_blocks, search_system_registry |
| GLOBcomp_3 | carbon dioxide | search_system_registry |
| GLOBcomp_14 | benzene | search_system_registry |
| GLOBcomp_202 | triethylamine | search_system_registry |
| GLOBcomp_357 | tributylamine | search_system_registry |
| GLOBcomp_156 | tetrahydropyran | search_system_registry |
| GLOBcomp_328 | 2-chloro-2-methylpropane | search_blocks, search_system_registry |
| GLOBcomp_307 | 2-chlorobutane | search_blocks, search_system_registry |
| GLOBcomp_361 | 1-chloro-2-methylpropane | search_blocks, search_system_registry |
| GLOBcomp_131 | 1-chlorobutane | search_blocks, search_system_registry |
| GLOBcomp_144 | aniline | search_system_registry |
| GLOBcomp_29 | 2-methyl-1-propanol | search_system_registry |
| GLOBcomp_44 | 2-methylpropan-2-ol | search_system_registry |
| GLOBcomp_208 | 1,3-dioxolane | search_system_registry |
| GLOBcomp_48 | 2-methoxy-2-methylpropane | search_blocks, search_system_registry |
| GLOBcomp_8 | toluene | search_blocks, search_system_registry |
| GLOBcomp_27 | ethylbenzene | search_system_registry |
| GLOBcomp_37 | 2,2,4-trimethylpentane | search_system_registry |
| GLOBcomp_40 | trichloromethane | search_system_registry |
| GLOBcomp_4 | methanol | search_system_registry |
| GLOBcomp_36 | 1-butyl-3-methylimidazolium tetrafluoroborate | search_blocks, search_system_registry |
| GLOBcomp_15 | acetonitrile | search_system_registry |
| GLOBcomp_63 | N,N-dimethylethanamide | search_system_registry |
| GLOBcomp_23 | tetrahydrofuran | search_system_registry |
| GLOBcomp_96 | chlorobenzene | search_system_registry |
| GLOBcomp_113 | triethylene glycol | search_system_registry |
| GLOBcomp_197 | bromobenzene | search_system_registry |
| GLOBcomp_170 | nitrobenzene | search_system_registry |
| GLOBcomp_111 | diethylene glycol | search_system_registry |
| GLOBcomp_2 | ethanol | search_blocks, search_system_registry |
| GLOBcomp_41 | potassium chloride | search_system_registry |
| GLOBcomp_233 | potassium nitrate | search_system_registry |
| GLOBcomp_641 | methyl propenoate | search_system_registry |
| GLOBcomp_352 | 1,3-benzenediol | search_system_registry |
| GLOBcomp_628 | chlorodifluoromethane | search_system_registry |
| GLOBcomp_1597 | 1-chloro-1,1-difluoroethane | search_system_registry |
| GLOBcomp_269 | 1-butanamine | search_system_registry |
| GLOBcomp_1046 | 1-(1-methyl-2-propoxyethoxy)-2-propanol | search_system_registry |
| GLOBcomp_358 | dibutylamine | search_system_registry |
| GLOBcomp_30 | 1,2-dimethylbenzene | search_system_registry |
| GLOBcomp_28 | 1,4-dimethylbenzene | search_system_registry |
| GLOBcomp_491 | 1-methyl-3-propylimidazolium bromide | search_system_registry |
| GLOBcomp_18 | dimethylformamide | search_system_registry |
| GLOBcomp_1358 | 1,3-dimethylimidazolium chloride | search_system_registry |
| GLOBcomp_11 | heptane | search_system_registry |
| GLOBcomp_85 | cyclooctane | search_system_registry |
| GLOBcomp_140 | 2-ethoxyethan-1-ol | search_system_registry |
| GLOBcomp_89 | 3-methylbutan-1-ol | search_system_registry |
| GLOBcomp_118 | 2-methoxyethan-1-ol | search_system_registry |
| GLOBcomp_189 | 2-butoxyethan-1-ol | search_system_registry |
| GLOBcomp_821 | cis-1,4-butenedioic acid | search_system_registry |
| GLOBcomp_2259 | 2,3-dihydroxybutanedioic acid | search_system_registry |
| GLOBcomp_52 | diisopropyl ether | search_blocks, search_system_registry |
| GLOBcomp_168 | potassium sulfate | search_system_registry |
| GLOBcomp_32 | 1,3-dimethylbenzene | search_system_registry |
| GLOBcomp_291 | (+)-galactose | search_system_registry |
| GLOBcomp_283 | cyclohexylamine | search_system_registry |
| GLOBcomp_65 | butyl ethanoate | search_system_registry |
| GLOBcomp_39 | butanone | search_system_registry |
| GLOBcomp_940 | 2-methyl-2-propanamine | search_system_registry |
| GLOBcomp_87 | cyclohexanone | search_system_registry |
| GLOBcomp_146 | 4-methyl-1,3-dioxolan-2-one | search_system_registry |
| GLOBcomp_25 | 1,4-dioxane | search_system_registry |
| GLOBcomp_379 | 2,4-pentanedione | search_system_registry |
| GLOBcomp_576 | 1-chloropentane | search_system_registry |
| GLOBcomp_391 | 1-chlorohexane | search_system_registry |
| GLOBcomp_1315 | 1-chloroheptane | search_system_registry |
| GLOBcomp_696 | 1-chlorooctane | search_system_registry |
| GLOBcomp_1514 | dimethyl methanephosphonate | search_system_registry |
| GLOBcomp_1713 | dimethyl phosphonate | search_system_registry |
| GLOBcomp_408 | 2-chlorotoluene | search_system_registry |
| GLOBcomp_59 | decan-1-ol | search_system_registry |
| GLOBcomp_664 | 3-chlorotoluene | search_system_registry |
| GLOBcomp_473 | 4-chlorotoluene | search_system_registry |
| GLOBcomp_389 | 2-amino-2-(hydroxymethyl)-1,3-propanediol | search_system_registry |
| GLOBcomp_264 | 1,2-dichlorobenzene | search_system_registry |
| GLOBcomp_544 | 2-octanol | search_system_registry |
| GLOBcomp_419 | 1,3-dichlorobenzene | search_system_registry |
| GLOBcomp_728 | 1,2,4-trichlorobenzene | search_system_registry |
| GLOBcomp_612 | 2,6-dimethylpyridine | search_system_registry |
| GLOBcomp_365 | 2-methylpyridine | search_system_registry |
| GLOBcomp_246 | sodium ethanoate | search_system_registry |
| GLOBcomp_375 | potassium ethanoate | search_system_registry |
| GLOBcomp_1515 | calcium acetate | search_system_registry |
| GLOBcomp_803 | butyl ethyl ether | search_blocks, search_system_registry |
| GLOBcomp_247 | 2,5,8,11,14-pentaoxapentadecane | search_blocks, search_system_registry |
| GLOBcomp_271 | benzaldehyde | search_system_registry |
| GLOBcomp_255 | 2-ethyl-1-hexanol | search_system_registry |
| GLOBcomp_235 | trichloroethene | search_system_registry |
| GLOBcomp_115 | propyl ethanoate | search_system_registry |
| GLOBcomp_551 | copper sulfate | search_system_registry |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_3 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBvar_1 | Temperature, K | search_blocks, search_system_registry |
| GLOBvar_2 | Mole fraction | search_blocks, search_system_registry |
| GLOBvar_5 | Mass fraction | search_system_registry |
| GLOBvar_4 | Molality, mol/kg | search_system_registry |
| GLOBvar_9 | Amount concentration (molarity), mol/dm3 | search_system_registry |

#### Phases (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_blocks, search_system_registry |
| GLOBphase_10 |  | search_system_registry |
| GLOBphase_3 |  | search_system_registry |

#### Properties (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_1 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBprop_4 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBprop_7 | Refractive index (Na D-line) | search_blocks |

#### Measurements (30 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_143 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_138 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_153 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_141 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_167 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_66 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_170 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_791 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_437 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_2 | Mass density, kg/m3 | search_blocks, search_system_registry |
| GLOBmeas_6 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_1662 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_147 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_280 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_56 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_179 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_184 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_4 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_165 | Viscosity, Pa*s | search_system_registry |
| GLOBmeas_8 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_75 | Viscosity, Pa*s | search_system_registry |
| GLOBmeas_140 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_142 | Viscosity, Pa*s | search_system_registry |
| GLOBmeas_271 | Viscosity, Pa*s | search_system_registry |
| GLOBmeas_308 | Viscosity, Pa*s | search_system_registry |
| GLOBmeas_11 | Viscosity, Pa*s | search_blocks, search_system_registry |
| GLOBmeas_205 | Viscosity, Pa*s | search_system_registry |
| GLOBmeas_227 | Viscosity, Pa*s | search_system_registry |
| GLOBmeas_3 | Refractive index (Na D-line) | search_blocks |

#### Constraints (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_2 | Temperature, K | search_system_registry |
| GLOBconstr_1 | Pressure, kPa | search_blocks, search_system_registry |
| GLOBconstr_12 | Amount concentration (molarity), mol/dm3 | search_system_registry |
| GLOBconstr_5 | Mass fraction | search_system_registry |
| GLOBconstr_3 | Mole fraction | search_system_registry |
| GLOBconstr_8 | Molality, mol/kg | search_system_registry |

#### Solvents (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_3 |  | search_system_registry |
| GLOBsolvent_5 |  | search_system_registry |
| GLOBsolvent_8 |  | search_system_registry |
| GLOBsolvent_21 |  | search_system_registry |
| GLOBsolvent_24 |  | search_system_registry |
| GLOBsolvent_1 |  | search_system_registry |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique References | 59 |
| Unique Block_Types | 1 |
| Unique Compounds | 120 |
| Unique Variables | 6 |
| Unique Phases | 3 |
| Unique Properties | 3 |
| Unique Measurements | 30 |
| Unique Constraints | 6 |
| Unique Solvents | 6 |
| Total DOIs | 59 |
| Unique parent blocks | 204 |
| Explicit block/subsystem targets | 204 |
| Subsystem targets | 0 |
| Target-matched data points | 12,664 |

---

## 3. DOI & Block References

**Unique DOIs:** 59  |  **Parent blocks:** 204  |  **Explicit targets:** 204  |  **Subsystems:** 0  |  **Target-matched datapoints:** 10,560

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1007/s10765-005-5567-5 | 1 | 172 | binary | search_system_registry |
| 10.1007/s10765-005-5570-x | 4 | 341 | binary | search_system_registry |
| 10.1007/s10765-005-5571-9 | 4 | 92 | binary | search_system_registry |
| 10.1007/s10765-005-5572-8 | 8 | 122 | binary | search_system_registry |
| 10.1007/s10765-005-8089-2 | 1 | 185 | binary | search_blocks, search_system_registry |
| 10.1007/s10765-005-8101-x | 4 | 40 | binary | search_system_registry |
| 10.1007/s10765-005-8102-9 | 3 | 33 | binary | search_system_registry |
| 10.1007/s10765-005-8590-7 | 1 | 277 | binary | search_system_registry |
| 10.1007/s10765-005-8591-6 | 1 | 102 | binary | search_system_registry |
| 10.1007/s10765-005-8592-5 | 1 | 85 | binary | search_system_registry |
| 10.1007/s10765-006-0051-4 | 1 | 246 | binary | search_system_registry |
| 10.1007/s10765-006-0053-2 | 6 | 448 | binary | search_blocks, search_system_registry |
| 10.1007/s10765-006-0056-z | 2 | 31 | binary | search_system_registry |
| 10.1007/s10765-006-0095-5 | 2 | 182 | binary | search_system_registry |
| 10.1007/s10765-006-0100-z | 4 | 104 | binary | search_system_registry |
| 10.1007/s10765-007-0204-0 | 4 | 504 | binary | search_system_registry |
| 10.1007/s10765-007-0220-0 | 2 | 24 | binary | search_system_registry |
| 10.1007/s10765-007-0223-x | 5 | 906 | binary | search_system_registry |
| 10.1007/s10765-007-0259-y | 2 | 160 | binary | search_system_registry |
| 10.1007/s10765-008-0390-4 | 2 | 264 | binary | search_system_registry |
| 10.1007/s10765-008-0395-z | 5 | 51 | binary | search_system_registry |
| 10.1007/s10765-008-0399-8 | 8 | 264 | binary | search_system_registry |
| 10.1007/s10765-008-0410-4 | 1 | 270 | binary | search_blocks, search_system_registry |
| 10.1007/s10765-008-0444-7 | 4 | 132 | binary | search_system_registry |
| 10.1007/s10765-008-0491-0 | 4 | 192 | binary | search_system_registry |
| 10.1007/s10765-008-0514-x | 2 | 12 | binary | search_system_registry |
| 10.1007/s10765-008-0535-5 | 1 | 194 | binary | search_system_registry |
| 10.1007/s10765-008-0542-6 | 2 | 8 | binary | search_system_registry |
| 10.1007/s10765-009-0562-x | 8 | 352 | binary | search_system_registry |
| 10.1007/s10765-009-0567-5 | 2 | 24 | binary | search_system_registry |
| 10.1007/s10765-009-0579-1 | 2 | 474 | binary | search_system_registry |
| 10.1007/s10765-009-0581-7 | 1 | 80 | binary | search_system_registry |
| 10.1007/s10765-009-0593-3 | 3 | 270 | binary | search_system_registry |
| 10.1007/s10765-009-0602-6 | 1 | 39 | binary | search_system_registry |
| 10.1007/s10765-009-0622-2 | 6 | 84 | binary | search_system_registry |
| 10.1007/s10765-009-0648-5 | 3 | 210 | binary | search_system_registry |
| 10.1007/s10765-009-0651-x | 1 | 48 | binary | search_system_registry |
| 10.1007/s10765-009-0665-4 | 2 | 24 | binary | search_system_registry |
| 10.1007/s10765-009-0667-2 | 20 | 440 | binary | search_system_registry |
| 10.1007/s10765-010-0719-7 | 6 | 198 | binary | search_system_registry |
| 10.1007/s10765-010-0736-6 | 2 | 28 | binary | search_system_registry |
| 10.1007/s10765-010-0737-5 | 8 | 727 | binary | search_blocks, search_system_registry |
| 10.1007/s10765-010-0742-8 | 1 | 4 | binary | search_system_registry |
| 10.1007/s10765-010-0752-6 | 10 | 110 | binary | search_system_registry |
| 10.1007/s10765-010-0860-3 | 3 | 135 | binary | search_system_registry |
| 10.1007/s10765-010-0902-x | 5 | 72 | binary | search_system_registry |
| 10.1007/s10765-011-0989-8 | 2 | 154 | binary | search_system_registry |
| 10.1007/s10765-011-0995-x | 3 | 144 | binary | search_system_registry |
| 10.1007/s10765-011-0996-9 | 2 | 12 | binary | search_system_registry |
| 10.1007/s10765-011-1065-0 | 1 | 40 | binary | search_system_registry |
| 10.1007/s10765-011-1087-7 | 3 | 138 | binary | search_system_registry |
| 10.1007/s10765-011-1100-1 | 3 | 135 | binary | search_system_registry |
| 10.1007/s10765-011-1111-y | 3 | 16 | binary | search_system_registry |
| 10.1007/s10765-012-1371-1 | 6 | 546 | binary | search_blocks, search_system_registry |
| 10.1007/s10765-013-1469-0 | 3 | 330 | binary | search_blocks, search_system_registry |
| 10.1007/s10765-013-1492-1 | 2 | 66 | binary | search_system_registry |
| 10.1007/s10765-013-1526-8 | 3 | 144 | binary | search_system_registry |
| 10.1007/s10765-015-1927-y | 3 | 30 | binary | search_system_registry |
| 10.1007/s10765-016-2089-2 | 1 | 45 | binary | search_system_registry |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1007/s10765-005-5567-5 | PROPblock_4 | declared | 172 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5570-x | PROPblock_11 | declared | 85 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5570-x | PROPblock_12 | declared | 85 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5570-x | PROPblock_13 | declared | 84 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5570-x | PROPblock_14 | declared | 87 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5571-9 | PROPblock_6 | declared | 23 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5571-9 | PROPblock_7 | declared | 23 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5571-9 | PROPblock_8 | declared | 23 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5571-9 | PROPblock_9 | declared | 23 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5572-8 | PROPblock_16 | declared | 15 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5572-8 | PROPblock_17 | declared | 15 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5572-8 | PROPblock_18 | declared | 15 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5572-8 | PROPblock_20 | declared | 15 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5572-8 | PROPblock_21 | declared | 15 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5572-8 | PROPblock_23 | declared | 15 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5572-8 | PROPblock_24 | declared | 16 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-5572-8 | PROPblock_26 | declared | 16 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-8089-2 | PROPblock_3 | declared | 185 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-005-8101-x | PROPblock_12 | declared | 10 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-8101-x | PROPblock_14 | declared | 10 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-8101-x | PROPblock_16 | declared | 10 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-8101-x | PROPblock_18 | declared | 10 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-8102-9 | PROPblock_15 | declared | 11 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-8102-9 | PROPblock_18 | declared | 11 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-8102-9 | PROPblock_21 | declared | 11 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-8590-7 | PROPblock_2 | declared | 277 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-8591-6 | PROPblock_3 | declared | 102 | binary | 2 | search_system_registry |
| 10.1007/s10765-005-8592-5 | PROPblock_4 | declared | 85 | binary | 2 | search_system_registry |
| 10.1007/s10765-006-0051-4 | PROPblock_1 | declared | 246 | binary | 2 | search_system_registry |
| 10.1007/s10765-006-0053-2 | PROPblock_10 | declared | 80 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-006-0053-2 | PROPblock_11 | declared | 64 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-006-0053-2 | PROPblock_12 | declared | 64 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-006-0053-2 | PROPblock_13 | declared | 80 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-006-0053-2 | PROPblock_14 | declared | 80 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-006-0053-2 | PROPblock_9 | declared | 80 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-006-0056-z | PROPblock_5 | declared | 7 | binary | 2 | search_system_registry |
| 10.1007/s10765-006-0056-z | PROPblock_6 | declared | 24 | binary | 2 | search_system_registry |
| 10.1007/s10765-006-0095-5 | PROPblock_10 | declared | 91 | binary | 2 | search_system_registry |
| 10.1007/s10765-006-0095-5 | PROPblock_8 | declared | 91 | binary | 2 | search_system_registry |
| 10.1007/s10765-006-0100-z | PROPblock_12 | declared | 26 | binary | 2 | search_system_registry |
| 10.1007/s10765-006-0100-z | PROPblock_14 | declared | 26 | binary | 2 | search_system_registry |
| 10.1007/s10765-006-0100-z | PROPblock_16 | declared | 26 | binary | 2 | search_system_registry |
| 10.1007/s10765-006-0100-z | PROPblock_18 | declared | 26 | binary | 2 | search_system_registry |
| 10.1007/s10765-007-0204-0 | PROPblock_6 | declared | 126 | binary | 2 | search_system_registry |
| 10.1007/s10765-007-0204-0 | PROPblock_7 | declared | 126 | binary | 2 | search_system_registry |
| 10.1007/s10765-007-0204-0 | PROPblock_8 | declared | 126 | binary | 2 | search_system_registry |
| 10.1007/s10765-007-0204-0 | PROPblock_9 | declared | 126 | binary | 2 | search_system_registry |
| 10.1007/s10765-007-0220-0 | PROPblock_1 | declared | 12 | binary | 2 | search_system_registry |
| 10.1007/s10765-007-0220-0 | PROPblock_2 | declared | 12 | binary | 2 | search_system_registry |
| 10.1007/s10765-007-0223-x | PROPblock_14 | declared | 191 | binary | 2 | search_system_registry |
| 10.1007/s10765-007-0223-x | PROPblock_16 | declared | 195 | binary | 2 | search_system_registry |
| 10.1007/s10765-007-0223-x | PROPblock_18 | declared | 195 | binary | 2 | search_system_registry |
| 10.1007/s10765-007-0223-x | PROPblock_20 | declared | 195 | binary | 2 | search_system_registry |
| 10.1007/s10765-007-0223-x | PROPblock_22 | declared | 130 | binary | 2 | search_system_registry |
| 10.1007/s10765-007-0259-y | PROPblock_3 | declared | 80 | binary | 2 | search_system_registry |
| 10.1007/s10765-007-0259-y | PROPblock_4 | declared | 80 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0390-4 | PROPblock_4 | declared | 126 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0390-4 | PROPblock_5 | declared | 138 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0395-z | PROPblock_13 | declared | 12 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0395-z | PROPblock_14 | declared | 11 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0395-z | PROPblock_15 | declared | 9 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0395-z | PROPblock_16 | declared | 12 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0395-z | PROPblock_17 | declared | 7 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0399-8 | PROPblock_16 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0399-8 | PROPblock_18 | declared | 44 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0399-8 | PROPblock_19 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0399-8 | PROPblock_21 | declared | 44 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0399-8 | PROPblock_22 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0399-8 | PROPblock_24 | declared | 44 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0399-8 | PROPblock_25 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0399-8 | PROPblock_27 | declared | 44 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0410-4 | PROPblock_2 | declared | 270 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-008-0444-7 | PROPblock_10 | declared | 33 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0444-7 | PROPblock_7 | declared | 33 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0444-7 | PROPblock_8 | declared | 33 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0444-7 | PROPblock_9 | declared | 33 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0491-0 | PROPblock_1 | declared | 48 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0491-0 | PROPblock_3 | declared | 48 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0491-0 | PROPblock_4 | declared | 48 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0491-0 | PROPblock_6 | declared | 48 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0514-x | PROPblock_2 | declared | 6 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0514-x | PROPblock_4 | declared | 6 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0535-5 | PROPblock_4 | declared | 194 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0542-6 | PROPblock_10 | declared | 4 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0542-6 | PROPblock_8 | declared | 4 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0562-x | PROPblock_21 | declared | 44 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0562-x | PROPblock_24 | declared | 44 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0562-x | PROPblock_25 | declared | 44 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0562-x | PROPblock_28 | declared | 44 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0562-x | PROPblock_29 | declared | 44 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0562-x | PROPblock_32 | declared | 44 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0562-x | PROPblock_33 | declared | 44 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0562-x | PROPblock_36 | declared | 44 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0567-5 | PROPblock_1 | declared | 12 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0567-5 | PROPblock_2 | declared | 12 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0579-1 | PROPblock_1 | declared | 237 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0579-1 | PROPblock_2 | declared | 237 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0581-7 | PROPblock_6 | declared | 80 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0593-3 | PROPblock_10 | declared | 90 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0593-3 | PROPblock_12 | declared | 90 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0593-3 | PROPblock_14 | declared | 90 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0602-6 | PROPblock_2 | declared | 39 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0622-2 | PROPblock_11 | declared | 17 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0622-2 | PROPblock_12 | declared | 14 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0622-2 | PROPblock_13 | declared | 14 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0622-2 | PROPblock_14 | declared | 13 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0622-2 | PROPblock_15 | declared | 13 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0622-2 | PROPblock_16 | declared | 13 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0648-5 | PROPblock_10 | declared | 75 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0648-5 | PROPblock_12 | declared | 70 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0648-5 | PROPblock_14 | declared | 65 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0651-x | PROPblock_3 | declared | 48 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0665-4 | PROPblock_6 | declared | 12 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0665-4 | PROPblock_8 | declared | 12 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_11 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_12 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_13 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_14 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_15 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_16 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_17 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_18 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_19 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_20 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_21 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_22 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_23 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_24 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_25 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_26 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_27 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_28 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_29 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0667-2 | PROPblock_30 | declared | 22 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0719-7 | PROPblock_17 | declared | 33 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0719-7 | PROPblock_20 | declared | 33 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0719-7 | PROPblock_21 | declared | 33 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0719-7 | PROPblock_24 | declared | 33 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0719-7 | PROPblock_25 | declared | 33 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0719-7 | PROPblock_28 | declared | 33 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0736-6 | PROPblock_2 | declared | 14 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0736-6 | PROPblock_4 | declared | 14 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0737-5 | PROPblock_11 | declared | 91 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-010-0737-5 | PROPblock_12 | declared | 91 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-010-0737-5 | PROPblock_13 | declared | 91 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-010-0737-5 | PROPblock_14 | declared | 90 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-010-0737-5 | PROPblock_15 | declared | 91 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-010-0737-5 | PROPblock_16 | declared | 91 | binary | — | search_blocks |
| 10.1007/s10765-010-0737-5 | PROPblock_17 | declared | 91 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-010-0737-5 | PROPblock_18 | declared | 91 | binary | — | search_blocks |
| 10.1007/s10765-010-0742-8 | PROPblock_1 | declared | 4 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0752-6 | PROPblock_22 | declared | 11 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0752-6 | PROPblock_25 | declared | 11 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0752-6 | PROPblock_28 | declared | 11 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0752-6 | PROPblock_31 | declared | 11 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0752-6 | PROPblock_34 | declared | 11 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0752-6 | PROPblock_37 | declared | 11 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0752-6 | PROPblock_40 | declared | 11 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0752-6 | PROPblock_43 | declared | 11 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0752-6 | PROPblock_46 | declared | 11 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0752-6 | PROPblock_49 | declared | 11 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0860-3 | PROPblock_11 | declared | 45 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0860-3 | PROPblock_13 | declared | 45 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0860-3 | PROPblock_9 | declared | 45 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0902-x | PROPblock_13 | declared | 17 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0902-x | PROPblock_16 | declared | 13 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0902-x | PROPblock_19 | declared | 14 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0902-x | PROPblock_22 | declared | 15 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0902-x | PROPblock_25 | declared | 13 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-0989-8 | PROPblock_7 | declared | 77 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-0989-8 | PROPblock_9 | declared | 77 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-0995-x | PROPblock_17 | declared | 48 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-0995-x | PROPblock_21 | declared | 48 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-0995-x | PROPblock_25 | declared | 48 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-0996-9 | PROPblock_1 | declared | 6 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-0996-9 | PROPblock_2 | declared | 6 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-1065-0 | PROPblock_2 | declared | 40 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-1087-7 | PROPblock_17 | declared | 45 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-1087-7 | PROPblock_21 | declared | 48 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-1087-7 | PROPblock_25 | declared | 45 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-1100-1 | PROPblock_7 | declared | 46 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-1100-1 | PROPblock_8 | declared | 41 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-1100-1 | PROPblock_9 | declared | 48 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-1111-y | PROPblock_1 | declared | 5 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-1111-y | PROPblock_2 | declared | 5 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-1111-y | PROPblock_3 | declared | 6 | binary | 2 | search_system_registry |
| 10.1007/s10765-012-1371-1 | PROPblock_10 | declared | 91 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-012-1371-1 | PROPblock_11 | declared | 91 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-012-1371-1 | PROPblock_6 | declared | 91 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-012-1371-1 | PROPblock_7 | declared | 91 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-012-1371-1 | PROPblock_8 | declared | 91 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-012-1371-1 | PROPblock_9 | declared | 91 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-013-1469-0 | PROPblock_7 | declared | 110 | binary | — | search_blocks |
| 10.1007/s10765-013-1469-0 | PROPblock_8 | declared | 110 | binary | 2 | search_blocks, search_system_registry |
| 10.1007/s10765-013-1469-0 | PROPblock_9 | declared | 110 | binary | — | search_blocks |
| 10.1007/s10765-013-1492-1 | PROPblock_11 | declared | 33 | binary | 2 | search_system_registry |
| 10.1007/s10765-013-1492-1 | PROPblock_14 | declared | 33 | binary | 2 | search_system_registry |
| 10.1007/s10765-013-1526-8 | PROPblock_19 | declared | 48 | binary | 2 | search_system_registry |
| 10.1007/s10765-013-1526-8 | PROPblock_23 | declared | 48 | binary | 2 | search_system_registry |
| 10.1007/s10765-013-1526-8 | PROPblock_27 | declared | 48 | binary | 2 | search_system_registry |
| 10.1007/s10765-015-1927-y | PROPblock_15 | declared | 10 | binary | 2 | search_system_registry |
| 10.1007/s10765-015-1927-y | PROPblock_18 | declared | 10 | binary | 2 | search_system_registry |
| 10.1007/s10765-015-1927-y | PROPblock_21 | declared | 10 | binary | 2 | search_system_registry |
| 10.1007/s10765-016-2089-2 | PROPblock_2 | declared | 45 | binary | 2 | search_system_registry |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `search_system_registry` | limit=100, property=GLOBprop_1, purpose=Find binar… | 709 | KEEP ←in 16,871 | 683 | 19.3 |
| 2 | 2 | `search_system_registry` | limit=100, property=GLOBprop_4, purpose=Find binar… | 1,400 | KEEP ←in 16,634 | 1282 | 20.0 |
| 3 | 4 | `block_search_adv` | explanation=Find binary liquid systems wh…, limit=… | 929 | DISCARD ←in 844 | 868 | 12.9 |
| 4 | 5 | `search_blocks` | limit=20, literature=GLOBlit_8, purpose=Check if G… | 623 | KEEP ←in 2,388 | 611 | 9.2 |
| 5 | 7 | `search_blocks` | limit=20, literature=GLOBlit_97, purpose=Check if … | 1,092 | KEEP ←in 5,434 | 1092 | 11.5 |
| 6 | 8 | `search_blocks` | limit=20, literature=GLOBlit_145, purpose=Check if… | 1,189 | KEEP ←in 8,821 | 1189 | 11.7 |
| 7 | 9 | `search_blocks` | limit=20, literature=GLOBlit_25, purpose=Check if … | 1,104 | KEEP ←in 8,422 | 1104 | 11.1 |
| 8 | 10 | `search_blocks` | limit=20, literature=GLOBlit_59, purpose=Check if … | 547 | KEEP ←in 2,395 | 547 | 8.8 |
| 9 | 11 | `search_blocks` | limit=20, literature=GLOBlit_151, purpose=Check if… | 890 | KEEP ←in 7,640 | 890 | 12.0 |
| 10 | 1 | `L1_query` | context=User wants to identify binary…, id_catalog… | 110,197 | — | — | 381.6 |
| | | **TOTAL (10 tools)** | | **118,680** | | **8,266** | **498.1** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 656 | 12,237 | 1,442 | 8.7 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,221 | 25,316 | 2,607 | 14.6 |
| 3 | L1-worker | claudeopus46 | 3,767 | 17,236 | 21,003 | 1,886 | 17.5 |
| 4 | L1-worker | claudeopus46 | 24,095 | 2,363 | 26,458 | 803 | 4.6 |
| 5 | L1-worker | claudeopus46 | 3,767 | 17,037 | 20,804 | 1,808 | 16.4 |
| 6 | L1-worker | claudeopus46 | 24,095 | 4,140 | 28,235 | 2,552 | 25.2 |
| 7 | L1-worker | claudeopus46 | 24,095 | 5,054 | 29,149 | 2,896 | 17.3 |
| 8 | L1-worker | claudeopus46 | 3,767 | 1,120 | 4,887 | 1,654 | 10.8 |
| 9 | L1-worker | claudeopus46 | 24,095 | 5,930 | 30,025 | 2,099 | 14.0 |
| 10 | L1-worker | claudeopus46 | 3,767 | 2,733 | 6,500 | 893 | 9.0 |
| 11 | L1-worker | claudeopus46 | 24,095 | 6,950 | 31,045 | 1,187 | 9.0 |
| 12 | L1-worker | claudeopus46 | 24,095 | 7,864 | 31,959 | 645 | 4.7 |
| 13 | L1-worker | claudeopus46 | 3,767 | 5,750 | 9,517 | 1,398 | 10.9 |
| 14 | L1-worker | claudeopus46 | 24,095 | 8,524 | 32,619 | 922 | 7.1 |
| 15 | L1-worker | claudeopus46 | 3,767 | 9,152 | 12,919 | 1,593 | 11.5 |
| 16 | L1-worker | claudeopus46 | 24,095 | 10,094 | 34,189 | 1,200 | 9.2 |
| 17 | L1-worker | claudeopus46 | 3,767 | 8,738 | 12,505 | 1,360 | 10.2 |
| 18 | L1-worker | claudeopus46 | 24,095 | 11,552 | 35,647 | 610 | 6.1 |
| 19 | L1-worker | claudeopus46 | 3,767 | 2,711 | 6,478 | 834 | 8.5 |
| 20 | L1-worker | claudeopus46 | 24,095 | 12,427 | 36,522 | 746 | 6.8 |
| 21 | L1-worker | claudeopus46 | 3,767 | 7,972 | 11,739 | 1,264 | 11.8 |
| 22 | L1-worker | claudeopus46 | 24,095 | 13,727 | 37,822 | 5,002 | 29.5 |
| 23 | L1-worker | claudeopus46 | 24,062 | 23,718 | 47,780 | 4,609 | 28.6 |
| 24 | L1-worker | claudeopus46 | 24,062 | 24,998 | 49,060 | 5,344 | 32.6 |
| 25 | L1-worker | claudeopus46 | 2,320 | 5,230 | 7,550 | 1,136 | 6.7 |
| 26 | L1-worker | claudeopus46 | 627 | 5,110 | 5,737 | 962 | 7.3 |
| 27 | L1-worker | claudeopus46 | 366 | 1,573 | 1,939 | 1,091 | 4.2 |
| 28 | L1-worker | claudeopus46 | 2,106 | 6,572 | 8,678 | 5,792 | 21.7 |
| 29 | L1-worker | claudeopus46 | 366 | 6,569 | 6,935 | 4,622 | 17.1 |
| 30 | L1-worker | claudeopus46 | 787 | 115,017 | 115,804 | 649 | 9.6 |
| 31 | L0-main | claudeopus46 | 11,581 | 42,765 | 54,346 | 5,269 | 36.3 |
| 32 | L0-main | claudeopus46 | 2,320 | 4,818 | 7,138 | 1,484 | 11.0 |
| 33 | L0-main | claudeopus46 | 2,106 | 5,306 | 7,412 | 2,710 | 13.6 |
| 34 | L0-main | claudeopus46 | 366 | 1,959 | 2,325 | 1,435 | 5.2 |
| 35 | L0-main | claudeopus46 | 366 | 3,259 | 3,625 | 2,714 | 10.2 |
| 36 | L0-main | claudeopus46 | 560 | 9,864 | 10,424 | 1,457 | 7.8 |
| 37 | L0-main | claudeopus46 | 1,156 | 22,098 | 23,254 | 5,570 | 25.1 |
| 38 | L0-main | claudeopus46 | 366 | 6,263 | 6,629 | 4,842 | 18.7 |

