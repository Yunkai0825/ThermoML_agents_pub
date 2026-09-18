# Hardcoded Search Helpers

Deterministic (no-LLM) search, validation, and review utilities.
Used both as the fast path for simple queries and as backing
implementations for several of the 16 MCP tools.

## Files

| File | Purpose |
|------|---------|
| `search_parser.py` | Parse free-text queries into `SearchBlock` objects |
| `dispatcher.py` | Route parsed blocks to the correct search strategy |
| `id_workers.py` | Resolve entity names to canonical index IDs |
| `validation_tools.py` | Validate fields & bibliography against the index |
| `review_workers.py` | Score and review top search results |
| `bibliography_scorer.py` | Title / author / DOI matching & scoring |
| `__init__.py` | Package init |

## Key Classes

- **`SearchBlock`** — structured representation of a parsed query
  (compounds, properties, conditions, bibliography)
- **`FieldVerdict`** / **`BibVerdict`** — validation results
- **`ValidationReport`** — aggregate validation across all fields
- **`FieldEdit`** / **`ReviewResult`** — review worker outputs

## Entry Points

```python
from .search_parser import parse_search_input
from .validation_tools import validate_field, validate_bibliography, validate_all_fields
from .review_workers import review_literature
```
