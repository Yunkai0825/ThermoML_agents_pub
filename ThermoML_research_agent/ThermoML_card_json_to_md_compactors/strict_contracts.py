"""Strict current-schema guards shared by direct card compactors."""

from __future__ import annotations

from collections.abc import Iterable

from ThermoML_raw_json_to_card_db_parsers.id_schema import validate_nested_identifiers


def require_payload(
    payload: object,
    required_fields: Iterable[str],
    *,
    context: str,
) -> dict:
    """Require an exact current-schema object boundary without repairing it."""
    if not isinstance(payload, dict):
        raise TypeError(f"{context} must be an object")
    expected = set(required_fields)
    actual = set(payload)
    missing = expected.difference(actual)
    if missing:
        raise ValueError(f"{context} is missing required fields: {sorted(missing)}")
    unknown = actual.difference(expected)
    if unknown:
        raise ValueError(f"{context} has unsupported fields: {sorted(unknown)}")
    validate_nested_identifiers(payload, path=context)
    return payload


__all__ = ["require_payload"]
