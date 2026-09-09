"""
Main agent hook catalog — single entry point.
==============================================
Every external consumer of the main agent context-hooks should import
from here.

1. **Interactive** — ``MainInteractiveCompactor``
2. **Compactors** — ``MainStageCompactor``, ``MainToolResultCompactor``,
   ``ToolResult``, ``COMPACTOR_CATALOG``, ``COMPACTOR_REGISTRY``
3. **Tracking** — ``MainHistoryRecorder``, ``MainStatsRecorder``,
   ``MainTimeBudgetTracker`` + module-level singletons
4. **Verdict** — ``MainVerdictRunner``, ``save_final_context``
5. **Memory** — ``MainWorkingMemory``, ``session_manager``, ``get_session``,
   ``init_session``, ``close_session``
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

# ── Interactive hooks ───────────────────────────────────────
from .interactive_hooks import MainInteractiveCompactor, menu_tool_pre_execution_guidance

# ── Compactor hooks ─────────────────────────────────────────
from .compactor_hooks import (
    MainStageCompactor,
    MainToolResultCompactor,
    ToolResult,
    COMPACTOR_CATALOG,
    COMPACTOR_REGISTRY,
)

# ── Tracking hooks ──────────────────────────────────────────
from .tracking_hooks import (
    MainHistoryRecorder,
    MainStatsRecorder,
    MainTimeBudgetTracker,
    MainReasoningTracker,
)
from .tracking_hooks.reasoning_hooks import main_reasoning_tracker

# Module-level singletons
main_history_recorder = MainHistoryRecorder()
main_stats_recorder = MainStatsRecorder()

# ── Verdict hooks ───────────────────────────────────────────
from .verdict_hooks import MainVerdictRunner, save_final_context

# ── Memory hooks ────────────────────────────────────────────
from .memory_hooks import (
    MainWorkingMemory,
    session_manager,
    get_session,
    init_session,
    reopen_session,
    close_session,
)

from ...general_db_query_engine.general_argo_engine_helpers.engine_hooks_anchors import AgentHookCollection, EngineHooks, bind_hook, build_agent_lifecycle_bindings, compile_hooks
from ...general_db_query_engine.general_hooks_management_helpers.general_context_hooks.context_cleanup_compactor_hooks import (
    compact_tool_calls_for_memory,
    stage_compact_batch,
)
from ...general_db_query_engine.general_hooks_management_helpers.general_context_hooks.self_compactor_interactive_hooks import (
    build_compaction_reminder,
    compact_memory,
    parse_compaction_guidance,
)
from ...general_db_query_engine.general_hooks_management_helpers.general_context_hooks.time_budget_reminder_hooks import TimeBudgetTracker
from ...general_db_query_engine.general_hooks_management_helpers.general_context_hooks import _context_hooks_anchors_catalog as ctx_anchor
from ...general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers import _memory_hooks_anchors_catalog as mem_anchor
from ...general_db_query_engine.general_tool_management_helpers import _tool_hooks_anchors_catalog as tool_anchor


def _compile_engine_hooks(
    *,
    history,
    stats,
    reasoning,
    working_memory_loader=None,
    compactor=None,
    batch_summary=None,
    batch_validator=None,
    verdict_runner=None,
    final_context_saver=None,
    anchors=None,
) -> EngineHooks:
    h = history
    s = stats
    r = reasoning
    effective_compactor = compactor or compact_memory

    bindings = [
        bind_hook(
            r.log_reasoning_from_response,
            ctx_anchor.SYNC_LLM_RESPONSE_AFTER.anchor_type,
            ctx_anchor.SYNC_COMPACTION_GUIDANCE_RESPONSE.anchor_type,
            ctx_anchor.ASYNC_LLM_RESPONSE_AFTER.anchor_type,
        ),
        bind_hook(
            s.log_tool_result,
            tool_anchor.SYNC_TOOL_RESULT_RECORDED.anchor_type,
            tool_anchor.ASYNC_TOOL_RESULT_RECORDED.anchor_type,
        ),
        bind_hook(
            h.log_tool_call,
            tool_anchor.SYNC_TOOL_CALL_RECORDED.anchor_type,
            tool_anchor.ASYNC_TOOL_CALL_RECORDED.anchor_type,
        ),
        bind_hook(
            h.log_error,
            tool_anchor.SYNC_TOOL_ERROR_RECORDED.anchor_type,
            tool_anchor.ASYNC_TOOL_ERROR_RECORDED.anchor_type,
        ),
        bind_hook(
            h.log_purpose_tasks_error,
            tool_anchor.SYNC_TOOL_PURPOSE_ERROR_RECORDED.anchor_type,
            tool_anchor.ASYNC_TOOL_PURPOSE_ERROR_RECORDED.anchor_type,
        ),
        bind_hook(
            h.log_stage_compaction,
            tool_anchor.SYNC_STAGE_COMPACTION_RECORDED.anchor_type,
        ),
        bind_hook(
            h.log_compaction,
            ctx_anchor.SYNC_COMPACTION_RECORDED.anchor_type,
            ctx_anchor.SYNC_COMPACTION_SKIPPED.anchor_type,
        ),
        bind_hook(
            s.log_compaction,
            ctx_anchor.SYNC_COMPACTION_STATS_RECORDED.anchor_type,
            ctx_anchor.SYNC_COMPACTION_SKIPPED.anchor_type,
        ),
        bind_hook(
            lambda timeout, thresholds, max_warnings, **_: TimeBudgetTracker(
                timeout=timeout,
                thresholds=list(thresholds),
                max_warnings=max_warnings,
            ),
            ctx_anchor.SYNC_TIME_BUDGET_TRACKER_CREATE.anchor_type,
            name="build_time_budget_tracker",
        ),
        bind_hook(
            lambda tracker, elapsed, memory, **_: tracker.check_and_inject_warnings(elapsed, memory),
            ctx_anchor.SYNC_TIME_BUDGET_WARNINGS_APPLY.anchor_type,
            name="apply_time_budget_warnings",
        ),
        bind_hook(
            lambda tracker, elapsed, **_: tracker.is_hard_stop(elapsed),
            ctx_anchor.SYNC_TIME_BUDGET_HARD_STOP_CHECK.anchor_type,
            name="check_time_budget_hard_stop",
        ),
        bind_hook(
            lambda tracker, **_: tracker.all_warnings_fired,
            ctx_anchor.SYNC_TIME_BUDGET_ALL_WARNINGS_CHECK.anchor_type,
            name="check_all_time_budget_warnings",
        ),
        bind_hook(
            lambda tracker, **_: tracker.make_final_warning_message(),
            ctx_anchor.SYNC_TIME_BUDGET_FINAL_MESSAGE_BUILD.anchor_type,
            name="build_final_warning_message",
        ),
        bind_hook(
            lambda **_: working_memory_loader() if working_memory_loader else None,
            mem_anchor.SYNC_WORKING_MEMORY_RENDER.anchor_type,
            mem_anchor.ASYNC_WORKING_MEMORY_RENDER.anchor_type,
            name="render_working_memory",
        ),
        bind_hook(
            lambda tool_calls, deferred_count, **_: compact_tool_calls_for_memory(tool_calls, deferred_count),
            tool_anchor.SYNC_TOOL_CALLS_MEMORY_COMPACT.anchor_type,
            tool_anchor.ASYNC_TOOL_CALLS_MEMORY_COMPACT.anchor_type,
            name="compact_tool_calls_for_memory",
        ),
        bind_hook(
            lambda tool_calls, result_parts, note_chars, **_: stage_compact_batch(
                tool_calls, result_parts, note_chars=note_chars,
            ),
            tool_anchor.SYNC_STAGE_COMPACTION_BUILD.anchor_type,
            name="stage_compact_batch",
        ),
        bind_hook(
            lambda total_chars, iteration, **_: build_compaction_reminder(total_chars, iteration),
            ctx_anchor.SYNC_COMPACTION_REMINDER_BUILD.anchor_type,
            name="build_compaction_reminder",
        ),
        bind_hook(
            lambda guidance_response, **_: parse_compaction_guidance(guidance_response),
            ctx_anchor.SYNC_COMPACTION_GUIDANCE_PARSE.anchor_type,
            name="parse_compaction_guidance",
        ),
        bind_hook(
            lambda memory, argo_fn, purpose="", tasks="", **_: effective_compactor(
                memory, argo_fn, purpose=purpose, tasks=tasks,
            ),
            ctx_anchor.SYNC_COMPACTION_EXECUTE.anchor_type,
            ctx_anchor.ASYNC_COMPACTION_EXECUTE.anchor_type,
            name="execute_context_compaction",
        ),
    ]
    # ── Per-tool guidance (anchor-dispatched) ────────────────
    bindings.append(bind_hook(
        menu_tool_pre_execution_guidance,
        tool_anchor.SYNC_TOOL_GUIDANCE_CHECK.anchor_type,
        name="menu_tool_guidance",
    ))
    if batch_summary is not None:
        bindings.append(bind_hook(
            lambda tool_calls, result_parts, **_: batch_summary(tool_calls, result_parts),
            tool_anchor.SYNC_BATCH_SUMMARY_BUILD.anchor_type,
            name="build_batch_summary",
        ))
    if batch_validator is not None:
        bindings.append(bind_hook(
            lambda tool_calls, tools, engine_hooks=None, **_: batch_validator(
                tool_calls, tools, hooks=engine_hooks,
            ),
            tool_anchor.SYNC_BATCH_PRE_VALIDATE.anchor_type,
            name="batch_pre_validate",
        ))
    bindings.extend(build_agent_lifecycle_bindings(
        history=history,
        stats=stats,
        reasoning=reasoning,
        verdict_runner=verdict_runner,
        final_context_saver=final_context_saver,
        anchors=anchors,
    ))
    return compile_hooks(bindings)


@dataclass
class MainAgentHooks(AgentHookCollection):
    history: MainHistoryRecorder = field(default_factory=lambda: main_history_recorder)
    stats: MainStatsRecorder = field(default_factory=lambda: main_stats_recorder)
    reasoning: MainReasoningTracker = field(default_factory=lambda: main_reasoning_tracker)
    working_memory_loader: Callable[[], str] | None = None
    compactor: Callable[..., Any] | None = None
    batch_summary: Callable[..., Any] | None = None
    batch_validator: Callable[..., Any] | None = None
    verdict_runner: Callable[..., Any] = field(default_factory=lambda: MainVerdictRunner().run_verdict)
    final_context_saver: Callable[..., Any] = field(default_factory=lambda: save_final_context)

    def build_engine_hooks(self) -> EngineHooks:
        return _compile_engine_hooks(
            history=self.history,
            stats=self.stats,
            reasoning=self.reasoning,
            working_memory_loader=self.working_memory_loader,
            compactor=self.compactor,
            batch_summary=self.batch_summary,
            batch_validator=self.batch_validator,
            verdict_runner=self.verdict_runner,
            final_context_saver=self.final_context_saver,
            anchors=self.anchors,
        )


def build_agent_hooks(
    history=None,
    stats=None,
    reasoning=None,
    *,
    working_memory_loader=None,
    compactor=None,
    batch_summary=None,
    batch_validator=None,
) -> MainAgentHooks:
    return MainAgentHooks(
        history=history or main_history_recorder,
        stats=stats or main_stats_recorder,
        reasoning=reasoning or main_reasoning_tracker,
        working_memory_loader=working_memory_loader,
        compactor=compactor,
        batch_summary=batch_summary,
        batch_validator=batch_validator,
    )


__all__ = [
    # Interactive
    "MainInteractiveCompactor",
    # Compactors
    "MainStageCompactor",
    "MainToolResultCompactor",
    "ToolResult",
    "COMPACTOR_CATALOG",
    "COMPACTOR_REGISTRY",
    # Tracking
    "MainHistoryRecorder",
    "MainStatsRecorder",
    "MainTimeBudgetTracker",
    "MainReasoningTracker",
    "main_history_recorder",
    "main_stats_recorder",
    "main_reasoning_tracker",
    "MainAgentHooks",
    "build_agent_hooks",
    # Verdict
    "MainVerdictRunner",
    "save_final_context",
    # Memory
    "MainWorkingMemory",
    "session_manager",
    "get_session",
    "init_session",
    "reopen_session",
    "close_session",
]
