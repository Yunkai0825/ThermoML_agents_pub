# Reference Stats — query-agent

**Run started:** 2026-09-05 05:28:45
**Wall time (at last flush):** 383.3 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 10 | 41,387 | 78,746 | 13,566 | 120,133 | 12,013 | 87.4 | claudeopus46 |
| L1-worker | 32 | 312,092 | 220,698 | 45,611 | 532,790 | 16,649 | 317.0 | claudeopus46 |
| **TOTAL** | **42** | **353,479** | **299,444** | **59,177** | **652,923** | **15,545** | **404.4** | |

**Estimated tokens:** ~163,230 input + ~14,794 output = ~178,024 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_system_summary` | 11 | 1 | 0 | 0 | 295 | 753 | 30,819 |
| `search_system_registry` | 87 | 1 | 5 | 6 | 48 | 100 | 4,126 |
| `search_system_summary` | 0 | 1 | 0 | 0 | 2713 | 8207 | 458,437 |
| `resolve_compound_ids` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_system_summary` | 11 | 1 | 0 | 0 | 1104 | 2558 | 132,045 |
| `search_system_registry` | 86 | 1 | 6 | 6 | 60 | 100 | 4,954 |
| **TOTAL** | **197** | **5** | **11** | **12** | **4220** | **11718** | **630,381** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Compounds (149 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBcomp_1 |  | resolve_compound_ids, search_system_registry, search_system_summary |
| GLOBcomp_53 | 2-aminoacetic acid | search_system_registry, search_system_summary |
| GLOBcomp_26 | sodium chloride | search_system_registry, search_system_summary |
| GLOBcomp_120 | D-sucrose | search_system_summary |
| GLOBcomp_90 | D-glucose | search_system_registry, search_system_summary |
| GLOBcomp_41 | potassium chloride | search_system_registry, search_system_summary |
| GLOBcomp_74 | (S)-2-aminopropanoic acid | search_system_registry, search_system_summary |
| GLOBcomp_116 | L-valine | search_system_registry, search_system_summary |
| GLOBcomp_233 | potassium nitrate | search_system_registry, search_system_summary |
| GLOBcomp_24 | 1,2-ethanediol | search_system_registry, search_system_summary |
| GLOBcomp_160 | tetrabutylammonium bromide | search_system_registry, search_system_summary |
| GLOBcomp_821 | cis-1,4-butenedioic acid | search_system_registry |
| GLOBcomp_2259 | 2,3-dihydroxybutanedioic acid | search_system_registry |
| GLOBcomp_464 | 4-aminobutanoic acid | search_system_registry |
| GLOBcomp_1016 | N,N-dimethylimidodicarbonimidic diamide hydrochloride | search_system_registry |
| GLOBcomp_168 | potassium sulfate | search_system_registry |
| GLOBcomp_489 | ammonium 2-hydroxypropane-1,2,3-tricarboxylate | search_system_registry |
| GLOBcomp_382 | disodium hydrogen phosphate | search_system_registry |
| GLOBcomp_5 | propan-1-ol | search_system_registry, search_system_summary |
| GLOBcomp_575 | trisodium phosphate | search_system_registry |
| GLOBcomp_1192 | 1-heptyl-3-methylimidazolium bromide | search_system_registry |
| GLOBcomp_2160 | tetrabutylphosphonium tetrafluoroborate | search_system_registry |
| GLOBcomp_6661 | sodium n-hexylsulfonate | search_system_registry |
| GLOBcomp_3032 | benzyldimethylammonium propionate | search_system_registry |
| GLOBcomp_2820 | benzyldimethylammonium hexanoate | search_system_registry |
| GLOBcomp_2696 | N,N-dimethylbenzylammonium acetate | search_system_registry |
| GLOBcomp_3293 | 2-hydroxy-N,N-dimethylethan-1-aminium butyrate | search_system_registry |
| GLOBcomp_4192 | N-(2-hydroxyethyl)butan-1-aminium butyrate | search_system_registry |
| GLOBcomp_873 | (S)-2-hydroxypropanoic acid | search_system_registry |
| GLOBcomp_2325 | diethylammonium butanoate | search_system_registry |
| GLOBcomp_555 | tetramethylammonium bromide | search_system_registry |
| GLOBcomp_369 | tetraethylammonium bromide | search_system_registry |
| GLOBcomp_493 | tetrapropylammonium bromide | search_system_registry |
| GLOBcomp_5019 | decyl beta.-D-glucopyranoside | search_system_registry |
| GLOBcomp_8167 | cholinium L-phenylalaninate | search_system_registry |
| GLOBcomp_158 | 1-butyl-3-methylimidazolium bromide | search_system_registry |
| GLOBcomp_8261 | butanoic acid, heptafluoro-, sodium salt | search_system_registry |
| GLOBcomp_363 | 1,4,7,10,13,16-hexaoxacyclooctadecane | search_system_registry |
| GLOBcomp_81 | N-methyldiethanolamine | search_system_registry, search_system_summary |
| GLOBcomp_44 | 2-methylpropan-2-ol | search_system_registry |
| GLOBcomp_31 | dimethyl sulfoxide | search_system_registry |
| GLOBcomp_246 | sodium ethanoate | search_system_registry |
| GLOBcomp_221 | L-threonine | search_system_registry |
| GLOBcomp_1037 | magnesium acetate | search_system_registry |
| GLOBcomp_171 | L-serine | search_system_registry |
| GLOBcomp_18 | dimethylformamide | search_system_registry |
| GLOBcomp_25 | 1,4-dioxane | search_system_registry |
| GLOBcomp_15 | acetonitrile | search_system_registry |
| GLOBcomp_23 | tetrahydrofuran | search_system_registry |
| GLOBcomp_112 | hydrogen chloride | search_system_registry |
| GLOBcomp_61 | 1,2-propanediol | search_system_registry |
| GLOBcomp_146 | 4-methyl-1,3-dioxolan-2-one | search_system_registry |
| GLOBcomp_381 | tetramethylurea | search_system_registry |
| GLOBcomp_779 | 2-hydroxyethylammonium formate | search_system_registry |
| GLOBcomp_133 | formamide | search_system_registry |
| GLOBcomp_177 | N-methylformamide | search_system_registry |
| GLOBcomp_63 | N,N-dimethylethanamide | search_system_registry |
| GLOBcomp_268 | 2-pyrrolidinone | search_system_registry |
| GLOBcomp_47 | N-methylpyrrolidone | search_system_registry |
| GLOBcomp_413 | ethane-1,2-diamine | search_system_registry |
| GLOBcomp_5015 | imidazolium chloride | search_system_registry |
| GLOBcomp_920 | 1-methylimidazolium chloride | search_system_registry |
| GLOBcomp_99 | 1-butyl-3-methylimidazolium chloride | search_system_registry |
| GLOBcomp_261 | 3-hexyl-1-methyl-1H-imidazolium bromide | search_system_registry |
| GLOBcomp_213 | sodium dihydrogen phosphate | search_system_registry |
| GLOBcomp_517 | 1-methyl-3-octylimidazolium bromide | search_system_registry |
| GLOBcomp_491 | 1-methyl-3-propylimidazolium bromide | search_system_registry |
| GLOBcomp_169 | 1,4-butanediol | search_system_registry |
| GLOBcomp_118 | 2-methoxyethan-1-ol | search_system_registry |
| GLOBcomp_140 | 2-ethoxyethan-1-ol | search_system_registry |
| GLOBcomp_317 | 3,6-dioxa-1-octanol | search_system_registry |
| GLOBcomp_478 | 2-(2-methoxyethoxy)ethanol | search_system_registry |
| GLOBcomp_1395 | trimethylbenzylammonium chloride | search_system_registry |
| GLOBcomp_1986 | benzyltributylammonium chloride | search_system_registry |
| GLOBcomp_2388 | benzyltriethylammonium chloride | search_system_registry |
| GLOBcomp_2914 | glycyl-L-serylglycine | search_system_registry |
| GLOBcomp_2769 | (2S,4R)-4-hydroxypyrrolidine-2-carboxylic acid | search_system_registry |
| GLOBcomp_398 | 1,2-benzenediol | search_system_registry |
| GLOBcomp_352 | 1,3-benzenediol | search_system_registry |
| GLOBcomp_343 | 1,4-benzenediol | search_system_registry |
| GLOBcomp_3200 | ammonium citrate, dibasic | search_system_registry |
| GLOBcomp_293 | potassium citrate | search_system_registry |
| GLOBcomp_355 | L-histidine | search_system_registry |
| GLOBcomp_273 | 1-methyl-3-octylimidazolium chloride | search_system_registry |
| GLOBcomp_150 | 1-butyl-3-methylimidazolium methyl sulfate | search_system_registry |
| GLOBcomp_562 | 1-butyl-3-methylimidazolium octyl sulfate | search_system_registry |
| GLOBcomp_36 | 1-butyl-3-methylimidazolium tetrafluoroborate | search_system_registry, search_system_summary |
| GLOBcomp_121 | 1-methyl-3-octylimidazolium tetrafluoroborate | search_system_registry |
| GLOBcomp_546 | 2-hydroxyethylammonium acetate | search_system_registry |
| GLOBcomp_2 | ethanol | search_system_registry, search_system_summary |
| GLOBcomp_199 | ammonia | search_system_registry |
| GLOBcomp_208 | 1,3-dioxolane | search_system_registry |
| GLOBcomp_1358 | 1,3-dimethylimidazolium chloride | search_system_registry |
| GLOBcomp_291 | (+)-galactose | search_system_registry |
| GLOBcomp_389 | 2-amino-2-(hydroxymethyl)-1,3-propanediol | search_system_registry |
| GLOBcomp_6845 | L-glutamic acid hydrochloride | search_system_registry |
| GLOBcomp_551 | copper sulfate | search_system_registry |
| GLOBcomp_205 | 1-ethyl-3-methylimidazolium diethyl phosphate | search_system_registry |
| GLOBcomp_550 | 3-methylnonyl 1,2-benzenedioate | search_system_registry |
| GLOBcomp_4 | methanol | search_system_registry |
| GLOBcomp_222 | potassium bromide | search_system_registry |
| GLOBcomp_84 | 1-ethyl-3-methylimidazolium tetrafluoroborate | search_system_registry |
| GLOBcomp_68 | 1-ethyl-3-methylimidazolium ethyl sulfate | search_system_registry |
| GLOBcomp_2030 | copper dinitrate | search_system_registry |
| GLOBcomp_806 | nickel chloride (NiCl2) | search_system_registry |
| GLOBcomp_105 | 1-hexyl-3-methylimidazolium tetrafluoroborate | search_system_registry |
| GLOBcomp_302 | 1,3-dimethylimidazolium methylsulfate | search_system_registry |
| GLOBcomp_252 | 1-ethyl-3-methylimidazolium thiocyanate | search_system_registry |
| GLOBcomp_3053 | tetraphenylphosphonium chloride | search_system_registry |
| GLOBcomp_1826 | 2-methylpiperidine | search_system_registry |
| GLOBcomp_900 | N-methylpiperidine | search_system_registry |
| GLOBcomp_217 | 1,3-dimethylimidazolium dimethylphosphate | search_system_registry |
| GLOBcomp_279 | 1-ethyl-3-methylimidazolium methylsulfate | search_system_registry |
| GLOBcomp_1868 | 1-hexyl-3-methylimidazolium methyl sulfate | search_system_registry |
| GLOBcomp_2982 | 1-hexyl-3-methylimidazolium ethyl sulfate | search_system_registry |
| GLOBcomp_494 | L-ascorbic acid | search_system_registry |
| GLOBcomp_202 | triethylamine | search_system_registry |
| GLOBcomp_20 | butan-2-ol | search_system_registry |
| GLOBcomp_3019 | decanoic acid, 2-[4-[3-[2-(trifluoromethyl)-10H-phenothiazin-10-yl]propyl]-1-piperazinyl]ethyl ester | search_system_registry |
| GLOBcomp_219 | D-xylose | search_system_registry |
| GLOBcomp_374 | D-ribose | search_system_registry |
| GLOBcomp_567 | ammonium dihydrogen phosphate | search_system_registry |
| GLOBcomp_2246 | urea phosphate | search_system_registry |
| GLOBcomp_2781 | 2-(hydroxymethyl)piperidine | search_system_registry |
| GLOBcomp_3038 | 3-(hydroxymethyl)piperidine | search_system_registry |
| GLOBcomp_7002 | .alpha.-picolyl alcohol | search_system_registry |
| GLOBcomp_5828 | .beta.-picolyl alcohol | search_system_registry |
| GLOBcomp_215 | magnesium sulfate | search_system_registry |
| GLOBcomp_800 | magnesium bromide (MgBr2) | search_system_registry |
| GLOBcomp_159 | D-fructose | search_system_registry |
| GLOBcomp_1760 | hexyltrimethylammonium bromide | search_system_registry |
| GLOBcomp_6 | propan-2-ol | search_system_registry |
| GLOBcomp_737 | di(2-aminoethyl)amine | search_system_registry |
| GLOBcomp_1394 | N,N,N',N'-tetramethyl-1,2-diaminoethane | search_system_registry |
| GLOBcomp_1629 | N,N,N',N'-tetramethyl-1,3-propanediamine | search_system_registry |
| GLOBcomp_619 | N-methyl-1,3-diaminopropane | search_system_registry |
| GLOBcomp_201 | glycylglycine | search_system_registry |
| GLOBcomp_742 | glycyl-L-valine | search_system_registry |
| GLOBcomp_495 | glycyl-L-leucine | search_system_registry |
| GLOBcomp_1131 | lithium metaborate | search_system_registry |
| GLOBcomp_258 | lithium sulfate | search_system_registry |
| GLOBcomp_8008 | 2-hydroxyethylammonium stearate | search_system_registry |
| GLOBcomp_8150 | bis(2-hydroxyethyl)ammonium stearate | search_system_registry |
| GLOBcomp_94 | urea | search_system_registry |
| GLOBcomp_1910 | N-ethyl-N-methylpiperidinium bromide | search_system_registry |
| GLOBcomp_3836 | 1-methyl-1-propylpiperidinium bromide | search_system_registry |
| GLOBcomp_3095 | N-butyl-N-methylpiperidinium bromide | search_system_registry |
| GLOBcomp_3196 | sodium 2-naphthalenesulfonate | search_system_registry |
| GLOBcomp_1697 | sodium 1-naphthalene sulfonate | search_system_registry |

#### Properties (2 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_8 |  | search_system_registry, search_system_summary |
| GLOBprop_1 |  | search_system_registry, search_system_summary |

#### References (144 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_5043 |  | search_system_summary |
| GLOBlit_5201 |  | search_system_summary |
| GLOBlit_8239 |  | search_system_summary |
| GLOBlit_10102 |  | search_system_summary |
| GLOBlit_9821 |  | search_system_summary |
| GLOBlit_10011 |  | search_system_summary |
| GLOBlit_10162 |  | search_system_summary |
| GLOBlit_3781 |  | search_system_summary |
| GLOBlit_8886 |  | search_system_summary |
| GLOBlit_10594 |  | search_system_summary |
| GLOBlit_4317 |  | search_system_summary |
| GLOBlit_3285 |  | search_system_registry, search_system_summary |
| GLOBlit_4742 |  | search_system_summary |
| GLOBlit_9777 |  | search_system_summary |
| GLOBlit_3601 |  | search_system_summary |
| GLOBlit_7113 |  | search_system_summary |
| GLOBlit_3007 |  | search_system_registry, search_system_summary |
| GLOBlit_2239 |  | search_system_registry, search_system_summary |
| GLOBlit_9758 |  | search_system_summary |
| GLOBlit_6686 |  | search_system_summary |
| GLOBlit_67 |  | search_system_registry |
| GLOBlit_96 |  | search_system_registry |
| GLOBlit_107 |  | search_system_registry |
| GLOBlit_149 |  | search_system_registry |
| GLOBlit_173 |  | search_system_registry |
| GLOBlit_555 |  | search_system_registry |
| GLOBlit_590 |  | search_system_registry |
| GLOBlit_865 |  | search_system_registry |
| GLOBlit_1243 |  | search_system_registry |
| GLOBlit_1373 |  | search_system_registry |
| GLOBlit_1591 |  | search_system_registry |
| GLOBlit_1867 |  | search_system_registry |
| GLOBlit_1890 |  | search_system_registry |
| GLOBlit_1949 |  | search_system_registry |
| GLOBlit_2030 |  | search_system_registry |
| GLOBlit_2124 |  | search_system_registry |
| GLOBlit_2171 |  | search_system_registry |
| GLOBlit_2274 |  | search_system_registry |
| GLOBlit_2492 |  | search_system_registry |
| GLOBlit_2528 |  | search_system_registry |
| GLOBlit_2535 |  | search_system_registry |
| GLOBlit_2625 |  | search_system_registry |
| GLOBlit_2652 |  | search_system_registry |
| GLOBlit_2673 |  | search_system_registry |
| GLOBlit_2733 |  | search_system_registry |
| GLOBlit_2736 |  | search_system_registry |
| GLOBlit_2820 |  | search_system_registry |
| GLOBlit_2831 |  | search_system_registry |
| GLOBlit_2832 |  | search_system_registry |
| GLOBlit_2834 |  | search_system_registry |
| GLOBlit_2842 |  | search_system_registry |
| GLOBlit_2879 |  | search_system_registry |
| GLOBlit_2900 |  | search_system_registry |
| GLOBlit_2911 |  | search_system_registry |
| GLOBlit_3009 |  | search_system_registry |
| GLOBlit_3053 |  | search_system_registry |
| GLOBlit_3063 |  | search_system_registry |
| GLOBlit_3139 |  | search_system_registry |
| GLOBlit_3162 |  | search_system_registry |
| GLOBlit_3179 |  | search_system_registry |
| GLOBlit_3239 |  | search_system_registry |
| GLOBlit_3307 |  | search_system_registry |
| GLOBlit_3319 |  | search_system_registry |
| GLOBlit_3346 |  | search_system_registry |
| GLOBlit_3347 |  | search_system_registry |
| GLOBlit_5458 |  | search_system_summary |
| GLOBlit_4652 |  | search_system_summary |
| GLOBlit_9601 |  | search_system_summary |
| GLOBlit_6244 |  | search_system_summary |
| GLOBlit_5265 |  | search_system_summary |
| GLOBlit_4052 |  | search_system_summary |
| GLOBlit_7580 |  | search_system_summary |
| GLOBlit_3356 |  | search_system_summary |
| GLOBlit_3034 |  | search_system_summary |
| GLOBlit_10888 |  | search_system_summary |
| GLOBlit_10906 |  | search_system_summary |
| GLOBlit_2432 |  | search_system_summary |
| GLOBlit_11627 |  | search_system_summary |
| GLOBlit_7685 |  | search_system_summary |
| GLOBlit_4754 |  | search_system_summary |
| GLOBlit_2749 |  | search_system_summary |
| GLOBlit_2794 |  | search_system_summary |
| GLOBlit_3882 |  | search_system_summary |
| GLOBlit_3450 |  | search_system_summary |
| GLOBlit_9646 |  | search_system_summary |
| GLOBlit_5017 |  | search_system_summary |
| GLOBlit_2639 |  | search_system_summary |
| GLOBlit_4704 |  | search_system_summary |
| GLOBlit_2567 |  | search_system_summary |
| GLOBlit_5580 |  | search_system_summary |
| GLOBlit_7992 |  | search_system_summary |
| GLOBlit_1311 |  | search_system_registry, search_system_summary |
| GLOBlit_9783 |  | search_system_summary |
| GLOBlit_4649 |  | search_system_summary |
| GLOBlit_220 |  | search_system_registry, search_system_summary |
| GLOBlit_14 |  | search_system_registry |
| GLOBlit_49 |  | search_system_registry |
| GLOBlit_73 |  | search_system_registry |
| GLOBlit_81 |  | search_system_registry |
| GLOBlit_87 |  | search_system_registry |
| GLOBlit_98 |  | search_system_registry |
| GLOBlit_126 |  | search_system_registry |
| GLOBlit_174 |  | search_system_registry |
| GLOBlit_178 |  | search_system_registry |
| GLOBlit_189 |  | search_system_registry |
| GLOBlit_373 |  | search_system_registry |
| GLOBlit_385 |  | search_system_registry |
| GLOBlit_389 |  | search_system_registry |
| GLOBlit_391 |  | search_system_registry |
| GLOBlit_462 |  | search_system_registry |
| GLOBlit_484 |  | search_system_registry |
| GLOBlit_622 |  | search_system_registry |
| GLOBlit_716 |  | search_system_registry |
| GLOBlit_725 |  | search_system_registry |
| GLOBlit_779 |  | search_system_registry |
| GLOBlit_787 |  | search_system_registry |
| GLOBlit_817 |  | search_system_registry |
| GLOBlit_835 |  | search_system_registry |
| GLOBlit_858 |  | search_system_registry |
| GLOBlit_895 |  | search_system_registry |
| GLOBlit_917 |  | search_system_registry |
| GLOBlit_941 |  | search_system_registry |
| GLOBlit_955 |  | search_system_registry |
| GLOBlit_971 |  | search_system_registry |
| GLOBlit_976 |  | search_system_registry |
| GLOBlit_1049 |  | search_system_registry |
| GLOBlit_1096 |  | search_system_registry |
| GLOBlit_1107 |  | search_system_registry |
| GLOBlit_1117 |  | search_system_registry |
| GLOBlit_1147 |  | search_system_registry |
| GLOBlit_1170 |  | search_system_registry |
| GLOBlit_1214 |  | search_system_registry |
| GLOBlit_1223 |  | search_system_registry |
| GLOBlit_1249 |  | search_system_registry |
| GLOBlit_1310 |  | search_system_registry |
| GLOBlit_1381 |  | search_system_registry |
| GLOBlit_1415 |  | search_system_registry |
| GLOBlit_1420 |  | search_system_registry |
| GLOBlit_1446 |  | search_system_registry |
| GLOBlit_1483 |  | search_system_registry |
| GLOBlit_1488 |  | search_system_registry |
| GLOBlit_1540 |  | search_system_registry |
| GLOBlit_1557 |  | search_system_registry |
| GLOBlit_1562 |  | search_system_registry |

#### Block_Types (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBblocktype_1 |  | search_system_registry |

#### Solvents (5 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBsolvent_1 |  | search_system_registry |
| GLOBsolvent_23 |  | search_system_registry |
| GLOBsolvent_68 |  | search_system_registry |
| GLOBsolvent_387 |  | search_system_registry |
| GLOBsolvent_12 |  | search_system_registry |

#### Constraints (7 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBconstr_1 | Pressure, kPa | search_system_registry |
| GLOBconstr_12 | Amount concentration (molarity), mol/dm3 | search_system_registry |
| GLOBconstr_8 | Molality, mol/kg | search_system_registry |
| GLOBconstr_4 | Frequency, MHz | search_system_registry |
| GLOBconstr_2 | Temperature, K | search_system_registry |
| GLOBconstr_3 | Mole fraction | search_system_registry |
| GLOBconstr_5 | Mass fraction | search_system_registry |

#### Phases (3 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | search_system_registry |
| GLOBphase_10 |  | search_system_registry |
| GLOBphase_3 |  | search_system_registry |

#### Variables (6 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBvar_1 | Temperature, K | search_system_registry |
| GLOBvar_4 | Molality, mol/kg | search_system_registry |
| GLOBvar_5 | Mass fraction | search_system_registry |
| GLOBvar_2 | Mole fraction | search_system_registry |
| GLOBvar_9 | Amount concentration (molarity), mol/dm3 | search_system_registry |
| GLOBvar_3 | Pressure, kPa | search_system_registry |

#### Measurements (28 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBmeas_190 | Speed of sound, m/s | search_system_registry |
| GLOBmeas_15 | Speed of sound, m/s | search_system_registry |
| GLOBmeas_7 | Speed of sound, m/s | search_system_registry |
| GLOBmeas_18 | Speed of sound, m/s | search_system_registry |
| GLOBmeas_181 | Speed of sound, m/s | search_system_registry |
| GLOBmeas_311 | Speed of sound, m/s | search_system_registry |
| GLOBmeas_209 | Speed of sound, m/s | search_system_registry |
| GLOBmeas_206 | Speed of sound, m/s | search_system_registry |
| GLOBmeas_811 | Speed of sound, m/s | search_system_registry |
| GLOBmeas_20 | Speed of sound, m/s | search_system_registry |
| GLOBmeas_694 | Speed of sound, m/s | search_system_registry |
| GLOBmeas_66 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_1662 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_280 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_6 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_56 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_147 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_184 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_153 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_2 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_187 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_138 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_141 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_176 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_1494 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_134 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_1694 | Mass density, kg/m3 | search_system_registry |
| GLOBmeas_861 | Mass density, kg/m3 | search_system_registry |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Compounds | 149 |
| Unique Properties | 2 |
| Unique References | 144 |
| Unique Block_Types | 1 |
| Unique Solvents | 5 |
| Unique Constraints | 7 |
| Unique Phases | 3 |
| Unique Variables | 6 |
| Unique Measurements | 28 |
| Total DOIs | 99 |
| Unique parent blocks | 200 |
| Explicit block/subsystem targets | 200 |
| Subsystem targets | 0 |
| Target-matched data points | 9,080 |

---

## 3. DOI & Block References

**Unique DOIs:** 99  |  **Parent blocks:** 200  |  **Explicit targets:** 200  |  **Subsystems:** 0  |  **Target-matched datapoints:** 9,080

| DOI | Blocks | Datapoints | System types | Source tools |
|-----|-------:|-----------:|--------------|--------------|
| 10.1007/s10765-005-8590-7 | 1 | 277 | binary | search_system_registry |
| 10.1007/s10765-007-0220-0 | 1 | 12 | binary | search_system_registry |
| 10.1007/s10765-008-0514-x | 4 | 27 | binary | search_system_registry |
| 10.1007/s10765-009-0567-5 | 1 | 12 | binary | search_system_registry |
| 10.1007/s10765-009-0602-6 | 1 | 39 | binary | search_system_registry |
| 10.1007/s10765-009-0651-x | 1 | 48 | binary | search_system_registry |
| 10.1007/s10765-010-0736-6 | 4 | 56 | binary | search_system_registry |
| 10.1007/s10765-010-0742-8 | 1 | 5 | binary | search_system_registry |
| 10.1007/s10765-010-0862-1 | 4 | 48 | binary | search_system_registry |
| 10.1007/s10765-011-1065-0 | 1 | 40 | binary | search_system_registry |
| 10.1007/s10765-013-1432-0 | 2 | 12 | binary | search_system_registry |
| 10.1007/s10765-015-2006-0 | 4 | 132 | binary | search_system_registry |
| 10.1007/s10765-015-2009-x | 1 | 24 | binary | search_system_registry |
| 10.1007/s10765-016-2089-2 | 1 | 45 | binary | search_system_registry |
| 10.1007/s10765-018-2359-2 | 1 | 20 | binary | search_system_registry |
| 10.1016/j.fluid.2004.11.019 | 1 | 810 | binary | search_system_registry |
| 10.1016/j.fluid.2006.03.012 | 1 | 4 | binary | search_system_registry |
| 10.1016/j.fluid.2006.05.007 | 1 | 45 | binary | search_system_registry |
| 10.1016/j.fluid.2006.05.015 | 2 | 156 | binary | search_system_registry |
| 10.1016/j.fluid.2006.05.028 | 2 | 40 | binary | search_system_registry |
| 10.1016/j.fluid.2006.12.005 | 2 | 10 | binary | search_system_registry |
| 10.1016/j.fluid.2007.01.043 | 2 | 4 | binary | search_system_registry |
| 10.1016/j.fluid.2007.07.066 | 4 | 220 | binary | search_system_registry |
| 10.1016/j.fluid.2008.01.004 | 4 | 280 | binary | search_system_registry |
| 10.1016/j.fluid.2008.04.003 | 1 | 35 | binary | search_system_registry |
| 10.1016/j.fluid.2009.06.008 | 1 | 42 | binary | search_system_registry |
| 10.1016/j.fluid.2009.07.010 | 3 | 55 | binary | search_system_registry |
| 10.1016/j.fluid.2010.01.002 | 1 | 72 | binary | search_system_registry |
| 10.1016/j.fluid.2010.01.020 | 1 | 78 | binary | search_system_registry |
| 10.1016/j.fluid.2010.03.017 | 1 | 18 | binary | search_system_registry |
| 10.1016/j.fluid.2010.05.001 | 2 | 112 | binary | search_system_registry |
| 10.1016/j.fluid.2010.07.005 | 1 | 30 | binary | search_system_registry |
| 10.1016/j.fluid.2010.08.004 | 2 | 140 | binary | search_system_registry |
| 10.1016/j.fluid.2010.10.005 | 1 | 34 | binary | search_system_registry |
| 10.1016/j.fluid.2011.01.001 | 3 | 168 | binary | search_system_registry |
| 10.1016/j.fluid.2011.02.017 | 1 | 9 | binary | search_system_registry |
| 10.1016/j.fluid.2011.03.031 | 1 | 29 | binary | search_system_registry |
| 10.1016/j.fluid.2011.05.017 | 1 | 9 | binary | search_system_registry |
| 10.1016/j.fluid.2011.06.008 | 1 | 5 | binary | search_system_registry |
| 10.1016/j.fluid.2011.11.028 | 4 | 24 | binary | search_system_registry |
| 10.1016/j.fluid.2012.04.003 | 1 | 6 | binary | search_system_registry |
| 10.1016/j.fluid.2012.05.007 | 2 | 20 | binary | search_system_registry |
| 10.1016/j.fluid.2012.06.002 | 2 | 4 | binary | search_system_registry |
| 10.1016/j.fluid.2012.08.024 | 2 | 10 | binary | search_system_registry |
| 10.1016/j.fluid.2012.10.024 | 4 | 348 | binary | search_system_registry |
| 10.1016/j.fluid.2013.01.004 | 2 | 2 | binary | search_system_registry |
| 10.1016/j.fluid.2013.01.025 | 1 | 85 | binary | search_system_registry |
| 10.1016/j.fluid.2013.03.030 | 2 | 6 | binary | search_system_registry |
| 10.1016/j.fluid.2013.05.006 | 3 | 18 | binary | search_system_registry |
| 10.1016/j.fluid.2013.08.005 | 1 | 20 | binary | search_system_registry |
| 10.1016/j.fluid.2013.08.007 | 1 | 1,110 | binary | search_system_registry |
| 10.1016/j.fluid.2013.11.015 | 2 | 170 | binary | search_system_registry |
| 10.1016/j.fluid.2013.11.028 | 4 | 100 | binary | search_system_registry |
| 10.1016/j.fluid.2014.01.038 | 3 | 24 | binary | search_system_registry |
| 10.1016/j.fluid.2014.01.044 | 1 | 5 | binary | search_system_registry |
| 10.1016/j.fluid.2014.03.019 | 2 | 4 | binary | search_system_registry |
| 10.1016/j.fluid.2014.05.032 | 1 | 140 | binary | search_system_registry |
| 10.1016/j.fluid.2014.05.043 | 2 | 36 | binary | search_system_registry |
| 10.1016/j.fluid.2014.08.026 | 4 | 17 | binary | search_system_registry |
| 10.1016/j.fluid.2014.09.020 | 3 | 120 | binary | search_system_registry |
| 10.1016/j.fluid.2014.09.026 | 2 | 6 | binary | search_system_registry |
| 10.1016/j.fluid.2014.11.005 | 5 | 240 | binary | search_system_registry |
| 10.1016/j.fluid.2016.01.036 | 1 | 4 | binary | search_system_registry |
| 10.1016/j.fluid.2016.02.035 | 1 | 126 | binary | search_system_registry |
| 10.1016/j.fluid.2016.07.022 | 1 | 4 | binary | search_system_registry |
| 10.1016/j.fluid.2017.02.019 | 1 | 40 | binary | search_system_registry |
| 10.1016/j.fluid.2017.12.001 | 1 | 88 | binary | search_system_registry |
| 10.1016/j.fluid.2018.03.002 | 4 | 47 | binary | search_system_registry |
| 10.1016/j.fluid.2018.08.011 | 1 | 323 | binary | search_system_registry |
| 10.1016/j.fluid.2018.12.017 | 1 | 28 | binary | search_system_registry |
| 10.1016/j.jct.2005.01.009 | 1 | 45 | binary | search_system_registry |
| 10.1016/j.jct.2005.03.021 | 1 | 162 | binary | search_system_registry |
| 10.1016/j.jct.2005.04.005 | 1 | 15 | binary | search_system_registry |
| 10.1016/j.jct.2005.10.013 | 1 | 24 | binary | search_system_registry |
| 10.1016/j.jct.2006.01.007 | 2 | 12 | binary | search_system_registry |
| 10.1016/j.jct.2006.03.009 | 3 | 15 | binary | search_system_registry |
| 10.1016/j.jct.2006.08.003 | 4 | 20 | binary | search_system_registry |
| 10.1016/j.jct.2006.08.007 | 4 | 34 | binary | search_system_registry |
| 10.1016/j.jct.2007.04.009 | 1 | 12 | binary | search_system_registry |
| 10.1016/j.jct.2007.05.010 | 4 | 36 | binary | search_system_registry |
| 10.1016/j.jct.2007.05.011 | 1 | 195 | binary | search_system_registry |
| 10.1016/j.jct.2007.05.015 | 6 | 195 | binary | search_system_registry |
| 10.1016/j.jct.2007.06.007 | 2 | 80 | binary | search_system_registry |
| 10.1016/j.jct.2007.10.007 | 3 | 33 | binary | search_system_registry |
| 10.1016/j.jct.2008.01.003 | 1 | 130 | binary | search_system_registry |
| 10.1016/j.jct.2008.01.018 | 1 | 120 | binary | search_system_registry |
| 10.1016/j.jct.2008.09.005 | 4 | 325 | binary | search_system_registry |
| 10.1016/j.jct.2008.09.008 | 1 | 10 | binary | search_system_registry |
| 10.1016/j.jct.2009.01.010 | 4 | 64 | binary | search_system_registry |
| 10.1016/j.jct.2009.03.004 | 3 | 150 | binary | search_system_registry |
| 10.1016/j.jct.2009.08.004 | 1 | 5 | binary | search_system_registry |
| 10.1016/j.jct.2009.10.007 | 1 | 75 | binary | search_system_registry |
| 10.1016/j.jct.2009.11.017 | 1 | 57 | binary | search_system_registry |
| 10.1016/j.jct.2010.04.018 | 3 | 110 | binary | search_system_registry |
| 10.1016/j.jct.2010.08.021 | 3 | 348 | binary | search_system_registry |
| 10.1016/j.jct.2010.11.003 | 1 | 80 | binary | search_system_registry |
| 10.1016/j.jct.2010.11.017 | 2 | 84 | binary | search_system_registry |
| 10.1016/j.jct.2011.01.013 | 6 | 72 | binary | search_system_registry |
| 10.1016/j.jct.2011.01.014 | 1 | 195 | binary | search_system_registry |

<details><summary>Block detail</summary>

| DOI | Block | Target | Datapoints | System | nComp | Source tools |
|-----|------:|--------|-----------:|--------|------:|--------------|
| 10.1007/s10765-005-8590-7 | PROPblock_2 | declared | 277 | binary | 2 | search_system_registry |
| 10.1007/s10765-007-0220-0 | PROPblock_2 | declared | 12 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0514-x | PROPblock_1 | declared | 6 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0514-x | PROPblock_2 | declared | 6 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0514-x | PROPblock_3 | declared | 9 | binary | 2 | search_system_registry |
| 10.1007/s10765-008-0514-x | PROPblock_4 | declared | 6 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0567-5 | PROPblock_2 | declared | 12 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0602-6 | PROPblock_2 | declared | 39 | binary | 2 | search_system_registry |
| 10.1007/s10765-009-0651-x | PROPblock_3 | declared | 48 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0736-6 | PROPblock_1 | declared | 14 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0736-6 | PROPblock_2 | declared | 14 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0736-6 | PROPblock_3 | declared | 14 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0736-6 | PROPblock_4 | declared | 14 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0742-8 | PROPblock_3 | declared | 5 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0862-1 | PROPblock_3 | declared | 15 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0862-1 | PROPblock_4 | declared | 15 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0862-1 | PROPblock_5 | declared | 9 | binary | 2 | search_system_registry |
| 10.1007/s10765-010-0862-1 | PROPblock_6 | declared | 9 | binary | 2 | search_system_registry |
| 10.1007/s10765-011-1065-0 | PROPblock_4 | declared | 40 | binary | 2 | search_system_registry |
| 10.1007/s10765-013-1432-0 | PROPblock_7 | declared | 6 | binary | 2 | search_system_registry |
| 10.1007/s10765-013-1432-0 | PROPblock_8 | declared | 6 | binary | 2 | search_system_registry |
| 10.1007/s10765-015-2006-0 | PROPblock_5 | declared | 40 | binary | 2 | search_system_registry |
| 10.1007/s10765-015-2006-0 | PROPblock_6 | declared | 16 | binary | 2 | search_system_registry |
| 10.1007/s10765-015-2006-0 | PROPblock_7 | declared | 40 | binary | 2 | search_system_registry |
| 10.1007/s10765-015-2006-0 | PROPblock_8 | declared | 36 | binary | 2 | search_system_registry |
| 10.1007/s10765-015-2009-x | PROPblock_3 | declared | 24 | binary | 2 | search_system_registry |
| 10.1007/s10765-016-2089-2 | PROPblock_3 | declared | 45 | binary | 2 | search_system_registry |
| 10.1007/s10765-018-2359-2 | PROPblock_4 | declared | 20 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2004.11.019 | PROPblock_2 | declared | 810 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2006.03.012 | PROPblock_6 | declared | 4 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2006.05.007 | PROPblock_1 | declared | 45 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2006.05.015 | PROPblock_2 | declared | 42 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2006.05.015 | PROPblock_3 | declared | 114 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2006.05.028 | PROPblock_7 | declared | 20 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2006.05.028 | PROPblock_9 | declared | 20 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2006.12.005 | PROPblock_3 | declared | 8 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2006.12.005 | PROPblock_4 | declared | 2 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2007.01.043 | PROPblock_2 | declared | 2 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2007.01.043 | PROPblock_4 | declared | 2 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2007.07.066 | PROPblock_5 | declared | 95 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2007.07.066 | PROPblock_6 | declared | 95 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2007.07.066 | PROPblock_7 | declared | 15 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2007.07.066 | PROPblock_8 | declared | 15 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2008.01.004 | PROPblock_2 | declared | 125 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2008.01.004 | PROPblock_3 | declared | 125 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2008.01.004 | PROPblock_4 | declared | 15 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2008.01.004 | PROPblock_5 | declared | 15 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2008.04.003 | PROPblock_2 | declared | 35 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2009.06.008 | PROPblock_2 | declared | 42 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2009.07.010 | PROPblock_14 | declared | 19 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2009.07.010 | PROPblock_16 | declared | 28 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2009.07.010 | PROPblock_18 | declared | 8 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.01.002 | PROPblock_19 | declared | 72 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.01.020 | PROPblock_26 | declared | 78 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.03.017 | PROPblock_7 | declared | 18 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.05.001 | PROPblock_11 | declared | 52 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.05.001 | PROPblock_7 | declared | 60 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.07.005 | PROPblock_8 | declared | 30 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.08.004 | PROPblock_1 | declared | 70 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.08.004 | PROPblock_2 | declared | 70 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2010.10.005 | PROPblock_1 | declared | 34 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2011.01.001 | PROPblock_7 | declared | 56 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2011.01.001 | PROPblock_8 | declared | 56 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2011.01.001 | PROPblock_9 | declared | 56 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2011.02.017 | PROPblock_2 | declared | 9 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2011.03.031 | PROPblock_2 | declared | 29 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2011.05.017 | PROPblock_2 | declared | 9 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2011.06.008 | PROPblock_6 | declared | 5 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2011.11.028 | PROPblock_2 | declared | 6 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2011.11.028 | PROPblock_4 | declared | 6 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2011.11.028 | PROPblock_6 | declared | 6 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2011.11.028 | PROPblock_8 | declared | 6 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2012.04.003 | PROPblock_1 | declared | 6 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2012.05.007 | PROPblock_6 | declared | 4 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2012.05.007 | PROPblock_9 | declared | 16 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2012.06.002 | PROPblock_5 | declared | 2 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2012.06.002 | PROPblock_8 | declared | 2 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2012.08.024 | PROPblock_6 | declared | 4 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2012.08.024 | PROPblock_8 | declared | 6 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2012.10.024 | PROPblock_3 | declared | 54 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2012.10.024 | PROPblock_4 | declared | 54 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2012.10.024 | PROPblock_5 | declared | 114 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2012.10.024 | PROPblock_6 | declared | 126 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.01.004 | PROPblock_10 | declared | 1 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.01.004 | PROPblock_13 | declared | 1 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.01.025 | PROPblock_2 | declared | 85 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.03.030 | PROPblock_1 | declared | 3 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.03.030 | PROPblock_4 | declared | 3 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.05.006 | PROPblock_1 | declared | 6 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.05.006 | PROPblock_3 | declared | 6 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.05.006 | PROPblock_5 | declared | 6 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.08.005 | PROPblock_5 | declared | 20 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.08.007 | PROPblock_4 | declared | 1,110 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.11.015 | PROPblock_2 | declared | 85 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.11.015 | PROPblock_3 | declared | 85 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.11.028 | PROPblock_10 | declared | 25 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.11.028 | PROPblock_13 | declared | 25 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.11.028 | PROPblock_16 | declared | 25 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2013.11.028 | PROPblock_7 | declared | 25 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.01.038 | PROPblock_1 | declared | 8 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.01.038 | PROPblock_2 | declared | 8 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.01.038 | PROPblock_3 | declared | 8 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.01.044 | PROPblock_3 | declared | 5 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.03.019 | PROPblock_14 | declared | 2 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.03.019 | PROPblock_17 | declared | 2 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.05.032 | PROPblock_1 | declared | 140 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.05.043 | PROPblock_2 | declared | 18 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.05.043 | PROPblock_4 | declared | 18 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.08.026 | PROPblock_1 | declared | 5 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.08.026 | PROPblock_3 | declared | 4 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.08.026 | PROPblock_5 | declared | 4 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.08.026 | PROPblock_7 | declared | 4 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.09.020 | PROPblock_1 | declared | 40 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.09.020 | PROPblock_4 | declared | 40 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.09.020 | PROPblock_7 | declared | 40 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.09.026 | PROPblock_11 | declared | 3 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.09.026 | PROPblock_13 | declared | 3 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.11.005 | PROPblock_10 | declared | 48 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.11.005 | PROPblock_13 | declared | 36 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.11.005 | PROPblock_14 | declared | 36 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.11.005 | PROPblock_5 | declared | 60 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2014.11.005 | PROPblock_6 | declared | 60 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2016.01.036 | PROPblock_12 | declared | 4 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2016.02.035 | PROPblock_6 | declared | 126 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2016.07.022 | PROPblock_18 | declared | 4 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2017.02.019 | PROPblock_5 | declared | 40 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2017.12.001 | PROPblock_11 | declared | 88 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2018.03.002 | PROPblock_12 | declared | 14 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2018.03.002 | PROPblock_3 | declared | 9 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2018.03.002 | PROPblock_6 | declared | 12 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2018.03.002 | PROPblock_9 | declared | 12 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2018.08.011 | PROPblock_6 | declared | 323 | binary | 2 | search_system_registry |
| 10.1016/j.fluid.2018.12.017 | PROPblock_2 | declared | 28 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2005.01.009 | PROPblock_1 | declared | 45 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2005.03.021 | PROPblock_1 | declared | 162 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2005.04.005 | PROPblock_3 | declared | 15 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2005.10.013 | PROPblock_2 | declared | 24 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2006.01.007 | PROPblock_1 | declared | 6 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2006.01.007 | PROPblock_3 | declared | 6 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2006.03.009 | PROPblock_1 | declared | 5 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2006.03.009 | PROPblock_3 | declared | 5 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2006.03.009 | PROPblock_5 | declared | 5 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2006.08.003 | PROPblock_2 | declared | 4 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2006.08.003 | PROPblock_4 | declared | 6 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2006.08.003 | PROPblock_6 | declared | 4 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2006.08.003 | PROPblock_8 | declared | 6 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2006.08.007 | PROPblock_1 | declared | 9 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2006.08.007 | PROPblock_3 | declared | 8 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2006.08.007 | PROPblock_5 | declared | 10 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2006.08.007 | PROPblock_7 | declared | 7 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.04.009 | PROPblock_1 | declared | 12 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.05.010 | PROPblock_11 | declared | 8 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.05.010 | PROPblock_13 | declared | 9 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.05.010 | PROPblock_15 | declared | 9 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.05.010 | PROPblock_9 | declared | 10 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.05.011 | PROPblock_7 | declared | 195 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.05.015 | PROPblock_13 | declared | 38 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.05.015 | PROPblock_15 | declared | 35 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.05.015 | PROPblock_17 | declared | 40 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.05.015 | PROPblock_19 | declared | 27 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.05.015 | PROPblock_21 | declared | 25 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.05.015 | PROPblock_23 | declared | 30 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.06.007 | PROPblock_2 | declared | 40 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.06.007 | PROPblock_5 | declared | 40 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.10.007 | PROPblock_1 | declared | 11 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.10.007 | PROPblock_3 | declared | 11 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2007.10.007 | PROPblock_5 | declared | 11 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2008.01.003 | PROPblock_1 | declared | 130 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2008.01.018 | PROPblock_3 | declared | 120 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2008.09.005 | PROPblock_10 | declared | 65 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2008.09.005 | PROPblock_12 | declared | 105 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2008.09.005 | PROPblock_6 | declared | 85 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2008.09.005 | PROPblock_8 | declared | 70 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2008.09.008 | PROPblock_2 | declared | 10 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2009.01.010 | PROPblock_17 | declared | 16 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2009.01.010 | PROPblock_20 | declared | 16 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2009.01.010 | PROPblock_23 | declared | 16 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2009.01.010 | PROPblock_26 | declared | 16 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2009.03.004 | PROPblock_1 | declared | 50 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2009.03.004 | PROPblock_3 | declared | 50 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2009.03.004 | PROPblock_5 | declared | 50 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2009.08.004 | PROPblock_1 | declared | 5 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2009.10.007 | PROPblock_2 | declared | 75 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2009.11.017 | PROPblock_3 | declared | 57 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2010.04.018 | PROPblock_1 | declared | 40 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2010.04.018 | PROPblock_3 | declared | 35 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2010.04.018 | PROPblock_5 | declared | 35 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2010.08.021 | PROPblock_3 | declared | 150 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2010.08.021 | PROPblock_6 | declared | 96 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2010.08.021 | PROPblock_9 | declared | 102 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2010.11.003 | PROPblock_2 | declared | 80 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2010.11.017 | PROPblock_5 | declared | 54 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2010.11.017 | PROPblock_8 | declared | 30 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2011.01.013 | PROPblock_11 | declared | 13 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2011.01.013 | PROPblock_14 | declared | 10 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2011.01.013 | PROPblock_17 | declared | 12 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2011.01.013 | PROPblock_2 | declared | 10 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2011.01.013 | PROPblock_5 | declared | 11 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2011.01.013 | PROPblock_8 | declared | 16 | binary | 2 | search_system_registry |
| 10.1016/j.jct.2011.01.014 | PROPblock_11 | declared | 195 | binary | 2 | search_system_registry |

</details>

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 2 | `resolve_compound_ids` | limit=5, min_score=80, purpose=Resolve water to it… | 148 | KEEP ←in 216 | 148 | 3.7 |
| 2 | 3 | `search_system_summary` | compound=GLOBcomp_1, limit=20, property=GLOBprop_8… | 1,350 | KEEP ←in 1,240 | 1350 | 11.2 |
| 3 | 4 | `search_system_registry` | compound=GLOBcomp_1, limit=100, property=GLOBprop_… | 2,008 | KEEP ←in 16,757 | 1789 | 42.6 |
| 4 | 1 | `L1_query` | context=User wants to validate an aco…, id_catalog… | 7,089 | — | — | 132.5 |
| 5 | 2 | `search_system_summary` | limit=20, property=GLOBprop_1, purpose=Get aggrega… | 906 | KEEP ←in 792 | 906 | 17.4 |
| 6 | 3 | `resolve_compound_ids` | purpose=Resolve water to GLOBcomp_N f…, queries=wa… | 170 | KEEP ←in 216 | 170 | 3.8 |
| 7 | 4 | `search_system_summary` | compound=GLOBcomp_1, limit=20, property=GLOBprop_1… | 1,319 | KEEP ←in 1,283 | 1319 | 17.6 |
| 8 | 5 | `search_system_registry` | compound=GLOBcomp_1, limit=100, property=GLOBprop_… | 2,070 | KEEP ←in 16,995 | 2070 | 38.5 |
| 9 | 2 | `L1_query` | context=User wants to know if speed-o…, id_catalog… | 10,348 | — | — | 173.2 |
| | | **TOTAL (9 tools)** | | **25,408** | | **7,752** | **440.5** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 670 | 12,251 | 1,437 | 10.6 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,302 | 25,397 | 719 | 5.7 |
| 3 | L1-worker | claudeopus46 | 24,095 | 2,278 | 26,373 | 558 | 4.0 |
| 4 | L1-worker | claudeopus46 | 3,767 | 349 | 4,116 | 285 | 3.6 |
| 5 | L1-worker | claudeopus46 | 24,095 | 1,878 | 25,973 | 1,610 | 9.8 |
| 6 | L1-worker | claudeopus46 | 3,767 | 1,753 | 5,520 | 1,748 | 10.7 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,607 | 27,702 | 1,025 | 9.1 |
| 8 | L1-worker | claudeopus46 | 3,767 | 17,229 | 20,996 | 1,758 | 15.8 |
| 9 | L1-worker | claudeopus46 | 3,767 | 17,531 | 21,298 | 2,117 | 20.2 |
| 10 | L1-worker | claudeopus46 | 24,095 | 6,021 | 30,116 | 3,842 | 27.0 |
| 11 | L1-worker | claudeopus46 | 2,320 | 3,403 | 5,723 | 988 | 6.7 |
| 12 | L1-worker | claudeopus46 | 2,106 | 4,826 | 6,932 | 1,291 | 7.3 |
| 13 | L1-worker | claudeopus46 | 627 | 3,283 | 3,910 | 1,337 | 8.8 |
| 14 | L1-worker | claudeopus46 | 366 | 1,425 | 1,791 | 976 | 4.2 |
| 15 | L1-worker | claudeopus46 | 366 | 2,068 | 2,434 | 479 | 3.6 |
| 16 | L1-worker | claudeopus46 | 787 | 10,323 | 11,110 | 725 | 6.5 |
| 17 | L0-main | claudeopus46 | 11,581 | 15,780 | 27,361 | 1,685 | 11.7 |
| 18 | L1-worker | claudeopus46 | 24,095 | 9,229 | 33,324 | 981 | 6.9 |
| 19 | L1-worker | claudeopus46 | 24,095 | 10,341 | 34,436 | 685 | 4.4 |
| 20 | L1-worker | claudeopus46 | 3,767 | 1,291 | 5,058 | 1,225 | 8.9 |
| 21 | L1-worker | claudeopus46 | 24,095 | 10,622 | 34,717 | 1,212 | 8.9 |
| 22 | L1-worker | claudeopus46 | 3,767 | 372 | 4,139 | 325 | 3.5 |
| 23 | L1-worker | claudeopus46 | 24,095 | 11,161 | 35,256 | 737 | 5.9 |
| 24 | L1-worker | claudeopus46 | 3,767 | 1,770 | 5,537 | 1,612 | 10.4 |
| 25 | L1-worker | claudeopus46 | 24,095 | 12,842 | 36,937 | 1,087 | 7.5 |
| 26 | L1-worker | claudeopus46 | 3,767 | 17,448 | 21,215 | 1,615 | 13.8 |
| 27 | L1-worker | claudeopus46 | 3,767 | 17,750 | 21,517 | 2,588 | 21.1 |
| 28 | L1-worker | claudeopus46 | 24,095 | 15,432 | 39,527 | 5,563 | 38.7 |
| 29 | L1-worker | claudeopus46 | 2,106 | 6,438 | 8,544 | 1,563 | 8.0 |
| 30 | L1-worker | claudeopus46 | 2,320 | 4,652 | 6,972 | 1,934 | 8.7 |
| 31 | L1-worker | claudeopus46 | 627 | 4,532 | 5,159 | 1,641 | 10.1 |
| 32 | L1-worker | claudeopus46 | 366 | 2,340 | 2,706 | 710 | 4.1 |
| 33 | L1-worker | claudeopus46 | 366 | 2,371 | 2,737 | 1,879 | 5.6 |
| 34 | L1-worker | claudeopus46 | 787 | 14,831 | 15,618 | 796 | 7.5 |
| 35 | L0-main | claudeopus46 | 11,581 | 36,562 | 48,143 | 4,693 | 31.2 |
| 36 | L0-main | claudeopus46 | 2,106 | 5,094 | 7,200 | 1,007 | 6.6 |
| 37 | L0-main | claudeopus46 | 2,320 | 4,592 | 6,912 | 1,306 | 8.1 |
| 38 | L0-main | claudeopus46 | 366 | 1,556 | 1,922 | 1,375 | 5.2 |
| 39 | L0-main | claudeopus46 | 366 | 1,781 | 2,147 | 1,257 | 4.4 |
| 40 | L0-main | claudeopus46 | 560 | 6,159 | 6,719 | 310 | 2.7 |
| 41 | L0-main | claudeopus46 | 560 | 5,489 | 6,049 | 481 | 5.2 |
| 42 | L0-main | claudeopus46 | 366 | 1,063 | 1,429 | 15 | 1.7 |

