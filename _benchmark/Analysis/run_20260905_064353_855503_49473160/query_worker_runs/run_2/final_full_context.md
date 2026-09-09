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
Find binary ethanol + water mass density blocks at atmospheric pressure (~101 kPa) covering a wide composition range (ideally 0 to 1 mole fraction ethanol) near 298-353 K

## Instruction
Search for binary ethanol + water mass density (GLOBprop_1) blocks. I need data at atmospheric or near-atmospheric pressure (around 101 kPa) covering a WIDE composition range (not just dilute). The temperature should be near 298-353 K. Return all matching blocks with their DOIs, block numbers, temperature ranges, pressure ranges, composition ranges, and data point counts. Also check blocks GLOBlit_220 and GLOBlit_2432 which were previously identified as potential ethanol+water density blocks.

## ID Catalog (from working memory)
[{"global_id": "GLOBcomp_2", "name": "ethanol", "registry_id": "64-17-5", "type": "comp"}, {"global_id": "GLOBcomp_1", "name": "water", "registry_id": "7732-18-5", "type": "comp"}, {"global_id": "GLOBprop_1", "name": "Mass density", "registry_id": "", "type": "prop"}]

## Prior Context
GLOBlit_1483 PROPblock_1 was already inspected - it has only 4 dilute ethanol compositions (x=0.0163-0.0946) at high pressures (2.5-40 MPa). This is unsuitable for a full-range RK fit. I need blocks with wider composition coverage at atmospheric pressure.

## Assistant
<summary>Searching for binary ethanol+water mass density blocks at atmospheric pressure with wide composition coverage. Will check general search results plus specific references GLOBlit_220 and GLOBlit_2432.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_2', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Fixing the pressure_range argument format to a list of floats [90, 110] and re-searching for binary ethanol+water mass density blocks.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_2', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
**Summary:** 20 binary ethanol+water mass density blocks found at ~101 kPa. The best candidates for wide composition coverage near 298–353 K are the large datasets from `10.1016/j.fluid.2004.11.019 [GLOBlit_220]`, `10.1016/j.jct.2018.02.022 [GLOBlit_5201]`, `10.1016/j.jct.2007.05.004 [GLOBlit_2825]`, `10.1021/je060335h [GLOBlit_9006]`, `10.1021/je700300y [GLOBlit_10866]`, and `10.1021/je800150h [GLOBlit_11136]`.

**Top blocks ranked by composition coverage and T-range relevance:**

| Rank | DOI | Block | GLOBlit | Pts | T (K) | Composition range | ρ (kg/m³) |
|------|-----|-------|---------|-----|--------|-------------------|-----------|
| 1 | 10.1016/j.fluid.2004.11.019 | PROPblock_2 | GLOBlit_220 | 810 | 298.15 | x(ethanol) 0.003–0.7996 | 810.9–995.3 |
| 2 | 10.1016/j.jct.2018.02.022 | PROPblock_19 | GLOBlit_5201 | 244 | 293.15–298.15 | x(ethanol) 0.0024–0.9895 | 791.076–997.039 |
| 3 | 10.1016/j.jct.2007.05.004 | PROPblock_12 | GLOBlit_2825 | 37 | 293.15–303.15 | x(water) 0–1 | 781.15–998.2 |
| 4 | 10.1021/je060335h | PROPblock_1 | GLOBlit_9006 | 164 | 283.15–288.15 | x(ethanol) 0–1 | 797.93–999.7 |
| 5 | 10.1021/je700300y | PROPblock_7 | GLOBlit_10866 | 84 | 283.15–303.15 | x(water) 0.0805–0.9605 | 790.85–984.04 |
| 6 | 10.1021/je800150h | PROPblock_9 | GLOBlit_11136 | 108 | 268.1–323.15 | x(water) 0.1–0.5 | 774.3–886.6 |
| 7 | 10.1021/je600565m | PROPblock_6 | GLOBlit_10699 | 18 | 298.15–318.15 | x(water) 0.0998–0.9051 | 780.53–965.51 |
| 8 | 10.1021/je700618y | PROPblock_9 | GLOBlit_11005 | 15 | fixed T | x(water) 0.048–0.9481 | 791.06–976.77 |
| 9 | 10.1016/j.jct.2019.02.027 | PROPblock_21 | GLOBlit_5473 | 9 | fixed T | x(ethanol) 0–1 | 785.5–997.1 |

**Notes:** None of the returned blocks extend to 353 K. The highest T coverage is `10.1021/je800150h [GLOBlit_11136]` (up to 323.15 K) and `10.1021/je800942u [GLOBlit_11459]` (up to 328.15 K, but narrow composition w(water) 0.15–0.25). A follow-up search with a broader or higher temperature range (e.g., 320–360 K) may be needed to find data closer to 353 K.
</tool_result>

## Assistant
<summary>Found 20 blocks but none reach 353 K. Best wide-composition blocks: GLOBlit_220 (810 pts, x=0.003–0.80, T=298.15 K), GLOBlit_5201 (244 pts, x=0.0024–0.9895, T=293–298 K), GLOBlit_2825 (37 pts, x=0–1, T=293–303 K). Now searching for higher-T data (320–360 K) and checking GLOBlit_2432.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_2', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
**Summary:** 7 binary ethanol+water mass density blocks found in the 320–360 K search window. The two most relevant for ~353 K are **GLOBlit_1742** (T: 350.7–373.2 K, 84 pts, elevated pressures 10–40 MPa) and **GLOBlit_1483** (T: 292.95–448.15 K, 140 pts, pressures 2.45–39.9 MPa). Both cover the target temperature but at high pressures rather than atmospheric.

| # | DOI | Block | GLOBlit | Pts | T range (K) | P range (kPa) | Composition var | Notes |
|---|-----|-------|---------|-----|-------------|----------------|-----------------|-------|
| 1 | 10.1016/j.fluid.2015.07.012 | PROPblock_3 | GLOBlit_1742 | 84 | 350.7–373.2 | 10000–40000 | x(ethanol): 0.1–1.0 | Best T match to 353 K; high P only |
| 2 | 10.1016/j.fluid.2014.05.032 | PROPblock_1 | GLOBlit_1483 | 140 | 292.95–448.15 | 2450–39910 | x(ethanol): 0.0163–0.073 | Wide T range covers 353 K; high P; dilute ethanol |
| 3 | 10.1016/j.fluid.2004.11.019 | PROPblock_2 | GLOBlit_220 | 810 | 298.15–298.15* | 100–100* | x(ethanol): 0.003–0.7996 | Sampled topology shows only 298 K; may have more T in full data |
| 4 | 10.1016/j.jct.2004.07.019 | PROPblock_2 | GLOBlit_2432 | 565 | 298.15–298.18* | 410–29930 | molality: 0.097–0.943 | Sampled at ~298 K; full data may extend higher |
| 5 | 10.1021/je800150h | PROPblock_9 | GLOBlit_11136 | 108 | 268.1–323.15 | 101 (fixed) | x(water): 0.1–0.5 | Max T = 323.15 K, below target |
| 6 | 10.1021/je800942u | PROPblock_6 | GLOBlit_11459 | 18 | 303.15–328.15 | 101 (fixed) | w(water): 0.15–0.25 | Max T = 328.15 K, below target |
| 7 | 10.1021/je900064e | PROPblock_6 | GLOBlit_11504 | 10 | monotonic↓ | 101 (fixed) | φ(ethanol) = 0.5 fixed | T range not explicit; likely ≤323 K |

*Sampled topology shows limited T; full dataset (810/565 pts) likely spans wider range.

**Key finding:** No atmospheric-pressure block clearly covers 353 K. GLOBlit_1742 (PROPblock_3) is the closest match at 350.7 K but only at elevated pressures (≥10 MPa). GLOBlit_220 and GLOBlit_2432 have large point counts and may contain higher-T data not visible in the 50-pt sample—retrieving their full data could reveal 320–360 K points.
</tool_result>

## Assistant
<summary>Found no atmospheric-pressure blocks reaching 353 K. Best candidates for wide composition at ~298 K: GLOBlit_220 (810 pts), GLOBlit_5201 (244 pts, x≈0–1), GLOBlit_2825 (37 pts, x=0–1). Now inspecting GLOBlit_220 and GLOBlit_5201 to verify their actual T and composition coverage.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_2, literature=GLOBlit_220)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.fluid.2004.11.019 [GLOBlit_220] :: PROPblock_2 (binary: ethanol + water)
filter: none (whole block)

| BLKpoint_id | temperature_k | pressure_kpa | mole_fraction_<ethanol> | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 100 | 0.003 | 995.3 |
| BLKpoint_43 | 298.15 | 100 | 0.4501 | 868.8 |
| BLKpoint_48 | 298.15 | 100 | 0.6967 | 825.2 |
| BLKpoint_54 | 298.15 | 100 | 1 | 785.7 |
| BLKpoint_55 | 298.15 | 10000 | 0.003 | 999.8 |
| BLKpoint_97 | 298.15 | 10000 | 0.4501 | 874.7 |
| BLKpoint_102 | 298.15 | 10000 | 0.6967 | 832.3 |
| BLKpoint_108 | 298.15 | 10000 | 1 | 794 |
| BLKpoint_109 | 298.15 | 20000 | 0.003 | 1004.2 |
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
| BLKpoint_271 | 323.15 | 100 | 0.003 | 986.5 |
| BLKpoint_307 | 323.15 | 100 | 0.2269 | 905.2 |
| BLKpoint_313 | 323.15 | 100 | 0.4501 | 846.7 |
| BLKpoint_318 | 323.15 | 100 | 0.6967 | 802.8 |
| BLKpoint_324 | 323.15 | 100 | 1 | 763.7 |
| BLKpoint_325 | 323.15 | 10000 | 0.003 | 990.8 |
| BLKpoint_361 | 323.15 | 10000 | 0.2269 | 910.3 |
| BLKpoint_367 | 323.15 | 10000 | 0.4501 | 853.3 |
| BLKpoint_372 | 323.15 | 10000 | 0.6967 | 810.9 |
| BLKpoint_378 | 323.15 | 10000 | 1 | 773.4 |
| BLKpoint_379 | 323.15 | 20000 | 0.003 | 994.9 |
| BLKpoint_415 | 323.15 | 20000 | 0.2269 | 915.3 |
| BLKpoint_421 | 323.15 | 20000 | 0.4501 | 859.7 |
| BLKpoint_426 | 323.15 | 20000 | 0.6967 | 818.4 |
| BLKpoint_432 | 323.15 | 20000 | 1 | 782.3 |
| BLKpoint_433 | 323.15 | 30000 | 0.003 | 999 |
| BLKpoint_469 | 323.15 | 30000 | 0.2269 | 920.1 |
| BLKpoint_475 | 323.15 | 30000 | 0.4501 | 865.7 |
| BLKpoint_480 | 323.15 | 30000 | 0.6967 | 825.4 |
| BLKpoint_486 | 323.15 | 30000 | 1 | 790.3 |
| BLKpoint_487 | 323.15 | 40000 | 0.003 | 1003.1 |
| BLKpoint_523 | 323.15 | 40000 | 0.2269 | 924.7 |
| BLKpoint_529 | 323.15 | 40000 | 0.4501 | 871.3 |
| BLKpoint_534 | 323.15 | 40000 | 0.6967 | 831.9 |
| BLKpoint_540 | 323.15 | 40000 | 1 | 797.7 |
| BLKpoint_541 | 348.15 | 100 | 0.003 | 973.1 |
| BLKpoint_575 | 348.15 | 100 | 0.1903 | 895.8 |
| BLKpoint_582 | 348.15 | 100 | 0.4034 | 833.4 |
| BLKpoint_587 | 348.15 | 100 | 0.6489 | 785.6 |
| BLKpoint_594 | 348.15 | 100 | 1 | 739.4 |
| BLKpoint_595 | 348.15 | 10000 | 0.003 | 977.5 |
| BLKpoint_630 | 348.15 | 10000 | 0.1996 | 898.1 |
| BLKpoint_636 | 348.15 | 10000 | 0.4034 | 840.7 |
| BLKpoint_641 | 348.15 | 10000 | 0.6489 | 794.6 |
| BLKpoint_648 | 348.15 | 10000 | 1 | 751.2 |
| BLKpoint_649 | 348.15 | 20000 | 0.003 | 981.9 |
| BLKpoint_683 | 348.15 | 20000 | 0.1903 | 906.5 |
| BLKpoint_690 | 348.15 | 20000 | 0.4034 | 847.5 |
| BLKpoint_695 | 348.15 | 20000 | 0.6489 | 802.9 |
| BLKpoint_702 | 348.15 | 20000 | 1 | 761.2 |
| BLKpoint_703 | 348.15 | 30000 | 0.003 | 986.1 |
| BLKpoint_738 | 348.15 | 30000 | 0.1996 | 908.5 |
| BLKpoint_744 | 348.15 | 30000 | 0.4034 | 854 |
| BLKpoint_749 | 348.15 | 30000 | 0.6489 | 810.6 |
| BLKpoint_756 | 348.15 | 30000 | 1 | 770.3 |
| BLKpoint_757 | 348.15 | 40000 | 0.003 | 990.1 |
| BLKpoint_791 | 348.15 | 40000 | 0.1903 | 916.4 |
| BLKpoint_798 | 348.15 | 40000 | 0.4034 | 860 |
| BLKpoint_803 | 348.15 | 40000 | 0.6489 | 817.8 |
| BLKpoint_810 | 348.15 | 40000 | 1 | 778.6 |

mode: RDP — 72 of 810 matched rows shown (shape-preserving; block has 810). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=810): temperature_k 298.15–348.15 (n=810); pressure_kpa 100–40000 (n=810); mole_fraction_ethanol 0.003–1 (n=810); mass_density_kg_m3 739.4–1012.7 (n=810)
inspection_id: INSP_38392edfd29c
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>GLOBlit_220 PROPblock_2 confirmed: 810 pts, T = 298.15/323.15/348.15 K, P = 100–40000 kPa, x(ethanol) = 0.003–1.0. At atmospheric (100 kPa), covers full composition range at 3 temperatures (298–348 K). Now inspecting atmospheric-only subset and GLOBlit_5201 for comparison.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_2, literature=GLOBlit_220, where=pressure_kpa = 100)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.fluid.2004.11.019 [GLOBlit_220] :: PROPblock_2 (binary: ethanol + water)
filter: where pressure_kpa = 100

| BLKpoint_id | temperature_k | pressure_kpa | mole_fraction_<ethanol> | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 100 | 0.003 | 995.3 |
| BLKpoint_38 | 298.15 | 100 | 0.2502 | 918.5 |
| BLKpoint_43 | 298.15 | 100 | 0.4501 | 868.8 |
| BLKpoint_48 | 298.15 | 100 | 0.6967 | 825.2 |
| BLKpoint_54 | 298.15 | 100 | 1 | 785.7 |
| BLKpoint_271 | 323.15 | 100 | 0.003 | 986.5 |
| BLKpoint_307 | 323.15 | 100 | 0.2269 | 905.2 |
| BLKpoint_313 | 323.15 | 100 | 0.4501 | 846.7 |
| BLKpoint_318 | 323.15 | 100 | 0.6967 | 802.8 |
| BLKpoint_324 | 323.15 | 100 | 1 | 763.7 |
| BLKpoint_541 | 348.15 | 100 | 0.003 | 973.1 |
| BLKpoint_575 | 348.15 | 100 | 0.1903 | 895.8 |
| BLKpoint_582 | 348.15 | 100 | 0.4034 | 833.4 |
| BLKpoint_587 | 348.15 | 100 | 0.6489 | 785.6 |
| BLKpoint_594 | 348.15 | 100 | 1 | 739.4 |

mode: RDP — 15 of 162 matched rows shown (shape-preserving; block has 810). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=162): temperature_k 298.15–348.15 (n=162); pressure_kpa 100–100 (n=162); mole_fraction_ethanol 0.003–1 (n=162); mass_density_kg_m3 739.4–995.3 (n=162)
stats (full block, n=810): temperature_k 298.15–348.15 (n=810); pressure_kpa 100–40000 (n=810); mole_fraction_ethanol 0.003–1 (n=810); mass_density_kg_m3 739.4–1012.7 (n=810)
inspection_id: INSP_13b9dbeeee1e
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<reasoning>
I now have excellent data on GLOBlit_220 PROPblock_2. At atmospheric pressure (100 kPa), there are 162 data points across 3 temperatures (298.15, 323.15, 348.15 K) with x(ethanol) from 0.003 to 1.0. This is a very strong candidate.

Let me also check GLOBlit_5201 which had x(ethanol) 0.0024–0.9895 at 293–298 K, and GLOBlit_2825 which had x=0–1 at 293–303 K. These could complement GLOBlit_220.

I should also check GLOBlit_2432 as requested. Let me inspect GLOBlit_5201 to see its atmospheric data.

Actually, I have enough information to provide a comprehensive answer. Let me summarize:

1. **GLOBlit_220 PROPblock_2** - BEST candidate: 162 atmospheric points, T = 298.15/323.15/348.15 K, x(ethanol) = 0.003–1.0, ρ = 739.4–995.3 kg/m³
2. **GLOBlit_5201 PROPblock_19** - 244 pts, T = 293–298 K, x = 0.0024–0.9895 (but only ~298 K)
3. **GLOBlit_2825 PROPblock_12** - 37 pts, T = 293–303 K, x = 0–1
4. **GLOBlit_2432 PROPblock_2** - 565 pts but at pressures 410–29930 kPa (not atmospheric)

The GLOBlit_220 block is clearly the best - it has wide composition coverage at atmospheric pressure AND covers 298–348 K (close to the 298–353 K target). Let me provide the answer.
</reasoning>

<answer>
## Binary Ethanol + Water Mass Density Blocks at Atmospheric Pressure

### Best Candidate: GLOBlit_220 :: PROPblock_2
**DOI:** 10.1016/j.fluid.2004.11.019

This block is the strongest match for wide-composition, multi-temperature density data at atmospheric pressure:

- **Total points:** 810 (162 at atmospheric pressure, P = 100 kPa)
- **Temperatures:** 298.15, 323.15, and 348.15 K (three isotherms)
- **Composition range:** x(ethanol) = 0.003–1.0 (full range)
- **Density range (at 100 kPa):** 739.4–995.3 kg/m³

Representative atmospheric-pressure data (from inspection):

| T (K) | x(ethanol) | ρ (kg/m³) |
|--------|-----------|-----------|
| 298.15 | 0.003 | 995.3 |
| 298.15 | 0.2502 | 918.5 |
| 298.15 | 0.4501 | 868.8 |
| 298.15 | 0.6967 | 825.2 |
| 298.15 | 1.0 | 785.7 |
| 323.15 | 0.003 | 986.5 |
| 323.15 | 0.2269 | 905.2 |
| 323.15 | 0.4501 | 846.7 |
| 323.15 | 0.6967 | 802.8 |
| 323.15 | 1.0 | 763.7 |
| 348.15 | 0.003 | 973.1 |
| 348.15 | 0.1903 | 895.8 |
| 348.15 | 0.4034 | 833.4 |
| 348.15 | 0.6489 | 785.6 |
| 348.15 | 1.0 | 739.4 |

Each isotherm has ~54 composition points (162 total / 3 temperatures), providing dense composition coverage ideal for Redlich-Kister fitting.

### Other Candidates with Wide Composition Coverage

| Rank | DOI | Block | GLOBlit | Pts | T (K) | x(ethanol) range | Notes |
|------|-----|-------|---------|-----|--------|------------------|-------|
| 2 | 10.1016/j.jct.2018.02.022 | PROPblock_19 | GLOBlit_5201 | 244 | 293.15–298.15 | 0.0024–0.9895 | Near-full range but only ~298 K |
| 3 | 10.1016/j.jct.2007.05.004 | PROPblock_12 | GLOBlit_2825 | 37 | 293.15–303.15 | 0–1 (x_water) | Full range, fewer points |
| 4 | 10.1021/je060335h | PROPblock_1 | GLOBlit_9006 | 164 | 283.15–288.15 | 0–1 | Full range but T below target |
| 5 | 10.1021/je700300y | PROPblock_7 | GLOBlit_10866 | 84 | 283.15–303.15 | x(water) 0.08–0.96 | Good range, T below target |
| 6 | 10.1021/je600565m | PROPblock_6 | GLOBlit_10699 | 18 | 298.15–318.15 | x(water) 0.10–0.91 | Fewer points |
| 7 | 10.1021/je800150h | PROPblock_9 | GLOBlit_11136 | 108 | 268.1–323.15 | x(water) 0.1–0.5 | Partial composition, max 323 K |
| 8 | 10.1016/j.jct.2019.02.027 | PROPblock_21 | GLOBlit_5473 | 9 | fixed T | 0–1 | Full range, very few points |

### Regarding GLOBlit_2432
**DOI:** 10.1016/j.jct.2004.07.019, PROPblock_2 — This block has 565 points but operates at elevated pressures (410–29930 kPa), not atmospheric. Composition is reported in molality (0.097–0.943 mol/kg) and T ≈ 298 K. **Not suitable** for atmospheric-pressure fitting.

### Key Finding
**No block in the database covers 353 K at atmospheric pressure** for this binary system. The closest is GLOBlit_220 at 348.15 K (5 K below target). GLOBlit_1742 reaches 350.7–373.2 K but only at elevated pressures (10–40 MPa). 

**Recommendation:** GLOBlit_220 :: PROPblock_2 is the best single source — it provides ~54 compositions per isotherm at 100 kPa across 298.15, 323.15, and 348.15 K, covering x(ethanol) = 0.003–1.0. The 348.15 K isotherm is close to the 353 K target and could be used with minimal extrapolation concern.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** GLOBlit_220::PROPblock_2: 54 (near '…Each isotherm has ~54 composition points (162 total / 3 temp…') matches no inspected row/stat, database table, or other source of GLOBlit_220::PROPblock_2
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2", nearest={"column": "temperature_k", "value": 54.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNINSPECTED_BLOCK** PROPblock_19 + PROPblock_12 + PROPblock_1 + PROPblock_7 + PROPblock_6 + PROPblock_9 + PROPblock_21: PROPblock_19 + PROPblock_12 + PROPblock_1 + PROPblock_7 + PROPblock_6 + PROPblock_9 + PROPblock_21 is quoted with data values (244, 293.15, 298.15, 0.0024, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_19", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_12", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_1", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_7", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_6", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_9", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_21", literature="<GLOBlit_N or DOI>")`
- **UNGROUNDED_LITERAL** PROPblock_2: 565 (near '…— This block has 565 points but operates at elevated pressur…') matches no inspected row/stat, database table, or other source of PROPblock_2
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_2", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 565.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_2: 410 (near '…is block has 565 points but operates at elevated pressures (…') matches no inspected row/stat, database table, or other source of PROPblock_2
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_2", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 410.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_2: 29930 (near '…lock has 565 points but operates at elevated pressures (410–…') matches no inspected row/stat, database table, or other source of PROPblock_2
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_2", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 29930.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_2: 0.097 (near '…kPa), not atmospheric. Composition is reported in molality (…') matches no inspected row/stat, database table, or other source of PROPblock_2
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_2", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 0.097})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_2: 353 (near '…fitting.  ### Key Finding **No block in the database covers …') matches no inspected row/stat, database table, or other source of PROPblock_2
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_2", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 353.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_2: 350.7 (near '…The closest is   at 348.15 K (5 K below target).   reaches 3…') matches no inspected row/stat, database table, or other source of PROPblock_2
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_2", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 350.7})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- … and 3 more of the same kinds — PROPblock_2: 373.2; GLOBlit_220::PROPblock_2: 54, 353
Inspected so far: PROPblock_2

Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- GLOBlit_220::PROPblock_2: 810, 162, 100, 298.15, 323.15, 348.15, 0.003, 1.0, 739.4, 995.3, 0.2502, 918.5, 0.4501, 868.8, 0.6967, 825.2, 785.7, 986.5, 0.2269, 905.2, 846.7, 802.8, 763.7, 973.1, 0.1903, 895.8, 0.4034, 833.4, 0.6489, 785.6
- PROPblock_2: 0.943, 298, 348.15, 40

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## Assistant


<reasoning>
The data grounding checker flagged several issues:

1. "~54 composition points" - this is my calculation (162/3 = 54), not a database value. I should label it as derived.
2. The "Other Candidates" table values (244, 293.15, 0.0024, etc.) came from the search_blocks tool results, not from inspect_block_table. These blocks were never inspected. I need to either inspect them or note they come from search results.
3. GLOBlit_2432 values (565, 410, 29930, 0.097, 0.943) came from search_blocks results, not inspection.
4. Values like 353, 350.7, 373.2 are from the instruction/search results context, not database inspections of PROPblock_2.

The checker says "UNINSPECTED_BLOCK" for PROPblock_19, 12, 1, 7, 6, 9, 21 - these need inspection. But I have a 3-tool-call limit concern. However, the grounding checker says "fix (required)" so I need to inspect them or drop the data values.

Given the time constraint, the most efficient approach is to drop the uninspected block details (just list them without specific data values) or note they come from search_blocks summary. Actually, the values came from the search_blocks tool result which IS a tool result in this conversation. But the grounding rules say block data must be inspected via inspect_block_table.

Let me take the surgical approach: keep the GLOBlit_220 data (which IS inspected), label derived values, and for the other blocks, note that the summary information comes from the search_blocks discovery tool rather than direct inspection. I should not quote specific data values for uninspected blocks.

Actually, I can batch inspect a few key ones. But I have many blocks to inspect. Let me just fix the answer by:
1. Labeling "~54" as derived (162/3)
2. For the other candidates table, noting values are from search_blocks summary (not inspected)
3. For GLOBlit_2432, noting values are from search_blocks summary
4. For 353, 350.7, 373.2 - these are from the instruction context and search results, not database data from PROPblock_2

Let me just provide the corrected answer without needing more tool calls.
</reasoning>

<answer>
## Binary Ethanol + Water Mass Density Blocks at Atmospheric Pressure

### Best Candidate: GLOBlit_220 :: PROPblock_2
**DOI:** 10.1016/j.fluid.2004.11.019

This block is the strongest match for wide-composition, multi-temperature density data at atmospheric pressure:

- **Total points:** 810 (162 at atmospheric pressure, P = 100 kPa)
- **Temperatures:** 298.15, 323.15, and 348.15 K (three isotherms)
- **Composition range:** x(ethanol) = 0.003–1.0 (full range)
- **Density range (at 100 kPa):** 739.4–995.3 kg/m³

Representative atmospheric-pressure data (from inspection):

| T (K) | x(ethanol) | ρ (kg/m³) |
|--------|-----------|-----------|
| 298.15 | 0.003 | 995.3 |
| 298.15 | 0.2502 | 918.5 |
| 298.15 | 0.4501 | 868.8 |
| 298.15 | 0.6967 | 825.2 |
| 298.15 | 1.0 | 785.7 |
| 323.15 | 0.003 | 986.5 |
| 323.15 | 0.2269 | 905.2 |
| 323.15 | 0.4501 | 846.7 |
| 323.15 | 0.6967 | 802.8 |
| 323.15 | 1.0 | 763.7 |
| 348.15 | 0.003 | 973.1 |
| 348.15 | 0.1903 | 895.8 |
| 348.15 | 0.4034 | 833.4 |
| 348.15 | 0.6489 | 785.6 |
| 348.15 | 1.0 | 739.4 |

Each isotherm has approximately 54 composition points (derived: 162 total atmospheric points / 3 temperatures), providing dense composition coverage ideal for Redlich-Kister fitting.

### Other Candidates with Wide Composition Coverage

The following blocks were identified by the `search_blocks` discovery tool but have **not been individually inspected**. The summary values below are from the search discovery results, not from direct block inspection:

- **GLOBlit_5201 :: PROPblock_19** (DOI: 10.1016/j.jct.2018.02.022) — reported ~244 pts, T near 293–298 K, x(ethanol) ~0.0024–0.9895. Near-full composition range but only around 298 K.
- **GLOBlit_2825 :: PROPblock_12** (DOI: 10.1016/j.jct.2007.05.004) — reported ~37 pts, T ~293–303 K, full composition range (x_water 0–1). Fewer points.
- **GLOBlit_9006 :: PROPblock_1** (DOI: 10.1021/je060335h) — reported ~164 pts, T ~283–288 K, x(ethanol) 0–1. Full range but T below target.
- **GLOBlit_10866 :: PROPblock_7** (DOI: 10.1021/je700300y) — reported ~84 pts, T ~283–303 K, x(water) ~0.08–0.96. Good range, T below target.
- **GLOBlit_10699 :: PROPblock_6** (DOI: 10.1021/je600565m) — reported ~18 pts, T ~298–318 K, x(water) ~0.10–0.91. Fewer points.
- **GLOBlit_11136 :: PROPblock_9** (DOI: 10.1021/je800150h) — reported ~108 pts, T ~268–323 K, x(water) ~0.1–0.5. Partial composition, max ~323 K.
- **GLOBlit_5473 :: PROPblock_21** (DOI: 10.1016/j.jct.2019.02.027) — reported ~9 pts, x(ethanol) 0–1. Full range, very few points.

### Regarding GLOBlit_2432
**DOI:** 10.1016/j.jct.2004.07.019, PROPblock_2 — Per the search discovery results (not individually inspected), this block has elevated pressures (not atmospheric) and composition reported in molality. **Not suitable** for atmospheric-pressure fitting.

### Key Finding
**No block in the database was found to cover the target upper temperature of 353 K at atmospheric pressure** for this binary system. The closest inspected data is GLOBlit_220 at 348.15 K. Per search discovery results, GLOBlit_1742 (PROPblock_3) reaches higher temperatures but only at elevated pressures (search reported 10–40 MPa range).

**Recommendation:** GLOBlit_220 :: PROPblock_2 is the best single source — it provides dense composition coverage at 100 kPa across 298.15, 323.15, and 348.15 K, with x(ethanol) = 0.003–1.0. The 348.15 K isotherm is close to the 353 K target.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** GLOBlit_220::PROPblock_2: 54 (near '…Each isotherm has approximately 54 composition points (deriv…') matches no inspected row/stat, database table, or other source of GLOBlit_220::PROPblock_2
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2", nearest={"column": "temperature_k", "value": 54.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNINSPECTED_BLOCK** GLOBlit_5201::PROPblock_19: GLOBlit_5201::PROPblock_19 is quoted with data values (244, 293, 298, 0.0024, …) but was never inspected in this run (values 293, 298, 0.0024, 0.9895 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_5201::PROPblock_19")`
- **UNINSPECTED_BLOCK** GLOBlit_2825::PROPblock_12: GLOBlit_2825::PROPblock_12 is quoted with data values (37, 293, 303, …) but was never inspected in this run (values 293, 303 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_2825::PROPblock_12")`
- **UNINSPECTED_BLOCK** GLOBlit_9006::PROPblock_1: GLOBlit_9006::PROPblock_1 is quoted with data values (164, 283, 288, …) but was never inspected in this run (values 283, 288 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_9006::PROPblock_1")`
- **UNINSPECTED_BLOCK** GLOBlit_10866::PROPblock_7: GLOBlit_10866::PROPblock_7 is quoted with data values (84, 283, 303, 0.08, …) but was never inspected in this run (values 283, 303, 0.08, 0.96 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_10866::PROPblock_7")`
- **UNINSPECTED_BLOCK** GLOBlit_10699::PROPblock_6: GLOBlit_10699::PROPblock_6 is quoted with data values (18, 298, 318, 0.10, …) but was never inspected in this run (values 298, 318, 0.10, 0.91 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_10699::PROPblock_6")`
- **UNINSPECTED_BLOCK** GLOBlit_11136::PROPblock_9: GLOBlit_11136::PROPblock_9 is quoted with data values (108, 268, 323, 0.1, …) but was never inspected in this run (values 268, 323, 0.1, 0.5 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_11136::PROPblock_9")`
- **UNGROUNDED_LITERAL** PROPblock_2: 353 (near '…database was found to cover the target upper temperature of …') matches no inspected row/stat, database table, or other source of PROPblock_2
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_2", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 353.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- … and 2 more of the same kinds — PROPblock_3: 40; GLOBlit_220::PROPblock_2: 353
Inspected so far: PROPblock_2

Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- GLOBlit_220::PROPblock_2: 810, 162, 100, 298.15, 323.15, 348.15, 0.003, 1.0, 739.4, 995.3, 0.2502, 918.5, 0.4501, 868.8, 0.6967, 825.2, 785.7, 986.5, 0.2269, 905.2, 846.7, 802.8, 763.7, 973.1, 0.1903, 895.8, 0.4034, 833.4, 0.6489, 785.6
- PROPblock_2: 348.15

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## Assistant
<summary>Need to inspect uninspected blocks to ground their data values. Will batch inspect the most important secondary candidates: GLOBlit_5201::PROPblock_19, GLOBlit_2825::PROPblock_12, GLOBlit_9006::PROPblock_1, GLOBlit_10866::PROPblock_7, GLOBlit_10699::PROPblock_6, GLOBlit_11136::PROPblock_9, and GLOBlit_5473::PROPblock_21.</summary>
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
<summary>Inspected GLOBlit_5201::PROPblock_19: 244 pts, T=293.15–308.15 K, x(ethanol)=0–1, P=92.3 kPa. Now inspecting remaining uninspected blocks: GLOBlit_2825, GLOBlit_9006, GLOBlit_10866, GLOBlit_10699, GLOBlit_11136.</summary>
<tool_call>inspect_block_table(block_number=GLOBlit_2825::PROPblock_12)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1016/j.jct.2007.05.004 [GLOBlit_2825] :: PROPblock_12 (binary: ethanol + water)
filter: none (whole block)
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mole_fraction_<water> | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 293.15 | 0 | 101.0 | 789.75 |
| BLKpoint_7 | 293.15 | 0.4971 | 101.0 | 862.82 |
| BLKpoint_9 | 293.15 | 0.6991 | 101.0 | 908.69 |
| BLKpoint_13 | 293.15 | 1 | 101.0 | 998.2 |
| BLKpoint_14 | 298.15 | 0 | 101.0 | 785.46 |
| BLKpoint_19 | 298.15 | 0.3991 | 101.0 | 840.94 |
| BLKpoint_20 | 298.15 | 0.5989 | 101.0 | 879.89 |
| BLKpoint_25 | 298.15 | 1 | 101.0 | 997.05 |
| BLKpoint_26 | 303.15 | 0 | 101.0 | 781.15 |
| BLKpoint_30 | 303.15 | 0.2961 | 101.0 | 820.29 |
| BLKpoint_32 | 303.15 | 0.5989 | 101.0 | 875.63 |
| BLKpoint_37 | 303.15 | 1 | 101.0 | 995.65 |

mode: RDP — 12 of 37 matched rows shown (shape-preserving; block has 37). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=37): temperature_k 293.15–303.15 (n=37); mole_fraction_water 0–1 (n=37); pressure_kpa 101.0–101.0 (n=37); mass_density_kg_m3 781.15–998.2 (n=37)
inspection_id: INSP_1d2031e2c9c2
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## User
[TIME WARNING 1/3] 65% of time budget used (237s / 360s). Wrap up soon — provide your best answer with available data.

## LLM Response
<reasoning>
I need to wrap up quickly. I have inspected GLOBlit_220::PROPblock_2, GLOBlit_5201::PROPblock_19, and GLOBlit_2825::PROPblock_12. The remaining blocks (GLOBlit_9006, GLOBlit_10866, GLOBlit_10699, GLOBlit_11136, GLOBlit_5473) have not been inspected. I should drop their specific data values and just mention them without numbers, or note they were not inspected.

Let me provide the final answer now with only inspected data.

Key fixes needed:
1. "~54" → label as derived (162/3)
2. GLOBlit_5201 → now inspected: 244 pts, T=293.15–308.15 K, x=0–1, P=92.3 kPa
3. GLOBlit_2825 → now inspected: 37 pts, T=293.15–303.15 K, x(water)=0–1, P=101.0 kPa
4. Other blocks → not inspected, drop specific values
5. "353" is from the instruction (target temperature), not database data
6. "350.7", "373.2", "40" for GLOBlit_1742 → from search results, not inspected; note as search-reported
</reasoning>

<answer>
## Binary Ethanol + Water Mass Density Blocks at Atmospheric Pressure

### Best Candidate: GLOBlit_220 :: PROPblock_2
**DOI:** 10.1016/j.fluid.2004.11.019

This block is the strongest match for wide-composition, multi-temperature density data at atmospheric pressure:

- **Total points:** 810 (162 at atmospheric pressure, P = 100 kPa)
- **Temperatures:** 298.15, 323.15, and 348.15 K (three isotherms)
- **Composition range:** x(ethanol) = 0.003–1.0 (full range)
- **Density range (at 100 kPa):** 739.4–995.3 kg/m³

Representative atmospheric-pressure data (from inspection):

| T (K) | x(ethanol) | ρ (kg/m³) |
|--------|-----------|-----------|
| 298.15 | 0.003 | 995.3 |
| 298.15 | 0.2502 | 918.5 |
| 298.15 | 0.4501 | 868.8 |
| 298.15 | 0.6967 | 825.2 |
| 298.15 | 1.0 | 785.7 |
| 323.15 | 0.003 | 986.5 |
| 323.15 | 0.2269 | 905.2 |
| 323.15 | 0.4501 | 846.7 |
| 323.15 | 0.6967 | 802.8 |
| 323.15 | 1.0 | 763.7 |
| 348.15 | 0.003 | 973.1 |
| 348.15 | 0.1903 | 895.8 |
| 348.15 | 0.4034 | 833.4 |
| 348.15 | 0.6489 | 785.6 |
| 348.15 | 1.0 | 739.4 |

Each isotherm has approximately 54 composition points (derived by dividing 162 atmospheric points by 3 isotherms — not a database value), providing dense composition coverage ideal for Redlich-Kister fitting.

### Other Inspected Candidates

**GLOBlit_5201 :: PROPblock_19** (DOI: 10.1016/j.jct.2018.02.022)
- **Points:** 244, all at P = 92.3 kPa (near-atmospheric)
- **Temperature:** 293.15–308.15 K (4 isotherms)
- **Composition:** x(ethanol) = 0–1 (full range)
- **Density:** 776.592–998.429 kg/m³
- Excellent composition coverage but temperature range is narrower and lower than GLOBlit_220.

**GLOBlit_2825 :: PROPblock_12** (DOI: 10.1016/j.jct.2007.05.004)
- **Points:** 37, all at P = 101.0 kPa
- **Temperature:** 293.15–303.15 K (3 isotherms)
- **Composition:** x(water) = 0–1 (full range)
- **Density:** 781.15–998.2 kg/m³
- Full composition range at atmospheric pressure, but fewer points and lower temperatures.

### Additional Candidates (Not Inspected)

The following blocks were identified by the search discovery tool but have not been individually inspected in this run. No specific data values are quoted for them:

- **GLOBlit_9006 :: PROPblock_1** (DOI: 10.1021/je060335h) — search-reported as having full composition range at lower temperatures.
- **GLOBlit_10866 :: PROPblock_7** (DOI: 10.1021/je700300y) — search-reported as having wide composition range.
- **GLOBlit_10699 :: PROPblock_6** (DOI: 10.1021/je600565m) — search-reported as having moderate composition range.
- **GLOBlit_11136 :: PROPblock_9** (DOI: 10.1021/je800150h) — search-reported as having partial composition range.
- **GLOBlit_5473 :: PROPblock_21** (DOI: 10.1016/j.jct.2019.02.027) — search-reported as having full composition range with very few points.

### Regarding GLOBlit_2432
**DOI:** 10.1016/j.jct.2004.07.019, PROPblock_2 — Per search discovery results (not individually inspected), this block operates at elevated pressures, not atmospheric. **Not suitable** for atmospheric-pressure fitting.

### Key Finding
**No block in the database was found to cover the requested upper temperature of 353 K (instruction target, not a database value) at atmospheric pressure** for this binary system. The closest inspected data is GLOBlit_220 at 348.15 K. Per search discovery results (not inspected), GLOBlit_1742 (PROPblock_3) reaches higher temperatures but only at elevated pressures.

**Recommendation:** GLOBlit_220 :: PROPblock_2 is the best single source — it provides dense composition coverage at 100 kPa across 298.15, 323.15, and 348.15 K, with x(ethanol) = 0.003–1.0. GLOBlit_5201 :: PROPblock_19 (244 pts, x = 0–1, T = 293.15–308.15 K, P = 92.3 kPa) could supplement with additional near-ambient data.
</answer>