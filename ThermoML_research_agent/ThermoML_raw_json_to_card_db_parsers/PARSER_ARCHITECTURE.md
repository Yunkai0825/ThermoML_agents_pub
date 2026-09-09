# ThermoML raw-JSON to card/database parser architecture

The parser projects the NIST ThermoML raw corpus into four per-literature card
families, global ID/DK cards, canonical CSV registries, denormalized block
registries, and the cross-card `ThermoML_index.db`. All generated identifiers
follow the strict `prefixed-v2` grammar in `id_schema.py`.

## Data flow

```text
thermoml_raw.db / compressed raw corpus
  -> raw_loader.py
  -> ThermoMLIndex (canonical CSV lookup)
  -> RMS / CCS / MTDKS / PCS builders
  -> Individual_cards_dbs/*.db
  -> PM and Reaction registry builders
  -> ThermoML_index.db
  -> search tools, browser, query agent, analysis agent, specialized pipelines
```

## Card families

| Card | Scope | Principal identifiers |
|---|---|---|
| RMS_INDIV | one literature/DOI | `doi`, `lit_id`, `GLOBlit_N` |
| CCS_INDIV | compounds and samples declared by one DOI | `DOIcomp_N`, `DOIcompSample_<compound>_<sample>`, global `GLOBcomp_N` references |
| MTDKS_INDIV | measurement descriptions in one DOI | `GLOBmeas_N` references and typed `PROPblock_N`/`RXNblock_N` references |
| PCS_INDIV | property/reaction blocks in one DOI | typed blocks; `BLKprop_N`, `BLKvar_N`, `BLKconstr_N`; global type/method/phase IDs |
| CCS_ID_DK | one global compound | `GLOBcomp_N` |
| MTDKS_ID_DK | one global measurement method | `GLOBmeas_N` |
| PCS_ID_DK | one global property type | `GLOBprop_N` |

## PCS block projection

For every source `PureOrMixtureData` block the builder emits
`PROPblock_N`; every `ReactionData` block emits `RXNblock_N`.

```text
block
  block_number: PROPblock_N | RXNblock_N
  blocktype_num_id: GLOBblocktype_N
  compounds[]
    org_num: DOIcomp_N
    comp_num_id: GLOBcomp_N
  properties[]
    BLKprop_id: BLKprop_N
    prop_num_id: GLOBprop_N
    meas_num_id: GLOBmeas_N
    component_org_num: DOIcomp_N | null
    property_phase.phase_num_id: GLOBphase_N
    uncertainty.assessment_num: BLKpropAssessment_<prop>_<assessment>
  variables[]
    BLKvar_id: BLKvar_N
    var_num_id: GLOBvar_N
    component_org_num: DOIcomp_N | null
  constraints[]
    BLKconstr_id: BLKconstr_N
    constr_num_id: GLOBconstr_N
    component_org_num: DOIcomp_N | null
  reaction
    rxn_type_num_id: GLOBrxntype_N
    participants[].org_num: DOIcomp_N
  data_points[]
    variable_values.BLKvar_N -> variables[].BLKvar_id
    property_values.BLKprop_N -> properties[].BLKprop_id
```

Component-linked canonical types use `{DOIcomp_id}` in registry templates and
resolve to occurrences such as `mole_fraction_DOIcomp_1`. The corresponding
`var_num_id`, `prop_num_id`, or `constr_num_id` remains global.

## Builder invariants

- Raw ThermoML ordinals are source data only; constructors in `id_schema.py`
  must format them before writing any generated artifact.
- Every populated `*_num_id` is an exact `GLOB*` string.
- DOI compound occurrences are never promoted to global identity without the
  explicit `comp_num_id` mapping.
- A block-local ID is safe only with `(doi, block_number)`.
- Retired unscoped IDs, bare ID ordinals, `{comp_id}`, and generic `number`
  declaration fields are rejected rather than converted.

## Data points and summaries

`build_pcs_card(..., max_datapoints_per_block=50)` stores at most the configured
number of point rows per block while `data_summary` is calculated over the
complete source block. Pass `None` only in an explicitly configured build that
must materialize every point. Tool-result compactors are downstream of this
card projection and never manufacture fields absent from the card.

## Validation and rebuild

Run `_publication_audit/validate_prefixed_rebuild.py` (workspace root) after
rebuilding the CSV and SQLite
artifacts. It checks ID grammar, nested references, component templates, typed
blocks, database metadata, and cross-card counts. Public search boundaries add
`ID_REFINEMENT_REQUIRED` responses so retired IDs cannot enter agent memory or
tool-result compaction.
