"""Graph model — nodes/edges carrying full Measures + provenance.

One skeleton per session holds ALL FOUR identities at once: every edge
carries a Measure (chars + id set); metric projections read
``measure.value(metric)`` and drop zero-value elements.  Merging by
group key (detailed→agentic→pooled) unions ids and sums chars — it can
never invent mass.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace

from framework_registry.stage_templates import (BlockSpec,
                                                pooled_group_label)
from funnel_evidence.measures import Measure

METRICS = ("chars", "ids", "blocks", "pts")


@dataclass
class Node:
    key: str
    label: str
    kind: str
    role: str
    agentic_group: str | None = None
    pooled_group: str | None = None
    source: bool = False         # declared root (may emit w/o inflow)
    sink: bool = False           # declared terminal (absorbs only)
    order: int = 0
    provenance: tuple = ()
    meta: dict = field(default_factory=dict)


@dataclass
class Edge:
    source: str
    target: str
    measure: Measure
    flow: str
    provenance: tuple = ()


class Skeleton:
    def __init__(self) -> None:
        self.nodes: dict[str, Node] = {}
        self.edges: list[Edge] = []
        self.problems: list[str] = []
        self._order = 0

    def block(self, spec: BlockSpec, order: int | None = None,
              provenance: tuple = (), **meta) -> str:
        node = self.nodes.get(spec.key)
        if node is None:
            self._order += 1
            node = Node(key=spec.key, label=spec.label, kind=spec.kind,
                        role=spec.role, agentic_group=spec.agentic_group,
                        pooled_group=spec.pooled_group,
                        source=spec.source, sink=spec.sink,
                        order=order if order is not None else self._order,
                        provenance=tuple(provenance), meta=dict(meta))
            self.nodes[spec.key] = node
        else:
            if provenance:
                node.provenance = tuple(dict.fromkeys(
                    node.provenance + tuple(provenance)))
            node.meta.update(meta)
        return spec.key

    def edge(self, source: str, target: str, measure: Measure, flow: str,
             provenance: tuple = ()) -> None:
        if source not in self.nodes or target not in self.nodes:
            raise KeyError(f"edge endpoints missing: {source} -> {target}")
        if measure.chars <= 0 and not measure.ids:
            return
        self.edges.append(Edge(source=source, target=target,
                               measure=measure, flow=flow,
                               provenance=tuple(provenance)))

    # ── mechanical group merges ───────────────────────────────

    def merged(self, group_attr: str) -> "Skeleton":
        """New skeleton with nodes sharing a non-None group key merged.

        The merged node keeps the group key as its new key; labels drop
        the instance-path prefix and gain an occurrence count; edges
        re-point and PARALLEL EDGES STAY SEPARATE — each instance's
        contribution keeps its copies (dedup is the contexts' job);
        self-loops from within-group edges collapse.
        """
        mapping: dict[str, str] = {}
        groups: dict[str, list[Node]] = {}
        for node in self.nodes.values():
            group = getattr(node, group_attr)
            if group:
                mapping[node.key] = f"grp:{group}"
                groups.setdefault(f"grp:{group}", []).append(node)
            else:
                mapping[node.key] = node.key

        out = Skeleton()
        out.problems = list(self.problems)
        # groups that swallow ALL their in-edges (e.g. a tool rail
        # collapsed to one node) become sources when any member is one
        ext_in: set = set()
        for edge in self.edges:
            s, t = mapping[edge.source], mapping[edge.target]
            if s != t:
                ext_in.add(t)
        for node in self.nodes.values():
            new_key = mapping[node.key]
            if new_key == node.key:
                out.nodes[node.key] = replace(node)
                continue
            members = groups[new_key]
            if new_key in out.nodes:
                continue
            first = members[0]
            label = (pooled_group_label(new_key[4:], len(members))
                     or _merged_label(members))
            merged_meta: dict = {}
            prov: list = []
            for m in members:
                prov.extend(m.provenance)
            src_flag = all(m.source for m in members) or (
                any(m.source for m in members) and new_key not in ext_in)
            roles = {m.role for m in members}
            # mixed-role pools (rails folded into a source block) act
            # as generic supportive sources
            role = first.role if len(roles) == 1 else "support"
            out.nodes[new_key] = Node(
                key=new_key, label=label, kind=first.kind, role=role,
                agentic_group=getattr(first, "agentic_group")
                if group_attr != "agentic_group" else None,
                pooled_group=getattr(first, "pooled_group")
                if group_attr != "pooled_group" else None,
                source=src_flag,
                sink=all(m.sink for m in members),
                order=min(m.order for m in members),
                provenance=tuple(dict.fromkeys(prov)),
                meta=merged_meta)
        for edge in self.edges:
            s, t = mapping[edge.source], mapping[edge.target]
            if s == t:
                continue
            out.edges.append(Edge(source=s, target=t,
                                  measure=edge.measure, flow=edge.flow,
                                  provenance=edge.provenance))
        return out


def _merged_label(members: list[Node]) -> str:
    base = members[0].label
    # drop the instance-path display prefix ("A1 · L1#2 · ") up to the
    # stage-descriptive tail, keep it when all members share the prefix
    tails = {m.label.split(" \u00b7 ", 1)[-1] if " \u00b7 " in m.label
             else m.label for m in members}
    prefixes = {m.label.rsplit(" \u00b7 ", 1)[0] for m in members}
    if len(members) == 1:
        return base
    if len(tails) == 1:
        tail = next(iter(tails))
        if len(prefixes) == 1 and " \u00b7 " in base:
            return f"{base} ({len(members)}\u00d7)"
        return f"{tail} ({len(members)}\u00d7)"
    common = base
    return f"{common} (+{len(members) - 1} merged)"


def node_measures(skel: Skeleton) -> dict[str, dict[str, Measure]]:
    """Per node: {'in': Measure, 'out': Measure} aggregates."""
    out: dict[str, dict[str, Measure]] = {
        k: {"in": Measure(), "out": Measure()} for k in skel.nodes}
    for e in skel.edges:
        i = out[e.target]["in"]
        out[e.target]["in"] = Measure(chars=i.chars + e.measure.chars,
                                      ids=i.ids | e.measure.ids)
        o = out[e.source]["out"]
        out[e.source]["out"] = Measure(chars=o.chars + e.measure.chars,
                                       ids=o.ids | e.measure.ids)
    return out
