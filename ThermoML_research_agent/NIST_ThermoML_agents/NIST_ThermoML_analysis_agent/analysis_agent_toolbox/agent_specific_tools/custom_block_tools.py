"""Agent-built custom block tools — explicitly sourced alternate data channel.
==========================================================
``register_custom_block`` lets the analysis agent register a self-built
data block under a pseudo-DOI (``agentblock/<label>``) so that ALL
deterministic tools (inspect_block, get_pure_values, fit_block,
propose_fitting_plan) can operate on it unchanged.

Hard policy (enforced here, not just prompted)
----------------------------------------------
1. **Missing-data only** — the tool first searches the ThermoML DB for the
   same compounds + property (optionally narrowed by temperature range)
   and REFUSES to register when real experimental blocks exist.
2. **Justified guesses only** — estimated numbers are allowed, but the
   call must carry a substantial ``basis`` (justification text) and
   ``citations`` pointing at real DOIs (optionally ``DOI#PROPblock_N``)
   that exist in the ThermoML DB.  Invalid or unknown citations are
   rejected.
3. **Provenance** — registered blocks are stamped
   ``metadata["source"]="agent_built"`` and audited to the session
   data/ dir; results must be flagged AGENT-BUILT downstream.
"""

from __future__ import annotations

import importlib as _il
import logging
import re

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    block_local_id,
    doi_comp_id,
    require_block_id,
    require_global_id,
)

from ....general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import (
    ToolEntry,
    uses_compactors,
)
from ...analysis_agent_context_hooks.compactor_hooks._tool_compactors import (
    compact_register_custom_block,
)
from ...ThermoML_core_calc_tools.csv_io_helpers import (
    identify_columns,
    parse_csv_text,
    virtual_block_registry as _vbr,
)
from card_db_search_tools.basic_search_tools.normalization_helpers.range_helpers import (
    validate_range,
)
from card_db_search_tools.basic_search_tools._id_alignment_search import (
    resolve_compound_ids,
    resolve_property_ids,
    resolve_variable_ids,
)

_log = logging.getLogger("CUSTOM-BLOCK-TOOLS")

# Deterministic DB access (same lazy-import pattern as discovery_tools)
_search_blocks = getattr(
    _il.import_module("card_db_search_tools.basic_search_tools.1_block_search"),
    "search_blocks",
)
_block_extractor = _il.import_module(
    "card_db_search_tools.basic_search_tools.11_block_data_extractor"
)

_DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
_ANGLE_RE = re.compile(r"<([^>]+)>")

_MIN_ROWS = 5
_MIN_BASIS_CHARS = 40


# ------------------------------------------------------------------
#  Deterministic checks
# ------------------------------------------------------------------

def check_existing_coverage(
    compounds: list[str],
    property_name: str,
    temperature_range: list[float] | None = None,
    limit: int = 10,
) -> list[dict]:
    """Return existing DB blocks for compounds+property (empty = no data).

    Pure deterministic search — used as the missing-data gate.
    """
    if not isinstance(compounds, list) or len(compounds) < 2 or any(
        not isinstance(name, str) or not name for name in compounds
    ):
        raise TypeError("compounds must be an array of at least two non-empty names")
    if not isinstance(property_name, str) or not property_name:
        raise TypeError("property_name must be a non-empty string")
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise TypeError("limit must be a positive integer")
    kwargs: dict = dict(compound=compounds, property=property_name, limit=limit)
    if temperature_range is not None:
        validated = validate_range(temperature_range, field="temperature_range")
        assert validated is not None
        kwargs["temperature_range"] = list(validated)
    res = _search_blocks(**kwargs)
    if not isinstance(res, dict) or set(res) < {"n_results", "results"}:
        raise ValueError("search_blocks returned an invalid result object")
    if not isinstance(res["results"], list):
        raise TypeError("search_blocks.results must be an array")

    blocks = []
    for index, r in enumerate(res["results"]):
        if not isinstance(r, dict):
            raise TypeError(f"search_blocks.results[{index}] must be an object")
        required = {"doi", "block_number", "n_datapoints", "properties", "data_summary"}
        missing = required - r.keys()
        if missing:
            raise ValueError(
                f"search_blocks.results[{index}] is missing {sorted(missing)}"
            )
        require_block_id(r["block_number"])
        summary = r["data_summary"]
        props = r["properties"]
        if not isinstance(summary, dict) or "variable_ranges" not in summary:
            raise ValueError(
                f"search_blocks.results[{index}].data_summary requires variable_ranges"
            )
        if not isinstance(props, list):
            raise TypeError(f"search_blocks.results[{index}].properties must be an array")
        prop_str = "; ".join(p["name"] for p in props[:3])
        blocks.append({
            "doi": r["doi"],
            "block_number": r["block_number"],
            "n_datapoints": r["n_datapoints"],
            "properties": prop_str,
            "temperature_range": summary["variable_ranges"],
        })
    return blocks


def _validate_citations(citations: list[dict]) -> tuple[list[dict], list[str]]:
    """Parse + verify citations against the ThermoML DB.

    Format: ``[{"doi": ..., "block_number": ...}, ...]``; block_number is optional.
    Returns (valid_entries, errors).
    """
    entries: list[dict] = []
    errors: list[str] = []

    if not isinstance(citations, list):
        return [], ["citations must be an array of objects"]
    for index, raw in enumerate(citations):
        if not isinstance(raw, dict):
            errors.append(f"citations[{index}] must be an object")
            continue
        unknown = sorted(set(raw) - {"doi", "block_number"})
        missing = sorted({"doi"} - set(raw))
        if unknown or missing:
            errors.append(
                f"citations[{index}] has missing={missing} and unknown={unknown} fields"
            )
            continue
        doi = raw["doi"]
        block = raw["block_number"] if "block_number" in raw else None
        if not isinstance(doi, str) or (block is not None and not isinstance(block, str)):
            errors.append(f"citations[{index}] doi/block_number must be strings")
            continue
        if not _DOI_RE.match(doi):
            errors.append(f"citations[{index}]: not a valid DOI (expected 10.xxxx/...)")
            continue
        try:
            if block:
                require_block_id(block)
                probe = _block_extractor.extract_block_csv(doi, block)
                if not isinstance(probe, dict) or "error" not in probe:
                    raise ValueError("extract_block_csv returned an invalid result object")
                if probe["error"] is not None:
                    errors.append(f"citations[{index}]: {probe['error']}")
                    continue
            else:
                con = _block_extractor.open_db(_block_extractor._PCS_DB)
                try:
                    row = con.execute(
                        "SELECT 1 FROM cards WHERE doi = ?", (doi,)
                    ).fetchone()
                finally:
                    con.close()
                if row is None:
                    errors.append(f"citations[{index}]: DOI not found in the ThermoML DB")
                    continue
        except Exception as exc:
            errors.append(f"citations[{index}]: citation check failed ({exc})")
            continue
        entries.append({"doi": doi, "block_number": block})

    return entries, errors


def _validate_csv(
    csv_text: str,
    compound_names: list[str],
    property_name: str,
) -> tuple[dict | None, str | None, list[str]]:
    """Validate agent-built CSV. Returns (parsed, error, warnings).

    ``parsed`` = {"columns", "rows_float", "n_rows", "match"} on success.
    """
    warnings: list[str] = []
    try:
        columns, rows = parse_csv_text(csv_text.strip() + "\n")
    except Exception as exc:
        return None, f"CSV does not parse: {exc}", warnings

    if len(columns) < 2:
        return None, f"Need >=2 columns (composition + property); got {columns}.", warnings
    if len(rows) < _MIN_ROWS:
        return None, (
            f"Only {len(rows)} data rows — need >={_MIN_ROWS} for a meaningful "
            f"RK fit (and >=8 is recommended)."
        ), warnings
    if len(rows) < 8:
        warnings.append(f"Only {len(rows)} rows — fits will be low-confidence.")

    # Every cell must be numeric (agent-built data must be complete).
    rows_float: list[dict] = []
    for i, row in enumerate(rows, 1):
        frow = {}
        for col in columns:
            raw = row.get(col)
            try:
                frow[col] = float(raw)
            except (TypeError, ValueError):
                return None, (
                    f"Row {i}, column '{col}': non-numeric value {raw!r}. "
                    f"Agent-built blocks must be fully numeric."
                ), warnings
        rows_float.append(frow)

    match = identify_columns(columns, property_hint=property_name)
    if not match.ok:
        return None, (
            f"Column identification failed: {match.error} "
            f"Composition columns must contain mole_fraction/mass_fraction/"
            f"volume_fraction/molality/concentration and tag the compound "
            f"like 'mole_fraction_<ethanol>'; the property column should "
            f"match '{property_name}'."
        ), warnings

    # Composition sanity: fraction-type columns must lie in [0, 1].
    for col in match.x_columns:
        if "fraction" in col.lower():
            vals = [r[col] for r in rows_float]
            if min(vals) < -1e-9 or max(vals) > 1 + 1e-9:
                return None, (
                    f"Composition column '{col}' outside [0, 1]: "
                    f"min={min(vals):.4g}, max={max(vals):.4g}."
                ), warnings

    # Compound tags must be declared in `compounds`.
    declared = {n.lower() for n in compound_names}
    tags = {m.group(1) for col in columns for m in [_ANGLE_RE.search(col)] if m}
    unknown = {t for t in tags if t.lower() not in declared}
    if unknown:
        return None, (
            f"Column compound tags {sorted(unknown)} are not in the declared "
            f"compounds {compound_names}."
        ), warnings
    tagged_x = [c for c in match.x_columns if _ANGLE_RE.search(c)]
    if not tagged_x:
        return None, (
            "At least one composition column must carry a compound tag, "
            "e.g. 'mole_fraction_<water>'."
        ), warnings

    return (
        {"columns": columns, "rows_float": rows_float,
         "n_rows": len(rows_float), "match": match},
        None,
        warnings,
    )


def _build_metadata(
    pseudo_label: str,
    compound_names: list[str],
    property_name: str,
    parsed: dict,
    basis: str,
    citation_entries: list[dict],
) -> dict:
    """Mimic the real extract_block_csv() metadata shape."""
    match = parsed["match"]
    columns = parsed["columns"]
    cmap = {doi_comp_id(i): n for i, n in enumerate(compound_names, 1)}

    def _tag(col: str) -> str | None:
        m = _ANGLE_RE.search(col)
        return m.group(1) if m else None

    condition_cols = [
        c for c in columns
        if c not in match.x_columns and c not in match.y_columns
    ]

    def _one_exact(rows: list[dict], *, entity: str, id_field: str) -> dict:
        exact = [row for row in rows if row["score"] == 100]
        if len(exact) != 1:
            raise ValueError(
                f"TOOL_ARGUMENT_REFINEMENT_REQUIRED: {entity} must resolve to "
                f"exactly one global registry entry; found {len(exact)} exact matches"
            )
        require_global_id(id_field, exact[0][id_field])
        return exact[0]

    compound_rows: list[dict] = []
    doi_id_by_name: dict[str, str] = {}
    for index, name in enumerate(compound_names, 1):
        row = _one_exact(
            resolve_compound_ids(name, min_score=100, limit=20),
            entity=f"compound {name!r}",
            id_field="comp_num_id",
        )
        compound_rows.append(row)
        doi_id_by_name[name.lower()] = doi_comp_id(index)

    def _registry_template(column: str) -> str:
        tag = _tag(column)
        if tag is None:
            return column
        return _ANGLE_RE.sub("{DOIcomp_id}", column)

    def _resolved_occurrence(template: str, column: str) -> tuple[str, str]:
        tag = _tag(column)
        if tag is None:
            return template, ""
        org_num = doi_id_by_name[tag.lower()]
        return template.replace("{DOIcomp_id}", org_num), tag

    variable_entries: list[dict] = []
    for index, column in enumerate(match.x_columns + condition_cols, 1):
        template = _registry_template(column)
        row = _one_exact(
            resolve_variable_ids(template, min_score=100, limit=20),
            entity=f"variable column {column!r}",
            id_field="var_num_id",
        )
        resolved_id, compound = _resolved_occurrence(row["var_id"], column)
        variable_entries.append({
            "BLKvar_id": block_local_id("var", index),
            "var_num_id": row["var_num_id"],
            "var_id": resolved_id,
            "column_name": column,
            "compound": compound,
        })

    declared_property = _one_exact(
        resolve_property_ids(property_name, min_score=100, limit=20),
        entity=f"property_name {property_name!r}",
        id_field="prop_num_id",
    )
    property_entries: list[dict] = []
    for index, column in enumerate(match.y_columns, 1):
        template = _registry_template(column)
        rows = resolve_property_ids(template, min_score=100, limit=20)
        row = _one_exact(
            rows if rows else [declared_property],
            entity=f"property column {column!r}",
            id_field="prop_num_id",
        )
        if row["prop_num_id"] != declared_property["prop_num_id"]:
            raise ValueError(
                f"TOOL_ARGUMENT_REFINEMENT_REQUIRED: property column {column!r} "
                f"resolves to {row['prop_num_id']}, but property_name resolves to "
                f"{declared_property['prop_num_id']}"
            )
        resolved_id, compound = _resolved_occurrence(row["prop_id"], column)
        property_entries.append({
            "BLKprop_id": block_local_id("prop", index),
            "prop_num_id": row["prop_num_id"],
            "prop_ID": resolved_id,
            "column_name": column,
            "prop_group": row["prop_group"],
            "compound": compound,
            # Agent-built values are declared as absolute observations.
            # The numerical pipeline never infers a missing presentation.
            "presentation": "Direct value, X",
            "standard_state": None,
            "ref_state_type": None,
            "ref_temperature_K": None,
            "ref_pressure_kPa": None,
            "property_phase": None,
            "ref_phase": None,
            "component_org_num": None,
            "meas_num_id": None,
            "meas_ID": None,
        })

    return {
        "doi": f"agentblock/{pseudo_label}",
        "block_number": "PROPblock_1",
        "block_type": "agent_built_virtual",
        "compounds": [
            {
                "org_num": doi_comp_id(i),
                "comp_num_id": row["comp_num_id"],
                "name": row["common_name"],
                "formula": row["formula"],
            }
            for i, row in enumerate(compound_rows, 1)
        ],
        "compound_map": cmap,
        "variables": variable_entries,
        "properties": property_entries,
        "constraints": [],
        "solvents": [],
        "n_datapoints": parsed["n_rows"],
        # ── Provenance (agent-built) ─────────────────────────
        "source": "agent_built",
        "label": pseudo_label,
        "property_name": property_name,
        "basis": basis,
        "lit_num_id": citation_entries[0]["lit_num_id"],
        "source_lit_num_ids": list(dict.fromkeys(
            entry["lit_num_id"] for entry in citation_entries
        )),
        "identity_scope": "agent_built_with_literature_provenance",
        "citations": citation_entries,
    }


# ------------------------------------------------------------------
#  register_custom_block  (agent-facing tool)
# ------------------------------------------------------------------

@uses_compactors(compact_register_custom_block)
def register_custom_block(
    label: str,
    csv_text: str,
    compounds: list[str],
    property_name: str,
    basis: str,
    citations: list[dict],
    temperature_range: list[float] | None = None,
) -> dict:
    """Register an AGENT-BUILT data block as a fallback when the DB has no data.

    The block becomes addressable as ``doi=<returned pseudo_doi>``,
    ``block_number="PROPblock_1"`` in inspect_block / get_pure_values /
    fit_block / propose_fitting_plan.

    HARD GATES (the tool refuses otherwise):
    - The ThermoML DB must have NO existing blocks for these
      compounds + property (narrow with ``temperature_range`` if your
      need is condition-specific).
    - ``basis`` must give a solid justification for every estimated
      number (>= 40 chars).
    - ``citations`` must be structured DOI/block references to real
      ThermoML records from which the estimates were derived.

    Parameters
    ----------
    label : str
        Short name for the block (becomes ``agentblock/<label>``).
    csv_text : str
        CSV with header. Composition columns must follow DB naming,
        e.g. ``mole_fraction_<water>``; property column should match
        *property_name* (e.g. ``viscosity_pas``). Fully numeric.
    compounds : list[str]
        Array of at least two compound names.
    property_name : str
        Property this block reports (e.g. "viscosity", "density").
    basis : str
        Justification: how each value was estimated and from what.
    citations : list[dict]
        Non-empty array of objects with ``doi`` and optional ``block_number``.
    temperature_range : list[float], optional
        Exact two-number JSON array ``[minimum_K, maximum_K]`` for the
        existing-data check.
    """
    # ── Parameter gates ───────────────────────────────────────
    if not str(label).strip():
        return {"error": "label is required.", "status": "rejected"}
    if not str(csv_text).strip():
        return {"error": "csv_text is required.", "status": "rejected"}
    if not isinstance(compounds, list) or len(compounds) < 2 or any(
        not isinstance(name, str) or not name for name in compounds
    ):
        return {"error": "compounds must be an array of at least two non-empty names.",
                "status": "rejected"}
    compound_names = compounds
    if not str(property_name).strip():
        return {"error": "property_name is required.", "status": "rejected"}
    if len(str(basis).strip()) < _MIN_BASIS_CHARS:
        return {
            "error": (
                f"basis too short ({len(str(basis).strip())} chars, need >= "
                f"{_MIN_BASIS_CHARS}). Estimated numbers require a solid "
                f"justification: what was assumed, derived from which data."
            ),
            "status": "rejected",
        }

    citation_entries, cite_errors = _validate_citations(citations)
    if cite_errors or not citation_entries:
        return {
            "error": "Citations to actual ThermoML data are required.",
            "citation_errors": cite_errors or ["no citations given"],
            "status": "rejected",
        }

    # ── Fallback-only gate: refuse when real data exists ──────
    existing = check_existing_coverage(
        compounds, property_name, temperature_range=temperature_range,
    )
    if existing and "error" in existing[0]:
        return {
            "error": (
                "Could not verify data absence (coverage check failed) — "
                "refusing to register an agent-built block. "
                + existing[0]["error"]
            ),
            "status": "rejected",
        }
    if existing:
        return {
            "status": "refused_existing_data",
            "reason": (
                f"The ThermoML DB already holds {len(existing)} block(s) for "
                f"{' + '.join(compound_names)} / {property_name}"
                + (f" in T range {temperature_range} K" if temperature_range else "")
                + ". Agent-built blocks are fallback-only: use the real data."
            ),
            "existing_blocks": existing,
            "compounds": compound_names,
            "property_name": property_name,
        }

    # ── Data validation ───────────────────────────────────────
    parsed, err, warnings = _validate_csv(csv_text, compound_names, property_name)
    if err:
        return {"error": err, "status": "rejected"}

    # ── Register ──────────────────────────────────────────────
    metadata = _build_metadata(
        _vbr.sanitize_label(label), compound_names, property_name,
        parsed, str(basis).strip(), citation_entries,
    )
    pseudo_doi = _vbr.register_virtual_block(
        label, csv_text.strip() + "\n",
        parsed["columns"], parsed["n_rows"], metadata,
    )

    match = parsed["match"]
    col_ranges = {
        col: {"min": min(r[col] for r in parsed["rows_float"]),
              "max": max(r[col] for r in parsed["rows_float"])}
        for col in (match.x_columns + match.y_columns)
    }
    return {
        "status": "registered",
        "provenance": "agent_built",
        "pseudo_doi": pseudo_doi,
        "block_number": _vbr.VIRTUAL_BLOCK_NUMBER,
        "compounds": compound_names,
        "property_name": property_name,
        "n_rows": parsed["n_rows"],
        "columns": parsed["columns"],
        "identified_x": match.x_columns,
        "identified_y": match.y_columns,
        "column_ranges": col_ranges,
        "basis": str(basis).strip(),
        "lit_num_id": metadata["lit_num_id"],
        "source_lit_num_ids": metadata["source_lit_num_ids"],
        "citations": citation_entries,
        "warnings": warnings,
        "note": (
            f"AGENT-BUILT block. Use doi='{pseudo_doi}', "
            f"block_number='{_vbr.VIRTUAL_BLOCK_NUMBER}' in inspect_block / "
            f"get_pure_values / fit_block. Every result derived from it MUST "
            f"be flagged as agent-built (not experimental) in the answer."
        ),
    }


# ── Catalog entries ─────────────────────────────────────────────────

TOOL_ENTRIES = [
    ToolEntry(
        "register_custom_block", register_custom_block,
        group="custom_data",
    ),
]
