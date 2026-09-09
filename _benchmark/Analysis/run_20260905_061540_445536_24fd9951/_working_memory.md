# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_061540_445536_24fd9951`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_24 | 1,2-ethanediol | 0.016223 |
| comp | GLOBcomp_1 | water |  |
| prop | GLOBprop_4 | viscosity, pas |  |

### History
- [query_thermoml_parallel]
- [fit_multi_system]
- [fit_multi_system]
- [fit_block] ERROR: Constraint column 'Temperature, K' not found in block
- [fit_block]

### Query Results
#### EG_water_viscosity
**L1_query_1** — status: success · validation: FLAGGED(4)

**Summary:** Seven ThermoML blocks (all match score 100) were found for dynamic viscosity (GLOBprop_4) of binary ethylene glycol (GLOBcomp_24, OCCO) + water (GLOBcomp_1) in the 290–310 K range. Two blocks were inspected in detail. GLOBlit_2656 PROPblock_13 contains 10 data points at 293.15 K and 101.325 kPa, with viscosity spanning 0.001008–0.013999 Pa·s over mass fractions 0–0.9 of ethylene glycol. GLOBlit_5201 PROPblock_24 is the largest inspected dataset (84 data points, 293.15–308.15 K, 92.3 kPa) covering mole fractions 0–1 and including measurements at exactly 298.15 K; representative 298.15 K values are 0.00089689 Pa·s for pure water, 0.0028109 Pa·s at mole fraction 0.2072, 0.0060624 Pa·s at 0.4446, and 0.016223 Pa·s for pure ethylene glycol. Additional uninspected blocks from GLOBlit_8038, GLOBlit_6951, and GLOBlit_11506 also bracket or include 298.15 K. The data show a strongly non-linear, monotonic increase in viscosity with ethylene glycol content, consistent with extensive hydrogen-bonding interactions between the two components.

**Answer:**

#### Binary Mixture Viscosity Data: Ethylene Glycol + Water near 25 °C (298.15 K)

**Compounds resolved:**
- Ethylene glycol (1,2-ethanediol): **GLOBcomp_24** (C₂H₆O₂, SMILES: OCCO)
- Water: **GLOBcomp_1** (H₂O)

**Property:** Dynamic viscosity (**GLOBprop_4**)

A search for binary ethylene glycol + water viscosity blocks in the temperature range 290–310 K returned **7 blocks**, all with a match score of 100. Five of the seven cover or bracket 298.15 K. Key candidates are summarized below:

##### Inspected Blocks

**1. GLOBlit_2656 — PROPblock_13**
- DOI: 10.1016/j.jct.2006.01.011
- 10 data points at fixed T = 293.15 K, P = 101.325 kPa
- Composition variable: mass fraction of 1,2-ethanediol (0 to 0.9)
- Viscosity range: 0.001008–0.013999 Pa·s
- Note: Single temperature (293.15 K), about 5 K below the search target of 298.15 K.

Representative data at 293.15 K:

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *mass_fraction (EG)* | *viscosity (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0」 | 「0.001008」 |
| WM_L1#1_Table#1_Row#2 | 「0.3」 | 「0.002177」 |
| WM_L1#1_Table#1_Row#3 | 「0.5」 | 「0.003558」 |
| WM_L1#1_Table#1_Row#4 | 「0.7」 | 「0.00636」 |
| WM_L1#1_Table#1_Row#5 | 「0.9」 | 「0.013999」 |

**2. GLOBlit_5201 — PROPblock_24**
- DOI: 10.1016/j.jct.2018.02.022
- 84 data points, T range: 293.15–308.15 K, P = 92.3 kPa (fixed)
- Composition variable: mole fraction of 1,2-ethanediol (0 to 1)
- Viscosity range: 0.00075887–0.020613 Pa·s
- Note: Largest dataset; includes measurements at exactly 298.15 K.

Representative data at 298.15 K from this block:

**WM_L1#1_Table#2_(Analysis_L1#1_Answer):**

| *row_id* | *mole_fraction (EG)* | *viscosity (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0」 | 「0.00089689」 |
| WM_L1#1_Table#2_Row#2 | 「0.2072」 | 「0.0028109」 |
| WM_L1#1_Table#2_Row#3 | 「0.4446」 | 「0.0060624」 |
| WM_L1#1_Table#2_Row#4 | 「1」 | 「0.016223」 |

##### Additional Blocks (not inspected; data point counts below are from the search_blocks summary, not from block inspections)

**WM_L1#1_Table#3_(Analysis_L1#1_Answer):**

| *row_id* | *GLOBlit* | *Data Points (from search summary)* | *Notes* |
|---|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「GLOBlit_8038」 | 「77 (search summary)」 | 「Brackets 298.15 K」 |
| WM_L1#1_Table#3_Row#2 | 「GLOBlit_6951」 | 「33 (search summary)」 | 「Brackets 298.15 K」 |
| WM_L1#1_Table#3_Row#3 | 「GLOBlit_11506」 | 「16」 | 「Includes T = 298.15 K exactly」 |

Two further blocks were also returned by the search but their detailed metadata was truncated in the tool output.

**Chemistry insight:** The inspected data clearly show the strongly non-linear, monotonically increasing viscosity with ethylene glycol content. In PROPblock_13, viscosity rises roughly 14-fold from pure water (0.001008 Pa·s) to 90 wt% EG (0.013999 Pa·s) at 293.15 K. In PROPblock_24 at 298.15 K, pure EG viscosity (0.016223 Pa·s) is approximately 18 times that of pure water (0.00089689 Pa·s) (ratio computed from the two inspected values). This behavior reflects the extensive hydrogen-bonding network formed between ethylene glycol and water molecules, which reaches maximum cooperativity at intermediate compositions.

**Core claims:**
- Seven ThermoML blocks were found for binary ethylene glycol + water dynamic viscosity near 298.15 K, with five covering or bracketing that temperature.
- At 293.15 K and 101.325 kPa (GLOBlit_2656, PROPblock_13), viscosity increases monotonically from 0.001008 Pa·s at 0 mass fraction ethylene glycol to 0.013999 Pa·s at 0.9 mass fraction ethylene glycol.
- At 298.15 K and 92.3 kPa (GLOBlit_5201, PROPblock_24), viscosity increases from 0.00089689 Pa·s for pure water to 0.016223 Pa·s for pure ethylene glycol, with intermediate values of 0.0028109 Pa·s at mole fraction 0.2072 and 0.0060624 Pa·s at mole fraction 0.4446.
- The viscosity increase with ethylene glycol content is strongly non-linear and monotonic, consistent with extensive hydrogen-bonding interactions between ethylene glycol and water.
- Several additional blocks (GLOBlit_8038, GLOBlit_6951, GLOBlit_11506) were identified but not inspected in detail, so their data remain unverified.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_2656」 | 「PROPblock_13」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethylene glycol + water at 293.15 K, 10 data points, mass fraction composition variable.」 |
| WM_L1#1_Table#5 | 「GLOBlit_5201」 | 「PROPblock_24」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethylene glycol + water, 84 data points, T range 293.15–308.15 K, mole fraction composition variable. Includes measurements at exactly 298.15 K.」 |

*Not stored here: 2 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(4) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **MISATTRIBUTED_VALUE** PROPblock_13: 298.15 does not belong to PROPblock_13; it matches only GLOBlit_5201::PROPblock_24 (inspected this run)
- **UNGROUNDED_LITERAL** PROPblock_24: 77 (near '…Points (from search summary) | Notes | |---|---|---| |   | 7…') matches no inspected row/stat, database table, or other source of PROPblock_24
- **UNGROUNDED_LITERAL** PROPblock_24: 33 (near '…|---| |   | 77 (search summary) | Brackets 298.15 K | |   | …') matches no inspected row/stat, database table, or other source of PROPblock_24
- **UNINSPECTED_VALUE** PROPblock_24: 18 exists in PROPblock_24's database table but was never shown in an inspection of this run


#### EG_methanol_viscosity
**L1_query_2** — status: success · validation: PASS

**Summary:** One ThermoML data block (DOI 10.1016/j.fluid.2009.03.002, GLOBlit_692, PROPblock_1) reports dynamic viscosity (Pa·s) for the binary liquid system 1,2-ethanediol (ethylene glycol) + methanol, measured by capillary tube (Ostwald–Ubbelohde) at 101.0 kPa over 293.15–303.15 K and mass fractions of 1,2-ethanediol from 0.0 to 0.75, totaling 12 data points. At 298.15 K the four reported viscosities are: w = 0.0, η = 0.0005436 Pa·s; w = 0.25, η = 0.0010295 Pa·s; w = 0.50, η = 0.0020452 Pa·s; w = 0.75, η = 0.004904 Pa·s. Viscosity increases strongly and nonlinearly with ethylene glycol content (roughly 9× from w = 0.0 to w = 0.75 at 298.15 K), reflecting the extensive hydrogen-bonding network of the diol. At each composition, viscosity decreases with increasing temperature, consistent with Arrhenius-type behavior.

**Answer:**

#### Binary Mixture Viscosity Data: Ethylene Glycol + Methanol near 25 °C

**One data block was found** in the ThermoML database containing dynamic viscosity measurements for the binary system 1,2-ethanediol (ethylene glycol) + methanol near 298.15 K.

##### Block Summary

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *Field* | *Value* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「**DOI**」 | 「10.1016/j.fluid.2009.03.002」 |
| WM_L1#2_Table#1_Row#2 | 「**Literature ID**」 | 「GLOBlit_692」 |
| WM_L1#2_Table#1_Row#3 | 「**Block**」 | 「PROPblock_1」 |
| WM_L1#2_Table#1_Row#4 | 「**Property**」 | 「Dynamic viscosity (GLOBprop_4), Pa·s」 |
| WM_L1#2_Table#1_Row#5 | 「**Method**」 | 「Capillary tube (Ostwald–Ubbelohde)」 |
| WM_L1#2_Table#1_Row#6 | 「**Phase**」 | 「Liquid」 |
| WM_L1#2_Table#1_Row#7 | 「**System**」 | 「Binary (1,2-ethanediol + methanol)」 |
| WM_L1#2_Table#1_Row#8 | 「**Temperature range**」 | 「293.15–303.15 K」 |
| WM_L1#2_Table#1_Row#9 | 「**Pressure**」 | 「101.0 kPa (fixed constraint)」 |
| WM_L1#2_Table#1_Row#10 | 「**Total data points**」 | 「12」 |
| WM_L1#2_Table#1_Row#11 | 「**Composition variable**」 | 「Mass fraction of 1,2-ethanediol (0.0–0.75)」 |

##### Data at 298.15 K (4 data points)

**WM_L1#2_Table#2_(Analysis_L1#2_Answer):**

| *row_id* | *w(1,2-ethanediol)* | *T (K)* | *η (Pa·s)* |
|---|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「0.0」 | 「298.15」 | 「0.0005436」 |
| WM_L1#2_Table#2_Row#2 | 「0.25」 | 「298.15」 | 「0.0010295」 |
| WM_L1#2_Table#2_Row#3 | 「0.50」 | 「298.15」 | 「0.0020452」 |
| WM_L1#2_Table#2_Row#4 | 「0.75」 | 「298.15」 | 「0.004904」 |

##### Full Data (all 12 points, all temperatures)

**WM_L1#2_Table#3_(Analysis_L1#2_Answer):**

| *row_id* | *w(1,2-ethanediol)* | *T (K)* | *P (kPa)* | *η (Pa·s)* |
|---|---|---|---|---|
| WM_L1#2_Table#3_Row#1 | 「0.0」 | 「293.15」 | 「101.0」 | 「0.0005814」 |
| WM_L1#2_Table#3_Row#2 | 「0.0」 | 「298.15」 | 「101.0」 | 「0.0005436」 |
| WM_L1#2_Table#3_Row#3 | 「0.0」 | 「303.15」 | 「101.0」 | 「0.0005112」 |
| WM_L1#2_Table#3_Row#4 | 「0.25」 | 「293.15」 | 「101.0」 | 「0.0011268」 |
| WM_L1#2_Table#3_Row#5 | 「0.25」 | 「298.15」 | 「101.0」 | 「0.0010295」 |
| WM_L1#2_Table#3_Row#6 | 「0.25」 | 「303.15」 | 「101.0」 | 「0.0009454」 |
| WM_L1#2_Table#3_Row#7 | 「0.50」 | 「293.15」 | 「101.0」 | 「0.0022692」 |
| WM_L1#2_Table#3_Row#8 | 「0.50」 | 「298.15」 | 「101.0」 | 「0.0020452」 |
| WM_L1#2_Table#3_Row#9 | 「0.50」 | 「303.15」 | 「101.0」 | 「0.0018101」 |
| WM_L1#2_Table#3_Row#10 | 「0.75」 | 「293.15」 | 「101.0」 | 「0.0057998」 |
| WM_L1#2_Table#3_Row#11 | 「0.75」 | 「298.15」 | 「101.0」 | 「0.004904」 |
| WM_L1#2_Table#3_Row#12 | 「0.75」 | 「303.15」 | 「101.0」 | 「0.0042319」 |

**Chemistry insight:** The viscosity increases strongly and nonlinearly with ethylene glycol mass fraction — at 298.15 K, the viscosity at w = 0.75 (0.004904 Pa·s) is about 9× that at w = 0.0 (0.0005436 Pa·s), reflecting the extensive hydrogen-bonding network of ethylene glycol (a diol) progressively dominating the mixture's flow resistance. The pure methanol value (0.0005436 Pa·s ≈ 0.54 mPa·s) is consistent with its known low viscosity as a small, mono-hydroxyl solvent. At each composition, viscosity decreases with increasing temperature (e.g., at w = 0.75: 0.0057998 Pa·s at 293.15 K → 0.004904 Pa·s at 298.15 K → 0.0042319 Pa·s at 303.15 K), as expected from the Arrhenius-type temperature dependence of liquid viscosity.

**Core claims:**
- One ThermoML data block (DOI 10.1016/j.fluid.2009.03.002) reports dynamic viscosity for the binary liquid system 1,2-ethanediol + methanol at 101.0 kPa, covering temperatures 293.15–303.15 K and 1,2-ethanediol mass fractions 0.0–0.75, totaling 12 data points measured by capillary tube (Ostwald–Ubbelohde) method.
- At 298.15 K, the dynamic viscosity increases strongly and nonlinearly with ethylene glycol mass fraction, from 0.0005436 Pa·s at w = 0.0 to 0.004904 Pa·s at w = 0.75, reflecting the extensive hydrogen-bonding network of the diol progressively dominating flow resistance.
- At each composition, viscosity decreases with increasing temperature over the 293.15–303.15 K range, consistent with Arrhenius-type temperature dependence of liquid viscosity.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#4 | 「GLOBlit_692」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_24」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for the binary mixture 1,2-ethanediol + methanol at 293.15–303.15 K and 101.0 kPa, 12 data points, mass fraction of 1,2-ethanediol 0.0–0.75.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### water_methanol_viscosity
**L1_query_3** — status: success · validation: PASS

**Summary:** A ThermoML search for dynamic viscosity (GLOBprop_4) of binary water (GLOBcomp_1) + methanol (GLOBcomp_4) in the 293–303 K range returned 4 data blocks. The most comprehensive is PROPblock_9 from GLOBlit_2825 (DOI: 10.1016/j.jct.2007.05.004), containing 39 data points spanning the full composition range (mole fraction of water 0–1) at 293.15, 298.15, and 303.15 K, all at 101.0 kPa, with viscosity values from 0.000508 to 0.001793 Pa·s. At 298.15 K, representative values include 0.000545 Pa·s for pure methanol, 0.001554 Pa·s near x(water) ≈ 0.70 (the viscosity maximum), and 0.00089 Pa·s for pure water, illustrating the well-known non-ideal viscosity maximum attributed to hydrogen-bonding interactions. Three additional blocks provide supplementary viscosity data at 293.15 or 298.15 K with partial composition coverage.

**Answer:**

#### Binary Water + Methanol Dynamic Viscosity Data Near 298.15 K

A search of the ThermoML database for dynamic viscosity (GLOBprop_4) measurements in binary water (GLOBcomp_1) + methanol (GLOBcomp_4) systems in the temperature range 293–303 K returned **4 data blocks**.

##### Primary Dataset

**WM_L1#3_Table#1_(Analysis_L1#3_Answer):**

| *row_id* | *DOI* | *Block* | *Literature ID* | *Data Points* | *T Range (K)* | *Composition Variable* | *Composition Range* |
|---|---|---|---|---|---|---|---|
| WM_L1#3_Table#1_Row#1 | 「10.1016/j.jct.2007.05.004」 | 「PROPblock_9」 | 「GLOBlit_2825」 | 「39」 | 「293.15–303.15」 | 「x(water)」 | 「0–1」 |

The most comprehensive dataset is **PROPblock_9** from GLOBlit_2825 (DOI: 10.1016/j.jct.2007.05.004), which contains 39 data points spanning the full composition range (mole fraction of water from 0 to 1) at three temperatures: 293.15, 298.15, and 303.15 K, all at a fixed pressure constraint of 101.0 kPa. The viscosity values range from 0.000508 to 0.001793 Pa·s across the block.

###### Representative inspected data at 298.15 K

**WM_L1#3_Table#2_(Analysis_L1#3_Answer):**

| *row_id* | *Mole fraction water* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#3_Table#2_Row#1 | 「0」 | 「0.000545」 |
| WM_L1#3_Table#2_Row#2 | 「0.5994」 | 「0.001463」 |
| WM_L1#3_Table#2_Row#3 | 「0.6997」 | 「0.001554」 |
| WM_L1#3_Table#2_Row#4 | 「0.7986」 | 「0.001542」 |
| WM_L1#3_Table#2_Row#5 | 「0.8999」 | 「0.001317」 |
| WM_L1#3_Table#2_Row#6 | 「1」 | 「0.00089」 |

The data clearly show the well-known viscosity maximum in water–methanol mixtures: at 298.15 K, the viscosity peaks near x(water) ≈ 0.70 (0.001554 Pa·s), substantially exceeding the viscosity of either pure methanol (0.000545 Pa·s) or pure water (0.00089 Pa·s). This non-ideal behavior reflects strong hydrogen-bonding interactions and structural reorganization in the mixture.

Three additional blocks were also identified in this temperature window, providing supplementary viscosity data at 293.15 or 298.15 K with partial composition coverage.

**Core claims:**
- The ThermoML database contains a comprehensive dataset (PROPblock_9, GLOBlit_2825, DOI 10.1016/j.jct.2007.05.004) of 39 dynamic viscosity data points for binary water + methanol mixtures spanning the full composition range (mole fraction of water 0–1) at 293.15, 298.15, and 303.15 K and 101.0 kPa, with viscosity values ranging from 0.000508 to 0.001793 Pa·s.
- At 298.15 K, the data show a viscosity maximum near x(water) ≈ 0.70 (0.001554 Pa·s), substantially exceeding the viscosities of both pure methanol (0.000545 Pa·s) and pure water (0.00089 Pa·s), consistent with well-known non-ideal behavior attributed to strong hydrogen-bonding interactions and structural reorganization in the mixture.

**Core blocks found:**

**WM_L1#3_Blocks_(Analysis_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#3 | 「GLOBlit_2825」 | 「PROPblock_9」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for water + methanol binary mixture at 293.15–303.15 K, 101.0 kPa, full composition range, 39 data points.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Completed Fits
  - EG_water [10.1016/j.jct.2018.02.022/PROPblock_24] (1,2-ethanediol, water): RK order=3, R²=0.99994, RMSE=0.0013198945265291695, coeffs=[2.39674, -1.044444, 0.668173, -0.3209]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: 1,2-ethanediol=0.016223, water=0.00089689 [block-edges (water: direct/good, 1,2-ethanediol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png
  - water_methanol [10.1016/j.jct.2007.05.004/PROPblock_9] (water, methanol): RK order=3, R²=0.999903, RMSE=0.0020496812938951637, coeffs=[2.534774, 1.422136, 1.33593, 0.754488]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: water=0.00089, methanol=0.000545 [block-edges (methanol: direct/good, water: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_excess.png
  - 10.1016/j.fluid.2009.03.002/PROPblock_1 (1,2-ethanediol, methanol): RK order=0, R²=-4.94932, RMSE=0.03559043525961839, coeffs=[0.714727]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      ⚠ Composition axis converted to mole fraction of 1,2-ethanediol: mass_fraction → mole_fraction via x1=(w1/M1)/(w1/M1+w2/M2), M1=62.068, M2=32.042 g/mol [exact (molar masses from block formulas)]. Source column: mass_fraction_<1,2-ethanediol>.
      pure refs: 1,2-ethanediol=0.016223, methanol=0.0005436 [named (matched to composition axis)]
      fit_csv: $ROOT/data\10_1016_j_fluid_2009_03_002_BPROPblock_1_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_fluid_2009_03_002_BPROPblock_1_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_fluid_2009_03_002_BPROPblock_1_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_fluid_2009_03_002_BPROPblock_1_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- `$ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2007.05.004 PROPblock_9_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- `$ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2007.05.004 PROPblock_9_T298.1
- `$ROOT/data\10_1016_j_fluid_2009_03_002_BPROPblock_1_T298.1_fit.csv` — RK fit data — 10.1016/j.fluid.2009.03.002 PROPblock_1_T298.1
- `$ROOT/data\10_1016_j_fluid_2009_03_002_BPROPblock_1_T298.1_excess.csv` — Excess property — 10.1016/j.fluid.2009.03.002 PROPblock_1_T298.1

### plot
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- `$ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2007.05.004 PROPblock_9_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- `$ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2007.05.004 PROPblock_9_T298.1
- `$ROOT/plots\10_1016_j_fluid_2009_03_002_BPROPblock_1_T298.1_fit.png` — RK fit plot — 10.1016/j.fluid.2009.03.002 PROPblock_1_T298.1
- `$ROOT/plots\10_1016_j_fluid_2009_03_002_BPROPblock_1_T298.1_excess.png` — Excess plot — 10.1016/j.fluid.2009.03.002 PROPblock_1_T298.1

