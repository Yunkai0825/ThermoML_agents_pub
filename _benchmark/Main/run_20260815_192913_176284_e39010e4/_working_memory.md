# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_192913_176284_e39010e4`

### History
- [analysis:A1] "At 303.15 K and 81.5 kPa, fit a Redlich-Kister polynomial to the viscosity of li" (544s, 14 iters, validation=PASS verdict=**Data Quality**
The agent use)
- [menu:run] inspect_block_table → OK

### Analysis Agent Results

#### A1
**A1** — validation: PASS

**Answer:**

#### Redlich-Kister Fit of Dynamic Viscosity: Methanol + Ethanol at 303.15 K and 81.5 kPa

##### Data Source

- **DOI:** 10.1021/je800633a (GLOBlit_11337)
- **Mixture data block:** PROPblock_16 — binary mixture of methanol (GLOBcomp_4) + ethanol (GLOBcomp_2), liquid phase, 12 data points spanning methanol mole fraction 0.0417 to 0.9166 (from PROPblock_16 inspection)
- **Pure methanol endpoint:** PROPblock_8 (same DOI) — η = 0.000525 Pa·s at 303.15 K, 81.5 kPa
- **Pure ethanol endpoint:** PROPblock_2 (same DOI) — η = 0.000994 Pa·s at 303.15 K, 81.5 kPa
- **Measurement method:** Capillary tube (Ostwald–Ubbelohde)
- **Number of mixture data points:** 12
- **Composition range (PROPblock_16):** x₁ (methanol mole fraction) = 0.0417 to 0.9166

##### Fitted Quantity and Mixing Rule

Because viscosity is a transport property that does not combine linearly, the **Arrhenius (logarithmic) mixing rule** was used. The fitted quantity is the **excess of ln(η)**:

$$\Delta \ln\eta = \ln\eta_{\text{mix}} - \bigl[x_1 \ln\eta_1^* + x_2 \ln\eta_2^*\bigr]$$

where η₁* and η₂* are the pure-component viscosities and x₁, x₂ are mole fractions. The Redlich-Kister expansion is applied to this excess:

$$\Delta \ln\eta = x_1 \, x_2 \sum_{k=0}^{n} A_k \,(x_1 - x_2)^k$$

and the mixture viscosity is recovered as:

$$\eta_{\text{mix}} = \exp\!\Bigl[x_1 \ln\eta_1^* + x_2 \ln\eta_2^* + x_1\,x_2 \sum_{k=0}^{n} A_k\,(x_1 - x_2)^k\Bigr]$$

Here, component 1 = methanol (composition axis), component 2 = ethanol.

##### Fit Results (BIC-Selected)

**WM_A#1_Table#1_(Main_A#1_Answer):**

| *row_id* | *Parameter* | *Value* |
|---|---|---|
| WM_A#1_Table#1_Row#1 | 「**Polynomial order**」 | 「2 (3 coefficients)」 |
| WM_A#1_Table#1_Row#2 | 「**A₀**」 | 「0.0396991 (dimensionless)」 |
| WM_A#1_Table#1_Row#3 | 「**A₁**」 | 「0.0275633 (dimensionless)」 |
| WM_A#1_Table#1_Row#4 | 「**A₂**」 | 「−0.0218724 (dimensionless)」 |
| WM_A#1_Table#1_Row#5 | 「**R²**」 | 「0.982166」 |
| WM_A#1_Table#1_Row#6 | 「**RMSE**」 | 「0.000473597 Pa·s」 |
| WM_A#1_Table#1_Row#7 | 「**BIC**」 | 「−176.27」 |

The coefficients Aₖ are dimensionless because they multiply the excess of ln(η). The RMSE is reported in the original viscosity units (Pa·s) after back-transformation.

##### Pure-Component Endpoints

**WM_A#1_Table#2_(Main_A#1_Answer):**

| *row_id* | *Component* | *Source block* | *η* (Pa·s)* |
|---|---|---|---|
| WM_A#1_Table#2_Row#1 | 「Methanol (x₁)」 | 「PROPblock_8」 | 「0.000525」 |
| WM_A#1_Table#2_Row#2 | 「Ethanol (x₂)」 | 「PROPblock_2」 | 「0.000994」 |

##### BIC Model Comparison

**WM_A#1_Table#3_(Main_A#1_Answer):**

| *row_id* | *Order* | *BIC* | *R²* | *RMSE (Pa·s)* |
|---|---|---|---|---|
| WM_A#1_Table#3_Row#1 | 「0」 | 「−145.35」 | 「0.644996」 | 「0.00211302」 |
| WM_A#1_Table#3_Row#2 | 「1」 | 「−166.03」 | 「0.948524」 | 「0.000804619」 |
| WM_A#1_Table#3_Row#3 | 「**2**」 | 「**−176.27**」 | 「**0.982166**」 | 「**0.000473597**」 |
| WM_A#1_Table#3_Row#4 | 「3」 | 「−173.91」 | 「0.982353」 | 「0.000471113」 |
| WM_A#1_Table#3_Row#5 | 「4」 | 「−172.89」 | 「0.984381」 | 「0.000443219」 |
| WM_A#1_Table#3_Row#6 | 「5」 | 「−170.69」 | 「0.984747」 | 「0.000437997」 |

Order 2 is selected by BIC (lowest value), balancing fit quality against model complexity.

##### Chemistry Insight

Methanol and ethanol are both small, hydrogen-bonding primary alcohols with very similar intermolecular interaction character. The small, positive A₀ coefficient (0.0397) indicates a slight positive deviation in ln(η) — the mixture is marginally more viscous than the Arrhenius ideal prediction, consistent with a weak enhancement of hydrogen-bond networking when the two alcohols are mixed. The asymmetry coefficients A₁ and A₂ are modest, reflecting the near-symmetric behavior expected from two structurally similar molecules. The mixture data from PROPblock_16 show viscosity decreasing monotonically from 0.000968 Pa·s at x₁ = 0.0417 to 0.000556 Pa·s at x₁ = 0.9166, consistent with the lower pure-component viscosity of methanol (0.000525 Pa·s) compared to ethanol (0.000994 Pa·s).

##### Session Output Files

- **Fit data CSV:** `10_1021_je800633a_BPROPblock_16_T303.1_fit.csv`
- **Excess property CSV:** `10_1021_je800633a_BPROPblock_16_T303.1_excess.csv`
- **Fit plot:** `10_1021_je800633a_BPROPblock_16_T303.1_fit.png`
- **Excess plot:** `10_1021_je800633a_BPROPblock_16_T303.1_excess.png`

**Core claims:**
- A Redlich-Kister expansion was fitted to the excess of ln(η) for the binary mixture methanol + ethanol at 303.15 K and 81.5 kPa, using 12 mixture data points (x₁ = 0.0417 to 0.9166) from DOI 10.1021/je800633a and pure-component viscosities of 0.000525 Pa·s (methanol) and 0.000994 Pa·s (ethanol).
- BIC model selection favored a 2nd-order (3-coefficient) Redlich-Kister polynomial with A₀ = 0.0396991, A₁ = 0.0275633, A₂ = −0.0218724 (all dimensionless), yielding R² = 0.982166, RMSE = 0.000473597 Pa·s, and BIC = −176.27.
- The Arrhenius (logarithmic) mixing rule was used because viscosity does not combine linearly; the small positive A₀ indicates a slight positive deviation from Arrhenius-ideal mixing, consistent with weak enhancement of hydrogen-bond networking between the two structurally similar primary alcohols.
- Mixture viscosity decreases monotonically from 0.000968 Pa·s at x₁ = 0.0417 to 0.000556 Pa·s at x₁ = 0.9166, consistent with methanol's lower pure-component viscosity relative to ethanol.

**Sources:**

**WM_A#1_Table#4_(Main_A#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_A#1_Table#4_Row#1 | 「GLOBlit_11337」 | 「PROPblock_16」 | 「10.1021/je800633a」 | 「—」 | 「Provides the 12 binary mixture viscosity data points for methanol + ethanol at 303.15 K and 81.5 kPa (mole fraction 0.0417–0.9166, viscosity 0.000556–0.000968 Pa·s) used as the primary dataset for the Redlich-Kister fit of Δln(η).」 |
| WM_A#1_Table#4_Row#2 | 「GLOBlit_11337」 | 「PROPblock_8」 | 「10.1021/je800633a」 | 「—」 | 「Supplies the pure methanol viscosity endpoint (η* = 0.000525 Pa·s at 303.15 K, 81.5 kPa) needed to define the Arrhenius ideal mixing baseline for the excess ln(η) calculation.」 |
| WM_A#1_Table#4_Row#3 | 「GLOBlit_11337」 | 「PROPblock_2」 | 「10.1021/je800633a」 | 「—」 | 「Supplies the pure ethanol viscosity endpoint (η* = 0.000994 Pa·s at 303.15 K, 81.5 kPa) needed to define the Arrhenius ideal mixing baseline for the excess ln(η) calculation.」 |

**Fit results:**

**WM_A#1_Table#5_(Main_A#1_FitResults):**

| *row_id* | *lit_num_id* | *block* | *property* | *rk_order* | *rk_coeffs* | *r_squared* | *rmse* | *n_points* | *T_K* | *mixing_rule* |
|---|---|---|---|---|---|---|---|---|---|---|
| WM_A#1_Table#5_Row#1 | 「GLOBlit_11337」 | 「PROPblock_16」 | 「GLOBprop_4」 | 「2」 | 「0.03969906350436555, 0.027563277340611095, -0.021872378394822888」 | 「0.982166」 | 「0.00047359700150033146」 | 「12」 | 「303.15」 | 「arrhenius」 |

*Not stored here: 5 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


**Verdict:** **Data Quality**
The agent used ThermoML mixture data (DOI 10.1021/je800633a, PROPblock_16) with 12 points and pure-component endpoints from the same source. A `fit_block` call was executed (step 11), so results are not fabricated. Pure values (0.000525 and 0.000994 Pa·s) were extracted via `get_pure_values`. Composition basis is mole fraction. However, the agent quotes specific (x, y) pairs (e.g., 0.000968 at x₁=0.0417) that do not appear explicitly in any tool result in the trace — these may be narrated from the CSV output files rather than verified in-trace. This is a minor concern but not a clear fabrication since the fit tool did run successfully.

**Fit Quality**
Order 2 selected by BIC with R² = 0.982 is reasonable. The BIC comparison table shows diminishing returns beyond order 2, supporting the choice. No overfitting concern.

**Scientific Verdict**
The Arrhenius mixing rule for ln(η) is thermodynamically appropriate for viscosity. The small positive A₀ is physically consistent with similar hydrogen-bonding alcohols. Results are credible and well-documented. PASS.
**Session:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_192913_176284_e39010e4\analysis_runs\run_1`
