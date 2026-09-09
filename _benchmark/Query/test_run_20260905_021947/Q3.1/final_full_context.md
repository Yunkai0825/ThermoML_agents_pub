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
| comp | GLOBcomp_102 | butane | butane |
| comp | GLOBcomp_284 | 2,6,10,15,19,23-hexamethyltetracosane | 2,6,10,15,19,23-hexamethyltetracosane |
| comp | GLOBcomp_12 | hexane | hexane |
| comp | GLOBcomp_17 | octane | octane |
| comp | GLOBcomp_131 | 1-chlorobutane | 1-chlorobutane |
| comp | GLOBcomp_52 | diisopropyl_ether | diisopropyl ether |
| comp | GLOBcomp_307 | 2-chlorobutane | 2-chlorobutane |
| comp | GLOBcomp_361 | 1-chloro-2-methylpropane | 1-chloro-2-methylpropane |
| comp | GLOBcomp_328 | 2-chloro-2-methylpropane | 2-chloro-2-methylpropane |
| comp | GLOBcomp_7 | butan-1-ol | butan-1-ol |
| comp | GLOBcomp_247 | 2,5,8,11,14-pentaoxapentadecane | 2,5,8,11,14-pentaoxapentadecane |
| prop | GLOBprop_1 | mass_density_kg_m3 | Mass density, kg/m3 |
| prop | GLOBprop_4 | viscosity_pa_s | Viscosity, Pa*s |
| prop | GLOBprop_7 | refractive_index_na_dline | Refractive index (Na D-line) |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|
| lit | GLOBlit_25 | 2006-kum-tom-0 | 10.1007/s10765-006-0053-2 |
| lit | GLOBlit_97 | 2010-mon-gue-0 | 10.1007/s10765-010-0737-5 |
| lit | GLOBlit_151 | 2013-ziv-ser-0 | 10.1007/s10765-013-1469-0 |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find binary liquid mixtures where both mass density and dynamic viscosity are measured in the same dataset/paper → stored as L1_query_1 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: FLAGGED(1)

**Summary:** Three ThermoML literature sources were identified as containing both mass density and dynamic viscosity co-measured for binary liquid mixtures, totaling 8 distinct binary systems. GLOBlit_25 (DOI 10.1007/s10765-006-0053-2) covers 3 alkane + squalane systems (butane, hexane, and octane each with squalane) with high-pressure data. GLOBlit_97 (DOI 10.1007/s10765-010-0737-5) covers 4 chlorobutane isomer + diisopropyl ether systems (1-chlorobutane, 2-chlorobutane, 1-chloro-2-methylpropane, and 2-chloro-2-methylpropane each with diisopropyl ether), providing a systematic isomer series. GLOBlit_151 (DOI 10.1007/s10765-013-1469-0) covers 1 system of butan-1-ol + TEGDME (2,5,8,11,14-pentaoxapentadecane) with three co-measured properties (density, viscosity, and refractive index). Exact temperature, pressure, and composition ranges for each data block were not independently verified via block-table inspection and should be confirmed before use.

**Answer:**

#### Binary Liquid Mixtures with Co-Measured Mass Density and Dynamic Viscosity

Three literature sources in the ThermoML database were confirmed to contain **both mass density (GLOBprop_1) and dynamic viscosity (GLOBprop_4)** measured for binary liquid systems. These are suitable candidates for jointly testing density and viscosity predictions.

---

##### 1. Alkanes + Squalane — GLOBlit_25
**DOI:** 10.1007/s10765-006-0053-2

Three binary sub-systems, each with paired density and viscosity blocks at high pressure. The following block-level summaries were returned by the `search_blocks` tool but individual block data tables were not inspected in this run, so exact numerical ranges should be verified by inspecting each block before use:

**WM_L1_Q1_Table#1_(Query_L1_Q1_Answer):**

| *row_id* | *System* | *Viscosity Block* | *Density Block* |
|---|---|---|---|
| WM_L1_Q1_Table#1_Row#1 | 「Butane (GLOBcomp_102) + squalane (GLOBcomp_284)」 | 「PROPblock_9」 | 「PROPblock_10」 |
| WM_L1_Q1_Table#1_Row#2 | 「Hexane (GLOBcomp_12) + squalane (GLOBcomp_284)」 | 「PROPblock_11」 | 「PROPblock_12」 |
| WM_L1_Q1_Table#1_Row#3 | 「Octane (GLOBcomp_17) + squalane (GLOBcomp_284)」 | 「PROPblock_13」 | 「PROPblock_14」 |

**Note:** The search_blocks result reported these blocks span temperature, pressure, and composition ranges, but the exact values were not verified via `inspect_block_table` in this run. Squalane is a common viscosity reference fluid, making these data useful for equation-of-state and transport-property model validation.

---

##### 2. Diisopropyl Ether + Chlorobutane Isomers — GLOBlit_97
**DOI:** 10.1007/s10765-010-0737-5

Four binary systems with paired density and viscosity blocks. Block-level summaries were returned by `search_blocks` but individual data tables were not inspected in this run:

**WM_L1_Q1_Table#2_(Query_L1_Q1_Answer):**

| *row_id* | *System* | *Viscosity Block* | *Density Block* |
|---|---|---|---|
| WM_L1_Q1_Table#2_Row#1 | 「1-Chlorobutane (GLOBcomp_131) + diisopropyl ether (GLOBcomp_52)」 | 「PROPblock_11」 | 「PROPblock_12」 |
| WM_L1_Q1_Table#2_Row#2 | 「2-Chlorobutane (GLOBcomp_307) + diisopropyl ether (GLOBcomp_52)」 | 「PROPblock_13」 | 「PROPblock_14」 |
| WM_L1_Q1_Table#2_Row#3 | 「1-Chloro-2-methylpropane (GLOBcomp_361) + diisopropyl ether (GLOBcomp_52)」 | 「PROPblock_15」 | 「PROPblock_16」 |
| WM_L1_Q1_Table#2_Row#4 | 「2-Chloro-2-methylpropane (GLOBcomp_328) + diisopropyl ether (GLOBcomp_52)」 | 「PROPblock_17」 | 「PROPblock_18」 |

**Chemistry note:** This set of structural isomers (1-chlorobutane, 2-chlorobutane, isobutyl chloride, tert-butyl chloride) with a common second component provides a systematic way to study the effect of branching and chlorine position on both density and viscosity of binary mixtures.

---

##### 3. Butan-1-ol + TEGDME — GLOBlit_151
**DOI:** 10.1007/s10765-013-1469-0

One binary system with density, viscosity, and refractive index all co-measured. Block-level summaries were returned by `search_blocks` but individual data tables were not inspected in this run:

**WM_L1_Q1_Table#3_(Query_L1_Q1_Answer):**

| *row_id* | *Property* | *Block* |
|---|---|---|
| WM_L1_Q1_Table#3_Row#1 | 「Mass density (GLOBprop_1)」 | 「PROPblock_7」 |
| WM_L1_Q1_Table#3_Row#2 | 「Dynamic viscosity (GLOBprop_4)」 | 「PROPblock_8」 |
| WM_L1_Q1_Table#3_Row#3 | 「Refractive index (GLOBprop_7)」 | 「PROPblock_9」 |

**Compounds:** butan-1-ol (GLOBcomp_7), 2,5,8,11,14-pentaoxapentadecane / TEGDME (GLOBcomp_247).

**Chemistry note:** The alcohol + polyether system exhibits hydrogen-bonding interactions that produce non-ideal mixing behavior in both density and viscosity, making it a stringent test for predictive models. Additionally, having three co-measured properties (density, viscosity, refractive index) in the same dataset adds further value for multi-property model validation.

---

##### Summary

**WM_L1_Q1_Table#4_(Query_L1_Q1_Answer):**

| *row_id* | *Literature* | *DOI* | *# Binary Systems* | *Key Chemistry* |
|---|---|---|---|---|
| WM_L1_Q1_Table#4_Row#1 | 「GLOBlit_25」 | 「10.1007/s10765-006-0053-2」 | 「3 (alkane + squalane)」 | 「Non-polar hydrocarbon mixtures, high-pressure data」 |
| WM_L1_Q1_Table#4_Row#2 | 「GLOBlit_97」 | 「10.1007/s10765-010-0737-5」 | 「4 (chlorobutane isomers + diisopropyl ether)」 | 「Isomer series, atmospheric pressure」 |
| WM_L1_Q1_Table#4_Row#3 | 「GLOBlit_151」 | 「10.1007/s10765-013-1469-0」 | 「1 (butan-1-ol + TEGDME)」 | 「H-bonding system, three co-measured properties」 |

In total, **8 distinct binary liquid systems** across these three literature sources have both mass density and dynamic viscosity co-measured. The exact temperature, pressure, and composition ranges for each block were reported by the registry search tool but were not independently verified via block-table inspection in this run; users should inspect individual blocks (e.g., `GLOBlit_25::PROPblock_9`) to confirm precise data ranges before use.

**Additional literature sources checked but found to contain only one property:**
- GLOBlit_8 (ethanol + toluene): viscosity only
- GLOBlit_59 (ethanol + BMIMBF₄): density only
- GLOBlit_145 (chlorobutane isomers + ethers): viscosity only

**Core claims:**
- Three ThermoML literature sources (GLOBlit_25, GLOBlit_97, GLOBlit_151) were identified as containing both mass density and dynamic viscosity co-measured for binary liquid systems, encompassing 8 distinct binary systems in total.
- GLOBlit_25 (DOI 10.1007/s10765-006-0053-2) covers three alkane + squalane binary systems (butane, hexane, octane each paired with squalane) with high-pressure density and viscosity data.
- GLOBlit_97 (DOI 10.1007/s10765-010-0737-5) covers four chlorobutane isomer + diisopropyl ether binary systems, providing a systematic series for studying branching and chlorine-position effects on density and viscosity.
- GLOBlit_151 (DOI 10.1007/s10765-013-1469-0) covers one butan-1-ol + TEGDME binary system with three co-measured properties: mass density, dynamic viscosity, and refractive index.
- Exact temperature, pressure, and composition ranges for the identified data blocks were not independently verified via block-table inspection in this run; the answer flags this as an unresolved limitation requiring further verification before use.

**Core blocks found:**

**WM_L1_Q1_Blocks_(Query_L1_Q1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1_Q1_Table#5 | 「GLOBlit_25」 | 「PROPblock_9」 | 「GLOBcomp_102, GLOBcomp_284」 | 「GLOBprop_4」 | 「Dynamic viscosity for butane + squalane.」 |
| WM_L1_Q1_Table#6 | 「GLOBlit_25」 | 「PROPblock_10」 | 「GLOBcomp_102, GLOBcomp_284」 | 「GLOBprop_1」 | 「Mass density for butane + squalane.」 |
| WM_L1_Q1_Table#7 | 「GLOBlit_25」 | 「PROPblock_11」 | 「GLOBcomp_12, GLOBcomp_284」 | 「GLOBprop_4」 | 「Dynamic viscosity for hexane + squalane.」 |
| WM_L1_Q1_Table#8 | 「GLOBlit_25」 | 「PROPblock_12」 | 「GLOBcomp_12, GLOBcomp_284」 | 「GLOBprop_1」 | 「Mass density for hexane + squalane.」 |
| WM_L1_Q1_Table#9 | 「GLOBlit_25」 | 「PROPblock_13」 | 「GLOBcomp_284, GLOBcomp_17」 | 「GLOBprop_4」 | 「Dynamic viscosity for octane + squalane.」 |
| WM_L1_Q1_Table#10 | 「GLOBlit_25」 | 「PROPblock_14」 | 「GLOBcomp_284, GLOBcomp_17」 | 「GLOBprop_1」 | 「Mass density for octane + squalane.」 |
| WM_L1_Q1_Table#11 | 「GLOBlit_97」 | 「PROPblock_11」 | 「GLOBcomp_52, GLOBcomp_131」 | 「GLOBprop_4」 | 「Dynamic viscosity for 1-chlorobutane + diisopropyl ether.」 |
| WM_L1_Q1_Table#12 | 「GLOBlit_97」 | 「PROPblock_12」 | 「GLOBcomp_52, GLOBcomp_131」 | 「GLOBprop_1」 | 「Mass density for 1-chlorobutane + diisopropyl ether.」 |
| WM_L1_Q1_Table#13 | 「GLOBlit_97」 | 「PROPblock_13」 | 「GLOBcomp_307, GLOBcomp_52」 | 「GLOBprop_4」 | 「Dynamic viscosity for 2-chlorobutane + diisopropyl ether.」 |
| WM_L1_Q1_Table#14 | 「GLOBlit_97」 | 「PROPblock_14」 | 「GLOBcomp_307, GLOBcomp_52」 | 「GLOBprop_1」 | 「Mass density for 2-chlorobutane + diisopropyl ether.」 |
| WM_L1_Q1_Table#15 | 「GLOBlit_97」 | 「PROPblock_15」 | 「GLOBcomp_52, GLOBcomp_361」 | 「GLOBprop_4」 | 「Dynamic viscosity for 1-chloro-2-methylpropane + diisopropyl ether.」 |
| WM_L1_Q1_Table#16 | 「GLOBlit_97」 | 「PROPblock_16」 | 「GLOBcomp_52, GLOBcomp_361」 | 「GLOBprop_1」 | 「Mass density for 1-chloro-2-methylpropane + diisopropyl ether.」 |
| WM_L1_Q1_Table#17 | 「GLOBlit_97」 | 「PROPblock_17」 | 「GLOBcomp_52, GLOBcomp_328」 | 「GLOBprop_4」 | 「Dynamic viscosity for 2-chloro-2-methylpropane + diisopropyl ether.」 |
| WM_L1_Q1_Table#18 | 「GLOBlit_97」 | 「PROPblock_18」 | 「GLOBcomp_52, GLOBcomp_328」 | 「GLOBprop_1」 | 「Mass density for 2-chloro-2-methylpropane + diisopropyl ether.」 |
| WM_L1_Q1_Table#19 | 「GLOBlit_151」 | 「PROPblock_7」 | 「GLOBcomp_7, GLOBcomp_247」 | 「GLOBprop_1」 | 「Mass density for butan-1-ol + TEGDME.」 |
| WM_L1_Q1_Table#20 | 「GLOBlit_151」 | 「PROPblock_8」 | 「GLOBcomp_7, GLOBcomp_247」 | 「GLOBprop_4」 | 「Dynamic viscosity for butan-1-ol + TEGDME.」 |
| WM_L1_Q1_Table#21 | 「GLOBlit_151」 | 「PROPblock_9」 | 「GLOBcomp_7, GLOBcomp_247」 | 「GLOBprop_7」 | 「Refractive index for butan-1-ol + TEGDME.」 |

*Not stored here: 17 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_9: PROPblock_9 is quoted with data values (14, …) but was never inspected in this run (values 14 verified against the database — inspection is still mandatory)



</memory>

## User
I need three binary liquid systems for jointly testing density and viscosity predictions. Which systems have both properties measured for the same mixture, and which papers should I start with?

## Assistant
<summary>Planning to search for binary liquid systems with both density (GLOBprop_1) and viscosity (GLOBprop_4) measured. Will dispatch L1 query to find co-measured systems.</summary>
<tool_call>L1_query(instruction=Search for binary…, id_catalog=, context=User wants to ide…)</tool_call>

## User
<tool_result>
[TOOL_RESULT_SIZE_WARNING: L1_query returned 29,657 characters after result processing; the target is 24,000. The full result follows — prefer narrower requests, and rely on your working memory for recall instead of re-running this call.]

<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** Three ThermoML literature sources were identified as containing both mass density and dynamic viscosity co-measured for binary liquid mixtures, totaling 8 distinct binary systems. GLOBlit_25 (DOI 10.1007/s10765-006-0053-2) covers 3 alkane + squalane systems (butane, hexane, and octane each with squalane) with high-pressure data. GLOBlit_97 (DOI 10.1007/s10765-010-0737-5) covers 4 chlorobutane isomer + diisopropyl ether systems (1-chlorobutane, 2-chlorobutane, 1-chloro-2-methylpropane, and 2-chloro-2-methylpropane each with diisopropyl ether), providing a systematic isomer series. GLOBlit_151 (DOI 10.1007/s10765-013-1469-0) covers 1 system of butan-1-ol + TEGDME (2,5,8,11,14-pentaoxapentadecane) with three co-measured properties (density, viscosity, and refractive index). Exact temperature, pressure, and composition ranges for each data block were not independently verified via block-table inspection and should be confirmed before use.

**Answer:**

#### Binary Liquid Mixtures with Co-Measured Mass Density and Dynamic Viscosity

Three literature sources in the ThermoML database were confirmed to contain **both mass density (GLOBprop_1) and dynamic viscosity (GLOBprop_4)** measured for binary liquid systems. These are suitable candidates for jointly testing density and viscosity predictions.

---

##### 1. Alkanes + Squalane — GLOBlit_25
**DOI:** 10.1007/s10765-006-0053-2

Three binary sub-systems, each with paired density and viscosity blocks at high pressure. The following block-level summaries were returned by the `search_blocks` tool but individual block data tables were not inspected in this run, so exact numerical ranges should be verified by inspecting each block before use:

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *System* | *Viscosity Block* | *Density Block* |
|---|---|---|---|
| L1#1_Table#1_Row#1 | 「Butane (GLOBcomp_102) + squalane (GLOBcomp_284)」 | 「PROPblock_9」 | 「PROPblock_10」 |
| L1#1_Table#1_Row#2 | 「Hexane (GLOBcomp_12) + squalane (GLOBcomp_284)」 | 「PROPblock_11」 | 「PROPblock_12」 |
| L1#1_Table#1_Row#3 | 「Octane (GLOBcomp_17) + squalane (GLOBcomp_284)」 | 「PROPblock_13」 | 「PROPblock_14」 |

**Note:** The search_blocks result reported these blocks span temperature, pressure, and composition ranges, but the exact values were not verified via `inspect_block_table` in this run. Squalane is a common viscosity reference fluid, making these data useful for equation-of-state and transport-property model validation.

---

##### 2. Diisopropyl Ether + Chlorobutane Isomers — GLOBlit_97
**DOI:** 10.1007/s10765-010-0737-5

Four binary systems with paired density and viscosity blocks. Block-level summaries were returned by `search_blocks` but individual data tables were not inspected in this run:

**L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *System* | *Viscosity Block* | *Density Block* |
|---|---|---|---|
| L1#1_Table#2_Row#1 | 「1-Chlorobutane (GLOBcomp_131) + diisopropyl ether (GLOBcomp_52)」 | 「PROPblock_11」 | 「PROPblock_12」 |
| L1#1_Table#2_Row#2 | 「2-Chlorobutane (GLOBcomp_307) + diisopropyl ether (GLOBcomp_52)」 | 「PROPblock_13」 | 「PROPblock_14」 |
| L1#1_Table#2_Row#3 | 「1-Chloro-2-methylpropane (GLOBcomp_361) + diisopropyl ether (GLOBcomp_52)」 | 「PROPblock_15」 | 「PROPblock_16」 |
| L1#1_Table#2_Row#4 | 「2-Chloro-2-methylpropane (GLOBcomp_328) + diisopropyl ether (GLOBcomp_52)」 | 「PROPblock_17」 | 「PROPblock_18」 |

**Chemistry note:** This set of structural isomers (1-chlorobutane, 2-chlorobutane, isobutyl chloride, tert-butyl chloride) with a common second component provides a systematic way to study the effect of branching and chlorine position on both density and viscosity of binary mixtures.

---

##### 3. Butan-1-ol + TEGDME — GLOBlit_151
**DOI:** 10.1007/s10765-013-1469-0

One binary system with density, viscosity, and refractive index all co-measured. Block-level summaries were returned by `search_blocks` but individual data tables were not inspected in this run:

**L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *Property* | *Block* |
|---|---|---|
| L1#1_Table#3_Row#1 | 「Mass density (GLOBprop_1)」 | 「PROPblock_7」 |
| L1#1_Table#3_Row#2 | 「Dynamic viscosity (GLOBprop_4)」 | 「PROPblock_8」 |
| L1#1_Table#3_Row#3 | 「Refractive index (GLOBprop_7)」 | 「PROPblock_9」 |

**Compounds:** butan-1-ol (GLOBcomp_7), 2,5,8,11,14-pentaoxapentadecane / TEGDME (GLOBcomp_247).

**Chemistry note:** The alcohol + polyether system exhibits hydrogen-bonding interactions that produce non-ideal mixing behavior in both density and viscosity, making it a stringent test for predictive models. Additionally, having three co-measured properties (density, viscosity, refractive index) in the same dataset adds further value for multi-property model validation.

---

##### Summary

**L1#1_Table#4_(Query_L1#1_Answer):**

| *row_id* | *Literature* | *DOI* | *# Binary Systems* | *Key Chemistry* |
|---|---|---|---|---|
| L1#1_Table#4_Row#1 | 「GLOBlit_25」 | 「10.1007/s10765-006-0053-2」 | 「3 (alkane + squalane)」 | 「Non-polar hydrocarbon mixtures, high-pressure data」 |
| L1#1_Table#4_Row#2 | 「GLOBlit_97」 | 「10.1007/s10765-010-0737-5」 | 「4 (chlorobutane isomers + diisopropyl ether)」 | 「Isomer series, atmospheric pressure」 |
| L1#1_Table#4_Row#3 | 「GLOBlit_151」 | 「10.1007/s10765-013-1469-0」 | 「1 (butan-1-ol + TEGDME)」 | 「H-bonding system, three co-measured properties」 |

In total, **8 distinct binary liquid systems** across these three literature sources have both mass density and dynamic viscosity co-measured. The exact temperature, pressure, and composition ranges for each block were reported by the registry search tool but were not independently verified via block-table inspection in this run; users should inspect individual blocks (e.g., `GLOBlit_25::PROPblock_9`) to confirm precise data ranges before use.

**Additional literature sources checked but found to contain only one property:**
- GLOBlit_8 (ethanol + toluene): viscosity only
- GLOBlit_59 (ethanol + BMIMBF₄): density only
- GLOBlit_145 (chlorobutane isomers + ethers): viscosity only

---
[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:
- **UNINSPECTED_BLOCK** PROPblock_9: PROPblock_9 is quoted with data values (14, …) but was never inspected in this run (values 14 verified against the database — inspection is still mandatory)
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_25::PROPblock_9")`

**Core claims:**
- Three ThermoML literature sources (GLOBlit_25, GLOBlit_97, GLOBlit_151) were identified as containing both mass density and dynamic viscosity co-measured for binary liquid systems, encompassing 8 distinct binary systems in total.
- GLOBlit_25 (DOI 10.1007/s10765-006-0053-2) covers three alkane + squalane binary systems (butane, hexane, octane each paired with squalane) with high-pressure density and viscosity data.
- GLOBlit_97 (DOI 10.1007/s10765-010-0737-5) covers four chlorobutane isomer + diisopropyl ether binary systems, providing a systematic series for studying branching and chlorine-position effects on density and viscosity.
- GLOBlit_151 (DOI 10.1007/s10765-013-1469-0) covers one butan-1-ol + TEGDME binary system with three co-measured properties: mass density, dynamic viscosity, and refractive index.
- Exact temperature, pressure, and composition ranges for the identified data blocks were not independently verified via block-table inspection in this run; the answer flags this as an unresolved limitation requiring further verification before use.

**Core ID updates:**
- add GLOBcomp_102 — butane (registry: butane)
- add GLOBcomp_284 — 2,6,10,15,19,23-hexamethyltetracosane (registry: 2,6,10,15,19,23-hexamethyltetracosane)
- add GLOBcomp_12 — hexane (registry: hexane)
- add GLOBcomp_17 — octane (registry: octane)
- add GLOBcomp_131 — 1-chlorobutane (registry: 1-chlorobutane)
- add GLOBcomp_52 — diisopropyl ether (registry: diisopropyl_ether)
- add GLOBcomp_307 — 2-chlorobutane (registry: 2-chlorobutane)
- add GLOBcomp_361 — 1-chloro-2-methylpropane (registry: 1-chloro-2-methylpropane)
- add GLOBcomp_328 — 2-chloro-2-methylpropane (registry: 2-chloro-2-methylpropane)
- add GLOBcomp_7 — butan-1-ol (registry: butan-1-ol)
- add GLOBcomp_247 — 2,5,8,11,14-pentaoxapentadecane (registry: 2,5,8,11,14-pentaoxapentadecane)
- add GLOBprop_1 — Mass density, kg/m3 (registry: mass_density_kg_m3)
- add GLOBprop_4 — Viscosity, Pa*s (registry: viscosity_pa_s)
- add GLOBprop_7 — Refractive index (Na D-line) (registry: refractive_index_na_dline)
- add GLOBlit_25 — 10.1007/s10765-006-0053-2 (registry: 2006-kum-tom-0)
- add GLOBlit_97 — 10.1007/s10765-010-0737-5 (registry: 2010-mon-gue-0)
- add GLOBlit_151 — 10.1007/s10765-013-1469-0 (registry: 2013-ziv-ser-0)

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#5_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_25 | lit_id: 2006-kum-tom-0 | doi: 10.1007/s10765-006-0053-2
block: PROPblock_9 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 80
compounds: butane (C4H10; GLOBcomp_102; DOIcomp_1; InChIKey IJDNQMDRQITEOD-UHFFFAOYSA-N); 2,6,10,15,19,23-hexamethyltetracosane (C30H62; GLOBcomp_284; DOIcomp_4; InChIKey PRAKJMSDJKAYCZ-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity for butane + squalane.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#5_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=273.15–333.15 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#5_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of 2,6,10,15,19,23-hexamethyltetracosane」 | 「range=0.0–0.753 · n_unique=7 · phase=Liquid」 |
| L1#1_Table#5_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_3」 | 「Pressure, kPa」 | 「range=100.0–30000.0 · n_unique=8 · phase=Liquid」 |
| L1#1_Table#5_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=Falling or rolling sphere viscometry (GLOBmeas_8) · range=0.000118–0.0915 · mean=0.008387 · n=80 · phase=Liquid」 |
```

```ledger
**L1#1_Table#6_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_25 | lit_id: 2006-kum-tom-0 | doi: 10.1007/s10765-006-0053-2
block: PROPblock_10 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 80
compounds: butane (C4H10; GLOBcomp_102; DOIcomp_1; InChIKey IJDNQMDRQITEOD-UHFFFAOYSA-N); 2,6,10,15,19,23-hexamethyltetracosane (C30H62; GLOBcomp_284; DOIcomp_4; InChIKey PRAKJMSDJKAYCZ-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density for butane + squalane.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#6_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=273.15–333.15 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#6_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of 2,6,10,15,19,23-hexamethyltetracosane」 | 「range=0.0–0.753 · n_unique=7 · phase=Liquid」 |
| L1#1_Table#6_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_3」 | 「Pressure, kPa」 | 「range=100.0–30000.0 · n_unique=8 · phase=Liquid」 |
| L1#1_Table#6_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Constant-volume piezometry (GLOBmeas_66) · range=529.0–825.0 · mean=723.9125 · n=80 · phase=Liquid」 |
```

```ledger
**L1#1_Table#7_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_25 | lit_id: 2006-kum-tom-0 | doi: 10.1007/s10765-006-0053-2
block: PROPblock_11 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 64
compounds: hexane (C6H14; GLOBcomp_12; DOIcomp_2; InChIKey VLKZOEOYAKHREP-UHFFFAOYSA-N); 2,6,10,15,19,23-hexamethyltetracosane (C30H62; GLOBcomp_284; DOIcomp_4; InChIKey PRAKJMSDJKAYCZ-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity for hexane + squalane.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#7_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=273.15–333.15 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#7_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of 2,6,10,15,19,23-hexamethyltetracosane」 | 「range=0.0–0.743 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#7_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_3」 | 「Pressure, kPa」 | 「range=100.0–30000.0 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#7_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=Falling or rolling sphere viscometry (GLOBmeas_8) · range=0.000218–0.0971 · mean=0.010363 · n=64 · phase=Liquid」 |
```

```ledger
**L1#1_Table#8_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_25 | lit_id: 2006-kum-tom-0 | doi: 10.1007/s10765-006-0053-2
block: PROPblock_12 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 64
compounds: hexane (C6H14; GLOBcomp_12; DOIcomp_2; InChIKey VLKZOEOYAKHREP-UHFFFAOYSA-N); 2,6,10,15,19,23-hexamethyltetracosane (C30H62; GLOBcomp_284; DOIcomp_4; InChIKey PRAKJMSDJKAYCZ-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density for hexane + squalane.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#8_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=273.15–333.15 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#8_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of 2,6,10,15,19,23-hexamethyltetracosane」 | 「range=0.0–0.743 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#8_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_3」 | 「Pressure, kPa」 | 「range=100.0–30000.0 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#8_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Constant-volume piezometry (GLOBmeas_66) · range=623.0–824.0 · mean=744.203125 · n=64 · phase=Liquid」 |
```

```ledger
**L1#1_Table#9_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_25 | lit_id: 2006-kum-tom-0 | doi: 10.1007/s10765-006-0053-2
block: PROPblock_13 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 80
compounds: 2,6,10,15,19,23-hexamethyltetracosane (C30H62; GLOBcomp_284; DOIcomp_4; InChIKey PRAKJMSDJKAYCZ-UHFFFAOYSA-N); octane (C8H18; GLOBcomp_17; DOIcomp_3; InChIKey TVMXDCGIABBOFY-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity for octane + squalane.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#9_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=273.15–333.15 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#9_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of 2,6,10,15,19,23-hexamethyltetracosane」 | 「range=0.0–1.0 · n_unique=6 · phase=Liquid」 |
| L1#1_Table#9_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_3」 | 「Pressure, kPa」 | 「range=100.0–30000.0 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#9_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=Falling or rolling sphere viscometry (GLOBmeas_8) · range=0.000351–0.2614 · mean=0.021392 · n=80 · phase=Liquid」 |
```

```ledger
**L1#1_Table#10_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_25 | lit_id: 2006-kum-tom-0 | doi: 10.1007/s10765-006-0053-2
block: PROPblock_14 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 80
compounds: 2,6,10,15,19,23-hexamethyltetracosane (C30H62; GLOBcomp_284; DOIcomp_4; InChIKey PRAKJMSDJKAYCZ-UHFFFAOYSA-N); octane (C8H18; GLOBcomp_17; DOIcomp_3; InChIKey TVMXDCGIABBOFY-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density for octane + squalane.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#10_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=273.15–333.15 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#10_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of 2,6,10,15,19,23-hexamethyltetracosane」 | 「range=0.0–1.0 · n_unique=6 · phase=Liquid」 |
| L1#1_Table#10_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_3」 | 「Pressure, kPa」 | 「range=100.0–30000.0 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#10_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Constant-volume piezometry (GLOBmeas_66) · range=670.0–835.0 · mean=772.7 · n=80 · phase=Liquid」 |
```

```ledger
**L1#1_Table#11_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_97 | lit_id: 2010-mon-gue-0 | doi: 10.1007/s10765-010-0737-5
block: PROPblock_11 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 91
compounds: diisopropyl ether (C6H14O; GLOBcomp_52; DOIcomp_4; InChIKey ZAFNJMIOTHYJRJ-UHFFFAOYSA-N); 1-chlorobutane (C4H9Cl; GLOBcomp_131; DOIcomp_2; InChIKey VFWCMGCRMGJXDK-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity for 1-chlorobutane + diisopropyl ether.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#11_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#11_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–313.15 · n_unique=7 · phase=Liquid」 |
| L1#1_Table#11_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of 1-chlorobutane」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#1_Table#11_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=Capillary tube (Ostwald; Ubbelohde) method (GLOBmeas_4) · range=0.000272–0.000499 · mean=0.000372 · n=91 · phase=Liquid」 |
```

```ledger
**L1#1_Table#12_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_97 | lit_id: 2010-mon-gue-0 | doi: 10.1007/s10765-010-0737-5
block: PROPblock_12 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 91
compounds: diisopropyl ether (C6H14O; GLOBcomp_52; DOIcomp_4; InChIKey ZAFNJMIOTHYJRJ-UHFFFAOYSA-N); 1-chlorobutane (C4H9Cl; GLOBcomp_131; DOIcomp_2; InChIKey VFWCMGCRMGJXDK-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density for 1-chlorobutane + diisopropyl ether.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#12_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.3 · phase=Liquid」 |
| L1#1_Table#12_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–313.15 · n_unique=7 · phase=Liquid」 |
| L1#1_Table#12_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of 1-chlorobutane」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#1_Table#12_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:6 (GLOBmeas_143) · range=702.378–897.339 · mean=795.892066 · n=91 · phase=Liquid」 |
```

```ledger
**L1#1_Table#13_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_97 | lit_id: 2010-mon-gue-0 | doi: 10.1007/s10765-010-0737-5
block: PROPblock_13 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 91
compounds: 2-chlorobutane (C4H9Cl; GLOBcomp_307; DOIcomp_1; InChIKey BSPCSKHALVHRSR-UHFFFAOYSA-N); diisopropyl ether (C6H14O; GLOBcomp_52; DOIcomp_4; InChIKey ZAFNJMIOTHYJRJ-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity for 2-chlorobutane + diisopropyl ether.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#13_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#13_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–313.15 · n_unique=7 · phase=Liquid」 |
| L1#1_Table#13_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of 2-chlorobutane」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#1_Table#13_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=Capillary tube (Ostwald; Ubbelohde) method (GLOBmeas_4) · range=0.000272–0.000463 · mean=0.000357 · n=91 · phase=Liquid」 |
```

```ledger
**L1#1_Table#14_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_97 | lit_id: 2010-mon-gue-0 | doi: 10.1007/s10765-010-0737-5
block: PROPblock_14 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 90
compounds: 2-chlorobutane (C4H9Cl; GLOBcomp_307; DOIcomp_1; InChIKey BSPCSKHALVHRSR-UHFFFAOYSA-N); diisopropyl ether (C6H14O; GLOBcomp_52; DOIcomp_4; InChIKey ZAFNJMIOTHYJRJ-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density for 2-chlorobutane + diisopropyl ether.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#14_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.3 · phase=Liquid」 |
| L1#1_Table#14_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–313.15 · n_unique=7 · phase=Liquid」 |
| L1#1_Table#14_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of 2-chlorobutane」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#1_Table#14_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:6 (GLOBmeas_143) · range=702.378–884.34 · mean=789.576322 · n=90 · phase=Liquid」 |
```

```ledger
**L1#1_Table#15_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_97 | lit_id: 2010-mon-gue-0 | doi: 10.1007/s10765-010-0737-5
block: PROPblock_15 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 91
compounds: diisopropyl ether (C6H14O; GLOBcomp_52; DOIcomp_4; InChIKey ZAFNJMIOTHYJRJ-UHFFFAOYSA-N); 1-chloro-2-methylpropane (C4H9Cl; GLOBcomp_361; DOIcomp_5; InChIKey QTBFPMKWQKYFLR-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity for 1-chloro-2-methylpropane + diisopropyl ether.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#15_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#15_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–313.15 · n_unique=7 · phase=Liquid」 |
| L1#1_Table#15_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of 1-chloro-2-methylpropane」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#1_Table#15_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=Capillary tube (Ostwald; Ubbelohde) method (GLOBmeas_4) · range=0.000272–0.000516 · mean=0.000371 · n=91 · phase=Liquid」 |
```

```ledger
**L1#1_Table#16_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_97 | lit_id: 2010-mon-gue-0 | doi: 10.1007/s10765-010-0737-5
block: PROPblock_16 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 91
compounds: diisopropyl ether (C6H14O; GLOBcomp_52; DOIcomp_4; InChIKey ZAFNJMIOTHYJRJ-UHFFFAOYSA-N); 1-chloro-2-methylpropane (C4H9Cl; GLOBcomp_361; DOIcomp_5; InChIKey QTBFPMKWQKYFLR-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density for 1-chloro-2-methylpropane + diisopropyl ether.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#16_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.3 · phase=Liquid」 |
| L1#1_Table#16_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–313.15 · n_unique=7 · phase=Liquid」 |
| L1#1_Table#16_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of 1-chloro-2-methylpropane」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#1_Table#16_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:6 (GLOBmeas_143) · range=702.378–888.845 · mean=790.074154 · n=91 · phase=Liquid」 |
```

```ledger
**L1#1_Table#17_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_97 | lit_id: 2010-mon-gue-0 | doi: 10.1007/s10765-010-0737-5
block: PROPblock_17 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 91
compounds: diisopropyl ether (C6H14O; GLOBcomp_52; DOIcomp_4; InChIKey ZAFNJMIOTHYJRJ-UHFFFAOYSA-N); 2-chloro-2-methylpropane (C4H9Cl; GLOBcomp_328; DOIcomp_3; InChIKey NBRKLOOSMBRFMH-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity for 2-chloro-2-methylpropane + diisopropyl ether.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#17_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#17_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–313.15 · n_unique=7 · phase=Liquid」 |
| L1#1_Table#17_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of 2-chloro-2-methylpropane」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#1_Table#17_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=Capillary tube (Ostwald; Ubbelohde) method (GLOBmeas_4) · range=0.000272–0.000598 · mean=0.000386 · n=91 · phase=Liquid」 |
```

```ledger
**L1#1_Table#18_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_97 | lit_id: 2010-mon-gue-0 | doi: 10.1007/s10765-010-0737-5
block: PROPblock_18 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 91
compounds: diisopropyl ether (C6H14O; GLOBcomp_52; DOIcomp_4; InChIKey ZAFNJMIOTHYJRJ-UHFFFAOYSA-N); 2-chloro-2-methylpropane (C4H9Cl; GLOBcomp_328; DOIcomp_3; InChIKey NBRKLOOSMBRFMH-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density for 2-chloro-2-methylpropane + diisopropyl ether.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#18_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.3 · phase=Liquid」 |
| L1#1_Table#18_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–313.15 · n_unique=7 · phase=Liquid」 |
| L1#1_Table#18_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of 2-chloro-2-methylpropane」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#1_Table#18_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:6 (GLOBmeas_143) · range=702.378–855.249 · mean=774.86622 · n=91 · phase=Liquid」 |
```

```ledger
**L1#1_Table#19_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_151 | lit_id: 2013-ziv-ser-0 | doi: 10.1007/s10765-013-1469-0
block: PROPblock_7 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 110
compounds: butan-1-ol (C4H10O; GLOBcomp_7; DOIcomp_1; InChIKey LRHPLDYGYMQRHN-UHFFFAOYSA-N); 2,5,8,11,14-pentaoxapentadecane (C10H22O5; GLOBcomp_247; DOIcomp_2; InChIKey ZUHZGEOKBKGPSW-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density for butan-1-ol + TEGDME.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#19_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#19_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=288.15–333.15 · n_unique=10 · phase=Liquid」 |
| L1#1_Table#19_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of butan-1-ol」 | 「range=0.0–1.0 · n_unique=11 · phase=Liquid」 |
| L1#1_Table#19_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=778.056–1015.63 · mean=920.3125 · n=110 · phase=Liquid」 |
```

```ledger
**L1#1_Table#20_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_151 | lit_id: 2013-ziv-ser-0 | doi: 10.1007/s10765-013-1469-0
block: PROPblock_8 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 110
compounds: butan-1-ol (C4H10O; GLOBcomp_7; DOIcomp_1; InChIKey LRHPLDYGYMQRHN-UHFFFAOYSA-N); 2,5,8,11,14-pentaoxapentadecane (C10H22O5; GLOBcomp_247; DOIcomp_2; InChIKey ZUHZGEOKBKGPSW-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Dynamic viscosity for butan-1-ol + TEGDME.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#20_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#20_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=288.15–333.15 · n_unique=10 · phase=Liquid」 |
| L1#1_Table#20_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of butan-1-ol」 | 「range=0.0–1.0 · n_unique=11 · phase=Liquid」 |
| L1#1_Table#20_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=Concentric cylinders viscometry (GLOBmeas_11) · range=0.001104–0.004341 · mean=0.002137 · n=110 · phase=Liquid」 |
```

```ledger
**L1#1_Table#21_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_151 | lit_id: 2013-ziv-ser-0 | doi: 10.1007/s10765-013-1469-0
block: PROPblock_9 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 110
compounds: butan-1-ol (C4H10O; GLOBcomp_7; DOIcomp_1; InChIKey LRHPLDYGYMQRHN-UHFFFAOYSA-N); 2,5,8,11,14-pentaoxapentadecane (C10H22O5; GLOBcomp_247; DOIcomp_2; InChIKey ZUHZGEOKBKGPSW-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_7
description: Refractive index for butan-1-ol + TEGDME.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#21_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#21_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=288.15–333.15 · n_unique=10 · phase=Liquid」 |
| L1#1_Table#21_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of butan-1-ol」 | 「range=0.0–1.0 · n_unique=11 · phase=Liquid」 |
| L1#1_Table#21_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_7」 | 「Refractive index (Na D-line)」 | 「method=Standard Abbe refractometry (GLOBmeas_3) · range=1.38237–1.4345 · mean=1.412611 · n=110 · phase=Liquid」 |
```
</subagent_answer>
</tool_result>

## LLM Response


<reasoning>
The user wants three binary liquid systems for jointly testing density and viscosity predictions. The L1 query has returned comprehensive results identifying 8 binary systems across 3 papers. I have all the data I need from the L1 return and working memory. Let me compose a clear, well-organized final answer selecting three representative systems (one from each paper) and providing the full context.

Actually, the user asked "which systems have both properties measured" — so I should present all 8 systems found, and recommend three diverse ones to start with. Let me craft the answer.
</reasoning>

<answer>

## Binary Liquid Systems with Co-Measured Density and Viscosity

The ThermoML database contains **8 binary liquid systems** across three publications where both mass density (kg/m³) and dynamic viscosity (Pa·s) were measured on the same mixture. Here is a summary, followed by a recommended starting set of three.

---

### Paper 1 — Alkanes + Squalane (high-pressure data)
**DOI:** 10.1007/s10765-006-0053-2 (GLOBlit_25)

| System | Density Block | Viscosity Block | T range (K) | P range (kPa) | x(squalane) range | n points |
|--------|--------------|----------------|-------------|---------------|-------------------|----------|
| Butane + squalane | PROPblock_10 | PROPblock_9 | 273.15–333.15 | 100.0–30000.0 | 0.0–0.753 | 80 each |
| Hexane + squalane | PROPblock_12 | PROPblock_11 | 273.15–333.15 | 100.0–30000.0 | 0.0–0.743 | 64 each |
| Octane + squalane | PROPblock_14 | PROPblock_13 | 273.15–333.15 | 100.0–30000.0 | 0.0–1.0 | 80 each |

Density ranges from 529.0 to 835.0 kg/m³ and viscosity spans 0.000118 to 0.2614 Pa·s across these three systems — nearly three orders of magnitude in viscosity, driven by squalane's high molecular weight (C₃₀H₆₂). Squalane is a widely used viscosity reference fluid, making these data especially valuable for equation-of-state and transport-property model benchmarking under pressure.

---

### Paper 2 — Chlorobutane Isomers + Diisopropyl Ether (atmospheric pressure)
**DOI:** 10.1007/s10765-010-0737-5 (GLOBlit_97)

| System | Density Block | Viscosity Block | T range (K) | P (kPa) | x(chlorobutane) range | n points |
|--------|--------------|----------------|-------------|---------|----------------------|----------|
| 1-Chlorobutane + diisopropyl ether | PROPblock_12 | PROPblock_11 | 283.15–313.15 | 101.0 | 0.0–1.0 | 91 each |
| 2-Chlorobutane + diisopropyl ether | PROPblock_14 | PROPblock_13 | 283.15–313.15 | 101.0 | 0.0–1.0 | 90–91 |
| 1-Chloro-2-methylpropane + diisopropyl ether | PROPblock_16 | PROPblock_15 | 283.15–313.15 | 101.0 | 0.0–1.0 | 91 each |
| 2-Chloro-2-methylpropane + diisopropyl ether | PROPblock_18 | PROPblock_17 | 283.15–313.15 | 101.0 | 0.0–1.0 | 91 each |

Density spans 702.378–897.339 kg/m³; viscosity spans 0.000272–0.000598 Pa·s. The four C₄H₉Cl isomers (linear, secondary, isobutyl, and tert-butyl chloride) with a common ether partner provide a systematic probe of how branching and chlorine position affect both properties.

---

### Paper 3 — Butan-1-ol + TEGDME (atmospheric pressure, three properties)
**DOI:** 10.1007/s10765-013-1469-0 (GLOBlit_151)

| Property | Block | T range (K) | P (kPa) | x(butan-1-ol) range | n points |
|----------|-------|-------------|---------|---------------------|----------|
| Mass density | PROPblock_7 | 288.15–333.15 | 101.0 | 0.0–1.0 | 110 |
| Dynamic viscosity | PROPblock_8 | 288.15–333.15 | 101.0 | 0.0–1.0 | 110 |
| Refractive index | PROPblock_9 | 288.15–333.15 | 101.0 | 0.0–1.0 | 110 |

Density: 778.056–1015.63 kg/m³; viscosity: 0.001104–0.004341 Pa·s; refractive index: 1.38237–1.4345. The alcohol + polyether (tetraethylene glycol dimethyl ether) system features hydrogen-bonding interactions that produce strongly non-ideal mixing, making it a stringent test for predictive models. A bonus: refractive index is also available for multi-property validation.

---

### Recommended Starting Set of Three Systems

For maximum diversity in chemistry, conditions, and model-testing value, I recommend one system from each paper:

1. **Octane + squalane** (from DOI 10.1007/s10765-006-0053-2, GLOBlit_25) — Non-polar hydrocarbon pair with high-pressure data (up to 30 000 kPa), full composition range (x = 0.0–1.0), and a very wide viscosity span (0.000351–0.2614 Pa·s). Ideal for testing pressure-dependent transport models.

2. **1-Chlorobutane + diisopropyl ether** (from DOI 10.1007/s10765-010-0737-5, GLOBlit_97) — Weakly polar/dispersion-dominated system at atmospheric pressure with 91 data points across 13 compositions and 7 temperatures. The three companion isomer systems in the same paper allow immediate extension to a structural-isomer study.

3. **Butan-1-ol + TEGDME** (from DOI 10.1007/s10765-013-1469-0, GLOBlit_151) — Hydrogen-bonding system at atmospheric pressure with 110 data points, 11 compositions, and 10 temperatures. The strong non-ideality challenges mixing rules, and the co-measured refractive index adds a third property for multi-objective model testing.

Together these three systems span non-polar, weakly polar, and strongly associating chemistries; atmospheric and high-pressure conditions; and viscosity values covering roughly three orders of magnitude.

</answer>