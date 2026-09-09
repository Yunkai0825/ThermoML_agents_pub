"""
Query agent hook catalog — single entry point.
===============================================
Every external consumer of the query context-hooks should import from
here.  The module exposes five concerns:

1. **Interactive** — ``QueryInteractiveCompactor``
   (LLM-driven context compaction for the chat loop).
2. **Compactors** — ``QueryStageCompactor``, ``QueryToolResultCompactor``,
   ``ToolResult`` (stage-level and tool-result compaction).
3. **Tracking** — ``QueryHistoryRecorder``, ``QueryStatsRecorder``,
   ``QueryTimeBudgetTracker`` + module-level singletons.
4. **Verdict** — ``QueryVerdictRunner``,
   ``save_final_context`` (post-job scientific review).
5. **Memory** — ``QueryWorkingMemory``, ``L1AutoSaver``,
   ``is_thin_answer``, ``force_data_presentation``.

Usage::

    from .hook_catalog import QueryInteractiveCompactor
    from .hook_catalog import query_history_recorder
    from .hook_catalog import QueryVerdictRunner, save_final_context
    from .hook_catalog import QueryWorkingMemory
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

# ── Interactive hooks ───────────────────────────────────────
from .interactive_hooks import QueryInteractiveCompactor

# ── Compactor hooks ─────────────────────────────────────────
from .compactor_hooks import (
    QueryStageCompactor,
    QueryToolResultCompactor,
    ToolResult,
    COMPACTOR_CATALOG,
    COMPACTOR_REGISTRY,
)

# ── Tracking hooks ──────────────────────────────────────────
from .tracking_hooks import (
    QueryHistoryRecorder,
    QueryStatsRecorder,
    QueryTimeBudgetTracker,
    QueryReasoningTracker,
)
from .tracking_hooks.history_hooks import query_history_recorder
from .tracking_hooks.stats_hooks import query_stats_recorder
from .tracking_hooks.reasoning_hooks import query_reasoning_tracker

# ── Verdict hooks ───────────────────────────────────────────
from .verdict_hooks import (
    QueryVerdictRunner,
    save_final_context,
)

# ── Memory hooks ────────────────────────────────────────────
from .memory_hooks import (
    QueryWorkingMemory,
    L1AutoSaver,
    is_thin_answer,
    force_data_presentation,
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
from specialized_tools_pipelines.property_screening_ranking_tool.interface.agent import (
    validate_screen_property_systems_guidance,
)
from card_db_search_tools.basic_search_tools.advanced_block_search.lifecycle import (
    validate_block_search_adv_batch,
    validate_block_search_adv_guidance,
)


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
    # Default to the agent's cfg-bound interactive compactor: the generic
    # compact_memory has no cfg and raises on any non-SKIP guidance.
    effective_compactor = compactor or QueryInteractiveCompactor().compact

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
            validate_screen_property_systems_guidance,
            tool_anchor.SYNC_TOOL_GUIDANCE_CHECK.anchor_type,
            name="validate_screen_property_systems_arguments",
        ),
        bind_hook(
            validate_block_search_adv_guidance,
            tool_anchor.SYNC_TOOL_GUIDANCE_CHECK.anchor_type,
            name="validate_block_search_adv_preexecution_lifecycle",
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
    if batch_summary is not None:
        bindings.append(bind_hook(
            lambda tool_calls, result_parts, **_: batch_summary(tool_calls, result_parts),
            tool_anchor.SYNC_BATCH_SUMMARY_BUILD.anchor_type,
            name="build_batch_summary",
        ))
    if batch_validator is not None:
        bindings.append(bind_hook(
            lambda tool_calls, tools, engine_hooks=None, **_: (
                validate_block_search_adv_batch(tool_calls)
                or batch_validator(tool_calls, tools, hooks=engine_hooks)
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
class QueryAgentHooks(AgentHookCollection):
    history: QueryHistoryRecorder = field(default_factory=lambda: query_history_recorder)
    stats: QueryStatsRecorder = field(default_factory=lambda: query_stats_recorder)
    reasoning: QueryReasoningTracker = field(default_factory=lambda: query_reasoning_tracker)
    working_memory_loader: Callable[[], str] | None = None
    compactor: Callable[..., Any] | None = None
    batch_summary: Callable[..., Any] | None = None
    batch_validator: Callable[..., Any] | None = None
    verdict_runner: Callable[..., Any] = field(default_factory=lambda: QueryVerdictRunner().run_verdict)
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
) -> QueryAgentHooks:
    return QueryAgentHooks(
        history=history or query_history_recorder,
        stats=stats or query_stats_recorder,
        reasoning=reasoning or query_reasoning_tracker,
        working_memory_loader=working_memory_loader,
        compactor=compactor,
        batch_summary=batch_summary,
        batch_validator=batch_validator,
    )


__all__ = [
    # Interactive
    "QueryInteractiveCompactor",
    # Compactors
    "QueryStageCompactor", "QueryToolResultCompactor", "ToolResult",
    "COMPACTOR_CATALOG", "COMPACTOR_REGISTRY",
    # Tracking (classes)
    "QueryHistoryRecorder", "QueryStatsRecorder", "QueryTimeBudgetTracker",
    "QueryReasoningTracker",
    # Tracking (singletons)
    "query_history_recorder", "query_stats_recorder",
    "query_reasoning_tracker",
    # Hook collection
    "QueryAgentHooks", "build_agent_hooks",
    # Verdict
    "QueryVerdictRunner", "save_final_context",
    # Memory
    "QueryWorkingMemory",
    "L1AutoSaver",
    "is_thin_answer", "force_data_presentation",
]
