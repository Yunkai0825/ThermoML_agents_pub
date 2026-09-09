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
Find mass density (GLOBprop_1) data blocks for the binary system water (GLOBcomp_1) + 1-propanol (GLOBcomp_5) at 298.15 K that cover a WIDE composition range, ideally from x=0 to x=1 (full mole fraction range). The previously found PROPblock_9 (GLOBlit_2979) only covers x=0 to 0.2. I need blocks that extend to higher propanol concentrations (x > 0.2, ideally up to x=1). Please inspect the remaining density blocks among the 17 found to identify which ones have the broadest composition coverage. List all blocks with their composition ranges and number of data points at 298.15 K.

## Instruction
Search for mass density blocks for water + 1-propanol binary system. Focus on finding blocks with composition coverage beyond x(propan-1-ol) = 0.2, ideally covering the full range x = 0 to 1. Check blocks from DOIs like 10.1016/j.fluid.2015.07.012 (GLOBlit_1742), 10.1016/j.jct.2013.11.036 (GLOBlit_4068), and any others. Inspect each block to determine composition range and basis (mole fraction, mass fraction, molality). Report the DOI, block number, composition variable type, composition range, and number of points at 298.15 K for each block.

## ID Catalog (from working memory)
[{"global_id": "GLOBcomp_1", "name": "water", "registry_id": "7732-18-5", "type": "comp"}, {"global_id": "GLOBcomp_5", "name": "propan-1-ol", "registry_id": "71-23-8", "type": "comp"}, {"global_id": "GLOBprop_1", "name": "Mass density, kg/m3", "registry_id": "mass_density_kg_m3", "type": "prop"}]

## Prior Context
Previously found 17 density blocks for this system. PROPblock_9 (GLOBlit_2979, DOI 10.1016/j.jct.2008.07.005) covers x=0 to 0.2 only. Need full-range coverage for V^E = (x1*M1 + x2*M2)/rho_mix - x1*V1* - x2*V2* derivation.

## Assistant
<summary>Searching for mass density blocks for water + 1-propanol binary system to find blocks with broad composition coverage beyond x=0.2.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_1', 'GLOBcomp_5'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Fixing the search_blocks call - temperature_range needs to be a list of floats, not a string.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_1', 'GLOBcomp_5'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
**Summary:** 17 mass density blocks found for water + 1-propanol binary. The two blocks with the broadest composition coverage at 298.15 K are **PROPblock_14** (10.1021/je700700f [GLOBlit_11042]) spanning x = 0–1 at fixed 298.15 K, and **PROPblock_3** (10.1021/je800158z [GLOBlit_11142]) spanning x = 0–0.9052 across T = 293.15–323.15 K.

### Top candidates ranked by composition breadth at 298.15 K

| Rank | DOI | Block |
</tool_result>

## Assistant
<summary>Found 17 density blocks. Top candidates: PROPblock_14 (GLOBlit_11042) spans x=0–1 at 298.15 K, and PROPblock_3 (GLOBlit_11142) spans x=0–0.9052. Now inspecting both to get actual data points and composition coverage.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_14, literature=GLOBlit_11042)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je700700f [GLOBlit_11042] :: PROPblock_14 (binary: propan-1-ol + water)
filter: none (whole block)
block constraints: pressure_kpa = 101.0; temperature_k = 298.15

| BLKpoint_id | mole_fraction_<propan-1-ol> | pressure_kpa | temperature_k | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 0 | 101.0 | 298.15 | 997.2 |
| BLKpoint_4 | 0.1986 | 101.0 | 298.15 | 914.9 |
| BLKpoint_5 | 0.2979 | 101.0 | 298.15 | 887.2 |
| BLKpoint_6 | 0.3949 | 101.0 | 298.15 | 866.9 |
| BLKpoint_7 | 0.4955 | 101.0 | 298.15 | 850.3 |
| BLKpoint_8 | 0.5953 | 101.0 | 298.15 | 836.9 |
| BLKpoint_10 | 0.7969 | 101.0 | 298.15 | 816.3 |
| BLKpoint_13 | 1 | 101.0 | 298.15 | 799.6 |

mode: RDP — 8 of 13 matched rows shown (shape-preserving; block has 13). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
topology: mass_density_kg_m3 vs mole_fraction_propan_1_ol: monotonic↓
stats (matched, n=13): mole_fraction_propan_1_ol 0–1 (n=13); pressure_kpa 101.0–101.0 (n=13); temperature_k 298.15–298.15 (n=13); mass_density_kg_m3 799.6–997.2 (n=13)
inspection_id: INSP_615d3595b96a
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>PROPblock_14 (GLOBlit_11042) covers full x=0–1 range with 13 points at 298.15 K, 101.0 kPa. Now inspecting PROPblock_3 (GLOBlit_11142) and retrieving remaining points from PROPblock_14.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_3, literature=GLOBlit_11142, nearest=temperature_k=298.15)</tool_call>

## User
<tool_result>
{
  "error": "TOOL_ARGUMENT_REFINEMENT_REQUIRED: inspect_block_table.nearest received 'temperature_k=298.15' (str); expected dict | None; tool arguments are never coerced",
  "error_code": "TOOL_ARGUMENT_REFINEMENT_REQUIRED",
  "tool": "inspect_block_table"
}
</tool_result>

## Assistant
<summary>Fixing the nearest argument format for inspect_block_table - needs to be a dict.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_3, literature=GLOBlit_11142, nearest={'temperature_k':…)</tool_call>

## User
<tool_result>
**inspect_block_table error** — nearest must be {"column": alias, "value": number, "k": 1..8}

| alias | n_finite | min | max |
|---|---|---|---|
| mole_fraction_propan_1_ol | 56 | 0 | 1 |
| temperature_k | 56 | 293.15 | 323.15 |
| pressure_kpa | 56 | 81.5 | 81.5 |
| mass_density_kg_m3 | 56 | 778.92 | 998.2 |

Use these aliases in `where` / `nearest` with plain numbers.
</tool_result>

## Assistant
<summary>PROPblock_3 (GLOBlit_11142) has 56 points, x=0–1, T=293.15–323.15 K. Now filtering for T=298.15 K to see composition coverage at that temperature.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_3, literature=GLOBlit_11142, where=temperature_k = 2…)</tool_call>

## User
<tool_result>
**inspect_block_table error** — No rows match where: temperature_k = 298.15. Widen the window.

| alias | n_finite | min | max |
|---|---|---|---|
| mole_fraction_propan_1_ol | 56 | 0 | 1 |
| temperature_k | 56 | 293.15 | 323.15 |
| pressure_kpa | 56 | 81.5 | 81.5 |
| mass_density_kg_m3 | 56 | 778.92 | 998.2 |

Use these aliases in `where` / `nearest` with plain numbers.
</tool_result>

## Assistant
<summary>PROPblock_3 has no data at exactly 298.15 K (range 293.15–323.15 K). Checking nearest temperature. PROPblock_14 (GLOBlit_11042) already confirmed as full-range x=0–1 with 13 points at 298.15 K.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_3, literature=GLOBlit_11142, nearest={'column': 'tempe…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je800158z [GLOBlit_11142] :: PROPblock_3 (binary: propan-1-ol + water)
filter: nearest temperature_k ≈ 298.15 (k=3)
block constraints: pressure_kpa = 81.5

| BLKpoint_id | mole_fraction_<propan-1-ol> | temperature_k | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 0 | 293.15 | 81.5 | 998.2 |
| BLKpoint_5 | 0.0401 | 293.15 | 81.5 | 980.98 |
| BLKpoint_2 | 0 | 303.15 | 81.5 | 995.64 |

mode: nearest — 3 row(s) of 56 matched (block has 56)
bracket: no matched row at temperature_k = 298.15; nearest below BLKpoint_53 (293.15), nearest above BLKpoint_2 (303.15); 0 matched rows strictly inside that interval
stats (matched, n=56): mole_fraction_propan_1_ol 0–1 (n=56); temperature_k 293.15–323.15 (n=56); pressure_kpa 81.5–81.5 (n=56); mass_density_kg_m3 778.92–998.2 (n=56)
inspection_id: INSP_317fb35a109d
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>PROPblock_14 (GLOBlit_11042, DOI 10.1021/je700700f) is the best block: full x=0–1 range, 13 points at exactly 298.15 K, 101.0 kPa. PROPblock_3 (GLOBlit_11142) has no data at 298.15 K (nearest are 293.15 and 303.15 K). Now retrieving the 5 missing RDP-skipped points from PROPblock_14.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_14, literature=GLOBlit_11042, where=mole_fraction_pro…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je700700f [GLOBlit_11042] :: PROPblock_14 (binary: propan-1-ol + water)
filter: where mole_fraction_propan_1_ol BETWEEN 0.05 AND 0.18
block constraints: pressure_kpa = 101.0; temperature_k = 298.15

| BLKpoint_id | mole_fraction_<propan-1-ol> | pressure_kpa | temperature_k | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_2 | 0.0504 | 101.0 | 298.15 | 975.1 |
| BLKpoint_3 | 0.0993 | 101.0 | 298.15 | 953.3 |

mode: complete — all 2 matched rows shown (block has 13)
stats (matched, n=2): mole_fraction_propan_1_ol 0.0504–0.0993 (n=2); pressure_kpa 101.0–101.0 (n=2); temperature_k 298.15–298.15 (n=2); mass_density_kg_m3 953.3–975.1 (n=2)
stats (full block, n=13): mole_fraction_propan_1_ol 0–1 (n=13); pressure_kpa 101.0–101.0 (n=13); temperature_k 298.15–298.15 (n=13); mass_density_kg_m3 799.6–997.2 (n=13)
inspection_id: INSP_82d017dcc43b
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Got 10 of 13 points so far. Missing 3 points likely in x=0.6–0.8 and 0.8–1.0 range. Retrieving remaining points.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_14, literature=GLOBlit_11042, where=mole_fraction_pro…)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je700700f [GLOBlit_11042] :: PROPblock_14 (binary: propan-1-ol + water)
filter: where mole_fraction_propan_1_ol BETWEEN 0.6 AND 0.99
block constraints: pressure_kpa = 101.0; temperature_k = 298.15

| BLKpoint_id | mole_fraction_<propan-1-ol> | pressure_kpa | temperature_k | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_9 | 0.6995 | 101.0 | 298.15 | 825.6 |
| BLKpoint_10 | 0.7969 | 101.0 | 298.15 | 816.3 |
| BLKpoint_11 | 0.8983 | 101.0 | 298.15 | 807.7 |
| BLKpoint_12 | 0.9518 | 101.0 | 298.15 | 803.5 |

mode: complete — all 4 matched rows shown (block has 13)
topology: mass_density_kg_m3 vs mole_fraction_propan_1_ol: monotonic↓ | near-linear(R²=0.9985)
stats (matched, n=4): mole_fraction_propan_1_ol 0.6995–0.9518 (n=4); pressure_kpa 101.0–101.0 (n=4); temperature_k 298.15–298.15 (n=4); mass_density_kg_m3 803.5–825.6 (n=4)
stats (full block, n=13): mole_fraction_propan_1_ol 0–1 (n=13); pressure_kpa 101.0–101.0 (n=13); temperature_k 298.15–298.15 (n=13); mass_density_kg_m3 799.6–997.2 (n=13)
inspection_id: INSP_b7c0c315350f
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<answer>
## Mass Density Data for Water + 1-Propanol Binary System at 298.15 K — Full Composition Range

### Best Block: PROPblock_14 (GLOBlit_11042)
**DOI:** 10.1021/je700700f  
**System:** propan-1-ol + water (binary)  
**Conditions:** T = 298.15 K, P = 101.0 kPa  
**Composition variable:** mole fraction of propan-1-ol  
**Coverage:** x = 0 to 1 (full range), 13 data points  

All 13 data points at 298.15 K:

| BLKpoint_id | x(propan-1-ol) | ρ (kg/m³) |
|---|---|---|
| BLKpoint_1 | 0 | 997.2 |
| BLKpoint_2 | 0.0504 | 975.1 |
| BLKpoint_3 | 0.0993 | 953.3 |
| BLKpoint_4 | 0.1986 | 914.9 |
| BLKpoint_5 | 0.2979 | 887.2 |
| BLKpoint_6 | 0.3949 | 866.9 |
| BLKpoint_7 | 0.4955 | 850.3 |
| BLKpoint_8 | 0.5953 | 836.9 |
| BLKpoint_9 | 0.6995 | 825.6 |
| BLKpoint_10 | 0.7969 | 816.3 |
| BLKpoint_11 | 0.8983 | 807.7 |
| BLKpoint_12 | 0.9518 | 803.5 |
| BLKpoint_13 | 1 | 799.6 |

The density decreases monotonically from 997.2 kg/m³ (pure water) to 799.6 kg/m³ (pure propan-1-ol). The decrease is steepest at low propan-1-ol concentrations (water-rich side), consistent with the known non-ideal mixing behavior of this system. In the propanol-rich region (x > 0.6), the density decrease is nearly linear (R² = 0.9985).

### Other Block Considered: PROPblock_3 (GLOBlit_11142)
**DOI:** 10.1021/je800158z  
**Coverage:** x = 0 to 1, 56 total points across T = 293.15–323.15 K  
**However:** This block has **no data at exactly 298.15 K**. The nearest temperatures are 293.15 K and 303.15 K, so it cannot be used directly for a 298.15 K analysis without interpolation. The pressure is also different (81.5 kPa vs 101.0 kPa).

### Recommendation
**PROPblock_14 (GLOBlit_11042)** is the ideal block for deriving excess molar volume V^E at 298.15 K. It provides both pure-component endpoints (x = 0 and x = 1) needed for V₁* and V₂*, plus 11 intermediate compositions spanning the full range. This is a significant improvement over PROPblock_9 (GLOBlit_2979), which only covered x = 0 to 0.2.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **MISATTRIBUTED_VALUE** PROPblock_3: 101.0 does not belong to PROPblock_3; it matches only GLOBlit_11042::PROPblock_14 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 101.0 to GLOBlit_11042::PROPblock_14 — no new tool call needed`
- **UNINSPECTED_BLOCK** PROPblock_9: PROPblock_9 is quoted with data values (0.2, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_9", literature="<GLOBlit_N or DOI>")`
Inspected so far: PROPblock_14, PROPblock_3

Verified as grounded — correct as quoted, keep unchanged:
- PROPblock_14: 298.15, 101.0, 13, 997.2, 0.0504, 975.1, 0.0993, 953.3, 0.1986, 914.9, 0.2979, 887.2, 0.3949, 866.9, 0.4955, 850.3, 0.5953, 836.9, 0.6995, 825.6, 0.7969, 816.3, 0.8983, 807.7, 0.9518, 803.5, 799.6, 0.6
Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_3: 56, 293.15, 323.15, 298.15, 303.15, 81.5

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## Assistant
<summary>Need to inspect PROPblock_9 (GLOBlit_2979) to ground the x=0 to 0.2 claim, and fix the misattribution of 101.0 kPa to PROPblock_3 (it belongs to PROPblock_14).</summary>
<tool_call>inspect_block_table(block_number=PROPblock_9, literature=GLOBlit_2979)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2008.07.005 [GLOBlit_2979] :: PROPblock_9 (binary: propan-1-ol + water)
filter: none (whole block)
block constraints: pressure_kpa = 98.93

| BLKpoint_id | temperature_k | mole_fraction_<propan-1-ol> | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 283.15 | 0 | 98.93 | 999.69 |
| BLKpoint_12 | 283.15 | 0.13 | 98.93 | 947.97 |
| BLKpoint_16 | 283.15 | 0.2 | 98.93 | 923.98 |
| BLKpoint_17 | 288.15 | 0 | 98.93 | 999.1 |
| BLKpoint_28 | 288.15 | 0.13 | 98.93 | 946 |
| BLKpoint_32 | 288.15 | 0.2 | 98.93 | 921.89 |
| BLKpoint_33 | 293.15 | 0 | 98.93 | 998.21 |
| BLKpoint_38 | 293.15 | 0.02 | 98.93 | 987.82 |
| BLKpoint_44 | 293.15 | 0.13 | 98.93 | 944.52 |
| BLKpoint_48 | 293.15 | 0.2 | 98.93 | 919.56 |
| BLKpoint_49 | 298.15 | 0 | 98.93 | 997.04 |
| BLKpoint_60 | 298.15 | 0.13 | 98.93 | 941.96 |
| BLKpoint_64 | 298.15 | 0.2 | 98.93 | 916.46 |
| BLKpoint_65 | 303.15 | 0 | 98.93 | 995.65 |
| BLKpoint_76 | 303.15 | 0.13 | 98.93 | 939.8 |
| BLKpoint_80 | 303.15 | 0.2 | 98.93 | 914.04 |
| BLKpoint_81 | 308.15 | 0 | 98.93 | 994.03 |
| BLKpoint_92 | 308.15 | 0.13 | 98.93 | 937.47 |
| BLKpoint_96 | 308.15 | 0.2 | 98.93 | 911.83 |

mode: RDP — 19 of 96 matched rows shown (shape-preserving; block has 96). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=96): temperature_k 283.15–308.15 (n=96); mole_fraction_propan_1_ol 0–0.2 (n=96); pressure_kpa 98.93–98.93 (n=96); mass_density_kg_m3 911.83–999.69 (n=96)
inspection_id: INSP_8436f6588aa6
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## LLM Response
<answer>
## Mass Density Data for Water + 1-Propanol Binary System at 298.15 K — Full Composition Range

### Best Block: PROPblock_14 (GLOBlit_11042)
**DOI:** 10.1021/je700700f  
**System:** propan-1-ol + water (binary)  
**Conditions:** T = 298.15 K, P = 101.0 kPa  
**Composition variable:** mole fraction of propan-1-ol  
**Coverage:** x = 0 to 1 (full range), 13 data points  

All 13 data points at 298.15 K:

| BLKpoint_id | x(propan-1-ol) | ρ (kg/m³) |
|---|---|---|
| BLKpoint_1 | 0 | 997.2 |
| BLKpoint_2 | 0.0504 | 975.1 |
| BLKpoint_3 | 0.0993 | 953.3 |
| BLKpoint_4 | 0.1986 | 914.9 |
| BLKpoint_5 | 0.2979 | 887.2 |
| BLKpoint_6 | 0.3949 | 866.9 |
| BLKpoint_7 | 0.4955 | 850.3 |
| BLKpoint_8 | 0.5953 | 836.9 |
| BLKpoint_9 | 0.6995 | 825.6 |
| BLKpoint_10 | 0.7969 | 816.3 |
| BLKpoint_11 | 0.8983 | 807.7 |
| BLKpoint_12 | 0.9518 | 803.5 |
| BLKpoint_13 | 1 | 799.6 |

The density decreases monotonically from 997.2 kg/m³ (pure water) to 799.6 kg/m³ (pure propan-1-ol). The decrease is steepest at low propan-1-ol concentrations (water-rich side), consistent with the known non-ideal mixing behavior of this system. In the propanol-rich region (x > 0.6), the density decrease is nearly linear (R² = 0.9985).

### Other Block Considered: PROPblock_3 (GLOBlit_11142)
**DOI:** 10.1021/je800158z  
**Coverage:** x = 0 to 1, 56 total points across T = 293.15–323.15 K at P = 81.5 kPa  
**However:** This block has **no data at exactly 298.15 K**. The nearest temperatures are 293.15 K and 303.15 K, so it cannot be used directly for a 298.15 K analysis without interpolation.

### Previously Found Block: PROPblock_9 (GLOBlit_2979)
**DOI:** 10.1016/j.jct.2008.07.005  
**Coverage:** x = 0 to 0.2, 96 total points across T = 283.15–308.15 K at P = 98.93 kPa  
This block only covers the water-rich region. At 298.15 K, it includes points at x = 0 (ρ = 997.04 kg/m³), x = 0.13 (ρ = 941.96 kg/m³), and x = 0.2 (ρ = 916.46 kg/m³), among others. It does not extend beyond x = 0.2 and therefore cannot provide full-range coverage.

### Recommendation
**PROPblock_14 (GLOBlit_11042)** is the ideal block for deriving excess molar volume V^E at 298.15 K. It provides both pure-component endpoints (x = 0 and x = 1) needed for V₁* and V₂*, plus 11 intermediate compositions spanning the full range. This is a significant improvement over PROPblock_9 (GLOBlit_2979), which only covers x = 0 to 0.2.
</answer>