"""File-backed structured-markdown working memory.

The working memory is a single ``.md`` file with three sections:

1. **ID Catalog** — protected table of strict global IDs. Never auto-compacted.
2. **History**    — append-only log of agent actions.  Compactable.
3. **Results**    — indexed findings from search/analysis.  Compactable.

Public API
----------
WorkingMemory(path)
    .read(section=None)           -> str   (full file or one section)
    .append_history(line)         -> None
    .add_result(key, body)        -> None
    .catalog_add(type, global_id, registry_id, name) -> None
    .catalog_remove(type, global_id) -> None
    .catalog_list()               -> list[dict]
    .compact_section(section, summariser) -> None
    .reset()                      -> None  (re-initialise to empty template)
"""

from __future__ import annotations

import re
from pathlib import Path
from .session_manager_output_storage import _filesystem_path, ensure_directory
from typing import Callable

from ThermoML_raw_json_to_card_db_parsers.id_schema import require_global_id


_TEMPLATE = """\
# Working Memory

## ID Catalog
<!-- PROTECTED — never compacted. Auto-populated by catalog ops. -->
### Resolved Entities
| type | global_id | registry_id | name |
|------|--------|----|------|

### Reference IDs
| type | global_id | registry_id | name |
|------|--------|----|------|

## History
<!-- Append-only log. Compactable when >30 entries. -->

## Results
<!-- Indexed findings. Compactable per-entry. -->
"""

_KNOWN_SECTIONS = frozenset({"ID Catalog", "History", "Results"})
_SECTION_RE = re.compile(r"^## (.+)$", re.MULTILINE)
_CATALOG_ROW_RE = re.compile(
    r"^\|\s*(?P<type>\w+)\s*\|\s*(?P<global_id>GLOB[A-Za-z]+_[1-9]\d*)\s*\|\s*(?P<registry_id>[^|]+?)\s*\|\s*(?P<name>[^|]+?)\s*\|$",
    re.MULTILINE,
)

_GLOBAL_FIELD_BY_CATALOG_TYPE = {
    "comp": "comp_num_id",
    "prop": "prop_num_id",
    "var": "var_num_id",
    "constr": "constr_num_id",
    "meas": "meas_num_id",
    "solvent": "solvent_num_id",
    "phase": "phase_num_id",
    "lit": "lit_num_id",
    "blocktype": "blocktype_num_id",
    "rxntype": "rxn_type_num_id",
}

# Entity types stored as plain reference IDs (separate sub-table)
_REF_ONLY_FILE_TYPES = frozenset({"lit"})
# Sub-table header markers within '## ID Catalog'
_RESOLVED_HEADER = "### Resolved Entities"
_REF_HEADER = "### Reference IDs"


class WorkingMemory:
    """Read/write interface over a structured-md working-memory file."""

    def __init__(self, path: str | Path):
        self._path = Path(path)
        if not self._path.exists():
            self.reset()

    # -- low-level I/O -----------------------------------------------------

    def _load(self) -> str:
        return _filesystem_path(self._path).read_text(encoding="utf-8")

    def _save(self, text: str) -> None:
        ensure_directory(self._path.parent)
        _filesystem_path(self._path).write_text(text, encoding="utf-8")

    # -- section slicing ---------------------------------------------------

    @staticmethod
    def _section_bounds(text: str, section: str) -> tuple[int, int]:
        """Return (start, end) byte offsets of the *body* of ``## section``.

        Only the three known sections (ID Catalog, History, Results) are
        treated as boundaries — any ``## …`` headers that the LLM injects
        inside result bodies are ignored.
        """
        headers = [
            m for m in _SECTION_RE.finditer(text)
            if m.group(1).strip() in _KNOWN_SECTIONS
        ]
        for i, m in enumerate(headers):
            if m.group(1).strip() == section:
                body_start = m.end() + 1  # skip newline after heading
                body_end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
                return body_start, body_end
        raise KeyError(f"Section '## {section}' not found in memory file")

    # -- public API --------------------------------------------------------

    def read(self, section: str | None = None) -> str:
        """Return full file or a specific ``## section`` body."""
        text = self._load()
        if section is None:
            return text
        start, end = self._section_bounds(text, section)
        return text[start:end].strip()

    def append_history(self, line: str) -> None:
        """Append a one-line entry to the History section."""
        text = self._load()
        start, end = self._section_bounds(text, "History")
        body = text[start:end].rstrip()
        new_body = body + "\n" + f"- {line}" + "\n"
        self._save(text[:start] + new_body + "\n" + text[end:])

    @staticmethod
    def _escape_body(body: str) -> str:
        """Downgrade ``## `` headers in *body* to ``### `` to avoid breaking section parsing."""
        return re.sub(r"^## ", "### ", body, flags=re.MULTILINE)

    def add_result(self, key: str, body: str) -> None:
        """Add or replace a ``### key`` entry in the Results section."""
        body = self._escape_body(body)
        text = self._load()
        start, end = self._section_bounds(text, "Results")
        section_body = text[start:end]
        # Replace existing entry with same key (if any)
        key_re = re.compile(
            rf"^### {re.escape(key)}\n.*?(?=^### |\Z)",
            re.MULTILINE | re.DOTALL,
        )
        if key_re.search(section_body):
            new_section = key_re.sub(f"### {key}\n{body}\n", section_body, count=1)
            self._save(text[:start] + new_section + text[end:])
        else:
            existing = section_body.rstrip()
            entry = f"\n### {key}\n{body}\n"
            self._save(text[:start] + existing + entry + "\n" + text[end:])

    # -- catalog ops -------------------------------------------------------

    def catalog_list(self) -> list[dict]:
        """Return all catalog rows as dicts."""
        text = self.read("ID Catalog")
        return [m.groupdict() for m in _CATALOG_ROW_RE.finditer(text)]

    @staticmethod
    def _require_catalog_global_id(type_: str, global_id: object) -> str:
        try:
            field = _GLOBAL_FIELD_BY_CATALOG_TYPE[type_]
        except KeyError as exc:
            raise ValueError(f"Unsupported ThermoML catalog type: {type_!r}") from exc
        return require_global_id(field, global_id)

    def catalog_add(
        self, type_: str, global_id: str, registry_id: str, name: str,
    ) -> None:
        """Add a row to the ID Catalog (no-op if already present).

        Resolved entities go under ``### Resolved Entities``.
        Literature entries go under ``### Reference IDs``. All other
        supported ThermoML entity types go under ``### Resolved Entities``.
        Rows are deduplicated by exact global ID.
        """
        global_id = self._require_catalog_global_id(type_, global_id)
        existing = self.catalog_list()
        for row in existing:
            if row["global_id"] == global_id:
                return  # already present
        text = self._load()
        start, end = self._section_bounds(text, "ID Catalog")
        body = text[start:end]
        if not isinstance(registry_id, str) or not registry_id.strip():
            raise ValueError("registry_id must be a non-empty string")
        new_row = f"| {type_} | {global_id} | {registry_id.strip()} | {name} |"

        # Determine target sub-table header
        target_header = _REF_HEADER if type_ in _REF_ONLY_FILE_TYPES else _RESOLVED_HEADER

        # Find the target sub-table within the section body
        header_pos = body.find(target_header)
        if header_pos != -1:
            after_header = header_pos + len(target_header)
            next_sub = body.find("\n###", after_header)
            if next_sub == -1:
                insert_region = body[after_header:]
            else:
                insert_region = body[after_header:next_sub]

            last_pipe = insert_region.rfind("|")
            if last_pipe != -1:
                nl = insert_region.find("\n", last_pipe)
                if nl == -1:
                    insert_at = after_header + len(insert_region)
                else:
                    insert_at = after_header + nl + 1
            else:
                insert_at = after_header + len(insert_region)

            abs_insert = start + insert_at
            self._save(text[:abs_insert] + new_row + "\n" + text[abs_insert:])
        else:
            raise ValueError(
                f"Working-memory catalog is missing required section {target_header!r}"
            )

    def catalog_remove(self, type_: str, global_id: str) -> None:
        """Remove a row from the ID Catalog by type and exact global ID."""
        global_id = self._require_catalog_global_id(type_, global_id)
        text = self._load()
        start, end = self._section_bounds(text, "ID Catalog")
        body = text[start:end]
        pattern = re.compile(
            rf"^\|\s*{re.escape(type_)}\s*\|\s*{re.escape(global_id)}\s*\|.*\|.*\|\s*$",
            re.MULTILINE,
        )
        new_body = pattern.sub("", body)
        # collapse double blank lines
        new_body = re.sub(r"\n{3,}", "\n\n", new_body)
        self._save(text[:start] + new_body + text[end:])

    # -- compaction --------------------------------------------------------

    def compact_section(
        self, section: str, summariser: Callable[[str], str]
    ) -> None:
        """Replace a section body with a summary produced by *summariser*.

        *summariser* is a callable(str) -> str.  Typically an LLM call that
        condenses the text.  The ID Catalog section is never compactable.
        """
        if section == "ID Catalog":
            raise ValueError("ID Catalog is protected and cannot be compacted")
        text = self._load()
        start, end = self._section_bounds(text, section)
        old_body = text[start:end].strip()
        summary = summariser(old_body)
        self._save(text[:start] + "\n" + summary.strip() + "\n\n" + text[end:])

    # -- reset -------------------------------------------------------------

    def reset(self) -> None:
        """Re-initialise the memory file to the empty template."""
        self._save(_TEMPLATE)
