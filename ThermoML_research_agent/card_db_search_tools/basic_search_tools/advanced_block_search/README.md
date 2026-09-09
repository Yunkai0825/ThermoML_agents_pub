# `block_search_adv` public adapter and private engine

The only public entry point is
`../12_block_search_adv.py::block_search_adv`. This package translates the
shallow public contract into the typed private query plan and executes it. The
AST tool registry therefore discovers one tool, not its engine helpers.

## Public boundary

Every public argument is either a scalar or one flat `list[str]`. A list item
is always a complete declaration or SQL-like expression:

```python
block_search_adv(
    targets=["GLOBprop_34 AS conductivity PHASE GLOBphase_3"],
    explanation="Find carbon dioxide thermal-conductivity measurements.",
    compounds=["GLOBcomp_3 AS carbon_dioxide"],
    parameters=["GLOBconstr_2 AS temperature PHASE GLOBphase_3"],
    where="temperature BETWEEN 298[K] AND 310[K]",
)
```

Public dictionaries, lists of dictionaries, nested arrays, a wrapper
`request`, and a caller-supplied `schema` are not accepted. Parentheses and
unit brackets inside a string are expression text, not JSON nesting.

The main declaration forms are:

```text
[REQUIRE|ANY|EXCLUDE] GLOBcomp_N AS alias [IN scope]

[REQUIRE|ANY|EXCLUDE] GLOBphase_N

GLOBprop|var|constr_N AS alias
  [COMPONENT compound_alias]
  [PHASE GLOBphase_N]
  [PHASE_COMPONENT compound_alias]
  [MIN_FINITE n]
  [MIN_DISTINCT n]
  [CARDINALITY ONE|EACH]

GLOBprop|var|constr_N AS alias ... [WHERE VALUE <predicate>]

GLOBprop|var|constr_N AS alias
  ON TARGET target_alias ... [WHERE VALUE <predicate>]
```

The first quantity form is used in `parameters` and `targets`; the third is
used in `fixed_constraints`; the fourth is used in `inline_state`.
`calculate`, `select`, and `order_by` each contain complete SQL-like clauses,
while `where` and `having` are scalar strings.

Compound and phase REQUIRE clauses are AND terms, multiple ANY clauses form
one OR group, and EXCLUDE clauses are NOT terms. An omitted clause mode follows
the corresponding `compound_match` or `phase_match` default. Exact systems
permit required compounds only. The canonical one-component system type is
`unary`, not `pure`.

## Identity and source-role rules

The argument determines the required authoritative ThermoML occurrence role:

| Public argument | Required source occurrence |
|---|---|
| `parameters` | `variable` |
| `targets` | `property` |
| `fixed_constraints` | `constraint` |
| `inline_state` | target-linked `inline_state` |

The PCS-metadata-named translation CSV maps equivalent global property,
variable, and constraint templates to one physical `quantity_key`. It lets a
chemist name the same quantity with any populated core global ID in that
translation row. It never casts the source occurrence into another role. For
example, a `GLOBconstr_N` supplied in `parameters` can resolve an equivalent
actual variable; it cannot make an actual constraint into a parameter.

Parameters and targets are row-aligned data columns. Fixed constraints are
one block-level value, and ReactionData inline state is one value attached to
a named target property. Neither fixed constraints nor inline state become
row columns, participate in `minimum_common_points`, or appear as aliases in
row calculations or `select`. Their values and target links are returned
automatically as `fixed_filter_evidence`. Omitting their `WHERE` predicate
requires one usable reported numeric value without restricting its range.

Component, exact phase, phase-component, finite/distinct-count, and
cardinality qualifiers disambiguate occurrences. `CARDINALITY ONE` rejects an
ambiguous block; `CARDINALITY EACH` preserves distinct legitimate bindings,
evaluating every binding independently up to the private safety limit. Alias
permutations never duplicate a block. Public aliases are case-insensitive and
normalized to lowercase.

## SQL-like expressions

`where` may reference declared parameter and target aliases and calculated
row aliases. The adapter automatically derives the private filter whitelist
from all declared parameter and target aliases; there is no public
`filtering_identity` argument.

Examples:

```text
temperature BETWEEN 425[K] AND 429[K]
x IN (0.1[1], 0.5[1], 0.9[1])
pressure IS NOT NULL
ABS(h_excess) / (x * (1[1] - x))
MEAN(scaled_h) AS mean_scaled_h
COUNT(*) >= 4
mean_scaled_h DESC NULLS LAST
```

Supported row operations include `+`, `-`, `*`, `/`, `^`, comparisons,
`BETWEEN`, `IN`, `AND`, `OR`, `NOT`, null tests, `ABS`, `SQRT`, `LN`,
`LOG10`, `EXP`, `POWER`, and `COALESCE`. `select` additionally accepts
`COUNT(*)`, `COUNT`, `COUNT_DISTINCT`, `MIN`, `MAX`, `SUM`, `AVG`/`MEAN`,
`MEDIAN`, and sample standard deviation. Expressions are parsed and
allowlisted; the strings are never executed as Python or passed through as
SQL.

`BETWEEN` accepts a row alias, function call, or parenthesized nested
expression on its left. A space before a unit bracket is optional. The adapter
normalizes common chemistry literals in MPa, Pa, bar, atm, degC/°C, J/mol,
mPa*s/cP, and g/cm3 to the engine's exact canonical units before semantic
checking. `having` may combine selected aliases with direct aggregates.

`MIN_FINITE` and `MIN_DISTINCT` qualify one candidate occurrence before row
alignment. `minimum_common_points` is a single integer applied after `where`
to complete finite rows across every declared parameter and target.
`calculate` materializes row expressions, `select` returns block scalars,
`having` filters those scalars, and `order_by` gives stable SQL-style
direction and null placement.

## Automatic pre-execution review hierarchy

See [the input-and-loop diagram](INPUT_AND_REACT_LOOPS.md) for the agent-facing
request shape and composite selector construction.

See [the tested argument-complexity examples](ARGUMENT_COMPLEXITY_EXAMPLES.md)
for the executable grammar minimum, recommended simple form, and
maximum-meaningful mixture and reaction requests with real database results.

The same flat request must pass three content-addressed reviews before any raw
row is read. The framework walks them AUTOMATICALLY inside one public call;
the calling agent never emits confirmation tokens:

1. **Composite ID enrichment** parses the grammar and resolves catalog IDs,
   role translations, canonical units/dimensions, compound and phase names,
   component annotations, expressions, and deterministic `ADVselector_*`
   composite selector IDs.
2. **Database ID intent** searches the registries and PCS identity indexes
   without opening raw rows. It reports real `GLOBlit`/DOI pairs, block and
   `BLKsubsys` IDs, actual `BLKprop`/`BLKvar`/`BLKconstr` bindings, ranges,
   coverage, components, phases, property presentation/reference state, and
   methods.
3. **Final intent and syntax** restates the chemistry, canonical AST,
   operations, common-point requirement, limits, and unresolved warnings. It
   explicitly does not claim row-filter or aggregate results.
4. Execution opens raw ThermoML `NumValues` only after all three internal
   confirmations remain valid for the same request and database state; the
   executed result returns the confirmed evidence under
   `preexecution_review` (`automatic_confirmation: true`).

Every internal token binds the normalized request and all lower-stage
evidence. Database state is also bound at the stages that depend on it, so
changed arguments or changed data fail closed and restart the internal
hierarchy. The query-agent `SYNC_TOOL_GUIDANCE_CHECK` hook fails fast on
invalid chemistry/syntax arguments before the callable runs; the call must
still be alone in its tool batch.

## Execution and deduplication

1. Reuse the confirmed registry/PCS preparation from the database-intent gate.
2. Open `thermoml_raw.db` read-only and materialize all uncapped `NumValues`
   rows only after final confirmation.
3. Reconcile raw occurrence counts against the embedded PCS statistics.
4. Apply fixed and inline-state gates, align row columns, evaluate expressions,
   aggregate, filter, and order.
5. Return one result per `(doi, PROPblock_N|RXNblock_N)`, with distinct
   occurrence alternatives nested in `binding_matches`.

The existing `search_blocks` tool neither reads this derived index nor calls
this engine, so its search behavior and compaction remain isolated.

## Hardcoded result compaction

The engine continues to return `block_search_adv/result-v1` (or
`block_search_adv/error-v1`). Input contract versioning is independent of
that result schema. The dedicated formatter is:

`../../_tools_results_compactors/basic_search_tools/block_search_adv_compactor.py`

It is registered with `@compacts("block_search_adv")` and accepts the
advanced result/error schemas. It emits bounded Markdown with provenance,
typed block IDs, actual occurrence roles and keys, complete-point counts,
selected values, fixed/inline-state evidence, row counts, ordering,
diagnostics, and truncation. It omits raw rows, embedded
permutations/statistics, and the full normalized query before the generic
agentic KEEP/DISCARD pass.
