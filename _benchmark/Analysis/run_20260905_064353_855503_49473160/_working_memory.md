# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064353_855503_49473160`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_2 | ethanol |  |
| comp | GLOBcomp_1 | water |  |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_3 | pressurekpa |  |
| var | GLOBvar_2 | molefraction<ethanol> |  |

### History
- [query_thermoml]
- [query_thermoml_parallel]
- [inspect_block]
- [fit_multi_system]
- [fit_multi_system]

### Query Results
#### query
**L1_query_1** — status: partial · validation: FLAGGED(2)

**Summary:** In the ThermoML database, one confirmed block of binary ethanol + water mass density data was identified: GLOBlit_1483 :: PROPblock_1 (DOI 10.1016/j.fluid.2014.05.032), containing 140 data points spanning 292.95–448.15 K, 2450–40140 kPa, and ethanol mole fractions 0.0163–0.0946 (dilute ethanol region only). Representative values at the 348.15 K isotherm show density decreasing with increasing ethanol mole fraction (e.g., ~982.3 kg/m³ at x=0.0163 and 39600 kPa down to ~933.7 kg/m³ at x=0.0946 and 2730 kPa) and increasing with pressure at each composition. This dataset covers only elevated pressures (2.5–40 MPa) and dilute ethanol compositions; it does not provide atmospheric-pressure or full-composition-range data. An initially returned block GLOBlit_1742 :: PROPblock_1 was confirmed upon inspection to be methanol + water, not ethanol + water. Two other blocks (GLOBlit_220 and GLOBlit_2432) were returned by the initial search but were not inspected, so their coverage cannot be confirmed.

**Answer:**

**Binary ethanol–water mass density data in the ThermoML database:**

The search for binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) mass density (GLOBprop_1) blocks found the following confirmed result:

##### Confirmed ethanol–water block

**GLOBlit_1483 :: PROPblock_1**  
- **DOI:** 10.1016/j.fluid.2014.05.032  
- **System:** binary ethanol + water  
- **Data points:** 140  
- **Temperature range:** 292.95–448.15 K (includes isotherms at 348.15 K, near the user-requested target of ~350 K)  
- **Pressure range:** 2450–40140 kPa (high-pressure data)  
- **Ethanol mole fraction range:** 0.0163–0.0946 (dilute ethanol region only)  

Representative data at 348.15 K (nearest isotherm to the requested ~350 K target):

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *Ethanol x* | *P (kPa)* | *ρ (kg/m³)* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.0163」 | 「39600」 | 「982.3」 |
| WM_L1#1_Table#1_Row#2 | 「0.0163」 | 「20750」 | 「974.7」 |
| WM_L1#1_Table#1_Row#3 | 「0.0163」 | 「10980」 | 「970.6」 |
| WM_L1#1_Table#1_Row#4 | 「0.0163」 | 「3220」 | 「967.1」 |
| WM_L1#1_Table#1_Row#5 | 「0.0343」 | 「39860」 | 「974.7」 |
| WM_L1#1_Table#1_Row#6 | 「0.0343」 | 「30850」 | 「971.3」 |
| WM_L1#1_Table#1_Row#7 | 「0.0343」 | 「21160」 | 「967.5」 |
| WM_L1#1_Table#1_Row#8 | 「0.0343」 | 「11590」 | 「963.5」 |
| WM_L1#1_Table#1_Row#9 | 「0.073」 | 「39600」 | 「958.9」 |
| WM_L1#1_Table#1_Row#10 | 「0.073」 | 「20870」 | 「950.8」 |
| WM_L1#1_Table#1_Row#11 | 「0.073」 | 「11060」 | 「946.6」 |
| WM_L1#1_Table#1_Row#12 | 「0.073」 | 「3330」 | 「943.0」 |
| WM_L1#1_Table#1_Row#13 | 「0.0946」 | 「37790」 | 「948.7」 |
| WM_L1#1_Table#1_Row#14 | 「0.0946」 | 「29730」 | 「945.4」 |
| WM_L1#1_Table#1_Row#15 | 「0.0946」 | 「20870」 | 「941.6」 |
| WM_L1#1_Table#1_Row#16 | 「0.0946」 | 「11390」 | 「937.4」 |
| WM_L1#1_Table#1_Row#17 | 「0.0946」 | 「2730」 | 「933.7」 |

**Note:** This dataset covers only dilute ethanol compositions (up to ~9.5 mol%) at elevated pressures (2.5–40 MPa). It does not provide atmospheric-pressure or full-composition-range density data.

##### Other blocks from the initial search

- **GLOBlit_1742 :: PROPblock_1** — Upon inspection, this block is actually **methanol + water** (not ethanol + water) and is therefore not relevant to this query.  
- **GLOBlit_220** and **GLOBlit_2432** were also returned by the initial search as potential ethanol–water density blocks, but these were not inspected in this run, so their exact composition/temperature coverage and data point counts cannot be confirmed here.

**Chemistry note:** The inspected data show the expected trend: at 348.15 K, density decreases with increasing ethanol mole fraction (from ~982 kg/m³ at x = 0.0163 to ~949 kg/m³ at x = 0.0946 at comparable pressures), and increases with pressure at each composition, consistent with the lower density of ethanol relative to water and normal liquid compressibility behavior.

**Core claims:**
- The ThermoML database contains a confirmed binary ethanol–water mass density block (GLOBlit_1483 :: PROPblock_1, DOI 10.1016/j.fluid.2014.05.032) with 140 data points spanning 292.95–448.15 K, 2450–40140 kPa, and ethanol mole fractions of 0.0163–0.0946 (dilute ethanol region only).
- At 348.15 K, the data show density decreasing with increasing ethanol mole fraction (from ~982 kg/m³ at x = 0.0163 to ~949 kg/m³ at x = 0.0946 at comparable pressures) and increasing with pressure at each composition, consistent with the lower density of ethanol relative to water and normal liquid compressibility.
- This dataset covers only dilute ethanol compositions (up to ~9.5 mol%) at elevated pressures (2.5–40 MPa) and does not provide atmospheric-pressure or full-composition-range density data.
- Two additional blocks (GLOBlit_220 and GLOBlit_2432) were returned by the initial search as potential ethanol–water density blocks but were not inspected, so their coverage cannot be confirmed.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_1483」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for binary ethanol + water mixtures at 292.95–448.15 K and 2450–40140 kPa, covering ethanol mole fractions 0.0163–0.0946; 140 data points.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** GLOBlit_1483::PROPblock_1: 350 (near '…s isotherms at 348.15 K, near the user-requested target of ~…') matches no inspected row/stat, database table, or other source of GLOBlit_1483::PROPblock_1
- **UNGROUNDED_LITERAL** GLOBlit_1483::PROPblock_1: 350 (near '…tative data at 348.15 K (nearest isotherm to the requested ~…') matches no inspected row/stat, database table, or other source of GLOBlit_1483::PROPblock_1


#### broad_search
**L1_query_2** — status: success · validation: FLAGGED(2)

**Summary:** For binary ethanol + water mass density at atmospheric pressure, the best ThermoML source identified is GLOBlit_220 :: PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019), providing 162 atmospheric-pressure points (P = 100 kPa) across three isotherms (298.15, 323.15, and 348.15 K) with x(ethanol) = 0.003–1.0 and densities from 739.4 to 995.3 kg/m³. A supplementary source is GLOBlit_5201 :: PROPblock_19 (DOI: 10.1016/j.jct.2018.02.022) with 244 points at P = 92.3 kPa, four isotherms from 293.15 to 308.15 K, x(ethanol) = 0–1, and densities 776.592–998.429 kg/m³. GLOBlit_2825 :: PROPblock_12 (DOI: 10.1016/j.jct.2007.05.004) offers 37 points at 101.0 kPa, 293.15–303.15 K, x(water) = 0–1, densities 781.15–998.2 kg/m³. No inspected block reaches the upper target temperature of 353 K at atmospheric pressure; the highest verified atmospheric-pressure isotherm is 348.15 K in GLOBlit_220.

**Answer:**

#### Binary Ethanol + Water Mass Density Blocks at Atmospheric Pressure

##### Best Candidate: GLOBlit_220 :: PROPblock_2
**DOI:** 10.1016/j.fluid.2004.11.019

This block is the strongest match for wide-composition, multi-temperature density data at atmospheric pressure:

- **Total points:** 810 (162 at atmospheric pressure, P = 100 kPa)
- **Temperatures:** 298.15, 323.15, and 348.15 K (three isotherms)
- **Composition range:** x(ethanol) = 0.003–1.0 (full range)
- **Density range (at 100 kPa):** 739.4–995.3 kg/m³

Representative atmospheric-pressure data (from inspection):

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *T (K)* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「298.15」 | 「0.003」 | 「995.3」 |
| WM_L1#2_Table#1_Row#2 | 「298.15」 | 「0.2502」 | 「918.5」 |
| WM_L1#2_Table#1_Row#3 | 「298.15」 | 「0.4501」 | 「868.8」 |
| WM_L1#2_Table#1_Row#4 | 「298.15」 | 「0.6967」 | 「825.2」 |
| WM_L1#2_Table#1_Row#5 | 「298.15」 | 「1.0」 | 「785.7」 |
| WM_L1#2_Table#1_Row#6 | 「323.15」 | 「0.003」 | 「986.5」 |
| WM_L1#2_Table#1_Row#7 | 「323.15」 | 「0.2269」 | 「905.2」 |
| WM_L1#2_Table#1_Row#8 | 「323.15」 | 「0.4501」 | 「846.7」 |
| WM_L1#2_Table#1_Row#9 | 「323.15」 | 「0.6967」 | 「802.8」 |
| WM_L1#2_Table#1_Row#10 | 「323.15」 | 「1.0」 | 「763.7」 |
| WM_L1#2_Table#1_Row#11 | 「348.15」 | 「0.003」 | 「973.1」 |
| WM_L1#2_Table#1_Row#12 | 「348.15」 | 「0.1903」 | 「895.8」 |
| WM_L1#2_Table#1_Row#13 | 「348.15」 | 「0.4034」 | 「833.4」 |
| WM_L1#2_Table#1_Row#14 | 「348.15」 | 「0.6489」 | 「785.6」 |
| WM_L1#2_Table#1_Row#15 | 「348.15」 | 「1.0」 | 「739.4」 |

Each isotherm has approximately 54 composition points (derived by dividing 162 atmospheric points by 3 isotherms — not a database value), providing dense composition coverage ideal for Redlich-Kister fitting.

##### Other Inspected Candidates

**GLOBlit_5201 :: PROPblock_19** (DOI: 10.1016/j.jct.2018.02.022)
- **Points:** 244, all at P = 92.3 kPa (near-atmospheric)
- **Temperature:** 293.15–308.15 K (4 isotherms)
- **Composition:** x(ethanol) = 0–1 (full range)
- **Density:** 776.592–998.429 kg/m³
- Excellent composition coverage but temperature range is narrower and lower than GLOBlit_220.

**GLOBlit_2825 :: PROPblock_12** (DOI: 10.1016/j.jct.2007.05.004)
- **Points:** 37, all at P = 101.0 kPa
- **Temperature:** 293.15–303.15 K (3 isotherms)
- **Composition:** x(water) = 0–1 (full range)
- **Density:** 781.15–998.2 kg/m³
- Full composition range at atmospheric pressure, but fewer points and lower temperatures.

##### Additional Candidates (Not Inspected)

The following blocks were identified by the search discovery tool but have not been individually inspected in this run. No specific data values are quoted for them:

- **GLOBlit_9006 :: PROPblock_1** (DOI: 10.1021/je060335h) — search-reported as having full composition range at lower temperatures.
- **GLOBlit_10866 :: PROPblock_7** (DOI: 10.1021/je700300y) — search-reported as having wide composition range.
- **GLOBlit_10699 :: PROPblock_6** (DOI: 10.1021/je600565m) — search-reported as having moderate composition range.
- **GLOBlit_11136 :: PROPblock_9** (DOI: 10.1021/je800150h) — search-reported as having partial composition range.
- **GLOBlit_5473 :: PROPblock_21** (DOI: 10.1016/j.jct.2019.02.027) — search-reported as having full composition range with very few points.

##### Regarding GLOBlit_2432
**DOI:** 10.1016/j.jct.2004.07.019, PROPblock_2 — Per search discovery results (not individually inspected), this block operates at elevated pressures, not atmospheric. **Not suitable** for atmospheric-pressure fitting.

##### Key Finding
**No block in the database was found to cover the requested upper temperature of 353 K (instruction target, not a database value) at atmospheric pressure** for this binary system. The closest inspected data is GLOBlit_220 at 348.15 K. Per search discovery results (not inspected), GLOBlit_1742 (PROPblock_3) reaches higher temperatures but only at elevated pressures.

**Recommendation:** GLOBlit_220 :: PROPblock_2 is the best single source — it provides dense composition coverage at 100 kPa across 298.15, 323.15, and 348.15 K, with x(ethanol) = 0.003–1.0. GLOBlit_5201 :: PROPblock_19 (244 pts, x = 0–1, T = 293.15–308.15 K, P = 92.3 kPa) could supplement with additional near-ambient data.

**Core claims:**
- GLOBlit_220 :: PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019) is identified as the best single source for binary ethanol + water mass density data at atmospheric pressure, providing 162 points at P = 100 kPa across three isotherms (298.15, 323.15, and 348.15 K) with x(ethanol) = 0.003–1.0 and densities ranging from 739.4–995.3 kg/m³.
- At each isotherm in GLOBlit_220 :: PROPblock_2, density decreases monotonically with increasing ethanol mole fraction at 100 kPa, and density decreases with increasing temperature at fixed composition.
- GLOBlit_5201 :: PROPblock_19 (DOI: 10.1016/j.jct.2018.02.022) provides a supplementary 244-point dataset at P = 92.3 kPa over T = 293.15–308.15 K with x(ethanol) = 0–1 and densities of 776.592–998.429 kg/m³, but covers a narrower and lower temperature range than GLOBlit_220.
- No block in the database was found to cover 353 K at atmospheric pressure for this binary system; the closest inspected atmospheric-pressure data reaches 348.15 K (GLOBlit_220). The value 353 K is identified as an instruction target, not a database value.
- The stated count of approximately 54 composition points per isotherm in GLOBlit_220 :: PROPblock_2 is derived by dividing 162 atmospheric points by 3 isotherms and is flagged as UNVERIFIED against the database.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_220」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of binary ethanol + water at 100 kPa across 298.15–348.15 K, x(ethanol) = 0.003–1.0, 162 atmospheric-pressure points from 810 total.」 |
| WM_L1#2_Table#3 | 「GLOBlit_5201」 | 「PROPblock_19」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of binary ethanol + water at 92.3 kPa across 293.15–308.15 K, x(ethanol) = 0–1, 244 points.」 |
| WM_L1#2_Table#4 | 「GLOBlit_2825」 | 「PROPblock_12」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of binary ethanol + water at 101.0 kPa across 293.15–303.15 K, x(water) = 0–1, 37 points.」 |

*Not stored here: 4 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** GLOBlit_220::PROPblock_2: 54 (near '…Each isotherm has approximately 54 composition points (deriv…') matches no inspected row/stat, database table, or other source of GLOBlit_220::PROPblock_2
- **UNGROUNDED_LITERAL** PROPblock_2: 353 (near '…abase was found to cover the requested upper temperature of …') matches no inspected row/stat, database table, or other source of PROPblock_2


#### inspect_220
**L1_query_3** — status: success · validation: PASS

**Summary:** GLOBlit_220 PROPblock_1 (DOI 10.1016/j.fluid.2004.11.019) contains pure ethanol density data only, not ethanol + water mixture data. The block reports 15 liquid-phase mass density measurements for pure ethanol (C₂H₆O) over 298.15–348.15 K and 100–40000 kPa, with densities ranging from 739.4 to 815.7 kg/m³. No water is present; no composition variable is included. Binary ethanol–water mixture data, if present in this DOI, would be in other blocks (e.g., PROPblock_2, PROPblock_3, etc.).

**Answer:**

**GLOBlit_220 PROPblock_1 — Inspection Result**

This block contains **pure ethanol density data only** — it is **not** ethanol + water mixture data.

**Details:**

**WM_L1#3_Table#1_(Analysis_L1#3_Answer):**

| *row_id* | *Field* | *Value* |
|---|---|---|
| WM_L1#3_Table#1_Row#1 | 「DOI」 | 「10.1016/j.fluid.2004.11.019 (GLOBlit_220)」 |
| WM_L1#3_Table#1_Row#2 | 「Block」 | 「PROPblock_1」 |
| WM_L1#3_Table#1_Row#3 | 「System type」 | 「Unary (pure component)」 |
| WM_L1#3_Table#1_Row#4 | 「Compound」 | 「Ethanol (GLOBcomp_2, C₂H₆O)」 |
| WM_L1#3_Table#1_Row#5 | 「Property」 | 「Mass density (GLOBprop_1), kg/m³」 |
| WM_L1#3_Table#1_Row#6 | 「Phase」 | 「Liquid」 |
| WM_L1#3_Table#1_Row#7 | 「Temperature range」 | 「298.15–348.15 K (15 points)」 |
| WM_L1#3_Table#1_Row#8 | 「Pressure range」 | 「100–40000 kPa (15 points)」 |
| WM_L1#3_Table#1_Row#9 | 「Density range」 | 「739.4–815.7 kg/m³ (15 points)」 |
| WM_L1#3_Table#1_Row#10 | 「Data points」 | 「15 total (12 shown via RDP)」 |
| WM_L1#3_Table#1_Row#11 | 「Composition」 | 「None (pure ethanol — no water present)」 |

**Inspected data (12 of 15 points shown):**

**WM_L1#3_Table#2_(Analysis_L1#3_Answer):**

| *row_id* | *BLKpoint_id* | *Temperature (K)* | *Pressure (kPa)* | *Mass density (kg/m³)* |
|---|---|---|---|---|
| WM_L1#3_Table#2_Row#1 | 「BLKpoint_1」 | 「298.15」 | 「100」 | 「785.7」 |
| WM_L1#3_Table#2_Row#2 | 「BLKpoint_3」 | 「298.15」 | 「20000」 | 「801.9」 |
| WM_L1#3_Table#2_Row#3 | 「BLKpoint_5」 | 「298.15」 | 「40000」 | 「815.7」 |
| WM_L1#3_Table#2_Row#4 | 「BLKpoint_6」 | 「323.15」 | 「100」 | 「763.7」 |
| WM_L1#3_Table#2_Row#5 | 「BLKpoint_7」 | 「323.15」 | 「10000」 | 「773.4」 |
| WM_L1#3_Table#2_Row#6 | 「BLKpoint_8」 | 「323.15」 | 「20000」 | 「782.3」 |
| WM_L1#3_Table#2_Row#7 | 「BLKpoint_10」 | 「323.15」 | 「40000」 | 「797.7」 |
| WM_L1#3_Table#2_Row#8 | 「BLKpoint_11」 | 「348.15」 | 「100」 | 「739.4」 |
| WM_L1#3_Table#2_Row#9 | 「BLKpoint_12」 | 「348.15」 | 「10000」 | 「751.2」 |
| WM_L1#3_Table#2_Row#10 | 「BLKpoint_13」 | 「348.15」 | 「20000」 | 「761.2」 |
| WM_L1#3_Table#2_Row#11 | 「BLKpoint_14」 | 「348.15」 | 「30000」 | 「770.3」 |
| WM_L1#3_Table#2_Row#12 | 「BLKpoint_15」 | 「348.15」 | 「40000」 | 「778.6」 |

**Conclusion:** This block does **not** contain ethanol + water binary density data. Although the parent DOI (10.1016/j.fluid.2004.11.019) references ethanol–water mixtures in its title, PROPblock_1 specifically holds only pure ethanol measurements. Other blocks within GLOBlit_220 (e.g., PROPblock_2, PROPblock_3, etc.) should be checked for the binary mixture data.

**Core claims:**
- GLOBlit_220 PROPblock_1 contains pure ethanol density data only, not ethanol + water binary mixture data, despite the parent DOI (10.1016/j.fluid.2004.11.019) referencing ethanol–water mixtures in its title.
- The block reports 15 liquid-phase mass density data points for pure ethanol spanning 298.15–348.15 K in temperature, 100–40000 kPa in pressure, and 739.4–815.7 kg/m³ in density.
- Other blocks within GLOBlit_220 (e.g., PROPblock_2, PROPblock_3) would need to be checked for binary ethanol + water mixture data.

**Core blocks found:**

**WM_L1#3_Blocks_(Analysis_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#3 | 「GLOBlit_220」 | 「PROPblock_1」 | 「GLOBcomp_2」 | 「GLOBprop_1」 | 「Pure ethanol mass density measurements at 298.15–348.15 K and 100–40000 kPa, 15 data points, liquid phase. Not ethanol+water binary data.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### inspect_2432
**L1_query_4** — status: success · validation: PASS

**Summary:** GLOBlit_2432 PROPblock_1 does not contain ethanol + water density data. It contains methanol + water density data. The DOI is 10.1016/j.jct.2004.07.019. The compounds are water (GLOBcomp_1) and methanol (GLOBcomp_4). The property is mass density (kg/m³), measured as density differences relative to pure water using the vibrating-tube method, in the liquid phase. The temperature range is 298.16–573.15 K, pressure range is 390–30320 kPa, methanol molality range is 0.07706–1.04694 mol/kg, and there are 596 data points. Density difference values range from −13.3065 to −0.4632 kg/m³, all negative, indicating methanol solutions are less dense than pure water at the same T and P. For example, at 298.16 K and 14450 kPa, the density difference at methanol molality 0.10243 mol/kg is −0.6308 kg/m³ and at molality 0.98932 mol/kg is −5.7028 kg/m³. The second component is methanol (CH₄O), not ethanol.

**Answer:**

**Inspection of GLOBlit_2432 PROPblock_1**

This block does **not** contain ethanol + water density data. It contains **methanol + water** density data instead.

**Details:**

- **DOI:** 10.1016/j.jct.2004.07.019 (GLOBlit_2432)
- **Compounds:** water (GLOBcomp_1) + methanol (GLOBcomp_4) — a binary system
- **Property:** Mass density (kg/m³), measured as density differences relative to pure solvent water, using the vibrating-tube method
- **Phase:** Liquid
- **Temperature range:** 298.16–573.15 K
- **Pressure range:** 390–30320 kPa (high-pressure measurements)
- **Composition range:** Methanol molality 0.07706–1.04694 mol/kg
- **Total data points:** 596
- **Density difference values:** range from −13.3065 to −0.4632 kg/m³ (all negative, indicating methanol solutions are less dense than pure water at the same T and P)

For example, at 298.16 K and 14450 kPa, the density difference at methanol molality 0.10243 mol/kg is −0.6308 kg/m³ (BLKpoint_1), while at molality 0.98932 mol/kg it is −5.7028 kg/m³ (BLKpoint_6), showing the expected trend of increasing density reduction with higher methanol content.

**Conclusion:** This block is **not** ethanol + water mass density data. The second component is methanol (CH₄O, GLOBcomp_4), not ethanol.

**Core claims:**
- PROPblock_1 of GLOBlit_2432 (DOI 10.1016/j.jct.2004.07.019) contains methanol + water density data, not ethanol + water density data; the second component is methanol (CH₄O, GLOBcomp_4).
- The block reports liquid-phase mass density differences (kg/m³) relative to pure water for the methanol + water binary system, covering 298.16–573.15 K, 390–30320 kPa, methanol molality 0.07706–1.04694 mol/kg, with 596 data points.
- All reported density difference values are negative (ranging from −13.3065 to −0.4632 kg/m³), indicating that methanol solutions are less dense than pure water at the same temperature and pressure, with the magnitude of the density reduction increasing with higher methanol content.

**Core blocks found:**

**WM_L1#4_Blocks_(Analysis_L1#4_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#4_Table#1 | 「GLOBlit_2432」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density difference measurements for methanol + water at 298.16–573.15 K, 390–30320 kPa, methanol molality 0.07706–1.04694 mol/kg; 596 data points. Not ethanol + water density data.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_220 | 10.1016/j.fluid.2004.11.019 | PROPblock_2: 810 rows; x=['mole_fraction_<ethanol>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3

### Completed Fits
  - EtOH-Water_298K [10.1016/j.fluid.2004.11.019/PROPblock_2] (ethanol, water): RK order=3, R²=0.997283, RMSE=0.47476545853553287, coeffs=[-120.55681, 18.567625, 43.919128, -31.350563]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      pure refs: ethanol=785.7, water=992.083 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png
  - EtOH-Water_323K [10.1016/j.fluid.2004.11.019/PROPblock_2] (ethanol, water): RK order=5, R²=0.998545, RMSE=0.4343815607863475, coeffs=[-147.181529, 39.605693, 7.017496, -0.818149, 43.210013, -57.743228]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      pure refs: ethanol=763.7, water=983.05 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_excess.png
  - EtOH-Water_348K [10.1016/j.fluid.2004.11.019/PROPblock_2] (ethanol, water): RK order=5, R²=0.998607, RMSE=0.4911460748640253, coeffs=[-167.860024, 50.451482, -18.395033, 43.192936, 76.872347, -109.653896]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      pure refs: ethanol=739.4, water=969.467 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv` — RK fit data — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_fit.csv` — RK fit data — 10.1016/j.fluid.2004.11.019 PROPblock_2_T323.1
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_fit.csv` — RK fit data — 10.1016/j.fluid.2004.11.019 PROPblock_2_T348.1
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv` — Excess property — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_excess.csv` — Excess property — 10.1016/j.fluid.2004.11.019 PROPblock_2_T348.1
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_excess.csv` — Excess property — 10.1016/j.fluid.2004.11.019 PROPblock_2_T323.1

### plot
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_fit.png` — RK fit plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T323.1
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png` — RK fit plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_fit.png` — RK fit plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T348.1
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_excess.png` — Excess plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T323.1
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png` — Excess plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_excess.png` — Excess plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T348.1

