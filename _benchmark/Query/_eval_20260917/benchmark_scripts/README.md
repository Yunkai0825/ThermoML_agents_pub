# ThermoML query-agent variant benchmarks

This directory contains five controlled, flat-agent benchmark arms built around
the current ThermoML query-agent prompt catalog. The catalog is
`ThermoML_research_agent/NIST_ThermoML_agents/NIST_ThermoML_query_agent/_DEBUG_script/test_prompts.md`
and currently contains 28 prompts in six sections. Every run records the prompt
file's SHA-256 digest so later comparisons can detect catalog drift.

The launchers are **dry-run/preflight only by default**. They read schemas and
validate the selected arm, but do not read the API key, call Anthropic, or write
run output. Paid execution requires the explicit `--go` flag.

## Benchmark arms

| Arm | Launcher | Evidence available to the answering agent | Fixed output directory |
|---|---|---|---|
| Parsed-card SQL, prefixed IDs | `run_only_sql_prefixed.py` | Exactly one read-only `execute_sql` tool over the parsed-card databases | `N:\_Code_Maintenance\__obsolete__\ThermoML_20260802_batch\Query\test_run_only_SQL_20260916` |
| Parsed-card SQL, no prefixes | `run_only_sql_no_prefix.py` | The same SQL tool and databases, with recognized domain-prefixed IDs reduced to their raw numeric suffixes | `N:\_Code_Maintenance\__obsolete__\ThermoML_20260802_batch\Query\test_run_only_SQL_no_prefix_20260916` |
| Raw ThermoML SQL | `run_only_sql_rawdb.py` | Exactly one read-only `execute_sql` tool over `thermoml_raw.db`, including source `json_data` | `N:\_Code_Maintenance\__obsolete__\ThermoML_20260802_batch\Query\test_run_only_SQL_rawdb_20260916` |
| Bare model | `run_bare_model.py` | No tools and no database access | `N:\_Code_Maintenance\__obsolete__\ThermoML_20260802_batch\Query\test_run_bare_model_20260916` |
| Flat L1 + L2 toolbox | `run_flat_tools.py` | The 13 underlying L1 search tools and 10 underlying L2 leaf tools, exposed directly as one 23-tool toolbox | `N:\_Code_Maintenance\__obsolete__\ThermoML_20260802_batch\Query\test_run_flat_tools_20260916` |

The parsed SQL arms attach the parsed index, registries, individual card stores,
and domain-knowledge stores under documented SQLite aliases. The raw SQL arm
instead exposes the database built from raw ThermoML documents. These are
different evidence sources, not two names for the same database.

The no-prefix arm strips the semantic prefix from recognized identifiers and
exposes the raw numeric suffix: for example, `GLOBcomp_51` becomes `51`. This
transformation is intentionally not a bijection. Identifiers from different
domains can have the same suffix, so every suffix must remain scoped by its
column plus DOI/block/card context; it must not be used as a globally unique
join key. Follow-up SQL can filter stored prefixed values explicitly with the
read-only helper `thermoml_raw_id(value)`, for example
`WHERE thermoml_raw_id(component_id) = '51'`. The helper returns text so a
multi-part suffix such as `1_2` stays intact. Sanitization happens before raw
result Markdown reaches the compactor, so semantic prefixes are not retained in
that arm's audit artifacts.

The flat-tools arm exposes the underlying functions themselves. It has no L1
or L2 query agents, dispatcher-agent calls, or delegation. Its results follow
the existing per-tool result policy: applicable deterministic compactors run
first, and the existing agentic compactor runs afterward. For this benchmark,
catalog skip/pass-through flags do not bypass that agentic stage: every
successful direct-tool result must receive a task-directed agentic verdict
before it can enter the answering model's context. Compaction is result
handling, not a delegated query-agent layer. If either required compaction stage
fails or rejects an oversized result, the lossless raw and deterministic
results remain available only in the audit artifact; the answering model
receives a concise failure notice, never a result fallback. The bare-model arm
has no tool loop at all.

## SQL result path and agentic compaction

Every SQL call has three mandatory semantic inputs:

- `sql`: one `SELECT`, `WITH`, or `EXPLAIN QUERY PLAN` statement;
- `purpose`: why this query is needed for the benchmark question; and
- `tasks`: a non-empty list of concrete facts, comparisons, or calculations
  that the result must support.

After read-only execution, typed rows are serialized losslessly as Markdown
(JSON column metadata plus JSONL row arrays). That exact Markdown is recorded
for audit and sent to a separate, tool-less agentic compactor together with the
original benchmark question, SQL purpose, SQL tasks, visible SQL, and database
schema. The answering agent receives the compactor's task-directed Markdown.

There is **no hardcoded or schema-specific semantic compaction step**. Row,
character, query-time, and one-statement limits are operational safety limits;
when a result exceeds them the tool asks the agent to narrow, filter, aggregate,
or paginate its SQL instead of silently summarizing it. A compactor failure also
does not bypass the compactor by leaking raw rows into the answering context.

This SQL path is deliberately different from the flat toolbox's established
per-tool pipeline: SQL raw Markdown goes **directly** to its task-directed
agentic compactor and never through a hardcoded semantic compactor.

## Folder layout

All code for these five query-agent variants is collected in this directory:

    benchmark_scripts/
    ├── run_only_sql_prefixed.py       # parsed cards; original prefixed IDs
    ├── run_only_sql_no_prefix.py      # parsed cards; raw numeric ID suffixes
    ├── run_only_sql_rawdb.py          # raw ThermoML JSON database
    ├── run_flat_tools.py              # flat L1 + L2 toolbox, no delegation
    ├── run_bare_model.py              # no tools
    ├── run_all.py                     # sequential launcher for all variants
    ├── benchmark.py                   # shared agent loop and variant registry
    ├── sql_backend.py                 # read-only SQL implementations
    ├── flat_tools.py                  # direct tool adapter and compaction
    ├── anthropic_api.py               # API transport and SQL compactor
    ├── artifacts.py                   # benchmark artifact writers
    ├── paths.py                       # archive/workspace discovery
    └── tests/                         # offline contract and SQL safety tests

Run outputs remain sibling directories under `Query/`; they are not mixed
with the executable benchmark code.

## API key and safety

The default key file is intentionally named (including the historical
misspelling):

```text
N:\_Code_Maintenance\__obsolete__\ThermoML_20260802_batch\ANTRHOPIC_API_KEY
```

It may contain a plain key, `ANTHROPIC_API_KEY=...`,
`ANTRHOPIC_API_KEY=...`, or a small JSON object with an `ANTHROPIC_API_KEY`,
`api_key`, or `key` field. It is opened only after `--go`, is excluded from
client representations and request records, and must never be copied into an
output artifact.

SQL connections are opened read-only, extension loading is disabled, a SQLite
authorizer rejects mutation/attach/pragma operations, and a progress deadline
interrupts long queries. The API client retries transient HTTP failures but
does not log request headers.

## Running

From this directory, a preflight of one arm is:

```powershell
N:\_python\miniforge3\python.exe .\run_only_sql_prefixed.py
```

Run one prompt first to validate paid execution and output:

```powershell
N:\_python\miniforge3\python.exe .\run_only_sql_prefixed.py 1.1 --go
```

Prompt IDs are positional arguments. `--section` selects a complete numbered
section when no IDs are supplied:

```powershell
N:\_python\miniforge3\python.exe .\run_only_sql_rawdb.py 2.1 2.2 --go
N:\_python\miniforge3\python.exe .\run_flat_tools.py --section 3 --go
```

To resume safely, `--skip-existing` skips a `Qx.y` directory only when it has
an OK `result.md` recorded at the requested API effort, a nonempty
`anthropic_raw_capture.jsonl`, and no in-progress marker. Legacy,
effort-mismatched, interrupted, ERROR, and TIMEOUT results are rerun. Without
that option the runner refuses to overwrite a selected existing result:

```powershell
N:\_python\miniforge3\python.exe .\run_only_sql_prefixed.py --skip-existing --go
```

`run_all.py` forwards common arguments to all five launchers, sequentially. Its
default is still a dry run. It rejects `--output` because one shared override
would mix five arms; use an individual launcher for an output override:

```powershell
N:\_python\miniforge3\python.exe .\run_all.py
N:\_python\miniforge3\python.exe .\run_all.py --section 1 --skip-existing --go
```

Useful controls include:

- `--effort` (default `max`), sent as Anthropic
  `output_config.effort` on every answering and agentic-compactor request;
- `--model` and `--compactor-model` (SQL and flat-tool compactor calls);
- `--max-tokens`, SQL `--compactor-max-tokens`, `--max-turns`, and
  `--soft-budget-strikes`
  (flat tools retain the existing compactor token policy);
- `--prompt-timeout`, `--request-timeout`, `--sql-timeout`, and
  `--sql-max-result-chars`;
- `--workers` and the inter-submission `--gap`;
- `--output`, `--prompt-file`, and `--api-key-file`; and
- `--allow-prompt-drift`, which should be used only for an intentional change
  from the expected 28-prompt catalog.

Use `--help` on any launcher for defaults. An output override is useful for a
smoke test, but the five fixed directories above are the comparison targets.

`--max-turns` is the soft-budget escalation threshold, not the hard cutoff.
With the benchmark defaults, strike 1 is issued on turn 20, strike 2 on turn
21, and strike 3 on turn 22. Turn 22 is the final chance: tools are removed and
the answering model receives a fresh answer-only context containing the
original question plus all already compacted, model-visible tool evidence. This
avoids replaying a bloated multi-turn transcript while preserving the evidence
needed to answer. No turn 23 is allowed. Every issued strike and the fresh
context's character count/SHA-256 are recorded in the prompt artifacts and raw
API capture.

> **Cost warning:** `--go` makes paid Anthropic requests. A complete
> `run_all.py --go` executes 140 answering-agent prompt runs (28 prompts across
> five arms). Every SQL call adds its dedicated agentic-compactor request, and
> flat-tool calls may add requests according to the established compaction
> policy. Start with dry-run preflight and one prompt. Increase `--workers` only
> with an understood rate limit and cost budget.

## Output contract

Each executed prompt is placed in `Q<id>/`. It contains the seven derived
reports from the recovered Query layout plus a streamed raw API sidecar:

```text
result.md
tool_trace.md
run_history.md
working_memory.md
final_full_context.md
reference_stats.md
reasoning_tokens_stripped.md
anthropic_raw_capture.jsonl
```

`anthropic_raw_capture.jsonl` is appended immediately after every Anthropic
HTTP exchange, including compactor calls and retry responses. Each line stores
the exact request payload, parsed raw response, safe response headers, status,
model, timing, and character counts. Request/authentication headers are never
stored, so the API key is excluded. In the no-prefix arm this file remains raw
wire evidence; the separately persisted audit transcript and database evidence
still apply that arm's numeric-suffix sanitization.

For SQL, `run_history.md` holds the exact raw Markdown supplied to the agentic
compactor, its SHA-256 digest, and the model-visible compacted result. The API
does not expose private chain-of-thought by default;
`reasoning_tokens_stripped.md` says so rather than reconstructing it.

A completed run writes exactly three run-root files in addition to the `Q*`
directories:

```text
run_log.txt
TEST_SUMMARY_<timestamp>.md
TEST_TRACE_<timestamp>.json
```

The summary links to each `result.md`; the JSON trace retains machine-readable
status, usage, and tool history.

## Offline tests

The test suite uses temporary SQLite databases and a fake compactor client. It
blocks `requests` network calls and never opens the real key file:

```powershell
N:\_python\miniforge3\python.exe -m pytest .\tests -q
```
