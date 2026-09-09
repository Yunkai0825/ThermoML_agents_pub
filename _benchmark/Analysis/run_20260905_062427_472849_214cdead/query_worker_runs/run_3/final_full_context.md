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
Find dynamic viscosity data for binary systems of N,N-dimethylformamide (DMF) + water and N,N-dimethylacetamide (DMAc) + water near 298.15 K at atmospheric pressure

## Instruction
Search for dynamic viscosity (GLOBprop_4) measurements for two binary systems: (1) N,N-dimethylformamide + water, and (2) N,N-dimethylacetamide + water. Look for data blocks containing measurements near 298.15 K. Report DOI, literature ID, block number, number of data points, temperature range, composition variable, and representative viscosity values at 298.15 K for each system found. Include the compound global IDs.

## ID Catalog (from working memory)
[]

## Assistant
(syntax-rejected turn — malformed tool calls never executed; corrected on a later turn. Full detail in the run log.)

## User
(validation fired earlier — corrected)

## Assistant
<summary>Resolving compound IDs for DMF, DMAc, and water to begin the search.</summary>
<tool_call>resolve_compound_ids(queries=['N,N-dimethylfor…, min_score=50, limit=5)</tool_call>

## User
<tool_result>
**Summary:** The resolution returned an exact match for DMF and a likely match for DMAc, but **water was not found** in the results. The main agent should issue a separate query for water (e.g., query "water" or CAS 7732-18-5).

**Resolved compounds:**

| Compound | Global ID | Name | Formula | SMILES | Score | Match |
|---|---|---|---|---|---|---|
| **DMF** | GLOBcomp_18 | dimethylformamide | C3H7NO | CN(C)C=O | 100 | name_exact |
| **DMAc** | GLOBcomp_63 | N,N-dimethylethanamide | C4H9NO | CC(=O)N(C)C | 88 | name_fuzzy |
| **Water** | — | *not returned* | — | — | — | — |

**Note:** GLOBcomp_63 (N,N-dimethylethanamide) is the IUPAC name for N,N-dimethylacetamide (DMAc). The main agent should confirm this ID and separately resolve water.
</tool_result>

## Assistant
<summary>DMF = GLOBcomp_18, DMAc = GLOBcomp_63. Now resolving water compound ID.</summary>
<tool_call>resolve_compound_ids(queries=['water'], min_score=50, limit=5)</tool_call>

## User
<tool_result>
Water resolved successfully.

| Name | ID | Formula | SMILES | Score | Match |
|---|---|---|---|---|---|
| water | GLOBcomp_1 | H2O | O | 100 | name_exact |
</tool_result>

## Assistant
<summary>All compound IDs resolved: DMF=GLOBcomp_18, DMAc=GLOBcomp_63, Water=GLOBcomp_1. Now searching for dynamic viscosity (GLOBprop_4) data blocks for both binary systems near 298.15 K.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_18', 'GLOBcomp_1'], property=GLOBprop_4, system_type=binary…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Fixing temperature_range format to list of floats and searching for DMF+water and DMAc+water viscosity data blocks.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_18', 'GLOBcomp_1'], property=GLOBprop_4, system_type=binary…)</tool_call>

## User
<tool_result>
**Summary:** Five blocks found with dynamic viscosity (Pa·s) data for the DMF (GLOBcomp_18) + water (GLOBcomp_1) binary system near 298.15 K. The best candidates are GLOBlit_8676 (isothermal at exactly 298.15 K, 11 pts across full composition range) and GLOBlit_11030 (98 pts, T: 293.15–323.15 K, full composition range).

| # | DOI | Block | GLOBlit | Pts | T range (K) | Composition var | Notes |
|---|-----|-------|---------|-----|-------------|-----------------|-------|
| 1 | 10.1021/je050209y | PROPblock_9 | GLOBlit_8676 | 11 | 298.15 (fixed) | x(DMF) 0–1 | **Exact T match**, full x range |
| 2 | 10.1021/je1008813 | PROPblock_3 | GLOBlit_9342 | 16 | 308.15–323.15 | w(DMF) 0.1–1.0 | T too high for 298.15 K |
| 3 | 10.1021/je300608v [GLOBlit_9900] | PROPblock
</tool_result>

## Assistant
<summary>Found 5 blocks for DMF+water viscosity. Best: GLOBlit_8676 PROPblock_9 (11 pts at exactly 298.15 K). Now searching DMAc+water.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_63', 'GLOBcomp_1'], property=GLOBprop_4, system_type=binary…)</tool_call>

## User
<tool_result>
**⚠ Tool `search_blocks` result discarded by subagent.**

1. **Explanation:** The search returned 0 results for dynamic viscosity (GLOBprop_4) of GLOBcomp_63 (DMAc) + GLOBcomp_1 (water) binary system within 293.15–303.15 K. No data is available under these exact filters.

2. **Refinement suggestions:**
   - **Broaden temperature range:** Remove or widen the `temperature_range` filter (e.g., `[273.15, 373.15]`) to check if viscosity data exists at other temperatures.
   - **Remove property filter:** Search with only the two compounds and `system_type: "binary"` to see what properties are available for this pair, confirming the compound IDs are correct.
   - **Try `system_scope: "any"`:** The system may not be declared as binary explicitly; using `"any"` may capture it.
   - **Verify compound ID:** Confirm that GLOBcomp_63 is indeed N,N-dimethylacetamide by using `get_compound_details` or searching compounds again; the wrong ID would yield no results.
</tool_result>

## Assistant
<summary>No DMAc+water viscosity data found near 298.15 K. Broadening search by removing temperature filter to check if any viscosity data exists for this binary system.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_63', 'GLOBcomp_1'], property=GLOBprop_4, system_type=binary…)</tool_call>

## User
<tool_result>
**⚠ Tool `search_blocks` result discarded by subagent.**

1. **Explanation:** The search returned zero results for dynamic viscosity (`GLOBprop_4`) of the binary system `GLOBcomp_63` (N,N-dimethylacetamide) + `GLOBcomp_1` (water). No viscosity data for this pair exists under these search parameters.

2. **Refinement suggestions:**
   - **Try removing `system_scope: "declared"`** — use `system_scope: "any"` or omit it, in case the data is stored without an explicit binary declaration.
   - **Search without the property filter** (drop `property`) to see what blocks exist at all for this compound pair (`GLOBcomp_63` + `GLOBcomp_1`), then inspect which properties are available.
   - **Verify the compound ID** for N,N-dimethylacetamide — try `lookup_compound` with alternative names (e.g., "dimethylacetamide", "DMAC", CAS 127-19-5) to confirm `GLOBcomp_63` is correct.
   - **Check for kinematic viscosity** or other viscosity-related property IDs (e.g., `GLOBprop_5` or similar) that might be stored instead of dynamic viscosity.
</tool_result>

## Assistant
<summary>No DMAc+water viscosity found with declared binary scope. Trying broader search: removing property filter to see what exists for this pair, and also trying subsystem scope.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_63', 'GLOBcomp_1'], system_type=binary, system_scope=either…)</tool_call>

## User
<tool_result>
**Summary:** 20 data blocks found for the DMAc (GLOBcomp_63) + water (GLOBcomp_1) binary system across 10 DOIs, covering 9 distinct property types spanning T ≈ 278–372 K and full composition range.

### Properties available for DMAc + Water

| Property | GLOBprop | DOI | Block | Points | T range (K) | Composition range |
|---|---|---|---|---|---|---|
| Mass density, kg/m³ | GLOBprop_1 | 10.1016/j.fluid.2014.08.026 [GLOBlit_1540] | PROPblock_7 | 4 | const. | w=0.1–0.4 |
| Mass density, kg/m³ | GLOBprop_1 | 10.1016/j.jct.2005.07.012 [GLOBlit_2584] | PROPblock_10 | 112 | 288.15–293.15 | x(water)=0.0323–0.9799 |
| Mass density, kg/m³ | GLOBprop_1 | 10.1016/j.jct.2007.05.015 [GLOBlit_2834] | PROPblock_20 | 27 | const. | x(DMAc)=0–1 |
| Mass density, kg/m³ | GLOBprop_1 | 10.1016/j.jct.2012.04.007 [GLOBlit_3614] | PROPblock_5 | 55 | 278.15–318.15 | x(water)=0.00029–0.012 |
| Mass density, kg/m³ | GLOBprop_1 | 10.1016/j.jct.2014.05.003 [GLOBlit_4166] | PROPblock_3 | 3 | const. | w=0.1–0.3 |
| Relative permittivity (freq) | GLOBprop_42 | 10.1016/j.fluid.2014.08.026 [GLOBlit_1540] | PROPblock_8 | 5 | const. | w=0–0.4 |
|
</tool_result>

## Assistant
<summary>DMAc+water binary has 20 blocks but NO dynamic viscosity data in the database. Now inspecting the best DMF+water viscosity block (GLOBlit_8676::PROPblock_9, 11 pts at 298.15 K) to get actual values.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_9, literature=GLOBlit_8676)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je050209y [GLOBlit_8676] :: PROPblock_9 (binary: dimethylformamide + water)
filter: none (whole block)
block constraints: temperature_k = 298.15; pressure_kpa = 101.325

| BLKpoint_id | mole_fraction_<dimethylformamide> | temperature_k | pressure_kpa | viscosity_pa_s |
|---|---|---|---|---|
| BLKpoint_1 | 0.05 | 298.15 | 101.325 | 0.00131 |
| BLKpoint_2 | 0.1001 | 298.15 | 101.325 | 0.001728 |
| BLKpoint_3 | 0.2 | 298.15 | 101.325 | 0.002346 |
| BLKpoint_4 | 0.299 | 298.15 | 101.325 | 0.002491 |
| BLKpoint_5 | 0.3998 | 298.15 | 101.325 | 0.002273 |
| BLKpoint_6 | 0.4997 | 298.15 | 101.325 | 0.001878 |
| BLKpoint_7 | 0.5993 | 298.15 | 101.325 | 0.001532 |
| BLKpoint_8 | 0.6995 | 298.15 | 101.325 | 0.001243 |
| BLKpoint_9 | 0.8 | 298.15 | 101.325 | 0.001045 |
| BLKpoint_10 | 0.8991 | 298.15 | 101.325 | 0.000901 |
| BLKpoint_11 | 0.9488 | 298.15 | 101.325 | 0.000843 |

mode: complete — all 11 matched rows shown (block has 11)
topology: viscosity_pa_s vs mole_fraction_dimethylformamide: non-monotonic(1 extrema)
stats (matched, n=11): mole_fraction_dimethylformamide 0.05–0.9488 (n=11); temperature_k 298.15–298.15 (n=11); pressure_kpa 101.325–101.325 (n=11); viscosity_pa_s 0.000843–0.002491 (n=11)
inspection_id: INSP_469970d3baa4
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<reasoning>
I now have all the information needed to provide a complete answer:

1. DMF + water: Found viscosity data at exactly 298.15 K with 11 data points across the full composition range. The data shows a non-monotonic behavior with a maximum viscosity around x(DMF) ≈ 0.3.

2. DMAc + water: No dynamic viscosity data exists in the ThermoML database for this binary system. The database has 20 blocks for this pair covering other properties (density, permittivity, etc.) but not viscosity.

Let me compile the answer.
</reasoning>

<summary>
Complete data found for DMF+water viscosity at 298.15 K (GLOBlit_8676, PROPblock_9, 11 pts). DMAc+water has no dynamic viscosity data in the database despite 20 blocks covering other properties. Ready to assemble final answer.
</summary>

<answer>
## Dynamic Viscosity Data for DMF + Water and DMAc + Water Binary Systems near 298.15 K

### 1. N,N-Dimethylformamide (DMF) + Water

**Compound IDs:** DMF = GLOBcomp_18 (C₃H₇NO), Water = GLOBcomp_1 (H₂O)

**Best data block:** GLOBlit_8676 (DOI: 10.1021/je050209y), PROPblock_9
- **System:** binary, DMF + water
- **Data points:** 11
- **Temperature:** 298.15 K (fixed constraint)
- **Pressure:** 101.325 kPa (fixed constraint)
- **Composition variable:** mole fraction of DMF, range 0.05–0.9488

**Complete viscosity data at 298.15 K:**

| x(DMF) | Viscosity (Pa·s) |
|--------|-----------------|
| 0.05   | 0.00131         |
| 0.1001 | 0.001728        |
| 0.2    | 0.002346        |
| 0.299  | 0.002491        |
| 0.3998 | 0.002273        |
| 0.4997 | 0.001878        |
| 0.5993 | 0.001532        |
| 0.6995 | 0.001243        |
| 0.8    | 0.001045        |
| 0.8991 | 0.000901        |
| 0.9488 | 0.000843        |

**Chemistry insight:** The viscosity shows a clear non-monotonic dependence on composition with a single maximum near x(DMF) ≈ 0.3 (viscosity = 0.002491 Pa·s). This is characteristic of strong intermolecular interactions (hydrogen bonding) between DMF and water. The maximum viscosity is roughly 2.8× the value at the DMF-rich end (0.000843 Pa·s at x = 0.9488), indicating significant structural reorganization in the water-rich to intermediate composition region.

**Additional blocks found (different temperature ranges):**
- GLOBlit_11030 (DOI: 10.1021/je300608v), PROPblock_3 — 98 data points, T: 293.15–323.15 K, full composition range
- GLOBlit_8676, PROPblock_10 — 11 data points at 303.15 K
- GLOBlit_9342 (DOI: 10.1021/je1008813), PROPblock_3 — 16 points, T: 308.15–323.15 K (above 298.15 K)

### 2. N,N-Dimethylacetamide (DMAc) + Water

**Compound IDs:** DMAc = GLOBcomp_63 (C₄H₉NO, N,N-dimethylethanamide), Water = GLOBcomp_1

**Result: No dynamic viscosity data found** in the ThermoML database for this binary system. A comprehensive search (with and without temperature filters, using both declared and subsystem scopes) returned zero viscosity blocks.

The database does contain 20 data blocks for DMAc + water covering other properties including mass density (GLOBprop_1), relative permittivity, speed of sound, excess molar volume, and others — but dynamic viscosity (GLOBprop_4) is not among them.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** PROPblock_9: 2.8 (near '…ng) between DMF and water. The maximum viscosity is roughly …') matches no inspected row/stat, database table, or other source of PROPblock_9
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_9", literature="<GLOBlit_N or DOI>", nearest={"column": "mole_fraction_<dimethylformamide>", "value": 2.8})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNINSPECTED_BLOCK** PROPblock_3: PROPblock_3 is quoted with data values (98, 293.15, 323.15, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_10: PROPblock_10 is quoted with data values (303.15, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_10", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_3: PROPblock_3 is quoted with data values (16, 308.15, 323.15, 298.15, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>")`
Inspected so far: PROPblock_9

Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_9: 298.15, 101.325, 0.05, 0.9488, 0.00131, 0.1001, 0.001728, 0.2, 0.002346, 0.299, 0.002491, 0.3998, 0.002273, 0.4997, 0.001878, 0.5993, 0.001532, 0.6995, 0.001243, 0.8, 0.001045, 0.8991, 0.000901, 0.000843, 0.3

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## Assistant


<reasoning>
The grounding check flagged several issues:

1. "2.8×" - This is a computed ratio (0.002491/0.000843 ≈ 2.96), not a database value. I should label it as derived.

2. PROPblock_3 (GLOBlit_11030), PROPblock_10 (GLOBlit_8676), PROPblock_3 (GLOBlit_9342) - These blocks are mentioned with data values from the search_blocks summary but were never inspected. I should either inspect them or remove the specific numerical values.

Since I'm limited on tool calls and these are just "additional blocks found" context from the search_blocks results (not data I'm quoting as viscosity measurements), I should remove the specific numerical values for uninspected blocks and just mention them qualitatively, or inspect them.

Actually, the values like "98 data points", "293.15–323.15 K" etc. came from the search_blocks tool result, not from inspect_block_table. The grounding rules say I need to inspect blocks before quoting data values from them. Let me just remove those specific numbers and describe them without numerical details, or inspect them.

Given efficiency, I'll just remove the numerical details for the uninspected blocks and label the "2.8×" as a derived calculation.
</reasoning>

<summary>
Fixing grounding issues: labeling the 2.8× ratio as derived from inspected data, and removing specific numerical values for uninspected blocks (PROPblock_3/GLOBlit_11030, PROPblock_10/GLOBlit_8676, PROPblock_3/GLOBlit_9342). Keeping all verified PROPblock_9 data intact.
</summary>

<answer>
## Dynamic Viscosity Data for DMF + Water and DMAc + Water Binary Systems near 298.15 K

### 1. N,N-Dimethylformamide (DMF) + Water

**Compound IDs:** DMF = GLOBcomp_18 (C₃H₇NO), Water = GLOBcomp_1 (H₂O)

**Best data block:** GLOBlit_8676 (DOI: 10.1021/je050209y), PROPblock_9
- **System:** binary, DMF + water
- **Data points:** 11
- **Temperature:** 298.15 K (fixed constraint)
- **Pressure:** 101.325 kPa (fixed constraint)
- **Composition variable:** mole fraction of DMF, range 0.05–0.9488

**Complete viscosity data at 298.15 K:**

| x(DMF) | Viscosity (Pa·s) |
|--------|-----------------|
| 0.05   | 0.00131         |
| 0.1001 | 0.001728        |
| 0.2    | 0.002346        |
| 0.299  | 0.002491        |
| 0.3998 | 0.002273        |
| 0.4997 | 0.001878        |
| 0.5993 | 0.001532        |
| 0.6995 | 0.001243        |
| 0.8    | 0.001045        |
| 0.8991 | 0.000901        |
| 0.9488 | 0.000843        |

**Chemistry insight:** The viscosity shows a clear non-monotonic dependence on composition with a single maximum near x(DMF) ≈ 0.3 (viscosity = 0.002491 Pa·s). This is characteristic of strong intermolecular interactions (hydrogen bonding) between DMF and water. The maximum viscosity is roughly 3.0× the value at the DMF-rich end (0.000843 Pa·s at x = 0.9488) — this ratio is derived by dividing the two inspected values (0.002491 / 0.000843 ≈ 2.96). This indicates significant structural reorganization in the water-rich to intermediate composition region.

**Additional blocks found (not inspected in this run):**
- GLOBlit_11030 (DOI: 10.1021/je300608v), PROPblock_3 — covers a range of temperatures and compositions
- GLOBlit_8676, PROPblock_10 — additional isothermal data at a different temperature
- GLOBlit_9342 (DOI: 10.1021/je1008813), PROPblock_3 — data at temperatures above 298.15 K

### 2. N,N-Dimethylacetamide (DMAc) + Water

**Compound IDs:** DMAc = GLOBcomp_63 (C₄H₉NO, N,N-dimethylethanamide), Water = GLOBcomp_1

**Result: No dynamic viscosity data found** in the ThermoML database for this binary system. A comprehensive search (with and without temperature filters, using both declared and subsystem scopes) returned zero viscosity blocks.

The database does contain data blocks for DMAc + water covering other properties including mass density (GLOBprop_1), relative permittivity, speed of sound, excess molar volume, and others — but dynamic viscosity (GLOBprop_4) is not among them.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** PROPblock_9: 2.96 (near '…by dividing the two inspected values (0.002491 / 0.000843 ≈ …') matches no inspected row/stat, database table, or other source of PROPblock_9
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_9", literature="<GLOBlit_N or DOI>", nearest={"column": "mole_fraction_<dimethylformamide>", "value": 2.96})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNINSPECTED_BLOCK** PROPblock_3: PROPblock_3 is quoted with data values (298.15, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>")`
Inspected so far: PROPblock_9

Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_9: 298.15, 101.325, 0.05, 0.9488, 0.00131, 0.1001, 0.001728, 0.2, 0.002346, 0.299, 0.002491, 0.3998, 0.002273, 0.4997, 0.001878, 0.5993, 0.001532, 0.6995, 0.001243, 0.8, 0.001045, 0.8991, 0.000901, 0.000843, 0.3, 3.0

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

NOTE: 1 tool-call block(s) on turn(s) 1 were rejected for malformed syntax and NEVER EXECUTED — no result exists for them. Repair the answer from executed tool results only; do not quote anything you 'remember' from those rejected turns.

## LLM Response


<reasoning>
Two remaining issues:

1. "2.96" is flagged as UNGROUNDED_LITERAL for PROPblock_9. It's a computed ratio (0.002491/0.000843). I already labeled it as derived but the "≈ 2.96" is still being flagged. I need to make it clearer that this is a computed value, not a database datum. The "3.0×" is verified. I'll just remove the "≈ 2.96" parenthetical.

2. PROPblock_3 (GLOBlit_9342) is flagged because "298.15" appears in the phrase "data at temperatures above 298.15 K". This "298.15" is not a data value from that block - it's a reference temperature from the question. I need to rephrase to avoid associating that number with PROPblock_3.

Let me fix both surgically.
</reasoning>

<summary>
Fixing two remaining issues: (1) removing the "≈ 2.96" computed ratio literal that keeps getting flagged, keeping the already-verified "3.0×"; (2) rephrasing the PROPblock_3/GLOBlit_9342 mention to avoid associating "298.15" with that uninspected block.
</summary>

<answer>
## Dynamic Viscosity Data for DMF + Water and DMAc + Water Binary Systems near 298.15 K

### 1. N,N-Dimethylformamide (DMF) + Water

**Compound IDs:** DMF = GLOBcomp_18 (C₃H₇NO), Water = GLOBcomp_1 (H₂O)

**Best data block:** GLOBlit_8676 (DOI: 10.1021/je050209y), PROPblock_9
- **System:** binary, DMF + water
- **Data points:** 11
- **Temperature:** 298.15 K (fixed constraint)
- **Pressure:** 101.325 kPa (fixed constraint)
- **Composition variable:** mole fraction of DMF, range 0.05–0.9488

**Complete viscosity data at 298.15 K:**

| x(DMF) | Viscosity (Pa·s) |
|--------|-----------------|
| 0.05   | 0.00131         |
| 0.1001 | 0.001728        |
| 0.2    | 0.002346        |
| 0.299  | 0.002491        |
| 0.3998 | 0.002273        |
| 0.4997 | 0.001878        |
| 0.5993 | 0.001532        |
| 0.6995 | 0.001243        |
| 0.8    | 0.001045        |
| 0.8991 | 0.000901        |
| 0.9488 | 0.000843        |

**Chemistry insight:** The viscosity shows a clear non-monotonic dependence on composition with a single maximum near x(DMF) ≈ 0.3 (viscosity = 0.002491 Pa·s). This is characteristic of strong intermolecular interactions (hydrogen bonding) between DMF and water. The maximum viscosity is roughly 3.0× the value at the DMF-rich end (0.000843 Pa·s at x = 0.9488) — this ratio is derived by dividing the two inspected values. This indicates significant structural reorganization in the water-rich to intermediate composition region.

**Additional blocks found (not inspected in this run):**
- GLOBlit_11030 (DOI: 10.1021/je300608v), PROPblock_3 — covers a range of temperatures and compositions
- GLOBlit_8676, PROPblock_10 — additional isothermal data at a different temperature
- GLOBlit_9342 (DOI: 10.1021/je1008813), PROPblock_3 — data at elevated temperatures

### 2. N,N-Dimethylacetamide (DMAc) + Water

**Compound IDs:** DMAc = GLOBcomp_63 (C₄H₉NO, N,N-dimethylethanamide), Water = GLOBcomp_1

**Result: No dynamic viscosity data found** in the ThermoML database for this binary system. A comprehensive search (with and without temperature filters, using both declared and subsystem scopes) returned zero viscosity blocks.

The database does contain data blocks for DMAc + water covering other properties including mass density (GLOBprop_1), relative permittivity, speed of sound, excess molar volume, and others — but dynamic viscosity (GLOBprop_4) is not among them.
</answer>