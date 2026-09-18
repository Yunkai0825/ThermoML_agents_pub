"""Structured fail-closed errors for the advanced ThermoML block search."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, NoReturn


@dataclass
class AdvancedSearchError(ValueError):
    """One request or execution error with a stable machine-readable code."""

    code: str
    message: str
    pointer: str = ""
    details: dict[str, Any] | None = None

    def __post_init__(self) -> None:
        ValueError.__init__(self, self.message)

    def as_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "code": self.code,
            "message": self.message,
            "pointer": self.pointer or "/",
        }
        if self.details:
            payload["details"] = self.details
        return payload


def fail(
    code: str,
    message: str,
    pointer: str = "",
    *,
    details: dict[str, Any] | None = None,
) -> NoReturn:
    raise AdvancedSearchError(code, message, pointer, details)


def require_object(value: Any, pointer: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail("INVALID_REQUEST", "Expected an object.", pointer)
    return value


def require_array(value: Any, pointer: str) -> list[Any]:
    if not isinstance(value, list):
        fail("INVALID_REQUEST", "Expected an array.", pointer)
    return value


def require_string(
    value: Any,
    pointer: str,
    *,
    nonempty: bool = True,
) -> str:
    if not isinstance(value, str):
        fail("INVALID_REQUEST", "Expected a string.", pointer)
    if nonempty and not value.strip():
        fail("INVALID_REQUEST", "Expected a non-empty string.", pointer)
    return value


def require_int(
    value: Any,
    pointer: str,
    *,
    minimum: int | None = None,
    maximum: int | None = None,
) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        fail("INVALID_REQUEST", "Expected an integer.", pointer)
    if minimum is not None and value < minimum:
        fail(
            "INVALID_REQUEST",
            f"Expected an integer greater than or equal to {minimum}.",
            pointer,
        )
    if maximum is not None and value > maximum:
        fail(
            "INVALID_REQUEST",
            f"Expected an integer less than or equal to {maximum}.",
            pointer,
        )
    return value


def exact_keys(
    value: dict[str, Any],
    pointer: str,
    *,
    allowed: set[str],
    required: set[str] | None = None,
) -> None:
    required = required or set()
    unknown = sorted(set(value) - allowed)
    missing = sorted(required - set(value))
    if unknown or missing:
        fail(
            "INVALID_REQUEST",
            "Object fields do not match the contract.",
            pointer,
            details={"missing": missing, "unknown": unknown},
        )


def pointer_join(pointer: str, token: str | int) -> str:
    escaped = str(token).replace("~", "~0").replace("/", "~1")
    return f"{pointer}/{escaped}" if pointer else f"/{escaped}"
