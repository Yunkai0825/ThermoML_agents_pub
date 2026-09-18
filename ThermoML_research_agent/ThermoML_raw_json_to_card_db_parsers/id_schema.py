"""Strict identifier grammar for generated ThermoML cards and databases.

Raw ThermoML ordinal fields (``nPropNumber``, ``nOrgNum``, and similar) are
source data.  They must pass through the constructors in this module before
they are written to a generated CSV, card, registry, or database.

There is deliberately no legacy ``comp_1`` / ``block_1`` compatibility here.
Consumers must use the same grammar as producers and reject unscoped IDs.
"""

from __future__ import annotations

import csv
import re
from functools import lru_cache
from pathlib import Path
from typing import Final


GLOBAL_PREFIX_BY_FIELD: Final[dict[str, str]] = {
    "lit_num_id": "GLOBlit_",
    "comp_num_id": "GLOBcomp_",
    "prop_num_id": "GLOBprop_",
    "var_num_id": "GLOBvar_",
    "constr_num_id": "GLOBconstr_",
    "meas_num_id": "GLOBmeas_",
    "phase_num_id": "GLOBphase_",
    "blocktype_num_id": "GLOBblocktype_",
    "rxn_type_num_id": "GLOBrxntype_",
    "solvent_num_id": "GLOBsolvent_",
}

_POSITIVE_ORDINAL_RE: Final[re.Pattern[str]] = re.compile(r"^[1-9]\d*$")
_DOI_COMP_RE: Final[re.Pattern[str]] = re.compile(r"^DOIcomp_([1-9]\d*)$")
_DOI_COMP_SAMPLE_RE: Final[re.Pattern[str]] = re.compile(
    r"^DOIcompSample_([1-9]\d*)_([1-9]\d*)$"
)
_BLOCK_ID_RE: Final[re.Pattern[str]] = re.compile(
    r"^(PROPblock|RXNblock)_([1-9]\d*)$"
)
_BLOCK_LOCAL_RE: Final[re.Pattern[str]] = re.compile(
    r"^BLK(prop|var|constr|point|subsys)_([1-9]\d*)$"
)
_PROPERTY_ASSESSMENT_RE: Final[re.Pattern[str]] = re.compile(
    r"^BLKpropAssessment_([1-9]\d*)_([1-9]\d*)$"
)
_RETIRED_ID_RE: Final[re.Pattern[str]] = re.compile(
    r"^(?:lit|comp|sample|block|prop|var|constr|meas|phase|solvent)_\d+$",
    re.IGNORECASE,
)
_DOI_TEXT_RE: Final[re.Pattern[str]] = re.compile(
    r"10\.\d{4,9}/[^\s<>\[\]\"']+",
    re.IGNORECASE,
)
_REFERENCE_IDS_CSV: Final[Path] = (
    Path(__file__).resolve().parents[1]
    / "card_databases_storage"
    / "Canonicalized_ID_name_lists_csvs"
    / "reference_ids.csv"
)
_MISSING: Final[object] = object()
_DOI_FIELD_ALIASES: Final[tuple[str, ...]] = (
    "doi_resolved",
    "source_doi",
    "pseudo_doi",
)


@lru_cache(maxsize=1)
def _reference_id_maps() -> tuple[dict[str, str], dict[str, str]]:
    """Return validated DOI↔GLOBlit maps from the canonical registry."""
    if not _REFERENCE_IDS_CSV.is_file():
        raise FileNotFoundError(
            f"Canonical reference registry is missing: {_REFERENCE_IDS_CSV}"
        )

    doi_to_lit: dict[str, str] = {}
    lit_to_doi: dict[str, str] = {}
    with _REFERENCE_IDS_CSV.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"doi", "lit_num_id"}
        missing = required - set(reader.fieldnames or ())
        if missing:
            raise ValueError(
                f"reference_ids.csv is missing required fields {sorted(missing)}"
            )
        for row_number, row in enumerate(reader, start=2):
            doi = row["doi"].strip()
            lit_num_id = require_global_id("lit_num_id", row["lit_num_id"])
            if not doi:
                raise ValueError(
                    f"reference_ids.csv row {row_number} has an empty DOI"
                )
            doi_key = doi.casefold()
            previous_lit = doi_to_lit.setdefault(doi_key, lit_num_id)
            if previous_lit != lit_num_id:
                raise ValueError(
                    f"DOI {doi!r} maps to both {previous_lit!r} and "
                    f"{lit_num_id!r}"
                )
            previous_doi = lit_to_doi.setdefault(lit_num_id, doi)
            if previous_doi.casefold() != doi_key:
                raise ValueError(
                    f"{lit_num_id!r} maps to both {previous_doi!r} and {doi!r}"
                )
    return doi_to_lit, lit_to_doi


def lit_num_id_for_doi(doi: object, *, allow_unregistered: bool = False) -> str | None:
    """Resolve one DOI to its canonical ``GLOBlit_N`` identifier.

    ``agentblock/`` values are internal virtual-source identifiers rather
    than literature DOIs, so they deliberately resolve to ``None``.
    """
    if doi is None:
        return None
    if not isinstance(doi, str) or not doi.strip():
        raise TypeError(f"doi must be non-empty text or null, got {doi!r}")
    text = doi.strip()
    if text.startswith("agentblock/"):
        return None
    doi_to_lit, _ = _reference_id_maps()
    lit_num_id = doi_to_lit.get(text.casefold())
    if lit_num_id is None and not allow_unregistered:
        raise ValueError(
            f"DOI {text!r} is not present in the canonical reference registry"
        )
    return lit_num_id


def doi_for_lit_num_id(lit_num_id: object) -> str:
    """Resolve one canonical ``GLOBlit_N`` identifier to its DOI."""
    validated = require_global_id("lit_num_id", lit_num_id)
    _, lit_to_doi = _reference_id_maps()
    try:
        return lit_to_doi[validated]
    except KeyError as exc:
        raise ValueError(
            f"lit_num_id {validated!r} is not present in the canonical "
            "reference registry"
        ) from exc


def attach_lit_num_ids(
    value: object,
    *,
    path: str = "$",
    allow_unregistered: bool = False,
) -> object:
    """Return a copy where every ``doi`` field has a sibling ``lit_num_id``.

    Registered ThermoML DOI values are resolved strictly to ``GLOBlit_N``.
    Existing pairs are cross-checked. Error results may opt into
    ``allow_unregistered`` so an invalid user-supplied DOI is represented as
    ``lit_num_id: null`` instead of obscuring the original tool error.
    """
    if isinstance(value, dict):
        child_allow_unregistered = allow_unregistered or "error" in value
        out = {
            key: attach_lit_num_ids(
                child,
                path=f"{path}.{key}",
                allow_unregistered=child_allow_unregistered,
            )
            for key, child in value.items()
        }
        doi_field = "doi" if "doi" in out else next(
            (field for field in _DOI_FIELD_ALIASES if field in out),
            None,
        )
        if doi_field is not None:
            # Alias fields can echo user input, so an unregistered value
            # remains visible with an explicit null instead of converting a
            # no-results response into a contract failure. Canonical ``doi``
            # fields stay strict except in structured error results.
            pair_allow_unregistered = (
                child_allow_unregistered or doi_field != "doi"
            )
            expected = lit_num_id_for_doi(
                out[doi_field],
                allow_unregistered=pair_allow_unregistered,
            )
            received = out.get("lit_num_id", _MISSING)
            if received is not _MISSING and received is not None:
                validated = require_global_id("lit_num_id", received)
                if expected is None:
                    raise ValueError(
                        f"{path}.lit_num_id={validated!r} accompanies "
                        f"unregistered or virtual DOI {out[doi_field]!r}"
                    )
                if validated != expected:
                    raise ValueError(
                        f"{path} has mismatched literature identity: "
                        f"{doi_field}={out[doi_field]!r} resolves to "
                        f"{expected!r}, not {validated!r}"
                    )
            out["lit_num_id"] = expected
        return out

    if isinstance(value, list):
        return [
            attach_lit_num_ids(
                child,
                path=f"{path}[{index}]",
                allow_unregistered=allow_unregistered,
            )
            for index, child in enumerate(value)
        ]

    return value


def reconcile_literature_identities(
    value: object,
    *,
    path: str = "$",
) -> tuple[object, list[str]]:
    """Deterministically enforce the DOI↔``GLOBlit_N`` coupling contract.

    ``GLOBlit_N`` is the authoritative literature identity; a DOI is coupled
    display metadata. Per structured entry:

    1. A registered ``lit_num_id`` wins — a missing, unregistered, or
       mismatched sibling ``doi`` is repaired from the registry.
    2. Without a usable ``lit_num_id``, a registered ``doi`` stands (strict
       enrichment attaches its identity afterwards).
    3. Entries with neither — an unregistered DOI and no registry identity —
       are dropped from lists or null-coupled in bare dicts: they carry no
       verifiable evidence.

    Structured error results and ``agentblock/`` virtual DOIs are preserved
    untouched. Returns the cleaned copy plus human-readable change records.
    """
    doi_to_lit, lit_to_doi = _reference_id_maps()
    notes: list[str] = []

    def _registered_lit(entry: dict) -> str | None:
        lit = entry.get("lit_num_id")
        if not isinstance(lit, str) or lit not in lit_to_doi:
            return None
        return lit

    def _doi_state(entry: dict) -> tuple[str | None, bool]:
        doi = entry.get("doi")
        if not isinstance(doi, str) or not doi.strip():
            return None, False
        text = doi.strip()
        if text.startswith("agentblock/"):
            return text, True
        return text, text.casefold() in doi_to_lit

    def _reconcile(entry: dict, entry_path: str) -> dict | None:
        """Return the fixed entry, or None when it must be dropped."""
        if "error" in entry:
            return entry
        has_doi_field = "doi" in entry
        has_lit_field = "lit_num_id" in entry
        if not has_doi_field and not has_lit_field:
            return entry
        doi, doi_registered = _doi_state(entry)
        if doi is not None and doi.startswith("agentblock/"):
            return entry
        lit = _registered_lit(entry)
        out = dict(entry)
        if lit is not None:
            registry_doi = lit_to_doi[lit]
            if doi is None or not doi_registered or doi_to_lit.get(doi.casefold()) != lit:
                if doi is not None and doi != registry_doi:
                    notes.append(
                        f"repaired {entry_path}: doi {doi!r} -> {registry_doi!r} "
                        f"(authoritative {lit})"
                    )
                out["doi"] = registry_doi
            return out
        # No authoritative identity: unusable lit values must not survive.
        if has_lit_field and entry.get("lit_num_id") is not None:
            notes.append(
                f"cleared {entry_path}: unregistered lit_num_id "
                f"{entry.get('lit_num_id')!r}"
            )
            out["lit_num_id"] = None
        if doi is None:
            return out
        if doi_registered:
            return out
        notes.append(f"dropped {entry_path}: unregistered doi {doi!r}")
        return None

    def _walk(node: object, node_path: str) -> object:
        if isinstance(node, list):
            kept = []
            for index, child in enumerate(node):
                child_path = f"{node_path}[{index}]"
                if isinstance(child, dict):
                    fixed = _reconcile(child, child_path)
                    if fixed is None:
                        continue
                    kept.append(_walk(fixed, child_path))
                else:
                    kept.append(_walk(child, child_path))
            return kept
        if isinstance(node, dict):
            if "error" in node:
                return node
            out = {
                key: _walk(child, f"{node_path}.{key}")
                for key, child in node.items()
            }
            fixed = _reconcile(out, node_path)
            if fixed is None:
                out["doi"] = None
                out["lit_num_id"] = None
                return out
            return fixed
        return node

    return _walk(value, path), notes


def annotate_dois_with_lit_num_ids(text: str) -> str:
    """Annotate every DOI token in compact text with its literature ID.

    JSON strings are handled structurally by the ReAct result validator.
    This helper covers markdown/plain-text compactors. Unknown DOI-like
    tokens are explicitly annotated with ``lit_num_id=null``.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    doi_to_lit, _ = _reference_id_maps()

    def replace(match: re.Match[str]) -> str:
        raw = match.group(0)
        candidate = raw
        suffix = ""
        lit_num_id: str | None = None
        while candidate:
            lit_num_id = doi_to_lit.get(candidate.casefold())
            if lit_num_id is not None:
                break
            suffix = candidate[-1] + suffix
            candidate = candidate[:-1]

        line_start = text.rfind("\n", 0, match.start()) + 1
        line_end = text.find("\n", match.end())
        if line_end < 0:
            line_end = len(text)
        line = text[line_start:line_end]

        if lit_num_id is not None:
            if lit_num_id in line:
                return raw
            return f"{candidate} [{lit_num_id}]{suffix}"

        if "lit_num_id=null" in line:
            return raw
        return f"{raw} [lit_num_id=null]"

    return _DOI_TEXT_RE.sub(replace, text)


def positive_ordinal(value: object, *, field: str) -> int:
    """Return a positive source ordinal or raise a field-specific error."""
    if isinstance(value, bool):
        raise ValueError(f"{field} must be a positive integer, got {value!r}")
    text = str(value).strip()
    if not _POSITIVE_ORDINAL_RE.fullmatch(text):
        raise ValueError(f"{field} must be a positive integer, got {value!r}")
    return int(text)


def global_id(field: str, source_ordinal: object | None) -> str | None:
    """Format one canonical registry ID; ``None`` remains an explicit null."""
    if source_ordinal is None:
        return None
    try:
        prefix = GLOBAL_PREFIX_BY_FIELD[field]
    except KeyError as exc:
        raise ValueError(f"Unknown global ID field: {field!r}") from exc
    return f"{prefix}{positive_ordinal(source_ordinal, field=field)}"


def require_global_id(field: str, value: object) -> str:
    """Validate and return an already formatted global ID."""
    try:
        prefix = GLOBAL_PREFIX_BY_FIELD[field]
    except KeyError as exc:
        raise ValueError(f"Unknown global ID field: {field!r}") from exc
    text = str(value)
    if not re.fullmatch(re.escape(prefix) + r"[1-9]\d*", text):
        raise ValueError(f"{field} must match {prefix}<positive integer>, got {value!r}")
    return text


def global_ordinal(field: str, value: object) -> int:
    """Extract the ordinal from a strictly validated global ID."""
    text = require_global_id(field, value)
    return int(text[len(GLOBAL_PREFIX_BY_FIELD[field]) :])


def doi_comp_id(source_ordinal: object) -> str:
    return f"DOIcomp_{positive_ordinal(source_ordinal, field='org_num')}"


def require_doi_comp_id(value: object) -> str:
    text = str(value)
    if not _DOI_COMP_RE.fullmatch(text):
        raise ValueError(f"org_num must match DOIcomp_<positive integer>, got {value!r}")
    return text


def doi_comp_ordinal(value: object) -> int:
    match = _DOI_COMP_RE.fullmatch(require_doi_comp_id(value))
    assert match is not None
    return int(match.group(1))


def doi_comp_sample_id(comp_ordinal: object, sample_ordinal: object) -> str:
    """Create a sample ID that remains unambiguous outside its parent object."""
    comp_n = positive_ordinal(comp_ordinal, field="sample parent org_num")
    sample_n = positive_ordinal(sample_ordinal, field="sample_num")
    return f"DOIcompSample_{comp_n}_{sample_n}"


def require_doi_comp_sample_id(
    value: object,
    *,
    component_org_num: object | None = None,
) -> str:
    """Validate a DOI-scoped sample ID and, optionally, its parent component."""
    text = str(value)
    match = _DOI_COMP_SAMPLE_RE.fullmatch(text)
    if not match:
        raise ValueError(
            "sample_num must match DOIcompSample_<component>_<sample>, "
            f"got {value!r}"
        )
    if component_org_num is not None:
        parent = require_doi_comp_id(component_org_num)
        if int(match.group(1)) != doi_comp_ordinal(parent):
            raise ValueError(
                f"sample_num {text!r} does not belong to component {parent!r}"
            )
    return text


def block_id(block_type: str, source_ordinal: object) -> str:
    prefix_by_type = {
        "PureOrMixtureData": "PROPblock_",
        "ReactionData": "RXNblock_",
    }
    try:
        prefix = prefix_by_type[block_type]
    except KeyError as exc:
        raise ValueError(f"Unsupported ThermoML block type: {block_type!r}") from exc
    return f"{prefix}{positive_ordinal(source_ordinal, field=f'{block_type} number')}"


def require_block_id(value: object, *, block_type: str | None = None) -> str:
    text = str(value)
    match = _BLOCK_ID_RE.fullmatch(text)
    if not match:
        raise ValueError(
            f"block_number must match PROPblock_<n> or RXNblock_<n>, got {value!r}"
        )
    if block_type is not None:
        prefix_by_type = {
            "PureOrMixtureData": "PROPblock",
            "ReactionData": "RXNblock",
        }
        try:
            expected = prefix_by_type[block_type]
        except KeyError as exc:
            raise ValueError(f"Unsupported ThermoML block type: {block_type!r}") from exc
        if match.group(1) != expected:
            raise ValueError(f"{value!r} conflicts with block_type={block_type!r}")
    return text


def block_local_id(kind: str, source_ordinal: object) -> str:
    if kind not in {"prop", "var", "constr", "point", "subsys"}:
        raise ValueError(f"Unsupported block-local ID kind: {kind!r}")
    return f"BLK{kind}_{positive_ordinal(source_ordinal, field=f'{kind} number')}"


def require_block_local_id(kind: str, value: object) -> str:
    text = str(value)
    match = _BLOCK_LOCAL_RE.fullmatch(text)
    if not match or match.group(1) != kind:
        raise ValueError(f"Expected BLK{kind}_<positive integer>, got {value!r}")
    return text


def block_local_ordinal(kind: str, value: object) -> int:
    text = require_block_local_id(kind, value)
    return int(text.split("_", 1)[1])


def property_assessment_id(prop_ordinal: object, assessment_ordinal: object) -> str:
    prop_n = positive_ordinal(prop_ordinal, field="property number")
    assess_n = positive_ordinal(assessment_ordinal, field="assessment_num")
    return f"BLKpropAssessment_{prop_n}_{assess_n}"


def require_property_assessment_id(
    value: object,
    *,
    BLKprop_id: object | None = None,
) -> str:
    """Validate a block-property uncertainty assessment identifier."""
    text = str(value)
    match = _PROPERTY_ASSESSMENT_RE.fullmatch(text)
    if not match:
        raise ValueError(
            "assessment_num must match BLKpropAssessment_<property>_<assessment>, "
            f"got {value!r}"
        )
    if BLKprop_id is not None:
        prop = require_block_local_id("prop", BLKprop_id)
        if int(match.group(1)) != block_local_ordinal("prop", prop):
            raise ValueError(
                f"assessment_num {text!r} does not belong to property {prop!r}"
            )
    return text


def component_template_id(base_id: str) -> str:
    """Declare a component-linked canonical type template."""
    if "{comp_id}" in base_id:
        raise ValueError(
            "Legacy component placeholder '{comp_id}' is invalid; "
            "use '{DOIcomp_id}'"
        )
    if "{DOIcomp_id}" in base_id:
        return base_id
    return f"{base_id}_{{DOIcomp_id}}"


def resolve_component_id(id_template: str, comp_ordinal: object | None) -> str:
    """Resolve a DOI-component placeholder for one card occurrence."""
    if "{comp_id}" in id_template:
        raise ValueError(
            "Legacy component placeholder '{comp_id}' is invalid; "
            "use '{DOIcomp_id}'"
        )
    template = id_template
    if comp_ordinal is None:
        return template
    if "{DOIcomp_id}" not in template:
        return template
    return template.replace("{DOIcomp_id}", doi_comp_id(comp_ordinal))


def base_component_id(identifier: str) -> str:
    """Remove only the declared DOI-component template suffix."""
    return identifier.replace("_{DOIcomp_id}", "")


def validate_nested_identifiers(value: object, *, path: str = "$") -> None:
    """Validate every identifier-bearing field in a card or tool result.

    The walk is intentionally structural and translation-free. It recognizes
    only the current generated-card field names and raises at the first
    malformed, wrong-scope, or retired identifier.
    """
    if isinstance(value, dict):
        if "number" in value:
            raise ValueError(f"{path}.number is a forbidden retired local-ID field")

        for key, child in value.items():
            child_path = f"{path}.{key}"
            global_field: str | None = None
            if key in GLOBAL_PREFIX_BY_FIELD:
                global_field = key
            elif key.endswith("_num_ids") and key[:-1] in GLOBAL_PREFIX_BY_FIELD:
                global_field = key[:-1]

            if global_field is not None:
                if key.endswith("_num_ids"):
                    if not isinstance(child, list):
                        raise TypeError(f"{child_path} must be a list of global IDs")
                    for index, item in enumerate(child):
                        require_global_id(global_field, item)
                elif child is not None:
                    require_global_id(global_field, child)

            if key in {"org_num", "component_org_num"} and child is not None:
                require_doi_comp_id(child)
            elif key == "sample_num" and child is not None:
                parent = value["org_num"] if "org_num" in value else None
                require_doi_comp_sample_id(child, component_org_num=parent)
            elif key == "block_number" and child is not None:
                block_type = value["block_type"] if "block_type" in value else None
                require_block_id(child, block_type=block_type)
            elif key == "block_numbers":
                if not isinstance(child, list):
                    raise TypeError(f"{child_path} must be a list of typed block IDs")
                for block_index, block_value in enumerate(child):
                    try:
                        require_block_id(block_value)
                    except ValueError as exc:
                        raise ValueError(f"{child_path}[{block_index}]: {exc}") from exc
            elif key in {
                "BLKprop_id",
                "BLKvar_id",
                "BLKconstr_id",
                "BLKpoint_id",
                "BLKsubsys_id",
            } and child is not None:
                require_block_local_id(key[3:-3], child)
            elif key == "BLKsubsys_refs":
                if not isinstance(child, list):
                    raise TypeError(f"{child_path} must be a list of BLKsubsys IDs")
                for local_id in child:
                    require_block_local_id("subsys", local_id)
            elif key == "assessment_num" and child is not None:
                owner = value["BLKprop_id"] if "BLKprop_id" in value else None
                require_property_assessment_id(child, BLKprop_id=owner)
            elif key == "variable_values":
                if not isinstance(child, dict):
                    raise TypeError(f"{child_path} must be an object keyed by BLKvar IDs")
                for local_id in child:
                    require_block_local_id("var", local_id)
            elif key == "property_values":
                if not isinstance(child, dict):
                    raise TypeError(f"{child_path} must be an object keyed by BLKprop IDs")
                for local_id in child:
                    require_block_local_id("prop", local_id)
            elif key == "constraint_values":
                if not isinstance(child, dict):
                    raise TypeError(f"{child_path} must be an object keyed by BLKconstr IDs")
                for local_id in child:
                    require_block_local_id("constr", local_id)

            validate_nested_identifiers(child, path=child_path)
        return

    if isinstance(value, list):
        for index, child in enumerate(value):
            validate_nested_identifiers(child, path=f"{path}[{index}]")
        return

    if isinstance(value, str):
        if _RETIRED_ID_RE.fullmatch(value):
            raise ValueError(f"{path} contains retired unscoped identifier {value!r}")
        if "{comp_id}" in value:
            raise ValueError(f"{path} contains retired component template {value!r}")
