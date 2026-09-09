"""Typed SQL-shaped expression validation and deterministic evaluation."""

from __future__ import annotations

import math
import statistics
from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Mapping

from .errors import (
    fail,
    exact_keys,
    pointer_join,
    require_array,
    require_object,
    require_string,
)
from .semantics import (
    DIMENSIONLESS,
    Dimension,
    divide_dimensions,
    multiply_dimensions,
    power_dimension,
    render_dimension,
    unit_dimension,
)


MAX_EXPRESSION_DEPTH = 12
MAX_EXPRESSION_NODES = 128
MAX_ABS_EXPONENT = 12


@dataclass(frozen=True)
class ExprType:
    scope: str  # row | block
    boolean: bool
    dimension: Dimension | None
    unit: str | None
    semantic_type: str | None
    contextual_literal: bool = False

    def as_block(self) -> "ExprType":
        return ExprType(
            scope="block",
            boolean=self.boolean,
            dimension=self.dimension,
            unit=self.unit,
            semantic_type=self.semantic_type,
            contextual_literal=False,
        )


def numeric_type(
    *,
    scope: str,
    dimension: Dimension | None,
    unit: str | None,
    semantic_type: str | None,
) -> ExprType:
    return ExprType(scope, False, dimension, unit, semantic_type)


def boolean_type(scope: str) -> ExprType:
    return ExprType(scope, True, None, None, "boolean")


def _scope(*types: ExprType) -> str:
    return "row" if any(value.scope == "row" for value in types) else "block"


def _require_numeric(value: ExprType, pointer: str) -> None:
    if value.boolean:
        fail("SEMANTIC_TYPE_MISMATCH", "Expected a numeric expression.", pointer)


def _require_boolean(value: ExprType, pointer: str) -> None:
    if not value.boolean:
        fail("SEMANTIC_TYPE_MISMATCH", "Expected a boolean expression.", pointer)


def _compatible_numeric(
    left: ExprType,
    right: ExprType,
    pointer: str,
) -> ExprType:
    _require_numeric(left, pointer)
    _require_numeric(right, pointer)
    scope = _scope(left, right)

    if left.contextual_literal and not right.contextual_literal:
        return ExprType(
            scope,
            False,
            right.dimension,
            right.unit,
            right.semantic_type,
        )
    if right.contextual_literal and not left.contextual_literal:
        return ExprType(
            scope,
            False,
            left.dimension,
            left.unit,
            left.semantic_type,
        )
    if left.dimension is None or right.dimension is None:
        fail(
            "QUANTITY_SEMANTICS_UNAVAILABLE",
            "Both operands require curated dimensional semantics.",
            pointer,
        )
    if left.dimension != right.dimension:
        fail(
            "UNIT_MISMATCH",
            "Expression operands have incompatible dimensions.",
            pointer,
            details={
                "left": render_dimension(left.dimension),
                "right": render_dimension(right.dimension),
            },
        )
    if (
        left.unit is not None
        and right.unit is not None
        and left.unit != right.unit
    ):
        fail(
            "UNIT_MISMATCH",
            "Automatic unit conversion is not permitted in v1.",
            pointer,
            details={"left": left.unit, "right": right.unit},
        )
    if (
        left.semantic_type is not None
        and right.semantic_type is not None
        and left.semantic_type != right.semantic_type
    ):
        fail(
            "SEMANTIC_TYPE_MISMATCH",
            "Expression operands have incompatible chemical semantics.",
            pointer,
            details={
                "left": left.semantic_type,
                "right": right.semantic_type,
            },
        )
    return ExprType(
        scope,
        False,
        left.dimension,
        left.unit or right.unit,
        left.semantic_type or right.semantic_type,
    )


def _literal_type(node: dict[str, Any], pointer: str) -> ExprType:
    exact_keys(
        node,
        pointer,
        allowed={"literal", "unit", "semantic_type"},
        required={"literal"},
    )
    value = node["literal"]
    if isinstance(value, bool):
        if "unit" in node or "semantic_type" in node:
            fail(
                "SEMANTIC_TYPE_MISMATCH",
                "Boolean literals cannot carry numerical semantics.",
                pointer,
            )
        return boolean_type("block")
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        fail(
            "INVALID_REQUEST",
            "Only finite numerical or boolean literals are supported.",
            f"{pointer}/literal",
        )
    if not math.isfinite(float(value)):
        fail(
            "INVALID_REQUEST",
            "Numerical literals must be finite.",
            f"{pointer}/literal",
        )
    unit = node.get("unit")
    semantic_type = node.get("semantic_type")
    if unit is not None:
        unit = require_string(unit, f"{pointer}/unit")
        dimension = unit_dimension(unit, f"{pointer}/unit")
    else:
        dimension = DIMENSIONLESS
    if semantic_type is not None:
        semantic_type = require_string(
            semantic_type,
            f"{pointer}/semantic_type",
        )
    return ExprType(
        "block",
        False,
        dimension,
        unit,
        semantic_type,
        contextual_literal=unit is None and semantic_type is None,
    )


def _validate_complexity(node: Any, pointer: str) -> None:
    stack = [(node, 1)]
    nodes = 0
    while stack:
        current, depth = stack.pop()
        nodes += 1
        if nodes > MAX_EXPRESSION_NODES or depth > MAX_EXPRESSION_DEPTH:
            fail(
                "EXPRESSION_TOO_COMPLEX",
                "Expression exceeds the v1 complexity limit.",
                pointer,
                details={
                    "max_nodes": MAX_EXPRESSION_NODES,
                    "max_depth": MAX_EXPRESSION_DEPTH,
                },
            )
        if isinstance(current, dict):
            stack.extend((value, depth + 1) for value in current.values())
        elif isinstance(current, list):
            stack.extend((value, depth + 1) for value in current)


def infer_expression(
    node: Any,
    references: Mapping[str, ExprType],
    pointer: str,
    *,
    allow_aggregates: bool,
) -> ExprType:
    _validate_complexity(node, pointer)
    return _infer(node, references, pointer, allow_aggregates=allow_aggregates)


def _infer(
    node: Any,
    references: Mapping[str, ExprType],
    pointer: str,
    *,
    allow_aggregates: bool,
) -> ExprType:
    obj = require_object(node, pointer)
    node_kinds = sum(
        key in obj for key in ("ref", "literal", "op", "aggregate")
    )
    if node_kinds != 1:
        fail(
            "INVALID_REQUEST",
            "Expression nodes require exactly one of ref, literal, op, aggregate.",
            pointer,
        )
    if "ref" in obj:
        exact_keys(obj, pointer, allowed={"ref"}, required={"ref"})
        ref = require_string(obj["ref"], f"{pointer}/ref")
        value = references.get(ref)
        if value is None:
            fail(
                "UNKNOWN_BINDING_REFERENCE",
                f"Unknown expression reference {ref!r}.",
                f"{pointer}/ref",
            )
        return value
    if "literal" in obj:
        return _literal_type(obj, pointer)
    if "aggregate" in obj:
        if not allow_aggregates:
            fail(
                "AGGREGATE_IN_WHERE",
                "Aggregate nodes are not permitted in this expression.",
                pointer,
            )
        aggregate = require_string(obj["aggregate"], f"{pointer}/aggregate")
        supported = {
            "count_rows",
            "count_nonnull",
            "count_distinct",
            "min",
            "max",
            "sum",
            "mean",
            "median",
            "stddev_sample",
        }
        if aggregate not in supported:
            fail(
                "INVALID_REQUEST",
                f"Unsupported aggregate {aggregate!r}.",
                f"{pointer}/aggregate",
            )
        if aggregate == "count_rows":
            exact_keys(
                obj,
                pointer,
                allowed={"aggregate"},
                required={"aggregate"},
            )
            return numeric_type(
                scope="block",
                dimension=DIMENSIONLESS,
                unit="1",
                semantic_type="count",
            )
        exact_keys(
            obj,
            pointer,
            allowed={"aggregate", "expr"},
            required={"aggregate", "expr"},
        )
        child = _infer(
            obj["expr"],
            references,
            f"{pointer}/expr",
            allow_aggregates=False,
        )
        _require_numeric(child, f"{pointer}/expr")
        if child.scope != "row":
            fail(
                "NONSCALAR_SELECT",
                "Aggregate input must be a row-valued expression.",
                f"{pointer}/expr",
            )
        if aggregate in {"count_nonnull", "count_distinct"}:
            return numeric_type(
                scope="block",
                dimension=DIMENSIONLESS,
                unit="1",
                semantic_type="count",
            )
        return child.as_block()

    op = require_string(obj["op"], f"{pointer}/op")
    arithmetic = {"add", "subtract", "multiply", "divide", "power"}
    unary = {"negate", "abs", "sqrt", "ln", "log10", "exp"}
    comparisons = {"eq", "ne", "lt", "lte", "gt", "gte"}
    boolean_ops = {"and", "or"}
    if op in arithmetic | unary | comparisons | boolean_ops | {
        "not",
        "is_null",
        "coalesce",
    }:
        exact_keys(
            obj,
            pointer,
            allowed={"op", "args"},
            required={"op", "args"},
        )
        args = require_array(obj["args"], f"{pointer}/args")
        if op in {"subtract", "divide", "power"} and len(args) != 2:
            fail(
                "INVALID_REQUEST",
                f"{op} requires exactly two arguments.",
                f"{pointer}/args",
            )
        if op in {"add", "multiply", "and", "or", "coalesce"} and len(args) < 2:
            fail(
                "INVALID_REQUEST",
                f"{op} requires at least two arguments.",
                f"{pointer}/args",
            )
        if op in unary | {"not", "is_null"} and len(args) != 1:
            fail(
                "INVALID_REQUEST",
                f"{op} requires exactly one argument.",
                f"{pointer}/args",
            )
        if op in comparisons and len(args) != 2:
            fail(
                "INVALID_REQUEST",
                f"{op} requires exactly two arguments.",
                f"{pointer}/args",
            )
        inferred = [
            _infer(
                value,
                references,
                pointer_join(f"{pointer}/args", index),
                allow_aggregates=allow_aggregates,
            )
            for index, value in enumerate(args)
        ]
        if op in {"and", "or", "not"}:
            for index, value in enumerate(inferred):
                _require_boolean(value, pointer_join(f"{pointer}/args", index))
            return boolean_type(_scope(*inferred))
        if op == "is_null":
            return boolean_type(inferred[0].scope)
        if op == "coalesce":
            result = inferred[0]
            for value in inferred[1:]:
                if result.boolean or value.boolean:
                    if not (result.boolean and value.boolean):
                        fail(
                            "SEMANTIC_TYPE_MISMATCH",
                            "coalesce arguments must share one type.",
                            pointer,
                        )
                    result = boolean_type(_scope(result, value))
                else:
                    result = _compatible_numeric(result, value, pointer)
            return result
        if op in comparisons:
            _compatible_numeric(inferred[0], inferred[1], pointer)
            return boolean_type(_scope(*inferred))
        if op in {"add", "subtract"}:
            result = inferred[0]
            for value in inferred[1:]:
                result = _compatible_numeric(result, value, pointer)
            return result
        if op in {"multiply", "divide"}:
            for index, value in enumerate(inferred):
                _require_numeric(value, pointer_join(f"{pointer}/args", index))
                if value.dimension is None:
                    fail(
                        "QUANTITY_SEMANTICS_UNAVAILABLE",
                        "Multiplication and division require known dimensions.",
                        pointer_join(f"{pointer}/args", index),
                    )
            dimension = inferred[0].dimension
            assert dimension is not None
            for value in inferred[1:]:
                assert value.dimension is not None
                dimension = (
                    multiply_dimensions(dimension, value.dimension)
                    if op == "multiply"
                    else divide_dimensions(dimension, value.dimension)
                )
            return numeric_type(
                scope=_scope(*inferred),
                dimension=dimension,
                unit=render_dimension(dimension),
                semantic_type=None,
            )
        if op == "power":
            base, exponent = inferred
            _require_numeric(base, f"{pointer}/args/0")
            _require_numeric(exponent, f"{pointer}/args/1")
            exponent_node = require_object(args[1], f"{pointer}/args/1")
            if set(exponent_node) - {"literal", "unit", "semantic_type"} or (
                "literal" not in exponent_node
            ):
                fail(
                    "INVALID_POWER",
                    "The exponent must be a bounded numerical literal.",
                    f"{pointer}/args/1",
                )
            exponent_value = exponent_node["literal"]
            if (
                isinstance(exponent_value, bool)
                or not isinstance(exponent_value, (int, float))
                or not math.isfinite(float(exponent_value))
                or abs(float(exponent_value)) > MAX_ABS_EXPONENT
            ):
                fail(
                    "INVALID_POWER",
                    "The exponent is outside the supported range.",
                    f"{pointer}/args/1",
                )
            if exponent.dimension != DIMENSIONLESS:
                fail(
                    "INVALID_POWER",
                    "The exponent must be dimensionless.",
                    f"{pointer}/args/1",
                )
            if base.dimension is None:
                fail(
                    "QUANTITY_SEMANTICS_UNAVAILABLE",
                    "Power requires known base dimensions.",
                    f"{pointer}/args/0",
                )
            if (
                base.dimension != DIMENSIONLESS
                and float(exponent_value) != int(exponent_value)
            ):
                fail(
                    "INVALID_POWER",
                    "A dimensioned base requires an integer exponent.",
                    f"{pointer}/args/1",
                )
            fraction = Fraction(exponent_value).limit_denominator(64)
            dimension = power_dimension(base.dimension, fraction)
            return numeric_type(
                scope=_scope(base, exponent),
                dimension=dimension,
                unit=render_dimension(dimension),
                semantic_type=None,
            )
        child = inferred[0]
        _require_numeric(child, f"{pointer}/args/0")
        if op in {"negate", "abs"}:
            return child
        if child.dimension is None:
            fail(
                "QUANTITY_SEMANTICS_UNAVAILABLE",
                f"{op} requires curated dimensions.",
                f"{pointer}/args/0",
            )
        if op == "sqrt":
            dimension = power_dimension(child.dimension, Fraction(1, 2))
            return numeric_type(
                scope=child.scope,
                dimension=dimension,
                unit=render_dimension(dimension),
                semantic_type=None,
            )
        if child.dimension != DIMENSIONLESS:
            fail(
                "UNIT_MISMATCH",
                f"{op} requires a dimensionless input.",
                f"{pointer}/args/0",
            )
        return numeric_type(
            scope=child.scope,
            dimension=DIMENSIONLESS,
            unit="1",
            semantic_type=None,
        )

    if op == "between":
        exact_keys(
            obj,
            pointer,
            allowed={"op", "expr", "lower", "upper", "inclusive"},
            required={"op", "expr", "lower", "upper"},
        )
        expression = _infer(
            obj["expr"],
            references,
            f"{pointer}/expr",
            allow_aggregates=allow_aggregates,
        )
        lower = _infer(
            obj["lower"],
            references,
            f"{pointer}/lower",
            allow_aggregates=allow_aggregates,
        )
        upper = _infer(
            obj["upper"],
            references,
            f"{pointer}/upper",
            allow_aggregates=allow_aggregates,
        )
        _compatible_numeric(expression, lower, pointer)
        _compatible_numeric(expression, upper, pointer)
        inclusive = obj.get("inclusive", [True, True])
        if (
            not isinstance(inclusive, list)
            or len(inclusive) != 2
            or any(not isinstance(value, bool) for value in inclusive)
        ):
            fail(
                "INVALID_REQUEST",
                "inclusive must contain exactly two booleans.",
                f"{pointer}/inclusive",
            )
        return boolean_type(_scope(expression, lower, upper))

    if op == "in":
        exact_keys(
            obj,
            pointer,
            allowed={"op", "expr", "values"},
            required={"op", "expr", "values"},
        )
        expression = _infer(
            obj["expr"],
            references,
            f"{pointer}/expr",
            allow_aggregates=allow_aggregates,
        )
        values = require_array(obj["values"], f"{pointer}/values")
        if not values:
            fail(
                "INVALID_REQUEST",
                "Expression-level in requires at least one value.",
                f"{pointer}/values",
            )
        inferred_values = [
            _infer(
                value,
                references,
                pointer_join(f"{pointer}/values", index),
                allow_aggregates=allow_aggregates,
            )
            for index, value in enumerate(values)
        ]
        for value in inferred_values:
            _compatible_numeric(expression, value, pointer)
        return boolean_type(_scope(expression, *inferred_values))

    fail(
        "INVALID_REQUEST",
        f"Unsupported expression operation {op!r}.",
        f"{pointer}/op",
    )


def expression_references(node: Any) -> set[str]:
    refs: set[str] = set()
    stack = [node]
    while stack:
        current = stack.pop()
        if isinstance(current, dict):
            if set(current) == {"ref"} and isinstance(current["ref"], str):
                refs.add(current["ref"])
            else:
                stack.extend(current.values())
        elif isinstance(current, list):
            stack.extend(current)
    return refs


def _diagnostic_null(diagnostics: dict[str, int] | None) -> None:
    if diagnostics is not None:
        diagnostics["numeric_nulls"] = diagnostics.get("numeric_nulls", 0) + 1


def _sql_and(values: list[Any]) -> bool | None:
    if any(value is False for value in values):
        return False
    if any(value is None for value in values):
        return None
    return True


def _sql_or(values: list[Any]) -> bool | None:
    if any(value is True for value in values):
        return True
    if any(value is None for value in values):
        return None
    return False


def _apply_op(
    op: str,
    args: list[Any],
    diagnostics: dict[str, int] | None,
) -> Any:
    if op == "and":
        return _sql_and(args)
    if op == "or":
        return _sql_or(args)
    if op == "not":
        return None if args[0] is None else not args[0]
    if op == "is_null":
        return args[0] is None
    if op == "coalesce":
        return next((value for value in args if value is not None), None)
    if any(value is None for value in args):
        return None
    try:
        if op == "add":
            return sum(args)
        if op == "subtract":
            return args[0] - args[1]
        if op == "multiply":
            value = 1.0
            for arg in args:
                value *= arg
            return value
        if op == "divide":
            if args[1] == 0:
                _diagnostic_null(diagnostics)
                return None
            return args[0] / args[1]
        if op == "power":
            value = math.pow(args[0], args[1])
            if not math.isfinite(value):
                _diagnostic_null(diagnostics)
                return None
            return value
        if op == "negate":
            return -args[0]
        if op == "abs":
            return abs(args[0])
        if op == "sqrt":
            if args[0] < 0:
                _diagnostic_null(diagnostics)
                return None
            return math.sqrt(args[0])
        if op == "ln":
            if args[0] <= 0:
                _diagnostic_null(diagnostics)
                return None
            return math.log(args[0])
        if op == "log10":
            if args[0] <= 0:
                _diagnostic_null(diagnostics)
                return None
            return math.log10(args[0])
        if op == "exp":
            value = math.exp(args[0])
            if not math.isfinite(value):
                _diagnostic_null(diagnostics)
                return None
            return value
        if op == "eq":
            return args[0] == args[1]
        if op == "ne":
            return args[0] != args[1]
        if op == "lt":
            return args[0] < args[1]
        if op == "lte":
            return args[0] <= args[1]
        if op == "gt":
            return args[0] > args[1]
        if op == "gte":
            return args[0] >= args[1]
    except (ArithmeticError, OverflowError, ValueError, TypeError):
        _diagnostic_null(diagnostics)
        return None
    raise AssertionError(f"Unhandled operation {op!r}")


def evaluate_row(
    node: Any,
    row: Mapping[str, Any],
    diagnostics: dict[str, int] | None = None,
) -> Any:
    obj = node
    if "ref" in obj:
        return row.get(obj["ref"])
    if "literal" in obj:
        return obj["literal"]
    if "aggregate" in obj:
        raise AssertionError("Aggregate cannot be evaluated on one row")
    op = obj["op"]
    if op == "between":
        value = evaluate_row(obj["expr"], row, diagnostics)
        lower = evaluate_row(obj["lower"], row, diagnostics)
        upper = evaluate_row(obj["upper"], row, diagnostics)
        if value is None or lower is None or upper is None:
            return None
        inclusive = obj.get("inclusive", [True, True])
        lower_ok = value >= lower if inclusive[0] else value > lower
        upper_ok = value <= upper if inclusive[1] else value < upper
        return lower_ok and upper_ok
    if op == "in":
        value = evaluate_row(obj["expr"], row, diagnostics)
        if value is None:
            return None
        candidates = [
            evaluate_row(candidate, row, diagnostics)
            for candidate in obj["values"]
        ]
        if value in candidates:
            return True
        return None if any(candidate is None for candidate in candidates) else False
    args = [
        evaluate_row(argument, row, diagnostics)
        for argument in obj["args"]
    ]
    return _apply_op(op, args, diagnostics)


def _aggregate(
    node: dict[str, Any],
    rows: list[Mapping[str, Any]],
    diagnostics: dict[str, int] | None,
) -> Any:
    aggregate = node["aggregate"]
    if aggregate == "count_rows":
        return len(rows)
    values = [
        evaluate_row(node["expr"], row, diagnostics)
        for row in rows
    ]
    nonnull = [value for value in values if value is not None]
    if aggregate == "count_nonnull":
        return len(nonnull)
    if aggregate == "count_distinct":
        return len(set(nonnull))
    if not nonnull:
        return None
    if aggregate == "min":
        return min(nonnull)
    if aggregate == "max":
        return max(nonnull)
    if aggregate == "sum":
        return sum(nonnull)
    if aggregate == "mean":
        return statistics.fmean(nonnull)
    if aggregate == "median":
        return statistics.median(nonnull)
    if aggregate == "stddev_sample":
        return statistics.stdev(nonnull) if len(nonnull) >= 2 else None
    raise AssertionError(f"Unhandled aggregate {aggregate!r}")


def evaluate_block(
    node: Any,
    rows: list[Mapping[str, Any]],
    selected: Mapping[str, Any],
    diagnostics: dict[str, int] | None = None,
) -> Any:
    obj = node
    if "ref" in obj:
        return selected.get(obj["ref"])
    if "literal" in obj:
        return obj["literal"]
    if "aggregate" in obj:
        return _aggregate(obj, rows, diagnostics)
    op = obj["op"]
    if op == "between":
        value = evaluate_block(obj["expr"], rows, selected, diagnostics)
        lower = evaluate_block(obj["lower"], rows, selected, diagnostics)
        upper = evaluate_block(obj["upper"], rows, selected, diagnostics)
        if value is None or lower is None or upper is None:
            return None
        inclusive = obj.get("inclusive", [True, True])
        lower_ok = value >= lower if inclusive[0] else value > lower
        upper_ok = value <= upper if inclusive[1] else value < upper
        return lower_ok and upper_ok
    if op == "in":
        value = evaluate_block(obj["expr"], rows, selected, diagnostics)
        if value is None:
            return None
        candidates = [
            evaluate_block(candidate, rows, selected, diagnostics)
            for candidate in obj["values"]
        ]
        if value in candidates:
            return True
        return None if any(candidate is None for candidate in candidates) else False
    args = [
        evaluate_block(argument, rows, selected, diagnostics)
        for argument in obj["args"]
    ]
    return _apply_op(op, args, diagnostics)
