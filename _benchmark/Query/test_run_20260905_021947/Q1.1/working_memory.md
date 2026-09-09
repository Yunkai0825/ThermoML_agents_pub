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
- [L1] Find experimental mass density of ethanol + water binary mixture at equimolar composition (mole fraction 0.5), 25 °C (29 → stored as L1_query_1 · validation: FLAGGED(3)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(3)

**Summary:** Two independent ThermoML sources report the mass density of the ethanol + water binary mixture at equimolar composition and 298.15 K. Source GLOBlit_9006 (DOI: 10.1021/je060335h), PROPblock_1, gives 858.98 kg/m³ at x(ethanol) = 0.49976 and 101.0 kPa. Source GLOBlit_5201 (DOI: 10.1016/j.jct.2018.02.022), PROPblock_19, gives 858.963 kg/m³ at x(ethanol) = 0.5002 and 92.3 kPa. The two values are in excellent agreement at approximately 859 kg/m³. This measured density is lower than an ideal-mixing estimate, reflecting the well-known negative excess volume of the ethanol–water system due to hydrogen-bonding reorganization. Near x(ethanol) = 0.5, density decreases steeply with increasing ethanol mole fraction, at roughly −4 to −5 kg/m³ per 0.01 increase in x(ethanol), as estimated from bracketing data in GLOBlit_9006::PROPblock_1.

**Answer:**

#### Mass Density of Ethanol + Water at Equimolar Composition, 25 °C, Atmospheric Pressure

Two independent ThermoML sources provide experimental mass density data for the binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) system at mole fraction x(ethanol) ≈ 0.5 and T = 298.15 K:

##### Source 1 (DOI: 10.1021/je060335h, GLOBlit_9006, PROPblock_1)
- **Pressure:** 101.0 kPa (atmospheric)
- Nearest data point to x(ethanol) = 0.5:

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *T (K)* | *p (kPa)* | *ρ (kg/m³)* |
|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.49976」 | 「298.15」 | 「101.0」 | 「**858.98**」 |

Bracketing points:

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0.47749」 | 「863.28」 |
| WM_L1#1_Table#2_Row#2 | 「0.49976」 | 「858.98」 |
| WM_L1#1_Table#2_Row#3 | 「0.54464」 | 「850.55」 |

##### Source 2 (DOI: 10.1016/j.jct.2018.02.022, GLOBlit_5201, PROPblock_19)
- **Pressure:** 92.3 kPa (slightly below standard atmospheric)
- Nearest data points to x(ethanol) = 0.5:

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *T (K)* | *p (kPa)* | *ρ (kg/m³)* |
|---|---|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0.4989」 | 「298.15」 | 「92.3」 | 「860.04」 |
| WM_L1#1_Table#3_Row#2 | 「0.5002」 | 「298.15」 | 「92.3」 | 「**858.963**」 |

##### Summary

At x(ethanol) ≈ 0.5 and T = 298.15 K, the experimental mass density of the ethanol + water mixture is approximately **859 kg/m³**, with the two independent sources in excellent agreement:

- **858.98 kg/m³** at x = 0.49976, 101.0 kPa — GLOBlit_9006, PROPblock_1
- **858.963 kg/m³** at x = 0.5002, 92.3 kPa — GLOBlit_5201, PROPblock_19

**Chemical insight:** This density is notably lower than what would be predicted by ideal mixing of the pure components. Pure ethanol has a density of roughly 785 kg/m³ and pure water roughly 997 kg/m³ (both values are approximate reference knowledge, not from this database search). A simple linear (ideal) estimate at x = 0.5 would therefore be around 891 kg/m³ (derived estimate, not a database value), but the measured value of ~859 kg/m³ reflects the well-known negative excess volume of the ethanol–water system — hydrogen-bonding reorganization causes the mixture to occupy more volume than ideal, yielding a lower density. The density decreases steeply with increasing ethanol mole fraction in this composition region (roughly −4 to −5 kg/m³ per 0.01 increase in x(ethanol) near x = 0.5, estimated from the inspected rows of GLOBlit_9006::PROPblock_1).

**Core claims:**
- At x(ethanol) ≈ 0.5 and T = 298.15 K, two independent ThermoML sources report the mass density of the ethanol + water mixture as 858.98 kg/m³ (x = 0.49976, 101.0 kPa) and 858.963 kg/m³ (x = 0.5002, 92.3 kPa), yielding an approximate consensus value of ~859 kg/m³.
- The two independent sources are in excellent mutual agreement despite slightly different pressures (101.0 kPa vs. 92.3 kPa).
- The measured density of ~859 kg/m³ is lower than an ideal-mixing linear estimate, consistent with the well-known negative excess volume of the ethanol–water system arising from hydrogen-bonding reorganization.
- The ideal-mixing estimate of ~891 kg/m³ and the pure-component densities (~785 kg/m³ for ethanol, ~997 kg/m³ for water) cited in the answer are approximate reference values, not drawn from the inspected database, and the comparative claim that the measured density is lower than the ideal estimate should be evaluated with that caveat.
- Near x(ethanol) = 0.5, the density decreases steeply with increasing ethanol mole fraction, at roughly −4 to −5 kg/m³ per 0.01 increase in x(ethanol), as estimated from the inspected data of one source.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_9006」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for ethanol + water binary mixture at 298.15 K and 101.0 kPa, including x(ethanol) = 0.49976 with ρ = 858.98 kg/m³.」 |
| WM_L1#1_Table#5 | 「GLOBlit_5201」 | 「PROPblock_19」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for ethanol + water binary mixture at 298.15 K and 92.3 kPa, including x(ethanol) = 0.5002 with ρ = 858.963 kg/m³.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(3) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **MISATTRIBUTED_VALUE** PROPblock_19: 101.0 does not belong to PROPblock_19; it matches only GLOBlit_9006::PROPblock_1 (inspected this run)
- **MISATTRIBUTED_VALUE** PROPblock_1: 92.3 does not belong to PROPblock_1; it matches only GLOBlit_5201::PROPblock_19 (inspected this run)
- **MISATTRIBUTED_VALUE** PROPblock_19: 891 does not belong to PROPblock_19; it matches only GLOBlit_9006::PROPblock_1 (inspected this run)


