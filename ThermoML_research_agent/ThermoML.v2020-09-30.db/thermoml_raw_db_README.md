# Raw ThermoML stores in this workspace

The current data inventory, upstream provenance, format details, and rebuild limitations are documented in [docs/DATA.md](../../docs/DATA.md).

This directory contains two complementary SQLite stores:

| File | Bytes | Role |
|---|---:|---|
| `thermoml_raw.db` | 2,014,683,136 | Full JSON for 11,923 papers plus raw query indexes; required by agent/parser/search paths |
| `thermoml_raw_corpus.db` | 388,104,192 | 11,923 paired compressed JSON/XML documents; used for browser source views |

These values were inspected read-only on 2026-09-09. The snapshot is NIST ThermoML v2020-09-30, and the stored paper publication years span 2003–2019. NIST's release consists of paired JSON/XML files; XML is generated from JSON, which can preserve additional fields. See the [upstream data record](https://data.nist.gov/pdr/lps/ark%3A/88434/mds2-2422).

The stored documents are NIST/TRC ThermoML Archive content and are not covered by the repository's MIT license; see the third-party data notice in [NOTICE](../../NOTICE). NIST asks that published research using ThermoML data cite [doi:10.1002/jcc.26842](https://doi.org/10.1002/jcc.26842) and [doi:10.18434/mds2-2422](https://doi.org/10.18434/mds2-2422); the full references are in the [workspace README](../../README.md#license-data-source-and-citation).

## Raw query database

`thermoml_raw.db` contains `papers` (11,923 rows), `compounds` (61,113), `blocks` (123,727), `block_properties` (130,104), and `block_variables` (168,687). `papers.json_data` is the full stored JSON text; the other tables provide extracted fields for queries. `papers.file_path` preserves the source-relative DOI path. `papers.md5_checksum` preserves the source `THERMOML_MD5_CHECKSUM`, which refers to the associated XML document rather than a newly computed JSON checksum.

The [database architecture notes](DATABASE_ARCHITECTURE.md) retain detailed schema descriptions. Their older reconstruction examples reference an absent `build_thermoml_sqlite.py`; they are not a supplied raw-database rebuild workflow.

## Compressed document container

`thermoml_raw_corpus.db` has a `documents` table keyed by source-relative JSON path and unique DOI. JSON and XML are independently zlib-compressed. Stored uncompressed sizes and CRC32 values support consistency checks; `metadata` records format `thermoml-zlib-sqlite-v1` and counts.

The [browser reader](../../ThermoML_database_browser/helpers/raw_corpus.py) retrieves one document at a time. It does not need loose DOI directories. The [archive builder](../build_raw_corpus_archive.py) requires the raw query database and extracted original XML files to produce a new container. No loose source DOI directories are present in this workspace. Obtain/extract the matching upstream source, or recover XML bytes from an existing container, before deliberately rebuilding it.

The two stores are not interchangeable: retaining only the compressed container does not satisfy the raw SQLite queries used by the agents. No full corpus rebuild or fresh upstream archive verification was performed during documentation preparation.
