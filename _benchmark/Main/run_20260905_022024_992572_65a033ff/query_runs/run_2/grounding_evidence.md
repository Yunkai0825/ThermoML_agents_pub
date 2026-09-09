# Data grounding evidence

- generated: 2026-09-05T02:24:07
- gate verdict: 6 violation(s)

## Cited blocks

| block | lit_num_id | inspected | inspections | db rows |
|---|---|---|---|---|
| PROPblock_18 | GLOBlit_7481 | yes | INSP_421661c26d77 | 66 |
| PROPblock_6 | GLOBlit_4124 | yes | INSP_116c1d101a97 | 20 |

## Literal verdicts

| token | region | verdict | source |
|---|---|---|---|
| 100.0 | PROPblock_18 | verified | — |
| 0.5000 | PROPblock_18 | uninspected_value | PROPblock_18 |
| 0.5029 | PROPblock_18 | verified | — |
| 298.15 | PROPblock_18 | verified | — |
| 298.15 | PROPblock_18 | verified | — |
| 0.3932 | PROPblock_18 | verified | — |
| 100.0 | PROPblock_18 | verified | — |
| 0.00054 | PROPblock_18 | verified | — |
| 0.54 | PROPblock_18 | verified | — |
| 298.15 | PROPblock_18 | verified | — |
| 0.5029 | PROPblock_18 | verified | — |
| 100.0 | PROPblock_18 | verified | — |
| 0.00061 | PROPblock_18 | verified | — |
| 0.61 | PROPblock_18 | verified | — |
| 298.15 | PROPblock_18 | verified | — |
| 0.6002 | PROPblock_18 | verified | — |
| 100.0 | PROPblock_18 | verified | — |
| 0.00065 | PROPblock_18 | verified | — |
| 0.65 | PROPblock_18 | verified | — |
| 298.15 | PROPblock_18 | verified | — |
| 0.6931 | PROPblock_18 | verified | — |
| 100.0 | PROPblock_18 | verified | — |
| 0.00069 | PROPblock_18 | verified | — |
| 0.69 | PROPblock_18 | verified | — |
| 0.00061 | PROPblock_18 | verified | — |
| 0.61 | PROPblock_18 | verified | — |
| 0.5029 | PROPblock_18 | verified | — |
| 298.15 | PROPblock_18 | verified | — |
| 100.0 | PROPblock_18 | verified | — |
| 101.0 | PROPblock_6 | verified | — |
| 0.5 | PROPblock_6 | verified | — |
| 0.64 | PROPblock_6 | ungrounded | — |
| 73.09 | PROPblock_6 | ungrounded | — |
| 41.05 | PROPblock_6 | ungrounded | — |
| 0.64 | PROPblock_6 | ungrounded | — |
| 298.15 | PROPblock_6 | verified | — |
| 298.15 | PROPblock_6 | verified | — |
| 0.25 | PROPblock_6 | verified | — |
| 101.0 | PROPblock_6 | verified | — |
| 0.0003959 | PROPblock_6 | verified | — |
| 0.396 | PROPblock_6 | verified | — |
| 298.15 | PROPblock_6 | verified | — |
| 0.50 | PROPblock_6 | verified | — |
| 101.0 | PROPblock_6 | verified | — |
| 0.0005214 | PROPblock_6 | verified | — |
| 0.521 | PROPblock_6 | verified | — |
| 298.15 | PROPblock_6 | verified | — |
| 0.75 | PROPblock_6 | verified | — |
| 101.0 | PROPblock_6 | verified | — |
| 0.0006465 | PROPblock_6 | verified | — |
| 0.647 | PROPblock_6 | verified | — |
| 298.15 | PROPblock_6 | verified | — |
| 1.00 | PROPblock_6 | verified | — |
| 101.0 | PROPblock_6 | verified | — |
| 0.0007986 | PROPblock_6 | verified | — |
| 0.799 | PROPblock_6 | verified | — |
| 0.50 | PROPblock_6 | verified | — |
| 0.75 | PROPblock_6 | verified | — |
| 0.5029 | PROPblock_18 + PROPblock_6 | verified | — |
| 0.00061 | PROPblock_18 + PROPblock_6 | verified | — |
| 0.61 | PROPblock_18 + PROPblock_6 | verified | — |
| 0.50 | PROPblock_18 + PROPblock_6 | verified | — |
| 0.75 | PROPblock_18 + PROPblock_6 | verified | — |
| 0.0005214 | PROPblock_18 + PROPblock_6 | verified | — |
| 0.0006465 | PROPblock_18 + PROPblock_6 | verified | — |
| 0.521 | PROPblock_18 + PROPblock_6 | verified | — |
| 0.647 | PROPblock_18 + PROPblock_6 | verified | — |
| 298.15 | PROPblock_6 | verified | — |
| 0.00080 | PROPblock_6 | verified | — |
| 0.00034 | PROPblock_6 | uninspected_value | PROPblock_6 |
| 0.00061 | PROPblock_18 | verified | — |

## Violations

- **UNINSPECTED_VALUE** PROPblock_18: 0.5000 exists in PROPblock_18's database table but was never shown in an inspection of this run
- **UNGROUNDED_LITERAL** PROPblock_6: 0.64 (near '…lar mixture (x = 0.5) corresponds to approximately w(DMF) ≈ …') matches no inspected row/stat, database table, or other source of PROPblock_6
- **UNGROUNDED_LITERAL** PROPblock_6: 73.09 (near '…proximately w(DMF) ≈ 0.64 based on the molar masses of DMF (…') matches no inspected row/stat, database table, or other source of PROPblock_6
- **UNGROUNDED_LITERAL** PROPblock_6: 41.05 (near '…on the molar masses of DMF (73.09 g/mol) and acetonitrile (4…') matches no inspected row/stat, database table, or other source of PROPblock_6
- **UNGROUNDED_LITERAL** PROPblock_6: 0.64 (near '…g/mol) and acetonitrile (41.05 g/mol). No exact row at w ≈ 0…') matches no inspected row/stat, database table, or other source of PROPblock_6
- **UNINSPECTED_VALUE** PROPblock_6: 0.00034 exists in PROPblock_6's database table but was never shown in an inspection of this run

## Inspections (verbatim)

### INSP_421661c26d77 — GLOBlit_7481::PROPblock_18 (nearest, 4 rows shown)

_structured envelope entry (no markdown)_

### INSP_116c1d101a97 — GLOBlit_4124::PROPblock_6 (nearest, 4 rows shown)

_structured envelope entry (no markdown)_
