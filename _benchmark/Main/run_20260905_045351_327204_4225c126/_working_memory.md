# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_045351_327204_4225c126`

### History
- [query:Q1] "Find density data for ethanol-water binary mixtures at 1000 K. If no data exists" (180s, 2 iters, validation=PASS verdict=## Verdict
The answer correctl)

### Query Agent Results

#### Q1
**Q1** — confidence: high · validation: PASS

**Answer:**

#### Density Data for Ethanol–Water Binary Mixtures at 1000 K

##### Data at 1000 K: Not Available

There is **no density data at or near 1000 K** (≈727 °C) for the ethanol–water system in the ThermoML database. This is physically expected:

- **Ethanol** (C₂H₆O, CAS 64-17-5) has a normal boiling point of ~351.5 K (78.4 °C) and a critical temperature T_c ≈ 514 K.
- **Water** (H₂O, CAS 7732-18-5) has a normal boiling point of ~373.15 K (100 °C) and a critical temperature T_c ≈ 647 K.

At 1000 K and moderate pressures, both substances would be supercritical gases with very low density, making experimental liquid-phase density measurements essentially impossible for this mixture.

---

##### Closest Available Temperature Range

The ThermoML database contains **29 data blocks** with mass density measurements for the ethanol + water binary system, totaling approximately **2,924 raw data points** spanning **268.1–618.2 K** (approximately −5 °C to 345 °C).

The **highest-temperature data** comes from:

- **Source:** DOI 10.1016/j.fluid.2017.09.005 (GLOBlit_2092)
- **Block:** PROPblock_3
- **Temperature range:** 523.2–618.2 K (250–345 °C)
- **Pressure range:** 20,000–40,000 kPa (200–400 bar)
- **Composition range:** x(ethanol) = 0–1
- **Overall density range:** 250.4–834.3 kg/m³
- **72 data points**, liquid phase, measured by vibrating tube method

These are high-pressure supercritical/compressed-liquid measurements — the elevated pressures keep the mixture in a dense fluid state even above the normal boiling points.

---

##### Representative Data at the Highest Available Temperature (618.2 K)

**At 618.2 K, 20,000 kPa:**

**WM_Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「0」 | 「619.7」 |
| WM_Q#1_Table#1_Row#2 | 「0.2」 | 「281.3」 |
| WM_Q#1_Table#1_Row#3 | 「0.3」 | 「250.4」 |
| WM_Q#1_Table#1_Row#4 | 「1.0」 | 「314.6」 |

**At 618.2 K, 30,000 kPa:**

**WM_Q#1_Table#2_(Main_Q#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_Q#1_Table#2_Row#1 | 「0」 | 「656.9」 |
| WM_Q#1_Table#2_Row#2 | 「0.2」 | 「501.5」 |
| WM_Q#1_Table#2_Row#3 | 「0.4」 | 「437.4」 |
| WM_Q#1_Table#2_Row#4 | 「0.6」 | 「420.1」 |
| WM_Q#1_Table#2_Row#5 | 「1.0」 | 「423.8」 |

**At 618.2 K, 40,000 kPa:**

**WM_Q#1_Table#3_(Main_Q#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_Q#1_Table#3_Row#1 | 「0」 | 「682.3」 |
| WM_Q#1_Table#3_Row#2 | 「0.2」 | 「561.0」 |
| WM_Q#1_Table#3_Row#3 | 「0.4」 | 「509.1」 |
| WM_Q#1_Table#3_Row#4 | 「1.0」 | 「481.2」 |

---

##### Chemistry Insight

At 618.2 K and 20,000 kPa, the density drops sharply from pure water (619.7 kg/m³) to intermediate ethanol mole fractions — reaching as low as 250.4 kg/m³ at x(ethanol) = 0.3. This dramatic non-monotonic behavior reflects the proximity to ethanol's critical point (T_c ≈ 514 K), where the fluid becomes highly compressible and density is extremely sensitive to composition. Notably, pure ethanol at this condition (314.6 kg/m³) is actually denser than the x = 0.3 mixture, illustrating the complex interplay of near-critical fluctuations in the mixture.

Increasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises the density across all compositions (e.g., pure water: 619.7 → 682.3 kg/m³; pure ethanol: 314.6 → 481.2 kg/m³), demonstrating the strong pressure dependence characteristic of near-critical and supercritical fluids.

**The maximum available temperature in the ThermoML database for ethanol–water density is 618.2 K — approximately 382 K below the queried 1000 K, with no data to bridge this gap.**

**Core claims:**
- No density data at or near 1000 K for the ethanol–water binary system exists in the ThermoML database; at 1000 K and moderate pressures both substances would be supercritical gases, making liquid-phase density measurements essentially impossible.
- The highest-temperature density data available for ethanol + water in ThermoML spans 523.2–618.2 K at 20,000–40,000 kPa, from DOI 10.1016/j.fluid.2017.09.005, comprising 72 data points with an overall density range of 250.4–834.3 kg/m³.
- At 618.2 K and 20,000 kPa, density exhibits strongly non-monotonic composition dependence: pure water is 619.7 kg/m³, the mixture at x(ethanol) = 0.3 drops to 250.4 kg/m³, while pure ethanol is 314.6 kg/m³, reflecting near-critical compressibility effects near ethanol's critical temperature (T_c ≈ 514 K).
- Increasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises density across all compositions (e.g., pure water: 619.7 → 682.3 kg/m³; pure ethanol: 314.6 → 481.2 kg/m³), demonstrating strong pressure dependence characteristic of near-critical and supercritical fluids.
- The maximum available temperature in the ThermoML database for ethanol–water density is 618.2 K, approximately 382 K below the queried 1000 K, with no data to bridge this gap.

**Sources:**

**WM_Q#1_Table#4_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#4_Row#1 | 「GLOBlit_2092」 | 「PROPblock_3」 | 「10.1016/j.fluid.2017.09.005」 | 「—」 | 「This block provides the highest-temperature mass density data for the ethanol–water binary system in ThermoML, covering 523.2–618.2 K at 20,000–40,000 kPa with 72 data points. The answer correctly uses it to demonstrate that no data exists at 1000 K and to present representative density values at the closest available temperatures (e.g., 250.4–834.3 kg/m³ range).」 |

*Not stored here: 1 verbatim data_inspections table(s); 4 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

