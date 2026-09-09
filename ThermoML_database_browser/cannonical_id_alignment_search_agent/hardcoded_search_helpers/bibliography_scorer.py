"""
Bibliography scoring engine — keyword-weighted search across DB fields.

Scores papers from the ThermoML index against user-supplied keywords
using a multi-signal approach, searching across **title**, **compound
names**, **compound system**, and **property names** (not just title).

 1. **Exact phrase match** in combined text → 100
 2. **All-keywords-present** → 85 + bonus for word order
 3. **Partial keyword overlap** → proportional (Jaccard-like)
 4. **Fuzzy per-word match** → SequenceMatcher fallback

Public API
----------
- ``score_titles(keywords, db_path, limit, min_score)`` → list[TitleHit]
- ``search_titles_sql(keywords, db_path, limit)`` → fast SQL pre-filter
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from difflib import SequenceMatcher

from ThermoML_database_browser.helpers.sqlite_readonly import connect_readonly

_STOP_WORDS = frozenset({
    "a", "an", "the", "of", "for", "in", "on", "at", "to", "and",
    "or", "with", "from", "by", "is", "are", "was", "were", "its",
    "between", "as", "up", "into", "through", "over", "under",
})

# ── Data classes ──────────────────────────────────────────────────────────

@dataclass
class TitleHit:
    """A single scored title match."""
    doi: str
    title: str
    first_author: str
    year: int
    journal: str
    score: int           # 0-100
    match_detail: str    # e.g. "all_keywords", "partial_3/5", "fuzzy"
    matched_words: list[str]
    n_blocks: int = 0
    total_datapoints: int = 0

    def to_dict(self) -> dict:
        return {
            "doi": self.doi,
            "title": self.title,
            "first_author": self.first_author,
            "year": self.year,
            "journal": self.journal,
            "score": self.score,
            "match_detail": self.match_detail,
            "matched_words": self.matched_words,
            "n_blocks": self.n_blocks,
            "total_datapoints": self.total_datapoints,
        }


# ── Tokeniser ─────────────────────────────────────────────────────────────

def _tokenise(text: str) -> list[str]:
    """Split text to lowercase words, strip stop-words & punctuation."""
    words = re.findall(r"[a-z0-9][a-z0-9'-]*", text.lower())
    return [w for w in words if w not in _STOP_WORDS and len(w) > 1]


def _fuzzy(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


# ── Core scorer ───────────────────────────────────────────────────────────

def _score_title(title_lower: str, title_tokens: list[str],
                 kw_tokens: list[str], kw_phrase: str) -> tuple[int, str, list[str]]:
    """Score a single title against keyword tokens.

    Returns (score 0-100, match_detail, matched_words).
    """
    if not kw_tokens:
        return (0, "empty", [])

    # Exact phrase match
    if kw_phrase in title_lower:
        return (100, "phrase_exact", list(kw_tokens))

    # Check each keyword token for presence
    matched = []
    unmatched = []
    for kw in kw_tokens:
        if kw in title_lower:
            matched.append(kw)
        else:
            # Fuzzy per-word: check each title word
            best_score = 0.0
            for tw in title_tokens:
                s = _fuzzy(kw, tw)
                if s > best_score:
                    best_score = s
            if best_score >= 0.80:
                matched.append(kw)
            else:
                unmatched.append(kw)

    n_kw = len(kw_tokens)
    n_matched = len(matched)

    if n_matched == 0:
        return (0, "no_match", [])

    if n_matched == n_kw:
        # All keywords present — bonus for adjacency
        base = 85
        # Check if they appear near each other in the title
        positions = []
        for kw in kw_tokens:
            idx = title_lower.find(kw)
            if idx >= 0:
                positions.append(idx)
        if positions:
            span = max(positions) - min(positions)
            # Tighter span → better score
            if span < 60:
                base = 90
            if span < 30:
                base = 95
        return (base, "all_keywords", matched)

    # Partial overlap — proportional
    ratio = n_matched / n_kw
    score = int(40 + ratio * 45)  # range 40-85
    return (score, f"partial_{n_matched}/{n_kw}", matched)


# ── Public API ────────────────────────────────────────────────────────────

def search_titles_sql(keywords: str, db_path: str,
                      limit: int = 200) -> list[dict]:
    """Fast SQL pre-filter: find papers matching ANY keyword in title,
    compound_system, comp_name, or prop_name.

    Returns raw rows as dicts (not scored yet). Used as the first pass
    before ``score_titles`` applies the full scoring.
    """
    kw_tokens = _tokenise(keywords)
    if not kw_tokens:
        return []

    db = connect_readonly(db_path)

    # Build per-keyword LIKE patterns
    like_pats = [f"%{kw}%" for kw in kw_tokens]

    # Title match
    title_clauses = " OR ".join(["title LIKE ?"] * len(kw_tokens))
    # compound_system match (block_index)
    cs_clauses = " OR ".join(["compound_system LIKE ?"] * len(kw_tokens))
    # comp_name match (block_compounds)
    cn_clauses = " OR ".join(["comp_name LIKE ?"] * len(kw_tokens))
    # prop_name match (block_properties)
    pn_clauses = " OR ".join(["prop_name LIKE ?"] * len(kw_tokens))

    # UNION across all keyword sources to collect matching DOIs
    sql = (
        "SELECT r.doi, r.title, r.first_author, r.year, r.journal, "
        "r.n_blocks, r.total_datapoints "
        "FROM ref_index r "
        "WHERE r.doi IN ("
        f"  SELECT doi FROM ref_index WHERE {title_clauses}"
        f"  UNION SELECT doi FROM block_index WHERE {cs_clauses}"
        f"  UNION SELECT doi FROM block_compounds WHERE {cn_clauses}"
        f"  UNION SELECT doi FROM block_properties WHERE {pn_clauses}"
        ") "
        "ORDER BY r.total_datapoints DESC "
        f"LIMIT ?"
    )
    params = like_pats * 4 + [limit]
    rows = db.execute(sql, params).fetchall()
    db.close()

    return [dict(r) for r in rows]


def _fetch_paper_keywords(dois: list[str], db_path: str) -> dict[str, str]:
    """Batch-fetch keyword text (compound_system, comp_name, prop_name)
    for a set of DOIs.

    Returns a dict mapping doi → concatenated keyword text.
    """
    if not dois:
        return {}

    db = connect_readonly(db_path)

    result: dict[str, list[str]] = {}
    placeholders = ",".join("?" for _ in dois)

    # compound_system from block_index
    rows = db.execute(
        f"SELECT doi, GROUP_CONCAT(kw, ' ') AS kw FROM "
        f"(SELECT DISTINCT doi, compound_system AS kw FROM block_index "
        f"WHERE doi IN ({placeholders})) GROUP BY doi",
        dois,
    ).fetchall()
    for r in rows:
        if r['kw']:
            result.setdefault(r['doi'], []).append(r['kw'])

    # comp_name from block_compounds
    rows = db.execute(
        f"SELECT doi, GROUP_CONCAT(kw, ' ') AS kw FROM "
        f"(SELECT DISTINCT doi, comp_name AS kw FROM block_compounds "
        f"WHERE doi IN ({placeholders})) GROUP BY doi",
        dois,
    ).fetchall()
    for r in rows:
        if r['kw']:
            result.setdefault(r['doi'], []).append(r['kw'])

    # prop_name from block_properties
    rows = db.execute(
        f"SELECT doi, GROUP_CONCAT(kw, ' ') AS kw FROM "
        f"(SELECT DISTINCT doi, prop_name AS kw FROM block_properties "
        f"WHERE doi IN ({placeholders})) GROUP BY doi",
        dois,
    ).fetchall()
    for r in rows:
        if r['kw']:
            result.setdefault(r['doi'], []).append(r['kw'])

    db.close()
    return {doi: " ".join(parts) for doi, parts in result.items()}


def score_titles(keywords: str, db_path: str, *,
                 limit: int = 30, min_score: int = 40) -> list[TitleHit]:
    """Score references against keywords using title + DB keyword fields.

    Two-pass approach:
      1. SQL pre-filter across title, compound_system, comp_name, prop_name
      2. Python scoring against combined title + DB keywords text

    Parameters
    ----------
    keywords : str
        Free-text keyword string (e.g. "viscosity ethanol binary mixture").
    db_path : str
        Path to ThermoML_index.db.
    limit : int
        Max results to return.
    min_score : int
        Minimum score threshold.

    Returns
    -------
    list[TitleHit]
        Scored and sorted title matches.
    """
    kw_tokens = _tokenise(keywords)
    if not kw_tokens:
        return []

    kw_phrase = " ".join(kw_tokens)

    # Pass 1: broad SQL pre-filter (now searches multiple DB fields)
    raw = search_titles_sql(keywords, db_path, limit=500)

    # Batch-fetch DB keyword text for all candidate DOIs
    dois = [r['doi'] for r in raw]
    kw_map = _fetch_paper_keywords(dois, db_path)

    # Pass 2: score each candidate against combined text
    hits: list[TitleHit] = []
    for row in raw:
        title = row.get("title", "")
        extra_kw = kw_map.get(row['doi'], "")
        combined = f"{title} {extra_kw}" if extra_kw else title
        combined_lower = combined.lower()
        combined_tokens = _tokenise(combined)

        score, detail, matched = _score_title(
            combined_lower, combined_tokens, kw_tokens, kw_phrase
        )

        if score >= min_score:
            hits.append(TitleHit(
                doi=row["doi"],
                title=title,
                first_author=row.get("first_author", ""),
                year=int(row.get("year", 0)),
                journal=row.get("journal", ""),
                score=score,
                match_detail=detail,
                matched_words=matched,
                n_blocks=int(row.get("n_blocks", 0)),
                total_datapoints=int(row.get("total_datapoints", 0)),
            ))

    # Sort by score desc, then by total_datapoints desc
    hits.sort(key=lambda h: (-h.score, -h.total_datapoints))
    return hits[:limit]
