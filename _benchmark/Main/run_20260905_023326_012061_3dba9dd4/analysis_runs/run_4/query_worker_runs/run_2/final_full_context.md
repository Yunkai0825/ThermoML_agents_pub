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

## User
## Purpose
Find density data for binary mixture of water and ethanol at 298.15 K

## Instruction
Search for blocks containing mass density (GLOBprop_1) for the binary system water (CAS 7732-18-5) + ethanol (CAS 64-17-5) at approximately 298.15 K. Return DOIs, block numbers, compound IDs, and number of data points. Prefer blocks with many composition points covering full range x=0 to x=1.

## ID Catalog (from working memory)
[]

## Assistant
(syntax-rejected turn — malformed tool calls never executed; corrected on a later turn. Full detail in the run log.)

## User
(validation fired earlier — corrected)

## Assistant
<summary>Resolving water and ethanol compound IDs to their canonical GLOBcomp identifiers.</summary>
<tool_call>resolve_compound_ids(queries=['water 7732-18-5…, min_score=70, limit=5)</tool_call>

## User
<tool_result>
Both water and ethanol were successfully resolved to global compound IDs.

| Name | ID | Formula | SMILES |
|---|---|---|---|
| water | GLOBcomp_1 | H2O | O |
| ethanol | GLOBcomp_2 | C2H6O | CCO |

(GLOBcomp_5494 "ethanol-1-d" is a deuterated variant and can be ignored for standard water–ethanol queries.)
</tool_result>

## Assistant
<summary>Water = GLOBcomp_1, Ethanol = GLOBcomp_2. Now searching for binary blocks with mass density (GLOBprop_1) at ~298.15 K.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_1', 'GLOBcomp_2'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Correcting temperature_range to list format [295.0, 301.0] and re-searching for binary water+ethanol density blocks.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_1', 'GLOBcomp_2'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
**Summary:** 22 blocks found for binary water+ethanol mass density near 298.15 K. Several provide excellent isothermal data at exactly 298.15 K with broad composition coverage; others span a narrow T range that includes 298.15 K.

**Top candidates (sorted by relevance for 298.15 K isothermal density vs
</tool_result>

## Assistant
<summary>Got 22 blocks but result was truncated. Re-searching with same filters to get complete block listing with DOIs, block numbers, and data point counts.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_1', 'GLOBcomp_2'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
**Summary:** 22 binary water+ethanol density blocks found near 298.15 K, all scoring 100. All use GLOBcomp_1 + GLOBcomp_2 for GLOBprop_1 (Mass density, kg/m³), liquid phase.

| # | DOI | Block | Pts | T(K) range | Composition variable | Comp. range | ρ(kg/m³) range | GLOBlit |
|---|-----|-------|-----|-----------|----------------------|-------------|----------------|---------|
| 1 | 10.1016/j.fluid.2004.11.019 | PROPblock_2 | 810 | 298.15 | x(ethanol) | 0.003–0.7996 | 810.9–995.3 | GLOBlit_220 |
| 2 | 10.1016/j.fluid.2014.05.032 | PROPblock_1 | 140 | 292.95–448.15 | x(ethanol) | 0.0163–0.073 | 882.3–1006.1 | GLOBlit_1483 |
| 3 | 10.1016/j.jct.2004.07. [lit_num_id=null]
</tool_result>

## Assistant
<summary>Got partial list of 22 blocks. Top candidate is GLOBlit_220::PROPblock_2 with 810 pts at 298.15 K. Searching registry for complete listing and inspecting top block.</summary>
<tool_call>search_system_registry(compound=['GLOBcomp_1', 'GLOBcomp_2'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
**Summary:** 17 binary water+ethanol density blocks were found in the temperature window 295–301 K. Data point counts range from 2 to 810, spanning 17 distinct DOI/block combinations.

| # | DOI | Block | Points |
|---|-----|-------|--------|
| 1 | 10.1016/j.fluid.2004.11.019 [GLOBlit_220] | PROPblock_2 | 810 |
| 2 | 10.1016/j.fluid.2014.05.032 [GLOBlit_1483] | PROPblock_1 | 140 |
| 3 | 10.1016/j.jct.2004.07.019 [GLOBlit_2432] | PROPblock_2 | 565 |
| 4 | 10.1016/j.jct.2007.05.004 [GLOBlit_2825] | PROPblock_12 | 37 |
| 5 | 10.1016/j.jct.2011.10.009 [GLOBlit_3475] | PROPblock_3 | 70 |
| 6 | 10.1016/j.jct.2015.06.024 [GLOBlit_4415] | PROPblock_7 | 40 |
| 7 | 10.1016/j.jct.2018.02.022 [GLOBlit_5201] | PROPblock_19 | 244 |
| 8 | 10.1021/acs.jced.6b01058 [GLOBlit_7085] | PROPblock_7 | 12 |
| 9 | 10.1021/acs.jced.7b00299 [GLOBlit_7178] | PROPblock_10 | 2 |
| 10 | 10.1021/je020173z [GLOBlit_8050] | PROPblock_5 | 24 |
| 11 | 10.1021/je060335h [GLOBlit_9006] | PROPblock_1 | 164 |
| 12 | 10.1021/je4003515 [GLOBlit_10159] | PROPblock_7 | 23 |
| 13 | 10.1021/je600565m [GLOBlit_10699] | PROPblock_6 | 18 |
| 14 | 10.1021/je700300y [GLOBlit_10866] | PROPblock_7 | 84 |
| 15 | 10.1021/je800150h [GLOBlit_11136] | PROPblock_9 | 108 |
| 16 | 10.1021/je900064e [GLOBlit_11504] | PROPblock_6 | 10 |
| 17 | 10.1021/je900743e [GLOBlit_11792] | PROPblock_3 | 15
</tool_result>

## Assistant
<reasoning>
I now have a complete listing of 17 binary water+ethanol density blocks in the 295–301 K temperature window. Let me compile the answer with all the information requested: DOIs, block numbers, compound IDs, and number of data points, highlighting blocks with many composition points.

The top candidates for full composition coverage at 298.15 K are:
1. GLOBlit_220::PROPblock_2 — 810 points, x(ethanol) 0.003–0.7996
2. GLOBlit_2432::PROPblock_2 — 565 points
3. GLOBlit_5201::PROPblock_19 — 244 points
4. GLOBlit_9006::PROPblock_1 — 164 points
5. GLOBlit_1483::PROPblock_1 — 140 points

I have all the information needed to provide a complete answer.
</reasoning>

<answer>
## Binary Water + Ethanol Mass Density Data near 298.15 K

**Compounds:** Water (GLOBcomp_1, CAS 7732-18-5) + Ethanol (GLOBcomp_2, CAS 64-17-5)  
**Property:** Mass density (GLOBprop_1, kg/m³)  
**System type:** Binary, liquid phase

### Available Blocks (T ≈ 295–301 K)

17 data blocks were found. Sorted by number of data points:

| # | DOI | GLOBlit | Block | Data Points |
|---|-----|---------|-------|-------------|
| 1 | 10.1016/j.fluid.2004.11.019 | GLOBlit_220 | PROPblock_2 | 810 |
| 2 | 10.1016/j.jct.2004.07.019 | GLOBlit_2432 | PROPblock_2 | 565 |
| 3 | 10.1016/j.jct.2018.02.022 | GLOBlit_5201 | PROPblock_19 | 244 |
| 4 | 10.1021/je060335h | GLOBlit_9006 | PROPblock_1 | 164 |
| 5 | 10.1016/j.fluid.2014.05.032 | GLOBlit_1483 | PROPblock_1 | 140 |
| 6 | 10.1021/je800150h | GLOBlit_11136 | PROPblock_9 | 108 |
| 7 | 10.1021/je700300y | GLOBlit_10866 | PROPblock_7 | 84 |
| 8 | 10.1016/j.jct.2011.10.009 | GLOBlit_3475 | PROPblock_3 | 70 |
| 9 | 10.1016/j.jct.2015.06.024 | GLOBlit_4415 | PROPblock_7 | 40 |
| 10 | 10.1016/j.jct.2007.05.004 | GLOBlit_2825 | PROPblock_12 | 37 |
| 11 | 10.1021/je020173z | GLOBlit_8050 | PROPblock_5 | 24 |
| 12 | 10.1021/je4003515 | GLOBlit_10159 | PROPblock_7 | 23 |
| 13 | 10.1021/je600565m | GLOBlit_10699 | PROPblock_6 | 18 |
| 14 | 10.1021/je900743e | GLOBlit_11792 | PROPblock_3 | 15 |
| 15 | 10.1021/acs.jced.6b01058 | GLOBlit_7085 | PROPblock_7 | 12 |
| 16 | 10.1021/je900064e | GLOBlit_11504 | PROPblock_6 | 10 |
| 17 | 10.1021/acs.jced.7b00299 | GLOBlit_7178 | PROPblock_10 | 2 |

### Best Candidates for Full Composition Coverage

**GLOBlit_220::PROPblock_2** (810 points) is the richest dataset, with ethanol mole fraction ranging from 0.003 to 0.7996 at exactly 298.15 K, and density spanning 810.9–995.3 kg/m³. This block provides excellent composition resolution across most of the binary range.

**GLOBlit_2432::PROPblock_2** (565 points) and **GLOBlit_5201::PROPblock_19** (244 points) are also strong candidates with substantial composition coverage.

**Chemistry note:** The water–ethanol binary system shows a well-known non-ideal density behavior: density decreases monotonically from pure water (~997 kg/m³) toward pure ethanol (~785 kg/m³) at 298.15 K, but with a negative excess volume (volume contraction on mixing) that is most pronounced near x(ethanol) ≈ 0.2–0.3.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_BLOCK** PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10: PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10 is quoted with data values (810, 565, 244, 164, …) but was never inspected in this run (values 810, 140, 84, 40 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2"); inspect_block_table(block_number="GLOBlit_5201::PROPblock_19"); inspect_block_table(block_number="PROPblock_1", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_9", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_7", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_12", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_5", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_6", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_10", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** GLOBlit_220::PROPblock_2: GLOBlit_220::PROPblock_2 is quoted with data values (810, 0.003, 0.7996, 298.15, …) but was never inspected in this run (values 810, 0.003, 0.7996, 298.15 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2")`
- **UNINSPECTED_BLOCK** GLOBlit_2432::PROPblock_2: GLOBlit_2432::PROPblock_2 is quoted with data values (565, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2")`
- **UNINSPECTED_BLOCK** GLOBlit_5201::PROPblock_19: GLOBlit_5201::PROPblock_19 is quoted with data values (244, 997, 785, 298.15, …) but was never inspected in this run (values 997, 785, 298.15, 0.2 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_5201::PROPblock_19")`

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## Assistant
<summary>Inspecting top 3 blocks (GLOBlit_220::PROPblock_2, GLOBlit_2432::PROPblock_2, GLOBlit_5201::PROPblock_19) to ground the data values quoted in the answer.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_220::PROPblock_2, where=Temperature BETWE…)</tool_call>

## User
<tool_result>
**inspect_block_table error** — where filter error: unknown column alias 'Temperature'

| alias | n_finite | min | max |
|---|---|---|---|
| temperature_k | 810 | 298.15 | 348.15 |
| pressure_kpa | 810 | 100 | 40000 |
| mole_fraction_ethanol | 810 | 0.003 | 1 |
| mass_density_kg_m3 | 810 | 739.4 | 1012.7 |

Use these aliases in `where` / `nearest` with plain numbers.
</tool_result>

## Assistant
<summary>Got column aliases for GLOBlit_220::PROPblock_2. Now inspecting at T=298.15 K and inspecting the other two top blocks.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_220::PROPblock_2, where=temperature_k = 2…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.fluid.2004.11.019 [GLOBlit_220] :: PROPblock_2 (binary: ethanol + water)
filter: where temperature_k = 298.15

| BLKpoint_id | temperature_k | pressure_kpa | mole_fraction_<ethanol> | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 100 | 0.003 | 995.3 |
| BLKpoint_38 | 298.15 | 100 | 0.2502 | 918.5 |
| BLKpoint_43 | 298.15 | 100 | 0.4501 | 868.8 |
| BLKpoint_48 | 298.15 | 100 | 0.6967 | 825.2 |
| BLKpoint_54 | 298.15 | 100 | 1 | 785.7 |
| BLKpoint_55 | 298.15 | 10000 | 0.003 | 999.8 |
| BLKpoint_92 | 298.15 | 10000 | 0.2502 | 923.3 |
| BLKpoint_97 | 298.15 | 10000 | 0.4501 | 874.7 |
| BLKpoint_102 | 298.15 | 10000 | 0.6967 | 832.3 |
| BLKpoint_108 | 298.15 | 10000 | 1 | 794 |
| BLKpoint_109 | 298.15 | 20000 | 0.003 | 1004.2 |
| BLKpoint_146 | 298.15 | 20000 | 0.2502 | 928 |
| BLKpoint_151 | 298.15 | 20000 | 0.4501 | 880.4 |
| BLKpoint_156 | 298.15 | 20000 | 0.6967 | 839 |
| BLKpoint_162 | 298.15 | 20000 | 1 | 801.9 |
| BLKpoint_163 | 298.15 | 30000 | 0.003 | 1008.5 |
| BLKpoint_199 | 298.15 | 30000 | 0.2269 | 938.7 |
| BLKpoint_205 | 298.15 | 30000 | 0.4501 | 885.7 |
| BLKpoint_210 | 298.15 | 30000 | 0.6967 | 845.1 |
| BLKpoint_216 | 298.15 | 30000 | 1 | 808.9 |
| BLKpoint_217 | 298.15 | 40000 | 0.003 | 1012.7 |
| BLKpoint_253 | 298.15 | 40000 | 0.2269 | 942.9 |
| BLKpoint_259 | 298.15 | 40000 | 0.4501 | 890.8 |
| BLKpoint_264 | 298.15 | 40000 | 0.6967 | 851 |
| BLKpoint_270 | 298.15 | 40000 | 1 | 815.7 |

mode: RDP — 25 of 270 matched rows shown (shape-preserving; block has 810). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=270): temperature_k 298.15–298.15 (n=270); pressure_kpa 100–40000 (n=270); mole_fraction_ethanol 0.003–1 (n=270); mass_density_kg_m3 785.7–1012.7 (n=270)
stats (full block, n=810): temperature_k 298.15–348.15 (n=810); pressure_kpa 100–40000 (n=810); mole_fraction_ethanol 0.003–1 (n=810); mass_density_kg_m3 739.4–1012.7 (n=810)
inspection_id: INSP_689860323003
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_220::PROPblock_2: 810 total pts, 270 at 298.15 K, x(ethanol) 0.003–1, ρ 785.7–1012.7 kg/m³. Now inspecting the other two top blocks.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_2432::PROPblock_2)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2004.07.019 [GLOBlit_2432] :: PROPblock_2 (binary: ethanol + water)
filter: none (whole block)

| BLKpoint_id | temperature_k | pressure_kpa | molality_mol_kg_<ethanol> | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 410 | 0.09647 | -0.8568 |
| BLKpoint_6 | 298.15 | 410 | 0.94275 | -7.4996 |
| BLKpoint_12 | 298.15 | 14450 | 0.94273 | -7.71 |
| BLKpoint_19 | 298.15 | 14450 | 0.09647 | -0.874 |
| BLKpoint_31 | 298.15 | 14450 | 0.09647 | -0.874 |
| BLKpoint_42 | 298.18 | 29930 | 0.94271 | -7.9243 |
| BLKpoint_48 | 298.18 | 29930 | 0.94271 | -7.9243 |
| BLKpoint_49 | 298.18 | 29930 | 0.09646 | -0.9011 |
| BLKpoint_58 | 318.14 | 390 | 0.55206 | -4.6779 |
| BLKpoint_62 | 318.14 | 15370 | 0.55207 | -4.7543 |
| BLKpoint_63 | 318.14 | 390 | 0.08808 | -0.7809 |
| BLKpoint_71 | 318.14 | 390 | 0.08808 | -0.7809 |
| BLKpoint_74 | 318.14 | 15370 | 0.08808 | -0.7943 |
| BLKpoint_80 | 318.15 | 29980 | 0.55208 | -4.8174 |
| BLKpoint_85 | 318.15 | 29980 | 0.08809 | -0.8061 |
| BLKpoint_94 | 338.15 | 510 | 0.9427 | -8.0628 |
| BLKpoint_100 | 338.15 | 14860 | 0.94264 | -8.1024 |
| BLKpoint_113 | 338.15 | 510 | 0.09646 | -0.8794 |
| BLKpoint_119 | 338.15 | 14860 | 0.09646 | -0.8864 |
| BLKpoint_128 | 338.16 | 30230 | 0.55204 | -4.909 |
| BLKpoint_129 | 338.16 | 30230 | 0.10088 | -0.9335 |
| BLKpoint_138 | 373.17 | 2090 | 0.94262 | -8.8555 |
| BLKpoint_144 | 373.17 | 14860 | 0.94259 | -8.7729 |
| BLKpoint_150 | 373.17 | 30110 | 0.94256 | -8.7019 |
| BLKpoint_168 | 373.17 | 30110 | 0.94256 | -8.7019 |
| BLKpoint_169 | 373.17 | 2090 | 0.09645 | -0.9474 |
| BLKpoint_175 | 373.17 | 14860 | 0.09645 | -0.9386 |
| BLKpoint_181 | 373.17 | 30110 | 0.09645 | -0.9356 |
| BLKpoint_192 | 408.15 | 2040 | 0.94252 | -9.7809 |
| BLKpoint_198 | 408.15 | 14990 | 0.94247 | -9.585 |
| BLKpoint_204 | 408.15 | 29940 | 0.99979 | -9.9551 |
| BLKpoint_223 | 408.15 | 2040 | 0.09572 | -1.0313 |
| BLKpoint_229 | 408.15 | 14990 | 0.09572 | -1.0118 |
| BLKpoint_235 | 408.15 | 29940 | 0.09571 | -0.992 |
| BLKpoint_245 | 443.16 | 14970 | 0.99975 | -11.1138 |
| BLKpoint_251 | 443.16 | 30300 | 0.99973 | -10.7304 |
| BLKpoint_264 | 443.16 | 14970 | 0.0957 | -1.1033 |
| BLKpoint_270 | 443.16 | 30300 | 0.0957 | -1.0627 |
| BLKpoint_288 | 443.17 | 2110 | 0.09571 | -1.1352 |
| BLKpoint_292 | 443.17 | 2110 | 0.99977 | -11.4775 |
| BLKpoint_298 | 473.16 | 2780 | 0.9997 | -12.5432 |
| BLKpoint_304 | 473.16 | 14990 | 0.99967 | -12.0186 |
| BLKpoint_310 | 473.16 | 30050 | 0.99964 | -11.4895 |
| BLKpoint_311 | 473.16 | 2780 | 0.0957 | -1.2406 |
| BLKpoint_329 | 473.16 | 2780 | 0.0957 | -1.2406 |
| BLKpoint_335 | 473.16 | 14990 | 0.10419 | -1.2973 |
| BLKpoint_341 | 473.16 | 30050 | 0.10418 | -1.2416 |
| BLKpoint_352 | 498.15 | 3810 | 0.99959 | -13.5611 |
| BLKpoint_358 | 498.15 | 30190 | 0.99954 | -12.1289 |
| BLKpoint_371 | 498.15 | 3810 | 0.10418 | -1.4613 |
| BLKpoint_383 | 498.15 | 30190 | 0.10418 | -1.3031 |
| BLKpoint_394 | 498.16 | 15030 | 1.04067 | -13.3718 |
| BLKpoint_401 | 498.16 | 15030 | 0.10418 | -1.3877 |
| BLKpoint_412 | 523.14 | 5880 | 1.04065 | -15.3473 |
| BLKpoint_418 | 523.14 | 15560 | 1.04063 | -14.4002 |
| BLKpoint_424 | 523.14 | 30170 | 1.04062 | -13.3657 |
| BLKpoint_443 | 523.14 | 5880 | 0.10417 | -1.5874 |
| BLKpoint_449 | 523.14 | 15560 | 0.10417 | -1.4921 |
| BLKpoint_455 | 523.14 | 30170 | 0.10416 | -1.3907 |
| BLKpoint_466 | 548.16 | 8000 | 1.04058 | -17.0046 |
| BLKpoint_472 | 548.16 | 15960 | 1.04054 | -15.7466 |
| BLKpoint_478 | 548.16 | 30120 | 1.04051 | -14.2262 |
| BLKpoint_496 | 548.16 | 30120 | 1.04051 | -14.2262 |
| BLKpoint_497 | 548.16 | 8000 | 0.0881 | -1.4865 |
| BLKpoint_503 | 548.16 | 15960 | 0.0881 | -1.3838 |
| BLKpoint_509 | 548.16 | 30120 | 0.0881 | -1.2547 |
| BLKpoint_519 | 573.14 | 30090 | 1.04039 | -15.3285 |
| BLKpoint_525 | 573.14 | 30090 | 0.08809 | -1.3474 |
| BLKpoint_535 | 573.15 | 10150 | 1.04048 | -19.634 |
| BLKpoint_554 | 573.15 | 10150 | 0.0881 | -1.7035 |
| BLKpoint_560 | 573.15 | 18040 | 0.08809 | -1.5198 |
| BLKpoint_565 | 573.15 | 18040 | 1.04045 | -17.3814 |

mode: RDP — 72 of 565 matched rows shown (shape-preserving; block has 565). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=565): temperature_k 298.15–573.15 (n=565); pressure_kpa 390–30300 (n=565); molality_mol_kg_ethanol 0.08808–1.04067 (n=565); mass_density_kg_m3 -19.634–-0.7809 (n=565)
inspection_id: INSP_b3500349e479
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>GLOBlit_2432::PROPblock_2 has 565 pts but reports negative density values (likely excess/relative density) with molality as composition variable — not ideal for absolute density vs mole fraction. Now inspecting GLOBlit_5201::PROPblock_19.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_5201::PROPblock_19)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2018.02.022 [GLOBlit_5201] :: PROPblock_19 (binary: ethanol + water)
filter: none (whole block)
block constraints: pressure_kpa = 92.3

| BLKpoint_id | temperature_k | mole_fraction_<ethanol> | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 293.15 | 0.0024 | 92.3 | 997.039 |
| BLKpoint_23 | 293.15 | 0.7006 | 92.3 | 829.434 |
| BLKpoint_59 | 298.15 | 0.7006 | 92.3 | 825.07 |
| BLKpoint_95 | 303.15 | 0.7006 | 92.3 | 820.66 |
| BLKpoint_131 | 308.15 | 0.7006 | 92.3 | 816.2 |
| BLKpoint_145 | 293.15 | 0 | 92.3 | 998.429 |
| BLKpoint_146 | 298.15 | 0 | 92.3 | 997.267 |
| BLKpoint_147 | 303.15 | 0 | 92.3 | 995.867 |
| BLKpoint_148 | 308.15 | 0 | 92.3 | 994.252 |
| BLKpoint_149 | 293.15 | 1 | 92.3 | 789.547 |
| BLKpoint_150 | 298.15 | 1 | 92.3 | 785.26 |
| BLKpoint_151 | 303.15 | 1 | 92.3 | 780.941 |
| BLKpoint_152 | 308.15 | 1 | 92.3 | 776.592 |
| BLKpoint_160 | 293.15 | 0.1984 | 92.3 | 935.19 |
| BLKpoint_165 | 293.15 | 0.4495 | 92.3 | 873.57 |
| BLKpoint_183 | 298.15 | 0.1984 | 92.3 | 931.84 |
| BLKpoint_188 | 298.15 | 0.4495 | 92.3 | 869.34 |
| BLKpoint_206 | 303.15 | 0.1984 | 92.3 | 928.77 |
| BLKpoint_211 | 303.15 | 0.4495 | 92.3 | 865.03 |
| BLKpoint_229 | 308.15 | 0.1984 | 92.3 | 925.04 |
| BLKpoint_234 | 308.15 | 0.4495 | 92.3 | 860.66 |
| BLKpoint_244 | 308.15 | 0.929 | 92.3 | 785.46 |

mode: RDP — 22 of 244 matched rows shown (shape-preserving; block has 244). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=244): temperature_k 293.15–308.15 (n=244); mole_fraction_ethanol 0–1 (n=244); pressure_kpa 92.3–92.3 (n=244); mass_density_kg_m3 776.592–998.429 (n=244)
inspection_id: INSP_b49f3d6ec58f
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<answer>
## Binary Water + Ethanol Mass Density Data near 298.15 K

**Compounds:** Water (GLOBcomp_1, CAS 7732-18-5) + Ethanol (GLOBcomp_2, CAS 64-17-5)  
**Property:** Mass density (GLOBprop_1, kg/m³)  
**System type:** Binary, liquid phase

### Available Blocks (T ≈ 295–301 K)

17 data blocks were found in the ThermoML database. Sorted by number of data points:

| # | DOI | GLOBlit | Block | Data Points |
|---|-----|---------|-------|-------------|
| 1 | 10.1016/j.fluid.2004.11.019 | GLOBlit_220 | PROPblock_2 | 810 |
| 2 | 10.1016/j.jct.2004.07.019 | GLOBlit_2432 | PROPblock_2 | 565 |
| 3 | 10.1016/j.jct.2018.02.022 | GLOBlit_5201 | PROPblock_19 | 244 |
| 4 | 10.1021/je060335h | GLOBlit_9006 | PROPblock_1 | 164 |
| 5 | 10.1016/j.fluid.2014.05.032 | GLOBlit_1483 | PROPblock_1 | 140 |
| 6 | 10.1021/je800150h | GLOBlit_11136 | PROPblock_9 | 108 |
| 7 | 10.1021/je700300y | GLOBlit_10866 | PROPblock_7 | 84 |
| 8 | 10.1016/j.jct.2011.10.009 | GLOBlit_3475 | PROPblock_3 | 70 |
| 9 | 10.1016/j.jct.2015.06.024 | GLOBlit_4415 | PROPblock_7 | 40 |
| 10 | 10.1016/j.jct.2007.05.004 | GLOBlit_2825 | PROPblock_12 | 37 |
| 11 | 10.1021/je020173z | GLOBlit_8050 | PROPblock_5 | 24 |
| 12 | 10.1021/je4003515 | GLOBlit_10159 | PROPblock_7 | 23 |
| 13 | 10.1021/je600565m | GLOBlit_10699 | PROPblock_6 | 18 |
| 14 | 10.1021/je900743e | GLOBlit_11792 | PROPblock_3 | 15 |
| 15 | 10.1021/acs.jced.6b01058 | GLOBlit_7085 | PROPblock_7 | 12 |
| 16 | 10.1021/je900064e | GLOBlit_11504 | PROPblock_6 | 10 |
| 17 | 10.1021/acs.jced.7b00299 | GLOBlit_7178 | PROPblock_10 | 2 |

### Best Candidates for Full Composition Coverage

**GLOBlit_220::PROPblock_2** (810 total points) is the richest dataset. At exactly 298.15 K, there are 270 data points spanning x(ethanol) = 0.003–1 and pressures from 100 to 40000 kPa, with mass density ranging from 785.7 to 1012.7 kg/m³. At atmospheric pressure (100 kPa) and 298.15 K, representative values include:

| x(ethanol) | ρ (kg/m³) |
|------------|-----------|
| 0.003 | 995.3 |
| 0.2502 | 918.5 |
| 0.4501 | 868.8 |
| 0.6967 | 825.2 |
| 1 | 785.7 |

**GLOBlit_5201::PROPblock_19** (244 points) provides data at 92.3 kPa across four temperatures (293.15–308.15 K) with x(ethanol) = 0–1. At 298.15 K, representative values include:

| x(ethanol) | ρ (kg/m³) |
|------------|-----------|
| 0 | 997.267 |
| 0.1984 | 931.84 |
| 0.4495 | 869.34 |
| 0.7006 | 825.07 |
| 1 | 785.26 |

**Note on GLOBlit_2432::PROPblock_2** (565 points): This block uses molality (mol/kg) as the composition variable and reports negative density values (likely relative or excess density differences), so it is less suitable for obtaining absolute density as a function of mole fraction.

**Chemistry note:** Both inspected absolute-density datasets show the expected monotonic decrease in density from pure water (~997 kg/m³) toward pure ethanol (~785 kg/m³) at 298.15 K. The density drop is steepest at low ethanol mole fractions, consistent with the well-known negative excess volume (volume contraction on mixing) in this system, which is most pronounced near x(ethanol) ≈ 0.2–0.3.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10: 164 (near '…|   |   | 565 | | 3 |   |   |   | 244 | | 4 |   |   |   | 16…') matches no inspected row/stat, database table, or other source of PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_2", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 164.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNINSPECTED_VALUE** PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10: 140 exists in PROPblock_2's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2", nearest={"column": "pressure_kpa", "value": 140.0})`
- **UNGROUNDED_LITERAL** PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10: 108 (near '…|   |   | 164 | | 5 |   |   |   | 140 | | 6 |   |   |   | 10…') matches no inspected row/stat, database table, or other source of PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_2", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 108.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNINSPECTED_VALUE** PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10: 84 exists in PROPblock_2's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2", nearest={"column": "temperature_k", "value": 84.0})`
- **UNINSPECTED_VALUE** PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10: 37 exists in PROPblock_2's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2", nearest={"column": "temperature_k", "value": 37.0})`
- **UNGROUNDED_LITERAL** PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10: 24 (near '…|   |   | 40 | | 10 |   |   |   | 37 | | 11 |   |   |   | 24…') matches no inspected row/stat, database table, or other source of PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_2", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 24.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10: 13 (near '…| 37 | | 11 |   |   |   | 24 | | 12 |   |   |   | 23 | | 13 …') matches no inspected row/stat, database table, or other source of PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_2", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 13.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10: 17 (near '…| 15 | | 15 |   |   |   | 12 | | 16 |   |   |   | 10 | | 17 …') matches no inspected row/stat, database table, or other source of PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_2", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 17.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- … and 2 more of the same kinds — GLOBlit_2432::PROPblock_2: 997, 785
Inspected so far: PROPblock_19, PROPblock_2

Verified as grounded — correct as quoted, keep unchanged:
- GLOBlit_220::PROPblock_2: 810, 298.15, 270, 0.003, 100, 40000, 785.7, 1012.7, 995.3, 0.2502, 918.5, 0.4501, 868.8, 0.6967, 825.2
- GLOBlit_5201::PROPblock_19: 244, 92.3, 293.15, 308.15, 298.15, 997.267, 0.1984, 931.84, 0.4495, 869.34, 0.7006, 825.07, 785.26
Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_2 + PROPblock_19 + PROPblock_1 + PROPblock_9 + PROPblock_7 + PROPblock_3 + PROPblock_12 + PROPblock_5 + PROPblock_6 + PROPblock_10: 810, 565, 244, 70, 40, 23, 18, 14, 15, 16
- GLOBlit_2432::PROPblock_2: 565, 298.15, 0.2, 0.3

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## User
[HARD STOP] Iteration/time limit reached. Summarise ALL findings from tool results so far into a complete answer. Do NOT call any more tools.

## LLM Response
<answer>
## Binary Water + Ethanol Mass Density Data near 298.15 K

**Compounds:** Water (GLOBcomp_1, CAS 7732-18-5) + Ethanol (GLOBcomp_2, CAS 64-17-5)
**Property:** Mass density (GLOBprop_1, kg/m³)
**System type:** Binary, liquid phase

### Available Blocks (T ≈ 295–301 K)

17 data blocks were found in the ThermoML database. The data-point counts in the table below are registry-level counts (total points in each block across all temperatures and pressures, not only at 298.15 K) as returned by the `search_system_registry` tool:

| # | DOI | GLOBlit | Block | Total Data Points (registry) |
|---|-----|---------|-------|------------------------------|
| 1 | 10.1016/j.fluid.2004.11.019 | GLOBlit_220 | PROPblock_2 | 810 |
| 2 | 10.1016/j.jct.2004.07.019 | GLOBlit_2432 | PROPblock_2 | 565 |
| 3 | 10.1016/j.jct.2018.02.022 | GLOBlit_5201 | PROPblock_19 | 244 |
| 4 | 10.1021/je060335h | GLOBlit_9006 | PROPblock_1 | (not individually inspected) |
| 5 | 10.1016/j.fluid.2014.05.032 | GLOBlit_1483 | PROPblock_1 | (not individually inspected) |
| 6 | 10.1021/je800150h | GLOBlit_11136 | PROPblock_9 | (not individually inspected) |
| 7 | 10.1021/je700300y | GLOBlit_10866 | PROPblock_7 | (not individually inspected) |
| 8 | 10.1016/j.jct.2011.10.009 | GLOBlit_3475 | PROPblock_3 | 70 |
| 9 | 10.1016/j.jct.2015.06.024 | GLOBlit_4415 | PROPblock_7 | 40 |
| 10 | 10.1016/j.jct.2007.05.004 | GLOBlit_2825 | PROPblock_12 | (not individually inspected) |
| 11 | 10.1021/je020173z | GLOBlit_8050 | PROPblock_5 | (not individually inspected) |
| 12 | 10.1021/je4003515 | GLOBlit_10159 | PROPblock_7 | 23 |
| 13 | 10.1021/je600565m | GLOBlit_10699 | PROPblock_6 | 18 |
| 14 | 10.1021/je900743e | GLOBlit_11792 | PROPblock_3 | 15 |
| 15 | 10.1021/acs.jced.6b01058 | GLOBlit_7085 | PROPblock_7 | (not individually inspected) |
| 16 | 10.1021/je900064e | GLOBlit_11504 | PROPblock_6 | (not individually inspected) |
| 17 | 10.1021/acs.jced.7b00299 | GLOBlit_7178 | PROPblock_10 | (not individually inspected) |

Entries marked "(not individually inspected)" had their point counts returned by the registry search but were not separately inspected in this run; the three inspected blocks are detailed below.

### Best Candidates for Full Composition Coverage

**GLOBlit_220::PROPblock_2** (810 total points) is the richest dataset. At exactly 298.15 K, there are 270 data points spanning x(ethanol) = 0.003–1 and pressures from 100 to 40000 kPa, with mass density ranging from 785.7 to 1012.7 kg/m³. At atmospheric pressure (100 kPa) and 298.15 K, representative inspected values include:

| x(ethanol) | ρ (kg/m³) |
|------------|-----------|
| 0.003 | 995.3 |
| 0.2502 | 918.5 |
| 0.4501 | 868.8 |
| 0.6967 | 825.2 |
| 1 | 785.7 |

**GLOBlit_5201::PROPblock_19** (244 points) provides data at 92.3 kPa across four temperatures (293.15–308.15 K) with x(ethanol) = 0–1. At 298.15 K, representative inspected values include:

| x(ethanol) | ρ (kg/m³) |
|------------|-----------|
| 0 | 997.267 |
| 0.1984 | 931.84 |
| 0.4495 | 869.34 |
| 0.7006 | 825.07 |
| 1 | 785.26 |

**Note on GLOBlit_2432::PROPblock_2** (565 points): Inspection revealed this block uses molality (mol/kg) as the composition variable and reports negative density values (likely relative or excess density differences, ranging from −19.634 to −0.7809 kg/m³), so it is less suitable for obtaining absolute density as a function of mole fraction.

**Chemistry note:** Both inspected absolute-density datasets show the expected monotonic decrease in density from pure water (~997 kg/m³ at GLOBlit_5201) toward pure ethanol (~785 kg/m³) at 298.15 K. The density drop is steepest at low ethanol mole fractions, consistent with the well-known negative excess volume (volume contraction on mixing) in this system.
</answer>