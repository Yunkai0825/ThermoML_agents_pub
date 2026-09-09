"""Bounded deterministic Markdown compactor for ``block_search_adv``."""

from __future__ import annotations

import json
import math
from typing import Any

from NIST_ThermoML_agents.general_db_query_engine.general_tool_management_helpers.general_agent_tool_catalog import (
    compacts,
)
from card_db_search_tools.basic_search_tools.advanced_block_search.lifecycle import (
    REVIEW_SCHEMA,
    render_review_markdown,
)


_RESULT_SCHEMA = "block_search_adv/result-v1"
_ERROR_SCHEMA = "block_search_adv/error-v1"
_MAX_COMPACT_CHARS = 32_000
_MAX_BLOCKS_RENDERED = 100
_MAX_BINDING_MATCHES_RENDERED = 160
_MAX_BINDINGS_PER_MATCH = 12
_MAX_FIXED_FILTERS_PER_MATCH = 12
_MAX_SELECTED_PER_MATCH = 12
_MAX_ORDER_KEYS_PER_MATCH = 12
_MAX_ALIAS_RESOLUTIONS = 24
_FOOTER_RESERVE = 420


def _require_object(value: Any, context: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise TypeError(f"{context} must be an object")
    return value


def _require_array(value: Any, context: str) -> list[Any]:
    if not isinstance(value, list):
        raise TypeError(f"{context} must be an array")
    return value


def _require_nonnegative_int(value: Any, context: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise TypeError(f"{context} must be a non-negative integer")
    return value


def _require_bool(value: Any, context: str) -> bool:
    if not isinstance(value, bool):
        raise TypeError(f"{context} must be a boolean")
    return value


def _require_nonempty_string(value: Any, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise TypeError(f"{context} must be a non-empty string")
    return value


def _require_fields(row: dict[str, Any], fields: tuple[str, ...], context: str) -> None:
    missing = [field for field in fields if field not in row]
    if missing:
        raise ValueError(f"{context} is missing required fields {missing}")


def _format_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("block_search_adv compact output contains a non-finite number")
        return f"{value:.12g}"
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _markdown_text(value: Any, *, max_chars: int) -> str:
    text = _format_scalar(value).replace("\r", " ").replace("\n", " ")
    if len(text) > max_chars:
        text = text[: max_chars - 1].rstrip() + "…"
    return text


def _value_with_unit(value: Any) -> str:
    if isinstance(value, dict) and "value" in value:
        rendered = _format_scalar(value["value"])
        unit = value.get("unit")
        if unit not in (None, ""):
            rendered += f" {_format_scalar(unit)}"
        return rendered
    return _format_scalar(value)


class _BoundedWriter:
    def __init__(self, limit: int) -> None:
        self._limit = limit
        self._lines: list[str] = []
        self._chars = 0

    def append(self, line: str = "", *, reserve: int = 0) -> bool:
        if not isinstance(line, str):
            raise TypeError("Markdown line must be text")
        addition = len(line) + (1 if self._lines else 0)
        # Keep one character for the final newline emitted by ``render``.
        if self._chars + addition + reserve + 1 > self._limit:
            return False
        self._lines.append(line)
        self._chars += addition
        return True

    def render(self) -> str:
        text = "\n".join(self._lines).rstrip() + "\n"
        if len(text) > self._limit:
            raise AssertionError("bounded Markdown writer exceeded its character limit")
        return text


def _format_binding(binding_alias: str, binding: Any) -> str:
    info = _require_object(binding, f"binding {binding_alias!r}")
    _require_fields(
        info,
        ("source_role", "occurrence_key"),
        f"binding {binding_alias!r}",
    )
    source_role = _require_nonempty_string(
        info["source_role"], f"binding {binding_alias!r}.source_role"
    )
    occurrence_key = _require_nonempty_string(
        info["occurrence_key"], f"binding {binding_alias!r}.occurrence_key"
    )
    if not occurrence_key.startswith(f"{source_role}|"):
        raise ValueError(
            f"binding {binding_alias!r} occurrence_key does not agree with source_role"
        )

    input_identity = (
        info.get("input_identity")
        or info.get("input_global_id")
        or info.get("input_alias")
    )
    left = _format_scalar(input_identity) if input_identity else binding_alias
    rendered = f"{left} → {occurrence_key}"

    source_global_id = (
        info.get("source_global_id")
        or info.get("source_num_id")
        or info.get("source_prop_num_id")
        or info.get("source_var_num_id")
        or info.get("source_constr_num_id")
    )
    annotations: list[str] = []
    if source_global_id:
        annotations.append(f"source={_format_scalar(source_global_id)}")
    if info.get("input_catalog_role"):
        annotations.append(
            f"input_role={_format_scalar(info['input_catalog_role'])}"
        )
    if info.get("translated_quantity_key"):
        annotations.append(
            f"quantity={_format_scalar(info['translated_quantity_key'])}"
        )
    if info.get("comp_num_id"):
        annotations.append(f"component={_format_scalar(info['comp_num_id'])}")
    if info.get("phase_num_id"):
        annotations.append(f"phase={_format_scalar(info['phase_num_id'])}")
    if info.get("phase_component_comp_num_id"):
        annotations.append(
            "phase_component="
            + _format_scalar(info["phase_component_comp_num_id"])
        )
    if info.get("applies_to_occurrence_key"):
        annotations.append(
            "applies_to="
            + _format_scalar(info["applies_to_occurrence_key"])
        )
    if annotations:
        rendered += " [" + "; ".join(annotations) + "]"
    return rendered


def _format_bindings(bindings: Any) -> str:
    rows = _require_object(bindings, "binding match bindings")
    parts: list[str] = []
    for alias, binding in list(rows.items())[:_MAX_BINDINGS_PER_MATCH]:
        parts.append(_format_binding(str(alias), binding))
    omitted = len(rows) - len(parts)
    if omitted:
        parts.append(f"+{omitted} binding(s)")
    return "; ".join(parts) if parts else "—"


def _format_fixed_filter(item: Any, index: int) -> str:
    evidence = _require_object(item, f"fixed_filter_evidence[{index}]")
    _require_fields(
        evidence,
        ("source_role", "occurrence_key"),
        f"fixed_filter_evidence[{index}]",
    )
    source_role = _require_nonempty_string(
        evidence["source_role"], f"fixed_filter_evidence[{index}].source_role"
    )
    occurrence_key = _require_nonempty_string(
        evidence["occurrence_key"], f"fixed_filter_evidence[{index}].occurrence_key"
    )
    if not occurrence_key.startswith(f"{source_role}|"):
        raise ValueError(
            f"fixed_filter_evidence[{index}] occurrence_key does not agree with source_role"
        )

    request_ref = evidence.get("request_ref") or evidence.get("alias")
    if request_ref:
        rendered = (
            f"{source_role}:{_format_scalar(request_ref)} "
            f"[{occurrence_key}]"
        )
    else:
        rendered = occurrence_key
    if "value" in evidence:
        rendered += f"={_value_with_unit(evidence)}"
    if "predicate_outcome" in evidence:
        outcome = _require_bool(
            evidence["predicate_outcome"],
            f"fixed_filter_evidence[{index}].predicate_outcome",
        )
        rendered += " ✓" if outcome else " ✗"
    applies_to = evidence.get("applies_to_occurrence_key")
    if applies_to:
        rendered += f" → applies_to {_format_scalar(applies_to)}"
    return rendered


def _format_fixed_filters(filters: Any) -> str:
    rows = _require_array(filters, "binding match fixed_filter_evidence")
    parts = [
        _format_fixed_filter(item, index)
        for index, item in enumerate(rows[:_MAX_FIXED_FILTERS_PER_MATCH])
    ]
    omitted = len(rows) - len(parts)
    if omitted:
        parts.append(f"+{omitted} gate(s)")
    return "; ".join(parts) if parts else "—"


def _format_selected(selected: Any) -> str:
    values = _require_object(selected, "binding match selected")
    parts = [
        f"{alias}={_value_with_unit(value)}"
        for alias, value in list(values.items())[:_MAX_SELECTED_PER_MATCH]
    ]
    omitted = len(values) - len(parts)
    if omitted:
        parts.append(f"+{omitted} selected value(s)")
    return "; ".join(parts) if parts else "—"


def _format_order_keys(order_keys: Any) -> str:
    values = _require_array(order_keys, "binding match order_keys")
    parts = [
        f"{index + 1}:{_format_scalar(value)}"
        for index, value in enumerate(values[:_MAX_ORDER_KEYS_PER_MATCH])
    ]
    omitted = len(values) - len(parts)
    if omitted:
        parts.append(f"+{omitted} key(s)")
    return ", ".join(parts) if parts else "natural typed-block order"


def _format_alias_resolution(item: Any, index: int) -> str:
    value = _require_object(item, f"alias_resolution[{index}]")
    _require_fields(
        value,
        ("alias", "input", "quantity_key", "required_source_role"),
        f"alias_resolution[{index}]",
    )
    rendered = (
        f"{_format_scalar(value['alias'])}: "
        f"{_format_scalar(value['input'])} → "
        f"{_format_scalar(value['quantity_key'])} "
        f"[requires {_format_scalar(value['required_source_role'])}]"
    )
    role_id = value.get("required_role_global_id")
    if role_id:
        rendered += f" ({_format_scalar(role_id)})"
    return rendered


def _format_trace(trace: Any) -> str:
    values = _require_object(trace, "binding match match_trace")
    names = (
        "point_scope", "BLKsubsys_id", "parent_rows",
        "rows_before_where", "rows_after_where", "complete_rows", "having",
    )
    parts = []
    for name in names:
        if name in values:
            if name == "having":
                value = _require_bool(values[name], f"match_trace.{name}")
            elif name in {
                "parent_rows", "rows_before_where", "rows_after_where",
                "complete_rows",
            }:
                value = _require_nonnegative_int(values[name], f"match_trace.{name}")
            else:
                value = values[name]
            parts.append(f"{name}={_format_scalar(value)}")
    return ", ".join(parts) if parts else "—"


def _compact_error(data: dict[str, Any]) -> str:
    _require_fields(
        data,
        ("schema", "error", "results", "diagnostics"),
        "block_search_adv error result",
    )
    if data["schema"] != _ERROR_SCHEMA:
        raise ValueError(
            f"block_search_adv error schema must be {_ERROR_SCHEMA!r}, "
            f"got {data['schema']!r}"
        )
    error = _require_object(data["error"], "block_search_adv.error")
    _require_fields(
        error,
        ("code", "message", "pointer"),
        "block_search_adv.error",
    )
    code = _require_nonempty_string(error["code"], "block_search_adv.error.code")
    message = _require_nonempty_string(
        error["message"], "block_search_adv.error.message"
    )
    pointer = _require_nonempty_string(
        error["pointer"], "block_search_adv.error.pointer"
    )
    if _require_array(data["results"], "block_search_adv error results"):
        raise ValueError("block_search_adv error results must be an empty array")
    _require_object(data["diagnostics"], "block_search_adv error diagnostics")
    if "details" in error:
        _require_object(error["details"], "block_search_adv.error.details")

    writer = _BoundedWriter(_MAX_COMPACT_CHARS)
    writer.append(f"# block_search_adv — {code}")
    writer.append()
    writer.append(f"**Error:** {_markdown_text(message, max_chars=2_000)}")
    writer.append(f"**JSON pointer:** `{_markdown_text(pointer, max_chars=500)}`")
    if data.get("search_explanation"):
        explanation = _require_nonempty_string(
            data["search_explanation"],
            "block_search_adv error search_explanation",
        )
        writer.append(
            f"**Search explanation:** {_markdown_text(explanation, max_chars=600)}"
        )
    if error.get("details") not in (None, {}, []):
        details = _markdown_text(error["details"], max_chars=6_000)
        writer.append(f"**Details:** `{details}`")
    return writer.render()


@compacts("block_search_adv")
def compact_block_search_adv(data: dict[str, Any]) -> str:
    """Render deduplicated advanced block-search results as bounded Markdown."""
    payload = _require_object(data, "block_search_adv result")
    if "error" in payload:
        return _compact_error(payload)
    if payload.get("schema") == REVIEW_SCHEMA:
        return render_review_markdown(payload)

    _require_fields(payload, ("schema", "results"), "block_search_adv result")
    if payload["schema"] != _RESULT_SCHEMA:
        raise ValueError(
            f"block_search_adv schema must be {_RESULT_SCHEMA!r}, "
            f"got {payload['schema']!r}"
        )
    results = _require_array(payload["results"], "block_search_adv.results")
    n_results = payload.get("n_results", len(results))
    n_results = _require_nonnegative_int(n_results, "block_search_adv.n_results")
    if n_results != len(results):
        raise ValueError(
            f"block_search_adv.n_results={n_results} does not match "
            f"{len(results)} deduplicated block results"
        )
    truncated = _require_bool(
        payload.get("truncated", False), "block_search_adv.truncated"
    )
    diagnostics = _require_object(
        payload.get("diagnostics", {}), "block_search_adv.diagnostics"
    )

    validated_rows: list[tuple[dict[str, Any], list[Any]]] = []
    total_binding_matches = 0
    for result_index, result_value in enumerate(results):
        result = _require_object(
            result_value, f"block_search_adv.results[{result_index}]"
        )
        _require_fields(
            result,
            ("block", "binding_matches"),
            f"block_search_adv.results[{result_index}]",
        )
        block = _require_object(
            result["block"], f"block_search_adv.results[{result_index}].block"
        )
        _require_fields(
            block,
            (
                "doi", "block_id", "BLKsubsys_id", "search_scope",
                "block_type", "system_type", "n_matching_datapoints",
            ),
            f"block_search_adv.results[{result_index}].block",
        )
        _require_nonempty_string(
            block["doi"], f"block_search_adv.results[{result_index}].block.doi"
        )
        _require_nonempty_string(
            block["block_id"],
            f"block_search_adv.results[{result_index}].block.block_id",
        )
        _require_nonempty_string(
            block["block_type"],
            f"block_search_adv.results[{result_index}].block.block_type",
        )
        _require_nonempty_string(
            block["system_type"],
            f"block_search_adv.results[{result_index}].block.system_type",
        )
        search_scope = _require_nonempty_string(
            block["search_scope"],
            f"block_search_adv.results[{result_index}].block.search_scope",
        )
        if search_scope not in {"declared", "subsystem"}:
            raise ValueError(
                f"block_search_adv.results[{result_index}].block.search_scope "
                "must be 'declared' or 'subsystem'"
            )
        subsystem_id = block["BLKsubsys_id"]
        if search_scope == "declared" and subsystem_id is not None:
            raise ValueError("declared advanced-search target has BLKsubsys_id")
        if search_scope == "subsystem":
            _require_nonempty_string(
                subsystem_id,
                f"block_search_adv.results[{result_index}].block.BLKsubsys_id",
            )
        _require_nonnegative_int(
            block["n_matching_datapoints"],
            f"block_search_adv.results[{result_index}].block.n_matching_datapoints",
        )
        binding_matches = _require_array(
            result["binding_matches"],
            f"block_search_adv.results[{result_index}].binding_matches",
        )
        if not binding_matches:
            raise ValueError(
                f"block_search_adv.results[{result_index}] has no binding matches"
            )
        total_binding_matches += len(binding_matches)
        validated_rows.append((result, binding_matches))

    declared_binding_matches = payload.get(
        "n_binding_matches", total_binding_matches
    )
    declared_binding_matches = _require_nonnegative_int(
        declared_binding_matches, "block_search_adv.n_binding_matches"
    )
    if declared_binding_matches != total_binding_matches:
        raise ValueError(
            "block_search_adv.n_binding_matches does not match the nested "
            "binding_matches arrays"
        )

    writer = _BoundedWriter(_MAX_COMPACT_CHARS)
    writer.append("# block_search_adv")
    writer.append()
    writer.append(
        f"**Matches:** {n_results} unique ThermoML search target(s), "
        f"{total_binding_matches} legitimate binding match(es)."
    )
    writer.append(f"**Truncated by search limit:** {'yes' if truncated else 'no'}")

    normalized_query = payload.get("normalized_query")
    if isinstance(normalized_query, dict) and normalized_query.get("explanation"):
        writer.append(
            "**Search explanation:** "
            + _markdown_text(normalized_query["explanation"], max_chars=600)
        )

    if diagnostics:
        diagnostic_parts = []
        for name, value in list(diagnostics.items())[:12]:
            diagnostic_parts.append(
                f"{_markdown_text(name, max_chars=80)}="
                f"{_markdown_text(value, max_chars=100)}"
            )
        writer.append("**Diagnostics:** " + ", ".join(diagnostic_parts))

    alias_resolution = payload.get("alias_resolution", [])
    alias_rows = _require_array(
        alias_resolution,
        "block_search_adv.alias_resolution",
    )
    if alias_rows:
        rendered_aliases = [
            _format_alias_resolution(item, index)
            for index, item in enumerate(
                alias_rows[:_MAX_ALIAS_RESOLUTIONS]
            )
        ]
        omitted_aliases = len(alias_rows) - len(rendered_aliases)
        if omitted_aliases:
            rendered_aliases.append(f"+{omitted_aliases} alias(es)")
        writer.append(
            "**Identity translation / required roles:** "
            + _markdown_text("; ".join(rendered_aliases), max_chars=3_600)
        )

    if not results:
        writer.append()
        writer.append("No exact search target and binding combination satisfied the query.")
        return writer.render()

    writer.append()
    writer.append("## Exact search-target / occurrence matches")

    rendered_blocks = 0
    rendered_binding_matches = 0
    stop = False
    for result, binding_matches in validated_rows:
        if rendered_blocks >= _MAX_BLOCKS_RENDERED:
            break
        block = result["block"]
        rendered_matches_for_block = 0
        doi = _markdown_text(block["doi"], max_chars=180)
        block_id = _markdown_text(block["block_id"], max_chars=80)
        subsystem_id = block.get("BLKsubsys_id")
        lit_num_id = block.get("lit_num_id")
        identity = f"{doi} / `{block_id}`"
        if subsystem_id is not None:
            identity += f" / `{_markdown_text(subsystem_id, max_chars=80)}`"
        if lit_num_id:
            identity += f" / `{_markdown_text(lit_num_id, max_chars=80)}`"
        block_type = _markdown_text(block["block_type"], max_chars=100)
        system_type = _markdown_text(block["system_type"], max_chars=80)
        search_scope = _markdown_text(block["search_scope"], max_chars=40)
        declared_system_type = block.get("declared_system_type")
        if subsystem_id is not None and declared_system_type:
            system_type = (
                f"{_markdown_text(declared_system_type, max_chars=80)} → "
                f"{system_type} subsystem"
            )
        target_points = block["n_matching_datapoints"]

        for match in binding_matches:
            if rendered_binding_matches >= _MAX_BINDING_MATCHES_RENDERED:
                stop = True
                break
            binding_match = _require_object(
                match,
                f"binding match in {block['doi']} / {block['block_id']}",
            )
            _require_fields(
                binding_match,
                (
                    "bindings",
                    "fixed_filter_evidence",
                    "matched_complete_points",
                    "selected",
                    "order_keys",
                    "match_trace",
                ),
                f"binding match in {block['doi']} / {block['block_id']}",
            )
            complete_points = _require_nonnegative_int(
                binding_match["matched_complete_points"],
                "binding match matched_complete_points",
            )
            bindings = _markdown_text(
                _format_bindings(binding_match["bindings"]), max_chars=900
            )
            fixed_filters = _markdown_text(
                _format_fixed_filters(binding_match["fixed_filter_evidence"]),
                max_chars=750,
            )
            selected = _markdown_text(
                _format_selected(binding_match["selected"]), max_chars=650
            )
            order_keys = _markdown_text(
                _format_order_keys(binding_match["order_keys"]),
                max_chars=260,
            )
            trace = _markdown_text(
                _format_trace(binding_match["match_trace"]), max_chars=240
            )
            row_number = rendered_binding_matches + 1
            line = (
                f"{row_number}. **{identity}** — {block_type} / {system_type}; "
                f"scope: {search_scope}; target points: {target_points}; "
                f"complete points: {complete_points}; actual source bindings: "
                f"{bindings}; fixed gates: {fixed_filters}; selected/calculated: "
                f"{selected}; order keys: {order_keys}; row trace: {trace}."
            )
            if not writer.append(line, reserve=_FOOTER_RESERVE):
                stop = True
                break
            rendered_binding_matches += 1
            rendered_matches_for_block += 1
        if rendered_matches_for_block:
            rendered_blocks += 1
        if stop:
            break

    omitted_blocks = max(0, n_results - rendered_blocks)
    omitted_binding_matches = max(
        0, total_binding_matches - rendered_binding_matches
    )
    if omitted_blocks or omitted_binding_matches:
        writer.append()
        writer.append(
            "**Deterministic compaction bound reached:** "
            f"rendered {rendered_blocks}/{n_results} search target(s) and "
            f"{rendered_binding_matches}/{total_binding_matches} binding match(es); "
            f"omitted {omitted_blocks} search target(s) and "
            f"{omitted_binding_matches} binding match(es) from Markdown. "
            "The search result counts and truncation flag above remain authoritative."
        )

    return writer.render()


__all__ = ["compact_block_search_adv"]
