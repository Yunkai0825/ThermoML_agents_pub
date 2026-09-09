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
Find viscosity data for aqueous N-methyl-2-pyrrolidone (NMP + water) mixtures near 25°C (298.15 K)

## Instruction
Search for binary mixture viscosity (dynamic viscosity, GLOBprop_4) data for the system N-methyl-2-pyrrolidone + water. NMP is also known as 1-methyl-2-pyrrolidone or 1-methyl-2-pyrrolidinone, CAS 872-50-4. Look for data near 298.15 K. Return DOIs, block numbers, temperature ranges, and number of data points.

## ID Catalog (from working memory)
[]

## Assistant
(syntax-rejected turn — malformed tool calls never executed; corrected on a later turn. Full detail in the run log.)

## User
(validation fired earlier — corrected)

## Assistant
<summary>Resolving compound IDs for N-methyl-2-pyrrolidone and water to search for viscosity data.</summary>
<tool_call>resolve_compound_ids(queries=['N-methyl-2-pyrr…, min_score=50, limit=5)</tool_call>

## User
<tool_result>
Both compounds resolved successfully with exact name matches.

| Compound | GLOBcomp ID | Formula | SMILES |
|---|---|---|---|
| N-methylpyrrolidone (NMP) | GLOBcomp_47 | C5H9NO | CN1CCCC1=O |
| water | GLOBcomp_1 | H2O | O |
</tool_result>

## Assistant
<summary>Resolved NMP = GLOBcomp_47, water = GLOBcomp_1. Now searching for binary viscosity (GLOBprop_4) data for NMP+water near 298.15 K.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_47', 'GLOBcomp_1'], property=GLOBprop_4, system_type=binary…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Correcting temperature_range to list format [290, 310] and re-searching for NMP+water binary viscosity data.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_47', 'GLOBcomp_1'], property=GLOBprop_4, system_type=binary…)</tool_call>

## User
<tool_result>
**Summary:** Three blocks of dynamic viscosity (Pa·s) for NMP+water binary mixtures were found with perfect relevance scores. Two blocks contain data exactly at 298.15 K; the third (GLOBlit_9372) brackets 298.15 K with data at 293.15 K and 303.15 K.

### Blocks Overview

| DOI | Block | GLOBlit | Pts | T range (K) | x variable | Pressure (kPa) |
|---|---|---|---|---|---|---|
| 10.1021/je034073k | PROPblock_3 | GLOBlit_8238 | 65 | 298.15–333.15 | x(NMP) | 101.15 |
| 10.1021/je0340809 | PROPblock_17 | GLOBlit_8242 | 95 | 298.15–338.15 | x(water) | 101.3 |
| 10.1021/je100967k | PROPblock_17 | GLOBlit_9372 | 44 | 293.15–323.15 | x(NMP) | 101.0 |

### Data at 298.15 K — Block 1 (GLOBlit_8238)

| x(NMP) | η (Pa·s) | ±U |
|---|---|---|
| 0.0 | 0.00089 | 1
</tool_result>

## Assistant
<reasoning>
I have the search results with three blocks of dynamic viscosity data for NMP+water binary mixtures near 298.15 K. Let me compile the answer with the information returned by the tool.

The three blocks found are:
1. GLOBlit_8238, PROPblock_3 - DOI: 10.1021/je034073k - 65 points, 298.15-333.15 K
2. GLOBlit_8242, PROPblock_17 - DOI: 10.1021/je0340809 - 95 points, 298.15-338.15 K
3. GLOBlit_9372, PROPblock_17 - DOI: 10.1021/je100967k - 44 points, 293.15-323.15 K

I have enough information to provide a complete answer. The tool result also showed some data at 298.15 K from Block 1 (GLOBlit_8238) with x(NMP) = 0.0, η = 0.00089 Pa·s. Let me provide the answer now.
</reasoning>

<answer>
Three data blocks containing dynamic viscosity (η, Pa·s) measurements for the binary system **N-methyl-2-pyrrolidone (NMP) + water** were found near 298.15 K:

| # | DOI | Literature ID | Block | Data Points | T range (K) | Composition variable | Pressure (kPa) |
|---|-----|---------------|-------|-------------|-------------|---------------------|----------------|
| 1 | 10.1021/je034073k | GLOBlit_8238 | PROPblock_3 | 65 | 298.15–333.15 | x(NMP) | 101.15 |
| 2 | 10.1021/je0340809 | GLOBlit_8242 | PROPblock_17 | 95 | 298.15–338.15 | x(water) | 101.3 |
| 3 | 10.1021/je100967k | GLOBlit_9372 | PROPblock_17 | 44 | 293.15–323.15 | x(NMP) | 101.0 |

**Key observations:**

- **Blocks 1 and 2** (GLOBlit_8238 and GLOBlit_8242) contain data exactly at **298.15 K**, making them directly usable without interpolation.
- **Block 3** (GLOBlit_9372) brackets 298.15 K with measurements at **293.15 K and 303.15 K** but does not include an exact 298.15 K isotherm.
- All three blocks report data at approximately atmospheric pressure (~101 kPa).
- Block 1 uses mole fraction of NMP as the composition variable, Block 2 uses mole fraction of water, and Block 3 uses mole fraction of NMP.

A representative data point from Block 1 (GLOBlit_8238::PROPblock_3) at 298.15 K: pure water (x(NMP) = 0.0) has η = 0.00089 Pa·s, consistent with the well-known viscosity of water near 25 °C.

NMP–water mixtures are known to exhibit a pronounced viscosity maximum at intermediate compositions due to strong hydrogen-bonding interactions between NMP and water, which these datasets should capture across the full composition range.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_BLOCK** PROPblock_3 + PROPblock_17: PROPblock_3 + PROPblock_17 is quoted with data values (65, 298.15, 333.15, 101.15, …) but was never inspected in this run (values 298.15, 333.15, 101.15, 298.15 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_8238::PROPblock_3"); inspect_block_table(block_number="PROPblock_17", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_17: PROPblock_17 is quoted with data values (298.15, 298.15, 293.15, 303.15, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_17", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** GLOBlit_8238::PROPblock_3: GLOBlit_8238::PROPblock_3 is quoted with data values (298.15, 0.0, 0.00089, 25, …) but was never inspected in this run (values 298.15, 0.0, 0.00089 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_8238::PROPblock_3")`

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## Assistant
<summary>Running inspect_block_table on all three blocks to ground the data values quoted in my answer.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_8238::PROPblock_3, nearest=T=298.15 K)</tool_call>

## User
<tool_result>
{
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'T=298.15 K' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINEMENT_REQUIRED",
  "tool": "inspect_block_table"
}
</tool_result>

## Assistant
<summary>Fixing nearest argument to dict format and inspecting all three blocks for data grounding.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_8238::PROPblock_3, nearest={'T': 298.15})</tool_call>

## User
<tool_result>
**inspect_block_table error** — nearest must be {"column": alias, "value": number, "k": 1..8}

| alias | n_finite | min | max |
|---|---|---|---|
| temperature_k | 65 | 298.15 | 343.15 |
| mole_fraction_n_methylpyrrolidone | 65 | 0 | 1 |
| pressure_kpa | 65 | 101.15 | 101.15 |
| viscosity_pa_s | 65 | 0.000405 | 0.005062 |

Use these aliases in `where` / `nearest` with plain numbers.
</tool_result>

## Assistant
<summary>Got column aliases for GLOBlit_8238::PROPblock_3. Now inspecting with correct nearest format and also inspecting the other two blocks.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_8238::PROPblock_3, nearest={'column': 'tempe…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je034073k [GLOBlit_8238] :: PROPblock_3 (binary: N-methylpyrrolidone + water)
filter: nearest temperature_k ≈ 298.15 (k=8)
block constraints: pressure_kpa = 101.15

| BLKpoint_id | temperature_k | mole_fraction_<N-methylpyrrolidone> | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 0 | 101.15 | 0.00089 |
| BLKpoint_2 | 298.15 | 0.0501 | 101.15 | 0.00174 |
| BLKpoint_3 | 298.15 | 0.0701 | 101.15 | 0.002137 |
| BLKpoint_4 | 298.15 | 0.1001 | 101.15 | 0.002762 |
| BLKpoint_5 | 298.15 | 0.2004 | 101.15 | 0.004555 |
| BLKpoint_6 | 298.15 | 0.3004 | 101.15 | 0.005062 |
| BLKpoint_7 | 298.15 | 0.4012 | 101.15 | 0.004505 |
| BLKpoint_8 | 298.15 | 0.503 | 101.15 | 0.003729 |

mode: nearest — 8 row(s) of 65 matched (block has 65)
bracket: exact row(s) at temperature_k = 298.15 exist in the matched set
stats (matched, n=65): temperature_k 298.15–343.15 (n=65); mole_fraction_n_methylpyrrolidone 0–1 (n=65); pressure_kpa 101.15–101.15 (n=65); viscosity_pa_s 0.000405–0.005062 (n=65)
inspection_id: INSP_bd9d3e42bc68
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_8238::PROPblock_3 successfully. Now inspecting GLOBlit_8242::PROPblock_17 and GLOBlit_9372::PROPblock_17.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_8242::PROPblock_17, nearest={'column': 'tempe…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je0340809 [GLOBlit_8242] :: PROPblock_17 (binary: N-methylpyrrolidone + water)
filter: nearest temperature_k ≈ 298.15 (k=4)
block constraints: pressure_kpa = 101.3

| BLKpoint_id | mole_fraction_<water> | temperature_k | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 0.0522 | 298.15 | 101.3 | 0.001721 |
| BLKpoint_6 | 0.1684 | 298.15 | 101.3 | 0.001985 |
| BLKpoint_11 | 0.2465 | 298.15 | 101.3 | 0.002147 |
| BLKpoint_16 | 0.3481 | 298.15 | 101.3 | 0.002535 |

mode: nearest — 4 row(s) of 95 matched (block has 95)
bracket: exact row(s) at temperature_k = 298.15 exist in the matched set
stats (matched, n=95): mole_fraction_water 0.0522–0.99 (n=95); temperature_k 298.15–338.15 (n=95); pressure_kpa 101.3–101.3 (n=95); viscosity_pa_s 0.000467–0.005159 (n=95)
inspection_id: INSP_8d8303b6d7df
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_8242::PROPblock_17. Now inspecting the third block GLOBlit_9372::PROPblock_17.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_9372::PROPblock_17, nearest={'column': 'tempe…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je100967k [GLOBlit_9372] :: PROPblock_17 (binary: N-methylpyrrolidone + water)
filter: nearest temperature_k ≈ 298.15 (k=4)
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mole_fraction_<N-methylpyrrolidone> | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 293.15 | 0 | 101.0 | 0.0009933 |
| BLKpoint_2 | 293.15 | 0.1 | 101.0 | 0.0033316 |
| BLKpoint_3 | 293.15 | 0.2 | 101.0 | 0.0059028 |
| BLKpoint_4 | 293.15 | 0.3001 | 101.0 | 0.0067739 |

mode: nearest — 4 row(s) of 44 matched (block has 44)
bracket: no matched row at temperature_k = 298.15; nearest below BLKpoint_11 (293.15), nearest above BLKpoint_12 (303.15); 0 matched rows strictly inside that interval
stats (matched, n=44): temperature_k 293.15–323.15 (n=44); mole_fraction_n_methylpyrrolidone 0–1 (n=44); pressure_kpa 101.0–101.0 (n=44); viscosity_pa_s 0.0005465–0.0067739 (n=44)
inspection_id: INSP_e2b42c422e04
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<answer>
Three data blocks containing dynamic viscosity (η, Pa·s) measurements for the binary system **N-methyl-2-pyrrolidone (NMP) + water** were found near 298.15 K:

| # | DOI | Literature ID | Block | Data Points | T range (K) | Composition variable | Pressure (kPa) |
|---|-----|---------------|-------|-------------|-------------|---------------------|----------------|
| 1 | 10.1021/je034073k | GLOBlit_8238 | PROPblock_3 | 65 | 298.15–343.15 | x(NMP) | 101.15 |
| 2 | 10.1021/je0340809 | GLOBlit_8242 | PROPblock_17 | 95 | 298.15–338.15 | x(water) | 101.3 |
| 3 | 10.1021/je100967k | GLOBlit_9372 | PROPblock_17 | 44 | 293.15–323.15 | x(NMP) | 101.0 |

**Key observations:**

- **Blocks 1 and 2** (GLOBlit_8238 and GLOBlit_8242) contain data exactly at **298.15 K**, making them directly usable without interpolation.
- **Block 3** (GLOBlit_9372) does **not** include an exact 298.15 K isotherm; the nearest temperatures are **293.15 K** (below) and **303.15 K** (above).
- All three blocks report data at approximately atmospheric pressure (~101 kPa).
- Block 1 uses mole fraction of NMP as the composition variable, Block 2 uses mole fraction of water, and Block 3 uses mole fraction of NMP.

**Representative data at 298.15 K from Block 1** (GLOBlit_8238::PROPblock_3):

| x(NMP) | η (Pa·s) |
|--------|----------|
| 0 | 0.00089 |
| 0.0501 | 0.00174 |
| 0.0701 | 0.002137 |
| 0.1001 | 0.002762 |
| 0.2004 | 0.004555 |
| 0.3004 | 0.005062 |
| 0.4012 | 0.004505 |
| 0.503 | 0.003729 |

**Representative data at 298.15 K from Block 2** (GLOBlit_8242::PROPblock_17):

| x(water) | η (Pa·s) |
|----------|----------|
| 0.0522 | 0.001721 |
| 0.1684 | 0.001985 |
| 0.2465 | 0.002147 |
| 0.3481 | 0.002535 |

The data from Block 1 clearly shows a pronounced viscosity maximum near x(NMP) ≈ 0.3 (η = 0.005062 Pa·s), after which viscosity decreases at higher NMP mole fractions. This maximum is characteristic of strong hydrogen-bonding interactions between NMP and water, which create extensive intermolecular association networks at intermediate compositions. The overall viscosity range across the full composition span at 298.15 K is 0.000405–0.005062 Pa·s (Block 1 stats) and 0.000467–0.005159 Pa·s (Block 2 stats).
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **MISATTRIBUTED_VALUE** GLOBlit_8242::PROPblock_17: 0.005062 does not belong to GLOBlit_8242::PROPblock_17; it matches only GLOBlit_8238::PROPblock_3 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 0.005062 to GLOBlit_8238::PROPblock_3 — no new tool call needed`
- **MISATTRIBUTED_VALUE** GLOBlit_8242::PROPblock_17: 0.000405 does not belong to GLOBlit_8242::PROPblock_17; it matches only GLOBlit_8238::PROPblock_3 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 0.000405 to GLOBlit_8238::PROPblock_3 — no new tool call needed`
- **MISATTRIBUTED_VALUE** GLOBlit_8242::PROPblock_17: 0.005062 does not belong to GLOBlit_8242::PROPblock_17; it matches only GLOBlit_8238::PROPblock_3 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 0.005062 to GLOBlit_8238::PROPblock_3 — no new tool call needed`
Inspected so far: PROPblock_17, PROPblock_3

Verified as grounded — correct as quoted, keep unchanged:
- PROPblock_3 + PROPblock_17: 65, 298.15, 343.15, 101.15, 95, 338.15, 101.3, 44, 293.15, 323.15, 101.0
- PROPblock_17: 298.15, 293.15, 303.15, 101
- GLOBlit_8238::PROPblock_3: 0.00089, 0.0501, 0.00174, 0.0701, 0.002137, 0.1001, 0.002762, 0.2004, 0.004555, 0.3004, 0.005062, 0.4012, 0.004505, 0.503, 0.003729, 298.15
Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- GLOBlit_8242::PROPblock_17: 0.0522, 0.001721, 0.1684, 0.001985, 0.2465, 0.002147, 0.3481, 0.002535, 0.3, 298.15, 0.000467, 0.005159

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## LLM Response
<answer>
Three data blocks containing dynamic viscosity (η, Pa·s) measurements for the binary system **N-methyl-2-pyrrolidone (NMP) + water** were found near 298.15 K:

| # | DOI | Literature ID | Block | Data Points | T range (K) | Composition variable | Pressure (kPa) |
|---|-----|---------------|-------|-------------|-------------|---------------------|----------------|
| 1 | 10.1021/je034073k | GLOBlit_8238 | PROPblock_3 | 65 | 298.15–343.15 | x(NMP) | 101.15 |
| 2 | 10.1021/je0340809 | GLOBlit_8242 | PROPblock_17 | 95 | 298.15–338.15 | x(water) | 101.3 |
| 3 | 10.1021/je100967k | GLOBlit_9372 | PROPblock_17 | 44 | 293.15–323.15 | x(NMP) | 101.0 |

**Key observations:**

- **Blocks 1 and 2** (GLOBlit_8238 and GLOBlit_8242) contain data exactly at **298.15 K**, making them directly usable without interpolation.
- **Block 3** (GLOBlit_9372) does **not** include an exact 298.15 K isotherm; the nearest temperatures are **293.15 K** (below) and **303.15 K** (above).
- All three blocks report data at approximately atmospheric pressure (~101 kPa).
- Block 1 uses mole fraction of NMP as the composition variable, Block 2 uses mole fraction of water, and Block 3 uses mole fraction of NMP.

**Representative data at 298.15 K from Block 1** (GLOBlit_8238::PROPblock_3):

| x(NMP) | η (Pa·s) |
|--------|----------|
| 0 | 0.00089 |
| 0.0501 | 0.00174 |
| 0.0701 | 0.002137 |
| 0.1001 | 0.002762 |
| 0.2004 | 0.004555 |
| 0.3004 | 0.005062 |
| 0.4012 | 0.004505 |
| 0.503 | 0.003729 |

**Representative data at 298.15 K from Block 2** (GLOBlit_8242::PROPblock_17):

| x(water) | η (Pa·s) |
|----------|----------|
| 0.0522 | 0.001721 |
| 0.1684 | 0.001985 |
| 0.2465 | 0.002147 |
| 0.3481 | 0.002535 |

The data from Block 1 clearly shows a pronounced viscosity maximum near x(NMP) ≈ 0.3 (η = 0.005062 Pa·s at x(NMP) = 0.3004, from GLOBlit_8238::PROPblock_3), after which viscosity decreases at higher NMP mole fractions. This maximum is characteristic of strong hydrogen-bonding interactions between NMP and water, which create extensive intermolecular association networks at intermediate compositions. The overall viscosity range across the full composition span is 0.000405–0.005062 Pa·s (Block 1, GLOBlit_8238::PROPblock_3 stats) and 0.000467–0.005159 Pa·s (Block 2, GLOBlit_8242::PROPblock_17 stats).
</answer>