# Data grounding evidence

- generated: 2026-09-05T05:45:53
- gate verdict: 35 violation(s)

## Cited blocks

| block | lit_num_id | inspected | inspections | db rows |
|---|---|---|---|---|
| PROPblock_18 | GLOBlit_7481 | yes | INSP_fbc270263cf3 | 66 |
| PROPblock_3 | GLOBlit_9900 | yes | INSP_223a0880d59c, INSP_98abce7cba9c | 60 |
| PROPblock_6 | GLOBlit_4124 | yes | INSP_5ce79feb1bd5 | 20 |
| PROPblock_9 | GLOBlit_8676 | yes | INSP_469970d3baa4 | 11 |

## Literal verdicts

| token | region | verdict | source |
|---|---|---|---|
| 0.0008045 | PROPblock_3 | verified | — |
| 0.0008903 | PROPblock_3 | verified | — |
| 0.0003417 | PROPblock_3 | verified | — |
| 298.15 | PROPblock_3 | verified | — |
| 0.5 | PROPblock_3 + PROPblock_18 | verified | — |
| 0.0018528 | PROPblock_3 + PROPblock_18 | verified | — |
| 0.5029 | PROPblock_3 + PROPblock_18 | verified | — |
| 0.00061 | PROPblock_3 + PROPblock_18 | verified | — |
| 0.5204 | PROPblock_3 + PROPblock_18 | verified | — |
| 0.0005387 | PROPblock_3 + PROPblock_18 | verified | — |
| +3.14 | PROPblock_18 | ungrounded | — |
| +0.59 | PROPblock_18 | uninspected_value | PROPblock_18 |
| -0.01 | PROPblock_18 | ungrounded | — |
| 0.0008045 | PROPblock_18 | misattributed | PROPblock_3 |
| 0.0008903 | PROPblock_18 | misattributed | PROPblock_3 |
| 0.0003417 | PROPblock_18 | ambiguous | 2 sources |
| -7.376 | PROPblock_18 | ungrounded | — |
| 3.14 | PROPblock_18 | ungrounded | — |
| 0.59 | PROPblock_18 | uninspected_value | PROPblock_18 |
| 0.01 | PROPblock_18 | verified | — |
| 3.72 | PROPblock_18 | ungrounded | — |
| +0.413 | PROPblock_18 | ungrounded | — |
| -7.376 | PROPblock_18 | ungrounded | — |
| 0.413 | PROPblock_18 | ungrounded | — |
| -6.963 | PROPblock_18 | ungrounded | — |
| -6.963 | PROPblock_18 | ungrounded | — |
| 0.00095 | PROPblock_18 | ambiguous | 2 sources |
| 0.95 | PROPblock_18 | ambiguous | 2 sources |
| 0.00063 | PROPblock_18 | uninspected_value | PROPblock_18 |
| 0.63 | PROPblock_18 | uninspected_value | PROPblock_18 |
| 0.00095 | PROPblock_18 | ambiguous | 2 sources |
| 0.95 | PROPblock_18 | ambiguous | 2 sources |
| 0.95 | PROPblock_18 | ambiguous | 2 sources |
| 0.00095 | PROPblock_18 | ambiguous | 2 sources |
| 298.15 | PROPblock_18 | verified | — |
| 0.3 | PROPblock_18 | verified | — |
| 0.0024775 | PROPblock_18 | misattributed | PROPblock_3 |
| 3.14 | PROPblock_18 | ungrounded | — |
| 0.00034 | PROPblock_18 | verified | — |
| 0.00081 | PROPblock_18 | verified | — |
| 0.59 | PROPblock_18 | uninspected_value | PROPblock_18 |
| 3.8 | PROPblock_18 | ungrounded | — |
| 3.9 | PROPblock_18 | ungrounded | — |
| 0.0009849 | PROPblock_18 | misattributed | PROPblock_3 |
| 0.051 | PROPblock_18 | misattributed | PROPblock_3 |
| 0.0005387 | PROPblock_18 | misattributed | PROPblock_3 |
| 0.95 | PROPblock_18 | ambiguous | 2 sources |
| 0.63 | PROPblock_18 | uninspected_value | PROPblock_18 |
| 0.89 | PROPblock_18 | misattributed | PROPblock_3 |
| 2.48 | PROPblock_18 | misattributed | PROPblock_3 |

## Violations

- **UNGROUNDED_LITERAL** PROPblock_18: +3.14 (near '…-----------|------|-----------------| | DMF–Water (1–2) | **…') matches no inspected row/stat, database table, or other source of PROPblock_18
- **UNINSPECTED_VALUE** PROPblock_18: +0.59 exists in PROPblock_18's database table but was never shown in an inspection of this run
- **UNGROUNDED_LITERAL** PROPblock_18: -0.01 (near '…ild dipolar interactions | | Water–Acetonitrile (2–3) | **≈ …') matches no inspected row/stat, database table, or other source of PROPblock_18
- **MISATTRIBUTED_VALUE** PROPblock_18: 0.0008045 does not belong to PROPblock_18; it matches only GLOBlit_9900::PROPblock_3 (inspected this run)
- **MISATTRIBUTED_VALUE** PROPblock_18: 0.0008903 does not belong to PROPblock_18; it matches only GLOBlit_9900::PROPblock_3 (inspected this run)
- **AMBIGUOUS_VALUE** PROPblock_18: 0.0003417 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **UNGROUNDED_LITERAL** PROPblock_18: -7.376 (near '….0008045) + (1/3) × ln(0.0008903) + (1/3) × ln(0.0003417) = …') matches no inspected row/stat, database table, or other source of PROPblock_18
- **UNGROUNDED_LITERAL** PROPblock_18: 3.14 (near '…-7.376  - **Excess (interaction) contribution:**   (1/9) × (…') matches no inspected row/stat, database table, or other source of PROPblock_18
- **UNINSPECTED_VALUE** PROPblock_18: 0.59 exists in PROPblock_18's database table but was never shown in an inspection of this run
- **UNGROUNDED_LITERAL** PROPblock_18: 3.72 (near '…n) contribution:**   (1/9) × (3.14 + 0.59 - 0.01) = (1/9) × …') matches no inspected row/stat, database table, or other source of PROPblock_18
- **UNGROUNDED_LITERAL** PROPblock_18: +0.413 (near '…ribution:**   (1/9) × (3.14 + 0.59 - 0.01) = (1/9) × 3.72 = …') matches no inspected row/stat, database table, or other source of PROPblock_18
- **UNGROUNDED_LITERAL** PROPblock_18: -7.376 (near '…9 - 0.01) = (1/9) × 3.72 = +0.413  - **Total:** ln(η_mix) = …') matches no inspected row/stat, database table, or other source of PROPblock_18
- **UNGROUNDED_LITERAL** PROPblock_18: 0.413 (near '…= (1/9) × 3.72 = +0.413  - **Total:** ln(η_mix) = -7.376 + 0…') matches no inspected row/stat, database table, or other source of PROPblock_18
- **UNGROUNDED_LITERAL** PROPblock_18: -6.963 (near '…3.72 = +0.413  - **Total:** ln(η_mix) = -7.376 + 0.413 = **-…') matches no inspected row/stat, database table, or other source of PROPblock_18
- **UNGROUNDED_LITERAL** PROPblock_18: -6.963 (near '…** ln(η_mix) = -7.376 + 0.413 = **-6.963**  - **η_mix = exp(…') matches no inspected row/stat, database table, or other source of PROPblock_18
- **AMBIGUOUS_VALUE** PROPblock_18: 0.00095 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **AMBIGUOUS_VALUE** PROPblock_18: 0.95 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **UNINSPECTED_VALUE** PROPblock_18: 0.00063 exists in PROPblock_18's database table but was never shown in an inspection of this run
- **UNINSPECTED_VALUE** PROPblock_18: 0.63 exists in PROPblock_18's database table but was never shown in an inspection of this run
- **AMBIGUOUS_VALUE** PROPblock_18: 0.00095 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **AMBIGUOUS_VALUE** PROPblock_18: 0.95 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **AMBIGUOUS_VALUE** PROPblock_18: 0.95 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **AMBIGUOUS_VALUE** PROPblock_18: 0.00095 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **MISATTRIBUTED_VALUE** PROPblock_18: 0.0024775 does not belong to PROPblock_18; it matches only GLOBlit_9900::PROPblock_3 (inspected this run)
- **UNGROUNDED_LITERAL** PROPblock_18: 3.14 (near '…lar associations that resist flow. The large positive G₁₂ = …') matches no inspected row/stat, database table, or other source of PROPblock_18
- **UNINSPECTED_VALUE** PROPblock_18: 0.59 exists in PROPblock_18's database table but was never shown in an inspection of this run
- **UNGROUNDED_LITERAL** PROPblock_18: 3.8 (near '…attributable to dipole–dipole interactions between DMF (μ ≈ …') matches no inspected row/stat, database table, or other source of PROPblock_18
- **UNGROUNDED_LITERAL** PROPblock_18: 3.9 (near '…interactions between DMF (μ ≈ 3.8 D) and acetonitrile (μ ≈ 3…') matches no inspected row/stat, database table, or other source of PROPblock_18
- **MISATTRIBUTED_VALUE** PROPblock_18: 0.0009849 does not belong to PROPblock_18; it matches only GLOBlit_9900::PROPblock_3 (inspected this run)
- **MISATTRIBUTED_VALUE** PROPblock_18: 0.051 does not belong to PROPblock_18; it matches only GLOBlit_9900::PROPblock_3 (inspected this run)
- **MISATTRIBUTED_VALUE** PROPblock_18: 0.0005387 does not belong to PROPblock_18; it matches only GLOBlit_9900::PROPblock_3 (inspected this run)
- **AMBIGUOUS_VALUE** PROPblock_18: 0.95 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
- **UNINSPECTED_VALUE** PROPblock_18: 0.63 exists in PROPblock_18's database table but was never shown in an inspection of this run
- **MISATTRIBUTED_VALUE** PROPblock_18: 0.89 does not belong to PROPblock_18; it matches only GLOBlit_9900::PROPblock_3 (inspected this run)
- **MISATTRIBUTED_VALUE** PROPblock_18: 2.48 does not belong to PROPblock_18; it matches only GLOBlit_9900::PROPblock_3 (inspected this run)

## Inspections (verbatim)

### INSP_469970d3baa4 — GLOBlit_8676::PROPblock_9 (complete, 11 rows shown)

_structured envelope entry (no markdown)_

### INSP_223a0880d59c — GLOBlit_9900::PROPblock_3 (rdp, 12 rows shown)

_structured envelope entry (no markdown)_

### INSP_5ce79feb1bd5 — GLOBlit_4124::PROPblock_6 (complete, 5 rows shown)

_structured envelope entry (no markdown)_

### INSP_fbc270263cf3 — GLOBlit_7481::PROPblock_18 (complete, 11 rows shown)

_structured envelope entry (no markdown)_

### INSP_98abce7cba9c — GLOBlit_2602::PROPblock_3 (rdp, 13 rows shown)

_structured envelope entry (no markdown)_
