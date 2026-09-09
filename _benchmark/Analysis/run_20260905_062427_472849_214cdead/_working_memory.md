# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062427_472849_214cdead`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_268 | 2-pyrrolidinone |  |
| comp | GLOBcomp_1 | water | 0.00089 |
| comp | GLOBcomp_18 | dimethylformamide |  |
| comp | GLOBcomp_63 | n,n-dimethylethanamide |  |
| comp | GLOBcomp_47 | n-methylpyrrolidone | 0.001656 |
| prop | GLOBprop_4 | viscositypas |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<water> |  |
| constr | GLOBconstr_1 | pressurekpa |  |
| lit | GLOBlit_8242 | 10.1021/je0340809 |  |

### History
- [query_thermoml]
- [query_thermoml]
- [query_thermoml]
- [fit_multi_system]
- [inspect_block]
- [inspect_block]
- [get_pure_values]
- [fit_multi_system]
- [fit_multi_system]

### Query Results
#### query
**L1_query_1** — status: success · validation: FLAGGED(4)

**Summary:** Dynamic viscosity (η, Pa·s) data for the binary system N-methyl-2-pyrrolidone (NMP) + water near 298.15 K were found in three ThermoML data blocks. Block 1 (DOI 10.1021/je034073k, GLOBlit_8238, PROPblock_3; 65 points, 298.15–343.15 K, x(NMP), 101.15 kPa) and Block 2 (DOI 10.1021/je0340809, GLOBlit_8242, PROPblock_17; 95 points, 298.15–338.15 K, x(water), 101.3 kPa) contain data exactly at 298.15 K. Block 3 (DOI 10.1021/je100967k, GLOBlit_9372, PROPblock_17; 44 points, 293.15–323.15 K, x(NMP), 101.0 kPa) lacks an exact 298.15 K isotherm, with nearest temperatures at 293.15 K and 303.15 K. Representative 298.15 K values from Block 1 include η = 0.00089 Pa·s at x(NMP) = 0, 0.002762 Pa·s at x(NMP) = 0.1001, a maximum of 0.005062 Pa·s at x(NMP) = 0.3004, and 0.003729 Pa·s at x(NMP) = 0.503. Block 2 values at 298.15 K include η = 0.001721 Pa·s at x(water) = 0.0522 and 0.002535 Pa·s at x(water) = 0.3481. The viscosity range across the full composition span is 0.000405–0.005062 Pa·s (Block 1) and 0.000467–0.005159 Pa·s (Block 2). The pronounced viscosity maximum near x(NMP) ≈ 0.3 is characteristic of strong NMP–water hydrogen-bonding interactions.

**Answer:**

Three data blocks containing dynamic viscosity (η, Pa·s) measurements for the binary system **N-methyl-2-pyrrolidone (NMP) + water** were found near 298.15 K:

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *#* | *DOI* | *Literature ID* | *Block* | *Data Points* | *T range (K)* | *Composition variable* | *Pressure (kPa)* |
|---|---|---|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「1」 | 「10.1021/je034073k」 | 「GLOBlit_8238」 | 「PROPblock_3」 | 「65」 | 「298.15–343.15」 | 「x(NMP)」 | 「101.15」 |
| WM_L1#1_Table#1_Row#2 | 「2」 | 「10.1021/je0340809」 | 「GLOBlit_8242」 | 「PROPblock_17」 | 「95」 | 「298.15–338.15」 | 「x(water)」 | 「101.3」 |
| WM_L1#1_Table#1_Row#3 | 「3」 | 「10.1021/je100967k」 | 「GLOBlit_9372」 | 「PROPblock_17」 | 「44」 | 「293.15–323.15」 | 「x(NMP)」 | 「101.0」 |

**Key observations:**

- **Blocks 1 and 2** (GLOBlit_8238 and GLOBlit_8242) contain data exactly at **298.15 K**, making them directly usable without interpolation.
- **Block 3** (GLOBlit_9372) does **not** include an exact 298.15 K isotherm; the nearest temperatures are **293.15 K** (below) and **303.15 K** (above).
- All three blocks report data at approximately atmospheric pressure (~101 kPa).
- Block 1 uses mole fraction of NMP as the composition variable, Block 2 uses mole fraction of water, and Block 3 uses mole fraction of NMP.

**Representative data at 298.15 K from Block 1** (GLOBlit_8238::PROPblock_3):

**WM_L1#1_Table#2_(Analysis_L1#1_Answer):**

| *row_id* | *x(NMP)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0」 | 「0.00089」 |
| WM_L1#1_Table#2_Row#2 | 「0.0501」 | 「0.00174」 |
| WM_L1#1_Table#2_Row#3 | 「0.0701」 | 「0.002137」 |
| WM_L1#1_Table#2_Row#4 | 「0.1001」 | 「0.002762」 |
| WM_L1#1_Table#2_Row#5 | 「0.2004」 | 「0.004555」 |
| WM_L1#1_Table#2_Row#6 | 「0.3004」 | 「0.005062」 |
| WM_L1#1_Table#2_Row#7 | 「0.4012」 | 「0.004505」 |
| WM_L1#1_Table#2_Row#8 | 「0.503」 | 「0.003729」 |

**Representative data at 298.15 K from Block 2** (GLOBlit_8242::PROPblock_17):

**WM_L1#1_Table#3_(Analysis_L1#1_Answer):**

| *row_id* | *x(water)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0.0522」 | 「0.001721」 |
| WM_L1#1_Table#3_Row#2 | 「0.1684」 | 「0.001985」 |
| WM_L1#1_Table#3_Row#3 | 「0.2465」 | 「0.002147」 |
| WM_L1#1_Table#3_Row#4 | 「0.3481」 | 「0.002535」 |

The data from Block 1 clearly shows a pronounced viscosity maximum near x(NMP) ≈ 0.3 (η = 0.005062 Pa·s at x(NMP) = 0.3004, from GLOBlit_8238::PROPblock_3), after which viscosity decreases at higher NMP mole fractions. This maximum is characteristic of strong hydrogen-bonding interactions between NMP and water, which create extensive intermolecular association networks at intermediate compositions. The overall viscosity range across the full composition span is 0.000405–0.005062 Pa·s (Block 1, GLOBlit_8238::PROPblock_3 stats) and 0.000467–0.005159 Pa·s (Block 2, GLOBlit_8242::PROPblock_17 stats).

**Core claims:**
- Three ThermoML data blocks report dynamic viscosity (η, Pa·s) for the binary system N-methyl-2-pyrrolidone (NMP) + water near 298.15 K at approximately atmospheric pressure (~101 kPa), sourced from DOIs 10.1021/je034073k, 10.1021/je0340809, and 10.1021/je100967k.
- Blocks 1 (GLOBlit_8238::PROPblock_3) and 2 (GLOBlit_8242::PROPblock_17) contain data exactly at 298.15 K, while Block 3 (GLOBlit_9372::PROPblock_17) lacks an exact 298.15 K isotherm, with nearest temperatures of 293.15 K and 303.15 K.
- Data from Block 1 (GLOBlit_8238::PROPblock_3) show a pronounced viscosity maximum near x(NMP) ≈ 0.3, with η = 0.005062 Pa·s at x(NMP) = 0.3004, after which viscosity decreases at higher NMP mole fractions.
- The viscosity maximum is attributed to strong hydrogen-bonding interactions between NMP and water creating extensive intermolecular association networks at intermediate compositions.
- The overall viscosity range across the full composition span is 0.000405–0.005062 Pa·s for Block 1 (GLOBlit_8238::PROPblock_3) and 0.000467–0.005159 Pa·s for Block 2 (GLOBlit_8242::PROPblock_17), after correcting misattributed block assignments flagged in the answer.
- Several quoted statistical range values were flagged as misattributed between blocks, requiring re-anchoring but not invalidating the underlying data.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_8238」 | 「PROPblock_3」 | 「GLOBcomp_47, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for N-methyl-2-pyrrolidone + water at 298.15–343.15 K, 101.15 kPa, 65 data points, composition as mole fraction of NMP.」 |
| WM_L1#1_Table#5 | 「GLOBlit_8242」 | 「PROPblock_17」 | 「GLOBcomp_47, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for N-methyl-2-pyrrolidone + water at 298.15–338.15 K, 101.3 kPa, 95 data points, composition as mole fraction of water.」 |
| WM_L1#1_Table#6 | 「GLOBlit_9372」 | 「PROPblock_17」 | 「GLOBcomp_47, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for N-methyl-2-pyrrolidone + water at 293.15–323.15 K, 101.0 kPa, 44 data points, composition as mole fraction of NMP.」 |

*Not stored here: 3 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(4) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **MISATTRIBUTED_VALUE** GLOBlit_8242::PROPblock_17: 0.005062 does not belong to GLOBlit_8242::PROPblock_17; it matches only GLOBlit_8238::PROPblock_3 (inspected this run)
- **MISATTRIBUTED_VALUE** GLOBlit_8242::PROPblock_17: 0.3004 does not belong to GLOBlit_8242::PROPblock_17; it matches only GLOBlit_8238::PROPblock_3 (inspected this run)
- **MISATTRIBUTED_VALUE** GLOBlit_8238::PROPblock_3: 0.000467 does not belong to GLOBlit_8238::PROPblock_3; it matches only GLOBlit_8242::PROPblock_17 (inspected this run)
- **MISATTRIBUTED_VALUE** GLOBlit_8238::PROPblock_3: 0.005159 does not belong to GLOBlit_8238::PROPblock_3; it matches only GLOBlit_8242::PROPblock_17 (inspected this run)


#### query
**L1_query_2** — status: success · validation: PASS

**Summary:** Dynamic viscosity of the binary system 2-pyrrolidinone + water was reported from DOI 10.1021/je0340809 (ThermoML block PROPblock_14). The property is dynamic viscosity in Pa·s for the liquid phase at 101.3 kPa, with 95 total data points spanning 298.15–338.15 K. At 298.15 K, 19 data points cover water mole fractions from 0.0549 to 0.9906. Viscosity decreases monotonically with increasing water content: from 0.01302 Pa·s at x(water)=0.0549 to 0.001036 Pa·s at x(water)=0.9906. Representative values include 0.012295 Pa·s at x=0.1506, 0.011766 Pa·s at x=0.2552, 0.01063 Pa·s at x=0.4496, 0.010127 Pa·s at x=0.5, 0.008014 Pa·s at x=0.6422, 0.005772 Pa·s at x=0.7532, 0.003645 Pa·s at x=0.8516, 0.002651 Pa·s at x=0.9, and 0.001667 Pa·s at x=0.9526. Additional isotherms at 308.15, 318.15, and 338.15 K are present in the block, with the full viscosity range being 0.000473–0.01302 Pa·s. The monotonic decrease reflects progressive dilution of the viscous lactam hydrogen-bonding network by water.

**Answer:**

**Dynamic Viscosity of 2-Pyrrolidinone + Water (Binary System) near 298.15 K**

A single data block was found in the ThermoML database:

- **DOI:** 10.1021/je0340809 (GLOBlit_8242)
- **Block:** PROPblock_14
- **System:** Binary — 2-pyrrolidinone (GLOBcomp_268) + water (GLOBcomp_1)
- **Property:** Dynamic viscosity (GLOBprop_4), liquid phase, in Pa·s
- **Composition variable:** Mole fraction of water (GLOBvar_2)
- **Temperature variable:** Temperature in K (GLOBvar_1)
- **Constraint:** Pressure = 101.3 kPa (atmospheric)
- **Total data points:** 95 (across temperatures 298.15–338.15 K)
- **Data points at 298.15 K:** 19 (13 shown via shape-preserving selection; mole fraction of water spans 0.0549–0.9906)

**Viscosity data at T = 298.15 K, P = 101.3 kPa:**

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *x(water)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0.0549」 | 「0.01302」 |
| WM_L1#2_Table#1_Row#2 | 「0.1506」 | 「0.012295」 |
| WM_L1#2_Table#1_Row#3 | 「0.2552」 | 「0.011766」 |
| WM_L1#2_Table#1_Row#4 | 「0.35」 | 「0.011319」 |
| WM_L1#2_Table#1_Row#5 | 「0.4496」 | 「0.01063」 |
| WM_L1#2_Table#1_Row#6 | 「0.5」 | 「0.010127」 |
| WM_L1#2_Table#1_Row#7 | 「0.5566」 | 「0.009408」 |
| WM_L1#2_Table#1_Row#8 | 「0.6422」 | 「0.008014」 |
| WM_L1#2_Table#1_Row#9 | 「0.7532」 | 「0.005772」 |
| WM_L1#2_Table#1_Row#10 | 「0.8516」 | 「0.003645」 |
| WM_L1#2_Table#1_Row#11 | 「0.9」 | 「0.002651」 |
| WM_L1#2_Table#1_Row#12 | 「0.9526」 | 「0.001667」 |
| WM_L1#2_Table#1_Row#13 | 「0.9906」 | 「0.001036」 |

**Chemical insight:** 2-Pyrrolidinone (γ-butyrolactam, the unmethylated parent of NMP) is a strongly hydrogen-bonding lactam. The viscosity decreases monotonically as the water mole fraction increases from 0.0549 to 0.9906, dropping from 0.01302 Pa·s (nearly pure 2-pyrrolidinone) to 0.001036 Pa·s (dilute 2-pyrrolidinone in water). This smooth, roughly order-of-magnitude decrease reflects the progressive dilution of the viscous lactam network by the much less viscous water. The block also contains isotherms at 308.15, 318.15, and 338.15 K (full block viscosity range: 0.000473–0.01302 Pa·s), showing the expected decrease in viscosity with rising temperature.

**Core claims:**
- A single ThermoML data block (DOI 10.1021/je0340809, PROPblock_14) reports dynamic viscosity for the binary system 2-pyrrolidinone + water in the liquid phase at 101.3 kPa, covering temperatures 298.15–338.15 K with 95 total data points.
- At 298.15 K and 101.3 kPa, 19 data points span water mole fractions from 0.0549 to 0.9906; the dynamic viscosity decreases monotonically from 0.01302 Pa·s at x(water) = 0.0549 to 0.001036 Pa·s at x(water) = 0.9906.
- The monotonic viscosity decrease with increasing water content reflects progressive dilution of the viscous hydrogen-bonding lactam network by the much less viscous water.
- The full block viscosity range across all temperatures (298.15–338.15 K) is 0.000473–0.01302 Pa·s, showing the expected decrease in viscosity with rising temperature.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_8242」 | 「PROPblock_14」 | 「GLOBcomp_268, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of 2-pyrrolidinone + water binary system at 298.15–338.15 K and 101.3 kPa; 95 data points; composition given as mole fraction of water.」 |

*Not stored here: 3 verbatim data_inspections table(s); 4 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### query
**L1_query_3** — status: partial · validation: PASS

**Summary:** Dynamic viscosity data were found for the DMF (GLOBcomp_18) + Water (GLOBcomp_1) binary system but not for the DMAc (GLOBcomp_63) + Water system. The best DMF + Water data come from GLOBlit_8676 (DOI: 10.1021/je050209y), PROPblock_9, reporting 11 points at 298.15 K and 101.325 kPa over mole fractions of DMF from 0.05 to 0.9488. Viscosities (Pa·s) are: 0.00131 at x = 0.05, 0.001728 at 0.1001, 0.002346 at 0.2, 0.002491 at 0.299, 0.002273 at 0.3998, 0.001878 at 0.4997, 0.001532 at 0.5993, 0.001243 at 0.6995, 0.001045 at 0.8, 0.000901 at 0.8991, and 0.000843 at 0.9488. A non-monotonic composition dependence is observed with a single maximum near x(DMF) ≈ 0.3, attributed to strong hydrogen-bonding interactions between DMF and water. For DMAc + Water, the ThermoML database contains blocks for other properties (mass density, relative permittivity, speed of sound, excess molar volume) but no dynamic viscosity (GLOBprop_4) data were found.

**Answer:**

#### Dynamic Viscosity Data for DMF + Water and DMAc + Water Binary Systems near 298.15 K

##### 1. N,N-Dimethylformamide (DMF) + Water

**Compound IDs:** DMF = GLOBcomp_18 (C₃H₇NO), Water = GLOBcomp_1 (H₂O)

**Best data block:** GLOBlit_8676 (DOI: 10.1021/je050209y), PROPblock_9
- **System:** binary, DMF + water
- **Data points:** 11
- **Temperature:** 298.15 K (fixed constraint)
- **Pressure:** 101.325 kPa (fixed constraint)
- **Composition variable:** mole fraction of DMF, range 0.05–0.9488

**Complete viscosity data at 298.15 K:**

**WM_L1#3_Table#1_(Analysis_L1#3_Answer):**

| *row_id* | *x(DMF)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#3_Table#1_Row#1 | 「0.05」 | 「0.00131」 |
| WM_L1#3_Table#1_Row#2 | 「0.1001」 | 「0.001728」 |
| WM_L1#3_Table#1_Row#3 | 「0.2」 | 「0.002346」 |
| WM_L1#3_Table#1_Row#4 | 「0.299」 | 「0.002491」 |
| WM_L1#3_Table#1_Row#5 | 「0.3998」 | 「0.002273」 |
| WM_L1#3_Table#1_Row#6 | 「0.4997」 | 「0.001878」 |
| WM_L1#3_Table#1_Row#7 | 「0.5993」 | 「0.001532」 |
| WM_L1#3_Table#1_Row#8 | 「0.6995」 | 「0.001243」 |
| WM_L1#3_Table#1_Row#9 | 「0.8」 | 「0.001045」 |
| WM_L1#3_Table#1_Row#10 | 「0.8991」 | 「0.000901」 |
| WM_L1#3_Table#1_Row#11 | 「0.9488」 | 「0.000843」 |

**Chemistry insight:** The viscosity shows a clear non-monotonic dependence on composition with a single maximum near x(DMF) ≈ 0.3 (viscosity = 0.002491 Pa·s). This is characteristic of strong intermolecular interactions (hydrogen bonding) between DMF and water. The maximum viscosity is roughly 3.0× the value at the DMF-rich end (0.000843 Pa·s at x = 0.9488) — this ratio is derived by dividing the two inspected values. This indicates significant structural reorganization in the water-rich to intermediate composition region.

**Additional blocks found (not inspected in this run):**
- GLOBlit_11030 (DOI: 10.1021/je300608v), PROPblock_3 — covers a range of temperatures and compositions
- GLOBlit_8676, PROPblock_10 — additional isothermal data at a different temperature
- GLOBlit_9342 (DOI: 10.1021/je1008813), PROPblock_3 — data at elevated temperatures

##### 2. N,N-Dimethylacetamide (DMAc) + Water

**Compound IDs:** DMAc = GLOBcomp_63 (C₄H₉NO, N,N-dimethylethanamide), Water = GLOBcomp_1

**Result: No dynamic viscosity data found** in the ThermoML database for this binary system. A comprehensive search (with and without temperature filters, using both declared and subsystem scopes) returned zero viscosity blocks.

The database does contain data blocks for DMAc + water covering other properties including mass density (GLOBprop_1), relative permittivity, speed of sound, excess molar volume, and others — but dynamic viscosity (GLOBprop_4) is not among them.

**Core claims:**
- At 298.15 K and 101.325 kPa, the dynamic viscosity of the DMF + water binary system (from GLOBlit_8676, PROPblock_9) exhibits a non-monotonic dependence on composition with a single maximum near x(DMF) ≈ 0.3 (viscosity = 0.002491 Pa·s), characteristic of strong hydrogen-bonding interactions between DMF and water.
- The reported viscosity data for DMF + water at 298.15 K span DMF mole fractions from 0.05 to 0.9488, with viscosity values ranging from 0.000843 Pa·s (x = 0.9488) to the maximum of 0.002491 Pa·s (x = 0.299).
- No dynamic viscosity data were found in the ThermoML database for the DMAc (N,N-dimethylacetamide) + water binary system, despite the database containing other properties (mass density, relative permittivity, speed of sound, excess molar volume) for that system.

**Core blocks found:**

**WM_L1#3_Blocks_(Analysis_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#2 | 「GLOBlit_8676」 | 「PROPblock_9」 | 「GLOBcomp_18, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for N,N-dimethylformamide + water at 298.15 K and 101.325 kPa; 11 data points covering mole fraction of DMF from 0.05 to 0.9488, showing a viscosity maximum near x(DMF) ≈ 0.3.」 |

*Not stored here: 1 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_8238 | 10.1021/je034073k | PROPblock_3: 65 rows; x=['mole_fraction_<N-methylpyrrolidone>']; y=['viscosity_pa_s']
    - BLKprop_1 / GLOBprop_4: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_4: kind=direct; materialize_reference=False; supported=True; units=Pa*s -> Pa*s
- GLOBlit_8242 | 10.1021/je0340809 | PROPblock_14: 95 rows; x=['mole_fraction_<water>']; y=['viscosity_pa_s']
    - BLKprop_1 / GLOBprop_4: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_4: kind=direct; materialize_reference=False; supported=True; units=Pa*s -> Pa*s

### Completed Fits
  - NMP+water [10.1021/je034073k/PROPblock_3] (N-methylpyrrolidone, water): RK order=4, R²=0.999957, RMSE=0.002865770833971775, coeffs=[4.502927, -5.412702, 3.895245, -1.40557, -0.290106]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: N-methylpyrrolidone=0.001656, water=0.00089 [block-edges (water: direct/good, N-methylpyrrolidone: direct/good)]
      fit_csv: $ROOT/data\10_1021_je034073k_BPROPblock_3_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je034073k_BPROPblock_3_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je034073k_BPROPblock_3_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je034073k_BPROPblock_3_T298.1_excess.png
  - 2-pyrrolidinone+water [10.1021/je0340809/PROPblock_14] (water, 2-pyrrolidinone): RK order=5, R²=0.999655, RMSE=0.0060262366694878895, coeffs=[4.378425, 3.250834, 0.651499, -0.06737, 2.858243, 2.067568]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: water=0.00089, 2-pyrrolidinone=0.01302 [named (matched to composition axis)]
      fit_csv: $ROOT/data\10_1021_je0340809_BPROPblock_14_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je0340809_BPROPblock_14_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je0340809_BPROPblock_14_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je0340809_BPROPblock_14_T298.1_excess.png
  - DMF+water [10.1021/je050209y/PROPblock_9] (dimethylformamide, water): RK order=5, R²=0.999956, RMSE=0.0022827571884589492, coeffs=[3.209476, -3.931318, 1.84991, 0.364686, -0.180491, -0.64387]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: dimethylformamide=0.000802, water=0.00089 [named (matched to composition axis)]
      fit_csv: $ROOT/data\10_1021_je050209y_BPROPblock_9_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je050209y_BPROPblock_9_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je050209y_BPROPblock_9_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je050209y_BPROPblock_9_T298.1_excess.png

### Property Response Preparation
- GLOBlit_8238 | 10.1021/je034073k | PROPblock_3: direct via X = reported X (0 reference source(s))

## Session Output Files

### data
- `$ROOT/data\10_1021_je034073k_BPROPblock_3_T298.1_fit.csv` — RK fit data — 10.1021/je034073k PROPblock_3_T298.1
- `$ROOT/data\10_1021_je034073k_BPROPblock_3_T298.1_excess.csv` — Excess property — 10.1021/je034073k PROPblock_3_T298.1
- `$ROOT/data\10_1021_je0340809_BPROPblock_14_T298.1_fit.csv` — RK fit data — 10.1021/je0340809 PROPblock_14_T298.1
- `$ROOT/data\10_1021_je050209y_BPROPblock_9_T298.1_fit.csv` — RK fit data — 10.1021/je050209y PROPblock_9_T298.1
- `$ROOT/data\10_1021_je0340809_BPROPblock_14_T298.1_excess.csv` — Excess property — 10.1021/je0340809 PROPblock_14_T298.1
- `$ROOT/data\10_1021_je050209y_BPROPblock_9_T298.1_excess.csv` — Excess property — 10.1021/je050209y PROPblock_9_T298.1

### plot
- `$ROOT/plots\10_1021_je034073k_BPROPblock_3_T298.1_fit.png` — RK fit plot — 10.1021/je034073k PROPblock_3_T298.1
- `$ROOT/plots\10_1021_je034073k_BPROPblock_3_T298.1_excess.png` — Excess plot — 10.1021/je034073k PROPblock_3_T298.1
- `$ROOT/plots\10_1021_je0340809_BPROPblock_14_T298.1_fit.png` — RK fit plot — 10.1021/je0340809 PROPblock_14_T298.1
- `$ROOT/plots\10_1021_je050209y_BPROPblock_9_T298.1_fit.png` — RK fit plot — 10.1021/je050209y PROPblock_9_T298.1
- `$ROOT/plots\10_1021_je0340809_BPROPblock_14_T298.1_excess.png` — Excess plot — 10.1021/je0340809 PROPblock_14_T298.1
- `$ROOT/plots\10_1021_je050209y_BPROPblock_9_T298.1_excess.png` — Excess plot — 10.1021/je050209y PROPblock_9_T298.1

