import os
import sqlite3

from NIST_ThermoML_agents.general_db_query_engine.general_ThermoML_db_csv_registry.ThermoML_db_csv_registry import (
    ALL_DATABASES,
    card_db_path,
    registry_db_path,
)


def test_all_database_import_paths_resolve_to_readable_sqlite_files():
    assert len(ALL_DATABASES) == 10

    for key, entry in ALL_DATABASES.items():
        path = (
            card_db_path(key)
            if hasattr(entry, "tier")
            else registry_db_path(key)
        )
        assert os.path.isfile(path), (key, path)
        connection = sqlite3.connect(
            f"file:{path}?mode=ro&immutable=1",
            uri=True,
        )
        try:
            table_count = connection.execute(
                "SELECT COUNT(*) FROM sqlite_master WHERE type = 'table'"
            ).fetchone()[0]
            assert table_count > 0, (key, path)
        finally:
            connection.close()
