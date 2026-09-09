"""
Side-logging helper — ``reference_stats.md``
=============================================
Context-propagating recorder that accumulates:

- **Tool results** (pre-compaction): tool name, args, raw result chars,
  subagent output chars, KEEP/DISCARD verdict, timing.
- **Argo API calls**: per-tier tallies (system chars, prompt chars,
  response chars, call count, total time).
- **Compaction events**: before/after context size.

Everything is flushed to ``reference_stats.md`` inside the session
output directory.  This module is 100% harmless — it never modifies
conversation context, working memory, or any tool results.

Run isolation
~~~~~~~~~~~~~
Each explicit agent run owns a ``ContextVar`` state which propagates
through delegated worker threads without leaking into parallel runs.

Usage::

    from NIST_ThermoML_agents.general_db_query_engine.general_hooks_management_helpers.general_context_hooks.stats_references_tracking_hooks import recorder

    # After an Argo API call:
    recorder.log_argo_call(tier="L0-main", system_chars=..., prompt_chars=...,
                           response_chars=..., elapsed_s=..., model="...")

    # After a tool result is captured (react_loop):
    recorder.log_tool_result(iteration=..., tool_name=..., args=...,
                             raw_result_chars=..., elapsed_s=...)

    # After the subagent processes a tool result:
    recorder.log_subagent_verdict(tool_name=..., verdict="KEEP",
                                  subagent_output_chars=..., subagent_elapsed_s=...)

    # After compaction:
    recorder.log_compaction(before_chars=..., after_chars=..., trigger="interval")

    # At the end of a run:
    recorder.flush("/path/to/session_dir/reference_stats.md")
    recorder.reset()
"""

from __future__ import annotations

import datetime as dt
import functools
import logging
import threading
from collections import OrderedDict
from contextvars import ContextVar
from dataclasses import dataclass, field
from pathlib import Path
from ..general_memory_management_tools_hooks_helpers.session_manager_output_storage import (
    _filesystem_path,
    ensure_directory,
)
from typing import Any, Dict, List, Optional

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_block_id,
    require_block_local_id,
    require_global_id,
)

log = logging.getLogger("stats-recorder")


# ═══════════════════════════════════════════════════════════════
#  Data containers
# ═══════════════════════════════════════════════════════════════

@dataclass
class _ToolEntry:
    """One tool invocation record."""
    iteration: int
    tool_name: str
    args_summary: str
    raw_result_chars: int
    elapsed_s: float
    # Filled later by log_subagent_verdict (analysis agent only)
    subagent_verdict: str = ""          # "KEEP" | "DISCARD" | "" (no subagent)
    subagent_output_chars: int = 0
    subagent_elapsed_s: float = 0.0
    subagent_input_chars: int = 0       # hardcoded-compacted chars fed to subagent


@dataclass
class _ArgoCallEntry:
    """One Argo API call record."""
    tier: str               # e.g. "L0-main", "L1-subagent", "compactor"
    model: str
    system_chars: int
    prompt_chars: int
    response_chars: int
    elapsed_s: float


@dataclass
class _CompactionEntry:
    """One compaction decision (executed or skipped)."""
    trigger: str            # "interval" | "size" | "stage" | "rolling"
    before_chars: int
    after_chars: int
    outcome: str = "compacted"   # "compacted" | "skipped_by_agent" | "skipped_by_selector"


@dataclass
class _PendingSubagentVerdict:
    """Agentic-compaction metadata staged before the outer ReAct hook runs."""
    tool_name: str
    verdict: str
    output_chars: int
    elapsed_s: float
    input_chars: int = 0


def _nonnegative_int(value: Any, *, field_name: str) -> int:
    """Validate a counter without numeric-string coercion."""
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise TypeError(f"{field_name} must be a non-negative integer")
    return value


def _nonnegative_float(value: Any, *, field_name: str) -> float:
    """Validate elapsed time without accepting booleans or numeric strings."""
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0:
        raise TypeError(f"{field_name} must be a non-negative number")
    return float(value)


def _nonempty_string(value: Any, *, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise TypeError(f"{field_name} must be a non-empty string")
    return value


_MAX_INTERNAL_ERRORS = 50


def _passive(method):
    """Recording is telemetry: any failure is noted in the stats report,
    never propagated into the engine frame that fired the hook."""
    @functools.wraps(method)
    def guarded(self: "StatsRecorder", *args: Any, **kwargs: Any) -> None:
        try:
            method(self, *args, **kwargs)
        except Exception as exc:  # noqa: BLE001 — observer must never kill the run
            self._note_internal_error(method.__name__, exc)
    return guarded


def _walk_objects(value: Any):
    """Yield every native object in a tool result without inferring schemas."""
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _walk_objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_objects(child)


_ENTITY_BY_GLOBAL_FIELD = {
    "comp_num_id": "compound",
    "prop_num_id": "property",
    "var_num_id": "variable",
    "constr_num_id": "constraint",
    "meas_num_id": "measurement",
    "phase_num_id": "phase",
    "lit_num_id": "reference",
    "solvent_num_id": "solvent",
    "blocktype_num_id": "block_type",
    "rxn_type_num_id": "reaction_type",
}


@dataclass
class _DoiBlockRef:
    """One DOI + block reference observed in a tool result."""
    doi: str
    block_number: str
    tool_name: str
    BLKsubsys_id: str | None = None
    n_datapoints: int = 0
    system_type: str = ""
    n_components: int = 0

    def __post_init__(self) -> None:
        if not isinstance(self.doi, str) or not self.doi:
            raise TypeError("doi must be a non-empty string")
        self.block_number = require_block_id(self.block_number)
        if self.BLKsubsys_id is not None:
            self.BLKsubsys_id = require_block_local_id(
                "subsys", self.BLKsubsys_id
            )
        self.n_datapoints = _nonnegative_int(
            self.n_datapoints, field_name="n_datapoints"
        )
        self.n_components = _nonnegative_int(
            self.n_components, field_name="n_components"
        )


@dataclass
class _EntityRef:
    """One resolved entity (compound, property, variable, constraint, phase)."""
    entity_type: str        # "compound", "property", "variable", "constraint", "phase"
    global_id: str
    name: str
    source_tool: str        # tool that produced this entity
    extra: Dict[str, Any] = field(default_factory=dict)   # e.g. score, formula


@dataclass
class _RawCounterEntry:
    """Raw item counts from one tool result, before any agent condensation."""
    tool_name: str
    n_compounds: int = 0
    n_properties: int = 0
    n_variables: int = 0
    n_constraints: int = 0
    n_dois: int = 0
    n_blocks: int = 0
    n_datapoints: int = 0


@dataclass
class _RunState:
    """Context-local mutable state for one agent run."""
    tools: List[_ToolEntry] = field(default_factory=list)
    argo_calls: List[_ArgoCallEntry] = field(default_factory=list)
    compactions: List[_CompactionEntry] = field(default_factory=list)
    doi_blocks: List[_DoiBlockRef] = field(default_factory=list)
    entities: List[_EntityRef] = field(default_factory=list)
    raw_counters: List[_RawCounterEntry] = field(default_factory=list)
    pending_subagent_verdicts: List[_PendingSubagentVerdict] = field(default_factory=list)
    internal_errors: List[str] = field(default_factory=list)
    run_started: Optional[dt.datetime] = None
    agent_label: str = ""
    out_path: Optional[Path] = None


# ═══════════════════════════════════════════════════════════════
#  Singleton recorder
# ═══════════════════════════════════════════════════════════════

class StatsRecorder:
    """Context-propagating accumulator for one agent run.

    The context variable carries the same run-state object through
    ``asyncio.to_thread()``. A recorder instance therefore captures its
    delegated calls instead of creating an unobserved worker-thread state.
    """

    def __init__(self) -> None:
        self._state_ref: ContextVar[_RunState | None] = ContextVar(
            f"thermoml_stats_state_{id(self)}", default=None
        )
        self._flush_lock = threading.RLock()

    def _state(self) -> _RunState:
        """Return the current thread's run state (create if absent)."""
        s = self._state_ref.get()
        if s is None:
            s = _RunState()
            self._state_ref.set(s)
        return s

    def _note_internal_error(self, origin: str, exc: Exception) -> None:
        """Register a non-fatal recording anomaly (reported in the stats file)."""
        log.warning("Stats recorder %s failed (non-fatal): %s", origin, exc)
        errors = self._state().internal_errors
        if len(errors) < _MAX_INTERNAL_ERRORS:
            errors.append(f"`{origin}`: {type(exc).__name__}: {exc}")
        elif len(errors) == _MAX_INTERNAL_ERRORS:
            errors.append("(further recorder errors suppressed)")

    # ── Public API ──────────────────────────────────────────

    def reset(self) -> None:
        """Clear all accumulated data for a fresh run."""
        self._state_ref.set(_RunState())

    def start_run(self, agent_label: str = "", out_path: str | Path | None = None) -> None:
        """Mark the beginning of a new agent run (also resets old data).

        Parameters
        ----------
        agent_label : str
            Human-readable label for this run (e.g. "query-agent").
        out_path : str or Path, optional
            If given, stats are auto-flushed to this file after every
            logging call so the file stays up-to-date in real time.
        """
        self._state_ref.set(_RunState(
            run_started=dt.datetime.now(),
            agent_label=agent_label,
            out_path=Path(out_path) if out_path else None,
        ))

    # ── Real-time auto-flush ────────────────────────────────

    def _auto_flush(self) -> None:
        """If *out_path* was set at start_run, re-write the stats file now."""
        with self._flush_lock:
            s = self._state()
            if s.out_path and (s.tools or s.argo_calls):
                md = self._render_markdown()
                ensure_directory(s.out_path.parent)
                _filesystem_path(s.out_path).write_text(md, encoding="utf-8")

    # ── Logging methods (called from hooks) ─────────────────

    @_passive
    def log_tool_result(
        self,
        iteration: int,
        tool_name: str,
        args: Dict[str, Any],
        raw_result_chars: int,
        elapsed_s: float,
    ) -> None:
        """Record a tool invocation (raw result, before subagent)."""
        iteration = _nonnegative_int(iteration, field_name="iteration")
        tool_name = _nonempty_string(tool_name, field_name="tool_name")
        if not isinstance(args, dict):
            raise TypeError("args must be an object")
        raw_result_chars = _nonnegative_int(
            raw_result_chars, field_name="raw_result_chars"
        )
        elapsed_s = _nonnegative_float(elapsed_s, field_name="elapsed_s")
        summary = ", ".join(
            f"{k}={_truncate_val(v)}" for k, v in sorted(args.items())[:4]
        )
        state = self._state()
        entry = _ToolEntry(
            iteration=iteration,
            tool_name=tool_name,
            args_summary=summary,
            raw_result_chars=raw_result_chars,
            elapsed_s=elapsed_s,
        )
        for index, pending in enumerate(state.pending_subagent_verdicts):
            if pending.tool_name == tool_name:
                entry.subagent_verdict = pending.verdict
                entry.subagent_output_chars = pending.output_chars
                entry.subagent_elapsed_s = pending.elapsed_s
                entry.subagent_input_chars = pending.input_chars
                del state.pending_subagent_verdicts[index]
                break
        state.tools.append(entry)
        self._auto_flush()

    @_passive
    def log_subagent_verdict(
        self,
        tool_name: str,
        verdict: str,
        subagent_output_chars: int,
        subagent_elapsed_s: float,
        subagent_input_chars: int = 0,
    ) -> None:
        """Attach subagent verdict to the most recent matching tool entry."""
        tool_name = _nonempty_string(tool_name, field_name="tool_name")
        if verdict not in {"KEEP", "DISCARD"}:
            raise ValueError("verdict must be exactly KEEP or DISCARD")
        subagent_output_chars = _nonnegative_int(
            subagent_output_chars, field_name="subagent_output_chars"
        )
        subagent_elapsed_s = _nonnegative_float(
            subagent_elapsed_s, field_name="subagent_elapsed_s"
        )
        subagent_input_chars = _nonnegative_int(
            subagent_input_chars, field_name="subagent_input_chars"
        )
        state = self._state()
        # A direct compactor call may occur after its outer tool hook.
        for entry in reversed(state.tools):
            if entry.tool_name == tool_name and not entry.subagent_verdict:
                entry.subagent_verdict = verdict
                entry.subagent_output_chars = subagent_output_chars
                entry.subagent_elapsed_s = subagent_elapsed_s
                entry.subagent_input_chars = subagent_input_chars
                self._auto_flush()
                return
        # In the normal wrapped-tool lifecycle the subagent runs *inside* the
        # tool callable, before react_loop can record the completed invocation.
        # Stage the exact verdict and consume it when log_tool_result runs.
        state.pending_subagent_verdicts.append(
            _PendingSubagentVerdict(
                tool_name=tool_name,
                verdict=verdict,
                output_chars=subagent_output_chars,
                elapsed_s=subagent_elapsed_s,
                input_chars=subagent_input_chars,
            )
        )

    @_passive
    def log_argo_call(
        self,
        tier: str,
        model: str,
        system_chars: int,
        prompt_chars: int,
        response_chars: int,
        elapsed_s: float,
    ) -> None:
        """Record a single Argo API call."""
        tier = _nonempty_string(tier, field_name="tier")
        model = _nonempty_string(model, field_name="model")
        system_chars = _nonnegative_int(system_chars, field_name="system_chars")
        prompt_chars = _nonnegative_int(prompt_chars, field_name="prompt_chars")
        response_chars = _nonnegative_int(response_chars, field_name="response_chars")
        elapsed_s = _nonnegative_float(elapsed_s, field_name="elapsed_s")
        self._state().argo_calls.append(_ArgoCallEntry(
            tier=tier,
            model=model,
            system_chars=system_chars,
            prompt_chars=prompt_chars,
            response_chars=response_chars,
            elapsed_s=elapsed_s,
        ))
        self._auto_flush()

    @_passive
    def log_compaction(
        self,
        before_chars: int,
        after_chars: int,
        trigger: str = "",
        outcome: str = "compacted",
        **_: Any,
    ) -> None:
        """Record a compaction decision (executed or agent-skipped)."""
        before_chars = _nonnegative_int(before_chars, field_name="before_chars")
        after_chars = _nonnegative_int(after_chars, field_name="after_chars")
        if not isinstance(trigger, str):
            raise TypeError("trigger must be a string")
        if not isinstance(outcome, str) or not outcome:
            raise TypeError("outcome must be a non-empty string")
        if after_chars > before_chars:
            # Still an anomaly (skip notes like [RETRY:n] can grow context),
            # but the event row must survive so Section 5 keeps the evidence.
            self._note_internal_error("log_compaction", ValueError(
                f"after_chars ({after_chars:,}) exceeds before_chars "
                f"({before_chars:,}) — outcome '{outcome}'"
            ))
        self._state().compactions.append(_CompactionEntry(
            trigger=trigger,
            before_chars=before_chars,
            after_chars=after_chars,
            outcome=outcome,
        ))
        self._auto_flush()

    @_passive
    def log_raw_counters(
        self,
        tool_name: str,
        raw_result: dict,
    ) -> None:
        """Count exact scoped identifiers and typed block records.

        This is a schema-independent structural walk: it recognizes only the
        current canonical ID field names and typed block identifiers. It does
        not translate alternate field names or infer an entity from prose.
        """
        if not isinstance(tool_name, str) or not tool_name:
            raise TypeError("tool_name must be a non-empty string")
        if not isinstance(raw_result, dict):
            raise TypeError("raw_result must be an object")

        entity_ids = {entity: set() for entity in _ENTITY_BY_GLOBAL_FIELD.values()}
        dois: set[str] = set()
        blocks: dict[tuple[str, str, str | None], int] = {}
        summary_counts: tuple[int, int, int] | None = None

        for obj in _walk_objects(raw_result):
            if "error" in obj:
                continue  # error echoes are diagnostics, not delivered references
            for field_name, entity_type in _ENTITY_BY_GLOBAL_FIELD.items():
                if field_name not in obj or obj[field_name] is None:
                    continue
                values = obj[field_name] if isinstance(obj[field_name], list) else [obj[field_name]]
                for value in values:
                    entity_ids[entity_type].add(require_global_id(field_name, value))

            if "doi" in obj:
                doi = obj["doi"]
                if not isinstance(doi, str) or not doi:
                    raise TypeError("tool-result doi must be a non-empty string")
                dois.add(doi)

            if "doi" in obj and "block_number" in obj:
                block_number = require_block_id(obj["block_number"])
                n_points = 0
                if "n_datapoints" in obj:
                    n_points = _nonnegative_int(
                        obj["n_datapoints"], field_name="n_datapoints"
                    )
                elif "n_points" in obj:
                    n_points = _nonnegative_int(obj["n_points"], field_name="n_points")
                subsystem_id = obj.get("BLKsubsys_id")
                if subsystem_id is not None:
                    subsystem_id = require_block_local_id("subsys", subsystem_id)
                blocks[(obj["doi"], block_number, subsystem_id)] = n_points

            if {
                "n_targets", "n_blocks", "n_papers",
                "total_matching_datapoints",
            } <= obj.keys():
                counts = (
                    _nonnegative_int(obj["n_blocks"], field_name="n_blocks"),
                    _nonnegative_int(obj["n_papers"], field_name="n_papers"),
                    _nonnegative_int(
                        obj["total_matching_datapoints"],
                        field_name="total_matching_datapoints",
                    ),
                )
                if summary_counts is not None and summary_counts != counts:
                    # Keep the first summary; the conflict is reported, not fatal.
                    self._note_internal_error("log_raw_counters", ValueError(
                        f"conflicting summary counters in '{tool_name}' result: "
                        f"{summary_counts} vs {counts}"
                    ))
                else:
                    summary_counts = counts

        c = _RawCounterEntry(
            tool_name=tool_name,
            n_compounds=len(entity_ids["compound"]),
            n_properties=len(entity_ids["property"]),
            n_variables=len(entity_ids["variable"]),
            n_constraints=len(entity_ids["constraint"]),
            n_dois=len(dois),
            n_blocks=len(blocks),
            n_datapoints=sum(blocks.values()),
        )
        if not blocks and summary_counts is not None:
            c.n_blocks, summary_dois, c.n_datapoints = summary_counts
            c.n_dois = max(c.n_dois, summary_dois)
        self._state().raw_counters.append(c)
        self._auto_flush()

    @_passive
    def log_entity_references(
        self,
        tool_name: str,
        raw_result: dict,
    ) -> None:
        """Record exact global IDs found in a native tool-result object."""
        if not isinstance(tool_name, str) or not tool_name:
            raise TypeError("tool_name must be a non-empty string")
        if not isinstance(raw_result, dict):
            raise TypeError("raw_result must be an object")
        s = self._state()
        seen: set[tuple[str, str]] = set()
        for obj in _walk_objects(raw_result):
            if "error" in obj:
                continue  # error echoes are diagnostics, not delivered references
            for field_name, entity_type in _ENTITY_BY_GLOBAL_FIELD.items():
                if field_name not in obj or obj[field_name] is None:
                    continue
                values = obj[field_name] if isinstance(obj[field_name], list) else [obj[field_name]]
                for value in values:
                    global_id = require_global_id(field_name, value)
                    key = (entity_type, global_id)
                    if key in seen:
                        continue
                    seen.add(key)
                    name = (
                        obj["name"]
                        if "name" in obj and isinstance(obj["name"], str)
                        else ""
                    )
                    extra = {
                        extra_key: obj[extra_key]
                        for extra_key in ("score", "formula", "group")
                        if extra_key in obj
                    }
                    s.entities.append(_EntityRef(
                        entity_type=entity_type,
                        global_id=global_id,
                        name=name,
                        source_tool=tool_name,
                        extra=extra,
                    ))
        self._auto_flush()

    @_passive
    def log_doi_block_references(
        self,
        tool_name: str,
        raw_result: dict,
    ) -> None:
        """Record objects that contain both an exact DOI and typed block ID."""
        if not isinstance(tool_name, str) or not tool_name:
            raise TypeError("tool_name must be a non-empty string")
        if not isinstance(raw_result, dict):
            raise TypeError("raw_result must be an object")
        s = self._state()
        seen: set[tuple[str, str, str | None]] = set()
        for obj in _walk_objects(raw_result):
            if "error" in obj:
                continue  # error echoes are diagnostics, not delivered references
            if "doi" not in obj or "block_number" not in obj:
                continue
            doi = obj["doi"]
            if not isinstance(doi, str) or not doi:
                raise TypeError("tool-result doi must be a non-empty string")
            block_number = require_block_id(obj["block_number"])
            subsystem_id = obj.get("BLKsubsys_id")
            if subsystem_id is not None:
                subsystem_id = require_block_local_id("subsys", subsystem_id)
            key = (doi, block_number, subsystem_id)
            if key in seen:
                continue
            seen.add(key)
            n_datapoints = 0
            if "n_datapoints" in obj:
                n_datapoints = _nonnegative_int(
                    obj["n_datapoints"], field_name="n_datapoints"
                )
            elif "n_points" in obj:
                n_datapoints = _nonnegative_int(obj["n_points"], field_name="n_points")
            system_type = obj["system_type"] if "system_type" in obj else ""
            if not isinstance(system_type, str):
                raise TypeError("system_type must be a string")
            n_components = obj["n_components"] if "n_components" in obj else 0
            n_components = _nonnegative_int(n_components, field_name="n_components")
            s.doi_blocks.append(_DoiBlockRef(
                doi=doi,
                block_number=block_number,
                tool_name=tool_name,
                BLKsubsys_id=subsystem_id,
                n_datapoints=n_datapoints,
                system_type=system_type,
                n_components=n_components,
            ))
        self._auto_flush()

    # ── Flush to markdown ───────────────────────────────────

    def flush(self, output_path: str | Path) -> Optional[Path]:
        """Write all accumulated stats to ``reference_stats.md``.

        Returns the path written, or None if there is nothing to write.
        """
        with self._flush_lock:
            s = self._state()
            if not s.tools and not s.argo_calls:
                return None
            md = self._render_markdown()

            out = Path(output_path)
            try:
                ensure_directory(out.parent)
                _filesystem_path(out).write_text(md, encoding="utf-8")
            except OSError as exc:
                # Transient FS failures (network drive) must not kill teardown.
                log.error("Stats flush to %s failed (non-fatal): %s", out, exc)
                return None
            log.info("Stats flushed to %s (%d chars)", out, len(md))
            return out

    # ── Data complexity renderer (Section 2) ──────────────

    def _render_data_complexity(self, s: _RunState, lines: list[str]) -> None:
        """Append the Data Complexity Summary section to *lines*.

        Two sub-sections:
        - 2a: Raw Tool-Return Counters (direct counts from tool JSON results,
               before any agent condensation)
        - 2b: Agent-Condensed Data Complexity (deduplicated entity/DOI tables
               as curated by the agent pipeline)
        """
        lines.append("---")
        lines.append("")
        lines.append("## 2. Data Complexity Summary")
        lines.append("")

        # ── 2a: Raw Tool-Return Counters ────────────────────
        lines.append("### 2a. Raw Tool-Return Counters")
        lines.append("")
        lines.append("*Direct counts from raw tool results, before agent condensation.*")
        lines.append("")

        if not s.raw_counters:
            lines.append("*(no raw counter data recorded)*")
            lines.append("")
        else:
            # Per-tool breakdown
            lines.append("| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |")
            lines.append("|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|")
            tot_comp = tot_prop = tot_var = tot_con = tot_doi = tot_blk = tot_dp = 0
            for rc in s.raw_counters:
                lines.append(
                    f"| `{rc.tool_name}` | {rc.n_compounds} | {rc.n_properties} "
                    f"| {rc.n_variables} | {rc.n_constraints} "
                    f"| {rc.n_dois} | {rc.n_blocks} | {rc.n_datapoints:,} |"
                )
                tot_comp += rc.n_compounds
                tot_prop += rc.n_properties
                tot_var += rc.n_variables
                tot_con += rc.n_constraints
                tot_doi += rc.n_dois
                tot_blk += rc.n_blocks
                tot_dp += rc.n_datapoints
            lines.append(
                f"| **TOTAL** | **{tot_comp}** | **{tot_prop}** "
                f"| **{tot_var}** | **{tot_con}** "
                f"| **{tot_doi}** | **{tot_blk}** | **{tot_dp:,}** |"
            )
            lines.append("")

        # ── 2b: Agent-Condensed Data Complexity ─────────────
        lines.append("### 2b. Agent-Condensed Data Complexity")
        lines.append("")
        lines.append("*Deduplicated entities and DOI references after agent processing.*")
        lines.append("")

        if not s.entities:
            lines.append("*(no entity references recorded)*")
            lines.append("")
            return

        # Deduplicate by (entity_type, global_id) and collect all source tools.
        # all source tools that mentioned the entity.
        seen: Dict[tuple, dict] = OrderedDict()
        for e in s.entities:
            key = (e.entity_type, e.global_id)
            if key not in seen:
                seen[key] = {"name": e.name, "sources": set()}
            seen[key]["sources"].add(e.source_tool)

        # Group by entity_type, preserving insertion order
        groups: Dict[str, list] = OrderedDict()
        for (etype, nid), info in seen.items():
            groups.setdefault(etype, []).append((nid, info["name"], info["sources"]))

        # Render per-type tables
        type_labels = {
            "compound": "Compounds",
            "property": "Properties",
            "variable": "Variables",
            "constraint": "Constraints",
            "phase": "Phases",
        }
        for etype, entries in groups.items():
            label = type_labels.get(etype, etype.title() + "s")
            lines.append(f"#### {label} ({len(entries)} unique)")
            lines.append("")
            lines.append("| ID | Name | Source tools |")
            lines.append("|---:|------|-------------|")
            for nid, name, sources in entries:
                src_str = ", ".join(sorted(sources))
                lines.append(f"| {nid} | {name} | {src_str} |")
            lines.append("")

        # Aggregate totals
        total_dois = len({r.doi for r in s.doi_blocks}) if s.doi_blocks else 0
        total_blocks = len({(r.doi, str(r.block_number)) for r in s.doi_blocks}) if s.doi_blocks else 0
        total_targets = len({(r.doi, str(r.block_number), r.BLKsubsys_id) for r in s.doi_blocks}) if s.doi_blocks else 0
        total_subsystems = len({(r.doi, str(r.block_number), r.BLKsubsys_id) for r in s.doi_blocks if r.BLKsubsys_id is not None}) if s.doi_blocks else 0
        total_dp = sum(r.n_datapoints for r in s.doi_blocks) if s.doi_blocks else 0

        lines.append("#### Aggregate Counts (Condensed)")
        lines.append("")
        lines.append("| Metric | Count |")
        lines.append("|--------|------:|")
        for etype, entries in groups.items():
            label = type_labels.get(etype, etype.title() + "s")
            lines.append(f"| Unique {label} | {len(entries)} |")
        lines.append(f"| Total DOIs | {total_dois} |")
        lines.append(f"| Unique parent blocks | {total_blocks} |")
        lines.append(f"| Explicit block/subsystem targets | {total_targets} |")
        lines.append(f"| Subsystem targets | {total_subsystems} |")
        lines.append(f"| Target-matched data points | {total_dp:,} |")
        lines.append("")

    # ── Markdown renderer ───────────────────────────────────

    def _render_markdown(self) -> str:
        """Build the full reference_stats.md content."""
        s = self._state()
        ts = s.run_started.strftime("%Y-%m-%d %H:%M:%S") if s.run_started else "unknown"
        lines: list[str] = []

        lines.append(f"# Reference Stats — {s.agent_label}")
        lines.append(f"")
        lines.append(f"**Run started:** {ts}")
        if s.run_started is not None:
            wall = (dt.datetime.now() - s.run_started).total_seconds()
            lines.append(f"**Wall time (at last flush):** {wall:,.1f} s")
        lines.append(f"")

        # ── Section 0: Recorder Internal Errors ─────────────
        if s.internal_errors:
            lines.append("---")
            lines.append("")
            lines.append("## ⚠ Recorder Internal Errors (non-fatal)")
            lines.append("")
            lines.append("*Anomalies caught while recording; the run was not interrupted.*")
            lines.append("")
            for err in s.internal_errors:
                lines.append(f"- {err}")
            lines.append("")

        # ── Section 1: Argo API Summary ─────────────────────
        lines.append("---")
        lines.append("")
        lines.append("## 1. Argo API Call Summary")
        lines.append("")

        if s.argo_calls:
            # Aggregate by tier
            tier_stats: Dict[str, dict] = {}
            for c in s.argo_calls:
                ts_entry = tier_stats.setdefault(c.tier, {
                    "calls": 0, "system_chars": 0, "prompt_chars": 0,
                    "response_chars": 0, "total_s": 0.0, "models": set(),
                })
                ts_entry["calls"] += 1
                ts_entry["system_chars"] += c.system_chars
                ts_entry["prompt_chars"] += c.prompt_chars
                ts_entry["response_chars"] += c.response_chars
                ts_entry["total_s"] += c.elapsed_s
                ts_entry["models"].add(c.model)

            lines.append("| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |")
            lines.append("|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|")
            grand_calls = 0
            grand_sys = 0
            grand_prompt = 0
            grand_resp = 0
            grand_time = 0.0
            for tier in sorted(tier_stats):
                ts_entry = tier_stats[tier]
                total_sent = ts_entry["system_chars"] + ts_entry["prompt_chars"]
                avg_ctx = total_sent // ts_entry["calls"] if ts_entry["calls"] else 0
                models = ", ".join(sorted(ts_entry["models"]))
                lines.append(
                    f"| {tier} | {ts_entry['calls']} | {ts_entry['system_chars']:,} "
                    f"| {ts_entry['prompt_chars']:,} | {ts_entry['response_chars']:,} "
                    f"| {total_sent:,} | {avg_ctx:,} | {ts_entry['total_s']:.1f} | {models} |"
                )
                grand_calls += ts_entry["calls"]
                grand_sys += ts_entry["system_chars"]
                grand_prompt += ts_entry["prompt_chars"]
                grand_resp += ts_entry["response_chars"]
                grand_time += ts_entry["total_s"]
            grand_sent = grand_sys + grand_prompt
            grand_avg = grand_sent // grand_calls if grand_calls else 0
            lines.append(
                f"| **TOTAL** | **{grand_calls}** | **{grand_sys:,}** "
                f"| **{grand_prompt:,}** | **{grand_resp:,}** "
                f"| **{grand_sent:,}** | **{grand_avg:,}** | **{grand_time:.1f}** | |"
            )
            lines.append("")

            # Estimated tokens (rough: 1 token ≈ 4 chars)
            est_in = grand_sent // 4
            est_out = grand_resp // 4
            lines.append(f"**Estimated tokens:** ~{est_in:,} input + ~{est_out:,} output = ~{est_in + est_out:,} total")
            lines.append(f"*(rough estimate: 1 token ≈ 4 chars)*")
            lines.append("")
        else:
            lines.append("*(no Argo calls recorded)*")
            lines.append("")

        # ── Section 2: Data Complexity Summary ────────────
        self._render_data_complexity(s, lines)

        # ── Section 3: DOI & Block References ──────────────
        lines.append("---")
        lines.append("")
        lines.append("## 3. DOI & Block References")
        lines.append("")

        if s.doi_blocks:
            # Deduplicate explicit targets: (doi, block_number, BLKsubsys_id).
            seen: Dict[tuple, dict] = {}
            for ref in s.doi_blocks:
                key = (ref.doi, str(ref.block_number), ref.BLKsubsys_id)
                if key not in seen:
                    seen[key] = {
                        "doi": ref.doi,
                        "block_number": ref.block_number,
                        "BLKsubsys_id": ref.BLKsubsys_id,
                        "n_datapoints": ref.n_datapoints,
                        "system_type": ref.system_type,
                        "n_components": ref.n_components,
                        "tools": {ref.tool_name},
                    }
                else:
                    seen[key]["tools"].add(ref.tool_name)
                    # Keep the richest metadata
                    if ref.n_datapoints:
                        seen[key]["n_datapoints"] = ref.n_datapoints
                    if ref.system_type:
                        seen[key]["system_type"] = ref.system_type
                    if ref.n_components:
                        seen[key]["n_components"] = ref.n_components

            unique_dois = sorted({v["doi"] for v in seen.values()})
            total_blocks = len({
                (v["doi"], str(v["block_number"])) for v in seen.values()
                if v["block_number"] != "(summary)"
            })
            total_targets = sum(
                1 for v in seen.values() if v["block_number"] != "(summary)"
            )
            total_subsystems = sum(
                v["BLKsubsys_id"] is not None for v in seen.values()
            )
            total_dp = sum(v["n_datapoints"] or 0 for v in seen.values())

            lines.append(f"**Unique DOIs:** {len(unique_dois)}  |  "
                         f"**Parent blocks:** {total_blocks}  |  "
                         f"**Explicit targets:** {total_targets}  |  "
                         f"**Subsystems:** {total_subsystems}  |  "
                         f"**Target-matched datapoints:** {total_dp:,}")
            lines.append("")

            # Per-DOI summary
            lines.append("| DOI | Blocks | Datapoints | System types | Source tools |")
            lines.append("|-----|-------:|-----------:|--------------|--------------|")
            for doi in unique_dois:
                entries = [v for v in seen.values() if v["doi"] == doi]
                n_blk = sum(1 for e in entries if e["block_number"] != "(summary)")
                dp = sum(e["n_datapoints"] or 0 for e in entries)
                sys_types = sorted({e["system_type"] for e in entries if e["system_type"]})
                tools = sorted({t for e in entries for t in e["tools"]})
                lines.append(
                    f"| {doi} | {n_blk} | {dp:,} "
                    f"| {', '.join(sys_types) or '—'} "
                    f"| {', '.join(tools)} |"
                )
            lines.append("")

            # Detailed block listing
            lines.append("<details><summary>Block detail</summary>")
            lines.append("")
            lines.append("| DOI | Block | Target | Datapoints | System | nComp | Source tools |")
            lines.append("|-----|------:|--------|-----------:|--------|------:|--------------|")
            for key in sorted(
                seen,
                key=lambda item: (item[0], item[1], item[2] or ""),
            ):
                v = seen[key]
                tools_str = ", ".join(sorted(v["tools"]))
                lines.append(
                    f"| {v['doi']} | {v['block_number']} | "
                    f"{v['BLKsubsys_id'] or 'declared'} | {(v['n_datapoints'] or 0):,} "
                    f"| {v['system_type'] or '—'} | {v['n_components'] or '—'} "
                    f"| {tools_str} |"
                )
            lines.append("")
            lines.append("</details>")
            lines.append("")
        else:
            lines.append("*(no DOI/block references recorded)*")
            lines.append("")

        # ── Section 4: Tool Results (as entered into context) ────────
        lines.append("---")
        lines.append("")
        lines.append("## 4. Tool Results (post tool-pipeline, pre context-compaction)")
        lines.append("")

        if s.tools:
            lines.append("| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |")
            lines.append("|--:|-----:|------|------|------------:|----------|------------:|---------:|")
            total_raw = 0
            total_sub = 0
            total_time = 0.0
            for i, t in enumerate(s.tools, 1):
                verdict_tag = t.subagent_verdict or "—"
                if t.subagent_verdict and t.subagent_input_chars:
                    verdict_tag = f"{t.subagent_verdict} ←in {t.subagent_input_chars:,}"
                sub_chars = t.subagent_output_chars or "—"
                args_short = t.args_summary[:50] + ("…" if len(t.args_summary) > 50 else "")
                lines.append(
                    f"| {i} | {t.iteration} | `{t.tool_name}` | {args_short} "
                    f"| {t.raw_result_chars:,} | {verdict_tag} | {sub_chars} "
                    f"| {t.elapsed_s:.1f} |"
                )
                total_raw += t.raw_result_chars
                total_sub += t.subagent_output_chars
                total_time += t.elapsed_s
            lines.append(
                f"| | | **TOTAL ({len(s.tools)} tools)** | | "
                f"**{total_raw:,}** | | **{total_sub:,}** | **{total_time:.1f}** |"
            )
            lines.append("")
        else:
            lines.append("*(no tool results recorded)*")
            lines.append("")

        # ── Section 5: Compaction Events ────────────────────
        lines.append("---")
        lines.append("")
        lines.append("## 5. Compaction Events")
        lines.append("")

        if s.compactions:
            lines.append("| # | Trigger | Outcome | Before (chars) | After (chars) | Saved (chars) | Saved (%) |")
            lines.append("|--:|---------|---------|---------------:|--------------:|--------------:|----------:|")
            for i, c in enumerate(s.compactions, 1):
                saved = c.before_chars - c.after_chars
                pct = (saved / c.before_chars * 100) if c.before_chars > 0 else 0
                lines.append(
                    f"| {i} | {c.trigger} | {c.outcome} | {c.before_chars:,} "
                    f"| {c.after_chars:,} | {saved:,} | {pct:.1f}% |"
                )
            executed = [c for c in s.compactions if c.outcome == "compacted"]
            if executed:
                tot_before = sum(c.before_chars for c in executed)
                tot_saved = sum(c.before_chars - c.after_chars for c in executed)
                eff = (tot_saved / tot_before * 100) if tot_before > 0 else 0
                lines.append("")
                lines.append(
                    f"**Compaction efficiency:** {tot_saved:,} chars removed across "
                    f"{len(executed)} executed compaction(s) ({eff:.1f}% of pre-compaction context); "
                    f"{len(s.compactions) - len(executed)} skip decision(s)."
                )
            lines.append("")
        else:
            lines.append("*(no compaction events recorded)*")
            lines.append("")

        # ── Section 6: Argo Call Detail Log ─────────────────
        lines.append("---")
        lines.append("")
        lines.append("## 6. Argo Call Detail Log")
        lines.append("")

        if s.argo_calls:
            lines.append("| # | Tier | Model | System | Prompt | Context | Response | Time (s) |")
            lines.append("|--:|------|-------|-------:|-------:|--------:|---------:|---------:|")
            for i, c in enumerate(s.argo_calls, 1):
                ctx = c.system_chars + c.prompt_chars
                lines.append(
                    f"| {i} | {c.tier} | {c.model} | {c.system_chars:,} "
                    f"| {c.prompt_chars:,} | {ctx:,} | {c.response_chars:,} "
                    f"| {c.elapsed_s:.1f} |"
                )
            lines.append("")
        else:
            lines.append("*(no Argo calls recorded)*")
            lines.append("")

        return "\n".join(lines) + "\n"


# ═══════════════════════════════════════════════════════════════
#  Module-level singleton + thread-local active recorder
# ═══════════════════════════════════════════════════════════════

recorder = StatsRecorder()

# Explicit active-recorder binding. Context variables propagate through
# ``asyncio.to_thread()``, so delegated L1/L2 calls retain the run recorder.
_active_recorder: ContextVar[StatsRecorder | None] = ContextVar(
    "thermoml_active_stats_recorder", default=None
)


def set_active_recorder(rec: StatsRecorder) -> None:
    """Designate *rec* as the active stats recorder for this thread."""
    if not isinstance(rec, StatsRecorder):
        raise TypeError("rec must be a StatsRecorder")
    _active_recorder.set(rec)


def get_active_recorder() -> StatsRecorder:
    """Return the explicitly active stats recorder for this thread."""
    active = _active_recorder.get()
    if active is None:
        raise RuntimeError("no active StatsRecorder; start agent tracking first")
    return active


def clear_active_recorder() -> None:
    """Remove the thread-local active recorder reference."""
    _active_recorder.set(None)


# ═══════════════════════════════════════════════════════════════
#  Helpers
# ═══════════════════════════════════════════════════════════════

def _truncate_val(v: Any, max_len: int = 30) -> str:
    """Truncate a value to a short string for the args summary."""
    s = str(v)
    if len(s) <= max_len:
        return s
    return s[:max_len - 1] + "…"
