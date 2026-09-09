# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_4 | methanol | methanol |
| comp | GLOBcomp_1 | water | water |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find viscosity data for methanol + water binary mixture at mole fraction ~0.5 and 298.15 K → stored as L1_query_1 · validation: PASS
- [L1] Search for excess viscosity or viscosity deviation data for methanol + water binary mixture near equimolar composition a → stored as L1_query_2 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** From DOI 10.1016/j.jct.2007.05.004 (GLOBlit_2825, PROPblock_9), the dynamic viscosity of the methanol + water binary mixture at the nearest equimolar composition x(water) = 0.5003 is 0.001309 Pa·s (≈ 1.309 mPa·s) at 298.15 K and 101.0 kPa, measured by capillary tube method. The block contains 39 data points spanning T = 293.15–303.15 K and the full mole-fraction range. At 298.15 K, the viscosity at this near-equimolar composition is substantially higher than that of pure methanol (0.000545 Pa·s at x(water) = 0) and continues to increase toward the water-rich side (0.001554 Pa·s at x(water) = 0.6997), reflecting non-ideal behavior attributed to enhanced hydrogen-bonding network formation. Three additional ThermoML blocks (GLOBlit_5533, GLOBlit_8869, GLOBlit_9571) also contain methanol + water viscosity data but were not inspected.

**Answer:**

#### Viscosity Data for Methanol + Water Binary Mixture near x = 0.5 and T = 298.15 K

##### Source
**DOI:** 10.1016/j.jct.2007.05.004 (GLOBlit_2825, PROPblock_9)

This block contains 39 data points of dynamic viscosity (Pa·s) for the methanol (GLOBcomp_4) + water (GLOBcomp_1) binary system, covering T = 293.15–303.15 K and the full mole-fraction range (0–1), measured by capillary tube method at 101.0 kPa.

##### Data at T = 298.15 K near equimolar composition

The block does not contain a row at exactly x(water) = 0.5; the nearest compositions bracket it:

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *temperature (K)* | *x(water)* | *Pressure (kPa)* | *η (Pa·s)* |
|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「298.15」 | 「0.2983」 | 「101.0」 | 「0.000987」 |
| WM_L1#1_Table#1_Row#2 | 「298.15」 | 「0.3985」 | 「101.0」 | 「0.00115」 |
| WM_L1#1_Table#1_Row#3 | 「298.15」 | 「**0.5003**」 | 「101.0」 | 「**0.001309**」 |
| WM_L1#1_Table#1_Row#4 | 「298.15」 | 「0.5994」 | 「101.0」 | 「0.001463」 |
| WM_L1#1_Table#1_Row#5 | 「298.15」 | 「0.6997」 | 「101.0」 | 「0.001554」 |

The closest composition to equimolar is **x(water) = 0.5003**, where the dynamic viscosity is **0.001309 Pa·s** (≈ 1.309 mPa·s) at 298.15 K and 101.0 kPa.

##### Chemistry insight

The viscosity of the methanol–water mixture at near-equimolar composition (0.001309 Pa·s) is notably higher than that of pure methanol at 298.15 K in this dataset: pure methanol (x(water) = 0) shows η = 0.000545 Pa·s. The viscosity continues to increase toward the water-rich side, reaching 0.001554 Pa·s at x(water) = 0.6997. This non-ideal viscosity behavior in methanol–water mixtures is attributed to enhanced hydrogen-bonding network formation between methanol and water molecules at intermediate compositions.

##### Additional blocks found

Three other blocks in the database contain dynamic viscosity data for the methanol + water binary system but were not inspected in this run and have less relevant coverage for the target conditions:

- GLOBlit_5533 (DOI: 10.1016/j.jct.2019.05.013), PROPblock_3
- GLOBlit_8869 (DOI: 10.1021/je0600810), PROPblock_3
- GLOBlit_9571 (DOI: 10.1021/je2003622), PROPblock_1

The primary and most complete data source for the requested conditions is **GLOBlit_2825 :: PROPblock_9**.

**Core claims:**
- In the methanol + water binary system at T = 298.15 K and 101.0 kPa, the dynamic viscosity at the nearest equimolar composition x(water) = 0.5003 is 0.001309 Pa·s, as reported in DOI 10.1016/j.jct.2007.05.004.
- The mixture viscosity at near-equimolar composition (0.001309 Pa·s) is substantially higher than that of pure methanol at 298.15 K (0.000545 Pa·s), and viscosity continues to increase toward the water-rich side, consistent with non-ideal behavior attributed to enhanced hydrogen-bonding network formation.
- Three additional ThermoML blocks containing methanol + water dynamic viscosity data were identified but not inspected; the primary source (GLOBlit_2825, PROPblock_9) covers 39 data points spanning T = 293.15–303.15 K and the full mole-fraction range.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_2825」 | 「PROPblock_9」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity (Pa·s) for methanol + water binary mixture, T = 293.15–303.15 K, full mole-fraction range, 101.0 kPa. Contains data point at x(water) = 0.5003, T = 298.15 K with η = 0.001309 Pa·s.」 |
| WM_L1#1_Table#3 | 「GLOBlit_5533」 | 「PROPblock_3」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity for methanol + water binary mixture (additional block, not inspected in detail).」 |
| WM_L1#1_Table#4 | 「GLOBlit_8869」 | 「PROPblock_3」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity for methanol + water binary mixture (additional block, not inspected in detail).」 |
| WM_L1#1_Table#5 | 「GLOBlit_9571」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity for methanol + water binary mixture (additional block, not inspected in detail).」 |

*Not stored here: 1 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: no_results · validation: PASS

**Summary:** No excess viscosity or viscosity deviation data exists for the methanol + water binary system in the ThermoML database. The ThermoML property registry contains no excess viscosity, viscosity deviation, or any other excess/deviation transport property; the only excess properties available are thermodynamic (excess molar enthalpy, excess molar volume, excess molar heat capacity, excess molar Gibbs energy). No kinematic viscosity data was found for this system either. The sole viscosity property in the registry is dynamic viscosity (GLOBprop_4, in Pa·s), with data identified in sources such as GLOBlit_2825 (PROPblock_9), but no excess or deviation form is stored. To obtain excess or deviation viscosity values, one would need to compute them manually from the available dynamic viscosity data using an appropriate mixing rule.

**Answer:**

###### Excess Viscosity / Viscosity Deviation Data for Methanol + Water: Not Found

A thorough search of the ThermoML database confirms that **no excess viscosity or viscosity deviation data** exists for the methanol + water binary system. The key findings are:

1. **No excess transport properties in the registry:** The ThermoML property registry contains no "excess viscosity," "viscosity deviation," or any other excess/deviation transport property. The only excess properties available are thermodynamic:
   - Excess molar enthalpy (GLOBprop_17)
   - Excess molar volume (GLOBprop_28)
   - Excess molar heat capacity (GLOBprop_85)
   - Excess molar Gibbs energy (GLOBprop_97)

2. **No kinematic viscosity data:** No blocks were found for kinematic viscosity (GLOBprop_40) in the methanol + water binary system.

3. **Only dynamic viscosity available:** The sole viscosity property in the ThermoML registry is dynamic viscosity (GLOBprop_4, in Pa·s). Data for this property in the methanol + water system was previously identified in GLOBlit_2825 (PROPblock_9) and other blocks, but no excess or deviation form of viscosity is stored.

**Implication:** To obtain excess or deviation viscosity values for this system, one would need to compute them manually from the available dynamic viscosity data (GLOBprop_4) using an appropriate mixing rule (e.g., Δη = η_mix − Σ xᵢηᵢ for a simple linear deviation, or logarithmic forms). The ThermoML database does not store pre-computed excess viscosity values.

**Core claims:**
- The ThermoML database contains no excess viscosity or viscosity deviation data for the methanol + water binary system, as the property registry includes no excess or deviation transport properties—only excess thermodynamic properties (excess molar enthalpy, excess molar volume, excess molar heat capacity, excess molar Gibbs energy).
- Dynamic viscosity (GLOBprop_4, in Pa·s) is the only viscosity property available in the ThermoML registry for the methanol + water system; no kinematic viscosity data were found either.
- To obtain excess or deviation viscosity values for methanol + water, one would need to compute them manually from the available dynamic viscosity data using an appropriate mixing rule, as the ThermoML database does not store pre-computed excess viscosity values.

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


