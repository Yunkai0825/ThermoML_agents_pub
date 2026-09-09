# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|
| prop | GLOBprop_8 | speed_of_sound_m_s | Speed of sound, m/s |
| comp | GLOBcomp_53 | 2-aminoacetic_acid | 2-aminoacetic acid |
| comp | GLOBcomp_26 | sodium_chloride | sodium chloride |
| comp | GLOBcomp_120 | d-sucrose | D-sucrose |
| comp | GLOBcomp_90 | d-glucose | D-glucose |
| comp | GLOBcomp_41 | potassium_chloride | potassium chloride |
| comp | GLOBcomp_74 | (s)-2-aminopropanoic_acid | (S)-2-aminopropanoic acid |
| comp | GLOBcomp_116 | l-valine | L-valine |
| comp | GLOBcomp_233 | potassium_nitrate | potassium nitrate |
| prop | GLOBprop_1 | mass_density_kg_m3 | Mass density, kg/m3 |
| comp | GLOBcomp_2 | ethanol | ethanol |
| comp | GLOBcomp_81 | n-methyldiethanolamine | N-methyldiethanolamine |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|
| lit | GLOBlit_9601 | 2011-sim-cib-0 | 10.1021/je200527t |
| lit | GLOBlit_5265 | 2018-cib--0 | 10.1016/j.jct.2018.05.032 |
| lit | GLOBlit_4052 | 2014-cib--0 | 10.1016/j.jct.2013.11.014 |
| lit | GLOBlit_3034 | 2009-cib-hne-1 | 10.1016/j.jct.2008.11.006 |
| lit | GLOBlit_2432 | 2004-hyn-hne-0 | 10.1016/j.jct.2004.07.019 |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Assess breadth of speed-of-sound data for aqueous mixtures → stored as L1_query_1 · validation: PASS
- [L1] Assess breadth of mass density (GLOBprop_1) data for aqueous binary mixtures (water + one co-solute) to compare against  → stored as L1_query_2 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** The ThermoML database contains speed-of-sound data for aqueous binary mixtures (water + one co-solute) spanning 295 distinct literature sources, 753 data blocks, and 30,819 total data points. The temperature range covered is 273.15–596.3 K and the pressure range is 100.0–120,000.0 kPa (approximately 1 atm to 1,200 atm). Approximately 75–80 distinct non-water co-solutes are identified in a partial registry search, with the true total across all 753 blocks being larger. The chemical diversity includes amino acids (e.g., glycine, L-alanine, L-valine), sugars (D-sucrose, D-glucose), inorganic salts (NaCl, KCl, KNO₃), organic solvents (DMSO, acetonitrile), alcohols (propan-1-ol), glycols (1,2-ethanediol), amides (formamide), ionic liquids (1-butyl-3-methylimidazolium bromide), and alkanolamines (N-methyldiethanolamine). The five largest literature sources by data volume are GLOBlit_5043 (961 points), GLOBlit_5201 (712 points), GLOBlit_8239 (675 points), GLOBlit_10102 (657 points), and GLOBlit_9821 (598 points). This breadth makes the dataset suitable for validating acoustic models across different solute–water interaction regimes including hydrophobic, electrostatic, and hydrogen-bonding interactions, and for deriving isentropic compressibilities and testing equation-of-state predictions in aqueous systems.

**Answer:**

#### Speed of Sound in Aqueous Binary Mixtures — Database Breadth Assessment

##### Aggregate Statistics

**WM_L1_Q1_Table#1_(Query_L1_Q1_Answer):**

| *row_id* | *Metric* | *Value* |
|---|---|---|
| WM_L1_Q1_Table#1_Row#1 | 「Distinct literature sources (GLOBlit_N)」 | 「**295**」 |
| WM_L1_Q1_Table#1_Row#2 | 「Total data blocks」 | 「**753**」 |
| WM_L1_Q1_Table#1_Row#3 | 「Total data points」 | 「**30,819**」 |
| WM_L1_Q1_Table#1_Row#4 | 「Temperature range」 | 「**273.15 – 596.3 K**」 |
| WM_L1_Q1_Table#1_Row#5 | 「Pressure range」 | 「**100.0 – 120,000.0 kPa** (≈ 1 atm to 1,200 atm)」 |
| WM_L1_Q1_Table#1_Row#6 | 「Property」 | 「Speed of sound (GLOBprop_8), m/s」 |
| WM_L1_Q1_Table#1_Row#7 | 「System type」 | 「Binary (water + one co-solute)」 |

##### Distinct Co-solute Compounds

A registry search capped at 100 blocks already returned approximately **75–80 distinct non-water co-solutes**; the true total across all 753 blocks is larger. The database covers a remarkably diverse chemical space — amino acids, sugars, electrolytes, organic solvents, ionic liquids, surfactants, and amines.

##### Representative Co-solute Compounds (15 examples)

**WM_L1_Q1_Table#2_(Query_L1_Q1_Answer):**

| *row_id* | *#* | *Co-solute* | *GLOBcomp_N* | *Chemical class* | *Example literature* |
|---|---|---|---|---|---|
| WM_L1_Q1_Table#2_Row#1 | 「1」 | 「2-Aminoacetic acid (glycine)」 | 「GLOBcomp_53」 | 「Amino acid」 | 「GLOBlit_173」 |
| WM_L1_Q1_Table#2_Row#2 | 「2」 | 「Sodium chloride」 | 「GLOBcomp_26」 | 「Inorganic salt」 | 「—」 |
| WM_L1_Q1_Table#2_Row#3 | 「3」 | 「D-Sucrose」 | 「GLOBcomp_120」 | 「Sugar」 | 「—」 |
| WM_L1_Q1_Table#2_Row#4 | 「4」 | 「D-Glucose」 | 「GLOBcomp_90」 | 「Sugar」 | 「GLOBlit_3319」 |
| WM_L1_Q1_Table#2_Row#5 | 「5」 | 「Potassium chloride」 | 「GLOBcomp_41」 | 「Inorganic salt」 | 「GLOBlit_67」 |
| WM_L1_Q1_Table#2_Row#6 | 「6」 | 「(S)-2-Aminopropanoic acid (L-alanine)」 | 「GLOBcomp_74」 | 「Amino acid」 | 「—」 |
| WM_L1_Q1_Table#2_Row#7 | 「7」 | 「L-Valine」 | 「GLOBcomp_116」 | 「Amino acid」 | 「—」 |
| WM_L1_Q1_Table#2_Row#8 | 「8」 | 「Potassium nitrate」 | 「GLOBcomp_233」 | 「Inorganic salt」 | 「GLOBlit_67」 |
| WM_L1_Q1_Table#2_Row#9 | 「9」 | 「Dimethyl sulfoxide」 | 「—」 | 「Organic solvent」 | 「GLOBlit_2652」 |
| WM_L1_Q1_Table#2_Row#10 | 「10」 | 「Propan-1-ol」 | 「—」 | 「Alcohol」 | 「GLOBlit_555」 |
| WM_L1_Q1_Table#2_Row#11 | 「11」 | 「1-Butyl-3-methylimidazolium bromide」 | 「—」 | 「Ionic liquid」 | 「GLOBlit_2492」 |
| WM_L1_Q1_Table#2_Row#12 | 「12」 | 「Formamide」 | 「—」 | 「Amide」 | 「GLOBlit_2834」 |
| WM_L1_Q1_Table#2_Row#13 | 「13」 | 「1,2-Ethanediol」 | 「—」 | 「Glycol」 | 「GLOBlit_2831」 |
| WM_L1_Q1_Table#2_Row#14 | 「14」 | 「Acetonitrile」 | 「—」 | 「Organic solvent」 | 「GLOBlit_2736」 |
| WM_L1_Q1_Table#2_Row#15 | 「15」 | 「N-Methyldiethanolamine」 | 「—」 | 「Alkanolamine」 | 「GLOBlit_2625」 |

##### Top 5 Literature Sources by Data Volume

**WM_L1_Q1_Table#3_(Query_L1_Q1_Answer):**

| *row_id* | *GLOBlit_N* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|---|
| WM_L1_Q1_Table#3_Row#1 | 「GLOBlit_5043」 | 「10.1016/j.jct.2017.06.001」 | 「1」 | 「961」 |
| WM_L1_Q1_Table#3_Row#2 | 「GLOBlit_5201」 | 「10.1016/j.jct.2018.02.022」 | 「5」 | 「712」 |
| WM_L1_Q1_Table#3_Row#3 | 「GLOBlit_8239」 | 「10.1021/je0340755」 | 「6」 | 「675」 |
| WM_L1_Q1_Table#3_Row#4 | 「GLOBlit_10102」 | 「10.1021/je4001203」 | 「5」 | 「657」 |
| WM_L1_Q1_Table#3_Row#5 | 「GLOBlit_9821」 | 「10.1021/je300175w」 | 「7」 | 「598」 |

##### Chemistry Context

The speed-of-sound dataset for aqueous binaries is substantial (753 blocks, ~31 k points, 295 papers) and spans a wide thermodynamic window — from near-freezing temperatures up to 596.3 K and pressures up to 1,200 atm. The chemical diversity is notable: electrolytes (NaCl, KCl, KNO₃), biologically relevant solutes (amino acids, sugars), industrial solvents (DMSO, acetonitrile, glycols), alkanolamines (MDEA), ionic liquids, and surfactants are all represented. This breadth makes the dataset well-suited for validating acoustic models across different solute–water interaction regimes (hydrophobic, electrostatic, hydrogen-bonding).

Compared to density data (which typically has even larger coverage in ThermoML), speed-of-sound data is somewhat less abundant but still provides a strong validation basis, especially for deriving isentropic compressibilities and testing equation-of-state predictions in aqueous systems.

**Core claims:**
- The ThermoML database contains speed-of-sound data for aqueous binary mixtures spanning 295 distinct literature sources, 753 data blocks, and 30,819 data points.
- The dataset covers a temperature range of 273.15 – 596.3 K and a pressure range of 100.0 – 120,000.0 kPa (approximately 1 atm to 1,200 atm).
- The chemical diversity of co-solutes is broad, encompassing approximately 75–80 or more distinct non-water co-solutes including amino acids, sugars, electrolytes, organic solvents, ionic liquids, surfactants, and alkanolamines.
- This breadth of solute classes (hydrophobic, electrostatic, hydrogen-bonding interaction regimes) makes the dataset well-suited for validating acoustic models and deriving isentropic compressibilities in aqueous systems.
- Compared to density data in ThermoML, speed-of-sound data is somewhat less abundant but still provides a strong validation basis for equation-of-state predictions.

*Not stored here: 9 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: success · validation: PASS

**Summary:** Mass density (kg/m³) data for aqueous binary mixtures in ThermoML spans 1,104 literature sources, 2,558 data blocks, and 132,045 data points, covering 253.15–673.15 K and 6.3–387,800.0 kPa, with at least 79 distinct non-water co-solutes identified from a partial registry search and likely several hundred total. The top co-solutes by number of data targets are sodium chloride (57 targets), glycine (41), D-glucose (33), potassium chloride (31), ethanol (29), N-methyldiethanolamine (28), and D-sucrose (25). Co-solute classes include inorganic salts, amino acids, sugars, alcohols, alkanolamines, ionic liquids, organic acids, transition-metal salts, phosphate salts, heterocyclic compounds, phenols, and buffer compounds. Compared with speed-of-sound data for the same system type (295 sources, 753 blocks, 30,819 points, 273.15–596.3 K, 100.0–120,000 kPa), mass density is roughly 3–4 times more abundant by every metric, with a wider thermodynamic window extending ~20 K lower, ~77 K higher, and to ~3.2× higher pressure. The top five literature sources by data volume are DOI 10.1021/je200527t (2,991 points), 10.1016/j.jct.2018.05.032 (2,478), 10.1016/j.jct.2013.11.014 (2,319), 10.1016/j.jct.2008.11.006 (2,226), and 10.1016/j.jct.2004.07.019 (2,146). The disparity reflects that density is the most commonly measured thermophysical property and is routinely co-reported, whereas speed-of-sound measurements require specialized acoustic instrumentation; nonetheless the speed-of-sound dataset remains substantial for validating acoustic models, isentropic compressibility derivations, and equation-of-state predictions.

**Answer:**

#### Mass Density in Aqueous Binary Mixtures — Database Breadth Assessment

##### Aggregate Statistics

**WM_L1_Q2_Table#1_(Query_L1_Q2_Answer):**

| *row_id* | *Metric* | *Value* |
|---|---|---|
| WM_L1_Q2_Table#1_Row#1 | 「Distinct literature sources (GLOBlit_N)」 | 「**1,104**」 |
| WM_L1_Q2_Table#1_Row#2 | 「Total data blocks」 | 「**2,558**」 |
| WM_L1_Q2_Table#1_Row#3 | 「Total data points」 | 「**132,045**」 |
| WM_L1_Q2_Table#1_Row#4 | 「Temperature range」 | 「**253.15 – 673.15 K**」 |
| WM_L1_Q2_Table#1_Row#5 | 「Pressure range」 | 「**6.3 – 387,800.0 kPa** (≈ 0.06 atm to 3,830 atm)」 |
| WM_L1_Q2_Table#1_Row#6 | 「Property」 | 「Mass density (GLOBprop_1), kg/m³」 |
| WM_L1_Q2_Table#1_Row#7 | 「System type」 | 「Binary (water + one co-solute)」 |

##### Distinct Co-solute Compounds

A registry search capped at 100 blocks already returned **79 distinct non-water co-solutes**; with 2,558 total blocks the true number is likely **several hundred** distinct co-solutes — far exceeding the ~75–80 identified for speed of sound.

##### Top 10 Co-solutes by Number of Data Targets

**WM_L1_Q2_Table#2_(Query_L1_Q2_Answer):**

| *row_id* | *#* | *Co-solute* | *GLOBcomp_N* | *Chemical class* | *Targets* |
|---|---|---|---|---|---|
| WM_L1_Q2_Table#2_Row#1 | 「1」 | 「Sodium chloride」 | 「GLOBcomp_26」 | 「Inorganic salt」 | 「57」 |
| WM_L1_Q2_Table#2_Row#2 | 「2」 | 「2-Aminoacetic acid (glycine)」 | 「GLOBcomp_53」 | 「Amino acid」 | 「41」 |
| WM_L1_Q2_Table#2_Row#3 | 「3」 | 「D-Glucose」 | 「GLOBcomp_90」 | 「Sugar」 | 「33」 |
| WM_L1_Q2_Table#2_Row#4 | 「4」 | 「Potassium chloride」 | 「GLOBcomp_41」 | 「Inorganic salt」 | 「31」 |
| WM_L1_Q2_Table#2_Row#5 | 「5」 | 「Ethanol」 | 「GLOBcomp_2」 | 「Alcohol」 | 「29」 |
| WM_L1_Q2_Table#2_Row#6 | 「6」 | 「N-Methyldiethanolamine」 | 「GLOBcomp_81」 | 「Alkanolamine」 | 「28」 |
| WM_L1_Q2_Table#2_Row#7 | 「7」 | 「D-Sucrose」 | 「GLOBcomp_120」 | 「Sugar」 | 「25」 |
| WM_L1_Q2_Table#2_Row#8 | 「8」 | 「Ammonia」 | 「—」 | 「Inorganic base」 | 「≥2」 |
| WM_L1_Q2_Table#2_Row#9 | 「9」 | 「Methanol」 | 「—」 | 「Alcohol」 | 「≥4」 |
| WM_L1_Q2_Table#2_Row#10 | 「10」 | 「Propan-1-ol」 | 「—」 | 「Alcohol」 | 「≥2」 |

Additional co-solute classes identified in the registry include: ionic liquids (1-ethyl-3-methylimidazolium tetrafluoroborate, 1-butyl-3-methylimidazolium tetrafluoroborate, 1-hexyl-3-methylimidazolium tetrafluoroborate, 1-ethyl-3-methylimidazolium diethyl phosphate, 1-ethyl-3-methylimidazolium ethyl sulfate, 1,3-dimethylimidazolium chloride), organic acids (cis-1,4-butenedioic acid, 2,3-dihydroxybutanedioic acid), amino acids (4-aminobutanoic acid, L-glutamic acid hydrochloride), sugars ((+)-galactose), transition-metal salts (copper sulfate, copper dinitrate, nickel chloride), phosphate salts (disodium hydrogen phosphate, trisodium phosphate), heterocyclic compounds (1,3-dioxolane), phenols (1,3-benzenediol), and buffer compounds (2-amino-2-(hydroxymethyl)-1,3-propanediol).

##### Top 5 Literature Sources by Data Volume

**WM_L1_Q2_Table#3_(Query_L1_Q2_Answer):**

| *row_id* | *GLOBlit_N* | *DOI* | *Blocks* | *Points* |
|---|---|---|---|---|
| WM_L1_Q2_Table#3_Row#1 | 「GLOBlit_9601」 | 「10.1021/je200527t」 | 「5」 | 「2,991」 |
| WM_L1_Q2_Table#3_Row#2 | 「GLOBlit_5265」 | 「10.1016/j.jct.2018.05.032」 | 「5」 | 「2,478」 |
| WM_L1_Q2_Table#3_Row#3 | 「GLOBlit_4052」 | 「10.1016/j.jct.2013.11.014」 | 「4」 | 「2,319」 |
| WM_L1_Q2_Table#3_Row#4 | 「GLOBlit_3034」 | 「10.1016/j.jct.2008.11.006」 | 「6」 | 「2,226」 |
| WM_L1_Q2_Table#3_Row#5 | 「GLOBlit_2432」 | 「10.1016/j.jct.2004.07.019」 | 「4」 | 「2,146」 |

##### Comparison: Mass Density vs. Speed of Sound for Aqueous Binaries

**WM_L1_Q2_Table#4_(Query_L1_Q2_Answer):**

| *row_id* | *Metric* | *Mass Density (GLOBprop_1)* | *Speed of Sound (GLOBprop_8)* | *Ratio (density / SoS)* |
|---|---|---|---|---|
| WM_L1_Q2_Table#4_Row#1 | 「Literature sources」 | 「1,104」 | 「295」 | 「~3.7×」 |
| WM_L1_Q2_Table#4_Row#2 | 「Data blocks」 | 「2,558」 | 「753」 | 「~3.4×」 |
| WM_L1_Q2_Table#4_Row#3 | 「Data points」 | 「132,045」 | 「30,819」 | 「~4.3×」 |
| WM_L1_Q2_Table#4_Row#4 | 「Temperature range (K)」 | 「253.15 – 673.15」 | 「273.15 – 596.3」 | 「Wider by ~20 K low, ~77 K high」 |
| WM_L1_Q2_Table#4_Row#5 | 「Pressure range (kPa)」 | 「6.3 – 387,800」 | 「100.0 – 120,000」 | 「~3.2× wider upper bound」 |
| WM_L1_Q2_Table#4_Row#6 | 「Distinct co-solutes (lower bound)」 | 「≥79 (from 100 blocks); likely several hundred total」 | 「~75–80 (from 100 blocks)」 | 「Substantially more for density」 |

##### Chemistry Context

Mass density data for aqueous binary mixtures in ThermoML is roughly **3–4 times more abundant** than speed-of-sound data by every metric — literature sources, blocks, and data points. The thermodynamic window is also wider, extending to lower temperatures (253 K vs. 273 K), higher temperatures (673 K vs. 596 K), and much higher pressures (387,800 kPa ≈ 3,830 atm vs. 120,000 kPa ≈ 1,200 atm). The chemical diversity of co-solutes is substantially greater for density, with likely several hundred distinct non-water co-solutes across the full 2,558 blocks.

Despite this disparity, the speed-of-sound dataset (753 blocks, ~31k points, 295 papers) remains substantial and covers a broad chemical space including amino acids, sugars, electrolytes, organic solvents, ionic liquids, and alkanolamines. The ~4× gap in data volume is expected: density is the most commonly measured thermophysical property and is routinely reported alongside other measurements, whereas speed-of-sound measurements require specialized acoustic instrumentation (e.g., ultrasonic pulse-echo or sing-around techniques). Nevertheless, the speed-of-sound dataset provides a strong validation basis for acoustic models, isentropic compressibility derivations, and equation-of-state predictions in aqueous systems.

**Core claims:**
- Mass density data for aqueous binary mixtures in ThermoML encompasses 1,104 distinct literature sources, 2,558 data blocks, and 132,045 data points, spanning a temperature range of 253.15–673.15 K and a pressure range of 6.3–387,800.0 kPa.
- At least 79 distinct non-water co-solutes were identified from 100 sampled blocks, with the true number across all 2,558 blocks likely being several hundred; top co-solutes by data volume include sodium chloride (57 targets), glycine (41 targets), D-glucose (33 targets), potassium chloride (31 targets), and ethanol (29 targets).
- Co-solute chemical classes span inorganic salts, amino acids, sugars, alcohols, alkanolamines, ionic liquids, organic acids, transition-metal salts, phosphate salts, heterocyclic compounds, phenols, and buffer compounds.
- Mass density data for aqueous binaries is roughly 3–4 times more abundant than speed-of-sound data by every metric: ~3.7× in literature sources (1,104 vs. 295), ~3.4× in data blocks (2,558 vs. 753), and ~4.3× in data points (132,045 vs. 30,819).
- The thermodynamic window for mass density is wider than for speed of sound, extending to lower temperatures (253.15 K vs. 273.15 K), higher temperatures (673.15 K vs. 596.3 K), and much higher pressures (387,800 kPa vs. 120,000 kPa).
- The ~4× gap in data volume between density and speed of sound is expected because density is the most commonly measured thermophysical property and is routinely reported alongside other measurements, whereas speed-of-sound measurements require specialized acoustic instrumentation.
- Despite the disparity, the speed-of-sound dataset (753 blocks, ~31k points, 295 papers) remains substantial and covers a broad chemical space, providing a strong validation basis for acoustic models, isentropic compressibility derivations, and equation-of-state predictions in aqueous systems.

*Not stored here: 14 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


