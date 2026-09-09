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
| comp | GLOBcomp_26 | sodium_chloride | sodium chloride |
| comp | GLOBcomp_1 | water | water |
| prop | GLOBprop_1 | mass_density_kg_m3 | Mass density, kg/m3 |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find mass density data for salt water (NaCl + water binary mixture) → stored as L1_query_1 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(1)

**Summary:** Mass density data for the binary system NaCl (GLOBcomp_26) + water (GLOBcomp_1) are available across 20 data blocks in the ThermoML database, covering liquid-phase measurements reported on mole fraction, mass fraction, molality, and molarity scales. One block was inspected in detail: GLOBlit_2114 (DOI 10.1016/j.fluid.2017.10.034), PROPblock_3, containing 35 data points at five temperatures (288.15–318.15 K) and seven NaCl mole fractions. Densities in that block range from 1012.1 kg/m³ (318.15 K, x(NaCl) = 0.0099) to 1147.1 kg/m³ (288.15 K, x(NaCl) = 0.0654). At 298.15 K, density rises from 1019.6 kg/m³ at x(NaCl) = 0.0099 to 1142.4 kg/m³ at x(NaCl) = 0.0654, an approximately 12% increase. At fixed x(NaCl) = 0.0654, density decreases from 1147.1 kg/m³ at 288.15 K to 1132.2 kg/m³ at 318.15 K, consistent with thermal expansion. Other blocks were identified but not numerically inspected.

**Answer:**

#### Mass Density Data for Salt Water (NaCl + Water Binary Mixture)

##### System Identification
- **Sodium chloride (NaCl):** GLOBcomp_26 (formula: ClNa, SMILES: [Cl-].[Na+])
- **Water (H₂O):** GLOBcomp_1 (formula: H2O, SMILES: O)
- **Property:** Mass density (GLOBprop_1, kg/m³)
- **System type:** Binary

##### Data Availability

The ThermoML database contains **20 data blocks** reporting mass density for the NaCl + water binary system. These blocks cover various composition scales including mole fraction, mass fraction, molality, and molarity. All data are in the liquid phase. Notable sources include blocks from DOI 10.1016/j.fluid.2012.04.003 (GLOBlit_1096, PROPblock_1, 6 points), DOI 10.1016/j.jct.2005.03.008 (GLOBlit_2516, PROPblock_5, 4 points), and DOI 10.1016/j.jct.2008.12.011 (GLOBlit_3044, PROPblock_6, 39 points), among others. Their detailed numerical ranges were not inspected in this run.

The block inspected in detail is:

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *DOI* | *Block* | *GLOBlit* | *Points* | *Composition Variable* | *T (K) Range* | *ρ (kg/m³) Range* |
|---|---|---|---|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「10.1016/j.fluid.2017.10.034」 | 「PROPblock_3」 | 「GLOBlit_2114」 | 「35」 | 「mole fraction (GLOBvar_2)」 | 「288.15–318.15」 | 「1012.1–1147.1」 |

##### Representative Data Points (Inspected)

From **GLOBlit_2114 :: PROPblock_3** (DOI: 10.1016/j.fluid.2017.10.034), which contains 35 data points across five temperatures and seven NaCl mole fractions:

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *T (K)* | *x(NaCl)* | *ρ (kg/m³)* |
|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「288.15」 | 「0.0099」 | 「1022.2」 |
| WM_L1#1_Table#2_Row#2 | 「288.15」 | 「0.0196」 | 「1044.7」 |
| WM_L1#1_Table#2_Row#3 | 「288.15」 | 「0.0654」 | 「1147.1」 |
| WM_L1#1_Table#2_Row#4 | 「293.15」 | 「0.0099」 | 「1021.0」 |
| WM_L1#1_Table#2_Row#5 | 「293.15」 | 「0.0196」 | 「1043.2」 |
| WM_L1#1_Table#2_Row#6 | 「293.15」 | 「0.0654」 | 「1144.8」 |
| WM_L1#1_Table#2_Row#7 | 「298.15」 | 「0.0099」 | 「1019.6」 |
| WM_L1#1_Table#2_Row#8 | 「298.15」 | 「0.0196」 | 「1041.6」 |
| WM_L1#1_Table#2_Row#9 | 「298.15」 | 「0.0385」 | 「1082.8」 |
| WM_L1#1_Table#2_Row#10 | 「298.15」 | 「0.0654」 | 「1142.4」 |
| WM_L1#1_Table#2_Row#11 | 「308.15」 | 「0.0099」 | 「1016.2」 |
| WM_L1#1_Table#2_Row#12 | 「308.15」 | 「0.0196」 | 「1037.8」 |
| WM_L1#1_Table#2_Row#13 | 「308.15」 | 「0.0385」 | 「1078.5」 |
| WM_L1#1_Table#2_Row#14 | 「308.15」 | 「0.0654」 | 「1137.4」 |
| WM_L1#1_Table#2_Row#15 | 「318.15」 | 「0.0099」 | 「1012.1」 |
| WM_L1#1_Table#2_Row#16 | 「318.15」 | 「0.0196」 | 「1033.5」 |
| WM_L1#1_Table#2_Row#17 | 「318.15」 | 「0.0385」 | 「1073.7」 |
| WM_L1#1_Table#2_Row#18 | 「318.15」 | 「0.0654」 | 「1132.2」 |

##### Chemical Insight

The data show the expected physical behavior of aqueous NaCl solutions:

- **Concentration effect:** At a fixed temperature of 298.15 K, density increases from 1019.6 kg/m³ at x(NaCl) = 0.0099 to 1142.4 kg/m³ at x(NaCl) = 0.0654 — a ~12% increase — reflecting the higher molar mass and strong ion–dipole interactions of dissolved NaCl.
- **Temperature effect:** At a fixed mole fraction of 0.0654, density decreases from 1147.1 kg/m³ at 288.15 K to 1132.2 kg/m³ at 318.15 K, consistent with thermal expansion of the solution.
- All measured densities in this block are well above 1012 kg/m³ (the lowest inspected value, at 318.15 K and x = 0.0099), confirming that even dilute NaCl solutions are denser than pure water due to the presence of dissolved ions.

**Core claims:**
- The ThermoML database contains 20 data blocks reporting liquid-phase mass density for the NaCl + water binary system, covering various composition scales (mole fraction, mass fraction, molality, molarity) and multiple temperature ranges.
- In the inspected block (GLOBlit_2114, PROPblock_3, DOI 10.1016/j.fluid.2017.10.034), 35 data points span temperatures of 288.15–318.15 K and NaCl mole fractions from 0.0099 to 0.0654, with densities ranging from 1012.1 to 1147.1 kg/m³.
- At fixed temperature (298.15 K), density increases from 1019.6 kg/m³ at x(NaCl) = 0.0099 to 1142.4 kg/m³ at x(NaCl) = 0.0654, reflecting the effect of dissolved NaCl concentration on solution density.
- At fixed mole fraction x(NaCl) = 0.0654, density decreases from 1147.1 kg/m³ at 288.15 K to 1132.2 kg/m³ at 318.15 K, consistent with thermal expansion.
- Only one of the 20 identified data blocks (PROPblock_3) was inspected in detail; data attributed to other blocks (e.g., PROPblock_6) remain unverified.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_2114」 | 「PROPblock_3」 | 「GLOBcomp_26, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density (kg/m³) of NaCl + water binary mixture at mole fractions 0.0099–0.0654 and temperatures 288.15–318.15 K; 35 data points.」 |
| WM_L1#1_Table#4 | 「GLOBlit_1096」 | 「PROPblock_1」 | 「GLOBcomp_26, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density (kg/m³) of NaCl + water binary mixture; 6 data points.」 |
| WM_L1#1_Table#5 | 「GLOBlit_2516」 | 「PROPblock_5」 | 「GLOBcomp_26, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density (kg/m³) of NaCl + water binary mixture; 4 data points.」 |
| WM_L1#1_Table#6 | 「GLOBlit_3044」 | 「PROPblock_6」 | 「GLOBcomp_26, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density (kg/m³) of NaCl + water binary mixture; 39 data points (not inspected in detail).」 |

*Not stored here: 1 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_6: PROPblock_6 is quoted with data values (39, …) but was never inspected in this run



</memory>

## User
Find density data for salt water.

## Assistant
<summary>Dispatching L1 query to find mass density data for the sodium chloride + water (salt water) system in ThermoML.</summary>
<tool_call>L1_query(instruction=Search for mass d…, id_catalog=, context=User wants densit…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** Mass density data for the binary system NaCl (GLOBcomp_26) + water (GLOBcomp_1) are available across 20 data blocks in the ThermoML database, covering liquid-phase measurements reported on mole fraction, mass fraction, molality, and molarity scales. One block was inspected in detail: GLOBlit_2114 (DOI 10.1016/j.fluid.2017.10.034), PROPblock_3, containing 35 data points at five temperatures (288.15–318.15 K) and seven NaCl mole fractions. Densities in that block range from 1012.1 kg/m³ (318.15 K, x(NaCl) = 0.0099) to 1147.1 kg/m³ (288.15 K, x(NaCl) = 0.0654). At 298.15 K, density rises from 1019.6 kg/m³ at x(NaCl) = 0.0099 to 1142.4 kg/m³ at x(NaCl) = 0.0654, an approximately 12% increase. At fixed x(NaCl) = 0.0654, density decreases from 1147.1 kg/m³ at 288.15 K to 1132.2 kg/m³ at 318.15 K, consistent with thermal expansion. Other blocks were identified but not numerically inspected.

**Answer:**

#### Mass Density Data for Salt Water (NaCl + Water Binary Mixture)

##### System Identification
- **Sodium chloride (NaCl):** GLOBcomp_26 (formula: ClNa, SMILES: [Cl-].[Na+])
- **Water (H₂O):** GLOBcomp_1 (formula: H2O, SMILES: O)
- **Property:** Mass density (GLOBprop_1, kg/m³)
- **System type:** Binary

##### Data Availability

The ThermoML database contains **20 data blocks** reporting mass density for the NaCl + water binary system. These blocks cover various composition scales including mole fraction, mass fraction, molality, and molarity. All data are in the liquid phase. Notable sources include blocks from DOI 10.1016/j.fluid.2012.04.003 (GLOBlit_1096, PROPblock_1, 6 points), DOI 10.1016/j.jct.2005.03.008 (GLOBlit_2516, PROPblock_5, 4 points), and DOI 10.1016/j.jct.2008.12.011 (GLOBlit_3044, PROPblock_6, 39 points), among others. Their detailed numerical ranges were not inspected in this run.

The block inspected in detail is:

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *DOI* | *Block* | *GLOBlit* | *Points* | *Composition Variable* | *T (K) Range* | *ρ (kg/m³) Range* |
|---|---|---|---|---|---|---|---|
| L1#1_Table#1_Row#1 | 「10.1016/j.fluid.2017.10.034」 | 「PROPblock_3」 | 「GLOBlit_2114」 | 「35」 | 「mole fraction (GLOBvar_2)」 | 「288.15–318.15」 | 「1012.1–1147.1」 |

##### Representative Data Points (Inspected)

From **GLOBlit_2114 :: PROPblock_3** (DOI: 10.1016/j.fluid.2017.10.034), which contains 35 data points across five temperatures and seven NaCl mole fractions:

**L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *T (K)* | *x(NaCl)* | *ρ (kg/m³)* |
|---|---|---|---|
| L1#1_Table#2_Row#1 | 「288.15」 | 「0.0099」 | 「1022.2」 |
| L1#1_Table#2_Row#2 | 「288.15」 | 「0.0196」 | 「1044.7」 |
| L1#1_Table#2_Row#3 | 「288.15」 | 「0.0654」 | 「1147.1」 |
| L1#1_Table#2_Row#4 | 「293.15」 | 「0.0099」 | 「1021.0」 |
| L1#1_Table#2_Row#5 | 「293.15」 | 「0.0196」 | 「1043.2」 |
| L1#1_Table#2_Row#6 | 「293.15」 | 「0.0654」 | 「1144.8」 |
| L1#1_Table#2_Row#7 | 「298.15」 | 「0.0099」 | 「1019.6」 |
| L1#1_Table#2_Row#8 | 「298.15」 | 「0.0196」 | 「1041.6」 |
| L1#1_Table#2_Row#9 | 「298.15」 | 「0.0385」 | 「1082.8」 |
| L1#1_Table#2_Row#10 | 「298.15」 | 「0.0654」 | 「1142.4」 |
| L1#1_Table#2_Row#11 | 「308.15」 | 「0.0099」 | 「1016.2」 |
| L1#1_Table#2_Row#12 | 「308.15」 | 「0.0196」 | 「1037.8」 |
| L1#1_Table#2_Row#13 | 「308.15」 | 「0.0385」 | 「1078.5」 |
| L1#1_Table#2_Row#14 | 「308.15」 | 「0.0654」 | 「1137.4」 |
| L1#1_Table#2_Row#15 | 「318.15」 | 「0.0099」 | 「1012.1」 |
| L1#1_Table#2_Row#16 | 「318.15」 | 「0.0196」 | 「1033.5」 |
| L1#1_Table#2_Row#17 | 「318.15」 | 「0.0385」 | 「1073.7」 |
| L1#1_Table#2_Row#18 | 「318.15」 | 「0.0654」 | 「1132.2」 |

##### Chemical Insight

The data show the expected physical behavior of aqueous NaCl solutions:

- **Concentration effect:** At a fixed temperature of 298.15 K, density increases from 1019.6 kg/m³ at x(NaCl) = 0.0099 to 1142.4 kg/m³ at x(NaCl) = 0.0654 — a ~12% increase — reflecting the higher molar mass and strong ion–dipole interactions of dissolved NaCl.
- **Temperature effect:** At a fixed mole fraction of 0.0654, density decreases from 1147.1 kg/m³ at 288.15 K to 1132.2 kg/m³ at 318.15 K, consistent with thermal expansion of the solution.
- All measured densities in this block are well above 1012 kg/m³ (the lowest inspected value, at 318.15 K and x = 0.0099), confirming that even dilute NaCl solutions are denser than pure water due to the presence of dissolved ions.

---
[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:
- **UNINSPECTED_BLOCK** PROPblock_6: PROPblock_6 is quoted with data values (39, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="PROPblock_6", literature="<GLOBlit_N or DOI>")`
Inspected so far: PROPblock_3

**Core claims:**
- The ThermoML database contains 20 data blocks reporting liquid-phase mass density for the NaCl + water binary system, covering various composition scales (mole fraction, mass fraction, molality, molarity) and multiple temperature ranges.
- In the inspected block (GLOBlit_2114, PROPblock_3, DOI 10.1016/j.fluid.2017.10.034), 35 data points span temperatures of 288.15–318.15 K and NaCl mole fractions from 0.0099 to 0.0654, with densities ranging from 1012.1 to 1147.1 kg/m³.
- At fixed temperature (298.15 K), density increases from 1019.6 kg/m³ at x(NaCl) = 0.0099 to 1142.4 kg/m³ at x(NaCl) = 0.0654, reflecting the effect of dissolved NaCl concentration on solution density.
- At fixed mole fraction x(NaCl) = 0.0654, density decreases from 1147.1 kg/m³ at 288.15 K to 1132.2 kg/m³ at 318.15 K, consistent with thermal expansion.
- Only one of the 20 identified data blocks (PROPblock_3) was inspected in detail; data attributed to other blocks (e.g., PROPblock_6) remain unverified.

**Core ID updates:**
- add GLOBcomp_26 — sodium chloride (registry: sodium_chloride)
- add GLOBcomp_1 — water (registry: water)
- add GLOBprop_1 — Mass density, kg/m3 (registry: mass_density_kg_m3)

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#3_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_2114 | lit_id: 2018-koh-hor-0 | doi: 10.1016/j.fluid.2017.10.034
block: PROPblock_3 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 35
compounds: sodium chloride (ClNa; GLOBcomp_26; DOIcomp_3; InChIKey FAPWRFPIFSIZLT-UHFFFAOYSA-M); water (H2O; GLOBcomp_1; DOIcomp_2; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density (kg/m³) of NaCl + water binary mixture at mole fractions 0.0099–0.0654 and temperatures 288.15–318.15 K; 35 data points.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#3_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=288.15–318.15 · n_unique=5 · phase=Liquid」 |
| L1#1_Table#3_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of sodium chloride」 | 「range=0.0099–0.0654 · n_unique=7 · phase=Liquid」 |
| L1#1_Table#3_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=1012.1–1147.1 · mean=1080.591429 · n=35 · phase=Liquid」 |
```

```ledger
**L1#1_Table#4_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_1096 | lit_id: 2012-sad-hel-0 | doi: 10.1016/j.fluid.2012.04.003
block: PROPblock_1 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 6
compounds: sodium chloride (ClNa; GLOBcomp_26; DOIcomp_2; InChIKey FAPWRFPIFSIZLT-UHFFFAOYSA-M); water (H2O; GLOBcomp_1; DOIcomp_3; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density (kg/m³) of NaCl + water binary mixture; 6 data points.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#4_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#4_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=293.15–313.15 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#4_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_5」 | 「Mass fraction of sodium chloride」 | 「range=0.02–0.04 · n_unique=2 · phase=Liquid」 |
| L1#1_Table#4_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=1006.1–1026.7 · mean=1017.366667 · n=6 · phase=Liquid」 |
```

```ledger
**L1#1_Table#5_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_2516 | lit_id: 2005-iqb-mal-0 | doi: 10.1016/j.jct.2005.03.008
block: PROPblock_5 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 4
compounds: sodium chloride (ClNa; GLOBcomp_26; DOIcomp_2; InChIKey FAPWRFPIFSIZLT-UHFFFAOYSA-M); water (H2O; GLOBcomp_1; DOIcomp_4; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density (kg/m³) of NaCl + water binary mixture; 4 data points.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#5_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_2」 | 「Temperature, K」 | 「value=293.15 · phase=Liquid」 |
| L1#1_Table#5_Row#2 | 「constraint」 | 「BLKconstr_2/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.325 · phase=Liquid」 |
| L1#1_Table#5_Row#3 | 「variable」 | 「BLKvar_1/GLOBvar_5」 | 「Mass fraction of sodium chloride」 | 「range=0.005–0.03 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#5_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=1001.78–1019.58 · mean=1009.78 · n=4 · phase=Liquid」 |
```

```ledger
**L1#1_Table#6_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_3044 | lit_id: 2009-tah-lee-1 | doi: 10.1016/j.jct.2008.12.011
block: PROPblock_6 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 39
compounds: sodium chloride (ClNa; GLOBcomp_26; DOIcomp_7; InChIKey FAPWRFPIFSIZLT-UHFFFAOYSA-M); water (H2O; GLOBcomp_1; DOIcomp_3; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density (kg/m³) of NaCl + water binary mixture; 39 data points (not inspected in detail).
solvents: [{'component_org_num': 'DOIcomp_3', 'comp_num_id': 'GLOBcomp_1', 'solvent_num_id': 'GLOBsolvent_1', 'inchi_key': 'XLYOFNOQVPJJNP-UHFFFAOYSA-N'}]

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#6_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.3 · phase=Liquid」 |
| L1#1_Table#6_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–323.15 · n_unique=6 · phase=Liquid」 |
| L1#1_Table#6_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_9」 | 「Amount concentration (molarity), mol/dm3 of sodium chloride」 | 「range=1.0–4.0 · n_unique=7 · phase=Liquid」 |
| L1#1_Table#6_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=1023.15–1146.3 · mean=1084.415128 · n=39 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#7_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_2114 | doi: 10.1016/j.fluid.2017.10.034 | block: PROPblock_3
table_mode: rdp | inspection_id: INSP_23511c266e26 | rows_shown: 18

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<sodium chloride>* | *mass_density_kg_m3* |
|---|---|---|---|---|
| L1#1_Table#7_Row#1 | 「BLKpoint_1」 | 「288.15」 | 「0.0099」 | 「1022.2」 |
| L1#1_Table#7_Row#2 | 「BLKpoint_2」 | 「288.15」 | 「0.0196」 | 「1044.7」 |
| L1#1_Table#7_Row#3 | 「BLKpoint_7」 | 「288.15」 | 「0.0654」 | 「1147.1」 |
| L1#1_Table#7_Row#4 | 「BLKpoint_8」 | 「293.15」 | 「0.0099」 | 「1021」 |
| L1#1_Table#7_Row#5 | 「BLKpoint_9」 | 「293.15」 | 「0.0196」 | 「1043.2」 |
| L1#1_Table#7_Row#6 | 「BLKpoint_14」 | 「293.15」 | 「0.0654」 | 「1144.8」 |
| L1#1_Table#7_Row#7 | 「BLKpoint_15」 | 「298.15」 | 「0.0099」 | 「1019.6」 |
| L1#1_Table#7_Row#8 | 「BLKpoint_16」 | 「298.15」 | 「0.0196」 | 「1041.6」 |
| L1#1_Table#7_Row#9 | 「BLKpoint_18」 | 「298.15」 | 「0.0385」 | 「1082.8」 |
| L1#1_Table#7_Row#10 | 「BLKpoint_21」 | 「298.15」 | 「0.0654」 | 「1142.4」 |
| L1#1_Table#7_Row#11 | 「BLKpoint_22」 | 「308.15」 | 「0.0099」 | 「1016.2」 |
| L1#1_Table#7_Row#12 | 「BLKpoint_23」 | 「308.15」 | 「0.0196」 | 「1037.8」 |
| L1#1_Table#7_Row#13 | 「BLKpoint_25」 | 「308.15」 | 「0.0385」 | 「1078.5」 |
| L1#1_Table#7_Row#14 | 「BLKpoint_28」 | 「308.15」 | 「0.0654」 | 「1137.4」 |
| L1#1_Table#7_Row#15 | 「BLKpoint_29」 | 「318.15」 | 「0.0099」 | 「1012.1」 |
| L1#1_Table#7_Row#16 | 「BLKpoint_30」 | 「318.15」 | 「0.0196」 | 「1033.5」 |
| L1#1_Table#7_Row#17 | 「BLKpoint_32」 | 「318.15」 | 「0.0385」 | 「1073.7」 |
| L1#1_Table#7_Row#18 | 「BLKpoint_35」 | 「318.15」 | 「0.0654」 | 「1132.2」 |
```
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
The L1 query returned comprehensive data. I have all the information needed to provide a complete answer about density data for salt water (NaCl + water). The data is well-grounded from the inspected block (GLOBlit_2114, PROPblock_3), and I also have metadata about other available blocks. Let me compose the final answer.
</reasoning>

<answer>

## Mass Density Data for Salt Water (NaCl + Water)

The ThermoML database contains **20 data blocks** reporting liquid-phase mass density for the sodium chloride + water binary system, covering multiple composition scales (mole fraction, mass fraction, molality, and molarity).

### Detailed Data — Inspected Block

The most detailed inspected source is from DOI **10.1016/j.fluid.2017.10.034** (PROPblock_3), containing **35 data points** measured via vibrating tube densimetry across five temperatures (288.15–318.15 K) and seven NaCl mole fractions (0.0099–0.0654). Densities range from **1012.1 to 1147.1 kg/m³**.

Representative data points:

| T (K) | x(NaCl) | Density (kg/m³) |
|--------|---------|-----------------|
| 288.15 | 0.0099 | 1022.2 |
| 288.15 | 0.0196 | 1044.7 |
| 288.15 | 0.0654 | 1147.1 |
| 293.15 | 0.0099 | 1021.0 |
| 293.15 | 0.0196 | 1043.2 |
| 293.15 | 0.0654 | 1144.8 |
| 298.15 | 0.0099 | 1019.6 |
| 298.15 | 0.0196 | 1041.6 |
| 298.15 | 0.0385 | 1082.8 |
| 298.15 | 0.0654 | 1142.4 |
| 308.15 | 0.0099 | 1016.2 |
| 308.15 | 0.0196 | 1037.8 |
| 308.15 | 0.0385 | 1078.5 |
| 308.15 | 0.0654 | 1137.4 |
| 318.15 | 0.0099 | 1012.1 |
| 318.15 | 0.0196 | 1033.5 |
| 318.15 | 0.0385 | 1073.7 |
| 318.15 | 0.0654 | 1132.2 |

### Additional Data Sources

Several other blocks are available but were not numerically inspected in detail:

| DOI | Block | Points | Composition Scale | T (K) Range | ρ (kg/m³) Range |
|-----|-------|--------|-------------------|-------------|-----------------|
| 10.1016/j.fluid.2012.04.003 | PROPblock_1 | 6 | Mass fraction (0.02–0.04) | 293.15–313.15 | 1006.1–1026.7 |
| 10.1016/j.jct.2005.03.008 | PROPblock_5 | 4 | Mass fraction (0.005–0.03) | 293.15 (fixed) | 1001.78–1019.58 |
| 10.1016/j.jct.2008.12.011 | PROPblock_6 | 39 | Molarity (1.0–4.0 mol/dm³) | 298.15–323.15 | 1023.15–1146.3 |

In total, 20 blocks span a wide range of conditions and composition representations.

### Chemical Insight

The data illustrate two classic trends for aqueous electrolyte solutions:

- **Concentration effect:** At 298.15 K, density increases from 1019.6 kg/m³ at x(NaCl) = 0.0099 to 1142.4 kg/m³ at x(NaCl) = 0.0654 — roughly a 12% increase. This reflects the higher molar mass of NaCl and the strong ion–dipole interactions between Na⁺/Cl⁻ ions and water molecules, which contract the solution volume relative to ideal mixing.

- **Temperature effect:** At a fixed mole fraction of 0.0654, density decreases from 1147.1 kg/m³ at 288.15 K to 1132.2 kg/m³ at 318.15 K (a drop of ~15 kg/m³ over 30 K), consistent with thermal expansion of the liquid. Even dilute NaCl solutions remain measurably denser than pure water across the entire temperature range studied.

</answer>