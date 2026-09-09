"""Embedded identity permutations and numeric statistics for PCS_INDIV blocks.

ThermoML's declared source role is authoritative: Property, Variable, and
Constraint occurrences are never reclassified from observed constancy.
Variation is reported separately through ``n_unique`` and ``is_varied``.

Global property/variable/constraint IDs are accepted as exact vocabulary
aliases through ``prop_var_constr_translations.csv``. Translation never
changes the matched occurrence's source role.
"""

from __future__ import annotations

import math
from collections import Counter
from typing import Iterable, Mapping

from ThermoML_raw_json_to_card_db_parsers.id_schema import require_block_local_id
from ThermoML_raw_json_to_card_db_parsers.shared_utils import system_type_label
from ThermoML_raw_json_to_card_db_parsers.identity_translation import (
    GlobalIdentityTranslations,
    ROLE_ORDER,
    TranslationRecord,
    get_global_identity_translations,
)


IDENTITY_INDEX_SCHEMA_VERSION = "pcs-block-identity-index-v2"
COMPOSITION_SUBSYSTEM_SCHEMA_VERSION = "pcs-composition-subsystem-v1"
_SOURCE_ROLE_ORDER = {
    "property": 0,
    "variable": 1,
    "constraint": 2,
    "inline_state": 3,
}


def _finite_values(values: Iterable[float]) -> tuple[list[float], int]:
    finite: list[float] = []
    nonfinite = 0
    for raw in values:
        value = float(raw)
        if math.isfinite(value):
            finite.append(value)
        else:
            nonfinite += 1
    return finite, nonfinite


def _sample_std(values: list[float], mean: float) -> float | None:
    if len(values) < 2:
        return None
    return math.sqrt(
        sum((value - mean) ** 2 for value in values) / (len(values) - 1)
    )


def _within_four_ulps(left: float, right: float) -> bool:
    """Return whether two finite floats differ only by representation noise."""
    tolerance = 4 * max(math.ulp(left), math.ulp(right))
    return abs(left - right) <= tolerance


def _numeric_statistics(
    values: Iterable[float],
    *,
    n_rows: int,
    n_limit_values: int = 0,
    n_applicable_points: int | None = None,
) -> dict[str, object]:
    if n_rows < 0:
        raise ValueError("n_rows must be nonnegative")
    if n_limit_values < 0:
        raise ValueError("n_limit_values must be nonnegative")
    finite, n_nonfinite = _finite_values(values)
    n_values = len(finite)
    accounted_rows = n_values + n_nonfinite + n_limit_values
    if accounted_rows > n_rows:
        raise ValueError(
            f"Numeric observations ({accounted_rows}) exceed n_rows ({n_rows})"
        )
    n_unique = len(set(finite))
    minimum = min(finite) if finite else None
    maximum = max(finite) if finite else None
    total = sum(finite) if finite else None
    mean = total / n_values if finite else None
    return {
        "n_rows": n_rows,
        "n_values": n_values,
        "n_missing": n_rows - accounted_rows,
        "n_nonfinite": n_nonfinite,
        "n_unique": n_unique,
        "minimum": minimum,
        "maximum": maximum,
        "sum": total,
        "mean": mean,
        "stddev_sample": _sample_std(finite, mean) if mean is not None else None,
        "coverage_fraction": (n_values / n_rows) if n_rows else None,
        "n_applicable_points": (
            n_values
            if n_applicable_points is None
            else (n_applicable_points if n_values else 0)
        ),
        "is_varied": n_unique > 1,
    }


def _phase_binding(
    source: Mapping[str, object] | None,
    component_map: Mapping[str, str],
) -> tuple[str | None, str | None, str | None]:
    if not source:
        return None, None, None
    phase_value = source.get("phase_num_id")
    phase_num_id = str(phase_value) if phase_value is not None else None
    component_value = source.get("component_org_num")
    phase_component_org_num = (
        str(component_value) if component_value is not None else None
    )
    phase_component_comp_num_id = _component_global_id(
        component_value, component_map
    )
    return (
        phase_num_id,
        phase_component_org_num,
        phase_component_comp_num_id,
    )


def _component_global_id(
    component_org_num: object,
    component_map: Mapping[str, str],
) -> str | None:
    if component_org_num is None:
        return None
    key = str(component_org_num)
    try:
        return component_map[key]
    except KeyError as exc:
        raise ValueError(
            f"Identity occurrence references {key!r}, which is absent from the "
            "block compound table"
        ) from exc


def _role_global_id(record: TranslationRecord, role: str) -> str | None:
    return record.global_id_for_role(role)


def _resolved_source_instance_key(
    record: TranslationRecord,
    component_org_num: str | None,
) -> str:
    """Resolve a canonical quantity template to one block occurrence."""
    placeholder = "{DOIcomp_id}"
    if record.component_linked:
        if component_org_num is None:
            raise ValueError(
                f"{record.quantity_key!r} requires a component binding"
            )
        if placeholder not in record.quantity_key:
            raise ValueError(
                f"Component-linked quantity {record.quantity_key!r} has no "
                f"{placeholder} placeholder"
            )
        return record.quantity_key.replace(placeholder, component_org_num)
    if component_org_num is not None:
        raise ValueError(
            f"{record.quantity_key!r} does not accept a component binding"
        )
    if placeholder in record.quantity_key:
        raise ValueError(
            f"Non-component quantity {record.quantity_key!r} retains a "
            f"{placeholder} placeholder"
        )
    return record.quantity_key


def _occurrence_row(
    *,
    occurrence_key: str,
    quantity_key: str,
    source_role: str,
    source_global_id: str | None,
    source_local_key: str,
    source_instance_key: str | None,
    component_org_num: str | None,
    comp_num_id: str | None,
    phase_num_id: str | None,
    phase_component_org_num: str | None,
    phase_component_comp_num_id: str | None,
    values: Iterable[float],
    n_rows: int,
    n_applicable_points: int | None = None,
    n_limit_values: int = 0,
    data_group: str = "data_points",
    applies_to_occurrence_key: str | None = None,
) -> dict[str, object]:
    statistics = _numeric_statistics(
        values,
        n_rows=n_rows,
        n_limit_values=n_limit_values,
        n_applicable_points=n_applicable_points,
    )
    return {
        "occurrence_key": occurrence_key,
        "quantity_key": quantity_key,
        "source_role": source_role,
        "source_global_id": source_global_id,
        "source_local_key": source_local_key,
        "source_instance_key": source_instance_key,
        "component_org_num": component_org_num,
        "comp_num_id": comp_num_id,
        "phase_num_id": phase_num_id,
        "phase_component_org_num": phase_component_org_num,
        "phase_component_comp_num_id": phase_component_comp_num_id,
        "data_group": data_group,
        "applies_to_occurrence_key": applies_to_occurrence_key,
        "n_limit_values": n_limit_values,
        **statistics,
    }


def _permutation_rows(
    occurrence: Mapping[str, object],
    record: TranslationRecord,
) -> list[dict[str, object]]:
    source_global_id = occurrence["source_global_id"]
    rows: list[dict[str, object]] = []
    for alias_role in ROLE_ORDER:
        search_global_id = _role_global_id(record, alias_role)
        if search_global_id is None:
            continue
        if occurrence["source_role"] == "inline_state":
            match_kind = "inline_context"
        elif search_global_id == source_global_id:
            match_kind = "source"
        else:
            match_kind = "translated"
        rows.append(
            {
                "search_global_id": search_global_id,
                "quantity_key": record.quantity_key,
                "occurrence_key": occurrence["occurrence_key"],
                "match_kind": match_kind,
            }
        )
    return rows


def _normal_occurrences(
    *,
    properties: list[dict],
    variables: list[dict],
    constraints: list[dict],
    component_map: Mapping[str, str],
    property_values: Mapping[int, list[float]],
    variable_values: Mapping[int, list[float]],
    property_limit_counts: Mapping[int, int],
    n_points: int,
    translations: GlobalIdentityTranslations,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    occurrences: list[dict[str, object]] = []
    permutations: list[dict[str, object]] = []

    for source_role, entries in (
        ("property", properties),
        ("variable", variables),
        ("constraint", constraints),
    ):
        for entry in entries:
            if source_role == "property":
                local_key = entry["BLKprop_id"]
                source_global_id = entry["prop_num_id"]
                source_instance_key = entry["prop_ID"]
                ordinal = int(str(local_key).split("_", 1)[1])
                values = property_values.get(ordinal, [])
                n_rows = n_points
                phase_binding = _phase_binding(
                    entry.get("property_phase"), component_map
                )
                n_limit_values = property_limit_counts.get(ordinal, 0)
                n_applicable_points = None
            elif source_role == "variable":
                local_key = entry["BLKvar_id"]
                source_global_id = entry["var_num_id"]
                source_instance_key = entry["var_id"]
                ordinal = int(str(local_key).split("_", 1)[1])
                values = variable_values.get(ordinal, [])
                n_rows = n_points
                phase_binding = _phase_binding(
                    entry.get("phase"), component_map
                )
                n_limit_values = 0
                n_applicable_points = None
            else:
                local_key = entry["BLKconstr_id"]
                source_global_id = entry["constr_num_id"]
                source_instance_key = entry["constr_id"]
                values = (
                    [entry["value"]] if entry.get("value") is not None else []
                )
                # A constraint is one declaration that applies to all data rows.
                n_rows = 1
                phase_binding = _phase_binding(
                    entry.get("phase"), component_map
                )
                n_limit_values = 0
                n_applicable_points = n_points

            record = translations.record_for_global_id(str(source_global_id))
            component_org_num = entry.get("component_org_num")
            if record.component_linked != (component_org_num is not None):
                raise ValueError(
                    f"{source_role} {local_key} / {source_global_id} disagrees "
                    "with the translation catalog on component linkage"
                )
            expected_instance_key = _resolved_source_instance_key(
                record,
                (
                    str(component_org_num)
                    if component_org_num is not None
                    else None
                ),
            )
            if str(source_instance_key) != expected_instance_key:
                raise ValueError(
                    f"{source_role} {local_key} has source instance "
                    f"{source_instance_key!r}; expected "
                    f"{expected_instance_key!r}"
                )
            occurrence = _occurrence_row(
                occurrence_key=f"{source_role}|{local_key}",
                quantity_key=record.quantity_key,
                source_role=source_role,
                source_global_id=str(source_global_id),
                source_local_key=str(local_key),
                source_instance_key=(
                    str(source_instance_key)
                    if source_instance_key is not None
                    else None
                ),
                component_org_num=(
                    str(component_org_num)
                    if component_org_num is not None
                    else None
                ),
                comp_num_id=_component_global_id(
                    component_org_num, component_map
                ),
                phase_num_id=phase_binding[0],
                phase_component_org_num=phase_binding[1],
                phase_component_comp_num_id=phase_binding[2],
                values=values,
                n_rows=n_rows,
                n_applicable_points=n_applicable_points,
                n_limit_values=n_limit_values,
            )
            occurrences.append(occurrence)
            permutations.extend(_permutation_rows(occurrence, record))

    return occurrences, permutations


def _inline_state_occurrences(
    *,
    properties: list[dict],
    property_values: Mapping[int, list[float]],
    component_map: Mapping[str, str],
    translations: GlobalIdentityTranslations,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    """Represent ReactionData property-level temperature/pressure context.

    These values are fixed for one property declaration rather than declared as
    a Variable or Constraint.  They therefore get an explicit ``inline_state``
    source role and a property-scoped applicability link; no source global ID is
    fabricated.
    """
    occurrences: list[dict[str, object]] = []
    permutations: list[dict[str, object]] = []
    field_to_quantity = (
        ("temperature_K", "temperature_k"),
        ("pressure_kPa", "pressure_kpa"),
    )
    for prop in properties:
        local_key = str(prop["BLKprop_id"])
        ordinal = int(local_key.split("_", 1)[1])
        target_key = f"property|{local_key}"
        target_points = sum(
            math.isfinite(float(value))
            for value in property_values.get(ordinal, [])
        )
        for source_field, quantity_key in field_to_quantity:
            value = prop.get(source_field)
            if value is None:
                continue
            record = translations.record_for_quantity_key(quantity_key)
            phase_binding = _phase_binding(
                prop.get("property_phase"), component_map
            )
            occurrence = _occurrence_row(
                occurrence_key=f"inline_state|{local_key}|{source_field}",
                quantity_key=quantity_key,
                source_role="inline_state",
                source_global_id=None,
                source_local_key=local_key,
                source_instance_key=source_field,
                component_org_num=None,
                comp_num_id=None,
                phase_num_id=phase_binding[0],
                phase_component_org_num=phase_binding[1],
                phase_component_comp_num_id=phase_binding[2],
                values=[value],
                n_rows=1,
                n_applicable_points=target_points,
                data_group="property_inline_state",
                applies_to_occurrence_key=target_key,
            )
            occurrences.append(occurrence)
            permutations.extend(_permutation_rows(occurrence, record))
    return occurrences, permutations


def _sort_occurrence(row: Mapping[str, object]) -> tuple[object, ...]:
    return (
        _SOURCE_ROLE_ORDER[str(row["source_role"])],
        str(row["source_local_key"]),
        str(row["source_instance_key"] or ""),
    )


def _sort_permutation(row: Mapping[str, object]) -> tuple[object, ...]:
    return (
        str(row["search_global_id"]),
        str(row["occurrence_key"]),
    )


def _compact_permutations(
    rows: list[dict[str, object]],
) -> dict[str, list[str]]:
    """Compact expanded alias/occurrence pairs for PCS JSON storage."""
    grouped: dict[str, list[str]] = {}
    for row in sorted(rows, key=_sort_permutation):
        search_global_id = str(row["search_global_id"])
        grouped.setdefault(search_global_id, []).append(
            str(row["occurrence_key"])
        )
    return grouped


def _expected_block_occurrences(
    block: Mapping[str, object],
) -> dict[str, dict[str, object]]:
    """Project immutable occurrence bindings from an existing PCS block."""
    compounds = block["compounds"]
    component_map = {
        str(compound["org_num"]): str(compound["comp_num_id"])
        for compound in compounds
    }
    n_points = int(block["data_summary"]["n_points"])
    expected: dict[str, dict[str, object]] = {}

    role_specs = (
        (
            "property",
            block["properties"],
            "BLKprop_id",
            "prop_num_id",
            "prop_ID",
            "property_phase",
        ),
        (
            "variable",
            block["variables"],
            "BLKvar_id",
            "var_num_id",
            "var_id",
            "phase",
        ),
        (
            "constraint",
            block["constraints"],
            "BLKconstr_id",
            "constr_num_id",
            "constr_id",
            "phase",
        ),
    )
    for (
        source_role,
        entries,
        local_field,
        global_field,
        instance_field,
        phase_field,
    ) in role_specs:
        for entry in entries:
            local_key = str(entry[local_field])
            component_org_num_raw = entry.get("component_org_num")
            component_org_num = (
                str(component_org_num_raw)
                if component_org_num_raw is not None
                else None
            )
            phase_binding = _phase_binding(
                entry.get(phase_field),
                component_map,
            )
            occurrence_key = f"{source_role}|{local_key}"
            if occurrence_key in expected:
                raise ValueError(
                    f"Duplicate {source_role} local declaration "
                    f"{local_key!r} in PCS block"
                )
            expected[occurrence_key] = {
                "source_role": source_role,
                "source_global_id": str(entry[global_field]),
                "source_local_key": local_key,
                "source_instance_key": (
                    str(entry[instance_field])
                    if entry.get(instance_field) is not None
                    else None
                ),
                "component_org_num": component_org_num,
                "comp_num_id": _component_global_id(
                    component_org_num_raw,
                    component_map,
                ),
                "phase_num_id": phase_binding[0],
                "phase_component_org_num": phase_binding[1],
                "phase_component_comp_num_id": phase_binding[2],
                "data_group": "data_points",
                "applies_to_occurrence_key": None,
                "n_rows": 1 if source_role == "constraint" else n_points,
            }

    if block["block_type"] == "ReactionData":
        for prop in block["properties"]:
            local_key = str(prop["BLKprop_id"])
            phase_binding = _phase_binding(
                prop.get("property_phase"),
                component_map,
            )
            for source_field in ("temperature_K", "pressure_kPa"):
                if prop.get(source_field) is None:
                    continue
                occurrence_key = (
                    f"inline_state|{local_key}|{source_field}"
                )
                if occurrence_key in expected:
                    raise ValueError(
                        f"Duplicate inline-state occurrence "
                        f"{occurrence_key!r} in PCS block"
                    )
                expected[occurrence_key] = {
                    "source_role": "inline_state",
                    "source_global_id": None,
                    "source_local_key": local_key,
                    "source_instance_key": source_field,
                    "component_org_num": None,
                    "comp_num_id": None,
                    "phase_num_id": phase_binding[0],
                    "phase_component_org_num": phase_binding[1],
                    "phase_component_comp_num_id": phase_binding[2],
                    "data_group": "property_inline_state",
                    "applies_to_occurrence_key": f"property|{local_key}",
                    "n_rows": 1,
                }

    return expected


def validate_block_identity_index(
    identity_index: Mapping[str, object],
    *,
    translations: GlobalIdentityTranslations,
    block: Mapping[str, object] | None = None,
) -> None:
    if not isinstance(identity_index, Mapping):
        raise TypeError("identity index must be an object")
    if identity_index.get("schema_version") != IDENTITY_INDEX_SCHEMA_VERSION:
        raise ValueError("Unexpected PCS block identity-index schema version")
    for field in ("n_occurrences", "n_key_permutations"):
        count = identity_index.get(field)
        if (
            isinstance(count, bool)
            or not isinstance(count, int)
            or count < 0
        ):
            raise ValueError(
                f"identity {field} must be a nonnegative integer"
            )
    source_role_counts = identity_index.get("source_role_counts")
    if not isinstance(source_role_counts, Mapping):
        raise TypeError("identity source_role_counts must be an object")
    for role, count in source_role_counts.items():
        if role not in _SOURCE_ROLE_ORDER:
            raise ValueError(
                f"identity source_role_counts has unknown role {role!r}"
            )
        if (
            isinstance(count, bool)
            or not isinstance(count, int)
            or count < 0
        ):
            raise ValueError(
                f"identity source_role_counts[{role!r}] must be a "
                "nonnegative integer"
            )
    statistics = identity_index.get("statistics")
    permutations = identity_index.get("key_permutations")
    if not isinstance(statistics, list) or not isinstance(
        permutations,
        Mapping,
    ):
        raise TypeError(
            "identity statistics must be a list and key_permutations an object"
        )

    by_occurrence: dict[str, Mapping[str, object]] = {}
    for row in statistics:
        if not isinstance(row, Mapping):
            raise TypeError("identity statistics rows must be objects")
        occurrence_key = str(row["occurrence_key"])
        if occurrence_key in by_occurrence:
            raise ValueError(f"Duplicate identity occurrence {occurrence_key!r}")
        by_occurrence[occurrence_key] = row
        source_role = str(row["source_role"])
        source_global_id = row["source_global_id"]
        record = translations.record_for_quantity_key(
            str(row["quantity_key"])
        )
        if source_role == "inline_state":
            if source_global_id is not None:
                raise ValueError(
                    f"{occurrence_key}: inline state cannot claim a source global ID"
                )
        else:
            expected_source_id = record.global_id_for_role(source_role)
            if source_global_id != expected_source_id:
                raise ValueError(
                    f"{occurrence_key}: source global ID {source_global_id!r} "
                    f"does not match the {source_role} catalog ID "
                    f"{expected_source_id!r}"
                )
            expected_instance_key = _resolved_source_instance_key(
                record,
                (
                    str(row["component_org_num"])
                    if row["component_org_num"] is not None
                    else None
                ),
            )
            if row["source_instance_key"] != expected_instance_key:
                raise ValueError(
                    f"{occurrence_key}: source_instance_key "
                    f"{row['source_instance_key']!r} does not match "
                    f"{expected_instance_key!r}"
                )

        count_fields = (
            "n_limit_values",
            "n_rows",
            "n_values",
            "n_missing",
            "n_nonfinite",
            "n_unique",
            "n_applicable_points",
        )
        for field in count_fields:
            value = row[field]
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ValueError(
                    f"{occurrence_key}: {field} must be a nonnegative integer"
                )
        accounted_rows = (
            row["n_values"]
            + row["n_missing"]
            + row["n_nonfinite"]
            + row["n_limit_values"]
        )
        if accounted_rows != row["n_rows"]:
            raise ValueError(
                f"{occurrence_key}: value/missing/nonfinite/limit counts "
                "do not reconcile with n_rows"
            )
        if source_role != "property" and row["n_limit_values"] != 0:
            raise ValueError(
                f"{occurrence_key}: only property observations may contain "
                "limit values"
            )
        if row["n_values"] < row["n_unique"]:
            raise ValueError(
                f"{occurrence_key}: n_unique cannot exceed n_values"
            )
        if not isinstance(row["is_varied"], bool):
            raise ValueError(f"{occurrence_key}: is_varied must be boolean")
        if row["is_varied"] != (row["n_unique"] > 1):
            raise ValueError(
                f"{occurrence_key}: is_varied disagrees with n_unique"
            )
        numeric_fields = (
            "minimum",
            "maximum",
            "sum",
            "mean",
            "stddev_sample",
        )
        for field in numeric_fields:
            value = row[field]
            if value is not None and (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
            ):
                raise ValueError(
                    f"{occurrence_key}: {field} must be finite or null"
                )
        if row["n_values"] == 0:
            if row["n_unique"] != 0 or any(
                row[field] is not None for field in numeric_fields
            ):
                raise ValueError(
                    f"{occurrence_key}: empty observations must have empty "
                    "numeric statistics"
                )
        else:
            if row["n_unique"] < 1:
                raise ValueError(
                    f"{occurrence_key}: populated observations require "
                    "at least one unique value"
                )
            if any(row[field] is None for field in ("minimum", "maximum", "sum", "mean")):
                raise ValueError(
                    f"{occurrence_key}: populated observations require "
                    "minimum, maximum, sum, and mean"
                )
            if row["minimum"] > row["maximum"]:
                raise ValueError(
                    f"{occurrence_key}: minimum cannot exceed maximum"
                )
            mean_below_minimum = (
                row["mean"] < row["minimum"]
                and not _within_four_ulps(
                    row["mean"],
                    row["minimum"],
                )
            )
            mean_above_maximum = (
                row["mean"] > row["maximum"]
                and not _within_four_ulps(
                    row["mean"],
                    row["maximum"],
                )
            )
            if mean_below_minimum or mean_above_maximum:
                raise ValueError(
                    f"{occurrence_key}: mean must lie between minimum and maximum"
                )
            if not math.isclose(
                row["sum"],
                row["mean"] * row["n_values"],
                rel_tol=1e-12,
                abs_tol=1e-12,
            ):
                raise ValueError(
                    f"{occurrence_key}: sum disagrees with mean and n_values"
                )
            if row["n_values"] < 2 and row["stddev_sample"] is not None:
                raise ValueError(
                    f"{occurrence_key}: one value cannot have sample deviation"
                )
            if row["n_values"] >= 2 and row["stddev_sample"] is None:
                raise ValueError(
                    f"{occurrence_key}: multiple values require sample deviation"
                )
            if (
                row["stddev_sample"] is not None
                and row["stddev_sample"] < 0
            ):
                raise ValueError(
                    f"{occurrence_key}: sample deviation cannot be negative"
                )
        expected_coverage = (
            row["n_values"] / row["n_rows"] if row["n_rows"] else None
        )
        coverage = row["coverage_fraction"]
        if coverage is not None and (
            isinstance(coverage, bool)
            or not isinstance(coverage, (int, float))
            or not math.isfinite(coverage)
        ):
            raise ValueError(
                f"{occurrence_key}: coverage_fraction must be finite or null"
            )
        if coverage != expected_coverage:
            raise ValueError(
                f"{occurrence_key}: coverage_fraction disagrees with counts"
            )

    seen_pairs: set[tuple[str, str]] = set()
    for search_global_id, occurrence_keys in permutations.items():
        if not isinstance(occurrence_keys, list):
            raise TypeError(
                f"Permutation entry {search_global_id!r} must be a list"
            )
        record = translations.record_for_global_id(str(search_global_id))
        for occurrence_key_raw in occurrence_keys:
            occurrence_key = str(occurrence_key_raw)
            if occurrence_key not in by_occurrence:
                raise ValueError(
                    f"Permutation references missing occurrence {occurrence_key!r}"
                )
            occurrence = by_occurrence[occurrence_key]
            pair = (str(search_global_id), occurrence_key)
            if pair in seen_pairs:
                raise ValueError(f"Duplicate identity permutation {pair!r}")
            seen_pairs.add(pair)
            if record.quantity_key != occurrence["quantity_key"]:
                raise ValueError(
                    f"Permutation {pair!r} crosses non-equivalent quantity keys"
                )

    expected_pairs = {
        (global_id, occurrence_key)
        for occurrence_key, occurrence in by_occurrence.items()
        for global_id in translations.record_for_quantity_key(
            str(occurrence["quantity_key"])
        ).global_ids
    }
    if seen_pairs != expected_pairs:
        missing = sorted(expected_pairs - seen_pairs)
        extra = sorted(seen_pairs - expected_pairs)
        raise ValueError(
            "identity key_permutations are incomplete or contain extras: "
            f"missing={missing[:5]!r}, extra={extra[:5]!r}"
        )
    for occurrence_key, occurrence in by_occurrence.items():
        target_key = occurrence["applies_to_occurrence_key"]
        if target_key is None:
            continue
        target = by_occurrence.get(str(target_key))
        if target is None or target["source_role"] != "property":
            raise ValueError(
                f"{occurrence_key}: applies_to_occurrence_key must reference "
                "a property occurrence in the same block"
            )

    expected_counts = Counter(str(row["source_role"]) for row in statistics)
    if (
        dict(sorted(expected_counts.items()))
        != dict(source_role_counts)
    ):
        raise ValueError(
            "identity source_role_counts do not match statistics rows"
        )
    if identity_index.get("n_occurrences") != len(statistics):
        raise ValueError("identity n_occurrences does not match statistics")
    if identity_index.get("n_key_permutations") != len(seen_pairs):
        raise ValueError(
            "identity n_key_permutations does not match key_permutations"
        )

    if block is not None:
        if not isinstance(block, Mapping):
            raise TypeError("PCS block must be an object")
        expected = _expected_block_occurrences(block)
        if set(by_occurrence) != set(expected):
            missing = sorted(set(expected) - set(by_occurrence))
            extra = sorted(set(by_occurrence) - set(expected))
            raise ValueError(
                "identity occurrences do not match the existing PCS block: "
                f"missing={missing[:5]!r}, extra={extra[:5]!r}"
            )
        binding_fields = (
            "source_role",
            "source_global_id",
            "source_local_key",
            "source_instance_key",
            "component_org_num",
            "comp_num_id",
            "phase_num_id",
            "phase_component_org_num",
            "phase_component_comp_num_id",
            "data_group",
            "applies_to_occurrence_key",
            "n_rows",
        )
        for occurrence_key, expected_row in expected.items():
            actual_row = by_occurrence[occurrence_key]
            for field in binding_fields:
                if actual_row[field] != expected_row[field]:
                    raise ValueError(
                        f"{occurrence_key}: {field} disagrees with the "
                        "existing PCS block"
                    )

            source_role = actual_row["source_role"]
            if source_role in {"property", "variable"}:
                expected_applicable = actual_row["n_values"]
            elif source_role == "constraint":
                expected_applicable = (
                    int(block["data_summary"]["n_points"])
                    if actual_row["n_values"]
                    else 0
                )
            else:
                target_key = actual_row["applies_to_occurrence_key"]
                expected_applicable = by_occurrence[target_key]["n_values"]
            if actual_row["n_applicable_points"] != expected_applicable:
                raise ValueError(
                    f"{occurrence_key}: n_applicable_points disagrees with "
                    "the existing PCS block"
                )


def _declared_ordinals(
    entries: Iterable[Mapping[str, object]],
    *,
    local_field: str,
    prefix: str,
) -> set[int]:
    ordinals: set[int] = set()
    for entry in entries:
        local_key = str(entry[local_field])
        expected_prefix = f"{prefix}_"
        if not local_key.startswith(expected_prefix):
            raise ValueError(
                f"{local_field}={local_key!r} must start with "
                f"{expected_prefix!r}"
            )
        try:
            ordinal = int(local_key[len(expected_prefix):])
        except ValueError as exc:
            raise ValueError(
                f"{local_field}={local_key!r} has no integer ordinal"
            ) from exc
        if ordinal <= 0:
            raise ValueError(
                f"{local_field}={local_key!r} must have a positive ordinal"
            )
        if ordinal in ordinals:
            raise ValueError(
                f"Duplicate {local_field} ordinal {ordinal!r}"
            )
        ordinals.add(ordinal)
    return ordinals


def _reject_orphan_observation_keys(
    mapping: Mapping[int, object],
    *,
    declared_ordinals: set[int],
    mapping_name: str,
) -> None:
    for ordinal in mapping:
        if (
            isinstance(ordinal, bool)
            or not isinstance(ordinal, int)
            or ordinal not in declared_ordinals
        ):
            raise ValueError(
                f"{mapping_name} contains orphan declaration ordinal "
                f"{ordinal!r}"
            )


def build_block_identity_index(
    *,
    properties: list[dict],
    variables: list[dict],
    constraints: list[dict],
    compounds: list[dict],
    property_values: Mapping[int, list[float]],
    variable_values: Mapping[int, list[float]],
    n_points: int,
    translations: GlobalIdentityTranslations,
    property_limit_counts: Mapping[int, int] | None = None,
    block_type: str,
) -> dict[str, object]:
    """Build the card-local statistics and exact key permutations for one block."""
    if block_type not in {"PureOrMixtureData", "ReactionData"}:
        raise ValueError(f"Unsupported ThermoML block_type {block_type!r}")
    for name, entries in (
        ("properties", properties),
        ("variables", variables),
        ("constraints", constraints),
        ("compounds", compounds),
    ):
        if not isinstance(entries, list):
            raise TypeError(f"{name} must be a list")
    for name, mapping in (
        ("property_values", property_values),
        ("variable_values", variable_values),
    ):
        if not isinstance(mapping, Mapping):
            raise TypeError(f"{name} must be an object keyed by ordinal")
    if property_limit_counts is None:
        property_limit_counts = {}
    elif not isinstance(property_limit_counts, Mapping):
        raise TypeError(
            "property_limit_counts must be an object keyed by ordinal"
        )
    for ordinal, count in property_limit_counts.items():
        if (
            isinstance(count, bool)
            or not isinstance(count, int)
            or count < 0
        ):
            raise ValueError(
                f"property_limit_counts[{ordinal!r}] must be a "
                "nonnegative integer"
            )
    if (
        isinstance(n_points, bool)
        or not isinstance(n_points, int)
        or n_points < 0
    ):
        raise ValueError("n_points must be a nonnegative integer")
    property_ordinals = _declared_ordinals(
        properties,
        local_field="BLKprop_id",
        prefix="BLKprop",
    )
    variable_ordinals = _declared_ordinals(
        variables,
        local_field="BLKvar_id",
        prefix="BLKvar",
    )
    _declared_ordinals(
        constraints,
        local_field="BLKconstr_id",
        prefix="BLKconstr",
    )
    _reject_orphan_observation_keys(
        property_values,
        declared_ordinals=property_ordinals,
        mapping_name="property_values",
    )
    _reject_orphan_observation_keys(
        variable_values,
        declared_ordinals=variable_ordinals,
        mapping_name="variable_values",
    )
    _reject_orphan_observation_keys(
        property_limit_counts,
        declared_ordinals=property_ordinals,
        mapping_name="property_limit_counts",
    )
    component_map = {
        str(compound["org_num"]): str(compound["comp_num_id"])
        for compound in compounds
    }
    normal_stats, normal_permutations = _normal_occurrences(
        properties=properties,
        variables=variables,
        constraints=constraints,
        component_map=component_map,
        property_values=property_values,
        variable_values=variable_values,
        property_limit_counts=property_limit_counts,
        n_points=n_points,
        translations=translations,
    )
    if block_type == "ReactionData":
        inline_stats, inline_permutations = _inline_state_occurrences(
            properties=properties,
            property_values=property_values,
            component_map=component_map,
            translations=translations,
        )
    else:
        inline_stats, inline_permutations = [], []
    statistics = sorted(normal_stats + inline_stats, key=_sort_occurrence)
    permutations = _compact_permutations(
        normal_permutations + inline_permutations
    )
    source_role_counts = dict(
        sorted(Counter(str(row["source_role"]) for row in statistics).items())
    )
    result: dict[str, object] = {
        "schema_version": IDENTITY_INDEX_SCHEMA_VERSION,
        "n_occurrences": len(statistics),
        "n_key_permutations": sum(
            len(occurrence_keys) for occurrence_keys in permutations.values()
        ),
        "source_role_counts": source_role_counts,
        "statistics": statistics,
        "key_permutations": permutations,
    }
    validate_block_identity_index(result, translations=translations)
    return result


def _validate_subsystem_point_runs(
    subsystem: Mapping[str, object],
    *,
    parent_n_points: int,
) -> set[int]:
    membership = subsystem.get("point_membership")
    if not isinstance(membership, Mapping):
        raise TypeError("composition subsystem point_membership must be an object")
    if membership.get("encoding") != "one_based_inclusive_runs":
        raise ValueError("composition subsystem point encoding is unsupported")
    runs = membership.get("runs")
    if not isinstance(runs, list):
        raise TypeError("composition subsystem point runs must be a list")
    points: set[int] = set()
    previous = 0
    for run in runs:
        if (
            not isinstance(run, list)
            or len(run) != 2
            or any(isinstance(value, bool) or not isinstance(value, int) for value in run)
        ):
            raise ValueError("composition subsystem point run must contain two integers")
        start, end = run
        if start <= previous or end < start or end > parent_n_points:
            raise ValueError("composition subsystem point runs overlap or exceed the parent block")
        points.update(range(start, end + 1))
        previous = end
    if subsystem.get("n_points") != len(points):
        raise ValueError("composition subsystem n_points disagrees with point runs")
    return points


def validate_card_composition_subsystems(
    card: Mapping[str, object],
    *,
    doi: str | None = None,
) -> int:
    """Validate authoritative composition views and their block-local links."""
    label = doi or "<card>"
    blocks = card.get("blocks")
    summary = card.get("blocks_summary")
    if not isinstance(blocks, list) or not isinstance(summary, Mapping):
        raise TypeError(f"{label}: PCS blocks and blocks_summary are required")
    derived = summary.get("derived_indexes")
    manifests = (
        derived.get("composition_subsystems")
        if isinstance(derived, Mapping)
        else None
    )
    if not isinstance(manifests, Mapping):
        raise ValueError(
            f"{label}: blocks_summary.derived_indexes.composition_subsystems is missing"
        )
    block_by_id = {
        block.get("block_number"): block
        for block in blocks
        if isinstance(block, Mapping)
    }
    if set(manifests) != set(block_by_id):
        raise ValueError(
            f"{label}: composition-subsystem keys do not match card blocks"
        )

    total = 0
    for block_id, block in block_by_id.items():
        entries = manifests[block_id]
        if not isinstance(entries, list):
            raise TypeError(f"{label}/{block_id}: subsystem manifest must be a list")
        compounds = block.get("compounds")
        properties = block.get("properties")
        variables = block.get("variables")
        constraints = block.get("constraints")
        data_summary = block.get("data_summary")
        if not all(isinstance(value, list) for value in (compounds, properties, variables, constraints)):
            raise TypeError(f"{label}/{block_id}: block declarations must be lists")
        if not isinstance(data_summary, Mapping):
            raise TypeError(f"{label}/{block_id}: data_summary must be an object")
        parent_n_points = data_summary.get("n_points")
        if isinstance(parent_n_points, bool) or not isinstance(parent_n_points, int) or parent_n_points < 0:
            raise ValueError(f"{label}/{block_id}: invalid parent n_points")
        parent_by_org = {item["org_num"]: item for item in compounds}
        prop_by_id = {item["BLKprop_id"]: item for item in properties}
        variable_ids = {item["BLKvar_id"] for item in variables}
        constraint_ids = {item["BLKconstr_id"] for item in constraints}
        membership_by_point: dict[int, set[str]] = {}
        eligible = 0
        expected_ids = []

        for ordinal, subsystem in enumerate(entries, start=1):
            if not isinstance(subsystem, Mapping):
                raise TypeError(f"{label}/{block_id}: subsystem entry must be an object")
            subsystem_id = subsystem.get("BLKsubsys_id")
            require_block_local_id("subsys", subsystem_id)
            expected_ids.append(f"BLKsubsys_{ordinal}")
            retained_rows = subsystem.get("retained_components")
            excluded_rows = subsystem.get("excluded_components")
            if not isinstance(retained_rows, list) or not isinstance(excluded_rows, list):
                raise TypeError("subsystem retained/excluded components must be lists")
            retained = {item.get("org_num") for item in retained_rows if isinstance(item, Mapping)}
            excluded = {item.get("org_num") for item in excluded_rows if isinstance(item, Mapping)}
            if (
                len(retained) != len(retained_rows)
                or len(excluded) != len(excluded_rows)
                or retained & excluded
                or retained | excluded != set(parent_by_org)
            ):
                raise ValueError("subsystem retained/excluded compounds must exactly partition the parent")
            if subsystem.get("n_retained_components") != len(retained):
                raise ValueError("subsystem n_retained_components is inconsistent")
            if subsystem.get("effective_system_type") != system_type_label(len(retained)):
                raise ValueError("subsystem effective_system_type is inconsistent")
            for projection in retained_rows + excluded_rows:
                parent = parent_by_org[projection["org_num"]]
                for field in ("comp_num_id", "name", "inchi_key"):
                    if projection.get(field) != parent.get(field):
                        raise ValueError(f"subsystem compound projection disagrees on {field}")

            points = _validate_subsystem_point_runs(
                subsystem,
                parent_n_points=parent_n_points,
            )
            for point in points:
                membership_by_point.setdefault(point, set()).add(subsystem_id)
            arities = subsystem.get("point_arity_counts")
            if not isinstance(arities, Mapping):
                raise TypeError("subsystem point_arity_counts must be an object")
            full_arity = int(arities.get(system_type_label(len(retained)), 0) or 0) > 0
            search_eligible = subsystem.get("search_eligible")
            if not isinstance(search_eligible, bool):
                raise TypeError("subsystem search_eligible must be boolean")
            expected_eligible = len(retained) == 1 or full_arity
            if search_eligible != expected_eligible:
                raise ValueError("subsystem search eligibility disagrees with point arity evidence")
            expected_path = (
                "unary_endpoint"
                if len(retained) == 1
                else "binary_face" if search_eligible else "endpoint_only_binary_face"
            )
            if subsystem.get("path_class") != expected_path:
                raise ValueError("subsystem path_class is inconsistent")
            if subsystem.get("evidence_quality") != "exact_reported_zero":
                raise ValueError("subsystem evidence_quality must be exact_reported_zero")
            if search_eligible:
                eligible += 1

            scope = subsystem.get("scope")
            support = subsystem.get("property_support")
            if not isinstance(scope, Mapping) or not isinstance(support, list):
                raise TypeError("subsystem scope and property_support are required")
            scope_phase = scope.get("phase_num_id")
            for item in support:
                if not isinstance(item, Mapping) or item.get("BLKprop_id") not in prop_by_id:
                    raise ValueError("subsystem property support references an unknown property")
                prop = prop_by_id[item["BLKprop_id"]]
                for field in ("prop_num_id", "prop_ID", "component_org_num"):
                    if item.get(field) != prop.get(field):
                        raise ValueError(f"subsystem property support disagrees on {field}")
                expected_role = (
                    "limiting_probe"
                    if prop.get("component_org_num") in excluded
                    else "bulk_property"
                )
                if item.get("role") != expected_role:
                    raise ValueError("subsystem property support role is inconsistent")
                prop_phase = (prop.get("property_phase") or {}).get("phase_num_id")
                compatible = scope_phase is None or prop_phase is None or scope_phase == prop_phase
                if item.get("phase_compatible") is not compatible:
                    raise ValueError("subsystem property phase compatibility is inconsistent")
            evidence = subsystem.get("evidence_sources")
            if not isinstance(evidence, list) or any(
                item not in variable_ids | constraint_ids for item in evidence
            ):
                raise ValueError("subsystem evidence_sources reference unknown declarations")

        actual_ids = [entry.get("BLKsubsys_id") for entry in entries]
        if actual_ids != expected_ids:
            raise ValueError(f"{label}/{block_id}: subsystem IDs must be sequential")
        if block.get("block_type") == "ReactionData" and entries:
            raise ValueError("ReactionData blocks cannot have composition subsystems")
        effective = data_summary.get("effective_system_summary")
        if not isinstance(effective, Mapping):
            raise ValueError(f"{label}/{block_id}: effective_system_summary is missing")
        if (
            effective.get("n_subsystems") != len(entries)
            or effective.get("n_search_eligible") != eligible
            or effective.get("n_unique_points") != len(membership_by_point)
            or effective.get("system_types") != sorted(
                {entry["effective_system_type"] for entry in entries}
            )
        ):
            raise ValueError("effective_system_summary disagrees with subsystem manifests")

        for point in block.get("data_points", []):
            if not isinstance(point, Mapping):
                raise TypeError("PCS data_points entries must be objects")
            point_id = point.get("BLKpoint_id")
            require_block_local_id("point", point_id)
            point_ordinal = int(str(point_id).rsplit("_", 1)[1])
            refs = point.get("BLKsubsys_refs")
            if not isinstance(refs, list) or refs != sorted(membership_by_point.get(point_ordinal, set()), key=lambda value: int(value.rsplit("_", 1)[1])):
                raise ValueError("stored PCS point has inconsistent BLKsubsys_refs")
        total += len(entries)
    return total


def validate_card_identity_indexes(
    card: Mapping[str, object],
    *,
    translations: GlobalIdentityTranslations | None = None,
    doi: str | None = None,
) -> tuple[int, int, int]:
    """Validate every embedded block index and return aggregate entry counts."""
    if not isinstance(card, Mapping):
        raise TypeError("PCS card must be an object")
    if translations is None:
        translations = get_global_identity_translations()
    blocks = card["blocks"]
    blocks_summary = card["blocks_summary"]
    if not isinstance(blocks, list):
        raise TypeError("PCS card blocks must be a list")
    if not isinstance(blocks_summary, Mapping):
        raise TypeError("PCS card blocks_summary must be an object")
    expected_blocks = blocks_summary["n_blocks"]
    if (
        isinstance(expected_blocks, bool)
        or not isinstance(expected_blocks, int)
        or expected_blocks < 0
    ):
        raise ValueError(
            "PCS card blocks_summary.n_blocks must be a nonnegative integer"
        )
    label = doi or "<card>"
    if expected_blocks != len(blocks):
        raise ValueError(
            f"{label}: blocks_summary.n_blocks={expected_blocks} "
            f"but the card contains {len(blocks)} blocks"
        )

    derived_indexes = blocks_summary.get("derived_indexes")
    if not isinstance(derived_indexes, Mapping):
        raise ValueError(
            f"{label}: blocks_summary.derived_indexes is missing"
        )
    block_indexes = derived_indexes.get("block_search_adv")
    if not isinstance(block_indexes, Mapping):
        raise ValueError(
            f"{label}: "
            "blocks_summary.derived_indexes.block_search_adv is missing"
        )

    for block in blocks:
        if not isinstance(block, Mapping):
            raise TypeError(f"{label}: every PCS block must be an object")
    block_numbers = [block["block_number"] for block in blocks]
    if len(set(block_numbers)) != len(block_numbers):
        raise ValueError(f"{label}: duplicate block_number in blocks")
    if set(block_indexes) != set(block_numbers):
        raise ValueError(
            f"{label}: embedded block-search keys do not match "
            "the existing card blocks"
        )

    subsystem_entries = validate_card_composition_subsystems(card, doi=doi)

    statistics_entries = 0
    permutation_entries = 0
    for block in blocks:
        block_number = block["block_number"]
        identity_index = block_indexes[block_number]
        validate_block_identity_index(
            identity_index,
            translations=translations,
            block=block,
        )
        statistics_entries += int(identity_index["n_occurrences"])
        permutation_entries += int(identity_index["n_key_permutations"])

    return len(blocks), statistics_entries, permutation_entries, subsystem_entries
