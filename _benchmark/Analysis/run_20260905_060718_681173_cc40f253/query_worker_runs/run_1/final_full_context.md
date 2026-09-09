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
Find binary mixture viscosity data for ethanol + water at 298.15 K (25°C)

## Instruction
Search for blocks containing dynamic viscosity (GLOBprop_4) measurements for binary mixtures of ethanol (CAS 64-17-5) and water (CAS 7732-18-5) at or near 298.15 K. Return DOIs, block numbers, temperature ranges, composition ranges, and number of data points. Prefer blocks with good composition coverage (many mole fractions across 0 to 1).

## ID Catalog (from working memory)
[]

## Assistant
(syntax-rejected turn — malformed tool calls never executed; corrected on a later turn. Full detail in the run log.)

## User
(validation fired earlier — corrected)

## Assistant
<summary>Resolving ethanol and water compound IDs to their canonical GLOBcomp identifiers.</summary>
<tool_call>resolve_compound_ids(queries=['ethanol CAS 64-…, min_score=70, limit=5)</tool_call>

## User
<tool_result>
Both compounds resolved successfully.

| Compound | Global ID | Formula | SMILES |
|----------|-----------|---------|--------|
| ethanol | GLOBcomp_2 | C2H6O | CCO |
| water | GLOBcomp_1 | H2O | O |
</tool_result>

## Assistant
<summary>Ethanol = GLOBcomp_2, Water = GLOBcomp_1. Now searching for binary mixture blocks with dynamic viscosity (GLOBprop_4) at ~298.15 K.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_2', 'GLOBcomp_1'], property=GLOBprop_4, system_type=binary,…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Re-emitting search_blocks with corrected temperature_range as a list of floats [295.0, 302.0].</summary>
<tool_call>search_blocks(compound=['GLOBcomp_2', 'GLOBcomp_1'], property=GLOBprop_4, system_type=binary,…)</tool_call>

## User
<tool_result>
**Summary:** 10 binary ethanol+water dynamic viscosity blocks found near 298.15 K, all scoring 100. They span various composition variables (mole fraction, mass fraction, molality) and temperature ranges within or overlapping [295–302 K].

| # | DOI | Block | GLOBlit | Pts (raw/kept) | Composition var | T range (K) | η range (Pa·s) |
|---|-----|-------|---------|----------------|-----------------|-------------|----------------|
| 1 | 10.1016/j.jct.2007.05.004 | PROPblock_11 | GLOBlit_2825 | 37/17 | x(water) 0–1 | 293.15–303.15 | 0.000797–0.002705 |
| 2 | 10.1016/j.jct.2018.02.022 | PROPblock_21 | GLOBlit_5201 | 100/14 | x(ethanol) 0.0201–0.929 | 293.15–303.15 | 0.0009816–0.0028641 |
| 3 | 10.1021/acs.jced.7b00299 | PROPblock_11 | GLOBlit_7178 | 2/2 | molality (constrained) | 298.15–303.15 | 0.001992–0.002367 |
| 4 | 10.1021/acs.jced.8b00086 | PROPblock_47 | GLOBlit_7448 | 6/6 | w(water) 0.206–0.508 | constrained | 0.001676–0.002235 |
| 5 | 10.1021/acs.jced.8b00939 | PROPblock_18 | GLOBlit_7676 | 9/9 | w(water) 0.061–0.62 | constrained | 0.00131–0.00234 |
| 6 | 10.1021/je4003515 | PROPblock_8 | GLOBlit_10159 | 25/14 | b(ethanol) 14–22 | 293.15–313.15 | 0.00144–0.0029 |
| 7 | 10.1021/je600565m | PROPblock_5 | GLOBlit_10699 |
</tool_result>

## Assistant


<reasoning>
The user wants binary mixture viscosity data for ethanol + water at 298.15 K. I have 10 blocks found. Let me look at the results more carefully. The table seems truncated at block 7. Let me compile what I have and identify the best blocks with good composition coverage.

From the results:
1. GLOBlit_2825, PROPblock_11 - 37 raw/17 kept points, x(water) 0–1, T 293.15–303.15 K - good composition coverage
2. GLOBlit_5201, PROPblock_21 - 100 raw/14 kept points, x(ethanol) 0.0201–0.929, T 293.15–303.15 K - good coverage
3. GLOBlit_7178, PROPblock_11 - only 2 points, molality constrained - limited
4. GLOBlit_7448, PROPblock_47 - 6 points, w(water) 0.206–0.508 - partial coverage
5. GLOBlit_7676, PROPblock_18 - 9 points, w(water) 0.061–0.62 - partial coverage
6. GLOBlit_10159, PROPblock_8 - 25 raw/14 kept, molality basis - decent coverage
7. GLOBlit_10699, PROPblock_5 - truncated

I should inspect the best blocks. Let me inspect the top two blocks that have the best composition coverage: GLOBlit_2825::PROPblock_11 and GLOBlit_5201::PROPblock_21. Let me inspect them to get actual data at 298.15 K.

Actually, I have 3 tool calls max total (including resolve_*), and I've already used 2 (resolve_compound_ids and search_blocks). I have 1 call left. But wait - the instruction says "Max 3 tool calls total (including resolve_*) for ordinary searches." Let me use my remaining call wisely.

Actually, looking more carefully at the rules: "Max 3 tool calls total (including resolve_*) for ordinary searches." I've used resolve_compound_ids (1) and search_blocks (1, though there were validation rejections). That's 2 successful calls. I can do 1 more.

Let me inspect the best block - GLOBlit_2825::PROPblock_11 which has x(water) 0-1 coverage and 37 raw points.

Wait, but the instruction says to "Return DOIs, block numbers, temperature ranges, composition ranges, and number of data points." This is a listing/discovery question, not a deep data inspection question. I already have the information needed from the search_blocks results. Let me just compile the answer from what I have.

The results are partially truncated (blocks 7-10 are cut off), but I have enough information to provide a comprehensive answer with the blocks shown.

Let me provide the answer with what I have. I should note the truncation.
</reasoning>

<answer>

## Binary Mixture Viscosity Data: Ethanol + Water at ~298.15 K

Ten data blocks were found in the ThermoML database containing dynamic viscosity measurements for binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) mixtures near 298.15 K. Below are the blocks with the most detail available:

| # | DOI | Block | GLOBlit | Raw/Kept Pts | Composition Variable | Composition Range | T Range (K) | η Range (Pa·s) |
|---|-----|-------|---------|-------------|---------------------|-------------------|-------------|----------------|
| 1 | 10.1016/j.jct.2007.05.004 | PROPblock_11 | GLOBlit_2825 | 37/17 | x(water), 0–1 | 293.15–303.15 | 0.000797–0.002705 |
| 2 | 10.1016/j.jct.2018.02.022 | PROPblock_21 | GLOBlit_5201 | 100/14 | x(ethanol), 0.0201–0.929 | 293.15–303.15 | 0.0009816–0.0028641 |
| 3 | 10.1021/acs.jced.7b00299 | PROPblock_11 | GLOBlit_7178 | 2/2 | molality (constrained) | 298.15–303.15 | 0.001992–0.002367 |
| 4 | 10.1021/acs.jced.8b00086 | PROPblock_47 | GLOBlit_7448 | 6/6 | w(water), 0.206–0.508 | constrained at 298.15 | 0.001676–0.002235 |
| 5 | 10.1021/acs.jced.8b00939 | PROPblock_18 | GLOBlit_7676 | 9/9 | w(water), 0.061–0.62 | constrained at 298.15 | 0.00131–0.00234 |
| 6 | 10.1021/je4003515 | PROPblock_8 | GLOBlit_10159 | 25/14 | b(ethanol), 14–22 mol/kg | 293.15–313.15 | 0.00144–0.0029 |
| 7 | 10.1021/je600565m | PROPblock_5 | GLOBlit_10699 | (truncated) | — | — | — |

**Blocks with best composition coverage:**

- **GLOBlit_2825 / PROPblock_11** (DOI: 10.1016/j.jct.2007.05.004) — 37 raw data points spanning the full mole-fraction range of water from 0 to 1, at temperatures 293.15–303.15 K. This block offers the widest composition sweep across the entire binary.

- **GLOBlit_5201 / PROPblock_21** (DOI: 10.1016/j.jct.2018.02.022) — 100 raw data points with ethanol mole fraction from 0.0201 to 0.929, at 293.15–303.15 K. This is the largest dataset by raw point count and covers nearly the full composition range.

- **GLOBlit_7676 / PROPblock_18** (DOI: 10.1021/acs.jced.8b00939) — 9 points at a constrained temperature (298.15 K), with water mass fraction 0.061–0.62, providing moderate coverage at the exact target temperature.

**Chemistry note:** The ethanol–water system is well known for exhibiting a pronounced viscosity maximum near x(ethanol) ≈ 0.3 at 298.15 K, where hydrogen-bonding network restructuring between ethanol and water leads to enhanced intermolecular friction. The viscosity values across these blocks range from ~0.0008 Pa·s (near pure components) up to ~0.0029 Pa·s (near the maximum), consistent with this behavior.

</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_BLOCK** PROPblock_11 + PROPblock_21 + PROPblock_47 + PROPblock_18 + PROPblock_8 + PROPblock_5: PROPblock_11 + PROPblock_21 + PROPblock_47 + PROPblock_18 + PROPblock_8 + PROPblock_5 is quoted with data values (37, 293.15, 303.15, 0.000797, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_11", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_21", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_47", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_18", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_8", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_5", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_11: PROPblock_11 is quoted with data values (37, 293.15, 303.15, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_11", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_21: PROPblock_21 is quoted with data values (100, 0.0201, 0.929, 293.15, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_21", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_18: PROPblock_18 is quoted with data values (298.15, 0.061, 0.62, 0.3, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_18", literature="<GLOBlit_N or DOI>")`

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## Assistant
<summary>Need to inspect key blocks to ground data values. Will inspect the top blocks with best composition coverage: GLOBlit_2825::PROPblock_11 and GLOBlit_5201::PROPblock_21, plus GLOBlit_7676::PROPblock_18.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_11, literature=GLOBlit_2825, nearest=Temperature = 298…)</tool_call>

## User
<tool_result>
{
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'Temperature = 298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINEMENT_REQUIRED",
  "tool": "inspect_block_table"
}
</tool_result>

## Assistant
<summary>Fixing inspect_block_table call syntax. nearest must be a dict. Batching inspections of the three key blocks.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_11, literature=GLOBlit_2825, nearest={'Temperature': 2…)</tool_call>

## User
<tool_result>
**inspect_block_table error** — nearest must be {"column": alias, "value": number, "k": 1..8}

| alias | n_finite | min | max |
|---|---|---|---|
| temperature_k | 37 | 293.15 | 303.15 |
| mole_fraction_water | 37 | 0 | 1 |
| pressure_kpa | 37 | 101 | 101 |
| viscosity_pa_s | 37 | 0.000797 | 0.002705 |

Use these aliases in `where` / `nearest` with plain numbers.
</tool_result>

## Assistant
<summary>Got column aliases for GLOBlit_2825::PROPblock_11. Now inspecting data rows at T=298.15 K for the three key blocks.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_11, literature=GLOBlit_2825, nearest={'column': 'tempe…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2007.05.004 [GLOBlit_2825] :: PROPblock_11 (binary: ethanol + water)
filter: nearest temperature_k ≈ 298.15 (k=8)
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mole_fraction_<water> | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_14 | 298.15 | 0 | 101.0 | 0.001082 |
| BLKpoint_15 | 298.15 | 0.0501 | 101.0 | 0.001153 |
| BLKpoint_16 | 298.15 | 0.0986 | 101.0 | 0.001232 |
| BLKpoint_17 | 298.15 | 0.1961 | 101.0 | 0.00138 |
| BLKpoint_18 | 298.15 | 0.2961 | 101.0 | 0.001531 |
| BLKpoint_19 | 298.15 | 0.3991 | 101.0 | 0.001659 |
| BLKpoint_20 | 298.15 | 0.5989 | 101.0 | 0.002115 |
| BLKpoint_21 | 298.15 | 0.6991 | 101.0 | 0.002275 |

mode: nearest — 8 row(s) of 37 matched (block has 37)
bracket: exact row(s) at temperature_k = 298.15 exist in the matched set
stats (matched, n=37): temperature_k 293.15–303.15 (n=37); mole_fraction_water 0–1 (n=37); pressure_kpa 101.0–101.0 (n=37); viscosity_pa_s 0.000797–0.002705 (n=37)
inspection_id: INSP_5ff8f4b75fda
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_2825::PROPblock_11 - got 8 rows at 298.15 K with x(water) 0–0.6991. Now inspecting GLOBlit_5201::PROPblock_21 and GLOBlit_7676::PROPblock_18.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_21, literature=GLOBlit_5201, nearest={'column': 'tempe…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2018.02.022 [GLOBlit_5201] :: PROPblock_21 (binary: ethanol + water)
filter: nearest temperature_k ≈ 298.15 (k=8)
block constraints: pressure_kpa = 92.3

| BLKpoint_id | temperature_k | mole_fraction_<ethanol> | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_24 | 298.15 | 0.0201 | 92.3 | 0.001098 |
| BLKpoint_25 | 298.15 | 0.0408 | 92.3 | 0.0013359 |
| BLKpoint_26 | 298.15 | 0.0497 | 92.3 | 0.0014322 |
| BLKpoint_27 | 298.15 | 0.06 | 92.3 | 0.0015515 |
| BLKpoint_28 | 298.15 | 0.0796 | 92.3 | 0.001748 |
| BLKpoint_29 | 298.15 | 0.1004 | 92.3 | 0.0019469 |
| BLKpoint_30 | 298.15 | 0.1499 | 92.3 | 0.0022424 |
| BLKpoint_31 | 298.15 | 0.1984 | 92.3 | 0.0023706 |

mode: nearest — 8 row(s) of 100 matched (block has 100)
bracket: exact row(s) at temperature_k = 298.15 exist in the matched set
stats (matched, n=100): temperature_k 293.15–308.15 (n=100); mole_fraction_ethanol 0–1 (n=100); pressure_kpa 92.3–92.3 (n=100); viscosity_pa_s 0.00075887–0.0028641 (n=100)
inspection_id: INSP_07241e3bacbf
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_5201::PROPblock_21 - got 8 rows at 298.15 K with x(ethanol) 0.0201–0.1984. Now inspecting GLOBlit_7676::PROPblock_18.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_18, literature=GLOBlit_7676, nearest={'column': 'tempe…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/acs.jced.8b00939 [GLOBlit_7676] :: PROPblock_18 (binary: ethanol + water)
filter: nearest temperature_k ≈ 298.15 (k=8)
block constraints: temperature_k = 298.2; pressure_kpa = 100.0

| BLKpoint_id | mass_fraction_<water> | temperature_k | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 0.061 | 298.2 | 100.0 | 0.00131 |
| BLKpoint_2 | 0.124 | 298.2 | 100.0 | 0.00146 |
| BLKpoint_3 | 0.172 | 298.2 | 100.0 | 0.00164 |
| BLKpoint_4 | 0.233 | 298.2 | 100.0 | 0.0018 |
| BLKpoint_5 | 0.276 | 298.2 | 100.0 | 0.00187 |
| BLKpoint_6 | 0.34 | 298.2 | 100.0 | 0.0019 |
| BLKpoint_7 | 0.41 | 298.2 | 100.0 | 0.00219 |
| BLKpoint_8 | 0.5 | 298.2 | 100.0 | 0.00231 |

mode: nearest — 8 row(s) of 9 matched (block has 9)
bracket: temperature_k = 298.15 lies outside the matched range 298.2–298.2 (no row below it)
topology: viscosity_pa_s vs mass_fraction_water: monotonic↑
stats (matched, n=9): mass_fraction_water 0.061–0.62 (n=9); temperature_k 298.2–298.2 (n=9); pressure_kpa 100.0–100.0 (n=9); viscosity_pa_s 0.00131–0.00234 (n=9)
inspection_id: INSP_e85736c913d0
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<answer>

## Binary Mixture Viscosity Data: Ethanol + Water at ~298.15 K

Ten data blocks were found in the ThermoML database containing dynamic viscosity (GLOBprop_4) measurements for binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) mixtures near 298.15 K. The three blocks with the best composition coverage are detailed below, followed by a summary of additional blocks.

---

### Best Blocks (Inspected)

**1. GLOBlit_2825 / PROPblock_11** — DOI: 10.1016/j.jct.2007.05.004

- **Total points:** 37 (full block)
- **Temperature range:** 293.15–303.15 K
- **Composition variable:** mole fraction of water, range 0–1
- **Viscosity range:** 0.000797–0.002705 Pa·s
- **Pressure:** 101.0 kPa (constrained)

Representative data at exactly 298.15 K (8 of 37 points shown):

| x(water) | Viscosity (Pa·s) |
|-----------|-----------------|
| 0         | 0.001082        |
| 0.0501    | 0.001153        |
| 0.0986    | 0.001232        |
| 0.1961    | 0.001380        |
| 0.2961    | 0.001531        |
| 0.3991    | 0.001659        |
| 0.5989    | 0.002115        |
| 0.6991    | 0.002275        |

This block spans the full mole-fraction range (0 to 1) and provides excellent composition coverage across multiple temperatures.

---

**2. GLOBlit_5201 / PROPblock_21** — DOI: 10.1016/j.jct.2018.02.022

- **Total points:** 100 (full block)
- **Temperature range:** 293.15–308.15 K
- **Composition variable:** mole fraction of ethanol, range 0–1
- **Viscosity range:** 0.00075887–0.0028641 Pa·s
- **Pressure:** 92.3 kPa (constrained)

Representative data at exactly 298.15 K (8 of 100 points shown):

| x(ethanol) | Viscosity (Pa·s) |
|------------|-----------------|
| 0.0201     | 0.001098        |
| 0.0408     | 0.0013359       |
| 0.0497     | 0.0014322       |
| 0.0600     | 0.0015515       |
| 0.0796     | 0.001748        |
| 0.1004     | 0.0019469       |
| 0.1499     | 0.0022424       |
| 0.1984     | 0.0023706       |

This is the largest dataset by raw point count (100 points) and covers nearly the full composition range. The 298.15 K isotherm extends beyond the 8 rows shown here.

---

**3. GLOBlit_7676 / PROPblock_18** — DOI: 10.1021/acs.jced.8b00939

- **Total points:** 9
- **Temperature:** 298.2 K (constrained)
- **Composition variable:** mass fraction of water, range 0.061–0.62
- **Viscosity range:** 0.00131–0.00234 Pa·s
- **Pressure:** 100.0 kPa (constrained)

Data at 298.2 K (8 of 9 points shown):

| w(water) | Viscosity (Pa·s) |
|----------|-----------------|
| 0.061    | 0.00131         |
| 0.124    | 0.00146         |
| 0.172    | 0.00164         |
| 0.233    | 0.00180         |
| 0.276    | 0.00187         |
| 0.340    | 0.00190         |
| 0.410    | 0.00219         |
| 0.500    | 0.00231         |

All points are at the constrained temperature of 298.2 K, with viscosity monotonically increasing with water mass fraction over this range.

---

### Additional Blocks Found (Not Inspected in Detail)

| DOI | Block | GLOBlit | Notes |
|-----|-------|---------|-------|
| 10.1021/acs.jced.7b00299 | PROPblock_11 | GLOBlit_7178 | 2 points, molality-based |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | GLOBlit_7448 | 6 points, w(water) 0.206–0.508 |
| 10.1021/je4003515 | PROPblock_8 | GLOBlit_10159 | 25 points, molality of ethanol 14–22 mol/kg, T 293.15–313.15 K |
| 10.1021/je600565m | PROPblock_5 | GLOBlit_10699 | (details truncated in search results) |

Plus 3 additional blocks from the original search whose details were truncated.

---

### Chemistry Insight

The inspected data clearly show the well-known non-ideal viscosity behavior of ethanol–water mixtures. At 298.15 K, viscosity increases substantially as the two components are mixed — for example, from 0.001082 Pa·s for pure ethanol to 0.002275 Pa·s at x(water) = 0.6991 in the GLOBlit_2825 block. The full-block statistics for GLOBlit_5201 show viscosity reaching up to 0.0028641 Pa·s, consistent with a viscosity maximum in the intermediate composition region. This behavior arises from enhanced hydrogen-bonding interactions between ethanol and water molecules in the mixture.

**Recommended blocks for comprehensive analysis:** GLOBlit_2825 / PROPblock_11 (full x = 0–1 coverage, 37 points) and GLOBlit_5201 / PROPblock_21 (100 points, nearly full composition range).

</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** PROPblock_11 + PROPblock_47 + PROPblock_8 + PROPblock_5: 0.206 (near '…2 points, molality-based | |   |   |   | 6 points, w(water) …') matches no inspected row/stat, database table, or other source of PROPblock_11 + PROPblock_47 + PROPblock_8 + PROPblock_5
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_11", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 0.206})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_11 + PROPblock_47 + PROPblock_8 + PROPblock_5: 0.508 (near '…ts, molality-based | |   |   |   | 6 points, w(water) 0.206–…') matches no inspected row/stat, database table, or other source of PROPblock_11 + PROPblock_47 + PROPblock_8 + PROPblock_5
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_11", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 0.508})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_11 + PROPblock_47 + PROPblock_8 + PROPblock_5: 25 (near '…|   |   | 6 points, w(water) 0.206–0.508 | |   |   |   | 25 …') matches no inspected row/stat, database table, or other source of PROPblock_11 + PROPblock_47 + PROPblock_8 + PROPblock_5
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_11", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 25.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_11 + PROPblock_47 + PROPblock_8 + PROPblock_5: 14 (near '…0.206–0.508 | |   |   |   | 25 points, molality of ethanol 1…') matches no inspected row/stat, database table, or other source of PROPblock_11 + PROPblock_47 + PROPblock_8 + PROPblock_5
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_11", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 14.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_11 + PROPblock_47 + PROPblock_8 + PROPblock_5: 22 (near '…206–0.508 | |   |   |   | 25 points, molality of ethanol 14–…') matches no inspected row/stat, database table, or other source of PROPblock_11 + PROPblock_47 + PROPblock_8 + PROPblock_5
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_11", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 22.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_11 + PROPblock_47 + PROPblock_8 + PROPblock_5: 313.15 (near '…|   | 25 points, molality of ethanol 14–22 mol/kg, T 293.15–…') matches no inspected row/stat, database table, or other source of PROPblock_11 + PROPblock_47 + PROPblock_8 + PROPblock_5
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_11", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 313.15})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNINSPECTED_BLOCK** PROPblock_5: PROPblock_5 is quoted with data values (298.15, 0.001082, 0.002275, 0.6991, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_5", literature="<GLOBlit_N or DOI>")`
Inspected so far: PROPblock_11, PROPblock_18, PROPblock_21

Verified as grounded — correct as quoted, keep unchanged:
- PROPblock_11: 37, 293.15, 303.15, 0.000797, 0.002705, 101.0, 298.15, 0.001082, 0.0501, 0.001153, 0.0986, 0.001232, 0.1961, 0.001380, 0.2961, 0.001531, 0.3991, 0.001659, 0.5989, 0.002115, 0.6991, 0.002275
- PROPblock_21: 100, 293.15, 308.15, 0.00075887, 0.0028641, 92.3, 298.15, 0.0201, 0.001098, 0.0408, 0.0013359, 0.0497, 0.0014322, 0.0600, 0.0015515, 0.0796, 0.001748, 0.1004, 0.0019469, 0.1499, 0.0022424, 0.1984, 0.0023706
- PROPblock_18: 298.2, 0.061, 0.62, 0.00131, 0.00234, 100.0, 0.124, 0.00146, 0.172, 0.00164, 0.233, 0.00180, 0.276, 0.00187, 0.340, 0.00190, 0.410, 0.00219, 0.500, 0.00231
Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_11 + PROPblock_47 + PROPblock_8 + PROPblock_5: 293.15

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## LLM Response


<reasoning>
The grounding checker is flagging values in the "Additional Blocks Found" table that came from the search_blocks results but were not individually inspected. These values (0.206, 0.508, 25, 14, 22, 313.15) are from the search_blocks summary, not from inspect_block_table. The checker also flags PROPblock_5 as uninspected.

The fix is straightforward:
1. The values in the "Additional Blocks Found" table (0.206, 0.508, 25, 14, 22, 313.15) came from the search_blocks summary results. They are search-result metadata, not inspected block data. I should note they are from search results, not inspected, or simply remove the specific numbers.
2. PROPblock_5 (GLOBlit_10699) was never inspected - I should not quote data values for it. The checker says it's quoted with values like 298.15, 0.001082 etc. - but those are actually from PROPblock_11 (GLOBlit_2825) in the Chemistry Insight section. The checker seems to be associating the Chemistry Insight values with PROPblock_5 because it's in the same answer region.

Let me re-read the flags more carefully:
- "UNINSPECTED_BLOCK PROPblock_5: PROPblock_5 is quoted with data values (298.15, 0.001082, 0.002275, 0.6991, …) but was never inspected in this run" - These values are actually from PROPblock_11 in the Chemistry Insight section. The checker may be confused about attribution. But the fix says "required."

The simplest surgical fix:
1. Remove specific numerical details from the uninspected blocks in the "Additional Blocks Found" table, or label them as "per search results, not individually inspected."
2. Make sure the Chemistry Insight section clearly attributes its values to the inspected blocks only.

Let me rewrite the answer surgically, keeping all verified values unchanged.
</reasoning>

<answer>

## Binary Mixture Viscosity Data: Ethanol + Water at ~298.15 K

Ten data blocks were found in the ThermoML database containing dynamic viscosity (GLOBprop_4) measurements for binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) mixtures near 298.15 K. The three blocks with the best composition coverage are detailed below, followed by a summary of additional blocks.

---

### Best Blocks (Inspected)

**1. GLOBlit_2825 / PROPblock_11** — DOI: 10.1016/j.jct.2007.05.004

- **Total points:** 37 (full block)
- **Temperature range:** 293.15–303.15 K
- **Composition variable:** mole fraction of water, range 0–1
- **Viscosity range:** 0.000797–0.002705 Pa·s
- **Pressure:** 101.0 kPa (constrained)

Representative data at exactly 298.15 K (8 of 37 points shown):

| x(water) | Viscosity (Pa·s) |
|-----------|-----------------|
| 0         | 0.001082        |
| 0.0501    | 0.001153        |
| 0.0986    | 0.001232        |
| 0.1961    | 0.001380        |
| 0.2961    | 0.001531        |
| 0.3991    | 0.001659        |
| 0.5989    | 0.002115        |
| 0.6991    | 0.002275        |

This block spans the full mole-fraction range (0 to 1) and provides excellent composition coverage across multiple temperatures.

---

**2. GLOBlit_5201 / PROPblock_21** — DOI: 10.1016/j.jct.2018.02.022

- **Total points:** 100 (full block)
- **Temperature range:** 293.15–308.15 K
- **Composition variable:** mole fraction of ethanol, range 0–1
- **Viscosity range:** 0.00075887–0.0028641 Pa·s
- **Pressure:** 92.3 kPa (constrained)

Representative data at exactly 298.15 K (8 of 100 points shown):

| x(ethanol) | Viscosity (Pa·s) |
|------------|-----------------|
| 0.0201     | 0.001098        |
| 0.0408     | 0.0013359       |
| 0.0497     | 0.0014322       |
| 0.0600     | 0.0015515       |
| 0.0796     | 0.001748        |
| 0.1004     | 0.0019469       |
| 0.1499     | 0.0022424       |
| 0.1984     | 0.0023706       |

This is the largest dataset by raw point count (100 points) and covers nearly the full composition range. The 298.15 K isotherm extends beyond the 8 rows shown here.

---

**3. GLOBlit_7676 / PROPblock_18** — DOI: 10.1021/acs.jced.8b00939

- **Total points:** 9
- **Temperature:** 298.2 K (constrained)
- **Composition variable:** mass fraction of water, range 0.061–0.62
- **Viscosity range:** 0.00131–0.00234 Pa·s
- **Pressure:** 100.0 kPa (constrained)

Data at 298.2 K (8 of 9 points shown):

| w(water) | Viscosity (Pa·s) |
|----------|-----------------|
| 0.061    | 0.00131         |
| 0.124    | 0.00146         |
| 0.172    | 0.00164         |
| 0.233    | 0.00180         |
| 0.276    | 0.00187         |
| 0.340    | 0.00190         |
| 0.410    | 0.00219         |
| 0.500    | 0.00231         |

All points are at the constrained temperature of 298.2 K, with viscosity monotonically increasing with water mass fraction over this range.

---

### Additional Blocks Found (Not Inspected — No Numerical Details Available)

The following blocks were returned by the discovery search but were not individually inspected in this run. No specific numerical values are quoted for them.

| DOI | Block | GLOBlit | Brief Description |
|-----|-------|---------|-------------------|
| 10.1021/acs.jced.7b00299 | PROPblock_11 | GLOBlit_7178 | Small dataset, molality-based composition |
| 10.1021/acs.jced.8b00086 | PROPblock_47 | GLOBlit_7448 | Mass-fraction-based, partial composition range |
| 10.1021/je4003515 | PROPblock_8 | GLOBlit_10159 | Molality-based, multiple temperatures |
| 10.1021/je600565m | PROPblock_5 | GLOBlit_10699 | Details not inspected |

Plus 3 additional blocks from the original search whose details were truncated.

---

### Chemistry Insight

The inspected data from GLOBlit_2825 / PROPblock_11 clearly show the well-known non-ideal viscosity behavior of ethanol–water mixtures. At 298.15 K, viscosity increases substantially as water is added to ethanol — from 0.001082 Pa·s for pure ethanol (x(water) = 0) to 0.002275 Pa·s at x(water) = 0.6991. The full-block statistics for GLOBlit_5201 / PROPblock_21 show viscosity reaching up to 0.0028641 Pa·s across the entire composition range, consistent with a viscosity maximum in the intermediate composition region. This behavior arises from enhanced hydrogen-bonding interactions between ethanol and water molecules in the mixture.

**Recommended blocks for comprehensive analysis:** GLOBlit_2825 / PROPblock_11 (full x = 0–1 coverage, 37 points) and GLOBlit_5201 / PROPblock_21 (100 points, nearly full composition range).

</answer>