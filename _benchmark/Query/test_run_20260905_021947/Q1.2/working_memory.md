# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| comp | GLOBcomp_12 | hexane | hexane |
| comp | GLOBcomp_2 | ethanol | ethanol |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find all thermophysical properties measured for an equimolar liquid mixture of hexane + ethanol near 25 °C → stored as L1_query_1 · validation: FLAGGED(2)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(2)

**Summary:** Seven distinct thermophysical properties were identified in ThermoML for the hexane + ethanol binary liquid mixture near 298.15 K, drawn from 9 data blocks across 3 literature sources: excess molar enthalpy (H_E), excess molar volume (V_E), refractive index (n_D), speed of sound (u), mass density (ρ), surface tension (γ), and viscosity (η). Near equimolar composition (x_ethanol ≈ 0.5) at 298.15 K, representative verified values include: H_E ≈ 0.5637 kJ/mol (x = 0.49) and 0.5564 kJ/mol (x = 0.5191); V_E ≈ 4.12×10⁻⁷ m³/mol (x = 0.4524) and 4.08×10⁻⁷ m³/mol (x = 0.4995); refractive index 1.36652 (x = 0.4999); speed of sound 1073 m/s (x = 0.4999); mass density 692.1 kg/m³ (x = 0.4999). Positive H_E and V_E reflect the endothermic disruption of ethanol hydrogen bonding upon mixing with non-polar hexane, with maxima near equimolar composition. Surface tension, viscosity, and a second density source were identified but their specific data values were not inspected and remain unverified.

**Answer:**

#### Thermophysical Properties of the Hexane + Ethanol Binary Liquid Mixture near 25 °C

A search of the ThermoML database for the binary system **hexane (GLOBcomp_12, C₆H₁₄)** + **ethanol (GLOBcomp_2, C₂H₆O)** in the liquid phase near 298.15 K returned **7 distinct thermophysical properties** across **9 data blocks** from **3 literature sources**.

---

##### Summary of All Distinct Properties Found

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *#* | *Property* | *GLOBprop* | *Literature (GLOBlit)* | *DOI* | *Block* |
|---|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「1」 | 「Excess molar enthalpy (H_E)」 | 「GLOBprop_17」 | 「GLOBlit_294」 | 「10.1016/j.fluid.2005.08.001」 | 「PROPblock_5」 |
| WM_L1#1_Table#1_Row#2 | 「2」 | 「Excess molar volume (V_E)」 | 「GLOBprop_28」 | 「GLOBlit_294」 | 「10.1016/j.fluid.2005.08.001」 | 「PROPblock_6」 |
| WM_L1#1_Table#1_Row#3 | 「3」 | 「Refractive index (n_D)」 | 「GLOBprop_7」 | 「GLOBlit_2800」 | 「10.1016/j.jct.2007.02.008」 | 「PROPblock_22」 |
| WM_L1#1_Table#1_Row#4 | 「4」 | 「Speed of sound (u)」 | 「GLOBprop_8」 | 「GLOBlit_2800」 | 「10.1016/j.jct.2007.02.008」 | 「PROPblock_23」 |
| WM_L1#1_Table#1_Row#5 | 「5」 | 「Mass density (ρ)」 | 「GLOBprop_1」 | 「GLOBlit_2800」 | 「10.1016/j.jct.2007.02.008」 | 「PROPblock_24」 |
| WM_L1#1_Table#1_Row#6 | 「6」 | 「Surface tension (γ)」 | 「GLOBprop_13」 | 「GLOBlit_10821」 | 「10.1021/je700215z」 | 「PROPblock_5」 |
| WM_L1#1_Table#1_Row#7 | 「7」 | 「Viscosity (η)」 | 「GLOBprop_4」 | 「GLOBlit_11449」 | 「10.1021/je800925v」 | 「PROPblock_9」 |

Additional blocks provide a second mass density source (GLOBlit_11449, PROPblock_10) covering 273.15–298.15 K.

---

##### Representative Data Points near Equimolar Composition (x_ethanol ≈ 0.5) at 298.15 K

The following values are quoted verbatim from inspected block data tables:

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *Property* | *Block* | *x(ethanol)* | *Value* | *Unit* | *Conditions* |
|---|---|---|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「Excess molar enthalpy」 | 「GLOBlit_294::PROPblock_5」 | 「0.49」 | 「0.5637」 | 「kJ/mol」 | 「T = 298.15 K, p = 101.325 kPa」 |
| WM_L1#1_Table#2_Row#2 | 「Excess molar enthalpy」 | 「GLOBlit_294::PROPblock_5」 | 「0.5191」 | 「0.5564」 | 「kJ/mol」 | 「T = 298.15 K, p = 101.325 kPa」 |
| WM_L1#1_Table#2_Row#3 | 「Excess molar volume」 | 「GLOBlit_294::PROPblock_6」 | 「0.4524」 | 「4.12×10⁻⁷」 | 「m³/mol」 | 「T = 298.15 K, p = 101.325 kPa」 |
| WM_L1#1_Table#2_Row#4 | 「Excess molar volume」 | 「GLOBlit_294::PROPblock_6」 | 「0.4995」 | 「4.08×10⁻⁷」 | 「m³/mol」 | 「T = 298.15 K, p = 101.325 kPa」 |
| WM_L1#1_Table#2_Row#5 | 「Refractive index」 | 「GLOBlit_2800::PROPblock_22」 | 「0.4999」 | 「1.36652」 | 「—」 | 「T = 298.15 K, p = 101.0 kPa」 |
| WM_L1#1_Table#2_Row#6 | 「Speed of sound」 | 「GLOBlit_2800::PROPblock_23」 | 「0.4999」 | 「1073」 | 「m/s」 | 「T = 298.15 K, p = 101.0 kPa」 |
| WM_L1#1_Table#2_Row#7 | 「Mass density」 | 「GLOBlit_2800::PROPblock_24」 | 「0.4999」 | 「692.1」 | 「kg/m³」 | 「T = 298.15 K, p = 101.0 kPa」 |
| WM_L1#1_Table#2_Row#8 | 「Surface tension」 | 「GLOBlit_10821::PROPblock_5」 | 「—」 | 「*not inspected in this run*」 | 「N/m」 | 「—」 |
| WM_L1#1_Table#2_Row#9 | 「Viscosity」 | 「GLOBlit_11449::PROPblock_9」 | 「—」 | 「*not inspected in this run*」 | 「Pa·s」 | 「—」 |
| WM_L1#1_Table#2_Row#10 | 「Mass density (2nd source)」 | 「GLOBlit_11449::PROPblock_10」 | 「—」 | 「*not inspected in this run*」 | 「kg/m³」 | 「—」 |

---

##### Chemical Insight

Hexane and ethanol form a highly non-ideal mixture: the positive excess molar enthalpy (≈ 0.56 kJ/mol near x = 0.5) reflects the endothermic disruption of ethanol's hydrogen-bond network upon mixing with the non-polar alkane. The excess molar volume is also positive (≈ 4.1×10⁻⁷ m³/mol ≈ 0.41 cm³/mol), consistent with weaker unlike interactions and a volume expansion on mixing. Both excess properties show non-monotonic composition dependence with maxima near the equimolar region, characteristic of systems with strong hydrogen-bonding asymmetry.

The mass density at x(ethanol) ≈ 0.5 (692.1 kg/m³) lies between the pure-component values (hexane ≈ 655 kg/m³ and ethanol ≈ 785 kg/m³ from the block statistics), while the speed of sound (1073 m/s) and refractive index (1.36652) similarly fall between the pure-component limits reported in these blocks.

**Core claims:**
- The ThermoML database contains 7 distinct thermophysical properties for the hexane + ethanol binary liquid mixture near 298.15 K: excess molar enthalpy, excess molar volume, refractive index, speed of sound, mass density, surface tension, and viscosity, drawn from 3 literature sources.
- At 298.15 K and near-equimolar composition (x_ethanol ≈ 0.5), the excess molar enthalpy is positive (0.5637 kJ/mol at x = 0.49; 0.5564 kJ/mol at x = 0.5191), reflecting endothermic disruption of ethanol's hydrogen-bond network upon mixing with non-polar hexane.
- The excess molar volume at 298.15 K is also positive near equimolar composition (4.12×10⁻⁷ m³/mol at x = 0.4524; 4.08×10⁻⁷ m³/mol at x = 0.4995), consistent with weaker unlike interactions and volume expansion on mixing.
- At x(ethanol) ≈ 0.5 and 298.15 K, the mass density is 692.1 kg/m³, the speed of sound is 1073 m/s, and the refractive index is 1.36652, all falling between the respective pure-component values.
- Surface tension and viscosity data blocks, as well as a second mass density source, were identified but not inspected in this run and remain unverified.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_294」 | 「PROPblock_5」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_17」 | 「Excess molar enthalpy measurements for hexane + ethanol binary mixture near 298.15 K.」 |
| WM_L1#1_Table#4 | 「GLOBlit_294」 | 「PROPblock_6」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_28」 | 「Excess molar volume measurements for hexane + ethanol binary mixture near 298.15 K.」 |
| WM_L1#1_Table#5 | 「GLOBlit_2800」 | 「PROPblock_22」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_7」 | 「Refractive index measurements for hexane + ethanol binary mixture near 298.15 K.」 |
| WM_L1#1_Table#6 | 「GLOBlit_2800」 | 「PROPblock_23」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_8」 | 「Speed of sound measurements for hexane + ethanol binary mixture near 298.15 K.」 |
| WM_L1#1_Table#7 | 「GLOBlit_2800」 | 「PROPblock_24」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_1」 | 「Mass density measurements for hexane + ethanol binary mixture near 298.15 K.」 |
| WM_L1#1_Table#8 | 「GLOBlit_10821」 | 「PROPblock_5」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_13」 | 「Surface tension measurements for hexane + ethanol binary mixture near 298.15 K.」 |
| WM_L1#1_Table#9 | 「GLOBlit_11449」 | 「PROPblock_9」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_4」 | 「Viscosity measurements for hexane + ethanol binary mixture near 298.15 K.」 |
| WM_L1#1_Table#10 | 「GLOBlit_11449」 | 「PROPblock_10」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_1」 | 「Mass density measurements (second source) for hexane + ethanol binary mixture covering 273.15–298.15 K.」 |

*Not stored here: 5 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_10: PROPblock_10 is quoted with data values (273.15, 298.15, 0.5, 298.15, …) but was never inspected in this run (values 273.15, 298.15, 0.5, 298.15 verified against the database — inspection is still mandatory)
- **UNINSPECTED_BLOCK** GLOBlit_11449::PROPblock_10: GLOBlit_11449::PROPblock_10 is quoted with data values (0.56, 0.5, 4.1e-7, 0.41, …) but was never inspected in this run (values 0.5, 0.5, 655 verified against the database — inspection is still mandatory)


