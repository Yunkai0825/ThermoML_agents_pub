# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_192913_176284_e39010e4\analysis_runs\run_1`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_2 | ethanol | 0.000994 |
| comp | GLOBcomp_4 | methanol | 0.000525 |
| comp | GLOBcomp_61 | 1,2-propanediol |  |
| prop | GLOBprop_4 | viscositypas |  |
| prop | GLOBprop_7 | refractiveindexnadline |  |
| var | GLOBvar_2 | molefraction<methanol> |  |
| constr | GLOBconstr_2 | temperaturek |  |
| constr | GLOBconstr_1 | pressurekpa |  |

### History
- [query_thermoml]
- [inspect_block]
- [get_pure_values] ERROR: No pure-component endpoints found within edge_threshold
- [query_thermoml_parallel]
- [inspect_block]
- [query_thermoml]
- [fit_block]
- [list_session_files]

### Query Results
#### query
**L1_query_1** — status: success · validation: PASS

**Summary:** Dynamic viscosity data for the binary mixture of methanol + ethanol at 303.15 K and 81.5 kPa (liquid phase) were found in ThermoML from DOI 10.1021/je800633a (GLOBlit_11337, PROPblock_16). Twelve data points span methanol mole fractions from 0.0417 to 0.9166, with viscosities ranging from 0.000556 to 0.000968 Pa·s. Viscosity decreases monotonically and nearly linearly (R² = 0.9960) with increasing methanol content, consistent with near-ideal mixing of two small hydrogen-bonding alcohols. Expanded uncertainties (k = 95%) are on the order of 7–9 × 10⁻⁶ Pa·s. No kinematic viscosity data were found for this system under these conditions.

**Answer:**

#### Viscosity Data for Methanol + Ethanol Binary System at 303.15 K and 81.5 kPa

An exact match was found in the ThermoML database:

**Source:** DOI 10.1021/je800633a (GLOBlit_11337), PROPblock_16

**System:** Binary mixture of ethanol (GLOBcomp_2) + methanol (GLOBcomp_4)

**Property:** Dynamic viscosity (GLOBprop_4), measured via capillary tube (Ostwald–Ubbelohde method, GLOBmeas_4)

**Conditions:** Temperature = 303.15 K, Pressure = 81.5 kPa, Liquid phase

**Number of data points:** 12

##### Complete Data Table

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *x(methanol)* | *T (K)* | *P (kPa)* | *η (Pa·s)* |
|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.0417」 | 「303.15」 | 「81.5」 | 「0.000968」 |
| WM_L1#1_Table#1_Row#2 | 「0.1476」 | 「303.15」 | 「81.5」 | 「0.000906」 |
| WM_L1#1_Table#1_Row#3 | 「0.2214」 | 「303.15」 | 「81.5」 | 「0.000865」 |
| WM_L1#1_Table#1_Row#4 | 「0.2952」 | 「303.15」 | 「81.5」 | 「0.000828」 |
| WM_L1#1_Table#1_Row#5 | 「0.3644」 | 「303.15」 | 「81.5」 | 「0.000793」 |
| WM_L1#1_Table#1_Row#6 | 「0.4488」 | 「303.15」 | 「81.5」 | 「0.000753」 |
| WM_L1#1_Table#1_Row#7 | 「0.5290」 | 「303.15」 | 「81.5」 | 「0.000717」 |
| WM_L1#1_Table#1_Row#8 | 「0.5995」 | 「303.15」 | 「81.5」 | 「0.000685」 |
| WM_L1#1_Table#1_Row#9 | 「0.6859」 | 「303.15」 | 「81.5」 | 「0.000648」 |
| WM_L1#1_Table#1_Row#10 | 「0.7442」 | 「303.15」 | 「81.5」 | 「0.000624」 |
| WM_L1#1_Table#1_Row#11 | 「0.8320」 | 「303.15」 | 「81.5」 | 「0.000588」 |
| WM_L1#1_Table#1_Row#12 | 「0.9166」 | 「303.15」 | 「81.5」 | 「0.000556」 |

**Composition range:** x(methanol) = 0.0417 to 0.9166

**Viscosity range:** 0.000556 to 0.000968 Pa·s

**Chemistry insight:** The dynamic viscosity decreases monotonically and nearly linearly (R² = 0.9960) as the methanol mole fraction increases. This is consistent with the lower viscosity of pure methanol compared to pure ethanol — both are small hydrogen-bonding alcohols with similar intermolecular interaction character, so their mixture viscosity shows near-ideal (close to linear) mixing behavior, with minimal viscosity excess. The reported expanded uncertainties (k = 95%) are on the order of 7–9 × 10⁻⁶ Pa·s.

No kinematic viscosity (GLOBprop_40) data were found for this system under these conditions.

**Core claims:**
- Dynamic viscosity data for the binary mixture of methanol + ethanol at 303.15 K and 81.5 kPa were found in the ThermoML database (DOI 10.1021/je800633a), comprising 12 data points measured via capillary tube (Ostwald–Ubbelohde method) over a methanol mole fraction range of 0.0417 to 0.9166.
- The dynamic viscosity decreases monotonically from 0.000968 Pa·s at x(methanol) = 0.0417 to 0.000556 Pa·s at x(methanol) = 0.9166, exhibiting near-linear mixing behavior (R² = 0.9960), consistent with the similar hydrogen-bonding character of the two small alcohols and minimal viscosity excess.
- Reported expanded uncertainties (k = 95%) are on the order of 7–9 × 10⁻⁶ Pa·s.
- No kinematic viscosity data were found for this system under these conditions.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_11337」 | 「PROPblock_16」 | 「GLOBcomp_2, GLOBcomp_4」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for the binary mixture of ethanol and methanol at 303.15 K and 81.5 kPa, 12 data points covering methanol mole fraction 0.0417 to 0.9166.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### pure_methanol_visc
**L1_query_2** — status: success · validation: PASS

**Summary:** The primary source DOI 10.1021/je800633a (GLOBlit_11337), PROPblock_8, reports the dynamic viscosity of pure liquid methanol (GLOBcomp_4, GLOBprop_4) measured by capillary tube (Ostwald–Ubbelohde) as a single data point: η = 0.000525 Pa·s at T = 303.15 K and P = 81.5 kPa. An additional source, DOI 10.1016/j.fluid.2006.02.023 (GLOBlit_369), PROPblock_8, reports η = 0.0005041 Pa·s for pure liquid methanol at 303.15 K and 101.325 kPa. The two independent measurements are consistent within ~4%, both falling in the expected range for liquid methanol near 303 K.

**Answer:**

**Pure Methanol Dynamic Viscosity at 303.15 K**

**Primary source (requested DOI):**

- **DOI:** 10.1021/je800633a (GLOBlit_11337)
- **Block:** PROPblock_8
- **System:** Unary (pure methanol, GLOBcomp_4)
- **Property:** Dynamic viscosity (GLOBprop_4)
- **Method:** Capillary tube (Ostwald–Ubbelohde)
- **Phase:** Liquid

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *T (K)* | *P (kPa)* | *η (Pa·s)* |
|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「303.15」 | 「81.5」 | 「0.000525」 |

This block contains a single data point for methanol viscosity at 303.15 K and 81.5 kPa.

**Additional source at exactly 303.15 K:**

- **DOI:** 10.1016/j.fluid.2006.02.023 (GLOBlit_369), PROPblock_8 — reports η = 0.0005041 Pa·s at 303.15 K and 101.325 kPa (single point, liquid phase).

The two independent measurements (0.000525 and 0.0005041 Pa·s) are consistent within ~4%, which is typical for viscosity measurements by different groups and methods. Both values fall in the expected range for liquid methanol near 303 K, where the viscosity decreases from higher values at lower temperatures as thermal energy increases molecular mobility.

**Core claims:**
- The primary source (DOI 10.1021/je800633a, PROPblock_8) reports the dynamic viscosity of pure liquid methanol at 303.15 K and 81.5 kPa as 0.000525 Pa·s, measured by capillary tube (Ostwald–Ubbelohde).
- An additional independent source (DOI 10.1016/j.fluid.2006.02.023, PROPblock_8) reports the dynamic viscosity of pure liquid methanol at 303.15 K and 101.325 kPa as 0.0005041 Pa·s.
- The two independent measurements (0.000525 and 0.0005041 Pa·s) are consistent within ~4%, which is typical for viscosity measurements by different groups and methods.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_11337」 | 「PROPblock_8」 | 「GLOBcomp_4」 | 「GLOBprop_4」 | 「Dynamic viscosity of pure methanol at 303.15 K and 81.5 kPa; η = 0.000525 Pa·s (liquid, capillary tube method).」 |
| WM_L1#2_Table#3 | 「GLOBlit_369」 | 「PROPblock_8」 | 「GLOBcomp_4」 | 「GLOBprop_4」 | 「Dynamic viscosity of pure methanol at 303.15 K and 101.325 kPa; η = 0.0005041 Pa·s (liquid phase).」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### pure_ethanol_visc — ERROR
query-L1 core-ID refinement exhausted 2 cycles: The working answer states the PROPblock_11 viscosity is 0.0009675 Pa·s, but the authoritative database-enriched candidate shows the actual value is 0.000968 Pa·s (range min/max/mean all = 0.000968). The answer text must be corrected to 0.000968 Pa·s for PROPblock_11 to match the authoritative data.

#### query
**L1_query_4** — status: success · validation: PASS

**Summary:** Pure ethanol dynamic viscosity at 303.15 K was identified in DOI 10.1021/je800633a (GLOBlit_11337, PROPblock_2). The reported value is 0.000994 Pa·s at 303.15 K and 81.5 kPa, measured by capillary tube method for the unary liquid-phase system. An additional source, DOI 10.1016/j.fluid.2006.02.023 (GLOBlit_369, PROPblock_11), reports 0.0009675 Pa·s at 303.15 K and 101.325 kPa. The GLOBlit_11337 value is recommended for internal consistency when used alongside the pure methanol endpoint from the same study for an Arrhenius mixing rule fit of the methanol + ethanol system.

**Answer:**

Pure ethanol dynamic viscosity at 303.15 K was found in DOI 10.1021/je800633a (GLOBlit_11337), PROPblock_2:

- **Compound:** Ethanol (GLOBcomp_2), unary (pure) system, liquid phase
- **Temperature:** 303.15 K
- **Pressure:** 81.5 kPa
- **Dynamic viscosity (η):** 0.000994 Pa·s
- **Measurement method:** Capillary tube (Ostwald/Ubbelohde)

This value comes from the same DOI and experimental conditions (303.15 K, 81.5 kPa) as the pure methanol viscosity (reported separately from PROPblock_8 of the same study), making it directly suitable as the pure ethanol endpoint for the Arrhenius mixing rule fit of the methanol + ethanol system.

An additional source, DOI 10.1016/j.fluid.2006.02.023 (GLOBlit_369, PROPblock_11), reports η = 0.0009675 Pa·s at 303.15 K and 101.325 kPa for pure ethanol — slightly lower, likely reflecting the different pressure and laboratory conditions. The value from GLOBlit_11337 PROPblock_2 (0.000994 Pa·s) is recommended for internal consistency with the methanol endpoint from the same study.

**Core claims:**
- Pure ethanol dynamic viscosity at 303.15 K and 81.5 kPa is 0.000994 Pa·s, measured by capillary tube method (DOI 10.1021/je800633a, PROPblock_2).
- An additional source (DOI 10.1016/j.fluid.2006.02.023, PROPblock_11) reports pure ethanol dynamic viscosity of 0.0009675 Pa·s at 303.15 K and 101.325 kPa, slightly lower than the primary value.
- The 0.000994 Pa·s value is recommended for internal consistency with the pure methanol endpoint from the same study, making it suitable as the pure ethanol endpoint for an Arrhenius mixing rule fit of the methanol + ethanol system.

**Core blocks found:**

**WM_L1#4_Blocks_(Analysis_L1#4_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#4_Table#1 | 「GLOBlit_11337」 | 「PROPblock_2」 | 「GLOBcomp_2」 | 「GLOBprop_4」 | 「Pure ethanol dynamic viscosity at 303.15 K and 81.5 kPa; η = 0.000994 Pa·s.」 |
| WM_L1#4_Table#2 | 「GLOBlit_369」 | 「PROPblock_11」 | 「GLOBcomp_2」 | 「GLOBprop_4」 | 「Pure ethanol dynamic viscosity at 303.15 K and 101.325 kPa; η = 0.0009675 Pa·s.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_11337 | 10.1021/je800633a | PROPblock_16: 12 rows; x=['mole_fraction_<methanol>']; y=['viscosity_pa_s']
    - BLKprop_1 / GLOBprop_4: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_4: kind=direct; materialize_reference=False; supported=True; units=Pa*s -> Pa*s
- GLOBlit_11337 | 10.1021/je800633a | PROPblock_11: 12 rows; x=['mole_fraction_<methanol>']; y=['refractive_index_na_dline']
    - BLKprop_1 / GLOBprop_7: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_7: kind=direct; materialize_reference=False; supported=True; units=1 -> 1

### Completed Fits
  - 10.1021/je800633a/PROPblock_16 (methanol, ethanol): RK order=2, R²=0.982166, RMSE=0.00047359700150033146, coeffs=[0.039699, 0.027563, -0.021872]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: methanol=0.000525, ethanol=0.000994 [named (matched to composition axis)]
      fit_csv: $ROOT/data\10_1021_je800633a_BPROPblock_16_T303.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je800633a_BPROPblock_16_T303.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je800633a_BPROPblock_16_T303.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je800633a_BPROPblock_16_T303.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1021_je800633a_BPROPblock_16_T303.1_fit.csv` — RK fit data — 10.1021/je800633a PROPblock_16_T303.1
- `$ROOT/data\10_1021_je800633a_BPROPblock_16_T303.1_excess.csv` — Excess property — 10.1021/je800633a PROPblock_16_T303.1

### plot
- `$ROOT/plots\10_1021_je800633a_BPROPblock_16_T303.1_fit.png` — RK fit plot — 10.1021/je800633a PROPblock_16_T303.1
- `$ROOT/plots\10_1021_je800633a_BPROPblock_16_T303.1_excess.png` — Excess plot — 10.1021/je800633a PROPblock_16_T303.1

