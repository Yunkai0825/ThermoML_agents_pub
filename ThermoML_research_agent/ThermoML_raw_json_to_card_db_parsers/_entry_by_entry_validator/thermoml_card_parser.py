"""Strict entry-by-entry validator for the current prefixed-v2 card parser.

This module deliberately delegates parsing to :mod:`card_orchestrator` so the
validator and production database builders cannot drift into separate schemas.
It never repairs, renames, or backfills identifiers in parser output.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from ThermoML_raw_json_to_card_db_parsers.card_orchestrator import (
    DB_PATH,
    EDGE_CASE_DOIS,
    OUTPUT_DIR,
    load_paper,
    parse_doi,
    print_card_summary,
    save_cards,
    validate_pcs_card,
)
from ThermoML_raw_json_to_card_db_parsers.id_schema import validate_nested_identifiers
from ThermoML_raw_json_to_card_db_parsers.index_lookup import ThermoMLIndex


def parse_paper(
    doi: str,
    index: ThermoMLIndex,
    db_path: str = DB_PATH,
    max_datapoints: int = 50,
) -> dict:
    """Parse one DOI with the production parser and strict current index."""
    cards = parse_doi(
        doi,
        index,
        db_path=db_path,
        max_datapoints=max_datapoints,
    )
    validate_nested_identifiers(cards, path=f"parsed[{doi}]")
    errors = validate_pcs_card(cards["pcs"])
    if errors:
        raise ValueError(f"PCS structural validation failed for {doi}: {errors}")
    return cards


def run_edge_cases(output_dir: str = OUTPUT_DIR, max_datapoints: int = 50) -> dict:
    """Parse and validate every declared edge case; failures are not downgraded."""
    index = ThermoMLIndex()
    os.makedirs(output_dir, exist_ok=True)
    results = {}
    for case_name, doi in sorted(EDGE_CASE_DOIS.items()):
        cards = parse_paper(doi, index, max_datapoints=max_datapoints)
        save_cards(doi, cards, output_dir)
        print_card_summary(doi, cards)
        results[case_name] = {"doi": doi, "status": "ok"}
    return results


def validate_saved_outputs(output_dir: str = OUTPUT_DIR) -> int:
    """Validate every saved card tree and return the number of DOI directories."""
    root = Path(output_dir)
    if not root.is_dir():
        raise FileNotFoundError(f"Output directory does not exist: {root}")
    total = 0
    for doi_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        card_files = sorted(doi_dir.glob("*_card.json"))
        if not card_files:
            raise ValueError(f"No card JSON files in {doi_dir}")
        for card_path in card_files:
            with card_path.open(encoding="utf-8") as handle:
                card = json.load(handle)
            validate_nested_identifiers(card, path=str(card_path))
            if card_path.name == "pcs_card.json":
                errors = validate_pcs_card(card)
                if errors:
                    raise ValueError(f"{card_path}: {errors}")
        total += 1
    return total


def main(argv: list[str] | None = None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    if args == ["--edge-cases"]:
        results = run_edge_cases()
        print(f"Validated {len(results)} current-schema edge cases")
        return
    if args == ["--check"]:
        print(f"Validated {validate_saved_outputs()} saved DOI directories")
        return
    if len(args) == 2 and args[0] == "--doi":
        doi = args[1]
    elif not args:
        doi = EDGE_CASE_DOIS["simple_unary"]
    else:
        raise ValueError("Usage: thermoml_card_parser.py [--edge-cases | --check | --doi DOI]")

    index = ThermoMLIndex()
    cards = parse_paper(doi, index)
    save_dir = save_cards(doi, cards)
    print_card_summary(doi, cards)
    print(f"Saved to: {save_dir}")


if __name__ == "__main__":
    main()
