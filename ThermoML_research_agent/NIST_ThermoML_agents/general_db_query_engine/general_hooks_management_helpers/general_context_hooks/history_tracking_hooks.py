"""
Real-time history recording helper — ``history_tracking_hooks.py``
==================================================================
Context-propagating recorder that builds a rich Markdown
history file incrementally.  Designed to be called from:

  - ``react_loop.py``    — after each tool call / compaction event
  - ``_tool_subagent.py`` — after subagent verdict (KEEP/DISCARD/oversized)
  - ``_wrap_tool()``      — when purpose/tasks are missing (error guard)
  - test runners          — start_run() / flush()

The recorder is 100% harmless — it never modifies conversation context,
working memory, or any tool results.  It only writes to disk.

**Task isolation:** A ``ContextVar`` carries one explicit ``_RunState``
through delegated ``asyncio.to_thread()`` calls.  Parallel agent runs
therefore remain isolated while every delegated result is recorded in
the parent run.

**Session event log (real-time):** every ``_RunState`` owns a unique
8-hex ``session_id``; Argo (LLM) calls, hook dispatches, tool/subagent
dispatches, and shipped answers are appended as ``_SessionEvent`` rows
rendered in the sibling ``<history>_detailed.md`` file ("## Session
Event Log" + "## Agent Outputs (verbatim)"), each carrying the stacked
label ``[session]_[root…]_[section…]_[activity…]_[kind]``
(e.g. ``[2e48c370]_[Main]_[Q#1]_[L1#1]_[Tool#3]_[inspection]``).  The
detailed file is joined to the tool history by the shared session id
and the canonical step tags ``cN`` (step header ``[… · cN]`` ↔ tool
event-row ``cN``).  All agent-generated texts (LLM responses, answers)
are retained verbatim so the session's context/id/block/pts evolution
can be replayed with zero loss of steps.

Usage::

    from ...general_context_hooks.history_tracking_hooks import history_recorder

    history_recorder.start_run(agent="query-agent", prompt="...", out_path="...")
    history_recorder.log_tool_call(iteration=1, tool_name="search_system_registry",
                                   args={...}, result_chars=1234, elapsed_s=2.1,
                                   result_full="full delivered result text")
    history_recorder.log_subagent_event(tool_name="search_system_registry",
                                        event="KEEP", detail="extracted 5 rows")
    history_recorder.log_compaction(iteration=3, before_chars=80000,
                                    after_chars=30000, trigger="interval=3")
    history_recorder.log_error(iteration=2, tool_name="bad_tool",
                               error_text="Unknown tool: bad_tool")
    history_recorder.flush()        # writes to out_path
    history_recorder.reset()
"""

from __future__ import annotations

import datetime as dt
import json
import logging
import re
import threading
import uuid
from contextvars import ContextVar
from dataclasses import dataclass, field
from pathlib import Path
from ..general_memory_management_tools_hooks_helpers.session_manager_output_storage import (
    _filesystem_path,
    ensure_directory,
)
from typing import Any, Dict, List, Optional

log = logging.getLogger("history-recorder")


# ═══════════════════════════════════════════════════════════════
#  Data containers
# ═══════════════════════════════════════════════════════════════

@dataclass
class _ToolEntry:
    """One tool invocation record."""
    iteration: int
    tool_name: str
    args: Dict[str, Any]
    result_chars: int
    elapsed_s: float
    result_preview: str = ""
    result_full: str = ""           # full delivered result text (verbatim)
    # Chronology / nesting
    seq: int = 0                    # global call index across all sections
    section: str = ""               # nested-section id ("" = own lane)
    started_ts: str = ""            # wall-clock initiation HH:MM:SS
    started_offset_s: float = -1.0  # initiation offset from run start
    # Enrichment flags
    is_error: bool = False
    error_text: str = ""
    is_oversized_guard: bool = False
    oversized_notice: str = ""
    is_purpose_error: bool = False
    purpose_error_text: str = ""
    is_validation_block: bool = False
    validation_status: str = ""       # "blocked" | "held-back-by-batch"


@dataclass
class _SubagentEvent:
    """Subagent verdict for a tool call."""
    tool_name: str
    event: str        # "KEEP", "DISCARD", "OVERSIZED", "ERROR"
    detail: str = ""
    output_chars: int = 0
    elapsed_s: float = 0.0
    input_chars: int = 0   # hardcoded-compacted markdown fed to the subagent
    section: str = ""      # nested-section id ("" = own lane)


@dataclass
class _CompactionPipelineEvent:
    """Per-call two-stage compaction sizes: native → hardcoded → agentic."""
    tool_name: str
    pipeline: str          # catalog pipeline_label ("query" | "analysis" | ...)
    native_chars: int      # serialized raw dict returned by the tool
    compact_chars: int     # after Layer-1 deterministic compactor
    final_chars: int       # after Layer-2 subagent (== compact_chars when skipped)
    verdict: str           # "KEEP" | "DISCARD" | "SKIP"
    section: str = ""      # nested-section id ("" = own lane)


@dataclass
class _CompactionEvent:
    """Context compaction event."""
    iteration: int
    before_chars: int
    after_chars: int
    trigger: str = ""     # "interval=3", "chars=80000>60000"
    purpose: str = ""
    tasks: str = ""
    receipt: str = ""     # what was compacted (tool names, char reductions)
    outcome: str = ""     # "compacted", "skipped_by_agent", "skipped_by_selector", "error"
    section: str = ""     # nested-section id ("" = own lane)


@dataclass
class _StageCompactionEvent:
    """Parallel-batch stage compaction."""
    iteration: int
    n_tools: int
    before_chars: int
    after_chars: int
    section: str = ""     # nested-section id ("" = own lane)


@dataclass
class _NestedSection:
    """One nested agent lane: an in-process worker (its tool calls are
    recorded in this history under the section id) or a saved child
    session (own run_history.md, linked by path)."""
    sid: str                    # "L1_1", "L2_2", "Q_1", "A_1", ...
    label: str                  # descriptive kind ("L1-query", "L2-comp eval")
    launcher_tool: str          # parent-side relay tool that launched it
    parent: str = ""            # enclosing section id ("" = own lane)
    started_ts: str = ""
    ended_ts: str = ""
    claimed_by_seq: int = 0     # seq of the parent-side relay entry
    child_history_path: str = ""  # saved child session's history file


@dataclass
class _InternalError:
    """An internal engine error (type mismatch, reference-tracking failure, etc.).

    Stored in run history so batch runs can be post-mortem analysed.
    """
    source: str              # e.g. "react_loop", "stats_references", "engine_hooks"
    error_type: str          # e.g. "json_parse", "type_mismatch", "anchor_callback"
    tool_name: str           # tool that was being processed when the error occurred
    message: str             # short description
    context_preview: str     # first N chars of the data that caused the error
    timestamp: str = ""      # ISO timestamp


@dataclass
class _SessionEvent:
    """One entry of the real-time session event log: an Argo (LLM) call,
    a hook dispatch, a tool/subagent dispatch, or a shipped answer.
    Every event carries the full stacked label
    ``[session]_[root…]_[section…]_[activity…]_[kind]`` so the whole
    context/id/block/pts evolution can be rebuilt step by step."""
    seq: int                 # event index (E1, E2, … per session)
    kind: str                # "argo" | "hook" | "tool" | "answer"
    label: str               # full stacked label
    ts: str                  # wall-clock HH:MM:SS at event creation
    offset_s: float = -1.0   # offset from run start
    status: str = ""         # "pending" | "running" | "ok" | "error"
    detail: str = ""         # compact free-text (tool name, hook kwargs, …)
    model: str = ""          # argo: model name
    tier: str = ""           # argo: stats tier label
    system_chars: int = 0    # argo: system prompt size
    prompt_chars: int = 0    # argo: flat prompt size
    response_chars: int = 0  # argo/tool/answer: output size
    elapsed_s: float = -1.0  # call duration (when known)
    attempts: int = 0        # argo: attempt count incl. retries
    text: str = ""           # verbatim agent-generated output
    error: str = ""          # short error text (status == "error")


# ═══════════════════════════════════════════════════════════════
#  Thread-local run state
# ═══════════════════════════════════════════════════════════════

@dataclass
class _RunState:
    """Per-thread state container for one recording session."""
    agent: str = ""
    prompt: str = ""
    nest_root: str = ""         # breadcrumb base: "main", "Q", "main - A_1", ...
    out_path: Optional[Path] = None
    started_at: Optional[dt.datetime] = None
    tool_entries: List[_ToolEntry] = field(default_factory=list)
    subagent_events: List[_SubagentEvent] = field(default_factory=list)
    pipeline_events: List[_CompactionPipelineEvent] = field(default_factory=list)
    compaction_events: List[_CompactionEvent] = field(default_factory=list)
    stage_compactions: List[_StageCompactionEvent] = field(default_factory=list)
    internal_errors: List[_InternalError] = field(default_factory=list)
    sections: List[_NestedSection] = field(default_factory=list)
    seq_counter: int = 0
    session_id: str = ""        # unique per recording session (8-hex)
    events: List[_SessionEvent] = field(default_factory=list)
    event_counter: int = 0
    tool_dispatch_counts: Dict[str, int] = field(default_factory=dict)
    working_memory: str = ""
    final_status: str = ""


# ── Nest-path plumbing (shared across all recorder instances) ──

#: Set by a parent session around a child launch; consumed by the
#: child's ``start_run`` so its step headers render the full nest
#: path (e.g. "main - A_1 - L1_2 - L2_1").
_pending_nest_prefix: ContextVar[str] = ContextVar(
    "thermoml_history_pending_nest_prefix", default="")


def set_pending_nest_prefix(prefix: str):
    """Declare the nest path the next child session renders under."""
    return _pending_nest_prefix.set(prefix)


def reset_pending_nest_prefix(token) -> None:
    """Clear a prefix set with :func:`set_pending_nest_prefix`."""
    try:
        _pending_nest_prefix.reset(token)
    except ValueError:
        _pending_nest_prefix.set("")   # token from another context copy


def _short_agent_root(agent: str) -> str:
    """Standard root identity for breadcrumbs: main / Q / A."""
    a = (agent or "").lower()
    if "main" in a:
        return "main"
    if a.startswith("query"):
        return "Q"
    if a.startswith("analysis"):
        return "A"
    return agent or "run"


def _section_layer(label: str) -> str:
    """Sid prefix for a nested section label ("L1-query" → "L1")."""
    if label.startswith("L1"):
        return "L1"
    if label.startswith("L2"):
        return "L2"
    return re.sub(r"\W+", "", label) or "S"


_SID_TOKEN_RE = re.compile(r"^([A-Za-z]+\d*)_(\d+)$")


def _label_token(part: str) -> str:
    """One breadcrumb token in label form: main → Main, L1_2 → L1#2."""
    part = part.strip()
    if part.lower() == "main":
        return "Main"
    m = _SID_TOKEN_RE.match(part)
    if m:
        return f"{m.group(1)}#{m.group(2)}"
    return part


#: Deterministic data-inspection tools — their dispatch events carry the
#: ``inspection`` kind in the session event log labels.
_INSPECTION_TOOL_NAMES = frozenset(
    {"inspect_block_table", "inspect_batch_result", "inspect_block"})


# ═══════════════════════════════════════════════════════════════
#  HistoryRecorder — singleton with thread-local state
# ═══════════════════════════════════════════════════════════════

class HistoryRecorder:
    """Accumulates tool history and writes incremental Markdown.

    Each logical agent run owns one context-propagating ``_RunState``.
    A re-entrant lock serializes incremental file writes from workers.
    """

    def __init__(self):
        self._state_ref: ContextVar[_RunState | None] = ContextVar(
            f"thermoml_history_state_{id(self)}", default=None
        )
        # context-local current nested-section id: parallel in-process
        # workers (context copies) tag their entries independently
        self._section_ref: ContextVar[str] = ContextVar(
            f"thermoml_history_section_{id(self)}", default=""
        )
        # context-local activity stack: Turn#N / Tool#N / hook-name
        # segments appended to event labels (parallel-safe)
        self._activity_ref: ContextVar[tuple] = ContextVar(
            f"thermoml_history_activity_{id(self)}", default=()
        )
        self._flush_lock = threading.RLock()

    # ── Internal: get/create the current thread's state ────

    def _state(self) -> _RunState:
        """Return the current thread's _RunState (create if needed)."""
        s = self._state_ref.get()
        if s is None:
            s = _RunState()
            self._state_ref.set(s)
        return s

    # ── Lifecycle ──────────────────────────────────────────────

    def start_run(
        self,
        agent: str,
        prompt: str,
        out_path: str | Path | None = None,
    ) -> None:
        """Begin a new recording session (resets state for this thread)."""
        s = _RunState(
            agent=agent,
            prompt=prompt,
            nest_root=_pending_nest_prefix.get() or _short_agent_root(agent),
            out_path=Path(out_path) if out_path is not None else None,
            started_at=dt.datetime.now(),
            session_id=uuid.uuid4().hex[:8],
        )
        self._state_ref.set(s)
        self._section_ref.set("")
        self._activity_ref.set(())
        log.debug("History recorder started for %s → %s", agent, out_path)

    def reset(self) -> None:
        """Clear all accumulated state for this thread."""
        self._state_ref.set(_RunState())

    def set_working_memory(self, text: str) -> None:
        """Set the working memory snapshot (appended at end of history)."""
        self._state().working_memory = text

    def set_final_status(self, status: str) -> None:
        """Set final run status (OK / TIMEOUT / ERROR)."""
        self._state().final_status = status

    # ── Nested sections (layered tool history) ─────────────────

    def begin_nested_section(self, label: str, launcher_tool: str):
        """Open a nested lane: entries logged in THIS context land in it
        until the returned handle is passed to ``end_nested_section``.
        Nesting stacks (an L2 evaluator inside an L1 worker records with
        the L1 section as parent)."""
        with self._flush_lock:
            s = self._state()
            parent = self._section_ref.get()
            layer = _section_layer(label)
            n = 1 + sum(1 for sec in s.sections
                        if sec.sid.startswith(f"{layer}_"))
            sid = f"{layer}_{n}"
            s.sections.append(_NestedSection(
                sid=sid, label=label, launcher_tool=launcher_tool,
                parent=parent,
                started_ts=dt.datetime.now().strftime("%H:%M:%S")))
        token = self._section_ref.set(sid)
        return (sid, token)

    def end_nested_section(self, handle) -> None:
        """Close a nested lane opened by ``begin_nested_section``."""
        sid, token = handle
        try:
            self._section_ref.reset(token)
        except ValueError:
            self._section_ref.set("")   # token from another context copy
        with self._flush_lock:
            for sec in self._state().sections:
                if sec.sid == sid and not sec.ended_ts:
                    sec.ended_ts = dt.datetime.now().strftime("%H:%M:%S")
                    break
        self._auto_flush()

    def reserve_child_session(self, tool_name: str, label: str,
                              short: str) -> str:
        """Allocate a child session's nest identity ("Q_1", "A_2") BEFORE
        launch so the child can render the full nest path in its own
        history.  Pair with ``finalize_child_session``."""
        with self._flush_lock:
            s = self._state()
            n = 1 + sum(1 for sec in s.sections
                        if sec.sid.startswith(f"{short}_"))
            sid = f"{short}_{n}"
            s.sections.append(_NestedSection(
                sid=sid, label=label, launcher_tool=tool_name,
                parent=self._section_ref.get(),
                started_ts=dt.datetime.now().strftime("%H:%M:%S")))
        return sid

    def finalize_child_session(self, sid: str, history_path) -> None:
        """Link the finished child's run_history.md to its reserved section."""
        with self._flush_lock:
            for sec in self._state().sections:
                if sec.sid == sid and not sec.child_history_path:
                    sec.child_history_path = str(history_path)
                    sec.ended_ts = dt.datetime.now().strftime("%H:%M:%S")
                    break
        self._auto_flush()

    def has_child_session(self, history_path) -> bool:
        """True when a child session with this history file is registered."""
        target = str(history_path)
        return any(sec.child_history_path == target
                   for sec in self._state().sections)

    def context_identity(self) -> tuple[str, str]:
        """(agent, current nested-section sid) for context-render captions."""
        s = self._state_ref.get()
        return ((s.agent if s else "") or "", self._section_ref.get() or "")

    def resolve_child_sid(self, tool_name: str, payload: dict,
                          result_text: str = "",
                          layer_prefix: str = "") -> str:
        """Sid of the section / child session that produced one subagent
        envelope ("" when unresolvable).  Joins, in order: envelope
        ``_session_dir`` ↔ ``section.child_history_path``; the delivered
        result string ↔ its relay entry → uniquely claimed section; first
        ``inspection_id`` ↔ a section-tagged in-process worker entry."""
        with self._flush_lock:
            s = self._state()
            sess = ""
            if isinstance(payload, dict):
                sess = str(payload.get("_session_dir")
                           or payload.get("session_dir") or "")
            if sess:
                sess_norm = str(Path(sess))
                for sec in reversed(s.sections):
                    p = sec.child_history_path
                    if p and str(Path(p).parent) == sess_norm:
                        return sec.sid
            if result_text:
                entry = next((e for e in reversed(s.tool_entries)
                              if e.result_full == result_text), None)
                if entry is not None:
                    claimed = [sec for sec in s.sections
                               if sec.claimed_by_seq == entry.seq]
                    if len(claimed) == 1:
                        return claimed[0].sid
            if isinstance(payload, dict) and "answer" in payload:
                insp = payload.get("data_inspections")
                iid = ""
                if isinstance(insp, list) and insp and isinstance(insp[0], dict):
                    iid = str(insp[0].get("inspection_id") or "")
                if iid:
                    for e in reversed(s.tool_entries):
                        if (e.section and iid in e.result_full
                                and (not layer_prefix or e.section.startswith(
                                    f"{layer_prefix}_"))):
                            return e.section
        return ""

    def child_nest_prefix(self, sid: str) -> str:
        """Full nest path a reserved child session renders under."""
        s = self._state()
        return f"{self._nest_path(s, self._section_ref.get())} - {sid}"

    def log_child_session(self, tool_name: str, label: str,
                          history_path, short: str = "") -> None:
        """Register a saved child agent session (its tool calls live in
        its OWN run_history.md) as a nested section linked by path.
        No-op when the child already self-registered."""
        if self.has_child_session(history_path):
            return
        sid = self.reserve_child_session(
            tool_name, label,
            short or (label[:1].upper() if label else "S"))
        self.finalize_child_session(sid, history_path)

    def _stamp_entry(self, entry: _ToolEntry, elapsed_s: float = 0.0) -> None:
        """Assign the global call index, owning section, and initiation
        wall time (log time minus tool elapsed)."""
        s = self._state()
        s.seq_counter += 1
        entry.seq = s.seq_counter
        entry.section = self._section_ref.get()
        started = dt.datetime.now() - dt.timedelta(
            seconds=max(elapsed_s, 0.0))
        entry.started_ts = started.strftime("%H:%M:%S")
        if s.started_at:
            entry.started_offset_s = (started - s.started_at).total_seconds()

    def _claim_sections(self, entry: _ToolEntry) -> None:
        """Attach finished, unclaimed nested sections to the relay entry
        that just returned them (parent/child pointers both ways)."""
        for sec in self._state().sections:
            if (sec.claimed_by_seq == 0
                    and sec.parent == entry.section
                    and sec.launcher_tool == entry.tool_name
                    and (sec.ended_ts or sec.child_history_path)):
                sec.claimed_by_seq = entry.seq

    # ── Logging hooks ──────────────────────────────────────────

    def log_tool_call(
        self,
        iteration: int,
        tool_name: str,
        args: Dict[str, Any],
        result_chars: int,
        elapsed_s: float,
        result_preview: str = "",
        result_full: str = "",
    ) -> None:
        """Record a tool invocation (called from react_loop after each tool)."""
        entry = _ToolEntry(
            iteration=iteration,
            tool_name=tool_name,
            args=args,
            result_chars=result_chars,
            elapsed_s=elapsed_s,
            result_preview=result_preview[:500],
            result_full=result_full,
        )
        with self._flush_lock:
            self._stamp_entry(entry, elapsed_s)
            self._state().tool_entries.append(entry)
            self._claim_sections(entry)
        self._auto_flush()

    def log_error(
        self,
        iteration: int,
        tool_name: str,
        error_text: str,
        args: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Record a tool-level error (exception, unknown tool, etc.)."""
        entry = _ToolEntry(
            iteration=iteration,
            tool_name=tool_name,
            args=args or {},
            result_chars=len(error_text),
            elapsed_s=0.0,
            result_preview=error_text[:500],
            is_error=True,
            error_text=error_text,
        )
        with self._flush_lock:
            self._stamp_entry(entry)
            self._state().tool_entries.append(entry)
            self._claim_sections(entry)   # crashed relays still ran a worker
        self._auto_flush()

    def log_validation_block(
        self,
        iteration: int,
        tool_name: str,
        status: str = "blocked",
        detail: str = "",
        args: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Record a tool blocked (or held back) by pre-execution validation."""
        entry = _ToolEntry(
            iteration=iteration,
            tool_name=tool_name,
            args=args or {},
            result_chars=len(detail),
            elapsed_s=0.0,
            result_preview=detail,
            is_validation_block=True,
            validation_status=status,
        )
        with self._flush_lock:
            self._stamp_entry(entry)
            self._state().tool_entries.append(entry)
        self._auto_flush()

    def log_purpose_tasks_error(
        self,
        iteration: int,
        tool_name: str,
        error_text: str,
    ) -> None:
        """Record when purpose/tasks were missing (mandatory-param guard)."""
        entry = _ToolEntry(
            iteration=iteration,
            tool_name=tool_name,
            args={},
            result_chars=len(error_text),
            elapsed_s=0.0,
            result_preview=error_text[:500],
            is_purpose_error=True,
            purpose_error_text=error_text,
        )
        with self._flush_lock:
            self._stamp_entry(entry)
            self._state().tool_entries.append(entry)
        self._auto_flush()

    def log_oversized_guard(
        self,
        tool_name: str,
        compact_chars: int,
        notice: str,
    ) -> None:
        """Record when the oversized-result guard triggered."""
        s = self._state()
        for entry in reversed(s.tool_entries):
            if entry.tool_name == tool_name:
                entry.is_oversized_guard = True
                entry.oversized_notice = notice[:2000]
                break
        self._auto_flush()

    def log_subagent_event(
        self,
        tool_name: str,
        event: str,
        detail: str = "",
        output_chars: int = 0,
        elapsed_s: float = 0.0,
        input_chars: int = 0,
    ) -> None:
        """Record a subagent verdict (KEEP, DISCARD, OVERSIZED, ERROR)."""
        ev = _SubagentEvent(
            tool_name=tool_name,
            event=event,
            detail=detail[:500],
            output_chars=output_chars,
            elapsed_s=elapsed_s,
            input_chars=input_chars,
            section=self._section_ref.get(),
        )
        self._state().subagent_events.append(ev)
        self._auto_flush()

    def log_compaction_pipeline(
        self,
        tool_name: str,
        pipeline: str,
        native_chars: int,
        compact_chars: int,
        final_chars: int,
        verdict: str,
    ) -> None:
        """Record one tool call's full compaction chain (native → hardcoded → agentic)."""
        ev = _CompactionPipelineEvent(
            tool_name=tool_name,
            pipeline=pipeline,
            native_chars=native_chars,
            compact_chars=compact_chars,
            final_chars=final_chars,
            verdict=verdict,
            section=self._section_ref.get(),
        )
        self._state().pipeline_events.append(ev)
        self._auto_flush()

    def log_compaction(
        self,
        iteration: int,
        before_chars: int,
        after_chars: int,
        trigger: str = "",
        purpose: str = "",
        tasks: str = "",
        receipt: str = "",
        outcome: str = "",
    ) -> None:
        """Record a context compaction event."""
        ev = _CompactionEvent(
            iteration=iteration,
            before_chars=before_chars,
            after_chars=after_chars,
            trigger=trigger,
            purpose=purpose,
            tasks=tasks,
            receipt=receipt,
            outcome=outcome,
            section=self._section_ref.get(),
        )
        self._state().compaction_events.append(ev)
        self._auto_flush()

    def log_internal_error(
        self,
        source: str,
        error_type: str,
        tool_name: str,
        message: str,
        context_preview: str = "",
    ) -> None:
        """Record an internal engine error for post-mortem batch analysis.

        These are non-fatal errors (type mismatches, failed JSON parses,
        hook callback failures) that don't stop execution but indicate
        data-shape issues worth investigating.
        """
        entry = _InternalError(
            source=source,
            error_type=error_type,
            tool_name=tool_name,
            message=message[:500],
            context_preview=context_preview[:500],
            timestamp=dt.datetime.now().strftime("%H:%M:%S"),
        )
        self._state().internal_errors.append(entry)
        self._auto_flush()

    def log_stage_compaction(
        self,
        iteration: int,
        n_tools: int,
        before_chars: int,
        after_chars: int,
    ) -> None:
        """Record a parallel-batch stage compaction event."""
        ev = _StageCompactionEvent(
            iteration=iteration,
            n_tools=n_tools,
            before_chars=before_chars,
            after_chars=after_chars,
            section=self._section_ref.get(),
        )
        self._state().stage_compactions.append(ev)
        self._auto_flush()

    # ── Session event log (Argo calls, hooks, dispatches, answers) ──

    def push_activity(self, segment: str):
        """Push one label segment (``Turn#2``, ``Tool#5``, a hook name)
        onto the context-local activity stack; returns a reset token."""
        cur = self._activity_ref.get()
        return self._activity_ref.set(cur + (str(segment),))

    def pop_activity(self, token) -> None:
        """Pop a segment pushed with :meth:`push_activity`."""
        try:
            self._activity_ref.reset(token)
        except ValueError:                 # token from another context copy
            cur = self._activity_ref.get()
            if cur:
                self._activity_ref.set(cur[:-1])

    def event_label(self, kind: str = "") -> str:
        """Full stacked label for the current context:
        ``[session]_[root…]_[section…]_[activity…]_[kind]``
        (e.g. ``[2e48c370]_[Main]_[Q#1]_[L1#1]_[Tool#3]_[inspection]``)."""
        s = self._state()
        tokens: List[str] = [s.session_id or "session"]
        for part in self._nest_parts(s, self._section_ref.get()):
            for piece in part.split(" - "):
                tokens.append(_label_token(piece))
        tokens.extend(self._activity_ref.get())
        if kind:
            tokens.append(kind)
        return "_".join(f"[{t}]" for t in tokens)

    def _new_event(self, kind: str, label: str, **kw) -> _SessionEvent:
        """Append one session event (caller decides whether to flush)."""
        with self._flush_lock:
            s = self._state()
            s.event_counter += 1
            now = dt.datetime.now()
            offset = ((now - s.started_at).total_seconds()
                      if s.started_at else -1.0)
            ev = _SessionEvent(
                seq=s.event_counter, kind=kind, label=label,
                ts=now.strftime("%H:%M:%S"), offset_s=offset, **kw)
            s.events.append(ev)
            return ev

    def begin_argo_event(self, *, tier: str = "", model: str = "",
                         system_chars: int = 0, prompt_chars: int = 0,
                         kind: str = "") -> _SessionEvent:
        """Record an Argo API request the moment it is issued (status
        ``pending``) and flush so the on-disk log is real-time."""
        ev = self._new_event(
            "argo", self.event_label(kind or tier or "argo"),
            status="pending", tier=tier, model=model,
            system_chars=system_chars, prompt_chars=prompt_chars)
        self._auto_flush()
        return ev

    def end_argo_event(self, event: _SessionEvent, *,
                       response_chars: int = 0, elapsed_s: float = -1.0,
                       attempts: int = 0, status: str = "ok",
                       response_text: str = "", error: str = "") -> None:
        """Complete a pending Argo event (verbatim response retained)."""
        event.response_chars = response_chars
        event.elapsed_s = elapsed_s
        event.attempts = attempts
        event.status = status
        event.text = response_text
        event.error = error[:300]
        self._auto_flush()

    def log_hook_event(self, hook_name: str, n_callbacks: int,
                       detail: str = "") -> None:
        """Record one anchor/hook dispatch (no flush — piggybacks on the
        next flushing event to keep hot anchors cheap)."""
        bits = f"n={n_callbacks}" + (f" · {detail}" if detail else "")
        self._new_event("hook", self.event_label(hook_name),
                        status="ok", detail=bits)

    def begin_tool_activity(self, tool_name: str):
        """Open one tool/subagent dispatch: allocates the per-section
        ``Tool#k`` ordinal, pushes it on the activity stack, and records
        a real-time ``running`` event.  Returns an opaque handle for
        :meth:`end_tool_activity`."""
        with self._flush_lock:
            s = self._state()
            sec = self._section_ref.get()
            k = s.tool_dispatch_counts.get(sec, 0) + 1
            s.tool_dispatch_counts[sec] = k
            entries_before = len(s.tool_entries)
        token = self.push_activity(f"Tool#{k}")
        kind = ("inspection" if tool_name in _INSPECTION_TOOL_NAMES
                else tool_name)
        ev = self._new_event("tool", self.event_label(kind),
                             status="running",
                             detail=f"`{tool_name}` · Tool#{k}")
        self._auto_flush()
        return (token, ev, sec, tool_name, entries_before,
                dt.datetime.now())

    def end_tool_activity(self, handle, *, result_chars: int = 0,
                          error: str = "") -> None:
        """Close a dispatch opened by :meth:`begin_tool_activity` and
        join the event to its recorded history entry (``cN``)."""
        token, ev, sec, tool_name, entries_before, started = handle
        self.pop_activity(token)
        with self._flush_lock:
            s = self._state()
            entry = next(
                (e for e in reversed(s.tool_entries[entries_before:])
                 if e.section == sec and e.tool_name == tool_name), None)
            if entry is not None:
                ev.detail += f" · c{entry.seq}"
        ev.response_chars = result_chars
        ev.elapsed_s = (dt.datetime.now() - started).total_seconds()
        ev.status = "error" if error else "ok"
        ev.error = error[:300]
        self._auto_flush()

    def log_answer_event(self, answer_text: str,
                         kind: str = "answer") -> None:
        """Record a shipped answer (verbatim) as a session event."""
        self._new_event("answer", self.event_label(kind), status="ok",
                        response_chars=len(answer_text),
                        text=answer_text)
        self._auto_flush()

    # ── Rendering ──────────────────────────────────────────────

    def _auto_flush(self) -> None:
        """Write history to disk if an output path is configured."""
        s = self._state()
        if s.out_path:
            with self._flush_lock:
                self.flush()

    def flush(self, path: Optional[str | Path] = None) -> None:
        """Write the tool-history markdown (and, when session events
        exist, the sibling ``*_detailed`` event/verbatim log) to disk."""
        s = self._state()
        out = Path(path) if path else s.out_path
        if not out:
            return
        md = self._render_markdown()
        ensure_directory(out.parent)
        _filesystem_path(out).write_text(md, encoding="utf-8")
        if s.events:
            detailed = out.with_name(
                f"{out.stem}_detailed{out.suffix or '.md'}")
            _filesystem_path(detailed).write_text(
                self._render_detailed_markdown(out.name), encoding="utf-8")

    def current_out_dir(self) -> Optional[Path]:
        """Directory of this context's history file (None when unset)."""
        s = self._state_ref.get()
        return s.out_path.parent if s is not None and s.out_path else None

    def export_section_history(self, sid: str, out_path: str | Path, *,
                               agent: str = "", prompt: str = "",
                               working_memory: str = "",
                               final_status: str = "") -> None:
        """Write one nested section (plus its descendant sections) as a
        standalone run_history.md (+ sibling detailed log) — the same
        artifact shape a saved child session gets.  The parent history is
        untouched: entries are copies re-rooted on the section lane."""
        from dataclasses import replace as _dc_replace
        out = Path(out_path)
        with self._flush_lock:
            s = self._state()
            by_sid = {sec.sid: sec for sec in s.sections}
            if sid not in by_sid:
                raise KeyError(f"nested section {sid!r} not recorded")
            kept = {sid}
            grew = True
            while grew:
                grew = False
                for sec in s.sections:
                    if sec.sid not in kept and sec.parent in kept:
                        kept.add(sec.sid)
                        grew = True

            def _retag(items):
                copies = []
                for it in items:
                    if it.section == sid:
                        copies.append(_dc_replace(it, section=""))
                    elif it.section in kept:
                        copies.append(it)
                return copies

            root_sec = by_sid[sid]
            # every event inside this lane (incl. nested L2s) carries the
            # section's label token in its full stacked label
            token = f"[{_label_token(sid)}]"
            sub = _RunState(
                agent=agent or root_sec.label or sid,
                prompt=prompt,
                nest_root=self._nest_path(s, sid),
                out_path=out,
                started_at=s.started_at,
                tool_entries=_retag(s.tool_entries),
                subagent_events=_retag(s.subagent_events),
                pipeline_events=_retag(s.pipeline_events),
                compaction_events=_retag(s.compaction_events),
                stage_compactions=_retag(s.stage_compactions),
                sections=[_dc_replace(sec, parent="" if sec.parent == sid
                                      else sec.parent)
                          for sec in s.sections
                          if sec.sid in kept and sec.sid != sid],
                session_id=s.session_id,
                events=[ev for ev in s.events if token in ev.label],
                working_memory=working_memory,
                final_status=final_status,
            )
            ctx_token = self._state_ref.set(sub)
            try:
                self.flush(out)
            finally:
                self._state_ref.reset(ctx_token)

    def _nest_parts(self, s: _RunState, section_sid: str) -> List[str]:
        """Breadcrumb parts for a lane: root plus the section chain."""
        parts = [s.nest_root or _short_agent_root(s.agent)]
        if section_sid:
            by_sid = {sec.sid: sec for sec in s.sections}
            chain: List[str] = []
            cur, hops = section_sid, 0
            while cur and hops < 20:
                chain.append(cur)
                sec = by_sid.get(cur)
                cur = sec.parent if sec is not None else ""
                hops += 1
            parts.extend(reversed(chain))
        return parts

    def _nest_path(self, s: _RunState, section_sid: str) -> str:
        """Standard breadcrumb for a lane: root plus the section chain
        (e.g. "main - A_1 - L1_2 - L2_1"; own lane → just the root)."""
        return " - ".join(self._nest_parts(s, section_sid))

    def _render_step_blocks(
        self,
        lines: List[str],
        s: _RunState,
        entries: List[_ToolEntry],
        _consumed_sa: set,
        entries_by_section: Dict[str, List["_ToolEntry"]],
        claimed_by_entry: Dict[int, List["_NestedSection"]],
    ) -> None:
        """Render one section's tool entries (steps, verdicts, pointers,
        compaction events scoped to the section)."""
        for _ei, entry in enumerate(entries):
            _is_last_in_iter = (
                _ei == len(entries) - 1
                or entries[_ei + 1].iteration != entry.iteration
            )
            # Step header with status badge
            badge = ""
            if entry.is_validation_block:
                if entry.validation_status == "blocked":
                    badge = " 🔒 VALIDATION BLOCKED"
                else:
                    badge = " ⏸️ HELD BACK BY BATCH"
            elif entry.is_error:
                badge = " ❌ ERROR"
            elif entry.is_purpose_error:
                badge = " ⚠️ MISSING purpose/tasks"
            elif entry.is_oversized_guard:
                badge = " 📏 OVERSIZED"

            tag = ""
            if entry.seq:
                tag = f" [{self._nest_path(s, entry.section)} · c{entry.seq}]"
            lines.append(f"### Step {entry.iteration}{tag}: "
                         f"`{entry.tool_name}`{badge}")
            lines.append(f"")

            # Args (full, verbatim — collapsed in the details block)
            if entry.args:
                args_json = json.dumps(entry.args, indent=2, default=str,
                                       ensure_ascii=False)
                lines.append(f"<details><summary>Arguments</summary>")
                lines.append(f"")
                lines.append(f"```json")
                lines.append(args_json)
                lines.append(f"```")
                lines.append(f"</details>")
                lines.append(f"")

            started = ""
            if entry.started_ts:
                off = (f" (t+{entry.started_offset_s:.1f}s)"
                       if entry.started_offset_s >= 0 else "")
                started = f"  |  **Started:** {entry.started_ts}{off}"
            lines.append(f"- **Result:** {entry.result_chars:,} chars  |  "
                          f"**Time:** {entry.elapsed_s:.1f}s{started}")

            # Validation detail (before generic error, so it doesn't collide)
            if entry.is_validation_block:
                lines.append(f"- **Status:** {entry.validation_status}")
                if entry.result_preview:
                    lines.append(f"")
                    lines.append(f"<details><summary>Validation detail</summary>")
                    lines.append(f"")
                    lines.append(f"```")
                    for vl in entry.result_preview.splitlines():
                        lines.append(vl)
                    lines.append(f"```")
                    lines.append(f"</details>")

            # Error detail
            if entry.is_error:
                lines.append(f"- **Error:** `{entry.error_text}`")

            # Purpose/tasks missing
            if entry.is_purpose_error:
                lines.append(f"- **Guard:** purpose/tasks not provided by LLM")
                lines.append(f"  ```")
                lines.append(f"  {entry.purpose_error_text}")
                lines.append(f"  ```")

            # Oversized guard
            if entry.is_oversized_guard:
                lines.append(f"- **Oversized guard triggered:**")
                lines.append(f"  ```")
                for ol in entry.oversized_notice.splitlines()[:10]:
                    lines.append(f"  {ol}")
                lines.append(f"  ```")

            # Subagent events for this tool (same section only)
            # Skip for purpose/tasks errors (subagent was never called)
            if not entry.is_purpose_error:
                sa_ev = None
                for idx, e in enumerate(s.subagent_events):
                    if (idx not in _consumed_sa
                            and e.tool_name == entry.tool_name
                            and e.section == entry.section):
                        sa_ev = e
                        _consumed_sa.add(idx)
                        break
                if sa_ev:
                    _in = (f" in {sa_ev.input_chars:,}"
                           if sa_ev.input_chars else "")
                    lines.append(f"- **Subagent:** {sa_ev.event}{_in}"
                                  f" → {sa_ev.output_chars:,} chars"
                                  f" ({sa_ev.elapsed_s:.1f}s)")
                    if sa_ev.detail:
                        lines.append(f"  - {sa_ev.detail}")

            # Child pointers: nested sections this relay entry returned
            for sec in claimed_by_entry.get(entry.seq, []):
                n_calls = len(entries_by_section.get(sec.sid, []))
                if sec.child_history_path:
                    lines.append(f"- **Nested:** ↳ {sec.sid} — child session"
                                 f" history: {sec.child_history_path}")
                else:
                    lines.append(f"- **Nested:** ↳ {n_calls} tool calls in"
                                 f" section '{sec.sid}' below")

            # Full delivered result text (verbatim; falls back to the
            # 500-char preview for records logged without result_full)
            body_text = entry.result_full or entry.result_preview
            if body_text and not entry.is_error and not entry.is_purpose_error and not entry.is_validation_block:
                fence = "```"
                while fence in body_text:
                    fence += "`"
                summary = "Result" if entry.result_full else "Preview"
                lines.append(f"")
                lines.append(f"<details><summary>{summary}</summary>")
                lines.append(f"")
                lines.append(fence)
                lines.append(body_text)
                lines.append(fence)
                lines.append(f"</details>")

            lines.append(f"")

            # Compaction / stage-compaction events — render only once,
            # after the LAST tool of each iteration IN THIS SECTION
            # (avoids duplicates when a parallel batch shares the same
            # iteration number).
            if _is_last_in_iter:
                comp_events = [c for c in s.compaction_events
                               if c.iteration == entry.iteration
                               and c.section == entry.section]
                for ce in comp_events:
                    pct = (1 - ce.after_chars / ce.before_chars) * 100 if ce.before_chars else 0
                    lines.append(f"**📦 Context compaction** (after step {ce.iteration}, "
                                  f"trigger: {ce.trigger})")
                    if ce.outcome:
                        lines.append(f"- **Outcome:** {ce.outcome}")
                    if ce.purpose:
                        lines.append(f"- **Purpose:** {ce.purpose}")
                    if ce.tasks:
                        lines.append(f"- **Tasks:** {ce.tasks}")
                    lines.append(f"- {ce.before_chars:,} → {ce.after_chars:,} chars "
                                  f"(−{pct:.0f}%)")
                    if ce.receipt:
                        lines.append(f"- **Receipt:** {ce.receipt}")
                    lines.append(f"")

                stage_events = [sc for sc in s.stage_compactions
                                if sc.iteration == entry.iteration
                                and sc.section == entry.section]
                for se in stage_events:
                    pct = (1 - se.after_chars / se.before_chars) * 100 if se.before_chars else 0
                    lines.append(f"**🔀 Stage compaction** (batch of {se.n_tools} tools)")
                    lines.append(f"- {se.before_chars:,} → {se.after_chars:,} chars "
                                  f"(−{pct:.0f}%)")
                    lines.append(f"")

            lines.append(f"---")
            lines.append(f"")

    def _render_event_sections(self, lines: List[str], s: _RunState,
                               history_name: str = "run_history.md") -> None:
        """Append the session event log and verbatim agent outputs."""
        if not s.events:
            return
        lines.append(f"## Session Event Log ({len(s.events)} events)")
        lines.append("")
        lines.append(
            "Real-time chronological spine — every Argo (LLM) call, hook "
            "dispatch, tool/subagent dispatch, and shipped answer. Label "
            "grammar: `[session]_[root…]_[section…]_[activity…]_[kind]`. "
            f"`cN` in tool rows = the canonical `[… · cN]` step tag in "
            f"{history_name}.")
        lines.append("")
        lines.append("| # | Time | t+s | Kind | Status | Chars sys·prompt→out | Call s | Label | Detail |")
        lines.append("|---|------|----:|------|--------|---------------------:|-------:|-------|--------|")
        for ev in s.events:
            if ev.kind == "argo":
                sizes = (f"{ev.system_chars:,}·{ev.prompt_chars:,}"
                         f"→{ev.response_chars:,}")
                detail = " · ".join(b for b in (
                    ev.model, ev.tier,
                    f"try {ev.attempts}" if ev.attempts else "",
                    ev.error) if b)
            elif ev.kind in ("tool", "answer"):
                sizes = f"→{ev.response_chars:,}" if ev.response_chars else ""
                detail = " · ".join(b for b in (ev.detail, ev.error) if b)
            else:
                sizes = ""
                detail = ev.detail
            off = f"{ev.offset_s:.1f}" if ev.offset_s >= 0 else "?"
            csec = f"{ev.elapsed_s:.1f}" if ev.elapsed_s >= 0 else ""
            detail = detail.replace("|", "\\|")
            lines.append(
                f"| E{ev.seq} | {ev.ts} | {off} | {ev.kind} | {ev.status} "
                f"| {sizes} | {csec} | `{ev.label}` | {detail or '—'} |")
        lines.append("")

        verbatim = [ev for ev in s.events if ev.text]
        if not verbatim:
            return
        lines.append(f"## Agent Outputs (verbatim) — {len(verbatim)} outputs")
        lines.append("")
        lines.append(
            "Every agent-generated text (LLM responses and shipped answers) "
            "verbatim, in event order — replay material for the session.")
        lines.append("")
        for ev in verbatim:
            lines.append(f"### E{ev.seq} — `{ev.label}`")
            lines.append("")
            fence = "```"
            while fence in ev.text:
                fence += "`"
            lines.append(f"<details><summary>{ev.kind} output "
                         f"({len(ev.text):,} chars)</summary>")
            lines.append("")
            lines.append(fence)
            lines.append(ev.text)
            lines.append(fence)
            lines.append("</details>")
            lines.append("")

    def _render_detailed_markdown(self, history_name: str) -> str:
        """Build the sibling detailed-log markdown (event spine +
        verbatim agent outputs), cross-linked to the tool history by
        the shared session id and the canonical ``cN`` step tags."""
        s = self._state()
        lines: List[str] = []
        ts = (s.started_at.strftime("%Y-%m-%d %H:%M:%S")
              if s.started_at else "?")
        elapsed_total = ((dt.datetime.now() - s.started_at).total_seconds()
                         if s.started_at else 0)
        lines.append(f"# Detailed Session Log — {s.agent}")
        lines.append("")
        lines.append(f"**Nest:** {s.nest_root or _short_agent_root(s.agent)}")
        if s.session_id:
            lines.append(f"**Session:** {s.session_id}")
        lines.append(f"**Tool history:** {history_name} — same session; its "
                     f"step tags `[… · cN]` are the canonical tool ids the "
                     f"event rows join via `cN`")
        lines.append(f"**Started:** {ts}  |  **Elapsed:** "
                     f"{elapsed_total:.1f}s  |  **Events:** {len(s.events)}")
        lines.append("")
        lines.append("---")
        lines.append("")
        self._render_event_sections(lines, s, history_name)
        argo_n = sum(1 for e in s.events if e.kind == "argo")
        status_str = (f"  |  **Status:** {s.final_status}"
                      if s.final_status else "")
        lines.append("---")
        lines.append("")
        lines.append(f"**Total:** {len(s.events)} events  |  "
                     f"Argo calls: {argo_n}{status_str}")
        lines.append("")
        return "\n".join(lines)

    def _render_markdown(self) -> str:
        """Build the complete history markdown."""
        s = self._state()
        lines: List[str] = []

        # Header
        ts = s.started_at.strftime("%Y-%m-%d %H:%M:%S") if s.started_at else "?"
        elapsed_total = (
            (dt.datetime.now() - s.started_at).total_seconds()
            if s.started_at else 0
        )
        lines.append(f"# Tool History — {s.agent}")
        lines.append(f"")
        lines.append(f"**Nest:** {s.nest_root or _short_agent_root(s.agent)}")
        if s.session_id:
            lines.append(f"**Session:** {s.session_id}")
        if s.events and s.out_path:
            lines.append(
                f"**Detailed log:** {s.out_path.stem}_detailed"
                f"{s.out_path.suffix or '.md'} — Argo events + verbatim "
                f"agent outputs (join: session id; step tag `cN` ↔ "
                f"event-row `cN`)")
        lines.append(f"**Prompt:** {s.prompt}")
        nested_note = (f"  |  **Nested sections:** {len(s.sections)}"
                       if s.sections else "")
        lines.append(f"**Started:** {ts}  |  **Elapsed:** {elapsed_total:.1f}s  |  "
                      f"**Tool calls:** {len(s.tool_entries)}{nested_note}")
        lines.append(f"")
        lines.append(f"---")
        lines.append(f"")

        if not s.tool_entries:
            lines.append("*No tool calls recorded yet.*")
            lines.append("")
            return "\n".join(lines)

        # Track which subagent events have been consumed per-tool
        _consumed_sa: set = set()  # indices into s.subagent_events

        # ── Layered step blocks: own lane first, nested sections after ──
        entries_by_section: Dict[str, List[_ToolEntry]] = {}
        for e in s.tool_entries:
            entries_by_section.setdefault(e.section, []).append(e)
        claimed_by_entry: Dict[int, List[_NestedSection]] = {}
        for sec in s.sections:
            if sec.claimed_by_seq:
                claimed_by_entry.setdefault(sec.claimed_by_seq, []).append(sec)

        self._render_step_blocks(
            lines, s, entries_by_section.get("", []), _consumed_sa,
            entries_by_section, claimed_by_entry)

        for sec in s.sections:
            sec_entries = entries_by_section.get(sec.sid, [])
            descr = (f" ({sec.label})"
                     if sec.label and sec.label != sec.sid else "")
            lines.append(f"## Nested tool calls — {sec.sid}{descr}")
            lines.append(f"")
            lines.append(f"**Nest:** {self._nest_path(s, sec.sid)}")
            parent_e = next((e for e in s.tool_entries
                             if e.seq == sec.claimed_by_seq), None)
            if parent_e is not None:
                lines.append(f"**Parent:** `{sec.launcher_tool}` — Step "
                             f"{parent_e.iteration} "
                             f"[{self._nest_path(s, parent_e.section)} "
                             f"· c{parent_e.seq}] "
                             f"relays this worker's result")
            else:
                lines.append(f"**Parent:** `{sec.launcher_tool}` "
                             f"(relay row not recorded)")
            span = f"**Started:** {sec.started_ts or '?'}"
            if sec.ended_ts:
                span += f"  |  **Ended:** {sec.ended_ts}"
            lines.append(f"{span}  |  **Tool calls:** {len(sec_entries)}")
            if sec.child_history_path:
                lines.append(f"**Child session history:** "
                             f"{sec.child_history_path}")
            lines.append(f"")
            if sec_entries:
                lines.append(f"---")
                lines.append(f"")
                self._render_step_blocks(
                    lines, s, sec_entries, _consumed_sa,
                    entries_by_section, claimed_by_entry)
            elif not sec.child_history_path:
                lines.append("*No tool calls recorded in this section.*")
                lines.append("")

        # ── Summary tables ──

        # Compaction summary
        if s.compaction_events:
            lines.append(f"## Compaction Summary ({len(s.compaction_events)} events)")
            lines.append(f"")
            lines.append(f"| Iter | Trigger | Before | After | Reduction | Outcome |")
            lines.append(f"|------|---------|--------|-------|-----------|---------|")
            for ce in s.compaction_events:
                pct = (1 - ce.after_chars / ce.before_chars) * 100 if ce.before_chars else 0
                lines.append(
                    f"| {ce.iteration} "
                    f"| {ce.trigger} "
                    f"| {ce.before_chars:,} "
                    f"| {ce.after_chars:,} "
                    f"| −{pct:.0f}% "
                    f"| {ce.outcome or '—'} |"
                )
            lines.append(f"")

        # Stage compaction summary
        if s.stage_compactions:
            lines.append(f"## Stage Compaction Summary ({len(s.stage_compactions)} events)")
            lines.append(f"")
            lines.append(f"| Iter | Tools | Before | After | Reduction |")
            lines.append(f"|------|-------|--------|-------|-----------|")
            for se in s.stage_compactions:
                pct = (1 - se.after_chars / se.before_chars) * 100 if se.before_chars else 0
                lines.append(
                    f"| {se.iteration} "
                    f"| {se.n_tools} "
                    f"| {se.before_chars:,} "
                    f"| {se.after_chars:,} "
                    f"| −{pct:.0f}% |"
                )
            lines.append(f"")

        # Compaction pipeline summary (per-call native → hardcoded → agentic)
        if s.pipeline_events:
            lines.append(f"## Tool Compaction Pipeline ({len(s.pipeline_events)} calls)")
            lines.append(f"")
            lines.append(f"| # | Tool | Pipeline | Native | Hardcoded | Agentic | Verdict | Native→Final | Section |")
            lines.append(f"|--:|------|----------|-------:|----------:|--------:|---------|-------------:|---------|")
            for pi, pe in enumerate(s.pipeline_events, 1):
                pct = (1 - pe.final_chars / pe.native_chars) * 100 if pe.native_chars else 0
                lines.append(
                    f"| {pi} "
                    f"| `{pe.tool_name}` "
                    f"| {pe.pipeline} "
                    f"| {pe.native_chars:,} "
                    f"| {pe.compact_chars:,} "
                    f"| {pe.final_chars:,} "
                    f"| {pe.verdict} "
                    f"| −{pct:.0f}% "
                    f"| {pe.section or '—'} |"
                )
            lines.append(f"")

        # Subagent summary
        if s.subagent_events:
            lines.append(f"## Subagent Summary ({len(s.subagent_events)} events)")
            lines.append(f"")
            lines.append(f"| Tool | Verdict | Input Chars | Output Chars | Time | Section |")
            lines.append(f"|------|---------|-------------|-------------|------|---------|")
            for se in s.subagent_events:
                _in_cell = f"{se.input_chars:,}" if se.input_chars else "—"
                lines.append(
                    f"| {se.tool_name} "
                    f"| {se.event} "
                    f"| {_in_cell} "
                    f"| {se.output_chars:,} "
                    f"| {se.elapsed_s:.1f}s "
                    f"| {se.section or '—'} |"
                )
            lines.append(f"")

        # Error summary
        errors = [e for e in s.tool_entries if e.is_error or e.is_purpose_error]
        if errors:
            lines.append(f"## Errors ({len(errors)})")
            lines.append(f"")
            for e in errors:
                kind = "purpose/tasks missing" if e.is_purpose_error else "exception"
                sec_tag = f" · {e.section}" if e.section else ""
                lines.append(f"- **Step {e.iteration}{sec_tag}** `{e.tool_name}` ({kind}): "
                              f"{e.error_text[:200] or e.purpose_error_text[:200]}")
            lines.append(f"")

        # Internal errors summary
        if s.internal_errors:
            lines.append(f"## Internal Errors ({len(s.internal_errors)})")
            lines.append(f"")
            lines.append(f"| Time | Source | Type | Tool | Message |")
            lines.append(f"|------|--------|------|------|---------|")
            for ie in s.internal_errors:
                msg_short = ie.message.replace("|", "\\|")[:120]
                lines.append(
                    f"| {ie.timestamp} "
                    f"| {ie.source} "
                    f"| {ie.error_type} "
                    f"| `{ie.tool_name}` "
                    f"| {msg_short} |"
                )
            lines.append(f"")
            # Detailed context previews
            lines.append(f"<details><summary>Context previews ({len(s.internal_errors)} errors)</summary>")
            lines.append(f"")
            for i, ie in enumerate(s.internal_errors, 1):
                lines.append(f"**{i}. [{ie.timestamp}] {ie.source}/{ie.error_type}** — `{ie.tool_name}`")
                lines.append(f"")
                lines.append(f"Message: {ie.message}")
                if ie.context_preview:
                    lines.append(f"")
                    lines.append(f"```")
                    lines.append(ie.context_preview)
                    lines.append(f"```")
                lines.append(f"")
            lines.append(f"</details>")
            lines.append(f"")

        # ── Working memory snapshot ──
        if s.working_memory and s.working_memory.strip():
            lines.append(f"## Working Memory (final snapshot)")
            lines.append(f"")
            lines.append(s.working_memory.strip())
            lines.append(f"")

        # Footer
        total_tool_time = sum(e.elapsed_s for e in s.tool_entries)
        status_str = f"  |  **Status:** {s.final_status}" if s.final_status else ""
        lines.append(f"---")
        lines.append(f"")
        lines.append(f"**Total:** {len(s.tool_entries)} tool calls  |  "
                      f"Tool time: {total_tool_time:.1f}s  |  "
                      f"Wall: {elapsed_total:.1f}s{status_str}")
        lines.append(f"")

        return "\n".join(lines)



# ═══════════════════════════════════════════════════════════════
#  Singleton instance
# ═══════════════════════════════════════════════════════════════

history_recorder = HistoryRecorder()

_active_history_recorder: ContextVar[HistoryRecorder | None] = ContextVar(
    "thermoml_active_history_recorder", default=None
)


def set_active_history_recorder(rec: HistoryRecorder) -> None:
    """Bind the recorder that owns the current agent run."""
    if not isinstance(rec, HistoryRecorder):
        raise TypeError("rec must be a HistoryRecorder")
    _active_history_recorder.set(rec)


def get_active_history_recorder() -> HistoryRecorder:
    """Return the explicitly bound history recorder."""
    active = _active_history_recorder.get()
    if active is None:
        raise RuntimeError("no active HistoryRecorder; start agent tracking first")
    return active


def clear_active_history_recorder() -> None:
    """Remove the recorder binding after a run is finalized."""
    _active_history_recorder.set(None)
