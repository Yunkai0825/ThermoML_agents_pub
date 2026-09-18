"""Direct, non-delegating ThermoML tools for the flat-tools benchmark.

Only the underlying L1/L2 search functions are exposed here. Their existing
catalog metadata is retained so the flat arm runs the same deterministic
compactors and task-directed KEEP/DISCARD compactor as the hierarchical agent,
without exposing an L1/L2 dispatcher.
"""

from __future__ import annotations

import hashlib
import importlib
import inspect
import json
import re
import sys
import time
import types
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Annotated, Any, Callable, Literal, Mapping, Union, get_args, get_origin, get_type_hints


_L1_MODULE = (
    "NIST_ThermoML_agents.NIST_ThermoML_query_agent.query_agent_workflows."
    "L1_workers.l1_query_dispatcher"
)
_L2_MODULE = (
    "NIST_ThermoML_agents.NIST_ThermoML_query_agent.query_agent_workflows."
    "L2_leaf_evaluators.l2_dispatchers"
)

# Fail preflight if upstream changes the compared toolbox.
_EXPECTED_L1_NAMES = (
    "resolve_ids",
    "resolve_compound_ids",
    "resolve_property_ids",
    "resolve_measurement_ids",
    "resolve_reference_ids",
    "search_id_alignment",
    "search_blocks",
    "block_search_adv",
    "inspect_block_table",
    "search_system_registry",
    "search_system_summary",
    "search_similar_compounds",
    "screen_property_systems",
)
_EXPECTED_L2_NAMES = (
    "search_comp_from_block",
    "search_compound_dk",
    "search_compound_indiv",
    "search_meas_from_block",
    "search_measurement_dk",
    "search_measurement_indiv",
    "search_reference_from_block",
    "search_references",
    "search_prop_dk_from_block",
    "search_property_dk",
)
_L2_ENTRY_GROUPS = (
    "_L2_COMP_ENTRIES",
    "_L2_MEAS_ENTRIES",
    "_L2_REF_ENTRIES",
    "_L2_PROP_ENTRIES",
)

_PURPOSE_DESCRIPTION = (
    "Why this tool call is needed for the user's question. This is passed "
    "unchanged to the agentic result compactor."
)
_TASKS_DESCRIPTION = (
    "Concrete evidence-gathering tasks this call must accomplish. These are "
    "passed unchanged to the agentic result compactor."
)


@dataclass(frozen=True)
class FlatTool:
    """One directly callable search function and its Anthropic input schema."""

    name: str
    description: str
    fn: Callable[..., Any]
    input_schema: dict[str, Any]
    # Actual resolved objects from QueryL1Catalog/L2*Catalog. Keeping these
    # objects preserves compactor functions, adaptive flags, and skip policy.
    entry: Any = None
    catalog: Any = None


def _find_python_root(project_root: Path) -> Path:
    """Return the directory that directly contains ``NIST_ThermoML_agents``."""

    supplied = Path(project_root).expanduser().resolve()
    candidates = (supplied, supplied / "ThermoML_research_agent")
    if supplied.name == "NIST_ThermoML_agents":
        candidates = (supplied.parent, *candidates)
    for candidate in candidates:
        if (candidate / "NIST_ThermoML_agents").is_dir():
            return candidate
    raise FileNotFoundError(
        "Could not find NIST_ThermoML_agents below project_root: "
        f"{supplied}"
    )


def _json_default(value: Any) -> tuple[bool, Any]:
    """Return a JSON-safe default value without stringifying it."""

    if isinstance(value, tuple):
        value = list(value)
    try:
        json.dumps(value, ensure_ascii=False, allow_nan=False)
    except (TypeError, ValueError):
        return False, None
    return True, value


def _schema_for_annotation(annotation: Any) -> dict[str, Any]:
    """Translate the annotation shapes used by the query tools to JSON Schema."""

    if annotation in (inspect.Signature.empty, Any):
        return {}
    if annotation in (None, type(None)):
        return {"type": "null"}

    # Usually get_type_hints resolves postponed annotations. This fallback
    # remains useful if an optional module dependency prevents evaluation.
    if isinstance(annotation, str):
        simple = annotation.strip().strip("'").strip('"')
        simple_types = {
            "str": "string",
            "int": "integer",
            "float": "number",
            "bool": "boolean",
            "dict": "object",
            "list": "array",
            "tuple": "array",
        }
        if simple in simple_types:
            return {"type": simple_types[simple]}
        return {}

    origin = get_origin(annotation)
    args = get_args(annotation)
    if origin is Annotated:
        return _schema_for_annotation(args[0]) if args else {}
    if origin in (Union, types.UnionType):
        variants = [_schema_for_annotation(item) for item in args]
        unique: list[dict[str, Any]] = []
        for variant in variants:
            if variant not in unique:
                unique.append(variant)
        return unique[0] if len(unique) == 1 else {"anyOf": unique}
    if origin is Literal:
        values = list(args)
        schema: dict[str, Any] = {"enum": values}
        value_types = {type(value) for value in values}
        type_names = {
            str: "string",
            int: "integer",
            float: "number",
            bool: "boolean",
            type(None): "null",
        }
        if len(value_types) == 1 and next(iter(value_types)) in type_names:
            schema["type"] = type_names[next(iter(value_types))]
        return schema
    if origin is list or annotation is list:
        return {
            "type": "array",
            "items": _schema_for_annotation(args[0]) if args else {},
        }
    if origin is tuple or annotation is tuple:
        if not args:
            return {"type": "array"}
        if len(args) == 2 and args[1] is Ellipsis:
            return {"type": "array", "items": _schema_for_annotation(args[0])}
        return {
            "type": "array",
            "prefixItems": [_schema_for_annotation(item) for item in args],
            "minItems": len(args),
            "maxItems": len(args),
        }
    if origin is dict or annotation is dict:
        value_schema = _schema_for_annotation(args[1]) if len(args) == 2 else {}
        return {"type": "object", "additionalProperties": value_schema}

    primitive_types = {str: "string", int: "integer", float: "number", bool: "boolean"}
    if annotation in primitive_types:
        return {"type": primitive_types[annotation]}
    return {}


def _resolved_hints(fn: Callable[..., Any]) -> dict[str, Any]:
    """Resolve postponed annotations, tolerating optional import failures."""

    try:
        return get_type_hints(fn, include_extras=True)
    except Exception:
        try:
            return inspect.get_annotations(fn, eval_str=True)
        except Exception:
            return dict(getattr(fn, "__annotations__", {}) or {})


def _input_schema(fn: Callable[..., Any]) -> dict[str, Any]:
    """Build an Anthropic-compatible object schema from a Python signature."""

    signature = inspect.signature(fn)
    hints = _resolved_hints(fn)
    properties: dict[str, Any] = {}
    required: list[str] = []
    for name, parameter in signature.parameters.items():
        if name == "hooks":
            continue
        if parameter.kind is inspect.Parameter.POSITIONAL_ONLY:
            raise TypeError(
                f"Cannot expose positional-only parameter {name!r} on {fn!r}"
            )
        if parameter.kind in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD):
            continue
        schema = _schema_for_annotation(hints.get(name, parameter.annotation))
        if parameter.default is inspect.Parameter.empty:
            required.append(name)
        else:
            safe, default = _json_default(parameter.default)
            if safe:
                schema = dict(schema)
                schema["default"] = default
        properties[name] = schema

    # All calls carry the relevance target needed by the separate compactor.
    # screen_property_systems already has purpose/tasks; its tasks array is
    # normalized back to the underlying string parameter at execution time.
    properties["purpose"] = {
        "type": "string",
        "minLength": 1,
        "description": _PURPOSE_DESCRIPTION,
    }
    properties["tasks"] = {
        "type": "array",
        "items": {"type": "string", "minLength": 1},
        "minItems": 1,
        "description": _TASKS_DESCRIPTION,
    }
    for wrapper_name in ("purpose", "tasks"):
        if wrapper_name not in required:
            required.append(wrapper_name)
    return {
        "type": "object",
        "properties": properties,
        "required": required,
        "additionalProperties": False,
    }


def _entry_description(entry: Any) -> str:
    """Prefer the callable's full usage documentation for a flat agent."""

    doc = inspect.getdoc(entry.fn)
    if doc:
        return doc
    description = str(getattr(entry, "description", "") or "").strip()
    if description:
        return description
    return f"Direct ThermoML search tool: {entry.name}."


def load_flat_tools(project_root: Path) -> dict[str, FlatTool]:
    """Load exactly 13 L1 and 10 raw L2 tools without invoking any of them."""

    python_root = _find_python_root(project_root)
    root_text = str(python_root)
    if root_text not in sys.path:
        sys.path.insert(0, root_text)

    l1_module = importlib.import_module(_L1_MODULE)
    l2_module = importlib.import_module(_L2_MODULE)
    l1_entries = tuple(getattr(l1_module, "_SEARCH_ENTRIES"))
    l2_entries = tuple(
        entry
        for group_name in _L2_ENTRY_GROUPS
        for entry in getattr(l2_module, group_name)
    )
    l1_names = tuple(entry.name for entry in l1_entries)
    l2_names = tuple(entry.name for entry in l2_entries)

    if l1_names != _EXPECTED_L1_NAMES:
        raise RuntimeError(
            "L1 direct-tool registry drifted; expected "
            f"{_EXPECTED_L1_NAMES!r}, found {l1_names!r}"
        )
    if l2_names != _EXPECTED_L2_NAMES:
        raise RuntimeError(
            "L2 raw-tool registry drifted; expected "
            f"{_EXPECTED_L2_NAMES!r}, found {l2_names!r}"
        )

    # Instantiate the real catalogs to resolve the L1 compactor catalog and
    # retain each layer's exact adaptive/skip flags. Constructors do not call
    # tools or create an LLM client; both behaviours remain lazy.
    source_catalog_groups = (
        (l1_module.QueryL1Catalog(), _EXPECTED_L1_NAMES),
        (l2_module.L2CompCatalog(), tuple(e.name for e in l2_module._L2_COMP_ENTRIES)),
        (l2_module.L2MeasCatalog(), tuple(e.name for e in l2_module._L2_MEAS_ENTRIES)),
        (l2_module.L2RefCatalog(), tuple(e.name for e in l2_module._L2_REF_ENTRIES)),
        (l2_module.L2PropCatalog(), tuple(e.name for e in l2_module._L2_PROP_ENTRIES)),
    )
    catalog_module = importlib.import_module(
        "NIST_ThermoML_agents.general_db_query_engine."
        "general_tool_management_helpers.general_agent_tool_catalog"
    )
    resolved: list[tuple[Any, Any]] = []
    for source_catalog, names in source_catalog_groups:
        source_entries = source_catalog.entries
        selected_entries = []
        for name in names:
            if name not in source_entries:
                raise RuntimeError(
                    f"Resolved catalog {type(source_catalog).__name__} omitted {name!r}"
                )
            selected_entries.append(source_entries[name])

        # Do not retain QueryL1Catalog itself: it also owns four task-delegating
        # L2 dispatcher entries. This compaction-only clone contains just the
        # selected direct functions and has no client factory, making Argo or
        # dispatcher invocation impossible from the returned flat toolbox.
        catalog = catalog_module.AgentToolCatalog(
            client_factory=None,
            cfg=getattr(source_catalog, "_cfg", None),
            entries=selected_entries,
        )
        catalog.pipeline_label = "query"
        flat_entries = catalog.entries
        resolved.extend((flat_entries[name], catalog) for name in names)

    tools: dict[str, FlatTool] = {}
    for entry, catalog in resolved:
        if entry.name in tools:
            raise RuntimeError(f"Duplicate direct tool name: {entry.name}")
        if not callable(entry.fn):
            raise TypeError(f"Direct tool {entry.name!r} is not callable")
        if not entry.skip_compactor and entry.compactor_fn is None:
            raise RuntimeError(
                f"Direct tool {entry.name!r} has no resolved deterministic compactor"
            )
        tools[entry.name] = FlatTool(
            name=entry.name,
            description=_entry_description(entry),
            fn=entry.fn,
            input_schema=_input_schema(entry.fn),
            entry=entry,
            catalog=catalog,
        )

    if len(tools) != 23:
        raise RuntimeError(f"Expected 23 direct tools, loaded {len(tools)}")
    return tools


def _normalize_tasks(value: Any) -> list[str]:
    """Validate wrapper tasks while tolerating a single legacy string."""

    if isinstance(value, str):
        tasks = [value]
    elif isinstance(value, (list, tuple)):
        tasks = list(value)
    else:
        raise TypeError("tasks must be an array of non-empty strings")
    if not tasks or any(not isinstance(task, str) or not task.strip() for task in tasks):
        raise ValueError("tasks must contain at least one non-empty string")
    return tasks


def _raw_markdown(tool_name: str, raw: Any) -> str:
    """Serialize a result deterministically inside a collision-safe fence."""

    try:
        payload = json.dumps(
            raw,
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        )
        payload_format = "json"
        language = "json"
    except (TypeError, ValueError):
        try:
            payload = repr(raw)
        except Exception as exc:  # pragma: no cover - pathological repr objects
            payload = f"<unrepresentable {type(raw).__name__}: {type(exc).__name__}>"
        payload_format = "python-repr"
        language = "text"

    longest_run = max(
        (len(match.group(0)) for match in re.finditer(r"`+", payload)),
        default=0,
    )
    fence = "`" * max(3, longest_run + 1)
    return (
        f"# Raw tool result: `{tool_name}`\n\n"
        f"Serialization: `{payload_format}`\n\n"
        f"{fence}{language}\n{payload}\n{fence}\n"
    )


def execute_flat_tool(tool: FlatTool, args: dict[str, Any]) -> dict[str, Any]:
    """Execute a direct tool and run its existing deterministic stage.

    The lossless native serialization is retained for auditing. Object results
    use the resolved catalog's hardcoded compactor unless the original entry
    explicitly opts out; pre-compacted strings keep the catalog's pass-through
    behaviour. Agentic KEEP/DISCARD is a separate call so its API usage can be
    measured independently by :func:`compact_flat_tool_result`.
    """

    started = time.perf_counter()
    purpose: str | None = None
    tasks: list[str] = []
    error: str | None = None
    error_stage: str | None = None
    raw: Any
    tool_started = time.perf_counter()
    try:
        if not isinstance(tool, FlatTool):
            raise TypeError("tool must be a FlatTool")
        if not isinstance(args, dict):
            raise TypeError("tool arguments must be a dictionary")

        call_args = dict(args)
        purpose_value = call_args.pop("purpose", None)
        if not isinstance(purpose_value, str) or not purpose_value.strip():
            raise ValueError("purpose must be a non-empty string")
        purpose = purpose_value
        tasks = _normalize_tasks(call_args.pop("tasks", None))

        signature = inspect.signature(tool.fn)
        if "purpose" in signature.parameters:
            call_args["purpose"] = purpose
        if "tasks" in signature.parameters:
            # screen_property_systems consumes a text task brief; the common
            # wrapper uses an array to retain task boundaries for compaction.
            call_args["tasks"] = "\n".join(tasks)

        # Gives clear errors for unknown/missing arguments before execution.
        signature.bind(**call_args)
        raw = tool.fn(**call_args)
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
        error_stage = "tool_execution"
        raw = {
            "error": {
                "message": str(exc),
                "type": type(exc).__name__,
            }
        }
    tool_elapsed_s = time.perf_counter() - tool_started

    raw_markdown = _raw_markdown(getattr(tool, "name", "unknown"), raw)
    raw_digest = hashlib.sha256(raw_markdown.encode("utf-8")).hexdigest()

    entry = tool.entry if isinstance(tool, FlatTool) else None
    skip_compactor = bool(entry is None or entry.skip_compactor)
    skip_subagent = bool(entry is None or entry.skip_subagent)
    adaptive_condense = bool(entry is not None and entry.adaptive_condense)
    compactor_name = (
        getattr(entry.compactor_fn, "__name__", None)
        if entry is not None else None
    )
    hardcoded_markdown = ""
    hardcoded_mode = "not_run"
    hardcoded_started = time.perf_counter()
    if error is None:
        try:
            if isinstance(raw, str):
                # AgentToolCatalog.wrap_tool passes strings through unchanged.
                hardcoded_markdown = raw
                hardcoded_mode = "precompacted_string_passthrough"
            elif not isinstance(raw, dict):
                raise TypeError(
                    f"Tool {tool.name!r} returned {type(raw).__name__}; "
                    "existing tool contracts require an object or string"
                )
            elif skip_compactor:
                hardcoded_markdown = raw_markdown
                hardcoded_mode = "catalog_passthrough"
            else:
                if tool.catalog is None:
                    raise RuntimeError(
                        f"Tool {tool.name!r} has no resolved catalog compactor"
                    )
                hardcoded_markdown = tool.catalog.compact_tool_result(
                    tool.name, raw, level="full"
                )
                hardcoded_mode = (
                    "existing_adaptive_compactor"
                    if adaptive_condense else "existing_hardcoded_compactor"
                )
            if not isinstance(hardcoded_markdown, str) or not hardcoded_markdown.strip():
                raise TypeError("deterministic compaction returned empty Markdown")
        except Exception as exc:
            error = f"{type(exc).__name__}: {exc}"
            error_stage = "hardcoded_compaction"
            hardcoded_markdown = ""
            hardcoded_mode = "failed"
    hardcoded_elapsed_s = time.perf_counter() - hardcoded_started
    hardcoded_digest = (
        hashlib.sha256(hardcoded_markdown.encode("utf-8")).hexdigest()
        if hardcoded_markdown else None
    )
    elapsed_s = time.perf_counter() - started
    return {
        "tool": getattr(tool, "name", "unknown"),
        "purpose": purpose,
        "tasks": tasks,
        "ok": error is None,
        "raw_result": raw,
        "raw_markdown": raw_markdown,
        "raw_sha256": raw_digest,
        "hardcoded_markdown": hardcoded_markdown,
        "hardcoded_sha256": hardcoded_digest,
        "hardcoded_mode": hardcoded_mode,
        "compactor_name": compactor_name,
        "adaptive_condense": adaptive_condense,
        "skip_compactor": skip_compactor,
        "skip_subagent": skip_subagent,
        # The benchmark deliberately overrides catalog skip_subagent flags:
        # every successful result must pass task-directed agentic compaction
        # before it can enter the answering model's context.
        "requires_agentic_compaction": bool(error is None),
        "tool_elapsed_s": tool_elapsed_s,
        "hardcoded_elapsed_s": hardcoded_elapsed_s,
        "elapsed_s": elapsed_s,
        "sha256": raw_digest,
        "error_stage": error_stage,
        "error": error,
    }


class _AnthropicCompactorClientAdapter:
    """Expose the existing compactor's ``.call`` API over Anthropic Messages."""

    def __init__(self, client: Any, model: str) -> None:
        if not isinstance(model, str) or not model.strip():
            raise ValueError("compactor model must be a non-empty string")
        if not callable(getattr(client, "create_message", None)):
            raise TypeError("client must provide create_message(...)")
        self.client = client
        self.model = model
        self.responses: list[dict[str, Any]] = []
        self.call_elapsed_s: list[float] = []

    def call(self, prompt: str, system: str, *, max_tokens: int) -> str:
        started = time.perf_counter()
        response = self.client.create_message(
            model=self.model,
            system=system,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.0,
        )
        self.call_elapsed_s.append(time.perf_counter() - started)
        if not isinstance(response, Mapping):
            raise TypeError("Anthropic compactor response must be an object")
        saved = dict(response)
        self.responses.append(saved)
        pieces = [
            str(block.get("text") or "")
            for block in saved.get("content") or []
            if isinstance(block, Mapping) and block.get("type") == "text"
        ]
        text = "\n".join(piece for piece in pieces if piece).strip()
        if not text:
            raise ValueError("Anthropic compactor returned no visible text")
        return text


def _usage_totals(responses: list[dict[str, Any]]) -> dict[str, int]:
    keys = (
        "input_tokens",
        "output_tokens",
        "cache_creation_input_tokens",
        "cache_read_input_tokens",
    )
    totals = {"calls": len(responses), **{key: 0 for key in keys}}
    for response in responses:
        usage = response.get("usage") or {}
        for key in keys:
            totals[key] += int(usage.get(key) or 0)
    return totals


@contextmanager
def _isolated_compactor_recorders(tool_name: str, purpose: str):
    """Bind no-output recorders required by the shared compactor, then restore."""

    history_module = importlib.import_module(
        "NIST_ThermoML_agents.general_db_query_engine."
        "general_hooks_management_helpers.general_context_hooks."
        "history_tracking_hooks"
    )
    stats_module = importlib.import_module(
        "NIST_ThermoML_agents.general_db_query_engine."
        "general_hooks_management_helpers.general_context_hooks."
        "stats_references_tracking_hooks"
    )
    try:
        previous_history = history_module.get_active_history_recorder()
    except RuntimeError:
        previous_history = None
    try:
        previous_stats = stats_module.get_active_recorder()
    except RuntimeError:
        previous_stats = None

    history = history_module.HistoryRecorder()
    stats = stats_module.StatsRecorder()
    history_bound = False
    stats_bound = False
    try:
        history.start_run(
            agent="flat-tool-agentic-compactor",
            prompt=f"{tool_name}: {purpose}",
            out_path=None,
        )
        stats.start_run(agent_label="flat-tool-agentic-compactor", out_path=None)
        history_module.set_active_history_recorder(history)
        history_bound = True
        stats_module.set_active_recorder(stats)
        stats_bound = True
        yield
    finally:
        if stats_bound:
            if previous_stats is None:
                stats_module.clear_active_recorder()
            else:
                stats_module.set_active_recorder(previous_stats)
        if history_bound:
            if previous_history is None:
                history_module.clear_active_history_recorder()
            else:
                history_module.set_active_history_recorder(previous_history)


def compact_flat_tool_result(
    tool: FlatTool,
    execution: Mapping[str, Any],
    *,
    client: Any,
    model: str,
) -> dict[str, Any]:
    """Run the existing task-directed agentic stage over stage-one Markdown.

    This calls the repository's shared ``call_tool_subagent`` implementation,
    so its system prompt, PURPOSE/TASKS payload, character guard, parser,
    bounded format retry, and ``ToolResult`` contract remain authoritative.
    A tiny transport adapter routes only its LLM request through the supplied
    benchmark Anthropic client/model; QueryClient/Argo is never constructed.

    Catalog ``skip_subagent`` flags are retained in audit metadata but are
    deliberately overridden: every successful flat-tool result must pass this
    agentic stage before entering the answering model's context.
    """

    started = time.perf_counter()
    if not isinstance(tool, FlatTool):
        raise TypeError("tool must be a FlatTool")
    if not isinstance(execution, Mapping):
        raise TypeError("execution must be the execute_flat_tool result")
    if execution.get("tool") != tool.name:
        raise ValueError(
            f"execution belongs to {execution.get('tool')!r}, not {tool.name!r}"
        )

    execution_ok = bool(execution.get("ok"))
    purpose = execution.get("purpose")
    if not isinstance(purpose, str) or not purpose.strip():
        if execution_ok:
            raise ValueError("execution purpose must be a non-empty string")
        purpose = ""
    try:
        tasks = _normalize_tasks(execution.get("tasks"))
    except (TypeError, ValueError):
        if execution_ok:
            raise
        tasks = []
    tasks_text = "\n".join(tasks)
    raw = execution.get("raw_result")
    raw_markdown = execution.get("raw_markdown")
    hardcoded_markdown = execution.get("hardcoded_markdown")
    if not isinstance(raw_markdown, str) or not raw_markdown.strip():
        raise ValueError("execution has no raw Markdown serialization")

    base: dict[str, Any] = {
        "tool": tool.name,
        "purpose": purpose,
        "tasks": tasks,
        "raw_result": raw,
        "raw_markdown": raw_markdown,
        "raw_sha256": execution.get("raw_sha256") or execution.get("sha256"),
        "hardcoded_markdown": hardcoded_markdown,
        "hardcoded_sha256": execution.get("hardcoded_sha256"),
        "hardcoded_mode": execution.get("hardcoded_mode"),
        "compactor_name": execution.get("compactor_name"),
        "tool_elapsed_s": float(execution.get("tool_elapsed_s") or 0.0),
        "hardcoded_elapsed_s": float(
            execution.get("hardcoded_elapsed_s") or 0.0
        ),
        "agentic_model": model,
        "agentic_markdown": None,
        "agentic_sha256": None,
        "final_markdown": "",
        "final_sha256": None,
        "verdict": "ERROR",
        "discarded": False,
        "agentic_elapsed_s": 0.0,
        "agentic_api_elapsed_s": 0.0,
        "agentic_attempts": 0,
        "agentic_protocol_responses": [],
        "api_responses": [],
        "api_usage": _usage_totals([]),
        "error": None,
    }

    if not execution_ok:
        base["error"] = execution.get("error") or "flat tool execution failed"
        base["error_stage"] = execution.get("error_stage") or "tool_execution"
        if base["error_stage"] == "hardcoded_compaction":
            # The lossless raw result remains in the audit record, but a
            # deterministic-compactor failure must never bypass the required
            # result pipeline and expose unreviewed data to the answering model.
            base["final_markdown"] = (
                "# Tool-result compaction failed\n\n"
                f"The `{tool.name}` tool executed, but its required deterministic "
                "compactor failed. The raw result was retained only in the "
                "benchmark audit artifact and was not exposed here. Retry with "
                "a narrower or different tool call."
            )
        else:
            # Even an exception message can echo query data. Keep the serialized
            # error envelope audit-only and expose only a static failure notice.
            base["final_markdown"] = (
                "# Tool execution failed\n\n"
                f"The `{tool.name}` tool did not produce a result. Execution "
                "details were retained only in the benchmark audit artifact "
                "and were not exposed here."
            )
        base["final_sha256"] = hashlib.sha256(
            base["final_markdown"].encode("utf-8")
        ).hexdigest()
        base["total_pipeline_elapsed_s"] = float(execution.get("elapsed_s") or 0.0)
        return base

    if not isinstance(hardcoded_markdown, str) or not hardcoded_markdown.strip():
        raise ValueError("successful execution has no deterministic-stage Markdown")

    if not execution.get("requires_agentic_compaction"):
        raise RuntimeError(
            "successful flat-tool execution must require agentic compaction"
        )
    if isinstance(raw, dict):
        agentic_raw = raw
    elif isinstance(raw, str):
        # The shared compactor requires a dict only for structured context and
        # audit retention. Keep a pre-compacted string inside an explicit
        # envelope while sending its hardcoded Markdown through the same
        # mandatory agentic gate as every other successful result.
        agentic_raw = {"precompacted_result": raw}
    else:
        raise TypeError("existing agentic compactor requires an object or string result")
    adapter = _AnthropicCompactorClientAdapter(client, model)
    protocol_responses: list[dict[str, str]] = []

    compactor_module = importlib.import_module(
        "NIST_ThermoML_agents.general_db_query_engine."
        "general_tool_management_helpers."
        "general_tool_results_compactor_agentic_hooks"
    )
    cfg = getattr(tool.catalog, "_cfg", None)
    if cfg is None:
        cfg_module = importlib.import_module(
            "NIST_ThermoML_agents.NIST_ThermoML_query_agent."
            "ThermoML_query_argo_config"
        )
        cfg = cfg_module.AGENT_CONFIG

    agentic_started = time.perf_counter()
    try:
        with _isolated_compactor_recorders(tool.name, purpose):
            result = compactor_module.call_tool_subagent(
                tool.name,
                purpose,
                tasks_text,
                hardcoded_markdown,
                agentic_raw,
                client_factory=lambda: adapter,
                cfg=cfg,
                pipeline_label="query",
                reasoning_hook=lambda label, text: protocol_responses.append(
                    {"label": label, "text": text}
                ),
            )
        if not isinstance(result, compactor_module.ToolResult):
            raise TypeError("existing agentic compactor did not return ToolResult")
        base["agentic_markdown"] = result.text
        base["agentic_sha256"] = hashlib.sha256(
            result.text.encode("utf-8")
        ).hexdigest()
        base["final_markdown"] = result.text
        base["final_sha256"] = base["agentic_sha256"]
        base["discarded"] = result.discarded
        base["verdict"] = "DISCARD" if result.discarded else "KEEP"
    except Exception as exc:
        # Preserve the explicit mandatory-compactor failure; never guess a
        # verdict or silently fall back to unreviewed deterministic Markdown.
        base["error"] = f"{type(exc).__name__}: {exc}"
        base["error_stage"] = "agentic_compaction"
        base["verdict"] = "ERROR"
    finally:
        base["agentic_elapsed_s"] = time.perf_counter() - agentic_started
        base["agentic_api_elapsed_s"] = sum(adapter.call_elapsed_s)
        base["agentic_attempts"] = len(adapter.responses)
        base["agentic_protocol_responses"] = protocol_responses
        base["api_responses"] = adapter.responses
        base["api_usage"] = _usage_totals(adapter.responses)
        base["total_pipeline_elapsed_s"] = (
            float(execution.get("elapsed_s") or 0.0)
            + base["agentic_elapsed_s"]
        )
        base["adapter_elapsed_s"] = time.perf_counter() - started
    return base


__all__ = [
    "FlatTool",
    "compact_flat_tool_result",
    "execute_flat_tool",
    "load_flat_tools",
]
