"""
ThermoML DB & CSV Registry — dataclass-based catalog of all databases.
======================================================================
Central, agent-agnostic registry of every SQLite database and CSV
canonical-ID file in the ThermoML card_databases_storage/ directory.

Three tiers
-----------
1. **Card databases** (Individual_cards_dbs/) — per-DOI or per-entity
   SQLite DBs holding markdown cards.
2. **Registry databases** (card_databases_storage/) — system-level block
   registries (PureOrMixture, Reaction) + the ThermoML index.
3. **CSV ID registries** (Canonicalized_ID_name_lists_csvs/) — canonical ID→name
   lookups for compounds, properties, measurements, etc.

Usage::

    from general_ThermoML_db_csv_registry import (
        card_databases_storage,      # dict[str, CardDatabaseEntry]
        REGISTRY_DATABASES,  # dict[str, RegistryDatabaseEntry]
        CSV_REGISTRIES,      # dict[str, CsvRegistryEntry]
        card_db_path,        # name → absolute path
    )
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Dict, List, Optional


# ═══════════════════════════════════════════════════════════════
#  Path roots (resolved once at import time)
# ═══════════════════════════════════════════════════════════════

_HERE = os.path.dirname(os.path.abspath(__file__))
# general_ThermoML_db_csv_registry/ → general_db_query_engine/
# → NIST_ThermoML_agents/ → ThermoML_research_agent/
_WORKSPACE = os.path.normpath(
    os.path.join(_HERE, os.pardir, os.pardir, os.pardir)
)
_CARD_DIR = os.path.join(_WORKSPACE, "card_databases_storage", "Individual_cards_dbs")
_REGISTRY_DIR = os.path.join(_WORKSPACE, "card_databases_storage")
_CSV_DIR = os.path.join(_WORKSPACE, "card_databases_storage", "Canonicalized_ID_name_lists_csvs")
_JSON_DIR = os.path.join(_WORKSPACE, "card_databases_storage", "ID_and_DK_cards_raw_json")


# ═══════════════════════════════════════════════════════════════
#  Dataclasses
# ═══════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class CardDatabaseEntry:
    """One SQLite card database in Individual_cards_dbs/."""

    key: str
    """Short identifier: CCS_ID_DK, CCS_INDIV, MTDKS_ID_DK, etc."""

    filename: str
    """Filename within Individual_cards_dbs/."""

    tier: str
    """'id_dk' (per-entity domain-knowledge) or 'indiv' (per-DOI individual cards)."""

    card_schema: str
    """Card schema family: CCS (Component), MTDKS (MeasTech), PCS (Property), RMS (Reference)."""

    description: str
    """One-line purpose."""


@dataclass(frozen=True)
class RegistryDatabaseEntry:
    """One SQLite registry/index database in card_databases_storage/."""

    key: str
    filename: str
    description: str


@dataclass(frozen=True)
class CsvRegistryEntry:
    """One canonical-ID CSV in Canonicalized_ID_name_lists_csvs/."""

    key: str
    """Lookup key: compound_ids, property_ids, etc."""

    filename: str
    """File within Canonicalized_ID_name_lists_csvs/."""

    entity_type: str
    """Entity class: compound, property, measurement, variable, constraint, phase, reference, solvent, block_type, reaction_type."""

    id_column: str
    """Primary global-ID column name in the CSV."""

    name_column: str
    """Human-readable name column."""

    description: str


# ═══════════════════════════════════════════════════════════════
#  Card databases (7 SQLite, Individual_cards_dbs/)
# ═══════════════════════════════════════════════════════════════

_CARD_DB_ENTRIES: List[CardDatabaseEntry] = [
    # Component cards
    CardDatabaseEntry(
        key="CCS_ID_DK", filename="CCS_ID_DK.db",
        tier="id_dk", card_schema="CCS",
        description="Component identity + domain-knowledge cards (per compound).",
    ),
    CardDatabaseEntry(
        key="CCS_INDIV", filename="CCS_INDIV.db",
        tier="indiv", card_schema="CCS",
        description="Per-DOI individual component characterization cards.",
    ),
    # Measurement technique cards
    CardDatabaseEntry(
        key="MTDKS_ID_DK", filename="MTDKS_ID_DK.db",
        tier="id_dk", card_schema="MTDKS",
        description="Measurement technique identity + domain-knowledge cards.",
    ),
    CardDatabaseEntry(
        key="MTDKS_INDIV", filename="MTDKS_INDIV.db",
        tier="indiv", card_schema="MTDKS",
        description="Per-DOI individual measurement technique usage cards.",
    ),
    # Property cards
    CardDatabaseEntry(
        key="PCS_ID_DK", filename="PCS_ID_DK.db",
        tier="id_dk", card_schema="PCS",
        description="Property identity + domain-knowledge cards.",
    ),
    CardDatabaseEntry(
        key="PCS_INDIV", filename="PCS_INDIV.db",
        tier="indiv", card_schema="PCS",
        description="Per-DOI individual property data blocks (the main data store).",
    ),
    # Reference metadata cards
    CardDatabaseEntry(
        key="RMS_INDIV", filename="RMS_INDIV.db",
        tier="indiv", card_schema="RMS",
        description="Per-DOI reference metadata cards (authors, journal, compounds).",
    ),
]

card_databases_storage: Dict[str, CardDatabaseEntry] = {e.key: e for e in _CARD_DB_ENTRIES}


# ═══════════════════════════════════════════════════════════════
#  Registry databases (3 SQLite, card_databases_storage/)
# ═══════════════════════════════════════════════════════════════

_REGISTRY_DB_ENTRIES: List[RegistryDatabaseEntry] = [
    RegistryDatabaseEntry(
        key="PM_REGISTRY",
        filename="PureOrMixtureData_registry.db",
        description="Block-level registry for PureOrMixtureData (compounds, properties, system type per block).",
    ),
    RegistryDatabaseEntry(
        key="RXN_REGISTRY",
        filename="ReactionData_registry.db",
        description="Block-level registry for ReactionData (reaction types, compounds, properties per block).",
    ),
    RegistryDatabaseEntry(
        key="THERMOML_INDEX",
        filename="ThermoML_index.db",
        description="Master index mapping DOIs to blocks, compounds, properties, and measurements across all papers.",
    ),
]

REGISTRY_DATABASES: Dict[str, RegistryDatabaseEntry] = {e.key: e for e in _REGISTRY_DB_ENTRIES}


# ═══════════════════════════════════════════════════════════════
#  CSV canonical-ID registries (10 CSVs)
# ═══════════════════════════════════════════════════════════════

_CSV_ENTRIES: List[CsvRegistryEntry] = [
    CsvRegistryEntry(
        key="compound_ids", filename="compound_ids.csv",
        entity_type="compound", id_column="comp_num_id", name_column="common_name",
        description="8,500+ compounds: comp_num_id, comp_id, InChI-key, name, formula, SMILES, n_papers.",
    ),
    CsvRegistryEntry(
        key="property_ids", filename="property_ids.csv",
        entity_type="property", id_column="prop_num_id", name_column="prop_name",
        description="105 properties: prop_num_id, prop_id, name, group, linked DOIcomp_id template, n_blocks.",
    ),
    CsvRegistryEntry(
        key="measurement_ids", filename="measurement_ids.csv",
        entity_type="measurement", id_column="meas_num_id", name_column="method_name",
        description="129 measurement techniques: meas_num_id, meas_id, method_name, method_type, n_blocks.",
    ),
    CsvRegistryEntry(
        key="variable_ids", filename="variable_ids.csv",
        entity_type="variable", id_column="var_num_id", name_column="var_name",
        description="Variables (Temperature, Mole fraction, etc.): var_num_id, var_id, name, type_key, n_blocks.",
    ),
    CsvRegistryEntry(
        key="constraint_ids", filename="constraint_ids.csv",
        entity_type="constraint", id_column="constr_num_id", name_column="constr_name",
        description="Constraints (Pressure, Temperature, etc.): constr_num_id, constr_id, name, type_key, n_blocks.",
    ),
    CsvRegistryEntry(
        key="phase_ids", filename="phase_ids.csv",
        entity_type="phase", id_column="phase_num_id", name_column="phase_name",
        description="Phases (Liquid, Crystal, Gas, etc.): phase_num_id, phase_id, name, n_occurrences.",
    ),
    CsvRegistryEntry(
        key="reference_ids", filename="reference_ids.csv",
        entity_type="reference", id_column="lit_num_id", name_column="doi",
        description="11,900+ publications: lit_num_id, DOI, lit_id, author, year, journal, n_compounds, n_blocks.",
    ),
    CsvRegistryEntry(
        key="solvent_components", filename="solvent_components.csv",
        entity_type="solvent", id_column="solvent_num_id", name_column="common_name",
        description="Solvent components: solvent_num_id, comp_num_id, InChI-key, name, formula, n_blocks_as_solvent.",
    ),
    CsvRegistryEntry(
        key="block_types", filename="block_types.csv",
        entity_type="block_type", id_column="blocktype_num_id", name_column="block_type",
        description="Block type × system type combinations: blocktype_num_id, block_type, system_type, n_blocks.",
    ),
    CsvRegistryEntry(
        key="reaction_type_ids", filename="reaction_type_ids.csv",
        entity_type="reaction_type", id_column="rxn_type_num_id", name_column="rxn_type_name",
        description="Reaction types: rxn_type_num_id, rxn_type_id, name, n_blocks.",
    ),
]

CSV_REGISTRIES: Dict[str, CsvRegistryEntry] = {e.key: e for e in _CSV_ENTRIES}


# ═══════════════════════════════════════════════════════════════
#  Unified view
# ═══════════════════════════════════════════════════════════════

ALL_DATABASES: Dict[str, CardDatabaseEntry | RegistryDatabaseEntry] = {
    **card_databases_storage, **REGISTRY_DATABASES,
}
"""All 10 SQLite databases (7 card + 3 registry) keyed by short name."""


# ═══════════════════════════════════════════════════════════════
#  Path helpers
# ═══════════════════════════════════════════════════════════════

def card_db_path(key: str) -> str:
    """Absolute path to a card database. *key* is a card_databases_storage key or filename."""
    entry = card_databases_storage.get(key)
    fn = entry.filename if entry else key
    return os.path.join(_CARD_DIR, fn)


def registry_db_path(key: str) -> str:
    """Absolute path to a registry database. *key* is a REGISTRY_DATABASES key or filename."""
    entry = REGISTRY_DATABASES.get(key)
    fn = entry.filename if entry else key
    return os.path.join(_REGISTRY_DIR, fn)


def csv_path(key: str) -> str:
    """Absolute path to a CSV registry. *key* is a CSV_REGISTRIES key or filename."""
    entry = CSV_REGISTRIES.get(key)
    fn = entry.filename if entry else key
    return os.path.join(_CSV_DIR, fn)


def json_cards_dir(family: str) -> str:
    """Absolute path to a JSON domain-knowledge card directory.

    *family* is one of: Comp, Constr, Meas, Solvt, VarProp.
    """
    return os.path.join(_JSON_DIR, f"{family}_ID_and_DK_cards")
