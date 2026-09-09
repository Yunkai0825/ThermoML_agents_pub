"""Composition-normalization branch over all discovered sources."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..interface import (
    Diagnostic,
    NormalizedRequest,
    SourceSeries,
)
from .reader import AuthoritativeBlock
from ..processing import build_source_series
from ..runtime import JsonContentCache


@dataclass
class CompositionBranchResult:
    series: list[SourceSeries]
    diagnostics: list[Diagnostic]
    cache_trace: dict[str, Any]
    candidates_processed: int


def run_composition_branch(
    request: NormalizedRequest,
    blocks: list[AuthoritativeBlock],
    *,
    unary_reference_pool: dict[str, dict[str, list[dict[str, Any]]]],
    database_fingerprint: dict[str, Any],
) -> CompositionBranchResult:
    """Normalize every candidate without ever combining source observations."""
    cache = JsonContentCache("composition_translation")
    cache_hits = 0
    cache_misses = 0
    cache_keys: list[str] = []
    series: list[SourceSeries] = []
    diagnostics: list[Diagnostic] = []

    for block in blocks:
        candidate = block.candidate
        try:
            if not block.units_aligned:
                raise ValueError(
                    f"{candidate.key} bypassed the unit-alignment boundary"
                )
            plans: list[dict[str, Any]] = []
            source_series, source_diagnostics = build_source_series(
                block,
                request,
                unary_reference_pool=unary_reference_pool,
                record_composition_plan=plans.append,
            )
            for plan in plans:
                key_payload = {
                        "database": database_fingerprint[
                            "fingerprint_sha256"
                        ],
                        "doi": plan["doi"],
                        "lit_num_id": plan["lit_num_id"],
                        "block_number": plan["block_number"],
                        "BLKsubsys_id": plan["BLKsubsys_id"],
                        "source_identity": plan["source_identity"],
                        "component_order": plan.get("component_order", []),
                        "field_catalog": plan.get("field_catalog", []),
                        "bridge_catalog": plan.get("bridge_catalog", []),
                        "unit_alignment": plan.get("unit_alignment", []),
                        "self_consistency_atol_mole_fraction": plan.get(
                            "self_consistency_atol_mole_fraction"
                        ),
                }
                key = cache.key(key_payload)
                cached = cache.read(key)
                if cached is None:
                    cache.write(key, plan)
                    cache_misses += 1
                else:
                    comparable = {
                            name: cached.get(name)
                            for name in (
                                "kind",
                                "degrees_of_freedom",
                                "selection_policy",
                                "self_consistency_atol_mole_fraction",
                                "source_identity",
                                "component_order",
                                "reference_component",
                                "field_catalog",
                                "bridge_catalog",
                                "unit_alignment",
                                "candidate_groups",
                                "selected_group_counts",
                                "conflicting_rows",
                                "uncovered_rows",
                            )
                    }
                    current = {
                        name: plan.get(name) for name in comparable
                    }
                    if comparable != current:
                        raise ValueError(
                            "composition cache disagrees with current "
                            f"database declarations for {candidate.key}"
                        )
                    cache_hits += 1
                cache_keys.append(key)
            series.extend(source_series)
            diagnostics.extend(source_diagnostics)
        except Exception as exc:
            diagnostics.append(
                Diagnostic(
                    code="SOURCE_EXTRACTION_FAILED",
                    message=f"{type(exc).__name__}: {exc}",
                    stage="composition_identity",
                    severity="warning",
                    source_key=candidate.key,
                )
            )
    return CompositionBranchResult(
        series=series,
        diagnostics=diagnostics,
        cache_trace={
            "namespace": cache.namespace,
            "hits": cache_hits,
            "misses": cache_misses,
            "keys": cache_keys,
        },
        candidates_processed=len(blocks),
    )
