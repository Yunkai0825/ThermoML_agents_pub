# L2 Leaf Evaluators

Focused single-card evaluators spawned by L1 workers.  Each evaluates one
aspect of a block (compound purity, measurement quality, reference metadata,
or property definitions) and returns a structured result within the token
budget set by ``L2_MAX_TOKENS`` in the query agent's argo config.

## Files

| File | Purpose |
|------|---------|
| `l2_dispatchers.py` | 4 dispatch functions: `dispatch_l2_{comp,meas,ref,prop}_eval` |
| `L2_comp_eval_workflow.md` | Compound DK+INDIV evaluation (purity, synonyms) |
| `L2_meas_eval_workflow.md` | Measurement method evaluation (DK+INDIV) |
| `L2_ref_eval_workflow.md` | Reference/paper evaluation (authors, journal, year) |
| `L2_prop_eval_workflow.md` | Property DK evaluation (definition, units, coverage) |

## Dispatch Signatures

All 4 dispatchers have the same interface:

```python
dispatch_l2_*_eval(
    purpose: str,        # What to evaluate
    instruction: str,    # Specific guidance from L1
    context: str,        # Block-level context passed from L1
    id_catalog: str = "" # Current ID catalog (JSON)
) -> str                 # Assembled downstream JSON result
```

## Tool Registries

| Evaluator | Working-agent search tools | Hidden post-answer constructor |
|-----------|----------------------------|--------------------------------|
| `L2_comp_eval` | `search_comp_from_block`, `search_compound_dk`, `search_compound_indiv` | `construct_l2_compounds` |
| `L2_meas_eval` | `search_meas_from_block`, `search_measurement_dk`, `search_measurement_indiv` | `construct_l2_measurements` |
| `L2_ref_eval` | `search_reference_from_block`, `search_references` | `construct_l2_reference` |
| `L2_prop_eval` | `search_prop_dk_from_block`, `search_property_dk` | `construct_l2_properties` |

Each hidden constructor lives in a separate one-tool catalog. It accepts only
`lit_num_id`, `block_number`, nullable `BLKsubsys_id`, `description`, and
the evaluator-specific validation IDs. It validates that exact target and its
checksums against the PCS block/subsystem manifest, then fills the remaining
fields from authoritative PCS/CCS/MTDKS/RMS cards. Constructor catalogs are not exposed to the working chemistry agents and cannot be mixed
between L2 evaluator types.

## Design

- **Stateless**: No memory, no children.  Receives context, returns result.
- **Budget**: 6 iterations, 90s max, L2-specific ArgoClient.
- **Parallel**: L1 can spawn multiple L2 evaluators via `asyncio.gather()`.
- **Working-agent output**: answer text only.
- **Post-answer output**: one anchor launches the claims agent, the minimal-ID
  agent, and the hidden answer-summary tool. The evaluator-specific constructor
  validates the minimal anchors and fills database-owned fields before strict
  reconstruction validation and deterministic JSON assembly.
