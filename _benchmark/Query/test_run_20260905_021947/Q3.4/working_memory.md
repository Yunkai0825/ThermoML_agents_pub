# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_1 | water | water |
| comp | GLOBcomp_2 | ethanol | ethanol |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find ethanol + water studies reporting multiple measured properties from the same paper → stored as L1_query_1 · validation: FLAGGED(4)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(4)

**Summary:** Six ThermoML papers were identified for the ethanol (GLOBcomp_2, CCO) + water (GLOBcomp_1, O) binary system and ranked by number of distinct measured properties. GLOBlit_3971 (DOI: 10.1016/j.jct.2013.08.020) leads with 4 distinct properties: boiling temperature (GLOBprop_14, PROPblock_9, 16 points), vapor-phase mole fraction (GLOBprop_2, PROPblock_10), azeotropic temperature (GLOBprop_58, PROPblock_11), and azeotropic composition (GLOBprop_45, PROPblock_12), totaling 34 data points of isobaric VLE at 101.3 kPa. Inspected PROPblock_9 data show boiling temperatures from 351.33 K (near x_ethanol = 0.9) to 373.15 K (pure water), consistent with the known ethanol–water positive azeotrope. GLOBlit_5201 (DOI: 10.1016/j.jct.2018.02.022) follows with 3 properties (mass density GLOBprop_1, speed of sound GLOBprop_8, viscosity GLOBprop_4) and 496 total data points. GLOBlit_7178 (DOI: 10.1021/acs.jced.7b00299) reports 3 properties (density, viscosity, refractive index GLOBprop_7) with 5 points. GLOBlit_7448 (DOI: 10.1021/acs.jced.8b00086) reports 3 properties (density, viscosity, surface tension GLOBprop_13) with 18 points at 298.2 K and 100.0 kPa. GLOBlit_2732 (DOI: 10.1016/j.jct.2006.08.002) reports 2 properties (vapor pressure GLOBprop_5, density) with 326 points. GLOBlit_299 (DOI: 10.1016/j.fluid.2005.08.018) reports 1 property (activity coefficient) with 13 points. Only PROPblock_9 was directly inspected; data for other blocks are flagged as unverified.

**Answer:**

#### Ethanol + Water Binary System: Papers Ranked by Number of Distinct Measured Properties

**Component IDs:**
- Ethanol: **GLOBcomp_2** (C₂H₆O, SMILES: CCO)
- Water: **GLOBcomp_1** (H₂O, SMILES: O)

##### Ranking by Distinct Properties (Descending)

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Rank* | *Literature ID* | *DOI* | *Distinct Properties* | *Property List* | *Total Data Points* |
|---|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「1」 | 「GLOBlit_3971」 | 「10.1016/j.jct.2013.08.020」 | 「**4**」 | 「Boiling temperature (GLOBprop_14), Mole fraction (GLOBprop_2), Azeotropic temperature (GLOBprop_58), Azeotropic composition (GLOBprop_45)」 | 「34」 |
| WM_L1#1_Table#1_Row#2 | 「2」 | 「GLOBlit_5201」 | 「10.1016/j.jct.2018.02.022」 | 「**3**」 | 「Mass density (GLOBprop_1), Speed of sound (GLOBprop_8), Viscosity (GLOBprop_4)」 | 「496」 |
| WM_L1#1_Table#1_Row#3 | 「3」 | 「GLOBlit_7178」 | 「10.1021/acs.jced.7b00299」 | 「**3**」 | 「Mass density (GLOBprop_1), Viscosity (GLOBprop_4), Refractive index (GLOBprop_7)」 | 「5」 |
| WM_L1#1_Table#1_Row#4 | 「4」 | 「GLOBlit_7448」 | 「10.1021/acs.jced.8b00086」 | 「**3**」 | 「Mass density (GLOBprop_1), Viscosity (GLOBprop_4), Surface tension (GLOBprop_13)」 | 「18」 |
| WM_L1#1_Table#1_Row#5 | 「5」 | 「GLOBlit_2732」 | 「10.1016/j.jct.2006.08.002」 | 「**2**」 | 「Vapor/sublimation pressure (GLOBprop_5), Mass density (GLOBprop_1)」 | 「326」 |
| WM_L1#1_Table#1_Row#6 | 「6」 | 「GLOBlit_299」 | 「10.1016/j.fluid.2005.08.018」 | 「**1**」 | 「Activity coefficient (3 blocks)」 | 「13」 |

##### Best Candidate for Cross-Checking

**GLOBlit_3971** (DOI: 10.1016/j.jct.2013.08.020) reports the **largest number of distinct measured properties (4)** for the ethanol + water binary system. All four blocks are isobaric VLE data at 101.3 kPa:

- **PROPblock_9:** Boiling temperature — 16 data points. Inspected data confirms boiling temperature ranges from 351.33 K (at x_ethanol = 0.899) to 373.15 K (pure water, x_ethanol = 0), showing the characteristic non-monotonic curve with an azeotropic minimum. The minimum observed boiling temperature of 351.33 K occurs near x_ethanol = 0.9, and pure ethanol boils at 351.45 K — consistent with the well-known ethanol–water positive azeotrope.
- **PROPblock_10:** Vapor-phase mole fraction of ethanol — not inspected in this run; block metadata from search indicates it contains data points at the same conditions.
- **PROPblock_11:** Azeotropic temperature — not inspected in this run; block metadata from search indicates 1 data point.
- **PROPblock_12:** Azeotropic mole fraction of ethanol — not inspected in this run; block metadata from search indicates 1 data point.

##### Notable Alternatives

**GLOBlit_5201** (DOI: 10.1016/j.jct.2018.02.022) is a strong alternative for data-rich cross-checking. Per the search_blocks result, it contains 3 distinct transport/volumetric properties (mass density: 244 pts in PROPblock_19; speed of sound: 152 pts in PROPblock_20; viscosity: 100 pts in PROPblock_21) with 496 total data points. The search result reported composition ranges of x_ethanol ≈ 0.0024–0.9895, temperature 293.15–303.15 K (density, speed of sound) or 293.15–303.15 K (viscosity), and pressure 92.3 kPa. (These values are from the search_blocks tool result for GLOBlit_5201, not from a block inspection.)

**GLOBlit_7448** (DOI: 10.1021/acs.jced.8b00086) is also notable: per the search_blocks result, its three properties (density, viscosity, surface tension) are all measured at 298.2 K and 100.0 kPa as a function of water mass fraction (range 0.206–0.508), enabling direct property-to-property comparison at identical state points. (These values are from the search_blocks tool result for GLOBlit_7448, not from a block inspection.)

**Core claims:**
- Six ThermoML papers were identified for the ethanol (CCO) + water (O) binary system, and GLOBlit_3971 (DOI: 10.1016/j.jct.2013.08.020) reports the largest number of distinct measured properties (4): boiling temperature, vapor-phase mole fraction, azeotropic temperature, and azeotropic mole fraction, all at 101.3 kPa.
- Verified inspection of PROPblock_9 in GLOBlit_3971 confirms boiling temperatures ranging from 351.33 K (near x_ethanol = 0.9) to 373.15 K (pure water), consistent with the well-known ethanol–water positive azeotrope; the minimum observed boiling temperature of 351.33 K occurs near x_ethanol = 0.9, and pure ethanol boils at 351.45 K.
- GLOBlit_5201 (DOI: 10.1016/j.jct.2018.02.022) is a data-rich alternative with 3 distinct properties (mass density, speed of sound, viscosity) and 496 total data points, but its block-level data values were not directly inspected and remain unverified.
- GLOBlit_7448 (DOI: 10.1021/acs.jced.8b00086) reports 3 properties (density, viscosity, surface tension) at 298.2 K and 100.0 kPa, but its block-level data were also not inspected and remain unverified.
- Multiple blocks (PROPblock_12, PROPblock_19, PROPblock_20, PROPblock_21) were quoted with specific data values but were never inspected, so those quoted values carry unresolved UNVERIFIED flags.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_3971」 | 「PROPblock_9」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_14」 | 「Boiling temperature for ethanol + water binary system at 101.3 kPa.」 |
| WM_L1#1_Table#3 | 「GLOBlit_3971」 | 「PROPblock_10」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_2」 | 「Vapor-phase mole fraction of ethanol for ethanol + water binary system at 101.3 kPa.」 |
| WM_L1#1_Table#4 | 「GLOBlit_3971」 | 「PROPblock_11」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_58」 | 「Azeotropic temperature for ethanol + water binary system.」 |
| WM_L1#1_Table#5 | 「GLOBlit_3971」 | 「PROPblock_12」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_45」 | 「Azeotropic mole fraction of ethanol for ethanol + water binary system.」 |
| WM_L1#1_Table#6 | 「GLOBlit_5201」 | 「PROPblock_19」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density for ethanol + water binary system.」 |
| WM_L1#1_Table#7 | 「GLOBlit_5201」 | 「PROPblock_20」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_8」 | 「Speed of sound for ethanol + water binary system.」 |
| WM_L1#1_Table#8 | 「GLOBlit_5201」 | 「PROPblock_21」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Viscosity for ethanol + water binary system.」 |

*Not stored here: 1 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(4) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_12: PROPblock_12 is quoted with data values (244, …) but was never inspected in this run
- **UNINSPECTED_BLOCK** PROPblock_19: PROPblock_19 is quoted with data values (152, …) but was never inspected in this run
- **UNINSPECTED_BLOCK** PROPblock_20: PROPblock_20 is quoted with data values (100, …) but was never inspected in this run
- **UNINSPECTED_BLOCK** PROPblock_21: PROPblock_21 is quoted with data values (496, 0.0024, 0.9895, 293.15, …) but was never inspected in this run


