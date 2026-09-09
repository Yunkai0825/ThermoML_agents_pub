# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_2 | ethanol | ethanol |
| comp | GLOBcomp_1 | water | water |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find excess molar enthalpy data for ethanol + water binary mixtures near 298 K → stored as L1_query_1 · validation: PASS
- [L1] Find excess molar volume data for ethanol + water binary mixtures near 298 K → stored as L1_query_2 · validation: PASS
- [L1] Find any other excess or mixing properties for ethanol + water binary mixtures near 298 K besides HE and VE → stored as L1_query_3 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Excess molar enthalpy (HE) data for the ethanol + water binary system at 298.15 K were found in three verified ThermoML data blocks from two sources. DOI 10.1016/j.fluid.2007.06.007 (GLOBlit_528) provides two dilute-solution blocks measured by Calvet calorimetry at 298.15 K and 101.0 kPa: one for dilute ethanol in water (15 points, x(ethanol) = 0.000102–0.001551, HE from −0.00104 to −0.01537 kJ/mol) and one for dilute water in ethanol (15 points, x(water) = 0.001021–0.015286, HE from −0.00212 to −0.02961 kJ/mol). Both show a monotonic, nearly linear decrease in HE with increasing solute mole fraction, consistent with the initial slope governed by the partial molar excess enthalpy at infinite dilution. DOI 10.1016/j.tca.2017.05.023 (GLOBlit_6377) provides a single data point at x(ethanol) = 0.102, 298.15 K, 100 kPa, with HE = −0.70659 kJ/mol. All HE values are negative, confirming exothermic mixing. The dilute-solution data show |HE| on the order of 0.001–0.03 kJ/mol at mole fractions below ~0.015, while at x(ethanol) = 0.102 the value reaches −0.707 kJ/mol, consistent with the known strongly exothermic mixing behaviour where the HE minimum (typically around −0.8 to −0.9 kJ/mol) occurs near x(ethanol) ≈ 0.2–0.3 at 298 K. A fourth block (GLOBlit_2574::PROPblock_1) was excluded because it contained 1,2-propanediol + water data, not ethanol + water.

**Answer:**

#### Excess Molar Enthalpy (HE) Data for Ethanol + Water Binary Mixtures near 298 K

Three verified data blocks were found in the ThermoML database containing excess molar enthalpy measurements for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system at 298.15 K.

---

##### Source 1: DOI 10.1016/j.fluid.2007.06.007 (GLOBlit_528)

This reference provides two complementary dilute-solution blocks measured by Calvet calorimetry at 298.15 K and 101.0 kPa.

**PROPblock_1 — Dilute ethanol in water**
- 15 data points; x(ethanol) = 0.000102–0.001551
- HE range: −0.01537 to −0.00104 kJ/mol

Representative data points:

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *T (K)* | *P (kPa)* | *HE (kJ/mol)* |
|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.000102」 | 「298.15」 | 「101.0」 | 「−0.00104」 |
| WM_L1#1_Table#1_Row#2 | 「0.000516」 | 「298.15」 | 「101.0」 | 「−0.00518」 |
| WM_L1#1_Table#1_Row#3 | 「0.001034」 | 「298.15」 | 「101.0」 | 「−0.0103」 |
| WM_L1#1_Table#1_Row#4 | 「0.001551」 | 「298.15」 | 「101.0」 | 「−0.01537」 |

**PROPblock_2 — Dilute water in ethanol**
- 15 data points; x(water) = 0.001021–0.015286
- HE range: −0.02961 to −0.00212 kJ/mol

Representative data points:

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(water)* | *T (K)* | *P (kPa)* | *HE (kJ/mol)* |
|---|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0.001021」 | 「298.15」 | 「101.0」 | 「−0.00212」 |
| WM_L1#1_Table#2_Row#2 | 「0.006155」 | 「298.15」 | 「101.0」 | 「−0.01238」 |
| WM_L1#1_Table#2_Row#3 | 「0.012264」 | 「298.15」 | 「101.0」 | 「−0.02405」 |
| WM_L1#1_Table#2_Row#4 | 「0.015286」 | 「298.15」 | 「101.0」 | 「−0.02961」 |

Both blocks show a monotonic, nearly linear decrease in HE with increasing solute mole fraction in the very dilute regime, consistent with the initial slope of the HE–composition curve being governed by the partial molar excess enthalpy at infinite dilution.

---

##### Source 2: DOI 10.1016/j.tca.2017.05.023 (GLOBlit_6377)

**PROPblock_1 — Single data point at moderate composition**
- 1 data point at x(ethanol) = 0.102, 298.15 K, 100 kPa

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *T (K)* | *P (kPa)* | *HE (kJ/mol)* |
|---|---|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0.102」 | 「298.15」 | 「100」 | 「−0.70659」 |

---

##### Chemistry Insight

All measured HE values are **negative**, confirming that mixing ethanol and water at 298.15 K is an exothermic process. The magnitude of HE increases sharply as composition moves away from the pure-component limits: the dilute-solution data from GLOBlit_528 show |HE| on the order of 0.001–0.03 kJ/mol at mole fractions below ~0.015, while the single point from GLOBlit_6377 at x(ethanol) = 0.102 already reaches −0.707 kJ/mol. This is consistent with the well-known strongly exothermic mixing behaviour of the ethanol–water system, where the HE minimum (typically around −0.8 to −0.9 kJ/mol) occurs near x(ethanol) ≈ 0.2–0.3 at 298 K, driven by disruption and reorganisation of the hydrogen-bond network.

**Note:** A fourth block initially returned (GLOBlit_2574::PROPblock_1) was found upon inspection to contain 1,2-propanediol + water data, not ethanol + water, and was therefore excluded.

**Core claims:**
- Three verified ThermoML data blocks provide excess molar enthalpy (HE) measurements for ethanol + water binary mixtures at 298.15 K: two dilute-solution blocks from DOI 10.1016/j.fluid.2007.06.007 and one moderate-composition point from DOI 10.1016/j.tca.2017.05.023.
- All measured HE values are negative, confirming that mixing ethanol and water at 298.15 K is exothermic.
- In the dilute ethanol-in-water regime (x(ethanol) = 0.000102–0.001551), HE ranges from −0.00104 to −0.01537 kJ/mol; in the dilute water-in-ethanol regime (x(water) = 0.001021–0.015286), HE ranges from −0.00212 to −0.02961 kJ/mol, both showing a monotonic, nearly linear decrease with increasing solute mole fraction consistent with infinite-dilution partial molar excess enthalpy behaviour.
- At x(ethanol) = 0.102 and 298.15 K, HE = −0.70659 kJ/mol, indicating a sharp increase in |HE| as composition moves away from the pure-component limits.
- A fourth data block (GLOBlit_2574::PROPblock_1) was excluded because it contained 1,2-propanediol + water data rather than ethanol + water.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_528」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for dilute ethanol in water at 298.15 K and 101.0 kPa; 15 data points, x(ethanol) = 0.000102–0.001551, HE = −0.01537 to −0.00104 kJ/mol.」 |
| WM_L1#1_Table#5 | 「GLOBlit_528」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for dilute water in ethanol at 298.15 K and 101.0 kPa; 15 data points, x(water) = 0.001021–0.015286, HE = −0.02961 to −0.00212 kJ/mol.」 |
| WM_L1#1_Table#6 | 「GLOBlit_6377」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for ethanol + water at 298.15 K and 100 kPa; single data point at x(ethanol) = 0.102, HE = −0.70659 kJ/mol.」 |

*Not stored here: 3 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: no_results · validation: PASS

**Summary:** A search of the ThermoML database for excess molar volume (VE) data for the ethanol + water binary system returned zero results. Searches were conducted with a temperature window of 293–303 K, without any temperature restriction, and with system scope set to check both declared binary studies and binary subsystems in multicomponent datasets — no data blocks were found in any case. The ThermoML database does not contain excess molar volume data for the ethanol–water binary system at any temperature or composition. Excess molar enthalpy (HE) data for this system are available (from GLOBlit_528 and GLOBlit_6377), but the volumetric excess property has not been reported in the ThermoML holdings for this binary pair.

**Answer:**

###### Excess Molar Volume (VE) Data for Ethanol + Water Binary Mixtures near 298 K

**No excess molar volume data found.**

A thorough search of the ThermoML database for excess molar volume (VE, GLOBprop_28) measurements of the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system returned **zero results**. The search was conducted:

1. With a temperature window of 293–303 K and declared binary scope — no blocks found.
2. Without any temperature restriction and declared binary scope — no blocks found.
3. Without any temperature restriction and with `system_scope="either"` (checking both declared binary studies and binary subsystems embedded in multicomponent datasets) — no blocks found.

The ThermoML database does not contain excess molar volume data for the ethanol–water binary system at any temperature or composition. While excess molar enthalpy (HE) data for this system are available (from GLOBlit_528 and GLOBlit_6377, as found in the prior query), the complementary volumetric excess property has not been reported in the ThermoML holdings for this particular binary pair.

**Core claims:**
- A thorough search of the ThermoML database returned zero excess molar volume (VE) data for the ethanol–water binary system at any temperature or composition, including searches with and without temperature restrictions and across both declared binary studies and binary subsystems embedded in multicomponent datasets.
- While excess molar enthalpy (HE) data for ethanol–water are available in ThermoML, the complementary excess molar volume property has not been reported in the database for this binary pair.

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_3
**L1_query_3** — status: success · validation: FLAGGED(1)

**Summary:** For the ethanol + water binary system in the 293–303 K temperature window, the ThermoML database contains 10 distinct property types across 39 data blocks from 26 publications, totaling 3263 matching data points. The properties available (beyond excess molar enthalpy) are: mass density (kg/m³, 17 blocks), dynamic viscosity (Pa·s, 7 blocks), speed of sound (m/s, 3 blocks), refractive index at Na D-line (3 blocks), thermal conductivity (W/(m·K), 2 blocks), Henry's Law constant on mole fraction scale (kPa, 2 blocks), vapor or sublimation pressure (kPa, 1 block), surface tension liquid–gas (N/m, 1 block), and activity coefficient (1 block). Excess molar volume is not directly reported as a stored quantity, though the extensive mass density data could in principle be used to compute it. Top sources by matching data points include GLOBlit_220 (DOI 10.1016/j.fluid.2004.11.019, 810 points), GLOBlit_2432 (DOI 10.1016/j.jct.2004.07.019, 565 points), and GLOBlit_5201 (DOI 10.1016/j.jct.2018.02.022, 496 points across 3 property types). Inspected speed of sound data from GLOBlit_5201::PROPblock_20 at 298.15 K and 92.3 kPa show a pronounced maximum near x(ethanol) ≈ 0.1 of 1618.97 m/s, compared with pure water at 1496.99 m/s and pure ethanol at 1143.50 m/s, reflecting strong intermolecular interactions and structural reorganization in the mixture.

**Answer:**

#### Other Excess and Mixing Properties for Ethanol + Water Binary Mixtures near 298 K

Beyond the previously identified excess molar enthalpy (HE) data and the confirmed absence of excess molar volume (VE) data, the ThermoML database contains a rich set of thermodynamic and transport property measurements for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system in the 293–303 K temperature window.

##### Overview

A total of **10 distinct property types** are available across **39 data blocks** from **26 publications**, encompassing **3263 matching data points** in the 293–303 K range.

##### Properties Found (excluding HE)

**WM_L1#4_Table#1_(Query_L1#4_Answer):**

| *row_id* | *Property* | *Unit* | *Number of Blocks* | *Notes* |
|---|---|---|---|---|
| WM_L1#4_Table#1_Row#1 | 「Mass density」 | 「kg/m³」 | 「17」 | 「Most extensively measured property for this system」 |
| WM_L1#4_Table#1_Row#2 | 「Viscosity (dynamic)」 | 「Pa·s」 | 「7」 | 「」 |
| WM_L1#4_Table#1_Row#3 | 「Speed of sound」 | 「m/s」 | 「3」 | 「」 |
| WM_L1#4_Table#1_Row#4 | 「Refractive index (Na D-line)」 | 「—」 | 「3」 | 「」 |
| WM_L1#4_Table#1_Row#5 | 「Thermal conductivity」 | 「W/(m·K)」 | 「2」 | 「」 |
| WM_L1#4_Table#1_Row#6 | 「Henry's Law constant (mole fraction scale)」 | 「kPa」 | 「2」 | 「」 |
| WM_L1#4_Table#1_Row#7 | 「Vapor or sublimation pressure」 | 「kPa」 | 「1」 | 「」 |
| WM_L1#4_Table#1_Row#8 | 「Surface tension (liquid–gas)」 | 「N/m」 | 「1」 | 「」 |
| WM_L1#4_Table#1_Row#9 | 「Activity coefficient」 | 「—」 | 「1」 | 「」 |

##### Key Sources (by number of matching data points)

These are the top five papers by number of data points matching the 293–303 K window, as returned by the summary tool:

**WM_L1#4_Table#2_(Query_L1#4_Answer):**

| *row_id* | *Literature ID* | *DOI* | *Number of Property Types* | *Matching Points* |
|---|---|---|---|---|
| WM_L1#4_Table#2_Row#1 | 「GLOBlit_220」 | 「10.1016/j.fluid.2004.11.019」 | 「1」 | 「810」 |
| WM_L1#4_Table#2_Row#2 | 「GLOBlit_2432」 | 「10.1016/j.jct.2004.07.019」 | 「1」 | 「565」 |
| WM_L1#4_Table#2_Row#3 | 「GLOBlit_5201」 | 「10.1016/j.jct.2018.02.022」 | 「3」 | 「496」 |
| WM_L1#4_Table#2_Row#4 | 「GLOBlit_11136」 | 「10.1021/je800150h」 | 「2」 | 「216」 |
| WM_L1#4_Table#2_Row#5 | 「GLOBlit_9006」 | 「10.1021/je060335h」 | 「1」 | 「164」 |

##### Representative Inspected Block: Speed of Sound

As an example of the available data, GLOBlit_5201::PROPblock_20 contains speed of sound measurements for ethanol + water at 92.3 kPa and 3.0 MHz across temperatures 293.15–308.15 K and the full composition range x(ethanol) = 0–1 (152 data points total). Selected data at 298.15 K:

**WM_L1#4_Table#3_(Query_L1#4_Answer):**

| *row_id* | *x(ethanol)* | *T (K)* | *P (kPa)* | *Speed of sound (m/s)* |
|---|---|---|---|---|
| WM_L1#4_Table#3_Row#1 | 「0」 | 「298.15」 | 「92.3」 | 「1496.99」 |
| WM_L1#4_Table#3_Row#2 | 「0.0997」 | 「298.15」 | 「92.3」 | 「1618.97」 |
| WM_L1#4_Table#3_Row#3 | 「0.1497」 | 「298.15」 | 「92.3」 | 「1600.11」 |
| WM_L1#4_Table#3_Row#4 | 「0.3507」 | 「298.15」 | 「92.3」 | 「1426.17」 |
| WM_L1#4_Table#3_Row#5 | 「0.5002」 | 「298.15」 | 「92.3」 | 「1337.91」 |
| WM_L1#4_Table#3_Row#6 | 「1」 | 「298.15」 | 「92.3」 | 「1143.50」 |

The speed of sound shows a pronounced maximum near x(ethanol) ≈ 0.1, reaching 1618.97 m/s — well above the values for either pure water (1496.99 m/s) or pure ethanol (1143.50 m/s) at 298.15 K. This non-monotonic behaviour reflects the strong intermolecular interactions and structural reorganization in ethanol–water mixtures.

##### Additional Blocks Identified

The following blocks were returned by the search tools as containing ethanol + water binary data in the 293–303 K range (listed by literature and block identifiers; individual block data were not inspected in this run except for GLOBlit_5201::PROPblock_20):

GLOBlit_220::PROPblock_2, GLOBlit_384::PROPblock_3, GLOBlit_1483::PROPblock_1, GLOBlit_2432::PROPblock_2, GLOBlit_2574::PROPblock_4, GLOBlit_2825::PROPblock_11, GLOBlit_2825::PROPblock_12, GLOBlit_3475::PROPblock_3, GLOBlit_4415::PROPblock_7, GLOBlit_4415::PROPblock_8, GLOBlit_5201::PROPblock_19, and others (39 blocks total from the registry search).

##### Chemistry Insight

The ethanol–water binary system near 298 K is very well characterized in ThermoML for **volumetric** (mass density — 17 blocks) and **transport** (viscosity — 7 blocks) properties, but notably lacks the derived excess molar volume (VE) as a directly reported quantity. The extensive mass density coverage could in principle be used to compute VE, but the database stores only the directly measured or reported quantities. Additional properties such as speed of sound, refractive index, and thermal conductivity provide complementary structural and dynamic information about the hydrogen-bond network reorganization in ethanol–water mixtures. The presence of Henry's Law constant and activity coefficient data reflects the importance of this system for vapor–liquid equilibrium modeling.

**Core claims:**
- The ThermoML database contains 10 distinct property types across 39 data blocks from 26 publications (3263 matching data points) for the ethanol + water binary system in the 293–303 K temperature window.
- Mass density is the most extensively measured property for ethanol + water near 298 K, with 17 data blocks, followed by dynamic viscosity (7 blocks), speed of sound (3 blocks), refractive index (3 blocks), thermal conductivity (2 blocks), Henry's Law constant (2 blocks), vapor or sublimation pressure (1 block), surface tension (1 block), and activity coefficient (1 block).
- Excess molar volume (VE) is not directly reported as a stored quantity in ThermoML for this system, though the extensive mass density data could in principle be used to compute it.
- At 298.15 K and 92.3 kPa, the speed of sound in ethanol + water mixtures shows a non-monotonic composition dependence with a pronounced maximum near x(ethanol) ≈ 0.1, reaching 1618.97 m/s, compared to 1496.99 m/s for pure water and 1143.50 m/s for pure ethanol.
- The non-monotonic speed-of-sound behaviour reflects strong intermolecular interactions and structural reorganization in ethanol–water mixtures.
- Some quoted data values from blocks not directly inspected (e.g., GLOBlit_5201::PROPblock_19) remain unverified.

**Core blocks found:**

**WM_L1#4_Blocks_(Query_L1#4_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#4_Table#4 | 「GLOBlit_5201」 | 「PROPblock_20」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_8」 | 「Speed of sound measurements for ethanol + water at 298.15 K across full composition range.」 |
| WM_L1#4_Table#5 | 「GLOBlit_220」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for ethanol + water binary in the 293–303 K range.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** GLOBlit_5201::PROPblock_19: GLOBlit_5201::PROPblock_19 is quoted with data values (39, 298, 17, …) but was never inspected in this run (values 298 verified against the database — inspection is still mandatory)


