"""
Working memory for the ThermoML Main Agent.
============================================
Tracks subagent delegation results (query and analysis agent calls)
and merges their key findings into a unified state.

Lighter than the analysis agent's working memory — no block-level
metadata extraction since the main agent never touches raw data.

Includes a **hardcoded markdown parser** that can reconstruct the
ID Catalog and History sections from a persisted ``_working_memory.md``
file, allowing state recovery after restarts.
"""
from __future__ import annotations

import logging
import re
from typing import TYPE_CHECKING

from ....general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers import session_manager_output_storage
from ....general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers.general_memory_hooks import (
    BaseWorkingMemory,
)
from ....general_db_query_engine.general_hooks_management_helpers.general_memory_management_tools_hooks_helpers.envelope_memory_digest import (
    digest_with_validation,
)

if TYPE_CHECKING:
    from pathlib import Path

log = logging.getLogger("MAIN-WM")

# ── Hardcoded markdown parsers ───────────────────────────────

# Matches a strict catalog row: | type | GLOBtype_N | registry_id | name text |
_CATALOG_ROW_RE = re.compile(
    r"^\|\s*(?P<type>\w+)\s*\|\s*(?P<global_id>GLOB[A-Za-z]+_[1-9]\d*)\s*\|\s*(?P<registry_id>\S+)\s*\|\s*(?P<name>.+?)\s*\|$",
    re.MULTILINE,
)
# Matches a history bullet:  - text
_HISTORY_LINE_RE = re.compile(r"^- (.+)$", re.MULTILINE)

# Section header (## Title)
_SECTION_RE = re.compile(r"^## (.+)$", re.MULTILINE)
def _extract_section(text: str, section_name: str) -> str:
    """Return the body text between ``## section_name`` and the next ``##``."""
    headers = list(_SECTION_RE.finditer(text))
    for i, m in enumerate(headers):
        if m.group(1).strip() == section_name:
            start = m.end() + 1
            end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
            return text[start:end]
    return ""


def parse_id_catalog(text: str) -> list[dict]:
    """Parse ID Catalog rows from markdown text.

    Returns strict ``{type, global_id, registry_id, name}`` dictionaries.
    """
    section = _extract_section(text, "ID Catalog")
    rows: list[dict] = []
    for m in _CATALOG_ROW_RE.finditer(section):
        rows.append(m.groupdict())
    return rows


def parse_history(text: str) -> list[str]:
    """Parse History bullet lines from markdown text."""
    section = _extract_section(text, "History")
    return [m.group(1) for m in _HISTORY_LINE_RE.finditer(section)]


class MainWorkingMemory(BaseWorkingMemory):
    """Main agent working memory — tracks subagent call results."""

    def __init__(self):
        super().__init__()
        self.query_results: list[dict] = []       # [{agent, answer_summary, ...}]
        self.analysis_results: list[dict] = []    # [{agent, answer, verdict, ...}]
        self.parallel_compactions: list[dict] = []  # [{philosophy, reports}]
        self.history: list[str] = []              # append-only action log

    # ── History helpers ──────────────────────────────────────

    def append_history(self, line: str) -> None:
        """Append a one-line entry to the in-memory history log."""
        self.history.append(line)
        self.sync_to_disk()

    # ── Hardcoded recovery from persisted markdown ───────────

    def load_from_markdown(self, text: str) -> None:
        """Reconstruct ID Catalog and History from a working-memory markdown.

        This is the "hardcoded parser" — it reads the structured markdown
        sections and populates ``self._catalog`` and ``self.history``
        without relying on LLM parsing.
        """
        # ── ID Catalog ──
        for row in parse_id_catalog(text):
            etype = row["type"]
            global_id = row.get("global_id")
            name = row.get("name", "")
            registry_id = row.get("registry_id", "")
            if etype and global_id and name and registry_id:
                self.add_entity(
                    etype, name.strip(), global_id, registry_id=registry_id
                )

        # ── History ──
        for line in parse_history(text):
            if line not in self.history:
                self.history.append(line)

    # ── Private helpers for recording individual subagent results ──

    @staticmethod
    def _sid_table_label(tool_name: str, r: dict) -> str:
        """Cross-surface table label from the OUTER envelope (it carries
        ``_session_dir``; the inner answer JSON handed to the digest does
        not).  "" → the digest falls back to the storage-key label."""
        try:
            from ....general_db_query_engine.general_argo_engine_helpers.engine_react_helpers.subagent_context_render import (
                resolve_sid_label,
            )
            return resolve_sid_label(tool_name, r)
        except Exception:
            return ""

    def _record_query(self, r: dict, label: str = "") -> str:
        """Ingest a single query result and return a history snippet."""
        answer = r.get("answer", "")
        q_text = r.get("_question", "")[:80]
        elapsed = r.get("elapsed_seconds", 0.0)
        iters = r.get("iterations", 0)
        timed_out = r.get("timed_out", False)
        lbl = label or r.get("label", f"Q{len(self.query_results)+1}")
        validation = "UNPARSED"
        try:
            answer, validation = digest_with_validation(
                answer, key=lbl, tool_name="run_query_agent", pair="main/Qi",
                label=self._sid_table_label("run_query_agent", r))
        except ValueError:
            pass    # free-text / error answers are stored as-is

        self.query_results.append({
            "tool": "run_query_agent",
            "label": lbl,
            "answer_summary": answer,
            "validation": validation,
            "verdict": r.get("verdict"),
            "iterations": iters,
            "elapsed_seconds": elapsed,
            "timed_out": timed_out,
        })

        tag = " TIMED-OUT" if timed_out else ""
        verdict_tag = f" verdict={r.get('verdict', 'none')[:30]}" if r.get("verdict") else ""
        return (
            f"[query:{lbl}]{tag} \"{q_text}\" ({elapsed:.0f}s, {iters} iters, "
            f"validation={validation}{verdict_tag})"
        )

    def _record_analysis(self, r: dict, label: str = "") -> str:
        """Ingest a single analysis result and return a history snippet."""
        answer = r.get("answer", "")
        q_text = r.get("_question", "")[:80]
        elapsed = r.get("elapsed_seconds", 0.0)
        iters = r.get("iterations", 0)
        timed_out = r.get("timed_out", False)
        lbl = label or r.get("label", f"A{len(self.analysis_results)+1}")
        validation = "UNPARSED"
        try:
            answer, validation = digest_with_validation(
                answer, key=lbl, tool_name="run_analysis_agent", pair="main/Ai",
                label=self._sid_table_label("run_analysis_agent", r))
        except ValueError:
            pass    # free-text / error answers are stored as-is

        self.analysis_results.append({
            "tool": "run_analysis_agent",
            "label": lbl,
            "answer_summary": answer,
            "validation": validation,
            "verdict": r.get("verdict"),
            "iterations": iters,
            "elapsed_seconds": elapsed,
            "timed_out": timed_out,
            "session_dir": r.get("session_dir"),
            "n_output_files": len(r.get("output_files", [])),
        })

        tag = " TIMED-OUT" if timed_out else ""
        verdict_tag = f" verdict={r.get('verdict', 'none')[:30]}" if r.get("verdict") else ""
        return (
            f"[analysis:{lbl}]{tag} \"{q_text}\" ({elapsed:.0f}s, {iters} iters, "
            f"validation={validation}{verdict_tag})"
        )

    def record_tool_result(self, tool_name: str, result: dict):
        """Store key information from subagent tool calls."""
        history_lines: list[str] = []

        if tool_name == "run_query_agent":
            history_lines.append(self._record_query(result))

        elif tool_name == "run_analysis_agent":
            history_lines.append(self._record_analysis(result))

        elif tool_name == "run_parallel_subagents":
            n_tasks = result.get("n_tasks", 0)
            for r in result.get("results", []):
                if not isinstance(r, dict):
                    continue
                agent = r.get("agent", "query")
                lbl = r.get("label", "")
                if agent == "analysis":
                    history_lines.append(self._record_analysis(r, label=lbl))
                else:
                    history_lines.append(self._record_query(r, label=lbl))
            # Wrap parallel entries in a group header
            if history_lines:
                header = f"[parallel:{n_tasks} tasks]"
                history_lines = [header] + [f"  {l}" for l in history_lines]
            # Automated two-stage compaction (oversized batches) records
            # its philosophy and per-task reports alongside the batch.
            auto = result.get("_auto_compaction")
            if isinstance(auto, dict) and auto.get("per_task_reports"):
                self.parallel_compactions.append({
                    "philosophy": auto.get("philosophy", ""),
                    "philosophy_source": auto.get("philosophy_source", ""),
                    "compaction": auto.get("compaction", ""),
                    "targets": auto.get("targets", ""),
                    "correction_rounds": auto.get("correction_rounds", 0),
                    "reports": dict(auto["per_task_reports"]),
                })
                history_lines.append(
                    f"[parallel:auto-compacted] {len(auto['per_task_reports'])} "
                    f"per-task reports ({auto.get('compaction', '?')}, "
                    f"targets {auto.get('targets', '?')}, "
                    f"philosophy {auto.get('philosophy_source', '?')})"
                )

        elif tool_name == "browse_subagent_tools":
            # Lightweight trace — no heavy data to record
            path = "(root)" if not result else str(result)[:60]
            history_lines.append(f"[menu:browse] {path}")

        elif tool_name == "run_subagent_tool":
            menu_tool = result.get("_menu_tool", "?")
            err = result.get("error")
            if err:
                history_lines.append(f"[menu:run] {menu_tool} → ERROR: {err[:80]}")
            else:
                history_lines.append(f"[menu:run] {menu_tool} → OK")

        if history_lines:
            self.history.extend(history_lines)

        self.sync_to_disk()

    def sync_to_disk(self):
        """Persist working memory to _working_memory.md in the session dir."""
        sess = session_manager_output_storage.get_session()
        if not sess:
            return
        content = self.render()
        if not content:
            return
        try:
            wm_path = sess.session_dir / "_working_memory.md"
            session_manager_output_storage._filesystem_path(wm_path).write_text(
                f"# Working Memory\n\n{content}\n", encoding="utf-8",
            )
        except Exception as exc:
            log.warning("sync_to_disk failed: %s", exc, exc_info=True)

    def render(self) -> str:
        """Render working memory as a text block for the LLM."""
        parts = []

        sess = session_manager_output_storage.get_session()
        root = str(sess.session_dir) if sess else None
        if root:
            parts.append(f"**ROOT:** `{root}`")

        # ── ID Catalog (from base class) ──
        catalog = self.render_id_catalog()
        if catalog:
            parts.append(catalog)

        # ── History ──
        if self.history:
            lines = "\n".join(f"- {h}" for h in self.history)
            parts.append(f"### History\n{lines}")

        # ── Query Agent Results ──
        if self.query_results:
            qr_lines = ["### Query Agent Results"]
            for i, q in enumerate(self.query_results):
                label = q.get("label", f"Q{i+1}")
                summary = q.get("answer_summary", "")
                timed_out = q.get("timed_out", False)
                status = " (TIMED OUT)" if timed_out else ""
                qr_lines.append(f"\n#### {label}{status}\n{summary}")
            parts.append("\n".join(qr_lines))

        # ── Analysis Agent Results ──
        if self.analysis_results:
            ar_lines = ["### Analysis Agent Results"]
            for i, a in enumerate(self.analysis_results):
                label = a.get("label", f"A{i+1}")
                summary = a.get("answer_summary", "")
                verdict = a.get("verdict")
                timed_out = a.get("timed_out", False)
                status = " (TIMED OUT)" if timed_out else ""
                ar_lines.append(f"\n#### {label}{status}\n{summary}")
                if verdict:
                    ar_lines.append(f"\n**Verdict:** {verdict}")
                sd = a.get("session_dir")
                if sd:
                    ar_lines.append(f"**Session:** `{sd}`")
            parts.append("\n".join(ar_lines))

        # ── Philosophy-guided parallel compactions ──
        if self.parallel_compactions:
            pc_lines = ["### Parallel Compaction Reports"]
            for i, pc in enumerate(self.parallel_compactions, 1):
                pc_lines.append(f"\n#### Compaction {i}")
                src = pc.get("philosophy_source", "")
                mode = pc.get("compaction", "")
                tgt = pc.get("targets", "")
                bits = [b for b in (mode, f"targets {tgt}" if tgt else "",
                                    f"philosophy {src}" if src else "") if b]
                tag = f" ({', '.join(bits)})" if bits else ""
                pc_lines.append(f"**Philosophy{tag}:** {pc.get('philosophy', '')}")
                for label, report in pc.get("reports", {}).items():
                    pc_lines.append(f"\n##### [{label}]\n{report}")
            parts.append("\n".join(pc_lines))

        return "\n\n".join(parts)
