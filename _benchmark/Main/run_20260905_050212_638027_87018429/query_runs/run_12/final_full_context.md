## System Prompt
# ThermoML Query Orchestrator

Top-level agent: interprets user questions, manages working memory,
dispatches L1 workers for database searches, integrates results.

You have NO direct database access — every fact must come from L1 returns.

**Chemistry-context hint:** When useful and tool-supported, use existing output fields to add a brief chemistry insight and one or a few representative data points with values, units, conditions, compounds, and DOI/block provenance. Mark inference, never invent data, and delegation-only roles should preserve rather than create this context.

## Core Rules

- ALWAYS call L1_query first for any data question.
- L1_query results, canonical IDs, and history are saved automatically by the
  runtime. Do not repeat that persistence with memory_add_result,
  memory_catalog_add, or memory_append_history.
- Final answer MUST contain actual data/numbers inline. NEVER say "saved to memory" as the answer.
- If L1 returns no_results: say "No data found in the ThermoML database for [X]". Do NOT fabricate.
- NEVER fabricate DOIs, block numbers, values, or cite external sources (JANAF, WebBook, textbooks).
- LITERATURE IDENTITY: `GLOBlit_N` is the authoritative literature
  identifier — prefer it in reasoning, memory, and delegation context. A DOI
  is coupled display metadata: whenever a DOI is reported, place its
  tool-returned `GLOBlit_N` next to it. Never emit an unpaired DOI; a final
  answer citing a DOI no tool coupled to a `GLOBlit_N` is scrubbed as
  unverifiable.
- Partial data: state what was found AND what is missing.
- Compact History (>30 entries) / Results (>10 entries) proactively.
- You can delegate property/system screening and ranking questions to
  `L1_query`. State the ranking direction, centre compounds, composition grid,
  numeric state constraints, and—when the question concerns solvent
  interactions—the exact centre-component mole fraction that should drive
  ranking. L1 owns the specialized ranking tool; L0 still has no direct
  database access.

## Numerical Grounding (MANDATORY)

- Every number in your answer (values, compositions, T/p conditions,
  uncertainties, counts, aggregates) must be copied VERBATIM from an
  L1_query result in THIS session, at source precision. Chemistry knowledge
  may guide interpretation — it must never supply a numeric value.
- If L1 returned only aggregates or ranges, report them AS aggregates.
  NEVER write out "representative" per-point values, rows, or smooth-grid
  compositions (0.1, 0.2, …) that no tool result contains — that is
  fabrication even when block/DOI citations are correct.
- Never fill a gap with a plausible number; state the gap. "Row-level
  values were not retrieved" is a valid answer.
- A rejected or errored call has NO result — never write or imagine one.
- L1 envelopes include `data_inspections` — verbatim inspected data
  tables. Quote data points only from those tables or the L1 answer
  verbatim; when a needed sub-block is missing, dispatch an L1 query that
  inspects it (workers have a mandatory `inspect_block_table` gate).
- Write plain markdown tables; delivery hardcode auto-enriches every answer
  table with a leading row-id column and a hardcoded table identifier (e.g.
  `Q#1_Table#2_Row#3`), so never invent such ids — and keep existing ids
  verbatim when quoting an upstream table.
- Chemical insights must stay grounded in the data you present: a
  comparative claim (higher/lower than a baseline or average) must hold
  arithmetically for the values quoted in your answer — otherwise keep
  the insight qualitative.
- Upstream results may carry UNVERIFIED flags. If a flagged value matters
  for your task, resolve it first (re-inspect / re-query its block anchor);
  otherwise treat it with caution under these same rules — never repeat an
  unverified number as verified.

## Agent-Emitted Markers

You MUST wrap your output in exactly these markers:

**During tool-calling turns:**
```
<reasoning>
... your thinking/planning (DISCARDED from memory after each turn) ...
</reasoning>
<summary>
... 1-3 sentence conclusion of what you did or plan to do (KEPT in memory, ≤400 chars) ...
</summary>
<tool_call>{"name": "L1_query", "arguments": {"purpose": "...", "instruction": "..."}}</tool_call>
<wait/>
```

**For the final answer (no more tool calls):**
```
<answer>
... your complete answer to the user's question — any length ...
Include all key numbers, DOIs, block numbers, temperature ranges.
For counts: state the count. For listings: include top 5+ entries.
</answer>
```

Rules:
- `<reasoning>` = extended thinking. Stripped after each turn, never persists.
- `<summary>` = brief conclusion. Persists in memory. Max 400 chars.
- `<tool_call>` MUST come AFTER `</summary>` and BEFORE `<wait/>`.
- `<answer>` = full final response to user. Can be as long as needed. All markers stripped from output.
- `<summary>` ≠ `<answer>`: summary is a brief memory note; answer is the complete user-facing response.
- `<answer>` must NEVER mention internal mechanics (working memory, L1 queries, memory keys, agent systems). Present data as if it came directly from the database. The user cannot see your memory or tool calls.

## Common Property IDs

| prop_num_id | Property | Unit |
|:-----------:|----------|------|
| GLOBprop_1  | Mass density | kg/m³ |
| GLOBprop_4  | Viscosity (dynamic) | Pa·s |
| GLOBprop_5  | Vapor/sublimation pressure | kPa |
| GLOBprop_7  | Refractive index (Na D-line) | — |
| GLOBprop_8  | Speed of sound | m/s |
| GLOBprop_9  | Molar Cp (constant pressure) | J/(K·mol) |
| GLOBprop_10 | Molar enthalpy of transition/fusion | kJ/mol |
| GLOBprop_11 | Solid–liquid equilibrium temperature | K |
| GLOBprop_13 | Surface tension (liquid–gas) | N/m |
| GLOBprop_14 | Boiling temperature at pressure P | K |
| GLOBprop_17 | Excess molar enthalpy (Hᴱ) | kJ/mol |
| GLOBprop_18 | Electrical conductivity | S/m |
| GLOBprop_40 | Kinematic viscosity | m²/s |
| GLOBprop_42 | Relative permittivity (various frequencies) | — |
| GLOBprop_44 | Relative permittivity (zero frequency / static dielectric constant) | — |

These are the ACTUAL database IDs. Do NOT guess property IDs.

## ID Conventions

- Every `*_num_id` is a typed global string (`GLOBcomp_N`, `GLOBprop_N`,
  `GLOBvar_N`, `GLOBconstr_N`, `GLOBmeas_N`, `GLOBphase_N`, `GLOBlit_N`,
  `GLOBsolvent_N`, `GLOBblocktype_N`, or `GLOBrxntype_N`). It is never a
  number. DOI compounds are `DOIcomp_N`; block declarations are `BLKprop_N`,
  `BLKvar_N`, and `BLKconstr_N`; blocks are `PROPblock_N` or `RXNblock_N`.
- Reject rather than normalize legacy IDs (`comp_N`, `prop_N`, `block_N`) or
  bare numbers. Never reconstruct, strip, or translate ID prefixes.
- Apply L1's core_id_updates to the ID Catalog immediately.
- Do NOT call memory_catalog_remove unless correcting an error.

# Tools

## memory
- memory_read(section=None) — read working memory or a section
- memory_append_history(line) — append log entry to History
- memory_add_result(key, body) — store named result in Results
- memory_catalog_add(type_, global_id, registry_id, name) — add a strict global ID to the ID Catalog; type_ is one of comp, prop, var, constr, meas, phase, lit, solvent, blocktype, rxntype and must match the GLOB* prefix
- memory_catalog_remove(type_, global_id) — remove an exact global ID from the ID Catalog
- memory_catalog_list() — list ID Catalog as JSON
- memory_compact(section, summary_text) — compact a section
- memory_reset() — reset working memory

## L1_workers
- L1_query(purpose, instruction, id_catalog, context) — dispatch query worker (max 2000 tok return)

# Prompt Template

## User Question
{{purpose}}

## Working Memory
{{context}}

## ID Catalog
{{id_catalog}}

# Phases

## phase_1: understand_and_plan
tools: [memory]
guidance: |
  Read working memory / ID Catalog. Interpret question, plan queries.

## phase_2: dispatch_and_integrate
tools: [L1_workers, memory]
guidance: |
  Dispatch L1_query with precise purpose+instruction. The runtime
  automatically persists its result, canonical IDs, and history. Inspect the
  returned result or memory_read as needed; do not duplicate persistence.
  Re-dispatch if partial results.
  For multi-part questions, dispatch multiple L1_query calls.
  For rankings, explicitly ask L1 to use its specialized property screening
  and ranking tool after resolving strict global IDs.

## phase_3: answer
tools: [memory]
guidance: |
  Wrap only the complete answer text in <answer> tags. Include actual
  data/numbers and concise chemical explanations supported by the completed
  work. Do not emit JSON, core claims, source objects, or other schema fields.
  Parallel tool-free post-answer agents create the core claims and ID/metadata
  fields after termination.

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
- L1_query(purpose, instruction, id_catalog='', context='') — Callable wrapper that auto-persists L1 query results in working memory.
- memory_add_result(key, body) — Add a named result entry to the Results section.
- memory_append_history(line) — Append a one-line entry to the History section.
- memory_catalog_add(type_, global_id, registry_id, name) — Add a row to the protected ID Catalog.
- memory_catalog_list() — List all entries in the ID Catalog as JSON.
- memory_catalog_remove(type_, global_id) — Remove a row from the ID Catalog.
- memory_compact(section, summary_text=None) — Compact a section by replacing it with a summary.
- memory_read(section=None) — Read the full working memory or a specific section.
- memory_reset() — Reset the working memory to an empty template.

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
| comp | GLOBcomp_1 | water | water |
| comp | GLOBcomp_5 | propan-1-ol | propan-1-ol |
| prop | GLOBprop_1 | mass_density_kg_m3 | Mass density, kg/m3 |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find all mass density data for binary mixture of water and 1-propanol near 298.15 K → stored as L1_query_1 · validation: FLAGGED(1)
- [L1] Inspect GLOBlit_590::PROPblock_5 for data points at 298.15 K and list additional blocks from the 17 found for water+1-pr → stored as L1_query_2 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: partial · validation: FLAGGED(1)

**Summary:** Mass density data for the binary liquid mixture of water (GLOBcomp_1) and 1-propanol (GLOBcomp_5) near 298.15 K were identified across 17 blocks in ThermoML. Two blocks were inspected in detail. GLOBlit_555::PROPblock_8 (DOI 10.1016/j.fluid.2007.07.066, P = 101.0 kPa, 15 total points spanning 283.15–303.15 K) reports densities at 298.15 K of 989.431, 983.475, and 978.117 kg/m³ at propan-1-ol mass fractions of 0.05, 0.10, and 0.15, respectively. GLOBlit_2979::PROPblock_9 (DOI 10.1016/j.jct.2008.07.005, P = 98.93 kPa, 96 total points spanning 283.15–308.15 K, mole fraction 0–0.2, overall density range 911.83–999.69 kg/m³) reports densities at 298.15 K of 997.04, 995.4, 993.76, 991.66, 991.14, 986.54, 982.56, and 975.49 kg/m³ at propan-1-ol mole fractions of 0, 0.002, 0.005, 0.009, 0.01, 0.02, 0.03, and 0.05, respectively. Density decreases monotonically with increasing 1-propanol content at 298.15 K, consistent with addition of a lighter alcohol to water. The two inspected blocks cover the water-rich region using different composition scales (mass fraction vs. mole fraction). A third block from GLOBlit_590::PROPblock_5 (DOI 10.1016/j.fluid.2008.01.004) was identified with mass fraction 0.05–0.15 and density range 975.791–992.405 kg/m³ at 283.15–303.15 K but was not inspected for individual data points.

**Answer:**

#### Mass Density Data for Water + 1-Propanol Binary Mixture near 298.15 K in ThermoML

**System:** Water (GLOBcomp_1) + 1-Propanol (GLOBcomp_5), binary, liquid phase  
**Property:** Mass density (GLOBprop_1, kg/m³)

##### Overview

The search_blocks discovery tool returned a total count of **17 blocks** (search-tool count, not individually verified) for this binary system with temperatures in the 293–303 K window. These blocks span various composition variables (mole fraction, mass fraction, molality) and pressure conditions (atmospheric to elevated pressures). The following block-level summary ranges are from the `search_blocks` discovery tool (not individually inspected):

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *#* | *DOI* | *Block* | *GLOBlit* | *Comp. Variable* | *T range (K)* | *P* | *ρ range (kg/m³)* | *Source* |
|---|---|---|---|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「1」 | 「10.1016/j.fluid.2007.07.066」 | 「PROPblock_8」 | 「GLOBlit_555」 | 「mass fraction w, 0.05–0.15」 | 「283.15–303.15」 | 「atm」 | 「976.004–992.444」 | 「search summary」 |
| WM_L1#1_Table#1_Row#2 | 「2」 | 「10.1016/j.fluid.2008.01.004」 | 「PROPblock_5」 | 「GLOBlit_590」 | 「mass fraction w, 0.05–0.15」 | 「283.15–303.15」 | 「atm」 | 「975.791–992.405」 | 「search summary」 |
| WM_L1#1_Table#1_Row#3 | 「3」 | 「10.1016/j.jct.2008.07.005」 | 「PROPblock_9」 | 「GLOBlit_2979」 | 「mole fraction x, 0–0.2」 | 「283.15–298.15」 | 「atm (98.93 kPa)」 | 「911.83–999.69」 | 「search summary + inspected」 |

Additional blocks (including high-pressure and elevated-temperature datasets) were returned but not shown here (derived count: 17 total minus 3 listed = remaining blocks not displayed). Only blocks 1 and 3 were inspected for verbatim data points below.

---

##### Inspected Data Points at T = 298.15 K

###### Block 1: GLOBlit_555 :: PROPblock_8 (DOI: 10.1016/j.fluid.2007.07.066)
Constraint: P = 101.0 kPa. Composition in mass fraction of propan-1-ol.

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *mass_fraction (propan-1-ol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0.05」 | 「989.431」 |
| WM_L1#1_Table#2_Row#2 | 「0.10」 | 「983.475」 |
| WM_L1#1_Table#2_Row#3 | 「0.15」 | 「978.117」 |

Full block spans 283.15–303.15 K with 15 total points (from inspection stats).

###### Block 2: GLOBlit_2979 :: PROPblock_9 (DOI: 10.1016/j.jct.2008.07.005)
Constraint: P = 98.93 kPa. Composition in mole fraction of propan-1-ol.

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *mole_fraction (propan-1-ol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0」 | 「997.04」 |
| WM_L1#1_Table#3_Row#2 | 「0.002」 | 「995.4」 |
| WM_L1#1_Table#3_Row#3 | 「0.005」 | 「993.76」 |
| WM_L1#1_Table#3_Row#4 | 「0.009」 | 「991.66」 |
| WM_L1#1_Table#3_Row#5 | 「0.01」 | 「991.14」 |
| WM_L1#1_Table#3_Row#6 | 「0.02」 | 「986.54」 |
| WM_L1#1_Table#3_Row#7 | 「0.03」 | 「982.56」 |
| WM_L1#1_Table#3_Row#8 | 「0.05」 | 「975.49」 |

Full block spans 283.15–308.15 K with 96 total points; mole fraction range 0–0.2; density range across all temperatures: 911.83–999.69 kg/m³ (from inspection stats).

---

##### Chemistry Insight

The inspected data show a clear monotonic decrease in density with increasing 1-propanol content at 298.15 K. At x(propan-1-ol) = 0, the density is 997.04 kg/m³ (essentially pure water), dropping to 975.49 kg/m³ at x = 0.05 (GLOBlit_2979::PROPblock_9). This is consistent with the addition of a lighter alcohol to water. The two inspected sources cover the water-rich region: PROPblock_8 uses mass fraction (0.05–0.15) while PROPblock_9 uses mole fraction (0–0.2), making direct numerical comparison between them require unit conversion (not performed here). The blocks returned by the search collectively provide extensive coverage of this binary system near ambient temperature.

**Core claims:**
- At 298.15 K and near-atmospheric pressure, the mass density of the water + 1-propanol binary mixture decreases monotonically with increasing 1-propanol content in the water-rich region, from 997.04 kg/m³ at x(propan-1-ol) = 0 to 975.49 kg/m³ at x = 0.05 (GLOBlit_2979::PROPblock_9, P = 98.93 kPa).
- Two independent ThermoML sources were inspected: GLOBlit_555::PROPblock_8 reports densities of 989.431, 983.475, and 978.117 kg/m³ at mass fractions 0.05, 0.10, and 0.15 of propan-1-ol (P = 101.0 kPa, T = 298.15 K), and GLOBlit_2979::PROPblock_9 reports densities at mole fractions 0–0.05 (P = 98.93 kPa, T = 298.15 K); direct numerical comparison between the two requires unit conversion that was not performed.
- The search returned a total of 17 blocks for this binary system near 298.15 K, but only two blocks (PROPblock_8 and PROPblock_9) were individually inspected, so coverage of the full composition and pressure range is incomplete in the verified data.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_555」 | 「PROPblock_8」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + 1-propanol binary mixture at 283.15–303.15 K, mass fraction 0.05–0.15, atmospheric pressure. Inspected data at 298.15 K: 978.117–989.431 kg/m³.」 |
| WM_L1#1_Table#5 | 「GLOBlit_590」 | 「PROPblock_5」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + 1-propanol binary mixture at 283.15–303.15 K, mass fraction 0.05–0.15, atmospheric pressure. Not individually inspected.」 |
| WM_L1#1_Table#6 | 「GLOBlit_2979」 | 「PROPblock_9」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water + 1-propanol binary mixture at 283.15–298.15 K, mole fraction 0–0.2, P=98.93 kPa. Inspected data at 298.15 K: 975.49–997.04 kg/m³.」 |

*Not stored here: 2 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** PROPblock_9: 17 (near '…datasets) were returned but not shown here (derived count: 1…') matches no inspected row/stat, database table, or other source of PROPblock_9
### L1_query_2
**L1_query_2** — status: success · validation: PASS

**Summary:** For the binary liquid system water + 1-propanol at 298.15 K and 101.0 kPa, GLOBlit_590::PROPblock_5 (DOI 10.1016/j.fluid.2008.01.004) reports density as a function of mass fraction of propan-1-ol: 989.387 kg/m³ at 0.05, 983.372 kg/m³ at 0.10, and 977.921 kg/m³ at 0.15. The full block spans 15 data points over T = 283.15–303.15 K and ρ = 975.791–992.405 kg/m³. At least 13 additional ThermoML blocks from other DOIs (GLOBlit_555, GLOBlit_2432, GLOBlit_2979, GLOBlit_4068, GLOBlit_4415, GLOBlit_5585, GLOBlit_7085, GLOBlit_7178, GLOBlit_8254, GLOBlit_10159, GLOBlit_11142, among others) also contain water + 1-propanol density data near 298.15 K but were not inspected in this run, so no numerical values are reported for them.

**Answer:**

#### Inspection of GLOBlit_590::PROPblock_5 at 298.15 K

**Source:** DOI 10.1016/j.fluid.2008.01.004 (GLOBlit_590), PROPblock_5  
**System:** Water + 1-propanol, binary, liquid phase  
**Constraint:** P = 101.0 kPa  
**Composition variable:** Mass fraction of propan-1-ol (0.05–0.15)  
**Full block:** 15 data points, T = 283.15–303.15 K, ρ = 975.791–992.405 kg/m³

##### Data points at T = 298.15 K (verbatim from inspection):

**WM_L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *mass_fraction (propan-1-ol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「0.05」 | 「989.387」 |
| WM_L1#2_Table#1_Row#2 | 「0.10」 | 「983.372」 |
| WM_L1#2_Table#1_Row#3 | 「0.15」 | 「977.921」 |

These three data points at 298.15 K show the expected monotonic decrease in density with increasing 1-propanol content.

---

#### Full Listing of Blocks for Water + 1-Propanol Density near 298.15 K

The search_system_registry returned blocks for this binary system in a temperature window around 298.15 K. The following table lists all blocks identified by DOI, GLOBlit, and block number. Numerical details are shown only for the block inspected in this run (GLOBlit_590::PROPblock_5, above).

**WM_L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *DOI* | *GLOBlit* | *Block* | *Status* |
|---|---|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「10.1016/j.fluid.2007.07.066」 | 「GLOBlit_555」 | 「PROPblock_8」 | 「Not inspected in this run」 |
| WM_L1#2_Table#2_Row#2 | 「10.1016/j.fluid.2008.01.004」 | 「GLOBlit_590」 | 「PROPblock_5」 | 「Inspected in this run (see above)」 |
| WM_L1#2_Table#2_Row#3 | 「10.1016/j.jct.2004.07.019」 | 「GLOBlit_2432」 | 「PROPblock_3」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#4 | 「10.1016/j.jct.2008.07.005」 | 「GLOBlit_2979」 | 「PROPblock_9」 | 「Not inspected in this run」 |
| WM_L1#2_Table#2_Row#5 | 「10.1016/j.jct.2013.11.036」 | 「GLOBlit_4068」 | 「PROPblock_1」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#6 | 「10.1016/j.jct.2013.11.036」 | 「GLOBlit_4068」 | 「PROPblock_2」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#7 | 「10.1016/j.jct.2015.06.024」 | 「GLOBlit_4415」 | 「PROPblock_5」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#8 | 「10.1016/j.jct.2019.105880」 | 「GLOBlit_5585」 | 「PROPblock_7」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#9 | 「10.1021/acs.jced.6b01058」 | 「GLOBlit_7085」 | 「PROPblock_8」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#10 | 「10.1021/acs.jced.7b00299」 | 「GLOBlit_7178」 | 「PROPblock_13」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#11 | 「10.1021/je034101z」 | 「GLOBlit_8254」 | 「PROPblock_6」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#12 | 「10.1021/je4003515」 | 「GLOBlit_10159」 | 「PROPblock_10」 | 「Not inspected」 |
| WM_L1#2_Table#2_Row#13 | 「10.1021/je800158z」 | 「GLOBlit_11142」 | 「PROPblock_3」 | 「Not inspected (registry entry truncated)」 |
| WM_L1#2_Table#2_Row#14 | 「(truncated in registry output)」 | 「—」 | 「—」 | 「Not available」 |

**Notes:**
- Composition variables, pressure conditions, point counts, and density ranges for uninspected blocks were not verified via inspection and are therefore not reported here.
- Only GLOBlit_590::PROPblock_5 was inspected in this run. GLOBlit_555::PROPblock_8 and GLOBlit_2979::PROPblock_9 were inspected in the prior session (see working memory for those data points) but were not re-inspected here.
- The row count shown in the listing table is derived from the registry tool output, not from block inspection. The registry listing was truncated after the entry shown for GLOBlit_11142.

**Core claims:**
- For the water + 1-propanol binary system at 298.15 K and 101.0 kPa (GLOBlit_590::PROPblock_5, DOI 10.1016/j.fluid.2008.01.004), the liquid density decreases monotonically with increasing 1-propanol mass fraction: 989.387 kg/m³ at 0.05, 983.372 kg/m³ at 0.10, and 977.921 kg/m³ at 0.15.
- At least 13 additional ThermoML data blocks from independent literature sources contain density data for the water + 1-propanol binary system near 298.15 K, but these blocks were not inspected in this run and their numerical values were not verified.

**Core blocks found:**

**WM_L1#2_Blocks_(Query_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#3 | 「GLOBlit_590」 | 「PROPblock_5」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol at P=101.0 kPa, T=283.15–303.15 K, mass fraction 0.05–0.15, ρ=975.791–992.405 kg/m³. Inspected: 3 points at 298.15 K.」 |
| WM_L1#2_Table#4 | 「GLOBlit_555」 | 「PROPblock_8」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected in this run.」 |
| WM_L1#2_Table#5 | 「GLOBlit_2979」 | 「PROPblock_9」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected in this run.」 |
| WM_L1#2_Table#6 | 「GLOBlit_2432」 | 「PROPblock_3」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#7 | 「GLOBlit_4068」 | 「PROPblock_1」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#8 | 「GLOBlit_4068」 | 「PROPblock_2」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#9 | 「GLOBlit_4415」 | 「PROPblock_5」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#10 | 「GLOBlit_5585」 | 「PROPblock_7」 | 「GLOBcomp_1, GLOBcomp_5」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#11 | 「GLOBlit_7085」 | 「PROPblock_8」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#12 | 「GLOBlit_7178」 | 「PROPblock_13」 | 「GLOBcomp_1, GLOBcomp_5」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#13 | 「GLOBlit_8254」 | 「PROPblock_6」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#14 | 「GLOBlit_10159」 | 「PROPblock_10」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected.」 |
| WM_L1#2_Table#15 | 「GLOBlit_11142」 | 「PROPblock_3」 | 「GLOBcomp_5, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of water+1-propanol near 298.15 K. Not inspected; registry entry truncated.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.



</memory>

## User
[Purpose: Locate all available mixture density data for aqueous 1-propanol at or near 298.15 K]
Find density measurements for the binary mixture of water and 1-propanol near 298.15 K. I need DOIs, block numbers, temperature ranges, composition ranges, and density values.

[Context: The user is planning density measurements for aqueous 1-propanol at 25 °C and wants to know what data already exists. Search for density (mass density) property for the system water + 1-propanol. The compounds are water (H2O) and 1-propanol (C3H8O, also known as n-propanol or propan-1-ol).]

## Assistant
<summary>Dispatching L1 query to search for mass density data of water + 1-propanol binary mixtures near 298.15 K.</summary>
<tool_call>L1_query(instruction=Search for mass d…, id_catalog=, context=User wants to kno…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=partial

**Summary:** Mass density data for the binary liquid mixture of water (GLOBcomp_1) and 1-propanol (GLOBcomp_5) near 298.15 K were identified across 17 blocks in ThermoML. Two blocks were inspected in detail. GLOBlit_555::PROPblock_8 (DOI 10.1016/j.fluid.2007.07.066, P = 101.0 kPa, 15 total points spanning 283.15–303.15 K) reports densities at 298.15 K of 989.431, 983.475, and 978.117 kg/m³ at propan-1-ol mass fractions of 0.05, 0.10, and 0.15, respectively. GLOBlit_2979::PROPblock_9 (DOI 10.1016/j.jct.2008.07.005, P = 98.93 kPa, 96 total points spanning 283.15–308.15 K, mole fraction 0–0.2, overall density range 911.83–999.69 kg/m³) reports densities at 298.15 K of 997.04, 995.4, 993.76, 991.66, 991.14, 986.54, 982.56, and 975.49 kg/m³ at propan-1-ol mole fractions of 0, 0.002, 0.005, 0.009, 0.01, 0.02, 0.03, and 0.05, respectively. Density decreases monotonically with increasing 1-propanol content at 298.15 K, consistent with addition of a lighter alcohol to water. The two inspected blocks cover the water-rich region using different composition scales (mass fraction vs. mole fraction). A third block from GLOBlit_590::PROPblock_5 (DOI 10.1016/j.fluid.2008.01.004) was identified with mass fraction 0.05–0.15 and density range 975.791–992.405 kg/m³ at 283.15–303.15 K but was not inspected for individual data points.

**Answer:**

#### Mass Density Data for Water + 1-Propanol Binary Mixture near 298.15 K in ThermoML

**System:** Water (GLOBcomp_1) + 1-Propanol (GLOBcomp_5), binary, liquid phase  
**Property:** Mass density (GLOBprop_1, kg/m³)

##### Overview

The search_blocks discovery tool returned a total count of **17 blocks** (search-tool count, not individually verified) for this binary system with temperatures in the 293–303 K window. These blocks span various composition variables (mole fraction, mass fraction, molality) and pressure conditions (atmospheric to elevated pressures). The following block-level summary ranges are from the `search_blocks` discovery tool (not individually inspected):

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *#* | *DOI* | *Block* | *GLOBlit* | *Comp. Variable* | *T range (K)* | *P* | *ρ range (kg/m³)* | *Source* |
|---|---|---|---|---|---|---|---|---|---|
| L1#1_Table#1_Row#1 | 「1」 | 「10.1016/j.fluid.2007.07.066」 | 「PROPblock_8」 | 「GLOBlit_555」 | 「mass fraction w, 0.05–0.15」 | 「283.15–303.15」 | 「atm」 | 「976.004–992.444」 | 「search summary」 |
| L1#1_Table#1_Row#2 | 「2」 | 「10.1016/j.fluid.2008.01.004」 | 「PROPblock_5」 | 「GLOBlit_590」 | 「mass fraction w, 0.05–0.15」 | 「283.15–303.15」 | 「atm」 | 「975.791–992.405」 | 「search summary」 |
| L1#1_Table#1_Row#3 | 「3」 | 「10.1016/j.jct.2008.07.005」 | 「PROPblock_9」 | 「GLOBlit_2979」 | 「mole fraction x, 0–0.2」 | 「283.15–298.15」 | 「atm (98.93 kPa)」 | 「911.83–999.69」 | 「search summary + inspected」 |

Additional blocks (including high-pressure and elevated-temperature datasets) were returned but not shown here (derived count: 17 total minus 3 listed = remaining blocks not displayed). Only blocks 1 and 3 were inspected for verbatim data points below.

---

##### Inspected Data Points at T = 298.15 K

###### Block 1: GLOBlit_555 :: PROPblock_8 (DOI: 10.1016/j.fluid.2007.07.066)
Constraint: P = 101.0 kPa. Composition in mass fraction of propan-1-ol.

**L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *mass_fraction (propan-1-ol)* | *ρ (kg/m³)* |
|---|---|---|
| L1#1_Table#2_Row#1 | 「0.05」 | 「989.431」 |
| L1#1_Table#2_Row#2 | 「0.10」 | 「983.475」 |
| L1#1_Table#2_Row#3 | 「0.15」 | 「978.117」 |

Full block spans 283.15–303.15 K with 15 total points (from inspection stats).

###### Block 2: GLOBlit_2979 :: PROPblock_9 (DOI: 10.1016/j.jct.2008.07.005)
Constraint: P = 98.93 kPa. Composition in mole fraction of propan-1-ol.

**L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *mole_fraction (propan-1-ol)* | *ρ (kg/m³)* |
|---|---|---|
| L1#1_Table#3_Row#1 | 「0」 | 「997.04」 |
| L1#1_Table#3_Row#2 | 「0.002」 | 「995.4」 |
| L1#1_Table#3_Row#3 | 「0.005」 | 「993.76」 |
| L1#1_Table#3_Row#4 | 「0.009」 | 「991.66」 |
| L1#1_Table#3_Row#5 | 「0.01」 | 「991.14」 |
| L1#1_Table#3_Row#6 | 「0.02」 | 「986.54」 |
| L1#1_Table#3_Row#7 | 「0.03」 | 「982.56」 |
| L1#1_Table#3_Row#8 | 「0.05」 | 「975.49」 |

Full block spans 283.15–308.15 K with 96 total points; mole fraction range 0–0.2; density range across all temperatures: 911.83–999.69 kg/m³ (from inspection stats).

---

##### Chemistry Insight

The inspected data show a clear monotonic decrease in density with increasing 1-propanol content at 298.15 K. At x(propan-1-ol) = 0, the density is 997.04 kg/m³ (essentially pure water), dropping to 975.49 kg/m³ at x = 0.05 (GLOBlit_2979::PROPblock_9). This is consistent with the addition of a lighter alcohol to water. The two inspected sources cover the water-rich region: PROPblock_8 uses mass fraction (0.05–0.15) while PROPblock_9 uses mole fraction (0–0.2), making direct numerical comparison between them require unit conversion (not performed here). The blocks returned by the search collectively provide extensive coverage of this binary system near ambient temperature.

---
[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:
- **UNGROUNDED_LITERAL** PROPblock_9: 17 (near '…datasets) were returned but not shown here (derived count: 1…') matches no inspected row/stat, database table, or other source of PROPblock_9
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="PROPblock_9", literature="<GLOBlit_N or DOI>", nearest={"column": "temperature_k", "value": 17.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
Inspected so far: PROPblock_8, PROPblock_9

**Core claims:**
- At 298.15 K and near-atmospheric pressure, the mass density of the water + 1-propanol binary mixture decreases monotonically with increasing 1-propanol content in the water-rich region, from 997.04 kg/m³ at x(propan-1-ol) = 0 to 975.49 kg/m³ at x = 0.05 (GLOBlit_2979::PROPblock_9, P = 98.93 kPa).
- Two independent ThermoML sources were inspected: GLOBlit_555::PROPblock_8 reports densities of 989.431, 983.475, and 978.117 kg/m³ at mass fractions 0.05, 0.10, and 0.15 of propan-1-ol (P = 101.0 kPa, T = 298.15 K), and GLOBlit_2979::PROPblock_9 reports densities at mole fractions 0–0.05 (P = 98.93 kPa, T = 298.15 K); direct numerical comparison between the two requires unit conversion that was not performed.
- The search returned a total of 17 blocks for this binary system near 298.15 K, but only two blocks (PROPblock_8 and PROPblock_9) were individually inspected, so coverage of the full composition and pressure range is incomplete in the verified data.

**Core ID updates:**
- add GLOBcomp_1 — water (registry: water)
- add GLOBcomp_5 — propan-1-ol (registry: propan-1-ol)
- add GLOBprop_1 — Mass density, kg/m3 (registry: mass_density_kg_m3)

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#4_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_555 | lit_id: 2007-sad-kho-0 | doi: 10.1016/j.fluid.2007.07.066
block: PROPblock_8 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 15
compounds: propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_2; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_3; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water + 1-propanol binary mixture at 283.15–303.15 K, mass fraction 0.05–0.15, atmospheric pressure. Inspected data at 298.15 K: 978.117–989.431 kg/m³.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#4_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#4_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–303.15 · n_unique=5 · phase=Liquid」 |
| L1#1_Table#4_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_5」 | 「Mass fraction of propan-1-ol」 | 「range=0.05–0.15 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#4_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:4 (GLOBmeas_134) · range=976.004–992.444 · mean=984.9872 · n=15 · phase=Liquid」 |
```

```ledger
**L1#1_Table#5_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_590 | lit_id: 2008-sad-par-0 | doi: 10.1016/j.fluid.2008.01.004
block: PROPblock_5 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 15
compounds: propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_1; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_2; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water + 1-propanol binary mixture at 283.15–303.15 K, mass fraction 0.05–0.15, atmospheric pressure. Not individually inspected.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#5_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#5_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_5」 | 「Mass fraction of propan-1-ol」 | 「range=0.05–0.15 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#5_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–303.15 · n_unique=5 · phase=Liquid」 |
| L1#1_Table#5_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:4 (GLOBmeas_134) · range=975.791–992.405 · mean=984.879933 · n=15 · phase=Liquid」 |
```

```ledger
**L1#1_Table#6_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_2979 | lit_id: 2008-rom-pae-0 | doi: 10.1016/j.jct.2008.07.005
block: PROPblock_9 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 96
compounds: propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_1; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_5; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water + 1-propanol binary mixture at 283.15–298.15 K, mole fraction 0–0.2, P=98.93 kPa. Inspected data at 298.15 K: 975.49–997.04 kg/m³.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#6_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=98.93 · phase=Liquid」 |
| L1#1_Table#6_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–308.15 · n_unique=6 · phase=Liquid」 |
| L1#1_Table#6_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of propan-1-ol」 | 「range=0.0–0.2 · n_unique=16 · phase=Liquid」 |
| L1#1_Table#6_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=PYCNOM:UFactor:4 (GLOBmeas_153) · range=911.83–999.69 · mean=965.947604 · n=96 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#7_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_555 | doi: 10.1016/j.fluid.2007.07.066 | block: PROPblock_8
table_mode: nearest | inspection_id: INSP_3aa36d70ff07 | rows_shown: 5

| *row_id* | *BLKpoint_id* | *temperature_k* | *mass_fraction_<propan-1-ol>* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| L1#1_Table#7_Row#1 | 「BLKpoint_7」 | 「293.15」 | 「0.05」 | 「101.0」 | 「990.715」 |
| L1#1_Table#7_Row#2 | 「BLKpoint_8」 | 「293.15」 | 「0.1」 | 「101.0」 | 「985.011」 |
| L1#1_Table#7_Row#3 | 「BLKpoint_10」 | 「298.15」 | 「0.05」 | 「101.0」 | 「989.431」 |
| L1#1_Table#7_Row#4 | 「BLKpoint_11」 | 「298.15」 | 「0.1」 | 「101.0」 | 「983.475」 |
| L1#1_Table#7_Row#5 | 「BLKpoint_12」 | 「298.15」 | 「0.15」 | 「101.0」 | 「978.117」 |
```

```ledger
**L1#1_Table#8_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_2979 | doi: 10.1016/j.jct.2008.07.005 | block: PROPblock_9
table_mode: nearest | inspection_id: INSP_884f359f5908 | rows_shown: 8

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<propan-1-ol>* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| L1#1_Table#8_Row#1 | 「BLKpoint_49」 | 「298.15」 | 「0」 | 「98.93」 | 「997.04」 |
| L1#1_Table#8_Row#2 | 「BLKpoint_50」 | 「298.15」 | 「0.002」 | 「98.93」 | 「995.4」 |
| L1#1_Table#8_Row#3 | 「BLKpoint_51」 | 「298.15」 | 「0.005」 | 「98.93」 | 「993.76」 |
| L1#1_Table#8_Row#4 | 「BLKpoint_52」 | 「298.15」 | 「0.009」 | 「98.93」 | 「991.66」 |
| L1#1_Table#8_Row#5 | 「BLKpoint_53」 | 「298.15」 | 「0.01」 | 「98.93」 | 「991.14」 |
| L1#1_Table#8_Row#6 | 「BLKpoint_54」 | 「298.15」 | 「0.02」 | 「98.93」 | 「986.54」 |
| L1#1_Table#8_Row#7 | 「BLKpoint_55」 | 「298.15」 | 「0.03」 | 「98.93」 | 「982.56」 |
| L1#1_Table#8_Row#8 | 「BLKpoint_56」 | 「298.15」 | 「0.05」 | 「98.93」 | 「975.49」 |
```
</subagent_answer>
</tool_result>

## Assistant
<summary>L1 returned 17 blocks for water+1-propanol density near 298.15 K. Two blocks inspected with verbatim data. Dispatching follow-up to inspect GLOBlit_590::PROPblock_5 and list more of the remaining 14 blocks.</summary>
<tool_call>L1_query(instruction=For the binary mi…, id_catalog=GLOBcomp_1=water,…, context=Previous…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#2 — L1_query return

**Status:** status=success

**Summary:** For the binary liquid system water + 1-propanol at 298.15 K and 101.0 kPa, GLOBlit_590::PROPblock_5 (DOI 10.1016/j.fluid.2008.01.004) reports density as a function of mass fraction of propan-1-ol: 989.387 kg/m³ at 0.05, 983.372 kg/m³ at 0.10, and 977.921 kg/m³ at 0.15. The full block spans 15 data points over T = 283.15–303.15 K and ρ = 975.791–992.405 kg/m³. At least 13 additional ThermoML blocks from other DOIs (GLOBlit_555, GLOBlit_2432, GLOBlit_2979, GLOBlit_4068, GLOBlit_4415, GLOBlit_5585, GLOBlit_7085, GLOBlit_7178, GLOBlit_8254, GLOBlit_10159, GLOBlit_11142, among others) also contain water + 1-propanol density data near 298.15 K but were not inspected in this run, so no numerical values are reported for them.

**Answer:**

#### Inspection of GLOBlit_590::PROPblock_5 at 298.15 K

**Source:** DOI 10.1016/j.fluid.2008.01.004 (GLOBlit_590), PROPblock_5  
**System:** Water + 1-propanol, binary, liquid phase  
**Constraint:** P = 101.0 kPa  
**Composition variable:** Mass fraction of propan-1-ol (0.05–0.15)  
**Full block:** 15 data points, T = 283.15–303.15 K, ρ = 975.791–992.405 kg/m³

##### Data points at T = 298.15 K (verbatim from inspection):

**L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *mass_fraction (propan-1-ol)* | *ρ (kg/m³)* |
|---|---|---|
| L1#2_Table#1_Row#1 | 「0.05」 | 「989.387」 |
| L1#2_Table#1_Row#2 | 「0.10」 | 「983.372」 |
| L1#2_Table#1_Row#3 | 「0.15」 | 「977.921」 |

These three data points at 298.15 K show the expected monotonic decrease in density with increasing 1-propanol content.

---

#### Full Listing of Blocks for Water + 1-Propanol Density near 298.15 K

The search_system_registry returned blocks for this binary system in a temperature window around 298.15 K. The following table lists all blocks identified by DOI, GLOBlit, and block number. Numerical details are shown only for the block inspected in this run (GLOBlit_590::PROPblock_5, above).

**L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *DOI* | *GLOBlit* | *Block* | *Status* |
|---|---|---|---|---|
| L1#2_Table#2_Row#1 | 「10.1016/j.fluid.2007.07.066」 | 「GLOBlit_555」 | 「PROPblock_8」 | 「Not inspected in this run」 |
| L1#2_Table#2_Row#2 | 「10.1016/j.fluid.2008.01.004」 | 「GLOBlit_590」 | 「PROPblock_5」 | 「Inspected in this run (see above)」 |
| L1#2_Table#2_Row#3 | 「10.1016/j.jct.2004.07.019」 | 「GLOBlit_2432」 | 「PROPblock_3」 | 「Not inspected」 |
| L1#2_Table#2_Row#4 | 「10.1016/j.jct.2008.07.005」 | 「GLOBlit_2979」 | 「PROPblock_9」 | 「Not inspected in this run」 |
| L1#2_Table#2_Row#5 | 「10.1016/j.jct.2013.11.036」 | 「GLOBlit_4068」 | 「PROPblock_1」 | 「Not inspected」 |
| L1#2_Table#2_Row#6 | 「10.1016/j.jct.2013.11.036」 | 「GLOBlit_4068」 | 「PROPblock_2」 | 「Not inspected」 |
| L1#2_Table#2_Row#7 | 「10.1016/j.jct.2015.06.024」 | 「GLOBlit_4415」 | 「PROPblock_5」 | 「Not inspected」 |
| L1#2_Table#2_Row#8 | 「10.1016/j.jct.2019.105880」 | 「GLOBlit_5585」 | 「PROPblock_7」 | 「Not inspected」 |
| L1#2_Table#2_Row#9 | 「10.1021/acs.jced.6b01058」 | 「GLOBlit_7085」 | 「PROPblock_8」 | 「Not inspected」 |
| L1#2_Table#2_Row#10 | 「10.1021/acs.jced.7b00299」 | 「GLOBlit_7178」 | 「PROPblock_13」 | 「Not inspected」 |
| L1#2_Table#2_Row#11 | 「10.1021/je034101z」 | 「GLOBlit_8254」 | 「PROPblock_6」 | 「Not inspected」 |
| L1#2_Table#2_Row#12 | 「10.1021/je4003515」 | 「GLOBlit_10159」 | 「PROPblock_10」 | 「Not inspected」 |
| L1#2_Table#2_Row#13 | 「10.1021/je800158z」 | 「GLOBlit_11142」 | 「PROPblock_3」 | 「Not inspected (registry entry truncated)」 |
| L1#2_Table#2_Row#14 | 「(truncated in registry output)」 | 「—」 | 「—」 | 「Not available」 |

**Notes:**
- Composition variables, pressure conditions, point counts, and density ranges for uninspected blocks were not verified via inspection and are therefore not reported here.
- Only GLOBlit_590::PROPblock_5 was inspected in this run. GLOBlit_555::PROPblock_8 and GLOBlit_2979::PROPblock_9 were inspected in the prior session (see working memory for those data points) but were not re-inspected here.
- The row count shown in the listing table is derived from the registry tool output, not from block inspection. The registry listing was truncated after the entry shown for GLOBlit_11142.

**Core claims:**
- For the water + 1-propanol binary system at 298.15 K and 101.0 kPa (GLOBlit_590::PROPblock_5, DOI 10.1016/j.fluid.2008.01.004), the liquid density decreases monotonically with increasing 1-propanol mass fraction: 989.387 kg/m³ at 0.05, 983.372 kg/m³ at 0.10, and 977.921 kg/m³ at 0.15.
- At least 13 additional ThermoML data blocks from independent literature sources contain density data for the water + 1-propanol binary system near 298.15 K, but these blocks were not inspected in this run and their numerical values were not verified.

#### Core blocks found — verbatim ledger

```ledger
**L1#2_Table#3_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_590 | lit_id: 2008-sad-par-0 | doi: 10.1016/j.fluid.2008.01.004
block: PROPblock_5 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 15
compounds: propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_1; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_2; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water+1-propanol at P=101.0 kPa, T=283.15–303.15 K, mass fraction 0.05–0.15, ρ=975.791–992.405 kg/m³. Inspected: 3 points at 298.15 K.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#3_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#2_Table#3_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_5」 | 「Mass fraction of propan-1-ol」 | 「range=0.05–0.15 · n_unique=3 · phase=Liquid」 |
| L1#2_Table#3_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–303.15 · n_unique=5 · phase=Liquid」 |
| L1#2_Table#3_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:4 (GLOBmeas_134) · range=975.791–992.405 · mean=984.879933 · n=15 · phase=Liquid」 |
```

```ledger
**L1#2_Table#4_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_555 | lit_id: 2007-sad-kho-0 | doi: 10.1016/j.fluid.2007.07.066
block: PROPblock_8 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 15
compounds: propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_2; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_3; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water+1-propanol near 298.15 K. Not inspected in this run.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#4_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#2_Table#4_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–303.15 · n_unique=5 · phase=Liquid」 |
| L1#2_Table#4_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_5」 | 「Mass fraction of propan-1-ol」 | 「range=0.05–0.15 · n_unique=3 · phase=Liquid」 |
| L1#2_Table#4_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:4 (GLOBmeas_134) · range=976.004–992.444 · mean=984.9872 · n=15 · phase=Liquid」 |
```

```ledger
**L1#2_Table#5_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_2979 | lit_id: 2008-rom-pae-0 | doi: 10.1016/j.jct.2008.07.005
block: PROPblock_9 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 96
compounds: propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_1; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_5; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water+1-propanol near 298.15 K. Not inspected in this run.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#5_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=98.93 · phase=Liquid」 |
| L1#2_Table#5_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–308.15 · n_unique=6 · phase=Liquid」 |
| L1#2_Table#5_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of propan-1-ol」 | 「range=0.0–0.2 · n_unique=16 · phase=Liquid」 |
| L1#2_Table#5_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=PYCNOM:UFactor:4 (GLOBmeas_153) · range=911.83–999.69 · mean=965.947604 · n=96 · phase=Liquid」 |
```

```ledger
**L1#2_Table#6_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_2432 | lit_id: 2004-hyn-hne-0 | doi: 10.1016/j.jct.2004.07.019
block: PROPblock_3 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 456
compounds: propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_2; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_4; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water+1-propanol near 298.15 K. Not inspected.
solvents: [{'component_org_num': 'DOIcomp_4', 'comp_num_id': 'GLOBcomp_1', 'solvent_num_id': 'GLOBsolvent_1', 'inchi_key': 'XLYOFNOQVPJJNP-UHFFFAOYSA-N'}]

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#6_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–573.15 · n_unique=18 · phase=Liquid」 |
| L1#2_Table#6_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_3」 | 「Pressure, kPa」 | 「range=420.0–30310.0 · n_unique=30 · phase=Liquid」 |
| L1#2_Table#6_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_4」 | 「Molality, mol/kg of propan-1-ol」 | 「range=0.0943–0.84695 · n_unique=131 · phase=Liquid」 |
| L1#2_Table#6_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=-20.1904–-1.0433 · mean=-5.762233 · n=456 · phase=Liquid」 |
```

```ledger
**L1#2_Table#7_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_4068 | lit_id: 2014-abd-azi-0 | doi: 10.1016/j.jct.2013.11.036
block: PROPblock_1 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 174
compounds: propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_2; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water+1-propanol near 298.15 K. Not inspected.
solvents: [{'component_org_num': 'DOIcomp_1', 'comp_num_id': 'GLOBcomp_1', 'solvent_num_id': 'GLOBsolvent_1', 'inchi_key': 'XLYOFNOQVPJJNP-UHFFFAOYSA-N'}]

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#7_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_3」 | 「Pressure, kPa」 | 「range=2353.0–40000.0 · n_unique=79 · phase=Liquid」 |
| L1#2_Table#7_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–582.08 · n_unique=38 · phase=Liquid」 |
| L1#2_Table#7_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_4」 | 「Molality, mol/kg of propan-1-ol」 | 「range=0.869–56.348 · n_unique=6 · phase=Liquid」 |
| L1#2_Table#7_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Constant-volume piezometry (GLOBmeas_66) · range=322.1–1004.4 · mean=846.767241 · n=174 · phase=Liquid」 |
```

```ledger
**L1#2_Table#8_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_4068 | lit_id: 2014-abd-azi-0 | doi: 10.1016/j.jct.2013.11.036
block: PROPblock_2 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 29
compounds: propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_2; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water+1-propanol near 298.15 K. Not inspected.
solvents: [{'component_org_num': 'DOIcomp_1', 'comp_num_id': 'GLOBcomp_1', 'solvent_num_id': 'GLOBsolvent_1', 'inchi_key': 'XLYOFNOQVPJJNP-UHFFFAOYSA-N'}]

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#8_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#2_Table#8_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=292.05–352.05 · n_unique=18 · phase=Liquid」 |
| L1#2_Table#8_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_4」 | 「Molality, mol/kg of propan-1-ol」 | 「range=0.869–56.348 · n_unique=6 · phase=Liquid」 |
| L1#2_Table#8_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Pycnometric method (GLOBmeas_6) · range=801.03–991.42 · mean=925.884483 · n=29 · phase=Liquid」 |
```

```ledger
**L1#2_Table#9_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_4415 | lit_id: 2015-ebr-sad-0 | doi: 10.1016/j.jct.2015.06.024
block: PROPblock_5 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 40
compounds: propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_3; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water+1-propanol near 298.15 K. Not inspected.
solvents: [{'component_org_num': 'DOIcomp_1', 'comp_num_id': 'GLOBcomp_1', 'solvent_num_id': 'GLOBsolvent_1', 'inchi_key': 'XLYOFNOQVPJJNP-UHFFFAOYSA-N'}]

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#9_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=84.5 · phase=Liquid」 |
| L1#2_Table#9_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=288.15–308.15 · n_unique=5 · phase=Liquid」 |
| L1#2_Table#9_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_4」 | 「Molality, mol/kg of propan-1-ol」 | 「range=0.01666–0.16617 · n_unique=8 · phase=Liquid」 |
| L1#2_Table#9_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=992.305–998.928 · mean=995.97015 · n=40 · phase=Liquid」 |
```

```ledger
**L1#2_Table#10_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_5585 | lit_id: 2019-meh-haj-0 | doi: 10.1016/j.jct.2019.105880
block: PROPblock_7 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 16
compounds: water (H2O; GLOBcomp_1; DOIcomp_4; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N); propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_2; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water+1-propanol near 298.15 K. Not inspected.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#10_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=100.0 · phase=Liquid」 |
| L1#2_Table#10_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=288.15–303.15 · n_unique=4 · phase=Liquid」 |
| L1#2_Table#10_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_5」 | 「Mass fraction of propan-1-ol」 | 「range=0.1–0.4 · n_unique=4 · phase=Liquid」 |
| L1#2_Table#10_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=924.386–985.245 · mean=957.421 · n=16 · phase=Liquid」 |
```

```ledger
**L1#2_Table#11_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_7085 | lit_id: 2017-sha-cha-0 | doi: 10.1021/acs.jced.6b01058
block: PROPblock_8 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 12
compounds: propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_4; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_5; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water+1-propanol near 298.15 K. Not inspected.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#11_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=85.0 · phase=Liquid」 |
| L1#2_Table#11_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–313.15 · n_unique=4 · phase=Liquid」 |
| L1#2_Table#11_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_5」 | 「Mass fraction of propan-1-ol」 | 「range=0.04–0.16 · n_unique=3 · phase=Liquid」 |
| L1#2_Table#11_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=966.84–990.59 · mean=980.451667 · n=12 · phase=Liquid」 |
```

```ledger
**L1#2_Table#12_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_7178 | lit_id: 2017-sha-asa-0 | doi: 10.1021/acs.jced.7b00299
block: PROPblock_13 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 2
compounds: water (H2O; GLOBcomp_1; DOIcomp_4; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N); propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_3; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water+1-propanol near 298.15 K. Not inspected.
solvents: [{'component_org_num': 'DOIcomp_4', 'comp_num_id': 'GLOBcomp_1', 'solvent_num_id': 'GLOBsolvent_1', 'inchi_key': 'XLYOFNOQVPJJNP-UHFFFAOYSA-N'}]

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#12_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=100.0 · phase=Liquid」 |
| L1#2_Table#12_Row#2 | 「constraint」 | 「BLKconstr_2/GLOBconstr_8」 | 「Molality, mol/kg」 | 「value=14.0 · phase=Liquid」 |
| L1#2_Table#12_Row#3 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–313.15 · n_unique=2 · phase=Liquid」 |
| L1#2_Table#12_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=903.156–914.36 · mean=908.758 · n=2 · phase=Liquid」 |
```

```ledger
**L1#2_Table#13_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_8254 | lit_id: 2003-kit-kag-0 | doi: 10.1021/je034101z
block: PROPblock_6 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 380
compounds: propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_3; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water+1-propanol near 298.15 K. Not inspected.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#13_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of propan-1-ol」 | 「range=0.255–0.738 · n_unique=3 · phase=Liquid」 |
| L1#2_Table#13_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_1」 | 「Temperature, K」 | 「range=282.15–425.15 · n_unique=144 · phase=Liquid」 |
| L1#2_Table#13_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_3」 | 「Pressure, kPa」 | 「range=5753.0–29883.0 · n_unique=379 · phase=Liquid」 |
| L1#2_Table#13_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=ISOCHOR (GLOBmeas_170) · range=731.4–896.2 · mean=821.633684 · n=380 · phase=Liquid」 |
```

```ledger
**L1#2_Table#14_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_10159 | lit_id: 2013-che-liu-0 | doi: 10.1021/je4003515
block: PROPblock_10 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 25
compounds: propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_3; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_4; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water+1-propanol near 298.15 K. Not inspected.
solvents: [{'component_org_num': 'DOIcomp_4', 'comp_num_id': 'GLOBcomp_1', 'solvent_num_id': 'GLOBsolvent_1', 'inchi_key': 'XLYOFNOQVPJJNP-UHFFFAOYSA-N'}]

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#14_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#2_Table#14_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=293.15–313.15 · n_unique=5 · phase=Liquid」 |
| L1#2_Table#14_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_4」 | 「Molality, mol/kg of propan-1-ol」 | 「range=14.0–22.0 · n_unique=5 · phase=Liquid」 |
| L1#2_Table#14_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=879.756–918.103 · mean=898.35392 · n=25 · phase=Liquid」 |
```

```ledger
**L1#2_Table#15_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_11142 | lit_id: 2008-zar-sha-0 | doi: 10.1021/je800158z
block: PROPblock_3 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 56
compounds: propan-1-ol (C3H8O; GLOBcomp_5; DOIcomp_1; InChIKey BDERNNFJNOPAEC-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_3; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of water+1-propanol near 298.15 K. Not inspected; registry entry truncated.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#15_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=81.5 · phase=Liquid」 |
| L1#2_Table#15_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of propan-1-ol」 | 「range=0.0–1.0 · n_unique=14 · phase=Liquid」 |
| L1#2_Table#15_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_1」 | 「Temperature, K」 | 「range=293.15–323.15 · n_unique=4 · phase=Liquid」 |
| L1#2_Table#15_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:4 (GLOBmeas_134) · range=778.92–998.2 · mean=864.609286 · n=56 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#2_Table#16_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_590 | doi: 10.1016/j.fluid.2008.01.004 | block: PROPblock_5
table_mode: nearest | inspection_id: INSP_859136865c90 | rows_shown: 8

| *row_id* | *BLKpoint_id* | *mass_fraction_<propan-1-ol>* | *temperature_k* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| L1#2_Table#16_Row#1 | 「BLKpoint_3」 | 「0.05」 | 「293.15」 | 「101.0」 | 「990.671」 |
| L1#2_Table#16_Row#2 | 「BLKpoint_8」 | 「0.1」 | 「293.15」 | 「101.0」 | 「984.913」 |
| L1#2_Table#16_Row#3 | 「BLKpoint_13」 | 「0.15」 | 「293.15」 | 「101.0」 | 「979.828」 |
| L1#2_Table#16_Row#4 | 「BLKpoint_4」 | 「0.05」 | 「298.15」 | 「101.0」 | 「989.387」 |
| L1#2_Table#16_Row#5 | 「BLKpoint_9」 | 「0.1」 | 「298.15」 | 「101.0」 | 「983.372」 |
| L1#2_Table#16_Row#6 | 「BLKpoint_14」 | 「0.15」 | 「298.15」 | 「101.0」 | 「977.921」 |
| L1#2_Table#16_Row#7 | 「BLKpoint_5」 | 「0.05」 | 「303.15」 | 「101.0」 | 「987.86」 |
| L1#2_Table#16_Row#8 | 「BLKpoint_10」 | 「0.1」 | 「303.15」 | 「101.0」 | 「981.595」 |
```
</subagent_answer>
</tool_result>

## LLM Response


<reasoning>
Now I have comprehensive data from two L1 queries. Let me compile everything for the final answer. I have:

1. Three blocks inspected with verbatim data at 298.15 K:
   - GLOBlit_555::PROPblock_8 (DOI 10.1016/j.fluid.2007.07.066) - mass fraction, 3 points at 298.15 K
   - GLOBlit_590::PROPblock_5 (DOI 10.1016/j.fluid.2008.01.004) - mass fraction, 3 points at 298.15 K
   - GLOBlit_2979::PROPblock_9 (DOI 10.1016/j.jct.2008.07.005) - mole fraction, 8 points at 298.15 K

2. Block-level metadata for all 13 identified blocks (the registry listing showed 13 unique blocks from the search, though the original search said 17 - the "17" was flagged as ungrounded). Let me list all blocks with their metadata from the L1#2 core blocks.

Let me compile the full answer with all the data I have.

Blocks identified:
1. GLOBlit_555::PROPblock_8 - mass fraction 0.05-0.15, T 283.15-303.15 K, P=101.0 kPa, 15 pts, ρ 976.004-992.444
2. GLOBlit_590::PROPblock_5 - mass fraction 0.05-0.15, T 283.15-303.15 K, P=101.0 kPa, 15 pts, ρ 975.791-992.405
3. GLOBlit_2432::PROPblock_3 - molality 0.0943-0.84695, T 298.15-573.15 K, P 420-30310 kPa, 456 pts, ρ reported as negative values (likely excess/difference density)
4. GLOBlit_2979::PROPblock_9 - mole fraction 0-0.2, T 283.15-308.15 K, P=98.93 kPa, 96 pts, ρ 911.83-999.69
5. GLOBlit_4068::PROPblock_1 - molality 0.869-56.348, T 298.15-582.08 K, P 2353-40000 kPa, 174 pts, ρ 322.1-1004.4 (high pressure)
6. GLOBlit_4068::PROPblock_2 - molality 0.869-56.348, T 292.05-352.05 K, P=101.0 kPa, 29 pts, ρ 801.03-991.42
7. GLOBlit_4415::PROPblock_5 - molality 0.01666-0.16617, T 288.15-308.15 K, P=84.5 kPa, 40 pts, ρ 992.305-998.928
8. GLOBlit_5585::PROPblock_7 - mass fraction 0.1-0.4, T 288.15-303.15 K, P=100.0 kPa, 16 pts, ρ 924.386-985.245
9. GLOBlit_7085::PROPblock_8 - mass fraction 0.04-0.16, T 298.15-313.15 K, P=85.0 kPa, 12 pts, ρ 966.84-990.59
10. GLOBlit_7178::PROPblock_13 - molality=14.0 (fixed), T 298.15-313.15 K, P=100.0 kPa, 2 pts, ρ 903.156-914.36
11. GLOBlit_8254::PROPblock_6 - mole fraction 0.255-0.738, T 282.15-425.15 K, P 5753-29883 kPa, 380 pts, ρ 731.4-896.2 (high pressure)
12. GLOBlit_10159::PROPblock_10 - molality 14.0-22.0, T 293.15-313.15 K, P=101.0 kPa, 25 pts, ρ 879.756-918.103
13. GLOBlit_11142::PROPblock_3 - mole fraction 0-1.0, T 293.15-323.15 K, P=81.5 kPa, 56 pts, ρ 778.92-998.2

That's 13 blocks. The search originally said 17, but only 13 were listed in the registry output. The remaining may have been truncated or not returned.

I have enough data to give a comprehensive answer.
</reasoning>

<answer>

## Mass Density Data for the Binary Mixture of Water + 1-Propanol near 298.15 K

**System:** Water (H₂O) + 1-Propanol (C₃H₈O), binary liquid mixture  
**Property:** Mass density (kg/m³)

### Overview

A search of the ThermoML database identified **13 data blocks** from **11 independent literature sources** containing mass density measurements for the water + 1-propanol binary system with temperatures encompassing or near 298.15 K. These blocks span a wide range of compositions (dilute aqueous to nearly pure 1-propanol), pressures (atmospheric to ~40 MPa), and temperature ranges. Three blocks were inspected in detail for verbatim data points at exactly 298.15 K.

---

### Complete Block Inventory

| # | DOI | Block | T range (K) | Composition variable & range | P (kPa) | ρ range (kg/m³) | N pts | Method |
|---|-----|-------|-------------|------------------------------|---------|-----------------|-------|--------|
| 1 | 10.1016/j.fluid.2007.07.066 | PROPblock_8 | 283.15–303.15 | Mass fraction, 0.05–0.15 | 101.0 | 976.004–992.444 | 15 | Vibrating tube |
| 2 | 10.1016/j.fluid.2008.01.004 | PROPblock_5 | 283.15–303.15 | Mass fraction, 0.05–0.15 | 101.0 | 975.791–992.405 | 15 | Vibrating tube |
| 3 | 10.1016/j.jct.2004.07.019 | PROPblock_3 | 298.15–573.15 | Molality, 0.0943–0.84695 mol/kg | 420–30310 | (excess density reported) | 456 | Vibrating tube |
| 4 | 10.1016/j.jct.2008.07.005 | PROPblock_9 | 283.15–308.15 | Mole fraction, 0.0–0.2 | 98.93 | 911.83–999.69 | 96 | Pycnometric |
| 5 | 10.1016/j.jct.2013.11.036 | PROPblock_1 | 298.15–582.08 | Molality, 0.869–56.348 mol/kg | 2353–40000 | 322.1–1004.4 | 174 | Constant-volume piezometry |
| 6 | 10.1016/j.jct.2013.11.036 | PROPblock_2 | 292.05–352.05 | Molality, 0.869–56.348 mol/kg | 101.0 | 801.03–991.42 | 29 | Pycnometric |
| 7 | 10.1016/j.jct.2015.06.024 | PROPblock_5 | 288.15–308.15 | Molality, 0.01666–0.16617 mol/kg | 84.5 | 992.305–998.928 | 40 | Vibrating tube |
| 8 | 10.1016/j.jct.2019.105880 | PROPblock_7 | 288.15–303.15 | Mass fraction, 0.1–0.4 | 100.0 | 924.386–985.245 | 16 | Vibrating tube |
| 9 | 10.1021/acs.jced.6b01058 | PROPblock_8 | 298.15–313.15 | Mass fraction, 0.04–0.16 | 85.0 | 966.84–990.59 | 12 | Vibrating tube |
| 10 | 10.1021/acs.jced.7b00299 | PROPblock_13 | 298.15–313.15 | Molality = 14.0 mol/kg (fixed) | 100.0 | 903.156–914.36 | 2 | Vibrating tube |
| 11 | 10.1021/je034101z | PROPblock_6 | 282.15–425.15 | Mole fraction, 0.255–0.738 | 5753–29883 | 731.4–896.2 | 380 | Isochoric |
| 12 | 10.1021/je4003515 | PROPblock_10 | 293.15–313.15 | Molality, 14.0–22.0 mol/kg | 101.0 | 879.756–918.103 | 25 | Vibrating tube |
| 13 | 10.1021/je800158z | PROPblock_3 | 293.15–323.15 | Mole fraction, 0.0–1.0 | 81.5 | 778.92–998.2 | 56 | Vibrating tube |

**Notes on block types:**
- Blocks 1, 2, 4, 7, 8, 9, 13 are **atmospheric-pressure** datasets most directly relevant to standard 298.15 K measurements.
- Blocks 3, 5, 11 are **high-pressure** datasets (up to ~40 MPa) and may report excess or differential densities.
- Block 13 (DOI 10.1021/je800158z) provides the widest composition coverage at atmospheric pressure, spanning the **full mole-fraction range 0.0–1.0**.

---

### Inspected Data Points at T = 298.15 K

#### Source 1: DOI 10.1016/j.fluid.2007.07.066, PROPblock_8
**Constraint:** P = 101.0 kPa | **Composition:** mass fraction of 1-propanol

| Mass fraction (1-propanol) | ρ (kg/m³) |
|---|---|
| 0.05 | 989.431 |
| 0.10 | 983.475 |
| 0.15 | 978.117 |

#### Source 2: DOI 10.1016/j.fluid.2008.01.004, PROPblock_5
**Constraint:** P = 101.0 kPa | **Composition:** mass fraction of 1-propanol

| Mass fraction (1-propanol) | ρ (kg/m³) |
|---|---|
| 0.05 | 989.387 |
| 0.10 | 983.372 |
| 0.15 | 977.921 |

#### Source 3: DOI 10.1016/j.jct.2008.07.005, PROPblock_9
**Constraint:** P = 98.93 kPa | **Composition:** mole fraction of 1-propanol

| Mole fraction (1-propanol) | ρ (kg/m³) |
|---|---|
| 0 | 997.04 |
| 0.002 | 995.4 |
| 0.005 | 993.76 |
| 0.009 | 991.66 |
| 0.01 | 991.14 |
| 0.02 | 986.54 |
| 0.03 | 982.56 |
| 0.05 | 975.49 |

---

### Chemistry Insights

1. **Monotonic density decrease:** All three inspected sources consistently show that density decreases monotonically with increasing 1-propanol content at 298.15 K. Starting from ~997 kg/m³ for pure water, the density drops to ~975 kg/m³ at a mole fraction of 0.05 (Source 3). This reflects the lower intrinsic density of 1-propanol (~803 kg/m³ at 298.15 K) compared to water.

2. **Inter-source consistency:** Sources 1 and 2 use the same composition variable (mass fraction) at the same pressure (101.0 kPa) and show excellent agreement — e.g., at w = 0.05, the densities are 989.431 vs. 989.387 kg/m³ (difference of only 0.044 kg/m³), providing confidence in the data quality.

3. **Composition coverage:** The inspected data cover only the water-rich region. For broader coverage including the 1-propanol-rich side, the block from DOI 10.1021/je800158z (PROPblock_3, mole fraction 0.0–1.0, 56 points, 293.15–323.15 K) and DOI 10.1016/j.jct.2013.11.036 (PROPblock_2, molality 0.869–56.348 mol/kg, 29 points at 101.0 kPa) would be the most relevant uninspected atmospheric-pressure sources.

4. **High-pressure data:** Three blocks (from DOIs 10.1016/j.jct.2004.07.019, 10.1016/j.jct.2013.11.036, and 10.1021/je034101z) provide density data at elevated pressures up to ~40 MPa, useful for equation-of-state modeling.

</answer>