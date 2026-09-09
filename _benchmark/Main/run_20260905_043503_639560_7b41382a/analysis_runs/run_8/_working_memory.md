# Working Memory

**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_043503_639560_7b41382a\analysis_runs\run_8`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_2 | ethanol | 0.0 |
| comp | GLOBcomp_1 | water | 0.0 |
| prop | GLOBprop_17 | excessmolarenthalpymolarenthalpyofmixingkjmol |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_2 | molefraction<ethanol> |  |
| constr | GLOBconstr_1 | pressurekpa |  |
| lit | GLOBlit_6377 | 10.1016/j.tca.2017.05.023 |  |

### History
- [query_thermoml]
- [query_thermoml]
- [inspect_block]
- [fit_block] ERROR: Requested x column 'Mole fraction of ethanol' not found in block
- [fit_block]
- [predict_from_rk]

### Query Results
#### query
**L1_query_1** — status: success · validation: PASS

**Summary:** Four ThermoML data blocks were identified for the excess molar enthalpy (HE) of ethanol + water at 298.15 K and 101.0 kPa. GLOBlit_2574::PROPblock_4 (DOI 10.1016/j.jct.2005.06.018) provides 5 data points spanning x(ethanol) = 0.0582–0.9, with HE ranging from −0.767 to −0.148 kJ/mol; the most exothermic mixing occurs near x(ethanol) ≈ 0.18, though a possible compound-mapping issue is flagged because the paper title references propanediols/butanediol. GLOBlit_528::PROPblock_1 (DOI 10.1016/j.fluid.2007.06.007) gives 15 points in the very dilute ethanol region (x(ethanol) = 0.000102–0.001551, HE from −0.01537 to −0.00104 kJ/mol), while GLOBlit_528::PROPblock_2 from the same DOI gives 15 points in the very dilute water region (x(water) = 0.001021–0.015286, HE from −0.02961 to −0.00212 kJ/mol). A fourth block (GLOBlit_6377) contains approximately one data point near 298.15 K. All reported HE values are negative, consistent with exothermic mixing driven by hydrogen-bonding interactions. The GLOBlit_2574 block offers the broadest composition coverage, while the two GLOBlit_528 blocks together provide high-resolution data at both infinite-dilution limits.

**Answer:**

#### Excess Molar Enthalpy (HE) Data for Ethanol + Water at 298.15 K

Four data blocks were found in the ThermoML database for the binary system ethanol (GLOBcomp_2) + water (GLOBcomp_1) containing excess molar enthalpy (GLOBprop_17) data at or near 298.15 K:

---

##### 1. GLOBlit_2574 :: PROPblock_4
- **DOI:** 10.1016/j.jct.2005.06.018
- **Total data points:** 27 (5 at 298.15 K, remainder at 323.15 K)
- **Temperature range:** 298.15–323.15 K
- **Composition range (full block):** x(ethanol) = 0.033–0.968
- **Pressure:** 101.0 kPa (fixed)
- **HE range:** −0.77 to −0.018 kJ/mol

**298.15 K data points:**

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *HE (kJ/mol)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.0582」 | 「−0.492」 |
| WM_L1#1_Table#1_Row#2 | 「0.1198」 | 「−0.747」 |
| WM_L1#1_Table#1_Row#3 | 「0.1837」 | 「−0.767」 |
| WM_L1#1_Table#1_Row#4 | 「0.5」 | 「−0.391」 |
| WM_L1#1_Table#1_Row#5 | 「0.9」 | 「−0.148」 |

This block offers the **widest composition coverage** at 298.15 K (from dilute ethanol to ethanol-rich), though with only 5 data points at that temperature. The minimum HE (most exothermic mixing) occurs near x(ethanol) ≈ 0.18, consistent with the known asymmetric HE curve for ethanol–water.

⚠️ **Note:** The paper title references propanediols/butanediol, not ethanol — possible compound-mapping issue; verify against the original publication.

---

##### 2. GLOBlit_528 :: PROPblock_1
- **DOI:** 10.1016/j.fluid.2007.06.007
- **Data points:** 15 (all at 298.15 K)
- **Temperature:** 298.15 K (fixed)
- **Pressure:** 101.0 kPa (fixed)
- **Composition range:** x(ethanol) = 0.000102–0.001551 (very dilute ethanol)
- **HE range:** −0.01537 to −0.00104 kJ/mol

This block covers the **infinite-dilution region of ethanol in water**, with a nearly linear, monotonically decreasing HE vs. composition relationship — useful for extracting partial molar excess enthalpy at infinite dilution.

---

##### 3. GLOBlit_528 :: PROPblock_2
- **DOI:** 10.1016/j.fluid.2007.06.007
- **Data points:** 15 (all at 298.15 K)
- **Temperature:** 298.15 K (fixed)
- **Pressure:** 101.0 kPa (fixed)
- **Composition range:** x(water) = 0.001021–0.015286 (very dilute water, i.e., ethanol-rich side)
- **HE range:** −0.02961 to −0.00212 kJ/mol

This block covers the **infinite-dilution region of water in ethanol**, complementing PROPblock_1 on the opposite end of the composition range.

---

##### 4. GLOBlit_6377 (single-point block)
- Reported in the initial search as containing a single data point near 298.15 K. Not inspected in detail due to its limited scope.

---

##### Summary & Recommendation

**WM_L1#1_Table#2_(Analysis_L1#1_Answer):**

| *row_id* | *Block* | *GLOBlit* | *DOI* | *Points at 298.15 K* | *Composition range* | *Best for* |
|---|---|---|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「PROPblock_4」 | 「GLOBlit_2574」 | 「10.1016/j.jct.2005.06.018」 | 「5」 | 「x(ethanol) = 0.058–0.9」 | 「Full composition range」 |
| WM_L1#1_Table#2_Row#2 | 「PROPblock_1」 | 「GLOBlit_528」 | 「10.1016/j.fluid.2007.06.007」 | 「15」 | 「x(ethanol) = 0.0001–0.0016」 | 「Dilute ethanol limit」 |
| WM_L1#1_Table#2_Row#3 | 「PROPblock_2」 | 「GLOBlit_528」 | 「10.1016/j.fluid.2007.06.007」 | 「15」 | 「x(water) = 0.001–0.015」 | 「Dilute water limit」 |
| WM_L1#1_Table#2_Row#4 | 「(single pt)」 | 「GLOBlit_6377」 | 「—」 | 「~1」 | 「—」 | 「Limited use」 |

**GLOBlit_2574::PROPblock_4** provides the broadest composition coverage at 298.15 K but has only 5 points. The two **GLOBlit_528** blocks together provide 15 (PROPblock_1) + 15 (PROPblock_2) high-resolution data points at 298.15 K, but are restricted to the two dilute extremes. All measured HE values are negative (exothermic mixing), consistent with the strong hydrogen-bonding interactions between ethanol and water.

**Core claims:**
- Four ThermoML data blocks were identified for excess molar enthalpy (HE) of ethanol + water at 298.15 K and 101.0 kPa: GLOBlit_2574::PROPblock_4 (5 points spanning x(ethanol) = 0.058–0.9, HE from −0.767 to −0.148 kJ/mol), GLOBlit_528::PROPblock_1 (15 points in the very dilute ethanol region, x(ethanol) = 0.000102–0.001551, HE from −0.01537 to −0.00104 kJ/mol), GLOBlit_528::PROPblock_2 (15 points in the very dilute water region, x(water) = 0.001021–0.015286, HE from −0.02961 to −0.00212 kJ/mol), and a single-point block from GLOBlit_6377.
- All measured HE values are negative (exothermic mixing), consistent with strong hydrogen-bonding interactions between ethanol and water.
- In the broad-composition block (GLOBlit_2574::PROPblock_4), the most exothermic HE value at 298.15 K is −0.767 kJ/mol near x(ethanol) ≈ 0.18, reflecting the known asymmetric HE curve for ethanol–water.
- A possible compound-mapping issue exists for GLOBlit_2574::PROPblock_4, as the associated paper title references propanediols/butanediol rather than ethanol; verification against the original publication is recommended.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_2574」 | 「PROPblock_4」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for ethanol + water; 27 points over 298.15–323.15 K (5 at 298.15 K), x(ethanol) = 0.033–0.968, HE = −0.77 to −0.018 kJ/mol, 101.0 kPa.」 |
| WM_L1#1_Table#4 | 「GLOBlit_528」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for ethanol + water at 298.15 K; 15 points in the dilute-ethanol region, x(ethanol) = 0.000102–0.001551, HE = −0.01537 to −0.00104 kJ/mol, 101.0 kPa.」 |
| WM_L1#1_Table#5 | 「GLOBlit_528」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for ethanol + water at 298.15 K; 15 points in the dilute-water (ethanol-rich) region, x(water) = 0.001021–0.015286, HE = −0.02961 to −0.00212 kJ/mol, 101.0 kPa.」 |

*Not stored here: 3 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### query
**L1_query_2** — status: success · validation: PASS

**Summary:** In the ThermoML database, excess molar enthalpy (HE) data for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system near 298.15 K were found in three sources: GLOBlit_528 (DOI 10.1016/j.fluid.2007.06.007), GLOBlit_2574 (DOI 10.1016/j.jct.2005.06.018), and GLOBlit_6377 (DOI 10.1016/j.tca.2017.05.023). GLOBlit_2574::PROPblock_4 offers the broadest composition coverage with 12 points at 298.15 K and 101.0 kPa spanning x(ethanol) = 0.0582–0.9, showing all-negative HE values with a minimum of −0.77 kJ/mol at x(ethanol) ≈ 0.15, consistent with the known asymmetric exothermic mixing curve; however, the paper title references propanediols/butanediol rather than ethanol, flagging a possible compound-mapping issue. GLOBlit_6377::PROPblock_1 provides a single point at 298.15 K (x(ethanol) = 0.102, HE = −0.70659 kJ/mol, 100 kPa), consistent with the GLOBlit_2574 data. GLOBlit_528 contains two blocks of 15 points each at 298.15 K and 101.0 kPa covering the infinite-dilution regions: PROPblock_1 for very dilute ethanol in water (x(ethanol) = 0.000102–0.001551, HE from −0.00104 to −0.01537 kJ/mol) and PROPblock_2 for very dilute water in ethanol (x(water) = 0.001021–0.015286, HE from −0.00212 to −0.02961 kJ/mol). No other DOIs were found for this system and property.

**Answer:**

Here are all the excess molar enthalpy (HE) data blocks found for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system near 298.15 K in the ThermoML database:

#### Summary of All HE Blocks Found

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *DOI* | *GLOBlit* | *Block* | *Total pts* | *Pts at 298.15 K* | *Composition range* | *Notes* |
|---|---|---|---|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「10.1016/j.fluid.2007.06.007」 | 「GLOBlit_528」 | 「PROPblock_1」 | 「15」 | 「15」 | 「x(ethanol) 0.000102–0.001551」 | 「Very dilute ethanol in water only」 |
| WM_L1#2_Table#1_Row#2 | 「10.1016/j.fluid.2007.06.007」 | 「GLOBlit_528」 | 「PROPblock_2」 | 「15」 | 「15」 | 「x(water) 0.001021–0.015286」 | 「Very dilute water in ethanol only」 |
| WM_L1#2_Table#1_Row#3 | 「10.1016/j.jct.2005.06.018」 | 「GLOBlit_2574」 | 「PROPblock_4」 | 「27」 | 「12」 | 「x(ethanol) 0.0582–0.9」 | 「Broad composition coverage; ⚠️ paper title references propanediols/butanediol — possible compound-mapping issue」 |
| WM_L1#2_Table#1_Row#4 | 「10.1016/j.tca.2017.05.023」 | 「GLOBlit_6377」 | 「PROPblock_1」 | 「1」 | 「1」 | 「x(ethanol) 0.102 only」 | 「Single data point」 |

#### Detailed Findings

##### GLOBlit_2574::PROPblock_4 — Best Composition Coverage at 298.15 K
This block contains **12 data points at 298.15 K**, spanning x(ethanol) = 0.0582 to 0.9, at 101.0 kPa:

**WM_L1#2_Table#2_(Analysis_L1#2_Answer):**

| *row_id* | *x(ethanol)* | *HE (kJ/mol)* |
|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「0.0582」 | 「−0.492」 |
| WM_L1#2_Table#2_Row#2 | 「0.1198」 | 「−0.747」 |
| WM_L1#2_Table#2_Row#3 | 「0.15」 | 「−0.77」 |
| WM_L1#2_Table#2_Row#4 | 「0.1837」 | 「−0.767」 |
| WM_L1#2_Table#2_Row#5 | 「0.25」 | 「−0.702」 |
| WM_L1#2_Table#2_Row#6 | 「0.2981」 | 「−0.649」 |
| WM_L1#2_Table#2_Row#7 | 「0.4127」 | 「−0.501」 |
| WM_L1#2_Table#2_Row#8 | 「0.5」 | 「−0.391」 |
| WM_L1#2_Table#2_Row#9 | 「0.607」 | 「−0.323」 |
| WM_L1#2_Table#2_Row#10 | 「0.701」 | 「−0.271」 |
| WM_L1#2_Table#2_Row#11 | 「0.812」 | 「−0.206」 |
| WM_L1#2_Table#2_Row#12 | 「0.9」 | 「−0.148」 |

The minimum HE is −0.77 kJ/mol at x(ethanol) ≈ 0.15, consistent with the well-known asymmetric exothermic mixing curve for ethanol + water. However, note the caution flag: the paper title in the database references propanediols/butanediol rather than ethanol, so this data should be verified against the original publication.

##### GLOBlit_6377::PROPblock_1 — Single Point
DOI: 10.1016/j.tca.2017.05.023. Contains only **1 data point** at 298.15 K: x(ethanol) = 0.102, HE = −0.70659 kJ/mol, at 100 kPa. This is consistent with the GLOBlit_2574::PROPblock_4 data, which gives −0.747 kJ/mol at x = 0.1198 (a nearby but not identical composition).

##### GLOBlit_528::PROPblock_1 — Dilute Ethanol in Water
DOI: 10.1016/j.fluid.2007.06.007. Contains 15 points at 298.15 K covering x(ethanol) = 0.000102–0.001551 at 101.0 kPa. HE ranges from −0.00104 to −0.01537 kJ/mol. This block covers only the very dilute ethanol end, useful for deriving partial molar excess enthalpies at infinite dilution.

##### GLOBlit_528::PROPblock_2 — Dilute Water in Ethanol
Same DOI. Contains 15 points at 298.15 K covering x(water) = 0.001021–0.015286 at 101.0 kPa. HE ranges from −0.00212 to −0.02961 kJ/mol. This block covers only the very dilute water-in-ethanol end.

##### Conclusion
No additional DOIs beyond GLOBlit_528, GLOBlit_2574, and GLOBlit_6377 were found in the database for HE of ethanol + water. GLOBlit_2574::PROPblock_4 provides the broadest composition coverage with 12 points at 298.15 K spanning x(ethanol) = 0.0582–0.9. The GLOBlit_528 blocks complement this with high-resolution data in the infinite-dilution regions at both ends.

**Core claims:**
- Three DOIs (GLOBlit_528, GLOBlit_2574, GLOBlit_6377) were found in the ThermoML database containing excess molar enthalpy (HE) data for the ethanol + water binary system near 298.15 K.
- GLOBlit_2574::PROPblock_4 provides the broadest composition coverage with 12 data points at 298.15 K spanning x(ethanol) = 0.0582–0.9 at 101.0 kPa, showing all-negative HE values with a minimum of −0.77 kJ/mol at x(ethanol) ≈ 0.15, consistent with the known asymmetric exothermic mixing curve for ethanol + water.
- A caution flag applies to GLOBlit_2574::PROPblock_4: the paper title in the database references propanediols/butanediol rather than ethanol, so the compound mapping should be verified against the original publication (DOI 10.1016/j.jct.2005.06.018).
- GLOBlit_6377::PROPblock_1 provides a single data point at 298.15 K: x(ethanol) = 0.102, HE = −0.70659 kJ/mol at 100 kPa, which is consistent with the GLOBlit_2574 data (−0.747 kJ/mol at x = 0.1198).
- GLOBlit_528 (DOI 10.1016/j.fluid.2007.06.007) provides high-resolution HE data in the infinite-dilution regions at both ends: 15 points for dilute ethanol in water (x(ethanol) = 0.000102–0.001551) and 15 points for dilute water in ethanol (x(water) = 0.001021–0.015286), all at 298.15 K and 101.0 kPa.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#3 | 「GLOBlit_528」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for dilute ethanol in water at 298.15 K; 15 points, x(ethanol) 0.000102–0.001551.」 |
| WM_L1#2_Table#4 | 「GLOBlit_528」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for dilute water in ethanol at 298.15 K; 15 points, x(water) 0.001021–0.015286.」 |
| WM_L1#2_Table#5 | 「GLOBlit_2574」 | 「PROPblock_4」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for ethanol + water; 12 points at 298.15 K spanning x(ethanol) 0.0582–0.9 at 101.0 kPa. Broadest composition coverage found.」 |
| WM_L1#2_Table#6 | 「GLOBlit_6377」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_17」 | 「Excess molar enthalpy for ethanol + water; single data point at 298.15 K, x(ethanol) = 0.102, HE = −0.70659 kJ/mol at 100 kPa.」 |

*Not stored here: 4 verbatim data_inspections table(s); 1 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_2574 | 10.1016/j.jct.2005.06.018 | PROPblock_4: 27 rows; x=['mole_fraction_<ethanol>']; y=['excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol']
    - BLKprop_1 / GLOBprop_17: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_17: kind=direct; materialize_reference=False; supported=True; units=kJ/mol -> kJ/mol

### Completed Fits
  - 10.1016/j.jct.2005.06.018/PROPblock_4 (ethanol, water): RK order=4, R²=0.998537, RMSE=0.008367192167912752, coeffs=[-1.601023, 1.734931, -3.19748, 3.113265, -2.361707]
      response: direct via X = reported X | 0 reference source(s) | kJ/mol -> kJ/mol
      pure refs: ethanol=0, water=0 [declared excess property: zero at pure limits]
      fit_csv: $ROOT/data\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_fit.csv` — RK fit data — 10.1016/j.jct.2005.06.018 PROPblock_4_T298.1
- `$ROOT/data\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_excess.csv` — Excess property — 10.1016/j.jct.2005.06.018 PROPblock_4_T298.1

### plot
- `$ROOT/plots\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_fit.png` — RK fit plot — 10.1016/j.jct.2005.06.018 PROPblock_4_T298.1
- `$ROOT/plots\10_1016_j_jct_2005_06_018_BPROPblock_4_T298.1_excess.png` — Excess plot — 10.1016/j.jct.2005.06.018 PROPblock_4_T298.1

