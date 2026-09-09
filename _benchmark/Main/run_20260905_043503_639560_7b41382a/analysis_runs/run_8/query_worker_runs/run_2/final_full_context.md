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
Find additional excess molar enthalpy (HE, GLOBprop_17) data blocks for ethanol (GLOBcomp_2) + water (GLOBcomp_1) at 298.15 K with broader composition coverage than the 5 points in GLOBlit_2574::PROPblock_4. Also check if there are any other DOIs with HE data for this system at 298.15 K that were not found in the initial search.

## Instruction
Search for all blocks containing excess molar enthalpy (GLOBprop_17) for the binary system ethanol (GLOBcomp_2) + water (GLOBcomp_1). Include blocks at any temperature near 298.15 K (e.g., 293-303 K). List all DOIs, block numbers, number of data points, temperature ranges, and composition ranges. Exclude GLOBlit_2574, GLOBlit_528 which were already found. Check GLOBlit_6377 specifically - what DOI is it, how many data points does it have at 298.15 K?

## ID Catalog (from working memory)
[{"global_id": "GLOBcomp_2", "name": "ethanol", "registry_id": "64-17-5", "type": "comp"}, {"global_id": "GLOBcomp_1", "name": "water", "registry_id": "7732-18-5", "type": "comp"}, {"global_id": "GLOBprop_17", "name": "Excess molar enthalpy", "registry_id": "", "type": "prop"}]

## Assistant
<summary>Searching for all HE blocks for ethanol+water binary system near 298.15 K, excluding already-found literature. Will also check GLOBlit_6377 specifically.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_2', 'GLOBcomp_1'], property=GLOBprop_17, system_type=binary…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Fixing tool call syntax - need to use proper list format for temperature_range and correct JSON arguments.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_2', 'GLOBcomp_1'], property=GLOBprop_17, system_type=binary…)</tool_call>

## User
<tool_result>
**Summary:** 4 HE (excess molar enthalpy) blocks found for ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary across 3 DOIs, all at or near 298.15 K. **Caution:** PROPblock_4 from `10.1016/j.jct.2005.06.018 [GLOBlit_2574]` has a paper title referencing propanediols/butanediol, not ethanol — possible compound-mapping issue in the database.

### Block Summary

| DOI | Block | GLOBlit | Pts | T (K) | x range | Composition variable | Method | Notes |
|---|---|---|---|---|---|---|---|---|
| 10.1016/j.fluid.2007.06.007 | PROPblock_1 | GLOBlit_528 | 15 | 298.15 (constr) | x(ethanol) 0.000102–0.001551 | DOIcomp_7 (ethanol) | calvet_calorimetry | Very dilute ethanol in water |
| 10.1016/j.fluid.2007.06.007 | PROPblock_2 | GLOBlit_528 | 15 | 298.15 (constr) | x(water) 0.001021–0.015286 | DOIcomp_6 (water) | calvet_calorimetry | Very dilute water in ethanol |
| 10.1016/j.jct.2005.06.018 | PROPblock_4 | GLOBlit_2574 | 27 | 298.15–323.15 (var) | x(ethanol) 0.033–0.968 | DOIcomp_5 (ethanol) | calvet_ufactor_2 | ⚠️ Title mismatch — may not be ethanol |
| 10.1016/j.tca.2017.05.023 [GLOBlit_6377] | PROPblock_1 | GLOBlit_6
</tool_result>

## Assistant
<summary>Found 4 HE blocks across 3 DOIs. GLOBlit_6377 (10.1016/j.tca.2017.05.023) has PROPblock_1 but details were truncated. Need to inspect GLOBlit_6377::PROPblock_1 for full details including data points at 298.15 K.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_1, literature=GLOBlit_6377, nearest=T=298.15 K)</tool_call>

## User
<tool_result>
{
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'T=298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINEMENT_REQUIRED",
  "tool": "inspect_block_table"
}
</tool_result>

## Assistant
<summary>Fixing the nearest argument format for inspect_block_table - needs to be a dict.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_1, literature=GLOBlit_6377, nearest={'Temperature': 2…)</tool_call>

## User
<tool_result>
**inspect_block_table error** — nearest must be {"column": alias, "value": number, "k": 1..8}

| alias | n_finite | min | max |
|---|---|---|---|
| mole_fraction_ethanol | 1 | 0.102 | 0.102 |
| pressure_kpa | 1 | 100 | 100 |
| temperature_k | 1 | 298.15 | 298.15 |
| excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol | 1 | -0.70659 | -0.70659 |

Use these aliases in `where` / `nearest` with plain numbers.
</tool_result>

## Assistant
<summary>GLOBlit_6377::PROPblock_1 has only 1 data point: x(ethanol)=0.102, T=298.15 K, HE=-0.70659 kJ/mol. Very limited. Need to check GLOBlit_2574::PROPblock_4 for how many points are at 298.15 K specifically, since T ranges 298.15-323.15 K.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_4, literature=GLOBlit_2574, where=temperature_k = 2…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2005.06.018 [GLOBlit_2574] :: PROPblock_4 (binary: ethanol + water)
filter: where temperature_k = 298.15
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mole_fraction_<ethanol> | pressure_kpa | excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 0.0582 | 101.0 | -0.492 |
| BLKpoint_2 | 298.15 | 0.1198 | 101.0 | -0.747 |
| BLKpoint_3 | 298.15 | 0.15 | 101.0 | -0.77 |
| BLKpoint_4 | 298.15 | 0.1837 | 101.0 | -0.767 |
| BLKpoint_5 | 298.15 | 0.25 | 101.0 | -0.702 |
| BLKpoint_6 | 298.15 | 0.2981 | 101.0 | -0.649 |
| BLKpoint_7 | 298.15 | 0.4127 | 101.0 | -0.501 |
| BLKpoint_8 | 298.15 | 0.5 | 101.0 | -0.391 |
| BLKpoint_9 | 298.15 | 0.607 | 101.0 | -0.323 |
| BLKpoint_10 | 298.15 | 0.701 | 101.0 | -0.271 |
| BLKpoint_11 | 298.15 | 0.812 | 101.0 | -0.206 |
| BLKpoint_12 | 298.15 | 0.9 | 101.0 | -0.148 |

mode: complete — all 12 matched rows shown (block has 27)
stats (matched, n=12): temperature_k 298.15–298.15 (n=12); mole_fraction_ethanol 0.0582–0.9 (n=12); pressure_kpa 101.0–101.0 (n=12); excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol -0.77–-0.148 (n=12)
stats (full block, n=27): temperature_k 298.15–323.15 (n=27); mole_fraction_ethanol 0.033–0.968 (n=27); pressure_kpa 101.0–101.0 (n=27); excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol -0.77–-0.018 (n=27)
inspection_id: INSP_6d19d0a7d0d6
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<answer>
Here are all the excess molar enthalpy (HE) data blocks found for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system near 298.15 K in the ThermoML database:

## Summary of All HE Blocks Found

| DOI | GLOBlit | Block | Total pts | Pts at 298.15 K | x(ethanol) range | Notes |
|---|---|---|---|---|---|---|
| 10.1016/j.fluid.2007.06.007 | GLOBlit_528 | PROPblock_1 | 15 | 15 | 0.000102–0.001551 | Very dilute ethanol in water only |
| 10.1016/j.fluid.2007.06.007 | GLOBlit_528 | PROPblock_2 | 15 | 15 | x(water) 0.001021–0.015286 | Very dilute water in ethanol only |
| 10.1016/j.jct.2005.06.018 | GLOBlit_2574 | PROPblock_4 | 27 | **12** | 0.0582–0.9 | Broad composition coverage; ⚠️ paper title references propanediols/butanediol — possible compound-mapping issue |
| 10.1016/j.tca.2017.05.023 | GLOBlit_6377 | PROPblock_1 | 1 | 1 | 0.102 only | Single data point |

## Key Findings

### GLOBlit_2574::PROPblock_4 — Best Composition Coverage at 298.15 K
This block actually contains **12 data points at 298.15 K** (not 5 as previously noted), spanning x(ethanol) = 0.0582 to 0.9, at 101.0 kPa. The full data at 298.15 K:

| x(ethanol) | HE (kJ/mol) |
|---|---|
| 0.0582 | −0.492 |
| 0.1198 | −0.747 |
| 0.15 | −0.77 |
| 0.1837 | −0.767 |
| 0.25 | −0.702 |
| 0.2981 | −0.649 |
| 0.4127 | −0.501 |
| 0.5 | −0.391 |
| 0.607 | −0.323 |
| 0.701 | −0.271 |
| 0.812 | −0.206 |
| 0.9 | −0.148 |

The minimum HE is −0.77 kJ/mol at x(ethanol) ≈ 0.15, consistent with the well-known asymmetric exothermic mixing curve for ethanol + water. However, note the caution flag: the paper title in the database references propanediols/butanediol rather than ethanol, so this data should be verified against the original publication.

### GLOBlit_6377::PROPblock_1 — Single Point
DOI: 10.1016/j.tca.2017.05.023. Contains only **1 data point** at 298.15 K: x(ethanol) = 0.102, HE = −0.70659 kJ/mol, at 100 kPa. This is consistent with the GLOBlit_2574 data (which gives −0.747 kJ/mol at x = 0.1198, nearby).

### GLOBlit_528 — Infinite Dilution Region Only
The two blocks from this DOI cover only the very dilute ends (x < 0.002 for ethanol-dilute; x(water) < 0.016 for water-dilute), so they do not provide broad composition coverage.

### Conclusion
GLOBlit_2574::PROPblock_4 provides the broadest composition coverage with 12 points at 298.15 K spanning x(ethanol) = 0.0582–0.9. No additional DOIs beyond GLOBlit_528, GLOBlit_2574, and GLOBlit_6377 were found in the database for this system and property.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_VALUE** PROPblock_1 + PROPblock_2 + PROPblock_4: 0.000102 exists in PROPblock_1's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_6377::PROPblock_1", nearest={"column": "mole_fraction_<ethanol>", "value": 0.000102})`
- **UNGROUNDED_LITERAL** PROPblock_1 + PROPblock_2 + PROPblock_4: 0.001551 (near '…-|---|---|---|---|---|---| |   |   |   | 15 | 15 | 0.000102–…') matches no inspected row/stat, database table, or other source of PROPblock_1 + PROPblock_2 + PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_1", literature="<GLOBlit_N or DOI>")` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_1 + PROPblock_2 + PROPblock_4: 0.001021 (near '…te ethanol in water only | |   |   |   | 15 | 15 | x(water) …') matches no inspected row/stat, database table, or other source of PROPblock_1 + PROPblock_2 + PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_1", literature="<GLOBlit_N or DOI>")` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_1 + PROPblock_2 + PROPblock_4: 0.015286 (near '…l in water only | |   |   |   | 15 | 15 | x(water) 0.001021–…') matches no inspected row/stat, database table, or other source of PROPblock_1 + PROPblock_2 + PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_1", literature="<GLOBlit_N or DOI>")` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNINSPECTED_VALUE** PROPblock_1 + PROPblock_2 + PROPblock_4: 0.102 exists in PROPblock_1's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_6377::PROPblock_1", nearest={"column": "mole_fraction_<ethanol>", "value": 0.102})`
- **UNINSPECTED_BLOCK** GLOBlit_6377::PROPblock_1: GLOBlit_6377::PROPblock_1 is quoted with data values (298.15, 0.102, -0.70659, 100, …) but was never inspected in this run (values 298.15, 0.102, -0.70659, 100 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_6377::PROPblock_1")`
Inspected so far: PROPblock_4

Verified as grounded — correct as quoted, keep unchanged:
- GLOBlit_2574::PROPblock_4: 298.15, 0.0582, 0.9, 101.0, -0.492, 0.1198, -0.747, 0.15, -0.77, 0.1837, -0.767, 0.25, -0.702, 0.2981, -0.649, 0.4127, -0.501, 0.5, -0.391, 0.607, -0.323, 0.701, -0.271, 0.812, -0.206, -0.148
Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_1 + PROPblock_2 + PROPblock_4: 298.15, 15, 27, 0.0582, 0.9

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## Assistant
<summary>Running required inspections for GLOBlit_6377::PROPblock_1, GLOBlit_528::PROPblock_1, and GLOBlit_528::PROPblock_2 to ground all quoted values.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_6377::PROPblock_1)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.tca.2017.05.023 [GLOBlit_6377] :: PROPblock_1 (binary: ethanol + water)
filter: none (whole block)

| BLKpoint_id | mole_fraction_<ethanol> | pressure_kpa | temperature_k | excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol |
|---|---|---|---|---|
| BLKpoint_1 | 0.102 | 100 | 298.15 | -0.70659 |

mode: complete — all 1 matched rows shown (block has 1)
stats (matched, n=1): mole_fraction_ethanol 0.102–0.102 (n=1); pressure_kpa 100–100 (n=1); temperature_k 298.15–298.15 (n=1); excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol -0.70659–-0.70659 (n=1)
inspection_id: INSP_b04400bcb35b
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>GLOBlit_6377::PROPblock_1 inspected: 1 point, x(ethanol)=0.102, T=298.15 K, HE=-0.70659 kJ/mol. Now need to inspect GLOBlit_528 blocks for composition ranges.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_528::PROPblock_1)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.fluid.2007.06.007 [GLOBlit_528] :: PROPblock_1 (binary: ethanol + water)
filter: none (whole block)
block constraints: temperature_k = 298.15; pressure_kpa = 101.0

| BLKpoint_id | mole_fraction_<ethanol> | temperature_k | pressure_kpa | excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol |
|---|---|---|---|---|
| BLKpoint_1 | 0.000102 | 298.15 | 101.0 | -0.00104 |
| BLKpoint_2 | 0.000206 | 298.15 | 101.0 | -0.00208 |
| BLKpoint_3 | 0.000308 | 298.15 | 101.0 | -0.00312 |
| BLKpoint_5 | 0.000516 | 298.15 | 101.0 | -0.00518 |
| BLKpoint_6 | 0.000619 | 298.15 | 101.0 | -0.00621 |
| BLKpoint_7 | 0.000723 | 298.15 | 101.0 | -0.00722 |
| BLKpoint_8 | 0.000827 | 298.15 | 101.0 | -0.00826 |
| BLKpoint_9 | 0.000931 | 298.15 | 101.0 | -0.00927 |
| BLKpoint_10 | 0.001034 | 298.15 | 101.0 | -0.0103 |
| BLKpoint_12 | 0.001241 | 298.15 | 101.0 | -0.01233 |
| BLKpoint_13 | 0.001345 | 298.15 | 101.0 | -0.01334 |
| BLKpoint_15 | 0.001551 | 298.15 | 101.0 | -0.01537 |

mode: RDP — 12 of 15 matched rows shown (shape-preserving; block has 15). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
topology: excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol vs mole_fraction_ethanol: monotonic↓ | linear
stats (matched, n=15): mole_fraction_ethanol 0.000102–0.001551 (n=15); temperature_k 298.15–298.15 (n=15); pressure_kpa 101.0–101.0 (n=15); excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol -0.01537–-0.00104 (n=15)
inspection_id: INSP_e0e7d5bc600c
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>GLOBlit_528::PROPblock_1 inspected: 15 points, x(ethanol) 0.000102–0.001551, all at 298.15 K. Now need to inspect GLOBlit_528::PROPblock_2 for the water-dilute end.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_528::PROPblock_2)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.fluid.2007.06.007 [GLOBlit_528] :: PROPblock_2 (binary: ethanol + water)
filter: none (whole block)
block constraints: temperature_k = 298.15; pressure_kpa = 101.0

| BLKpoint_id | mole_fraction_<water> | temperature_k | pressure_kpa | excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol |
|---|---|---|---|---|
| BLKpoint_1 | 0.001021 | 298.15 | 101.0 | -0.00212 |
| BLKpoint_2 | 0.00205 | 298.15 | 101.0 | -0.00424 |
| BLKpoint_4 | 0.004102 | 298.15 | 101.0 | -0.00835 |
| BLKpoint_6 | 0.006155 | 298.15 | 101.0 | -0.01238 |
| BLKpoint_7 | 0.007179 | 298.15 | 101.0 | -0.01437 |
| BLKpoint_10 | 0.010239 | 298.15 | 101.0 | -0.02023 |
| BLKpoint_11 | 0.011252 | 298.15 | 101.0 | -0.02213 |
| BLKpoint_12 | 0.012264 | 298.15 | 101.0 | -0.02405 |
| BLKpoint_13 | 0.013276 | 298.15 | 101.0 | -0.0259 |
| BLKpoint_14 | 0.014283 | 298.15 | 101.0 | -0.02777 |
| BLKpoint_15 | 0.015286 | 298.15 | 101.0 | -0.02961 |

mode: RDP — 11 of 15 matched rows shown (shape-preserving; block has 15). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
topology: excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol vs mole_fraction_water: monotonic↓ | linear
stats (matched, n=15): mole_fraction_water 0.001021–0.015286 (n=15); temperature_k 298.15–298.15 (n=15); pressure_kpa 101.0–101.0 (n=15); excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol -0.02961–-0.00212 (n=15)
inspection_id: INSP_b146b18bf0c3
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<answer>
Here are all the excess molar enthalpy (HE) data blocks found for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system near 298.15 K in the ThermoML database:

## Summary of All HE Blocks Found

| DOI | GLOBlit | Block | Total pts | Pts at 298.15 K | Composition range | Notes |
|---|---|---|---|---|---|---|
| 10.1016/j.fluid.2007.06.007 | GLOBlit_528 | PROPblock_1 | 15 | 15 | x(ethanol) 0.000102–0.001551 | Very dilute ethanol in water only |
| 10.1016/j.fluid.2007.06.007 | GLOBlit_528 | PROPblock_2 | 15 | 15 | x(water) 0.001021–0.015286 | Very dilute water in ethanol only |
| 10.1016/j.jct.2005.06.018 | GLOBlit_2574 | PROPblock_4 | 27 | 12 | x(ethanol) 0.0582–0.9 | Broad composition coverage; ⚠️ paper title references propanediols/butanediol — possible compound-mapping issue |
| 10.1016/j.tca.2017.05.023 | GLOBlit_6377 | PROPblock_1 | 1 | 1 | x(ethanol) 0.102 only | Single data point |

## Detailed Findings

### GLOBlit_2574::PROPblock_4 — Best Composition Coverage at 298.15 K
This block contains **12 data points at 298.15 K**, spanning x(ethanol) = 0.0582 to 0.9, at 101.0 kPa:

| x(ethanol) | HE (kJ/mol) |
|---|---|
| 0.0582 | −0.492 |
| 0.1198 | −0.747 |
| 0.15 | −0.77 |
| 0.1837 | −0.767 |
| 0.25 | −0.702 |
| 0.2981 | −0.649 |
| 0.4127 | −0.501 |
| 0.5 | −0.391 |
| 0.607 | −0.323 |
| 0.701 | −0.271 |
| 0.812 | −0.206 |
| 0.9 | −0.148 |

The minimum HE is −0.77 kJ/mol at x(ethanol) ≈ 0.15, consistent with the well-known asymmetric exothermic mixing curve for ethanol + water. However, note the caution flag: the paper title in the database references propanediols/butanediol rather than ethanol, so this data should be verified against the original publication.

### GLOBlit_6377::PROPblock_1 — Single Point
DOI: 10.1016/j.tca.2017.05.023. Contains only **1 data point** at 298.15 K: x(ethanol) = 0.102, HE = −0.70659 kJ/mol, at 100 kPa. This is consistent with the GLOBlit_2574 data (which gives −0.747 kJ/mol at x = 0.1198, a nearby composition).

### GLOBlit_528::PROPblock_1 — Dilute Ethanol in Water
DOI: 10.1016/j.fluid.2007.06.007. Contains 15 points at 298.15 K covering x(ethanol) = 0.000102–0.001551 at 101.0 kPa. HE ranges from −0.00104 to −0.01537 kJ/mol. This block covers only the very dilute ethanol end, useful for deriving partial molar excess enthalpies at infinite dilution.

### GLOBlit_528::PROPblock_2 — Dilute Water in Ethanol
Same DOI. Contains 15 points at 298.15 K covering x(water) = 0.001021–0.015286 at 101.0 kPa. HE ranges from −0.00212 to −0.02961 kJ/mol. This block covers only the very dilute water-in-ethanol end.

### Conclusion
No additional DOIs beyond GLOBlit_528, GLOBlit_2574, and GLOBlit_6377 were found in the database for HE of ethanol + water. GLOBlit_2574::PROPblock_4 provides the broadest composition coverage with 12 points at 298.15 K spanning x(ethanol) = 0.0582–0.9. The GLOBlit_528 blocks complement this with high-resolution data in the infinite-dilution regions at both ends.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **MISATTRIBUTED_VALUE** GLOBlit_6377::PROPblock_1: -0.747 does not belong to GLOBlit_6377::PROPblock_1; it matches only GLOBlit_2574::PROPblock_4 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor -0.747 to GLOBlit_2574::PROPblock_4 — no new tool call needed`
- **MISATTRIBUTED_VALUE** GLOBlit_6377::PROPblock_1: 0.1198 does not belong to GLOBlit_6377::PROPblock_1; it matches only GLOBlit_2574::PROPblock_4 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 0.1198 to GLOBlit_2574::PROPblock_4 — no new tool call needed`
Inspected so far: PROPblock_1, PROPblock_2, PROPblock_4

Verified as grounded — correct as quoted, keep unchanged:
- PROPblock_1 + PROPblock_2 + PROPblock_4: 298.15, 15, 0.000102, 0.001551, 0.001021, 0.015286, 27, 0.0582, 0.9, 0.102
- GLOBlit_2574::PROPblock_4: 298.15, 0.0582, 0.9, 101.0, -0.492, 0.1198, -0.747, 0.15, -0.77, 0.1837, -0.767, 0.25, -0.702, 0.2981, -0.649, 0.4127, -0.501, 0.5, -0.391, 0.607, -0.323, 0.701, -0.271, 0.812, -0.206, -0.148
- GLOBlit_528::PROPblock_1: 15, 298.15, 0.000102, 0.001551, 101.0, -0.00104, -0.01537
- GLOBlit_528::PROPblock_2: 15, 298.15, 0.001021, 0.015286, 101.0, -0.00212, -0.02961
Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- GLOBlit_6377::PROPblock_1: 298.15, 0.102, -0.70659, 100

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## LLM Response
<answer>
Here are all the excess molar enthalpy (HE) data blocks found for the ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary system near 298.15 K in the ThermoML database:

## Summary of All HE Blocks Found

| DOI | GLOBlit | Block | Total pts | Pts at 298.15 K | Composition range | Notes |
|---|---|---|---|---|---|---|
| 10.1016/j.fluid.2007.06.007 | GLOBlit_528 | PROPblock_1 | 15 | 15 | x(ethanol) 0.000102–0.001551 | Very dilute ethanol in water only |
| 10.1016/j.fluid.2007.06.007 | GLOBlit_528 | PROPblock_2 | 15 | 15 | x(water) 0.001021–0.015286 | Very dilute water in ethanol only |
| 10.1016/j.jct.2005.06.018 | GLOBlit_2574 | PROPblock_4 | 27 | 12 | x(ethanol) 0.0582–0.9 | Broad composition coverage; ⚠️ paper title references propanediols/butanediol — possible compound-mapping issue |
| 10.1016/j.tca.2017.05.023 | GLOBlit_6377 | PROPblock_1 | 1 | 1 | x(ethanol) 0.102 only | Single data point |

## Detailed Findings

### GLOBlit_2574::PROPblock_4 — Best Composition Coverage at 298.15 K
This block contains **12 data points at 298.15 K**, spanning x(ethanol) = 0.0582 to 0.9, at 101.0 kPa:

| x(ethanol) | HE (kJ/mol) |
|---|---|
| 0.0582 | −0.492 |
| 0.1198 | −0.747 |
| 0.15 | −0.77 |
| 0.1837 | −0.767 |
| 0.25 | −0.702 |
| 0.2981 | −0.649 |
| 0.4127 | −0.501 |
| 0.5 | −0.391 |
| 0.607 | −0.323 |
| 0.701 | −0.271 |
| 0.812 | −0.206 |
| 0.9 | −0.148 |

The minimum HE is −0.77 kJ/mol at x(ethanol) ≈ 0.15, consistent with the well-known asymmetric exothermic mixing curve for ethanol + water. However, note the caution flag: the paper title in the database references propanediols/butanediol rather than ethanol, so this data should be verified against the original publication.

### GLOBlit_6377::PROPblock_1 — Single Point
DOI: 10.1016/j.tca.2017.05.023. Contains only **1 data point** at 298.15 K: x(ethanol) = 0.102, HE = −0.70659 kJ/mol, at 100 kPa. This is consistent with the GLOBlit_2574::PROPblock_4 data, which gives −0.747 kJ/mol at x = 0.1198 (a nearby but not identical composition).

### GLOBlit_528::PROPblock_1 — Dilute Ethanol in Water
DOI: 10.1016/j.fluid.2007.06.007. Contains 15 points at 298.15 K covering x(ethanol) = 0.000102–0.001551 at 101.0 kPa. HE ranges from −0.00104 to −0.01537 kJ/mol. This block covers only the very dilute ethanol end, useful for deriving partial molar excess enthalpies at infinite dilution.

### GLOBlit_528::PROPblock_2 — Dilute Water in Ethanol
Same DOI. Contains 15 points at 298.15 K covering x(water) = 0.001021–0.015286 at 101.0 kPa. HE ranges from −0.00212 to −0.02961 kJ/mol. This block covers only the very dilute water-in-ethanol end.

### Conclusion
No additional DOIs beyond GLOBlit_528, GLOBlit_2574, and GLOBlit_6377 were found in the database for HE of ethanol + water. GLOBlit_2574::PROPblock_4 provides the broadest composition coverage with 12 points at 298.15 K spanning x(ethanol) = 0.0582–0.9. The GLOBlit_528 blocks complement this with high-resolution data in the infinite-dilution regions at both ends.
</answer>