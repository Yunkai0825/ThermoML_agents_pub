# RMS_INDIV active schema

One RMS card represents one literature record.

```text
identity
  doi
  lit_id
  lit_num_id: GLOBlit_N
  trc_ref_id
bibliographic
content
data_inventory
  compound_list[]
    org_num: DOIcomp_N
    comp_num_id: GLOBcomp_N
  typed block inventory
```

The RMS card never assigns global compound identity from a DOI ordinal. It
records both fields explicitly. Retired `comp_N` values are not part of the
active schema.
