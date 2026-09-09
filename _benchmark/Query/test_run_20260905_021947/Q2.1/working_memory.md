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
- [L1] Find all measured mixture properties for benzene + toluene binary near room temperature (~288-308 K). Report: (1) list o → stored as L1_query_1 · validation: PASS
- [L1] Find all measured mixture properties for binary hexane + ethanol near room temperature (288–308 K). Report: (1) list of  → stored as L1_query_2 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** A search of the ThermoML database for binary benzene + toluene data in the 288–308 K range returned 2 data blocks covering 2 distinct liquid-phase property types across 4 total data points. The properties are excess molar enthalpy (GLOBprop_17, from GLOBlit_6057, DOI 10.1016/j.tca.2013.01.028) and molar enthalpy of solution (GLOBprop_15, from GLOBlit_6268, DOI 10.1016/j.tca.2015.09.022). Excess molar enthalpy was measured at 303.15 K and 101.0 kPa over toluene mole fractions 0.247–0.7685 (3 points), yielding small positive values of 0.0543, 0.0713, and 0.0477 kJ/mol at x(toluene) = 0.247, 0.4944, and 0.7685 respectively, with a maximum near equimolar composition consistent with nearly ideal mixing. Molar enthalpy of solution was measured at 298.15 K and 100 kPa at infinite dilution (x(toluene) = 0), giving 0.28 kJ/mol, reflecting weak endothermic mixing of these structurally similar aromatic hydrocarbons.

**Answer:**

#### Binary Mixture Properties for Benzene + Toluene Near Room Temperature (288–308 K)

##### Overview

A search of the ThermoML database for binary (benzene + toluene) data blocks with temperatures in the 288–308 K range returned **2 data blocks** covering **2 distinct property types**, all in the **liquid phase**.

---

##### 1. Distinct Property Types

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *GLOBprop ID* | *Property Name* | *Measurement Method* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「GLOBprop_17」 | 「Excess molar enthalpy (enthalpy of mixing), kJ/mol」 | 「Calvet calorimetry」 |
| WM_L1#1_Table#1_Row#2 | 「GLOBprop_15」 | 「Molar enthalpy of solution, kJ/mol」 | 「Titration calorimetry」 |

---

##### 2. Composition (Mole Fraction of Toluene) Range Covered

- **GLOBprop_17** (excess molar enthalpy, GLOBlit_6057 :: PROPblock_1): 0.247 – 0.7685 (3 data points spanning the mid-composition range)
- **GLOBprop_15** (molar enthalpy of solution, GLOBlit_6268 :: PROPblock_7): 0 (infinite dilution, 1 data point; toluene dissolved in benzene solvent)

---

##### 3. Number of Data Blocks and Data Points

- **Total data blocks:** 2
- **Total data points:** 4 (3 + 1)

---

##### 4. Literature References

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *GLOBlit ID* | *DOI* | *Block(s)* |
|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「GLOBlit_6057」 | 「10.1016/j.tca.2013.01.028」 | 「PROPblock_1 (excess molar enthalpy)」 |
| WM_L1#1_Table#2_Row#2 | 「GLOBlit_6268」 | 「10.1016/j.tca.2015.09.022」 | 「PROPblock_7 (molar enthalpy of solution)」 |

---

##### 5. Representative Data

###### GLOBlit_6057 :: PROPblock_1 — Excess Molar Enthalpy

This block reports excess molar enthalpy at constrained T = 303.15 K and P = 101.0 kPa:

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *x(toluene)* | *Excess Molar Enthalpy (kJ/mol)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0.247」 | 「0.0543」 |
| WM_L1#1_Table#3_Row#2 | 「0.4944」 | 「0.0713」 |
| WM_L1#1_Table#3_Row#3 | 「0.7685」 | 「0.0477」 |

The excess molar enthalpy values are very small and positive (0.0477–0.0713 kJ/mol), consistent with the nearly ideal mixing behavior expected for benzene + toluene — two structurally similar aromatic hydrocarbons with comparable intermolecular interactions. The non-monotonic profile with a maximum near equimolar composition (x ≈ 0.49) is characteristic of symmetric excess enthalpy curves.

###### GLOBlit_6268 :: PROPblock_7 — Molar Enthalpy of Solution

This block reports molar enthalpy of solution at T = 298.15 K and P = 100 kPa:

**WM_L1#1_Table#4_(Query_L1#1_Answer):**

| *row_id* | *x(toluene)* | *Molar Enthalpy of Solution (kJ/mol)* |
|---|---|---|
| WM_L1#1_Table#4_Row#1 | 「0」 | 「0.28」 |

The molar enthalpy of solution for toluene at infinite dilution in benzene is 0.28 kJ/mol, again reflecting the weak endothermic character of mixing these two similar aromatics.

**Core claims:**
- A ThermoML search for binary benzene + toluene data in the 288–308 K range returned 2 data blocks covering 2 liquid-phase property types: excess molar enthalpy (kJ/mol) and molar enthalpy of solution (kJ/mol), with a total of 4 data points.
- Excess molar enthalpy at 303.15 K and 101.0 kPa spans toluene mole fractions 0.247–0.7685, with small positive values (0.0543, 0.0713, and 0.0477 kJ/mol), exhibiting a maximum near equimolar composition consistent with nearly ideal mixing of two structurally similar aromatic hydrocarbons.
- The molar enthalpy of solution for toluene at infinite dilution in benzene at 298.15 K and 100 kPa is 0.28 kJ/mol, reflecting weak endothermic mixing character.
- The two data blocks originate from two literature sources with DOIs 10.1016/j.tca.2013.01.028 and 10.1016/j.tca.2015.09.022.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#5 | 「GLOBlit_6057」 | 「PROPblock_1」 | 「GLOBcomp_14, GLOBcomp_8」 | 「GLOBprop_17」 | 「Excess molar enthalpy (enthalpy of mixing) for benzene + toluene at 303.15 K, mole fraction of toluene 0.247–0.7685.」 |
| WM_L1#1_Table#6 | 「GLOBlit_6268」 | 「PROPblock_7」 | 「GLOBcomp_14, GLOBcomp_8」 | 「GLOBprop_15」 | 「Molar enthalpy of solution for toluene at infinite dilution in benzene at 298.15 K.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: success · validation: FLAGGED(1)

**Summary:** The hexane (GLOBcomp_12) + ethanol (GLOBcomp_2) binary system in the ThermoML database near room temperature (288–308 K) spans 9 data blocks, 8 distinct property types, and 5 literature sources. The 8 property types are: excess molar enthalpy (GLOBprop_17), excess molar volume (GLOBprop_28), refractive index (GLOBprop_7), speed of sound (GLOBprop_8), mass density (GLOBprop_1), binary diffusion coefficient (GLOBprop_29), surface tension (GLOBprop_13), and viscosity (GLOBprop_4). Composition coverage for most properties extends across the full mole-fraction range of ethanol (0–1). Three blocks were inspected in detail: excess molar enthalpy (GLOBlit_294::PROPblock_5, 17 data points at 298.15 K, x(ethanol) 0.0544–0.9528, positive values peaking at approximately 0.5795 kJ/mol near x(ethanol) ≈ 0.36); excess molar volume (GLOBlit_294::PROPblock_6, 23 data points at 298.15 K, x(ethanol) 0.0417–0.9497, positive values with a maximum of 4.12×10⁻⁷ m³/mol near x(ethanol) ≈ 0.45); and binary diffusion coefficient (GLOBlit_8445::PROPblock_8, 9 data points at 298.15 K, ranging from 5.74×10⁻⁹ m²/s at x(ethanol) = 0 to a minimum of 1.3×10⁻⁹ m²/s at x(ethanol) = 0.5–0.7). The five literature sources are GLOBlit_294 (DOI 10.1016/j.fluid.2005.08.001), GLOBlit_2800 (DOI 10.1016/j.jct.2007.02.008), GLOBlit_8445 (DOI 10.1021/je0497303), GLOBlit_10821 (DOI 10.1021/je700215z), and GLOBlit_11449 (DOI 10.1021/je800925v). Compared with the benzene + toluene binary (2 blocks, 2 property types), hexane + ethanol is a far richer model-testing system, covering thermodynamic, transport, acoustic, optical, volumetric, and interfacial properties. Six blocks were not individually inspected, so their exact data-point counts remain unverified.

**Answer:**

### Binary Hexane + Ethanol Mixture Properties Near Room Temperature (288–308 K)

#### Overview

The ThermoML database contains **9 data blocks** for the binary system hexane (GLOBcomp_12) + ethanol (GLOBcomp_2) with temperature values or constraints in the 288–308 K range. These blocks span **8 distinct property types** across **5 literature sources**, offering substantially more property diversity than the benzene + toluene binary (which had only 2 blocks, 2 property types, and 4 data points in the same temperature window).

---

#### (1) Distinct Property Types with GLOBprop IDs

**WM_L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *#* | *Property* | *GLOBprop ID* |
|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「1」 | 「Excess molar enthalpy (molar enthalpy of mixing)」 | 「GLOBprop_17」 |
| WM_L1#2_Table#1_Row#2 | 「2」 | 「Excess molar volume」 | 「GLOBprop_28」 |
| WM_L1#2_Table#1_Row#3 | 「3」 | 「Refractive index (Na D-line)」 | 「GLOBprop_7」 |
| WM_L1#2_Table#1_Row#4 | 「4」 | 「Speed of sound」 | 「GLOBprop_8」 |
| WM_L1#2_Table#1_Row#5 | 「5」 | 「Mass density」 | 「GLOBprop_1」 |
| WM_L1#2_Table#1_Row#6 | 「6」 | 「Binary diffusion coefficient」 | 「GLOBprop_29」 |
| WM_L1#2_Table#1_Row#7 | 「7」 | 「Surface tension (liquid–gas)」 | 「GLOBprop_13」 |
| WM_L1#2_Table#1_Row#8 | 「8」 | 「Viscosity」 | 「GLOBprop_4」 |

**Total distinct property types: 8**

---

#### (2) Composition Range Covered for Each Property

**WM_L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *Property* | *Block(s)* | *x(ethanol) range* | *Source of range* |
|---|---|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「Excess molar enthalpy」 | 「GLOBlit_294::PROPblock_5」 | 「0.0544–0.9528」 | 「Inspected (n=17)」 |
| WM_L1#2_Table#2_Row#2 | 「Excess molar volume」 | 「GLOBlit_294::PROPblock_6」 | 「0.0417–0.9497」 | 「Inspected (n=23)」 |
| WM_L1#2_Table#2_Row#3 | 「Refractive index」 | 「GLOBlit_2800::PROPblock_22」 | 「0–1 (full range incl. pure components)」 | 「From search_blocks summary」 |
| WM_L1#2_Table#2_Row#4 | 「Speed of sound」 | 「GLOBlit_2800::PROPblock_23」 | 「0–1 (full range incl. pure components)」 | 「From search_blocks summary」 |
| WM_L1#2_Table#2_Row#5 | 「Mass density」 | 「GLOBlit_2800::PROPblock_24 + GLOBlit_11449::PROPblock_10」 | 「0–1 (PROPblock_24, from search summary); not inspected for PROPblock_10 in this run」 | 「From search_blocks summary」 |
| WM_L1#2_Table#2_Row#6 | 「Binary diffusion coefficient」 | 「GLOBlit_8445::PROPblock_8」 | 「0–1 (full range incl. pure components)」 | 「Inspected (n=9)」 |
| WM_L1#2_Table#2_Row#7 | 「Surface tension」 | 「GLOBlit_10821::PROPblock_5」 | 「Not inspected in this run; search summary reported range from tool result」 | 「From search_blocks summary」 |
| WM_L1#2_Table#2_Row#8 | 「Viscosity」 | 「GLOBlit_11449::PROPblock_9」 | 「Not inspected in this run; search summary reported ethanol-rich limit」 | 「From search_blocks summary」 |

---

#### (3) Number of Data Blocks and Data Points

**WM_L1#2_Table#3_(Query_L1#2_Answer):**

| *row_id* | *Block* | *GLOBlit* | *Property* | *Data points (total in block)* |
|---|---|---|---|---|
| WM_L1#2_Table#3_Row#1 | 「PROPblock_5」 | 「GLOBlit_294」 | 「Excess molar enthalpy」 | 「17」 |
| WM_L1#2_Table#3_Row#2 | 「PROPblock_6」 | 「GLOBlit_294」 | 「Excess molar volume」 | 「23」 |
| WM_L1#2_Table#3_Row#3 | 「PROPblock_22」 | 「GLOBlit_2800」 | 「Refractive index」 | 「Not inspected; search summary reported the block」 |
| WM_L1#2_Table#3_Row#4 | 「PROPblock_23」 | 「GLOBlit_2800」 | 「Speed of sound」 | 「Not inspected; search summary reported the block」 |
| WM_L1#2_Table#3_Row#5 | 「PROPblock_24」 | 「GLOBlit_2800」 | 「Mass density」 | 「Not inspected; search summary reported the block」 |
| WM_L1#2_Table#3_Row#6 | 「PROPblock_8」 | 「GLOBlit_8445」 | 「Binary diffusion coefficient」 | 「9」 |
| WM_L1#2_Table#3_Row#7 | 「PROPblock_5」 | 「GLOBlit_10821」 | 「Surface tension」 | 「Not inspected; search summary reported the block」 |
| WM_L1#2_Table#3_Row#8 | 「PROPblock_9」 | 「GLOBlit_11449」 | 「Viscosity」 | 「Not inspected; search summary reported the block」 |
| WM_L1#2_Table#3_Row#9 | 「PROPblock_10」 | 「GLOBlit_11449」 | 「Mass density」 | 「Not inspected; search summary reported the block」 |

- **Total blocks: 9**
- **Total data points across inspected blocks: 49** (17 + 23 + 9). The remaining 6 blocks were not inspected in this run, so their exact point counts cannot be confirmed here. The search summaries indicated substantial additional data.

---

#### (4) Literature References

**WM_L1#2_Table#4_(Query_L1#2_Answer):**

| *row_id* | *#* | *GLOBlit ID* | *DOI* | *Blocks* | *Properties* |
|---|---|---|---|---|---|
| WM_L1#2_Table#4_Row#1 | 「1」 | 「GLOBlit_294」 | 「10.1016/j.fluid.2005.08.001」 | 「PROPblock_5, PROPblock_6」 | 「Excess molar enthalpy, Excess molar volume」 |
| WM_L1#2_Table#4_Row#2 | 「2」 | 「GLOBlit_2800」 | 「10.1016/j.jct.2007.02.008」 | 「PROPblock_22, PROPblock_23, PROPblock_24」 | 「Refractive index, Speed of sound, Mass density」 |
| WM_L1#2_Table#4_Row#3 | 「3」 | 「GLOBlit_8445」 | 「10.1021/je0497303」 | 「PROPblock_8」 | 「Binary diffusion coefficient」 |
| WM_L1#2_Table#4_Row#4 | 「4」 | 「GLOBlit_10821」 | 「10.1021/je700215z」 | 「PROPblock_5」 | 「Surface tension (liquid–gas)」 |
| WM_L1#2_Table#4_Row#5 | 「5」 | 「GLOBlit_11449」 | 「10.1021/je800925v」 | 「PROPblock_9, PROPblock_10」 | 「Viscosity, Mass density」 |

---

#### Representative Inspected Data

**Excess molar enthalpy** (GLOBlit_294::PROPblock_5, T = 298.15 K, P = 101.325 kPa):
The enthalpy of mixing is positive across the full composition range, peaking at approximately 0.5795 kJ/mol near x(ethanol) ≈ 0.36, consistent with the endothermic disruption of hydrogen-bonding networks in ethanol by the nonpolar hexane.

**Excess molar volume** (GLOBlit_294::PROPblock_6, T = 298.15 K, P = 101.325 kPa):
Positive excess volumes across the full range, with a maximum of 4.12×10⁻⁷ m³/mol near x(ethanol) ≈ 0.45, indicating volume expansion on mixing — typical for systems with strong unlike-molecule repulsion and poor packing.

**Binary diffusion coefficient** (GLOBlit_8445::PROPblock_8, T = 298.15 K, P = 101.3 kPa):
Diffusion coefficients decrease sharply from 5.74×10⁻⁹ m²/s at x(ethanol) = 0 to a minimum of 1.3×10⁻⁹ m²/s at x(ethanol) = 0.5–0.7, reflecting the increased viscosity and hydrogen-bonding interactions in the ethanol-rich regime.

---

#### Comparison with Benzene + Toluene

**WM_L1#2_Table#5_(Query_L1#2_Answer):**

| *row_id* | *Metric* | *Hexane + Ethanol* | *Benzene + Toluene* |
|---|---|---|---|
| WM_L1#2_Table#5_Row#1 | 「Distinct property types」 | 「8」 | 「2」 |
| WM_L1#2_Table#5_Row#2 | 「Total data blocks」 | 「9」 | 「2」 |
| WM_L1#2_Table#5_Row#3 | 「Literature sources」 | 「5」 | 「(from prior context)」 |
| WM_L1#2_Table#5_Row#4 | 「Composition coverage」 | 「Near-full (0–1) for most properties」 | 「Limited」 |

Hexane + ethanol is clearly a far richer model-testing binary in the ThermoML database near room temperature, offering diverse thermodynamic (excess enthalpy, excess volume), transport (diffusion, viscosity), acoustic (speed of sound), optical (refractive index), volumetric (density), and interfacial (surface tension) data across wide composition ranges.

**Core claims:**
- The ThermoML database contains 9 data blocks for the hexane + ethanol binary system in the 288–308 K temperature range, spanning 8 distinct property types (excess molar enthalpy, excess molar volume, refractive index, speed of sound, mass density, binary diffusion coefficient, surface tension, and viscosity) from 5 literature sources.
- Most properties cover a near-full ethanol mole fraction range (0–1), with inspected blocks confirming coverage of x(ethanol) from 0.0544–0.9528 for excess molar enthalpy, 0.0417–0.9497 for excess molar volume, and 0–1 for binary diffusion coefficient.
- Excess molar enthalpy at 298.15 K and 101.325 kPa is positive across the full composition range, peaking at approximately 0.5795 kJ/mol near x(ethanol) ≈ 0.36, consistent with endothermic disruption of ethanol hydrogen-bonding networks by nonpolar hexane.
- Excess molar volume at 298.15 K and 101.325 kPa is positive across the full range, with a maximum of 4.12×10⁻⁷ m³/mol near x(ethanol) ≈ 0.45, indicating volume expansion on mixing.
- Binary diffusion coefficients at 298.15 K and 101.3 kPa decrease from 5.74×10⁻⁹ m²/s at x(ethanol) = 0 to a minimum of 1.3×10⁻⁹ m²/s at x(ethanol) = 0.5–0.7.
- Hexane + ethanol offers substantially greater property diversity in ThermoML near room temperature than benzene + toluene, which had only 2 data blocks and 2 property types in the same temperature window.
- Six of the nine blocks were not individually inspected in this run, so their exact data-point counts and composition ranges remain unverified.

**Core blocks found:**

**WM_L1#2_Blocks_(Query_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#6 | 「GLOBlit_294」 | 「PROPblock_5」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_17」 | 「Excess molar enthalpy for hexane + ethanol at 298.15 K; x(ethanol) 0.0544–0.9528; 17 data points.」 |
| WM_L1#2_Table#7 | 「GLOBlit_294」 | 「PROPblock_6」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_28」 | 「Excess molar volume for hexane + ethanol at 298.15 K; x(ethanol) 0.0417–0.9497; 23 data points.」 |
| WM_L1#2_Table#8 | 「GLOBlit_2800」 | 「PROPblock_22」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_7」 | 「Refractive index (Na D-line) for hexane + ethanol; x(ethanol) 0–1.」 |
| WM_L1#2_Table#9 | 「GLOBlit_2800」 | 「PROPblock_23」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_8」 | 「Speed of sound for hexane + ethanol; x(ethanol) 0–1.」 |
| WM_L1#2_Table#10 | 「GLOBlit_2800」 | 「PROPblock_24」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_1」 | 「Mass density for hexane + ethanol; x(ethanol) 0–1.」 |
| WM_L1#2_Table#11 | 「GLOBlit_8445」 | 「PROPblock_8」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_29」 | 「Binary diffusion coefficient for hexane + ethanol at 298.15 K; x(ethanol) 0–1; 9 data points.」 |
| WM_L1#2_Table#12 | 「GLOBlit_10821」 | 「PROPblock_5」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_13」 | 「Surface tension (liquid–gas) for hexane + ethanol.」 |
| WM_L1#2_Table#13 | 「GLOBlit_11449」 | 「PROPblock_9」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_4」 | 「Viscosity for hexane + ethanol.」 |
| WM_L1#2_Table#14 | 「GLOBlit_11449」 | 「PROPblock_10」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_1」 | 「Mass density for hexane + ethanol.」 |

*Not stored here: 3 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_10: PROPblock_10 is quoted with data values (49, 17, 23, …) but was never inspected in this run


