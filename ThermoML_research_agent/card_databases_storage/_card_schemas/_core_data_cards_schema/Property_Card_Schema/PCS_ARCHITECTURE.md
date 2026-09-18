# PCS active schema

One PCS_INDIV card contains every property or reaction block for one DOI.

```text
key: doi, lit_id, GLOBlit_N
blocks_summary.block_index[].block_number: PROPblock_N | RXNblock_N
blocks[]
  block_number: PROPblock_N | RXNblock_N
  blocktype_num_id: GLOBblocktype_N
  compounds[]: DOIcomp_N -> GLOBcomp_N
  properties[]: BLKprop_N -> GLOBprop_N and GLOBmeas_N
  variables[]: BLKvar_N -> GLOBvar_N
  constraints[]: BLKconstr_N -> GLOBconstr_N
  reaction: GLOBrxntype_N and DOIcomp_N participants
  data_points[]
    variable_values.BLKvar_N
    property_values.BLKprop_N
```

The point dictionaries deliberately use block-local declaration IDs. They are
resolved with `(doi, block_number)` and are never promoted to global IDs.
Component-linked declarations retain both an exact global type ID and their
`component_org_num=DOIcomp_N` occurrence reference.
