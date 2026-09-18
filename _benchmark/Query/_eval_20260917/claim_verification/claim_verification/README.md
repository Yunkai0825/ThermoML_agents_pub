# ThermoML Q1 claim verification

This is the sole active representation of the Q1 scientific claim review.
Each reviewed answer has one JSON file under `answers/<group>/`.

| Group | Answers | Resolved claims | Unresolved |
|---|---:|---:|---:|
| Bare model | 6 | 93 | 4 |
| Flat all tools | 6 | 137 | 1 |
| SQL tool prefixed ID | 6 | 119 | 0 |
| SQL tool flat num ID | 6 | 109 | 0 |
| SQL tool one raw DB | 6 | 119 | 0 |
| Hierarchical agents | 6 | 116 | 0 |
| No ledger | 6 | 103 | 0 |

Totals: **42 answers**, **796 resolved claims**, and **5 explicitly unresolved
empirical assertions**.

Start with [manifest.json](manifest.json), which lists every answer file,
content hash, claim count, category count, source hash, and source-path status.
Category and evidence rules are in [METHODS.md](METHODS.md).

The active package contains no aggregate CSV, rendered claim duplicate,
whole-answer score, benchmark plot, timing, token, or cost output. Those former
comparison materials are archived outside this directory.
