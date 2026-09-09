# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194722_684644_49ae3f02`

### History
- [analysis:A1] "Fit a Redlich-Kister polynomial to the viscosity of the binary liquid mixture wa" (469s, 14 iters, validation=PASS verdict=**Data Quality**
The trace sho)

### Analysis Agent Results

#### A1
**A1** — validation: PASS

**Answer:**

#### Redlich-Kister Fit for Viscosity of Water + Ethylene Glycol at 298.15 K

##### System & Source

**WM_A#1_Table#1_(Main_A#1_Answer):**

| *row_id* | *Parameter* | *Value* |
|---|---|---|
| WM_A#1_Table#1_Row#1 | 「System」 | 「Water + 1,2-ethanediol (ethylene glycol), binary liquid」 |
| WM_A#1_Table#1_Row#2 | 「Source」 | 「GLOBlit_5201 / DOI 10.1016/j.jct.2018.02.022 / PROPblock_24」 |
| WM_A#1_Table#1_Row#3 | 「Measurement method」 | 「Concentric cylinders viscometry」 |
| WM_A#1_Table#1_Row#4 | 「Temperature」 | 「298.15 K」 |
| WM_A#1_Table#1_Row#5 | 「Pressure」 | 「92.3 kPa」 |
| WM_A#1_Table#1_Row#6 | 「Composition basis」 | 「Mole fraction of 1,2-ethanediol (*x*₁), range 0–1 (21 unique compositions)」 |
| WM_A#1_Table#1_Row#7 | 「Viscosity basis」 | 「Dynamic viscosity, η (Pa·s)」 |
| WM_A#1_Table#1_Row#8 | 「Data points used」 | 「19 mixture + 2 pure-component endpoints = 21 points」 |

##### Pure-Component Endpoint Values (from block edges)

**WM_A#1_Table#2_(Main_A#1_Answer):**

| *row_id* | *Component* | *η* (Pa·s)* |
|---|---|---|
| WM_A#1_Table#2_Row#1 | 「1,2-ethanediol (x₁ = 1)」 | 「0.016223」 |
| WM_A#1_Table#2_Row#2 | 「Water (x₁ = 0)」 | 「0.00089689」 |

##### Mixing Rule & RK Equation

Because viscosity spans nearly two orders of magnitude across the composition range, the **Arrhenius (logarithmic) mixing rule** is used:

$$\ln\eta = x_1 \ln\eta_1^* + (1 - x_1)\ln\eta_2^* + x_1(1 - x_1)\sum_{k=0}^{n} A_k\,(2x_1 - 1)^k$$

where *x*₁ = mole fraction of 1,2-ethanediol, η₁\* = 0.016223 Pa·s, η₂\* = 0.00089689 Pa·s.

##### BIC-Selected Fit: Order 3

**WM_A#1_Table#3_(Main_A#1_Answer):**

| *row_id* | *Coefficient* | *Value (dimensionless)* |
|---|---|---|
| WM_A#1_Table#3_Row#1 | 「A₀」 | 「2.39674」 |
| WM_A#1_Table#3_Row#2 | 「A₁」 | 「−1.04444」 |
| WM_A#1_Table#3_Row#3 | 「A₂」 | 「0.668173」 |
| WM_A#1_Table#3_Row#4 | 「A₃」 | 「−0.3209」 |

##### Fit Quality

**WM_A#1_Table#4_(Main_A#1_Answer):**

| *row_id* | *Metric* | *Value* |
|---|---|---|
| WM_A#1_Table#4_Row#1 | 「R²」 | 「0.999940」 |
| WM_A#1_Table#4_Row#2 | 「RMSE」 | 「0.001320 (in ln η space)」 |
| WM_A#1_Table#4_Row#3 | 「BIC」 | 「−240.17」 |

##### Model Selection (BIC Comparison)

**WM_A#1_Table#5_(Main_A#1_Answer):**

| *row_id* | *Order* | *BIC* | *R²* | *RMSE* |
|---|---|---|---|---|
| WM_A#1_Table#5_Row#1 | 「0」 | 「−90.89」 | 「0.7516」 | 「0.08465」 |
| WM_A#1_Table#5_Row#2 | 「1」 | 「−141.05」 | 「0.9848」 | 「0.02092」 |
| WM_A#1_Table#5_Row#3 | 「2」 | 「−194.71」 | 「0.9992」 | 「0.00472」 |
| WM_A#1_Table#5_Row#4 | 「**3**」 | 「**−240.17**」 | 「**0.9999**」 | 「**0.00132**」 |
| WM_A#1_Table#5_Row#5 | 「4」 | 「−237.59」 | 「0.9999」 | 「0.00131」 |
| WM_A#1_Table#5_Row#6 | 「5」 | 「−234.83」 | 「0.9999」 | 「0.00130」 |

Order 3 is selected by BIC — orders 4 and 5 offer negligible improvement and are penalized for additional parameters.

##### Chemistry Insight

The large, positive A₀ coefficient (+2.40) confirms a strong **positive deviation** of viscosity from the Arrhenius ideal-mixing baseline. This is characteristic of the water–ethylene glycol system, where the two hydroxyl groups of ethylene glycol form an extensive hydrogen-bonding network with water, creating transient supramolecular structures that resist flow more than either pure component would predict. The asymmetry captured by A₁ (−1.04) and higher-order terms reflects the fact that the viscosity maximum shifts toward the ethylene-glycol-rich side, consistent with the stoichiometry of the hydrogen-bonding complexes.

Representative data points at 298.15 K (from inspected block data):
- *x*₁ = 0 (pure water): η = 0.00089689 Pa·s
- *x*₁ = 0.2072: η = 0.0028109 Pa·s
- *x*₁ = 0.4446: η = 0.0060624 Pa·s
- *x*₁ = 1.0 (pure EG): η = 0.016223 Pa·s

##### Output Files

- Fit data CSV: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv`
- Excess property CSV: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv`
- Fit plot: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png`
- Excess plot: `10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png`

**Core claims:**
- For the water + 1,2-ethanediol (ethylene glycol) binary liquid system at 298.15 K and 92.3 kPa, dynamic viscosity across 21 compositions (x₁ = 0–1) is well described by an Arrhenius (logarithmic) mixing rule with a Redlich-Kister excess term of order 3, selected by BIC (BIC = −240.17, R² = 0.999940, RMSE = 0.001320 in ln η space).
- The fitted Redlich-Kister coefficients (dimensionless) are A₀ = 2.39674, A₁ = −1.04444, A₂ = 0.668173, A₃ = −0.3209, with pure-component endpoints η*(1,2-ethanediol) = 0.016223 Pa·s and η*(water) = 0.00089689 Pa·s.
- The large positive A₀ (+2.40) indicates a strong positive deviation of viscosity from the Arrhenius ideal-mixing baseline, attributed to extensive hydrogen-bonding interactions between the two hydroxyl groups of ethylene glycol and water that form transient supramolecular structures resisting flow.
- The asymmetry captured by A₁ (−1.04) and higher-order terms reflects a shift of the viscosity maximum toward the ethylene-glycol-rich side, consistent with the stoichiometry of hydrogen-bonding complexes.
- Orders 4 and 5 offer negligible improvement over order 3 and are penalized by BIC for additional parameters.

**Sources:**

**WM_A#1_Table#6_(Main_A#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_A#1_Table#6_Row#1 | 「GLOBlit_5201」 | 「PROPblock_24」 | 「10.1016/j.jct.2018.02.022」 | 「—」 | 「This block provides binary viscosity data for water + 1,2-ethanediol across the full mole-fraction range (0–1) at multiple temperatures including 298.15 K, measured by concentric cylinders viscometry at 92.3 kPa. The 21 data points at 298.15 K extracted from the 84-point block were used to perform the Redlich-Kister fit of order 3 in ln η space, yielding the reported coefficients and fit statistics.」 |

**Fit results:**

**WM_A#1_Table#7_(Main_A#1_FitResults):**

| *row_id* | *lit_num_id* | *block* | *property* | *rk_order* | *rk_coeffs* | *r_squared* | *rmse* | *n_points* | *T_K* | *mixing_rule* |
|---|---|---|---|---|---|---|---|---|---|---|
| WM_A#1_Table#7_Row#1 | 「GLOBlit_5201」 | 「PROPblock_24」 | 「GLOBprop_4」 | 「3」 | 「2.3967401058713325, -1.0444436005853195, 0.6681733607879681, -0.3209004397507546」 | 「0.99994」 | 「0.0013198945265291695」 | 「19」 | 「298.15」 | 「arrhenius」 |

*Not stored here: 6 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


**Verdict:** **Data Quality**
The trace shows multiple `fit_block` attempts, with the final call (step 11) returning 899 chars — likely a successful fit result. Data originates from a ThermoML DOI (10.1016/j.jct.2018.02.022), and the block was inspected before fitting. The composition basis is mole fraction, and the property is dynamic viscosity — appropriate. However, the representative data points quoted (x₁ = 0.2072, 0.4446, etc.) cannot be independently verified against tool results in the trace since inspect_block outputs are truncated. The Arrhenius mixing rule is correctly applied for viscosity spanning ~1.8 orders of magnitude. No composition-basis conversion issues are apparent.

**Fit Quality**
Order 3 selected by BIC is reasonable. R² = 0.999940 with RMSE = 0.00132 in ln η space is excellent. BIC comparison shows clear plateau at order 3 — no overfitting concern.

**Scientific Verdict**
The fit is scientifically sound: logarithmic mixing rule is appropriate for viscosity, and the positive A₀ aligns with known strong H-bonding in this system. The truncated answer text is a minor presentation issue. Results are reliable for engineering interpolation across the full composition range.
**Session:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194722_684644_49ae3f02\analysis_runs\run_1`
