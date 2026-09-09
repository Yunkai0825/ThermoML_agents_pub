# general_ThermoML_db_csv_registry

Agent-agnostic catalog of every SQLite database and CSV canonical-ID file
used by the ThermoML system.

## Three Tiers

| Tier | Directory | Dataclass | Helper |
|------|-----------|-----------|--------|
| Card databases | `card_databases_storage/Individual_cards/` | `CardDatabaseEntry` | `card_db_path(key)` |
| Registry databases | `card_databases_storage/` | `RegistryDatabaseEntry` | `registry_db_path(key)` |
| CSV ID registries | `card_databases_storage/ID_name_lists_csv/` | `CsvRegistryEntry` | `csv_path(key)` |

## Public API

```python
from general_ThermoML_db_csv_registry import (
    card_databases_storage,       # dict[str, CardDatabaseEntry]
    REGISTRY_DATABASES,   # dict[str, RegistryDatabaseEntry]
    CSV_REGISTRIES,       # dict[str, CsvRegistryEntry]
    ALL_DATABASES,        # merged dict of all entries
    card_db_path,         # key → absolute Path
    registry_db_path,
    csv_path,
)
```

## Files

| File | Purpose |
|------|---------|
| `ThermoML_db_csv_registry.py` | Dataclass definitions + frozen catalog dicts |
| `__init__.py` | Re-exports the full public API |
