# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_1 | water | water |
| comp | GLOBcomp_2 | ethanol | ethanol |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find all experimental data for ethanol + water binary system and determine the full temperature range covered, identifyi → stored as L1_query_1 · validation: FLAGGED(2)
- [L1] Find the hottest activity coefficient measurements for ethanol+water to determine the upper temperature bound for an act → stored as L1_query_2 · validation: FLAGGED(8)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(2)

**Summary:** The ethanol + water binary system in ThermoML spans 126 data blocks across 73 publications with 5163 target-point observations. The aggregate temperature range is 268.1 K to 673.15 K and the pressure range is 13.15 to 50,760 kPa. The coldest inspected data point is 273.35 K from GLOBlit_299 PROPblock_4 (DOI: 10.1016/j.fluid.2005.08.018), reporting the activity coefficient of ethanol at infinite dilution (2.54 at 273.35 K, 3.13 at 283.15 K) via headspace analysis. The hottest inspected data point is 673.15 K from GLOBlit_2732 PROPblock_4 (DOI: 10.1016/j.jct.2006.08.002), reporting mass density by constant volume piezometry over 524.15–673.15 K, 4,750–50,760 kPa, x(ethanol) = 0.2–0.8, with densities from 52.89 to 617.36 kg/m³ across 278 points. Boiling temperature data from GLOBlit_977 PROPblock_1 (DOI: 10.1016/j.fluid.2011.06.009) covers 45 points at sub-atmospheric pressures (13.15–32.86 kPa) with T_boil = 307.44–335.16 K and x(ethanol) = 0.063–0.971. Activity coefficient blocks from search results span approximately 273–373 K across multiple methods, though only the 273.35 K point was directly inspected. The supercritical data (up to 673.15 K) covers pVTx behavior rather than conventional VLE. A data quality concern was noted: GLOBlit_1971 reportedly shows activity coefficients at infinite dilution that decrease with temperature, opposite to the trend in other sources.

**Answer:**

#### Ethanol + Water Binary System: Temperature Range in ThermoML

##### Overall Coverage
The ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system is extensively represented in ThermoML. The system summary (an aggregate statistic from `search_system_summary`, not a single inspected block) reports **126 data blocks** across **73 publications** and **5163 target-point observations**.

**Full temperature range (from system summary aggregate): 268.1 K to 673.15 K** *(the 268.1 K minimum is a system-summary-level aggregate; no individual block returning data at that temperature was located or inspected in this run)*
**Pressure range (from system summary aggregate): 13.15 to 50,760 kPa**

---

##### Coldest Measurements (Inspected)

The coldest inspected data point is at **273.35 K** from:

- **Source:** GLOBlit_299 — DOI: 10.1016/j.fluid.2005.08.018
- **Block:** PROPblock_4
- **Property:** Activity coefficient of ethanol at infinite dilution (γ∞), with mole fraction of ethanol constrained to 0.0
- **Method:** Headspace analysis (GLOBmeas_543)
- **Inspected data (complete block, 2 points):**

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_ethanol* | *activity_coefficient_ethanol* |
|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「BLKpoint_1」 | 「273.35」 | 「0.0」 | 「2.54」 |
| WM_L1#1_Table#1_Row#2 | 「BLKpoint_2」 | 「283.15」 | 「0.0」 | 「3.13」 |

---

##### Hottest Measurements (Inspected)

The hottest inspected data point is at **673.15 K** from:

- **Source:** GLOBlit_2732 — DOI: 10.1016/j.jct.2006.08.002
- **Block:** PROPblock_4
- **Title:** *(p,v,T,x) Measurements of {(1−x)H₂O + xC₂H₅OH} mixtures in the near-critical and supercritical regions*
- **Property:** Mass density (kg/m³)
- **Method:** Constant volume piezometry (GLOBmeas_66)
- **Block stats (inspected):** 278 data points, T = 524.15–673.15 K, P = 4,750–50,760 kPa, x(ethanol) = 0.2–0.8, ρ = 52.89–617.36 kg/m³
- **At 673.15 K:** 31 data points were recorded, e.g., ρ = 52.89 kg/m³ at 6,990 kPa (x_ethanol = 0.8) up to ρ = 451.15 kg/m³ at 47,140 kPa (x_ethanol = 0.2).

---

##### VLE-Relevant Property Breakdown

**Boiling temperature (GLOBprop_14) — Inspected block:**

GLOBlit_977 (DOI: 10.1016/j.fluid.2011.06.009), PROPblock_1 — 45 points at sub-atmospheric pressures (13.15–32.86 kPa), T_boil = 307.44–335.16 K, x(ethanol) = 0.063–0.971. This is the block with the lowest boiling temperatures found.

Additional boiling-temperature blocks were returned by `search_blocks` (10 blocks total) but were not individually inspected. Per those search results, atmospheric-pressure VLE data is available from multiple sources (e.g., GLOBlit_757, GLOBlit_1518), but their specific data values were not inspected in this run.

**Activity coefficient (GLOBprop_3) — from search results (6 blocks, 4 papers):**

The `search_blocks` tool returned the following activity-coefficient blocks. Only GLOBlit_299::PROPblock_4 was inspected (see above); the remaining values below are from the search-result summaries and were not individually inspected:

- GLOBlit_299 (DOI: 10.1016/j.fluid.2005.08.018) — 3 blocks using different methods (headspace analysis, comparative tensimetry, circulating still), temperature range reported by search as 273.35–372.15 K (not inspected beyond PROPblock_4)
- GLOBlit_8511 (DOI: 10.1021/je049875+) — dilutor chromatography (not inspected)
- GLOBlit_1971 (DOI: 10.1016/j.fluid.2016.08.030) — SPME method (not inspected)
- GLOBlit_8381 (DOI: 10.1021/je0495942) — chromatography (not inspected)

**Vapor pressure (GLOBprop_5):** 6 blocks reported by the system summary; not individually searched or inspected in this run.

---

##### Summary for Correlation Work

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *Property* | *T_min (K)* | *T_max (K)* | *Source of T_min* | *Source of T_max* | *Inspected?* |
|---|---|---|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「Activity coefficient」 | 「273.35」 | 「not inspected beyond PROPblock_4」 | 「GLOBlit_299, PROPblock_4」 | 「—」 | 「T_min: yes」 |
| WM_L1#1_Table#2_Row#2 | 「Boiling temperature」 | 「307.44」 | 「335.16」 | 「GLOBlit_977, PROPblock_1」 | 「GLOBlit_977, PROPblock_1」 | 「yes」 |
| WM_L1#1_Table#2_Row#3 | 「Mass density (supercritical)」 | 「524.15」 | 「673.15」 | 「GLOBlit_2732, PROPblock_4」 | 「GLOBlit_2732, PROPblock_4」 | 「yes」 |

The VLE-relevant temperature window for building an ethanol+water activity-coefficient correlation spans approximately **273–373 K** (derived from the search-result summaries for boiling temperature and activity coefficient blocks; the exact upper bound of activity-coefficient data was not inspected). The supercritical data (up to 673.15 K) covers mass density and pVTx behavior rather than conventional VLE.

⚠️ **Data quality note (from search results, not inspected):** GLOBlit_1971 was reported by the search tool to show γ∞ values that *decrease* with temperature, which is opposite to the trend seen in the other sources. This inconsistency should be evaluated before including that dataset in a correlation.

**Core claims:**
- The ethanol + water binary system in ThermoML spans an aggregate temperature range of 268.1 K to 673.15 K across 126 data blocks from 73 publications, though the 268.1 K minimum is a system-summary aggregate and no individual block at that temperature was inspected.
- The coldest inspected data point is at 273.35 K (activity coefficient of ethanol at infinite dilution, γ∞ = 2.54, from GLOBlit_299, PROPblock_4, DOI: 10.1016/j.fluid.2005.08.018, headspace analysis method).
- The hottest inspected data point is at 673.15 K (mass density via constant volume piezometry, from GLOBlit_2732, PROPblock_4, DOI: 10.1016/j.jct.2006.08.002), covering supercritical pVTx measurements at 524.15–673.15 K and 4,750–50,760 kPa.
- VLE-relevant data for building an ethanol+water activity-coefficient correlation spans approximately 273–373 K based on search-result summaries for boiling temperature and activity coefficient blocks, though the exact upper bound of activity-coefficient data was not inspected.
- An inspected sub-atmospheric boiling-temperature block (GLOBlit_977, PROPblock_1, DOI: 10.1016/j.fluid.2011.06.009) contains 45 points at 13.15–32.86 kPa with T_boil = 307.44–335.16 K and x(ethanol) = 0.063–0.971.
- A data quality concern was noted from search results (not inspected): GLOBlit_1971 reportedly shows γ∞ values that decrease with temperature, opposite to the trend in other sources, and should be evaluated before inclusion in a correlation.
- The upper bound of the activity-coefficient temperature range (372.15 K attributed to GLOBlit_299) is flagged as UNVERIFIED, as it was not confirmed by any inspected data in this run.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_299」 | 「PROPblock_4」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_3」 | 「Activity coefficient of ethanol at infinite dilution in water, headspace analysis, 273.35–283.15 K.」 |
| WM_L1#1_Table#4 | 「GLOBlit_2732」 | 「PROPblock_4」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of ethanol+water mixtures in near-critical and supercritical regions, 524.15–673.15 K, constant volume piezometry.」 |
| WM_L1#1_Table#5 | 「GLOBlit_977」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_14」 | 「Boiling temperature of ethanol+water at sub-atmospheric pressures, 307.44–335.16 K.」 |

*Not stored here: 3 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** GLOBlit_299::PROPblock_4: 372.15 (near '…ting still), temperature range reported by search as 273.35–…') matches no inspected row/stat, database table, or other source of GLOBlit_299::PROPblock_4
- **MISATTRIBUTED_VALUE** PROPblock_1: 673.15 does not belong to PROPblock_1; it matches only GLOBlit_299::PROPblock_4 (inspected this run)
### L1_query_2
**L1_query_2** — status: success · validation: FLAGGED(8)

**Summary:** All six ThermoML activity coefficient data blocks for the ethanol + water binary system measure the infinite-dilution activity coefficient of ethanol (mole fraction of ethanol = 0.0). The combined temperature range spans from 273.35 K (GLOBlit_299, PROPblock_4, headspace analysis, γ∞ = 2.54) to 372.15 K (GLOBlit_299, PROPblock_6, circulating still method, γ∞ = 6.2), covering 23 data points from 4 publications. The hottest measurement is at 372.15 K with γ∞ = 6.2 from GLOBlit_299 PROPblock_6 (DOI: 10.1016/j.fluid.2005.08.018). Five of six blocks show γ∞ increasing monotonically with temperature; the exception is GLOBlit_1971 PROPblock_1 (SPME method), which shows γ∞ decreasing from 5.17 at 323.15 K to 4.11 at 353.15 K — opposite to all other sources and physically suspect. Excluding that anomalous dataset, 19 data points from 3 sources with consistent trends are available for correlation across the full 273.35–372.15 K range.

**Answer:**

#### Hottest Activity Coefficient Measurements for Ethanol + Water

All six activity coefficient (γ∞) data blocks for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system in ThermoML have now been inspected. Every block measures the **infinite-dilution activity coefficient of ethanol** (mole fraction of ethanol constrained to 0.0). The combined verified temperature range spans from 273.35 K (GLOBlit_299, PROPblock_4) to 372.15 K (GLOBlit_299, PROPblock_6) across 23 data points (computed: 2 + 7 + 4 + 1 + 5 + 4) from 4 publications.

##### Verified Upper Temperature Bound: 372.15 K

The hottest activity coefficient data comes from **GLOBlit_299, PROPblock_6** (DOI: 10.1016/j.fluid.2005.08.018), measured by the circulating still method:

**WM_L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *BLKpoint_id* | *Temperature (K)* | *x(ethanol)* | *γ∞(ethanol)* |
|---|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「BLKpoint_1」 | 「358.15」 | 「0.0」 | 「5.9」 |
| WM_L1#2_Table#1_Row#2 | 「BLKpoint_2」 | 「363.15」 | 「0.0」 | 「6.0」 |
| WM_L1#2_Table#1_Row#3 | 「BLKpoint_3」 | 「368.15」 | 「0.0」 | 「6.1」 |
| WM_L1#2_Table#1_Row#4 | 「BLKpoint_4」 | 「372.15」 | 「0.0」 | 「6.2」 |

The trend is monotonically increasing and near-linear (R² = 0.9973), consistent with the expected positive temperature dependence of γ∞ for ethanol in water.

##### Complete Block-by-Block Summary (All Inspected)

**WM_L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *Source (GLOBlit)* | *DOI* | *Block* | *Method* | *T range (K)* | *γ∞ range* | *Points* | *Trend* |
|---|---|---|---|---|---|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「GLOBlit_299」 | 「10.1016/j.fluid.2005.08.018」 | 「PROPblock_4」 | 「Headspace analysis」 | 「273.35–283.15」 | 「2.54–3.13」 | 「2」 | 「↑」 |
| WM_L1#2_Table#2_Row#2 | 「GLOBlit_299」 | 「10.1016/j.fluid.2005.08.018」 | 「PROPblock_5」 | 「Comparative tensimetry」 | 「303.15–333.15」 | 「4.14–5.3」 | 「7」 | 「↑」 |
| WM_L1#2_Table#2_Row#3 | 「GLOBlit_299」 | 「10.1016/j.fluid.2005.08.018」 | 「PROPblock_6」 | 「Circulating still」 | 「358.15–372.15」 | 「5.9–6.2」 | 「4」 | 「↑」 |
| WM_L1#2_Table#2_Row#4 | 「GLOBlit_8381」 | 「10.1021/je0495942」 | 「PROPblock_1」 | 「Chromatography」 | 「298.15」 | 「3.77」 | 「1」 | 「—」 |
| WM_L1#2_Table#2_Row#5 | 「GLOBlit_8511」 | 「10.1021/je049875+」 | 「PROPblock_1」 | 「Chromatography (dilutor)」 | 「303.25–343.25」 | 「5.03–5.96」 | 「5」 | 「↑」 |
| WM_L1#2_Table#2_Row#6 | 「GLOBlit_1971」 | 「10.1016/j.fluid.2016.08.030」 | 「PROPblock_1」 | 「Solid-phase micro-extraction」 | 「323.15–353.15」 | 「4.11–5.17」 | 「4」 | 「**↓ (anomalous)**」 |

##### Key Findings

1. **Verified maximum temperature for activity coefficient data: 372.15 K** (GLOBlit_299, PROPblock_6, circulating still method, γ∞ = 6.2).

2. **Consistent temperature dependence across 5 of 6 blocks:** γ∞ increases monotonically with temperature. The three GLOBlit_299 blocks together provide nearly continuous coverage using three complementary methods: from 273.35 K with γ∞ = 2.54 (PROPblock_4, headspace analysis) through 303.15–333.15 K with γ∞ = 4.14–5.3 (PROPblock_5, comparative tensimetry) to 358.15–372.15 K with γ∞ = 5.9–6.2 (PROPblock_6, circulating still).

3. **Data quality concern confirmed for GLOBlit_1971 (PROPblock_1):** The SPME-method data shows γ∞ *decreasing* from 5.17 at 323.15 K to 4.11 at 353.15 K, which is the opposite of every other source. For comparison at overlapping temperatures: at ~323 K, GLOBlit_1971 PROPblock_1 reports γ∞ = 5.17, while GLOBlit_8511 PROPblock_1 reports 5.54 at 323.25 K and GLOBlit_299 PROPblock_5 reports 5.03 at 323.15 K. The decreasing trend in GLOBlit_1971 is physically suspect and this dataset should be critically evaluated before inclusion in a correlation.

4. **For correlation building:** The verified activity coefficient temperature window spans from 273.35 K (GLOBlit_299, PROPblock_4) to 372.15 K (GLOBlit_299, PROPblock_6). Excluding the anomalous GLOBlit_1971 data, 19 data points (computed: 2 + 7 + 4 + 1 + 5 from the five consistent blocks) from 3 sources with consistent trends are available.

**Core claims:**
- All six activity coefficient data blocks for ethanol + water in the ThermoML dataset measure the infinite-dilution activity coefficient of ethanol (mole fraction of ethanol constrained to 0.0), spanning a verified temperature range from 273.35 K to 372.15 K across 23 data points from 4 publications.
- The highest temperature at which activity coefficient data are available is 372.15 K (GLOBlit_299, PROPblock_6, circulating still method), where γ∞ of ethanol = 6.2.
- In 5 of the 6 data blocks, γ∞ of ethanol increases monotonically with temperature, consistent with the expected positive temperature dependence for ethanol in water.
- The GLOBlit_1971 (PROPblock_1, SPME method) data show γ∞ decreasing from 5.17 at 323.15 K to 4.11 at 353.15 K, which is opposite to all other sources and is flagged as physically suspect; this dataset should be critically evaluated before inclusion in any correlation.
- Excluding the anomalous GLOBlit_1971 data, 19 data points from 3 sources with mutually consistent trends are available for correlation across the 273.35–372.15 K range.
- Several specific block-to-value attributions in the answer carry MISATTRIBUTED_VALUE or AMBIGUOUS_VALUE flags, indicating that while the underlying data values were inspected and verified, some were cited under incorrect block labels; the numeric values themselves remain consistent with the inspected records.

**Core blocks found:**

**WM_L1#2_Blocks_(Query_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#3 | 「GLOBlit_299」 | 「PROPblock_4」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_3」 | 「Infinite-dilution activity coefficient of ethanol in water by headspace analysis, 273.35–283.15 K.」 |
| WM_L1#2_Table#4 | 「GLOBlit_299」 | 「PROPblock_5」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_3」 | 「Infinite-dilution activity coefficient of ethanol in water by comparative tensimetry, 303.15–333.15 K.」 |
| WM_L1#2_Table#5 | 「GLOBlit_299」 | 「PROPblock_6」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_3」 | 「Infinite-dilution activity coefficient of ethanol in water by circulating still, 358.15–372.15 K. Contains the verified maximum temperature of 372.15 K.」 |
| WM_L1#2_Table#6 | 「GLOBlit_8381」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_3」 | 「Infinite-dilution activity coefficient of ethanol in water by chromatography at 298.15 K.」 |
| WM_L1#2_Table#7 | 「GLOBlit_8511」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_3」 | 「Infinite-dilution activity coefficient of ethanol in water by dilutor chromatography, 303.25–343.25 K.」 |
| WM_L1#2_Table#8 | 「GLOBlit_1971」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_3」 | 「Infinite-dilution activity coefficient of ethanol in water by solid-phase micro-extraction, 323.15–353.15 K. Anomalous decreasing trend flagged.」 |

*Not stored here: 6 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(8) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **MISATTRIBUTED_VALUE** PROPblock_4: 372.15 does not belong to PROPblock_4; it matches only GLOBlit_299::PROPblock_6 (inspected this run)
- **UNGROUNDED_LITERAL** PROPblock_6: 23 (near '…) across 23 data points (computed: 2 + 7 + 4 + 1 +…') matches no inspected row/stat, database table, or other source of PROPblock_6
- **MISATTRIBUTED_VALUE** PROPblock_6: 273.35 does not belong to PROPblock_6; it matches only GLOBlit_299::PROPblock_4 (inspected this run)
- **MISATTRIBUTED_VALUE** PROPblock_6: 2.54 does not belong to PROPblock_6; it matches only GLOBlit_299::PROPblock_4 (inspected this run)
- **MISATTRIBUTED_VALUE** PROPblock_4: 303.15 does not belong to PROPblock_4; it matches only GLOBlit_299::PROPblock_5 (inspected this run)
- **AMBIGUOUS_VALUE** PROPblock_4: 333.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **MISATTRIBUTED_VALUE** PROPblock_4: 4.14 does not belong to PROPblock_4; it matches only GLOBlit_299::PROPblock_5 (inspected this run)
- **AMBIGUOUS_VALUE** PROPblock_4: 5.3 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean


