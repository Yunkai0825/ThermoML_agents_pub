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
Find density (mass density, GLOBprop_1) data blocks for binary mixtures of ethanol and water, especially at or near 350 K. Need mixture composition-dependent density data.

## Instruction
Search for blocks containing both ethanol and water as components with mass density (GLOBprop_1) as the measured property. Look for mixture data (not pure component) with temperature coverage near 350 K. Return DOIs, block numbers, temperature ranges, and number of data points.

## ID Catalog (from working memory)
[]

## Assistant
<summary>Resolving compound IDs for ethanol and water to search for binary mixture density data near 350 K.</summary>
<tool_call>resolve_compound_ids(queries=['ethanol', 'water'], min_score=80, limit=5)</tool_call>

## User
<tool_result>
Both compounds resolved with exact name matches.

| Compound | ID | Formula | SMILES |
|----------|----|---------|--------|
| ethanol | GLOBcomp_2 | C2H6O | CCO |
| water | GLOBcomp_1 | H2O | O |
</tool_result>

## Assistant
<summary>Resolved: ethanol = GLOBcomp_2, water = GLOBcomp_1. Now searching for binary mixture density (GLOBprop_1) blocks near 350 K.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_2', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Fixing temperature_range to proper list format [330, 370] and re-searching for ethanol+water binary density blocks.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_2', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
**Summary:** Four binary ethanol–water mass density blocks were found. The most relevant for ~350 K are **GLOBlit_1742** (T: 350.7–373.2 K, 84 pts) and **GLOBlit_1483** (T: 292.95–448.15 K, 140 pts). GLOBlit_220 (810 pts) and GLOBlit_2432 (565 pts) have titles mentioning high temperatures but their RDP-sampled topologies only showed ~298 K; the full datasets likely extend into the 330–370 K range.

| # | GLOBlit | DOI | Block | Pts | T range (K) | P range (kPa) | Composition | Method |
|---|---------|-----|-------|-----|-------------|---------------|-------------|--------|
| 1
</tool_result>

## Assistant


<reasoning>
The tool result was truncated, but I have key information: four binary ethanol-water density blocks were found. The most relevant for ~350 K are GLOBlit_1742 (T: 350.7–373.2 K, 84 pts) and GLOBlit_1483 (T: 292.95–448.15 K, 140 pts). GLOBlit_220 (810 pts) and GLOBlit_2432 (565 pts) also exist. Let me provide the answer with what I have. I should try to get the full table though - let me see if I can get more detail on the blocks near 350 K.

Actually, I have enough information to provide a useful answer. The summary clearly states the four blocks and their key characteristics. Let me compile the answer.
</reasoning>

<answer>
Four binary ethanol–water mass density (GLOBprop_1) data blocks were found in the ThermoML database:

**Most relevant for ~350 K:**

1. **GLOBlit_1742** — PROPblock_1  
   - Temperature range: 350.7–373.2 K  
   - 84 data points  
   - Directly covers the 350 K region

2. **GLOBlit_1483** — PROPblock_1  
   - Temperature range: 292.95–448.15 K  
   - 140 data points  
   - Broad temperature coverage that spans well through 350 K

**Additional blocks (likely extending into 330–370 K range):**

3. **GLOBlit_220** — 810 data points  
   - Title mentions high temperatures; the full dataset likely extends into the 330–370 K range

4. **GLOBlit_2432** — 565 data points  
   - Also likely covers the target temperature region based on its scope

**Compounds:** ethanol (GLOBcomp_2) + water (GLOBcomp_1), binary system.

The two most promising sources for composition-dependent density data near 350 K are GLOBlit_1483 (broadest T coverage, 140 pts) and GLOBlit_1742 (starts right at ~350.7 K, 84 pts). GLOBlit_220 and GLOBlit_2432 have the largest datasets (810 and 565 points respectively) and may also contain data near 350 K.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_BLOCK** PROPblock_1: PROPblock_1 is quoted with data values (350.7, 373.2, 84, 350, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_1", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_1: PROPblock_1 is quoted with data values (292.95, 448.15, 140, 350, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_1", literature="<GLOBlit_N or DOI>")`

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## Assistant
<summary>Inspecting the two most relevant blocks (GLOBlit_1742::PROPblock_1 and GLOBlit_1483::PROPblock_1) to ground temperature ranges and data point counts for the answer.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_1, literature=GLOBlit_1742)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.fluid.2015.07.012 [GLOBlit_1742] :: PROPblock_1 (binary: methanol + water)
filter: none (whole block)

| BLKpoint_id | temperature_k | pressure_kpa | mole_fraction_<methanol> | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 350.7 | 10000 | 0.1 | 945.55 |
| BLKpoint_4 | 350.7 | 10000 | 0.4 | 865.13 |
| BLKpoint_6 | 350.7 | 10000 | 0.8 | 780.91 |
| BLKpoint_7 | 350.7 | 20000 | 0.1 | 949.82 |
| BLKpoint_10 | 350.7 | 20000 | 0.4 | 870.55 |
| BLKpoint_12 | 350.7 | 20000 | 0.8 | 789.25 |
| BLKpoint_13 | 350.7 | 30000 | 0.1 | 954.11 |
| BLKpoint_16 | 350.7 | 30000 | 0.4 | 876.99 |
| BLKpoint_18 | 350.7 | 30000 | 0.8 | 797.6 |
| BLKpoint_19 | 350.7 | 40000 | 0.1 | 958.39 |
| BLKpoint_22 | 350.7 | 40000 | 0.4 | 882.71 |
| BLKpoint_24 | 350.7 | 40000 | 0.8 | 805.96 |
| BLKpoint_25 | 373.2 | 10000 | 0.1 | 928.71 |
| BLKpoint_29 | 373.2 | 10000 | 0.6 | 799.33 |
| BLKpoint_31 | 373.2 | 10000 | 1 | 725.29 |
| BLKpoint_32 | 373.2 | 20000 | 0.1 | 932.78 |
| BLKpoint_36 | 373.2 | 20000 | 0.6 | 807.98 |
| BLKpoint_38 | 373.2 | 20000 | 1 | 737.85 |
| BLKpoint_39 | 373.2 | 30000 | 0.1 | 939.53 |
| BLKpoint_42 | 373.2 | 30000 | 0.4 | 858.91 |
| BLKpoint_45 | 373.2 | 30000 | 1 | 748.83 |
| BLKpoint_46 | 373.2 | 40000 | 0.1 | 943.52 |
| BLKpoint_50 | 373.2 | 40000 | 0.6 | 823.64 |
| BLKpoint_52 | 373.2 | 40000 | 1 | 758.66 |
| BLKpoint_53 | 476.2 | 10000 | 0.1 | 822.65 |
| BLKpoint_56 | 476.2 | 10000 | 0.4 | 714.67 |
| BLKpoint_59 | 476.2 | 10000 | 1 | 576.84 |
| BLKpoint_60 | 476.2 | 20000 | 0.1 | 831.4 |
| BLKpoint_63 | 476.2 | 20000 | 0.4 | 730.97 |
| BLKpoint_66 | 476.2 | 20000 | 1 | 612.56 |
| BLKpoint_67 | 476.2 | 30000 | 0.1 | 838.61 |
| BLKpoint_70 | 476.2 | 30000 | 0.4 | 744.11 |
| BLKpoint_73 | 476.2 | 30000 | 1 | 636.82 |
| BLKpoint_74 | 476.2 | 40000 | 0.1 | 845.82 |
| BLKpoint_77 | 476.2 | 40000 | 0.4 | 754.89 |
| BLKpoint_80 | 476.2 | 40000 | 1 | 655.67 |

mode: RDP — 36 of 80 matched rows shown (shape-preserving; block has 80). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=80): temperature_k 350.7–476.2 (n=80); pressure_kpa 10000–40000 (n=80); mole_fraction_methanol 0.1–1 (n=80); mass_density_kg_m3 576.84–958.39 (n=80)
inspection_id: INSP_da246e84fdf8
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
(syntax-rejected turn — malformed tool calls never executed; corrected on a later turn. Full detail in the run log.)

## User
(validation fired earlier — corrected)

## Assistant
<summary>GLOBlit_1742::PROPblock_1 is actually methanol+water (not ethanol+water). Need to inspect GLOBlit_1483::PROPblock_1 to check if it's ethanol+water.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_1, literature=GLOBlit_1483)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.fluid.2014.05.032 [GLOBlit_1483] :: PROPblock_1 (binary: ethanol + water)
filter: none (whole block)

| BLKpoint_id | pressure_kpa | temperature_k | mole_fraction_<ethanol> | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 39170 | 297.05 | 0.0163 | 1006.1 |
| BLKpoint_2 | 30810 | 297.05 | 0.0163 | 1003.2 |
| BLKpoint_3 | 21070 | 297.05 | 0.0163 | 997.5 |
| BLKpoint_4 | 11280 | 297.05 | 0.0163 | 993.5 |
| BLKpoint_5 | 2490 | 297.05 | 0.0163 | 990.8 |
| BLKpoint_6 | 38480 | 323.15 | 0.0163 | 995.2 |
| BLKpoint_7 | 30890 | 323.15 | 0.0163 | 992.3 |
| BLKpoint_8 | 21080 | 323.15 | 0.0163 | 988.4 |
| BLKpoint_9 | 11390 | 323.15 | 0.0163 | 984.4 |
| BLKpoint_10 | 2570 | 323.15 | 0.0163 | 980.6 |
| BLKpoint_11 | 39910 | 348.15 | 0.0163 | 982.3 |
| BLKpoint_12 | 29500 | 348.15 | 0.0163 | 978.3 |
| BLKpoint_13 | 20750 | 348.15 | 0.0163 | 974.7 |
| BLKpoint_14 | 10980 | 348.15 | 0.0163 | 970.6 |
| BLKpoint_15 | 3220 | 348.15 | 0.0163 | 967.1 |
| BLKpoint_16 | 35700 | 373.15 | 0.0163 | 964.6 |
| BLKpoint_17 | 30600 | 373.15 | 0.0163 | 962.5 |
| BLKpoint_18 | 21160 | 373.15 | 0.0163 | 958.3 |
| BLKpoint_19 | 11320 | 373.15 | 0.0163 | 953.8 |
| BLKpoint_20 | 3370 | 373.15 | 0.0163 | 950.2 |
| BLKpoint_21 | 39890 | 398.15 | 0.0163 | 948 |
| BLKpoint_22 | 30790 | 398.15 | 0.0163 | 943.7 |
| BLKpoint_23 | 21360 | 398.15 | 0.0163 | 939.3 |
| BLKpoint_24 | 11630 | 398.15 | 0.0163 | 934.4 |
| BLKpoint_25 | 3710 | 398.15 | 0.0163 | 930.3 |
| BLKpoint_26 | 39560 | 423.15 | 0.0163 | 927.2 |
| BLKpoint_27 | 30570 | 423.15 | 0.0163 | 922.4 |
| BLKpoint_28 | 20970 | 423.15 | 0.0163 | 917 |
| BLKpoint_29 | 10170 | 423.15 | 0.0163 | 911 |
| BLKpoint_30 | 2680 | 423.15 | 0.0163 | 906.7 |
| BLKpoint_31 | 38340 | 448.15 | 0.0163 | 903.5 |
| BLKpoint_32 | 31050 | 448.15 | 0.0163 | 899.4 |
| BLKpoint_33 | 21530 | 448.15 | 0.0163 | 893.7 |
| BLKpoint_34 | 11920 | 448.15 | 0.0163 | 887.5 |
| BLKpoint_35 | 3960 | 448.15 | 0.0163 | 882.3 |
| BLKpoint_36 | 39230 | 292.95 | 0.073 | 988 |
| BLKpoint_37 | 30930 | 292.95 | 0.073 | 985 |
| BLKpoint_38 | 21120 | 292.95 | 0.073 | 981.2 |
| BLKpoint_39 | 11320 | 292.95 | 0.073 | 977.6 |
| BLKpoint_40 | 2450 | 292.95 | 0.073 | 974.2 |
| BLKpoint_41 | 38600 | 323.15 | 0.073 | 973.6 |
| BLKpoint_42 | 30360 | 323.15 | 0.073 | 970.6 |
| BLKpoint_43 | 20790 | 323.15 | 0.073 | 966.7 |
| BLKpoint_44 | 10940 | 323.15 | 0.073 | 962.8 |
| BLKpoint_45 | 2610 | 323.15 | 0.073 | 959.3 |
| BLKpoint_46 | 39600 | 348.15 | 0.073 | 958.9 |
| BLKpoint_48 | 20870 | 348.15 | 0.073 | 950.8 |
| BLKpoint_49 | 11060 | 348.15 | 0.073 | 946.6 |
| BLKpoint_50 | 3330 | 348.15 | 0.073 | 943 |
| BLKpoint_51 | 37230 | 373.15 | 0.073 | 939.9 |
| BLKpoint_52 | 30670 | 373.15 | 0.073 | 937 |
| BLKpoint_53 | 21080 | 373.15 | 0.073 | 932.5 |
| BLKpoint_54 | 11320 | 373.15 | 0.073 | 927.7 |
| BLKpoint_55 | 3510 | 373.15 | 0.073 | 923.9 |
| BLKpoint_56 | 39500 | 398.15 | 0.073 | 920.7 |
| BLKpoint_57 | 30790 | 398.15 | 0.073 | 916.3 |
| BLKpoint_58 | 21160 | 398.15 | 0.073 | 911.4 |
| BLKpoint_59 | 11510 | 398.15 | 0.073 | 906.2 |
| BLKpoint_60 | 3710 | 398.15 | 0.073 | 901.9 |
| BLKpoint_61 | 40110 | 423.15 | 0.073 | 898.6 |
| BLKpoint_62 | 30490 | 423.15 | 0.073 | 893 |
| BLKpoint_63 | 20110 | 423.15 | 0.073 | 887.1 |
| BLKpoint_64 | 10710 | 423.15 | 0.073 | 881.1 |
| BLKpoint_65 | 2760 | 423.15 | 0.073 | 875.9 |
| BLKpoint_66 | 37210 | 448.15 | 0.073 | 873 |
| BLKpoint_67 | 31170 | 448.15 | 0.073 | 869.2 |
| BLKpoint_68 | 21690 | 448.15 | 0.073 | 862.7 |
| BLKpoint_69 | 12160 | 448.15 | 0.073 | 855.6 |
| BLKpoint_70 | 4000 | 448.15 | 0.073 | 849.3 |
| BLKpoint_71 | 40030 | 298.15 | 0.0946 | 979.8 |
| BLKpoint_72 | 29980 | 298.15 | 0.0946 | 976.1 |
| BLKpoint_73 | 20060 | 298.15 | 0.0946 | 972.4 |
| BLKpoint_74 | 10120 | 298.15 | 0.0946 | 968.6 |
| BLKpoint_75 | 2560 | 298.15 | 0.0946 | 965.8 |
| BLKpoint_76 | 39810 | 323.15 | 0.0946 | 966.2 |
| BLKpoint_77 | 32400 | 323.15 | 0.0946 | 963.3 |
| BLKpoint_78 | 20710 | 323.15 | 0.0946 | 958.8 |
| BLKpoint_79 | 11140 | 323.15 | 0.0946 | 954.9 |
| BLKpoint_80 | 2730 | 323.15 | 0.0946 | 951.3 |
| BLKpoint_81 | 37790 | 348.15 | 0.0946 | 948.7 |
| BLKpoint_82 | 29730 | 348.15 | 0.0946 | 945.4 |
| BLKpoint_83 | 20870 | 348.15 | 0.0946 | 941.6 |
| BLKpoint_84 | 11390 | 348.15 | 0.0946 | 937.4 |
| BLKpoint_85 | 2730 | 348.15 | 0.0946 | 933.7 |
| BLKpoint_86 | 39410 | 373.15 | 0.0946 | 927.3 |
| BLKpoint_87 | 30850 | 373.15 | 0.0946 | 922.3 |
| BLKpoint_88 | 21200 | 373.15 | 0.0946 | 917.7 |
| BLKpoint_90 | 3330 | 373.15 | 0.0946 | 908.6 |
| BLKpoint_91 | 39610 | 398.15 | 0.0946 | 905.3 |
| BLKpoint_92 | 30850 | 398.15 | 0.0946 | 901.1 |
| BLKpoint_93 | 21200 | 398.15 | 0.0946 | 896 |
| BLKpoint_94 | 11430 | 398.15 | 0.0946 | 890.4 |
| BLKpoint_95 | 3510 | 398.15 | 0.0946 | 885.8 |
| BLKpoint_96 | 39860 | 423.15 | 0.0946 | 882.2 |
| BLKpoint_97 | 30100 | 423.15 | 0.0946 | 875.5 |
| BLKpoint_98 | 20200 | 423.15 | 0.0946 | 869.5 |
| BLKpoint_99 | 10050 | 423.15 | 0.0946 | 863.9 |
| BLKpoint_100 | 2750 | 423.15 | 0.0946 | 860.1 |
| BLKpoint_101 | 40140 | 448.15 | 0.0946 | 858.6 |
| BLKpoint_102 | 30990 | 448.15 | 0.0946 | 852.6 |
| BLKpoint_103 | 21690 | 448.15 | 0.0946 | 845.8 |
| BLKpoint_104 | 11550 | 448.15 | 0.0946 | 837.9 |
| BLKpoint_105 | 3860 | 448.15 | 0.0946 | 831.7 |
| BLKpoint_106 | 39150 | 298.35 | 0.0343 | 998.6 |
| BLKpoint_107 | 31040 | 298.35 | 0.0343 | 995.7 |
| BLKpoint_108 | 21300 | 298.35 | 0.0343 | 991.9 |
| BLKpoint_110 | 2590 | 298.35 | 0.0343 | 984.1 |
| BLKpoint_112 | 30930 | 323.65 | 0.0343 | 985.2 |
| BLKpoint_113 | 21200 | 323.65 | 0.0343 | 981.4 |
| BLKpoint_114 | 11320 | 323.65 | 0.0343 | 977.4 |
| BLKpoint_115 | 2610 | 323.65 | 0.0343 | 973.6 |
| BLKpoint_116 | 39860 | 348.15 | 0.0343 | 974.7 |
| BLKpoint_117 | 30850 | 348.15 | 0.0343 | 971.3 |
| BLKpoint_118 | 21160 | 348.15 | 0.0343 | 967.5 |
| BLKpoint_119 | 11590 | 348.15 | 0.0343 | 963.5 |
| BLKpoint_121 | 39000 | 373.15 | 0.0343 | 957.9 |
| BLKpoint_122 | 30520 | 373.15 | 0.0343 | 954.5 |
| BLKpoint_123 | 21120 | 373.15 | 0.0343 | 950.3 |
| BLKpoint_124 | 11470 | 373.15 | 0.0343 | 945.9 |
| BLKpoint_126 | 37300 | 398.15 | 0.0343 | 938.3 |
| BLKpoint_127 | 30930 | 398.15 | 0.0343 | 935.2 |
| BLKpoint_128 | 21530 | 398.15 | 0.0343 | 930.7 |
| BLKpoint_129 | 11730 | 398.15 | 0.0343 | 925.8 |
| BLKpoint_131 | 39680 | 423.15 | 0.0343 | 918.2 |
| BLKpoint_132 | 30640 | 423.15 | 0.0343 | 913.4 |
| BLKpoint_133 | 21070 | 423.15 | 0.0343 | 908.1 |
| BLKpoint_135 | 2680 | 423.15 | 0.0343 | 897.3 |
| BLKpoint_136 | 40060 | 448.15 | 0.0343 | 894.8 |
| BLKpoint_137 | 31010 | 448.15 | 0.0343 | 889.8 |
| BLKpoint_138 | 22180 | 448.15 | 0.0343 | 884.2 |
| BLKpoint_140 | 4080 | 448.15 | 0.0343 | 872.1 |

mode: RDP — 131 of 140 matched rows shown (shape-preserving; block has 140). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=140): pressure_kpa 2450–40140 (n=140); temperature_k 292.95–448.15 (n=140); mole_fraction_ethanol 0.0163–0.0946 (n=140); mass_density_kg_m3 831.7–1006.1 (n=140)
inspection_id: INSP_51f9b5335a8a
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<reasoning>
Now I have inspected both blocks:

1. **GLOBlit_1742::PROPblock_1** — This is actually **methanol + water** (not ethanol + water). So this block is NOT relevant to the query about ethanol + water.

2. **GLOBlit_1483::PROPblock_1** — This IS ethanol + water, binary. It has 140 data points covering T: 292.95–448.15 K, P: 2450–40140 kPa, and mole fractions of ethanol: 0.0163–0.0946. It does cover 348.15 K which is near 350 K. However, the composition range is quite narrow (only up to ~9.5 mol% ethanol), so it's high-pressure density data at low ethanol concentrations.

I should also search for the other blocks (GLOBlit_220, GLOBlit_2432) but I need to be careful about my tool call budget. Let me also re-search specifically for ethanol+water binary density blocks to make sure I'm not missing any that have broader composition ranges near 350 K.

Actually, the original search found 4 blocks. GLOBlit_1742 turned out to be methanol+water, not ethanol+water. So I should note that. The other two blocks (GLOBlit_220 and GLOBlit_2432) were mentioned but I haven't inspected them. Let me provide the answer with what I have verified, noting that GLOBlit_1742 is methanol+water (not relevant), and GLOBlit_1483 is confirmed ethanol+water but with limited composition range. I should mention the other two blocks but note they weren't inspected.

Wait, I need to be more careful. The original search result mentioned 4 blocks but the table was truncated. I only have confirmed data for GLOBlit_1483. Let me do one more search to find the other ethanol+water density blocks properly.

Actually, I should just provide the answer with what I have. GLOBlit_1483 is confirmed. GLOBlit_1742 is methanol+water (excluded). The other two (GLOBlit_220, GLOBlit_2432) were mentioned in the search results but I haven't verified them. I should note this honestly.

Let me provide the answer now.
</reasoning>

<answer>
**Binary ethanol–water mass density data in the ThermoML database:**

The search for binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) mass density (GLOBprop_1) blocks found the following confirmed result:

### Confirmed ethanol–water block

**GLOBlit_1483 :: PROPblock_1**  
- **DOI:** 10.1016/j.fluid.2014.05.032  
- **System:** binary ethanol + water  
- **Data points:** 140  
- **Temperature range:** 292.95–448.15 K (includes isotherms at 348.15 K, near the target of 350 K)  
- **Pressure range:** 2450–40140 kPa (high-pressure data)  
- **Ethanol mole fraction range:** 0.0163–0.0946 (dilute ethanol region only)  

Representative data near 350 K (at 348.15 K):

| Ethanol x | P (kPa) | ρ (kg/m³) |
|-----------|---------|-----------|
| 0.0163 | 39600 | 982.3 |
| 0.0163 | 20750 | 974.7 |
| 0.0163 | 10980 | 970.6 |
| 0.0163 | 3220 | 967.1 |
| 0.0343 | 39860 | 974.7 |
| 0.0343 | 30850 | 971.3 |
| 0.0343 | 21160 | 967.5 |
| 0.0343 | 11590 | 963.5 |
| 0.073 | 39600 | 958.9 |
| 0.073 | 20870 | 950.8 |
| 0.073 | 11060 | 946.6 |
| 0.073 | 3330 | 943.0 |
| 0.0946 | 37790 | 948.7 |
| 0.0946 | 29730 | 945.4 |
| 0.0946 | 20870 | 941.6 |
| 0.0946 | 11390 | 937.4 |
| 0.0946 | 2730 | 933.7 |

**Note:** This dataset covers only dilute ethanol compositions (up to ~9.5 mol%) at elevated pressures (2.5–40 MPa). It does not provide atmospheric-pressure or full-composition-range density data.

### Other blocks from the initial search

- **GLOBlit_1742 :: PROPblock_1** — Upon inspection, this block is actually **methanol + water** (not ethanol + water) and is therefore not relevant to this query.  
- **GLOBlit_220** and **GLOBlit_2432** were also returned by the initial search as potential ethanol–water density blocks (with 810 and 565 data points respectively), but these were not inspected in this run, so their exact composition/temperature coverage cannot be confirmed here. They may contain broader composition-range data near 350 K.

**Chemistry note:** The inspected data show the expected trend: at 348.15 K, density decreases with increasing ethanol mole fraction (from ~982 kg/m³ at x = 0.0163 to ~949 kg/m³ at x = 0.0946 at comparable pressures), and increases with pressure at each composition, consistent with the lower density of ethanol relative to water and normal liquid compressibility behavior.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** GLOBlit_1483::PROPblock_1: 350 (near '…48.15 K (includes isotherms at 348.15 K, near the target of …') matches no inspected row/stat, database table, or other source of GLOBlit_1483::PROPblock_1
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_1483::PROPblock_1", nearest={"column": "temperature_k", "value": 350.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** GLOBlit_1483::PROPblock_1: 350 (near '…46 (dilute ethanol region only)    Representative data near …') matches no inspected row/stat, database table, or other source of GLOBlit_1483::PROPblock_1
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_1483::PROPblock_1", nearest={"column": "temperature_k", "value": 350.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** GLOBlit_1742::PROPblock_1: 810 (near '…tial search as potential ethanol–water density blocks (with …') matches no inspected row/stat, database table, or other source of GLOBlit_1742::PROPblock_1
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_1742::PROPblock_1", nearest={"column": "temperature_k", "value": 810.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** GLOBlit_1742::PROPblock_1: 565 (near '…rch as potential ethanol–water density blocks (with 810 and …') matches no inspected row/stat, database table, or other source of GLOBlit_1742::PROPblock_1
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_1742::PROPblock_1", nearest={"column": "temperature_k", "value": 565.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** GLOBlit_1742::PROPblock_1: 350 (near '…here. They may contain broader composition-range data near 3…') matches no inspected row/stat, database table, or other source of GLOBlit_1742::PROPblock_1
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_1742::PROPblock_1", nearest={"column": "temperature_k", "value": 350.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
Inspected so far: PROPblock_1

Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- GLOBlit_1483::PROPblock_1: 140, 292.95, 448.15, 348.15, 2450, 40140, 0.0163, 0.0946, 39600, 982.3, 20750, 974.7, 10980, 970.6, 3220, 967.1, 0.0343, 39860, 30850, 971.3, 21160, 967.5, 11590, 963.5, 0.073, 958.9, 20870, 950.8, 11060, 946.6, 3330, 943.0, 37790, 948.7, 29730, 945.4, 941.6, 11390, 937.4, 2730, 933.7, 9.5, 2.5, 40
- GLOBlit_1742::PROPblock_1: 348.15, 982, 0.0163, 949, 0.0946

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 6 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## LLM Response
<reasoning>
Let me analyze each flagged value:

1. "350" in "near the target of 350 K" — This is the user's requested target temperature from the instruction, not a database datum. I should label it as the user's query target.

2. "350" in "Representative data near 350 K" — Same as above, referring to the user's target temperature.

3. "810" in "with 810 and 565 data points" — These were from the initial search_blocks result summary (not from an inspection of GLOBlit_1742). The 810 and 565 values were attributed to GLOBlit_220 and GLOBlit_2432 respectively in the search_blocks summary. The grounding checker is flagging them as if they're from GLOBlit_1742::PROPblock_1, but they're actually from the search_blocks summary about GLOBlit_220 and GLOBlit_2432. However, the search_blocks result was truncated and I can't verify these numbers precisely. I should remove these specific counts since I can't verify them.

4. "565" — Same issue as 810.

5. "350" in "They may contain broader composition-range data near 350 K" — This is the user's target temperature again, not a database datum.

Let me fix the answer surgically:
- Replace "near the target of 350 K" with "near the user-requested target of ~350 K" to clarify provenance
- Replace "Representative data near 350 K" with "Representative data near the requested ~350 K target"
- Remove the specific data point counts (810, 565) for GLOBlit_220 and GLOBlit_2432 since they came from a truncated search result and weren't inspected
- Replace "near 350 K" at the end with "near the requested temperature"
</reasoning>

<answer>
**Binary ethanol–water mass density data in the ThermoML database:**

The search for binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) mass density (GLOBprop_1) blocks found the following confirmed result:

### Confirmed ethanol–water block

**GLOBlit_1483 :: PROPblock_1**  
- **DOI:** 10.1016/j.fluid.2014.05.032  
- **System:** binary ethanol + water  
- **Data points:** 140  
- **Temperature range:** 292.95–448.15 K (includes isotherms at 348.15 K, near the user-requested target of ~350 K)  
- **Pressure range:** 2450–40140 kPa (high-pressure data)  
- **Ethanol mole fraction range:** 0.0163–0.0946 (dilute ethanol region only)  

Representative data at 348.15 K (nearest isotherm to the requested ~350 K target):

| Ethanol x | P (kPa) | ρ (kg/m³) |
|-----------|---------|-----------|
| 0.0163 | 39600 | 982.3 |
| 0.0163 | 20750 | 974.7 |
| 0.0163 | 10980 | 970.6 |
| 0.0163 | 3220 | 967.1 |
| 0.0343 | 39860 | 974.7 |
| 0.0343 | 30850 | 971.3 |
| 0.0343 | 21160 | 967.5 |
| 0.0343 | 11590 | 963.5 |
| 0.073 | 39600 | 958.9 |
| 0.073 | 20870 | 950.8 |
| 0.073 | 11060 | 946.6 |
| 0.073 | 3330 | 943.0 |
| 0.0946 | 37790 | 948.7 |
| 0.0946 | 29730 | 945.4 |
| 0.0946 | 20870 | 941.6 |
| 0.0946 | 11390 | 937.4 |
| 0.0946 | 2730 | 933.7 |

**Note:** This dataset covers only dilute ethanol compositions (up to ~9.5 mol%) at elevated pressures (2.5–40 MPa). It does not provide atmospheric-pressure or full-composition-range density data.

### Other blocks from the initial search

- **GLOBlit_1742 :: PROPblock_1** — Upon inspection, this block is actually **methanol + water** (not ethanol + water) and is therefore not relevant to this query.  
- **GLOBlit_220** and **GLOBlit_2432** were also returned by the initial search as potential ethanol–water density blocks, but these were not inspected in this run, so their exact composition/temperature coverage and data point counts cannot be confirmed here.

**Chemistry note:** The inspected data show the expected trend: at 348.15 K, density decreases with increasing ethanol mole fraction (from ~982 kg/m³ at x = 0.0163 to ~949 kg/m³ at x = 0.0946 at comparable pressures), and increases with pressure at each composition, consistent with the lower density of ethanol relative to water and normal liquid compressibility behavior.
</answer>