"""Strict entry-by-entry parser facade used by compactor diagnostics.

Card generation belongs to ``ThermoML_raw_json_to_card_db_parsers``.  This
module deliberately contains no second parser and no legacy ID translation;
it delegates every request to the canonical prefixed-v2 orchestrator.
"""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from ThermoML_raw_json_to_card_db_parsers.card_orchestrator import (
    EDGE_CASE_DOIS,
    parse_doi,
    print_card_summary,
    run_edge_cases,
    save_cards,
    validate_pcs_card,
)
from ThermoML_raw_json_to_card_db_parsers.index_lookup import ThermoMLIndex


def parse_one(doi: str, *, max_datapoints: int = 50) -> dict:
    """Build all strict card families for one canonical source DOI."""
    return parse_doi(doi, ThermoMLIndex(), max_datapoints=max_datapoints)


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if "--edge-cases" in args or "--check" in args:
        results = run_edge_cases()
        return 0 if all(item["status"] == "ok" for item in results.values()) else 1

    if "--doi" in args:
        pos = args.index("--doi")
        if pos + 1 >= len(args):
            raise SystemExit("--doi requires a DOI value")
        doi = args[pos + 1]
    else:
        doi = EDGE_CASE_DOIS["simple_unary"]

    cards = parse_one(doi)
    save_dir = save_cards(doi, cards)
    print_card_summary(doi, cards)
    errors = validate_pcs_card(cards["pcs"])
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Saved to: {save_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
