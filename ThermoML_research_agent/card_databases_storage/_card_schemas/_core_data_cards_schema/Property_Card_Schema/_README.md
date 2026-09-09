# Property Card Schema — Directory README

## Architecture

Two-tier design following the universal card pattern (same as CCS, MTDKS):

- **Tier 1 — ID & Domain Knowledge**: One card per unique property (105 total). Static identity + domain knowledge.
- **Tier 2 — INDIV Snapshot**: One card per paper/DOI (11,923 total). All experimental blocks and data points from that paper.

## File Structure

```
Property_Card_Schema/
├── PCS_property_ID_and_DK_schema.json     # Per-property DK card schema (v1.0.0)
├── PCS_property_INDIV_snapshot_schema.json # Per-DOI block data card schema (v3.0.0)
├── PCS_property_summary.json              # Global property catalog (105 properties × 12 groups)
├── PCS_purpose.md                         # Purpose and usage documentation
├── _README.md                             # This file
├── PCS_ID_and_DK_cards/                   # Generated ID_and_DK card instances (105 cards)
└── _obsolete/                             # Previous schema versions
    ├── _base_card_schema.json             # v1.0.0 — per-property design (1 card per property per block)
    ├── _block_card_schema.json            # v2.0.0 — per-block design (1 card per block)
    ├── STAT_PCS_data_summary_schema.json  # Data summary schema (still referenced by INDIV blocks)
    └── PCS_property_BLOCK_datablock_schema.json  # Unused placeholder
```

## Schema Sections

### ID_and_DK (`PCS_property_ID_and_DK_schema.json` v1.0.0)

| Section | Contents |
|---------|----------|
| prop_ID | Primary key — slugified property name |
| identity | name, unit, symbol, dimension, group, class, boolean flags, aliases, typical_variables, typical_constraints, db_usage |
| domain_knowledge.structured_block | definition, measurement_context, phase_applicability, typical_ranges, uncertainty_profile, data_patterns |
| domain_knowledge.description_block | 12 prose sections for LLM reasoning |

### INDIV Snapshot (`PCS_property_INDIV_snapshot_schema.json` v3.0.0)

| Section | Contents |
|---------|----------|
| key | doi + lit_id (primary key) |
| paper | doi + title (lightweight → RMS) |
| blocks_summary | n_blocks, property/compound/method lists, T/P ranges, block_index[] |
| blocks[] | Array of blocks, each with: compounds, properties, variables, constraints, data_summary, data_points, reaction, provenance |

## Design Evolution

| Version | Schema | Design | Key Change |
|---------|--------|--------|------------|
| v1.0.0 | `_base_card_schema.json` | Per-property per-block | 1 card = 1 property from 1 block. Duplicated shared block context. |
| v2.0.0 | `_block_card_schema.json` | Per-block | 1 card = 1 block (1–6 properties). Eliminated duplication. |
| v3.0.0 | `PCS_property_INDIV_snapshot_schema.json` | Per-DOI | 1 card = 1 paper (all blocks). Uniform INDIV pattern across all schemas. |

## Cross-Card References

```
PCS INDIV.key.doi                          → RMS card
PCS INDIV.blocks[].compounds[].comp_id     → CCS Identity card
PCS INDIV.blocks[].properties[].prop_ID    → PCS ID_and_DK card
PCS INDIV.blocks[].properties[].meas_ID    → MTDKS ID_and_DK card
```

## Key Concepts

**Variables vs Constraints**: Variables are conditions *swept* across data points (e.g., temperature series). Constraints are *fixed* for all points in a block (e.g., constant pressure at 101.325 kPa).

**Multi-property blocks**: 2.5% of blocks contain 3–6 properties, always the same property group. Each data point carries values for ALL properties. 97.5% are single-property.

**blocks_summary for navigation**: The `blocks_summary.block_index[]` array gives a one-line-per-block index (property names, system type, n_points, method) so agents can jump to relevant blocks without reading full data.

**data_summary for screening**: Each block's `data_summary` (~150–400 tokens) provides min/max/mean/std for properties and variables, methods, phases — enough for relevance filtering without loading data_points.

## Token Budgets

| Level | Tokens |
|-------|--------|
| ID_and_DK card | ~300–800 |
| INDIV blocks_summary | ~100–500 |
| INDIV per-block data_summary | ~150–400 |
| INDIV per-block full (50 pts) | ~2–5K |
| INDIV full card (large paper) | up to 100K+ |
