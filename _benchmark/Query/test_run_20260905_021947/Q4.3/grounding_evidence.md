# Data grounding evidence

- generated: 2026-09-05T06:00:48
- gate verdict: 33 violation(s)

## Cited blocks

| block | lit_num_id | inspected | inspections | db rows |
|---|---|---|---|---|
| PROPblock_1 | GLOBlit_57 | yes | INSP_7861323c4024 | 1 |
| PROPblock_10 | GLOBlit_2825 | yes | INSP_5d31e929df24 | 39 |
| PROPblock_4 | GLOBlit_5688 | yes | INSP_15c1ba3ad05f, INSP_6931016a10b1, INSP_3731e85c0b92 | 13 |
| PROPblock_6 | GLOBlit_86 | yes | INSP_07e3683a04fb, INSP_6715d3baae18, INSP_428715c8042d, INSP_2a46f0d6e4fd | 5 |

## Literal verdicts

| token | region | verdict | source |
|---|---|---|---|
| 943.81 | PROPblock_4 + PROPblock_6 + PROPblock_1 | verified | — |
| 997.06 | PROPblock_4 + PROPblock_6 + PROPblock_1 | verified | — |
| 786.531 | PROPblock_4 + PROPblock_6 + PROPblock_1 | verified | — |
| 73.09 | PROPblock_1 | ungrounded | — |
| 18.015 | PROPblock_1 | ungrounded | — |
| 32.04 | PROPblock_1 | ungrounded | — |
| 73.09 | PROPblock_1 | ungrounded | — |
| 0.94381 | PROPblock_1 | misattributed | PROPblock_4 |
| 77.44 | PROPblock_1 | ungrounded | — |
| 18.015 | PROPblock_1 | ungrounded | — |
| 0.99706 | PROPblock_1 | misattributed | PROPblock_6 |
| 18.07 | PROPblock_1 | ungrounded | — |
| 32.04 | PROPblock_1 | ungrounded | — |
| 0.786531 | PROPblock_1 | verified | — |
| 40.73 | PROPblock_1 | ungrounded | — |
| 77.44 | PROPblock_1 | ungrounded | — |
| 18.07 | PROPblock_1 | ungrounded | — |
| 40.73 | PROPblock_1 | ungrounded | — |
| 45.41 | PROPblock_1 | ungrounded | — |
| 73.09 | PROPblock_1 | ungrounded | — |
| 18.015 | PROPblock_1 | ungrounded | — |
| 32.04 | PROPblock_1 | ungrounded | — |
| 41.05 | PROPblock_1 | ungrounded | — |
| 41.05 | PROPblock_1 | ungrounded | — |
| 0.9040 | PROPblock_1 | ungrounded | — |
| 904.0 | PROPblock_1 | ungrounded | — |
| 298.15 | PROPblock_1 | verified | — |
| 14 | PROPblock_4 | ungrounded | — |
| 0.30 | PROPblock_4 | verified | — |
| 991.40 | PROPblock_4 | verified | — |
| 0.498 | PROPblock_4 | verified | — |
| 976.64 | PROPblock_4 | verified | — |
| 0.10 | PROPblock_4 | verified | — |
| 997 | PROPblock_4 | verified | — |
| 26 | PROPblock_6 | ungrounded | — |
| 0.5002 | PROPblock_6 | verified | — |
| 894.978 | PROPblock_6 | verified | — |
| 13 | PROPblock_10 | ungrounded | — |
| 0.5003 | PROPblock_10 | verified | — |
| 881.69 | PROPblock_10 | verified | — |
| -0.5 | PROPblock_10 | ungrounded | — |
| -1.0 | PROPblock_10 | ungrounded | — |
| 44.4 | PROPblock_10 | ungrounded | — |
| 44.9 | PROPblock_10 | ungrounded | — |
| 45.4 | PROPblock_10 | ungrounded | — |
| 914 | PROPblock_10 | ungrounded | — |
| 924 | PROPblock_10 | ungrounded | — |
| 904 | PROPblock_10 | ungrounded | — |
| 0.10 | PROPblock_10 | verified | — |

## Violations

- **UNGROUNDED_LITERAL** PROPblock_1: 73.09 (near '…Using standard molar masses (M_DMF = 73.09 g/mol, M_water = …') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 18.015 (near '…Using standard molar masses (M_DMF = 73.09 g/mol, M_water = …') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 32.04 (near '…(M_DMF = 73.09 g/mol, M_water = 18.015 g/mol, M_methanol = 3…') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 73.09 (near '…entries), the pure-component molar volumes are:  - V*_DMF = …') matches no inspected row/stat, database table, or other source of PROPblock_1
- **MISATTRIBUTED_VALUE** PROPblock_1: 0.94381 does not belong to PROPblock_1; it matches only GLOBlit_5688::PROPblock_4 (inspected this run)
- **UNGROUNDED_LITERAL** PROPblock_1: 77.44 (near '…-component molar volumes are:  - V*_DMF = 73.09 / 0.94381 = …') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 18.015 (near '…e:  - V*_DMF = 73.09 / 0.94381 = 77.44 cm3/mol - V*_water = …') matches no inspected row/stat, database table, or other source of PROPblock_1
- **MISATTRIBUTED_VALUE** PROPblock_1: 0.99706 does not belong to PROPblock_1; it matches only GLOBlit_86::PROPblock_6 (inspected this run)
- **UNGROUNDED_LITERAL** PROPblock_1: 18.07 (near '…9 / 0.94381 = 77.44 cm3/mol - V*_water = 18.015 / 0.99706 = …') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 32.04 (near '…V*_water = 18.015 / 0.99706 = 18.07 cm3/mol - V*_methanol = …') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 40.73 (near '…0.99706 = 18.07 cm3/mol - V*_methanol = 32.04 / 0.786531 = 4…') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 77.44 (near '…equimolar mixture (x₁ = x₂ = x₃ = 1/3):  **V_ideal = (1/3)(7…') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 18.07 (near '…ure (x₁ = x₂ = x₃ = 1/3):  **V_ideal = (1/3)(77.44) + (1/3)(…') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 40.73 (near '…x₃ = 1/3):  **V_ideal = (1/3)(77.44) + (1/3)(18.07) + (1/3)(…') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 45.41 (near '…:  **V_ideal = (1/3)(77.44) + (1/3)(18.07) + (1/3)(40.73) = …') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 73.09 (near '…The average molar mass of the mixture is:  **M_mix = (1/3)(7…') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 18.015 (near '…rage molar mass of the mixture is:  **M_mix = (1/3)(73.09 + …') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 32.04 (near '…r mass of the mixture is:  **M_mix = (1/3)(73.09 + 18.015 + …') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 41.05 (near '…the mixture is:  **M_mix = (1/3)(73.09 + 18.015 + 32.04) = 4…') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 41.05 (near '…corresponds to an ideal mixture density of M_mix/V_ideal = 4…') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 0.9040 (near '…o an ideal mixture density of M_mix/V_ideal = 41.05/45.41 = …') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 904.0 (near '…e density of M_mix/V_ideal = 41.05/45.41 = 0.9040 g/cm3 = **…') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_4: 14 (near '…, DOI:  ): 14 data points. At x_DMF = 0.30, ρ = 991.4…') matches no inspected row/stat, database table, or other source of PROPblock_4
- **UNGROUNDED_LITERAL** PROPblock_6: 26 (near '…, DOI:  ): 26 data points. At x_DMF = 0.5002, ρ = 894…') matches no inspected row/stat, database table, or other source of PROPblock_6
- **UNGROUNDED_LITERAL** PROPblock_10: 13 (near '…, DOI:  ): 13 data points. At x_water = 0.5003, ρ = 8…') matches no inspected row/stat, database table, or other source of PROPblock_10
- **UNGROUNDED_LITERAL** PROPblock_10: -0.5 (near '…to the ternary, a net excess volume correction of roughly **…') matches no inspected row/stat, database table, or other source of PROPblock_10
- **UNGROUNDED_LITERAL** PROPblock_10: -1.0 (near '…ernary, a net excess volume correction of roughly **-0.5 to …') matches no inspected row/stat, database table, or other source of PROPblock_10
- **UNGROUNDED_LITERAL** PROPblock_10: 44.4 (near '…nary molar volume is reasonable.  **Expected molar volume ≈ …') matches no inspected row/stat, database table, or other source of PROPblock_10
- **UNGROUNDED_LITERAL** PROPblock_10: 44.9 (near '…molar volume is reasonable.  **Expected molar volume ≈ 44.4–…') matches no inspected row/stat, database table, or other source of PROPblock_10
- **UNGROUNDED_LITERAL** PROPblock_10: 45.4 (near '…lar volume ≈ 44.4–44.9 cm3/mol** (i.e., the ideal value of ~…') matches no inspected row/stat, database table, or other source of PROPblock_10
- **UNGROUNDED_LITERAL** PROPblock_10: 914 (near '…rresponds to an expected mixture density of approximately **…') matches no inspected row/stat, database table, or other source of PROPblock_10
- **UNGROUNDED_LITERAL** PROPblock_10: 924 (near '…ponds to an expected mixture density of approximately **914–…') matches no inspected row/stat, database table, or other source of PROPblock_10
- **UNGROUNDED_LITERAL** PROPblock_10: 904 (near '…/m3**, somewhat higher than the ideal-mixing prediction of ~…') matches no inspected row/stat, database table, or other source of PROPblock_10

## Inspections (verbatim)

### INSP_15c1ba3ad05f — GLOBlit_5688::PROPblock_4 (rdp, 8 rows shown)

_structured envelope entry (no markdown)_

### INSP_07e3683a04fb — GLOBlit_86::PROPblock_6 (nearest, 3 rows shown)

_structured envelope entry (no markdown)_

### INSP_6931016a10b1 — GLOBlit_228::PROPblock_4 (complete, 1 rows shown)

_structured envelope entry (no markdown)_

### INSP_7861323c4024 — GLOBlit_57::PROPblock_1 (nearest, 1 rows shown)

_structured envelope entry (no markdown)_

### INSP_6715d3baae18 — GLOBlit_306::PROPblock_6 (nearest, 1 rows shown)

_structured envelope entry (no markdown)_

### INSP_3731e85c0b92 — GLOBlit_11030::PROPblock_4 (rdp, 14 rows shown)

_structured envelope entry (no markdown)_

### INSP_428715c8042d — GLOBlit_4125::PROPblock_6 (rdp, 9 rows shown)

_structured envelope entry (no markdown)_

### INSP_5d31e929df24 — GLOBlit_2825::PROPblock_10 (rdp, 12 rows shown)

_structured envelope entry (no markdown)_

### INSP_2a46f0d6e4fd — GLOBlit_4125::PROPblock_6 (nearest, 1 rows shown)

_structured envelope entry (no markdown)_
