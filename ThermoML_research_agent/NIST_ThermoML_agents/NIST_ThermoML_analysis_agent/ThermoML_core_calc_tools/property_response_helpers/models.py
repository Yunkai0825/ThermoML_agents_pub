"""Immutable identity of one authoritative ThermoML reference block."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class CandidateRef:
    doi: str
    lit_num_id: str
    block_number: str
    BLKsubsys_id: str | None
    search_scope: str
    block_type: str
    declared_system_type: str
    effective_system_type: str
    comp_num_ids: tuple[str, ...]
    n_datapoints: int
    declared_quantity_ids: tuple[str, ...] = ()

    @property
    def key(self) -> str:
        parts = [self.lit_num_id, self.block_number]
        if self.BLKsubsys_id is not None:
            parts.append(self.BLKsubsys_id)
        return "::".join(parts)

    def as_dict(self) -> dict[str, Any]:
        return {
            "doi": self.doi,
            "lit_num_id": self.lit_num_id,
            "block_number": self.block_number,
            "BLKsubsys_id": self.BLKsubsys_id,
            "search_scope": self.search_scope,
            "block_type": self.block_type,
            "declared_system_type": self.declared_system_type,
            "effective_system_type": self.effective_system_type,
            "comp_num_ids": list(self.comp_num_ids),
            "n_datapoints": self.n_datapoints,
            "declared_quantity_ids": list(self.declared_quantity_ids),
        }
