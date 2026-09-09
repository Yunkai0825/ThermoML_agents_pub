# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_023326_012061_3dba9dd4\analysis_runs\run_4`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_1 | water | 1.8110836e-05 |
| comp | GLOBcomp_2 | ethanol | 5.8206813e-05 |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<ethanol> |  |
| constr | GLOBconstr_1 | pressurekpa |  |

### History
- [query_thermoml_parallel]
- [inspect_block]
- [fit_block_derived] ERROR: Unknown transform 'density_to_excess_molar_volume'. Available: ['density_to_mola
- [fit_block_derived] ERROR: Constraint column 'Temperature, K' not found
- [fit_block_derived]
- [predict_from_rk]
- [fit_block_derived]
- [predict_from_rk]
- [list_session_files]
- [inspect_block]
- [inspect_block]

### Query Results
#### VE_direct
**L1_query_1** — status: no_results · validation: PASS

**Summary:** A comprehensive search of the ThermoML database for excess molar volume (V^E) data for the binary system water (CAS 7732-18-5) + ethanol (CAS 64-17-5) at 298.15 K found no results. The database contains 50 data blocks for this binary pair, but none report excess molar volume. Available properties for this system include mass density (12 blocks), excess molar enthalpy (5 blocks), boiling temperature (9 blocks), vapor/sublimation pressure (5 blocks), mole fraction VLE (8 blocks), activity coefficient (4 blocks), viscosity (4 blocks), speed of sound (1 block), and relative permittivity (1 block).

**Answer:**

**Excess molar volume (V^E) data for water + ethanol at 298.15 K: Not found in the ThermoML database.**

A comprehensive search was conducted for the binary system water (GLOBcomp_1, CAS 7732-18-5) + ethanol (GLOBcomp_2, CAS 64-17-5) with the property excess molar volume (GLOBprop_28). No data blocks were found — neither as declared binary systems nor as subsystems of higher-order mixtures.

The ThermoML database does contain data for the water + ethanol binary system, but for other properties. Among the 50 blocks found for this pair, the available properties include:

- **Mass density** (kg/m³) — 12 blocks (e.g., DOI 10.1016/j.fluid.2004.11.019 [GLOBlit_220]/PROPblock_2)
- **Excess molar enthalpy** (kJ/mol) — 5 blocks (e.g., DOI 10.1016/j.fluid.2007.06.007 [GLOBlit_528]/PROPblock_1)
- **Boiling temperature** (K) — 9 blocks
- **Vapor/sublimation pressure** (kPa) — 5 blocks
- **Mole fraction** (VLE) — 8 blocks
- **Activity coefficient** — 4 blocks
- **Viscosity** (Pa·s) — 4 blocks
- **Speed of sound** (m/s) — 1 block
- **Relative permittivity** — 1 block

No excess molar volume (V^E) data is available for this system in the database.

**Core claims:**
- No excess molar volume (V^E) data for the water + ethanol binary system at 298.15 K were found in the ThermoML database.
- The ThermoML database does contain data for the water + ethanol binary system for other properties, including mass density, excess molar enthalpy, boiling temperature, vapor/sublimation pressure, mole fraction (VLE), activity coefficient, viscosity, speed of sound, and relative permittivity, across 50 data blocks.

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### density_data
**L1_query_2** — status: success · validation: FLAGGED(3)

**Summary:** Seventeen ThermoML data blocks report mass density (kg/m³) for the binary water (CAS 7732-18-5) + ethanol (CAS 64-17-5) system near 298.15 K. Three blocks were individually inspected. The richest is GLOBlit_220::PROPblock_2 (810 points), which at 298.15 K and 100 kPa spans x(ethanol) = 0.003–1 with density from 995.3 to 785.7 kg/m³; at 298.15 K it covers pressures from 100 to 40000 kPa across 270 points. GLOBlit_5201::PROPblock_19 (244 points) provides data at 92.3 kPa across four temperatures (293.15–308.15 K) with x(ethanol) = 0–1; at 298.15 K representative values range from 997.267 kg/m³ (pure water) to 785.26 kg/m³ (pure ethanol). GLOBlit_2432::PROPblock_2 (565 points) uses molality as the composition variable and reports negative density values (range −19.634 to −0.7809 kg/m³), likely excess or relative density differences, making it less suitable for absolute density. Both absolute-density datasets show monotonic decrease from pure water toward pure ethanol at 298.15 K. Fourteen additional blocks were identified but not individually inspected; their data point counts and contents remain unverified.

**Answer:**

#### Binary Water + Ethanol Mass Density Data near 298.15 K

**Compounds:** Water (GLOBcomp_1, CAS 7732-18-5) + Ethanol (GLOBcomp_2, CAS 64-17-5)  
**Property:** Mass density (GLOBprop_1, kg/m³)  
**System type:** Binary, liquid phase

##### Available Blocks (T ≈ 295–301 K)

17 data blocks were found in the ThermoML database. The three largest blocks were individually inspected; the remaining 14 blocks were identified via the registry search but not individually inspected in this run. Data point counts for the uninspected blocks are from the registry search results.

###### Inspected Blocks

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *#* | *DOI* | *GLOBlit* | *Block* | *Data Points* |
|---|---|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「1」 | 「10.1016/j.fluid.2004.11.019」 | 「GLOBlit_220」 | 「PROPblock_2」 | 「810」 |
| WM_L1#2_Table#1_Row#2 | 「2」 | 「10.1016/j.jct.2004.07.019」 | 「GLOBlit_2432」 | 「PROPblock_2」 | 「565」 |
| WM_L1#2_Table#1_Row#3 | 「3」 | 「10.1016/j.jct.2018.02.022」 | 「GLOBlit_5201」 | 「PROPblock_19」 | 「244」 |

###### Additional Blocks (not individually inspected in this run)

**WM_L1#2_Table#2_(Analysis_L1#2_Answer):**

| *row_id* | *#* | *DOI* | *GLOBlit* | *Block* | *Data Points (from registry)* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「4」 | 「10.1021/je060335h」 | 「GLOBlit_9006」 | 「PROPblock_1」 | 「(not individually inspected)」 |
| WM_L1#2_Table#2_Row#2 | 「5」 | 「10.1016/j.fluid.2014.05.032」 | 「GLOBlit_1483」 | 「PROPblock_1」 | 「(not individually inspected)」 |
| WM_L1#2_Table#2_Row#3 | 「6」 | 「10.1021/je800150h」 | 「GLOBlit_11136」 | 「PROPblock_9」 | 「(not individually inspected)」 |
| WM_L1#2_Table#2_Row#4 | 「7」 | 「10.1021/je700300y」 | 「GLOBlit_10866」 | 「PROPblock_7」 | 「(not individually inspected)」 |
| WM_L1#2_Table#2_Row#5 | 「8」 | 「10.1016/j.jct.2011.10.009」 | 「GLOBlit_3475」 | 「PROPblock_3」 | 「70」 |
| WM_L1#2_Table#2_Row#6 | 「9」 | 「10.1016/j.jct.2015.06.024」 | 「GLOBlit_4415」 | 「PROPblock_7」 | 「40」 |
| WM_L1#2_Table#2_Row#7 | 「10」 | 「10.1016/j.jct.2007.05.004」 | 「GLOBlit_2825」 | 「PROPblock_12」 | 「(not individually inspected)」 |
| WM_L1#2_Table#2_Row#8 | 「11」 | 「10.1021/je020173z」 | 「GLOBlit_8050」 | 「PROPblock_5」 | 「(not individually inspected)」 |
| WM_L1#2_Table#2_Row#9 | 「12」 | 「10.1021/je4003515」 | 「GLOBlit_10159」 | 「PROPblock_7」 | 「23」 |
| WM_L1#2_Table#2_Row#10 | 「13」 | 「10.1021/je600565m」 | 「GLOBlit_10699」 | 「PROPblock_6」 | 「18」 |
| WM_L1#2_Table#2_Row#11 | 「14」 | 「10.1021/je900743e」 | 「GLOBlit_11792」 | 「PROPblock_3」 | 「15」 |
| WM_L1#2_Table#2_Row#12 | 「15」 | 「10.1021/acs.jced.6b01058」 | 「GLOBlit_7085」 | 「PROPblock_7」 | 「(not individually inspected)」 |
| WM_L1#2_Table#2_Row#13 | 「16」 | 「10.1021/je900064e」 | 「GLOBlit_11504」 | 「PROPblock_6」 | 「(not individually inspected)」 |
| WM_L1#2_Table#2_Row#14 | 「17」 | 「10.1021/acs.jced.7b00299」 | 「GLOBlit_7178」 | 「PROPblock_10」 | 「(not individually inspected)」 |

##### Best Candidates for Full Composition Coverage

**GLOBlit_220::PROPblock_2** (810 total points) is the richest dataset. At exactly 298.15 K, there are 270 data points spanning x(ethanol) = 0.003–1 and pressures from 100 to 40000 kPa, with mass density ranging from 785.7 to 1012.7 kg/m³. At atmospheric pressure (100 kPa) and 298.15 K, representative values include:

**WM_L1#2_Table#3_(Analysis_L1#2_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#3_Row#1 | 「0.003」 | 「995.3」 |
| WM_L1#2_Table#3_Row#2 | 「0.2502」 | 「918.5」 |
| WM_L1#2_Table#3_Row#3 | 「0.4501」 | 「868.8」 |
| WM_L1#2_Table#3_Row#4 | 「0.6967」 | 「825.2」 |
| WM_L1#2_Table#3_Row#5 | 「1」 | 「785.7」 |

**GLOBlit_5201::PROPblock_19** (244 points) provides data at 92.3 kPa across four temperatures (293.15–308.15 K) with x(ethanol) = 0–1. At 298.15 K, representative values include:

**WM_L1#2_Table#4_(Analysis_L1#2_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#4_Row#1 | 「0」 | 「997.267」 |
| WM_L1#2_Table#4_Row#2 | 「0.1984」 | 「931.84」 |
| WM_L1#2_Table#4_Row#3 | 「0.4495」 | 「869.34」 |
| WM_L1#2_Table#4_Row#4 | 「0.7006」 | 「825.07」 |
| WM_L1#2_Table#4_Row#5 | 「1」 | 「785.26」 |

**Note on GLOBlit_2432::PROPblock_2** (565 points): This block uses molality (mol/kg) as the composition variable and reports negative density values (range: −19.634 to −0.7809 kg/m³, likely relative or excess density differences), so it is less suitable for obtaining absolute density as a function of mole fraction.

**Chemistry note:** Both inspected absolute-density datasets show a monotonic decrease in density from pure water (995.3–997.267 kg/m³) toward pure ethanol (785.26–785.7 kg/m³) at 298.15 K, consistent with the well-known non-ideal mixing behavior of this system.

**Core claims:**
- 17 ThermoML data blocks were identified for binary water + ethanol mass density near 298.15 K, but only three were individually inspected in this run; 14 blocks remain uninspected.
- GLOBlit_220::PROPblock_2 is the richest inspected dataset (810 total points), with 270 points at exactly 298.15 K spanning x(ethanol) = 0.003–1 and pressures from 100 to 40000 kPa, yielding mass densities from 785.7 to 1012.7 kg/m³.
- GLOBlit_5201::PROPblock_19 (244 points) provides absolute density data at 92.3 kPa and 298.15 K across x(ethanol) = 0–1, with density ranging from 997.267 kg/m³ (pure water) to 785.26 kg/m³ (pure ethanol).
- GLOBlit_2432::PROPblock_2 (565 points) reports negative density values (range: −19.634 to −0.7809 kg/m³), likely relative or excess density differences, making it less suitable for obtaining absolute density as a function of mole fraction.
- Both inspected absolute-density datasets show a monotonic decrease in density from pure water toward pure ethanol at 298.15 K, consistent with the well-known non-ideal mixing behavior of this system.
- Multiple data values and block-level details for the 14 uninspected blocks remain unverified, and some values were flagged as misattributed between blocks, limiting confidence in the completeness and attribution accuracy of the full survey.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#5 | 「GLOBlit_220」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol at 298.15 K; 810 data points spanning x(ethanol) = 0.003–1 and pressures 100–40000 kPa.」 |
| WM_L1#2_Table#6 | 「GLOBlit_2432」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density (relative/excess) for water + ethanol; 565 data points using molality composition variable with negative density values.」 |
| WM_L1#2_Table#7 | 「GLOBlit_5201」 | 「PROPblock_19」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol at 92.3 kPa across 293.15–308.15 K; 244 data points spanning x(ethanol) = 0–1.」 |
| WM_L1#2_Table#8 | 「GLOBlit_9006」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol (not individually inspected).」 |
| WM_L1#2_Table#9 | 「GLOBlit_1483」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol (not individually inspected).」 |
| WM_L1#2_Table#10 | 「GLOBlit_11136」 | 「PROPblock_9」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol (not individually inspected).」 |
| WM_L1#2_Table#11 | 「GLOBlit_10866」 | 「PROPblock_7」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol (not individually inspected).」 |
| WM_L1#2_Table#12 | 「GLOBlit_3475」 | 「PROPblock_3」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol; 70 data points.」 |
| WM_L1#2_Table#13 | 「GLOBlit_4415」 | 「PROPblock_7」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol; 40 data points.」 |
| WM_L1#2_Table#14 | 「GLOBlit_2825」 | 「PROPblock_12」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol (not individually inspected).」 |
| WM_L1#2_Table#15 | 「GLOBlit_8050」 | 「PROPblock_5」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol (not individually inspected).」 |
| WM_L1#2_Table#16 | 「GLOBlit_10159」 | 「PROPblock_7」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol; 23 data points.」 |
| WM_L1#2_Table#17 | 「GLOBlit_10699」 | 「PROPblock_6」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol; 18 data points.」 |
| WM_L1#2_Table#18 | 「GLOBlit_11792」 | 「PROPblock_3」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol; 15 data points.」 |
| WM_L1#2_Table#19 | 「GLOBlit_7085」 | 「PROPblock_7」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol (not individually inspected).」 |
| WM_L1#2_Table#20 | 「GLOBlit_11504」 | 「PROPblock_6」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for water + ethanol (not individually inspected).」 |
| WM_L1#2_Table#21 | 「GLOBlit_7178」 | 「PROPblock_10」 | 「GLOBcomp_1, GLOBcomp_2」 | 「GLOBprop_1」 | 「Mass density for water + ethanol (not individually inspected).」 |

*Not stored here: 3 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(3) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10: PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10 is quoted with data values (70, 40, 23, 13, …) but was never inspected in this run
- **MISATTRIBUTED_VALUE** GLOBlit_2432::PROPblock_2: 997.267 does not belong to GLOBlit_2432::PROPblock_2; it matches only GLOBlit_5201::PROPblock_19 (inspected this run)
- **MISATTRIBUTED_VALUE** GLOBlit_2432::PROPblock_2: 785.26 does not belong to GLOBlit_2432::PROPblock_2; it matches only GLOBlit_5201::PROPblock_19 (inspected this run)


### Inspected Blocks
- GLOBlit_9006 | 10.1021/je060335h | PROPblock_1: 164 rows; x=['mole_fraction_<ethanol>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3
- GLOBlit_9006 | 10.1021/je060335h | PROPblock_1: 164 rows; x=['mole_fraction_<ethanol>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3
- GLOBlit_9006 | 10.1021/je060335h | PROPblock_1: 164 rows; x=['mole_fraction_<ethanol>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3

### Completed Fits
  - 10.1021/je060335h/PROPblock_1 (ethanol, water): RK order=5, R²=0.996842, RMSE=1.6883259756124596e-08, coeffs=[-5e-06, 2e-06, -2e-06, -0.0, -1e-06, 2e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: ethanol=5.86702e-05, water=1.82629e-05 [block-edges of derived data (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1021_je060335h_BPROPblock_1_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je060335h_BPROPblock_1_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je060335h_BPROPblock_1_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je060335h_BPROPblock_1_T298.1_excess.png
  - 10.1016/j.jct.2018.02.022/PROPblock_19 (ethanol, water): RK order=5, R²=0.99002, RMSE=3.7458122188924395e-08, coeffs=[-3e-06, 2e-06, -3e-06, -2e-06, 7e-06, 7e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: ethanol=5.82068e-05, water=1.81108e-05 [block-edges of derived data (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_19_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_19_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_19_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_19_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1021_je060335h_BPROPblock_1_T298.1_fit.csv` — RK fit data — 10.1021/je060335h PROPblock_1_T298.1
- `$ROOT/data\10_1021_je060335h_BPROPblock_1_T298.1_excess.csv` — Excess property — 10.1021/je060335h PROPblock_1_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_19_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_19_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_19_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_19_T298.1

### plot
- `$ROOT/plots\10_1021_je060335h_BPROPblock_1_T298.1_fit.png` — RK fit plot — 10.1021/je060335h PROPblock_1_T298.1
- `$ROOT/plots\10_1021_je060335h_BPROPblock_1_T298.1_excess.png` — Excess plot — 10.1021/je060335h PROPblock_1_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_19_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_19_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_19_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_19_T298.1

