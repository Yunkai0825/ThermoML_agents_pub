# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_060724_675016_8e01b1a7`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_4 | methanol | 787.2 |
| comp | GLOBcomp_1 | water | 997.05 |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<water> |  |
| constr | GLOBconstr_1 | pressurekpa |  |

### History
- [query_thermoml]
- [inspect_block]
- [fit_block] ERROR: Constraint column 'Temperature, K' not found in block
- [fit_block]

### Query Results
#### query
**L1_query_1** — status: success · validation: FLAGGED(1)

**Summary:** Ten ThermoML data blocks were identified for mass density (kg/m³) of the methanol + water binary system near 298.15 K. Three blocks were inspected in detail. GLOBlit_2825 / PROPblock_10 (DOI: 10.1016/j.jct.2007.05.004) is the best single source, covering x(water) = 0–1 at 101.0 kPa with 39 points across 293.15–303.15 K; representative 298.15 K values include 787.2 kg/m³ at x(water)=0 and 997.05 kg/m³ at x(water)=1. GLOBlit_8424 / PROPblock_3 (DOI: 10.1021/je049691v) has the most points (180) spanning 283.15–353.15 K and x(water) = 0.08–0.9603. GLOBlit_10866 / PROPblock_6 (DOI: 10.1021/je700300y) provides 84 points at 283.15–313.15 K and 101.0 kPa for x(water) = 0.0871–0.964. All three blocks show the expected monotonic, non-linear increase in density from methanol-rich to water-rich compositions. Seven additional blocks were returned but not individually inspected; these cover narrower composition or temperature ranges, different concentration bases, or high-pressure conditions.

**Answer:**

#### Density (Mass Density) Data for Methanol + Water Binary Mixtures near 298.15 K

Ten data blocks were found in the ThermoML database for the binary system methanol (GLOBcomp_4) + water (GLOBcomp_1) with mass density (GLOBprop_1, kg/m³) measurements that include or approach 298.15 K. The three best candidates for atmospheric-pressure density across the composition range at 298.15 K are detailed below, followed by a summary of additional blocks.

---

##### Top 3 Candidates (Inspected)

**1. GLOBlit_2825 / PROPblock_10** — DOI: 10.1016/j.jct.2007.05.004

- **Points:** 39 total
- **T range:** 293.15–303.15 K
- **Composition range:** x(water) = 0–1 (full range, including pure endpoints)
- **ρ range:** 782.48–998.2 kg/m³
- **Pressure:** 101.0 kPa (constrained)

Representative data at 298.15 K (from inspection):

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *x(water)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0」 | 「787.2」 |
| WM_L1#1_Table#1_Row#2 | 「0.2983」 | 「840.79」 |
| WM_L1#1_Table#1_Row#3 | 「0.5003」 | 「881.69」 |
| WM_L1#1_Table#1_Row#4 | 「0.8999」 | 「969.84」 |
| WM_L1#1_Table#1_Row#5 | 「1」 | 「997.05」 |

This block offers the best composition coverage, spanning from pure methanol to pure water at three temperatures.

---

**2. GLOBlit_8424 / PROPblock_3** — DOI: 10.1021/je049691v

- **Points:** 180 total
- **T range:** 283.15–353.15 K
- **Composition range:** x(water) = 0.08–0.9603
- **ρ range:** 747.01–988.05 kg/m³

Representative data at 298.15 K (from inspection):

**WM_L1#1_Table#2_(Analysis_L1#1_Answer):**

| *row_id* | *x(water)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0.08」 | 「800.1」 |
| WM_L1#1_Table#2_Row#2 | 「0.4799」 | 「876.94」 |
| WM_L1#1_Table#2_Row#3 | 「0.9603」 | 「985.01」 |

This block has the largest total point count (180) and spans a wide temperature range, making it excellent for temperature-dependent studies as well.

---

**3. GLOBlit_10866 / PROPblock_6** — DOI: 10.1021/je700300y

- **Points:** 84 total
- **T range:** 283.15–313.15 K
- **Composition range:** x(water) = 0.0871–0.964
- **ρ range:** 787.52–988.96 kg/m³
- **Pressure:** 101.0 kPa (constrained)

Representative data at 298.15 K (from inspection):

**WM_L1#1_Table#3_(Analysis_L1#1_Answer):**

| *row_id* | *x(water)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0.0871」 | 「801.35」 |
| WM_L1#1_Table#3_Row#2 | 「0.4788」 | 「876.68」 |
| WM_L1#1_Table#3_Row#3 | 「0.964」 | 「986」 |

---

##### Additional Blocks (Not Individually Inspected)

The following blocks were returned by the search but were not inspected for individual data rows. No specific numerical values are quoted for these blocks.

**WM_L1#1_Table#4_(Analysis_L1#1_Answer):**

| *row_id* | *DOI* | *Literature ID* | *Block* | *Brief Description* |
|---|---|---|---|---|
| WM_L1#1_Table#4_Row#1 | 「10.1021/je0601098」 | 「GLOBlit_8888」 | 「PROPblock_18」 | 「Solvent=methanol, fixed T」 |
| WM_L1#1_Table#4_Row#2 | 「10.1021/je0600810」 | 「GLOBlit_8869」 | 「PROPblock_4」 | 「Volume fraction basis」 |
| WM_L1#1_Table#4_Row#3 | 「10.1021/acs.jced.6b01058」 | 「GLOBlit_7085」 | 「PROPblock_6」 | 「Narrow composition range」 |
| WM_L1#1_Table#4_Row#4 | 「10.1021/je2003622」 | 「GLOBlit_9571」 | 「PROPblock_2」 | 「Mass fraction basis」 |
| WM_L1#1_Table#4_Row#5 | 「10.1016/j.jct.2004.07.019」 | 「GLOBlit_2432」 | 「PROPblock_1」 | 「High-pressure, Δρ values」 |
| WM_L1#1_Table#4_Row#6 | 「10.1016/j.jct.2019.05.013」 | 「GLOBlit_5533」 | 「PROPblock_2」 | 「Below 298 K」 |
| WM_L1#1_Table#4_Row#7 | 「10.1021/je034101z」 | 「GLOBlit_8254」 | 「PROPblock_4」 | 「High T, high P — less relevant for 298 K」 |

---

##### Summary

For atmospheric-pressure density of methanol + water at 298.15 K across the full composition range, **GLOBlit_2825 / PROPblock_10** is the best single source (full x = 0–1 coverage at 101.0 kPa). **GLOBlit_8424 / PROPblock_3** provides the most data points overall (180) with broad temperature coverage. All three top blocks show the expected non-linear density–composition behavior characteristic of the methanol–water system, with density increasing monotonically from methanol-rich to water-rich compositions.

**Core claims:**
- Ten ThermoML data blocks were identified for mass density of the methanol + water binary system near 298.15 K, with three blocks inspected in detail.
- GLOBlit_2825 / PROPblock_10 (DOI 10.1016/j.jct.2007.05.004) provides the best single-source composition coverage, spanning x(water) = 0–1 at 101.0 kPa and 298.15 K, with densities ranging from 787.2 kg/m³ (pure methanol) to 997.05 kg/m³ (pure water).
- GLOBlit_8424 / PROPblock_3 (DOI 10.1021/je049691v) has the largest total point count (180 points) covering 283.15–353.15 K and x(water) = 0.08–0.9603.
- GLOBlit_10866 / PROPblock_6 (DOI 10.1021/je700300y) covers x(water) = 0.0871–0.964 at 101.0 kPa across 283.15–313.15 K with 84 points.
- All three inspected blocks show density increasing monotonically from methanol-rich to water-rich compositions at 298.15 K.
- Seven additional blocks were returned by the search but were not individually inspected, so no specific numerical values are quoted for them; one block (PROPblock_1) was flagged as UNVERIFIED because data values attributed to it were never confirmed by inspection.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#5 | 「GLOBlit_2825」 | 「PROPblock_10」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water at 293.15–303.15 K, x(water) = 0–1, 39 points, 101.0 kPa.」 |
| WM_L1#1_Table#6 | 「GLOBlit_8424」 | 「PROPblock_3」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water at 283.15–353.15 K, x(water) = 0.08–0.9603, 180 points.」 |
| WM_L1#1_Table#7 | 「GLOBlit_10866」 | 「PROPblock_6」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water at 283.15–313.15 K, x(water) = 0.0871–0.964, 84 points, 101.0 kPa.」 |
| WM_L1#1_Table#8 | 「GLOBlit_8888」 | 「PROPblock_18」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water; not individually inspected.」 |
| WM_L1#1_Table#9 | 「GLOBlit_8869」 | 「PROPblock_4」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water, volume fraction basis; not individually inspected.」 |
| WM_L1#1_Table#10 | 「GLOBlit_7085」 | 「PROPblock_6」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water, narrow composition range; not individually inspected.」 |
| WM_L1#1_Table#11 | 「GLOBlit_9571」 | 「PROPblock_2」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water, mass fraction basis; not individually inspected.」 |
| WM_L1#1_Table#12 | 「GLOBlit_2432」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water, high-pressure Δρ values; not individually inspected.」 |
| WM_L1#1_Table#13 | 「GLOBlit_5533」 | 「PROPblock_2」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water, below 298 K; not individually inspected.」 |
| WM_L1#1_Table#14 | 「GLOBlit_8254」 | 「PROPblock_4」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water, high T and high P; not individually inspected.」 |

*Not stored here: 3 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_1: PROPblock_1 is quoted with data values (298.15, …) but was never inspected in this run


### Inspected Blocks
- GLOBlit_2825 | 10.1016/j.jct.2007.05.004 | PROPblock_10: 39 rows; x=['mole_fraction_<water>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3

### Completed Fits
  - 10.1016/j.jct.2007.05.004/PROPblock_10 (water, methanol): RK order=5, R²=0.999796, RMSE=0.03885240667464569, coeffs=[-42.310758, 2.461285, 7.280933, -0.41971, -46.15381, -43.843096]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      pure refs: water=997.05, methanol=787.2 [block-edges (methanol: direct/good, water: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2007.05.004 PROPblock_10_T298.1
- `$ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2007.05.004 PROPblock_10_T298.1

### plot
- `$ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2007.05.004 PROPblock_10_T298.1
- `$ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_10_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2007.05.004 PROPblock_10_T298.1

