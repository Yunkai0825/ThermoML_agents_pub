"""Shared read-only SQLite access for compactor main APIs.

Provides a single helper to fetch a card's json_data from any card database
given a card type key and a lookup value.
"""

import json
import os
import sqlite3

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_global_id,
    validate_nested_identifiers,
)

_HERE = os.path.dirname(os.path.abspath(__file__))
_CARD_DIR = os.path.normpath(
    os.path.join(_HERE, os.pardir, "card_databases_storage", "Individual_cards_dbs")
)

_DB_FILES = {
    "CCS_INDIV":   "CCS_INDIV.db",
    "CCS_ID_DK":   "CCS_ID_DK.db",
    "MTDKS_INDIV": "MTDKS_INDIV.db",
    "MTDKS_ID_DK": "MTDKS_ID_DK.db",
    "PCS_INDIV":   "PCS_INDIV.db",
    "PCS_ID_DK":   "PCS_ID_DK.db",
    "RMS_INDIV":   "RMS_INDIV.db",
}

_GLOBAL_FIELD_BY_COLUMN = {
    "lit_num_id": "lit_num_id",
    "comp_num_id": "comp_num_id",
    "prop_num_id": "prop_num_id",
    "meas_num_id": "meas_num_id",
}
_ALLOWED_COLUMNS = frozenset({"doi", "meas_id", "prop_id", *_GLOBAL_FIELD_BY_COLUMN})


def _db_path(card_type: str) -> str:
    try:
        fn = _DB_FILES[card_type]
    except KeyError as exc:
        raise ValueError(f"Unknown card type: {card_type}") from exc
    return os.path.join(_CARD_DIR, fn)


def fetch_card(card_type: str, column: str, value) -> dict:
    """Fetch a single card from a card database.

    Parameters
    ----------
    card_type : str
        One of the _DB_FILES keys (e.g. ``"CCS_INDIV"``).
    column : str
        Column name to match (e.g. ``"doi"``, ``"comp_num_id"``).
    value
        The value to look up.

    Returns
    -------
    dict — the parsed canonical ``json_data`` object exactly as stored.

    Raises
    ------
    LookupError
        If no matching row is found.
    """
    if column not in _ALLOWED_COLUMNS:
        raise ValueError(f"Unsupported card lookup column: {column!r}")
    if column in _GLOBAL_FIELD_BY_COLUMN:
        value = require_global_id(_GLOBAL_FIELD_BY_COLUMN[column], value)
    elif not isinstance(value, str) or not value.strip():
        raise ValueError(f"{column} must be a non-empty string, got {value!r}")

    db = _db_path(card_type)
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute(
            f"SELECT * FROM cards WHERE {column} = ?", (value,)
        ).fetchone()
    finally:
        conn.close()
    if row is None:
        raise LookupError(
            f"No {card_type} card found for {column}={value!r}"
        )
    card = json.loads(row["json_data"])
    if not isinstance(card, dict):
        raise TypeError(f"{card_type}.json_data must decode to an object")
    validate_nested_identifiers(card, path=f"{card_type}[{column}={value!r}]")
    return card
