"""result.md envelope evidence — partition by field provenance class.

Every part returns a Measure plus provenance anchors; the ledger comes
from the envelope JSON field AND/OR the split-out "## Data Inspections"
report section (new-format writers pop it out of the blob).
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from framework_registry.agent_registry import (ENVELOPE_FIELD_CLASSES,
                                               FieldClass)
from funnel_evidence.measures import Measure, measure, thermoml_ids

_INSP_ID_RE = re.compile(r"INSP_[0-9a-f]{6,}")


def envelope_blob(path: Path) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    for section in ("## Data Inspections", "## Verdict"):
        if section in text:
            text = text[: text.index(section)]
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end <= start:
        return ""
    return text[start: end + 1]


def ledger_section(path: Path) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    marker = "## Data Inspections"
    if marker not in text:
        return ""
    seg = text[text.index(marker):]
    nxt = re.search(r"(?m)^## (?!Data Inspections)", seg[1:])
    return seg[: nxt.start() + 1] if nxt else seg


_QUESTION_RE = re.compile(
    r"\*\*Question:\*\*\s*(.+?)(?=\n\s*\n|\n\*\*)", re.S)
_Q_CACHE: dict[Path, str] = {}
_FCTX_CACHE: dict[Path, frozenset] = {}


def question_text(session: Path) -> str:
    """The root prompt as recorded in result.md."""
    session = Path(session)
    if session in _Q_CACHE:
        return _Q_CACHE[session]
    text = ""
    path = session / "result.md"
    if path.exists():
        m = _QUESTION_RE.search(
            path.read_text(encoding="utf-8", errors="replace")[:8000])
        if m:
            text = m.group(1).strip()
    _Q_CACHE[session] = text
    return text


def final_context_ids(session: Path) -> frozenset:
    """IDs present in the ACTUAL delivered context text at session end
    (final_full_context*.md) — the honest pool for transient context
    carry (nudges, gate bounces, in-loop renders never archived to WM)."""
    session = Path(session)
    if session in _FCTX_CACHE:
        return _FCTX_CACHE[session]
    ids: set = set()
    for path in sorted(session.glob("final_full_context*.md")):
        ids |= set(thermoml_ids(
            path.read_text(encoding="utf-8", errors="replace")))
    out = frozenset(ids)
    _FCTX_CACHE[session] = out
    return out


@dataclass(frozen=True)
class EnvelopePartition:
    total: Measure
    parts: dict                      # FieldClass -> Measure
    fields: dict                     # FieldClass -> tuple of field names
    inspection_ids: tuple            # INSP_* anchors in the ledger
    answer_text: str
    provenance: tuple                # artifact anchors

    def part(self, field_class: str) -> Measure:
        return self.parts.get(field_class, Measure())


_EMPTY = EnvelopePartition(total=Measure(), parts={}, fields={},
                           inspection_ids=(), answer_text="",
                           provenance=())
_CACHE: dict[Path, EnvelopePartition] = {}


def envelope_partition(session: Path) -> EnvelopePartition:
    session = Path(session)
    if session in _CACHE:
        return _CACHE[session]
    path = session / "result.md"
    blob = envelope_blob(path)
    section = ledger_section(path)
    if not blob and not section:
        _CACHE[session] = _EMPTY
        return _EMPTY

    parts: dict[str, Measure] = {}
    names: dict[str, list[str]] = {}
    answer = ""
    total_chars = 0
    total_ids: set[str] = set()
    prov = [f"result.md::{session.name}"]

    def add(cls: str, text: str, name: str = "") -> None:
        m = measure(text)
        prev = parts.get(cls, Measure())
        parts[cls] = Measure(chars=prev.chars + m.chars,
                             ids=prev.ids | m.ids)
        if name:
            names.setdefault(cls, []).append(name)

    payload = None
    if blob:
        try:
            payload = json.loads(blob)
        except json.JSONDecodeError:
            payload = None
        total_chars += len(blob)
        total_ids |= thermoml_ids(blob)
    if payload is None and blob:
        add(FieldClass.SCAFFOLD, blob)
    elif isinstance(payload, dict):
        answer = payload.get("answer", "")
        answer = answer if isinstance(answer, str) else str(answer)
        add(FieldClass.ANSWER, answer, "answer")
        for k, v in payload.items():
            if k == "answer":
                continue
            text = json.dumps(v, ensure_ascii=False)
            cls = ENVELOPE_FIELD_CLASSES.get(k)
            if cls is None:
                cls = FieldClass.WM
                print(f"warning: unclassified envelope field '{k}' -> wm")
            add(cls, text, k)
    if section:
        add(FieldClass.LEDGER, section, "data_inspections(section)")
        total_chars += len(section)
        total_ids |= thermoml_ids(section)
        prov.append("result.md::## Data Inspections")

    accounted = sum(m.chars for m in parts.values())
    scaffold_pad = max(total_chars - accounted, 0)
    if scaffold_pad:
        prev = parts.get(FieldClass.SCAFFOLD, Measure())
        parts[FieldClass.SCAFFOLD] = Measure(chars=prev.chars + scaffold_pad,
                                             ids=prev.ids)

    ledger_m = parts.get(FieldClass.LEDGER, Measure())
    insp = tuple(sorted(set(_INSP_ID_RE.findall(section or blob or ""))))
    result = EnvelopePartition(
        total=Measure(chars=total_chars, ids=frozenset(total_ids)),
        parts=parts,
        fields={k: tuple(v) for k, v in names.items()},
        inspection_ids=insp,
        answer_text=answer,
        provenance=tuple(prov),
    )
    _CACHE[session] = result
    return result


def partition_payload_text(text: str, provenance: str = "") -> EnvelopePartition:
    """Partition an in-process worker's relay payload (delivered text).

    The relay text is the rendered subagent return; the embedded JSON
    envelope is partitioned by field class, any rendering outside the
    blob counts as SCAFFOLD (wrapper markdown).
    """
    text = text or ""
    if not text:
        return _EMPTY
    start, end = text.find("{"), text.rfind("}")
    blob = text[start: end + 1] if (start >= 0 and end > start) else ""
    payload = None
    if blob:
        try:
            payload = json.loads(blob)
        except json.JSONDecodeError:
            payload = None

    parts: dict[str, Measure] = {}
    names: dict[str, list[str]] = {}
    answer = ""

    def add(cls: str, part_text: str, name: str = "") -> None:
        m = measure(part_text)
        prev = parts.get(cls, Measure())
        parts[cls] = Measure(chars=prev.chars + m.chars, ids=prev.ids | m.ids)
        if name:
            names.setdefault(cls, []).append(name)

    if isinstance(payload, dict) and "answer" in payload:
        answer = payload.get("answer", "")
        answer = answer if isinstance(answer, str) else str(answer)
        add(FieldClass.ANSWER, answer, "answer")
        for k, v in payload.items():
            if k == "answer":
                continue
            part_text = json.dumps(v, ensure_ascii=False)
            cls = ENVELOPE_FIELD_CLASSES.get(k, FieldClass.WM)
            add(cls, part_text, k)
    else:
        # unparseable relay text / error reports ARE the agent-facing
        # reply
        add(FieldClass.ANSWER, text, "answer(text)")
        answer = text
    total = measure(text)
    accounted = sum(m.chars for m in parts.values())
    pad = max(total.chars - accounted, 0)
    if pad:
        prev = parts.get(FieldClass.SCAFFOLD, Measure())
        parts[FieldClass.SCAFFOLD] = Measure(chars=prev.chars + pad,
                                             ids=prev.ids)
    return EnvelopePartition(
        total=total, parts=parts,
        fields={k: tuple(v) for k, v in names.items()},
        inspection_ids=tuple(sorted(set(_INSP_ID_RE.findall(text)))),
        answer_text=answer,
        provenance=(provenance,) if provenance else (),
    )
