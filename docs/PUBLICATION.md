# Publication and data distribution

The repository is [ThermoML_agents_pub](https://github.com/Yunkai0825/ThermoML_agents_pub).
This page describes the publication layout and validation workflow. See the
[installation guide](INSTALLATION.md) for the commands to obtain a usable checkout.

## Repository contents

The snapshot includes all nonignored workspace files: the root browser launcher,
`ThermoML_database_browser/`, `ThermoML_research_agent/`, documentation, database
artifacts, and retained `_benchmark/` and `_output/` records. The
[ignore rules](../.gitignore) determine exclusions, including caches, credentials,
scratch archives, and directories named `test` or `tests` at any depth.
Those local test directories are not part of the published snapshot; included
validation scripts are documented in [DEVELOPMENT.md](DEVELOPMENT.md).

Keep the sibling code folders and their data paths intact. The raw query store
and generated cards support the agents; the compressed JSON/XML container supports
browser source views. The empty `card_databases_storage/PCS_INDIV.db` placeholder
is not a substitute for `Individual_cards_dbs/PCS_INDIV.db`.

## SQLite files use Git LFS

[.gitattributes](../.gitattributes) assigns every `*.db` file to Git Large File
Storage (Git LFS). Source files stay in ordinary Git; database contents are stored
as LFS objects referenced by the commit. The 12 nonempty SQLite databases total
**4,875,669,504 bytes (about 4.875 GB)**, before source files, saved outputs, the local
LFS cache, and space for new runs. Exact paths and sizes are listed in
[DATA.md](DATA.md).

Five database files exceed GitHub's 100 MiB ordinary-Git file limit. The selected
LFS rule covers all databases consistently, including smaller files. See
[GitHub's large-file documentation](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Install Git LFS, then use `git lfs install` and `git lfs pull` as shown in
[INSTALLATION.md](INSTALLATION.md). A checkout containing only small LFS pointer
files cannot serve SQLite queries. Keep `.gitattributes` with the repository so
future database changes continue through LFS. A complete publication requires
both the Git commit and its referenced LFS objects to reach the remote.

The NIST upstream archive is not the project's generated card/index bundle, and
the original raw SQLite build script is absent. The prepared databases delivered
through LFS provide the supported starting point; the rebuild boundaries remain
documented in [DATA.md](DATA.md).

## License, citation, and recorded runs

Include [LICENSE](../LICENSE), [NOTICE](../NOTICE), and [CITATION.cff](../CITATION.cff)
with the source. The MIT software license covers the project's code and
documentation; the NOTICE file is a third-party data notice stating that content
originating from the NIST/TRC ThermoML Archive is NIST public data outside the MIT
grant, together with NIST's citation request and liability statement. Keep that
notice with any redistribution of the databases. Provenance details are in
[DATA.md](DATA.md). The citation file lists the manuscript authors, carries the
manuscript as `preferred-citation`, and lists the two NIST works under
`references`; update its `version` and `date-released` for each release, and add
the journal reference and DOI when available.

The [_benchmark](../_benchmark) tree contains migrated sessions and batch traces;
[_output](../_output) contains shared freeform records and diagnostics. Retained
outputs are historical evidence, not results of a new evaluation. Record the
code/data snapshot, selected prompt IDs, and provider configuration when reporting
a cohort. The current Main launcher lists 17 IDs but only **16 match** the prompt
file: `3.4` is absent, while existing `4.4` is not selected.
[BENCHMARKS.md](BENCHMARKS.md) explains resume behavior, partial traces, and why an
operational `OK` status is not a chemistry accuracy score.

## Validate a publication

Validate a fresh clone after pulling its LFS objects. Follow the installation and
included offline checks, start the browser, open a source JSON/XML document, and
confirm the required databases resolve locally. Check documentation links and
confirm new freeform outputs go under `_output` and benchmark plans point under
`_benchmark`. Record the commit and the commands and results actually obtained.

Live API evaluations require configured provider access. Import checks and
migrated output files do not establish fresh model performance.
