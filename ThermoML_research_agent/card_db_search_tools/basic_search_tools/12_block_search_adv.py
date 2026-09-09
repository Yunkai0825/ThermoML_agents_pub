"""Advanced chemistry-role search over exact, uncapped ThermoML data blocks."""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from advanced_block_search import (  # noqa: E402
    AdvancedSearchError,
    review_or_execute_flat_search,
    flat_error_result,
)


def block_search_adv(
    targets: str | list[str],
    explanation: str,
    compounds: str | list[str] | None = None,
    compound_match: str = "all",
    system_type: str | None = None,
    system_scope: str = "declared",
    system_size_min: int | None = None,
    system_size_max: int | None = None,
    parameters: str | list[str] | None = None,
    literature: str | list[str] | None = None,
    phases: str | list[str] | None = None,
    phase_match: str = "all",
    fixed_constraints: str | list[str] | None = None,
    inline_state: str | list[str] | None = None,
    where: str | None = None,
    minimum_common_points: int | None = 1,
    calculate: str | list[str] | None = None,
    select: str | list[str] | None = None,
    having: str | None = None,
    order_by: str | list[str] | None = None,
    limit: int = 50,
) -> dict:
    """Run uncommon, exact-row chemistry searches over ThermoML data blocks.

    INPUT SHAPE
    Each plural argument accepts one string or one flat ``list[str]``. Never
    pass dictionaries, objects, or nested arrays. ``targets`` is mandatory
    and nonempty. ``explanation`` is one sentence stating the chemistry goal.
    Never guess numeric ``GLOB...`` IDs; resolve human names first.

    AUTOMATIC PRE-EXECUTION REVIEW HIERARCHY
    One call is sufficient. The tool internally walks its mandatory
    three-gate review hierarchy — catalog/composite-ID enrichment, actual
    PCS/registry BLK binding, and final chemistry-intent/syntax validation —
    using content-addressed confirmations that also bind the current
    database state. Invalid chemistry or syntax fails closed with a specific
    error before any raw row is read; a valid call executes over the raw
    rows and returns block-level aggregate output plus the confirmed review
    evidence under ``preexecution_review``.
    No confirmation tokens are emitted by or requested from the caller.

    CHEMICAL ROLES AND ID TRANSLATION
    The argument fixes the actual block role: ``parameters`` bind varying
    columns (BLKvar), ``targets`` bind measured-result columns (BLKprop),
    ``fixed_constraints`` bind one-valued block constraints (BLKconstr), and
    ``inline_state`` binds one-valued state attached to a target. Any
    GLOBprop_N, GLOBvar_N, or GLOBconstr_N may identify the same physical
    quantity in any of these arguments: the internal prop-var-constr catalog
    first translates it to a canonical quantity, then binds only the role
    named by the argument. The GLOB ID prefix does not choose the block role.

    COMPOUNDS, SYSTEMS, AND PHASES
    Compound clause:
      ``[REQUIRE|ANY|EXCLUDE] GLOBcomp_N AS alias [IN scope]``
    where scope is system, solvent, participant, reactant, product, or any.
    REQUIRE clauses are AND; multiple ANY clauses form one OR group; EXCLUDE
    means NOT. An omitted mode follows ``compound_match`` (all, any, exact).
    ``compound_match='exact'`` permits only required compounds. Canonical
    ``system_type`` values are unary, binary, ternary, quaternary, and
    ``N-component`` for any N>=5; never use ``pure``. ``system_scope`` is
    exactly ``declared``, ``subsystem``, or ``either``. A subsystem result
    carries a non-null ``BLKsubsys_id`` and remains a view of its parent.
    Phase clause: ``[REQUIRE|ANY|EXCLUDE] GLOBphase_N`` with the same Boolean
    meanings; an omitted mode follows ``phase_match`` (all or any).

    IDENTITY DECLARATIONS
      ``GLOB*_N AS alias [COMPONENT compound_alias] [PHASE GLOBphase_N]
      [PHASE_COMPONENT compound_alias] [MIN_FINITE n] [MIN_DISTINCT n]
      [CARDINALITY ONE|EACH]``
    Aliases are case-insensitive and normalized to lowercase. Use COMPONENT
    to select a component-specific quantity and PHASE to disambiguate phase
    occurrences. ONE rejects ambiguity. EACH emits one independently
    filtered and aggregated binding_match per legitimate occurrence.

    FIXED AND INLINE EVIDENCE
    A fixed declaration may append ``WHERE VALUE <condition>``. Omitting
    WHERE means require one usable reported numeric value. Inline state also
    requires ``ON TARGET target_alias`` and may append the same WHERE clause.
    These aliases are automatically returned as ``fixed_filter_evidence``;
    they are evidence, not row columns, so do not reference them in WHERE,
    CALCULATE, or SELECT.

    SQL-LIKE ROW AND BLOCK OPERATIONS
    ``where`` filters common raw rows. ``calculate`` entries are row
    expressions written ``expression AS alias``. ``select`` entries are
    block aggregates written ``aggregate expression AS alias``. ``having``
    is a block predicate and may use selected aliases or direct aggregates.
    ``order_by`` uses selected aliases, e.g. ``mean_h DESC NULLS LAST``.
    ``minimum_common_points`` is applied after WHERE to finite common rows.
    BETWEEN accepts an alias or parenthesized expression. Units can be
    adjacent or spaced: ``293.15[K]`` and ``293.15 [K]`` are equivalent.
    Common inputs MPa, Pa, bar, atm, degC/°C, J/mol, mPa*s/cP, and g/cm3 are
    normalized to canonical ThermoML units before type checking.

    Supported row functions: ABS, SQRT, LN, LOG10, EXP, POWER, COALESCE.
    Supported aggregates: COUNT(*), COUNT, COUNT_DISTINCT, MIN, MAX, SUM,
    AVG/MEAN, MEDIAN, and STDDEV. Use arithmetic operators +, -, *, /, ^;
    Boolean operators AND, OR, NOT; comparisons; IN; BETWEEN; and IS NULL.
    ``select`` outputs are block-level scalars; row arrays are never
    returned. To read the actual data rows of one identified block, call
    ``search_blocks`` with ``block_number='GLOBlit_N::PROPblock_M'`` instead.
    This tool does not infer wildcard targets, joins between blocks, window
    operations, or a numerical derivative estimator.

    Literature entries accept a DOI, GLOBlit_N, ``YEAR BETWEEN y AND y``,
    ``FIRST_AUTHOR CONTAINS text``, or ``JOURNAL CONTAINS text``.
    """
    try:
        return review_or_execute_flat_search(
            compounds=compounds,
            compound_match=compound_match,
            system_type=system_type,
            system_scope=system_scope,
            system_size_min=system_size_min,
            system_size_max=system_size_max,
            parameters=parameters,
            targets=targets,
            literature=literature,
            phases=phases,
            phase_match=phase_match,
            fixed_constraints=fixed_constraints,
            inline_state=inline_state,
            where=where,
            minimum_common_points=minimum_common_points,
            calculate=calculate,
            select=select,
            having=having,
            order_by=order_by,
            limit=limit,
            explanation=explanation,
        )
    except AdvancedSearchError as exc:
        return flat_error_result(exc, explanation=explanation)
