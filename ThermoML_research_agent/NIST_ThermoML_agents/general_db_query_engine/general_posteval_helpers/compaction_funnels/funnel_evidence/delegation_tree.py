"""Delegation tree — WHO dispatched WHOM, from the exhaustive logs.

Type-agnostic parenthood: an instance's parent is whichever instance
actually dispatched it (resolved from the dispatcher ToolUse), never a
static layer assumption.  A ToolUse's caller is the DEEPEST instance on
the step's breadcrumb — an L2 evaluator's tools belong to the L2
instance, which is the direct child of its L1, never to L1 itself.

Instance kinds:
- session owners  — own artifact dir (root, run_query/analysis_agent
  children under query_runs/ / analysis_runs/).
- in-process      — a section of the owner's artifacts (L1_n / L2_n
  breadcrumb tokens; Q_L1 / A_L1_ALIGN / L2_* specs).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from framework_registry.agent_registry import AGENTS, AgentSpec
from framework_registry.tool_registry import (MENU_WRAPPER, SUBSTEP_KEYS,
                                              ToolSpec, tool_spec)
from funnel_evidence.history_evidence import (LegacySessionError,
                                              PipelineRow, SessionHistory,
                                              Step, SubagentRow,
                                              session_history)

_CHILD_DIRS = {
    "run_query_agent": ("query_runs", "Q_L0"),
    "run_analysis_agent": ("analysis_runs", "A_L0"),
}
_TOKEN_DISPLAY_RE = re.compile(r"^([A-Za-z]+\d*)_(\d+)$")


def _display(token: str) -> str:
    m = _TOKEN_DISPLAY_RE.match(token)
    if not m:
        return token
    head, num = m.groups()
    if head in ("A", "Q"):
        return f"{head}{num}"
    return f"{head}#{num}"


def _section_spec_key(sid: str, label: str) -> str:
    low = label.lower()
    if low.startswith("l2"):
        for kind in ("comp", "meas", "ref", "prop"):
            if kind in low:
                return f"L2_{kind.upper()}"
        return "L2_COMP"
    if "align" in low:
        return "A_L1_ALIGN"
    if sid.startswith("L2"):
        return "L2_COMP"
    return "Q_L1"


@dataclass
class ToolUse:
    spec: ToolSpec
    caller: "AgentInstance"
    step: Step
    kwargs: dict
    occ: int
    menu_expanded: bool = False
    wrapper_args: dict | None = None       # original run_subagent_tool args
    pipeline_row: PipelineRow | None = None
    subagent_row: SubagentRow | None = None
    substep_rows: tuple[PipelineRow, ...] = ()
    children: tuple["AgentInstance", ...] = ()

    @property
    def provenance(self) -> str:
        crumb = " - ".join(self.step.breadcrumb)
        return (f"run_history.md::Step {self.step.index} "
                f"[{crumb} \u00b7 c{self.step.seq}]")


@dataclass
class AgentInstance:
    spec: AgentSpec
    token: str                       # nest token ("main", "A_1", "L1_2")
    parent: "AgentInstance | None"
    session: Path                    # artifact dir (owner's for in-process)
    section: str = ""                # section sid inside session ("" = owner)
    dispatch: "ToolUse | None" = None
    context_dir: Path | None = None  # query_worker_runs ctx-only dir
    children: list = field(default_factory=list)
    tool_uses: list = field(default_factory=list)
    problems: list = field(default_factory=list)

    @property
    def sid(self) -> str:
        parts = []
        node = self
        while node is not None:
            parts.append(_display(node.token) if node.parent else
                         node.spec.label)
            node = node.parent
        return "/".join(reversed(parts))

    @property
    def owns_session(self) -> bool:
        return not self.section

    @property
    def dispatch_args(self) -> dict:
        return dict(self.dispatch.kwargs) if self.dispatch else {}

    def walk(self):
        yield self
        for child in self.children:
            yield from child.walk()


@dataclass
class DelegationTree:
    root: AgentInstance
    problems: list

    def instances(self) -> list[AgentInstance]:
        return list(self.root.walk())


_ROOT_SPEC = {"main": "MAIN", "query": "Q_L0", "analysis": "A_L0"}


def build_tree(session: Path, kind: str) -> DelegationTree:
    spec_key = _ROOT_SPEC.get(kind)
    if spec_key is None:
        raise ValueError(f"unknown session kind '{kind}'")
    root = AgentInstance(spec=AGENTS[spec_key], token=kind if kind != "main"
                         else "main", parent=None, session=Path(session))
    problems: list[str] = []
    _build_session(root, problems)
    return DelegationTree(root=root, problems=problems)


def _child_dir_queues(session: Path) -> dict[str, list[Path]]:
    queues: dict[str, list[Path]] = {}
    for tool, (dirname, _spec) in _CHILD_DIRS.items():
        base = session / dirname
        queues[tool] = (
            [d for d in sorted(base.iterdir())
             if (d / "run_history.md").exists()]
            if base.exists() else [])
    return queues


def _worker_ctx_queue(session: Path) -> list[Path]:
    base = session / "query_worker_runs"
    return ([d for d in sorted(base.iterdir()) if d.is_dir()]
            if base.exists() else [])


def _build_session(owner: AgentInstance, problems: list[str]) -> None:
    hist = session_history(owner.session)
    prefix = hist.nest
    section_labels = dict(hist.sections)
    dir_queues = _child_dir_queues(owner.session)
    ctx_queue = _worker_ctx_queue(owner.session)
    # in-process sections claimable by dispatcher rows, file order
    section_queue: list[str] = [sid for sid, label in hist.sections
                                if not label.endswith("-agent")]
    occ_counter: dict[tuple[int, str], int] = {}

    def instance_for(tokens: tuple[str, ...]) -> AgentInstance:
        node = owner
        for tok in tokens:
            found = next((c for c in node.children if c.token == tok), None)
            if found is None:
                key = _section_spec_key(tok, section_labels.get(tok, ""))
                found = AgentInstance(
                    spec=AGENTS[key], token=tok, parent=node,
                    session=owner.session, section=tok)
                node.children.append(found)
            node = found
        return node

    def rel_tokens(crumb: tuple[str, ...]) -> tuple[str, ...]:
        i = 0
        while i < len(prefix) and i < len(crumb) and crumb[i] == prefix[i]:
            i += 1
        return crumb[i:]

    for step in hist.steps:
        caller = instance_for(rel_tokens(step.breadcrumb))
        spec = tool_spec(step.tool)
        kwargs = step.arguments
        menu = False
        wrapper_args = None
        if step.tool == MENU_WRAPPER and isinstance(
                step.arguments.get("tool_name"), str):
            wrapper_args = step.arguments
            spec = tool_spec(step.arguments["tool_name"])
            inner = step.arguments.get("kwargs")
            kwargs = inner if isinstance(inner, dict) else {}
            menu = True
        key = (id(caller), spec.name)
        occ_counter[key] = occ_counter.get(key, 0) + 1
        use = ToolUse(spec=spec, caller=caller, step=step, kwargs=kwargs,
                      occ=occ_counter[key], menu_expanded=menu,
                      wrapper_args=wrapper_args)
        caller.tool_uses.append(use)

        if spec.is_dispatcher and step.status == "ok":
            claimed: list[AgentInstance] = []
            n_children = 1
            if spec.batch:
                for k in ("queries", "tasks"):
                    v = step.arguments.get(k)
                    if isinstance(v, list) and v:
                        n_children = len(v)
                        break
            if spec.name in _CHILD_DIRS or spec.name in (
                    "run_parallel_subagents", "run_query_agents_parallel"):
                # full-session children live in their own dirs
                candidate_tools = (("run_query_agent",)
                                   if spec.name == "run_query_agents_parallel"
                                   else tuple(_CHILD_DIRS)
                                   if spec.name == "run_parallel_subagents"
                                   else (spec.name,))
                for _ in range(n_children):
                    child_dir = None
                    child_key = ""
                    for tool_key in candidate_tools:
                        queue = dir_queues.get(tool_key) or []
                        if queue:
                            child_dir = queue.pop(0)
                            child_key = _CHILD_DIRS[tool_key][1]
                            break
                    if child_dir is None:
                        problems.append(f"{owner.sid}: no child dir left for "
                                        f"{spec.name} step c{step.seq}")
                        continue
                    try:
                        child_hist = session_history(child_dir)
                        token = child_hist.nest[-1]
                    except LegacySessionError as exc:
                        problems.append(str(exc))
                        token = child_dir.name
                    child = AgentInstance(
                        spec=AGENTS[child_key], token=token, parent=caller,
                        session=child_dir, dispatch=use)
                    caller.children.append(child)
                    claimed.append(child)
                    _build_session(child, problems)
            else:
                # in-process sections of THIS session; relay rows carry
                # explicit "**Nested:** ... section 'L1_4'" pointers
                sids = list(step.nested_sections)
                if not sids:
                    sids = section_queue[:n_children]
                for sid in sids:
                    if sid in section_queue:
                        section_queue.remove(sid)
                    elif not step.nested_sections:
                        problems.append(
                            f"{owner.sid}: no unclaimed section for "
                            f"{spec.name} step c{step.seq}")
                        continue
                    child = instance_for(rel_tokens(step.breadcrumb) + (sid,))
                    child.dispatch = use
                    if ctx_queue and child.spec.key == "Q_L1":
                        child.context_dir = ctx_queue.pop(0)
                    claimed.append(child)
            use.children = tuple(claimed)

    _join_pipeline_rows(owner, hist, problems)
    _join_subagent_rows(owner, hist, problems)

    leftovers = [str(d) for q in dir_queues.values() for d in q]
    if leftovers:
        problems.append(f"{owner.sid}: unclaimed child dirs {leftovers}")


def _uses_by_section(owner: AgentInstance) -> dict[tuple[str, str], list[ToolUse]]:
    """Executed (status ok) uses per (section, tool) — pipeline/subagent
    tables only log calls that actually ran the tool pipeline."""
    grouped: dict[tuple[str, str], list[ToolUse]] = {}
    for inst in owner.walk():
        if inst.session != owner.session:
            continue
        for use in inst.tool_uses:
            if use.step.status != "ok":
                continue
            grouped.setdefault((inst.section, use.spec.name), []).append(use)
    return grouped


def _join_pipeline_rows(owner: AgentInstance, hist: SessionHistory,
                        problems: list[str]) -> None:
    grouped = _uses_by_section(owner)
    queues = {k: list(v) for k, v in grouped.items()}
    orphans: list[PipelineRow] = []
    for row in hist.pipeline:
        queue = queues.get((row.section, row.tool))
        if queue:
            queue.pop(0).pipeline_row = row
        elif row.tool in SUBSTEP_KEYS:
            orphans.append(row)
        else:
            orphans.append(row)
            problems.append(f"{owner.sid}: unmatched pipeline row "
                            f"#{row.index} {row.tool} [{row.section}]")
    # fold substep rows into the nearest preceding claimed use of the section
    for row in orphans:
        if row.tool not in SUBSTEP_KEYS:
            continue
        candidates = [u for (sec, _t), uses in grouped.items()
                      if sec == row.section for u in uses
                      if u.pipeline_row is not None
                      and u.pipeline_row.index < row.index]
        if candidates:
            host = max(candidates, key=lambda u: u.pipeline_row.index)
            host.substep_rows = host.substep_rows + (row,)


def _join_subagent_rows(owner: AgentInstance, hist: SessionHistory,
                        problems: list[str]) -> None:
    grouped = _uses_by_section(owner)
    queues = {k: [u for u in v] for k, v in grouped.items()}
    for row in hist.subagent:
        if row.tool in SUBSTEP_KEYS:
            continue
        queue = [u for u in queues.get((row.section, row.tool), [])
                 if u.subagent_row is None]
        if queue:
            queue[0].subagent_row = row
