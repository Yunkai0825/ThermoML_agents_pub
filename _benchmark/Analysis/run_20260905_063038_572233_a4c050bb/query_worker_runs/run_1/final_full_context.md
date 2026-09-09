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
Find density data blocks for binary mixture of ethanol and water at or near 310 K

## Instruction
Search for blocks containing mass density (GLOBprop_1) data for binary mixtures of ethanol (C2H5OH / CAS 64-17-5) and water (H2O / CAS 7732-18-5). I need data that covers temperatures near 310 K and spans a wide composition range (ideally full 0-1 mole fraction). Return DOIs, block numbers, temperature ranges, composition ranges, and number of data points.

## ID Catalog (from working memory)
[]

## Assistant
<summary>Resolving compound IDs for ethanol and water, and property ID for mass density to search for binary mixture density data near 310 K.</summary>
<tool_call>resolve_compound_ids(queries=['ethanol', 'water'])</tool_call>

## User
<tool_result>
Both compounds resolved with exact name matches at 100% confidence.

| Compound | GLOBcomp ID | Formula | SMILES |
|----------|-------------|---------|--------|
| ethanol  | GLOBcomp_2  | C2H6O   | CCO    |
| water    | GLOBcomp_1  | H2O     | O      |
</tool_result>

## Assistant
<summary>Resolved: ethanol=GLOBcomp_2, water=GLOBcomp_1. Property mass density=GLOBprop_1. Now searching for binary mixture blocks near 310 K.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_2', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
(validation blocked search_blocks earlier — corrected)
</tool_result>

## Assistant
<summary>Fixing temperature_range argument format to list of floats [305, 315] and re-searching for binary ethanol+water density blocks near 310 K.</summary>
<tool_call>search_blocks(compound=['GLOBcomp_2', 'GLOBcomp_1'], property=GLOBprop_1, system_type=binary,…)</tool_call>

## User
<tool_result>
**Summary:** 16 binary ethanol–water mass density blocks found in the 305–315 K window. The most useful for wide composition coverage near 310 K are highlighted below.

**Top candidates (wide composition + T near 310 K):**

| DOI | Block | GLOBlit | Pts | T range (K) | Composition range | ρ range (kg/m³) | Comp. variable |
|-----|-------|---------|-----|-------------|-------------------|-----------------|----------------|
| 10.1021/je020173z | PROPblock_5 | GLOBlit_8050 | 24 (16 kept) | 298.15–313.15 | w(ethanol) 0.10835–0.71144 | 848.29–979.29 | GLOBvar_5 |
| 10.1021/je600565m | PROPblock_6 | GLOBlit_10699 | 18 (13 kept) | 298.15–318.15 | x(water) 0.0998–0.9051 | 780.53–965.51 | GLOBvar_2 |
| 10.1021/je800150h | PROPblock_9 | GLOBlit_11136 | 108 (15 kept) | 268.1–323.15 | x(water) 0.1–0.5 | 774.3–886.6 | GLOBvar_2 |
| 10.1021/je900743e | PROPblock_3 | GLOBlit_11792 | 15 | 293.15–313.15 | w(ethanol) 0.1–0.5 | 897.6–981.8 | GLOBvar_5 |
| 10.1021/je800942u | PROPblock_6 | GLOBlit_11459 | 18 (14 kept) | 303.15–328.15 | w(water) 0.15–0.25 | 796.9–848.8 | GLOBvar_5 |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | GLOBlit_7085 | 12 | 298.15–313.15 | w(ethanol) 0.04–0.16 | 966.4–990.13 | GLOBvar_5 |
| 10.1021/je4003515 | PROPblock_7 | GLOBlit_10159 | 23 (14 kept) | 293.15–313.15 | b(ethanol) 14–22 | 901.281–936.706 | GLOBvar_4 |
| 10.1021/je900064e | PROPblock_6 | GLOBlit_11504 | 10 (8 kept) | 288.15–323.15 | fixed vol. fraction | 903.71–930.86 | GLOBvar_1 only |

**Best picks for wide composition near 310 K:**
- **10.1021/je600565m [GLOBlit_10699] / PROPblock_6** — widest mole fraction range (x_water 0.0998–0.9051), T up to 318.15 K
- **10.1021/je020173z [GLOBlit_8050] / PROPblock_5** — wide weight fraction (w_ethanol 0.108–0.711), T up to 313.15 K
- **10.1021/je800150h [GLOBlit_11136] / PROPblock_9** — 108 original pts, broad T range covering 310 K, x(water) 0.1–0.5
</tool_result>

## Assistant
<reasoning>
I have comprehensive results for binary ethanol-water density blocks near 310 K. Let me compile the answer with all the relevant information from the tool results.
</reasoning>

<answer>
## Density Data for Binary Ethanol–Water Mixtures near 310 K

Sixteen binary ethanol–water mass density (GLOBprop_1) blocks were found in the 305–315 K temperature window. The most useful candidates for wide composition coverage near 310 K are summarized below:

### Top Candidates

| DOI | Block | GLOBlit | Points | T range (K) | Composition range | ρ range (kg/m³) | Comp. variable |
|-----|-------|---------|--------|-------------|-------------------|-----------------|----------------|
| 10.1021/je600565m | PROPblock_6 | GLOBlit_10699 | 18 (13 kept) | 298.15–318.15 | x(water) 0.0998–0.9051 | 780.53–965.51 | GLOBvar_2 (mole fraction) |
| 10.1021/je020173z | PROPblock_5 | GLOBlit_8050 | 24 (16 kept) | 298.15–313.15 | w(ethanol) 0.10835–0.71144 | 848.29–979.29 | GLOBvar_5 (mass fraction) |
| 10.1021/je800150h | PROPblock_9 | GLOBlit_11136 | 108 (15 kept) | 268.1–323.15 | x(water) 0.1–0.5 | 774.3–886.6 | GLOBvar_2 (mole fraction) |
| 10.1021/je900743e | PROPblock_3 | GLOBlit_11792 | 15 | 293.15–313.15 | w(ethanol) 0.1–0.5 | 897.6–981.8 | GLOBvar_5 (mass fraction) |
| 10.1021/je800942u | PROPblock_6 | GLOBlit_11459 | 18 (14 kept) | 303.15–328.15 | w(water) 0.15–0.25 | 796.9–848.8 | GLOBvar_5 (mass fraction) |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | GLOBlit_7085 | 12 | 298.15–313.15 | w(ethanol) 0.04–0.16 | 966.4–990.13 | GLOBvar_5 (mass fraction) |
| 10.1021/je4003515 | PROPblock_7 | GLOBlit_10159 | 23 (14 kept) | 293.15–313.15 | b(ethanol) 14–22 | 901.281–936.706 | GLOBvar_4 (molality) |
| 10.1021/je900064e | PROPblock_6 | GLOBlit_11504 | 10 (8 kept) | 288.15–323.15 | fixed vol. fraction | 903.71–930.86 | GLOBvar_1 (volume fraction) |

### Best Picks

1. **GLOBlit_10699 / PROPblock_6** (DOI: 10.1021/je600565m) — **Widest mole-fraction range**: x(water) from 0.0998 to 0.9051, covering nearly the full composition range. Temperature extends to 318.15 K, comfortably bracketing 310 K. 18 data points (13 in the T window).

2. **GLOBlit_8050 / PROPblock_5** (DOI: 10.1021/je020173z) — **Wide mass-fraction range**: w(ethanol) from 0.108 to 0.711, T up to 313.15 K. 24 data points (16 in the T window).

3. **GLOBlit_11136 / PROPblock_9** (DOI: 10.1021/je800150h) — **Largest dataset**: 108 original data points across a broad T range (268.1–323.15 K), though composition coverage is limited to x(water) 0.1–0.5 (ethanol-rich side).

### Resolved IDs
- Ethanol: GLOBcomp_2 (C₂H₆O, CCO)
- Water: GLOBcomp_1 (H₂O)
- Mass density: GLOBprop_1

The GLOBlit_10699 block is the strongest candidate for a full composition sweep near 310 K, while GLOBlit_11136 offers the most data points if the ethanol-rich half of the composition range is sufficient.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_BLOCK** PROPblock_6 + PROPblock_5 + PROPblock_9 + PROPblock_3 + PROPblock_7: PROPblock_6 + PROPblock_5 + PROPblock_9 + PROPblock_3 + PROPblock_7 is quoted with data values (18, 13, 298.15, 318.15, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_6", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_5", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_9", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_3", literature="<GLOBlit_N or DOI>"); inspect_block_table(block_number="PROPblock_7", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_6: PROPblock_6 is quoted with data values (0.0998, 0.9051, 318.15, 310, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_6", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_5: PROPblock_5 is quoted with data values (0.108, 0.711, 313.15, 24, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_5", literature="<GLOBlit_N or DOI>")`
- **UNINSPECTED_BLOCK** PROPblock_9: PROPblock_9 is quoted with data values (108, 268.1, 323.15, 0.1, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_9", literature="<GLOBlit_N or DOI>")`

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## Assistant
<summary>Running inspect_block_table on the top 5 candidate blocks to ground all quoted data values from the search results.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_6, literature=GLOBlit_10699)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je600565m [GLOBlit_10699] :: PROPblock_6 (binary: ethanol + water)
filter: none (whole block)
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mole_fraction_<water> | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 0.0998 | 101.0 | 797.6 |
| BLKpoint_2 | 298.15 | 0.2018 | 101.0 | 810.78 |
| BLKpoint_3 | 298.15 | 0.3085 | 101.0 | 826.73 |
| BLKpoint_4 | 298.15 | 0.4145 | 101.0 | 843.26 |
| BLKpoint_5 | 298.15 | 0.5001 | 101.0 | 858.65 |
| BLKpoint_7 | 298.15 | 0.7005 | 101.0 | 904.69 |
| BLKpoint_9 | 298.15 | 0.9051 | 101.0 | 965.51 |
| BLKpoint_10 | 318.15 | 0.1 | 101.0 | 780.53 |
| BLKpoint_12 | 318.15 | 0.3001 | 101.0 | 807.71 |
| BLKpoint_14 | 318.15 | 0.5003 | 101.0 | 840.31 |
| BLKpoint_16 | 318.15 | 0.7001 | 101.0 | 888.76 |
| BLKpoint_17 | 318.15 | 0.8001 | 101.0 | 919.19 |
| BLKpoint_18 | 318.15 | 0.9 | 101.0 | 952.47 |

mode: RDP — 13 of 18 matched rows shown (shape-preserving; block has 18). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=18): temperature_k 298.15–318.15 (n=18); mole_fraction_water 0.0998–0.9051 (n=18); pressure_kpa 101.0–101.0 (n=18); mass_density_kg_m3 780.53–965.51 (n=18)
inspection_id: INSP_222b8f50d354
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_10699/PROPblock_6: 18 pts, T 298.15–318.15 K, x(water) 0.0998–0.9051, ρ 780.53–965.51 kg/m³. Now inspecting the other 4 blocks.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_5, literature=GLOBlit_8050)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je020173z [GLOBlit_8050] :: PROPblock_5 (binary: ethanol + water)
filter: none (whole block)
block constraints: pressure_kpa = 101.3

| BLKpoint_id | temperature_k | mass_fraction_<ethanol> | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 0.10835 | 101.3 | 979.29 |
| BLKpoint_4 | 298.15 | 0.29072 | 101.3 | 952.58 |
| BLKpoint_5 | 298.15 | 0.37367 | 101.3 | 937.25 |
| BLKpoint_6 | 298.15 | 0.37505 | 101.3 | 936.69 |
| BLKpoint_7 | 298.15 | 0.44319 | 101.3 | 922.6 |
| BLKpoint_8 | 298.15 | 0.44452 | 101.3 | 922.55 |
| BLKpoint_9 | 298.15 | 0.49979 | 101.3 | 910.43 |
| BLKpoint_10 | 298.15 | 0.50494 | 101.3 | 908.96 |
| BLKpoint_12 | 298.15 | 0.62751 | 101.3 | 880.81 |
| BLKpoint_13 | 313.15 | 0.16716 | 101.3 | 964.04 |
| BLKpoint_14 | 313.15 | 0.28575 | 101.3 | 943.6 |
| BLKpoint_16 | 313.15 | 0.35254 | 101.3 | 930.27 |
| BLKpoint_18 | 313.15 | 0.44202 | 101.3 | 911.19 |
| BLKpoint_19 | 313.15 | 0.44449 | 101.3 | 910.92 |
| BLKpoint_23 | 313.15 | 0.62707 | 101.3 | 868.41 |
| BLKpoint_24 | 313.15 | 0.71144 | 101.3 | 848.29 |

mode: RDP — 16 of 24 matched rows shown (shape-preserving; block has 24). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=24): temperature_k 298.15–313.15 (n=24); mass_fraction_ethanol 0.10835–0.71144 (n=24); pressure_kpa 101.3–101.3 (n=24); mass_density_kg_m3 848.29–979.29 (n=24)
inspection_id: INSP_1e3a753d7d42
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected GLOBlit_8050/PROPblock_5: 24 pts, T 298.15–313.15 K, w(ethanol) 0.10835–0.71144, ρ 848.29–979.29 kg/m³. Now inspecting remaining 3 blocks.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_9, literature=GLOBlit_11136)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je800150h [GLOBlit_11136] :: PROPblock_9 (binary: ethanol + water)
filter: none (whole block)
block constraints: pressure_kpa = 101.0

| BLKpoint_id | mole_fraction_<water> | temperature_k | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 0.1 | 268.1 | 101.0 | 824.9 |
| BLKpoint_12 | 0.1 | 323.15 | 101.0 | 774.3 |
| BLKpoint_13 | 0.2 | 268.1 | 101.0 | 838.2 |
| BLKpoint_24 | 0.2 | 323.15 | 101.0 | 787.5 |
| BLKpoint_25 | 0.3 | 268.1 | 101.0 | 852.2 |
| BLKpoint_36 | 0.3 | 323.15 | 101.0 | 801.9 |
| BLKpoint_37 | 0.4 | 268.1 | 101.0 | 867.7 |
| BLKpoint_48 | 0.4 | 323.15 | 101.0 | 817.7 |
| BLKpoint_49 | 0.5 | 268.1 | 101.0 | 886.6 |
| BLKpoint_60 | 0.5 | 323.15 | 101.0 | 835.8 |
| BLKpoint_61 | 0.6 | 268.1 | 101.0 | 908.1 |
| BLKpoint_72 | 0.6 | 323.15 | 101.0 | 857.3 |
| BLKpoint_73 | 0.7 | 268.1 | 101.0 | 931.6 |
| BLKpoint_84 | 0.7 | 323.15 | 101.0 | 883 |
| BLKpoint_85 | 0.8 | 268.1 | 101.0 | 951 |
| BLKpoint_96 | 0.8 | 323.15 | 101.0 | 911.2 |
| BLKpoint_97 | 0.9 | 268.1 | 101.0 | 977.3 |
| BLKpoint_108 | 0.9 | 323.15 | 101.0 | 942 |

mode: RDP — 18 of 108 matched rows shown (shape-preserving; block has 108). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=108): mole_fraction_water 0.1–0.9 (n=108); temperature_k 268.1–323.15 (n=108); pressure_kpa 101.0–101.0 (n=108); mass_density_kg_m3 774.3–977.3 (n=108)
inspection_id: INSP_5d3a3a494c0a
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected 3 of 5 flagged blocks. Now inspecting GLOBlit_11792/PROPblock_3 and GLOBlit_7085/PROPblock_7 to complete grounding.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_3, literature=GLOBlit_11792)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/je900743e [GLOBlit_11792] :: PROPblock_3 (binary: ethanol + water)
filter: none (whole block)
block constraints: pressure_kpa = 101.0

| BLKpoint_id | temperature_k | mass_fraction_<ethanol> | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 293.15 | 0.1 | 101.0 | 981.8 |
| BLKpoint_2 | 293.15 | 0.2 | 101.0 | 968.2 |
| BLKpoint_3 | 293.15 | 0.3 | 101.0 | 953.6 |
| BLKpoint_4 | 293.15 | 0.4 | 101.0 | 935.5 |
| BLKpoint_5 | 293.15 | 0.5 | 101.0 | 913.9 |
| BLKpoint_6 | 303.15 | 0.1 | 101.0 | 979 |
| BLKpoint_7 | 303.15 | 0.2 | 101.0 | 964.1 |
| BLKpoint_8 | 303.15 | 0.3 | 101.0 | 947.4 |
| BLKpoint_9 | 303.15 | 0.4 | 101.0 | 927.2 |
| BLKpoint_10 | 303.15 | 0.5 | 101.0 | 905.6 |
| BLKpoint_11 | 313.15 | 0.1 | 101.0 | 974.6 |
| BLKpoint_12 | 313.15 | 0.2 | 101.0 | 958.7 |
| BLKpoint_13 | 313.15 | 0.3 | 101.0 | 940.3 |
| BLKpoint_14 | 313.15 | 0.4 | 101.0 | 919.8 |
| BLKpoint_15 | 313.15 | 0.5 | 101.0 | 897.6 |

mode: RDP — 15 of 15 matched rows shown (shape-preserving; block has 15). Quote ONLY shown rows or the stats line; narrow `where` for other rows.
stats (matched, n=15): temperature_k 293.15–313.15 (n=15); mass_fraction_ethanol 0.1–0.5 (n=15); pressure_kpa 101.0–101.0 (n=15); mass_density_kg_m3 897.6–981.8 (n=15)
inspection_id: INSP_5cbf22ac92af
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<summary>Inspected 4 of 5 blocks. Now inspecting the last flagged block: GLOBlit_7085/PROPblock_7.</summary>
<tool_call>inspect_block_table(block_number=PROPblock_7, literature=GLOBlit_7085)</tool_call>

## User
<tool_result>
**Data inspection** — 10.1021/acs.jced.6b01058 [GLOBlit_7085] :: PROPblock_7 (binary: ethanol + water)
filter: none (whole block)
block constraints: pressure_kpa = 85.0

| BLKpoint_id | temperature_k | mass_fraction_<ethanol> | pressure_kpa | mass_density_kg_m3 |
|---|---|---|---|---|
| BLKpoint_1 | 298.15 | 0.04 | 85.0 | 990.13 |
| BLKpoint_2 | 303.15 | 0.04 | 85.0 | 988.79 |
| BLKpoint_3 | 308.15 | 0.04 | 85.0 | 987.24 |
| BLKpoint_4 | 313.15 | 0.04 | 85.0 | 985.42 |
| BLKpoint_5 | 298.15 | 0.08 | 85.0 | 983.9 |
| BLKpoint_6 | 303.15 | 0.08 | 85.0 | 982.43 |
| BLKpoint_7 | 308.15 | 0.08 | 85.0 | 980.77 |
| BLKpoint_8 | 313.15 | 0.08 | 85.0 | 978.85 |
| BLKpoint_9 | 298.15 | 0.16 | 85.0 | 972.57 |
| BLKpoint_10 | 303.15 | 0.16 | 85.0 | 970.69 |
| BLKpoint_11 | 308.15 | 0.16 | 85.0 | 968.6 |
| BLKpoint_12 | 313.15 | 0.16 | 85.0 | 966.4 |

mode: complete — all 12 matched rows shown (block has 12)
stats (matched, n=12): temperature_k 298.15–313.15 (n=12); mass_fraction_ethanol 0.04–0.16 (n=12); pressure_kpa 85.0–85.0 (n=12); mass_density_kg_m3 966.4–990.13 (n=12)
inspection_id: INSP_d9f5b67c278b
Data points may be quoted ONLY verbatim from the table above or the stats lines.
</tool_result>

## Assistant
<reasoning>
All 5 flagged blocks have now been inspected. Let me also note that the original search returned additional blocks (GLOBlit_11459/PROPblock_6, GLOBlit_10159/PROPblock_7, GLOBlit_11504/PROPblock_6) but those were not flagged. I should now compile the answer using only inspected/verified data.

Key corrections from inspections:
- GLOBlit_10699/PROPblock_6: 18 pts total, 13 shown (RDP). T 298.15–318.15 K, x(water) 0.0998–0.9051, ρ 780.53–965.51 kg/m³. Confirmed.
- GLOBlit_8050/PROPblock_5: 24 pts total, 16 shown (RDP). T 298.15–313.15 K, w(ethanol) 0.10835–0.71144, ρ 848.29–979.29 kg/m³. Confirmed.
- GLOBlit_11136/PROPblock_9: 108 pts total, 18 shown (RDP). T 268.1–323.15 K, x(water) 0.1–0.9, ρ 774.3–977.3 kg/m³. Note: the stats show x(water) 0.1–0.9, not 0.1–0.5 as the search summary said. The search summary was filtered to the 305-315 K window showing 15 kept points with x(water) 0.1–0.5, but the full block covers 0.1–0.9. I should report the full block stats from the inspection.
- GLOBlit_11792/PROPblock_3: 15 pts total. T 293.15–313.15 K, w(ethanol) 0.1–0.5, ρ 897.6–981.8 kg/m³. Confirmed.
- GLOBlit_7085/PROPblock_7: 12 pts total. T 298.15–313.15 K, w(ethanol) 0.04–0.16, ρ 966.4–990.13 kg/m³. Confirmed. Note: pressure is 85.0 kPa, not 101 kPa.

I need to correct the earlier statement about GLOBlit_11136 composition range - the full block covers x(water) 0.1–0.9, which is actually wider than I initially reported.
</reasoning>

<answer>
## Density Data for Binary Ethanol–Water Mixtures near 310 K

Sixteen binary ethanol–water mass density (GLOBprop_1) blocks were found in the 305–315 K temperature window. The five most useful candidates, all verified by inspection, are summarized below.

### Inspected Candidates

| DOI | Block | GLOBlit | Total Points | T range (K) | Composition range | ρ range (kg/m³) | Pressure (kPa) | Comp. variable |
|-----|-------|---------|--------------|-------------|-------------------|-----------------|-----------------|----------------|
| 10.1021/je600565m | PROPblock_6 | GLOBlit_10699 | 18 | 298.15–318.15 | x(water) 0.0998–0.9051 | 780.53–965.51 | 101.0 | GLOBvar_2 (mole fraction) |
| 10.1021/je800150h | PROPblock_9 | GLOBlit_11136 | 108 | 268.1–323.15 | x(water) 0.1–0.9 | 774.3–977.3 | 101.0 | GLOBvar_2 (mole fraction) |
| 10.1021/je020173z | PROPblock_5 | GLOBlit_8050 | 24 | 298.15–313.15 | w(ethanol) 0.10835–0.71144 | 848.29–979.29 | 101.3 | GLOBvar_5 (mass fraction) |
| 10.1021/je900743e | PROPblock_3 | GLOBlit_11792 | 15 | 293.15–313.15 | w(ethanol) 0.1–0.5 | 897.6–981.8 | 101.0 | GLOBvar_5 (mass fraction) |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | GLOBlit_7085 | 12 | 298.15–313.15 | w(ethanol) 0.04–0.16 | 966.4–990.13 | 85.0 | GLOBvar_5 (mass fraction) |

### Best Picks for Wide Composition near 310 K

1. **GLOBlit_11136 / PROPblock_9** (DOI: 10.1021/je800150h) — **Largest dataset with wide composition**: 108 data points spanning x(water) 0.1–0.9 across T = 268.1–323.15 K at 101.0 kPa. This block covers nearly the full composition range and a broad temperature window that well brackets 310 K. Representative inspected points at the temperature extremes:
   - x(water) = 0.1: ρ = 824.9 kg/m³ (268.1 K) to 774.3 kg/m³ (323.15 K)
   - x(water) = 0.9: ρ = 977.3 kg/m³ (268.1 K) to 942 kg/m³ (323.15 K)

2. **GLOBlit_10699 / PROPblock_6** (DOI: 10.1021/je600565m) — **Widest mole-fraction range at two temperatures**: 18 points at x(water) 0.0998–0.9051, measured at 298.15 K and 318.15 K (101.0 kPa). Representative inspected points at 318.15 K (closest to 310 K):
   - x(water) = 0.1: ρ = 780.53 kg/m³
   - x(water) = 0.5003: ρ = 840.31 kg/m³
   - x(water) = 0.9: ρ = 952.47 kg/m³

3. **GLOBlit_8050 / PROPblock_5** (DOI: 10.1021/je020173z) — **Wide mass-fraction range**: 24 points with w(ethanol) 0.10835–0.71144 at 298.15 K and 313.15 K (101.3 kPa). At 313.15 K:
   - w(ethanol) = 0.16716: ρ = 964.04 kg/m³
   - w(ethanol) = 0.44202: ρ = 911.19 kg/m³
   - w(ethanol) = 0.71144: ρ = 848.29 kg/m³

4. **GLOBlit_11792 / PROPblock_3** (DOI: 10.1021/je900743e) — 15 points at w(ethanol) 0.1–0.5 across 293.15–313.15 K (101.0 kPa). At 313.15 K:
   - w(ethanol) = 0.1: ρ = 974.6 kg/m³
   - w(ethanol) = 0.5: ρ = 897.6 kg/m³

5. **GLOBlit_7085 / PROPblock_7** (DOI: 10.1021/acs.jced.6b01058) — 12 points but narrow composition (w(ethanol) 0.04–0.16) at 298.15–313.15 K. Note: measured at 85.0 kPa rather than atmospheric pressure. At 308.15 K (nearest to 310 K):
   - w(ethanol) = 0.04: ρ = 987.24 kg/m³
   - w(ethanol) = 0.16: ρ = 968.6 kg/m³

### Resolved IDs
- Ethanol: GLOBcomp_2 (C₂H₆O)
- Water: GLOBcomp_1 (H₂O)
- Mass density: GLOBprop_1

The GLOBlit_11136 block is the strongest overall candidate, offering 108 data points across x(water) 0.1–0.9 and a temperature range (268.1–323.15 K) that densely brackets 310 K. GLOBlit_10699 provides the widest single-isotherm composition sweep (x(water) 0.0998–0.9051) but at only two temperatures.
</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNGROUNDED_LITERAL** PROPblock_7: 310 (near '…### Best Picks for Wide Composition near 310 K  1. **  /…') matches no inspected row/stat, database table, or other source of PROPblock_7
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_7", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 310.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_9: 310 (near '…ion range and a broad temperature window that well brackets …') matches no inspected row/stat, database table, or other source of PROPblock_9
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_9", literature="<GLOBlit_N or DOI>", nearest={"column": "mole_fraction_<water>", "value": 310.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_6: 310 (near '…a). Representative inspected points at 318.15 K (closest to …') matches no inspected row/stat, database table, or other source of PROPblock_6
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_6", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 310.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** PROPblock_7: 310 (near '…a rather than atmospheric pressure. At 308.15 K (nearest to …') matches no inspected row/stat, database table, or other source of PROPblock_7
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_7", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 310.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **AMBIGUOUS_VALUE** PROPblock_7: 108 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_7", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 108.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **MISATTRIBUTED_VALUE** PROPblock_7: 268.1 does not belong to PROPblock_7; it matches only GLOBlit_11136::PROPblock_9 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 268.1 to GLOBlit_11136::PROPblock_9 — no new tool call needed`
- **MISATTRIBUTED_VALUE** PROPblock_7: 323.15 does not belong to PROPblock_7; it matches only GLOBlit_11136::PROPblock_9 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 323.15 to GLOBlit_11136::PROPblock_9 — no new tool call needed`
- **UNGROUNDED_LITERAL** PROPblock_7: 310 (near '…a temperature range (268.1–323.15 K) that densely brackets 3…') matches no inspected row/stat, database table, or other source of PROPblock_7
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_7", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 310.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- … and 2 more of the same kinds — PROPblock_7: 0.0998, 0.9051
Inspected so far: PROPblock_3, PROPblock_5, PROPblock_6, PROPblock_7, PROPblock_9

Verified as grounded — correct as quoted, keep unchanged:
- PROPblock_6 + PROPblock_9 + PROPblock_5 + PROPblock_3 + PROPblock_7: 18, 298.15, 318.15, 0.0998, 0.9051, 780.53, 965.51, 101.0, 108, 268.1, 323.15, 0.1, 0.9, 774.3, 977.3, 24, 313.15, 0.10835, 0.71144, 848.29, 979.29, 101.3, 15, 293.15, 0.5, 897.6, 981.8, 0.04, 0.16, 966.4, 990.13, 85.0
- PROPblock_5: 24, 0.10835, 0.71144, 298.15, 313.15, 101.3, 0.16716, 964.04, 0.44202, 911.19, 848.29
- PROPblock_3: 15, 0.1, 0.5, 293.15, 313.15, 101.0, 974.6, 897.6
Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- PROPblock_9: 108, 0.1, 0.9, 268.1, 323.15, 101.0, 824.9, 774.3, 977.3, 942
- PROPblock_6: 18, 0.0998, 0.9051, 298.15, 318.15, 101.0, 0.1, 780.53, 0.5003, 840.31, 0.9, 952.47
- PROPblock_7: 0.04, 0.16, 298.15, 313.15, 85.0, 308.15, 987.24, 968.6, 0.1, 0.9

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## LLM Response

<reasoning>
The grounding checker flagged several issues:

1. "310" appears multiple times in prose like "near 310 K", "brackets 310 K", "closest to 310 K", "nearest to 310 K". These are NOT database data values — they are the user's query target temperature. I need to label them as the user's requested target, not database values.

2. "108" is flagged as ambiguous for PROPblock_7 — this is because in my final summary paragraph I wrote "GLOBlit_11136 block... 108 data points... x(water) 0.1–0.9... (268.1–323.15 K)" but the checker sees this paragraph as potentially about PROPblock_7 (the last block mentioned before the summary). I need to make sure the summary paragraph clearly attributes 108, 268.1, 323.15, 0.1–0.9, 0.0998–0.9051 to their correct blocks.

3. MISATTRIBUTED: 268.1 and 323.15 flagged as belonging to PROPblock_9 but attributed to PROPblock_7 — this is in the summary paragraph where the checker thinks I'm talking about PROPblock_7. I need to re-anchor clearly.

4. 0.0998 and 0.9051 in the summary are from PROPblock_6/GLOBlit_10699, not PROPblock_7.

The fix is purely textual — I need to restructure the final summary paragraph so the block attributions are unambiguous. No new tool calls needed.

Let me rewrite the answer surgically, keeping all verified values and just fixing the attribution/provenance issues.
</reasoning>

<summary>All flagged "310" values are the user's query target temperature, not database data. The misattributed values (108, 268.1, 323.15, 0.0998, 0.9051) in the summary paragraph need clear re-anchoring to their correct blocks (GLOBlit_11136/PROPblock_9 and GLOBlit_10699/PROPblock_6). No new inspections needed.</summary>

<answer>
## Density Data for Binary Ethanol–Water Mixtures near 310 K

Sixteen binary ethanol–water mass density (GLOBprop_1) blocks were found in the 305–315 K temperature window. The five most useful candidates, all verified by inspection, are summarized below. The target temperature of 310 K referenced throughout is the user's query condition, not a database measurement temperature.

### Inspected Candidates

| DOI | Block | GLOBlit | Total Points | T range (K) | Composition range | ρ range (kg/m³) | Pressure (kPa) | Comp. variable |
|-----|-------|---------|--------------|-------------|-------------------|-----------------|-----------------|----------------|
| 10.1021/je600565m | PROPblock_6 | GLOBlit_10699 | 18 | 298.15–318.15 | x(water) 0.0998–0.9051 | 780.53–965.51 | 101.0 | GLOBvar_2 (mole fraction) |
| 10.1021/je800150h | PROPblock_9 | GLOBlit_11136 | 108 | 268.1–323.15 | x(water) 0.1–0.9 | 774.3–977.3 | 101.0 | GLOBvar_2 (mole fraction) |
| 10.1021/je020173z | PROPblock_5 | GLOBlit_8050 | 24 | 298.15–313.15 | w(ethanol) 0.10835–0.71144 | 848.29–979.29 | 101.3 | GLOBvar_5 (mass fraction) |
| 10.1021/je900743e | PROPblock_3 | GLOBlit_11792 | 15 | 293.15–313.15 | w(ethanol) 0.1–0.5 | 897.6–981.8 | 101.0 | GLOBvar_5 (mass fraction) |
| 10.1021/acs.jced.6b01058 | PROPblock_7 | GLOBlit_7085 | 12 | 298.15–313.15 | w(ethanol) 0.04–0.16 | 966.4–990.13 | 85.0 | GLOBvar_5 (mass fraction) |

### Best Picks for Wide Composition Coverage

1. **GLOBlit_11136 / PROPblock_9** (DOI: 10.1021/je800150h) — **Largest dataset with wide composition**: 108 data points spanning x(water) 0.1–0.9 across T = 268.1–323.15 K at 101.0 kPa. This block covers nearly the full composition range and a broad temperature window that brackets the user's target of 310 K. Representative inspected points at the temperature extremes:
   - x(water) = 0.1: ρ = 824.9 kg/m³ (268.1 K) to 774.3 kg/m³ (323.15 K)
   - x(water) = 0.9: ρ = 977.3 kg/m³ (268.1 K) to 942 kg/m³ (323.15 K)

2. **GLOBlit_10699 / PROPblock_6** (DOI: 10.1021/je600565m) — **Widest mole-fraction range at two temperatures**: 18 points at x(water) 0.0998–0.9051, measured at 298.15 K and 318.15 K (101.0 kPa). The 318.15 K isotherm is the closer of the two to the user's target of 310 K. Representative inspected points at 318.15 K:
   - x(water) = 0.1: ρ = 780.53 kg/m³
   - x(water) = 0.5003: ρ = 840.31 kg/m³
   - x(water) = 0.9: ρ = 952.47 kg/m³

3. **GLOBlit_8050 / PROPblock_5** (DOI: 10.1021/je020173z) — **Wide mass-fraction range**: 24 points with w(ethanol) 0.10835–0.71144 at 298.15 K and 313.15 K (101.3 kPa). At 313.15 K:
   - w(ethanol) = 0.16716: ρ = 964.04 kg/m³
   - w(ethanol) = 0.44202: ρ = 911.19 kg/m³
   - w(ethanol) = 0.71144: ρ = 848.29 kg/m³

4. **GLOBlit_11792 / PROPblock_3** (DOI: 10.1021/je900743e) — 15 points at w(ethanol) 0.1–0.5 across 293.15–313.15 K (101.0 kPa). At 313.15 K:
   - w(ethanol) = 0.1: ρ = 974.6 kg/m³
   - w(ethanol) = 0.5: ρ = 897.6 kg/m³

5. **GLOBlit_7085 / PROPblock_7** (DOI: 10.1021/acs.jced.6b01058) — 12 points but narrow composition (w(ethanol) 0.04–0.16) at 298.15–313.15 K. Note: measured at 85.0 kPa rather than atmospheric pressure. At 308.15 K:
   - w(ethanol) = 0.04: ρ = 987.24 kg/m³
   - w(ethanol) = 0.16: ρ = 968.6 kg/m³

### Resolved IDs
- Ethanol: GLOBcomp_2 (C₂H₆O)
- Water: GLOBcomp_1 (H₂O)
- Mass density: GLOBprop_1

**GLOBlit_11136 / PROPblock_9** is the strongest overall candidate, offering 108 data points across x(water) 0.1–0.9 and a temperature range (268.1–323.15 K) that densely brackets the user's query target. **GLOBlit_10699 / PROPblock_6** provides the widest single-isotherm composition sweep (x(water) 0.0998–0.9051) but at only two temperatures (298.15 K and 318.15 K).
</answer>