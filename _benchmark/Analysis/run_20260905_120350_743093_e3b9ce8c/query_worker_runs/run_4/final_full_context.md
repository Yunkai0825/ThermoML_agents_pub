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
Find refractive index, speed of sound, surface tension, or heat capacity data for DMSO + water near 25°C

## Instruction
Search for binary mixture blocks containing dimethyl sulfoxide (DMSO) and water with refractive index (GLOBprop_7), speed of sound (GLOBprop_8), surface tension (GLOBprop_13), or heat capacity (GLOBprop_9) measurements near 298.15 K. Return DOIs, block numbers, property types.

## ID Catalog (from working memory)
[]

## Assistant
(syntax-rejected turn — malformed tool calls never executed; corrected on a later turn. Full detail in the run log.)

## User
(validation fired earlier — corrected)

## Assistant
<summary>Resolving DMSO and water compound IDs to search for binary mixture data.</summary>
<tool_call>resolve_compound_ids(queries=['dimethyl sulfox…, min_score=50, limit=5)</tool_call>

## User
<tool_result>
Both compounds resolved with exact name matches.

| Compound | Global ID | Formula | SMILES |
|---|---|---|---|
| dimethyl sulfoxide | GLOBcomp_31 | C2H6OS | CS(C)=O |
| water | GLOBcomp_1 | H2O | O |
</tool_result>

## Assistant
<summary>DMSO = GLOBcomp_31, water = GLOBcomp_1. Now searching for binary blocks with refractive index, speed of sound, surface tension, or heat capacity near 298.15 K.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_31', 'GLOBcomp_1'], property=['GLOBprop_7', 'G…, system_typ…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Correcting temperature_range to list[float] format and re-searching for DMSO+water binary blocks with refractive index, speed of sound, surface tension, or heat capacity.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_31', 'GLOBcomp_1'], property=['GLOBprop_7', 'G…, system_typ…)</tool_call>

## User
<tool_result>
**Summary:** Three blocks found for DMSO (GLOBcomp_31) + water (GLOBcomp_1) binary mixtures covering speed of sound, surface tension, and refractive index near 298.15 K. No heat capacity (GLOBprop_9) data was returned.

### Blocks Overview

| Block | DOI | GLOBlit | Property | GLOBprop | Pts | T range (K) | x(DMSO) range |
|---|---|---|---|---|---|---|---|
| PROPblock_3 | 10.1016/j.jct.2006.01.007 | GLOBlit_2652 | Speed of sound (m/s) | GLOBprop_8 | 6 | 288.15–313.15 | 0.0385 (fixed) |
| PROPblock_9 | 10.1021/je7001013 | GLOBlit_10766 | Surface tension (N/m) | GLOBprop_13 | 112 (25 kept) | 298.15–313.15 | 0.0121–0.8945 |
| PROPblock_10 | 10.1021/je7001013 | GLOBlit_10766 | Refractive index (Na D-line) | GLOBprop_7 | 33 (18 kept) | 298.15–308.15 | 0.0121–0.7685 |

### Data at 298.15 K

**Speed of sound** (PROPblock_3) — single composition x(DMSO)=0.0385, P=101.0 kPa:
| T(K) | u(m/s) | ±U |
|---|---|---|
| 298.15 | 1568.53 | 0.78 |

**Surface tension** (PROPblock_9) at 298.15 K:
| x(DMSO) | γ (N/m) | ±U |
|---|---|---|
| 0.0121 | 0.071 | 0.0005 |
| 0.1044 | 0.0612 | 0.0004 |
| 0.2999 | 0.0533 | 0.0004 |
| 0.4523 | 0.0503 | 0.0004 |
| 0.59 | 0.046
</tool_result>

## Assistant


<reasoning>
I have found three blocks with data for DMSO + water binary mixtures near 298.15 K:
1. Speed of sound (PROPblock_3, GLOBlit_2652)
2. Surface tension (PROPblock_9, GLOBlit_10766)
3. Refractive index (PROPblock_10, GLOBlit_10766)

No heat capacity data was found. I have enough information to provide a complete answer. Let me compile the results.
</reasoning>

<answer>
## DMSO + Water Binary Mixture Data Near 25 °C

Three data blocks were found in the ThermoML database for dimethyl sulfoxide (DMSO, GLOBcomp_31) + water (GLOBcomp_1) binary mixtures with refractive index, speed of sound, or surface tension measurements near 298.15 K. **No heat capacity (Cp) data** was found for this system.

### Summary of Available Blocks

| Block | DOI | Literature ID | Property | Pts | T range (K) |
|---|---|---|---|---|---|
| PROPblock_3 | 10.1016/j.jct.2006.01.007 | GLOBlit_2652 | Speed of sound (m/s) | 6 | 288.15–313.15 |
| PROPblock_9 | 10.1021/je7001013 | GLOBlit_10766 | Surface tension (N/m) | 112 | 298.15–313.15 |
| PROPblock_10 | 10.1021/je7001013 | GLOBlit_10766 | Refractive index (Na D-line) | 33 | 298.15–308.15 |

### Representative Data at 298.15 K

**Speed of sound** (GLOBlit_2652 :: PROPblock_3) — single composition x(DMSO) = 0.0385, P = 101.0 kPa:
- u = 1568.53 ± 0.78 m/s

**Surface tension** (GLOBlit_10766 :: PROPblock_9) at 298.15 K spans x(DMSO) = 0.0121–0.89, showing a monotonic decrease from γ ≈ 0.071 N/m (near pure water) to γ ≈ 0.046 N/m at x(DMSO) ≈ 0.59. Selected values:

| x(DMSO) | γ (N/m) | ±U |
|---|---|---|
| 0.0121 | 0.071 | 0.0005 |
| 0.1044 | 0.0612 | 0.0004 |
| 0.2999 | 0.0533 | 0.0004 |
| 0.4523 | 0.0503 | 0.0004 |
| 0.59 | 0.046 | — |

**Refractive index** (GLOBlit_10766 :: PROPblock_10) covers x(DMSO) = 0.0121–0.7685 at 298.15–308.15 K.

### Chemistry Insight
The surface tension data illustrate the well-known surface-active behavior of DMSO in aqueous solution: even modest additions of DMSO sharply reduce the surface tension from the pure-water value (~0.072 N/m), with the steepest drop occurring in the dilute DMSO region (x < 0.1). This reflects DMSO's preferential adsorption at the air–water interface. The speed of sound datum at x(DMSO) = 0.0385 (1568.53 m/s) is notably higher than the pure-water value (~1497 m/s at 298.15 K), consistent with the known maximum in the speed of sound for DMSO–water mixtures at low DMSO mole fractions, arising from strong hydrogen-bonding interactions between DMSO and water.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_BLOCK** PROPblock_3 + PROPblock_9 + PROPblock_10: PROPblock_3 + PROPblock_9 + PROPblock_10 is quoted with data values (288.15, 313.15, 112, 298.15, …) but was never inspected in this run (values 288.15, 313.15, 298.15, 313.15 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_2652::PROPblock_3"); inspect_block_table(block_number="GLOBlit_10766::PROPblock_9"); inspect_block_table(block_number="GLOBlit_10766::PROPblock_10")`
- **UNINSPECTED_BLOCK** PROPblock_10: PROPblock_10 is quoted with data values (298.15, …) but was never inspected in this run (values 298.15 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_10766::PROPblock_10")`
- **UNINSPECTED_BLOCK** GLOBlit_2652::PROPblock_3: GLOBlit_2652::PROPblock_3 is quoted with data values (0.0385, 101.0, 1568.53, 0.78, …) but was never inspected in this run (values 0.0385, 101.0, 1568.53 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_2652::PROPblock_3")`
- **UNINSPECTED_BLOCK** GLOBlit_10766::PROPblock_9: GLOBlit_10766::PROPblock_9 is quoted with data values (298.15, 0.0121, 0.89, 0.071, …) but was never inspected in this run (values 298.15, 0.0121, 0.89, 0.071 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_10766::PROPblock_9")`
- **UNINSPECTED_BLOCK** GLOBlit_10766::PROPblock_9: GLOBlit_10766::PROPblock_9 is quoted with data values (0.0121, 0.071, 0.0005, 0.1044, …) but was never inspected in this run (values 0.0121, 0.071, 0.0005, 0.1044 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_10766::PROPblock_9")`
- **UNINSPECTED_BLOCK** GLOBlit_10766::PROPblock_10: GLOBlit_10766::PROPblock_10 is quoted with data values (0.0121, 0.7685, 298.15, 308.15, …) but was never inspected in this run (values 0.0121, 0.7685, 298.15, 308.15 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_10766::PROPblock_10")`

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## Assistant
<summary>Inspecting all three blocks (GLOBlit_2652::PROPblock_3, GLOBlit_10766::PROPblock_9, GLOBlit_10766::PROPblock_10) to ground data values before re-assembling the answer.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_2652::PROPblock_3)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2006.01.007 [GLOBlit_2652] :: PROPblock_3 (binary: dimethyl sulfoxide + water)
filter: none (whole block)
block constraints: mole_fraction_dimethyl_sulfoxide = 0.0385; pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mole_fraction_<dimethyl sulfoxide> | pressure_kpa | speed_of_sound_m_s |
|---|---|---|---|---|
| BLKpoint_1 | 288.15 | 0.0385 | 101.0 | 1555.18 |
| BLKpoint_2 | 293.15 | 0.0385 | 101.0 | 1562.46 |
| BLKpoint_3 | 298.15 | 0.0385 | 101.0 | 1568.53 |
| BLKpoint_4 | 303.15 | 0.0385 | 101.0 | 1573.38 |
| BLKpoint_5 | 308.15 | 0.0385 | 101.0 | 1577 |
| BLKpoint_6 | 313.15 | 0.0385 | 101.0 | 1579.41 |

mode: complete — all 6 matched rows shown (block has 6)
topology: speed_of_sound_m_s vs temperature_k: monotonic↑
stats (matched, n=6): temperature_k 288.15–313.15 (n=6); mole_fraction_dimethyl_sulfoxide 0.0385–0.0385 (n=6); pressure_kpa 101.0–101.0 (n=6); speed_of_sound_m_s 1555.18–1579.41 (n=6)
inspection_id: INSP_859c666658c3
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>PROPblock_3 inspected: 6 points, speed of sound 1555.18–1579.41 m/s, T 288.15–313.15 K, x(DMSO)=0.0385, P=101.0 kPa. Now inspecting PROPblock_9 and PROPblock_10.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_10766::PROPblock_9, where=temperature_k = 2…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je7001013 [GLOBlit_10766] :: PROPblock_9 (binary: dimethyl sulfoxide + water)
filter: where temperature_k = 298.15

| BLKpoint_id | temperature_k | mole_fraction_<dimethyl sulfoxide> | surface_tension_liquidgas_n_m |
|---|---|---|---|
| BLKpoint_1 | 298.15 | 0.0121 | 0.071 |
| BLKpoint_3 | 298.15 | 0.1044 | 0.0612 |
| BLKpoint_4 | 298.15 | 0.1979 | 0.0567 |
| BLKpoint_5 | 298.15 | 0.2507 | 0.0554 |
| BLKpoint_6 | 298.15 | 0.2999 | 0.0533 |
| BLKpoint_8 | 298.15 | 0.3536 | 0.0526 |
| BLKpoint_11 | 298.15 | 0.4523 | 0.0503 |
| BLKpoint_12 | 298.15 | 0.501 | 0.0483 |
| BLKpoint_13 | 298.15 | 0.59 | 0.046 |
| BLKpoint_14 | 298.15 | 0.7027 | 0.044 |
| BLKpoint_15 | 298.15 | 0.8088 | 0.0426 |
| BLKpoint_16 | 298.15 | 0.8945 | 0.042 |

mode: RDP — 12 of 16 matched rows shown (shape-preserving; block has 112). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=16): temperature_k 298.15–298.15 (n=16); mole_fraction_dimethyl_sulfoxide 0.0121–0.8945 (n=16); surface_tension_liquidgas_n_m 0.042–0.071 (n=16)
stats (full block, n=112): temperature_k 298.15–328.15 (n=112); mole_fraction_dimethyl_sulfoxide 0.0121–0.8945 (n=112); surface_tension_liquidgas_n_m 0.0387–0.071 (n=112)
inspection_id: INSP_4c118f2b8c2e
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>PROPblock_9 inspected: 16 matched rows at 298.15 K (12 shown via RDP), surface tension 0.042–0.071 N/m, x(DMSO) 0.0121–0.8945. Now inspecting PROPblock_10.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_10766::PROPblock_10, where=temperature_k = 2…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je7001013 [GLOBlit_10766] :: PROPblock_10 (binary: dimethyl sulfoxide + water)
filter: where temperature_k = 298.15
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mole_fraction_<dimethyl sulfoxide> | pressure_kpa | refractive_index_na_dline |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 0.0121 | 101.0 | 1.34 |
| BLKpoint_2 | 298.15 | 0.0202 | 101.0 | 1.344 |
| BLKpoint_3 | 298.15 | 0.1467 | 101.0 | 1.396 |
| BLKpoint_4 | 298.15 | 0.2455 | 101.0 | 1.4215 |
| BLKpoint_5 | 298.15 | 0.2959 | 101.0 | 1.4305 |
| BLKpoint_6 | 298.15 | 0.3213 | 101.0 | 1.4345 |
| BLKpoint_7 | 298.15 | 0.3713 | 101.0 | 1.4415 |
| BLKpoint_8 | 298.15 | 0.3967 | 101.0 | 1.4445 |
| BLKpoint_9 | 298.15 | 0.4301 | 101.0 | 1.4475 |
| BLKpoint_10 | 298.15 | 0.5964 | 101.0 | 1.461 |
| BLKpoint_11 | 298.15 | 0.7685 | 101.0 | 1.47 |

mode: complete — all 11 matched rows shown (block has 33)
stats (matched, n=11): temperature_k 298.15–298.15 (n=11); mole_fraction_dimethyl_sulfoxide 0.0121–0.7685 (n=11); pressure_kpa 101.0–101.0 (n=11); refractive_index_na_dline 1.34–1.47 (n=11)
stats (full block, n=33): temperature_k 298.15–308.15 (n=33); mole_fraction_dimethyl_sulfoxide 0.0121–0.7685 (n=33); pressure_kpa 101.0–101.0 (n=33); refractive_index_na_dline 1.339–1.47 (n=33)
inspection_id: INSP_6c692cd44b0e
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<answer>
## DMSO + Water Binary Mixture Data Near 25 °C

Three data blocks were found in the ThermoML database for dimethyl sulfoxide (DMSO, GLOBcomp_31) + water (GLOBcomp_1) binary mixtures with refractive index, speed of sound, or surface tension measurements near 298.15 K. **No heat capacity (Cp) data** was found for this system.

### Summary of Available Blocks

| Block | DOI | Literature ID | Property | Total Pts | T range (K) |
|---|---|---|---|---|---|
| PROPblock_3 | 10.1016/j.jct.2006.01.007 | GLOBlit_2652 | Speed of sound (m/s) | 6 | 288.15–313.15 |
| PROPblock_9 | 10.1021/je7001013 | GLOBlit_10766 | Surface tension (N/m) | 112 | 298.15–328.15 |
| PROPblock_10 | 10.1021/je7001013 | GLOBlit_10766 | Refractive index (Na D-line) | 33 | 298.15–308.15 |

### Representative Data at 298.15 K

**Speed of sound** (GLOBlit_2652 :: PROPblock_3) — fixed composition x(DMSO) = 0.0385, P = 101.0 kPa:

| T (K) | u (m/s) |
|---|---|
| 298.15 | 1568.53 |

The full block spans 288.15–313.15 K with speed of sound ranging from 1555.18 to 1579.41 m/s (6 points, monotonically increasing with temperature).

**Surface tension** (GLOBlit_10766 :: PROPblock_9) at 298.15 K — 16 compositions measured, x(DMSO) = 0.0121–0.8945:

| x(DMSO) | γ (N/m) |
|---|---|
| 0.0121 | 0.071 |
| 0.1044 | 0.0612 |
| 0.1979 | 0.0567 |
| 0.2507 | 0.0554 |
| 0.2999 | 0.0533 |
| 0.3536 | 0.0526 |
| 0.4523 | 0.0503 |
| 0.501 | 0.0483 |
| 0.59 | 0.046 |
| 0.7027 | 0.044 |
| 0.8088 | 0.0426 |
| 0.8945 | 0.042 |

**Refractive index** (GLOBlit_10766 :: PROPblock_10) at 298.15 K, P = 101.0 kPa — 11 compositions, x(DMSO) = 0.0121–0.7685:

| x(DMSO) | n_D |
|---|---|
| 0.0121 | 1.34 |
| 0.0202 | 1.344 |
| 0.1467 | 1.396 |
| 0.2455 | 1.4215 |
| 0.2959 | 1.4305 |
| 0.3213 | 1.4345 |
| 0.3713 | 1.4415 |
| 0.3967 | 1.4445 |
| 0.4301 | 1.4475 |
| 0.5964 | 1.461 |
| 0.7685 | 1.47 |

### Chemistry Insight

The surface tension data show a steep initial drop from γ = 0.071 N/m at x(DMSO) = 0.0121 to 0.0612 N/m at x(DMSO) = 0.1044, followed by a more gradual decrease to 0.042 N/m at x(DMSO) = 0.8945. This steep initial decline reflects DMSO's preferential adsorption at the air–water interface at low concentrations. The refractive index increases monotonically from 1.34 to 1.47 across the composition range, consistent with the higher polarizability of DMSO compared to water.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **MISATTRIBUTED_VALUE** GLOBlit_10766::PROPblock_10: 0.071 does not belong to GLOBlit_10766::PROPblock_10; it matches only GLOBlit_10766::PROPblock_9 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 0.071 to GLOBlit_10766::PROPblock_9 — no new tool call needed`
- **MISATTRIBUTED_VALUE** GLOBlit_10766::PROPblock_10: 0.0612 does not belong to GLOBlit_10766::PROPblock_10; it matches only GLOBlit_10766::PROPblock_9 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 0.0612 to GLOBlit_10766::PROPblock_9 — no new tool call needed`
- **MISATTRIBUTED_VALUE** GLOBlit_10766::PROPblock_10: 0.1044 does not belong to GLOBlit_10766::PROPblock_10; it matches only GLOBlit_10766::PROPblock_9 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 0.1044 to GLOBlit_10766::PROPblock_9 — no new tool call needed`
- **MISATTRIBUTED_VALUE** GLOBlit_10766::PROPblock_10: 0.042 does not belong to GLOBlit_10766::PROPblock_10; it matches only GLOBlit_10766::PROPblock_9 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 0.042 to GLOBlit_10766::PROPblock_9 — no new tool call needed`
- **MISATTRIBUTED_VALUE** GLOBlit_10766::PROPblock_10: 0.8945 does not belong to GLOBlit_10766::PROPblock_10; it matches only GLOBlit_10766::PROPblock_9 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 0.8945 to GLOBlit_10766::PROPblock_9 — no new tool call needed`
Inspected so far: PROPblock_10, PROPblock_3, PROPblock_9

Verified as grounded — correct as quoted, keep unchanged:
- PROPblock_3 + PROPblock_9 + PROPblock_10: 288.15, 313.15, 112, 298.15, 328.15, 33, 308.15
- PROPblock_10: 298.15
- GLOBlit_2652::PROPblock_3: 0.0385, 101.0, 298.15, 1568.53, 288.15, 313.15, 1555.18, 1579.41
- GLOBlit_10766::PROPblock_9: 298.15, 16, 0.0121, 0.8945, 0.071, 0.1044, 0.0612, 0.1979, 0.0567, 0.2507, 0.0554, 0.2999, 0.0533, 0.3536, 0.0526, 0.4523, 0.0503, 0.501, 0.0483, 0.59, 0.046, 0.7027, 0.044, 0.8088, 0.0426, 0.042
Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- GLOBlit_10766::PROPblock_10: 298.15, 101.0, 0.0121, 0.7685, 1.34, 0.0202, 1.344, 0.1467, 1.396, 0.2455, 1.4215, 0.2959, 1.4305, 0.3213, 1.4345, 0.3713, 1.4415, 0.3967, 1.4445, 0.4301, 1.4475, 0.5964, 1.461, 1.47

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## LLM Response
<reasoning>
The misattribution errors are in the Chemistry Insight paragraph at the end. The values 0.071, 0.0612, 0.1044, 0.042, and 0.8945 are from PROPblock_9 (surface tension) but are mentioned in the insight paragraph in a way that the validator interprets as being attributed to PROPblock_10 (refractive index). I need to make sure the insight paragraph clearly attributes these values to PROPblock_9, not PROPblock_10.

Looking at the insight paragraph:
"The surface tension data show a steep initial drop from γ = 0.071 N/m at x(DMSO) = 0.0121 to 0.0612 N/m at x(DMSO) = 0.1044, followed by a more gradual decrease to 0.042 N/m at x(DMSO) = 0.8945."

These values are correctly described as surface tension data, but the paragraph follows immediately after the refractive index section, so the validator may be associating them with PROPblock_10. I need to explicitly re-anchor them to PROPblock_9 in the text.

Similarly: "The refractive index increases monotonically from 1.34 to 1.47 across the composition range" - these are correctly from PROPblock_10.

I'll fix the insight paragraph to explicitly cite the block anchors.
</reasoning>

<answer>
## DMSO + Water Binary Mixture Data Near 25 °C

Three data blocks were found in the ThermoML database for dimethyl sulfoxide (DMSO, GLOBcomp_31) + water (GLOBcomp_1) binary mixtures with refractive index, speed of sound, or surface tension measurements near 298.15 K. **No heat capacity (Cp) data** was found for this system.

### Summary of Available Blocks

| Block | DOI | Literature ID | Property | Total Pts | T range (K) |
|---|---|---|---|---|---|
| PROPblock_3 | 10.1016/j.jct.2006.01.007 | GLOBlit_2652 | Speed of sound (m/s) | 6 | 288.15–313.15 |
| PROPblock_9 | 10.1021/je7001013 | GLOBlit_10766 | Surface tension (N/m) | 112 | 298.15–328.15 |
| PROPblock_10 | 10.1021/je7001013 | GLOBlit_10766 | Refractive index (Na D-line) | 33 | 298.15–308.15 |

### Representative Data at 298.15 K

**Speed of sound** (GLOBlit_2652 :: PROPblock_3) — fixed composition x(DMSO) = 0.0385, P = 101.0 kPa:

| T (K) | u (m/s) |
|---|---|
| 298.15 | 1568.53 |

The full block spans 288.15–313.15 K with speed of sound ranging from 1555.18 to 1579.41 m/s (6 points, monotonically increasing with temperature).

**Surface tension** (GLOBlit_10766 :: PROPblock_9) at 298.15 K — 16 compositions measured, x(DMSO) = 0.0121–0.8945:

| x(DMSO) | γ (N/m) |
|---|---|
| 0.0121 | 0.071 |
| 0.1044 | 0.0612 |
| 0.1979 | 0.0567 |
| 0.2507 | 0.0554 |
| 0.2999 | 0.0533 |
| 0.3536 | 0.0526 |
| 0.4523 | 0.0503 |
| 0.501 | 0.0483 |
| 0.59 | 0.046 |
| 0.7027 | 0.044 |
| 0.8088 | 0.0426 |
| 0.8945 | 0.042 |

**Refractive index** (GLOBlit_10766 :: PROPblock_10) at 298.15 K, P = 101.0 kPa — 11 compositions, x(DMSO) = 0.0121–0.7685:

| x(DMSO) | n_D |
|---|---|
| 0.0121 | 1.34 |
| 0.0202 | 1.344 |
| 0.1467 | 1.396 |
| 0.2455 | 1.4215 |
| 0.2959 | 1.4305 |
| 0.3213 | 1.4345 |
| 0.3713 | 1.4415 |
| 0.3967 | 1.4445 |
| 0.4301 | 1.4475 |
| 0.5964 | 1.461 |
| 0.7685 | 1.47 |

### Chemistry Insight

From the surface tension block (GLOBlit_10766 :: PROPblock_9), the data show a steep initial drop from γ = 0.071 N/m at x(DMSO) = 0.0121 to 0.0612 N/m at x(DMSO) = 0.1044, followed by a more gradual decrease to 0.042 N/m at x(DMSO) = 0.8945. This steep initial decline reflects DMSO's preferential adsorption at the air–water interface at low concentrations. From the refractive index block (GLOBlit_10766 :: PROPblock_10), the refractive index increases monotonically from 1.34 to 1.47 across the composition range x(DMSO) = 0.0121–0.7685, consistent with the higher polarizability of DMSO compared to water.
</answer>