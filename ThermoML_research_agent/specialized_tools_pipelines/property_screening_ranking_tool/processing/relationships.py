"""Deterministic chemistry relationships for target-evidence materialization.

The agent names one ranking target.  Discovery may retrieve chemically
equivalent volume-density-molar evidence, but only this module is allowed to
turn that evidence into the requested response quantity.  Every transform is
one-way, dimensionally explicit, and provenance preserving.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Any

import numpy as np

from ..interface import Diagnostic, SourceSeries


EVIDENCE_METADATA: dict[str, dict[str, str]] = {
    "GLOBprop_1": {
        "quantity_key": "mass_density_kg_m3",
        "preferred_name": "Mass density, kg/m3",
        "canonical_unit": "kg/m3",
    },
    "GLOBprop_28": {
        "quantity_key": "excess_molar_volume_m3_mol",
        "preferred_name": "Excess molar volume, m3/mol",
        "canonical_unit": "m3/mol",
    },
    "GLOBprop_41": {
        "quantity_key": "molar_volume_m3_mol",
        "preferred_name": "Molar volume, m3/mol",
        "canonical_unit": "m3/mol",
    },
    "GLOBprop_67": {
        "quantity_key": "amount_density_mol_m3",
        "preferred_name": "Amount density, mol/m3",
        "canonical_unit": "mol/m3",
    },
    "GLOBprop_74": {
        "quantity_key": "specific_volume_m3_kg",
        "preferred_name": "Specific volume, m3/kg",
        "canonical_unit": "m3/kg",
    },
}


def evidence_metadata(global_id: str, source: SourceSeries) -> dict[str, str]:
    """Return canonical evidence metadata without accepting free-text aliases."""
    if global_id == source.target.source_global_id:
        return {
            "quantity_key": source.target.quantity_key,
            "preferred_name": source.target.preferred_name,
            "canonical_unit": source.target.canonical_unit,
        }
    try:
        return EVIDENCE_METADATA[global_id]
    except KeyError as exc:
        raise ValueError(f"no hard-coded evidence metadata for {global_id}") from exc


def _full_fraction_matrix(source: SourceSeries) -> np.ndarray:
    if source.coordinates.shape[1] == 0:
        return np.ones((len(source.values), 1), dtype=float)
    closure = 1.0 - source.coordinates.sum(axis=1, keepdims=True)
    return np.concatenate((source.coordinates, closure), axis=1)


def _molar_mass_vector(source: SourceSeries) -> np.ndarray | None:
    masses = source.derivation.get("molar_masses_g_mol", {})
    values = np.asarray(
        [masses.get(comp_num_id, np.nan) for comp_num_id in source.comp_num_ids],
        dtype=float,
    )
    if not np.all(np.isfinite(values)) or np.any(values <= 0):
        return None
    return values * 1e-3


def _compatible_unary_records(
    *,
    doi: str | None,
    phase_num_id: str | None,
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    compatible = [
        record
        for record in records
        if record.get("unit") == "m3/mol"
        and (
            phase_num_id is None
            or record.get("phase_num_id") == phase_num_id
        )
    ]
    same_doi = [
        record
        for record in compatible
        if doi is not None and record.get("source", {}).get("doi") == doi
    ]
    selected = same_doi or compatible
    if phase_num_id is None:
        phases = {record.get("phase_num_id") for record in selected}
        if len(phases) > 1:
            return []
    return selected


def select_unary_molar_volume_ensembles(
    comp_num_ids: tuple[str, ...],
    unary_reference_pool: dict[str, dict[str, list[dict[str, Any]]]],
    *,
    doi: str | None,
    phase_num_id: str | None,
) -> tuple[np.ndarray | None, list[dict[str, Any]]]:
    """Select same-state pure Vm ensembles without inventing phase matches."""
    values: list[float] = []
    ensembles: list[dict[str, Any]] = []
    for comp_num_id in comp_num_ids:
        records = _compatible_unary_records(
            doi=doi,
            phase_num_id=phase_num_id,
            records=unary_reference_pool.get(comp_num_id, {}).get(
                "molar_volume_m3_mol", []
            ),
        )
        if not records:
            return None, []
        raw = np.asarray([record["value"] for record in records], dtype=float)
        if not np.all(np.isfinite(raw)) or np.any(raw <= 0):
            return None, []
        representative = float(np.mean(raw))
        values.append(representative)
        ensembles.append(
            {
                "comp_num_id": comp_num_id,
                "reference_tier": (
                    "same_doi_unary_ensemble"
                    if any(
                        record.get("source", {}).get("doi") == doi
                        for record in records
                    )
                    else "global_unary_ensemble"
                ),
                "representative_value": representative,
                "canonical_unit": "m3/mol",
                "distribution": {
                    "mean": representative,
                    "median": float(np.median(raw)),
                    "standard_deviation": float(np.std(raw, ddof=0)),
                    "minimum": float(np.min(raw)),
                    "maximum": float(np.max(raw)),
                    "n_sources": len(records),
                    "n_observations": sum(
                        int(record.get("n_observations", 0)) for record in records
                    ),
                },
                "sources": records,
            }
        )
    return np.asarray(values, dtype=float), ensembles


def _to_molar_volume(
    source: SourceSeries,
    observed_id: str,
    unary_reference_pool: dict[str, dict[str, list[dict[str, Any]]]],
) -> tuple[np.ndarray | None, dict[str, Any], str | None]:
    x = _full_fraction_matrix(source)
    masses = _molar_mass_vector(source)
    values = np.asarray(source.values, dtype=float)
    if observed_id == "GLOBprop_41":
        return values.copy(), {"equation": "Vm = reported Vm"}, None
    if observed_id == "GLOBprop_67":
        if np.any(values <= 0):
            return None, {}, "nonpositive_amount_density"
        return 1.0 / values, {"equation": "Vm = 1 / amount_density"}, None
    if observed_id in {"GLOBprop_1", "GLOBprop_74"}:
        if masses is None:
            return None, {}, "molar_mass_unavailable"
        mixture_mass = x @ masses
        if observed_id == "GLOBprop_1":
            if np.any(values <= 0):
                return None, {}, "nonpositive_mass_density"
            return (
                mixture_mass / values,
                {"equation": "Vm = mixture_molar_mass / mass_density"},
                None,
            )
        if np.any(values <= 0):
            return None, {}, "nonpositive_specific_volume"
        return (
            values * mixture_mass,
            {"equation": "Vm = specific_volume * mixture_molar_mass"},
            None,
        )
    if observed_id == "GLOBprop_28":
        pure, ensembles = select_unary_molar_volume_ensembles(
            source.comp_num_ids,
            unary_reference_pool,
            doi=source.doi,
            phase_num_id=source.phase_num_id,
        )
        if pure is None:
            return None, {}, "unary_molar_volume_unavailable"
        ideal = x @ pure
        return (
            ideal + values,
            {
                "equation": "Vm = sum(x_i * Vm_i_pure) + excess_molar_volume",
                "unary_molar_volume_ensembles": ensembles,
            },
            None,
        )
    return None, {}, "unsupported_volumetric_evidence"


def _from_molar_volume(
    source: SourceSeries,
    vm: np.ndarray,
    unary_reference_pool: dict[str, dict[str, list[dict[str, Any]]]],
) -> tuple[np.ndarray | None, dict[str, Any], str | None]:
    target_id = source.target.source_global_id
    if target_id == "GLOBprop_41":
        return vm, {"equation": "target Vm = materialized Vm"}, None
    x = _full_fraction_matrix(source)
    masses = _molar_mass_vector(source)
    if target_id == "GLOBprop_28":
        pure, ensembles = select_unary_molar_volume_ensembles(
            source.comp_num_ids,
            unary_reference_pool,
            doi=source.doi,
            phase_num_id=source.phase_num_id,
        )
        if pure is None:
            return None, {}, "unary_molar_volume_unavailable"
        return (
            vm - x @ pure,
            {
                "equation": "excess_molar_volume = Vm - sum(x_i * Vm_i_pure)",
                "unary_molar_volume_ensembles": ensembles,
            },
            None,
        )
    if np.any(vm <= 0):
        return None, {}, "nonpositive_materialized_molar_volume"
    if target_id == "GLOBprop_67":
        return 1.0 / vm, {"equation": "amount_density = 1 / Vm"}, None
    if target_id in {"GLOBprop_1", "GLOBprop_74"}:
        if masses is None:
            return None, {}, "molar_mass_unavailable"
        mixture_mass = x @ masses
        if target_id == "GLOBprop_1":
            return (
                mixture_mass / vm,
                {"equation": "mass_density = mixture_molar_mass / Vm"},
                None,
            )
        if np.any(mixture_mass <= 0):
            return None, {}, "nonpositive_mixture_molar_mass"
        return (
            vm / mixture_mass,
            {"equation": "specific_volume = Vm / mixture_molar_mass"},
            None,
        )
    return None, {}, "target_not_in_volumetric_relationship_graph"


def materialize_target_evidence(
    sources: list[SourceSeries],
    unary_reference_pool: dict[str, dict[str, list[dict[str, Any]]]],
) -> tuple[list[SourceSeries], list[Diagnostic]]:
    """Convert absolute observed evidence into the requested target.

    ThermoML reference presentations must already have been materialized by
    ``materialize_property_presentations``.  This graph only performs
    relationships between physical quantities; it never interprets X/X(REF)
    or X-X(REF).
    """
    materialized: list[SourceSeries] = []
    diagnostics: list[Diagnostic] = []
    for source in sources:
        if source.response_semantics != "absolute_observed_quantity":
            diagnostics.append(
                Diagnostic(
                    code="NONABSOLUTE_EVIDENCE_AT_RELATIONSHIP_GATE",
                    message=(
                        "Cross-property materialization received a response "
                        "that was not converted to an absolute observed "
                        "quantity."
                    ),
                    stage="target_materialization",
                    severity="warning",
                    source_key=source.source_key,
                    details={
                        "response_semantics": source.response_semantics,
                        "presentation": source.presentation,
                    },
                )
            )
            continue
        observed_id = source.observed_global_id or source.target.source_global_id
        if observed_id == source.target.source_global_id:
            materialized.append(
                replace(source, response_semantics="absolute_target")
            )
            continue
        vm, first_trace, failure = _to_molar_volume(
            source, observed_id, unary_reference_pool
        )
        if vm is None:
            diagnostics.append(
                Diagnostic(
                    code="BRIDGE_EVIDENCE_UNRESOLVED",
                    message=(
                        f"{observed_id} could not construct "
                        f"{source.target.source_global_id}: {failure}."
                    ),
                    stage="composition_translation",
                    source_key=source.source_key,
                    details={"failure_reason": failure},
                )
            )
            continue
        converted, second_trace, failure = _from_molar_volume(
            source, vm, unary_reference_pool
        )
        if converted is None or not np.all(np.isfinite(converted)):
            diagnostics.append(
                Diagnostic(
                    code="BRIDGE_EVIDENCE_UNRESOLVED",
                    message=(
                        f"Materialized Vm could not construct "
                        f"{source.target.source_global_id}: {failure}."
                    ),
                    stage="composition_translation",
                    source_key=source.source_key,
                    details={"failure_reason": failure},
                )
            )
            continue
        materialized.append(
            replace(
                source,
                values=np.asarray(converted, dtype=float),
                evidence_relation=f"derived_from_{observed_id}",
                response_semantics="absolute_target",
                derivation={
                    **source.derivation,
                    "target_materialization": {
                        "observed_global_id": observed_id,
                        "target_global_id": source.target.source_global_id,
                        "steps": [first_trace, second_trace],
                    },
                },
            )
        )
    return materialized, diagnostics
