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
Find density data for methanol + water binary mixture at 298.15 K to derive excess molar volume

## Instruction
Search for density (GLOBprop_1, mass density kg/m3) data for the binary mixture of methanol (CH3OH, CAS 67-56-1) + water (H2O, CAS 7732-18-5) at temperature near 298.15 K and atmospheric pressure. Need composition-dependent density data across the full mole fraction range. Return DOIs, block numbers, compound IDs, and data point counts.

## ID Catalog (from working memory)
[]

## Assistant
(syntax-rejected turn — malformed tool calls never executed; corrected on a later turn. Full detail in the run log.)

## User
(validation fired earlier — corrected)

## Assistant
<summary>Resolving compound IDs for methanol and water to begin the search for density data in binary mixtures.</summary>
<tool_call>resolve_compound_ids(queries=['methanol', 'wat…, min_score=70, limit=5)</tool_call>

## User
<tool_result>
Both compounds resolved with exact name matches.

| Compound | Global ID | Formula | SMILES | Score |
|----------|-----------|---------|--------|-------|
| methanol | GLOBcomp_4 | CH4O | CO | 100 |
| water | GLOBcomp_1 | H2O | O | 100 |
</tool_result>

## Assistant
<summary>Resolved: methanol=GLOBcomp_4, water=GLOBcomp_1. Now searching for density (GLOBprop_1) data in binary methanol+water mixtures near 298.15 K.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_4', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Fixing temperature_range format to list of floats [295, 302] and re-searching for density data in methanol+water binary mixtures.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_4', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
**Summary:** 9 mass density blocks found for binary methanol (GLOBcomp_4) + water (GLOBcomp_1) near 298.
</tool_result>

## Assistant
<summary>Got 9 blocks but need full details. Re-running search_blocks with proper parameters to get DOIs, block numbers, and data point counts for methanol+water density at 298.15 K.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_4', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
**Summary:** 9 density blocks found for methanol+water binary in the 295–302 K window. All match with score 100. The best candidates for 298.15 K with broad composition coverage are GLOBlit_2825 (x = 0–1), GLOBlit_8424 (x = 0.08–0.96), and GLOBlit_10866 (x = 0.087–0.964). Note GLOBlit_8254 has T = 346–398 K (likely only partially
</tool_result>

## Assistant
<summary>Have 9 density blocks for methanol+water binary. Top candidates: GLOBlit_2825, GLOBlit_8424, GLOBlit_10866 with broad composition coverage at 298.15 K. Need block-level details (PROPblock numbers, DOIs, data point counts). Will search the registry for complete listing.</summary>
<tool_call>search_system_registry(compound=['GLOBcomp_4', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
**Summary:** 8 binary methanol+water density (GLOBprop_1) blocks found with temperature ranges overlapping 295–302 K. All are liquid-phase mass density measurements from different literature sources, ranging from 9 to 596 data points.

| # | DOI | Block | GLOBlit | Points | T range (K) | Composition variable | P constraint (kPa) | Density range (kg/m³) |
|---|-----|-------|---------|--------|-------------|---------------------|--------------------|-----------------------|
| 1 | 10.1016/j.jct.2004.07.019 | PROPblock_1 | GLOBlit_2432 | 596 | [298.16, 573.15] | BLKvar_3: molality (0.07706–1.04694) | variable (390–30320) | −13.3065 to −0.4632 (relative) |
| 2 | 10.1016/j.jct.2007.05.004 | PROPblock_10 | GLOBlit_2825 | 39 | [293.15, 303.15] | BLKvar_2: mole_fraction water (0.0–1.0) | 101.0 | 782.48–998.2 |
| 3 | 10.1021/acs.jced.6b01058 | PROPblock_6 | GLOBlit_7085 | 12 | [298.15, 313.15] | BLKvar_2: mass_fraction methanol (0.04–0.16) | 85.0 | 963.68–989.97 |
| 4 | 10.1021/je034101z | PROPblock_4 | GLOBlit_8254 | 401 | [287.15, 417.15] | BLKvar_1: mole_fraction methanol (0.059–0.708) | variable (3721–29927) | 762.2–966.0 |
| 5 | 10.1021/je049691v | PROPblock_3 | GLOBlit_8424 | 180 | [283.15, 353.15] | BLKvar_2: mole_fraction water (0.08–0.9603) | — | 747.01–988.05 |
| 6 | 10.1021/je0600810 [GLOBlit_8869] | PROPblock_4 | GLOBlit
</tool_result>

## Assistant
<summary>Found 8+ density blocks for methanol+water binary. Best candidate for full composition coverage at 298.15 K is GLOBlit_2825::PROPblock_10 (39 pts, x=0–1, 101 kPa). Inspecting this block for actual data points.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_2825::PROPblock_10, where=T BETWEEN 297.5 A…)</tool_call>

## User
<tool_result>
**inspect_block_table error** — where filter error: unknown column alias 'T'

| alias | n_finite | min | max |
|---|---|---|---|
| temperature_k | 39 | 293.15 | 303.15 |
| mole_fraction_water | 39 | 0 | 1 |
| pressure_kpa | 39 | 101 | 101 |
| mass_density_kg_m3 | 39 | 782.48 | 998.2 |

Use these aliases in `where` / `nearest` with plain numbers.
</tool_result>

## Assistant
<summary>Got column aliases for GLOBlit_2825::PROPblock_10. Re-inspecting with correct alias "temperature_k" to filter for 298.15 K data points across the full mole fraction range.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_2825::PROPblock_10, where=temperature_k BET…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2007.05.004 [GLOBlit_2825] :: PROPblock_10 (binary: methanol + water)
filter: where temperature_k BETWEEN 297.5 AND 298.5
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mole_fraction_<water> | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_14 | 298.15 | 0 | 101.0 | 787.2 |
| BLKpoint_15 | 298.15 | 0.049 | 101.0 | 795.47 |
| BLKpoint_16 | 298.15 | 0.0993 | 101.0 | 804.11 |
| BLKpoint_17 | 298.15 | 0.1973 | 101.0 | 821.73 |
| BLKpoint_18 | 298.15 | 0.2983 | 101.0 | 840.79 |
| BLKpoint_19 | 298.15 | 0.3985 | 101.0 | 860.59 |
| BLKpoint_20 | 298.15 | 0.5003 | 101.0 | 881.69 |
| BLKpoint_21 | 298.15 | 0.5994 | 101.0 | 902.96 |
| BLKpoint_23 | 298.15 | 0.7986 | 101.0 | 947.17 |
| BLKpoint_24 | 298.15 | 0.8999 | 101.0 | 969.84 |
| BLKpoint_25 | 298.15 | 0.9512 | 101.0 | 982.53 |
| BLKpoint_26 | 298.15 | 1 | 101.0 | 997.05 |

mode: RDP — 12 of 13 matched rows shown (shape-preserving; block has 39). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=13): temperature_k 298.15–298.15 (n=13); mole_fraction_water 0–1 (n=13); pressure_kpa 101.0–101.0 (n=13); mass_density_kg_m3 787.2–997.05 (n=13)
stats (full block, n=39): temperature_k 293.15–303.15 (n=39); mole_fraction_water 0–1 (n=39); pressure_kpa 101.0–101.0 (n=39); mass_density_kg_m3 782.48–998.2 (n=39)
inspection_id: INSP_5d31e929df24
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<answer>
## Density Data for Methanol + Water Binary Mixture at 298.15 K

### Best Dataset: Full Composition Coverage

**Source:** DOI 10.1016/j.jct.2007.05.004 (GLOBlit_2825, PROPblock_10)

This block contains 13 data points at exactly 298.15 K and 101.0 kPa, spanning the full mole fraction range of water from 0 (pure methanol) to 1 (pure water). The composition variable is mole fraction of water (BLKvar_2).

| Mole fraction water | Mass density (kg/m³) |
|---|---|
| 0 | 787.2 |
| 0.049 | 795.47 |
| 0.0993 | 804.11 |
| 0.1973 | 821.73 |
| 0.2983 | 840.79 |
| 0.3985 | 860.59 |
| 0.5003 | 881.69 |
| 0.5994 | 902.96 |
| 0.7986 | 947.17 |
| 0.8999 | 969.84 |
| 0.9512 | 982.53 |
| 1 | 997.05 |

(12 of 13 matched rows shown via RDP shape-preserving selection; one additional point near x_water ≈ 0.7 exists in the block but was not displayed.)

### Additional Datasets Available

Several other blocks also contain methanol + water density data with temperature ranges overlapping 298.15 K:

| DOI | GLOBlit | Block | Total Points | T range (K) | Composition range | Notes |
|---|---|---|---|---|---|---|
| 10.1021/je049691v | GLOBlit_8424 | PROPblock_3 | 180 | 283.15–353.15 | x_water 0.08–0.9603 | Multi-temperature; broad composition |
| 10.1021/je034101z | GLOBlit_8254 | PROPblock_4 | 401 | 287.15–417.15 | x_methanol 0.059–0.708 | High-pressure data (3721–29927 kPa) |
| 10.1021/acs.jced.6b01058 | GLOBlit_7085 | PROPblock_6 | 12 | 298.15–313.15 | w_methanol 0.04–0.16 | Narrow mass fraction range |
| 10.1016/j.jct.2004.07.019 | GLOBlit_2432 | PROPblock_1 | 596 | 298.16–573.15 | Molality 0.077–1.047 | Relative density; variable pressure |

### Compound IDs
- **Methanol:** GLOBcomp_4 (CH₄O, CAS 67-56-1)
- **Water:** GLOBcomp_1 (H₂O, CAS 7732-18-5)
- **Property:** Mass density (GLOBprop_1, kg/m³)

### Chemistry Note
The GLOBlit_2825 dataset is ideal for deriving excess molar volume (V^E) at 298.15 K because it covers the complete composition range at constant atmospheric pressure. The density increases monotonically from 787.2 kg/m³ (pure methanol) to 997.05 kg/m³ (pure water). The methanol–water system is well known for exhibiting negative excess molar volumes across the entire composition range, reflecting strong hydrogen-bonding interactions and efficient molecular packing between the two components. The non-linear density–composition relationship visible in these data (the density does not follow a simple linear mixing rule) is the signature of this non-ideal volumetric behavior.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_VALUE** PROPblock_10: 0.7 exists in PROPblock_10's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_2825::PROPblock_10", nearest={"column": "mole_fraction_<water>", "value": 0.7})`
- **UNINSPECTED_BLOCK** PROPblock_3 + PROPblock_4 + PROPblock_6 + PROPblock_1: PROPblock_3 + PROPblock_4 + PROPblock_6 + PROPblock_1 is quoted with data values (180, 283.15, 353.15, 0.08, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_4", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_6", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_1", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_1: PROPblock_1 is quoted with data values (67, 7732, 298.15, 787.2, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_1", literature="<GLOBlit_N or DOI>")`
Inspected so far: PROPblock_10

Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_10: 13, 298.15, 101.0, 787.2, 0.049, 795.47, 0.0993, 804.11, 0.1973, 821.73, 0.2983, 840.79, 0.3985, 860.59, 0.5003, 881.69, 0.5994, 902.96, 0.7986, 947.17, 0.8999, 969.84, 0.9512, 982.53, 997.05

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## Assistant
<summary>Need to inspect the missing x_water ≈ 0.7 point from GLOBlit_2825::PROPblock_10, and remove uninspected numerical values from the additional datasets table (PROPblock_3, 4, 6, 1) to comply with grounding rules.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_2825::PROPblock_10, nearest={'column': 'mole_…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2007.05.004 [GLOBlit_2825] :: PROPblock_10 (binary: methanol + water)
filter: nearest mole_fraction_water ≈ 0.7 (k=1)
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mole_fraction_<water> | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_9 | 293.15 | 0.6997 | 101.0 | 928.45 |

mode: nearest — 1 row(s) of 39 matched (block has 39)
bracket: no matched row at mole_fraction_water = 0.7; nearest below BLKpoint_35 (0.6997), nearest above BLKpoint_10 (0.7986); 0 matched rows strictly inside that interval
stats (matched, n=39): temperature_k 293.15–303.15 (n=39); mole_fraction_water 0–1 (n=39); pressure_kpa 101.0–101.0 (n=39); mass_density_kg_m3 782.48–998.2 (n=39)
inspection_id: INSP_41f65b5c2ff4
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>The nearest x_water ≈ 0.7 point found is at 293.15 K, not 298.15 K. Need to find the missing 13th point at 298.15 K between x=0.5994 and x=0.7986. Inspecting with combined filter.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_2825::PROPblock_10, where=temperature_k BET…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2007.05.004 [GLOBlit_2825] :: PROPblock_10 (binary: methanol + water)
filter: where temperature_k BETWEEN 297.5 AND 298.5 AND mole_fraction_water BETWEEN 0.6 AND 0.8
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mole_fraction_<water> | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_22 | 298.15 | 0.6997 | 101.0 | 925.21 |
| BLKpoint_23 | 298.15 | 0.7986 | 101.0 | 947.17 |

mode: complete — all 2 matched rows shown (block has 39)
stats (matched, n=2): temperature_k 298.15–298.15 (n=2); mole_fraction_water 0.6997–0.7986 (n=2); pressure_kpa 101.0–101.0 (n=2); mass_density_kg_m3 925.21–947.17 (n=2)
stats (full block, n=39): temperature_k 293.15–303.15 (n=39); mole_fraction_water 0–1 (n=39); pressure_kpa 101.0–101.0 (n=39); mass_density_kg_m3 782.48–998.2 (n=39)
inspection_id: INSP_924974a9f3ca
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<answer>
## Density Data for Methanol + Water Binary Mixture at 298.15 K

### Best Dataset: Full Composition Coverage

**Source:** DOI 10.1016/j.jct.2007.05.004 (GLOBlit_2825, PROPblock_10)

This block contains 13 data points at exactly 298.15 K and 101.0 kPa, spanning the full mole fraction range of water from 0 (pure methanol) to 1 (pure water). The composition variable is mole fraction of water (BLKvar_2).

| Mole fraction water | Mass density (kg/m³) |
|---|---|
| 0 | 787.2 |
| 0.049 | 795.47 |
| 0.0993 | 804.11 |
| 0.1973 | 821.73 |
| 0.2983 | 840.79 |
| 0.3985 | 860.59 |
| 0.5003 | 881.69 |
| 0.5994 | 902.96 |
| 0.6997 | 925.21 |
| 0.7986 | 947.17 |
| 0.8999 | 969.84 |
| 0.9512 | 982.53 |
| 1 | 997.05 |

(All 13 matched rows at 298.15 K shown.)

### Additional Datasets Available

Several other blocks also contain methanol + water density data with temperature ranges that may include 298.15 K. These were identified in the registry search but their individual data rows were not inspected in this run:

- DOI 10.1021/je049691v (GLOBlit_8424, PROPblock_3) — multi-temperature dataset with broad composition coverage
- DOI 10.1021/je034101z (GLOBlit_8254, PROPblock_4) — multi-temperature, variable-pressure dataset
- DOI 10.1021/acs.jced.6b01058 (GLOBlit_7085, PROPblock_6) — narrow mass fraction range
- DOI 10.1016/j.jct.2004.07.019 (GLOBlit_2432, PROPblock_1) — relative density, variable pressure

Specific numerical details (point counts, exact temperature and composition ranges, density values) for these additional blocks were not inspected and are therefore not quoted here.

### Compound IDs
- **Methanol:** GLOBcomp_4 (CH₄O, CAS 67-56-1)
- **Water:** GLOBcomp_1 (H₂O, CAS 7732-18-5)
- **Property:** Mass density (GLOBprop_1, kg/m³)

### Chemistry Note
The GLOBlit_2825 dataset is ideal for deriving excess molar volume (V^E) at 298.15 K because it covers the complete composition range at constant atmospheric pressure. The density increases monotonically from 787.2 kg/m³ (pure methanol) to 997.05 kg/m³ (pure water). The methanol–water system is well known for exhibiting negative excess molar volumes across the entire composition range, reflecting strong hydrogen-bonding interactions and efficient molecular packing between the two components. The non-linear density–composition relationship visible in these data (the density does not follow a simple linear mixing rule) is the signature of this non-ideal volumetric behavior.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_BLOCK** PROPblock_1: PROPblock_1 is quoted with data values (67, 7732, 298.15, 787.2, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_1", literature="<GLOBlit_N or DOI>")`
Inspected so far: PROPblock_10

Verified as grounded — correct as quoted, keep unchanged:
- PROPblock_10: 13, 298.15, 101.0, 787.2, 0.049, 795.47, 0.0993, 804.11, 0.1973, 821.73, 0.2983, 840.79, 0.3985, 860.59, 0.5003, 881.69, 0.5994, 902.96, 0.6997, 925.21, 0.7986, 947.17, 0.8999, 969.84, 0.9512, 982.53, 997.05

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## User
[HARD STOP] Iteration/time limit reached. Summarise ALL findings from tool results so far into a complete answer. Do NOT call any more tools.

## LLM Response
<answer>
## Density Data for Methanol + Water Binary Mixture at 298.15 K

### Best Dataset: Full Composition Coverage

**Source:** DOI 10.1016/j.jct.2007.05.004 (GLOBlit_2825, PROPblock_10)

This block contains 13 data points at exactly 298.15 K and 101.0 kPa, spanning the full mole fraction range of water from 0 (pure methanol) to 1 (pure water). The composition variable is mole fraction of water (BLKvar_2).

| Mole fraction water | Mass density (kg/m³) |
|---|---|
| 0 | 787.2 |
| 0.049 | 795.47 |
| 0.0993 | 804.11 |
| 0.1973 | 821.73 |
| 0.2983 | 840.79 |
| 0.3985 | 860.59 |
| 0.5003 | 881.69 |
| 0.5994 | 902.96 |
| 0.6997 | 925.21 |
| 0.7986 | 947.17 |
| 0.8999 | 969.84 |
| 0.9512 | 982.53 |
| 1 | 997.05 |

(All 13 matched rows at 298.15 K shown.)

### Additional Datasets Available

Several other blocks also contain methanol + water density data with temperature ranges that may include 298.15 K. These were identified in the registry search but their individual data rows were not inspected in this run, so no specific numerical details are quoted for them:

- DOI 10.1021/je049691v (GLOBlit_8424, PROPblock_3) — multi-temperature dataset with broad composition coverage
- DOI 10.1021/je034101z (GLOBlit_8254, PROPblock_4) — multi-temperature, variable-pressure dataset
- DOI 10.1021/acs.jced.6b01058 (GLOBlit_7085, PROPblock_6) — narrow mass fraction range
- DOI 10.1016/j.jct.2004.07.019 (GLOBlit_2432, PROPblock_1) — relative density, variable pressure

### Compound IDs
- **Methanol:** GLOBcomp_4 (CH₄O, CAS 67-56-1)
- **Water:** GLOBcomp_1 (H₂O, CAS 7732-18-5)
- **Property:** Mass density (GLOBprop_1, kg/m³)

### Chemistry Note
The GLOBlit_2825 dataset is ideal for deriving excess molar volume (V^E) at 298.15 K because it covers the complete composition range at constant atmospheric pressure. The density increases monotonically from 787.2 kg/m³ (pure methanol) to 997.05 kg/m³ (pure water). The methanol–water system is well known for exhibiting negative excess molar volumes across the entire composition range, reflecting strong hydrogen-bonding interactions and efficient molecular packing between the two components. The non-linear density–composition relationship visible in these data (the density does not follow a simple linear mixing rule) is the signature of this non-ideal volumetric behavior.
</answer>