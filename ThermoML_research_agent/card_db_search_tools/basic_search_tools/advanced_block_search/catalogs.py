"""Exact runtime catalogs and DB-generation coherence checks."""

from __future__ import annotations

import csv
import hashlib
import os
import re
import sqlite3
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.parse import quote

from normalization_helpers.db_helpers import open_db
from normalization_helpers.paths import card_db_path

from .errors import fail, require_object, require_string
from .semantics import QuantitySemantics, semantics_for_quantity


_WORKSPACE = Path(
    os.environ.get(
        "THERMOML_QUERY_AGENT_ROOT",
        str(Path(__file__).resolve().parents[3]),
    )
).resolve()
_CSV_DIR = (
    _WORKSPACE
    / "card_databases_storage"
    / "Canonicalized_ID_name_lists_csvs"
)
PCS_DB = Path(card_db_path("PCS_INDIV"))
RAW_DB = _WORKSPACE / "ThermoML.v2020-09-30.db" / "thermoml_raw.db"
PM_REGISTRY_DB = (
    _WORKSPACE / "card_databases_storage" / "PureOrMixtureData_registry.db"
)
RXN_REGISTRY_DB = (
    _WORKSPACE / "card_databases_storage" / "ReactionData_registry.db"
)

_GLOBAL_QUANTITY_RE = re.compile(r"^GLOB(prop|var|constr)_[1-9][0-9]*$")
_GLOBAL_COMPOUND_RE = re.compile(r"^GLOBcomp_[1-9][0-9]*$")
_GLOBAL_PHASE_RE = re.compile(r"^GLOBphase_[1-9][0-9]*$")
_GLOBAL_LITERATURE_RE = re.compile(r"^GLOBlit_[1-9][0-9]*$")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_csv(path: Path) -> list[dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                fail(
                    "CATALOG_INCOHERENT",
                    f"Catalog {path.name!r} has no header.",
                    "/",
                )
            return [dict(row) for row in reader]
    except OSError as exc:
        fail(
            "CATALOG_INCOHERENT",
            f"Could not read catalog {path}.",
            "/",
            details={"error": str(exc)},
        )


@dataclass(frozen=True)
class TranslationRow:
    quantity_key: str
    preferred_name: str
    component_linked: bool
    prop_num_id: str | None
    var_num_id: str | None
    constr_num_id: str | None
    semantics: QuantitySemantics

    @property
    def available_global_ids(self) -> tuple[str, ...]:
        return tuple(
            value
            for value in (
                self.prop_num_id,
                self.var_num_id,
                self.constr_num_id,
            )
            if value is not None
        )

    def global_id_for_role(self, role: str) -> str | None:
        return {
            "property": self.prop_num_id,
            "variable": self.var_num_id,
            "constraint": self.constr_num_id,
        }.get(role)


@dataclass(frozen=True)
class QuantityResolution:
    input_value: str
    input_catalog_role: str | None
    row: TranslationRow

    def as_result(self) -> dict[str, Any]:
        return {
            "input": self.input_value,
            "input_catalog_role": self.input_catalog_role,
            "quantity_key": self.row.quantity_key,
            "available_global_ids": list(self.row.available_global_ids),
        }


class TranslationCatalog:
    def __init__(self, rows: list[TranslationRow]) -> None:
        self.by_key: dict[str, TranslationRow] = {}
        self.by_global_id: dict[str, TranslationRow] = {}
        for row in rows:
            if row.quantity_key in self.by_key:
                fail(
                    "CATALOG_INCOHERENT",
                    f"Duplicate quantity key {row.quantity_key!r}.",
                    "/",
                )
            self.by_key[row.quantity_key] = row
            for global_id in row.available_global_ids:
                if global_id in self.by_global_id:
                    fail(
                        "CATALOG_INCOHERENT",
                        f"Duplicate global quantity ID {global_id!r}.",
                        "/",
                    )
                self.by_global_id[global_id] = row

    def resolve(
        self,
        quantity: Any,
        pointer: str,
    ) -> QuantityResolution:
        obj = require_object(quantity, pointer)
        if set(obj) == {"global_id"}:
            value = require_string(obj["global_id"], f"{pointer}/global_id")
            if not _GLOBAL_QUANTITY_RE.fullmatch(value):
                fail(
                    "UNKNOWN_QUANTITY",
                    "Expected GLOBprop_N, GLOBvar_N, or GLOBconstr_N.",
                    f"{pointer}/global_id",
                    details={"received": value},
                )
            row = self.by_global_id.get(value)
            if row is None:
                fail(
                    "UNKNOWN_QUANTITY",
                    f"Unknown global quantity ID {value!r}.",
                    f"{pointer}/global_id",
                )
            role = {
                "prop": "property",
                "var": "variable",
                "constr": "constraint",
            }[_GLOBAL_QUANTITY_RE.fullmatch(value).group(1)]  # type: ignore[union-attr]
            return QuantityResolution(value, role, row)
        if set(obj) == {"key"}:
            value = require_string(obj["key"], f"{pointer}/key")
            row = self.by_key.get(value)
            if row is None:
                fail(
                    "UNKNOWN_QUANTITY",
                    f"Unknown exact quantity key {value!r}.",
                    f"{pointer}/key",
                )
            return QuantityResolution(value, None, row)
        fail(
            "INVALID_REQUEST",
            "quantity requires exactly one of global_id or key.",
            pointer,
        )


@dataclass(frozen=True)
class CompoundRecord:
    comp_num_id: str
    comp_id: str
    inchi_key: str
    common_name: str
    formula: str
    smiles: str
    standard_inchi: str

    def as_dict(self) -> dict[str, str]:
        return {
            "comp_num_id": self.comp_num_id,
            "comp_id": self.comp_id,
            "inchi_key": self.inchi_key,
            "common_name": self.common_name,
            "formula": self.formula,
            "smiles": self.smiles,
            "standard_inchi": self.standard_inchi,
        }


@dataclass(frozen=True)
class PhaseRecord:
    phase_num_id: str
    phase_id: str
    phase_name: str


@dataclass(frozen=True)
class ReferenceRecord:
    lit_num_id: str
    doi: str
    lit_id: str
    first_author: str
    year: int
    journal: str


@dataclass(frozen=True)
class RuntimeCatalogs:
    translation: TranslationCatalog
    compounds: tuple[CompoundRecord, ...]
    phases_by_id: dict[str, PhaseRecord]
    phases_by_name: dict[str, PhaseRecord]
    references_by_doi: dict[str, ReferenceRecord]
    references_by_id: dict[str, ReferenceRecord]
    identity_index_schema: str
    translation_filename: str
    translation_sha256: str
    pcs_build_time: str | None

    def resolve_compound(
        self,
        identity: Any,
        pointer: str,
    ) -> CompoundRecord:
        obj = require_object(identity, pointer)
        allowed = {
            "comp_num_id",
            "global_id",
            "comp_id",
            "inchi_key",
            "standard_inchi",
            "smiles",
            "name",
        }
        if len(obj) != 1 or not set(obj) <= allowed:
            fail(
                "INVALID_REQUEST",
                "Compound identity requires exactly one exact identity field.",
                pointer,
                details={"allowed": sorted(allowed)},
            )
        field, raw_value = next(iter(obj.items()))
        value = require_string(raw_value, f"{pointer}/{field}")
        if field == "global_id":
            field = "comp_num_id"
        if field == "comp_num_id" and not _GLOBAL_COMPOUND_RE.fullmatch(value):
            fail(
                "UNKNOWN_COMPOUND",
                "Expected a typed GLOBcomp_N identifier.",
                f"{pointer}/{field}",
            )

        matches: list[CompoundRecord] = []
        for row in self.compounds:
            candidate = (
                row.common_name
                if field == "name"
                else getattr(row, field)
            )
            if field in {"name", "comp_id"}:
                if candidate.casefold() == value.casefold():
                    matches.append(row)
            elif candidate == value:
                matches.append(row)
        if not matches:
            fail(
                "UNKNOWN_COMPOUND",
                f"No exact compound match for {value!r}.",
                pointer,
            )
        unique = {row.comp_num_id: row for row in matches}
        if len(unique) != 1:
            fail(
                "AMBIGUOUS_ALIAS",
                f"Compound identity {value!r} is not unique.",
                pointer,
                details={"candidate_ids": sorted(unique)},
            )
        return next(iter(unique.values()))

    def require_phase(self, phase_num_id: Any, pointer: str) -> PhaseRecord:
        value = require_string(phase_num_id, pointer)
        if not _GLOBAL_PHASE_RE.fullmatch(value):
            fail(
                "UNKNOWN_PHASE",
                "Expected a typed GLOBphase_N identifier.",
                pointer,
            )
        row = self.phases_by_id.get(value)
        if row is None:
            fail("UNKNOWN_PHASE", f"Unknown phase ID {value!r}.", pointer)
        return row

    def require_literature_id(
        self,
        lit_num_id: Any,
        pointer: str,
    ) -> ReferenceRecord:
        value = require_string(lit_num_id, pointer)
        if not _GLOBAL_LITERATURE_RE.fullmatch(value):
            fail(
                "UNKNOWN_LITERATURE",
                "Expected a typed GLOBlit_N identifier.",
                pointer,
            )
        row = self.references_by_id.get(value)
        if row is None:
            fail(
                "UNKNOWN_LITERATURE",
                f"Unknown literature ID {value!r}.",
                pointer,
            )
        return row


def _load_translation_rows(path: Path) -> list[TranslationRow]:
    raw_rows = _read_csv(path)
    required = {
        "quantity_key",
        "preferred_name",
        "component_linked",
        "prop_num_id",
        "var_num_id",
        "constr_num_id",
    }
    rows: list[TranslationRow] = []
    for index, raw in enumerate(raw_rows):
        missing = sorted(required - set(raw))
        if missing:
            fail(
                "CATALOG_INCOHERENT",
                "Translation CSV has an incomplete schema.",
                "/",
                details={"row": index, "missing": missing},
            )
        key = raw["quantity_key"]
        semantics = semantics_for_quantity(key)
        if semantics.canonical_unit is None:
            fail(
                "QUANTITY_SEMANTICS_UNAVAILABLE",
                f"No curated semantics for {key!r}.",
                "/",
            )
        component_text = raw["component_linked"]
        if component_text not in {"0", "1"}:
            fail(
                "CATALOG_INCOHERENT",
                "component_linked must be 0 or 1.",
                "/",
                details={"row": index, "value": component_text},
            )
        rows.append(
            TranslationRow(
                quantity_key=key,
                preferred_name=raw["preferred_name"],
                component_linked=component_text == "1",
                prop_num_id=raw["prop_num_id"] or None,
                var_num_id=raw["var_num_id"] or None,
                constr_num_id=raw["constr_num_id"] or None,
                semantics=semantics,
            )
        )
    return rows


def _load_compounds() -> tuple[CompoundRecord, ...]:
    rows: list[CompoundRecord] = []
    for raw in _read_csv(_CSV_DIR / "compound_ids.csv"):
        rows.append(
            CompoundRecord(
                comp_num_id=raw["comp_num_id"],
                comp_id=raw["comp_id"],
                inchi_key=raw["inchi_key"],
                common_name=raw["common_name"],
                formula=raw["formula"],
                smiles=raw["smiles"],
                standard_inchi=raw["standard_inchi"],
            )
        )
    return tuple(rows)


def _load_phases() -> tuple[dict[str, PhaseRecord], dict[str, PhaseRecord]]:
    by_id: dict[str, PhaseRecord] = {}
    by_name: dict[str, PhaseRecord] = {}
    for raw in _read_csv(_CSV_DIR / "phase_ids.csv"):
        row = PhaseRecord(
            phase_num_id=raw["phase_num_id"],
            phase_id=raw["phase_id"],
            phase_name=raw["phase_name"],
        )
        by_id[row.phase_num_id] = row
        by_name[row.phase_name.casefold()] = row
    return by_id, by_name


def _load_references(
) -> tuple[dict[str, ReferenceRecord], dict[str, ReferenceRecord]]:
    by_doi: dict[str, ReferenceRecord] = {}
    by_id: dict[str, ReferenceRecord] = {}
    for raw in _read_csv(_CSV_DIR / "reference_ids.csv"):
        try:
            year = int(raw["year"])
        except (TypeError, ValueError):
            year = 0
        row = ReferenceRecord(
            lit_num_id=raw["lit_num_id"],
            doi=raw["doi"],
            lit_id=raw["lit_id"],
            first_author=raw["first_author"],
            year=year,
            journal=raw["journal"],
        )
        by_doi[row.doi] = row
        by_id[row.lit_num_id] = row
    return by_doi, by_id


@lru_cache(maxsize=8)
def _load_runtime_catalogs_cached(
    translation_filename: str,
    expected_sha256: str,
    identity_index_schema: str,
    pcs_build_time: str | None,
) -> RuntimeCatalogs:
    if os.path.basename(translation_filename) != translation_filename:
        fail(
            "CATALOG_INCOHERENT",
            "PCS metadata contains an unsafe translation filename.",
            "/",
        )
    translation_path = _CSV_DIR / translation_filename
    actual_sha256 = _sha256(translation_path)
    if actual_sha256 != expected_sha256:
        fail(
            "CATALOG_INCOHERENT",
            "PCS database and identity translation CSV are incoherent.",
            "/",
            details={
                "expected_sha256": expected_sha256,
                "actual_sha256": actual_sha256,
                "filename": translation_filename,
            },
        )
    phases_by_id, phases_by_name = _load_phases()
    references_by_doi, references_by_id = _load_references()
    return RuntimeCatalogs(
        translation=TranslationCatalog(
            _load_translation_rows(translation_path)
        ),
        compounds=_load_compounds(),
        phases_by_id=phases_by_id,
        phases_by_name=phases_by_name,
        references_by_doi=references_by_doi,
        references_by_id=references_by_id,
        identity_index_schema=identity_index_schema,
        translation_filename=translation_filename,
        translation_sha256=expected_sha256,
        pcs_build_time=pcs_build_time,
    )


def load_runtime_catalogs() -> RuntimeCatalogs:
    if not PCS_DB.is_file():
        fail(
            "DATABASE_UNAVAILABLE",
            f"PCS_INDIV.db is unavailable at {PCS_DB}.",
            "/",
        )
    connection = open_db(str(PCS_DB))
    try:
        metadata = dict(
            connection.execute(
                "SELECT key, value FROM metadata WHERE key IN ("
                "'identity_translation_csv',"
                "'identity_translation_sha256',"
                "'identity_index_schema',"
                "'build_time_s'"
                ")"
            )
        )
    finally:
        connection.close()
    required = (
        "identity_translation_csv",
        "identity_translation_sha256",
        "identity_index_schema",
    )
    missing = [field for field in required if not metadata.get(field)]
    if missing:
        fail(
            "CATALOG_INCOHERENT",
            "PCS metadata is missing advanced-search identity metadata.",
            "/",
            details={"missing": missing},
        )
    if metadata["identity_index_schema"] != "pcs-block-identity-index-v2":
        fail(
            "CATALOG_INCOHERENT",
            "Unsupported embedded identity-index schema.",
            "/",
            details={"received": metadata["identity_index_schema"]},
        )
    return _load_runtime_catalogs_cached(
        metadata["identity_translation_csv"],
        metadata["identity_translation_sha256"],
        metadata["identity_index_schema"],
        metadata.get("build_time_s"),
    )


def open_raw_db() -> sqlite3.Connection:
    if not RAW_DB.is_file():
        fail(
            "DATABASE_UNAVAILABLE",
            f"Raw ThermoML database is unavailable at {RAW_DB}.",
            "/",
        )
    absolute = str(RAW_DB.resolve()).replace("\\", "/")
    # This Windows SQLite build rejects a remote host in URI authority form.
    # A resolved UNC path therefore needs the four-slash local-path spelling
    # (``file:////server/share/...``); mapped drive paths use ``file:N:/...``.
    uri = (
        f"file://{quote(absolute, safe='/:')}?mode=ro"
        if absolute.startswith("//")
        else f"file:{quote(absolute, safe='/:')}?mode=ro"
    )
    connection = sqlite3.connect(
        uri,
        uri=True,
    )
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA query_only=ON")
    return connection
