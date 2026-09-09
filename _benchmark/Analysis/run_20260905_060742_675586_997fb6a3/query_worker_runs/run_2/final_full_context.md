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
Find binary density data for DMF + water at 298.15 K

## Instruction
Search for blocks containing both N,N-dimethylformamide (DMF, GLOBcomp_18) and water (GLOBcomp_1) with mass density (GLOBprop_1) at temperature 298.15 K. Return DOIs, block numbers, row counts, composition ranges. Need mixture density across the full composition range.

## ID Catalog (from working memory)
[]

## Assistant
<summary>Searching for binary density blocks containing DMF (GLOBcomp_18) and water (GLOBcomp_1) with mass density (GLOBprop_1) at ~298.15 K.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_18', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Fixing the temperature_range argument to be a list of floats [297.0, 300.0] and re-calling search_blocks for DMF + water binary density data.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_18', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary…)</tool_call>

## User
<tool_result>
**Summary:** 11 binary DMF + water mass density blocks found near 298.15 K, all score 100. They span various composition variables (mole fraction, mass fraction, molality) and cover the full composition range. The largest datasets are from `10.1021/je700671t [GLOBlit_11030]` (210 pts) and `10.1016/j.jct.2005.07.012 [GLOBlit_2584]` (128 pts).

| # | DOI | Block | Pts | Lit ID | Comp. Variable | Comp. Range | ρ Range (kg/m³) | T Info |
|---|-----|-------|-----|--------|---------------|-------------|-----------------|--------|
| 1 | 10.1016/j.fluid.2014.08.026 | PROPblock_5 | 4 | GLOBlit_1540 | w(DMF) | 0.1–0.4 | 996.25–997.05 | constrained |
| 2 | 10.1016/j.jct.2005.07.012 | PROPblock_9 | 128 | GLOBlit_2584 | x(water) | 0.0272–0.9974 | 950.03–1003.75 | var 288.15–293.15 |
| 3 | 10.1016/j.jct.2007.05.015 | PROPblock_18 | 40 | GLOBlit_2834 | x(DMF) | 0–1 | 943.94–997.02 | constrained |
| 4 | 10.1016/j.jct.2012.04.007 | PROPblock_3 | 55 | GLOBlit_3614 | x(water) | 0.0002–0.0118 | 924.69–963.47 | var 278.15–318.15 |
| 5 | 10.1016/j.jct.2014.05.003 | PROPblock_1 | 3 | GLOBlit_4166 | w(DMF) | 0.1–0.3 | 996.3–996.9 | constrained |
| 6 | 10.1016/j.jct.2014.05.013 | PROPblock_19 | 18 | GLOBlit_4174 | w(DMF) | 0–1 | 934.39–1003.56
</tool_result>

## Assistant


<reasoning>
I have good results from the search. Let me compile the findings. The tool returned 11 blocks of binary DMF + water mass density data near 298.15 K. I should present the key findings including DOIs, block numbers, row counts, composition ranges, and density ranges. Let me also note which datasets cover the full composition range vs. partial ranges.

Looking at the results:
1. GLOBlit_1540 / PROPblock_5 - only 4 points, w(DMF) 0.1-0.4 (partial)
2. GLOBlit_2584 / PROPblock_9 - 128 points, x(water) 0.0272-0.9974 (full range), but T varies 288.15-293.15 (may not include 298.15 K exactly)
3. GLOBlit_2834 / PROPblock_18 - 40 points, x(DMF) 0-1 (full range), constrained T
4. GLOBlit_3614 / PROPblock_3 - 55 points, x(water) 0.0002-0.0118 (very narrow, water-dilute)
5. GLOBlit_4166 / PROPblock_1 - 3 points, w(DMF) 0.1-0.3 (partial)
6. GLOBlit_4174 / PROPblock_19 - 18 points, w(DMF) 0-1 (full range)

And the remaining 5 blocks from the truncated results. The summary mentions GLOBlit_11030 with 210 points as the largest dataset.

I have enough information to provide a comprehensive answer. The key datasets covering the full composition range at 298.15 K appear to be:
- GLOBlit_2834 / PROPblock_18 (40 pts, x(DMF) 0-1, constrained T)
- GLOBlit_4174 / PROPblock_19 (18 pts, w(DMF) 0-1)
- GLOBlit_11030 (210 pts - largest dataset)

Let me provide the answer with all the information I have.
</reasoning>

<answer>
## Binary Density Data: DMF + Water at 298.15 K

**11 binary blocks** were found in ThermoML containing both N,N-dimethylformamide (DMF, GLOBcomp_18) and water (GLOBcomp_1) with mass density (GLOBprop_1) near 298.15 K.

### Key Datasets

| # | DOI | Lit ID | Block | Points | Comp. Variable | Comp. Range | ρ Range (kg/m³) | T Note |
|---|-----|--------|-------|--------|----------------|-------------|-----------------|--------|
| 1 | 10.1016/j.fluid.2014.08.026 | GLOBlit_1540 | PROPblock_5 | 4 | w(DMF) | 0.1–0.4 | 996.25–997.05 | constrained |
| 2 | 10.1016/j.jct.2005.07.012 | GLOBlit_2584 | PROPblock_9 | 128 | x(water) | 0.0272–0.9974 | 950.03–1003.75 | var 288.15–293.15 |
| 3 | 10.1016/j.jct.2007.05.015 | GLOBlit_2834 | PROPblock_18 | 40 | x(DMF) | 0–1 | 943.94–997.02 | constrained |
| 4 | 10.1016/j.jct.2012.04.007 | GLOBlit_3614 | PROPblock_3 | 55 | x(water) | 0.0002–0.0118 | 924.69–963.47 | var 278.15–318.15 |
| 5 | 10.1016/j.jct.2014.05.003 | GLOBlit_4166 | PROPblock_1 | 3 | w(DMF) | 0.1–0.3 | 996.3–996.9 | constrained |
| 6 | 10.1016/j.jct.2014.05.013 | GLOBlit_4174 | PROPblock_19 | 18 | w(DMF) | 0–1 | 934.39–1003.56 | constrained |

Additional blocks were found (up to 11 total), with the largest dataset from **10.1021/je700671t (GLOBlit_11030)** containing **210 data points**.

### Best Candidates for Full Composition Range at 298.15 K

1. **GLOBlit_2834 / PROPblock_18** — 40 points spanning x(DMF) = 0 to 1, with constrained temperature (likely at 298.15 K). Density ranges from 943.94 to 997.02 kg/m³. This is an excellent full-range dataset.

2. **GLOBlit_4174 / PROPblock_19** — 18 points spanning w(DMF) = 0 to 1 (mass fraction basis), density 934.39–1003.56 kg/m³, constrained temperature.

3. **GLOBlit_11030** — 210 points (largest dataset), likely multi-temperature but should contain 298.15 K isotherms.

4. **GLOBlit_2584 / PROPblock_9** — 128 points with near-full composition coverage (x(water) 0.0272–0.9974), but the temperature variable range is listed as 288.15–293.15 K, which may not extend to 298.15 K.

**Note:** Blocks with "constrained" temperature are most likely fixed at 298.15 K. Blocks with variable temperature (GLOBlit_2584, GLOBlit_3614) contain multi-temperature data and would need filtering to the 298.15 K isotherm. The density trend shows that pure DMF (~943.9 kg/m³) is less dense than pure water (~997.0 kg/m³), with the mixture density varying non-linearly across composition.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_BLOCK** PROPblock_5 + PROPblock_9 + PROPblock_18 + PROPblock_3 + PROPblock_1 + PROPblock_19: PROPblock_5 + PROPblock_9 + PROPblock_18 + PROPblock_3 + PROPblock_1 + PROPblock_19 is quoted with data values (0.1, 0.4, 996.25, 997.05, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_5", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_9", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_18", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_1", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_19", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_19: PROPblock_19 is quoted with data values (210, 298.15, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_19", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_18: PROPblock_18 is quoted with data values (40, 298.15, 943.94, 997.02, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_18", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_19: PROPblock_19 is quoted with data values (18, 934.39, 1003.56, 210, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_19", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_9: PROPblock_9 is quoted with data values (128, 0.0272, 0.9974, 288.15, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_9", literature="<GLOBlit_N or DOI>")`

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## Assistant
<summary>Running inspect_block_table on the three most relevant full-range blocks: GLOBlit_2834/PROPblock_18, GLOBlit_4174/PROPblock_19, and GLOBlit_2584/PROPblock_9 to ground the data values.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_18, literature=GLOBlit_2834)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2007.05.015 [GLOBlit_2834] :: PROPblock_18 (binary: dimethylformamide + water)
filter: none (whole block)
block constraints: pressure_kpa = 101.0; temperature_k = 298.15

| BLKpoint_id | mole_fraction_<dimethylformamide> | pressure_kpa | temperature_k | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 0 | 101.0 | 298.15 | 997.02 |
| BLKpoint_2 | 0.01233 | 101.0 | 298.15 | 996.44 |
| BLKpoint_3 | 0.0266 | 101.0 | 298.15 | 996.21 |
| BLKpoint_4 | 0.0276 | 101.0 | 298.15 | 996.23 |
| BLKpoint_5 | 0.04154 | 101.0 | 298.15 | 996.18 |
| BLKpoint_9 | 0.11728 | 101.0 | 298.15 | 997.02 |
| BLKpoint_10 | 0.14116 | 101.0 | 298.15 | 996.93 |
| BLKpoint_13 | 0.23003 | 101.0 | 298.15 | 993.87 |
| BLKpoint_14 | 0.28661 | 101.0 | 298.15 | 990.18 |
| BLKpoint_15 | 0.31385 | 101.0 | 298.15 | 989.17 |
| BLKpoint_16 | 0.37711 | 101.0 | 298.15 | 984.28 |
| BLKpoint_38 | 0.92495 | 101.0 | 298.15 | 948.01 |
| BLKpoint_39 | 0.96614 | 101.0 | 298.15 | 946.28 |
| BLKpoint_40 | 1 | 101.0 | 298.15 | 943.94 |

mode: RDP — 14 of 40 matched rows shown (shape-preserving; block has 40). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
topology: mass_density_kg_m3 vs mole_fraction_dimethylformamide: non-monotonic(4 extrema)
stats (matched, n=40): mole_fraction_dimethylformamide 0–1 (n=40); pressure_kpa 101.0–101.0 (n=40); temperature_k 298.15–298.15 (n=40); mass_density_kg_m3 943.94–997.02 (n=40)
inspection_id: INSP_440a0c0a80b2
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_2834/PROPblock_18: 40 pts at 298.15 K, x(DMF) 0–1, ρ 943.94–997.02 kg/m³. Now inspecting GLOBlit_4174/PROPblock_19 and GLOBlit_2584/PROPblock_9.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_19, literature=GLOBlit_4174)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2014.05.013 [GLOBlit_4174] :: PROPblock_19 (binary: dimethylformamide + water)
filter: none (whole block)
block constraints: pressure_kpa = 100.0

| BLKpoint_id | temperature_k | mass_fraction_<dimethylformamide> | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 288.15 | 0 | 100.0 | 999 |
| BLKpoint_3 | 288.15 | 0.4 | 100.0 | 1003.56 |
| BLKpoint_4 | 288.15 | 0.6 | 100.0 | 1001.34 |
| BLKpoint_5 | 288.15 | 0.8 | 100.0 | 986.63 |
| BLKpoint_6 | 288.15 | 1 | 100.0 | 953.53 |
| BLKpoint_7 | 298.15 | 0 | 100.0 | 997 |
| BLKpoint_9 | 298.15 | 0.4 | 100.0 | 996.99 |
| BLKpoint_10 | 298.15 | 0.6 | 100.0 | 992.97 |
| BLKpoint_11 | 298.15 | 0.8 | 100.0 | 977.38 |
| BLKpoint_12 | 298.15 | 1 | 100.0 | 943.89 |
| BLKpoint_13 | 308.15 | 0 | 100.0 | 994.03 |
| BLKpoint_15 | 308.15 | 0.4 | 100.0 | 990 |
| BLKpoint_16 | 308.15 | 0.6 | 100.0 | 984.33 |
| BLKpoint_17 | 308.15 | 0.8 | 100.0 | 968.07 |
| BLKpoint_18 | 308.15 | 1 | 100.0 | 934.39 |

mode: RDP — 15 of 18 matched rows shown (shape-preserving; block has 18). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=18): temperature_k 288.15–308.15 (n=18); mass_fraction_dimethylformamide 0–1 (n=18); pressure_kpa 100.0–100.0 (n=18); mass_density_kg_m3 934.39–1003.56 (n=18)
inspection_id: INSP_3831ba56c42d
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<reasoning>
Now I have inspected two key blocks. Let me also inspect GLOBlit_2584/PROPblock_9 to verify its temperature range. But I also need to be efficient. Let me provide the answer now with the inspected data.

For GLOBlit_4174/PROPblock_19: At 298.15 K, the shown rows are BLKpoint_7 through BLKpoint_12, with w(DMF) = 0, 0.4, 0.6, 0.8, 1 and densities 997, 996.99, 992.97, 977.38, 943.89 kg/m³. The block has 18 total points across 3 temperatures (288.15, 298.15, 308.15 K), so only ~6 points at 298.15 K. The density range at 298.15 K is 943.89–997 kg/m³.

For GLOBlit_2834/PROPblock_18: 40 points all at 298.15 K, x(DMF) 0–1, ρ 943.94–997.02 kg/m³. This is the best full-range dataset at exactly 298.15 K.

I should note the search_blocks results gave me summary-level information (point counts, composition ranges, density ranges) for all 11 blocks. The data grounding issue is that I was quoting those summary values without inspection. For the blocks I haven't inspected, I should either inspect them or only reference them without specific data values.

Let me provide the answer using only inspected data for specific values, and for the other blocks just mention their existence without quoting specific numbers. I'll also note the search found 11 blocks total.

Actually, the search_blocks tool returned those summary values as part of its result. The grounding gate flagged them because they come from blocks I haven't individually inspected. But the search_blocks summary itself is a tool result. However, the rules say "before quoting any data point of a block, call inspect_block_table." The composition ranges and density ranges from search_blocks are aggregate summaries of the block, not individual data points. But the grounding gate still flagged them.

To be safe, I'll only quote values from the two inspected blocks and reference the other blocks without specific numerical values. For the remaining blocks I'll just note they exist.

Let me also note that the search_blocks result mentioned GLOBlit_11030 with 210 points - I haven't inspected that one. I should mention it exists but not quote specific values.
</reasoning>

<answer>
## Binary Density Data: DMF + Water at 298.15 K

**11 binary blocks** were found in ThermoML containing both N,N-dimethylformamide (DMF, GLOBcomp_18) and water (GLOBcomp_1) with mass density (GLOBprop_1) near 298.15 K.

### Best Full-Range Dataset: GLOBlit_2834 / PROPblock_18

**DOI:** 10.1016/j.jct.2007.05.015  
**40 data points**, all at T = 298.15 K and p = 101.0 kPa, spanning x(DMF) = 0 to 1.  
**Density range (n=40):** 943.94–997.02 kg/m³

Representative inspected rows:

| x(DMF) | ρ (kg/m³) |
|--------|-----------|
| 0 | 997.02 |
| 0.01233 | 996.44 |
| 0.0266 | 996.21 |
| 0.04154 | 996.18 |
| 0.11728 | 997.02 |
| 0.14116 | 996.93 |
| 0.23003 | 993.87 |
| 0.28661 | 990.18 |
| 0.31385 | 989.17 |
| 0.37711 | 984.28 |
| 0.92495 | 948.01 |
| 0.96614 | 946.28 |
| 1 | 943.94 |

The topology is **non-monotonic** (4 extrema), showing a density maximum near x(DMF) ≈ 0.12 where the mixture density equals or slightly exceeds that of pure water (~997 kg/m³), before decreasing toward pure DMF (943.94 kg/m³).

### Additional Full-Range Dataset: GLOBlit_4174 / PROPblock_19

**DOI:** 10.1016/j.jct.2014.05.013  
**18 total points** across three temperatures (288.15, 298.15, 308.15 K) at p = 100.0 kPa, using mass fraction w(DMF) = 0 to 1.

At 298.15 K specifically (inspected rows):

| w(DMF) | ρ (kg/m³) |
|--------|-----------|
| 0 | 997 |
| 0.4 | 996.99 |
| 0.6 | 992.97 |
| 0.8 | 977.38 |
| 1 | 943.89 |

This dataset has fewer composition points (~6 at 298.15 K) but confirms the same trend.

### Other Blocks Found (not individually inspected)

The search also returned blocks from the following sources, which may contain relevant 298.15 K data:

- **GLOBlit_11030** (10.1021/je700671t) — the largest dataset with 210 points total
- **GLOBlit_2584** (10.1016/j.jct.2005.07.012) — 128 points, multi-temperature
- **GLOBlit_3614** (10.1016/j.jct.2012.04.007) — 55 points, narrow water-dilute composition range
- **GLOBlit_1540** (10.1016/j.fluid.2014.08.026) — 4 points, partial composition range
- **GLOBlit_4166** (10.1016/j.jct.2014.05.003) — 3 points, partial composition range
- Plus additional blocks (11 total found)

### Recommendation

**GLOBlit_2834 / PROPblock_18** is the best single block for full-range binary density of DMF + water at 298.15 K: 40 points spanning x(DMF) = 0–1, all at exactly 298.15 K and 101.0 kPa. The non-monotonic density behavior (density maximum near x(DMF) ≈ 0.12) reflects strong DMF–water hydrogen-bonding interactions that produce volume contraction in the water-rich region.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** PROPblock_19: 210 (near '…vant 298.15 K data:  - ** ** ( ) — the largest dataset with …') matches no inspected row/stat, database table, or other source of PROPblock_19
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_19", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 210.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_19: 128 (near '…) — the largest dataset with 210 points total - ** ** ( ) — …') matches no inspected row/stat, database table, or other source of PROPblock_19
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_19", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 128.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_19: 55 (near '…l - ** ** ( ) — 128 points, multi-temperature - ** ** ( ) — …') matches no inspected row/stat, database table, or other source of PROPblock_19
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_19", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 55.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
Inspected so far: PROPblock_18, PROPblock_19

Verified as grounded — correct as quoted, keep unchanged:
- PROPblock_18: 40, 298.15, 101.0, 943.94, 997.02, 0.01233, 996.44, 0.0266, 996.21, 0.04154, 996.18, 0.11728, 0.14116, 996.93, 0.23003, 993.87, 0.28661, 990.18, 0.31385, 989.17, 0.37711, 984.28, 0.92495, 948.01, 0.96614, 946.28, 0.12, 997
Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_19: 18, 288.15, 298.15, 308.15, 100.0, 997, 0.4, 996.99, 0.6, 992.97, 0.8, 977.38, 943.89

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## LLM Response
<reasoning>
The grounding gate is flagging the numbers 210, 128, and 55 as being associated with PROPblock_19, but they're actually point counts for OTHER blocks (GLOBlit_11030, GLOBlit_2584, GLOBlit_3614) from the search_blocks summary result. These are not data values from PROPblock_19 — they are point counts reported by the search_blocks tool for different blocks. The gate seems to be misattributing them.

These values (210, 128, 55) came from the search_blocks tool result summary, not from any specific block inspection. They are metadata counts from the search tool. I should label them as "per the search_blocks summary" to clarify their provenance, since they are not from inspect_block_table but from the search tool's summary output.

Let me just fix the answer by noting these are from the search summary, not from block inspections.
</reasoning>

<answer>
## Binary Density Data: DMF + Water at 298.15 K

**11 binary blocks** were found in ThermoML containing both N,N-dimethylformamide (DMF, GLOBcomp_18) and water (GLOBcomp_1) with mass density (GLOBprop_1) near 298.15 K.

### Best Full-Range Dataset: GLOBlit_2834 / PROPblock_18

**DOI:** 10.1016/j.jct.2007.05.015  
**40 data points**, all at T = 298.15 K and p = 101.0 kPa, spanning x(DMF) = 0 to 1.  
**Density range (n=40):** 943.94–997.02 kg/m³

Representative inspected rows:

| x(DMF) | ρ (kg/m³) |
|--------|-----------|
| 0 | 997.02 |
| 0.01233 | 996.44 |
| 0.0266 | 996.21 |
| 0.04154 | 996.18 |
| 0.11728 | 997.02 |
| 0.14116 | 996.93 |
| 0.23003 | 993.87 |
| 0.28661 | 990.18 |
| 0.31385 | 989.17 |
| 0.37711 | 984.28 |
| 0.92495 | 948.01 |
| 0.96614 | 946.28 |
| 1 | 943.94 |

The topology is **non-monotonic** (4 extrema), showing a density maximum near x(DMF) ≈ 0.12 where the mixture density equals or slightly exceeds that of pure water (~997 kg/m³), before decreasing toward pure DMF (943.94 kg/m³).

### Additional Full-Range Dataset: GLOBlit_4174 / PROPblock_19

**DOI:** 10.1016/j.jct.2014.05.013  
**18 total points** across three temperatures (288.15, 298.15, 308.15 K) at p = 100.0 kPa, using mass fraction w(DMF) = 0 to 1.

At 298.15 K specifically (inspected rows):

| w(DMF) | ρ (kg/m³) |
|--------|-----------|
| 0 | 997 |
| 0.4 | 996.99 |
| 0.6 | 992.97 |
| 0.8 | 977.38 |
| 1 | 943.89 |

This dataset has fewer composition points at 298.15 K but confirms the same trend.

### Other Blocks Found (not individually inspected)

The search_blocks tool summary also returned blocks from the following sources, which may contain relevant 298.15 K data. Point counts below are per the search_blocks summary and have not been individually verified by block inspection:

- **GLOBlit_11030** (10.1021/je700671t) — reported as the largest dataset (per search summary)
- **GLOBlit_2584** (10.1016/j.jct.2005.07.012) — multi-temperature block
- **GLOBlit_3614** (10.1016/j.jct.2012.04.007) — narrow water-dilute composition range
- **GLOBlit_1540** (10.1016/j.fluid.2014.08.026) — partial composition range
- **GLOBlit_4166** (10.1016/j.jct.2014.05.003) — partial composition range
- Plus additional blocks (11 total found)

### Recommendation

**GLOBlit_2834 / PROPblock_18** is the best single block for full-range binary density of DMF + water at 298.15 K: 40 points spanning x(DMF) = 0–1, all at exactly 298.15 K and 101.0 kPa. The non-monotonic density behavior (density maximum near x(DMF) ≈ 0.12) reflects strong DMF–water hydrogen-bonding interactions that produce volume contraction in the water-rich region.
</answer>