"""Prepare one ThermoML property response for numerical analysis.

ThermoML ``presentation`` describes the mathematical response stored in a
property column.  It is orthogonal to the global property identity: a column
may contain ``X``, ``X-X(ref)``, ``X/X(ref)``, or a relative difference for
the same ``prop_num_id``.  This module is the deterministic barrier between
authoritative reported values and chemistry calculations.

The LLM selects a block/property/state.  It never selects equations or
reference values.  Reference evidence is resolved from direct unary property
blocks, preferring the same DOI and then a provenance-complete global
ensemble.  Any unresolved or ambiguous response fails closed.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from typing import Any, Mapping

import numpy as np

from card_db_search_tools.basic_search_tools.advanced_block_search.catalogs import (
    PM_REGISTRY_DB,
    load_runtime_catalogs,
)
from card_db_search_tools.basic_search_tools.normalization_helpers.db_helpers import (
    open_db,
)
from specialized_tools_pipelines.property_screening_ranking_tool.interface import (
    CandidateRef,
)
from specialized_tools_pipelines.property_screening_ranking_tool.sources.reader import (
    AuthoritativeBlockReader,
)
from specialized_tools_pipelines.property_screening_ranking_tool.unit_conversion_lib.block_alignment import (
    align_authoritative_block_units,
)
from specialized_tools_pipelines.property_screening_ranking_tool.unit_conversion_lib.property_response import (
    PURE_COMPONENTS_SAME_PROPORTION,
    PURE_SOLUTE_SAME_STATE,
    PURE_SOLVENT_SAME_STATE,
    PresentationKind,
    classify_presentation,
    materialize_reported_response,
    presentation_requires_reference,
    reference_component_num_ids,
    reported_canonical_unit,
)


_SUPPORTED_REFERENCE_STATES = {
    PURE_SOLVENT_SAME_STATE,
    PURE_SOLUTE_SAME_STATE,
    PURE_COMPONENTS_SAME_PROPORTION,
}


class PropertyResponsePreparationError(ValueError):
    """A reported response cannot safely enter chemistry calculations."""

    def __init__(self, code: str, message: str, *, details: dict | None = None):
        super().__init__(message)
        self.code = code
        self.details = details or {}

    def as_dict(self) -> dict[str, Any]:
        return {
            "error": f"{self.code}: {self}",
            "error_code": self.code,
            "details": dict(self.details),
        }


@dataclass(frozen=True)
class PreparedPropertyResponse:
    """Absolute values of one declared property plus its derivation trace."""

    values: np.ndarray
    declaration: dict[str, Any]
    trace: dict[str, Any]


def _require_property_declaration(
    metadata: Mapping[str, Any], y_column: str
) -> dict[str, Any]:
    properties = metadata.get("properties")
    if not isinstance(properties, list):
        raise PropertyResponsePreparationError(
            "PROPERTY_METADATA_MISSING",
            "Block metadata does not contain property declarations.",
        )
    matches = [
        item
        for item in properties
        if isinstance(item, dict) and item.get("column_name") == y_column
    ]
    if len(matches) != 1:
        raise PropertyResponsePreparationError(
            "PROPERTY_DECLARATION_NOT_UNIQUE",
            f"Column {y_column!r} resolves to {len(matches)} property declarations.",
            details={"y_column": y_column},
        )
    return dict(matches[0])


def _phase_num_id(value: object) -> str | None:
    if not isinstance(value, dict):
        return None
    phase_num_id = value.get("phase_num_id")
    return phase_num_id if isinstance(phase_num_id, str) else None


def _reference_candidates(
    comp_num_id: str, prop_num_id: str
) -> tuple[CandidateRef, ...]:
    sql = (
        "SELECT * FROM block_registry br "
        "WHERE br.system_type='unary' "
        "AND EXISTS (SELECT 1 FROM json_each(br.comp_ids_smiles) c "
        "WHERE json_extract(c.value,'$.comp_num_id')=?) "
        "AND EXISTS (SELECT 1 FROM json_each(br.prop_ids_meas_ranges) p "
        "WHERE json_extract(p.value,'$.prop_num_id')=?) "
        "ORDER BY br.doi,br.block_number"
    )
    connection = open_db(str(PM_REGISTRY_DB))
    try:
        rows = connection.execute(sql, (comp_num_id, prop_num_id)).fetchall()
    finally:
        connection.close()
    output: list[CandidateRef] = []
    for row in rows:
        compounds = json.loads(row["comp_ids_smiles"])
        ids = tuple(str(item["comp_num_id"]) for item in compounds)
        output.append(
            CandidateRef(
                doi=row["doi"],
                lit_num_id=row["lit_num_id"],
                block_number=row["block_number"],
                BLKsubsys_id=None,
                search_scope="declared",
                block_type=row["block_type"],
                declared_system_type="unary",
                effective_system_type="unary",
                comp_num_ids=ids,
                n_datapoints=int(row["n_datapoints"]),
            )
        )
    return tuple(output)


def _state_field(
    block,
    quantity: str,
) -> tuple[str | None, str | None]:
    """Return (local_id, canonical_unit) for temperature or pressure."""
    translation = load_runtime_catalogs().translation.by_global_id
    matches: list[tuple[str, str]] = []
    for section, local_field, global_field in (
        ("variables", "BLKvar_id", "var_num_id"),
        ("constraints", "BLKconstr_id", "constr_num_id"),
    ):
        for declaration in block.projected.get(section, []):
            global_id = declaration.get(global_field)
            local_id = declaration.get(local_field)
            registry = translation.get(global_id)
            if registry is None or not isinstance(local_id, str):
                continue
            key = registry.quantity_key.casefold()
            if quantity == "temperature_k" and key.startswith("temperature_"):
                matches.append((local_id, registry.semantics.canonical_unit or ""))
            if quantity == "pressure_kpa" and key.startswith("pressure_"):
                matches.append((local_id, registry.semantics.canonical_unit or ""))
    unique = list(dict.fromkeys(matches))
    if len(unique) > 1:
        raise PropertyResponsePreparationError(
            "REFERENCE_STATE_FIELD_AMBIGUOUS",
            f"Unary reference block has multiple {quantity} fields.",
            details={"fields": unique, "source": block.candidate.as_dict()},
        )
    return unique[0] if unique else (None, None)


def _row_matches_state(
    row: Mapping[str, Any],
    fields: Mapping[str, str | None],
    state: Mapping[str, float | None],
    tolerances: Mapping[str, float],
) -> bool:
    for quantity in ("temperature_k", "pressure_kpa"):
        target = state.get(quantity)
        if target is None:
            continue
        local_id = fields.get(quantity)
        if local_id is None:
            return False
        value = row.get(local_id)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return False
        if abs(float(value) - float(target)) > float(tolerances[quantity]):
            return False
    return True


def _direct_reference_records(
    comp_num_id: str,
    prop_num_id: str,
    phase_num_id: str | None,
    state: Mapping[str, float | None],
    tolerances: Mapping[str, float],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    rejections: list[dict[str, Any]] = []
    with AuthoritativeBlockReader() as reader:
        for candidate in _reference_candidates(comp_num_id, prop_num_id):
            candidate_identity = {
                "doi": candidate.doi,
                "lit_num_id": candidate.lit_num_id,
                "block_number": candidate.block_number,
            }
            try:
                block = align_authoritative_block_units(reader.read(candidate))
                temperature_field, _ = _state_field(block, "temperature_k")
                pressure_field, _ = _state_field(block, "pressure_kpa")
                fields = {
                    "temperature_k": temperature_field,
                    "pressure_kpa": pressure_field,
                }
                matched_property = False
                matched_direct = False
                matched_phase = False
                retained_record = False
                for declaration in block.projected.get("properties", []):
                    if declaration.get("prop_num_id") != prop_num_id:
                        continue
                    matched_property = True
                    kind = classify_presentation(declaration.get("presentation"))
                    if kind != PresentationKind.DIRECT:
                        continue
                    matched_direct = True
                    source_phase = _phase_num_id(declaration.get("property_phase"))
                    if phase_num_id is not None and source_phase != phase_num_id:
                        continue
                    matched_phase = True
                    local_id = declaration.get("BLKprop_id")
                    if not isinstance(local_id, str):
                        continue
                    retained = [
                        (row.get(local_id), row.get("BLKpoint_id"))
                        for row in block.rows
                        if _row_matches_state(row, fields, state, tolerances)
                    ]
                    values = np.asarray(
                        [
                            float(value)
                            for value, _point_id in retained
                            if isinstance(value, (int, float))
                            and not isinstance(value, bool)
                            and math.isfinite(float(value))
                        ],
                        dtype=float,
                    )
                    if values.size == 0:
                        continue
                    point_ids = [
                        str(point_id)
                        for value, point_id in retained
                        if isinstance(value, (int, float))
                        and not isinstance(value, bool)
                        and math.isfinite(float(value))
                        and isinstance(point_id, str)
                    ]
                    records.append(
                        {
                            "doi": candidate.doi,
                            "lit_num_id": candidate.lit_num_id,
                            "block_number": candidate.block_number,
                            "BLKprop_id": local_id,
                            "comp_num_id": comp_num_id,
                            "prop_num_id": prop_num_id,
                            "phase_num_id": source_phase,
                            "mean": float(np.mean(values)),
                            "median": float(np.median(values)),
                            "minimum": float(np.min(values)),
                            "maximum": float(np.max(values)),
                            "standard_deviation": float(np.std(values, ddof=0)),
                            "n_observations": int(values.size),
                            "BLKpoint_ids": point_ids,
                        }
                    )
                    retained_record = True
                if not retained_record:
                    if not matched_property:
                        reason = "global_property_not_declared"
                    elif not matched_direct:
                        reason = "reference_property_is_not_direct"
                    elif not matched_phase:
                        reason = "reference_phase_mismatch"
                    else:
                        reason = "no_row_matches_requested_state"
                    rejections.append({**candidate_identity, "reason": reason})
            except PropertyResponsePreparationError as exc:
                # A malformed or ambiguous candidate is local to that block.
                # Independent direct evidence remains admissible.
                rejections.append(
                    {
                        **candidate_identity,
                        "reason": "candidate_semantics_rejected",
                        "error_code": exc.code,
                    }
                )
            except Exception as exc:
                rejections.append(
                    {
                        **candidate_identity,
                        "reason": "candidate_read_failed",
                        "error_type": type(exc).__name__,
                    }
                )
    return records, rejections


def _resolve_reference_value(
    *,
    comp_num_id: str,
    prop_num_id: str,
    phase_num_id: str | None,
    state: Mapping[str, float | None],
    tolerances: Mapping[str, float],
    preferred_doi: str,
) -> tuple[float, dict[str, Any]]:
    records, rejections = _direct_reference_records(
        comp_num_id,
        prop_num_id,
        phase_num_id,
        state,
        tolerances,
    )
    same_doi = [item for item in records if item["doi"] == preferred_doi]
    selected = same_doi or records
    if not selected:
        raise PropertyResponsePreparationError(
            "PRESENTATION_REFINEMENT_REQUIRED",
            "No direct unary reference property matches the required component, phase, and state.",
            details={
                "comp_num_id": comp_num_id,
                "prop_num_id": prop_num_id,
                "phase_num_id": phase_num_id,
                "state": dict(state),
                "tolerances": dict(tolerances),
                "n_reference_blocks_considered": len(records) + len(rejections),
                "candidate_rejections": rejections[:20],
            },
        )
    block_means = np.asarray([item["mean"] for item in selected], dtype=float)
    value = float(np.mean(block_means))
    return value, {
        "reference_tier": (
            "same_doi_unary_ensemble" if same_doi else "global_unary_ensemble"
        ),
        "representative_value": value,
        "distribution": {
            "mean_of_block_means": value,
            "median_of_block_means": float(np.median(block_means)),
            "minimum_block_mean": float(np.min(block_means)),
            "maximum_block_mean": float(np.max(block_means)),
            "standard_deviation_of_block_means": float(np.std(block_means, ddof=0)),
            "n_blocks": len(selected),
            "n_observations": sum(item["n_observations"] for item in selected),
        },
        "sources": selected,
    }


def _normalized_state(
    declaration: Mapping[str, Any],
    state: Mapping[str, float | None] | None,
) -> dict[str, float | None]:
    state = state or {}
    ref_temperature = declaration.get("ref_temperature_K")
    ref_pressure = declaration.get("ref_pressure_kPa")
    return {
        "temperature_k": (
            float(ref_temperature)
            if isinstance(ref_temperature, (int, float))
            and not isinstance(ref_temperature, bool)
            else state.get("temperature_k")
        ),
        "pressure_kpa": (
            float(ref_pressure)
            if isinstance(ref_pressure, (int, float))
            and not isinstance(ref_pressure, bool)
            else state.get("pressure_kpa")
        ),
    }


def prepare_property_response(
    *,
    metadata: Mapping[str, Any],
    y_column: str,
    reported_values: np.ndarray,
    normalized_composition: Mapping[str, np.ndarray] | None = None,
    state: Mapping[str, float | None] | None = None,
    state_tolerances: Mapping[str, float] | None = None,
) -> PreparedPropertyResponse:
    """Return an absolute property vector or fail before calculation.

    ``normalized_composition`` is keyed by strict ``GLOBcomp_N`` IDs and must
    contain one mole-fraction vector per active component when a same-
    proportion reference is requested.
    """
    values = np.asarray(reported_values, dtype=float)
    declaration = _require_property_declaration(metadata, y_column)
    prop_num_id = declaration.get("prop_num_id")
    if not isinstance(prop_num_id, str):
        raise PropertyResponsePreparationError(
            "PROPERTY_GLOBAL_ID_MISSING",
            f"Property declaration for {y_column!r} lacks prop_num_id.",
        )
    registry = load_runtime_catalogs().translation.by_global_id.get(prop_num_id)
    if registry is None:
        raise PropertyResponsePreparationError(
            "PROPERTY_GLOBAL_ID_UNKNOWN",
            f"Property {prop_num_id!r} is absent from the translation registry.",
        )
    canonical_unit = registry.semantics.canonical_unit or ""
    presentation = declaration.get("presentation")
    kind = classify_presentation(presentation)
    reported_unit = reported_canonical_unit(kind, canonical_unit)
    identity = {
        "doi": metadata.get("doi"),
        "lit_num_id": metadata.get("lit_num_id"),
        "block_number": metadata.get("block_number"),
        "BLKsubsys_id": metadata.get("BLKsubsys_id"),
        "BLKprop_id": declaration.get("BLKprop_id"),
        "prop_num_id": prop_num_id,
        "quantity_key": registry.quantity_key,
        "column_name": y_column,
        "standard_state": declaration.get("standard_state"),
        "property_phase": declaration.get("property_phase"),
        "ref_phase": declaration.get("ref_phase"),
        "meas_num_id": declaration.get("meas_num_id"),
        "meas_ID": declaration.get("meas_ID"),
    }
    if kind == PresentationKind.DIRECT:
        return PreparedPropertyResponse(
            values=values.copy(),
            declaration=declaration,
            trace={
                **identity,
                "status": "identity",
                "reported_presentation": presentation,
                "presentation_kind": kind.value,
                "reported_unit": reported_unit,
                "absolute_unit": canonical_unit,
                "response_semantics": "absolute_observed_quantity",
                "equation": "X = reported X",
                "reference_state": None,
                "reference_sources": [],
            },
        )
    if not presentation_requires_reference(kind):
        raise PropertyResponsePreparationError(
            "PROPERTY_PRESENTATION_UNSUPPORTED",
            f"Presentation {presentation!r} cannot be reduced to one absolute-state property.",
            details={**identity, "presentation_kind": kind.value},
        )

    ref_state_type = declaration.get("ref_state_type")
    if ref_state_type not in _SUPPORTED_REFERENCE_STATES:
        raise PropertyResponsePreparationError(
            "REFERENCE_STATE_UNSUPPORTED",
            f"Reference state {ref_state_type!r} is unsupported.",
            details=identity,
        )
    block_view = {
        "compounds": metadata.get("compounds", []),
        "solvents": metadata.get("solvents", []),
    }
    reference_ids, resolution = reference_component_num_ids(
        block_view, declaration
    )
    if not reference_ids:
        raise PropertyResponsePreparationError(
            "REFERENCE_COMPONENT_UNRESOLVED",
            f"Reference component could not be resolved: {resolution}.",
            details=identity,
        )
    requested_state = _normalized_state(declaration, state)
    tolerances = {
        "temperature_k": 0.5,
        "pressure_kpa": 1.0,
        **(dict(state_tolerances) if state_tolerances else {}),
    }
    ref_phase_num_id = (
        _phase_num_id(declaration.get("ref_phase"))
        or _phase_num_id(declaration.get("property_phase"))
    )
    doi = metadata.get("doi")
    if not isinstance(doi, str):
        raise PropertyResponsePreparationError(
            "BLOCK_DOI_MISSING",
            "Block metadata lacks DOI required for reference-source priority.",
            details=identity,
        )

    ensembles: dict[str, dict[str, Any]] = {}
    pure_values: dict[str, float] = {}
    for comp_num_id in reference_ids:
        value, ensemble = _resolve_reference_value(
            comp_num_id=comp_num_id,
            prop_num_id=prop_num_id,
            phase_num_id=ref_phase_num_id,
            state=requested_state,
            tolerances=tolerances,
            preferred_doi=doi,
        )
        pure_values[comp_num_id] = value
        ensembles[comp_num_id] = ensemble

    reference: float | np.ndarray
    reference_equation: str
    if ref_state_type == PURE_COMPONENTS_SAME_PROPORTION:
        if normalized_composition is None:
            raise PropertyResponsePreparationError(
                "REFERENCE_COMPOSITION_REQUIRED",
                "Same-proportion materialization requires normalized mole fractions.",
                details=identity,
            )
        active_ids = {
            str(item.get("comp_num_id"))
            for item in metadata.get("compounds", [])
            if isinstance(item, dict) and isinstance(item.get("comp_num_id"), str)
        }
        if set(reference_ids) != active_ids:
            raise PropertyResponsePreparationError(
                "REFERENCE_COMPONENT_SET_MISMATCH",
                "Same-proportion reference components do not match the active system.",
                details={**identity, "reference_ids": list(reference_ids), "active_ids": sorted(active_ids)},
            )
        missing = active_ids.difference(normalized_composition)
        if missing:
            raise PropertyResponsePreparationError(
                "REFERENCE_COMPOSITION_INCOMPLETE",
                f"Normalized composition is missing {sorted(missing)}.",
                details=identity,
            )
        fractions = {
            comp_num_id: np.asarray(normalized_composition[comp_num_id], dtype=float)
            for comp_num_id in sorted(active_ids)
        }
        if any(vector.shape != values.shape for vector in fractions.values()):
            raise PropertyResponsePreparationError(
                "REFERENCE_COMPOSITION_SHAPE_MISMATCH",
                "Composition vectors and reported property values have different shapes.",
                details=identity,
            )
        closure = np.sum(np.vstack(list(fractions.values())), axis=0)
        if not np.allclose(closure, 1.0, atol=1e-8, rtol=0.0):
            raise PropertyResponsePreparationError(
                "REFERENCE_COMPOSITION_NOT_CLOSED",
                "Normalized mole fractions do not close to one.",
                details={**identity, "closure_min": float(np.min(closure)), "closure_max": float(np.max(closure))},
            )
        reference = np.zeros_like(values, dtype=float)
        for comp_num_id, fraction in fractions.items():
            reference += fraction * pure_values[comp_num_id]
        reference_equation = "X_ref(row) = sum_i x_i * X_i,pure"
    else:
        if len(reference_ids) != 1:
            raise PropertyResponsePreparationError(
                "REFERENCE_COMPONENT_AMBIGUOUS",
                "Pure-solvent or pure-solute response requires exactly one reference component.",
                details={**identity, "reference_ids": list(reference_ids)},
            )
        reference = pure_values[reference_ids[0]]
        reference_equation = "X_ref = X_pure_component"

    converted, equation = materialize_reported_response(kind, values, reference)
    converted = np.asarray(converted, dtype=float)
    if converted.shape != values.shape or not np.all(np.isfinite(converted[np.isfinite(values)])):
        raise PropertyResponsePreparationError(
            "REFERENCE_MATERIALIZATION_NONFINITE",
            "Reference-state materialization produced invalid absolute values.",
            details=identity,
        )
    reference_sources = [
        source
        for ensemble in ensembles.values()
        for source in ensemble["sources"]
    ]
    return PreparedPropertyResponse(
        values=converted,
        declaration=declaration,
        trace={
            **identity,
            "status": "materialized",
            "reported_presentation": presentation,
            "presentation_kind": kind.value,
            "reported_unit": reported_unit,
            "absolute_unit": canonical_unit,
            "response_semantics": "absolute_observed_quantity",
            "equation": equation,
            "reference_state": {
                "ref_state_type": ref_state_type,
                "ref_phase_num_id": ref_phase_num_id,
                "state": requested_state,
                "tolerances": tolerances,
                "component_resolution": resolution,
                "reference_equation": reference_equation,
                "component_values": pure_values,
                "component_ensembles": ensembles,
            },
            "reference_sources": reference_sources,
        },
    )


def property_response_error_result(
    exc: PropertyResponsePreparationError,
    *,
    doi: str,
    lit_num_id: str,
    block_number: str,
    BLKsubsys_id: str | None,
) -> dict[str, Any]:
    """Convert a preparation exception to the analysis-tool error contract."""
    return {
        **exc.as_dict(),
        "doi": doi,
        "lit_num_id": lit_num_id,
        "block_number": block_number,
        "BLKsubsys_id": BLKsubsys_id,
    }


def inspect_property_response_contract(
    metadata: Mapping[str, Any],
    y_column: str,
) -> dict[str, Any]:
    """Describe the deterministic preparation required before calculation.

    This performs no reference lookup and no numerical materialization.  It
    is used by plan/inspection tools so the agent can see whether a selected
    property is already absolute or requires a reference-state gate.
    """
    declaration = _require_property_declaration(metadata, y_column)
    prop_num_id = declaration.get("prop_num_id")
    if not isinstance(prop_num_id, str):
        raise PropertyResponsePreparationError(
            "PROPERTY_GLOBAL_ID_MISSING",
            f"Property declaration for {y_column!r} lacks prop_num_id.",
        )
    registry = load_runtime_catalogs().translation.by_global_id.get(prop_num_id)
    if registry is None:
        raise PropertyResponsePreparationError(
            "PROPERTY_GLOBAL_ID_UNKNOWN",
            f"Property {prop_num_id!r} is absent from the translation registry.",
        )
    presentation = declaration.get("presentation")
    kind = classify_presentation(presentation)
    requires_reference = presentation_requires_reference(kind)
    ref_state_type = declaration.get("ref_state_type")
    supported = (
        kind == PresentationKind.DIRECT
        or (requires_reference and ref_state_type in _SUPPORTED_REFERENCE_STATES)
    )
    return {
        "BLKprop_id": declaration.get("BLKprop_id"),
        "prop_num_id": prop_num_id,
        "quantity_key": registry.quantity_key,
        "column_name": y_column,
        "reported_presentation": presentation,
        "presentation_kind": kind.value,
        "reported_unit": reported_canonical_unit(
            kind, registry.semantics.canonical_unit or ""
        ),
        "absolute_unit": registry.semantics.canonical_unit or "",
        "requires_reference_materialization": requires_reference,
        "requires_normalized_composition": (
            ref_state_type == PURE_COMPONENTS_SAME_PROPORTION
        ),
        "ref_state_type": ref_state_type,
        "ref_temperature_K": declaration.get("ref_temperature_K"),
        "ref_pressure_kPa": declaration.get("ref_pressure_kPa"),
        "property_phase": declaration.get("property_phase"),
        "ref_phase": declaration.get("ref_phase"),
        "component_org_num": declaration.get("component_org_num"),
        "supported": supported,
    }


def compact_property_response_trace(trace: Mapping[str, Any]) -> str:
    """Bounded one-line chemistry provenance for agent tool results."""
    identity = f"{trace.get('BLKprop_id')} / {trace.get('prop_num_id')}"
    kind = trace.get("presentation_kind")
    if trace.get("status") == "identity":
        return (
            f"Property response: {identity}: direct absolute value; "
            f"unit={trace.get('absolute_unit') or 'dimensionless'}."
        )
    sources = trace.get("reference_sources")
    source_count = len(sources) if isinstance(sources, list) else 0
    return (
        f"Property response: {identity}: {kind} -> absolute via "
        f"{trace.get('equation')}; {source_count} direct unary reference "
        f"source(s); unit {trace.get('reported_unit') or 'dimensionless'} -> "
        f"{trace.get('absolute_unit') or 'dimensionless'}."
    )


__all__ = [
    "PreparedPropertyResponse",
    "PropertyResponsePreparationError",
    "compact_property_response_trace",
    "inspect_property_response_contract",
    "prepare_property_response",
    "property_response_error_result",
]
