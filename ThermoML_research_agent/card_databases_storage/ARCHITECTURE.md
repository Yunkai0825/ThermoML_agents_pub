# ThermoML card database architecture (`prefixed-v2`)

This directory contains the active generated card databases, canonical ID
CSVs, denormalized block registries, and the cross-card search index.

The measured file inventory and rebuild prerequisites are in [docs/DATA.md](../../docs/DATA.md). The zero-byte `PCS_INDIV.db` at this directory level is an unused placeholder; the active property database is `Individual_cards_dbs/PCS_INDIV.db`.

## Active databases

| Database | Identity |
|---|---|
| `Individual_cards_dbs/RMS_INDIV.db` | one row per DOI / `GLOBlit_N` |
| `Individual_cards_dbs/CCS_INDIV.db` | one DOI compound map using `DOIcomp_N` and `GLOBcomp_N` |
| `Individual_cards_dbs/MTDKS_INDIV.db` | methods in one DOI using `GLOBmeas_N` and typed block references |
| `Individual_cards_dbs/PCS_INDIV.db` | typed property/reaction blocks and block-local declaration IDs |
| `Individual_cards_dbs/CCS_ID_DK.db` | one card per `GLOBcomp_N` |
| `Individual_cards_dbs/MTDKS_ID_DK.db` | one card per `GLOBmeas_N` |
| `Individual_cards_dbs/PCS_ID_DK.db` | one card per `GLOBprop_N` |
| `PureOrMixtureData_registry.db` | denormalized `PROPblock_N` rows |
| `ReactionData_registry.db` | denormalized `RXNblock_N` rows |
| `ThermoML_index.db` | normalized cross-card search index |

## Scope contract

- Every `*_num_id` is a typed global `GLOB*` string.
- DOI compound declarations use `DOIcomp_N`; samples use
  `DOIcompSample_<compound>_<sample>`.
- Blocks use `PROPblock_N` or `RXNblock_N`.
- Property, variable, and constraint declarations use `BLKprop_N`, `BLKvar_N`,
  and `BLKconstr_N` in their named fields, never generic `number`.
- Component-linked registry templates contain `{DOIcomp_id}`.
- Bare ordinals and retired unscoped IDs are invalid at every tool boundary.

Canonical CSV headers and normalized index tables are documented in
[the parser index-builder directory](../ThermoML_raw_json_to_card_db_parsers/_index_builder/).
