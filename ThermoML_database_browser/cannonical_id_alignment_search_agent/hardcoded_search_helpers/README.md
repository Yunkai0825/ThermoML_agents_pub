# Deterministic search helpers

These modules parse search text and use local ThermoML databases to resolve,
validate, and review fields. They also implement several tools used by the Argo
alignment workflow.

| Module | Main objects / functions |
|---|---|
| [search_parser.py](search_parser.py) | `SearchBlock`, `parse_search_input()` |
| [dispatcher.py](dispatcher.py) | `ResolvedQuery`, `dispatch_search()`, `dispatch_search_validated()`, `build_index_sql()` |
| [id_workers.py](id_workers.py) | `ResolvedID` and typed entity resolvers |
| [validation_tools.py](validation_tools.py) | `FieldVerdict`, `BibVerdict`, `ValidationReport`, field/bibliography validation |
| [review_workers.py](review_workers.py) | `FieldEdit`, `ReviewResult`, review workers and edit application |
| [bibliography_scorer.py](bibliography_scorer.py) | `TitleHit`, local title scoring |

From the repository root, a parser-only example is:

```python
from ThermoML_database_browser.cannonical_id_alignment_search_agent.hardcoded_search_helpers.search_parser import parse_search_input

blocks = parse_search_input("ethanol + viscosity ; water + density")
print(len(blocks))
```

`dispatch_search(raw_text)` adds local ID resolution. The validated dispatcher
can also validate fields and run deterministic review workers. Its
`enable_query_agent` option defaults to `False`; explicitly enabling it permits
an escalation to the live Query agent, so that mode is not model-free.

See [the alignment API](../README.md) for the browser-facing result format.
