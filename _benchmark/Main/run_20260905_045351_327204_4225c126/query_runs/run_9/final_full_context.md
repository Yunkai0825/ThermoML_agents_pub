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
| comp | GLOBcomp_2 | ethanol | ethanol |
| comp | GLOBcomp_1 | water | water |
| prop | GLOBprop_1 | mass_density_kg_m3 | Mass density, kg/m3 |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|
| lit | GLOBlit_2092 | 2017-ono-kyo-0 | 10.1016/j.fluid.2017.09.005 |

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find density data for ethanol-water binary mixtures. Determine if data exists at 1000 K, and if not, identify the closes → stored as L1_query_1 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** The ThermoML database contains 29 data blocks with mass density measurements for the ethanol (C₂H₆O, CAS 64-17-5) + water (H₂O, CAS 7732-18-5) binary system, totaling approximately 2,924 raw data points spanning 268.1–618.2 K. There is no density data at or near 1000 K; this temperature far exceeds the normal boiling points and critical temperatures of both components (ethanol T_c ≈ 514 K; water T_c ≈ 647 K). The highest-temperature data, from DOI 10.1016/j.fluid.2017.09.005, covers 523.2–618.2 K at 20,000–40,000 kPa with 72 data points. At 618.2 K and 20,000 kPa, densities range from 619.7 kg/m³ (pure water) down to 250.4 kg/m³ (x(ethanol) = 0.3), reflecting near-critical compressibility of ethanol. At 618.2 K and 40,000 kPa, densities are substantially higher (e.g., 682.3 kg/m³ for pure water, 481.2 kg/m³ for pure ethanol). The maximum temperature in the database is 618.2 K, well below the queried 1000 K, and no data exists to bridge this gap.

**Answer:**

#### Density Data for Ethanol–Water Binary Mixtures

##### Compound and Property Identification
- **Ethanol**: GLOBcomp_2 (C₂H₆O, CAS 64-17-5)
- **Water**: GLOBcomp_1 (H₂O, CAS 7732-18-5)
- **Property**: Mass density (GLOBprop_1, kg/m³)

##### Data Availability Overview

The ThermoML database contains **29 data blocks** with mass density measurements for the ethanol + water binary system, totaling approximately **2,924 raw data points**.

**Temperature range covered: 268.1–618.2 K** (approximately −5 °C to 345 °C).

##### Is There Data at 1000 K?

**No.** There is no density data at or near 1000 K (≈727 °C) for the ethanol–water system in the ThermoML database. This is physically expected: 1000 K is far above the normal boiling points of both ethanol (351.5 K / 78.4 °C) and water (373.15 K / 100 °C), and also above the critical temperatures of both components (ethanol T_c ≈ 514 K; water T_c ≈ 647 K). At 1000 K and moderate pressures, both substances would be supercritical gases with very low density, and experimental measurements in this regime for this mixture are essentially absent from the literature.

##### Closest Available High-Temperature Data

The highest-temperature data block is from:

- **DOI**: 10.1016/j.fluid.2017.09.005 (GLOBlit_2092, PROPblock_3)
- **Temperature range**: 523.2–618.2 K
- **Pressure range**: 20,000–40,000 kPa (200–400 bar)
- **Composition range**: x(ethanol) = 0–1
- **Density range**: 250.4–834.3 kg/m³
- **72 data points**, liquid phase

These are high-pressure supercritical/compressed-liquid measurements — the elevated pressures keep the mixture in a dense fluid state even above the normal boiling points.

##### Representative Data Points (highest available temperatures)

**At 618.2 K (highest T in the database), 20,000 kPa:**

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0」 | 「619.7」 |
| WM_L1#1_Table#1_Row#2 | 「0.2」 | 「281.3」 |
| WM_L1#1_Table#1_Row#3 | 「0.3」 | 「250.4」 |
| WM_L1#1_Table#1_Row#4 | 「1.0」 | 「314.6」 |

**At 618.2 K, 30,000 kPa:**

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0」 | 「656.9」 |
| WM_L1#1_Table#2_Row#2 | 「0.2」 | 「501.5」 |
| WM_L1#1_Table#2_Row#3 | 「0.4」 | 「437.4」 |
| WM_L1#1_Table#2_Row#4 | 「0.6」 | 「420.1」 |
| WM_L1#1_Table#2_Row#5 | 「1.0」 | 「423.8」 |

**At 618.2 K, 40,000 kPa:**

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0」 | 「682.3」 |
| WM_L1#1_Table#3_Row#2 | 「0.2」 | 「561.0」 |
| WM_L1#1_Table#3_Row#3 | 「0.4」 | 「509.1」 |
| WM_L1#1_Table#3_Row#4 | 「1.0」 | 「481.2」 |

##### Chemistry Insight

At 618.2 K and 20,000 kPa, the density drops sharply from pure water (619.7 kg/m³) to intermediate ethanol mole fractions (as low as 250.4 kg/m³ at x = 0.3), reflecting the proximity to ethanol's critical point where the fluid becomes highly compressible. Increasing pressure to 40,000 kPa substantially raises the density across all compositions (e.g., pure water reaches 682.3 kg/m³), demonstrating the strong pressure dependence in this near-critical regime.

The maximum available temperature in the database is 618.2 K — well below the queried 1000 K. No data exists in the ThermoML database to bridge this gap for the ethanol–water system.

**Core claims:**
- The ThermoML database contains no density data at or near 1000 K for the ethanol–water binary system; the maximum temperature covered is 618.2 K.
- The absence of data at 1000 K is physically expected because 1000 K far exceeds the critical temperatures of both ethanol (T_c ≈ 514 K) and water (T_c ≈ 647 K), where both substances would be supercritical gases at moderate pressures.
- The database contains approximately 2,924 raw mass density data points for ethanol–water across 29 data blocks, spanning a temperature range of 268.1–618.2 K.
- The highest-temperature data (618.2 K) come from DOI 10.1016/j.fluid.2017.09.005 at pressures of 20,000–40,000 kPa, with densities ranging from 250.4 to 834.3 kg/m³ depending on composition and pressure.
- At 618.2 K and 20,000 kPa, density drops sharply from pure water (619.7 kg/m³) to as low as 250.4 kg/m³ at x(ethanol) = 0.3, reflecting proximity to ethanol's critical point and high compressibility in this regime.
- Increasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises density across all compositions, demonstrating strong pressure dependence in the near-critical regime.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#4 | 「GLOBlit_2092」 | 「PROPblock_3」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for ethanol + water binary system at 523.2–618.2 K and 20,000–40,000 kPa, 72 data points, liquid phase. DOI: 10.1016/j.fluid.2017.09.005」 |

*Not stored here: 1 verbatim data_inspections table(s); 4 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.



</memory>

## User
[Purpose: Search for density data of ethanol-water mixtures, determine if data exists at 1000 K, and if not, identify the closest available temperature range.]
Find density data for ethanol-water binary mixtures at 1000 K. If no data exists at that temperature, report the closest available temperature range for density measurements of ethanol-water systems.

[Context: Ethanol is C2H5OH (CAS 64-17-5) and water is H2O (CAS 7732-18-5). 1000 K is approximately 727°C, which is far above the normal boiling points of both ethanol (78.37°C) and water (100°C). Liquid-phase density data at this temperature is extremely unlikely. We need to find what temperature range is actually available in the ThermoML database for density of ethanol-water mixtures.]

## Assistant
<summary>Dispatching L1 query to search for density (mass density, GLOBprop_1) data for ethanol-water binary mixtures, looking for data at 1000 K and identifying the available temperature range.</summary>
<tool_call>L1_query(instruction=Search for mass d…, id_catalog=, context=Ethanol is C2H5OH…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** The ThermoML database contains 29 data blocks with mass density measurements for the ethanol (C₂H₆O, CAS 64-17-5) + water (H₂O, CAS 7732-18-5) binary system, totaling approximately 2,924 raw data points spanning 268.1–618.2 K. There is no density data at or near 1000 K; this temperature far exceeds the normal boiling points and critical temperatures of both components (ethanol T_c ≈ 514 K; water T_c ≈ 647 K). The highest-temperature data, from DOI 10.1016/j.fluid.2017.09.005, covers 523.2–618.2 K at 20,000–40,000 kPa with 72 data points. At 618.2 K and 20,000 kPa, densities range from 619.7 kg/m³ (pure water) down to 250.4 kg/m³ (x(ethanol) = 0.3), reflecting near-critical compressibility of ethanol. At 618.2 K and 40,000 kPa, densities are substantially higher (e.g., 682.3 kg/m³ for pure water, 481.2 kg/m³ for pure ethanol). The maximum temperature in the database is 618.2 K, well below the queried 1000 K, and no data exists to bridge this gap.

**Answer:**

#### Density Data for Ethanol–Water Binary Mixtures

##### Compound and Property Identification
- **Ethanol**: GLOBcomp_2 (C₂H₆O, CAS 64-17-5)
- **Water**: GLOBcomp_1 (H₂O, CAS 7732-18-5)
- **Property**: Mass density (GLOBprop_1, kg/m³)

##### Data Availability Overview

The ThermoML database contains **29 data blocks** with mass density measurements for the ethanol + water binary system, totaling approximately **2,924 raw data points**.

**Temperature range covered: 268.1–618.2 K** (approximately −5 °C to 345 °C).

##### Is There Data at 1000 K?

**No.** There is no density data at or near 1000 K (≈727 °C) for the ethanol–water system in the ThermoML database. This is physically expected: 1000 K is far above the normal boiling points of both ethanol (351.5 K / 78.4 °C) and water (373.15 K / 100 °C), and also above the critical temperatures of both components (ethanol T_c ≈ 514 K; water T_c ≈ 647 K). At 1000 K and moderate pressures, both substances would be supercritical gases with very low density, and experimental measurements in this regime for this mixture are essentially absent from the literature.

##### Closest Available High-Temperature Data

The highest-temperature data block is from:

- **DOI**: 10.1016/j.fluid.2017.09.005 (GLOBlit_2092, PROPblock_3)
- **Temperature range**: 523.2–618.2 K
- **Pressure range**: 20,000–40,000 kPa (200–400 bar)
- **Composition range**: x(ethanol) = 0–1
- **Density range**: 250.4–834.3 kg/m³
- **72 data points**, liquid phase

These are high-pressure supercritical/compressed-liquid measurements — the elevated pressures keep the mixture in a dense fluid state even above the normal boiling points.

##### Representative Data Points (highest available temperatures)

**At 618.2 K (highest T in the database), 20,000 kPa:**

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| L1#1_Table#1_Row#1 | 「0」 | 「619.7」 |
| L1#1_Table#1_Row#2 | 「0.2」 | 「281.3」 |
| L1#1_Table#1_Row#3 | 「0.3」 | 「250.4」 |
| L1#1_Table#1_Row#4 | 「1.0」 | 「314.6」 |

**At 618.2 K, 30,000 kPa:**

**L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| L1#1_Table#2_Row#1 | 「0」 | 「656.9」 |
| L1#1_Table#2_Row#2 | 「0.2」 | 「501.5」 |
| L1#1_Table#2_Row#3 | 「0.4」 | 「437.4」 |
| L1#1_Table#2_Row#4 | 「0.6」 | 「420.1」 |
| L1#1_Table#2_Row#5 | 「1.0」 | 「423.8」 |

**At 618.2 K, 40,000 kPa:**

**L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|
| L1#1_Table#3_Row#1 | 「0」 | 「682.3」 |
| L1#1_Table#3_Row#2 | 「0.2」 | 「561.0」 |
| L1#1_Table#3_Row#3 | 「0.4」 | 「509.1」 |
| L1#1_Table#3_Row#4 | 「1.0」 | 「481.2」 |

##### Chemistry Insight

At 618.2 K and 20,000 kPa, the density drops sharply from pure water (619.7 kg/m³) to intermediate ethanol mole fractions (as low as 250.4 kg/m³ at x = 0.3), reflecting the proximity to ethanol's critical point where the fluid becomes highly compressible. Increasing pressure to 40,000 kPa substantially raises the density across all compositions (e.g., pure water reaches 682.3 kg/m³), demonstrating the strong pressure dependence in this near-critical regime.

The maximum available temperature in the database is 618.2 K — well below the queried 1000 K. No data exists in the ThermoML database to bridge this gap for the ethanol–water system.

**Core claims:**
- The ThermoML database contains no density data at or near 1000 K for the ethanol–water binary system; the maximum temperature covered is 618.2 K.
- The absence of data at 1000 K is physically expected because 1000 K far exceeds the critical temperatures of both ethanol (T_c ≈ 514 K) and water (T_c ≈ 647 K), where both substances would be supercritical gases at moderate pressures.
- The database contains approximately 2,924 raw mass density data points for ethanol–water across 29 data blocks, spanning a temperature range of 268.1–618.2 K.
- The highest-temperature data (618.2 K) come from DOI 10.1016/j.fluid.2017.09.005 at pressures of 20,000–40,000 kPa, with densities ranging from 250.4 to 834.3 kg/m³ depending on composition and pressure.
- At 618.2 K and 20,000 kPa, density drops sharply from pure water (619.7 kg/m³) to as low as 250.4 kg/m³ at x(ethanol) = 0.3, reflecting proximity to ethanol's critical point and high compressibility in this regime.
- Increasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises density across all compositions, demonstrating strong pressure dependence in the near-critical regime.

**Core ID updates:**
- add GLOBcomp_2 — ethanol (registry: ethanol)
- add GLOBcomp_1 — water (registry: water)
- add GLOBprop_1 — Mass density, kg/m3 (registry: mass_density_kg_m3)
- add GLOBlit_2092 — 10.1016/j.fluid.2017.09.005 (registry: 2017-ono-kyo-0)

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#4_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_2092 | lit_id: 2017-ono-kyo-0 | doi: 10.1016/j.fluid.2017.09.005
block: PROPblock_3 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 72
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_3; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density measurements for ethanol + water binary system at 523.2–618.2 K and 20,000–40,000 kPa, 72 data points, liquid phase. DOI: 10.1016/j.fluid.2017.09.005

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#4_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=523.2–618.2 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#4_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_3」 | 「Pressure, kPa」 | 「range=20000.0–40000.0 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#4_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0–1.0 · n_unique=8 · phase=Liquid」 |
| L1#1_Table#4_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=250.4–834.3 · mean=569.888889 · n=72 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#5_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_2092 | doi: 10.1016/j.fluid.2017.09.005 | block: PROPblock_3
table_mode: rdp | inspection_id: INSP_c6457ac47ddc | rows_shown: 41

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mole_fraction_<ethanol>* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| L1#1_Table#5_Row#1 | 「BLKpoint_1」 | 「523.2」 | 「20000」 | 「0」 | 「816.1」 |
| L1#1_Table#5_Row#2 | 「BLKpoint_3」 | 「523.2」 | 「20000」 | 「0.2」 | 「694.1」 |
| L1#1_Table#5_Row#3 | 「BLKpoint_5」 | 「523.2」 | 「20000」 | 「0.4」 | 「622.3」 |
| L1#1_Table#5_Row#4 | 「BLKpoint_6」 | 「523.2」 | 「20000」 | 「0.6」 | 「578.5」 |
| L1#1_Table#5_Row#5 | 「BLKpoint_8」 | 「523.2」 | 「20000」 | 「1」 | 「533.1」 |
| L1#1_Table#5_Row#6 | 「BLKpoint_9」 | 「523.2」 | 「30000」 | 「0」 | 「825.5」 |
| L1#1_Table#5_Row#7 | 「BLKpoint_11」 | 「523.2」 | 「30000」 | 「0.2」 | 「713.6」 |
| L1#1_Table#5_Row#8 | 「BLKpoint_13」 | 「523.2」 | 「30000」 | 「0.4」 | 「650.7」 |
| L1#1_Table#5_Row#9 | 「BLKpoint_14」 | 「523.2」 | 「30000」 | 「0.6」 | 「612.4」 |
| L1#1_Table#5_Row#10 | 「BLKpoint_16」 | 「523.2」 | 「30000」 | 「1」 | 「573.6」 |
| L1#1_Table#5_Row#11 | 「BLKpoint_17」 | 「523.2」 | 「40000」 | 「0」 | 「834.3」 |
| L1#1_Table#5_Row#12 | 「BLKpoint_20」 | 「523.2」 | 「40000」 | 「0.3」 | 「694.7」 |
| L1#1_Table#5_Row#13 | 「BLKpoint_22」 | 「523.2」 | 「40000」 | 「0.6」 | 「636.3」 |
| L1#1_Table#5_Row#14 | 「BLKpoint_24」 | 「523.2」 | 「40000」 | 「1」 | 「601.3」 |
| L1#1_Table#5_Row#15 | 「BLKpoint_25」 | 「573.2」 | 「20000」 | 「0」 | 「734.8」 |
| L1#1_Table#5_Row#16 | 「BLKpoint_27」 | 「573.2」 | 「20000」 | 「0.2」 | 「585.4」 |
| L1#1_Table#5_Row#17 | 「BLKpoint_29」 | 「573.2」 | 「20000」 | 「0.4」 | 「494.9」 |
| L1#1_Table#5_Row#18 | 「BLKpoint_30」 | 「573.2」 | 「20000」 | 「0.6」 | 「446.2」 |
| L1#1_Table#5_Row#19 | 「BLKpoint_32」 | 「573.2」 | 「20000」 | 「1」 | 「421.1」 |
| L1#1_Table#5_Row#20 | 「BLKpoint_33」 | 「573.2」 | 「30000」 | 「0」 | 「750.7」 |
| L1#1_Table#5_Row#21 | 「BLKpoint_35」 | 「573.2」 | 「30000」 | 「0.2」 | 「621.4」 |
| L1#1_Table#5_Row#22 | 「BLKpoint_37」 | 「573.2」 | 「30000」 | 「0.4」 | 「553.5」 |
| L1#1_Table#5_Row#23 | 「BLKpoint_38」 | 「573.2」 | 「30000」 | 「0.6」 | 「517.6」 |
| L1#1_Table#5_Row#24 | 「BLKpoint_40」 | 「573.2」 | 「30000」 | 「1」 | 「491.5」 |
| L1#1_Table#5_Row#25 | 「BLKpoint_41」 | 「573.2」 | 「40000」 | 「0」 | 「764.3」 |
| L1#1_Table#5_Row#26 | 「BLKpoint_43」 | 「573.2」 | 「40000」 | 「0.2」 | 「647.6」 |
| L1#1_Table#5_Row#27 | 「BLKpoint_45」 | 「573.2」 | 「40000」 | 「0.4」 | 「587.9」 |
| L1#1_Table#5_Row#28 | 「BLKpoint_48」 | 「573.2」 | 「40000」 | 「1」 | 「531」 |
| L1#1_Table#5_Row#29 | 「BLKpoint_49」 | 「618.2」 | 「20000」 | 「0」 | 「619.7」 |
| L1#1_Table#5_Row#30 | 「BLKpoint_51」 | 「618.2」 | 「20000」 | 「0.2」 | 「281.3」 |
| L1#1_Table#5_Row#31 | 「BLKpoint_52」 | 「618.2」 | 「20000」 | 「0.3」 | 「250.4」 |
| L1#1_Table#5_Row#32 | 「BLKpoint_56」 | 「618.2」 | 「20000」 | 「1」 | 「314.6」 |
| L1#1_Table#5_Row#33 | 「BLKpoint_57」 | 「618.2」 | 「30000」 | 「0」 | 「656.9」 |
| L1#1_Table#5_Row#34 | 「BLKpoint_59」 | 「618.2」 | 「30000」 | 「0.2」 | 「501.5」 |
| L1#1_Table#5_Row#35 | 「BLKpoint_61」 | 「618.2」 | 「30000」 | 「0.4」 | 「437.4」 |
| L1#1_Table#5_Row#36 | 「BLKpoint_62」 | 「618.2」 | 「30000」 | 「0.6」 | 「420.1」 |
| L1#1_Table#5_Row#37 | 「BLKpoint_64」 | 「618.2」 | 「30000」 | 「1」 | 「423.8」 |
| L1#1_Table#5_Row#38 | 「BLKpoint_65」 | 「618.2」 | 「40000」 | 「0」 | 「682.3」 |
| L1#1_Table#5_Row#39 | 「BLKpoint_67」 | 「618.2」 | 「40000」 | 「0.2」 | 「561」 |
| L1#1_Table#5_Row#40 | 「BLKpoint_69」 | 「618.2」 | 「40000」 | 「0.4」 | 「509.1」 |
| L1#1_Table#5_Row#41 | 「BLKpoint_72」 | 「618.2」 | 「40000」 | 「1」 | 「481.2」 |
```
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
The L1 query has returned comprehensive results. I have all the data needed to provide a complete answer. Let me compile the final answer.
</reasoning>

<answer>

## Density Data for Ethanol–Water Binary Mixtures at 1000 K

### Data at 1000 K: Not Available

There is **no density data at or near 1000 K** (≈727 °C) for the ethanol–water system in the ThermoML database. This is physically expected:

- **Ethanol** (C₂H₆O, CAS 64-17-5) has a normal boiling point of ~351.5 K (78.4 °C) and a critical temperature T_c ≈ 514 K.
- **Water** (H₂O, CAS 7732-18-5) has a normal boiling point of ~373.15 K (100 °C) and a critical temperature T_c ≈ 647 K.

At 1000 K and moderate pressures, both substances would be supercritical gases with very low density, making experimental liquid-phase density measurements essentially impossible for this mixture.

---

### Closest Available Temperature Range

The ThermoML database contains **29 data blocks** with mass density measurements for the ethanol + water binary system, totaling approximately **2,924 raw data points** spanning **268.1–618.2 K** (approximately −5 °C to 345 °C).

The **highest-temperature data** comes from:

- **Source:** DOI 10.1016/j.fluid.2017.09.005 (GLOBlit_2092)
- **Block:** PROPblock_3
- **Temperature range:** 523.2–618.2 K (250–345 °C)
- **Pressure range:** 20,000–40,000 kPa (200–400 bar)
- **Composition range:** x(ethanol) = 0–1
- **Overall density range:** 250.4–834.3 kg/m³
- **72 data points**, liquid phase, measured by vibrating tube method

These are high-pressure supercritical/compressed-liquid measurements — the elevated pressures keep the mixture in a dense fluid state even above the normal boiling points.

---

### Representative Data at the Highest Available Temperature (618.2 K)

**At 618.2 K, 20,000 kPa:**

| x(ethanol) | ρ (kg/m³) |
|:----------:|:---------:|
| 0          | 619.7     |
| 0.2        | 281.3     |
| 0.3        | 250.4     |
| 1.0        | 314.6     |

**At 618.2 K, 30,000 kPa:**

| x(ethanol) | ρ (kg/m³) |
|:----------:|:---------:|
| 0          | 656.9     |
| 0.2        | 501.5     |
| 0.4        | 437.4     |
| 0.6        | 420.1     |
| 1.0        | 423.8     |

**At 618.2 K, 40,000 kPa:**

| x(ethanol) | ρ (kg/m³) |
|:----------:|:---------:|
| 0          | 682.3     |
| 0.2        | 561.0     |
| 0.4        | 509.1     |
| 1.0        | 481.2     |

---

### Chemistry Insight

At 618.2 K and 20,000 kPa, the density drops sharply from pure water (619.7 kg/m³) to intermediate ethanol mole fractions — reaching as low as 250.4 kg/m³ at x(ethanol) = 0.3. This dramatic non-monotonic behavior reflects the proximity to ethanol's critical point (T_c ≈ 514 K), where the fluid becomes highly compressible and density is extremely sensitive to composition. Notably, pure ethanol at this condition (314.6 kg/m³) is actually denser than the x = 0.3 mixture, illustrating the complex interplay of near-critical fluctuations in the mixture.

Increasing pressure from 20,000 to 40,000 kPa at 618.2 K substantially raises the density across all compositions (e.g., pure water: 619.7 → 682.3 kg/m³; pure ethanol: 314.6 → 481.2 kg/m³), demonstrating the strong pressure dependence characteristic of near-critical and supercritical fluids.

**The maximum available temperature in the ThermoML database for ethanol–water density is 618.2 K — approximately 382 K below the queried 1000 K, with no data to bridge this gap.**

</answer>