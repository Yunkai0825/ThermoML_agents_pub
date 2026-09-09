## System Prompt
# ThermoML Analysis Agent

You are the ThermoML Analysis Agent — a thermodynamic data fitting specialist.

You access the NIST ThermoML database (~170K data blocks) via the ThermoML
query agent and deterministic data tools.  Your job: identify systems, fit
Redlich-Kister polynomials, report results.

**Chemistry-context hint:** When useful and tool-supported, use existing output fields to add a brief chemistry insight and one or a few representative data points with values, units, conditions, compounds, and DOI/block provenance. Mark inference, never invent data, and delegation-only roles should preserve rather than create this context.

You do NOT have direct access to the ThermoML databases.  Instead you:
1. **Dispatch** queries to the ThermoML query agent via L1 workers.
2. **Inspect** returned blocks with deterministic tools (inspect_block, get_pure_values).
3. **Fit** thermodynamic data with Redlich-Kister tools.
4. **Report** results with full numerical detail.

## MANDATORY OUTPUT FORMAT

Every response with tool calls MUST use this exact structure due to automated parsing:

<reasoning>
... your thinking/planning (DISCARDED from memory after tool execution) ...
</reasoning>
<summary>
... 1-3 sentence actionable conclusion (KEPT in memory, max 400 chars) ...
</summary>
<tool_call>{"name": "query_thermoml", "arguments": {"purpose": "...", "instruction": "..."}}</tool_call>
<wait/>

CRITICAL ORDERING: <tool_call> blocks MUST come AFTER </summary> and BEFORE <wait/>.
Tool calls AFTER <wait/> are DISCARDED. Tool calls BEFORE </summary> are NOT detected.
The <reasoning> block is STRIPPED from conversation history after each turn.
Only <summary> text + <tool_call> blocks persist in memory.
For final answers (no tool calls): wrap in <answer>...</answer> tags (any length).
<summary> ≠ <answer>: summary is a brief memory note (≤400 chars); answer is the full response.

## ANTI-HALLUCINATION RULE
EVERY number you report MUST come from a tool call. No fit_block called = no results.
DO NOT answer until fitting is complete.

## NUMERICAL GROUNDING (MANDATORY)

- Data rows (x, y pairs), pure-component values, and fit outputs (RK
  coefficients, R², RMSE, BIC) may ONLY be quoted from tool results
  delivered in THIS session — verbatim, at source precision.
- If fitting tools fail, report the failure and stop the fit narrative.
  NEVER supply substitute coefficients, fit statistics, comparison tables,
  or output file names for a fit that no tool returned.
- inspect_block reports column RANGES, not rows. Knowing n, min, and max
  does NOT license writing the rows in between: interpolated or smooth-grid
  compositions (0.1, 0.2, …) that no tool returned are fabrication.
- Derived values (excess properties, deviations, baselines) only from
  tool-returned inputs; state the inputs and their source blocks next to
  each derived value.
- Tool results arrive ONLY from the environment after `<wait/>`. A rejected
  or errored call has NO result — never write or imagine a tool_result
  block; anything you "remember" from one is fabricated.
- Reporting "rows not retrieved / fit not achieved" honestly is a valid,
  passing outcome. An invented number invalidates the whole session.
- INSPECTION MANDATE: `inspect_block` shows structure; `inspect_block_table`
  shows the actual rows. Before quoting any data point, inspect that exact
  sub-block (`where=`/`nearest=`) and quote ONLY its shown rows or stats.
  A deterministic gate bounces answers whose block-anchored values lack a
  matching inspection in THIS run (fit-tool outputs are exempt — they are
  their own grounded rail); under [TIME WARNING] drop uninspected points
  and keep aggregates. Child query envelopes carry `data_inspections` —
  those tables are already grounded and reusable.
- Write plain markdown tables; delivery hardcode auto-enriches every answer
  table with a leading row-id column and a hardcoded table identifier (e.g.
  `A#1_Table#2_Row#3`), so never invent such ids — and keep existing ids
  verbatim when quoting an upstream table.
- Chemical insights must stay grounded in the data you present: a
  comparative claim (higher/lower than a baseline or average) must hold
  arithmetically for the values quoted in your answer — otherwise keep
  the insight qualitative.
- Upstream results may carry UNVERIFIED flags. If a flagged value matters
  for your task, resolve it first (re-inspect / re-query its block anchor);
  otherwise treat it with caution under these same rules — never repeat an
  unverified number as verified.

## Tool Interface
Results are markdown tables — use them directly, don't re-request.

## Rules
1. Use query_thermoml first to find compound/property IDs and data blocks.
2. Every `*_num_id` is an opaque typed global string (`GLOBcomp_N`,
   `GLOBprop_N`, `GLOBvar_N`, `GLOBconstr_N`, `GLOBmeas_N`, `GLOBphase_N`,
   `GLOBlit_N`, `GLOBsolvent_N`, `GLOBblocktype_N`, `GLOBrxntype_N`). DOI
   compound occurrences are `DOIcomp_N`; block declarations are `BLKprop_N`,
   `BLKvar_N`, and `BLKconstr_N`; block IDs are `PROPblock_N` or
   `RXNblock_N`; embedded composition-subsystem IDs are `BLKsubsys_N`.
   Reject legacy IDs and bare numbers; never normalize them. A block target is
   identified by `(doi, block_number)` for the declared parent; add the exact
   recorded `BLKsubsys_id` only when selecting an embedded subsystem.
3. inspect_block to verify columns; get_pure_values for endpoints. Omit
   `BLKsubsys_id` for the parent and pass it only for an explicit subsystem.
4. Viscosity: property_type="viscosity" (Arrhenius mixing rule).
5. Report RK coefficients, R², RMSE, BIC-selected order.
6. Ternary: decompose into binary pairs, fit_multi_system.
7. Data < 5 mixture points: report limitation.
8. NEVER fabricate. Only report tool-returned numbers.
9. Include DOIs, block numbers, T, data point counts.
   `GLOBlit_N` is the authoritative literature identifier — prefer it when
   passing sources between tools and subagents; a DOI is coupled display
   metadata. Every real DOI must be accompanied by its tool-returned
   `GLOBlit_N` `lit_num_id`; never emit an unpaired or remembered DOI —
   final answers citing DOIs no tool coupled to a `GLOBlit_N` are scrubbed
   as unverifiable. Agent-built `agentblock/` sources carry
   `lit_num_id: null`.
10. Semicolons for multi-value strings (commas in chemical names).
11. register_custom_block is a LAST-RESORT fallback: use it ONLY after
    query_thermoml shows NO usable blocks for the compounds + property
    (the tool refuses otherwise). Estimated numbers are allowed but MUST
    carry a solid `basis` justification and `citations` to real ThermoML
    DOIs they derive from. Every result obtained from an `agentblock/`
    pseudo-DOI MUST be flagged AGENT-BUILT (estimated, not experimental)
    in the final answer.
12. DATA-PRIORITY LADDER (measurements first, always). When a derived or
    excess quantity is requested, search and use in this order — a lower
    rung is allowed ONLY when every higher rung has no data for the
    system + state, and you must state which rung you used:
    - DP0: directly measured excess data (e.g. GLOBprop_17 Hᴱ, excess molar
      volume blocks) — RK-fit as-is; the fit IS the representation.
    - DP1: directly measured total mixture property (molar volume,
      viscosity, density curves) — RK-fit the measured curve; endpoints
      from the same block's own edge rows at the same state.
    - DP2: exact pointwise transform of measured mixture data —
      fit_block_derived (e.g. measured ρ(x) → V_m(x) → true Vᴱ via
      exact V_m=(x₁M₁+x₂M₂)/ρ). Still measurement-grade.
    - DP3 (FALLBACK ONLY): anything composed from pure-component values
      (ideal-baseline estimates, binary→ternary combination). Label it
      an ESTIMATE; never core claim an "excess" from it — excess is undefined
      without mixture measurements.
    Never use pure-component values as an approximation when mixture
    measurements exist. For density questions about packing/Vᴱ, use
    DP0/DP2 — Δρ vs a linear baseline is a deviation function, not Vᴱ.
12a. PROPERTY RESPONSE GATE. `inspect_block` reports the PCS mathematical
    presentation of every property (`X`, `X-X(ref)`, `X/X(ref)`, or relative
    difference); its displayed range is the REPORTED column, not a silently
    converted value. `propose_fitting_plan` says whether the declared response
    has a deterministic semantic route, but reference availability is verified
    only during execution. `get_pure_values`, `fit_block`, composition bridges,
    and `fit_block_derived` deterministically materialize the absolute property
    before endpoint extraction, baselines, exact transforms, or fitting, and
    return the equation plus reference provenance. For a relative response,
    constrain one temperature/pressure state; if evidence is missing,
    ambiguous, or unsupported, refine the source/state instead of treating the
    reported numbers as absolute. Never calculate or invent X(ref) in text.
13. COMPOSITION BASES. All fits are performed in MOLE FRACTION (molar
    excess functions are defined on it). Blocks reported on other bases
    (mass fraction, molality, mass/amount ratio) are converted EXACTLY
    and automatically inside fit_block (annotated in the result).
    Molarity / volume-fraction / mass-concentration blocks need a
    density bridge. When the survey shows ANY non-mole basis for your
    system, run align_compositions ONCE per system+state: it dispatches
    a COMPOSITION ALIGNMENT L1 agent (a chemist reviewer) that surveys
    ALL literature blocks, deduplicates sources, and chooses a
    literature source PER DEGREE OF FREEDOM of the mapping — the two
    pure density endpoints (DoF-2) and the mixture excess shape
    (DoF-3); molar masses (DoF-1) come from block formulas. The
    assembler pins the endpoints, refits the shape, physically
    validates ρ(x) on the full grid (falling back to the agent's ranked
    alternates if a source fails), and derives everything else —
    estimates are last-resort, artifact-backed, and flagged. The result
    includes a STANDARD COMPOSITION DATA SHEET (translation table CSV,
    every convertible basis with per-column relation + source). Then:
    - If the question itself asks for density/molar volume, the
      library's measured bridge fit IS the answer — do NOT refit;
      report it (predict_from_rk for specific compositions).
    - Otherwise fit the target property normally; the basis gate
      converts axes via the library automatically.
    - Alignment NEVER blocks: if it fails, mole-fraction and
      exact-basis fits still proceed (molar masses come from block
      formulas inside fit_block).
    Always report which basis the source data used, the conversion
    route applied, and cite the bridge DOI (or the estimate flag).

Common property IDs (for reference when building query instructions):

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

# Tools

## query_delegation
- query_thermoml(purpose, instruction="", id_catalog=None, context="") — send a DB query to the ThermoML query agent; `id_catalog` is a native array of strict ID objects
- query_thermoml_parallel(queries) — send a native array of exact `{label, purpose, instruction, id_catalog, context}` query objects in parallel
- align_compositions(system, state=None, instruction="", purpose="") — dispatch the composition-alignment L1 agent. `system` is a two-name array and `state` is a JSON object such as `{"temperature_k": 298.15, "pressure_kpa": 100}`.

## discovery
- inspect_block(doi, block_number, BLKsubsys_id=None, property_filter="") — inspect exact target columns, value ranges, row count (deterministic)
- get_pure_values(doi, block_number, property_hint, BLKsubsys_id=None, composition_hint="", edge_threshold=0.02) — extract endpoint values from the exact target

## custom_data
- register_custom_block(label, csv_text, compounds, property_name, basis, citations, temperature_range=None) — register an explicitly agent-built block only when the DB has no data. `compounds` is a string array; `citations` is an array of `{doi, block_number?}` objects; `temperature_range` is a two-number array.

## fitting
- fit_block(doi, block_number, BLKsubsys_id=None, property_hint="", property_type="", component_names=None, composition_hint="mole_fraction", max_rk_order=5, mixing_rule="", x_vars=None, y_props=None, x_vars_constrained=None, properties=None, pure_values=None, temperature_tolerance=0.5) — native structured fitting interface; all block IDs are typed
- fit_block_derived(doi, block_number, BLKsubsys_id=None, transform="density_to_molar_volume", property_hint="", composition_hint="mole_fraction", x_vars=None, y_props=None, x_vars_constrained=None, max_rk_order=5) — exact pointwise transform then RK fit
- fit_multi_system(systems) — parallel fits from a native array of exact system objects; each requires `label`, `doi`, and `block_number`; omit `BLKsubsys_id` for the parent and include exact `BLKsubsys_N` only for a selected subsystem
- propose_fitting_plan(doi, block_number, BLKsubsys_id=None, x_vars=None, y_props=None, x_vars_constrained=None, property_hint="", composition_hint="mole_fraction") — validate column and constraint selections

## fitting (deterministic prediction helpers)
- compute_ideal_baseline(pure_values, property_type, n_points=101, mixing_rule="") — `pure_values` is a component-name-to-number object
- predict_from_rk(coeffs, pure_values, property_type, n_points=101, mixing_rule="") — numeric coefficient array plus component-name-to-number object

## session
- list_session_files() — list all output files in this session

# Prompt Template

## User Question
{{purpose}}

## Working Memory
{{context}}

# Phases

## phase_1: query_database
tools: [query_delegation]
guidance: |
  Use query_thermoml to find compound/property IDs and relevant data blocks.
  Include specific compound names, property types, and constraints in the
  purpose and instruction.  For multiple independent queries, use
  query_thermoml_parallel.
  Wait for results before proceeding — do NOT guess DOIs/block numbers.

## phase_2: inspect_and_extract
tools: [discovery, custom_data]
guidance: |
  Using exact `(doi, block_number, BLKsubsys_id)` targets from query results:
  1. Call inspect_block to verify column names, value ranges, and row count.
  2. Call get_pure_values to extract pure-component endpoint values.
  These values are needed for the fitting step.
  Multiple inspect_block / get_pure_values calls can run in parallel.

  FALLBACK (only when phase_1 found NO usable blocks for a needed system):
  build a small estimated dataset and register it with register_custom_block
  — include a solid basis (how each value was estimated) and citations to the
  real DOIs the estimates derive from. Column naming must follow DB style,
  e.g. mole_fraction_<water>, viscosity_pas. Then treat the returned
  agentblock/ pseudo-DOI like any DOI (inspect_block → fit_block).

## phase_3: fit_data
tools: [fitting]
guidance: |
  With DOI, block_number, nullable BLKsubsys_id, property hints, and pure values from phase 2:
  - fit_block for single binary system at one temperature; when a block spans
    several temperatures use x_vars_constrained to pin the isotherm (fit_block
    then reports one fit per sweep value), and y_props to select the property
    when a block holds several property columns
  - fit_multi_system for multiple binary systems in parallel
  - fit_block_derived for exact derived-property fits (e.g. density → Vᴱ)
  Fitting tools handle internal data extraction — provide DOI + block_number
  + BLKsubsys_id + property_hint + property_type + pure values.
  Mixing rules: "linear" (default for density), "arrhenius" (for viscosity).

  **Variable selection:** inspect_block results include "Fitting variable guidance"
  showing exact column names.  Use these to set x_vars, y_props, and
  x_vars_constrained when the block has multiple variables or you need
  a specific isotherm/isobar.
  - x_vars: JSON list of composition columns, e.g. '["Mole fraction of ethanol"]'
  - y_props: JSON list of property columns, e.g. '["Density, kg/m3"]'
  - x_vars_constrained: JSON dict to fix conditions, e.g.
    '{"Temperature, K": {"value": 298.15, "tol": 0.5}}'
  - propose_fitting_plan: optional — validate column/constraint choices before fitting

## phase_4: assemble_answer
tools: [session]
guidance: |
  Assemble only the complete answer text from all fitting results.
  MUST include: RK coefficients, R², RMSE, BIC-selected order,
  DOIs, block numbers, temperature, data point counts.
  Any result derived from an agentblock/ pseudo-DOI MUST be labelled
  AGENT-BUILT (estimated fallback data — not experimental), with its
  basis and citations restated.
  Optionally call list_session_files to reference generated CSVs/PNGs.
  Wrap the final answer in <answer> tags.
  Do not emit JSON, core claims, fit_results objects, sources objects, or other
  schema fields. Parallel tool-free post-answer agents create the core claims and
  ID/metadata fields after this agent terminates.
  NEVER fabricate numbers — only report tool-returned values.

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
- align_compositions(system, state=None, instruction='', purpose, tasks) — Run the COMPOSITION ALIGNMENT L1 agent and assemble its verdict
- compute_ideal_baseline(pure_values, property_type, n_points=101, mixing_rule='', purpose, tasks) — Compute ideal-mixture baseline from pure component values.
- fit_block(doi, block_number, BLKsubsys_id=None, property_hint='', property_type='', component_names=None, composition_hint='mole_fraction', max_rk_order=5, mixing_rule='', x_vars=None, y_props=None, x_vars_constrained=None, properties=None, pure_values=None, temperature_tolerance=0.5, purpose, tasks) — Unified binary-mixture RK fitting from a ThermoML block.
- fit_block_derived(doi, block_number, BLKsubsys_id=None, transform='density_to_molar_volume', property_hint='', composition_hint='mole_fraction', x_vars=None, y_props=None, x_vars_constrained=None, max_rk_order=5, purpose, tasks) — Fit an EXACTLY-DERIVED property from a measured mixture block (DP2).
- fit_multi_system(systems, purpose, tasks) — Fit exact ``fit_block`` requests concurrently.
- get_pure_values(doi, block_number, property_hint, BLKsubsys_id=None, composition_hint='mole_fraction', edge_threshold=0.02, x_vars_constrained=None, purpose, tasks) — Extract pure-component property values from a ThermoML block.
- inspect_block(doi, block_number, BLKsubsys_id=None, property_filter='', purpose, tasks) — Inspect a block's structure: column names, row count, value ranges.
- list_session_files() — Return a manifest of all output files generated in this session.
- predict_from_rk(coeffs, pure_values, property_type, n_points=101, mixing_rule='', purpose, tasks) — Predict mixture property using fitted RK coefficients.
- propose_fitting_plan(doi, block_number, BLKsubsys_id=None, x_vars=None, y_props=None, x_vars_constrained=None, property_hint='', composition_hint='mole_fraction', purpose, tasks) — Validate a fitting plan against a block before calling fit_block.
- query_thermoml(purpose, instruction='', id_catalog=None, context='') — Send a database query to the ThermoML query agent.
- query_thermoml_parallel(queries) — Send multiple database queries to the ThermoML query agent in parallel.
- register_custom_block(label, csv_text, compounds, property_name, basis, citations, temperature_range=None, purpose, tasks) — Register an AGENT-BUILT data block as a fallback when the DB has no data.
- run_query_agent(question, purpose, tasks, context) — Run the ThermoML Query Agent for in-depth database exploration.
- run_query_agents_parallel(queries) — Run multiple query-agent tasks in parallel for broad exploration.

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
**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Main\run_20260905_022036_971412_4d2e842e\analysis_runs\run_1`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_1 | water | 992.08333 |
| comp | GLOBcomp_2 | ethanol | 785.7 |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_3 | pressurekpa |  |
| var | GLOBvar_2 | molefraction<ethanol> |  |

### History
- [query_thermoml]
- [inspect_block]
- [fit_block] ERROR: Requested x column 'Mole fraction of ethanol' not found in block
- [fit_block]
- [list_session_files]

### Query Results
#### query
**L1_query_1** — status: success · validation: PASS

**Summary:** Six ThermoML blocks containing mass density data for ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary mixtures near 298.15 K were identified. The most detailed block is GLOBlit_220::PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019), which contains 810 total data points spanning 298.15–348.15 K, 100–40000 kPa, and ethanol mole fractions 0.003–1, with 270 points at exactly 298.15 K. At 298.15 K and 100 kPa, density decreases monotonically from ~995.3 kg/m³ (x = 0.003) to 785.7 kg/m³ (x = 1); at 40000 kPa the corresponding values are 1012.7 and 815.7 kg/m³. Five additional blocks from DOIs 10.1016/j.jct.2018.02.022 (GLOBlit_5201::PROPblock_19), 10.1021/je060335h (GLOBlit_9006::PROPblock_1), 10.1016/j.fluid.2015.07.012 (GLOBlit_1742::PROPblock_3), 10.1016/j.fluid.2017.09.005 (GLOBlit_2092::PROPblock_3), and 10.1016/j.jct.2019.02.027 (GLOBlit_5473::PROPblock_21) were found but not inspected in detail. GLOBlit_220::PROPblock_2 is recommended as the richest dataset for this system.

**Answer:**

#### Density (Mass Density) Data for Ethanol + Water Binary Mixtures near 298.15 K

Six ethanol–water binary density blocks with mole-fraction composition variation were identified in the ThermoML database. The compounds are **ethanol** (GLOBcomp_2) and **water** (GLOBcomp_1), and the property is **mass density** (GLOBprop_1, kg/m³).

##### Summary of Blocks Found

The block_search_adv tool returned six blocks. Only **GLOBlit_220::PROPblock_2** was inspected in detail in this run; aggregate values for the other blocks were returned by the search tool but individual data points were not inspected. Below, I report only what was verified or clearly sourced.

---

##### 1. Best Block — GLOBlit_220 :: PROPblock_2

- **DOI:** 10.1016/j.fluid.2004.11.019
- **Total data points:** 810
- **Full-block temperature range:** 298.15–348.15 K
- **Full-block pressure range:** 100–40000 kPa
- **Full-block mole fraction (ethanol) range:** 0.003–1
- **Full-block density range:** 739.4–1012.7 kg/m³

**At T = 298.15 K** (270 matched rows; 25 shown by RDP sampling across 5 pressure isobars):

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *Pressure (kPa)* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「100」 | 「0.003」 | 「995.3」 |
| WM_L1#1_Table#1_Row#2 | 「100」 | 「0.2502」 | 「918.5」 |
| WM_L1#1_Table#1_Row#3 | 「100」 | 「0.4501」 | 「868.8」 |
| WM_L1#1_Table#1_Row#4 | 「100」 | 「0.6967」 | 「825.2」 |
| WM_L1#1_Table#1_Row#5 | 「100」 | 「1」 | 「785.7」 |
| WM_L1#1_Table#1_Row#6 | 「10000」 | 「0.003」 | 「999.8」 |
| WM_L1#1_Table#1_Row#7 | 「10000」 | 「0.2502」 | 「923.3」 |
| WM_L1#1_Table#1_Row#8 | 「10000」 | 「0.4501」 | 「874.7」 |
| WM_L1#1_Table#1_Row#9 | 「10000」 | 「0.6967」 | 「832.3」 |
| WM_L1#1_Table#1_Row#10 | 「10000」 | 「1」 | 「794」 |
| WM_L1#1_Table#1_Row#11 | 「20000」 | 「0.003」 | 「1004.2」 |
| WM_L1#1_Table#1_Row#12 | 「20000」 | 「0.2502」 | 「928」 |
| WM_L1#1_Table#1_Row#13 | 「20000」 | 「0.4501」 | 「880.4」 |
| WM_L1#1_Table#1_Row#14 | 「20000」 | 「0.6967」 | 「839」 |
| WM_L1#1_Table#1_Row#15 | 「20000」 | 「1」 | 「801.9」 |
| WM_L1#1_Table#1_Row#16 | 「30000」 | 「0.003」 | 「1008.5」 |
| WM_L1#1_Table#1_Row#17 | 「30000」 | 「0.2269」 | 「938.7」 |
| WM_L1#1_Table#1_Row#18 | 「30000」 | 「0.4501」 | 「885.7」 |
| WM_L1#1_Table#1_Row#19 | 「30000」 | 「0.6967」 | 「845.1」 |
| WM_L1#1_Table#1_Row#20 | 「30000」 | 「1」 | 「808.9」 |
| WM_L1#1_Table#1_Row#21 | 「40000」 | 「0.003」 | 「1012.7」 |
| WM_L1#1_Table#1_Row#22 | 「40000」 | 「0.2269」 | 「942.9」 |
| WM_L1#1_Table#1_Row#23 | 「40000」 | 「0.4501」 | 「890.8」 |
| WM_L1#1_Table#1_Row#24 | 「40000」 | 「0.6967」 | 「851」 |
| WM_L1#1_Table#1_Row#25 | 「40000」 | 「1」 | 「815.7」 |

This is the richest dataset: 810 total points spanning three temperatures, five pressures, and the full ethanol mole-fraction range (0.003–1). At 298.15 K alone there are 270 data points. The density decreases monotonically from ~995 kg/m³ (nearly pure water) to ~786 kg/m³ (pure ethanol) at atmospheric pressure, consistent with the well-known non-ideal mixing behavior of this system.

---

##### 2–5. Additional Blocks (search-level metadata only; not individually inspected)

The block_search_adv tool identified these additional blocks. Because they were not inspected with `inspect_block_table` in this run, only the search-returned block-level metadata (total point counts, composition range endpoints, and density range endpoints) is available. These values are from the search tool's aggregate output, not from direct row inspection.

**WM_L1#1_Table#2_(Analysis_L1#1_Answer):**

| *row_id* | *Rank* | *DOI* | *Literature ID* | *Block* | *Total pts* | *x range* | *ρ range (kg/m³)* | *Notes* |
|---|---|---|---|---|---|---|---|---|
| WM_L1#1_Table#2_Row#1 | 「2」 | 「10.1016/j.jct.2018.02.022」 | 「GLOBlit_5201」 | 「PROPblock_19」 | 「not inspected」 | 「0–1」 | 「not inspected」 | 「Full x range per search」 |
| WM_L1#1_Table#2_Row#2 | 「3」 | 「10.1021/je060335h」 | 「GLOBlit_9006」 | 「PROPblock_1」 | 「not inspected」 | 「0–1」 | 「not inspected」 | 「Full x range per search」 |
| WM_L1#1_Table#2_Row#3 | 「4」 | 「10.1016/j.fluid.2015.07.012」 | 「GLOBlit_1742」 | 「PROPblock_3」 | 「not inspected」 | 「not inspected–1」 | 「not inspected」 | 「Partial x range per search」 |
| WM_L1#1_Table#2_Row#4 | 「5」 | 「10.1016/j.fluid.2017.09.005」 | 「GLOBlit_2092」 | 「PROPblock_3」 | 「not inspected」 | 「0–1」 | 「not inspected」 | 「Full x range per search」 |
| WM_L1#1_Table#2_Row#5 | 「6」 | 「10.1016/j.jct.2019.02.027」 | 「GLOBlit_5473」 | 「PROPblock_21」 | 「not inspected」 | 「0–1」 | 「not inspected」 | 「Full x range per search」 |

---

##### Recommendation

**GLOBlit_220 :: PROPblock_2** (DOI: 10.1016/j.fluid.2004.11.019) is the clear top choice: it has 810 data points, covers the full ethanol mole-fraction range (0.003–1), spans multiple temperatures (298.15–348.15 K) and pressures (100–40000 kPa), and provides 270 points at exactly 298.15 K. The remaining blocks (GLOBlit_5201, GLOBlit_9006, GLOBlit_1742, GLOBlit_2092, GLOBlit_5473) also cover the ethanol–water binary system with mole-fraction variation but were not inspected in detail during this run.

**Core claims:**
- Six ethanol–water binary density blocks with mole-fraction composition variation were identified in the ThermoML database; the richest is GLOBlit_220::PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019) with 810 total data points spanning 298.15–348.15 K, 100–40000 kPa, and ethanol mole fractions 0.003–1.
- At 298.15 K and 100 kPa, the mass density in GLOBlit_220::PROPblock_2 decreases monotonically from ~995.3 kg/m³ at x(ethanol) = 0.003 to ~785.7 kg/m³ at x(ethanol) = 1.
- At 298.15 K, increasing pressure from 100 to 40000 kPa increases the density at each composition; for example, pure ethanol density rises from 785.7 kg/m³ (100 kPa) to 815.7 kg/m³ (40000 kPa), and near-pure water density rises from 995.3 kg/m³ to 1012.7 kg/m³.
- Five additional ethanol–water density blocks were identified (GLOBlit_5201, GLOBlit_9006, GLOBlit_1742, GLOBlit_2092, GLOBlit_5473) but were not inspected at the individual data-point level, so their detailed content remains unverified.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#3 | 「GLOBlit_220」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of ethanol + water binary mixture; 810 points; T 298.15–348.15 K; P 100–40000 kPa; x(ethanol) 0.003–1; ρ 739.4–1012.7 kg/m³. At 298.15 K: 270 points spanning full composition range.」 |
| WM_L1#1_Table#4 | 「GLOBlit_5201」 | 「PROPblock_19」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of ethanol + water binary mixture; full x range 0–1; not inspected in detail.」 |
| WM_L1#1_Table#5 | 「GLOBlit_9006」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of ethanol + water binary mixture; full x range 0–1; not inspected in detail.」 |
| WM_L1#1_Table#6 | 「GLOBlit_1742」 | 「PROPblock_3」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of ethanol + water binary mixture; partial x range; not inspected in detail.」 |
| WM_L1#1_Table#7 | 「GLOBlit_2092」 | 「PROPblock_3」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of ethanol + water binary mixture; full x range 0–1; not inspected in detail.」 |
| WM_L1#1_Table#8 | 「GLOBlit_5473」 | 「PROPblock_21」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of ethanol + water binary mixture; full x range 0–1; not inspected in detail.」 |

*Not stored here: 1 verbatim data_inspections table(s); 3 core_id_update(s) already applied to the ID catalog. Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_220 | 10.1016/j.fluid.2004.11.019 | PROPblock_2: 810 rows; x=['mole_fraction_<ethanol>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3

### Completed Fits
  - 10.1016/j.fluid.2004.11.019/PROPblock_2 (ethanol, water): RK order=3, R²=0.997283, RMSE=0.47476545853553287, coeffs=[-120.55681, 18.567625, 43.919128, -31.350563]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      pure refs: ethanol=785.7, water=992.083 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv` — RK fit data — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv` — Excess property — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1

### plot
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png` — RK fit plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png` — Excess plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1

</memory>

## User
[Purpose: Obtain a Redlich-Kister correlation for density of ethanol+water mixtures at 25°C]
Fit a Redlich-Kister polynomial to the density of liquid ethanol + water at 25°C (298.15 K) as a function of ethanol mole fraction. Report the fitted equation, polynomial order, coefficients with units, R², RMSE, and composition range.

[Context: The user wants density (kg/m³ or g/cm³) of ethanol+water liquid mixtures at 25°C. Search for ThermoML data covering this binary system, then fit a Redlich-Kister polynomial to the excess or total density. Ethanol = C2H5OH, Water = H2O. Report all fitting details.]

## Assistant
<summary>Starting Phase 1: Querying ThermoML for density data of ethanol + water binary mixtures at 298.15 K.</summary>
<tool_call>query_thermoml(instruction=Search for blocks…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — query_thermoml return

**Status:** status=success

**Summary:** Six ThermoML blocks containing mass density data for ethanol (GLOBcomp_2) + water (GLOBcomp_1) binary mixtures near 298.15 K were identified. The most detailed block is GLOBlit_220::PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019), which contains 810 total data points spanning 298.15–348.15 K, 100–40000 kPa, and ethanol mole fractions 0.003–1, with 270 points at exactly 298.15 K. At 298.15 K and 100 kPa, density decreases monotonically from ~995.3 kg/m³ (x = 0.003) to 785.7 kg/m³ (x = 1); at 40000 kPa the corresponding values are 1012.7 and 815.7 kg/m³. Five additional blocks from DOIs 10.1016/j.jct.2018.02.022 (GLOBlit_5201::PROPblock_19), 10.1021/je060335h (GLOBlit_9006::PROPblock_1), 10.1016/j.fluid.2015.07.012 (GLOBlit_1742::PROPblock_3), 10.1016/j.fluid.2017.09.005 (GLOBlit_2092::PROPblock_3), and 10.1016/j.jct.2019.02.027 (GLOBlit_5473::PROPblock_21) were found but not inspected in detail. GLOBlit_220::PROPblock_2 is recommended as the richest dataset for this system.

**Answer:**

#### Density (Mass Density) Data for Ethanol + Water Binary Mixtures near 298.15 K

Six ethanol–water binary density blocks with mole-fraction composition variation were identified in the ThermoML database. The compounds are **ethanol** (GLOBcomp_2) and **water** (GLOBcomp_1), and the property is **mass density** (GLOBprop_1, kg/m³).

##### Summary of Blocks Found

The block_search_adv tool returned six blocks. Only **GLOBlit_220::PROPblock_2** was inspected in detail in this run; aggregate values for the other blocks were returned by the search tool but individual data points were not inspected. Below, I report only what was verified or clearly sourced.

---

##### 1. Best Block — GLOBlit_220 :: PROPblock_2

- **DOI:** 10.1016/j.fluid.2004.11.019
- **Total data points:** 810
- **Full-block temperature range:** 298.15–348.15 K
- **Full-block pressure range:** 100–40000 kPa
- **Full-block mole fraction (ethanol) range:** 0.003–1
- **Full-block density range:** 739.4–1012.7 kg/m³

**At T = 298.15 K** (270 matched rows; 25 shown by RDP sampling across 5 pressure isobars):

**L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *Pressure (kPa)* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|---|
| L1#1_Table#1_Row#1 | 「100」 | 「0.003」 | 「995.3」 |
| L1#1_Table#1_Row#2 | 「100」 | 「0.2502」 | 「918.5」 |
| L1#1_Table#1_Row#3 | 「100」 | 「0.4501」 | 「868.8」 |
| L1#1_Table#1_Row#4 | 「100」 | 「0.6967」 | 「825.2」 |
| L1#1_Table#1_Row#5 | 「100」 | 「1」 | 「785.7」 |
| L1#1_Table#1_Row#6 | 「10000」 | 「0.003」 | 「999.8」 |
| L1#1_Table#1_Row#7 | 「10000」 | 「0.2502」 | 「923.3」 |
| L1#1_Table#1_Row#8 | 「10000」 | 「0.4501」 | 「874.7」 |
| L1#1_Table#1_Row#9 | 「10000」 | 「0.6967」 | 「832.3」 |
| L1#1_Table#1_Row#10 | 「10000」 | 「1」 | 「794」 |
| L1#1_Table#1_Row#11 | 「20000」 | 「0.003」 | 「1004.2」 |
| L1#1_Table#1_Row#12 | 「20000」 | 「0.2502」 | 「928」 |
| L1#1_Table#1_Row#13 | 「20000」 | 「0.4501」 | 「880.4」 |
| L1#1_Table#1_Row#14 | 「20000」 | 「0.6967」 | 「839」 |
| L1#1_Table#1_Row#15 | 「20000」 | 「1」 | 「801.9」 |
| L1#1_Table#1_Row#16 | 「30000」 | 「0.003」 | 「1008.5」 |
| L1#1_Table#1_Row#17 | 「30000」 | 「0.2269」 | 「938.7」 |
| L1#1_Table#1_Row#18 | 「30000」 | 「0.4501」 | 「885.7」 |
| L1#1_Table#1_Row#19 | 「30000」 | 「0.6967」 | 「845.1」 |
| L1#1_Table#1_Row#20 | 「30000」 | 「1」 | 「808.9」 |
| L1#1_Table#1_Row#21 | 「40000」 | 「0.003」 | 「1012.7」 |
| L1#1_Table#1_Row#22 | 「40000」 | 「0.2269」 | 「942.9」 |
| L1#1_Table#1_Row#23 | 「40000」 | 「0.4501」 | 「890.8」 |
| L1#1_Table#1_Row#24 | 「40000」 | 「0.6967」 | 「851」 |
| L1#1_Table#1_Row#25 | 「40000」 | 「1」 | 「815.7」 |

This is the richest dataset: 810 total points spanning three temperatures, five pressures, and the full ethanol mole-fraction range (0.003–1). At 298.15 K alone there are 270 data points. The density decreases monotonically from ~995 kg/m³ (nearly pure water) to ~786 kg/m³ (pure ethanol) at atmospheric pressure, consistent with the well-known non-ideal mixing behavior of this system.

---

##### 2–5. Additional Blocks (search-level metadata only; not individually inspected)

The block_search_adv tool identified these additional blocks. Because they were not inspected with `inspect_block_table` in this run, only the search-returned block-level metadata (total point counts, composition range endpoints, and density range endpoints) is available. These values are from the search tool's aggregate output, not from direct row inspection.

**L1#1_Table#2_(Analysis_L1#1_Answer):**

| *row_id* | *Rank* | *DOI* | *Literature ID* | *Block* | *Total pts* | *x range* | *ρ range (kg/m³)* | *Notes* |
|---|---|---|---|---|---|---|---|---|
| L1#1_Table#2_Row#1 | 「2」 | 「10.1016/j.jct.2018.02.022」 | 「GLOBlit_5201」 | 「PROPblock_19」 | 「not inspected」 | 「0–1」 | 「not inspected」 | 「Full x range per search」 |
| L1#1_Table#2_Row#2 | 「3」 | 「10.1021/je060335h」 | 「GLOBlit_9006」 | 「PROPblock_1」 | 「not inspected」 | 「0–1」 | 「not inspected」 | 「Full x range per search」 |
| L1#1_Table#2_Row#3 | 「4」 | 「10.1016/j.fluid.2015.07.012」 | 「GLOBlit_1742」 | 「PROPblock_3」 | 「not inspected」 | 「not inspected–1」 | 「not inspected」 | 「Partial x range per search」 |
| L1#1_Table#2_Row#4 | 「5」 | 「10.1016/j.fluid.2017.09.005」 | 「GLOBlit_2092」 | 「PROPblock_3」 | 「not inspected」 | 「0–1」 | 「not inspected」 | 「Full x range per search」 |
| L1#1_Table#2_Row#5 | 「6」 | 「10.1016/j.jct.2019.02.027」 | 「GLOBlit_5473」 | 「PROPblock_21」 | 「not inspected」 | 「0–1」 | 「not inspected」 | 「Full x range per search」 |

---

##### Recommendation

**GLOBlit_220 :: PROPblock_2** (DOI: 10.1016/j.fluid.2004.11.019) is the clear top choice: it has 810 data points, covers the full ethanol mole-fraction range (0.003–1), spans multiple temperatures (298.15–348.15 K) and pressures (100–40000 kPa), and provides 270 points at exactly 298.15 K. The remaining blocks (GLOBlit_5201, GLOBlit_9006, GLOBlit_1742, GLOBlit_2092, GLOBlit_5473) also cover the ethanol–water binary system with mole-fraction variation but were not inspected in detail during this run.

**Core claims:**
- Six ethanol–water binary density blocks with mole-fraction composition variation were identified in the ThermoML database; the richest is GLOBlit_220::PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019) with 810 total data points spanning 298.15–348.15 K, 100–40000 kPa, and ethanol mole fractions 0.003–1.
- At 298.15 K and 100 kPa, the mass density in GLOBlit_220::PROPblock_2 decreases monotonically from ~995.3 kg/m³ at x(ethanol) = 0.003 to ~785.7 kg/m³ at x(ethanol) = 1.
- At 298.15 K, increasing pressure from 100 to 40000 kPa increases the density at each composition; for example, pure ethanol density rises from 785.7 kg/m³ (100 kPa) to 815.7 kg/m³ (40000 kPa), and near-pure water density rises from 995.3 kg/m³ to 1012.7 kg/m³.
- Five additional ethanol–water density blocks were identified (GLOBlit_5201, GLOBlit_9006, GLOBlit_1742, GLOBlit_2092, GLOBlit_5473) but were not inspected at the individual data-point level, so their detailed content remains unverified.

**Core ID updates:**
- add GLOBcomp_1 — water (registry: water)
- add GLOBcomp_2 — ethanol (registry: ethanol)
- add GLOBprop_1 — Mass density, kg/m3 (registry: mass_density_kg_m3)

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#3_(Analysis_L1#1_CoreBLK):**
lit_num_id: GLOBlit_220 | lit_id: 2005-pec-dol-0 | doi: 10.1016/j.fluid.2004.11.019
block: PROPblock_2 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 810
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_2; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of ethanol + water binary mixture; 810 points; T 298.15–348.15 K; P 100–40000 kPa; x(ethanol) 0.003–1; ρ 739.4–1012.7 kg/m³. At 298.15 K: 270 points spanning full composition range.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#3_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=298.15–348.15 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#3_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_3」 | 「Pressure, kPa」 | 「range=100.0–40000.0 · n_unique=5 · phase=Liquid」 |
| L1#1_Table#3_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.003–1.0 · n_unique=54 · phase=Liquid」 |
| L1#1_Table#3_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:2 (GLOBmeas_138) · range=739.4–1012.7 · mean=923.644444 · n=810 · phase=Liquid」 |
```

```ledger
**L1#1_Table#4_(Analysis_L1#1_CoreBLK):**
lit_num_id: GLOBlit_5201 | lit_id: 2018-hog-tor-0 | doi: 10.1016/j.jct.2018.02.022
block: PROPblock_19 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 244
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_6; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of ethanol + water binary mixture; full x range 0–1; not inspected in detail.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#4_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=92.3 · phase=Liquid」 |
| L1#1_Table#4_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=293.15–308.15 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#4_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0–1.0 · n_unique=59 · phase=Liquid」 |
| L1#1_Table#4_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=776.592–998.429 · mean=881.16518 · n=244 · phase=Liquid」 |
```

```ledger
**L1#1_Table#5_(Analysis_L1#1_CoreBLK):**
lit_num_id: GLOBlit_9006 | lit_id: 2007-her-san-0 | doi: 10.1021/je060335h
block: PROPblock_1 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 164
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_2; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_3; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of ethanol + water binary mixture; full x range 0–1; not inspected in detail.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#5_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=101.0 · phase=Liquid」 |
| L1#1_Table#5_Row#2 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=283.15–298.15 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#5_Row#3 | 「variable」 | 「BLKvar_2/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0–1.0 · n_unique=41 · phase=Liquid」 |
| L1#1_Table#5_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=VIBTUB:UFactor:4 (GLOBmeas_134) · range=785.22–999.7 · mean=908.57689 · n=164 · phase=Liquid」 |
```

```ledger
**L1#1_Table#6_(Analysis_L1#1_CoreBLK):**
lit_num_id: GLOBlit_1742 | lit_id: 2016-ono-ame-0 | doi: 10.1016/j.fluid.2015.07.012
block: PROPblock_3 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 84
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_3; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of ethanol + water binary mixture; partial x range; not inspected in detail.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#6_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=350.7–476.2 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#6_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_3」 | 「Pressure, kPa」 | 「range=10000.0–40000.0 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#6_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.1–1.0 · n_unique=7 · phase=Liquid」 |
| L1#1_Table#6_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=582.85–945.15 · mean=793.264881 · n=84 · phase=Liquid」 |
```

```ledger
**L1#1_Table#7_(Analysis_L1#1_CoreBLK):**
lit_num_id: GLOBlit_2092 | lit_id: 2017-ono-kyo-0 | doi: 10.1016/j.fluid.2017.09.005
block: PROPblock_3 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 72
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_3; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of ethanol + water binary mixture; full x range 0–1; not inspected in detail.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#7_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_1」 | 「Temperature, K」 | 「range=523.2–618.2 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#7_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_3」 | 「Pressure, kPa」 | 「range=20000.0–40000.0 · n_unique=3 · phase=Liquid」 |
| L1#1_Table#7_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0–1.0 · n_unique=8 · phase=Liquid」 |
| L1#1_Table#7_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=250.4–834.3 · mean=569.888889 · n=72 · phase=Liquid」 |
```

```ledger
**L1#1_Table#8_(Analysis_L1#1_CoreBLK):**
lit_num_id: GLOBlit_5473 | lit_id: 2019-fol-sos-0 | doi: 10.1016/j.jct.2019.02.027
block: PROPblock_21 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 9
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_2; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_1; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density of ethanol + water binary mixture; full x range 0–1; not inspected in detail.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#8_Row#1 | 「constraint」 | 「BLKconstr_1/GLOBconstr_2」 | 「Temperature, K」 | 「value=298.15 · phase=Liquid」 |
| L1#1_Table#8_Row#2 | 「constraint」 | 「BLKconstr_2/GLOBconstr_1」 | 「Pressure, kPa」 | 「value=100.0 · phase=Liquid」 |
| L1#1_Table#8_Row#3 | 「variable」 | 「BLKvar_1/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0–1.0 · n_unique=9 · phase=Liquid」 |
| L1#1_Table#8_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Vibrating tube method (GLOBmeas_2) · range=785.5–997.1 · mean=906.744444 · n=9 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#9_(Analysis_L1#1_INSP):**
lit_num_id: GLOBlit_220 | doi: 10.1016/j.fluid.2004.11.019 | block: PROPblock_2
table_mode: rdp | inspection_id: INSP_689860323003 | rows_shown: 25

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mole_fraction_<ethanol>* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| L1#1_Table#9_Row#1 | 「BLKpoint_1」 | 「298.15」 | 「100」 | 「0.003」 | 「995.3」 |
| L1#1_Table#9_Row#2 | 「BLKpoint_38」 | 「298.15」 | 「100」 | 「0.2502」 | 「918.5」 |
| L1#1_Table#9_Row#3 | 「BLKpoint_43」 | 「298.15」 | 「100」 | 「0.4501」 | 「868.8」 |
| L1#1_Table#9_Row#4 | 「BLKpoint_48」 | 「298.15」 | 「100」 | 「0.6967」 | 「825.2」 |
| L1#1_Table#9_Row#5 | 「BLKpoint_54」 | 「298.15」 | 「100」 | 「1」 | 「785.7」 |
| L1#1_Table#9_Row#6 | 「BLKpoint_55」 | 「298.15」 | 「10000」 | 「0.003」 | 「999.8」 |
| L1#1_Table#9_Row#7 | 「BLKpoint_92」 | 「298.15」 | 「10000」 | 「0.2502」 | 「923.3」 |
| L1#1_Table#9_Row#8 | 「BLKpoint_97」 | 「298.15」 | 「10000」 | 「0.4501」 | 「874.7」 |
| L1#1_Table#9_Row#9 | 「BLKpoint_102」 | 「298.15」 | 「10000」 | 「0.6967」 | 「832.3」 |
| L1#1_Table#9_Row#10 | 「BLKpoint_108」 | 「298.15」 | 「10000」 | 「1」 | 「794」 |
| L1#1_Table#9_Row#11 | 「BLKpoint_109」 | 「298.15」 | 「20000」 | 「0.003」 | 「1004.2」 |
| L1#1_Table#9_Row#12 | 「BLKpoint_146」 | 「298.15」 | 「20000」 | 「0.2502」 | 「928」 |
| L1#1_Table#9_Row#13 | 「BLKpoint_151」 | 「298.15」 | 「20000」 | 「0.4501」 | 「880.4」 |
| L1#1_Table#9_Row#14 | 「BLKpoint_156」 | 「298.15」 | 「20000」 | 「0.6967」 | 「839」 |
| L1#1_Table#9_Row#15 | 「BLKpoint_162」 | 「298.15」 | 「20000」 | 「1」 | 「801.9」 |
| L1#1_Table#9_Row#16 | 「BLKpoint_163」 | 「298.15」 | 「30000」 | 「0.003」 | 「1008.5」 |
| L1#1_Table#9_Row#17 | 「BLKpoint_199」 | 「298.15」 | 「30000」 | 「0.2269」 | 「938.7」 |
| L1#1_Table#9_Row#18 | 「BLKpoint_205」 | 「298.15」 | 「30000」 | 「0.4501」 | 「885.7」 |
| L1#1_Table#9_Row#19 | 「BLKpoint_210」 | 「298.15」 | 「30000」 | 「0.6967」 | 「845.1」 |
| L1#1_Table#9_Row#20 | 「BLKpoint_216」 | 「298.15」 | 「30000」 | 「1」 | 「808.9」 |
| L1#1_Table#9_Row#21 | 「BLKpoint_217」 | 「298.15」 | 「40000」 | 「0.003」 | 「1012.7」 |
| L1#1_Table#9_Row#22 | 「BLKpoint_253」 | 「298.15」 | 「40000」 | 「0.2269」 | 「942.9」 |
| L1#1_Table#9_Row#23 | 「BLKpoint_259」 | 「298.15」 | 「40000」 | 「0.4501」 | 「890.8」 |
| L1#1_Table#9_Row#24 | 「BLKpoint_264」 | 「298.15」 | 「40000」 | 「0.6967」 | 「851」 |
| L1#1_Table#9_Row#25 | 「BLKpoint_270」 | 「298.15」 | 「40000」 | 「1」 | 「815.7」 |
```
</subagent_answer>
</tool_result>

## Assistant
<summary>Query found GLOBlit_220::PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019) as the richest ethanol+water density block: 810 pts, T=298.15–348.15 K, P=100–40000 kPa, x(ethanol)=0.003–1. Need to inspect block for exact column names, then fit at T=298.15 K, P=100 kPa (atmospheric). Also considering GLOBlit_9006::PROPblock_1 (P=101 kPa, 41 compositions) as a second source.</summary>
<tool_call>inspect_block(doi=10.1016/j.fluid.2004.11.019, block_number=PROPblock_2)</tool_call>

## User
<tool_result>
(validation blocked inspect_block earlier — corrected)
</tool_result>

## Assistant
<summary>Inspecting GLOBlit_220::PROPblock_2 to verify column names and structure before fitting. Also getting pure values for the endpoints.</summary>
<tool_call>inspect_block(doi=10.1016/j.fluid.2004.11.019, block_number=PROPblock_2)</tool_call>

## User
<tool_result>
(validation blocked inspect_block earlier — corrected)
</tool_result>

## Assistant
<summary>Inspecting GLOBlit_220::PROPblock_2 to get exact column names for fitting at T=298.15 K, P=100 kPa.</summary>
<tool_call>inspect_block(doi=10.1016/j.fluid.2004.11.019, block_number=PROPblock_2)</tool_call>

## User
<tool_result>
**Block GLOBlit_220 / DOI 10.1016/j.fluid.2004.11.019 / PROPblock_2 @ declared** (PureOrMixtureData)
Compounds: ethanol, water | Rows: 810
x‑columns: ['mole_fraction_<ethanol>'] | y‑columns: ['mass_density_kg_m3']

**Property response semantics (reported metadata; values are not materialized here)**
- **BLKprop_1 / GLOBprop_1** `mass_density_kg_m3` (mass_density_kg_m3)
  - reported response: Direct value, X
  - measurement: GLOBmeas_138 / vibtub_ufactor_2
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference: none; T=unspecified K; P=unspecified kPa
  - reference phase: none
  - component_org_num: none

**Selected property response contract (inspection only; values are not materialized here)**
- **BLKprop_1 / GLOBprop_1** `mass_density_kg_m3` (mass_density_kg_m3)
  - reported response: Direct value, X [direct]
  - units: reported=kg/m3; absolute=kg/m3
  - preparation gate: reference_materialization=False; normalized_composition=False; supported=True
  - reference: none; T=unspecified K; P=unspecified kPa
  - property phase: Liquid (GLOBphase_1; liquid)
  - reference phase: none
  - component_org_num: none

| Column | Min | Max | Valid pts |
|--------|-----|-----|-----------|
| temperature_k | 298.15 | 348.15 | 810 |
| pressure_kpa | 100 | 40000 | 810 |
| mole_fraction_<ethanol> | 0.003 | 1 | 810 |
| mass_density_kg_m3 | 739.4 | 1012.7 | 810 |

</tool_result>

## Assistant
<summary>Block inspected: GLOBlit_220::PROPblock_2 has columns temperature_k, pressure_kpa, mole_fraction_<ethanol>, mass_density_kg_m3. 810 rows total. Now fitting at T=298.15 K, P=100 kPa with linear mixing rule for density.</summary>
<tool_call>fit_block(doi=10.1016/j.fluid.2004.11.019, property_hint=mass_density_kg_m3, block_number…)</tool_call>

## User
<tool_result>
(validation blocked fit_block earlier — corrected)
</tool_result>

## Assistant
<summary>Fitting GLOBlit_220::PROPblock_2 at T=298.15 K, P=100 kPa using fit_block with x_vars_constrained to pin temperature and pressure, linear mixing rule for density.</summary>
<tool_call>fit_block(doi=10.1016/j.fluid.2004.11.019, property_hint=mass_density_kg_m3, block_number…)</tool_call>

## User
<tool_result>
(validation blocked fit_block earlier — corrected)
</tool_result>

## Assistant
<summary>Fitting GLOBlit_220::PROPblock_2 at T=298.15 K, P=100 kPa with linear mixing rule for density. Using x_vars_constrained to pin temperature and pressure.</summary>
<tool_call>fit_block(doi=10.1016/j.fluid.2004.11.019, property_hint=mass_density_kg_m3, block_number…)</tool_call>

## User
<tool_result>
(validation blocked fit_block earlier — corrected)
</tool_result>

## Assistant
<summary>Calling fit_block on GLOBlit_220::PROPblock_2 at T=298.15 K, P=100 kPa with linear mixing rule for density, constraining temperature and pressure.</summary>
<tool_call>fit_block(doi=10.1016/j.fluid.2004.11.019, property_hint=mass_density_kg_m3, block_number…)</tool_call>

## User
<tool_result>
**Fit error** (GLOBlit_220 / DOI 10.1016/j.fluid.2004.11.019 / PROPblock_2): Requested x column 'Mole fraction of ethanol' not found in block
Columns available: ['BLKpoint_id', 'temperature_k', 'pressure_kpa', 'mole_fraction_<ethanol>', 'mass_density_kg_m3']

</tool_result>

## Assistant
<summary>Fit failed because default x column name didn't match. The actual column is `mole_fraction_<ethanol>`. Retrying fit_block with explicit x_vars and x_vars_constrained for T=298.15 K, P=100 kPa.</summary>
<tool_call>fit_block(doi=10.1016/j.fluid.2004.11.019, property_hint=mass_density_kg_m3, block_number…)</tool_call>

## User
<tool_result>
(validation blocked fit_block earlier — corrected)
</tool_result>

## Assistant
<summary>Retrying fit_block with explicit x_vars=["mole_fraction_<ethanol>"], y_props=["mass_density_kg_m3"], x_vars_constrained for T=298.15 K and P=100 kPa, linear mixing rule.</summary>
<tool_call>fit_block(doi=10.1016/j.fluid.2004.11.019, property_hint=mass_density_kg_m3, block_number…)</tool_call>

## User
<tool_result>
(validation blocked fit_block earlier — corrected)
</tool_result>

## Assistant
<summary>Retrying fit_block with all required arguments including purpose and tasks, using explicit x_vars and x_vars_constrained to pin T=298.15 K and P=100 kPa.</summary>
<tool_call>fit_block(doi=10.1016/j.fluid.2004.11.019, property_hint=mass_density_kg_m3, block_number…)</tool_call>

## User
<tool_result>
(validation blocked fit_block earlier — corrected)
</tool_result>

## Assistant
<summary>Retrying fit_block with correct argument types: tasks as string, explicit x_vars and x_vars_constrained for T=298.15 K and P=100 kPa.</summary>
<tool_call>fit_block(doi=10.1016/j.fluid.2004.11.019, property_hint=mass_density_kg_m3, block_number…)</tool_call>

## User
<tool_result>
**RK Fit** — GLOBlit_220 / DOI 10.1016/j.fluid.2004.11.019 / PROPblock_2 @ declared
Components: ethanol, water | Mixing rule: linear
Points: 47 mixture / 810 total
Property response: BLKprop_1 / GLOBprop_1; kind=direct; equation=X = reported X; reference_sources=0; units=kg/m3 -> kg/m3.

| Component | Pure value |
|-----------|-----------|
| ethanol | 785.7 |
| water | 992.08333 |
Pure values: block-edges (water: direct/good, ethanol: direct/good)

BIC-selected order: 3 | R² = 0.997283 | RMSE = 0.474765 | BIC = -54.62
Coefficients: [-120.557, 18.5676, 43.9191, -31.3506]

| Order | BIC | R² | RMSE |
|-------|-----|----|------|
| 0 | 47.60 | 0.969419 | 1.59267 |
| 1 | 48.19 | 0.971469 | 1.53836 |
| 2 | -33.56 | 0.995383 | 0.618852 |
| 3 | -54.62 | 0.997283 | 0.474765 |
| 4 | -52.17 | 0.997362 | 0.467746 |
| 5 | -53.77 | 0.997651 | 0.441438 |

</tool_result>

## Assistant
<summary>Fit completed: GLOBlit_220::PROPblock_2 at T=298.15 K, P=100 kPa. BIC-selected RK order 3, R²=0.997283, RMSE=0.4748 kg/m³, coeffs=[-120.557, 18.5676, 43.9191, -31.3506]. Pure: ethanol=785.7, water=992.083 kg/m³. 47 mixture points. Now assembling final answer.</summary>
<tool_call>list_session_files()</tool_call>

## User
<tool_result>
{
  "session_dir": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Main\\run_20260905_022036_971412_4d2e842e\\analysis_runs\\run_1",
  "n_files": 4,
  "files": [
    {
      "category": "data",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Main\\run_20260905_022036_971412_4d2e842e\\analysis_runs\\run_1\\data\\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv",
      "description": "RK fit data \u2014 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1"
    },
    {
      "category": "data",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Main\\run_20260905_022036_971412_4d2e842e\\analysis_runs\\run_1\\data\\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv",
      "description": "Excess property \u2014 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1"
    },
    {
      "category": "plot",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Main\\run_20260905_022036_971412_4d2e842e\\analysis_runs\\run_1\\plots\\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png",
      "description": "RK fit plot \u2014 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1"
    },
    {
      "category": "plot",
      "path": "\\\\Sheldon.cse.anl.gov\\yunkai.sun$\\_Code_Maintenance\\_outputs_user\\yunkai.sun\\ThermoML\\Main\\run_20260905_022036_971412_4d2e842e\\analysis_runs\\run_1\\plots\\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png",
      "description": "Excess plot \u2014 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1"
    }
  ]
}
</tool_result>

## LLM Response
<answer>

## Redlich-Kister Correlation for Density of Ethanol + Water at 298.15 K

### Data Source

- **DOI:** 10.1016/j.fluid.2004.11.019 (GLOBlit_220)
- **Block:** PROPblock_2
- **System:** ethanol (GLOBcomp_2) + water (GLOBcomp_1), liquid phase
- **Conditions:** T = 298.15 K, P = 100 kPa (atmospheric)
- **Data points used:** 47 mixture compositions (from 810 total rows spanning multiple T and P)
- **Composition range:** x(ethanol) = 0.003 to 1.0 (mole fraction)
- **Measurement method:** Vibrating-tube densimeter (GLOBmeas_138)

### Pure-Component Densities

| Component | ρ* (kg/m³) | Source |
|-----------|-----------|--------|
| Water | 992.083 | Block edge value (direct/good) |
| Ethanol | 785.7 | Block edge value (direct/good) |

### Fitted Equation

The total density is expressed as:

$$\rho(x_1) = x_1 \, \rho_1^* + x_2 \, \rho_2^* + x_1 \, x_2 \sum_{k=0}^{n} A_k (x_1 - x_2)^k$$

where x₁ = mole fraction of ethanol, x₂ = 1 − x₁, ρ₁* = 785.7 kg/m³ (pure ethanol), ρ₂* = 992.083 kg/m³ (pure water), and the mixing rule is **linear** (appropriate for density).

### BIC-Selected Polynomial Order and Coefficients

| Parameter | Value |
|-----------|-------|
| **BIC-selected order** | **3** |
| A₀ | −120.557 kg/m³ |
| A₁ | 18.568 kg/m³ |
| A₂ | 43.919 kg/m³ |
| A₃ | −31.351 kg/m³ |
| **R²** | **0.997283** |
| **RMSE** | **0.4748 kg/m³** |
| **BIC** | **−54.62** |

### Model Selection Summary

| Order | BIC | R² | RMSE (kg/m³) |
|-------|---------|----------|------------|
| 0 | 47.60 | 0.969419 | 1.593 |
| 1 | 48.19 | 0.971469 | 1.538 |
| 2 | −33.56 | 0.995383 | 0.619 |
| 3 | **−54.62** | **0.997283** | **0.475** |
| 4 | −52.17 | 0.997362 | 0.468 |
| 5 | −53.77 | 0.997651 | 0.441 |

The BIC criterion selects order 3 as optimal — orders 4 and 5 provide negligible improvement in R² while incurring a complexity penalty.

### Chemistry Insight

The large negative A₀ coefficient (−120.6 kg/m³) reflects the well-known **volume contraction** upon mixing ethanol and water: hydrogen-bonding reorganization allows water molecules to partially fill the voids in ethanol's structure, producing a mixture denser than the mole-fraction-weighted average of the pure components. The asymmetry captured by A₁ through A₃ indicates that the maximum deviation from ideal (linear) mixing occurs at water-rich compositions (roughly x(ethanol) ≈ 0.3–0.4), consistent with the composition range where the ethanol–water hydrogen-bond network undergoes the most dramatic restructuring.

Representative data points at 298.15 K, 100 kPa (from inspected block rows):

| x(ethanol) | ρ (kg/m³) |
|------------|-----------|
| 0.003 | 995.3 |
| 0.2502 | 918.5 |
| 0.4501 | 868.8 |
| 0.6967 | 825.2 |
| 1.000 | 785.7 |

### Output Files

- **Fit data CSV:** `10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv`
- **Excess property CSV:** `10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv`
- **Fit plot:** `10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png`
- **Excess plot:** `10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png`

</answer>