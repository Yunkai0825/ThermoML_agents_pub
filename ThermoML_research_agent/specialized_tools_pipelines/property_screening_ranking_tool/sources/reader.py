"""Read PCS declarations and every authoritative raw ThermoML point.

PCS ``data_points`` are display samples capped for compact cards.  Numerical
screening must therefore join PCS metadata to ``thermoml_raw.db`` and read the
complete ``NumValues`` array, exactly as ``extract_block_csv`` does.
"""

from __future__ import annotations

import json
import math
from collections import OrderedDict
from dataclasses import dataclass
from typing import Any

from card_db_search_tools.basic_search_tools.advanced_block_search.catalogs import (
    PCS_DB,
    open_raw_db,
)
from card_db_search_tools.basic_search_tools.normalization_helpers.db_helpers import (
    open_db,
    project_pcs_block_target,
)
from ThermoML_raw_json_to_card_db_parsers.id_schema import block_local_id

from ..interface import CandidateRef, Diagnostic


@dataclass
class AuthoritativeBlock:
    candidate: CandidateRef
    key: dict[str, Any]
    block: dict[str, Any]
    projected: dict[str, Any]
    subsystem: dict[str, Any] | None
    rows: list[dict[str, float | str | None]]
    units_aligned: bool
    unit_alignment: tuple[dict[str, Any], ...]


@dataclass
class BlockGatheringResult:
    blocks: list[AuthoritativeBlock]
    diagnostics: list[Diagnostic]


class AuthoritativeBlockReader:
    """Connection-reusing reader with a deliberately small DOI cache."""

    def __init__(self, *, cache_size: int = 4) -> None:
        self._pcs = open_db(str(PCS_DB))
        self._raw = open_raw_db()
        self._cache_size = max(1, int(cache_size))
        self._cards: OrderedDict[str, dict[str, Any]] = OrderedDict()
        self._papers: OrderedDict[str, dict[str, Any]] = OrderedDict()

    def __enter__(self) -> "AuthoritativeBlockReader":
        return self

    def __exit__(self, *_exc: object) -> None:
        self.close()

    def close(self) -> None:
        self._pcs.close()
        self._raw.close()
        self._cards.clear()
        self._papers.clear()

    def _cached_json(
        self,
        cache: OrderedDict[str, dict[str, Any]],
        connection,
        table: str,
        doi: str,
    ) -> dict[str, Any]:
        value = cache.pop(doi, None)
        if value is not None:
            cache[doi] = value
            return value
        row = connection.execute(
            f"SELECT json_data FROM {table} WHERE doi=?", (doi,)
        ).fetchone()
        if row is None:
            raise LookupError(f"{doi!r} not found in {table}")
        value = json.loads(row["json_data"])
        if not isinstance(value, dict):
            raise TypeError(f"{table} row for {doi!r} is not an object")
        cache[doi] = value
        while len(cache) > self._cache_size:
            cache.popitem(last=False)
        return value

    def read(self, candidate: CandidateRef) -> AuthoritativeBlock:
        card = self._cached_json(
            self._cards, self._pcs, "cards", candidate.doi
        )
        paper = self._cached_json(
            self._papers, self._raw, "papers", candidate.doi
        )
        key = card.get("key")
        if not isinstance(key, dict):
            raise ValueError("PCS card key is missing")
        if key.get("lit_num_id") != candidate.lit_num_id:
            raise ValueError(
                f"DOI/literature mismatch for {candidate.doi}: "
                f"{key.get('lit_num_id')!r} != {candidate.lit_num_id!r}"
            )
        block = next(
            (
                item
                for item in card.get("blocks", [])
                if isinstance(item, dict)
                and item.get("block_number") == candidate.block_number
            ),
            None,
        )
        if block is None:
            raise LookupError(
                f"{candidate.doi} lacks {candidate.block_number}"
            )
        subsystem = self._resolve_subsystem(card, candidate)
        projected = project_pcs_block_target(block, subsystem)
        raw_block = self._raw_block(paper, candidate.block_number)
        raw_points = raw_block.get("NumValues")
        if not isinstance(raw_points, list):
            raise ValueError("raw block NumValues must be an array")
        declared_count = int(block["data_summary"]["n_points"])
        if len(raw_points) != declared_count:
            raise ValueError(
                f"raw/PCS row-count mismatch for {candidate.key}: "
                f"{len(raw_points)} != {declared_count}"
            )
        selected = self._selected_ordinals(subsystem, len(raw_points))
        rows = [
            self._point_row(point, ordinal, projected)
            for ordinal, point in enumerate(raw_points, start=1)
            if selected is None or ordinal in selected
        ]
        if len(rows) != candidate.n_datapoints:
            raise ValueError(
                f"candidate row-count mismatch for {candidate.key}: "
                f"{len(rows)} != {candidate.n_datapoints}"
            )
        return AuthoritativeBlock(
            candidate=candidate,
            key=key,
            block=block,
            projected=projected,
            subsystem=subsystem,
            rows=rows,
            units_aligned=False,
            unit_alignment=(),
        )

    @staticmethod
    def _resolve_subsystem(
        card: dict[str, Any], candidate: CandidateRef
    ) -> dict[str, Any] | None:
        if candidate.BLKsubsys_id is None:
            return None
        manifests = (
            card["blocks_summary"]["derived_indexes"][
                "composition_subsystems"
            ][candidate.block_number]
        )
        matches = [
            item
            for item in manifests
            if item.get("BLKsubsys_id") == candidate.BLKsubsys_id
        ]
        if len(matches) != 1:
            raise ValueError(
                f"{candidate.BLKsubsys_id} does not resolve uniquely in "
                f"{candidate.doi}/{candidate.block_number}"
            )
        return matches[0]

    @staticmethod
    def _raw_block(
        paper: dict[str, Any], block_number: str
    ) -> dict[str, Any]:
        prefix, ordinal_text = block_number.rsplit("_", 1)
        if prefix == "PROPblock":
            family = "PureOrMixtureData"
            number_field = "nPureOrMixtureDataNumber"
        elif prefix == "RXNblock":
            family = "ReactionData"
            number_field = "nReactionDataNumber"
        else:
            raise ValueError(f"unsupported typed block {block_number!r}")
        ordinal = int(ordinal_text)
        matches = [
            item
            for item in paper.get(family, [])
            if isinstance(item, dict) and item.get(number_field) == ordinal
        ]
        if len(matches) != 1:
            raise ValueError(
                f"raw paper resolves {len(matches)} {block_number!r} blocks"
            )
        return matches[0]

    @staticmethod
    def _selected_ordinals(
        subsystem: dict[str, Any] | None, n_points: int
    ) -> set[int] | None:
        if subsystem is None:
            return None
        selected: set[int] = set()
        for run in subsystem["point_membership"]["runs"]:
            if (
                not isinstance(run, list)
                or len(run) != 2
                or not all(isinstance(value, int) for value in run)
            ):
                raise ValueError("subsystem point runs must be [start,end]")
            start, end = run
            if start < 1 or end < start or end > n_points:
                raise ValueError(f"invalid subsystem point run {run!r}")
            selected.update(range(start, end + 1))
        if len(selected) != int(subsystem["n_points"]):
            raise ValueError("subsystem point membership count is incoherent")
        return selected

    @staticmethod
    def _point_row(
        raw_point: Any,
        ordinal: int,
        projected: dict[str, Any],
    ) -> dict[str, float | str | None]:
        if not isinstance(raw_point, dict):
            raise TypeError("raw NumValues entry must be an object")
        row: dict[str, float | str | None] = {
            "BLKpoint_id": block_local_id("point", ordinal)
        }
        for section, collection, number_field, value_field, local_field in (
            (
                "variables",
                "VariableValue",
                "nVarNumber",
                "nVarValue",
                "BLKvar_id",
            ),
            (
                "properties",
                "PropertyValue",
                "nPropNumber",
                "nPropValue",
                "BLKprop_id",
            ),
        ):
            items = raw_point.get(collection, [])
            if not isinstance(items, list):
                raise TypeError(f"raw {collection} must be an array")
            by_number = {
                item[number_field]: item
                for item in items
                if isinstance(item, dict) and number_field in item
            }
            for declaration in projected[section]:
                local_id = declaration[local_field]
                number = int(local_id.rsplit("_", 1)[1])
                item = by_number.get(number)
                raw_value = item.get(value_field) if item is not None else None
                row[local_id] = _finite_float(raw_value)
        for declaration in projected["constraints"]:
            row[declaration["BLKconstr_id"]] = _finite_float(
                declaration.get("value")
            )
        return row


def _finite_float(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if math.isfinite(number) else None


def gather_authoritative_blocks(
    candidates: tuple[CandidateRef, ...],
) -> BlockGatheringResult:
    """Read every discovered block once before downstream chemistry stages."""
    blocks: list[AuthoritativeBlock] = []
    diagnostics: list[Diagnostic] = []
    with AuthoritativeBlockReader() as reader:
        for candidate in candidates:
            try:
                blocks.append(reader.read(candidate))
            except Exception as exc:
                diagnostics.append(
                    Diagnostic(
                        code="AUTHORITATIVE_BLOCK_GATHERING_FAILED",
                        message=f"{type(exc).__name__}: {exc}",
                        stage="authoritative_block_gathering",
                        severity="warning",
                        source_key=candidate.key,
                    )
                )
    return BlockGatheringResult(blocks=blocks, diagnostics=diagnostics)
