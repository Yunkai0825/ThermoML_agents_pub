# Card Workflows Search Tools

Multi-tier search tool library for the ThermoML card database.
Used by the agentic system (L1/L2 layers) and the Flask web browser.

## Directory Structure

```
card_db_search_tools/
├── basic_search_tools/            # 12 public search/extraction functions
│   ├── ARCHITECTURE.md            # Full API reference
│   ├── _id_alignment_search.py    # Shared fuzzy name→num_id resolution
│   ├── normalization_helpers/     # resolve_compound(), fuzzy matching
│   ├── 1_block_search.py          # search_blocks()
│   ├── 2_system_registry_search.py
│   ├── 3_compound_DK_search.py
│   ├── 4_reference_search.py
│   ├── 5_meas_DK_search.py
│   ├── 6_meas_INDIV_search.py
│   ├── 7_prop_DK_search.py
│   ├── 8_compound_INDIV_search.py
│   ├── 9_system_summary_search.py
│   ├── 10_compound_similarity_search.py  # Morgan fingerprint Tanimoto
│   ├── 11_block_data_extractor.py        # Raw data point extraction
│   ├── 12_block_search_adv.py             # Strict advanced block query
│   └── advanced_block_search/             # Private exact-row engine
│
├── block_centric_search_tools/    # Multi-DB: block → compound/method/ref DK+INDIV
├── comp_centric_search_tools/     # Multi-DB: compound → all related cards
├── meas_centric_search_tools/     # Multi-DB: measurement → related cards
└── pcs_doi_centric_search_tools/  # Multi-DB: DOI → all cards for that paper
```

## Design Pattern

**Basic tools** (numbered 1–11) each wrap ONE database with ONE public
function. Input is human-friendly (names, formulas, DOIs); output is
`{"query_params": {...}, "n_results": N, "results": [...]}`.

`block_search_adv` (tool 12) is intentionally separate from `search_blocks`.
It combines the two block registries, the embedded PCS
`blocks_summary.derived_indexes.block_search_adv` index, and uncapped raw
ThermoML `NumValues` for strict role-aware SQL-shaped queries. Its result is
compacted by
`_tools_results_compactors/basic_search_tools/block_search_adv_compactor.py`;
the ordinary block-search JSON and Markdown behavior is not changed.

**Higher-level tools** (block/comp/meas/doi-centric) combine multiple
basic tools into single convenience functions for common query patterns.
Used primarily by L2 leaf evaluators.

## Consumers

| Consumer | Tools Used |
|----------|-----------|
| L1 Query Worker | basic tools 1–10 and advanced tool 12 |
| L2 Compound Eval | `search_compound_dk`, `search_compound_indiv` |
| L2 Measurement Eval | `search_measurement_dk`, `search_measurement_indiv` |
| L2 Reference Eval | `search_references` |
| L2 Property Eval | `search_property_dk` |
| Analysis Agent | `extract_block_csv` (tool 11) |
| Flask Browser | `search_blocks`, `search_system_registry`, `search_similar_compounds` |
