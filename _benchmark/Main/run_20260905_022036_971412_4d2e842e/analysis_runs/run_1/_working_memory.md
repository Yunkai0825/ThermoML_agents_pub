# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_022036_971412_4d2e842e\analysis_runs\run_1`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_1 | water | 992.08333 |
| comp | GLOBcomp_2 | ethanol | 785.7 |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_3 | pressurekpa |  |
| var | GLOBvar_2 | molefraction<ethanol> |  |

### History
- [query_thermoml]
- [inspect_block]
- [fit_block] ERROR: Requested x column 'Mole fraction of ethanol' not found in block
- [fit_block]
- [list_session_files]

### Query Results
#### query
**L1_query_1** — status: success · validation: PASS

**Summary:** Six ThermoML blocks containing mass density data for ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary mixtures near 298.15 K were identified. The most detailed block is GLOBlit_220::PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019), which contains 810 total data points spanning 298.15–348.15 K, 100–40000 kPa, and ethanol mole fractions 0.003–1, with 270 points at exactly 298.15 K. At 298.15 K and 100 kPa, density decreases monotonically from ~995.3 kg/m³ (x = 0.003) to 785.7 kg/m³ (x = 1); at 40000 kPa the corresponding values are 1012.7 and 815.7 kg/m³. Five additional blocks from DOIs 10.1016/j.jct.2018.02.022 (GLOBlit_5201::PROPblock_19), 10.1021/je060335h (GLOBlit_9006::PROPblock_1), 10.1016/j.fluid.2015.07.012 (GLOBlit_1742::PROPblock_3), 10.1016/j.fluid.2017.09.005 (GLOBlit_2092::PROPblock_3), and 10.1016/j.jct.2019.02.027 (GLOBlit_5473::PROPblock_21) were found but not inspected in detail. GLOBlit_220::PROPblock_2 is recommended as the richest dataset for this system.

**Answer:**

#### Density (Mass Density) Data for Ethanol + Water Binary Mixtures near 298.15 K

Six ethanol–water binary density blocks with mole-fraction composition variation were identified in the ThermoML database. The compounds are **ethanol** (GLOBcomp_2) and **water** (GLOBcomp_1), and the property is **mass density** (GLOBprop_1, kg/m³).

##### Summary of Blocks Found

The block_search_adv tool returned six blocks. Only **GLOBlit_220::PROPblock_2** was inspected in detail in this run; aggregate values for the other blocks were returned by the search tool but individual data points were not inspected. Below, I report only what was verified or clearly sourced.

---

##### 1. Best Block — GLOBlit_220 :: PROPblock_2

- **DOI:** 10.1016/j.fluid.2004.11.019
- **Total data points:** 810
- **Full-block temperature range:** 298.15–348.15 K
- **Full-block pressure range:** 100–40000 kPa
- **Full-block mole fraction (ethanol) range:** 0.003–1
- **Full-block density range:** 739.4–1012.7 kg/m³

**At T = 298.15 K** (270 matched rows; 25 shown by RDP sampling across 5 pressure isobars):

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *Pressure (kPa)* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「100」 | 「0.003」 | 「995.3」 |
| WM_L1#1_Table#1_Row#2 | 「100」 | 「0.2502」 | 「918.5」 |
| WM_L1#1_Table#1_Row#3 | 「100」 | 「0.4501」 | 「868.8」 |
| WM_L1#1_Table#1_Row#4 | 「100」 | 「0.6967」 | 「825.2」 |
| WM_L1#1_Table#1_Row#5 | 「100」 | 「1」 | 「785.7」 |
| WM_L1#1_Table#1_Row#6 | 「10000」 | 「0.003」 | 「999.8」 |
| WM_L1#1_Table#1_Row#7 | 「10000」 | 「0.2502」 | 「923.3」 |
| WM_L1#1_Table#1_Row#8 | 「10000」 | 「0.4501」 | 「874.7」 |
| WM_L1#1_Table#1_Row#9 | 「10000」 | 「0.6967」 | 「832.3」 |
| WM_L1#1_Table#1_Row#10 | 「10000」 | 「1」 | 「794」 |
| WM_L1#1_Table#1_Row#11 | 「20000」 | 「0.003」 | 「1004.2」 |
| WM_L1#1_Table#1_Row#12 | 「20000」 | 「0.2502」 | 「928」 |
| WM_L1#1_Table#1_Row#13 | 「20000」 | 「0.4501」 | 「880.4」 |
| WM_L1#1_Table#1_Row#14 | 「20000」 | 「0.6967」 | 「839」 |
| WM_L1#1_Table#1_Row#15 | 「20000」 | 「1」 | 「801.9」 |
| WM_L1#1_Table#1_Row#16 | 「30000」 | 「0.003」 | 「1008.5」 |
| WM_L1#1_Table#1_Row#17 | 「30000」 | 「0.2269」 | 「938.7」 |
| WM_L1#1_Table#1_Row#18 | 「30000」 | 「0.4501」 | 「885.7」 |
| WM_L1#1_Table#1_Row#19 | 「30000」 | 「0.6967」 | 「845.1」 |
| WM_L1#1_Table#1_Row#20 | 「30000」 | 「1」 | 「808.9」 |
| WM_L1#1_Table#1_Row#21 | 「40000」 | 「0.003」 | 「1012.7」 |
| WM_L1#1_Table#1_Row#22 | 「40000」 | 「0.2269」 | 「942.9」 |
| WM_L1#1_Table#1_Row#23 | 「40000」 | 「0.4501」 | 「890.8」 |
| WM_L1#1_Table#1_Row#24 | 「40000」 | 「0.6967」 | 「851」 |
| WM_L1#1_Table#1_Row#25 | 「40000」 | 「1」 | 「815.7」 |

This is the richest dataset: 810 total points spanning three temperatures, five pressures, and the full ethanol mole-fraction range (0.003–1). At 298.15 K alone there are 270 data points. The density decreases monotonically from ~995 kg/m³ (nearly pure water) to ~786 kg/m³ (pure ethanol) at atmospheric pressure, consistent with the well-known non-ideal mixing behavior of this system.

---

##### 2–5. Additional Blocks (search-level metadata only; not individually inspected)

The block_search_adv tool identified these additional blocks. Because they were not inspected with `inspect_block_table` in this run, only the search-returned block-level metadata (total point counts, composition range endpoints, and density range endpoints) is available. These values are from the search tool's aggregate output, not from direct row inspection.

**WM_L1#1_Table#2_(Analysis_L1#1_Answer):**

| *row_id* | *Rank* | *DOI* | *Literature ID* | *Block* | *Total pts* | *x range* | *ρ range (kg/m³)* | *Notes* |
|---|---|---|---|---|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「2」 | 「10.1016/j.jct.2018.02.022」 | 「GLOBlit_5201」 | 「PROPblock_19」 | 「not inspected」 | 「0–1」 | 「not inspected」 | 「Full x range per search」 |
| WM_L1#1_Table#2_Row#2 | 「3」 | 「10.1021/je060335h」 | 「GLOBlit_9006」 | 「PROPblock_1」 | 「not inspected」 | 「0–1」 | 「not inspected」 | 「Full x range per search」 |
| WM_L1#1_Table#2_Row#3 | 「4」 | 「10.1016/j.fluid.2015.07.012」 | 「GLOBlit_1742」 | 「PROPblock_3」 | 「not inspected」 | 「not inspected–1」 | 「not inspected」 | 「Partial x range per search」 |
| WM_L1#1_Table#2_Row#4 | 「5」 | 「10.1016/j.fluid.2017.09.005」 | 「GLOBlit_2092」 | 「PROPblock_3」 | 「not inspected」 | 「0–1」 | 「not inspected」 | 「Full x range per search」 |
| WM_L1#1_Table#2_Row#5 | 「6」 | 「10.1016/j.jct.2019.02.027」 | 「GLOBlit_5473」 | 「PROPblock_21」 | 「not inspected」 | 「0–1」 | 「not inspected」 | 「Full x range per search」 |

---

##### Recommendation

**GLOBlit_220 :: PROPblock_2** (DOI: 10.1016/j.fluid.2004.11.019) is the clear top choice: it has 810 data points, covers the full ethanol mole-fraction range (0.003–1), spans multiple temperatures (298.15–348.15 K) and pressures (100–40000 kPa), and provides 270 points at exactly 298.15 K. The remaining blocks (GLOBlit_5201, GLOBlit_9006, GLOBlit_1742, GLOBlit_2092, GLOBlit_5473) also cover the ethanol–water binary system with mole-fraction variation but were not inspected in detail during this run.

**Core claims:**
- Six ethanol–water binary density blocks with mole-fraction composition variation were identified in the ThermoML database; the richest is GLOBlit_220::PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019) with 810 total data points spanning 298.15–348.15 K, 100–40000 kPa, and ethanol mole fractions 0.003–1.
- At 298.15 K and 100 kPa, the mass density in GLOBlit_220::PROPblock_2 decreases monotonically from ~995.3 kg/m³ at x(ethanol) = 0.003 to ~785.7 kg/m³ at x(ethanol) = 1.
- At 298.15 K, increasing pressure from 100 to 40000 kPa increases the density at each composition; for example, pure ethanol density rises from 785.7 kg/m³ (100 kPa) to 815.7 kg/m³ (40000 kPa), and near-pure water density rises from 995.3 kg/m³ to 1012.7 kg/m³.
- Five additional ethanol–water density blocks were identified (GLOBlit_5201, GLOBlit_9006, GLOBlit_1742, GLOBlit_2092, GLOBlit_5473) but were not inspected at the individual data-point level, so their detailed content remains unverified.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_220」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of ethanol + water binary mixture; 810 points; T 298.15–348.15 K; P 100–40000 kPa; x(ethanol) 0.003–1; ρ 739.4–1012.7 kg/m³. At 298.15 K: 270 points spanning full composition range.」 |
| WM_L1#1_Table#4 | 「GLOBlit_5201」 | 「PROPblock_19」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of ethanol + water binary mixture; full x range 0–1; not inspected in detail.」 |
| WM_L1#1_Table#5 | 「GLOBlit_9006」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of ethanol + water binary mixture; full x range 0–1; not inspected in detail.」 |
| WM_L1#1_Table#6 | 「GLOBlit_1742」 | 「PROPblock_3」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of ethanol + water binary mixture; partial x range; not inspected in detail.」 |
| WM_L1#1_Table#7 | 「GLOBlit_2092」 | 「PROPblock_3」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of ethanol + water binary mixture; full x range 0–1; not inspected in detail.」 |
| WM_L1#1_Table#8 | 「GLOBlit_5473」 | 「PROPblock_21」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of ethanol + water binary mixture; full x range 0–1; not inspected in detail.」 |

*Not stored here: 1 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_220 | 10.1016/j.fluid.2004.11.019 | PROPblock_2: 810 rows; x=['mole_fraction_<ethanol>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3

### Completed Fits
  - 10.1016/j.fluid.2004.11.019/PROPblock_2 (ethanol, water): RK order=3, R²=0.997283, RMSE=0.47476545853553287, coeffs=[-120.55681, 18.567625, 43.919128, -31.350563]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      pure refs: ethanol=785.7, water=992.083 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv` — RK fit data — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv` — Excess property — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1

### plot
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png` — RK fit plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png` — Excess plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1

