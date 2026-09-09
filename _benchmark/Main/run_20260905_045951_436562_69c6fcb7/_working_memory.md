# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_045951_436562_69c6fcb7`

### History
- [query:Q1] "Find experimental data for binary mixtures of ethanol and water near room temper" (893s, 5 iters, validation=PASS verdict=## Verdict
The answer is compr)

### Query Agent Results

#### Q1
**Q1** — confidence: high · validation: PASS

**Answer:**

### Ethanol + Water Binary Mixture: Thermodynamic Data near 298 K from the ThermoML Database

#### Overview

The ThermoML database contains extensive experimental data for the ethanol + water binary system in the 293–303 K temperature window: **10 distinct property types** across **39 data blocks** from **26 publications**, totaling **3,263 matching data points**.

---

#### 1. Excess Molar Enthalpy (H^E)

Three verified data blocks provide excess molar enthalpy measurements at 298.15 K.

##### Source 1: DOI 10.1016/j.fluid.2007.06.007 (GLOBlit_528)

Two complementary dilute-solution blocks measured by Calvet calorimetry at 298.15 K and 101.0 kPa.

**Block PROPblock_1 — Dilute ethanol in water** (15 data points)

**WM_Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *x(ethanol)* | *T (K)* | *P (kPa)* | *H^E (kJ/mol)* |
|---|---|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「0.000102」 | 「298.15」 | 「101.0」 | 「−0.00104」 |
| WM_Q#1_Table#1_Row#2 | 「0.000206」 | 「298.15」 | 「101.0」 | 「−0.00208」 |
| WM_Q#1_Table#1_Row#3 | 「0.000308」 | 「298.15」 | 「101.0」 | 「−0.00312」 |
| WM_Q#1_Table#1_Row#4 | 「0.000516」 | 「298.15」 | 「101.0」 | 「−0.00518」 |
| WM_Q#1_Table#1_Row#5 | 「0.000619」 | 「298.15」 | 「101.0」 | 「−0.00621」 |
| WM_Q#1_Table#1_Row#6 | 「0.000723」 | 「298.15」 | 「101.0」 | 「−0.00722」 |
| WM_Q#1_Table#1_Row#7 | 「0.000827」 | 「298.15」 | 「101.0」 | 「−0.00826」 |
| WM_Q#1_Table#1_Row#8 | 「0.000931」 | 「298.15」 | 「101.0」 | 「−0.00927」 |
| WM_Q#1_Table#1_Row#9 | 「0.001034」 | 「298.15」 | 「101.0」 | 「−0.0103」 |
| WM_Q#1_Table#1_Row#10 | 「0.001241」 | 「298.15」 | 「101.0」 | 「−0.01233」 |
| WM_Q#1_Table#1_Row#11 | 「0.001345」 | 「298.15」 | 「101.0」 | 「−0.01334」 |
| WM_Q#1_Table#1_Row#12 | 「0.001551」 | 「298.15」 | 「101.0」 | 「−0.01537」 |

- Composition range: x(ethanol) = 0.000102–0.001551
- H^E range: −0.01537 to −0.00104 kJ/mol

**Block PROPblock_2 — Dilute water in ethanol** (15 data points)

**WM_Q#1_Table#2_(Main_Q#1_Answer):**

| *row_id* | *x(water)* | *T (K)* | *P (kPa)* | *H^E (kJ/mol)* |
|---|---|---|---|---|
| WM_Q#1_Table#2_Row#1 | 「0.001021」 | 「298.15」 | 「101.0」 | 「−0.00212」 |
| WM_Q#1_Table#2_Row#2 | 「0.00205」 | 「298.15」 | 「101.0」 | 「−0.00424」 |
| WM_Q#1_Table#2_Row#3 | 「0.004102」 | 「298.15」 | 「101.0」 | 「−0.00835」 |
| WM_Q#1_Table#2_Row#4 | 「0.006155」 | 「298.15」 | 「101.0」 | 「−0.01238」 |
| WM_Q#1_Table#2_Row#5 | 「0.007179」 | 「298.15」 | 「101.0」 | 「−0.01437」 |
| WM_Q#1_Table#2_Row#6 | 「0.010239」 | 「298.15」 | 「101.0」 | 「−0.02023」 |
| WM_Q#1_Table#2_Row#7 | 「0.011252」 | 「298.15」 | 「101.0」 | 「−0.02213」 |
| WM_Q#1_Table#2_Row#8 | 「0.012264」 | 「298.15」 | 「101.0」 | 「−0.02405」 |
| WM_Q#1_Table#2_Row#9 | 「0.013276」 | 「298.15」 | 「101.0」 | 「−0.0259」 |
| WM_Q#1_Table#2_Row#10 | 「0.014283」 | 「298.15」 | 「101.0」 | 「−0.02777」 |
| WM_Q#1_Table#2_Row#11 | 「0.015286」 | 「298.15」 | 「101.0」 | 「−0.02961」 |

- Composition range: x(water) = 0.001021–0.015286
- H^E range: −0.02961 to −0.00212 kJ/mol

##### Source 2: DOI 10.1016/j.tca.2017.05.023 (GLOBlit_6377)

**Block PROPblock_1** — Flow calorimetry, single data point at moderate composition:

**WM_Q#1_Table#3_(Main_Q#1_Answer):**

| *row_id* | *x(ethanol)* | *T (K)* | *P (kPa)* | *H^E (kJ/mol)* |
|---|---|---|---|---|
| WM_Q#1_Table#3_Row#1 | 「0.102」 | 「298.15」 | 「100」 | 「−0.70659」 |

**Chemistry insight:** All H^E values are **negative**, confirming that mixing ethanol and water at 298.15 K is exothermic. In the dilute regime, |H^E| is on the order of 0.001–0.03 kJ/mol, but at x(ethanol) = 0.102 it already reaches −0.707 kJ/mol, consistent with the well-known strongly exothermic mixing behaviour where the H^E minimum occurs near x(ethanol) ≈ 0.2–0.3. The nearly linear H^E–composition relationship in the dilute regime reflects the partial molar excess enthalpy at infinite dilution.

---

#### 2. Excess Molar Volume (V^E)

**No data found in the ThermoML database.** Searches were conducted with and without temperature restrictions and across both declared binary studies and binary subsystems in multicomponent datasets — no V^E data blocks exist for ethanol + water at any temperature or composition. However, the extensive mass density data (17 blocks; see below) could in principle be used to compute V^E.

---

#### 3. Other Properties Available (293–303 K)

**WM_Q#1_Table#4_(Main_Q#1_Answer):**

| *row_id* | *Property* | *Unit* | *Number of Blocks* |
|---|---|---|---|
| WM_Q#1_Table#4_Row#1 | 「Mass density」 | 「kg/m³」 | 「17」 |
| WM_Q#1_Table#4_Row#2 | 「Dynamic viscosity」 | 「Pa·s」 | 「7」 |
| WM_Q#1_Table#4_Row#3 | 「Speed of sound」 | 「m/s」 | 「3」 |
| WM_Q#1_Table#4_Row#4 | 「Refractive index (Na D-line)」 | 「—」 | 「3」 |
| WM_Q#1_Table#4_Row#5 | 「Thermal conductivity」 | 「W/(m·K)」 | 「2」 |
| WM_Q#1_Table#4_Row#6 | 「Henry's Law constant (mole fraction)」 | 「kPa」 | 「2」 |
| WM_Q#1_Table#4_Row#7 | 「Excess molar enthalpy」 | 「kJ/mol」 | 「2」 |
| WM_Q#1_Table#4_Row#8 | 「Vapor or sublimation pressure」 | 「kPa」 | 「1」 |
| WM_Q#1_Table#4_Row#9 | 「Surface tension (liquid–gas)」 | 「N/m」 | 「1」 |
| WM_Q#1_Table#4_Row#10 | 「Activity coefficient」 | 「—」 | 「1」 |

##### Top 5 Sources by Number of Data Points (293–303 K)

**WM_Q#1_Table#5_(Main_Q#1_Answer):**

| *row_id* | *Literature ID* | *DOI* | *Property Types* | *Matching Points* |
|---|---|---|---|---|
| WM_Q#1_Table#5_Row#1 | 「GLOBlit_220」 | 「10.1016/j.fluid.2004.11.019」 | 「1」 | 「810」 |
| WM_Q#1_Table#5_Row#2 | 「GLOBlit_2432」 | 「10.1016/j.jct.2004.07.019」 | 「1」 | 「565」 |
| WM_Q#1_Table#5_Row#3 | 「GLOBlit_5201」 | 「10.1016/j.jct.2018.02.022」 | 「3」 | 「496」 |
| WM_Q#1_Table#5_Row#4 | 「GLOBlit_11136」 | 「10.1021/je800150h」 | 「2」 | 「216」 |
| WM_Q#1_Table#5_Row#5 | 「GLOBlit_9006」 | 「10.1021/je060335h」 | 「1」 | 「164」 |

##### Representative Data: Speed of Sound (GLOBlit_5201, PROPblock_20)

DOI 10.1016/j.jct.2018.02.022 — 152 data points at 92.3 kPa and 3.0 MHz, T = 293.15–308.15 K, x(ethanol) = 0–1. Selected values at 298.15 K:

**WM_Q#1_Table#6_(Main_Q#1_Answer):**

| *row_id* | *x(ethanol)* | *T (K)* | *P (kPa)* | *Speed of sound (m/s)* |
|---|---|---|---|---|
| WM_Q#1_Table#6_Row#1 | 「0」 | 「298.15」 | 「92.3」 | 「1496.99」 |
| WM_Q#1_Table#6_Row#2 | 「0.0997」 | 「298.15」 | 「92.3」 | 「1618.97」 |
| WM_Q#1_Table#6_Row#3 | 「0.1497」 | 「298.15」 | 「92.3」 | 「1600.11」 |
| WM_Q#1_Table#6_Row#4 | 「0.3507」 | 「298.15」 | 「92.3」 | 「1426.17」 |
| WM_Q#1_Table#6_Row#5 | 「0.5002」 | 「298.15」 | 「92.3」 | 「1337.91」 |
| WM_Q#1_Table#6_Row#6 | 「1」 | 「298.15」 | 「92.3」 | 「1143.50」 |

The speed of sound exhibits a pronounced **non-monotonic maximum** near x(ethanol) ≈ 0.1, reaching 1618.97 m/s — well above pure water (1496.99 m/s) or pure ethanol (1143.50 m/s). This reflects the strong intermolecular interactions and structural reorganization of the hydrogen-bond network in ethanol–water mixtures.

##### Representative Data: Mass Density (GLOBlit_220, PROPblock_2)

DOI 10.1016/j.fluid.2004.11.019 — 810 data points, T = 298.15–348.15 K, P = 100–40,000 kPa, x(ethanol) = 0.003–1.0. Density range: 739.4–1012.7 kg/m³.

---

#### Summary of Key Findings

**WM_Q#1_Table#7_(Main_Q#1_Answer):**

| *row_id* | *Property* | *Available?* | *Sources (DOIs)* | *Key Observations* |
|---|---|---|---|---|
| WM_Q#1_Table#7_Row#1 | 「Excess molar enthalpy (H^E)」 | 「✅ Yes (3 blocks, 31 points)」 | 「10.1016/j.fluid.2007.06.007, 10.1016/j.tca.2017.05.023」 | 「All negative (exothermic mixing); −0.707 kJ/mol at x(EtOH) = 0.102」 |
| WM_Q#1_Table#7_Row#2 | 「Excess molar volume (V^E)」 | 「❌ Not in database」 | 「—」 | 「Not directly reported; could be derived from density data」 |
| WM_Q#1_Table#7_Row#3 | 「Mass density」 | 「✅ Yes (17 blocks)」 | 「Multiple (see above)」 | 「739.4–1012.7 kg/m³ across full composition range」 |
| WM_Q#1_Table#7_Row#4 | 「Dynamic viscosity」 | 「✅ Yes (7 blocks)」 | 「Multiple」 | 「—」 |
| WM_Q#1_Table#7_Row#5 | 「Speed of sound」 | 「✅ Yes (3 blocks)」 | 「10.1016/j.jct.2018.02.022」 | 「Maximum ~1619 m/s near x(EtOH) ≈ 0.1 at 298.15 K」 |
| WM_Q#1_Table#7_Row#6 | 「Refractive index」 | 「✅ Yes (3 blocks)」 | 「Multiple」 | 「—」 |
| WM_Q#1_Table#7_Row#7 | 「Thermal conductivity」 | 「✅ Yes (2 blocks)」 | 「Multiple」 | 「—」 |
| WM_Q#1_Table#7_Row#8 | 「Henry's Law constant」 | 「✅ Yes (2 blocks)」 | 「Multiple」 | 「—」 |
| WM_Q#1_Table#7_Row#9 | 「Vapor pressure」 | 「✅ Yes (1 block)」 | 「—」 | 「—」 |
| WM_Q#1_Table#7_Row#10 | 「Surface tension」 | 「✅ Yes (1 block)」 | 「—」 | 「—」 |
| WM_Q#1_Table#7_Row#11 | 「Activity coefficient」 | 「✅ Yes (1 block)」 | 「—」 | 「—」 |

**Chemistry context:** The ethanol–water system is one of the most studied binary mixtures in thermodynamics. The strongly negative H^E values reflect the disruption and reorganization of the hydrogen-bond network upon mixing: water's tetrahedral H-bond structure is partially broken as ethanol molecules are incorporated, releasing energy. The non-monotonic speed of sound (maximum near x ≈ 0.1) and the well-known viscosity maximum near x(ethanol) ≈ 0.15–0.2 both point to the formation of microheterogeneous structures — ethanol-rich and water-rich clusters — that characterize this system at intermediate compositions. While V^E is not directly stored in ThermoML, the 17 mass density blocks spanning the full composition range provide the raw data needed to compute it.

**Core claims:**
- The ThermoML database contains extensive experimental data for the ethanol + water binary system in the 293–303 K window: 10 distinct property types across 39 data blocks from 26 publications, totaling 3,263 matching data points.
- Three verified data blocks provide excess molar enthalpy (H^E) measurements at 298.15 K; all H^E values are negative (exothermic mixing), ranging from −0.00104 kJ/mol at x(ethanol) = 0.000102 to −0.70659 kJ/mol at x(ethanol) = 0.102.
- Excess molar volume (V^E) is not directly reported in the ThermoML database for ethanol + water at any temperature or composition, though 17 mass density data blocks spanning the full composition range could in principle be used to compute it.
- Speed of sound at 298.15 K exhibits a non-monotonic maximum near x(ethanol) ≈ 0.1, reaching 1618.97 m/s — above pure water (1496.99 m/s) and pure ethanol (1143.50 m/s) — reflecting strong intermolecular interactions and hydrogen-bond network reorganization.
- Mass density data span 739.4–1012.7 kg/m³ across the full composition range at temperatures from 298.15–348.15 K and pressures from 100–40,000 kPa (17 blocks).

**Sources:**

**WM_Q#1_Table#8_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#8_Row#1 | 「GLOBlit_528」 | 「PROPblock_1」 | 「10.1016/j.fluid.2007.06.007」 | 「—」 | 「Provides 15 dilute-ethanol-in-water excess molar enthalpy data points at 298.15 K and 101.0 kPa, with H^E ranging from −0.01537 to −0.00104 kJ/mol, directly quoted in the answer's Section 1 tables.」 |
| WM_Q#1_Table#8_Row#2 | 「GLOBlit_528」 | 「PROPblock_2」 | 「10.1016/j.fluid.2007.06.007」 | 「—」 | 「Provides 15 dilute-water-in-ethanol excess molar enthalpy data points at 298.15 K and 101.0 kPa, with H^E ranging from −0.02961 to −0.00212 kJ/mol, directly quoted in the answer's Section 1 tables.」 |
| WM_Q#1_Table#8_Row#3 | 「GLOBlit_6377」 | 「PROPblock_1」 | 「10.1016/j.tca.2017.05.023」 | 「—」 | 「Provides a single excess molar enthalpy measurement of −0.70659 kJ/mol at x(ethanol) = 0.102 and 298.15 K, directly quoted in the answer to illustrate the magnitude of exothermic mixing at moderate composition.」 |
| WM_Q#1_Table#8_Row#4 | 「GLOBlit_5201」 | 「PROPblock_20」 | 「10.1016/j.jct.2018.02.022」 | 「—」 | 「Provides 152 speed-of-sound data points for ethanol + water at 293.15–308.15 K across the full composition range, with representative 298.15 K values quoted in the answer showing the non-monotonic maximum near x(ethanol) ≈ 0.1.」 |
| WM_Q#1_Table#8_Row#5 | 「GLOBlit_220」 | 「PROPblock_2」 | 「10.1016/j.fluid.2004.11.019」 | 「—」 | 「Provides 810 mass density data points for ethanol + water spanning 298.15–348.15 K and 100–40000 kPa across the full composition range, cited in the answer as the largest single data source and as representative density data.」 |

*Not stored here: 4 verbatim data_inspections table(s); 2 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

