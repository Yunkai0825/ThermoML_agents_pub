"""Fail-closed invariants for absolute-property screening results."""

from __future__ import annotations

from typing import Any

import numpy as np

from ..interface import SourceSeries


def validate_materialized_target_sources(
    sources: list[SourceSeries],
) -> list[SourceSeries]:
    """Reject any source that bypassed presentation/relationship materialization."""
    for source in sources:
        if source.response_semantics != "absolute_target":
            raise ValueError(
                "semantic barrier received a non-absolute target source: "
                f"{source.source_key} ({source.response_semantics})"
            )
        if not np.all(np.isfinite(source.values)):
            raise ValueError(
                f"semantic barrier received non-finite values: {source.source_key}"
            )
        trace = source.derivation.get("presentation_materialization")
        if source.presentation_kind != "direct":
            if not isinstance(trace, dict) or trace.get("status") != "materialized":
                raise ValueError(
                    "reference presentation lacks a successful materialization "
                    f"trace: {source.source_key}"
                )
            reference = trace.get("reference_ensemble")
            if not isinstance(reference, dict) or not reference.get("sources"):
                raise ValueError(
                    "reference presentation lacks traceable reference sources: "
                    f"{source.source_key}"
                )
    return sources


def _validate_ranking_row(row: dict[str, Any], *, location: str) -> None:
    for criterion in row.get("criteria", []):
        evidence = criterion.get("evidence")
        if not isinstance(evidence, dict):
            raise ValueError(f"{location} criterion lacks evidence identity")
        if evidence.get("response_semantics") != "absolute_target":
            raise ValueError(
                f"{location} contains a non-absolute ranked response"
            )
        raw = criterion.get("raw_value")
        if not isinstance(raw, (int, float)) or not np.isfinite(raw):
            raise ValueError(f"{location} contains a non-finite ranking value")


def validate_ranking_output(
    rankings: list[dict[str, Any]],
    secondary_grid_rankings: list[dict[str, Any]],
) -> dict[str, int]:
    """Validate final semantics and active-identity uniqueness before publish."""
    for index, row in enumerate(rankings):
        _validate_ranking_row(row, location=f"primary[{index}]")

    for panel_index, panel in enumerate(secondary_grid_rankings):
        seen: set[tuple[Any, ...]] = set()
        for row_index, row in enumerate(panel.get("rankings", [])):
            _validate_ranking_row(
                row,
                location=f"secondary[{panel_index}].rankings[{row_index}]",
            )
            signature = row.get("active_composition_signature")
            key = (
                repr(signature),
                row.get("phase_num_id"),
                repr(row.get("ranking_group")),
            )
            if key in seen:
                raise ValueError(
                    "secondary panel contains a duplicate active chemical "
                    f"identity at coordinate {panel.get('coordinate')}"
                )
            seen.add(key)
    return {
        "primary_rows_validated": len(rankings),
        "secondary_panels_validated": len(secondary_grid_rankings),
        "secondary_rows_validated": sum(
            len(panel.get("rankings", []))
            for panel in secondary_grid_rankings
        ),
    }
