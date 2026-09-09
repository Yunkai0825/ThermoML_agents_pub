# Data, provenance, and database maintenance

This guide describes the data present in this workspace, inspected read-only on **2026-09-09**. Paths below are relative to the repository root unless stated otherwise. Installation and launch instructions are in the [root README](../README.md).

## Source and provenance

The source snapshot is **NIST ThermoML v2020-09-30**. NIST describes this release as covering archive entries published through 2019, distributed as paired JSON/XML files in DOI-prefix directories. NIST generates the ThermoML XML representation from JSON; the JSON can contain additional fields. The original release and its published archive checksum are available in the [NIST data record](https://data.nist.gov/pdr/lps/ark%3A/88434/mds2-2422). The [NIST archive overview](https://www.nist.gov/mml/acmd/trc/thermoml/thermoml-archive) describes the contributing journals and publisher cooperation.

The local SQLite stores and generated cards are project representations of that snapshot. They are not a newer NIST release. Local inspection found publication years **2003–2019** in `papers`. Source DOIs and the original paper metadata remain available for tracing a result to its publication.

### License boundary and citation request

The MIT license in [LICENSE](../LICENSE) covers this project's code, documentation, and other original material. Content originating from the ThermoML Archive is NIST public data, published with the permission of the cooperating journal publishers, and is not licensed by this project; the third-party data notice in [NOTICE](../NOTICE) records this boundary, NIST's copyright and fair-use terms, and the NIST/TRC liability statement. NIST/TRC do not warrant the correctness of archive values; check a value against its source publication before relying on it.

NIST asks that published research using ThermoML data cite:

- Riccardi, D.; Trautt, Z.; Bazyleva, A.; Paulechka, E.; Diky, V.; Magee, J. W.; Kazakov, A. F.; Townsend, S. A.; Muzny, C. D. *Towards improved FAIRness of the ThermoML Archive.* J. Comput. Chem. **2022**, 43 (12), 879–887. [doi:10.1002/jcc.26842](https://doi.org/10.1002/jcc.26842)
- Riccardi, D.; Bazyleva, A.; Paulechka, E.; Diky, V.; Magee, J. W.; Kazakov, A. F.; Townsend, S. A.; Muzny, C. D. *ThermoML/Data Archive*; National Institute of Standards and Technology, **2021**. [doi:10.18434/mds2-2422](https://doi.org/10.18434/mds2-2422)

Both references are also recorded under `references` in [CITATION.cff](../CITATION.cff). Results traced through this workspace should additionally cite the original publication identified by the block's DOI.

## Included SQLite files

The workspace contains **12 nonempty SQLite files totaling 4,875,669,504 bytes** (about 4.88 GB), plus one empty placeholder. This total excludes CSVs, authored knowledge cards, code, and run artifacts. Counts are database rows, not independent experimental measurements.

| Location | Bytes | Principal contents |
|---|---:|---|
| `ThermoML_research_agent/ThermoML.v2020-09-30.db/thermoml_raw.db` | 2,014,683,136 | 11,923 paper JSON records and raw query indexes |
| `ThermoML_research_agent/ThermoML.v2020-09-30.db/thermoml_raw_corpus.db` | 388,104,192 | 11,923 paired, independently compressed JSON/XML documents |
| `ThermoML_research_agent/card_databases_storage/Individual_cards_dbs/CCS_ID_DK.db` | 35,622,912 | 8,526 global compound cards |
| `ThermoML_research_agent/card_databases_storage/Individual_cards_dbs/CCS_INDIV.db` | 65,069,056 | 11,923 paper-level compound/sample cards |
| `ThermoML_research_agent/card_databases_storage/Individual_cards_dbs/MTDKS_ID_DK.db` | 6,156,288 | 2,302 measurement cards; 2,776 aliases |
| `ThermoML_research_agent/card_databases_storage/Individual_cards_dbs/MTDKS_INDIV.db` | 19,341,312 | 11,923 paper-level measurement cards |
| `ThermoML_research_agent/card_databases_storage/Individual_cards_dbs/PCS_ID_DK.db` | 577,536 | 110 global property cards |
| `ThermoML_research_agent/card_databases_storage/Individual_cards_dbs/PCS_INDIV.db` | 1,381,466,112 | 11,923 paper-level property/reaction cards |
| `ThermoML_research_agent/card_databases_storage/Individual_cards_dbs/RMS_INDIV.db` | 56,520,704 | 11,923 literature cards |
| `ThermoML_research_agent/card_databases_storage/PureOrMixtureData_registry.db` | 491,024,384 | 122,481 property blocks; 57,741 composition subsystems |
| `ThermoML_research_agent/card_databases_storage/ReactionData_registry.db` | 5,070,848 | 1,246 reaction blocks |
| `ThermoML_research_agent/card_databases_storage/ThermoML_index.db` | 412,033,024 | 123,727 blocks and normalized identity/search tables |

`ThermoML_research_agent/card_databases_storage/PCS_INDIV.db` is a **zero-byte placeholder**. The active property database is the file under `Individual_cards_dbs`; the placeholder has no usable card tables.

Five database files exceed 100 MiB. The publication tracks **all `*.db` files with Git LFS**, as declared in [.gitattributes](../.gitattributes). Install Git LFS before cloning the repository so the checkout can retrieve the SQLite payloads. For an existing checkout, run these commands from its root:

```bash
git lfs install
git lfs pull
git lfs ls-files
```

`git lfs pull` downloads the LFS objects for the checked-out revision and updates the working files. A source-only archive or checkout containing small text LFS pointers is not a runnable data bundle. Compare the restored database sizes with the inventory above; the zero-byte placeholder is the exception already identified. The application itself does not download missing databases. See the [installation guide](INSTALLATION.md) for the repository acquisition steps.

## Raw JSON and compressed JSON/XML

The [raw database directory](../ThermoML_research_agent/ThermoML.v2020-09-30.db) contains both stores; it currently contains **no extracted DOI directories**.

`thermoml_raw.db` contains these five tables:

| Table | Rows | Meaning |
|---|---:|---|
| `papers` | 11,923 | DOI, source-relative file path, full JSON text, citation metadata |
| `compounds` | 61,113 | Compound occurrences within papers |
| `blocks` | 123,727 | 122,481 PureOrMixtureData blocks and 1,246 ReactionData blocks |
| `block_properties` | 130,104 | Property declarations in raw blocks |
| `block_variables` | 168,687 | Variable declarations in raw blocks |

Summing the stored `blocks.n_datapoints` gives **2,690,357** PureOrMixtureData rows and **2,577** ReactionData rows. One row can contain multiple property values; these sums are not a count of unique scalar observations. `papers.json_data` retains the full source representation used by parser and analysis code. The `md5_checksum` field preserves NIST's `THERMOML_MD5_CHECKSUM`, associated with the XML document; it is not a locally computed hash of the JSON string.

`thermoml_raw_corpus.db` uses format `thermoml-zlib-sqlite-v1`. Its `documents` table has `path`, `doi`, `json_zlib`, `xml_zlib`, `json_size`, `xml_size`, `json_crc32`, and `xml_crc32`. Its `metadata` table records 11,923 JSON and 11,923 XML documents, 1,897,543,094 JSON source bytes, 2,188,461,662 XML source bytes, and compression level 6.

The browser reads individual members with [helpers/raw_corpus.py](../ThermoML_database_browser/helpers/raw_corpus.py), without extracting the archive. Agent search/parser paths still require the uncompressed `thermoml_raw.db` and generated databases; the compressed container does not replace them.

For example, run this Python code from the repository root to inspect one stored document:

```python
from ThermoML_database_browser.helpers.raw_corpus import (
    archive_status, read_json, read_bytes,
)

print(archive_status())
paper = read_json("10.1007/s10765-005-5566-6.json")
xml_bytes = read_bytes("10.1007/s10765-005-5566-6.xml")
print(paper["Citation"]["sDOI"], len(xml_bytes))
```

Publication preparation checked the first, middle, and last archive records in path order: decompressed JSON matched the corresponding raw SQLite JSON bytes, and JSON/XML sizes and CRC32 values matched the stored values. This was a three-record consistency check, not a full corpus revalidation or a comparison against a freshly downloaded upstream archive. CRC32 is a corruption check, not an authenticity signature.

## Generated cards and identifiers

The operational flow is:

```text
NIST source JSON in thermoml_raw.db
  -> canonical CSV identities + authored knowledge inputs
  -> per-paper RMS / CCS / MTDKS / PCS cards and global ID/DK cards
  -> property/reaction block registries + ThermoML_index.db
  -> search tools, agents, numerical pipelines, and browser views

Paired source JSON/XML -> thermoml_raw_corpus.db -> browser source views
```

See the [card database architecture](../ThermoML_research_agent/card_databases_storage/ARCHITECTURE.md), [identifier grammar](../ThermoML_research_agent/card_databases_storage/ID_architecture.md), [canonical CSVs](../ThermoML_research_agent/card_databases_storage/Canonicalized_ID_name_lists_csvs), and [parser source](../ThermoML_research_agent/ThermoML_raw_json_to_card_db_parsers). Global IDs such as `GLOBcomp_N` and `GLOBlit_N` are distinct from DOI-local `DOIcomp_N`, block IDs `PROPblock_N`/`RXNblock_N`, and block-local `BLKprop_N`/`BLKvar_N`/`BLKconstr_N`. Keep a local identifier with its paper/block context.

The included PCS metadata declares `prefixed-v2`, **50 stored datapoints per block**, and 123,727 identity-enriched blocks. Card summaries and derived indexes can describe more source rows than the materialized card sample. Use the full raw source for analyses requiring all observations. The runtime also validates the identity-translation CSV/hash recorded by the PCS database; copy related databases and canonical CSVs as a coherent set.

Some build metadata retains the original machine's source path. That string is provenance, not the runtime database location. Active code resolves database paths from its own project location.

## Rebuild capabilities and limits

Using the supplied databases does not require a rebuild. The repository includes individual builders, not a single validated command that regenerates every artifact from an upstream download.

| Stage | Included implementation | Requirements and limitations |
|---|---|---|
| Canonical CSVs | [export_csvs.py](../ThermoML_research_agent/ThermoML_raw_json_to_card_db_parsers/_index_builder/csv_ids_generation_helper/export_csvs.py) | Reads full raw JSON; writes parser ID lists and canonical storage copies. RDKit affects structure enrichment. |
| Per-paper and compound cards | [parser builder directories](../ThermoML_research_agent/ThermoML_raw_json_to_card_db_parsers) | Depend on raw SQLite and matching identity catalogs; outputs can replace existing generated databases. |
| PCS cards/identity translation | [build_pcs_indiv_db.py](../ThermoML_research_agent/ThermoML_raw_json_to_card_db_parsers/property_card_helpers/build_pcs_indiv_db.py) | Stages the database and a content-addressed translation CSV, validates them, then publishes. Default point cap is 50; `None` requests all points through the Python function. |
| Measurement knowledge cards | [build_mtdks_iddk_db_full.py](../ThermoML_research_agent/ThermoML_raw_json_to_card_db_parsers/measurement_card_helpers/build_mtdks_iddk_db_full.py) | Uses measurement IDs/aliases, raw SQLite, and authored cards in `ID_and_DK_cards_raw_json/Meas_ID_and_DK_cards`. |
| Property knowledge cards | [build_pcs_iddk_db.py](../ThermoML_research_agent/ThermoML_raw_json_to_card_db_parsers/property_card_helpers/build_pcs_iddk_db.py) | Uses authored cards under `Property_Card_Schema/PCS_ID_and_DK_cards`; canonical types without an authored card receive a registry stub. |
| Block registries | [registry builders](../ThermoML_research_agent/ThermoML_raw_json_to_card_db_parsers/_index_builder/registry_db_generation_helper) | Project validated PCS cards; preserve typed block and subsystem identities. |
| Cross-card index | [build_index.py](../ThermoML_research_agent/ThermoML_raw_json_to_card_db_parsers/_index_builder/index_db_builder_helper/build_index.py) | Uses generated PCS and canonical CSV inputs; offers `--output` for an alternate index destination. |
| Compressed JSON/XML container | [build_raw_corpus_archive.py](../ThermoML_research_agent/build_raw_corpus_archive.py) | Requires raw SQLite **and extracted original XML files** at paths matching `papers.file_path`; those loose files are not included in the current layout. |

The historical `build_thermoml_sqlite.py` and `raw_loader.py` named in older architecture notes are not present. Rebuilding the raw query database from an upstream download is therefore not a supplied turnkey workflow. Rebuilding the compressed container additionally requires obtaining/extracting the paired XML source or recovering those bytes from an existing container.

The archive builder accepts `--source`, `--raw-db`, `--output`, `--compresslevel`, and `--workers`; its default destination is the active corpus file. It verifies every compressed record before atomic replacement. Database builders also need staging disk space and a coherent generation order; many target the active data paths. Work in a separate copy when deliberately regenerating a dataset, then check schema, counts, identity catalogs, and appropriate parser/search tests before using the result. No full rebuild was performed during documentation preparation.

For a smaller diagnostic, [card_orchestrator.py](../ThermoML_research_agent/ThermoML_raw_json_to_card_db_parsers/card_orchestrator.py) can parse a selected DOI, and [run_all_compactor_tests.py](../ThermoML_research_agent/ThermoML_card_json_to_md_compactors/_entry_by_entry_validator/run_all_compactor_tests.py) exercises current card/registry examples. Their generated reports go under `_output/Query/Diagnostics`; they do not establish full rebuild reproducibility.
