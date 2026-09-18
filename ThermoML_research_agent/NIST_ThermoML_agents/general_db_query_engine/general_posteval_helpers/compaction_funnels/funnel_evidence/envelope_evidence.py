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
_RESULT_ROUND_RE = re.compile(r"^result(?:_R([1-9][0-9]*))?\.md$")


def latest_result_path(session: Path) -> Path:
    """Return the newest numeric result round in *session*.

    Round one is stored as ``result.md``; continuations use
    ``result_R2.md``, ``result_R3.md``, and so on. Numeric comparison is
    deliberate so R10 sorts after R9. Returning the round-one path when no
    result exists preserves the former missing-file behaviour.
    """
    session = Path(session)
    fallback = session / "result.md"
    best_path = fallback
    best_round = 1 if fallback.is_file() else -1
    if not session.is_dir():
        return fallback
    for candidate in session.glob("result_R*.md"):
        match = _RESULT_ROUND_RE.fullmatch(candidate.name)
        if match is None or not candidate.is_file():
            continue
        round_number = int(match.group(1))
        if round_number > best_round:
            best_path = candidate
            best_round = round_number
    return best_path


def _file_freshness(path: Path) -> tuple[int, int]:
    """Cheap cache fingerprint that changes on rewrite or replacement."""
    try:
        stat = path.stat()
    except OSError:
        return (-1, -1)
    return (stat.st_mtime_ns, stat.st_size)


def _result_cache_key(path: Path) -> tuple[Path, tuple[int, int], tuple[int, int]]:
    """Key evidence caches by selected round and both persisted surfaces."""
    path = Path(path)
    return (
        path,
        _file_freshness(path),
        _file_freshness(envelope_sidecar_path(path)),
    )


def envelope_sidecar_path(result_path: Path) -> Path:
    """Mirror the live writer's round/benchmark-safe sidecar naming."""
    path = Path(result_path)
    stem = path.stem
    if stem == "result":
        name = "answer_envelope.json"
    elif stem.startswith("result_"):
        name = f"answer_envelope{stem[len('result'):]}.json"
    elif stem.endswith("_result"):
        name = f"{stem[:-len('_result')]}_answer_envelope.json"
    else:
        name = f"{stem}_answer_envelope.json"
    return path.with_name(name)


def _envelope_source(path: Path) -> tuple[str, Path | None]:
    """Read a valid sidecar first, else fall back to legacy embedded JSON."""
    sidecar = envelope_sidecar_path(path)
    if sidecar.exists():
        blob = sidecar.read_text(encoding="utf-8", errors="replace").strip()
        try:
            payload = json.loads(blob)
        except json.JSONDecodeError:
            payload = None
        if isinstance(payload, dict):
            return blob, sidecar
    if not path.exists():
        return "", None
    text = path.read_text(encoding="utf-8", errors="replace")
    for section in ("## Data Inspections", "## Verdict"):
        if section in text:
            text = text[: text.index(section)]
    marker = "## Answer"
    if marker not in text:
        return "", None
    body = text[text.index(marker) + len(marker):].lstrip()
    if body.startswith("```json") or body.startswith("```\n"):
        fence = re.match(
            r"```(?:json)?\s*\n(.*?)\n```", body,
            re.DOTALL | re.IGNORECASE,
        )
        if not fence:
            return "", None
        blob = fence.group(1).strip()
    else:
        if not body.startswith("{"):
            return "", None
        try:
            payload, consumed = json.JSONDecoder().raw_decode(body)
        except json.JSONDecodeError:
            return "", None
        if not isinstance(payload, dict):
            return "", None
        blob = body[:consumed]
    try:
        payload = json.loads(blob)
    except json.JSONDecodeError:
        return "", None
    return (blob, path) if isinstance(payload, dict) else ("", None)


def envelope_blob(path: Path) -> str:
    blob, _ = _envelope_source(path)
    return blob


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
_Q_CACHE: dict[tuple[Path, tuple[int, int], tuple[int, int]], str] = {}
_FCTX_CACHE: dict[Path, frozenset] = {}


def question_text(session: Path) -> str:
    """The prompt recorded in the latest result round."""
    session = Path(session)
    path = latest_result_path(session)
    cache_key = _result_cache_key(path)
    if cache_key in _Q_CACHE:
        return _Q_CACHE[cache_key]
    text = ""
    if path.exists():
        m = _QUESTION_RE.search(
            path.read_text(encoding="utf-8", errors="replace")[:8000])
        if m:
            text = m.group(1).strip()
    _Q_CACHE[cache_key] = text
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
_CACHE: dict[
    tuple[Path, tuple[int, int], tuple[int, int]],
    EnvelopePartition,
] = {}


def envelope_partition(session: Path) -> EnvelopePartition:
    session = Path(session)
    path = latest_result_path(session)
    cache_key = _result_cache_key(path)
    if cache_key in _CACHE:
        return _CACHE[cache_key]
    blob, blob_source = _envelope_source(path)
    section = ledger_section(path)
    if not blob and not section:
        _CACHE[cache_key] = _EMPTY
        return _EMPTY

    parts: dict[str, Measure] = {}
    names: dict[str, list[str]] = {}
    answer = ""
    total_chars = 0
    total_ids: set[str] = set()
    prov = ([f"{blob_source.name}::{session.name}"]
            if blob_source is not None else [])

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
    ledger_in_payload = (
        isinstance(payload, dict)
        and payload.get("data_inspections") not in (None, [], {})
    )
    if section and not ledger_in_payload:
        add(FieldClass.LEDGER, section, "data_inspections(section)")
        total_chars += len(section)
        total_ids |= thermoml_ids(section)
        prov.append(f"{path.name}::## Data Inspections")
    elif section and ledger_in_payload:
        # The Markdown section is a view of the exact sidecar field, not a
        # second evidence payload. Keep its anchor without counting it twice.
        prov.append(f"{path.name}::## Data Inspections (view copy)")

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
    _CACHE[cache_key] = result
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
