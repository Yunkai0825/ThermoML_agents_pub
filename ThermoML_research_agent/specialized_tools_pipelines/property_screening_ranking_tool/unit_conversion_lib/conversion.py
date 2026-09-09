"""Validated affine unit conversions loaded from the local translation table."""

from __future__ import annotations

import csv
import hashlib
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any


_TABLE_PATH = Path(__file__).with_name("unit_translation_table.csv")


class UnitConversionError(ValueError):
    """Raised when a unit is unknown or dimensionally incompatible."""


@dataclass(frozen=True)
class UnitTransform:
    alias: str
    canonical_unit: str
    scale: float
    offset: float
    notes: str

    def convert_value(self, value: float) -> float:
        return value * self.scale + self.offset

    def convert_delta(self, value: float) -> float:
        return abs(value * self.scale)

    def as_dict(self) -> dict[str, Any]:
        return {
            "input_unit": self.alias,
            "canonical_unit": self.canonical_unit,
            "scale": self.scale,
            "offset": self.offset,
        }


def _normalized_key(value: str) -> str:
    return value.strip().replace("·", "*").casefold()


@lru_cache(maxsize=1)
def unit_translation_table_sha256() -> str:
    return hashlib.sha256(_TABLE_PATH.read_bytes()).hexdigest()

@lru_cache(maxsize=1)
def unit_translation_table() -> dict[str, UnitTransform]:
    table: dict[str, UnitTransform] = {}
    with _TABLE_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            transform = UnitTransform(
                alias=row["alias"],
                canonical_unit=row["canonical_unit"],
                scale=float(row["scale"]),
                offset=float(row["offset"]),
                notes=row.get("notes", ""),
            )
            key = _normalized_key(transform.alias)
            previous = table.get(key)
            if previous is not None and previous != transform:
                raise RuntimeError(
                    f"conflicting unit alias {transform.alias!r} in {_TABLE_PATH}"
                )
            table[key] = transform
    if not table:
        raise RuntimeError(f"unit translation table is empty: {_TABLE_PATH}")
    return table


def resolve_unit(input_unit: str, canonical_unit: str) -> UnitTransform:
    requested = input_unit.strip() or canonical_unit
    if not requested and not canonical_unit:
        return UnitTransform("", "", 1.0, 0.0, "unitless")
    transform = unit_translation_table().get(_normalized_key(requested))
    if transform is None:
        raise UnitConversionError(f"Unknown input unit {input_unit!r}.")
    if transform.canonical_unit != canonical_unit:
        raise UnitConversionError(
            f"Cannot convert {input_unit!r} to canonical unit "
            f"{canonical_unit!r}; it resolves to {transform.canonical_unit!r}."
        )
    return transform


def convert_value(value: float, input_unit: str, canonical_unit: str) -> float:
    return resolve_unit(input_unit, canonical_unit).convert_value(value)


def convert_delta(value: float, input_unit: str, canonical_unit: str) -> float:
    """Convert an interval width without applying an affine origin offset."""
    return resolve_unit(input_unit, canonical_unit).convert_delta(value)


def conversion_trace(
    *, value: float, input_unit: str, canonical_unit: str, role: str,
    is_delta: bool = False,
) -> tuple[float, dict[str, Any]]:
    transform = resolve_unit(input_unit, canonical_unit)
    converted = (
        transform.convert_delta(value)
        if is_delta
        else transform.convert_value(value)
    )
    trace = {
        "role": role,
        "input_value": value,
        **transform.as_dict(),
        "converted_value": converted,
        "is_interval_delta": is_delta,
    }
    return converted, trace


def accepted_units(canonical_unit: str) -> tuple[str, ...]:
    return tuple(
        sorted(
            transform.alias
            for transform in unit_translation_table().values()
            if transform.canonical_unit == canonical_unit
        )
    )