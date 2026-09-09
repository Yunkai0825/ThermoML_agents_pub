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
| comp | GLOBcomp_4 | methanol | methanol |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find mass density (GLOBprop_1) data for ethanol + water binary mixtures. Report the number of data blocks, temperature r → stored as L1_query_1 · validation: PASS
- [L1] Find mass density (GLOBprop_1) data for methanol + water binary mixtures. Report the number of data blocks, DOIs, total  → stored as L1_query_2 · validation: FLAGGED(8)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** The ThermoML database contains 29 data blocks across 22 DOIs reporting mass density (kg/m³) for the ethanol + water binary system, totaling approximately 2,920 data points. Coverage spans temperatures of 268.1–618.2 K, pressures from 100 kPa to 40,000 kPa, and the full ethanol mole fraction range (0–1). One of the largest blocks (DOI 10.1016/j.fluid.2004.11.019, 810 data points, 298.15–348.15 K, 100–40,000 kPa) provides representative values at T = 298.15 K and P = 100 kPa: density decreases monotonically from 995.3 kg/m³ at x(ethanol) = 0.003 to 785.7 kg/m³ at x(ethanol) = 1.0. The decrease is steepest in the water-rich region (x < 0.1), reflecting non-linear excess volume effects from disruption of water's hydrogen-bonding network by small amounts of ethanol. The dataset offers dense composition coverage (54 points at atmospheric pressure and 298.15 K in a single block) and is well-suited for liquid density model validation.

**Answer:**

#### Ethanol + Water Binary Mixture: Mass Density Data Summary

##### Overview

The ThermoML database contains **29 data blocks across 22 DOIs** (block count from the search_blocks result) reporting mass density (kg/m³) for the ethanol + water binary system.

##### Coverage

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Parameter* | *Range* |
|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「**Temperature**」 | 「268.1 – 618.2 K」 |
| WM_L1#1_Table#1_Row#2 | 「**Pressure**」 | 「Ambient (100 kPa) to 40,000 kPa (40 MPa)」 |
| WM_L1#1_Table#1_Row#3 | 「**Ethanol mole fraction**」 | 「0 – 1 (full composition range)」 |
| WM_L1#1_Table#1_Row#4 | 「**Total data points**」 | 「~2,920」 |

##### Representative Data Block

One of the largest blocks is from DOI 10.1016/j.fluid.2004.11.019 (GLOBlit_220, PROPblock_2), containing **810 data points** covering 298.15–348.15 K and pressures from 100–40,000 kPa.

Below are representative density values at **T = 298.15 K, P = 100 kPa** across the full ethanol mole fraction range (the inspection tool returned a shape-preserving RDP selection of the 54 matched rows):

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *Density (kg/m³)* |
|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「0.003」 | 「995.3」 |
| WM_L1#1_Table#2_Row#2 | 「0.0184」 | 「988.4」 |
| WM_L1#1_Table#2_Row#3 | 「0.0279」 | 「984.7」 |
| WM_L1#1_Table#2_Row#4 | 「0.0483」 | 「977.5」 |
| WM_L1#1_Table#2_Row#5 | 「0.0801」 | 「968.6」 |
| WM_L1#1_Table#2_Row#6 | 「0.1296」 | 「954.9」 |
| WM_L1#1_Table#2_Row#7 | 「0.2502」 | 「918.5」 |
| WM_L1#1_Table#2_Row#8 | 「0.3009」 | 「904.5」 |
| WM_L1#1_Table#2_Row#9 | 「0.35」 | 「891.9」 |
| WM_L1#1_Table#2_Row#10 | 「0.4501」 | 「868.8」 |
| WM_L1#1_Table#2_Row#11 | 「0.498」 | 「859.3」 |
| WM_L1#1_Table#2_Row#12 | 「0.5501」 | 「849.5」 |
| WM_L1#1_Table#2_Row#13 | 「0.6489」 | 「832.7」 |
| WM_L1#1_Table#2_Row#14 | 「0.6967」 | 「825.2」 |
| WM_L1#1_Table#2_Row#15 | 「0.8484」 | 「804.4」 |
| WM_L1#1_Table#2_Row#16 | 「1.0」 | 「785.7」 |

##### Chemistry Insight

The density decreases monotonically from ~995 kg/m³ (nearly pure water) to ~786 kg/m³ (pure ethanol) at 298.15 K and atmospheric pressure (values from the inspected rows above). The decrease is steepest in the water-rich region (x < 0.1), reflecting the strong disruption of water's hydrogen-bonding network by even small amounts of ethanol. This non-linear composition dependence — with excess volume effects most pronounced in the dilute-ethanol region — is a well-known feature of the ethanol–water system and is important for liquid density model validation.

The dataset is well-suited for model validation near room temperature, with dense composition coverage at 298.15 K (54 points at atmospheric pressure alone in this single block) and additional high-pressure and elevated-temperature data across the many other blocks identified by the search.

**Core claims:**
- The ThermoML database contains 29 data blocks across 22 DOIs reporting mass density (kg/m³) for the ethanol + water binary system, covering approximately 2,920 total data points.
- The data span temperatures of 268.1–618.2 K, pressures from ambient (100 kPa) to 40,000 kPa (40 MPa), and the full ethanol mole fraction range (0–1).
- At 298.15 K and 100 kPa, the density decreases monotonically from ~995 kg/m³ (nearly pure water) to ~786 kg/m³ (pure ethanol), with the steepest decrease in the water-rich region (x < 0.1).
- The non-linear composition dependence of density, with excess volume effects most pronounced in the dilute-ethanol region, reflects the strong disruption of water's hydrogen-bonding network by small amounts of ethanol.
- One of the largest blocks (DOI 10.1016/j.fluid.2004.11.019) contains 810 data points covering 298.15–348.15 K and pressures from 100–40,000 kPa, with 54 points at 298.15 K and atmospheric pressure alone.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_220」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density data for ethanol + water binary mixture, 810 data points, 298.15–348.15 K, 100–40000 kPa, full ethanol mole fraction range.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: success · validation: FLAGGED(8)

**Summary:** The ThermoML database contains approximately 18 data blocks across 15 DOIs reporting mass density (kg/m³) for the methanol + water binary system, totaling roughly 1,610 data points (these aggregate counts are from a search-level summary, not individually verified). Two blocks were inspected in detail. GLOBlit_8254::PROPblock_4 (DOI: 10.1021/je034101z) contains 401 data points of absolute density at elevated pressures, covering T = 287.15–417.15 K, P = 3,721–29,927 kPa, x(MeOH) = 0.059–0.708, and ρ = 762.2–966 kg/m³. GLOBlit_2825::PROPblock_10 (DOI: 10.1016/j.jct.2007.05.004) contains 39 data points at atmospheric pressure (101 kPa), T = 293.15–303.15 K, spanning the full composition range. At T = 298.15 K and P = 101 kPa, representative densities from GLOBlit_2825::PROPblock_10 range from 787.2 kg/m³ (pure methanol, x(water) = 0) through 881.69 kg/m³ (x(water) = 0.5003) to 997.05 kg/m³ (pure water, x(water) = 1). Specific reported values include x(water) = 0.049 → 795.47, 0.0993 → 804.11, 0.1973 → 821.73, 0.2983 → 840.79, 0.3985 → 860.59, 0.5994 → 902.96, 0.7986 → 947.17, 0.8999 → 969.84, and 0.9512 → 982.53 kg/m³. The dataset is smaller than the ethanol + water density dataset but provides good coverage for liquid density model validation, particularly at atmospheric pressure and near-ambient temperatures.

**Answer:**

###### Methanol + Water Binary Mixture: Mass Density Data Summary

####### Overview

The ThermoML database contains **18 data blocks across 15 DOIs** reporting mass density (kg/m³) for the methanol + water binary system, totaling approximately **1,610 data points**. (These aggregate counts — 18, 15, and 1,610 — are from the search_system_registry summary, not from individual block inspections.)

####### Coverage

**WM_L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *Parameter* | *Range* |
|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「**Temperature**」 | 「Not fully inspected in this run; the search_blocks summary reported 273.15–618.2 K (search-level aggregate, not block-inspected)」 |
| WM_L1#2_Table#1_Row#2 | 「**Pressure**」 | 「Ranges from atmospheric (101 kPa, confirmed in GLOBlit_2825::PROPblock_10) to high pressure (up to 29,927 kPa confirmed in GLOBlit_8254::PROPblock_4); search-level summary reported up to 40,000 kPa (not block-inspected)」 |
| WM_L1#2_Table#1_Row#3 | 「**Methanol mole fraction**」 | 「0 – 1 (full composition range, confirmed in GLOBlit_2825::PROPblock_10)」 |

####### Inspected Blocks

**GLOBlit_8254::PROPblock_4** (DOI: 10.1021/je034101z) — 401 data points; absolute density at elevated pressures. Inspected stats: T = 287.15–417.15 K; P = 3,721–29,927 kPa; x(MeOH) = 0.059–0.708; ρ = 762.2–966 kg/m³.

**GLOBlit_2825::PROPblock_10** (DOI: 10.1016/j.jct.2007.05.004) — 39 data points at atmospheric pressure (101 kPa); T = 293.15–303.15 K; full composition range. This is the most suitable block for room-temperature, atmospheric-pressure density data.

####### Representative Density Data at T = 298.15 K, P = 101 kPa

From GLOBlit_2825::PROPblock_10, 13 data points at T = 298.15 K (the block variable is mole fraction of water; x(methanol) = 1 − x(water) is a derived quantity):

**WM_L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *x(water)* | *Density (kg/m³)* |
|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「0」 | 「787.2」 |
| WM_L1#2_Table#2_Row#2 | 「0.049」 | 「795.47」 |
| WM_L1#2_Table#2_Row#3 | 「0.0993」 | 「804.11」 |
| WM_L1#2_Table#2_Row#4 | 「0.1973」 | 「821.73」 |
| WM_L1#2_Table#2_Row#5 | 「0.2983」 | 「840.79」 |
| WM_L1#2_Table#2_Row#6 | 「0.3985」 | 「860.59」 |
| WM_L1#2_Table#2_Row#7 | 「0.5003」 | 「881.69」 |
| WM_L1#2_Table#2_Row#8 | 「0.5994」 | 「902.96」 |
| WM_L1#2_Table#2_Row#9 | 「0.7986」 | 「947.17」 |
| WM_L1#2_Table#2_Row#10 | 「0.8999」 | 「969.84」 |
| WM_L1#2_Table#2_Row#11 | 「0.9512」 | 「982.53」 |
| WM_L1#2_Table#2_Row#12 | 「1」 | 「997.05」 |

*12 of 13 matched rows shown (shape-preserving RDP subset of the block's 39 total points).*

####### Chemistry Insight — Comparison with Ethanol + Water

At 298.15 K and atmospheric pressure, the density of the methanol + water system spans from 997.05 kg/m³ (pure water) down to 787.2 kg/m³ (pure methanol). At the equimolar point (x(water) = 0.5003), the density is 881.69 kg/m³.

From the prior context (provided by the user, not inspected in this run), the ethanol + water system was reported to have 29 blocks, ~2,920 points across 22 DOIs, with broader temperature (268.1–618.2 K) and pressure (100–40,000 kPa) coverage. Those ethanol + water statistics are from the prior user-supplied context and were not verified against the database in this run.

The methanol + water dataset (18 blocks, ~1,610 points from the search summary) is smaller but still provides good coverage for liquid density model validation, particularly at atmospheric pressure and near-ambient temperatures.

**Core claims:**
- The ThermoML database contains mass density data for the methanol + water binary system; two inspected blocks (GLOBlit_8254::PROPblock_4 and GLOBlit_2825::PROPblock_10) provide verified coverage at elevated pressures (3,721–29,927 kPa, T = 287.15–417.15 K, x(MeOH) = 0.059–0.708) and at atmospheric pressure (101 kPa, T = 293.15–303.15 K, full composition range), respectively.
- At T = 298.15 K and P = 101 kPa (GLOBlit_2825::PROPblock_10), the mass density of the methanol + water mixture increases monotonically with increasing water mole fraction, from 787.2 kg/m³ at x(water) = 0 (pure methanol) to 997.05 kg/m³ at x(water) = 1 (pure water), with an equimolar value of 881.69 kg/m³ at x(water) = 0.5003.
- Aggregate dataset statistics (18 blocks, ~1,610 points, 15 DOIs, and overall temperature and pressure ranges) are from a search-level summary and were not individually verified by block inspection; several specific values cited for ethanol + water comparison and for overall coverage ranges are flagged as UNVERIFIED.

**Core blocks found:**

**WM_L1#2_Blocks_(Query_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#3 | 「GLOBlit_8254」 | 「PROPblock_4」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water at elevated pressures (3721–29927 kPa), T = 287.15–417.15 K, x(MeOH) = 0.059–0.708; 401 data points.」 |
| WM_L1#2_Table#4 | 「GLOBlit_2825」 | 「PROPblock_10」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of methanol + water at atmospheric pressure (101 kPa), T = 293.15–303.15 K, full composition range; 39 data points.」 |

*Not stored here: 3 verbatim data_inspections table(s); 1 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(8) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10 + GLOBlit_8254::PROPblock_4: 273.15 (near '…y inspected in this run; the search_blocks summary reported …') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10 + GLOBlit_8254::PROPblock_4
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10 + GLOBlit_8254::PROPblock_4: 618.2 (near '…cted in this run; the search_blocks summary reported 273.15–…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10 + GLOBlit_8254::PROPblock_4
- **MISATTRIBUTED_VALUE** GLOBlit_2825::PROPblock_10: 29 does not belong to GLOBlit_2825::PROPblock_10; it matches only GLOBlit_8254::PROPblock_4 (inspected this run)
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10: 2920 (near '…the ethanol + water system was reported to have 29 blocks, ~…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10
- **MISATTRIBUTED_VALUE** GLOBlit_2825::PROPblock_10: 22 does not belong to GLOBlit_2825::PROPblock_10; it matches only GLOBlit_8254::PROPblock_4 (inspected this run)
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10: 268.1 (near '…ks, ~2,920 points across 22 DOIs, with broader temperature (…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10: 618.2 (near '…,920 points across 22 DOIs, with broader temperature (268.1–…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10: 40000 (near '…with broader temperature (268.1–618.2 K) and pressure (100–4…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10



</memory>

## User
For validating a liquid-density model near room temperature, should I use ethanol + water or methanol + water? Which system has measurements over the broader composition and temperature ranges?

## Assistant
<summary>Dispatching two parallel L1 queries to compare mass density data coverage for ethanol+water and methanol+water binary mixtures in the ThermoML database.</summary>
<tool_call>L1_query(instruction=Search for binary…, id_catalog=, context=User wants to com…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** The ThermoML database contains 29 data blocks across 22 DOIs reporting mass density (kg/m³) for the ethanol + water binary system, totaling approximately 2,920 data points. Coverage spans temperatures of 268.1–618.2 K, pressures from 100 kPa to 40,000 kPa, and the full ethanol mole fraction range (0–1). One of the largest blocks (DOI 10.1016/j.fluid.2004.11.019, 810 data points, 298.15–348.15 K, 100–40,000 kPa) provides representative values at T = 298.15 K and P = 100 kPa: density decreases monotonically from 995.3 kg/m³ at x(ethanol) = 0.003 to 785.7 kg/m³ at x(ethanol) = 1.0. The decrease is steepest in the water-rich region (x < 0.1), reflecting non-linear excess volume effects from disruption of water's hydrogen-bonding network by small amounts of ethanol. The dataset offers dense composition coverage (54 points at atmospheric pressure and 298.15 K in a single block) and is well-suited for liquid density model validation.

**Answer:**

#### Ethanol + Water Binary Mixture: Mass Density Data Summary

##### Overview

The ThermoML database contains **29 data blocks across 22 DOIs** (block count from the search_blocks result) reporting mass density (kg/m³) for the ethanol + water binary system.

##### Coverage

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Parameter* | *Range* |
|---|---|---|
| L1#1_Table#1_Row#1 | 「**Temperature**」 | 「268.1 – 618.2 K」 |
| L1#1_Table#1_Row#2 | 「**Pressure**」 | 「Ambient (100 kPa) to 40,000 kPa (40 MPa)」 |
| L1#1_Table#1_Row#3 | 「**Ethanol mole fraction**」 | 「0 – 1 (full composition range)」 |
| L1#1_Table#1_Row#4 | 「**Total data points**」 | 「~2,920」 |

##### Representative Data Block

One of the largest blocks is from DOI 10.1016/j.fluid.2004.11.019 (GLOBlit_220, PROPblock_2), containing **810 data points** covering 298.15–348.15 K and pressures from 100–40,000 kPa.

Below are representative density values at **T = 298.15 K, P = 100 kPa** across the full ethanol mole fraction range (the inspection tool returned a shape-preserving RDP selection of the 54 matched rows):

**L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *x(ethanol)* | *Density (kg/m³)* |
|---|---|---|
| L1#1_Table#2_Row#1 | 「0.003」 | 「995.3」 |
| L1#1_Table#2_Row#2 | 「0.0184」 | 「988.4」 |
| L1#1_Table#2_Row#3 | 「0.0279」 | 「984.7」 |
| L1#1_Table#2_Row#4 | 「0.0483」 | 「977.5」 |
| L1#1_Table#2_Row#5 | 「0.0801」 | 「968.6」 |
| L1#1_Table#2_Row#6 | 「0.1296」 | 「954.9」 |
| L1#1_Table#2_Row#7 | 「0.2502」 | 「918.5」 |
| L1#1_Table#2_Row#8 | 「0.3009」 | 「904.5」 |
| L1#1_Table#2_Row#9 | 「0.35」 | 「891.9」 |
| L1#1_Table#2_Row#10 | 「0.4501」 | 「868.8」 |
| L1#1_Table#2_Row#11 | 「0.498」 | 「859.3」 |
| L1#1_Table#2_Row#12 | 「0.5501」 | 「849.5」 |
| L1#1_Table#2_Row#13 | 「0.6489」 | 「832.7」 |
| L1#1_Table#2_Row#14 | 「0.6967」 | 「825.2」 |
| L1#1_Table#2_Row#15 | 「0.8484」 | 「804.4」 |
| L1#1_Table#2_Row#16 | 「1.0」 | 「785.7」 |

##### Chemistry Insight

The density decreases monotonically from ~995 kg/m³ (nearly pure water) to ~786 kg/m³ (pure ethanol) at 298.15 K and atmospheric pressure (values from the inspected rows above). The decrease is steepest in the water-rich region (x < 0.1), reflecting the strong disruption of water's hydrogen-bonding network by even small amounts of ethanol. This non-linear composition dependence — with excess volume effects most pronounced in the dilute-ethanol region — is a well-known feature of the ethanol–water system and is important for liquid density model validation.

The dataset is well-suited for model validation near room temperature, with dense composition coverage at 298.15 K (54 points at atmospheric pressure alone in this single block) and additional high-pressure and elevated-temperature data across the many other blocks identified by the search.

**Core claims:**
- The ThermoML database contains 29 data blocks across 22 DOIs reporting mass density (kg/m³) for the ethanol + water binary system, covering approximately 2,920 total data points.
- The data span temperatures of 268.1–618.2 K, pressures from ambient (100 kPa) to 40,000 kPa (40 MPa), and the full ethanol mole fraction range (0–1).
- At 298.15 K and 100 kPa, the density decreases monotonically from ~995 kg/m³ (nearly pure water) to ~786 kg/m³ (pure ethanol), with the steepest decrease in the water-rich region (x < 0.1).
- The non-linear composition dependence of density, with excess volume effects most pronounced in the dilute-ethanol region, reflects the strong disruption of water's hydrogen-bonding network by small amounts of ethanol.
- One of the largest blocks (DOI 10.1016/j.fluid.2004.11.019) contains 810 data points covering 298.15–348.15 K and pressures from 100–40,000 kPa, with 54 points at 298.15 K and atmospheric pressure alone.

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#3_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_220 | lit_id: 2005-pec-dol-0 | doi: 10.1016/j.fluid.2004.11.019
block: PROPblock_2 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 810
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_2; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density data for ethanol + water binary mixture, 810 data points, 298.15–348.15 K, 100–40000 kPa, full ethanol mole fraction range.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#3_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–348.15 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#3_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_3」 | 「Pressure, kPa」 | 「range=100.0–40000.0 · n_unique=5 · phase=Liquid」 |
| L1#1_Table#3_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.003–1.0 · n_unique=54 · phase=Liquid」 |
| L1#1_Table#3_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:2 (GLOBmeas_138) · range=739.4–1012.7 · mean=923.644444 · n=810 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#4_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_220 | doi: 10.1016/j.fluid.2004.11.019 | block: PROPblock_2
table_mode: rdp | inspection_id: INSP_1061f889512c | rows_shown: 21

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mole_fraction_<ethanol>* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| L1#1_Table#4_Row#1 | 「BLKpoint_1」 | 「298.15」 | 「100」 | 「0.003」 | 「995.3」 |
| L1#1_Table#4_Row#2 | 「BLKpoint_6」 | 「298.15」 | 「100」 | 「0.0184」 | 「988.4」 |
| L1#1_Table#4_Row#3 | 「BLKpoint_7」 | 「298.15」 | 「100」 | 「0.0219」 | 「987.6」 |
| L1#1_Table#4_Row#4 | 「BLKpoint_9」 | 「298.15」 | 「100」 | 「0.0279」 | 「984.7」 |
| L1#1_Table#4_Row#5 | 「BLKpoint_10」 | 「298.15」 | 「100」 | 「0.0315」 | 「984」 |
| L1#1_Table#4_Row#6 | 「BLKpoint_11」 | 「298.15」 | 「100」 | 「0.0366」 | 「981.6」 |
| L1#1_Table#4_Row#7 | 「BLKpoint_14」 | 「298.15」 | 「100」 | 「0.0483」 | 「977.5」 |
| L1#1_Table#4_Row#8 | 「BLKpoint_15」 | 「298.15」 | 「100」 | 「0.0516」 | 「977.1」 |
| L1#1_Table#4_Row#9 | 「BLKpoint_21」 | 「298.15」 | 「100」 | 「0.0801」 | 「968.6」 |
| L1#1_Table#4_Row#10 | 「BLKpoint_24」 | 「298.15」 | 「100」 | 「0.0926」 | 「965.6」 |
| L1#1_Table#4_Row#11 | 「BLKpoint_29」 | 「298.15」 | 「100」 | 「0.1296」 | 「954.9」 |
| L1#1_Table#4_Row#12 | 「BLKpoint_38」 | 「298.15」 | 「100」 | 「0.2502」 | 「918.5」 |
| L1#1_Table#4_Row#13 | 「BLKpoint_40」 | 「298.15」 | 「100」 | 「0.3009」 | 「904.5」 |
| L1#1_Table#4_Row#14 | 「BLKpoint_41」 | 「298.15」 | 「100」 | 「0.35」 | 「891.9」 |
| L1#1_Table#4_Row#15 | 「BLKpoint_43」 | 「298.15」 | 「100」 | 「0.4501」 | 「868.8」 |
| L1#1_Table#4_Row#16 | 「BLKpoint_44」 | 「298.15」 | 「100」 | 「0.498」 | 「859.3」 |
| L1#1_Table#4_Row#17 | 「BLKpoint_45」 | 「298.15」 | 「100」 | 「0.5501」 | 「849.5」 |
| L1#1_Table#4_Row#18 | 「BLKpoint_47」 | 「298.15」 | 「100」 | 「0.6489」 | 「832.7」 |
| L1#1_Table#4_Row#19 | 「BLKpoint_48」 | 「298.15」 | 「100」 | 「0.6967」 | 「825.2」 |
| L1#1_Table#4_Row#20 | 「BLKpoint_51」 | 「298.15」 | 「100」 | 「0.8484」 | 「804.4」 |
| L1#1_Table#4_Row#21 | 「BLKpoint_54」 | 「298.15」 | 「100」 | 「1」 | 「785.7」 |
```
</subagent_answer>
</tool_result>

## Assistant
<summary>Received ethanol+water data (already known: 29 blocks, 22 DOIs, ~2920 points, 268.1–618.2 K, 0–40000 kPa). Now need methanol+water mass density data for comparison. Dispatching L1 query for methanol+water.</summary>
<tool_call>L1_query(instruction=Search for all da…, id_catalog=GLOBprop_1: Mass …, context=User wan…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#2 — L1_query return

**Status:** status=success

**Summary:** The ThermoML database contains approximately 18 data blocks across 15 DOIs reporting mass density (kg/m³) for the methanol + water binary system, totaling roughly 1,610 data points (these aggregate counts are from a search-level summary, not individually verified). Two blocks were inspected in detail. GLOBlit_8254::PROPblock_4 (DOI: 10.1021/je034101z) contains 401 data points of absolute density at elevated pressures, covering T = 287.15–417.15 K, P = 3,721–29,927 kPa, x(MeOH) = 0.059–0.708, and ρ = 762.2–966 kg/m³. GLOBlit_2825::PROPblock_10 (DOI: 10.1016/j.jct.2007.05.004) contains 39 data points at atmospheric pressure (101 kPa), T = 293.15–303.15 K, spanning the full composition range. At T = 298.15 K and P = 101 kPa, representative densities from GLOBlit_2825::PROPblock_10 range from 787.2 kg/m³ (pure methanol, x(water) = 0) through 881.69 kg/m³ (x(water) = 0.5003) to 997.05 kg/m³ (pure water, x(water) = 1). Specific reported values include x(water) = 0.049 → 795.47, 0.0993 → 804.11, 0.1973 → 821.73, 0.2983 → 840.79, 0.3985 → 860.59, 0.5994 → 902.96, 0.7986 → 947.17, 0.8999 → 969.84, and 0.9512 → 982.53 kg/m³. The dataset is smaller than the ethanol + water density dataset but provides good coverage for liquid density model validation, particularly at atmospheric pressure and near-ambient temperatures.

**Answer:**

###### Methanol + Water Binary Mixture: Mass Density Data Summary

####### Overview

The ThermoML database contains **18 data blocks across 15 DOIs** reporting mass density (kg/m³) for the methanol + water binary system, totaling approximately **1,610 data points**. (These aggregate counts — 18, 15, and 1,610 — are from the search_system_registry summary, not from individual block inspections.)

####### Coverage

**L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *Parameter* | *Range* |
|---|---|---|
| L1#2_Table#1_Row#1 | 「**Temperature**」 | 「Not fully inspected in this run; the search_blocks summary reported 273.15–618.2 K (search-level aggregate, not block-inspected)」 |
| L1#2_Table#1_Row#2 | 「**Pressure**」 | 「Ranges from atmospheric (101 kPa, confirmed in GLOBlit_2825::PROPblock_10) to high pressure (up to 29,927 kPa confirmed in GLOBlit_8254::PROPblock_4); search-level summary reported up to 40,000 kPa (not block-inspected)」 |
| L1#2_Table#1_Row#3 | 「**Methanol mole fraction**」 | 「0 – 1 (full composition range, confirmed in GLOBlit_2825::PROPblock_10)」 |

####### Inspected Blocks

**GLOBlit_8254::PROPblock_4** (DOI: 10.1021/je034101z) — 401 data points; absolute density at elevated pressures. Inspected stats: T = 287.15–417.15 K; P = 3,721–29,927 kPa; x(MeOH) = 0.059–0.708; ρ = 762.2–966 kg/m³.

**GLOBlit_2825::PROPblock_10** (DOI: 10.1016/j.jct.2007.05.004) — 39 data points at atmospheric pressure (101 kPa); T = 293.15–303.15 K; full composition range. This is the most suitable block for room-temperature, atmospheric-pressure density data.

####### Representative Density Data at T = 298.15 K, P = 101 kPa

From GLOBlit_2825::PROPblock_10, 13 data points at T = 298.15 K (the block variable is mole fraction of water; x(methanol) = 1 − x(water) is a derived quantity):

**L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *x(water)* | *Density (kg/m³)* |
|---|---|---|
| L1#2_Table#2_Row#1 | 「0」 | 「787.2」 |
| L1#2_Table#2_Row#2 | 「0.049」 | 「795.47」 |
| L1#2_Table#2_Row#3 | 「0.0993」 | 「804.11」 |
| L1#2_Table#2_Row#4 | 「0.1973」 | 「821.73」 |
| L1#2_Table#2_Row#5 | 「0.2983」 | 「840.79」 |
| L1#2_Table#2_Row#6 | 「0.3985」 | 「860.59」 |
| L1#2_Table#2_Row#7 | 「0.5003」 | 「881.69」 |
| L1#2_Table#2_Row#8 | 「0.5994」 | 「902.96」 |
| L1#2_Table#2_Row#9 | 「0.7986」 | 「947.17」 |
| L1#2_Table#2_Row#10 | 「0.8999」 | 「969.84」 |
| L1#2_Table#2_Row#11 | 「0.9512」 | 「982.53」 |
| L1#2_Table#2_Row#12 | 「1」 | 「997.05」 |

*12 of 13 matched rows shown (shape-preserving RDP subset of the block's 39 total points).*

####### Chemistry Insight — Comparison with Ethanol + Water

At 298.15 K and atmospheric pressure, the density of the methanol + water system spans from 997.05 kg/m³ (pure water) down to 787.2 kg/m³ (pure methanol). At the equimolar point (x(water) = 0.5003), the density is 881.69 kg/m³.

From the prior context (provided by the user, not inspected in this run), the ethanol + water system was reported to have 29 blocks, ~2,920 points across 22 DOIs, with broader temperature (268.1–618.2 K) and pressure (100–40,000 kPa) coverage. Those ethanol + water statistics are from the prior user-supplied context and were not verified against the database in this run.

The methanol + water dataset (18 blocks, ~1,610 points from the search summary) is smaller but still provides good coverage for liquid density model validation, particularly at atmospheric pressure and near-ambient temperatures.

---
[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10 + GLOBlit_8254::PROPblock_4: 273.15 (near '…y inspected in this run; the search_blocks summary reported …') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10 + GLOBlit_8254::PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_2825::PROPblock_10", nearest={"column": "temperature_k", "value": 273.15})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10 + GLOBlit_8254::PROPblock_4: 618.2 (near '…cted in this run; the search_blocks summary reported 273.15–…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10 + GLOBlit_8254::PROPblock_4
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_2825::PROPblock_10", nearest={"column": "temperature_k", "value": 618.2})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **MISATTRIBUTED_VALUE** GLOBlit_2825::PROPblock_10: 29 does not belong to GLOBlit_2825::PROPblock_10; it matches only GLOBlit_8254::PROPblock_4 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 29 to GLOBlit_8254::PROPblock_4 — no new tool call needed`
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10: 2920 (near '…the ethanol + water system was reported to have 29 blocks, ~…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_2825::PROPblock_10", nearest={"column": "temperature_k", "value": 2920.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **MISATTRIBUTED_VALUE** GLOBlit_2825::PROPblock_10: 22 does not belong to GLOBlit_2825::PROPblock_10; it matches only GLOBlit_8254::PROPblock_4 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 22 to GLOBlit_8254::PROPblock_4 — no new tool call needed`
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10: 268.1 (near '…ks, ~2,920 points across 22 DOIs, with broader temperature (…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_2825::PROPblock_10", nearest={"column": "temperature_k", "value": 268.1})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10: 618.2 (near '…,920 points across 22 DOIs, with broader temperature (268.1–…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_2825::PROPblock_10", nearest={"column": "temperature_k", "value": 618.2})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** GLOBlit_2825::PROPblock_10: 40000 (near '…with broader temperature (268.1–618.2 K) and pressure (100–4…') matches no inspected row/stat, database table, or other source of GLOBlit_2825::PROPblock_10
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_2825::PROPblock_10", nearest={"column": "temperature_k", "value": 40000.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- … and 2 more of the same kinds — GLOBlit_2825::PROPblock_10: 18, 1610
Inspected so far: PROPblock_10, PROPblock_4

**Core claims:**
- The ThermoML database contains mass density data for the methanol + water binary system; two inspected blocks (GLOBlit_8254::PROPblock_4 and GLOBlit_2825::PROPblock_10) provide verified coverage at elevated pressures (3,721–29,927 kPa, T = 287.15–417.15 K, x(MeOH) = 0.059–0.708) and at atmospheric pressure (101 kPa, T = 293.15–303.15 K, full composition range), respectively.
- At T = 298.15 K and P = 101 kPa (GLOBlit_2825::PROPblock_10), the mass density of the methanol + water mixture increases monotonically with increasing water mole fraction, from 787.2 kg/m³ at x(water) = 0 (pure methanol) to 997.05 kg/m³ at x(water) = 1 (pure water), with an equimolar value of 881.69 kg/m³ at x(water) = 0.5003.
- Aggregate dataset statistics (18 blocks, ~1,610 points, 15 DOIs, and overall temperature and pressure ranges) are from a search-level summary and were not individually verified by block inspection; several specific values cited for ethanol + water comparison and for overall coverage ranges are flagged as UNVERIFIED.

**Core ID updates:**
- add GLOBcomp_4 — methanol (registry: methanol)

#### Core blocks found — verbatim ledger

```ledger
**L1#2_Table#3_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_8254 | lit_id: 2003-kit-kag-0 | doi: 10.1021/je034101z
block: PROPblock_4 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 401
compounds: methanol (CH4O; GLOBcomp_4; DOIcomp_2; InChIKey OKKJLVBELUTLKV-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of methanol + water at elevated pressures (3721–29927 kPa), T = 287.15–417.15 K, x(MeOH) = 0.059–0.708; 401 data points.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#3_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of methanol」 | 「range=0.059–0.708 · n_unique=4 · phase=Liquid」 |
| L1#2_Table#3_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_1」 | 「Temperature, K」 | 「range=287.15–417.15 · n_unique=131 · phase=Liquid」 |
| L1#2_Table#3_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_3」 | 「Pressure, kPa」 | 「range=3721.0–29927.0 · n_unique=396 · phase=Liquid」 |
| L1#2_Table#3_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=ISOCHOR (GLOBmeas_170) · range=762.2–966.0 · mean=864.876808 · n=401 · phase=Liquid」 |
```

```ledger
**L1#2_Table#4_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_2825 | lit_id: 2007-gon-cal-1 | doi: 10.1016/j.jct.2007.05.004
block: PROPblock_10 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 39
compounds: methanol (CH4O; GLOBcomp_4; DOIcomp_2; InChIKey OKKJLVBELUTLKV-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of methanol + water at atmospheric pressure (101 kPa), T = 293.15–303.15 K, full composition range; 39 data points.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#4_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#2_Table#4_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=293.15–303.15 · n_unique=3 · phase=Liquid」 |
| L1#2_Table#4_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of water」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#2_Table#4_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:4 (GLOBmeas_134) · range=782.48–998.2 · mean=885.828974 · n=39 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#2_Table#5_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_8254 | doi: 10.1021/je034101z | block: PROPblock_4
table_mode: rdp | inspection_id: INSP_4471b90596fd | rows_shown: 58

| *row_id* | *BLKpoint_id* | *mole_fraction_<methanol>* | *temperature_k* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| L1#2_Table#5_Row#1 | 「BLKpoint_1」 | 「0.059」 | 「346.15」 | 「8815」 | 「966」 |
| L1#2_Table#5_Row#2 | 「BLKpoint_17」 | 「0.059」 | 「362.15」 | 「28959」 | 「964.2」 |
| L1#2_Table#5_Row#3 | 「BLKpoint_18」 | 「0.059」 | 「364.15」 | 「4292」 | 「951.9」 |
| L1#2_Table#5_Row#4 | 「BLKpoint_36」 | 「0.059」 | 「382.15」 | 「28600」 | 「949.8」 |
| L1#2_Table#5_Row#5 | 「BLKpoint_37」 | 「0.059」 | 「385.15」 | 「10606」 | 「937.2」 |
| L1#2_Table#5_Row#6 | 「BLKpoint_50」 | 「0.059」 | 「398.15」 | 「29222」 | 「935.6」 |
| L1#2_Table#5_Row#7 | 「BLKpoint_51」 | 「0.059」 | 「400.15」 | 「5808」 | 「919」 |
| L1#2_Table#5_Row#8 | 「BLKpoint_67」 | 「0.059」 | 「416.15」 | 「29157」 | 「917.2」 |
| L1#2_Table#5_Row#9 | 「BLKpoint_68」 | 「0.352」 | 「291.15」 | 「8041」 | 「933.5」 |
| L1#2_Table#5_Row#10 | 「BLKpoint_83」 | 「0.352」 | 「306.15」 | 「25201」 | 「932.2」 |
| L1#2_Table#5_Row#11 | 「BLKpoint_84」 | 「0.352」 | 「307.15」 | 「3721」 | 「922.5」 |
| L1#2_Table#5_Row#12 | 「BLKpoint_89」 | 「0.352」 | 「309.15」 | 「28914」 | 「931.9」 |
| L1#2_Table#5_Row#13 | 「BLKpoint_90」 | 「0.352」 | 「310.15」 | 「7400」 | 「922.2」 |
| L1#2_Table#5_Row#14 | 「BLKpoint_107」 | 「0.352」 | 「327.15」 | 「28981」 | 「920.6」 |
| L1#2_Table#5_Row#15 | 「BLKpoint_108」 | 「0.352」 | 「331.15」 | 「10996」 | 「909.4」 |
| L1#2_Table#5_Row#16 | 「BLKpoint_121」 | 「0.352」 | 「344.15」 | 「28202」 | 「908」 |
| L1#2_Table#5_Row#17 | 「BLKpoint_122」 | 「0.352」 | 「345.15」 | 「9340」 | 「897.6」 |
| L1#2_Table#5_Row#18 | 「BLKpoint_123」 | 「0.352」 | 「345.15」 | 「29545」 | 「907.9」 |
| L1#2_Table#5_Row#19 | 「BLKpoint_124」 | 「0.352」 | 「346.15」 | 「10663」 | 「897.5」 |
| L1#2_Table#5_Row#20 | 「BLKpoint_137」 | 「0.352」 | 「359.15」 | 「28029」 | 「896.2」 |
| L1#2_Table#5_Row#21 | 「BLKpoint_138」 | 「0.352」 | 「360.15」 | 「8932」 | 「884.8」 |
| L1#2_Table#5_Row#22 | 「BLKpoint_139」 | 「0.352」 | 「360.15」 | 「29375」 | 「896.1」 |
| L1#2_Table#5_Row#23 | 「BLKpoint_140」 | 「0.352」 | 「361.15」 | 「10269」 | 「884.8」 |
| L1#2_Table#5_Row#24 | 「BLKpoint_153」 | 「0.352」 | 「374.15」 | 「27836」 | 「883.4」 |
| L1#2_Table#5_Row#25 | 「BLKpoint_154」 | 「0.352」 | 「378.15」 | 「11440」 | 「870」 |
| L1#2_Table#5_Row#26 | 「BLKpoint_163」 | 「0.352」 | 「387.15」 | 「23492」 | 「869.1」 |
| L1#2_Table#5_Row#27 | 「BLKpoint_164」 | 「0.352」 | 「388.15」 | 「6236」 | 「856.9」 |
| L1#2_Table#5_Row#28 | 「BLKpoint_165」 | 「0.352」 | 「388.15」 | 「24839」 | 「869」 |
| L1#2_Table#5_Row#29 | 「BLKpoint_166」 | 「0.352」 | 「389.15」 | 「7545」 | 「856.8」 |
| L1#2_Table#5_Row#30 | 「BLKpoint_171」 | 「0.352」 | 「391.15」 | 「28891」 | 「868.7」 |
| L1#2_Table#5_Row#31 | 「BLKpoint_172」 | 「0.352」 | 「392.15」 | 「11481」 | 「856.5」 |
| L1#2_Table#5_Row#32 | 「BLKpoint_181」 | 「0.352」 | 「401.15」 | 「23367」 | 「855.6」 |
| L1#2_Table#5_Row#33 | 「BLKpoint_182」 | 「0.352」 | 「402.15」 | 「7258」 | 「843.1」 |
| L1#2_Table#5_Row#34 | 「BLKpoint_183」 | 「0.352」 | 「402.15」 | 「24695」 | 「855.5」 |
| L1#2_Table#5_Row#35 | 「BLKpoint_184」 | 「0.352」 | 「403.15」 | 「8545」 | 「843.1」 |
| L1#2_Table#5_Row#36 | 「BLKpoint_189」 | 「0.352」 | 「405.15」 | 「28682」 | 「855.2」 |
| L1#2_Table#5_Row#37 | 「BLKpoint_190」 | 「0.352」 | 「406.15」 | 「12414」 | 「842.8」 |
| L1#2_Table#5_Row#38 | 「BLKpoint_201」 | 「0.352」 | 「417.15」 | 「26686」 | 「841.8」 |
| L1#2_Table#5_Row#39 | 「BLKpoint_202」 | 「0.502」 | 「287.15」 | 「8823」 | 「884.1」 |
| L1#2_Table#5_Row#40 | 「BLKpoint_219」 | 「0.502」 | 「304.15」 | 「29322」 | 「882.4」 |
| L1#2_Table#5_Row#41 | 「BLKpoint_220」 | 「0.502」 | 「308.15」 | 「6151」 | 「868.1」 |
| L1#2_Table#5_Row#42 | 「BLKpoint_245」 | 「0.502」 | 「333.15」 | 「29426」 | 「865.9」 |
| L1#2_Table#5_Row#43 | 「BLKpoint_246」 | 「0.502」 | 「336.15」 | 「9956」 | 「852.4」 |
| L1#2_Table#5_Row#44 | 「BLKpoint_262」 | 「0.502」 | 「352.15」 | 「28463」 | 「850.8」 |
| L1#2_Table#5_Row#45 | 「BLKpoint_263」 | 「0.502」 | 「355.15」 | 「8187」 | 「834.9」 |
| L1#2_Table#5_Row#46 | 「BLKpoint_282」 | 「0.502」 | 「374.15」 | 「29927」 | 「833.2」 |
| L1#2_Table#5_Row#47 | 「BLKpoint_283」 | 「0.502」 | 「377.15」 | 「5641」 | 「804.7」 |
| L1#2_Table#5_Row#48 | 「BLKpoint_312」 | 「0.502」 | 「406.15」 | 「29592」 | 「802.6」 |
| L1#2_Table#5_Row#49 | 「BLKpoint_313」 | 「0.708」 | 「319.15」 | 「6096」 | 「819.1」 |
| L1#2_Table#5_Row#50 | 「BLKpoint_335」 | 「0.708」 | 「341.15」 | 「29116」 | 「817.2」 |
| L1#2_Table#5_Row#51 | 「BLKpoint_336」 | 「0.708」 | 「343.15」 | 「8107」 | 「807.4」 |
| L1#2_Table#5_Row#52 | 「BLKpoint_356」 | 「0.708」 | 「363.15」 | 「28356」 | 「805.6」 |
| L1#2_Table#5_Row#53 | 「BLKpoint_357」 | 「0.708」 | 「367.15」 | 「10222」 | 「786.2」 |
| L1#2_Table#5_Row#54 | 「BLKpoint_373」 | 「0.708」 | 「383.15」 | 「25781」 | 「784.8」 |
| L1#2_Table#5_Row#55 | 「BLKpoint_374」 | 「0.708」 | 「384.15」 | 「6211」 | 「764.1」 |
| L1#2_Table#5_Row#56 | 「BLKpoint_379」 | 「0.708」 | 「386.15」 | 「28748」 | 「784.6」 |
| L1#2_Table#5_Row#57 | 「BLKpoint_380」 | 「0.708」 | 「387.15」 | 「8903」 | 「763.9」 |
| L1#2_Table#5_Row#58 | 「BLKpoint_401」 | 「0.708」 | 「408.15」 | 「28475」 | 「762.2」 |
```

```ledger
**L1#2_Table#6_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_2825 | doi: 10.1016/j.jct.2007.05.004 | block: PROPblock_10
table_mode: nearest | inspection_id: INSP_10785849f385 | rows_shown: 8

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<water>* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| L1#2_Table#6_Row#1 | 「BLKpoint_14」 | 「298.15」 | 「0」 | 「101.0」 | 「787.2」 |
| L1#2_Table#6_Row#2 | 「BLKpoint_15」 | 「298.15」 | 「0.049」 | 「101.0」 | 「795.47」 |
| L1#2_Table#6_Row#3 | 「BLKpoint_16」 | 「298.15」 | 「0.0993」 | 「101.0」 | 「804.11」 |
| L1#2_Table#6_Row#4 | 「BLKpoint_17」 | 「298.15」 | 「0.1973」 | 「101.0」 | 「821.73」 |
| L1#2_Table#6_Row#5 | 「BLKpoint_18」 | 「298.15」 | 「0.2983」 | 「101.0」 | 「840.79」 |
| L1#2_Table#6_Row#6 | 「BLKpoint_19」 | 「298.15」 | 「0.3985」 | 「101.0」 | 「860.59」 |
| L1#2_Table#6_Row#7 | 「BLKpoint_20」 | 「298.15」 | 「0.5003」 | 「101.0」 | 「881.69」 |
| L1#2_Table#6_Row#8 | 「BLKpoint_21」 | 「298.15」 | 「0.5994」 | 「101.0」 | 「902.96」 |
```

```ledger
**L1#2_Table#7_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_2825 | doi: 10.1016/j.jct.2007.05.004 | block: PROPblock_10
table_mode: rdp | inspection_id: INSP_5d31e929df24 | rows_shown: 12

| *row_id* | *BLKpoint_id* | *temperature_k* | *mole_fraction_<water>* | *pressure_kpa* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| L1#2_Table#7_Row#1 | 「BLKpoint_14」 | 「298.15」 | 「0」 | 「101.0」 | 「787.2」 |
| L1#2_Table#7_Row#2 | 「BLKpoint_15」 | 「298.15」 | 「0.049」 | 「101.0」 | 「795.47」 |
| L1#2_Table#7_Row#3 | 「BLKpoint_16」 | 「298.15」 | 「0.0993」 | 「101.0」 | 「804.11」 |
| L1#2_Table#7_Row#4 | 「BLKpoint_17」 | 「298.15」 | 「0.1973」 | 「101.0」 | 「821.73」 |
| L1#2_Table#7_Row#5 | 「BLKpoint_18」 | 「298.15」 | 「0.2983」 | 「101.0」 | 「840.79」 |
| L1#2_Table#7_Row#6 | 「BLKpoint_19」 | 「298.15」 | 「0.3985」 | 「101.0」 | 「860.59」 |
| L1#2_Table#7_Row#7 | 「BLKpoint_20」 | 「298.15」 | 「0.5003」 | 「101.0」 | 「881.69」 |
| L1#2_Table#7_Row#8 | 「BLKpoint_21」 | 「298.15」 | 「0.5994」 | 「101.0」 | 「902.96」 |
| L1#2_Table#7_Row#9 | 「BLKpoint_23」 | 「298.15」 | 「0.7986」 | 「101.0」 | 「947.17」 |
| L1#2_Table#7_Row#10 | 「BLKpoint_24」 | 「298.15」 | 「0.8999」 | 「101.0」 | 「969.84」 |
| L1#2_Table#7_Row#11 | 「BLKpoint_25」 | 「298.15」 | 「0.9512」 | 「101.0」 | 「982.53」 |
| L1#2_Table#7_Row#12 | 「BLKpoint_26」 | 「298.15」 | 「1」 | 「101.0」 | 「997.05」 |
```
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
I now have all the data I need to compare the two systems. Let me compile the comparison:

**Ethanol + Water (from L1_query_1):**
- 29 data blocks across 22 DOIs
- ~2,920 data points
- Temperature: 268.1–618.2 K
- Pressure: 100–40,000 kPa
- Composition: full range (0–1 ethanol mole fraction)
- At 298.15 K, 100 kPa: 54 composition points in a single block (GLOBlit_220::PROPblock_2, 810 points total)
- Density range at 298.15 K: 995.3 (x=0.003) to 785.7 kg/m³ (x=1.0)

**Methanol + Water (from L1_query_2):**
- ~18 data blocks across ~15 DOIs (search-level summary, UNVERIFIED aggregate)
- ~1,610 data points (search-level summary, UNVERIFIED aggregate)
- Two inspected blocks:
  - GLOBlit_8254::PROPblock_4: 401 points, T=287.15–417.15 K, P=3,721–29,927 kPa, x(MeOH)=0.059–0.708
  - GLOBlit_2825::PROPblock_10: 39 points, T=293.15–303.15 K, P=101 kPa, full composition range
- At 298.15 K, 101 kPa: 12-13 composition points, density 787.2–997.05 kg/m³

The ethanol + water system clearly wins on all metrics: more blocks, more DOIs, more data points, broader temperature range, broader pressure range, and denser composition coverage at room temperature. Both cover the full composition range.

I need to be careful about the UNVERIFIED flags on the methanol+water aggregate statistics. The ethanol+water statistics were verified (PASS validation). For methanol+water, the block-level inspected data is verified but the aggregate counts (18 blocks, 15 DOIs, ~1,610 points) are from search-level summaries.

Let me present a clear comparison answer.
</reasoning>

<answer>
## Ethanol + Water vs. Methanol + Water: Mass Density Data Comparison

For validating a liquid-density model near room temperature, **ethanol + water is the stronger choice** based on the ThermoML database holdings. It offers substantially more data, broader coverage in temperature and pressure, and denser composition grids at near-ambient conditions. Here is a side-by-side comparison:

### Dataset Size and Coverage

| Feature | Ethanol + Water | Methanol + Water |
|---|---|---|
| Data blocks | 29 | ~18 (search-level estimate) |
| Distinct DOIs | 22 | ~15 (search-level estimate) |
| Total data points | ~2,920 | ~1,610 (search-level estimate) |
| Temperature range | 268.1–618.2 K | 287.15–417.15 K (block-verified) |
| Pressure range | 100–40,000 kPa | 101–29,927 kPa (block-verified) |
| Composition range | 0–1 (full) | 0–1 (full) |

### Near Room Temperature (298.15 K, atmospheric pressure)

**Ethanol + water** has **54 composition points** at 298.15 K and 100 kPa in a single block alone (GLOBlit_220, PROPblock_2; DOI 10.1016/j.fluid.2004.11.019), with density spanning from 995.3 kg/m³ at x(ethanol) = 0.003 to 785.7 kg/m³ at x(ethanol) = 1.0.

**Methanol + water** has **13 composition points** at 298.15 K and 101 kPa (GLOBlit_2825, PROPblock_10; DOI 10.1016/j.jct.2007.05.004), with density spanning from 787.2 kg/m³ (pure methanol) to 997.05 kg/m³ (pure water).

Representative density values at 298.15 K for both systems:

| x(alcohol) ≈ | Ethanol + Water ρ (kg/m³) | Methanol + Water ρ (kg/m³) |
|---|---|---|
| 0 (pure water) | 995.3 (at x = 0.003) | 997.05 |
| ~0.1 | 954.9 (x = 0.1296) | 804.11 (at x(water) = 0.0993, i.e. x(MeOH) ≈ 0.90) — *see note* |
| ~0.3 | 904.5 (x = 0.3009) | 840.79 (at x(water) = 0.2983, i.e. x(MeOH) ≈ 0.70) |
| ~0.5 | 859.3 (x = 0.498) | 881.69 (at x(water) = 0.5003, i.e. x(MeOH) ≈ 0.50) |
| 1.0 (pure alcohol) | 785.7 | 787.2 |

*Note: The methanol + water block reports composition as x(water), so x(methanol) = 1 − x(water). Pure methanol densities are very similar (785.7 vs. 787.2 kg/m³), as expected for these two small alcohols.*

### Why Ethanol + Water Is Preferred for Model Validation

1. **~1.8× more data points** (~2,920 vs. ~1,610), providing better statistical power for parameter fitting and residual analysis.

2. **Broader temperature range** (268.1–618.2 K vs. 287.15–417.15 K verified), spanning from sub-ambient to supercritical-like conditions — a 350 K window versus ~130 K.

3. **Broader pressure range** (100–40,000 kPa vs. 101–29,927 kPa verified), reaching 40 MPa.

4. **Much denser composition grid near room temperature**: 54 mole-fraction points at 298.15 K in a single ethanol + water block versus 13 for methanol + water. This dense grid is critical for capturing the non-linear excess volume behavior that challenges density models.

5. **More independent sources** (22 DOIs vs. ~15), allowing cross-validation between laboratories.

### Chemistry Insight

Both systems exhibit the classic alcohol–water density behavior: a monotonic decrease from the high density of pure water (~997 kg/m³) to the lower density of the pure alcohol (~786–787 kg/m³). The non-linearity is most pronounced in the water-rich region, where even small additions of alcohol strongly disrupt water's hydrogen-bonding network, producing significant excess volumes. Ethanol, being larger and more hydrophobic than methanol, tends to produce larger excess volume effects, making the ethanol + water system a more demanding (and therefore more informative) test case for liquid density models.

### Recommendation

Use **ethanol + water** as your primary validation system. Its larger dataset, broader state-space coverage, denser composition grids, and more numerous independent sources make it the superior benchmark. The methanol + water system can serve as a useful secondary validation set, particularly at atmospheric pressure and near-ambient temperatures.
</answer>