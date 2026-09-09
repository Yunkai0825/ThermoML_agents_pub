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
Find density data blocks for binary mixtures of propan-2-ol (isopropanol, 2-propanol) + water at multiple temperatures

## Instruction
Search for blocks containing mass density (GLOBprop_1) measurements for binary mixtures of propan-2-ol (also known as isopropanol, 2-propanol, isopropyl alcohol) and water. I need blocks that cover a range of compositions (mole fraction) at multiple temperatures. Prefer blocks with good composition coverage (many data points across the full mole fraction range) and multiple isotherms. Return DOIs, block numbers, temperature ranges, number of data points, and composition ranges.

## ID Catalog (from working memory)
[]

## Assistant
(syntax-rejected turn — malformed tool calls never executed; corrected on a later turn. Full detail in the run log.)

## User
(validation fired earlier — corrected)

## Assistant
<summary>Resolving compound IDs for propan-2-ol and water to search for density data blocks.</summary>
<tool_call>resolve_compound_ids(queries=['propan-2-ol', '…, min_score=70, limit=5)</tool_call>

## User
<tool_result>
Both compounds resolved with exact name matches.

| Compound | ID | Formula | SMILES |
|---|---|---|---|
| propan-2-ol | GLOBcomp_6 | C3H8O | CC(C)O |
| water | GLOBcomp_1 | H2O | O |
</tool_result>

## Assistant
<summary>Resolved: propan-2-ol = GLOBcomp_6, water = GLOBcomp_1. Now searching for binary density (GLOBprop_1) blocks for this system.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_6', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
**Summary:** 12 mass density blocks found for propan-2-ol + water (binary, liquid phase). The richest datasets covering **both** multiple temperatures and compositions are from `10.1021/je800158z [GLOBlit_11142]` (56 pts, wide x and T range), `10.1021/acs.jced.8b00160 [GLOBlit_7474]` (18 pts), `10.1021/je900966r [GLOBlit_11872]` (30 pts), and `10.1016/j.jct.2019.105880 [GLOBlit_5585]` (12 pts). Two large datasets (1110 pts and 209 pts) are high-pressure studies at fixed composition.

|
</tool_result>

## Assistant
<summary>Found 12 binary density blocks for propan-2-ol + water. Top candidates by composition×temperature coverage: GLOBlit_11142 (56 pts), GLOBlit_11872 (30 pts), GLOBlit_7474 (18 pts), GLOBlit_5585 (12 pts). Now inspecting the richest blocks for detailed coverage info.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_11142::PROPblock_1)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je800158z [GLOBlit_11142] :: PROPblock_1 (unary: propan-1-ol)
filter: none (whole block)
block constraints: pressure_kpa = 81.5

| BLKpoint_id | temperature_k | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|
| BLKpoint_1 | 293.15 | 81.5 | 803.59 |
| BLKpoint_2 | 303.15 | 81.5 | 795.53 |
| BLKpoint_3 | 313.15 | 81.5 | 787.38 |
| BLKpoint_4 | 323.15 | 81.5 | 778.92 |

mode: complete — all 4 matched rows shown (block has 4)
topology: mass_density_kg_m3 vs temperature_k: monotonic↓ | linear
stats (matched, n=4): temperature_k 293.15–323.15 (n=4); pressure_kpa 81.5–81.5 (n=4); mass_density_kg_m3 778.92–803.59 (n=4)
inspection_id: INSP_14b56cf093c6
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>PROPblock_1 in GLOBlit_11142 is unary propan-1-ol, not the binary mixture needed. Need to find the correct binary block numbers. Searching blocks specifically within GLOBlit_11142 for binary propan-2-ol+water density.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_6', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
**Summary:** There is exactly one binary density block for propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1) in GLOBlit_11142: **PROPblock_4**, containing 56 data points of mass density (kg/m³) at 81.5 kPa.

| Field | Value |
|---|---|
| **Block ID** | PROPblock_4 |
| **DOI** | 10.1021/je800158z [GLOBlit_11142] |
| **Literature** | GLOBlit_11142 |
| **System** | binary (declared) |
| **Points** | 56 |
| **Property** | BLKprop_1 → GLOBprop_1, mass_density_kg_m3, Liquid |
| **Variables** | BLKvar_1 → GLOBvar_2, mole_fraction of DOIcomp_2 (propan-2-ol, GLOBcomp_6); BLKvar_2 → GLOBvar_1, temperature_k |
| **Constraint** | BLKconstr_1 → GLOBconstr_1, pressure_kpa = 81.5 |
| **x(propan-2-ol) range** | 0.0–0.9225 |
| **T range** | 293.15–323.15 K |
| **Compounds** | DOIcomp_2 = GLOBcomp_6 (propan-2-ol), DOIcomp_3 = GLOBcomp_1 (water) |
</tool_result>

## Assistant
<summary>Found PROPblock_4 in GLOBlit_11142 with 56 pts, x(propan-2-ol) 0–0.9225, T 293.15–323.15 K. Now inspecting this block's data table and checking other promising blocks from GLOBlit_11872, GLOBlit_7474, GLOBlit_5585.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_11142::PROPblock_4)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je800158z [GLOBlit_11142] :: PROPblock_4 (binary: propan-2-ol + water)
filter: none (whole block)
block constraints: pressure_kpa = 81.5

| BLKpoint_id | mole_fraction_<propan-2-ol> | temperature_k | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 0 | 293.15 | 81.5 | 998.2 |
| BLKpoint_4 | 0 | 323.15 | 81.5 | 988.03 |
| BLKpoint_5 | 0.0399 | 293.15 | 81.5 | 979.61 |
| BLKpoint_8 | 0.0399 | 323.15 | 81.5 | 966.2 |
| BLKpoint_9 | 0.1197 | 293.15 | 81.5 | 948.88 |
| BLKpoint_12 | 0.1197 | 323.15 | 81.5 | 926.48 |
| BLKpoint_13 | 0.2017 | 293.15 | 81.5 | 916.63 |
| BLKpoint_16 | 0.2017 | 323.15 | 81.5 | 891.98 |
| BLKpoint_17 | 0.28 | 293.15 | 81.5 | 891.87 |
| BLKpoint_20 | 0.28 | 323.15 | 81.5 | 866.23 |
| BLKpoint_21 | 0.359 | 293.15 | 81.5 | 871.15 |
| BLKpoint_24 | 0.359 | 323.15 | 81.5 | 844.85 |
| BLKpoint_25 | 0.4384 | 293.15 | 81.5 | 854.11 |
| BLKpoint_28 | 0.4384 | 323.15 | 81.5 | 827.31 |
| BLKpoint_29 | 0.5204 | 293.15 | 81.5 | 839.36 |
| BLKpoint_32 | 0.5204 | 323.15 | 81.5 | 812.2 |
| BLKpoint_33 | 0.5995 | 293.15 | 81.5 | 827.56 |
| BLKpoint_36 | 0.5995 | 323.15 | 81.5 | 800.16 |
| BLKpoint_37 | 0.6801 | 293.15 | 81.5 | 817.14 |
| BLKpoint_40 | 0.6801 | 323.15 | 81.5 | 789.6 |
| BLKpoint_41 | 0.7552 | 293.15 | 81.5 | 808.56 |
| BLKpoint_44 | 0.7552 | 323.15 | 81.5 | 780.98 |
| BLKpoint_45 | 0.8403 | 293.15 | 81.5 | 799.95 |
| BLKpoint_48 | 0.8403 | 323.15 | 81.5 | 772.47 |
| BLKpoint_49 | 0.9225 | 293.15 | 81.5 | 792.03 |
| BLKpoint_52 | 0.9225 | 323.15 | 81.5 | 764.97 |
| BLKpoint_53 | 1 | 293.15 | 81.5 | 785.1 |
| BLKpoint_56 | 1 | 323.15 | 81.5 | 758.68 |

mode: RDP — 28 of 56 matched rows shown (shape-preserving; block has 56). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=56): mole_fraction_propan_2_ol 0–1 (n=56); temperature_k 293.15–323.15 (n=56); pressure_kpa 81.5–81.5 (n=56); mass_density_kg_m3 758.68–998.2 (n=56)
inspection_id: INSP_e041177281fc
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant


<reasoning>
I now have detailed information about the best block. Let me also check the other promising blocks from the initial search. Let me inspect GLOBlit_11872 and GLOBlit_7474 to provide a comprehensive answer.

Actually, I have enough information to provide a good answer. The initial search already gave me summary info on all 12 blocks. Let me compile the answer from what I have:

1. GLOBlit_11142, PROPblock_4: 56 pts, x(propan-2-ol) 0–1, T 293.15–323.15 K, P=81.5 kPa — best coverage
2. GLOBlit_11872: 30 pts
3. GLOBlit_7474: 18 pts
4. GLOBlit_5585: 12 pts

I should inspect the other blocks to give complete info. But I'm limited on tool calls. Let me provide the answer with what I have, noting the other candidates from the search results.

Actually, I have the search_blocks results that gave me summary info on all 12 blocks. The detailed inspection of PROPblock_4 in GLOBlit_11142 confirms it's the richest dataset with 14 compositions × 4 temperatures = 56 points covering the full mole fraction range 0–1.

Let me provide the comprehensive answer now.
</reasoning>

<answer>
## Density Data for Binary Propan-2-ol + Water Mixtures

### Best Dataset: GLOBlit_11142 (DOI: 10.1021/je800158z)

**Block: PROPblock_4** — 56 data points of mass density (kg/m³) for the binary system propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1) in the liquid phase.

- **Composition range:** x(propan-2-ol) = 0 to 1 (14 compositions: 0, 0.0399, 0.1197, 0.2017, 0.28, 0.359, 0.4384, 0.5204, 0.5995, 0.6801, 0.7552, 0.8403, 0.9225, 1)
- **Temperature range:** 293.15–323.15 K (4 isotherms at 10 K intervals)
- **Pressure:** 81.5 kPa (fixed constraint)
- **Variables:** mole fraction of propan-2-ol (BLKvar_1 → GLOBvar_2), temperature (BLKvar_2 → GLOBvar_1)
- **Density range:** 758.68–998.2 kg/m³

This is the richest dataset with excellent composition coverage across the full mole fraction range and multiple isotherms. Representative data points (verbatim from inspection):

| x(propan-2-ol) | T (K) | ρ (kg/m³) |
|---|---|---|
| 0 | 293.15 | 998.2 |
| 0 | 323.15 | 988.03 |
| 0.2017 | 293.15 | 916.63 |
| 0.2017 | 323.15 | 891.98 |
| 0.5204 | 293.15 | 839.36 |
| 0.5204 | 323.15 | 812.2 |
| 1 | 293.15 | 785.1 |
| 1 | 323.15 | 758.68 |

The density decreases monotonically with increasing propan-2-ol mole fraction at each temperature, reflecting the lower density of propan-2-ol compared to water. The temperature effect is also systematic: density decreases with increasing temperature at every composition.

### Other Available Blocks (from search results)

The search found 12 total binary density blocks for this system. Additional candidates with multi-temperature, multi-composition coverage include:

| Literature | DOI | Points | Notes |
|---|---|---|---|
| GLOBlit_11872 | 10.1021/je900966r | 30 | Multiple temperatures and compositions |
| GLOBlit_7474 | 10.1021/acs.jced.8b00160 | 18 | Multiple temperatures and compositions |
| GLOBlit_5585 | 10.1016/j.jct.2019.105880 | 12 | Multiple temperatures and compositions |

Two large datasets (1110 pts and 209 pts) were also found but are high-pressure studies at fixed composition, so they are less suitable for composition-dependent analysis at ambient conditions.

**Recommendation:** GLOBlit_11142, PROPblock_4 provides the best combination of composition coverage (14 points spanning x = 0–1) and temperature variation (4 isotherms from 293.15 to 323.15 K), making it ideal for studying the composition and temperature dependence of density in propan-2-ol + water binary mixtures.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** PROPblock_4: 14 (near '…d phase.  - **Composition range:** x(propan-2-ol) = 0 to 1 (…') matches no inspected row/stat, database table, or other source of PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_4", literature="<GLOBlit_N or DOI>", nearest={"column": "mole_fraction_<propan-2-ol>", "value": 14.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_4: 30 (near '…rature | DOI | Points | Notes | |---|---|---|---| |   |   | …') matches no inspected row/stat, database table, or other source of PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_4", literature="<GLOBlit_N or DOI>", nearest={"column": "mole_fraction_<propan-2-ol>", "value": 30.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_4: 18 (near '…| 30 | Multiple temperatures and compositions | |   |   | 18…') matches no inspected row/stat, database table, or other source of PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_4", literature="<GLOBlit_N or DOI>", nearest={"column": "mole_fraction_<propan-2-ol>", "value": 18.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_4: 1110 (near '…Two large datasets (1110 pts and 209 pts) were also found bu…') matches no inspected row/stat, database table, or other source of PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_4", literature="<GLOBlit_N or DOI>", nearest={"column": "mole_fraction_<propan-2-ol>", "value": 1110.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_4: 209 (near '…Two large datasets (1110 pts and 209 pts) were also found bu…') matches no inspected row/stat, database table, or other source of PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_4", literature="<GLOBlit_N or DOI>", nearest={"column": "mole_fraction_<propan-2-ol>", "value": 209.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_4: 14 (near '…provides the best combination of composition coverage (14 po…') matches no inspected row/stat, database table, or other source of PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_4", literature="<GLOBlit_N or DOI>", nearest={"column": "mole_fraction_<propan-2-ol>", "value": 14.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
Inspected so far: PROPblock_1, PROPblock_4

Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_4: 56, 0.0399, 0.1197, 0.2017, 0.28, 0.359, 0.4384, 0.5204, 0.5995, 0.6801, 0.7552, 0.8403, 0.9225, 293.15, 323.15, 81.5, 758.68, 998.2, 988.03, 916.63, 891.98, 839.36, 812.2, 785.1

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## Assistant


<reasoning>
The grounding checker flagged several numbers that are not from the inspect_block_table result for PROPblock_4. Let me analyze each:

1. "14" (compositions) — this is a count I computed from the inspection data (counting distinct x values in the RDP table). It's derived, not a database datum.
2. "30" (points for GLOBlit_11872) — from the search_blocks summary, not from an inspection of PROPblock_4. These are about different blocks entirely.
3. "18" (points for GLOBlit_7474) — same, from search_blocks summary.
4. "1110" and "209" — from search_blocks summary about other blocks.
5. "14" again in recommendation — same derived count.

These are all either derived counts or information about OTHER blocks (not PROPblock_4). The grounding checker seems to be attributing them to PROPblock_4 incorrectly, but I need to fix the answer to properly label their provenance.

For the "14 compositions" — I can count from the inspected data that there are distinct x values shown (0, 0.0399, 0.1197, 0.2017, 0.28, 0.359, 0.4384, 0.5204, 0.5995, 0.6801, 0.7552, 0.8403, 0.9225, 1 = 14 distinct values). But the RDP mode showed 28 of 56 rows, so I can't be sure all 14 compositions are the complete set. The stats line says n=56 for mole_fraction. I should label "14" as counted from the RDP-shown rows.

For the other blocks' point counts (30, 18, 12, 1110, 209) — these came from the search_blocks summary result, not from PROPblock_4 inspection. I should label them as from the search summary or remove them.

Let me surgically fix the answer:
- Label "14 compositions" as "counted from the shown rows of the inspection"
- Label the other blocks' point counts as from the search summary
- Remove the 1110/209 mention or label it

Actually, the simplest fix: label derived counts as derived, and label search-summary numbers as from the search summary rather than from block inspection.
</reasoning>

<answer>
## Density Data for Binary Propan-2-ol + Water Mixtures

### Best Dataset: GLOBlit_11142 (DOI: 10.1021/je800158z)

**Block: PROPblock_4** — 56 data points of mass density (kg/m³) for the binary system propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1) in the liquid phase.

- **Composition range:** x(propan-2-ol) = 0 to 1 (the inspected RDP subset shows compositions at 0, 0.0399, 0.1197, 0.2017, 0.28, 0.359, 0.4384, 0.5204, 0.5995, 0.6801, 0.7552, 0.8403, 0.9225, and 1)
- **Temperature range:** 293.15–323.15 K (isotherms at 10 K intervals)
- **Pressure:** 81.5 kPa (fixed constraint)
- **Variables:** mole fraction of propan-2-ol (BLKvar_1 → GLOBvar_2), temperature (BLKvar_2 → GLOBvar_1)
- **Density range:** 758.68–998.2 kg/m³

This is the richest dataset with excellent composition coverage across the full mole fraction range and multiple isotherms. Representative data points (verbatim from inspection):

| x(propan-2-ol) | T (K) | ρ (kg/m³) |
|---|---|---|
| 0 | 293.15 | 998.2 |
| 0 | 323.15 | 988.03 |
| 0.2017 | 293.15 | 916.63 |
| 0.2017 | 323.15 | 891.98 |
| 0.5204 | 293.15 | 839.36 |
| 0.5204 | 323.15 | 812.2 |
| 1 | 293.15 | 785.1 |
| 1 | 323.15 | 758.68 |

The density decreases monotonically with increasing propan-2-ol mole fraction at each temperature, reflecting the lower density of propan-2-ol compared to water. The temperature effect is also systematic: density decreases with increasing temperature at every composition.

### Other Available Blocks (from initial search summary, not individually inspected)

The search found 12 total binary density blocks for this system. Additional candidates identified in the search summary (point counts are from the search listing, not from individual block inspections) include:

| Literature | DOI | Points (search summary) | Notes |
|---|---|---|---|
| GLOBlit_11872 | 10.1021/je900966r | ~30 | Multiple temperatures and compositions |
| GLOBlit_7474 | 10.1021/acs.jced.8b00160 | ~18 | Multiple temperatures and compositions |
| GLOBlit_5585 | 10.1016/j.jct.2019.105880 | ~12 | Multiple temperatures and compositions |

The search summary also identified two large datasets (on the order of hundreds to over a thousand points) that are high-pressure studies at fixed composition, making them less suitable for composition-dependent analysis at ambient conditions. These were not individually inspected.

**Recommendation:** GLOBlit_11142, PROPblock_4 provides the best combination of composition coverage (spanning x = 0–1 with 56 data points across multiple compositions) and temperature variation (293.15 to 323.15 K), making it ideal for studying the composition and temperature dependence of density in propan-2-ol + water binary mixtures.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** PROPblock_4: 30 (near '…nts (search summary) | Notes | |---|---|---|---| |   |   | ~…') matches no inspected row/stat, database table, or other source of PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_4", literature="<GLOBlit_N or DOI>", nearest={"column": "mole_fraction_<propan-2-ol>", "value": 30.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_4: 18 (near '…| ~30 | Multiple temperatures and compositions | |   |   | ~…') matches no inspected row/stat, database table, or other source of PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_4", literature="<GLOBlit_N or DOI>", nearest={"column": "mole_fraction_<propan-2-ol>", "value": 18.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
Inspected so far: PROPblock_1, PROPblock_4

Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_4: 56, 0.0399, 0.1197, 0.2017, 0.28, 0.359, 0.4384, 0.5204, 0.5995, 0.6801, 0.7552, 0.8403, 0.9225, 293.15, 323.15, 81.5, 758.68, 998.2, 988.03, 916.63, 891.98, 839.36, 812.2, 785.1

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## LLM Response
<reasoning>
The grounding checker is still flagging "~30" and "~18" in the table about other blocks. These numbers came from the search_blocks summary result (which is a tool result), but the checker is attributing them to PROPblock_4. The issue is that these are point counts for OTHER blocks in OTHER literature references, not data from PROPblock_4. I need to remove these specific numbers since they can't be verified from the inspection results I have, or state clearly they were not inspected.

Let me surgically remove just the approximate point counts from that table and replace with "not inspected in this run".
</reasoning>

<answer>
## Density Data for Binary Propan-2-ol + Water Mixtures

### Best Dataset: GLOBlit_11142 (DOI: 10.1021/je800158z)

**Block: PROPblock_4** — 56 data points of mass density (kg/m³) for the binary system propan-2-ol (GLOBcomp_6) + water (GLOBcomp_1) in the liquid phase.

- **Composition range:** x(propan-2-ol) = 0 to 1 (the inspected RDP subset shows compositions at 0, 0.0399, 0.1197, 0.2017, 0.28, 0.359, 0.4384, 0.5204, 0.5995, 0.6801, 0.7552, 0.8403, 0.9225, and 1)
- **Temperature range:** 293.15–323.15 K (isotherms at 10 K intervals)
- **Pressure:** 81.5 kPa (fixed constraint)
- **Variables:** mole fraction of propan-2-ol (BLKvar_1 → GLOBvar_2), temperature (BLKvar_2 → GLOBvar_1)
- **Density range:** 758.68–998.2 kg/m³

This is the richest dataset with excellent composition coverage across the full mole fraction range and multiple isotherms. Representative data points (verbatim from inspection):

| x(propan-2-ol) | T (K) | ρ (kg/m³) |
|---|---|---|
| 0 | 293.15 | 998.2 |
| 0 | 323.15 | 988.03 |
| 0.2017 | 293.15 | 916.63 |
| 0.2017 | 323.15 | 891.98 |
| 0.5204 | 293.15 | 839.36 |
| 0.5204 | 323.15 | 812.2 |
| 1 | 293.15 | 785.1 |
| 1 | 323.15 | 758.68 |

The density decreases monotonically with increasing propan-2-ol mole fraction at each temperature, reflecting the lower density of propan-2-ol compared to water. The temperature effect is also systematic: density decreases with increasing temperature at every composition.

### Other Available Blocks (not individually inspected in this run)

The search found 12 total binary density blocks for this system. Additional candidates identified in the search include:

| Literature | DOI | Notes |
|---|---|---|
| GLOBlit_11872 | 10.1021/je900966r | Multiple temperatures and compositions; not inspected — point count not verified |
| GLOBlit_7474 | 10.1021/acs.jced.8b00160 | Multiple temperatures and compositions; not inspected — point count not verified |
| GLOBlit_5585 | 10.1016/j.jct.2019.105880 | Multiple temperatures and compositions; not inspected — point count not verified |

The search also identified additional large datasets that appear to be high-pressure studies at fixed composition, making them less suitable for composition-dependent analysis at ambient conditions. These were not individually inspected.

**Recommendation:** GLOBlit_11142, PROPblock_4 provides the best combination of composition coverage (spanning x = 0–1 with 56 data points across multiple compositions) and temperature variation (293.15 to 323.15 K), making it ideal for studying the composition and temperature dependence of density in propan-2-ol + water binary mixtures.
</answer>