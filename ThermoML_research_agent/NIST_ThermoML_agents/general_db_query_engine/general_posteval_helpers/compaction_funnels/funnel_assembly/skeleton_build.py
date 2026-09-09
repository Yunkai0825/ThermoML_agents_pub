"""Canonical detailed skeleton — recursive assembly over the tree.

One skeleton per session carries chars + ids on every edge (blocks/pts
are projections).  Assembly rules (registry-encoded caveats):

- every tool chain and every child relay targets the CALLER's
  context_merge; the context is the id dedup layer (duplicate copies
  exit via the dedup sink; chars are additive).
- stage sizes come from the logged pipeline table; pre-delivery ids
  from sanctioned re-execution off the verbatim logged args (pure DB
  tools only; stateful tools inherit the det ids).
- DISCARD stubs enter context as chars only (stub prose ids are
  excluded from evidence).
- the inspection ledger feeds the envelope DIRECTLY (deterministic
  side-channel); inspection mass reaches context via the validation
  tool lane.
- CONSERVATION: every downstream lane DRAWS from the caller's context
  budget (chars capped, each id exits once); shortfalls come from
  explicit declared sources (transient carry / LLM additions /
  hydration / scaffolding); WM recording is a chars-only copy drawn
  out of the context into the archive store, and the WM render into
  the prompt is a declared supportive-context root.
"""

from __future__ import annotations

import json

from framework_registry.agent_registry import FieldClass
from framework_registry.stage_templates import (NodeRole, SinkFamily,
                                                SupportClass, answer_block,
                                                batch_block, context_block,
                                                deliverable_block,
                                                envelope_part_block,
                                                expansion_block,
                                                hydration_block,
                                                introduced_block, sink_block,
                                                support_block, tool_family,
                                                tool_stage_block,
                                                wm_archive_block,
                                                wrapper_block)
from framework_registry.tool_registry import (DET_ONLY, EXEMPT,
                                              FULL_PIPELINE, RELAY,
                                              chain_shape)
from funnel_evidence.delegation_tree import AgentInstance, ToolUse
from funnel_evidence.envelope_evidence import (EnvelopePartition,
                                               envelope_partition,
                                               final_context_ids,
                                               partition_payload_text,
                                               question_text)
from funnel_evidence.measures import Measure, measure, thermoml_ids
from funnel_evidence.memory_evidence import wm_measure, wm_records
from funnel_evidence.reexec import reexec_stages
from funnel_assembly.graph_model import Skeleton


def build_skeleton(tree) -> Skeleton:
    skel = Skeleton()
    skel.problems.extend(tree.problems)
    _emit_instance(skel, tree.root)
    return skel


# ── per-ToolUse stage measures ────────────────────────────────

def _stage_measures(use: ToolUse) -> dict:
    """native/det/kept Measures + verdict for one executed ToolUse."""
    step = use.step
    delivered = Measure(chars=step.result_chars,
                        ids=frozenset(thermoml_ids(step.result_text)))
    shape = chain_shape(use.spec)
    pr, sub = use.pipeline_row, use.subagent_row
    verdict = (pr.verdict if pr else sub.verdict if sub else
               ("SKIP" if shape != FULL_PIPELINE else "KEEP"))
    kept_ids = frozenset() if verdict == "DISCARD" else delivered.ids
    kept_c = (pr.agentic if pr else
              sub.output_chars if sub else delivered.chars)

    det_c = (pr.hardcoded if pr else
             sub.input_chars if sub else delivered.chars)
    native_c = pr.native if pr else None

    rx = None
    if shape in (FULL_PIPELINE, DET_ONLY) and not use.spec.stateful \
            and step.status == "ok":
        rx = reexec_stages(use.spec.name, use.kwargs,
                           use.spec.catalog)
    if shape == DET_ONLY:
        det_ids = delivered.ids
    else:
        det_ids = (rx[1].ids | kept_ids) if rx else kept_ids
    native_ids = (rx[0].ids | det_ids) if rx else det_ids
    if native_c is None:
        native_c = rx[0].chars if rx else det_c
    return {
        "native": Measure(chars=native_c, ids=native_ids),
        "det": Measure(chars=det_c, ids=det_ids),
        "kept": Measure(chars=kept_c, ids=kept_ids),
        "delivered": delivered,
        "verdict": verdict,
        "reexec_checked": rx is not None,
    }


def _branch(inst: AgentInstance) -> str:
    """Top-level dispatch lane: the root's direct child this instance
    sits under (terminal roots), the root itself otherwise — evidence
    tool rails pool only inside one lane."""
    node = inst
    while node.parent is not None and node.parent.parent is not None:
        node = node.parent
    if node.parent is None or not node.parent.spec.terminal:
        root = node if node.parent is None else node.parent
        return root.sid.split("/")[-1]
    return node.sid.split("/")[-1]


def _emit_tool_chain(skel: Skeleton, use: ToolUse, ctx_key: str,
                     dedup: "_CtxPool") -> None:
    path = use.caller.sid
    layer = use.caller.spec.layer
    branch = _branch(use.caller)
    # the menu wrapper always runs the owning catalog's FULL two-stage
    # pipeline, whatever the inner tool's native flags say
    shape = (FULL_PIPELINE if use.menu_expanded
             else chain_shape(use.spec))
    order = use.step.seq * 10
    prov = (use.provenance,)
    meta = {"args": json.dumps(use.kwargs, ensure_ascii=False, default=str),
            "status": use.step.status, "menu": use.menu_expanded}

    if use.step.status != "ok" or shape in (EXEMPT, RELAY):
        family = ("error" if use.step.status != "ok"
                  else tool_family(use.spec))
        node = tool_stage_block(path, use.spec, use.occ, NodeRole.ASIS,
                                menu=use.menu_expanded, family=family,
                                source=True, layer=layer, branch=branch)
        # error text enters context verbatim; its echoed ids are real
        # transient carries (arg echoes), NOT DB evidence
        m = Measure(chars=use.step.result_chars,
                    ids=frozenset(thermoml_ids(use.step.result_text)))
        if m.chars <= 0 and not m.ids:
            return
        skel.block(node, order=order, provenance=prov, **meta)
        dedup.feed(skel, node.key, ctx_key, m, "context", prov)
        return

    stages = _stage_measures(use)
    meta["verdict"] = stages["verdict"]
    meta["reexec_checked"] = stages["reexec_checked"]
    native, det, kept = stages["native"], stages["det"], stages["kept"]
    discard = stages["verdict"] == "DISCARD"

    raw_b = tool_stage_block(path, use.spec, use.occ, NodeRole.RAW,
                             menu=use.menu_expanded, layer=layer,
                             branch=branch)
    hard_b = tool_stage_block(path, use.spec, use.occ, NodeRole.HARDCODED,
                              menu=use.menu_expanded, layer=layer,
                              branch=branch)
    skel.block(raw_b, order=order, provenance=prov, **meta)
    skel.block(hard_b, order=order + 1, provenance=prov)
    skel.edge(raw_b.key, hard_b.key,
              Measure(chars=min(det.chars, native.chars), ids=det.ids),
              "retained", prov)
    _stage_expansion(skel, use, hard_b.key, det.chars - native.chars, prov)
    cut = Measure(chars=max(native.chars - det.chars, 0),
                  ids=native.ids - det.ids)
    # compaction may drop an INSPECTED block's id token, but the
    # deterministic inspection ledger keeps the record — those ids
    # ride to the context's ledger shelf instead of dying in the cut
    rec_ids = (cut.ids if tool_family(use.spec) == "inspection"
               else frozenset())
    if rec_ids:
        dedup.feed(skel, raw_b.key, ctx_key,
                   Measure(chars=0, ids=rec_ids), "metadata", prov,
                   split={"ledger": Measure(chars=0, ids=rec_ids)})
        cut = Measure(chars=cut.chars, ids=cut.ids - rec_ids)
    if cut.chars or cut.ids:
        sink = sink_block(path, SinkFamily.HARDCODED_CUT, layer=layer)
        skel.block(sink, order=order + 5)
        skel.edge(raw_b.key, sink.key, cut, "removed", prov)

    if shape == FULL_PIPELINE:
        kept_b = tool_stage_block(path, use.spec, use.occ, NodeRole.AGENTIC,
                                  menu=use.menu_expanded, layer=layer,
                                  branch=branch)
        skel.block(kept_b, order=order + 2, provenance=prov)
        if discard:
            # whole det content cut; the stub is triage-agent prose
            sink = sink_block(path, SinkFamily.TRIAGE_CUT, layer=layer)
            skel.block(sink, order=order + 5)
            skel.edge(hard_b.key, sink.key, det, "removed", prov)
            _stage_expansion(skel, use, kept_b.key, kept.chars, prov,
                             note="DISCARD stub (triage-agent prose)")
        else:
            skel.edge(hard_b.key, kept_b.key,
                      Measure(chars=min(kept.chars, det.chars),
                              ids=kept.ids),
                      "retained", prov)
            _stage_expansion(skel, use, kept_b.key,
                             kept.chars - det.chars, prov)
            tcut = Measure(chars=max(det.chars - kept.chars, 0),
                           ids=det.ids - kept.ids)
            if tcut.chars or tcut.ids:
                sink = sink_block(path, SinkFamily.TRIAGE_CUT, layer=layer)
                skel.block(sink, order=order + 5)
                skel.edge(hard_b.key, sink.key, tcut, "removed", prov)
        dedup.feed(skel, kept_b.key, ctx_key, kept, "context", prov)
    else:  # DET_ONLY — delivered as-is (no agentic triage)
        asis_b = tool_stage_block(path, use.spec, use.occ, NodeRole.ASIS,
                                  menu=use.menu_expanded, layer=layer,
                                  branch=branch)
        skel.block(asis_b, order=order + 2, provenance=prov)
        skel.edge(hard_b.key, asis_b.key, kept, "retained", prov)
        dedup.feed(skel, asis_b.key, ctx_key, kept, "context", prov)


def _stage_expansion(skel: Skeleton, use: ToolUse, target_key: str,
                     diff: int, prov: tuple, note: str = "") -> None:
    """Downstream stage larger than upstream = deterministic rendering /
    triage prose growth, drawn as an explicit expansion source."""
    if diff <= 0:
        return
    exp = expansion_block(use.caller.sid, layer=use.caller.spec.layer,
                          family=tool_family(use.spec))
    skel.block(exp, note=note or "stage rendering expansion")
    skel.edge(exp.key, target_key, Measure(chars=diff), "metadata", prov)


# ── context dedup pool ────────────────────────────────────────

class _CtxPool:
    """Budget ledger of one agent context.

    In-edges carry full Measures; every downstream lane must DRAW from
    the pool (chars capped by the remaining budget, each id exits at
    most once).  Contributions are class-tagged (general evidence /
    memory carry / relayed ledger) so uncited leftovers exit through
    class-specific sinks; draws consume general content first —
    memory and ledger are reference material.  Whatever is never
    drawn leaves via the explicit sinks at close().
    """

    _BUCKETS = ("general", "memory", "ledger")

    def __init__(self, path: str, layer: str = ""):
        self.path = path
        self.layer = layer
        self.seen: set = set()        # every id ever fed
        self.dups: set = set()        # ids fed 2+ times
        self.available: set = set()   # fed, not yet drawn
        self.id_bucket: dict = {}     # id -> arrival bucket (first wins)
        self.chars_left = {b: 0 for b in self._BUCKETS}
        self.chars_in = 0
        self.archive_chars = 0        # WM-archive budget (record draws)

    def feed(self, skel: Skeleton, source: str, ctx_key: str,
             m: Measure, flow: str, prov: tuple = (),
             split: dict | None = None) -> None:
        skel.edge(source, ctx_key, m, flow, prov)
        for bucket, bm in (split or {"general": m}).items():
            self.chars_left[bucket] += bm.chars
            self.chars_in += bm.chars
            for i in bm.ids:
                if i not in self.seen:
                    self.id_bucket[i] = bucket
            self.dups |= (bm.ids & self.seen)
            self.available |= (bm.ids - self.seen)
            self.seen |= bm.ids

    def draw(self, skel: Skeleton, ctx_key: str, target: str,
             want: Measure, flow: str, prov: tuple = (),
             ids_only: bool = False) -> tuple[Measure, frozenset]:
        """Draw ``want`` from the context toward ``target``.

        Returns (drawn, never): ``drawn`` is what the budget allowed
        (edge emitted when non-empty); ``never`` are ids that never
        entered the context (caller sources them explicitly).  Ids
        already drawn by an earlier lane are dropped silently — they
        reached the destination via that lane.
        """
        ids = frozenset(want.ids & self.available)
        self.available -= ids
        chars = 0
        if not ids_only:
            need = want.chars
            for bucket in self._BUCKETS:
                take = min(need - chars, self.chars_left[bucket])
                self.chars_left[bucket] -= take
                chars += take
                if chars >= need:
                    break
        drawn = Measure(chars=chars, ids=ids)
        if drawn.chars > 0 or drawn.ids:
            skel.edge(ctx_key, target, drawn, flow, prov)
        return drawn, frozenset(want.ids - self.seen)

    def close(self, skel: Skeleton, ctx_key: str) -> None:
        if self.dups:
            sink = sink_block(self.path, SinkFamily.DEDUP_EXIT,
                              layer=self.layer)
            skel.block(sink)
            skel.edge(ctx_key, sink.key,
                      Measure(chars=0, ids=frozenset(self.dups)),
                      "deduplicated")
        leftover_ids = {b: set() for b in self._BUCKETS}
        for i in self.available:
            leftover_ids[self.id_bucket.get(i, "general")].add(i)
        families = {"general": (SinkFamily.NOT_CITED,
                                SinkFamily.CONDENSED),
                    "memory": (SinkFamily.MEMORY_UNCITED,) * 2,
                    "ledger": (SinkFamily.LEDGER_UNCITED,) * 2}
        for bucket in self._BUCKETS:
            id_fam, chars_fam = families[bucket]
            ids = leftover_ids[bucket]
            chars = self.chars_left[bucket]
            if id_fam == chars_fam:
                if ids or chars > 0:
                    sink = sink_block(self.path, id_fam, layer=self.layer)
                    skel.block(sink)
                    skel.edge(ctx_key, sink.key,
                              Measure(chars=max(chars, 0),
                                      ids=frozenset(ids)), "removed")
                continue
            if ids:
                sink = sink_block(self.path, id_fam, layer=self.layer)
                skel.block(sink)
                skel.edge(ctx_key, sink.key,
                          Measure(chars=0, ids=frozenset(ids)), "removed")
            if chars > 0:
                sink = sink_block(self.path, chars_fam, layer=self.layer)
                skel.block(sink)
                skel.edge(ctx_key, sink.key, Measure(chars=chars),
                          "removed")

    @property
    def pool(self) -> frozenset:
        return frozenset(self.seen)


# ── instance emission ─────────────────────────────────────────

def _instance_partition(inst: AgentInstance) -> EnvelopePartition:
    if inst.owns_session:
        return envelope_partition(inst.session)
    rec = _wm_record_for(inst)
    if rec is not None:
        return partition_payload_text(
            rec.text, f"{_wm_name_of(inst.session)}::### {rec.record}")
    if inst.dispatch is not None:
        text = inst.dispatch.step.result_text
        if len(inst.dispatch.children) > 1:
            item = _batch_item(text, inst)
            if item is not None:
                return partition_payload_text(
                    item, f"{inst.dispatch.provenance}::batch item")
        return partition_payload_text(text, inst.dispatch.provenance)
    return partition_payload_text("")


def _batch_item(text: str, inst: AgentInstance) -> str | None:
    """One worker's envelope out of a parallel-batch result JSON."""
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end <= start:
        return None
    try:
        payload = json.loads(text[start: end + 1])
    except json.JSONDecodeError:
        return None
    items = payload.get("results") if isinstance(payload, dict) else None
    if not isinstance(items, list) or not items:
        return None
    siblings = list(inst.dispatch.children)
    idx = next((i for i, c in enumerate(siblings) if c is inst), None)
    if idx is None or idx >= len(items):
        return None
    item = items[idx]
    inner = item.get("result", item) if isinstance(item, dict) else item
    return inner if isinstance(inner, str) else json.dumps(
        inner, ensure_ascii=False)


def _wm_record_for(inst: AgentInstance):
    """The archived L1_query_N payload matching an in-process worker.
    JSON records only — prose archive copies never outrank the
    verbatim dispatch text as the partition source."""
    if not inst.token.startswith("L1_"):
        return None
    ordinal = inst.token.rsplit("_", 1)[-1]
    for rec in wm_records(inst.session):
        if rec.fields and rec.record.rsplit("_", 1)[-1] == ordinal:
            return rec
    return None


def _wm_name_of(session) -> str:
    from funnel_evidence.memory_evidence import wm_path
    p = wm_path(session)
    return p.name if p else "working_memory.md"


def _emit_instance(skel: Skeleton, inst: AgentInstance) -> str:
    """Emit one instance subgraph; returns its deliverable node key
    ("" for the terminal root)."""
    path = inst.sid
    layer = inst.spec.layer
    ctx_b = context_block(path, layer=layer)
    ctx_key = skel.block(ctx_b, sid=path, agent=inst.spec.key)
    pool = _CtxPool(path, layer=layer)

    # support: brief (from the live dispatch args) or root seed
    if inst.dispatch is not None:
        brief_text = json.dumps(inst.dispatch.kwargs, ensure_ascii=False,
                                default=str)
        brief = support_block(path, SupportClass.BRIEF, layer=layer)
        skel.block(brief, provenance=(inst.dispatch.provenance,),
                   args=brief_text)
        pool.feed(skel, brief.key, ctx_key, measure(brief_text),
                  "context", (inst.dispatch.provenance,))
    elif inst.owns_session:
        seed_text = question_text(inst.session)
        if seed_text:
            seed = support_block(path, SupportClass.SEED, layer=layer)
            skel.block(seed, provenance=("result.md::Question",))
            pool.feed(skel, seed.key, ctx_key, measure(seed_text),
                      "context", ("result.md::Question",))

    # working-memory render (session owners with a WM file)
    if inst.owns_session and inst.spec.wm_kind:
        wm_m = wm_measure(inst.session)
        if wm_m.chars:
            wmr = support_block(path, SupportClass.WM_RENDER, layer=layer)
            skel.block(wmr, provenance=(f"{_wm_name(inst)}::{path}",))
            pool.feed(skel, wmr.key, ctx_key, wm_m, "memory",
                      split={"memory": wm_m})

    # tool uses in chronology; dispatchers recurse first
    for use in inst.tool_uses:
        if use.spec.is_dispatcher and use.children:
            child_deliverables = []
            for child in use.children:
                d_key = _emit_instance(skel, child)
                child_deliverables.append(
                    (child, d_key, _instance_partition(child)))
            target = ctx_key
            if len(child_deliverables) > 1:
                bat = batch_block(path, use.spec.name, use.occ,
                                  layer=layer)
                skel.block(bat, order=use.step.seq * 10,
                           provenance=(use.provenance,))
                target = bat.key
            total_parts = sum(p.total.chars for _c, _k, p
                              in child_deliverables)
            wrap_c = max(use.step.result_chars - total_parts, 0)
            relay_total = Measure()
            seen_batch: set = set()
            dup_batch: set = set()
            led_chars = 0
            led_ids: set = set()
            for child, d_key, part in child_deliverables:
                # relay what ARRIVED at the deliverable (union of the
                # class lanes) — whole-text re-extraction can pair
                # lit::block ids differently than the field texts did
                ids = (frozenset().union(*(mm.ids for mm
                                           in part.parts.values()))
                       if part.parts else part.total.ids)
                m = Measure(chars=part.total.chars, ids=ids)
                led = part.part(FieldClass.LEDGER)
                led_m = Measure(chars=min(led.chars, m.chars),
                                ids=m.ids & led.ids)
                if target == ctx_key:
                    pool.feed(skel, d_key, ctx_key, m, "relay",
                              (use.provenance,),
                              split={"general": Measure(
                                  chars=m.chars - led_m.chars,
                                  ids=m.ids - led_m.ids),
                                  "ledger": led_m})
                else:
                    skel.edge(d_key, target, m, "relay", (use.provenance,))
                    dup_batch |= (m.ids & seen_batch)
                    seen_batch |= m.ids
                    led_chars += led_m.chars
                    led_ids |= led_m.ids
                relay_total = Measure(
                    chars=relay_total.chars + m.chars,
                    ids=relay_total.ids | m.ids)
            if wrap_c:
                wr = wrapper_block(path, f"{use.spec.name}#{use.occ}",
                                   layer=layer)
                skel.block(wr)
                if target == ctx_key:
                    pool.feed(skel, wr.key, ctx_key, Measure(chars=wrap_c),
                              "metadata", (use.provenance,))
                else:
                    skel.edge(wr.key, target, Measure(chars=wrap_c),
                              "metadata", (use.provenance,))
                relay_total = Measure(chars=relay_total.chars + wrap_c,
                                      ids=relay_total.ids)
            if target != ctx_key:
                # duplicate copies delivered by 2+ children exit the
                # batch collector explicitly (relay carries the union)
                if dup_batch:
                    sink = sink_block(path, SinkFamily.DUP_CANONICAL,
                                      layer=layer)
                    skel.block(sink)
                    skel.edge(target, sink.key,
                              Measure(chars=0, ids=frozenset(dup_batch)),
                              "deduplicated")
                led_m = Measure(chars=led_chars,
                                ids=relay_total.ids & frozenset(led_ids))
                pool.feed(skel, target, ctx_key, relay_total, "relay",
                          (use.provenance,),
                          split={"general": Measure(
                              chars=relay_total.chars - led_m.chars,
                              ids=relay_total.ids - led_m.ids),
                              "ledger": led_m})
            # WM archive of children payloads (chars-copy out of ctx)
            if inst.spec.wm_kind and inst.owns_session:
                _archive_children(skel, inst,
                                  [(c, k) for c, k, _p in
                                   child_deliverables], pool, ctx_key)
        elif use.spec.is_dispatcher:
            # dispatcher without claimed children (rejected/empty):
            _emit_tool_chain(skel, use, ctx_key, pool)
        else:
            _emit_tool_chain(skel, use, ctx_key, pool)

    part = _instance_partition(inst)
    _emit_tail(skel, inst, ctx_key, pool, part)
    _flush_archive(skel, inst, pool)
    pool.close(skel, ctx_key)
    if inst.spec.terminal:
        return ""
    return deliverable_block(inst.sid, inst.parent.spec.label
                             if inst.parent else "caller",
                             layer=inst.spec.layer).key


def _wm_name(inst: AgentInstance) -> str:
    return ("working_memory.md" if inst.spec.wm_kind == "query_file"
            else "_working_memory.md")


def _archive_children(skel: Skeleton, inst: AgentInstance,
                      child_deliverables, pool: _CtxPool,
                      ctx_key: str) -> None:
    """WM recording of received child payloads: a chars-only copy is
    drawn OUT of the caller's context into the archive store (id
    anchors stay on their context evidence path)."""
    records = wm_records(inst.session)
    if not records:
        return
    wm_b = wm_archive_block(inst.sid, layer=inst.spec.layer)
    for child, _d_key in child_deliverables:
        rec = next((r for r in records
                    if r.record.endswith(f"_{child.token.split('_')[-1]}")),
                   None)
        if rec is None:
            continue
        skel.block(wm_b, provenance=(f"{_wm_name(inst)}::records",))
        drawn, _never = pool.draw(
            skel, ctx_key, wm_b.key, Measure(chars=rec.payload.chars),
            "memory", (f"{_wm_name(inst)}::### {rec.record}",))
        pool.archive_chars += drawn.chars


def _emit_tail(skel: Skeleton, inst: AgentInstance, ctx_key: str,
               pool: _CtxPool, part: EnvelopePartition) -> None:
    path = inst.sid
    layer = inst.spec.layer
    terminal = inst.spec.terminal
    ans_part = part.part(FieldClass.ANSWER)
    ans_b = answer_block(path, terminal, layer=layer)
    skel.block(ans_b, provenance=part.provenance)

    # transient carry: ids the LLM really saw in its delivered context
    # (nudges, gate bounces, in-loop renders) but no modeled channel fed
    carry_pool = (final_context_ids(inst.session) if inst.owns_session
                  else frozenset())

    def top_up(target_key: str, never: frozenset, chars: int) -> frozenset:
        """Source ids/chars that never entered the context: transient
        carries first, LLM additions for the rest.  Returns arrived ids."""
        tr_ids = never & carry_pool
        intro_ids = never - tr_ids
        if tr_ids:
            tr = support_block(path, SupportClass.TRANSIENT, layer=layer)
            skel.block(tr, provenance=("final_full_context.md",))
            skel.edge(tr.key, target_key,
                      Measure(chars=0, ids=frozenset(tr_ids)), "memory")
        if chars > 0 or intro_ids:
            intro = introduced_block(path, layer=layer)
            skel.block(intro)
            skel.edge(intro.key, target_key,
                      Measure(chars=chars, ids=frozenset(intro_ids)),
                      "introduced")
        return never

    # answer lane draws first (evidence priority on the id budget)
    drawn, never = pool.draw(skel, ctx_key, ans_b.key, ans_part,
                             "synthesis")
    top_up(ans_b.key, never, ans_part.chars - drawn.chars)

    if terminal:
        return

    deliv = deliverable_block(path, inst.parent.spec.label
                              if inst.parent else "caller",
                              sink=inst.parent is None, layer=layer)
    deliverable_key = skel.block(deliv, provenance=part.provenance)
    skel.edge(ans_b.key, deliverable_key, ans_part, "relay")
    lane_seen: set = set(ans_part.ids)
    lane_dups: set = set()

    for cls, flow, src in (
            (FieldClass.WRITTEN, "synthesis", "ctx"),
            (FieldClass.HYDRATED, "metadata", "hydration"),
            (FieldClass.WM, "memory", "wm"),
            (FieldClass.VERDICT, "synthesis", "intro"),
            (FieldClass.LEDGER, "metadata", "ledger"),
            (FieldClass.SCAFFOLD, "metadata", "scaffold")):
        m = part.part(cls)
        if not m.chars and not m.ids:
            continue
        env_b = envelope_part_block(path, cls, layer=layer)
        skel.block(env_b, provenance=part.provenance,
                   fields=list(part.fields.get(cls, ())))
        arrived = m.ids
        if src == "ctx":
            drawn, never = pool.draw(skel, ctx_key, env_b.key, m, flow)
            arrived = drawn.ids | top_up(env_b.key, never,
                                         m.chars - drawn.chars)
        elif src == "hydration":
            # DB-hydration writes the text; only the ID anchors ride
            # out of the context
            drawn, never = pool.draw(skel, ctx_key, env_b.key,
                                     Measure(chars=0, ids=m.ids), flow,
                                     ids_only=True)
            hyd = hydration_block(path, layer=layer)
            skel.block(hyd)
            skel.edge(hyd.key, env_b.key,
                      Measure(chars=m.chars, ids=never), "metadata")
            arrived = drawn.ids | never
        elif src == "wm":
            if pool.archive_chars > 0:
                # session owner: field text is assembled from the WM
                # archive store; id anchors stay context evidence
                wm_b = wm_archive_block(path, layer=layer)
                skel.block(wm_b)
                take = min(m.chars, pool.archive_chars)
                pool.archive_chars -= take
                if take:
                    skel.edge(wm_b.key, env_b.key, Measure(chars=take),
                              "memory")
                drawn, never = pool.draw(skel, ctx_key, env_b.key,
                                         Measure(chars=0, ids=m.ids),
                                         flow, ids_only=True)
                arrived = drawn.ids | top_up(env_b.key, never,
                                             m.chars - take)
            else:
                # in-process workers write their own wm fields
                drawn, never = pool.draw(skel, ctx_key, env_b.key, m, flow)
                arrived = drawn.ids | top_up(env_b.key, never,
                                             m.chars - drawn.chars)
        elif src == "ledger":
            led = support_block(path, SupportClass.LEDGER, layer=layer)
            skel.block(led, provenance=part.provenance,
                       inspections=list(part.inspection_ids))
            skel.edge(led.key, env_b.key, m, "metadata")
        elif src == "scaffold":
            sc = support_block(path, SupportClass.SCAFFOLD, layer=layer)
            skel.block(sc)
            skel.edge(sc.key, env_b.key, m, "metadata")
        else:  # intro (verdict prose)
            drawn, never = pool.draw(skel, ctx_key, env_b.key,
                                     Measure(chars=0, ids=m.ids), flow,
                                     ids_only=True)
            intro = introduced_block(path, layer=layer)
            skel.block(intro)
            skel.edge(intro.key, env_b.key,
                      Measure(chars=m.chars, ids=never), "synthesis")
            arrived = drawn.ids | never
        # relay exactly what arrived (ids drawn elsewhere already flow
        # to the deliverable through their own lane)
        skel.edge(env_b.key, deliverable_key,
                  Measure(chars=m.chars, ids=frozenset(arrived)), "relay")
        lane_dups |= (set(arrived) & lane_seen)
        lane_seen |= set(arrived)

    # duplicate copies delivered by 2+ lanes (e.g. an id cited in the
    # answer AND registered in the ledger) exit the envelope explicitly
    # (a parentless root envelope is itself a sink — it absorbs them)
    if lane_dups and inst.parent is not None:
        sink = sink_block(path, SinkFamily.DUP_CANONICAL, layer=layer)
        skel.block(sink)
        skel.edge(deliverable_key, sink.key,
                  Measure(chars=0, ids=frozenset(lane_dups)),
                  "deduplicated")


def _flush_archive(skel: Skeleton, inst: AgentInstance,
                   pool: _CtxPool) -> None:
    """Archived payload mass never shipped in the envelope."""
    if pool.archive_chars <= 0:
        return
    wm_b = wm_archive_block(inst.sid, layer=inst.spec.layer)
    skel.block(wm_b)
    sink = sink_block(inst.sid, SinkFamily.WM_RETAINED,
                      layer=inst.spec.layer)
    skel.block(sink)
    skel.edge(wm_b.key, sink.key, Measure(chars=pool.archive_chars),
              "removed")
    pool.archive_chars = 0
