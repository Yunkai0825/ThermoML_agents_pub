# Component Definition Schema (CDS)

**Purpose**: Two-tier compound registry. **Identity cards** hold canonical chemical identity (one per unique compound). **Sample cards** hold per-paper sample provenance and purity (one per compound per paper). PCS cards reference CDS by InChIKey + DOI + sample_num.

## Tier 1: Compound Identity Card (`CDS_compound_identity_schema.json`)

**Scope**: ~8,502 unique compounds (by InChIKey). Plus ~59 graphite entries without InChI (keyed by name+formula fallback).

**Sections** (4):
- **identity**: InChIKey (primary key), InChI, formula
- **names**: primary_name + all_names[] (deduplicated across all papers; median 2, max 29)
- **substance_type**: "normal" (8,498) or "polymer" (4). Polymer carries Mn/Mw/Mz/Mv/PDI.
- **provenance**: paper_count, sample_record_count

**Token budget**: ~120 tok (simple) to ~400 tok (29 names)

**What is NOT here**: Sample source, purity, purification → Tier 2. Phase, measurements → PCS. Papers → RMS.

## Tier 2: Compound Sample/Purity Card (`CDS_compound_sample_schema.json`)

**Scope**: ~58,814 sample records across all papers. ~32,730 unique (source + purity) combinations after deduplication. 63% of compounds have exactly 1 unique record; water has 467.

**Key**: `{doi, InChIKey, sample_num}` — matches the PCS card's `{paper.doi, compounds[].InChIKey, compounds[].sample_num}`.

**Sections** (3):
- **key**: doi, InChIKey, sample_num
- **source**: eSource (98.9% have it) or eStatus (764 records)
- **purity_steps[]**: ordered purification/analysis steps, each with:
  - purity measurement (mass/mol/vol fraction + digits)
  - impurities (water, halide, unknown %)
  - analysis methods (24 standard + ~160 custom)
  - purification methods (24 standard + ~150 custom)

**Token budget**: ~60 tok (minimal) to ~200 tok (complex multi-step)

**1,899 compounds have no sample records** — identity-only entries (no purity reported in source papers).

## Cross-reference flow

```
PCS card                          CDS
──────────                        ───
compounds[i].InChIKey  ──────→  Identity card (names, formula, type)
paper.doi + 
compounds[i].InChIKey +
compounds[i].sample_num ──────→  Sample card (source, purity steps)
```

**Agent use**: Identity lookup for name resolution and chemical search. Sample lookup only when purity/provenance is needed for data quality assessment. Most queries never need the sample card — the PCS data_summary is usually sufficient for relevance filtering.