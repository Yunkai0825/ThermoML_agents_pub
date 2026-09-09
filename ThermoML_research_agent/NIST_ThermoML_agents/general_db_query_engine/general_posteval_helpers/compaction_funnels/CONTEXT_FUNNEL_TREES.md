# Context Funnel Trees — Full-Complexity Reference
**Engine-verified context (chars) and ID branches, compartmentalized from the lowest hardcoded
workers to the highest shell.** Every branch below was verified against engine source
(`general_db_query_engine`, query/analysis agent packages) and the four benchmark cases
(I: EtOH+H2O density · II: MeOH+ACN surface tension · III: MeOH+EtOH viscosity · IV: H2O+EG viscosity).

**Legend**
```
─▸   flow into next stage                 [CTX]  enters the calling agent's LLM context
├─   branch (all siblings possible)       [WM]   archived to working memory, bypasses context
⊘    volume removed / cut                 [ID]   identifier-set note (GLOB*/PROPblock/BLKsubsys)
⊕    volume introduced (newly written /   [DB]   deterministic database hydration (expansion)
     hydrated / scaffolding)              ⚠      error branch (text still enters context!)
⇄    dedup / add-only merge               §      measured exemplar (est.) = estimated
```

---

## 0 · Shell stack overview

```
USER PROMPT
└─▸ M · MAIN ORCHESTRATOR (shell 0, own session dir)
    ├─▸ M.menu   browse_subagent_tools / run_subagent_tool  (direct tools, menu batches)
    ├─▸ M.child  run_query_agent → QUERY AGENT L0   (shell 1, query_runs/run_N session)
    │            │
    │            └─▸ Q.L1 dispatch → L1 QUERY WORKER (shell 2, in-process, shared recorders)
    │                 ├─▸ T · search tools     (shell 3, hardcoded + agentic pipeline)
    │                 └─▸ L2 · leaf evaluators (shell 3, agents w/ own det-compacted tools)
    ├─▸ M.child  run_analysis_agent → ANALYSIS AGENT (shell 1, analysis_runs/run_N session)
    │            ├─▸ A.tools   discovery / evidence / fit / custom-block tools (shell 2, pipeline T)
    │            ├─▸ A.L1q     query_thermoml[_parallel] → L1 QUERY WORKER (shell 2→3, in-process)
    │            ├─▸ A.L1a     align_compositions → L1 COMPOSITION-ALIGNMENT WORKER (shell 2→3,
    │            │           own mixed analysis+query compactor catalog, in-process)
    │            └─▸ A.nested  run_query_agent[s_parallel] → FULL QUERY AGENT(S)
    │                        (shell 2, own session(s); e.g. A5/Q1)
    ├─▸ M.par    run_parallel_subagents → N children at once (philosophy elicitation,
    │            AUTO2STAGE internal batch compaction, merged tracking)
    └─▸ M.synth  Main synthesis → MAIN ANSWER (highest sink)
Every shell owns: LLM context [CTX] · working memory [WM] · ID catalog [ID] · envelope grammar (§6).
```

**Algebraic form** — the same stack as production rules, exhaustive to the tool level
(literal `ToolEntry` names; `∥` = parallel fan-out, `∘` = wrapped execution; enforced
edge-by-edge by `workflow_audits.hierarchy_audits`):

```
Main → { T_M , Q_i , A_i , ∥(Q ⊎ A) }
  T_M  = { run_query_agent→Q_i , run_analysis_agent→A_i , run_parallel_subagents→∥(Q⊎A) ,
           browse_subagent_tools , run_subagent_tool∘t (t ∈ T_L1 ∪ T_A^menu) , list_session_files }
         T_L1 = T_id∪T_blk∪T_sim∪T_rank ; T_A^menu = {inspect_block, get_pure_values}∪T_fit∪
         { query_system_summary , query_blocks , find_similar_compounds } (trio menu-only)
  mem  : MainWorkingMemory ⊕ prev-prompt carry-over          post: claim ∥ id-align → summary

Q_i  → { T_mem , L1_1 … L1_k }
  T_mem = { memory_read , memory_append_history , memory_add_result , memory_catalog_add ,
            memory_catalog_remove , memory_catalog_list , memory_compact , memory_reset }
          (working_memory.md [WM]; L1 payloads auto-archived — L1AutoSaver)

L1   → { T_id , T_blk , T_sim , T_rank , L2_comp , L2_meas , L2_ref , L2_prop }
  T_id   = { resolve_ids , resolve_compound_ids , resolve_property_ids ,
             resolve_measurement_ids , resolve_reference_ids , search_id_alignment }
  T_blk  = { search_blocks , block_search_adv , search_system_registry , search_system_summary }
  T_sim  = { search_similar_compounds }        T_rank = { screen_property_systems }
  post   : claim ∥ id-align → { construct_core_blocks_found , construct_core_id_updates } → payload (§5)

L2_comp → { search_comp_from_block , search_compound_dk , search_compound_indiv }
L2_meas → { search_meas_from_block , search_measurement_dk , search_measurement_indiv }
L2_ref  → { search_reference_from_block , search_references }
L2_prop → { search_prop_dk_from_block , search_property_dk }
  post   : id-align → construct_l2_{compounds,measurements,properties,reference}   (§4)

A_i  → { T_ev , T_fit , T_cust , query_thermoml[_parallel]→L1 (headless) ,
         align_compositions→L1_align , run_query_agent[s_parallel]→Q_j (nested FULL hierarchy) }
  T_ev   = { inspect_block , get_pure_values , list_session_files }
  T_fit  = { fit_block , fit_block_derived , fit_multi_system , compute_ideal_baseline ,
             predict_from_rk , propose_fitting_plan }
  T_cust = { register_custom_block }
  (resolve_compounds / resolve_properties / query_blocks / query_system_summary /
   find_similar_compounds = compactor-only sub-step keys, not agent-facing tools)
  mem    : AnalysisWorkingMemory (auto-extraction from inspect_block/get_pure_values/fit_block)

L1_align → { search_blocks , search_system_registry , resolve_compound_ids , inspect_block ,
             get_pure_values , fit_block , validate_dual_basis_block , register_estimated_bridge }

∀ shell, ∀ tool call t : raw(t) → det(t) → kept(t) → [CTX]   (compartment T, §1)
∀ agentic shell S      : answer(S) → claim(S) ∥ id-align(S) → construct_*(S) → JSON(S)
session memory   : Main WM ⊕ carry-over · Q working_memory.md (T_mem) · A WM        [WM]/[ID]
transient memory : downward briefs (purpose, instruction, id_catalog, context)
                   Main→{Q,A}→L1→L2 + relay-carried ids never logged at a tool stage
```

---

## 1 · Compartment T — single tool call (lowest hardcoded worker pipeline)

The universal per-call funnel (`AgentToolCatalog.wrap_tool` → `compact_and_call` →
`call_tool_subagent`). Applies to L1 search tools, analysis evidence tools, and any
compacted tool at any shell.

```
LLM tool call (purpose, tasks, args)
│
├─⚠ purpose/tasks missing ──▸ TOOL_ARGUMENT_REFINEMENT_REQUIRED text  [CTX]
├─⚠ batch pre-validation (SYNC_TOOL_GUIDANCE_CHECK)
│     ├─ blocked  ──▸ per-tool validation report REPLACES batch      [CTX]  (§ A4 steps 2,3,5)
│     ├─ ready(+autofilled params) ─▸ proceeds
│     └─ held-back-by-batch ─▸ report line                            [CTX]
│
└─ execute fn(**args) ──▸ result
   ├─⚠ unknown tool name ─▸ {"error": "Unknown tool: X"}                       [CTX]
   ├─ result: str
   │    ├─ _returns_subagent_answer ─▸ <subagent_answer> wrapper       [CTX]  (relay branch → §5/§6)
   │    └─ plain str  ─▸ as-is                                         [CTX]
   ├─⚠ result: non-dict/non-str ─▸ TypeError                           [CTX as error]
   └─ result: dict ─▸ validate_native_tool_result
        │            └─ side-log: record_references (DOIs/blocks/entities → stats only, no CTX) [ID]
        ├─ _returns_subagent_answer dict ─▸ wrapped as-is               [CTX]
        └─▸ NATIVE RAW  (serialized dict; never logged before 2026-08-05 fix)
            │           [ID] native id-set = superset of everything downstream
            │
            ─▸ LAYER 1 · HARDCODED COMPACTOR (deterministic, monotone on chars, ID-preserving)
            ├─ level=full            compactor_fn
            ├─ level=condense        condense_fn (strips data rows)
            ├─ level=ultra_condense  one-liner per block
            ├─ adaptive_condense     compactor self-tiers on size (search_blocks, block_search_adv,
            │                        search_system_registry)
            ├─⚠ compactor missing/raises ─▸ "Compactor for 'X' failed" TOOL_EXECUTION_ERROR [CTX]
            │                              (§ A4 step 4 get_pure_values)
            │   ⊘ Hardcoded compaction cut: measured ×1.6–5.9
            │     § measured: resolve_ids 389→241 · block_search_adv 9,483→1,752
            │     § search_blocks 50,954→8,653 (×5.9)
            │
            ─▸ DET COMPACT MD   [ID] ids(det) ≈ ids(native) (contract: IDs/values verbatim)
            │
            ─▸ LAYER 2 · AGENTIC KEEP/DISCARD TRIAGE (skip_subagent bypasses → det text [CTX])
            ├─⚠ oversized guard: det > SUBAGENT_CHAR_LIMIT
            │     └─▸ stats notice (keys/rows/sizes) [CTX] + OVERSIZED event; raw only in [WM side]
            ├─ error/0-result context block prepended to triage prompt (error-aware triage)
            ├─ KEEP    ─▸ extracted summary+tables                     [CTX]
            │            ⊘ Agentic triage cut  (§ Q3-L1#2: 6,736→2,618)
            │            ⊕ triage may EXPAND small inputs (§ A5: 574→787; resolve 241→319)
            │            [ID] ids(kept) ⊆ ids(det); survivors cited verbatim
            ├─ DISCARD ─▸ ⚠ stub "result discarded" + reason + refinement hint [CTX]
            │            ⊘ all content; [ID] stub may still cite a few IDs
            │            (§ A4 dispatch-1 block_search_adv → 865-char stub)
            ├─ malformed reply ─▸ 1 bounded retry ─▸ still malformed ⚠ RuntimeError
            └─⚠ subagent call fails ─▸ "Mandatory agentic compaction failed"  [CTX as error]
```

---

## 2 · Compartment B — ordered-batch / stage compaction (any shell's react loop)

```
N>1 tools in one ordered batch ─▸ parts labeled "### tool\n…" → combined_result
├─ batch_summary hook claims batch (menu batches at Main) ─▸ hook summary        [CTX]
├─ combined ≤ STAGE_COMPACT_BUDGET ─▸ combined as-is                             [CTX]
└─ combined >  budget ─▸ STAGE COMPACTION
      ├─▸ summary table (before→after; § Q2-L1 batch of 4: 7,939→864, −89%)     [CTX]
      ├─⊘ full parts → _batch_cache (in-memory, not persisted)
      └─⊕ inspect_batch_result(tool_number) temp tool registered
            └─ agent re-reads a cached part ─▸ RE-EXPANSION branch               [CTX]
WAIT BARRIER (<wait/> in an ordered batch)
      └─▸ ⊕ "[WAIT BARRIER COMPLETE] N tool(s) finished … K deferred call(s)
           were discarded" note appended to results                             [CTX]
NOTE  stage records log ONLY post-per-tool-pipeline sizes — never native raws.
```

---

## 3 · Compartment X — agent-loop context maintenance (any shell)

```
📦 CONTEXT COMPACTION  trigger: interval=K or size threshold
└─▸ agent-guided compaction proposal (reminder → guidance response → parse → execute)
    ├─ compacted          ─▸ context rewritten (before→after + receipt)   [CTX shrinks]
    ├─ skipped_by_agent   ─▸ no-op (§ A4: 16,064→16,064 ×3 events)
    ├─ skipped_by_selector─▸ no-op
    └─⚠ error             ─▸ logged, context unchanged
WORKING-MEMORY RENDER (each turn; SYNC_WORKING_MEMORY_RENDER / SYNC_PRIOR_CONTEXT_APPEND)
└─⊕ [WM → CTX] re-injection: ID catalog + prior context + memory results rendered
     into the prompt — the channel by which the catalog reaches every LLM turn
TIME BUDGET (TimeBudgetTracker; progressive thresholds)
├─⊕ "[TIME WARNING …]" user-messages appended to conversation memory        [CTX]
└─⚠ hard-stop ─▸ forced final-answer path (WARNING/HARD_STOP final-answer anchors)
LOOP NUDGES (react loop)
├─⊕ "[EMPTY WAIT] you emitted <wait/> but no tool calls" (stuck-loop detector,
│    escalates until _MAX_EMPTY_WAITS)                                        [CTX]
└─⊕ no-tool-calls + no-<answer> nudge (max 2) — demands explicit final answer [CTX]
[ID] compaction may drop cited IDs from context; ID catalog [WM] is NOT affected (add-only).
```

---

## 4 · Compartment L2 — leaf evaluators (lowest agentic worker)

```
L1 calls L2_comp_eval / L2_meas_eval / L2_ref_eval / L2_prop_eval (purpose, instruction,
                                                     context, id_catalog)
└─▸ L2 agent turn (own small system prompt; § A4 §6 systems 298–1,356)
    ├─▸ L2's OWN TOOL SET (block-centric + basic search wired from card_db_search_tools)
    │     ├─ det-compacted tools: search_meas_from_block · search_measurement_dk ·
    │     │   search_measurement_indiv (compactor_fn only — Layer 1 without Layer 2:
    │     │   NO agentic KEEP/DISCARD exists at this layer)
    │     └─ skip-both tools → results enter L2 context as-is
    ├─ L2 LLM writes structured verdict JSON
    └─▸ returns as <subagent_answer> — skip_compactor + skip_subagent
        ─▸ relayed AS-IS into L1 context                                  [CTX(L1)]
        [ID] L2 evidence cites block-qualified IDs (GLOBlit_N::PROPblock_M)
        (§ A5/Q1 payload embedded 6 L2 blocks · 2,357–2,434 chars each)
```

---

## 5 · Compartment L1 — query worker shell (tools → context → synthesis → strict envelope)

```
INPUT [CTX(L1) seed]: ## Purpose + ## Instruction + ## ID Catalog (from parent WM) + ## Prior Context
│
├─▸ L1 TOOL CALLS  (each = Compartment T; batches = Compartment B; periodic X)
│     ├─ id_resolution: resolve_ids / resolve_compound_ids / resolve_property_ids /
│     │                 resolve_measurement_ids / resolve_reference_ids / search_id_alignment
│     ├─ block_search:  search_blocks / block_search_adv / search_system_registry /
│     │                 search_system_summary          (adaptive tiers)
│     ├─ similarity:    search_similar_compounds
│     ├─ ranking:       screen_property_systems        (det + agentic, IDs verbatim contract)
│     └─ L2 dispatch:   Compartment L2 answers as-is   [CTX(L1)]
│     (memory_* tools live at Query L0, NOT here — see §8)
│     § measured worker context intake: Q3-L1#1 raw 14,065→det 3,853→kept 2,996
│     § estimated (analysis-driven):    A4-L1#1 raw ~17,683→det ~3,710→kept 3,273 (est.)
│
├─▸ L1 SYNTHESIS (answer-only system prompt)
│     ├─ LLM answer written FROM kept context      ⊘ condensed away   ⊕ newly written
│     └─ [ID] answer cites subset of context IDs
│
├─▸ POST-ANSWER PIPELINE (evaluate_and_assemble_return; anchored stages:
│   ANSWER_RECEIVED → EVALUATION → SUMMARY_TOOL → L2_FIELD_TOOL (+L2_FIELD_REFINEMENT
│   retry loop) → CORE_ID_TOOLS (+CORE_ID_REFINEMENT) → SUBMISSION_REVIEW → ASSEMBLY
│   → ⚠ VALIDATION_FAILED branch)
│     ├─ claim agent  → core_claims / summary / follow_up_suggestions / confidence
│     │   (tool-free; reads full tool history + task context; § A4 §6 prompts 12,540 / 21,866)
│     └─ ID/metadata agent → MINIMAL CORE ANCHORS ONLY
│         {lit_num_id, block_number, BLKsubsys_id, system_type, comp/prop_num_ids, description}
│
├─▸ CORE-ID REFINEMENT + DB HYDRATION (refine_and_enrich_l1_core_ids)
│     ├─ _validate_core_block: checksum anchors vs authoritative card DB
│     │    ├─ pass ─▸ construct_core_blocks_found [DB]⊕ hydrates FULL metadata per block:
│     │    │        doi, lit_id, block_type, n_datapoints, compounds, solvents, constraints,
│     │    │        variables, properties, phases, reaction, participants, notes, declared_*,
│     │    │        parent_n_datapoints, subsystem_* — ~2.5–3k chars/block, PURE EXPANSION
│     │    │        (never passed through any LLM context)
│     │    └─⚠ mismatch ─▸ CoreIDValidationError → refinement retry (≤2 cycles)
│     │         └─⚠ exhausted ─▸ TOOL_EXECUTION_ERROR into PARENT context
│     │             (§ A4 dispatch 2: "checksum mismatch (GLOBlit_267, PROPblock_2):
│     │              comp_num_ids expected ['GLOBcomp_4'], received ['GLOBcomp_2']")
│     ├─ construct_core_id_updates [DB]⊕ registry hydration {global_id, registry_id, name}
│     │    └─⚠ ID absent from canonical registry ─▸ CoreIDValidationError
│     └─ duplicate block identity ─▸ ⚠ error                                  [ID ⇄ strict]
│
└─▸ STRICT ENVELOPE (validate_l1_query_output → to_json)
      { answer ⊕LLM · core_claims/summary/follow_ups/confidence ⊕LLM ·
        core_blocks_found [DB]⊕ · core_id_updates [DB]⊕ · status ⊕workflow }
      § A4 relay anatomy (47,195 total): LLM-written ≈7,798 (17%) ·
        DB-hydrated blocks ≈25,548 · hardcoded rendering ≈12,984 (83% bulk)
```

---

## 6 · Compartment R — relay & dedup layer (L1 → parent; the ID-resolution merge)

```
L1 envelope JSON ─▸ <subagent_answer> marker (skip_compactor + skip_subagent)
│
├─▸ PARENT CONTEXT: rendered AS-IS                                        [CTX(parent)]
│     ⊕ hardcoded relay rendering (§ Q3#1: +2,176)
│     (contamination: DB-hydrated bulk re-enters a context that could re-fetch by ID)
│
└─▸ record_tool_result hooks (working_memory_hooks) — runs BEFORE the parent LLM sees it
      ├─ per-block summaries  ─▸ [WM] archive
      ├─ FULL PAYLOAD          ─▸ [WM] archive, bypasses context
      │    └─ payload > relay ─▸ ⊘ "retained only in working memory"
      │        (§ A5/Q1: payload 26,439 vs relay 417 → 26,022 WM-only)
      ├─ core_id_updates ⇄ ID CATALOG MERGE (ADD-ONLY dedup layer)
      │    ├─ novel IDs   ─▸ catalog grows                                [ID ⊕]
      │    └─ duplicates  ─▸ collapsed                                    [ID ⊘]
      │        (§ A4: 87 relayed occurrences → 51 unique, 36 dups removed)
      └─ chars PASS THROUGH the merge uncut (dedup acts on IDs, not text)
```

---

## 7 · Compartment A — analysis agent shell

```
INPUT [CTX(A) seed]: delegated brief from Main WM (§ A4: 762 · A5: 860 · A6: 998)
│
├─▸ DISCOVERY TOOLS (direct DB search WITHOUT L1! Compartment T): search_blocks ·
│     search_system_registry · resolve_compound_ids · query_system_summary ·
│     query_blocks · find_similar_compounds · resolve_compounds · resolve_properties
├─▸ EVIDENCE TOOLS: inspect_block · get_pure_values (det compactor; ⚠ compactor-failure
│     branch § A4 step 4) · custom-block suite: register_custom_block ·
│     validate_dual_basis_block · register_estimated_bridge
├─▸ RESULT TOOLS: fit_block / fit_block_derived / fit_multi_system (RK fits →
│     [WM fit_results] + short text [CTX]) · compute_ideal_baseline · predict_from_rk ·
│     propose_fitting_plan · list_session_files
│
├─▸ L1 QUERY DELEGATION  query_thermoml / query_thermoml_parallel
│     ├─⚠ PRE-DISPATCH VALIDATION REJECT (no L1 ever launches, instant)
│     │    └─ "queries[0].id_catalog[0] must contain exactly […]" error   [CTX]
│     │       (§ A4 steps 7–8: 184 + 323 chars, 0.0/0.4 s)
│     ├─ LAUNCH ─▸ Compartment L1 (in-process; shares recorders)
│     │    ├─ success ─▸ Compartment R                                    [CTX + WM + ID⇄]
│     │    └─⚠ refinement exhausted ─▸ error rump only                    [CTX]
│     │       (§ A4 dispatch 2: 251 s of L1 work → 358-char error;
│     │        est. raw ~32,392 → kept 1,346 → 358 relayed, 988 lost)
│     └─ parallel variant: ThreadPoolExecutor max_workers=4; per-label envelopes
│          {"label", "result"} | {"label", "error"} merge through R
│
├─▸ L1 COMPOSITION-ALIGNMENT WORKER  align_compositions (SECOND analysis L1 type)
│     └─ own agent_turn on AnalysisClient with a mixed analysis+query compactor
│        catalog (search/inspect tools, two-stage compaction inside), deterministic
│        assembler after the turn → structured alignment relay              [CTX]
│
├─▸ NESTED SAVED AGENTS  run_query_agent / run_query_agents_parallel
│     └─ FULL QUERY AGENT(S) (Compartment Q, own session each)
│        └─ child envelope relayed as-is + wrapper (§ A5 ← Q1: env 8,302 + wrap 1,318)
│
├─▸ Compartments B & X as they trigger
│
└─▸ SYNTHESIS + ENVELOPE (§ same grammar every shell)
      ├─ orange synthesis: answer + written fields FROM context
      │    ⊘ condensed away (§ A4: 47,037 of 52,195) · ⊕ newly written beyond context
      ├─ envelope = answer(verbatim) + agent-written(core_claims/confidence/follow_ups/summary)
      │            + [WM] workflow fields (sources / id_catalog_snapshot / fit_results / status
      │            / files) + ⊕ hardcoded JSON scaffolding
      │    (§ A4 env 6,892 · A5 9,471 · A6 5,500 · A1 8,229)
      └─▸ Main context: envelope + ⊕ relay wrapper (§ A5 wrap 5,331 · A6 wrap 3,668)
```

---

## 8 · Compartment Q — query agent L0 shell

```
INPUT [CTX(Q) seed]: delegated brief from Main
├─▸ L0 MEMORY TOOL SUITE (skip both stages; tiny "OK" returns [CTX], entries → [WM]):
│     memory_read · memory_append_history · memory_add_result · memory_catalog_add /
│     _remove / _list · memory_compact · memory_reset   (§ Q2: memory_catalog_add ×3)
├─▸ L1_query dispatches (Compartment L1; in-process, shared history — L1 steps interleave)
│     └─ relay + rendering (§ Q3: #1 9,940 = payload 7,764 + rendering 2,176; #2 8,870)
├─▸ Compartments B, X as they trigger
└─▸ SYNTHESIS + ENVELOPE (same grammar)
      § Q3: context 24,424 → answers 2,552 + written 1,594 (⊘ 20,278 condensed) → env 6,147
      § Q2: env 3,986 = answer 1,235 + written 1,006 + wm 1,254 + scaffold 491
```

---

## 9 · Compartment N — nested saved-agent relay (agent inside agent)

```
ANALYSIS agent calls run_query_agent (or run_query_agents_parallel for N at once)
└─▸ child QUERY AGENT(S) with OWN session dir (query_runs/run_1 under parent's dir)
    ├─ full Compartment Q tree recurses (L1 → T/L2 → R …)
    └─▸ child envelope ─▸ parent context decomposed as:
        answer (verbatim relay) + child-written fields + child-WM workflow fields
        + ⊕ scaffolding + ⊕ relay wrapper
        (§ A5/Q1 → A5: 9,620 = env 8,302 + wrap 1,318; A5 ctx 17,122)
        [ID] child catalog snapshot ⇄ parent catalog (add-only again)
```

---

## 10 · Compartment M — Main orchestrator (highest shell)

```
USER PROMPT [CTX(M) seed]
├─▸ MENU TOOLS: browse_subagent_tools (catalog listing ⊕ menu text, § I: 2,882) ·
│     run_subagent_tool (menu-batch summary hook — Compartment B variant)
├─▸ CHILD DELEGATIONS  run_query_agent / run_analysis_agent (sequential): each spawns
│     shell-1 session (Compartment A/Q)
│     └─ child envelope + ⊕ relay wrapper ─▸ Main context
│        § I:  Main ctx 7,823 = Q2 env 3,986 + wrap 955 + menu 2,882
│        § II: Main ctx 19,213 ← Q3 env 6,147 + A1 env 8,229 + wrappers + own tools 1,612
│        § IV: Main ctx 28,597 = A5 env 9,471 + wrap 5,331 + A6 env 5,500 + wrap 3,668 + own 4,627
├─▸ PARALLEL DELEGATION  run_parallel_subagents (N children at once)
│     ├─ philosophy elicitation (need/targets/philosophy; ⚠ PHILOSOPHY_RETRY rounds)
│     ├─ children run → combined payload
│     ├─ AUTO2STAGE: payload > limit ─▸ internal parallel-batch compaction (det + agentic
│     │   batch compactor; oversized events logged)                        [CTX]
│     └─ per-child session tracking merged into Main's records
├─▸ Compartment X (Main-level 📦 compactions)
└─▸ MAIN SYNTHESIS ─▸ MAIN ANSWER (user-facing sink)
      ⊘ condensed away in Main synthesis (§ II: 14,716 · IV: 24,902)
      § answers: I n/a · II 4,497 · III 5,172 · IV 3,695
```

---

## 11 · ID-branch master tree (origins → transforms → sinks)

```
ID ORIGINS ⊕
├─ native tool results (registry rows, block tables)            → shell 3
├─ analysis discovery tools (direct search, no L1)              → shell 2
├─ memory_catalog_add / memory_add_result (agent-registered
│  catalog entries at query L0; § Q2 ×3 pre-dispatch)           → [WM catalog]
├─ DB hydration anchors → full ID families per block [DB]       → L1 envelope
├─ registry hydration of catalog updates [DB]                   → L1 envelope
├─ LLM-written text citing IDs (answers/claims at every shell)
├─ delegated briefs + ID-catalog snapshots passed DOWN (parent → child seed)
└─ L2 evaluator verdicts (block-qualified GLOBlit_N::PROPblock_M)

ID TRANSFORMS
├─ T: det compactor  ids(det) ≈ ids(native)   (measured: near-lossless)
├─ T: agentic triage ids(kept) ⊆ ids(det)     ⊘ dropped with cut rows; DISCARD ⊘ nearly all
├─ L1 synthesis      answer/claims cite subsets; ⊕ may introduce catalog-known IDs
├─ checksum gate     ⚠ mispaired anchors REJECTED (never enter parent) — quality filter
├─ R: catalog merge  ⇄ ADD-ONLY: novel ⊕ · duplicates ⊘ (§ A4: 51 unique / 36 dups)
├─ envelope          answer-IDs ∪ written-IDs ∪ WM snapshot-IDs (∪ = containment-true)
├─ X: context compaction may ⊘ cited IDs from CTX; catalog [WM] retains them
└─ parent synthesis  answer cites final subset; rest ⊘ "not cited in answer"

ID SINKS
├─ Main answer citations (user-facing)
├─ ID catalog / _working_memory.md (authoritative, add-only, session-persistent)
├─ result.md envelopes (id_catalog_snapshot)
└─ reference_stats.md §2/§3 (side-logged aggregates, non-context)
```

---

## 12 · Where each node is evidenced (per session dir)

| Artifact | Funnel nodes it evidences |
|---|---|
| `run_history.md` | T verdicts (Subagent Summary; + Input Chars post-fix), B stage records, X events, ⚠ errors, **Tool Compaction Pipeline table (native→det→agentic, post-fix)** |
| `reference_stats.md` §1/§6 | per-tier LLM calls; triage calls (system 1,900–2,300) → det-size estimation; L1 dispatch clusters |
| `reference_stats.md` §2–§4 | ID side-logs; per-call entered-context sizes (post-pipeline) |
| `final_full_context.md` | [CTX] ground truth: relays, wrappers, rendering, seed |
| `result.md` | envelope grammar decomposition (answer/written/WM/scaffold) |
| `_working_memory.md` | [WM] archives, ID catalog, fit results |
| `reasoning_tokens_stripped.md` | synthesis reasoning blocks (triage outputs only post-fix) |
| audit TSVs (`origin_*.tsv`) | every edge above with values; `origin_l1_internal_costs.tsv` = measured + estimated within-L1 stages |

**Known blind spots in the four benchmark runs (all fixed in engine 2026-08-05, apply to future runs):**
native raw sizes (estimated via measured compactor ratios) · det sizes inside analysis-driven L1
(estimated via triage prompts − 250) · triage output text for analysis-driven L1 (kept-stage IDs
unrecoverable) · L1 steps in analysis sessions (recorder routing).
