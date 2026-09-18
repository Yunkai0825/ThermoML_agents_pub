# CCS active schema

## CCS_INDIV

One card represents the compounds and samples declared by one DOI.

```text
key: doi, lit_id, GLOBlit_N
compounds[]
  org_num: DOIcomp_N
  comp_num_id: GLOBcomp_N
  inchi_key, name, formula
  samples[]
    sample_num: DOIcompSample_<compound ordinal>_<sample ordinal>
    source, status, purity_steps[]
```

Safe keys are `(doi, org_num)` for a compound occurrence and
`(doi, org_num, sample_num)` for a sample. `comp_num_id` points to global
CCS_ID_DK identity; it never replaces the occurrence key.

## CCS_ID_DK

One card represents one canonical `GLOBcomp_N`, with structure identifiers,
canonical name, aliases, formula, and fingerprints where available.
