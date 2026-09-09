"""ReAct helpers — strict tool-argument and result-contract validation."""

from __future__ import annotations

import inspect
import json
import logging
import types
from dataclasses import dataclass, field
from typing import Any, Callable, Literal, Union, get_args, get_origin, get_type_hints

from ..engine_config import get_config
from ...general_text_context_marker_catalog import MARKERS, wrap_subagent_answer
from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    annotate_dois_with_lit_num_ids,
    attach_lit_num_ids,
    validate_nested_identifiers,
)

log = logging.getLogger("ThermoML-UI")

# Adaptive compaction threshold — when the flat prompt exceeds this
# many chars, trigger the LLM-driven compaction cycle.  This is NOT
# a hard cap; it's a heuristic trigger.  The LLM decides what to
# compress (if anything) via the 3-step select→compress→validate cycle.


def _get_compaction_trigger_chars() -> int:
    """Return the active COMPACTION_TRIGGER_CHARS from agent config."""
    return get_config().COMPACTION_TRIGGER_CHARS


# ═══════════════════════════════════════════════════════════════
#  Strict tool-argument validation
# ═══════════════════════════════════════════════════════════════

def _annotation_accepts(value: object, annotation: object) -> bool:
    """Check a decoded JSON value without coercing it to the annotation."""
    if annotation in {inspect.Parameter.empty, Any, object}:
        return True
    origin = get_origin(annotation)
    if origin in {Union, types.UnionType}:
        return any(_annotation_accepts(value, item) for item in get_args(annotation))
    if origin is Literal:
        return value in get_args(annotation)
    if origin is list:
        args = get_args(annotation)
        return isinstance(value, list) and (
            not args or all(_annotation_accepts(item, args[0]) for item in value)
        )
    if origin is dict:
        args = get_args(annotation)
        return isinstance(value, dict) and (
            len(args) != 2
            or all(
                _annotation_accepts(key, args[0])
                and _annotation_accepts(item, args[1])
                for key, item in value.items()
            )
        )
    if origin is tuple:
        # JSON arrays decode to lists. Agent-facing interfaces must annotate
        # arrays as list[...] rather than relying on tuple coercion.
        return False
    if origin is set:
        return False
    if annotation is bool:
        return isinstance(value, bool)
    if annotation is int:
        return isinstance(value, int) and not isinstance(value, bool)
    if annotation is float:
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if annotation is str:
        return isinstance(value, str)
    if annotation is type(None):
        return value is None
    return isinstance(value, annotation) if isinstance(annotation, type) else True


def _validate_tool_arguments(tool_name: str, args: dict, fn: Callable) -> dict:
    """Return exact, type-valid tool arguments or raise a refinement error.

    Tool parameter names are part of the public contract. They are never
    case-folded, aliased, or silently dropped.
    """
    if not isinstance(args, dict):
        raise TypeError(
            f"TOOL_ARGUMENT_REFINEMENT_REQUIRED: {tool_name} arguments must be an object"
        )
    sig = inspect.signature(fn)
    valid_params = set(sig.parameters)

    unsupported = [
        name
        for name, parameter in sig.parameters.items()
        if parameter.kind in {
            inspect.Parameter.VAR_POSITIONAL,
            inspect.Parameter.VAR_KEYWORD,
        }
    ]
    if unsupported:
        raise TypeError(
            f"TOOL_INTERFACE_CONTRACT_ERROR: {tool_name} exposes variadic "
            f"parameter(s) {unsupported}; every agent-facing parameter must be declared"
        )

    unknown = sorted(set(args) - valid_params)
    if unknown:
        accepted = sorted(
            name for name, param in sig.parameters.items()
            if param.kind not in {
                inspect.Parameter.VAR_POSITIONAL,
                inspect.Parameter.VAR_KEYWORD,
            }
        )
        raise TypeError(
            f"TOOL_ARGUMENT_REFINEMENT_REQUIRED: {tool_name} received undeclared "
            f"parameter(s) {unknown}; accepted parameters are {accepted}"
        )
    try:
        sig.bind(**args)
    except TypeError as exc:
        raise TypeError(
            f"TOOL_ARGUMENT_REFINEMENT_REQUIRED: invalid call to {tool_name}: {exc}"
        ) from exc

    annotation_target = fn
    if (
        not inspect.isfunction(fn)
        and not inspect.ismethod(fn)
        and not inspect.isclass(fn)
    ):
        annotation_target = fn.__call__
    try:
        annotations = get_type_hints(annotation_target)
    except (NameError, TypeError) as exc:
        raise TypeError(
            f"TOOL_INTERFACE_CONTRACT_ERROR: cannot resolve annotations for "
            f"{tool_name}: {exc}"
        ) from exc
    for name, value in args.items():
        annotation = annotations.get(name, sig.parameters[name].annotation)
        if not _annotation_accepts(value, annotation):
            raise TypeError(
                f"TOOL_ARGUMENT_REFINEMENT_REQUIRED: {tool_name}.{name} received "
                f"{value!r} ({type(value).__name__}); expected {annotation!r}; "
                "tool arguments are never coerced"
            )
    return dict(args)


def require_result_within_limit(tool_name: str, text: str) -> str:
    """Soft size gate: oversized results are delivered with a visible warning.

    The full result always reaches the agent — completed tool work is never
    replaced by an error. The banner makes an under-powered compaction
    pipeline visible to both the agent and the run logs.
    """
    cfg = get_config()
    if len(text) > cfg.TOOL_RESULT_CHAR_LIMIT:
        log.warning(
            "Tool %s result is %s chars (target %s) — delivering with a size "
            "warning banner; tighten its compaction pipeline",
            tool_name, f"{len(text):,}", f"{cfg.TOOL_RESULT_CHAR_LIMIT:,}",
        )
        return (
            f"[TOOL_RESULT_SIZE_WARNING: {tool_name} returned {len(text):,} "
            f"characters after result processing; the target is "
            f"{cfg.TOOL_RESULT_CHAR_LIMIT:,}. The full result follows — prefer "
            "narrower requests, and rely on your working memory for recall "
            "instead of re-running this call.]\n\n" + text
        )
    return text


def validate_native_tool_result(tool_name: str, result: object) -> dict | str:
    """Require native result types, DOI/literature pairs, and current IDs.

    Every registered ThermoML DOI is enriched with its sibling
    ``lit_num_id`` before the result enters tool history, compaction, working
    memory, or the next agent context. JSON strings are enriched
    structurally; compact markdown/plain text is annotated in place.
    """
    if not isinstance(tool_name, str) or not tool_name:
        raise TypeError("tool_name must be a non-empty string")
    if isinstance(result, str):
        if not result.strip():
            raise ValueError(f"TOOL_RESULT_CONTRACT_ERROR: {tool_name} returned empty text")
        stripped = result.strip()
        subagent_match = MARKERS.subagent_answer_re.fullmatch(stripped)
        if subagent_match:
            try:
                parsed = json.loads(subagent_match.group(1).strip())
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"TOOL_RESULT_CONTRACT_ERROR: {tool_name} returned a "
                    "subagent_answer marker without valid JSON"
                ) from exc
            if not isinstance(parsed, (dict, list)):
                raise TypeError(
                    f"TOOL_RESULT_CONTRACT_ERROR: {tool_name} subagent_answer "
                    "JSON must be an object or array"
                )
            enriched = attach_lit_num_ids(
                parsed,
                path=f"tool_result[{tool_name}].subagent_answer",
            )
            validate_nested_identifiers(
                enriched,
                path=f"tool_result[{tool_name}].subagent_answer",
            )
            return wrap_subagent_answer(enriched)
        if stripped[:1] in {"{", "["}:
            try:
                parsed = json.loads(stripped)
            except json.JSONDecodeError:
                return annotate_dois_with_lit_num_ids(result)
            enriched = attach_lit_num_ids(
                parsed,
                path=f"tool_result[{tool_name}]",
            )
            validate_nested_identifiers(
                enriched,
                path=f"tool_result[{tool_name}]",
            )
            return json.dumps(enriched, indent=2, ensure_ascii=False)
        return annotate_dois_with_lit_num_ids(result)
    if not isinstance(result, dict):
        raise TypeError(
            f"TOOL_RESULT_CONTRACT_ERROR: {tool_name} returned "
            f"{type(result).__name__}; agent-facing tools must return dict or str"
        )
    enriched = attach_lit_num_ids(
        result,
        path=f"tool_result[{tool_name}]",
    )
    if not isinstance(enriched, dict):
        raise AssertionError("DOI/literature enrichment changed object result type")
    result = enriched
    if "error_code" in result:
        if not isinstance(result["error_code"], str) or not result["error_code"]:
            raise TypeError(f"{tool_name} error_code must be a non-empty string")
        if "error" not in result or not isinstance(result["error"], str):
            raise ValueError(f"{tool_name} structured error must contain string field 'error'")
        if result["error_code"] == "ID_REFINEMENT_REQUIRED":
            refinement = result["refinement"] if "refinement" in result else None
            required = {"field", "received", "expected", "reason"}
            if not isinstance(refinement, dict) or set(refinement) != required:
                raise ValueError(
                    f"{tool_name} ID refinement must contain exactly {sorted(required)}"
                )
        return result
    validate_nested_identifiers(result, path=f"tool_result[{tool_name}]")
    return result


# ═══════════════════════════════════════════════════════════════
#  AgentTurnResult dataclass
# ═══════════════════════════════════════════════════════════════

@dataclass
class AgentTurnResult:
    """Result of a single agent_turn() execution."""
    answer: str
    iterations: int
    elapsed_seconds: float
    tool_history: list[dict] = field(default_factory=list)
    timed_out: bool = False
    final_context: str = ""
    session_dir: str | None = None
    round_number: int = 1
    working_memory: Any = field(default=None, repr=False)
    verdict: str | None = None
