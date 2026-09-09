# ThermoML chemistry question and batch-call matrix

This matrix tests the active Query L1 runtime catalog, not the broader
auto-discovery registry. The runtime surface is:

- 11 retained L1 database/search tools, each with deterministic JSON-to-Markdown
  compaction.
- 4 L1-to-L2 delegation tools.
- 10 database tools inside the four L2 evaluators.

All compacted L1 calls require nonempty `purpose` and `tasks`. Calls in the
tables omit those two repeated wrapper fields for readability.

## Common chemistry questions

| ID | Natural question | Intended route | Stable evidence |
|---|---|---|---|
| C01 | What are the canonical identities of water, carbon dioxide, and methanol? | `resolve_compound_ids` | `GLOBcomp_1`, `GLOBcomp_3`, `GLOBcomp_4` |
| C02 | Resolve mass density, viscosity, and thermal conductivity. | `resolve_property_ids` | `GLOBprop_1`, `GLOBprop_4`, `GLOBprop_34` |
| C03 | Resolve DSC and hot-wire methods. | `resolve_measurement_ids` | `GLOBmeas_132`, `GLOBmeas_41` |
| C04 | Identify DOI `10.1007/s10765-005-5566-6`. | `resolve_reference_ids` | `GLOBlit_1` and exact DOI |
| C05 | Resolve temperature, pressure, mole fraction, liquid, and gas in their typed catalogs. | Independent `resolve_ids` batch for variable, constraint, and phase | Typed IDs remain in their own namespaces |
| C06 | I only remember “thermal conductivity”; show its catalog identity. | `search_id_alignment` | Includes `GLOBprop_34`; no guessed suffix |
| C07 | List unary gas CO2 conductivity blocks covering 425–429 K and 1–5 MPa. | `search_blocks` | Patek DOI, `PROPblock_1`; ranges are block-overlap filters |
| C08 | List binary PureOrMixtureData blocks containing both water and CO2. | `search_system_registry` | Exact two-component registry rows; no redundant rich search |
| C09 | How much conductivity data exists for unary CO2? | Only `search_system_summary` | Positive block, paper, and point counts |
| C10 | Find five Morgan-fingerprint analogues of methanol above similarity 0.2. | Resolve methanol, wait, then `search_similar_compounds` | Five typed IDs; nonincreasing scores |

## Complicated chemistry questions

| ID | Natural question | Intended route | Main edge exercised |
|---|---|---|---|
| A01 | In Patek's CO2 paper, average gas conductivity over 151.85–155.85 °C and 1–5 MPa, requiring four aligned points. | `block_search_adv` | Unit normalization, constraint-ID-to-variable translation, row alignment, aggregate |
| A02 | Rank binary ionic-liquid excess-enthalpy blocks by mean `ABS(H^E)/(x*(1-x))` over x=0.2–0.8 at 298–299 K and 101–102 kPa. | `block_search_adv` | Component binding, fixed constraints, nested math, ordering |
| A03 | Find potassium-benzoate reaction enthalpy near 298 K and 200 kPa, retaining values at or below -600 kJ/mol. | `block_search_adv` | ReactionData, target-scoped inline state, negative unit literal |
| A04 | Count complete feed/product composition rows for methanol + 2,2'-oxybisbutane + water liquid-liquid equilibrium. | `block_search_adv` | Ternary component/phase qualification and missing cells |
| A05 | Return each legitimate ether mole-fraction phase occurrence separately. | `block_search_adv` with `CARDINALITY EACH` | One block with multiple independently aggregated bindings |
| A06 | For one selected block, summarize compounds, properties, methods, and reference metadata. | Batch `L2_comp_eval`, `L2_prop_eval`, `L2_meas_eval`, `L2_ref_eval` | Four independent delegations with the same explicit DOI/block context |

## Valid ordered batches

The synchronous ReAct engine executes same-turn calls in emitted order. A
batch is not concurrent.

1. Batch independent compound, property, measurement, and reference
   resolutions before one `<wait/>`.
2. After IDs are known, batch two independent `search_blocks` questions.
3. After one block is selected, batch the four L2 domain evaluations.
4. Batch the independent CO2 conductivity and potassium-benzoate reaction
   advanced searches.

Do not batch a resolver with a search that needs the resolver's returned ID.
The dependent search must be emitted on the next turn. A call written after
`<wait/>` is counted as deferred and discarded; it must be re-emitted.

## Negative parser, schema, and routing cases

| ID | Deliberate bad case | Required behavior |
|---|---|---|
| N01 | One valid call plus malformed JSON sibling | Reject the complete batch; run nothing |
| N02 | Duplicate JSON key at any depth | Reject as noncanonical JSON |
| N03 | `NaN`, `Infinity`, `-Infinity`, or overflowing `1e400` | Reject as non-finite JSON |
| N04 | Unknown tool or undeclared argument beside a valid call | Atomic preflight; valid sibling held |
| N05 | Advanced call with `compound_list`, `target_identity`, or `compute` | Reject retired v1 names |
| N06 | Advanced target represented by a dictionary | Reject nesting; targets are strings |
| N07 | `system_type="pure"` | Reject; canonical value is `unary` |
| N08 | Non-component conductivity target with `COMPONENT` | Reject chemically inapplicable qualifier |
| N09 | Empty advanced `targets` | Reject; a measured result is mandatory |
| N10 | Compare temperature directly with pressure | Reject dimensional mismatch |
| N11 | Ask `search_blocks` to filter on a variable/constraint ID | Route exact row-state work to `block_search_adv` |
| N12 | Count blocks by calling all discovery tools | Route counting only to `search_system_summary` |
| N13 | Oversized first result in a two-call batch | Return a per-call compaction error and still execute the sibling |
| N14 | Inspect a stage-compacted batch on the next turn | Temporary `inspect_batch_result` must retain the cached full result |

## Auxiliary extraction limitation

`extract_block_csv` and `extract_multi_block_csv` are public helper functions
but are not registered in active Query L1. They execute successfully and label
merged rows, but currently read the PCS card's 50 displayed rows rather than
the full raw block:

| Block | Returned rows | Embedded `n_datapoints` |
|---|---:|---:|
| Patek `PROPblock_1` | 50 | 77 |
| Patek `PROPblock_2` | 50 | 180 |

The regression suite records the uncapped-export contract as an explicit
strict xfail. It must not be reported as a full-data pass.

## Executable coverage

- `test_runtime_catalog_contracts.py`: exact runtime inventory, signatures,
  compactor coverage, and agent-facing description drift.
- `test_live_chemistry_tools.py`: all 12 live L1 searches, all 10 L2 database
  tools, deterministic compaction, and auxiliary extraction.
- `test_react_batch_contracts.py`: canonical wire parsing, wait barriers,
  atomic gates, ordered execution, real complex batches, four L2 delegations,
  stage-result inspection, and oversized-result isolation.
