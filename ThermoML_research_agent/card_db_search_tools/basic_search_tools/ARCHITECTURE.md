# Search Tools — Architecture

> **Version**: 2.1  
> **Updated**: 2026-07-24

## Overview

12 public search/extraction functions. Tools 1–11 retain their existing
single-purpose behavior. Tool 12 is the strict advanced-query exception: it
coarsely searches both block registries, binds the embedded PCS identity
index, and evaluates uncapped raw `NumValues`.

1. Agent passes human-friendly input (names, formulas, DOIs, keywords)
2. `_id_alignment_search` + `normalization_helpers/` resolve to `num_id`s
3. Single SQLite query against the appropriate card database
4. Returns `{"query_params": {...}, "n_results": N, "results": [...]}`

**Type Coercion:** Several functions coerce numeric parameters from strings
to the appropriate type (`int(limit)`, `float()`) to handle LLM-generated
JSON where numbers may arrive as quoted strings.

## Directory Structure

```
basic_search_tools/
├── _id_alignment_search.py        # Shared fuzzy name→num_id resolution
├── normalization_helpers/
│   ├── resolve.py                 # resolve_compound(), fuzzy matching
│   └── ...
├── 1_block_search.py              # search_blocks()
├── 2_system_registry_search.py    # search_system_registry()
├── 3_compound_DK_search.py        # search_compound_dk()
├── 4_reference_search.py          # search_references()
├── 5_meas_DK_search.py            # search_measurement_dk()
├── 6_meas_INDIV_search.py         # search_measurement_indiv()
├── 7_prop_DK_search.py            # search_property_dk()
├── 8_compound_INDIV_search.py     # search_compound_indiv()
├── 9_system_summary_search.py     # search_system_summary()
├── 10_compound_similarity_search.py  # search_similar_compounds()
├── 11_block_data_extractor.py     # extract_block_csv()
├── 12_block_search_adv.py         # block_search_adv()
├── advanced_block_search/         # Private validation/binding/row engine
├── test_all_search_tools.py       # Integration tests
└── purpose.md                     # Original design intent
```

## API Reference

### Tool 1: `search_blocks`
```python
search_blocks(
    compound=None,          # name/formula/SMILES/InChI/comp_num_id
    property=None,          # property name/prop_id/prop_num_id
    measurement=None,       # method name/meas_id/meas_num_id
    literature=None,        # DOI/lit_id/lit_num_id
    system_type=None,       # "pure", "binary", "ternary", etc.
    phase=None,             # "Liquid", "Gas", etc.
    temperature_range=None, # (T_min, T_max) in K
    pressure_range=None,    # (P_min, P_max) in kPa
    limit=50                # max results (coerced to int)
) -> dict
```
Returns block-level results with compounds, properties, variables, constraints.
Includes `int(limit)` and `float()` coercion in `_ranges_overlap()`.

### Tool 2: `search_system_registry`
```python
search_system_registry(
    compound=None,
    property=None,
    system_type=None,       # "pure", "binary", "ternary"
    block_type=None,        # "PM" or "RD"
    literature=None,
    n_components=None,      # exact component count
    phase=None,
    temperature_range=None,
    pressure_range=None,
    n_datapoints_min=None,  # minimum data points per block
    include_reactions=False, # include ReactionData blocks
    limit=100               # coerced to int
) -> dict
```
Block metadata search (no data points, fast overview).

### Tool 3: `search_compound_dk`
```python
search_compound_dk(
    compound=None,          # name, formula, SMILES, InChI
    limit=5
) -> dict
```
Returns compound identity cards with SMILES, formula, `has_fingerprint` flag.

### Tool 4: `search_references`
```python
search_references(
    literature=None,        # DOI, lit_id, lit_num_id
    author=None,            # partial name match
    year=None,              # exact year (coerced to int)
    year_range=None,        # (start_year, end_year) (coerced to int)
    compound=None,          # filter by compound
    property=None,          # filter by property
    journal=None,
    title_keywords=None,    # title keyword search
    limit=50
) -> dict
```

### Tool 5: `search_measurement_dk`
```python
search_measurement_dk(measurement, limit=5) -> dict
```

### Tool 6: `search_measurement_indiv`
```python
search_measurement_indiv(
    method=None,
    doi=None,
    compound=None,          # filter papers containing this compound
    limit=50
) -> dict
```

### Tool 7: `search_property_dk`
```python
search_property_dk(property, prop_group=None, limit=5) -> dict
```

### Tool 8: `search_compound_indiv`
```python
search_compound_indiv(
    compound=None,
    doi=None,
    min_purity=None,        # e.g. 0.99
    limit=50
) -> dict
```

### Tool 9: `search_system_summary`
```python
search_system_summary(
    compound=None,          # one string or a native list[str]
    property=None,
    system_type=None,       # "pure", "binary", "ternary"
    temperature_range=None,
    pressure_range=None,
    include_reactions=False,
    limit=20
) -> dict
```
Returns aggregated statistics: total blocks, data points, DOI count,
property distribution, co-occurrence counts.

### Tool 10: `search_similar_compounds`
```python
search_similar_compounds(
    comp_num_id=None,       # direct compound ID
    smiles=None,            # SMILES string
    inchi=None,             # InChI string
    name=None,              # compound name (resolved internally)
    top_k=10,               # number of results
    min_similarity=0.0,     # Tanimoto threshold
    metric="morgan"         # "morgan" or "maccs"
) -> dict
```
Morgan fingerprint Tanimoto similarity search against CCS_ID_DK.db.

### Tool 11: `extract_block_csv`
```python
extract_block_csv(
    doi: str,
    block_number: str | int,
    *,
    property_filter: str | None = None
) -> dict
```
Returns resolved column names (`mole_fraction_<ethanol>`) + data as
dict-of-lists. Used by the analysis agent; not exposed to the query agent.

### Tool 12: `block_search_adv`

```python
block_search_adv(
    compound_list=None,
    para_identity=None,
    target_identity=None,
    literature=None,
    phase=None,
    filtering_identity=None,
    constraint_filter=None,
    inline_state_filter=None,
    where=None,
    minimum_common_points=None,
    compute=None,
    select=None,
    having=None,
    order_by=None,
    limit=50,
    explanation="",
    schema="block_search_adv/v1",
) -> dict
```

This is the uncommon-query path for exact row filtering, nested arithmetic,
aggregation, `having`, and stable sorting. It uses the global
property-variable-constraint translation only to identify the physical
quantity; requested chemistry roles remain strict:

- `para_identity` binds variables.
- `target_identity` binds properties.
- `constraint_filter` binds block constraints.
- `inline_state_filter` binds target-linked ReactionData inline state.

One result represents one typed `(doi, PROPblock_N|RXNblock_N)` block.
Legitimate `cardinality="all"` alternatives are retained in its
`binding_matches`; alias permutations never duplicate a block.

The dedicated deterministic compactor is
`_tools_results_compactors/basic_search_tools/block_search_adv_compactor.py`.
It emits bounded Markdown with DOI, typed block ID, actual occurrence roles,
fixed-state evidence, point counts, and selected values. It deliberately
omits raw rows, embedded permutations/statistics, and the full normalized
query. Existing `search_blocks` and its compactor are unchanged.

## Higher-Level Search Tools

| Directory | Pattern |
|-----------|---------|
| `block_centric_search_tools/` | Start from a block → fetch compound/method DK+INDIV |
| `comp_centric_search_tools/` | Start from a compound → fetch all related cards |
| `meas_centric_search_tools/` | Start from a measurement → fetch related cards |
| `pcs_doi_centric_search_tools/` | Start from a DOI → fetch all cards for that paper |

These combine multiple basic_search_tools into single convenience functions.
