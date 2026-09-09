# Tool 12 argument complexity: tested minimum and maximum-meaningful calls

Tool 12 has only two required chemistry arguments: `targets` and
`explanation`. All other chemistry fields are optional, but the three
confirmation tokens become mandatory sequentially during execution. A valid
call can therefore be syntactically tiny while still being chemically too broad.

## Complexity layers

| Layer | Fields | Main complication |
|---|---|---|
| Quantity | `targets`, `parameters`, `fixed_constraints`, `inline_state` | The field selects the actual BLK role; the supplied GLOB ID only resolves the physical quantity. |
| Occurrence | `COMPONENT`, `PHASE`, `PHASE_COMPONENT`, `CARDINALITY`, `MIN_FINITE`, `MIN_DISTINCT` | These qualifiers form the tool-constructed `ADVselector_*` composite identity. |
| System | `compounds`, matching modes, system type/size/scope, phases, literature | Declared systems and `BLKsubsys` views must not be conflated. |
| Numerical plan | `where`, `minimum_common_points`, `calculate`, `select`, `having`, `order_by`, `limit` | Row expressions, block aggregates, units, and aliases are checked at different stages. |
| ReAct state | three confirmation tokens | Every resubmission must otherwise be identical; semantic changes restart Gate 1. |

`fixed_constraints` and `inline_state` are not interchangeable complexity
options. Fixed constraints are block-level constraint declarations used mainly
with PureOrMixtureData. Inline state is attached to a named ReactionData target.
Similarly, parameters and targets are aligned row columns, while fixed or inline
state cannot be referenced as row-calculation aliases.

## 1. Exact grammar minimum — valid but too broad for normal agent use

```python
block_search_adv(
    targets="GLOBprop_34 AS conductivity",
    explanation="Return measured thermal-conductivity blocks.",
)
```

Actual database result: Gate 2 found 484 bindable blocks. The default `limit=50`
returned 50 real block results and marked the output truncated. This proves the
two-field contract is executable, but it is usually an inefficient agent query.

## 2. Recommended final simple chemistry input

```python
block_search_adv(
    targets="GLOBprop_34 AS conductivity",
    literature="GLOBlit_1",
    explanation="Return thermal-conductivity blocks in literature record 1.",
)
```

This three-field chemistry request returned two nontrivial results:

| Literature | Block | System | Complete points | Mean conductivity |
|---|---|---|---:|---:|
| `GLOBlit_1`; DOI `10.1007/s10765-005-5566-6` | `PROPblock_1` | unary | 77 | 0.026388961 W/(m K) |
| `GLOBlit_1`; DOI `10.1007/s10765-005-5566-6` | `PROPblock_2` | binary | 180 | 0.034542667 W/(m K) |

This is the preferred simple shape: one target, one compact global search
anchor, and one clear purpose. A compound/system filter can replace the
literature anchor when the question is system-centered. Calls 2–4 repeat these
three chemistry arguments unchanged while adding the returned tokens.

## 3. Maximum-meaningful PureOrMixtureData input

The validated mixture request uses 20 semantic top-level arguments. It exercises
component-specific role translation, system and phase scoping, two fixed
constraints, row filtering, complete-point validation, nested calculations,
five aggregates, `HAVING`, multi-key ordering, and an explicit cap.

```python
block_search_adv(
    compounds="REQUIRE GLOBcomp_681 AS ionic_liquid IN system",
    compound_match="all",
    system_type="binary",
    system_scope="declared",
    system_size_min=2,
    system_size_max=2,
    parameters=(
        "GLOBconstr_3 AS x_ionic_liquid COMPONENT ionic_liquid "
        "PHASE GLOBphase_1 MIN_FINITE 3 MIN_DISTINCT 2 CARDINALITY ONE"
    ),
    targets=(
        "GLOBprop_17 AS h_excess PHASE GLOBphase_1 "
        "MIN_FINITE 3 CARDINALITY ONE"
    ),
    literature=[
        "GLOBlit_3317",
        "DOI=10.1016/j.jct.2010.11.014",
        "YEAR BETWEEN 2010 AND 2012",
    ],
    phases=["REQUIRE GLOBphase_1", "EXCLUDE GLOBphase_3"],
    phase_match="all",
    fixed_constraints=[
        "GLOBvar_3 AS pressure_constraint PHASE GLOBphase_1 "
        "MIN_FINITE 1 CARDINALITY ONE "
        "WHERE VALUE BETWEEN 101[kPa] AND 102[kPa]",
        "GLOBvar_1 AS temperature_constraint PHASE GLOBphase_1 "
        "MIN_FINITE 1 CARDINALITY ONE "
        "WHERE VALUE BETWEEN 298[K] AND 299[K]",
    ],
    where="x_ionic_liquid BETWEEN 0.2[1] AND 0.8[1]",
    minimum_common_points=3,
    calculate=[
        "EXP(LN(x_ionic_liquid)) AS x_roundtrip",
        "ABS(h_excess) / "
        "(x_roundtrip * (1[1] - x_roundtrip)) AS scaled_h",
    ],
    select=[
        "COUNT(*) AS point_count",
        "MEAN(h_excess) AS mean_h_excess",
        "MEAN(scaled_h) AS mean_scaled_h",
        "MIN(x_roundtrip) AS minimum_x",
        "MAX(x_roundtrip) AS maximum_x",
    ],
    having="point_count >= 3 AND mean_scaled_h IS NOT NULL",
    order_by=[
        "mean_scaled_h DESC NULLS LAST",
        "point_count DESC NULLS LAST",
    ],
    limit=10,
    explanation=(
        "Rank real binary ionic-liquid excess-enthalpy blocks at 298 K and "
        "about 101.3 kPa after component-specific composition filtering."
    ),
)
```

Actual result for `GLOBlit_3317` / DOI `10.1016/j.jct.2010.11.014`:

| Block | Complete points | x range | Mean excess enthalpy (kJ/mol) | Mean scaled magnitude |
|---|---:|---:|---:|---:|
| `PROPblock_1` | 3 | 0.31–0.64 | −5.710770 | 24.888049 |
| `PROPblock_4` | 4 | 0.30–0.79 | −2.781425 | 12.945067 |
| `PROPblock_7` | 4 | 0.31–0.80 | −2.126407 | 9.722672 |

All three bindings resolved `x_ionic_liquid` to the actual variable occurrence
`BLKvar_1`, `h_excess` to `BLKprop_1`, pressure to `BLKconstr_1 = 101.3 kPa`,
and temperature to `BLKconstr_2 = 298.15 K`. The output ordering matched the
requested descending scaled magnitude.

One important expression edge is visible here: the arithmetic result
`scaled_h` has a composite SI unit rather than the property's named `kJ/mol`
semantic label. A scale-bearing `HAVING` literal would require an explicitly
supported conversion; the tested query therefore uses the chemically neutral
and type-safe `mean_scaled_h IS NOT NULL` check.

## 4. Maximum-meaningful ReactionData companion

ReactionData uses target-linked inline state instead of pretending those values
are ordinary row parameters or block constraints. The tested request returned
`RXNblock_1` for `GLOBlit_74` / DOI `10.1007/s10765-009-0568-4`: one complete
point with reaction enthalpy −610.94 kJ/mol, magnitude 610.94 kJ/mol,
temperature 298.15 K, and pressure 200 kPa. Its full validated arguments and all
three review payloads are preserved in the test artifact linked below.

## Reproducible actual outputs

- Test driver: `_tmp/archive_202607_ThermoML_temp_script/test_folder/tool12_argument_complexity/analyze_argument_complexity.py` (repo root; archived campaign evidence)
- Gate evidence and compact real results: `_tmp/archive_202607_ThermoML_temp_script/test_folder/tool12_argument_complexity/argument_complexity_results.json`

Every case passed the three review loops with `raw_rows_read=false`; raw values
were opened only on the confirmed fourth call. No example above is a no-data or
identity-only result.
