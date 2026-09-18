"""Strict identifier validation at public ThermoML tool boundaries.

Search fields may contain human-readable names, structures, DOIs, or the
correct canonical global identifier.  Identifier-looking values are never
coerced: bare ordinals, the retired unscoped prefixes, and wrong-scope IDs
produce an explicit refinement error for the calling agent.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import wraps
import re
from typing import Callable, TypeAlias

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    GLOBAL_PREFIX_BY_FIELD,
    require_block_id,
    require_global_id,
)


GLOBAL_FIELD_BY_ENTITY: dict[str, str] = {
    "compound": "comp_num_id",
    "property": "prop_num_id",
    "measurement": "meas_num_id",
    "variable": "var_num_id",
    "constraint": "constr_num_id",
    "phase": "phase_num_id",
    "reference": "lit_num_id",
    "solvent": "solvent_num_id",
    "block_type": "blocktype_num_id",
    "reaction_type": "rxn_type_num_id",
}

SearchValue: TypeAlias = str | list[str] | None

_LEGACY_ID_RE = re.compile(
    r"^(?:comp|prop|var|constr|meas|phase|lit|solvent|block)_\d+$",
    re.IGNORECASE,
)
_SCOPED_ID_RE = re.compile(
    r"^(?:GLOB[A-Za-z]+|DOIcomp|DOIcompSample|BLK(?:comp|prop|var|constr)|"
    r"BLKpropAssessment|PROPblock|RXNblock)_",
)


@dataclass(frozen=True)
class IdentifierRefinementError(ValueError):
    """A caller supplied an ambiguous, legacy, or wrong-scope identifier."""

    field: str
    received: object
    expected: str
    reason: str

    @property
    def code(self) -> str:
        return "ID_REFINEMENT_REQUIRED"

    def __str__(self) -> str:
        return (
            f"{self.code}: field '{self.field}' received {self.received!r}; "
            f"{self.reason}. Expected {self.expected}."
        )

    def as_result(self) -> dict:
        return {
            "error": str(self),
            "error_code": self.code,
            "refinement": {
                "field": self.field,
                "received": self.received,
                "expected": self.expected,
                "reason": self.reason,
            },
        }


def expected_global_id(entity_type: str) -> str:
    field = GLOBAL_FIELD_BY_ENTITY[entity_type]
    return f"{GLOBAL_PREFIX_BY_FIELD[field]}<positive integer> or a human-readable search value"


def validate_search_atom(entity_type: str, value: object, *, field: str) -> str:
    """Return one valid search atom or raise :class:`IdentifierRefinementError`."""
    if isinstance(value, bool) or not isinstance(value, str):
        raise IdentifierRefinementError(
            field, value, expected_global_id(entity_type),
            "all identifier-bearing search inputs must be strings",
        )
    text = value.strip()
    if not text:
        return ""
    expected = expected_global_id(entity_type)
    if text.isdigit():
        raise IdentifierRefinementError(
            field, value, expected, "bare numeric identifiers have no declared scope"
        )
    if _LEGACY_ID_RE.fullmatch(text):
        raise IdentifierRefinementError(
            field, value, expected, "retired unscoped identifier syntax is forbidden"
        )
    if _SCOPED_ID_RE.match(text):
        global_field = GLOBAL_FIELD_BY_ENTITY[entity_type]
        try:
            return require_global_id(global_field, text)
        except ValueError as exc:
            raise IdentifierRefinementError(
                field, value, expected,
                "the identifier belongs to a different namespace or entity type",
            ) from exc
    return text


def require_global_tool_id(entity_type: str, value: object, *, field: str) -> str:
    """Require the exact global namespace for an ID-only tool parameter."""
    text = validate_search_atom(entity_type, value, field=field)
    global_field = GLOBAL_FIELD_BY_ENTITY[entity_type]
    try:
        return require_global_id(global_field, text)
    except ValueError as exc:
        raise IdentifierRefinementError(
            field, value,
            f"{GLOBAL_PREFIX_BY_FIELD[global_field]}<positive integer>",
            "this parameter accepts a canonical global ID, not free text",
        ) from exc


def validate_search_values(entity_type: str, raw: object, *, field: str) -> list[str]:
    """Validate one search string or a flat native list of search strings."""
    if raw is None:
        return []
    if isinstance(raw, list):
        values: list[str] = []
        for item in raw:
            if isinstance(item, list):
                raise IdentifierRefinementError(
                    field, raw, "a flat list of search strings",
                    "nested search arrays are not part of the tool contract",
                )
            atom = validate_search_atom(entity_type, item, field=field)
            if atom:
                if ";" in atom:
                    raise IdentifierRefinementError(
                        field, raw, "a flat native list of search strings",
                        "retired semicolon-encoded multi-value syntax is forbidden",
                    )
                values.append(atom)
        return values
    atom = validate_search_atom(entity_type, raw, field=field)
    if not atom:
        return []
    if ";" in atom:
        raise IdentifierRefinementError(
            field, raw, "one search string or a native list of search strings",
            "retired semicolon-encoded multi-value syntax is forbidden",
        )
    return [atom]


def require_typed_block_input(value: object, *, field: str = "block_number") -> str:
    """Require ``PROPblock_N`` or ``RXNblock_N`` without coercion."""
    if not isinstance(value, str):
        raise IdentifierRefinementError(
            field, value, "PROPblock_<positive integer> or RXNblock_<positive integer>",
            "block identifiers must be typed strings",
        )
    try:
        return require_block_id(value)
    except ValueError as exc:
        raise IdentifierRefinementError(
            field, value, "PROPblock_<positive integer> or RXNblock_<positive integer>",
            "untyped, numeric, and legacy block identifiers are forbidden",
        ) from exc


def refinement_errors_as_results(function: Callable) -> Callable:
    """Convert strict-ID validation failures into agent-actionable results."""
    @wraps(function)
    def wrapped(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except IdentifierRefinementError as exc:
            return exc.as_result()
    return wrapped
