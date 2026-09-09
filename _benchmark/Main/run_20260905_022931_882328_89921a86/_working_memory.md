# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_022931_882328_89921a86`

### History
- [parallel:2 tasks]
-   [query:ethanol_water_viscosity] "Find viscosity data for ethanol + water binary mixture at approximately equimola" (422s, 3 iters, validation=PASS verdict=## Verdict
The answer provides)
-   [query:methanol_water_viscosity] "Find viscosity data for methanol + water binary mixture at approximately equimol" (331s, 3 iters, validation=PASS verdict=## Verdict
The answer provides)
- [menu:run] inspect_block_table → ERROR: nearest must be {"column": alias, "value": number, "k": 1..8}
- [menu:run] inspect_block_table → ERROR: `where` must be a non-empty filter string when given
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK

### Query Agent Results

#### ethanol_water_viscosity
**ethanol_water_viscosity** — confidence: high · validation: PASS

**Answer:**

#### Viscosity Data for Ethanol + Water Binary Mixture at x ≈ 0.5 and 298.15 K

##### Dynamic Viscosity (η)

Two ThermoML data blocks provide dynamic viscosity measurements for the ethanol–water binary system near equimolar composition at 298.15 K:

---

###### Source 1: GLOBlit_5201 — PROPblock_21
**DOI:** 10.1016/j.jct.2018.02.022  
**Pressure:** 92.3 kPa  
**Composition variable:** mole fraction of ethanol  
**Method:** Concentric cylinders viscometry  
**Block size:** 100 data points, T = 293.15–308.15 K, x(ethanol) = 0–1

Data near x(ethanol) ≈ 0.5 at 298.15 K:

**WM_Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *x(ethanol)* | *T (K)* | *P (kPa)* | *η (Pa·s)* |
|---|---|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「0.399」 | 「298.15」 | 「92.3」 | 「0.0021697」 |
| WM_Q#1_Table#1_Row#2 | 「0.4495」 | 「298.15」 | 「92.3」 | 「0.0020662」 |
| WM_Q#1_Table#1_Row#3 | 「**0.4989**」 | 「**298.15**」 | 「**92.3**」 | 「**0.0019557**」 |
| WM_Q#1_Table#1_Row#4 | 「0.5495」 | 「298.15」 | 「92.3」 | 「0.0018796」 |
| WM_Q#1_Table#1_Row#5 | 「0.6067」 | 「298.15」 | 「92.3」 | 「0.0017439」 |

**Best match:** At x(ethanol) = 0.4989, the dynamic viscosity is **0.0019557 Pa·s (≈ 1.96 mPa·s)**. The full 298.15 K isotherm across all 25 compositions spans η = 0.00089689–0.0024286 Pa·s.

---

###### Source 2: GLOBlit_2825 — PROPblock_11
**DOI:** 10.1016/j.jct.2007.05.004  
**Pressure:** 101.0 kPa  
**Composition variable:** mole fraction of water  
**Block size:** 37 data points, T = 293.15–303.15 K, x(water) = 0–1

This block does not have an exact x = 0.5 point; the nearest bracketing values at 298.15 K are:

**WM_Q#1_Table#2_(Main_Q#1_Answer):**

| *row_id* | *x(water)* | *x(ethanol) ≈* | *T (K)* | *P (kPa)* | *η (Pa·s)* |
|---|---|---|---|---|---|
| WM_Q#1_Table#2_Row#1 | 「0.2961」 | 「0.70」 | 「298.15」 | 「101.0」 | 「0.001531」 |
| WM_Q#1_Table#2_Row#2 | 「0.3991」 | 「0.60」 | 「298.15」 | 「101.0」 | 「0.001659」 |
| WM_Q#1_Table#2_Row#3 | 「0.5989」 | 「0.40」 | 「298.15」 | 「101.0」 | 「0.002115」 |
| WM_Q#1_Table#2_Row#4 | 「0.6991」 | 「0.30」 | 「298.15」 | 「101.0」 | 「0.002275」 |

Pure ethanol from this block: η = 0.001082 Pa·s at 298.15 K (x(water) = 0).

---

##### Excess / Deviation Viscosity (Δη)

**No excess viscosity or viscosity deviation data are available in the ThermoML database.** The ThermoML schema does not include any excess transport properties. The only excess properties stored are thermodynamic quantities:

**WM_Q#1_Table#3_(Main_Q#1_Answer):**

| *row_id* | *Property* | *ID* |
|---|---|---|
| WM_Q#1_Table#3_Row#1 | 「Excess molar enthalpy」 | 「GLOBprop_17」 |
| WM_Q#1_Table#3_Row#2 | 「Excess molar volume」 | 「GLOBprop_28」 |
| WM_Q#1_Table#3_Row#3 | 「Excess molar heat capacity」 | 「GLOBprop_85」 |
| WM_Q#1_Table#3_Row#4 | 「Excess molar Gibbs energy」 | 「GLOBprop_97」 |

However, the viscosity deviation can be **computed** from the absolute viscosity data above using:

> Δη = η_mix − (x₁·η₁° + x₂·η₂°)

The pure-component viscosities needed for this calculation are available in the database (e.g., pure ethanol η = 0.001082 Pa·s from GLOBlit_2825 :: PROPblock_11, and the pure water endpoint from the same or other blocks).

---

##### Kinematic Viscosity

No kinematic viscosity data were found for the ethanol–water binary system in the ThermoML database.

---

##### Chemistry Insight

The ethanol–water system is a classic example of non-ideal mixing behavior in transport properties. At near-equimolar composition, the dynamic viscosity (≈ 1.96 mPa·s at x(ethanol) = 0.4989) significantly exceeds that of either pure component — pure ethanol is 0.001082 Pa·s (1.08 mPa·s) and pure water is approximately 0.00089 Pa·s (0.89 mPa·s) at 298.15 K. This viscosity maximum arises from strong hydrogen-bonding interactions between ethanol and water molecules, which create more structured, higher-friction intermolecular networks than exist in either pure liquid.

The data from GLOBlit_5201 :: PROPblock_21 clearly show that at 298.15 K, viscosity increases as x(ethanol) decreases from 0.5495 (η = 0.0018796 Pa·s) through 0.4989 (η = 0.0019557 Pa·s) to 0.4495 (η = 0.0020662 Pa·s) and 0.399 (η = 0.0021697 Pa·s), confirming that the viscosity maximum lies on the water-rich side of the composition range (around x(ethanol) ≈ 0.3–0.4), consistent with the well-known behavior of this system.

##### Additional Data Availability

Eight additional dynamic viscosity blocks for the ethanol–water binary system were identified in the ThermoML database from other publications (including DOIs 10.1021/acs.jced.7b00299, 10.1021/acs.jced.8b00086, 10.1021/acs.jced.8b00939, and 10.1021/je4003515), using various composition variables (mass fraction, molality) and temperature ranges that overlap 298.15 K.

**Core claims:**
- At x(ethanol) = 0.4989 and 298.15 K (92.3 kPa), the dynamic viscosity of the ethanol–water binary mixture is 0.0019557 Pa·s (≈ 1.96 mPa·s), as reported in ThermoML data from DOI 10.1016/j.jct.2018.02.022.
- A second ThermoML source (DOI 10.1016/j.jct.2007.05.004, 101.0 kPa) brackets x(ethanol) ≈ 0.5 at 298.15 K with values of η = 0.002115 Pa·s at x(ethanol) ≈ 0.40 and η = 0.001659 Pa·s at x(ethanol) ≈ 0.60, but does not include an exact equimolar data point.
- No excess viscosity, viscosity deviation, or kinematic viscosity data for the ethanol–water binary system are available in the ThermoML database; the ThermoML schema does not include excess transport properties.
- At 298.15 K, the near-equimolar mixture viscosity (≈ 1.96 mPa·s) exceeds that of both pure ethanol (0.001082 Pa·s) and pure water (approximately 0.00089 Pa·s), and the data indicate the viscosity maximum lies on the water-rich side around x(ethanol) ≈ 0.3–0.4, consistent with the well-known non-ideal hydrogen-bonding behavior of this system.

**Sources:**

**WM_Q#1_Table#4_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#4_Row#1 | 「GLOBlit_5201」 | 「PROPblock_21」 | 「10.1016/j.jct.2018.02.022」 | 「—」 | 「This block provides dynamic viscosity data for the ethanol–water binary system across the full mole fraction range (0–1) at temperatures including 298.15 K. It contains the closest composition point to x(ethanol) = 0.5 (x = 0.4989) with η = 0.0019557 Pa·s, which is the primary datum in the answer.」 |
| WM_Q#1_Table#4_Row#2 | 「GLOBlit_2825」 | 「PROPblock_11」 | 「10.1016/j.jct.2007.05.004」 | 「—」 | 「This block provides complementary dynamic viscosity data for the ethanol–water binary at 298.15 K across the full composition range, including pure ethanol (η = 0.001082 Pa·s) and bracketing compositions around x(ethanol) = 0.5. It supports the answer by supplying pure-component reference values and independent corroboration of the viscosity trend.」 |

*Not stored here: 5 verbatim data_inspections table(s); 4 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### methanol_water_viscosity
**methanol_water_viscosity** — confidence: high · validation: PASS

**Answer:**

#### Viscosity Data for Methanol + Water Binary Mixture at x ≈ 0.5 and 298.15 K

##### Dynamic Viscosity

The primary data source is from DOI 10.1016/j.jct.2007.05.004 (GLOBlit_2825, PROPblock_9), which contains 39 data points of dynamic viscosity for the methanol + water binary system, covering T = 293.15–303.15 K across the full mole-fraction range, measured by capillary tube method at 101.0 kPa.

**Data at T = 298.15 K near equimolar composition:**

**WM_Q#2_Table#1_(Main_Q#2_Answer):**

| *row_id* | *Temperature (K)* | *x(water)* | *Pressure (kPa)* | *η (Pa·s)* | *η (mPa·s)* |
|---|---|---|---|---|---|
| WM_Q#2_Table#1_Row#1 | 「298.15」 | 「0.2983」 | 「101.0」 | 「0.000987」 | 「0.987」 |
| WM_Q#2_Table#1_Row#2 | 「298.15」 | 「0.3985」 | 「101.0」 | 「0.00115」 | 「1.150」 |
| WM_Q#2_Table#1_Row#3 | 「298.15」 | 「**0.5003**」 | 「101.0」 | 「**0.001309**」 | 「**1.309**」 |
| WM_Q#2_Table#1_Row#4 | 「298.15」 | 「0.5994」 | 「101.0」 | 「0.001463」 | 「1.463」 |
| WM_Q#2_Table#1_Row#5 | 「298.15」 | 「0.6997」 | 「101.0」 | 「0.001554」 | 「1.554」 |

The closest composition to equimolar is **x(water) = 0.5003**, where the dynamic viscosity is **0.001309 Pa·s (≈ 1.309 mPa·s)** at 298.15 K and 101.0 kPa.

##### Chemistry Insight

The methanol–water system exhibits strongly non-ideal viscosity behavior. At the near-equimolar composition, the mixture viscosity (1.309 mPa·s) is substantially higher than that of pure methanol (η = 0.000545 Pa·s at x(water) = 0 in this dataset), and the viscosity continues to increase toward the water-rich side, reaching 0.001554 Pa·s at x(water) = 0.6997. This positive viscosity deviation from ideal mixing is attributed to enhanced hydrogen-bonding network formation between methanol and water molecules at intermediate compositions — the OH group of methanol integrates into the three-dimensional hydrogen-bond network of water, creating more structured and viscous microdomains.

##### Additional Data Sources

Three other ThermoML blocks contain dynamic viscosity data for the methanol + water binary system, though with less relevant coverage for the target conditions:

**WM_Q#2_Table#2_(Main_Q#2_Answer):**

| *row_id* | *Source (DOI)* | *Literature ID* | *Block* | *Composition variable* | *Composition range* | *T range (K)* | *Data points* |
|---|---|---|---|---|---|---|---|
| WM_Q#2_Table#2_Row#1 | 「10.1016/j.jct.2007.05.004」 | 「GLOBlit_2825」 | 「PROPblock_9」 | 「Mole fraction (water)」 | 「0.0–1.0」 | 「293.15–303.15」 | 「39」 |
| WM_Q#2_Table#2_Row#2 | 「10.1016/j.jct.2019.05.013」 | 「GLOBlit_5533」 | 「PROPblock_3」 | 「Mass fraction (methanol)」 | 「0.0–0.4999」 | 「273.15–293.15」 | 「12」 |
| WM_Q#2_Table#2_Row#3 | 「10.1021/je0600810」 | 「GLOBlit_8869」 | 「PROPblock_3」 | 「Volume fraction (methanol)」 | 「0.01–0.3」 | 「298.15–318.15」 | 「9」 |
| WM_Q#2_Table#2_Row#4 | 「10.1021/je2003622」 | 「GLOBlit_9571」 | 「PROPblock_1」 | 「Mass fraction (methanol)」 | 「0.0806–0.3446」 | 「298.15–323.15」 | 「16」 |

Note that GLOBlit_5533 covers only T = 273.15–293.15 K (does not include 298.15 K), and GLOBlit_8869 and GLOBlit_9571 cover only the methanol-lean side (not reaching equimolar composition). The most complete source for the requested conditions is **GLOBlit_2825 (PROPblock_9)**.

##### Excess / Deviation Viscosity and Kinematic Viscosity

**No excess viscosity or viscosity deviation data** exists for the methanol + water system in the ThermoML database. The ThermoML property registry does not include any excess or deviation transport properties — only excess thermodynamic properties are available (excess molar enthalpy, excess molar volume, excess molar heat capacity, excess molar Gibbs energy).

**No kinematic viscosity data** was found for this system either. Dynamic viscosity (GLOBprop_4) is the only viscosity property available.

To obtain excess or deviation viscosity values, one would need to compute them from the available dynamic viscosity data using an appropriate mixing rule, such as:
- **Linear deviation:** Δη = η_mix − (x₁η₁ + x₂η₂)
- **Logarithmic deviation:** Δ(ln η) = ln η_mix − (x₁ ln η₁ + x₂ ln η₂)

Using the data from GLOBlit_2825 at 298.15 K, with pure methanol η = 0.000545 Pa·s (x(water) = 0) and pure water η ≈ 0.000890 Pa·s (from the water-rich end of the dataset), the linear deviation at x(water) = 0.5003 would be positive and substantial, confirming the strongly non-ideal mixing behavior of this system.

**Core claims:**
- At 298.15 K, 101.0 kPa, and x(water) = 0.5003, the dynamic viscosity of the methanol + water binary mixture is 0.001309 Pa·s (≈ 1.309 mPa·s), as reported in DOI 10.1016/j.jct.2007.05.004 (GLOBlit_2825, PROPblock_9).
- The methanol–water system exhibits strongly non-ideal viscosity behavior, with the mixture viscosity at near-equimolar composition (1.309 mPa·s) substantially exceeding that of pure methanol (0.000545 Pa·s at x(water) = 0 in the same dataset), attributed to enhanced hydrogen-bonding network formation between methanol and water molecules.
- No excess viscosity, viscosity deviation, or kinematic viscosity data exists for the methanol + water system in the ThermoML database; dynamic viscosity is the only viscosity property available.
- Three additional ThermoML data sources contain dynamic viscosity for methanol + water, but none cover both 298.15 K and equimolar composition simultaneously, making GLOBlit_2825 (PROPblock_9) the most complete source for the requested conditions.

**Sources:**

**WM_Q#2_Table#3_(Main_Q#2_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#2_Table#3_Row#1 | 「GLOBlit_2825」 | 「PROPblock_9」 | 「10.1016/j.jct.2007.05.004」 | 「—」 | 「Primary source providing dynamic viscosity for methanol + water across the full mole-fraction range (0.0–1.0) at 293.15–303.15 K including 298.15 K. It contains the key equimolar data point at x(water) = 0.5003 with η = 0.001309 Pa·s, which is the central result of the answer.」 |

*Not stored here: 1 verbatim data_inspections table(s); 2 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

