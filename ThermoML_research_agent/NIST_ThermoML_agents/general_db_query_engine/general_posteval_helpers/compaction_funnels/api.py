"""Public API — per-session workflow artifact generation.

One call generates EVERYTHING for ONE agent session (a Main
orchestrator run, or a standalone query / analysis agent run) into a
``workflow/`` folder inside that session's run directory: the canonical
detailed skeleton (delegation-tree scoped, chars+ids on every node)
projected to chars/ids/blocks/pts at detailed/agentic/pooled levels,
per-agent sub_ figures, session views, edge + node TSVs (with full id
lists, dispatch args and artifact provenance), and the registry-driven
audit report.  Sessions without exhaustive breadcrumb logs are refused
(WorkflowReport.error mentions "legacy").

Typical use::

    from NIST_ThermoML_agents.general_db_query_engine.\
        general_posteval_helpers.compaction_funnels.api import (
            generate_workflow)

    report = generate_workflow(run_dir)            # kind auto-detected
    report = generate_workflow(run_dir, kind="analysis")

Engine wiring uses :func:`maybe_generate_workflow` to generate artifacts
after every root session. Child runs are included in their root workflow;
figure-generation failures never raise into the agent caller.
"""

from __future__ import annotations

import sys
import threading
import time
import traceback
from dataclasses import dataclass, field
from pathlib import Path

_PACKAGE_ROOT = Path(__file__).resolve().parent
if str(_PACKAGE_ROOT) not in sys.path:  # self-root (mirrors __init__)
    sys.path.insert(0, str(_PACKAGE_ROOT))

WORKFLOW_DIRNAME = "workflow"

# one generation at a time: the flat output re-route and the parse/
# evidence caches are process-global (browser agent threads share them)
_GENERATION_LOCK = threading.Lock()

# run directories whose parent marks them as children of a bigger session
_CHILD_MARKERS = ("query_runs", "analysis_runs")
_KIND_FOLDERS = {"main": "main", "query": "query", "analysis": "analysis"}


@dataclass
class WorkflowReport:
    """What one generation pass produced."""
    session: Path
    kind: str
    label: str
    out_dir: Path
    outputs: list[Path] = field(default_factory=list)
    audit_findings: int = 0
    audit_failures: int = 0
    elapsed_seconds: float = 0.0
    error: str = ""

    @property
    def ok(self) -> bool:
        return not self.error


def session_kind(session_dir: Path) -> str:
    """Detect what agent produced ``session_dir``.

    The exhaustive history's own Nest breadcrumb is authoritative
    (last token: main / Q_n / A_n); folder-name and artifact heuristics
    remain as fallbacks.
    """
    session_dir = Path(session_dir)
    history = session_dir / "run_history.md"
    if history.exists():
        import re
        head = history.read_text(encoding="utf-8", errors="replace")[:2000]
        m = re.search(r"^\*\*Nest:\*\*\s*(.+)$", head, re.M)
        if m:
            last = m.group(1).split(" - ")[-1].strip()
            if last == "main":
                return "main"
            if last.startswith("Q"):
                return "query"
            if last.startswith("A"):
                return "analysis"
    for ancestor in [session_dir, *session_dir.parents]:
        name = ancestor.name.lower()
        if name in _KIND_FOLDERS:
            return _KIND_FOLDERS[name]
        if name in _CHILD_MARKERS:
            break
    if (session_dir / "working_memory.md").exists():
        return "query"
    if (session_dir / "analysis_runs").exists() and (
            session_dir / "query_runs").exists():
        return "main"
    raise ValueError(
        f"cannot detect agent kind for {session_dir}; pass kind= explicitly")


def session_label(session_dir: Path, kind: str) -> str:
    """Stable, short prompt label for figures/TSV `case` columns."""
    name = Path(session_dir).name
    parts = name.split("_")
    stamp = "_".join(parts[1:3]) if parts[0] == "run" and len(parts) >= 3 else name
    return f"{kind.capitalize()} {stamp}"


def generate_workflow(session_dir: Path | str,
                      kind: str = "auto",
                      label: str | None = None,
                      out_dir: Path | str | None = None,
                      settings=None,
                      audit: bool = True) -> WorkflowReport:
    """Generate ALL workflow artifacts for one session run directory.

    kind: "main" | "query" | "analysis" | "auto".
    out_dir: defaults to ``<session_dir>/workflow/``.
    audit: also run the registry audits (conservation, adjacency,
    coverage, envelope partition) and write
    ``registry_audit_report.tsv`` into the workflow folder.
    """
    started = time.time()
    session_dir = Path(session_dir)
    if not session_dir.exists():
        raise FileNotFoundError(f"session directory not found: {session_dir}")
    if kind == "auto":
        kind = session_kind(session_dir)
    if kind not in _KIND_FOLDERS:
        raise ValueError(f"unknown session kind {kind!r}")
    label = label or session_label(session_dir, kind)
    out_path = Path(out_dir) if out_dir else session_dir / WORKFLOW_DIRNAME
    report = WorkflowReport(session_dir, kind, label, out_path)

    from funnel_evidence.history_evidence import LegacySessionError

    with _GENERATION_LOCK:
        try:
            from funnel_assembly.build import build_all
            result = build_all(session_dir, kind, label, out_path)
        except LegacySessionError as exc:
            report.error = f"legacy session not supported: {exc}"
            report.elapsed_seconds = time.time() - started
            return report
        report.outputs = list(result["outputs"])

    if audit:
        from workflow_audits.registry_audits import run_audits, write_report
        findings = run_audits(result)
        report.outputs.append(write_report(
            findings, out_path / "registry_audit_report.tsv"))
        report.audit_findings = len(findings)
        report.audit_failures = sum(1 for f in findings
                                    if f.severity == "FAIL")
    report.elapsed_seconds = time.time() - started
    return report


def generate_workflows(sessions, **kwargs) -> list[WorkflowReport]:
    """Prompt-major batch: finish one session's artifacts, then move on.

    ``sessions``: iterable of session dirs or (session_dir, kind) pairs.
    """
    reports = []
    for entry in sessions:
        session, kind = (entry if isinstance(entry, (tuple, list))
                         else (entry, "auto"))
        reports.append(generate_workflow(session, kind=kind, **kwargs))
    return reports


def is_root_session(session_dir: Path | str) -> bool:
    """True when the run is NOT a saved child of a bigger session (child
    runs are covered by their root session's workflow generation)."""
    return Path(session_dir).parent.name not in _CHILD_MARKERS


def maybe_generate_workflow(session_dir: Path | str,
                            kind: str = "auto") -> WorkflowReport | None:
    """Engine seam: generate workflow artifacts at session end.

    Child sessions are covered by their root; never raises — a figure
    generation failure must not fail the agent run that produced the
    session.  Returns the report (with .error set on failure) or None
    when skipped.
    """
    try:
        if not is_root_session(session_dir):
            return None
        print(f"[workflow] generating compaction workflow artifacts for "
              f"{session_dir} ...", flush=True)
        report = generate_workflow(session_dir, kind=kind)
        print(f"[workflow] wrote {len(report.outputs)} artifacts to "
              f"{report.out_dir} in {report.elapsed_seconds:.0f}s "
              f"(audit: {report.audit_failures} FAIL / "
              f"{report.audit_findings} findings)", flush=True)
        return report
    except Exception as exc:  # noqa: BLE001 — post-run best effort
        print(f"[workflow] generation failed for {session_dir}: {exc}",
              flush=True)
        traceback.print_exc()
        report = WorkflowReport(Path(session_dir), kind, "", Path(session_dir)
                                / WORKFLOW_DIRNAME)
        report.error = str(exc)
        return report
