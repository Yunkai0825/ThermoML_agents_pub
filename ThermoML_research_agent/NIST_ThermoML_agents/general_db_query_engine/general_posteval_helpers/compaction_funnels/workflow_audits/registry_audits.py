"""Registry-driven audits over the canonical skeleton + projections.

Checks (enum/role/flag-based — no label regexes):
- conservation   — per mid node: chars in == out and out ids ⊆ in ids.
- flow           — per projected metric: declared SOURCE blocks never
                   receive, declared SINK blocks never emit, zero-in /
                   zero-out is legal ONLY for them, and internal
                   nodes never emit more value than they receive
                   (chars: exactly what they receive).
- balance        — per layer × metric: Σ source emission == Σ sink
                   intake (chars strict; set metrics: every id must
                   terminate at a sink — no stranded ids).
- acyclic        — every level is a DAG.
- hierarchy      — every edge legal per the role-pair matrix from the
                   stage grammar.
- orphan         — every node reaches the root answer component.
- raw_coverage   — every id in delivered results / envelopes / ledgers
                   appears in the ids-detailed graph.
- envelope_parts — Σ partition == envelope total per instance.
- reexec_drift   — logged pipeline sizes vs re-exec sizes (WARN).
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

from framework_registry.stage_templates import NodeRole
from funnel_evidence.envelope_evidence import envelope_partition
from funnel_evidence.measures import thermoml_ids
from funnel_assembly.graph_model import Skeleton


@dataclass(frozen=True)
class Finding:
    severity: str          # FAIL | WARN | INFO
    check: str
    subject: str
    detail: str


_SOURCE_ROLES = {NodeRole.RAW, NodeRole.SUPPORT, NodeRole.INTRODUCED,
                 NodeRole.RELAY_WRAPPER}
_SINK_ROLES = {NodeRole.SINK}

_ALLOWED = {
    (NodeRole.RAW, NodeRole.HARDCODED), (NodeRole.RAW, NodeRole.SINK),
    (NodeRole.RAW, NodeRole.CONTEXT),
    (NodeRole.RAW, NodeRole.ENVELOPE_PART),
    (NodeRole.HARDCODED, NodeRole.AGENTIC),
    (NodeRole.HARDCODED, NodeRole.ASIS),
    (NodeRole.HARDCODED, NodeRole.SINK),
    (NodeRole.HARDCODED, NodeRole.CONTEXT),
    (NodeRole.AGENTIC, NodeRole.CONTEXT), (NodeRole.ASIS, NodeRole.CONTEXT),
    (NodeRole.ASIS, NodeRole.BATCH),
    (NodeRole.ASIS, NodeRole.ENVELOPE_PART),
    (NodeRole.SUPPORT, NodeRole.CONTEXT),
    (NodeRole.SUPPORT, NodeRole.ENVELOPE_PART),
    (NodeRole.SUPPORT, NodeRole.ANSWER),
    (NodeRole.SUPPORT, NodeRole.HARDCODED),
    (NodeRole.SUPPORT, NodeRole.AGENTIC),
    (NodeRole.SUPPORT, NodeRole.ASIS),
    (NodeRole.SUPPORT, NodeRole.BATCH),
    (NodeRole.SUPPORT, NodeRole.SINK),
    (NodeRole.RELAY_WRAPPER, NodeRole.CONTEXT),
    (NodeRole.RELAY_WRAPPER, NodeRole.BATCH),
    (NodeRole.DELIVERABLE, NodeRole.CONTEXT),
    (NodeRole.DELIVERABLE, NodeRole.BATCH),
    (NodeRole.BATCH, NodeRole.CONTEXT),
    (NodeRole.CONTEXT, NodeRole.ANSWER),
    (NodeRole.CONTEXT, NodeRole.ENVELOPE_PART),
    (NodeRole.CONTEXT, NodeRole.WM_ARCHIVE),
    (NodeRole.CONTEXT, NodeRole.SINK),
    (NodeRole.ANSWER, NodeRole.DELIVERABLE),
    (NodeRole.ENVELOPE_PART, NodeRole.DELIVERABLE),
    (NodeRole.DELIVERABLE, NodeRole.SINK),
    (NodeRole.BATCH, NodeRole.SINK),
    (NodeRole.INTRODUCED, NodeRole.ANSWER),
    (NodeRole.INTRODUCED, NodeRole.ENVELOPE_PART),
    (NodeRole.WM_ARCHIVE, NodeRole.ENVELOPE_PART),
    (NodeRole.WM_ARCHIVE, NodeRole.SINK),
}


def audit_skeleton(skel: Skeleton, level: str) -> list[Finding]:
    findings: list[Finding] = []
    for p in skel.problems:
        findings.append(Finding("WARN", "tree", level, p))

    ins: dict[str, dict] = {}
    outs: dict[str, dict] = {}
    for e in skel.edges:
        i = ins.setdefault(e.target, {"chars": 0, "ids": set()})
        i["chars"] += e.measure.chars
        i["ids"] |= e.measure.ids
        o = outs.setdefault(e.source, {"chars": 0, "ids": set()})
        o["chars"] += e.measure.chars
        o["ids"] |= e.measure.ids

    for key, node in skel.nodes.items():
        has_in, has_out = key in ins, key in outs
        if not has_in or not has_out:
            continue
        if node.source or node.sink:
            continue
        din = ins[key]["chars"]
        dout = outs[key]["chars"]
        if din != dout:
            findings.append(Finding(
                "FAIL", "conservation", f"{level}:{key}",
                f"chars in={din:,} out={dout:,}"))
        extra = outs[key]["ids"] - ins[key]["ids"]
        if extra:
            findings.append(Finding(
                "FAIL", "conservation", f"{level}:{key}",
                f"{len(extra)} ids out of nowhere: "
                f"{sorted(extra)[:6]}"))

    for e in skel.edges:
        src, tgt = skel.nodes[e.source], skel.nodes[e.target]
        if (src.role, tgt.role) not in _ALLOWED:
            findings.append(Finding(
                "FAIL", "hierarchy", f"{level}:{e.source}->{e.target}",
                f"illegal role pair {src.role}->{tgt.role} ({e.flow})"))

    # orphan: connectivity to any answer node (undirected reach)
    answers = {k for k, n in skel.nodes.items() if n.role == NodeRole.ANSWER}
    if answers:
        adjacency: dict[str, set] = {}
        for e in skel.edges:
            adjacency.setdefault(e.source, set()).add(e.target)
            adjacency.setdefault(e.target, set()).add(e.source)
        seen = set()
        stack = list(answers)
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            stack.extend(adjacency.get(node, ()))
        for key in skel.nodes:
            if key not in seen and (key in ins or key in outs):
                findings.append(Finding(
                    "FAIL", "orphan", f"{level}:{key}",
                    "not connected to any answer component"))
    return findings


def audit_coverage(tree, ids_detailed_graph) -> list[Finding]:
    """Every id in delivered results + envelopes + ledgers must appear
    in the detailed ids graph."""
    findings: list[Finding] = []
    graph_ids: set = set()
    for node in ids_detailed_graph.nodes.values():
        graph_ids |= node.ids
    for inst in tree.instances():
        expected: set = set()
        for use in inst.tool_uses:
            if use.step.status == "ok" and (use.pipeline_row is None
                                            or use.pipeline_row.verdict
                                            != "DISCARD"):
                expected |= thermoml_ids(use.step.result_text)
        if inst.owns_session:
            part = envelope_partition(inst.session)
            expected |= part.total.ids
        missing = expected - graph_ids
        if missing:
            findings.append(Finding(
                "FAIL", "raw_coverage", inst.sid,
                f"{len(missing)} evidence ids missing from ids-detailed: "
                f"{sorted(missing)[:8]}"))
    return findings


def audit_envelopes(tree) -> list[Finding]:
    findings: list[Finding] = []
    for inst in tree.instances():
        if not inst.owns_session:
            continue
        part = envelope_partition(inst.session)
        if not part.parts:
            continue
        total = sum(m.chars for m in part.parts.values())
        if total != part.total.chars:
            findings.append(Finding(
                "FAIL", "envelope_parts", inst.sid,
                f"partition {total:,} != envelope {part.total.chars:,}"))
    return findings


def audit_reexec_drift(tree) -> list[Finding]:
    findings: list[Finding] = []
    for inst in tree.instances():
        for use in inst.tool_uses:
            pr = use.pipeline_row
            if pr is None or use.spec.stateful:
                continue
            # drift is informational: the DB may have moved since the run
            from funnel_evidence.reexec import _RESULT_CACHE  # noqa: PLC0415
            import json as _json
            key = (use.spec.name,
                   _json.dumps(use.kwargs, sort_keys=True, default=str))
            cached = _RESULT_CACHE.get(key)
            if not cached:
                continue
            native, det = cached
            if pr.native and native.chars and \
                    abs(native.chars - pr.native) > max(0.15 * pr.native, 200):
                findings.append(Finding(
                    "WARN", "reexec_drift",
                    f"{inst.sid}:{use.spec.name}#{use.occ}",
                    f"native logged {pr.native:,} vs re-exec "
                    f"{native.chars:,} (DB moved since run?)"))
    return findings


def audit_acyclic(skel: Skeleton, level: str) -> list[Finding]:
    """Sankey graphs must be DAGs at every level (plotly draws loops)."""
    graph: dict[str, set] = {}
    for e in skel.edges:
        graph.setdefault(e.source, set()).add(e.target)
    findings: list[Finding] = []
    color: dict[str, int] = {}          # 0 white, 1 gray, 2 black

    def dfs(node: str, stack: list) -> None:
        color[node] = 1
        for nxt in graph.get(node, ()):
            c = color.get(nxt, 0)
            if c == 1:
                cycle = stack[stack.index(nxt):] + [nxt]
                findings.append(Finding(
                    "FAIL", "acyclic", level,
                    " -> ".join(skel.nodes[k].label for k in cycle)))
            elif c == 0:
                dfs(nxt, stack + [nxt])
        color[node] = 2

    for node in list(graph):
        if color.get(node, 0) == 0:
            dfs(node, [node])
    return findings


def audit_flow_conservation(graph, metric: str, level: str) -> list[Finding]:
    """Value-based conservation on the graph that actually renders,
    driven by the DECLARED source/sink flags: sources never receive,
    sinks never emit, zero-in/zero-out is legal only for them, and
    internal nodes emit exactly (chars) / at most (set metrics) what
    they receive."""
    findings: list[Finding] = []
    inflow: dict[str, int] = {}
    outflow: dict[str, int] = {}
    for e in graph.edges:
        inflow[e.target] = inflow.get(e.target, 0) + e.value
        outflow[e.source] = outflow.get(e.source, 0) + e.value
    where = f"{level}/{metric}"
    for key, node in graph.nodes.items():
        nin = inflow.get(key, 0)
        nout = outflow.get(key, 0)
        if node.source:
            if nin > 0:
                findings.append(Finding(
                    "FAIL", "flow", f"{where}:{key}",
                    f"declared source '{node.label}' receives {nin:,}"))
            continue
        if node.sink:
            if nout > 0:
                findings.append(Finding(
                    "FAIL", "flow", f"{where}:{key}",
                    f"declared sink '{node.label}' emits {nout:,}"))
            continue
        if nin == 0 and nout > 0:
            findings.append(Finding(
                "FAIL", "flow", f"{where}:{key}",
                f"'{node.label}' emits {nout:,} with no inflow and no"
                f" source declaration (role {node.role})"))
        elif nout == 0 and nin > 0:
            findings.append(Finding(
                "FAIL", "flow", f"{where}:{key}",
                f"'{node.label}' absorbs {nin:,} without a sink"
                f" declaration (role {node.role})"))
        elif nout > nin:
            findings.append(Finding(
                "FAIL", "flow", f"{where}:{key}",
                f"'{node.label}' out {nout:,} > in {nin:,} "
                f"(value from nowhere)"))
        elif nout < nin:
            findings.append(Finding(
                "FAIL", "flow", f"{where}:{key}",
                f"'{node.label}' out {nout:,} < in {nin:,} "
                f"(copies vanish without a sink)"))
    return findings


def audit_layer_balance(graph, metric: str, level: str) -> list[Finding]:
    """Source↔sink conservation across one layer: everything sources
    emit must be absorbed by declared sinks (exact equality in every
    metric — internal nodes are exactly conserved — plus set metrics:
    every id in the layer must terminate at a sink)."""
    findings: list[Finding] = []
    inflow: dict[str, int] = {}
    outflow: dict[str, int] = {}
    for e in graph.edges:
        inflow[e.target] = inflow.get(e.target, 0) + e.value
        outflow[e.source] = outflow.get(e.source, 0) + e.value
    src_total = sum(outflow.get(k, 0) for k, n in graph.nodes.items()
                    if n.source)
    sink_total = sum(inflow.get(k, 0) for k, n in graph.nodes.items()
                     if n.sink)
    where = f"{level}/{metric}"
    if src_total != sink_total:
        findings.append(Finding(
            "FAIL", "balance", where,
            f"source emission {src_total:,} != sink intake "
            f"{sink_total:,}"))
    if metric != "chars":
        all_ids: set = set()
        sunk_ids: set = set()
        for e in graph.edges:
            all_ids |= e.ids
            if graph.nodes[e.target].sink:
                sunk_ids |= e.ids
        stranded = all_ids - sunk_ids
        if stranded:
            findings.append(Finding(
                "FAIL", "balance", where,
                f"{len(stranded)} ids never reach a sink: "
                f"{sorted(stranded)[:8]}"))
    findings.append(Finding(
        "INFO", "balance", where,
        f"sources emit {src_total:,} / sinks absorb {sink_total:,}"))
    return findings


def audit_projected_connectivity(graph, metric: str, level: str
                                 ) -> list[Finding]:
    """Strict orphan detection on the rendered graph: every node must
    sit in the weak component holding the answer spine, reach a
    declared sink forward, and trace back to a declared source.  A
    detached component is legal ONLY as a dead branch: a complete
    instance sub-funnel (it has its own agent context) whose delivery
    upward weighs zero in this metric — reported as INFO.  Contextless
    fragments (severed tool chains) FAIL."""
    findings: list[Finding] = []
    if not graph.nodes:
        return findings
    fwd: dict[str, set] = {}
    bwd: dict[str, set] = {}
    und: dict[str, set] = {}
    for e in graph.edges:
        fwd.setdefault(e.source, set()).add(e.target)
        bwd.setdefault(e.target, set()).add(e.source)
        und.setdefault(e.source, set()).add(e.target)
        und.setdefault(e.target, set()).add(e.source)

    def reach(starts, adj):
        seen = set(starts)
        stack = list(starts)
        while stack:
            for nb in adj.get(stack.pop(), ()):
                if nb not in seen:
                    seen.add(nb)
                    stack.append(nb)
        return seen

    where = f"{level}/{metric}"
    anchors = [k for k, n in graph.nodes.items()
               if n.role in ("answer", "deliverable")]
    main = reach(anchors, und)
    to_sink = reach([k for k, n in graph.nodes.items() if n.sink], bwd)
    from_src = reach([k for k, n in graph.nodes.items() if n.source], fwd)
    stray = [k for k in graph.nodes if anchors and k not in main]
    while stray:
        comp = sorted(reach([stray[0]], und))
        stray = [k for k in stray if k not in comp]
        if any(graph.nodes[k].role == "context" for k in comp):
            findings.append(Finding(
                "INFO", "orphan", f"{where}:{comp[0]}",
                f"dead branch ({len(comp)} nodes): complete sub-funnel"
                f" with zero {metric} delivered upward"))
        else:
            for key in comp:
                findings.append(Finding(
                    "FAIL", "orphan", f"{where}:{key}",
                    f"'{graph.nodes[key].label}' is disconnected from"
                    f" the answer spine (severed fragment)"))
    for key, node in graph.nodes.items():
        if not node.sink and key not in to_sink:
            findings.append(Finding(
                "FAIL", "orphan", f"{where}:{key}",
                f"'{node.label}' has no forward path to any sink"))
        if not node.source and key not in from_src:
            findings.append(Finding(
                "FAIL", "orphan", f"{where}:{key}",
                f"'{node.label}' is not fed from any declared source"))
    return findings


def run_audits(build_result) -> list[Finding]:
    findings: list[Finding] = []
    for level, skel in build_result["skeletons"].items():
        findings.extend(audit_skeleton(skel, level))
        findings.extend(audit_acyclic(skel, level))
    for (metric, level), graph in build_result["graphs"].items():
        findings.extend(audit_flow_conservation(graph, metric, level))
        findings.extend(audit_layer_balance(graph, metric, level))
        findings.extend(audit_projected_connectivity(graph, metric, level))
    tree = build_result["tree"]
    findings.extend(audit_coverage(
        tree, build_result["graphs"][("ids", "detailed")]))
    findings.extend(audit_envelopes(tree))
    findings.extend(audit_reexec_drift(tree))
    return findings


def write_report(findings: list[Finding], path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle,
                                fieldnames=["severity", "check", "subject",
                                            "detail"],
                                delimiter="\t")
        writer.writeheader()
        for f in findings:
            writer.writerow({"severity": f.severity, "check": f.check,
                             "subject": f.subject, "detail": f.detail})
    return path
