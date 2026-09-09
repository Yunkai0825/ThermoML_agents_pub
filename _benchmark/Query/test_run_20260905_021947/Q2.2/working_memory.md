# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Compare experimental viscosity (dynamic) data availability for binary vs. ternary liquid mixtures in ThermoML, focusing  → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** Dynamic viscosity (Viscosity, Pa·s, GLOBprop_4) data in ThermoML is far more abundant for binary liquid mixtures than ternary ones: 1176 distinct literature sources and 3294 property blocks (137,229 total data points) for binary systems versus 429 sources and 1081 blocks (81,066 points) for ternary systems. However, ternary blocks are denser in composition coverage, averaging ~75 data points per block compared to ~42 for binary, reflecting the need to map the two-dimensional Gibbs triangle. Binary data spans a wider temperature range (199.918–1173.0 K) and pressure range (0.0–387,800.0 kPa) compared to ternary (20.0–1023.0 K; 0.0–196,130.0 kPa). Notable top sources include GLOBlit_7152 (DOI: 10.1021/acs.jced.7b00221, 25 blocks, 1448 points) for binary and GLOBlit_6743 (DOI: 10.1021/acs.jced.5b00845, 48 blocks, 5168 points) for ternary systems.

**Answer:**

#### Comparison of Dynamic Viscosity Data Availability: Binary vs. Ternary Liquid Mixtures in ThermoML

##### Summary Table

**WM_L1_Q1_Table#1_(Query_L1_Q1_Answer):**

| *row_id* | *Metric* | *Binary (2-component)* | *Ternary (3-component)* |
|---|---|---|---|
| WM_L1_Q1_Table#1_Row#1 | 「Distinct literature sources (DOIs)」 | 「1176」 | 「429」 |
| WM_L1_Q1_Table#1_Row#2 | 「Property blocks」 | 「3294」 | 「1081」 |
| WM_L1_Q1_Table#1_Row#3 | 「Total data points」 | 「137,229」 | 「81,066」 |
| WM_L1_Q1_Table#1_Row#4 | 「Avg. data points per block」 | 「~41.7」 | 「~75.0」 |
| WM_L1_Q1_Table#1_Row#5 | 「Avg. blocks per literature source」 | 「~2.8」 | 「~2.5」 |
| WM_L1_Q1_Table#1_Row#6 | 「Temperature range (K)」 | 「199.918 – 1173.0」 | 「20.0 – 1023.0」 |
| WM_L1_Q1_Table#1_Row#7 | 「Pressure range (kPa)」 | 「0.0 – 387,800.0」 | 「0.0 – 196,130.0」 |

All data refer to the property **Viscosity, Pa·s** (GLOBprop_4) in declared binary or ternary systems.

##### Key Observations

1. **Binary systems dominate in volume:** There are roughly 3× more literature sources and 3× more property blocks for binary mixtures compared to ternary ones. This reflects the general trend in experimental thermodynamics where binary systems are studied more frequently as they are simpler to prepare and interpret.

2. **Ternary blocks are denser in composition coverage:** Despite fewer total blocks, ternary systems average ~75 data points per block versus ~42 for binary systems. This is chemically expected — ternary composition space is two-dimensional (a Gibbs triangle), so experimentalists typically measure viscosity at many more composition points per block to adequately map the composition surface. A binary system only requires a one-dimensional composition sweep.

3. **Top binary sources** include GLOBlit_7152 (DOI: 10.1021/acs.jced.7b00221, 25 blocks, 1448 points) and GLOBlit_3363 (DOI: 10.1016/j.jct.2011.02.018, 6 blocks, 848 points).

4. **Top ternary sources** include GLOBlit_6743 (DOI: 10.1021/acs.jced.5b00845, 48 blocks, 5168 points) — a notably large ternary viscosity dataset — and GLOBlit_10411 (DOI: 10.1021/je5001523, 17 blocks, 1604 points).

5. **Condition coverage:** Binary data spans a wider temperature and pressure range, consistent with the greater diversity of binary systems studied (including high-temperature molten salt or industrial systems up to 1173 K and high-pressure measurements up to ~388 MPa). Ternary data reaches up to 1023 K and ~196 MPa, still substantial but somewhat narrower.

6. **Composition coverage per system:** The higher average points-per-block for ternary systems (~75 vs. ~42) suggests that individual ternary studies tend to cover composition space more thoroughly. For binary systems, a typical block might span 10–20 mole-fraction values across the full range (0→1), while ternary blocks often include grid-like sampling across the composition triangle.

**Core claims:**
- Binary liquid mixtures have roughly 3× more literature sources (1176 vs. 429 DOIs) and 3× more property blocks (3294 vs. 1081) for dynamic viscosity (Viscosity, Pa·s) in ThermoML compared to ternary liquid mixtures.
- Despite fewer total blocks, ternary viscosity blocks average ~75.0 data points per block versus ~41.7 for binary blocks, consistent with the need to cover two-dimensional composition space in ternary systems.
- Total data-point counts are 137,229 for binary and 81,066 for ternary dynamic viscosity measurements.
- Binary viscosity data span a wider range of conditions (temperature 199.918–1173.0 K, pressure 0.0–387,800.0 kPa) than ternary data (temperature 20.0–1023.0 K, pressure 0.0–196,130.0 kPa).
- All reported data refer to the property Viscosity, Pa·s (GLOBprop_4) in declared binary or ternary systems within ThermoML.

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


