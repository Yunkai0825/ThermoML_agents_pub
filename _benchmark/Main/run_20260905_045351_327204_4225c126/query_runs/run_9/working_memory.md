# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_2 | ethanol | ethanol |
| comp | GLOBcomp_1 | water | water |
| prop | GLOBprop_1 | mass_density_kg_m3 | Mass density, kg/m3 |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|
| lit | GLOBlit_2092 | 2017-ono-kyo-0 | 10.1016/j.fluid.2017.09.005 |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find density data for ethanol-water binary mixtures. Determine if data exists at 1000 K, and if not, identify the closes → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** The ThermoML database contains 29 data blocks with mass density measurements for the ethanol (C₂H₆O, CAS 64-17-5) + water (H₂O, CAS 7732-18-5) binary system, totaling approximately 2,924 raw data points spanning 268.1–618.2 K. There is no density data at or near 1000 K; this temperature far exceeds the normal boiling points and critical temperatures of both components (ethanol T_c ≈ 514 K; water T_c ≈ 647 K). The highest-temperature data, from DOI 10.1016/j.fluid.2017.09.005, covers 523.2–618.2 K at 20,000–40,000 kPa with 72 data points. At 618.2 K and 20,000 kPa, densities range from 619.7 kg/m³ (pure water) down to 250.4 kg/m³ (x(ethanol) = 0.3), reflecting near-critical compressibility of ethanol. At 618.2 K and 40,000 kPa, densities are substantially higher (e.g., 682.3 kg/m³ for pure water, 481.2 kg/m³ for pure ethanol). The maximum temperature in the database is 618.2 K, well below the queried 1000 K, and no data exists to bridge this gap.

**Answer:**

#### Density Data for Ethanol–Water Binary Mixtures

##### Compound and Property Identification
- **Ethanol**: GLOBcomp_2 (C₂H₆O, CAS 64-17-5)
- **Water**: GLOBcomp_1 (H₂O, CAS 7732-18-5)
- **Property**: Mass density (GLOBprop_1, kg/m³)

##### Data Availability Overview

The ThermoML database contains **29 data blocks** with mass density measurements for the ethanol + water binary system, totaling approximately **2,924 raw data points**.

**Temperature range covered: 268.1–618.2 K** (approximately −5 °C to 345 °C).

##### Is There Data at 1000 K?

**No.** There is no density data at or near 1000 K (≈727 °C) for the ethanol–water system in the ThermoML database. This is physically expected: 1000 K is far above the normal boiling points of both ethanol (351.5 K / 78.4 °C) and water (373.15 K / 100 °C), and also above the critical temperatures of both components (ethanol T_c ≈ 514 K; water T_c ≈ 647 K). At 1000 K and moderate pressures, both substances would be supercritical gases with very low density, and experimental measurements in this regime for this mixture are essentially absent from the literature.

##### Closest Available High-Temperature Data

The highest-temperature data block is from:

- **DOI**: 10.1016/j.fluid.2017.09.005 (GLOBlit_2092, PROPblock_3)
- **Temperature range**: 523.2–618.2 K
- **Pressure range**: 20,000–40,000 kPa (200–400 bar)
- **Composition range**: x(ethanol) = 0–1
- **Density range**: 250.4–834.3 kg/m³
- **72 data points**, liquid phase

These are high-pressure supercritical/compressed-liquid measurements — the elevated pressures keep the mixture in a dense fluid state even above the normal boiling points.

##### Representative Data Points (highest available temperatures)

**At 618.2 K (highest T in the database), 20,000 kPa:**

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0」 | 「619.7」 |
| WM_L1#1_Table#1_Row#2 | 「0.2」 | 「281.3」 |
| WM_L1#1_Table#1_Row#3 | 「0.3」 | 「250.4」 |
| WM_L1#1_Table#1_Row#4 | 「1.0」 | 「314.6」 |

**At 618.2 K, 30,000 kPa:**

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0」 | 「656.9」 |
| WM_L1#1_Table#2_Row#2 | 「0.2」 | 「501.5」 |
| WM_L1#1_Table#2_Row#3 | 「0.4」 | 「437.4」 |
| WM_L1#1_Table#2_Row#4 | 「0.6」 | 「420.1」 |
| WM_L1#1_Table#2_Row#5 | 「1.0」 | 「423.8」 |

**At 618.2 K, 40,000 kPa:**

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0」 | 「682.3」 |
| WM_L1#1_Table#3_Row#2 | 「0.2」 | 「561.0」 |
| WM_L1#1_Table#3_Row#3 | 「0.4」 | 「509.1」 |
| WM_L1#1_Table#3_Row#4 | 「1.0」 | 「481.2」 |

##### Chemistry Insight

At 618.2 K and 20,000 kPa, the density drops sharply from pure water (619.7 kg/m³) to intermediate ethanol mole fractions (as low as 250.4 kg/m³ at x = 0.3), reflecting the proximity to ethanol's critical point where the fluid becomes highly compressible. Increasing pressure to 40,000 kPa substantially raises the density across all compositions (e.g., pure water reaches 682.3 kg/m³), demonstrating the strong pressure dependence in this near-critical regime.

The maximum available temperature in the database is 618.2 K — well below the queried 1000 K. No data exists in the ThermoML database to bridge this gap for the ethanol–water system.

**Core claims:**
- The ThermoML database contains no density data at or near 1000 K for the ethanol–water binary system; the maximum temperature covered is 618.2 K.
- The absence of data at 1000 K is physically expected because 1000 K far exceeds the critical temperatures of both ethanol (T_c ≈ 514 K) and water (T_c ≈ 647 K), where both substances would be supercritical gases at moderate pressures.
- The database contains approximately 2,924 raw mass density data points for ethanol–water across 29 data blocks, spanning a temperature range of 268.1–618.2 K.
- The highest-temperature data (618.2 K) come from DOI 10.1016/j.fluid.2017.09.005 at pressures of 20,000–40,000 kPa, with densities ranging from 250.4 to 834.3 kg/m³ depending on composition and pressure.
- At 618.2 K and 20,000 kPa, density drops sharply from pure water (619.7 kg/m³) to as low as 250.4 kg/m³ at x(ethanol) = 0.3, reflecting proximity to ethanol's critical point and high compressibility in this regime.
- Increasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises density across all compositions, demonstrating strong pressure dependence in the near-critical regime.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_2092」 | 「PROPblock_3」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for ethanol + water binary system at 523.2–618.2 K and 20,000–40,000 kPa, 72 data points, liquid phase. DOI: 10.1016/j.fluid.2017.09.005」 |

*Not stored here: 1 verbatim data_inspections table(s); 4 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


