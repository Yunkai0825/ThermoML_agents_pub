# Sankey Abstraction Levels — Exhaustive vs. General Diagrams

One table per layer, from the deepest tool layer upward. "Exhaustive" =
the per-run + session figures (`sub_<Agent>_*_detailed_*` — each ending
at its `Result envelope to <parent> (deliverable)`; `session_*`
and the DETAILED matrix cells `chars_detailed_*` /
`{ids,pts,blocks}_detailed_*`, which stack the per-run
lanes and continue into the Main context/answer); "General" = the
consolidated figures
(`chars_{pooled,agentic}_*`; the former `general_ids_*` coverage view
is retired — the ids DETAILED cell carries the full raw-ID coverage,
gap-checked at build time). Every level exists for both metrics: **chars**
(volumes) and **IDs** (unique ThermoML identifiers, edges carry the
actual ID sets); differences are noted per row. The full metric ×
abstraction-mode preset matrix (chars/ids/pts × pooled/agentic/detailed)
lives in `compaction_pipeline.settings.FUNNEL_MATRIX`; the general-diagram rows
below describe the chars POOLED cell — the AGENTIC cell stops before the
merged-block/contraction passes, keeping the worker-context,
payload-archive, DB-hydrated and ID-resolution-merge nodes that the ids
column of each table describes. The three modes form a strict
hierarchy: POOLED abstracts AGENTIC, AGENTIC abstracts DETAILED —
every agentic-layer component appears in the detailed lanes expanded
down to raw tool results.

A third family exists for the chronological story: **Workflow
compaction** = `ids_agentic_sankey_*` (IDs) and
`pts_agentic_sankey_*` (datapoints; the same flow with
every edge weighted by the datapoints its qualified block IDs pin) —
Table 5. In the AGENTIC cells, fitting-tool rows (`fit_block`) omit
their hardcoded/agentic stage blocks (fit results pass det-compaction
with unchanged ids, no agentic triage): the raw block feeds the merge
directly; the pooled cells keep fit rows fully staged.
The POOLED cells (`{ids,pts}_pooled_sankey_*`) merge
each agent's per-dispatch L1 rows, its L2 card-read rows AND its
direct tools (`inspect_block`, `get_pure_values`, … — det-compacted
but with no agentic triage) into one row each per stage with
occurrence counts SUMMED — connections unchanged, values no longer
unique-ID cardinalities; only `fit_block` keeps its own row (the pts
pooled cell pools the datapoint projection with the ids grouping,
datapoint totals preserved).
Consolidating set-valued ID flows into per-lane funnels proved to carry
no meaning (a pooled "(n×)" node counts nothing real when values are
set cardinalities), so the IDs story is told as the workflow's
chronology: one funnel per agent activation in TRUE dispatch order,
every tool row showing all three tool-level compaction layers, and the
delivered ids following the workflow's merging layers to the Main
answer.

## Reference — the framework call hierarchy (exhaustive)

The tables below abstract THIS tree (literal `ToolEntry` names;
`workflow_audits.hierarchy_audits` enforces it edge-by-edge on every
built graph; `∥` = parallel fan-out, `∘` = wrapped execution):

```
Main → { T_M , Q_i , A_i , ∥(Q ⊎ A) }                                  shell 0
  T_M  = { run_query_agent→Q_i , run_analysis_agent→A_i , run_parallel_subagents→∥(Q⊎A) ,
           browse_subagent_tools , run_subagent_tool∘t (t ∈ T_L1 ∪ T_A^menu) , list_session_files }
         T_L1 = T_id∪T_blk∪T_sim∪T_rank ; T_A^menu = {inspect_block, get_pure_values}∪T_fit∪
         { query_system_summary , query_blocks , find_similar_compounds } (trio menu-only)
  mem  : MainWorkingMemory ⊕ prev-prompt carry-over
  post : claim ∥ id-align → construct_answer_summary → session ledger

Q_i  → { T_mem , L1_1 … L1_k }                                          shell 1
  T_mem = { memory_read , memory_append_history , memory_add_result , memory_catalog_add ,
            memory_catalog_remove , memory_catalog_list , memory_compact , memory_reset }
          (working_memory.md; L1 payloads auto-archived — L1AutoSaver)

L1   → { T_id , T_blk , T_sim , T_rank , L2_comp , L2_meas , L2_ref , L2_prop }   shell 2
  T_id   = { resolve_ids , resolve_compound_ids , resolve_property_ids ,
             resolve_measurement_ids , resolve_reference_ids , search_id_alignment }
  T_blk  = { search_blocks , block_search_adv , search_system_registry , search_system_summary }
  T_sim  = { search_similar_compounds }        T_rank = { screen_property_systems }
  post   : claim ∥ id-align → { construct_core_blocks_found , construct_core_id_updates }
           → DB-hydrated payload JSON

L2_comp → { search_comp_from_block , search_compound_dk , search_compound_indiv }   shell 3
L2_meas → { search_meas_from_block , search_measurement_dk , search_measurement_indiv }
L2_ref  → { search_reference_from_block , search_references }
L2_prop → { search_prop_dk_from_block , search_property_dk }
  post   : id-align → construct_l2_{compounds,measurements,properties,reference}
  (card-read tools are skip_subagent — the evaluator's answer IS the agentic stage)

A_i  → { T_ev , T_fit , T_cust , query_thermoml[_parallel]→L1 (headless) ,
         align_compositions→L1_align , run_query_agent[s_parallel]→Q_j (nested FULL) }   shell 1
  T_ev   = { inspect_block , get_pure_values , list_session_files }
  T_fit  = { fit_block , fit_block_derived , fit_multi_system , compute_ideal_baseline ,
             predict_from_rk , propose_fitting_plan }
  T_cust = { register_custom_block }
  mem    : AnalysisWorkingMemory (auto-extraction from inspect_block/get_pure_values/fit_block)

L1_align → { search_blocks , search_system_registry , resolve_compound_ids , inspect_block ,
             get_pure_values , fit_block , validate_dual_basis_block , register_estimated_bridge }
```

Universal verticals: per tool call `raw(t) → det(t) → kept(t) → ctx`
(hardcoded compactor, then agentic KEEP/DISCARD triage; skip-flags
short-circuit; side-channels [WM] payload archive + add-only [ID]
catalog) and per agentic shell `answer → claim ∥ id-align →
construct_* → JSON`. **Session memory** = Main WM ⊕ carry-over, Q
`working_memory.md`, A WM; **transient memory** = downward dispatch
briefs + relay-carried ids never logged at a tool stage (pooled per
lane as `transient memory (brief-carried + unlogged in-worker IDs)`).

Mapping onto the diagram vocabulary: `T_id`/`T_blk`/`T_sim`/`T_rank`
rows are the L1 tool stages of Table 2; the `L2_*` card reads and
`construct_core_*` hydration are Table 1; `T_ev`/`T_fit`/`T_cust` are
the agent direct-tool components of Table 3; `T_M` menu-call chains,
child relays and the context→answer sink are Table 4; the
working-memory archive ([WM]) and transient-memory pools live in
Table 2's relay/payload + IDs rows; the post-answer chains surface as
the envelope/summary stages of Tables 3 and 5.

## Table 1 — Raw tool results & L2 layer (leaf evaluators inside L1 workers)

| Abstraction level | Exhaustive diagrams | General diagrams | Basis / provenance |
|---|---|---|---|
| Raw tool results | Not drawn (runs never logged L2 steps); only the per-block evidence appears as `DB-hydrated L2 block GLOBlit_X::PROPblock_Y · N pts` | `L2 tool results · raw (re-exec., N blocks, metadata card reads)` — 4 block-centric reads per validated block (`search_comp/meas/reference/prop_dk_from_block`) + evidence-gated DK/reference follow-ups (`search_compound_dk`, `search_measurement_dk`, `search_property_dk`, `search_references`); exact per-call args in `_l2_calls.txt` | Re-executed against the card DB; follow-ups only counted while the lane total fits the observed §6 L2 prompt budget |
| Hardcoded compaction | — | `L2 hardcoded compact (re-exec.)` + `L2 hardcoded compaction cut (re-exec.)` | Real compactors; only the measurement reads have one (`search_meas_from_block`, `search_measurement_dk`) — all other L2 tools are registered `skip_compactor` (det = raw) |
| Agentic compaction | `L2-evaluator answers · as-is` folded into the L1 kept context | `L2 evaluator answers (observed)` (+ `Condensed by L2 evaluators` cut); in chars the full answers then feed the lane's merged `L1 + L2 tool results` block (the actual engine hand-off into the L1 worker) | Observed: Σ responses of §6 sub-1,900-char-system LLM turns; L2 has **no triage on tool results** (`skip_subagent`) — the evaluator's written answer *is* the agentic compaction |
| Validated anchors | `DB-hydrated L2 block … · N pts` (one node per block) | chars: contracted away — the DB-copied share rides the merged tool block's purple metadata edge into the relays; ids: `DB-hydrated L2 blocks + ID updates/status (n×) · pts avail. in block(s)` (one per lane) with anchor-set stubs | Checksum-validated minimal anchors hydrated from the authoritative DB row (`construct_core_blocks_found`); pts = exact block-CSV row counts |
| IDs metric | Per-block ID sets on the hydrated nodes | `L2 tool results · raw IDs (re-exec.)` → `L2 hardcoded compact IDs` → anchors, with dropped/added ID stubs; IDs pass ≈1:1 through det (compactors trim prose, not IDs) | Union sets from the re-executed texts |

## Table 2 — Raw tool results & L1 layer (query workers dispatched by Q/A agents)

| Abstraction level | Exhaustive diagrams | General diagrams | Basis / provenance |
|---|---|---|---|
| Raw tool results | `L1-query #k tools · raw results` (one node **per worker**; measured for query children) and `L1-query #k tools raw · re-executed (reconstructed args)` (analysis-driven dispatches) | `L1 tool results · raw (n×)` — one canonical node per lane; measured + re-executed variants merged | Query lanes: logged sizes (worker rows precede their relay in the shared log); analysis lanes: re-executed calls with args reconstructed from briefs/envelopes, each validated against the logged triage-prompt size |
| Hardcoded compaction | `L1-query #k tools · hardcoded compact` + per-stage cuts | `L1 hardcoded compact (n×)` + `{agent} · hardcoded compaction cut` pool | Real deterministic compactors (re-exec where unlogged) |
| Agentic compaction | `L1-query #k tools · agentic kept` (logged KEEP/DISCARD verdict outputs); DISCARD stubs | `L1 agentic kept (n×)` — in chars it feeds the lane's merged `L1 + L2 tool results (L1 agentic kept + L2 evaluator answers)` block (the layer's compacted tool deliveries in ONE node; lanes without an L2 chain feed the relays from the kept stage directly) | Logged triage verdicts (§4/Subagent Summary) |
| Worker context | `L1-query #k dispatch brief (seed)` + `L1-query #k worker context` (= seed + kept + L2 answers) | chars: no worker-context node — briefs + seed are instructions, not tool results, and exit via `briefs + seed consumed by the L1 worker (prompts, not re-emitted)`; ids: `L1 worker context (n×)`. Seed split unchanged: `L1 dispatch args (briefs)` (→ `Dispatch briefs` pool) + `L1 seed rendering` (→ `Supporting context` pool) | Seed = first L1 main-turn prompt in §6; args = the dispatch call's JSON in run_history |
| Relay / payload | `L1 query worker relay #k` + payload decomposition: `L1 worker answer+claims (LLM-written)`, `DB-hydrated ID updates + status`, `Payload JSON scaffolding`, DB-hydrated blocks, `L1 full payload · archived to working memory`, `retained only in working memory` | chars: `L1 worker relays into context (n×)` fed by the merged tool block (orange synthesis = worker-written share, purple metadata = DB-hydrated share; archived-but-unrelayed payloads contribute only their forwarded fraction) + supporting scaffolding; the payload-archive node is contracted away (`payload scaffolding retained only in working memory` stub); ids: `L1 payload archive (working memory)` kept | Payload split by provenance from `final_full_context.md` blobs / paper-cases detail TSVs |
| IDs metric | Per-worker set-transitions with drop/add stubs; relay/blob ID decomposition. Every agentic-layer component is expanded: per-dispatch raw→det chains continue through an explicit `L1-query #k agentic kept / delivered (re-exec.)` stage into the relay; each worker's archived L2 blocks expand to `L2 card reads (#k, re-exec.) · raw tool results → · hardcoded compact → · evaluator kept / anchored` (cuts exit at `· IDs cut by L2 evaluators`); the lane's unclaimed reads form one `L2 metadata card reads (re-exec.)` chain into the received merge; relay-text ids beyond every tool stage / payload field pool into ONE per-lane `transient memory (brief-carried + unlogged in-worker IDs)` block (memory links into the relays) | Per-worker raw→det ID chains (re-exec) into each relay with `present in delivered context (dedup'd)` vs `not carried (unlogged agentic kept)` splits; workers with PARSED relay envelopes draw the same raw→det chain (det∩blob forwards first, novel-first attribution shrinks the answer/claims/evidence decomposition groups accordingly) | Delivered-side checked against the full final-context text (previews are truncated) |

## Table 3 — Raw tool results & delegated agent layer (Q/A children, incl. nested)

| Abstraction level | Exhaustive diagrams | General diagrams | Basis / provenance |
|---|---|---|---|
| Raw tool results | Per-component chains: `{agent} Evidence retrieval · raw`, `ID resolution merge · raw`, `Result outputs · raw`, plus `· as-is (compaction-exempt)` and `· direct` | Three-stage pooled categories per lane: `Database search results · raw`, `Fitting tool results` (fit family), everything else classed | Analysis evidence tools (`inspect_block`, `get_pure_values`, …) are det-compacted by the engine but logged post-compaction → natives re-executed |
| Hardcoded compaction | `{component} · hardcoded` + `Hardcoded cut` | `Database search results · hardcoded compact` + per-agent cut pool | Real analysis compactors (`@compacts`); fallback det = logged when a compactor needs runtime enrichment |
| Agentic compaction | `{component} · agentic` + `Agentic cut` | `Database search results · agentic kept / delivered` | Evidence tools have no triage (delivered = det); menu-style calls keep their logged KEEP verdicts |
| Agent context | `{agent} context` fed by tools + relays + `{agent} delegated input` brief + dedup layer `ID-resolution merge · dedup layer (ID catalog, add-only)`; per-agent `dispatch args (tool calls, written)` → engine-boundary `dispatch args consumed at dispatch` sink | Same context + dedup nodes (hierarchy is never pooled), except chars contracts the pass-through `ID-resolution merge · dedup layer` into the agent context (the add-only catalog never cuts text; ids/pts keep the layer — duplicates exit there); delegated-input briefs + written args pooled into `Dispatch briefs — tool-call + agent-dispatch arguments`; WINDOW semantics: each agent's written args flow into its OWN context node and exit via its condensed-in-synthesis sink; engine-derived `L2 read args (reconstructed)` keep the engine sink | Context totals = Σ agent-visible results (§4) + own written args (general only); args = §4-paired run_history JSON (successful calls only) |
| Synthesis / envelope | `{agent} answers`, `{agent}-written envelope fields`, `Workflow fields from {agent} working memory`, `Hardcoded JSON scaffolding`, `Result envelope to {parent} (deliverable)` (per-run figures END here; the session figures' `{agent} envelope` relays on into Main), `Condensed away in {agent} synthesis` | `{agent} answers` → `{agent} envelope` (written fields + memory flows contracted into the envelope); `{agent} · condensed / cut content` pool | Envelope partitioned by provenance (answer / LLM-written / WM-assembled / scaffolding) |
| Nested agents | `Nested Q1 agent relay` decomposed into child answer/written/WM/scaffolding + the child's own L1/L2 machinery | Nested lane kept as its own separate sub-hierarchy (never merged with the parent's workers) | Child session parsed recursively |
| IDs metric | Novel-first attribution into contexts; `Duplicate IDs removed` at merge points | Same + per-agent `{agent} · duplicate / already-known IDs` pool; every node with block IDs carries `· k blocks · N pts` | Dedup marks implicit use/confirmation, not loss |

## Table 4 — Raw tool results & Main agent layer

| Abstraction level | Exhaustive diagrams | General diagrams | Basis / provenance |
|---|---|---|---|
| Raw tool results | `M Database search results · raw` staged chain for menu calls (`run_subagent_tool` unwrapped: e.g. Case I `search_blocks(limit=20)` native 167,646) + `Main tools · as-is` | `Database search results · raw` (Main lane) | Menu wrapper logs only post-pipeline size under the wrapper name → the wrapped tool is re-executed with its logged kwargs |
| Hardcoded compaction | `M … · hardcoded compact` + `Hardcoded cut` | `Database search results · hardcoded compact` + `Main · hardcoded compaction cut` pool | Real compactors (e.g. 20-row score table, 13,157) |
| Agentic compaction | `M … · agentic kept / delivered` (KEEP verdicts in Main's Subagent Summary) | Same pooled node | Logged verdict outputs (674/706 delivered) |
| Child relays | `{child} envelope` → `Main context` (+ `Relay wrapper`), `Children envelopes (parallel batch)` → `Parallel-batch relay` for batch-spawned children (Freeform) | Same hierarchy; wrappers pooled into Supporting context | Engine-structure-driven routing (1:1 relay vs `run_parallel_subagents`) |
| Main context → answer | `Main context` → `Main answer` + `Condensed away in Main synthesis`; `Main context volume not attributed` filler when inflow < total | Same, with `Main · condensed / cut content` pool | Main ctx = Σ Main-visible results; answer = answer text only |
| IDs metric | `Main tools` novel/dup edges into `Main context`; `Not cited in Main answer` | `Main raw tool-result IDs (re-exec., full set)` → `Main hardcoded-compact IDs` → `Main delivered tool IDs (post-triage)` → inherited context/dedup edges | Coverage chains guarantee every raw tool-result ID from every branch appears (verified: 0 missing in Cases I–IV) |

## Table 5 — Workflow compaction (`{ids,pts,blocks}_{pooled,agentic}_*`)

Built as a three-stage pipeline: `funnel_sources/id_evidence.py`
(Stage 1: per-call/session ID evidence; the future engine hook seam) →
`funnel_sources/id_phases.py` (Stage 2: plotting-agnostic Phase →
PhaseCluster → StageFunnel / NestedAgentStep records, one Phase per
agent activation in TRUE Main-log dispatch order) →
`abstraction_modules/id_compaction_view.py` (Stage 3: FlowGraph
assembly + the datapoint projection `pts_compaction_graph`).

| Element | Diagram nodes | Basis / provenance |
|---|---|---|
| Phase (chronology) | `Main tools [#k]`, `{child agent}` — in Main-log call order; batch-spawned children slot in at their `run_parallel_subagents` row; node label prefixes + edge order carry the time axis (drawn columns are the compaction stages, as in the general view) | Dispatch rows matched to child sessions (saved-child folder queues); relay-less children appended last |
| Tool sub-steps (per phase) | `L1 worker #k tools + relay`, `L1 dispatch #k (tool)` (analysis re-exec; §6 dispatch clusters mapped to LAUNCHED relays via §4 elapsed — validation rejects get no funnel), `L2 card reads for worker/dispatch #k (re-exec.)`, `L2 metadata card reads (re-exec.)` (L0 post-answer refinement only), `nested {tag} agent` (recursive sub-phase), consecutive same-tool groups `tool (×n)` | Worker rows precede their relay in the shared log (buffer attribution); analysis L1 = re-executed reconstructions grouped per §6 dispatch cluster; each worker's own DB-hydrated payload blocks claim its L2 card reads, leftovers pin to the dispatch that surfaced their literature, nested subtrees claim theirs first |
| Three tool-level layers | ALWAYS drawn per tool row: `· raw tool results` → `· hardcoded compact` → `· agentic kept / delivered`, even where a stage cut nothing; `{phase} · IDs cut by hardcoded compaction (never delivered)` and `{phase} · IDs cut by agentic triage / not carried into relay` right-edge sinks; L2 reads have no triage compactor — their agentic tier is the L2 evaluator agents: chain runs `· hardcoded compact` → `· evaluator kept / anchored` (det ids that surfaced in the run's payload/context evidence), unanchored ids exiting into `{phase} · IDs cut by L2 evaluators (metadata read, not anchored)`; `· IDs introduced by hardcoded rendering` stubs for qualified forms first spelled by the det text; ids cited only in a delivery enter from ONE `· transient memory (brief-carried + unlogged in-worker IDs)` block per subagent activation, INTO that worker's context merge — the triage stage only ever sees tool results (purple, `memory` links; rows outside a worker cluster keep the edge into their delivered node; nested agents get their own); unlogged rows stay one `· delivered (stages not logged)` node | Raw = logged natives ∪ re-executed sets (menu-wrapped, analysis det-compacted, L1 estimates, L2 reads); delivered = logged agentic/relay text + raw/det ids present in the child's `final_full_context.md` (previews truncate); L2 anchored = det ids in the archived worker payloads ∪ final context; delivery-only ids = brief echoes of the agent's add-only catalog or in-worker steps whose transient state left no rows |
| Merging layers | `· worker context` → `{phase} · ID-resolution merge · dedup layer (ID catalog + payload archive, add-only)` → `{phase} · agent context (merged IDs)` → `{phase} · envelope hand-off` (+ `envelope WM fields (written)`) → `Main context · merged IDs (add-only)`; each worker's L2 card reads feed that worker's context via the evaluator-anchored stage (L2 evaluators run inside the L1 worker), then worker contexts AND the agent's direct tool deliveries feed the same merge; at EVERY merge repeated ids displace into `{phase} · repeated IDs removed at merges (within phase)`; ids never carried into the envelope exit as `condensed` | Mirrors the engine: `working_memory_hooks.record_tool_result` is ONE step — verbatim payload archival + add-only ID-catalog merge — so archive and catalog are one node; nested agents render as full sub-phases (their own L1 worker funnels + attributed L2 card reads → worker context → nested agent context → relay incl. the child envelope the engine renders verbatim) feeding the parent's merge |
| Main context → answer | Re-delivered ids dedup as `re-confirmed known IDs`; `Main answer · IDs used for reasoning` = known ∩ cited-in-answer-text; rest → `Known IDs never used in the final answer` | Answers introduce no evidence: usage, not discovery |
| ID hierarchy | every set canonicalized before counting; every node carries `· k blocks · N pts` | Bare `PROP/RXNblock` → `GLOBlit::block` via same-set lit pairing, else case-unique candidate; a block and its qualified form are ONE knowledge item |
| pts variant | same graph re-weighted: edge ID sets → Σ datapoints of their qualified block IDs; 0-pt ids/edges/nodes drop out; labels de-ID'd (`data pts …`) | `qualified_block_pts` = exact block-CSV row counts |

## Design notes — the hard parts (brief)

- **Aggregation is meaningless for sets.** Chars pool additively; ID sets
  don't — consolidated "(n×)" funnels answered no question. Fix: keep the
  general family for chars, tell the IDs story chronologically (Table 5,
  the workflow-compaction family).
- **No-double-count is a global invariant, not a local one.** Every merge
  pass must re-derive `value = max(in, out)` and displace an ID's second
  arrival into an explicit dedup sink (repartition: the old carrier edge
  loses the id, the displaced occurrence exits). One-pass local fixes kept
  going stale after later passes unioned parallel edges.
- **ID hierarchy is the main double-count trap.** `PROPblock_7` and
  `GLOBlit_3::PROPblock_7` are the same knowledge item. Resolution order:
  qualified form in the same set → co-flow / lit pairing → case-unique
  candidate; irreducibly ambiguous bare ids stay bare (still one item),
  pts annotate only resolved blocks — never guess a number.
- **Chronology is implicit and asymmetric.** Order had to be reconstructed
  from: Main log row order; saved-child folder queues (dispatch matching);
  L1 worker rows preceding their own relay row in the SHARED parent log;
  batch children having no 1:1 relay row at all.
- **Unlogged stages force re-execution, not estimation.** Runs never
  logged L2 reads or analysis-dispatch natives; raw/hardcoded stages are
  re-executed through the real tools + real compactors from reconstructed
  args, each validated against a logged prompt-size bound. No ratios.
- **LLM-written text is not evidence.** Extracting IDs from answers or
  envelopes "discovers" written artifacts; the answer node counts usage
  (known ∩ cited) and envelope hand-offs contribute novel IDs only when
  genuinely first surfaced there (e.g. newly qualified pairs).
- **Balance vs honesty.** When inflow can't cover a context total, an
  explicit unattributed/filler node beats silently rescaling; when an ID
  branch dead-ends, it is merged along the real workflow with the
  displaced copy shown — never dropped.
