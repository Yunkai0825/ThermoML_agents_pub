# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_2 | ethanol | ethanol |
| comp | GLOBcomp_1 | water | water |
| prop | GLOBprop_4 | viscosity_pa_s | Viscosity, Pa*s |
| prop | GLOBprop_40 | kinematic_viscosity_m2_s | Kinematic viscosity, m2/s |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find viscosity data for ethanol + water binary mixture at mole fraction ~0.5 and 298.15 K → stored as L1_query_1 · validation: PASS
- [L1] Find excess viscosity or viscosity deviation data for ethanol + water binary mixture near x≈0.5 at 298.15 K → stored as L1_query_2 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Dynamic viscosity data for the ethanol + water binary mixture near equimolar composition at 298.15 K were found in ThermoML. The closest match is from GLOBlit_5201::PROPblock_21 (DOI 10.1016/j.jct.2018.02.022) at x(ethanol) = 0.4989 and 92.3 kPa, giving η = 0.0019557 Pa·s (≈1.96 mPa·s). That block contains 100 data points spanning T = 293.15–308.15 K and x(ethanol) = 0–1; at 298.15 K the full range is η = 0.00089689–0.0024286 Pa·s. A second block, GLOBlit_2825::PROPblock_11 (DOI 10.1016/j.jct.2007.05.004, 101.0 kPa), brackets x(ethanol) ≈ 0.5 with x(water) = 0.3991 (η = 0.001659 Pa·s) and x(water) = 0.5989 (η = 0.002115 Pa·s), and reports pure ethanol at 298.15 K as η = 0.001082 Pa·s. No kinematic viscosity data were found for this binary system. The near-equimolar viscosity exceeds that of either pure component, consistent with the well-known viscosity maximum arising from strong ethanol–water hydrogen-bonding interactions on the water-rich side. Eight additional dynamic viscosity blocks for this system were identified across other DOIs and composition variables.

**Answer:**

#### Viscosity Data for Ethanol + Water Binary Mixture near x ≈ 0.5 at 298.15 K

##### Compounds
- **Ethanol** (GLOBcomp_2, C₂H₆O)
- **Water** (GLOBcomp_1, H₂O)

##### Dynamic Viscosity (GLOBprop_4) — Results

Ten binary ethanol+water blocks with dynamic viscosity data were found in the database. Two blocks with the best composition coverage near x = 0.5 at 298.15 K were inspected in detail:

---

###### Block 1: GLOBlit_5201 :: PROPblock_21
**DOI:** 10.1016/j.jct.2018.02.022  
**Pressure constraint:** 92.3 kPa  
**Composition variable:** mole fraction of ethanol

This block contains a near-exact match at x(ethanol) = 0.4989:

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *BLKpoint_id* | *T (K)* | *x(ethanol)* | *P (kPa)* | *η (Pa·s)* |
|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「BLKpoint_35」 | 「298.15」 | 「0.399」 | 「92.3」 | 「0.0021697」 |
| WM_L1#1_Table#1_Row#2 | 「BLKpoint_36」 | 「298.15」 | 「0.4495」 | 「92.3」 | 「0.0020662」 |
| WM_L1#1_Table#1_Row#3 | 「BLKpoint_37」 | 「298.15」 | 「0.4989」 | 「92.3」 | 「0.0019557」 |
| WM_L1#1_Table#1_Row#4 | 「BLKpoint_38」 | 「298.15」 | 「0.5495」 | 「92.3」 | 「0.0018796」 |

**Best match:** At x(ethanol) = 0.4989, the dynamic viscosity is **0.0019557 Pa·s** (≈ 1.96 mPa·s) at 298.15 K. The block has 100 total data points spanning T = 293.15–308.15 K and x(ethanol) = 0–1. The full composition range at 298.15 K spans η = 0.00089689–0.0024286 Pa·s.

---

###### Block 2: GLOBlit_2825 :: PROPblock_11
**DOI:** 10.1016/j.jct.2007.05.004  
**Pressure constraint:** 101.0 kPa  
**Composition variable:** mole fraction of water

No exact x(water) = 0.5 point exists; the nearest bracketing points are:

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *BLKpoint_id* | *T (K)* | *x(water)* | *P (kPa)* | *η (Pa·s)* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「BLKpoint_19」 | 「298.15」 | 「0.3991」 | 「101.0」 | 「0.001659」 |
| WM_L1#1_Table#2_Row#2 | 「BLKpoint_20」 | 「298.15」 | 「0.5989」 | 「101.0」 | 「0.002115」 |

At x(water) = 0.3991 (i.e., x(ethanol) ≈ 0.6), η = 0.001659 Pa·s; at x(water) = 0.5989 (i.e., x(ethanol) ≈ 0.4), η = 0.002115 Pa·s. The block has 37 total data points spanning T = 293.15–303.15 K and x(water) = 0–1.

Additionally, the pure ethanol endpoint from this block at 298.15 K is η = 0.001082 Pa·s (x(water) = 0), and the full 298.15 K isotherm spans η = 0.00089–0.0023 Pa·s.

---

##### Kinematic Viscosity (GLOBprop_40)
No kinematic viscosity data was found for the ethanol + water binary system in the ThermoML database.

##### Chemistry Insight
The viscosity of the ethanol–water mixture at near-equimolar composition is notably higher than either pure component. From GLOBlit_5201::PROPblock_21, the value at x(ethanol) = 0.4989 is 0.0019557 Pa·s (≈ 1.96 mPa·s), while from GLOBlit_2825::PROPblock_11, pure ethanol (x(water) = 0) has η = 0.001082 Pa·s (1.082 mPa·s) at 298.15 K. The pure water endpoint from GLOBlit_2825::PROPblock_11 falls within the reported range of 0.00089–0.0023 Pa·s at 298.15 K.

This well-known viscosity maximum in the ethanol–water system arises from strong hydrogen-bonding interactions between ethanol and water molecules, which create more structured, higher-friction intermolecular networks than exist in either pure liquid. The data from GLOBlit_5201::PROPblock_21 show that the viscosity increases as x(ethanol) decreases from 0.5495 (η = 0.0018796 Pa·s) through 0.4989 (η = 0.0019557 Pa·s) to 0.4495 (η = 0.0020662 Pa·s) and 0.399 (η = 0.0021697 Pa·s), consistent with the known maximum occurring on the water-rich side of the composition range.

##### Additional Blocks Available
Eight other dynamic viscosity blocks for this binary system were identified (from DOIs including 10.1021/acs.jced.7b00299, 10.1021/acs.jced.8b00086, 10.1021/acs.jced.8b00939, 10.1021/je4003515, among others), spanning various composition variables (mass fraction, molality) and temperature ranges overlapping 298.15 K.

**Core claims:**
- At 298.15 K and 92.3 kPa, the dynamic viscosity of the ethanol–water binary mixture at x(ethanol) = 0.4989 is 0.0019557 Pa·s (≈ 1.96 mPa·s), from GLOBlit_5201 :: PROPblock_21 (DOI: 10.1016/j.jct.2018.02.022).
- The viscosity at near-equimolar composition (x(ethanol) ≈ 0.5) is notably higher than that of pure ethanol, which is reported as 0.001082 Pa·s at 298.15 K from GLOBlit_2825 :: PROPblock_11.
- Data from GLOBlit_5201 :: PROPblock_21 show that at 298.15 K, viscosity increases as x(ethanol) decreases from 0.5495 (η = 0.0018796 Pa·s) through 0.4989 (η = 0.0019557 Pa·s) to 0.4495 (η = 0.0020662 Pa·s) and 0.399 (η = 0.0021697 Pa·s), consistent with the known viscosity maximum occurring on the water-rich side of the composition range.
- No kinematic viscosity data was found for the ethanol–water binary system in the ThermoML database.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_5201」 | 「PROPblock_21」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture at 92.3 kPa; mole fraction of ethanol as composition variable; 100 data points spanning T = 293.15–308.15 K and x(ethanol) = 0–1. Best match at x(ethanol) = 0.4989, T = 298.15 K: η = 0.0019557 Pa·s.」 |
| WM_L1#1_Table#4 | 「GLOBlit_2825」 | 「PROPblock_11」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water binary mixture at 101.0 kPa; mole fraction of water as composition variable; 37 data points spanning T = 293.15–303.15 K and x(water) = 0–1. Nearest bracketing points at 298.15 K: x(water) = 0.3991 (η = 0.001659 Pa·s) and x(water) = 0.5989 (η = 0.002115 Pa·s).」 |

*Not stored here: 3 verbatim data_inspections table(s); 4 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: no_results · validation: PASS

**Summary:** Excess viscosity (viscosity deviation, Δη) for ethanol + water is not available as a stored property in ThermoML. The ThermoML schema contains only four excess properties—excess molar enthalpy (GLOBprop_17), excess molar volume (GLOBprop_28), excess molar heat capacity (GLOBprop_85), and excess molar Gibbs energy (GLOBprop_97)—all thermodynamic rather than transport quantities. The only viscosity-related property in the registry is dynamic viscosity (GLOBprop_4, Pa·s). However, Δη can be computed from absolute dynamic viscosity data present in the database: GLOBlit_5201 PROPblock_21 (DOI: 10.1016/j.jct.2018.02.022) reports η = 0.0019557 Pa·s at x(ethanol) = 0.4989 and T = 298.15 K, with the full 298.15 K isotherm spanning η = 0.00089689–0.0024286 Pa·s across 25 compositions at a constraint of 92.3 kPa; GLOBlit_2825 PROPblock_11 (DOI: 10.1016/j.jct.2007.05.004) provides pure ethanol viscosity η = 0.001082 Pa·s at 298.15 K and 101.0 kPa. Pure-component and mixture viscosities are thus available for external calculation of Δη = η_mix − (x₁·η₁° + x₂·η₂°), but ThermoML does not store or report viscosity deviation as a separate measured quantity.

**Answer:**

**Excess Viscosity / Viscosity Deviation Data for Ethanol + Water: Not Available in ThermoML**

A thorough search of the ThermoML property registry confirms that **no excess viscosity, viscosity deviation, or any excess transport property** is catalogued in the database. The ThermoML schema contains only four excess properties, all of which are thermodynamic rather than transport quantities:

**WM_L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *Global ID* | *Property* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「GLOBprop_17」 | 「Excess molar enthalpy (molar enthalpy of mixing), kJ/mol」 |
| WM_L1#2_Table#1_Row#2 | 「GLOBprop_28」 | 「Excess molar volume, m³/mol」 |
| WM_L1#2_Table#1_Row#3 | 「GLOBprop_85」 | 「Excess molar heat capacity, J/K/mol」 |
| WM_L1#2_Table#1_Row#4 | 「GLOBprop_97」 | 「Excess molar Gibbs energy, kJ/mol」 |

Furthermore, the only viscosity-related property in the entire ThermoML registry is **GLOBprop_4 — Viscosity, Pa·s** (dynamic viscosity). There is no dedicated "excess viscosity," "viscosity deviation," or "Δη" property type.

This means that viscosity deviation values for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system **cannot be retrieved directly** from ThermoML. However, they can be **computed** from the absolute dynamic viscosity data already found:

- From **GLOBlit_5201 :: PROPblock_21** (DOI: 10.1016/j.jct.2018.02.022), the dynamic viscosity at x(ethanol) = 0.4989 and T = 298.15 K is **0.0019557 Pa·s**, with the full 298.15 K isotherm spanning η = 0.00089689–0.0024286 Pa·s across x(ethanol) = 0–1 (25 points at that temperature, 100 total in the block). The block constraint is 92.3 kPa.

- From **GLOBlit_2825 :: PROPblock_11** (DOI: 10.1016/j.jct.2007.05.004), pure ethanol at 298.15 K gives η = 0.001082 Pa·s (at x(water) = 0). The block constraint is 101.0 kPa, with 12 points at 298.15 K spanning η = 0.00089–0.0023 Pa·s across x(water) = 0–1.

The viscosity deviation Δη is typically defined as:

Δη = η_mix − (x₁·η₁° + x₂·η₂°)

where η₁° and η₂° are the pure-component viscosities. Since both mixture and pure-component viscosity values are available in the existing blocks, Δη can be derived externally, but ThermoML does not store or report it as a separate measured quantity.

**Core claims:**
- The ThermoML schema contains no excess viscosity, viscosity deviation, or any excess transport property; its only four excess properties are thermodynamic: excess molar enthalpy (GLOBprop_17), excess molar volume (GLOBprop_28), excess molar heat capacity (GLOBprop_85), and excess molar Gibbs energy (GLOBprop_97).
- The only viscosity-related property in the ThermoML registry is GLOBprop_4 — Viscosity, Pa·s (dynamic viscosity); there is no dedicated excess viscosity or viscosity deviation property type.
- Viscosity deviation values for the ethanol + water binary system cannot be retrieved directly from ThermoML, but can be computed from absolute dynamic viscosity data available in the database, since both mixture and pure-component viscosity values exist in catalogued property blocks.

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


