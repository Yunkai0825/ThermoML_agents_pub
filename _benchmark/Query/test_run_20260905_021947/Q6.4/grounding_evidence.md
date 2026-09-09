# Data grounding evidence

- generated: 2026-09-05T06:05:48
- gate verdict: 12 violation(s)

## Cited blocks

| block | lit_num_id | inspected | inspections | db rows |
|---|---|---|---|---|
| PROPblock_1 | GLOBlit_1246 | yes | INSP_c120fd362f0c | 1 |
| PROPblock_3 | GLOBlit_779 | yes | INSP_ae4f04a9ca18, INSP_7d4176a6acb2 | 4 |
| PROPblock_4 | GLOBlit_86 | yes | INSP_66cf20e92a90 | 5 |
| PROPblock_7 | GLOBlit_57 | yes | INSP_4af5341b9c11 | 1 |

## Literal verdicts

| token | region | verdict | source |
|---|---|---|---|
| 298.15 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 101.325 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 1095.271 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 298.15 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 101.0 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 1095.278 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 298.15 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 101.325 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 1095.27 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 298.15 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 101.0 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 1095.37 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 298.15 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 85.9 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 1095.29 | PROPblock_7 + PROPblock_4 + PROPblock_3 + PROPblock_1 | verified | — |
| 25 | PROPblock_1 | ungrounded | — |
| 1095.3 | PROPblock_1 | verified | — |
| 1.0953 | PROPblock_1 | verified | — |
| 1095.27 | PROPblock_1 | verified | — |
| 1095.37 | PROPblock_1 | verified | — |
| 0.1 | PROPblock_1 | verified | — |
| 25 | PROPblock_1 | ungrounded | — |
| 293.15 | PROPblock_1 | misattributed | PROPblock_4 |
| 101.0 | PROPblock_1 | ambiguous | 2 sources |
| 1100.306 | PROPblock_1 | misattributed | PROPblock_4 |
| 298.15 | PROPblock_1 | verified | — |
| 101.0 | PROPblock_1 | ambiguous | 2 sources |
| 1095.278 | PROPblock_1 | verified | — |
| 303.15 | PROPblock_1 | misattributed | PROPblock_4 |
| 101.0 | PROPblock_1 | ambiguous | 2 sources |
| 1090.253 | PROPblock_1 | misattributed | PROPblock_4 |
| 78.13 | PROPblock_1 | ungrounded | — |
| 25 | PROPblock_1 | ungrounded | — |
| 3.96 | PROPblock_1 | ungrounded | — |

## Violations

- **UNGROUNDED_LITERAL** PROPblock_1: 25 (near '…### Recommended value for your calculation  > **ρ(DMSO, 25 °…') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 25 (near '…exact pressure conditions.  ### Temperature dependence near …') matches no inspected row/stat, database table, or other source of PROPblock_1
- **MISATTRIBUTED_VALUE** PROPblock_1: 293.15 does not belong to PROPblock_1; it matches only GLOBlit_86::PROPblock_4 (inspected this run)
- **AMBIGUOUS_VALUE** PROPblock_1: 101.0 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **MISATTRIBUTED_VALUE** PROPblock_1: 1100.306 does not belong to PROPblock_1; it matches only GLOBlit_86::PROPblock_4 (inspected this run)
- **AMBIGUOUS_VALUE** PROPblock_1: 101.0 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **MISATTRIBUTED_VALUE** PROPblock_1: 303.15 does not belong to PROPblock_1; it matches only GLOBlit_86::PROPblock_4 (inspected this run)
- **AMBIGUOUS_VALUE** PROPblock_1: 101.0 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **MISATTRIBUTED_VALUE** PROPblock_1: 1090.253 does not belong to PROPblock_1; it matches only GLOBlit_86::PROPblock_4 (inspected this run)
- **UNGROUNDED_LITERAL** PROPblock_1: 78.13 (near '…ent temperature.  ### Chemistry note  DMSO (CH₃–SO–CH₃, M = …') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 25 (near '…DMSO (CH₃–SO–CH₃, M = 78.13 g/mol) is denser than water at 2…') matches no inspected row/stat, database table, or other source of PROPblock_1
- **UNGROUNDED_LITERAL** PROPblock_1: 3.96 (near '…h molecular mass and strong dipole–dipole interactions (μ ≈ …') matches no inspected row/stat, database table, or other source of PROPblock_1

## Inspections (verbatim)

### INSP_66cf20e92a90 — GLOBlit_86::PROPblock_4 (nearest, 3 rows shown)

_structured envelope entry (no markdown)_

### INSP_4af5341b9c11 — GLOBlit_57::PROPblock_7 (nearest, 1 rows shown)

_structured envelope entry (no markdown)_

### INSP_ae4f04a9ca18 — GLOBlit_779::PROPblock_3 (nearest, 1 rows shown)

_structured envelope entry (no markdown)_

### INSP_7d4176a6acb2 — GLOBlit_938::PROPblock_3 (nearest, 1 rows shown)

_structured envelope entry (no markdown)_

### INSP_c120fd362f0c — GLOBlit_1246::PROPblock_1 (nearest, 1 rows shown)

_structured envelope entry (no markdown)_
