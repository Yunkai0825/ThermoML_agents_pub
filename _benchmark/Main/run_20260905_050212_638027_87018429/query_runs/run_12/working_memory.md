# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_1 | water | water |
| comp | GLOBcomp_5 | propan-1-ol | propan-1-ol |
| prop | GLOBprop_1 | mass_density_kg_m3 | Mass density, kg/m3 |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find all mass density data for binary mixture of water and 1-propanol near 298.15 K → stored as L1_query_1 · validation: FLAGGED(1)
- [L1] Inspect GLOBlit_590::PROPblock_5 for data points at 298.15 K and list additional blocks from the 17 found for water+1-pr → stored as L1_query_2 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: partial · validation: FLAGGED(1)

**Summary:** Mass density data for the binary liquid mixture of water (GLOBcomp_1) and 1-propanol (GLOBcomp_5) near 298.15 K were identified across 17 blocks in ThermoML. Two blocks were inspected in detail. GLOBlit_555::PROPblock_8 (DOI 10.1016/j.fluid.2007.07.066, P = 101.0 kPa, 15 total points spanning 283.15–303.15 K) reports densities at 298.15 K of 989.431, 983.475, and 978.117 kg/m³ at propan-1-ol mass fractions of 0.05, 0.10, and 0.15, respectively. GLOBlit_2979::PROPblock_9 (DOI 10.1016/j.jct.2008.07.005, P = 98.93 kPa, 96 total points spanning 283.15–308.15 K, mole fraction 0–0.2, overall density range 911.83–999.69 kg/m³) reports densities at 298.15 K of 997.04, 995.4, 993.76, 991.66, 991.14, 986.54, 982.56, and 975.49 kg/m³ at propan-1-ol mole fractions of 0, 0.002, 0.005, 0.009, 0.01, 0.02, 0.03, and 0.05, respectively. Density decreases monotonically with increasing 1-propanol content at 298.15 K, consistent with addition of a lighter alcohol to water. The two inspected blocks cover the water-rich region using different composition scales (mass fraction vs. mole fraction). A third block from GLOBlit_590::PROPblock_5 (DOI 10.1016/j.fluid.2008.01.004) was identified with mass fraction 0.05–0.15 and density range 975.791–992.405 kg/m³ at 283.15–303.15 K but was not inspected for individual data points.

**Answer:**

#### Mass Density Data for Water + 1-Propanol Binary Mixture near 298.15 K in ThermoML

**System:** Water (GLOBcomp_1) + 1-Propanol (GLOBcomp_5), binary, liquid phase  
**Property:** Mass density (GLOBprop_1, kg/m³)

##### Overview

The search_blocks discovery tool returned a total count of **17 blocks** (search-tool count, not individually verified) for this binary system with temperatures in the 293–303 K window. These blocks span various composition variables (mole fraction, mass fraction, molality) and pressure conditions (atmospheric to elevated pressures). The following block-level summary ranges are from the `search_blocks` discovery tool (not individually inspected):

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *#* | *DOI* | *Block* | *GLOBlit* | *Comp. Variable* | *T range (K)* | *P* | *ρ range (kg/m³)* | *Source* |
|---|---|---|---|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「1」 | 「10.1016/j.fluid.2007.07.066」 | 「PROPblock_8」 | 「GLOBlit_555」 | 「mass fraction w, 0.05–0.15」 | 「283.15–303.15」 | 「atm」 | 「976.004–992.444」 | 「search summary」 |
| WM_L1#1_Table#1_Row#2 | 「2」 | 「10.1016/j.fluid.2008.01.004」 | 「PROPblock_5」 | 「GLOBlit_590」 | 「mass fraction w, 0.05–0.15」 | 「283.15–303.15」 | 「atm」 | 「975.791–992.405」 | 「search summary」 |
| WM_L1#1_Table#1_Row#3 | 「3」 | 「10.1016/j.jct.2008.07.005」 | 「PROPblock_9」 | 「GLOBlit_2979」 | 「mole fraction x, 0–0.2」 | 「283.15–298.15」 | 「atm (98.93 kPa)」 | 「911.83–999.69」 | 「search summary + inspected」 |

Additional blocks (including high-pressure and elevated-temperature datasets) were returned but not shown here (derived count: 17 total minus 3 listed = remaining blocks not displayed). Only blocks 1 and 3 were inspected for verbatim data points below.

---

##### Inspected Data Points at T = 298.15 K

###### Block 1: GLOBlit_555 :: PROPblock_8 (DOI: 10.1016/j.fluid.2007.07.066)
Constraint: P = 101.0 kPa. Composition in mass fraction of propan-1-ol.

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *mass_fraction (propan-1-ol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0.05」 | 「989.431」 |
| WM_L1#1_Table#2_Row#2 | 「0.10」 | 「983.475」 |
| WM_L1#1_Table#2_Row#3 | 「0.15」 | 「978.117」 |

Full block spans 283.15–303.15 K with 15 total points (from inspection stats).

###### Block 2: GLOBlit_2979 :: PROPblock_9 (DOI: 10.1016/j.jct.2008.07.005)
Constraint: P = 98.93 kPa. Composition in mole fraction of propan-1-ol.

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *mole_fraction (propan-1-ol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0」 | 「997.04」 |
| WM_L1#1_Table#3_Row#2 | 「0.002」 | 「995.4」 |
| WM_L1#1_Table#3_Row#3 | 「0.005」 | 「993.76」 |
| WM_L1#1_Table#3_Row#4 | 「0.009」 | 「991.66」 |
| WM_L1#1_Table#3_Row#5 | 「0.01」 | 「991.14」 |
| WM_L1#1_Table#3_Row#6 | 「0.02」 | 「986.54」 |
| WM_L1#1_Table#3_Row#7 | 「0.03」 | 「982.56」 |
| WM_L1#1_Table#3_Row#8 | 「0.05」 | 「975.49」 |

Full block spans 283.15–308.15 K with 96 total points; mole fraction range 0–0.2; density range across all temperatures: 911.83–999.69 kg/m³ (from inspection stats).

---

##### Chemistry Insight

The inspected data show a clear monotonic decrease in density with increasing 1-propanol content at 298.15 K. At x(propan-1-ol) = 0, the density is 997.04 kg/m³ (essentially pure water), dropping to 975.49 kg/m³ at x = 0.05 (GLOBlit_2979::PROPblock_9). This is consistent with the addition of a lighter alcohol to water. The two inspected sources cover the water-rich region: PROPblock_8 uses mass fraction (0.05–0.15) while PROPblock_9 uses mole fraction (0–0.2), making direct numerical comparison between them require unit conversion (not performed here). The blocks returned by the search collectively provide extensive coverage of this binary system near ambient temperature.

**Core claims:**
- At 298.15 K and near-atmospheric pressure, the mass density of the water + 1-propanol binary mixture decreases monotonically with increasing 1-propanol content in the water-rich region, from 997.04 kg/m³ at x(propan-1-ol) = 0 to 975.49 kg/m³ at x = 0.05 (GLOBlit_2979::PROPblock_9, P = 98.93 kPa).
- Two independent ThermoML sources were inspected: GLOBlit_555::PROPblock_8 reports densities of 989.431, 983.475, and 978.117 kg/m³ at mass fractions 0.05, 0.10, and 0.15 of propan-1-ol (P = 101.0 kPa, T = 298.15 K), and GLOBlit_2979::PROPblock_9 reports densities at mole fractions 0–0.05 (P = 98.93 kPa, T = 298.15 K); direct numerical comparison between the two requires unit conversion that was not performed.
- The search returned a total of 17 blocks for this binary system near 298.15 K, but only two blocks (PROPblock_8 and PROPblock_9) were individually inspected, so coverage of the full composition and pressure range is incomplete in the verified data.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_555」 | 「PROPblock_8」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + 1-propanol binary mixture at 283.15–303.15 K, mass fraction 0.05–0.15, atmospheric pressure. Inspected data at 298.15 K: 978.117–989.431 kg/m³.」 |
| WM_L1#1_Table#5 | 「GLOBlit_590」 | 「PROPblock_5」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + 1-propanol binary mixture at 283.15–303.15 K, mass fraction 0.05–0.15, atmospheric pressure. Not individually inspected.」 |
| WM_L1#1_Table#6 | 「GLOBlit_2979」 | 「PROPblock_9」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + 1-propanol binary mixture at 283.15–298.15 K, mole fraction 0–0.2, P=98.93 kPa. Inspected data at 298.15 K: 975.49–997.04 kg/m³.」 |

*Not stored here: 2 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** PROPblock_9: 17 (near '…datasets) were returned but not shown here (derived count: 1…') matches no inspected row/stat, database table, or other source of PROPblock_9
### L1_query_2
**L1_query_2** — status: success · validation: PASS

**Summary:** For the binary liquid system water + 1-propanol at 298.15 K and 101.0 kPa, GLOBlit_590::PROPblock_5 (DOI 10.1016/j.fluid.2008.01.004) reports density as a function of mass fraction of propan-1-ol: 989.387 kg/m³ at 0.05, 983.372 kg/m³ at 0.10, and 977.921 kg/m³ at 0.15. The full block spans 15 data points over T = 283.15–303.15 K and ρ = 975.791–992.405 kg/m³. At least 13 additional ThermoML blocks from other DOIs (GLOBlit_555, GLOBlit_2432, GLOBlit_2979, GLOBlit_4068, GLOBlit_4415, GLOBlit_5585, GLOBlit_7085, GLOBlit_7178, GLOBlit_8254, GLOBlit_10159, GLOBlit_11142, among others) also contain water + 1-propanol density data near 298.15 K but were not inspected in this run, so no numerical values are reported for them.

**Answer:**

#### Inspection of GLOBlit_590::PROPblock_5 at 298.15 K

**Source:** DOI 10.1016/j.fluid.2008.01.004 (GLOBlit_590), PROPblock_5  
**System:** Water + 1-propanol, binary, liquid phase  
**Constraint:** P = 101.0 kPa  
**Composition variable:** Mass fraction of propan-1-ol (0.05–0.15)  
**Full block:** 15 data points, T = 283.15–303.15 K, ρ = 975.791–992.405 kg/m³

##### Data points at T = 298.15 K (verbatim from inspection):

**WM_L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *mass_fraction (propan-1-ol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0.05」 | 「989.387」 |
| WM_L1#2_Table#1_Row#2 | 「0.10」 | 「983.372」 |
| WM_L1#2_Table#1_Row#3 | 「0.15」 | 「977.921」 |

These three data points at 298.15 K show the expected monotonic decrease in density with increasing 1-propanol content.

---

#### Full Listing of Blocks for Water + 1-Propanol Density near 298.15 K

The search_system_registry returned blocks for this binary system in a temperature window around 298.15 K. The following table lists all blocks identified by DOI, GLOBlit, and block number. Numerical details are shown only for the block inspected in this run (GLOBlit_590::PROPblock_5, above).

**WM_L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *DOI* | *GLOBlit* | *Block* | *Status* |
|---|---|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「10.1016/j.fluid.2007.07.066」 | 「GLOBlit_555」 | 「PROPblock_8」 | 「Not inspected in this run」 |
| WM_L1#2_Table#2_Row#2 | 「10.1016/j.fluid.2008.01.004」 | 「GLOBlit_590」 | 「PROPblock_5」 | 「Inspected in this run (see above)」 |
| WM_L1#2_Table#2_Row#3 | 「10.1016/j.jct.2004.07.019」 | 「GLOBlit_2432」 | 「PROPblock_3」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#4 | 「10.1016/j.jct.2008.07.005」 | 「GLOBlit_2979」 | 「PROPblock_9」 | 「Not inspected in this run」 |
| WM_L1#2_Table#2_Row#5 | 「10.1016/j.jct.2013.11.036」 | 「GLOBlit_4068」 | 「PROPblock_1」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#6 | 「10.1016/j.jct.2013.11.036」 | 「GLOBlit_4068」 | 「PROPblock_2」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#7 | 「10.1016/j.jct.2015.06.024」 | 「GLOBlit_4415」 | 「PROPblock_5」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#8 | 「10.1016/j.jct.2019.105880」 | 「GLOBlit_5585」 | 「PROPblock_7」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#9 | 「10.1021/acs.jced.6b01058」 | 「GLOBlit_7085」 | 「PROPblock_8」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#10 | 「10.1021/acs.jced.7b00299」 | 「GLOBlit_7178」 | 「PROPblock_13」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#11 | 「10.1021/je034101z」 | 「GLOBlit_8254」 | 「PROPblock_6」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#12 | 「10.1021/je4003515」 | 「GLOBlit_10159」 | 「PROPblock_10」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#13 | 「10.1021/je800158z」 | 「GLOBlit_11142」 | 「PROPblock_3」 | 「Not inspected (registry entry truncated)」 |
| WM_L1#2_Table#2_Row#14 | 「(truncated in registry output)」 | 「—」 | 「—」 | 「Not available」 |

**Notes:**
- Composition variables, pressure conditions, point counts, and density ranges for uninspected blocks were not verified via inspection and are therefore not reported here.
- Only GLOBlit_590::PROPblock_5 was inspected in this run. GLOBlit_555::PROPblock_8 and GLOBlit_2979::PROPblock_9 were inspected in the prior session (see working memory for those data points) but were not re-inspected here.
- The row count shown in the listing table is derived from the registry tool output, not from block inspection. The registry listing was truncated after the entry shown for GLOBlit_11142.

**Core claims:**
- For the water + 1-propanol binary system at 298.15 K and 101.0 kPa (GLOBlit_590::PROPblock_5, DOI 10.1016/j.fluid.2008.01.004), the liquid density decreases monotonically with increasing 1-propanol mass fraction: 989.387 kg/m³ at 0.05, 983.372 kg/m³ at 0.10, and 977.921 kg/m³ at 0.15.
- At least 13 additional ThermoML data blocks from independent literature sources contain density data for the water + 1-propanol binary system near 298.15 K, but these blocks were not inspected in this run and their numerical values were not verified.

**Core blocks found:**

**WM_L1#2_Blocks_(Query_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#3 | 「GLOBlit_590」 | 「PROPblock_5」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol at P=101.0 kPa, T=283.15–303.15 K, mass fraction 0.05–0.15, ρ=975.791–992.405 kg/m³. Inspected: 3 points at 298.15 K.」 |
| WM_L1#2_Table#4 | 「GLOBlit_555」 | 「PROPblock_8」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected in this run.」 |
| WM_L1#2_Table#5 | 「GLOBlit_2979」 | 「PROPblock_9」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected in this run.」 |
| WM_L1#2_Table#6 | 「GLOBlit_2432」 | 「PROPblock_3」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#7 | 「GLOBlit_4068」 | 「PROPblock_1」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#8 | 「GLOBlit_4068」 | 「PROPblock_2」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#9 | 「GLOBlit_4415」 | 「PROPblock_5」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#10 | 「GLOBlit_5585」 | 「PROPblock_7」 | 「GLOBcomp_1, GLOBcomp_5」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#11 | 「GLOBlit_7085」 | 「PROPblock_8」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#12 | 「GLOBlit_7178」 | 「PROPblock_13」 | 「GLOBcomp_1, GLOBcomp_5」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#13 | 「GLOBlit_8254」 | 「PROPblock_6」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#14 | 「GLOBlit_10159」 | 「PROPblock_10」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#15 | 「GLOBlit_11142」 | 「PROPblock_3」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected; registry entry truncated.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


