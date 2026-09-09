"""Extract ThermoML identifiers from saved prose and JSON artifacts.

Kept with the production workflow code so reporting does not depend on
temporary publication-audit scripts or another checkout.
"""
from __future__ import annotations

import re

GLOBAL_ID_RE = re.compile(r"\bGLOB[A-Za-z0-9]+_\d+(?:_\d+)*\b")

BLOCK_ID_RE = re.compile(r"\b(?:PROP|RXN)block_\d+\b")

LOCAL_ID_RE = re.compile(
    r"\b(?:BLK[A-Za-z0-9]+|DOIcomp(?:Sample)?|L1_query)_\d+(?:_\d+)*\b"
)

PAIR_FIELD_RE = re.compile(
    # same-entry lit→block: the gap may not cross an entry boundary
    # (brace) or another lit field — adjacent JSON entries with
    # "block" ordered before "lit_num_id" would cross-pair otherwise;
    # \\? tolerates escaped-JSON quoting (\"field\": \"value\")
    r'"lit_num_id\\?"\s*:\s*\\?"(GLOBlit_\d+)\\?"'
    r'(?:(?!"lit_num_id)[^{}]){0,700}?'
    r'"(?:block|block_number)\\?"\s*:\s*\\?"((?:PROP|RXN)block_\d+)\\?"',
    re.S,
)

PAIR_FIELD_REV_RE = re.compile(
    # same-entry block→lit (entries that order the block field first)
    r'"(?:block|block_number)\\?"\s*:\s*\\?"((?:PROP|RXN)block_\d+)\\?"'
    r'(?:(?!"(?:block|block_number)\\?"\s*:)[^{}]){0,700}?'
    r'"lit_num_id\\?"\s*:\s*\\?"(GLOBlit_\d+)\\?"',
    re.S,
)

_LIT_MENTION_RE = re.compile(r"\bGLOBlit_\d+\b")

_LINEISH_RE = re.compile(r"\r?\n|\\+n")

_REV_PAIR_RE = re.compile(
    # "PROPblock_11 from GLOBlit_369", "PROPblock_16 (GLOBlit_11337)" —
    # tempered: never cross another id, quote or brace (compact-JSON
    # neighbours would cross-pair)
    r"\b((?:PROP|RXN)block_\d+)\b"
    r"(?:(?!GLOBlit_\d+|(?:PROP|RXN)block_\d+)[^\r\n\"{}]){0,60}?"
    r"\b(GLOBlit_\d+)\b")

def _inline_pairs(text: str) -> set[tuple[str, str]]:
    """Pair block mentions with their literature per line: an adjacent
    FOLLOWING lit binds first ("block from lit" prose), else the nearest
    PRECEDING lit with no other id in between (registry-style
    "lit / DOI / block" lines). Directional-window-only pairing
    mispaired list prose ("PROPblock_16 from GLOBlit_11337,
    PROPblock_3 from GLOBlit_267" must not yield 11337::block_3)."""
    pairs: set[tuple[str, str]] = set()
    for line in _LINEISH_RE.split(text):
        lits = [(m.start(), m.end(), m.group(0))
                for m in _LIT_MENTION_RE.finditer(line)]
        if not lits:
            continue
        blocks = [(m.start(), m.end(), m.group(0))
                  for m in BLOCK_ID_RE.finditer(line)]
        reversed_hits = {m.start(1): (m.group(2), m.group(1))
                         for m in _REV_PAIR_RE.finditer(line)}
        for bs, be, block in blocks:
            hit = reversed_hits.get(bs)
            if hit is not None:
                pairs.add((hit[0], block))
                continue
            best = None
            for ls, le, lit in lits:
                if le > bs or bs - le > 180:
                    continue
                gap = line[le:bs]
                if _LIT_MENTION_RE.search(gap) or BLOCK_ID_RE.search(gap):
                    continue
                if "{" in gap or "}" in gap or '"' in gap:
                    continue        # JSON structure: field rules own it
                if best is None or ls > best[0]:
                    best = (ls, lit)
            if best is not None:
                pairs.add((best[1], block))
    return pairs

def extract_ids(text: str) -> set[str]:
    """Return raw IDs plus unambiguous literature-qualified block IDs."""
    ids = set(GLOBAL_ID_RE.findall(text))
    ids.update(BLOCK_ID_RE.findall(text))
    ids.update(LOCAL_ID_RE.findall(text))
    pairs = set(PAIR_FIELD_RE.findall(text)) | _inline_pairs(text)
    pairs |= {(lit, block)
              for block, lit in PAIR_FIELD_REV_RE.findall(text)}
    ids.update(f"{lit}::{block}" for lit, block in pairs)
    return ids
