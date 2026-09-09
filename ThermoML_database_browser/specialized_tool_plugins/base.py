"""Stable contract between specialized pipelines and the web browser."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class PluginManifest:
    """Metadata needed to render and route one specialized-tool browser."""

    plugin_id: str
    label: str
    description: str
    icon: str = "bi-puzzle"
    display_contract: str = "tabular-run-v1"
    capabilities: tuple[str, ...] = (
        "run-list",
        "summary",
        "tables",
        "artifacts",
    )

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["capabilities"] = list(self.capabilities)
        return payload


class SpecializedToolBrowserPlugin(ABC):
    """Read-only adapter implemented by every browsable specialized tool.

    A new pipeline implements these four operations and registers one instance
    in :func:`build_default_registry`.  Browser routes, navigation, filtering,
    and the table/plot UI then work without pipeline-specific Flask code.
    """

    manifest: PluginManifest

    @abstractmethod
    def list_runs(self, *, limit: int = 200) -> list[dict[str, Any]]:
        """Return newest-first normalized run summaries."""

    @abstractmethod
    def get_run(self, run_key: str) -> dict[str, Any]:
        """Return one normalized ``tabular-run-v1`` detail payload."""

    @abstractmethod
    def read_table(
        self, run_key: str, table_id: str, *, max_rows: int = 10_000
    ) -> dict[str, Any]:
        """Read one declared tabular artifact without arbitrary file access."""

    @abstractmethod
    def artifact_path(self, run_key: str, artifact_id: str) -> Path:
        """Resolve one declared downloadable artifact under the plugin root."""
