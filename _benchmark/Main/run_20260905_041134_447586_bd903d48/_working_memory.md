# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041134_447586_bd903d48`

### History
- [analysis:A1] "At 25 °C, what Redlich–Kister correlation best represents the density of liquid " (271s, 15 iters, validation=PASS verdict=**Data Quality**
The trace sho)

### Analysis Agent Results

#### A1
**A1** — validation: PASS

**Answer:**

#### Redlich–Kister Correlation for the Density of Liquid Methanol + Water at 298.15 K

##### Data Source

**WM_A#1_Table#1_(Main_A#1_Answer):**

| *row_id* | *Item* | *Value* |
|---|---|---|
| WM_A#1_Table#1_Row#1 | 「DOI」 | 「10.1016/j.jct.2007.05.004」 |
| WM_A#1_Table#1_Row#2 | 「Literature ID」 | 「GLOBlit_2825」 |
| WM_A#1_Table#1_Row#3 | 「Block」 | 「PROPblock_10」 |
| WM_A#1_Table#1_Row#4 | 「System」 | 「Binary: methanol + water」 |
| WM_A#1_Table#1_Row#5 | 「Temperature」 | 「298.15 K」 |
| WM_A#1_Table#1_Row#6 | 「Pressure」 | 「101 kPa」 |
| WM_A#1_Table#1_Row#7 | 「Data points used in fit」 | 「11 mixture points + 2 pure endpoints (derived from fit_block output: "Points: 11 mixture / 39 total")」 |
| WM_A#1_Table#1_Row#8 | 「Composition range」 | 「x(water) = 0 to 1 (full mole-fraction range)」 |

##### Pure-Component Densities (Block Endpoints)

**WM_A#1_Table#2_(Main_A#1_Answer):**

| *row_id* | *Component* | *ρ* (kg/m³)* |
|---|---|---|
| WM_A#1_Table#2_Row#1 | 「Water」 | 「997.05」 |
| WM_A#1_Table#2_Row#2 | 「Methanol」 | 「787.2」 |

##### Fitted Equation

The density is represented with a **linear mixing rule** plus a Redlich–Kister deviation polynomial:

$$\rho(x_1) = x_1\,\rho_1^* + x_2\,\rho_2^* + x_1\,x_2\,\sum_{k=0}^{n} A_k\,(x_1 - x_2)^k$$

where **x₁ = mole fraction of water**, **x₂ = 1 − x₁ = mole fraction of methanol**, ρ₁* = 997.05 kg/m³ (water), ρ₂* = 787.2 kg/m³ (methanol), and all coefficients Aₖ are in **kg/m³**.

##### BIC-Selected Optimal Order: 5

The Bayesian Information Criterion (BIC) was evaluated for orders 0–5. Order 5 gives the lowest (most negative) BIC and is selected as optimal:

**WM_A#1_Table#3_(Main_A#1_Answer):**

| *row_id* | *Order* | *BIC* | *R²* | *RMSE (kg/m³)* |
|---|---|---|---|---|
| WM_A#1_Table#3_Row#1 | 「0」 | 「2.56」 | 「0.862798」 | 「1.00745」 |
| WM_A#1_Table#3_Row#2 | 「1」 | 「3.22」 | 「0.882879」 | 「0.930813」 |
| WM_A#1_Table#3_Row#3 | 「2」 | 「−1.47」 | 「0.938515」 | 「0.674419」 |
| WM_A#1_Table#3_Row#4 | 「3」 | 「−12.24」 | 「0.981419」 | 「0.370747」 |
| WM_A#1_Table#3_Row#5 | 「4」 | 「−29.48」 | 「0.996883」 | 「0.151854」 |
| WM_A#1_Table#3_Row#6 | 「**5**」 | 「**−57.07**」 | 「**0.999796**」 | 「**0.038852**」 |

##### Best-Fit Coefficients (Order 5)

**WM_A#1_Table#4_(Main_A#1_Answer):**

| *row_id* | *Coefficient* | *Value (kg/m³)* |
|---|---|---|
| WM_A#1_Table#4_Row#1 | 「A₀」 | 「−42.3108」 |
| WM_A#1_Table#4_Row#2 | 「A₁」 | 「2.46129」 |
| WM_A#1_Table#4_Row#3 | 「A₂」 | 「7.28093」 |
| WM_A#1_Table#4_Row#4 | 「A₃」 | 「−0.41971」 |
| WM_A#1_Table#4_Row#5 | 「A₄」 | 「−46.1538」 |
| WM_A#1_Table#4_Row#6 | 「A₅」 | 「−43.8431」 |

##### Fit Statistics (Order 5)

**WM_A#1_Table#5_(Main_A#1_Answer):**

| *row_id* | *Statistic* | *Value* |
|---|---|---|
| WM_A#1_Table#5_Row#1 | 「R²」 | 「0.999796」 |
| WM_A#1_Table#5_Row#2 | 「RMSE」 | 「0.038852 kg/m³」 |
| WM_A#1_Table#5_Row#3 | 「BIC」 | 「−57.07」 |

##### Chemistry Insight

The density of the methanol–water mixture increases monotonically from 787.2 kg/m³ (pure methanol) to 997.05 kg/m³ (pure water) at 298.15 K, but the relationship is markedly non-linear in mole fraction. The large negative leading coefficient A₀ = −42.31 kg/m³ indicates that the density deviates substantially below the linear (ideal) mixing line — this corresponds to **negative excess volume** (volume contraction upon mixing), a hallmark of the strong hydrogen-bonding interactions between methanol and water molecules. The need for a 5th-order polynomial (with significant higher-order terms A₄ and A₅) reflects the pronounced asymmetry of the deviation curve, which peaks in the water-rich region where methanol molecules are incorporated into the extended water hydrogen-bond network.

##### Output Files

- **Fit data CSV:** `10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_fit.csv`
- **Excess property CSV:** `10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_excess.csv`
- **Fit plot:** `10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_fit.png`
- **Excess plot:** `10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_excess.png`

**Core claims:**
- The liquid density of methanol + water at 298.15 K and 101 kPa is well represented by a linear mixing rule plus a 5th-order Redlich–Kister deviation polynomial in water mole fraction, with pure-component densities ρ*(water) = 997.05 kg/m³ and ρ*(methanol) = 787.2 kg/m³ and coefficients A₀ = −42.3108, A₁ = 2.46129, A₂ = 7.28093, A₃ = −0.41971, A₄ = −46.1538, A₅ = −43.8431 (all in kg/m³).
- Order 5 was selected as optimal by the Bayesian Information Criterion (BIC = −57.07), yielding R² = 0.999796 and RMSE = 0.038852 kg/m³ over 11 mixture data points spanning the full mole-fraction range.
- The large negative leading coefficient A₀ = −42.3108 kg/m³ indicates substantial negative deviation from ideal (linear) mixing, corresponding to negative excess volume (volume contraction on mixing), attributed to strong hydrogen-bonding interactions between methanol and water.
- The requirement for a 5th-order polynomial with significant higher-order terms reflects pronounced asymmetry of the density deviation curve.

**Sources:**

**WM_A#1_Table#6_(Main_A#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_A#1_Table#6_Row#1 | 「GLOBlit_2825」 | 「PROPblock_10」 | 「10.1016/j.jct.2007.05.004」 | 「—」 | 「This block provides binary methanol + water mass density data (782.48–998.2 kg/m³) over the full mole-fraction range at 101 kPa, with temperatures spanning 293.15–303.15 K. The 298.15 K subset (11 mixture points from the 39 total) was used to fit the 5th-order Redlich–Kister correlation reported in the answer.」 |

**Fit results:**

**WM_A#1_Table#7_(Main_A#1_FitResults):**

| *row_id* | *lit_num_id* | *block* | *property* | *rk_order* | *rk_coeffs* | *r_squared* | *rmse* | *n_points* | *T_K* | *mixing_rule* |
|---|---|---|---|---|---|---|---|---|---|---|
| WM_A#1_Table#7_Row#1 | 「GLOBlit_2825」 | 「PROPblock_10」 | 「GLOBprop_1」 | 「5」 | 「-42.310757722792545, 2.461285361216577, 7.280933000115691, -0.4197102000547031, -46.153810492202304, -43.843096353659426」 | 「0.999796」 | 「0.03885240667464569」 | 「11」 | 「298.15」 | 「linear」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


**Verdict:** **Data Quality**
The trace shows a successful `fit_block` at step 12 returning 871 chars with results, confirming the fit was not fabricated. Data from DOI 10.1016/j.jct.2007.05.004 is a legitimate ThermoML source. However, only 11 mixture points is modest for a 6-parameter (order-5) fit. The density data appear to be in mole fraction basis, which is appropriate. No composition conversion issues flagged.

**Fit Quality**
Order 5 with 6 parameters fitted to 11 data points raises overfitting concerns (nearly 1 parameter per 2 points). While BIC penalizes complexity, with so few points BIC may still favor overfitting. R² = 0.9998 and RMSE = 0.039 kg/m³ are excellent, but the high-order coefficients A₄ and A₅ are large, suggesting potential instability outside the fitted range.

**Scientific Verdict**
Results are physically reasonable—negative A₀ correctly reflects volume contraction in methanol-water. However, order 5 with only 11 points risks overfitting; order 3–4 may be more robust. Recommend validating against additional datasets and considering lower-order fits for extrapolation reliability.
**Session:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041134_447586_bd903d48\analysis_runs\run_1`
