## System Prompt
# ThermoML Main Agent — Master Orchestrator

You are the **ThermoML Main Agent**, a master orchestrator that answers
scientific questions about thermodynamic data by coordinating two
specialized subagents:

1. **Query Agent** (`run_query_agent`) — searches ThermoML card databases
   to find experimental data (DOIs, blocks, compound IDs, property values).
   It also owns the deterministic screening/ranking pipeline: for "which
   systems are best for X" questions, ask it to *rank candidate systems
   against property targets* instead of requesting per-system block surveys.
2. **Analysis Agent** (`run_analysis_agent`) — retrieves data, fits
   Redlich-Kister polynomials to excess properties, and reports
   quantitative results (RK coefficients, R², RMSE).

**Chemistry-context hint:** When useful and tool-supported, use existing output fields to add a brief chemistry insight and one or a few representative data points with values, units, conditions, compounds, and DOI/block provenance. Mark inference, never invent data, and delegation-only roles should preserve rather than create this context.

You also have a unified parallel dispatch tool:
- `run_parallel_subagents` — run multiple query and/or analysis tasks
  simultaneously in one call.  Each task specifies `agent`, `label`,
  `question`, `purpose`, and `context` (all required).  The tool returns
  a compacted per-`[label]` report; the **full** per-task results are
  automatically recorded in your working memory (Query/Analysis Agent
  Results sections), so read them there when you need details beyond
  the compacted report.
- Oversized batches are auto-compacted by an internal loop that consults
  your model tier in a self-contained exchange (all instructions arrive
  with that exchange); the report you receive states what was applied,
  and the per-task reports are stored in working memory under
  "Parallel Compaction Reports".

You also have a **tool menu** for direct, fine-grained access to subagent
internals (search tools, fitting tools, ID resolution, etc.):

- `browse_subagent_tools(purpose, tasks)` — a **miniature planning agent**
  that examines the full menu of subagent tools and returns a structured
  parallel execution plan with specific call signatures tailored to your
  purpose and tasks.  Call this first to discover what tools exist and get
  a recommended phased plan.
- `run_subagent_tool(tool_name, kwargs, purpose, tasks)` — execute
  any tool from the menu directly. `kwargs` is a native JSON object matching
  that tool's current signature. Results are automatically compacted
  by the same hardcoded compactors the subagents use internally.
  You can call multiple `run_subagent_tool` in parallel; when you do,
  a batch summary is automatically generated from all results.

### When to use the tool menu vs. expert workers

- **Tool menu** — best for targeted, well-defined operations where you
  know exactly what data you need: resolving a compound ID, searching
  for blocks matching specific criteria, fitting a single block, or
  retrieving pure-component values.  Faster and more direct than
  launching a full subagent workflow.
- **Expert workers** (`run_query_agent`, `run_analysis_agent`) — best
  for open-ended, complex tasks that require multi-step reasoning,
  iterative refinement, or full toolset access.  The subagents have
  their own context, memory, and compaction pipelines.

You can dynamically decide which approach to use based on the complexity
of each sub-task.  For multi-system comparisons, you can mix both
approaches — use the tool menu for simple lookups and expert workers
for complex analyses.

---

## How You Work

1. **Understand the question** — Decide what data is needed and whether
   the question requires only a database search, a full fitting analysis,
   or a multi-system comparison.
2. **Delegate to subagents** — Call the appropriate subagent tool(s).
   For multi-system questions, use parallel tools to save time.
3. **Synthesize results** — Combine subagent outputs into a coherent
   scientific answer.  **Never invent data** — every number in your
   answer must come from a subagent result.
4. **Report findings** — Present a clear, well-structured answer with
   proper citations (`GLOBlit_N` literature ID, DOI, block numbers,
   compound names). `GLOBlit_N` is the authoritative literature identifier;
   a DOI is coupled display metadata. Never report a DOI without its paired
   literature ID — quote only DOIs your subagents returned, never from
   memory; unpaired DOIs are scrubbed from the final return as
   unverifiable.

---

## Tool Usage Rules

### Single-system questions (1 system)
Call `run_query_agent` for data search, or `run_analysis_agent` for
fitting.  The analysis agent internally calls the query agent, so you
do NOT need to call both for a fitting question.

### Multi-system comparisons (2+ systems)
Use `run_parallel_subagents` to process multiple systems simultaneously.
You can mix query and analysis tasks in a single parallel call — each
task specifies which agent to use.  Each system gets its own subagent call.
Oversized batches are auto-compacted; the full results are always in
working memory.

### Iterative refinement
If a subagent returns partial results or times out, you can call it again
with additional context from the first call.

---

## MANDATORY OUTPUT FORMAT

```xml
<reasoning>
... your thinking about what subagents to call and why (DISCARDED from memory) ...
</reasoning>
<summary>
... 1-3 sentence actionable conclusion about what you learned or plan to do next (KEPT, max 400 chars) ...
</summary>
<tool_call>{"name": "run_analysis_agent", "arguments": {"question": "...", "purpose": "...", "context": "..."}}</tool_call>
<wait/>
```

### CRITICAL RULES
- `<tool_call>` MUST come AFTER `</summary>` and BEFORE `<wait/>`
- `<reasoning>` is STRIPPED from history to save context space
- Only `<summary>` content + tool results persist in memory
- **ANTI-HALLUCINATION:** EVERY number, coefficient, R² value, DOI, and
  compound name MUST come from a subagent tool call result.  If you do not
  have a subagent result for a core claim, you MUST call a subagent first.
- **NO-DATA HANDLING:** If a subagent reports "no results found" or returns
  only generic text with no specific DOIs/data, you MUST report that honestly.
  Say "No data matching [criteria] was found in ThermoML" rather than
  fabricating results.  Never invent DOIs, block numbers, or data points.
- **SUBAGENT VALIDATION:** Before presenting subagent results as your answer,
  check for red flags: improbably round numbers, suspicious consistency,
  lack of specific block references, or caveats about "infrastructure errors."
  If in doubt, state that results could not be verified.
- When you have gathered all needed results, provide a FINAL ANSWER
  by wrapping your complete answer in `<answer>` tags (no `<tool_call>`).
- `<answer>` = full-length final response (any length). All markers stripped before delivery.
- `<summary>` ≠ `<answer>`: summary is a brief memory note (≤400 chars); answer is the complete user-facing response.

---

## NUMERICAL GROUNDING (MANDATORY)

Applies to every number you emit: data values, compositions, temperatures,
pressures, uncertainties, counts, and aggregates.

- Copy numeric values VERBATIM from subagent results. Never quote more
  decimal places than the source shows. Chemistry knowledge may guide
  interpretation — it must NEVER supply a numeric value.
- If row-level data were never returned, present only the tool-returned
  aggregates, explicitly labeled as aggregates. NEVER reconstruct the
  individual rows behind an aggregate (n, min, max, mean, range) — a data
  table you assemble yourself from ranges is fabrication.
- Fabrication tells (all forbidden): compositions on a smooth grid (0.1,
  0.2, 0.3, …) that no subagent returned; "representative values" absent
  from every subagent result; agreement/comparison percentages nobody
  computed; a table whose own min/max/mean contradict the reported
  aggregates.
- Derived numbers (excess values, deviations, averages) are allowed only
  when computed from subagent-returned inputs — name those inputs and their
  source blocks beside the derived value.
- Tool results arrive ONLY from the environment after `<wait/>`. If a batch
  is rejected or errors, NO result exists — never write, quote, or continue
  from an imagined tool_result block.
- An honest "row-level values were not retrieved" is a valid answer. An
  invented number is a critical failure that invalidates the whole session.
- INSPECTION MANDATE: subagent envelopes carry `data_inspections` —
  verbatim inspected data tables; quote data points only from them or
  from subagent answers verbatim. To cite a sub-block nobody inspected,
  run `inspect_block_table` via the tool menu (`where=`/`nearest=`).
  A deterministic gate bounces answers whose block-anchored values lack a
  matching inspection in THIS session; under [TIME WARNING] drop
  uninspected points and keep aggregates.
- Chemical insights must stay grounded in the data you present: a
  comparative claim (higher/lower than a baseline or average) must hold
  arithmetically for the values quoted in your answer — otherwise keep
  the insight qualitative.
- Upstream results may carry UNVERIFIED flags. If a flagged value matters
  for your task, resolve it first (re-inspect / re-query its block anchor);
  otherwise treat it with caution under these same rules — never repeat an
  unverified number as verified.

---

## Final Answer Format

When all subagent work is done, wrap your complete answer in `<answer>` tags:

```
<answer>
[Your synthesized scientific answer here — any length.
Include all key data, DOIs, block numbers, compound names.
Every number must come from a subagent result.]

### Sources
- Literature ID: GLOBlit_N | DOI: ... | Block: ... | Subsystem: declared or BLKsubsys_N | System: ...
</answer>
```

# Phases

## phase_1: choose_route
tools: [browse_subagent_tools, run_subagent_tool]
guidance: |
  Decide whether the question needs a targeted lower-level operation or a
  full expert subagent. Browse the hierarchical menu only when direct tool
  execution is likely to be more efficient than expert delegation.

## phase_2: delegate_or_execute
tools: [run_query_agent, run_analysis_agent, run_parallel_subagents, run_subagent_tool]
guidance: |
  Supply every argument in the injected callable signature. Use one expert
  for a single complex task and run_parallel_subagents for independent query
  or analysis tasks. Preserve exact subagent identifiers and evidence.
  Oversized parallel batch results are auto-compacted; full results stay
  in working memory.

## phase_3: synthesize
tools: [list_session_files]
guidance: |
  Synthesize only tool-returned chemistry and numbers. Wrap the complete
  answer in <answer> tags; post-answer workers build the JSON fields.

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
- browse_subagent_tools(purpose, tasks) — Browse the tool menu and get a recommended execution plan.
- list_session_files() — Return a manifest of all output files generated in this session.
- run_analysis_agent(question, context, purpose, tasks) — Run the ThermoML Analysis Agent for fitting and modeling.
- run_parallel_subagents(tasks) — Run multiple query and/or analysis agent tasks in parallel.
- run_query_agent(question, context, purpose, tasks) — Run the ThermoML Query Agent on a database search question.
- run_subagent_tool(tool_name, kwargs, purpose, tasks) — Execute a subagent tool directly with full compaction pipeline.

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
**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_190212_574300_1e8b238b`

### History
- [menu:browse] {'text': 'I need to explore the available tools in the subme
- [menu:run] search_id_alignment → OK
- [menu:run] search_id_alignment → OK
- [query:Q1] "Find experimental density (mass density) data for the binary mixture of ethanol " (180s, 2 iters, validation=PASS verdict=## Verdict
The answer is scien)

### Query Agent Results

#### Q1
**Q1** — confidence: high · validation: PASS

**Answer:**

#### Experimental Mass Density of Ethanol + Water at 298.15 K, x_ethanol ≈ 0.5

Experimental mass density data for the binary mixture of **ethanol + water** near equimolar composition at 298.15 K were found in the ThermoML database.

**Source:** DOI [10.1016/j.fluid.2004.11.019](https://doi.org/10.1016/j.fluid.2004.11.019) (GLOBlit_220, block PROPblock_2)

##### Key details

- The dataset contains **810 data points** covering temperatures 298.15–348.15 K, pressures 100–40000 kPa, and ethanol mole fractions from 0.003 to 1.
- **No data point exists at exactly x_ethanol = 0.500**; the closest composition is **x_ethanol = 0.498** (the next nearest above is 0.5501).

##### Data at T = 298.15 K, x_ethanol = 0.498

| Pressure (kPa) | Mass Density (kg/m³) |
|:-:|:-:|
| 100 | 859.3 |
| 10 000 | 865.4 |
| 20 000 | 871.3 |
| 30 000 | 876.8 |
| 40 000 | 882.0 |

##### Atmospheric-pressure result

At **T = 298.15 K, P = 100 kPa, and x_ethanol = 0.498**, the mass density is **859.3 kg/m³**.

##### Chemistry context

This value sits between the densities of pure water (~997 kg/m³) and pure ethanol (~785 kg/m³) at the same temperature, but is closer to ethanol's value, reflecting the near-equimolar composition. The ethanol–water system is well known for its **negative excess volume** (volume contraction on mixing), meaning the actual mixture density is slightly higher than what a simple linear (ideal) mixing rule would predict. The systematic increase in density with pressure (859.3 → 882.0 kg/m³ over 100–40 000 kPa) is the expected isothermal compression behavior for a liquid mixture.

No uncertainty values were reported for these data points in the source block.

**Core claims:**
- Experimental mass density data for ethanol + water near equimolar composition at 298.15 K were found in the ThermoML database from DOI 10.1016/j.fluid.2004.11.019.
- The closest available ethanol mole fraction to 0.500 in the dataset is x_ethanol = 0.498.
- At T = 298.15 K, P = 100 kPa, and x_ethanol = 0.498, the mass density is 859.3 kg/m³.
- At T = 298.15 K and x_ethanol = 0.498, the mass density increases with pressure from 859.3 kg/m³ at 100 kPa to 882.0 kg/m³ at 40 000 kPa.
- No uncertainty values were reported for these data points in the source block.

**Sources:**

**WM_Q#1_Table#1_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| WM_Q#1_Table#1_Row#1 | 「GLOBlit_220」 | 「PROPblock_2」 | 「10.1016/j.fluid.2004.11.019」 | 「—」 | 「This block provides mass density data for the ethanol + water binary system covering T = 298.15–348.15 K, P = 100–40000 kPa, and ethanol mole fractions 0.003–1.0 (810 data points). It directly supports the answer's reported density of 859.3 kg/m³ at T = 298.15 K, P = 100 kPa, x_ethanol = 0.498, which falls within the block's density range of 739.4–1012.7 kg/m³.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.

</memory>

## User
I am preparing an equimolar ethanol + water liquid mixture at 25 °C and atmospheric pressure. What experimental density should I expect?

## Assistant
<summary>Searching ThermoML for density data of ethanol + water at x(ethanol) = 0.5, T = 298.15 K, atmospheric pressure.</summary>
<tool_call>run_query_agent(question=Find experimental…, context=The user wants to…)</tool_call>

## User
<tool_result>
(validation blocked run_query_agent earlier — corrected)
</tool_result>

## Assistant
<summary>Browsing subagent tools to plan an efficient search for ethanol + water density data at equimolar composition, 298.15 K, atmospheric pressure.</summary>
<tool_call>browse_subagent_tools()</tool_call>

## User
<tool_result>
(validation blocked browse_subagent_tools earlier — corrected)
</tool_result>

## Assistant
<summary>Browsing subagent tools to plan a search for ethanol + water density data at equimolar composition, 298.15 K, atmospheric pressure.</summary>
<tool_call>browse_subagent_tools()</tool_call>

## User
<tool_result>
I need to explore the available tools in the submenus before making specific recommendations. Let me map out the relevant tools.

### Recommended Plan

**Phase 1** (parallel):
- Explore `query/id_resolution` — to find compound IDs for ethanol and water
- Explore `query/block_search` — to understand how to search for density data blocks

Since I can see the submenus but not the individual tool signatures yet, here is the practical plan based on the menu structure:

---

### Recommended Plan

**Phase 1** (parallel):
- `query/id_resolution` → resolve compound names **"ethanol"** and **"water"** to their ThermoML compound IDs
- `query/block_search` → identify the appropriate block-search tool for binary mixture property data

**Phase 2** (after IDs are known):
- `query/block_search` tool for multi-component systems — search for blocks containing:
  - Both compound IDs (ethanol + water)
  - Property: **density** (mass density / molar volume)
  - Temperature near **298.15 K**
  - Composition near **mole fraction 0.5** (equimolar)

**Phase 3** (after block results):
- `analysis/discovery` — inspect retrieved blocks to extract the specific data point(s) at x ≈ 0.5 and T = 298.15 K
- `query/specialized_ranking` — optionally rank results by proximity to the target conditions if multiple sources are found

---

### Notes
- **Ethanol** (CAS 64-17-5) and **water** (CAS 7732-18-5) are well-known compounds; ID resolution should be straightforward.
- Density in ThermoML may appear as **"Mass density"** or **"Molar volume"** — both should be queried.
- Atmospheric pressure ≈ **101.325 kPa**; confirm pressure condition is applied as a filter if the block-search tool supports it.
- If exact x = 0.5 is not available, nearby compositions can be interpolated using `analysis/fitting` (e.g., RK fitting over composition range).

[WAIT BARRIER COMPLETE] 1 tool(s) finished (browse_subagent_tools). 0 deferred call(s) were discarded. Use the results above to plan your next tool calls with correct IDs/DOIs — do NOT guess.
</tool_result>

## Assistant
<summary>Resolving compound IDs for ethanol and water, then searching for density data blocks for the binary mixture near 298.15 K and x=0.5.</summary>
<tool_call>run_subagent_tool(tool_name=query/id_resolution, kwargs={'compound_name':…)</tool_call>
<tool_call>run_subagent_tool(tool_name=query/id_resolution, kwargs={'compound_name':…)</tool_call>

## User
<tool_result>
(validation blocked run_subagent_tool, run_subagent_tool earlier — corrected)
</tool_result>

## Assistant
<summary>Fixing argument types for run_subagent_tool calls to resolve ethanol and water compound IDs.</summary>
<tool_call>run_subagent_tool(tool_name=query/id_resolution, kwargs={'compound_name':…)</tool_call>
<tool_call>run_subagent_tool(tool_name=query/id_resolution, kwargs={'compound_name':…)</tool_call>

## User
<tool_result>
(validation blocked run_subagent_tool, run_subagent_tool earlier — corrected)
</tool_result>

## Assistant
<summary>Using search_id_alignment to resolve ethanol and water compound IDs in parallel.</summary>
<tool_call>run_subagent_tool(tool_name=search_id_alignment, kwargs={'query': 'ethano…)</tool_call>
<tool_call>run_subagent_tool(tool_name=search_id_alignment, kwargs={'query': 'water'…)</tool_call>

## User
<tool_result>
## Menu Tool Batch Summary

Ethanol and water both resolve to exact-match compounds in the ThermoML database.

| Compound | comp_num_id | Formula | SMILES | Score | Match |
|---|---|---|---|---|---|
| ethanol | GLOBcomp_2 | C2H6O | CCO | 100 | name_exact |
| water | GLOBcomp_1 | H2O | O | 100 | name_exact |

[WAIT BARRIER COMPLETE] 2 tool(s) finished (run_subagent_tool, run_subagent_tool). 0 deferred call(s) were discarded. Use the results above to plan your next tool calls with correct IDs/DOIs — do NOT guess.
</tool_result>

## Assistant
<summary>Ethanol=GLOBcomp_2, water=GLOBcomp_1. Now searching for density blocks of ethanol+water binary near 298.15 K and x≈0.5.</summary>
<tool_call>run_query_agent(question=Find experimental…, context=Compound IDs reso…)</tool_call>

## User
<tool_result>
(validation blocked run_query_agent earlier — corrected)
</tool_result>

## Assistant
<summary>Calling run_query_agent with all required arguments to find density data for ethanol+water binary at 298.15 K, x=0.5.</summary>
<tool_call>run_query_agent(question=Find experimental…, context=Compound IDs reso…)</tool_call>

## User
<tool_result>
<subagent_answer>
### Q#1 — run_query_agent return

**Status:** 2 iterations · 179.7s · 1 tool call(s) · agent=query
**Question:** Find experimental density (mass density) data for the binary mixture of ethanol (GLOBcomp_2) + water (GLOBcomp_1) at temperature near 298.15 K and mole fraction of ethanol near 0.5. I need specific data points with values, units, and block references.
**Session:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260815_190212_574300_1e8b238b\query_runs\run_1`

**Answer:**

#### Experimental Mass Density of Ethanol + Water at 298.15 K, x_ethanol ≈ 0.5

Experimental mass density data for the binary mixture of **ethanol + water** near equimolar composition at 298.15 K were found in the ThermoML database.

**Source:** DOI [10.1016/j.fluid.2004.11.019](https://doi.org/10.1016/j.fluid.2004.11.019) (GLOBlit_220, block PROPblock_2)

##### Key details

- The dataset contains **810 data points** covering temperatures 298.15–348.15 K, pressures 100–40000 kPa, and ethanol mole fractions from 0.003 to 1.
- **No data point exists at exactly x_ethanol = 0.500**; the closest composition is **x_ethanol = 0.498** (the next nearest above is 0.5501).

##### Data at T = 298.15 K, x_ethanol = 0.498

| Pressure (kPa) | Mass Density (kg/m³) |
|:-:|:-:|
| 100 | 859.3 |
| 10 000 | 865.4 |
| 20 000 | 871.3 |
| 30 000 | 876.8 |
| 40 000 | 882.0 |

##### Atmospheric-pressure result

At **T = 298.15 K, P = 100 kPa, and x_ethanol = 0.498**, the mass density is **859.3 kg/m³**.

##### Chemistry context

This value sits between the densities of pure water (~997 kg/m³) and pure ethanol (~785 kg/m³) at the same temperature, but is closer to ethanol's value, reflecting the near-equimolar composition. The ethanol–water system is well known for its **negative excess volume** (volume contraction on mixing), meaning the actual mixture density is slightly higher than what a simple linear (ideal) mixing rule would predict. The systematic increase in density with pressure (859.3 → 882.0 kg/m³ over 100–40 000 kPa) is the expected isothermal compression behavior for a liquid mixture.

No uncertainty values were reported for these data points in the source block.

**Core claims:**
- Experimental mass density data for ethanol + water near equimolar composition at 298.15 K were found in the ThermoML database from DOI 10.1016/j.fluid.2004.11.019.
- The closest available ethanol mole fraction to 0.500 in the dataset is x_ethanol = 0.498.
- At T = 298.15 K, P = 100 kPa, and x_ethanol = 0.498, the mass density is 859.3 kg/m³.
- At T = 298.15 K and x_ethanol = 0.498, the mass density increases with pressure from 859.3 kg/m³ at 100 kPa to 882.0 kg/m³ at 40 000 kPa.
- No uncertainty values were reported for these data points in the source block.

**Confidence:** high

**Sources:**

**Q#1_Table#1_(Main_Q#1_Sources):**

| *row_id* | *lit_num_id* | *block* | *doi* | *BLKsubsys_id* | *description* |
|---|---|---|---|---|---|
| Q#1_Table#1_Row#1 | 「GLOBlit_220」 | 「PROPblock_2」 | 「10.1016/j.fluid.2004.11.019」 | 「—」 | 「This block provides mass density data for the ethanol + water binary system covering T = 298.15–348.15 K, P = 100–40000 kPa, and ethanol mole fractions 0.003–1.0 (810 data points). It directly supports the answer's reported density of 859.3 kg/m³ at T = 298.15 K, P = 100 kPa, x_ethanol = 0.498, which falls within the block's density range of 739.4–1012.7 kg/m³.」 |

**Follow-up suggestions:**
- Retrieve excess molar volume data for ethanol+water at 298.15 K to quantify the volume contraction on mixing.
- Compare density values from other ThermoML sources for ethanol+water at x_ethanol ≈ 0.5 and 298.15 K to assess inter-laboratory consistency.
- Look up density data at exactly x_ethanol = 0.500 from alternative literature sources in ThermoML.

#### Data inspections — verbatim ledger

```ledger
**Q#1_Table#2_(Main_Q#1_INSP):**
lit_num_id: GLOBlit_220 | doi: 10.1016/j.fluid.2004.11.019 | block: PROPblock_2
table_mode: nearest | inspection_id: INSP_31ca7f6dfc0e | rows_shown: 5

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mole_fraction_<ethanol>* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| Q#1_Table#2_Row#1 | 「BLKpoint_44」 | 「298.15」 | 「100」 | 「0.498」 | 「859.3」 |
| Q#1_Table#2_Row#2 | 「BLKpoint_98」 | 「298.15」 | 「10000」 | 「0.498」 | 「865.4」 |
| Q#1_Table#2_Row#3 | 「BLKpoint_152」 | 「298.15」 | 「20000」 | 「0.498」 | 「871.3」 |
| Q#1_Table#2_Row#4 | 「BLKpoint_206」 | 「298.15」 | 「30000」 | 「0.498」 | 「876.8」 |
| Q#1_Table#2_Row#5 | 「BLKpoint_260」 | 「298.15」 | 「40000」 | 「0.498」 | 「882」 |
```

**Verdict:**

#### Verdict
The answer is scientifically plausible and well-structured, but the specific numeric density values (859.3, 865.4, 871.3, 876.8, 882.0 kg/m³) at each pressure are **UNVERIFIED** — the tool-call summary does not show individual data point retrieval, only a single L1_query returning ~10k chars. The five-point pressure table with smooth, evenly spaced density increments (~5.5–6.0 kg/m³ steps) raises concern about possible fabrication or interpolation rather than direct extraction.

#### Explanation
The source (DOI 10.1016/j.fluid.2004.11.019, Experiment of Arce et al. or similar) and block reference appear credible. The atmospheric-pressure density of ~859 kg/m³ at x_ethanol ≈ 0.5 is consistent with known literature (~855–862 kg/m³), lending plausibility. The discussion of negative excess volume is scientifically correct.

#### Numeric Grounding
All five density values and the composition x = 0.498 are **UNVERIFIED** against raw tool output. The suspiciously regular pressure-density spacing warrants caution.
</subagent_answer>

[WAIT BARRIER COMPLETE] 1 tool(s) finished (run_query_agent). 0 deferred call(s) were discarded. Use the results above to plan your next tool calls with correct IDs/DOIs — do NOT guess.
</tool_result>

## LLM Response


<reasoning>
The query agent returned data with a verbatim data inspection ledger (INSP_31ca7f6dfc0e) showing 5 rows from PROPblock_2 of GLOBlit_220. The inspection confirms the data points at T=298.15 K, x_ethanol=0.498, with mass density values at various pressures. The atmospheric pressure point (P=100 kPa) shows 859.3 kg/m³.

The verdict flags the values as "UNVERIFIED" due to smooth spacing, but the data inspection ledger IS the verbatim evidence — the rows come directly from the database with specific BLKpoint_ids. The inspection table confirms these are actual database entries, not interpolated values. The regular spacing in density with pressure is physically expected for isothermal compression of a liquid.

I have enough information to answer the user's question. The key data point is:
- At T = 298.15 K, P = 100 kPa (≈ atmospheric), x_ethanol = 0.498, mass density = 859.3 kg/m³

This comes from a verified data inspection of PROPblock_2 in GLOBlit_220 (DOI: 10.1016/j.fluid.2004.11.019).

Let me provide the final answer.
</reasoning>

<summary>
Query agent found ethanol+water density data in GLOBlit_220/PROPblock_2 (DOI 10.1016/j.fluid.2004.11.019). At T=298.15 K, P=100 kPa, x_ethanol=0.498 (closest to 0.5), mass density = 859.3 kg/m³. Verbatim inspection confirms 5 data points at this composition across pressures. Ready to deliver final answer.
</summary>

<answer>
## Experimental Density of an Equimolar Ethanol + Water Mixture at 25 °C and Atmospheric Pressure

Based on data retrieved from the ThermoML database, you should expect a mass density of approximately **859.3 kg/m³** for your equimolar ethanol + water mixture at 25 °C (298.15 K) and atmospheric pressure (100 kPa).

### Data Details

The closest available composition to an exact equimolar mixture (x_ethanol = 0.500) in the dataset is **x_ethanol = 0.498**, which is essentially equimolar. The specific data point is:

| Temperature (K) | Pressure (kPa) | x_ethanol | Mass Density (kg/m³) |
|:---:|:---:|:---:|:---:|
| 298.15 | 100 | 0.498 | 859.3 |

This value comes from a comprehensive dataset containing 810 data points spanning temperatures of 298.15–348.15 K, pressures of 100–40 000 kPa, and ethanol mole fractions from 0.003 to 1.0. No uncertainty values were reported for these measurements in the source.

### Chemistry Context

The measured density of 859.3 kg/m³ falls between the pure-component densities of water (~997 kg/m³) and ethanol (~785 kg/m³) at the same temperature, but sits closer to ethanol's value, consistent with the near-equimolar composition. Notably, the ethanol–water system exhibits a well-known **negative excess volume** (volume contraction upon mixing), meaning the mixture is slightly denser than what a simple linear (ideal) mixing rule would predict. A naïve ideal-mixing estimate would give roughly 891 kg/m³ (the mole-fraction-weighted average of pure-component densities), but the actual value of 859.3 kg/m³ reflects the non-ideal volumetric behavior of this system — specifically, the strong hydrogen-bonding interactions between ethanol and water molecules that lead to more efficient molecular packing compared to the pure liquids.

### Source

- **Literature ID:** GLOBlit_220 | **DOI:** 10.1016/j.fluid.2004.11.019 | **Block:** PROPblock_2 | **Data point:** BLKpoint_44
</answer>