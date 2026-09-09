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
Find viscosity data blocks for DMSO + water binary mixtures near 25°C

## Instruction
Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with dynamic viscosity (GLOBprop_4) measurements near 298.15 K. Return DOIs, block numbers, temperature ranges.

## ID Catalog (from working memory)
[]

## Assistant
(syntax-rejected turn — malformed tool calls never executed; corrected on a later turn. Full detail in the run log.)

## User
(validation fired earlier — corrected)

## Assistant
<summary>Resolving compound IDs for DMSO and water to search for viscosity data in binary mixtures.</summary>
<tool_call>resolve_compound_ids(queries=['dimethyl sulfox…, min_score=50, limit=5)</tool_call>

## User
<tool_result>
Both compounds resolved with exact name matches.

| Compound | Global ID | Formula | SMILES |
|---|---|---|---|
| dimethyl sulfoxide (DMSO) | GLOBcomp_31 | C2H6OS | CS(C)=O |
| water | GLOBcomp_1 | H2O | O |
</tool_result>

## Assistant
<summary>DMSO = GLOBcomp_31, water = GLOBcomp_1. Now searching for binary mixture blocks with dynamic viscosity (GLOBprop_4) near 298.15 K.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_31', 'GLOBcomp_1'], property=GLOBprop_4, system_type=binary…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Re-emitting search_blocks with correct temperature_range format as list of floats [293.0, 303.0].</summary>
<tool_call>search_blocks(compound=['GLOBcomp_31', 'GLOBcomp_1'], property=GLOBprop_4, system_type=binary…)</tool_call>

## User
<tool_result>
**Summary:** Two binary DMSO + water viscosity blocks found, both with data at exactly 298.15 K and 101 kPa. Block 1 (GLOBlit_2781) provides mole-fraction-based data with 8 points at 298.15 K spanning x(DMSO) = 0–1. Block 2 (GLOBlit_11517) provides mass-fraction-based data with 6 points at 298.15 K spanning w(DMSO) = 0–1.

### Block Overview

| # | DOI | Block | GLOBlit | Pts | Composition var | T range (K) | Score |
|---|-----|-------|---------|-----|-----------------|-------------|-------|
| 1 | 10.1016/j.jct.2006.12.012 | PROPblock_3 | GLOBlit_2781 | 120 | mole_fraction (BLKvar_2 / GLOBvar_2) | 298.15–308.15 | 100 |
| 2 | 10.1021/je9001027 | PROPblock_3 | GLOBlit_11517 | 35 | mass_fraction (BLKvar_2 / GLOBvar_5) | 298.15–318.15 | 100 |

### Block 1 — 298.15 K data (mole fraction, GLOBlit_2781)

| x(DMSO) | η (Pa·s) | ±U |
|---|---|---|
| 0.0 | 0.0008901 | 1.18e-05 |
| 0.2036 | 0.0030165 | 3.57e-05 |
| 0.2768 | 0.0035372 | 4.16e-05 |
| 0.3335 | 0.0037144 | 4.37e-05 |
| 0.3906 | 0.0037169 | 4.36e-05 |
| 0.4412 | 0.0036062 | 4.21e-05 |
| 0.7595 | 0.0
</tool_result>

## Assistant


<reasoning>
The search has returned two binary DMSO + water viscosity blocks with data near 298.15 K. I have the key information needed to answer the question. Let me compile the results.

The tool returned two blocks:
1. GLOBlit_2781 (DOI: 10.1016/j.jct.2006.12.012), PROPblock_3 — 120 total data points, mole fraction composition, T range 298.15–308.15 K
2. GLOBlit_11517 (DOI: 10.1021/je9001027), PROPblock_3 — 35 total data points, mass fraction composition, T range 298.15–318.15 K

Both have data at exactly 298.15 K. The first block shows 8 data points at 298.15 K with mole fraction of DMSO from 0 to ~1, and the second block has 6 points at 298.15 K with mass fraction.

I have enough information to provide the answer. The data table from Block 1 was partially cut off but shows the viscosity maximum near x(DMSO) ≈ 0.33–0.39 where η reaches about 0.00371 Pa·s, which is the well-known viscosity maximum in the DMSO-water system.
</reasoning>

<answer>
## Viscosity Data for DMSO + Water Binary Mixtures near 25 °C

Two binary mixture blocks containing dimethyl sulfoxide (DMSO, GLOBcomp_31) and water (GLOBcomp_1) with dynamic viscosity (GLOBprop_4) measurements near 298.15 K were found in the ThermoML database:

### Block Summary

| # | DOI | Block | GLOBlit | Total pts | Composition variable | T range (K) |
|---|-----|-------|---------|-----------|---------------------|-------------|
| 1 | 10.1016/j.jct.2006.12.012 | PROPblock_3 | GLOBlit_2781 | 120 | Mole fraction (GLOBvar_2) | 298.15–308.15 |
| 2 | 10.1021/je9001027 | PROPblock_3 | GLOBlit_11517 | 35 | Mass fraction (GLOBvar_5) | 298.15–318.15 |

Both blocks report data at exactly 298.15 K and 101 kPa (standard pressure).

### Representative Data at 298.15 K (Block 1 — mole-fraction basis)

| x(DMSO) | η (Pa·s) | ±U (Pa·s) |
|---------|----------|-----------|
| 0.0 | 0.0008901 | 1.18×10⁻⁵ |
| 0.2036 | 0.0030165 | 3.57×10⁻⁵ |
| 0.2768 | 0.0035372 | 4.16×10⁻⁵ |
| 0.3335 | 0.0037144 | 4.37×10⁻⁵ |
| 0.3906 | 0.0037169 | 4.36×10⁻⁵ |
| 0.4412 | 0.0036062 | 4.21×10⁻⁵ |

**Chemistry insight:** The data from Block 1 clearly shows the well-known viscosity maximum in the DMSO–water system, occurring near x(DMSO) ≈ 0.33–0.39 where the dynamic viscosity reaches approximately 0.00372 Pa·s — roughly 4× higher than pure water (0.00089 Pa·s). This maximum is attributed to strong hydrogen-bonding interactions between DMSO and water that form structured DMSO·2H₂O complexes, enhancing intermolecular friction and thus viscosity in this composition range.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_BLOCK** PROPblock_3: PROPblock_3 is quoted with data values (120, 298.15, 308.15, 35, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_3: PROPblock_3 is quoted with data values (298.15, 101, 298.15, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_3: PROPblock_3 is quoted with data values (0.0, 0.0008901, 1.18e-5, 0.2036, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_3: PROPblock_3 is quoted with data values (0.33, 0.39, 0.00372, 0.00089, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>")`

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## Assistant
<summary>Running inspect_block_table on both DMSO+water viscosity blocks (GLOBlit_2781::PROPblock_3 and GLOBlit_11517::PROPblock_3) to ground all quoted data values.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_3, literature=GLOBlit_2781, where=T BETWEEN 297 AND…)</tool_call>

## User
<tool_result>
**inspect_block_table error** — where filter error: unknown column alias 'T'

| alias | n_finite | min | max |
|---|---|---|---|
| temperature_k | 120 | 298.15 | 318.15 |
| mole_fraction_dimethyl_sulfoxide | 120 | 0 | 1 |
| pressure_kpa | 120 | 101 | 101 |
| viscosity_pa_s | 120 | 0.0005961 | 0.0037353 |

Use these aliases in `where` / `nearest` with plain numbers.
</tool_result>

## Assistant
<summary>Got column aliases for GLOBlit_2781::PROPblock_3. Re-running with correct alias temperature_k for 298.15 K filter, and also inspecting GLOBlit_11517::PROPblock_3.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_3, literature=GLOBlit_2781, where=temperature_k BET…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2006.12.012 [GLOBlit_2781] :: PROPblock_3 (binary: dimethyl sulfoxide + water)
filter: where temperature_k BETWEEN 297.5 AND 299
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mole_fraction_<dimethyl sulfoxide> | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 0 | 101.0 | 0.0008901 |
| BLKpoint_2 | 298.15 | 0.0238 | 101.0 | 0.0010331 |
| BLKpoint_3 | 298.15 | 0.0489 | 101.0 | 0.0012576 |
| BLKpoint_6 | 298.15 | 0.1587 | 101.0 | 0.0025493 |
| BLKpoint_7 | 298.15 | 0.2036 | 101.0 | 0.0030165 |
| BLKpoint_8 | 298.15 | 0.2379 | 101.0 | 0.0033011 |
| BLKpoint_9 | 298.15 | 0.2768 | 101.0 | 0.0035372 |
| BLKpoint_10 | 298.15 | 0.3074 | 101.0 | 0.0036564 |
| BLKpoint_11 | 298.15 | 0.3335 | 101.0 | 0.0037144 |
| BLKpoint_12 | 298.15 | 0.3638 | 101.0 | 0.0037353 |
| BLKpoint_13 | 298.15 | 0.3906 | 101.0 | 0.0037169 |
| BLKpoint_14 | 298.15 | 0.4412 | 101.0 | 0.0036062 |
| BLKpoint_15 | 298.15 | 0.5193 | 101.0 | 0.0033124 |
| BLKpoint_17 | 298.15 | 0.6195 | 101.0 | 0.0028832 |
| BLKpoint_18 | 298.15 | 0.6813 | 101.0 | 0.0026556 |
| BLKpoint_19 | 298.15 | 0.7595 | 101.0 | 0.0024317 |
| BLKpoint_21 | 298.15 | 0.8856 | 101.0 | 0.0021754 |
| BLKpoint_24 | 298.15 | 1 | 101.0 | 0.001996 |

mode: RDP — 18 of 24 matched rows shown (shape-preserving; block has 120). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=24): temperature_k 298.15–298.15 (n=24); mole_fraction_dimethyl_sulfoxide 0–1 (n=24); pressure_kpa 101.0–101.0 (n=24); viscosity_pa_s 0.0008901–0.0037353 (n=24)
stats (full block, n=120): temperature_k 298.15–318.15 (n=120); mole_fraction_dimethyl_sulfoxide 0–1 (n=120); pressure_kpa 101.0–101.0 (n=120); viscosity_pa_s 0.0005961–0.0037353 (n=120)
inspection_id: INSP_b08a03233872
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_2781::PROPblock_3 — 24 points at 298.15 K, full block 120 pts spanning 298.15–318.15 K. Now inspecting GLOBlit_11517::PROPblock_3.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_3, literature=GLOBlit_11517, where=temperature_k BET…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je9001027 [GLOBlit_11517] :: PROPblock_3 (binary: dimethyl sulfoxide + water)
filter: where temperature_k BETWEEN 297.5 AND 299
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mass_fraction_<dimethyl sulfoxide> | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 0 | 101.0 | 0.00089 |
| BLKpoint_2 | 298.15 | 0.2 | 101.0 | 0.00134 |
| BLKpoint_3 | 298.15 | 0.4 | 101.0 | 0.002221 |
| BLKpoint_4 | 298.15 | 0.5 | 101.0 | 0.0028073 |
| BLKpoint_5 | 298.15 | 0.6 | 101.0 | 0.003421 |
| BLKpoint_6 | 298.15 | 0.7 | 101.0 | 0.0023568 |
| BLKpoint_7 | 298.15 | 1 | 101.0 | 0.001966 |

mode: complete — all 7 matched rows shown (block has 35)
stats (matched, n=7): temperature_k 298.15–298.15 (n=7); mass_fraction_dimethyl_sulfoxide 0–1 (n=7); pressure_kpa 101.0–101.0 (n=7); viscosity_pa_s 0.00089–0.003421 (n=7)
stats (full block, n=35): temperature_k 298.15–318.15 (n=35); mass_fraction_dimethyl_sulfoxide 0–1 (n=35); pressure_kpa 101.0–101.0 (n=35); viscosity_pa_s 0.0005346–0.003421 (n=35)
inspection_id: INSP_c018a8ec4dd8
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<answer>
## Viscosity Data for DMSO + Water Binary Mixtures near 25 °C

Two binary mixture blocks containing dimethyl sulfoxide (DMSO, GLOBcomp_31) and water (GLOBcomp_1) with dynamic viscosity (GLOBprop_4) measurements near 298.15 K were found in the ThermoML database:

### Block Summary

| # | DOI | Block | GLOBlit | Total pts | Composition variable | T range (K) |
|---|-----|-------|---------|-----------|---------------------|-------------|
| 1 | 10.1016/j.jct.2006.12.012 | PROPblock_3 | GLOBlit_2781 | 120 | Mole fraction (GLOBvar_2) | 298.15–318.15 |
| 2 | 10.1021/je9001027 | PROPblock_3 | GLOBlit_11517 | 35 | Mass fraction (GLOBvar_5) | 298.15–318.15 |

Both blocks report data at exactly 298.15 K with a pressure constraint of 101.0 kPa.

### Block 1 — Data at 298.15 K (mole-fraction basis, GLOBlit_2781::PROPblock_3)

24 data points at 298.15 K spanning x(DMSO) = 0–1. Representative inspected rows:

| x(DMSO) | η (Pa·s) |
|---------|----------|
| 0 | 0.0008901 |
| 0.0238 | 0.0010331 |
| 0.0489 | 0.0012576 |
| 0.1587 | 0.0025493 |
| 0.2036 | 0.0030165 |
| 0.2768 | 0.0035372 |
| 0.3335 | 0.0037144 |
| 0.3638 | 0.0037353 |
| 0.3906 | 0.0037169 |
| 0.4412 | 0.0036062 |
| 0.5193 | 0.0033124 |
| 0.6195 | 0.0028832 |
| 0.7595 | 0.0024317 |
| 0.8856 | 0.0021754 |
| 1 | 0.001996 |

### Block 2 — Data at 298.15 K (mass-fraction basis, GLOBlit_11517::PROPblock_3)

7 data points at 298.15 K spanning w(DMSO) = 0–1:

| w(DMSO) | η (Pa·s) |
|---------|----------|
| 0 | 0.00089 |
| 0.2 | 0.00134 |
| 0.4 | 0.002221 |
| 0.5 | 0.0028073 |
| 0.6 | 0.003421 |
| 0.7 | 0.0023568 |
| 1 | 0.001966 |

**Chemistry insight:** Both datasets clearly show the well-known viscosity maximum in the DMSO–water system. In Block 1, the maximum viscosity of 0.0037353 Pa·s occurs at x(DMSO) = 0.3638, roughly 4.2× higher than pure water (0.0008901 Pa·s) and 1.9× higher than pure DMSO (0.001996 Pa·s). In Block 2, the maximum of 0.003421 Pa·s appears at w(DMSO) = 0.6. This pronounced viscosity maximum is attributed to strong hydrogen-bonding interactions between DMSO and water that form structured DMSO·2H₂O complexes, enhancing intermolecular friction in this composition range.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** GLOBlit_11517::PROPblock_3: 4.2 (near '…osity of 0.0037353 Pa·s occurs at x(DMSO) = 0.3638, roughly …') matches no inspected row/stat, database table, or other source of GLOBlit_11517::PROPblock_3
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_11517::PROPblock_3", nearest={"column": "temperature_k", "value": 4.2})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNINSPECTED_VALUE** GLOBlit_11517::PROPblock_3: 1.9 exists in PROPblock_3's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_2781::PROPblock_3", nearest={"column": "temperature_k", "value": 1.9})`
Inspected so far: PROPblock_3

Verified as grounded — correct as quoted, keep unchanged:
- PROPblock_3: 120, 298.15, 318.15, 35, 101.0
- GLOBlit_2781::PROPblock_3: 24, 298.15, 0.0008901, 0.0238, 0.0010331, 0.0489, 0.0012576, 0.1587, 0.0025493, 0.2036, 0.0030165, 0.2768, 0.0035372, 0.3335, 0.0037144, 0.3638, 0.0037353, 0.3906, 0.0037169, 0.4412, 0.0036062, 0.5193, 0.0033124, 0.6195, 0.0028832, 0.7595, 0.0024317, 0.8856, 0.0021754, 0.001996
Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- GLOBlit_11517::PROPblock_3: 298.15, 0.00089, 0.2, 0.00134, 0.4, 0.002221, 0.5, 0.0028073, 0.6, 0.003421, 0.7, 0.0023568, 0.001966, 0.0037353, 0.3638, 0.0008901, 0.001996

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## LLM Response


<reasoning>
The grounding checker flagged two values:
1. "4.2" — this is a ratio I computed (0.0037353 / 0.0008901 ≈ 4.20). It's not a database datum, it's derived. I need to label it as a computed ratio.
2. "1.9" — this is also a ratio I computed (0.0037353 / 0.001996 ≈ 1.87). It's not a database datum, it's derived. I need to label it as a computed ratio.

Both are simple arithmetic from inspected values. I just need to label them as derived and fix the arithmetic precision. Let me verify:
- 0.0037353 / 0.0008901 = 4.197... ≈ 4.2× — correct as approximate
- 0.0037353 / 0.001996 = 1.871... ≈ 1.9× — correct as approximate

I'll label both as computed ratios from the inspected data. No new tool calls needed.
</reasoning>

<answer>
## Viscosity Data for DMSO + Water Binary Mixtures near 25 °C

Two binary mixture blocks containing dimethyl sulfoxide (DMSO, GLOBcomp_31) and water (GLOBcomp_1) with dynamic viscosity (GLOBprop_4) measurements near 298.15 K were found in the ThermoML database:

### Block Summary

| # | DOI | Block | GLOBlit | Total pts | Composition variable | T range (K) |
|---|-----|-------|---------|-----------|---------------------|-------------|
| 1 | 10.1016/j.jct.2006.12.012 | PROPblock_3 | GLOBlit_2781 | 120 | Mole fraction (GLOBvar_2) | 298.15–318.15 |
| 2 | 10.1021/je9001027 | PROPblock_3 | GLOBlit_11517 | 35 | Mass fraction (GLOBvar_5) | 298.15–318.15 |

Both blocks report data at exactly 298.15 K with a pressure constraint of 101.0 kPa.

### Block 1 — Data at 298.15 K (mole-fraction basis, GLOBlit_2781::PROPblock_3)

24 data points at 298.15 K spanning x(DMSO) = 0–1. Representative inspected rows:

| x(DMSO) | η (Pa·s) |
|---------|----------|
| 0 | 0.0008901 |
| 0.0238 | 0.0010331 |
| 0.0489 | 0.0012576 |
| 0.1587 | 0.0025493 |
| 0.2036 | 0.0030165 |
| 0.2768 | 0.0035372 |
| 0.3335 | 0.0037144 |
| 0.3638 | 0.0037353 |
| 0.3906 | 0.0037169 |
| 0.4412 | 0.0036062 |
| 0.5193 | 0.0033124 |
| 0.6195 | 0.0028832 |
| 0.7595 | 0.0024317 |
| 0.8856 | 0.0021754 |
| 1 | 0.001996 |

### Block 2 — Data at 298.15 K (mass-fraction basis, GLOBlit_11517::PROPblock_3)

7 data points at 298.15 K spanning w(DMSO) = 0–1:

| w(DMSO) | η (Pa·s) |
|---------|----------|
| 0 | 0.00089 |
| 0.2 | 0.00134 |
| 0.4 | 0.002221 |
| 0.5 | 0.0028073 |
| 0.6 | 0.003421 |
| 0.7 | 0.0023568 |
| 1 | 0.001966 |

**Chemistry insight:** Both datasets clearly show the well-known viscosity maximum in the DMSO–water system. In Block 1, the maximum viscosity of 0.0037353 Pa·s occurs at x(DMSO) = 0.3638, which is roughly 4.2× higher than pure water (0.0008901 Pa·s) and roughly 1.9× higher than pure DMSO (0.001996 Pa·s) (both ratios computed from the inspected data rows above). In Block 2, the maximum of 0.003421 Pa·s appears at w(DMSO) = 0.6. This pronounced viscosity maximum is attributed to strong hydrogen-bonding interactions between DMSO and water that form structured DMSO·2H₂O complexes, enhancing intermolecular friction in this composition range.
</answer>