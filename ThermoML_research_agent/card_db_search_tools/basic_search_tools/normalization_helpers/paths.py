"""Centralized path resolution for all card databases, registry DBs, and CSV files."""

import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_WORKSPACE = os.path.normpath(os.path.join(_HERE, os.pardir, os.pardir, os.pardir))
_CARD_DIR = os.path.join(_WORKSPACE, "card_databases_storage", "Individual_cards_dbs")
_REGISTRY_DIR = os.path.join(_WORKSPACE, "card_databases_storage")
_CSV_DIR = os.path.join(_WORKSPACE, "card_databases_storage", "Canonicalized_ID_name_lists_csvs")

# ── Canonical names ──────────────────────────────────────────────────────────

CARD_DBS = {
    "CCS_ID_DK":   "CCS_ID_DK.db",
    "CCS_INDIV":   "CCS_INDIV.db",
    "MTDKS_ID_DK": "MTDKS_ID_DK.db",
    "MTDKS_INDIV": "MTDKS_INDIV.db",
    "PCS_ID_DK":   "PCS_ID_DK.db",
    "PCS_INDIV":   "PCS_INDIV.db",
    "RMS_INDIV":   "RMS_INDIV.db",
}

REGISTRY_DBS = {
    "PM_REGISTRY":  "PureOrMixtureData_registry.db",
    "RXN_REGISTRY": "ReactionData_registry.db",
}

CSV_FILES = {
    "compound_ids":      "compound_ids.csv",
    "property_ids":      "property_ids.csv",
    "measurement_ids":   "measurement_ids.csv",
    "measurement_aliases": "measurement_aliases.csv",
    "variable_ids":      "variable_ids.csv",
    "constraint_ids":    "constraint_ids.csv",
    "phase_ids":         "phase_ids.csv",
    "reference_ids":     "reference_ids.csv",
    "solvent_components": "solvent_components.csv",
    "block_types":       "block_types.csv",
    "reaction_type_ids": "reaction_type_ids.csv",
}


def card_db_path(name: str) -> str:
    """Return the path for one declared card-database key."""
    try:
        fn = CARD_DBS[name]
    except KeyError as exc:
        raise ValueError(f"Unknown card database key: {name!r}") from exc
    return os.path.join(_CARD_DIR, fn)


def registry_db_path(name: str) -> str:
    """Return the path for one declared registry-database key."""
    try:
        fn = REGISTRY_DBS[name]
    except KeyError as exc:
        raise ValueError(f"Unknown registry database key: {name!r}") from exc
    return os.path.join(_REGISTRY_DIR, fn)


def csv_path(name: str) -> str:
    """Return the path for one declared canonical-registry CSV key."""
    try:
        fn = CSV_FILES[name]
    except KeyError as exc:
        raise ValueError(f"Unknown canonical CSV key: {name!r}") from exc
    return os.path.join(_CSV_DIR, fn)
