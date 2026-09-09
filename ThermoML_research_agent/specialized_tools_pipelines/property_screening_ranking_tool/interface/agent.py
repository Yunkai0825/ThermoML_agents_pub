"""Agent-visible request reviews and bounded executed-result Markdown."""

from __future__ import annotations

import json
from typing import Any

from NIST_ThermoML_agents.general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import (
    compacts,
)


from ..tool_settings import (
    AGENT_MAX_DIAGNOSTICS,
    AGENT_MAX_INLINE_PRIMARY_GRID_PROFILES,
    AGENT_MAX_MARKDOWN_CHARS,
    AGENT_MAX_RANKINGS,
    AGENT_MAX_SECONDARY_COORDINATES,
    AGENT_MAX_SECONDARY_RANKINGS_PER_COORDINATE,
)
def _clip(lines: list[str]) -> str:
    rendered: list[str] = []
    count = 0
    for line in lines:
        addition = len(line) + 1
        if count + addition > AGENT_MAX_MARKDOWN_CHARS:
            rendered.append(
                "… compact context bound reached; inspect the run manifest "
                "for complete artifacts."
            )
            break
        rendered.append(line)
        count += addition
    return "\n".join(rendered).rstrip() + "\n"


def _selected_curve_label(source: dict[str, Any]) -> str:
    curve_id = source.get("selected_curve_id")
    doi = source.get("doi")
    lit_num_id = source.get("lit_num_id")
    if not curve_id or not doi or not lit_num_id:
        raise ValueError(
            "ranked criterion must identify its selected curve and paired "
            "DOI/lit_num_id source"
        )
    label = f"{curve_id}; selected source: {lit_num_id} ({doi})"
    if source.get("block_number"):
        label += f"/{source['block_number']}"
    if source.get("BLKsubsys_id"):
        label += f"/{source['BLKsubsys_id']}"
    if source.get("target_local_id"):
        label += f"/{source['target_local_id']}"
    if source.get("selection_score") is not None:
        label += f"; curve-selection score={source['selection_score']:.4g}"
    return label


def _profile_number(value: Any) -> str:
    if not isinstance(value, (int, float)):
        return "—"
    return f"{float(value):.8g}"


def _presentation_materialization_note(
    criterion: dict[str, Any],
) -> str | None:
    derivation = criterion.get("derivation")
    if not isinstance(derivation, dict):
        return None
    trace = derivation.get("presentation_materialization")
    if not isinstance(trace, dict) or trace.get("status") != "materialized":
        return None
    ensemble = trace.get("reference_ensemble")
    if not isinstance(ensemble, dict):
        return None
    component_ensembles = ensemble.get("component_ensembles")
    if isinstance(component_ensembles, list) and component_ensembles:
        tiers = sorted(
            {
                str(item.get("reference_tier"))
                for item in component_ensembles
                if isinstance(item, dict) and item.get("reference_tier")
            }
        )
        n_sources = sum(
            int(item.get("distribution", {}).get("n_sources", 0))
            for item in component_ensembles
            if isinstance(item, dict)
        )
    else:
        tiers = [str(ensemble.get("reference_tier"))]
        n_sources = int(
            ensemble.get("distribution", {}).get("n_sources", 0)
        )
    tier_text = ",".join(value for value in tiers if value != "None")
    return (
        f"reported {trace.get('presentation_kind')} → absolute property via "
        f"{ensemble.get('reference_state_type')}; {tier_text or 'reference'}; "
        f"n_reference_sources={n_sources}; {trace.get('equation')}"
    )


def _secondary_grid_lines(
    profile: dict[str, Any], target: dict[str, Any]
) -> list[str]:
    values = profile.get("values")
    if not isinstance(values, list) or not values:
        return []
    dimensions = profile.get("dimensions")
    coordinate_ids = profile.get("coordinate_comp_num_ids", [])
    coordinate_names = profile.get("coordinate_compound_names", [])
    labels = [
        f"x{index}={name} (`{comp_num_id}`)"
        for index, (comp_num_id, name) in enumerate(
            zip(coordinate_ids, coordinate_names), start=1
        )
    ]
    closure = (
        f"closure={profile.get('closure_compound_name')} "
        f"(`{profile.get('closure_comp_num_id')}`)"
    )
    lines = [
        (
            "     Secondary regulated composition grid; context only, "
            "not used to calculate the ranking score."
        ),
        "     - Coordinates: " + "; ".join([*labels, closure]),
        "     - Axis: "
        + " | ".join(_profile_number(value) for value in profile.get("axis", [])),
    ]
    basis = target.get("basis")
    value_fields = ["real"]
    if basis in {"ideal", "deviation", "absolute_deviation"}:
        value_fields.append(basis)

    if dimensions == 1:
        lines.append(
            "     - `x1`: "
            + " | ".join(
                _profile_number(row.get("composition", [None])[0])
                for row in values
            )
        )
        for field in value_fields:
            key = f"{field}_value" if field in {"real", "ideal"} else field
            lines.append(
                f"     - `{field}`: "
                + " | ".join(_profile_number(row.get(key)) for row in values)
            )
    else:
        rendered_points: list[str] = []
        for row in values:
            coordinate = ",".join(
                _profile_number(value)
                for value in row.get("composition", [])
            )
            rendered_points.append(
                f"({coordinate})={_profile_number(row.get('real_value'))}"
            )
        display_limit = 66 if dimensions == 2 else 32
        displayed = rendered_points[:display_limit]
        suffix = (
            f" | … {len(rendered_points) - display_limit} more in the grid CSV"
            if len(rendered_points) > display_limit
            else ""
        )
        lines.append(
            f"     - `real(x1..x{dimensions})`: "
            + " | ".join(displayed)
            + suffix
        )

    coverage = profile.get("coverage", {})
    failures = coverage.get("unavailable_by_reason", {})
    failure_text = ", ".join(
        f"{reason}={count}" for reason, count in sorted(failures.items())
    ) or "none"
    lines.append(
        f"     - Coverage: {coverage.get('available', 0)}/"
        f"{coverage.get('requested', len(values))}; failures: {failure_text}. "
        "`—` means no strict first-order interpolation without extrapolation."
    )
    return lines


def _coordinate_label(coordinate: list[Any]) -> str:
    return ", ".join(
        f"x{index}={_profile_number(value)}"
        for index, value in enumerate(coordinate, start=1)
    )


def _secondary_ranking_lines(
    panels: list[dict[str, Any]],
) -> list[str]:
    lines = [
        "",
        "## Ordered secondary coordinate rankings",
        "",
        (
            "These are independent cross-system rankings at fixed regulated "
            "coordinates. They are secondary context only: a value at one "
            "composition never substitutes for the primary query value."
        ),
    ]
    first_ranked_panel = next(
        (panel for panel in panels if panel.get("rankings")),
        None,
    )
    if first_ranked_panel is not None:
        axis_semantics = first_ranked_panel.get("axis_semantics", {})
        center_ids = axis_semantics.get("center_comp_num_ids", [])
        first_criterion = (
            first_ranked_panel["rankings"][0].get("criteria") or [{}]
        )[0]
        composition_names = {
            item.get("comp_num_id"): item.get("compound_name")
            for item in first_criterion.get("full_composition", [])
            if item.get("comp_num_id")
        }
        axis_labels = [
            f"x{index}={composition_names.get(comp_num_id, comp_num_id)} "
            f"(`{comp_num_id}`)"
            for index, comp_num_id in enumerate(center_ids, start=1)
        ]
        if axis_labels:
            lines.extend(
                [
                    "",
                    "Aligned leading axes: " + "; ".join(axis_labels) + ".",
                ]
            )
        lines.append(
            "Axis rule: requested center components first, remaining global "
            "component IDs sorted within each system, and the last component "
            "is closure. Equal-distance coordinates remain separate panels."
        )
    displayed_panels = panels[:AGENT_MAX_SECONDARY_COORDINATES]
    for panel in displayed_panels:
        coordinate = panel.get("coordinate", [])
        nearest = panel.get("nearest_primary_coordinate", [])
        lines.extend(
            [
                "",
                (
                    f"### {panel.get('sequence')}. "
                    f"{_coordinate_label(coordinate)}"
                ),
                (
                    f"Nearest primary coordinate: "
                    f"{_coordinate_label(nearest)}; distance "
                    f"{_profile_number(panel.get('distance_from_primary'))}. "
                    f"Eligible systems: {panel.get('eligible_systems', 0)}; "
                    f"stored cap: {panel.get('per_coordinate_limit', 0)}."
                ),
            ]
        )
        rankings = panel.get("rankings", [])
        if not rankings:
            lines.append(
                "No selected whole curve covers this coordinate for every "
                "requested target/basis."
            )
            continue
        for row in rankings[
            :AGENT_MAX_SECONDARY_RANKINGS_PER_COORDINATE
        ]:
            names = " + ".join(row.get("compound_names", []))
            criterion_text: list[str] = []
            source_text: list[str] = []
            for criterion in row.get("criteria", []):
                target = criterion.get("target", {})
                unit = target.get("canonical_unit") or "1"
                criterion_text.append(
                    f"{target.get('quantity_key')}="
                    f"{_profile_number(criterion.get('raw_value'))} {unit} "
                    f"(score {criterion.get('score')})"
                )
                materialization_note = _presentation_materialization_note(
                    criterion
                )
                if materialization_note:
                    criterion_text[-1] += f" [{materialization_note}]"
                source = criterion.get("source", {})
                source_text.append(_selected_curve_label(source))
            lines.append(
                f"{row.get('rank')}. **{names or row.get('system_signature')}** "
                f"(`{row.get('candidate_key')}`): "
                + "; ".join(criterion_text)
                + f"; evidence {row.get('quality_score')}; source "
                + " | ".join(source_text)
                + "."
            )
        hidden = len(rankings) - min(
            len(rankings), AGENT_MAX_SECONDARY_RANKINGS_PER_COORDINATE
        )
        if hidden:
            lines.append(
                f"… {hidden} additional stored candidate(s) for this "
                "coordinate are in secondary_grid_rankings.json/csv."
            )
    if len(panels) > len(displayed_panels):
        lines.append(
            f"… {len(panels) - len(displayed_panels)} additional ordered "
            "coordinate panel(s) are in secondary_grid_rankings.json/csv."
        )
    return lines


@compacts("screen_property_systems")
def compact_screen_property_systems(data: dict[str, Any]) -> str:
    """Keep ranked chemistry and core nested IDs; move full grids to artifacts."""
    if not isinstance(data, dict):
        raise TypeError("screen_property_systems result must be an object")
    is_request_review = (
        data.get("executed") is False
        and isinstance(data.get("enriched_tool_call"), dict)
        and isinstance(data.get("confirmation"), dict)
    )
    if is_request_review:
        status = data.get("status")
        confirmation = data.get("confirmation", {})
        issues = data.get("issues", [])
        lines = [
            (
                "# Property screening — correct the request"
                if status == "correction_required"
                else "# Property screening — confirm enriched metadata"
            ),
            "",
            "**No database screening has executed.**",
        ]
        if confirmation.get("token"):
            lines.extend(
                [
                    "",
                    "**Confirmation token:**",
                    f"`{confirmation['token']}`",
                ]
            )
        if issues:
            lines.extend(["", "## Issues"])
            for issue in issues:
                lines.append(
                    f"- `{issue.get('code')}` in "
                    f"`{issue.get('field')}`: {issue.get('message')}"
                )
        lines.extend(
            [
                "",
                "## Required agent action",
                str(confirmation.get("instruction", "Review the request.")),
                "",
                "## Complete hard-parsed request review",
                "```json",
                json.dumps(data, indent=2, ensure_ascii=False, default=str),
                "```",
            ]
        )
        # Confirmation is a semantic gate: the agent must see every parsed
        # identity, value, unit, conversion, operation, and issue before it can
        # authorize execution. Only executed ranking results are compacted.
        return "\n".join(lines).rstrip() + "\n"
    if data.get("executed") is not True:
        raise ValueError("unsupported property-screening result structure")
    summary = data.get("summary")
    rankings = data.get("rankings")
    if not isinstance(summary, dict) or not isinstance(rankings, list):
        raise TypeError("screening result lacks summary/rankings")
    lines = [
        "# Property screening and ranking",
        "",
        f"**Status:** {data.get('status')}",
        (
            "**Coverage:** "
            f"{summary.get('registry_candidates', 0)} registry candidates → "
            f"{summary.get('normalized_evidence_sources', 0)} normalized evidence sources → "
            f"{summary.get('materialized_target_sources', 0)} target-materialized sources → "
            f"{summary.get('selected_property_curves', 0)} selected whole curves "
            f"from {summary.get('property_curve_candidates', 0)} candidates → "
            f"{summary.get('interpolated_selected_curves', 0)} source-local interpolations → "
            f"{summary.get('eligible_systems', 0)} eligible systems; "
            f"{summary.get('returned_systems', 0)} returned."
        ),
        (
            "**Subsystem mode:** "
            f"{data.get('request', {}).get('system_scope', 'declared')} "
            "(declared is the default; BLKsubsys is opt-in)."
        ),
        "",
        "## State matching",
    ]
    constraints = data.get("request", {}).get("target_constraints", [])
    if not constraints:
        lines.append("No state constraints were supplied.")
    for constraint in constraints:
        tolerance = constraint.get("tolerance", {})
        lines.append(
            "- "
            f"{constraint.get('preferred_name')} "
            f"[`{constraint.get('canonical_unit') or '1'}`]: requested "
            f"{_profile_number(constraint.get('minimum'))} to "
            f"{_profile_number(constraint.get('maximum'))}; effective "
            f"{_profile_number(constraint.get('effective_minimum'))} to "
            f"{_profile_number(constraint.get('effective_maximum'))}; "
            f"{tolerance.get('source')} {tolerance.get('kind')} tolerance "
            f"{_profile_number(tolerance.get('value'))}."
        )
    lines.extend(["", "## Ranked systems"])
    if not rankings:
        lines.append("No system satisfied every requested chemistry and coverage gate.")
    for row_index, row in enumerate(
        rankings[:AGENT_MAX_RANKINGS], start=1
    ):
        names = " + ".join(row.get("compound_names", []))
        lines.append(
            f"{row.get('rank')}. **{names or row.get('system_signature')}** "
            f"({row.get('system_type')}); overall score "
            f"{row.get('overall_score')}, evidence {row.get('quality_score')}."
        )
        for criterion in row.get("criteria", []):
            target = criterion.get("target", {})
            source = criterion.get("source", {})
            grid = criterion.get("grid_values", [])
            baseline_kinds = sorted(
                {
                    point.get("baseline_kind")
                    for point in grid
                    if point.get("baseline_kind")
                    not in {None, "not_requested"}
                }
            )
            baseline = (
                f"; baseline={','.join(baseline_kinds)}"
                if baseline_kinds
                else ""
            )
            lines.append(
                "   - "
                f"{target.get('quantity_key')} [{target.get('basis')}, "
                f"{target.get('direction')}]: raw={criterion.get('raw_value')}, "
                f"score={criterion.get('score')}, "
                f"{len(grid)} common-grid value(s){baseline}; "
                f"{_selected_curve_label(source)}."
            )
            materialization_note = _presentation_materialization_note(
                criterion
            )
            if materialization_note:
                lines.append(
                    f"     Reference materialization: {materialization_note}."
                )
            profile = criterion.get("secondary_composition_grid")
            if (
                isinstance(profile, dict)
                and row_index <= AGENT_MAX_INLINE_PRIMARY_GRID_PROFILES
            ):
                lines.extend(_secondary_grid_lines(profile, target))
            primary_coverage = criterion.get("ranking_grid_coverage", {})
            if isinstance(primary_coverage, dict):
                primary_failures = primary_coverage.get(
                    "unavailable_by_reason", {}
                )
                primary_failure_text = ", ".join(
                    f"{reason}={count}"
                    for reason, count in sorted(primary_failures.items())
                ) or "none"
                lines.append(
                    "     Primary grid coverage: "
                    f"{primary_coverage.get('interpolated', 0)}/"
                    f"{primary_coverage.get('requested', 0)} interpolated; "
                    f"{primary_coverage.get('used_for_ranking', 0)} used; "
                    f"failures: {primary_failure_text}."
                )
            if criterion.get("baseline_message"):
                lines.append(
                    f"     Baseline note: {criterion['baseline_message']}"
                )
            for ensemble in criterion.get(
                "baseline_reference_ensembles", []
            ):
                distribution = ensemble.get("distribution", {})
                lines.append(
                    "     Pure reference "
                    f"`{ensemble.get('comp_num_id')}`: "
                    f"{ensemble.get('reference_tier')}, mean="
                    f"{_profile_number(distribution.get('mean'))} "
                    f"{ensemble.get('canonical_unit') or '1'}, "
                    f"SD={_profile_number(distribution.get('standard_deviation'))}, "
                    f"n_sources={distribution.get('n_sources', 0)}, "
                    f"n_points={distribution.get('n_observations', 0)}."
                )
    if len(rankings) > AGENT_MAX_RANKINGS:
        lines.append(
            f"… {len(rankings) - AGENT_MAX_RANKINGS} additional returned ranking(s) "
            "are in the artifact."
        )
    if len(rankings) > AGENT_MAX_INLINE_PRIMARY_GRID_PROFILES:
        lines.append(
            "Full regulated profiles for all returned primary systems are in "
            "ranking_grid_values.csv; inline profiles are limited to the first "
            f"{AGENT_MAX_INLINE_PRIMARY_GRID_PROFILES} systems to preserve "
            "agent context."
        )
    secondary_panels = data.get("secondary_grid_rankings")
    if not isinstance(secondary_panels, list):
        raise TypeError(
            "executed screening result lacks secondary_grid_rankings"
        )
    if secondary_panels:
        lines.extend(_secondary_ranking_lines(secondary_panels))
    observer = data.get("result_observer")
    if not isinstance(observer, dict):
        raise TypeError("executed screening result lacks result_observer metadata")
    assessment = observer.get("assessment")
    snapshot = observer.get("quality_snapshot")
    if not isinstance(assessment, dict) or not isinstance(snapshot, dict):
        raise TypeError("result_observer lacks assessment/quality_snapshot")
    grid_coverage = snapshot.get("grid_coverage", {})
    provenance = snapshot.get("provenance", {})
    lines.extend(
        [
            "",
            "## Read-only result quality review",
            (
                "This commentary is agent-generated from immutable result-local "
                "inspection tools; deterministic ranks, values, selected curves, "
                "and diagnostics remain authoritative."
            ),
            "",
            f"**Quality verdict:** {assessment.get('quality_verdict')}",
            "",
            str(assessment.get("tool_quality_comment", "")),
            "",
            (
                "**Deterministic checks:** primary-grid interpolation "
                f"{grid_coverage.get('primary_interpolated', 0)}/"
                f"{grid_coverage.get('primary_requested', 0)}; complete source "
                f"identities {provenance.get('complete_source_identities', 0)}/"
                f"{provenance.get('criterion_sources', 0)}."
            ),
        ]
    )
    strengths = assessment.get("strengths", [])
    if strengths:
        lines.extend(["", "**Strengths**"])
        lines.extend(f"- {item}" for item in strengths)
    limitations = assessment.get("limitations", [])
    if limitations:
        lines.extend(["", "**Limitations**"])
        lines.extend(f"- {item}" for item in limitations)
    insights = assessment.get("chemistry_insights", [])
    if insights:
        lines.extend(["", "## Result-supported chemistry insights"])
        for insight in insights:
            candidates = ", ".join(
                f"`{value}`"
                for value in insight.get("supporting_candidate_keys", [])
            )
            targets = ", ".join(
                f"`{value}`"
                for value in insight.get("supporting_target_ids", [])
            )
            lines.append(
                f"- {insight.get('statement')} "
                f"(confidence: {insight.get('confidence')}; "
                f"systems: {candidates}; targets: {targets})"
            )
    follow_up = assessment.get("recommended_follow_up", [])
    if follow_up:
        lines.extend(["", "**Recommended follow-up**"])
        lines.extend(f"- {item}" for item in follow_up)
    diagnostics = data.get("diagnostics", [])
    if diagnostics:
        lines.extend(["", "## Diagnostics (bounded)"])
        for diagnostic in diagnostics[:AGENT_MAX_DIAGNOSTICS]:
            lines.append(
                f"- `{diagnostic.get('code')}` [{diagnostic.get('stage')}]: "
                f"{diagnostic.get('message')}"
            )
        total = summary.get("diagnostics", len(diagnostics))
        if total > len(diagnostics[:AGENT_MAX_DIAGNOSTICS]):
            lines.append(
                f"… {total - len(diagnostics[:AGENT_MAX_DIAGNOSTICS])} additional "
                "diagnostic(s) are in diagnostics.json."
            )
    artifacts = data.get("artifacts", {})
    if artifacts:
        lines.extend(
            [
                "",
                "## Full evidence",
                f"- Run manifest: `{artifacts.get('run_manifest')}`",
                f"- Run directory: `{artifacts.get('run_directory')}`",
            ]
        )
    return _clip(lines)


def validate_screen_property_systems_guidance(
    *,
    tool_name: str,
    call_kwargs: dict,
    **_kwargs,
) -> str | None:
    """Route property calls into the tool-owned parse/review lifecycle."""
    if tool_name != "screen_property_systems":
        return None
    # Signature/type errors are handled by the universal gate. All chemistry,
    # identity, unit, and confirmation decisions return as a visible, raw-
    # recorded tool review so passed and failed hard-parses share one structure.
    return ""
