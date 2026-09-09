"""Public orchestrator for the ThermoML property-screening stage DAG."""

from __future__ import annotations

import time
from typing import Any, Callable

from .interface import Diagnostic, review_request
from .interface.agent import compact_screen_property_systems
from .interface.result_observer import (
    build_quality_snapshot,
    observe_screening_result,
)
from .processing import (
    apply_baselines,
    interpolate_sources,
    materialize_property_presentations,
    materialize_target_evidence,
    rank_criteria,
    select_property_curves,
    validate_harmonized_sources,
    validate_materialized_target_sources,
    validate_ranking_output,
)
from .runtime import (
    publish_agent_markdown,
    write_run_artifacts,
)
from .sources import discover_candidates, gather_authoritative_blocks
from .sources.composition import run_composition_branch
from .sources.unary import (
    required_unary_comp_num_ids,
    run_unary_reference_branch,
)
from .unit_conversion_lib.block_alignment import align_gathered_block_units


def _timed_stage(
    trace: list[dict[str, Any]],
    name: str,
    function: Callable[[], Any],
) -> Any:
    started = time.perf_counter()
    try:
        result = function()
    except Exception:
        trace.append(
            {
                "stage": name,
                "status": "failed",
                "elapsed_seconds": round(
                    time.perf_counter() - started, 6
                ),
            }
        )
        raise
    trace.append(
        {
            "stage": name,
            "status": "completed",
            "elapsed_seconds": round(time.perf_counter() - started, 6),
        }
    )
    return result


def _observe_result_nonfatal(result: dict[str, Any]) -> dict[str, Any]:
    """Run the bounded observer; its failure never voids the ranking result."""
    try:
        return observe_screening_result(result)
    except Exception as exc:  # noqa: BLE001 — commentary must not kill data
        try:
            snapshot = build_quality_snapshot(result)
        except Exception:  # noqa: BLE001
            snapshot = {}
        reason = f"{type(exc).__name__}: {exc}"
        return {
            "role": "non_authoritative_post_ranking_result_observer",
            "authoritative_result_unchanged": True,
            "quality_snapshot": snapshot,
            "assessment": {
                "quality_verdict": "unavailable",
                "tool_quality_comment": (
                    "The bounded read-only result observer failed "
                    f"({reason}); deterministic ranks, values, selected "
                    "curves, and diagnostics remain authoritative."
                ),
                "strengths": [],
                "limitations": [
                    f"Automatic result review unavailable: {reason}"
                ],
                "chemistry_insights": [],
                "recommended_follow_up": [],
            },
            "execution": {
                "agent_type": "bounded_read_only_react",
                "status": "observer_unavailable",
                "error": reason,
            },
        }


def screen_property_systems(
    ranking_targets: str | list[str],
    target_constraints: str | list[str],
    center_comp_num_ids: str | list[str],
    purpose: str,
    tasks: str,
    system_type: str | None = None,
    system_scope: str = "declared",
    comparison_grid: str | list[str] = "auto",
    limit: int = 20,
    confirmation_token: str | None = None,
) -> dict:
    """Screen and rank ThermoML systems on chemically comparable data.

    Public input is flat
    --------------------
    Every plural argument accepts one string or one flat ``list[str]``.
    Nested dictionaries are rejected.

    A ranking target has the form::

        QUANTITY; basis=real; direction=maximize; at_mole_fraction=0.5; aggregate=mean

    ``QUANTITY`` must be a typed GLOBprop_N/GLOBvar_N/GLOBconstr_N ID.
    ``basis`` is real, ideal, deviation, or absolute_deviation.
    ``at_mole_fraction`` contains independent mole-fraction coordinates.
    ``aggregate`` is mean, maximum, minimum, or integral.
    Component-linked templates require ``component=GLOBcomp_N``; optional
    ``phase=GLOBphase_N`` disambiguates repeated phase occurrences.

    A state constraint has either form::

        GLOBvar_1 = 298.15 K ± 0.5 K
        GLOBconstr_18 BETWEEN 95 kPa AND 105 kPa; tol=0.1 kPa; component=GLOBcomp_1

    Component/phase suffixes use the same flat form::

        GLOBconstr_5 = 20 %; component=GLOBcomp_1; phase=GLOBphase_3

    At least one target, constraint, and GLOBcomp_N center ID is required.
    ``center_comp_num_ids`` lists ONLY the compound(s) shared by every
    compared system — the fixed chemistry axis (for example water when
    ranking aqueous binaries). Every candidate system must contain ALL
    center compounds; the ranked alternatives are the remaining
    components and must NOT be listed here.

    Confirmation gate
    -----------------
    The deterministic ID, unit, value, tolerance, operation, default, and
    compound-metadata enrichment gate is walked automatically inside the
    tool: a parseable call is enriched, content-address confirmed against
    the current registry/database/settings state, and executed in one call.
    Invalid inputs return a ``correction_required`` review with actionable
    issues and never touch the data databases. The ``confirmation_token``
    parameter is retained for compatibility but is no longer required.

    Chemistry and scope
    -------------------
    ``system_scope='declared'`` is the default. ``subsystem`` and ``either``
    explicitly opt into searchable BLKsubsys views. Composition is normalized
    to mole fraction only from exact evidence: reported fractions,
    formula-mass conversion, multisolute molality with an explicit solvent,
    exact ratios, or dimensionally complete density/volume bridges. Required
    formula masses and phase-compatible unary molar-volume ensembles are
    resolved deterministically and retained as evidence; missing bridges are
    diagnosed rather than guessed.

    Each experimental property curve is scored as a complete block-local
    object. Exactly one curve is selected per compatible
    system/property/state group before strict source-local interpolation;
    independent blocks are never averaged pointwise. The selected DOI,
    block, subsystem, local property, score, and rejected alternatives remain
    documented. Unary values are separate reference ensembles: a same-block
    pure endpoint is preferred, otherwise compatible same-DOI unary sources
    are averaged, and only then are compatible global unary sources averaged.
    A real ranking never requires pure endpoints. Ideal/deviation requests use
    explicit property policies.

    Output
    ------
    Compact JSON identifies each selected experimental curve with paired DOI
    + GLOBlit_N and block/local IDs. Complete discovery, raw-point provenance,
    curve-selection scores and alternatives, transformations, grids,
    diagnostics, caches, and rankings are published under one run manifest.
    The requested composition remains the authoritative primary ranking.
    Other regulated coordinates are independently ranked in deterministic
    target-distance order as bounded secondary context; they never substitute
    values into the primary comparison.
    ``limit`` is applied only after complete deterministic ranking.
    """
    review = review_request(
        ranking_targets=ranking_targets,
        target_constraints=target_constraints,
        center_comp_num_ids=center_comp_num_ids,
        purpose=purpose,
        tasks=tasks,
        system_type=system_type,
        system_scope=system_scope,
        comparison_grid=comparison_grid,
        limit=limit,
        confirmation_token=confirmation_token,
    )
    if (
        review.review["status"] == "confirmation_required"
        and review.request is not None
    ):
        # Automatic framework confirmation: the enriched request and database
        # fingerprint were derived in-process this instant, so the tool — not
        # the calling agent — resubmits with the content-addressed token.
        review = review_request(
            ranking_targets=ranking_targets,
            target_constraints=target_constraints,
            center_comp_num_ids=center_comp_num_ids,
            purpose=purpose,
            tasks=tasks,
            system_type=system_type,
            system_scope=system_scope,
            comparison_grid=comparison_grid,
            limit=limit,
            confirmation_token=review.review["confirmation"]["token"],
        )
    if review.review["status"] != "confirmed":
        return review.review
    if review.request is None or review.database_fingerprint is None:
        raise AssertionError("confirmed request lacks immutable execution state")
    request = review.request

    stage_trace: list[dict[str, Any]] = []
    diagnostics: list[Diagnostic] = []
    fingerprint = _timed_stage(
        stage_trace,
        "stage_0_database_fingerprint",
        lambda: review.database_fingerprint,
    )
    discovery = _timed_stage(
        stage_trace,
        "stage_1_candidate_discovery",
        lambda: discover_candidates(request),
    )
    if not discovery.candidates:
        diagnostics.append(
            Diagnostic(
                code="NO_REGISTRY_RANGE_OVERLAP",
                message=(
                    "No registry block contains every requested identity "
                    "and overlaps every converted effective state window."
                ),
                stage="candidate_discovery",
                details={
                    "constraints": [
                        constraint.as_dict()
                        for constraint in request.constraints
                    ]
                },
            )
        )
    gathering = _timed_stage(
        stage_trace,
        "stage_2_authoritative_block_gathering",
        lambda: gather_authoritative_blocks(discovery.candidates),
    )
    diagnostics.extend(gathering.diagnostics)
    unit_alignment = _timed_stage(
        stage_trace,
        "stage_3_gathered_block_unit_alignment",
        lambda: align_gathered_block_units(gathering.blocks),
    )
    diagnostics.extend(unit_alignment.diagnostics)
    unary_comp_ids = required_unary_comp_num_ids(
        request, unit_alignment.blocks
    )

    unary = _timed_stage(
        stage_trace,
        "stage_4_unary_dependency_pool",
        lambda: run_unary_reference_branch(
            request,
            unary_comp_ids,
            database_fingerprint=fingerprint,
        ),
    )
    composition = _timed_stage(
        stage_trace,
        "stage_5_source_extraction_and_composition_translation",
        lambda: run_composition_branch(
            request,
            unit_alignment.blocks,
            unary_reference_pool=unary.reference_pool,
            database_fingerprint=fingerprint,
        ),
    )
    # Unary discovery is a dependency pool, not a candidate gate. Individual
    # rejected unary blocks are therefore not user-facing failures. A
    # composition conversion or baseline that actually needs a missing pool
    # entry emits the relevant, system-specific diagnostic at its consumption
    # stage instead of flooding a valid real-basis screen with optional-source
    # notices.
    diagnostics.extend(composition.diagnostics)

    harmonized_sources = _timed_stage(
        stage_trace,
        "stage_6_normalized_source_validation_barrier",
        lambda: validate_harmonized_sources(composition.series),
    )
    absolute_observed_sources, presentation_diagnostics = _timed_stage(
        stage_trace,
        "stage_7_reference_presentation_materialization",
        lambda: materialize_property_presentations(
            harmonized_sources, unary.reference_pool
        ),
    )
    diagnostics.extend(presentation_diagnostics)
    materialized_sources, materialization_diagnostics = _timed_stage(
        stage_trace,
        "stage_8_target_evidence_materialization",
        lambda: materialize_target_evidence(
            absolute_observed_sources, unary.reference_pool
        ),
    )
    diagnostics.extend(materialization_diagnostics)
    validated_target_sources = _timed_stage(
        stage_trace,
        "stage_9_absolute_target_semantic_barrier",
        lambda: validate_materialized_target_sources(
            materialized_sources
        ),
    )
    property_curve_selection = _timed_stage(
        stage_trace,
        "stage_10_whole_curve_property_block_selection",
        lambda: select_property_curves(validated_target_sources, request),
    )
    diagnostics.extend(property_curve_selection.diagnostics)
    interpolated_selected, interpolation_diagnostics = _timed_stage(
        stage_trace,
        "stage_11_selected_source_strict_linear_interpolation",
        lambda: interpolate_sources(property_curve_selection.sources, request),
    )
    diagnostics.extend(interpolation_diagnostics)
    baselined, baseline_diagnostics = _timed_stage(
        stage_trace,
        "stage_12_coherent_basis_evaluation",
        lambda: apply_baselines(
            interpolated_selected, unary.reference_pool
        ),
    )
    diagnostics.extend(baseline_diagnostics)
    ranking = _timed_stage(
        stage_trace,
        "stage_13_cross_system_deterministic_ranking",
        lambda: rank_criteria(baselined, request),
    )
    diagnostics.extend(ranking.diagnostics)
    semantic_gate = _timed_stage(
        stage_trace,
        "stage_14_final_result_semantic_barrier",
        lambda: validate_ranking_output(
            ranking.rankings, ranking.secondary_grid_rankings
        ),
    )

    unary_reference_sources = sum(
        len(records)
        for quantities in unary.reference_pool.values()
        for records in quantities.values()
    )
    summary = {
        "registry_candidates": len(discovery.candidates),
        "declared_candidates": discovery.declared_count,
        "subsystem_candidates": discovery.subsystem_count,
        "registry_pages_read": discovery.pages_read,
        "authoritative_blocks_gathered": len(gathering.blocks),
        "unit_aligned_blocks": len(unit_alignment.blocks),
        "unit_aligned_fields": sum(
            len(block.unit_alignment) for block in unit_alignment.blocks
        ),
        "normalized_evidence_sources": len(composition.series),
        "absolute_observed_sources": len(absolute_observed_sources),
        "reference_presentations_materialized": sum(
            source.presentation_kind != "direct"
            for source in absolute_observed_sources
        ),
        "reference_presentations_rejected": len(
            presentation_diagnostics
        ),
        "materialized_target_sources": len(materialized_sources),
        "semantic_gate": semantic_gate,
        "property_curve_candidates": (
            property_curve_selection.n_candidate_curves
        ),
        "selected_property_curves": (
            property_curve_selection.n_selected_curves
        ),
        "secondary_fallback_property_curves": (
            property_curve_selection.n_secondary_fallback_curves
        ),
        "rejected_property_curves": (
            property_curve_selection.n_rejected_curves
        ),
        "interpolated_selected_curves": len(interpolated_selected),
        "eligible_systems": ranking.n_eligible_candidates,
        "incomplete_systems": ranking.n_incomplete_candidates,
        "returned_systems": len(ranking.rankings),
        "secondary_grid_coordinates": len(
            ranking.secondary_grid_rankings
        ),
        "secondary_grid_coordinates_with_results": sum(
            bool(panel["returned_systems"])
            for panel in ranking.secondary_grid_rankings
        ),
        "secondary_grid_candidate_occurrences": (
            ranking.n_secondary_candidate_occurrences
        ),
        "secondary_grid_returned_occurrences": (
            ranking.n_secondary_returned_occurrences
        ),
        "unary_reference_compounds": len(unary.reference_pool),
        "unary_reference_sources": unary_reference_sources,
        "unary_pool_rejections": len(unary.diagnostics),
        "diagnostics": len(diagnostics),
    }
    composition_plans = {
        source.source_key: {
            "source": source.source_identity(),
            "derivation": source.derivation,
            "coordinate_comp_num_ids": list(
                source.coordinate_comp_num_ids
            ),
            "original_coordinate_basis": list(
                source.original_coordinate_basis
            ),
        }
        for source in composition.series
    }
    cache_trace = {
        "unary_reference_pool": unary.cache_trace,
        "composition_translation": composition.cache_trace,
    }
    has_secondary_results = any(
        panel["returned_systems"] for panel in ranking.secondary_grid_rankings
    )
    result = {
        "status": (
            "success"
            if ranking.rankings
            else "secondary_context_only"
            if has_secondary_results
            else "no_results"
        ),
        "executed": True,
        "request_confirmation": {
            "status": "confirmed",
            "token": review.review["confirmation"]["token"],
            "request_sha256": review.review["fingerprints"][
                "request_sha256"
            ],
        },
        "summary": summary,
        "request": request.as_dict(),
        "rankings": ranking.rankings,
        "secondary_grid_rankings": ranking.secondary_grid_rankings,
        "diagnostics": [
            item.as_dict() for item in diagnostics[:50]
        ],
        "diagnostics_truncated_in_result": len(diagnostics) > 50,
        "cache_trace": cache_trace,
        "stage_trace": stage_trace,
    }
    result_observer = _timed_stage(
        stage_trace,
        "stage_15_read_only_result_observer",
        lambda: _observe_result_nonfatal(result),
    )
    result["result_observer"] = result_observer

    artifacts = _timed_stage(
        stage_trace,
        "stage_16_artifact_publication",
        lambda: write_run_artifacts(
            request=request,
            database_fingerprint=fingerprint,
            candidates=discovery.candidates,
            unit_alignment_report=unit_alignment.report,
            materialized_evidence_sources=validated_target_sources,
            selected_property_curves=property_curve_selection.sources,
            unary_reference_pool=unary.reference_pool,
            unary_reference_diagnostics=unary.diagnostics,
            composition_plans=composition_plans,
            property_curve_selection_report=(
                property_curve_selection.report
            ),
            rankings=ranking.rankings,
            secondary_grid_rankings=ranking.secondary_grid_rankings,
            diagnostics=diagnostics,
            cache_trace=cache_trace,
            stage_trace=stage_trace,
            run_summary=summary,
            result_observer=result_observer,
        ),
    )
    result["artifacts"] = artifacts
    result["artifacts"] = publish_agent_markdown(
        artifacts, compact_screen_property_systems(result)
    )
    return result
