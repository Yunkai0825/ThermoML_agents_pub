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
| comp | GLOBcomp_12 | hexane | hexane |
| comp | GLOBcomp_2 | ethanol | ethanol |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Find all measured mixture properties for benzene + toluene binary near room temperature (~288-308 K). Report: (1) list o → stored as L1_query_1 · validation: PASS
- [L1] Find all measured mixture properties for binary hexane + ethanol near room temperature (288–308 K). Report: (1) list of  → stored as L1_query_2 · validation: FLAGGED(1)

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** A search of the ThermoML database for binary benzene + toluene data in the 288–308 K range returned 2 data blocks covering 2 distinct liquid-phase property types across 4 total data points. The properties are excess molar enthalpy (GLOBprop_17, from GLOBlit_6057, DOI 10.1016/j.tca.2013.01.028) and molar enthalpy of solution (GLOBprop_15, from GLOBlit_6268, DOI 10.1016/j.tca.2015.09.022). Excess molar enthalpy was measured at 303.15 K and 101.0 kPa over toluene mole fractions 0.247–0.7685 (3 points), yielding small positive values of 0.0543, 0.0713, and 0.0477 kJ/mol at x(toluene) = 0.247, 0.4944, and 0.7685 respectively, with a maximum near equimolar composition consistent with nearly ideal mixing. Molar enthalpy of solution was measured at 298.15 K and 100 kPa at infinite dilution (x(toluene) = 0), giving 0.28 kJ/mol, reflecting weak endothermic mixing of these structurally similar aromatic hydrocarbons.

**Answer:**

#### Binary Mixture Properties for Benzene + Toluene Near Room Temperature (288–308 K)

##### Overview

A search of the ThermoML database for binary (benzene + toluene) data blocks with temperatures in the 288–308 K range returned **2 data blocks** covering **2 distinct property types**, all in the **liquid phase**.

---

##### 1. Distinct Property Types

**WM_L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *GLOBprop ID* | *Property Name* | *Measurement Method* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「GLOBprop_17」 | 「Excess molar enthalpy (enthalpy of mixing), kJ/mol」 | 「Calvet calorimetry」 |
| WM_L1#1_Table#1_Row#2 | 「GLOBprop_15」 | 「Molar enthalpy of solution, kJ/mol」 | 「Titration calorimetry」 |

---

##### 2. Composition (Mole Fraction of Toluene) Range Covered

- **GLOBprop_17** (excess molar enthalpy, GLOBlit_6057 :: PROPblock_1): 0.247 – 0.7685 (3 data points spanning the mid-composition range)
- **GLOBprop_15** (molar enthalpy of solution, GLOBlit_6268 :: PROPblock_7): 0 (infinite dilution, 1 data point; toluene dissolved in benzene solvent)

---

##### 3. Number of Data Blocks and Data Points

- **Total data blocks:** 2
- **Total data points:** 4 (3 + 1)

---

##### 4. Literature References

**WM_L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *GLOBlit ID* | *DOI* | *Block(s)* |
|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「GLOBlit_6057」 | 「10.1016/j.tca.2013.01.028」 | 「PROPblock_1 (excess molar enthalpy)」 |
| WM_L1#1_Table#2_Row#2 | 「GLOBlit_6268」 | 「10.1016/j.tca.2015.09.022」 | 「PROPblock_7 (molar enthalpy of solution)」 |

---

##### 5. Representative Data

###### GLOBlit_6057 :: PROPblock_1 — Excess Molar Enthalpy

This block reports excess molar enthalpy at constrained T = 303.15 K and P = 101.0 kPa:

**WM_L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *x(toluene)* | *Excess Molar Enthalpy (kJ/mol)* |
|---|---|---|
| WM_L1#1_Table#3_Row#1 | 「0.247」 | 「0.0543」 |
| WM_L1#1_Table#3_Row#2 | 「0.4944」 | 「0.0713」 |
| WM_L1#1_Table#3_Row#3 | 「0.7685」 | 「0.0477」 |

The excess molar enthalpy values are very small and positive (0.0477–0.0713 kJ/mol), consistent with the nearly ideal mixing behavior expected for benzene + toluene — two structurally similar aromatic hydrocarbons with comparable intermolecular interactions. The non-monotonic profile with a maximum near equimolar composition (x ≈ 0.49) is characteristic of symmetric excess enthalpy curves.

###### GLOBlit_6268 :: PROPblock_7 — Molar Enthalpy of Solution

This block reports molar enthalpy of solution at T = 298.15 K and P = 100 kPa:

**WM_L1#1_Table#4_(Query_L1#1_Answer):**

| *row_id* | *x(toluene)* | *Molar Enthalpy of Solution (kJ/mol)* |
|---|---|---|
| WM_L1#1_Table#4_Row#1 | 「0」 | 「0.28」 |

The molar enthalpy of solution for toluene at infinite dilution in benzene is 0.28 kJ/mol, again reflecting the weak endothermic character of mixing these two similar aromatics.

**Core claims:**
- A ThermoML search for binary benzene + toluene data in the 288–308 K range returned 2 data blocks covering 2 liquid-phase property types: excess molar enthalpy (kJ/mol) and molar enthalpy of solution (kJ/mol), with a total of 4 data points.
- Excess molar enthalpy at 303.15 K and 101.0 kPa spans toluene mole fractions 0.247–0.7685, with small positive values (0.0543, 0.0713, and 0.0477 kJ/mol), exhibiting a maximum near equimolar composition consistent with nearly ideal mixing of two structurally similar aromatic hydrocarbons.
- The molar enthalpy of solution for toluene at infinite dilution in benzene at 298.15 K and 100 kPa is 0.28 kJ/mol, reflecting weak endothermic mixing character.
- The two data blocks originate from two literature sources with DOIs 10.1016/j.tca.2013.01.028 and 10.1016/j.tca.2015.09.022.

**Core blocks found:**

**WM_L1#1_Blocks_(Query_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#5 | 「GLOBlit_6057」 | 「PROPblock_1」 | 「GLOBcomp_14, GLOBcomp_8」 | 「GLOBprop_17」 | 「Excess molar enthalpy (enthalpy of mixing) for benzene + toluene at 303.15 K, mole fraction of toluene 0.247–0.7685.」 |
| WM_L1#1_Table#6 | 「GLOBlit_6268」 | 「PROPblock_7」 | 「GLOBcomp_14, GLOBcomp_8」 | 「GLOBprop_15」 | 「Molar enthalpy of solution for toluene at infinite dilution in benzene at 298.15 K.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: success · validation: FLAGGED(1)

**Summary:** The hexane (GLOBcomp_12) + ethanol (GLOBcomp_2) binary system in the ThermoML database near room temperature (288–308 K) spans 9 data blocks, 8 distinct property types, and 5 literature sources. The 8 property types are: excess molar enthalpy (GLOBprop_17), excess molar volume (GLOBprop_28), refractive index (GLOBprop_7), speed of sound (GLOBprop_8), mass density (GLOBprop_1), binary diffusion coefficient (GLOBprop_29), surface tension (GLOBprop_13), and viscosity (GLOBprop_4). Composition coverage for most properties extends across the full mole-fraction range of ethanol (0–1). Three blocks were inspected in detail: excess molar enthalpy (GLOBlit_294::PROPblock_5, 17 data points at 298.15 K, x(ethanol) 0.0544–0.9528, positive values peaking at approximately 0.5795 kJ/mol near x(ethanol) ≈ 0.36); excess molar volume (GLOBlit_294::PROPblock_6, 23 data points at 298.15 K, x(ethanol) 0.0417–0.9497, positive values with a maximum of 4.12×10⁻⁷ m³/mol near x(ethanol) ≈ 0.45); and binary diffusion coefficient (GLOBlit_8445::PROPblock_8, 9 data points at 298.15 K, ranging from 5.74×10⁻⁹ m²/s at x(ethanol) = 0 to a minimum of 1.3×10⁻⁹ m²/s at x(ethanol) = 0.5–0.7). The five literature sources are GLOBlit_294 (DOI 10.1016/j.fluid.2005.08.001), GLOBlit_2800 (DOI 10.1016/j.jct.2007.02.008), GLOBlit_8445 (DOI 10.1021/je0497303), GLOBlit_10821 (DOI 10.1021/je700215z), and GLOBlit_11449 (DOI 10.1021/je800925v). Compared with the benzene + toluene binary (2 blocks, 2 property types), hexane + ethanol is a far richer model-testing system, covering thermodynamic, transport, acoustic, optical, volumetric, and interfacial properties. Six blocks were not individually inspected, so their exact data-point counts remain unverified.

**Answer:**

### Binary Hexane + Ethanol Mixture Properties Near Room Temperature (288–308 K)

#### Overview

The ThermoML database contains **9 data blocks** for the binary system hexane (GLOBcomp_12) + ethanol (GLOBcomp_2) with temperature values or constraints in the 288–308 K range. These blocks span **8 distinct property types** across **5 literature sources**, offering substantially more property diversity than the benzene + toluene binary (which had only 2 blocks, 2 property types, and 4 data points in the same temperature window).

---

#### (1) Distinct Property Types with GLOBprop IDs

**WM_L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *#* | *Property* | *GLOBprop ID* |
|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「1」 | 「Excess molar enthalpy (molar enthalpy of mixing)」 | 「GLOBprop_17」 |
| WM_L1#2_Table#1_Row#2 | 「2」 | 「Excess molar volume」 | 「GLOBprop_28」 |
| WM_L1#2_Table#1_Row#3 | 「3」 | 「Refractive index (Na D-line)」 | 「GLOBprop_7」 |
| WM_L1#2_Table#1_Row#4 | 「4」 | 「Speed of sound」 | 「GLOBprop_8」 |
| WM_L1#2_Table#1_Row#5 | 「5」 | 「Mass density」 | 「GLOBprop_1」 |
| WM_L1#2_Table#1_Row#6 | 「6」 | 「Binary diffusion coefficient」 | 「GLOBprop_29」 |
| WM_L1#2_Table#1_Row#7 | 「7」 | 「Surface tension (liquid–gas)」 | 「GLOBprop_13」 |
| WM_L1#2_Table#1_Row#8 | 「8」 | 「Viscosity」 | 「GLOBprop_4」 |

**Total distinct property types: 8**

---

#### (2) Composition Range Covered for Each Property

**WM_L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *Property* | *Block(s)* | *x(ethanol) range* | *Source of range* |
|---|---|---|---|---|
| WM_L1#2_Table#2_Row#1 | 「Excess molar enthalpy」 | 「GLOBlit_294::PROPblock_5」 | 「0.0544–0.9528」 | 「Inspected (n=17)」 |
| WM_L1#2_Table#2_Row#2 | 「Excess molar volume」 | 「GLOBlit_294::PROPblock_6」 | 「0.0417–0.9497」 | 「Inspected (n=23)」 |
| WM_L1#2_Table#2_Row#3 | 「Refractive index」 | 「GLOBlit_2800::PROPblock_22」 | 「0–1 (full range incl. pure components)」 | 「From search_blocks summary」 |
| WM_L1#2_Table#2_Row#4 | 「Speed of sound」 | 「GLOBlit_2800::PROPblock_23」 | 「0–1 (full range incl. pure components)」 | 「From search_blocks summary」 |
| WM_L1#2_Table#2_Row#5 | 「Mass density」 | 「GLOBlit_2800::PROPblock_24 + GLOBlit_11449::PROPblock_10」 | 「0–1 (PROPblock_24, from search summary); not inspected for PROPblock_10 in this run」 | 「From search_blocks summary」 |
| WM_L1#2_Table#2_Row#6 | 「Binary diffusion coefficient」 | 「GLOBlit_8445::PROPblock_8」 | 「0–1 (full range incl. pure components)」 | 「Inspected (n=9)」 |
| WM_L1#2_Table#2_Row#7 | 「Surface tension」 | 「GLOBlit_10821::PROPblock_5」 | 「Not inspected in this run; search summary reported range from tool result」 | 「From search_blocks summary」 |
| WM_L1#2_Table#2_Row#8 | 「Viscosity」 | 「GLOBlit_11449::PROPblock_9」 | 「Not inspected in this run; search summary reported ethanol-rich limit」 | 「From search_blocks summary」 |

---

#### (3) Number of Data Blocks and Data Points

**WM_L1#2_Table#3_(Query_L1#2_Answer):**

| *row_id* | *Block* | *GLOBlit* | *Property* | *Data points (total in block)* |
|---|---|---|---|---|
| WM_L1#2_Table#3_Row#1 | 「PROPblock_5」 | 「GLOBlit_294」 | 「Excess molar enthalpy」 | 「17」 |
| WM_L1#2_Table#3_Row#2 | 「PROPblock_6」 | 「GLOBlit_294」 | 「Excess molar volume」 | 「23」 |
| WM_L1#2_Table#3_Row#3 | 「PROPblock_22」 | 「GLOBlit_2800」 | 「Refractive index」 | 「Not inspected; search summary reported the block」 |
| WM_L1#2_Table#3_Row#4 | 「PROPblock_23」 | 「GLOBlit_2800」 | 「Speed of sound」 | 「Not inspected; search summary reported the block」 |
| WM_L1#2_Table#3_Row#5 | 「PROPblock_24」 | 「GLOBlit_2800」 | 「Mass density」 | 「Not inspected; search summary reported the block」 |
| WM_L1#2_Table#3_Row#6 | 「PROPblock_8」 | 「GLOBlit_8445」 | 「Binary diffusion coefficient」 | 「9」 |
| WM_L1#2_Table#3_Row#7 | 「PROPblock_5」 | 「GLOBlit_10821」 | 「Surface tension」 | 「Not inspected; search summary reported the block」 |
| WM_L1#2_Table#3_Row#8 | 「PROPblock_9」 | 「GLOBlit_11449」 | 「Viscosity」 | 「Not inspected; search summary reported the block」 |
| WM_L1#2_Table#3_Row#9 | 「PROPblock_10」 | 「GLOBlit_11449」 | 「Mass density」 | 「Not inspected; search summary reported the block」 |

- **Total blocks: 9**
- **Total data points across inspected blocks: 49** (17 + 23 + 9). The remaining 6 blocks were not inspected in this run, so their exact point counts cannot be confirmed here. The search summaries indicated substantial additional data.

---

#### (4) Literature References

**WM_L1#2_Table#4_(Query_L1#2_Answer):**

| *row_id* | *#* | *GLOBlit ID* | *DOI* | *Blocks* | *Properties* |
|---|---|---|---|---|---|
| WM_L1#2_Table#4_Row#1 | 「1」 | 「GLOBlit_294」 | 「10.1016/j.fluid.2005.08.001」 | 「PROPblock_5, PROPblock_6」 | 「Excess molar enthalpy, Excess molar volume」 |
| WM_L1#2_Table#4_Row#2 | 「2」 | 「GLOBlit_2800」 | 「10.1016/j.jct.2007.02.008」 | 「PROPblock_22, PROPblock_23, PROPblock_24」 | 「Refractive index, Speed of sound, Mass density」 |
| WM_L1#2_Table#4_Row#3 | 「3」 | 「GLOBlit_8445」 | 「10.1021/je0497303」 | 「PROPblock_8」 | 「Binary diffusion coefficient」 |
| WM_L1#2_Table#4_Row#4 | 「4」 | 「GLOBlit_10821」 | 「10.1021/je700215z」 | 「PROPblock_5」 | 「Surface tension (liquid–gas)」 |
| WM_L1#2_Table#4_Row#5 | 「5」 | 「GLOBlit_11449」 | 「10.1021/je800925v」 | 「PROPblock_9, PROPblock_10」 | 「Viscosity, Mass density」 |

---

#### Representative Inspected Data

**Excess molar enthalpy** (GLOBlit_294::PROPblock_5, T = 298.15 K, P = 101.325 kPa):
The enthalpy of mixing is positive across the full composition range, peaking at approximately 0.5795 kJ/mol near x(ethanol) ≈ 0.36, consistent with the endothermic disruption of hydrogen-bonding networks in ethanol by the nonpolar hexane.

**Excess molar volume** (GLOBlit_294::PROPblock_6, T = 298.15 K, P = 101.325 kPa):
Positive excess volumes across the full range, with a maximum of 4.12×10⁻⁷ m³/mol near x(ethanol) ≈ 0.45, indicating volume expansion on mixing — typical for systems with strong unlike-molecule repulsion and poor packing.

**Binary diffusion coefficient** (GLOBlit_8445::PROPblock_8, T = 298.15 K, P = 101.3 kPa):
Diffusion coefficients decrease sharply from 5.74×10⁻⁹ m²/s at x(ethanol) = 0 to a minimum of 1.3×10⁻⁹ m²/s at x(ethanol) = 0.5–0.7, reflecting the increased viscosity and hydrogen-bonding interactions in the ethanol-rich regime.

---

#### Comparison with Benzene + Toluene

**WM_L1#2_Table#5_(Query_L1#2_Answer):**

| *row_id* | *Metric* | *Hexane + Ethanol* | *Benzene + Toluene* |
|---|---|---|---|
| WM_L1#2_Table#5_Row#1 | 「Distinct property types」 | 「8」 | 「2」 |
| WM_L1#2_Table#5_Row#2 | 「Total data blocks」 | 「9」 | 「2」 |
| WM_L1#2_Table#5_Row#3 | 「Literature sources」 | 「5」 | 「(from prior context)」 |
| WM_L1#2_Table#5_Row#4 | 「Composition coverage」 | 「Near-full (0–1) for most properties」 | 「Limited」 |

Hexane + ethanol is clearly a far richer model-testing binary in the ThermoML database near room temperature, offering diverse thermodynamic (excess enthalpy, excess volume), transport (diffusion, viscosity), acoustic (speed of sound), optical (refractive index), volumetric (density), and interfacial (surface tension) data across wide composition ranges.

**Core claims:**
- The ThermoML database contains 9 data blocks for the hexane + ethanol binary system in the 288–308 K temperature range, spanning 8 distinct property types (excess molar enthalpy, excess molar volume, refractive index, speed of sound, mass density, binary diffusion coefficient, surface tension, and viscosity) from 5 literature sources.
- Most properties cover a near-full ethanol mole fraction range (0–1), with inspected blocks confirming coverage of x(ethanol) from 0.0544–0.9528 for excess molar enthalpy, 0.0417–0.9497 for excess molar volume, and 0–1 for binary diffusion coefficient.
- Excess molar enthalpy at 298.15 K and 101.325 kPa is positive across the full composition range, peaking at approximately 0.5795 kJ/mol near x(ethanol) ≈ 0.36, consistent with endothermic disruption of ethanol hydrogen-bonding networks by nonpolar hexane.
- Excess molar volume at 298.15 K and 101.325 kPa is positive across the full range, with a maximum of 4.12×10⁻⁷ m³/mol near x(ethanol) ≈ 0.45, indicating volume expansion on mixing.
- Binary diffusion coefficients at 298.15 K and 101.3 kPa decrease from 5.74×10⁻⁹ m²/s at x(ethanol) = 0 to a minimum of 1.3×10⁻⁹ m²/s at x(ethanol) = 0.5–0.7.
- Hexane + ethanol offers substantially greater property diversity in ThermoML near room temperature than benzene + toluene, which had only 2 data blocks and 2 property types in the same temperature window.
- Six of the nine blocks were not individually inspected in this run, so their exact data-point counts and composition ranges remain unverified.

**Core blocks found:**

**WM_L1#2_Blocks_(Query_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#6 | 「GLOBlit_294」 | 「PROPblock_5」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_17」 | 「Excess molar enthalpy for hexane + ethanol at 298.15 K; x(ethanol) 0.0544–0.9528; 17 data points.」 |
| WM_L1#2_Table#7 | 「GLOBlit_294」 | 「PROPblock_6」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_28」 | 「Excess molar volume for hexane + ethanol at 298.15 K; x(ethanol) 0.0417–0.9497; 23 data points.」 |
| WM_L1#2_Table#8 | 「GLOBlit_2800」 | 「PROPblock_22」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_7」 | 「Refractive index (Na D-line) for hexane + ethanol; x(ethanol) 0–1.」 |
| WM_L1#2_Table#9 | 「GLOBlit_2800」 | 「PROPblock_23」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_8」 | 「Speed of sound for hexane + ethanol; x(ethanol) 0–1.」 |
| WM_L1#2_Table#10 | 「GLOBlit_2800」 | 「PROPblock_24」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_1」 | 「Mass density for hexane + ethanol; x(ethanol) 0–1.」 |
| WM_L1#2_Table#11 | 「GLOBlit_8445」 | 「PROPblock_8」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_29」 | 「Binary diffusion coefficient for hexane + ethanol at 298.15 K; x(ethanol) 0–1; 9 data points.」 |
| WM_L1#2_Table#12 | 「GLOBlit_10821」 | 「PROPblock_5」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_13」 | 「Surface tension (liquid–gas) for hexane + ethanol.」 |
| WM_L1#2_Table#13 | 「GLOBlit_11449」 | 「PROPblock_9」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_4」 | 「Viscosity for hexane + ethanol.」 |
| WM_L1#2_Table#14 | 「GLOBlit_11449」 | 「PROPblock_10」 | 「GLOBcomp_2, GLOBcomp_12」 | 「GLOBprop_1」 | 「Mass density for hexane + ethanol.」 |

*Not stored here: 3 verbatim data_inspections table(s); 2 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(1) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNINSPECTED_BLOCK** PROPblock_10: PROPblock_10 is quoted with data values (49, 17, 23, …) but was never inspected in this run



</memory>

## User
I need a binary liquid for testing a mixture-property model near room temperature. Between benzene + toluene and hexane + ethanol, which would let me test the model over a wider composition range and against more types of measured properties?

## Assistant
<summary>Planning two parallel L1 queries to compare benzene+toluene and hexane+ethanol binary mixtures near room temperature for composition coverage and property diversity.</summary>
<tool_call>L1_query(instruction=Search for binary…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** A search of the ThermoML database for binary benzene + toluene data in the 288–308 K range returned 2 data blocks covering 2 distinct liquid-phase property types across 4 total data points. The properties are excess molar enthalpy (GLOBprop_17, from GLOBlit_6057, DOI 10.1016/j.tca.2013.01.028) and molar enthalpy of solution (GLOBprop_15, from GLOBlit_6268, DOI 10.1016/j.tca.2015.09.022). Excess molar enthalpy was measured at 303.15 K and 101.0 kPa over toluene mole fractions 0.247–0.7685 (3 points), yielding small positive values of 0.0543, 0.0713, and 0.0477 kJ/mol at x(toluene) = 0.247, 0.4944, and 0.7685 respectively, with a maximum near equimolar composition consistent with nearly ideal mixing. Molar enthalpy of solution was measured at 298.15 K and 100 kPa at infinite dilution (x(toluene) = 0), giving 0.28 kJ/mol, reflecting weak endothermic mixing of these structurally similar aromatic hydrocarbons.

**Answer:**

#### Binary Mixture Properties for Benzene + Toluene Near Room Temperature (288–308 K)

##### Overview

A search of the ThermoML database for binary (benzene + toluene) data blocks with temperatures in the 288–308 K range returned **2 data blocks** covering **2 distinct property types**, all in the **liquid phase**.

---

##### 1. Distinct Property Types

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *GLOBprop ID* | *Property Name* | *Measurement Method* |
|---|---|---|---|
| L1#1_Table#1_Row#1 | 「GLOBprop_17」 | 「Excess molar enthalpy (enthalpy of mixing), kJ/mol」 | 「Calvet calorimetry」 |
| L1#1_Table#1_Row#2 | 「GLOBprop_15」 | 「Molar enthalpy of solution, kJ/mol」 | 「Titration calorimetry」 |

---

##### 2. Composition (Mole Fraction of Toluene) Range Covered

- **GLOBprop_17** (excess molar enthalpy, GLOBlit_6057 :: PROPblock_1): 0.247 – 0.7685 (3 data points spanning the mid-composition range)
- **GLOBprop_15** (molar enthalpy of solution, GLOBlit_6268 :: PROPblock_7): 0 (infinite dilution, 1 data point; toluene dissolved in benzene solvent)

---

##### 3. Number of Data Blocks and Data Points

- **Total data blocks:** 2
- **Total data points:** 4 (3 + 1)

---

##### 4. Literature References

**L1#1_Table#2_(Query_L1#1_Answer):**

| *row_id* | *GLOBlit ID* | *DOI* | *Block(s)* |
|---|---|---|---|
| L1#1_Table#2_Row#1 | 「GLOBlit_6057」 | 「10.1016/j.tca.2013.01.028」 | 「PROPblock_1 (excess molar enthalpy)」 |
| L1#1_Table#2_Row#2 | 「GLOBlit_6268」 | 「10.1016/j.tca.2015.09.022」 | 「PROPblock_7 (molar enthalpy of solution)」 |

---

##### 5. Representative Data

###### GLOBlit_6057 :: PROPblock_1 — Excess Molar Enthalpy

This block reports excess molar enthalpy at constrained T = 303.15 K and P = 101.0 kPa:

**L1#1_Table#3_(Query_L1#1_Answer):**

| *row_id* | *x(toluene)* | *Excess Molar Enthalpy (kJ/mol)* |
|---|---|---|
| L1#1_Table#3_Row#1 | 「0.247」 | 「0.0543」 |
| L1#1_Table#3_Row#2 | 「0.4944」 | 「0.0713」 |
| L1#1_Table#3_Row#3 | 「0.7685」 | 「0.0477」 |

The excess molar enthalpy values are very small and positive (0.0477–0.0713 kJ/mol), consistent with the nearly ideal mixing behavior expected for benzene + toluene — two structurally similar aromatic hydrocarbons with comparable intermolecular interactions. The non-monotonic profile with a maximum near equimolar composition (x ≈ 0.49) is characteristic of symmetric excess enthalpy curves.

###### GLOBlit_6268 :: PROPblock_7 — Molar Enthalpy of Solution

This block reports molar enthalpy of solution at T = 298.15 K and P = 100 kPa:

**L1#1_Table#4_(Query_L1#1_Answer):**

| *row_id* | *x(toluene)* | *Molar Enthalpy of Solution (kJ/mol)* |
|---|---|---|
| L1#1_Table#4_Row#1 | 「0」 | 「0.28」 |

The molar enthalpy of solution for toluene at infinite dilution in benzene is 0.28 kJ/mol, again reflecting the weak endothermic character of mixing these two similar aromatics.

**Core claims:**
- A ThermoML search for binary benzene + toluene data in the 288–308 K range returned 2 data blocks covering 2 liquid-phase property types: excess molar enthalpy (kJ/mol) and molar enthalpy of solution (kJ/mol), with a total of 4 data points.
- Excess molar enthalpy at 303.15 K and 101.0 kPa spans toluene mole fractions 0.247–0.7685, with small positive values (0.0543, 0.0713, and 0.0477 kJ/mol), exhibiting a maximum near equimolar composition consistent with nearly ideal mixing of two structurally similar aromatic hydrocarbons.
- The molar enthalpy of solution for toluene at infinite dilution in benzene at 298.15 K and 100 kPa is 0.28 kJ/mol, reflecting weak endothermic mixing character.
- The two data blocks originate from two literature sources with DOIs 10.1016/j.tca.2013.01.028 and 10.1016/j.tca.2015.09.022.

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#5_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_6057 | lit_id: 2013-did-ait-0 | doi: 10.1016/j.tca.2013.01.028
block: PROPblock_1 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 3
compounds: benzene (C6H6; GLOBcomp_14; DOIcomp_2; InChIKey UHOVQNZJYSORNB-UHFFFAOYSA-N); toluene (C7H8; GLOBcomp_8; DOIcomp_3; InChIKey YXFVVABEGXRONW-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_17
description: Excess molar enthalpy (enthalpy of mixing) for benzene + toluene at 303.15 K, mole fraction of toluene 0.247–0.7685.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#5_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_2」 | 「Temperature, K」 | 「value=303.15 · phase=Liquid」 |
| L1#1_Table#5_Row#2 | 「constraint」 | 「BLKconstr_2/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#5_Row#3 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of toluene」 | 「range=0.247–0.7685 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#5_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_17」 | 「Excess molar enthalpy (molar enthalpy of mixing), kJ/mol」 | 「method=Calvet calorimetry (GLOBmeas_13) · range=0.0477–0.0713 · mean=0.057767 · n=3 · phase=Liquid」 |
```

```ledger
**L1#1_Table#6_(Query_L1#1_CoreBLK):**
lit_num_id: GLOBlit_6268 | lit_id: 2015-sol-var-1 | doi: 10.1016/j.tca.2015.09.022
block: PROPblock_7 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 1
compounds: benzene (C6H6; GLOBcomp_14; DOIcomp_9; InChIKey UHOVQNZJYSORNB-UHFFFAOYSA-N); toluene (C7H8; GLOBcomp_8; DOIcomp_8; InChIKey YXFVVABEGXRONW-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_15
description: Molar enthalpy of solution for toluene at infinite dilution in benzene at 298.15 K.
solvents: [{'component_org_num': 'DOIcomp_9', 'comp_num_id': 'GLOBcomp_14', 'solvent_num_id': 'GLOBsolvent_13', 'inchi_key': 'UHOVQNZJYSORNB-UHFFFAOYSA-N'}]

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#6_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of toluene」 | 「range=0.0–0.0 · n_unique=1 · phase=Liquid」 |
| L1#1_Table#6_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_3」 | 「Pressure, kPa」 | 「range=100.0–100.0 · n_unique=1 · phase=Liquid」 |
| L1#1_Table#6_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–298.15 · n_unique=1 · phase=Liquid」 |
| L1#1_Table#6_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_15」 | 「Molar enthalpy of solution, kJ/mol」 | 「method=Titration calorimetry (GLOBmeas_25) · range=0.28–0.28 · mean=0.28 · n=1 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#7_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_6057 | doi: 10.1016/j.tca.2013.01.028 | block: PROPblock_1
table_mode: complete | inspection_id: INSP_131b9ce737e2 | rows_shown: 3

| *row_id* | *BLKpoint_id* | *mole_fraction_<toluene>* | *temperature_k* | *pressure_kpa* | *excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol* |
|---|---|---|---|---|---|
| L1#1_Table#7_Row#1 | 「BLKpoint_1」 | 「0.247」 | 「303.15」 | 「101.0」 | 「0.0543」 |
| L1#1_Table#7_Row#2 | 「BLKpoint_2」 | 「0.4944」 | 「303.15」 | 「101.0」 | 「0.0713」 |
| L1#1_Table#7_Row#3 | 「BLKpoint_3」 | 「0.7685」 | 「303.15」 | 「101.0」 | 「0.0477」 |
```

```ledger
**L1#1_Table#8_(Query_L1#1_INSP):**
lit_num_id: GLOBlit_6268 | doi: 10.1016/j.tca.2015.09.022 | block: PROPblock_7
table_mode: complete | inspection_id: INSP_b980ad0378b4 | rows_shown: 1

| *row_id* | *BLKpoint_id* | *mole_fraction_<toluene>* | *pressure_kpa* | *temperature_k* | *molar_enthalpy_of_solution_kj_mol* |
|---|---|---|---|---|---|
| L1#1_Table#8_Row#1 | 「BLKpoint_1」 | 「0」 | 「100」 | 「298.15」 | 「0.28」 |
```
</subagent_answer>
</tool_result>

## Assistant
<summary>Benzene+toluene data confirmed: 2 blocks, 2 property types, 4 points, composition 0–0.7685. Now dispatching L1 query for hexane+ethanol binary near room temperature to compare.</summary>
<tool_call>L1_query(instruction=Search the Thermo…, id_catalog=, context=This is for compa…)</tool_call>

## User
<tool_result>
[TOOL_RESULT_SIZE_WARNING: L1_query returned 24,633 characters after result processing; the target is 24,000. The full result follows — prefer narrower requests, and rely on your working memory for recall instead of re-running this call.]

<subagent_answer>
### L1#2 — L1_query return

**Status:** status=success

**Summary:** The hexane (GLOBcomp_12) + ethanol (GLOBcomp_2) binary system in the ThermoML database near room temperature (288–308 K) spans 9 data blocks, 8 distinct property types, and 5 literature sources. The 8 property types are: excess molar enthalpy (GLOBprop_17), excess molar volume (GLOBprop_28), refractive index (GLOBprop_7), speed of sound (GLOBprop_8), mass density (GLOBprop_1), binary diffusion coefficient (GLOBprop_29), surface tension (GLOBprop_13), and viscosity (GLOBprop_4). Composition coverage for most properties extends across the full mole-fraction range of ethanol (0–1). Three blocks were inspected in detail: excess molar enthalpy (GLOBlit_294::PROPblock_5, 17 data points at 298.15 K, x(ethanol) 0.0544–0.9528, positive values peaking at approximately 0.5795 kJ/mol near x(ethanol) ≈ 0.36); excess molar volume (GLOBlit_294::PROPblock_6, 23 data points at 298.15 K, x(ethanol) 0.0417–0.9497, positive values with a maximum of 4.12×10⁻⁷ m³/mol near x(ethanol) ≈ 0.45); and binary diffusion coefficient (GLOBlit_8445::PROPblock_8, 9 data points at 298.15 K, ranging from 5.74×10⁻⁹ m²/s at x(ethanol) = 0 to a minimum of 1.3×10⁻⁹ m²/s at x(ethanol) = 0.5–0.7). The five literature sources are GLOBlit_294 (DOI 10.1016/j.fluid.2005.08.001), GLOBlit_2800 (DOI 10.1016/j.jct.2007.02.008), GLOBlit_8445 (DOI 10.1021/je0497303), GLOBlit_10821 (DOI 10.1021/je700215z), and GLOBlit_11449 (DOI 10.1021/je800925v). Compared with the benzene + toluene binary (2 blocks, 2 property types), hexane + ethanol is a far richer model-testing system, covering thermodynamic, transport, acoustic, optical, volumetric, and interfacial properties. Six blocks were not individually inspected, so their exact data-point counts remain unverified.

**Answer:**

### Binary Hexane + Ethanol Mixture Properties Near Room Temperature (288–308 K)

#### Overview

The ThermoML database contains **9 data blocks** for the binary system hexane (GLOBcomp_12) + ethanol (GLOBcomp_2) with temperature values or constraints in the 288–308 K range. These blocks span **8 distinct property types** across **5 literature sources**, offering substantially more property diversity than the benzene + toluene binary (which had only 2 blocks, 2 property types, and 4 data points in the same temperature window).

---

#### (1) Distinct Property Types with GLOBprop IDs

**L1#2_Table#1_(Query_L1#2_Answer):**

| *row_id* | *#* | *Property* | *GLOBprop ID* |
|---|---|---|---|
| L1#2_Table#1_Row#1 | 「1」 | 「Excess molar enthalpy (molar enthalpy of mixing)」 | 「GLOBprop_17」 |
| L1#2_Table#1_Row#2 | 「2」 | 「Excess molar volume」 | 「GLOBprop_28」 |
| L1#2_Table#1_Row#3 | 「3」 | 「Refractive index (Na D-line)」 | 「GLOBprop_7」 |
| L1#2_Table#1_Row#4 | 「4」 | 「Speed of sound」 | 「GLOBprop_8」 |
| L1#2_Table#1_Row#5 | 「5」 | 「Mass density」 | 「GLOBprop_1」 |
| L1#2_Table#1_Row#6 | 「6」 | 「Binary diffusion coefficient」 | 「GLOBprop_29」 |
| L1#2_Table#1_Row#7 | 「7」 | 「Surface tension (liquid–gas)」 | 「GLOBprop_13」 |
| L1#2_Table#1_Row#8 | 「8」 | 「Viscosity」 | 「GLOBprop_4」 |

**Total distinct property types: 8**

---

#### (2) Composition Range Covered for Each Property

**L1#2_Table#2_(Query_L1#2_Answer):**

| *row_id* | *Property* | *Block(s)* | *x(ethanol) range* | *Source of range* |
|---|---|---|---|---|
| L1#2_Table#2_Row#1 | 「Excess molar enthalpy」 | 「GLOBlit_294::PROPblock_5」 | 「0.0544–0.9528」 | 「Inspected (n=17)」 |
| L1#2_Table#2_Row#2 | 「Excess molar volume」 | 「GLOBlit_294::PROPblock_6」 | 「0.0417–0.9497」 | 「Inspected (n=23)」 |
| L1#2_Table#2_Row#3 | 「Refractive index」 | 「GLOBlit_2800::PROPblock_22」 | 「0–1 (full range incl. pure components)」 | 「From search_blocks summary」 |
| L1#2_Table#2_Row#4 | 「Speed of sound」 | 「GLOBlit_2800::PROPblock_23」 | 「0–1 (full range incl. pure components)」 | 「From search_blocks summary」 |
| L1#2_Table#2_Row#5 | 「Mass density」 | 「GLOBlit_2800::PROPblock_24 + GLOBlit_11449::PROPblock_10」 | 「0–1 (PROPblock_24, from search summary); not inspected for PROPblock_10 in this run」 | 「From search_blocks summary」 |
| L1#2_Table#2_Row#6 | 「Binary diffusion coefficient」 | 「GLOBlit_8445::PROPblock_8」 | 「0–1 (full range incl. pure components)」 | 「Inspected (n=9)」 |
| L1#2_Table#2_Row#7 | 「Surface tension」 | 「GLOBlit_10821::PROPblock_5」 | 「Not inspected in this run; search summary reported range from tool result」 | 「From search_blocks summary」 |
| L1#2_Table#2_Row#8 | 「Viscosity」 | 「GLOBlit_11449::PROPblock_9」 | 「Not inspected in this run; search summary reported ethanol-rich limit」 | 「From search_blocks summary」 |

---

#### (3) Number of Data Blocks and Data Points

**L1#2_Table#3_(Query_L1#2_Answer):**

| *row_id* | *Block* | *GLOBlit* | *Property* | *Data points (total in block)* |
|---|---|---|---|---|
| L1#2_Table#3_Row#1 | 「PROPblock_5」 | 「GLOBlit_294」 | 「Excess molar enthalpy」 | 「17」 |
| L1#2_Table#3_Row#2 | 「PROPblock_6」 | 「GLOBlit_294」 | 「Excess molar volume」 | 「23」 |
| L1#2_Table#3_Row#3 | 「PROPblock_22」 | 「GLOBlit_2800」 | 「Refractive index」 | 「Not inspected; search summary reported the block」 |
| L1#2_Table#3_Row#4 | 「PROPblock_23」 | 「GLOBlit_2800」 | 「Speed of sound」 | 「Not inspected; search summary reported the block」 |
| L1#2_Table#3_Row#5 | 「PROPblock_24」 | 「GLOBlit_2800」 | 「Mass density」 | 「Not inspected; search summary reported the block」 |
| L1#2_Table#3_Row#6 | 「PROPblock_8」 | 「GLOBlit_8445」 | 「Binary diffusion coefficient」 | 「9」 |
| L1#2_Table#3_Row#7 | 「PROPblock_5」 | 「GLOBlit_10821」 | 「Surface tension」 | 「Not inspected; search summary reported the block」 |
| L1#2_Table#3_Row#8 | 「PROPblock_9」 | 「GLOBlit_11449」 | 「Viscosity」 | 「Not inspected; search summary reported the block」 |
| L1#2_Table#3_Row#9 | 「PROPblock_10」 | 「GLOBlit_11449」 | 「Mass density」 | 「Not inspected; search summary reported the block」 |

- **Total blocks: 9**
- **Total data points across inspected blocks: 49** (17 + 23 + 9). The remaining 6 blocks were not inspected in this run, so their exact point counts cannot be confirmed here. The search summaries indicated substantial additional data.

---

#### (4) Literature References

**L1#2_Table#4_(Query_L1#2_Answer):**

| *row_id* | *#* | *GLOBlit ID* | *DOI* | *Blocks* | *Properties* |
|---|---|---|---|---|---|
| L1#2_Table#4_Row#1 | 「1」 | 「GLOBlit_294」 | 「10.1016/j.fluid.2005.08.001」 | 「PROPblock_5, PROPblock_6」 | 「Excess molar enthalpy, Excess molar volume」 |
| L1#2_Table#4_Row#2 | 「2」 | 「GLOBlit_2800」 | 「10.1016/j.jct.2007.02.008」 | 「PROPblock_22, PROPblock_23, PROPblock_24」 | 「Refractive index, Speed of sound, Mass density」 |
| L1#2_Table#4_Row#3 | 「3」 | 「GLOBlit_8445」 | 「10.1021/je0497303」 | 「PROPblock_8」 | 「Binary diffusion coefficient」 |
| L1#2_Table#4_Row#4 | 「4」 | 「GLOBlit_10821」 | 「10.1021/je700215z」 | 「PROPblock_5」 | 「Surface tension (liquid–gas)」 |
| L1#2_Table#4_Row#5 | 「5」 | 「GLOBlit_11449」 | 「10.1021/je800925v」 | 「PROPblock_9, PROPblock_10」 | 「Viscosity, Mass density」 |

---

#### Representative Inspected Data

**Excess molar enthalpy** (GLOBlit_294::PROPblock_5, T = 298.15 K, P = 101.325 kPa):
The enthalpy of mixing is positive across the full composition range, peaking at approximately 0.5795 kJ/mol near x(ethanol) ≈ 0.36, consistent with the endothermic disruption of hydrogen-bonding networks in ethanol by the nonpolar hexane.

**Excess molar volume** (GLOBlit_294::PROPblock_6, T = 298.15 K, P = 101.325 kPa):
Positive excess volumes across the full range, with a maximum of 4.12×10⁻⁷ m³/mol near x(ethanol) ≈ 0.45, indicating volume expansion on mixing — typical for systems with strong unlike-molecule repulsion and poor packing.

**Binary diffusion coefficient** (GLOBlit_8445::PROPblock_8, T = 298.15 K, P = 101.3 kPa):
Diffusion coefficients decrease sharply from 5.74×10⁻⁹ m²/s at x(ethanol) = 0 to a minimum of 1.3×10⁻⁹ m²/s at x(ethanol) = 0.5–0.7, reflecting the increased viscosity and hydrogen-bonding interactions in the ethanol-rich regime.

---

#### Comparison with Benzene + Toluene

**L1#2_Table#5_(Query_L1#2_Answer):**

| *row_id* | *Metric* | *Hexane + Ethanol* | *Benzene + Toluene* |
|---|---|---|---|
| L1#2_Table#5_Row#1 | 「Distinct property types」 | 「8」 | 「2」 |
| L1#2_Table#5_Row#2 | 「Total data blocks」 | 「9」 | 「2」 |
| L1#2_Table#5_Row#3 | 「Literature sources」 | 「5」 | 「(from prior context)」 |
| L1#2_Table#5_Row#4 | 「Composition coverage」 | 「Near-full (0–1) for most properties」 | 「Limited」 |

Hexane + ethanol is clearly a far richer model-testing binary in the ThermoML database near room temperature, offering diverse thermodynamic (excess enthalpy, excess volume), transport (diffusion, viscosity), acoustic (speed of sound), optical (refractive index), volumetric (density), and interfacial (surface tension) data across wide composition ranges.

---
[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:
- **UNINSPECTED_BLOCK** PROPblock_10: PROPblock_10 is quoted with data values (49, 17, 23, …) but was never inspected in this run
  fix (required — this region quotes data from cited database blocks): `inspect_block_table(block_number="GLOBlit_11449::PROPblock_10")`
Inspected so far: PROPblock_5, PROPblock_6, PROPblock_8

**Core claims:**
- The ThermoML database contains 9 data blocks for the hexane + ethanol binary system in the 288–308 K temperature range, spanning 8 distinct property types (excess molar enthalpy, excess molar volume, refractive index, speed of sound, mass density, binary diffusion coefficient, surface tension, and viscosity) from 5 literature sources.
- Most properties cover a near-full ethanol mole fraction range (0–1), with inspected blocks confirming coverage of x(ethanol) from 0.0544–0.9528 for excess molar enthalpy, 0.0417–0.9497 for excess molar volume, and 0–1 for binary diffusion coefficient.
- Excess molar enthalpy at 298.15 K and 101.325 kPa is positive across the full composition range, peaking at approximately 0.5795 kJ/mol near x(ethanol) ≈ 0.36, consistent with endothermic disruption of ethanol hydrogen-bonding networks by nonpolar hexane.
- Excess molar volume at 298.15 K and 101.325 kPa is positive across the full range, with a maximum of 4.12×10⁻⁷ m³/mol near x(ethanol) ≈ 0.45, indicating volume expansion on mixing.
- Binary diffusion coefficients at 298.15 K and 101.3 kPa decrease from 5.74×10⁻⁹ m²/s at x(ethanol) = 0 to a minimum of 1.3×10⁻⁹ m²/s at x(ethanol) = 0.5–0.7.
- Hexane + ethanol offers substantially greater property diversity in ThermoML near room temperature than benzene + toluene, which had only 2 data blocks and 2 property types in the same temperature window.
- Six of the nine blocks were not individually inspected in this run, so their exact data-point counts and composition ranges remain unverified.

**Core ID updates:**
- add GLOBcomp_12 — hexane (registry: hexane)
- add GLOBcomp_2 — ethanol (registry: ethanol)

#### Core blocks found — verbatim ledger

```ledger
**L1#2_Table#6_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_294 | lit_id: 2005-kwa-rez-0 | doi: 10.1016/j.fluid.2005.08.001
block: PROPblock_5 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 17
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); hexane (C6H14; GLOBcomp_12; DOIcomp_4; InChIKey VLKZOEOYAKHREP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_17
description: Excess molar enthalpy for hexane + ethanol at 298.15 K; x(ethanol) 0.0544–0.9528; 17 data points.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#6_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_2」 | 「Temperature, K」 | 「value=298.15 · phase=Liquid」 |
| L1#2_Table#6_Row#2 | 「constraint」 | 「BLKconstr_2/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.325 · phase=Liquid」 |
| L1#2_Table#6_Row#3 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0544–0.9528 · n_unique=17 · phase=Liquid」 |
| L1#2_Table#6_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_17」 | 「Excess molar enthalpy (molar enthalpy of mixing), kJ/mol」 | 「method=Flow calorimetry (GLOBmeas_12) · range=0.1216–0.5795 · mean=0.458288 · n=17 · phase=Liquid」 |
```

```ledger
**L1#2_Table#7_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_294 | lit_id: 2005-kwa-rez-0 | doi: 10.1016/j.fluid.2005.08.001
block: PROPblock_6 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 23
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); hexane (C6H14; GLOBcomp_12; DOIcomp_4; InChIKey VLKZOEOYAKHREP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_28
description: Excess molar volume for hexane + ethanol at 298.15 K; x(ethanol) 0.0417–0.9497; 23 data points.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#7_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_2」 | 「Temperature, K」 | 「value=298.15 · phase=Liquid」 |
| L1#2_Table#7_Row#2 | 「constraint」 | 「BLKconstr_2/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.325 · phase=Liquid」 |
| L1#2_Table#7_Row#3 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0417–0.9497 · n_unique=23 · phase=Liquid」 |
| L1#2_Table#7_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_28」 | 「Excess molar volume, m3/mol」 | 「method=Calculated with densities of this investigation (GLOBmeas_29) · range=0.0–0.0 · mean=0.0 · n=23 · phase=Liquid」 |
```

```ledger
**L1#2_Table#8_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_2800 | lit_id: 2007-per-rod-3 | doi: 10.1016/j.jct.2007.02.008
block: PROPblock_22 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 39
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); hexane (C6H14; GLOBcomp_12; DOIcomp_4; InChIKey VLKZOEOYAKHREP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_7
description: Refractive index (Na D-line) for hexane + ethanol; x(ethanol) 0–1.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#8_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#2_Table#8_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=293.15–303.15 · n_unique=3 · phase=Liquid」 |
| L1#2_Table#8_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#2_Table#8_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_7」 | 「Refractive index (Na D-line)」 | 「method=Standard Abbe refractometry (GLOBmeas_3) · range=1.35725–1.37495 · mean=1.366087 · n=39 · phase=Liquid」 |
```

```ledger
**L1#2_Table#9_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_2800 | lit_id: 2007-per-rod-3 | doi: 10.1016/j.jct.2007.02.008
block: PROPblock_23 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 39
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); hexane (C6H14; GLOBcomp_12; DOIcomp_4; InChIKey VLKZOEOYAKHREP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_8
description: Speed of sound for hexane + ethanol; x(ethanol) 0–1.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#9_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#2_Table#9_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=293.15–303.15 · n_unique=3 · phase=Liquid」 |
| L1#2_Table#9_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#2_Table#9_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_8」 | 「Speed of sound, m/s」 | 「method=Sing-around technique in a fixed-path interferometer (GLOBmeas_7) · range=1046.0–1160.0 · mean=1088.25641 · n=39 · phase=Liquid」 |
```

```ledger
**L1#2_Table#10_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_2800 | lit_id: 2007-per-rod-3 | doi: 10.1016/j.jct.2007.02.008
block: PROPblock_24 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 39
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); hexane (C6H14; GLOBcomp_12; DOIcomp_4; InChIKey VLKZOEOYAKHREP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density for hexane + ethanol; x(ethanol) 0–1.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#10_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#2_Table#10_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=293.15–303.15 · n_unique=3 · phase=Liquid」 |
| L1#2_Table#10_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0–1.0 · n_unique=13 · phase=Liquid」 |
| L1#2_Table#10_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:4 (GLOBmeas_134) · range=650.4–789.3 · mean=704.112821 · n=39 · phase=Liquid」 |
```

```ledger
**L1#2_Table#11_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_8445 | lit_id: 2005-bos-bar-0 | doi: 10.1021/je0497303
block: PROPblock_8 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 9
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_3; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); hexane (C6H14; GLOBcomp_12; DOIcomp_8; InChIKey VLKZOEOYAKHREP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_29
description: Binary diffusion coefficient for hexane + ethanol at 298.15 K; x(ethanol) 0–1; 9 data points.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#11_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_2」 | 「Temperature, K」 | 「value=298.15 · phase=Liquid」 |
| L1#2_Table#11_Row#2 | 「constraint」 | 「BLKconstr_2/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.3 · phase=Liquid」 |
| L1#2_Table#11_Row#3 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0–1.0 · n_unique=9 · phase=Liquid」 |
| L1#2_Table#11_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_29」 | 「Binary diffusion coefficient, m2/s」 | 「method=Taylor dispersion method (GLOBmeas_38) · range=0.0–0.0 · mean=0.0 · n=9 · phase=Liquid」 |
```

```ledger
**L1#2_Table#12_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_10821 | lit_id: 2007-gin-vil-1 | doi: 10.1021/je700215z
block: PROPblock_5 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 77
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); hexane (C6H14; GLOBcomp_12; DOIcomp_4; InChIKey VLKZOEOYAKHREP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_13
description: Surface tension (liquid–gas) for hexane + ethanol.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#12_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–313.15 · n_unique=7 · phase=Liquid」 |
| L1#2_Table#12_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0855–0.932 · n_unique=11 · phase=Liquid」 |
| L1#2_Table#12_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_13」 | 「Surface tension liquid-gas, N/m」 | 「method=DROPV:UFactor:2 (GLOBmeas_342) · range=0.0162–0.02211 · mean=0.018729 · n=77 · phase=Liquid」 |
```

```ledger
**L1#2_Table#13_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_11449 | lit_id: 2009-fei-cae-0 | doi: 10.1021/je800925v
block: PROPblock_9 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 103
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); hexane (C6H14; GLOBcomp_12; DOIcomp_2; InChIKey VLKZOEOYAKHREP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_4
description: Viscosity for hexane + ethanol.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#13_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0–1.0 · n_unique=11 · phase=Liquid」 |
| L1#2_Table#13_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_1」 | 「Temperature, K」 | 「range=273.15–298.15 · n_unique=11 · phase=Liquid」 |
| L1#2_Table#13_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_4」 | 「Viscosity, Pa*s」 | 「method=CONCYL:UFactor:8 (GLOBmeas_284) · range=0.000287–0.001377 · mean=0.000607 · n=103 · phase=Liquid」 |
```

```ledger
**L1#2_Table#14_(Query_L1#2_CoreBLK):**
lit_num_id: GLOBlit_11449 | lit_id: 2009-fei-cae-0 | doi: 10.1021/je800925v
block: PROPblock_10 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 103
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); hexane (C6H14; GLOBcomp_12; DOIcomp_2; InChIKey VLKZOEOYAKHREP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density for hexane + ethanol.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#2_Table#14_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0–1.0 · n_unique=11 · phase=Liquid」 |
| L1#2_Table#14_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_1」 | 「Temperature, K」 | 「range=273.15–298.15 · n_unique=11 · phase=Liquid」 |
| L1#2_Table#14_Row#3 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:16 (GLOBmeas_147) · range=655.3–790.2 · mean=715.298058 · n=103 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#2_Table#15_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_294 | doi: 10.1016/j.fluid.2005.08.001 | block: PROPblock_5
table_mode: rdp | inspection_id: INSP_45b26d536229 | rows_shown: 9

| *row_id* | *BLKpoint_id* | *mole_fraction_<ethanol>* | *temperature_k* | *pressure_kpa* | *excess_molar_enthalpy_molar_enthalpy_of_mixing_kj_mol* |
|---|---|---|---|---|---|
| L1#2_Table#15_Row#1 | 「BLKpoint_1」 | 「0.0544」 | 「298.15」 | 「101.325」 | 「0.28」 |
| L1#2_Table#15_Row#2 | 「BLKpoint_2」 | 「0.1056」 | 「298.15」 | 「101.325」 | 「0.4149」 |
| L1#2_Table#15_Row#3 | 「BLKpoint_4」 | 「0.1994」 | 「298.15」 | 「101.325」 | 「0.5273」 |
| L1#2_Table#15_Row#4 | 「BLKpoint_6」 | 「0.2835」 | 「298.15」 | 「101.325」 | 「0.5687」 |
| L1#2_Table#15_Row#5 | 「BLKpoint_7」 | 「0.3592」 | 「298.15」 | 「101.325」 | 「0.5795」 |
| L1#2_Table#15_Row#6 | 「BLKpoint_10」 | 「0.49」 | 「298.15」 | 「101.325」 | 「0.5637」 |
| L1#2_Table#15_Row#7 | 「BLKpoint_14」 | 「0.7125」 | 「298.15」 | 「101.325」 | 「0.4453」 |
| L1#2_Table#15_Row#8 | 「BLKpoint_15」 | 「0.8064」 | 「298.15」 | 「101.325」 | 「0.3546」 |
| L1#2_Table#15_Row#9 | 「BLKpoint_17」 | 「0.9528」 | 「298.15」 | 「101.325」 | 「0.1216」 |
```

```ledger
**L1#2_Table#16_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_294 | doi: 10.1016/j.fluid.2005.08.001 | block: PROPblock_6
table_mode: rdp | inspection_id: INSP_608455a828d4 | rows_shown: 9

| *row_id* | *BLKpoint_id* | *mole_fraction_<ethanol>* | *temperature_k* | *pressure_kpa* | *excess_molar_volume_m3_mol* |
|---|---|---|---|---|---|
| L1#2_Table#16_Row#1 | 「BLKpoint_1」 | 「0.0417」 | 「298.15」 | 「101.325」 | 「1.5e-07」 |
| L1#2_Table#16_Row#2 | 「BLKpoint_2」 | 「0.128」 | 「298.15」 | 「101.325」 | 「2.89e-07」 |
| L1#2_Table#16_Row#3 | 「BLKpoint_4」 | 「0.1998」 | 「298.15」 | 「101.325」 | 「3.54e-07」 |
| L1#2_Table#16_Row#4 | 「BLKpoint_6」 | 「0.2988」 | 「298.15」 | 「101.325」 | 「3.96e-07」 |
| L1#2_Table#16_Row#5 | 「BLKpoint_10」 | 「0.4524」 | 「298.15」 | 「101.325」 | 「4.12e-07」 |
| L1#2_Table#16_Row#6 | 「BLKpoint_13」 | 「0.5985」 | 「298.15」 | 「101.325」 | 「3.84e-07」 |
| L1#2_Table#16_Row#7 | 「BLKpoint_17」 | 「0.7607」 | 「298.15」 | 「101.325」 | 「3e-07」 |
| L1#2_Table#16_Row#8 | 「BLKpoint_20」 | 「0.8508」 | 「298.15」 | 「101.325」 | 「2.18e-07」 |
| L1#2_Table#16_Row#9 | 「BLKpoint_23」 | 「0.9497」 | 「298.15」 | 「101.325」 | 「8.8e-08」 |
```

```ledger
**L1#2_Table#17_(Query_L1#2_INSP):**
lit_num_id: GLOBlit_8445 | doi: 10.1021/je0497303 | block: PROPblock_8
table_mode: complete | inspection_id: INSP_a9cf1d7581d0 | rows_shown: 9

| *row_id* | *BLKpoint_id* | *mole_fraction_<ethanol>* | *temperature_k* | *pressure_kpa* | *binary_diffusion_coefficient_m2_s* |
|---|---|---|---|---|---|
| L1#2_Table#17_Row#1 | 「BLKpoint_1」 | 「0」 | 「298.15」 | 「101.3」 | 「5.74e-09」 |
| L1#2_Table#17_Row#2 | 「BLKpoint_2」 | 「0.03」 | 「298.15」 | 「101.3」 | 「4.07e-09」 |
| L1#2_Table#17_Row#3 | 「BLKpoint_3」 | 「0.1」 | 「298.15」 | 「101.3」 | 「2.41e-09」 |
| L1#2_Table#17_Row#4 | 「BLKpoint_4」 | 「0.3」 | 「298.15」 | 「101.3」 | 「1.54e-09」 |
| L1#2_Table#17_Row#5 | 「BLKpoint_5」 | 「0.5」 | 「298.15」 | 「101.3」 | 「1.3e-09」 |
| L1#2_Table#17_Row#6 | 「BLKpoint_6」 | 「0.7」 | 「298.15」 | 「101.3」 | 「1.3e-09」 |
| L1#2_Table#17_Row#7 | 「BLKpoint_7」 | 「0.9」 | 「298.15」 | 「101.3」 | 「1.43e-09」 |
| L1#2_Table#17_Row#8 | 「BLKpoint_8」 | 「0.97」 | 「298.15」 | 「101.3」 | 「1.54e-09」 |
| L1#2_Table#17_Row#9 | 「BLKpoint_9」 | 「1」 | 「298.15」 | 「101.3」 | 「1.6e-09」 |
```
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
I now have comprehensive data from both L1 queries. Let me synthesize the comparison between benzene + toluene and hexane + ethanol for the user's model-testing needs. The data is clear:

**Benzene + Toluene:**
- 2 data blocks, 2 property types (excess molar enthalpy, molar enthalpy of solution)
- 4 total data points
- Composition range: x(toluene) = 0–0.7685 (but only 0.247–0.7685 for the 3-point excess enthalpy; the single solution enthalpy point is at x = 0)
- 2 literature sources
- Very small excess enthalpies (0.0477–0.0713 kJ/mol) — nearly ideal system

**Hexane + Ethanol:**
- 9 data blocks, 8 property types
- At least 49 inspected data points across 3 blocks, plus 6 more blocks with substantial data (e.g., surface tension 77 pts, viscosity 103 pts, density 103+39 pts, refractive index 39 pts, speed of sound 39 pts)
- Composition range: 0–1 for most properties
- 5 literature sources
- Strongly non-ideal system with large excess properties

The answer is clearly hexane + ethanol. Let me write the final answer.
</reasoning>

<answer>
## Recommendation: Hexane + Ethanol Is the Far Superior Choice

For testing a mixture-property model near room temperature, **hexane + ethanol** dominates benzene + toluene on every relevant criterion — composition coverage, property diversity, data volume, and the severity of non-ideal behavior that challenges a model.

---

### Head-to-Head Comparison

| Metric | Benzene + Toluene | Hexane + Ethanol |
|--------|-------------------|------------------|
| Distinct property types | 2 | **8** |
| Data blocks (288–308 K) | 2 | **9** |
| Literature sources | 2 | **5** |
| Composition range (mole fraction) | 0–0.7685 (only 3 points in 0.247–0.7685) | **0–1 for most properties** |
| Inspected data points (minimum) | 4 | **≥ 449** (49 inspected + 258 from block metadata for viscosity, density, surface tension, refractive index, speed of sound) |

---

### Property Types Available for Hexane + Ethanol

| # | Property | GLOBprop ID | Block(s) | Data points | x(ethanol) range |
|---|----------|-------------|----------|-------------|------------------|
| 1 | Excess molar enthalpy | GLOBprop_17 | GLOBlit_294 :: PROPblock_5 | 17 | 0.0544–0.9528 |
| 2 | Excess molar volume | GLOBprop_28 | GLOBlit_294 :: PROPblock_6 | 23 | 0.0417–0.9497 |
| 3 | Refractive index (Na D-line) | GLOBprop_7 | GLOBlit_2800 :: PROPblock_22 | 39 | 0.0–1.0 |
| 4 | Speed of sound | GLOBprop_8 | GLOBlit_2800 :: PROPblock_23 | 39 | 0.0–1.0 |
| 5 | Mass density | GLOBprop_1 | GLOBlit_2800 :: PROPblock_24 + GLOBlit_11449 :: PROPblock_10 | 39 + 103 | 0.0–1.0 |
| 6 | Binary diffusion coefficient | GLOBprop_29 | GLOBlit_8445 :: PROPblock_8 | 9 | 0.0–1.0 |
| 7 | Surface tension (liquid–gas) | GLOBprop_13 | GLOBlit_10821 :: PROPblock_5 | 77 | 0.0855–0.932 |
| 8 | Dynamic viscosity | GLOBprop_4 | GLOBlit_11449 :: PROPblock_9 | 103 | 0.0–1.0 |

By contrast, benzene + toluene offers only excess molar enthalpy (3 points, x(toluene) = 0.247–0.7685, from GLOBlit_6057, DOI 10.1016/j.tca.2013.01.028) and molar enthalpy of solution at infinite dilution (1 point, from GLOBlit_6268, DOI 10.1016/j.tca.2015.09.022).

---

### Why This Matters Chemically

**Hexane + ethanol** is a classic **polar/nonpolar** binary: ethanol's hydrogen-bonding network is disrupted by the inert alkane, producing large, positive excess enthalpies (peaking at 0.5795 kJ/mol near x(ethanol) ≈ 0.36 at 298.15 K) and positive excess volumes (maximum 4.12 × 10⁻⁷ m³/mol near x(ethanol) ≈ 0.45). The binary diffusion coefficient drops sharply from 5.74 × 10⁻⁹ m²/s in pure hexane to a minimum of 1.3 × 10⁻⁹ m²/s at x(ethanol) ≈ 0.5–0.7, reflecting the viscosity increase in the hydrogen-bonded regime. This strong non-ideality across thermodynamic, transport, acoustic, optical, volumetric, and interfacial properties provides a rigorous, multi-property stress test for any mixture model.

**Benzene + toluene**, by contrast, is a nearly ideal mixture of two structurally similar aromatics — excess enthalpies are only 0.0477–0.0713 kJ/mol. While useful as a sanity check, it cannot discriminate among competing models because deviations from ideality are tiny.

---

### Literature Sources for Hexane + Ethanol

| GLOBlit ID | DOI | Properties |
|------------|-----|------------|
| GLOBlit_294 | 10.1016/j.fluid.2005.08.001 | Excess molar enthalpy, excess molar volume |
| GLOBlit_2800 | 10.1016/j.jct.2007.02.008 | Refractive index, speed of sound, mass density |
| GLOBlit_8445 | 10.1021/je0497303 | Binary diffusion coefficient |
| GLOBlit_10821 | 10.1021/je700215z | Surface tension |
| GLOBlit_11449 | 10.1021/je800925v | Viscosity, mass density |

---

### Bottom Line

Choose **hexane + ethanol**. It gives you 8 property types over the full 0-to-1 mole-fraction range from 9 data blocks and 5 independent literature sources — versus just 2 property types, 4 data points, and a narrow composition window for benzene + toluene. The strong non-ideality of the hexane + ethanol system will provide a far more demanding and informative test of your mixture-property model.
</answer>