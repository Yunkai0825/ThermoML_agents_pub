"""Collect provenance-complete unary chemistry dependency pools.

The branch deliberately does not select one database-wide "best" value.
Reference priority depends on the mixture block that will consume the value,
so context-first selection and source-level statistics belong to baseline
evaluation. This stage only finds, validates, and records every admissible
unary source at the requested state window.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, replace
from typing import Any

from card_db_search_tools.basic_search_tools.advanced_block_search.catalogs import (
    PM_REGISTRY_DB,
    load_runtime_catalogs,
)
from NIST_ThermoML_agents.NIST_ThermoML_analysis_agent.ThermoML_core_calc_tools.mixture_nonideality_calc.composition_transforms import (
    detect_composition_basis,
)
from card_db_search_tools.basic_search_tools.normalization_helpers.db_helpers import (
    open_db,
)

from ..interface import CandidateRef, Diagnostic, NormalizedRequest
from .reader import AuthoritativeBlock, AuthoritativeBlockReader
from ..unit_conversion_lib.block_alignment import (
    align_authoritative_block_units,
)
from ..processing import (
    build_source_series,
    materialize_property_presentations,
)
from ..processing.relationships import (
    EVIDENCE_METADATA,
    materialize_target_evidence,
)
from ..unit_conversion_lib.property_response import (
    classify_presentation,
    presentation_requires_reference,
    reference_component_num_ids,
)
from ..runtime import JsonContentCache


@dataclass
class UnaryReferenceResult:
    reference_pool: dict[str, dict[str, list[dict[str, Any]]]]
    diagnostics: list[Diagnostic]
    cache_trace: dict[str, Any]


def required_unary_comp_num_ids(
    request: NormalizedRequest,
    blocks: list[AuthoritativeBlock],
) -> tuple[str, ...]:
    """Return only compounds whose requested chemistry needs unary data."""
    all_compounds = {
        comp_num_id
        for block in blocks
        for comp_num_id in block.candidate.comp_num_ids
    }
    required: set[str] = set()
    if any(
        target.basis != "real" or len(target.evidence_global_ids) > 1
        for target in request.targets
    ):
        required.update(all_compounds)

    translation = load_runtime_catalogs().translation.by_global_id
    evidence_ids = {
        global_id
        for target in request.targets
        for global_id in target.evidence_global_ids
    }
    for block in blocks:
        for global_id in block.candidate.declared_quantity_ids:
            row = translation.get(global_id)
            if row is not None and detect_composition_basis(
                row.quantity_key
            ) == "volume_fraction":
                required.update(block.candidate.comp_num_ids)
                break
        for declaration in block.projected.get("properties", []):
            if declaration.get("prop_num_id") not in evidence_ids:
                continue
            kind = classify_presentation(declaration.get("presentation"))
            if not presentation_requires_reference(kind):
                continue
            component_ids, _resolution = reference_component_num_ids(
                block.projected, declaration
            )
            required.update(component_ids)
    return tuple(sorted(required))


def _candidate_rows(
    comp_num_ids: tuple[str, ...],
    prop_num_ids: tuple[str, ...],
) -> list[CandidateRef]:
    if not comp_num_ids or not prop_num_ids:
        return []
    comp_placeholders = ",".join("?" for _ in comp_num_ids)
    prop_placeholders = ",".join("?" for _ in prop_num_ids)
    sql = (
        "SELECT * FROM block_registry br "
        "WHERE br.system_type='unary' "
        "AND EXISTS (SELECT 1 FROM json_each(br.comp_ids_smiles) c "
        f"WHERE json_extract(c.value,'$.comp_num_id') IN ({comp_placeholders})) "
        "AND EXISTS (SELECT 1 FROM json_each(br.prop_ids_meas_ranges) p "
        f"WHERE json_extract(p.value,'$.prop_num_id') IN ({prop_placeholders})) "
        "ORDER BY br.doi,br.block_number"
    )
    connection = open_db(str(PM_REGISTRY_DB))
    try:
        rows = connection.execute(
            sql, [*comp_num_ids, *prop_num_ids]
        ).fetchall()
    finally:
        connection.close()
    candidates = []
    for row in rows:
        compounds = json.loads(row["comp_ids_smiles"])
        ids = tuple(item["comp_num_id"] for item in compounds)
        candidates.append(
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
    return candidates


def _source_record(source) -> dict[str, Any]:
    point_ids = tuple(
        sorted(
            {
                point_id
                for group in source.point_ids
                for point_id in group
            }
        )
    )
    return {
        "value": float(source.values[0]),
        "unit": source.target.canonical_unit,
        "quality_score": float(source.quality_score),
        "source_key": source.source_key,
        "source": source.source_identity(),
        "BLKpoint_ids": list(point_ids),
        "n_observations": len(point_ids),
        "phase_num_id": source.phase_num_id,
        "phase_id": source.phase_id,
        "presentation": source.presentation,
        "presentation_kind": source.presentation_kind,
        "reported_unit": source.reported_unit,
        "response_semantics": source.response_semantics,
        "reference_semantics": dict(source.reference_semantics),
        "constraint_signature": [
            list(value) for value in source.constraint_signature
        ],
        "unit_alignment": source.derivation["unit_alignment"],
        "state_aggregation": (
            "constraint_and_composition_reliability_weighted_mean_of_"
            "surviving_points_within_the_confirmed_constraint_window"
        ),
    }


def _compute_reference_pool(
    request: NormalizedRequest,
    comp_num_ids: tuple[str, ...],
) -> tuple[
    dict[str, dict[str, list[dict[str, Any]]]],
    list[Diagnostic],
]:
    # Pure molar volume is always a composition-translation dependency
    # (volume-fraction axes may appear even when the ranked response is not
    # volumetric). It is also the common thermodynamic bridge for density,
    # amount density, specific volume, Vm, and excess Vm.
    template = request.targets[0]
    unary_by_id = {
        "GLOBprop_41": replace(
            template,
            input_value="GLOBprop_41; basis=real",
            quantity_key="molar_volume_m3_mol",
            preferred_name="Molar volume, m3/mol",
            canonical_unit="m3/mol",
            prop_num_id="GLOBprop_41",
            var_num_id=None,
            constr_num_id=None,
            source_role="property",
            source_global_id="GLOBprop_41",
            basis="real",
            component_comp_num_id=None,
            phase_num_id_filter=template.phase_num_id_filter,
            component=None,
            component_linked=False,
        )
    }
    for target in request.targets:
        for evidence_id in target.evidence_global_ids:
            if not evidence_id.startswith("GLOBprop_"):
                continue
            if evidence_id == target.source_global_id:
                unary_by_id[evidence_id] = replace(
                    target,
                    basis="real",
                    component_comp_num_id=None,
                    component=None,
                    component_linked=False,
                )
                continue
            metadata = EVIDENCE_METADATA[evidence_id]
            unary_by_id[evidence_id] = replace(
                template,
                input_value=f"{evidence_id}; basis=real",
                quantity_key=metadata["quantity_key"],
                preferred_name=metadata["preferred_name"],
                canonical_unit=metadata["canonical_unit"],
                prop_num_id=evidence_id,
                var_num_id=None,
                constr_num_id=None,
                source_role="property",
                source_global_id=evidence_id,
                basis="real",
                component_comp_num_id=None,
                component=None,
                component_linked=False,
            )
    unary_targets = list(unary_by_id.values())
    unary_request = replace(request, targets=tuple(unary_targets))
    prop_ids = tuple(
        sorted(
            {
                global_id
                for target in unary_request.targets
                for global_id in target.evidence_global_ids
                if global_id.startswith("GLOBprop_")
            }
        )
    )
    candidates = _candidate_rows(comp_num_ids, prop_ids)
    pool: dict[str, dict[str, list[dict[str, Any]]]] = {}
    diagnostics: list[Diagnostic] = []
    with AuthoritativeBlockReader() as reader:
        for candidate in candidates:
            try:
                block = align_authoritative_block_units(reader.read(candidate))
                source_series, source_diagnostics = build_source_series(
                    block, unary_request
                )
                diagnostics.extend(source_diagnostics)
                absolute_sources, presentation_diagnostics = (
                    materialize_property_presentations(source_series, {})
                )
                diagnostics.extend(presentation_diagnostics)
                materialized, _materialization_diagnostics = (
                    materialize_target_evidence(absolute_sources, {})
                )
                # Relationship bridges are opportunistic while building the
                # unary dependency pool. A direct requested unary property
                # remains valid when an additional derived representation
                # cannot be constructed from the same block. Consumers emit
                # a specific missing-reference diagnostic only if they later
                # require that absent representation.
                for source in materialized:
                    if len(source.comp_num_ids) != 1 or len(source.values) == 0:
                        continue
                    comp_num_id = source.comp_num_ids[0]
                    pool.setdefault(comp_num_id, {}).setdefault(
                        source.target.quantity_key, []
                    ).append(_source_record(source))
            except Exception as exc:
                diagnostics.append(
                    Diagnostic(
                        code="UNARY_REFERENCE_EXTRACTION_FAILED",
                        message=f"{type(exc).__name__}: {exc}",
                        stage="unary_reference",
                        severity="warning",
                        source_key=candidate.key,
                    )
                )
    for quantities in pool.values():
        for quantity_key, records in quantities.items():
            unique = {
                (
                    record["source_key"],
                    round(float(record["value"]), 15),
                ): record
                for record in records
            }
            quantities[quantity_key] = sorted(
                unique.values(), key=lambda item: item["source_key"]
            )
    return pool, diagnostics


def run_unary_reference_branch(
    request: NormalizedRequest,
    candidate_comp_num_ids: tuple[str, ...],
    *,
    database_fingerprint: dict[str, Any],
) -> UnaryReferenceResult:
    """Return admissible unary sources for the planned chemistry dependencies."""
    cache = JsonContentCache("unary_reference_pool")
    if not candidate_comp_num_ids:
        return UnaryReferenceResult(
            reference_pool={},
            diagnostics=[],
            cache_trace={
                "namespace": cache.namespace,
                "skipped": "no ranking or composition dependency needs unary data",
                "hits": 0,
                "misses": 0,
            },
        )
    payload = {
        "database": database_fingerprint["fingerprint_sha256"],
        "unary_reference_contract": (
            "absolute_direct_property_with_presentation_provenance_v1"
        ),
        "comp_num_ids": list(sorted(set(candidate_comp_num_ids))),
        "targets": [target.as_dict() for target in request.targets],
        "constraints": [
            constraint.as_dict() for constraint in request.constraints
        ],
    }
    computed_diagnostics: list[Diagnostic] = []

    def compute() -> dict[str, Any]:
        reference_pool, diagnostics = _compute_reference_pool(
            request, tuple(sorted(set(candidate_comp_num_ids)))
        )
        computed_diagnostics.extend(diagnostics)
        return {
            "reference_pool": reference_pool,
            "diagnostics": [item.as_dict() for item in diagnostics],
        }

    value, hit, key = cache.get_or_compute(payload, compute)
    if hit:
        diagnostics = [
            Diagnostic(
                code=item["code"],
                message=item["message"],
                stage=item["stage"],
                severity=item.get("severity", "notice"),
                source_key=item.get("source_key"),
                details=item.get("details", {}),
            )
            for item in value.get("diagnostics", [])
        ]
    else:
        diagnostics = computed_diagnostics
    reference_pool = value.get("reference_pool", {})
    if not isinstance(reference_pool, dict):
        raise TypeError("unary reference cache has invalid reference_pool")
    return UnaryReferenceResult(
        reference_pool=reference_pool,
        diagnostics=diagnostics,
        cache_trace={
            "namespace": cache.namespace,
            "key": key,
            "hits": int(hit),
            "misses": int(not hit),
        },
    )
