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
Find pure-component surface tension and refractive index values for DMSO and water at 298.15 K

## Instruction
Search for pure-component data blocks for dimethyl sulfoxide (GLOBcomp_31) that report surface tension (GLOBprop_13) or refractive index (GLOBprop_7) near 298.15 K. Also search for pure water (GLOBcomp_1) surface tension and refractive index near 298.15 K. I need the pure-component endpoint values to complete RK fits of mixture data. Return DOIs, block numbers, and the measured values if possible.

## ID Catalog (from working memory)
[]

## Prior Context
Surface tension block GLOBlit_10766::PROPblock_9 covers x(DMSO)=0.0121-0.8945 but not pure endpoints. Refractive index block GLOBlit_10766::PROPblock_10 covers x(DMSO)=0.0121-0.7685 but not pure endpoints.

## Assistant
(syntax-rejected turn — malformed tool calls never executed; corrected on a later turn. Full detail in the run log.)

## User
(validation fired earlier — corrected)

## Assistant
<summary>Correcting tool call syntax. Searching for pure DMSO surface tension and refractive index, and pure water surface tension and refractive index near 298.15 K.</summary>
<tool_call>search_blocks(compound=GLOBcomp_31, property=GLOBprop_13, system_type=unary, temperature_rang…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Correcting temperature_range to list format and batching all four pure-component searches: DMSO surface tension, DMSO refractive index, water surface tension, water refractive index near 298.15 K.</summary>
<tool_call>search_blocks(compound=GLOBcomp_31, property=GLOBprop_13, system_type=unary, temperature_rang…)</tool_call>

## User
<tool_result>
**Summary:** Found 7 independent literature sources for pure DMSO surface tension, all containing data at 298.15 K. Values at 298.15 K range from 0.0417 to 0.0425 N/m, with most clustering around 0.0422–0.0428 N/m.

### Pure DMSO Surface Tension at 298.15 K

| DOI | Block | GLOBlit | Method | γ (N/m) | ±U (N/m) |
|-----|-------|---------|--------|---------|----------|
| 10.1016/j.jct.2009.06.021 | PROPblock_1 | GLOBlit_3114 | maximal_bubble_pressure | 0.0425 | 0.0004 |
| 10.1016/j.jct.2013.02.021 | PROPblock_1 | GLOBlit_3840 | pendant_drop_shape | 0.04278 | 0.00042 |
| 10.1016/j.jct.2013.04.009 | PROPblock_1 | GLOBlit_3869 | ring_tensiometer | 0.042179 | 0.001131 |
| 10.1016/j.jct.2014.06.005 | PROPblock_1 | GLOBlit_4186 | ring_tensiometer | 0.042282 | 0.001132 |
| 10.1016/j.jct.2016.06.004 | PROPblock_1 | GLOBlit_4715 | ring_tensiometer | 0.042426 | 0.000744 |
| 10.1021/je0497294 | PROPblock_10 | GLOBlit_8444 | pendant_drop_shape | 0.04209 | 0.00043 |
| 10.1021/je7001013 | PROPblock_1 | GLOBlit_10766 | bubblep_ufactor_8 | 0.0417 | 0.0022 |

All blocks: compound = GLOBcomp_31 (DMSO), property = GLOBprop_13 (surface_tension_liquidgas_n_m), unary system, liquid phase.
</tool_result>

## Assistant
<summary>Got 7 sources for pure DMSO surface tension at 298.15 K (0.0417–0.0428 N/m). Now searching for DMSO refractive index, water surface tension, and water refractive index near 298.15 K.</summary>
<tool_call>search_blocks(compound=GLOBcomp_31, property=GLOBprop_7, system_type=unary, temperature_range…)</tool_call>

## User
<tool_result>
**Summary:** Found 10 unary DMSO refractive index (Na D-line) blocks near 298.15 K, all in liquid phase. Single-point measurements at exactly 298.15 K report n_D values ranging from 1.4762 to 1.4775, providing good reference data.

| DOI | Block | GLOBlit | Pts | T range (K) | n_D range | n_D at 298.15 K | Notes |
|-----|-------|---------|-----|-------------|-----------|-----------------|-------|
| 10.1016/j.fluid.2013.05.001 | PROPblock_3 | GLOBlit_1246 | 1 | 298.15 | 1.4762 | 1.4762 | P=85.9 kPa |
| 10.1016/j.jct.2008.05.010 | PROPblock_11 | GLOBlit_2957 | 1 | 298.15 | 1.4771 | 1.4771 | P=101.325 kPa |
| 10.1016/j.jct.2013.04.022 | PROPblock_4 | GLOBlit_3879 | 1 | 298.15 | 1.4762 | 1.4762 | P=85.9 kPa |
| 10.1016/j.jct.2017.06.020 | PROPblock_12 | GLOBlit_5058 | 1 | 298.15 | 1.4767 | 1.4767 | P=101.3 kPa |
| 10.1016/j.tca.2014.11.010 | PROPblock_8 | GLOBlit_6204 | 1 | 298.15 | 1.4773 | 1.4773 | P=101.325 kPa |
| 10.1016/j.fluid.2010.01.002 | PROPblock_2 | GLOBlit_779 | 4 | 298.15–328.15 | 1.462–1.4737 | ~1.4737 (low end T) | R²=0.9930 |
| 10.1016/j.jct.2012.10.022 [GLOBlit_3755] | PROPblock_6 | GLO
</tool_result>

## Assistant
<summary>Got DMSO refractive index data (n_D ≈ 1.4762–1.4775 at 298.15 K). Now searching for pure water surface tension and refractive index near 298.15 K.</summary>
<tool_call>search_blocks(compound=GLOBcomp_1, property=GLOBprop_13, system_type=unary, temperature_range…)</tool_call>

## User
<tool_result>
**Summary:** 10 unary water blocks found reporting surface tension (liquid–gas) in the 295–301 K window, all with perfect relevance score. Four blocks give single-point values exactly at 298.15 K (γ ≈ 0.07135–0.072 N/m); six others span ranges that include 298.15 K.

| DOI | Block | GLOBlit | Pts | T range (K) | γ range (N/m) | Notes |
|-----|-------|---------|-----|-------------|---------------|-------|
| 10.1016/j.fluid.2009.07.010 | PROPblock_12 | GLOBlit_725 | 1 | 298.15 | 0.07135 | single point |
| 10.1016/j.fluid.2015.03.040 | PROPblock_33 | GLOBlit_1671 | 1 | 298.15 | 0.07194 | single point |
| 10.1016/j.fluid.2015.07.022 | PROPblock_3 | GLOBlit_1747 | 1 | 298.15 | 0.072 | single point |
| 10.1016/j.jct.2012.01.023 | PROPblock_12 | GLOBlit_3548 | 1 | 298.15 | 0.07135 | single point |
| 10.1016/j.fluid.2014.12.040 | PROPblock_6 | GLOBlit_1623 | 4 | 298.15–328.15 | 0.0669–0.07203 | includes 298.15 K |
| 10.1016/j.fluid.2007.05.029 | PROPblock_4 | GLOBlit_522 | 6 | 283.15–308.15 | 0.0702–0.0741 | spans 298.15 K |
| 10.1016/j.fluid.2012.01.014 | PROPblock_1 | GLOBlit_1065 | 3 | 293–313 | 0.0696–0.0728 | spans 298.15 K |
| 10.1016/j. [lit_num_id=null]
</tool_result>

## Assistant
<summary>Got water surface tension data (γ ≈ 0.07135–0.072 N/m at 298.15 K). Now searching for pure water refractive index near 298.15 K to complete the set.</summary>
<tool_call>search_blocks(compound=GLOBcomp_1, property=GLOBprop_7, system_type=unary, temperature_range=…)</tool_call>

## User
<tool_result>
**Summary:** Ten unary water blocks report refractive index (Na D-line) at ~298.15 K and ~101.325 kPa in the liquid phase. Values cluster tightly around **n_D = 1.3324–1.3330**, with one outlier at 1.333.

| DOI | Block | GLOBlit | T (K) | P (kPa) | n_D | Pts |
|-----|-------|---------|--------|----------|------|-----|
| 10.1016/j.fluid.2004.11.025 | PROPblock_1 | GLOBlit_226 | 298.15 | 101.325 | 1.3324 | 1 |
| 10.1016/j.fluid.2005.09.009 | PROPblock_5 | GLOBlit_306 | 298.15 | 101.325 | 1.3325 | 1 |
| 10.1016/j.fluid.2007.08.008 | PROPblock_5 | GLOBlit_560 | 298.15 | 101.325 | 1.3325 | 1 |
| 10.1016/j.fluid.2008.02.008 | PROPblock_37 | GLOBlit_604 | 298.15 | 101.325 | 1.3325 | 1 |
| 10.1016/j.fluid.2008.07.001 | PROPblock_7 | GLOBlit_645 | 298.15 | 101.325 | 1.3325 | 1 |
| 10.1016/j.fluid.2010.01.002 | PROPblock_17 | GLOBlit_779 | 298.15–328.15 | constr | 1.3282–1.3325 | 4 |
| 10.1016/j.fluid.2012.07.032 | PROPblock_1 | GLOBlit_1136 | 288.2–318.2 | constr | 1.3298–1.3334 | 3 |
| 10.1016/j.fluid.2012.09.038 | PROPblock_6 | GLOBlit_1161 | 298.2 | 101.325 | 1.3324 | 1 |
| 10.1016/j.fluid.2012.11.018 [GLOBlit_1182] | PROP
</tool_result>

## Assistant
<reasoning>
I now have all four sets of pure-component data needed:

1. **Pure DMSO surface tension at 298.15 K**: 0.0417–0.0428 N/m (7 sources)
2. **Pure DMSO refractive index at 298.15 K**: n_D ≈ 1.4762–1.4775 (10 sources)
3. **Pure water surface tension at 298.15 K**: γ ≈ 0.07135–0.072 N/m (10 sources)
4. **Pure water refractive index at 298.15 K**: n_D ≈ 1.3324–1.3330 (10 sources)

I can now assemble the final answer with representative values, DOIs, and block numbers.
</reasoning>

<answer>
## Pure-Component Surface Tension and Refractive Index at 298.15 K

### DMSO (GLOBcomp_31)

**Surface tension (GLOBprop_13)** — 7 independent ThermoML sources report γ at 298.15 K in the range **0.0417–0.04278 N/m**, with most values clustering around 0.0422–0.0428 N/m. Representative entries:

| DOI | Block | GLOBlit | Method | γ (N/m) | ±U (N/m) |
|-----|-------|---------|--------|---------|----------|
| 10.1016/j.jct.2009.06.021 | PROPblock_1 | GLOBlit_3114 | maximal bubble pressure | 0.0425 | 0.0004 |
| 10.1016/j.jct.2013.02.021 | PROPblock_1 | GLOBlit_3840 | pendant drop | 0.04278 | 0.00042 |
| 10.1016/j.jct.2013.04.009 | PROPblock_1 | GLOBlit_3869 | ring tensiometer | 0.042179 | 0.001131 |
| 10.1016/j.jct.2016.06.004 | PROPblock_1 | GLOBlit_4715 | ring tensiometer | 0.042426 | 0.000744 |
| 10.1021/je0497294 | PROPblock_10 | GLOBlit_8444 | pendant drop | 0.04209 | 0.00043 |
| 10.1021/je7001013 | PROPblock_1 | GLOBlit_10766 | bubble pressure | 0.0417 | 0.0022 |

**Refractive index, Na D-line (GLOBprop_7)** — 10 sources report n_D at 298.15 K in the range **1.4762–1.4775**. Representative entries:

| DOI | Block | GLOBlit | n_D at 298.15 K |
|-----|-------|---------|-----------------|
| 10.1016/j.jct.2008.05.010 | PROPblock_11 | GLOBlit_2957 | 1.4771 |
| 10.1016/j.tca.2014.11.010 | PROPblock_8 | GLOBlit_6204 | 1.4773 |
| 10.1016/j.jct.2017.06.020 | PROPblock_12 | GLOBlit_5058 | 1.4767 |
| 10.1016/j.fluid.2013.05.001 | PROPblock_3 | GLOBlit_1246 | 1.4762 |
| 10.1016/j.jct.2013.04.022 | PROPblock_4 | GLOBlit_3879 | 1.4762 |

---

### Water (GLOBcomp_1)

**Surface tension (GLOBprop_13)** — 10 sources report γ at 298.15 K in the range **0.07135–0.072 N/m**. Representative single-point entries at exactly 298.15 K:

| DOI | Block | GLOBlit | γ (N/m) |
|-----|-------|---------|---------|
| 10.1016/j.fluid.2009.07.010 | PROPblock_12 | GLOBlit_725 | 0.07135 |
| 10.1016/j.fluid.2015.03.040 | PROPblock_33 | GLOBlit_1671 | 0.07194 |
| 10.1016/j.fluid.2015.07.022 | PROPblock_3 | GLOBlit_1747 | 0.072 |
| 10.1016/j.jct.2012.01.023 | PROPblock_12 | GLOBlit_3548 | 0.07135 |

**Refractive index, Na D-line (GLOBprop_7)** — 10 sources report n_D at 298.15 K, tightly clustered around **1.3324–1.3330**. Representative entries:

| DOI | Block | GLOBlit | n_D at 298.15 K |
|-----|-------|---------|-----------------|
| 10.1016/j.fluid.2004.11.025 | PROPblock_1 | GLOBlit_226 | 1.3324 |
| 10.1016/j.fluid.2005.09.009 | PROPblock_5 | GLOBlit_306 | 1.3325 |
| 10.1016/j.fluid.2008.02.008 | PROPblock_37 | GLOBlit_604 | 1.3325 |
| 10.1016/j.fluid.2012.09.038 | PROPblock_6 | GLOBlit_1161 | 1.3324 |

---

### Summary for RK Endpoint Values

| Property | DMSO (x=1) | Water (x=0) |
|----------|-----------|-------------|
| Surface tension γ (N/m) | ~0.0422–0.0428 (consensus) | ~0.07135–0.072 |
| Refractive index n_D | ~1.4767–1.4773 (consensus) | ~1.3324–1.3325 |

These pure-component endpoint values can be combined with the mixture data from GLOBlit_10766 (PROPblock_9 for surface tension, PROPblock_10 for refractive index) to complete Redlich-Kister fits across the full DMSO–water composition range.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_BLOCK** PROPblock_1 + PROPblock_10: PROPblock_1 + PROPblock_10 is quoted with data values (0.0425, 0.0004, 0.04278, 0.00042, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_1", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_10", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_10: PROPblock_10 is quoted with data values (298.15, 1.4762, 1.4775, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_10", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_11 + PROPblock_8 + PROPblock_12 + PROPblock_3 + PROPblock_4: PROPblock_11 + PROPblock_8 + PROPblock_12 + PROPblock_3 + PROPblock_4 is quoted with data values (298.15, 1.4771, 1.4773, 1.4767, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_11", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_8", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_12", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_4", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_4: PROPblock_4 is quoted with data values (298.15, 0.07135, 0.072, 298.15, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_4", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_12 + PROPblock_33 + PROPblock_3: PROPblock_12 + PROPblock_33 + PROPblock_3 is quoted with data values (0.07135, 0.07194, 0.072, 0.07135, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_12", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_33", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_3: PROPblock_3 is quoted with data values (298.15, 1.3324, 1.3330, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_1 + PROPblock_5 + PROPblock_37 + PROPblock_6: PROPblock_1 + PROPblock_5 + PROPblock_37 + PROPblock_6 is quoted with data values (298.15, 1.3324, 1.3325, 1.3325, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_1", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_5", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_37", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_6", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_6: PROPblock_6 is quoted with data values (0.0422, 0.0428, 0.07135, 0.072, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_6", literature="<GLOBlit_N or DOI>")`

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## Assistant
<summary>Need to inspect representative blocks before quoting data. Starting with DMSO surface tension (GLOBlit_3840::PROPblock_1), DMSO refractive index (GLOBlit_2957::PROPblock_11), and water surface tension (GLOBlit_725::PROPblock_12).</summary>
<tool_call>inspect_block_table(block_number=PROPblock_1, literature=GLOBlit_3840, nearest=T=298.15 K)</tool_call>

## User
<tool_result>
{
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'T=298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINEMENT_REQUIRED",
  "tool": "inspect_block_table"
}
</tool_result>

## Assistant
<summary>Fixing nearest argument to dict format. Inspecting representative blocks for all four property/compound combinations.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_1, literature=GLOBlit_3840, nearest={'T': 298.15})</tool_call>

## User
<tool_result>
**inspect_block_table error** — nearest must be {"column": alias, "value": number, "k": 1..8}

| alias | n_finite | min | max |
|---|---|---|---|
| temperature_k | 5 | 293.15 | 313.15 |
| surface_tension_liquidgas_n_m | 5 | 0.04103 | 0.04336 |

Use these aliases in `where` / `nearest` with plain numbers.
</tool_result>

## Assistant
<summary>Fixing nearest format to {"column": "temperature_k", "value": 298.15, "k": 1}. Batching inspections for representative blocks across all four property/compound combinations.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_1, literature=GLOBlit_3840, nearest={'column': 'tempe…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2013.02.021 [GLOBlit_3840] :: PROPblock_1 (unary: dimethyl sulfoxide)
filter: nearest temperature_k ≈ 298.15 (k=1)

| BLKpoint_id | temperature_k | surface_tension_liquidgas_n_m |
|---|---|---|
| BLKpoint_2 | 298.15 | 0.04278 |

mode: nearest — 1 row(s) of 5 matched (block has 5)
bracket: exact row(s) at temperature_k = 298.15 exist in the matched set
topology: surface_tension_liquidgas_n_m vs temperature_k: monotonic↓ | linear
stats (matched, n=5): temperature_k 293.15–313.15 (n=5); surface_tension_liquidgas_n_m 0.04103–0.04336 (n=5)
inspection_id: INSP_e4b65cd8115a
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_3840::PROPblock_1 — DMSO surface tension at 298.15 K = 0.04278 N/m. Now inspecting DMSO refractive index, water surface tension, and water refractive index blocks.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_11, literature=GLOBlit_2957, nearest={'column': 'tempe…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2008.05.010 [GLOBlit_2957] :: PROPblock_11 (unary: dimethyl sulfoxide)
filter: nearest temperature_k ≈ 298.15 (k=1)

| BLKpoint_id | temperature_k | pressure_kpa | refractive_index_na_dline |
|---|---|---|---|
| BLKpoint_1 | 298.15 | 101.325 | 1.4771 |

mode: nearest — 1 row(s) of 1 matched (block has 1)
bracket: exact row(s) at temperature_k = 298.15 exist in the matched set
stats (matched, n=1): temperature_k 298.15–298.15 (n=1); pressure_kpa 101.325–101.325 (n=1); refractive_index_na_dline 1.4771–1.4771 (n=1)
inspection_id: INSP_3d7d879c463b
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_2957::PROPblock_11 — DMSO n_D at 298.15 K = 1.4771. Now inspecting water surface tension and water refractive index blocks.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_12, literature=GLOBlit_725, nearest={'column': 'tempe…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.fluid.2009.07.010 [GLOBlit_725] :: PROPblock_12 (unary: water)
filter: nearest temperature_k ≈ 298.15 (k=1)

| BLKpoint_id | temperature_k | surface_tension_liquidgas_n_m |
|---|---|---|
| BLKpoint_1 | 298.15 | 0.07135 |

mode: nearest — 1 row(s) of 1 matched (block has 1)
bracket: exact row(s) at temperature_k = 298.15 exist in the matched set
stats (matched, n=1): temperature_k 298.15–298.15 (n=1); surface_tension_liquidgas_n_m 0.07135–0.07135 (n=1)
inspection_id: INSP_cf6ea779f190
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## User
[HARD STOP] Iteration/time limit reached. Summarise ALL findings from tool results so far into a complete answer. Do NOT call any more tools.

## LLM Response
<answer>
## Pure-Component Surface Tension and Refractive Index at 298.15 K

### DMSO (GLOBcomp_31)

**Surface tension (GLOBprop_13)** — The `search_blocks` discovery found 7 independent ThermoML sources reporting pure DMSO surface tension at 298.15 K. The inspected representative block confirms:

| DOI | Block | GLOBlit | T (K) | γ (N/m) |
|-----|-------|---------|--------|---------|
| 10.1016/j.jct.2013.02.021 | PROPblock_1 | GLOBlit_3840 | 298.15 | 0.04278 |

The discovery search indicated values across the 7 sources range from approximately 0.0417 to 0.0428 N/m (aggregates from the search tool), but only the inspected value above (0.04278 N/m) is verified at source precision. Additional sources identified in the discovery (GLOBlit_3114, GLOBlit_3869, GLOBlit_4186, GLOBlit_4715, GLOBlit_8444, GLOBlit_10766) were not individually inspected in this run.

**Refractive index, Na D-line (GLOBprop_7)** — 10 sources were found. The inspected representative block confirms:

| DOI | Block | GLOBlit | T (K) | P (kPa) | n_D |
|-----|-------|---------|--------|---------|-----|
| 10.1016/j.jct.2008.05.010 | PROPblock_11 | GLOBlit_2957 | 298.15 | 101.325 | 1.4771 |

The discovery search indicated n_D values across sources range from approximately 1.4762 to 1.4775 at 298.15 K (search-level aggregates). Only the inspected value (1.4771) is verified at source precision.

---

### Water (GLOBcomp_1)

**Surface tension (GLOBprop_13)** — 10 sources were found. The inspected representative block confirms:

| DOI | Block | GLOBlit | T (K) | γ (N/m) |
|-----|-------|---------|--------|---------|
| 10.1016/j.fluid.2009.07.010 | PROPblock_12 | GLOBlit_725 | 298.15 | 0.07135 |

The discovery search indicated γ values at 298.15 K across sources range from approximately 0.07135 to 0.072 N/m (search-level aggregates). Additional sources (GLOBlit_1671, GLOBlit_1747, GLOBlit_3548, and others) were not individually inspected in this run.

**Refractive index, Na D-line (GLOBprop_7)** — 10 sources were found in the discovery search. The search-level aggregates indicated n_D values at 298.15 K cluster around 1.3324–1.3330. No individual water refractive index block was inspected in this run due to time constraints; these aggregate values from the search tool should be treated as indicative rather than verified at source precision. Representative sources identified include GLOBlit_226, GLOBlit_306, GLOBlit_560, GLOBlit_604, and GLOBlit_645.

---

### Summary for RK Endpoint Values

| Property | DMSO (x = 1) — inspected | Water (x = 0) — inspected |
|----------|--------------------------|---------------------------|
| Surface tension γ (N/m) | 0.04278 (GLOBlit_3840) | 0.07135 (GLOBlit_725) |
| Refractive index n_D | 1.4771 (GLOBlit_2957) | ~1.3324–1.3325 (search aggregate, not inspected) |

These pure-component endpoint values can be combined with the mixture data from GLOBlit_10766 (PROPblock_9 for surface tension covering x(DMSO) = 0.0121–0.8945, and PROPblock_10 for refractive index covering x(DMSO) = 0.0121–0.7685) to complete Redlich-Kister fits across the full DMSO–water composition range.
</answer>