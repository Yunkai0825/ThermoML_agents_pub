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
| comp | GLOBcomp_2407 | oxirane | oxirane |
| comp | GLOBcomp_952 | 1,3,5-trioxane | 1,3,5-trioxane |
| comp | GLOBcomp_1480 | 2,4,6-trimethyl-1,3,5-trioxane | 2,4,6-trimethyl-1,3,5-trioxane |

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->
- [L1] Search for compounds matching 'ethylene trioxide', '1,3,5-trioxane', 'trioxane', 'trioxolane', or 'ethylene oxide' in Th → stored as L1_query_1 · validation: PASS
- [L1] Find viscosity data blocks for 1,3,5-trioxane + water and oxirane + water binary systems → stored as L1_query_2 · validation: PASS

## Results
<!-- Indexed findings. Compactable per-entry. -->
### L1_query_1
**L1_query_1** — status: success · validation: PASS

**Summary:** No compound named "ethylene trioxide" exists in the ThermoML database. The closest matches found are oxirane (ethylene oxide, GLOBcomp_2407, C₂H₄O, SMILES C1CO1), 1,3,5-trioxane (GLOBcomp_952, C₃H₆O₃, SMILES C1OCOCO1), and 2,4,6-trimethyl-1,3,5-trioxane (GLOBcomp_1480, C₆H₁₂O₃). Trioxolane (1,2,4-trioxolane / ozonide class) is also not present. "Ethylene trioxide" is not a standard IUPAC name; the most plausible candidate if "trioxide" refers to three ring oxygens is 1,3,5-trioxane (GLOBcomp_952). Oxirane (GLOBcomp_2407) contains only one oxygen and would not match "trioxide."

**Answer:**

The ThermoML database was searched for compounds matching "ethylene trioxide," "trioxane," "trioxolane," and "ethylene oxide." Here are the results:

**Compounds found:**

**WM_L1_Q1_Table#1_(Query_L1_Q1_Answer):**

| *row_id* | *Global ID* | *Name* | *Molecular Formula* | *SMILES* |
|---|---|---|---|---|
| WM_L1_Q1_Table#1_Row#1 | 「GLOBcomp_2407」 | 「oxirane (ethylene oxide)」 | 「C₂H₄O」 | 「C1CO1」 |
| WM_L1_Q1_Table#1_Row#2 | 「GLOBcomp_952」 | 「1,3,5-trioxane」 | 「C₃H₆O₃」 | 「C1OCOCO1」 |
| WM_L1_Q1_Table#1_Row#3 | 「GLOBcomp_1480」 | 「2,4,6-trimethyl-1,3,5-trioxane」 | 「C₆H₁₂O₃」 | 「CC1OC(C)OC(C)O1」 |

**Compounds not found:**
- **"Ethylene trioxide"** — No compound with this exact name exists in the ThermoML database.
- **Trioxolane** (1,2,4-trioxolane / ozonide class) — Not present in the database.

**Chemical context:**
- "Ethylene trioxide" is not a standard IUPAC name. It could potentially refer to **1,3,5-trioxane** (GLOBcomp_952), which is the cyclic trimer of formaldehyde (C₃H₆O₃), or less likely to ethylene oxide (oxirane, GLOBcomp_2407, C₂H₄O). The name "ethylene trioxide" does not correspond to any single well-established compound in standard chemical nomenclature or in the ThermoML database.
- **1,3,5-trioxane** (GLOBcomp_952) is the most plausible candidate if "trioxide" refers to the three oxygen atoms in the ring structure.
- **Oxirane / ethylene oxide** (GLOBcomp_2407) is a simple three-membered epoxide ring with only one oxygen, so it would not match "trioxide."

**Core claims:**
- No compound named "ethylene trioxide" exists in the ThermoML database; the name is not a standard IUPAC designation and does not correspond to any single well-established compound in standard chemical nomenclature.
- The closest plausible match in the ThermoML database is 1,3,5-trioxane (GLOBcomp_952, C₃H₆O₃), which contains three oxygen atoms in its ring structure.
- Oxirane (ethylene oxide, GLOBcomp_2407, C₂H₄O) is present in the database but contains only one oxygen atom and would not match a "trioxide" designation.
- Trioxolane (1,2,4-trioxolane / ozonide class) is not present in the ThermoML database.

*Not stored here: 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.
### L1_query_2
**L1_query_2** — status: no_results · validation: PASS

**Summary:** No viscosity data were found in the ThermoML database for any of the candidate binary systems: 1,3,5-trioxane (GLOBcomp_952) + water (GLOBcomp_1), oxirane/ethylene oxide (GLOBcomp_2407) + water (GLOBcomp_1), and 2,4,6-trimethyl-1,3,5-trioxane (GLOBcomp_1480) + water (GLOBcomp_1). Searches covered both dynamic viscosity (GLOBprop_4) and kinematic viscosity (GLOBprop_40) for declared binary systems, and all returned zero results.

**Answer:**

No viscosity data were found in the ThermoML database for any of the candidate binary systems:

1. **1,3,5-trioxane (GLOBcomp_952) + water (GLOBcomp_1)** — No dynamic viscosity (GLOBprop_4) or kinematic viscosity (GLOBprop_40) data blocks exist for this binary system.

2. **Oxirane / ethylene oxide (GLOBcomp_2407) + water (GLOBcomp_1)** — No viscosity data blocks found for this binary system either.

3. **2,4,6-trimethyl-1,3,5-trioxane (GLOBcomp_1480) + water (GLOBcomp_1)** — Also no viscosity data blocks found.

All three searches were conducted for declared binary systems with both dynamic and kinematic viscosity properties, and all returned zero results. The ThermoML database does not contain viscosity measurements for any of these aqueous binary systems involving trioxane-type compounds or oxirane.

**Core claims:**
- No dynamic viscosity or kinematic viscosity data were found in the ThermoML database for the binary systems 1,3,5-trioxane + water, oxirane (ethylene oxide) + water, or 2,4,6-trimethyl-1,3,5-trioxane + water.

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.



</memory>

## User
[Purpose: Locate viscosity data blocks for the ethylene trioxide-water system]
Find viscosity data for the ethylene trioxide and water binary system. Search for compound names including 'ethylene trioxide', '1,3,5-trioxane', 'trioxane', '1,2,3-trioxolane', 'trioxolane', and 'ethylene oxide'. I need to identify which compound is meant and find any viscosity measurements in ThermoML.

[Context: The user wants to estimate viscosity of ethylene trioxide-water system. The compound name is unusual and may correspond to 1,3,5-trioxane, trioxolane, or ethylene oxide. Need to search broadly.]

## Assistant
<summary>Starting search for viscosity data in the ethylene trioxide-water system. Will search for multiple possible compound names: ethylene trioxide, 1,3,5-trioxane, trioxane, trioxolane, and ethylene oxide, combined with viscosity (GLOBprop_4 for dynamic viscosity, GLOBprop_40 for kinematic viscosity).</summary>
<tool_call>L1_query(instruction=Search for compou…, id_catalog=, context=User is trying to…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — L1_query return

**Status:** status=success

**Summary:** No compound named "ethylene trioxide" exists in the ThermoML database. The closest matches found are oxirane (ethylene oxide, GLOBcomp_2407, C₂H₄O, SMILES C1CO1), 1,3,5-trioxane (GLOBcomp_952, C₃H₆O₃, SMILES C1OCOCO1), and 2,4,6-trimethyl-1,3,5-trioxane (GLOBcomp_1480, C₆H₁₂O₃). Trioxolane (1,2,4-trioxolane / ozonide class) is also not present. "Ethylene trioxide" is not a standard IUPAC name; the most plausible candidate if "trioxide" refers to three ring oxygens is 1,3,5-trioxane (GLOBcomp_952). Oxirane (GLOBcomp_2407) contains only one oxygen and would not match "trioxide."

**Answer:**

The ThermoML database was searched for compounds matching "ethylene trioxide," "trioxane," "trioxolane," and "ethylene oxide." Here are the results:

**Compounds found:**

**L1#1_Table#1_(Query_L1#1_Answer):**

| *row_id* | *Global ID* | *Name* | *Molecular Formula* | *SMILES* |
|---|---|---|---|---|
| L1#1_Table#1_Row#1 | 「GLOBcomp_2407」 | 「oxirane (ethylene oxide)」 | 「C₂H₄O」 | 「C1CO1」 |
| L1#1_Table#1_Row#2 | 「GLOBcomp_952」 | 「1,3,5-trioxane」 | 「C₃H₆O₃」 | 「C1OCOCO1」 |
| L1#1_Table#1_Row#3 | 「GLOBcomp_1480」 | 「2,4,6-trimethyl-1,3,5-trioxane」 | 「C₆H₁₂O₃」 | 「CC1OC(C)OC(C)O1」 |

**Compounds not found:**
- **"Ethylene trioxide"** — No compound with this exact name exists in the ThermoML database.
- **Trioxolane** (1,2,4-trioxolane / ozonide class) — Not present in the database.

**Chemical context:**
- "Ethylene trioxide" is not a standard IUPAC name. It could potentially refer to **1,3,5-trioxane** (GLOBcomp_952), which is the cyclic trimer of formaldehyde (C₃H₆O₃), or less likely to ethylene oxide (oxirane, GLOBcomp_2407, C₂H₄O). The name "ethylene trioxide" does not correspond to any single well-established compound in standard chemical nomenclature or in the ThermoML database.
- **1,3,5-trioxane** (GLOBcomp_952) is the most plausible candidate if "trioxide" refers to the three oxygen atoms in the ring structure.
- **Oxirane / ethylene oxide** (GLOBcomp_2407) is a simple three-membered epoxide ring with only one oxygen, so it would not match "trioxide."

**Core claims:**
- No compound named "ethylene trioxide" exists in the ThermoML database; the name is not a standard IUPAC designation and does not correspond to any single well-established compound in standard chemical nomenclature.
- The closest plausible match in the ThermoML database is 1,3,5-trioxane (GLOBcomp_952, C₃H₆O₃), which contains three oxygen atoms in its ring structure.
- Oxirane (ethylene oxide, GLOBcomp_2407, C₂H₄O) is present in the database but contains only one oxygen atom and would not match a "trioxide" designation.
- Trioxolane (1,2,4-trioxolane / ozonide class) is not present in the ThermoML database.

**Core ID updates:**
- add GLOBcomp_2407 — oxirane (registry: oxirane)
- add GLOBcomp_952 — 1,3,5-trioxane (registry: 1,3,5-trioxane)
- add GLOBcomp_1480 — 2,4,6-trimethyl-1,3,5-trioxane (registry: 2,4,6-trimethyl-1,3,5-trioxane)
</subagent_answer>
</tool_result>

## Assistant
<summary>Compound search confirmed: no "ethylene trioxide" in DB. Best candidates are 1,3,5-trioxane (GLOBcomp_952) and oxirane (GLOBcomp_2407). Now searching for viscosity data blocks (GLOBprop_4 dynamic viscosity, GLOBprop_40 kinematic viscosity) for binary systems of these compounds with water.</summary>
<tool_call>L1_query(instruction=Search for proper…, id_catalog=comp | GLOBcomp_2…, context=User wan…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#2 — L1_query return

**Status:** status=no_results

**Summary:** No viscosity data were found in the ThermoML database for any of the candidate binary systems: 1,3,5-trioxane (GLOBcomp_952) + water (GLOBcomp_1), oxirane/ethylene oxide (GLOBcomp_2407) + water (GLOBcomp_1), and 2,4,6-trimethyl-1,3,5-trioxane (GLOBcomp_1480) + water (GLOBcomp_1). Searches covered both dynamic viscosity (GLOBprop_4) and kinematic viscosity (GLOBprop_40) for declared binary systems, and all returned zero results.

**Answer:**

No viscosity data were found in the ThermoML database for any of the candidate binary systems:

1. **1,3,5-trioxane (GLOBcomp_952) + water (GLOBcomp_1)** — No dynamic viscosity (GLOBprop_4) or kinematic viscosity (GLOBprop_40) data blocks exist for this binary system.

2. **Oxirane / ethylene oxide (GLOBcomp_2407) + water (GLOBcomp_1)** — No viscosity data blocks found for this binary system either.

3. **2,4,6-trimethyl-1,3,5-trioxane (GLOBcomp_1480) + water (GLOBcomp_1)** — Also no viscosity data blocks found.

All three searches were conducted for declared binary systems with both dynamic and kinematic viscosity properties, and all returned zero results. The ThermoML database does not contain viscosity measurements for any of these aqueous binary systems involving trioxane-type compounds or oxirane.

**Core claims:**
- No dynamic viscosity or kinematic viscosity data were found in the ThermoML database for the binary systems 1,3,5-trioxane + water, oxirane (ethylene oxide) + water, or 2,4,6-trimethyl-1,3,5-trioxane + water.
</subagent_answer>
</tool_result>

## LLM Response
<reasoning>
Both queries have been completed. The results are clear:

1. No compound named "ethylene trioxide" exists in the ThermoML database.
2. The closest candidates are 1,3,5-trioxane (GLOBcomp_952), oxirane/ethylene oxide (GLOBcomp_2407), and 2,4,6-trimethyl-1,3,5-trioxane (GLOBcomp_1480).
3. No viscosity data (dynamic or kinematic) exist for any of these compounds in binary systems with water.

I should provide a comprehensive final answer.
</reasoning>

<answer>
## Viscosity Data Search: "Ethylene Trioxide"–Water System

### Compound Identification

**"Ethylene trioxide" is not a standard IUPAC name** and does not correspond to any compound in the ThermoML database under that exact designation. The database was searched broadly for related compounds:

| Global ID | Name | Molecular Formula | SMILES |
|---|---|---|---|
| GLOBcomp_952 | 1,3,5-trioxane | C₃H₆O₃ | C1OCOCO1 |
| GLOBcomp_2407 | oxirane (ethylene oxide) | C₂H₄O | C1CO1 |
| GLOBcomp_1480 | 2,4,6-trimethyl-1,3,5-trioxane | C₆H₁₂O₃ | CC1OC(C)OC(C)O1 |

- **1,3,5-trioxane** (GLOBcomp_952) is the most plausible candidate if "trioxide" refers to three oxygen atoms in the ring. It is the cyclic trimer of formaldehyde.
- **Oxirane / ethylene oxide** (GLOBcomp_2407) contains only one oxygen atom and would not match a "trioxide" designation.
- **Trioxolane** (1,2,4-trioxolane / ozonide class) and **1,2,3-trioxolane** are **not present** in the ThermoML database at all.

### Viscosity Data: Not Found

**No viscosity data exist in the ThermoML database** for any of the following binary aqueous systems:

1. **1,3,5-trioxane + water** — No dynamic viscosity or kinematic viscosity data blocks.
2. **Oxirane (ethylene oxide) + water** — No viscosity data blocks.
3. **2,4,6-trimethyl-1,3,5-trioxane + water** — No viscosity data blocks.

Searches covered both dynamic viscosity (η) and kinematic viscosity (ν) for all three binary systems, and all returned zero results.

### Summary

The compound "ethylene trioxide" cannot be unambiguously identified, but the best candidate in the ThermoML database is **1,3,5-trioxane** (GLOBcomp_952, C₃H₆O₃). Unfortunately, the ThermoML database contains **no viscosity measurements** for any binary system pairing 1,3,5-trioxane (or oxirane, or trimethyl-trioxane) with water. To obtain viscosity data for these systems, external literature sources or experimental measurements would be needed.
</answer>