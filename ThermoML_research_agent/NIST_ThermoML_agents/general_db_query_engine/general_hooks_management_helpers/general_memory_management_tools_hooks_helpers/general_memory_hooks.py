"""
General working-memory base class — shared by query and analysis agents.
========================================================================
Provides a **unified ID Catalog** for all entity types (compounds,
properties, variables, constraints, measurements, solvents, phases),
along with core serialisation helpers and merge logic.

Each agent subclasses and adds its own session management, persistence,
and tool-result extraction.  Literature (``lit_num_id``) is handled
separately outside the catalog.

Supported entity types and their exact global-ID fields
--------------------------------------------------------
| type    | global-ID field    |
|---------|--------------------|
| comp    | comp_num_id     |
| prop    | prop_num_id     |
| var     | var_num_id      |
| constr  | constr_num_id   |
| meas    | meas_num_id     |
| solvent | solvent_num_id  |
| phase   | phase_num_id    |

Public API
----------
BaseWorkingMemory
    .add_entity(entity_type, name, global_id, **extras)
    .merge_entity(entity_type, name, **fields)
    .find_entity_by_global_id(entity_type, global_id) -> (name, info) | None
    .find_entity_by_name(entity_type, name)     -> (key, info) | None
    .add_compound / merge_compound / find_compound_by_*  (convenience)
    .add_property  (convenience)
    .ingest_block_metadata(metadata)            -> None
    .render_id_catalog() -> str
normalize_name(raw) -> str
extract_entities_from_block_metadata(metadata) -> dict[str, list[dict]]
"""

from __future__ import annotations

import logging
import re
from collections import defaultdict

from ThermoML_raw_json_to_card_db_parsers.id_schema import (
    require_block_local_id,
    require_doi_comp_id,
    require_global_id,
)

log = logging.getLogger("BASE-WM")


# ── Name normalisation ───────────────────────────────────────

_BOLD_RE = re.compile(r"\*\*?|__?")
_STOP_WORDS = frozenset({
    "for", "the", "of", "and", "or", "in", "at", "to", "by",
    "is", "a", "an", "with",
})


def normalize_name(raw: str) -> str:
    """Canonical lowercase name: strip markdown, leading stop-words."""
    name = _BOLD_RE.sub("", raw).strip().strip(",;. ").lower()
    parts = name.split()
    while parts and parts[0] in _STOP_WORDS:
        parts.pop(0)
    return " ".join(parts)


# ── Entity-type metadata ────────────────────────────────────

# Maps entity type → its strict global-ID field inside metadata dicts.
_GLOBAL_ID_FIELD: dict[str, str] = {
    "comp":    "comp_num_id",
    "prop":    "prop_num_id",
    "var":     "var_num_id",
    "constr":  "constr_num_id",
    "meas":    "meas_num_id",
    "solvent": "solvent_num_id",
    "phase":   "phase_num_id",
    "lit":     "lit_num_id",
    "blocktype": "blocktype_num_id",
    "rxntype": "rxn_type_num_id",
}

# Entity types that can carry pure_values (shown in the catalog column)
_PURE_VALUE_TYPES = frozenset({"comp"})


def _global_id_field(entity_type: str) -> str:
    """Return the metadata field containing this entity's strict global ID."""
    try:
        return _GLOBAL_ID_FIELD[entity_type]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported ThermoML catalog entity type: {entity_type!r}"
        ) from exc


# ── Shared entity extraction from block metadata ────────────

def extract_entities_from_block_metadata(metadata: dict) -> dict[str, list[dict]]:
    """Extract all entity types from block metadata (from ``11_block_data_extractor``).

    The block metadata has:
      - ``compounds``: ``[{comp_num_id, org_num, name, formula}]``
      - ``variables``: ``[{var_num_id, var_id, column_name, compound}]``
      - ``properties``: ``[{prop_num_id, prop_ID, column_name, prop_group, compound}]``
      - ``constraints``: ``[{constr_num_id, constr_id, column_name, compound}]``

    Returns a dict keyed by entity type.  Each value is a list of
    ``{name: str, global_id: GLOB*, ...extras}``. Literature is excluded.
    Missing, null, DOI-local, and block-local values are rejected rather than
    retained as unresolved catalog entries.
    """
    if not isinstance(metadata, dict):
        raise TypeError("block metadata must be an object")
    required_arrays = ("compounds", "variables", "properties", "constraints")
    for field in required_arrays:
        if field not in metadata or not isinstance(metadata[field], list):
            raise ValueError(f"block metadata requires array field {field!r}")

    entities: dict[str, list[dict]] = {}

    # ── Compounds ──
    comps = []
    for c in metadata["compounds"]:
        if not isinstance(c, dict):
            raise TypeError("metadata.compounds entries must be objects")
        required = {"name", "comp_num_id", "org_num", "formula"}
        missing = required - c.keys()
        if missing:
            raise ValueError(f"compound metadata missing fields: {sorted(missing)}")
        if not isinstance(c["name"], str) or not c["name"].strip():
            raise ValueError("compound metadata name must be a non-empty string")
        require_doi_comp_id(c["org_num"])
        require_global_id("comp_num_id", c["comp_num_id"])
        comps.append({
            "name": c["name"],
            "global_id": c["comp_num_id"],
            "formula": c["formula"],
        })
    if comps:
        entities["comp"] = comps

    # ── Variables ──
    vars_ = []
    for v in metadata["variables"]:
        if not isinstance(v, dict):
            raise TypeError("metadata.variables entries must be objects")
        required = {"BLKvar_id", "column_name", "var_num_id", "var_id"}
        missing = required - v.keys()
        if missing:
            raise ValueError(f"variable metadata missing fields: {sorted(missing)}")
        if not isinstance(v["column_name"], str) or not v["column_name"].strip():
            raise ValueError("variable column_name must be a non-empty string")
        require_block_local_id("var", v["BLKvar_id"])
        require_global_id("var_num_id", v["var_num_id"])
        if not isinstance(v["var_id"], str) or not v["var_id"]:
            raise ValueError("variable var_id must be a non-empty string")
        vars_.append({
            "name": v["column_name"],
            "global_id": v["var_num_id"],
            "var_id": v["var_id"],
        })
    if vars_:
        entities["var"] = vars_

    # ── Properties ──
    props = []
    for p in metadata["properties"]:
        if not isinstance(p, dict):
            raise TypeError("metadata.properties entries must be objects")
        required = {"BLKprop_id", "column_name", "prop_num_id", "prop_ID", "prop_group"}
        missing = required - p.keys()
        if missing:
            raise ValueError(f"property metadata missing fields: {sorted(missing)}")
        if not isinstance(p["column_name"], str) or not p["column_name"].strip():
            raise ValueError("property column_name must be a non-empty string")
        require_block_local_id("prop", p["BLKprop_id"])
        require_global_id("prop_num_id", p["prop_num_id"])
        if not isinstance(p["prop_ID"], str) or not p["prop_ID"]:
            raise ValueError("property prop_ID must be a non-empty string")
        props.append({
            "name": p["column_name"],
            "global_id": p["prop_num_id"],
            "prop_ID": p["prop_ID"],
            "prop_group": p["prop_group"],
        })
    if props:
        entities["prop"] = props

    # ── Constraints ──
    constrs = []
    for c in metadata["constraints"]:
        if not isinstance(c, dict):
            raise TypeError("metadata.constraints entries must be objects")
        required = {"BLKconstr_id", "column_name", "constr_num_id", "constr_id"}
        missing = required - c.keys()
        if missing:
            raise ValueError(f"constraint metadata missing fields: {sorted(missing)}")
        if not isinstance(c["column_name"], str) or not c["column_name"].strip():
            raise ValueError("constraint column_name must be a non-empty string")
        require_block_local_id("constr", c["BLKconstr_id"])
        require_global_id("constr_num_id", c["constr_num_id"])
        if not isinstance(c["constr_id"], str) or not c["constr_id"]:
            raise ValueError("constraint constr_id must be a non-empty string")
        constrs.append({
            "name": c["column_name"],
            "global_id": c["constr_num_id"],
            "constr_id": c["constr_id"],
        })
    if constrs:
        entities["constr"] = constrs

    return entities


# ── Base class ───────────────────────────────────────────────

class BaseWorkingMemory:
    """Core ID-catalog state shared by every agent.

    All resolved entities live in ``self._catalog[entity_type][name]``.
    Convenience properties ``resolved_compounds`` and ``resolved_properties``
    provide direct references to the most-used sub-dicts.

    Subclasses must call ``super().__init__()`` and may override
    ``render()`` to append agent-specific sections after the catalog.
    """

    def __init__(self) -> None:
        # entity_type → {normalised_name → {global-ID field: GLOB* string, ...}}
        self._catalog: dict[str, dict[str, dict]] = defaultdict(dict)

    # ── Generic entity operations ────────────────────────────

    def add_entity(
        self,
        entity_type: str,
        name: str,
        global_id: str,
        **extras,
    ) -> None:
        """Register or update an entity in the ID catalog.

        If an entity with the same *global_id* already exists under a
        different name within the same type, the entries are merged
        under the new canonical ``name`` and the old key is removed.
        """
        key = normalize_name(name)
        if not key:
            raise ValueError(f"{entity_type} catalog name must be non-empty")

        global_field = _global_id_field(entity_type)
        global_id = require_global_id(
            global_field, global_id
        )
        section = self._catalog[entity_type]

        # Dedup: merge if the same strict global ID exists under another name.
        for existing_key, info in list(section.items()):
            if (
                existing_key != key
                and isinstance(info, dict)
                and info.get(global_field) == global_id
            ):
                merged = dict(info)
                merged.update(extras)
                merged[global_field] = global_id
                section[key] = merged
                del section[existing_key]
                log.debug(
                    "Merged %s '%s' into '%s' (%s)",
                    entity_type, existing_key, key, global_id,
                )
                return

        entry = section.get(key)
        if isinstance(entry, dict):
            entry[global_field] = global_id
            entry.update(extras)
        else:
            d: dict = {global_field: global_id}
            d.update(extras)
            section[key] = d

    def merge_entity(self, entity_type: str, name: str, **fields) -> None:
        """Merge fields into an existing entity, matching by name then global ID.

        A missing entry is created only when *fields* contains the exact
        canonical global ID. Name-only records do not belong in the ID catalog.
        """
        key = normalize_name(name)
        if not key:
            raise ValueError(f"{entity_type} catalog name must be non-empty")

        global_field = _global_id_field(entity_type)
        section = self._catalog[entity_type]
        if global_field in fields:
            fields[global_field] = require_global_id(
                global_field, fields[global_field]
            )

        # Exact name match
        entry = section.get(key)
        if isinstance(entry, dict):
            entry.update(fields)
            return

        # Match by the exact canonical global ID.
        global_id = fields.get(global_field)
        if global_id is not None:
            for _k, info in section.items():
                if isinstance(info, dict) and info.get(global_field) == global_id:
                    info.update(fields)
                    return

        if global_id is None:
            raise ValueError(
                f"Cannot create {entity_type!r} catalog entry {name!r} without "
                f"its {global_field}"
            )

        section[key] = dict(fields)

    def find_entity_by_global_id(
        self, entity_type: str, global_id: str,
    ) -> tuple[str, dict] | None:
        """Look up an entity by its exact canonical global ID."""
        global_field = _global_id_field(entity_type)
        global_id = require_global_id(
            global_field, global_id
        )
        for name, info in self._catalog.get(entity_type, {}).items():
            if isinstance(info, dict) and info.get(global_field) == global_id:
                return name, info
        return None

    def find_entity_by_name(
        self, entity_type: str, name: str,
    ) -> tuple[str, dict] | None:
        """Lookup entity by normalised name → (key, info) or None."""
        key = normalize_name(name)
        entry = self._catalog.get(entity_type, {}).get(key)
        if isinstance(entry, dict):
            return key, entry
        return None

    # ── Compound convenience methods ─────────────────────────

    def add_compound(self, name: str, comp_num_id: str, **extras) -> None:
        self.add_entity("comp", name, comp_num_id, **extras)

    def merge_compound(self, name: str, **fields) -> None:
        self.merge_entity("comp", name, **fields)

    def find_compound_by_global_id(self, comp_num_id: str) -> tuple[str, dict] | None:
        return self.find_entity_by_global_id("comp", comp_num_id)

    def find_compound_by_name(self, name: str) -> tuple[str, dict] | None:
        return self.find_entity_by_name("comp", name)

    # ── Property convenience methods ─────────────────────────

    def add_property(self, name: str, prop_num_id: str, **extras) -> None:
        self.add_entity("prop", name, prop_num_id, **extras)

    # ── Bulk ingestion from block metadata ───────────────────

    def ingest_block_metadata(self, metadata: dict) -> None:
        """Register all entities from block metadata in the catalog.

        Calls ``extract_entities_from_block_metadata`` and then
        ``add_entity`` for each item.  Subclasses can override to
        add agent-specific logic (e.g. storing inspected-blocks list).
        """
        for etype, items in extract_entities_from_block_metadata(metadata).items():
            for item in items:
                name = item.pop("name")
                if "global_id" not in item:
                    raise ValueError(
                        f"block metadata {etype!r} entity {name!r} has no global_id"
                    )
                global_id = item.pop("global_id")
                self.add_entity(etype, name, global_id, **item)

    # ── Serialisation ────────────────────────────────────────

    def render_id_catalog(self) -> str:
        """Render the ID Catalog as a markdown table.

        All entity types with at least one entry are included.
        Compounds get a ``pure_values`` column; other types leave it
        blank.

        ``| type | global_id | name | pure_values |``
        """
        rows: list[str] = []

        for etype in (
            "comp", "prop", "var", "constr", "meas", "solvent", "phase",
            "lit", "blocktype", "rxntype",
        ):
            section = self._catalog.get(etype)
            if not section:
                continue
            global_field = _global_id_field(etype)

            for name, info in section.items():
                if not isinstance(info, dict):
                    raise TypeError(
                        f"catalog entry {etype}.{name} must be an object"
                    )
                if global_field not in info:
                    raise ValueError(
                        f"catalog entry {etype}.{name} is missing {global_field}"
                    )
                nid_str = require_global_id(global_field, info[global_field])
                # Pure-values column (compounds only)
                pv_str = ""
                if etype in _PURE_VALUE_TYPES:
                    pv = info.get("pure_values")
                    if pv is not None:
                        if isinstance(pv, dict):
                            pv_str = "; ".join(f"{k}={v}" for k, v in pv.items())
                        else:
                            pv_str = str(pv)
                rows.append(f"| {etype} | {nid_str} | {name} | {pv_str} |")

        if not rows:
            return ""
        header = (
            "### ID Catalog\n"
            "| type | global_id | name | pure_values |\n"
            "|------|--------|------|-------------|"
        )
        return header + "\n" + "\n".join(rows)

    def render(self) -> str:
        """Render the full working memory.  Subclasses extend this."""
        return self.render_id_catalog()
