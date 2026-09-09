# Utility Summary Schema (USS)

**Purpose**: The agent's "table of contents" — a compact global summary of the entire database. This is the FIRST thing an agent reads to understand what's available before making any targeted queries. Critical for context window management.

**Scope**: One file (or a small set of summary files) covering the entire database.

**Core content**:

### Database Overview:
- Total papers: 11,923
- Total unique compounds: ~8,517 (by InChI)
- Total unique compound names: ~22,587
- Total measurement blocks: 123,727 (122,481 PureOrMixture + 1,246 Reaction)
- Total data points: ~2.7M
- DOI prefixes: 10.1016 (Elsevier), 10.1021 (ACS), 10.1063 (AIP)

### System Distribution:
- Unary systems: ~46K blocks
- Binary systems: ~58K blocks
- Ternary systems: ~18K blocks
- Quaternary+: ~1K blocks
- Unique systems (deduplicated): ~4,000–6,000

### Property Coverage:
- 13 PropertyGroups (11 PureOrMixture + 2 Reaction)
- 105 distinct property names observed in data (of 188 defined in schema)
- Per-group block counts and data point counts
- Top-N most measured properties

### Phase Coverage:
- Top phases: Liquid (59K), Liquid+Gas VLE (19K), Liquid+Crystal SLE (12K), LLE (5.6K+2.7K)
- Crystal, Gas, Fluid, Solution, Glass all represented

### Temporal Coverage:
- Publication year range and distribution

### Quick Lookup Indexes:
- PropertyGroup → list of property names → block counts
- Compound name → compound_id (most common ~100 compounds)
- Common system shortcuts (e.g., "water+ethanol" → system_id)

**Agent use**: Read first to scope queries. Decide which SCS/CDS/PCS to load. Avoid loading everything when a summary suffices. Answer "how much data exists for X?" without touching PCS.