"""run_history_detailed.md evidence — the Session Event Log.

Rows: ``| E5 | 19:49:09 | 0.0 | argo | ok | 22,518·999→981 | 9.7 |
`[sid]_[Main]_[A#1]_[Turn#1]_[ReAct]` | claudeopus46 · L0-main · try 1 |``

Provides per-instance argo turns (system/prompt/response sizes), the
per-tool triage argo events (label ends `[Tool#k]_[<tier>]` between a
tool event and its sync_tool_result_recorded hook), and verbatim argo
output text by event number (Agent Outputs section).
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

EVENT_ROW_RE = re.compile(
    r"^\|\s*E(\d+)\s*\|\s*([\d:]+)\s*\|\s*([\d.]+)\s*\|\s*(\w+)\s*\|"
    r"\s*(\w+)\s*\|\s*([^|]*)\|\s*([\d.]*)\s*\|\s*`([^`]+)`\s*\|"
    r"\s*([^|]*?)\s*\|\s*$", re.M)
SIZES_RE = re.compile(r"([\d,]+)\u00b7([\d,]+)\u2192([\d,]+)")
OUT_ONLY_RE = re.compile(r"\u2192([\d,]+)")
VERBATIM_HEAD_RE = re.compile(r"^### E(\d+) \u2014 `([^`]+)`", re.M)


def _num(text: str) -> int:
    return int(text.replace(",", "").strip() or 0)


@dataclass(frozen=True)
class Event:
    index: int
    offset_s: float
    kind: str                  # argo | hook | tool | answer
    status: str
    system: int
    prompt: int
    response: int
    call_s: float
    tokens: tuple[str, ...]    # label tokens without brackets
    detail: str

    @property
    def label(self) -> str:
        return "_".join(f"[{t}]" for t in self.tokens)


_CACHE: dict[Path, tuple[tuple[Event, ...], dict[int, str]]] = {}


def _load(session: Path) -> tuple[tuple[Event, ...], dict[int, str]]:
    session = Path(session)
    if session in _CACHE:
        return _CACHE[session]
    path = session / "run_history_detailed.md"
    text = (path.read_text(encoding="utf-8", errors="replace")
            if path.exists() else "")
    events: list[Event] = []
    for m in EVENT_ROW_RE.finditer(text):
        sizes = m.group(6).strip()
        system = prompt = response = 0
        sm = SIZES_RE.search(sizes)
        if sm:
            system, prompt, response = (_num(sm.group(1)), _num(sm.group(2)),
                                        _num(sm.group(3)))
        else:
            om = OUT_ONLY_RE.search(sizes)
            if om:
                response = _num(om.group(1))
        tokens = tuple(t[1:-1] for t in re.findall(r"\[[^\]]*\]", m.group(8)))
        events.append(Event(
            index=int(m.group(1)), offset_s=float(m.group(3)),
            kind=m.group(4), status=m.group(5),
            system=system, prompt=prompt, response=response,
            call_s=float(m.group(7)) if m.group(7) else 0.0,
            tokens=tokens, detail=m.group(9).strip(),
        ))
    verbatim: dict[int, str] = {}
    heads = list(VERBATIM_HEAD_RE.finditer(text))
    for i, head in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        verbatim[int(head.group(1))] = text[head.end():end]
    data = (tuple(events), verbatim)
    _CACHE[session] = data
    return data


def events(session: Path) -> tuple[Event, ...]:
    return _load(session)[0]


def verbatim_output(session: Path, event_index: int) -> str:
    return _load(session)[1].get(event_index, "")


def triage_events(session: Path) -> list[Event]:
    """Per-tool triage argo calls: argo rows whose label nests a second
    [Tool#j] under a tool activity (the doubled-Tool# signature)."""
    out = []
    for e in events(session):
        if e.kind != "argo":
            continue
        tool_tokens = [t for t in e.tokens if t.startswith("Tool#")]
        if len(tool_tokens) >= 2:
            out.append(e)
    return out


def turn_events(session: Path) -> list[Event]:
    """Instance reasoning turns ([Turn#i] labels)."""
    return [e for e in events(session)
            if e.kind == "argo" and any(t.startswith("Turn#")
                                        for t in e.tokens)]
