"""
Engine hook dispatch primitives.
================================
The engine does not define concrete anchors or hook implementations.
It only provides the data structures used by the anchor catalogs and
the dispatch helpers consumed by the ReAct loops.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
import logging
import threading
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping

from ..general_hooks_management_helpers.general_context_hooks.history_tracking_hooks import (
    set_active_history_recorder as _set_active_history,
    get_active_history_recorder as _get_active_history,
    clear_active_history_recorder as _clear_active_history,
)

from ..general_hooks_management_helpers.general_context_hooks.stats_references_tracking_hooks import (
    set_active_recorder as _set_active_recorder,
    get_active_recorder as _get_active_recorder,
    clear_active_recorder as _clear_active_recorder,
)
from ..general_hooks_management_helpers.general_context_hooks.reasoning_token_tracking_hooks import (
    set_active_reasoning_tracker as _set_active_reasoning,
    get_active_reasoning_tracker as _get_active_reasoning,
    clear_active_reasoning_tracker as _clear_active_reasoning,
)

log = logging.getLogger("ENGINE-HOOKS")


@dataclass(frozen=True)
class AnchorPoint:
    """A concrete anchor point declared by one of the anchor catalogs."""

    name: str
    anchor_types: tuple[str, ...]

    @property
    def anchor_type(self) -> str:
        return self.anchor_types[0]


@dataclass(frozen=True)
class AnchorCollection:
    """Named collection of anchor points declared by an anchor catalog."""

    points: Mapping[str, AnchorPoint]

    def get(self, name: str) -> AnchorPoint:
        return self.points[name]

    @property
    def anchor_types(self) -> tuple[str, ...]:
        seen: list[str] = []
        for point in self.points.values():
            for anchor_type in point.anchor_types:
                if anchor_type not in seen:
                    seen.append(anchor_type)
        return tuple(seen)


@dataclass(frozen=True)
class HookBinding:
    """A callback together with the anchor types it applies to."""

    callback: Callable[..., Any]
    anchor_types: tuple[str, ...]
    name: str = ""


EngineHooks = Mapping[str, tuple[Callable[..., Any], ...]]


AGENT_START_TRACKING = AnchorPoint(
    name="agent_start_tracking",
    anchor_types=("agent_start_tracking",),
)
AGENT_FINALIZE_TRACKING = AnchorPoint(
    name="agent_finalize_tracking",
    anchor_types=("agent_finalize_tracking",),
)
AGENT_RECORD_REFERENCES = AnchorPoint(
    name="agent_record_references",
    anchor_types=("agent_record_references",),
)
AGENT_SAVE_FINAL_CONTEXT = AnchorPoint(
    name="agent_save_final_context",
    anchor_types=("agent_save_final_context",),
)
AGENT_RUN_VERDICT = AnchorPoint(
    name="agent_run_verdict",
    anchor_types=("agent_run_verdict",),
)


@dataclass(frozen=True)
class AgentAnchorCollection:
    start_tracking: AnchorPoint = AGENT_START_TRACKING
    finalize_tracking: AnchorPoint = AGENT_FINALIZE_TRACKING
    record_references: AnchorPoint = AGENT_RECORD_REFERENCES
    save_final_context: AnchorPoint = AGENT_SAVE_FINAL_CONTEXT
    run_verdict: AnchorPoint = AGENT_RUN_VERDICT


@dataclass
class AgentHookCollection:
    """Shared agent hook collection with compiled engine hooks."""

    engine_hooks: EngineHooks = field(init=False, default_factory=dict)
    anchors: AgentAnchorCollection = field(default_factory=AgentAnchorCollection)
    history: Any = None
    stats: Any = None
    reasoning: Any = None
    working_memory_loader: Callable[[], str] | None = None
    compactor: Callable[..., Any] | None = None
    batch_summary: Callable[..., Any] | None = None
    verdict_runner: Callable[..., Any] | None = None
    final_context_saver: Callable[..., Any] | None = None

    def __post_init__(self) -> None:
        self.rebuild_engine_hooks()

    def build_engine_hooks(self) -> Iterable[HookBinding] | EngineHooks | None:
        return EMPTY_HOOKS

    def rebuild_engine_hooks(self) -> EngineHooks:
        self.engine_hooks = compile_hooks(self.build_engine_hooks())
        return self.engine_hooks


def define_anchor(name: str, *anchor_types: str) -> AnchorPoint:
    """Create an anchor point for use in an anchor catalog."""
    types = tuple(anchor_types) or (name,)
    return AnchorPoint(name=name, anchor_types=types)


def define_anchor_collection(**points: AnchorPoint) -> AnchorCollection:
    """Create a named anchor collection for a catalog."""
    return AnchorCollection(points=dict(points))


def build_agent_lifecycle_bindings(
    *,
    history: Any = None,
    stats: Any = None,
    reasoning: Any = None,
    verdict_runner: Callable[..., Any] | None = None,
    final_context_saver: Callable[..., Any] | None = None,
    anchors: AgentAnchorCollection | None = None,
) -> tuple[HookBinding, ...]:
    """Build generic lifecycle bindings for an agent hook collection."""
    anchor_set = anchors or AgentAnchorCollection()

    # Nested sibling/subagent runs share the caller's thread and context, so
    # teardown must RESTORE the parent's active trackers, never blanket-clear
    # them. Keyed by thread id; each bindings instance tracks its own runs.
    _previous_trackers: dict[int, dict[str, Any]] = {}
    _evidence_dirs: dict[int, Path | None] = {}

    def _capture_active(getter: Callable[[], Any]) -> Any:
        try:
            return getter()
        except RuntimeError:
            return None

    def _start_tracking(
        *,
        agent: str,
        prompt: str = "",
        history_out_path: str | Path | None = None,
        stats_out_path: str | Path | None = None,
        reasoning_out_path: str | Path | None = None,
        **_: Any,
    ) -> None:
        _previous_trackers[threading.get_ident()] = {
            "history": _capture_active(_get_active_history),
            "stats": _capture_active(_get_active_recorder),
            "reasoning": _capture_active(_get_active_reasoning),
        }
        _evidence_dirs[threading.get_ident()] = (
            Path(history_out_path).parent if history_out_path else None
        )
        if history is not None:
            history.start_run(agent=agent, prompt=prompt, out_path=history_out_path)
            _set_active_history(history)
        if stats is not None:
            stats.start_run(
                agent,
                out_path=Path(stats_out_path) if stats_out_path is not None else None,
            )
            _set_active_recorder(stats)
        if reasoning is not None and reasoning_out_path is not None:
            reasoning.start_run(agent, out_path=str(reasoning_out_path))
            _set_active_reasoning(reasoning)

    def _finalize_tracking(
        *,
        status: str,
        stats_path: str | Path | None = None,
        flush_history: bool = True,
        **_: Any,
    ) -> None:
        previous = _previous_trackers.pop(threading.get_ident(), {})
        _evidence_dirs.pop(threading.get_ident(), None)
        if history is not None and flush_history:
            history.set_final_status(status)
            history.flush()
            history.reset()
            if previous.get("history") is not None:
                _set_active_history(previous["history"])
            else:
                _clear_active_history()
        if stats is not None:
            if stats_path is not None:
                stats.flush(str(stats_path))
            stats.reset()
            if previous.get("stats") is not None:
                _set_active_recorder(previous["stats"])
            else:
                _clear_active_recorder()
        if reasoning is not None:
            reasoning.set_final_status(status)
            reasoning.flush()
            reasoning.reset()
            if previous.get("reasoning") is not None:
                _set_active_reasoning(previous["reasoning"])
            else:
                _clear_active_reasoning()

    def _record_references(*, tool_name: str, raw_result: dict, **_: Any) -> None:
        if stats is None:
            return
        # Core reference tracking — must always run
        stats.log_doi_block_references(tool_name, raw_result)
        stats.log_entity_references(tool_name, raw_result)
        stats.log_raw_counters(tool_name, raw_result)

    def _save_final_context(
        *,
        session_dir: str | Path,
        final_context: str,
        filename: str = "final_full_context.md",
        **_: Any,
    ) -> None:
        if final_context_saver is not None:
            final_context_saver(session_dir, final_context, filename=filename)

    def _run_verdict(*args: Any, **kwargs: Any) -> Any:
        if verdict_runner is None:
            return None
        return verdict_runner(*args, **kwargs)

    def _write_grounding_evidence(
        *,
        answer: str = "",
        tool_history: list | None = None,
        **_: Any,
    ) -> None:
        """Passive per-run grounding evidence bundle (json + md)."""
        run_dir = _evidence_dirs.get(threading.get_ident())
        if run_dir is None or tool_history is None:
            return
        try:
            from ..general_data_grounding_gate.evidence_log import (
                write_grounding_evidence,
            )
            write_grounding_evidence(run_dir, answer, tool_history)
        except Exception:  # audit artifact — never disturb the run
            log.debug("grounding evidence write skipped", exc_info=True)

    return (
        bind_hook(_start_tracking, anchor_set.start_tracking.anchor_type, name="start_tracking"),
        bind_hook(_finalize_tracking, anchor_set.finalize_tracking.anchor_type, name="finalize_tracking"),
        bind_hook(_record_references, anchor_set.record_references.anchor_type, name="record_references"),
        bind_hook(_save_final_context, anchor_set.save_final_context.anchor_type, name="save_final_context"),
        bind_hook(_run_verdict, anchor_set.run_verdict.anchor_type, name="run_verdict"),
        # Literal anchor-type strings: importing the context anchor catalog
        # here would be circular (it imports define_anchor from this module).
        bind_hook(
            _write_grounding_evidence,
            "context.sync.final_answer.after",
            "context.sync.warning_final_answer.after",
            "context.sync.hard_stop.final_answer.after",
            "context.async.final_answer.after",
            name="write_grounding_evidence",
        ),
    )


def bind_hook(
    callback: Callable[..., Any],
    *anchor_types: str,
    name: str = "",
) -> HookBinding:
    """Declare which anchor types a callback applies to."""
    if not anchor_types:
        raise ValueError("bind_hook() requires at least one anchor type")
    return HookBinding(
        callback=callback,
        anchor_types=tuple(anchor_types),
        name=name or getattr(callback, "__name__", "hook"),
    )


def compile_hooks(
    bindings: Iterable[HookBinding] | EngineHooks | None,
) -> EngineHooks:
    """Compile hook bindings into the dispatch structure used by anchor()."""
    if bindings is None:
        return EMPTY_HOOKS
    if isinstance(bindings, Mapping):
        return bindings

    compiled: dict[str, list[Callable[..., Any]]] = defaultdict(list)
    for binding in bindings:
        for anchor_type in binding.anchor_types:
            compiled[anchor_type].append(binding.callback)
    return {anchor_type: tuple(callbacks) for anchor_type, callbacks in compiled.items()}


def _hook_event_detail(kwargs: Mapping[str, Any]) -> str:
    """Compact, size-bounded kwargs summary for hook event rows."""
    bits: list[str] = []
    iteration = kwargs.get("iteration")
    if isinstance(iteration, int):
        bits.append(f"iter={iteration}")
    tool_name = kwargs.get("tool_name")
    if isinstance(tool_name, str) and tool_name:
        bits.append(f"`{tool_name}`")
    for key, value in kwargs.items():
        if key.endswith("_chars") and isinstance(value, int):
            bits.append(f"{key}={value:,}")
    return " · ".join(bits)


def anchor(
    point: AnchorPoint,
    hooks: EngineHooks | None,
    /,
    *args: Any,
    **kwargs: Any,
) -> Any:
    """Dispatch a catalog-defined anchor point against the compiled hooks map.

    Every dispatch with bound callbacks is recorded in the active run
    history's session event log, and the anchor name rides the label
    activity stack for the duration of the callbacks — nested Argo calls
    therefore carry ``…_[hook name]_[kind]`` labels.  Instrumentation is
    best-effort and never interferes with dispatch.
    """
    if not hooks:
        return None
    callbacks = [
        callback
        for anchor_type in point.anchor_types
        for callback in hooks.get(anchor_type, ())
    ]
    if not callbacks:
        return None

    recorder = None
    activity_token = None
    try:
        recorder = _get_active_history()
        recorder.log_hook_event(
            point.name, len(callbacks), detail=_hook_event_detail(kwargs))
        activity_token = recorder.push_activity(point.name)
    except Exception:
        recorder, activity_token = None, None

    try:
        result = None
        for callback in callbacks:
            value = callback(*args, **kwargs)
            if value is not None:
                result = value
        return result
    finally:
        if recorder is not None and activity_token is not None:
            try:
                recorder.pop_activity(activity_token)
            except Exception:
                pass


# ═══════════════════════════════════════════════════════════════
#  Empty hooks dict (useful as default)
# ═══════════════════════════════════════════════════════════════

EMPTY_HOOKS: EngineHooks = {}


__all__ = [
    "AnchorPoint",
    "AnchorCollection",
    "AgentAnchorCollection",
    "HookBinding",
    "EngineHooks",
    "AgentHookCollection",
    "AGENT_START_TRACKING",
    "AGENT_FINALIZE_TRACKING",
    "AGENT_RECORD_REFERENCES",
    "AGENT_SAVE_FINAL_CONTEXT",
    "AGENT_RUN_VERDICT",
    "define_anchor",
    "define_anchor_collection",
    "bind_hook",
    "build_agent_lifecycle_bindings",
    "compile_hooks",
    "anchor",
    "EMPTY_HOOKS",
]
