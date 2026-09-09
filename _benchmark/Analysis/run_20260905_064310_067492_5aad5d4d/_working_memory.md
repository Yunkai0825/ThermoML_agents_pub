# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064310_067492_5aad5d4d`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_18 | dimethylformamide |  |
| comp | GLOBcomp_24 | 1,2-ethanediol |  |
| comp | GLOBcomp_1 | water |  |
| prop | GLOBprop_4 | viscositypas |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<water> |  |
| constr | GLOBconstr_1 | pressurekpa |  |
| meas | GLOBmeas_4 | capillary tube (ostwald; ubbelohde) method |  |
| lit | GLOBlit_8892 | 10.1021/je060113j |  |

### History
- [query_thermoml_parallel]
- [fit_multi_system]
- [inspect_block]
- [fit_multi_system]
- [predict_from_rk]
- [predict_from_rk]
- [list_session_files]

### Query Results
#### ternary_viscosity
**L1_query_1** — status: success · validation: PASS

**Summary:** Viscosity data for the ternary mixture of N,N-dimethylformamide (DMF) + ethylene glycol (1,2-ethanediol) + water at 298.15 K were found in the ThermoML database (DOI 10.1021/je060113j, GLOBlit_8892, PROPblock_38). Measured by capillary tube (Ostwald–Ubbelohde) in the liquid phase at 101.0 kPa, 11 data points at 298.15 K span the full water mole-fraction range from 0 to 1. Viscosity values are: x(water)=0.0000, x(ethanediol)=0.5408, η=0.0030647 Pa·s; x(water)=0.2929, x(ethanediol)=0.3824, η=0.0035692 Pa·s; x(water)=0.4825, x(ethanediol)=0.2799, η=0.0037485 Pa·s; x(water)=0.6152, x(ethanediol)=0.2081, η=0.0034817 Pa·s; x(water)=0.7132, x(ethanediol)=0.1551, η=0.0032008 Pa·s; x(water)=0.7886, x(ethanediol)=0.1143, η=0.0028546 Pa·s; x(water)=0.8484, x(ethanediol)=0.0820, η=0.0024439 Pa·s; x(water)=0.8969, x(ethanediol)=0.0557, η=0.0019531 Pa·s; x(water)=0.9372, x(ethanediol)=0.0339, η=0.0016778 Pa·s; x(water)=0.9711, x(ethanediol)=0.0156, η=0.0013057 Pa·s; x(water)=1.0000, x(ethanediol)=0.0000, η=0.0008904 Pa·s. The viscosity shows a non-monotonic trend, rising from 0.0030647 Pa·s at x(water)=0 to a maximum of 0.0037485 Pa·s near x(water)≈0.48, then decreasing to 0.0008904 Pa·s for pure water, characteristic of strongly hydrogen-bonding ternary systems. The full data block contains 33 points covering 298.15 K to 318.15 K with viscosities ranging from 0.000596 to 0.0037485 Pa·s.

**Answer:**

Viscosity data for the ternary mixture of N,N-dimethylformamide (DMF) + ethylene glycol (1,2-ethanediol) + water at 298.15 K were found in the ThermoML database.

**Source:** DOI 10.1021/je060113j (GLOBlit_8892), PROPblock_38  
**Method:** Capillary tube (Ostwald–Ubbelohde), liquid phase  
**Pressure:** 101.0 kPa (fixed constraint)  
**Compounds:** DMF (GLOBcomp_18), 1,2-ethanediol (GLOBcomp_24), water (GLOBcomp_1)

There are **11 data points at 298.15 K** spanning the full water mole-fraction range from 0 to 1 (the third component, DMF, makes up the balance). The data are tabulated below:

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *x(water)* | *x(1,2-ethanediol)* | *Viscosity (Pa·s)* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.0000」 | 「0.5408」 | 「0.0030647」 |
| WM_L1#1_Table#1_Row#2 | 「0.2929」 | 「0.3824」 | 「0.0035692」 |
| WM_L1#1_Table#1_Row#3 | 「0.4825」 | 「0.2799」 | 「0.0037485」 |
| WM_L1#1_Table#1_Row#4 | 「0.6152」 | 「0.2081」 | 「0.0034817」 |
| WM_L1#1_Table#1_Row#5 | 「0.7132」 | 「0.1551」 | 「0.0032008」 |
| WM_L1#1_Table#1_Row#6 | 「0.7886」 | 「0.1143」 | 「0.0028546」 |
| WM_L1#1_Table#1_Row#7 | 「0.8484」 | 「0.0820」 | 「0.0024439」 |
| WM_L1#1_Table#1_Row#8 | 「0.8969」 | 「0.0557」 | 「0.0019531」 |
| WM_L1#1_Table#1_Row#9 | 「0.9372」 | 「0.0339」 | 「0.0016778」 |
| WM_L1#1_Table#1_Row#10 | 「0.9711」 | 「0.0156」 | 「0.0013057」 |
| WM_L1#1_Table#1_Row#11 | 「1.0000」 | 「0.0000」 | 「0.0008904」 |

**Chemistry insight:** The viscosity exhibits a non-monotonic trend with composition. Starting from the DMF + ethylene glycol binary end (x_water = 0, η = 0.0030647 Pa·s), the viscosity increases as water is added, reaching a maximum of 0.0037485 Pa·s near x(water) ≈ 0.48. Beyond this composition, the viscosity decreases steadily as the mixture becomes more water-rich, dropping to 0.0008904 Pa·s for pure water. This maximum in viscosity at intermediate compositions is characteristic of strongly hydrogen-bonding ternary systems, where the interplay of DMF–water and ethylene glycol–water interactions enhances intermolecular association beyond what either binary pair alone would produce.

The full block contains 33 data points covering temperatures from 298.15 K to 318.15 K, with viscosity values ranging from 0.000596 to 0.0037485 Pa·s across all temperatures and compositions.

**Core claims:**
- Viscosity data for the ternary mixture DMF + ethylene glycol + water at 298.15 K and 101.0 kPa were found in the ThermoML database (DOI 10.1021/je060113j), comprising 11 data points spanning the full water mole-fraction range from 0 to 1.
- The viscosity exhibits a non-monotonic trend with composition: starting at 0.0030647 Pa·s for the DMF + ethylene glycol binary end (x_water = 0), it increases to a maximum of 0.0037485 Pa·s near x(water) ≈ 0.48, then decreases steadily to 0.0008904 Pa·s for pure water.
- The viscosity maximum at intermediate compositions is attributed to strongly hydrogen-bonding interactions in the ternary system, where DMF–water and ethylene glycol–water interactions enhance intermolecular association beyond what either binary pair alone would produce.
- The full data block contains 33 data points covering temperatures from 298.15 K to 318.15 K, with viscosity values ranging from 0.000596 to 0.0037485 Pa·s across all temperatures and compositions.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_8892」 | 「PROPblock_38」 | 「GLOBcomp_18, GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for the ternary mixture N,N-dimethylformamide + 1,2-ethanediol + water at 298.15 K and 101.0 kPa, with 11 data points spanning the full water mole-fraction range.」 |

*Not stored here: 1 verbatim data_inspections table(s); 4 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### binary_DMF_water
**L1_query_2** — status: success · validation: PASS

**Summary:** Dynamic viscosity (Pa·s) data for the binary system N,N-dimethylformamide (DMF) + water at 298.15 K were found in four data blocks. Two key blocks were inspected in detail. Block 1 (DOI 10.1021/je050209y, GLOBlit_8676::PROPblock_9) reports 11 points at 298.15 K and 101.325 kPa as a function of DMF mole fraction, with viscosities ranging from 0.000843 to 0.002491 Pa·s across x(DMF) = 0.05–0.9488. Block 2 (DOI 10.1021/je300608v, GLOBlit_9900::PROPblock_3) reports 15 points at 298.15 K and 101.0 kPa as a function of water mole fraction, with viscosities ranging from 0.0008045 to 0.0024775 Pa·s across x(water) = 0–1. Both datasets exhibit a pronounced viscosity maximum near ~30 mol% DMF / ~70 mol% water (0.002491 Pa·s in Block 1 at x(DMF) ≈ 0.3; 0.0024775 Pa·s in Block 2 at x(water) ≈ 0.7), attributed to strong DMF–water hydrogen-bonding interactions forming structured molecular associations. Two additional blocks were also returned but not inspected in detail.

**Answer:**

#### Dynamic Viscosity Data for Binary DMF + Water Mixtures near 298.15 K

**Compounds:** N,N-dimethylformamide (DMF, GLOBcomp_18) and water (GLOBcomp_1)  
**Property:** Dynamic viscosity (GLOBprop_4, Pa·s)  
**System type:** Binary

##### Data Blocks Found

Four blocks of dynamic viscosity data for binary DMF + water were identified. Two key blocks with inspected data at 298.15 K are detailed below:

---

**Block 1: GLOBlit_8676 :: PROPblock_9**  
DOI: 10.1021/je050209y  
Total points: 11 | Temperature: 298.15 K (fixed) | Pressure: 101.325 kPa  
Composition variable: mole fraction of DMF

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *x(DMF)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0.05」 | 「0.00131」 |
| WM_L1#2_Table#1_Row#2 | 「0.1001」 | 「0.001728」 |
| WM_L1#2_Table#1_Row#3 | 「0.2」 | 「0.002346」 |
| WM_L1#2_Table#1_Row#4 | 「0.299」 | 「0.002491」 |
| WM_L1#2_Table#1_Row#5 | 「0.3998」 | 「0.002273」 |
| WM_L1#2_Table#1_Row#6 | 「0.4997」 | 「0.001878」 |
| WM_L1#2_Table#1_Row#7 | 「0.5993」 | 「0.001532」 |
| WM_L1#2_Table#1_Row#8 | 「0.6995」 | 「0.001243」 |
| WM_L1#2_Table#1_Row#9 | 「0.8」 | 「0.001045」 |
| WM_L1#2_Table#1_Row#10 | 「0.8991」 | 「0.000901」 |
| WM_L1#2_Table#1_Row#11 | 「0.9488」 | 「0.000843」 |

Viscosity range: 0.000843–0.002491 Pa·s across x(DMF) = 0.05–0.9488.

---

**Block 2: GLOBlit_9900 :: PROPblock_3**  
DOI: 10.1021/je300608v  
Total points: 60 (full block, 293.15–308.15 K) | 15 points at 298.15 K | Pressure: 101.0 kPa  
Composition variable: mole fraction of water

**WM_L1#2_Table#2_(Analysis_L1#2_Answer):**

| *row_id* | *x(water)* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「0」 | 「0.0008045」 |
| WM_L1#2_Table#2_Row#2 | 「0.1」 | 「0.0009018」 |
| WM_L1#2_Table#2_Row#3 | 「0.2」 | 「0.0010386」 |
| WM_L1#2_Table#2_Row#4 | 「0.3」 | 「0.0012331」 |
| WM_L1#2_Table#2_Row#5 | 「0.4」 | 「0.0015078」 |
| WM_L1#2_Table#2_Row#6 | 「0.5」 | 「0.0018528」 |
| WM_L1#2_Table#2_Row#7 | 「0.6」 | 「0.0022264」 |
| WM_L1#2_Table#2_Row#8 | 「0.7」 | 「0.0024775」 |
| WM_L1#2_Table#2_Row#9 | 「0.8」 | 「0.0023495」 |
| WM_L1#2_Table#2_Row#10 | 「0.9」 | 「0.0017464」 |
| WM_L1#2_Table#2_Row#11 | 「0.94」 | 「0.0014116」 |
| WM_L1#2_Table#2_Row#12 | 「1」 | 「0.0008903」 |

Viscosity range at 298.15 K: 0.0008045–0.0024775 Pa·s across x(water) = 0–1.

---

Two additional blocks were also returned in the search (4 total), including one from GLOBlit_11030 (temperature range not inspected in this run).

**Chemistry insight:** Both datasets show a pronounced viscosity maximum at intermediate compositions — near x(DMF) ≈ 0.3 in Block 1 (GLOBlit_8676::PROPblock_9, 0.002491 Pa·s) and near x(water) ≈ 0.7 in Block 2 (GLOBlit_9900::PROPblock_3, 0.0024775 Pa·s). These correspond to the same composition region (~30 mol% DMF / 70 mol% water), consistent with strong DMF–water hydrogen-bonding interactions that create structured molecular associations and enhance viscous resistance to flow at these intermediate compositions.

**Core claims:**
- Four blocks of dynamic viscosity data for binary DMF + water mixtures were identified, with two key blocks providing detailed measurements at 298.15 K and near-ambient pressure.
- Block 1 (DOI: 10.1021/je050209y) reports 11 viscosity values at 298.15 K and 101.325 kPa spanning x(DMF) = 0.05–0.9488, with viscosity ranging from 0.000843 to 0.002491 Pa·s.
- Block 2 (DOI: 10.1021/je300608v) reports 12 viscosity values at 298.15 K and 101.0 kPa spanning x(water) = 0–1, with viscosity ranging from 0.0008045 to 0.0024775 Pa·s.
- Both datasets show a pronounced viscosity maximum at intermediate compositions near ~30 mol% DMF / 70 mol% water (0.002491 Pa·s in Block 1 at x(DMF) ≈ 0.3; 0.0024775 Pa·s in Block 2 at x(water) ≈ 0.7), consistent with strong DMF–water hydrogen-bonding interactions that create structured molecular associations and enhance viscous resistance to flow.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#3 | 「GLOBlit_8676」 | 「PROPblock_9」 | 「GLOBcomp_18, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary DMF + water at 298.15 K and 101.325 kPa as a function of DMF mole fraction (11 points, viscosity range 0.000843–0.002491 Pa·s).」 |
| WM_L1#2_Table#4 | 「GLOBlit_9900」 | 「PROPblock_3」 | 「GLOBcomp_18, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary DMF + water at 293.15–308.15 K and 101.0 kPa as a function of water mole fraction (60 total points, 15 at 298.15 K, viscosity range at 298.15 K: 0.0008045–0.0024775 Pa·s).」 |

*Not stored here: 2 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### binary_DMF_EG
**L1_query_3** — status: success · validation: PASS

**Summary:** A single data block from DOI 10.1021/je060113j (GLOBlit_8892, PROPblock_25) reports the dynamic viscosity of the binary system N,N-dimethylformamide (DMF) + 1,2-ethanediol (ethylene glycol) at a fixed mole fraction of 1,2-ethanediol = 0.5408 and 101.0 kPa, measured by capillary tube method in the liquid phase. Three data points are provided: at 298.15 K the viscosity is 0.0030647 Pa·s, at 308.15 K it is 0.0024529 Pa·s, and at 318.15 K it is 0.0019599 Pa·s. Viscosity decreases monotonically with increasing temperature. No additional composition-sweep blocks were found for this binary system in the database.

**Answer:**

**Viscosity data for binary DMF + ethylene glycol mixtures near 298.15 K**

One data block was found in the ThermoML database for the dynamic viscosity of the binary system N,N-dimethylformamide (DMF) + 1,2-ethanediol (ethylene glycol):

- **DOI:** 10.1021/je060113j (GLOBlit_8892)
- **Block:** PROPblock_25
- **Compounds:** GLOBcomp_18 (dimethylformamide), GLOBcomp_24 (1,2-ethanediol)
- **Property:** Dynamic viscosity (GLOBprop_4), measured by capillary tube method (GLOBmeas_4), liquid phase
- **Composition:** Fixed mole fraction of 1,2-ethanediol = 0.5408
- **Pressure:** 101.0 kPa

The block contains 3 data points at three temperatures:

**WM_L1#3_Table#1_(Analysis_L1#3_Answer):**

| *row_id* | *BLKpoint_id* | *Temperature (K)* | *x(1,2-ethanediol)* | *Pressure (kPa)* | *Viscosity (Pa·s)* |
|---|---|---|---|---|---|
| WM_L1#3_Table#1_Row#1 | 「BLKpoint_1」 | 「298.15」 | 「0.5408」 | 「101.0」 | 「0.0030647」 |
| WM_L1#3_Table#1_Row#2 | 「BLKpoint_2」 | 「308.15」 | 「0.5408」 | 「101.0」 | 「0.0024529」 |
| WM_L1#3_Table#1_Row#3 | 「BLKpoint_3」 | 「318.15」 | 「0.5408」 | 「101.0」 | 「0.0019599」 |

At exactly 298.15 K, the viscosity is **0.0030647 Pa·s** (≈ 3.06 mPa·s).

**Chemistry note:** The viscosity decreases monotonically with increasing temperature (near-linear, R² = 0.9962), as expected for liquid mixtures. This block provides data at only one composition (x_EG = 0.5408); no additional composition-sweep blocks were found for this binary system in the database.

**Core claims:**
- In the ThermoML database (DOI 10.1021/je060113j), the dynamic viscosity of the binary DMF + ethylene glycol mixture at a fixed 1,2-ethanediol mole fraction of 0.5408 and 101.0 kPa is reported as 0.0030647 Pa·s at 298.15 K, 0.0024529 Pa·s at 308.15 K, and 0.0019599 Pa·s at 318.15 K, decreasing monotonically with increasing temperature consistent with expected liquid-mixture behavior, with only one composition (x_EG = 0.5408) available for this binary system in the database.

**Core blocks found:**

**WM_L1#3_Blocks_(Analysis_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#2 | 「GLOBlit_8892」 | 「PROPblock_25」 | 「GLOBcomp_18, GLOBcomp_24」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary dimethylformamide + 1,2-ethanediol at 298.15–318.15 K, fixed x(1,2-ethanediol) = 0.5408, 101.0 kPa, capillary tube method.」 |

*Not stored here: 1 verbatim data_inspections table(s); 5 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### binary_EG_water
**L1_query_4** — status: success · validation: FLAGGED(2)

**Summary:** Dynamic viscosity (GLOBprop_4, Pa·s) data for binary mixtures of ethylene glycol (GLOBcomp_24, OCCO) and water (GLOBcomp_1) near 298.15 K were identified across five data blocks. The most data-rich blocks are GLOBlit_5201::PROPblock_24 (84 points, 293.15–308.15 K, mole fraction EG, 92.3 kPa) and GLOBlit_8038::PROPblock_5 (77 points, 293.15–353.15 K, mole fraction EG, 101.0 kPa). Additional blocks include GLOBlit_2656::PROPblock_13 (10 points at 293.15 K, mass fraction EG, 101.325 kPa), GLOBlit_6951::PROPblock_18 (33 points, 293.15–303.15 K, mole fraction water, 100.0 kPa), and GLOBlit_8106::PROPblock_5 (30 points, 296.45–449.85 K, mole fraction EG, 100.0 kPa). Representative values at 298.15 K from GLOBlit_5201::PROPblock_24: pure water viscosity 0.00089689 Pa·s, mole fraction EG 0.2072 gives 0.0028109 Pa·s, mole fraction EG 0.4446 gives 0.0060624 Pa·s, pure EG gives 0.016223 Pa·s. From GLOBlit_6951::PROPblock_18 at 298.15 K: pure EG (mole fraction water 0) gives 0.01724 Pa·s, mole fraction water 0.2014 gives 0.01219 Pa·s, mole fraction water 0.4011 gives 0.00831 Pa·s, mole fraction water 0.6995 gives 0.003884 Pa·s, pure water gives 0.000843 Pa·s. Viscosity increases strongly and nonlinearly with ethylene glycol content, reflecting the extensive hydrogen-bonding network of its two hydroxyl groups.

**Answer:**

**Viscosity data for binary ethylene glycol (1,2-ethanediol) + water mixtures near 298.15 K**

**Compounds resolved:**
- Ethylene glycol (1,2-ethanediol): **GLOBcomp_24** (C₂H₆O₂, SMILES: OCCO)
- Water: **GLOBcomp_1** (H₂O)

**Property:** Dynamic viscosity (GLOBprop_4), units: Pa·s

Five inspected data blocks were found for binary liquid-phase mixtures covering temperatures near 298.15 K:

**WM_L1#4_Table#1_(Analysis_L1#4_Answer):**

| *row_id* | *#* | *DOI* | *Block* | *Literature ID* | *Data Points* | *T range (K)* | *Composition Variable* | *P (kPa)* |
|---|---|---|---|---|---|---|---|---|
| WM_L1#4_Table#1_Row#1 | 「1」 | 「10.1016/j.jct.2006.01.011」 | 「PROPblock_13」 | 「GLOBlit_2656」 | 「10」 | 「293.15–293.15」 | 「mass fraction EG (GLOBcomp_24)」 | 「101.325」 |
| WM_L1#4_Table#1_Row#2 | 「2」 | 「10.1016/j.jct.2018.02.022」 | 「PROPblock_24」 | 「GLOBlit_5201」 | 「84」 | 「293.15–308.15」 | 「mole fraction EG (GLOBcomp_24)」 | 「92.3」 |
| WM_L1#4_Table#1_Row#3 | 「3」 | 「10.1021/acs.jced.6b00526」 | 「PROPblock_18」 | 「GLOBlit_6951」 | 「33」 | 「293.15–303.15」 | 「mole fraction water (GLOBcomp_1)」 | 「100.0」 |
| WM_L1#4_Table#1_Row#4 | 「4」 | 「10.1021/je020140j」 | 「PROPblock_5」 | 「GLOBlit_8038」 | 「77」 | 「293.15–353.15」 | 「mole fraction EG (GLOBcomp_24)」 | 「101.0」 |
| WM_L1#4_Table#1_Row#5 | 「5」 | 「10.1021/je025610o」 | 「PROPblock_5」 | 「GLOBlit_8106」 | 「30」 | 「296.45–449.85」 | 「mole fraction EG (GLOBcomp_24)」 | 「100.0」 |

A sixth block was also matched in the initial search but its details were truncated; the five blocks above were fully inspected.

**Representative data near 298.15 K:**

From GLOBlit_5201::PROPblock_24 (at 298.15 K, 92.3 kPa):

**WM_L1#4_Table#2_(Analysis_L1#4_Answer):**

| *row_id* | *Mole fraction EG* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#4_Table#2_Row#1 | 「0」 | 「0.00089689」 |
| WM_L1#4_Table#2_Row#2 | 「0.2072」 | 「0.0028109」 |
| WM_L1#4_Table#2_Row#3 | 「0.4446」 | 「0.0060624」 |
| WM_L1#4_Table#2_Row#4 | 「1」 | 「0.016223」 |

From GLOBlit_6951::PROPblock_18 (at 298.15 K, 100.0 kPa):

**WM_L1#4_Table#3_(Analysis_L1#4_Answer):**

| *row_id* | *Mole fraction water* | *Viscosity (Pa·s)* |
|---|---|---|
| WM_L1#4_Table#3_Row#1 | 「0」 | 「0.01724」 |
| WM_L1#4_Table#3_Row#2 | 「0.2014」 | 「0.01219」 |
| WM_L1#4_Table#3_Row#3 | 「0.4011」 | 「0.00831」 |
| WM_L1#4_Table#3_Row#4 | 「0.6995」 | 「0.003884」 |
| WM_L1#4_Table#3_Row#5 | 「1」 | 「0.000843」 |

**Chemistry insight:** The viscosity of ethylene glycol–water mixtures increases strongly and nonlinearly with ethylene glycol content. In GLOBlit_5201::PROPblock_24 at 298.15 K, pure EG viscosity is 0.016223 Pa·s versus 0.00089689 Pa·s for pure water (a ratio of approximately 18×, derived by division). In GLOBlit_6951::PROPblock_18 at 298.15 K, pure EG viscosity is 0.01724 Pa·s versus 0.000843 Pa·s for pure water (a ratio of approximately 20×, derived by division). This reflects the extensive hydrogen-bonding network formed by the two hydroxyl groups of ethylene glycol. The most data-rich blocks near 298.15 K are GLOBlit_5201::PROPblock_24 (84 points, 293.15–308.15 K) and GLOBlit_8038::PROPblock_5 (77 points, 293.15–353.15 K), both using mole fraction of ethylene glycol as the composition variable.

**Core claims:**
- Five ThermoML data blocks were identified containing dynamic viscosity data for binary ethylene glycol (1,2-ethanediol) + water liquid mixtures near 298.15 K, with the most data-rich blocks being GLOBlit_5201::PROPblock_24 (84 points, 293.15–308.15 K) and GLOBlit_8038::PROPblock_5 (77 points, 293.15–353.15 K).
- At 298.15 K, the viscosity of ethylene glycol–water mixtures increases strongly and nonlinearly with ethylene glycol content; in GLOBlit_5201::PROPblock_24 pure EG viscosity is 0.016223 Pa·s versus 0.00089689 Pa·s for pure water, and in GLOBlit_6951::PROPblock_18 pure EG viscosity is 0.01724 Pa·s versus 0.000843 Pa·s for pure water.
- The strong increase in viscosity with ethylene glycol content is attributed to the extensive hydrogen-bonding network formed by the two hydroxyl groups of ethylene glycol.

**Core blocks found:**

**WM_L1#4_Blocks_(Analysis_L1#4_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#4_Table#4 | 「GLOBlit_2656」 | 「PROPblock_13」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary ethylene glycol + water at 293.15 K, mass fraction composition, 101.325 kPa.」 |
| WM_L1#4_Table#5 | 「GLOBlit_5201」 | 「PROPblock_24」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary ethylene glycol + water, 293.15–308.15 K, mole fraction composition, 92.3 kPa. 84 data points.」 |
| WM_L1#4_Table#6 | 「GLOBlit_6951」 | 「PROPblock_18」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary ethylene glycol + water, 293.15–303.15 K, mole fraction of water composition, 100.0 kPa. 33 data points.」 |
| WM_L1#4_Table#7 | 「GLOBlit_8038」 | 「PROPblock_5」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary ethylene glycol + water, 293.15–353.15 K, mole fraction composition, 101.0 kPa. 77 data points.」 |
| WM_L1#4_Table#8 | 「GLOBlit_8106」 | 「PROPblock_5」 | 「GLOBcomp_24, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of binary ethylene glycol + water, 296.45–449.85 K, mole fraction composition, 100.0 kPa. 30 data points.」 |

*Not stored here: 5 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **AMBIGUOUS_VALUE** PROPblock_5: 298.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **UNINSPECTED_VALUE** GLOBlit_5201::PROPblock_24: 18 exists in PROPblock_24's database table but was never shown in an inspection of this run


### Inspected Blocks
- GLOBlit_9900 | 10.1021/je300608v | PROPblock_3: 60 rows; x=['mole_fraction_<water>']; y=['viscosity_pa_s']
    - BLKprop_1 / GLOBprop_4: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_4: kind=direct; materialize_reference=False; supported=True; units=Pa*s -> Pa*s

### Completed Fits
  - DMF_water [10.1021/je300608v/PROPblock_3] (water, dimethylformamide): RK order=5, R²=0.999973, RMSE=0.0015230866140327202, coeffs=[3.140292, 3.885439, 1.915786, -0.005693, 0.041789, 0.390893]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: water=0.0008903, dimethylformamide=0.0008045 [block-edges (dimethylformamide: direct/good, water: direct/good)]
      fit_csv: $ROOT/data\10_1021_je300608v_BPROPblock_3_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je300608v_BPROPblock_3_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je300608v_BPROPblock_3_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je300608v_BPROPblock_3_T298.1_excess.png
  - EG_water [10.1016/j.jct.2018.02.022/PROPblock_24] (1,2-ethanediol, water): RK order=3, R²=0.99994, RMSE=0.0013198945265291695, coeffs=[2.39674, -1.044444, 0.668173, -0.3209]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: 1,2-ethanediol=0.016223, water=0.00089689 [block-edges (water: direct/good, 1,2-ethanediol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1021_je300608v_BPROPblock_3_T298.1_fit.csv` — RK fit data — 10.1021/je300608v PROPblock_3_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- `$ROOT/data\10_1021_je300608v_BPROPblock_3_T298.1_excess.csv` — Excess property — 10.1021/je300608v PROPblock_3_T298.1

### plot
- `$ROOT/plots\10_1021_je300608v_BPROPblock_3_T298.1_fit.png` — RK fit plot — 10.1021/je300608v PROPblock_3_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1
- `$ROOT/plots\10_1021_je300608v_BPROPblock_3_T298.1_excess.png` — Excess plot — 10.1021/je300608v PROPblock_3_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_24_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_24_T298.1

