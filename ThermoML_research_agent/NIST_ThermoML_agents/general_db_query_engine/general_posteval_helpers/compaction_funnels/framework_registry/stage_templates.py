"""Stage templates — the Sankey block grammar.

Every node in every funnel figure is minted here, so keys, labels,
kinds (colors), and merge groups stay consistent across the detailed /
agentic / pooled levels:

- key            unique within a session graph; instance-path scoped
                 ("Main/A1/L1#2:search_blocks#3:raw")
- agentic_group  detailed→agentic merge key (instance-scoped)
- pooled_group   agentic→pooled merge key — LAYER-scoped: same-type
                 nodes of each delegation layer (main/Q/A/L1/L2)
                 merge; in-flows keep per-instance copies and
                 deduplication happens only at each layer's agent
                 context

Merging is mechanical: nodes sharing a group key merge (ids union,
chars sum); a node with group None never merges; parallel edges stay
separate so contribution copies remain visible.
"""

from __future__ import annotations

from dataclasses import dataclass

from .tool_registry import ToolSpec, chain_shape, FULL_PIPELINE, DET_ONLY, EXEMPT, RELAY
from .agent_registry import AGENTS, AgentSpec, FieldClass, LAYERS


class NodeRole:
    RAW = "raw"
    HARDCODED = "hardcoded"
    AGENTIC = "agentic"          # agentic kept (triage KEEP output)
    ASIS = "asis"                # delivered as-is (no triage)
    CONTEXT = "context"          # THE per-instance dedup/merge layer
    ANSWER = "answer"
    ENVELOPE_PART = "envelope_part"
    DELIVERABLE = "deliverable"  # envelope hand-off node
    RELAY_WRAPPER = "wrapper"
    SUPPORT = "support"
    WM_ARCHIVE = "wm_archive"
    INTRODUCED = "introduced"
    SINK = "sink"
    BATCH = "batch"              # parallel batch collector


class SupportClass:
    BRIEF = "BRIEF"
    SEED = "SEED"
    WM_RENDER = "WM_RENDER"
    TRANSIENT = "TRANSIENT"
    LEDGER = "LEDGER"
    SCAFFOLD = "SCAFFOLD"        # envelope scaffolding (chars-only)


class SinkFamily:
    HARDCODED_CUT = "hardcoded_cut"
    TRIAGE_CUT = "triage_cut"
    CONDENSED = "condensed_in_synthesis"
    DEDUP_EXIT = "dedup_exit"
    DUP_CANONICAL = "duplicate_canonical"
    NOT_CITED = "not_cited_downstream"
    MEMORY_UNCITED = "memory_uncited"
    LEDGER_UNCITED = "ledger_uncited"
    INSPECTION_DROPPED = "inspection_dropped"
    LEDGER_CONSUMED = "ledger_consumed"
    WM_RETAINED = "wm_retained"
    BATCH_CONDENSED = "batch_condensed"


_SINK_LABEL = {
    SinkFamily.HARDCODED_CUT: "hardcoded compaction cut",
    SinkFamily.TRIAGE_CUT: "agentic triage cut",
    SinkFamily.CONDENSED: "condensed away in synthesis",
    SinkFamily.DEDUP_EXIT: "re-confirmed known IDs (dedup)",
    SinkFamily.DUP_CANONICAL: "duplicate canonical copies (deduplicated)",
    SinkFamily.NOT_CITED: "not cited downstream",
    SinkFamily.MEMORY_UNCITED: "memory carry not cited (WM render / transient)",
    SinkFamily.LEDGER_UNCITED: "ledger content not cited",
    SinkFamily.INSPECTION_DROPPED: "inspection rows dropped (errored/refined)",
    SinkFamily.LEDGER_CONSUMED: "ledger consumed at summary level",
    SinkFamily.WM_RETAINED: "payload retained only in working memory",
    SinkFamily.BATCH_CONDENSED: "condensed in batch consolidation",
}

_SUPPORT_LABEL = {
    SupportClass.BRIEF: "dispatch brief",
    SupportClass.SEED: "seed context (user question)",
    SupportClass.WM_RENDER: "working-memory render",
    SupportClass.TRANSIENT: "transient context carry (in-loop text, not WM-recorded)",
    SupportClass.LEDGER: "inspection ledger (data_inspections)",
    SupportClass.SCAFFOLD: "envelope JSON scaffolding",
}

# node kind → NODE_COLORS key in sankey rendering (reuse existing palette)
_ROLE_KIND = {
    NodeRole.RAW: "raw",
    NodeRole.HARDCODED: "hardcoded",
    NodeRole.AGENTIC: "agentic",
    NodeRole.ASIS: "agentic",
    NodeRole.CONTEXT: "merge",
    NodeRole.ANSWER: "answer",
    NodeRole.ENVELOPE_PART: "envelope",
    NodeRole.DELIVERABLE: "envelope",
    NodeRole.RELAY_WRAPPER: "hardmeta",
    NodeRole.SUPPORT: "hardmeta",
    NodeRole.WM_ARCHIVE: "payload",
    NodeRole.INTRODUCED: "introduced",
    NodeRole.SINK: "removed",
    NodeRole.BATCH: "merge",
}

_FIELD_LABEL = {
    FieldClass.ANSWER: "answer (verbatim)",
    FieldClass.WRITTEN: "LLM-written fields",
    FieldClass.WM: "WM-assembled fields",
    FieldClass.HYDRATED: "DB-hydrated fields",
    FieldClass.LEDGER: "inspection ledger (data_inspections)",
    FieldClass.VERDICT: "verdict",
    FieldClass.SCAFFOLD: "JSON scaffolding",
}


@dataclass(frozen=True)
class BlockSpec:
    key: str
    label: str
    kind: str                    # sankey color kind
    role: str                    # NodeRole
    agentic_group: str | None    # detailed→agentic merge key
    pooled_group: str | None     # agentic→pooled merge key
    # declared flow endpoints — the conservation audits enforce that
    # ONLY source blocks emit without inflow (tool emissions +
    # supportive contexts) and ONLY sink blocks absorb without outflow
    source: bool = False
    sink: bool = False


# ── factories ─────────────────────────────────────────────────
# ``path`` = instance path token, e.g. "Main", "Main/A1", "Main/A1/L1#2"
# ``disp`` = short display prefix derived from path ("A1 · L1#2")


def _disp(path: str) -> str:
    parts = path.split("/")
    return " · ".join(parts[1:]) if len(parts) > 1 else parts[0]


def _p(path: str, label: str) -> str:
    d = _disp(path)
    return f"{d} · {label}" if d else label


_STAGE_LABEL = {
    NodeRole.RAW: "raw results",
    NodeRole.HARDCODED: "hardcoded compact",
    NodeRole.AGENTIC: "agentic kept",
    NodeRole.ASIS: "delivered as-is",
}


def tool_stage_block(path: str, tool: ToolSpec, occ: int, role: str,
                     menu: bool = False, family: str | None = None,
                     source: bool = False, layer: str = "",
                     branch: str = "") -> BlockSpec:
    """One stage node of one ToolUse chain.  ``source=True`` marks a
    stage that IS the tool emission itself (raw, or delivered-as-is
    for exempt/error calls) — source stages never merge with fed
    stages of the same family.  ``layer`` = the CALLER's delegation
    layer; ``branch`` = the top-level dispatch lane — evidence tool
    rails pool only INSIDE one dispatch (Main's own / each Qi / each
    Ai), while inspection / hydration / utility / error content pools
    across dispatches."""
    fam = family or tool_family(tool)
    menu_tag = " (menu)" if menu else ""
    is_source = source or role == NodeRole.RAW
    grp_role = f"{role}:src" if source else role
    # utility/error returns are supportive context; hardcoded_data
    # rails (deterministic DB reads) join the deterministic-evidence
    # pool together with the inspection tools
    pooled = ("inspection" if fam in ("inspection", "hardcoded_data")
              else "support|content" if fam in ("utility", "error")
              else f"{branch}|{layer}|{fam}|{grp_role}")
    return BlockSpec(
        key=f"{path}:{tool.name}#{occ}:{role}",
        label=_p(path, f"{tool.name}{menu_tag} · {_STAGE_LABEL[role]}"),
        kind="validation" if tool.inspection else _ROLE_KIND[role],
        role=role,
        agentic_group=f"{path}|{fam}|{grp_role}",
        pooled_group=pooled,
        source=is_source,
    )


def tool_family(tool: ToolSpec) -> str:
    if tool.inspection:
        return "inspection"
    if tool.fit_rail:
        return "fitting"
    if tool.is_dispatcher:
        return "dispatch"
    return {
        FULL_PIPELINE: "search",
        DET_ONLY: "hardcoded_data",
        EXEMPT: "utility",
        RELAY: "dispatch",
    }[chain_shape(tool)]


def context_block(path: str, layer: str = "") -> BlockSpec:
    return BlockSpec(
        key=f"{path}:context",
        label=_p(path, "agent context (dedup merge)"),
        kind="merge", role=NodeRole.CONTEXT,
        agentic_group=None, pooled_group=f"{layer}|context",
    )


def answer_block(path: str, terminal: bool, layer: str = "") -> BlockSpec:
    return BlockSpec(
        key=f"{path}:answer",
        label=_p(path, "final answer" if terminal else "answer"),
        kind="answer", role=NodeRole.ANSWER,
        agentic_group=None, pooled_group=f"{layer}|answer",
        sink=terminal,
    )


def envelope_part_block(path: str, field_class: str,
                        layer: str = "") -> BlockSpec:
    return BlockSpec(
        key=f"{path}:env:{field_class}",
        label=_p(path, f"envelope · {_FIELD_LABEL[field_class]}"),
        kind="envelope", role=NodeRole.ENVELOPE_PART,
        agentic_group=f"{path}|env|{field_class}",
        pooled_group=f"{layer}|env",
    )


def deliverable_block(path: str, parent_label: str,
                      sink: bool = False, layer: str = "") -> BlockSpec:
    """``sink=True`` for a parentless root's envelope — the session's
    terminal hand-off (nobody consumes it inside the graph)."""
    return BlockSpec(
        key=f"{path}:deliverable",
        label=_p(path, f"result envelope to {parent_label} (deliverable)"),
        kind="envelope", role=NodeRole.DELIVERABLE,
        agentic_group=None, pooled_group=f"{layer}|deliverable",
        sink=sink,
    )


def wrapper_block(path: str, occ: str = "", layer: str = "") -> BlockSpec:
    """Hardcoded relay framing, keyed per dispatching ToolUse — the
    wrapper belongs to the CALLER's lane (child-sid keys collide with
    the child's own wrappers and straddle subgraph slices)."""
    return BlockSpec(
        key=f"{path}:wrapper" + (f":{occ}" if occ else ""),
        label=_p(path, "hardcoded relay wrapper"),
        kind="hardmeta", role=NodeRole.RELAY_WRAPPER,
        agentic_group=f"{path}|wrapper",
        pooled_group="support|content",
        source=True,
    )


def support_block(path: str, support_class: str,
                  layer: str = "") -> BlockSpec:
    # pooled consolidation: ledger joins the global inspection block;
    # WM render + transient carries form one memory block; briefs,
    # seeds and scaffolding form one supporting-content block
    pooled = ("inspection" if support_class == SupportClass.LEDGER
              else "support|memory" if support_class in
              (SupportClass.WM_RENDER, SupportClass.TRANSIENT)
              else "support|content")
    kind = ("validation" if support_class == SupportClass.LEDGER else
            "delegated" if support_class == SupportClass.BRIEF else
            "payload" if support_class == SupportClass.TRANSIENT else
            "hardmeta")
    return BlockSpec(
        key=f"{path}:support:{support_class}",
        label=_p(path, _SUPPORT_LABEL[support_class]),
        kind=kind,
        role=NodeRole.SUPPORT,
        agentic_group=f"{path}|support|{support_class}",
        pooled_group=pooled,
        source=True,
    )


def wm_archive_block(path: str, layer: str = "") -> BlockSpec:
    return BlockSpec(
        key=f"{path}:wm",
        label=_p(path, "working-memory archive"),
        kind="payload", role=NodeRole.WM_ARCHIVE,
        agentic_group=None, pooled_group=f"{layer}|wm",
    )


def introduced_block(path: str, layer: str = "") -> BlockSpec:
    return BlockSpec(
        key=f"{path}:introduced",
        label=_p(path, "newly written by the agent (LLM additions)"),
        kind="introduced", role=NodeRole.INTRODUCED,
        agentic_group=f"{path}|introduced",
        # pure source like the rest of the content pool; the red
        # "introduced" flow edge keeps the LLM-addition signal visible
        pooled_group="support|content",
        source=True,
    )


def hydration_block(path: str, layer: str = "") -> BlockSpec:
    """Deterministic DB-hydration source (workflow-written, not LLM)."""
    return BlockSpec(
        key=f"{path}:hydration",
        label=_p(path, "DB hydration (workflow enrichment)"),
        kind="payload", role=NodeRole.SUPPORT,
        agentic_group=f"{path}|support|HYDRATION",
        pooled_group="inspection",
        source=True,
    )


def expansion_block(path: str, layer: str = "",
                    family: str = "") -> BlockSpec:
    """Deterministic stage growth (rendering markdown, DISCARD stubs).
    Family-scoped so inspection / hardcoded_data growth folds into its
    own pool instead of feeding it from outside; generic growth is
    supporting content (framework rendering overhead)."""
    suffix = f":{family}" if family else ""
    pooled = ("inspection" if family in ("inspection", "hardcoded_data")
              else "support|content")
    return BlockSpec(
        key=f"{path}:expansion{suffix}",
        label=_p(path, "stage rendering expansion (deterministic growth)"),
        kind="hardmeta", role=NodeRole.SUPPORT,
        agentic_group=f"{path}|support|EXPANSION{suffix}",
        pooled_group=pooled,
        source=True,
    )


# cross-layer pooled sinks: compaction cuts, synthesis condensation
# and memory-only carry merge across all agents (sinks never emit —
# no cycle risk)
_SINK_POOL_GLOBAL = {
    SinkFamily.HARDCODED_CUT: "sink|hardcoded_cut",
    SinkFamily.TRIAGE_CUT: "sink|triage_cut",
    SinkFamily.CONDENSED: "sink|condensed",
    SinkFamily.MEMORY_UNCITED: "sink|memory",
    SinkFamily.WM_RETAINED: "sink|memory",
    SinkFamily.LEDGER_UNCITED: "sink|memory",
    SinkFamily.NOT_CITED: "sink|not_cited",
    SinkFamily.DEDUP_EXIT: "sink|dedup",
}


def sink_block(path: str, family: str, layer: str = "") -> BlockSpec:
    return BlockSpec(
        key=f"{path}:sink:{family}",
        label=_p(path, _SINK_LABEL[family]),
        kind="removed", role=NodeRole.SINK,
        agentic_group=f"{path}|sink|{family}",
        pooled_group=_SINK_POOL_GLOBAL.get(family,
                                           f"{layer}|sink|{family}"),
        sink=True,
    )


def batch_block(path: str, tool_name: str, occ: int,
                layer: str = "") -> BlockSpec:
    return BlockSpec(
        key=f"{path}:{tool_name}#{occ}:batch",
        label=_p(path, f"{tool_name} · parallel batch collector"),
        kind="merge", role=NodeRole.BATCH,
        agentic_group=None, pooled_group=f"{layer}|batch",
    )


_POOLED_CORE = {
    "context": "agent context (dedup merge)",
    "answer": "answer",
    "deliverable": "result envelope (deliverable)",
    "wm": "working-memory archive",
    "introduced": "newly written by the agent (LLM additions)",
    "batch": "parallel batch collector",
}

_POOLED_SUPPORT = dict(
    {c.lower(): lbl for c, lbl in _SUPPORT_LABEL.items()},
    wrapper="hardcoded relay wrapper",
    hydration="DB hydration (workflow enrichment)",
    expansion="stage rendering expansion (deterministic growth)",
)


_POOLED_GLOBAL = {
    "support|content": "supporting content (briefs · seeds ·"
                       " scaffolding · wrappers · utility/error"
                       " returns · LLM additions)",
    "support|memory": "memory carry (WM render · transient)",
    "inspection": "deterministic DB evidence (inspection tools +"
                  " ledger + DB hydration · deduped)",
    "sink|hardcoded_cut": "hardcoded compaction cut",
    "sink|triage_cut": "agentic triage cut",
    "sink|condensed": "condensed away in synthesis",
    "sink|memory": "retained only in memory (WM archive · uncited"
                   " memory carry · uncited ledger)",
    "sink|not_cited": "not cited downstream",
    "sink|dedup": "re-confirmed known IDs (dedup)",
}


def pooled_group_label(group: str, count: int) -> str | None:
    """Readable label for a layer-scoped pooled group key
    ("L1|search|raw" → "L1 · search · raw results (6×)")."""
    tally = f" ({count}×)" if count > 1 else ""
    if group in _POOLED_GLOBAL:
        return f"{_POOLED_GLOBAL[group]}{tally}"
    parts = group.split("|")
    if parts[0] not in LAYERS:
        # branch-scoped tool rail: branch | layer | family | role
        if len(parts) == 4 and parts[1] in LAYERS:
            role = parts[3].removesuffix(":src")
            stage = _STAGE_LABEL.get(role, role)
            tag = " (direct call)" if parts[3].endswith(":src") else ""
            head = (parts[0] if parts[0].lower() == parts[1].lower()
                    else f"{parts[0]} · {parts[1]}")
            return f"{head} · {parts[2]} · {stage}{tag}{tally}"
        return None
    layer, rest = parts[0], parts[1:]
    if len(rest) == 1 and rest[0] in _POOLED_CORE:
        core = _POOLED_CORE[rest[0]]
        if rest[0] == "answer" and layer == "main":
            core = "final answer"
    elif rest == ["env"]:
        core = "envelope (merged fields)"
    elif rest[0] == "env" and len(rest) == 2:
        core = f"envelope · {_FIELD_LABEL[rest[1]]}"
    elif rest[0] == "support" and len(rest) == 2:
        core = _POOLED_SUPPORT.get(rest[1], rest[1])
    elif rest[0] == "sink" and len(rest) == 2:
        core = _SINK_LABEL.get(rest[1], rest[1])
    elif len(rest) == 2:  # tool rail: family | role(:src)
        role = rest[1].removesuffix(":src")
        stage = _STAGE_LABEL.get(role, role)
        tag = " (direct call)" if rest[1].endswith(":src") else ""
        core = f"{rest[0]} · {stage}{tag}"
    else:
        return None
    return f"{layer} · {core}{tally}"


# ── registry validation ───────────────────────────────────────

def validate_registry() -> list[str]:
    """Static consistency checks; returns problem strings (empty = ok)."""
    from .tool_registry import TOOLS
    problems: list[str] = []
    for spec in AGENTS.values():
        for t in spec.tools:
            if t not in TOOLS:
                problems.append(f"{spec.key}: tool '{t}' not in TOOLS")
        for d in spec.dispatchable:
            if d not in spec.tools:
                problems.append(f"{spec.key}: dispatcher '{d}' not in own tools")
            tool = TOOLS.get(d)
            if tool is not None and not tool.is_dispatcher:
                problems.append(f"{spec.key}: '{d}' has no dispatch target")
    for tool in TOOLS.values():
        if tool.is_dispatcher and tool.dispatches != "MIXED" \
                and tool.dispatches not in AGENTS:
            problems.append(f"tool '{tool.name}' dispatches unknown agent "
                            f"'{tool.dispatches}'")
    return problems
