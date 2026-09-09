# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_102 | butane | butane |
| comp | GLOBcomp_284 | 2,6,10,15,19,23-hexamethyltetracosane | 2,6,10,15,19,23-hexamethyltetracosane |
| comp | GLOBcomp_12 | hexane | hexane |
| comp | GLOBcomp_17 | octane | octane |
| comp | GLOBcomp_131 | 1-chlorobutane | 1-chlorobutane |
| comp | GLOBcomp_52 | diisopropyl_ether | diisopropyl ether |
| comp | GLOBcomp_307 | 2-chlorobutane | 2-chlorobutane |
| comp | GLOBcomp_361 | 1-chloro-2-methylpropane | 1-chloro-2-methylpropane |
| comp | GLOBcomp_328 | 2-chloro-2-methylpropane | 2-chloro-2-methylpropane |
| comp | GLOBcomp_7 | butan-1-ol | butan-1-ol |
| comp | GLOBcomp_247 | 2,5,8,11,14-pentaoxapentadecane | 2,5,8,11,14-pentaoxapentadecane |
| prop | GLOBprop_1 | mass_density_kg_m3 | Mass density, kg/m3 |
| prop | GLOBprop_4 | viscosity_pa_s | Viscosity, Pa*s |
| prop | GLOBprop_7 | refractive_index_na_dline | Refractive index (Na D-line) |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|
| lit | GLOBlit_25 | 2006-kum-tom-0 | 10.1007/s10765-006-0053-2 |
| lit | GLOBlit_97 | 2010-mon-gue-0 | 10.1007/s10765-010-0737-5 |
| lit | GLOBlit_151 | 2013-ziv-ser-0 | 10.1007/s10765-013-1469-0 |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find binary liquid mixtures where both mass density and dynamic viscosity are measured in the same dataset/paper → stored as L1_query_1 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(1)

**Summary:** Three ThermoML literature sources were identified as containing both mass density and dynamic viscosity co-measured for binary liquid mixtures, totaling 8 distinct binary systems. GLOBlit_25 (DOI 10.1007/s10765-006-0053-2) covers 3 alkane + squalane systems (butane, hexane, and octane each with squalane) with high-pressure data. GLOBlit_97 (DOI 10.1007/s10765-010-0737-5) covers 4 chlorobutane isomer + diisopropyl ether systems (1-chlorobutane, 2-chlorobutane, 1-chloro-2-methylpropane, and 2-chloro-2-methylpropane each with diisopropyl ether), providing a systematic isomer series. GLOBlit_151 (DOI 10.1007/s10765-013-1469-0) covers 1 system of butan-1-ol + TEGDME (2,5,8,11,14-pentaoxapentadecane) with three co-measured properties (density, viscosity, and refractive index). Exact temperature, pressure, and composition ranges for each data block were not independently verified via block-table inspection and should be confirmed before use.

**Answer:**

#### Binary Liquid Mixtures with Co-Measured Mass Density and Dynamic Viscosity

Three literature sources in the ThermoML database were confirmed to contain **both mass density (GLOBprop_1) and dynamic viscosity (GLOBprop_4)** measured for binary liquid systems. These are suitable candidates for jointly testing density and viscosity predictions.

---

##### 1. Alkanes + Squalane — GLOBlit_25
**DOI:** 10.1007/s10765-006-0053-2

Three binary sub-systems, each with paired density and viscosity blocks at high pressure. The following block-level summaries were returned by the `search_blocks` tool but individual block data tables were not inspected in this run, so exact numerical ranges should be verified by inspecting each block before use:

**WM_L1_Q1_Table#1_(Query_L1_Q1_Answer):**

| *row_id* | *System* | *Viscosity Block* | *Density Block* |
|---|---|---|---|
| WM_L1_Q1_Table#1_Row#1 | 「Butane (GLOBcomp_102) + squalane (GLOBcomp_284)」 | 「PROPblock_9」 | 「PROPblock_10」 |
| WM_L1_Q1_Table#1_Row#2 | 「Hexane (GLOBcomp_12) + squalane (GLOBcomp_284)」 | 「PROPblock_11」 | 「PROPblock_12」 |
| WM_L1_Q1_Table#1_Row#3 | 「Octane (GLOBcomp_17) + squalane (GLOBcomp_284)」 | 「PROPblock_13」 | 「PROPblock_14」 |

**Note:** The search_blocks result reported these blocks span temperature, pressure, and composition ranges, but the exact values were not verified via `inspect_block_table` in this run. Squalane is a common viscosity reference fluid, making these data useful for equation-of-state and transport-property model validation.

---

##### 2. Diisopropyl Ether + Chlorobutane Isomers — GLOBlit_97
**DOI:** 10.1007/s10765-010-0737-5

Four binary systems with paired density and viscosity blocks. Block-level summaries were returned by `search_blocks` but individual data tables were not inspected in this run:

**WM_L1_Q1_Table#2_(Query_L1_Q1_Answer):**

| *row_id* | *System* | *Viscosity Block* | *Density Block* |
|---|---|---|---|
| WM_L1_Q1_Table#2_Row#1 | 「1-Chlorobutane (GLOBcomp_131) + diisopropyl ether (GLOBcomp_52)」 | 「PROPblock_11」 | 「PROPblock_12」 |
| WM_L1_Q1_Table#2_Row#2 | 「2-Chlorobutane (GLOBcomp_307) + diisopropyl ether (GLOBcomp_52)」 | 「PROPblock_13」 | 「PROPblock_14」 |
| WM_L1_Q1_Table#2_Row#3 | 「1-Chloro-2-methylpropane (GLOBcomp_361) + diisopropyl ether (GLOBcomp_52)」 | 「PROPblock_15」 | 「PROPblock_16」 |
| WM_L1_Q1_Table#2_Row#4 | 「2-Chloro-2-methylpropane (GLOBcomp_328) + diisopropyl ether (GLOBcomp_52)」 | 「PROPblock_17」 | 「PROPblock_18」 |

**Chemistry note:** This set of structural isomers (1-chlorobutane, 2-chlorobutane, isobutyl chloride, tert-butyl chloride) with a common second component provides a systematic way to study the effect of branching and chlorine position on both density and viscosity of binary mixtures.

---

##### 3. Butan-1-ol + TEGDME — GLOBlit_151
**DOI:** 10.1007/s10765-013-1469-0

One binary system with density, viscosity, and refractive index all co-measured. Block-level summaries were returned by `search_blocks` but individual data tables were not inspected in this run:

**WM_L1_Q1_Table#3_(Query_L1_Q1_Answer):**

| *row_id* | *Property* | *Block* |
|---|---|---|
| WM_L1_Q1_Table#3_Row#1 | 「Mass density (GLOBprop_1)」 | 「PROPblock_7」 |
| WM_L1_Q1_Table#3_Row#2 | 「Dynamic viscosity (GLOBprop_4)」 | 「PROPblock_8」 |
| WM_L1_Q1_Table#3_Row#3 | 「Refractive index (GLOBprop_7)」 | 「PROPblock_9」 |

**Compounds:** butan-1-ol (GLOBcomp_7), 2,5,8,11,14-pentaoxapentadecane / TEGDME (GLOBcomp_247).

**Chemistry note:** The alcohol + polyether system exhibits hydrogen-bonding interactions that produce non-ideal mixing behavior in both density and viscosity, making it a stringent test for predictive models. Additionally, having three co-measured properties (density, viscosity, refractive index) in the same dataset adds further value for multi-property model validation.

---

##### Summary

**WM_L1_Q1_Table#4_(Query_L1_Q1_Answer):**

| *row_id* | *Literature* | *DOI* | *# Binary Systems* | *Key Chemistry* |
|---|---|---|---|---|
| WM_L1_Q1_Table#4_Row#1 | 「GLOBlit_25」 | 「10.1007/s10765-006-0053-2」 | 「3 (alkane + squalane)」 | 「Non-polar hydrocarbon mixtures, high-pressure data」 |
| WM_L1_Q1_Table#4_Row#2 | 「GLOBlit_97」 | 「10.1007/s10765-010-0737-5」 | 「4 (chlorobutane isomers + diisopropyl ether)」 | 「Isomer series, atmospheric pressure」 |
| WM_L1_Q1_Table#4_Row#3 | 「GLOBlit_151」 | 「10.1007/s10765-013-1469-0」 | 「1 (butan-1-ol + TEGDME)」 | 「H-bonding system, three co-measured properties」 |

In total, **8 distinct binary liquid systems** across these three literature sources have both mass density and dynamic viscosity co-measured. The exact temperature, pressure, and composition ranges for each block were reported by the registry search tool but were not independently verified via block-table inspection in this run; users should inspect individual blocks (e.g., `GLOBlit_25::PROPblock_9`) to confirm precise data ranges before use.

**Additional literature sources checked but found to contain only one property:**
- GLOBlit_8 (ethanol + toluene): viscosity only
- GLOBlit_59 (ethanol + BMIMBF₄): density only
- GLOBlit_145 (chlorobutane isomers + ethers): viscosity only

**Core claims:**
- Three ThermoML literature sources (GLOBlit_25, GLOBlit_97, GLOBlit_151) were identified as containing both mass density and dynamic viscosity co-measured for binary liquid systems, encompassing 8 distinct binary systems in total.
- GLOBlit_25 (DOI 10.1007/s10765-006-0053-2) covers three alkane + squalane binary systems (butane, hexane, octane each paired with squalane) with high-pressure density and viscosity data.
- GLOBlit_97 (DOI 10.1007/s10765-010-0737-5) covers four chlorobutane isomer + diisopropyl ether binary systems, providing a systematic series for studying branching and chlorine-position effects on density and viscosity.
- GLOBlit_151 (DOI 10.1007/s10765-013-1469-0) covers one butan-1-ol + TEGDME binary system with three co-measured properties: mass density, dynamic viscosity, and refractive index.
- Exact temperature, pressure, and composition ranges for the identified data blocks were not independently verified via block-table inspection in this run; the answer flags this as an unresolved limitation requiring further verification before use.

**Core blocks found:**

**WM_L1_Q1_Blocks_(Query_L1_Q1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1_Q1_Table#5 | 「GLOBlit_25」 | 「PROPblock_9」 | 「GLOBcomp_102, GLOBcomp_284」 | 「GLOBprop_4」 | 「Dynamic viscosity for butane + squalane.」 |
| WM_L1_Q1_Table#6 | 「GLOBlit_25」 | 「PROPblock_10」 | 「GLOBcomp_102, GLOBcomp_284」 | 「GLOBprop_1」 | 「Mass density for butane + squalane.」 |
| WM_L1_Q1_Table#7 | 「GLOBlit_25」 | 「PROPblock_11」 | 「GLOBcomp_12, GLOBcomp_284」 | 「GLOBprop_4」 | 「Dynamic viscosity for hexane + squalane.」 |
| WM_L1_Q1_Table#8 | 「GLOBlit_25」 | 「PROPblock_12」 | 「GLOBcomp_12, GLOBcomp_284」 | 「GLOBprop_1」 | 「Mass density for hexane + squalane.」 |
| WM_L1_Q1_Table#9 | 「GLOBlit_25」 | 「PROPblock_13」 | 「GLOBcomp_284, GLOBcomp_17」 | 「GLOBprop_4」 | 「Dynamic viscosity for octane + squalane.」 |
| WM_L1_Q1_Table#10 | 「GLOBlit_25」 | 「PROPblock_14」 | 「GLOBcomp_284, GLOBcomp_17」 | 「GLOBprop_1」 | 「Mass density for octane + squalane.」 |
| WM_L1_Q1_Table#11 | 「GLOBlit_97」 | 「PROPblock_11」 | 「GLOBcomp_52, GLOBcomp_131」 | 「GLOBprop_4」 | 「Dynamic viscosity for 1-chlorobutane + diisopropyl ether.」 |
| WM_L1_Q1_Table#12 | 「GLOBlit_97」 | 「PROPblock_12」 | 「GLOBcomp_52, GLOBcomp_131」 | 「GLOBprop_1」 | 「Mass density for 1-chlorobutane + diisopropyl ether.」 |
| WM_L1_Q1_Table#13 | 「GLOBlit_97」 | 「PROPblock_13」 | 「GLOBcomp_307, GLOBcomp_52」 | 「GLOBprop_4」 | 「Dynamic viscosity for 2-chlorobutane + diisopropyl ether.」 |
| WM_L1_Q1_Table#14 | 「GLOBlit_97」 | 「PROPblock_14」 | 「GLOBcomp_307, GLOBcomp_52」 | 「GLOBprop_1」 | 「Mass density for 2-chlorobutane + diisopropyl ether.」 |
| WM_L1_Q1_Table#15 | 「GLOBlit_97」 | 「PROPblock_15」 | 「GLOBcomp_52, GLOBcomp_361」 | 「GLOBprop_4」 | 「Dynamic viscosity for 1-chloro-2-methylpropane + diisopropyl ether.」 |
| WM_L1_Q1_Table#16 | 「GLOBlit_97」 | 「PROPblock_16」 | 「GLOBcomp_52, GLOBcomp_361」 | 「GLOBprop_1」 | 「Mass density for 1-chloro-2-methylpropane + diisopropyl ether.」 |
| WM_L1_Q1_Table#17 | 「GLOBlit_97」 | 「PROPblock_17」 | 「GLOBcomp_52, GLOBcomp_328」 | 「GLOBprop_4」 | 「Dynamic viscosity for 2-chloro-2-methylpropane + diisopropyl ether.」 |
| WM_L1_Q1_Table#18 | 「GLOBlit_97」 | 「PROPblock_18」 | 「GLOBcomp_52, GLOBcomp_328」 | 「GLOBprop_1」 | 「Mass density for 2-chloro-2-methylpropane + diisopropyl ether.」 |
| WM_L1_Q1_Table#19 | 「GLOBlit_151」 | 「PROPblock_7」 | 「GLOBcomp_7, GLOBcomp_247」 | 「GLOBprop_1」 | 「Mass density for butan-1-ol + TEGDME.」 |
| WM_L1_Q1_Table#20 | 「GLOBlit_151」 | 「PROPblock_8」 | 「GLOBcomp_7, GLOBcomp_247」 | 「GLOBprop_4」 | 「Dynamic viscosity for butan-1-ol + TEGDME.」 |
| WM_L1_Q1_Table#21 | 「GLOBlit_151」 | 「PROPblock_9」 | 「GLOBcomp_7, GLOBcomp_247」 | 「GLOBprop_7」 | 「Refractive index for butan-1-ol + TEGDME.」 |

*Not stored here: 17 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_9: PROPblock_9 is quoted with data values (14, …) but was never inspected in this run (values 14 verified against the database — inspection is still mandatory)


