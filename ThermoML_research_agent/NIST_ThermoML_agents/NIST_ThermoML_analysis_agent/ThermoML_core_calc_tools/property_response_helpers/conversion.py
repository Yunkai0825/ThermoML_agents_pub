"""Validated affine unit conversions for authoritative property responses."""
from __future__ import annotations

import csv
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
