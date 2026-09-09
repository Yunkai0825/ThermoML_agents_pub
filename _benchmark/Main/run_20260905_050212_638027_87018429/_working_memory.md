# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_050212_638027_87018429`

### History
- [parallel:2 tasks]
-   [query:mixture_density] "Find density measurements for the binary mixture of water and 1-propanol near 29" (567s, 3 iters, validation=PASS verdict=## Verdict
The answer is compr)
-   [query:pure_water_density] "Find the experimental density of pure water at 298.15 K. I need the exact densit" (141s, 2 iters, validation=PASS verdict=## Verdict
The answer appears )
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → ERROR: nearest must be {"column": alias, "value": number, "k": 1..8}
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK

### Query Agent Results

#### mixture_density
**mixture_density** — confidence: medium · validation: PASS

**Answer:**

#### Mass Density Data for the Binary Mixture of Water + 1-Propanol near 298.15 K

**System:** Water (H₂O) + 1-Propanol (C₃H₈O), binary liquid mixture  
**Property:** Mass density (kg/m³)

##### Overview

A search of the ThermoML database identified **13 data blocks** from **11 independent literature sources** containing mass density measurements for the water + 1-propanol binary system with temperatures encompassing or near 298.15 K. These blocks span a wide range of compositions (dilute aqueous to nearly pure 1-propanol), pressures (atmospheric to ~40 MPa), and temperature ranges. Three blocks were inspected in detail for verbatim data points at exactly 298.15 K.

---

##### Complete Block Inventory

**WM_Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *#* | *DOI* | *Block* | *T range (K)* | *Composition variable & range* | *P (kPa)* | *ρ range (kg/m³)* | *N pts* | *Method* |
|---|---|---|---|---|---|---|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「1」 | 「10.1016/j.fluid.2007.07.066」 | 「PROPblock_8」 | 「283.15–303.15」 | 「Mass fraction, 0.05–0.15」 | 「101.0」 | 「976.004–992.444」 | 「15」 | 「Vibrating tube」 |
| WM_Q#1_Table#1_Row#2 | 「2」 | 「10.1016/j.fluid.2008.01.004」 | 「PROPblock_5」 | 「283.15–303.15」 | 「Mass fraction, 0.05–0.15」 | 「101.0」 | 「975.791–992.405」 | 「15」 | 「Vibrating tube」 |
| WM_Q#1_Table#1_Row#3 | 「3」 | 「10.1016/j.jct.2004.07.019」 | 「PROPblock_3」 | 「298.15–573.15」 | 「Molality, 0.0943–0.84695 mol/kg」 | 「420–30310」 | 「(excess density reported)」 | 「456」 | 「Vibrating tube」 |
| WM_Q#1_Table#1_Row#4 | 「4」 | 「10.1016/j.jct.2008.07.005」 | 「PROPblock_9」 | 「283.15–308.15」 | 「Mole fraction, 0.0–0.2」 | 「98.93」 | 「911.83–999.69」 | 「96」 | 「Pycnometric」 |
| WM_Q#1_Table#1_Row#5 | 「5」 | 「10.1016/j.jct.2013.11.036」 | 「PROPblock_1」 | 「298.15–582.08」 | 「Molality, 0.869–56.348 mol/kg」 | 「2353–40000」 | 「322.1–1004.4」 | 「174」 | 「Constant-volume piezometry」 |
| WM_Q#1_Table#1_Row#6 | 「6」 | 「10.1016/j.jct.2013.11.036」 | 「PROPblock_2」 | 「292.05–352.05」 | 「Molality, 0.869–56.348 mol/kg」 | 「101.0」 | 「801.03–991.42」 | 「29」 | 「Pycnometric」 |
| WM_Q#1_Table#1_Row#7 | 「7」 | 「10.1016/j.jct.2015.06.024」 | 「PROPblock_5」 | 「288.15–308.15」 | 「Molality, 0.01666–0.16617 mol/kg」 | 「84.5」 | 「992.305–998.928」 | 「40」 | 「Vibrating tube」 |
| WM_Q#1_Table#1_Row#8 | 「8」 | 「10.1016/j.jct.2019.105880」 | 「PROPblock_7」 | 「288.15–303.15」 | 「Mass fraction, 0.1–0.4」 | 「100.0」 | 「924.386–985.245」 | 「16」 | 「Vibrating tube」 |
| WM_Q#1_Table#1_Row#9 | 「9」 | 「10.1021/acs.jced.6b01058」 | 「PROPblock_8」 | 「298.15–313.15」 | 「Mass fraction, 0.04–0.16」 | 「85.0」 | 「966.84–990.59」 | 「12」 | 「Vibrating tube」 |
| WM_Q#1_Table#1_Row#10 | 「10」 | 「10.1021/acs.jced.7b00299」 | 「PROPblock_13」 | 「298.15–313.15」 | 「Molality = 14.0 mol/kg (fixed)」 | 「100.0」 | 「903.156–914.36」 | 「2」 | 「Vibrating tube」 |
| WM_Q#1_Table#1_Row#11 | 「11」 | 「10.1021/je034101z」 | 「PROPblock_6」 | 「282.15–425.15」 | 「Mole fraction, 0.255–0.738」 | 「5753–29883」 | 「731.4–896.2」 | 「380」 | 「Isochoric」 |
| WM_Q#1_Table#1_Row#12 | 「12」 | 「10.1021/je4003515」 | 「PROPblock_10」 | 「293.15–313.15」 | 「Molality, 14.0–22.0 mol/kg」 | 「101.0」 | 「879.756–918.103」 | 「25」 | 「Vibrating tube」 |
| WM_Q#1_Table#1_Row#13 | 「13」 | 「10.1021/je800158z」 | 「PROPblock_3」 | 「293.15–323.15」 | 「Mole fraction, 0.0–1.0」 | 「81.5」 | 「778.92–998.2」 | 「56」 | 「Vibrating tube」 |

**Notes on block types:**
- Blocks 1, 2, 4, 7, 8, 9, 13 are **atmospheric-pressure** datasets most directly relevant to standard 298.15 K measurements.
- Blocks 3, 5, 11 are **high-pressure** datasets (up to ~40 MPa) and may report excess or differential densities.
- Block 13 (DOI 10.1021/je800158z) provides the widest composition coverage at atmospheric pressure, spanning the **full mole-fraction range 0.0–1.0**.

---

##### Inspected Data Points at T = 298.15 K

###### Source 1: DOI 10.1016/j.fluid.2007.07.066, PROPblock_8
**Constraint:** P = 101.0 kPa | **Composition:** mass fraction of 1-propanol

**WM_Q#1_Table#2_(Main_Q#1_Answer):**

| *row_id* | *Mass fraction (1-propanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_Q#1_Table#2_Row#1 | 「0.05」 | 「989.431」 |
| WM_Q#1_Table#2_Row#2 | 「0.10」 | 「983.475」 |
| WM_Q#1_Table#2_Row#3 | 「0.15」 | 「978.117」 |

###### Source 2: DOI 10.1016/j.fluid.2008.01.004, PROPblock_5
**Constraint:** P = 101.0 kPa | **Composition:** mass fraction of 1-propanol

**WM_Q#1_Table#3_(Main_Q#1_Answer):**

| *row_id* | *Mass fraction (1-propanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_Q#1_Table#3_Row#1 | 「0.05」 | 「989.387」 |
| WM_Q#1_Table#3_Row#2 | 「0.10」 | 「983.372」 |
| WM_Q#1_Table#3_Row#3 | 「0.15」 | 「977.921」 |

###### Source 3: DOI 10.1016/j.jct.2008.07.005, PROPblock_9
**Constraint:** P = 98.93 kPa | **Composition:** mole fraction of 1-propanol

**WM_Q#1_Table#4_(Main_Q#1_Answer):**

| *row_id* | *Mole fraction (1-propanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_Q#1_Table#4_Row#1 | 「0」 | 「997.04」 |
| WM_Q#1_Table#4_Row#2 | 「0.002」 | 「995.4」 |
| WM_Q#1_Table#4_Row#3 | 「0.005」 | 「993.76」 |
| WM_Q#1_Table#4_Row#4 | 「0.009」 | 「991.66」 |
| WM_Q#1_Table#4_Row#5 | 「0.01」 | 「991.14」 |
| WM_Q#1_Table#4_Row#6 | 「0.02」 | 「986.54」 |
| WM_Q#1_Table#4_Row#7 | 「0.03」 | 「982.56」 |
| WM_Q#1_Table#4_Row#8 | 「0.05」 | 「975.49」 |

---

##### Chemistry Insights

1. **Monotonic density decrease:** All three inspected sources consistently show that density decreases monotonically with increasing 1-propanol content at 298.15 K. Starting from ~997 kg/m³ for pure water, the density drops to ~975 kg/m³ at a mole fraction of 0.05 (Source 3). This reflects the lower intrinsic density of 1-propanol (~803 kg/m³ at 298.15 K) compared to water.

2. **Inter-source consistency:** Sources 1 and 2 use the same composition variable (mass fraction) at the same pressure (101.0 kPa) and show excellent agreement — e.g., at w = 0.05, the densities are 989.431 vs. 989.387 kg/m³ (difference of only 0.044 kg/m³), providing confidence in the data quality.

3. **Composition coverage:** The inspected data cover only the water-rich region. For broader coverage including the 1-propanol-rich side, the block from DOI 10.1021/je800158z (PROPblock_3, mole fraction 0.0–1.0, 56 points, 293.15–323.15 K) and DOI 10.1016/j.jct.2013.11.036 (PROPblock_2, molality 0.869–56.348 mol/kg, 29 points at 101.0 kPa) would be the most relevant uninspected atmospheric-pressure sources.

4. **High-pressure data:** Three blocks (from DOIs 10.1016/j.jct.2004.07.019, 10.1016/j.jct.2013.11.036, and 10.1021/je034101z) provide density data at elevated pressures up to ~40 MPa, useful for equation-of-state modeling.

**Core claims:**
- Thirteen data blocks from eleven independent ThermoML literature sources were identified containing mass density measurements for the water + 1-propanol binary liquid mixture at or near 298.15 K, spanning compositions from dilute aqueous to nearly pure 1-propanol and pressures from atmospheric to ~40 MPa.
- At 298.15 K and atmospheric pressure, all three inspected sources consistently show that mass density decreases monotonically with increasing 1-propanol content, from ~997 kg/m³ for pure water to ~975 kg/m³ at a 1-propanol mole fraction of 0.05.
- Two independent sources at 101.0 kPa and mass fraction 0.05 of 1-propanol report densities of 989.431 and 989.387 kg/m³, a difference of only 0.044 kg/m³, indicating excellent inter-source consistency.
- The three inspected data blocks cover only the water-rich composition region; broader composition coverage including the 1-propanol-rich side is available in uninspected blocks but was not verified.

**Sources:**

**WM_Q#1_Table#5_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#5_Row#1 | 「GLOBlit_555」 | 「PROPblock_8」 | 「10.1016/j.fluid.2007.07.066」 | 「—」 | 「Provides mass density of water + 1-propanol at 298.15 K and 101.0 kPa for mass fractions 0.05–0.15; verbatim data points (989.431, 983.475, 978.117 kg/m³) are quoted in the answer.」 |
| WM_Q#1_Table#5_Row#2 | 「GLOBlit_590」 | 「PROPblock_5」 | 「10.1016/j.fluid.2008.01.004」 | 「—」 | 「Provides mass density of water + 1-propanol at 298.15 K and 101.0 kPa for mass fractions 0.05–0.15; verbatim data points (989.387, 983.372, 977.921 kg/m³) are quoted and used for inter-source consistency comparison.」 |
| WM_Q#1_Table#5_Row#3 | 「GLOBlit_2432」 | 「PROPblock_3」 | 「10.1016/j.jct.2004.07.019」 | 「—」 | 「High-pressure density data for water + 1-propanol starting at 298.15 K; the card shows negative property values indicating excess/differential density rather than absolute density, which the answer correctly notes. Contributes to the high-pressure data inventory.」 |
| WM_Q#1_Table#5_Row#4 | 「GLOBlit_2979」 | 「PROPblock_9」 | 「10.1016/j.jct.2008.07.005」 | 「—」 | 「Provides mass density of water + 1-propanol at 298.15 K and 98.93 kPa for mole fractions 0.0–0.2; verbatim data points (997.04 down to 975.49 kg/m³) are quoted in the answer's inspected data section.」 |
| WM_Q#1_Table#5_Row#5 | 「GLOBlit_4068」 | 「PROPblock_1」 | 「10.1016/j.jct.2013.11.036」 | 「—」 | 「High-pressure (2353–40000 kPa) mass density data for water + 1-propanol including 298.15 K; contributes to the answer's inventory of high-pressure datasets for equation-of-state modeling.」 |
| WM_Q#1_Table#5_Row#6 | 「GLOBlit_4068」 | 「PROPblock_2」 | 「10.1016/j.jct.2013.11.036」 | 「—」 | 「Atmospheric-pressure (101.0 kPa) pycnometric density data for water + 1-propanol spanning 292.05–352.05 K and molality 0.869–56.348 mol/kg, providing broad composition coverage including the 1-propanol-rich region as noted in the answer.」 |
| WM_Q#1_Table#5_Row#7 | 「GLOBlit_4415」 | 「PROPblock_5」 | 「10.1016/j.jct.2015.06.024」 | 「—」 | 「Provides mass density of dilute water + 1-propanol mixtures (molality 0.017–0.166 mol/kg) at temperatures including 298.15 K; contributes atmospheric-pressure data in the very dilute composition regime.」 |
| WM_Q#1_Table#5_Row#8 | 「GLOBlit_5585」 | 「PROPblock_7」 | 「10.1016/j.jct.2019.105880」 | 「—」 | 「Provides mass density at 288.15–303.15 K and 100.0 kPa for mass fractions 0.1–0.4, extending composition coverage to higher 1-propanol content than Sources 1 and 2 in the answer.」 |
| WM_Q#1_Table#5_Row#9 | 「GLOBlit_7085」 | 「PROPblock_8」 | 「10.1021/acs.jced.6b01058」 | 「—」 | 「Provides mass density at 298.15–313.15 K and 85.0 kPa for mass fractions 0.04–0.16; contributes atmospheric-pressure data at 298.15 K in the water-rich region.」 |
| WM_Q#1_Table#5_Row#10 | 「GLOBlit_7178」 | 「PROPblock_13」 | 「10.1021/acs.jced.7b00299」 | 「—」 | 「Provides mass density at fixed molality 14.0 mol/kg (1-propanol-rich) at 298.15 and 313.15 K; contributes a data point in the propanol-rich composition regime at 298.15 K.」 |
| WM_Q#1_Table#5_Row#11 | 「GLOBlit_8254」 | 「PROPblock_6」 | 「10.1021/je034101z」 | 「—」 | 「High-pressure isochoric density data for water + 1-propanol at mole fractions 0.255–0.738 and temperatures including near 298.15 K; contributes to the answer's high-pressure data inventory.」 |
| WM_Q#1_Table#5_Row#12 | 「GLOBlit_10159」 | 「PROPblock_10」 | 「10.1021/je4003515」 | 「—」 | 「Provides mass density at 293.15–313.15 K and 101.0 kPa for molality 14.0–22.0 mol/kg, covering the 1-propanol-rich composition range at atmospheric pressure including near 298.15 K.」 |
| WM_Q#1_Table#5_Row#13 | 「GLOBlit_11142」 | 「PROPblock_3」 | 「10.1021/je800158z」 | 「—」 | 「Provides mass density spanning the full mole-fraction range 0.0–1.0 at 293.15–323.15 K and 81.5 kPa; the answer highlights this as the widest composition coverage atmospheric-pressure source.」 |

*Not stored here: 3 verbatim data_inspections table(s); 3 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### pure_water_density
**pure_water_density** — confidence: high · validation: PASS

**Answer:**

#### Experimental Density of Pure Water at 298.15 K

Multiple independent sources in the ThermoML database report the mass density of pure liquid water at 298.15 K. Here are two verified data points:

##### Source 1 — Single-point measurement

**WM_Q#2_Table#1_(Main_Q#2_Answer):**

| *row_id* | *Parameter* | *Value* |
|---|---|---|
| WM_Q#2_Table#1_Row#1 | 「**Density**」 | 「**997.06 kg/m³**」 |
| WM_Q#2_Table#1_Row#2 | 「Temperature」 | 「298.15 K」 |
| WM_Q#2_Table#1_Row#3 | 「Pressure」 | 「101.325 kPa」 |
| WM_Q#2_Table#1_Row#4 | 「Phase」 | 「Liquid」 |
| WM_Q#2_Table#1_Row#5 | 「DOI」 | 「10.1016/j.fluid.2005.09.009 (GLOBlit_306)」 |
| WM_Q#2_Table#1_Row#6 | 「Block」 | 「PROPblock_6」 |
| WM_Q#2_Table#1_Row#7 | 「Measurement method」 | 「Vibrating tube (GLOBmeas_141)」 |

##### Source 2 — Multi-point measurement

**WM_Q#2_Table#2_(Main_Q#2_Answer):**

| *row_id* | *Parameter* | *Value* |
|---|---|---|
| WM_Q#2_Table#2_Row#1 | 「**Density**」 | 「**997.043 kg/m³**」 |
| WM_Q#2_Table#2_Row#2 | 「Temperature」 | 「298.15 K」 |
| WM_Q#2_Table#2_Row#3 | 「Pressure」 | 「101.0 kPa」 |
| WM_Q#2_Table#2_Row#4 | 「Phase」 | 「Liquid」 |
| WM_Q#2_Table#2_Row#5 | 「DOI」 | 「10.1016/j.fluid.2007.07.066 (GLOBlit_555)」 |
| WM_Q#2_Table#2_Row#6 | 「Block」 | 「PROPblock_2」 |
| WM_Q#2_Table#2_Row#7 | 「Measurement method」 | 「Vibrating tube (GLOBmeas_134)」 |

##### Summary

Across at least six independent single-point measurements and several multi-point datasets in the ThermoML database, the mass density of pure water at 298.15 K consistently falls in the narrow range **997.04–997.06 kg/m³** at ambient pressure (~101 kPa). The two inspected values — 997.06 kg/m³ and 997.043 kg/m³ — differ by only ~0.02 kg/m³, reflecting excellent inter-laboratory agreement. The tiny difference is consistent with the slightly different reported pressures (101.325 vs. 101.0 kPa). Either value serves as a reliable baseline for comparing mixture density measurements at 298.15 K.

**Core claims:**
- Multiple independent ThermoML sources report the mass density of pure liquid water at 298.15 K and ambient pressure (~101 kPa) consistently in the narrow range 997.04–997.06 kg/m³.
- Two verified values — 997.06 kg/m³ (at 101.325 kPa) and 997.043 kg/m³ (at 101.0 kPa) — differ by only ~0.02 kg/m³, reflecting excellent inter-laboratory agreement.
- Both measurements were obtained using vibrating tube densimetry and either value serves as a reliable baseline for comparing mixture density measurements at 298.15 K.

**Sources:**

**WM_Q#2_Table#3_(Main_Q#2_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#2_Table#3_Row#1 | 「GLOBlit_306」 | 「PROPblock_6」 | 「10.1016/j.fluid.2005.09.009」 | 「—」 | 「Provides a single-point mass density measurement of pure water at 298.15 K and 101.325 kPa, reporting 997.06 kg/m³ via vibrating tube densimetry, which is directly quoted in the answer as Source 1.」 |
| WM_Q#2_Table#3_Row#2 | 「GLOBlit_555」 | 「PROPblock_2」 | 「10.1016/j.fluid.2007.07.066」 | 「—」 | 「Contains 5 data points of pure water density spanning 283.15–303.15 K at 101.0 kPa (range 995.645–999.699 kg/m³), which includes the 298.15 K point yielding 997.043 kg/m³ cited in the answer as Source 2.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

