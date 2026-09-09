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
**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_050055_271432_708d49b4`

### History
- [menu:browse] {'text': 'I need to explore the `query/id_resolution` submen
- [menu:run] search_id_alignment → OK
- [menu:run] search_id_alignment → OK
- [menu:run] search_id_alignment → OK
- [menu:run] search_id_alignment → OK
</memory>

## User
I am combining aqueous-alcohol measurements reported under the names “ethanol,” “ethyl alcohol,” “water,” and “aqua.” Before I compare the measurements, which canonical ThermoML compounds do these names refer to?

## Assistant
<summary>Need to resolve four common names ("ethanol", "ethyl alcohol", "water", "aqua") to their canonical ThermoML compound identifiers. Will browse tools first to find the compound resolution capability.</summary>
<tool_call>browse_subagent_tools()</tool_call>

## User
<tool_result>
(validation blocked browse_subagent_tools earlier — corrected)
</tool_result>

## Assistant
<summary>Browsing subagent tools to find the compound name resolution capability for "ethanol", "ethyl alcohol", "water", and "aqua".</summary>
<tool_call>browse_subagent_tools()</tool_call>

## User
<tool_result>
I need to explore the `query/id_resolution` submenu to find the right tools for resolving compound names.

### Recommended Plan

**Phase 1** (parallel):
- `query/id_resolution` — Explore the id_resolution submenu to identify available tools for name-to-ID resolution

*(Note: Since I can only see the submenu label but not the individual tools yet, I need to drill into the submenu first.)*

---

Let me provide a more actionable plan based on what's clearly available:

### Recommended Plan

**Phase 1** (parallel):
- `query/id_resolution(query="ethanol")` — Resolve 'ethanol' to its canonical ThermoML compound ID, CAS, formula, and metadata
- `query/id_resolution(query="ethyl alcohol")` — Resolve synonym 'ethyl alcohol' to check if it maps to the same compound as 'ethanol'
- `query/id_resolution(query="water")` — Resolve 'water' to its canonical ThermoML compound ID and metadata
- `query/id_resolution(query="aqua")` — Resolve synonym 'aqua' to check if it maps to the same compound as 'water'

### Notes
- **Synonym collapsing**: 'ethanol' and 'ethyl alcohol' are expected to resolve to the same canonical ID (CAS 64-17-5); similarly 'water' and 'aqua' should map to the same entry (CAS 7732-18-5). The results should confirm this.
- **Fallback**: If `query/id_resolution` does not support free-text name queries directly, consider using `query/compound_similarity` as an alternative for fuzzy/synonym matching.
- **Metadata**: Request CAS number, molecular formula, and any aliases returned by the tool to fully satisfy the task requirements.
- Drill into `query/id_resolution` submenu first if the tool requires a more specific sub-tool name before executing the parallel calls above.
</tool_result>

## Assistant
<summary>Running four parallel compound name resolutions for "ethanol", "ethyl alcohol", "water", and "aqua" using the id_resolution tool.</summary>
<tool_call>run_subagent_tool(tool_name=query/id_resolution, kwargs={'query': 'ethanol'})</tool_call>

## User
<tool_result>
(validation blocked run_subagent_tool earlier — corrected)
</tool_result>

## Assistant
<summary>Using `search_id_alignment` to resolve all four compound names ("ethanol", "ethyl alcohol", "water", "aqua") against the ThermoML compound registry in parallel.</summary>
<tool_call>run_subagent_tool(tool_name=search_id_alignment, kwargs={'query': 'ethano…)</tool_call>

## User
<tool_result>
**Summary:** Ethanol resolves to a single canonical compound with an exact name match.

| comp_num_id | Name | Formula | SMILES | Score | Match |
|---|---|---|---|---|---|
| GLOBcomp_2 | ethanol | C2H6O | CCO | 100 | name_exact |
</tool_result>

## Assistant
<summary>Ethanol → GLOBcomp_2 (exact match). Now resolving "ethyl alcohol", "water", and "aqua" in parallel.</summary>
<tool_call>run_subagent_tool(tool_name=search_id_alignment, kwargs={'query': 'ethyl …)</tool_call>

## User
<tool_result>
(validation blocked run_subagent_tool earlier — corrected)
</tool_result>

## Assistant
<summary>Need to include entity_type="compound" in the search_id_alignment calls. Running three parallel lookups for "ethyl alcohol", "water", and "aqua".</summary>
<tool_call>run_subagent_tool(tool_name=search_id_alignment, kwargs={'entity_type': '…)</tool_call>

## User
<tool_result>
**Summary:** 'Ethyl alcohol' resolves to **GLOBcomp_2** (ethanol, C₂H₆O, SMILES: CCO) with a perfect score of 100 via exact name match. It is the same compound as 'ethanol'.

| Query | Resolved ID | Name | Formula | SMILES | Score | Match Type |
|---|---|---|---|---|---|---|
| ethyl alcohol | GLOBcomp_2 | ethanol | C₂H₆O | CCO | 100 | name_exact |
</tool_result>

## Assistant
(syntax-rejected turn — malformed tool calls never executed; corrected on a later turn. Full detail in the run log.)

## User
(validation fired earlier — corrected)

## Assistant
<summary>Resolving "water" and "aqua" in parallel to complete the four-name resolution task. Ethanol and ethyl alcohol both map to GLOBcomp_2.</summary>
<tool_call>run_subagent_tool(tool_name=search_id_alignment, kwargs={'entity_type': '…)</tool_call>

## User
<tool_result>
(validation blocked run_subagent_tool earlier — corrected)
</tool_result>

## Assistant
<summary>Fixing tasks parameter type (string not list) and resolving "water" and "aqua" in parallel.</summary>
<tool_call>run_subagent_tool(tool_name=search_id_alignment, kwargs={'entity_type': '…)</tool_call>

## User
<tool_result>
**Water** resolves to a single exact-match compound in the ThermoML database.

| comp_num_id | Name | Formula | SMILES | Score | Match |
|---|---|---|---|---|---|
| GLOBcomp_1 | water | H2O | O | 100 | name_exact |
</tool_result>

## Assistant
<summary>Water → GLOBcomp_1 (exact match). Now resolving "aqua" to complete the set.</summary>
<tool_call>run_subagent_tool(tool_name=search_id_alignment, kwargs={'entity_type': '…)</tool_call>

## User
<tool_result>
**Summary:** The name **'aqua'** does **not** resolve to water (GLOBcomp_1) in ThermoML. All 8 results are fuzzy matches to complex coordination compounds containing "aqua" as a substring (e.g., "diaquabis…", "triaqua…"). None correspond to the simple compound water.

| Query | Resolved? | Maps to GLOBcomp_1 (water)? | Notes |
|-------|-----------|----------------------------|-------|
| `aqua` | No exact match | **No** | Only fuzzy hits to metal-aqua complexes (score 85, all `name_fuzzy`) |

**Conclusion:** To reference water, use the canonical name **'water'** (GLOBcomp_1) directly. The Latin name 'aqua' is not indexed as a standalone compound in ThermoML.
</tool_result>

## LLM Response
<answer>
Here is how the four names you mentioned map to canonical ThermoML compounds:

| Your name | Canonical ThermoML ID | Canonical name | Formula | SMILES | Match quality |
|---|---|---|---|---|---|
| **ethanol** | **GLOBcomp_2** | ethanol | C₂H₆O | CCO | Exact (score 100) |
| **ethyl alcohol** | **GLOBcomp_2** | ethanol | C₂H₆O | CCO | Exact (score 100) |
| **water** | **GLOBcomp_1** | water | H₂O | O | Exact (score 100) |
| **aqua** | — (no match) | — | — | — | No exact match found |

### Key findings

1. **"Ethanol" and "ethyl alcohol"** both resolve to the same canonical compound, **GLOBcomp_2** (ethanol, C₂H₆O). You can safely merge measurements reported under either name.

2. **"Water"** resolves to **GLOBcomp_1** (water, H₂O) with a perfect exact-name match.

3. **"Aqua"** does **not** resolve to water in ThermoML. The only hits returned are fuzzy matches (score 85) to metal–aqua coordination complexes (e.g., "diaquabis…", "triaqua…") that contain "aqua" as a substring. The Latin name "aqua" is not indexed as a standalone compound synonym for water in the ThermoML database.

### Recommendation

Before combining your datasets, re-label any measurements tagged "aqua" under the canonical name **water (GLOBcomp_1)** manually — the database will not do this mapping for you automatically. For the ethanol side, both "ethanol" and "ethyl alcohol" are safe to merge directly since they share the same canonical identifier (GLOBcomp_2).
</answer>