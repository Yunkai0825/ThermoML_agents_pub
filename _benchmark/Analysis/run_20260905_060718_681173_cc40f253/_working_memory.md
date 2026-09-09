# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_060718_681173_cc40f253`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_1 | water |  |
| comp | GLOBcomp_2 | ethanol |  |
| prop | GLOBprop_4 | viscositypas |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<water> |  |
| constr | GLOBconstr_1 | pressurekpa |  |

### History
- [query_thermoml]
- [inspect_block]
- [fit_multi_system]
- [fit_multi_system]

### Query Results
#### query
**L1_query_1** — status: success · validation: PASS

**Summary:** Ten ThermoML data blocks were identified containing dynamic viscosity measurements for binary ethanol + water mixtures near 298.15 K. Three blocks were inspected in detail. GLOBlit_2825 / PROPblock_11 (DOI: 10.1016/j.jct.2007.05.004) contains 37 points spanning 293.15–303.15 K and the full water mole-fraction range 0–1 at 101.0 kPa, with viscosities from 0.000797 to 0.002705 Pa·s; at 298.15 K, viscosity rises from 0.001082 Pa·s at x(water)=0 to 0.002275 Pa·s at x(water)=0.6991. GLOBlit_5201 / PROPblock_21 (DOI: 10.1016/j.jct.2018.02.022) is the largest block with 100 points over 293.15–308.15 K, ethanol mole-fraction 0–1, at 92.3 kPa, with viscosities from 0.00075887 to 0.0028641 Pa·s. GLOBlit_7676 / PROPblock_18 (DOI: 10.1021/acs.jced.8b00939) provides 9 points at 298.2 K and 100.0 kPa using water mass fraction (0.061–0.62), with viscosities from 0.00131 to 0.00234 Pa·s increasing monotonically with water content. Seven additional blocks from other DOIs were found but not numerically inspected. The data exhibit the well-known non-ideal viscosity maximum at intermediate compositions, attributed to enhanced hydrogen-bonding interactions between ethanol and water. GLOBlit_2825 / PROPblock_11 and GLOBlit_5201 / PROPblock_21 are recommended for comprehensive analysis.

**Answer:**

#### Binary Mixture Viscosity Data: Ethanol + Water at ~298.15 K

Ten data blocks were found in the ThermoML database containing dynamic viscosity (GLOBprop_4) measurements for binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) mixtures near 298.15 K. The three blocks with the best composition coverage are detailed below, followed by a summary of additional blocks.

---

##### Best Blocks (Inspected)

**1. GLOBlit_2825 / PROPblock_11** — DOI: 10.1016/j.jct.2007.05.004

- **Total points:** 37 (full block)
- **Temperature range:** 293.15–303.15 K
- **Composition variable:** mole fraction of water, range 0–1
- **Viscosity range:** 0.000797–0.002705 Pa·s
- **Pressure:** 101.0 kPa (constrained)

Representative data at exactly 298.15 K (8 of 37 points shown):

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0」 | 「0.001082」 |
| WM_L1#1_Table#1_Row#2 | 「0.0501」 | 「0.001153」 |
| WM_L1#1_Table#1_Row#3 | 「0.0986」 | 「0.001232」 |
| WM_L1#1_Table#1_Row#4 | 「0.1961」 | 「0.001380」 |
| WM_L1#1_Table#1_Row#5 | 「0.2961」 | 「0.001531」 |
| WM_L1#1_Table#1_Row#6 | 「0.3991」 | 「0.001659」 |
| WM_L1#1_Table#1_Row#7 | 「0.5989」 | 「0.002115」 |
| WM_L1#1_Table#1_Row#8 | 「0.6991」 | 「0.002275」 |

This block spans the full mole-fraction range (0 to 1) and provides excellent composition coverage across multiple temperatures.

---

**2. GLOBlit_5201 / PROPblock_21** — DOI: 10.1016/j.jct.2018.02.022

- **Total points:** 100 (full block)
- **Temperature range:** 293.15–308.15 K
- **Composition variable:** mole fraction of ethanol, range 0–1
- **Viscosity range:** 0.00075887–0.0028641 Pa·s
- **Pressure:** 92.3 kPa (constrained)

Representative data at exactly 298.15 K (8 of 100 points shown):

**WM_L1#1_Table#2_(Analysis_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0.0201」 | 「0.001098」 |
| WM_L1#1_Table#2_Row#2 | 「0.0408」 | 「0.0013359」 |
| WM_L1#1_Table#2_Row#3 | 「0.0497」 | 「0.0014322」 |
| WM_L1#1_Table#2_Row#4 | 「0.0600」 | 「0.0015515」 |
| WM_L1#1_Table#2_Row#5 | 「0.0796」 | 「0.001748」 |
| WM_L1#1_Table#2_Row#6 | 「0.1004」 | 「0.0019469」 |
| WM_L1#1_Table#2_Row#7 | 「0.1499」 | 「0.0022424」 |
| WM_L1#1_Table#2_Row#8 | 「0.1984」 | 「0.0023706」 |

This is the largest dataset by raw point count (100 points) and covers nearly the full composition range. The 298.15 K isotherm extends beyond the 8 rows shown here.

---

**3. GLOBlit_7676 / PROPblock_18** — DOI: 10.1021/acs.jced.8b00939

- **Total points:** 9
- **Temperature:** 298.2 K (constrained)
- **Composition variable:** mass fraction of water, range 0.061–0.62
- **Viscosity range:** 0.00131–0.00234 Pa·s
- **Pressure:** 100.0 kPa (constrained)

Data at 298.2 K (8 of 9 points shown):

**WM_L1#1_Table#3_(Analysis_L1#1_Answer):**

| *row_id* | *w(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0.061」 | 「0.00131」 |
| WM_L1#1_Table#3_Row#2 | 「0.124」 | 「0.00146」 |
| WM_L1#1_Table#3_Row#3 | 「0.172」 | 「0.00164」 |
| WM_L1#1_Table#3_Row#4 | 「0.233」 | 「0.00180」 |
| WM_L1#1_Table#3_Row#5 | 「0.276」 | 「0.00187」 |
| WM_L1#1_Table#3_Row#6 | 「0.340」 | 「0.00190」 |
| WM_L1#1_Table#3_Row#7 | 「0.410」 | 「0.00219」 |
| WM_L1#1_Table#3_Row#8 | 「0.500」 | 「0.00231」 |

All points are at the constrained temperature of 298.2 K, with viscosity monotonically increasing with water mass fraction over this range.

---

##### Additional Blocks Found (Not Inspected — No Numerical Details Available)

The following blocks were returned by the discovery search but were not individually inspected in this run. No specific numerical values are quoted for them.

**WM_L1#1_Table#4_(Analysis_L1#1_Answer):**

| *row_id* | *DOI* | *Block* | *GLOBlit* | *Brief Description* |
|---|---|---|---|---|
| WM_L1#1_Table#4_Row#1 | 「10.1021/acs.jced.7b00299」 | 「PROPblock_11」 | 「GLOBlit_7178」 | 「Small dataset, molality-based composition」 |
| WM_L1#1_Table#4_Row#2 | 「10.1021/acs.jced.8b00086」 | 「PROPblock_47」 | 「GLOBlit_7448」 | 「Mass-fraction-based, partial composition range」 |
| WM_L1#1_Table#4_Row#3 | 「10.1021/je4003515」 | 「PROPblock_8」 | 「GLOBlit_10159」 | 「Molality-based, multiple temperatures」 |
| WM_L1#1_Table#4_Row#4 | 「10.1021/je600565m」 | 「PROPblock_5」 | 「GLOBlit_10699」 | 「Details not inspected」 |

Plus 3 additional blocks from the original search whose details were truncated.

---

##### Chemistry Insight

The inspected data from GLOBlit_2825 / PROPblock_11 clearly show the well-known non-ideal viscosity behavior of ethanol–water mixtures. At 298.15 K, viscosity increases substantially as water is added to ethanol — from 0.001082 Pa·s for pure ethanol (x(water) = 0) to 0.002275 Pa·s at x(water) = 0.6991. The full-block statistics for GLOBlit_5201 / PROPblock_21 show viscosity reaching up to 0.0028641 Pa·s across the entire composition range, consistent with a viscosity maximum in the intermediate composition region. This behavior arises from enhanced hydrogen-bonding interactions between ethanol and water molecules in the mixture.

**Recommended blocks for comprehensive analysis:** GLOBlit_2825 / PROPblock_11 (full x = 0–1 coverage, 37 points) and GLOBlit_5201 / PROPblock_21 (100 points, nearly full composition range).

**Core claims:**
- Ten ThermoML data blocks were identified containing dynamic viscosity measurements for binary ethanol + water mixtures near 298.15 K, of which three were inspected in detail.
- GLOBlit_2825 / PROPblock_11 (DOI: 10.1016/j.jct.2007.05.004) provides 37 points spanning the full water mole-fraction range 0–1 at 101.0 kPa across 293.15–303.15 K, with viscosity ranging from 0.000797 to 0.002705 Pa·s.
- GLOBlit_5201 / PROPblock_21 (DOI: 10.1016/j.jct.2018.02.022) is the largest dataset with 100 points covering nearly the full ethanol mole-fraction range at 92.3 kPa across 293.15–308.15 K, with viscosity ranging from 0.00075887 to 0.0028641 Pa·s.
- GLOBlit_7676 / PROPblock_18 (DOI: 10.1021/acs.jced.8b00939) provides 9 points at 298.2 K and 100.0 kPa with water mass fraction 0.061–0.62 and viscosity 0.00131–0.00234 Pa·s, showing viscosity monotonically increasing with water mass fraction over that range.
- At 298.15 K in GLOBlit_2825, viscosity increases from 0.001082 Pa·s for pure ethanol (x(water) = 0) to 0.002275 Pa·s at x(water) = 0.6991, and the full-range data from GLOBlit_5201 show viscosity reaching up to 0.0028641 Pa·s, consistent with a viscosity maximum in the intermediate composition region attributed to enhanced hydrogen-bonding interactions between ethanol and water.
- Seven additional data blocks were identified but not inspected, so no numerical details are available for them.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#5 | 「GLOBlit_2825」 | 「PROPblock_11」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture at 293.15–303.15 K, mole fraction of water 0–1, 37 points, 101.0 kPa.」 |
| WM_L1#1_Table#6 | 「GLOBlit_5201」 | 「PROPblock_21」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture at 293.15–308.15 K, mole fraction of ethanol 0–1, 100 points, 92.3 kPa.」 |
| WM_L1#1_Table#7 | 「GLOBlit_7676」 | 「PROPblock_18」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture at 298.2 K, mass fraction of water 0.061–0.62, 9 points, 100.0 kPa.」 |
| WM_L1#1_Table#8 | 「GLOBlit_7178」 | 「PROPblock_11」 | 「GLOBcomp_1, GLOBcomp_2」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture; molality-based composition, small dataset.」 |
| WM_L1#1_Table#9 | 「GLOBlit_7448」 | 「PROPblock_47」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture; mass-fraction-based, partial composition range.」 |
| WM_L1#1_Table#10 | 「GLOBlit_10159」 | 「PROPblock_8」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture; molality-based, multiple temperatures.」 |
| WM_L1#1_Table#11 | 「GLOBlit_10699」 | 「PROPblock_5」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture; details not inspected.」 |

*Not stored here: 3 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_2825 | 10.1016/j.jct.2007.05.004 | PROPblock_11: 37 rows; x=['mole_fraction_<water>']; y=['viscosity_pa_s']
    - BLKprop_1 / GLOBprop_4: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_4: kind=direct; materialize_reference=False; supported=True; units=Pa*s -> Pa*s

### Completed Fits
  - ethanol_water_GLOBlit_2825 [10.1016/j.jct.2007.05.004/PROPblock_11] (water, ethanol): RK order=5, R²=0.999408, RMSE=0.006911011918291117, coeffs=[2.57153, 2.710634, 3.054789, 1.014728, 0.587547, 1.218457]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: water=0.00089, ethanol=0.001082 [block-edges (ethanol: direct/good, water: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_11_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_11_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_11_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_11_T298.1_excess.png
  - ethanol_water_GLOBlit_5201 [10.1016/j.jct.2018.02.022/PROPblock_21] (ethanol, water): RK order=4, R²=0.999334, RMSE=0.006612838327445672, coeffs=[2.727996, -2.492594, 2.550047, -2.44775, 1.536444]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: ethanol=0.0010914, water=0.00089689 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_11_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2007.05.004 PROPblock_11_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1
- `$ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_11_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2007.05.004 PROPblock_11_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1

### plot
- `$ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_11_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2007.05.004 PROPblock_11_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1
- `$ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_11_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2007.05.004 PROPblock_11_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1

