"""Normalize every gathered numerical block before chemistry processing."""

from __future__ import annotations

import copy
import math
from dataclasses import dataclass, replace
from typing import Any

from card_db_search_tools.basic_search_tools.advanced_block_search.catalogs import (
    load_runtime_catalogs,
)

from ..interface import Diagnostic
from .property_response import (
    PresentationKind,
    classify_presentation,
    presentation_requires_reference,
    reported_canonical_unit,
)
from ..sources.reader import AuthoritativeBlock
from .conversion import resolve_unit


@dataclass
class UnitAlignmentResult:
    blocks: list[AuthoritativeBlock]
    diagnostics: list[Diagnostic]
    report: list[dict[str, Any]]


_FIELD_ROLES = (
    ("properties", "BLKprop_id", "prop_num_id", "property"),
    ("variables", "BLKvar_id", "var_num_id", "variable"),
    ("constraints", "BLKconstr_id", "constr_num_id", "constraint"),
)
_EXPLICIT_UNIT_FIELDS = (
    "source_unit",
    "reported_unit",
    "unit",
    "units",
)


def _source_unit(
    declaration: dict[str, Any], canonical_unit: str
) -> tuple[str, str]:
    for field in _EXPLICIT_UNIT_FIELDS:
        value = declaration.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip(), f"declaration.{field}"
    # ThermoML numerical quantity types have fixed registry units. PCS keeps
    # the readable name but does not need a redundant unit field.
    return canonical_unit, "ThermoML_registry_fixed_unit"


def _alignment_record(
    *,
    section: str,
    role: str,
    local_id: str,
    global_id: str,
    quantity_key: str,
    source_unit: str,
    source_unit_origin: str,
    reported_unit: str,
    target_unit: str,
    presentation: str | None,
    presentation_kind: str | None,
    materialization_required: bool,
    scale: float,
    offset: float,
    n_values: int,
) -> dict[str, Any]:
    identity = scale == 1.0 and offset == 0.0
    return {
        "section": section,
        "role": role,
        "local_id": local_id,
        "global_id": global_id,
        "quantity_key": quantity_key,
        "from_unit": source_unit,
        "to_unit": reported_unit,
        "target_unit": target_unit,
        "source_unit_origin": source_unit_origin,
        "presentation": presentation,
        "presentation_kind": presentation_kind,
        "materialization_required": materialization_required,
        "status": "identity" if identity else "converted",
        "scale": scale,
        "offset": offset,
        "n_values": n_values,
    }


def align_authoritative_block_units(
    block: AuthoritativeBlock,
) -> AuthoritativeBlock:
    """Return a copied block whose numerical fields use registry units."""
    if block.units_aligned:
        raise ValueError(f"{block.candidate.key} was already unit aligned")
    translation = load_runtime_catalogs().translation.by_global_id
    projected = copy.deepcopy(block.projected)
    rows = [dict(row) for row in block.rows]
    records: list[dict[str, Any]] = []

    for section, local_field, global_field, role in _FIELD_ROLES:
        for declaration in projected.get(section, []):
            local_id = declaration.get(local_field)
            global_id = declaration.get(global_field)
            if not isinstance(local_id, str) or not isinstance(global_id, str):
                raise ValueError(
                    f"{block.candidate.key} has an invalid {section} identity"
                )
            registry = translation.get(global_id)
            if registry is None:
                raise ValueError(
                    f"{block.candidate.key}/{local_id} has unknown {global_id}"
                )
            target_unit = registry.semantics.canonical_unit or ""
            presentation = (
                declaration.get("presentation")
                if role == "property"
                else None
            )
            kind = (
                classify_presentation(presentation)
                if role == "property"
                else PresentationKind.DIRECT
            )
            reported_unit = (
                reported_canonical_unit(kind, target_unit)
                if role == "property"
                else target_unit
            )
            source_unit, origin = _source_unit(
                declaration, reported_unit
            )
            transform = resolve_unit(source_unit, reported_unit)
            n_values = 0
            for row in rows:
                value = row.get(local_id)
                if isinstance(value, bool) or not isinstance(value, (int, float)):
                    continue
                converted = transform.convert_value(float(value))
                if not math.isfinite(converted):
                    raise ValueError(
                        f"{block.candidate.key}/{local_id} produced a "
                        "non-finite canonical value"
                    )
                row[local_id] = converted
                n_values += 1
            if role == "constraint" and isinstance(
                declaration.get("value"), (int, float)
            ):
                declaration["value"] = transform.convert_value(
                    float(declaration["value"])
                )
            record = _alignment_record(
                section=section,
                role=role,
                local_id=local_id,
                global_id=global_id,
                quantity_key=registry.quantity_key,
                source_unit=source_unit,
                source_unit_origin=origin,
                reported_unit=reported_unit,
                target_unit=target_unit,
                presentation=(
                    str(presentation)
                    if isinstance(presentation, str)
                    else None
                ),
                presentation_kind=(
                    kind.value if role == "property" else None
                ),
                materialization_required=(
                    presentation_requires_reference(kind)
                    if role == "property"
                    else False
                ),
                scale=float(transform.scale),
                offset=float(transform.offset),
                n_values=n_values,
            )
            declaration["unit_alignment"] = {
                key: record[key]
                for key in (
                    "from_unit",
                    "to_unit",
                    "target_unit",
                    "presentation_kind",
                    "materialization_required",
                    "status",
                    "scale",
                    "offset",
                )
            }
            records.append(record)

    return replace(
        block,
        projected=projected,
        rows=rows,
        units_aligned=True,
        unit_alignment=tuple(records),
    )


def align_gathered_block_units(
    blocks: list[AuthoritativeBlock],
) -> UnitAlignmentResult:
    """Unit-align gathered blocks independently and retain all failures."""
    aligned: list[AuthoritativeBlock] = []
    diagnostics: list[Diagnostic] = []
    report: list[dict[str, Any]] = []
    for block in blocks:
        try:
            normalized = align_authoritative_block_units(block)
            aligned.append(normalized)
            report.append(
                {
                    "source": {
                        "doi": normalized.candidate.doi,
                        "lit_num_id": normalized.candidate.lit_num_id,
                        "block_number": normalized.candidate.block_number,
                        "BLKsubsys_id": normalized.candidate.BLKsubsys_id,
                        "search_scope": normalized.candidate.search_scope,
                    },
                    "fields": list(normalized.unit_alignment),
                }
            )
        except Exception as exc:
            diagnostics.append(
                Diagnostic(
                    code="BLOCK_UNIT_ALIGNMENT_FAILED",
                    message=f"{type(exc).__name__}: {exc}",
                    stage="unit_alignment",
                    severity="warning",
                    source_key=block.candidate.key,
                )
            )
    return UnitAlignmentResult(
        blocks=aligned,
        diagnostics=diagnostics,
        report=report,
    )
