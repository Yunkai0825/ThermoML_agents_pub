"""reference_stats.md evidence — argo turn ledger (§6), tool results
(§4), and the session wall-clock window."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path

RUN_STARTED_RE = re.compile(r"\*\*Run started:\*\*\s*([\d-]+ [\d:]+)")
# wall time carries thousands commas past 1000 s
WALL_TIME_RE = re.compile(
    r"\*\*Wall time \(at last flush\):\*\*\s*([\d,.]+)\s*s")
ARGO_ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([\w-]+)\s*\|\s*([\w.-]+)\s*\|\s*([\d,]+)\s*\|"
    r"\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d.]+)\s*\|\s*$",
    re.M)
TOOL_ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|.*?"
    r"\|\s*([\d,]+)\s*\|\s*([^|]*?)\s*\|\s*([\d,\u2014\-]*)\s*"
    r"\|\s*([\d.]+)\s*\|\s*$", re.M)


def _num(text: str) -> int:
    cleaned = text.replace(",", "").strip()
    return int(cleaned) if cleaned.isdigit() else 0


@dataclass(frozen=True)
class ArgoRow:
    index: int
    tier: str
    model: str
    system: int
    prompt: int
    context: int
    response: int
    seconds: float


@dataclass(frozen=True)
class ToolRow:
    index: int
    iteration: int
    tool: str
    result_chars: int
    subagent: str
    out_chars: int
    seconds: float


_CACHE: dict[Path, dict] = {}


def _load(session: Path) -> dict:
    session = Path(session)
    if session in _CACHE:
        return _CACHE[session]
    path = session / "reference_stats.md"
    text = (path.read_text(encoding="utf-8", errors="replace")
            if path.exists() else "")
    data: dict = {"window": None, "argo": (), "tools": ()}
    if text:
        started = RUN_STARTED_RE.search(text[:600])
        wall = WALL_TIME_RE.search(text[:600])
        if started and wall:
            begin = datetime.strptime(started.group(1), "%Y-%m-%d %H:%M:%S")
            data["window"] = (begin, begin + timedelta(
                seconds=float(wall.group(1).replace(",", ""))))
        if "## 6." in text:
            seg = text[text.index("## 6."):]
            data["argo"] = tuple(
                ArgoRow(index=int(m.group(1)), tier=m.group(2),
                        model=m.group(3), system=_num(m.group(4)),
                        prompt=_num(m.group(5)), context=_num(m.group(6)),
                        response=_num(m.group(7)),
                        seconds=float(m.group(8)))
                for m in ARGO_ROW_RE.finditer(seg))
        if "## 4." in text:
            seg = text[text.index("## 4."):]
            if "## 5." in seg:
                seg = seg[: seg.index("## 5.")]
            data["tools"] = tuple(
                ToolRow(index=int(m.group(1)), iteration=int(m.group(2)),
                        tool=m.group(3), result_chars=_num(m.group(4)),
                        subagent=m.group(5).strip(),
                        out_chars=_num(m.group(6)),
                        seconds=float(m.group(7)))
                for m in TOOL_ROW_RE.finditer(seg)
                if "TOTAL" not in m.group(3))
    _CACHE[session] = data
    return data


def run_window(session: Path):
    return _load(session)["window"]


def argo_rows(session: Path) -> tuple[ArgoRow, ...]:
    return _load(session)["argo"]


def tool_rows(session: Path) -> tuple[ToolRow, ...]:
    return _load(session)["tools"]
