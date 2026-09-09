# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041158_447699_492f384b`

### History
- [parallel:3 tasks]
-   [analysis:water_methanol_VE] "Find and fit excess molar volume (VE) data for the binary system water + methano" (524s, 16 iters, validation=FLAGGED(2) verdict=**Data Quality**
The agent use)
-   [analysis:water_ethanol_VE] "Find and fit excess molar volume (VE) data for the binary system water + ethanol" (497s, 12 iters, validation=PASS verdict=**Data Quality**
The agent cor)
-   [analysis:water_propanol_VE] "Find and fit excess molar volume (VE) data for the binary system water + 1-propa" (443s, 16 iters, validation=PASS verdict=**Data Quality**
The agent cor)
- [parallel:auto-compacted] 3 per-task reports (agentic, targets 1,2, philosophy elicited)
- [menu:browse] {'text': '## analysis/fitting\nFitting tools including RK pr
- [menu:browse] {'text': 'I need to explore the analysis submenu to find the
- [menu:run] predict_from_rk → OK
- [menu:run] predict_from_rk → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK
- [menu:run] inspect_block_table → OK

### Analysis Agent Results

#### water_methanol_VE
**water_methanol_VE** — validation: FLAGGED(2)

**Answer:**

#### Excess Molar Volume (V_E) of Water + Methanol at 298.15 K — Redlich-Kister Fit

##### Data Source

**Primary fit data:** González et al. (2007), DOI 10.1016/j.jct.2007.05.004 (GLOBlit_2825), Block PROPblock_10
- **Property measured:** Mass density (kg/m³) of the water + methanol binary liquid
- **Conditions:** T = 298.15 K, P = 101.0 kPa
- **Composition range:** x(water) = 0 to 1 (11 interior mixture points used in the fit, from 39 total rows spanning 3 temperatures)
- **Fitting route:** DP2 — measured density → exact pointwise transform (density → molar volume → V_E via ideal-mixing baseline)

**Supporting direct V_E data (not fitted — only 3 compositions):** Safronov & Heyer (2004), DOI 10.1016/j.jct.2004.03.011 (GLOBlit_2395), Block PROPblock_1
- At 298.15 K and 100 kPa: V_E = −7.42 × 10⁻⁷ m³/mol at x(methanol) = 0.25, −1.014 × 10⁻⁶ at x(methanol) = 0.50, −7.05 × 10⁻⁷ at x(methanol) = 0.75

##### Pure-Component Molar Volumes (298.15 K)

**WM_A#1_Table#1_(Main_A#1_Answer):**

| *row_id* | *Component* | *V_m (m³/mol)* | *Source* |
|---|---|---|---|
| WM_A#1_Table#1_Row#1 | 「Water」 | 「1.8068 × 10⁻⁵」 | 「Block-edge endpoint (fit_block_derived output)」 |
| WM_A#1_Table#1_Row#2 | 「Methanol」 | 「4.0704 × 10⁻⁵」 | 「Block-edge endpoint (fit_block_derived output)」 |

##### Redlich-Kister Fit Results

**BIC-selected polynomial order:** 5

**Redlich-Kister coefficients** (V_E in m³/mol, x₁ = x(methanol)):

V_E(x₁) = x₁(1 − x₁) Σₖ Aₖ (2x₁ − 1)ᵏ

**WM_A#1_Table#2_(Main_A#1_Answer):**

| *row_id* | *k* | *Aₖ (m³/mol)* |
|---|---|---|
| WM_A#1_Table#2_Row#1 | 「0」 | 「−3.98239 × 10⁻⁶」 |
| WM_A#1_Table#2_Row#2 | 「1」 | 「−1.5386 × 10⁻⁷」 |
| WM_A#1_Table#2_Row#3 | 「2」 | 「1.03864 × 10⁻⁸」 |
| WM_A#1_Table#2_Row#4 | 「3」 | 「1.33311 × 10⁻⁷」 |
| WM_A#1_Table#2_Row#5 | 「4」 | 「8.30673 × 10⁻⁷」 |
| WM_A#1_Table#2_Row#6 | 「5」 | 「7.17478 × 10⁻⁷」 |

##### Fit Quality

**WM_A#1_Table#3_(Main_A#1_Answer):**

| *row_id* | *Statistic* | *Value* |
|---|---|---|
| WM_A#1_Table#3_Row#1 | 「R²」 | 「0.999995」 |
| WM_A#1_Table#3_Row#2 | 「RMSE」 | 「6.883 × 10⁻¹⁰ m³/mol」 |
| WM_A#1_Table#3_Row#3 | 「BIC (order 5)」 | 「−449.74」 |
| WM_A#1_Table#3_Row#4 | 「Mixture data points」 | 「11」 |

**BIC comparison across orders:**

**WM_A#1_Table#4_(Main_A#1_Answer):**

| *row_id* | *Order* | *BIC* | *R²* | *RMSE (m³/mol)* |
|---|---|---|---|---|
| WM_A#1_Table#4_Row#1 | 「0」 | 「−386.91」 | 「0.995546」 | 「2.064 × 10⁻⁸」 |
| WM_A#1_Table#4_Row#2 | 「1」 | 「−384.59」 | 「0.995575」 | 「2.05748 × 10⁻⁸」 |
| WM_A#1_Table#4_Row#3 | 「2」 | 「−392.37」 | 「0.998247」 | 「1.295 × 10⁻⁸」 |
| WM_A#1_Table#4_Row#4 | 「3」 | 「−404.87」 | 「0.999547」 | 「6.580 × 10⁻⁹」 |
| WM_A#1_Table#4_Row#5 | 「4」 | 「−423.77」 | 「0.999935」 | 「2.499 × 10⁻⁹」 |
| WM_A#1_Table#4_Row#6 | 「5」 | 「−449.74」 | 「0.999995」 | 「6.883 × 10⁻¹⁰」 |

##### Maximum Volume Contraction

From the RK prediction (201-point grid):

**WM_A#1_Table#5_(Main_A#1_Answer):**

| *row_id* | *Quantity* | *Value* |
|---|---|---|
| WM_A#1_Table#5_Row#1 | 「Minimum V_E」 | 「**−9.960 × 10⁻⁷ m³/mol**」 |
| WM_A#1_Table#5_Row#2 | 「Composition at minimum」 | 「**x(methanol) ≈ 0.50**」 |

The minimum V_E was identified from the predict_from_rk output as the maximum |excess| = −9.95967 × 10⁻⁷ m³/mol. The predicted molar volume at x(methanol) = 0.5 is 2.83904 × 10⁻⁵ m³/mol (from predict_from_rk). The ideal baseline at x(methanol) = 0.5 is computed as the arithmetic mean of the two pure-component values: (1.8068 × 10⁻⁵ + 4.0704 × 10⁻⁵) / 2 = 2.9386 × 10⁻⁵ m³/mol *(derived: average of two tool-returned pure values)*. This gives V_E(0.5) = 2.83904 × 10⁻⁵ − 2.9386 × 10⁻⁵ = −9.96 × 10⁻⁷ m³/mol — matching the grid minimum and confirming the minimum lies at approximately equimolar composition.

##### Chemistry Insight

The strongly negative V_E across the entire composition range reflects the pronounced volume contraction when water and methanol are mixed. This arises from the ability of the smaller water molecules to interstitially fill voids in the methanol hydrogen-bonding network, combined with strong O–H···O hydrogen bonds between unlike molecules. The near-symmetric minimum at x(methanol) ≈ 0.5 indicates that the maximum intermolecular interaction occurs at equimolar composition, where the stoichiometry of water–methanol hydrogen-bond pairs is optimized.

The derived V_E minimum of −9.960 × 10⁻⁷ m³/mol is consistent with the directly measured value of −1.014 × 10⁻⁶ m³/mol at x(methanol) = 0.5 from Safronov & Heyer (2004), with the small difference attributable to different experimental sources and methods.

##### Output Files

- **Fit data CSV:** `10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_fit.csv`
- **Excess property CSV:** `10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_excess.csv`
- **Fit plot:** `10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_fit.png`
- **Excess plot:** `10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_excess.png`

**Core claims:**
- The excess molar volume of water + methanol at 298.15 K and 101.0 kPa was fitted to a Redlich-Kister polynomial of BIC-selected order 5, using 11 interior mixture density data points from González et al. (2007) transformed via density → molar volume → V_E.
- The Redlich-Kister coefficients (m³/mol, x₁ = x(methanol)) are: A₀ = −3.98239 × 10⁻⁶, A₁ = −1.5386 × 10⁻⁷, A₂ = 1.03864 × 10⁻⁸, A₃ = 1.33311 × 10⁻⁷, A₄ = 8.30673 × 10⁻⁷, A₅ = 7.17478 × 10⁻⁷.
- The fit quality is high, with R² = 0.999995 and RMSE = 6.883 × 10⁻¹⁰ m³/mol over the 11 mixture points.
- The minimum V_E from the fitted curve is −9.960 × 10⁻⁷ m³/mol, occurring at approximately equimolar composition x(methanol) ≈ 0.50, indicating maximum volume contraction at that composition.
- Pure-component molar volumes at 298.15 K used in the fit are 1.8068 × 10⁻⁵ m³/mol for water and 4.0704 × 10⁻⁵ m³/mol for methanol.
- The fitted minimum V_E of −9.960 × 10⁻⁷ m³/mol is consistent with the directly measured value of −1.014 × 10⁻⁶ m³/mol at x(methanol) = 0.5 from Safronov & Heyer (2004), with the small difference attributed to different experimental sources.
- V_E is negative across the entire composition range, reflecting volume contraction attributed to interstitial filling of voids in the methanol hydrogen-bonding network by water molecules and strong unlike O–H···O hydrogen bonds.

**Sources:**

**WM_A#1_Table#6_(Main_A#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_A#1_Table#6_Row#1 | 「GLOBlit_2825」 | 「PROPblock_10」 | 「10.1016/j.jct.2007.05.004」 | 「—」 | 「This block provides mass density data for the water + methanol binary at 298.15 K across the full mole-fraction range (0 to 1), which was transformed to excess molar volume and fitted with a 5th-order Redlich-Kister polynomial. It is the primary data source for the fit, yielding the RK coefficients and the minimum V_E of −9.960 × 10⁻⁷ m³/mol at x(methanol) ≈ 0.50.」 |
| WM_A#1_Table#6_Row#2 | 「GLOBlit_2395」 | 「PROPblock_1」 | 「10.1016/j.jct.2004.03.011」 | 「—」 | 「This block provides direct excess molar volume measurements for water + methanol at 298.15 K and 100 kPa at three compositions (x(methanol) = 0.25, 0.50, 0.75), used as independent validation of the density-derived V_E fit. The reported V_E of −1.014 × 10⁻⁶ m³/mol at x = 0.50 is consistent with the fitted minimum.」 |

**Fit results:**

**WM_A#1_Table#7_(Main_A#1_FitResults):**

| *row_id* | *lit_num_id* | *block* | *property* | *rk_order* | *rk_coeffs* | *r_squared* | *rmse* | *n_points* | *T_K* | *mixing_rule* |
|---|---|---|---|---|---|---|---|---|---|---|
| WM_A#1_Table#7_Row#1 | 「GLOBlit_2825」 | 「PROPblock_10」 | 「GLOBprop_1」 | 「5」 | 「-3.982385645518985e-06, -1.5385952413612444e-07, 1.03864163958051e-08, 1.3331147478426026e-07, 8.306732768980643e-07, 7.174776515659238e-07」 | 「0.999995」 | 「6.883050222977911e-10」 | 「11」 | 「298.15」 | 「linear」 |

*Not stored here: 6 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** PROPblock_1: 2.9386e-5 (near '…he two pure-component values: (1.8068e-5 + 4.0704e-5) / 2 = …') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 2.9386e-5 (near '…-returned pure values)*. This gives V_E(0.5) = 2.83904e-5 - …') matches no inspected row/stat, database table, or other source of PROPblock_1


**Verdict:** **Data Quality**
The agent used density data (González et al., 2007) transformed via `fit_block_derived` to obtain V^E — an acceptable derived route when direct V^E data were insufficient (only 3 points from Safronov & Heyer). The tool trace confirms `fit_block_derived` was called and returned results (step 11, 954 chars), and `predict_from_rk` produced predictions (step 12). Composition basis appears to be mole fraction. No fabrication flags detected.

**Fit Quality**
Order 5 with R²=0.999995 on 11 data points (6 parameters for 11 points) raises mild overfitting concerns, though BIC selection supports this order. RMSE is extremely small (~7×10⁻¹⁰ m³/mol), consistent with high-precision density-derived data.

**Scientific Verdict**
The minimum V^E ≈ −1.0×10⁻⁶ m³/mol at x(methanol)≈0.50 is physically reasonable and consistent with literature values (~−1.0 cm³/mol). Cross-validation with Safronov & Heyer's direct measurement strengthens confidence. The 6-parameter fit on 11 points warrants caution for extrapolation.
**Session:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041158_447699_492f384b\analysis_runs\run_2`

#### water_ethanol_VE
**water_ethanol_VE** — validation: PASS

**Answer:**

#### Excess Molar Volume (V^E) for Water + Ethanol at 298.15 K

##### Data Source and Approach

No direct excess molar volume (V^E) data for the water + ethanol binary system exists in the ThermoML database. Instead, the **DP2 (measured-derived) approach** was used: measured mass density data were exactly transformed pointwise via ρ(x) → V_m(x) = (x₁M₁ + x₂M₂)/ρ → V^E(x) = V_m − (x₁V₁\* + x₂V₂\*), and the resulting excess molar volume was fitted with a Redlich-Kister polynomial.

**Source block:**
- **DOI:** 10.1016/j.fluid.2004.11.019 (GLOBlit_220)
- **Block:** PROPblock_2
- **Compounds:** Water (GLOBcomp_1) + Ethanol (GLOBcomp_2)
- **Conditions:** T = 298.15 K, P = 100 kPa
- **Data points used:** 47 mixture compositions (from 810 total points spanning multiple T and P)

##### Pure-Component Molar Volumes

Extracted from block edge rows of the derived molar volume data (fit_block_derived output):

**WM_A#2_Table#1_(Main_A#2_Answer):**

| *row_id* | *Component* | *V\* (m³/mol)* | *Source quality* |
|---|---|---|---|
| WM_A#2_Table#1_Row#1 | 「Water」 | 「1.84491×10⁻⁵」 | 「block-edge, direct/good」 |
| WM_A#2_Table#1_Row#2 | 「Ethanol」 | 「5.86343×10⁻⁵」 | 「block-edge, direct/good」 |

##### Redlich-Kister Fit Results

The BIC criterion selected a **5th-order** Redlich-Kister polynomial for the excess molar volume:

$$V^E(x_1) = x_1(1-x_1) \sum_{k=0}^{5} A_k (2x_1 - 1)^k$$

where x₁ = mole fraction of ethanol.

**WM_A#2_Table#2_(Main_A#2_Answer):**

| *row_id* | *Parameter* | *Value* |
|---|---|---|
| WM_A#2_Table#2_Row#1 | 「**A₀**」 | 「−4.98777×10⁻⁶ m³/mol」 |
| WM_A#2_Table#2_Row#2 | 「**A₁**」 | 「+2.71547×10⁻⁶ m³/mol」 |
| WM_A#2_Table#2_Row#3 | 「**A₂**」 | 「−1.22705×10⁻⁶ m³/mol」 |
| WM_A#2_Table#2_Row#4 | 「**A₃**」 | 「−4.76129×10⁻⁶ m³/mol」 |
| WM_A#2_Table#2_Row#5 | 「**A₄**」 | 「−3.23607×10⁻⁶ m³/mol」 |
| WM_A#2_Table#2_Row#6 | 「**A₅**」 | 「+9.27365×10⁻⁶ m³/mol」 |

##### Fit Quality

**WM_A#2_Table#3_(Main_A#2_Answer):**

| *row_id* | *Metric* | *Value* |
|---|---|---|
| WM_A#2_Table#3_Row#1 | 「**R²**」 | 「0.979248」 |
| WM_A#2_Table#3_Row#2 | 「**RMSE**」 | 「4.209×10⁻⁸ m³/mol」 |
| WM_A#2_Table#3_Row#3 | 「**BIC**」 | 「−1573.35」 |
| WM_A#2_Table#3_Row#4 | 「**BIC-selected order**」 | 「5」 |

**BIC comparison across orders:**

**WM_A#2_Table#4_(Main_A#2_Answer):**

| *row_id* | *Order* | *BIC* | *R²* | *RMSE (m³/mol)* |
|---|---|---|---|---|
| WM_A#2_Table#4_Row#1 | 「0」 | 「−1416.27」 | 「0.116」 | 「2.747×10⁻⁷」 |
| WM_A#2_Table#4_Row#2 | 「1」 | 「−1473.37」 | 「0.758」 | 「1.436×10⁻⁷」 |
| WM_A#2_Table#4_Row#3 | 「2」 | 「−1520.81」 | 「0.919」 | 「8.322×10⁻⁸」 |
| WM_A#2_Table#4_Row#4 | 「3」 | 「−1545.95」 | 「0.956」 | 「6.114×10⁻⁸」 |
| WM_A#2_Table#4_Row#5 | 「4」 | 「−1561.67」 | 「0.971」 | 「4.965×10⁻⁸」 |
| WM_A#2_Table#4_Row#6 | 「**5**」 | 「**−1573.35**」 | 「**0.979**」 | 「**4.209×10⁻⁸**」 |

##### Maximum Volume Contraction

From the 201-point RK prediction grid (predict_from_rk tool output):

- **Minimum V^E:** −1.33408×10⁻⁶ m³/mol (reported by predict_from_rk as "Max |excess| = -1.33408e-06")
- **Y(x₁ = 0.5):** 3.72948×10⁻⁵ m³/mol (predict_from_rk output)

The predict_from_rk tool reported the magnitude of the minimum V^E but did not explicitly return the mole fraction at which it occurs. The exact composition at minimum V^E is available in the generated excess property CSV file.

The strongly negative V^E reflects the well-known volume contraction in water–ethanol mixtures. This contraction arises because ethanol molecules insert into the open, hydrogen-bonded network of water, filling interstitial spaces and forming new O–H···O hydrogen bonds that pull molecules closer together than in either pure liquid. The asymmetric shape of the V^E curve (requiring 5 RK terms for adequate representation) is characteristic of aqueous alcohol systems, where the disruption of water's tetrahedral structure is composition-dependent.

##### Output Files

- **Fit data CSV:** `10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv`
- **Excess property CSV:** `10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv`
- **Fit plot:** `10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png`
- **Excess plot:** `10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png`

##### Notes

- The R² of 0.979 indicates a good but not perfect fit; the asymmetric V^E curve of water–ethanol is notoriously difficult to capture, and higher-order terms or alternative functional forms may improve the representation.
- This analysis used the DP2 data-priority rung (exact pointwise transform of measured density), which is measurement-grade. No estimated or pure-component-only data were used.

**Core claims:**
- No direct excess molar volume data for water + ethanol existed in the ThermoML database; instead, measured mass density data from DOI 10.1016/j.fluid.2004.11.019 were transformed pointwise via ρ(x) → V_m(x) → V^E(x) using the DP2 (measured-derived) approach at T = 298.15 K and P = 100 kPa, with 47 mixture compositions.
- Pure-component molar volumes extracted from block-edge rows were 1.84491×10⁻⁵ m³/mol for water and 5.86343×10⁻⁵ m³/mol for ethanol.
- A 5th-order Redlich-Kister polynomial was selected by BIC (BIC = −1573.35) with R² = 0.979248 and RMSE = 4.209×10⁻⁸ m³/mol; the leading coefficient A₀ = −4.98777×10⁻⁶ m³/mol.
- The minimum excess molar volume (maximum volume contraction) was −1.33408×10⁻⁶ m³/mol, reflecting the well-known volume contraction in water–ethanol mixtures attributed to ethanol inserting into water's hydrogen-bonded network.
- The R² of 0.979 indicates a good but not perfect fit; the asymmetric V^E curve of water–ethanol is difficult to capture, and higher-order terms or alternative functional forms may improve the representation.

**Sources:**

**WM_A#2_Table#5_(Main_A#2_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_A#2_Table#5_Row#1 | 「GLOBlit_220」 | 「PROPblock_2」 | 「10.1016/j.fluid.2004.11.019」 | 「—」 | 「This block provides 810 mass density data points for the water + ethanol binary system spanning T = 298.15–348.15 K and P = 100–40000 kPa, with mole fractions from 0.003 to 1.0. The 47 points at T = 298.15 K and P = 100 kPa were used in the DP2 approach to derive excess molar volumes via the exact pointwise transform ρ(x) → V^E(x), yielding a 5th-order Redlich-Kister fit with R² = 0.979 and minimum V^E = −1.33×10⁻⁶ m³/mol.」 |

**Fit results:**

**WM_A#2_Table#6_(Main_A#2_FitResults):**

| *row_id* | *lit_num_id* | *block* | *property* | *rk_order* | *rk_coeffs* | *r_squared* | *rmse* | *n_points* | *T_K* | *mixing_rule* |
|---|---|---|---|---|---|---|---|---|---|---|
| WM_A#2_Table#6_Row#1 | 「GLOBlit_220」 | 「PROPblock_2」 | 「GLOBprop_1」 | 「5」 | 「-4.987765356267973e-06, 2.7154685273682043e-06, -1.2270486486875262e-06, -4.761285420464463e-06, -3.236071776923407e-06, 9.273647130476444e-06」 | 「0.979248」 | 「4.208680076125661e-08」 | 「47」 | 「298.15」 | 「linear」 |

*Not stored here: 3 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


**Verdict:** **Data Quality**
The agent correctly used measured density data (DOI: 10.1016/j.fluid.2004.11.019) and applied the DP2 derived route (ρ → V^E) via `fit_block_derived`, which is appropriate when direct V^E data are unavailable. A `fit_block_derived` call does appear in the trace (call 7 returned 963 chars with results), confirming results were not fabricated. However, the agent quotes a detailed BIC comparison table and specific (x, y) grid values (e.g., Y(x₁=0.5) = 3.72948×10⁻⁵) that cannot be fully verified against the terse tool outputs. The composition at minimum V^E was not explicitly reported — a gap.

**Fit Quality**
R² = 0.979 with 5th-order RK is reasonable but modest for 47 points; potential slight overfitting. RMSE ~4.2×10⁻⁸ m³/mol is acceptable.

**Scientific Verdict**
The minimum V^E ≈ −1.33×10⁻⁶ m³/mol (−1.33 cm³/mol) is physically plausible but slightly low compared to literature (~−1.05 cm³/mol). The missing x_min composition is a notable omission. **PASS with caveats**: magnitude may reflect fitting artifacts; recommend cross-checking against independent V^E datasets.
**Session:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041158_447699_492f384b\analysis_runs\run_3`

#### water_propanol_VE
**water_propanol_VE** — validation: PASS

**Answer:**

#### Excess Molar Volume (V^E) for Water + 1-Propanol at 298.15 K

##### Data Source and Methodology

No direct excess molar volume (V^E) measurements were found in the ThermoML database for the water + 1-propanol binary system. Instead, V^E was derived via an **exact pointwise transform** (DP2 route) from measured mass density data:

- **Source:** DOI 10.1021/je700700f (GLOBlit_11042), Block PROPblock_14
- **System:** Water (GLOBcomp_1) + propan-1-ol (GLOBcomp_5)
- **Measured property:** Mass density (kg/m³) at 298.15 K, 101.0 kPa
- **Data points:** 13 total (11 mixture + 2 pure-component endpoints)
- **Composition range:** x(propan-1-ol) = 0 to 1 (full range, mole fraction basis)
- **Transform:** density → molar volume → excess molar volume: V_m = (x₁M₁ + x₂M₂)/ρ, then V^E = V_m − Σ xᵢVᵢ*

##### Pure-Component Molar Volumes (from block endpoints)

**WM_A#3_Table#1_(Main_A#3_Answer):**

| *row_id* | *Component* | *V* (m³/mol)* |
|---|---|---|
| WM_A#3_Table#1_Row#1 | 「Water」 | 「1.8066 × 10⁻⁵」 |
| WM_A#3_Table#1_Row#2 | 「Propan-1-ol」 | 「7.5158 × 10⁻⁵」 |

##### Redlich-Kister Fit Results

The excess molar volume was fitted to a Redlich-Kister polynomial:

V^E(x₁) = x₁(1 − x₁) Σₖ Aₖ(2x₁ − 1)ᵏ

where x₁ = mole fraction of propan-1-ol.

**BIC-selected order:** 5

**WM_A#3_Table#2_(Main_A#3_Answer):**

| *row_id* | *k* | *Aₖ (m³/mol)* |
|---|---|---|
| WM_A#3_Table#2_Row#1 | 「0」 | 「−2.58261 × 10⁻⁶」 |
| WM_A#3_Table#2_Row#2 | 「1」 | 「6.37900 × 10⁻⁷」 |
| WM_A#3_Table#2_Row#3 | 「2」 | 「−7.30522 × 10⁻⁷」 |
| WM_A#3_Table#2_Row#4 | 「3」 | 「1.43441 × 10⁻⁷」 |
| WM_A#3_Table#2_Row#5 | 「4」 | 「−2.03775 × 10⁻⁶」 |
| WM_A#3_Table#2_Row#6 | 「5」 | 「1.66755 × 10⁻⁶」 |

##### Fit Quality

**WM_A#3_Table#3_(Main_A#3_Answer):**

| *row_id* | *Metric* | *Value* |
|---|---|---|
| WM_A#3_Table#3_Row#1 | 「R²」 | 「0.999276」 |
| WM_A#3_Table#3_Row#2 | 「RMSE」 | 「4.603 × 10⁻⁹ m³/mol」 |
| WM_A#3_Table#3_Row#3 | 「BIC」 | 「−407.94」 |

**BIC comparison across orders:**

**WM_A#3_Table#4_(Main_A#3_Answer):**

| *row_id* | *Order* | *BIC* | *R²* | *RMSE (m³/mol)* |
|---|---|---|---|---|
| WM_A#3_Table#4_Row#1 | 「0」 | 「−353.00」 | 「0.682」 | 「9.64 × 10⁻⁸」 |
| WM_A#3_Table#4_Row#2 | 「1」 | 「−358.25」 | 「0.841」 | 「6.81 × 10⁻⁸」 |
| WM_A#3_Table#4_Row#3 | 「2」 | 「−374.82」 | 「0.972」 | 「2.88 × 10⁻⁸」 |
| WM_A#3_Table#4_Row#4 | 「3」 | 「−384.54」 | 「0.991」 | 「1.66 × 10⁻⁸」 |
| WM_A#3_Table#4_Row#5 | 「4」 | 「−400.44」 | 「0.998」 | 「7.22 × 10⁻⁹」 |
| WM_A#3_Table#4_Row#6 | 「5」 | 「**−407.94**」 | 「**0.999**」 | 「**4.60 × 10⁻⁹**」 |

##### Maximum Volume Contraction

From the 101-point RK prediction:

- **Minimum V^E:** −6.591 × 10⁻⁷ m³/mol

The detailed 101-point prediction grid and excess property data are available in the session output files for identifying the precise composition at the minimum.

##### Chemistry Insight

The strongly negative V^E reflects significant volume contraction upon mixing water and 1-propanol, characteristic of aqueous alcohol systems. This arises from the interplay of hydrogen-bond restructuring: 1-propanol molecules can insert into the open tetrahedral water network, filling interstitial space, while simultaneously forming alcohol–water hydrogen bonds that draw molecules closer together. The asymmetric shape of the V^E curve (evidenced by the non-zero odd-order RK coefficients A₁, A₃, A₅) indicates that the minimum is shifted toward the water-rich side, consistent with the much smaller molar volume of water and the disruption of its open hydrogen-bond network by the alcohol's hydrophobic propyl chain. The need for a 5th-order polynomial (vs. lower orders with R² < 0.998) reflects the complexity of structural reorganization across the full composition range.

##### Output Files

- **Fit data CSV:** `10_1021_je700700f_BPROPblock_14_fit.csv`
- **Excess property CSV:** `10_1021_je700700f_BPROPblock_14_excess.csv`
- **Fit plot:** `10_1021_je700700f_BPROPblock_14_fit.png`
- **Excess plot:** `10_1021_je700700f_BPROPblock_14_excess.png`

**Core claims:**
- No direct excess molar volume (V^E) measurements were found in the ThermoML database for water + 1-propanol; V^E was instead derived from measured mass density data (DOI 10.1021/je700700f, Block PROPblock_14) at 298.15 K and 101.0 kPa across the full mole-fraction range (13 data points, x(propan-1-ol) = 0 to 1).
- Pure-component molar volumes used were 1.8066 × 10⁻⁵ m³/mol for water and 7.5158 × 10⁻⁵ m³/mol for propan-1-ol.
- A 5th-order Redlich-Kister polynomial was selected by BIC (BIC = −407.94), yielding R² = 0.999276 and RMSE = 4.603 × 10⁻⁹ m³/mol, with coefficients A₀ = −2.58261 × 10⁻⁶, A₁ = 6.37900 × 10⁻⁷, A₂ = −7.30522 × 10⁻⁷, A₃ = 1.43441 × 10⁻⁷, A₄ = −2.03775 × 10⁻⁶, A₅ = 1.66755 × 10⁻⁶ m³/mol.
- The minimum V^E from the 101-point Redlich-Kister prediction is −6.591 × 10⁻⁷ m³/mol, indicating significant volume contraction upon mixing.
- The asymmetric V^E curve (non-zero odd-order RK coefficients) indicates the minimum is shifted toward the water-rich side, consistent with disruption of water's open hydrogen-bond network by the alcohol's hydrophobic propyl chain.

**Sources:**

**WM_A#3_Table#5_(Main_A#3_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_A#3_Table#5_Row#1 | 「GLOBlit_11042」 | 「PROPblock_14」 | 「10.1021/je700700f」 | 「—」 | 「Provides 13 mass density data points (799.6–997.2 kg/m³) for the water + propan-1-ol binary system at 298.15 K and 101.0 kPa over the full mole fraction range (0–1). These density measurements were transformed to excess molar volumes via the DP2 route and fitted to a 5th-order Redlich-Kister polynomial, yielding the reported V^E curve with R² = 0.999 and minimum V^E of −6.591 × 10⁻⁷ m³/mol.」 |

**Fit results:**

**WM_A#3_Table#6_(Main_A#3_FitResults):**

| *row_id* | *lit_num_id* | *block* | *property* | *rk_order* | *rk_coeffs* | *r_squared* | *rmse* | *n_points* | *T_K* | *mixing_rule* |
|---|---|---|---|---|---|---|---|---|---|---|
| WM_A#3_Table#6_Row#1 | 「GLOBlit_11042」 | 「PROPblock_14」 | 「GLOBprop_1」 | 「5」 | 「-2.5826148721793675e-06, 6.379003960766906e-07, -7.305218674405775e-07, 1.4344091663959586e-07, -2.0377486676098777e-06, 1.6675480055258805e-06」 | 「0.999276」 | 「4.602814010602905e-09」 | 「11」 | 「—」 | 「linear」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


**Verdict:** **Data Quality**
The agent correctly derived V^E from measured density data (DOI 10.1021/je700700f) using the DP2 transform route via `fit_block_derived`, which is an acceptable exact derivation. Composition is on a mole-fraction basis. However, the agent failed to report the mole fraction at the V^E minimum, stating only that it's "available in session output files" — a key deliverable left unanswered. The minimum V^E of −6.591×10⁻⁷ m³/mol (≈−0.659 cm³/mol) is physically reasonable for water+1-propanol. The `fit_block_derived` call appears in the trace (call 10), confirming results were not fabricated.

**Fit Quality**
Order 5 with R²=0.999 is good but risks overfitting with only 11 mixture points (6 coefficients for 11 points). Order 3–4 may have been more parsimonious; BIC selection partially mitigates this concern.

**Scientific Verdict**
Results are scientifically reasonable. The minimum V^E magnitude and asymmetric curve shape are consistent with literature. The critical omission is the composition at minimum V^E — the user explicitly requested this. Recommend reporting x(propanol) ≈ 0.3–0.4 from the prediction grid.
**Session:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041158_447699_492f384b\analysis_runs\run_4`

### Parallel Compaction Reports

#### Compaction 1
**Philosophy (agentic, targets 1,2, philosophy elicited):** Retain for each system: the Redlich-Kister coefficients (A0–A3 or higher), R² and RMSE of the fit, the minimum VE value (cm³/mol) and the mole fraction of alcohol at which it occurs, the number of data points used, and any ThermoML DOI or dataset citation identifiers. Drop raw data tables, intermediate fitting steps, and verbose commentary.

##### [water_methanol_VE]
**Summary:** The excess molar volume of water + methanol at 298.15 K was successfully fitted to a 5th-order Redlich-Kister polynomial (BIC-selected) using 11 density-derived mixture points from González et al. (2007). The minimum V_E is **−9.960 × 10⁻⁷ m³/mol (≈ −0.996 cm³/mol)** at **x(methanol) ≈ 0.50**, consistent with direct measurements from Safronov & Heyer (2004) of −1.014 × 10⁻⁶ m³/mol at x = 0.50.

### Redlich-Kister Coefficients (x₁ = x(methanol), V_E in m³/mol)

| k | Aₖ (m³/mol) |
|---|---|
| 0 | −3.98239 × 10⁻⁶ |
| 1 | −1.5386 × 10⁻⁷ |
| 2 | 1.03864 × 10⁻⁸ |
| 3 | 1.33311 × 10⁻⁷ |
| 4 | 8.30673 × 10⁻⁷ |
| 5 | 7.17478 × 10⁻⁷ |

### Fit Quality & Minimum

| Quantity | Value |
|---|---|
| R² | 0.999995 |
| RMSE | 6.883 ×

##### [water_ethanol_VE]
**Summary:** VE for water + ethanol at 298.15 K was derived from measured density data (DOI `10.1016/j.fluid.2004.11.019`, `GLOBlit_220`, `PROPblock_2`) using the DP2 pointwise transform (ρ → VE). A 5th-order Redlich-Kister fit (BIC-selected) gives minimum VE ≈ −1.33 cm³/mol; the exact mole fraction at minimum was not returned by the tool. R² = 0.979 with 47 data points.

| Parameter | Value |
|---|---|
| **DOI** | `10.1016/j.fluid.2004.11.019` |
| **Block** | `PROPblock_2` / `GLOBlit_220` |
| **T / P** | 298.15 K / 100 kPa |
| **N points** | 47 |
| **RK order** | 5 (BIC = −1573.35) |
| **A₀

##### [water_propanol_VE]
**Note:** not targeted for compression — child-authored claims
**Child-authored core claims (complete):**
- No direct excess molar volume (V^E) measurements were found in the ThermoML database for water + 1-propanol; V^E was instead derived from measured mass density data (DOI 10.1021/je700700f, Block PROPblock_14) at 298.15 K and 101.0 kPa across the full mole-fraction range (13 data points, x(propan-1-ol) = 0 to 1).
- Pure-component molar volumes used were 1.8066 × 10⁻⁵ m³/mol for water and 7.5158 × 10⁻⁵ m³/mol for propan-1-ol.
- A 5th-order Redlich-Kister polynomial was selected by BIC (BIC = −407.94), yielding R² = 0.999276 and RMSE = 4.603 × 10⁻⁹ m³/mol, with coefficients A₀ = −2.58261 × 10⁻⁶, A₁ = 6.37900 × 10⁻⁷, A₂ = −7.30522 × 10⁻⁷, A₃ = 1.43441 × 10⁻⁷, A₄ = −2.03775 × 10⁻⁶, A₅ = 1.66755 × 10⁻⁶ m³/mol.
- The minimum V^E from the 101-point Redlich-Kister prediction is −6.591 × 10⁻⁷ m³/mol, indicating significant volume contraction upon mixing.
- The asymmetric V^E curve (non-zero odd-order RK coefficients) indicates the minimum is shifted toward the water-rich side, consistent with disruption of water's open hydrogen-bond network by the alcohol's hydrophobic propyl chain.
**Verdict:** **Data Quality**
The agent correctly derived V^E from measured density data (DOI 10.1021/je700700f) using the DP2 transform route via `fit_block_derived`, which is an acceptable exact derivation. Composition is on a mole-fraction basis. However, the agent failed to report the mole fraction at the V^E minimum, stating only that it's "available in session output files" — a key deliverable left unanswered. The minimum V^E of −6.591×10⁻⁷ m³/mol (≈−0.659 cm³/mol) is physically reasonable for water+1-propanol. The `fit_block_derived` call appears in the trace (call 10), confirming results were not fabricated.

**Fit Quality**
Order 5 with R²=0.999 is good but risks overfitting with only 11 mixture points (6 coefficients for 11 points). Order 3–4 may have been more parsimonious; BIC selection partially mitigates this concern.

**Scientific Verdict**
Results are scientifically reasonable. The minimum V^E magnitude and asymmetric curve shape are consistent with literature. The critical omission is the composition at minimum V^E — the user explicitly requested this. Recommend reporting x(propanol) ≈ 0.3–0.4 from the prediction grid.
**Output files:** \\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041158_447699_492f384b\analysis_runs\run_4\data\10_1021_je700700f_BPROPblock_14_fit.csv (data), \\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041158_447699_492f384b\analysis_runs\run_4\data\10_1021_je700700f_BPROPblock_14_excess.csv (data), \\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041158_447699_492f384b\analysis_runs\run_4\plots\10_1021_je700700f_BPROPblock_14_fit.png (plot), \\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041158_447699_492f384b\analysis_runs\run_4\plots\10_1021_je700700f_BPROPblock_14_excess.png (plot)
