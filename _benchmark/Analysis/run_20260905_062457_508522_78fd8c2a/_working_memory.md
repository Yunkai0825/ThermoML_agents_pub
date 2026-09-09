# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062457_508522_78fd8c2a`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_31 | dimethyl sulfoxide |  |
| comp | GLOBcomp_1 | water |  |
| comp | GLOBcomp_1294 | diethyl sulfoxide |  |
| comp | GLOBcomp_2145 | dipropyl sulfoxide |  |
| comp | GLOBcomp_7698 | 2,2'-sulfinylbispropane |  |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| prop | GLOBprop_4 | viscositypas |  |
| prop | GLOBprop_44 | relativepermittivityatzerofrequency |  |
| prop | GLOBprop_64 | apparentmolarheatcapacityjkmol |  |
| prop | GLOBprop_8 | speedofsoundms |  |
| prop | GLOBprop_34 | thermal conductivity, w/m/k |  |
| prop | GLOBprop_13 | surface tension liquid-gas, n/m |  |
| prop | GLOBprop_7 | refractive index (na d-line) |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<dimethyl sulfoxide> |  |
| var | GLOBvar_4 | molalitymolkg<dimethyl sulfoxide> |  |
| constr | GLOBconstr_1 | pressurekpa |  |
| meas | GLOBmeas_41 | hot wire method |  |
| meas | GLOBmeas_36 | maximal bubble pressure |  |
| meas | GLOBmeas_163 | abbe:ufactor:4 |  |
| lit | GLOBlit_10024 | 10.1021/je301171y |  |
| lit | GLOBlit_10766 | 10.1021/je7001013 |  |

### History
- [query_thermoml]
- [inspect_block]
- [inspect_block]
- [inspect_block]
- [inspect_block]
- [inspect_block]
- [query_thermoml]

### Query Results
#### query
**L1_query_1** — status: partial · validation: FLAGGED(7)

**Summary:** The ThermoML database contains 19 property data blocks for the DMSO (GLOBcomp_31) + water (GLOBcomp_1) binary system in the 288–313 K temperature range, drawn from 12 publications and totaling 1,425 liquid-phase data points. The most extensively covered property is mass density (kg/m³, GLOBprop_1) with 8 blocks, followed by viscosity (Pa·s, GLOBprop_4, 3 blocks), speed of sound (m/s, GLOBprop_8, 2 blocks), and single blocks each for apparent molar heat capacity (J/K/mol, GLOBprop_64), molar enthalpy of solution (kJ/mol, GLOBprop_15), relative permittivity at zero frequency (GLOBprop_44), thermal conductivity, surface tension, and refractive index. The largest single contributor is GLOBlit_10109 (DOI: 10.1021/je400149j) with 363 points of relative permittivity data, followed by GLOBlit_2844 (DOI: 10.1016/j.jct.2007.06.010) with 308 points covering apparent molar heat capacity and density, and GLOBlit_2781 (DOI: 10.1016/j.jct.2006.12.012) with 240 points of viscosity and density. Other notable sources include GLOBlit_10766 (DOI: 10.1021/je7001013, 145 points), GLOBlit_2584 (DOI: 10.1016/j.jct.2005.07.012, 96 density points), GLOBlit_5953 (DOI: 10.1016/j.tca.2011.08.013, 48 points across density, viscosity, and speed of sound), and GLOBlit_5958 (DOI: 10.1016/j.tca.2011.09.009, 1 enthalpy-of-solution point). Individual data-point values at specific compositions and temperatures were not inspected; block-level point counts and property assignments are reported but flagged as unverified against direct block inspection.

**Answer:**

#### DMSO + Water Binary Mixture Data in the ThermoML Database (288–313 K)

##### Overview

The ThermoML database contains **19 property data blocks** for the dimethyl sulfoxide (DMSO, GLOBcomp_31) + water (GLOBcomp_1) binary system in the 288–313 K temperature window, spanning **12 publications** and totaling **1,425 data points**. All data are for the liquid phase.

##### Property Coverage

**WM_L1_Q1_Table#1_(Analysis_L1_Q1_Answer):**

| *row_id* | *Property* | *GLOBprop* | *Block count* |
|---|---|---|---|
| WM_L1_Q1_Table#1_Row#1 | 「Mass density (kg/m³)」 | 「GLOBprop_1」 | 「8」 |
| WM_L1_Q1_Table#1_Row#2 | 「Viscosity (Pa·s)」 | 「GLOBprop_4」 | 「3」 |
| WM_L1_Q1_Table#1_Row#3 | 「Speed of sound (m/s)」 | 「GLOBprop_8」 | 「2」 |
| WM_L1_Q1_Table#1_Row#4 | 「Apparent molar heat capacity (J/K/mol)」 | 「GLOBprop_64」 | 「1」 |
| WM_L1_Q1_Table#1_Row#5 | 「Molar enthalpy of solution (kJ/mol)」 | 「GLOBprop_15」 | 「1」 |
| WM_L1_Q1_Table#1_Row#6 | 「Thermal conductivity (W/m/K)」 | 「—」 | 「1」 |
| WM_L1_Q1_Table#1_Row#7 | 「Relative permittivity at zero frequency」 | 「GLOBprop_44」 | 「1」 |
| WM_L1_Q1_Table#1_Row#8 | 「Surface tension liquid–gas (N/m)」 | 「—」 | 「1」 |
| WM_L1_Q1_Table#1_Row#9 | 「Refractive index (Na D-line)」 | 「—」 | 「1」 |

##### Block Listing by Source

**1. GLOBlit_2584** — DOI: 10.1016/j.jct.2005.07.012

**WM_L1_Q1_Table#2_(Analysis_L1_Q1_Answer):**

| *row_id* | *Block* | *Property* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#2_Row#1 | 「PROPblock_8」 | 「Mass density (GLOBprop_1)」 | 「96」 |

*(Block-level details not inspected in this run.)*

**2. GLOBlit_2652** — DOI: 10.1016/j.jct.2006.01.007

**WM_L1_Q1_Table#3_(Analysis_L1_Q1_Answer):**

| *row_id* | *Block* | *Property* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#3_Row#1 | 「PROPblock_3」 | 「Speed of sound (GLOBprop_8)」 | 「6」 |
| WM_L1_Q1_Table#3_Row#2 | 「PROPblock_4」 | 「Mass density (GLOBprop_1)」 | 「6」 |

*(Block-level details not inspected in this run.)*

**3. GLOBlit_2781** — DOI: 10.1016/j.jct.2006.12.012

**WM_L1_Q1_Table#4_(Analysis_L1_Q1_Answer):**

| *row_id* | *Block* | *Property* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#4_Row#1 | 「PROPblock_3」 | 「Viscosity (GLOBprop_4)」 | 「120」 |
| WM_L1_Q1_Table#4_Row#2 | 「PROPblock_4」 | 「Mass density (GLOBprop_1)」 | 「120」 |

*(Block-level details not inspected in this run.)*

**4. GLOBlit_2844** — DOI: 10.1016/j.jct.2007.06.010

**WM_L1_Q1_Table#5_(Analysis_L1_Q1_Answer):**

| *row_id* | *Block* | *Property* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#5_Row#1 | 「PROPblock_3」 | 「Apparent molar Cp (GLOBprop_64)」 | 「216」 |
| WM_L1_Q1_Table#5_Row#2 | 「PROPblock_4」 | 「Mass density (GLOBprop_1)」 | 「92」 |

*(Block-level details not inspected in this run.)*

**5. GLOBlit_5953** — DOI: 10.1016/j.tca.2011.08.013

**WM_L1_Q1_Table#6_(Analysis_L1_Q1_Answer):**

| *row_id* | *Block* | *Property* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#6_Row#1 | 「PROPblock_10」 | 「Viscosity (GLOBprop_4)」 | 「16」 |
| WM_L1_Q1_Table#6_Row#2 | 「PROPblock_11」 | 「Speed of sound (GLOBprop_8)」 | 「16」 |
| WM_L1_Q1_Table#6_Row#3 | 「PROPblock_12」 | 「Mass density (GLOBprop_1)」 | 「16」 |

*(Block-level details not inspected in this run.)*

**6. GLOBlit_5958** — DOI: 10.1016/j.tca.2011.09.009

**WM_L1_Q1_Table#7_(Analysis_L1_Q1_Answer):**

| *row_id* | *Block* | *Property* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#7_Row#1 | 「PROPblock_1」 | 「Molar enthalpy of solution (GLOBprop_15)」 | 「1」 |

*(Block-level details not inspected in this run.)*

**7. GLOBlit_7713** — DOI: 10.1021/acs.jced.8b01048

**WM_L1_Q1_Table#8_(Analysis_L1_Q1_Answer):**

| *row_id* | *Block* | *Property* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#8_Row#1 | 「PROPblock_10」 | 「Mass density (GLOBprop_1)」 | 「9」 |

*(Block-level details not inspected in this run.)*

**8. GLOBlit_10109** — DOI: 10.1021/je400149j

**WM_L1_Q1_Table#9_(Analysis_L1_Q1_Answer):**

| *row_id* | *Block* | *Property* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#9_Row#1 | 「PROPblock_5」 | 「Relative permittivity at zero frequency (GLOBprop_44)」 | 「363」 |

*(Block-level details not inspected in this run.)*

**9–12. Additional DOIs (from summary)**

The system summary confirms 4 additional DOIs contributing blocks, including GLOBlit_10766 (DOI: 10.1021/je7001013, 2 blocks, 145 points) and others covering the remaining properties (thermal conductivity, surface tension, refractive index, and additional density data). Detailed block-level information for these was not retrieved in this run.

##### Top Papers by Data Volume

**WM_L1_Q1_Table#10_(Analysis_L1_Q1_Answer):**

| *row_id* | *GLOBlit* | *DOI* | *Blocks* | *Matching points* |
|---|---|---|---|---|
| WM_L1_Q1_Table#10_Row#1 | 「GLOBlit_10109」 | 「10.1021/je400149j」 | 「1」 | 「363」 |
| WM_L1_Q1_Table#10_Row#2 | 「GLOBlit_2844」 | 「10.1016/j.jct.2007.06.010」 | 「2」 | 「308」 |
| WM_L1_Q1_Table#10_Row#3 | 「GLOBlit_2781」 | 「10.1016/j.jct.2006.12.012」 | 「2」 | 「240」 |
| WM_L1_Q1_Table#10_Row#4 | 「GLOBlit_10766」 | 「10.1021/je7001013」 | 「2」 | 「145」 |
| WM_L1_Q1_Table#10_Row#5 | 「GLOBlit_2584」 | 「10.1016/j.jct.2005.07.012」 | 「1」 | 「96」 |

##### Chemistry Context

The DMSO–water system is well known for its strong non-ideal mixing behavior driven by DMSO–water hydrogen bonding. The database coverage is richest for mass density (8 blocks from multiple research groups), providing good redundancy for cross-validation. Transport properties (viscosity, speed of sound, thermal conductivity), dielectric properties (relative permittivity), and interfacial properties (surface tension, refractive index) are also represented, along with calorimetric data (apparent molar heat capacity, enthalpy of solution). Individual data-point values were not inspected in this run; targeted block inspections would be needed to retrieve specific numerical values at particular compositions and temperatures.

**Core claims:**
- The ThermoML database contains 19 property data blocks for the DMSO + water binary system in the 288–313 K temperature window, spanning 12 publications and totaling 1,425 data points, all for the liquid phase.
- Mass density is the most extensively covered property with 8 blocks from multiple research groups, followed by viscosity (3 blocks), speed of sound (2 blocks), and single blocks each for apparent molar heat capacity, molar enthalpy of solution, thermal conductivity, relative permittivity at zero frequency, surface tension, and refractive index.
- Individual data-point values were not inspected in this run; all block-level point counts and property assignments carry UNVERIFIED flags and would require targeted block inspections to confirm.

**Core blocks found:**

**WM_L1_Q1_Blocks_(Analysis_L1_Q1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1_Q1_Table#11 | 「GLOBlit_2584」 | 「PROPblock_8」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for DMSO + water binary mixture.」 |
| WM_L1_Q1_Table#12 | 「GLOBlit_2652」 | 「PROPblock_3」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_8」 | 「Speed of sound for DMSO + water binary mixture.」 |
| WM_L1_Q1_Table#13 | 「GLOBlit_2652」 | 「PROPblock_4」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for DMSO + water binary mixture.」 |
| WM_L1_Q1_Table#14 | 「GLOBlit_2781」 | 「PROPblock_3」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_4」 | 「Viscosity for DMSO + water binary mixture.」 |
| WM_L1_Q1_Table#15 | 「GLOBlit_2781」 | 「PROPblock_4」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for DMSO + water binary mixture.」 |
| WM_L1_Q1_Table#16 | 「GLOBlit_2844」 | 「PROPblock_3」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_64」 | 「Apparent molar heat capacity for DMSO + water binary mixture.」 |
| WM_L1_Q1_Table#17 | 「GLOBlit_2844」 | 「PROPblock_4」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for DMSO + water binary mixture.」 |
| WM_L1_Q1_Table#18 | 「GLOBlit_5953」 | 「PROPblock_10」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_4」 | 「Viscosity for DMSO + water binary mixture.」 |
| WM_L1_Q1_Table#19 | 「GLOBlit_5953」 | 「PROPblock_11」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_8」 | 「Speed of sound for DMSO + water binary mixture.」 |
| WM_L1_Q1_Table#20 | 「GLOBlit_5953」 | 「PROPblock_12」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for DMSO + water binary mixture.」 |
| WM_L1_Q1_Table#21 | 「GLOBlit_5958」 | 「PROPblock_1」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_15」 | 「Molar enthalpy of solution for DMSO + water binary mixture.」 |
| WM_L1_Q1_Table#22 | 「GLOBlit_7713」 | 「PROPblock_10」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for DMSO + water binary mixture.」 |
| WM_L1_Q1_Table#23 | 「GLOBlit_10109」 | 「PROPblock_5」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_44」 | 「Relative permittivity at zero frequency for DMSO + water binary mixture.」 |

*Not stored here: 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(7) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_8: PROPblock_8 is quoted with data values (96, …) but was never inspected in this run
- **UNINSPECTED_BLOCK** PROPblock_3 + PROPblock_4: PROPblock_3 + PROPblock_4 is quoted with data values (120, 120, …) but was never inspected in this run
- **UNINSPECTED_BLOCK** PROPblock_3 + PROPblock_4: PROPblock_3 + PROPblock_4 is quoted with data values (216, 92, …) but was never inspected in this run
- **UNINSPECTED_BLOCK** PROPblock_10 + PROPblock_11 + PROPblock_12: PROPblock_10 + PROPblock_11 + PROPblock_12 is quoted with data values (16, 16, 16, …) but was never inspected in this run
- **UNINSPECTED_BLOCK** PROPblock_5: PROPblock_5 is quoted with data values (363, …) but was never inspected in this run
- **UNINSPECTED_BLOCK** PROPblock_5: PROPblock_5 is quoted with data values (145, …) but was never inspected in this run
- **UNINSPECTED_BLOCK** PROPblock_5: PROPblock_5 is quoted with data values (363, 308, 240, 145, …) but was never inspected in this run


#### query
**L1_query_2** — status: success · validation: FLAGGED(1)

**Summary:** Three DMSO + water binary mixture data blocks were identified and inspected. (1) Thermal conductivity (GLOBprop_34) in PROPblock_5 of GLOBlit_10024 (DOI: 10.1021/je301171y): 63 points, w(DMSO) = 0.1–0.9 mass fraction, T = 279.18–339.37 K, P = 100.0 kPa, measured by hot-wire method; representative values include λ = 0.522 W/m/K at w=0.1, T=279.63 K and λ = 0.196 W/m/K at w=0.9, T=338.51 K, with thermal conductivity decreasing with increasing DMSO content. (2) Surface tension (GLOBprop_13) in PROPblock_9 of GLOBlit_10766 (DOI: 10.1021/je7001013): 112 points, x(DMSO) = 0.0121–0.8945 mole fraction, T = 298.15–328.15 K, measured by maximal bubble pressure; representative values include γ = 0.071 N/m at x=0.0121, T=298.15 K and γ = 0.0387 N/m at x=0.8945, T=328.15 K, with surface tension decreasing sharply upon initial DMSO addition. (3) Refractive index (GLOBprop_7) in PROPblock_10 of GLOBlit_10766: 33 points, x(DMSO) = 0.0121–0.7685, T = 298.15–308.15 K, P = 101.0 kPa, measured by Abbe refractometer; n_D increases monotonically with DMSO mole fraction from 1.34 to 1.47. GLOBlit_10766 additionally contains 16 total blocks covering four sulfoxides (DMSO, diethyl sulfoxide, dipropyl sulfoxide, diisopropyl sulfoxide) as pure components and binary mixtures with water, measuring surface tension and refractive index; only the DMSO+water blocks (PROPblock_9 and PROPblock_10) were numerically inspected.

**Answer:**

#### DMSO + Water Binary Mixture Blocks

##### Thermal Conductivity (GLOBprop_34)
- **Block:** PROPblock_5 in GLOBlit_10024 (DOI: 10.1021/je301171y)
- **Points:** 63
- **Composition range:** w(DMSO) = 0.1–0.9 (mass fraction)
- **Temperature range:** 279.18–339.37 K
- **Pressure:** 100.0 kPa (fixed constraint)
- **Method:** Hot-wire method (GLOBmeas_41)
- **Representative inspected values:** λ = 0.522 W/m/K at w=0.1, T=279.63 K; λ = 0.319 W/m/K at w=0.5013, T=279.57 K; λ = 0.196 W/m/K at w=0.9, T=338.51 K. Thermal conductivity decreases with increasing DMSO mass fraction and generally increases with temperature at each composition.

##### Surface Tension (GLOBprop_13)
- **Block:** PROPblock_9 in GLOBlit_10766 (DOI: 10.1021/je7001013)
- **Points:** 112
- **Composition range:** x(DMSO) = 0.0121–0.8945 (mole fraction)
- **Temperature range:** 298.15–328.15 K
- **Method:** Maximal bubble pressure (GLOBmeas_36)
- **Representative inspected values:** γ = 0.071 N/m at x=0.0121, T=298.15 K; γ = 0.046 N/m at x=0.59, T=298.15 K; γ = 0.042 N/m at x=0.8945, T=298.15 K; γ = 0.0387 N/m at x=0.8945, T=328.15 K. Surface tension decreases sharply with initial DMSO addition and more gradually at higher DMSO content.

##### Refractive Index (GLOBprop_7)
- **Block:** PROPblock_10 in GLOBlit_10766 (DOI: 10.1021/je7001013)
- **Points:** 33
- **Composition range:** x(DMSO) = 0.0121–0.7685 (mole fraction)
- **Temperature range:** 298.15–308.15 K
- **Pressure:** 101.0 kPa (fixed constraint)
- **Method:** Abbe refractometer (GLOBmeas_163)
- **Representative inspected values:** n_D = 1.34 at x=0.0121, T=298.15 K; n_D = 1.4305 at x=0.2959, T=298.15 K; n_D = 1.47 at x=0.7685, T=298.15 K. Refractive index increases monotonically with DMSO mole fraction.

---

#### All Blocks from GLOBlit_10766 (DOI: 10.1021/je7001013)

This reference contains data blocks (count derived from the search_blocks listing of that literature source) covering four sulfoxides (pure and binary with water), measuring surface tension (GLOBprop_13) and refractive index (GLOBprop_7):

**Compounds studied:**
- GLOBcomp_31 = dimethyl sulfoxide (DMSO)
- GLOBcomp_1294 = diethyl sulfoxide
- GLOBcomp_2145 = dipropyl sulfoxide
- GLOBcomp_7698 = diisopropyl sulfoxide (2,2'-sulfinylbispropane)
- GLOBcomp_1 = water

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *Block* | *System* | *Compound(s)* | *Property* |
|---|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「PROPblock_1」 | 「unary」 | 「GLOBcomp_31 (DMSO)」 | 「GLOBprop_13 (surface tension)」 |
| WM_L1#2_Table#1_Row#2 | 「PROPblock_2」 | 「unary」 | 「GLOBcomp_31 (DMSO)」 | 「GLOBprop_7 (refractive index)」 |
| WM_L1#2_Table#1_Row#3 | 「PROPblock_3」 | 「unary」 | 「GLOBcomp_1294 (diethyl sulfoxide)」 | 「GLOBprop_13 (surface tension)」 |
| WM_L1#2_Table#1_Row#4 | 「PROPblock_4」 | 「unary」 | 「GLOBcomp_1294 (diethyl sulfoxide)」 | 「GLOBprop_7 (refractive index)」 |
| WM_L1#2_Table#1_Row#5 | 「PROPblock_5」 | 「unary」 | 「GLOBcomp_2145 (dipropyl sulfoxide)」 | 「GLOBprop_13 (surface tension)」 |
| WM_L1#2_Table#1_Row#6 | 「PROPblock_6」 | 「unary」 | 「GLOBcomp_2145 (dipropyl sulfoxide)」 | 「GLOBprop_7 (refractive index)」 |
| WM_L1#2_Table#1_Row#7 | 「PROPblock_7」 | 「unary」 | 「GLOBcomp_7698 (diisopropyl sulfoxide)」 | 「GLOBprop_13 (surface tension)」 |
| WM_L1#2_Table#1_Row#8 | 「PROPblock_8」 | 「unary」 | 「GLOBcomp_7698 (diisopropyl sulfoxide)」 | 「GLOBprop_7 (refractive index)」 |
| WM_L1#2_Table#1_Row#9 | 「PROPblock_9」 | 「binary」 | 「GLOBcomp_31 + GLOBcomp_1」 | 「GLOBprop_13 (surface tension) — 112 pts, x(DMSO) 0.0121–0.8945, T 298.15–328.15 K」 |
| WM_L1#2_Table#1_Row#10 | 「PROPblock_10」 | 「binary」 | 「GLOBcomp_31 + GLOBcomp_1」 | 「GLOBprop_7 (refractive index) — 33 pts, x(DMSO) 0.0121–0.7685, T 298.15–308.15 K」 |
| WM_L1#2_Table#1_Row#11 | 「PROPblock_11」 | 「binary」 | 「GLOBcomp_1294 + GLOBcomp_1」 | 「GLOBprop_13 (surface tension)」 |
| WM_L1#2_Table#1_Row#12 | 「PROPblock_12」 | 「binary」 | 「GLOBcomp_1294 + GLOBcomp_1」 | 「GLOBprop_7 (refractive index)」 |
| WM_L1#2_Table#1_Row#13 | 「PROPblock_13」 | 「binary」 | 「GLOBcomp_2145 + GLOBcomp_1」 | 「GLOBprop_13 (surface tension)」 |
| WM_L1#2_Table#1_Row#14 | 「PROPblock_14」 | 「binary」 | 「GLOBcomp_2145 + GLOBcomp_1」 | 「GLOBprop_7 (refractive index)」 |
| WM_L1#2_Table#1_Row#15 | 「PROPblock_15」 | 「binary」 | 「GLOBcomp_7698 + GLOBcomp_1」 | 「GLOBprop_13 (surface tension)」 |
| WM_L1#2_Table#1_Row#16 | 「PROPblock_16」 | 「binary」 | 「GLOBcomp_7698 + GLOBcomp_1」 | 「GLOBprop_7 (refractive index)」 |

The eight unary blocks provide pure-component baselines for each sulfoxide, while the eight binary blocks systematically cover each sulfoxide mixed with water. The DMSO+water blocks (PROPblock_9 and PROPblock_10) are the most data-rich among the binary blocks in this reference. Detailed numerical ranges for blocks not inspected in this run (PROPblock_1–8, PROPblock_11–16) are available but were not verified here.

**Core claims:**
- For the DMSO + water binary mixture at 100.0 kPa, thermal conductivity (63 points, w(DMSO) = 0.1–0.9, T = 279.18–339.37 K, hot-wire method) decreases with increasing DMSO mass fraction and generally increases with temperature at each composition, with representative values of λ = 0.522 W/m/K at w=0.1, T=279.63 K; λ = 0.319 W/m/K at w=0.5013, T=279.57 K; and λ = 0.196 W/m/K at w=0.9, T=338.51 K.
- For the DMSO + water binary mixture, surface tension (112 points, x(DMSO) = 0.0121–0.8945, T = 298.15–328.15 K, maximal bubble pressure method) decreases sharply with initial DMSO addition and more gradually at higher DMSO content, with representative values of γ = 0.071 N/m at x=0.0121, T=298.15 K; γ = 0.046 N/m at x=0.59, T=298.15 K; and γ = 0.042 N/m at x=0.8945, T=298.15 K.
- For the DMSO + water binary mixture at 101.0 kPa, refractive index (33 points, x(DMSO) = 0.0121–0.7685, T = 298.15–308.15 K, Abbe refractometer) increases monotonically with DMSO mole fraction, from n_D = 1.34 at x=0.0121 to n_D = 1.47 at x=0.7685 at 298.15 K.
- The reference DOI 10.1021/je7001013 contains 16 data blocks covering surface tension and refractive index for four sulfoxides (DMSO, diethyl sulfoxide, dipropyl sulfoxide, diisopropyl sulfoxide) as pure components and as binary mixtures with water; only the DMSO+water blocks (PROPblock_9 and PROPblock_10) were numerically inspected and verified.
- Several blocks cited in the answer (PROPblock_1–8, PROPblock_11–16) were not inspected during the analysis run and their detailed numerical ranges remain unverified.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_10024」 | 「PROPblock_5」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_34」 | 「Thermal conductivity of DMSO+water binary mixture; 63 points; w(DMSO) 0.1–0.9 (mass fraction); T 279.18–339.37 K; P 100.0 kPa; hot-wire method (GLOBmeas_41).」 |
| WM_L1#2_Table#3 | 「GLOBlit_10766」 | 「PROPblock_1」 | 「GLOBcomp_31」 | 「GLOBprop_13」 | 「Surface tension of pure DMSO.」 |
| WM_L1#2_Table#4 | 「GLOBlit_10766」 | 「PROPblock_2」 | 「GLOBcomp_31」 | 「GLOBprop_7」 | 「Refractive index of pure DMSO.」 |
| WM_L1#2_Table#5 | 「GLOBlit_10766」 | 「PROPblock_3」 | 「GLOBcomp_1294」 | 「GLOBprop_13」 | 「Surface tension of pure diethyl sulfoxide.」 |
| WM_L1#2_Table#6 | 「GLOBlit_10766」 | 「PROPblock_4」 | 「GLOBcomp_1294」 | 「GLOBprop_7」 | 「Refractive index of pure diethyl sulfoxide.」 |
| WM_L1#2_Table#7 | 「GLOBlit_10766」 | 「PROPblock_5」 | 「GLOBcomp_2145」 | 「GLOBprop_13」 | 「Surface tension of pure dipropyl sulfoxide.」 |
| WM_L1#2_Table#8 | 「GLOBlit_10766」 | 「PROPblock_6」 | 「GLOBcomp_2145」 | 「GLOBprop_7」 | 「Refractive index of pure dipropyl sulfoxide.」 |
| WM_L1#2_Table#9 | 「GLOBlit_10766」 | 「PROPblock_7」 | 「GLOBcomp_7698」 | 「GLOBprop_13」 | 「Surface tension of pure diisopropyl sulfoxide.」 |
| WM_L1#2_Table#10 | 「GLOBlit_10766」 | 「PROPblock_8」 | 「GLOBcomp_7698」 | 「GLOBprop_7」 | 「Refractive index of pure diisopropyl sulfoxide.」 |
| WM_L1#2_Table#11 | 「GLOBlit_10766」 | 「PROPblock_9」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_13」 | 「Surface tension of DMSO+water binary mixture; 112 points; x(DMSO) 0.0121–0.8945; T 298.15–328.15 K; maximal bubble pressure method (GLOBmeas_36).」 |
| WM_L1#2_Table#12 | 「GLOBlit_10766」 | 「PROPblock_10」 | 「GLOBcomp_31, GLOBcomp_1」 | 「GLOBprop_7」 | 「Refractive index of DMSO+water binary mixture; 33 points; x(DMSO) 0.0121–0.7685; T 298.15–308.15 K; P 101.0 kPa; Abbe refractometer (GLOBmeas_163).」 |
| WM_L1#2_Table#13 | 「GLOBlit_10766」 | 「PROPblock_11」 | 「GLOBcomp_1294, GLOBcomp_1」 | 「GLOBprop_13」 | 「Surface tension of diethyl sulfoxide+water binary mixture.」 |
| WM_L1#2_Table#14 | 「GLOBlit_10766」 | 「PROPblock_12」 | 「GLOBcomp_1294, GLOBcomp_1」 | 「GLOBprop_7」 | 「Refractive index of diethyl sulfoxide+water binary mixture.」 |
| WM_L1#2_Table#15 | 「GLOBlit_10766」 | 「PROPblock_13」 | 「GLOBcomp_2145, GLOBcomp_1」 | 「GLOBprop_13」 | 「Surface tension of dipropyl sulfoxide+water binary mixture.」 |
| WM_L1#2_Table#16 | 「GLOBlit_10766」 | 「PROPblock_14」 | 「GLOBcomp_2145, GLOBcomp_1」 | 「GLOBprop_7」 | 「Refractive index of dipropyl sulfoxide+water binary mixture.」 |
| WM_L1#2_Table#17 | 「GLOBlit_10766」 | 「PROPblock_15」 | 「GLOBcomp_7698, GLOBcomp_1」 | 「GLOBprop_13」 | 「Surface tension of diisopropyl sulfoxide+water binary mixture.」 |
| WM_L1#2_Table#18 | 「GLOBlit_10766」 | 「PROPblock_16」 | 「GLOBcomp_7698, GLOBcomp_1」 | 「GLOBprop_7」 | 「Refractive index of diisopropyl sulfoxide+water binary mixture.」 |

*Not stored here: 3 verbatim data_inspections table(s); 13 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_11: PROPblock_11 is quoted with data values (16, …) but was never inspected in this run


### Inspected Blocks
- GLOBlit_2584 | 10.1016/j.jct.2005.07.012 | PROPblock_8: 96 rows; x=['mole_fraction_<water>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3
- GLOBlit_2781 | 10.1016/j.jct.2006.12.012 | PROPblock_3: 120 rows; x=['mole_fraction_<dimethyl sulfoxide>']; y=['viscosity_pa_s']
    - BLKprop_1 / GLOBprop_4: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_4: kind=direct; materialize_reference=False; supported=True; units=Pa*s -> Pa*s
- GLOBlit_10109 | 10.1021/je400149j | PROPblock_5: 363 rows; x=['mole_fraction_<dimethyl sulfoxide>']; y=['relative_permittivity_at_zero_frequency']
    - BLKprop_1 / GLOBprop_44: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_44: kind=direct; materialize_reference=False; supported=True; units=1 -> 1
- GLOBlit_2844 | 10.1016/j.jct.2007.06.010 | PROPblock_3: 216 rows; x=['molality_mol_kg_<dimethyl sulfoxide>']; y=['apparent_molar_heat_capacity_j_k_mol']
    - BLKprop_1 / GLOBprop_64: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_64: kind=direct; materialize_reference=False; supported=True; units=J/(K mol) -> J/(K mol)
- GLOBlit_5953 | 10.1016/j.tca.2011.08.013 | PROPblock_11: 16 rows; x=['mole_fraction_<dimethyl sulfoxide>']; y=['speed_of_sound_m_s']
    - BLKprop_1 / GLOBprop_8: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_8: kind=direct; materialize_reference=False; supported=True; units=m/s -> m/s
