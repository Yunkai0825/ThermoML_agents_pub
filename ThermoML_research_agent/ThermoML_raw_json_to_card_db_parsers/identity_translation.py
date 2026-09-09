"""Exact global property/variable/constraint identity translations.

The three ThermoML catalogs describe source roles, not three independent
physical-quantity vocabularies.  This module builds and loads a conservative
cross-role translation table by joining only on the exact canonical identity
template (for example ``temperature_k`` or
``mole_fraction_{DOIcomp_id}``).

No fuzzy, unit-only, or quantity-family matching is permitted here.  Such
relationships are useful for discovery, but they are not safe executable
translations.
"""

from __future__ import annotations

import csv
import hashlib
import os
import tempfile
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Final, Iterable

from ThermoML_raw_json_to_card_db_parsers.id_schema import require_global_id


PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[1]
SOURCE_CATALOG_DIR: Final[Path] = (
    PROJECT_ROOT
    / "ThermoML_raw_json_to_card_db_parsers"
    / "_index_builder"
    / "id_name_lists"
)
CANONICAL_CATALOG_DIR: Final[Path] = (
    PROJECT_ROOT / "card_databases_storage" / "Canonicalized_ID_name_lists_csvs"
)
TRANSLATION_CSV: Final[Path] = (
    CANONICAL_CATALOG_DIR / "prop_var_constr_translations.csv"
)

ROLE_ORDER: Final[tuple[str, ...]] = ("property", "variable", "constraint")
ROLE_SPECS: Final[dict[str, dict[str, str]]] = {
    "property": {
        "filename": "property_ids.csv",
        "num_id": "prop_num_id",
        "template": "prop_id",
        "name": "prop_name",
        "taxonomy": "prop_group",
    },
    "variable": {
        "filename": "variable_ids.csv",
        "num_id": "var_num_id",
        "template": "var_id",
        "name": "var_name",
        "taxonomy": "var_type_key",
    },
    "constraint": {
        "filename": "constraint_ids.csv",
        "num_id": "constr_num_id",
        "template": "constr_id",
        "name": "constr_name",
        "taxonomy": "constr_type_key",
    },
}

TRANSLATION_FIELDS: Final[tuple[str, ...]] = (
    "quantity_key",
    "preferred_name",
    "component_linked",
    "available_roles",
    "role_count",
    "translation_status",
    "equivalence_basis",
    "prop_num_id",
    "prop_name",
    "prop_group",
    "var_num_id",
    "var_name",
    "var_type_key",
    "constr_num_id",
    "constr_name",
    "constr_type_key",
)


def _role_prefix(role: str) -> str:
    return {
        "property": "prop",
        "variable": "var",
        "constraint": "constr",
    }[role]


def _parse_binary_flag(raw: object, *, field: str, context: str) -> bool:
    text = str(raw)
    if text != text.strip():
        raise ValueError(
            f"{context}: {field} has leading or trailing whitespace"
        )
    if text not in {"0", "1"}:
        raise ValueError(f"{context}: {field} must be 0 or 1, got {raw!r}")
    return text == "1"


def _parse_nonnegative_int(raw: object, *, field: str, context: str) -> int:
    text = str(raw)
    if text != text.strip():
        raise ValueError(
            f"{context}: {field} has leading or trailing whitespace"
        )
    try:
        value = int(text)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{context}: {field} must be an integer") from exc
    if value < 0:
        raise ValueError(f"{context}: {field} must be nonnegative")
    return value


def _require_unpadded(raw: object, *, field: str, context: str) -> str:
    text = str(raw)
    if text != text.strip():
        raise ValueError(
            f"{context}: {field} has leading or trailing whitespace"
        )
    if not text:
        raise ValueError(f"{context}: {field} is empty")
    return text


def _optional_unpadded(raw: object, *, field: str, context: str) -> str | None:
    text = str(raw)
    if text != text.strip():
        raise ValueError(
            f"{context}: {field} has leading or trailing whitespace"
        )
    return text or None


def _validate_quantity_key(
    quantity_key: str,
    *,
    component_linked: bool,
    context: str,
) -> None:
    placeholder = "{DOIcomp_id}"
    count = quantity_key.count(placeholder)
    if component_linked:
        if count != 1 or not quantity_key.endswith(f"_{placeholder}"):
            raise ValueError(
                f"{context}: component-linked quantity_key must contain exactly "
                f"one terminal _{placeholder}"
            )
    elif count:
        raise ValueError(
            f"{context}: non-component quantity_key contains {placeholder}"
        )
    remainder = quantity_key.replace(placeholder, "")
    if "{" in remainder or "}" in remainder:
        raise ValueError(
            f"{context}: quantity_key contains an unsupported placeholder"
        )


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_catalog_sha256s(
    catalog_dir: os.PathLike[str] | str = SOURCE_CATALOG_DIR,
) -> dict[str, str]:
    """Return role-keyed hashes for the exact catalogs used by this build."""
    catalog_path = Path(catalog_dir)
    return {
        role: _file_sha256(catalog_path / ROLE_SPECS[role]["filename"])
        for role in ROLE_ORDER
    }


def verify_catalog_mirror(
    source_dir: os.PathLike[str] | str = SOURCE_CATALOG_DIR,
    mirror_dir: os.PathLike[str] | str = CANONICAL_CATALOG_DIR,
) -> None:
    """Fail if the main-index catalogs and published-card mirrors diverge."""
    source_path = Path(source_dir)
    mirror_path = Path(mirror_dir)
    for role in ROLE_ORDER:
        filename = ROLE_SPECS[role]["filename"]
        source_hash = _file_sha256(source_path / filename)
        mirror_hash = _file_sha256(mirror_path / filename)
        if source_hash != mirror_hash:
            raise ValueError(
                f"Catalog mirror drift for {filename}: "
                f"{source_path / filename} ({source_hash}) != "
                f"{mirror_path / filename} ({mirror_hash})"
            )


@dataclass(frozen=True)
class TranslationRecord:
    """One exact canonical quantity template and its available source roles."""

    quantity_key: str
    preferred_name: str
    component_linked: bool
    prop_num_id: str | None
    var_num_id: str | None
    constr_num_id: str | None
    prop_name: str | None = None
    var_name: str | None = None
    constr_name: str | None = None
    prop_group: str | None = None
    var_type_key: str | None = None
    constr_type_key: str | None = None

    def global_id_for_role(self, role: str) -> str | None:
        if role not in ROLE_ORDER:
            raise ValueError(f"Unknown identity role {role!r}")
        return {
            "property": self.prop_num_id,
            "variable": self.var_num_id,
            "constraint": self.constr_num_id,
        }[role]

    @property
    def available_roles(self) -> tuple[str, ...]:
        return tuple(
            role for role in ROLE_ORDER if self.global_id_for_role(role) is not None
        )

    @property
    def global_ids(self) -> tuple[str, ...]:
        return tuple(
            global_id
            for role in ROLE_ORDER
            if (global_id := self.global_id_for_role(role)) is not None
        )


class GlobalIdentityTranslations:
    """Validated lookup registry for exact cross-role identity translations."""

    def __init__(
        self,
        records: Iterable[TranslationRecord],
        *,
        source_path: Path | None = None,
    ) -> None:
        by_quantity_key: dict[str, TranslationRecord] = {}
        by_global_id: dict[str, TranslationRecord] = {}

        for record in records:
            if not record.quantity_key:
                raise ValueError("Translation record has an empty quantity_key")
            if record.quantity_key in by_quantity_key:
                raise ValueError(
                    f"Duplicate translation quantity_key {record.quantity_key!r}"
                )
            if not record.global_ids:
                raise ValueError(
                    f"Translation record {record.quantity_key!r} has no global IDs"
                )
            by_quantity_key[record.quantity_key] = record

            for role in ROLE_ORDER:
                global_id = record.global_id_for_role(role)
                if global_id is None:
                    continue
                field = ROLE_SPECS[role]["num_id"]
                require_global_id(field, global_id)
                if global_id in by_global_id:
                    other = by_global_id[global_id]
                    raise ValueError(
                        f"Global ID {global_id!r} maps to both "
                        f"{other.quantity_key!r} and {record.quantity_key!r}"
                    )
                by_global_id[global_id] = record

        self._by_quantity_key = by_quantity_key
        self._by_global_id = by_global_id
        self.source_path = source_path

    @classmethod
    def from_csv(cls, path: os.PathLike[str] | str = TRANSLATION_CSV):
        source_path = Path(path)
        with source_path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            actual_fields = tuple(reader.fieldnames or ())
            if actual_fields != TRANSLATION_FIELDS:
                raise ValueError(
                    f"{source_path} has columns {actual_fields!r}, expected "
                    f"{TRANSLATION_FIELDS!r}"
                )

            records: list[TranslationRecord] = []
            for row_number, row in enumerate(reader, start=2):
                context = f"{source_path.name}:{row_number}"
                quantity_key = _require_unpadded(
                    row["quantity_key"],
                    field="quantity_key",
                    context=context,
                )
                role_values = {
                    role: _optional_unpadded(
                        row[ROLE_SPECS[role]["num_id"]],
                        field=ROLE_SPECS[role]["num_id"],
                        context=context,
                    )
                    for role in ROLE_ORDER
                }
                actual_roles = tuple(
                    role for role in ROLE_ORDER if role_values[role] is not None
                )
                available_roles = _require_unpadded(
                    row["available_roles"],
                    field="available_roles",
                    context=context,
                )
                declared_roles = tuple(
                    item for item in available_roles.split("|") if item
                )
                if declared_roles != actual_roles:
                    raise ValueError(
                        f"{context}: available_roles={declared_roles!r} does not "
                        f"match populated IDs {actual_roles!r}"
                    )
                role_count = _parse_nonnegative_int(
                    row["role_count"], field="role_count", context=context
                )
                if role_count != len(actual_roles):
                    raise ValueError(
                        f"{context}: role_count={role_count} but found "
                        f"{len(actual_roles)} populated roles"
                    )
                expected_status = (
                    "cross_role_exact" if role_count > 1 else "single_role"
                )
                translation_status = _require_unpadded(
                    row["translation_status"],
                    field="translation_status",
                    context=context,
                )
                if translation_status != expected_status:
                    raise ValueError(
                        f"{context}: translation_status must be {expected_status!r}"
                    )
                equivalence_basis = _require_unpadded(
                    row["equivalence_basis"],
                    field="equivalence_basis",
                    context=context,
                )
                if equivalence_basis != "exact_canonical_template":
                    raise ValueError(
                        f"{context}: unsupported equivalence_basis "
                        f"{equivalence_basis!r}"
                    )
                component_linked = _parse_binary_flag(
                    row["component_linked"],
                    field="component_linked",
                    context=context,
                )
                _validate_quantity_key(
                    quantity_key,
                    component_linked=component_linked,
                    context=context,
                )
                preferred_name = _require_unpadded(
                    row["preferred_name"],
                    field="preferred_name",
                    context=context,
                )
                role_names: dict[str, str | None] = {}
                role_taxonomies: dict[str, str | None] = {}
                for role in ROLE_ORDER:
                    name_field = ROLE_SPECS[role]["name"]
                    taxonomy_field = ROLE_SPECS[role]["taxonomy"]
                    role_names[role] = _optional_unpadded(
                        row[name_field],
                        field=name_field,
                        context=context,
                    )
                    role_taxonomies[role] = _optional_unpadded(
                        row[taxonomy_field],
                        field=taxonomy_field,
                        context=context,
                    )
                    populated = role_values[role] is not None
                    if populated != (role_names[role] is not None):
                        raise ValueError(
                            f"{context}: {name_field} population must match "
                            f"{ROLE_SPECS[role]['num_id']}"
                        )
                    if populated != (role_taxonomies[role] is not None):
                        raise ValueError(
                            f"{context}: {taxonomy_field} population must match "
                            f"{ROLE_SPECS[role]['num_id']}"
                        )
                    if populated and role_names[role] != preferred_name:
                        raise ValueError(
                            f"{context}: {name_field} disagrees with preferred_name"
                        )
                if (
                    role_taxonomies["variable"] is not None
                    and role_taxonomies["constraint"] is not None
                    and role_taxonomies["variable"]
                    != role_taxonomies["constraint"]
                ):
                    raise ValueError(
                        f"{context}: variable and constraint taxonomies disagree"
                    )

                records.append(
                    TranslationRecord(
                        quantity_key=quantity_key,
                        preferred_name=preferred_name,
                        component_linked=component_linked,
                        prop_num_id=role_values["property"],
                        var_num_id=role_values["variable"],
                        constr_num_id=role_values["constraint"],
                        prop_name=role_names["property"],
                        var_name=role_names["variable"],
                        constr_name=role_names["constraint"],
                        prop_group=role_taxonomies["property"],
                        var_type_key=role_taxonomies["variable"],
                        constr_type_key=role_taxonomies["constraint"],
                    )
                )
        return cls(records, source_path=source_path)

    def record_for_global_id(self, global_id: str) -> TranslationRecord:
        try:
            return self._by_global_id[global_id]
        except KeyError as exc:
            raise KeyError(
                f"Global property/variable/constraint ID {global_id!r} is absent "
                "from the exact translation registry"
            ) from exc

    def record_for_quantity_key(self, quantity_key: str) -> TranslationRecord:
        try:
            return self._by_quantity_key[quantity_key]
        except KeyError as exc:
            raise KeyError(
                f"Unknown canonical quantity_key {quantity_key!r}"
            ) from exc

    def translate(self, global_id: str) -> tuple[str, ...]:
        """Return all exact role-specific global IDs for ``global_id``."""
        return self.record_for_global_id(global_id).global_ids

    @property
    def records(self) -> tuple[TranslationRecord, ...]:
        return tuple(
            self._by_quantity_key[key] for key in sorted(self._by_quantity_key)
        )

    @property
    def n_global_ids(self) -> int:
        return len(self._by_global_id)


def _read_role_catalog(catalog_dir: Path, role: str) -> list[dict[str, object]]:
    spec = ROLE_SPECS[role]
    path = catalog_dir / spec["filename"]
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        expected = (
            spec["num_id"],
            spec["template"],
            spec["name"],
            spec["taxonomy"],
            "comp_id_linked",
            "n_blocks",
        )
        actual = tuple(reader.fieldnames or ())
        if actual != expected:
            raise ValueError(
                f"{path} has columns {actual!r}, expected {expected!r}"
            )

        rows: list[dict[str, object]] = []
        seen_keys: set[str] = set()
        seen_global_ids: set[str] = set()
        for row_number, row in enumerate(reader, start=2):
            context = f"{path.name}:{row_number}"
            quantity_key = _require_unpadded(
                row[spec["template"]],
                field=spec["template"],
                context=context,
            )
            global_id = _require_unpadded(
                row[spec["num_id"]],
                field=spec["num_id"],
                context=context,
            )
            component_linked = _parse_binary_flag(
                row["comp_id_linked"],
                field="comp_id_linked",
                context=context,
            )
            _validate_quantity_key(
                quantity_key,
                component_linked=component_linked,
                context=context,
            )
            _parse_nonnegative_int(
                row["n_blocks"],
                field="n_blocks",
                context=context,
            )
            if quantity_key in seen_keys:
                raise ValueError(
                    f"{context}: duplicate {role} quantity_key {quantity_key!r}"
                )
            if global_id in seen_global_ids:
                raise ValueError(f"{context}: duplicate global ID {global_id!r}")
            require_global_id(spec["num_id"], global_id)
            seen_keys.add(quantity_key)
            seen_global_ids.add(global_id)
            rows.append(
                {
                    "quantity_key": quantity_key,
                    "global_id": global_id,
                    "name": _require_unpadded(
                        row[spec["name"]],
                        field=spec["name"],
                        context=context,
                    ),
                    "taxonomy": _require_unpadded(
                        row[spec["taxonomy"]],
                        field=spec["taxonomy"],
                        context=context,
                    ),
                    "component_linked": component_linked,
                }
            )
    return rows


def build_translation_rows(
    catalog_dir: os.PathLike[str] | str = SOURCE_CATALOG_DIR,
) -> list[dict[str, object]]:
    """Join the three role catalogs on exact canonical identity templates."""
    catalog_path = Path(catalog_dir)
    grouped: dict[str, dict[str, object]] = {}

    for role in ROLE_ORDER:
        prefix = _role_prefix(role)
        for source in _read_role_catalog(catalog_path, role):
            quantity_key = str(source["quantity_key"])
            entry = grouped.setdefault(
                quantity_key,
                {
                    "quantity_key": quantity_key,
                    "component_linked": source["component_linked"],
                },
            )
            if entry["component_linked"] != source["component_linked"]:
                raise ValueError(
                    f"Canonical quantity {quantity_key!r} disagrees on "
                    "component_linked across source roles"
                )
            entry[f"{prefix}_num_id"] = source["global_id"]
            entry[f"{prefix}_name"] = source["name"]
            entry[ROLE_SPECS[role]["taxonomy"]] = source["taxonomy"]

    rows: list[dict[str, object]] = []
    for quantity_key in sorted(grouped):
        grouped_row = grouped[quantity_key]
        roles = tuple(
            role
            for role in ROLE_ORDER
            if grouped_row.get(f"{_role_prefix(role)}_num_id")
        )
        names = [
            str(grouped_row.get(f"{_role_prefix(role)}_name") or "")
            for role in ROLE_ORDER
        ]
        populated_names = {name for name in names if name}
        if len(populated_names) != 1:
            raise ValueError(
                f"Canonical quantity {quantity_key!r} disagrees on display "
                f"name across roles: {sorted(populated_names)!r}"
            )
        var_type_key = grouped_row.get("var_type_key")
        constr_type_key = grouped_row.get("constr_type_key")
        if (
            var_type_key
            and constr_type_key
            and var_type_key != constr_type_key
        ):
            raise ValueError(
                f"Canonical quantity {quantity_key!r} disagrees on variable/"
                f"constraint taxonomy: {var_type_key!r} != {constr_type_key!r}"
            )
        preferred_name = next(name for name in names if name)
        row: dict[str, object] = {
            "quantity_key": quantity_key,
            "preferred_name": preferred_name,
            "component_linked": int(bool(grouped_row["component_linked"])),
            "available_roles": "|".join(roles),
            "role_count": len(roles),
            "translation_status": (
                "cross_role_exact" if len(roles) > 1 else "single_role"
            ),
            "equivalence_basis": "exact_canonical_template",
        }
        for role in ROLE_ORDER:
            prefix = _role_prefix(role)
            row[f"{prefix}_num_id"] = grouped_row.get(f"{prefix}_num_id", "")
            row[f"{prefix}_name"] = grouped_row.get(f"{prefix}_name", "")
            taxonomy_field = ROLE_SPECS[role]["taxonomy"]
            row[taxonomy_field] = grouped_row.get(taxonomy_field, "")
        rows.append(row)
    return rows


def write_translation_csv(
    output_path: os.PathLike[str] | str = TRANSLATION_CSV,
    *,
    catalog_dir: os.PathLike[str] | str = SOURCE_CATALOG_DIR,
) -> list[dict[str, object]]:
    """Build and atomically publish the exact translation CSV."""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    if Path(catalog_dir).resolve() == SOURCE_CATALOG_DIR.resolve():
        verify_catalog_mirror()
    rows = build_translation_rows(catalog_dir)
    staging_handle = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="",
        dir=output.parent,
        prefix=f".{output.name}.",
        suffix=".building",
        delete=False,
    )
    staging = Path(staging_handle.name)
    try:
        with staging_handle as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=list(TRANSLATION_FIELDS),
                lineterminator="\n",
            )
            writer.writeheader()
            writer.writerows(rows)
        GlobalIdentityTranslations.from_csv(staging)
        os.replace(staging, output)
        _cached_translations.cache_clear()
    finally:
        if staging.exists():
            staging.unlink()

    return rows


def translation_csv_sha256(
    path: os.PathLike[str] | str = TRANSLATION_CSV,
) -> str:
    return _file_sha256(Path(path))


@lru_cache(maxsize=4)
def _cached_translations(path_text: str) -> GlobalIdentityTranslations:
    return GlobalIdentityTranslations.from_csv(Path(path_text))


def get_global_identity_translations(
    path: os.PathLike[str] | str = TRANSLATION_CSV,
) -> GlobalIdentityTranslations:
    return _cached_translations(str(Path(path).resolve()))


if __name__ == "__main__":
    generated = write_translation_csv()
    cross_role = sum(1 for row in generated if row["role_count"] > 1)
    print(
        f"Published {TRANSLATION_CSV}: {len(generated)} quantity keys, "
        f"{cross_role} exact cross-role translations"
    )
