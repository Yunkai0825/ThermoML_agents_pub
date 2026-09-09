# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_194722_684644_49ae3f02\analysis_runs\run_1`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_1 | water | 0.00089689 |
| comp | GLOBcomp_24 | 1,2-ethanediol | 0.016223 |
| prop | GLOBprop_40 | kinematic viscosity, m2/s |  |
| prop | GLOBprop_4 | viscositypas |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<1,2-ethanediol> |  |
| constr | GLOBconstr_1 | pressurekpa |  |

### History
- [query_thermoml]
- [inspect_block]
- [fit_block] ERROR: Requested x column 'Mole fraction of 1,2-ethanediol' not found in block
- [fit_block]

### Query Results
#### query
**L1_query_1** — status: success · validation: FLAGGED(2)

**Summary:** Dynamic viscosity data for the binary water + ethylene glycol (1,2-ethanediol) system near 298.15 K were found in 7 ThermoML blocks; no kinematic viscosity data were found. The largest dataset is from GLOBlit_5201 (DOI 10.1016/j.jct.2018.02.022, PROPblock_24) with 84 points spanning 293.15–308.15 K over the full composition range (mole fraction EG 0–1), viscosity 0.00075887–0.020613 Pa·s at 92.3 kPa. GLOBlit_6951 (DOI 10.1021/acs.jced.6b00526, PROPblock_18) provides 33 points at 293.15–303.15 K, mole fraction water 0–1, viscosity 0.000755–0.02113 Pa·s at 100 kPa. GLOBlit_8038 (DOI 10.1021/je020140j, PROPblock_5) gives 77 points over 293.15–353.15 K, mole fraction EG 0–1, viscosity 0.000356–0.020833 Pa·s at 101 kPa. GLOBlit_8106 (DOI 10.1021/je025610o, PROPblock_5) has 30 points at mole fraction EG 0.25, 0.5, and 0.75 over 296.45–449.85 K, viscosity 0.000366–0.0123 Pa·s at 100.0 kPa. GLOBlit_2656 (DOI 10.1016/j.jct.2006.01.011, PROPblock_13) contains 10 points at 293.15 K, mass fraction EG 0–0.9, viscosity 0.001008–0.013999 Pa·s at 101.325 kPa. GLOBlit_11186 (DOI 10.1021/je800271e, PROPblock_4) covers 308.15–323.15 K with 52 points, mole fraction EG 0–1, viscosity 0.00055–0.0092122 Pa·s. The system exhibits a strong positive viscosity deviation from ideal mixing, attributed to extensive hydrogen bonding between ethylene glycol and water.

**Answer:**

#### Viscosity Data for Binary Water + Ethylene Glycol System Near 298.15 K

**Compounds:** Water (GLOBcomp_1) + 1,2-Ethanediol / Ethylene Glycol (GLOBcomp_24)

**Properties searched:** Dynamic viscosity (GLOBprop_4) and Kinematic viscosity (GLOBprop_40)

##### Results

**Dynamic viscosity (GLOBprop_4):** 7 blocks found in the binary system within the 290–310 K search window.

**Kinematic viscosity (GLOBprop_40):** No blocks found for this system in the database.

##### Block Details (from inspections)

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *#* | *DOI* | *Block* | *GLOBlit* | *Data Points* | *T Range (K)* | *Composition Variable & Range* | *P (kPa)* |
|---|---|---|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「1」 | 「10.1016/j.jct.2006.01.011」 | 「PROPblock_13」 | 「GLOBlit_2656」 | 「10」 | 「293.15–293.15」 | 「mass fraction EG: 0–0.9」 | 「101.325」 |
| WM_L1#1_Table#1_Row#2 | 「2」 | 「10.1016/j.jct.2018.02.022」 | 「PROPblock_24」 | 「GLOBlit_5201」 | 「84」 | 「293.15–308.15」 | 「mole fraction EG: 0–1」 | 「92.3」 |
| WM_L1#1_Table#1_Row#3 | 「3」 | 「10.1021/acs.jced.6b00526」 | 「PROPblock_18」 | 「GLOBlit_6951」 | 「33」 | 「293.15–303.15」 | 「mole fraction water: 0–1」 | 「100」 |
| WM_L1#1_Table#1_Row#4 | 「4」 | 「10.1021/je020140j」 | 「PROPblock_5」 | 「GLOBlit_8038」 | 「77」 | 「293.15–353.15」 | 「mole fraction EG: 0–1」 | 「101」 |
| WM_L1#1_Table#1_Row#5 | 「5」 | 「10.1021/je025610o」 | 「PROPblock_5」 | 「GLOBlit_8106」 | 「30」 | 「296.45–449.85」 | 「mole fraction EG: 0.25–0.75」 | 「100.0」 |
| WM_L1#1_Table#1_Row#6 | 「6」 | 「10.1021/je800271e」 | 「PROPblock_4」 | 「GLOBlit_11186」 | 「52」 | 「308.15–323.15」 | 「mole fraction EG: 0–1」 | 「(not reported)」 |

(A 7th block was indicated in the search but its details were truncated in the search results.)

##### Key Observations

- The largest dataset near 298.15 K is from GLOBlit_5201 (DOI: 10.1016/j.jct.2018.02.022, PROPblock_24) with 84 data points spanning 293.15–308.15 K and the full composition range (mole fraction EG 0–1), with viscosity values ranging from 0.00075887 to 0.020613 Pa·s.
- GLOBlit_6951 (DOI: 10.1021/acs.jced.6b00526, PROPblock_18) covers the full composition range (mole fraction water 0–1) with 33 points at 293.15–303.15 K, viscosity 0.000755–0.02113 Pa·s.
- GLOBlit_8038 (DOI: 10.1021/je020140j, PROPblock_5) provides 77 points over 293.15–353.15 K with mole fraction EG 0–1, viscosity 0.000356–0.020833 Pa·s.
- GLOBlit_8106 (DOI: 10.1021/je025610o, PROPblock_5) has 30 points at three compositions (mole fraction EG 0.25, 0.5, 0.75) over 296.45–449.85 K, viscosity 0.000366–0.0123 Pa·s.
- GLOBlit_2656 (DOI: 10.1016/j.jct.2006.01.011, PROPblock_13) is at a single temperature (293.15 K) with 10 points across mass fraction EG 0–0.9, viscosity 0.001008–0.013999 Pa·s.
- GLOBlit_11186 (DOI: 10.1021/je800271e, PROPblock_4) starts at 308.15 K (52 points, 308.15–323.15 K), above the 298.15 K target, with viscosity 0.00055–0.0092122 Pa·s.

The ethylene glycol–water system shows a strong positive viscosity deviation from ideal mixing, with viscosity increasing substantially as ethylene glycol content rises, consistent with the extensive hydrogen-bonding network formed between the two hydroxyl groups of ethylene glycol and water molecules.

**Core claims:**
- The ThermoML database contains at least 6 identified blocks of dynamic viscosity data for the binary water + ethylene glycol system within the 290–310 K temperature window; no kinematic viscosity blocks were found for this system.
- The largest dataset near 298.15 K is from GLOBlit_5201 (DOI: 10.1016/j.jct.2018.02.022, PROPblock_24) with 84 data points spanning 293.15–308.15 K and the full composition range (mole fraction EG 0–1), with viscosity values ranging from 0.00075887 to 0.020613 Pa·s.
- Multiple independent sources (GLOBlit_5201, GLOBlit_6951, GLOBlit_8038) cover the full composition range of the water–ethylene glycol system at temperatures encompassing 298.15 K, with reported dynamic viscosities spanning roughly 0.000356–0.020833 Pa·s across all compositions and temperatures.
- The ethylene glycol–water system shows a strong positive viscosity deviation from ideal mixing, with viscosity increasing substantially as ethylene glycol content rises, consistent with extensive hydrogen bonding between the two components.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_2656」 | 「PROPblock_13」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of water + ethylene glycol at 293.15 K, 10 points, mass fraction EG 0–0.9.」 |
| WM_L1#1_Table#3 | 「GLOBlit_5201」 | 「PROPblock_24」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of water + ethylene glycol, 84 points, 293.15–308.15 K, mole fraction EG 0–1.」 |
| WM_L1#1_Table#4 | 「GLOBlit_6951」 | 「PROPblock_18」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of water + ethylene glycol, 33 points, 293.15–303.15 K, mole fraction water 0–1.」 |
| WM_L1#1_Table#5 | 「GLOBlit_8038」 | 「PROPblock_5」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of water + ethylene glycol, 77 points, 293.15–353.15 K, mole fraction EG 0–1.」 |
| WM_L1#1_Table#6 | 「GLOBlit_8106」 | 「PROPblock_5」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of water + ethylene glycol, 30 points, 296.45–449.85 K, mole fraction EG 0.25–0.75.」 |
| WM_L1#1_Table#7 | 「GLOBlit_11186」 | 「PROPblock_4」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of water + ethylene glycol, 52 points, 308.15–323.15 K, mole fraction EG 0–1.」 |

*Not stored here: 6 verbatim data_inspections table(s); 4 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **AMBIGUOUS_VALUE** PROPblock_4: 298.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **AMBIGUOUS_VALUE** PROPblock_4: 298.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean


### Inspected Blocks
- GLOBlit_5201 | 10.1016/j.jct.2018.02.022 | PROPblock_24: 84 rows; x=['mole_fraction_<1,2-ethanediol>']; y=['viscosity_pa_s']
    - BLKprop_1 / GLOBprop_4: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_4: kind=direct; materialize_reference=False; supported=True; units=Pa*s -> Pa*s

### Completed Fits
  - 10.1016/j.jct.2018.02.022/PROPblock_24 (1,2-ethanediol, water): RK order=3, R²=0.99994, RMSE=0.0013198945265291695, coeffs=[2.39674, -1.044444, 0.668173, -0.3209]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: 1,2-ethanediol=0.016223, water=0.00089689 [block-edges (water: direct/good, 1,2-ethanediol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1

### plot
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1

