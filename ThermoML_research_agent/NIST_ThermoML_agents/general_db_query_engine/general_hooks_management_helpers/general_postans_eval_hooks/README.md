# General post-answer evaluation hooks

This package implements the shared four-stage return lifecycle:

1. The working ReAct agent's final emission contains only its complete
   chemistry answer text. Its earlier ReAct turns may still contain the
   normal reasoning/summary/tool-call protocol.
2. One shared anchor launches two tool-free agents in parallel:
   - core-claims distillation from the answer only;
   - ID/metadata alignment from the answer, task, and completed tool record.
   For schemas containing `summary`, a hidden summary-construction tool runs
   concurrently from the answer only and contributes to the ID branch.
3. Agent-specific hidden construction tools validate minimal search anchors and
   populate database-owned chemistry, identifier, and bibliographic fields.
4. Deterministic code restores the untouched answer, attaches canonical
   DOI/literature pairs, validates scoped identifiers, and emits the JSON
   document consumed downstream.

Neither agent is a ReAct chain and neither receives a tool registry. The
core-claims agent cannot see tool history. The ID/metadata agent receives a
read-only rendering of completed calls. Neither can rewrite the answer text.

All final schemas contain:

```json
{
  "answer": "Untouched working-agent answer text.",
  "core_claims": ["One central, well-supported summary claim."],
  "...": "agent-specific evaluated fields"
}
```

Use `prepare_answer_only_system_prompt()` before the working-agent ReAct
call, then `evaluate_and_assemble_return()` after it terminates.

Every ThermoML agent skill Markdown contains exactly one
`# Response JSON Schema` section. `parse_workflow()` removes that entire
section from the answer-agent `system_prompt` and returns it separately as
`response_json_schema`. The answer agent therefore cannot see or imitate the
downstream structure. The same parsed schema is split after termination:
`core_claims` goes to the core-claims distillation agent, `summary` goes to
the hidden answer-summary tool, and the remaining fields go to the
ID/metadata-alignment agent. Assembly uses
the exact declared schema; it does not synthesize missing fields or fall back
to a legacy schema.

## Stage contracts

### 1. Working-agent answer

The final `<answer>` payload is ordinary prose. It may include concise
chemical insight, explanations, examples, and inline citations needed for
the scientific answer. It must not contain a second JSON object, core claims
array, source array, identifier catalog, or other machine-facing payload.

### 2. Parallel evaluation and hidden summary construction

`POSTANS_PARALLEL_AGENTS_DISPATCH` (the semantic alias of
`POSTANS_EVALUATION_BEFORE`) fires exactly once with both prompts and schemas.
Immediately afterward, both independent agents and, when required, the
hidden summary tool are submitted concurrently. Each call receives its own copy of the parent
`ContextVar` context so Argo statistics and run-record bindings remain
attached to the same parent agent run.

The core-claims agent receives:

- the untouched answer;
- the one-field `core_claims` schema.

The schema document uses one array element as a type exemplar; the evaluated
`core_claims` value must contain one or several non-empty central claims.

The ID/metadata agent receives:

- the original task context;
- the untouched answer;
- a read-only rendering of completed tool history using each full recorded
  result;
- all agent-specific output fields except `answer`, `core_claims`, and `summary`.

The summary tool receives only the untouched answer and returns exactly one
non-empty `summary` string. The ID agent cannot see or revise that field.

Both agents receive no tool dictionary. A branch may make one formatting-correction
call only when its JSON is malformed. Neither branch is a ReAct loop or can
resume database exploration.

### 3. Agent-specific deterministic field construction

When configured, hidden tools consume the ID agent's minimal anchors, validate
them against authoritative cards/registries, and fill every database-owned
field. Validation mismatches may trigger a bounded correction call that cannot
change the answer, core claims, or tool-generated summary.

### 4. Deterministic assembly

Python code inserts the original answer and the core-claims-agent result, verifies
that both agents emitted exactly their non-overlapping fields, then joins
the ID/metadata result. Literature identities are then settled in two passes:

1. `reconcile_literature_identities` — the registered `GLOBlit_N` is
   **authoritative**. A missing, unregistered, or mismatched `doi` next to a
   registered `lit_num_id` is repaired from the registry; source entries with
   no verifiable identity are dropped from lists (or null-coupled in bare
   dicts); unregistered bare literature values are cleared. Every repair is
   logged as an error-level note — unverifiable citations degrade
   deterministically instead of destroying a completed run.
2. `attach_lit_num_ids` — fully strict enrichment/cross-check of the now
   clean `doi`/`lit_num_id` pairs.

It then validates all nested scoped identifiers, invokes any agent-specific
exact validator, and serializes the object for downstream consumers. Neither
agent can overwrite `answer`, and the ID agent cannot emit `core_claims`.

```text
completed ReAct run
  └─ answer text only
       └─ POSTANS_PARALLEL_AGENTS_DISPATCH (fires once)
            ├─ core-claims agent ───────→ {"core_claims": [...]}
            ├─ summary tool ─────────────→ {"summary": "..."}
            └─ ID/metadata agent ────────→ {minimal agent-specific fields}
                         │
                         └─ field-construction tools
                              └─ deterministic join + ID validation
                                      └─ downstream JSON
```

Assembly waits for both branches. Any failure in either branch's JSON, exact
field membership, ID pairing, scoped-ID validation, or the agent-specific
validator stops the handoff. A one-sided or malformed partial object is never
sent downstream.


