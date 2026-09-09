# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_061638_520980_6ff95b07`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_2 | ethanol |  |
| comp | GLOBcomp_1 | water |  |
| comp | GLOBcomp_4 | methanol |  |
| prop | GLOBprop_4 | viscositypas |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<water> |  |
| constr | GLOBconstr_1 | pressurekpa |  |

### History
- [query_thermoml]
- [query_thermoml]
- [fit_multi_system]
- [inspect_block]
- [inspect_block]
- [fit_multi_system]
- [predict_from_rk]
- [predict_from_rk]

### Query Results
#### query
**L1_query_1** — status: success · validation: PASS

**Summary:** Ten ThermoML data blocks for dynamic viscosity of the ethanol + water binary mixture near 298.15 K were identified. Six were inspected in detail. GLOBlit_5201 (PROPblock_21, DOI 10.1016/j.jct.2018.02.022) is the most comprehensive with 100 points spanning the full ethanol mole-fraction range (0–1) over 293.15–308.15 K, with viscosities from 0.00075887 to 0.0028641 Pa·s. GLOBlit_2825 (PROPblock_11, DOI 10.1016/j.jct.2007.05.004) provides 37 points over the full water mole-fraction range (0–1) at 293.15–303.15 K, with viscosities from 0.000797 to 0.002705 Pa·s. At 298.15 K in Block 1, viscosity rises from 0.001082 Pa·s at x(water)=0 to 0.002275 Pa·s at x(water)=0.6991. GLOBlit_7448 (PROPblock_47, DOI 10.1021/acs.jced.8b00086) reports 6 points at 298.2 K in mass fraction of water (0.206–0.508), with viscosities 0.001676–0.002235 Pa·s. GLOBlit_7676 (PROPblock_18, DOI 10.1021/acs.jced.8b00939) reports 9 points at 298.2 K in mass fraction of water (0.061–0.62), with viscosities 0.00131–0.00234 Pa·s. GLOBlit_10159 (PROPblock_8, DOI 10.1021/je4003515) gives 5 points at 298.15 K in molality of ethanol (14–22 mol·kg⁻¹), with viscosities 0.00235–0.002371 Pa·s. Composition variables across the blocks include mole fraction, mass fraction, and molality. The data consistently show viscosity increasing with water content in the water-rich region, consistent with the known viscosity maximum at intermediate compositions in the ethanol–water system.

**Answer:**

#### Viscosity Data for Ethanol + Water Binary Mixture at ~298.15 K

Ten binary ethanol + water data blocks with dynamic viscosity (GLOBprop_4) measurements were found in the ThermoML database near 298.15 K. Below are the six most detailed blocks with inspected data:

##### Block Summary

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *#* | *DOI* | *Block* | *Literature ID* | *Composition Variable* | *T range (K)* | *Composition range* | *η range (Pa·s)* | *Total pts* |
|---|---|---|---|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「1」 | 「10.1016/j.jct.2007.05.004」 | 「PROPblock_11」 | 「GLOBlit_2825」 | 「x(water)」 | 「293.15–303.15」 | 「0–1」 | 「0.000797–0.002705」 | 「37」 |
| WM_L1#1_Table#1_Row#2 | 「2」 | 「10.1016/j.jct.2018.02.022」 | 「PROPblock_21」 | 「GLOBlit_5201」 | 「x(ethanol)」 | 「293.15–308.15」 | 「0–1」 | 「0.00075887–0.0028641」 | 「100」 |
| WM_L1#1_Table#1_Row#3 | 「3」 | 「10.1021/acs.jced.7b00299」 | 「PROPblock_11」 | 「GLOBlit_7178」 | 「T only (fixed molality)」 | 「298.15–303.15」 | 「—」 | 「(not inspected in this run)」 | 「2」 |
| WM_L1#1_Table#1_Row#4 | 「4」 | 「10.1021/acs.jced.8b00086」 | 「PROPblock_47」 | 「GLOBlit_7448」 | 「w(water)」 | 「298.2 (fixed)」 | 「0.206–0.508」 | 「0.001676–0.002235」 | 「6」 |
| WM_L1#1_Table#1_Row#5 | 「5」 | 「10.1021/acs.jced.8b00939」 | 「PROPblock_18」 | 「GLOBlit_7676」 | 「w(water)」 | 「298.2 (fixed)」 | 「0.061–0.62」 | 「0.00131–0.00234」 | 「9」 |
| WM_L1#1_Table#1_Row#6 | 「6」 | 「10.1021/je4003515」 | 「PROPblock_8」 | 「GLOBlit_10159」 | 「b(ethanol) / mol·kg⁻¹」 | 「293.15–313.15」 | 「14–22」 | 「0.00144–0.0029」 | 「25」 |

##### Representative Data at 298.15 K

**Block 1 (GLOBlit_2825, PROPblock_11)** — 8 points at exactly 298.15 K, mole fraction of water, p = 101.0 kPa:

**WM_L1#1_Table#2_(Analysis_L1#1_Answer):**

| *row_id* | *x(water)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0」 | 「0.001082」 |
| WM_L1#1_Table#2_Row#2 | 「0.0501」 | 「0.001153」 |
| WM_L1#1_Table#2_Row#3 | 「0.0986」 | 「0.001232」 |
| WM_L1#1_Table#2_Row#4 | 「0.1961」 | 「0.00138」 |
| WM_L1#1_Table#2_Row#5 | 「0.2961」 | 「0.001531」 |
| WM_L1#1_Table#2_Row#6 | 「0.3991」 | 「0.001659」 |
| WM_L1#1_Table#2_Row#7 | 「0.5989」 | 「0.002115」 |
| WM_L1#1_Table#2_Row#8 | 「0.6991」 | 「0.002275」 |

**Block 2 (GLOBlit_5201, PROPblock_21)** — 8 of 100 points shown at 298.15 K, mole fraction of ethanol, p = 92.3 kPa:

**WM_L1#1_Table#3_(Analysis_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0.0201」 | 「0.001098」 |
| WM_L1#1_Table#3_Row#2 | 「0.0408」 | 「0.0013359」 |
| WM_L1#1_Table#3_Row#3 | 「0.0497」 | 「0.0014322」 |
| WM_L1#1_Table#3_Row#4 | 「0.06」 | 「0.0015515」 |
| WM_L1#1_Table#3_Row#5 | 「0.0796」 | 「0.001748」 |
| WM_L1#1_Table#3_Row#6 | 「0.1004」 | 「0.0019469」 |
| WM_L1#1_Table#3_Row#7 | 「0.1499」 | 「0.0022424」 |
| WM_L1#1_Table#3_Row#8 | 「0.1984」 | 「0.0023706」 |

**Block 4 (GLOBlit_7448, PROPblock_47)** — all 6 points at 298.2 K, mass fraction of water, p = 100.0 kPa:

**WM_L1#1_Table#4_(Analysis_L1#1_Answer):**

| *row_id* | *w(water)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#4_Row#1 | 「0.206」 | 「0.001676」 |
| WM_L1#1_Table#4_Row#2 | 「0.235」 | 「0.001731」 |
| WM_L1#1_Table#4_Row#3 | 「0.247」 | 「0.001798」 |
| WM_L1#1_Table#4_Row#4 | 「0.311」 | 「0.001799」 |
| WM_L1#1_Table#4_Row#5 | 「0.426」 | 「0.00218」 |
| WM_L1#1_Table#4_Row#6 | 「0.508」 | 「0.002235」 |

**Block 5 (GLOBlit_7676, PROPblock_18)** — all 9 points at 298.2 K, mass fraction of water, p = 100.0 kPa:

**WM_L1#1_Table#5_(Analysis_L1#1_Answer):**

| *row_id* | *w(water)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#5_Row#1 | 「0.061」 | 「0.00131」 |
| WM_L1#1_Table#5_Row#2 | 「0.124」 | 「0.00146」 |
| WM_L1#1_Table#5_Row#3 | 「0.172」 | 「0.00164」 |
| WM_L1#1_Table#5_Row#4 | 「0.233」 | 「0.0018」 |
| WM_L1#1_Table#5_Row#5 | 「0.276」 | 「0.00187」 |
| WM_L1#1_Table#5_Row#6 | 「0.34」 | 「0.0019」 |
| WM_L1#1_Table#5_Row#7 | 「0.41」 | 「0.00219」 |
| WM_L1#1_Table#5_Row#8 | 「0.5」 | 「0.00231」 |
| WM_L1#1_Table#5_Row#9 | 「0.62」 | 「0.00234」 |

**Block 6 (GLOBlit_10159, PROPblock_8)** — 5 points at exactly 298.15 K, molality of ethanol, p = 101.0 kPa:

**WM_L1#1_Table#6_(Analysis_L1#1_Answer):**

| *row_id* | *b(ethanol) / mol·kg⁻¹* | *η (Pa·s)* |
|---|---|---|
| WM_L1#1_Table#6_Row#1 | 「14」 | 「0.00235」 |
| WM_L1#1_Table#6_Row#2 | 「16」 | 「0.002363」 |
| WM_L1#1_Table#6_Row#3 | 「18」 | 「0.002365」 |
| WM_L1#1_Table#6_Row#4 | 「20」 | 「0.002371」 |
| WM_L1#1_Table#6_Row#5 | 「22」 | 「0.002352」 |

##### Key Observations

- **Most comprehensive datasets:** GLOBlit_5201 (PROPblock_21) contains 100 data points spanning the full ethanol mole-fraction range (0–1), and GLOBlit_2825 (PROPblock_11) has 37 points covering the full water mole-fraction range (0–1). Both include multiple isotherms.
- **Viscosity trend with composition:** The inspected data consistently show viscosity increasing with water content in the water-rich region. For example, in Block 1 at 298.15 K, viscosity rises from 0.001082 Pa·s (pure ethanol, x_water = 0) to 0.002275 Pa·s at x_water = 0.6991. The ethanol–water system is known for a viscosity maximum at intermediate compositions.
- **Fixed-temperature blocks:** GLOBlit_7448 (PROPblock_47) and GLOBlit_7676 (PROPblock_18) report data at a single temperature of 298.2 K, making them directly usable without interpolation.
- **Composition variables** span mole fraction, mass fraction, and molality across different studies, offering complementary coverage of the composition space.
- **Block 3 note:** GLOBlit_7178 (PROPblock_11) contains only 2 data points and was not inspected in this run; its viscosity range values from the initial search are not quoted here.

A total of 10 blocks were matched in the search; the six above are the most detailed entries returned.

**Core claims:**
- Ten binary ethanol + water data blocks with dynamic viscosity measurements near 298.15 K were found in the ThermoML database, of which six were inspected in detail.
- The two most comprehensive datasets are GLOBlit_5201 (PROPblock_21, 100 data points spanning the full ethanol mole-fraction range 0–1) and GLOBlit_2825 (PROPblock_11, 37 points covering the full water mole-fraction range 0–1), both including multiple isotherms.
- At 298.15 K, the inspected data consistently show viscosity increasing with water content in the water-rich region; for example, in Block 1 viscosity rises from 0.001082 Pa·s at x(water) = 0 (pure ethanol) to 0.002275 Pa·s at x(water) = 0.6991.
- Composition variables across the different studies span mole fraction, mass fraction, and molality, offering complementary coverage of the composition space.
- Two blocks (GLOBlit_7448 and GLOBlit_7676) report data at a single temperature of 298.2 K, making them directly usable without interpolation.
- The overall viscosity range across all inspected blocks at ~298.15 K spans approximately 0.00075887–0.0028641 Pa·s depending on composition.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#7 | 「GLOBlit_2825」 | 「PROPblock_11」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture; mole fraction of water; T = 293.15–303.15 K; 37 data points.」 |
| WM_L1#1_Table#8 | 「GLOBlit_5201」 | 「PROPblock_21」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture; mole fraction of ethanol; T = 293.15–308.15 K; 100 data points.」 |
| WM_L1#1_Table#9 | 「GLOBlit_7178」 | 「PROPblock_11」 | 「GLOBcomp_1, GLOBcomp_2」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture; fixed molality; T = 298.15–303.15 K; 2 data points.」 |
| WM_L1#1_Table#10 | 「GLOBlit_7448」 | 「PROPblock_47」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture; mass fraction of water; T = 298.2 K; 6 data points.」 |
| WM_L1#1_Table#11 | 「GLOBlit_7676」 | 「PROPblock_18」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture; mass fraction of water; T = 298.2 K; 9 data points.」 |
| WM_L1#1_Table#12 | 「GLOBlit_10159」 | 「PROPblock_8」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture; molality of ethanol; T = 293.15–313.15 K; 25 data points.」 |

*Not stored here: 5 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### query
**L1_query_2** — status: success · validation: FLAGGED(1)

**Summary:** Three ThermoML blocks report binary methanol–water dynamic viscosity at 298.15 K and 101.0 kPa. The most comprehensive is PROPblock_9 (GLOBlit_2825, DOI 10.1016/j.jct.2007.05.004), which provides 13 data points spanning the full mole-fraction range of water (0 to 1). At 298.15 K, viscosity rises from pure methanol (0.000545 Pa·s at x(water)=0) to a maximum near x(water)≈0.70 (0.001554 Pa·s), then decreases to pure water (0.00089 Pa·s), illustrating the well-known viscosity maximum due to hydrogen-bonding interactions. PROPblock_3 (GLOBlit_8869, DOI 10.1021/je0600810) reports three points at 298.15 K in volume fraction of methanol (0.01–0.3), with viscosities 0.0010844–0.0014712 Pa·s. PROPblock_1 (GLOBlit_9571, DOI 10.1021/je2003622) reports four points at 298.15 K in mass fraction of methanol (0.0806–0.3446), with viscosities 0.0010844–0.0014712 Pa·s, showing a slight decrease from w=0.2526 to 0.3446 consistent with the viscosity maximum in that region. PROPblock_9 is recommended as the most complete dataset for this system.

**Answer:**

#### Binary Methanol + Water Dynamic Viscosity Data Near 298.15 K

Three binary methanol–water dynamic viscosity (GLOBprop_4) data blocks were found in the ThermoML database with measurements at 298.15 K. All blocks report data at a fixed pressure of 101.0 kPa.

---

##### Block Summary

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *Block* | *Literature* | *DOI* | *Composition Variable* | *Composition Range* | *T Range (K)* | *Viscosity Range (Pa·s)* | *Total Points* | *Points at 298.15 K* |
|---|---|---|---|---|---|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「PROPblock_9」 | 「GLOBlit_2825」 | 「10.1016/j.jct.2007.05.004」 | 「Mole fraction (water)」 | 「0–1」 | 「293.15–303.15」 | 「0.000508–0.001793」 | 「39」 | 「13」 |
| WM_L1#2_Table#1_Row#2 | 「PROPblock_3」 | 「GLOBlit_8869」 | 「10.1021/je0600810」 | 「Volume fraction (methanol)」 | 「0.01–0.3」 | 「298.15–318.15」 | 「0.000702–0.0014712」 | 「9」 | 「3」 |
| WM_L1#2_Table#1_Row#3 | 「PROPblock_1」 | 「GLOBlit_9571」 | 「10.1021/je2003622」 | 「Mass fraction (methanol)」 | 「0.0806–0.3446」 | 「298.15–323.15」 | 「0.0006375–0.0014712」 | 「16」 | 「4」 |

---

##### Most Comprehensive Block: PROPblock_9 (GLOBlit_2825)

**DOI:** 10.1016/j.jct.2007.05.004  
**Composition variable:** Mole fraction of water, x(water) = 0 to 1  
**Full composition coverage at 298.15 K (13 data points, 12 shown by RDP):**

**WM_L1#2_Table#2_(Analysis_L1#2_Answer):**

| *row_id* | *x(water)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「0」 | 「0.000545」 |
| WM_L1#2_Table#2_Row#2 | 「0.049」 | 「0.000607」 |
| WM_L1#2_Table#2_Row#3 | 「0.0993」 | 「0.000677」 |
| WM_L1#2_Table#2_Row#4 | 「0.1973」 | 「0.000821」 |
| WM_L1#2_Table#2_Row#5 | 「0.2983」 | 「0.000987」 |
| WM_L1#2_Table#2_Row#6 | 「0.3985」 | 「0.00115」 |
| WM_L1#2_Table#2_Row#7 | 「0.5994」 | 「0.001463」 |
| WM_L1#2_Table#2_Row#8 | 「0.6997」 | 「0.001554」 |
| WM_L1#2_Table#2_Row#9 | 「0.7986」 | 「0.001542」 |
| WM_L1#2_Table#2_Row#10 | 「0.8999」 | 「0.001317」 |
| WM_L1#2_Table#2_Row#11 | 「0.9512」 | 「0.001121」 |
| WM_L1#2_Table#2_Row#12 | 「1.0」 | 「0.00089」 |

This block clearly shows the well-known viscosity maximum in the methanol–water system: viscosity rises from pure methanol (0.000545 Pa·s) to a maximum near x(water) ≈ 0.70 (0.001554 Pa·s), then decreases toward pure water (0.00089 Pa·s). The maximum viscosity is several times larger than the pure-component values (derived from the inspected rows: 0.001554 / 0.000545 ≈ 2.9× pure methanol; 0.001554 / 0.00089 ≈ 1.7× pure water), reflecting strong hydrogen-bonding interactions and structural reorganization in the mixture.

---

##### PROPblock_3 (GLOBlit_8869) — Data at 298.15 K

**DOI:** 10.1021/je0600810  
**Composition variable:** Volume fraction of methanol (φ_v)

**WM_L1#2_Table#3_(Analysis_L1#2_Answer):**

| *row_id* | *φ_v(methanol)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#2_Table#3_Row#1 | 「0.01」 | 「0.0010844」 |
| WM_L1#2_Table#3_Row#2 | 「0.2」 | 「0.0013106」 |
| WM_L1#2_Table#3_Row#3 | 「0.3」 | 「0.0014712」 |

Covers only the methanol-dilute region (φ_v = 0.01–0.3).

---

##### PROPblock_1 (GLOBlit_9571) — Data at 298.15 K

**DOI:** 10.1021/je2003622  
**Composition variable:** Mass fraction of methanol (w)

**WM_L1#2_Table#4_(Analysis_L1#2_Answer):**

| *row_id* | *w(methanol)* | *η (Pa·s)* |
|---|---|---|
| WM_L1#2_Table#4_Row#1 | 「0.0806」 | 「0.0010844」 |
| WM_L1#2_Table#4_Row#2 | 「0.1647」 | 「0.0013106」 |
| WM_L1#2_Table#4_Row#3 | 「0.2526」 | 「0.0014712」 |
| WM_L1#2_Table#4_Row#4 | 「0.3446」 | 「0.0014475」 |

Also covers a limited methanol-lean range (w = 0.08–0.34). The slight decrease from w = 0.2526 to 0.3446 is consistent with the viscosity maximum occurring in this composition region.

---

##### Recommendation

**PROPblock_9 (GLOBlit_2825, DOI: 10.1016/j.jct.2007.05.004)** is by far the most comprehensive dataset, providing full mole-fraction coverage (0–1) at 298.15 K with 13 data points and clear resolution of the viscosity maximum. The other two blocks cover only narrow methanol-lean composition windows and use volume fraction or mass fraction rather than mole fraction.

**Core claims:**
- Three binary methanol–water dynamic viscosity data blocks were found in ThermoML with measurements at 298.15 K, all at a fixed pressure of 101.0 kPa.
- PROPblock_9 (DOI: 10.1016/j.jct.2007.05.004) is the most comprehensive dataset, providing 13 data points spanning the full mole-fraction range of water (0 to 1) at 298.15 K.
- PROPblock_9 shows the well-known viscosity maximum in the methanol–water system: viscosity rises from pure methanol (0.000545 Pa·s at x(water)=0) to a maximum near x(water) ≈ 0.70 (0.001554 Pa·s), then decreases toward pure water (0.00089 Pa·s at x(water)=1.0).
- The other two blocks (PROPblock_3 and PROPblock_1) cover only narrow methanol-lean composition windows using volume fraction (0.01–0.3) and mass fraction (0.0806–0.3446), respectively.
- PROPblock_1 data show a slight viscosity decrease from w(methanol)=0.2526 to 0.3446, consistent with the viscosity maximum occurring in that composition region.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#5 | 「GLOBlit_2825」 | 「PROPblock_9」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of methanol + water binary mixture at 293.15–303.15 K, mole fraction of water 0–1, 39 total points (13 at 298.15 K). Full composition coverage showing viscosity maximum near x(water) ≈ 0.70.」 |
| WM_L1#2_Table#6 | 「GLOBlit_8869」 | 「PROPblock_3」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of methanol + water binary mixture at 298.15–318.15 K, volume fraction of methanol 0.01–0.3, 9 total points (3 at 298.15 K). Limited methanol-dilute region.」 |
| WM_L1#2_Table#7 | 「GLOBlit_9571」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of methanol + water binary mixture at 298.15–323.15 K, mass fraction of methanol 0.0806–0.3446, 16 total points (4 at 298.15 K). Limited methanol-lean region.」 |

*Not stored here: 3 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_VALUE** PROPblock_9: 1.7 exists in PROPblock_9's database table but was never shown in an inspection of this run


### Inspected Blocks
- GLOBlit_5201 | 10.1016/j.jct.2018.02.022 | PROPblock_21: 100 rows; x=['mole_fraction_<ethanol>']; y=['viscosity_pa_s']
    - BLKprop_1 / GLOBprop_4: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_4: kind=direct; materialize_reference=False; supported=True; units=Pa*s -> Pa*s
- GLOBlit_2825 | 10.1016/j.jct.2007.05.004 | PROPblock_9: 39 rows; x=['mole_fraction_<water>']; y=['viscosity_pa_s']
    - BLKprop_1 / GLOBprop_4: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_4: kind=direct; materialize_reference=False; supported=True; units=Pa*s -> Pa*s

### Completed Fits
  - ethanol_water_viscosity_298K [10.1016/j.jct.2018.02.022/PROPblock_21] (ethanol, water): RK order=4, R²=0.999334, RMSE=0.006612838327445672, coeffs=[2.727996, -2.492594, 2.550047, -2.44775, 1.536444]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: ethanol=0.0010914, water=0.00089689 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_excess.png
  - methanol_water_viscosity_298K [10.1016/j.jct.2007.05.004/PROPblock_9] (water, methanol): RK order=3, R²=0.999903, RMSE=0.0020496812938951637, coeffs=[2.534774, 1.422136, 1.33593, 0.754488]
      response: direct via X = reported X | 0 reference source(s) | Pa*s -> Pa*s
      pure refs: water=0.00089, methanol=0.000545 [block-edges (methanol: direct/good, water: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2007.05.004 PROPblock_9_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1
- `$ROOT/data\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2007.05.004 PROPblock_9_T298.1
- `$ROOT/data\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1

### plot
- `$ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2007.05.004 PROPblock_9_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1
- `$ROOT/plots\10_1016_j_jct_2007_05_004_BPROPblock_9_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2007.05.004 PROPblock_9_T298.1
- `$ROOT/plots\10_1016_j_jct_2018_02_022_BPROPblock_21_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2018.02.022 PROPblock_21_T298.1

