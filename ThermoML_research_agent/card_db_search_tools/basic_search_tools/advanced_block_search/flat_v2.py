"""Shallow, chemistry-oriented public contract for :func:`block_search_adv`.

Every public argument is a scalar or one ``list[str]``. SQL-like text is
parsed into the existing typed private query plan; it is never executed as
SQL or Python. The private engine remains authoritative for chemical role,
unit, cardinality, and exact-row validation.
"""

from __future__ import annotations

import ast
import math
import re
from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Mapping

from .engine import error_result
from .errors import AdvancedSearchError, fail, pointer_join, require_int, require_string
from .semantics import UNIT_DIMENSIONS


INPUT_CONTRACT = "block_search_adv/flat-v2"

_ALIAS_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]{0,63}$")
_GLOBAL_COMPOUND_RE = re.compile(r"^GLOBcomp_[1-9][0-9]*$")
_GLOBAL_PHASE_RE = re.compile(r"^GLOBphase_[1-9][0-9]*$")
_GLOBAL_LITERATURE_RE = re.compile(r"^GLOBlit_[1-9][0-9]*$")
_GLOBAL_QUANTITY_RE = re.compile(r"^GLOB(?:prop|var|constr)_[1-9][0-9]*$")
_SYSTEM_TYPE_RE = re.compile(
    r"^(?:unary|binary|ternary|quaternary|(?:[5-9]|[1-9][0-9]+)-component)$"
)
_SYSTEM_SCOPES = {"declared", "subsystem", "either"}

_COMPOUND_SCOPES = {
    "any",
    "system",
    "solvent",
    "participant",
    "reactant",
    "product",
}
_COMPOUND_MATCH = {"all", "any", "exact"}
_PHASE_MATCH = {"all", "any"}
_MAX_FLAT_ITEMS = 32
_MAX_CLAUSE_CHARS = 2_000
_NOT_NUMERIC = object()

_UNIT_ALIASES: dict[str, tuple[str, Decimal, Decimal]] = {
    unit: (unit, Decimal(1), Decimal(0)) for unit in UNIT_DIMENSIONS
}
_UNIT_ALIASES.update(
    {
        "J/(K*mol)": ("J/(K mol)", Decimal(1), Decimal(0)),
        "J/(K*m3)": ("J/(K m3)", Decimal(1), Decimal(0)),
        "J/(K*kg)": ("J/(K kg)", Decimal(1), Decimal(0)),
        "W/(m*K)": ("W/(m K)", Decimal(1), Decimal(0)),
        # Common chemistry input units are normalized to the exact canonical
        # units already used by the private engine. No runtime conversion is
        # delegated to the search engine.
        "MPa": ("kPa", Decimal(1000), Decimal(0)),
        "Pa": ("kPa", Decimal("0.001"), Decimal(0)),
        "bar": ("kPa", Decimal(100), Decimal(0)),
        "atm": ("kPa", Decimal("101.325"), Decimal(0)),
        "degC": ("K", Decimal(1), Decimal("273.15")),
        "°C": ("K", Decimal(1), Decimal("273.15")),
        "J/mol": ("kJ/mol", Decimal("0.001"), Decimal(0)),
        "mPa*s": ("Pa*s", Decimal("0.001"), Decimal(0)),
        "cP": ("Pa*s", Decimal("0.001"), Decimal(0)),
        "g/cm3": ("kg/m3", Decimal(1000), Decimal(0)),
        "g/mL": ("kg/m3", Decimal(1000), Decimal(0)),
    }
)
_UNIT_PATTERN = "|".join(
    re.escape(unit)
    for unit in sorted(_UNIT_ALIASES, key=len, reverse=True)
    if unit != "1"
)
_NUMBER_PATTERN = r"(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
_NUMBER_WITH_UNIT_RE = re.compile(
    rf"(?<![\w.])(?P<number>[+-]?{_NUMBER_PATTERN})"
    rf"\s+(?P<unit>{_UNIT_PATTERN})(?![\w/])"
)
_BRACKETED_NUMBER_WITH_UNIT_RE = re.compile(
    rf"(?<![\w.])(?P<number>[+-]?{_NUMBER_PATTERN})"
    rf"\s*\[(?P<unit>1|{_UNIT_PATTERN})\]"
)
_BOUND_PATTERN = (
    rf"(?:Q\(\s*[+-]?{_NUMBER_PATTERN}\s*,\s*'[^']+'\s*\)"
    rf"|[+-]?{_NUMBER_PATTERN})"
)
_BETWEEN_TAIL_RE = re.compile(
    rf"(?P<negated>NOT\s+)?BETWEEN\s+"
    rf"(?P<lower>{_BOUND_PATTERN})\s+AND\s+"
    rf"(?P<upper>{_BOUND_PATTERN})",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class CompiledFlatRequest:
    engine_kwargs: dict[str, Any]
    public_query: dict[str, Any]


def _flat_string_list(value: Any, pointer: str) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list):
        fail(
            "NESTING_NOT_ALLOWED",
            "Expected one string or one flat array containing only strings.",
            pointer,
        )
    if len(value) > _MAX_FLAT_ITEMS:
        fail(
            "INVALID_REQUEST",
            f"At most {_MAX_FLAT_ITEMS} entries are permitted.",
            pointer,
        )
    parsed: list[str] = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            fail(
                "NESTING_NOT_ALLOWED",
                "Flat arrays may contain only non-empty strings.",
                pointer_join(pointer, index),
            )
        clause = item.strip()
        if len(clause) > _MAX_CLAUSE_CHARS:
            fail(
                "INVALID_REQUEST",
                f"Each clause is limited to {_MAX_CLAUSE_CHARS} characters.",
                pointer_join(pointer, index),
            )
        if any(ord(character) < 32 for character in clause):
            fail(
                "INVALID_REQUEST",
                "Clauses cannot contain control characters or newlines.",
                pointer_join(pointer, index),
            )
        parsed.append(clause)
    return parsed


def _alias(value: str, pointer: str) -> str:
    received = require_string(value, pointer)
    alias = received.casefold()
    if not _ALIAS_RE.fullmatch(alias):
        fail(
            "INVALID_ALIAS",
            "Aliases must start with a letter and contain only letters, "
            "digits, or underscores.",
            pointer,
            details={"received": received},
        )
    if alias == "value":
        fail("INVALID_ALIAS", "The alias 'value' is reserved.", pointer)
    return alias


def _segments(value: str, pointer: str) -> list[str]:
    parts = [part.strip() for part in value.split("|")]
    if not parts or not parts[0] or any(not part for part in parts):
        fail(
            "INVALID_DECLARATION",
            "Declarations use non-empty segments separated by '|'.",
            pointer,
        )
    return parts


def _key_value(segment: str, pointer: str) -> tuple[str, str]:
    if "=" not in segment:
        fail(
            "INVALID_DECLARATION",
            "Expected a qualifier in key=value form.",
            pointer,
            details={"segment": segment},
        )
    key, value = segment.split("=", 1)
    key = key.strip().casefold()
    value = value.strip()
    if not key or not value:
        fail(
            "INVALID_DECLARATION",
            "Qualifier keys and values must be non-empty.",
            pointer,
            details={"segment": segment},
        )
    return key, value


def _quantity(value: str) -> dict[str, str]:
    return (
        {"global_id": value}
        if _GLOBAL_QUANTITY_RE.fullmatch(value)
        else {"key": value}
    )


def _component_alias(
    value: str,
    compounds: Mapping[str, str],
    pointer: str,
) -> str:
    normalized = value.casefold()
    if normalized in compounds:
        return normalized
    if _GLOBAL_COMPOUND_RE.fullmatch(value):
        matches = [
            alias
            for alias, global_id in compounds.items()
            if global_id == value
        ]
        if len(matches) == 1:
            return matches[0]
        if not matches:
            fail(
                "UNKNOWN_COMPOUND_REFERENCE",
                "Component IDs must also be declared in compounds.",
                pointer,
                details={"comp_num_id": value},
            )
        fail(
            "AMBIGUOUS_ALIAS",
            "The component ID has multiple compounds aliases.",
            pointer,
            details={"comp_num_id": value, "aliases": matches},
        )
    fail(
        "UNKNOWN_COMPOUND_REFERENCE",
        "Expected a compounds alias or GLOBcomp_N.",
        pointer,
        details={"received": value},
    )


def _compile_compounds(
    value: Any,
    *,
    compound_match: Any,
    system_type: Any,
    system_scope: Any,
    system_size_min: Any,
    system_size_max: Any,
) -> tuple[dict[str, Any], dict[str, str], dict[str, Any]]:
    entries = _flat_string_list(value, "/compounds")
    match_mode = require_string(compound_match, "/compound_match").casefold()
    if match_mode not in _COMPOUND_MATCH:
        fail(
            "INVALID_REQUEST",
            "compound_match must be all, any, or exact.",
            "/compound_match",
        )
    system_type_value: str | None = None
    if system_type is not None:
        system_type_value = require_string(
            system_type,
            "/system_type",
        ).casefold()
        if _SYSTEM_TYPE_RE.fullmatch(system_type_value) is None:
            fail(
                "INVALID_REQUEST",
                "Use canonical system types such as unary, binary, or ternary.",
                "/system_type",
                details={"received": system_type_value},
            )

    system_scope_value = require_string(
        system_scope, "/system_scope"
    ).casefold()
    if system_scope_value not in _SYSTEM_SCOPES:
        fail(
            "INVALID_REQUEST",
            "system_scope must be declared, subsystem, or either.",
            "/system_scope",
            details={"received": system_scope_value},
        )

    compiled: dict[str, Any] = {
        "all_of": [],
        "any_of": [],
        "none_of": [],
        "exact_system": match_mode == "exact",
        "system_scope": system_scope_value,
    }
    if system_type_value is not None:
        compiled["system_type"] = {"in": [system_type_value]}
    minimum_size: int | None = None
    maximum_size: int | None = None
    if system_size_min is not None:
        minimum_size = require_int(
            system_size_min,
            "/system_size_min",
            minimum=1,
            maximum=100,
        )
    if system_size_max is not None:
        maximum_size = require_int(
            system_size_max,
            "/system_size_max",
            minimum=1,
            maximum=100,
        )
    if (
        minimum_size is not None
        and maximum_size is not None
        and minimum_size > maximum_size
    ):
        fail(
            "INVALID_REQUEST",
            "system_size_min cannot exceed system_size_max.",
            "/system_size_min",
        )
    if minimum_size is not None or maximum_size is not None:
        compiled["system_size"] = {}
        if minimum_size is not None:
            compiled["system_size"]["min"] = minimum_size
        if maximum_size is not None:
            compiled["system_size"]["max"] = maximum_size

    alias_to_id: dict[str, str] = {}
    for index, declaration in enumerate(entries):
        pointer = pointer_join("/compounds", index)
        match = re.fullmatch(
            r"(?:(REQUIRE|ANY|EXCLUDE)\s+)?"
            r"(GLOBcomp_[1-9][0-9]*)\s+AS\s+"
            r"([A-Za-z][A-Za-z0-9_]{0,63})"
            r"(?:\s+(?:IN|SCOPE)\s+"
            r"(any|system|solvent|participant|reactant|product))?",
            declaration,
            re.IGNORECASE,
        )
        if match is None:
            fail(
                "INVALID_DECLARATION",
                "Use '[REQUIRE|ANY|EXCLUDE] GLOBcomp_N AS alias "
                "[IN scope]'.",
                pointer,
                details={"clause": declaration},
            )
        clause_mode = (
            match.group(1).casefold()
            if match.group(1)
            else "any"
            if match_mode == "any"
            else "require"
        )
        global_id = match.group(2)
        if not _GLOBAL_COMPOUND_RE.fullmatch(global_id):
            fail(
                "UNKNOWN_COMPOUND",
                "Compound IDs use canonical spelling GLOBcomp_N.",
                pointer,
                details={"received": global_id},
            )
        alias = _alias(match.group(3), pointer)
        scope = (match.group(4) or "system").casefold()
        if global_id in alias_to_id.values():
            fail(
                "AMBIGUOUS_ALIAS",
                "Each compound ID may have only one public alias.",
                pointer,
                details={"comp_num_id": global_id},
            )
        if alias in alias_to_id:
            fail(
                "DUPLICATE_ALIAS",
                f"Compound alias {alias!r} is declared more than once.",
                pointer,
            )
        if match_mode == "exact" and clause_mode != "require":
            fail(
                "INVALID_DECLARATION",
                "compound_match='exact' permits only REQUIRE compounds.",
                pointer,
            )
        destination = {
            "require": "all_of",
            "any": "any_of",
            "exclude": "none_of",
        }[clause_mode]
        compiled[destination].append(
            {
                "as": alias,
                "identity": {"comp_num_id": global_id},
                "scope": scope,
            }
        )
        alias_to_id[alias] = global_id
    if match_mode == "exact" and not entries:
        fail(
            "INVALID_REQUEST",
            "compound_match='exact' requires at least one compound.",
            "/compounds",
        )
    return compiled, alias_to_id, {
        "compounds": entries,
        "compound_match": match_mode,
        "system_type": system_type_value,
        "system_scope": system_scope_value,
        "system_size_min": minimum_size,
        "system_size_max": maximum_size,
    }


def _unitize(text: str, pointer: str) -> str:
    def replace(match: re.Match[str]) -> str:
        unit, scale, offset = _UNIT_ALIASES[match.group("unit")]
        value = Decimal(match.group("number")) * scale + offset
        if value == 0:
            value = Decimal(0)
        normalized_float = float(value)
        if (
            not math.isfinite(normalized_float)
            or (value != 0 and normalized_float == 0)
        ):
            fail(
                "INVALID_EXPRESSION",
                "Unit literal is outside the finite numeric range.",
                pointer,
                details={"literal": match.group(0)},
            )
        normalized_number = repr(normalized_float)
        return f"Q({normalized_number}, {unit!r})"

    bracketed = _BRACKETED_NUMBER_WITH_UNIT_RE.sub(replace, text)
    return _NUMBER_WITH_UNIT_RE.sub(replace, bracketed)


def _replace_between(text: str, pointer: str) -> str:
    current = text
    while True:
        match = _BETWEEN_TAIL_RE.search(current)
        if match is None:
            break
        cursor = match.start()
        while cursor > 0 and current[cursor - 1].isspace():
            cursor -= 1
        if cursor <= 0:
            break
        end = cursor
        if current[cursor - 1] == ")":
            depth = 0
            quote: str | None = None
            opening: int | None = None
            for index in range(cursor - 1, -1, -1):
                character = current[index]
                if character in {"'", '"'}:
                    quote = None if quote == character else character
                    continue
                if quote is not None:
                    continue
                if character == ")":
                    depth += 1
                elif character == "(":
                    depth -= 1
                    if depth == 0:
                        opening = index
                        break
            if opening is None:
                break
            start = opening
            identifier_end = opening
            identifier_start = identifier_end
            while (
                identifier_start > 0
                and (
                    current[identifier_start - 1].isalnum()
                    or current[identifier_start - 1] == "_"
                )
            ):
                identifier_start -= 1
            if (
                identifier_start < identifier_end
                and (
                    current[identifier_start].isalpha()
                    or current[identifier_start] == "_"
                )
            ):
                start = identifier_start
        else:
            start = cursor
            while (
                start > 0
                and (
                    current[start - 1].isalnum()
                    or current[start - 1] == "_"
                )
            ):
                start -= 1
            if start == end or not current[start].isalpha():
                break
        left = current[start:end].strip()
        expression = (
            f"between({left}, {match.group('lower')}, "
            f"{match.group('upper')})"
        )
        if match.group("negated"):
            expression = f"not ({expression})"
        current = f"{current[:start]}{expression}{current[match.end():]}"
    if re.search(r"\sBETWEEN\s", current, re.IGNORECASE):
        fail(
            "INVALID_EXPRESSION",
            "BETWEEN requires an alias or parenthesized expression and two "
            "numerical bounds.",
            pointer,
            details={"expression": text},
        )
    return current


def _pythonize_expression(text: str, pointer: str) -> str:
    expression = require_string(text, pointer)
    if len(expression) > _MAX_CLAUSE_CHARS:
        fail(
            "EXPRESSION_TOO_COMPLEX",
            f"Expressions are limited to {_MAX_CLAUSE_CHARS} characters.",
            pointer,
        )
    if (
        ";" in expression
        or "--" in expression
        or "/*" in expression
        or "*/" in expression
        or "`" in expression
    ):
        fail(
            "INVALID_EXPRESSION",
            "SQL statements, comments, and quoted identifiers are not accepted.",
            pointer,
        )
    expression = re.sub(
        r"\bCOUNT\s*\(\s*\*\s*\)",
        "count_rows()",
        expression,
        flags=re.IGNORECASE,
    )
    expression = _unitize(expression, pointer)
    expression = _replace_between(expression, pointer)
    expression = expression.replace("<>", "!=").replace("^", "**")
    expression = re.sub(
        r"\bIS\s+NOT\s+NULL\b",
        "is not None",
        expression,
        flags=re.IGNORECASE,
    )
    expression = re.sub(
        r"\bIS\s+NULL\b",
        "is None",
        expression,
        flags=re.IGNORECASE,
    )
    for source, target in (
        ("AND", "and"),
        ("OR", "or"),
        ("NOT", "not"),
        ("IN", "in"),
        ("NULL", "None"),
        ("TRUE", "True"),
        ("FALSE", "False"),
    ):
        expression = re.sub(
            rf"\b{source}\b",
            target,
            expression,
            flags=re.IGNORECASE,
        )
    expression = re.sub(r"(?<![<>=!])=(?!=)", "==", expression)
    if len(expression) > _MAX_CLAUSE_CHARS:
        fail(
            "EXPRESSION_TOO_COMPLEX",
            "Normalized expression exceeds the parser size limit.",
            pointer,
        )
    return expression


def _call_name(node: ast.Call, pointer: str) -> str:
    if not isinstance(node.func, ast.Name):
        fail(
            "INVALID_EXPRESSION",
            "Only allowlisted function names are permitted.",
            pointer,
        )
    return node.func.id.casefold()


def _numeric_literal(node: ast.AST) -> int | float | object:
    if (
        isinstance(node, ast.Constant)
        and isinstance(node.value, (int, float))
        and not isinstance(node.value, bool)
    ):
        return node.value
    if (
        isinstance(node, ast.UnaryOp)
        and isinstance(node.op, (ast.UAdd, ast.USub))
        and isinstance(node.operand, ast.Constant)
        and isinstance(node.operand.value, (int, float))
        and not isinstance(node.operand.value, bool)
    ):
        value = node.operand.value
        return -value if isinstance(node.op, ast.USub) else value
    return _NOT_NUMERIC


def _ast_to_expression(
    node: ast.AST,
    pointer: str,
    *,
    allow_aggregates: bool,
) -> dict[str, Any]:
    if isinstance(node, ast.Name):
        if node.id in {"True", "False"}:
            return {"literal": node.id == "True"}
        reference = node.id.casefold()
        if reference != "value" and not _ALIAS_RE.fullmatch(reference):
            fail(
                "INVALID_EXPRESSION",
                "Expression references must be declared aliases.",
                pointer,
                details={"reference": node.id},
            )
        return {"ref": reference}
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool):
            return {"literal": node.value}
        if isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            return {"literal": node.value}
        fail(
            "INVALID_EXPRESSION",
            "Only numerical and boolean literals are permitted.",
            pointer,
        )
    if isinstance(node, ast.UnaryOp):
        operand = _ast_to_expression(
            node.operand,
            pointer,
            allow_aggregates=allow_aggregates,
        )
        if isinstance(node.op, ast.USub):
            return {"op": "negate", "args": [operand]}
        if isinstance(node.op, ast.UAdd):
            return operand
        if isinstance(node.op, ast.Not):
            return {"op": "not", "args": [operand]}
        fail("INVALID_EXPRESSION", "Unsupported unary operation.", pointer)
    if isinstance(node, ast.BinOp):
        operation = {
            ast.Add: "add",
            ast.Sub: "subtract",
            ast.Mult: "multiply",
            ast.Div: "divide",
            ast.Pow: "power",
        }.get(type(node.op))
        if operation is None:
            fail("INVALID_EXPRESSION", "Unsupported arithmetic operation.", pointer)
        return {
            "op": operation,
            "args": [
                _ast_to_expression(
                    node.left,
                    pointer,
                    allow_aggregates=allow_aggregates,
                ),
                _ast_to_expression(
                    node.right,
                    pointer,
                    allow_aggregates=allow_aggregates,
                ),
            ],
        }
    if isinstance(node, ast.BoolOp):
        operation = "and" if isinstance(node.op, ast.And) else "or"
        return {
            "op": operation,
            "args": [
                _ast_to_expression(
                    item,
                    pointer,
                    allow_aggregates=allow_aggregates,
                )
                for item in node.values
            ],
        }
    if isinstance(node, ast.Compare):
        comparisons: list[dict[str, Any]] = []
        operands = [node.left, *node.comparators]
        for index, operation_node in enumerate(node.ops):
            left = _ast_to_expression(
                operands[index],
                pointer,
                allow_aggregates=allow_aggregates,
            )
            right_node = operands[index + 1]
            if isinstance(operation_node, (ast.In, ast.NotIn)):
                if not isinstance(right_node, (ast.Tuple, ast.List)):
                    fail(
                        "INVALID_EXPRESSION",
                        "IN requires a parenthesized literal list.",
                        pointer,
                    )
                values = [
                    _ast_to_expression(
                        item,
                        pointer,
                        allow_aggregates=allow_aggregates,
                    )
                    for item in right_node.elts
                ]
                expression: dict[str, Any] = {
                    "op": "in",
                    "expr": left,
                    "values": values,
                }
                if isinstance(operation_node, ast.NotIn):
                    expression = {"op": "not", "args": [expression]}
                comparisons.append(expression)
                continue
            if isinstance(operation_node, (ast.Is, ast.IsNot)):
                if not (
                    isinstance(right_node, ast.Constant)
                    and right_node.value is None
                ):
                    fail(
                        "INVALID_EXPRESSION",
                        "IS is supported only for NULL checks.",
                        pointer,
                    )
                expression = {"op": "is_null", "args": [left]}
                if isinstance(operation_node, ast.IsNot):
                    expression = {"op": "not", "args": [expression]}
                comparisons.append(expression)
                continue
            operation = {
                ast.Eq: "eq",
                ast.NotEq: "ne",
                ast.Lt: "lt",
                ast.LtE: "lte",
                ast.Gt: "gt",
                ast.GtE: "gte",
            }.get(type(operation_node))
            if operation is None:
                fail(
                    "INVALID_EXPRESSION",
                    "Unsupported comparison operation.",
                    pointer,
                )
            comparisons.append(
                {
                    "op": operation,
                    "args": [
                        left,
                        _ast_to_expression(
                            right_node,
                            pointer,
                            allow_aggregates=allow_aggregates,
                        ),
                    ],
                }
            )
        return (
            comparisons[0]
            if len(comparisons) == 1
            else {"op": "and", "args": comparisons}
        )
    if isinstance(node, ast.Call):
        function = _call_name(node, pointer)
        if node.keywords:
            fail(
                "INVALID_EXPRESSION",
                "Function calls do not accept keyword arguments.",
                pointer,
            )
        if function == "q":
            number = (
                _numeric_literal(node.args[0])
                if len(node.args) == 2
                else _NOT_NUMERIC
            )
            if (
                len(node.args) != 2
                or number is _NOT_NUMERIC
                or not isinstance(node.args[1], ast.Constant)
                or not isinstance(node.args[1].value, str)
            ):
                fail("INVALID_EXPRESSION", "Malformed unit literal.", pointer)
            return {
                "literal": number,
                "unit": node.args[1].value,
            }
        if function == "between":
            if len(node.args) != 3:
                fail("INVALID_EXPRESSION", "BETWEEN requires three terms.", pointer)
            return {
                "op": "between",
                "expr": _ast_to_expression(
                    node.args[0],
                    pointer,
                    allow_aggregates=allow_aggregates,
                ),
                "lower": _ast_to_expression(
                    node.args[1],
                    pointer,
                    allow_aggregates=allow_aggregates,
                ),
                "upper": _ast_to_expression(
                    node.args[2],
                    pointer,
                    allow_aggregates=allow_aggregates,
                ),
            }
        aggregate_names = {
            "count_rows": "count_rows",
            "count": "count_nonnull",
            "count_nonnull": "count_nonnull",
            "count_distinct": "count_distinct",
            "min": "min",
            "max": "max",
            "sum": "sum",
            "avg": "mean",
            "mean": "mean",
            "median": "median",
            "stddev": "stddev_sample",
            "stddev_samp": "stddev_sample",
            "stddev_sample": "stddev_sample",
        }
        if function in aggregate_names:
            if not allow_aggregates:
                fail(
                    "AGGREGATE_IN_WHERE",
                    "Aggregates are permitted only in SELECT.",
                    pointer,
                )
            aggregate = aggregate_names[function]
            if aggregate == "count_rows":
                if node.args:
                    fail(
                        "INVALID_EXPRESSION",
                        "COUNT(*) takes no compiled arguments.",
                        pointer,
                    )
                return {"aggregate": "count_rows"}
            if len(node.args) != 1:
                fail(
                    "INVALID_EXPRESSION",
                    f"{function.upper()} requires one argument.",
                    pointer,
                )
            return {
                "aggregate": aggregate,
                "expr": _ast_to_expression(
                    node.args[0],
                    pointer,
                    allow_aggregates=False,
                ),
            }
        function_names = {
            "abs": "abs",
            "sqrt": "sqrt",
            "ln": "ln",
            "log10": "log10",
            "exp": "exp",
            "power": "power",
            "pow": "power",
            "coalesce": "coalesce",
        }
        operation = function_names.get(function)
        if operation is None:
            fail(
                "INVALID_EXPRESSION",
                f"Unsupported function {function!r}.",
                pointer,
            )
        arguments = [
            _ast_to_expression(
                item,
                pointer,
                allow_aggregates=allow_aggregates,
            )
            for item in node.args
        ]
        return {"op": operation, "args": arguments}
    fail(
        "INVALID_EXPRESSION",
        f"Unsupported expression syntax {type(node).__name__}.",
        pointer,
    )


def _parse_expression(
    value: str,
    pointer: str,
    *,
    allow_aggregates: bool = False,
) -> dict[str, Any]:
    translated = _pythonize_expression(value, pointer)
    try:
        parsed = ast.parse(translated, mode="eval")
    except SyntaxError as exc:
        fail(
            "INVALID_EXPRESSION",
            "Could not parse the SQL-like expression.",
            pointer,
            details={
                "expression": value,
                "offset": exc.offset,
                "message": exc.msg,
            },
        )
    stack = [(parsed.body, 1)]
    node_count = 0
    while stack:
        node, depth = stack.pop()
        node_count += 1
        if node_count > 256 or depth > 20:
            fail(
                "EXPRESSION_TOO_COMPLEX",
                "Expression exceeds the parser complexity limit.",
                pointer,
                details={"max_nodes": 256, "max_depth": 20},
            )
        stack.extend(
            (child, depth + 1) for child in ast.iter_child_nodes(node)
        )
    return _ast_to_expression(
        parsed.body,
        pointer,
        allow_aggregates=allow_aggregates,
    )


def _compile_occurrences(
    value: Any,
    pointer: str,
    *,
    compounds: Mapping[str, str],
    fixed: bool = False,
    inline: bool = False,
) -> tuple[list[dict[str, Any]], list[str]]:
    entries = _flat_string_list(value, pointer)
    compiled: list[dict[str, Any]] = []
    aliases: set[str] = set()
    for index, declaration in enumerate(entries):
        item_pointer = pointer_join(pointer, index)
        condition: str | None = None
        prefix = declaration
        where_match = re.search(r"\s+WHERE\s+", declaration, re.IGNORECASE)
        if where_match is not None:
            prefix = declaration[: where_match.start()].strip()
            condition = declaration[where_match.end() :].strip()
            if not condition:
                fail(
                    "INVALID_DECLARATION",
                    "WHERE requires a condition.",
                    item_pointer,
                )
        tokens = prefix.split()
        if len(tokens) < 3 or tokens[1].casefold() != "as":
            fail(
                "INVALID_DECLARATION",
                (
                    "Use 'GLOBprop|var|constr_N AS alias' followed by "
                    "optional selector qualifiers."
                ),
                item_pointer,
                details={"clause": declaration},
            )
        identity = tokens[0]
        if not _GLOBAL_QUANTITY_RE.fullmatch(identity) and not re.fullmatch(
            r"[A-Za-z][A-Za-z0-9_{}.-]{0,127}",
            identity,
        ):
            fail(
                "INVALID_DECLARATION",
                "Quantity identity must be a GLOB ID or catalog key.",
                item_pointer,
                details={"identity": identity},
            )
        alias = _alias(tokens[2], item_pointer)
        if alias in aliases:
            fail(
                "DUPLICATE_ALIAS",
                f"Alias {alias!r} is declared more than once in this argument.",
                item_pointer,
            )
        aliases.add(alias)
        selector: dict[str, Any] = {
            "as": alias,
            "quantity": _quantity(identity),
            "observations": {
                "min_finite_values": 1,
                "min_distinct_values": 1,
            },
            "cardinality": "exactly_one",
        }
        cursor = 3
        while cursor < len(tokens):
            key = tokens[cursor].casefold()
            if key == "component":
                if cursor + 1 >= len(tokens):
                    fail(
                        "INVALID_DECLARATION",
                        "COMPONENT requires a declared compound alias.",
                        item_pointer,
                    )
                item = tokens[cursor + 1]
                selector["component"] = {
                    "compound_ref": _component_alias(
                        item,
                        compounds,
                        item_pointer,
                    )
                }
                cursor += 2
            elif key == "phase":
                if cursor + 1 >= len(tokens):
                    fail(
                        "INVALID_DECLARATION",
                        "PHASE requires GLOBphase_N.",
                        item_pointer,
                    )
                item = tokens[cursor + 1]
                if not _GLOBAL_PHASE_RE.fullmatch(item):
                    fail(
                        "UNKNOWN_PHASE",
                        "phase must be GLOBphase_N.",
                        item_pointer,
                    )
                selector["phase"] = {
                    "phase_num_id": item,
                    "match": "exact",
                }
                cursor += 2
            elif key == "phase_component":
                if cursor + 1 >= len(tokens):
                    fail(
                        "INVALID_DECLARATION",
                        "PHASE_COMPONENT requires a compound alias.",
                        item_pointer,
                    )
                item = tokens[cursor + 1]
                selector["phase_component"] = {
                    "compound_ref": _component_alias(
                        item,
                        compounds,
                        item_pointer,
                    )
                }
                cursor += 2
            elif key in {"min_finite", "min_points"}:
                if cursor + 1 >= len(tokens):
                    fail(
                        "INVALID_DECLARATION",
                        "MIN_FINITE requires a non-negative integer.",
                        item_pointer,
                    )
                item = tokens[cursor + 1]
                try:
                    parsed = int(item)
                except ValueError:
                    fail(
                        "INVALID_DECLARATION",
                        "MIN_FINITE must be a non-negative integer.",
                        item_pointer,
                    )
                if parsed < 0:
                    fail(
                        "INVALID_DECLARATION",
                        "MIN_FINITE must be non-negative.",
                        item_pointer,
                    )
                selector["observations"]["min_finite_values"] = parsed
                cursor += 2
            elif key == "min_distinct":
                if cursor + 1 >= len(tokens):
                    fail(
                        "INVALID_DECLARATION",
                        "MIN_DISTINCT requires a non-negative integer.",
                        item_pointer,
                    )
                item = tokens[cursor + 1]
                try:
                    parsed = int(item)
                except ValueError:
                    fail(
                        "INVALID_DECLARATION",
                        "min_distinct must be a non-negative integer.",
                        item_pointer,
                    )
                if parsed < 0:
                    fail(
                        "INVALID_DECLARATION",
                        "min_distinct must be non-negative.",
                        item_pointer,
                    )
                selector["observations"]["min_distinct_values"] = parsed
                cursor += 2
            elif key in {"cardinality", "match"}:
                if cursor + 1 >= len(tokens):
                    fail(
                        "INVALID_DECLARATION",
                        "CARDINALITY requires ONE or EACH.",
                        item_pointer,
                    )
                item = tokens[cursor + 1]
                normalized = item.casefold()
                if normalized not in {"one", "each", "all"}:
                    fail(
                        "INVALID_DECLARATION",
                        "CARDINALITY must be ONE or EACH.",
                        item_pointer,
                    )
                selector["cardinality"] = (
                    "exactly_one" if normalized == "one" else "all"
                )
                cursor += 2
            elif key == "on" and inline:
                if (
                    cursor + 2 >= len(tokens)
                    or tokens[cursor + 1].casefold() != "target"
                ):
                    fail(
                        "INVALID_DECLARATION",
                        "Inline state uses ON TARGET target_alias.",
                        item_pointer,
                    )
                selector["applies_to"] = _alias(
                    tokens[cursor + 2],
                    item_pointer,
                )
                cursor += 3
            elif key == "applies_to" and inline:
                if cursor + 1 >= len(tokens):
                    fail(
                        "INVALID_DECLARATION",
                        "APPLIES_TO requires a target alias.",
                        item_pointer,
                    )
                selector["applies_to"] = _alias(
                    tokens[cursor + 1],
                    item_pointer,
                )
                cursor += 2
            else:
                fail(
                    "INVALID_DECLARATION",
                    f"Unknown selector keyword {tokens[cursor]!r}.",
                    item_pointer,
                )
        if condition is not None and not fixed:
            fail(
                "INVALID_DECLARATION",
                "WHERE belongs in fixed_constraints or inline_state.",
                item_pointer,
            )
        if fixed:
            selector["condition"] = (
                {"literal": True}
                if condition is None
                else _parse_expression(
                    re.sub(
                        r"\bVALUE\b",
                        "value",
                        condition,
                        flags=re.IGNORECASE,
                    ),
                    item_pointer,
                )
            )
        if inline and "applies_to" not in selector:
            fail(
                "INLINE_TARGET_REQUIRED",
                "Inline state requires ON TARGET target_alias.",
                item_pointer,
            )
        compiled.append(selector)
    return compiled, entries


def _compile_literature(value: Any) -> tuple[dict[str, Any], list[str]]:
    entries = _flat_string_list(value, "/literature")
    compiled: dict[str, Any] = {}
    dois: list[str] = []
    lit_ids: list[str] = []
    for index, entry in enumerate(entries):
        pointer = pointer_join("/literature", index)
        if _GLOBAL_LITERATURE_RE.fullmatch(entry):
            lit_ids.append(entry)
            continue
        year_match = re.fullmatch(
            r"YEAR\s+BETWEEN\s+(\d{4})\s+AND\s+(\d{4})",
            entry,
            re.IGNORECASE,
        )
        if year_match is not None:
            if "year" in compiled:
                fail(
                    "INVALID_DECLARATION",
                    "Only one YEAR range is permitted.",
                    pointer,
                )
            compiled["year"] = {
                "min": int(year_match.group(1)),
                "max": int(year_match.group(2)),
            }
            continue
        text_match = re.fullmatch(
            r"(FIRST_AUTHOR|AUTHOR|JOURNAL)\s*(?:=|CONTAINS)\s*(.+)",
            entry,
            re.IGNORECASE,
        )
        if text_match is not None:
            field = (
                "first_author"
                if text_match.group(1).casefold() in {"first_author", "author"}
                else "journal"
            )
            if field in compiled:
                fail(
                    "INVALID_DECLARATION",
                    f"Only one {field.upper()} condition is permitted.",
                    pointer,
                )
            text = text_match.group(2).strip()
            if (
                len(text) >= 2
                and text[0] == text[-1]
                and text[0] in {"'", '"'}
            ):
                text = text[1:-1].strip()
            if not text:
                fail(
                    "INVALID_DECLARATION",
                    "Literature text conditions cannot be empty.",
                    pointer,
                )
            compiled[field] = text
            continue
        if "=" not in entry:
            dois.append(entry)
            continue
        key, item = _key_value(entry, pointer)
        if (
            len(item) >= 2
            and item[0] == item[-1]
            and item[0] in {"'", '"'}
        ):
            item = item[1:-1].strip()
        if key == "doi":
            dois.append(item)
        elif key in {"lit", "lit_num_id"}:
            if not _GLOBAL_LITERATURE_RE.fullmatch(item):
                fail(
                    "UNKNOWN_LITERATURE",
                    "Literature IDs must be GLOBlit_N.",
                    pointer,
                )
            lit_ids.append(item)
        elif key == "year":
            match = re.fullmatch(r"(\d{4})\.\.(\d{4})", item)
            if match is None:
                fail(
                    "INVALID_DECLARATION",
                    "year uses YYYY..YYYY.",
                    pointer,
                )
            if "year" in compiled:
                fail(
                    "INVALID_DECLARATION",
                    "Only one YEAR range is permitted.",
                    pointer,
                )
            compiled["year"] = {
                "min": int(match.group(1)),
                "max": int(match.group(2)),
            }
        elif key == "author":
            if "first_author" in compiled:
                fail(
                    "INVALID_DECLARATION",
                    "Only one FIRST_AUTHOR condition is permitted.",
                    pointer,
                )
            compiled["first_author"] = item
        elif key == "journal":
            if "journal" in compiled:
                fail(
                    "INVALID_DECLARATION",
                    "Only one JOURNAL condition is permitted.",
                    pointer,
                )
            compiled["journal"] = item
        else:
            fail(
                "INVALID_DECLARATION",
                f"Unknown literature qualifier {key!r}.",
                pointer,
            )
    if dois:
        compiled["doi_in"] = dois
    if lit_ids:
        compiled["lit_num_id_in"] = lit_ids
    return compiled, entries


def _compile_phases(
    value: Any,
    *,
    phase_match: Any,
) -> tuple[dict[str, list[str]], list[str], str]:
    entries = _flat_string_list(value, "/phases")
    match_mode = require_string(phase_match, "/phase_match").casefold()
    if match_mode not in _PHASE_MATCH:
        fail(
            "INVALID_REQUEST",
            "phase_match must be all or any.",
            "/phase_match",
        )
    compiled = {"all_of": [], "any_of": [], "none_of": []}
    for index, entry in enumerate(entries):
        pointer = pointer_join("/phases", index)
        match = re.fullmatch(
            r"(?:(REQUIRE|ANY|EXCLUDE)\s+)?"
            r"(GLOBphase_[1-9][0-9]*)",
            entry,
            re.IGNORECASE,
        )
        if match is None:
            fail(
                "UNKNOWN_PHASE",
                "Use '[REQUIRE|ANY|EXCLUDE] GLOBphase_N'.",
                pointer,
            )
        clause_mode = (
            match.group(1).casefold()
            if match.group(1)
            else "any"
            if match_mode == "any"
            else "require"
        )
        destination = {
            "require": "all_of",
            "any": "any_of",
            "exclude": "none_of",
        }[clause_mode]
        compiled[destination].append(match.group(2))
    return compiled, entries, match_mode


def _compile_minimum(
    value: Any,
    *,
    row_aliases: list[str],
) -> tuple[dict[str, Any] | None, int | None]:
    if value is None:
        return None, None
    count = require_int(
        value,
        "/minimum_common_points",
        minimum=1,
        maximum=1_000_000,
    )
    if not row_aliases:
        fail(
            "INVALID_REQUEST",
            "minimum_common_points requires at least one parameter or target.",
            "/minimum_common_points",
        )
    return {"count": count, "of": row_aliases}, count


def _compile_operations(
    *,
    calculate_value: Any,
    select_value: Any,
    having_value: Any,
    order_by_value: Any,
) -> tuple[
    list[dict[str, Any]],
    list[dict[str, Any]] | None,
    dict[str, Any] | None,
    list[dict[str, Any]],
    dict[str, Any],
]:
    calculations = _flat_string_list(calculate_value, "/calculate")
    selections = _flat_string_list(select_value, "/select")
    order_entries = _flat_string_list(order_by_value, "/order_by")
    compute: list[dict[str, Any]] = []
    select: list[dict[str, Any]] = []
    order_by: list[dict[str, Any]] = []
    for index, entry in enumerate(calculations):
        pointer = pointer_join("/calculate", index)
        match = re.fullmatch(
            r"(.+)\s+AS\s+([a-z][a-z0-9_]*)",
            entry,
            re.IGNORECASE,
        )
        if match is None:
            fail(
                "INVALID_DECLARATION",
                "Calculated columns use '<row expression> AS alias'.",
                pointer,
            )
        compute.append(
            {
                "as": _alias(match.group(2), pointer),
                "expr": _parse_expression(match.group(1), pointer),
            }
        )
    for index, entry in enumerate(selections):
        pointer = pointer_join("/select", index)
        match = re.fullmatch(
            r"(.+)\s+AS\s+([a-z][a-z0-9_]*)",
            entry,
            re.IGNORECASE,
        )
        if match is None:
            fail(
                "INVALID_DECLARATION",
                "Selected block values use '<aggregate expression> AS alias'.",
                pointer,
            )
        select.append(
            {
                "as": _alias(match.group(2), pointer),
                "expr": _parse_expression(
                    match.group(1),
                    pointer,
                    allow_aggregates=True,
                ),
            }
        )
    having_text: str | None = None
    having: dict[str, Any] | None = None
    if having_value is not None:
        having_text = require_string(having_value, "/having")
        having = _parse_expression(
            having_text,
            "/having",
            allow_aggregates=True,
        )
    for index, entry in enumerate(order_entries):
        pointer = pointer_join("/order_by", index)
        body = entry
        nulls = "last"
        null_match = re.search(
            r"\s+NULLS\s+(FIRST|LAST)\s*$",
            body,
            re.IGNORECASE,
        )
        if null_match is not None:
            nulls = null_match.group(1).casefold()
            body = body[: null_match.start()].rstrip()
        direction = "asc"
        direction_match = re.search(
            r"\s+(ASC|DESC)\s*$",
            body,
            re.IGNORECASE,
        )
        if direction_match is not None:
            direction = direction_match.group(1).casefold()
            body = body[: direction_match.start()].rstrip()
        if not body:
            fail(
                "INVALID_DECLARATION",
                "ORDER BY requires a selected alias expression.",
                pointer,
            )
        order_by.append(
            {
                "expr": _parse_expression(body, pointer),
                "direction": direction,
                "nulls": nulls,
            }
        )
    return (
        compute,
        select or None,
        having,
        order_by,
        {
            "calculate": calculations,
            "select": selections,
            "having": having_text,
            "order_by": order_entries,
        },
    )


def compile_flat_request(
    *,
    compounds: Any,
    compound_match: Any,
    system_type: Any,
    system_scope: Any,
    system_size_min: Any,
    system_size_max: Any,
    parameters: Any,
    targets: Any,
    literature: Any,
    phases: Any,
    phase_match: Any,
    where: Any,
    fixed_constraints: Any,
    inline_state: Any,
    minimum_common_points: Any,
    calculate: Any,
    select: Any,
    having: Any,
    order_by: Any,
    limit: Any,
    explanation: Any,
) -> CompiledFlatRequest:
    compounds, compound_aliases, compound_public = _compile_compounds(
        compounds,
        compound_match=compound_match,
        system_type=system_type,
        system_scope=system_scope,
        system_size_min=system_size_min,
        system_size_max=system_size_max,
    )
    parameter_selectors, parameter_public = _compile_occurrences(
        parameters,
        "/parameters",
        compounds=compound_aliases,
    )
    target_selectors, target_public = _compile_occurrences(
        targets,
        "/targets",
        compounds=compound_aliases,
    )
    if not target_selectors:
        fail(
            "INVALID_REQUEST",
            "targets requires at least one measured-result declaration.",
            "/targets",
        )
    constraints, constraint_public = _compile_occurrences(
        fixed_constraints,
        "/fixed_constraints",
        compounds=compound_aliases,
        fixed=True,
    )
    inline_states, inline_public = _compile_occurrences(
        inline_state,
        "/inline_state",
        compounds=compound_aliases,
        fixed=True,
        inline=True,
    )
    literature_compiled, literature_public = _compile_literature(literature)
    phase_compiled, phase_public, phase_match_public = _compile_phases(
        phases,
        phase_match=phase_match,
    )
    row_aliases = [
        item["as"] for item in parameter_selectors + target_selectors
    ]
    where_public: str | None = None
    where_compiled: dict[str, Any] | None = None
    if where is not None:
        where_public = require_string(where, "/where", nonempty=False).strip()
        if where_public:
            where_compiled = _parse_expression(where_public, "/where")
    minimum, minimum_public = _compile_minimum(
        minimum_common_points,
        row_aliases=row_aliases,
    )
    compute, select, having, order_by, operations_public = _compile_operations(
        calculate_value=calculate,
        select_value=select,
        having_value=having,
        order_by_value=order_by,
    )
    limit_value = require_int(limit, "/limit", minimum=1, maximum=500)
    explanation_value = require_string(explanation, "/explanation")
    if "\n" in explanation_value or len(explanation_value) > 500:
        fail(
            "INVALID_REQUEST",
            "explanation must be one line of at most 500 characters.",
            "/explanation",
        )

    engine_kwargs = {
        "compound_list": compounds,
        "para_identity": parameter_selectors,
        "target_identity": target_selectors,
        "literature": literature_compiled,
        "phase": phase_compiled,
        "filtering_identity": [
            {"ref": alias} for alias in row_aliases
        ],
        "constraint_filter": constraints,
        "inline_state_filter": inline_states,
        "where": where_compiled,
        "minimum_common_points": minimum,
        "compute": compute,
        "select": select,
        "having": having,
        "order_by": order_by,
        "limit": limit_value,
        "explanation": explanation_value,
        "schema": "block_search_adv/v1",
    }
    public_query = {
        "input_contract": INPUT_CONTRACT,
        **compound_public,
        "parameters": parameter_public,
        "targets": target_public,
        "literature": literature_public,
        "phases": phase_public,
        "phase_match": phase_match_public,
        "where": where_public,
        "fixed_constraints": constraint_public,
        "inline_state": inline_public,
        "minimum_common_points": minimum_public,
        **operations_public,
        "limit": limit_value,
        "explanation": explanation_value,
    }
    return CompiledFlatRequest(engine_kwargs, public_query)


_PRIVATE_POINTERS = (
    ("/compound_list", "/compounds"),
    ("/para_identity", "/parameters"),
    ("/target_identity", "/targets"),
    ("/constraint_filter", "/fixed_constraints"),
    ("/inline_state_filter", "/inline_state"),
    ("/phase", "/phases"),
    ("/compute", "/calculate"),
    ("/filtering_identity", "/where"),
)


def public_error(error: AdvancedSearchError) -> AdvancedSearchError:
    pointer = error.pointer
    code = error.code
    for private, public in _PRIVATE_POINTERS:
        if pointer == private or pointer.startswith(f"{private}/"):
            pointer = f"{public}{pointer[len(private):]}"
            break
    if code == "UNKNOWN_BINDING_REFERENCE" and pointer.startswith("/where/"):
        code = "UNKNOWN_ALIAS"
        pointer = "/where"
    return AdvancedSearchError(
        code,
        error.message,
        pointer,
        error.details,
    )


def flat_error_result(
    error: AdvancedSearchError,
    *,
    explanation: Any = None,
) -> dict[str, Any]:
    return error_result(public_error(error), explanation=explanation)


__all__ = [
    "INPUT_CONTRACT",
    "compile_flat_request",
    "flat_error_result",
    "public_error",
]
