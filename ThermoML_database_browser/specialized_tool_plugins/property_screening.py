"""Manifest-driven browser adapter for property-screening runs."""

from __future__ import annotations

import csv
import json
import logging
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .base import PluginManifest, SpecializedToolBrowserPlugin


log = logging.getLogger(__name__)
_RUN_KEY_RE = re.compile(r"^screen_[A-Za-z0-9_.-]+$")


class PropertyScreeningBrowserPlugin(SpecializedToolBrowserPlugin):
    """Read only files explicitly declared by a validated run manifest."""

    manifest = PluginManifest(
        plugin_id="property-screening",
        label="Property screening & ranking",
        description=(
            "Browse canonical regulated-grid profiles, baseline semantics, "
            "rankings, diagnostics, and nested ThermoML evidence."
        ),
        icon="bi-sort-numeric-down",
        capabilities=(
            "run-list",
            "summary",
            "rankings",
            "tables",
            "artifacts",
            "diagnostics",
        ),
    )

    def __init__(self, roots: list[Path] | None = None) -> None:
        source_roots = roots if roots is not None else [
            Path(__file__).resolve().parents[2] / "_output" / "Query",
        ]
        self._roots = [Path(value).resolve() for value in source_roots]

    def _manifest_paths(self) -> list[Path]:
        by_run_id: dict[str, Path] = {}
        patterns = (
            "property_screening_runs/*/run_manifest.json",
            "*/data/property_screening/*/run_manifest.json",
        )
        for root in self._roots:
            if not root.is_dir():
                continue
            for pattern in patterns:
                for path in root.glob(pattern):
                    if not path.is_file():
                        continue
                    manifest = _read_object(path)
                    run_id = manifest.get("run_id")
                    try:
                        _validate_manifest_shape(manifest)
                    except (TypeError, ValueError) as exc:
                        log.warning(
                            "property-screening run hidden from the browser "
                            "(manifest %s): %s", path, exc,
                        )
                        continue
                    if isinstance(run_id, str) and _RUN_KEY_RE.fullmatch(run_id):
                        by_run_id[run_id] = path.resolve()
                    else:
                        log.warning(
                            "property-screening run hidden from the browser "
                            "(manifest %s): run_id %r is not a valid run key",
                            path, run_id,
                        )
        return sorted(
            by_run_id.values(),
            key=lambda path: path.stat().st_mtime,
            reverse=True,
        )

    def _manifest_index(self) -> dict[str, Path]:
        return {
            _read_object(path)["run_id"]: path
            for path in self._manifest_paths()
        }

    def list_runs(self, *, limit: int = 200) -> list[dict[str, Any]]:
        bounded = max(1, min(int(limit), 1000))
        return [
            self._summary(_read_object(path), path)
            for path in self._manifest_paths()[:bounded]
        ]

    def get_run(self, run_key: str) -> dict[str, Any]:
        manifest_path, manifest = self._resolve(run_key)
        request = self._artifact_json(
            manifest_path, manifest, "request"
        )
        ranking = self._artifact_json(
            manifest_path, manifest, "ranking-results-json"
        )
        diagnostics = self._artifact_json(
            manifest_path, manifest, "diagnostics"
        )
        cache_trace = self._artifact_json(
            manifest_path, manifest, "cache-trace"
        )
        result_observer = self._artifact_json(
            manifest_path, manifest, "result-observer"
        )
        assessment = result_observer.get("assessment")
        if not isinstance(assessment, dict):
            raise TypeError("result-observer lacks assessment metadata")
        rankings = ranking.get("rankings")
        if not isinstance(rankings, list):
            raise TypeError("ranking-results-json lacks rankings[]")
        if not isinstance(diagnostics, list):
            raise TypeError("diagnostics artifact must be a list")
        ranking_rows, grid_rows = _flatten_rankings(rankings)

        artifacts: list[dict[str, Any]] = []
        tables: list[dict[str, str]] = []
        for item in manifest["artifacts"]:
            path = self._declared_artifact_path(
                manifest_path, manifest, item["artifact_id"]
            )
            artifacts.append(
                {
                    "artifact_id": item["artifact_id"],
                    "label": item["filename"],
                    "media_type": item["media_type"],
                    "size_bytes": path.stat().st_size,
                    "description": item.get("description", ""),
                }
            )
            if item["media_type"] == "text/csv":
                tables.append(
                    {
                        "table_id": item["artifact_id"],
                        "label": item["filename"],
                    }
                )
        counts = manifest["counts"]
        return {
            "display_contract": self.manifest.display_contract,
            "plugin": self.manifest.to_dict(),
            "run": self._summary(manifest, manifest_path),
            "summary_cards": [
                {
                    "label": "Registry candidates",
                    "value": counts["registry_candidates"],
                    "detail": "Complete paginated discovery",
                },
                {
                    "label": "Curve candidates → selected",
                    "value": (
                        f"{counts['property_curve_candidates']} / "
                        f"{counts['selected_property_curves']}"
                    ),
                    "detail": (
                        "One complete experimental block curve is selected "
                        "before source-local interpolation"
                    ),
                },
                {
                    "label": "Eligible / returned",
                    "value": (
                        f"{counts['eligible_systems']} / "
                        f"{counts['returned_systems']}"
                    ),
                    "detail": "Final limit applies only after ranking",
                },
                {
                    "label": "Diagnostics",
                    "value": counts["diagnostics"],
                    "detail": "Full exclusions and edge-case log",
                },
                {
                    "label": "Result quality review",
                    "value": assessment.get("quality_verdict", "unknown"),
                    "detail": assessment.get("tool_quality_comment", ""),
                },
            ],
            "request": request,
            "cache_trace": cache_trace,
            "result_observer": result_observer,
            "ranking_columns": [
                {"key": "rank", "label": "Rank"},
                {"key": "compounds", "label": "System"},
                {"key": "target", "label": "Target"},
                {"key": "ranking_basis", "label": "Basis"},
                {"key": "raw_value", "label": "Ranking value"},
                {"key": "overall_score", "label": "Overall score"},
                {"key": "quality_score", "label": "Evidence quality"},
                {"key": "source", "label": "Selected curve / block IDs"},
            ],
            "ranking_rows": ranking_rows,
            "grid_columns": [
                {"key": "rank", "label": "Rank"},
                {"key": "compounds", "label": "System"},
                {"key": "target", "label": "Target"},
                {"key": "composition", "label": "Mole-fraction coordinates"},
                {"key": "real_value", "label": "Real"},
                {"key": "ideal_value", "label": "Ideal/reference"},
                {"key": "deviation", "label": "Real − reference"},
                {"key": "baseline_kind", "label": "Reference meaning"},
                {"key": "BLKpoint_ids", "label": "Point evidence"},
            ],
            "grid_rows": grid_rows,
            "diagnostics": diagnostics,
            "artifacts": artifacts,
            "tables": tables,
        }

    def read_table(
        self,
        run_key: str,
        table_id: str,
        *,
        max_rows: int = 10_000,
    ) -> dict[str, Any]:
        manifest_path, manifest = self._resolve(run_key)
        item = _artifact_entry(manifest, table_id)
        if item["media_type"] != "text/csv":
            raise LookupError(f"{table_id!r} is not a declared CSV table")
        path = self._declared_artifact_path(
            manifest_path, manifest, table_id
        )
        bounded = max(1, min(int(max_rows), 50_000))
        with path.open(
            "r", encoding="utf-8-sig", errors="replace", newline=""
        ) as handle:
            reader = csv.reader(handle)
            columns = next(reader, [])
            rows = []
            truncated = False
            for index, row in enumerate(reader):
                if index >= bounded:
                    truncated = True
                    break
                rows.append(row)
        return {
            "table_id": table_id,
            "columns": columns,
            "rows": rows,
            "n_rows": len(rows),
            "truncated": truncated,
        }

    def artifact_path(self, run_key: str, artifact_id: str) -> Path:
        manifest_path, manifest = self._resolve(run_key)
        return self._declared_artifact_path(
            manifest_path, manifest, artifact_id
        )

    def _resolve(self, run_key: str) -> tuple[Path, dict[str, Any]]:
        if not isinstance(run_key, str) or not _RUN_KEY_RE.fullmatch(run_key):
            raise ValueError("invalid property-screening run key")
        path = self._manifest_index().get(run_key)
        if path is None:
            raise FileNotFoundError(run_key)
        manifest = _read_object(path)
        _validate_manifest_shape(manifest)
        return path, manifest

    def _declared_artifact_path(
        self,
        manifest_path: Path,
        manifest: dict[str, Any],
        artifact_id: str,
    ) -> Path:
        item = _artifact_entry(manifest, artifact_id)
        filename = item.get("filename")
        if (
            not isinstance(filename, str)
            or Path(filename).name != filename
            or filename in {"", ".", ".."}
        ):
            raise ValueError("manifest artifact filename is unsafe")
        root = manifest_path.parent.resolve()
        path = (root / filename).resolve()
        if os.path.commonpath((str(root), str(path))) != str(root):
            raise PermissionError("artifact path escapes its run directory")
        if not path.is_file():
            raise FileNotFoundError(path)
        return path

    def _artifact_json(
        self,
        manifest_path: Path,
        manifest: dict[str, Any],
        artifact_id: str,
    ) -> Any:
        path = self._declared_artifact_path(
            manifest_path, manifest, artifact_id
        )
        with path.open("r", encoding="utf-8-sig") as handle:
            return json.load(handle)

    @staticmethod
    def _summary(
        manifest: dict[str, Any], manifest_path: Path
    ) -> dict[str, Any]:
        _validate_manifest_shape(manifest)
        request = manifest["request_summary"]
        counts = manifest["counts"]
        tasks = request["tasks"]
        return {
            "run_key": manifest["run_id"],
            "run_name": manifest["run_id"],
            "modified_utc": datetime.fromtimestamp(
                manifest_path.stat().st_mtime, tz=timezone.utc
            ).isoformat(),
            "status": manifest["status"],
            "centers": [
                {"global_id": value, "label": value}
                for value in request["center_comp_num_ids"]
            ],
            "targets": [
                {"global_id": value, "label": value}
                for value in request["targets"]
            ],
            "constraints": [
                {"global_id": value, "label": value}
                for value in request["constraints"]
            ],
            "composition_grid": [],
            "n_returned": counts["returned_systems"],
            "n_eligible_candidates": counts["eligible_systems"],
            "n_incomplete_candidates": counts["incomplete_systems"],
            "n_diagnostics": counts["diagnostics"],
            "purpose": request["purpose"],
            "tasks": ", ".join(tasks),
            "system_scope": request["system_scope"],
            "system_type": request["system_type"],
        }


def _validate_manifest_shape(manifest: dict[str, Any]) -> None:
    if "schema" in manifest:
        raise ValueError("property-screening manifests must not use schema markers")
    if not isinstance(manifest.get("request_summary"), dict):
        raise TypeError("manifest request_summary must be an object")
    if not isinstance(manifest.get("counts"), dict):
        raise TypeError("manifest counts must be an object")
    if not isinstance(manifest.get("artifacts"), list):
        raise TypeError("manifest artifacts must be a list")
    if any(
        isinstance(item, dict) and "schema" in item
        for item in manifest["artifacts"]
    ):
        raise ValueError("property-screening artifacts must not use schema markers")
    request_keys = {
        "center_comp_num_ids",
        "targets",
        "constraints",
        "system_scope",
        "system_type",
        "purpose",
        "tasks",
    }
    count_keys = {
        "registry_candidates",
        "materialized_target_sources",
        "property_curve_candidates",
        "selected_property_curves",
        "eligible_systems",
        "incomplete_systems",
        "returned_systems",
        "diagnostics",
    }
    missing_request = request_keys - set(manifest["request_summary"])
    missing_counts = count_keys - set(manifest["counts"])
    if missing_request or missing_counts:
        raise ValueError(
            "incomplete property-screening manifest: "
            f"request={sorted(missing_request)}, counts={sorted(missing_counts)}"
        )


def _read_object(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise TypeError(f"{path} must contain a JSON object")
    return value


def _artifact_entry(
    manifest: dict[str, Any], artifact_id: str
) -> dict[str, Any]:
    matches = [
        item
        for item in manifest["artifacts"]
        if isinstance(item, dict) and item.get("artifact_id") == artifact_id
    ]
    if len(matches) != 1:
        raise LookupError(
            f"artifact {artifact_id!r} is not declared exactly once"
        )
    return matches[0]


def _flatten_rankings(
    rankings: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    ranking_rows: list[dict[str, Any]] = []
    grid_rows: list[dict[str, Any]] = []
    for ranking in rankings:
        compounds = " + ".join(ranking["compound_names"])
        for criterion in ranking["criteria"]:
            target = criterion["target"]
            source = criterion["source"]
            curve_id = source.get("selected_curve_id")
            doi = source.get("doi")
            lit_num_id = source.get("lit_num_id")
            if not curve_id or not doi or not lit_num_id:
                raise ValueError(
                    "ranking criterion must identify its selected curve and "
                    "paired DOI/lit_num_id source"
                )
            source_text = (
                f"{curve_id}: {lit_num_id} ({doi}) / "
                f"{source.get('block_number')}"
            )
            if source.get("BLKsubsys_id"):
                source_text += f" / {source['BLKsubsys_id']}"
            if source.get("target_local_id"):
                source_text += f" / {source['target_local_id']}"
            ranking_rows.append(
                {
                    "rank": ranking["rank"],
                    "candidate_key": ranking["candidate_key"],
                    "system_signature": ranking["system_signature"],
                    "compounds": compounds,
                    "target": target["quantity_key"],
                    "ranking_basis": target["basis"],
                    "raw_value": criterion["raw_value"],
                    "overall_score": ranking["overall_score"],
                    "quality_score": ranking["quality_score"],
                    "source": source_text,
                }
            )
            for point in criterion["grid_values"]:
                grid_rows.append(
                    {
                        "rank": ranking["rank"],
                        "candidate_key": ranking["candidate_key"],
                        "system_signature": ranking["system_signature"],
                        "compounds": compounds,
                        "target": target["quantity_key"],
                        "composition": point["composition"],
                        "real_value": point["real_value"],
                        "ideal_value": point["ideal_value"],
                        "deviation": point["deviation"],
                        "absolute_deviation": point["absolute_deviation"],
                        "baseline_kind": point["baseline_kind"],
                        "BLKpoint_ids": point["source_point_ids"],
                    }
                )
    return ranking_rows, grid_rows
