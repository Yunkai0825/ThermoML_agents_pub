"""Shared tool-result instrumentation wrapper.
======================================================
Provides ``make_instrumented_wrapper`` — a factory that wraps any tool
callable so that:

1. The result is stored in working memory.
2. The ``record_references`` anchor is fired for entity / DOI tracking.
3. Internal ``ToolResult`` containers are converted to their declared text
   at the final agent-tool boundary; structured results remain native dicts.

Both the analysis agent and main agent orchestrators share this
pattern.  Extracting it here avoids drift between the two
implementations and ensures bug-fixes land once.
"""

from __future__ import annotations

import functools
import json
from typing import Any, Callable

from ...general_tool_management_helpers.general_tool_results_compactor_agentic_hooks import (
    ToolResult,
)
from ...general_argo_engine_helpers.engine_react_helpers.react_helpers import (
    validate_native_tool_result,
)
from ...general_text_context_marker_catalog import MARKERS


def make_instrumented_wrapper(
    name: str,
    fn: Callable,
    *,
    working_mem: Any,
    agent_hooks: Any,
    anchor_fn: Callable,
    mem_anchor_record: Any,
) -> Callable:
    """Return a wrapped version of *fn* that records results.

    Parameters
    ----------
    name : str
        The tool name (used as key in working memory).
    fn : callable
        The original tool function.
    working_mem
        An object with ``record_tool_result(name, result)`` method.
    agent_hooks
        Agent hook collection exposing ``anchors.record_references``
        and ``engine_hooks``.
    anchor_fn : callable
        The ``anchor()`` helper (from ``general_argo_engine_helpers``).
    mem_anchor_record
        The ``SYNC_WORKING_MEMORY_RECORD`` anchor point.
    """

    def wrapper(**kwargs: Any) -> Any:
        result = fn(**kwargs)

        # --- Determine raw_result (dict) and stored_result for memory ---
        raw_dict: dict | None = None

        agent_result: dict | str
        if isinstance(result, ToolResult):
            if not isinstance(result.raw, dict):
                raise TypeError(f"ToolResult.raw for {name!r} must be an object")
            if not isinstance(result.text, str) or not result.text.strip():
                raise TypeError(f"ToolResult.text for {name!r} must be non-empty text")
            validated_raw = validate_native_tool_result(name, result.raw)
            if not isinstance(validated_raw, dict):
                raise AssertionError("validated ToolResult.raw changed type")
            validated_text = validate_native_tool_result(name, result.text)
            if not isinstance(validated_text, str):
                raise AssertionError("validated ToolResult.text changed type")
            raw_dict = validated_raw
            transformed = anchor_fn(
                mem_anchor_record,
                agent_hooks.engine_hooks,
                tool_name=name,
                content=raw_dict,
                tool_args=dict(kwargs),
            )
            stored_result = raw_dict if transformed is None else transformed
            agent_result = validated_text

        elif isinstance(result, dict):
            validated_result = validate_native_tool_result(name, result)
            if not isinstance(validated_result, dict):
                raise AssertionError("validated object result changed type")
            raw_dict = validated_result
            transformed = anchor_fn(
                mem_anchor_record,
                agent_hooks.engine_hooks,
                tool_name=name,
                content=raw_dict,
                tool_args=dict(kwargs),
            )
            stored_result = raw_dict if transformed is None else transformed
            agent_result = validated_result

        elif isinstance(result, str):
            validated_text = validate_native_tool_result(name, result)
            if not isinstance(validated_text, str):
                raise AssertionError("validated text result changed type")
            if getattr(fn, "_returns_subagent_answer", False):
                match = MARKERS.subagent_answer_re.fullmatch(validated_text.strip())
                if match is None:
                    raise ValueError(
                        f"Marked subagent tool {name!r} must return exactly one "
                        "<subagent_answer> JSON envelope"
                    )
                try:
                    content = json.loads(match.group(1))
                except json.JSONDecodeError as exc:
                    raise ValueError(
                        f"Marked subagent tool {name!r} returned invalid JSON"
                    ) from exc
                if not isinstance(content, dict):
                    raise TypeError(
                        f"Marked subagent tool {name!r} JSON must be an object"
                    )
            else:
                content = {"text": validated_text}
            transformed = anchor_fn(
                mem_anchor_record,
                agent_hooks.engine_hooks,
                tool_name=name,
                content=content,
                tool_args=dict(kwargs),
            )
            stored_result = content if transformed is None else transformed
            agent_result = validated_text

        else:
            raise TypeError(
                f"Tool {name!r} returned unsupported {type(result).__name__}; "
                "tool results must be a dict, string, or internal ToolResult"
            )

        if not isinstance(stored_result, dict):
            raise TypeError(f"working-memory hook for {name!r} must return an object or None")

        working_mem.record_tool_result(name, stored_result)

        # NOTE: record_references is fired by react_loop.py after tool
        # execution — no need to duplicate it here.

        return agent_result

    wrapper.__name__ = getattr(fn, '__name__', name)
    wrapper.__doc__ = getattr(fn, '__doc__', None)
    functools.update_wrapper(wrapper, fn)
    return wrapper
