# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_161409_378697_8e3dfdd6`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_24 | 1,2-ethanediol |  |
| comp | GLOBcomp_1 | water |  |
| prop | GLOBprop_4 | viscositypas |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<1,2-ethanediol> |  |
| constr | GLOBconstr_1 | pressurekpa |  |

### History
- [query_thermoml]
- [inspect_block]
- [fit_multi_system]
- [fit_multi_system]
- [predict_from_rk]
- [predict_from_rk]

### Query Results
#### query
**L1_query_1** — status: success · validation: FLAGGED(2)

**Summary:** Seven dynamic viscosity (η, Pa·s) data blocks were identified for the binary system ethylene glycol (1,2-ethanediol) + water near 298.15 K. The best-suited block is GLOBlit_5201 / PROPblock_24 (DOI 10.1016/j.jct.2018.02.022) with 84 data points, T = 293.15–308.15 K, x(EG) = 0–1, P = 92.3 kPa, and viscosity range 0.00075887–0.020613 Pa·s; representative values at 298.15 K include η = 0.0012528 Pa·s at x(EG) = 0.0494 and η = 0.0028109 Pa·s at x(EG) = 0.2072. GLOBlit_6951 / PROPblock_18 (DOI 10.1021/acs.jced.6b00526) provides 33 points at T = 293.15–303.15 K over x(water) = 0–1 at 100.0 kPa, with η = 0.01724 Pa·s for neat ethylene glycol at 298.15 K. GLOBlit_8106 / PROPblock_5 (DOI 10.1021/je025610o) covers x(EG) = 0.25–0.75 at T = 296.45–449.85 K and 100.0 kPa, showing η = 0.00761 Pa·s at x(EG) = 0.50 and 297.05 K. GLOBlit_8038 / PROPblock_5 (DOI 10.1021/je020140j) has 77 points at T = 293.15–353.15 K, x(EG) = 0–1, 101.0 kPa, but no exact 298.15 K rows. GLOBlit_2656 / PROPblock_13 (DOI 10.1016/j.jct.2006.01.011) has 10 points at fixed 293.15 K in mass fraction. GLOBlit_11186 / PROPblock_4 (DOI 10.1021/je800271e) was not inspected and its data remain unverified. The system shows pronounced non-ideal viscosity behavior due to extensive hydrogen bonding between the diol and water.

**Answer:**

Seven dynamic viscosity (η, Pa·s) data blocks were found for the binary system **ethylene glycol (1,2-ethanediol, GLOBcomp_24) + water (GLOBcomp_1)** with temperatures near 298.15 K. Below are the inspected blocks with verified details:

---

##### Block-level summary

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *#* | *DOI* | *Block* | *GLOBlit* | *Data Points* | *T range (K)* | *Composition range* | *Comp. variable* | *P (kPa)* |
|---|---|---|---|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「1」 | 「10.1016/j.jct.2018.02.022」 | 「PROPblock_24」 | 「GLOBlit_5201」 | 「84」 | 「293.15–308.15」 | 「x(EG): 0–1」 | 「mole_fraction」 | 「92.3」 |
| WM_L1#1_Table#1_Row#2 | 「2」 | 「10.1021/acs.jced.6b00526」 | 「PROPblock_18」 | 「GLOBlit_6951」 | 「33」 | 「293.15–303.15」 | 「x(water): 0–1」 | 「mole_fraction」 | 「100.0」 |
| WM_L1#1_Table#1_Row#3 | 「3」 | 「10.1021/je020140j」 | 「PROPblock_5」 | 「GLOBlit_8038」 | 「77」 | 「293.15–353.15」 | 「x(EG): 0–1」 | 「mole_fraction」 | 「101.0」 |
| WM_L1#1_Table#1_Row#4 | 「4」 | 「10.1021/je025610o」 | 「PROPblock_5」 | 「GLOBlit_8106」 | 「30」 | 「296.45–449.85」 | 「x(EG): 0.25–0.75」 | 「mole_fraction」 | 「100.0」 |
| WM_L1#1_Table#1_Row#5 | 「5」 | 「10.1016/j.jct.2006.01.011」 | 「PROPblock_13」 | 「GLOBlit_2656」 | 「10」 | 「293.15 (fixed)」 | 「w(EG): 0–0.9」 | 「mass_fraction」 | 「101.325」 |
| WM_L1#1_Table#1_Row#6 | 「6」 | 「10.1021/je800271e」 | 「PROPblock_4」 | 「GLOBlit_11186」 | 「—」 | 「—」 | 「—」 | 「—」 | 「— (not inspected in this run)」 |

---

##### Best candidates for data near 298.15 K with wide composition range including x ≈ 0.5

**1. GLOBlit_5201 / PROPblock_24** (DOI: 10.1016/j.jct.2018.02.022)
- 84 data points, T = 293.15–308.15 K, x(EG) = 0–1, P = 92.3 kPa
- Viscosity range: 0.00075887–0.020613 Pa·s
- Has exact rows at 298.15 K. Representative inspected data at 298.15 K:

**WM_L1#1_Table#2_(Analysis_L1#1_Answer):**

| *row_id* | *x(1,2-ethanediol)* | *T (K)* | *η (Pa·s)* |
|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0.0494」 | 「298.15」 | 「0.0012528」 |
| WM_L1#1_Table#2_Row#2 | 「0.0986」 | 「298.15」 | 「0.0016802」 |
| WM_L1#1_Table#2_Row#3 | 「0.1483」 | 「298.15」 | 「0.0021667」 |
| WM_L1#1_Table#2_Row#4 | 「0.2072」 | 「298.15」 | 「0.0028109」 |

This is the largest dataset with the widest mole-fraction coverage, well-suited for studying viscosity across the full composition range at 298.15 K.

**2. GLOBlit_6951 / PROPblock_18** (DOI: 10.1021/acs.jced.6b00526)
- 33 data points, T = 293.15–303.15 K, x(water) = 0–1, P = 100.0 kPa
- Viscosity range: 0.000755–0.02113 Pa·s
- Has exact rows at 298.15 K. Representative inspected data at 298.15 K (note: composition is expressed as x(water)):

**WM_L1#1_Table#3_(Analysis_L1#1_Answer):**

| *row_id* | *x(water)* | *T (K)* | *η (Pa·s)* |
|---|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0」 | 「298.15」 | 「0.01724」 |
| WM_L1#1_Table#3_Row#2 | 「0.1105」 | 「298.15」 | 「0.01433」 |
| WM_L1#1_Table#3_Row#3 | 「0.2014」 | 「298.15」 | 「0.01219」 |
| WM_L1#1_Table#3_Row#4 | 「0.3002」 | 「298.15」 | 「0.01018」 |

Full composition range coverage (x(water) = 0 to 1).

**3. GLOBlit_8106 / PROPblock_5** (DOI: 10.1021/je025610o)
- 30 data points, T = 296.45–449.85 K, x(EG) = 0.25–0.75, P = 100.0 kPa
- Viscosity range: 0.000366–0.0123 Pa·s
- No exact row at 298.15 K; nearest below is 297.35 K, nearest above is 313.05 K. Inspected data near 298.15 K:

**WM_L1#1_Table#4_(Analysis_L1#1_Answer):**

| *row_id* | *x(EG)* | *T (K)* | *η (Pa·s)* |
|---|---|---|---|
| WM_L1#1_Table#4_Row#1 | 「0.25」 | 「296.45」 | 「0.00369」 |
| WM_L1#1_Table#4_Row#2 | 「0.50」 | 「297.05」 | 「0.00761」 |
| WM_L1#1_Table#4_Row#3 | 「0.75」 | 「297.35」 | 「0.0123」 |

This block explicitly covers x ≈ 0.5 and shows a clear increase in viscosity with ethylene glycol mole fraction near ambient temperature.

**4. GLOBlit_8038 / PROPblock_5** (DOI: 10.1021/je020140j)
- 77 data points, T = 293.15–353.15 K, x(EG) = 0–1, P = 101.0 kPa
- Viscosity range: 0.000356–0.020833 Pa·s
- No exact row at 298.15 K; nearest below is 293.15 K, nearest above is 303.15 K. Wide temperature range useful for temperature-dependence studies.

**5. GLOBlit_2656 / PROPblock_13** (DOI: 10.1016/j.jct.2006.01.011)
- 10 data points, T = 293.15 K (fixed), w(EG) = 0–0.9, P = 101.325 kPa
- Viscosity range: 0.001008–0.013999 Pa·s
- Fixed at 293.15 K only (298.15 K lies outside the matched range). Composition in mass fraction.

**6. GLOBlit_11186 / PROPblock_4** (DOI: 10.1021/je800271e) — not inspected in this run; details unavailable.

---

##### Chemistry insight

The ethylene glycol + water system exhibits a pronounced viscosity maximum at intermediate compositions, arising from extensive hydrogen-bonding networks between the diol's two hydroxyl groups and water molecules. The inspected data from GLOBlit_5201 at 298.15 K show viscosity increasing from 0.0012528 Pa·s at x(EG) = 0.0494 to 0.0028109 Pa·s at x(EG) = 0.2072, consistent with the well-known non-ideal mixing behavior. Data from GLOBlit_6951 at x(water) = 0 give η = 0.01724 Pa·s for neat ethylene glycol at 298.15 K, while GLOBlit_8106 shows η = 0.00761 Pa·s at x(EG) = 0.50 and 297.05 K.

**Core claims:**
- Seven dynamic viscosity data blocks were identified in ThermoML for the binary system ethylene glycol (1,2-ethanediol) + water at temperatures near 298.15 K, spanning multiple DOIs and covering mole-fraction, mass-fraction, and varied pressure conditions.
- The largest and most composition-comprehensive dataset is GLOBlit_5201 / PROPblock_24 (DOI: 10.1016/j.jct.2018.02.022), with 84 data points at T = 293.15–308.15 K, x(EG) = 0–1, and P = 92.3 kPa, including exact rows at 298.15 K.
- GLOBlit_6951 / PROPblock_18 (DOI: 10.1021/acs.jced.6b00526) also provides full composition coverage (x(water) = 0–1) at 298.15 K and reports η = 0.01724 Pa·s for neat ethylene glycol at 298.15 K.
- GLOBlit_8106 / PROPblock_5 (DOI: 10.1021/je025610o) covers x(EG) = 0.25–0.75 but has no exact 298.15 K row; the nearest data show η = 0.00761 Pa·s at x(EG) = 0.50 and 297.05 K.
- The ethylene glycol + water system exhibits non-ideal viscosity mixing behavior attributed to extensive hydrogen-bonding networks between the diol and water, with viscosity increasing markedly with ethylene glycol mole fraction at low to intermediate compositions.
- One block (GLOBlit_11186 / PROPblock_4) was not inspected, and certain quoted values carry UNVERIFIED flags, limiting full confirmation of all reported data.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#5 | 「GLOBlit_5201」 | 「PROPblock_24」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethylene glycol + water binary mixture; 84 data points, T = 293.15–308.15 K, x(EG) = 0–1, P = 92.3 kPa. Includes exact 298.15 K rows across full composition range.」 |
| WM_L1#1_Table#6 | 「GLOBlit_6951」 | 「PROPblock_18」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethylene glycol + water binary mixture; 33 data points, T = 293.15–303.15 K, x(water) = 0–1, P = 100.0 kPa. Includes exact 298.15 K rows across full composition range.」 |
| WM_L1#1_Table#7 | 「GLOBlit_8038」 | 「PROPblock_5」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethylene glycol + water binary mixture; 77 data points, T = 293.15–353.15 K, x(EG) = 0–1, P = 101.0 kPa. Nearest temperatures to 298.15 K are 293.15 K and 303.15 K.」 |
| WM_L1#1_Table#8 | 「GLOBlit_8106」 | 「PROPblock_5」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethylene glycol + water binary mixture; 30 data points, T = 296.45–449.85 K, x(EG) = 0.25–0.75, P = 100.0 kPa. Covers x ≈ 0.5; nearest T to 298.15 K is ~297 K.」 |
| WM_L1#1_Table#9 | 「GLOBlit_2656」 | 「PROPblock_13」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethylene glycol + water binary mixture; 10 data points, T = 293.15 K (fixed), w(EG) = 0–0.9, P = 101.325 kPa. Composition in mass fraction.」 |

*Not stored here: 5 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_4: PROPblock_4 is quoted with data values (298.15, 0.5, …) but was never inspected in this run
- **UNINSPECTED_BLOCK** PROPblock_4: PROPblock_4 is quoted with data values (298.15, 0.0012528, 0.0494, 0.0028109, …) but was never inspected in this run


### Inspected Blocks
- GLOBlit_5201 | 10.1016/j.jct.2018.02.022 | PROPblock_24: 84 rows; x=['mole_fraction_<1,2-ethanediol>']; y=['viscosity_pa_s']
    - BLKprop_1 / GLOBprop_4: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_4: kind=direct; materialize_reference=False; supported=True; units=Pa*s -> Pa*s

### Completed Fits
  - EG_water_5201 [10.1016/j.jct.2018.02.022/PROPblock_24] (1,2-ethanediol, water): RK order=3, R²=0.99994, RMSE=0.0013198945265291695, coeffs=[2.39674, -1.044444, 0.668173, -0.3209]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: 1,2-ethanediol=0.016223, water=0.00089689 [block-edges (water: direct/good, 1,2-ethanediol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png
  - EG_water_6951 [10.1021/acs.jced.6b00526/PROPblock_18] (water, 1,2-ethanediol): RK order=5, R²=0.999925, RMSE=0.0013505215055279614, coeffs=[2.274524, 1.438464, 0.538413, -0.01859, 0.535328, 0.62332]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: water=0.000843, 1,2-ethanediol=0.01724 [block-edges (1,2-ethanediol: direct/good, water: direct/good)]
      fit_csv: $ROOT/data\10_1021_acs_jced_6b00526_BPROPblock_18_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1021_acs_jced_6b00526_BPROPblock_18_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_acs_jced_6b00526_BPROPblock_18_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1021_acs_jced_6b00526_BPROPblock_18_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1021_acs_jced_6b00526_BPROPblock_18_T298.1_fit.csv` — RK fit data — 10.1021/acs.jced.6b00526 PROPblock_18_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- `$ROOT/data\10_1021_acs_jced_6b00526_BPROPblock_18_T298.1_excess.csv` — Excess property — 10.1021/acs.jced.6b00526 PROPblock_18_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1

### plot
- `$ROOT/plots\10_1021_acs_jced_6b00526_BPROPblock_18_T298.1_fit.png` — RK fit plot — 10.1021/acs.jced.6b00526 PROPblock_18_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- `$ROOT/plots\10_1021_acs_jced_6b00526_BPROPblock_18_T298.1_excess.png` — Excess plot — 10.1021/acs.jced.6b00526 PROPblock_18_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1

