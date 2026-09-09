# Data grounding evidence

- generated: 2026-09-05T04:23:40
- gate verdict: 12 violation(s)

## Cited blocks

| block | lit_num_id | inspected | inspections | db rows |
|---|---|---|---|---|
| PROPblock_18 | GLOBlit_7481 | yes | INSP_0a0742d5bd6a | 66 |
| PROPblock_6 | GLOBlit_4124 | yes | INSP_5e97b19eeb51 | 20 |

## Literal verdicts

| token | region | verdict | source |
|---|---|---|---|
| 303.15 | PROPblock_6 | verified | — |
| 101.0 | PROPblock_6 | verified | — |
| 298.15 | PROPblock_6 | uninspected_value | PROPblock_6 |
| 313.15 | PROPblock_6 | uninspected_value | PROPblock_6 |
| 20 | PROPblock_6 | ungrounded | — |
| 0.0003269 | PROPblock_6 | verified | — |
| 0.25 | PROPblock_6 | verified | — |
| 0.0003598 | PROPblock_6 | verified | — |
| 0.50 | PROPblock_6 | verified | — |
| 0.00046 | PROPblock_6 | verified | — |
| 0.75 | PROPblock_6 | verified | — |
| 0.0006145 | PROPblock_6 | verified | — |
| 1.00 | PROPblock_6 | verified | — |
| 0.000755 | PROPblock_6 | verified | — |
| 303.15 | PROPblock_18 | verified | — |
| 100.0 | PROPblock_18 | verified | — |
| 298.15 | PROPblock_18 | uninspected_value | PROPblock_18 |
| 323.15 | PROPblock_18 | uninspected_value | PROPblock_18 |
| 66 | PROPblock_18 | ungrounded | — |
| 0.00032 | PROPblock_18 | verified | — |
| 0.0989 | PROPblock_18 | verified | — |
| 0.00039 | PROPblock_18 | verified | — |
| 0.1916 | PROPblock_18 | verified | — |
| 0.00042 | PROPblock_18 | verified | — |
| 0.2925 | PROPblock_18 | verified | — |
| 0.00046 | PROPblock_18 | verified | — |
| 0.3932 | PROPblock_18 | verified | — |
| 0.00051 | PROPblock_18 | verified | — |
| 0.5029 | PROPblock_18 | verified | — |
| 0.00057 | PROPblock_18 | verified | — |
| 0.6002 | PROPblock_18 | verified | — |
| 0.00061 | PROPblock_18 | verified | — |
| 0.6931 | PROPblock_18 | verified | — |
| 0.00065 | PROPblock_18 | verified | — |
| 0.7926 | PROPblock_18 | verified | — |
| 0.00070 | PROPblock_18 | verified | — |
| 0.8996 | PROPblock_18 | verified | — |
| 0.00075 | PROPblock_18 | verified | — |
| 1.0000 | PROPblock_18 | verified | — |
| 0.00077 | PROPblock_18 | verified | — |
| 303.15 | PROPblock_18 | verified | — |
| 2.4 | PROPblock_18 | ungrounded | — |
| 0.00077 | PROPblock_18 | verified | — |
| 0.00032 | PROPblock_18 | verified | — |
| 3.86 | PROPblock_18 | ungrounded | — |
| 3.92 | PROPblock_18 | ungrounded | — |
| 101.0 | PROPblock_18 | misattributed | PROPblock_6 |
| 100.0 | PROPblock_18 | verified | — |
| 298.15 | PROPblock_18 | uninspected_value | PROPblock_18 |
| 323.15 | PROPblock_18 | uninspected_value | PROPblock_18 |

## Violations

- **UNINSPECTED_VALUE** PROPblock_6: 298.15 exists in PROPblock_6's database table but was never shown in an inspection of this run
- **UNINSPECTED_VALUE** PROPblock_6: 313.15 exists in PROPblock_6's database table but was never shown in an inspection of this run
- **UNGROUNDED_LITERAL** PROPblock_6: 20 (near '…5 K, P = 101.0 kPa   **Full block range:** 298.15–313.15 K, …') matches no inspected row/stat, database table, or other source of PROPblock_6
- **UNINSPECTED_VALUE** PROPblock_18: 298.15 exists in PROPblock_18's database table but was never shown in an inspection of this run
- **UNINSPECTED_VALUE** PROPblock_18: 323.15 exists in PROPblock_18's database table but was never shown in an inspection of this run
- **UNGROUNDED_LITERAL** PROPblock_18: 66 (near '…5 K, P = 100.0 kPa   **Full block range:** 298.15–323.15 K, …') matches no inspected row/stat, database table, or other source of PROPblock_18
- **UNGROUNDED_LITERAL** PROPblock_18: 2.4 (near '…ith increasing DMF content at 303.15 K. Pure DMF is roughly …') matches no inspected row/stat, database table, or other source of PROPblock_18
- **UNGROUNDED_LITERAL** PROPblock_18: 3.86 (near '…DMF — it is a larger molecule with a higher dipole moment (~…') matches no inspected row/stat, database table, or other source of PROPblock_18
- **UNGROUNDED_LITERAL** PROPblock_18: 3.92 (near '…a larger molecule with a higher dipole moment (~3.86 D vs. ~…') matches no inspected row/stat, database table, or other source of PROPblock_18
- **MISATTRIBUTED_VALUE** PROPblock_18: 101.0 does not belong to PROPblock_18; it matches only GLOBlit_4124::PROPblock_6 (inspected this run)
- **UNINSPECTED_VALUE** PROPblock_18: 298.15 exists in PROPblock_18's database table but was never shown in an inspection of this run
- **UNINSPECTED_VALUE** PROPblock_18: 323.15 exists in PROPblock_18's database table but was never shown in an inspection of this run

## Inspections (verbatim)

### INSP_5e97b19eeb51 — GLOBlit_4124::PROPblock_6 (complete, 5 rows shown)

_structured envelope entry (no markdown)_

### INSP_0a0742d5bd6a — GLOBlit_7481::PROPblock_18 (complete, 11 rows shown)

_structured envelope entry (no markdown)_
