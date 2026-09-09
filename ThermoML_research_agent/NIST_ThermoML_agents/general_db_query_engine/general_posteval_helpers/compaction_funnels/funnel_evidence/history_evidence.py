"""Exhaustive run_history.md parsing (new-format sessions ONLY).

A session qualifies when its run_history.md carries the "**Nest:**"
breadcrumb header — anything else raises ``LegacySessionError`` (the
funnels no longer support pre-breadcrumb logs).

Yields per session:
- steps: every tool call with breadcrumb tokens, seq (cN), args,
  delivered result text (verbatim), timing.
- pipeline rows: "## Tool Compaction Pipeline" table —
  Native/Hardcoded/Agentic chars + verdict + owning section.
- subagent rows: "## Subagent Summary" triage events.
- sections: "## Nested tool calls — {sid} ({label})" inventory.
- errors: "## Errors" entries.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path


class LegacySessionError(RuntimeError):
    """Session lacks the exhaustive breadcrumb history."""


NEST_RE = re.compile(r"^\*\*Nest:\*\*\s*(.+)$", re.M)
STEP_RE = re.compile(
    r"^### Step (\d+)(?: \[([^\]]+)\])?: `(.+?)`(.*?)(?=^### Step |^## |\Z)",
    re.M | re.S,
)
SEQ_TAG_RE = re.compile(r"\bc(\d+)\s*$")
ARGS_RE = re.compile(r"```json\n(.*?)\n```", re.S)
RESULT_DETAILS_RE = re.compile(
    r"<details><summary>Result</summary>\s*(.*?)</details>", re.S)
RESULT_LINE_RE = re.compile(
    r"\*\*Result:\*\*\s*([\d,]+) chars(?:\s*\|\s*\*\*Time:\*\*\s*([\d.]+)s)?"
    r"(?:\s*\|\s*\*\*Started:\*\*\s*([\d:]+)\s*\(t\+([\d.]+)s\))?")
NESTED_LINE_RE = re.compile(r"\*\*Nested:\*\*[^\n]*?section '([^']+)'")
ERROR_LINE_RE = re.compile(r"\*\*Error", re.I)
SECTION_HEAD_RE = re.compile(
    r"^## Nested tool calls \u2014 (\S+) \(([^)]*)\)", re.M)
PIPELINE_HEAD_RE = re.compile(r"^## Tool Compaction Pipeline", re.M)
PIPELINE_ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*(\w+)\s*\|\s*([\d,]+)\s*\|"
    r"\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*(\w+)\s*\|[^|]*\|\s*([^|]*?)\s*\|\s*$",
    re.M)
SUBAGENT_ROW_RE = re.compile(
    r"^\|\s*([\w_]+)\s*\|\s*(\w+)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|"
    r"\s*([\d.]+)s\s*\|\s*([^|]*?)\s*\|\s*$", re.M)


def _num(text: str) -> int:
    return int(text.replace(",", "").strip() or 0)


@dataclass(frozen=True)
class Step:
    index: int                 # "### Step N" ordinal (per section render)
    seq: int                   # global cN call index
    breadcrumb: tuple[str, ...]  # nest tokens ("main", "A_1", "L1_1", ...)
    tool: str
    arguments: dict
    result_text: str           # verbatim delivered result ("" if absent)
    result_chars: int          # logged delivered size (result line)
    elapsed_s: float
    started_offset_s: float
    status: str                # ok | error | validation_blocked | held_back
    nested_sections: tuple[str, ...]  # explicit '**Nested:**' pointers
    body: str = field(repr=False, default="")

    @property
    def ok(self) -> bool:
        return self.status == "ok"


@dataclass(frozen=True)
class PipelineRow:
    index: int
    tool: str
    pipeline: str              # compacting catalog family (query|analysis)
    native: int
    hardcoded: int
    agentic: int
    verdict: str               # KEEP | DISCARD | SKIP | ...
    section: str               # owning section sid ("" = own lane)


@dataclass(frozen=True)
class SubagentRow:
    tool: str
    verdict: str
    input_chars: int
    output_chars: int
    elapsed_s: float
    section: str


@dataclass(frozen=True)
class SessionHistory:
    session: Path
    nest: tuple[str, ...]      # session's own nest prefix tokens
    steps: tuple[Step, ...]
    pipeline: tuple[PipelineRow, ...]
    subagent: tuple[SubagentRow, ...]
    sections: tuple[tuple[str, str], ...]   # (sid, launcher label)
    prompt_chars: int          # root prompt size when logged in header


def _strip_fence(text: str) -> str:
    lines = text.strip("\n").split("\n")
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip().startswith("```"):
        lines = lines[:-1]
    return "\n".join(lines)


def _is_error_result(text: str) -> bool:
    """Error/refinement payloads never ran the tool pipeline."""
    head = text.lstrip()[:400]
    if not head.startswith("{"):
        return False
    return ('"error"' in head or '"error_code"' in head
            or "REFINEMENT_REQUIRED" in head)


def _parse_step(match: re.Match) -> Step:
    body = match.group(4)
    bracket = match.group(2) or ""
    seq_match = SEQ_TAG_RE.search(bracket)
    seq = int(seq_match.group(1)) if seq_match else 0
    crumb = (bracket[: seq_match.start()].strip(" \u00b7")
             if seq_match else bracket).strip()
    tokens = tuple(t.strip() for t in crumb.split(" - ") if t.strip())
    arguments: dict = {}
    arg_match = ARGS_RE.search(body)
    if arg_match:
        try:
            parsed = json.loads(arg_match.group(1))
            if isinstance(parsed, dict):
                arguments = parsed
        except json.JSONDecodeError:
            pass
    result_text = ""
    res_match = RESULT_DETAILS_RE.search(body)
    if res_match:
        result_text = _strip_fence(res_match.group(1))
    line = RESULT_LINE_RE.search(body)
    result_chars = _num(line.group(1)) if line else len(result_text)
    elapsed = float(line.group(2)) if line and line.group(2) else 0.0
    offset = float(line.group(4)) if line and line.group(4) else 0.0
    head = body[:200]
    if "VALIDATION BLOCKED" in head:
        status = "validation_blocked"
    elif "HELD BACK BY BATCH" in head:
        status = "held_back"
    elif "ERROR" in head or (ERROR_LINE_RE.search(body) and not res_match):
        status = "error"
    elif _is_error_result(result_text):
        status = "error"
    else:
        status = "ok"
    return Step(
        index=int(match.group(1)), seq=seq, breadcrumb=tokens,
        tool=match.group(3), arguments=arguments, result_text=result_text,
        result_chars=result_chars, elapsed_s=elapsed,
        started_offset_s=offset, status=status,
        nested_sections=tuple(NESTED_LINE_RE.findall(body)),
        body=body,
    )


_HISTORY_CACHE: dict[Path, SessionHistory] = {}


def session_history(session: Path) -> SessionHistory:
    session = Path(session)
    if session in _HISTORY_CACHE:
        return _HISTORY_CACHE[session]
    path = session / "run_history.md"
    if not path.exists():
        raise LegacySessionError(f"no run_history.md under {session}")
    text = path.read_text(encoding="utf-8", errors="replace")
    nest_match = NEST_RE.search(text[:2000])
    if not nest_match:
        raise LegacySessionError(
            f"legacy session (no exhaustive '**Nest:**' history): {session}")
    nest = tuple(t.strip() for t in nest_match.group(1).split(" - ")
                 if t.strip())

    steps = sorted((_parse_step(m) for m in STEP_RE.finditer(text)),
                   key=lambda s: (s.seq or 10**9, s.index))

    pipeline: list[PipelineRow] = []
    pipe_head = PIPELINE_HEAD_RE.search(text)
    if pipe_head:
        seg = text[pipe_head.start():]
        nxt = re.search(r"^## (?!Tool Compaction)", seg[1:], re.M)
        seg = seg[: nxt.start() + 1] if nxt else seg
        for m in PIPELINE_ROW_RE.finditer(seg):
            section = m.group(8).strip()
            pipeline.append(PipelineRow(
                index=int(m.group(1)), tool=m.group(2),
                pipeline=m.group(3),
                native=_num(m.group(4)), hardcoded=_num(m.group(5)),
                agentic=_num(m.group(6)), verdict=m.group(7),
                section="" if section in ("\u2014", "-", "") else section,
            ))

    subagent: list[SubagentRow] = []
    sub_head = re.search(r"^## Subagent Summary", text, re.M)
    if sub_head:
        seg = text[sub_head.start():]
        nxt = re.search(r"^## (?!Subagent)", seg[1:], re.M)
        seg = seg[: nxt.start() + 1] if nxt else seg
        for m in SUBAGENT_ROW_RE.finditer(seg):
            if m.group(1).lower() == "tool":
                continue
            section = m.group(6).strip()
            subagent.append(SubagentRow(
                tool=m.group(1), verdict=m.group(2),
                input_chars=_num(m.group(3)), output_chars=_num(m.group(4)),
                elapsed_s=float(m.group(5)),
                section="" if section in ("\u2014", "-", "") else section,
            ))

    sections = tuple((m.group(1), m.group(2))
                     for m in SECTION_HEAD_RE.finditer(text))

    prompt_match = re.search(r"\*\*Prompt(?: chars)?:\*\*\s*([\d,]+)",
                             text[:2000])
    hist = SessionHistory(
        session=session, nest=nest, steps=tuple(steps),
        pipeline=tuple(pipeline), subagent=tuple(subagent),
        sections=sections,
        prompt_chars=_num(prompt_match.group(1)) if prompt_match else 0,
    )
    _HISTORY_CACHE[session] = hist
    return hist


def is_exhaustive(session: Path) -> bool:
    try:
        session_history(session)
        return True
    except LegacySessionError:
        return False
