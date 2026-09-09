import sys
from pathlib import Path


_PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
_DIAGNOSTICS = _PROJECT_ROOT.parent / "_output" / "Query" / "Diagnostics"
"""
Per-DOI card orchestrator for ThermoML parsed data.

Central module for building all card types for a given DOI:
  - RMS  (Reference Metadata Schema)
  - CCS  (Component Card Schema — sample/purity INDIV)
  - MTDKS (MeasTech DK Schema — method usage INDIV)
  - PCS  (Property Card Schema — measurement data INDIV)
  - CCS Identity (Tier 1 compound identity cards)

Usage:
    python -m ThermoML_raw_json_to_card_db_parsers.card_orchestrator                       # simple unary
    python -m ThermoML_raw_json_to_card_db_parsers.card_orchestrator --doi "10.1016/..."   # specific DOI
    python -m ThermoML_raw_json_to_card_db_parsers.card_orchestrator --edge-cases          # all edge cases
"""

import sqlite3
import json
import os
import sys
import tempfile

from ThermoML_raw_json_to_card_db_parsers.index_lookup import ThermoMLIndex
from ThermoML_raw_json_to_card_db_parsers.reference_card_helpers.rms_builder import build_rms_card
from ThermoML_raw_json_to_card_db_parsers.component_card_helpers.ccs_builder import build_ccs_card
from ThermoML_raw_json_to_card_db_parsers.measurement_card_helpers.mtdks_builder import build_mtdks_card
from ThermoML_raw_json_to_card_db_parsers.property_card_helpers.pcs_builder import build_pcs_card
from ThermoML_raw_json_to_card_db_parsers.property_card_helpers.pcs_identity_enrichment import (
    validate_card_identity_indexes,
)
from ThermoML_raw_json_to_card_db_parsers._ID_and_DK_card_helper.ccs_identity_builder import build_ccs_identity_cards_for_doi
from ThermoML_raw_json_to_card_db_parsers.id_schema import validate_nested_identifiers

_ROOT = os.path.join(os.path.dirname(__file__), "..")
DB_PATH = os.path.join(_ROOT, "ThermoML.v2020-09-30.db", "thermoml_raw.db")
OUTPUT_DIR = os.fspath(_DIAGNOSTICS / 'card_orchestrator')

EDGE_CASE_DOIS = {
    "simple_unary":        "10.1007/s10765-005-5568-4",
    "reaction_data":       "10.1016/j.fluid.2016.01.035",
    "multi_property_6":    "10.1016/j.fluid.2005.07.015",
    "binary_vle":          "10.1007/s10765-006-0018-5",
    "complex_constraints": "10.1016/j.fluid.2016.03.016",
    "large_block":         "10.1021/je060271a",
    "many_compounds":      "10.1021/je3010535",
    "mixed_block_types":   "10.1016/j.jct.2003.08.017",
}


def _write_json_atomically(path, payload):
    """Strictly serialize before replacing one diagnostic JSON artifact."""
    serialized = json.dumps(
        payload,
        indent=2,
        ensure_ascii=False,
        allow_nan=False,
    )
    directory = os.path.dirname(path)
    descriptor, staging = tempfile.mkstemp(
        dir=directory,
        prefix=f".{os.path.basename(path)}.",
        suffix=".building",
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(serialized)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(staging, path)
    finally:
        if os.path.exists(staging):
            os.remove(staging)


def load_paper(doi, db_path=DB_PATH):
    """Load a paper's JSON data from the raw database."""
    conn = sqlite3.connect(db_path)
    row = conn.execute("SELECT json_data FROM papers WHERE doi = ?", (doi,)).fetchone()
    conn.close()
    if not row:
        raise ValueError(f"DOI not found in database: {doi}")
    return json.loads(row[0])


def parse_doi(doi, index, db_path=DB_PATH, max_datapoints=50):
    """Parse a single DOI into all card types.

    Returns:
        dict with keys: rms, ccs, mtdks, pcs, ccs_identity
    """
    data = load_paper(doi, db_path)
    cards = {
        "rms":          build_rms_card(data, index),
        "ccs":          build_ccs_card(data, index),
        "mtdks":        build_mtdks_card(data, index),
        "pcs":          build_pcs_card(data, index, max_datapoints_per_block=max_datapoints),
        "ccs_identity": build_ccs_identity_cards_for_doi(data, index),
    }
    validate_nested_identifiers(cards, path=f"parsed[{doi}]")
    return cards


def save_cards(doi, cards, output_dir=OUTPUT_DIR):
    """Save all card types to JSON files under output_dir/{doi_slug}/."""
    doi_slug = doi.replace("/", "_").replace(":", "_")
    doi_dir = os.path.join(output_dir, doi_slug)
    os.makedirs(doi_dir, exist_ok=True)

    for card_type, card in cards.items():
        if card_type == "ccs_identity":
            # List of identity cards — one file per compound
            for identity_card in card:
                validate_nested_identifiers(identity_card, path=f"ccs_identity[{doi}]")
                cid = identity_card["comp_num_id"]
                fpath = os.path.join(doi_dir, f"ccs_identity_{cid}.json")
                _write_json_atomically(fpath, identity_card)
        else:
            validate_nested_identifiers(card, path=f"{card_type}[{doi}]")
            fpath = os.path.join(doi_dir, f"{card_type}_card.json")
            _write_json_atomically(fpath, card)

    return doi_dir


def print_card_summary(doi, cards):
    """Print a concise summary of all parsed cards."""
    print(f"\n{'='*80}")
    print(f"  DOI: {doi}")
    print(f"{'='*80}")

    rms = cards["rms"]
    di = rms["data_inventory"]
    print(f"  RMS: {rms['bibliographic']['title'][:70]}...")
    print(f"       lit_num_id={rms['identity']['lit_num_id']}")
    print(f"       {di['n_compounds']} compounds, {di['n_blocks']} blocks, {di['n_datapoints']} pts")

    ccs = cards["ccs"]
    n_samples = sum(len(c.get("samples") or []) for c in ccs["compounds"])
    indexed = sum(1 for c in ccs["compounds"] if c["comp_num_id"])
    print(f"  CCS: {len(ccs['compounds'])} compounds ({indexed} indexed), {n_samples} samples")

    identity_cards = cards.get("ccs_identity", [])
    print(f"  CCS Identity: {len(identity_cards)} compound cards")

    mtdks = cards["mtdks"]
    ms = mtdks["methods_summary"]
    indexed_m = sum(1 for m in mtdks["methods"] if m["meas_num_id"])
    print(f"  MTDKS: {ms['n_unique_methods']} methods ({ms['n_standard']} std, {ms['n_custom']} custom, {indexed_m} indexed)")

    pcs = cards["pcs"]
    bs = pcs["blocks_summary"]
    print(f"  PCS: {bs['n_blocks']} blocks ({bs['n_pure_or_mixture']} P/M, {bs['n_reaction']} rxn)")
    print(f"       {bs['total_datapoints']} total pts, T={bs.get('temperature_range_K')}, P={bs.get('pressure_range_kPa')}")

    for idx_entry in bs["block_index"][:5]:
        print(f"       {idx_entry['block_number']}: {idx_entry['property_names']} via {idx_entry['method']} ({idx_entry['n_points']} pts)")
    if len(bs["block_index"]) > 5:
        print(f"       ... and {len(bs['block_index']) - 5} more blocks")

    # Edge case flags
    flags = []
    if bs["n_reaction"] > 0:
        flags.append("REACTION_DATA")
    if any(len(b.get("properties", [])) > 1 for b in pcs["blocks"]):
        flags.append("MULTI_PROPERTY")
    if bs["total_datapoints"] > 1000:
        flags.append("LARGE_DATASET")
    if di["n_compounds"] > 10:
        flags.append("MANY_COMPOUNDS")
    if any(len(b.get("constraints", [])) >= 3 for b in pcs["blocks"]):
        flags.append("COMPLEX_CONSTRAINTS")
    for b in pcs["blocks"]:
        phases = set()
        for p in b.get("properties", []):
            pp = p.get("property_phase")
            if pp:
                phases.add(pp.get("phase", ""))
        if len(phases) > 1:
            flags.append("MULTI_PHASE")
            break
    if flags:
        print(f"  FLAGS: {', '.join(flags)}")


def validate_pcs_card(card):
    """Basic structural validation of a PCS INDIV card. Returns list of errors."""
    if not isinstance(card, dict):
        return ["PCS card must be an object"]
    errors = []
    required = {"key", "paper", "blocks_summary", "blocks"}
    missing = required - card.keys()
    if missing:
        return [f"Missing required top-level fields: {sorted(missing)}"]
    unknown = card.keys() - required
    if unknown:
        errors.append(f"Unknown top-level fields: {sorted(unknown)}")
    for field in ("key", "paper"):
        if not isinstance(card[field], dict):
            errors.append(f"{field} must be an object")
    try:
        validate_nested_identifiers(card)
    except (TypeError, ValueError) as exc:
        errors.append(str(exc))
    try:
        key = card.get("key")
        doi = key.get("doi") if isinstance(key, dict) else None
        validate_card_identity_indexes(
            card,
            doi=doi,
        )
    except (AttributeError, KeyError, TypeError, ValueError) as exc:
        errors.append(str(exc))

    bs = card["blocks_summary"]
    blocks = card["blocks"]
    if not isinstance(bs, dict):
        errors.append("blocks_summary must be an object")
        return errors
    if not isinstance(blocks, list):
        errors.append("blocks must be a list")
        return errors
    if "n_blocks" not in bs:
        errors.append("blocks_summary is missing n_blocks")
    elif (
        isinstance(bs["n_blocks"], bool)
        or not isinstance(bs["n_blocks"], int)
        or bs["n_blocks"] < 0
    ):
        errors.append(
            "blocks_summary.n_blocks must be a nonnegative integer"
        )
    elif bs["n_blocks"] != len(blocks):
        errors.append(
            f"n_blocks mismatch: summary={bs['n_blocks']} actual={len(blocks)}"
        )

    for i, block in enumerate(blocks):
        prefix = f"blocks[{i}]"
        if not isinstance(block, dict):
            errors.append(f"{prefix}: block must be an object")
            continue
        properties = block.get("properties")
        compounds = block.get("compounds")
        if not isinstance(properties, list):
            errors.append(f"{prefix}.properties must be a list")
            continue
        if not isinstance(compounds, list):
            errors.append(f"{prefix}.compounds must be a list")
            continue
        if not properties:
            errors.append(f"{prefix}: no properties")
        if (
            block.get("block_type") == "ReactionData"
            and not block.get("reaction")
        ):
            errors.append(f"{prefix}: ReactionData but no reaction field")

        # Check indexed fields
        for j, prop in enumerate(properties):
            if not isinstance(prop, dict):
                errors.append(
                    f"{prefix}.properties[{j}]: property must be an object"
                )
                continue
            if not prop.get("prop_ID"):
                errors.append(f"{prefix}.properties[{j}]: empty prop_ID")
            if not prop.get("group"):
                errors.append(f"{prefix}.properties[{j}]: empty group")

        for j, comp in enumerate(compounds):
            if not isinstance(comp, dict):
                errors.append(
                    f"{prefix}.compounds[{j}]: compound must be an object"
                )
                continue
            if comp.get("comp_num_id") is None:
                errors.append(f"{prefix}.compounds[{j}]: missing comp_num_id")

    return errors


def run_edge_cases(output_dir=OUTPUT_DIR, max_datapoints=50):
    """Parse all edge-case DOIs and save results to output_dir."""
    index = ThermoMLIndex()
    os.makedirs(output_dir, exist_ok=True)

    results = {}
    for case_name, doi in sorted(EDGE_CASE_DOIS.items()):
        print(f"\nParsing: {case_name} ({doi})")
        try:
            cards = parse_doi(doi, index, max_datapoints=max_datapoints)
            save_dir = save_cards(doi, cards, output_dir)
            print_card_summary(doi, cards)

            errors = validate_pcs_card(cards["pcs"])
            if errors:
                print(f"  VALIDATION ERRORS:")
                for e in errors:
                    print(f"    - {e}")
            else:
                print(f"  VALIDATION: OK")

            results[case_name] = {"doi": doi, "status": "ok", "errors": errors}
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback
            traceback.print_exc()
            results[case_name] = {"doi": doi, "status": "error", "error": str(e)}

    print(f"\n{'='*80}")
    print(f"  SUMMARY: {sum(1 for r in results.values() if r['status'] == 'ok')}/{len(results)} parsed successfully")
    for name, r in sorted(results.items()):
        if r["status"] == "ok":
            n_err = len(r.get("errors", []))
            status = "OK" if n_err == 0 else f"WARN({n_err})"
        else:
            status = "ERROR"
        print(f"    {name:25s} {status}")

    return results


if __name__ == "__main__":
    if "--edge-cases" in sys.argv:
        run_edge_cases()
    elif "--doi" in sys.argv:
        idx_pos = sys.argv.index("--doi")
        doi = sys.argv[idx_pos + 1]
        index = ThermoMLIndex()
        cards = parse_doi(doi, index)
        save_dir = save_cards(doi, cards)
        print_card_summary(doi, cards)
        print(f"\n  Saved to: {save_dir}")
    else:
        doi = EDGE_CASE_DOIS["simple_unary"]
        index = ThermoMLIndex()
        cards = parse_doi(doi, index)
        save_dir = save_cards(doi, cards)
        print_card_summary(doi, cards)
        print(f"\n  Saved to: {save_dir}")
