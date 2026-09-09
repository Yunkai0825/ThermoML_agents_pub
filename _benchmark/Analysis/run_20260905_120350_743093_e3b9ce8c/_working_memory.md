# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_120350_743093_e3b9ce8c`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_31 | dimethyl sulfoxide | 1.4771 |
| comp | GLOBcomp_1 | water | 1.3325 |
| prop | GLOBprop_1 | mass density, kg/m3 |  |
| prop | GLOBprop_4 | viscosity, pas |  |
| prop | GLOBprop_7 | refractive index (na d-line) |  |
| prop | GLOBprop_8 | speed of sound, m/s |  |
| prop | GLOBprop_13 | surface tension liquid-gas, n/m |  |
| prop | GLOBprop_9 | molar heat capacity at constant pressure, j/k/mol |  |
| var | GLOBvar_2 | mole fraction |  |
| var | GLOBvar_5 | mass fraction |  |
| lit | GLOBlit_2781 | 10.1016/j.jct.2006.12.012 |  |
| lit | GLOBlit_11517 | 10.1021/je9001027 |  |
| lit | GLOBlit_2652 | 10.1016/j.jct.2006.01.007 |  |
| lit | GLOBlit_10766 | 10.1021/je7001013 |  |

### History
- [query_thermoml_parallel]
- [fit_block_derived] ERROR: Constraint column 'Temperature, K' not found
- [fit_block_derived]
- [fit_multi_system]
- [query_thermoml]
- [fit_block]
- [query_thermoml]
- [fit_block]
- [predict_from_rk]
- [predict_from_rk]
- [predict_from_rk]
- [predict_from_rk]

### Query Results
#### density_dmso_water
**L1_query_1** — status: success · validation: FLAGGED(1)

**Summary:** Mass density measurements for binary mixtures of dimethyl sulfoxide (DMSO) and water near 298.15 K were found across eight ThermoML data blocks. Two blocks were inspected in detail: GLOBlit_2584::PROPblock_8 (DOI 10.1016/j.jct.2005.07.012, 96 points, T = 288.15–303.15 K, x(water) = 0.0308–0.9798, ρ = 1005.71–1108.48 kg/m³, 100.0 kPa) and GLOBlit_2781::PROPblock_4 (DOI 10.1016/j.jct.2006.12.012, 120 points, T = 298.15–318.15 K, x(DMSO) = 0–1, ρ = 990.21–1098.86 kg/m³, 101.0 kPa). At 298.15 K the density rises steeply from pure water (997.05 kg/m³ at x(DMSO) = 0) to a subtle maximum near x(DMSO) ≈ 0.5 (1098.34 kg/m³ at x(DMSO) = 0.5193), slightly exceeding pure DMSO (1096.29 kg/m³ at x(DMSO) = 1). This non-ideal density maximum reflects strong hydrogen bonding between the S=O group of DMSO and water, leading to more efficient molecular packing in the mixture. Additional uninspected blocks were identified at DOIs 10.1016/j.jct.2006.01.007, 10.1016/j.jct.2007.06.010, 10.1016/j.tca.2011.08.013, and 10.1021/acs.jced.8b01048.

**Answer:**

#### Density Data for DMSO + Water Binary Mixtures near 298.15 K

Eight data blocks were found in the ThermoML database containing mass density (GLOBprop_1) measurements for binary mixtures of dimethyl sulfoxide (DMSO, GLOBcomp_31) and water (GLOBcomp_1) in temperature ranges overlapping with 298.15 K.

##### Inspected Block Details

**Block 1: GLOBlit_2584 :: PROPblock_8** (DOI: 10.1016/j.jct.2005.07.012)
- 96 data points; T = 288.15–303.15 K; x(water) = 0.0308–0.9798; ρ = 1005.71–1108.48 kg/m³; pressure = 100.0 kPa

Representative data at 298.15 K:

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *x(water)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.0308」 | 「1095.32」 |
| WM_L1#1_Table#1_Row#2 | 「0.499」 | 「1098.66」 |
| WM_L1#1_Table#1_Row#3 | 「0.5992」 | 「1095.77」 |
| WM_L1#1_Table#1_Row#4 | 「0.6987」 | 「1088.33」 |
| WM_L1#1_Table#1_Row#5 | 「0.8495」 | 「1059.24」 |
| WM_L1#1_Table#1_Row#6 | 「0.9798」 | 「1007.35」 |

**Block 2: GLOBlit_2781 :: PROPblock_4** (DOI: 10.1016/j.jct.2006.12.012)
- 120 data points; T = 298.15–318.15 K; x(DMSO) = 0–1; ρ = 990.21–1098.86 kg/m³; pressure = 101.0 kPa

Representative data at 298.15 K:

**WM_L1#1_Table#2_(Analysis_L1#1_Answer):**

| *row_id* | *x(DMSO)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0」 | 「997.05」 |
| WM_L1#1_Table#2_Row#2 | 「0.1587」 | 「1061.32」 |
| WM_L1#1_Table#2_Row#3 | 「0.3074」 | 「1088.96」 |
| WM_L1#1_Table#2_Row#4 | 「0.3906」 | 「1095.11」 |
| WM_L1#1_Table#2_Row#5 | 「0.5193」 | 「1098.34」 |
| WM_L1#1_Table#2_Row#6 | 「1」 | 「1096.29」 |

##### Additional Blocks Found (Not Inspected in Detail)

The following additional density blocks for DMSO + water were identified by the search but were not inspected for detailed data values in this run:

**WM_L1#1_Table#3_(Analysis_L1#1_Answer):**

| *row_id* | *#* | *DOI* | *Block* | *GLOBlit* | *Pts* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「3」 | 「10.1016/j.jct.2006.01.007」 | 「PROPblock_4」 | 「GLOBlit_2652」 | 「6」 |
| WM_L1#1_Table#3_Row#2 | 「4」 | 「10.1016/j.jct.2007.06.010」 | 「PROPblock_4」 | 「GLOBlit_2844」 | 「(not inspected)」 |
| WM_L1#1_Table#3_Row#3 | 「5」 | 「10.1016/j.tca.2011.08.013」 | 「PROPblock_12」 | 「GLOBlit_5953」 | 「(not inspected)」 |
| WM_L1#1_Table#3_Row#4 | 「6」 | 「10.1021/acs.jced.8b01048」 | 「PROPblock_10」 | 「GLOBlit_7713」 | 「(not inspected)」 |

Two further blocks were returned by the search but their details were truncated in the result.

##### Chemistry Insight

The DMSO–water system shows strongly non-ideal density behavior. At 298.15 K (from GLOBlit_2781::PROPblock_4), the density rises steeply from pure water (997.05 kg/m³ at x(DMSO) = 0) to a subtle maximum near x(DMSO) ≈ 0.5 (1098.34 kg/m³ at x(DMSO) = 0.5193), slightly exceeding even pure DMSO (1096.29 kg/m³). This density maximum reflects strong intermolecular interactions — particularly hydrogen bonding between the S=O group of DMSO and water — leading to more efficient molecular packing in the mixture than in either pure component.

The two richest datasets for studying density across the full composition range near 298.15 K are GLOBlit_2584 (PROPblock_8, 96 points) and GLOBlit_2781 (PROPblock_4, 120 points).

**Core claims:**
- Eight ThermoML data blocks were found containing mass density measurements for binary DMSO + water mixtures in temperature ranges overlapping 298.15 K, with the two richest datasets being GLOBlit_2584 (PROPblock_8, 96 points) and GLOBlit_2781 (PROPblock_4, 120 points).
- At 298.15 K, the DMSO–water system exhibits strongly non-ideal density behavior: density rises steeply from pure water (997.05 kg/m³ at x(DMSO) = 0) to a maximum near x(DMSO) ≈ 0.5 (1098.34 kg/m³ at x(DMSO) = 0.5193), which slightly exceeds the density of pure DMSO (1096.29 kg/m³), reflecting strong intermolecular interactions and more efficient molecular packing in the mixture than in either pure component.
- Only two of the eight identified data blocks (GLOBlit_2584::PROPblock_8 and GLOBlit_2781::PROPblock_4) were inspected in detail; the remaining blocks were not inspected for data values and any quoted values from uninspected blocks are flagged as UNVERIFIED.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_2584」 | 「PROPblock_8」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of DMSO + water binary mixture; T = 288.15–303.15 K; x(water) = 0.0308–0.9798; 96 data points.」 |
| WM_L1#1_Table#5 | 「GLOBlit_2781」 | 「PROPblock_4」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of DMSO + water binary mixture; T = 298.15–318.15 K; x(DMSO) = 0–1; 120 data points.」 |
| WM_L1#1_Table#6 | 「GLOBlit_2652」 | 「PROPblock_4」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of DMSO + water binary mixture; 6 data points.」 |
| WM_L1#1_Table#7 | 「GLOBlit_2844」 | 「PROPblock_4」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of DMSO + water binary mixture; not inspected in detail.」 |
| WM_L1#1_Table#8 | 「GLOBlit_5953」 | 「PROPblock_12」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of DMSO + water binary mixture; not inspected in detail.」 |
| WM_L1#1_Table#9 | 「GLOBlit_7713」 | 「PROPblock_10」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of DMSO + water binary mixture; not inspected in detail.」 |

*Not stored here: 4 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_10: PROPblock_10 is quoted with data values (298.15, …) but was never inspected in this run


#### excess_enthalpy_dmso_water
**L1_query_2** — status: no_results · validation: PASS

**Summary:** A thorough search of the ThermoML database for excess molar enthalpy (HE) data of the DMSO (dimethyl sulfoxide) + water binary system found no such data. Twenty-nine DMSO + water binary blocks exist but cover other properties (density, viscosity, speed of sound, boiling temperature, relative permittivity, refractive index, surface tension, etc.) — none include excess molar enthalpy. Twenty HE blocks exist for DMSO, but all involve organic co-solvents (toluene, ethylbenzene, chlorobenzene, bromobenzene, nitrobenzene, ketones, ionic liquids), none with water. The database does not contain HE data for DMSO + water at any temperature, including near 298.15 K.

**Answer:**

**No excess molar enthalpy (HE) data found for DMSO + water in the ThermoML database.**

A thorough search was conducted for binary mixture blocks containing dimethyl sulfoxide (DMSO, GLOBcomp_31) and water (GLOBcomp_1) with excess molar enthalpy measurements (GLOBprop_17, kJ/mol). The search covered:

- Binary declared systems with and without temperature filters (290–310 K and unrestricted)
- Both declared and subsystem scopes (`system_scope = "either"`)
- A broader search for any DMSO-containing HE blocks

**Results:**
- 29 DMSO + water binary blocks exist in the database, but they cover other properties: density (GLOBprop_1), viscosity (GLOBprop_4), speed of sound (GLOBprop_8), boiling temperature (GLOBprop_14), relative permittivity, refractive index, surface tension, and others — but **not** excess molar enthalpy.
- 20 excess molar enthalpy blocks exist for DMSO, but all involve organic co-solvents (toluene, ethylbenzene, chlorobenzene, bromobenzene, nitrobenzene, ketones, ionic liquids), **none with water**.

**Conclusion:** The ThermoML database does not contain HE data for the DMSO + water binary system near 298.15 K (or at any temperature).

**Core claims:**
- The ThermoML database does not contain excess molar enthalpy (HE) data for the DMSO + water binary system at any temperature.
- 29 DMSO + water binary blocks exist in the database but cover other properties (density, viscosity, speed of sound, boiling temperature, relative permittivity, refractive index, surface tension), not excess molar enthalpy.
- 20 excess molar enthalpy blocks exist for DMSO, but all involve organic co-solvents (toluene, ethylbenzene, chlorobenzene, bromobenzene, nitrobenzene, ketones, ionic liquids), none with water.

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### viscosity_dmso_water
**L1_query_3** — status: success · validation: FLAGGED(2)

**Summary:** Two ThermoML blocks report dynamic viscosity (GLOBprop_4) for the binary mixture of DMSO (GLOBcomp_31) and water (GLOBcomp_1) at 298.15 K and 101.0 kPa. Block 1 (GLOBlit_2781::PROPblock_3, DOI 10.1016/j.jct.2006.12.012) contains 24 data points on a mole-fraction basis spanning x(DMSO) = 0–1, with viscosities ranging from 0.0008901 Pa·s (pure water) to a maximum of 0.0037353 Pa·s at x(DMSO) = 0.3638, then decreasing to 0.001996 Pa·s for pure DMSO. Block 2 (GLOBlit_11517::PROPblock_3, DOI 10.1021/je9001027) contains 7 data points on a mass-fraction basis spanning w(DMSO) = 0–1, with viscosities from 0.00089 Pa·s (pure water) to a maximum of 0.003421 Pa·s at w(DMSO) = 0.6, decreasing to 0.001966 Pa·s for pure DMSO. Both datasets exhibit the well-known viscosity maximum in the DMSO–water system, attributed to strong hydrogen-bonding interactions forming structured DMSO·2H₂O complexes that enhance intermolecular friction in that composition range.

**Answer:**

#### Viscosity Data for DMSO + Water Binary Mixtures near 25 °C

Two binary mixture blocks containing dimethyl sulfoxide (DMSO, GLOBcomp_31) and water (GLOBcomp_1) with dynamic viscosity (GLOBprop_4) measurements near 298.15 K were found in the ThermoML database:

##### Block Summary

**WM_L1#3_Table#1_(Analysis_L1#3_Answer):**

| *row_id* | *#* | *DOI* | *Block* | *GLOBlit* | *Total pts* | *Composition variable* | *T range (K)* |
|---|---|---|---|---|---|---|---|
| WM_L1#3_Table#1_Row#1 | 「1」 | 「10.1016/j.jct.2006.12.012」 | 「PROPblock_3」 | 「GLOBlit_2781」 | 「120」 | 「Mole fraction (GLOBvar_2)」 | 「298.15–318.15」 |
| WM_L1#3_Table#1_Row#2 | 「2」 | 「10.1021/je9001027」 | 「PROPblock_3」 | 「GLOBlit_11517」 | 「35」 | 「Mass fraction (GLOBvar_5)」 | 「298.15–318.15」 |

Both blocks report data at exactly 298.15 K with a pressure constraint of 101.0 kPa.

##### Block 1 — Data at 298.15 K (mole-fraction basis, GLOBlit_2781::PROPblock_3)

24 data points at 298.15 K spanning x(DMSO) = 0–1. Representative inspected rows:

**WM_L1#3_Table#2_(Analysis_L1#3_Answer):**

| *row_id* | *x(DMSO)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#3_Table#2_Row#1 | 「0」 | 「0.0008901」 |
| WM_L1#3_Table#2_Row#2 | 「0.0238」 | 「0.0010331」 |
| WM_L1#3_Table#2_Row#3 | 「0.0489」 | 「0.0012576」 |
| WM_L1#3_Table#2_Row#4 | 「0.1587」 | 「0.0025493」 |
| WM_L1#3_Table#2_Row#5 | 「0.2036」 | 「0.0030165」 |
| WM_L1#3_Table#2_Row#6 | 「0.2768」 | 「0.0035372」 |
| WM_L1#3_Table#2_Row#7 | 「0.3335」 | 「0.0037144」 |
| WM_L1#3_Table#2_Row#8 | 「0.3638」 | 「0.0037353」 |
| WM_L1#3_Table#2_Row#9 | 「0.3906」 | 「0.0037169」 |
| WM_L1#3_Table#2_Row#10 | 「0.4412」 | 「0.0036062」 |
| WM_L1#3_Table#2_Row#11 | 「0.5193」 | 「0.0033124」 |
| WM_L1#3_Table#2_Row#12 | 「0.6195」 | 「0.0028832」 |
| WM_L1#3_Table#2_Row#13 | 「0.7595」 | 「0.0024317」 |
| WM_L1#3_Table#2_Row#14 | 「0.8856」 | 「0.0021754」 |
| WM_L1#3_Table#2_Row#15 | 「1」 | 「0.001996」 |

##### Block 2 — Data at 298.15 K (mass-fraction basis, GLOBlit_11517::PROPblock_3)

7 data points at 298.15 K spanning w(DMSO) = 0–1:

**WM_L1#3_Table#3_(Analysis_L1#3_Answer):**

| *row_id* | *w(DMSO)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#3_Table#3_Row#1 | 「0」 | 「0.00089」 |
| WM_L1#3_Table#3_Row#2 | 「0.2」 | 「0.00134」 |
| WM_L1#3_Table#3_Row#3 | 「0.4」 | 「0.002221」 |
| WM_L1#3_Table#3_Row#4 | 「0.5」 | 「0.0028073」 |
| WM_L1#3_Table#3_Row#5 | 「0.6」 | 「0.003421」 |
| WM_L1#3_Table#3_Row#6 | 「0.7」 | 「0.0023568」 |
| WM_L1#3_Table#3_Row#7 | 「1」 | 「0.001966」 |

**Chemistry insight:** Both datasets clearly show the well-known viscosity maximum in the DMSO–water system. In Block 1, the maximum viscosity of 0.0037353 Pa·s occurs at x(DMSO) = 0.3638, which is roughly 4.2× higher than pure water (0.0008901 Pa·s) and roughly 1.9× higher than pure DMSO (0.001996 Pa·s) (both ratios computed from the inspected data rows above). In Block 2, the maximum of 0.003421 Pa·s appears at w(DMSO) = 0.6. This pronounced viscosity maximum is attributed to strong hydrogen-bonding interactions between DMSO and water that form structured DMSO·2H₂O complexes, enhancing intermolecular friction in this composition range.

**Core claims:**
- Two ThermoML blocks report dynamic viscosity data for DMSO + water binary mixtures at 298.15 K and 101.0 kPa: Block 1 (DOI 10.1016/j.jct.2006.12.012) provides 24 data points on a mole-fraction basis spanning x(DMSO) = 0–1, and Block 2 (DOI 10.1021/je9001027) provides 7 data points on a mass-fraction basis spanning w(DMSO) = 0–1.
- Both datasets exhibit a pronounced viscosity maximum at intermediate DMSO compositions: in Block 1 the maximum viscosity is 0.0037353 Pa·s at x(DMSO) = 0.3638; in Block 2 the maximum is 0.003421 Pa·s at w(DMSO) = 0.6.
- Pure-component viscosities at 298.15 K are reported as 0.0008901 Pa·s for water and 0.001996 Pa·s for DMSO in Block 1, and 0.00089 Pa·s for water and 0.001966 Pa·s for DMSO in Block 2.
- The viscosity maximum is attributed to strong hydrogen-bonding interactions between DMSO and water that form structured DMSO·2H₂O complexes, enhancing intermolecular friction in the intermediate composition range.

**Core blocks found:**

**WM_L1#3_Blocks_(Analysis_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#4 | 「GLOBlit_2781」 | 「PROPblock_3」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for DMSO + water binary mixture at 298.15–318.15 K on mole-fraction basis; 120 total data points, 24 at 298.15 K.」 |
| WM_L1#3_Table#5 | 「GLOBlit_11517」 | 「PROPblock_3」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity measurements for DMSO + water binary mixture at 298.15–318.15 K on mass-fraction basis; 35 total data points, 7 at 298.15 K.」 |

*Not stored here: 2 verbatim data_inspections table(s); 7 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** GLOBlit_11517::PROPblock_3: 4.2 (near '…0.0037353 Pa·s occurs at x(DMSO) = 0.3638, which is roughly …') matches no inspected row/stat, database table, or other source of GLOBlit_11517::PROPblock_3
- **UNINSPECTED_VALUE** GLOBlit_11517::PROPblock_3: 1.9 exists in PROPblock_3's database table but was never shown in an inspection of this run


#### other_props_dmso_water
**L1_query_4** — status: success · validation: PASS

**Summary:** Three ThermoML data blocks were found for the DMSO (GLOBcomp_31) + water (GLOBcomp_1) binary system near 298.15 K. No heat capacity data was found. Speed of sound data (DOI 10.1016/j.jct.2006.01.007, GLOBlit_2652, PROPblock_3) at fixed x(DMSO) = 0.0385 and 101.0 kPa gives 1568.53 m/s at 298.15 K, spanning 1555.18–1579.41 m/s over 288.15–313.15 K (6 points). Surface tension data (DOI 10.1021/je7001013, GLOBlit_10766, PROPblock_9) at 298.15 K covers 16 compositions from x(DMSO) = 0.0121 (γ = 0.071 N/m) to 0.8945 (γ = 0.042 N/m), showing a steep initial drop reflecting DMSO's preferential adsorption at the air–water interface. Refractive index data (same DOI, PROPblock_10) at 298.15 K and 101.0 kPa spans 11 compositions from x(DMSO) = 0.0121 (n_D = 1.34) to 0.7685 (n_D = 1.47), increasing monotonically consistent with DMSO's higher polarizability relative to water.

**Answer:**

#### DMSO + Water Binary Mixture Data Near 25 °C

Three data blocks were found in the ThermoML database for dimethyl sulfoxide (DMSO, GLOBcomp_31) + water (GLOBcomp_1) binary mixtures with refractive index, speed of sound, or surface tension measurements near 298.15 K. **No heat capacity (Cp) data** was found for this system.

##### Summary of Available Blocks

**WM_L1#4_Table#1_(Analysis_L1#4_Answer):**

| *row_id* | *Block* | *DOI* | *Literature ID* | *Property* | *Total Pts* | *T range (K)* |
|---|---|---|---|---|---|---|
| WM_L1#4_Table#1_Row#1 | 「PROPblock_3」 | 「10.1016/j.jct.2006.01.007」 | 「GLOBlit_2652」 | 「Speed of sound (m/s)」 | 「6」 | 「288.15–313.15」 |
| WM_L1#4_Table#1_Row#2 | 「PROPblock_9」 | 「10.1021/je7001013」 | 「GLOBlit_10766」 | 「Surface tension (N/m)」 | 「112」 | 「298.15–328.15」 |
| WM_L1#4_Table#1_Row#3 | 「PROPblock_10」 | 「10.1021/je7001013」 | 「GLOBlit_10766」 | 「Refractive index (Na D-line)」 | 「33」 | 「298.15–308.15」 |

##### Representative Data at 298.15 K

**Speed of sound** (GLOBlit_2652 :: PROPblock_3) — fixed composition x(DMSO) = 0.0385, P = 101.0 kPa:

**WM_L1#4_Table#2_(Analysis_L1#4_Answer):**

| *row_id* | *T (K)* | *u (m/s)* |
|---|---|---|
| WM_L1#4_Table#2_Row#1 | 「298.15」 | 「1568.53」 |

The full block spans 288.15–313.15 K with speed of sound ranging from 1555.18 to 1579.41 m/s (6 points, monotonically increasing with temperature).

**Surface tension** (GLOBlit_10766 :: PROPblock_9) at 298.15 K — 16 compositions measured, x(DMSO) = 0.0121–0.8945:

**WM_L1#4_Table#3_(Analysis_L1#4_Answer):**

| *row_id* | *x(DMSO)* | *γ (N/m)* |
|---|---|---|
| WM_L1#4_Table#3_Row#1 | 「0.0121」 | 「0.071」 |
| WM_L1#4_Table#3_Row#2 | 「0.1044」 | 「0.0612」 |
| WM_L1#4_Table#3_Row#3 | 「0.1979」 | 「0.0567」 |
| WM_L1#4_Table#3_Row#4 | 「0.2507」 | 「0.0554」 |
| WM_L1#4_Table#3_Row#5 | 「0.2999」 | 「0.0533」 |
| WM_L1#4_Table#3_Row#6 | 「0.3536」 | 「0.0526」 |
| WM_L1#4_Table#3_Row#7 | 「0.4523」 | 「0.0503」 |
| WM_L1#4_Table#3_Row#8 | 「0.501」 | 「0.0483」 |
| WM_L1#4_Table#3_Row#9 | 「0.59」 | 「0.046」 |
| WM_L1#4_Table#3_Row#10 | 「0.7027」 | 「0.044」 |
| WM_L1#4_Table#3_Row#11 | 「0.8088」 | 「0.0426」 |
| WM_L1#4_Table#3_Row#12 | 「0.8945」 | 「0.042」 |

**Refractive index** (GLOBlit_10766 :: PROPblock_10) at 298.15 K, P = 101.0 kPa — 11 compositions, x(DMSO) = 0.0121–0.7685:

**WM_L1#4_Table#4_(Analysis_L1#4_Answer):**

| *row_id* | *x(DMSO)* | *n_D* |
|---|---|---|
| WM_L1#4_Table#4_Row#1 | 「0.0121」 | 「1.34」 |
| WM_L1#4_Table#4_Row#2 | 「0.0202」 | 「1.344」 |
| WM_L1#4_Table#4_Row#3 | 「0.1467」 | 「1.396」 |
| WM_L1#4_Table#4_Row#4 | 「0.2455」 | 「1.4215」 |
| WM_L1#4_Table#4_Row#5 | 「0.2959」 | 「1.4305」 |
| WM_L1#4_Table#4_Row#6 | 「0.3213」 | 「1.4345」 |
| WM_L1#4_Table#4_Row#7 | 「0.3713」 | 「1.4415」 |
| WM_L1#4_Table#4_Row#8 | 「0.3967」 | 「1.4445」 |
| WM_L1#4_Table#4_Row#9 | 「0.4301」 | 「1.4475」 |
| WM_L1#4_Table#4_Row#10 | 「0.5964」 | 「1.461」 |
| WM_L1#4_Table#4_Row#11 | 「0.7685」 | 「1.47」 |

##### Chemistry Insight

From the surface tension block (GLOBlit_10766 :: PROPblock_9), the data show a steep initial drop from γ = 0.071 N/m at x(DMSO) = 0.0121 to 0.0612 N/m at x(DMSO) = 0.1044, followed by a more gradual decrease to 0.042 N/m at x(DMSO) = 0.8945. This steep initial decline reflects DMSO's preferential adsorption at the air–water interface at low concentrations. From the refractive index block (GLOBlit_10766 :: PROPblock_10), the refractive index increases monotonically from 1.34 to 1.47 across the composition range x(DMSO) = 0.0121–0.7685, consistent with the higher polarizability of DMSO compared to water.

**Core claims:**
- Three ThermoML data blocks were found for the DMSO + water binary system near 298.15 K, covering speed of sound, surface tension, and refractive index; no heat capacity (Cp) data was found for this system.
- At 298.15 K and x(DMSO) = 0.0385, the speed of sound is 1568.53 m/s (P = 101.0 kPa), from a block spanning 288.15–313.15 K with values ranging from 1555.18 to 1579.41 m/s.
- At 298.15 K, surface tension decreases steeply from 0.071 N/m at x(DMSO) = 0.0121 to 0.0612 N/m at x(DMSO) = 0.1044, then more gradually to 0.042 N/m at x(DMSO) = 0.8945, reflecting DMSO's preferential adsorption at the air–water interface at low concentrations.
- At 298.15 K and P = 101.0 kPa, the refractive index increases monotonically from 1.34 at x(DMSO) = 0.0121 to 1.47 at x(DMSO) = 0.7685, consistent with the higher polarizability of DMSO compared to water.

**Core blocks found:**

**WM_L1#4_Blocks_(Analysis_L1#4_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#4_Table#5 | 「GLOBlit_2652」 | 「PROPblock_3」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_8」 | 「Speed of sound measurements for DMSO + water binary mixture, 6 points, T = 288.15–313.15 K, fixed x(DMSO) = 0.0385, P = 101.0 kPa.」 |
| WM_L1#4_Table#6 | 「GLOBlit_10766」 | 「PROPblock_9」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_13」 | 「Surface tension measurements for DMSO + water binary mixture, 112 points, T = 298.15–328.15 K, x(DMSO) = 0.0121–0.8945.」 |
| WM_L1#4_Table#7 | 「GLOBlit_10766」 | 「PROPblock_10」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_7」 | 「Refractive index (Na D-line) measurements for DMSO + water binary mixture, 33 points, T = 298.15–308.15 K, P = 101.0 kPa, x(DMSO) = 0.0121–0.7685.」 |

*Not stored here: 3 verbatim data_inspections table(s); 8 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### query
**L1_query_5** — status: success · validation: FLAGGED(2)

**Summary:** Pure-component property values at 298.15 K were retrieved from ThermoML for the DMSO–water system. For DMSO: surface tension γ = 0.04278 N/m (GLOBlit_3840, PROPblock_1, DOI 10.1016/j.jct.2013.02.021) and refractive index n_D = 1.4771 (GLOBlit_2957, PROPblock_11, DOI 10.1016/j.jct.2008.05.010). For water: surface tension γ = 0.07135 N/m (GLOBlit_725, PROPblock_12, DOI 10.1016/j.fluid.2009.07.010); the water refractive index endpoint was not inspected and no verified value is available. Mixture data from GLOBlit_10766 (PROPblock_9 for surface tension and PROPblock_10 for refractive index) were referenced but flagged as unverified because those blocks were not inspected. Additional ThermoML sources exist for each property (6 more for DMSO surface tension, 9 more for DMSO refractive index, 9 more for water surface tension, and 10 for water refractive index) but were not individually examined.

**Answer:**

#### Pure-Component Surface Tension and Refractive Index at 298.15 K

##### DMSO (GLOBcomp_31)

**Surface tension (GLOBprop_13)** — Seven independent ThermoML sources report pure DMSO surface tension near 298.15 K. The search returned aggregated values across these sources, but only one block was inspected in this run:

- **Inspected:** GLOBlit_3840 :: PROPblock_1 (DOI: 10.1016/j.jct.2013.02.021, pendant drop method) — at 298.15 K, γ = **0.04278 N/m**. The block spans 293.15–313.15 K with 5 data points; surface tension ranges 0.04103–0.04336 N/m across that temperature window.

The remaining 6 sources were identified but their individual data points were not inspected in this run.

**Refractive index, Na D-line (GLOBprop_7)** — Ten ThermoML sources report pure DMSO refractive index near 298.15 K. One block was inspected:

- **Inspected:** GLOBlit_2957 :: PROPblock_11 (DOI: 10.1016/j.jct.2008.05.010) — at 298.15 K, P = 101.325 kPa, n_D = **1.4771** (single-point block).

The remaining 9 sources were identified but their individual data points were not inspected in this run.

---

##### Water (GLOBcomp_1)

**Surface tension (GLOBprop_13)** — Ten ThermoML sources report pure water surface tension near 298.15 K. One block was inspected:

- **Inspected:** GLOBlit_725 :: PROPblock_12 (DOI: 10.1016/j.fluid.2009.07.010) — at 298.15 K, γ = **0.07135 N/m** (single-point block).

The remaining 9 sources were identified but their individual data points were not inspected in this run.

**Refractive index, Na D-line (GLOBprop_7)** — Ten ThermoML sources report pure water refractive index near 298.15 K. No block was inspected in this run for this property; individual data values cannot be quoted. The search-level summary indicated tight clustering of values, but specific numbers were not verified by inspection.

---

##### Summary for RK Endpoint Values (inspected data only)

**WM_L1#5_Table#1_(Analysis_L1#5_Answer):**

| *row_id* | *Property* | *DMSO (x = 1)* | *Water (x = 0)* |
|---|---|---|---|
| WM_L1#5_Table#1_Row#1 | 「Surface tension γ (N/m)」 | 「0.04278 (GLOBlit_3840 :: PROPblock_1)」 | 「0.07135 (GLOBlit_725 :: PROPblock_12)」 |
| WM_L1#5_Table#1_Row#2 | 「Refractive index n_D」 | 「1.4771 (GLOBlit_2957 :: PROPblock_11)」 | 「not inspected in this run」 |

These inspected pure-component endpoint values can be combined with the mixture data from GLOBlit_10766 (PROPblock_9 for surface tension covering x(DMSO) = 0.0121–0.8945; PROPblock_10 for refractive index covering x(DMSO) = 0.0121–0.7685; composition ranges per prior context, not re-inspected) to complete Redlich-Kister fits across the full DMSO–water composition range. For the water refractive index endpoint, an additional inspection of one of the 10 identified blocks would be needed to provide a verified value.

**Core claims:**
- At 298.15 K, one inspected ThermoML source (GLOBlit_3840, pendant drop method) reports pure DMSO surface tension γ = 0.04278 N/m, and one inspected source (GLOBlit_725) reports pure water surface tension γ = 0.07135 N/m.
- At 298.15 K, one inspected ThermoML source (GLOBlit_2957) reports pure DMSO refractive index n_D = 1.4771; the pure water refractive index was not inspected and no verified value is available.
- Multiple additional ThermoML sources exist for each property and component (6 more for DMSO surface tension, 9 more for DMSO refractive index, 9 more for water surface tension, 10 for water refractive index), but their individual data points were not inspected in this run.
- Mixture-composition data blocks (PROPblock_9 for surface tension, PROPblock_10 for refractive index from GLOBlit_10766) are referenced but flagged as UNVERIFIED because they were never inspected; quoted composition ranges for those blocks must be treated as unverified.
- A complete Redlich-Kister fit across the full DMSO–water composition range cannot be finalized without a verified pure water refractive index endpoint and without inspection of the mixture data blocks.

**Core blocks found:**

**WM_L1#5_Blocks_(Analysis_L1#5_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#5_Table#2 | 「GLOBlit_3840」 | 「PROPblock_1」 | 「GLOBcomp_31」 | 「GLOBprop_13」 | 「Pure DMSO surface tension at 293.15–313.15 K (pendant drop); γ = 0.04278 N/m at 298.15 K.」 |
| WM_L1#5_Table#3 | 「GLOBlit_2957」 | 「PROPblock_11」 | 「GLOBcomp_31」 | 「GLOBprop_7」 | 「Pure DMSO refractive index (Na D-line) at 298.15 K; n_D = 1.4771.」 |
| WM_L1#5_Table#4 | 「GLOBlit_725」 | 「PROPblock_12」 | 「GLOBcomp_1」 | 「GLOBprop_13」 | 「Pure water surface tension at 298.15 K; γ = 0.07135 N/m.」 |

*Not stored here: 3 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_9: PROPblock_9 is quoted with data values (0.0121, 0.8945, …) but was never inspected in this run
- **UNINSPECTED_BLOCK** PROPblock_10: PROPblock_10 is quoted with data values (0.0121, 0.7685, …) but was never inspected in this run


#### query
**L1_query_6** — status: success · validation: PASS

**Summary:** The refractive index (Na D-line) of pure water at 298.15 K and 101.325 kPa is n_D = 1.3325, as reported in GLOBlit_306 (DOI: 10.1016/j.fluid.2005.09.009), PROPblock_5. This value is consistent across the ThermoML database, with 6 out of 10 independent unary water blocks reporting n_D = 1.3325 at 298.15 K. For the Redlich-Kister fit of the DMSO + water system, the pure water endpoint (x_DMSO = 0) is n_D = 1.3325. The DMSO pure-component endpoint was not inspected in this run.

**Answer:**

The refractive index (Na D-line) of pure water at 298.15 K is **n_D = 1.3325**, measured at 101.325 kPa.

This value was verified by inspection of GLOBlit_306 (DOI: 10.1016/j.fluid.2005.09.009), PROPblock_5, which reports a single data point for the unary water system:

**WM_L1#6_Table#1_(Analysis_L1#6_Answer):**

| *row_id* | *Temperature (K)* | *Pressure (kPa)* | *n_D* |
|---|---|---|---|
| WM_L1#6_Table#1_Row#1 | 「298.15」 | 「101.325」 | 「1.3325」 |

This value is highly consistent across the ThermoML database — 6 out of 10 independent unary water blocks report n_D = 1.3325 at 298.15 K.

For the Redlich-Kister fit of the DMSO + water system, the pure water endpoint is:
- **Water (x_DMSO = 0):** n_D = 1.3325 (from GLOBlit_306 PROPblock_5, inspected in this run)

The DMSO pure-component endpoint was supplied in prior context and was not inspected in this run.

**Core claims:**
- The refractive index (Na D-line) of pure water at 298.15 K and 101.325 kPa is n_D = 1.3325, as reported in GLOBlit_306 PROPblock_5 and consistent across 6 out of 10 independent unary water blocks in the ThermoML database.
- This n_D = 1.3325 value serves as the pure water endpoint (x_DMSO = 0) for the Redlich-Kister fit of the DMSO + water system.
- The DMSO pure-component endpoint was not inspected in this run.

**Core blocks found:**

**WM_L1#6_Blocks_(Analysis_L1#6_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#6_Table#2 | 「GLOBlit_306」 | 「PROPblock_5」 | 「GLOBcomp_1」 | 「GLOBprop_7」 | 「Refractive index (Na D-line) of pure water at 298.15 K and 101.325 kPa; n_D = 1.3325.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Completed Fits
  - 10.1016/j.jct.2006.12.012/PROPblock_4 (dimethyl sulfoxide, water): RK order=5, R²=0.999909, RMSE=2.9839840842544677e-09, coeffs=[-4e-06, 2e-06, -0.0, -2e-06, 2e-06, 1e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: dimethyl sulfoxide=7.12667e-05, water=1.80683e-05 [block-edges of derived data (water: direct/good, dimethyl sulfoxide: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2006_12_012_BPROPblock_4_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2006_12_012_BPROPblock_4_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2006_12_012_BPROPblock_4_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2006_12_012_BPROPblock_4_T298.1_excess.png
  - viscosity_298K [10.1016/j.jct.2006.12.012/PROPblock_3] (dimethyl sulfoxide, water): RK order=5, R²=0.999497, RMSE=0.00881979868119369, coeffs=[3.705556, -3.859721, 2.183037, -0.818153, -1.803052, 2.548267]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: dimethyl sulfoxide=0.001996, water=0.0008901 [block-edges (water: direct/good, dimethyl sulfoxide: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2006_12_012_BPROPblock_3_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2006_12_012_BPROPblock_3_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2006_12_012_BPROPblock_3_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2006_12_012_BPROPblock_3_T298.1_excess.png
  - 10.1021/je7001013/PROPblock_9 (dimethyl sulfoxide, water): RK order=5, R²=0.985302, RMSE=0.00027135333058068, coeffs=[-0.033894, -0.002541, -0.032477, 0.087181, -0.006592, -0.081761]
      response: direct via X = reported X | 0 reference source(s) | N/m -> N/m
      pure refs: dimethyl sulfoxide=0.04278, water=0.07135 [named (matched to composition axis)]
      fit_csv: $ROOT/data\10_1021_je7001013_BPROPblock_9_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je7001013_BPROPblock_9_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je7001013_BPROPblock_9_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je7001013_BPROPblock_9_T298.1_excess.png
  - 10.1021/je7001013/PROPblock_10 (dimethyl sulfoxide, water): RK order=3, R²=0.999858, RMSE=0.00017833544272879883, coeffs=[0.197127, -0.128481, 0.084211, -0.0264]
      response: direct via X = reported X | 0 reference source(s) | 1 -> 1
      pure refs: dimethyl sulfoxide=1.4771, water=1.3325 [named (matched to composition axis)]
      fit_csv: $ROOT/data\10_1021_je7001013_BPROPblock_10_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1021_je7001013_BPROPblock_10_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1021_je7001013_BPROPblock_10_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1021_je7001013_BPROPblock_10_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_jct_2006_12_012_BPROPblock_4_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2006.12.012 PROPblock_4_T298.1
- `$ROOT/data\10_1016_j_jct_2006_12_012_BPROPblock_4_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2006.12.012 PROPblock_4_T298.1
- `$ROOT/data\10_1016_j_jct_2006_12_012_BPROPblock_3_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2006.12.012 PROPblock_3_T298.1
- `$ROOT/data\10_1016_j_jct_2006_12_012_BPROPblock_3_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2006.12.012 PROPblock_3_T298.1
- `$ROOT/data\10_1021_je7001013_BPROPblock_9_T298.1_fit.csv` — RK fit data — 10.1021/je7001013 PROPblock_9_T298.1
- `$ROOT/data\10_1021_je7001013_BPROPblock_9_T298.1_excess.csv` — Excess property — 10.1021/je7001013 PROPblock_9_T298.1
- `$ROOT/data\10_1021_je7001013_BPROPblock_10_T298.1_fit.csv` — RK fit data — 10.1021/je7001013 PROPblock_10_T298.1
- `$ROOT/data\10_1021_je7001013_BPROPblock_10_T298.1_excess.csv` — Excess property — 10.1021/je7001013 PROPblock_10_T298.1

### plot
- `$ROOT/plots\10_1016_j_jct_2006_12_012_BPROPblock_4_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2006.12.012 PROPblock_4_T298.1
- `$ROOT/plots\10_1016_j_jct_2006_12_012_BPROPblock_4_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2006.12.012 PROPblock_4_T298.1
- `$ROOT/plots\10_1016_j_jct_2006_12_012_BPROPblock_3_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2006.12.012 PROPblock_3_T298.1
- `$ROOT/plots\10_1016_j_jct_2006_12_012_BPROPblock_3_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2006.12.012 PROPblock_3_T298.1
- `$ROOT/plots\10_1021_je7001013_BPROPblock_9_T298.1_fit.png` — RK fit plot — 10.1021/je7001013 PROPblock_9_T298.1
- `$ROOT/plots\10_1021_je7001013_BPROPblock_9_T298.1_excess.png` — Excess plot — 10.1021/je7001013 PROPblock_9_T298.1
- `$ROOT/plots\10_1021_je7001013_BPROPblock_10_T298.1_fit.png` — RK fit plot — 10.1021/je7001013 PROPblock_10_T298.1
- `$ROOT/plots\10_1021_je7001013_BPROPblock_10_T298.1_excess.png` — Excess plot — 10.1021/je7001013 PROPblock_10_T298.1

