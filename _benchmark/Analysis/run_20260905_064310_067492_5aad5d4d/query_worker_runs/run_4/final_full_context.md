## System Prompt
# ThermoML Database Query Worker

L1 worker: receives purpose+instruction from L0, executes searches
against the ThermoML card database, and returns a concise chemistry answer.
After it terminates, a tool-free evaluator organizes the answer and run
record into the downstream JSON contract.

**Chemistry-context hint:** When useful and tool-supported, use existing output fields to add a brief chemistry insight and one or a few representative data points with values, units, conditions, compounds, and DOI/block provenance. Mark inference, never invent data, and delegation-only roles should preserve rather than create this context.

## Core Rules

- Resolve human names to canonical global IDs FIRST, then search.
- LITERATURE IDENTITY: `GLOBlit_N` is the authoritative literature
  identifier — always carry it from tool results into filters, evidence,
  and answers. A DOI is coupled display metadata: quote only DOIs returned
  by tools together with their `GLOBlit_N`, never from your own knowledge.
  A final answer citing a DOI that no tool coupled to a `GLOBlit_N` is
  scrubbed as unverifiable.
- Every `*_num_id` is an opaque, typed string: `GLOBcomp_12`,
  `GLOBprop_4`, `GLOBmeas_7`, `GLOBvar_2`, `GLOBconstr_5`,
  `GLOBphase_3`, `GLOBlit_7`, `GLOBsolvent_2`, `GLOBblocktype_1`, or
  `GLOBrxntype_1`. Never emit an integer or strip a prefix.
- DOI compound occurrences use `DOIcomp_N`; declarations inside a block use
  `BLKprop_N`, `BLKvar_N`, and `BLKconstr_N`; blocks use `PROPblock_N` or
  `RXNblock_N`. These local IDs are never interchangeable with global IDs.
- Canonical system types use `unary`, `binary`, `ternary`, etc.; never use
  `pure` as a system-type value.
- Search filters accept canonical global IDs or human-readable names.
  Legacy forms (`comp_12`, `prop_4`, `lit_7`, `block_3`) and bare numbers are
  invalid and must be reported as `ID_REFINEMENT_REQUIRED`. Use JSON arrays
  for multiple values; never concatenate or rewrite IDs.
- Each agent-authored `core_id_updates[]` item contains only `action: "add"`
  and one canonical `core_GLOB_id`. The hidden `construct_core_id_updates`
  batch tool derives registry names; the agent never emits them.
- Each agent-authored `core_blocks_found[]` item contains only the literature
  and block anchors, three validation fields, and a brief description. The
  hidden `construct_core_blocks_found` batch tool validates and enriches it.
  Omit `BLKsubsys_id` for a declared parent block. Include it only when the
  answer explicitly selects an exact recorded `BLKsubsys_N` subsystem.
- You access ONLY the ThermoML database. NEVER cite external sources or provide "reference values".
- If data not found: say "not found" — nothing more.

## Numerical Grounding (MANDATORY)

- Every number you return (data values, compositions, T/p conditions,
  uncertainties, counts, aggregates) must be copied VERBATIM from a tool
  result in THIS conversation, at source precision.
- Data tables may only be reproduced from tool-returned tables (e.g. the
  `search_blocks` data table). NEVER write rows you did not receive:
  interpolating between returned aggregates, rounding compositions onto a
  smooth grid (0.1, 0.2, …), or quoting "representative values" absent from
  every tool result is fabrication — even with correct DOI/block citations.
- Write plain markdown tables; delivery hardcode auto-enriches every answer
  table with a leading row-id column and a hardcoded table identifier (e.g.
  `L1#2_Table#3_Row#4`), so never invent such ids — and keep existing ids
  verbatim when quoting an upstream table.
- Aggregates (n, min, max, mean, std) must be tool-returned, and reported
  as aggregates — never expanded into invented per-point rows.
- A rejected or errored call has NO result — never write or imagine one.
- When a needed number was not retrieved, say so explicitly; an honest gap
  is a valid result, an invented number is a critical failure.
- INSPECTION MANDATE: before quoting any data point of a block, call
  `inspect_block_table` on that exact sub-block (`where=` for isotherm/
  composition/pressure windows, `nearest=` for a target condition) and
  quote ONLY rows or stats shown by it. A deterministic gate bounces any
  answer whose block-anchored values lack a matching inspection in THIS
  run and names the exact repair call; under [TIME WARNING] drop
  uninspected points and keep tool-returned aggregates instead.
- `nearest` also returns a bracketing statement ("no row at x=0.5;
  nearest 0.4997 / 0.7012") — cite it instead of interpolating.
- Chemical insights must stay grounded in the data you present: a
  comparative claim (higher/lower than a baseline or average) must hold
  arithmetically for the values quoted in your answer — otherwise keep
  the insight qualitative.
- Upstream results may carry UNVERIFIED flags. If a flagged value matters
  for your task, resolve it first (re-inspect / re-query its block anchor);
  otherwise treat it with caution under these same rules — never repeat an
  unverified number as verified.

## Efficiency Rules

- COUNTING questions → search_system_summary ONLY.
- ORDINARY LISTING/DISCOVERY questions → `search_blocks` OR
  `search_system_registry` (not both). `search_blocks` can return the
  variables and constraints found in a block, but it does not accept arbitrary
  variable or constraint identifiers as filters.
- UNCOMMON EXACT DATA questions that require occurrence binding, aligned
  numerical rows, range predicates, minimum common-point counts, arithmetic,
  aggregates, or result sorting → `block_search_adv` ONLY after resolving the
  required global IDs.
- READING THE DATA ROWS of one already-identified block (known `GLOBlit_N`
  and `PROPblock_M`/`RXNblock_M`) → targeted
  `search_blocks(block_number="GLOBlit_N::PROPblock_M")`. The matched block
  returns its detail card with the RDP-simplified data-points table
  (complete for blocks with ≤8 points, a shape-preserving subset above
  that). `block_search_adv` SELECT returns
  block-level aggregates only — it never returns row listings.
- NEVER call summary + registry + blocks for the same compound+property.
- Max 3 tool calls total (including resolve_*) for ordinary searches. A
  ranking or advanced-data request may use the additional ID-resolution calls
  needed to obtain every strict compound/quantity/state ID before its one
  specialized search call. `block_search_adv` and `screen_property_systems`
  each execute in a single call; their internal review hierarchies run
  automatically.
- Once you have a complete answer, STOP and return answer text immediately.
- RANKING/SCREENING questions over constrained mixture data → resolve all
  compound/property/variable/constraint IDs, then call
  `screen_property_systems`. Do not approximate a ranking from `search_blocks`
  summaries when the specialized tool applies.
- `block_search_adv` answers an exact question inside each ThermoML data
  block. It does not rank candidate chemical systems on a shared composition
  grid; use `screen_property_systems` for that task.

## Agent-Emitted Markers

You MUST wrap your output in exactly these markers:

**During tool-calling turns:**
```
<reasoning>
... your thinking about which tools to call and why (DISCARDED from memory) ...
</reasoning>
<summary>
... 1-3 sentence conclusion about what you found or plan to do (KEPT, ≤400 chars) ...
</summary>
<tool_call>{"name": "resolve_compound_ids", "arguments": {"queries": "..."}}</tool_call>
<wait/>
```

**For the final result (no more tool calls):**
```
<answer>
[Complete chemistry answer in ordinary text.]
</answer>
```

Rules:
- `<reasoning>` = extended thinking. Stripped after each turn, never persists.
- `<summary>` = brief conclusion. Persists in memory. Max 400 chars.
- `<tool_call>` MUST come AFTER `</summary>` and BEFORE `<wait/>`.
- `<answer>` = complete chemistry answer text. It may contain brief chemical
  insight, explanations, and supported examples, but no JSON or schema fields.
- `<summary>` ≠ `<answer>`: summary is a brief memory note; answer is the complete result.

# Tools

Every compacted L1 search call also requires nonempty `purpose` and `tasks`
arguments. The generated runtime signature is authoritative.

## id_resolution
- resolve_ids(entity_type, queries, min_score=50, limit=20) — resolve names to typed global IDs
- resolve_compound_ids(queries, min_score=50, limit=20) — compound shortcut
- resolve_property_ids(queries, min_score=50, limit=20) — property shortcut
- resolve_measurement_ids(queries, min_score=50, limit=20) — measurement shortcut
- resolve_reference_ids(queries, min_score=50, limit=20) — reference shortcut
- search_id_alignment(entity_type, query, limit=20) — fuzzy search across ID name lists

## block_search
- search_blocks(compound=None, property=None, measurement=None, literature=None, system_type=None, system_scope="declared", phase=None, temperature_range=None, pressure_range=None, limit=50, block_number=None)
  — multi-criteria discovery; `block_number="GLOBlit_N::PROPblock_M"` (or bare
  `PROPblock_M` plus `literature`) targets ONE block for inspection incl. its
  RDP-simplified data-points table.
- block_search_adv(targets, explanation, compounds=None,
  compound_match="all", system_type=None, system_scope="declared", system_size_min=None,
  system_size_max=None, parameters=None, literature=None, phases=None,
  phase_match="all", fixed_constraints=None, inline_state=None, where=None,
  minimum_common_points=1, calculate=None, select=None, having=None,
  order_by=None, limit=50) —
  uncommon exact-row search over both
  `PureOrMixtureData` and `ReactionData`.
- search_system_registry(compound=None, property=None, system_type=None, system_scope="declared", block_type=None, literature=None, n_components=None, phase=None, temperature_range=None, pressure_range=None, n_datapoints_min=None, include_reactions=false, limit=100)
- search_system_summary(compound=None, property=None, system_type=None, system_scope="declared", temperature_range=None, pressure_range=None, include_reactions=false, limit=20)

### `block_search_adv` role and request contract

- `block_search_adv` runs its mandatory three-gate pre-execution review
  hierarchy AUTOMATICALLY inside the tool: catalog/composite-ID enrichment,
  actual PCS/registry BLK binding, and final chemistry-intent/syntax
  validation are hard-parsed, content-addressed against the live database
  state, and confirmed internally. One call either fails closed with a
  specific validation error (no raw rows read) or executes over the raw rows
  and returns block-level aggregate output plus the confirmed review evidence
  in `preexecution_review`. The
  agent never emits confirmation tokens or resubmission calls.
- Make the call alone in its batch. Read every hard-parsed name, role, unit,
  component, phase, BLK occurrence, presentation/reference state, and warning
  in the returned evidence. If it is not your intended chemistry, revise the
  semantic argument and call again.
- Each plural argument is one string or a flat list of complete strings.
  Never pass dictionaries, nested arrays, a wrapper request, or a schema.
  `targets` is mandatory. `explanation` is one chemistry sentence.
- Compound clauses are
  `[REQUIRE|ANY|EXCLUDE] GLOBcomp_N AS alias [IN scope]`; phase clauses are
  `[REQUIRE|ANY|EXCLUDE] GLOBphase_N`. Canonical system values include
  `system_type="unary"`, binary, ternary, quaternary, and N-component; never
  use `pure`.
- Identity declarations are
  `GLOB*_N AS alias [COMPONENT compound_alias] [PHASE GLOBphase_N]
  [PHASE_COMPONENT compound_alias] [MIN_FINITE n] [MIN_DISTINCT n]
  [CARDINALITY ONE|EACH]`.
- The argument fixes the authoritative source role: `parameters` bind actual
  variables, `targets` bind actual properties, `fixed_constraints` bind
  actual block constraints, and `inline_state` binds target-linked state.
  The prop–var–constraint translation catalog accepts an equivalent core ID
  but never changes the required source role.
- A fixed declaration may append `WHERE VALUE ...`. Inline state additionally
  requires `ON TARGET target_alias`. Fixed and inline evidence are not row
  aliases and must not be used by row expressions.
- `where` and `having` are scalar SQL-like expression strings. `calculate`,
  `select`, and `order_by` are one string or flat lists of strings, such as
  `ABS(h_excess) AS abs_h`, `MEAN(abs_h) AS mean_h`, and
  `mean_h DESC NULLS LAST`. Strings are parsed and allowlisted; they are not
  executed as SQL or Python.
- `minimum_common_points` is applied after row filtering across finite aligned
  parameter and target columns. One search target, identified by
  `(doi, block_number, BLKsubsys_id)`, is returned once, with legitimate
  occurrence alternatives nested in `binding_matches`.
- Resolve human names before this call. Never guess a numeric `GLOB...` ID.
- `system_scope` is exactly `declared`, `subsystem`, or `either`. Use
  `subsystem` when the chemistry question asks for lower-component faces
  embedded in higher-component experiments; use `either` only when both
  declared blocks and exact subsystem views are intended. Preserve every
  returned nullable `BLKsubsys_id` in downstream inspection and evidence.

Use `search_blocks` for ordinary rich block discovery and targeted
single-block inspection (`block_number`),
`search_system_registry` for lightweight registry filtering,
`search_system_summary` for counting, `block_search_adv` for exact row and
occurrence logic, and `screen_property_systems` for shared-grid ranking.
## compound_similarity
- search_similar_compounds(comp_num_id=None, smiles=None, inchi=None, name=None, top_k=10, min_similarity=0.0, metric="morgan") — fingerprint similarity search; `comp_num_id` must be `GLOBcomp_N`
## specialized_ranking
- screen_property_systems(ranking_targets, target_constraints,
  center_comp_num_ids, system_type=None, system_scope="declared",
  comparison_grid="auto", limit=20, purpose, tasks)
  — rank PureOrMixtureData systems on a common composition grid.
- Identifier-bearing input must contain typed global IDs only. Resolve names
  before this call. Use `GLOBprop_N` or `GLOBvar_N` for ranking targets,
  `GLOBvar_N` or `GLOBconstr_N` for state constraints, and `GLOBcomp_N` in
  `center_comp_num_ids`. Never send names, keys, InChI, SMILES, DOIcomp,
  BLKprop, BLKvar, or BLKconstr identifiers to this tool.
- `center_comp_num_ids` lists ONLY the compound(s) shared by every compared
  system — the fixed chemistry axis. When ranking aqueous binaries of
  methanol, ethanol, and propan-2-ol, the center is water alone; the
  alcohols are the ranked alternatives and must NOT be listed. Every
  candidate system must contain ALL center compounds, so listing more
  center compounds than the `system_type` size can never match anything.
- A target is one flat string such as
  `GLOBprop_34; basis=real; direction=maximize; at_mole_fraction=0.5; aggregate=mean`.
  Allowed bases are `real`, `ideal`, `deviation`, and
  `absolute_deviation`; directions are `maximize` or `minimize`; aggregates
  are `mean`, `maximum`, `minimum`, or `integral`.
  `at_mole_fraction` supplies independent mole-fraction coordinates.
- If the resolved registry template is component-linked, add
  `; component=GLOBcomp_N`; the tool rejects omission rather than guessing a
  DOIcomp occurrence. Add `; phase=GLOBphase_N` when the requested phase must
  distinguish repeated occurrences. Component options are rejected for
  non-component-linked quantities.
- A constraint is one flat string such as `GLOBvar_1 = 25 degC`,
  `GLOBvar_3 = 1 atm ± 0.05 atm`, or
  `GLOBconstr_1 BETWEEN 95 kPa AND 105 kPa; tol=0.1 kPa`.
  Component- and phase-linked constraints use the same suffix options, for
  example `GLOBconstr_5 = 20 %; component=GLOBcomp_1; phase=GLOBphase_3`.
- `system_scope` is exactly `declared`, `subsystem`, or `either`; subsystem
  search is opt-in. `comparison_grid` is `auto` or flat composition points.
- The enrichment/confirmation gate runs AUTOMATICALLY inside the tool: a
  parseable call is hard-parsed, enriched, content-address confirmed against
  the live registry/database/settings state, and executed in one call. The
  executed result restates the complete enriched identities, names,
  structures, canonical units/values, conversion traces, tolerances,
  operations, defaults, and scope. Invalid inputs return a
  `correction_required` review with actionable issues and never search data.
  The agent never emits a confirmation token; verify the returned enrichment
  evidence and revise the minimal GLOB-ID call if the chemistry is wrong.

## L2_subagents
- L2_comp_eval(purpose, instruction, context) — evaluate compounds (≤500 tok)
- L2_meas_eval(purpose, instruction, context) — evaluate measurements (≤500 tok)
- L2_ref_eval(purpose, instruction, context) — evaluate references (≤500 tok)
- L2_prop_eval(purpose, instruction, context) — evaluate properties (≤500 tok)

## automatic compaction (not callable tools)

Search JSON is automatically converted to compact Markdown. Do not emit calls
to internal card or block compactor functions.

# Prompt Template

## Purpose
{{purpose}}

## Instruction
{{instruction}}

## ID Catalog (from working memory)
{{id_catalog}}

## Prior Context
{{context}}

# Phases

## phase_1: resolve_ids
tools: [id_resolution]
guidance: |
  Resolve all names to typed global IDs. Report ambiguous/failed resolutions.

## phase_2: search_and_filter
tools: [block_search, specialized_ranking, compactors]
guidance: |
  Search with resolved global IDs. Compact returned cards before reasoning.
  Use block_search_adv only for exact row-level predicates, common-point
  requirements, calculations, aggregates, or ordering inside ThermoML blocks.
  For requested rankings, use screen_property_systems after ID resolution.
  If no results, try broadening filters.

## phase_3: deep_evaluate
tools: [L2_subagents]
guidance: |
  Call only the L2 evaluators needed for chemistry interpretation or evidence
  checking. Use the literature and block anchors returned by search tools in
  the current ReAct trace. `core_blocks_found` is constructed later by the
  post-answer ID-alignment branch and is therefore not a live fan-out source.

## phase_4: assemble_return
tools: []
guidance: |
  Put only the complete chemistry answer text inside the required
  `<answer>...</answer>` protocol marker. Include concise explanations and
  useful examples supported by the completed tool results. Do not emit JSON,
  core claims, identifier catalogs, or schema fields. The tool-free post-answer
  evaluator will organize core claims and minimal core ID batches after this agent terminates. Two hidden
  deterministic tools validate and construct the enriched core ID fields before assembly.
  `data_inspections` is harvested mechanically from your inspect_block_table
  results after termination — never author it; just run the inspections.

## Tool Calling

Format — one or more tool calls per turn:

<reasoning>
... internal reasoning (discarded each turn) ...
</reasoning>
<summary>
... 2-5 sentence conclusion (kept in memory, ≤600 chars) ...
</summary>
<tool_call>{"name": "tool_a", "arguments": {"p1": "v1"}}</tool_call>
<tool_call>{"name": "tool_b", "arguments": {"p2": 123}}</tool_call>
<wait/>

Final answer (no more tool calls):

<answer>
... complete answer — any length, markers stripped ...
</answer>

Rules:
- Batch independent tool calls in one turn — add multiple <tool_call>…</tool_call> blocks before <wait/>. All execute before the next turn.
- <tool_call> MUST come AFTER </summary> and BEFORE <wait/>. Arguments must be valid JSON.
- <answer> must NEVER mention internal mechanics (working memory, queries, memory keys, agent systems).
- If a tool returns an error, try a different approach or adjust parameters.

Available tools:
- L2_comp_eval(purpose, instruction='', context='', id_catalog='') — Create a new function with partial application of the given arguments
- L2_meas_eval(purpose, instruction='', context='', id_catalog='') — Create a new function with partial application of the given arguments
- L2_prop_eval(purpose, instruction='', context='', id_catalog='') — Create a new function with partial application of the given arguments
- L2_ref_eval(purpose, instruction='', context='', id_catalog='') — Create a new function with partial application of the given arguments
- block_search_adv(targets, explanation, compounds=None, compound_match='all', system_type=None, system_scope='declared', system_size_min=None, system_size_max=None, parameters=None, literature=None, phases=None, phase_match='all', fixed_constraints=None, inline_state=None, where=None, minimum_common_points=1, calculate=None, select=None, having=None, order_by=None, limit=50, purpose, tasks) — Run uncommon, exact-row chemistry searches over ThermoML data blocks.
- inspect_block_table(block_number, literature=None, where=None, nearest=None, BLKsubsys_id=None, property_filter=None, purpose, tasks) — Return the verbatim data sub-table of ONE block for answer grounding.
- resolve_compound_ids(queries, min_score=50, limit=20, purpose, tasks)
- resolve_ids(entity_type, queries, min_score=50, limit=20, purpose, tasks)
- resolve_measurement_ids(queries, min_score=50, limit=20, purpose, tasks)
- resolve_property_ids(queries, min_score=50, limit=20, purpose, tasks)
- resolve_reference_ids(queries, min_score=50, limit=20, purpose, tasks)
- screen_property_systems(ranking_targets, target_constraints, center_comp_num_ids, system_type=None, system_scope='declared', comparison_grid='auto', limit=20, confirmation_token=None, purpose, tasks) — Screen and rank ThermoML systems on chemically comparable data.
- search_blocks(compound=None, property=None, measurement=None, literature=None, system_type=None, system_scope='declared', phase=None, temperature_range=None, pressure_range=None, limit=50, block_number=None, purpose, tasks) — Search PCS_INDIV.db for data blocks matching multi-criteria filters.
- search_id_alignment(entity_type, query, limit=20, purpose, tasks) — Resolve *query* against the CSV registry for *entity_type*.
- search_similar_compounds(comp_num_id=None, smiles=None, inchi=None, name=None, top_k=10, min_similarity=0.0, metric='morgan', purpose, tasks) — Find the top-K most structurally similar compounds.
- search_system_registry(compound=None, property=None, system_type=None, system_scope='declared', block_type=None, literature=None, n_components=None, phase=None, temperature_range=None, pressure_range=None, n_datapoints_min=None, include_reactions=False, limit=100, purpose, tasks) — Search the block registries for data blocks matching the given criteria.
- search_system_summary(compound=None, property=None, system_type=None, system_scope='declared', temperature_range=None, pressure_range=None, include_reactions=False, limit=20, purpose, tasks) — Return aggregate statistics for a compound, property, or both.

# Working-agent final-answer contract

When the chemistry exploration is complete, emit exactly one
`<answer>...</answer>` block containing the full user-facing answer text.
The answer should include concise chemical insight, explanations, and useful
examples when supported by the completed work.

Do not emit JSON, core_claims arrays, source objects, identifier catalogs, schema
fields, or any other separate machine-facing structure in the final answer.
Identifiers or citations may appear naturally inside the answer text when
they are needed to explain a supported result, but they must not be emitted
as an additional structure. Two parallel, tool-free post-answer agents will
distill core_claims and organize ID/metadata fields after this agent terminates.
Earlier instructions that ask you to assemble final JSON are superseded by
this contract.

# Final-answer precedence

The working-agent final-answer contract above has precedence over all earlier phase guidance. Final output is answer text only; the parallel post-answer agents create every JSON field after termination.

## Working Memory
<memory>
# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->

## Results
<!-- Indexed findings. Compactable per-entry. -->

</memory>

## Subagent
## Purpose
Find viscosity data for binary ethylene glycol + water mixtures near 298.15 K

## Instruction
Search for dynamic viscosity (GLOBprop_4) data blocks for binary mixtures of ethylene glycol (1,2-ethanediol) and water at temperature near 298.15 K. Return DOIs, block numbers, and compound IDs.

## ID Catalog (from working memory)
[]

## Assistant
(syntax-rejected turn — malformed tool calls never executed; corrected on a later turn. Full detail in the run log.)

## User
(validation fired earlier — corrected)

## Assistant
<summary>Resolving compound IDs for ethylene glycol and water to search for viscosity data in binary mixtures.</summary>
<tool_call>resolve_compound_ids(queries=['ethylene glycol…, min_score=50, limit=5)</tool_call>

## User
<tool_result>
Both compounds resolved with exact name matches.

| Compound | ID | Formula | SMILES |
|---|---|---|---|
| 1,2-ethanediol (ethylene glycol) | GLOBcomp_24 | C2H6O2 | OCCO |
| water | GLOBcomp_1 | H2O | O |
</tool_result>

## Assistant
<summary>Compounds resolved: ethylene glycol = GLOBcomp_24, water = GLOBcomp_1. Now searching for binary viscosity (GLOBprop_4) blocks near 298.15 K.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_24', 'GLOBcomp_1'], property=GLOBprop_4, system_type=binary…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Re-emitting search_blocks with correct temperature_range format as list of floats [293.0, 303.0].</summary>
<tool_call>search_blocks(compound=['GLOBcomp_24', 'GLOBcomp_1'], property=GLOBprop_4, system_type=binary…)</tool_call>

## User
<tool_result>
**Summary:** Found 6 viscosity (Pa·s) blocks for binary 1,2-ethanediol (GLOBcomp_24) + water (GLOBcomp_1) mixtures with temperatures within 293–303 K. All blocks are liquid-phase, declared binary systems with score 100.

| # | DOI | Block | GLOBlit | Pts | T range (K) | Composition var | P (kPa) | EG comp ID | Water comp ID |
|---|-----|-------|---------|-----|-------------|-----------------|---------|------------|---------------|
| 1 | 10.1016/j.jct.2006.01.011 | PROPblock_13 | GLOBlit_2656 | 10 | 293.15 (fixed) | mass_fraction EG | 101.325 | DOIcomp_1→GLOBcomp_24 | DOIcomp_3→GLOBcomp_1 |
| 2 | 10.1016/j.jct.2018.02.022 | PROPblock_24 | GLOBlit_5201 | 84 | 293.15–303.15 | mole_fraction EG | 92.3 | DOIcomp_2→GLOBcomp_24 | DOIcomp_6→GLOBcomp_1 |
| 3 | 10.1021/acs.jced.6b00526 | PROPblock_18 | GLOBlit_6951 | 33 | 293.15–303.15 | mole_fraction water | 100.0 | DOIcomp_1→GLOBcomp_24 | DOIcomp_5→GLOBcomp_1 |
| 4 | 10.1021/je020140j | PROPblock_5 | GLOBlit_8038 | 77 | 293.15–353.15 | mole_fraction EG | 101.0 | DOIcomp_1→GLOBcomp_24 | DOIcomp_2→GLOBcomp_1 |
| 5 | 10.1021/je025610o | PROPblock_5 | GLOBlit_8106 | 30 | 296.45–449.85 | mole_fraction EG | 100.0 | DOIcomp_1→GLOBcomp_24 | DOIcomp_4→GL
</tool_result>

## Assistant


<reasoning>
The search returned 6 blocks with viscosity data for binary ethylene glycol + water mixtures near 298.15 K. I have all the information needed to answer the question. Let me compile the results.

Looking at the results, I can see 5 entries clearly (the 6th seems cut off). Let me provide the answer with what was returned.

The results show:
1. GLOBlit_2656, PROPblock_13 - DOI: 10.1016/j.jct.2006.01.011
2. GLOBlit_5201, PROPblock_24 - DOI: 10.1016/j.jct.2018.02.022
3. GLOBlit_6951, PROPblock_18 - DOI: 10.1021/acs.jced.6b00526
4. GLOBlit_8038, PROPblock_5 - DOI: 10.1021/je020140j
5. GLOBlit_8106, PROPblock_5 - DOI: 10.1021/je025610o
6. (truncated - likely one more)

I have enough to provide a complete answer.
</reasoning>

<answer>
**Viscosity data for binary ethylene glycol (1,2-ethanediol) + water mixtures near 298.15 K**

**Compounds resolved:**
- Ethylene glycol (1,2-ethanediol): **GLOBcomp_24** (C₂H₆O₂, SMILES: OCCO)
- Water: **GLOBcomp_1** (H₂O)

**Property:** Dynamic viscosity (GLOBprop_4), units: Pa·s

Six data blocks were found for binary liquid-phase mixtures in the temperature range 293–303 K:

| # | DOI | Block | Literature ID | Data Points | T range (K) | Composition Variable | P (kPa) |
|---|-----|-------|---------------|-------------|-------------|----------------------|---------|
| 1 | 10.1016/j.jct.2006.01.011 | PROPblock_13 | GLOBlit_2656 | 10 | 293.15 (fixed) | mass fraction EG (DOIcomp_1→GLOBcomp_24) | 101.325 |
| 2 | 10.1016/j.jct.2018.02.022 | PROPblock_24 | GLOBlit_5201 | 84 | 293.15–303.15 | mole fraction EG (DOIcomp_2→GLOBcomp_24) | 92.3 |
| 3 | 10.1021/acs.jced.6b00526 | PROPblock_18 | GLOBlit_6951 | 33 | 293.15–303.15 | mole fraction water (DOIcomp_5→GLOBcomp_1) | 100.0 |
| 4 | 10.1021/je020140j | PROPblock_5 | GLOBlit_8038 | 77 | 293.15–353.15 | mole fraction EG (DOIcomp_1→GLOBcomp_24) | 101.0 |
| 5 | 10.1021/je025610o | PROPblock_5 | GLOBlit_8106 | 30 | 296.45–449.85 | mole fraction EG (DOIcomp_1→GLOBcomp_24) | 100.0 |

A sixth block was also matched but its details were truncated in the search return.

All blocks represent declared binary systems in the liquid phase. The composition is expressed as either mole fraction or mass fraction of ethylene glycol (or, in one case, mole fraction of water). The most data-rich blocks near 298.15 K are GLOBlit_5201::PROPblock_24 (84 points, 293–303 K) and GLOBlit_8038::PROPblock_5 (77 points, 293–353 K), both using mole fraction of ethylene glycol as the composition variable.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_BLOCK** PROPblock_13 + PROPblock_24 + PROPblock_18 + PROPblock_5: PROPblock_13 + PROPblock_24 + PROPblock_18 + PROPblock_5 is quoted with data values (293.15, 101.325, 84, 293.15, …) but was never inspected in this run (values 293.15, 293.15, 303.15, 92.3 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_13", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="GLOBlit_5201::PROPblock_24"); inspect_block_table(block_number="PROPblock_18", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="GLOBlit_8038::PROPblock_5")`
- **UNINSPECTED_BLOCK** PROPblock_5: PROPblock_5 is quoted with data values (298.15, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_8038::PROPblock_5")`
- **UNINSPECTED_BLOCK** GLOBlit_5201::PROPblock_24: GLOBlit_5201::PROPblock_24 is quoted with data values (84, 293, 303, …) but was never inspected in this run (values 293, 303 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_5201::PROPblock_24")`
- **UNINSPECTED_BLOCK** GLOBlit_8038::PROPblock_5: GLOBlit_8038::PROPblock_5 is quoted with data values (77, 293, 353, …) but was never inspected in this run (values 293, 353 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_8038::PROPblock_5")`

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## Assistant
<summary>Running inspect_block_table on the cited blocks to ground the data values from the search results. Inspecting blocks from GLOBlit_2656, GLOBlit_5201, GLOBlit_6951, GLOBlit_8038, and GLOBlit_8106.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_13, literature=GLOBlit_2656)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2006.01.011 [GLOBlit_2656] :: PROPblock_13 (binary: 1,2-ethanediol + water)
filter: none (whole block)
block constraints: temperature_k = 293.15; pressure_kpa = 101.325

| BLKpoint_id | mass_fraction_<1,2-ethanediol> | temperature_k | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 0 | 293.15 | 101.325 | 0.001008 |
| BLKpoint_2 | 0.1 | 293.15 | 101.325 | 0.001293 |
| BLKpoint_3 | 0.2 | 293.15 | 101.325 | 0.001671 |
| BLKpoint_4 | 0.3 | 293.15 | 101.325 | 0.002177 |
| BLKpoint_5 | 0.4 | 293.15 | 101.325 | 0.002837 |
| BLKpoint_6 | 0.5 | 293.15 | 101.325 | 0.003558 |
| BLKpoint_7 | 0.6 | 293.15 | 101.325 | 0.004724 |
| BLKpoint_8 | 0.7 | 293.15 | 101.325 | 0.00636 |
| BLKpoint_9 | 0.8 | 293.15 | 101.325 | 0.008003 |
| BLKpoint_10 | 0.9 | 293.15 | 101.325 | 0.013999 |

mode: complete — all 10 matched rows shown (block has 10)
topology: viscosity_pa_s vs mass_fraction_1_2_ethanediol: monotonic↑
stats (matched, n=10): mass_fraction_1_2_ethanediol 0–0.9 (n=10); temperature_k 293.15–293.15 (n=10); pressure_kpa 101.325–101.325 (n=10); viscosity_pa_s 0.001008–0.013999 (n=10)
inspection_id: INSP_eb6a6a268c1a
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_2656::PROPblock_13 — 10 points at 293.15 K, 101.325 kPa, mass fraction EG 0–0.9, viscosity 0.001008–0.013999 Pa·s. Now inspecting remaining blocks.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_5201::PROPblock_24)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2018.02.022 [GLOBlit_5201] :: PROPblock_24 (binary: 1,2-ethanediol + water)
filter: none (whole block)
block constraints: pressure_kpa = 92.3

| BLKpoint_id | temperature_k | mole_fraction_<1,2-ethanediol> | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 293.15 | 0.0494 | 92.3 | 0.0015411 |
| BLKpoint_4 | 293.15 | 0.2072 | 92.3 | 0.0035171 |
| BLKpoint_9 | 293.15 | 0.4446 | 92.3 | 0.0076382 |
| BLKpoint_23 | 298.15 | 0.2072 | 92.3 | 0.0028109 |
| BLKpoint_28 | 298.15 | 0.4446 | 92.3 | 0.0060624 |
| BLKpoint_47 | 303.15 | 0.4446 | 92.3 | 0.0053492 |
| BLKpoint_65 | 308.15 | 0.3921 | 92.3 | 0.0040265 |
| BLKpoint_77 | 293.15 | 0 | 92.3 | 0.0010673 |
| BLKpoint_78 | 298.15 | 0 | 92.3 | 0.00089689 |
| BLKpoint_79 | 303.15 | 0 | 92.3 | 0.0008385 |
| BLKpoint_80 | 308.15 | 0 | 92.3 | 0.00075887 |
| BLKpoint_81 | 293.15 | 1 | 92.3 | 0.020613 |
| BLKpoint_82 | 298.15 | 1 | 92.3 | 0.016223 |
| BLKpoint_83 | 303.15 | 1 | 92.3 | 0.013867 |
| BLKpoint_84 | 308.15 | 1 | 92.3 | 0.011483 |

mode: RDP — 15 of 84 matched rows shown (shape-preserving; block has 84). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=84): temperature_k 293.15–308.15 (n=84); mole_fraction_1_2_ethanediol 0–1 (n=84); pressure_kpa 92.3–92.3 (n=84); viscosity_pa_s 0.00075887–0.020613 (n=84)
inspection_id: INSP_10e84136b97d
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_5201::PROPblock_24 — 84 points, T 293.15–308.15 K, mole fraction EG 0–1, viscosity 0.00075887–0.020613 Pa·s at 92.3 kPa. Now inspecting remaining 3 blocks.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_6951::PROPblock_18)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/acs.jced.6b00526 [GLOBlit_6951] :: PROPblock_18 (binary: 1,2-ethanediol + water)
filter: none (whole block)
block constraints: pressure_kpa = 100.0

| BLKpoint_id | temperature_k | mole_fraction_<water> | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 293.15 | 0 | 100.0 | 0.02113 |
| BLKpoint_3 | 293.15 | 0.2014 | 100.0 | 0.01495 |
| BLKpoint_5 | 293.15 | 0.4011 | 100.0 | 0.01005 |
| BLKpoint_8 | 293.15 | 0.6995 | 100.0 | 0.004584 |
| BLKpoint_11 | 293.15 | 1 | 100.0 | 0.000949 |
| BLKpoint_12 | 298.15 | 0 | 100.0 | 0.01724 |
| BLKpoint_14 | 298.15 | 0.2014 | 100.0 | 0.01219 |
| BLKpoint_16 | 298.15 | 0.4011 | 100.0 | 0.00831 |
| BLKpoint_19 | 298.15 | 0.6995 | 100.0 | 0.003884 |
| BLKpoint_22 | 298.15 | 1 | 100.0 | 0.000843 |
| BLKpoint_23 | 303.15 | 0 | 100.0 | 0.01423 |
| BLKpoint_25 | 303.15 | 0.2014 | 100.0 | 0.01014 |
| BLKpoint_28 | 303.15 | 0.4969 | 100.0 | 0.005653 |
| BLKpoint_33 | 303.15 | 1 | 100.0 | 0.000755 |

mode: RDP — 14 of 33 matched rows shown (shape-preserving; block has 33). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=33): temperature_k 293.15–303.15 (n=33); mole_fraction_water 0–1 (n=33); pressure_kpa 100.0–100.0 (n=33); viscosity_pa_s 0.000755–0.02113 (n=33)
inspection_id: INSP_bdb58d28aae5
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_6951::PROPblock_18 — 33 points, T 293.15–303.15 K, mole fraction water 0–1, viscosity 0.000755–0.02113 Pa·s at 100.0 kPa. Now inspecting the last two blocks.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_8038::PROPblock_5)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je020140j [GLOBlit_8038] :: PROPblock_5 (binary: 1,2-ethanediol + water)
filter: none (whole block)
block constraints: pressure_kpa = 101.0

| BLKpoint_id | mole_fraction_<1,2-ethanediol> | temperature_k | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 0 | 293.15 | 101.0 | 0.001002 |
| BLKpoint_7 | 0 | 353.15 | 101.0 | 0.000356 |
| BLKpoint_8 | 0.0312 | 293.15 | 101.0 | 0.001337 |
| BLKpoint_14 | 0.0312 | 353.15 | 101.0 | 0.000434 |
| BLKpoint_15 | 0.0676 | 293.15 | 101.0 | 0.001785 |
| BLKpoint_21 | 0.0676 | 353.15 | 101.0 | 0.000525 |
| BLKpoint_22 | 0.1105 | 293.15 | 101.0 | 0.002272 |
| BLKpoint_24 | 0.1105 | 313.15 | 101.0 | 0.001319 |
| BLKpoint_28 | 0.1105 | 353.15 | 101.0 | 0.000629 |
| BLKpoint_29 | 0.162 | 293.15 | 101.0 | 0.002951 |
| BLKpoint_31 | 0.162 | 313.15 | 101.0 | 0.001677 |
| BLKpoint_35 | 0.162 | 353.15 | 101.0 | 0.000758 |
| BLKpoint_36 | 0.2248 | 293.15 | 101.0 | 0.003941 |
| BLKpoint_38 | 0.2248 | 313.15 | 101.0 | 0.002132 |
| BLKpoint_42 | 0.2248 | 353.15 | 101.0 | 0.000906 |
| BLKpoint_43 | 0.3031 | 293.15 | 101.0 | 0.005102 |
| BLKpoint_45 | 0.3031 | 313.15 | 101.0 | 0.002756 |
| BLKpoint_49 | 0.3031 | 353.15 | 101.0 | 0.0011 |
| BLKpoint_50 | 0.4036 | 293.15 | 101.0 | 0.006898 |
| BLKpoint_52 | 0.4036 | 313.15 | 101.0 | 0.003575 |
| BLKpoint_54 | 0.4036 | 333.15 | 101.0 | 0.002053 |
| BLKpoint_56 | 0.4036 | 353.15 | 101.0 | 0.001359 |
| BLKpoint_57 | 0.537 | 293.15 | 101.0 | 0.009696 |
| BLKpoint_58 | 0.537 | 303.15 | 101.0 | 0.006749 |
| BLKpoint_59 | 0.537 | 313.15 | 101.0 | 0.004776 |
| BLKpoint_61 | 0.537 | 333.15 | 101.0 | 0.002684 |
| BLKpoint_63 | 0.537 | 353.15 | 101.0 | 0.001748 |
| BLKpoint_64 | 0.723 | 293.15 | 101.0 | 0.014042 |
| BLKpoint_65 | 0.723 | 303.15 | 101.0 | 0.009399 |
| BLKpoint_66 | 0.723 | 313.15 | 101.0 | 0.006449 |
| BLKpoint_68 | 0.723 | 333.15 | 101.0 | 0.00351 |
| BLKpoint_70 | 0.723 | 353.15 | 101.0 | 0.002296 |
| BLKpoint_71 | 1 | 293.15 | 101.0 | 0.020833 |
| BLKpoint_72 | 1 | 303.15 | 101.0 | 0.013646 |
| BLKpoint_73 | 1 | 313.15 | 101.0 | 0.009443 |
| BLKpoint_75 | 1 | 333.15 | 101.0 | 0.00506 |
| BLKpoint_77 | 1 | 353.15 | 101.0 | 0.003021 |

mode: RDP — 37 of 77 matched rows shown (shape-preserving; block has 77). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=77): mole_fraction_1_2_ethanediol 0–1 (n=77); temperature_k 293.15–353.15 (n=77); pressure_kpa 101.0–101.0 (n=77); viscosity_pa_s 0.000356–0.020833 (n=77)
inspection_id: INSP_ca607c3d05dd
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_8038::PROPblock_5 — 77 points, T 293.15–353.15 K, mole fraction EG 0–1, viscosity 0.000356–0.020833 Pa·s at 101.0 kPa. Now inspecting the last block GLOBlit_8106::PROPblock_5.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_8106::PROPblock_5)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je025610o [GLOBlit_8106] :: PROPblock_5 (binary: 1,2-ethanediol + water)
filter: none (whole block)
block constraints: pressure_kpa = 100.0

| BLKpoint_id | mole_fraction_<1,2-ethanediol> | temperature_k | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 0.25 | 296.45 | 100.0 | 0.00369 |
| BLKpoint_2 | 0.25 | 313.05 | 100.0 | 0.00229 |
| BLKpoint_4 | 0.25 | 353.05 | 100.0 | 0.00099 |
| BLKpoint_8 | 0.25 | 435.55 | 100.0 | 0.000366 |
| BLKpoint_9 | 0.5 | 297.05 | 100.0 | 0.00761 |
| BLKpoint_10 | 0.5 | 313.05 | 100.0 | 0.00449 |
| BLKpoint_11 | 0.5 | 333.1 | 100.0 | 0.00262 |
| BLKpoint_12 | 0.5 | 353.05 | 100.0 | 0.0017 |
| BLKpoint_13 | 0.5 | 380.05 | 100.0 | 0.00107 |
| BLKpoint_17 | 0.5 | 440.65 | 100.0 | 0.0005 |
| BLKpoint_18 | 0.75 | 297.35 | 100.0 | 0.0123 |
| BLKpoint_19 | 0.75 | 313.05 | 100.0 | 0.00697 |
| BLKpoint_20 | 0.75 | 333.1 | 100.0 | 0.00388 |
| BLKpoint_21 | 0.75 | 353.05 | 100.0 | 0.00242 |
| BLKpoint_22 | 0.75 | 373.45 | 100.0 | 0.00162 |
| BLKpoint_30 | 0.75 | 449.85 | 100.0 | 0.000594 |

mode: RDP — 16 of 30 matched rows shown (shape-preserving; block has 30). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=30): mole_fraction_1_2_ethanediol 0.25–0.75 (n=30); temperature_k 296.45–449.85 (n=30); pressure_kpa 100.0–100.0 (n=30); viscosity_pa_s 0.000366–0.0123 (n=30)
inspection_id: INSP_475115ec48f0
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<answer>
**Viscosity data for binary ethylene glycol (1,2-ethanediol) + water mixtures near 298.15 K**

**Compounds resolved:**
- Ethylene glycol (1,2-ethanediol): **GLOBcomp_24** (C₂H₆O₂, SMILES: OCCO)
- Water: **GLOBcomp_1** (H₂O)

**Property:** Dynamic viscosity (GLOBprop_4), units: Pa·s

Five inspected data blocks were found for binary liquid-phase mixtures covering temperatures near 298.15 K:

| # | DOI | Block | Literature ID | Data Points | T range (K) | Composition Variable | P (kPa) |
|---|-----|-------|---------------|-------------|-------------|----------------------|---------|
| 1 | 10.1016/j.jct.2006.01.011 | PROPblock_13 | GLOBlit_2656 | 10 | 293.15–293.15 | mass fraction EG (GLOBcomp_24) | 101.325 |
| 2 | 10.1016/j.jct.2018.02.022 | PROPblock_24 | GLOBlit_5201 | 84 | 293.15–308.15 | mole fraction EG (GLOBcomp_24) | 92.3 |
| 3 | 10.1021/acs.jced.6b00526 | PROPblock_18 | GLOBlit_6951 | 33 | 293.15–303.15 | mole fraction water (GLOBcomp_1) | 100.0 |
| 4 | 10.1021/je020140j | PROPblock_5 | GLOBlit_8038 | 77 | 293.15–353.15 | mole fraction EG (GLOBcomp_24) | 101.0 |
| 5 | 10.1021/je025610o | PROPblock_5 | GLOBlit_8106 | 30 | 296.45–449.85 | mole fraction EG (GLOBcomp_24) | 100.0 |

A sixth block was also matched in the initial search but its details were truncated; the five blocks above were fully inspected.

**Representative data near 298.15 K:**

From GLOBlit_5201::PROPblock_24 (at 298.15 K, 92.3 kPa):

| Mole fraction EG | Viscosity (Pa·s) |
|---|---|
| 0 | 0.00089689 |
| 0.2072 | 0.0028109 |
| 0.4446 | 0.0060624 |
| 1 | 0.016223 |

From GLOBlit_6951::PROPblock_18 (at 298.15 K, 100.0 kPa):

| Mole fraction water | Viscosity (Pa·s) |
|---|---|
| 0 | 0.01724 |
| 0.2014 | 0.01219 |
| 0.4011 | 0.00831 |
| 0.6995 | 0.003884 |
| 1 | 0.000843 |

**Chemistry insight:** The viscosity of ethylene glycol–water mixtures increases strongly and nonlinearly with ethylene glycol content. Pure EG at 298.15 K has a viscosity roughly 16–20 times that of pure water (e.g., 0.016223 vs 0.00089689 Pa·s in GLOBlit_5201, and 0.01724 vs 0.000843 Pa·s in GLOBlit_6951). This reflects the extensive hydrogen-bonding network formed by the two hydroxyl groups of ethylene glycol. The most data-rich blocks near 298.15 K are GLOBlit_5201::PROPblock_24 (84 points, 293.15–308.15 K) and GLOBlit_8038::PROPblock_5 (77 points, 293.15–353.15 K), both using mole fraction of ethylene glycol as the composition variable.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **AMBIGUOUS_VALUE** PROPblock_5: 298.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_5", literature="<GLOBlit_N or DOI>", nearest={"column": "mole_fraction_<1,2-ethanediol>", "value": 298.15})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **MISATTRIBUTED_VALUE** GLOBlit_6951::PROPblock_18: 16 does not belong to GLOBlit_6951::PROPblock_18; it matches only GLOBlit_5201::PROPblock_24 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 16 to GLOBlit_5201::PROPblock_24 — no new tool call needed`
- **MISATTRIBUTED_VALUE** GLOBlit_6951::PROPblock_18: 0.016223 does not belong to GLOBlit_6951::PROPblock_18; it matches only GLOBlit_5201::PROPblock_24 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 0.016223 to GLOBlit_5201::PROPblock_24 — no new tool call needed`
- **MISATTRIBUTED_VALUE** GLOBlit_6951::PROPblock_18: 0.00089689 does not belong to GLOBlit_6951::PROPblock_18; it matches only GLOBlit_5201::PROPblock_24 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 0.00089689 to GLOBlit_5201::PROPblock_24 — no new tool call needed`
Inspected so far: PROPblock_13, PROPblock_18, PROPblock_24, PROPblock_5

Verified as grounded — correct as quoted, keep unchanged:
- PROPblock_13 + PROPblock_24 + PROPblock_18 + PROPblock_5: 293.15, 101.325, 84, 308.15, 92.3, 33, 303.15, 100.0, 77, 353.15, 101.0, 30, 296.45, 449.85
- GLOBlit_5201::PROPblock_24: 298.15, 92.3, 0.00089689, 0.2072, 0.0028109, 0.4446, 0.0060624, 0.016223, 84, 293.15, 308.15
- GLOBlit_8038::PROPblock_5: 77, 293.15, 353.15
Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- GLOBlit_6951::PROPblock_18: 298.15, 100.0, 0.01724, 0.2014, 0.01219, 0.4011, 0.00831, 0.6995, 0.003884, 0.000843, 20

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## LLM Response
<reasoning>
Let me analyze the flagged issues:

1. **AMBIGUOUS_VALUE** PROPblock_5: "298.15" — This value appears in my chemistry insight paragraph where I say "Pure EG at 298.15 K". The value 298.15 is a temperature condition I'm discussing, not a data value from a specific block. It appears in inspected data from GLOBlit_5201::PROPblock_24 and GLOBlit_6951::PROPblock_18. I should clarify which block I'm referencing.

2. **MISATTRIBUTED_VALUE** GLOBlit_6951::PROPblock_18: "16" — This is a computed ratio (0.016223/0.00089689 ≈ 18, or 0.01724/0.000843 ≈ 20.5). I said "roughly 16–20 times". The "16" was derived from GLOBlit_5201 data (0.016223/0.00089689 ≈ 18.1), and "20" from GLOBlit_6951 data (0.01724/0.000843 ≈ 20.5). These are computed ratios, not database values. I need to label them as derived.

3. **MISATTRIBUTED_VALUE** GLOBlit_6951::PROPblock_18: "0.016223" and "0.00089689" — These are from GLOBlit_5201::PROPblock_24, not GLOBlit_6951. I cited them in the same sentence as GLOBlit_6951 data. I need to re-anchor them properly.

Let me fix the chemistry insight paragraph to properly attribute values and label computed ratios.

The fix: In the chemistry insight, I compared values from two different blocks in one sentence. I need to properly attribute 0.016223 and 0.00089689 to GLOBlit_5201::PROPblock_24, and 0.01724 and 0.000843 to GLOBlit_6951::PROPblock_18. The ratios "16–20" are derived computations that should be labeled as such.

Actually, let me recompute: 0.016223/0.00089689 = ~18.1, and 0.01724/0.000843 = ~20.5. So "roughly 16–20 times" should be corrected to "roughly 18–20 times" based on the actual computed ratios. Wait, the grounding check says "16" is flagged but "20" is verified as grounded to GLOBlit_6951. Actually "20" is listed as verified for GLOBlit_6951::PROPblock_18. But 20 is also a computed ratio... Let me just label both as derived values and fix the attribution.

I'll rewrite the insight paragraph to properly anchor each value to its source block and label the ratios as derived.
</reasoning>

<answer>
**Viscosity data for binary ethylene glycol (1,2-ethanediol) + water mixtures near 298.15 K**

**Compounds resolved:**
- Ethylene glycol (1,2-ethanediol): **GLOBcomp_24** (C₂H₆O₂, SMILES: OCCO)
- Water: **GLOBcomp_1** (H₂O)

**Property:** Dynamic viscosity (GLOBprop_4), units: Pa·s

Five inspected data blocks were found for binary liquid-phase mixtures covering temperatures near 298.15 K:

| # | DOI | Block | Literature ID | Data Points | T range (K) | Composition Variable | P (kPa) |
|---|-----|-------|---------------|-------------|-------------|----------------------|---------|
| 1 | 10.1016/j.jct.2006.01.011 | PROPblock_13 | GLOBlit_2656 | 10 | 293.15–293.15 | mass fraction EG (GLOBcomp_24) | 101.325 |
| 2 | 10.1016/j.jct.2018.02.022 | PROPblock_24 | GLOBlit_5201 | 84 | 293.15–308.15 | mole fraction EG (GLOBcomp_24) | 92.3 |
| 3 | 10.1021/acs.jced.6b00526 | PROPblock_18 | GLOBlit_6951 | 33 | 293.15–303.15 | mole fraction water (GLOBcomp_1) | 100.0 |
| 4 | 10.1021/je020140j | PROPblock_5 | GLOBlit_8038 | 77 | 293.15–353.15 | mole fraction EG (GLOBcomp_24) | 101.0 |
| 5 | 10.1021/je025610o | PROPblock_5 | GLOBlit_8106 | 30 | 296.45–449.85 | mole fraction EG (GLOBcomp_24) | 100.0 |

A sixth block was also matched in the initial search but its details were truncated; the five blocks above were fully inspected.

**Representative data near 298.15 K:**

From GLOBlit_5201::PROPblock_24 (at 298.15 K, 92.3 kPa):

| Mole fraction EG | Viscosity (Pa·s) |
|---|---|
| 0 | 0.00089689 |
| 0.2072 | 0.0028109 |
| 0.4446 | 0.0060624 |
| 1 | 0.016223 |

From GLOBlit_6951::PROPblock_18 (at 298.15 K, 100.0 kPa):

| Mole fraction water | Viscosity (Pa·s) |
|---|---|
| 0 | 0.01724 |
| 0.2014 | 0.01219 |
| 0.4011 | 0.00831 |
| 0.6995 | 0.003884 |
| 1 | 0.000843 |

**Chemistry insight:** The viscosity of ethylene glycol–water mixtures increases strongly and nonlinearly with ethylene glycol content. In GLOBlit_5201::PROPblock_24 at 298.15 K, pure EG viscosity is 0.016223 Pa·s versus 0.00089689 Pa·s for pure water (a ratio of approximately 18×, derived by division). In GLOBlit_6951::PROPblock_18 at 298.15 K, pure EG viscosity is 0.01724 Pa·s versus 0.000843 Pa·s for pure water (a ratio of approximately 20×, derived by division). This reflects the extensive hydrogen-bonding network formed by the two hydroxyl groups of ethylene glycol. The most data-rich blocks near 298.15 K are GLOBlit_5201::PROPblock_24 (84 points, 293.15–308.15 K) and GLOBlit_8038::PROPblock_5 (77 points, 293.15–353.15 K), both using mole fraction of ethylene glycol as the composition variable.
</answer>