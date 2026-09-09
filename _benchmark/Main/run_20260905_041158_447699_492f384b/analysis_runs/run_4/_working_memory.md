# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_041158_447699_492f384b\analysis_runs\run_4`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_1 | water | 1.8065584e-05 |
| comp | GLOBcomp_5 | propan-1-ol | 7.5157579e-05 |
| prop | GLOBprop_28 | excess molar volume, m3/mol |  |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_2 | molefraction<propan-1-ol> |  |
| constr | GLOBconstr_1 | pressurekpa |  |
| constr | GLOBconstr_2 | temperaturek |  |
| lit | GLOBlit_11042 | 10.1021/je700700f |  |

### History
- [query_thermoml_parallel]
- [inspect_block]
- [fit_block_derived]
- [predict_from_rk]
- [list_session_files]

### Query Results
#### direct_VE
**L1_query_1** — status: no_results · validation: PASS

**Summary:** Excess molar volume (VE) data for the binary system water + 1-propanol at 298.15 K was not found in the ThermoML database. The compounds were resolved as water (GLOBcomp_1) and 1-propanol (GLOBcomp_5), and excess molar volume corresponds to GLOBprop_28. Searching binary blocks containing both components filtered for GLOBprop_28 returned 0 results, even with no temperature filter. The database does contain extensive data for water + 1-propanol covering other properties such as mass density (GLOBprop_1), mole fraction/VLE (GLOBprop_2), activity coefficient (GLOBprop_3), and viscosity (GLOBprop_4), but excess molar volume is not among them. VE data for 1-propanol exists only paired with other co-solvents, including 1-butyl-3-methylimidazolium nitrate, 3-methylbutyl ethanoate, 1-methylimidazolium acetate, 2-pyrrolidinone, and formamide.

**Answer:**

**Excess molar volume (VE) data for the binary system water + 1-propanol at 298.15 K was not found in the ThermoML database.**

##### Search Summary

**Compounds resolved:**
- Water → GLOBcomp_1
- 1-Propanol (propan-1-ol) → GLOBcomp_5
- Excess molar volume → GLOBprop_28

**What was searched:**
1. Binary blocks with both water + 1-propanol filtered for excess molar volume (GLOBprop_28) — **0 results**, even with no temperature filter and both declared and subsystem scopes.

2. Excess molar volume blocks for 1-propanol with any binary partner — blocks were found, but none involve water. The available VE data for 1-propanol pairs with other co-solvents including:
   - 1-butyl-3-methylimidazolium nitrate (GLOBlit_3116, PROPblock_14)
   - 3-methylbutyl ethanoate (GLOBlit_3325, PROPblock_20)
   - 1-methylimidazolium acetate (GLOBlit_3540, PROPblock_23)
   - 2-pyrrolidinone (GLOBlit_5836, PROPblock_16)
   - formamide (GLOBlit_6063, PROPblock_7)
   - and one additional system (GLOBlit_8993)

3. Any binary data for water + 1-propanol (no property filter) — multiple blocks were found across numerous DOIs, covering properties including mass density (GLOBprop_1), mole fraction/VLE (GLOBprop_2), activity coefficient (GLOBprop_3), viscosity (GLOBprop_4), and others — but **excess molar volume is not among them**.

##### Conclusion

The ThermoML database contains extensive thermodynamic data for the water + 1-propanol binary system (density, VLE, viscosity, activity coefficients, etc.) but does not include excess molar volume measurements for this particular pair. VE data for 1-propanol exists only with other co-solvents (ionic liquids, formamide, isoamyl acetate, 2-pyrrolidinone).

**Core claims:**
- Excess molar volume (VE) data for the binary system water + 1-propanol at 298.15 K was not found in the ThermoML database.
- The ThermoML database contains extensive thermodynamic data for the water + 1-propanol binary system (density, VLE, viscosity, activity coefficients, etc.) but does not include excess molar volume measurements for this pair.
- VE data for 1-propanol in the ThermoML database exists only with other co-solvents (ionic liquids, formamide, isoamyl acetate, 2-pyrrolidinone), not with water.

*Not stored here: 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### density_data
**L1_query_2** — status: success · validation: PASS

**Summary:** Density data for the binary system water + 1-propanol at 298.15 K and 101.0 kPa were identified in the ThermoML database from DOI 10.1021/je700700f (GLOBlit_11042, Block PROPblock_14). The dataset contains 13 mass density measurements spanning the full composition range (x₁-propanol = 0 to 1), with density decreasing monotonically from 997.2 kg/m³ (pure water) to 799.6 kg/m³ (pure propan-1-ol). Representative values include 914.9 kg/m³ at x = 0.1986, 887.2 at 0.2979, 866.9 at 0.3949, 850.3 at 0.4955, 836.9 at 0.5953, and 816.3 at 0.7969. Both pure-component endpoints are included, making the block suitable for calculating excess molar volumes V^E at each composition. Additional mass density blocks for this binary system near 298.15 K exist in the database but were not individually inspected.

**Answer:**

#### Density Data for Binary Water + 1-Propanol at 298.15 K

A comprehensive density dataset suitable for deriving excess molar volume (V^E) was found in the ThermoML database for the binary system **water + 1-propanol**.

##### Primary Dataset

**Source:** DOI 10.1021/je700700f (GLOBlit_11042), Block PROPblock_14

- **System:** Binary mixture of water (GLOBcomp_1) + propan-1-ol (GLOBcomp_5)
- **Property:** Mass density (kg/m³)
- **Temperature:** 298.15 K (isothermal)
- **Pressure:** 101.0 kPa
- **Total data points:** 13 across the full composition range (x₁-propanol = 0 to 1)
- **Density range:** 799.6–997.2 kg/m³

Representative data points (RDP subset, 8 of 13 points shown):

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *x(propan-1-ol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0」 | 「997.2」 |
| WM_L1#2_Table#1_Row#2 | 「0.1986」 | 「914.9」 |
| WM_L1#2_Table#1_Row#3 | 「0.2979」 | 「887.2」 |
| WM_L1#2_Table#1_Row#4 | 「0.3949」 | 「866.9」 |
| WM_L1#2_Table#1_Row#5 | 「0.4955」 | 「850.3」 |
| WM_L1#2_Table#1_Row#6 | 「0.5953」 | 「836.9」 |
| WM_L1#2_Table#1_Row#7 | 「0.7969」 | 「816.3」 |
| WM_L1#2_Table#1_Row#8 | 「1」 | 「799.6」 |

The density decreases monotonically with increasing propan-1-ol mole fraction, from pure water (997.2 kg/m³) to pure propan-1-ol (799.6 kg/m³). This block covers the full composition range including both pure-component endpoints, making it well-suited for calculating excess molar volumes V^E = V_mix − Σ xᵢVᵢ* at each composition, where the pure-component molar volumes Vᵢ* can be obtained directly from the endpoint densities.

##### Additional Sources

Multiple additional mass density blocks were also found for this binary system near 298.15 K, providing opportunities for cross-validation. These additional blocks were not individually inspected in this run.

**Core claims:**
- A comprehensive density dataset for the binary system water + 1-propanol at 298.15 K and 101.0 kPa was identified in ThermoML (DOI 10.1021/je700700f, Block PROPblock_14), containing 13 data points spanning the full composition range (x₁-propanol = 0 to 1) with densities ranging from 799.6–997.2 kg/m³.
- The density decreases monotonically with increasing propan-1-ol mole fraction, from pure water (997.2 kg/m³) to pure propan-1-ol (799.6 kg/m³).
- The dataset includes both pure-component endpoints, making it suitable for calculating excess molar volumes V^E at each composition.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_11042」 | 「PROPblock_14」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density (kg/m³) for binary water + propan-1-ol at 298.15 K, 101.0 kPa; 13 data points across full composition range (x₁-propanol = 0 to 1); density range 799.6–997.2 kg/m³.」 |

*Not stored here: 1 verbatim data_inspections table(s); 4 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_11042 | 10.1021/je700700f | PROPblock_14: 13 rows; x=['mole_fraction_<propan-1-ol>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3

### Completed Fits
  - 10.1021/je700700f/PROPblock_14 (propan-1-ol, water): RK order=5, R²=0.999276, RMSE=4.602814010602905e-09, coeffs=[-3e-06, 1e-06, -1e-06, 0.0, -2e-06, 2e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: propan-1-ol=7.51576e-05, water=1.80656e-05 [block-edges of derived data (water: direct/good, propan-1-ol: direct/good)]
      fit_csv: $ROOT/data\10_1021_je700700f_BPROPblock_14_fit.csv
      excess_csv: $ROOT/data\10_1021_je700700f_BPROPblock_14_excess.csv
      fit_plot: $ROOT/plots\10_1021_je700700f_BPROPblock_14_fit.png
      excess_plot: $ROOT/plots\10_1021_je700700f_BPROPblock_14_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1021_je700700f_BPROPblock_14_fit.csv` — RK fit data — 10.1021/je700700f PROPblock_14
- `$ROOT/data\10_1021_je700700f_BPROPblock_14_excess.csv` — Excess property — 10.1021/je700700f PROPblock_14

### plot
- `$ROOT/plots\10_1021_je700700f_BPROPblock_14_fit.png` — RK fit plot — 10.1021/je700700f PROPblock_14
- `$ROOT/plots\10_1021_je700700f_BPROPblock_14_excess.png` — Excess plot — 10.1021/je700700f PROPblock_14

