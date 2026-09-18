"""
Async ReAct loop — ``async_agent_turn()`` for parallel L2 subagent dispatch.
"""

from __future__ import annotations

import asyncio
import json
import logging
import time
from typing import Callable, Dict, List

from ..engine_config import get_config
from ..argo_client_caller import ArgoClient
from ..engine_tool_interface_helpers.tool_call_parser import extract_all_tool_calls
from .react_helpers import (
    _validate_tool_arguments,
    validate_native_tool_result,
    require_result_within_limit,
    AgentTurnResult,
    _get_compaction_trigger_chars,
)
from ..engine_hooks_anchors import anchor as _anchor, EngineHooks, AGENT_RECORD_REFERENCES as _AGENT_RECORD_REFERENCES

from ...general_hooks_management_helpers.general_context_hooks.context_cleanup_compactor_hooks import (
    SUMMARY_BLOCK_RE as _SUMMARY_BLOCK_RE,
    compact_tool_calls_for_memory as _compact_tool_calls_for_memory,
)
from ...general_hooks_management_helpers.general_context_hooks.self_compactor_interactive_hooks import (
    compact_memory as _compact_memory,
)
from ...general_hooks_management_helpers.general_context_hooks import _context_hooks_anchors_catalog as ctx_anchor
from ...general_hooks_management_helpers.general_memory_management_tools_hooks_helpers import _memory_hooks_anchors_catalog as mem_anchor
from ...general_tool_management_helpers import _tool_hooks_anchors_catalog as tool_anchor
from ...general_text_context_marker_catalog import (
    ALL_CONTEXT_MARKERS_RE as _ALL_MARKERS_RE,
    MARKERS,
    wrap_subagent_answer,
)
from .react_loop import (
    _clean_answer_text,
    _begin_tool_event,
    _end_tool_event,
    _log_answer_event,
    _pop_history_activity,
    _push_history_activity,
)
from .subagent_context_render import build_subagent_context_display

TAG_TOOL_CALL_OPEN = MARKERS.tool_call.open
TAG_TOOL_RESULT_OPEN = MARKERS.tool_result.open
TAG_TOOL_RESULT_CLOSE = MARKERS.tool_result.close
TAG_SUMMARY_OPEN = MARKERS.summary.open
TAG_SUMMARY_CLOSE = MARKERS.summary.close
TAG_SYSTEM_PROMPT_OPEN = MARKERS.system_prompt.open
TAG_SYSTEM_PROMPT_CLOSE = MARKERS.system_prompt.close
TAG_MEMORY_OPEN = MARKERS.memory.open
TAG_MEMORY_CLOSE = MARKERS.memory.close

log = logging.getLogger("ThermoML-UI")

async def async_agent_turn(
    user_message: str,
    *,
    system_prompt: str,
    tools: Dict[str, Callable],
    memory: List[dict],
    client: ArgoClient | None = None,
    max_iterations: int | None = None,
    timeout: int | None = None,
    hooks: EngineHooks | None = None,
    is_subagent: bool = False,
) -> AgentTurnResult:
    """Async version of agent_turn() using ArgoClient.acall().

    Designed for use with asyncio.gather() to run multiple L2
    subagent evaluations in parallel.  Same ReAct loop logic as
    agent_turn(), but uses the async (thread-wrapped) endpoint.
    """
    if not isinstance(user_message, str) or not user_message.strip():
        raise TypeError("user_message must be a non-empty string")
    if not isinstance(system_prompt, str) or not system_prompt.strip():
        raise TypeError("system_prompt must be a non-empty string")
    if not isinstance(tools, dict) or not tools:
        raise TypeError("tools must be a non-empty name-to-callable object")
    for name, fn in tools.items():
        if not isinstance(name, str) or not name or not callable(fn):
            raise TypeError("every tool entry must have a non-empty string name and callable value")
    if not isinstance(memory, list):
        raise TypeError("memory must be a list")
    if not isinstance(is_subagent, bool):
        raise TypeError("is_subagent must be a boolean")

    if client is None:
        client = ArgoClient.with_tier("L2")

    # Build an argo_fn wrapper for the compactor (same as sync loop)
    def _argo_fn(prompt, system, stop=None):
        return client.call(prompt, system, stop=stop)

    _cfg = get_config()
    _max_iter = _cfg.L2_MAX_ITERATIONS if max_iterations is None else max_iterations
    _timeout = _cfg.L2_MAX_SECONDS if timeout is None else timeout
    if isinstance(_max_iter, bool) or not isinstance(_max_iter, int) or _max_iter <= 0:
        raise TypeError("max_iterations must be a positive integer")
    if isinstance(_timeout, bool) or not isinstance(_timeout, int) or _timeout <= 0:
        raise TypeError("timeout must be a positive integer")

    memory.append({"role": "user", "content": user_message})
    _anchor(mem_anchor.ASYNC_USER_MESSAGE_APPEND, hooks,
            iteration=0, content=user_message)
    t0 = time.time()
    tool_history: list[dict] = []

    for iteration in range(1, _max_iter + 1):
        elapsed = time.time() - t0
        if elapsed > _timeout:
            break

        # ── 🔗 Build flat prompt with anchors ────────────
        flat_parts = []
        wm_chars = 0
        wm = _anchor(mem_anchor.ASYNC_WORKING_MEMORY_RENDER, hooks, iteration=iteration)
        if wm:
            wm_part = (
                f"## Working Memory\n"
                f"{TAG_MEMORY_OPEN}\n{wm}\n{TAG_MEMORY_CLOSE}"
            )
            flat_parts.append(wm_part)
            wm_chars = len(wm_part)
        _first_user_seen = False
        user_chars = 0
        asst_chars = 0
        turn_details: list[str] = []
        for turn in memory:
            if turn["role"] == "user" and is_subagent and not _first_user_seen:
                tag = "Subagent"
                _first_user_seen = True
            elif turn["role"] == "user":
                tag = "User"
            else:
                tag = "Assistant"
            part = f"## {tag}\n{turn['content']}"
            flat_parts.append(part)
            plen = len(part)
            if turn["role"] == "user":
                user_chars += plen
            else:
                asst_chars += plen
            turn_details.append(f"{tag[:1]}:{plen}")
        flat_prompt = "\n\n".join(flat_parts)
        _anchor(ctx_anchor.ASYNC_FLAT_PROMPT_BUILD, hooks,
                iteration=iteration, prompt_chars=len(flat_prompt))

        log.info(
            "CTX turn=%d | system=%d wm=%d user=%d asst=%d "
            "total_prompt=%d | turns=[%s]",
            iteration, len(system_prompt), wm_chars,
            user_chars, asst_chars, len(flat_prompt),
            ", ".join(turn_details),
        )

        # ── 🔗 Anchor: LLM_CALL_BEFORE ─────────────────────
        _anchor(ctx_anchor.ASYNC_LLM_CALL_BEFORE, hooks, iteration=iteration)

        # Async LLM call
        _tagged_system = (
            f"{TAG_SYSTEM_PROMPT_OPEN}\n{system_prompt}\n{TAG_SYSTEM_PROMPT_CLOSE}"
        )
        _turn_activity = _push_history_activity(f"Turn#{iteration}")
        try:
            response = await client.acall(flat_prompt, _tagged_system,
                                          event_kind="ReAct")
        finally:
            _pop_history_activity(_turn_activity)

        # ── 🔗 Anchor: LLM_RESPONSE_AFTER + ON_REASONING ───
        _anchor(ctx_anchor.ASYNC_LLM_RESPONSE_AFTER, hooks, iteration, response)

        batch = extract_all_tool_calls(response)
        if not batch.syntax_valid:
            correction = batch.correction_message()
            log.warning(
                "[async] Tool call rejected before execution: %d malformed block(s)",
                len(batch.syntax_errors),
            )
            for error in batch.syntax_errors:
                log.warning("[async] Malformed tool-call detail: %s", error)
            memory.append({"role": "assistant", "content": response})
            memory.append({
                "role": "user",
                "content": correction,
            })
            # Anchor-only — rejected calls never enter tool_history (they
            # would leak into logs, counts, and evaluator summaries).
            for index, error in enumerate(batch.syntax_errors, start=1):
                _anchor(
                    tool_anchor.ASYNC_TOOL_ERROR_RECORDED,
                    hooks,
                    iteration=iteration,
                    tool_name=f"<malformed_tool_call_{index}>",
                    error_text=error,
                    args={},
                )
            continue
        if len(batch.calls) > 1:
            correction = (
                "[TOOL SYNTAX CORRECTION] The asynchronous L2 ReAct engine "
                "accepts exactly one tool call per turn. No tool ran. Re-emit "
                "one canonical <tool_call> block, observe its result, and then "
                "issue the next call."
            )
            memory.append({"role": "assistant", "content": response})
            memory.append({"role": "user", "content": correction})
            continue
        tool_call = batch.calls[0] if batch.calls else None
        if tool_call is None:
            _anchor(ctx_anchor.ASYNC_FINAL_ANSWER_BEFORE, hooks,
                iteration=iteration, answer=response)
            _clean_answer = _clean_answer_text(response)
            memory.append({"role": "assistant", "content": response})
            _anchor(ctx_anchor.ASYNC_FINAL_ANSWER_AFTER, hooks,
                iteration=iteration, answer=_clean_answer,
                tool_history=tool_history)
            _log_answer_event(_clean_answer)
            return AgentTurnResult(
                answer=_clean_answer,
                iterations=iteration,
                elapsed_seconds=time.time() - t0,
                tool_history=tool_history,
            )

        # Execute tool (tools are sync — run in thread to not block)
        tool_name = tool_call.get("name", "")
        raw_args = tool_call.get("arguments", {})
        fn = tools.get(tool_name)

        # Exact name/argument preflight happens before thread dispatch. Invalid
        # input is fed back to ReAct as a correction; the callable is untouched.
        argument_error = ""
        args: dict = {}
        if fn is None:
            argument_error = (
                f"UNKNOWN_TOOL: {tool_name!r} is not registered; available tools "
                f"are {sorted(tools)}"
            )
        else:
            try:
                args = _validate_tool_arguments(tool_name, raw_args, fn)
            except Exception as exc:
                argument_error = str(exc)
        if argument_error:
            correction = (
                "[TOOL ARGUMENT CORRECTION] The tool call was rejected before "
                "execution. No tool ran. Re-emit one canonical call using a "
                "registered name and exact declared JSON arguments.\n"
                f"- {tool_name}: {argument_error}"
            )
            memory.append({"role": "assistant", "content": response})
            memory.append({"role": "user", "content": correction})
            tool_history.append({
                "iteration": iteration,
                "tool": tool_name,
                "args_keys": sorted(raw_args),
                "result_chars": len(correction),
                "result_full": f"[argument blocked] {argument_error}",
                "elapsed_s": 0.0,
            })
            _anchor(
                tool_anchor.ASYNC_TOOL_ERROR_RECORDED,
                hooks,
                iteration=iteration,
                tool_name=tool_name,
                error_text=argument_error,
                args=raw_args,
            )
            continue

        tool_t0 = time.time()
        _tool_event = _begin_tool_event(tool_name)
        try:
            native_result = validate_native_tool_result(
                tool_name, await asyncio.to_thread(fn, **args)
            )
            if isinstance(native_result, dict):
                tool_result = json.dumps(native_result, indent=2)
                if len(tool_result) > 2000:
                    log.debug(
                        "Tool %s returned a raw dict (%d chars) — "
                        "skip-subagent tool (normal for L2)",
                        tool_name, len(tool_result),
                    )
            else:
                tool_result = native_result
        except Exception as e:
            _err_text = str(e)
            if "TOOL_ARGUMENT_REFINEMENT_REQUIRED" in _err_text:
                # agent-input error, not a system failure: relay the
                # refinement message without traceback noise
                log.warning("Tool %s argument refinement required: %s",
                            tool_name, _err_text)
                _err_code = "TOOL_ARGUMENT_REFINEMENT_REQUIRED"
            else:
                log.error("Tool %s execution failed: %s",
                          tool_name, e, exc_info=True)
                _err_code = "TOOL_EXECUTION_ERROR"
            native_result = {
                "error": _err_text,
                "error_code": _err_code,
                "tool": tool_name,
            }
            tool_result = json.dumps(native_result, indent=2)

        if (
            getattr(fn, "_returns_subagent_answer", False)
            and not (
                isinstance(native_result, dict)
                and "error_code" in native_result
            )
        ):
            tool_result = wrap_subagent_answer(tool_result)

        tool_result = require_result_within_limit(tool_name, tool_result)
        tool_elapsed = time.time() - tool_t0

        tool_history.append({
            "iteration": iteration,
            "tool": tool_name,
            "args_keys": sorted(raw_args.keys()) if raw_args else [],
            "result_chars": len(tool_result),
            "elapsed_s": round(tool_elapsed, 1),
        })

        # ── 🔗 Anchor: tool execution hooks ──────────────
        _anchor(tool_anchor.ASYNC_TOOL_RESULT_RECORDED, hooks,
              iteration=iteration, tool_name=tool_name,
              args=raw_args or {}, raw_result_chars=len(tool_result),
              elapsed_s=round(tool_elapsed, 1))

        # ── 🔗 Anchor: AGENT_RECORD_REFERENCES (entity/DOI) ──
        if isinstance(native_result, dict):
            _anchor(_AGENT_RECORD_REFERENCES, hooks,
                    tool_name=tool_name, raw_result=native_result)

        _is_json_err = isinstance(native_result, dict) and "error_code" in native_result
        _is_purpose_err = tool_result.startswith("ERROR: Tool") and "purpose" in tool_result[:200]
        if _is_purpose_err:
            _anchor(tool_anchor.ASYNC_TOOL_PURPOSE_ERROR_RECORDED, hooks,
                  iteration=iteration, tool_name=tool_name,
                  error_text=tool_result)
        elif _is_json_err:
            _anchor(tool_anchor.ASYNC_TOOL_ERROR_RECORDED, hooks,
                  iteration=iteration, tool_name=tool_name,
                  error_text=tool_result, args=raw_args)
        else:
            _anchor(tool_anchor.ASYNC_TOOL_CALL_RECORDED, hooks,
                  iteration=iteration, tool_name=tool_name,
                  args=raw_args or {}, result_chars=len(tool_result),
                  elapsed_s=round(tool_elapsed, 1),
                  result_preview=tool_result[:500],
                  result_full=tool_result)

        _end_tool_event(
            _tool_event, result_chars=len(tool_result),
            error=(tool_result[:300]
                   if (_is_json_err or _is_purpose_err) else ""))

        # Compact tool call XML for memory (same as sync loop)
        # Context-only markdown view for marked subagent results; the
        # anchors/history above keep the JSON tool_result verbatim.
        tool_result = build_subagent_context_display(
            tool_name, fn, native_result, tool_result, tool_history)
        compact_tc = _anchor(
            tool_anchor.ASYNC_TOOL_CALLS_MEMORY_COMPACT,
            hooks,
            tool_calls=[tool_call],
            deferred_count=0,
        )
        if compact_tc is None:
            compact_tc = _compact_tool_calls_for_memory([tool_call], 0)
        tc_idx = response.find(TAG_TOOL_CALL_OPEN)
        kept_prefix = ""
        if tc_idx > 0:
            pre_tc = response[:tc_idx]
            sm = _SUMMARY_BLOCK_RE.search(pre_tc)
            summary_text = sm.group(1).strip() if sm else ""
            if len(summary_text) > _cfg.SUMMARY_MAX_CHARS:
                summary_text = summary_text[:_cfg.SUMMARY_MAX_CHARS] + "…"
            if summary_text:
                kept_prefix = f"{TAG_SUMMARY_OPEN}{summary_text}{TAG_SUMMARY_CLOSE}"
        response = (kept_prefix + "\n" + compact_tc) if kept_prefix else compact_tc
        # ── 🔗 Anchor: MEMORY_APPEND_ASSISTANT ─────────────
        memory.append({"role": "assistant", "content": response})
        _anchor(mem_anchor.ASYNC_ASSISTANT_MESSAGE_APPEND, hooks,
                iteration=iteration, content=response)
        # ── 🔗 Anchor: TOOL_RESULT_INJECT ──────────────────
        memory.append({
            "role": "user",
            "content": f"{TAG_TOOL_RESULT_OPEN}\n{tool_result}\n{TAG_TOOL_RESULT_CLOSE}",
        })
        _anchor(tool_anchor.ASYNC_TOOL_RESULT_INJECT, hooks,
                iteration=iteration, result_chars=len(tool_result))

        # ── LLM-driven context compaction (same as sync loop) ──
        total_chars = sum(len(m["content"]) for m in memory)
        if total_chars > _get_compaction_trigger_chars():
            log.info("[async] Context at %d chars — triggering LLM compaction", total_chars)
            try:
                _receipt = _anchor(
                    ctx_anchor.ASYNC_COMPACTION_EXECUTE,
                    hooks,
                    memory=memory,
                    argo_fn=_argo_fn,
                )
                if _receipt is None:
                    _receipt = _compact_memory(memory, _argo_fn, cfg=_cfg)
                if not isinstance(_receipt, str):
                    raise RuntimeError(
                        "Async context-compaction hook must return a string or None"
                    )
            except Exception as e:
                raise RuntimeError(
                    "Mandatory async context compaction failed; context was not "
                    "trimmed or rewritten by a compatibility path"
                ) from e

    _final_placeholder = "(Max iterations reached — returning partial results)"
    _log_answer_event(_final_placeholder, kind="answer-max-iterations")
    return AgentTurnResult(
        answer=_final_placeholder,
        iterations=_max_iter,
        elapsed_seconds=time.time() - t0,
        tool_history=tool_history,
        timed_out=True,
    )
