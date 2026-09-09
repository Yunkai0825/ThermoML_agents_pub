# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find experimental mass density data for ethanol+water binary mixture at 298.15 K and x_ethanol near 0.5 → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Experimental mass density data for the ethanol + water binary mixture at 298.15 K and ethanol mole fraction near 0.5 were found in the ThermoML database from DOI 10.1016/j.fluid.2004.11.019 (GLOBlit_220, PROPblock_2). The closest composition to x_ethanol = 0.5 is x_ethanol = 0.498. At T = 298.15 K and x_ethanol = 0.498, the mass density values are: 859.3 kg/m³ at 100 kPa, 865.4 kg/m³ at 10000 kPa, 871.3 kg/m³ at 20000 kPa, 876.8 kg/m³ at 30000 kPa, and 882.0 kg/m³ at 40000 kPa. At atmospheric pressure (100 kPa), the mass density is 859.3 kg/m³. The density increases systematically with pressure under isothermal compression, and the value is consistent with the known negative excess volume of ethanol–water mixtures. No uncertainty values were reported for these data points.

**Answer:**

Experimental mass density data for the ethanol + water binary mixture at 298.15 K and mole fraction of ethanol near 0.5 were found in the ThermoML database.

**Source:** DOI 10.1016/j.fluid.2004.11.019 (GLOBlit_220, PROPblock_2)

The block contains 810 data points covering T = 298.15–348.15 K, pressures from 100 to 40000 kPa, and ethanol mole fractions from 0.003 to 1. The closest composition to x_ethanol = 0.5 in this dataset is **x_ethanol = 0.498** (no data point exists at exactly 0.5; the nearest above is 0.5501).

At **T = 298.15 K and x_ethanol = 0.498**, the mass density varies with pressure as follows:

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Pressure (kPa)* | *Mass Density (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「100」 | 「859.3」 |
| WM_L1#1_Table#1_Row#2 | 「10000」 | 「865.4」 |
| WM_L1#1_Table#1_Row#3 | 「20000」 | 「871.3」 |
| WM_L1#1_Table#1_Row#4 | 「30000」 | 「876.8」 |
| WM_L1#1_Table#1_Row#5 | 「40000」 | 「882.0」 |

At atmospheric pressure (100 kPa), the mass density of the near-equimolar ethanol–water mixture is **859.3 kg/m³** at 298.15 K. This value lies between the densities of pure water and pure ethanol at the same temperature, consistent with the known negative excess volume (volume contraction) of ethanol–water mixtures. The density increases systematically with pressure, as expected for a liquid mixture under isothermal compression.

No uncertainty values were reported for these data points in the inspected block.

**Core claims:**
- Experimental mass density data for the ethanol + water binary mixture at 298.15 K and x_ethanol = 0.498 were found in the ThermoML database (DOI 10.1016/j.fluid.2004.11.019), with the mass density at atmospheric pressure (100 kPa) reported as 859.3 kg/m³.
- At T = 298.15 K and x_ethanol = 0.498, the mass density increases systematically with pressure: 859.3 kg/m³ at 100 kPa, 865.4 kg/m³ at 10000 kPa, 871.3 kg/m³ at 20000 kPa, 876.8 kg/m³ at 30000 kPa, and 882.0 kg/m³ at 40000 kPa.
- No data point exists at exactly x_ethanol = 0.5; the closest composition in the dataset is x_ethanol = 0.498, with the nearest above being 0.5501.
- No uncertainty values were reported for these data points in the inspected block.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_220」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for ethanol + water binary mixture at 298.15–348.15 K, 100–40000 kPa, and ethanol mole fractions from 0.003 to 1.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


