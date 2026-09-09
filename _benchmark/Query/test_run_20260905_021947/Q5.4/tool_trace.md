# Q5.4 — Tool Trace

**Prompt:** I'm looking for heat capacity data for butanol.

**Summary:** 380.2s  |  2 iterations  |  1 tools

---

### Step 1: `L1_query`
- **Args:** `{"context": "...", "id_catalog": "...", "instruction": "...", "purpose": "..."}`
- **Result size:** 27,007 chars
- **Elapsed:** 278.4s

---

## Working Memory (final snapshot)

# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_7 | butan-1-ol | butan-1-ol |
| comp | GLOBcomp_20 | butan-2-ol | butan-2-ol |
| comp | GLOBcomp_29 | 2-methyl-1-propanol | 2-methyl-1-propanol |
| comp | GLOBcomp_44 | 2-methylpropan-2-ol | 2-methylpropan-2-ol |
| prop | GLOBprop_9 | molar_heat_capacity_at_constant_pressure_j_k_mol | Molar heat capacity at constant pressure, J/K/mol |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find heat capacity (molar Cp) data for butanol in the ThermoML database → stored as L1_query_1 · validation: FLAGGED(2)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(2)

**Summary:** ThermoML contains molar heat capacity (Cp) data for three of the four butanol isomers; no data was found for tert-butanol (2-methylpropan-2-ol). 1-Butanol (butan-1-ol) is the most extensively covered with 16 data blocks spanning ~273–353 K and pressures up to 25,000 kPa. Representative liquid-phase values at 101.3 kPa (from DOI 10.1016/j.jct.2004.09.007) range from 168.64 J·K⁻¹·mol⁻¹ at 285.15 K to 222.81 J·K⁻¹·mol⁻¹ at 353.15 K, increasing monotonically. 2-Butanol (butan-2-ol) has 5 data blocks; inspected data (from DOI 10.1016/j.jct.2017.03.006) show Cp values of 189.1 J·K⁻¹·mol⁻¹ at 293.15 K and 100 kPa decreasing to 182.7 J·K⁻¹·mol⁻¹ at 25,000 kPa, and 214.9 J·K⁻¹·mol⁻¹ at 313.15 K and 100 kPa decreasing to 204.9 J·K⁻¹·mol⁻¹ at 25,000 kPa. Isobutanol (2-methyl-1-propanol) has only 1 data block (from DOI 10.1021/je049738c) with a single liquid-phase data point near 298 K, but specific numerical values were not inspected and cannot be quoted. At 293.15 K and atmospheric pressure, 2-butanol (189.1 J·K⁻¹·mol⁻¹) has a notably higher Cp than 1-butanol (173.56 J·K⁻¹·mol⁻¹), attributed to differences in branching and hydroxyl group position affecting hydrogen bonding and rotational degrees of freedom.

**Answer:**

#### Molar Heat Capacity (Cp) Data for Butanol Isomers in ThermoML

The ThermoML database contains molar heat capacity at constant pressure (Cp) data for three of the four butanol isomers. No data was found for tert-butanol (2-methylpropan-2-ol).

---

##### 1. **1-Butanol (butan-1-ol, GLOBcomp_7)**

The most extensively covered isomer, with **16 data blocks** (7 pure-component, 9 binary mixtures), all in the liquid phase. Temperature coverage spans approximately 273–353 K, with pressures from atmospheric up to 25,000 kPa.

**Representative data** (from GLOBlit_2451 :: PROPblock_2, DOI: 10.1016/j.jct.2004.09.007, atmospheric pressure at 101.3 kPa, liquid phase, 29 total data points):

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *T (K)* | *Cp (J·K⁻¹·mol⁻¹)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「285.15」 | 「168.64」 |
| WM_L1#1_Table#1_Row#2 | 「293.15」 | 「173.56」 |
| WM_L1#1_Table#1_Row#3 | 「300.65」 | 「178.53」 |
| WM_L1#1_Table#1_Row#4 | 「313.15」 | 「187.99」 |
| WM_L1#1_Table#1_Row#5 | 「328.15」 | 「200.45」 |
| WM_L1#1_Table#1_Row#6 | 「338.15」 | 「209.17」 |
| WM_L1#1_Table#1_Row#7 | 「343.15」 | 「213.82」 |
| WM_L1#1_Table#1_Row#8 | 「348.15」 | 「218.32」 |
| WM_L1#1_Table#1_Row#9 | 「353.15」 | 「222.81」 |

The Cp of liquid 1-butanol increases monotonically with temperature in a near-linear fashion (R² = 0.9966), rising from 168.64 J·K⁻¹·mol⁻¹ at 285.15 K to 222.81 J·K⁻¹·mol⁻¹ at 353.15 K. This steady increase reflects the growing contribution of intermolecular hydrogen-bonding disruption and increased molecular motion with temperature.

---

##### 2. **2-Butanol (butan-2-ol, GLOBcomp_20)**

**5 data blocks** found (3 pure-component, 2 binary mixtures), liquid phase.

**Inspected data** (from GLOBlit_4977 :: PROPblock_3, DOI: 10.1016/j.jct.2017.03.006, 12 data points across a T×P grid):

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *T (K)* | *P (kPa)* | *Cp (J·K⁻¹·mol⁻¹)* |
|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「293.15」 | 「100」 | 「189.1」 |
| WM_L1#1_Table#2_Row#2 | 「293.15」 | 「5000」 | 「187.1」 |
| WM_L1#1_Table#2_Row#3 | 「293.15」 | 「10000」 | 「185.5」 |
| WM_L1#1_Table#2_Row#4 | 「293.15」 | 「15000」 | 「185.2」 |
| WM_L1#1_Table#2_Row#5 | 「293.15」 | 「20000」 | 「183.6」 |
| WM_L1#1_Table#2_Row#6 | 「293.15」 | 「25000」 | 「182.7」 |
| WM_L1#1_Table#2_Row#7 | 「313.15」 | 「100」 | 「214.9」 |
| WM_L1#1_Table#2_Row#8 | 「313.15」 | 「5000」 | 「213.1」 |
| WM_L1#1_Table#2_Row#9 | 「313.15」 | 「10000」 | 「211.1」 |
| WM_L1#1_Table#2_Row#10 | 「313.15」 | 「15000」 | 「209.4」 |
| WM_L1#1_Table#2_Row#11 | 「313.15」 | 「20000」 | 「207.2」 |
| WM_L1#1_Table#2_Row#12 | 「313.15」 | 「25000」 | 「204.9」 |

Cp decreases at higher pressures (e.g., 189.1 → 182.7 J·K⁻¹·mol⁻¹ at 293.15 K going from 100 to 25,000 kPa), consistent with compression reducing the configurational contribution to heat capacity. The overall range is 182.7–214.9 J·K⁻¹·mol⁻¹.

---

##### 3. **Isobutanol (2-methyl-1-propanol, GLOBcomp_29)**

Only **1 data block** found (GLOBlit_8447 :: PROPblock_9, DOI: 10.1021/je049738c), containing a single liquid-phase data point measured by flow calorimetry. This block was not inspected in this run, so specific numerical values cannot be quoted. The search summary indicated one data point near 298 K at atmospheric pressure.

---

##### 4. **tert-Butanol (2-methylpropan-2-ol, GLOBcomp_44)**

**No molar heat capacity data found** in the ThermoML database for this isomer.

---

##### Summary Comparison at ~293 K (atmospheric pressure)

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *Isomer* | *Cp at 293.15 K (J·K⁻¹·mol⁻¹)* | *Source* |
|---|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「1-Butanol」 | 「173.56」 | 「GLOBlit_2451, PROPblock_2」 |
| WM_L1#1_Table#3_Row#2 | 「2-Butanol」 | 「189.1」 | 「GLOBlit_4977, PROPblock_3」 |
| WM_L1#1_Table#3_Row#3 | 「Isobutanol」 | 「Not inspected in this run」 | 「GLOBlit_8447, PROPblock_9」 |
| WM_L1#1_Table#3_Row#4 | 「tert-Butanol」 | 「Not available」 | 「—」 |

Among the two isomers with inspected data at 293.15 K, 2-butanol (189.1 J·K⁻¹·mol⁻¹) shows a notably higher Cp than 1-butanol (173.56 J·K⁻¹·mol⁻¹). The branching pattern and hydroxyl group position influence hydrogen bonding networks and rotational degrees of freedom, contributing to these differences.

**Core claims:**
- ThermoML contains molar heat capacity (Cp) data for three of the four butanol isomers (1-butanol, 2-butanol, and isobutanol); no Cp data were found for tert-butanol.
- Liquid 1-butanol Cp increases monotonically with temperature from 168.64 J·K⁻¹·mol⁻¹ at 285.15 K to 222.81 J·K⁻¹·mol⁻¹ at 353.15 K at atmospheric pressure (101.3 kPa), based on verified data from GLOBlit_2451 :: PROPblock_2.
- Liquid 2-butanol Cp decreases with increasing pressure at fixed temperature (e.g., 189.1 → 182.7 J·K⁻¹·mol⁻¹ at 293.15 K from 100 to 25,000 kPa) and increases with temperature (overall range 182.7–214.9 J·K⁻¹·mol⁻¹), based on verified data from GLOBlit_4977 :: PROPblock_3.
- At 293.15 K and atmospheric pressure, 2-butanol has a higher Cp (189.1 J·K⁻¹·mol⁻¹) than 1-butanol (173.56 J·K⁻¹·mol⁻¹), based on the two inspected data blocks.
- Isobutanol Cp data (GLOBlit_8447 :: PROPblock_9) were identified but not inspected; no specific numerical values for isobutanol can be confirmed.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_2451」 | 「PROPblock_2」 | 「GLOBcomp_7」 | 「GLOBprop_9」 | 「Molar heat capacity at constant pressure for liquid 1-butanol at atmospheric pressure (101.3 kPa), 285.15–353.15 K, 29 data points.」 |
| WM_L1#1_Table#5 | 「GLOBlit_4977」 | 「PROPblock_3」 | 「GLOBcomp_20」 | 「GLOBprop_9」 | 「Molar heat capacity at constant pressure for liquid 2-butanol across a T×P grid (293.15–313.15 K, 100–25000 kPa), 12 data points.」 |
| WM_L1#1_Table#6 | 「GLOBlit_8447」 | 「PROPblock_9」 | 「GLOBcomp_29」 | 「GLOBprop_9」 | 「Molar heat capacity at constant pressure for liquid isobutanol (2-methyl-1-propanol); single data point near 298 K at atmospheric pressure.」 |

*Not stored here: 2 verbatim data_inspections table(s); 5 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** GLOBlit_8447::PROPblock_9: GLOBlit_8447::PROPblock_9 is quoted with data values (298, 293, …) but was never inspected in this run (values 298 verified against the database — inspection is still mandatory)
- **UNINSPECTED_BLOCK** PROPblock_9: PROPblock_9 is quoted with data values (293.15, 189.1, 173.56, …) but was never inspected in this run

---

**Total:** 1 tool calls  |  380.2s  |  OK
