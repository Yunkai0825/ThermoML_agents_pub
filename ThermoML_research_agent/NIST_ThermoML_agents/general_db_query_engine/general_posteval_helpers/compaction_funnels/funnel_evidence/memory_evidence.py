"""Working-memory + final-context evidence."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from funnel_evidence.measures import Measure, measure, thermoml_ids

L1_RECORD_RE = re.compile(r"^### (L1_query_\d+)\s*$", re.M)
_WM_NAMES = ("working_memory.md", "_working_memory.md")


def wm_path(session: Path) -> Path | None:
    for name in _WM_NAMES:
        p = Path(session) / name
        if p.exists():
            return p
    return None


def wm_measure(session: Path) -> Measure:
    p = wm_path(session)
    return measure(p.read_text(encoding="utf-8", errors="replace")) \
        if p else Measure()


@dataclass(frozen=True)
class WmRecord:
    record: str                # "L1_query_N"
    payload: Measure
    fields: dict               # field name -> chars ({} = prose record)
    blocks: tuple              # qualified block ids in core_blocks_found
    text: str                  # serialized payload JSON (verbatim archive)


def wm_records(session: Path) -> tuple[WmRecord, ...]:
    """``### L1_query_N`` archived worker payload records.

    JSON payloads keep their field breakdown; markdown-prose records
    (current WM format) fall back to the whole section text with
    ``fields={}`` so partitioning keeps preferring the dispatch text.
    """
    p = wm_path(session)
    if p is None:
        return ()
    text = p.read_text(encoding="utf-8", errors="replace")
    headings = list(L1_RECORD_RE.finditer(text))
    decoder = json.JSONDecoder()
    out: list[WmRecord] = []
    for i, head in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        blob = text[head.end():end]
        fields = None
        start = blob.find("{")
        if start >= 0:
            try:
                fields, _ = decoder.raw_decode(blob[start:])
            except json.JSONDecodeError:
                fields = None
        if not isinstance(fields, dict):
            prose = blob.strip()
            if prose:
                out.append(WmRecord(record=head.group(1),
                                    payload=measure(prose),
                                    fields={}, blocks=(), text=prose))
            continue
        serialized = json.dumps(fields, ensure_ascii=False,
                                separators=(",", ":"), default=str)
        sizes = {k: (len(v) if isinstance(v, str)
                     else len(json.dumps(v, ensure_ascii=False)))
                 for k, v in fields.items()}
        blocks = []
        for block in fields.get("core_blocks_found") or []:
            if isinstance(block, dict):
                lit = block.get("lit_num_id") or ""
                num = block.get("block_number") or block.get("block") or ""
                if lit and num:
                    blocks.append(f"{lit}::{num}")
                elif num:
                    blocks.append(str(num))
        out.append(WmRecord(record=head.group(1),
                            payload=measure(serialized),
                            fields=sizes, blocks=tuple(blocks),
                            text=serialized))
    return tuple(out)


_CTX_CACHE: dict[Path, frozenset] = {}


def context_ids(session: Path) -> frozenset:
    """IDs in the delivered final full context (authoritative text)."""
    session = Path(session)
    if session not in _CTX_CACHE:
        candidates = [session / "final_full_context.md",
                      session / "final_full_context_R.md"]
        text = ""
        for p in candidates:
            if p.exists():
                text = p.read_text(encoding="utf-8", errors="replace")
                break
        _CTX_CACHE[session] = frozenset(thermoml_ids(text))
    return _CTX_CACHE[session]
