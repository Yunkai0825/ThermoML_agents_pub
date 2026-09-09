"""
Validation tools for the canonical ID alignment search agent.

MCP-style tools that validate field values against canonical registries
and return confidence scores + suggestions.  These are called by the
dispatcher **after** initial field filling to catch misalignments.

Workflow
--------
1. Alignment agent fills search fields (compounds, properties, etc.)
2. Validator checks each field against the registry:
   - Exact match → PASS (confidence 100)
   - Fuzzy match with score ≥ 80 → PASS with suggestion
   - Fuzzy match 50-79 → WARN: ambiguous, returns top alternatives
   - No match or score < 50 → FAIL: needs escalation
3. Validation report is returned with per-field verdicts
4. If any field FAILs, the dispatcher can:
   a. Let review workers re-examine top results
   b. Escalate to the ThermoML query agent

Public API
----------
- ``validate_all_fields(resolved_query)`` → ValidationReport
- ``validate_field(entity_type, value, db_path)`` → FieldVerdict
- ``validate_bibliography(title_kw, author, doi, db_path)`` → BibVerdict
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Optional

from ThermoML_database_browser.helpers.sqlite_readonly import connect_readonly

from .id_workers import (
    ResolvedID,
    resolve_compound,
    resolve_property,
    resolve_measurement,
    resolve_variable,
    resolve_constraint,
    resolve_phase,
)
from .bibliography_scorer import score_titles


# ── Data classes ──────────────────────────────────────────────────────────

@dataclass
class FieldVerdict:
    """Validation result for a single field."""
    field_name: str
    original_value: str
    status: str                 # "pass", "warn", "fail"
    confidence: int             # 0-100
    best_match: Optional[ResolvedID] = None
    alternatives: list[ResolvedID] = field(default_factory=list)
    message: str = ""

    def to_dict(self) -> dict:
        d = {
            "field_name": self.field_name,
            "original_value": self.original_value,
            "status": self.status,
            "confidence": self.confidence,
            "message": self.message,
        }
        if self.best_match:
            d["best_match"] = self.best_match.to_dict()
        if self.alternatives:
            d["alternatives"] = [a.to_dict() for a in self.alternatives]
        return d


@dataclass
class BibVerdict:
    """Validation result for bibliography fields."""
    title_status: str = "skip"     # "pass", "warn", "fail", "skip"
    title_confidence: int = 0
    title_matches: list[dict] = field(default_factory=list)
    author_status: str = "skip"
    doi_status: str = "skip"
    message: str = ""

    def to_dict(self) -> dict:
        return {
            "title_status": self.title_status,
            "title_confidence": self.title_confidence,
            "title_matches": self.title_matches[:5],
            "author_status": self.author_status,
            "doi_status": self.doi_status,
            "message": self.message,
        }


@dataclass
class ValidationReport:
    """Complete validation report for all fields in a resolved query."""
    field_verdicts: list[FieldVerdict] = field(default_factory=list)
    bib_verdict: Optional[BibVerdict] = None
    overall_status: str = "pass"     # "pass", "warn", "fail"
    needs_escalation: bool = False
    escalation_reason: str = ""

    def to_dict(self) -> dict:
        return {
            "field_verdicts": [v.to_dict() for v in self.field_verdicts],
            "bib_verdict": self.bib_verdict.to_dict() if self.bib_verdict else None,
            "overall_status": self.overall_status,
            "needs_escalation": self.needs_escalation,
            "escalation_reason": self.escalation_reason,
        }


# ── Entity validators ────────────────────────────────────────────────────

_RESOLVER_MAP = {
    "compound": resolve_compound,
    "property": resolve_property,
    "measurement": resolve_measurement,
    "variable": resolve_variable,
    "constraint": resolve_constraint,
    "phase": resolve_phase,
}


def validate_field(entity_type: str, value: str) -> FieldVerdict:
    """Validate a single field value against its canonical registry.

    Returns a FieldVerdict with status, confidence, and alternatives.
    """
    try:
        resolver = _RESOLVER_MAP[entity_type]
    except KeyError as exc:
        raise ValueError(f"Unknown entity type: {entity_type!r}") from exc
    if not isinstance(value, str) or not value:
        raise TypeError("value must be a non-empty string")

    hits = resolver(value, limit=5)

    if not hits:
        return FieldVerdict(
            field_name=entity_type,
            original_value=value,
            status="fail",
            confidence=0,
            message=f"No match found for '{value}' in {entity_type} registry",
        )

    best = hits[0]

    if best.score >= 80:
        return FieldVerdict(
            field_name=entity_type,
            original_value=value,
            status="pass",
            confidence=best.score,
            best_match=best,
            alternatives=hits[1:3],
            message=f"Confident match: {best.display_name} (score={best.score})",
        )

    if best.score >= 50:
        return FieldVerdict(
            field_name=entity_type,
            original_value=value,
            status="warn",
            confidence=best.score,
            best_match=best,
            alternatives=hits[1:5],
            message=(
                f"Ambiguous match for '{value}': top candidate is "
                f"'{best.display_name}' (score={best.score}). "
                f"Alternatives: {', '.join(h.display_name for h in hits[1:3])}"
            ),
        )

    return FieldVerdict(
        field_name=entity_type,
        original_value=value,
        status="fail",
        confidence=best.score,
        best_match=best,
        alternatives=hits[1:5],
        message=(
            f"Low-confidence match for '{value}': "
            f"'{best.display_name}' (score={best.score}). "
            f"Consider rephrasing or using canonical ID."
        ),
    )


def validate_bibliography(title_kw: str = "", author: str = "",
                          doi: str = "", db_path: str = "") -> BibVerdict:
    """Validate bibliography fields against the ref_index.

    For title keywords, uses the bibliography scorer to find matching
    papers by title similarity.
    """
    verdict = BibVerdict()
    if not any((title_kw, author, doi)):
        raise ValueError("At least one bibliography field is required")
    if not isinstance(db_path, str) or not db_path or not os.path.exists(db_path):
        raise FileNotFoundError(f"ThermoML index database not found: {db_path!r}")

    if doi:
        # Check DOI exists in the DB
        db = connect_readonly(db_path)
        try:
            row = db.execute(
                "SELECT doi FROM ref_index WHERE doi = ?", (doi,)
            ).fetchone()
        finally:
            db.close()
        verdict.doi_status = "pass" if row else "warn"

    if author:
        db = connect_readonly(db_path)
        try:
            rows = db.execute(
                "SELECT COUNT(*) FROM ref_index WHERE first_author LIKE ?",
                (f"%{author}%",)
            ).fetchone()
        finally:
            db.close()
        if rows is None:
            raise RuntimeError("Author validation query returned no count row")
        count = rows[0]
        if count > 0:
            verdict.author_status = "pass"
        else:
            verdict.author_status = "warn"

    if title_kw:
        hits = score_titles(title_kw, db_path, limit=10, min_score=40)
        if hits:
            verdict.title_matches = [h.to_dict() for h in hits]
            best_score = hits[0].score
            if best_score >= 80:
                verdict.title_status = "pass"
                verdict.title_confidence = best_score
            elif best_score >= 50:
                verdict.title_status = "warn"
                verdict.title_confidence = best_score
            else:
                verdict.title_status = "fail"
                verdict.title_confidence = best_score
        else:
            verdict.title_status = "fail"
            verdict.title_confidence = 0

    statuses = [verdict.title_status, verdict.author_status, verdict.doi_status]
    if "fail" in statuses:
        verdict.message = "Some bibliography fields could not be validated"
    elif "warn" in statuses:
        verdict.message = "Some bibliography fields are ambiguous"
    else:
        verdict.message = "Bibliography fields validated"

    return verdict


# ── Full-query validator ──────────────────────────────────────────────────

def validate_all_fields(resolved_query, db_path: str = "") -> ValidationReport:
    """Validate all fields in a ResolvedQuery.

    Checks each resolved entity against its registry (re-resolution)
    and validates bibliography fields if present.

    Parameters
    ----------
    resolved_query : ResolvedQuery
        The query to validate (from dispatcher.py).
    db_path : str
        Path to ThermoML_index.db for bibliography validation.
    """
    report = ValidationReport()

    # Validate each resolved entity
    entity_buckets = [
        ("compound", resolved_query.compounds),
        ("property", resolved_query.properties),
        ("measurement", resolved_query.measurements),
        ("variable", resolved_query.variables),
        ("constraint", resolved_query.constraints),
    ]

    for entity_type, items in entity_buckets:
        for item in items:
            verdict = validate_field(entity_type, item.display_name)
            report.field_verdicts.append(verdict)

    # Validate bibliography
    title_kw = " ".join(resolved_query.title_words) if resolved_query.title_words else ""
    author = resolved_query.authors[0] if resolved_query.authors else ""
    doi = resolved_query.dois[0] if resolved_query.dois else ""

    if title_kw or author or doi:
        report.bib_verdict = validate_bibliography(
            title_kw=title_kw, author=author, doi=doi, db_path=db_path
        )

    # Compute overall status
    statuses = [v.status for v in report.field_verdicts]
    if report.bib_verdict:
        statuses.extend([
            report.bib_verdict.title_status,
            report.bib_verdict.author_status,
            report.bib_verdict.doi_status,
        ])
    statuses = [s for s in statuses if s != "skip"]

    if "fail" in statuses:
        report.overall_status = "fail"
    elif "warn" in statuses:
        report.overall_status = "warn"
    else:
        report.overall_status = "pass"

    # Determine escalation need
    fail_count = statuses.count("fail")
    warn_count = statuses.count("warn")
    total = len(statuses) or 1

    if fail_count > 0:
        report.needs_escalation = True
        failed_fields = [v.field_name for v in report.field_verdicts if v.status == "fail"]
        report.escalation_reason = (
            f"{fail_count} field(s) failed validation: {', '.join(failed_fields)}. "
            f"Consider using query agent for disambiguation."
        )
    elif warn_count / total > 0.5:
        report.needs_escalation = True
        report.escalation_reason = (
            f"Too many ambiguous fields ({warn_count}/{total}). "
            f"Query agent may improve result quality."
        )

    # Also check unresolved tokens
    if resolved_query.unresolved:
        report.needs_escalation = True
        report.escalation_reason += (
            f" {len(resolved_query.unresolved)} unresolved token(s): "
            f"{', '.join(resolved_query.unresolved[:5])}"
        )

    return report
