# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_062559_197899_3acd2447`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_2 | ethanol | 0.0 |
| comp | GLOBcomp_1 | water | 1.8065584e-05 |
| prop | GLOBprop_17 | excessmolarenthalpymolarenthalpyofmixingkjmol |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<ethanol> |  |
| constr | GLOBconstr_1 | pressurekpa |  |
| lit | GLOBlit_528 | 10.1016/j.fluid.2007.06.007 |  |
| lit | GLOBlit_2574 | 10.1016/j.jct.2005.06.018 |  |

### History
- [query_thermoml_parallel]
- [query_thermoml_parallel]
- [fit_multi_system]
- [inspect_block]
- [fit_block]
- [predict_from_rk]
- [predict_from_rk]
- [query_thermoml]
- [fit_block_derived] ERROR: Unknown transform 'density_to_excess_volume'. Available: ['density_to_molar_volu
- [fit_block_derived]

### Query Results
#### HE_methanol_water
**L1_query_1** — status: success · validation: PASS

**Summary:** One ThermoML block was found for the excess molar enthalpy (Hᴱ) of methanol + water at 298.15 K and 101.0 kPa, from DOI 10.1016/j.tca.2006.02.028, measured by titration calorimetry. The block contains 13 data points spanning x(methanol) = 0–1. Hᴱ is negative across the entire composition range, with a minimum of approximately −0.85 kJ/mol near x(methanol) ≈ 0.3, indicating exothermic mixing driven by strong hydrogen-bonding interactions. A shape-preserving subset of 10 points is reported, including x(methanol) values of 0.0, 0.05, 0.15, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, and 1.0 with corresponding Hᴱ values of 0.0, −0.326, −0.714, −0.806, −0.85, −0.841, −0.777, −0.583, −0.241, and 0.0 kJ/mol. The asymmetric curve shape, with the minimum shifted toward the methanol-lean side, is characteristic of aqueous alcohol systems.

**Answer:**

#### Excess Molar Enthalpy (Hᴱ) Data for Methanol + Water at 298.15 K

**One block found** in the ThermoML database containing excess molar enthalpy data for the methanol + water binary system at 298.15 K.

##### Source Details

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *Field* | *Value* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「**DOI**」 | 「10.1016/j.tca.2006.02.028」 |
| WM_L1#1_Table#1_Row#2 | 「**Literature ID**」 | 「GLOBlit_5688」 |
| WM_L1#1_Table#1_Row#3 | 「**Block**」 | 「PROPblock_1」 |
| WM_L1#1_Table#1_Row#4 | 「**Property**」 | 「Excess molar enthalpy (GLOBprop_17), kJ/mol」 |
| WM_L1#1_Table#1_Row#5 | 「**Method**」 | 「Titration calorimetry (GLOBmeas_25)」 |
| WM_L1#1_Table#1_Row#6 | 「**Temperature**」 | 「298.15 K (constant)」 |
| WM_L1#1_Table#1_Row#7 | 「**Pressure**」 | 「101.0 kPa (constant)」 |
| WM_L1#1_Table#1_Row#8 | 「**Total data points**」 | 「13」 |

##### Data Table (10 of 13 points, RDP shape-preserving subset)

**WM_L1#1_Table#2_(Analysis_L1#1_Answer):**

| *row_id* | *x(methanol)* | *Hᴱ (kJ/mol)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0.0」 | 「0.0」 |
| WM_L1#1_Table#2_Row#2 | 「0.05」 | 「−0.326」 |
| WM_L1#1_Table#2_Row#3 | 「0.15」 | 「−0.714」 |
| WM_L1#1_Table#2_Row#4 | 「0.2」 | 「−0.806」 |
| WM_L1#1_Table#2_Row#5 | 「0.3」 | 「−0.85」 |
| WM_L1#1_Table#2_Row#6 | 「0.4」 | 「−0.841」 |
| WM_L1#1_Table#2_Row#7 | 「0.5」 | 「−0.777」 |
| WM_L1#1_Table#2_Row#8 | 「0.7」 | 「−0.583」 |
| WM_L1#1_Table#2_Row#9 | 「0.9」 | 「−0.241」 |
| WM_L1#1_Table#2_Row#10 | 「1.0」 | 「0.0」 |

**Full-block statistics (all 13 points):** x(methanol) spans 0–1; Hᴱ ranges from −0.85 to 0 kJ/mol.

##### Chemical Insight

The excess molar enthalpy is negative across the entire composition range, indicating that mixing methanol and water at 298.15 K is an exothermic process. The minimum Hᴱ of approximately −0.85 kJ/mol occurs near x(methanol) ≈ 0.3, reflecting the strong hydrogen-bonding interactions between methanol and water molecules. The asymmetric shape of the Hᴱ curve (minimum shifted toward the methanol-lean side) is characteristic of aqueous alcohol systems, where the disruption and reformation of hydrogen-bond networks is most energetically favorable at compositions where water molecules can effectively solvate the alcohol hydroxyl groups.

**Core claims:**
- One block of excess molar enthalpy (Hᴱ) data for methanol + water at 298.15 K and 101.0 kPa was found in the ThermoML database (DOI 10.1016/j.tca.2006.02.028), measured by titration calorimetry, containing 13 data points spanning x(methanol) = 0–1.
- Hᴱ is negative across the entire composition range, indicating that mixing methanol and water at 298.15 K is exothermic, with values ranging from −0.85 to 0 kJ/mol.
- The minimum Hᴱ of approximately −0.85 kJ/mol occurs near x(methanol) ≈ 0.3, and the asymmetric shape of the Hᴱ curve (minimum shifted toward the methanol-lean side) is characteristic of aqueous alcohol systems reflecting strong hydrogen-bonding interactions.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_5688」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for methanol + water at 298.15 K and 101.0 kPa, 13 data points, measured by titration calorimetry.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### HE_ethanol_water
**L1_query_2** — status: success · validation: PASS

**Summary:** Three ThermoML data blocks report excess molar enthalpy (Hᴱ) for ethanol + water near 298.15 K. GLOBlit_528 PROPblock_1 (DOI 10.1016/j.fluid.2007.06.007) gives 15 points at 298.15 K and 101.0 kPa in the very dilute ethanol regime, x(ethanol) 0.000102–0.001551, with Hᴱ from −0.00104 to −0.01537 kJ/mol, showing nearly linear exothermic behavior. GLOBlit_528 PROPblock_2 (same DOI) gives 15 points at 298.15 K and 101.0 kPa in the very dilute water regime, x(water) 0.001021–0.015286, with Hᴱ from −0.00212 to −0.02961 kJ/mol, also monotonic and linear. GLOBlit_2574 PROPblock_4 (DOI 10.1016/j.jct.2005.06.018) provides 27 points spanning 298.15–323.15 K at 101.0 kPa over x(ethanol) 0.033–0.968, with Hᴱ ranging from −0.77 to −0.018 kJ/mol; at 298.15 K the minimum Hᴱ is around −0.767 kJ/mol near x(ethanol) ≈ 0.18. A caveat applies to the third block: the source publication title references propanediols/butanediol rather than ethanol, so the compound mapping may be erroneous and should be verified independently. The GLOBlit_528 blocks are considered high-quality dilute-regime data at exactly 298.15 K.

**Answer:**

#### Excess Molar Enthalpy (Hᴱ) Data for Ethanol + Water at 298.15 K

Three blocks of excess molar enthalpy data for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system were found in the ThermoML database near 298.15 K:

##### Block 1 — GLOBlit_528 :: PROPblock_1
**DOI:** 10.1016/j.fluid.2007.06.007  
**Temperature:** 298.15 K (fixed constraint)  
**Pressure:** 101.0 kPa (fixed constraint)  
**Data points:** 15  
**Composition range:** x(ethanol) 0.000102–0.001551 (very dilute ethanol in water)  
**Hᴱ range:** −0.00104 to −0.01537 kJ/mol  

Representative inspected rows:

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *x(ethanol)* | *Hᴱ (kJ/mol)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0.000102」 | 「−0.00104」 |
| WM_L1#2_Table#1_Row#2 | 「0.000516」 | 「−0.00518」 |
| WM_L1#2_Table#1_Row#3 | 「0.001034」 | 「−0.0103」 |
| WM_L1#2_Table#1_Row#4 | 「0.001551」 | 「−0.01537」 |

The data show a monotonic, nearly linear decrease in Hᴱ with increasing ethanol mole fraction in this very dilute regime, consistent with exothermic hydration of ethanol at infinite dilution.

##### Block 2 — GLOBlit_528 :: PROPblock_2
**DOI:** 10.1016/j.fluid.2007.06.007  
**Temperature:** 298.15 K (fixed constraint)  
**Pressure:** 101.0 kPa (fixed constraint)  
**Data points:** 15  
**Composition range:** x(water) 0.001021–0.015286 (very dilute water in ethanol)  
**Hᴱ range:** −0.00212 to −0.02961 kJ/mol  

Representative inspected rows:

**WM_L1#2_Table#2_(Analysis_L1#2_Answer):**

| *row_id* | *x(water)* | *Hᴱ (kJ/mol)* |
|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「0.001021」 | 「−0.00212」 |
| WM_L1#2_Table#2_Row#2 | 「0.006155」 | 「−0.01238」 |
| WM_L1#2_Table#2_Row#3 | 「0.010239」 | 「−0.02023」 |
| WM_L1#2_Table#2_Row#4 | 「0.015286」 | 「−0.02961」 |

Again monotonic and linear, reflecting exothermic mixing at the water-dilute end.

##### Block 3 — GLOBlit_2574 :: PROPblock_4
**DOI:** 10.1016/j.jct.2005.06.018  
**Temperature range:** 298.15–323.15 K  
**Pressure:** 101.0 kPa (fixed constraint)  
**Data points:** 27 total (covers both 298.15 K and 323.15 K)  
**Composition range:** x(ethanol) 0.033–0.968  
**Hᴱ range:** −0.77 to −0.018 kJ/mol (full block)  

Inspected rows at 298.15 K:

**WM_L1#2_Table#3_(Analysis_L1#2_Answer):**

| *row_id* | *x(ethanol)* | *Hᴱ (kJ/mol)* |
|---|---|---|
| WM_L1#2_Table#3_Row#1 | 「0.0582」 | 「−0.492」 |
| WM_L1#2_Table#3_Row#2 | 「0.1198」 | 「−0.747」 |
| WM_L1#2_Table#3_Row#3 | 「0.1837」 | 「−0.767」 |
| WM_L1#2_Table#3_Row#4 | 「0.5」 | 「−0.391」 |
| WM_L1#2_Table#3_Row#5 | 「0.9」 | 「−0.148」 |

⚠️ **Caution:** The source publication title references propanediols/butanediol rather than ethanol — the compound mapping in this block may be erroneous. The Hᴱ values at 298.15 K (minimum around −0.767 kJ/mol near x(ethanol) ≈ 0.18) are broadly consistent with known ethanol–water mixing behavior, but the provenance should be verified independently.

##### Summary

**WM_L1#2_Table#4_(Analysis_L1#2_Answer):**

| *row_id* | *DOI* | *Block* | *GLOBlit* | *T (K)* | *Points* | *Composition variable* | *Composition range* | *Hᴱ range (kJ/mol)* |
|---|---|---|---|---|---|---|---|---|
| WM_L1#2_Table#4_Row#1 | 「10.1016/j.fluid.2007.06.007」 | 「PROPblock_1」 | 「GLOBlit_528」 | 「298.15」 | 「15」 | 「x(ethanol)」 | 「0.000102–0.001551」 | 「−0.01537 to −0.00104」 |
| WM_L1#2_Table#4_Row#2 | 「10.1016/j.fluid.2007.06.007」 | 「PROPblock_2」 | 「GLOBlit_528」 | 「298.15」 | 「15」 | 「x(water)」 | 「0.001021–0.015286」 | 「−0.02961 to −0.00212」 |
| WM_L1#2_Table#4_Row#3 | 「10.1016/j.jct.2005.06.018」 | 「PROPblock_4」 | 「GLOBlit_2574」 | 「298.15–323.15」 | 「27」 | 「x(ethanol)」 | 「0.033–0.968」 | 「−0.77 to −0.018」 |

The GLOBlit_528 blocks provide high-quality dilute-regime Hᴱ data at exactly 298.15 K. GLOBlit_2574 PROPblock_4 offers wider composition coverage but includes data at two temperatures and carries a compound-mapping caveat.

**Core claims:**
- Three blocks of excess molar enthalpy (Hᴱ) data for ethanol + water near 298.15 K at 101.0 kPa were identified in the ThermoML database.
- GLOBlit_528 PROPblock_1 (DOI 10.1016/j.fluid.2007.06.007) provides 15 data points at 298.15 K in the very dilute ethanol regime (x(ethanol) 0.000102–0.001551), with Hᴱ ranging from −0.00104 to −0.01537 kJ/mol, showing a monotonic, nearly linear decrease consistent with exothermic hydration of ethanol at infinite dilution.
- GLOBlit_528 PROPblock_2 (DOI 10.1016/j.fluid.2007.06.007) provides 15 data points at 298.15 K in the very dilute water regime (x(water) 0.001021–0.015286), with Hᴱ ranging from −0.00212 to −0.02961 kJ/mol, again monotonic and linear, reflecting exothermic mixing at the water-dilute end.
- GLOBlit_2574 PROPblock_4 (DOI 10.1016/j.jct.2005.06.018) provides 27 data points spanning 298.15–323.15 K over a wide composition range (x(ethanol) 0.033–0.968), with Hᴱ ranging from −0.77 to −0.018 kJ/mol; at 298.15 K the minimum Hᴱ is around −0.767 kJ/mol near x(ethanol) ≈ 0.18.
- The GLOBlit_2574 block carries a provenance caveat: the source publication title references propanediols/butanediol rather than ethanol, so the compound mapping may be erroneous and should be verified independently.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#5 | 「GLOBlit_528」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for ethanol + water at 298.15 K, 101.0 kPa; 15 data points in very dilute ethanol regime (x(ethanol) 0.000102–0.001551).」 |
| WM_L1#2_Table#6 | 「GLOBlit_528」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for ethanol + water at 298.15 K, 101.0 kPa; 15 data points in very dilute water regime (x(water) 0.001021–0.015286).」 |
| WM_L1#2_Table#7 | 「GLOBlit_2574」 | 「PROPblock_4」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for ethanol + water at 298.15–323.15 K, 101.0 kPa; 27 data points over full composition range (x(ethanol) 0.033–0.968). Compound-mapping caveat noted.」 |

*Not stored here: 3 verbatim data_inspections table(s); 4 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### HE_propanol_water — ERROR
query-L1 core-ID refinement exhausted 2 cycles: construct_core_blocks_found: core_blocks_found[0] checksum mismatch for (GLOBlit_1766, PROPblock_1): system_type expected 'binary', received 'ternary'; comp_num_ids expected ['GLOBcomp_5', 'GLOBcomp_1'], received ['GLOBcomp_35', 'GLOBcomp_5', 'GLOBcomp_1']

#### HE_propanol_water_retry
**L1_query_4** — status: no_results · validation: PASS

**Summary:** No meaningful excess molar enthalpy (Hᴱ) data were found for the binary system 1-propanol + water in the ThermoML database. A direct binary search returned zero blocks. A subsystem search found only one block (DOI: 10.1016/j.fluid.2015.07.053), containing 3 data points all with Hᴱ = 0 kJ/mol at mole fractions of 0.25, 0.50, and 0.75 at 313.15 K; these are the acetic-acid-free boundary of a ternary (propan-1-ol + water + acetic acid) dataset and do not constitute useful binary mixing enthalpy data. A broad search for any Hᴱ blocks involving 1-propanol returned 50 blocks across many partner compounds, but none with water as the second component in a declared binary system. No composition-dependent Hᴱ data spanning the full mole fraction range is available for this system.

**Answer:**

**No meaningful excess molar enthalpy (Hᴱ) data found for the binary system 1-propanol + water in the ThermoML database.**

A comprehensive search was conducted:

1. **Direct binary search** (declared scope) for GLOBcomp_5 (1-propanol) + GLOBcomp_1 (water) with GLOBprop_17 (excess molar enthalpy) returned **zero blocks** — both with and without temperature constraints.

2. **Subsystem search** (scope = "either") found only **one block**: GLOBlit_1766 (DOI: 10.1016/j.fluid.2015.07.053), PROPblock_1, BLKsubsys_1. This is a binary subsystem extracted from a ternary (propan-1-ol + water + acetic acid) dataset. However, it contains only **3 data points**, all with **Hᴱ = 0 kJ/mol** at mole fractions of 0.25, 0.50, and 0.75 — and at **313.15 K**. These zero values represent the acetic-acid-free boundary of the ternary system and do not constitute useful binary mixing enthalpy data.

3. **Broad search** for any Hᴱ blocks involving 1-propanol (without specifying water) returned 50 blocks across many partner compounds, but **none with water** as the second component in a declared binary system.

**Conclusion:** The ThermoML database does not contain excess molar enthalpy data for the 1-propanol + water binary system. No composition-dependent Hᴱ data spanning the full mole fraction range is available for this system.

**Core claims:**
- No meaningful excess molar enthalpy (Hᴱ) data for the binary system 1-propanol + water were found in the ThermoML database; the only related block found (GLOBlit_1766, DOI: 10.1016/j.fluid.2015.07.053) is a binary subsystem extracted from a ternary dataset containing only 3 data points all with Hᴱ = 0 kJ/mol, representing the acetic-acid-free boundary rather than useful binary mixing enthalpy data, and a broad search for any Hᴱ blocks involving 1-propanol returned 50 blocks across many partner compounds but none with water as the second component in a declared binary system.

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### HE_ethanol_water_fullrange
**L1_query_5** — status: success · validation: PASS

**Summary:** Excess molar enthalpy (Hᴱ) for ethanol + water at 298.15 K across the full composition range is reported from GLOBlit_2574 PROPblock_4 (DOI: 10.1016/j.jct.2005.06.018). The block contains 12 data points at 101.0 kPa spanning x(ethanol) = 0.0582 to 0.9. All Hᴱ values are negative (exothermic mixing), with a minimum of −0.770 kJ/mol near x(ethanol) ≈ 0.15. Representative values include −0.492 kJ/mol at x = 0.0582, −0.747 at x = 0.1198, −0.702 at x = 0.25, −0.391 at x = 0.5, −0.271 at x = 0.701, and −0.148 kJ/mol at x = 0.9. The asymmetric minimum shifted toward the water-rich side is characteristic of ethanol–water systems. No other full-range source was found in the database; GLOBlit_528 covers only the extremely dilute regime (x < 0.002) and GLOBlit_6377 has only a single point. A caveat is noted that the source publication title references propanediols, but the block is registered as binary ethanol + water, and the data values are consistent with well-known ethanol–water Hᴱ behavior.

**Answer:**

#### Excess Molar Enthalpy (Hᴱ) for Ethanol + Water at 298.15 K — Full Composition Range

After searching all available binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) excess molar enthalpy (GLOBprop_17) blocks in the ThermoML database, **GLOBlit_2574 PROPblock_4** (DOI: 10.1016/j.jct.2005.06.018) is confirmed as the best available full-range source at 298.15 K.

##### Data Summary

The block contains **12 data points at 298.15 K** spanning x(ethanol) = 0.0582 to 0.9, at a fixed pressure of 101.0 kPa. All Hᴱ values are negative (exothermic mixing), with a minimum (most exothermic) near x ≈ 0.15.

**WM_L1#5_Table#1_(Analysis_L1#5_Answer):**

| *row_id* | *x(ethanol)* | *Hᴱ (kJ/mol)* |
|---|---|---|
| WM_L1#5_Table#1_Row#1 | 「0.0582」 | 「−0.492」 |
| WM_L1#5_Table#1_Row#2 | 「0.1198」 | 「−0.747」 |
| WM_L1#5_Table#1_Row#3 | 「0.15」 | 「−0.770」 |
| WM_L1#5_Table#1_Row#4 | 「0.1837」 | 「−0.767」 |
| WM_L1#5_Table#1_Row#5 | 「0.25」 | 「−0.702」 |
| WM_L1#5_Table#1_Row#6 | 「0.2981」 | 「−0.649」 |
| WM_L1#5_Table#1_Row#7 | 「0.4127」 | 「−0.501」 |
| WM_L1#5_Table#1_Row#8 | 「0.5」 | 「−0.391」 |
| WM_L1#5_Table#1_Row#9 | 「0.607」 | 「−0.323」 |
| WM_L1#5_Table#1_Row#10 | 「0.701」 | 「−0.271」 |
| WM_L1#5_Table#1_Row#11 | 「0.812」 | 「−0.206」 |
| WM_L1#5_Table#1_Row#12 | 「0.9」 | 「−0.148」 |

Source: GLOBlit_2574 :: PROPblock_4 (DOI: 10.1016/j.jct.2005.06.018)

##### Key Observations

- **Composition coverage**: x(ethanol) from 0.0582 to 0.9 — good but not extending to the very dilute water-in-ethanol limit (x → 1) or the most dilute ethanol-in-water region (x < 0.058). The full block (including other temperatures) extends to x = 0.033–0.968.
- **Hᴱ minimum**: The most exothermic mixing occurs at x(ethanol) ≈ 0.15, with Hᴱ = −0.770 kJ/mol. This asymmetric minimum (shifted toward the water-rich side) is characteristic of ethanol–water systems, reflecting the disruption of the water hydrogen-bond network by ethanol molecules.
- **No other full-range source found**: GLOBlit_528 covers only the extremely dilute regime (x < 0.002), and GLOBlit_6377 has only a single point. No additional full-range blocks exist in the database.

##### Note on the Source

The publication (10.1016/j.jct.2005.06.018) title references propanediols, but the block is registered as binary ethanol + water. This compound-mapping caveat was noted in prior context. The data values themselves are consistent with well-known ethanol–water Hᴱ behavior (negative, asymmetric minimum near x ≈ 0.15–0.2, magnitude ~0.7–0.8 kJ/mol at the minimum).

**Core claims:**
- The best available full-range source for excess molar enthalpy (Hᴱ) of ethanol + water at 298.15 K in the ThermoML database is GLOBlit_2574 PROPblock_4 (DOI: 10.1016/j.jct.2005.06.018), containing 12 data points at 101.0 kPa spanning x(ethanol) = 0.0582 to 0.9.
- All reported Hᴱ values at 298.15 K are negative (exothermic mixing), with the most exothermic value of −0.770 kJ/mol occurring at x(ethanol) ≈ 0.15, reflecting an asymmetric minimum shifted toward the water-rich side.
- The composition coverage does not extend to the very dilute ethanol-in-water region (x < 0.058) or the dilute water-in-ethanol limit (x → 1) at 298.15 K, and no other full-range source was found in the database.
- A compound-mapping caveat exists: the source publication title references propanediols, but the block is registered as binary ethanol + water; however, the data values are consistent with well-known ethanol–water Hᴱ behavior.

**Core blocks found:**

**WM_L1#5_Blocks_(Analysis_L1#5_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#5_Table#2 | 「GLOBlit_2574」 | 「PROPblock_4」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for ethanol + water at 298.15 K, 12 data points spanning x(ethanol) = 0.0582 to 0.9, all negative with minimum near x ≈ 0.15.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### query
**L1_query_6** — status: success · validation: PASS

**Summary:** Density data for the binary system 1-propanol + water at 298.15 K and 101.0 kPa, from PROPblock_14 of GLOBlit_11042 (DOI: 10.1021/je700700f). The dataset contains 13 data points spanning the full mole-fraction range x(1-propanol) = 0 to 1. Density decreases monotonically from 997.2 kg/m³ (pure water) to 799.6 kg/m³ (pure 1-propanol). Specific measured compositions and densities include x = 0.0504 (975.1 kg/m³), 0.0993 (953.3), 0.1986 (914.9), 0.2979 (887.2), 0.3949 (866.9), 0.4955 (850.3), 0.5953 (836.9), 0.6995 (825.6), 0.7969 (816.3), 0.8983 (807.7), and 0.9518 (803.5 kg/m³). The full-range coverage is suitable for deriving excess molar volumes V^E, which are expected to be negative across the composition range due to volume contraction from hydrogen-bonding interactions, with a minimum typically near x ≈ 0.3–0.4.

**Answer:**

#### Density Data for 1-Propanol + Water at 298.15 K (for Excess Molar Volume Derivation)

The best block found is **PROPblock_14** from **GLOBlit_11042** (DOI: 10.1021/je700700f), which contains mass density data for the binary system 1-propanol (propan-1-ol) + water at 298.15 K and 101.0 kPa, covering the full mole-fraction range from 0 to 1 with **13 data points**.

##### Complete Data Table

**WM_L1#6_Table#1_(Analysis_L1#6_Answer):**

| *row_id* | *BLKpoint_id* | *x(1-propanol)* | *Pressure (kPa)* | *Temperature (K)* | *Density (kg/m³)* |
|---|---|---|---|---|---|
| WM_L1#6_Table#1_Row#1 | 「BLKpoint_1」 | 「0」 | 「101.0」 | 「298.15」 | 「997.2」 |
| WM_L1#6_Table#1_Row#2 | 「BLKpoint_2」 | 「0.0504」 | 「101.0」 | 「298.15」 | 「975.1」 |
| WM_L1#6_Table#1_Row#3 | 「BLKpoint_3」 | 「0.0993」 | 「101.0」 | 「298.15」 | 「953.3」 |
| WM_L1#6_Table#1_Row#4 | 「BLKpoint_4」 | 「0.1986」 | 「101.0」 | 「298.15」 | 「914.9」 |
| WM_L1#6_Table#1_Row#5 | 「BLKpoint_5」 | 「0.2979」 | 「101.0」 | 「298.15」 | 「887.2」 |
| WM_L1#6_Table#1_Row#6 | 「BLKpoint_6」 | 「0.3949」 | 「101.0」 | 「298.15」 | 「866.9」 |
| WM_L1#6_Table#1_Row#7 | 「BLKpoint_7」 | 「0.4955」 | 「101.0」 | 「298.15」 | 「850.3」 |
| WM_L1#6_Table#1_Row#8 | 「BLKpoint_8」 | 「0.5953」 | 「101.0」 | 「298.15」 | 「836.9」 |
| WM_L1#6_Table#1_Row#9 | 「BLKpoint_9」 | 「0.6995」 | 「101.0」 | 「298.15」 | 「825.6」 |
| WM_L1#6_Table#1_Row#10 | 「BLKpoint_10」 | 「0.7969」 | 「101.0」 | 「298.15」 | 「816.3」 |
| WM_L1#6_Table#1_Row#11 | 「BLKpoint_11」 | 「0.8983」 | 「101.0」 | 「298.15」 | 「807.7」 |
| WM_L1#6_Table#1_Row#12 | 「BLKpoint_12」 | 「0.9518」 | 「101.0」 | 「298.15」 | 「803.5」 |
| WM_L1#6_Table#1_Row#13 | 「BLKpoint_13」 | 「1」 | 「101.0」 | 「298.15」 | 「799.6」 |

##### Key Details
- **Literature:** GLOBlit_11042, DOI 10.1021/je700700f
- **Block:** PROPblock_14 (binary: propan-1-ol + water)
- **Data points:** 13
- **Composition range:** x(1-propanol) = 0 to 1 (full range)
- **Temperature:** 298.15 K (isothermal, all points)
- **Pressure:** 101.0 kPa (all points)
- **Density range:** 799.6 kg/m³ (pure 1-propanol) to 997.2 kg/m³ (pure water)

##### Chemistry Insight for Excess Molar Volume Derivation

The density decreases monotonically from pure water (997.2 kg/m³) to pure 1-propanol (799.6 kg/m³). The excess molar volume V^E can be computed at each composition from:

V^E = V_mix − (x₁V₁* + x₂V₂*)

where V_mix = (x₁M₁ + x₂M₂)/ρ_mix, using the molar masses of 1-propanol and water (these are standard IUPAC molar masses, not from this database). The pure-component molar volumes V₁* and V₂* are obtained from the endpoint densities (BLKpoint_13 and BLKpoint_1). For 1-propanol + water, V^E is expected to be negative across the composition range, reflecting volume contraction due to hydrogen-bonding interactions between the alcohol and water molecules, with a minimum typically near x ≈ 0.3–0.4. The 13-point coverage across the full composition range is well-suited for this derivation.

**Core claims:**
- Mass density data for the binary system 1-propanol + water at 298.15 K and 101.0 kPa are available from PROPblock_14 of GLOBlit_11042 (DOI: 10.1021/je700700f), comprising 13 data points spanning the full mole-fraction range x(1-propanol) = 0 to 1.
- The density decreases monotonically from 997.2 kg/m³ for pure water to 799.6 kg/m³ for pure 1-propanol across the composition range at 298.15 K and 101.0 kPa.
- The 13-point full-range composition coverage is suitable for deriving excess molar volume V^E, which for 1-propanol + water is expected to be negative across the composition range due to volume contraction from hydrogen-bonding interactions, with a minimum typically near x ≈ 0.3–0.4.

**Core blocks found:**

**WM_L1#6_Blocks_(Analysis_L1#6_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#6_Table#2 | 「GLOBlit_11042」 | 「PROPblock_14」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density data for 1-propanol + water at 298.15 K and 101.0 kPa, 13 data points covering x(1-propanol) = 0 to 1, density range 799.6–997.2 kg/m³.」 |

*Not stored here: 3 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_2574 | 10.1016/j.jct.2005.06.018 | PROPblock_4: 27 rows; x=['mole_fraction_<ethanol>']; y=['excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol']
    - BLKprop_1 / GLOBprop_17: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_17: kind=direct; materialize_reference=False; supported=True; units=kJ/mol -> kJ/mol

### Completed Fits
  - MeOH_water_HE [10.1016/j.tca.2006.02.028/PROPblock_1] (methanol, water): RK order=3, R²=0.998432, RMSE=0.008035478840357078, coeffs=[-3.092541, 1.550802, -2.027138, 1.085445]
      response: direct via X = reported X | 0 reference source(s) | kJ/mol -> kJ/mol
      pure refs: methanol=0, water=0 [declared excess property: zero at pure limits]
      fit_csv: $ROOT/data\10_1016_j_tca_2006_02_028_BPROPblock_1_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_tca_2006_02_028_BPROPblock_1_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_tca_2006_02_028_BPROPblock_1_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_tca_2006_02_028_BPROPblock_1_T298.1_excess.png
  - 10.1016/j.jct.2005.06.018/PROPblock_4 (ethanol, water): RK order=4, R²=0.998537, RMSE=0.008367192167912752, coeffs=[-1.601023, 1.734931, -3.19748, 3.113265, -2.361707]
      response: direct via X = reported X | 0 reference source(s) | kJ/mol -> kJ/mol
      pure refs: ethanol=0, water=0 [declared excess property: zero at pure limits]
      fit_csv: $ROOT/data\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_excess.png
  - 10.1021/je700700f/PROPblock_14 (propan-1-ol, water): RK order=5, R²=0.999276, RMSE=4.602814010602905e-09, coeffs=[-3e-06, 1e-06, -1e-06, 0.0, -2e-06, 2e-06]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      route: measured-derived (density_to_molar_volume, exact pointwise) via density_to_molar_volume
      pure refs: propan-1-ol=7.51576e-05, water=1.80656e-05 [block-edges of derived data (water: direct/good, propan-1-ol: direct/good)]
      fit_csv: $ROOT/data\10_1021_je700700f_BPROPblock_14_fit.csv
      excess_csv: $ROOT/data\10_1021_je700700f_BPROPblock_14_excess.csv
      fit_plot: $ROOT/plots\10_1021_je700700f_BPROPblock_14_fit.png
      excess_plot: $ROOT/plots\10_1021_je700700f_BPROPblock_14_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_tca_2006_02_028_BPROPblock_1_T298.1_fit.csv` — RK fit data — 10.1016/j.tca.2006.02.028 PROPblock_1_T298.1
- `$ROOT/data\10_1016_j_tca_2006_02_028_BPROPblock_1_T298.1_excess.csv` — Excess property — 10.1016/j.tca.2006.02.028 PROPblock_1_T298.1
- `$ROOT/data\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2005.06.018 PROPblock_4_T298.1
- `$ROOT/data\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2005.06.018 PROPblock_4_T298.1
- `$ROOT/data\10_1021_je700700f_BPROPblock_14_fit.csv` — RK fit data — 10.1021/je700700f PROPblock_14
- `$ROOT/data\10_1021_je700700f_BPROPblock_14_excess.csv` — Excess property — 10.1021/je700700f PROPblock_14

### plot
- `$ROOT/plots\10_1016_j_tca_2006_02_028_BPROPblock_1_T298.1_fit.png` — RK fit plot — 10.1016/j.tca.2006.02.028 PROPblock_1_T298.1
- `$ROOT/plots\10_1016_j_tca_2006_02_028_BPROPblock_1_T298.1_excess.png` — Excess plot — 10.1016/j.tca.2006.02.028 PROPblock_1_T298.1
- `$ROOT/plots\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2005.06.018 PROPblock_4_T298.1
- `$ROOT/plots\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2005.06.018 PROPblock_4_T298.1
- `$ROOT/plots\10_1021_je700700f_BPROPblock_14_fit.png` — RK fit plot — 10.1021/je700700f PROPblock_14
- `$ROOT/plots\10_1021_je700700f_BPROPblock_14_excess.png` — Excess plot — 10.1021/je700700f PROPblock_14

