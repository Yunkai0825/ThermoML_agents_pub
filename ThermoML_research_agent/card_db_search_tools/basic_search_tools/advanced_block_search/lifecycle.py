"""Mandatory three-gate pre-execution lifecycle for ``block_search_adv``.

The gates deliberately separate catalog identity interpretation, exact PCS/registry
binding, and final executable intent.  Raw ThermoML rows are opened only after all
three content-addressed confirmations remain valid for the same request and DB state.
"""

from __future__ import annotations

import hashlib
import json
import secrets
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from . import catalogs as catalog_module
from .catalogs import RuntimeCatalogs
from .engine import (
    PreparedSearch,
    database_intent_summary,
    _RAW_EXECUTION_CAPABILITY,
    _execute_prepared_search,
    normalize_search_request,
    prepare_normalized_search,
)
from .errors import AdvancedSearchError, fail
from .flat_v2 import CompiledFlatRequest, compile_flat_request, public_error
from .models import NormalizedRequest, OccurrenceSelector

REVIEW_SCHEMA = "block_search_adv/preexecution-review-v1"
READY_SCHEMA = "block_search_adv/preexecution-ready-v1"
_COMPOSITE_PARAMETER = "composite_confirmation_token"
_DATABASE_PARAMETER = "database_intent_confirmation_token"
_EXECUTION_PARAMETER = "execution_confirmation_token"
_MAX_REVIEW_EXAMPLES = 8
_FLAT_DEFAULTS: dict[str, Any] = {
    "compounds": None,
    "compound_match": "all",
    "system_type": None,
    "system_scope": "declared",
    "system_size_min": None,
    "system_size_max": None,
    "parameters": None,
    "literature": None,
    "phases": None,
    "phase_match": "all",
    "fixed_constraints": None,
    "inline_state": None,
    "where": None,
    "minimum_common_points": 1,
    "calculate": None,
    "select": None,
    "having": None,
    "order_by": None,
    "limit": 50,
}


@dataclass
class LifecycleAssessment:
    compiled: CompiledFlatRequest
    catalogs: RuntimeCatalogs
    request: NormalizedRequest
    prepared: PreparedSearch | None
    review: dict[str, Any] | None
    confirmations: dict[str, str]


def _canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def _sha256(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def _token(prefix: str, value: Any) -> str:
    return f"{prefix}{_sha256(value)}"


def _same_token(received: Any, expected: str) -> bool:
    return isinstance(received, str) and secrets.compare_digest(received, expected)


def _file_state(path: Path) -> dict[str, Any]:
    try:
        stat = path.stat()
    except OSError as exc:
        fail(
            "DATABASE_UNAVAILABLE",
            f"Required Tool 12 database is unavailable at {path}.",
            "/",
            details={"error": str(exc)},
        )
    return {
        "path": str(path),
        "size": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
    }


def _format_dimension(dimension: Any) -> str:
    if dimension is None:
        return "quantity-specific/unknown"
    labels = ("M", "L", "T", "Theta", "N", "I")
    terms: list[str] = []
    for label, exponent in zip(labels, dimension):
        numerator = getattr(exponent, "numerator", exponent)
        denominator = getattr(exponent, "denominator", 1)
        if numerator == 0:
            continue
        rendered = str(numerator) if denominator == 1 else f"{numerator}/{denominator}"
        terms.append(label if rendered == "1" else f"{label}^{rendered}")
    return "1 (dimensionless)" if not terms else " ".join(terms)

def _selector_review(
    selector: OccurrenceSelector,
    request: NormalizedRequest,
    catalogs: RuntimeCatalogs,
) -> dict[str, Any]:
    row = selector.resolution.row
    component = (
        request.compounds.aliases[selector.component_ref]
        if selector.component_ref is not None
        else None
    )
    phase_component = (
        request.compounds.aliases[selector.phase_component_ref]
        if selector.phase_component_ref is not None
        else None
    )
    phase = (
        catalogs.phases_by_id.get(selector.phase_num_id)
        if selector.phase_num_id is not None
        else None
    )
    body = {
        "input_identity": selector.resolution.input_value,
        "input_catalog_role": selector.resolution.input_catalog_role,
        "requested_source_role": selector.source_role,
        "quantity_key": row.quantity_key,
        "preferred_name": row.preferred_name,
        "available_role_global_ids": {
            "property": row.prop_num_id,
            "variable": row.var_num_id,
            "constraint": row.constr_num_id,
        },
        "required_role_global_id": (
            row.global_id_for_role(selector.source_role)
            if selector.source_role != "inline_state"
            else None
        ),
        "component_linked": row.component_linked,
        "canonical_unit": row.semantics.canonical_unit,
        "dimension": _format_dimension(row.semantics.dimension),
        "semantic_type": row.semantics.semantic_type,
        "component": (
            {
                "alias": component.alias,
                "comp_num_id": component.record.comp_num_id,
                "name": component.record.common_name,
            }
            if component is not None
            else None
        ),
        "phase": (
            {
                "phase_num_id": phase.phase_num_id,
                "phase_id": phase.phase_id,
                "name": phase.phase_name,
            }
            if phase is not None
            else None
        ),
        "phase_component": (
            {
                "alias": phase_component.alias,
                "comp_num_id": phase_component.record.comp_num_id,
                "name": phase_component.record.common_name,
            }
            if phase_component is not None
            else None
        ),
        "minimum_finite_values": selector.min_finite_values,
        "minimum_distinct_values": selector.min_distinct_values,
        "cardinality": selector.cardinality,
        "condition_ast": selector.condition,
        "applies_to": selector.applies_to,
    }
    body["composite_selector_id"] = "ADVselector_" + _sha256(body)[:16]
    return {"alias": selector.alias, **body}


def _compound_review(request: NormalizedRequest) -> list[dict[str, Any]]:
    modes = (
        ("require", request.compounds.all_of),
        ("any", request.compounds.any_of),
        ("exclude", request.compounds.none_of),
    )
    return [
        {
            "mode": mode,
            "alias": selector.alias,
            "scope": selector.scope,
            **selector.record.as_dict(),
        }
        for mode, selectors in modes
        for selector in selectors
    ]


def _literature_review(
    request: NormalizedRequest,
    catalogs: RuntimeCatalogs,
) -> list[dict[str, Any]]:
    records: dict[str, Any] = {}
    for doi in request.literature.dois:
        record = catalogs.references_by_doi.get(doi)
        if record is not None:
            records[record.lit_num_id] = record
    for lit_num_id in request.literature.lit_num_ids:
        record = catalogs.references_by_id.get(lit_num_id)
        if record is not None:
            records[record.lit_num_id] = record
    return [
        {
            "lit_num_id": record.lit_num_id,
            "doi": record.doi,
            "lit_id": record.lit_id,
            "year": record.year,
            "first_author": record.first_author,
            "journal": record.journal,
        }
        for record in sorted(records.values(), key=lambda item: item.lit_num_id)
    ]


def _validate_semantic_annotations(
    request: NormalizedRequest,
) -> list[dict[str, Any]]:
    warnings: list[dict[str, Any]] = []
    excluded_aliases = {item.alias for item in request.compounds.none_of}
    excluded_phases = set(request.phases.none_of)
    for selector in request.row_selectors + request.fixed_selectors:
        row = selector.resolution.row
        if selector.source_role != "inline_state":
            required = row.global_id_for_role(selector.source_role)
            if required is None:
                fail(
                    "ROLE_UNAVAILABLE",
                    f"Quantity {row.quantity_key!r} has no {selector.source_role} representation.",
                    "/",
                    details={"alias": selector.alias},
                )
        for ref_name, ref in (
            ("component", selector.component_ref),
            ("phase_component", selector.phase_component_ref),
        ):
            if ref in excluded_aliases:
                fail(
                    "CONTRADICTORY_ID_ANNOTATION",
                    f"{selector.alias!r} uses excluded compound alias {ref!r} as {ref_name}.",
                    "/",
                )
        if selector.component_ref is not None and not row.component_linked:
            fail(
                "INVALID_COMPONENT_ANNOTATION",
                f"Quantity {row.quantity_key!r} is not component-linked but COMPONENT was supplied.",
                "/",
                details={"alias": selector.alias},
            )
        if selector.phase_num_id in excluded_phases:
            fail(
                "CONTRADICTORY_PHASE_ANNOTATION",
                f"{selector.alias!r} requires a phase excluded at block scope.",
                "/",
            )
        if (
            selector.resolution.input_catalog_role is not None
            and selector.resolution.input_catalog_role != selector.source_role
            and selector.source_role != "inline_state"
        ):
            warnings.append(
                {
                    "code": "CROSS_ROLE_TRANSLATION",
                    "alias": selector.alias,
                    "message": (
                        f"{selector.resolution.input_value} is a "
                        f"{selector.resolution.input_catalog_role} catalog ID, while this "
                        f"clause requests a {selector.source_role} occurrence. It resolves "
                        f"through quantity {row.quantity_key} to "
                        f"{row.global_id_for_role(selector.source_role)}."
                    ),
                }
            )
        if row.component_linked and selector.component_ref is None:
            warnings.append(
                {
                    "code": "COMPONENT_FANOUT_POSSIBLE",
                    "alias": selector.alias,
                    "message": (
                        f"{row.quantity_key} is component-linked but no COMPONENT qualifier "
                        "was supplied; CARDINALITY controls whether multiple occurrences bind."
                    ),
                }
            )
    return warnings


def _validate_literature_consistency(
    request: NormalizedRequest,
    catalogs: RuntimeCatalogs,
) -> None:
    if not request.literature.dois or not request.literature.lit_num_ids:
        return
    doi_ids = {
        record.lit_num_id
        for doi in request.literature.dois
        if (record := catalogs.references_by_doi.get(doi)) is not None
    }
    requested = set(request.literature.lit_num_ids)
    if doi_ids != requested:
        fail(
            "CONTRADICTORY_LITERATURE_IDS",
            "The DOI selectors and GLOBlit selectors must identify exactly the same literature records.",
            "/literature",
            details={
                "doi_lit_num_ids": sorted(doi_ids),
                "requested": sorted(requested),
                "missing_for_doi": sorted(doi_ids - requested),
                "extraneous_lit_num_ids": sorted(requested - doi_ids),
            },
        )


def _composite_payload(
    compiled: CompiledFlatRequest,
    catalogs: RuntimeCatalogs,
    request: NormalizedRequest,
) -> dict[str, Any]:
    _validate_literature_consistency(request, catalogs)
    warnings = _validate_semantic_annotations(request)
    phase_records = []
    for mode, phase_ids in (
        ("require", request.phases.all_of),
        ("any", request.phases.any_of),
        ("exclude", request.phases.none_of),
    ):
        for phase_id in phase_ids:
            phase = catalogs.phases_by_id[phase_id]
            phase_records.append(
                {
                    "mode": mode,
                    "phase_num_id": phase.phase_num_id,
                    "phase_id": phase.phase_id,
                    "name": phase.phase_name,
                }
            )
    return {
        "catalog_state": {
            "identity_index_schema": catalogs.identity_index_schema,
            "translation_filename": catalogs.translation_filename,
            "translation_sha256": catalogs.translation_sha256,
            "pcs_build_time": catalogs.pcs_build_time,
        },
        "compounds": _compound_review(request),
        "literature": _literature_review(request, catalogs),
        "block_phase_filters": phase_records,
        "selectors": [
            _selector_review(selector, request, catalogs)
            for selector in request.row_selectors + request.fixed_selectors
        ],
        "system": {
            "exact_system": request.compounds.exact_system,
            "system_types": list(request.compounds.system_types),
            "system_scope": request.compounds.system_scope,
            "system_size_min": request.compounds.system_size_min,
            "system_size_max": request.compounds.system_size_max,
        },
        "normalized_units_and_expressions": {
            "where": request.where,
            "minimum_common_points": compiled.public_query.get("minimum_common_points"),
            "calculate": compiled.public_query.get("calculate"),
            "select": compiled.public_query.get("select"),
            "having": compiled.public_query.get("having"),
            "order_by": compiled.public_query.get("order_by"),
        },
        "warnings": warnings,
    }


def _review(
    *,
    stage: str,
    stage_number: int,
    parameter: str,
    token: str,
    title: str,
    payload: dict[str, Any],
    invalid_received_token: bool,
    prior_confirmations: dict[str, str] | None = None,
) -> dict[str, Any]:
    prior = dict(prior_confirmations or {})
    required_parameters = [*prior.keys(), parameter]
    return {
        "schema": REVIEW_SCHEMA,
        "status": "confirmation_required",
        "stage": stage,
        "stage_number": stage_number,
        "title": title,
        "review": payload,
        "confirmation": {
            "parameter": parameter,
            "token": token,
            "required_prior_tokens": prior,
            "invalid_or_stale_token_received": invalid_received_token,
            "instruction": (
                "Inspect this stage, correct the chemistry or syntax if needed, then "
                f"resubmit the otherwise unchanged block_search_adv call alone with {parameter} exactly as shown"
                + (
                    " while STILL including the earlier confirmed token(s): "
                    + ", ".join(f"{key}={value}" for key, value in prior.items())
                    + ". Omitting any earlier token restarts the hierarchy at gate 1."
                    if prior
                    else "."
                )
            ),
            "all_required_token_parameters": required_parameters,
        },
        "raw_rows_read": False,
    }


def _final_payload(
    compiled: CompiledFlatRequest,
    request: NormalizedRequest,
    database_summary: Mapping[str, Any],
) -> dict[str, Any]:
    compound_modes = [
        {
            "mode": mode,
            "alias": item.alias,
            "scope": item.scope,
            "comp_num_id": item.record.comp_num_id,
            "name": item.record.common_name,
        }
        for mode, values in (
            ("require", request.compounds.all_of),
            ("any", request.compounds.any_of),
            ("exclude", request.compounds.none_of),
        )
        for item in values
    ]
    db_selectors = {
        item.get("alias"): item
        for item in database_summary.get("selectors", [])
        if isinstance(item, dict)
    }
    selector_intents = []
    for item in request.row_selectors + request.fixed_selectors:
        database_item = db_selectors.get(item.alias, {})
        selector_intents.append(
            {
                "alias": item.alias,
                "preferred_name": item.resolution.row.preferred_name,
                "quantity_key": item.resolution.row.quantity_key,
                "input_identity": item.resolution.input_value,
                "requested_source_role": item.source_role,
                "required_role_global_id": database_item.get(
                    "required_role_global_id"
                ),
                "component": database_item.get("component"),
                "phase": database_item.get("phase"),
                "phase_component": database_item.get("phase_component"),
                "condition_ast": item.condition,
                "applies_to": item.applies_to,
                "cardinality": item.cardinality,
                "minimum_finite_values": item.min_finite_values,
                "minimum_distinct_values": item.min_distinct_values,
                "actual_source_global_ids": database_item.get(
                    "actual_source_global_ids", []
                ),
                "property_observands": database_item.get(
                    "property_observands", []
                ),
            }
        )
    property_observands = [
        observand
        for selector in database_summary.get("selectors", [])
        if isinstance(selector, dict)
        for observand in selector.get("property_observands", [])
        if isinstance(observand, dict)
    ]
    return {
        "chemistry_intent_restatement": {
            "explanation": request.explanation,
            "compound_modes_and_scopes": compound_modes,
            "selectors": selector_intents,
            "block_phase_presence_filters": request.phases.as_dict(),
            "system_scope": request.compounds.system_scope,
            "system_types": list(request.compounds.system_types),
            "system_size": {
                "minimum": request.compounds.system_size_min,
                "maximum": request.compounds.system_size_max,
                "exact": request.compounds.exact_system,
            },
            "literature": request.literature.as_dict(),
            "where_ast": request.where,
            "fixed_and_inline_conditions": [
                {
                    "alias": item.alias,
                    "source_role": item.source_role,
                    "condition_ast": item.condition,
                    "applies_to": item.applies_to,
                }
                for item in request.fixed_selectors
            ],
            "calculations": compiled.public_query.get("calculate"),
            "selections": compiled.public_query.get("select"),
            "having": compiled.public_query.get("having"),
            "ordering": compiled.public_query.get("order_by"),
            "bound_property_observands": property_observands[:24],
            "important_scope_distinctions": [
                "Top-level phases require phase presence somewhere in a block; selector PHASE constrains that exact occurrence.",
                "Compound scope ANY is block membership; selector COMPONENT identifies the compound-specific occurrence.",
                "Property presentation and reference state qualify the observand beyond its GLOB property and phase IDs.",
            ],
        },
        "canonical_public_query": compiled.public_query,
        "executable_ast": request.as_dict(),
        "database_binding_counts": database_summary.get("counts"),
        "database_warnings": database_summary.get("warnings", []),
        "execution_limits": {
            "minimum_common_points": compiled.public_query.get(
                "minimum_common_points"
            ),
            "result_limit": request.limit,
        },
        "not_yet_established": [
            "common finite raw rows after WHERE",
            "calculated row values",
            "block aggregates and HAVING",
            "ranking order and final results",
        ],
    }

def assess_flat_search(
    *,
    composite_confirmation_token: str | None = None,
    database_intent_confirmation_token: str | None = None,
    execution_confirmation_token: str | None = None,
    **flat_kwargs: Any,
) -> LifecycleAssessment:
    """Return the next mandatory review, or a fully confirmed prepared search."""
    complete_flat_kwargs = {**_FLAT_DEFAULTS, **flat_kwargs}
    compiled = compile_flat_request(**complete_flat_kwargs)
    try:
        catalogs, request = normalize_search_request(**compiled.engine_kwargs)
        composite = _composite_payload(compiled, catalogs, request)
    except AdvancedSearchError as exc:
        raise public_error(exc) from exc

    composite_token = _token(
        "bsa_comp_",
        {
            "public_query": compiled.public_query,
            "normalized_request": request.as_dict(),
            "composite": composite,
        },
    )
    confirmations = {_COMPOSITE_PARAMETER: composite_token}
    if not _same_token(composite_confirmation_token, composite_token):
        return LifecycleAssessment(
            compiled,
            catalogs,
            request,
            None,
            _review(
                stage="composite_id_enrichment",
                stage_number=1,
                parameter=_COMPOSITE_PARAMETER,
                token=composite_token,
                title="Confirm catalog identities, role translations, units, and composite selectors",
                payload=composite,
                invalid_received_token=composite_confirmation_token is not None,
            ),
            confirmations,
        )

    try:
        prepared = prepare_normalized_search(catalogs, request)
        database = database_intent_summary(prepared)
    except AdvancedSearchError as exc:
        raise public_error(exc) from exc
    database_state = {
        "pcs": _file_state(catalog_module.PCS_DB),
        "pure_or_mixture_registry": _file_state(catalog_module.PM_REGISTRY_DB),
        "reaction_registry": _file_state(catalog_module.RXN_REGISTRY_DB),
    }
    database_token = _token(
        "bsa_db_",
        {
            "composite_token": composite_token,
            "database_state": database_state,
            "database_review": database,
        },
    )
    confirmations[_DATABASE_PARAMETER] = database_token
    database_payload = {"database_state": database_state, **database}
    if not _same_token(database_intent_confirmation_token, database_token):
        return LifecycleAssessment(
            compiled,
            catalogs,
            request,
            prepared,
            _review(
                stage="database_id_intent",
                stage_number=2,
                parameter=_DATABASE_PARAMETER,
                token=database_token,
                title="Confirm actual PCS/registry BLK bindings and observand metadata",
                payload=database_payload,
                invalid_received_token=database_intent_confirmation_token is not None,
                prior_confirmations={_COMPOSITE_PARAMETER: composite_token},
            ),
            confirmations,
        )

    final = _final_payload(compiled, request, database)
    raw_state = _file_state(catalog_module.RAW_DB)
    execution_token = _token(
        "bsa_final_",
        {
            "composite_token": composite_token,
            "database_token": database_token,
            "raw_database_state": raw_state,
            "final_review": final,
        },
    )
    confirmations[_EXECUTION_PARAMETER] = execution_token
    final_payload = {"raw_database_state": raw_state, **final}
    if not _same_token(execution_confirmation_token, execution_token):
        return LifecycleAssessment(
            compiled,
            catalogs,
            request,
            prepared,
            _review(
                stage="final_intent_and_syntax",
                stage_number=3,
                parameter=_EXECUTION_PARAMETER,
                token=execution_token,
                title="Confirm final chemistry intent, syntax, operations, and execution limits",
                payload=final_payload,
                invalid_received_token=execution_confirmation_token is not None,
                prior_confirmations={
                    _COMPOSITE_PARAMETER: composite_token,
                    _DATABASE_PARAMETER: database_token,
                },
            ),
            confirmations,
        )

    return LifecycleAssessment(
        compiled,
        catalogs,
        request,
        prepared,
        None,
        confirmations,
    )


def review_or_execute_flat_search(**kwargs: Any) -> dict[str, Any]:
    """Run the mandatory review hierarchy automatically, then execute.

    The three pre-execution gates remain content-addressed and fail-closed,
    but the framework — not the calling agent — performs the confirmation
    resubmissions. One public call therefore either raises a specific
    validation error or executes the fully reviewed plan and returns raw
    rows together with the confirmed review evidence.
    """
    # Agent-supplied tokens are obsolete; the hierarchy is walked internally.
    for legacy in (_COMPOSITE_PARAMETER, _DATABASE_PARAMETER, _EXECUTION_PARAMETER):
        kwargs.pop(legacy, None)

    tokens: dict[str, str] = {}
    assessment: LifecycleAssessment | None = None
    for _ in range(4):
        assessment = assess_flat_search(**kwargs, **tokens)
        if assessment.review is None:
            break
        confirmation = assessment.review["confirmation"]
        parameter = confirmation["parameter"]
        token = confirmation["token"]
        if tokens.get(parameter) == token:
            raise RuntimeError(
                "block_search_adv automatic review hierarchy did not advance "
                f"past stage {assessment.review.get('stage')!r}"
            )
        tokens[parameter] = token
    if assessment is None or assessment.review is not None:
        raise RuntimeError(
            "block_search_adv automatic review hierarchy failed to confirm "
            "all three gates"
        )
    if assessment.prepared is None:
        raise RuntimeError("confirmed block_search_adv plan has no prepared search")
    result = _execute_prepared_search(
        assessment.prepared,
        capability=_RAW_EXECUTION_CAPABILITY,
    )
    result["normalized_query"] = assessment.compiled.public_query
    result["preexecution_review"] = {
        "schema": READY_SCHEMA,
        "confirmed_stages": [
            "composite_id_enrichment",
            "database_id_intent",
            "final_intent_and_syntax",
        ],
        "confirmation_tokens": assessment.confirmations,
        "raw_execution_authorized": True,
        "automatic_confirmation": True,
    }
    return result


def render_review_markdown(review: Mapping[str, Any]) -> str:
    """Render bounded, deterministic ReAct guidance for a blocked tool call."""
    stage = review.get("stage", "unknown")
    title = review.get("title", "Tool 12 confirmation required")
    body = review.get("review") if isinstance(review.get("review"), dict) else {}
    confirmation = review.get("confirmation") if isinstance(review.get("confirmation"), dict) else {}
    lines = [
        f"## block_search_adv pre-execution gate {review.get('stage_number')}/3: {title}",
        "",
        "The tool has **not executed raw ThermoML data**. Review the hard-parsed evidence below.",
        "",
    ]
    if stage == "composite_id_enrichment":
        lines.append(f"- Compounds: `{_canonical_json(body.get('compounds', []))}`")
        lines.append(f"- Literature IDs: `{_canonical_json(body.get('literature', []))}`")
        lines.append(f"- System intent: `{_canonical_json(body.get('system', {}))}`")
        lines.append(
            f"- Block phase-presence filters: `{_canonical_json(body.get('block_phase_filters', []))}`"
        )
        for selector in body.get("selectors", [])[:16]:
            lines.append(
                "- `{alias}`: `{input_identity}` ({input_catalog_role}) -> "
                "{requested_source_role} `{required_role_global_id}`; **{preferred_name}**; "
                "unit `{canonical_unit}`, dimension `{dimension}`; composite "
                "`{composite_selector_id}`; component `{component}`; phase `{phase}`; "
                "condition `{condition_ast}`; applies-to `{applies_to}`.".format(**selector)
            )
        lines.append(
            "- Normalized expressions/units: `"
            + _canonical_json(body.get("normalized_units_and_expressions", {}))
            + "`"
        )
        for warning in body.get("warnings", [])[:12]:
            lines.append(f"- Warning `{warning.get('code')}`: {warning.get('message')}")
    elif stage == "database_id_intent":
        counts = body.get("counts", {})
        lines.append(
            "- Candidate counts: registry={registry_candidates}, PCS exact={card_exact_candidates}, "
            "bindable={bindable_blocks}, combinations={binding_combinations}.".format(**counts)
        )
        lines.append(
            f"- Progressive-count scope: {body.get('selector_stage_counts_scope')}"
        )
        for selector in body.get("selectors", [])[:16]:
            lines.append(
                f"- `{selector.get('alias')}` requested/effective IDs: "
                f"required={selector.get('required_role_global_id')}, "
                f"available={selector.get('effective_quantity_global_ids')}, "
                f"actual={selector.get('actual_source_global_ids')} across "
                f"{selector.get('n_distinct_database_occurrences')} occurrences; "
                f"progressive counts={selector.get('stage_counts')}; "
                f"note={selector.get('source_global_id_note')}."
            )
            for example in selector.get("examples", [])[:2]:
                lines.append(
                    f"  - `{example.get('lit_num_id')}` / {example.get('doi')} / "
                    f"`{example.get('block_id')}` / `{example.get('BLKsubsys_id')}` / "
                    f"`{example.get('source_local_key')}`; role={example.get('source_role')}, "
                    f"component={example.get('comp_num_id')}, phase={example.get('phase_num_id')}, "
                    f"n={example.get('n_values')}, unique={example.get('n_unique')}, "
                    f"range={example.get('min')}..{example.get('max')}, "
                    f"constant={example.get('constant_value')}, "
                    f"property_context={example.get('property_context')}."
                )
        for preview in body.get("blocks_preview", [])[:8]:
            lines.append(
                f"- Bindable block: `{_canonical_json(preview.get('block', {}))}`; "
                f"combinations={preview.get('n_binding_combinations')}."
            )
        for warning in body.get("warnings", [])[:12]:
            lines.append(
                f"- Warning `{warning.get('code')}`: {warning.get('message')}; "
                f"examples={warning.get('examples')}."
            )
    else:
        restatement = body.get("chemistry_intent_restatement", {})
        lines.extend(
            [
                f"- Goal: {restatement.get('explanation')}",
                f"- Compound modes/scopes: `{_canonical_json(restatement.get('compound_modes_and_scopes', []))}`",
                f"- Quantity roles, phases, components, conditions, and observands: `{_canonical_json(restatement.get('selectors', []))}`",
                f"- Block phase-presence filters: `{_canonical_json(restatement.get('block_phase_presence_filters', {}))}`",
                f"- System: scope={restatement.get('system_scope')}, types={restatement.get('system_types')}, size={restatement.get('system_size')}",
                f"- Literature IDs: `{_canonical_json(restatement.get('literature', {}))}`",
                f"- WHERE AST: `{_canonical_json(restatement.get('where_ast'))}`",
                f"- Fixed/inline state conditions: `{_canonical_json(restatement.get('fixed_and_inline_conditions', []))}`",
                f"- Calculations/select/HAVING/order: `{_canonical_json({'calculate': restatement.get('calculations'), 'select': restatement.get('selections'), 'having': restatement.get('having'), 'order_by': restatement.get('ordering')})}`",
                f"- Bound property presentation/reference states: `{_canonical_json(restatement.get('bound_property_observands', []))}`",
                f"- Scope distinctions: {restatement.get('important_scope_distinctions')}",
                f"- Database warnings still requiring judgment: `{_canonical_json(body.get('database_warnings', []))}`",
                f"- Raw execution will establish only now: {body.get('not_yet_established')}",
                f"- Canonical public query: `{_canonical_json(body.get('canonical_public_query'))}`",
            ]
        )
    prior_tokens = confirmation.get("required_prior_tokens")
    prior_clause = ""
    if isinstance(prior_tokens, Mapping) and prior_tokens:
        rendered_prior = ", ".join(
            f"`{key}={value}`" for key, value in prior_tokens.items()
        )
        prior_clause = (
            " You MUST also keep the earlier confirmed token(s) in the same call: "
            f"{rendered_prior}. Omitting any earlier token restarts the hierarchy at gate 1."
        )
    footer = (
        "\n\nResubmit this tool call **alone** with "
        f"`{confirmation.get('parameter')}={confirmation.get('token')}` after "
        "confirming the evidence."
        + prior_clause
        + " Changing any chemistry or syntax argument "
        "invalidates the tokens and restarts the hierarchy."
    )
    body_text = "\n".join(lines)
    body_limit = max(0, 32_000 - len(footer))
    if len(body_text) > body_limit:
        marker = "\n\n[Review evidence truncated; confirmation footer preserved.]"
        body_text = body_text[: max(0, body_limit - len(marker))].rstrip() + marker
    return body_text + footer


def validate_block_search_adv_batch(
    tool_calls: list[dict[str, Any]],
) -> str | None:
    """Require every advanced-search lifecycle call to occupy its own batch."""
    if len(tool_calls) <= 1 or not any(
        call.get("name") == "block_search_adv" for call in tool_calls
    ):
        return None
    return (
        "### Tool batch rejected before execution\n\n"
        "**✗ block_search_adv**\n\n"
        "`block_search_adv` is a state-bound review lifecycle and must be the "
        "only tool call in its batch, including the final confirmed execution. "
        "Retry it alone so its review evidence and token cannot be confused "
        "with sibling results. No tool in this batch executed."
    )

def validate_block_search_adv_guidance(
    *,
    tool_name: str,
    call_kwargs: dict[str, Any],
    **_kwargs: Any,
) -> str | None:
    """True pre-execution hook: nonempty guidance prevents callable execution.

    The review hierarchy itself is walked automatically inside the tool, so
    this hook only fails fast on invalid chemistry/syntax arguments; a
    parseable call is released for execution with no agent-facing gates.
    """
    if tool_name != "block_search_adv":
        return None
    kwargs = dict(call_kwargs)
    kwargs.pop("purpose", None)
    kwargs.pop("tasks", None)
    for legacy in (_COMPOSITE_PARAMETER, _DATABASE_PARAMETER, _EXECUTION_PARAMETER):
        kwargs.pop(legacy, None)
    try:
        assess_flat_search(**kwargs)
    except AdvancedSearchError as exc:
        error = public_error(exc)
        return (
            "## block_search_adv pre-execution validation failed\n\n"
            f"- `{error.code}` at `{error.pointer}`: {error.message}\n"
            f"- Details: `{_canonical_json(error.details)}`\n\n"
            "Correct the arguments and call `block_search_adv` alone. No raw rows were read."
        )
    return ""


__all__ = [
    "READY_SCHEMA",
    "REVIEW_SCHEMA",
    "assess_flat_search",
    "render_review_markdown",
    "review_or_execute_flat_search",
    "validate_block_search_adv_batch",
    "validate_block_search_adv_guidance",
]
