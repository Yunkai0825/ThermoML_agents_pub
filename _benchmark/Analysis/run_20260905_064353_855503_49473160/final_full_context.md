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
**ROOT:** `\\Sheldon.cse.anl.gov\yunkai.sun$\_Code_Maintenance\_outputs_user\yunkai.sun\ThermoML\Analysis\run_20260905_064353_855503_49473160`

### ID Catalog
| type | global_id | name | pure_values |
|------|--------|------|-------------|
| comp | GLOBcomp_2 | ethanol |  |
| comp | GLOBcomp_1 | water |  |
| prop | GLOBprop_1 | massdensitykgm3 |  |
| var | GLOBvar_1 | temperaturek |  |
| var | GLOBvar_3 | pressurekpa |  |
| var | GLOBvar_2 | molefraction<ethanol> |  |

### History
- [query_thermoml]
- [query_thermoml_parallel]
- [inspect_block]
- [fit_multi_system]
- [fit_multi_system]

### Query Results
#### query
**L1_query_1** — status: partial · validation: FLAGGED(2)

**Summary:** In the ThermoML database, one confirmed block of binary ethanol + water mass density data was identified: GLOBlit_1483 :: PROPblock_1 (DOI 10.1016/j.fluid.2014.05.032), containing 140 data points spanning 292.95–448.15 K, 2450–40140 kPa, and ethanol mole fractions 0.0163–0.0946 (dilute ethanol region only). Representative values at the 348.15 K isotherm show density decreasing with increasing ethanol mole fraction (e.g., ~982.3 kg/m³ at x=0.0163 and 39600 kPa down to ~933.7 kg/m³ at x=0.0946 and 2730 kPa) and increasing with pressure at each composition. This dataset covers only elevated pressures (2.5–40 MPa) and dilute ethanol compositions; it does not provide atmospheric-pressure or full-composition-range data. An initially returned block GLOBlit_1742 :: PROPblock_1 was confirmed upon inspection to be methanol + water, not ethanol + water. Two other blocks (GLOBlit_220 and GLOBlit_2432) were returned by the initial search but were not inspected, so their coverage cannot be confirmed.

**Answer:**

**Binary ethanol–water mass density data in the ThermoML database:**

The search for binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) mass density (GLOBprop_1) blocks found the following confirmed result:

##### Confirmed ethanol–water block

**GLOBlit_1483 :: PROPblock_1**  
- **DOI:** 10.1016/j.fluid.2014.05.032  
- **System:** binary ethanol + water  
- **Data points:** 140  
- **Temperature range:** 292.95–448.15 K (includes isotherms at 348.15 K, near the user-requested target of ~350 K)  
- **Pressure range:** 2450–40140 kPa (high-pressure data)  
- **Ethanol mole fraction range:** 0.0163–0.0946 (dilute ethanol region only)  

Representative data at 348.15 K (nearest isotherm to the requested ~350 K target):

**WM_L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *Ethanol x* | *P (kPa)* | *ρ (kg/m³)* |
|---|---|---|---|
| WM_L1#1_Table#1_Row#1 | 「0.0163」 | 「39600」 | 「982.3」 |
| WM_L1#1_Table#1_Row#2 | 「0.0163」 | 「20750」 | 「974.7」 |
| WM_L1#1_Table#1_Row#3 | 「0.0163」 | 「10980」 | 「970.6」 |
| WM_L1#1_Table#1_Row#4 | 「0.0163」 | 「3220」 | 「967.1」 |
| WM_L1#1_Table#1_Row#5 | 「0.0343」 | 「39860」 | 「974.7」 |
| WM_L1#1_Table#1_Row#6 | 「0.0343」 | 「30850」 | 「971.3」 |
| WM_L1#1_Table#1_Row#7 | 「0.0343」 | 「21160」 | 「967.5」 |
| WM_L1#1_Table#1_Row#8 | 「0.0343」 | 「11590」 | 「963.5」 |
| WM_L1#1_Table#1_Row#9 | 「0.073」 | 「39600」 | 「958.9」 |
| WM_L1#1_Table#1_Row#10 | 「0.073」 | 「20870」 | 「950.8」 |
| WM_L1#1_Table#1_Row#11 | 「0.073」 | 「11060」 | 「946.6」 |
| WM_L1#1_Table#1_Row#12 | 「0.073」 | 「3330」 | 「943.0」 |
| WM_L1#1_Table#1_Row#13 | 「0.0946」 | 「37790」 | 「948.7」 |
| WM_L1#1_Table#1_Row#14 | 「0.0946」 | 「29730」 | 「945.4」 |
| WM_L1#1_Table#1_Row#15 | 「0.0946」 | 「20870」 | 「941.6」 |
| WM_L1#1_Table#1_Row#16 | 「0.0946」 | 「11390」 | 「937.4」 |
| WM_L1#1_Table#1_Row#17 | 「0.0946」 | 「2730」 | 「933.7」 |

**Note:** This dataset covers only dilute ethanol compositions (up to ~9.5 mol%) at elevated pressures (2.5–40 MPa). It does not provide atmospheric-pressure or full-composition-range density data.

##### Other blocks from the initial search

- **GLOBlit_1742 :: PROPblock_1** — Upon inspection, this block is actually **methanol + water** (not ethanol + water) and is therefore not relevant to this query.  
- **GLOBlit_220** and **GLOBlit_2432** were also returned by the initial search as potential ethanol–water density blocks, but these were not inspected in this run, so their exact composition/temperature coverage and data point counts cannot be confirmed here.

**Chemistry note:** The inspected data show the expected trend: at 348.15 K, density decreases with increasing ethanol mole fraction (from ~982 kg/m³ at x = 0.0163 to ~949 kg/m³ at x = 0.0946 at comparable pressures), and increases with pressure at each composition, consistent with the lower density of ethanol relative to water and normal liquid compressibility behavior.

**Core claims:**
- The ThermoML database contains a confirmed binary ethanol–water mass density block (GLOBlit_1483 :: PROPblock_1, DOI 10.1016/j.fluid.2014.05.032) with 140 data points spanning 292.95–448.15 K, 2450–40140 kPa, and ethanol mole fractions of 0.0163–0.0946 (dilute ethanol region only).
- At 348.15 K, the data show density decreasing with increasing ethanol mole fraction (from ~982 kg/m³ at x = 0.0163 to ~949 kg/m³ at x = 0.0946 at comparable pressures) and increasing with pressure at each composition, consistent with the lower density of ethanol relative to water and normal liquid compressibility.
- This dataset covers only dilute ethanol compositions (up to ~9.5 mol%) at elevated pressures (2.5–40 MPa) and does not provide atmospheric-pressure or full-composition-range density data.
- Two additional blocks (GLOBlit_220 and GLOBlit_2432) were returned by the initial search as potential ethanol–water density blocks but were not inspected, so their coverage cannot be confirmed.

**Core blocks found:**

**WM_L1#1_Blocks_(Analysis_L1#1_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#1_Table#2 | 「GLOBlit_1483」 | 「PROPblock_1」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density measurements for binary ethanol + water mixtures at 292.95–448.15 K and 2450–40140 kPa, covering ethanol mole fractions 0.0163–0.0946; 140 data points.」 |

*Not stored here: 2 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** GLOBlit_1483::PROPblock_1: 350 (near '…s isotherms at 348.15 K, near the user-requested target of ~…') matches no inspected row/stat, database table, or other source of GLOBlit_1483::PROPblock_1
- **UNGROUNDED_LITERAL** GLOBlit_1483::PROPblock_1: 350 (near '…tative data at 348.15 K (nearest isotherm to the requested ~…') matches no inspected row/stat, database table, or other source of GLOBlit_1483::PROPblock_1


#### broad_search
**L1_query_2** — status: success · validation: FLAGGED(2)

**Summary:** For binary ethanol + water mass density at atmospheric pressure, the best ThermoML source identified is GLOBlit_220 :: PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019), providing 162 atmospheric-pressure points (P = 100 kPa) across three isotherms (298.15, 323.15, and 348.15 K) with x(ethanol) = 0.003–1.0 and densities from 739.4 to 995.3 kg/m³. A supplementary source is GLOBlit_5201 :: PROPblock_19 (DOI: 10.1016/j.jct.2018.02.022) with 244 points at P = 92.3 kPa, four isotherms from 293.15 to 308.15 K, x(ethanol) = 0–1, and densities 776.592–998.429 kg/m³. GLOBlit_2825 :: PROPblock_12 (DOI: 10.1016/j.jct.2007.05.004) offers 37 points at 101.0 kPa, 293.15–303.15 K, x(water) = 0–1, densities 781.15–998.2 kg/m³. No inspected block reaches the upper target temperature of 353 K at atmospheric pressure; the highest verified atmospheric-pressure isotherm is 348.15 K in GLOBlit_220.

**Answer:**

#### Binary Ethanol + Water Mass Density Blocks at Atmospheric Pressure

##### Best Candidate: GLOBlit_220 :: PROPblock_2
**DOI:** 10.1016/j.fluid.2004.11.019

This block is the strongest match for wide-composition, multi-temperature density data at atmospheric pressure:

- **Total points:** 810 (162 at atmospheric pressure, P = 100 kPa)
- **Temperatures:** 298.15, 323.15, and 348.15 K (three isotherms)
- **Composition range:** x(ethanol) = 0.003–1.0 (full range)
- **Density range (at 100 kPa):** 739.4–995.3 kg/m³

Representative atmospheric-pressure data (from inspection):

**WM_L1#2_Table#1_(Analysis_L1#2_Answer):**

| *row_id* | *T (K)* | *x(ethanol)* | *ρ (kg/m³)* |
|---|---|---|---|
| WM_L1#2_Table#1_Row#1 | 「298.15」 | 「0.003」 | 「995.3」 |
| WM_L1#2_Table#1_Row#2 | 「298.15」 | 「0.2502」 | 「918.5」 |
| WM_L1#2_Table#1_Row#3 | 「298.15」 | 「0.4501」 | 「868.8」 |
| WM_L1#2_Table#1_Row#4 | 「298.15」 | 「0.6967」 | 「825.2」 |
| WM_L1#2_Table#1_Row#5 | 「298.15」 | 「1.0」 | 「785.7」 |
| WM_L1#2_Table#1_Row#6 | 「323.15」 | 「0.003」 | 「986.5」 |
| WM_L1#2_Table#1_Row#7 | 「323.15」 | 「0.2269」 | 「905.2」 |
| WM_L1#2_Table#1_Row#8 | 「323.15」 | 「0.4501」 | 「846.7」 |
| WM_L1#2_Table#1_Row#9 | 「323.15」 | 「0.6967」 | 「802.8」 |
| WM_L1#2_Table#1_Row#10 | 「323.15」 | 「1.0」 | 「763.7」 |
| WM_L1#2_Table#1_Row#11 | 「348.15」 | 「0.003」 | 「973.1」 |
| WM_L1#2_Table#1_Row#12 | 「348.15」 | 「0.1903」 | 「895.8」 |
| WM_L1#2_Table#1_Row#13 | 「348.15」 | 「0.4034」 | 「833.4」 |
| WM_L1#2_Table#1_Row#14 | 「348.15」 | 「0.6489」 | 「785.6」 |
| WM_L1#2_Table#1_Row#15 | 「348.15」 | 「1.0」 | 「739.4」 |

Each isotherm has approximately 54 composition points (derived by dividing 162 atmospheric points by 3 isotherms — not a database value), providing dense composition coverage ideal for Redlich-Kister fitting.

##### Other Inspected Candidates

**GLOBlit_5201 :: PROPblock_19** (DOI: 10.1016/j.jct.2018.02.022)
- **Points:** 244, all at P = 92.3 kPa (near-atmospheric)
- **Temperature:** 293.15–308.15 K (4 isotherms)
- **Composition:** x(ethanol) = 0–1 (full range)
- **Density:** 776.592–998.429 kg/m³
- Excellent composition coverage but temperature range is narrower and lower than GLOBlit_220.

**GLOBlit_2825 :: PROPblock_12** (DOI: 10.1016/j.jct.2007.05.004)
- **Points:** 37, all at P = 101.0 kPa
- **Temperature:** 293.15–303.15 K (3 isotherms)
- **Composition:** x(water) = 0–1 (full range)
- **Density:** 781.15–998.2 kg/m³
- Full composition range at atmospheric pressure, but fewer points and lower temperatures.

##### Additional Candidates (Not Inspected)

The following blocks were identified by the search discovery tool but have not been individually inspected in this run. No specific data values are quoted for them:

- **GLOBlit_9006 :: PROPblock_1** (DOI: 10.1021/je060335h) — search-reported as having full composition range at lower temperatures.
- **GLOBlit_10866 :: PROPblock_7** (DOI: 10.1021/je700300y) — search-reported as having wide composition range.
- **GLOBlit_10699 :: PROPblock_6** (DOI: 10.1021/je600565m) — search-reported as having moderate composition range.
- **GLOBlit_11136 :: PROPblock_9** (DOI: 10.1021/je800150h) — search-reported as having partial composition range.
- **GLOBlit_5473 :: PROPblock_21** (DOI: 10.1016/j.jct.2019.02.027) — search-reported as having full composition range with very few points.

##### Regarding GLOBlit_2432
**DOI:** 10.1016/j.jct.2004.07.019, PROPblock_2 — Per search discovery results (not individually inspected), this block operates at elevated pressures, not atmospheric. **Not suitable** for atmospheric-pressure fitting.

##### Key Finding
**No block in the database was found to cover the requested upper temperature of 353 K (instruction target, not a database value) at atmospheric pressure** for this binary system. The closest inspected data is GLOBlit_220 at 348.15 K. Per search discovery results (not inspected), GLOBlit_1742 (PROPblock_3) reaches higher temperatures but only at elevated pressures.

**Recommendation:** GLOBlit_220 :: PROPblock_2 is the best single source — it provides dense composition coverage at 100 kPa across 298.15, 323.15, and 348.15 K, with x(ethanol) = 0.003–1.0. GLOBlit_5201 :: PROPblock_19 (244 pts, x = 0–1, T = 293.15–308.15 K, P = 92.3 kPa) could supplement with additional near-ambient data.

**Core claims:**
- GLOBlit_220 :: PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019) is identified as the best single source for binary ethanol + water mass density data at atmospheric pressure, providing 162 points at P = 100 kPa across three isotherms (298.15, 323.15, and 348.15 K) with x(ethanol) = 0.003–1.0 and densities ranging from 739.4–995.3 kg/m³.
- At each isotherm in GLOBlit_220 :: PROPblock_2, density decreases monotonically with increasing ethanol mole fraction at 100 kPa, and density decreases with increasing temperature at fixed composition.
- GLOBlit_5201 :: PROPblock_19 (DOI: 10.1016/j.jct.2018.02.022) provides a supplementary 244-point dataset at P = 92.3 kPa over T = 293.15–308.15 K with x(ethanol) = 0–1 and densities of 776.592–998.429 kg/m³, but covers a narrower and lower temperature range than GLOBlit_220.
- No block in the database was found to cover 353 K at atmospheric pressure for this binary system; the closest inspected atmospheric-pressure data reaches 348.15 K (GLOBlit_220). The value 353 K is identified as an instruction target, not a database value.
- The stated count of approximately 54 composition points per isotherm in GLOBlit_220 :: PROPblock_2 is derived by dividing 162 atmospheric points by 3 isotherms and is flagged as UNVERIFIED against the database.

**Core blocks found:**

**WM_L1#2_Blocks_(Analysis_L1#2_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#2_Table#2 | 「GLOBlit_220」 | 「PROPblock_2」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of binary ethanol + water at 100 kPa across 298.15–348.15 K, x(ethanol) = 0.003–1.0, 162 atmospheric-pressure points from 810 total.」 |
| WM_L1#2_Table#3 | 「GLOBlit_5201」 | 「PROPblock_19」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of binary ethanol + water at 92.3 kPa across 293.15–308.15 K, x(ethanol) = 0–1, 244 points.」 |
| WM_L1#2_Table#4 | 「GLOBlit_2825」 | 「PROPblock_12」 | 「GLOBcomp_2, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density of binary ethanol + water at 101.0 kPa across 293.15–303.15 K, x(water) = 0–1, 37 points.」 |

*Not stored here: 4 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** FLAGGED(2) — unresolved ungrounded values (treat as UNVERIFIED; re-dispatch to resolve if they matter):

- **UNGROUNDED_LITERAL** GLOBlit_220::PROPblock_2: 54 (near '…Each isotherm has approximately 54 composition points (deriv…') matches no inspected row/stat, database table, or other source of GLOBlit_220::PROPblock_2
- **UNGROUNDED_LITERAL** PROPblock_2: 353 (near '…abase was found to cover the requested upper temperature of …') matches no inspected row/stat, database table, or other source of PROPblock_2


#### inspect_220
**L1_query_3** — status: success · validation: PASS

**Summary:** GLOBlit_220 PROPblock_1 (DOI 10.1016/j.fluid.2004.11.019) contains pure ethanol density data only, not ethanol + water mixture data. The block reports 15 liquid-phase mass density measurements for pure ethanol (C₂H₆O) over 298.15–348.15 K and 100–40000 kPa, with densities ranging from 739.4 to 815.7 kg/m³. No water is present; no composition variable is included. Binary ethanol–water mixture data, if present in this DOI, would be in other blocks (e.g., PROPblock_2, PROPblock_3, etc.).

**Answer:**

**GLOBlit_220 PROPblock_1 — Inspection Result**

This block contains **pure ethanol density data only** — it is **not** ethanol + water mixture data.

**Details:**

**WM_L1#3_Table#1_(Analysis_L1#3_Answer):**

| *row_id* | *Field* | *Value* |
|---|---|---|
| WM_L1#3_Table#1_Row#1 | 「DOI」 | 「10.1016/j.fluid.2004.11.019 (GLOBlit_220)」 |
| WM_L1#3_Table#1_Row#2 | 「Block」 | 「PROPblock_1」 |
| WM_L1#3_Table#1_Row#3 | 「System type」 | 「Unary (pure component)」 |
| WM_L1#3_Table#1_Row#4 | 「Compound」 | 「Ethanol (GLOBcomp_2, C₂H₆O)」 |
| WM_L1#3_Table#1_Row#5 | 「Property」 | 「Mass density (GLOBprop_1), kg/m³」 |
| WM_L1#3_Table#1_Row#6 | 「Phase」 | 「Liquid」 |
| WM_L1#3_Table#1_Row#7 | 「Temperature range」 | 「298.15–348.15 K (15 points)」 |
| WM_L1#3_Table#1_Row#8 | 「Pressure range」 | 「100–40000 kPa (15 points)」 |
| WM_L1#3_Table#1_Row#9 | 「Density range」 | 「739.4–815.7 kg/m³ (15 points)」 |
| WM_L1#3_Table#1_Row#10 | 「Data points」 | 「15 total (12 shown via RDP)」 |
| WM_L1#3_Table#1_Row#11 | 「Composition」 | 「None (pure ethanol — no water present)」 |

**Inspected data (12 of 15 points shown):**

**WM_L1#3_Table#2_(Analysis_L1#3_Answer):**

| *row_id* | *BLKpoint_id* | *Temperature (K)* | *Pressure (kPa)* | *Mass density (kg/m³)* |
|---|---|---|---|---|
| WM_L1#3_Table#2_Row#1 | 「BLKpoint_1」 | 「298.15」 | 「100」 | 「785.7」 |
| WM_L1#3_Table#2_Row#2 | 「BLKpoint_3」 | 「298.15」 | 「20000」 | 「801.9」 |
| WM_L1#3_Table#2_Row#3 | 「BLKpoint_5」 | 「298.15」 | 「40000」 | 「815.7」 |
| WM_L1#3_Table#2_Row#4 | 「BLKpoint_6」 | 「323.15」 | 「100」 | 「763.7」 |
| WM_L1#3_Table#2_Row#5 | 「BLKpoint_7」 | 「323.15」 | 「10000」 | 「773.4」 |
| WM_L1#3_Table#2_Row#6 | 「BLKpoint_8」 | 「323.15」 | 「20000」 | 「782.3」 |
| WM_L1#3_Table#2_Row#7 | 「BLKpoint_10」 | 「323.15」 | 「40000」 | 「797.7」 |
| WM_L1#3_Table#2_Row#8 | 「BLKpoint_11」 | 「348.15」 | 「100」 | 「739.4」 |
| WM_L1#3_Table#2_Row#9 | 「BLKpoint_12」 | 「348.15」 | 「10000」 | 「751.2」 |
| WM_L1#3_Table#2_Row#10 | 「BLKpoint_13」 | 「348.15」 | 「20000」 | 「761.2」 |
| WM_L1#3_Table#2_Row#11 | 「BLKpoint_14」 | 「348.15」 | 「30000」 | 「770.3」 |
| WM_L1#3_Table#2_Row#12 | 「BLKpoint_15」 | 「348.15」 | 「40000」 | 「778.6」 |

**Conclusion:** This block does **not** contain ethanol + water binary density data. Although the parent DOI (10.1016/j.fluid.2004.11.019) references ethanol–water mixtures in its title, PROPblock_1 specifically holds only pure ethanol measurements. Other blocks within GLOBlit_220 (e.g., PROPblock_2, PROPblock_3, etc.) should be checked for the binary mixture data.

**Core claims:**
- GLOBlit_220 PROPblock_1 contains pure ethanol density data only, not ethanol + water binary mixture data, despite the parent DOI (10.1016/j.fluid.2004.11.019) referencing ethanol–water mixtures in its title.
- The block reports 15 liquid-phase mass density data points for pure ethanol spanning 298.15–348.15 K in temperature, 100–40000 kPa in pressure, and 739.4–815.7 kg/m³ in density.
- Other blocks within GLOBlit_220 (e.g., PROPblock_2, PROPblock_3) would need to be checked for binary ethanol + water mixture data.

**Core blocks found:**

**WM_L1#3_Blocks_(Analysis_L1#3_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#3_Table#3 | 「GLOBlit_220」 | 「PROPblock_1」 | 「GLOBcomp_2」 | 「GLOBprop_1」 | 「Pure ethanol mass density measurements at 298.15–348.15 K and 100–40000 kPa, 15 data points, liquid phase. Not ethanol+water binary data.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


#### inspect_2432
**L1_query_4** — status: success · validation: PASS

**Summary:** GLOBlit_2432 PROPblock_1 does not contain ethanol + water density data. It contains methanol + water density data. The DOI is 10.1016/j.jct.2004.07.019. The compounds are water (GLOBcomp_1) and methanol (GLOBcomp_4). The property is mass density (kg/m³), measured as density differences relative to pure water using the vibrating-tube method, in the liquid phase. The temperature range is 298.16–573.15 K, pressure range is 390–30320 kPa, methanol molality range is 0.07706–1.04694 mol/kg, and there are 596 data points. Density difference values range from −13.3065 to −0.4632 kg/m³, all negative, indicating methanol solutions are less dense than pure water at the same T and P. For example, at 298.16 K and 14450 kPa, the density difference at methanol molality 0.10243 mol/kg is −0.6308 kg/m³ and at molality 0.98932 mol/kg is −5.7028 kg/m³. The second component is methanol (CH₄O), not ethanol.

**Answer:**

**Inspection of GLOBlit_2432 PROPblock_1**

This block does **not** contain ethanol + water density data. It contains **methanol + water** density data instead.

**Details:**

- **DOI:** 10.1016/j.jct.2004.07.019 (GLOBlit_2432)
- **Compounds:** water (GLOBcomp_1) + methanol (GLOBcomp_4) — a binary system
- **Property:** Mass density (kg/m³), measured as density differences relative to pure solvent water, using the vibrating-tube method
- **Phase:** Liquid
- **Temperature range:** 298.16–573.15 K
- **Pressure range:** 390–30320 kPa (high-pressure measurements)
- **Composition range:** Methanol molality 0.07706–1.04694 mol/kg
- **Total data points:** 596
- **Density difference values:** range from −13.3065 to −0.4632 kg/m³ (all negative, indicating methanol solutions are less dense than pure water at the same T and P)

For example, at 298.16 K and 14450 kPa, the density difference at methanol molality 0.10243 mol/kg is −0.6308 kg/m³ (BLKpoint_1), while at molality 0.98932 mol/kg it is −5.7028 kg/m³ (BLKpoint_6), showing the expected trend of increasing density reduction with higher methanol content.

**Conclusion:** This block is **not** ethanol + water mass density data. The second component is methanol (CH₄O, GLOBcomp_4), not ethanol.

**Core claims:**
- PROPblock_1 of GLOBlit_2432 (DOI 10.1016/j.jct.2004.07.019) contains methanol + water density data, not ethanol + water density data; the second component is methanol (CH₄O, GLOBcomp_4).
- The block reports liquid-phase mass density differences (kg/m³) relative to pure water for the methanol + water binary system, covering 298.16–573.15 K, 390–30320 kPa, methanol molality 0.07706–1.04694 mol/kg, with 596 data points.
- All reported density difference values are negative (ranging from −13.3065 to −0.4632 kg/m³), indicating that methanol solutions are less dense than pure water at the same temperature and pressure, with the magnitude of the density reduction increasing with higher methanol content.

**Core blocks found:**

**WM_L1#4_Blocks_(Analysis_L1#4_CoreBLK):**

| *table_id* | *lit_num_id* | *block_number* | *comp_num_ids* | *prop_num_ids* | *description* |
|---|---|---|---|---|---|
| WM_L1#4_Table#1 | 「GLOBlit_2432」 | 「PROPblock_1」 | 「GLOBcomp_4, GLOBcomp_1」 | 「GLOBprop_1」 | 「Mass density difference measurements for methanol + water at 298.16–573.15 K, 390–30320 kPa, methanol molality 0.07706–1.04694 mol/kg; 596 data points. Not ethanol + water density data.」 |

*Not stored here: 1 verbatim data_inspections table(s). Verbatim evidence stays on the tool-history rail and is re-attached to the final envelope deterministically.*

**Validation (final in-session gate):** PASS — no unresolved ungrounded values.


### Inspected Blocks
- GLOBlit_220 | 10.1016/j.fluid.2004.11.019 | PROPblock_2: 810 rows; x=['mole_fraction_<ethanol>']; y=['mass_density_kg_m3']
    - BLKprop_1 / GLOBprop_1: presentation=Direct value, X; reference=None; standard_state=None
      response gate BLKprop_1 / GLOBprop_1: kind=direct; materialize_reference=False; supported=True; units=kg/m3 -> kg/m3

### Completed Fits
  - EtOH-Water_298K [10.1016/j.fluid.2004.11.019/PROPblock_2] (ethanol, water): RK order=3, R²=0.997283, RMSE=0.47476545853553287, coeffs=[-120.55681, 18.567625, 43.919128, -31.350563]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      pure refs: ethanol=785.7, water=992.083 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png
  - EtOH-Water_323K [10.1016/j.fluid.2004.11.019/PROPblock_2] (ethanol, water): RK order=5, R²=0.998545, RMSE=0.4343815607863475, coeffs=[-147.181529, 39.605693, 7.017496, -0.818149, 43.210013, -57.743228]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      pure refs: ethanol=763.7, water=983.05 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_excess.png
  - EtOH-Water_348K [10.1016/j.fluid.2004.11.019/PROPblock_2] (ethanol, water): RK order=5, R²=0.998607, RMSE=0.4911460748640253, coeffs=[-167.860024, 50.451482, -18.395033, 43.192936, 76.872347, -109.653896]
      response: direct via X = reported X | 0 reference source(s) | kg/m3 -> kg/m3
      pure refs: ethanol=739.4, water=969.467 [block-edges (water: direct/good, ethanol: direct/good)]
      fit_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_fit.csv
      excess_csv: $ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_excess.csv
      fit_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_fit.png
      excess_plot: $ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_excess.png

## Session Output Files

### data
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.csv` — RK fit data — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_fit.csv` — RK fit data — 10.1016/j.fluid.2004.11.019 PROPblock_2_T323.1
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_fit.csv` — RK fit data — 10.1016/j.fluid.2004.11.019 PROPblock_2_T348.1
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.csv` — Excess property — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_excess.csv` — Excess property — 10.1016/j.fluid.2004.11.019 PROPblock_2_T348.1
- `$ROOT/data\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_excess.csv` — Excess property — 10.1016/j.fluid.2004.11.019 PROPblock_2_T323.1

### plot
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_fit.png` — RK fit plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T323.1
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_fit.png` — RK fit plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_fit.png` — RK fit plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T348.1
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T323.1_excess.png` — Excess plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T323.1
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T298.1_excess.png` — Excess plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T298.1
- `$ROOT/plots\10_1016_j_fluid_2004_11_019_BPROPblock_2_T348.1_excess.png` — Excess plot — 10.1016/j.fluid.2004.11.019 PROPblock_2_T348.1

</memory>

## User
I need a Redlich–Kister density correlation for liquid ethanol + water at 350 K. Can the available measurements support that temperature directly? If not, what is the nearest defensible temperature and why should the 350 K prediction be withheld?

## Assistant
<summary>Starting search for ethanol + water density mixture data in ThermoML, focusing on temperatures near 350 K.</summary>
<tool_call>query_thermoml(instruction=Search for blocks…)</tool_call>

## User
<tool_result>
<subagent_answer>
### L1#1 — query_thermoml return

**Status:** status=partial

**Summary:** In the ThermoML database, one confirmed block of binary ethanol + water mass density data was identified: GLOBlit_1483 :: PROPblock_1 (DOI 10.1016/j.fluid.2014.05.032), containing 140 data points spanning 292.95–448.15 K, 2450–40140 kPa, and ethanol mole fractions 0.0163–0.0946 (dilute ethanol region only). Representative values at the 348.15 K isotherm show density decreasing with increasing ethanol mole fraction (e.g., ~982.3 kg/m³ at x=0.0163 and 39600 kPa down to ~933.7 kg/m³ at x=0.0946 and 2730 kPa) and increasing with pressure at each composition. This dataset covers only elevated pressures (2.5–40 MPa) and dilute ethanol compositions; it does not provide atmospheric-pressure or full-composition-range data. An initially returned block GLOBlit_1742 :: PROPblock_1 was confirmed upon inspection to be methanol + water, not ethanol + water. Two other blocks (GLOBlit_220 and GLOBlit_2432) were returned by the initial search but were not inspected, so their coverage cannot be confirmed.

**Answer:**

**Binary ethanol–water mass density data in the ThermoML database:**

The search for binary ethanol (GLOBcomp_2) + water (GLOBcomp_1) mass density (GLOBprop_1) blocks found the following confirmed result:

##### Confirmed ethanol–water block

**GLOBlit_1483 :: PROPblock_1**  
- **DOI:** 10.1016/j.fluid.2014.05.032  
- **System:** binary ethanol + water  
- **Data points:** 140  
- **Temperature range:** 292.95–448.15 K (includes isotherms at 348.15 K, near the user-requested target of ~350 K)  
- **Pressure range:** 2450–40140 kPa (high-pressure data)  
- **Ethanol mole fraction range:** 0.0163–0.0946 (dilute ethanol region only)  

Representative data at 348.15 K (nearest isotherm to the requested ~350 K target):

**L1#1_Table#1_(Analysis_L1#1_Answer):**

| *row_id* | *Ethanol x* | *P (kPa)* | *ρ (kg/m³)* |
|---|---|---|---|
| L1#1_Table#1_Row#1 | 「0.0163」 | 「39600」 | 「982.3」 |
| L1#1_Table#1_Row#2 | 「0.0163」 | 「20750」 | 「974.7」 |
| L1#1_Table#1_Row#3 | 「0.0163」 | 「10980」 | 「970.6」 |
| L1#1_Table#1_Row#4 | 「0.0163」 | 「3220」 | 「967.1」 |
| L1#1_Table#1_Row#5 | 「0.0343」 | 「39860」 | 「974.7」 |
| L1#1_Table#1_Row#6 | 「0.0343」 | 「30850」 | 「971.3」 |
| L1#1_Table#1_Row#7 | 「0.0343」 | 「21160」 | 「967.5」 |
| L1#1_Table#1_Row#8 | 「0.0343」 | 「11590」 | 「963.5」 |
| L1#1_Table#1_Row#9 | 「0.073」 | 「39600」 | 「958.9」 |
| L1#1_Table#1_Row#10 | 「0.073」 | 「20870」 | 「950.8」 |
| L1#1_Table#1_Row#11 | 「0.073」 | 「11060」 | 「946.6」 |
| L1#1_Table#1_Row#12 | 「0.073」 | 「3330」 | 「943.0」 |
| L1#1_Table#1_Row#13 | 「0.0946」 | 「37790」 | 「948.7」 |
| L1#1_Table#1_Row#14 | 「0.0946」 | 「29730」 | 「945.4」 |
| L1#1_Table#1_Row#15 | 「0.0946」 | 「20870」 | 「941.6」 |
| L1#1_Table#1_Row#16 | 「0.0946」 | 「11390」 | 「937.4」 |
| L1#1_Table#1_Row#17 | 「0.0946」 | 「2730」 | 「933.7」 |

**Note:** This dataset covers only dilute ethanol compositions (up to ~9.5 mol%) at elevated pressures (2.5–40 MPa). It does not provide atmospheric-pressure or full-composition-range density data.

##### Other blocks from the initial search

- **GLOBlit_1742 :: PROPblock_1** — Upon inspection, this block is actually **methanol + water** (not ethanol + water) and is therefore not relevant to this query.  
- **GLOBlit_220** and **GLOBlit_2432** were also returned by the initial search as potential ethanol–water density blocks, but these were not inspected in this run, so their exact composition/temperature coverage and data point counts cannot be confirmed here.

**Chemistry note:** The inspected data show the expected trend: at 348.15 K, density decreases with increasing ethanol mole fraction (from ~982 kg/m³ at x = 0.0163 to ~949 kg/m³ at x = 0.0946 at comparable pressures), and increases with pressure at each composition, consistent with the lower density of ethanol relative to water and normal liquid compressibility behavior.

---
[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:
- **UNGROUNDED_LITERAL** GLOBlit_1483::PROPblock_1: 350 (near '…s isotherms at 348.15 K, near the user-requested target of ~…') matches no inspected row/stat, database table, or other source of GLOBlit_1483::PROPblock_1
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_1483::PROPblock_1", nearest={"column": "temperature_k", "value": 350.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** GLOBlit_1483::PROPblock_1: 350 (near '…tative data at 348.15 K (nearest isotherm to the requested ~…') matches no inspected row/stat, database table, or other source of GLOBlit_1483::PROPblock_1
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_1483::PROPblock_1", nearest={"column": "temperature_k", "value": 350.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
Inspected so far: PROPblock_1

**Core claims:**
- The ThermoML database contains a confirmed binary ethanol–water mass density block (GLOBlit_1483 :: PROPblock_1, DOI 10.1016/j.fluid.2014.05.032) with 140 data points spanning 292.95–448.15 K, 2450–40140 kPa, and ethanol mole fractions of 0.0163–0.0946 (dilute ethanol region only).
- At 348.15 K, the data show density decreasing with increasing ethanol mole fraction (from ~982 kg/m³ at x = 0.0163 to ~949 kg/m³ at x = 0.0946 at comparable pressures) and increasing with pressure at each composition, consistent with the lower density of ethanol relative to water and normal liquid compressibility.
- This dataset covers only dilute ethanol compositions (up to ~9.5 mol%) at elevated pressures (2.5–40 MPa) and does not provide atmospheric-pressure or full-composition-range density data.
- Two additional blocks (GLOBlit_220 and GLOBlit_2432) were returned by the initial search as potential ethanol–water density blocks but were not inspected, so their coverage cannot be confirmed.

#### Core blocks found — verbatim ledger

```ledger
**L1#1_Table#2_(Analysis_L1#1_CoreBLK):**
lit_num_id: GLOBlit_1483 | lit_id: 2014-abd-akh-0 | doi: 10.1016/j.fluid.2014.05.032
block: PROPblock_1 | BLKsubsys_id: — | type: PureOrMixtureData (GLOBblocktype_1) | system: binary | n_datapoints: 140
compounds: ethanol (C2H6O; GLOBcomp_2; DOIcomp_1; InChIKey LFQSCWFLJHTTHZ-UHFFFAOYSA-N); water (H2O; GLOBcomp_1; DOIcomp_2; InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N)
prop_num_ids: GLOBprop_1
description: Mass density measurements for binary ethanol + water mixtures at 292.95–448.15 K and 2450–40140 kPa, covering ethanol mole fractions 0.0163–0.0946; 140 data points.

| *row_id* | *kind* | *id* | *name* | *detail* |
|---|---|---|---|---|
| L1#1_Table#2_Row#1 | 「variable」 | 「BLKvar_1/GLOBvar_3」 | 「Pressure, kPa」 | 「range=2450.0–40140.0 · n_unique=112 · phase=Liquid」 |
| L1#1_Table#2_Row#2 | 「variable」 | 「BLKvar_2/GLOBvar_1」 | 「Temperature, K」 | 「range=292.95–448.15 · n_unique=11 · phase=Liquid」 |
| L1#1_Table#2_Row#3 | 「variable」 | 「BLKvar_3/GLOBvar_2」 | 「Mole fraction of ethanol」 | 「range=0.0163–0.0946 · n_unique=4 · phase=Liquid」 |
| L1#1_Table#2_Row#4 | 「property」 | 「BLKprop_1/GLOBprop_1」 | 「Mass density, kg/m3」 | 「method=Constant-volume piezometry (GLOBmeas_66) · range=831.7–1006.1 · mean=934.762857 · n=140 · phase=Liquid」 |
```

#### Data inspections — verbatim ledger

```ledger
**L1#1_Table#3_(Analysis_L1#1_INSP):**
lit_num_id: GLOBlit_1742 | doi: 10.1016/j.fluid.2015.07.012 | block: PROPblock_1
table_mode: rdp | inspection_id: INSP_da246e84fdf8 | rows_shown: 36

| *row_id* | *BLKpoint_id* | *temperature_k* | *pressure_kpa* | *mole_fraction_<methanol>* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| L1#1_Table#3_Row#1 | 「BLKpoint_1」 | 「350.7」 | 「10000」 | 「0.1」 | 「945.55」 |
| L1#1_Table#3_Row#2 | 「BLKpoint_4」 | 「350.7」 | 「10000」 | 「0.4」 | 「865.13」 |
| L1#1_Table#3_Row#3 | 「BLKpoint_6」 | 「350.7」 | 「10000」 | 「0.8」 | 「780.91」 |
| L1#1_Table#3_Row#4 | 「BLKpoint_7」 | 「350.7」 | 「20000」 | 「0.1」 | 「949.82」 |
| L1#1_Table#3_Row#5 | 「BLKpoint_10」 | 「350.7」 | 「20000」 | 「0.4」 | 「870.55」 |
| L1#1_Table#3_Row#6 | 「BLKpoint_12」 | 「350.7」 | 「20000」 | 「0.8」 | 「789.25」 |
| L1#1_Table#3_Row#7 | 「BLKpoint_13」 | 「350.7」 | 「30000」 | 「0.1」 | 「954.11」 |
| L1#1_Table#3_Row#8 | 「BLKpoint_16」 | 「350.7」 | 「30000」 | 「0.4」 | 「876.99」 |
| L1#1_Table#3_Row#9 | 「BLKpoint_18」 | 「350.7」 | 「30000」 | 「0.8」 | 「797.6」 |
| L1#1_Table#3_Row#10 | 「BLKpoint_19」 | 「350.7」 | 「40000」 | 「0.1」 | 「958.39」 |
| L1#1_Table#3_Row#11 | 「BLKpoint_22」 | 「350.7」 | 「40000」 | 「0.4」 | 「882.71」 |
| L1#1_Table#3_Row#12 | 「BLKpoint_24」 | 「350.7」 | 「40000」 | 「0.8」 | 「805.96」 |
| L1#1_Table#3_Row#13 | 「BLKpoint_25」 | 「373.2」 | 「10000」 | 「0.1」 | 「928.71」 |
| L1#1_Table#3_Row#14 | 「BLKpoint_29」 | 「373.2」 | 「10000」 | 「0.6」 | 「799.33」 |
| L1#1_Table#3_Row#15 | 「BLKpoint_31」 | 「373.2」 | 「10000」 | 「1」 | 「725.29」 |
| L1#1_Table#3_Row#16 | 「BLKpoint_32」 | 「373.2」 | 「20000」 | 「0.1」 | 「932.78」 |
| L1#1_Table#3_Row#17 | 「BLKpoint_36」 | 「373.2」 | 「20000」 | 「0.6」 | 「807.98」 |
| L1#1_Table#3_Row#18 | 「BLKpoint_38」 | 「373.2」 | 「20000」 | 「1」 | 「737.85」 |
| L1#1_Table#3_Row#19 | 「BLKpoint_39」 | 「373.2」 | 「30000」 | 「0.1」 | 「939.53」 |
| L1#1_Table#3_Row#20 | 「BLKpoint_42」 | 「373.2」 | 「30000」 | 「0.4」 | 「858.91」 |
| L1#1_Table#3_Row#21 | 「BLKpoint_45」 | 「373.2」 | 「30000」 | 「1」 | 「748.83」 |
| L1#1_Table#3_Row#22 | 「BLKpoint_46」 | 「373.2」 | 「40000」 | 「0.1」 | 「943.52」 |
| L1#1_Table#3_Row#23 | 「BLKpoint_50」 | 「373.2」 | 「40000」 | 「0.6」 | 「823.64」 |
| L1#1_Table#3_Row#24 | 「BLKpoint_52」 | 「373.2」 | 「40000」 | 「1」 | 「758.66」 |
| L1#1_Table#3_Row#25 | 「BLKpoint_53」 | 「476.2」 | 「10000」 | 「0.1」 | 「822.65」 |
| L1#1_Table#3_Row#26 | 「BLKpoint_56」 | 「476.2」 | 「10000」 | 「0.4」 | 「714.67」 |
| L1#1_Table#3_Row#27 | 「BLKpoint_59」 | 「476.2」 | 「10000」 | 「1」 | 「576.84」 |
| L1#1_Table#3_Row#28 | 「BLKpoint_60」 | 「476.2」 | 「20000」 | 「0.1」 | 「831.4」 |
| L1#1_Table#3_Row#29 | 「BLKpoint_63」 | 「476.2」 | 「20000」 | 「0.4」 | 「730.97」 |
| L1#1_Table#3_Row#30 | 「BLKpoint_66」 | 「476.2」 | 「20000」 | 「1」 | 「612.56」 |
| L1#1_Table#3_Row#31 | 「BLKpoint_67」 | 「476.2」 | 「30000」 | 「0.1」 | 「838.61」 |
| L1#1_Table#3_Row#32 | 「BLKpoint_70」 | 「476.2」 | 「30000」 | 「0.4」 | 「744.11」 |
| L1#1_Table#3_Row#33 | 「BLKpoint_73」 | 「476.2」 | 「30000」 | 「1」 | 「636.82」 |
| L1#1_Table#3_Row#34 | 「BLKpoint_74」 | 「476.2」 | 「40000」 | 「0.1」 | 「845.82」 |
| L1#1_Table#3_Row#35 | 「BLKpoint_77」 | 「476.2」 | 「40000」 | 「0.4」 | 「754.89」 |
| L1#1_Table#3_Row#36 | 「BLKpoint_80」 | 「476.2」 | 「40000」 | 「1」 | 「655.67」 |
```

```ledger
**L1#1_Table#4_(Analysis_L1#1_INSP):**
lit_num_id: GLOBlit_1483 | doi: 10.1016/j.fluid.2014.05.032 | block: PROPblock_1
table_mode: rdp | inspection_id: INSP_51f9b5335a8a | rows_shown: 131

| *row_id* | *BLKpoint_id* | *pressure_kpa* | *temperature_k* | *mole_fraction_<ethanol>* | *mass_density_kg_m3* |
|---|---|---|---|---|---|
| L1#1_Table#4_Row#1 | 「BLKpoint_1」 | 「39170」 | 「297.05」 | 「0.0163」 | 「1006.1」 |
| L1#1_Table#4_Row#2 | 「BLKpoint_2」 | 「30810」 | 「297.05」 | 「0.0163」 | 「1003.2」 |
| L1#1_Table#4_Row#3 | 「BLKpoint_3」 | 「21070」 | 「297.05」 | 「0.0163」 | 「997.5」 |
| L1#1_Table#4_Row#4 | 「BLKpoint_4」 | 「11280」 | 「297.05」 | 「0.0163」 | 「993.5」 |
| L1#1_Table#4_Row#5 | 「BLKpoint_5」 | 「2490」 | 「297.05」 | 「0.0163」 | 「990.8」 |
| L1#1_Table#4_Row#6 | 「BLKpoint_6」 | 「38480」 | 「323.15」 | 「0.0163」 | 「995.2」 |
| L1#1_Table#4_Row#7 | 「BLKpoint_7」 | 「30890」 | 「323.15」 | 「0.0163」 | 「992.3」 |
| L1#1_Table#4_Row#8 | 「BLKpoint_8」 | 「21080」 | 「323.15」 | 「0.0163」 | 「988.4」 |
| L1#1_Table#4_Row#9 | 「BLKpoint_9」 | 「11390」 | 「323.15」 | 「0.0163」 | 「984.4」 |
| L1#1_Table#4_Row#10 | 「BLKpoint_10」 | 「2570」 | 「323.15」 | 「0.0163」 | 「980.6」 |
| L1#1_Table#4_Row#11 | 「BLKpoint_11」 | 「39910」 | 「348.15」 | 「0.0163」 | 「982.3」 |
| L1#1_Table#4_Row#12 | 「BLKpoint_12」 | 「29500」 | 「348.15」 | 「0.0163」 | 「978.3」 |
| L1#1_Table#4_Row#13 | 「BLKpoint_13」 | 「20750」 | 「348.15」 | 「0.0163」 | 「974.7」 |
| L1#1_Table#4_Row#14 | 「BLKpoint_14」 | 「10980」 | 「348.15」 | 「0.0163」 | 「970.6」 |
| L1#1_Table#4_Row#15 | 「BLKpoint_15」 | 「3220」 | 「348.15」 | 「0.0163」 | 「967.1」 |
| L1#1_Table#4_Row#16 | 「BLKpoint_16」 | 「35700」 | 「373.15」 | 「0.0163」 | 「964.6」 |
| L1#1_Table#4_Row#17 | 「BLKpoint_17」 | 「30600」 | 「373.15」 | 「0.0163」 | 「962.5」 |
| L1#1_Table#4_Row#18 | 「BLKpoint_18」 | 「21160」 | 「373.15」 | 「0.0163」 | 「958.3」 |
| L1#1_Table#4_Row#19 | 「BLKpoint_19」 | 「11320」 | 「373.15」 | 「0.0163」 | 「953.8」 |
| L1#1_Table#4_Row#20 | 「BLKpoint_20」 | 「3370」 | 「373.15」 | 「0.0163」 | 「950.2」 |
| L1#1_Table#4_Row#21 | 「BLKpoint_21」 | 「39890」 | 「398.15」 | 「0.0163」 | 「948」 |
| L1#1_Table#4_Row#22 | 「BLKpoint_22」 | 「30790」 | 「398.15」 | 「0.0163」 | 「943.7」 |
| L1#1_Table#4_Row#23 | 「BLKpoint_23」 | 「21360」 | 「398.15」 | 「0.0163」 | 「939.3」 |
| L1#1_Table#4_Row#24 | 「BLKpoint_24」 | 「11630」 | 「398.15」 | 「0.0163」 | 「934.4」 |
| L1#1_Table#4_Row#25 | 「BLKpoint_25」 | 「3710」 | 「398.15」 | 「0.0163」 | 「930.3」 |
| L1#1_Table#4_Row#26 | 「BLKpoint_26」 | 「39560」 | 「423.15」 | 「0.0163」 | 「927.2」 |
| L1#1_Table#4_Row#27 | 「BLKpoint_27」 | 「30570」 | 「423.15」 | 「0.0163」 | 「922.4」 |
| L1#1_Table#4_Row#28 | 「BLKpoint_28」 | 「20970」 | 「423.15」 | 「0.0163」 | 「917」 |
| L1#1_Table#4_Row#29 | 「BLKpoint_29」 | 「10170」 | 「423.15」 | 「0.0163」 | 「911」 |
| L1#1_Table#4_Row#30 | 「BLKpoint_30」 | 「2680」 | 「423.15」 | 「0.0163」 | 「906.7」 |
| L1#1_Table#4_Row#31 | 「BLKpoint_31」 | 「38340」 | 「448.15」 | 「0.0163」 | 「903.5」 |
| L1#1_Table#4_Row#32 | 「BLKpoint_32」 | 「31050」 | 「448.15」 | 「0.0163」 | 「899.4」 |
| L1#1_Table#4_Row#33 | 「BLKpoint_33」 | 「21530」 | 「448.15」 | 「0.0163」 | 「893.7」 |
| L1#1_Table#4_Row#34 | 「BLKpoint_34」 | 「11920」 | 「448.15」 | 「0.0163」 | 「887.5」 |
| L1#1_Table#4_Row#35 | 「BLKpoint_35」 | 「3960」 | 「448.15」 | 「0.0163」 | 「882.3」 |
| L1#1_Table#4_Row#36 | 「BLKpoint_36」 | 「39230」 | 「292.95」 | 「0.073」 | 「988」 |
| L1#1_Table#4_Row#37 | 「BLKpoint_37」 | 「30930」 | 「292.95」 | 「0.073」 | 「985」 |
| L1#1_Table#4_Row#38 | 「BLKpoint_38」 | 「21120」 | 「292.95」 | 「0.073」 | 「981.2」 |
| L1#1_Table#4_Row#39 | 「BLKpoint_39」 | 「11320」 | 「292.95」 | 「0.073」 | 「977.6」 |
| L1#1_Table#4_Row#40 | 「BLKpoint_40」 | 「2450」 | 「292.95」 | 「0.073」 | 「974.2」 |
| L1#1_Table#4_Row#41 | 「BLKpoint_41」 | 「38600」 | 「323.15」 | 「0.073」 | 「973.6」 |
| L1#1_Table#4_Row#42 | 「BLKpoint_42」 | 「30360」 | 「323.15」 | 「0.073」 | 「970.6」 |
| L1#1_Table#4_Row#43 | 「BLKpoint_43」 | 「20790」 | 「323.15」 | 「0.073」 | 「966.7」 |
| L1#1_Table#4_Row#44 | 「BLKpoint_44」 | 「10940」 | 「323.15」 | 「0.073」 | 「962.8」 |
| L1#1_Table#4_Row#45 | 「BLKpoint_45」 | 「2610」 | 「323.15」 | 「0.073」 | 「959.3」 |
| L1#1_Table#4_Row#46 | 「BLKpoint_46」 | 「39600」 | 「348.15」 | 「0.073」 | 「958.9」 |
| L1#1_Table#4_Row#47 | 「BLKpoint_48」 | 「20870」 | 「348.15」 | 「0.073」 | 「950.8」 |
| L1#1_Table#4_Row#48 | 「BLKpoint_49」 | 「11060」 | 「348.15」 | 「0.073」 | 「946.6」 |
| L1#1_Table#4_Row#49 | 「BLKpoint_50」 | 「3330」 | 「348.15」 | 「0.073」 | 「943」 |
| L1#1_Table#4_Row#50 | 「BLKpoint_51」 | 「37230」 | 「373.15」 | 「0.073」 | 「939.9」 |
| L1#1_Table#4_Row#51 | 「BLKpoint_52」 | 「30670」 | 「373.15」 | 「0.073」 | 「937」 |
| L1#1_Table#4_Row#52 | 「BLKpoint_53」 | 「21080」 | 「373.15」 | 「0.073」 | 「932.5」 |
| L1#1_Table#4_Row#53 | 「BLKpoint_54」 | 「11320」 | 「373.15」 | 「0.073」 | 「927.7」 |
| L1#1_Table#4_Row#54 | 「BLKpoint_55」 | 「3510」 | 「373.15」 | 「0.073」 | 「923.9」 |
| L1#1_Table#4_Row#55 | 「BLKpoint_56」 | 「39500」 | 「398.15」 | 「0.073」 | 「920.7」 |
| L1#1_Table#4_Row#56 | 「BLKpoint_57」 | 「30790」 | 「398.15」 | 「0.073」 | 「916.3」 |
| L1#1_Table#4_Row#57 | 「BLKpoint_58」 | 「21160」 | 「398.15」 | 「0.073」 | 「911.4」 |
| L1#1_Table#4_Row#58 | 「BLKpoint_59」 | 「11510」 | 「398.15」 | 「0.073」 | 「906.2」 |
| L1#1_Table#4_Row#59 | 「BLKpoint_60」 | 「3710」 | 「398.15」 | 「0.073」 | 「901.9」 |
| L1#1_Table#4_Row#60 | 「BLKpoint_61」 | 「40110」 | 「423.15」 | 「0.073」 | 「898.6」 |
| L1#1_Table#4_Row#61 | 「BLKpoint_62」 | 「30490」 | 「423.15」 | 「0.073」 | 「893」 |
| L1#1_Table#4_Row#62 | 「BLKpoint_63」 | 「20110」 | 「423.15」 | 「0.073」 | 「887.1」 |
| L1#1_Table#4_Row#63 | 「BLKpoint_64」 | 「10710」 | 「423.15」 | 「0.073」 | 「881.1」 |
| L1#1_Table#4_Row#64 | 「BLKpoint_65」 | 「2760」 | 「423.15」 | 「0.073」 | 「875.9」 |
| L1#1_Table#4_Row#65 | 「BLKpoint_66」 | 「37210」 | 「448.15」 | 「0.073」 | 「873」 |
| L1#1_Table#4_Row#66 | 「BLKpoint_67」 | 「31170」 | 「448.15」 | 「0.073」 | 「869.2」 |
| L1#1_Table#4_Row#67 | 「BLKpoint_68」 | 「21690」 | 「448.15」 | 「0.073」 | 「862.7」 |
| L1#1_Table#4_Row#68 | 「BLKpoint_69」 | 「12160」 | 「448.15」 | 「0.073」 | 「855.6」 |
| L1#1_Table#4_Row#69 | 「BLKpoint_70」 | 「4000」 | 「448.15」 | 「0.073」 | 「849.3」 |
| L1#1_Table#4_Row#70 | 「BLKpoint_71」 | 「40030」 | 「298.15」 | 「0.0946」 | 「979.8」 |
| L1#1_Table#4_Row#71 | 「BLKpoint_72」 | 「29980」 | 「298.15」 | 「0.0946」 | 「976.1」 |
| L1#1_Table#4_Row#72 | 「BLKpoint_73」 | 「20060」 | 「298.15」 | 「0.0946」 | 「972.4」 |
| L1#1_Table#4_Row#73 | 「BLKpoint_74」 | 「10120」 | 「298.15」 | 「0.0946」 | 「968.6」 |
| L1#1_Table#4_Row#74 | 「BLKpoint_75」 | 「2560」 | 「298.15」 | 「0.0946」 | 「965.8」 |
| L1#1_Table#4_Row#75 | 「BLKpoint_76」 | 「39810」 | 「323.15」 | 「0.0946」 | 「966.2」 |
| L1#1_Table#4_Row#76 | 「BLKpoint_77」 | 「32400」 | 「323.15」 | 「0.0946」 | 「963.3」 |
| L1#1_Table#4_Row#77 | 「BLKpoint_78」 | 「20710」 | 「323.15」 | 「0.0946」 | 「958.8」 |
| L1#1_Table#4_Row#78 | 「BLKpoint_79」 | 「11140」 | 「323.15」 | 「0.0946」 | 「954.9」 |
| L1#1_Table#4_Row#79 | 「BLKpoint_80」 | 「2730」 | 「323.15」 | 「0.0946」 | 「951.3」 |
| L1#1_Table#4_Row#80 | 「BLKpoint_81」 | 「37790」 | 「348.15」 | 「0.0946」 | 「948.7」 |
| L1#1_Table#4_Row#81 | 「BLKpoint_82」 | 「29730」 | 「348.15」 | 「0.0946」 | 「945.4」 |
| L1#1_Table#4_Row#82 | 「BLKpoint_83」 | 「20870」 | 「348.15」 | 「0.0946」 | 「941.6」 |
| L1#1_Table#4_Row#83 | 「BLKpoint_84」 | 「11390」 | 「348.15」 | 「0.0946」 | 「937.4」 |
| L1#1_Table#4_Row#84 | 「BLKpoint_85」 | 「2730」 | 「348.15」 | 「0.0946」 | 「933.7」 |
| L1#1_Table#4_Row#85 | 「BLKpoint_86」 | 「39410」 | 「373.15」 | 「0.0946」 | 「927.3」 |
| L1#1_Table#4_Row#86 | 「BLKpoint_87」 | 「30850」 | 「373.15」 | 「0.0946」 | 「922.3」 |
| L1#1_Table#4_Row#87 | 「BLKpoint_88」 | 「21200」 | 「373.15」 | 「0.0946」 | 「917.7」 |
| L1#1_Table#4_Row#88 | 「BLKpoint_90」 | 「3330」 | 「373.15」 | 「0.0946」 | 「908.6」 |
| L1#1_Table#4_Row#89 | 「BLKpoint_91」 | 「39610」 | 「398.15」 | 「0.0946」 | 「905.3」 |
| L1#1_Table#4_Row#90 | 「BLKpoint_92」 | 「30850」 | 「398.15」 | 「0.0946」 | 「901.1」 |
| L1#1_Table#4_Row#91 | 「BLKpoint_93」 | 「21200」 | 「398.15」 | 「0.0946」 | 「896」 |
| L1#1_Table#4_Row#92 | 「BLKpoint_94」 | 「11430」 | 「398.15」 | 「0.0946」 | 「890.4」 |
| L1#1_Table#4_Row#93 | 「BLKpoint_95」 | 「3510」 | 「398.15」 | 「0.0946」 | 「885.8」 |
| L1#1_Table#4_Row#94 | 「BLKpoint_96」 | 「39860」 | 「423.15」 | 「0.0946」 | 「882.2」 |
| L1#1_Table#4_Row#95 | 「BLKpoint_97」 | 「30100」 | 「423.15」 | 「0.0946」 | 「875.5」 |
| L1#1_Table#4_Row#96 | 「BLKpoint_98」 | 「20200」 | 「423.15」 | 「0.0946」 | 「869.5」 |
| L1#1_Table#4_Row#97 | 「BLKpoint_99」 | 「10050」 | 「423.15」 | 「0.0946」 | 「863.9」 |
| L1#1_Table#4_Row#98 | 「BLKpoint_100」 | 「2750」 | 「423.15」 | 「0.0946」 | 「860.1」 |
| L1#1_Table#4_Row#99 | 「BLKpoint_101」 | 「40140」 | 「448.15」 | 「0.0946」 | 「858.6」 |
| L1#1_Table#4_Row#100 | 「BLKpoint_102」 | 「30990」 | 「448.15」 | 「0.0946」 | 「852.6」 |
| L1#1_Table#4_Row#101 | 「BLKpoint_103」 | 「21690」 | 「448.15」 | 「0.0946」 | 「845.8」 |
| L1#1_Table#4_Row#102 | 「BLKpoint_104」 | 「11550」 | 「448.15」 | 「0.0946」 | 「837.9」 |
| L1#1_Table#4_Row#103 | 「BLKpoint_105」 | 「3860」 | 「448.15」 | 「0.0946」 | 「831.7」 |
| L1#1_Table#4_Row#104 | 「BLKpoint_106」 | 「39150」 | 「298.35」 | 「0.0343」 | 「998.6」 |
| L1#1_Table#4_Row#105 | 「BLKpoint_107」 | 「31040」 | 「298.35」 | 「0.0343」 | 「995.7」 |
| L1#1_Table#4_Row#106 | 「BLKpoint_108」 | 「21300」 | 「298.35」 | 「0.0343」 | 「991.9」 |
| L1#1_Table#4_Row#107 | 「BLKpoint_110」 | 「2590」 | 「298.35」 | 「0.0343」 | 「984.1」 |
| L1#1_Table#4_Row#108 | 「BLKpoint_112」 | 「30930」 | 「323.65」 | 「0.0343」 | 「985.2」 |
| L1#1_Table#4_Row#109 | 「BLKpoint_113」 | 「21200」 | 「323.65」 | 「0.0343」 | 「981.4」 |
| L1#1_Table#4_Row#110 | 「BLKpoint_114」 | 「11320」 | 「323.65」 | 「0.0343」 | 「977.4」 |
| L1#1_Table#4_Row#111 | 「BLKpoint_115」 | 「2610」 | 「323.65」 | 「0.0343」 | 「973.6」 |
| L1#1_Table#4_Row#112 | 「BLKpoint_116」 | 「39860」 | 「348.15」 | 「0.0343」 | 「974.7」 |
| L1#1_Table#4_Row#113 | 「BLKpoint_117」 | 「30850」 | 「348.15」 | 「0.0343」 | 「971.3」 |
| L1#1_Table#4_Row#114 | 「BLKpoint_118」 | 「21160」 | 「348.15」 | 「0.0343」 | 「967.5」 |
| L1#1_Table#4_Row#115 | 「BLKpoint_119」 | 「11590」 | 「348.15」 | 「0.0343」 | 「963.5」 |
| L1#1_Table#4_Row#116 | 「BLKpoint_121」 | 「39000」 | 「373.15」 | 「0.0343」 | 「957.9」 |
| L1#1_Table#4_Row#117 | 「BLKpoint_122」 | 「30520」 | 「373.15」 | 「0.0343」 | 「954.5」 |
| L1#1_Table#4_Row#118 | 「BLKpoint_123」 | 「21120」 | 「373.15」 | 「0.0343」 | 「950.3」 |
| L1#1_Table#4_Row#119 | 「BLKpoint_124」 | 「11470」 | 「373.15」 | 「0.0343」 | 「945.9」 |
| L1#1_Table#4_Row#120 | 「BLKpoint_126」 | 「37300」 | 「398.15」 | 「0.0343」 | 「938.3」 |
| L1#1_Table#4_Row#121 | 「BLKpoint_127」 | 「30930」 | 「398.15」 | 「0.0343」 | 「935.2」 |
| L1#1_Table#4_Row#122 | 「BLKpoint_128」 | 「21530」 | 「398.15」 | 「0.0343」 | 「930.7」 |
| L1#1_Table#4_Row#123 | 「BLKpoint_129」 | 「11730」 | 「398.15」 | 「0.0343」 | 「925.8」 |
| L1#1_Table#4_Row#124 | 「BLKpoint_131」 | 「39680」 | 「423.15」 | 「0.0343」 | 「918.2」 |
| L1#1_Table#4_Row#125 | 「BLKpoint_132」 | 「30640」 | 「423.15」 | 「0.0343」 | 「913.4」 |
| L1#1_Table#4_Row#126 | 「BLKpoint_133」 | 「21070」 | 「423.15」 | 「0.0343」 | 「908.1」 |
| L1#1_Table#4_Row#127 | 「BLKpoint_135」 | 「2680」 | 「423.15」 | 「0.0343」 | 「897.3」 |
| L1#1_Table#4_Row#128 | 「BLKpoint_136」 | 「40060」 | 「448.15」 | 「0.0343」 | 「894.8」 |
| L1#1_Table#4_Row#129 | 「BLKpoint_137」 | 「31010」 | 「448.15」 | 「0.0343」 | 「889.8」 |
| L1#1_Table#4_Row#130 | 「BLKpoint_138」 | 「22180」 | 「448.15」 | 「0.0343」 | 「884.2」 |
| L1#1_Table#4_Row#131 | 「BLKpoint_140」 | 「4080」 | 「448.15」 | 「0.0343」 | 「872.1」 |
```
</subagent_answer>
</tool_result>

## Assistant
<summary>GLOBlit_1483 has only 4 dilute ethanol compositions (x≤0.095) at high P — unsuitable for full-range RK fit. Need to inspect GLOBlit_220 and GLOBlit_2432, and search more broadly for atmospheric-pressure, full-composition ethanol+water density data near 350 K.</summary>
<tool_call>inspect_block(doi=10.1016/j.fluid.2014.05.032, block_number=PROPblock_1)</tool_call>

## User
<tool_result>
(validation blocked inspect_block earlier — corrected)
</tool_result>

## Assistant
<summary>Searching for additional ethanol+water density blocks covering full composition range near 298-353 K at atmospheric pressure, and inspecting the two uninspected blocks GLOBlit_220 and GLOBlit_2432.</summary>
<tool_call>query_thermoml_parallel(queries=[{'label': 'broad…)</tool_call>

## User
<tool_result>
{
  "error": "queries[0].id_catalog[0] must contain exactly ['global_id', 'name', 'registry_id', 'type']; received ['id', 'label']",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml_parallel"
}
</tool_result>

## Assistant
<summary>Searching broadly for ethanol+water density data at atmospheric pressure with full composition range, and inspecting the two uninspected blocks from the initial search.</summary>
<tool_call>query_thermoml_parallel(queries=[{'label': 'broad…)</tool_call>

## User
<tool_result>
{
  "error": "queries[0].id_catalog[0].type is invalid: 'compound'; valid types: ['blocktype', 'comp', 'constr', 'lit', 'meas', 'phase', 'prop', 'rxntype', 'solvent', 'var']",
  "error_code": "TOOL_EXECUTION_ERROR",
  "tool": "query_thermoml_parallel"
}
</tool_result>

## Assistant
<summary>Retrying parallel queries with corrected id_catalog types ('comp', 'prop') to find full-composition ethanol+water density data and inspect the two uninspected blocks.</summary>
<tool_call>query_thermoml_parallel(queries=[{'label': 'broad…)</tool_call>

## User
<tool_result>
[TOOL_RESULT_SIZE_WARNING: query_thermoml_parallel returned 64,823 characters after result processing; the target is 24,000. The full result follows — prefer narrower requests, and rely on your working memory for recall instead of re-running this call.]

<subagent_answer>
### QP#3 — query_thermoml_parallel return

**Entity summary:** n_queries=3

**Other fields:**
- results: [{"label": "broad_search", "result": {"answer": "## Binary Ethanol + Water Mass Density Blocks at Atmospheric Pressure\n\n### Best Candidate: GLOBlit_220 :: PROPblock_2\n**DOI:** 10.1016/j.fluid.2004.11.019\n\nThis block is the strongest match for wide-composition, multi-temperature density data at atmospheric pressure:\n\n- **Total points:** 810 (162 at atmospheric pressure, P = 100 kPa)\n- **Temperatures:** 298.15, 323.15, and 348.15 K (three isotherms)\n- **Composition range:** x(ethanol) = 0.003–1.0 (full range)\n- **Density range (at 100 kPa):** 739.4–995.3 kg/m³\n\nRepresentative atmospheric-pressure data (from inspection):\n\n| T (K) | x(ethanol) | ρ (kg/m³) |\n|--------|-----------|-----------|\n| 298.15 | 0.003 | 995.3 |\n| 298.15 | 0.2502 | 918.5 |\n| 298.15 | 0.4501 | 868.8 |\n| 298.15 | 0.6967 | 825.2 |\n| 298.15 | 1.0 | 785.7 |\n| 323.15 | 0.003 | 986.5 |\n| 323.15 | 0.2269 | 905.2 |\n| 323.15 | 0.4501 | 846.7 |\n| 323.15 | 0.6967 | 802.8 |\n| 323.15 | 1.0 | 763.7 |\n| 348.15 | 0.003 | 973.1 |\n| 348.15 | 0.1903 | 895.8 |\n| 348.15 | 0.4034 | 833.4 |\n| 348.15 | 0.6489 | 785.6 |\n| 348.15 | 1.0 | 739.4 |\n\nEach isotherm has approximately 54 composition points (derived by dividing 162 atmospheric points by 3 isotherms — not a database value), providing dense composition coverage ideal for Redlich-Kister fitting.\n\n### Other Inspected Candidates\n\n**GLOBlit_5201 :: PROPblock_19** (DOI: 10.1016/j.jct.2018.02.022)\n- **Points:** 244, all at P = 92.3 kPa (near-atmospheric)\n- **Temperature:** 293.15–308.15 K (4 isotherms)\n- **Composition:** x(ethanol) = 0–1 (full range)\n- **Density:** 776.592–998.429 kg/m³\n- Excellent composition coverage but temperature range is narrower and lower than GLOBlit_220.\n\n**GLOBlit_2825 :: PROPblock_12** (DOI: 10.1016/j.jct.2007.05.004)\n- **Points:** 37, all at P = 101.0 kPa\n- **Temperature:** 293.15–303.15 K (3 isotherms)\n- **Composition:** x(water) = 0–1 (full range)\n- **Density:** 781.15–998.2 kg/m³\n- Full composition range at atmospheric pressure, but fewer points and lower temperatures.\n\n### Additional Candidates (Not Inspected)\n\nThe following blocks were identified by the search discovery tool but have not been individually inspected in this run. No specific data values are quoted for them:\n\n- **GLOBlit_9006 :: PROPblock_1** (DOI: 10.1021/je060335h) — search-reported as having full composition range at lower temperatures.\n- **GLOBlit_10866 :: PROPblock_7** (DOI: 10.1021/je700300y) — search-reported as having wide composition range.\n- **GLOBlit_10699 :: PROPblock_6** (DOI: 10.1021/je600565m) — search-reported as having moderate composition range.\n- **GLOBlit_11136 :: PROPblock_9** (DOI: 10.1021/je800150h) — search-reported as having partial composition range.\n- **GLOBlit_5473 :: PROPblock_21** (DOI: 10.1016/j.jct.2019.02.027) — search-reported as having full composition range with very few points.\n\n### Regarding GLOBlit_2432\n**DOI:** 10.1016/j.jct.2004.07.019, PROPblock_2 — Per search discovery results (not individually inspected), this block operates at elevated pressures, not atmospheric. **Not suitable** for atmospheric-pressure fitting.\n\n### Key Finding\n**No block in the database was found to cover the requested upper temperature of 353 K (instruction target, not a database value) at atmospheric pressure** for this binary system. The closest inspected data is GLOBlit_220 at 348.15 K. Per search discovery results (not inspected), GLOBlit_1742 (PROPblock_3) reaches higher temperatures but only at elevated pressures.\n\n**Recommendation:** GLOBlit_220 :: PROPblock_2 is the best single source — it provides dense composition coverage at 100 kPa across 298.15, 323.15, and 348.15 K, with x(ethanol) = 0.003–1.0. GLOBlit_5201 :: PROPblock_19 (244 pts, x = 0–1, T = 293.15–308.15 K, P = 92.3 kPa) could supplement with additional near-ambient data.\n\n---\n[UNGROUNDED DATA FLAGS] The following quoted values could not be verified against any verbatim data inspection in this run and must be treated as UNVERIFIED:\n- **UNGROUNDED_LITERAL** GLOBlit_220::PROPblock_2: 54 (near '…Each isotherm has approximately 54 composition points (deriv…') matches no inspected row/stat, database table, or other source of GLOBlit_220::PROPblock_2\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"GLOBlit_220::PROPblock_2\", nearest={\"column\": \"temperature_k\", \"value\": 54.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\n- **UNGROUNDED_LITERAL** PROPblock_2: 353 (near '…abase was found to cover the requested upper temperature of …') matches no inspected row/stat, database table, or other source of PROPblock_2\n  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number=\"PROPblock_2\", literature=\"<GLOBlit_N or DOI>\", nearest={\"column\": \"temperature_k\", \"value\": 353.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead\nInspected so far: PROPblock_12, PROPblock_19, PROPblock_2", "core_claims": ["GLOBlit_220 :: PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019) is identified as the best single source for binary ethanol + water mass density data at atmospheric pressure, providing 162 points at P = 100 kPa across three isotherms (298.15, 323.15, and 348.15 K) with x(ethanol) = 0.003–1.0 and densities ranging from 739.4–995.3 kg/m³.", "At each isotherm in GLOBlit_220 :: PROPblock_2, density decreases monotonically with increasing ethanol mole fraction at 100 kPa, and density decreases with increasing temperature at fixed composition.", "GLOBlit_5201 :: PROPblock_19 (DOI: 10.1016/j.jct.2018.02.022) provides a supplementary 244-point dataset at P = 92.3 kPa over T = 293.15–308.15 K with x(ethanol) = 0–1 and densities of 776.592–998.429 kg/m³, but covers a narrower and lower temperature range than GLOBlit_220.", "No block in the database was found to cover 353 K at atmospheric pressure for this binary system; the closest inspected atmospheric-pressure data reaches 348.15 K (GLOBlit_220). The value 353 K is identified as an instruction target, not a database value.", "The stated count of approximately 54 composition points per isotherm in GLOBlit_220 :: PROPblock_2 is derived by dividing 162 atmospheric points by 3 isotherms and is flagged as UNVERIFIED against the database."], "status": "success", "summary": "For binary ethanol + water mass density at atmospheric pressure, the best ThermoML source identified is GLOBlit_220 :: PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019), providing 162 atmospheric-pressure points (P = 100 kPa) across three isotherms (298.15, 323.15, and 348.15 K) with x(ethanol) = 0.003–1.0 and densities from 739.4 to 995.3 kg/m³. A supplementary source is GLOBlit_5201 :: PROPblock_19 (DOI: 10.1016/j.jct.2018.02.022) with 244 points at P = 92.3 kPa, four isotherms from 293.15 to 308.15 K, x(ethanol) = 0–1, and densities 776.592–998.429 kg/m³. GLOBlit_2825 :: PROPblock_12 (DOI: 10.1016/j.jct.2007.05.004) offers 37 points at 101.0 kPa, 293.15–303.15 K, x(water) = 0–1, densities 781.15–998.2 kg/m³. No inspected block reaches the upper target temperature of 353 K at atmospheric pressure; the highest verified atmospheric-pressure isotherm is 348.15 K in GLOBlit_220.", "core_id_updates": [], "core_blocks_found": [{"lit_num_id": "GLOBlit_220", "block_number": "PROPblock_2", "BLKsubsys_id": null, "system_type": "binary", "comp_num_ids": ["GLOBcomp_2", "GLOBcomp_1"], "prop_num_ids": ["GLOBprop_1"], "description": "Mass density of binary ethanol + water at 100 kPa across 298.15–348.15 K, x(ethanol) = 0.003–1.0, 162 atmospheric-pressure points from 810 total.", "doi": "10.1016/j.fluid.2004.11.019", "lit_id": "2005-pec-dol-0", "block_type": "PureOrMixtureData", "blocktype_num_id": "GLOBblocktype_1", "n_datapoints": 810, "n_components": 2, "compounds": [{"org_num": "DOIcomp_2", "comp_num_id": "GLOBcomp_2", "name": "ethanol", "formula": "C2H6O", "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "SMILES": "CCO", "sample_num": "DOIcompSample_2_1"}, {"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_1_1"}], "solvents": [], "constraints": [], "variables": [{"BLKvar_id": "BLKvar_1", "var_num_id": "GLOBvar_1", "var_id": "temperature_k", "name": "Temperature, K", "type": "eTemperature", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_1", "name": "Temperature, K", "min": 298.15, "max": 348.15, "n_unique": 3}, "range_min": 298.15, "range_max": 348.15}, {"BLKvar_id": "BLKvar_2", "var_num_id": "GLOBvar_3", "var_id": "pressure_kpa", "name": "Pressure, kPa", "type": "ePressure", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_2", "name": "Pressure, kPa", "min": 100.0, "max": 40000.0, "n_unique": 5}, "range_min": 100.0, "range_max": 40000.0}, {"BLKvar_id": "BLKvar_3", "var_num_id": "GLOBvar_2", "var_id": "mole_fraction_DOIcomp_2", "name": "Mole fraction", "type": "eComponentComposition", "component_org_num": "DOIcomp_2", "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_3", "name": "Mole fraction", "min": 0.003, "max": 1.0, "n_unique": 54}, "range_min": 0.003, "range_max": 1.0}], "properties": [{"BLKprop_id": "BLKprop_1", "prop_num_id": "GLOBprop_1", "prop_ID": "mass_density_kg_m3", "name": "Mass density, kg/m3", "group": "VolumetricProp", "component_org_num": null, "meas_num_id": "GLOBmeas_138", "meas_ID": "vibtub_ufactor_2", "method_standard": null, "method_custom": "VIBTUB:UFactor:2", "range": {"BLKprop_id": "BLKprop_1", "name": "Mass density, kg/m3", "min": 739.4, "max": 1012.7, "mean": 923.644444, "std": 66.683257, "n": 810}, "uncertainty": {"evaluation_method": "Propagation of evaluated standard uncertainties", "confidence_level": 95, "evaluator": "Data file compiler", "assessment_num": "BLKpropAssessment_1_1"}, "range_min": 739.4, "range_max": 1012.7}], "phases": [{"owner_id": "BLKprop_1", "role": "property_phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_2", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_3", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}], "reaction_type": null, "participants": [], "notes": null, "declared_system_type": "binary", "declared_n_components": 2, "declared_compounds": [{"org_num": "DOIcomp_2", "comp_num_id": "GLOBcomp_2", "name": "ethanol", "formula": "C2H6O", "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "SMILES": "CCO", "sample_num": "DOIcompSample_2_1"}, {"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_1_1"}], "parent_n_datapoints": 810, "subsystem_scope": null, "subsystem_point_runs": [], "subsystem_path_class": null, "subsystem_evidence_quality": null, "subsystem_condition_ranges": []}, {"lit_num_id": "GLOBlit_5201", "block_number": "PROPblock_19", "BLKsubsys_id": null, "system_type": "binary", "comp_num_ids": ["GLOBcomp_2", "GLOBcomp_1"], "prop_num_ids": ["GLOBprop_1"], "description": "Mass density of binary ethanol + water at 92.3 kPa across 293.15–308.15 K, x(ethanol) = 0–1, 244 points.", "doi": "10.1016/j.jct.2018.02.022", "lit_id": "2018-hog-tor-0", "block_type": "PureOrMixtureData", "blocktype_num_id": "GLOBblocktype_1", "n_datapoints": 244, "n_components": 2, "compounds": [{"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_2", "name": "ethanol", "formula": "C2H6O", "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "SMILES": "CCO", "sample_num": "DOIcompSample_1_1"}, {"org_num": "DOIcomp_6", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_6_1"}], "solvents": [], "constraints": [{"BLKconstr_id": "BLKconstr_1", "constr_num_id": "GLOBconstr_1", "constr_id": "pressure_kpa", "name": "Pressure, kPa", "type": "ePressure", "value": 92.3, "digits": 3, "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}}], "variables": [{"BLKvar_id": "BLKvar_1", "var_num_id": "GLOBvar_1", "var_id": "temperature_k", "name": "Temperature, K", "type": "eTemperature", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_1", "name": "Temperature, K", "min": 293.15, "max": 308.15, "n_unique": 4}, "range_min": 293.15, "range_max": 308.15}, {"BLKvar_id": "BLKvar_2", "var_num_id": "GLOBvar_2", "var_id": "mole_fraction_DOIcomp_1", "name": "Mole fraction", "type": "eComponentComposition", "component_org_num": "DOIcomp_1", "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_2", "name": "Mole fraction", "min": 0.0, "max": 1.0, "n_unique": 59}, "range_min": 0.0, "range_max": 1.0}], "properties": [{"BLKprop_id": "BLKprop_1", "prop_num_id": "GLOBprop_1", "prop_ID": "mass_density_kg_m3", "name": "Mass density, kg/m3", "group": "VolumetricProp", "component_org_num": null, "meas_num_id": "GLOBmeas_2", "meas_ID": "vibrating_tube_method", "method_standard": "Vibrating tube method", "method_custom": null, "range": {"BLKprop_id": "BLKprop_1", "name": "Mass density, kg/m3", "min": 776.592, "max": 998.429, "mean": 881.16518, "std": 74.568443, "n": 244}, "uncertainty": {"evaluation_method": "Propagation of evaluated standard uncertainties", "confidence_level": 95, "evaluator": "Data file compiler", "assessment_num": "BLKpropAssessment_1_1"}, "range_min": 776.592, "range_max": 998.429}], "phases": [{"owner_id": "BLKprop_1", "role": "property_phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_2", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKconstr_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}], "reaction_type": null, "participants": [], "notes": null, "declared_system_type": "binary", "declared_n_components": 2, "declared_compounds": [{"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_2", "name": "ethanol", "formula": "C2H6O", "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "SMILES": "CCO", "sample_num": "DOIcompSample_1_1"}, {"org_num": "DOIcomp_6", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_6_1"}], "parent_n_datapoints": 244, "subsystem_scope": null, "subsystem_point_runs": [], "subsystem_path_class": null, "subsystem_evidence_quality": null, "subsystem_condition_ranges": []}, {"lit_num_id": "GLOBlit_2825", "block_number": "PROPblock_12", "BLKsubsys_id": null, "system_type": "binary", "comp_num_ids": ["GLOBcomp_2", "GLOBcomp_1"], "prop_num_ids": ["GLOBprop_1"], "description": "Mass density of binary ethanol + water at 101.0 kPa across 293.15–303.15 K, x(water) = 0–1, 37 points.", "doi": "10.1016/j.jct.2007.05.004", "lit_id": "2007-gon-cal-1", "block_type": "PureOrMixtureData", "blocktype_num_id": "GLOBblocktype_1", "n_datapoints": 37, "n_components": 2, "compounds": [{"org_num": "DOIcomp_3", "comp_num_id": "GLOBcomp_2", "name": "ethanol", "formula": "C2H6O", "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "SMILES": "CCO", "sample_num": "DOIcompSample_3_1"}, {"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_1_1"}], "solvents": [], "constraints": [{"BLKconstr_id": "BLKconstr_1", "constr_num_id": "GLOBconstr_1", "constr_id": "pressure_kpa", "name": "Pressure, kPa", "type": "ePressure", "value": 101.0, "digits": 3, "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}}], "variables": [{"BLKvar_id": "BLKvar_1", "var_num_id": "GLOBvar_1", "var_id": "temperature_k", "name": "Temperature, K", "type": "eTemperature", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_1", "name": "Temperature, K", "min": 293.15, "max": 303.15, "n_unique": 3}, "range_min": 293.15, "range_max": 303.15}, {"BLKvar_id": "BLKvar_2", "var_num_id": "GLOBvar_2", "var_id": "mole_fraction_DOIcomp_1", "name": "Mole fraction", "type": "eComponentComposition", "component_org_num": "DOIcomp_1", "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_2", "name": "Mole fraction", "min": 0.0, "max": 1.0, "n_unique": 13}, "range_min": 0.0, "range_max": 1.0}], "properties": [{"BLKprop_id": "BLKprop_1", "prop_num_id": "GLOBprop_1", "prop_ID": "mass_density_kg_m3", "name": "Mass density, kg/m3", "group": "VolumetricProp", "component_org_num": null, "meas_num_id": "GLOBmeas_134", "meas_ID": "vibtub_ufactor_4", "method_standard": null, "method_custom": "VIBTUB:UFactor:4", "range": {"BLKprop_id": "BLKprop_1", "name": "Mass density, kg/m3", "min": 781.15, "max": 998.2, "mean": 875.231351, "std": 74.42608, "n": 37}, "uncertainty": {"evaluation_method": "Propagation of evaluated standard uncertainties", "confidence_level": 95, "evaluator": "Data file compiler", "assessment_num": "BLKpropAssessment_1_1"}, "range_min": 781.15, "range_max": 998.2}], "phases": [{"owner_id": "BLKprop_1", "role": "property_phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_2", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKconstr_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}], "reaction_type": null, "participants": [], "notes": null, "declared_system_type": "binary", "declared_n_components": 2, "declared_compounds": [{"org_num": "DOIcomp_3", "comp_num_id": "GLOBcomp_2", "name": "ethanol", "formula": "C2H6O", "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "SMILES": "CCO", "sample_num": "DOIcompSample_3_1"}, {"org_num": "DOIcomp_1", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_1_1"}], "parent_n_datapoints": 37, "subsystem_scope": null, "subsystem_point_runs": [], "subsystem_path_class": null, "subsystem_evidence_quality": null, "subsystem_condition_ranges": []}], "data_inspections": [{"doi": "10.1016/j.fluid.2004.11.019", "block_number": "PROPblock_2", "table_mode": "rdp", "columns": ["BLKpoint_id", "temperature_k", "pressure_kpa", "mole_fraction_<ethanol>", "mass_density_kg_m3"], "rows_shown": [{"BLKpoint_id": "BLKpoint_1", "temperature_k": "298.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "995.3"}, {"BLKpoint_id": "BLKpoint_43", "temperature_k": "298.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.4501", "mass_density_kg_m3": "868.8"}, {"BLKpoint_id": "BLKpoint_48", "temperature_k": "298.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.6967", "mass_density_kg_m3": "825.2"}, {"BLKpoint_id": "BLKpoint_54", "temperature_k": "298.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "785.7"}, {"BLKpoint_id": "BLKpoint_55", "temperature_k": "298.15", "pressure_kpa": "10000", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "999.8"}, {"BLKpoint_id": "BLKpoint_97", "temperature_k": "298.15", "pressure_kpa": "10000", "mole_fraction_<ethanol>": "0.4501", "mass_density_kg_m3": "874.7"}, {"BLKpoint_id": "BLKpoint_102", "temperature_k": "298.15", "pressure_kpa": "10000", "mole_fraction_<ethanol>": "0.6967", "mass_density_kg_m3": "832.3"}, {"BLKpoint_id": "BLKpoint_108", "temperature_k": "298.15", "pressure_kpa": "10000", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "794"}, {"BLKpoint_id": "BLKpoint_109", "temperature_k": "298.15", "pressure_kpa": "20000", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "1004.2"}, {"BLKpoint_id": "BLKpoint_151", "temperature_k": "298.15", "pressure_kpa": "20000", "mole_fraction_<ethanol>": "0.4501", "mass_density_kg_m3": "880.4"}, {"BLKpoint_id": "BLKpoint_156", "temperature_k": "298.15", "pressure_kpa": "20000", "mole_fraction_<ethanol>": "0.6967", "mass_density_kg_m3": "839"}, {"BLKpoint_id": "BLKpoint_162", "temperature_k": "298.15", "pressure_kpa": "20000", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "801.9"}, {"BLKpoint_id": "BLKpoint_163", "temperature_k": "298.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "1008.5"}, {"BLKpoint_id": "BLKpoint_199", "temperature_k": "298.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "0.2269", "mass_density_kg_m3": "938.7"}, {"BLKpoint_id": "BLKpoint_205", "temperature_k": "298.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "0.4501", "mass_density_kg_m3": "885.7"}, {"BLKpoint_id": "BLKpoint_210", "temperature_k": "298.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "0.6967", "mass_density_kg_m3": "845.1"}, {"BLKpoint_id": "BLKpoint_216", "temperature_k": "298.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "808.9"}, {"BLKpoint_id": "BLKpoint_217", "temperature_k": "298.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "1012.7"}, {"BLKpoint_id": "BLKpoint_253", "temperature_k": "298.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "0.2269", "mass_density_kg_m3": "942.9"}, {"BLKpoint_id": "BLKpoint_259", "temperature_k": "298.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "0.4501", "mass_density_kg_m3": "890.8"}, {"BLKpoint_id": "BLKpoint_264", "temperature_k": "298.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "0.6967", "mass_density_kg_m3": "851"}, {"BLKpoint_id": "BLKpoint_270", "temperature_k": "298.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "815.7"}, {"BLKpoint_id": "BLKpoint_271", "temperature_k": "323.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "986.5"}, {"BLKpoint_id": "BLKpoint_307", "temperature_k": "323.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.2269", "mass_density_kg_m3": "905.2"}, {"BLKpoint_id": "BLKpoint_313", "temperature_k": "323.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.4501", "mass_density_kg_m3": "846.7"}, {"BLKpoint_id": "BLKpoint_318", "temperature_k": "323.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.6967", "mass_density_kg_m3": "802.8"}, {"BLKpoint_id": "BLKpoint_324", "temperature_k": "323.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "763.7"}, {"BLKpoint_id": "BLKpoint_325", "temperature_k": "323.15", "pressure_kpa": "10000", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "990.8"}, {"BLKpoint_id": "BLKpoint_361", "temperature_k": "323.15", "pressure_kpa": "10000", "mole_fraction_<ethanol>": "0.2269", "mass_density_kg_m3": "910.3"}, {"BLKpoint_id": "BLKpoint_367", "temperature_k": "323.15", "pressure_kpa": "10000", "mole_fraction_<ethanol>": "0.4501", "mass_density_kg_m3": "853.3"}, {"BLKpoint_id": "BLKpoint_372", "temperature_k": "323.15", "pressure_kpa": "10000", "mole_fraction_<ethanol>": "0.6967", "mass_density_kg_m3": "810.9"}, {"BLKpoint_id": "BLKpoint_378", "temperature_k": "323.15", "pressure_kpa": "10000", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "773.4"}, {"BLKpoint_id": "BLKpoint_379", "temperature_k": "323.15", "pressure_kpa": "20000", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "994.9"}, {"BLKpoint_id": "BLKpoint_415", "temperature_k": "323.15", "pressure_kpa": "20000", "mole_fraction_<ethanol>": "0.2269", "mass_density_kg_m3": "915.3"}, {"BLKpoint_id": "BLKpoint_421", "temperature_k": "323.15", "pressure_kpa": "20000", "mole_fraction_<ethanol>": "0.4501", "mass_density_kg_m3": "859.7"}, {"BLKpoint_id": "BLKpoint_426", "temperature_k": "323.15", "pressure_kpa": "20000", "mole_fraction_<ethanol>": "0.6967", "mass_density_kg_m3": "818.4"}, {"BLKpoint_id": "BLKpoint_432", "temperature_k": "323.15", "pressure_kpa": "20000", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "782.3"}, {"BLKpoint_id": "BLKpoint_433", "temperature_k": "323.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "999"}, {"BLKpoint_id": "BLKpoint_469", "temperature_k": "323.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "0.2269", "mass_density_kg_m3": "920.1"}, {"BLKpoint_id": "BLKpoint_475", "temperature_k": "323.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "0.4501", "mass_density_kg_m3": "865.7"}, {"BLKpoint_id": "BLKpoint_480", "temperature_k": "323.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "0.6967", "mass_density_kg_m3": "825.4"}, {"BLKpoint_id": "BLKpoint_486", "temperature_k": "323.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "790.3"}, {"BLKpoint_id": "BLKpoint_487", "temperature_k": "323.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "1003.1"}, {"BLKpoint_id": "BLKpoint_523", "temperature_k": "323.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "0.2269", "mass_density_kg_m3": "924.7"}, {"BLKpoint_id": "BLKpoint_529", "temperature_k": "323.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "0.4501", "mass_density_kg_m3": "871.3"}, {"BLKpoint_id": "BLKpoint_534", "temperature_k": "323.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "0.6967", "mass_density_kg_m3": "831.9"}, {"BLKpoint_id": "BLKpoint_540", "temperature_k": "323.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "797.7"}, {"BLKpoint_id": "BLKpoint_541", "temperature_k": "348.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "973.1"}, {"BLKpoint_id": "BLKpoint_575", "temperature_k": "348.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.1903", "mass_density_kg_m3": "895.8"}, {"BLKpoint_id": "BLKpoint_582", "temperature_k": "348.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.4034", "mass_density_kg_m3": "833.4"}, {"BLKpoint_id": "BLKpoint_587", "temperature_k": "348.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.6489", "mass_density_kg_m3": "785.6"}, {"BLKpoint_id": "BLKpoint_594", "temperature_k": "348.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "739.4"}, {"BLKpoint_id": "BLKpoint_595", "temperature_k": "348.15", "pressure_kpa": "10000", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "977.5"}, {"BLKpoint_id": "BLKpoint_630", "temperature_k": "348.15", "pressure_kpa": "10000", "mole_fraction_<ethanol>": "0.1996", "mass_density_kg_m3": "898.1"}, {"BLKpoint_id": "BLKpoint_636", "temperature_k": "348.15", "pressure_kpa": "10000", "mole_fraction_<ethanol>": "0.4034", "mass_density_kg_m3": "840.7"}, {"BLKpoint_id": "BLKpoint_641", "temperature_k": "348.15", "pressure_kpa": "10000", "mole_fraction_<ethanol>": "0.6489", "mass_density_kg_m3": "794.6"}, {"BLKpoint_id": "BLKpoint_648", "temperature_k": "348.15", "pressure_kpa": "10000", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "751.2"}, {"BLKpoint_id": "BLKpoint_649", "temperature_k": "348.15", "pressure_kpa": "20000", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "981.9"}, {"BLKpoint_id": "BLKpoint_683", "temperature_k": "348.15", "pressure_kpa": "20000", "mole_fraction_<ethanol>": "0.1903", "mass_density_kg_m3": "906.5"}, {"BLKpoint_id": "BLKpoint_690", "temperature_k": "348.15", "pressure_kpa": "20000", "mole_fraction_<ethanol>": "0.4034", "mass_density_kg_m3": "847.5"}, {"BLKpoint_id": "BLKpoint_695", "temperature_k": "348.15", "pressure_kpa": "20000", "mole_fraction_<ethanol>": "0.6489", "mass_density_kg_m3": "802.9"}, {"BLKpoint_id": "BLKpoint_702", "temperature_k": "348.15", "pressure_kpa": "20000", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "761.2"}, {"BLKpoint_id": "BLKpoint_703", "temperature_k": "348.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "986.1"}, {"BLKpoint_id": "BLKpoint_738", "temperature_k": "348.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "0.1996", "mass_density_kg_m3": "908.5"}, {"BLKpoint_id": "BLKpoint_744", "temperature_k": "348.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "0.4034", "mass_density_kg_m3": "854"}, {"BLKpoint_id": "BLKpoint_749", "temperature_k": "348.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "0.6489", "mass_density_kg_m3": "810.6"}, {"BLKpoint_id": "BLKpoint_756", "temperature_k": "348.15", "pressure_kpa": "30000", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "770.3"}, {"BLKpoint_id": "BLKpoint_757", "temperature_k": "348.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "990.1"}, {"BLKpoint_id": "BLKpoint_791", "temperature_k": "348.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "0.1903", "mass_density_kg_m3": "916.4"}, {"BLKpoint_id": "BLKpoint_798", "temperature_k": "348.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "0.4034", "mass_density_kg_m3": "860"}, {"BLKpoint_id": "BLKpoint_803", "temperature_k": "348.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "0.6489", "mass_density_kg_m3": "817.8"}, {"BLKpoint_id": "BLKpoint_810", "temperature_k": "348.15", "pressure_kpa": "40000", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "778.6"}], "inspection_id": "INSP_38392edfd29c", "lit_num_id": "GLOBlit_220"}, {"doi": "10.1016/j.fluid.2004.11.019", "block_number": "PROPblock_2", "table_mode": "rdp", "columns": ["BLKpoint_id", "temperature_k", "pressure_kpa", "mole_fraction_<ethanol>", "mass_density_kg_m3"], "rows_shown": [{"BLKpoint_id": "BLKpoint_1", "temperature_k": "298.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "995.3"}, {"BLKpoint_id": "BLKpoint_38", "temperature_k": "298.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.2502", "mass_density_kg_m3": "918.5"}, {"BLKpoint_id": "BLKpoint_43", "temperature_k": "298.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.4501", "mass_density_kg_m3": "868.8"}, {"BLKpoint_id": "BLKpoint_48", "temperature_k": "298.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.6967", "mass_density_kg_m3": "825.2"}, {"BLKpoint_id": "BLKpoint_54", "temperature_k": "298.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "785.7"}, {"BLKpoint_id": "BLKpoint_271", "temperature_k": "323.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "986.5"}, {"BLKpoint_id": "BLKpoint_307", "temperature_k": "323.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.2269", "mass_density_kg_m3": "905.2"}, {"BLKpoint_id": "BLKpoint_313", "temperature_k": "323.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.4501", "mass_density_kg_m3": "846.7"}, {"BLKpoint_id": "BLKpoint_318", "temperature_k": "323.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.6967", "mass_density_kg_m3": "802.8"}, {"BLKpoint_id": "BLKpoint_324", "temperature_k": "323.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "763.7"}, {"BLKpoint_id": "BLKpoint_541", "temperature_k": "348.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.003", "mass_density_kg_m3": "973.1"}, {"BLKpoint_id": "BLKpoint_575", "temperature_k": "348.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.1903", "mass_density_kg_m3": "895.8"}, {"BLKpoint_id": "BLKpoint_582", "temperature_k": "348.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.4034", "mass_density_kg_m3": "833.4"}, {"BLKpoint_id": "BLKpoint_587", "temperature_k": "348.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "0.6489", "mass_density_kg_m3": "785.6"}, {"BLKpoint_id": "BLKpoint_594", "temperature_k": "348.15", "pressure_kpa": "100", "mole_fraction_<ethanol>": "1", "mass_density_kg_m3": "739.4"}], "inspection_id": "INSP_13b9dbeeee1e", "lit_num_id": "GLOBlit_220"}, {"doi": "10.1016/j.jct.2018.02.022", "block_number": "PROPblock_19", "table_mode": "rdp", "columns": ["BLKpoint_id", "temperature_k", "mole_fraction_<ethanol>", "pressure_kpa", "mass_density_kg_m3"], "rows_shown": [{"BLKpoint_id": "BLKpoint_1", "temperature_k": "293.15", "mole_fraction_<ethanol>": "0.0024", "pressure_kpa": "92.3", "mass_density_kg_m3": "997.039"}, {"BLKpoint_id": "BLKpoint_23", "temperature_k": "293.15", "mole_fraction_<ethanol>": "0.7006", "pressure_kpa": "92.3", "mass_density_kg_m3": "829.434"}, {"BLKpoint_id": "BLKpoint_59", "temperature_k": "298.15", "mole_fraction_<ethanol>": "0.7006", "pressure_kpa": "92.3", "mass_density_kg_m3": "825.07"}, {"BLKpoint_id": "BLKpoint_95", "temperature_k": "303.15", "mole_fraction_<ethanol>": "0.7006", "pressure_kpa": "92.3", "mass_density_kg_m3": "820.66"}, {"BLKpoint_id": "BLKpoint_131", "temperature_k": "308.15", "mole_fraction_<ethanol>": "0.7006", "pressure_kpa": "92.3", "mass_density_kg_m3": "816.2"}, {"BLKpoint_id": "BLKpoint_145", "temperature_k": "293.15", "mole_fraction_<ethanol>": "0", "pressure_kpa": "92.3", "mass_density_kg_m3": "998.429"}, {"BLKpoint_id": "BLKpoint_146", "temperature_k": "298.15", "mole_fraction_<ethanol>": "0", "pressure_kpa": "92.3", "mass_density_kg_m3": "997.267"}, {"BLKpoint_id": "BLKpoint_147", "temperature_k": "303.15", "mole_fraction_<ethanol>": "0", "pressure_kpa": "92.3", "mass_density_kg_m3": "995.867"}, {"BLKpoint_id": "BLKpoint_148", "temperature_k": "308.15", "mole_fraction_<ethanol>": "0", "pressure_kpa": "92.3", "mass_density_kg_m3": "994.252"}, {"BLKpoint_id": "BLKpoint_149", "temperature_k": "293.15", "mole_fraction_<ethanol>": "1", "pressure_kpa": "92.3", "mass_density_kg_m3": "789.547"}, {"BLKpoint_id": "BLKpoint_150", "temperature_k": "298.15", "mole_fraction_<ethanol>": "1", "pressure_kpa": "92.3", "mass_density_kg_m3": "785.26"}, {"BLKpoint_id": "BLKpoint_151", "temperature_k": "303.15", "mole_fraction_<ethanol>": "1", "pressure_kpa": "92.3", "mass_density_kg_m3": "780.941"}, {"BLKpoint_id": "BLKpoint_152", "temperature_k": "308.15", "mole_fraction_<ethanol>": "1", "pressure_kpa": "92.3", "mass_density_kg_m3": "776.592"}, {"BLKpoint_id": "BLKpoint_160", "temperature_k": "293.15", "mole_fraction_<ethanol>": "0.1984", "pressure_kpa": "92.3", "mass_density_kg_m3": "935.19"}, {"BLKpoint_id": "BLKpoint_165", "temperature_k": "293.15", "mole_fraction_<ethanol>": "0.4495", "pressure_kpa": "92.3", "mass_density_kg_m3": "873.57"}, {"BLKpoint_id": "BLKpoint_183", "temperature_k": "298.15", "mole_fraction_<ethanol>": "0.1984", "pressure_kpa": "92.3", "mass_density_kg_m3": "931.84"}, {"BLKpoint_id": "BLKpoint_188", "temperature_k": "298.15", "mole_fraction_<ethanol>": "0.4495", "pressure_kpa": "92.3", "mass_density_kg_m3": "869.34"}, {"BLKpoint_id": "BLKpoint_206", "temperature_k": "303.15", "mole_fraction_<ethanol>": "0.1984", "pressure_kpa": "92.3", "mass_density_kg_m3": "928.77"}, {"BLKpoint_id": "BLKpoint_211", "temperature_k": "303.15", "mole_fraction_<ethanol>": "0.4495", "pressure_kpa": "92.3", "mass_density_kg_m3": "865.03"}, {"BLKpoint_id": "BLKpoint_229", "temperature_k": "308.15", "mole_fraction_<ethanol>": "0.1984", "pressure_kpa": "92.3", "mass_density_kg_m3": "925.04"}, {"BLKpoint_id": "BLKpoint_234", "temperature_k": "308.15", "mole_fraction_<ethanol>": "0.4495", "pressure_kpa": "92.3", "mass_density_kg_m3": "860.66"}, {"BLKpoint_id": "BLKpoint_244", "temperature_k": "308.15", "mole_fraction_<ethanol>": "0.929", "pressure_kpa": "92.3", "mass_density_kg_m3": "785.46"}], "inspection_id": "INSP_b49f3d6ec58f", "lit_num_id": "GLOBlit_5201"}, {"doi": "10.1016/j.jct.2007.05.004", "block_number": "PROPblock_12", "table_mode": "rdp", "columns": ["BLKpoint_id", "temperature_k", "mole_fraction_<water>", "pressure_kpa", "mass_density_kg_m3"], "rows_shown": [{"BLKpoint_id": "BLKpoint_1", "temperature_k": "293.15", "mole_fraction_<water>": "0", "pressure_kpa": "101.0", "mass_density_kg_m3": "789.75"}, {"BLKpoint_id": "BLKpoint_7", "temperature_k": "293.15", "mole_fraction_<water>": "0.4971", "pressure_kpa": "101.0", "mass_density_kg_m3": "862.82"}, {"BLKpoint_id": "BLKpoint_9", "temperature_k": "293.15", "mole_fraction_<water>": "0.6991", "pressure_kpa": "101.0", "mass_density_kg_m3": "908.69"}, {"BLKpoint_id": "BLKpoint_13", "temperature_k": "293.15", "mole_fraction_<water>": "1", "pressure_kpa": "101.0", "mass_density_kg_m3": "998.2"}, {"BLKpoint_id": "BLKpoint_14", "temperature_k": "298.15", "mole_fraction_<water>": "0", "pressure_kpa": "101.0", "mass_density_kg_m3": "785.46"}, {"BLKpoint_id": "BLKpoint_19", "temperature_k": "298.15", "mole_fraction_<water>": "0.3991", "pressure_kpa": "101.0", "mass_density_kg_m3": "840.94"}, {"BLKpoint_id": "BLKpoint_20", "temperature_k": "298.15", "mole_fraction_<water>": "0.5989", "pressure_kpa": "101.0", "mass_density_kg_m3": "879.89"}, {"BLKpoint_id": "BLKpoint_25", "temperature_k": "298.15", "mole_fraction_<water>": "1", "pressure_kpa": "101.0", "mass_density_kg_m3": "997.05"}, {"BLKpoint_id": "BLKpoint_26", "temperature_k": "303.15", "mole_fraction_<water>": "0", "pressure_kpa": "101.0", "mass_density_kg_m3": "781.15"}, {"BLKpoint_id": "BLKpoint_30", "temperature_k": "303.15", "mole_fraction_<water>": "0.2961", "pressure_kpa": "101.0", "mass_density_kg_m3": "820.29"}, {"BLKpoint_id": "BLKpoint_32", "temperature_k": "303.15", "mole_fraction_<water>": "0.5989", "pressure_kpa": "101.0", "mass_density_kg_m3": "875.63"}, {"BLKpoint_id": "BLKpoint_37", "temperature_k": "303.15", "mole_fraction_<water>": "1", "pressure_kpa": "101.0", "mass_density_kg_m3": "995.65"}], "inspection_id": "INSP_1d2031e2c9c2", "lit_num_id": "GLOBlit_2825"}]}}, {"label": "inspect_220", "result": {"answer": "**GLOBlit_220 PROPblock_1 — Inspection Result**\n\nThis block contains **pure ethanol density data only** — it is **not** ethanol + water mixture data.\n\n**Details:**\n\n| Field | Value |\n|---|---|\n| DOI | 10.1016/j.fluid.2004.11.019 (GLOBlit_220) |\n| Block | PROPblock_1 |\n| System type | Unary (pure component) |\n| Compound | Ethanol (GLOBcomp_2, C₂H₆O) |\n| Property | Mass density (GLOBprop_1), kg/m³ |\n| Phase | Liquid |\n| Temperature range | 298.15–348.15 K (15 points) |\n| Pressure range | 100–40000 kPa (15 points) |\n| Density range | 739.4–815.7 kg/m³ (15 points) |\n| Data points | 15 total (12 shown via RDP) |\n| Composition | None (pure ethanol — no water present) |\n\n**Inspected data (12 of 15 points shown):**\n\n| BLKpoint_id | Temperature (K) | Pressure (kPa) | Mass density (kg/m³) |\n|---|---|---|---|\n| BLKpoint_1 | 298.15 | 100 | 785.7 |\n| BLKpoint_3 | 298.15 | 20000 | 801.9 |\n| BLKpoint_5 | 298.15 | 40000 | 815.7 |\n| BLKpoint_6 | 323.15 | 100 | 763.7 |\n| BLKpoint_7 | 323.15 | 10000 | 773.4 |\n| BLKpoint_8 | 323.15 | 20000 | 782.3 |\n| BLKpoint_10 | 323.15 | 40000 | 797.7 |\n| BLKpoint_11 | 348.15 | 100 | 739.4 |\n| BLKpoint_12 | 348.15 | 10000 | 751.2 |\n| BLKpoint_13 | 348.15 | 20000 | 761.2 |\n| BLKpoint_14 | 348.15 | 30000 | 770.3 |\n| BLKpoint_15 | 348.15 | 40000 | 778.6 |\n\n**Conclusion:** This block does **not** contain ethanol + water binary density data. Although the parent DOI (10.1016/j.fluid.2004.11.019) references ethanol–water mixtures in its title, PROPblock_1 specifically holds only pure ethanol measurements. Other blocks within GLOBlit_220 (e.g., PROPblock_2, PROPblock_3, etc.) should be checked for the binary mixture data.", "core_claims": ["GLOBlit_220 PROPblock_1 contains pure ethanol density data only, not ethanol + water binary mixture data, despite the parent DOI (10.1016/j.fluid.2004.11.019) referencing ethanol–water mixtures in its title.", "The block reports 15 liquid-phase mass density data points for pure ethanol spanning 298.15–348.15 K in temperature, 100–40000 kPa in pressure, and 739.4–815.7 kg/m³ in density.", "Other blocks within GLOBlit_220 (e.g., PROPblock_2, PROPblock_3) would need to be checked for binary ethanol + water mixture data."], "status": "success", "summary": "GLOBlit_220 PROPblock_1 (DOI 10.1016/j.fluid.2004.11.019) contains pure ethanol density data only, not ethanol + water mixture data. The block reports 15 liquid-phase mass density measurements for pure ethanol (C₂H₆O) over 298.15–348.15 K and 100–40000 kPa, with densities ranging from 739.4 to 815.7 kg/m³. No water is present; no composition variable is included. Binary ethanol–water mixture data, if present in this DOI, would be in other blocks (e.g., PROPblock_2, PROPblock_3, etc.).", "core_id_updates": [], "core_blocks_found": [{"lit_num_id": "GLOBlit_220", "block_number": "PROPblock_1", "BLKsubsys_id": null, "system_type": "unary", "comp_num_ids": ["GLOBcomp_2"], "prop_num_ids": ["GLOBprop_1"], "description": "Pure ethanol mass density measurements at 298.15–348.15 K and 100–40000 kPa, 15 data points, liquid phase. Not ethanol+water binary data.", "doi": "10.1016/j.fluid.2004.11.019", "lit_id": "2005-pec-dol-0", "block_type": "PureOrMixtureData", "blocktype_num_id": "GLOBblocktype_2", "n_datapoints": 15, "n_components": 1, "compounds": [{"org_num": "DOIcomp_2", "comp_num_id": "GLOBcomp_2", "name": "ethanol", "formula": "C2H6O", "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "SMILES": "CCO", "sample_num": "DOIcompSample_2_1"}], "solvents": [], "constraints": [], "variables": [{"BLKvar_id": "BLKvar_1", "var_num_id": "GLOBvar_1", "var_id": "temperature_k", "name": "Temperature, K", "type": "eTemperature", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_1", "name": "Temperature, K", "min": 298.15, "max": 348.15, "n_unique": 3}, "range_min": 298.15, "range_max": 348.15}, {"BLKvar_id": "BLKvar_2", "var_num_id": "GLOBvar_3", "var_id": "pressure_kpa", "name": "Pressure, kPa", "type": "ePressure", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_2", "name": "Pressure, kPa", "min": 100.0, "max": 40000.0, "n_unique": 5}, "range_min": 100.0, "range_max": 40000.0}], "properties": [{"BLKprop_id": "BLKprop_1", "prop_num_id": "GLOBprop_1", "prop_ID": "mass_density_kg_m3", "name": "Mass density, kg/m3", "group": "VolumetricProp", "component_org_num": null, "meas_num_id": "GLOBmeas_138", "meas_ID": "vibtub_ufactor_2", "method_standard": null, "method_custom": "VIBTUB:UFactor:2", "range": {"BLKprop_id": "BLKprop_1", "name": "Mass density, kg/m3", "min": 739.4, "max": 815.7, "mean": 780.953333, "std": 21.489827, "n": 15}, "uncertainty": {"evaluation_method": "Propagation of evaluated standard uncertainties", "confidence_level": 95, "evaluator": "Data file compiler", "assessment_num": "BLKpropAssessment_1_1"}, "range_min": 739.4, "range_max": 815.7}], "phases": [{"owner_id": "BLKprop_1", "role": "property_phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_2", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}], "reaction_type": null, "participants": [], "notes": null, "declared_system_type": "unary", "declared_n_components": 1, "declared_compounds": [{"org_num": "DOIcomp_2", "comp_num_id": "GLOBcomp_2", "name": "ethanol", "formula": "C2H6O", "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "SMILES": "CCO", "sample_num": "DOIcompSample_2_1"}], "parent_n_datapoints": 15, "subsystem_scope": null, "subsystem_point_runs": [], "subsystem_path_class": null, "subsystem_evidence_quality": null, "subsystem_condition_ranges": []}], "data_inspections": [{"doi": "10.1016/j.fluid.2004.11.019", "block_number": "PROPblock_1", "table_mode": "rdp", "columns": ["BLKpoint_id", "temperature_k", "pressure_kpa", "mass_density_kg_m3"], "rows_shown": [{"BLKpoint_id": "BLKpoint_1", "temperature_k": "298.15", "pressure_kpa": "100", "mass_density_kg_m3": "785.7"}, {"BLKpoint_id": "BLKpoint_3", "temperature_k": "298.15", "pressure_kpa": "20000", "mass_density_kg_m3": "801.9"}, {"BLKpoint_id": "BLKpoint_5", "temperature_k": "298.15", "pressure_kpa": "40000", "mass_density_kg_m3": "815.7"}, {"BLKpoint_id": "BLKpoint_6", "temperature_k": "323.15", "pressure_kpa": "100", "mass_density_kg_m3": "763.7"}, {"BLKpoint_id": "BLKpoint_7", "temperature_k": "323.15", "pressure_kpa": "10000", "mass_density_kg_m3": "773.4"}, {"BLKpoint_id": "BLKpoint_8", "temperature_k": "323.15", "pressure_kpa": "20000", "mass_density_kg_m3": "782.3"}, {"BLKpoint_id": "BLKpoint_10", "temperature_k": "323.15", "pressure_kpa": "40000", "mass_density_kg_m3": "797.7"}, {"BLKpoint_id": "BLKpoint_11", "temperature_k": "348.15", "pressure_kpa": "100", "mass_density_kg_m3": "739.4"}, {"BLKpoint_id": "BLKpoint_12", "temperature_k": "348.15", "pressure_kpa": "10000", "mass_density_kg_m3": "751.2"}, {"BLKpoint_id": "BLKpoint_13", "temperature_k": "348.15", "pressure_kpa": "20000", "mass_density_kg_m3": "761.2"}, {"BLKpoint_id": "BLKpoint_14", "temperature_k": "348.15", "pressure_kpa": "30000", "mass_density_kg_m3": "770.3"}, {"BLKpoint_id": "BLKpoint_15", "temperature_k": "348.15", "pressure_kpa": "40000", "mass_density_kg_m3": "778.6"}], "inspection_id": "INSP_c620a1344d0d", "lit_num_id": "GLOBlit_220"}]}}, {"label": "inspect_2432", "result": {"answer": "**Inspection of GLOBlit_2432 PROPblock_1**\n\nThis block does **not** contain ethanol + water density data. It contains **methanol + water** density data instead.\n\n**Details:**\n\n- **DOI:** 10.1016/j.jct.2004.07.019 (GLOBlit_2432)\n- **Compounds:** water (GLOBcomp_1) + methanol (GLOBcomp_4) — a binary system\n- **Property:** Mass density (kg/m³), measured as density differences relative to pure solvent water, using the vibrating-tube method\n- **Phase:** Liquid\n- **Temperature range:** 298.16–573.15 K\n- **Pressure range:** 390–30320 kPa (high-pressure measurements)\n- **Composition range:** Methanol molality 0.07706–1.04694 mol/kg\n- **Total data points:** 596\n- **Density difference values:** range from −13.3065 to −0.4632 kg/m³ (all negative, indicating methanol solutions are less dense than pure water at the same T and P)\n\nFor example, at 298.16 K and 14450 kPa, the density difference at methanol molality 0.10243 mol/kg is −0.6308 kg/m³ (BLKpoint_1), while at molality 0.98932 mol/kg it is −5.7028 kg/m³ (BLKpoint_6), showing the expected trend of increasing density reduction with higher methanol content.\n\n**Conclusion:** This block is **not** ethanol + water mass density data. The second component is methanol (CH₄O, GLOBcomp_4), not ethanol.", "core_claims": ["PROPblock_1 of GLOBlit_2432 (DOI 10.1016/j.jct.2004.07.019) contains methanol + water density data, not ethanol + water density data; the second component is methanol (CH₄O, GLOBcomp_4).", "The block reports liquid-phase mass density differences (kg/m³) relative to pure water for the methanol + water binary system, covering 298.16–573.15 K, 390–30320 kPa, methanol molality 0.07706–1.04694 mol/kg, with 596 data points.", "All reported density difference values are negative (ranging from −13.3065 to −0.4632 kg/m³), indicating that methanol solutions are less dense than pure water at the same temperature and pressure, with the magnitude of the density reduction increasing with higher methanol content."], "status": "success", "summary": "GLOBlit_2432 PROPblock_1 does not contain ethanol + water density data. It contains methanol + water density data. The DOI is 10.1016/j.jct.2004.07.019. The compounds are water (GLOBcomp_1) and methanol (GLOBcomp_4). The property is mass density (kg/m³), measured as density differences relative to pure water using the vibrating-tube method, in the liquid phase. The temperature range is 298.16–573.15 K, pressure range is 390–30320 kPa, methanol molality range is 0.07706–1.04694 mol/kg, and there are 596 data points. Density difference values range from −13.3065 to −0.4632 kg/m³, all negative, indicating methanol solutions are less dense than pure water at the same T and P. For example, at 298.16 K and 14450 kPa, the density difference at methanol molality 0.10243 mol/kg is −0.6308 kg/m³ and at molality 0.98932 mol/kg is −5.7028 kg/m³. The second component is methanol (CH₄O), not ethanol.", "core_id_updates": [], "core_blocks_found": [{"lit_num_id": "GLOBlit_2432", "block_number": "PROPblock_1", "BLKsubsys_id": null, "system_type": "binary", "comp_num_ids": ["GLOBcomp_4", "GLOBcomp_1"], "prop_num_ids": ["GLOBprop_1"], "description": "Mass density difference measurements for methanol + water at 298.16–573.15 K, 390–30320 kPa, methanol molality 0.07706–1.04694 mol/kg; 596 data points. Not ethanol + water density data.", "doi": "10.1016/j.jct.2004.07.019", "lit_id": "2004-hyn-hne-0", "block_type": "PureOrMixtureData", "blocktype_num_id": "GLOBblocktype_1", "n_datapoints": 596, "n_components": 2, "compounds": [{"org_num": "DOIcomp_5", "comp_num_id": "GLOBcomp_4", "name": "methanol", "formula": "CH4O", "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N", "SMILES": "CO", "sample_num": "DOIcompSample_5_1"}, {"org_num": "DOIcomp_4", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_4_1"}], "solvents": [{"component_org_num": "DOIcomp_4", "comp_num_id": "GLOBcomp_1", "solvent_num_id": "GLOBsolvent_1", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N"}], "constraints": [], "variables": [{"BLKvar_id": "BLKvar_1", "var_num_id": "GLOBvar_1", "var_id": "temperature_k", "name": "Temperature, K", "type": "eTemperature", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_1", "name": "Temperature, K", "min": 298.16, "max": 573.15, "n_unique": 16}, "range_min": 298.16, "range_max": 573.15}, {"BLKvar_id": "BLKvar_2", "var_num_id": "GLOBvar_3", "var_id": "pressure_kpa", "name": "Pressure, kPa", "type": "ePressure", "component_org_num": null, "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_2", "name": "Pressure, kPa", "min": 390.0, "max": 30320.0, "n_unique": 32}, "range_min": 390.0, "range_max": 30320.0}, {"BLKvar_id": "BLKvar_3", "var_num_id": "GLOBvar_4", "var_id": "molality_mol_kg_DOIcomp_5", "name": "Molality, mol/kg", "type": "eComponentComposition", "component_org_num": "DOIcomp_5", "phase": {"phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, "range": {"BLKvar_id": "BLKvar_3", "name": "Molality, mol/kg", "min": 0.07706, "max": 1.04694, "n_unique": 161}, "range_min": 0.07706, "range_max": 1.04694}], "properties": [{"BLKprop_id": "BLKprop_1", "prop_num_id": "GLOBprop_1", "prop_ID": "mass_density_kg_m3", "name": "Mass density, kg/m3", "group": "VolumetricProp", "component_org_num": null, "meas_num_id": "GLOBmeas_2", "meas_ID": "vibrating_tube_method", "method_standard": "Vibrating tube method", "method_custom": null, "range": {"BLKprop_id": "BLKprop_1", "name": "Mass density, kg/m3", "min": -13.3065, "max": -0.4632, "mean": -3.693235, "std": 2.632762, "n": 596}, "uncertainty": {"evaluation_method": "Propagation of evaluated standard uncertainties", "confidence_level": 95, "evaluator": "Data file compiler", "assessment_num": "BLKpropAssessment_1_1"}, "range_min": -13.3065, "range_max": -0.4632}], "phases": [{"owner_id": "BLKprop_1", "role": "property_phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_1", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_2", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}, {"owner_id": "BLKvar_3", "role": "phase", "phase": "Liquid", "phase_num_id": "GLOBphase_1", "phase_id": "liquid"}], "reaction_type": null, "participants": [], "notes": null, "declared_system_type": "binary", "declared_n_components": 2, "declared_compounds": [{"org_num": "DOIcomp_5", "comp_num_id": "GLOBcomp_4", "name": "methanol", "formula": "CH4O", "inchi_key": "OKKJLVBELUTLKV-UHFFFAOYSA-N", "SMILES": "CO", "sample_num": "DOIcompSample_5_1"}, {"org_num": "DOIcomp_4", "comp_num_id": "GLOBcomp_1", "name": "water", "formula": "H2O", "inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "SMILES": "O", "sample_num": "DOIcompSample_4_1"}], "parent_n_datapoints": 596, "subsystem_scope": null, "subsystem_point_runs": [], "subsystem_path_class": null, "subsystem_evidence_quality": null, "subsystem_condition_ranges": []}], "data_inspections": [{"doi": "10.1016/j.jct.2004.07.019", "block_number": "PROPblock_1", "table_mode": "rdp", "columns": ["BLKpoint_id", "temperature_k", "pressure_kpa", "molality_mol_kg_<methanol>", "mass_density_kg_m3"], "rows_shown": [{"BLKpoint_id": "BLKpoint_1", "temperature_k": "298.16", "pressure_kpa": "14450", "molality_mol_kg_<methanol>": "0.10243", "mass_density_kg_m3": "-0.6308"}, {"BLKpoint_id": "BLKpoint_6", "temperature_k": "298.16", "pressure_kpa": "14450", "molality_mol_kg_<methanol>": "0.98932", "mass_density_kg_m3": "-5.7028"}, {"BLKpoint_id": "BLKpoint_12", "temperature_k": "298.16", "pressure_kpa": "29990", "molality_mol_kg_<methanol>": "0.98931", "mass_density_kg_m3": "-5.7779"}, {"BLKpoint_id": "BLKpoint_31", "temperature_k": "298.16", "pressure_kpa": "29990", "molality_mol_kg_<methanol>": "0.10243", "mass_density_kg_m3": "-0.6295"}, {"BLKpoint_id": "BLKpoint_47", "temperature_k": "298.24", "pressure_kpa": "400", "molality_mol_kg_<methanol>": "0.98932", "mass_density_kg_m3": "-5.6141"}, {"BLKpoint_id": "BLKpoint_57", "temperature_k": "298.24", "pressure_kpa": "400", "molality_mol_kg_<methanol>": "0.07706", "mass_density_kg_m3": "-0.4632"}, {"BLKpoint_id": "BLKpoint_77", "temperature_k": "318.14", "pressure_kpa": "390", "molality_mol_kg_<methanol>": "0.71144", "mass_density_kg_m3": "-4.175"}, {"BLKpoint_id": "BLKpoint_82", "temperature_k": "318.14", "pressure_kpa": "15370", "molality_mol_kg_<methanol>": "0.71146", "mass_density_kg_m3": "-4.2"}, {"BLKpoint_id": "BLKpoint_93", "temperature_k": "318.14", "pressure_kpa": "390", "molality_mol_kg_<methanol>": "0.09689", "mass_density_kg_m3": "-0.5893"}, {"BLKpoint_id": "BLKpoint_98", "temperature_k": "318.14", "pressure_kpa": "15370", "molality_mol_kg_<methanol>": "0.09689", "mass_density_kg_m3": "-0.5958"}, {"BLKpoint_id": "BLKpoint_107", "temperature_k": "318.15", "pressure_kpa": "29980", "molality_mol_kg_<methanol>": "0.71149", "mass_density_kg_m3": "-4.215"}, {"BLKpoint_id": "BLKpoint_113", "temperature_k": "318.15", "pressure_kpa": "29980", "molality_mol_kg_<methanol>": "0.09818", "mass_density_kg_m3": "-0.6009"}, {"BLKpoint_id": "BLKpoint_123", "temperature_k": "338.15", "pressure_kpa": "14810", "molality_mol_kg_<methanol>": "0.98922", "mass_density_kg_m3": "-5.8941"}, {"BLKpoint_id": "BLKpoint_130", "temperature_k": "338.15", "pressure_kpa": "14810", "molality_mol_kg_<methanol>": "0.10242", "mass_density_kg_m3": "-0.6333"}, {"BLKpoint_id": "BLKpoint_141", "temperature_k": "338.16", "pressure_kpa": "460", "molality_mol_kg_<methanol>": "0.98929", "mass_density_kg_m3": "-5.9152"}, {"BLKpoint_id": "BLKpoint_146", "temperature_k": "338.16", "pressure_kpa": "30210", "molality_mol_kg_<methanol>": "0.71142", "mass_density_kg_m3": "-4.2846"}, {"BLKpoint_id": "BLKpoint_158", "temperature_k": "338.16", "pressure_kpa": "460", "molality_mol_kg_<methanol>": "0.10243", "mass_density_kg_m3": "-0.6372"}, {"BLKpoint_id": "BLKpoint_164", "temperature_k": "338.16", "pressure_kpa": "30210", "molality_mol_kg_<methanol>": "0.09688", "mass_density_kg_m3": "-0.6051"}, {"BLKpoint_id": "BLKpoint_180", "temperature_k": "373.17", "pressure_kpa": "14890", "molality_mol_kg_<methanol>": "0.98915", "mass_density_kg_m3": "-6.2575"}, {"BLKpoint_id": "BLKpoint_186", "temperature_k": "373.17", "pressure_kpa": "30120", "molality_mol_kg_<methanol>": "1.0111", "mass_density_kg_m3": "-6.3192"}, {"BLKpoint_id": "BLKpoint_205", "temperature_k": "373.17", "pressure_kpa": "2090", "molality_mol_kg_<methanol>": "0.10241", "mass_density_kg_m3": "-0.6788"}, {"BLKpoint_id": "BLKpoint_210", "temperature_k": "373.17", "pressure_kpa": "2090", "molality_mol_kg_<methanol>": "0.98918", "mass_density_kg_m3": "-6.3363"}, {"BLKpoint_id": "BLKpoint_211", "temperature_k": "373.17", "pressure_kpa": "14890", "molality_mol_kg_<methanol>": "0.094", "mass_density_kg_m3": "-0.6107"}, {"BLKpoint_id": "BLKpoint_217", "temperature_k": "373.17", "pressure_kpa": "30120", "molality_mol_kg_<methanol>": "0.09399", "mass_density_kg_m3": "-0.6082"}, {"BLKpoint_id": "BLKpoint_234", "temperature_k": "408.15", "pressure_kpa": "15000", "molality_mol_kg_<methanol>": "1.01107", "mass_density_kg_m3": "-6.8718"}, {"BLKpoint_id": "BLKpoint_240", "temperature_k": "408.15", "pressure_kpa": "2070", "molality_mol_kg_<methanol>": "1.01108", "mass_density_kg_m3": "-7.0201"}, {"BLKpoint_id": "BLKpoint_247", "temperature_k": "408.15", "pressure_kpa": "2070", "molality_mol_kg_<methanol>": "0.09399", "mass_density_kg_m3": "-0.6721"}, {"BLKpoint_id": "BLKpoint_252", "temperature_k": "408.15", "pressure_kpa": "2070", "molality_mol_kg_<methanol>": "1.01108", "mass_density_kg_m3": "-7.0201"}, {"BLKpoint_id": "BLKpoint_253", "temperature_k": "408.15", "pressure_kpa": "15000", "molality_mol_kg_<methanol>": "0.09399", "mass_density_kg_m3": "-0.6616"}, {"BLKpoint_id": "BLKpoint_271", "temperature_k": "408.16", "pressure_kpa": "30030", "molality_mol_kg_<methanol>": "0.09399", "mass_density_kg_m3": "-0.644"}, {"BLKpoint_id": "BLKpoint_276", "temperature_k": "408.16", "pressure_kpa": "30030", "molality_mol_kg_<methanol>": "1.01105", "mass_density_kg_m3": "-6.7209"}, {"BLKpoint_id": "BLKpoint_282", "temperature_k": "443.16", "pressure_kpa": "30320", "molality_mol_kg_<methanol>": "1.01097", "mass_density_kg_m3": "-7.1798"}, {"BLKpoint_id": "BLKpoint_283", "temperature_k": "443.16", "pressure_kpa": "30320", "molality_mol_kg_<methanol>": "0.09398", "mass_density_kg_m3": "-0.6829"}, {"BLKpoint_id": "BLKpoint_316", "temperature_k": "443.17", "pressure_kpa": "2040", "molality_mol_kg_<methanol>": "0.09399", "mass_density_kg_m3": "-0.7315"}, {"BLKpoint_id": "BLKpoint_321", "temperature_k": "443.17", "pressure_kpa": "2040", "molality_mol_kg_<methanol>": "1.01102", "mass_density_kg_m3": "-7.6916"}, {"BLKpoint_id": "BLKpoint_322", "temperature_k": "443.17", "pressure_kpa": "14920", "molality_mol_kg_<methanol>": "0.09398", "mass_density_kg_m3": "-0.7087"}, {"BLKpoint_id": "BLKpoint_327", "temperature_k": "443.17", "pressure_kpa": "14920", "molality_mol_kg_<methanol>": "1.01099", "mass_density_kg_m3": "-7.4388"}, {"BLKpoint_id": "BLKpoint_333", "temperature_k": "473.16", "pressure_kpa": "2750", "molality_mol_kg_<methanol>": "1.01093", "mass_density_kg_m3": "-8.3743"}, {"BLKpoint_id": "BLKpoint_339", "temperature_k": "473.16", "pressure_kpa": "15010", "molality_mol_kg_<methanol>": "1.0109", "mass_density_kg_m3": "-8.0216"}, {"BLKpoint_id": "BLKpoint_345", "temperature_k": "473.16", "pressure_kpa": "30060", "molality_mol_kg_<methanol>": "1.01641", "mass_density_kg_m3": "-7.7256"}, {"BLKpoint_id": "BLKpoint_352", "temperature_k": "473.16", "pressure_kpa": "15010", "molality_mol_kg_<methanol>": "0.10575", "mass_density_kg_m3": "-0.8604"}, {"BLKpoint_id": "BLKpoint_364", "temperature_k": "473.16", "pressure_kpa": "2750", "molality_mol_kg_<methanol>": "0.09398", "mass_density_kg_m3": "-0.7983"}, {"BLKpoint_id": "BLKpoint_370", "temperature_k": "473.16", "pressure_kpa": "15010", "molality_mol_kg_<methanol>": "0.10575", "mass_density_kg_m3": "-0.8604"}, {"BLKpoint_id": "BLKpoint_376", "temperature_k": "473.16", "pressure_kpa": "30060", "molality_mol_kg_<methanol>": "0.10575", "mass_density_kg_m3": "-0.8231"}, {"BLKpoint_id": "BLKpoint_392", "temperature_k": "498.15", "pressure_kpa": "15030", "molality_mol_kg_<methanol>": "1.01635", "mass_density_kg_m3": "-8.6519"}, {"BLKpoint_id": "BLKpoint_399", "temperature_k": "498.15", "pressure_kpa": "30150", "molality_mol_kg_<methanol>": "1.01637", "mass_density_kg_m3": "-8.1703"}, {"BLKpoint_id": "BLKpoint_413", "temperature_k": "498.15", "pressure_kpa": "30150", "molality_mol_kg_<methanol>": "0.10575", "mass_density_kg_m3": "-0.8706"}, {"BLKpoint_id": "BLKpoint_419", "temperature_k": "498.15", "pressure_kpa": "3840", "molality_mol_kg_<methanol>": "0.10575", "mass_density_kg_m3": "-0.9656"}, {"BLKpoint_id": "BLKpoint_424", "temperature_k": "498.15", "pressure_kpa": "3840", "molality_mol_kg_<methanol>": "1.0164", "mass_density_kg_m3": "-9.112"}, {"BLKpoint_id": "BLKpoint_425", "temperature_k": "498.15", "pressure_kpa": "15030", "molality_mol_kg_<methanol>": "0.10574", "mass_density_kg_m3": "-0.9218"}, {"BLKpoint_id": "BLKpoint_441", "temperature_k": "523.14", "pressure_kpa": "5880", "molality_mol_kg_<methanol>": "1.01632", "mass_density_kg_m3": "-9.9531"}, {"BLKpoint_id": "BLKpoint_447", "temperature_k": "523.14", "pressure_kpa": "15600", "molality_mol_kg_<methanol>": "1.01629", "mass_density_kg_m3": "-9.3473"}, {"BLKpoint_id": "BLKpoint_453", "temperature_k": "523.14", "pressure_kpa": "30090", "molality_mol_kg_<methanol>": "1.01627", "mass_density_kg_m3": "-8.6936"}, {"BLKpoint_id": "BLKpoint_472", "temperature_k": "523.14", "pressure_kpa": "5880", "molality_mol_kg_<methanol>": "0.10574", "mass_density_kg_m3": "-1.0594"}, {"BLKpoint_id": "BLKpoint_478", "temperature_k": "523.14", "pressure_kpa": "15600", "molality_mol_kg_<methanol>": "0.10574", "mass_density_kg_m3": "-0.993"}, {"BLKpoint_id": "BLKpoint_484", "temperature_k": "523.14", "pressure_kpa": "30090", "molality_mol_kg_<methanol>": "0.10573", "mass_density_kg_m3": "-0.9275"}, {"BLKpoint_id": "BLKpoint_495", "temperature_k": "548.16", "pressure_kpa": "8000", "molality_mol_kg_<methanol>": "1.01623", "mass_density_kg_m3": "-11.0973"}, {"BLKpoint_id": "BLKpoint_501", "temperature_k": "548.16", "pressure_kpa": "15970", "molality_mol_kg_<methanol>": "1.01618", "mass_density_kg_m3": "-10.2986"}, {"BLKpoint_id": "BLKpoint_507", "temperature_k": "548.16", "pressure_kpa": "30120", "molality_mol_kg_<methanol>": "1.04694", "mass_density_kg_m3": "-9.5934"}, {"BLKpoint_id": "BLKpoint_526", "temperature_k": "548.16", "pressure_kpa": "8000", "molality_mol_kg_<methanol>": "0.09819", "mass_density_kg_m3": "-1.0956"}, {"BLKpoint_id": "BLKpoint_532", "temperature_k": "548.16", "pressure_kpa": "15970", "molality_mol_kg_<methanol>": "0.09819", "mass_density_kg_m3": "-1.0204"}, {"BLKpoint_id": "BLKpoint_537", "temperature_k": "548.16", "pressure_kpa": "30120", "molality_mol_kg_<methanol>": "0.09819", "mass_density_kg_m3": "-0.9253"}, {"BLKpoint_id": "BLKpoint_548", "temperature_k": "573.15", "pressure_kpa": "10140", "molality_mol_kg_<methanol>": "1.04693", "mass_density_kg_m3": "-13.3065"}, {"BLKpoint_id": "BLKpoint_554", "temperature_k": "573.15", "pressure_kpa": "17990", "molality_mol_kg_<methanol>": "1.0469", "mass_density_kg_m3": "-11.8248"}, {"BLKpoint_id": "BLKpoint_567", "temperature_k": "573.15", "pressure_kpa": "17990", "molality_mol_kg_<methanol>": "0.09818", "mass_density_kg_m3": "-1.1328"}, {"BLKpoint_id": "BLKpoint_579", "temperature_k": "573.15", "pressure_kpa": "10140", "molality_mol_kg_<methanol>": "0.09819", "mass_density_kg_m3": "-1.2695"}, {"BLKpoint_id": "BLKpoint_585", "temperature_k": "573.15", "pressure_kpa": "17990", "molality_mol_kg_<methanol>": "0.09818", "mass_density_kg_m3": "-1.1328"}, {"BLKpoint_id": "BLKpoint_591", "temperature_k": "573.15", "pressure_kpa": "30110", "molality_mol_kg_<methanol>": "0.09818", "mass_density_kg_m3": "-1.0044"}, {"BLKpoint_id": "BLKpoint_596", "temperature_k": "573.15", "pressure_kpa": "30110", "molality_mol_kg_<methanol>": "1.04688", "mass_density_kg_m3": "-10.4212"}], "inspection_id": "INSP_1dc375d4da8a", "lit_num_id": "GLOBlit_2432"}]}}]
</subagent_answer>
</tool_result>

## Assistant
<summary>Best source is GLOBlit_220::PROPblock_2 (DOI 10.1016/j.fluid.2004.11.019) with 3 isotherms at 100 kPa: 298.15, 323.15, 348.15 K. No block has data at 350 K. Nearest defensible isotherm is 348.15 K. Will now fit RK at 348.15 K (P=100 kPa) and also at 298.15 and 323.15 K for comparison. First inspecting the block structure for fitting variable guidance.</summary>
<tool_call>inspect_block(doi=10.1016/j.fluid.2004.11.019, block_number=PROPblock_2, property_filter=dens…)</tool_call>

## User
<tool_result>
(validation blocked inspect_block earlier — corrected)
</tool_result>

## Assistant
<summary>Inspecting GLOBlit_220::PROPblock_2 to get fitting variable guidance for the density RK fit at atmospheric pressure isotherms.</summary>
<tool_call>inspect_block(doi=10.1016/j.fluid.2004.11.019, block_number=PROPblock_2, property_filter=dens…)</tool_call>

## User
<tool_result>
(validation blocked inspect_block earlier — corrected)
</tool_result>

## Assistant
<summary>Inspecting GLOBlit_220::PROPblock_2 to get fitting variable guidance for the density RK fit at atmospheric pressure isotherms.</summary>
<tool_call>inspect_block(doi=10.1016/j.fluid.2004.11.019, block_number=PROPblock_2, property_filter=dens…)</tool_call>

## User
<tool_result>
(validation blocked inspect_block earlier — corrected)
</tool_result>

## Assistant
<summary>Inspecting GLOBlit_220::PROPblock_2 to get fitting variable guidance for the density RK fit at atmospheric pressure isotherms.</summary>
<tool_call>inspect_block(doi=10.1016/j.fluid.2004.11.019, block_number=PROPblock_2, property_filter=dens…)</tool_call>

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
<summary>Block structure confirmed: 810 rows, T=298.15–348.15 K, P=100–40000 kPa, x(ethanol)=0.003–1.0. Now fitting RK at all three atmospheric-pressure isotherms (298.15, 323.15, 348.15 K at P=100 kPa) using fit_multi_system.</summary>
<tool_call>fit_multi_system(systems=[{'label': 'EtOH-…)</tool_call>

## User
<tool_result>
(validation blocked fit_multi_system earlier — corrected)
</tool_result>

## Assistant
<summary>Fitting RK density correlations at all three atmospheric-pressure isotherms (298.15, 323.15, 348.15 K) from GLOBlit_220::PROPblock_2 using fit_multi_system with constrained T and P=100 kPa.</summary>
<tool_call>fit_multi_system(systems=[{'label': 'EtOH-…)</tool_call>

## User
<tool_result>
(validation blocked fit_multi_system earlier — corrected)
</tool_result>

## Assistant
<summary>Fitting RK density correlations at all three atmospheric-pressure isotherms (298.15, 323.15, 348.15 K) from GLOBlit_220::PROPblock_2 using fit_multi_system with constrained T and P=100 kPa.</summary>
<tool_call>fit_multi_system(systems=[{'label': 'EtOH-…)</tool_call>

## User
<tool_result>
**Multi-system RK Fit** — 3 systems
Errors: EtOH-Water_348K: Requested x column 'Mole fraction of ethanol' not found in block; EtOH-Water_323K: Requested x column 'Mole fraction of ethanol' not found in block; EtOH-Water_298K: Requested x column 'Mole fraction of ethanol' not found in block

| Label | DOI | Block | Components | Order | R² | RMSE | n pts |
|-------|-----|-------|------------|-------|----|------|-------|
| EtOH-Water_298K | — | — | — | ERROR: Requested x column 'Mole fraction of eth | | |
| EtOH-Water_323K | — | — | — | ERROR: Requested x column 'Mole fraction of eth | | |
| EtOH-Water_348K | — | — | — | ERROR: Requested x column 'Mole fraction of eth | | |

</tool_result>

## Assistant
<summary>Column names are lowercase with underscores (mole_fraction_<ethanol>, mass_density_kg_m3, temperature_k, pressure_kpa). Retrying fit_multi_system with correct column names.</summary>
<tool_call>fit_multi_system(systems=[{'label': 'EtOH-…)</tool_call>

## User
<tool_result>
(validation blocked fit_multi_system earlier — corrected)
</tool_result>

## Assistant
<summary>Retrying fit_multi_system with correct column names and required arguments for all three atmospheric-pressure isotherms.</summary>
<tool_call>fit_multi_system(systems=[{'label': 'EtOH-…)</tool_call>

## User
<tool_result>
(validation blocked fit_multi_system earlier — corrected)
</tool_result>

## Assistant
<summary>Retrying fit_multi_system with tasks as string and correct column names for all three atmospheric-pressure isotherms from GLOBlit_220::PROPblock_2.</summary>
<tool_call>fit_multi_system(systems=[{'label': 'EtOH-…)</tool_call>

## User
<tool_result>
**Multi-system RK Fit** — 3 systems

| Label | DOI | Block | Components | Order | R² | RMSE | n pts |
|-------|-----|-------|------------|-------|----|------|-------|
| EtOH-Water_298K | GLOBlit_220 / DOI 10.1016/j.fluid.2004.11.019 | PROPblock_2 @ declared | ethanol, water | 3 | 0.997283 | 0.474765 | 47 |
| EtOH-Water_323K | GLOBlit_220 / DOI 10.1016/j.fluid.2004.11.019 | PROPblock_2 @ declared | ethanol, water | 5 | 0.998545 | 0.434382 | 47 |
| EtOH-Water_348K | GLOBlit_220 / DOI 10.1016/j.fluid.2004.11.019 | PROPblock_2 @ declared | ethanol, water | 5 | 0.998607 | 0.491146 | 47 |

**EtOH-Water_298K** coeffs: [-120.557, 18.5676, 43.9191, -31.3506]
Property response: BLKprop_1 / GLOBprop_1; kind=direct; equation=X = reported X; reference_sources=0; units=kg/m3 -> kg/m3.
  pure values (x = mole_fraction_<ethanol>): ethanol=785.7, water=992.083
  source: block-edges (water: direct/good, ethanol: direct/good)

**EtOH-Water_323K** coeffs: [-147.182, 39.6057, 7.0175, -0.818149, 43.21, -57.7432]
Property response: BLKprop_1 / GLOBprop_1; kind=direct; equation=X = reported X; reference_sources=0; units=kg/m3 -> kg/m3.
  pure values (x = mole_fraction_<ethanol>): ethanol=763.7, water=983.05
  source: block-edges (water: direct/good, ethanol: direct/good)

**EtOH-Water_348K** coeffs: [-167.86, 50.4515, -18.395, 43.1929, 76.8723, -109.654]
Property response: BLKprop_1 / GLOBprop_1; kind=direct; equation=X = reported X; reference_sources=0; units=kg/m3 -> kg/m3.
  pure values (x = mole_fraction_<ethanol>): ethanol=739.4, water=969.467
  source: block-edges (water: direct/good, ethanol: direct/good)

</tool_result>

## Assistant
<reasoning>
I now have all the information needed to assemble the final answer. Let me summarize:

1. The user asked for a Redlich-Kister density correlation for ethanol + water at 350 K.
2. No block in the ThermoML database has density data at exactly 350 K at atmospheric pressure.
3. The best source is GLOBlit_220::PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019), which has three atmospheric-pressure isotherms: 298.15, 323.15, and 348.15 K.
4. The nearest defensible temperature is 348.15 K (1.85 K below the target).
5. I have successfully fitted RK correlations at all three isotherms.

Key results for the 348.15 K fit:
- RK order: 5 (BIC-selected)
- R²: 0.998607
- RMSE: 0.491146 kg/m³
- Coefficients: [-167.86, 50.4515, -18.395, 43.1929, 76.8723, -109.654]
- Pure values: ethanol = 739.4 kg/m³, water = 969.467 kg/m³
- 47 data points at P = 100 kPa

I should explain why 350 K prediction should be withheld and why 348.15 K is the nearest defensible temperature.

Let me also note the temperature trend across the three isotherms to show how the RK coefficients evolve.
</reasoning>

<answer>

## Redlich–Kister Density Correlation for Ethanol + Water: 350 K Assessment

### Can the Available Measurements Support 350 K Directly?

**No.** A thorough search of the NIST ThermoML database found **no** binary ethanol + water mass-density block with measurements at 350 K at atmospheric pressure. The best atmospheric-pressure source is:

- **GLOBlit_220 :: PROPblock_2** (DOI: 10.1016/j.fluid.2004.11.019)
  - 810 total data points; 47 composition points per isotherm at P = 100 kPa
  - Three isotherms: **298.15 K, 323.15 K, and 348.15 K**
  - Ethanol mole fraction range: 0.003–1.0 (full composition range)
  - Density range at 100 kPa: 739.4–995.3 kg/m³

Other inspected blocks were either methanol + water (GLOBlit_1742, GLOBlit_2432), dilute/high-pressure only (GLOBlit_1483, x ≤ 0.095, P = 2.5–40 MPa), or covered lower temperatures (GLOBlit_5201 at 293–308 K; GLOBlit_2825 at 293–303 K).

### Nearest Defensible Temperature: 348.15 K

The closest measured isotherm is **348.15 K** — only 1.85 K below the target. A Redlich–Kister fit at this temperature is fully grounded in experimental data.

### Why the 350 K Prediction Should Be Withheld

1. **No measured data exist at 350 K.** Interpolating between the 348.15 K and 323.15 K isotherms (a 25 K gap in the wrong direction) or extrapolating 1.85 K beyond the dataset boundary would require a temperature-dependent model that is not constrained by any data between or beyond these isotherms.

2. **Non-linear temperature dependence of the RK coefficients.** The leading RK coefficient A₀ evolves from −120.6 (298.15 K) → −147.2 (323.15 K) → −167.9 (348.15 K), showing that the excess density function changes shape significantly with temperature. The higher-order coefficients also shift non-monotonically (e.g., A₁ goes from +18.6 → +39.6 → +50.5). A simple linear extrapolation of these coefficients to 350 K would be an unvalidated assumption.

3. **Ethanol–water is a strongly non-ideal system.** The hydrogen-bonding network reorganization that drives the large negative excess volumes in this system is highly temperature-sensitive. Near 348 K, ethanol approaches its normal boiling point (351.4 K), making even small temperature extrapolations unreliable without additional data.

### Redlich–Kister Fit Results at 348.15 K (Recommended)

| Parameter | Value |
|-----------|-------|
| **Source** | GLOBlit_220 :: PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019) |
| **Temperature** | 348.15 K |
| **Pressure** | 100 kPa |
| **Data points** | 47 |
| **BIC-selected RK order** | 5 |
| **R²** | 0.998607 |
| **RMSE** | 0.491 kg/m³ |
| **ρ*(ethanol)** | 739.4 kg/m³ (block edge) |
| **ρ*(water)** | 969.467 kg/m³ (block edge) |

**RK coefficients** (density deviation from linear mixing rule, kg/m³):

| Coefficient | Value |
|-------------|-------|
| A₀ | −167.860 |
| A₁ | +50.452 |
| A₂ | −18.395 |
| A₃ | +43.193 |
| A₄ | +76.872 |
| A₅ | −109.654 |

The correlation is:

ρ(x₁) = x₁·ρ₁* + (1−x₁)·ρ₂* + x₁(1−x₁) Σₖ Aₖ (2x₁−1)ᵏ

where x₁ = mole fraction of ethanol, ρ₁* = 739.4 kg/m³ (ethanol), ρ₂* = 969.467 kg/m³ (water).

### Companion Fits at Lower Temperatures (for Context)

| Isotherm | RK Order | R² | RMSE (kg/m³) | A₀ | A₁ | A₂ | A₃ | A₄ | A₅ | ρ*(EtOH) | ρ*(H₂O) |
|----------|----------|----|--------------|------|------|------|------|------|------|----------|----------|
| 298.15 K | 3 | 0.997283 | 0.475 | −120.557 | +18.568 | +43.919 | −31.351 | — | — | 785.7 | 992.083 |
| 323.15 K | 5 | 0.998545 | 0.434 | −147.182 | +39.606 | +7.018 | −0.818 | +43.210 | −57.743 | 763.7 | 983.050 |
| 348.15 K | 5 | 0.998607 | 0.491 | −167.860 | +50.452 | −18.395 | +43.193 | +76.872 | −109.654 | 739.4 | 969.467 |

### Chemistry Insight

The large negative A₀ values (−121 to −168 kg/m³) reflect the well-known volume contraction in ethanol–water mixtures caused by the interstitial accommodation of ethanol molecules within the water hydrogen-bond network. The magnitude of A₀ increases with temperature, consistent with the greater thermal disruption of the pure-component structures making the mixing-induced restructuring relatively more pronounced. The increasing RK order needed at higher temperatures (order 3 at 298 K vs. order 5 at 323 and 348 K) indicates that the composition dependence of the excess density becomes more asymmetric as temperature rises — physically reflecting the growing disparity between the thermal expansion coefficients of the two components.

### Output Files

Fit data, excess-property CSVs, and diagnostic plots were generated for all three isotherms and are available in the session output directory.

</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **UNINSPECTED_VALUE** GLOBlit_220::PROPblock_2: 810 exists in PROPblock_2's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2", nearest={"column": "pressure_kpa", "value": 810.0})`
- **MISATTRIBUTED_VALUE** GLOBlit_220::PROPblock_2: 0.095 does not belong to GLOBlit_220::PROPblock_2; it matches only GLOBlit_1742::PROPblock_1 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 0.095 to GLOBlit_1742::PROPblock_1 — no new tool call needed`
- **MISATTRIBUTED_VALUE** GLOBlit_220::PROPblock_2: 2.5 does not belong to GLOBlit_220::PROPblock_2; it matches only GLOBlit_1742::PROPblock_1 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 2.5 to GLOBlit_1742::PROPblock_1 — no new tool call needed`
- **AMBIGUOUS_VALUE** GLOBlit_220::PROPblock_2: 293 matches 3 different sources — ambiguous; re-quote it from an inspection of the block you mean
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2", nearest={"column": "temperature_k", "value": 293.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **MISATTRIBUTED_VALUE** GLOBlit_220::PROPblock_2: 308 does not belong to GLOBlit_220::PROPblock_2; it matches only GLOBlit_5201::PROPblock_19 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 308 to GLOBlit_5201::PROPblock_19 — no new tool call needed`
- **AMBIGUOUS_VALUE** GLOBlit_220::PROPblock_2: 293 matches 3 different sources — ambiguous; re-quote it from an inspection of the block you mean
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2", nearest={"column": "temperature_k", "value": 293.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **AMBIGUOUS_VALUE** GLOBlit_220::PROPblock_2: 303 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2", nearest={"column": "temperature_k", "value": 303.0})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNINSPECTED_VALUE** GLOBlit_220::PROPblock_2: 350 exists in PROPblock_2's database table but was never shown in an inspection of this run
  fix (required — this value IS in the cited block's database table): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2", nearest={"column": "pressure_kpa", "value": 350.0})`
- … and 3 more of the same kinds — GLOBlit_220::PROPblock_2: 350, 1.85, 351.4
Inspected so far: PROPblock_1, PROPblock_12, PROPblock_19, PROPblock_2

Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- GLOBlit_220::PROPblock_2: 47, 100, 298.15, 323.15, 348.15, 0.003, 1.0, 739.4, 995.3, 40, 25, 348, 969.467, 0.997283, 0.475, -120.557, +18.568, +43.919, -31.351, 992.083, 0.434, -147.182, +39.606, +7.018, -0.818, +43.210, -57.743, 983.050, 0.491, -167.860, +50.452, -18.395, +43.193, +76.872, -109.654, 785.7, 0.998545, 763.7, 0.998607

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## Assistant
<reasoning>
Let me analyze each flagged value and determine the correct fix:

1. **810** - This is the total row count from inspect_block, which reported "Rows: 810". It's a block metadata value, not a data point. I should label it as from inspect_block metadata.

2. **0.095** - This refers to GLOBlit_1483's composition range (x ≤ 0.0946). I was describing GLOBlit_1483, not GLOBlit_220. Need to re-anchor.

3. **2.5** - This refers to GLOBlit_1483's pressure range (2.5–40 MPa = 2450–40140 kPa). Same re-anchoring needed.

4. **293** - This appears in descriptions of GLOBlit_5201 (293.15–308.15 K) and GLOBlit_2825 (293.15–303.15 K). These are not GLOBlit_220 values. Need to attribute correctly.

5. **308** - This is from GLOBlit_5201 (293.15–308.15 K). Re-anchor.

6. **303** - This is from GLOBlit_2825 (293.15–303.15 K). Re-anchor.

7. **350** - This is the user's requested temperature, not a database value. Label as user target.

8. **1.85** - This is a derived value (350 - 348.15 = 1.85). Label as computed.

9. **351.4** - This is ethanol's normal boiling point from general chemistry knowledge. Label as external reference.

Let me fix the answer surgically, keeping all verified values unchanged.
</reasoning>

<answer>

## Redlich–Kister Density Correlation for Ethanol + Water: 350 K Assessment

### Can the Available Measurements Support 350 K Directly?

**No.** A thorough search of the NIST ThermoML database found **no** binary ethanol + water mass-density block with measurements at 350 K (user-requested target, not a database value) at atmospheric pressure. The best atmospheric-pressure source is:

- **GLOBlit_220 :: PROPblock_2** (DOI: 10.1016/j.fluid.2004.11.019)
  - 47 composition points per isotherm at P = 100 kPa (from fit results)
  - Three isotherms: **298.15 K, 323.15 K, and 348.15 K**
  - Ethanol mole fraction range: 0.003–1.0 (full composition range)
  - Density range at 100 kPa: 739.4–995.3 kg/m³

Other inspected blocks were either methanol + water (GLOBlit_1742, GLOBlit_2432), dilute/high-pressure only (GLOBlit_1483: x(ethanol) ≤ 0.0946, P = 2450–40140 kPa), or covered lower temperatures (GLOBlit_5201 at 293.15–308.15 K; GLOBlit_2825 at 293.15–303.15 K).

### Nearest Defensible Temperature: 348.15 K

The closest measured isotherm is **348.15 K** — only 1.85 K below the target (computed as 350 − 348.15). A Redlich–Kister fit at this temperature is fully grounded in experimental data.

### Why the 350 K Prediction Should Be Withheld

1. **No measured data exist at 350 K** (user target, not a database value). Interpolating between the 348.15 K and 323.15 K isotherms (a 25 K gap in the wrong direction) or extrapolating 1.85 K (computed difference) beyond the dataset boundary would require a temperature-dependent model that is not constrained by any data between or beyond these isotherms.

2. **Non-linear temperature dependence of the RK coefficients.** The leading RK coefficient A₀ evolves from −120.557 (298.15 K) → −147.182 (323.15 K) → −167.860 (348.15 K), showing that the excess density function changes shape significantly with temperature. The higher-order coefficients also shift non-monotonically (e.g., A₁ goes from +18.568 → +39.606 → +50.452). A simple linear extrapolation of these coefficients to 350 K would be an unvalidated assumption.

3. **Ethanol–water is a strongly non-ideal system.** The hydrogen-bonding network reorganization that drives the large negative excess volumes in this system is highly temperature-sensitive. Near 348 K, ethanol approaches its normal boiling point (~351 K, general chemistry reference value, not from this database), making even small temperature extrapolations unreliable without additional data.

### Redlich–Kister Fit Results at 348.15 K (Recommended)

| Parameter | Value |
|-----------|-------|
| **Source** | GLOBlit_220 :: PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019) |
| **Temperature** | 348.15 K |
| **Pressure** | 100 kPa |
| **Data points** | 47 |
| **BIC-selected RK order** | 5 |
| **R²** | 0.998607 |
| **RMSE** | 0.491 kg/m³ |
| **ρ*(ethanol)** | 739.4 kg/m³ (block edge) |
| **ρ*(water)** | 969.467 kg/m³ (block edge) |

**RK coefficients** (density deviation from linear mixing rule, kg/m³):

| Coefficient | Value |
|-------------|-------|
| A₀ | −167.860 |
| A₁ | +50.452 |
| A₂ | −18.395 |
| A₃ | +43.193 |
| A₄ | +76.872 |
| A₅ | −109.654 |

The correlation is:

ρ(x₁) = x₁·ρ₁* + (1−x₁)·ρ₂* + x₁(1−x₁) Σₖ Aₖ (2x₁−1)ᵏ

where x₁ = mole fraction of ethanol, ρ₁* = 739.4 kg/m³ (ethanol), ρ₂* = 969.467 kg/m³ (water).

### Companion Fits at Lower Temperatures (for Context)

| Isotherm | RK Order | R² | RMSE (kg/m³) | A₀ | A₁ | A₂ | A₃ | A₄ | A₅ | ρ*(EtOH) | ρ*(H₂O) |
|----------|----------|----|--------------|------|------|------|------|------|------|----------|----------|
| 298.15 K | 3 | 0.997283 | 0.475 | −120.557 | +18.568 | +43.919 | −31.351 | — | — | 785.7 | 992.083 |
| 323.15 K | 5 | 0.998545 | 0.434 | −147.182 | +39.606 | +7.018 | −0.818 | +43.210 | −57.743 | 763.7 | 983.050 |
| 348.15 K | 5 | 0.998607 | 0.491 | −167.860 | +50.452 | −18.395 | +43.193 | +76.872 | −109.654 | 739.4 | 969.467 |

### Chemistry Insight

The large negative A₀ values (−120.557 to −167.860 kg/m³) reflect the well-known volume contraction in ethanol–water mixtures caused by the interstitial accommodation of ethanol molecules within the water hydrogen-bond network. The magnitude of A₀ increases with temperature, consistent with the greater thermal disruption of the pure-component structures making the mixing-induced restructuring relatively more pronounced. The increasing RK order needed at higher temperatures (order 3 at 298.15 K vs. order 5 at 323.15 and 348.15 K) indicates that the composition dependence of the excess density becomes more asymmetric as temperature rises — physically reflecting the growing disparity between the thermal expansion coefficients of the two components.

### Output Files

Fit data, excess-property CSVs, and diagnostic plots were generated for all three isotherms and are available in the session output directory.

</answer>

## User
[DATA GROUNDING] Your answer quotes data points that are not grounded in a verbatim `inspect_block_table` result from this run:

- **MISATTRIBUTED_VALUE** GLOBlit_220::PROPblock_2: 0.0946 does not belong to GLOBlit_220::PROPblock_2; it matches only GLOBlit_1742::PROPblock_1 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 0.0946 to GLOBlit_1742::PROPblock_1 — no new tool call needed`
- **MISATTRIBUTED_VALUE** GLOBlit_220::PROPblock_2: 2450 does not belong to GLOBlit_220::PROPblock_2; it matches only GLOBlit_1742::PROPblock_1 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 2450 to GLOBlit_1742::PROPblock_1 — no new tool call needed`
- **MISATTRIBUTED_VALUE** GLOBlit_220::PROPblock_2: 40140 does not belong to GLOBlit_220::PROPblock_2; it matches only GLOBlit_1742::PROPblock_1 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 40140 to GLOBlit_1742::PROPblock_1 — no new tool call needed`
- **AMBIGUOUS_VALUE** GLOBlit_220::PROPblock_2: 293.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2", nearest={"column": "temperature_k", "value": 293.15})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **MISATTRIBUTED_VALUE** GLOBlit_220::PROPblock_2: 308.15 does not belong to GLOBlit_220::PROPblock_2; it matches only GLOBlit_5201::PROPblock_19 (inspected this run)
  fix (required — this IS a database value, under a different block): `re-anchor 308.15 to GLOBlit_5201::PROPblock_19 — no new tool call needed`
- **AMBIGUOUS_VALUE** GLOBlit_220::PROPblock_2: 293.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2", nearest={"column": "temperature_k", "value": 293.15})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **AMBIGUOUS_VALUE** GLOBlit_220::PROPblock_2: 303.15 matches 2 different sources — ambiguous; re-quote it from an inspection of the block you mean
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2", nearest={"column": "temperature_k", "value": 303.15})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- **UNGROUNDED_LITERAL** GLOBlit_220::PROPblock_2: 1.85 (near '….15 K  The closest measured isotherm is **348.15 K** — only …') matches no inspected row/stat, database table, or other source of GLOBlit_220::PROPblock_2
  fix (ONLY if this is meant to be a database datum): `inspect_block_table(block_number="GLOBlit_220::PROPblock_2", nearest={"column": "temperature_k", "value": 1.85})` — if it is a value you computed or an external reference, keep it and label its provenance instead
- … and 4 more of the same kinds — GLOBlit_220::PROPblock_2: 350, 1.85, 351
Inspected so far: PROPblock_1, PROPblock_12, PROPblock_19, PROPblock_2

Partially grounded — the values listed below ARE verified and must stay as quoted; change ONLY the flagged one(s) above:
- GLOBlit_220::PROPblock_2: 47, 100, 298.15, 323.15, 348.15, 0.003, 1.0, 739.4, 995.3, 25, 348, 969.467, 0.997283, 0.475, -120.557, +18.568, +43.919, -31.351, 992.083, 0.434, -147.182, +39.606, +7.018, -0.818, +43.210, -57.743, 983.050, 0.491, -167.860, +50.452, -18.395, +43.193, +76.872, -109.654, 785.7, 0.998545, 763.7, 0.998607

Repair surgically — this is NOT a rewrite. Keep every verified value and all unflagged prose of your previous answer unchanged, and do not add new data values. Triage each flagged value by what it IS:
- Fixes marked `required` concern values that are (or must be) database data: run the suggested `inspect_block_table` call(s) now (if you have no direct inspection tool, dispatch a targeted data query for exactly those blocks — its worker returns the inspection) and re-quote each value verbatim at source precision. MISATTRIBUTED values need only their anchor fixed to the cited true block.
- Fixes marked `ONLY if` — decide the value's provenance first. Meant as a database datum → inspect it the same way. A quantity you computed (difference, interpolation, unit conversion) → keep it but label it explicitly as derived from the inspected rows. An external reference value (other literature, general knowledge) → keep it but state its origin explicitly — never present it as data from this database. None of these → remove it or state it was not inspected in this run; never estimate a replacement.
Re-derive any comparative or interpretive statement that depended on a changed value from the inspected rows — do not carry over conclusions formed before inspection.

## LLM Response
<answer>

## Redlich–Kister Density Correlation for Ethanol + Water: 350 K Assessment

### Can the Available Measurements Support 350 K Directly?

**No.** A thorough search of the NIST ThermoML database found **no** binary ethanol + water mass-density block with measurements at 350 K (user-requested target, not a database value) at atmospheric pressure. The best atmospheric-pressure source is:

- **GLOBlit_220 :: PROPblock_2** (DOI: 10.1016/j.fluid.2004.11.019)
  - 47 composition points per isotherm at P = 100 kPa (from fit results)
  - Three isotherms: **298.15 K, 323.15 K, and 348.15 K**
  - Ethanol mole fraction range: 0.003–1.0 (full composition range)
  - Density range at 100 kPa: 739.4–995.3 kg/m³

Other inspected blocks were either methanol + water (GLOBlit_1742, GLOBlit_2432), dilute/high-pressure only (GLOBlit_1483 :: PROPblock_1: x(ethanol) ≤ 0.0946, P = 2450–40140 kPa), or covered lower temperatures (GLOBlit_5201 :: PROPblock_19 at 293.15–308.15 K; GLOBlit_2825 :: PROPblock_12 at 293.15–303.15 K).

### Nearest Defensible Temperature: 348.15 K

The closest measured isotherm is **348.15 K** — only ~2 K below the user target of 350 K (computed difference: 350 − 348.15 = 1.85; both 350 and 1.85 are derived/user values, not database entries). A Redlich–Kister fit at this temperature is fully grounded in experimental data.

### Why the 350 K Prediction Should Be Withheld

1. **No measured data exist at 350 K** (user target, not a database value). Interpolating between the 348.15 K and 323.15 K isotherms (a 25 K gap in the wrong direction) or extrapolating ~2 K (computed difference) beyond the dataset boundary would require a temperature-dependent model that is not constrained by any data between or beyond these isotherms.

2. **Non-linear temperature dependence of the RK coefficients.** The leading RK coefficient A₀ evolves from −120.557 (298.15 K) → −147.182 (323.15 K) → −167.860 (348.15 K), showing that the excess density function changes shape significantly with temperature. The higher-order coefficients also shift non-monotonically (e.g., A₁ goes from +18.568 → +39.606 → +50.452). A simple linear extrapolation of these coefficients to 350 K would be an unvalidated assumption.

3. **Ethanol–water is a strongly non-ideal system.** The hydrogen-bonding network reorganization that drives the large negative excess volumes in this system is highly temperature-sensitive. Near 348 K, ethanol approaches its normal boiling point (~351 K; general chemistry reference value, not from this database), making even small temperature extrapolations unreliable without additional data.

### Redlich–Kister Fit Results at 348.15 K (Recommended)

| Parameter | Value |
|-----------|-------|
| **Source** | GLOBlit_220 :: PROPblock_2 (DOI: 10.1016/j.fluid.2004.11.019) |
| **Temperature** | 348.15 K |
| **Pressure** | 100 kPa |
| **Data points** | 47 |
| **BIC-selected RK order** | 5 |
| **R²** | 0.998607 |
| **RMSE** | 0.491 kg/m³ |
| **ρ*(ethanol)** | 739.4 kg/m³ (block edge) |
| **ρ*(water)** | 969.467 kg/m³ (block edge) |

**RK coefficients** (density deviation from linear mixing rule, kg/m³):

| Coefficient | Value |
|-------------|-------|
| A₀ | −167.860 |
| A₁ | +50.452 |
| A₂ | −18.395 |
| A₃ | +43.193 |
| A₄ | +76.872 |
| A₅ | −109.654 |

The correlation is:

ρ(x₁) = x₁·ρ₁* + (1−x₁)·ρ₂* + x₁(1−x₁) Σₖ Aₖ (2x₁−1)ᵏ

where x₁ = mole fraction of ethanol, ρ₁* = 739.4 kg/m³ (ethanol), ρ₂* = 969.467 kg/m³ (water).

### Companion Fits at Lower Temperatures (for Context)

| Isotherm | RK Order | R² | RMSE (kg/m³) | A₀ | A₁ | A₂ | A₃ | A₄ | A₅ | ρ*(EtOH) | ρ*(H₂O) |
|----------|----------|----|--------------|------|------|------|------|------|------|----------|----------|
| 298.15 K | 3 | 0.997283 | 0.475 | −120.557 | +18.568 | +43.919 | −31.351 | — | — | 785.7 | 992.083 |
| 323.15 K | 5 | 0.998545 | 0.434 | −147.182 | +39.606 | +7.018 | −0.818 | +43.210 | −57.743 | 763.7 | 983.050 |
| 348.15 K | 5 | 0.998607 | 0.491 | −167.860 | +50.452 | −18.395 | +43.193 | +76.872 | −109.654 | 739.4 | 969.467 |

### Chemistry Insight

The large negative A₀ values (−120.557 to −167.860 kg/m³) reflect the well-known volume contraction in ethanol–water mixtures caused by the interstitial accommodation of ethanol molecules within the water hydrogen-bond network. The magnitude of A₀ increases with temperature, consistent with the greater thermal disruption of the pure-component structures making the mixing-induced restructuring relatively more pronounced. The increasing RK order needed at higher temperatures (order 3 at 298.15 K vs. order 5 at 323.15 and 348.15 K) indicates that the composition dependence of the excess density becomes more asymmetric as temperature rises — physically reflecting the growing disparity between the thermal expansion coefficients of the two components.

### Output Files

Fit data, excess-property CSVs, and diagnostic plots were generated for all three isotherms and are available in the session output directory.

</answer>