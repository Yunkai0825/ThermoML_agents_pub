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

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Search for viscosity data of ethanol + water mixtures at or near 2000 K → stored as L1_query_1 · validation: FLAGGED(5)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: no_results · validation: FLAGGED(5)

**Summary:** The ThermoML database contains no dynamic viscosity data for ethanol + water binary mixtures at or near 2000 K. Across 14 data blocks and 14 DOIs, all available viscosity data for this system are in the liquid phase, spanning 268.1 K to 618.2 K. The highest-temperature data come from GLOBlit_2092::PROPblock_4 (DOI: 10.1016/j.fluid.2017.09.005), reaching 618.2 K at elevated pressures of 20000–40000 kPa, with viscosities ranging from 3.1×10⁻⁵ to 1.34×10⁻⁴ Pa·s. At 2000 K both ethanol and water would be far above their critical temperatures, making conventional liquid-phase viscosity measurements physically inapplicable, which explains the absence of such data in the archive.

**Answer:**

**Viscosity data for ethanol + water mixtures near 2000 K: Not found**

The ThermoML database contains **no dynamic viscosity data** for ethanol + water binary mixtures at or near 2000 K.

##### What data does exist

A search for dynamic viscosity (η, Pa·s) of ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary mixtures returned **14 data blocks across 14 DOIs**, all in the **liquid phase**. The overall temperature range covered is **268.1 K to 618.2 K** — far below 2000 K.

**Representative data blocks spanning the temperature extremes:**

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *DOI* | *Literature ID* | *Block* | *T range (K)* | *Composition variable* | *η range (Pa·s)* | *Points* |
|---|---|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「10.1016/j.fluid.2017.09.005」 | 「GLOBlit_2092」 | 「PROPblock_4」 | 「523.2–618.2」 | 「x(ethanol) 0–1」 | 「3.1×10⁻⁵ – 1.34×10⁻⁴」 | 「72」 |
| WM_L1#1_Table#1_Row#2 | 「10.1016/j.fluid.2015.07.012」 | 「GLOBlit_1742」 | 「PROPblock_4」 | 「350.7–476.2」 | 「x(ethanol) 0.1–1」 | 「1.07×10⁻⁴ – 7.37×10⁻⁴」 | 「84」 |
| WM_L1#1_Table#1_Row#3 | 「10.1016/j.jct.2007.05.004」 | 「GLOBlit_2825」 | 「PROPblock_11」 | 「293.15–303.15」 | 「x(water) 0–1」 | 「7.97×10⁻⁴ – 2.705×10⁻³」 | 「37」 |

The **highest temperature** with viscosity data in this system is **618.2 K**, from GLOBlit_2092::PROPblock_4 (DOI: 10.1016/j.fluid.2017.09.005). Some example data points from that block at 618.2 K:

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *T (K)* | *P (kPa)* | *x(ethanol)* | *η (Pa·s)* | *Source* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「618.2」 | 「20000」 | 「0」 | 「7.2×10⁻⁵」 | 「GLOBlit_2092::PROPblock_4」 |
| WM_L1#1_Table#2_Row#2 | 「618.2」 | 「20000」 | 「0.2」 | 「3.5×10⁻⁵」 | 「GLOBlit_2092::PROPblock_4」 |
| WM_L1#1_Table#2_Row#3 | 「618.2」 | 「20000」 | 「0.3」 | 「3.1×10⁻⁵」 | 「GLOBlit_2092::PROPblock_4」 |
| WM_L1#1_Table#2_Row#4 | 「618.2」 | 「20000」 | 「1」 | 「3.9×10⁻⁵」 | 「GLOBlit_2092::PROPblock_4」 |
| WM_L1#1_Table#2_Row#5 | 「618.2」 | 「40000」 | 「0」 | 「8.1×10⁻⁵」 | 「GLOBlit_2092::PROPblock_4」 |
| WM_L1#1_Table#2_Row#6 | 「618.2」 | 「40000」 | 「1」 | 「6.7×10⁻⁵」 | 「GLOBlit_2092::PROPblock_4」 |

Note that these high-temperature measurements were conducted at elevated pressures (20000–40000 kPa) to maintain a liquid or dense fluid phase.

##### Physical context

The highest-temperature viscosity data available (618.2 K, from GLOBlit_2092::PROPblock_4) is still approximately 1382 K below the requested 2000 K (derived: 2000 − 618.2 = 1382 K). At 2000 K, both ethanol and water would be well above their critical temperatures (general chemistry knowledge: ethanol T_b ≈ 351 K, T_c ≈ 514 K; water T_b ≈ 373 K, T_c ≈ 647 K — these are textbook reference values, not from this database). A conventional liquid-phase viscosity measurement of this mixture at 2000 K is not physically meaningful — both components would exist as supercritical fluids or decomposition products at that temperature. This explains the absence of such data in the ThermoML archive.

**Core claims:**
- The ThermoML database contains no dynamic viscosity data for ethanol + water binary mixtures at or near 2000 K, as all available measurements span 268.1 K to 618.2 K and both components would be well above their critical temperatures at 2000 K, making such measurements physically meaningless.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_2092」 | 「PROPblock_4」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water at 523.2–618.2 K and elevated pressures (20000–40000 kPa).」 |
| WM_L1#1_Table#4 | 「GLOBlit_1742」 | 「PROPblock_4」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water at 350.7–476.2 K.」 |
| WM_L1#1_Table#5 | 「GLOBlit_2825」 | 「PROPblock_11」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_4」 | 「Dynamic viscosity of ethanol + water at 293.15–303.15 K.」 |

*Not stored here: 3 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(5) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **MISATTRIBUTED_VALUE** PROPblock_11: 618.2 does not belong to PROPblock_11; it matches only GLOBlit_2092::PROPblock_4 (inspected this run)
- **UNGROUNDED_LITERAL** GLOBlit_2092::PROPblock_4: 1382 (near '…:: ) is still approximately 1382 K below the requested 2000 …') matches no inspected row/stat, database table, or other source of GLOBlit_2092::PROPblock_4
- **UNGROUNDED_LITERAL** GLOBlit_2092::PROPblock_4: 1382 (near '…1382 K below the requested 2000 K (derived: 2000 - 618.2 = 1…') matches no inspected row/stat, database table, or other source of GLOBlit_2092::PROPblock_4
- **UNGROUNDED_LITERAL** GLOBlit_2092::PROPblock_4: 514 (near '…es (general chemistry knowledge: ethanol T_b ≈ 351 K, T_c ≈ …') matches no inspected row/stat, database table, or other source of GLOBlit_2092::PROPblock_4
- **UNGROUNDED_LITERAL** GLOBlit_2092::PROPblock_4: 647 (near '…ethanol T_b ≈ 351 K, T_c ≈ 514 K; water T_b ≈ 373 K, T_c ≈ 6…') matches no inspected row/stat, database table, or other source of GLOBlit_2092::PROPblock_4



</memory>

## User
What is the viscosity of ethanol + water mixtures at 2000 K?

## Assistant
<summary>User asks for viscosity of ethanol + water at 2000 K. This temperature is far above the boiling points of both components (~351 K and ~373 K), so liquid-phase data is physically impossible. Querying L1 to check if any data exists at or near this condition.</summary>
<tool_call>L1_query(instruction=Search for dynami…, id_catalog=, context=User is asking fo…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=no_results

**Summary:** The ThermoML database contains no dynamic viscosity data for ethanol + water binary mixtures at or near 2000 K. Across 14 data blocks and 14 DOIs, all available viscosity data for this system are in the liquid phase, spanning 268.1 K to 618.2 K. The highest-temperature data come from GLOBlit_2092::PROPblock_4 (DOI: 10.1016/j.fluid.2017.09.005), reaching 618.2 K at elevated pressures of 20000–40000 kPa, with viscosities ranging from 3.1×10⁻⁵ to 1.34×10⁻⁴ Pa·s. At 2000 K both ethanol and water would be far above their critical temperatures, making conventional liquid-phase viscosity measurements physically inapplicable, which explains the absence of such data in the archive.

**Answer:**

**Viscosity data for ethanol + water mixtures near 2000 K: Not found**

The ThermoML database contains **no dynamic viscosity data** for ethanol + water binary mixtures at or near 2000 K.

##### What data does exist

A search for dynamic viscosity (η, Pa·s) of ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary mixtures returned **14 data blocks across 14 DOIs**, all in the **liquid phase**. The overall temperature range covered is **268.1 K to 618.2 K** — far below 2000 K.

**Representative data blocks spanning the temperature extremes:**

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *DOI* | *Literature ID* | *Block* | *T range (K)* | *Composition variable* | *η range (Pa·s)* | *Points* |
|---|---|---|---|---|---|---|---|
| L1#1_Table#1_Row#1 | 「10.1016/j.fluid.2017.09.005」 | 「GLOBlit_2092」 | 「PROPblock_4」 | 「523.2–618.2」 | 「x(ethanol) 0–1」 | 「3.1×10⁻⁵ – 1.34×10⁻⁴」 | 「72」 |
| L1#1_Table#1_Row#2 | 「10.1016/j.fluid.2015.07.012」 | 「GLOBlit_1742」 | 「PROPblock_4」 | 「350.7–476.2」 | 「x(ethanol) 0.1–1」 | 「1.07×10⁻⁴ – 7.37×10⁻⁴」 | 「84」 |
| L1#1_Table#1_Row#3 | 「10.1016/j.jct.2007.05.004」 | 「GLOBlit_2825」 | 「PROPblock_11」 | 「293.15–303.15」 | 「x(water) 0–1」 | 「7.97×10⁻⁴ – 2.705×10⁻³」 | 「37」 |

The **highest temperature** with viscosity data in this system is **618.2 K**, from GLOBlit_2092::PROPblock_4 (DOI: 10.1016/j.fluid.2017.09.005). Some example data points from that block at 618.2 K:

**L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *T (K)* | *P (kPa)* | *x(ethanol)* | *η (Pa·s)* | *Source* |
|---|---|---|---|---|---|
| L1#1_Table#2_Row#1 | 「618.2」 | 「20000」 | 「0」 | 「7.2×10⁻⁵」 | 「GLOBlit_2092::PROPblock_4」 |
| L1#1_Table#2_Row#2 | 「618.2」 | 「20000」 | 「0.2」 | 「3.5×10⁻⁵」 | 「GLOBlit_2092::PROPblock_4」 |
| L1#1_Table#2_Row#3 | 「618.2」 | 「20000」 | 「0.3」 | 「3.1×10⁻⁵」 | 「GLOBlit_2092::PROPblock_4」 |
| L1#1_Table#2_Row#4 | 「618.2」 | 「20000」 | 「1」 | 「3.9×10⁻⁵」 | 「GLOBlit_2092::PROPblock_4」 |
| L1#1_Table#2_Row#5 | 「618.2」 | 「40000」 | 「0」 | 「8.1×10⁻⁵」 | 「GLOBlit_2092::PROPblock_4」 |
| L1#1_Table#2_Row#6 | 「618.2」 | 「40000」 | 「1」 | 「6.7×10⁻⁵」 | 「GLOBlit_2092::PROPblock_4」 |

Note that these high-temperature measurements were conducted at elevated pressures (20000–40000 kPa) to maintain a liquid or dense fluid phase.

##### Physical context

The highest-temperature viscosity data available (618.2 K, from GLOBlit_2092::PROPblock_4) is still approximately 1382 K below the requested 2000 K (derived: 2000 − 618.2 = 1382 K). At 2000 K, both ethanol and water would be well above their critical temperatures (general chemistry knowledge: ethanol T_b ≈ 351 K, T_c ≈ 514 K; water T_b ≈ 373 K, T_c ≈ 647 K — these are textbook reference values, not from this database). A conventional liquid-phase viscosity measurement of this mixture at 2000 K is not physically meaningful — both components would exist as supercritical fluids or decomposition products at that temperature. This explains the absence of such data in the ThermoML archive.

---
[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:
- **MISATTRIBUTED_VALUE** PROPblock_11: 618.2 does not belong to PROPblock_11; it matches only GLOBlit_2092::PROPblock_4 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 618.2 to GLOBlit_2092::PROPblock_4 — no new tool call needed`
- **UNGROUNDED_LITERAL** GLOBlit_2092::PROPblock_4: 1382 (near '…:: ) is still approximately 1382 K below the requested 2000 …') matches no inspected row/stat, database table, or other source of GLOBlit_2092::PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_2092::PROPblock_4", nearest={"column": "temperature_k", "value": 1382.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** GLOBlit_2092::PROPblock_4: 1382 (near '…1382 K below the requested 2000 K (derived: 2000 - 618.2 = 1…') matches no inspected row/stat, database table, or other source of GLOBlit_2092::PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_2092::PROPblock_4", nearest={"column": "temperature_k", "value": 1382.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** GLOBlit_2092::PROPblock_4: 514 (near '…es (general chemistry knowledge: ethanol T_b ≈ 351 K, T_c ≈ …') matches no inspected row/stat, database table, or other source of GLOBlit_2092::PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_2092::PROPblock_4", nearest={"column": "temperature_k", "value": 514.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** GLOBlit_2092::PROPblock_4: 647 (near '…ethanol T_b ≈ 351 K, T_c ≈ 514 K; water T_b ≈ 373 K, T_c ≈ 6…') matches no inspected row/stat, database table, or other source of GLOBlit_2092::PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_2092::PROPblock_4", nearest={"column": "temperature_k", "value": 647.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
Inspected so far: PROPblock_11, PROPblock_4

**Core claims:**
- The ThermoML database contains no dynamic viscosity data for ethanol + water binary mixtures at or near 2000 K, as all available measurements span 268.1 K to 618.2 K and both components would be well above their critical temperatures at 2000 K, making such measurements physically meaningless.

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#3_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_2092 | lit_id: 2017-ono-kyo-0 | doi: 10.1016/j.fluid.2017.09.005
block: PROPblock_4 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 72
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_3; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity of ethanol + water at 523.2–618.2 K and elevated pressures (20000–40000 kPa).

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#3_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=523.2–618.2 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#3_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_3」 | 「Pressure, kPa」 | 「range=20000.0–40000.0 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#3_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0–1.0 · n_unique=8 · phase=Liquid」 |
| L1#1_Table#3_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=Capillary tube (Ostwald; Ubbelohde) method (GLOBmeas_4) · range=3.1e-05–0.000134 · mean=8.4e-05 · n=72 · phase=Liquid」 |
```

```ledger
**L1#1_Table#4_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_1742 | lit_id: 2016-ono-ame-0 | doi: 10.1016/j.fluid.2015.07.012
block: PROPblock_4 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 84
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_3; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity of ethanol + water at 350.7–476.2 K.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#4_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=350.7–476.2 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#4_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_3」 | 「Pressure, kPa」 | 「range=10000.0–40000.0 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#4_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.1–1.0 · n_unique=7 · phase=Liquid」 |
| L1#1_Table#4_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=Capillary tube (Ostwald; Ubbelohde) method (GLOBmeas_4) · range=0.000107–0.000737 · mean=0.000403 · n=84 · phase=Liquid」 |
```

```ledger
**L1#1_Table#5_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_2825 | lit_id: 2007-gon-cal-1 | doi: 10.1016/j.jct.2007.05.004
block: PROPblock_11 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 37
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_3; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity of ethanol + water at 293.15–303.15 K.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#5_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#5_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=293.15–303.15 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#5_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of water」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#1_Table#5_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=CAPTUB:UFactor:2 (GLOBmeas_140) · range=0.000797–0.002705 · mean=0.001607 · n=37 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#6_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_2092 | doi: 10.1016/j.fluid.2017.09.005 | block: PROPblock_4
table_mode: rdp | inspection_id: INSP_987176e5cf18 | rows_shown: 37

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mole_fraction_<ethanol>* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| L1#1_Table#6_Row#1 | 「BLKpoint_1」 | 「523.2」 | 「20000」 | 「0」 | 「0.00011」 |
| L1#1_Table#6_Row#2 | 「BLKpoint_2」 | 「523.2」 | 「20000」 | 「0.1」 | 「0.00012」 |
| L1#1_Table#6_Row#3 | 「BLKpoint_3」 | 「523.2」 | 「20000」 | 「0.2」 | 「0.000119」 |
| L1#1_Table#6_Row#4 | 「BLKpoint_6」 | 「523.2」 | 「20000」 | 「0.6」 | 「9.9e-05」 |
| L1#1_Table#6_Row#5 | 「BLKpoint_8」 | 「523.2」 | 「20000」 | 「1」 | 「8.7e-05」 |
| L1#1_Table#6_Row#6 | 「BLKpoint_9」 | 「523.2」 | 「30000」 | 「0」 | 「0.000113」 |
| L1#1_Table#6_Row#7 | 「BLKpoint_10」 | 「523.2」 | 「30000」 | 「0.1」 | 「0.000126」 |
| L1#1_Table#6_Row#8 | 「BLKpoint_11」 | 「523.2」 | 「30000」 | 「0.2」 | 「0.000127」 |
| L1#1_Table#6_Row#9 | 「BLKpoint_16」 | 「523.2」 | 「30000」 | 「1」 | 「0.000103」 |
| L1#1_Table#6_Row#10 | 「BLKpoint_17」 | 「523.2」 | 「40000」 | 「0」 | 「0.000115」 |
| L1#1_Table#6_Row#11 | 「BLKpoint_18」 | 「523.2」 | 「40000」 | 「0.1」 | 「0.000132」 |
| L1#1_Table#6_Row#12 | 「BLKpoint_20」 | 「523.2」 | 「40000」 | 「0.3」 | 「0.000134」 |
| L1#1_Table#6_Row#13 | 「BLKpoint_21」 | 「523.2」 | 「40000」 | 「0.4」 | 「0.000128」 |
| L1#1_Table#6_Row#14 | 「BLKpoint_24」 | 「523.2」 | 「40000」 | 「1」 | 「0.000115」 |
| L1#1_Table#6_Row#15 | 「BLKpoint_25」 | 「573.2」 | 「20000」 | 「0」 | 「9e-05」 |
| L1#1_Table#6_Row#16 | 「BLKpoint_28」 | 「573.2」 | 「20000」 | 「0.3」 | 「7e-05」 |
| L1#1_Table#6_Row#17 | 「BLKpoint_30」 | 「573.2」 | 「20000」 | 「0.6」 | 「5.7e-05」 |
| L1#1_Table#6_Row#18 | 「BLKpoint_32」 | 「573.2」 | 「20000」 | 「1」 | 「5.3e-05」 |
| L1#1_Table#6_Row#19 | 「BLKpoint_33」 | 「573.2」 | 「30000」 | 「0」 | 「9.3e-05」 |
| L1#1_Table#6_Row#20 | 「BLKpoint_38」 | 「573.2」 | 「30000」 | 「0.6」 | 「6.9e-05」 |
| L1#1_Table#6_Row#21 | 「BLKpoint_40」 | 「573.2」 | 「30000」 | 「1」 | 「6.6e-05」 |
| L1#1_Table#6_Row#22 | 「BLKpoint_41」 | 「573.2」 | 「40000」 | 「0」 | 「9.6e-05」 |
| L1#1_Table#6_Row#23 | 「BLKpoint_46」 | 「573.2」 | 「40000」 | 「0.6」 | 「8e-05」 |
| L1#1_Table#6_Row#24 | 「BLKpoint_48」 | 「573.2」 | 「40000」 | 「1」 | 「7.7e-05」 |
| L1#1_Table#6_Row#25 | 「BLKpoint_49」 | 「618.2」 | 「20000」 | 「0」 | 「7.2e-05」 |
| L1#1_Table#6_Row#26 | 「BLKpoint_51」 | 「618.2」 | 「20000」 | 「0.2」 | 「3.5e-05」 |
| L1#1_Table#6_Row#27 | 「BLKpoint_52」 | 「618.2」 | 「20000」 | 「0.3」 | 「3.1e-05」 |
| L1#1_Table#6_Row#28 | 「BLKpoint_56」 | 「618.2」 | 「20000」 | 「1」 | 「3.9e-05」 |
| L1#1_Table#6_Row#29 | 「BLKpoint_57」 | 「618.2」 | 「30000」 | 「0」 | 「7.7e-05」 |
| L1#1_Table#6_Row#30 | 「BLKpoint_60」 | 「618.2」 | 「30000」 | 「0.3」 | 「5.9e-05」 |
| L1#1_Table#6_Row#31 | 「BLKpoint_62」 | 「618.2」 | 「30000」 | 「0.6」 | 「5.5e-05」 |
| L1#1_Table#6_Row#32 | 「BLKpoint_64」 | 「618.2」 | 「30000」 | 「1」 | 「5.5e-05」 |
| L1#1_Table#6_Row#33 | 「BLKpoint_65」 | 「618.2」 | 「40000」 | 「0」 | 「8.1e-05」 |
| L1#1_Table#6_Row#34 | 「BLKpoint_66」 | 「618.2」 | 「40000」 | 「0.1」 | 「8.1e-05」 |
| L1#1_Table#6_Row#35 | 「BLKpoint_69」 | 「618.2」 | 「40000」 | 「0.4」 | 「7e-05」 |
| L1#1_Table#6_Row#36 | 「BLKpoint_70」 | 「618.2」 | 「40000」 | 「0.6」 | 「6.7e-05」 |
| L1#1_Table#6_Row#37 | 「BLKpoint_72」 | 「618.2」 | 「40000」 | 「1」 | 「6.7e-05」 |
```

```ledger
**L1#1_Table#7_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_1742 | doi: 10.1016/j.fluid.2015.07.012 | block: PROPblock_4
table_mode: rdp | inspection_id: INSP_2bf04912dbc3 | rows_shown: 42

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mole_fraction_<ethanol>* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| L1#1_Table#7_Row#1 | 「BLKpoint_1」 | 「350.7」 | 「10000」 | 「0.1」 | 「0.000537」 |
| L1#1_Table#7_Row#2 | 「BLKpoint_2」 | 「350.7」 | 「10000」 | 「0.2」 | 「0.000625」 |
| L1#1_Table#7_Row#3 | 「BLKpoint_4」 | 「350.7」 | 「10000」 | 「0.4」 | 「0.00064」 |
| L1#1_Table#7_Row#4 | 「BLKpoint_5」 | 「350.7」 | 「10000」 | 「0.6」 | 「0.000595」 |
| L1#1_Table#7_Row#5 | 「BLKpoint_7」 | 「350.7」 | 「10000」 | 「1」 | 「0.000461」 |
| L1#1_Table#7_Row#6 | 「BLKpoint_8」 | 「350.7」 | 「20000」 | 「0.1」 | 「0.000546」 |
| L1#1_Table#7_Row#7 | 「BLKpoint_9」 | 「350.7」 | 「20000」 | 「0.2」 | 「0.000638」 |
| L1#1_Table#7_Row#8 | 「BLKpoint_11」 | 「350.7」 | 「20000」 | 「0.4」 | 「0.000669」 |
| L1#1_Table#7_Row#9 | 「BLKpoint_14」 | 「350.7」 | 「20000」 | 「1」 | 「0.000518」 |
| L1#1_Table#7_Row#10 | 「BLKpoint_15」 | 「350.7」 | 「30000」 | 「0.1」 | 「0.000556」 |
| L1#1_Table#7_Row#11 | 「BLKpoint_16」 | 「350.7」 | 「30000」 | 「0.2」 | 「0.000651」 |
| L1#1_Table#7_Row#12 | 「BLKpoint_18」 | 「350.7」 | 「30000」 | 「0.4」 | 「0.000691」 |
| L1#1_Table#7_Row#13 | 「BLKpoint_21」 | 「350.7」 | 「30000」 | 「1」 | 「0.000555」 |
| L1#1_Table#7_Row#14 | 「BLKpoint_22」 | 「350.7」 | 「40000」 | 「0.1」 | 「0.000578」 |
| L1#1_Table#7_Row#15 | 「BLKpoint_23」 | 「350.7」 | 「40000」 | 「0.2」 | 「0.000681」 |
| L1#1_Table#7_Row#16 | 「BLKpoint_24」 | 「350.7」 | 「40000」 | 「0.3」 | 「0.000726」 |
| L1#1_Table#7_Row#17 | 「BLKpoint_25」 | 「350.7」 | 「40000」 | 「0.4」 | 「0.000737」 |
| L1#1_Table#7_Row#18 | 「BLKpoint_28」 | 「350.7」 | 「40000」 | 「1」 | 「0.00059」 |
| L1#1_Table#7_Row#19 | 「BLKpoint_29」 | 「373.2」 | 「10000」 | 「0.1」 | 「0.000401」 |
| L1#1_Table#7_Row#20 | 「BLKpoint_30」 | 「373.2」 | 「10000」 | 「0.2」 | 「0.000448」 |
| L1#1_Table#7_Row#21 | 「BLKpoint_32」 | 「373.2」 | 「10000」 | 「0.4」 | 「0.000462」 |
| L1#1_Table#7_Row#22 | 「BLKpoint_34」 | 「373.2」 | 「10000」 | 「0.8」 | 「0.000381」 |
| L1#1_Table#7_Row#23 | 「BLKpoint_35」 | 「373.2」 | 「10000」 | 「1」 | 「0.000364」 |
| L1#1_Table#7_Row#24 | 「BLKpoint_36」 | 「373.2」 | 「20000」 | 「0.1」 | 「0.000397」 |
| L1#1_Table#7_Row#25 | 「BLKpoint_37」 | 「373.2」 | 「20000」 | 「0.2」 | 「0.000449」 |
| L1#1_Table#7_Row#26 | 「BLKpoint_39」 | 「373.2」 | 「20000」 | 「0.4」 | 「0.000477」 |
| L1#1_Table#7_Row#27 | 「BLKpoint_42」 | 「373.2」 | 「20000」 | 「1」 | 「0.000382」 |
| L1#1_Table#7_Row#28 | 「BLKpoint_43」 | 「373.2」 | 「30000」 | 「0.1」 | 「0.000403」 |
| L1#1_Table#7_Row#29 | 「BLKpoint_44」 | 「373.2」 | 「30000」 | 「0.2」 | 「0.000459」 |
| L1#1_Table#7_Row#30 | 「BLKpoint_46」 | 「373.2」 | 「30000」 | 「0.4」 | 「0.000489」 |
| L1#1_Table#7_Row#31 | 「BLKpoint_49」 | 「373.2」 | 「30000」 | 「1」 | 「0.000404」 |
| L1#1_Table#7_Row#32 | 「BLKpoint_50」 | 「373.2」 | 「40000」 | 「0.1」 | 「0.000421」 |
| L1#1_Table#7_Row#33 | 「BLKpoint_52」 | 「373.2」 | 「40000」 | 「0.3」 | 「0.000515」 |
| L1#1_Table#7_Row#34 | 「BLKpoint_56」 | 「373.2」 | 「40000」 | 「1」 | 「0.000443」 |
| L1#1_Table#7_Row#35 | 「BLKpoint_57」 | 「476.2」 | 「10000」 | 「0.1」 | 「0.000148」 |
| L1#1_Table#7_Row#36 | 「BLKpoint_63」 | 「476.2」 | 「10000」 | 「1」 | 「0.000107」 |
| L1#1_Table#7_Row#37 | 「BLKpoint_64」 | 「476.2」 | 「20000」 | 「0.1」 | 「0.000152」 |
| L1#1_Table#7_Row#38 | 「BLKpoint_70」 | 「476.2」 | 「20000」 | 「1」 | 「0.000123」 |
| L1#1_Table#7_Row#39 | 「BLKpoint_71」 | 「476.2」 | 「30000」 | 「0.1」 | 「0.000159」 |
| L1#1_Table#7_Row#40 | 「BLKpoint_77」 | 「476.2」 | 「30000」 | 「1」 | 「0.000138」 |
| L1#1_Table#7_Row#41 | 「BLKpoint_78」 | 「476.2」 | 「40000」 | 「0.1」 | 「0.000164」 |
| L1#1_Table#7_Row#42 | 「BLKpoint_84」 | 「476.2」 | 「40000」 | 「1」 | 「0.000151」 |
```

```ledger
**L1#1_Table#8_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_2825 | doi: 10.1016/j.jct.2007.05.004 | block: PROPblock_11
table_mode: rdp | inspection_id: INSP_78cce36f2f6f | rows_shown: 17

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<water>* | *pressure_kpa* | *viscosity_pa_s* |
|---|---|---|---|---|---|
| L1#1_Table#8_Row#1 | 「BLKpoint_1」 | 「293.15」 | 「0」 | 「101.0」 | 「0.001187」 |
| L1#1_Table#8_Row#2 | 「BLKpoint_5」 | 「293.15」 | 「0.2961」 | 「101.0」 | 「0.001735」 |
| L1#1_Table#8_Row#3 | 「BLKpoint_9」 | 「293.15」 | 「0.6991」 | 「101.0」 | 「0.002705」 |
| L1#1_Table#8_Row#4 | 「BLKpoint_10」 | 「293.15」 | 「0.8001」 | 「101.0」 | 「0.0027」 |
| L1#1_Table#8_Row#5 | 「BLKpoint_11」 | 「293.15」 | 「0.8996」 | 「101.0」 | 「0.002223」 |
| L1#1_Table#8_Row#6 | 「BLKpoint_13」 | 「293.15」 | 「1」 | 「101.0」 | 「0.001002」 |
| L1#1_Table#8_Row#7 | 「BLKpoint_14」 | 「298.15」 | 「0」 | 「101.0」 | 「0.001082」 |
| L1#1_Table#8_Row#8 | 「BLKpoint_19」 | 「298.15」 | 「0.3991」 | 「101.0」 | 「0.001659」 |
| L1#1_Table#8_Row#9 | 「BLKpoint_21」 | 「298.15」 | 「0.6991」 | 「101.0」 | 「0.002275」 |
| L1#1_Table#8_Row#10 | 「BLKpoint_22」 | 「298.15」 | 「0.8001」 | 「101.0」 | 「0.0023」 |
| L1#1_Table#8_Row#11 | 「BLKpoint_23」 | 「298.15」 | 「0.8996」 | 「101.0」 | 「0.00186」 |
| L1#1_Table#8_Row#12 | 「BLKpoint_25」 | 「298.15」 | 「1」 | 「101.0」 | 「0.00089」 |
| L1#1_Table#8_Row#13 | 「BLKpoint_26」 | 「303.15」 | 「0」 | 「101.0」 | 「0.000987」 |
| L1#1_Table#8_Row#14 | 「BLKpoint_33」 | 「303.15」 | 「0.6991」 | 「101.0」 | 「0.001941」 |
| L1#1_Table#8_Row#15 | 「BLKpoint_34」 | 「303.15」 | 「0.8001」 | 「101.0」 | 「0.001937」 |
| L1#1_Table#8_Row#16 | 「BLKpoint_35」 | 「303.15」 | 「0.8996」 | 「101.0」 | 「0.00158」 |
| L1#1_Table#8_Row#17 | 「BLKpoint_37」 | 「303.15」 | 「1」 | 「101.0」 | 「0.000797」 |
```
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
The L1 query confirms there is no viscosity data for ethanol + water at 2000 K. The database only has data up to 618.2 K. I have all the information needed to give a complete answer.
</reasoning>

<answer>
**No data found in the ThermoML database for viscosity of ethanol + water mixtures at 2000 K.**

At 2000 K, both ethanol and water would be far above their critical temperatures and normal boiling points, so a conventional liquid-phase viscosity measurement is not physically meaningful — both components would exist as supercritical fluids or thermal decomposition products. This explains why no such data exist in the archive.

### What viscosity data *are* available for ethanol + water

The ThermoML database contains dynamic viscosity (η, Pa·s) data for ethanol + water binary mixtures across **14 data blocks from 14 publications**, but all measurements are in the **liquid phase** and span only **268.1 K to 618.2 K**.

#### Highest-temperature data: up to 618.2 K

The closest data to your requested temperature come from two studies that used elevated pressures to keep the mixture in a dense/liquid state:

| DOI | Literature ID | Block | T range (K) | P range (kPa) | x(ethanol) | η range (Pa·s) | Points |
|-----|---------------|-------|-------------|---------------|------------|----------------|--------|
| 10.1016/j.fluid.2017.09.005 | GLOBlit_2092 | PROPblock_4 | 523.2–618.2 | 20 000–40 000 | 0–1 | 3.1×10⁻⁵ – 1.34×10⁻⁴ | 72 |
| 10.1016/j.fluid.2015.07.012 | GLOBlit_1742 | PROPblock_4 | 350.7–476.2 | 10 000–40 000 | 0.1–1 | 1.07×10⁻⁴ – 7.37×10⁻⁴ | 84 |

**Selected data points at the highest available temperature (618.2 K)** from GLOBlit_2092 · PROPblock_4:

| T (K) | P (kPa) | x(ethanol) | η (Pa·s) |
|-------|---------|------------|----------|
| 618.2 | 20 000 | 0 | 7.2×10⁻⁵ |
| 618.2 | 20 000 | 0.2 | 3.5×10⁻⁵ |
| 618.2 | 20 000 | 0.3 | 3.1×10⁻⁵ |
| 618.2 | 20 000 | 1 | 3.9×10⁻⁵ |
| 618.2 | 40 000 | 0 | 8.1×10⁻⁵ |
| 618.2 | 40 000 | 1 | 6.7×10⁻⁵ |

#### Near-ambient data: 293–303 K

At more conventional conditions (atmospheric pressure), data from GLOBlit_2825 · PROPblock_11 (DOI: 10.1016/j.jct.2007.05.004) cover 293.15–303.15 K at 101 kPa, with viscosities ranging from 7.97×10⁻⁴ to 2.705×10⁻³ Pa·s across the full water mole-fraction range.

### Summary

The maximum temperature with viscosity data for this system in ThermoML is **618.2 K** — still far below 2000 K. No extrapolation to 2000 K is possible from these liquid-phase measurements, and no gas-phase or supercritical viscosity data for this mixture are present in the database.
</answer>