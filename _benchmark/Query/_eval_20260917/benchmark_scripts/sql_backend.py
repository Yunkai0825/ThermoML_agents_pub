"""Safe, lossless SQLite transport for the flat ThermoML benchmarks.

This module does no semantic compaction. The harness must pass raw_markdown,
plus the SQL purpose and tasks, to the separate agentic compactor. In sanitized
mode semantic ID prefixes are stripped to their raw numeric suffixes.
"""

from __future__ import annotations

import base64
import hashlib
import json
import math
import re
import sqlite3
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence
from urllib.parse import quote


_BACKTICK = chr(96)


class PrefixSanitizer:
    """Strip ThermoML semantic prefixes and retain raw numeric ID suffixes."""

    _CANONICAL_PREFIX_PATTERN = (
        r"(?:BLKpropAssessment|GLOBblocktype|DOIcompSample|GLOBsolvent|"
        r"GLOBconstr|GLOBrxntype|PROPblock|RXNblock|GLOBphase|GLOBcomp|"
        r"GLOBprop|GLOBvar|GLOBmeas|GLOBlit|BLKconstr|BLKsubsys|"
        r"BLKpoint|BLKprop|BLKvar|DOIcomp)"
    )
    _DOMAIN_ID_RE = re.compile(
        r"(?<![A-Za-z0-9])(?:GLOB|BLK|DOI|PROP|RXN)[A-Za-z0-9]*_"
        r"(?P<numeric>[0-9]+(?:_[0-9]+)*)(?![A-Za-z0-9_])"
    )
    _BARE_PREFIX_RE = re.compile(_CANONICAL_PREFIX_PATTERN + r"_?")

    def __init__(self) -> None:
        self._seen: set[str] = set()

    def sanitize_text(self, text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("sanitize_text expects str")

        def replace(match: re.Match[str]) -> str:
            self._seen.add(match.group(0))
            return match.group("numeric")

        return self._DOMAIN_ID_RE.sub(replace, text)

    def sanitize_output_text(self, text: str) -> str:
        """Sanitize full IDs and bare canonical prefixes in returned content."""

        sanitized = self.sanitize_text(text)
        return self._BARE_PREFIX_RE.sub("", sanitized)

    def restore_text(self, text: str) -> str:
        """Return raw-ID SQL unchanged; stripped namespaces are non-bijective."""

        if not isinstance(text, str):
            raise TypeError("restore_text expects str")
        return text

    @property
    def size(self) -> int:
        return len(self._seen)


@dataclass(slots=True)
class SqlExecution:
    raw_markdown: str
    visible_sql: str
    executed_sql: str
    columns: list[str]
    row_count: int
    truncated: bool
    elapsed_s: float
    sha256: str
    error: str | None = None


class SQLBackend:
    """Read-only backend for parsed-card or raw ThermoML SQLite databases."""

    _MODE_ALIASES = {
        "parsed": "parsed",
        "cards": "parsed",
        "parsed_cards": "parsed",
        "raw": "raw",
        "rawdb": "raw",
        "raw_thermoml": "raw",
    }
    _PARSED_DATABASES: tuple[tuple[str, str], ...] = (
        ("idx", "card_databases_storage/ThermoML_index.db"),
        ("registry", "card_databases_storage/PureOrMixtureData_registry.db"),
        ("reaction_registry", "card_databases_storage/ReactionData_registry.db"),
        ("pcs", "card_databases_storage/Individual_cards_dbs/PCS_INDIV.db"),
        ("ccs", "card_databases_storage/Individual_cards_dbs/CCS_INDIV.db"),
        ("rms", "card_databases_storage/Individual_cards_dbs/RMS_INDIV.db"),
        ("mtdks", "card_databases_storage/Individual_cards_dbs/MTDKS_INDIV.db"),
        ("compound_dk", "card_databases_storage/Individual_cards_dbs/CCS_ID_DK.db"),
        ("property_dk", "card_databases_storage/Individual_cards_dbs/PCS_ID_DK.db"),
        ("measurement_dk", "card_databases_storage/Individual_cards_dbs/MTDKS_ID_DK.db"),
    )
    _RAW_DATABASES: tuple[tuple[str, str], ...] = (
        ("raw", "ThermoML.v2020-09-30.db/thermoml_raw.db"),
    )

    def __init__(
        self,
        project_root: Path,
        mode: str,
        sanitize_prefix_ids: bool = False,
        max_result_chars: int = 800_000,
        timeout_s: float = 30,
    ) -> None:
        normalized_mode = self._MODE_ALIASES.get(str(mode).strip().lower())
        if normalized_mode is None:
            allowed = ", ".join(sorted(self._MODE_ALIASES))
            raise ValueError(f"Unsupported SQL mode {mode!r}; expected: {allowed}")
        if isinstance(max_result_chars, bool) or max_result_chars < 1:
            raise ValueError("max_result_chars must be a positive integer")
        if isinstance(timeout_s, bool) or float(timeout_s) <= 0:
            raise ValueError("timeout_s must be positive")

        self.project_root = self._resolve_project_root(Path(project_root))
        self.mode = normalized_mode
        self.sanitize_prefix_ids = bool(sanitize_prefix_ids)
        self.max_result_chars = int(max_result_chars)
        self.timeout_s = float(timeout_s)
        self.sanitizer = PrefixSanitizer()
        self._closed = False
        self._database_paths = self._resolve_database_paths()
        self._connection = sqlite3.connect(
            "file::memory:?cache=private",
            uri=True,
            isolation_level=None,
            timeout=min(self.timeout_s, 60.0),
        )
        try:
            self._connection.enable_load_extension(False)
            self._attach_databases()
            self._connection.create_function(
                "thermoml_raw_id",
                1,
                self._sql_raw_id,
                deterministic=True,
            )
            self._schema_markdown = self._build_schema_markdown()
            self._connection.execute("PRAGMA trusted_schema = OFF")
            self._connection.execute("PRAGMA query_only = ON")
            self._connection.set_authorizer(self._authorizer)
        except BaseException:
            self._connection.close()
            self._closed = True
            raise

    @staticmethod
    def _resolve_project_root(candidate: Path) -> Path:
        # Keep a mapped-drive spelling when one was supplied. Path.resolve()
        # turns it into a UNC URI whose non-local authority SQLite rejects.
        candidate = candidate.expanduser().absolute()
        if (candidate / "card_databases_storage").is_dir():
            return candidate
        nested = candidate / "ThermoML_research_agent"
        if (nested / "card_databases_storage").is_dir():
            return nested.absolute()
        raise FileNotFoundError(
            "Could not find the ThermoML_research_agent database layout below "
            f"{candidate}"
        )

    def _resolve_database_paths(self) -> tuple[tuple[str, Path], ...]:
        specs = self._PARSED_DATABASES if self.mode == "parsed" else self._RAW_DATABASES
        resolved: list[tuple[str, Path]] = []
        missing: list[Path] = []
        for alias, relative in specs:
            path = (self.project_root / Path(relative)).absolute()
            if not path.is_file() or path.stat().st_size <= 0:
                missing.append(path)
            else:
                resolved.append((alias, path))
        if missing:
            formatted = "\n".join(f"- {path}" for path in missing)
            raise FileNotFoundError(
                f"Required {self.mode} databases are missing or empty:\n{formatted}"
            )
        return tuple(resolved)

    @staticmethod
    def _quote_identifier(identifier: str) -> str:
        return '"' + identifier.replace('"', '""') + '"'

    @staticmethod
    def _read_only_uri(path: Path) -> str:
        if str(path).startswith("\\\\"):
            # Four slashes keep the UNC server in the path component. The
            # usual file://server form is an authority URI rejected by the
            # SQLite build used for these benchmarks.
            unc_path = quote(path.as_posix().lstrip("/"), safe="/:")
            return "file:////" + unc_path + "?mode=ro"
        return path.as_uri() + "?mode=ro"

    def _attach_databases(self) -> None:
        for alias, path in self._database_paths:
            self._connection.execute(
                f"ATTACH DATABASE ? AS {self._quote_identifier(alias)}",
                (self._read_only_uri(path),),
            )

    def _build_schema_markdown(self) -> str:
        lines = [
            f"# ThermoML SQLite schema ({self.mode})",
            "",
            "All databases are attached read-only. Qualify tables as alias.table_name.",
            "",
        ]
        if self.mode == "parsed":
            lines.extend(
                (
                    "## Usage notes",
                    "",
                    "- idx contains normalized searchable metadata and summary statistics.",
                    "- pcs.cards.json_data contains full parsed property cards; exact",
                    "  measurements are under blocks/data_points with variable_values",
                    "  and property_values. Use SQLite JSON functions to inspect them.",
                    "- ccs, rms, mtdks and the *_dk aliases contain the corresponding",
                    "  individual/domain-knowledge card JSON.",
                    "- Keep DOI and block/local-ID scope when joining card evidence.",
                    "",
                )
            )
        else:
            lines.extend(
                (
                    "## Usage notes",
                    "",
                    "- raw.papers.json_data contains the full raw parsed ThermoML",
                    "  document; PureOrMixtureData entries contain NumValues data.",
                    "- raw.compounds, raw.blocks, raw.block_properties and",
                    "  raw.block_variables are searchable indices into that corpus.",
                    "- Use SQLite JSON functions and narrow paths/filters rather than",
                    "  returning whole source documents.",
                    "",
                )
            )
        if self.sanitize_prefix_ids:
            lines.extend(
                (
                    "Returned structured IDs have their semantic prefix stripped,",
                    "leaving the raw numeric suffix (for example *_51 -> 51).",
                    "Raw IDs are not globally unique. Keep column/DOI/block scope.",
                    "For filters over a stored prefixed value use",
                    "thermoml_raw_id(column_name) = '51'.",
                    "",
                )
            )
        for alias, path in self._database_paths:
            quoted_alias = self._quote_identifier(alias)
            tables = self._connection.execute(
                f"SELECT name FROM {quoted_alias}.sqlite_master "
                "WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
            ).fetchall()
            lines.extend((f"## {alias} ({path.name})", ""))
            for (table_name,) in tables:
                quoted_table = self._quote_identifier(str(table_name))
                info = self._connection.execute(
                    f"PRAGMA {quoted_alias}.table_info({quoted_table})"
                ).fetchall()
                columns: list[str] = []
                for column in info:
                    detail = f"{column[1]} {str(column[2]).strip()}".rstrip()
                    if column[5]:
                        detail += " PRIMARY KEY"
                    if column[3]:
                        detail += " NOT NULL"
                    columns.append(detail)
                lines.append(f"- {alias}.{table_name}({', '.join(columns)})")
            if not tables:
                lines.append("(No user tables.)")
            lines.append("")
        markdown = "\n".join(lines).rstrip() + "\n"
        return (
            self.sanitizer.sanitize_text(markdown)
            if self.sanitize_prefix_ids
            else markdown
        )

    def schema_markdown(self) -> str:
        self._ensure_open()
        return self._schema_markdown

    def _sql_raw_id(self, value: Any) -> Any:
        """SQLite scalar for explicit comparisons against stripped ID values."""

        if value is None:
            return None
        if isinstance(value, str):
            return self.sanitizer.sanitize_output_text(value)
        return value

    @staticmethod
    def _denied_authorizer_actions() -> frozenset[int]:
        names = (
            "SQLITE_ALTER_TABLE",
            "SQLITE_ANALYZE",
            "SQLITE_ATTACH",
            "SQLITE_CREATE_INDEX",
            "SQLITE_CREATE_TABLE",
            "SQLITE_CREATE_TEMP_INDEX",
            "SQLITE_CREATE_TEMP_TABLE",
            "SQLITE_CREATE_TEMP_TRIGGER",
            "SQLITE_CREATE_TEMP_VIEW",
            "SQLITE_CREATE_TRIGGER",
            "SQLITE_CREATE_VIEW",
            "SQLITE_CREATE_VTABLE",
            "SQLITE_DELETE",
            "SQLITE_DETACH",
            "SQLITE_DROP_INDEX",
            "SQLITE_DROP_TABLE",
            "SQLITE_DROP_TEMP_INDEX",
            "SQLITE_DROP_TEMP_TABLE",
            "SQLITE_DROP_TEMP_TRIGGER",
            "SQLITE_DROP_TEMP_VIEW",
            "SQLITE_DROP_TRIGGER",
            "SQLITE_DROP_VIEW",
            "SQLITE_DROP_VTABLE",
            "SQLITE_INSERT",
            "SQLITE_PRAGMA",
            "SQLITE_REINDEX",
            "SQLITE_SAVEPOINT",
            "SQLITE_TRANSACTION",
            "SQLITE_UPDATE",
        )
        return frozenset(
            value
            for name in names
            if isinstance((value := getattr(sqlite3, name, None)), int)
        )

    def _authorizer(
        self,
        action_code: int,
        arg1: str | None,
        arg2: str | None,
        database_name: str | None,
        trigger_name: str | None,
    ) -> int:
        del database_name, trigger_name
        if action_code in self._denied_authorizer_actions():
            return sqlite3.SQLITE_DENY
        if action_code == getattr(sqlite3, "SQLITE_FUNCTION", -1):
            function_name = (arg2 or arg1 or "").lower()
            if function_name == "load_extension" or function_name.startswith("pragma_"):
                return sqlite3.SQLITE_DENY
        return sqlite3.SQLITE_OK

    def execute(
        self,
        sql: str,
        purpose: str,
        tasks: list[str],
        max_rows: int = 500,
    ) -> SqlExecution:
        """Execute one query and serialize it without semantic compaction.

        purpose and tasks are mandatory context for the downstream agentic
        compactor. They are included verbatim in the raw Markdown envelope.
        """

        self._ensure_open()
        started = time.monotonic()
        if not isinstance(sql, str) or not sql.strip():
            return self._error_execution(
                sql if isinstance(sql, str) else repr(sql),
                "SQL must be a nonempty string.",
                purpose,
                tasks,
                started,
            )
        if not isinstance(purpose, str) or not purpose.strip():
            return self._error_execution(
                sql,
                "purpose must be a nonempty string describing why this SQL is needed.",
                purpose,
                tasks,
                started,
            )
        if (
            not isinstance(tasks, list)
            or not tasks
            or any(not isinstance(task, str) or not task.strip() for task in tasks)
        ):
            return self._error_execution(
                sql,
                "tasks must be a nonempty list of nonempty strings.",
                purpose,
                tasks,
                started,
            )
        if (
            isinstance(max_rows, bool)
            or not isinstance(max_rows, int)
            or not 1 <= max_rows <= 2_000
        ):
            return self._error_execution(
                sql,
                "max_rows must be an integer from 1 through 2000.",
                purpose,
                tasks,
                started,
            )

        submitted_sql = sql.strip()
        executed_sql = (
            self.sanitizer.restore_text(submitted_sql)
            if self.sanitize_prefix_ids
            else submitted_sql
        )
        visible_sql = (
            self.sanitizer.sanitize_text(executed_sql)
            if self.sanitize_prefix_ids
            else executed_sql
        )
        validation_error = self._validate_statement(executed_sql)
        if validation_error is not None:
            return self._error_execution(
                executed_sql,
                validation_error,
                purpose,
                tasks,
                started,
                visible_sql=visible_sql,
            )

        deadline = time.monotonic() + self.timeout_s
        self._connection.set_progress_handler(
            lambda: 1 if time.monotonic() >= deadline else 0, 1_000
        )
        try:
            cursor = self._connection.execute(executed_sql)
            if cursor.description is None:
                raise sqlite3.DatabaseError(
                    "Statement did not produce a read-only result set."
                )
            columns = [self._visible_text(str(item[0])) for item in cursor.description]
            # Stream rows into the character budget. This avoids materializing
            # max_rows worth of wide JSON documents before rejecting them.
            json_rows: list[list[Any]] = []
            estimated_chars = (
                len(visible_sql)
                + len(purpose)
                + sum(len(task) for task in tasks)
                + len(self._json_dump(columns))
                + 2_048
            )
            while True:
                row = cursor.fetchone()
                if row is None:
                    break
                if len(json_rows) >= max_rows:
                    return self._error_execution(
                        executed_sql,
                        f"Query returned more than max_rows={max_rows}. Run "
                        "narrower SQL with filters, aggregation, or an explicit "
                        "LIMIT. No partial row payload was returned and no "
                        "semantic compaction was performed.",
                        purpose,
                        tasks,
                        started,
                        visible_sql=visible_sql,
                        columns=columns,
                        row_count=len(json_rows) + 1,
                        truncated=True,
                    )
                json_row = [self._json_value(value) for value in row]
                estimated_chars += len(self._json_dump(json_row)) + 1
                if estimated_chars > self.max_result_chars:
                    return self._error_execution(
                        executed_sql,
                        "Serialized SQL result exceeded "
                        f"max_result_chars={self.max_result_chars:,} while "
                        f"streaming row {len(json_rows) + 1}. Run narrower SQL: "
                        "select fewer columns, add filters, aggregate, or lower "
                        "max_rows. No partial row payload was returned and no "
                        "semantic compaction was performed.",
                        purpose,
                        tasks,
                        started,
                        visible_sql=visible_sql,
                        columns=columns,
                        row_count=len(json_rows) + 1,
                        truncated=True,
                    )
                json_rows.append(json_row)
            truncated = False
            elapsed_s = time.monotonic() - started
            markdown = self._render_result(
                visible_sql=visible_sql,
                purpose=purpose,
                tasks=tasks,
                columns=columns,
                rows=json_rows,
                truncated=truncated,
                elapsed_s=elapsed_s,
                max_rows=max_rows,
            )
            if len(markdown) > self.max_result_chars:
                message = (
                    f"Serialized SQL result was {len(markdown):,} characters, "
                    f"exceeding max_result_chars={self.max_result_chars:,}. "
                    "Run narrower SQL: select fewer columns, add filters, "
                    "aggregate, or lower max_rows. No row payload was returned "
                    "and no semantic compaction was performed."
                )
                return self._error_execution(
                    executed_sql,
                    message,
                    purpose,
                    tasks,
                    started,
                    visible_sql=visible_sql,
                    columns=columns,
                    row_count=len(json_rows),
                    truncated=truncated,
                )
            return SqlExecution(
                raw_markdown=markdown,
                visible_sql=visible_sql,
                executed_sql=executed_sql,
                columns=columns,
                row_count=len(json_rows),
                truncated=truncated,
                elapsed_s=elapsed_s,
                sha256=hashlib.sha256(markdown.encode("utf-8")).hexdigest(),
                error=None,
            )
        except sqlite3.Error as exc:
            message = str(exc)
            if "interrupted" in message.lower() and time.monotonic() >= deadline:
                message = (
                    f"SQL exceeded the {self.timeout_s:g}-second execution timeout. "
                    "Use a narrower or better-indexed query."
                )
            return self._error_execution(
                executed_sql,
                message,
                purpose,
                tasks,
                started,
                visible_sql=visible_sql,
            )
        finally:
            self._connection.set_progress_handler(None, 0)

    def _validate_statement(self, sql: str) -> str | None:
        leading = self._strip_leading_comments(sql)
        if not re.match(
            r"(?is)^(?:SELECT\b|WITH\b|EXPLAIN\s+QUERY\s+PLAN\b)", leading
        ):
            return (
                "Only one read-only SELECT, WITH, or EXPLAIN QUERY PLAN "
                "statement is allowed."
            )
        if self._has_statement_after_semicolon(sql):
            return "Exactly one SQL statement is allowed."
        return None

    @staticmethod
    def _strip_leading_comments(sql: str) -> str:
        remaining = sql.lstrip()
        while remaining:
            if remaining.startswith("--"):
                newline = remaining.find("\n")
                if newline < 0:
                    return ""
                remaining = remaining[newline + 1 :].lstrip()
                continue
            if remaining.startswith("/*"):
                end = remaining.find("*/", 2)
                if end < 0:
                    return remaining
                remaining = remaining[end + 2 :].lstrip()
                continue
            break
        return remaining

    @classmethod
    def _has_statement_after_semicolon(cls, sql: str) -> bool:
        """Return true when non-comment SQL follows a top-level semicolon."""

        state = "normal"
        index = 0
        first_semicolon: int | None = None
        while index < len(sql):
            char = sql[index]
            next_char = sql[index + 1] if index + 1 < len(sql) else ""
            if state == "normal":
                if char == "'":
                    state = "single"
                elif char == '"':
                    state = "double"
                elif char == _BACKTICK:
                    state = "backtick"
                elif char == "[":
                    state = "bracket"
                elif char == "-" and next_char == "-":
                    state = "line_comment"
                    index += 1
                elif char == "/" and next_char == "*":
                    state = "block_comment"
                    index += 1
                elif char == ";":
                    first_semicolon = index
                    break
            elif state == "single" and char == "'":
                if next_char == "'":
                    index += 1
                else:
                    state = "normal"
            elif state == "double" and char == '"':
                if next_char == '"':
                    index += 1
                else:
                    state = "normal"
            elif state == "backtick" and char == _BACKTICK:
                if next_char == _BACKTICK:
                    index += 1
                else:
                    state = "normal"
            elif state == "bracket" and char == "]":
                state = "normal"
            elif state == "line_comment" and char in "\r\n":
                state = "normal"
            elif state == "block_comment" and char == "*" and next_char == "/":
                state = "normal"
                index += 1
            index += 1

        if first_semicolon is None:
            return False
        tail = cls._strip_leading_comments(sql[first_semicolon + 1 :])
        return bool(tail.strip())

    def _visible_text(self, value: str) -> str:
        return (
            self.sanitizer.sanitize_output_text(value)
            if self.sanitize_prefix_ids
            else value
        )

    def _json_value(self, value: Any) -> Any:
        if value is None or isinstance(value, (str, int)):
            return self._visible_text(value) if isinstance(value, str) else value
        if isinstance(value, float):
            if math.isnan(value):
                return {"$sqlite_float": "NaN"}
            if math.isinf(value):
                return {
                    "$sqlite_float": "Infinity" if value > 0 else "-Infinity"
                }
            return value
        if isinstance(value, (bytes, bytearray, memoryview)):
            payload = bytes(value)
            return {
                "$sqlite_blob_base64": base64.b64encode(payload).decode("ascii"),
                "$byte_length": len(payload),
            }
        raise TypeError(f"Unsupported SQLite result type: {type(value).__name__}")

    @staticmethod
    def _json_dump(value: Any) -> str:
        return json.dumps(
            value,
            ensure_ascii=False,
            separators=(",", ":"),
            allow_nan=False,
        )

    @staticmethod
    def _fenced(payload: str, language: str = "") -> str:
        runs = re.findall(re.escape(_BACKTICK) + r"+", payload)
        longest = max((len(run) for run in runs), default=0)
        fence = _BACKTICK * max(3, longest + 1)
        return f"{fence}{language}\n{payload}\n{fence}"

    def _render_result(
        self,
        *,
        visible_sql: str,
        purpose: str,
        tasks: Sequence[str],
        columns: Sequence[str],
        rows: Sequence[Sequence[Any]],
        truncated: bool,
        elapsed_s: float,
        max_rows: int,
    ) -> str:
        visible_purpose = self._visible_text(purpose.strip())
        visible_tasks = [self._visible_text(task.strip()) for task in tasks]
        rows_jsonl = "\n".join(self._json_dump(list(row)) for row in rows)
        truncation_note = (
            f"Yes. More than {max_rows} rows were available; only the first "
            f"{max_rows} are serialized."
            if truncated
            else "No."
        )
        return "\n".join(
            (
                "# Raw SQLite tool result",
                "",
                "This is a lossless transport serialization, not a semantic summary.",
                "",
                "## SQL purpose",
                "",
                visible_purpose,
                "",
                "## SQL tasks",
                "",
                self._fenced(self._json_dump(visible_tasks), "json"),
                "",
                "## Executed SQL (visible form)",
                "",
                self._fenced(visible_sql, "sql"),
                "",
                "## Result metadata",
                "",
                f"- Rows serialized: {len(rows)}",
                f"- Truncated by max_rows: {truncation_note}",
                f"- Elapsed seconds: {elapsed_s:.6f}",
                "",
                "## Columns",
                "",
                self._fenced(self._json_dump(list(columns)), "json"),
                "",
                "## Rows (JSONL arrays in column order)",
                "",
                self._fenced(rows_jsonl, "jsonl"),
                "",
            )
        )

    def _error_execution(
        self,
        sql: str,
        message: str,
        purpose: Any,
        tasks: Any,
        started: float,
        *,
        visible_sql: str | None = None,
        columns: Iterable[str] = (),
        row_count: int = 0,
        truncated: bool = False,
    ) -> SqlExecution:
        executed_sql = sql if isinstance(sql, str) else repr(sql)
        if visible_sql is None:
            if self.sanitize_prefix_ids:
                executed_sql = self.sanitizer.restore_text(executed_sql)
                visible_sql = self.sanitizer.sanitize_text(executed_sql)
            else:
                visible_sql = executed_sql
        visible_message = self._visible_text(str(message))
        visible_purpose = (
            self._visible_text(purpose.strip())
            if isinstance(purpose, str) and purpose.strip()
            else "(invalid or missing)"
        )
        if isinstance(tasks, list):
            visible_tasks = [
                self._visible_text(task) if isinstance(task, str) else repr(task)
                for task in tasks
            ]
        else:
            visible_tasks = ["(invalid or missing)"]
        elapsed_s = time.monotonic() - started
        markdown = "\n".join(
            (
                "# Raw SQLite tool error",
                "",
                f"**Error:** {visible_message}",
                "",
                "## SQL purpose",
                "",
                visible_purpose,
                "",
                "## SQL tasks",
                "",
                self._fenced(self._json_dump(visible_tasks), "json"),
                "",
                "## Submitted SQL (visible form)",
                "",
                self._fenced(visible_sql, "sql"),
                "",
                "No row payload was returned and no semantic compaction was performed.",
                "",
            )
        )
        return SqlExecution(
            raw_markdown=markdown,
            visible_sql=visible_sql,
            executed_sql=executed_sql,
            columns=[self._visible_text(str(column)) for column in columns],
            row_count=row_count,
            truncated=truncated,
            elapsed_s=elapsed_s,
            sha256=hashlib.sha256(markdown.encode("utf-8")).hexdigest(),
            error=visible_message,
        )

    def _ensure_open(self) -> None:
        if self._closed:
            raise RuntimeError("SQLBackend is closed")

    def close(self) -> None:
        if not self._closed:
            self._connection.set_authorizer(None)
            self._connection.close()
            self._closed = True

    def __enter__(self) -> "SQLBackend":
        self._ensure_open()
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        del exc_type, exc, traceback
        self.close()


__all__ = ["PrefixSanitizer", "SQLBackend", "SqlExecution"]
