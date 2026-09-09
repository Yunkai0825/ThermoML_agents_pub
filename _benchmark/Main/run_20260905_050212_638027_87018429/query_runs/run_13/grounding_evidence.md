# Data grounding evidence

- generated: 2026-09-05T05:04:48
- gate verdict: 2 violation(s)

## Cited blocks

| block | lit_num_id | inspected | inspections | db rows |
|---|---|---|---|---|
| PROPblock_2 | GLOBlit_555 | yes | INSP_9e4417a4e81d | 5 |
| PROPblock_6 | GLOBlit_306 | yes | INSP_6715d3baae18 | 1 |

## Literal verdicts

| token | region | verdict | source |
|---|---|---|---|
| 997.06 | PROPblock_6 | verified | — |
| 298.15 | PROPblock_6 | verified | — |
| 101.325 | PROPblock_6 | verified | — |
| 997.043 | PROPblock_2 | verified | — |
| 298.15 | PROPblock_2 | verified | — |
| 101.0 | PROPblock_2 | verified | — |
| 298.15 | PROPblock_2 | verified | — |
| 997.04 | PROPblock_2 | verified | — |
| 997.06 | PROPblock_2 | verified | — |
| 101 | PROPblock_2 | verified | — |
| 997.06 | PROPblock_2 | verified | — |
| 997.043 | PROPblock_2 | verified | — |
| 0.02 | PROPblock_2 | ungrounded | — |
| 101.325 | PROPblock_2 | misattributed | PROPblock_6 |
| 101.0 | PROPblock_2 | verified | — |
| 298.15 | PROPblock_2 | verified | — |

## Violations

- **UNGROUNDED_LITERAL** PROPblock_2: 0.02 (near '…d values — 997.06 kg/m3 and 997.043 kg/m3 — differ by only ~…') matches no inspected row/stat, database table, or other source of PROPblock_2
- **MISATTRIBUTED_VALUE** PROPblock_2: 101.325 does not belong to PROPblock_2; it matches only GLOBlit_306::PROPblock_6 (inspected this run)

## Inspections (verbatim)

### INSP_9e4417a4e81d — GLOBlit_555::PROPblock_2 (nearest, 2 rows shown)

_structured envelope entry (no markdown)_

### INSP_6715d3baae18 — GLOBlit_306::PROPblock_6 (nearest, 1 rows shown)

_structured envelope entry (no markdown)_
