# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_4 | methanol | methanol |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find mass density (GLOBprop_1) data for ethanol + water binary mixtures. Report the number of data blocks, temperature r → stored as L1_query_1 · validation: PASS
- [L1] Find mass density (GLOBprop_1) data for methanol + water binary mixtures. Report the number of data blocks, DOIs, total  → stored as L1_query_2 · validation: FLAGGED(8)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** The ThermoML database contains 29 data blocks across 22 DOIs reporting mass density (kg/m³) for the ethanol + water binary system, totaling approximately 2,920 data points. Coverage spans temperatures of 268.1–618.2 K, pressures from 100 kPa to 40,000 kPa, and the full ethanol mole fraction range (0–1). One of the largest blocks (DOI 10.1016/j.fluid.2004.11.019, 810 data points, 298.15–348.15 K, 100–40,000 kPa) provides representative values at T = 298.15 K and P = 100 kPa: density decreases monotonically from 995.3 kg/m³ at x(ethanol) = 0.003 to 785.7 kg/m³ at x(ethanol) = 1.0. The decrease is steepest in the water-rich region (x < 0.1), reflecting non-linear excess volume effects from disruption of water's hydrogen-bonding network by small amounts of ethanol. The dataset offers dense composition coverage (54 points at atmospheric pressure and 298.15 K in a single block) and is well-suited for liquid density model validation.

**Answer:**

#### Ethanol + Water Binary Mixture: Mass Density Data Summary

##### Overview

The ThermoML database contains **29 data blocks across 22 DOIs** (block count from the search_blocks result) reporting mass density (kg/m³) for the ethanol + water binary system.

##### Coverage

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Parameter* | *Range* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「**Temperature**」 | 「268.1 – 618.2 K」 |
| WM_L1#1_Table#1_Row#2 | 「**Pressure**」 | 「Ambient (100 kPa) to 40,000 kPa (40 MPa)」 |
| WM_L1#1_Table#1_Row#3 | 「**Ethanol mole fraction**」 | 「0 – 1 (full composition range)」 |
| WM_L1#1_Table#1_Row#4 | 「**Total data points**」 | 「~2,920」 |

##### Representative Data Block

One of the largest blocks is from DOI 10.1016/j.fluid.2004.11.019 (GLOBlit_220, PROPblock_2), containing **810 data points** covering 298.15–348.15 K and pressures from 100–40,000 kPa.

Below are representative density values at **T = 298.15 K, P = 100 kPa** across the full ethanol mole fraction range (the inspection tool returned a shape-preserving RDP selection of the 54 matched rows):

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *Density (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0.003」 | 「995.3」 |
| WM_L1#1_Table#2_Row#2 | 「0.0184」 | 「988.4」 |
| WM_L1#1_Table#2_Row#3 | 「0.0279」 | 「984.7」 |
| WM_L1#1_Table#2_Row#4 | 「0.0483」 | 「977.5」 |
| WM_L1#1_Table#2_Row#5 | 「0.0801」 | 「968.6」 |
| WM_L1#1_Table#2_Row#6 | 「0.1296」 | 「954.9」 |
| WM_L1#1_Table#2_Row#7 | 「0.2502」 | 「918.5」 |
| WM_L1#1_Table#2_Row#8 | 「0.3009」 | 「904.5」 |
| WM_L1#1_Table#2_Row#9 | 「0.35」 | 「891.9」 |
| WM_L1#1_Table#2_Row#10 | 「0.4501」 | 「868.8」 |
| WM_L1#1_Table#2_Row#11 | 「0.498」 | 「859.3」 |
| WM_L1#1_Table#2_Row#12 | 「0.5501」 | 「849.5」 |
| WM_L1#1_Table#2_Row#13 | 「0.6489」 | 「832.7」 |
| WM_L1#1_Table#2_Row#14 | 「0.6967」 | 「825.2」 |
| WM_L1#1_Table#2_Row#15 | 「0.8484」 | 「804.4」 |
| WM_L1#1_Table#2_Row#16 | 「1.0」 | 「785.7」 |

##### Chemistry Insight

The density decreases monotonically from ~995 kg/m³ (nearly pure water) to ~786 kg/m³ (pure ethanol) at 298.15 K and atmospheric pressure (values from the inspected rows above). The decrease is steepest in the water-rich region (x < 0.1), reflecting the strong disruption of water's hydrogen-bonding network by even small amounts of ethanol. This non-linear composition dependence — with excess volume effects most pronounced in the dilute-ethanol region — is a well-known feature of the ethanol–water system and is important for liquid density model validation.

The dataset is well-suited for model validation near room temperature, with dense composition coverage at 298.15 K (54 points at atmospheric pressure alone in this single block) and additional high-pressure and elevated-temperature data across the many other blocks identified by the search.

**Core claims:**
- The ThermoML database contains 29 data blocks across 22 DOIs reporting mass density (kg/m³) for the ethanol + water binary system, covering approximately 2,920 total data points.
- The data span temperatures of 268.1–618.2 K, pressures from ambient (100 kPa) to 40,000 kPa (40 MPa), and the full ethanol mole fraction range (0–1).
- At 298.15 K and 100 kPa, the density decreases monotonically from ~995 kg/m³ (nearly pure water) to ~786 kg/m³ (pure ethanol), with the steepest decrease in the water-rich region (x < 0.1).
- The non-linear composition dependence of density, with excess volume effects most pronounced in the dilute-ethanol region, reflects the strong disruption of water's hydrogen-bonding network by small amounts of ethanol.
- One of the largest blocks (DOI 10.1016/j.fluid.2004.11.019) contains 810 data points covering 298.15–348.15 K and pressures from 100–40,000 kPa, with 54 points at 298.15 K and atmospheric pressure alone.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_220」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density data for ethanol + water binary mixture, 810 data points, 298.15–348.15 K, 100–40000 kPa, full ethanol mole fraction range.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: success · validation: FLAGGED(8)

**Summary:** The ThermoML database contains approximately 18 data blocks across 15 DOIs reporting mass density (kg/m³) for the methanol + water binary system, totaling roughly 1,610 data points (these aggregate counts are from a search-level summary, not individually verified). Two blocks were inspected in detail. GLOBlit_8254::PROPblock_4 (DOI: 10.1021/je034101z) contains 401 data points of absolute density at elevated pressures, covering T = 287.15–417.15 K, P = 3,721–29,927 kPa, x(MeOH) = 0.059–0.708, and ρ = 762.2–966 kg/m³. GLOBlit_2825::PROPblock_10 (DOI: 10.1016/j.jct.2007.05.004) contains 39 data points at atmospheric pressure (101 kPa), T = 293.15–303.15 K, spanning the full composition range. At T = 298.15 K and P = 101 kPa, representative densities from GLOBlit_2825::PROPblock_10 range from 787.2 kg/m³ (pure methanol, x(water) = 0) through 881.69 kg/m³ (x(water) = 0.5003) to 997.05 kg/m³ (pure water, x(water) = 1). Specific reported values include x(water) = 0.049 → 795.47, 0.0993 → 804.11, 0.1973 → 821.73, 0.2983 → 840.79, 0.3985 → 860.59, 0.5994 → 902.96, 0.7986 → 947.17, 0.8999 → 969.84, and 0.9512 → 982.53 kg/m³. The dataset is smaller than the ethanol + water density dataset but provides good coverage for liquid density model validation, particularly at atmospheric pressure and near-ambient temperatures.

**Answer:**

###### Methanol + Water Binary Mixture: Mass Density Data Summary

####### Overview

The ThermoML database contains **18 data blocks across 15 DOIs** reporting mass density (kg/m³) for the methanol + water binary system, totaling approximately **1,610 data points**. (These aggregate counts — 18, 15, and 1,610 — are from the search_system_registry summary, not from individual block inspections.)

####### Coverage

**WM_L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *Parameter* | *Range* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「**Temperature**」 | 「Not fully inspected in this run; the search_blocks summary reported 273.15–618.2 K (search-level aggregate, not block-inspected)」 |
| WM_L1#2_Table#1_Row#2 | 「**Pressure**」 | 「Ranges from atmospheric (101 kPa, confirmed in GLOBlit_2825::PROPblock_10) to high pressure (up to 29,927 kPa confirmed in GLOBlit_8254::PROPblock_4); search-level summary reported up to 40,000 kPa (not block-inspected)」 |
| WM_L1#2_Table#1_Row#3 | 「**Methanol mole fraction**」 | 「0 – 1 (full composition range, confirmed in GLOBlit_2825::PROPblock_10)」 |

####### Inspected Blocks

**GLOBlit_8254::PROPblock_4** (DOI: 10.1021/je034101z) — 401 data points; absolute density at elevated pressures. Inspected stats: T = 287.15–417.15 K; P = 3,721–29,927 kPa; x(MeOH) = 0.059–0.708; ρ = 762.2–966 kg/m³.

**GLOBlit_2825::PROPblock_10** (DOI: 10.1016/j.jct.2007.05.004) — 39 data points at atmospheric pressure (101 kPa); T = 293.15–303.15 K; full composition range. This is the most suitable block for room-temperature, atmospheric-pressure density data.

####### Representative Density Data at T = 298.15 K, P = 101 kPa

From GLOBlit_2825::PROPblock_10, 13 data points at T = 298.15 K (the block variable is mole fraction of water; x(methanol) = 1 − x(water) is a derived quantity):

**WM_L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *x(water)* | *Density (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「0」 | 「787.2」 |
| WM_L1#2_Table#2_Row#2 | 「0.049」 | 「795.47」 |
| WM_L1#2_Table#2_Row#3 | 「0.0993」 | 「804.11」 |
| WM_L1#2_Table#2_Row#4 | 「0.1973」 | 「821.73」 |
| WM_L1#2_Table#2_Row#5 | 「0.2983」 | 「840.79」 |
| WM_L1#2_Table#2_Row#6 | 「0.3985」 | 「860.59」 |
| WM_L1#2_Table#2_Row#7 | 「0.5003」 | 「881.69」 |
| WM_L1#2_Table#2_Row#8 | 「0.5994」 | 「902.96」 |
| WM_L1#2_Table#2_Row#9 | 「0.7986」 | 「947.17」 |
| WM_L1#2_Table#2_Row#10 | 「0.8999」 | 「969.84」 |
| WM_L1#2_Table#2_Row#11 | 「0.9512」 | 「982.53」 |
| WM_L1#2_Table#2_Row#12 | 「1」 | 「997.05」 |

*12 of 13 matched rows shown (shape-preserving RDP subset of the block's 39 total points).*

####### Chemistry Insight — Comparison with Ethanol + Water

At 298.15 K and atmospheric pressure, the density of the methanol + water system spans from 997.05 kg/m³ (pure water) down to 787.2 kg/m³ (pure methanol). At the equimolar point (x(water) = 0.5003), the density is 881.69 kg/m³.

From the prior context (provided by the user, not inspected in this run), the ethanol + water system was reported to have 29 blocks, ~2,920 points across 22 DOIs, with broader temperature (268.1–618.2 K) and pressure (100–40,000 kPa) coverage. Those ethanol + water statistics are from the prior user-supplied context and were not verified against the database in this run.

The methanol + water dataset (18 blocks, ~1,610 points from the search summary) is smaller but still provides good coverage for liquid density model validation, particularly at atmospheric pressure and near-ambient temperatures.

**Core claims:**
- The ThermoML database contains mass density data for the methanol + water binary system; two inspected blocks (GLOBlit_8254::PROPblock_4 and GLOBlit_2825::PROPblock_10) provide verified coverage at elevated pressures (3,721–29,927 kPa, T = 287.15–417.15 K, x(MeOH) = 0.059–0.708) and at atmospheric pressure (101 kPa, T = 293.15–303.15 K, full composition range), respectively.
- At T = 298.15 K and P = 101 kPa (GLOBlit_2825::PROPblock_10), the mass density of the methanol + water mixture increases monotonically with increasing water mole fraction, from 787.2 kg/m³ at x(water) = 0 (pure methanol) to 997.05 kg/m³ at x(water) = 1 (pure water), with an equimolar value of 881.69 kg/m³ at x(water) = 0.5003.
- Aggregate dataset statistics (18 blocks, ~1,610 points, 15 DOIs, and overall temperature and pressure ranges) are from a search-level summary and were not individually verified by block inspection; several specific values cited for ethanol + water comparison and for overall coverage ranges are flagged as UNVERIFIED.

**Core blocks found:**

**WM_L1#2_Blocks_(Query_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#3 | 「GLOBlit_8254」 | 「PROPblock_4」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water at elevated pressures (3721–29927 kPa), T = 287.15–417.15 K, x(MeOH) = 0.059–0.708; 401 data points.」 |
| WM_L1#2_Table#4 | 「GLOBlit_2825」 | 「PROPblock_10」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water at atmospheric pressure (101 kPa), T = 293.15–303.15 K, full composition range; 39 data points.」 |

*Not stored here: 3 verbatim data_inspections table(s); 1 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(8) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10 + GLOBlit_8254::PROPblock_4: 273.15 (near '…y inspected in this run; the search_blocks summary reported …') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10 + GLOBlit_8254::PROPblock_4
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10 + GLOBlit_8254::PROPblock_4: 618.2 (near '…cted in this run; the search_blocks summary reported 273.15–…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10 + GLOBlit_8254::PROPblock_4
- **MISATTRIBUTED_VALUE** GLOBlit_2825::PROPblock_10: 29 does not belong to GLOBlit_2825::PROPblock_10; it matches only GLOBlit_8254::PROPblock_4 (inspected this run)
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10: 2920 (near '…the ethanol + water system was reported to have 29 blocks, ~…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10
- **MISATTRIBUTED_VALUE** GLOBlit_2825::PROPblock_10: 22 does not belong to GLOBlit_2825::PROPblock_10; it matches only GLOBlit_8254::PROPblock_4 (inspected this run)
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10: 268.1 (near '…ks, ~2,920 points across 22 DOIs, with broader temperature (…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10: 618.2 (near '…,920 points across 22 DOIs, with broader temperature (268.1–…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10: 40000 (near '…with broader temperature (268.1–618.2 K) and pressure (100–4…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10


