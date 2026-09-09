# `block_search_adv` real-data regression suite

This suite exercises the installed public `block_search_adv(**request)` API
against the published PCS and raw ThermoML databases.

From the `ThermoML_research_agent` directory, run:

```powershell
pytest -q card_db_search_tools/tests/test_block_search_adv
```

Set `THERMOML_QUERY_ROOT` to test another ThermoML query checkout.

The suite discovers its enclosing ThermoML query checkout without depending
on a mapped drive. External staging runs may use
`THERMOML_QUERY_ROOT` or the default live checkout.

The fixtures deliberately cover:

- uncapped raw rows beyond the PCS card's 50-row display limit;
- exact property/variable/constraint translation without role casting;
- block constraints versus ReactionData inline state;
- row filtering, nested `exp(ln(x))` and arithmetic expressions;
- completeness-aware minimum common points;
- stable sorting, limiting, and alias-path deduplication;
- cardinality ambiguity versus legitimate `cardinality=all` expansion;
- compact-Markdown registration and information preservation;
- byte-identical current `search_blocks` source and output behavior.
- censored `PropLimit` reconciliation as NULL without finite-count inflation;
- fail-closed schema, role, component, unit, alias-cycle, and raw-SQL errors.
