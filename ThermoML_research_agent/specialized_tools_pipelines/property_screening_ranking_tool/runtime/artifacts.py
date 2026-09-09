"""Write complete machine-readable artifacts behind one run manifest."""

from __future__ import annotations

import csv
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from ..interface import CandidateRef, Diagnostic, NormalizedRequest, SourceSeries
from .storage import new_run_directory, register_session_file


def _atomic_json(path: Path, value: Any) -> None:
    temp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    with temp.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temp, path)


def _atomic_text(path: Path, value: str) -> None:
    temp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    with temp.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(value)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temp, path)

def _jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> int:
    count = 0
    with path.open("x", encoding="utf-8") as handle:
        for row in rows:
            handle.write(
                json.dumps(
                    row,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                )
                + "\n"
            )
            count += 1
    return count


def _source_rows(sources: list[SourceSeries]) -> Iterable[dict[str, Any]]:
    for source in sources:
        yield {
            "source_key": source.source_key,
            "source": source.source_identity(),
            "system_type": source.system_type,
            "comp_num_ids": list(source.comp_num_ids),
            "compound_names": list(source.compound_names),
            "target": source.target.as_dict(),
            "target_local_id": source.target_local_id,
            "phase_num_id": source.phase_num_id,
            "phase_id": source.phase_id,
            "presentation": source.presentation,
            "presentation_kind": source.presentation_kind,
            "reported_unit": source.reported_unit,
            "response_semantics": source.response_semantics,
            "reference_semantics": source.reference_semantics,
            "coordinates": source.coordinates.tolist(),
            "values": source.values.tolist(),
            "point_ids": [list(value) for value in source.point_ids],
            "original_coordinate_basis": list(
                source.original_coordinate_basis
            ),
            "coordinate_comp_num_ids": list(
                source.coordinate_comp_num_ids
            ),
            "coordinate_constraint_proximity": (
                source.coordinate_constraint_proximity.tolist()
            ),
            "coordinate_composition_reliability": (
                source.coordinate_composition_reliability.tolist()
            ),
            "constraint_signature": [
                list(value) for value in source.constraint_signature
            ],
            "quality_score": source.quality_score,
            "derivation": source.derivation,
            "observed_global_id": source.observed_global_id,
            "observed_quantity_key": source.observed_quantity_key,
            "observed_canonical_unit": source.observed_canonical_unit,
            "evidence_relation": source.evidence_relation,
        }


def _ranking_csv(path: Path, rankings: list[dict[str, Any]]) -> None:
    fields = (
        "rank",
        "rank_within_group",
        "candidate_key",
        "system_signature",
        "system_type",
        "comp_num_ids",
        "compound_names",
        "target",
        "basis",
        "direction",
        "raw_value",
        "criterion_score",
        "overall_score",
        "quality_score",
        "selected_curve_id",
        "selection_score",
        "source_lit_num_id",
        "source_doi",
        "source_block_number",
        "source_BLKsubsys_id",
        "source_target_local_id",
    )
    with path.open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for ranking in rankings:
            for criterion in ranking["criteria"]:
                source = criterion["source"]
                target = criterion["target"]
                writer.writerow(
                    {
                        "rank": ranking["rank"],
                        "rank_within_group": ranking["rank_within_group"],
                        "candidate_key": ranking["candidate_key"],
                        "system_signature": ranking["system_signature"],
                        "system_type": ranking["system_type"],
                        "comp_num_ids": "|".join(ranking["comp_num_ids"]),
                        "compound_names": "|".join(
                            ranking["compound_names"]
                        ),
                        "target": target["quantity_key"],
                        "basis": target["basis"],
                        "direction": target["direction"],
                        "raw_value": criterion["raw_value"],
                        "criterion_score": criterion["score"],
                        "overall_score": ranking["overall_score"],
                        "quality_score": ranking["quality_score"],
                        "selected_curve_id": source.get(
                            "selected_curve_id"
                        ),
                        "selection_score": source.get("selection_score"),
                        "source_lit_num_id": source.get("lit_num_id"),
                        "source_doi": source.get("doi"),
                        "source_block_number": source.get("block_number"),
                        "source_BLKsubsys_id": source.get("BLKsubsys_id"),
                        "source_target_local_id": source.get(
                            "target_local_id"
                        ),
                    }
                )


def _secondary_ranking_csv(
    path: Path, panels: list[dict[str, Any]]
) -> None:
    fields = (
        "coordinate_sequence",
        "dimensions",
        "coordinate",
        "nearest_primary_coordinate",
        "distance_from_primary",
        "eligible_systems_at_coordinate",
        "rank",
        "rank_within_group",
        "candidate_key",
        "system_signature",
        "system_type",
        "comp_num_ids",
        "compound_names",
        "target",
        "basis",
        "direction",
        "raw_value",
        "criterion_score",
        "overall_score",
        "quality_score",
        "coordinate_comp_num_ids",
        "closure_comp_num_id",
        "selected_curve_id",
        "selection_score",
        "source_lit_num_id",
        "source_doi",
        "source_block_number",
        "source_BLKsubsys_id",
        "source_target_local_id",
    )
    with path.open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for panel in panels:
            for ranking in panel.get("rankings", []):
                for criterion in ranking.get("criteria", []):
                    source = criterion["source"]
                    target = criterion["target"]
                    writer.writerow(
                        {
                            "coordinate_sequence": panel["sequence"],
                            "dimensions": panel["dimensions"],
                            "coordinate": "|".join(
                                f"{value:.12g}"
                                for value in panel["coordinate"]
                            ),
                            "nearest_primary_coordinate": "|".join(
                                f"{value:.12g}"
                                for value in panel[
                                    "nearest_primary_coordinate"
                                ]
                            ),
                            "distance_from_primary": panel[
                                "distance_from_primary"
                            ],
                            "eligible_systems_at_coordinate": panel[
                                "eligible_systems"
                            ],
                            "rank": ranking["rank"],
                            "rank_within_group": ranking[
                                "rank_within_group"
                            ],
                            "candidate_key": ranking["candidate_key"],
                            "system_signature": ranking[
                                "system_signature"
                            ],
                            "system_type": ranking["system_type"],
                            "comp_num_ids": "|".join(
                                ranking["comp_num_ids"]
                            ),
                            "compound_names": "|".join(
                                ranking["compound_names"]
                            ),
                            "target": target["quantity_key"],
                            "basis": target["basis"],
                            "direction": target["direction"],
                            "raw_value": criterion["raw_value"],
                            "criterion_score": criterion["score"],
                            "overall_score": ranking["overall_score"],
                            "quality_score": ranking["quality_score"],
                            "coordinate_comp_num_ids": "|".join(
                                criterion["coordinate_comp_num_ids"]
                            ),
                            "closure_comp_num_id": criterion[
                                "closure_comp_num_id"
                            ],
                            "selected_curve_id": source.get(
                                "selected_curve_id"
                            ),
                            "selection_score": source.get(
                                "selection_score"
                            ),
                            "source_lit_num_id": source.get(
                                "lit_num_id"
                            ),
                            "source_doi": source.get("doi"),
                            "source_block_number": source.get(
                                "block_number"
                            ),
                            "source_BLKsubsys_id": source.get(
                                "BLKsubsys_id"
                            ),
                            "source_target_local_id": source.get(
                                "target_local_id"
                            ),
                        }
                    )


def _grid_csv(path: Path, rankings: list[dict[str, Any]]) -> None:
    fields = (
        "rank",
        "system_signature",
        "target",
        "basis",
        "grid_role",
        "available",
        "used_for_ranking",
        "coordinate_comp_num_ids",
        "composition",
        "full_composition",
        "coverage_failure_reason",
        "real_value",
        "ideal_value",
        "deviation",
        "absolute_deviation",
        "baseline_kind",
        "interpolation_kind",
        "BLKpoint_ids",
        "selected_curve_id",
        "selection_score",
        "source_lit_num_id",
        "source_doi",
        "source_block_number",
        "source_BLKsubsys_id",
        "source_target_local_id",
    )
    with path.open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()

        def write_point(
            *,
            ranking: dict[str, Any],
            criterion: dict[str, Any],
            point: dict[str, Any],
            grid_role: str,
            coordinate_comp_num_ids: list[str],
        ) -> None:
            target = criterion["target"]
            source = criterion["source"]
            writer.writerow(
                {
                    "rank": ranking["rank"],
                    "system_signature": ranking["system_signature"],
                    "target": target["quantity_key"],
                    "basis": target["basis"],
                    "grid_role": grid_role,
                    "available": point.get("available", True),
                    "used_for_ranking": point.get("used_for_ranking", False),
                    "coordinate_comp_num_ids": "|".join(
                        coordinate_comp_num_ids
                    ),
                    "composition": "|".join(
                        f"{value:.12g}"
                        for value in point.get("composition", [])
                    ),
                    "full_composition": "|".join(
                        f"{item['comp_num_id']}={item['mole_fraction']:.12g}"
                        for item in point.get("full_composition", [])
                    ),
                    "coverage_failure_reason": point.get(
                        "coverage_failure_reason"
                    ),
                    "real_value": point.get("real_value"),
                    "ideal_value": point.get("ideal_value"),
                    "deviation": point.get("deviation"),
                    "absolute_deviation": point.get(
                        "absolute_deviation"
                    ),
                    "baseline_kind": point.get("baseline_kind"),
                    "interpolation_kind": point.get(
                        "interpolation_kind"
                    ),
                    "BLKpoint_ids": "|".join(
                        point.get("source_point_ids", [])
                    ),
                    "selected_curve_id": source.get("selected_curve_id"),
                    "selection_score": source.get("selection_score"),
                    "source_lit_num_id": source.get("lit_num_id"),
                    "source_doi": source.get("doi"),
                    "source_block_number": source.get("block_number"),
                    "source_BLKsubsys_id": source.get("BLKsubsys_id"),
                    "source_target_local_id": source.get(
                        "target_local_id"
                    ),
                }
            )

        for ranking in rankings:
            for criterion in ranking["criteria"]:
                for point in criterion["ranking_grid_coverage"]["values"]:
                    write_point(
                        ranking=ranking,
                        criterion=criterion,
                        point=point,
                        grid_role="ranking_requested",
                        coordinate_comp_num_ids=[],
                    )
                profile = criterion.get("secondary_composition_grid")
                if isinstance(profile, dict):
                    for point in profile.get("values", []):
                        write_point(
                            ranking=ranking,
                            criterion=criterion,
                            point=point,
                            grid_role="secondary_composition_profile",
                            coordinate_comp_num_ids=profile.get(
                                "coordinate_comp_num_ids", []
                            ),
                        )


def _write_run_artifacts(
    *,
    request: NormalizedRequest,
    database_fingerprint: dict[str, Any],
    candidates: tuple[CandidateRef, ...],
    unit_alignment_report: list[dict[str, Any]],
    materialized_evidence_sources: list[SourceSeries],
    selected_property_curves: list[SourceSeries],
    unary_reference_pool: dict[
        str, dict[str, list[dict[str, Any]]]
    ],
    unary_reference_diagnostics: list[Diagnostic],
    composition_plans: dict[str, Any],
    property_curve_selection_report: list[dict[str, Any]],
    rankings: list[dict[str, Any]],
    secondary_grid_rankings: list[dict[str, Any]],
    diagnostics: list[Diagnostic],
    result_observer: dict[str, Any],
    cache_trace: dict[str, Any],
    stage_trace: list[dict[str, Any]],
) -> dict[str, Any]:
    """Publish a complete run and return its compact manifest reference."""
    run_dir, session = new_run_directory()
    artifacts: list[dict[str, Any]] = []

    def add(
        artifact_id: str,
        filename: str,
        media_type: str,
        description: str,
    ) -> Path:
        path = run_dir / filename
        artifacts.append(
            {
                "artifact_id": artifact_id,
                "filename": filename,
                "media_type": media_type,
                "description": description,
            }
        )
        return path

    request_path = add(
        "request",
        "request.json",
        "application/json",
        "Strict normalized tool request and resolved global IDs.",
    )
    _atomic_json(request_path, request.as_dict())
    fingerprint_path = add(
        "database-fingerprint",
        "database_fingerprint.json",
        "application/json",
        "Database and registry generation used by this run.",
    )
    _atomic_json(fingerprint_path, database_fingerprint)
    candidate_path = add(
        "candidate-registry",
        "candidate_registry.jsonl",
        "application/x-ndjson",
        "Every paginated coarse registry candidate; never final-limit truncated.",
    )
    _jsonl(candidate_path, (candidate.as_dict() for candidate in candidates))
    unit_alignment_path = add(
        "unit-alignment",
        "unit_alignment.json",
        "application/json",
        (
            "Per-block, per-field source-to-canonical unit transformations "
            "applied before unary and composition processing."
        ),
    )
    _atomic_json(unit_alignment_path, unit_alignment_report)
    sources_path = add(
        "materialized-evidence-sources",
        "materialized_evidence_sources.jsonl",
        "application/x-ndjson",
        "Source-local normalized observations with BLKpoint provenance.",
    )
    _jsonl(sources_path, _source_rows(materialized_evidence_sources))
    selected_curves_path = add(
        "selected-property-curves",
        "selected_property_curves.jsonl",
        "application/x-ndjson",
        (
            "The one selected complete experimental block curve for each "
            "chemical system, target, phase, and normalized constraint state."
        ),
    )
    _jsonl(
        selected_curves_path, _source_rows(selected_property_curves)
    )
    unary_path = add(
        "unary-reference-pool",
        "unary_reference_pool.json",
        "application/json",
        (
            "Every admissible unary property source at the confirmed state "
            "window, with point-level provenance for context-first baseline "
            "ensembles."
        ),
    )
    _atomic_json(unary_path, unary_reference_pool)
    unary_diagnostics_path = add(
        "unary-reference-diagnostics",
        "unary_reference_diagnostics.json",
        "application/json",
        (
            "Optional unary-source exclusions retained separately; a missing "
            "dependency becomes a user-facing diagnostic only when consumed."
        ),
    )
    _atomic_json(
        unary_diagnostics_path,
        [diagnostic.as_dict() for diagnostic in unary_reference_diagnostics],
    )
    composition_path = add(
        "composition-translation",
        "composition_translation.json",
        "application/json",
        "Composition-basis identities and deterministic conversion relations.",
    )
    _atomic_json(composition_path, composition_plans)
    selection_path = add(
        "property-curve-selection-report",
        "property_curve_selection_report.json",
        "application/json",
        (
            "Whole-curve composite scores, selected block identity, primary "
            "and regulated-grid coverage, secondary fallback identity, and "
            "every rejected alternative."
        ),
    )
    _atomic_json(selection_path, property_curve_selection_report)
    ranking_json = add(
        "ranking-results-json",
        "ranking_results.json",
        "application/json",
        "Full ranked systems and coherent real/baseline/deviation grids.",
    )
    _atomic_json(
        ranking_json,
        {
            "n_returned": len(rankings),
            "rankings": rankings,
            "secondary_grid_rankings": secondary_grid_rankings,
        },
    )
    ranking_csv = add(
        "ranking-results-csv",
        "ranking_results.csv",
        "text/csv",
        "One row per ranked system and criterion.",
    )
    _ranking_csv(ranking_csv, rankings)
    secondary_json = add(
        "secondary-grid-rankings-json",
        "secondary_grid_rankings.json",
        "application/json",
        (
            "Ordered independent cross-system rankings at regulated "
            "composition coordinates other than the primary query grid."
        ),
    )
    _atomic_json(
        secondary_json,
        {
            "n_coordinates": len(secondary_grid_rankings),
            "coordinates": secondary_grid_rankings,
        },
    )
    secondary_csv = add(
        "secondary-grid-rankings-csv",
        "secondary_grid_rankings.csv",
        "text/csv",
        (
            "One row per secondary coordinate, ranked system, and target "
            "criterion with selected-curve provenance."
        ),
    )
    _secondary_ranking_csv(secondary_csv, secondary_grid_rankings)
    grid_csv = add(
        "ranking-grid-csv",
        "ranking_grid_values.csv",
        "text/csv",
        "Ranking coordinates and regulated multidimensional composition profiles with coverage reasons.",
    )
    _grid_csv(grid_csv, rankings)
    diagnostics_path = add(
        "diagnostics",
        "diagnostics.json",
        "application/json",
        "Complete exclusions, edge cases, and stage notices.",
    )
    _atomic_json(
        diagnostics_path, [diagnostic.as_dict() for diagnostic in diagnostics]
    )
    observer_path = add(
        "result-observer",
        "result_observer.json",
        "application/json",
        (
            "Read-only ReAct quality assessment, chemistry insights, "
            "deterministic quality snapshot, and observer execution metadata."
        ),
    )
    _atomic_json(observer_path, result_observer)
    cache_path = add(
        "cache-trace",
        "cache_trace.json",
        "application/json",
        (
            "Independent unary-reference-pool and composition-translation "
            "cache trace."
        ),
    )
    _atomic_json(cache_path, cache_trace)
    stage_path = add(
        "stage-trace",
        "stage_trace.json",
        "application/json",
        "Counts and elapsed times at every workflow stage.",
    )
    _atomic_json(stage_path, stage_trace)

    manifest = {
        "run_id": run_dir.name,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": (
            "success"
            if rankings
            else "secondary_context_only"
            if any(
                panel.get("returned_systems")
                for panel in secondary_grid_rankings
            )
            else "no_results"
        ),
        "run_directory": str(run_dir),
        "request_summary": {
            "center_comp_num_ids": list(request.center_comp_num_ids),
            "targets": [
                target.quantity_key for target in request.targets
            ],
            "system_scope": request.system_scope,
            "system_type": request.system_type,
            "limit": request.limit,
        },
        "counts": {
            "registry_candidates": len(candidates),
            "materialized_evidence_sources": len(
                materialized_evidence_sources
            ),
            "selected_property_curves": len(selected_property_curves),
            "rankings_returned": len(rankings),
            "secondary_grid_coordinates": len(
                secondary_grid_rankings
            ),
            "secondary_grid_returned_occurrences": sum(
                int(panel.get("returned_systems", 0))
                for panel in secondary_grid_rankings
            ),
            "diagnostics": len(diagnostics),
        },
        "artifacts": artifacts,
    }
    manifest_path = run_dir / "run_manifest.json"
    _atomic_json(manifest_path, manifest)
    manifest_artifact = {
        "artifact_id": "run-manifest",
        "filename": "run_manifest.json",
        "media_type": "application/json",
        "description": "Authoritative browser and downstream artifact contract.",
    }
    manifest["artifacts"].append(manifest_artifact)
    _atomic_json(manifest_path, manifest)

    if session is not None:
        for artifact in manifest["artifacts"]:
            session.register_file(
                "property_screening",
                run_dir / artifact["filename"],
                artifact["description"],
            )
    return {
        "run_id": run_dir.name,
        "run_directory": str(run_dir),
        "run_manifest": str(manifest_path),
        "artifacts": manifest["artifacts"],
        "session_registered": session is not None,
    }


def write_run_artifacts(
    *,
    stage_trace: list[dict[str, Any]],
    run_summary: dict[str, int] | None = None,
    **kwargs,
) -> dict:
    """Publish and then finalize self-referential trace/manifest metadata."""
    started = time.perf_counter()
    result = _write_run_artifacts(stage_trace=stage_trace, **kwargs)
    completed = {
        "stage": "stage_16_artifact_publication",
        "status": "completed",
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    run_dir = Path(result["run_directory"])
    _atomic_json(run_dir / "stage_trace.json", [*stage_trace, completed])

    request = kwargs["request"]
    manifest_path = Path(result["run_manifest"])
    with manifest_path.open("r", encoding="utf-8") as handle:
        manifest = json.load(handle)
    manifest["request_summary"].update(
        {
            "constraints": [
                constraint.quantity_key
                for constraint in request.constraints
            ],
            "purpose": request.purpose,
            "tasks": list(request.tasks),
        }
    )
    if run_summary is not None:
        manifest["counts"] = dict(run_summary)
    _atomic_json(manifest_path, manifest)
    return result

def publish_agent_markdown(
    artifact_result: dict[str, Any], markdown: str
) -> dict[str, Any]:
    """Publish the exact bounded Markdown returned to the Query agent."""
    run_dir = Path(artifact_result["run_directory"])
    manifest_path = Path(artifact_result["run_manifest"])
    output_path = run_dir / "agent_result.md"
    _atomic_text(output_path, markdown)

    with manifest_path.open("r", encoding="utf-8") as handle:
        manifest = json.load(handle)
    artifact = {
        "artifact_id": "agent-result-markdown",
        "filename": output_path.name,
        "media_type": "text/markdown",
        "description": (
            "Exact bounded Markdown view supplied to the Query agent."
        ),
    }
    existing = {
        item.get("artifact_id") for item in manifest.get("artifacts", [])
    }
    if artifact["artifact_id"] in existing:
        raise ValueError("agent Markdown artifact is already published")
    manifest.setdefault("artifacts", []).append(artifact)
    _atomic_json(manifest_path, manifest)
    registered = register_session_file(
        "property_screening", output_path, artifact["description"]
    )

    result = dict(artifact_result)
    result["artifacts"] = manifest["artifacts"]
    result["agent_markdown"] = str(output_path)
    result["session_registered"] = bool(
        artifact_result.get("session_registered") or registered
    )
    return result

__all__ = ["publish_agent_markdown", "write_run_artifacts"]
