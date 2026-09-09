"""Read-only ReAct observer for completed deterministic screening results.

The observer runs after ranking and before artifact publication.  It can query
only an immutable in-memory result bundle through three deterministic tools.
It cannot search ThermoML, select evidence, interpolate, calculate a baseline,
or alter scores/ranks.  Its sole product is structured quality commentary and
chemistry insight with validated references back to returned systems/targets.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from contextlib import contextmanager
from statistics import fmean
from typing import Any, Callable, Iterator

from NIST_ThermoML_agents.NIST_ThermoML_query_agent.query_agent_argo_engine.argo_client import (
    QueryClient,
)
from NIST_ThermoML_agents.general_db_query_engine.general_argo_engine_helpers import (
    agent_turn,
)
from NIST_ThermoML_agents.general_db_query_engine.general_argo_engine_helpers.json_answer_guard import (
    guard_json_answer,
)
from NIST_ThermoML_agents.general_db_query_engine.general_hooks_management_helpers.general_context_hooks.stats_references_tracking_hooks import (
    StatsRecorder,
    clear_active_recorder,
    get_active_recorder,
    set_active_recorder,
)
from NIST_ThermoML_agents.general_db_query_engine.general_subagent_skill_schema_and_parser.subworkflow_md_tool_descriptions import (
    build_tool_instructions,
)

from ..tool_settings import (
    RESULT_OBSERVER_MAX_CHEMISTRY_INSIGHTS,
    RESULT_OBSERVER_MAX_COMPARISON_RANKS,
    RESULT_OBSERVER_MAX_FOLLOW_UPS,
    RESULT_OBSERVER_MAX_ITERATIONS,
    RESULT_OBSERVER_MAX_LIMITATIONS,
    RESULT_OBSERVER_MAX_RANKINGS_PER_INSPECTION,
    RESULT_OBSERVER_MAX_SECONDS,
    RESULT_OBSERVER_MAX_STRENGTHS,
    RESULT_OBSERVER_MAX_TOKENS,
    RESULT_OBSERVER_TOP_RANKINGS_IN_QUALITY_SNAPSHOT,
)


_QUALITY_VERDICTS = {"high", "moderate", "low", "insufficient"}
_INSIGHT_CONFIDENCE = {"high", "medium", "low"}


def _authoritative_result_sha256(result: dict[str, Any]) -> str:
    payload = json.dumps(
        result,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        default=str,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


@contextmanager
def _observer_stats_scope() -> Iterator[str]:
    """Reuse parent tracking or own a bounded standalone tracking scope."""
    try:
        get_active_recorder()
    except RuntimeError:
        recorder = StatsRecorder()
        recorder.start_run("property-screening-result-observer")
        set_active_recorder(recorder)
        try:
            yield "standalone_observer"
        finally:
            recorder.reset()
            clear_active_recorder()
        return
    yield "parent_agent"

_ASSESSMENT_SCHEMA_EXAMPLE = {
    "quality_verdict": "moderate",
    "tool_quality_comment": (
        "The returned ranking is usable, but incomplete-system exclusions "
        "limit its scope."
    ),
    "strengths": [
        "Every returned criterion retains a paired DOI and lit_num_id."
    ],
    "limitations": [
        "Some discovered systems did not support the complete target set."
    ],
    "chemistry_insights": [
        {
            "statement": (
                "The first-ranked returned system has the largest measured "
                "value within its comparable ranking group."
            ),
            "supporting_candidate_keys": ["GLOBcomp_1::GLOBcomp_2"],
            "supporting_target_ids": ["GLOBprop_1"],
            "confidence": "medium",
        }
    ],
    "recommended_follow_up": [
        "Inspect the full regulated composition profiles before generalizing."
    ],
}

_SYSTEM_PROMPT = """
You are the read-only result-observer agent inside the ThermoML property
screening tool.  The scientific pipeline has already completed deterministically.
You assess the quality of that returned result and state concise chemistry
insights supported by it.

Mandatory behavior:
1. Call `inspect_return_quality` before answering.  Use
   `inspect_ranked_results` or `compare_ranked_systems` when the quality
   snapshot is insufficient for a statement.
2. Treat ranks, values, selected curves, provenance, diagnostics, and coverage
   as immutable.  Never propose edits to the completed result.
3. Do not search databases, invent mechanisms, infer missing endpoints, perform
   arithmetic mentally, or create a new numerical result.  Use the comparison
   tool for numerical differences.
4. Distinguish evidence quality from chemistry interpretation.  Mention scope,
   comparability, coverage, incomplete systems, provenance, and diagnostics in
   the quality comment.
5. Chemistry insights must be observations supported directly by returned
   rankings.  Preserve conditions and ranking-group limitations.  Reference
   only candidate keys and global target IDs returned by the tools.
6. If no systems were ranked, use quality_verdict `insufficient`, emit no
   chemistry insights, and explain the limiting diagnostics.

Return exactly one JSON object matching the required schema.  Do not return
Markdown, prose outside JSON, tool calls in the final answer, or additional
fields.
""".strip()


def _as_nonnegative_int(value: Any) -> int:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return 0
    return max(0, int(value))


def _same_ranking_group(left: dict[str, Any], right: dict[str, Any]) -> bool:
    return left.get("ranking_group") == right.get("ranking_group")


def _source_summary(source: dict[str, Any]) -> dict[str, Any]:
    return {
        "doi": source.get("doi"),
        "lit_num_id": source.get("lit_num_id"),
        "block_number": source.get("block_number"),
        "BLKsubsys_id": source.get("BLKsubsys_id"),
        "target_local_id": source.get("target_local_id"),
        "selected_curve_id": source.get("selected_curve_id"),
        "selection_score": source.get("selection_score"),
    }


def _criterion_summary(criterion: dict[str, Any]) -> dict[str, Any]:
    target = criterion.get("target", {})
    coverage = criterion.get("ranking_grid_coverage", {})
    secondary = criterion.get("secondary_composition_grid")
    return {
        "target_global_id": target.get("source_global_id"),
        "target_name": target.get("preferred_name"),
        "canonical_unit": target.get("canonical_unit"),
        "basis": target.get("basis"),
        "direction": target.get("direction"),
        "aggregate": target.get("aggregate"),
        "at_mole_fraction": target.get("at_mole_fraction"),
        "raw_value": criterion.get("raw_value"),
        "normalized_score": criterion.get("score"),
        "evidence_quality_score": criterion.get("quality_score"),
        "primary_grid_coverage": {
            "requested": coverage.get("requested", 0),
            "interpolated": coverage.get("interpolated", 0),
            "used_for_ranking": coverage.get("used_for_ranking", 0),
            "unavailable": coverage.get("unavailable", 0),
            "unavailable_by_reason": coverage.get(
                "unavailable_by_reason", {}
            ),
        },
        "secondary_grid_coverage": (
            secondary.get("coverage")
            if isinstance(secondary, dict)
            else None
        ),
        "baseline_message": criterion.get("baseline_message"),
        "source": _source_summary(criterion.get("source", {})),
    }


def _ranking_summary(ranking: dict[str, Any]) -> dict[str, Any]:
    return {
        "rank": ranking.get("rank"),
        "rank_within_group": ranking.get("rank_within_group"),
        "candidate_key": ranking.get("candidate_key"),
        "system_signature": ranking.get("system_signature"),
        "system_type": ranking.get("system_type"),
        "comp_num_ids": ranking.get("comp_num_ids", []),
        "compound_names": ranking.get("compound_names", []),
        "phase_num_id": ranking.get("phase_num_id"),
        "phase_id": ranking.get("phase_id"),
        "overall_score": ranking.get("overall_score"),
        "evidence_quality_score": ranking.get("quality_score"),
        "ranking_group": ranking.get("ranking_group", {}),
        "criteria": [
            _criterion_summary(criterion)
            for criterion in ranking.get("criteria", [])
        ],
    }


def build_quality_snapshot(result: dict[str, Any]) -> dict[str, Any]:
    """Calculate deterministic result-quality metadata for the observer."""
    if not isinstance(result, dict):
        raise TypeError("result observer input must be an object")
    summary = result.get("summary")
    rankings = result.get("rankings")
    secondary_panels = result.get("secondary_grid_rankings")
    diagnostics = result.get("diagnostics")
    stage_trace = result.get("stage_trace")
    if (
        not isinstance(summary, dict)
        or not isinstance(rankings, list)
        or not isinstance(secondary_panels, list)
    ):
        raise TypeError("result observer input lacks summary/rankings")
    if not isinstance(diagnostics, list) or not isinstance(stage_trace, list):
        raise TypeError("result observer input lacks diagnostics/stage_trace")

    primary_requested = primary_interpolated = primary_used = 0
    secondary_requested = secondary_available = 0
    source_count = complete_source_identity_count = 0
    criteria_count = 0
    for ranking in rankings:
        for criterion in ranking.get("criteria", []):
            criteria_count += 1
            coverage = criterion.get("ranking_grid_coverage", {})
            primary_requested += _as_nonnegative_int(coverage.get("requested"))
            primary_interpolated += _as_nonnegative_int(
                coverage.get("interpolated")
            )
            primary_used += _as_nonnegative_int(
                coverage.get("used_for_ranking")
            )
            secondary = criterion.get("secondary_composition_grid")
            if isinstance(secondary, dict):
                secondary_coverage = secondary.get("coverage", {})
                secondary_requested += _as_nonnegative_int(
                    secondary_coverage.get("requested")
                )
                secondary_available += _as_nonnegative_int(
                    secondary_coverage.get("available")
                )
            source = criterion.get("source", {})
            source_count += 1
            required = (
                source.get("doi"),
                source.get("lit_num_id"),
                source.get("block_number"),
                source.get("target_local_id"),
                source.get("selected_curve_id"),
            )
            complete_source_identity_count += int(all(required))

    severity_counts = Counter(
        str(item.get("severity", "notice"))
        for item in diagnostics
        if isinstance(item, dict)
    )
    diagnostic_codes = Counter(
        str(item.get("code", "UNKNOWN"))
        for item in diagnostics
        if isinstance(item, dict)
    )
    stage_statuses = Counter(
        str(item.get("status", "unknown"))
        for item in stage_trace
        if isinstance(item, dict)
    )
    overall_scores = [
        float(row["overall_score"])
        for row in rankings
        if isinstance(row.get("overall_score"), (int, float))
        and not isinstance(row.get("overall_score"), bool)
    ]
    quality_scores = [
        float(row["quality_score"])
        for row in rankings
        if isinstance(row.get("quality_score"), (int, float))
        and not isinstance(row.get("quality_score"), bool)
    ]
    ranking_groups = {
        json.dumps(
            row.get("ranking_group", {}), sort_keys=True, default=str
        )
        for row in rankings
    }
    exact_score_ties = 0
    for index, left in enumerate(rankings):
        for right in rankings[index + 1 :]:
            if (
                _same_ranking_group(left, right)
                and left.get("overall_score") == right.get("overall_score")
            ):
                exact_score_ties += 1

    eligible = _as_nonnegative_int(summary.get("eligible_systems"))
    returned = len(rankings)
    secondary_returned = sum(
        _as_nonnegative_int(panel.get("returned_systems"))
        for panel in secondary_panels
        if isinstance(panel, dict)
    )
    secondary_coordinates_with_results = sum(
        bool(panel.get("returned_systems"))
        for panel in secondary_panels
        if isinstance(panel, dict)
    )
    flags: list[dict[str, str]] = []
    if returned == 0:
        flags.append(
            {
                "code": (
                    "NO_PRIMARY_RANKED_SYSTEMS"
                    if secondary_returned
                    else "NO_RANKED_SYSTEMS"
                ),
                "severity": "caution" if secondary_returned else "critical",
                "message": (
                    "No system covers the authoritative primary composition; "
                    "independent secondary-coordinate rankings are available."
                    if secondary_returned
                    else "No system passed the complete ranking gates."
                ),
            }
        )
    if eligible > returned:
        flags.append(
            {
                "code": "RETURN_LIMIT_TRUNCATED",
                "severity": "notice",
                "message": (
                    f"{eligible - returned} eligible systems are outside the "
                    "returned ranking limit."
                ),
            }
        )
    incomplete = _as_nonnegative_int(summary.get("incomplete_systems"))
    if incomplete:
        flags.append(
            {
                "code": "INCOMPLETE_SYSTEMS_EXCLUDED",
                "severity": "caution",
                "message": (
                    f"{incomplete} systems lacked a complete comparable "
                    "target/grid result."
                ),
            }
        )
    if primary_requested > primary_interpolated:
        flags.append(
            {
                "code": "PRIMARY_GRID_COVERAGE_PARTIAL",
                "severity": "caution",
                "message": (
                    f"{primary_requested - primary_interpolated} returned "
                    "primary-grid coordinates were unavailable."
                ),
            }
        )
    if source_count != complete_source_identity_count:
        flags.append(
            {
                "code": "INCOMPLETE_SOURCE_IDENTITY",
                "severity": "critical",
                "message": (
                    f"{source_count - complete_source_identity_count} returned "
                    "criteria lack a complete DOI/literature/block/curve identity."
                ),
            }
        )

    return {
        "result_status": result.get("status"),
        "pipeline_counts": {
            key: summary.get(key)
            for key in (
                "registry_candidates",
                "authoritative_blocks_gathered",
                "normalized_evidence_sources",
                "materialized_target_sources",
                "property_curve_candidates",
                "selected_property_curves",
                "rejected_property_curves",
                "interpolated_selected_curves",
                "eligible_systems",
                "incomplete_systems",
                "returned_systems",
                "secondary_grid_coordinates",
                "secondary_grid_coordinates_with_results",
                "secondary_grid_candidate_occurrences",
                "secondary_grid_returned_occurrences",
            )
        },
        "ranking": {
            "criteria_returned": criteria_count,
            "systems_returned": returned,
            "systems_eligible_before_limit": eligible,
            "truncated_by_limit": max(0, eligible - returned),
            "comparable_groups_returned": len(ranking_groups),
            "exact_score_tie_pairs_within_groups": exact_score_ties,
            "overall_score_range": (
                {
                    "minimum": min(overall_scores),
                    "maximum": max(overall_scores),
                }
                if overall_scores
                else None
            ),
            "evidence_quality_score": (
                {
                    "minimum": min(quality_scores),
                    "maximum": max(quality_scores),
                    "mean": fmean(quality_scores),
                }
                if quality_scores
                else None
            ),
        },
        "grid_coverage": {
            "primary_requested": primary_requested,
            "primary_interpolated": primary_interpolated,
            "primary_used_for_ranking": primary_used,
            "primary_interpolation_fraction": (
                primary_interpolated / primary_requested
                if primary_requested
                else None
            ),
            "secondary_requested": secondary_requested,
            "secondary_available": secondary_available,
            "secondary_coverage_fraction": (
                secondary_available / secondary_requested
                if secondary_requested
                else None
            ),
        },
        "secondary_coordinate_rankings": {
            "coordinates_evaluated": len(secondary_panels),
            "coordinates_with_results": secondary_coordinates_with_results,
            "returned_candidate_occurrences": secondary_returned,
            "role": "secondary_context_not_primary_substitution",
            "leading_coordinates": [
                {
                    "sequence": panel.get("sequence"),
                    "coordinate": panel.get("coordinate"),
                    "eligible_systems": panel.get("eligible_systems"),
                    "returned_systems": panel.get("returned_systems"),
                    "top_candidate_keys": [
                        row.get("candidate_key")
                        for row in panel.get("rankings", [])[:3]
                    ],
                }
                for panel in secondary_panels[:5]
                if isinstance(panel, dict)
            ],
        },
        "provenance": {
            "criterion_sources": source_count,
            "complete_source_identities": complete_source_identity_count,
            "complete_source_identity_fraction": (
                complete_source_identity_count / source_count
                if source_count
                else None
            ),
            "required_identity": (
                "doi + lit_num_id + block_number + target_local_id + "
                "selected_curve_id"
            ),
        },
        "diagnostics": {
            "returned_count": len(diagnostics),
            "truncated_in_result": bool(
                result.get("diagnostics_truncated_in_result")
            ),
            "severity_counts": dict(sorted(severity_counts.items())),
            "top_codes": [
                {"code": code, "count": count}
                for code, count in diagnostic_codes.most_common(12)
            ],
        },
        "stage_status_counts": dict(sorted(stage_statuses.items())),
        "quality_flags": flags,
        "top_rankings": [
            _ranking_summary(row)
            for row in rankings[
                :RESULT_OBSERVER_TOP_RANKINGS_IN_QUALITY_SNAPSHOT
            ]
        ],
    }


def build_result_observer_tools(
    result: dict[str, Any],
) -> dict[str, Callable[..., dict[str, Any]]]:
    """Bind deterministic read-only inspection tools to one frozen result."""
    rankings = result.get("rankings")
    if not isinstance(rankings, list):
        raise TypeError("result observer input lacks rankings")
    by_rank = {
        int(row["rank"]): row
        for row in rankings
        if isinstance(row, dict)
        and isinstance(row.get("rank"), int)
        and not isinstance(row.get("rank"), bool)
    }

    def inspect_return_quality() -> dict[str, Any]:
        """Return deterministic coverage, provenance, diagnostic, and top-rank quality metrics."""
        return build_quality_snapshot(result)

    def inspect_ranked_results(
        start_rank: int = 1,
        count: int = 10,
    ) -> dict[str, Any]:
        """Return exact bounded ranked-system summaries, preserving IDs, values, coverage, and sources."""
        if isinstance(start_rank, bool) or not isinstance(start_rank, int):
            raise TypeError("start_rank must be an integer")
        if isinstance(count, bool) or not isinstance(count, int):
            raise TypeError("count must be an integer")
        if start_rank < 1:
            raise ValueError("start_rank must be positive")
        if count < 1 or count > RESULT_OBSERVER_MAX_RANKINGS_PER_INSPECTION:
            raise ValueError(
                "count must be between 1 and "
                f"{RESULT_OBSERVER_MAX_RANKINGS_PER_INSPECTION}"
            )
        selected = [
            _ranking_summary(by_rank[rank])
            for rank in range(start_rank, start_rank + count)
            if rank in by_rank
        ]
        return {
            "start_rank": start_rank,
            "requested_count": count,
            "returned_count": len(selected),
            "total_rankings": len(rankings),
            "rankings": selected,
        }

    def compare_ranked_systems(ranks: list[int]) -> dict[str, Any]:
        """Calculate exact score and criterion-value deltas for selected ranks when their ranking groups are comparable."""
        if not isinstance(ranks, list) or any(
            isinstance(rank, bool) or not isinstance(rank, int)
            for rank in ranks
        ):
            raise TypeError("ranks must be a flat integer array")
        if len(ranks) < 2 or len(ranks) > RESULT_OBSERVER_MAX_COMPARISON_RANKS:
            raise ValueError(
                "ranks must contain 2 to "
                f"{RESULT_OBSERVER_MAX_COMPARISON_RANKS} entries"
            )
        if len(set(ranks)) != len(ranks):
            raise ValueError("ranks must be unique")
        missing = [rank for rank in ranks if rank not in by_rank]
        if missing:
            raise ValueError(f"unknown returned ranks: {missing}")
        reference = by_rank[ranks[0]]
        reference_criteria = {
            (
                row.get("target", {}).get("source_global_id"),
                row.get("target", {}).get("basis"),
            ): row
            for row in reference.get("criteria", [])
        }
        comparisons: list[dict[str, Any]] = []
        for rank in ranks:
            row = by_rank[rank]
            comparable = _same_ranking_group(reference, row)
            deltas: list[dict[str, Any]] = []
            if comparable:
                for criterion in row.get("criteria", []):
                    key = (
                        criterion.get("target", {}).get("source_global_id"),
                        criterion.get("target", {}).get("basis"),
                    )
                    left = reference_criteria.get(key)
                    left_value = left.get("raw_value") if left else None
                    right_value = criterion.get("raw_value")
                    delta = (
                        float(right_value) - float(left_value)
                        if isinstance(left_value, (int, float))
                        and not isinstance(left_value, bool)
                        and isinstance(right_value, (int, float))
                        and not isinstance(right_value, bool)
                        else None
                    )
                    deltas.append(
                        {
                            "target_global_id": key[0],
                            "basis": key[1],
                            "canonical_unit": criterion.get(
                                "target", {}
                            ).get("canonical_unit"),
                            "raw_value": right_value,
                            "delta_from_reference": delta,
                        }
                    )
            comparisons.append(
                {
                    "rank": rank,
                    "candidate_key": row.get("candidate_key"),
                    "compound_names": row.get("compound_names", []),
                    "comparable_to_reference": comparable,
                    "overall_score": row.get("overall_score"),
                    "overall_score_delta_from_reference": (
                        float(row["overall_score"])
                        - float(reference["overall_score"])
                        if comparable
                        else None
                    ),
                    "criterion_deltas": deltas,
                }
            )
        return {
            "reference_rank": ranks[0],
            "comparisons": comparisons,
            "warning": (
                "Deltas are emitted only for systems in the same comparable "
                "ranking group."
            ),
        }

    return {
        "inspect_return_quality": inspect_return_quality,
        "inspect_ranked_results": inspect_ranked_results,
        "compare_ranked_systems": compare_ranked_systems,
    }


def validate_result_assessment(
    assessment: dict[str, Any], result: dict[str, Any]
) -> dict[str, Any]:
    """Require the exact commentary schema and valid returned-result refs."""
    if not isinstance(assessment, dict):
        raise TypeError("result-observer assessment must be an object")
    expected = set(_ASSESSMENT_SCHEMA_EXAMPLE)
    if set(assessment) != expected:
        raise ValueError(
            "RESULT_OBSERVER_SCHEMA_ERROR: expected exactly "
            f"{sorted(expected)}, received {sorted(assessment)}"
        )
    verdict = assessment["quality_verdict"]
    if verdict not in _QUALITY_VERDICTS:
        raise ValueError(
            f"quality_verdict must be one of {sorted(_QUALITY_VERDICTS)}"
        )
    comment = assessment["tool_quality_comment"]
    if not isinstance(comment, str) or not comment.strip():
        raise TypeError("tool_quality_comment must be non-empty text")

    def validate_text_list(name: str, maximum: int) -> None:
        values = assessment[name]
        if not isinstance(values, list) or len(values) > maximum or any(
            not isinstance(value, str) or not value.strip()
            for value in values
        ):
            raise TypeError(
                f"{name} must be an array of at most {maximum} non-empty strings"
            )

    validate_text_list("strengths", RESULT_OBSERVER_MAX_STRENGTHS)
    validate_text_list("limitations", RESULT_OBSERVER_MAX_LIMITATIONS)
    validate_text_list("recommended_follow_up", RESULT_OBSERVER_MAX_FOLLOW_UPS)

    rankings = result.get("rankings", [])
    if not isinstance(rankings, list):
        raise TypeError("result rankings must be an array")
    candidate_keys = {
        row.get("candidate_key")
        for row in rankings
        if isinstance(row, dict) and isinstance(row.get("candidate_key"), str)
    }
    secondary_panels = result.get("secondary_grid_rankings", [])
    if not isinstance(secondary_panels, list):
        raise TypeError("result secondary_grid_rankings must be an array")
    secondary_candidate_keys = {
        row.get("candidate_key")
        for panel in secondary_panels
        if isinstance(panel, dict)
        for row in panel.get("rankings", [])
        if isinstance(row, dict)
        and isinstance(row.get("candidate_key"), str)
    }
    candidate_keys.update(secondary_candidate_keys)
    request = result.get("request", {})
    target_ids = {
        row.get("source_global_id")
        for row in request.get("ranking_targets", [])
        if isinstance(row, dict)
        and isinstance(row.get("source_global_id"), str)
    }
    insights = assessment["chemistry_insights"]
    if (
        not isinstance(insights, list)
        or len(insights) > RESULT_OBSERVER_MAX_CHEMISTRY_INSIGHTS
    ):
        raise TypeError(
            "chemistry_insights must be an array of at most "
            f"{RESULT_OBSERVER_MAX_CHEMISTRY_INSIGHTS} objects"
        )
    insight_fields = {
        "statement",
        "supporting_candidate_keys",
        "supporting_target_ids",
        "confidence",
    }
    for index, insight in enumerate(insights):
        if not isinstance(insight, dict) or set(insight) != insight_fields:
            raise ValueError(
                f"chemistry_insights[{index}] must contain exactly "
                f"{sorted(insight_fields)}"
            )
        if not isinstance(insight["statement"], str) or not insight[
            "statement"
        ].strip():
            raise TypeError(
                f"chemistry_insights[{index}].statement must be non-empty text"
            )
        refs = insight["supporting_candidate_keys"]
        ids = insight["supporting_target_ids"]
        if not isinstance(refs, list) or not refs or any(
            ref not in candidate_keys for ref in refs
        ):
            raise ValueError(
                f"chemistry_insights[{index}] references an unknown candidate"
            )
        if not isinstance(ids, list) or not ids or any(
            target_id not in target_ids for target_id in ids
        ):
            raise ValueError(
                f"chemistry_insights[{index}] references an unknown target ID"
            )
        if insight["confidence"] not in _INSIGHT_CONFIDENCE:
            raise ValueError(
                f"chemistry_insights[{index}].confidence must be one of "
                f"{sorted(_INSIGHT_CONFIDENCE)}"
            )
    if not rankings and not secondary_candidate_keys:
        if verdict != "insufficient" or insights:
            raise ValueError(
                "a no-results observer assessment must be insufficient and "
                "contain no chemistry insights"
            )
    critical_flags = {
        row["code"]
        for row in build_quality_snapshot(result)["quality_flags"]
        if row["severity"] == "critical"
    }
    if critical_flags and verdict == "high":
        raise ValueError(
            "a high quality verdict is incompatible with critical flags: "
            + ", ".join(sorted(critical_flags))
        )
    return assessment


def observe_screening_result(
    result: dict[str, Any],
    *,
    client: Any | None = None,
) -> dict[str, Any]:
    """Run the bounded observer and return metadata for result/artifacts."""
    authoritative_sha256 = _authoritative_result_sha256(result)
    snapshot = build_quality_snapshot(result)
    tools = build_result_observer_tools(result)
    system_prompt = (
        _SYSTEM_PROMPT
        + "\n\n# Required final JSON schema example\n"
        + json.dumps(_ASSESSMENT_SCHEMA_EXAMPLE, indent=2, ensure_ascii=False)
        + "\n\n"
        + build_tool_instructions(tools)
    )
    request = result.get("request", {})
    user_message = (
        "Assess the completed deterministic property-screening result. "
        "Begin by calling inspect_return_quality.\n\n"
        "## Confirmed request context\n"
        + json.dumps(
            {
                "purpose": request.get("purpose"),
                "tasks": request.get("tasks"),
                "ranking_targets": request.get("ranking_targets", []),
                "target_constraints": request.get("target_constraints", []),
                "center_comp_num_ids": request.get("center_comp_num_ids", []),
                "system_type": request.get("system_type"),
                "system_scope": request.get("system_scope"),
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    observer_client = client if client is not None else QueryClient.for_l2()
    with _observer_stats_scope() as stats_tracking_scope:
        turn = agent_turn(
            user_message,
            system_prompt=system_prompt,
            tools=tools,
            memory=[],
            client=observer_client,
            max_iterations=RESULT_OBSERVER_MAX_ITERATIONS,
            timeout=RESULT_OBSERVER_MAX_SECONDS,
            required_tools={"inspect_return_quality"},
            is_subagent=True,
        )
        if turn.timed_out:
            raise RuntimeError("property-screening result observer timed out")
        parsed, _ = guard_json_answer(
            turn.answer,
            client=observer_client,
            label="property-screening-result-observer",
            schema=_ASSESSMENT_SCHEMA_EXAMPLE,
            max_retries=1,
            max_tokens=RESULT_OBSERVER_MAX_TOKENS,
        )
    if not isinstance(parsed, dict):
        raise ValueError("result observer returned invalid JSON")
    assessment = validate_result_assessment(parsed, result)
    if _authoritative_result_sha256(result) != authoritative_sha256:
        raise RuntimeError(
            "result observer mutated the authoritative deterministic result"
        )
    tools_called = [
        item.get("tool")
        for item in turn.tool_history
        if isinstance(item, dict) and isinstance(item.get("tool"), str)
    ]
    if "inspect_return_quality" not in tools_called:
        raise ValueError(
            "result observer did not execute its mandatory quality inspection"
        )
    return {
        "role": "non_authoritative_post_ranking_result_observer",
        "authoritative_result_unchanged": True,
        "authoritative_result_sha256": authoritative_sha256,
        "authoritative_fields": [
            "request",
            "rankings",
            "diagnostics",
            "cache_trace",
            "stage_trace",
        ],
        "quality_snapshot": snapshot,
        "assessment": assessment,
        "execution": {
            "agent_type": "bounded_read_only_react",
            "model": getattr(observer_client, "model", None),
            "iterations": turn.iterations,
            "elapsed_seconds": turn.elapsed_seconds,
            "timed_out": turn.timed_out,
            "tools_called": tools_called,
            "stats_tracking_scope": stats_tracking_scope,
            "database_tools_available": False,
            "result_mutation_tools_available": False,
        },
    }


__all__ = [
    "build_quality_snapshot",
    "build_result_observer_tools",
    "observe_screening_result",
    "validate_result_assessment",
]
