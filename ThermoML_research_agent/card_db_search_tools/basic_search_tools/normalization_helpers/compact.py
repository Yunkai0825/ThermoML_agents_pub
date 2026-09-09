"""
Compact card dispatcher — runs the appropriate compactor on a card dict.

Centralizes compactor imports so each search tool only needs::

    from normalization_helpers.compact import compact_card, compact_block
"""

import os
import sys

# Ensure workspace root is on sys.path for ThermoML_card_json_to_md_compactors imports
_HERE = os.path.dirname(os.path.abspath(__file__))
_WORKSPACE = os.path.normpath(os.path.join(_HERE, os.pardir, os.pardir, os.pardir))
if _WORKSPACE not in sys.path:
    sys.path.insert(0, _WORKSPACE)

from ThermoML_card_json_to_md_compactors._basic_compactors.component_cards_compactor.ccs_compactor import compact_ccs
from ThermoML_card_json_to_md_compactors._basic_compactors.component_cards_compactor.ccs_iddk_compactor import compact_ccs_iddk
from ThermoML_card_json_to_md_compactors._basic_compactors.measurement_cards_compactor.mtdks_compactor import compact_mtdks
from ThermoML_card_json_to_md_compactors._basic_compactors.measurement_cards_compactor.mtdks_iddk_compactor import compact_mtdks_iddk
from ThermoML_card_json_to_md_compactors._basic_compactors.property_cards_compactor.pcs_compactor import compact_pcs
from ThermoML_card_json_to_md_compactors._basic_compactors.property_cards_compactor.pcs_iddk_compactor import compact_pcs_iddk
from ThermoML_card_json_to_md_compactors._basic_compactors.reference_cards_compactor.rms_compactor import compact_rms
from ThermoML_card_json_to_md_compactors._basic_compactors.registry_cards_compactor.registry_block_compactor import (
    compact_pm_registry,
    compact_rxn_registry,
)
from ThermoML_card_json_to_md_compactors._cross_cards_compactors.block_cards_compactor.block_compactor import (
    compact_block as _block_compactor_compact_block,
)
from ThermoML_raw_json_to_card_db_parsers.id_schema import validate_nested_identifiers

# card_type key → compactor function
_COMPACTORS = {
    "CCS_INDIV":     compact_ccs,
    "CCS_ID_DK":     compact_ccs_iddk,
    "MTDKS_INDIV":   compact_mtdks,
    "MTDKS_ID_DK":   compact_mtdks_iddk,
    "PCS_INDIV":     compact_pcs,
    "PCS_ID_DK":     compact_pcs_iddk,
    "RMS_INDIV":     compact_rms,
    "PM_REGISTRY":   compact_pm_registry,
    "RXN_REGISTRY":  compact_rxn_registry,
}

_REQUIRED_CARD_FIELDS = {
    "CCS_INDIV": {"key", "compounds"},
    "CCS_ID_DK": {"comp_num_id", "identity", "names"},
    "MTDKS_INDIV": {"key", "methods", "methods_summary"},
    "MTDKS_ID_DK": {"card_type", "meas_num_id", "meas_ID", "identity", "domain_knowledge"},
    "PCS_INDIV": {"key", "paper", "blocks_summary", "blocks"},
    "PCS_ID_DK": {
        "card_type", "prop_num_id", "prop_ID", "base_prop_ID",
        "component_linked", "identity", "domain_knowledge",
    },
    "RMS_INDIV": {"identity", "bibliographic", "content", "data_inventory"},
}

_REQUIRED_BLOCK_FIELDS = {
    "block_number", "block_type", "blocktype_num_id", "system_type",
    "compounds", "properties", "variables", "constraints", "solvents",
    "reaction", "equation", "data_points", "data_summary", "auxiliary",
    "provenance",
}


def _require_fields(payload: dict, required: set[str], *, context: str) -> None:
    missing = required.difference(payload)
    if missing:
        raise ValueError(f"{context} is missing required fields: {sorted(missing)}")
    unknown = set(payload).difference(required)
    if unknown:
        raise ValueError(f"{context} has unsupported fields: {sorted(unknown)}")


def compact_card(card_type: str, card: dict) -> str:
    """Run the appropriate compactor for *card_type*, return markdown string.

    Parameters
    ----------
    card_type : str
        One of the _COMPACTORS keys (e.g. ``"CCS_ID_DK"``, ``"RMS_INDIV"``).
    card : dict
        The full card dict (or registry row dict for registry types).

    Unknown card types are rejected; an empty compacted payload is never used
    as a substitute for a missing compactor.
    """
    try:
        fn = _COMPACTORS[card_type]
    except KeyError as exc:
        raise ValueError(f"Unknown ThermoML card type: {card_type!r}") from exc
    if not isinstance(card, dict):
        raise TypeError("card must be an object")
    if card_type in _REQUIRED_CARD_FIELDS:
        _require_fields(card, _REQUIRED_CARD_FIELDS[card_type], context=f"{card_type} card")
    validate_nested_identifiers(card, path=f"{card_type} card")
    result = fn(card)
    if not isinstance(result, str) or not result.strip():
        raise ValueError(f"{card_type} compactor returned an empty/non-text result")
    return result


def compact_block(block: dict, key_info: dict, compounds_map: dict = None) -> str:
    """Compact a single PCS_INDIV block with RDP topology compaction.

    Delegates to the cross-cards block_compactor which applies RDP
    data-point simplification and topology annotation.

    Parameters
    ----------
    block : dict
        One element from card["blocks"].
    key_info : dict
        {"doi": ..., "lit_num_id": ..., "lit_id": ..., "title": ...}
        for the header.
    compounds_map : dict, optional
        org_num -> short label for data-table column headers.
    """
    if not isinstance(block, dict):
        raise TypeError("block must be an object")
    _require_fields(block, _REQUIRED_BLOCK_FIELDS, context="PCS block")
    validate_nested_identifiers(block, path="PCS block")
    if not isinstance(key_info, dict):
        raise TypeError("key_info must be an object")
    _require_fields(
        key_info,
        {"doi", "lit_num_id", "lit_id", "title"},
        context="key_info",
    )
    validate_nested_identifiers(key_info, path="key_info")
    result = _block_compactor_compact_block(
        block, key_info=key_info, compounds_map=compounds_map
    )
    if not isinstance(result, str) or not result.strip():
        raise ValueError("block compactor returned an empty/non-text result")
    return result
