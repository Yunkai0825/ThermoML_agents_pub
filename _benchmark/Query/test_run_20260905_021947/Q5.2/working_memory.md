# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_24 | 1,2-ethanediol | 1,2-ethanediol |
| comp | GLOBcomp_1 | water | water |
| comp | GLOBcomp_61 | 1,2-propanediol | 1,2-propanediol |
| comp | GLOBcomp_111 | diethylene_glycol | diethylene glycol |
| comp | GLOBcomp_113 | triethylene_glycol | triethylene glycol |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|
| lit | GLOBlit_5201 | 2018-hog-tor-0 | 10.1016/j.jct.2018.02.022 |
| lit | GLOBlit_10102 | 2013-hne-cib-1 | 10.1021/je4001203 |
| lit | GLOBlit_8038 | 2003-yan-ma-2 | 10.1021/je020140j |
| lit | GLOBlit_6951 | 2017-moo-ros-0 | 10.1021/acs.jced.6b00526 |
| lit | GLOBlit_1283 | 2013-zem-tro-0 | 10.1016/j.fluid.2013.06.041 |
| lit | GLOBlit_8239 | 2003-geo-sas-1 | 10.1021/je0340755 |
| lit | GLOBlit_7545 | 2018-mik-sko-0 | 10.1021/acs.jced.8b00403 |
| lit | GLOBlit_9758 | 2012-kat-hne-0 | 10.1021/je201184b |
| lit | GLOBlit_1623 | 2015-cha-hsi-0 | 10.1016/j.fluid.2014.12.040 |
| lit | GLOBlit_4754 | 2017-cib--1 | 10.1016/j.jct.2016.07.016 |
| lit | GLOBlit_11031 | 2008-man-guz-0 | 10.1021/je700672f |
| lit | GLOBlit_9382 | 2011-beg-cla-0 | 10.1021/je1009976 |
| lit | GLOBlit_6630 | 2016-cib--0 | 10.1021/acs.jced.5b00498 |
| lit | GLOBlit_1753 | 2015-ani-sin-0 | 10.1016/j.fluid.2015.07.030 |
| lit | GLOBlit_4395 | 2015-kli-str-1 | 10.1016/j.jct.2015.05.024 |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find all available data for glycol + water mixtures in ThermoML → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** The ThermoML database contains extensive binary mixture data for four glycol + water systems, totaling 161 property blocks across 81 literature sources (with some shared across systems) and 10,081 data points. Ethylene glycol (GLOBcomp_24) + water (GLOBcomp_1) has 59 blocks, 32 papers, 2,584 points, spanning 258.32–573.23 K and 50.0–350,200.0 kPa. Propylene glycol (GLOBcomp_61) + water has 34 blocks, 18 papers, 1,780 points, spanning 253.15–573.19 K and 100.0–350,000.0 kPa. Diethylene glycol (GLOBcomp_111) + water has 28 blocks, 15 papers, 2,079 points, spanning 278.15–573.184 K and 50.0–30,500.0 kPa. Triethylene glycol (GLOBcomp_113) + water has 40 blocks, 16 papers, 3,638 points, spanning 278.15–573.183 K and 50.0–30,510.0 kPa. Mass density is the most commonly measured property across all four systems (46 blocks total), followed by speed of sound and viscosity. Triethylene glycol + water has the largest dataset, driven largely by a single study (DOI 10.1016/j.fluid.2015.07.030, GLOBlit_1753) contributing 1,370 points across 12 blocks. Ethylene glycol + water has the broadest literature coverage. All four systems reach similar upper temperatures (~573 K), but ethylene glycol and propylene glycol systems extend to higher pressures (~350 MPa). Transport properties and excess thermodynamic properties are available but less common than volumetric and acoustic properties.

**Answer:**

#### Glycol + Water Binary Mixture Data in ThermoML — Comprehensive Overview

The ThermoML database contains extensive data for four glycol + water binary systems, totaling **161 property blocks** across **81 literature sources** (some shared across systems) with **10,081 data points**.

---

##### 1. Ethylene Glycol (1,2-Ethanediol) + Water

- **Compound IDs:** GLOBcomp_24 + GLOBcomp_1
- **Coverage:** 59 blocks, 32 papers, 2,584 data points
- **Temperature range:** 258.32 – 573.23 K
- **Pressure range:** 50.0 – 350,200.0 kPa

**Properties measured (blocks):**

**WM_L1_Q1_Table#1_(Query_L1_Q1_Answer):**

| *row_id* | *Property* | *Blocks* |
|---|---|---|
| WM_L1_Q1_Table#1_Row#1 | 「Mass density, kg/m³」 | 「16」 |
| WM_L1_Q1_Table#1_Row#2 | 「Speed of sound, m/s」 | 「8」 |
| WM_L1_Q1_Table#1_Row#3 | 「Viscosity, Pa·s」 | 「7」 |
| WM_L1_Q1_Table#1_Row#4 | 「Binary diffusion coefficient, m²/s」 | 「5」 |
| WM_L1_Q1_Table#1_Row#5 | 「Surface tension liquid-gas, N/m」 | 「4」 |
| WM_L1_Q1_Table#1_Row#6 | 「Vapor or sublimation pressure, kPa」 | 「3」 |
| WM_L1_Q1_Table#1_Row#7 | 「Boiling temperature at pressure P, K」 | 「3」 |
| WM_L1_Q1_Table#1_Row#8 | 「Mole fraction」 | 「2」 |
| WM_L1_Q1_Table#1_Row#9 | 「Refractive index (Na D-line)」 | 「2」 |
| WM_L1_Q1_Table#1_Row#10 | 「Specific volume, m³/kg」 | 「2」 |

**Top literature sources:**

**WM_L1_Q1_Table#2_(Query_L1_Q1_Answer):**

| *row_id* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#2_Row#1 | 「10.1016/j.jct.2018.02.022 (GLOBlit_5201)」 | 「3」 | 「456」 |
| WM_L1_Q1_Table#2_Row#2 | 「10.1021/je4001203 (GLOBlit_10102)」 | 「2」 | 「276」 |
| WM_L1_Q1_Table#2_Row#3 | 「10.1021/je020140j (GLOBlit_8038)」 | 「3」 | 「249」 |
| WM_L1_Q1_Table#2_Row#4 | 「10.1021/acs.jced.6b00526 (GLOBlit_6951)」 | 「3」 | 「236」 |
| WM_L1_Q1_Table#2_Row#5 | 「10.1016/j.fluid.2013.06.041 (GLOBlit_1283)」 | 「2」 | 「214」 |

---

##### 2. Propylene Glycol (1,2-Propanediol) + Water

- **Compound IDs:** GLOBcomp_61 + GLOBcomp_1
- **Coverage:** 34 blocks, 18 papers, 1,780 data points
- **Temperature range:** 253.15 – 573.19 K
- **Pressure range:** 100.0 – 350,000.0 kPa

**Properties measured (blocks):**

**WM_L1_Q1_Table#3_(Query_L1_Q1_Answer):**

| *row_id* | *Property* | *Blocks* |
|---|---|---|
| WM_L1_Q1_Table#3_Row#1 | 「Mass density, kg/m³」 | 「10」 |
| WM_L1_Q1_Table#3_Row#2 | 「Speed of sound, m/s」 | 「4」 |
| WM_L1_Q1_Table#3_Row#3 | 「Viscosity, Pa·s」 | 「4」 |
| WM_L1_Q1_Table#3_Row#4 | 「Excess molar volume, m³/mol」 | 「2」 |
| WM_L1_Q1_Table#3_Row#5 | 「Molar heat capacity at constant pressure, J/K/mol」 | 「2」 |
| WM_L1_Q1_Table#3_Row#6 | 「Thermal conductivity, W/m/K」 | 「2」 |
| WM_L1_Q1_Table#3_Row#7 | 「Specific volume, m³/kg」 | 「2」 |
| WM_L1_Q1_Table#3_Row#8 | 「Excess molar heat capacity, J/K/mol」 | 「1」 |
| WM_L1_Q1_Table#3_Row#9 | 「Surface tension liquid-gas, N/m」 | 「1」 |
| WM_L1_Q1_Table#3_Row#10 | 「Excess molar enthalpy (molar enthalpy of mixing), kJ/mol」 | 「1」 |

**Top literature sources:**

**WM_L1_Q1_Table#4_(Query_L1_Q1_Answer):**

| *row_id* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#4_Row#1 | 「10.1021/je0340755 (GLOBlit_8239)」 | 「3」 | 「375」 |
| WM_L1_Q1_Table#4_Row#2 | 「10.1021/acs.jced.8b00403 (GLOBlit_7545)」 | 「3」 | 「291」 |
| WM_L1_Q1_Table#4_Row#3 | 「10.1021/je201184b (GLOBlit_9758)」 | 「2」 | 「212」 |
| WM_L1_Q1_Table#4_Row#4 | 「10.1016/j.fluid.2013.06.041 (GLOBlit_1283)」 | 「2」 | 「185」 |
| WM_L1_Q1_Table#4_Row#5 | 「10.1016/j.fluid.2014.12.040 (GLOBlit_1623)」 | 「2」 | 「168」 |

---

##### 3. Diethylene Glycol + Water

- **Compound IDs:** GLOBcomp_111 + GLOBcomp_1
- **Coverage:** 28 blocks, 15 papers, 2,079 data points
- **Temperature range:** 278.15 – 573.184 K
- **Pressure range:** 50.0 – 30,500.0 kPa

**Properties measured (blocks):**

**WM_L1_Q1_Table#5_(Query_L1_Q1_Answer):**

| *row_id* | *Property* | *Blocks* |
|---|---|---|
| WM_L1_Q1_Table#5_Row#1 | 「Mass density, kg/m³」 | 「10」 |
| WM_L1_Q1_Table#5_Row#2 | 「Speed of sound, m/s」 | 「6」 |
| WM_L1_Q1_Table#5_Row#3 | 「Viscosity, Pa·s」 | 「4」 |
| WM_L1_Q1_Table#5_Row#4 | 「Binary diffusion coefficient, m²/s」 | 「2」 |
| WM_L1_Q1_Table#5_Row#5 | 「Excess molar enthalpy (molar enthalpy of mixing), kJ/mol」 | 「2」 |
| WM_L1_Q1_Table#5_Row#6 | 「Molar heat capacity at constant pressure, J/K/mol」 | 「1」 |
| WM_L1_Q1_Table#5_Row#7 | 「Boiling temperature at pressure P, K」 | 「1」 |
| WM_L1_Q1_Table#5_Row#8 | 「Refractive index (Na D-line)」 | 「1」 |
| WM_L1_Q1_Table#5_Row#9 | 「Thermal conductivity, W/m/K」 | 「1」 |

**Top literature sources:**

**WM_L1_Q1_Table#6_(Query_L1_Q1_Answer):**

| *row_id* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#6_Row#1 | 「10.1016/j.jct.2016.07.016 (GLOBlit_4754)」 | 「1」 | 「588」 |
| WM_L1_Q1_Table#6_Row#2 | 「10.1016/j.jct.2018.02.022 (GLOBlit_5201)」 | 「3」 | 「456」 |
| WM_L1_Q1_Table#6_Row#3 | 「10.1021/je700672f (GLOBlit_11031)」 | 「2」 | 「286」 |
| WM_L1_Q1_Table#6_Row#4 | 「10.1021/je1009976 (GLOBlit_9382)」 | 「2」 | 「170」 |
| WM_L1_Q1_Table#6_Row#5 | 「10.1021/acs.jced.5b00498 (GLOBlit_6630)」 | 「2」 | 「140」 |

---

##### 4. Triethylene Glycol + Water

- **Compound IDs:** GLOBcomp_113 + GLOBcomp_1
- **Coverage:** 40 blocks, 16 papers, 3,638 data points
- **Temperature range:** 278.15 – 573.183 K
- **Pressure range:** 50.0 – 30,510.0 kPa

**Properties measured (blocks):**

**WM_L1_Q1_Table#7_(Query_L1_Q1_Answer):**

| *row_id* | *Property* | *Blocks* |
|---|---|---|
| WM_L1_Q1_Table#7_Row#1 | 「Mass density, kg/m³」 | 「10」 |
| WM_L1_Q1_Table#7_Row#2 | 「Refractive index (other wavelength)」 | 「9」 |
| WM_L1_Q1_Table#7_Row#3 | 「Speed of sound, m/s」 | 「6」 |
| WM_L1_Q1_Table#7_Row#4 | 「Boiling temperature at pressure P, K」 | 「3」 |
| WM_L1_Q1_Table#7_Row#5 | 「Viscosity, Pa·s」 | 「3」 |
| WM_L1_Q1_Table#7_Row#6 | 「Binary diffusion coefficient, m²/s」 | 「2」 |
| WM_L1_Q1_Table#7_Row#7 | 「Mole fraction」 | 「2」 |
| WM_L1_Q1_Table#7_Row#8 | 「Joule-Thomson coefficient, K/kPa」 | 「1」 |
| WM_L1_Q1_Table#7_Row#9 | 「Molar heat capacity at constant pressure, J/K/mol」 | 「1」 |
| WM_L1_Q1_Table#7_Row#10 | 「Excess molar enthalpy (molar enthalpy of mixing), kJ/mol」 | 「1」 |

**Top literature sources:**

**WM_L1_Q1_Table#8_(Query_L1_Q1_Answer):**

| *row_id* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|
| WM_L1_Q1_Table#8_Row#1 | 「10.1016/j.fluid.2015.07.030 (GLOBlit_1753)」 | 「12」 | 「1370」 |
| WM_L1_Q1_Table#8_Row#2 | 「10.1016/j.jct.2015.05.024 (GLOBlit_4395)」 | 「2」 | 「667」 |
| WM_L1_Q1_Table#8_Row#3 | 「10.1016/j.jct.2016.07.016 (GLOBlit_4754)」 | 「1」 | 「598」 |
| WM_L1_Q1_Table#8_Row#4 | 「10.1016/j.jct.2018.02.022 (GLOBlit_5201)」 | 「3」 | 「432」 |
| WM_L1_Q1_Table#8_Row#5 | 「10.1021/acs.jced.5b00498 (GLOBlit_6630)」 | 「2」 | 「140」 |

---

##### Cross-System Summary

**WM_L1_Q1_Table#9_(Query_L1_Q1_Answer):**

| *row_id* | *Glycol + Water System* | *Blocks* | *Papers* | *Data Points* | *T range (K)* | *P range (kPa)* |
|---|---|---|---|---|---|---|
| WM_L1_Q1_Table#9_Row#1 | 「Ethylene glycol」 | 「59」 | 「32」 | 「2,584」 | 「258.32 – 573.23」 | 「50.0 – 350,200.0」 |
| WM_L1_Q1_Table#9_Row#2 | 「Propylene glycol」 | 「34」 | 「18」 | 「1,780」 | 「253.15 – 573.19」 | 「100.0 – 350,000.0」 |
| WM_L1_Q1_Table#9_Row#3 | 「Diethylene glycol」 | 「28」 | 「15」 | 「2,079」 | 「278.15 – 573.184」 | 「50.0 – 30,500.0」 |
| WM_L1_Q1_Table#9_Row#4 | 「Triethylene glycol」 | 「40」 | 「16」 | 「3,638」 | 「278.15 – 573.183」 | 「50.0 – 30,510.0」 |
| WM_L1_Q1_Table#9_Row#5 | 「**Total**」 | 「**161**」 | 「**81***」 | 「**10,081**」 | 「—」 | 「—」 |

*Some papers appear in multiple systems (e.g., GLOBlit_5201 and GLOBlit_1283 cover multiple glycol systems), so the unique paper count is lower.

##### Key Observations

- **Mass density** is the most commonly measured property across all four systems (46 blocks total), reflecting its importance for engineering applications of glycol-water heat transfer fluids and antifreeze formulations.
- **Speed of sound** and **viscosity** are the next most common, each appearing in all four systems.
- **Triethylene glycol + water** has the largest dataset (3,638 points), driven largely by a single comprehensive study (GLOBlit_1753, DOI: 10.1016/j.fluid.2015.07.030) contributing 1,370 points across 12 blocks.
- **Ethylene glycol + water** has the broadest literature coverage (32 papers), consistent with its widespread industrial use as an antifreeze and coolant.
- All four systems span similar upper temperature ranges (~573 K), but ethylene glycol and propylene glycol systems extend to higher pressures (up to ~350 MPa), likely from high-pressure density studies.
- Transport properties (diffusion coefficients, thermal conductivity) and excess thermodynamic properties (excess molar enthalpy, excess molar volume) are available but less common than volumetric and acoustic properties.

**Core claims:**
- The ThermoML database contains data for four glycol + water binary systems (ethylene glycol, propylene glycol, diethylene glycol, triethylene glycol), totaling 161 property blocks across 81 literature sources (some shared across systems) with 10,081 data points.
- Ethylene glycol + water has the broadest literature coverage (59 blocks, 32 papers, 2,584 data points), spanning 258.32 – 573.23 K and 50.0 – 350,200.0 kPa.
- Propylene glycol + water covers 34 blocks, 18 papers, and 1,780 data points, spanning 253.15 – 573.19 K and 100.0 – 350,000.0 kPa.
- Diethylene glycol + water covers 28 blocks, 15 papers, and 2,079 data points, spanning 278.15 – 573.184 K and 50.0 – 30,500.0 kPa.
- Triethylene glycol + water has the largest dataset (40 blocks, 16 papers, 3,638 data points), spanning 278.15 – 573.183 K and 50.0 – 30,510.0 kPa, driven largely by a single study (DOI: 10.1016/j.fluid.2015.07.030) contributing 1,370 points across 12 blocks.
- Mass density is the most commonly measured property across all four systems (46 blocks total), followed by speed of sound and viscosity, each appearing in all four systems.
- Ethylene glycol and propylene glycol systems extend to higher pressures (up to ~350 MPa), likely from high-pressure density studies, while all four systems span similar upper temperature ranges (~573 K).
- Transport properties (diffusion coefficients, thermal conductivity) and excess thermodynamic properties (excess molar enthalpy, excess molar volume) are available but less common than volumetric and acoustic properties.

*Not stored here: 20 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


