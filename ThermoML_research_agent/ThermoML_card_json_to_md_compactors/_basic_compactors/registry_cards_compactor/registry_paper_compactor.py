"""Paper-level views composed from strict block-registry rows."""

from ThermoML_card_json_to_md_compactors._basic_compactors.registry_cards_compactor.registry_block_compactor import (
    compact_pm_registry,
    compact_rxn_registry,
)
from ThermoML_raw_json_to_card_db_parsers.id_schema import require_block_id


def _sort_rows(rows):
    def key(row):
        value = require_block_id(row["block_number"])
        return int(value.rsplit("_", 1)[1])
    return sorted(rows, key=key)


def _compact(rows, label, renderer):
    if not rows:
        return ""
    doi = rows[0]["doi"]
    if any(row["doi"] != doi for row in rows):
        raise ValueError("Paper registry compaction received multiple DOI values")
    parts = [f"# {label} | {doi} | {len(rows)} blocks", ""]
    parts.extend(renderer(row).rstrip() for row in _sort_rows(rows))
    return "\n\n".join(parts) + "\n"


def compact_pm_paper(rows: list[dict]) -> str:
    return _compact(rows, "REG-PM-PAPER", compact_pm_registry)


def compact_rxn_paper(rows: list[dict]) -> str:
    return _compact(rows, "REG-RXN-PAPER", compact_rxn_registry)
