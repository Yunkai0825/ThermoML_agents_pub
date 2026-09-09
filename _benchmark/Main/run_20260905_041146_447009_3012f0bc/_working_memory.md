# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041146_447009_3012f0bc`

### History
- [parallel:2 tasks]
-   [query:ethanol_water_viscosity] "Find viscosity data for the binary mixture of ethanol and water at 25°C (298.15 " (188s, 2 iters, validation=PASS verdict=## Verdict
The answer is scien)
-   [query:methanol_water_viscosity] "Find viscosity data for the binary mixture of methanol and water at 25°C (298.15" (215s, 2 iters, validation=PASS verdict=## Verdict
The answer is scien)
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

### Query Agent Results

#### ethanol_water_viscosity
**ethanol_water_viscosity** — confidence: high · validation: PASS

**Answer:**

#### Dynamic Viscosity of Ethanol + Water Binary Mixtures at 298.15 K

Two comprehensive experimental datasets were found in the ThermoML database for the dynamic viscosity of ethanol + water binary mixtures at 298.15 K (25 °C).

---

##### Dataset 1 — DOI: 10.1016/j.jct.2007.05.004

**Source block:** PROPblock_11 · Pressure: 101.0 kPa · 12 data points at 298.15 K · Method: Capillary tube viscometry  
Composition expressed as **mole fraction of water**.

**WM_Q#1_Table#1_(Main_Q#1_Answer):**

| *row_id* | *x(water)* | *η (Pa·s)* |
|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「0 (pure ethanol)」 | 「0.001082」 |
| WM_Q#1_Table#1_Row#2 | 「0.0501」 | 「0.001153」 |
| WM_Q#1_Table#1_Row#3 | 「0.0986」 | 「0.001232」 |
| WM_Q#1_Table#1_Row#4 | 「0.1961」 | 「0.001380」 |
| WM_Q#1_Table#1_Row#5 | 「0.2961」 | 「0.001531」 |
| WM_Q#1_Table#1_Row#6 | 「0.3991」 | 「0.001659」 |
| WM_Q#1_Table#1_Row#7 | 「0.5989」 | 「0.002115」 |
| WM_Q#1_Table#1_Row#8 | 「0.6991」 | 「0.002275」 |
| WM_Q#1_Table#1_Row#9 | 「0.8001」 | 「**0.002300** (maximum)」 |
| WM_Q#1_Table#1_Row#10 | 「0.8996」 | 「0.001860」 |
| WM_Q#1_Table#1_Row#11 | 「0.9499」 | 「0.001388」 |
| WM_Q#1_Table#1_Row#12 | 「1 (pure water)」 | 「0.000890」 |

---

##### Dataset 2 — DOI: 10.1016/j.jct.2018.02.022

**Source block:** PROPblock_21 · Pressure: 92.3 kPa · 25 data points at 298.15 K · Method: Concentric cylinders viscometry  
Composition expressed as **mole fraction of ethanol**.

**WM_Q#1_Table#2_(Main_Q#1_Answer):**

| *row_id* | *x(ethanol)* | *x(water)* | *η (Pa·s)* |
|---|---|---|---|
| WM_Q#1_Table#2_Row#1 | 「0 (pure water)」 | 「1」 | 「0.00089689」 |
| WM_Q#1_Table#2_Row#2 | 「0.0201」 | 「~0.98」 | 「0.001098」 |
| WM_Q#1_Table#2_Row#3 | 「0.1004」 | 「~0.90」 | 「0.0019469」 |
| WM_Q#1_Table#2_Row#4 | 「0.1499」 | 「~0.85」 | 「0.0022424」 |
| WM_Q#1_Table#2_Row#5 | 「0.1984」 | 「~0.80」 | 「0.0023706」 |
| WM_Q#1_Table#2_Row#6 | 「0.2499」 | 「~0.75」 | 「**0.0024286** (maximum)」 |
| WM_Q#1_Table#2_Row#7 | 「0.3499」 | 「~0.65」 | 「0.0022633」 |
| WM_Q#1_Table#2_Row#8 | 「0.3990」 | 「~0.60」 | 「0.0021697」 |
| WM_Q#1_Table#2_Row#9 | 「**0.4989**」 | 「**~0.50**」 | 「**0.0019557**」 |
| WM_Q#1_Table#2_Row#10 | 「0.5495」 | 「~0.45」 | 「0.0018796」 |
| WM_Q#1_Table#2_Row#11 | 「0.6067」 | 「~0.39」 | 「0.0017439」 |
| WM_Q#1_Table#2_Row#12 | 「0.6956」 | 「~0.30」 | 「0.0015722」 |
| WM_Q#1_Table#2_Row#13 | 「0.8475」 | 「~0.15」 | 「0.0013415」 |
| WM_Q#1_Table#2_Row#14 | 「1 (pure ethanol)」 | 「0」 | 「0.0010914」 |

---

##### Pure Component Viscosities at 298.15 K

**WM_Q#1_Table#3_(Main_Q#1_Answer):**

| *row_id* | *Component* | *Dataset 1 (η, Pa·s)* | *Dataset 2 (η, Pa·s)* |
|---|---|---|---|
| WM_Q#1_Table#3_Row#1 | 「Water」 | 「0.000890」 | 「0.00089689」 |
| WM_Q#1_Table#3_Row#2 | 「Ethanol」 | 「0.001082」 | 「0.0010914」 |

The two datasets agree closely: η(water) ≈ 0.00089–0.00090 Pa·s and η(ethanol) ≈ 0.00108–0.00109 Pa·s.

---

##### Near-Equimolar Composition (x ≈ 0.5)

- **Dataset 2** provides a direct measurement at x(ethanol) = 0.4989 (essentially equimolar): **η = 0.0019557 Pa·s**.
- **Dataset 1** has its nearest point at x(water) = 0.5989 (x(ethanol) ≈ 0.40): η = 0.002115 Pa·s — slightly off equimolar but consistent with the trend.

At equimolar composition, the mixture viscosity (~0.00196 Pa·s) is roughly **double** that of either pure component (~0.001 Pa·s), demonstrating a very large positive deviation from ideal mixing.

---

##### Deviation from Ideal Mixing — Analysis

For a simple linear (mole-fraction-weighted) ideal mixing rule:

> η_ideal(x = 0.5) ≈ 0.5 × 0.00109 + 0.5 × 0.00090 ≈ 0.00100 Pa·s

The measured value at x(ethanol) ≈ 0.50 is **0.0019557 Pa·s** — nearly **twice** the ideal estimate. The excess viscosity (η_mix − η_ideal) at this composition is approximately +0.00096 Pa·s.

Even more striking, the **viscosity maximum** does not occur at equimolar composition but is shifted strongly toward the water-rich side:

- Dataset 1: maximum η = 0.002300 Pa·s at x(water) ≈ 0.80 (x(ethanol) ≈ 0.20)
- Dataset 2: maximum η = 0.0024286 Pa·s at x(ethanol) ≈ 0.25 (x(water) ≈ 0.75)

The peak viscosity exceeds the ideal value by more than a **factor of 2.4**. This large positive excess viscosity is a hallmark of the ethanol–water system and is attributed to:

1. **Extensive hydrogen-bond network reorganization** — water's tetrahedral H-bond network is disrupted and reformed around ethanol's hydrophobic methyl/methylene groups.
2. **Microheterogeneity** — at water-rich compositions, ethanol molecules cluster into transient aggregates surrounded by structured water shells, increasing internal friction.
3. **Asymmetric maximum** — the shift of the viscosity peak toward x(water) ≈ 0.75–0.80 reflects the stoichiometry of the most stable ethanol–water hydrogen-bonded complexes (roughly 1 ethanol : 3 water molecules).

**Core claims:**
- Two ThermoML datasets (DOI: 10.1016/j.jct.2007.05.004 and DOI: 10.1016/j.jct.2018.02.022) provide dynamic viscosity data for ethanol + water binary mixtures at 298.15 K, with 12 and 25 data points respectively.
- Pure-component viscosities at 298.15 K agree closely between the two datasets: η(water) ≈ 0.00089–0.00090 Pa·s and η(ethanol) ≈ 0.00108–0.00109 Pa·s.
- At near-equimolar composition (x(ethanol) = 0.4989), Dataset 2 reports η = 0.0019557 Pa·s, which is approximately twice the value of either pure component (~0.001 Pa·s), demonstrating a large positive deviation from ideal mixing.
- The viscosity maximum does not occur at equimolar composition but is shifted toward the water-rich side: Dataset 1 reports a maximum of 0.002300 Pa·s at x(water) ≈ 0.80, and Dataset 2 reports a maximum of 0.0024286 Pa·s at x(ethanol) ≈ 0.25 (x(water) ≈ 0.75).
- The large positive excess viscosity is attributed to extensive hydrogen-bond network reorganization, microheterogeneity with transient ethanol aggregates in structured water shells, and the stoichiometry of the most stable ethanol–water hydrogen-bonded complexes (roughly 1 ethanol : 3 water molecules).

**Sources:**

**WM_Q#1_Table#4_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#4_Row#1 | 「GLOBlit_2825」 | 「PROPblock_11」 | 「10.1016/j.jct.2007.05.004」 | 「—」 | 「Provides dynamic viscosity of ethanol + water binary mixtures across the full mole-fraction range at 298.15 K (block spans 293.15–303.15 K), measured by capillary tube viscometry at 101.0 kPa. The answer quotes 12 data points from this block including pure-component values and the viscosity maximum near x(water) ≈ 0.80.」 |
| WM_Q#1_Table#4_Row#2 | 「GLOBlit_5201」 | 「PROPblock_21」 | 「10.1016/j.jct.2018.02.022」 | 「—」 | 「Provides dynamic viscosity of ethanol + water binary mixtures across the full mole-fraction range at 298.15 K (block spans 293.15–308.15 K), measured by concentric cylinders viscometry at 92.3 kPa. The answer quotes 14 data points from this block including the near-equimolar measurement at x(ethanol) = 0.4989 and the viscosity maximum near x(ethanol) ≈ 0.25.」 |

*Not stored here: 3 verbatim data_inspections table(s); 3 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### methanol_water_viscosity
**methanol_water_viscosity** — confidence: high · validation: PASS

**Answer:**

#### Dynamic Viscosity of Methanol + Water Binary Mixtures at 298.15 K

##### Primary Dataset

The most comprehensive dataset comes from **DOI: 10.1016/j.jct.2007.05.004** (PROPblock_9), which reports dynamic viscosity (η) for the methanol + water binary system across the full composition range at 298.15 K and 101.0 kPa. Twelve data points are available:

**WM_Q#2_Table#1_(Main_Q#2_Answer):**

| *row_id* | *Mole fraction of water (x_water)* | *Mole fraction of methanol (x_MeOH)* | *η (Pa·s)* | *η (mPa·s)* |
|---|---|---|---|---|
| WM_Q#2_Table#1_Row#1 | 「0 (pure methanol)」 | 「1.0」 | 「0.000545」 | 「0.545」 |
| WM_Q#2_Table#1_Row#2 | 「0.049」 | 「0.951」 | 「0.000607」 | 「0.607」 |
| WM_Q#2_Table#1_Row#3 | 「0.0993」 | 「0.9007」 | 「0.000677」 | 「0.677」 |
| WM_Q#2_Table#1_Row#4 | 「0.1973」 | 「0.8027」 | 「0.000821」 | 「0.821」 |
| WM_Q#2_Table#1_Row#5 | 「0.2983」 | 「0.7017」 | 「0.000987」 | 「0.987」 |
| WM_Q#2_Table#1_Row#6 | 「0.3985」 | 「0.6015」 | 「0.00115」 | 「1.150」 |
| WM_Q#2_Table#1_Row#7 | 「0.5994」 | 「0.4006」 | 「0.001463」 | 「1.463」 |
| WM_Q#2_Table#1_Row#8 | 「0.6997」 | 「0.3003」 | 「0.001554」 | 「1.554」 |
| WM_Q#2_Table#1_Row#9 | 「0.7986」 | 「0.2014」 | 「0.001542」 | 「1.542」 |
| WM_Q#2_Table#1_Row#10 | 「0.8999」 | 「0.1001」 | 「0.001317」 | 「1.317」 |
| WM_Q#2_Table#1_Row#11 | 「0.9512」 | 「0.0488」 | 「0.001121」 | 「1.121」 |
| WM_Q#2_Table#1_Row#12 | 「1.0 (pure water)」 | 「0」 | 「0.00089」 | 「0.890」 |

##### Pure Component Viscosities
- **Pure methanol:** η = 0.000545 Pa·s (0.545 mPa·s)
- **Pure water:** η = 0.00089 Pa·s (0.890 mPa·s)

##### Near-Equimolar Composition (x_methanol ≈ 0.5)

The dataset does not contain an exact equimolar point, but the two closest compositions bracket x_methanol = 0.5:

- **x_methanol = 0.6015** (x_water = 0.3985): η = 0.00115 Pa·s (1.150 mPa·s)
- **x_methanol = 0.4006** (x_water = 0.5994): η = 0.001463 Pa·s (1.463 mPa·s)

Both values are already substantially above either pure component, confirming strong non-ideal mixing behavior in this composition region.

##### Deviation from Ideal Mixing

The methanol–water system exhibits a **pronounced positive deviation** from linear (ideal) mixing of viscosity:

- The viscosity maximum is **0.001554 Pa·s** (1.554 mPa·s), occurring near x_water ≈ 0.70 (x_methanol ≈ 0.30).
- This maximum is approximately **2.9× the pure methanol viscosity** (0.001554 / 0.000545) and **1.7× the pure water viscosity** (0.001554 / 0.00089).
- A simple linear mixing rule at equimolar composition would predict roughly (0.000545 + 0.00089)/2 ≈ 0.000718 Pa·s, whereas the measured values near x_methanol = 0.5 are 0.00115–0.001463 Pa·s — about 1.6–2.0× the linear estimate.

**Physical origin:** This behavior is attributed to the enhancement of the hydrogen-bonding network when methanol and water are mixed. At intermediate compositions, methanol molecules integrate into the water H-bond network, forming larger, more structured clusters that increase the resistance to flow. The viscosity maximum near x_water ≈ 0.70 corresponds to compositions where these cooperative H-bonding interactions are strongest.

##### Supplementary Datasets

Two additional datasets provide complementary viscosity values in the methanol-dilute (water-rich) region at 298.15 K and 101.0 kPa:

**DOI: 10.1021/je0600810** (PROPblock_3) — reported vs. volume fraction of methanol:

**WM_Q#2_Table#2_(Main_Q#2_Answer):**

| *row_id* | *Volume fraction of methanol (φ_v)* | *η (Pa·s)* |
|---|---|---|
| WM_Q#2_Table#2_Row#1 | 「0.01」 | 「0.0010844」 |
| WM_Q#2_Table#2_Row#2 | 「0.20」 | 「0.0013106」 |
| WM_Q#2_Table#2_Row#3 | 「0.30」 | 「0.0014712」 |

**DOI: 10.1021/je2003622** (PROPblock_1) — reported vs. mass fraction of methanol:

**WM_Q#2_Table#3_(Main_Q#2_Answer):**

| *row_id* | *Mass fraction of methanol (w)* | *η (Pa·s)* |
|---|---|---|
| WM_Q#2_Table#3_Row#1 | 「0.0806」 | 「0.0010844」 |
| WM_Q#2_Table#3_Row#2 | 「0.1647」 | 「0.0013106」 |
| WM_Q#2_Table#3_Row#3 | 「0.2526」 | 「0.0014712」 |
| WM_Q#2_Table#3_Row#4 | 「0.3446」 | 「0.0014475」 |

These supplementary sets are consistent with the primary dataset and confirm the steep rise in viscosity as methanol is added to water, with values already approaching the maximum near w_methanol ≈ 0.25–0.35.

**Core claims:**
- At 298.15 K and 101.0 kPa, the dynamic viscosity of methanol + water binary mixtures exhibits a pronounced positive deviation from linear (ideal) mixing, with a viscosity maximum of 0.001554 Pa·s (1.554 mPa·s) occurring near x_water ≈ 0.70 (x_methanol ≈ 0.30).
- Pure component viscosities at 298.15 K are 0.000545 Pa·s (0.545 mPa·s) for methanol and 0.00089 Pa·s (0.890 mPa·s) for water.
- Near equimolar composition, measured viscosities (0.00115 Pa·s at x_methanol = 0.6015 and 0.001463 Pa·s at x_methanol = 0.4006) substantially exceed a simple linear mixing estimate of approximately 0.000718 Pa·s.
- The positive viscosity deviation is attributed to enhancement of the hydrogen-bonding network at intermediate compositions, where methanol molecules integrate into the water H-bond structure forming larger, more structured clusters.
- The primary dataset (DOI: 10.1016/j.jct.2007.05.004) covers twelve compositions spanning the full mole-fraction range; supplementary datasets (DOI: 10.1021/je0600810 and DOI: 10.1021/je2003622) confirm the steep viscosity rise in the water-rich region and are consistent with the primary data.

**Sources:**

**WM_Q#2_Table#4_(Main_Q#2_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#2_Table#4_Row#1 | 「GLOBlit_2825」 | 「PROPblock_9」 | 「10.1016/j.jct.2007.05.004」 | 「—」 | 「This block is the primary dataset providing dynamic viscosity of methanol + water across the full mole fraction range (0.0–1.0) at temperatures spanning 293.15–303.15 K (including 298.15 K) and 101.0 kPa. The answer's 12-point table with viscosities from 0.000545 to 0.001554 Pa·s falls within the block's reported range of 0.000508–0.001793 Pa·s, and the 39 datapoints accommodate three temperatures times ~13 compositions.」 |
| WM_Q#2_Table#4_Row#2 | 「GLOBlit_8869」 | 「PROPblock_3」 | 「10.1021/je0600810」 | 「—」 | 「This block provides supplementary viscosity data for methanol + water in the methanol-dilute region (volume fraction 0.01–0.30) at temperatures including 298.15 K and 101.0 kPa. The answer cites three viscosity values from this block (0.0010844, 0.0013106, 0.001471 Pa·s) that fall within the block's reported range of 0.000702–0.001471 Pa·s.」 |
| WM_Q#2_Table#4_Row#3 | 「GLOBlit_9571」 | 「PROPblock_1」 | 「10.1021/je2003622」 | 「—」 | 「This block provides supplementary viscosity data for methanol + water reported versus mass fraction (0.0806–0.3446) at temperatures including 298.15 K and 101.0 kPa. The answer cites four viscosity values from this block that fall within its reported range of 0.000638–0.001471 Pa·s, confirming the steep viscosity rise and approach to the maximum near w_methanol ≈ 0.25–0.35.」 |

*Not stored here: 3 verbatim data_inspections table(s); 2 id_catalog_snapshot row(s) (catalog is merged separately). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

